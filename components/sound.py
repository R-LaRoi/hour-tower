"""
Sound effects management for the Hour Tower game
"""

class SoundEffects:
    """Simple sound effect simulation"""
    
    def __init__(self):
        self.enabled = True
    
    def play_success(self):
        """Play success sound effect"""
        if self.enabled:
            # In a real implementation, this would play a chime sound
            print("🎵 Success chime!")
    
    def play_error(self):
        """Play error sound effect"""
        if self.enabled:
            # In a real implementation, this would play a gentle error sound
            print("🔔 Gentle error sound!")
    
    def play_victory(self):
        """Play victory sound effect"""
        if self.enabled:
            print("🎉 Victory fanfare!")
    
    def toggle(self) -> str:
        """Toggle sound effects on/off"""
        self.enabled = not self.enabled
        return "ON" if self.enabled else "OFF"
    
    def is_enabled(self) -> bool:
        """Check if sound is enabled"""
        return self.enabled 