"""
Game logic and state management for Hour Tower
"""

import random
import math
from typing import List, Tuple
from .colors import NeonColors
from .clock_number import ClockNumber

class GameLogic:
    """Handles game logic and state management"""
    
    def __init__(self, canvas, clock_face, tower, sound_effects, message_display):
        self.canvas = canvas
        self.clock_face = clock_face
        self.tower = tower
        self.sound_effects = sound_effects
        self.message_display = message_display
        
        self.numbers = []
        self.original_positions = []
        self.score = 0
        self.game_complete = False
    
    def start_new_game(self):
        """Start a new game with random number placement"""
        # Clear existing numbers
        for number in self.numbers:
            number.remove()
        self.numbers.clear()
        self.original_positions.clear()
        
        # Reset game state
        self.score = 0
        self.game_complete = False
        
        # Get clock center for positioning numbers
        cx = self.clock_face.center_x
        cy = self.clock_face.center_y

        # Create random positions for numbers 1-12
        colors = NeonColors.get_neon_palette()
        for i in range(12):
            # Random position around the clock, ensuring visibility
            is_valid_position = False
            x, y = 0, 0
            while not is_valid_position:
                angle = random.uniform(0, 2 * math.pi)
                distance = random.uniform(220, 260) 
                x = cx + distance * math.cos(angle)
                y = cy + distance * math.sin(angle)
                
                # Check if the position is valid (not overlapping tower or buttons)
                if x > 30 and x < 570 and y > 80 and y < 480:
                    is_valid_position = True
            
            color = NeonColors.get_color_by_index(i)
            number = ClockNumber(self.canvas, i + 1, x, y, color)
            self.numbers.append(number)
            self.original_positions.append((x, y))
    
    def handle_number_placement(self, number: ClockNumber, x: int, y: int) -> bool:
        """Handle placing a number on the clock"""
        # Check if number is placed correctly
        if self.clock_face.check_placement(number.number, x, y):
            # Correct placement
            if self.clock_face.place_number(number.number, x, y):
                # Remove from draggable numbers
                index = self.numbers.index(number)
                number.remove()
                self.numbers.pop(index)
                self.original_positions.pop(index)
                
                # Update score and progress
                self.score += 10
                self.tower.add_progress()
                
                # Play success sound
                self.sound_effects.play_success()
                
                # Show success message
                self.message_display.show_success("Great Job!")
                
                # Check if game is complete
                if len(self.numbers) == 0:
                    self.game_complete = True
                    self.sound_effects.play_victory()
                    self.message_display.show_victory()
                
                return True
        else:
            # Incorrect placement
            self.clock_face.wiggle_hands()
            index = self.numbers.index(number)
            number.bounce_back(self.original_positions[index][0], self.original_positions[index][1])
            self.sound_effects.play_error()
            self.message_display.show_error()
            return False
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.score = 0
        self.game_complete = False
        
        # Reset clock face
        self.clock_face.reset()
        
        # Reset tower
        self.tower.reset()
        
        # Start new game
        self.start_new_game()
    
    def get_score(self) -> int:
        """Get current score"""
        return self.score
    
    def is_game_complete(self) -> bool:
        """Check if game is complete"""
        return self.game_complete
    
    def get_remaining_numbers(self) -> int:
        """Get number of remaining numbers to place"""
        return len(self.numbers)
    
    def get_numbers(self) -> List[ClockNumber]:
        """Get list of current draggable numbers"""
        return self.numbers.copy() 