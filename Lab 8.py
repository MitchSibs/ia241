'''
Lab 8

'''

#3.1

def string_count(input_str):

    return len(input_str.split())

print(string_count('a string'))

#3.2

demo_str = 'Hello World!'

print(string_count(demo_str))


#3.3

def min_number(num_list):

    min_item = num_list[0]

    for num in num_list:
        if type(num) is int:
            if min_item >= num:
                min_item = num

    return min_item

    

#3.4

demo_list = [1,2,3,4,5,6]

print(min_number(demo_list))

#3.5

mix_list = [1,2,3,4,'a',5,6]

print(min_number(mix_list))

