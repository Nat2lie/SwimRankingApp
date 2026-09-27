athletelist = [("A",34),("B",36),("C",38)]
def fouls(athletes, athlete):
    checkfoul = athletes
    fouled = athlete
    for i in range(len(checkfoul)):
        if checkfoul[i][0] == fouled:
            temp = checkfoul[i]
            
            for j in range(i, len(checkfoul) - 1):
                checkfoul[j] = checkfoul[j + 1]
            
            checkfoul[len(checkfoul) - 1] = temp
            break
    return(checkfoul)

if __name__ == "__main__":
    athletefoul = input("Which athlete committed a foul? A/B/C: ")
    results = fouls(athletelist, athletefoul)
    print("\n Rankings")
    for i in range(len(results)):
        if results[i][0] == athletefoul:
            print(i+1, results[i][0], "DQ")
        else:
            print(i+1, results[i][0], results[i][1])
            
        