def calendar(m):

    for i in range(1, len(month)):
        if m == month[i]:
            return i + 1

    return m + " is not a month"

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

print(calendar("March"))
