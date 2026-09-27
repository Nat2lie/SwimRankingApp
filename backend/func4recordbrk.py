athleteslist = []
record = [45.3,39.6,32.9,30.4,27.89]
def newrecord(time, records):
    update = time
    check = records
    for i in range(len(update)):
        if update[i][1] == 8 or update[i][1] == 9:
            if update[i][2] < check[i]:
                check[i] = update[i][2]
                print("New Record!")
        elif update[i][1] == 10 or update[i][1] == 11:
            if update[i][2] < check[i+1]:
                check[i+1] = update[i][2]
                print("New Record!")
        elif update[i][1] == 12 or update[i][1] == 13:
            if update[i][2] < check[i+2]:
                check[i+2] = update[i][2]
                print("New Record!")
        elif update[i][1] == 14 or update[i][1] == 15:
            if update[i][2] < check[i+3]:
                check[i+3] = update[i][2]
                print("New Record!")
        elif update[i][1] >= 16:
            if update[i][2] < check[i+4]:
                check[i+4] = update[i][2]
                print("New Record!")
    return(check)

if __name__ == "__main__":
    athletename = input("Enter athlete name: ")
    athleteage = int(input("Enter athlete age: "))
    athletetime = float(input("Enter athlete time: "))
    athleteslist.append([athletename, athleteage, athletetime])
    print(athleteslist)

    update_record = newrecord(athleteslist, record)
    print(update_record)



    
