"""
UI components for the Hour Tower game
"""

import tkinter as tk
from .colors import NeonColors

class NeonButton:
    """A neon-styled button for the interface"""
    
    def __init__(self, canvas: tk.Canvas, x: int, y: int, width: int, height: int, 
                 text: str, command, color: str = NeonColors.ORANGE):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.command = command
        self.color = color
        
        # Create button background with glow effect
        self.background = canvas.create_rectangle(
            x, y, x + width, y + height,
            fill=color, outline=NeonColors.WHITE, width=3
        )
        
        # Add glow effect
        self.glow1 = canvas.create_rectangle(
            x - 2, y - 2, x + width + 2, y + height + 2,
            outline=color, width=2, stipple="gray50"
        )
        self.glow2 = canvas.create_rectangle(
            x - 4, y - 4, x + width + 4, y + height + 4,
            outline=color, width=1, stipple="gray25"
        )
        
        # Create button text
        self.text_item = canvas.create_text(
            x + width // 2, y + height // 2,
            text=text, font=("Permanent Marker", 14, "bold"),
            fill=NeonColors.WHITE
        )
        
        # Bind click events
        canvas.tag_bind(self.background, "<Button-1>", self.on_click)
        canvas.tag_bind(self.text_item, "<Button-1>", self.on_click)
    
    def on_click(self, event):
        """Handle button click"""
        if self.command:
            self.command()
    
    def update_text(self, new_text: str):
        """Update button text"""
        self.canvas.itemconfig(self.text_item, text=new_text)

class GameTitle:
    """Main title component with glow effects"""
    
    def __init__(self, canvas: tk.Canvas, x: int, y: int):
        self.canvas = canvas
        self.x = x
        self.y = y
        
        # Title glow effects
        self.title_glow1 = canvas.create_text(
            x, y, text="HOUR TOWER",
            font=("Permanent Marker", 36, "bold"),
            fill=NeonColors.DEEP_PURPLE
        )
        self.title_glow2 = canvas.create_text(
            x, y, text="HOUR TOWER",
            font=("Permanent Marker", 36, "bold"),
            fill=NeonColors.DEEP_PURPLE, stipple="gray50"
        )
        
        # Main title
        self.title = canvas.create_text(
            x, y, text="HOUR TOWER",
            font=("Permanent Marker", 36, "bold"),
            fill=NeonColors.WHITE
        )

class ScoreDisplay:
    """Score display component"""
    
    def __init__(self, canvas: tk.Canvas, x: int, y: int):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.score = 0
        
        # Create score text
        self.score_text = canvas.create_text(
            x, y, text="Score: 0",
            font=("Permanent Marker", 18, "bold"),
            fill=NeonColors.GOLDEN_YELLOW
        )
    
    def update_score(self, new_score: int):
        """Update the displayed score"""
        self.score = new_score
        self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
    
    def reset(self):
        """Reset score to 0"""
        self.update_score(0)

class MessageDisplay:
    """Temporary message display component"""
    
    def __init__(self, canvas: tk.Canvas, x: int, y: int):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.current_message = None
    
    def show_message(self, text: str, color: str = NeonColors.HOT_MAGENTA, duration: int = 2000):
        """Show a temporary message"""
        # Remove any existing message
        if self.current_message:
            self.canvas.delete(self.current_message)
        
        # Create new message
        self.current_message = self.canvas.create_text(
            self.x, self.y, text=text,
            font=("Permanent Marker", 24, "bold"),
            fill=color
        )
        
        # Remove message after duration
        self.canvas.after(duration, self.clear_message)
    
    def clear_message(self):
        """Clear the current message"""
        if self.current_message:
            self.canvas.delete(self.current_message)
            self.current_message = None
    
    def show_error(self, text: str = "Try Again!"):
        """Show error message"""
        self.show_message(text, NeonColors.HOT_MAGENTA, 2000)
    
    def show_success(self, text: str = "Great Job!"):
        """Show success message"""
        self.show_message(text, NeonColors.LIME_GREEN, 2000)
    
    def show_victory(self, text: str = "AMAZING! Clock Complete!"):
        """Show victory message"""
        self.show_message(text, NeonColors.LIME_GREEN, 3000) 