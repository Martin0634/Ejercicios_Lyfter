def string_to_list(string):
    words_list = []
    count_hyphen = 0
    words_list.append('')
    for char in range(len(string)):
        if string[char] == '-':
            count_hyphen += 1
            words_list.append('')
        else:
            words_list[count_hyphen] = words_list[count_hyphen] + string[char]
    return (words_list)

def sort_list_alphabetically(list):
    list.sort(key=str.lower)
    return list

def list_to_string(list):
    new_string = ''
    for i in range(len(list)):
        new_string = new_string + list[i]
        if i < len(list)-1:
            new_string = new_string + '-'
    return new_string

print("---- EJERCICIOS DE FUNCIONES - 6")

user_string = 'python-variable-funcion-computadora-monitor'
print(string_to_list(user_string))
print(sort_list_alphabetically(string_to_list(user_string)))
print(list_to_string(sort_list_alphabetically(string_to_list(user_string))))
