#if statements
price = 1000000
has_good_credit = False
if has_good_credit:
    price *= 0.1
else:
    price *= 0.2
print(price)