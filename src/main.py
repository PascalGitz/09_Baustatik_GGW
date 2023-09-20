import actions as ac
import reactions as re
import structure as st


einwirkungen_kraefte = [ac.Force(magnitude=10,rotation_to_x=-90, position_x=10, position_y=0)]

reaktionen_kraefte = [re.Force(position_x=0, position_y=0, rotation_to_x=90), re.Force(0,0,0)]
reaktion_momente = [re.Moment(0,0)]


system_1 = st.System(actionforces=einwirkungen_kraefte, reactionforces=reaktionen_kraefte, reactionmoments=reaktion_momente)
system_1.calculate_reaction_force()


st.Plot(system_1).plot_forces_and_moments()