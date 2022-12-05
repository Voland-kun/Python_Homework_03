#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

lst1 = [2, 3, 4, 5, 6]
lst2 = [2, 3, 5, 6]

def get_product_of_pair_numbers(user_list):
    result_list = []
    for i in range(0, len(user_list)//2+len(user_list)%2):
        result_list.append(user_list[i]*user_list[-i-1])
    return result_list

print(get_product_of_pair_numbers(lst1))
print(get_product_of_pair_numbers(lst2))