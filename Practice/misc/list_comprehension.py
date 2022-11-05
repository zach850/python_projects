foods = ['cheese', 'bread', 'pesto', 'cracker']

foods = [food.upper() for food in foods]


bits = [False, True, False, False, True, False, False, True]
new_bits = [1 if b == True else 0 for b in bits]


my_string = "HiMyNameIsZach"
my_string = ''.join(
    [i if i.islower() else ' ' + i for i in my_string]
    )[1:]
print(my_string)