# CIS 2348 Homework 4 Fall 2020.
# Dwayne Ellis
# Student ID: #######
# Lab 14.13  Sorting user IDs

# Global variable
num_calls = 0

def partition(user_ids, i, k):
    # Pick the middle element as the pivot
    pivot_i = (i + k) // 2
    pivot = user_ids[pivot_i]
    # Low and high indices
    l = i
    h = k
    # Move low and high indices on each other and swap when necessary until they meet
    while True:
        while user_ids[l] < pivot:
            l += 1
        while user_ids[h] > pivot:
            h -= 1
        if l >= h:
            return h
        user_ids[l], user_ids[h] = user_ids[h], user_ids[l]
        l += 1
        h -= 1
    
    
def quicksort(user_ids, i, k):
    global num_calls
    # Keep track of how many times quicksort() is called
    num_calls += 1
    if i < k:
        # Perform partition
        mid = partition(user_ids, i, k)
        # Recursive call on the left side
        quicksort(user_ids, i, mid)
        # Recursive call on the right side
        quicksort(user_ids, mid + 1, k)   
    

if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()
        
    # Initial call to quicksort 
    quicksort(user_ids, 0, len(user_ids) - 1)
    
    # Print number of calls to quicksort
    print(num_calls)
    
    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
