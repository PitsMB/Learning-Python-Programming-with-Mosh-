#Comparison Operators

#<: a is less than b
#>: a is greater than b
#<=: a is less than or equal to b
#>=: a is greater than or equal to b
#==: a is equal to b
#!=: a is not equal to b

name = 'Pits'
store_name_value = len(name)
if store_name_value < 3:
    print('name must be at least 3 characters')
elif store_name_value > 50:
    print('name can be a maximum of 50 character')
else:
    print('name looks good!')