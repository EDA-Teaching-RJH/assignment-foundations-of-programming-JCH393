def init_database():
    names = ['Jean-Luc Picard','William Riker','Data','Geordi La Forge','Worf']
    ranks = ['Captain','Commander','Lieutenant Commander','Lieutenant Commander','Lieutenant']
    divs = ['Command','Command','Operations','Engineering','Security']
    ids = [1001,1002,1003,1004,1005]
    return names, ranks, divs, ids

def display_menu():
    student_name = input('What is your full name? ')

    print("\n--- MENU ---")
    print("Student logged in:", student_name)
    print("1. View Crew")
    print("2. Add Crew")
    print("3. Remove Crew")
    print("4. Analyze Data")
    print("5. Exit")
    
    choice = input("Select option: ").strip()
    return choice

def add_member(names, ranks, divs, ids):
    valid_ranks = ['Captain','Lieutenant Commander','Lieutenant','Commander']
    name = input('Enter name: ').strip()
    rank = input('Enter rank: ').strip()
    div = input('Enter division: ').strip()

    try:
        new_id = int(input('Enter ID: '))
    except ValueError:
        print('ID must be a number.')
        return
    
    if new_id in ids:
        print('Error: ID already exists.')
        return
    if rank not in valid_ranks:
        print('Error: Invalid rank.')
        return
    names.append(name)
    ranks.append(rank)
    divs.append(div)
    ids.append(new_id)
    print('Crew member added successfully.')

def remove_member(names, ranks, divs, ids):
    try:
        rem_id = int(input('Enter ID to remove: '))
    except ValueError:
        print('ID must be a number.')
    if rem_id not in ids:
        print('Error: ID not found')
    idx = ids.index(rem_id)
    names.pop(idx)
    ranks.pop(idx)
    divs.pop(idx)
    ids.pop(idx)
    print('Crew member removed succesfully.')

def update_rank(ranks, ids):
    try:
        member_id = int(input('Enter member ID: '))
    except ValueError:
        print('ID must be a number.')
        return

    if member_id not in ids:
        print('Error: ID not found.')
        return

    idx = ids.index(member_id)

    new_rank = input('Enter new rank: ').strip()

    ranks[idx] = new_rank

    print('Rank updated successfully.')

def display_roster(names, ranks, divs, ids):
    print('\n--- CREW ROSTER ---')
    print(f'{'ID':<6} {'Name':<20} {'Rank':<22} {'Division'}')
    print('-' * 90)

    for i in range(len(names)):
        print(f'{ids[i]:<6} {names[i]:<20} {ranks[i]:<22} {divs[i]}')

def search_crew(names, ranks, divs, ids):
    term = input('Enter search term: ').strip().lower()
    found = False

    print('\n--- SEARCH RESULTS ---')

    for i in range(len(names)):
        if term in names[i].lower():
            print(f'{ids[i]} - {names[i]} ({ranks[i]}, {divs[i]})')
            found = True

    if found == False:
        print('No matching crew members found.')

def filter_by_division(names, divs):
    division = input('Enter division (Command, Operations, Security, Engineering): ').strip()

    print(f'\n--- {division.upper()} DIVISION ---')
    found = False

    for i in range(len(names)):
        if divs[i] == division:
            print(names[i])
            found = True

    if not found:
        print('No crew members found in this division.')

def calculate_payroll(ranks):
    total = 0

    for rank in ranks:
        if rank == "Captain":
            total += 1000
        elif rank == "Commander":
            total += 800
        elif rank == "Lieutenant Commander":
            total += 600
        elif rank == "Lieutenant":
            total += 400
        elif rank == "Ensign":
            total += 200
    
    return total
