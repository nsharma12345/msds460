# Critical Path Analysis 
# Implemented using activities dictionary with derived start_times and end_times
# rather than time decision variables as in Williams (2013)

from pulp import *

# Create a dictionary of the activities and their durations for the expected scenario
activities = {'A':50, 'B':40, 'C':16, 'D1':40, 'D2':40, 'D3':32, 'D4':160, 'D5':25,'D6':50, 'D7':50, 'D8':25, 'E':40, 'F':40, 'G':60, 'H':24}

# Create a list of the activities
activities_list = list(activities.keys())

# Create a dictionary of the activity precedences
precedences = {'A': [], 'B': [], 'C': ['A'], 'D1': ['A'],  'D2': ['D1'], 'D3': ['D1'], 'D4': ['D2','D3'], 'D5': ['D4'], 'D6': ['D4'], 'D7': ['D6'], 'D8': ['D5', 'D7'],  'E': ['B','C'], 'F': ['D8','E'], 'G': ['A','D8'], 'H': ['F','G']}

# Create the LP problem
prob = LpProblem("Critical Path", LpMinimize)

# Create the LP variables
start_times = {activity: LpVariable(f"start_{activity}", 0, None) for activity in activities_list}
end_times = {activity: LpVariable(f"end_{activity}", 0, None) for activity in activities_list}

# Add the constraints
for activity in activities_list:
    prob += end_times[activity] == start_times[activity] + activities[activity], f"{activity}_duration"
    for predecessor in precedences[activity]:
        prob += start_times[activity] >= end_times[predecessor], f"{activity}_predecessor_{predecessor}"

# Set the objective function
prob += lpSum([end_times[activity] for activity in activities_list]), "minimize_end_times"

# Solve the LP problem
status = prob.solve()

# Print the results
print("Critical Path time:")
for activity in activities_list:
    if value(start_times[activity]) == 0:
        print(f"{activity} starts at time 0")
    if value(end_times[activity]) == max([value(end_times[activity]) for activity in activities_list]):
        print(f"{activity} ends at {value(end_times[activity])} hours in duration")

# Print solution
print("\nSolution variable values:")
for var in prob.variables():
    if var.name != "_dummy":
        print(var.name, "=", var.varValue)

# Expected Case Scenario Solution Variable Values:
# end_A = 50.0
# end_B = 40.0
# end_C = 66.0
# end_D1 = 90.0
# end_D2 = 130.0
# end_D3 = 122.0
# end_D4 = 290.0
# end_D5 = 315.0
# end_D6 = 340.0
# end_D7 = 390.0
# end_D8 = 415.0
# end_E = 106.0
# end_F = 455.0
# end_G = 475.0
# end_H = 499.0
# start_A = 0.0
# start_B = 0.0
# start_C = 50.0
# start_D1 = 50.0
# start_D2 = 90.0
# start_D3 = 90.0
# start_D4 = 130.0
# start_D5 = 290.0
# start_D6 = 290.0
# start_D7 = 340.0
# start_D8 = 390.0
# start_E = 66.0
# start_F = 415.0
# start_G = 415.0
# start_H = 475.0    
    
# The minimum duration for the expected scenario is 499 hours, which is the critical path time.
# The min cost code for the expected scenario is found in "expected_case_min_cost.py" file
    
    
    
    
    
    
