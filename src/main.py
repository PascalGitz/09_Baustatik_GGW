from actions_on_structures import *
from structure import *
from equilibrium import *


kraefte = [Actionforce(-15,90, 1.5,0), Actionforce(50, 90, 3,0), Actionforce(-104, 90, 7.4, 0), Actionforce(50, 0,10,0)]
resultierende_kraft = Equilibrium(kraefte, None).calculate_resultant_force()
resultierendes_moment = Equilibrium(kraefte, None).calculate_resultant_moment()
plotter = System(kraefte, resultant_force=resultierende_kraft, resultant_moment=resultierendes_moment)


plotter.plot_forces_and_moments()