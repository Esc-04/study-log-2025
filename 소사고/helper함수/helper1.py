#2025/04/28
def sort_nums(a):
    def is_odd(list1):
        sum_odd=0
        for i in list1:
            if i%2:
                sum+=i
        return sum_odd

    def is_even(list2):
        sum_even=0
        for j in list2:
            if j%2==0:
                sum+=j
        return sum_even
    result1=is_odd(a)
    result2=is_even(a)
    return result1, result2

    