
import actions as ac
import reactions as re
import structure as st

einwirkungen_kraefte = []

for i in range(10):
    einwirkungen_kraefte.append(ac.Force(10, -90, 5+i, 0))
    einwirkungen_kraefte.append(ac.Force(i, i*10, 5,0))


einwirkungen_momente = [ac.Moment(0, 0,0), ac.Moment(0, 10,0)]
reaktionen_kraefte = [re.Force(90, 0, 0), re.Force(0,0,0)]
reaktionen_moment = [re.Moment(0,0)]

system_3 = st.System(actionforces=einwirkungen_kraefte, reactionforces=reaktionen_kraefte, actionmoments=einwirkungen_momente, reactionmoments=reaktionen_moment)
system_3.calculate_reaction_force()


st.Plot(system_3).plot_forces_and_moments()