def leap_year(year):
    if year % 400 == 0:
        # print("********* 400 only ******")
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Used these to get visibility on which tests were working and which were not:
# print("********* 100 not 400 ******")
# print("********* 400 only ******")
# print("********* 4 not 400 or 100 ******")

print(leap_year(2007))