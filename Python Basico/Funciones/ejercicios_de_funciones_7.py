def is_prime_number(user_number):
    count_divisors = 0
    for i in range(1,user_number+1):
        if user_number % i == 0:
            count_divisors += 1
    if count_divisors == 2:
        return True
    else:
        return False

def build_prime_numbers_list(user_list):
    prime_numbers_list = []
    for i in range(len(user_list)):
        if is_prime_number(user_list[i]):
            prime_numbers_list.append(user_list[i])
    return prime_numbers_list

print("---- EJERCICIOS DE FUNCIONES - 7")
my_list = [1,2,4,5,6,7,8,10,11,12,13,9,67]

print(build_prime_numbers_list(my_list))