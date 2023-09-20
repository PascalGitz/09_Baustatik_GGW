import numpy as np
import sympy as sp

class Force:
    def __init__(self, rotation_to_x, position_x, position_y):
        self.magnitude = sp.Symbol(f'R_{position_x, position_y, rotation_to_x}') #Die Stärke wird als Symbol eingeführt um nach diesen zu solven
        self.magnitude_x = self.magnitude *np.round(np.cos(np.radians(rotation_to_x)),1)
        self.magnitude_y = self.magnitude *np.round(np.sin(np.radians(rotation_to_x)),1)
        self.rotation = rotation_to_x  # Winkel in Bezug auf die X-Achse
        self.position_x = position_x   # Position des Angriffspunkts in X-Richtung
        self.position_y = position_y    # Position des Angriffspunkts in Y-Richtung

    def __str__(self):
        return f"Reaktionskraft: | Winkel zur Horizontalen: {self.rotation} | Position: (x ={self.position_x}, y = {self.position_y})"


class Moment:
    def __init__(self, position_x, position_y):
        self.magnitude = sp.Symbol(f'M_{position_x, position_y}')
        self.position_x = position_x  # Position des Moments in X-Richtung
        self.position_y = position_y  # Position des Moments in Y-Richtung

    def __str__(self):
        return f"Reaktionsmoment: | Position: (x = {self.position_x}, y = {self.position_y})"
  