import core.crossover as xo


""" 1-pt Crossover

Test random crossover of 2 strings at one point

"""
# initialize bit strings
list_1 = list("10110010")
list_2 = list("01001100")

# recombine using OnePointCrossover
co = xo.OnePointCrossover()
child_1, child_2 = co.recombine(list_1, list_2)

# verify strings got crossed over
assert str(list_1) != str(child_1)
assert str(list_2) != str(child_2)
assert len(child_1) == len(child_2)

print("crossover tests PASS")