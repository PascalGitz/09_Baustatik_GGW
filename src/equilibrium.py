import numpy as np
from actions_on_structures import Force, Moment


class Equilibrium:
    def __init__(self, forces=None, moments=None):
        self.forces = forces  # Liste der Kräfte
        self.moments = moments  # Liste der Momente

    def calculate_resultant_force(self):
        if self.forces != None:
            resultant_x = sum(force.magnitude_x for force in self.forces)
            resultant_y = sum(force.magnitude_y for force in self.forces)
            resultant_angle = np.arctan2(resultant_y, resultant_x)  # Verwenden Sie np.arctan2, um den Winkel korrekt zu berechnen
            resultant_force = Force(np.sqrt(resultant_x**2 + resultant_y**2), resultant_angle, 0, 0)
            return resultant_force
        
    def calculate_resultant_moment(self):
        if self.moments != None:
            resultant_moment = sum(moment.magnitude for moment in self.moments)
        if self.moments == None:
            resultant_moment = 0
            for force in self.forces:
                moment = force.magnitude_x * force.position_y + force.magnitude_y * force.position_x
                resultant_moment += moment
            resultant_moment_object = Moment(resultant_moment, 0, 0)
            return resultant_moment_object

