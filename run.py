from auth import authorization, register
from operation import simple_operations, trigonometric

def main():
    try:
        print('Thank you for choosing our high-quality Product!')
        user_type_input = input('''Have you already registered?
        Please type Yes (Y) or No (N) ''').lower().strip()
        if user_type_input == 'yes' or user_type_input == 'y':
            print('Authorization')
            authorization()
        elif user_type_input == 'no' or user_type_input == 'n':
            user_second_answer = input('Would you like to register? Please type Yes (Y) or No (N)')
            if user_second_answer == 'y' or user_second_answer == 'yes':
                print('Registering')
                register()
            elif user_second_answer == 'no' or user_second_answer == 'n':
                print('BASIC CALCULATION VERSION')
                simple_operations()
            else:
                print('Not correct input. Have a nice day! Bye!')
        else:
            print('Not correct input. Please try again')
            input('Would you try again? Type Yes or No'.lower().strip())
            if user_type_input == 'yes' or user_type_input == 'y':
                main()
            else:
                print('Have a nice day! Bye!')
    except Exception as e:
        print(Exception)

main()