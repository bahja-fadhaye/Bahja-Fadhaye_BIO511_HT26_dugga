#part2 

''''Question 2: a'''

my_list = [1, 5, "4", "six", 3.14]  # a list with both number and string

my_new_list = []  # cretaetd an  new list 

for number in my_list:   # loops over all the item  in the list 
    if isinstance(number, (int, float)): # vilkor som kontrollerar ifaall om det är redan int eller float 
        my_new_list.append(number)  # om vilkoret är uppfyllen  its basically appends to new list
    elif isinstance(number, str) and number.isnumeric(): # another vilkor som kontrolllerrar om de det är sträng och numbber
           my_new_list.append(int(number)) # detta konvertar  and append to new list
    print(my_new_list) ## prints the new list 

try:    ### if it cannot be cannot be converted use an try and exception 
      ## hinner ej  men den bor de var aupp under for-statse,
    print(number)
except ValueError:
    print('That is not a valid number.', number)