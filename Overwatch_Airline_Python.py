from datetime import datetime

#Database
category_id = 10
categories = {}  #category ID : (name, perk, price, validity)
members = {}  #member ID : member details
member_id = 10000

#Function to get a valid date in DD/MM/YYYY form
def check_date(prompt):
    while True:
        date_text = input(prompt).strip()
        try:
            return datetime.strptime(date_text, '%d/%m/%Y').strftime('%d/%m/%Y')
        except ValueError:  #if date is not valid, ask again
            print('Invalid date. Please use DD/MM/YYYY.')

#Function to check if the category ID exists
def check_category_id(prompt):
    while True:
        category_text = input(prompt).strip()
        if category_text.isdigit() and int(category_text) in categories:  #must be digit and exist in categories
            return int(category_text)
        print('Category ID does not exist. Please enter a valid category ID.')

#Function to create, update and delete category
def manage_category(category_id):
    
    while True:
        print('\n' + '=' * 40 +
              '\n🔵MANAGE CATEGORY🔵'
              '\n' + '=' * 40 +
              '\n1. Create'
              '\n2. Update'
              '\n3. Delete'
              '\n4. Back'
              )
        print('-' * 40)
        category_option = input('Enter your option (1-4): ')
        print('-' * 40)

        if category_option == '1':  #create category
            category_name = input('Enter category name: ').title().strip()
            category_perk = input('Enter category perk: ').title().strip()
            category_price = input('Enter new category price (RM): ')
            category_validity = input('Enter category validity: ').title().strip()

            categories[category_id] = (category_name, category_perk, category_price, category_validity)  #save category details as tuple

            category_id = category_id + 1  #next category ID
            print('\nSuccessfully created category!')

        elif category_option == '2':  #update category
            update_category_id = input('Enter category ID to update: ').strip()
            if update_category_id.isdigit():
                update_category_id = int(update_category_id)

                if update_category_id in categories:  #check if category exists
                    new_category_name = input('Enter category name: ').title().strip()
                    new_category_perk = input('Enter new category perk: ').title().strip()
                    new_category_price = input('Enter new category price (RM): ')
                    new_category_validity = input('Enter new category validity: ').title().strip()

                    categories[update_category_id] = (new_category_name, new_category_perk,
                                                      new_category_price, new_category_validity)  #replace old details with new details
                    print('\nSuccessfully updated category!')

                else:
                    print('\nCategory not found. Please enter a valid category.')

            else:
                print('Invalid category ID. Please enter a valid ID.')

        elif category_option == '3':  #Delete Category
            delete_category_id = input('Enter category ID to delete: ').strip()
            if delete_category_id.isdigit():
                delete_category_id = int(delete_category_id)

                if delete_category_id in categories:
                    del categories[delete_category_id]  #delete category from dictionary
                    print('\nSuccessfully deleted category!')

                else:
                    print('\nCategory not found. Please enter a valid category.')

            else:
                print('Invalid category ID. Please enter a valid ID.')

        elif category_option == '4':
            return category_id  #send latest category ID back to main menu

        else:
            print('\nInvalid option. Please enter a valid option.')

#Function to add, update and delete member
def manage_member(member_id):
    while True:
        print('\n' + '=' * 40 +
              '\n🟢MANAGE MEMBER🟢'
              '\n' + '=' * 40 +
              '\n1. Add member'
              '\n2. Update member'
              '\n3. Delete member'
              '\n4. Back'
              )
        print('-' * 40)
        member_option = input('Enter your option (1-4): ')
        print('-' * 40)

        if member_option == '1':  #add member
            if not categories:
                print('\nNo categories available. Please create a category first.')
                continue

            member_name = input('Please enter member full name: ').title().strip()
            member_ic_number = input('Please enter IC number: ').strip()
            member_category_id = check_category_id('Please enter category ID: ')
            card_usage = input('Please enter card usage: ').strip()
            start_date = check_date('Please enter start date (DD/MM/YYYY): ')
            end_date = check_date('Please enter end date (DD/MM/YYYY): ')

            members[member_id] = {  #save member details as dictionary
                'Name': member_name,
                'IC': member_ic_number,
                'Category ID': member_category_id,
                'Card Usage': card_usage,
                'Start Date': start_date,
                'End Date': end_date,
                'Points': 0  #new member starts with 0 points
            }
            member_id = member_id + 1  #next member ID
            print('\nSuccessfully created member!')

        elif member_option == '2':  #update member
            if not categories:
                print('\nNo categories available. Please create a category first.')
                continue

            update_member_id = input('Please enter member ID to update: ').strip()
            if update_member_id.isdigit(): #Validate if input is numbers only
                update_member_id = int(update_member_id) #Convert it into INTEGER

                if update_member_id in members:  #check if member exists
                    new_member_name = input('Please enter member full name: ').title().strip()
                    new_member_ic_number = input('Please enter IC number: ').strip()
                    new_member_category_id = check_category_id('Please enter category ID: ')
                    new_card_usage = input('Please enter card usage: ').strip()
                    new_start_date = check_date('Please enter start date (DD/MM/YYYY): ')
                    new_end_date = check_date('Please enter end date (DD/MM/YYYY): ')

                    members[update_member_id].update({  #points will not be changed
                        'Name': new_member_name,
                        'IC': new_member_ic_number,
                        'Category ID': new_member_category_id,
                        'Card Usage': new_card_usage,
                        'Start Date': new_start_date,
                        'End Date': new_end_date
                    })
                    print('\nSuccessfully updated member!')

                else:
                    print('\nMember ID does not exist.')

            else:
                print('\nInvalid member ID. Please enter a valid ID.')

        elif member_option == '3':  #delete member
            delete_member_id = input('Please enter member ID to delete: ').strip()
            if delete_member_id.isdigit():
                delete_member_id = int(delete_member_id)

                if delete_member_id in members:
                    del members[delete_member_id]  #delete member from dictionary
                    print('\nMember deleted successfully.')

                else:
                    print('\nMember ID does not exist.')

            else:
                print('\nInvalid member ID. Please enter a valid ID.')

        elif member_option == '4':
            return member_id  #send latest member ID back to main menu

        else:
            print('\nInvalid option. Please enter a valid option.')

