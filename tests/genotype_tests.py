import core.genotype as gt


""" 1-gene genotype
        gene labels: ['8_bit','7_bit','6_bit','5_bit','4_bit','3_bit','2_bit','1_bit']
        gene values: [[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]]
"""
# initialize gene label and range
labels = ['8_bit', '7_bit', '6_bit', '5_bit', '4_bit', '3_bit', '2_bit', '1_bit']
values = [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]

# create genotype
geno_type = gt.Genotype(labels=labels, values=values)

# get tuple with genotype info
description = geno_type.describe()

# verify genotype has 8 gene
assert description[0] == 8

# create random chromosome from genotype
random_x = geno_type.create_random_instance()

# print instance using default formatter
instance_string = geno_type.print_instance(random_x)
instance = list(instance_string)
assert len(instance) == len(random_x.genes)
for i in range(len(instance)):
    assert instance[i] == random_x.genes[i]

# print instance using custom formatter
def custom_print(chromosome):
    num = 0
    for y in reversed(range(8)):
        if chromosome.genes[7-y] == '1':
                num += pow(2, y)

    return str(num)

geno_type.formatter = custom_print
instance_string = geno_type.print_instance(random_x)
instance_value = int(instance_string)
assert instance_value >= 0
assert instance_value <= 255

# verify first gene position is '8_bit'
pos = geno_type.get_pos('8_bit')
assert pos == 0

# verify first gene label is '8_bit'
label = geno_type.get_label(0)
assert label == '8_bit'


"""2-gene genotype
        labels: 'eye_color', 'hair_color'
        ranges: 0-2, 0-3
"""

# initialize gene label and range
labels = ['eye_color', 'hair_color']
values = [range(3), range(4)]

# create genotype
geno_type = gt.Genotype(labels=labels, values=values)

# get tuple with genotype info
description = geno_type.describe()

# verify genotype has two genes
assert description[0] == 2

# verify genotype labels are ['eye_color', 'hair_color']
assert description[0] == 2
assert description[1][0] == 'eye_color'
assert description[1][1] == 'hair_color'

# create random chromosome from genotype
random_colors = geno_type.create_random_instance()


print("genotype tests PASS")