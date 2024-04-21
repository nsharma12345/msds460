# Critical Path Analysis 

# Problem description from Williams (2013, pages 94-98)
# Williams, H. Paul. 2013. Model Building in Mathematical Programming (fifth edition). New York: Wiley. [ISBN-13: 978-1-118-44333-0]

# Python PuLP solution prepared by Thomas W. Miller
# Revised April 20, 2023
# Implemented using activities dictionary with derived start_times and end_times
# rather than time decision variables as in Williams (2013)

from pulp import *

# Create a dictionary of the activities and their durations for the best-case scenario
activities = {'A':30, 'B':30, 'C':10, 'D1':25, 'D2':25, 'D3':20, 'D4':120, 'D5':15,'D6':45, 'D7':30, 'D8':20, 'E':25, 'F':25, 'G':40, 'H':16}

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

# Best Case Scenario Solution Variable Values:
# end_A = 30.0
# end_B = 30.0
# end_C = 40.0
# end_D1 = 55.0
# end_D2 = 80.0
# end_D3 = 75.0
# end_D4 = 200.0
# end_D5 = 215.0
# end_D6 = 245.0
# end_D7 = 275.0
# end_D8 = 295.0
# end_E = 65.0
# end_F = 320.0
# end_G = 335.0
# end_H = 351.0
# start_A = 0.0
# start_B = 0.0
# start_C = 30.0
# start_D1 = 30.0
# start_D2 = 55.0
# start_D3 = 55.0
# start_D4 = 80.0
# start_D5 = 200.0
# start_D6 = 200.0
# start_D7 = 245.0
# start_D8 = 275.0
# start_E = 40.0
# start_F = 295.0
# start_G = 295.0
# start_H = 335.0

# The minimum duration for the best case scenario is 351 hours, which is the critical path time.


