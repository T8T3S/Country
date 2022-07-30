#Display menu items and header
def display_command():
    print('COMMAND MENU')
    print('view - View country name')
    print('add  - Add a country')
    print('del  - Delete a country')
    print('exit - Exit program')
#Display country code list
def display_country_codes(country_dict):
    country_codes = list(country_dict.keys())
    country_codes.sort()
    print_codes = 'Country codes: '
    for c in country_codes:
        print_codes += c + " "
    print(print_codes)
#View all country codes in dictionary, user select, view select's name
def view(country_dict):
    display_country_codes(country_dict)
    country_to_view = input('Enter country code: ').upper()
    if country_to_view in country_dict:
        print(f'Country name: {country_dict[country_to_view]}.')
    else:
        print('There is no country with that code.')
#Add country if it does not exist in dictionary
def add_country(country_dict):
     country_code_to_add = input('Enter country code: ').upper()
     if country_code_to_add in country_dict:
         print(country_dict[country_code_to_add],'is already using this code.')
     else:
         country_name_to_add = input('Enter country name: ') 
         country_dict[country_code_to_add] = country_name_to_add
         print(country_name_to_add,'was added.')
#Delete country from list if it exists
def delete_country(country_dict):
    country_to_delete = input('Enter country code: ').upper()
    if country_to_delete in country_dict:
        country_name = country_dict[country_to_delete]
        del country_dict[country_to_delete]
        print(country_name,'was deleted.')
    else:
        print('No country with that code to delete.')
def create_dict():
    country_dict = {
        'CA':'Canada',
        'MX':'Mexico',
        'US':'United States'
        }
    return country_dict
#Main function
def main():
    country_dict = create_dict()
    display_command()
    while True:
        command = input('\nCommand: ')
        if command.lower() == 'view':
            view(country_dict)
        elif command.lower() == 'add':
            add_country(country_dict)
        elif command.lower() == 'del':
            delete_country(country_dict)
        elif command.lower() == 'exit':
            print('Bye!')
            break
        else:
            print('Not a valid command. Please try again.')
#Calling main if namespace is main
if __name__ == '__main__':
    main()