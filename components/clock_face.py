"""
Clock face component with positions for numbers
"""

import tkinter as tk
import math
from .colors import NeonColors

class ClockFace:
    """The main clock face with positions for numbers"""
    
    def __init__(self, canvas: tk.Canvas, center_x: int, center_y: int, radius: int = 200):
        self.canvas = canvas
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.positions = []
        self.placed_numbers = {}
        
        # Create clock outline with glow effect
        self.clock_outline = canvas.create_oval(
            center_x - radius, center_y - radius,
            center_x + radius, center_y + radius,
            outline=NeonColors.WHITE, width=4
        )
        
        # Add glow effect to clock
        self.clock_glow1 = canvas.create_oval(
            center_x - radius - 3, center_y - radius - 3,
            center_x + radius + 3, center_y + radius + 3,
            outline=NeonColors.DEEP_PURPLE, width=2, stipple="gray50"
        )
        self.clock_glow2 = canvas.create_oval(
            center_x - radius - 6, center_y - radius - 6,
            center_x + radius + 6, center_y + radius + 6,
            outline=NeonColors.DEEP_PURPLE, width=1, stipple="gray25"
        )
        
        # Create center dot
        self.center_dot = canvas.create_oval(
            center_x - 8, center_y - 8, center_x + 8, center_y + 8,
            fill=NeonColors.WHITE, outline=NeonColors.DEEP_PURPLE, width=2
        )
        
        # Create clock hands
        self.hour_hand = canvas.create_line(
            center_x, center_y, center_x, center_y - 60,
            fill=NeonColors.HOT_MAGENTA, width=6, capstyle=tk.ROUND
        )
        self.minute_hand = canvas.create_line(
            center_x, center_y, center_x, center_y - 90,
            fill=NeonColors.LIME_GREEN, width=4, capstyle=tk.ROUND
        )
        
        # Create 12 positions for numbers
        self.create_number_positions()
    
    def create_number_positions(self):
        """Create the 12 circular positions around the clock"""
        # Define the correct number positions around a clock face
        # 12 at top, 1 at 1 o'clock, 2 at 2 o'clock, etc.
        number_positions = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        
        for i in range(12):
            angle = i * 30 - 90  # Start at 12 o'clock position
            angle_rad = math.radians(angle)
            
            x = self.center_x + (self.radius - 40) * math.cos(angle_rad)
            y = self.center_y + (self.radius - 40) * math.sin(angle_rad)
            
            # Create position circle with subtle glow
            position_circle = self.canvas.create_oval(
                x - 20, y - 20, x + 20, y + 20,
                outline=NeonColors.DEEP_PURPLE, width=2, stipple="gray75"
            )
            
            self.positions.append({
                'number': number_positions[i],  # Use the correct number for this position
                'x': x,
                'y': y,
                'circle': position_circle,
                'occupied': False
            })
    
    def check_placement(self, number: int, x: int, y: int) -> bool:
        """Check if a number is placed in the correct position"""
        for position in self.positions:
            if position['number'] == number:
                distance = math.sqrt((x - position['x'])**2 + (y - position['y'])**2)
                return distance < 30  # Within 30 pixels
        return False
    
    def place_number(self, number: int, x: int, y: int) -> bool:
        """Place a number in its correct position"""
        for position in self.positions:
            if position['number'] == number and not position['occupied']:
                # Remove the position circle
                self.canvas.delete(position['circle'])
                
                # Create the placed number with glow effect
                placed_circle = self.canvas.create_oval(
                    position['x'] - 25, position['y'] - 25,
                    position['x'] + 25, position['y'] + 25,
                    fill=NeonColors.DEEP_PURPLE, outline=NeonColors.WHITE, width=3
                )
                
                placed_text = self.canvas.create_text(
                    position['x'], position['y'], text=str(number),
                    font=("Permanent Marker", 24, "bold"), fill=NeonColors.WHITE
                )
                
                position['occupied'] = True
                self.placed_numbers[number] = {
                    'circle': placed_circle,
                    'text': placed_text
                }
                return True
        return False
    
    def wiggle_hands(self):
        """Animate clock hands wiggling for incorrect placement"""
        def wiggle_step(step=0):
            if step < 6:
                angle = math.sin(step * 0.5) * 5
                angle_rad = math.radians(angle)
                
                # Wiggle hour hand
                end_x = self.center_x + 60 * math.sin(angle_rad)
                end_y = self.center_y - 60 * math.cos(angle_rad)
                self.canvas.coords(self.hour_hand, self.center_x, self.center_y, end_x, end_y)
                
                # Wiggle minute hand
                end_x = self.center_x + 90 * math.sin(angle_rad)
                end_y = self.center_y - 90 * math.cos(angle_rad)
                self.canvas.coords(self.minute_hand, self.center_x, self.center_y, end_x, end_y)
                
                self.canvas.after(100, lambda: wiggle_step(step + 1))
            else:
                # Reset hands to normal position
                self.canvas.coords(self.hour_hand, self.center_x, self.center_y, self.center_x, self.center_y - 60)
                self.canvas.coords(self.minute_hand, self.center_x, self.center_y, self.center_x, self.center_y - 90)
        
        wiggle_step()
    
    def reset(self):
        """Reset the clock face to initial state"""
        # Clear placed numbers
        for position in self.positions:
            if position['occupied']:
                self.canvas.delete(self.placed_numbers[position['number']]['circle'])
                self.canvas.delete(self.placed_numbers[position['number']]['text'])
                position['occupied'] = False
        
        self.placed_numbers.clear()
        
        # Recreate position circles
        for position in self.positions:
            position['circle'] = self.canvas.create_oval(
                position['x'] - 20, position['y'] - 20,
                position['x'] + 20, position['y'] + 20,
                outline=NeonColors.DEEP_PURPLE, width=2, stipple="gray75"
            ) 