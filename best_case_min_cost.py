# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:14:18 2024

@author: nsharma
"""

# Best Case Scenario Solution Variable Values:
end_A = 30.0
end_B = 30.0
end_C = 40.0
end_D1 = 55.0
end_D2 = 80.0
end_D3 = 75.0
end_D4 = 200.0
end_D5 = 215.0
end_D6 = 245.0
end_D7 = 275.0
end_D8 = 295.0
end_E = 65.0
end_F = 320.0
end_G = 335.0
end_H = 351.0
start_A = 0.0
start_B = 0.0
start_C = 30.0
start_D1 = 30.0
start_D2 = 55.0
start_D3 = 55.0
start_D4 = 80.0
start_D5 = 200.0
start_D6 = 200.0
start_D7 = 245.0
start_D8 = 275.0
start_E = 40.0
start_F = 295.0
start_G = 295.0
start_H = 335.0

A_hours = end_A - start_A
B_hours = end_B - start_B
C_hours = end_C -start_C
D1_hours = end_D1 - start_D1
D2_hours = end_D2 - start_D2
D3_hours = end_D3 - start_D3
D4_hours = end_D4 - start_D4
D5_hours = end_D5 - start_D5
D6_hours = end_D6 - start_D6
D7_hours = end_D7 - start_D7
D8_hours = end_D8 - start_D8
E_hours = end_E - start_E
F_hours = end_F -start_F
G_hours = end_G -start_G
H_hours = end_H -start_H

min_cost = 55*(A_hours + B_hours + C_hours + D1_hours + D2_hours + D3_hours + D4_hours + D5_hours + D6_hours + D7_hours + D8_hours + E_hours + F_hours + G_hours + H_hours)
print("The minimum cost for the best case scenario is: ", min_cost)

# The minimum cost for the best case scenario is:  26180.0