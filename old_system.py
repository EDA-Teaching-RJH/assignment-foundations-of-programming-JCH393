n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        loading += 1 #Made the loading loop progress and end
        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ").strip() #remove whitespaces
        
        if opt == "1":  #'==' instead of '='
            print("Current Crew List:") 
            
            for i in range(len(n)): #uses number of indices in the list 
                print(n[i] + " - " + r[i] + ' (' + d[i] + ')') # added d  
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
            n.append(new_name)
            r.append(new_rank) #append to the other two lists as well
            d.append(new_div)
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
           
            if rem in n: #added if statement incase user types names not in n
                idx = n.index(rem)
                n.pop(idx)
                r.pop(idx)
                d.pop(idx)
                print("Removed.")
            else:
                print('Name not found')
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or rank == "Commander": #added 'rank =='
                    count = count + 1
            print("High ranking officers: " + str(count)) #allows integer in string 
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
    x = 10 #changed indentation, outside of while loop
    if x > 5:
        print("System Check OK")
    else:
        print("System Failure")
            
       
    if len(n) > 0:
        print("Database has entries.")
    if len(n) == 0:
        print("Database empty.")

        
    fuel = 100
    consumption = 0
    while fuel > 0:
            
        print("Idling...")
        break 
            
    print("End of cycle.")

run_system_monolith() #added '()'
