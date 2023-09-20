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
        
    def calculate_reaction_force(self):
        
        
            # Zuerst werden alle Einwirkungen in Variablen gespeichert:
            if self.actionforces == None:
                forces_x, forces_y, distances_x, distances_y = 0,0,0,0
                print('Das System hat keine einwirkende Kräfte')
            
            if self.actionforces != None:
                if type(self.actionforces[0]) == type(ac.Force(0,0,0,0)):
                    forces_x = np.array([actionforces.magnitude_x for actionforces in self.actionforces])
                    forces_y = np.array([actionforces.magnitude_y for actionforces in self.actionforces])
                    distances_x = np.array([actionforces.position_x for actionforces in self.actionforces])
                    distances_y = np.array([actionforces.position_y for actionforces in self.actionforces])
                else:
                    print('Fehlerhafte Eingabe in den einwirkenden Kräften')
                
                
            # Danach für alle einwirkenden Momente
            if self.actionmoments == None:
                moments = 0
                print('Das System hat keine einwirkenden Momente')
                
            if self.actionmoments != None:
                if type(self.actionmoments[0]) == type(ac.Moment(0,0,0)):
                    moments = np.array([actionmoments.magnitude for actionmoments in self.actionmoments])
                else:
                    print('Fehlerhafte Eingabe in den einwirkenden Momenten')
                
                
            
            
            # Die Positionen der Reaktionskräfte und Momente dienen direkt als Drehpunkt für das Gleichgewicht der Momente. Dazu wird eine leere Liste erstellt, welche mit den Koordinaten gefüttert wird, sofern diese vorhanden sind.
            
            node_pos_x = np.array([-10e9, -10e8, -10e7])
            node_pos_y = np.array([10e9, 10e8, 10e7])
            
            
            # Alle Reaktionskräfte in Variablen:
            if self.reactionforces == None:
                reactionforces_symbols,reactionforces_x, reactionforces_y, distances_x_reaction, distances_y_reaction = 0,0,0,0,0
                print('Das System hat keine Auflagerkräfte')
            
            if self.reactionforces != None:
                if type(self.reactionforces[0]) == type(re.Force(0,0,0)):
                    reactionforces_x = np.array([reactionforces.magnitude_x for reactionforces in self.reactionforces])
                    reactionforces_y = np.array([reactionforces.magnitude_y for reactionforces in self.reactionforces])
                    distances_x_reaction = np.array([reactionforces.position_x for reactionforces in self.reactionforces])
                    distances_y_reaction = np.array([reactionforces.position_y for reactionforces in self.reactionforces])
                    reactionforces_symbols = [reactionforces.magnitude for reactionforces in self.reactionforces]
                    
                    # Die Drehpunkte der Reaktionskräfte hinzugefügt
                    # node_pos_x = np.append(node_pos_x,distances_x_reaction)
                    # node_pos_y = np.append(node_pos_y,distances_y_reaction)
                else: 
                    print('Fehlerhafte Eingabe in den Reaktionskräften')
                
                
            # Alle Reaktionsmomente in Variablen:
            if self.reactionmoments == None:
                print('Das System hat keine Auflagermomente')
                reactionmoments_symbols, distances_x_reactionmoment, distances_y_reactionmoment = 0,0,0
            
            if self.reactionmoments != None:
                if type(self.reactionmoments[0]) == type(re.Moment(0,0)):
                    reactionmoments_symbols = np.array([reactionmoments.magnitude for reactionmoments in self.reactionmoments])
                    distances_x_reactionmoment = np.array([reactionmoments.position_x for reactionmoments in self.reactionmoments])
                    distances_y_reactionmoment = np.array([reactionmoments.position_y for reactionmoments in self.reactionmoments])
                    
                    # Die Koordinaten der Reaktionsmomente werden den Drehpunkten hinzugefügt
                    # node_pos_x = np.append(node_pos_x,distances_x_reactionmoment)
                    # node_pos_y = np.append(node_pos_y,distances_y_reactionmoment)
                
                else:
                    print('Fehlerhafte Eingabe in den Reaktionsmomenten')
                
            # Gleichgewicht            
            equations_equilibrium = []
            # Es wird die Summe aller Momente um jeden Auflagerpunkt gebildet
            for i in range(0,len(node_pos_x)):
                sum_moment = np.sum(forces_x * (distances_y-node_pos_y[i]) + forces_y * (distances_x-node_pos_x[i])) + np.sum(reactionforces_x * (distances_y_reaction-node_pos_y[i]) + reactionforces_y * (distances_x_reaction-node_pos_x[i])) + np.sum(moments) + np.sum(reactionmoments_symbols)
                equations_equilibrium.append(sum_moment)
            
            # Durch die Summe der horizontalen Kräfte können weitere Lagerkräfte bestimmt werden.
            sum_fx = np.sum(forces_x) + np.sum(reactionforces_x)
            equations_equilibrium.append(sum_fx)
            print(equations_equilibrium, len(equations_equilibrium))
            # Bestimmung der Symbole, nach welchen gelöst wird
            symbols_to_solve = np.append(reactionforces_symbols, reactionmoments_symbols)
            print(symbols_to_solve, len(symbols_to_solve))
            


            # Das Lösen der Gleichungen ergibt die magnitudes
            sol = sp.solve(equations_equilibrium, symbols_to_solve)
            print(sol)
            
            # Die Symbolischen Werte der Reaktionskräfte und der Reaktionsmomente werden mit der Lösung überschrieben       
            if self.reactionforces != None:
                if type(self.reactionforces[0]) == type(re.Force(0,0,0)):
                    for reactionforces in self.reactionforces:
                        reactionforces.magnitude = np.float64(reactionforces.magnitude.subs(sol))
                        reactionforces.magnitude_x = reactionforces.magnitude * np.cos(np.radians(reactionforces.rotation))
                        reactionforces.magnitude_y = reactionforces.magnitude * np.sin(np.radians(reactionforces.rotation))
            if self.reactionmoments != None:
                if type(self.reactionmoments[0]) == type(re.Moment(0,0)):                        
                    for reactionmoment in self.reactionmoments:
                            reactionmoment.magnitude = np.float64(reactionmoment.magnitude.subs(sol))
  
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
            
            # Die Position der Vektoren wird durch die länge des Vektors subtrahiert, dies gewährleistet, dass die Pfeilspitze am definierten Punkt zu liegen kommt.
            ax.annotate(f'F = {abs(round(force.magnitude,1))}', xy=(force.position_x - force.magnitude_x/scaler,force.position_y - force.magnitude_y/scaler), xytext = (7,7), textcoords="offset pixels", color=color)
            ax.quiver(force.position_x- force.magnitude_x/scaler, force.position_y - force.magnitude_y/scaler, force.magnitude_x, force.magnitude_y, color=color, **quiver_style)
            ax.quiver(force.position_x- force.magnitude_x/scaler, force.position_y - force.position_y - force.magnitude_y/scaler, force.magnitude_x, 0, color=color, **quiver_style, alpha=0.08)
            ax.quiver(force.position_x- force.magnitude_x/scaler, force.position_y - force.position_y - force.magnitude_y/scaler, 0, force.magnitude_y, color=color, **quiver_style, alpha=0.08)
            
            
            
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
        if self.system.reactionmoments != None:
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
