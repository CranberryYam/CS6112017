
def print_element(datas):
    for data in datas:
        print(data)

def print_element_reversed(datas):
    for data in reversed(datas):
        print(data)

def get_len(datas):
    count = 0
    for data in datas:
        count = count + 1
    return count


list = ['baseball','basketball','football']
print_element(list)
print_element_reversed(list)
print(get_len(list))



