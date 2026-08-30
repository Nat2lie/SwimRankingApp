
#Parameter :(
def team_detail(tname, aname, Aage, agender, rstatus):
    return (tname, aname, Aage, agender, rstatus)


def count_memperteam(athletes):
    Totalcount = 0
    Fcount = 0
    Mcount = 0

    for athlete in athletes:
        if athlete[3] == "F":
            Fcount = Fcount + 1
            Totalcount = Totalcount + 1

        elif athlete[3] == "M":
            Mcount = Mcount + 1
            Totalcount = Totalcount + 1

    return (Totalcount, Fcount, Mcount)


def complete_registration(status, registration):
    if status == "y":
        registration = True
    else:
        registration = False

    return registration