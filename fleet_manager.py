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


