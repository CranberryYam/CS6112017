
def get_list(nested_list):
    final_list = []
    for sublist in nested_list:
        for item in sublist:
            final_list.append(item)
    return final_list

nested_list = [[1,3],[3,6]]
print(get_list(nested_list))