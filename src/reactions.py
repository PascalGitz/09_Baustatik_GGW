import numpy as np

class Force:
    def __init__(self,  rotation_to_x, position_x, position_y):
        self.rotation = rotation_to_x # Winkel in Bezug auf die X-Achse
        self.position_x = position_x    # Position des Angriffspunkts in X-Richtung
        self.position_y = position_y    # Position des Angriffspunkts in Y-Richtung

    def __str__(self):
        return f"Reaktionskraft: | Winkel zur Horizontalen: {self.rotation} | Position: (x ={self.position_x}, y = {self.position_y})"


class Moment:
    def __init__(self, position_x, position_y):
        self.position_x = position_x  # Position des Moments in X-Richtung
        self.position_y = position_y  # Position des Moments in Y-Richtung

    def __str__(self):
        return f"Reaktionsmoment: | Position: (x = {self.position_x}, y = {self.position_y})"
 