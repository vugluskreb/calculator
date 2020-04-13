import os
import json


#                                   МОДУЛЬ ПРОВЕРКИ ЛОГИНА И ПАРОЛЯ ПОЛЬЗОВАТЕЛЯ
def check_pass(pass1, pass2):
#     ТУТ НАДО ПРОВЕРИТЬ ЛОГИН и ПОТОМ ПРОВЕРИТЬ ПАРОЛЬ
#     ЕСЛИ ДА ТО ОБЕЗБЯНУ КИДАЕТ В МОДУЛЬ ОПАРАЦИЙ
#




def register():
    repeat_register = True
    user = None
    while repeat_register:
        try:
            login = input('Enter your login:')
            password = input('Enter your password:')
            confirmed_password = input('Repeat your password:')
            if check_pass(password, confirmed_password):
                try:
                    user = write_to_db(login=login, password=password)
                    repeat_register = False
                    print('You are registered successfully!')
                except ValueError as e:
                    repeat_register = True
                    print(e)
            else:
                print('Incorrect password')
        except Exception as e:
            print(e)
    return user


def write_to_db(**new_user):
    file = os.path.join('users.json')

    def check_user_in_db(login):
        nonlocal file
        with open(file, 'r') as users:
            list_users = json.load(users)
            for user in list_users:
                if user['login'] == login:
                    raise ValueError('user already exists with login {}'.format(login))

    with open(file, 'r') as users:
        user_data = json.load(users)
        if len(user_data) == 0:
            new_user.update(
                {'id': 1}
            )
        else:
            check_user_in_db(login=new_user['login'])
            new_id = user_data[-1]['id'] + 1
            new_user.update({
                'id': new_id
            })
    user_data.append(new_user)
    with open(file, 'w+') as f:
        json.dump(user_data, f)
    return new_user



                            # Module to define if user is already registered



def main():
    print('Thank you for choosing our high-quality Product!')
    user_type_input = input('''Have you already registered as USER?
    Please type Yes (Y) or No (N) ''').lower().strip()

    if user_type_input == 'yes' or user_type_input == 'y':
        print('authorization module started >>>>>>>> ')
    # вход по логину и паролю                                      ВСТАВИТЬ ССЫЛКУ НА МОДУЛЬ АВТОРИЗАЦИИ!!!!!!!!!!!!!!!!
    elif user_type_input == 'no' or user_type_input == 'n':
        user_second_answer = input('Would you like to register? Please type Yes (Y) or No (N)')
        if user_second_answer == 'y' or user_second_answer == 'yes':
            print('full operational capabilities available!!! ')
            register()    # регистрация                                             ССЫЛКА НА МОДУЛЬ РЕЕГИСТРАЦИИ!!!!!!!!!!!
        elif user_second_answer == 'no' or user_second_answer == 'n':\
            print('simple module available only (simple operations)')
            # simple_operations()                                               ССЫЛКА НА МОДУЛЬ +  - / *    !!!!!!!!!!!
        else:
            print('Not correct input. Please try again')
            main()
    else:
        print('Not correct input. Please try again')
        input('Would you try again? Type Yes or No'.lower().strip() )
        if user_type_input == 'yes' or user_type_input == 'y':
            main()
        else:
            print('Have a nice day! Bye!')


# user = register()
# print(user)

main()
