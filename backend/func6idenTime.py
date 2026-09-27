athletelist = [["rob", 34, 0], ["charlie", 35, 0], ["brown", 36, 0], ["Bill", 36, 0]]
def identical_times(athletes):
    iden_ath = athletes
    if iden_ath[0][1] == iden_ath[1][1]:
        awardpoint = (15+7)/2
        iden_ath[0][2] = iden_ath[0][2] + awardpoint
        iden_ath[1][2] = iden_ath[1][2] + awardpoint
        iden_ath[2][2] = iden_ath[2][2] + 7
        iden_ath[3][2] = iden_ath[3][2] + 3

    elif iden_ath[1][1] == iden_ath[2][1]:
        awardpoint1 = (7+5)/2
        iden_ath[1][2] = iden_ath[1][2] + awardpoint1
        iden_ath[2][2] = iden_ath[2][2] + awardpoint1
        iden_ath[0][2] = iden_ath[0][2] + 15
        iden_ath[3][2] = iden_ath[3][2] + 3

    elif iden_ath[2][1] == iden_ath[3][1]:
        awardpoint2 = (5+3)/2
        iden_ath[2][2] = iden_ath[2][2] + awardpoint2
        iden_ath[3][2] = iden_ath[3][2] + awardpoint2
        iden_ath[0][2] = iden_ath[0][2] + 15
        iden_ath[1][2] = iden_ath[1][2] + 7

    else:
        iden_ath[0][2] = iden_ath[0][2] + 15
        iden_ath[1][2] = iden_ath[1][2] + 7
        iden_ath[2][2] = iden_ath[2][2] + 5
        iden_ath[3][2] = iden_ath[3][2] + 3
    
    return(iden_ath)

medals = ["Gold", "Silver", "Bronze"]
if __name__ == "__main__":
    results = identical_times(athletelist)
    print(results)
    print()
    f = results[0][1]
    s = 0
    t = 0

    for i in range(len(results)):
        if results[i][1] == f:
            print(results[i][0], "GOLD")


        elif results[i][1] > f and s == 0:
            s = results[i][1]
            print(results[i][0], "Silver")
        elif results[i][1] == s:
            print(results[i][0], "Silver")


        elif results[i][1] > s and t == 0:
            t = results[i][1]
            print(results[i][0], "Bronze")
        elif results[i][1] == t:
            print(results[i][0], "Bronze")