#Function to display all category
def display_category():
    print('\n=== DISPLAY ALL CATEGORY ===')
    if not categories:  #if there's no category
        print('No categories available.')

    else:
        for category_id, category_details in categories.items():  #display every category
            print(f'\nCategory ID: {category_id}')
            print(f'Category Name: {category_details[0]}')
            print(f'Category Perk: {category_details[1]}')
            print(f'Category Price: RM{category_details[2]}')
            print(f'Category Validity: {category_details[3]}')

# Function to display member
def display_member():
    while True:
        print('\n' + '=' * 40 +
              '\n🟡DISPLAY MEMBER🟡'
              '\n' + '=' * 40 +
              '\n1. Display all members'
              '\n2. Display members under a category'
              '\n3. Display active members'
              '\n4. Display inactive members'
              '\n5. Display member card usage'
              '\n6. Back'
              )
        print('-' * 40)
        display_member_option = input('Enter your option (1-6): ')
        print('-' * 40)

        if display_member_option == '1':  
            if not members:
                print('No members available.')  #if there's no member

            else:
                for member_id, member_info in members.items():  #display all member
                    print(f'\nMember ID: {member_id}')
                    print(f'Name: {member_info["Name"]}')
                    print(f'IC: {member_info["IC"]}')
                    print(f'Category ID: {member_info["Category ID"]}')
                    print(f'Start Date: {member_info["Start Date"]}')
                    print(f'End Date: {member_info["End Date"]}')
                    print(f'Card Usage: {member_info["Card Usage"]}')
                    print(f'Points: {member_info["Points"]}')

        elif display_member_option == '2':  #MEMBERS BY CATEGORY
            filter_category_id = input('Enter category ID: ').strip()

            found = False
            if filter_category_id.isdigit():
                filter_category_id = int(filter_category_id)

                for member_id, member_info in members.items():
                    if member_info['Category ID'] == filter_category_id:
                        print(f'\nMember ID: {member_id}')
                        print(f'Name: {member_info["Name"]}')
                        found = True

                if not found:
                    print('\nNo members found under this category.')

        elif display_member_option == '3':  #DISPLAY ACTIVE MEMBER
            today = datetime.today().date()

            found = False
            for member_id, member_info in members.items():  #Checking active expiry date
                end_date = datetime.strptime(member_info['End Date'], '%d/%m/%Y').date()

                if end_date >= today:
                    print(f'\nMember ID: {member_id}')
                    print(f'Name: {member_info["Name"]}')
                    found = True

            if not found:
                print('\nNo active members found.')    #if no active member found

        elif display_member_option == '4':  #display inactive member
            today = datetime.today().date()

            found = False               
            for member_id, member_info in members.items(): ##Checking active expiry date
                end_date = datetime.strptime(member_info['End Date'], '%d/%m/%Y').date()

                if end_date < today:  #yes
                    print(f'\nMember ID: {member_id}')
                    print(f'Name: {member_info["Name"]}')
                    found = True

            if not found:
                print('\nNo inactive members found.')  #if no inactive member found

        elif display_member_option == '5':  #display member card usage
            display_member_id = input('Please enter member ID: ').strip()
            if display_member_id.isdigit():     #checking if id in digit form
                display_member_id = int(display_member_id)

                if display_member_id in members:
                    member_info = members[display_member_id]
                    print('\n=== MEMBER CARD USAGE ===')
                    print(f'Member ID: {display_member_id}')
                    print(f'Name: {member_info["Name"]}')
                    print(f'Card Usage: {member_info["Card Usage"]} times')

                else:
                    print('\nMember ID does not exist.')    #if id does not exist

            else:
                print('\nInvalid member ID. Please enter a valid ID.') #not in digit form

        elif display_member_option == '6':  #return to menu
            break

        else:
            print('\nInvalid option. Please enter a valid option.') #Invalid option output

