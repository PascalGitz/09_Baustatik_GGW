import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import actions as ac
import reactions as re


class System:
    def __init__(self, actionforces=None, actionmoments=None, reactionforces=None, reactionmoments=None):
        self.actionforces = actionforces
        self.actionmoments = actionmoments
        self.reactionforces = reactionforces
        self.reactionmoments = reactionmoments

    # def calculate_resultant_force(self):
    #     if self.actionforces != None:
    #         resultant_x = sum(actionforces.magnitude_x for actionforces in self.actionforces)
    #         resultant_y = sum(actionforces.magnitude_y for actionforces in self.actionforces)
    #         resultant_angle = np.arctan2(resultant_y, resultant_x)  # Verwenden Sie np.arctan2, um den Winkel korrekt zu berechnen
    #         resultant_force = ac.Force(np.sqrt(resultant_x**2 + resultant_y**2), resultant_angle, 0, 0)
    #         return resultant_force

        
    # def calculate_resultant_moment(self):
    #     if self.actionmoments != None:
    #         resultant_moment = sum(actionmoments.magnitude for actionmoments in self.actionmoments)
    #     if self.actionmoments == None:
    #         resultant_moment = 0
    #         for actionforce in self.actionforces:
    #             moment = actionforce.magnitude_x * actionforce.position_y + actionforce.magnitude_y * actionforce.position_x
    #             resultant_moment += moment
    #         resultant_moment_object = ac.Moment(resultant_moment, 0, 0)
    #         return resultant_moment_object
        
    def calculate_reaction_force(self):
            # Zuerst werden alle Einwirkungen in Variablen gespeichert:
            forces_x = np.array([actionforces.magnitude_x for actionforces in self.actionforces])
            forces_y = np.array([actionforces.magnitude_y for actionforces in self.actionforces])
            distances_x = np.array([actionforces.position_x for actionforces in self.actionforces])
            distances_y = np.array([actionforces.position_y for actionforces in self.actionforces])

            # Danach wird der Drehpunkt bestimmt anhand einer Reaktionskraft
            node_pos_x = np.array([reactionforce.position_x for reactionforce in self.reactionforces])
            node_pos_y = np.array([reactionforce.position_y for reactionforce in self.reactionforces])
            
            # Alle Reaktionen in Variablen:
            reactionforces_x = np.array([reactionforces.magnitude_x for reactionforces in self.reactionforces])
            reactionforces_y = np.array([reactionforces.magnitude_y for reactionforces in self.reactionforces])
            distances_x_reaction = np.array([reactionforces.position_x for reactionforces in self.reactionforces])
            distances_y_reaction = np.array([reactionforces.position_y for reactionforces in self.reactionforces])
            reacntionforces_magnitude = [reactionforces.magnitude for reactionforces in self.reactionforces]
            reactionmoments = np.array([reactionmoments.magnitude for reactionmoments in self.reactionmoments])
            distances_x_reactionmoment = np.array([reactionmoments.distances_x for reactionmoments in self.reactionmoments])
            distances_y_reactionmoment = np.array([reactionmoments.distances_y for reactionmoments in self.reactionmoments])
            
            # Gleichgewicht            
            equations_equilibrium = []
            
            # Es wird die Summe aller Momente um jeden Auflagerpunkt gebildet
            for i in range(len(node_pos_x)):
                sum_moment = np.sum(forces_x * (distances_y-node_pos_y[i]) + forces_y * (distances_x-node_pos_x[i])) + np.sum(reactionforces_x * (distances_y_reaction-node_pos_y[i]) + reactionforces_y * (distances_x_reaction-node_pos_x[i]))
                equations_equilibrium.append(sum_moment)
                
            # Durch die Summe der horizontalen Kräfte können weitere Lagerkräfte bestimmt werden.
            sum_fx = np.sum(forces_x) + np.sum(reactionforces_x)
            equations_equilibrium.append(sum_fx)
            
            
            # Das Lösen der Gleichungen ergibt die magnitudes
            sol = sp.solve(equations_equilibrium, reacntionforces_magnitude)
            for reactionforces in self.reactionforces:
                # Die Symbolischen Werte der Reaktionskräfte werden mit der Lösung überschrieben
                reactionforces.magnitude = np.float64(reactionforces.magnitude.subs(sol))
                reactionforces.magnitude_x = reactionforces.magnitude * np.cos(np.radians(reactionforces.rotation))
                reactionforces.magnitude_y = reactionforces.magnitude * np.sin(np.radians(reactionforces.rotation))

  
class Plot:
    
    def __init__(self, system=None):
        self.system = system
    
    def plot_forces_and_moments(self):
        
        """Plot des Systems
        """
        fig, ax = plt.subplots(figsize=(15, 15))        
        
        
        def moment_symbol(moment, color):
            """Symbol of Moments

            Args:
                moment (Moment): Moment-class
                color (string): matplotlib color
                label (string): label for the legend
            """
            ax.annotate(f'M = {round(moment.magnitude,1)}', xy=(moment.position_x,moment.position_y), xytext = (30,30), textcoords="offset pixels", color=color)
            ax.plot(moment.position_x, moment.position_y, marker=r'$\circlearrowleft$',ms=40, color=color)
            
            
            
        def force_symbol(force, color):
            """Symbol of Forces / Forcevectors

            Args:
                force (_type_): _description_
                color (_type_): _description_
                label (_type_): _description_
            """
            scaler = max([force.magnitude for force in self.system.actionforces])   
             
            quiver_style = {
                'angles':'xy',
                'scale_units':'xy',
                'scale':scaler
            }
            
            ax.annotate(f'F = {round(force.magnitude,1)}', xy=(force.position_x,force.position_y), color=color)
            
            ax.quiver(force.position_x, force.position_y, force.magnitude_x, force.magnitude_y, color=color, **quiver_style)
            
            ax.quiver(force.position_x, force.position_y, force.magnitude_x, 0, color=color, **quiver_style, alpha=0.08)
            
            ax.quiver(force.position_x, force.position_y, 0, force.magnitude_y, color=color, **quiver_style, alpha=0.08)
            
            
            
        if self.system.actionforces != None:
            for actionforce in self.system.actionforces:
                # Symboldarstellung
                force_symbol(actionforce, 'red')
            for reactionforce in self.system.reactionforces:
                force_symbol(reactionforce, 'green', )
                force_symbol(reactionforce, 'green', )
                
                
        if self.system.actionmoments != None:    
            for actionmoment in self.system.actionmoments:
                # Symboldarstellung
                moment_symbol(actionmoment, 'red', )
            for reactionmoment in self.system.reactionmoments:
                moment_symbol(reactionmoment, 'green', )            
            
        
        # Berechnen Sie die Begrenzungen basierend auf den Kräften und Momenten
        max_magnitude = max(actionforce.magnitude for actionforce in self.system.actionforces)
        ax.set_xlim(-max_magnitude, max_magnitude)
        ax.set_ylim(-max_magnitude, max_magnitude)

        # Optional: Beschriften Sie die Achsen
        ax.set_xlabel('X-Achse [Krafteinheit]')
        ax.set_ylabel('Y-Achse [Krafteinheit]')
        ax.set_aspect('equal')
        ax.axis('equal')
        # ax.legend(ncol=2)
        ax.grid()

        plt.show()
