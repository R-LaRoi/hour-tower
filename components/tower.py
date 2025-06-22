"""
Clock tower building component
"""

import tkinter as tk
from .colors import NeonColors

class TowerBlock:
    """Represents a block in the clock tower"""
    
    def __init__(self, canvas: tk.Canvas, x: int, y: int, width: int, height: int, color: str):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        
        # Create block with glow effect
        self.rect = canvas.create_rectangle(
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

class ClockTower:
    """The clock tower building area"""
    
    def __init__(self, canvas: tk.Canvas, x: int, y: int, width: int, height: int):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.blocks = []
        self.progress = 0
        self.max_progress = 12  # Need 12 correct answers to complete a block
        
        # Create tower background
        self.background = canvas.create_rectangle(
            x, y, x + width, y + height,
            fill=NeonColors.BLACK, outline=NeonColors.DEEP_PURPLE, width=2
        )
        
        # Create tower title
        self.title = canvas.create_text(
            x + width // 2, y + 30,
            text="CLOCK TOWER", font=("Permanent Marker", 16, "bold"),
            fill=NeonColors.WHITE
        )
        
        # Create progress bar
        self.progress_bg = canvas.create_rectangle(
            x + 20, y + 60, x + width - 20, y + 80,
            fill=NeonColors.BLACK, outline=NeonColors.WHITE, width=2
        )
        self.progress_fill = canvas.create_rectangle(
            x + 22, y + 62, x + 22, y + 78,
            fill=NeonColors.LIME_GREEN, outline=""
        )
        
        # Create progress text
        self.progress_text = canvas.create_text(
            x + width // 2, y + 100,
            text="0/12 Numbers Placed", font=("Permanent Marker", 12, "bold"),
            fill=NeonColors.WHITE
        )
    
    def add_progress(self):
        """Add progress toward completing a tower block"""
        self.progress += 1
        progress_ratio = self.progress / self.max_progress
        
        # Update progress bar
        fill_width = int((self.width - 44) * progress_ratio)
        self.canvas.coords(self.progress_fill, 
                          self.x + 22, self.y + 62,
                          self.x + 22 + fill_width, self.y + 78)
        
        # Update progress text
        self.canvas.itemconfig(self.progress_text, 
                              text=f"{self.progress}/{self.max_progress} Numbers Placed")
        
        # Check if block is complete
        if self.progress >= self.max_progress:
            self.add_block()
            self.progress = 0
            self.canvas.coords(self.progress_fill, self.x + 22, self.y + 62, self.x + 22, self.y + 78)
            self.canvas.itemconfig(self.progress_text, text="0/12 Numbers Placed")
    
    def add_block(self):
        """Add a new block to the tower"""
        block_y = self.y + self.height - 40 - (len(self.blocks) * 40)
        if block_y > self.y + 120:  # Keep space for title and progress
            colors = NeonColors.get_neon_palette()
            color = colors[len(self.blocks) % len(colors)]
            
            block = TowerBlock(self.canvas, self.x + 20, block_y, self.width - 40, 35, color)
            self.blocks.append(block)
            
            # Add bell to the top if this is the first block
            if len(self.blocks) == 1:
                self.add_bell(block_y - 30)
    
    def add_bell(self, y_pos: int):
        """Add a bell to the top of the tower"""
        bell_x = self.x + self.width // 2
        bell_y = y_pos
        
        # Bell body
        self.bell = self.canvas.create_oval(
            bell_x - 15, bell_y, bell_x + 15, bell_y + 30,
            fill=NeonColors.GOLDEN_YELLOW, outline=NeonColors.WHITE, width=2
        )
        
        # Bell top
        self.bell_top = self.canvas.create_oval(
            bell_x - 8, bell_y - 8, bell_x + 8, bell_y + 8,
            fill=NeonColors.ORANGE, outline=NeonColors.WHITE, width=2
        )
    
    def reset(self):
        """Reset the tower to initial state"""
        # Remove all blocks
        for block in self.blocks:
            self.canvas.delete(block.rect)
            self.canvas.delete(block.glow1)
            self.canvas.delete(block.glow2)
        
        self.blocks.clear()
        
        # Reset progress
        self.progress = 0
        self.canvas.coords(self.progress_fill, self.x + 22, self.y + 62, self.x + 22, self.y + 78)
        self.canvas.itemconfig(self.progress_text, text="0/12 Numbers Placed")
        
        # Remove bell if it exists
        if hasattr(self, 'bell'):
            self.canvas.delete(self.bell)
            self.canvas.delete(self.bell_top)
            delattr(self, 'bell')
            delattr(self, 'bell_top') 