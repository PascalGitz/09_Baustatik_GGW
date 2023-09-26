from equilibrium import *


def test_calculate_reaction_force():
    einwirkungen_kraefte = [Actionforce(-15,90, 1.5,0), Actionforce(50, 90, 3,0), Actionforce(-104, 90, 7.4, 0), Actionforce(50, 0,10,0)]
    einwirkungen_momente = [Actionmoment(10, 0,0)]
    reaktionen_kraefte = [Reactionforce(90, 10,0), Reactionforce(0,5,5)]
    reaktionen_momente = [Reactionmoment(0,0)]

    system_1 = System(actionforces=einwirkungen_kraefte, reactionforces=reaktionen_kraefte, actionmoments=einwirkungen_momente, reactionmoments=reaktionen_momente)
    
    solution_system = system_1.calculate_reaction_force()
    soultion_expected = '{M_(0, 0): 192.100000000000, R_(10, 0, 90): 69.0000000000000, R_(5, 5, 0): -50.0000000000000}'
    
    assert str(solution_system) == soultion_expected


