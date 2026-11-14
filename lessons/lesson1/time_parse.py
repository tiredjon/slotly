def time2mins(time):
    if len(time) < 5:
        time = "0" + time
    hrs = time[0] + time[1]
    mins = time[3] + time[4]

    return str(int(hrs) * 60 + int(mins))


def halfhourlater(time):
    if len(time) < 5:
        time = "0" + time
    cur = int(time2mins(time))
    halfadded = cur + 30
    if halfadded >= 1440:
        halfadded = halfadded - 1440
    hrs = halfadded // 60
    mins = halfadded % 60
    return f"{hrs}:{mins}"


a = input("hh:mm format: ")

print(halfhourlater(a))

