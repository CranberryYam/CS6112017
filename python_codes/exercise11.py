
def get_product_by_iteration(numbers):
    product = 1
    for number in numbers:
        product = product*number
    return product

def get_product_by_recursion(numbers):
    if(len(numbers)==0):
        return numbers[0]
    return numbers[0]*get_product_by_iteration(numbers[1:])

list = [1,2,3,4,5]
print(get_product_by_iteration(list))
print(get_product_by_recursion(list))


