athleteslist = []

def ranking(athletes):
    for i in range(len(athletes)):
        for j in range(len(athletes)- 1):
            if athletes[j][1] > athletes[j+1][1]:
                athletes[j], athletes[j+1] = athletes[j+1], athletes[j]
    return (athletes)

Medals = ["Gold", "Silver", "Bronze"]

if __name__ == "__main__":
    n = int(input("Enter the number of swimmers: "))

    for i in range(n):
        athletename = input("Athlete name: ")
        time = float(input("Athlete time: "))
        athleteslist.append([athletename, time])

    print("\n Ranking")
    for i in range(n):
        print(f"{i+1} {ranking(athleteslist)[i][0]} {ranking(athleteslist)[i][1]} {Medals[i]}")






