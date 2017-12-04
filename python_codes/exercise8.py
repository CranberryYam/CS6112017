
a = ['baseball','basketball','football']
b = a
b[1] = 'ping-pong'
print(a)
c = a[:]
c[2] = 'soccer'
print(a)

def set_first_elem_to_zero(l):
    l[0] = 0
    return l

list = [3,4,5,6]
print(set_first_elem_to_zero(list))