import numpy as np

class Force:
    def __init__(self, magnitude, rotation_to_x, position_x, position_y):
        self.magnitude = magnitude  # Kraftbetrag 
        self.rotation = rotation_to_x # Winkel in Bezug auf die X-Achse
        self.magnitude_x = magnitude * np.cos(np.radians(rotation_to_x))
        self.magnitude_y = magnitude * np.sin(np.radians(rotation_to_x))
        self.position_x = position_x    # Position des Angriffspunkts in X-Richtung
        self.position_y = position_y    # Position des Angriffspunkts in Y-Richtung

    def __str__(self):
        return f"Kraft: (F_x = {round(self.magnitude_x,1)}, F_y = {round(self.magnitude_y)}) | Position: (x ={self.position_x}, y = {self.position_y})"


class Moment:
    def __init__(self, magnitude, position_x, position_y):
        self.magnitude = magnitude    # Betrag des Moments
        self.position_x = position_x  # Position des Moments in X-Richtung
        self.position_y = position_y  # Position des Moments in Y-Richtung

    def __str__(self):
        return f"Moment: (M = {round(self.magnitude, 1)}) | Position: (x = {self.position_x}, y = {self.position_y})"
