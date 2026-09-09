print("Welcome to homepage")
option = int(input("Select option(1 = registration, 2 = team ranking, 3 = athlete ranking): "))

if option == 1:
    from func1teaminput import team_detail
    from func1teaminput import count_memperteam
    from func1teaminput import complete_registration
    
    print("\n team registration")
    teamname = input("Team name: ")
    registrationstatus = False
    athletes = []
    
    Totalcount = 0
    Mcount = 0
    Fcount = 0
    
    while registrationstatus == False:
        athletename = input("Athlete full name: ")
        athleteage = int(input("Athlete age group: "))
        athletegender = input("Athlete gender F/M: ")
        
        registered = team_detail(teamname,athletename,athleteage,athletegender,False)
        athletes.append(registered)
        
        status = input("Is registration complete? y/n: ")
        
        registrationstatus = complete_registration(status,registrationstatus)
    
    quantity = count_memperteam(athletes)
    print("\nRegistered athletes:")
    print(athletes)
    
    print("\nTeam quantity:")
    print("Total:", quantity[0])
    print("Female:", quantity[1])
    print("Male:", quantity[2])
