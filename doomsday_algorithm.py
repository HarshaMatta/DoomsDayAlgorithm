# Global variables
WeekArr = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

DDays = {
    1: 3,
    2: 28,
    3: 14,
    4: 4,
    5: 9,
    6: 6,
    7: 11,
    8: 8,
    9: 5,
    10: 10,
    11: 7,
    12: 12,
}


# ------------------------------------
def CenCodeAlg(year):
    # ---find century code--- #
    v = int(year // 100)
    mod = (v % 4)
    # ---4 condition if statement--- #
    if mod == 0:
        cenCode = 2
    elif mod == 1:
        cenCode = 0
    elif mod == 2:
        cenCode = 5
    elif mod == 3:
        cenCode = 3

    return cenCode


# ------------------------------------
def DoomsDayAlg(year, cenCode):
    # --- a ---#
    a = cenCode

    # --- b ---#
    num = year % 100
    b = num // 12

    # --- c ---#
    c = num % 12

    # --- d ---#
    d = c // 4

    # ---doomsday---#
    e = a + b + c + d
    doomsday = e % 7
    return doomsday


# ---------------------------------------------
def daytime(year, month, day, doomsday):
    dday = DDays[month]
    diff = day - dday
    theday = (diff + doomsday) % 7

    return theday


def get_day_name(year, month, day):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        DDays[1] = 4
        DDays[2] = 29

    cenCode = CenCodeAlg(year)
    doomsday = DoomsDayAlg(year, cenCode)
    day = daytime(year, month, day, doomsday)
    return WeekArr[day]


def get_day_name_input():
    year = int(input('Year: '))
    month = int(input('Month: '))
    day = int(input('Day: '))

    name = get_day_name(year, month, day)
    print(name)


# ----------------------
get_day_name_input()