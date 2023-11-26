def calc_total(total_bill, tip_percent, num_people):
    tip_calc = float(tip_percent) / 100
    total_amt = float(total_bill) * (tip_calc + 1)
    total_per_person = total_amt / int(num_people)
    return total_per_person


def build_total_string(raw_amt):
    rounded_amt = round(raw_amt, 2)
    return f'${rounded_amt:.2f}'


print('Welcome to the tip calculator')
billAmt = input('What was the total bill?')
tipPercent = input('What percentage tip would you like to give?')
numPeople = input('How many people to split the bill?')
totalPerPerson = calc_total(billAmt, tipPercent, numPeople)
print(f'Each person should pay {build_total_string(totalPerPerson)}')
