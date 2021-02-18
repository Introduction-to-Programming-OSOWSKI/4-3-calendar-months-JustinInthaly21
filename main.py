def calendar(m):

    for i in range(o, len(month)):
        if m == month[i]:
            return i

    return m + " is not a month"

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
