def to_indian_currency(value):
    num_str = str(value)
    if len(num_str) <= 3:
        return num_str
    last3 = num_str[-3:]
    remaining = num_str[:-3]
    remaining_reverse = remaining[::-1]
    two_digits = [remaining_reverse[i:i+2] for i in range(0,len(remaining_reverse),2)] # split into groups of 2
    remaining = ','.join(two[::-1] for two in two_digits[::-1]) # reverse the two_digits and join with commas
    return remaining + ',' + last3

value = 504678
print(to_indian_currency(value))
