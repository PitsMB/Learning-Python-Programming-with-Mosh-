#Weight Converter Program
weight = input('Weight: ')
metric_weight = input('(L)bs or (K)g: ')
if metric_weight == 'l' or metric_weight == 'L':
    to_kg = float(weight) * 0.45
    print(to_kg)
elif metric_weight == 'k' or metric_weight == 'K':
    to_lbs = float(weight) / 0.45
    print(to_lbs)