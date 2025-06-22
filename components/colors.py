"""
Neon color palette for Lite-Brite aesthetic
"""

class NeonColors:
    """Neon color palette for Lite-Brite aesthetic"""
    # New palette based on the user's image
    DEEP_PURPLE = "#4B00FF"
    HOT_MAGENTA = "#E600FF"
    GOLDEN_YELLOW = "#FFC200"

    # Original colors for UI elements
    ELECTRIC_BLUE = "#00FFFF"
    LIME_GREEN = "#32CD32"
    ORANGE = "#FF4500"
    
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    
    @classmethod
    def get_neon_palette(cls) -> list[str]:
        """Get the full neon color palette for the numbers"""
        return [cls.DEEP_PURPLE, cls.HOT_MAGENTA, cls.GOLDEN_YELLOW]
    
    @classmethod
    def get_color_by_index(cls, index: int) -> str:
        """Get a color from the palette by index"""
        colors = cls.get_neon_palette()
        return colors[index % len(colors)] 