#Function to generate and save member receipt
def generate_receipt():
    if not members: #check member exisity
        print('No members found.')
        return

    receipt_member_id = input('Please enter member ID: ').strip()   #ask user to enter member ID
    if not receipt_member_id.isdigit(): #check if id is digit form
        print('\nInvalid member ID. Please enter a valid ID.') #if id is invalid (not digit)
        return

    receipt_member_id = int(receipt_member_id)  
    if receipt_member_id not in members:
        print('\nMember ID does not exist.')    #if member id does not exist
        return

    member_info = members[receipt_member_id]
    category_id = member_info['Category ID']
    if category_id not in categories:
        print('\nCategory not found. Cannot generate receipt.')  #no category found
        return

    category_info = categories[category_id]
#check activity
    today = datetime.today().date()
    end_date = datetime.strptime(member_info['End Date'], '%d/%m/%Y').date()
    if end_date >= today:
        membership_status = 'Active'
    else:
        membership_status = 'Inactive' #setting inactive and active status

#generate file name using member id
    filename = str(receipt_member_id) + '_receipt.txt' 
    with open(filename, 'w') as file:
        file.write('\n====== MEMBER RECEIPT ======')
        file.write(f'\nMember ID: {receipt_member_id}')
        file.write(f'\nName: {member_info["Name"]}')
        file.write(f'\nCategory ID: {category_id}')
        file.write(f'\nCategory Name: {category_info[0]}')
        file.write(f'\nCategory Perk: {category_info[1]}')
        file.write(f'\nCategory Price: RM{category_info[2]}')
        file.write(f'\nMembership Validity: {category_info[3]}')
        file.write(f'\nCard usage: {member_info["Card Usage"]}')
        file.write(f'\nMembership renewal: {member_info["End Date"]}')
        file.write(f'\nMembership status: {membership_status}')
        file.write(f'\nMembership points: {member_info["Points"]}')

    print('Receipt saved as ' + filename)   #informing receipt have been saved

#Function to load and display receipt
def load_receipt():
    receipt_member_id = input('Please enter member ID: ').strip()  #input member id
    if receipt_member_id.isdigit(): #Check if id in digit form
        receipt_member_id = int(receipt_member_id)

        filename = str(receipt_member_id) + '_receipt.txt'
        try:
            with open(filename, 'r') as file:   #opening and display receipt
                print(file.read())
        except FileNotFoundError:
            print('No receipt file found for ' + filename)  #if file cant be found

    else:
        print('\nInvalid member ID. Please enter a valid ID.') #id not in digit form
        
#function to renew membership
def membership_renewal():
    if not members:
        print('\nNo members found.')    #if there's no member
        return

    member_id = input('Please enter member ID: ').strip()
    if not member_id.isdigit():
        print('\nInvalid member ID. Please enter a valid ID.')  #id not in digit form
        return

    member_id = int(member_id)
    if member_id not in members:
        print('\nMember ID does not exist.')    #member id does not exist
        return

    member_info = members[member_id]    #checking expiry
    today = datetime.today().date()
    end_date = datetime.strptime(member_info['End Date'], '%d/%m/%Y').date()

    if end_date >= today:   #display activity
        print('\nMembership is still active.')
        print('Renewal is not required yet.')
        return

    while True:
        new_end_date = datetime.strptime(check_date('Enter new end date (DD/MM/YYYY): '), '%d/%m/%Y').date()
        if new_end_date > today:  #only accept end date after today as new membership end date
            break
        print('\nNew end date must be after today.')

    member_info['Start Date'] = today.strftime('%d/%m/%Y')
    member_info['End Date'] = new_end_date.strftime('%d/%m/%Y') #display new date

    print('\nMembership renewed successfully!')
    print(f'New Start Date: {member_info["Start Date"]}')
    print(f'New End Date: {member_info["End Date"]}')

