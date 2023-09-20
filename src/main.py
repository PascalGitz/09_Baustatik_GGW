import actions as ac
import reactions as re
import structure as st


einwirkungen = [ac.Force(-15,90, 1.5,0), ac.Force(+50, 90, 3,0), ac.Force(-104, 90, 7.4, 0), ac.Force(50, 0,10,0)]
reaktionen = [re.Force(90, 0, 0), re.Force(90, 10,0), re.Force(0,0,0)]

system_1 = st.System(actionforces=einwirkungen, reactionforces=reaktionen)
system_1.calculate_reaction_force()


st.Plot(system_1).plot_forces_and_moments()