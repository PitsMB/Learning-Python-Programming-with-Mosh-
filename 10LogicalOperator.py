#Logical operator

#AND: both must be True
#OR: at least one is true
#NOT makes a True statement in to False

has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit and not has_criminal_record:
    print("Eligible for loan")