#Function for loyalty_point program
def loyalty_points_program():
    if not members:
        print('\nNo members found.')    #If there's no member
        return
    loyalty_member_id = input("Please enter member ID: ").strip()  #input member id

    if not loyalty_member_id.isdigit():
        print('\nInvalid member ID. Please enter a valid ID.') #if id not in digit form
        return

    loyalty_member_id = int(loyalty_member_id)

    if loyalty_member_id not in members:
        print('\nMember ID does not exist.')    #if member does not exist
        return

    member_info = members[loyalty_member_id]  

    while True: #Enter a loop
        print('\n' + '=' * 40 +
              '\n🟠LOYALTY POINTS PROGRAM⚪'  #loyalty point menu
              '\n' + '=' * 40 +
              '\n1. Check Loyalty Points'
              '\n2. Collect Points'
              '\n3. Redeem Rewards'
              '\n4. Back')
        print('-' * 40)
        loyalty_option = input('Enter your option (1-4): ').strip()
        print('-' * 40)

        if loyalty_option == '1': #check loyalty point
            print('\nLOYALTY POINTS BALANCE')
            print('Member ID:', loyalty_member_id)
            print('Member Name:', member_info['Name'])
            print('Available Points:', member_info["Points"])

        elif loyalty_option == '2':  #collect point
            points_input = input(
                'Enter points earned: '
            ).strip()

            if points_input.isdigit() and int(points_input) > 0:  #check if point entered is digit and greater then 0
                points_earned = int(points_input)
                member_info["Points"] += points_earned #Add new points to existing balance

                print('\nPoints collected successfully!')
                print('Points Earned:', points_earned)
                print('Total Points:', member_info["Points"])

            else:
                print('\nInvalid points. Enter a number greater than zero.') #if point entered less then zero

        elif loyalty_option == '3': #Redeem rewards
            print('\n' + '=' * 30 +
                  '\n🎁AVAILABLE REWARDS🎁'
                  '\n' + '=' * 30 +
                  '\n1. Airline Merchandise - 500 points'
                  '\n2. Free Hotel Stay - 1000 points'
                  '\n3. Free Flight - 2500 points')
            print('-' * 40)
            reward_option = input('Select a reward (1-3): ').strip() #select reward
            print('-' * 40)

            if reward_option == '1':    #select merchandise
                reward_name = 'Airline Merchandise'
                reward_cost = 500

            elif reward_option == '2':  #select free hotel stay
                reward_name = 'Free Hotel Stay'
                reward_cost = 1000

            elif reward_option == '3':  #select free flight
                reward_name = 'Free Flight'
                reward_cost = 2500

            else:
                print('\nInvalid reward option.')
                continue

            # Check whether the member has enough points
            if member_info["Points"] >= reward_cost: #if yes
                member_info["Points"] -= reward_cost #Deduct points blance

                print('\nReward redeemed successfully!')
                print('Reward:', reward_name)
                print('Points Used:', reward_cost)
                print('Remaining Points:', member_info["Points"])
            
            else:
                print('\nInsufficient loyalty points.') #if no
                print('Required Points:', reward_cost)
                print('Your Points:', member_info["Points"])

        elif loyalty_option == '4': #yes
            break #back to main menu

        else:
            print('\nInvalid option. Please enter a valid option.') #option not available


#Main Menu
while True:
    print('\n' + '='* 60)
    print('✈️⚫🟡🟠OVERWATCH AIRLINE MEMBERSHIP SYSTEM🟠🟡⚫✈️')
    print('='* 60)
    print('1. Manage Category')
    print('2. Manage Member')
    print('3. Display Category')
    print('4. Display Member')
    print('5. Generate member receipt')
    print('6. Membership renewal')
    print('7. Loyalty Points Program')
    print('8. Exit')
    print('-' * 60)

    main_option = input('Enter your option (1-8): ')

    if main_option == '1':  #Manage category
        category_id = manage_category(category_id)

    elif main_option == '2':  #Manage members
        member_id = manage_member(member_id)

    elif main_option == '3':  #Display categories
        display_category()

    elif main_option == '4': #Display member 
        display_member()

    elif main_option == '5': #Generate and load receipt
        while True:
            print('\n' + '=' * 40 +
                  '\n🧾MEMBER RECEIPT🧾'
                  '\n' + '=' * 40 +
                  '\n1. Generate receipt'
                  '\n2. Load receipt'
                  '\n3. Back'
                  )
            print('-' * 40)
            generate_option = input('Enter your option (1-3): ')
            print('-' * 40)

            if generate_option == '1':
                generate_receipt()
            elif generate_option == '2':
                load_receipt()
            elif generate_option == '3':
                break
            else:
                print('\nInvalid option. Please enter a valid option')

    elif main_option == '6': #membership renewal
        membership_renewal()

    elif main_option == '7': #loyalty point program
        loyalty_points_program()

    elif main_option == '8':
        print('\nExit')
        break

    else:
        print('\nInvalid option. Please enter a valid option') #option not available