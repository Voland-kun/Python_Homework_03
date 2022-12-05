#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

lst1 = [1.1, 1.2, 3.1, 5.1, 10.01]
lst2 = [1, 2.18, 2.3, 4.5, 6.8]
lst3 = [6.8, 4.5, 2.3, 2.18, 1]

def get_fraction_diff(user_list):
    min_ = user_list[0] % 1
    max_ = user_list[0] % 1
    for i in user_list:
        i = i % 1
        if max_ == 0:
            min_ = i
            max_ = i
        elif 0 < i < min_:
            min_ = i
        elif i > max_:
            max_ = i    
    return  round(max_ - min_, 2)

print(get_fraction_diff(lst1))
print(get_fraction_diff(lst2))
print(get_fraction_diff(lst3))