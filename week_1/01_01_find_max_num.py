input = [3, 5, 6, 1, 2, 4]


# find_max_num 이라는 함수 선언
def find_max_num(array):
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num

    # 이 부분을 채워보세요 !
    return 1


result = find_max_num(input)
print(result)
