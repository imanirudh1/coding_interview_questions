digit=4321
def digit_sum(digit):
    if len(str(digit)) == 1:
        return digit
    else:
        return digit%10 + digit_sum(digit//10)

print(digit_sum(digit))            