def is_leap(year):
    leap = False

    # Write your logic here
    if (leap % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
        leap = False
    else:
        leap = True

    return leap


year = int(input())
print(is_leap(year))