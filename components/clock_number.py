"""
Draggable clock number component
"""

import tkinter as tk
from .colors import NeonColors

class ClockNumber:
    """Represents a draggable number on the clock"""
    
    def __init__(self, canvas: tk.Canvas, number: int, x: int, y: int, color: str):
        self.canvas = canvas
        self.number = number
        self.x = x
        self.y = y
        self.color = color
        self.dragging = False
        self.drag_offset_x = 0
        self.drag_offset_y = 0
        
        # Create the number circle with glow effect
        self.circle = canvas.create_oval(
            x - 25, y - 25, x + 25, y + 25,
            fill=color, outline=NeonColors.WHITE, width=3
        )
        
        # Add glow effect (multiple outline layers)
        self.glow1 = canvas.create_oval(
            x - 28, y - 28, x + 28, y + 28,
            outline=color, width=2, stipple="gray50"
        )
        self.glow2 = canvas.create_oval(
            x - 31, y - 31, x + 31, y + 31,
            outline=color, width=1, stipple="gray25"
        )
        
        # Create the number text
        self.text = canvas.create_text(
            x, y, text=str(number), font=("Permanent Marker", 20, "bold"),
            fill=NeonColors.WHITE
        )
        
        # Bind mouse events
        canvas.tag_bind(self.circle, "<Button-1>", self.start_drag)
        canvas.tag_bind(self.text, "<Button-1>", self.start_drag)
    
    def start_drag(self, event):
        """Start dragging the number"""
        self.dragging = True
        self.drag_offset_x = event.x - self.x
        self.drag_offset_y = event.y - self.y
        self.canvas.tag_raise(self.circle)
        self.canvas.tag_raise(self.text)
        self.canvas.tag_raise(self.glow1)
        self.canvas.tag_raise(self.glow2)
    
    def drag(self, event):
        """Handle dragging motion"""
        if self.dragging:
            new_x = event.x - self.drag_offset_x
            new_y = event.y - self.drag_offset_y
            
            # Move all elements
            self.canvas.coords(self.circle, new_x - 25, new_y - 25, new_x + 25, new_y + 25)
            self.canvas.coords(self.glow1, new_x - 28, new_y - 28, new_x + 28, new_y + 28)
            self.canvas.coords(self.glow2, new_x - 31, new_y - 31, new_x + 31, new_y + 31)
            self.canvas.coords(self.text, new_x, new_y)
            
            self.x = new_x
            self.y = new_y
    
    def stop_drag(self):
        """Stop dragging the number"""
        self.dragging = False
    
    def remove(self):
        """Remove the number from the canvas"""
        self.canvas.delete(self.circle)
        self.canvas.delete(self.glow1)
        self.canvas.delete(self.glow2)
        self.canvas.delete(self.text)
    
    def bounce_back(self, original_x: int, original_y: int):
        """Animate bouncing back to original position"""
        self.x = original_x
        self.y = original_y
        self.canvas.coords(self.circle, original_x - 25, original_y - 25, original_x + 25, original_y + 25)
        self.canvas.coords(self.glow1, original_x - 28, original_y - 28, original_x + 28, original_y + 28)
        self.canvas.coords(self.glow2, original_x - 31, original_y - 31, original_x + 31, original_y + 31)
        self.canvas.coords(self.text, original_x, original_y) 