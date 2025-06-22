"""
Hour Tower - Clock Learning Game
Main application file that brings together all components
"""

import tkinter as tk
from tkinter import messagebox

# Import all components
from components.colors import NeonColors
from components.sound import SoundEffects
from components.clock_face import ClockFace
from components.tower import ClockTower
from components.ui import NeonButton, GameTitle, ScoreDisplay, MessageDisplay
from components.game_logic import GameLogic

class HourTowerGame:
    """Main game application that orchestrates all components"""
    
    def __init__(self):
        # Initialize main window
        self.root = tk.Tk()
        self.root.title("Hour Tower - Clock Learning Game")
        self.root.configure(bg=NeonColors.BLACK)
        self.root.minsize(800, 600)
        
        # Create main canvas
        self.canvas = tk.Canvas(
            self.root, width=800, height=600,
            bg=NeonColors.BLACK, highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Initialize components
        self.initialize_components()
        
        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        
        # Start the game
        self.game_logic.start_new_game()
    
    def initialize_components(self):
        """Initialize all game components"""
        # Create UI components
        self.title = GameTitle(self.canvas, 400, 40)
        self.score_display = ScoreDisplay(self.canvas, 325, 520)
        self.message_display = MessageDisplay(self.canvas, 325, 220)
        
        # Create sound effects
        self.sound_effects = SoundEffects()
        
        # Create game area components - Adjusted vertical positioning
        self.clock_face = ClockFace(self.canvas, 325, 325, 180)
        self.tower = ClockTower(self.canvas, 620, 80, 160, 450)
        
        # Create control buttons, centered below the score
        button_width = 120
        button_padding = 20
        total_button_width = (button_width * 2) + button_padding
        start_x = 325 - (total_button_width // 2)

        self.reset_button = NeonButton(
            self.canvas, start_x, 550, button_width, 40, "RESET GAME",
            self.reset_game, NeonColors.ORANGE
        )
        
        self.sound_button = NeonButton(
            self.canvas, start_x + button_width + button_padding, 550, button_width, 40, "🔊 SOUND ON",
            self.toggle_sound, NeonColors.DEEP_PURPLE
        )
        
        # Create game logic
        self.game_logic = GameLogic(
            self.canvas, self.clock_face, self.tower, 
            self.sound_effects, self.message_display
        )
    
    def on_drag(self, event):
        """Handle drag events"""
        numbers = self.game_logic.get_numbers()
        for number in numbers:
            number.drag(event)
    
    def on_release(self, event):
        """Handle mouse release events"""
        numbers = self.game_logic.get_numbers()
        for number in numbers:
            if number.dragging:
                number.stop_drag()
                
                # Handle number placement
                success = self.game_logic.handle_number_placement(number, number.x, number.y)
                
                # Update score display
                if success:
                    self.score_display.update_score(self.game_logic.get_score())
                break
    
    def reset_game(self):
        """Reset the game"""
        self.game_logic.reset_game()
        self.score_display.reset()
    
    def toggle_sound(self):
        """Toggle sound effects on/off"""
        status = self.sound_effects.toggle()
        self.sound_button.update_text(f"🔊 SOUND {status}")
    
    def run(self):
        """Start the game"""
        try:
            self.root.mainloop()
        except Exception as e:
            print(f"Error running Hour Tower: {e}")
            messagebox.showerror("Error", f"Failed to run Hour Tower: {e}")

def main():
    """Main entry point"""
    try:
        game = HourTowerGame()
        game.run()
    except Exception as e:
        print(f"Error starting Hour Tower: {e}")
        messagebox.showerror("Error", f"Failed to start Hour Tower: {e}")

if __name__ == "__main__":
    main() 