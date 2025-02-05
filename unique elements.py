def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
input_data = [3, 7, 3, 5, 2, 5, 9, 2]
output_data = unique_elements(input_data)
print(output_data) 
