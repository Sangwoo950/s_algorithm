input = [3, 5, 6, 1, 2, 4]
max_num = 6


# find_max_num 이라는 함수 선언
def find_max_num(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num


result = find_max_num(input)
print(result)
