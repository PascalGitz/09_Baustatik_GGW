import numpy as np
import matplotlib.pyplot as plt



class System:
    def __init__(self, forces=None, moments=None, resultant_force=None, resultant_moment = None):
        self.forces = forces
        self.moments = moments
        self.resultant_force = resultant_force
        self.resultant_moment = resultant_moment


    def plot_forces_and_moments(self):
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
            scaler = max([force.magnitude for force in self.forces])    
            quiver_style = {
                'angles':'xy',
                'scale_units':'xy',
                'scale':scaler
            }
            ax.annotate(f'F = {round(force.magnitude,1)}', xy=(force.position_x,force.position_y), color=color)
            
            ax.quiver(force.position_x, force.position_y, force.magnitude_x, force.magnitude_y, color=color, **quiver_style)
            
            ax.quiver(force.position_x, force.position_y, force.magnitude_x, 0, color=color, **quiver_style, alpha=0.08)
            
            ax.quiver(force.position_x, force.position_y, 0, force.magnitude_y, color=color, **quiver_style, alpha=0.08)
            
        if self.forces != None:
            for force in self.forces:
                # Symboldarstellung
                force_symbol(force, 'red')
                force_symbol(self.resultant_force, 'green', )
                force_symbol(self.resultant_force, 'green', )
        if self.moments != None:    
            for moment in self.moments:
                # Symboldarstellung
                moment_symbol(moment, 'red', )
                moment_symbol(self.resultant_moment, 'green', )            
            
        
        # Berechnen Sie die Begrenzungen basierend auf den Kräften und Momenten
        max_magnitude = max(max(force.magnitude for force in self.forces),self.resultant_force.magnitude)
        ax.set_xlim(-max_magnitude, max_magnitude)
        ax.set_ylim(-max_magnitude, max_magnitude)

        # Optional: Beschriften Sie die Achsen
        ax.set_xlabel('X-Achse [Krafteinheit]')
        ax.set_ylabel('Y-Achse [Krafteinheit]')
        ax.set_aspect('equal')
        ax.axis('equal')
        ax.legend(ncol=2)
        ax.grid()

        plt.show()
