def count_ele(list):
    even = 0
    odd = 0
    positive = 0
    negative = 0


    for num in list:
        if num % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1

        if num > 0:
            positive = positive + 1
        elif num < 0:
            negative = negative + 1

    return even, odd, positive, negative

numbers = [10, -5, 3, -8, 7, 2, -4]

even, odd, positive, negative = count_ele(numbers)

print("Even:",even)
print("ODD:",odd)
print("Positive:",positive)
print("Negative:",negative)