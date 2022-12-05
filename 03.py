#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def input_int():
    while True:
        try:
            user_number = input('Введите целое число: ')
            user_number = int(user_number)
            return user_number
        except ValueError:
            print('Введено не целое число.')

def dec_to_bin (user_number):
    result = ''
    while user_number > 0:
        result = result + str(user_number%2)
        user_number //= 2
    return result

x = input_int()
print(dec_to_bin (x))
