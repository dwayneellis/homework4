# CIS 2348 Homework 4 Fall 2020.
# Dwayne Ellis
# Student ID: #######
# Lab 14.11  Descending selection sort with output during execution

def selection_sort_descend_trace(integers_list):
    for i in range(len(integers_list) - 1):
        # Find the biggest element in unsorted sub-list
        max_j = i
        for j in range(i, len(integers_list)):
            if integers_list[j] > integers_list[max_j]:
                max_j = j
        # Swap the biggest element with the current element at index i
        integers_list[i], integers_list[max_j] = integers_list[max_j], integers_list[i]
        # Output the list at the end of the iteration
        integers_list_str = ''
        for i in integers_list:
            integers_list_str += str(i) + ' '
        print(integers_list_str)


if __name__ == '__main__':
    # Read in a list of integers
    integers_list_str = input()
    # Convert input string to a list of integers
    integers_list = []
    for integer_str in integers_list_str.split():
        integers_list.append(int(integer_str))
    # Call selection_sort_descend_trace()
    selection_sort_descend_trace(integers_list)
