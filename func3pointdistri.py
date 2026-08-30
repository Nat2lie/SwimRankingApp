#variables
athletelist = [["rob",0], ["charlie",0], ["brown",0]]
#points = [15,7,5,3,2,1]
def point(athletes):
    sorted = athletes
    for i in range(len(sorted)):
        if i == 0:
            sorted[i][1] = sorted[i][1] + 15
        elif i == 1:
            sorted[i][1] = sorted[i][1] + 7
        elif i == 2:
            sorted[i][1] = sorted[i][1] + 5
        elif i == 3:
            sorted[i][1] = sorted[i][1] + 3
        elif i == 4:
            sorted[i][1] = sorted[i][1] + 2
        elif i == 5:
            sorted[i][1] = sorted[i][1] + 1
    return (sorted)

print("\n Ranking")
result=point(athletelist)
for i in range(len(result)):
    print(f"{i+1} {result[i][0]} {result[i][1]}")

