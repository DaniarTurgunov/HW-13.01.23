new_string = input('Введите строку: ')
my_list = [new_string[i] for i in range(len(new_string))]
print(my_list)
new_list =[]
my_dict = {}

def encode():
    for i in range(len(my_list)):
        if my_list[i].isdigit():
            c = int(my_list[i])
            for j in range(c):
                word = my_list[i+1]
                new_list.append(word)
    word_str = ''.join(new_list)
    print(word_str)

def decode():
    count = 0
    count1 = 0
    for i in range(len(my_list)):
        j = 0
        if my_list[i] == my_list[+j]:
            count += 1
            j+=1
            my_dict[my_list[i]] = count
        else:
            count1 += 1
            my_dict[my_list[i]] = count
    result = "".join(str(value) + str(key) for key, value in my_dict.items())
    print(result)

if my_list[0].isdigit():
    z = encode()
else:
    z = decode()