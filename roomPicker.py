import numpy as np
from scipy.optimize import linear_sum_assignment
no_of_rooms:int = 4 #fill in number of rooms here, assume that number of people is the same as number of rooms

# assign numerical value to rooms in order e.g. [3,4,2,1] means that the person prefers room 2 the most and room 4 the least
daniel_choices = [3,4,2,1]
dwayne_choices = [4,3,2,1]
joel_choices = [3,4,1,2]
zaheer_choices = [2,3,4,1]

#makes sure no-one is cheating
array = np.array([daniel_choices, dwayne_choices, joel_choices, zaheer_choices])

for choices in array:
    if len(choices) != len(set(choices)):
        raise Exception("Someone has entered the same value twice")
    for entry in choices:
        if entry > no_of_rooms or entry < 0:
            raise Exception("Someone hasn't entered the data correctly")


#deal with remaining rooms
cost_matrix = -array

# Hungarian algorithm
row_ind, col_ind = linear_sum_assignment(cost_matrix)

# Results
max_sum = array[row_ind, col_ind].sum()
selected_entries = array[row_ind, col_ind]

print("Maximum sum:", max_sum)
print("Selected entries:", selected_entries)
print("Rows chosen:", row_ind)
print("Columns:", col_ind)

for row, col in zip(row_ind, col_ind):
    print(f"Person {row+1} gets room {col+1}")
