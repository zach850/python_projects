
#write a program that returns a list that contains only the 
#elements that are common between the lists (without duplicates)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

combine_lists = a + b
unique_list = list(set(combine_lists))

print(unique_list)


#Extras:
    #Randomly generate two lists to test this
    #Write this in one line of Python
        

import random

list1 = random.sample(range(50), 10)
list2 = random.sample(range(-50, 50), 15)

combine_listss = list1 + list2
print(list(set(combine_listss)))

