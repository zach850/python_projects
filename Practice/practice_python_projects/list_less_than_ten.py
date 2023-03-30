#write a program that prints out all the elements of the list that are less than 10.

def less_than_ten():
    user_input = int(input("Enter a number: "))
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    new_list = []
    for value in a:
        if value < user_input:
            new_list.append(value)
            print(new_list)
            
less_than_ten()

#one line of code 
# print( [ x for x in a if x<5 ] )