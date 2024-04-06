Part 1. 
In this assignment, the diet problem aims to find the most cost-effective way to meet specified nutritional requirements, based on five food items I eat daily. In the context of the code provided, the diet problem involves selecting a combination of food items from a given set, each with its cost and nutritional content per serving. The goal is to minimize the total cost of the selected food items while ensuring that the combined nutritional content meets or exceeds certain weekly nutritional requirements. These requirements typically include components like sodium, energy (calories), protein, vitamin D, calcium, iron, and potassium.
The food items I have selected for this diet problem are the following: Tricolor quinoa, whole milk, eggs, coconut water, and Lightlife tempeh. The following are screenshots of the nutrition labels and prices of each item, as well as the calculated cost per serving for each item.

Quinoa:
![image](https://github.com/nsharma12345/msds460/assets/166173519/33fa5dc8-1319-49dd-bcbe-7ede54aa906c)
![image](https://github.com/nsharma12345/msds460/assets/166173519/fc7c204c-b0f5-4454-bcf6-885f7a8344e7)

Cost per serving of quinoa = $3.99/11 = $0.69/serving

Whole milk:
![image](https://github.com/nsharma12345/msds460/assets/166173519/782470dc-6e20-4188-a8df-6a4291ddf3c6)
![image](https://github.com/nsharma12345/msds460/assets/166173519/6b317c04-d556-43a6-b96d-869898ba4a25)

Cost per serving of whole milk = $5.49/8 = $0.36/serving

Eggs:
![image](https://github.com/nsharma12345/msds460/assets/166173519/361f39c8-3873-4448-8eeb-24954007978d)
![image](https://github.com/nsharma12345/msds460/assets/166173519/29f04353-3db4-49b2-b625-8484c7cbe990)
![image](https://github.com/nsharma12345/msds460/assets/166173519/516c8ada-1009-4530-8f98-e89db091ba31)

Cost per serving of eggs = $10.49/12 = $0.87/serving

Coconut water:
![image](https://github.com/nsharma12345/msds460/assets/166173519/828c60b7-3481-4963-81e6-d0c2d3d40dc1)
![image](https://github.com/nsharma12345/msds460/assets/166173519/1f89f36d-e19c-4797-aa5d-e4fdd5d3ce9d)

Cost per serving of coconut water = $3.19/2 = $1.60/serving

Tempeh:
![image](https://github.com/nsharma12345/msds460/assets/166173519/79f5d98f-c284-49dc-a6a1-1ae0218b6084)
![image](https://github.com/nsharma12345/msds460/assets/166173519/f3ae28fc-a83b-4372-aef7-0415cf48407d)

Cost per serving of tempeh = $3.79/2.5 = $1.52/serving


Part 2. The following is the program code for the diet problem. 
```
from pulp import *

# Define the nutritional requirements (weekly)
nutrition_requirements = {
    'Sodium': 5000 * 7,  # mg
    'Energy': 2000 * 7,  # kcal
    'Protein': 50 * 7,    # g
    'Vitamin D': 20 * 7,  # mcg
    'Calcium': 1300 * 7,  # mg
    'Iron': 18 * 7,       # mg
    'Potassium': 4700 * 7  # mg
}

# Nutrition facts for the five packaged food items
# Each row represents a food item with its cost & nutritional content per serving
# Columns: Food item, Cost (per serving), Sodium, Energy, Protein, Vitamin D, Calcium, Iron, Potassium
food_items = [
    ['Lightlife tempeh', 1.52, 0, 160, 18, 0, 87, 2, 284],
    ['VitaCoco coconut water', 1.60, 60, 45, 0, 0, 34, 0, 470],
    ['Eggs', 0.87, 80, 80, 7, 1.1, 30, 1, 80],
    ['Horizon Organic Whole High Vitamin D Milk', 0.36, 135, 160, 8, 4.5, 310, 0, 410],
    ['Organic Tricolor Quinoa', 0.69, 0, 150, 6, 0, 20, 2, 240]
]

# Create a list of food item names
food_names = [item[0] for item in food_items]

# Create a dictionary to hold the cost of each food item
costs = {item[0]: item[1] for item in food_items}

# Create dictionaries to hold the nutritional content of each food item separately
nutritional_content = {item[0]: item[2:] for item in food_items}

# Create the 'prob' variable to contain the problem data
prob = LpProblem("Diet Problem", LpMinimize)

# Define decision variables
food_vars = LpVariable.dicts('Food', food_names, lowBound=0, cat='Continuous')

# Add objective function to minimize the total cost
prob += lpSum([costs[i] * food_vars[i] for i in food_names]), "Total Cost"

# Add constraints for each nutritional requirement
for nutrient, requirement in nutrition_requirements.items():
    if nutrient == 'Sodium':
        prob += lpSum([nutritional_content[item][list(nutrition_requirements.keys()).index(nutrient)] * food_vars[item] for item in food_names]) <= requirement, nutrient + "Maximum"
    else:
        prob += lpSum([nutritional_content[item][list(nutrition_requirements.keys()).index(nutrient)] * food_vars[item] for item in food_names]) >= requirement, nutrient + "Minimum"

# Solve the problem
prob.solve()

# Print the optimal diet plan
print("Optimal Diet Plan:")
for food in food_names:
    if food_vars[food].varValue > 0:
        print(food, ": ", food_vars[food].varValue)

# Print the total cost of the optimal diet
print("Total Cost of the Diet: $", value(prob.objective))

# Output
# Optimal Diet Plan:
# Horizon Organic Whole High Vitamin D Milk :  43.365854
# Organic Tricolor Quinoa :  63.0
# Total Cost of the Diet: $ 59.081707439999995
```


Specify the linear programming problem in standard form, showing decision variables, objective function with cost coefficients, and weekly nutritional constraints. Describe the problem in plain English. Implement the linear programming problem using Python PuLP or AMPL. Provide the program code and output/listing as plain text files, posting within a GitHub repository dedicated to this assignment. 
Part 3. Solve the linear programming problem using your Python PuLP or AMPL code. Describe the solution, showing units (serving sizes) for each of the five food items. What is the minimum cost solution? How much would you need to spend on food each week? Include the text file (listing) of your solution in the GitHub repository.
Part 4. Solutions to the diet problem are notorious for their lack of variety. Suppose you require at least one serving of each food item or meal during the week, setting constraints in the diet problem accordingly. Solve the revised linear programming problem. How do these additional constraints change the solution? How much more would you have to spend on food each week? Include the text file (listing) of your solution of this revised problem in the GitHub repository. Suppose this diet solution continues to lack variety. Describe how could you add further variety to your diet by making additional revisions to the model specification.
Part 5. Large language models (LLMs), as implemented with ChatGPT and other generative AI systems, are being used to solve many problems in data science. Select an LLM-based service or agent with which to work. Pick a free plan or one that is freely available to Northwestern students. (Do not pay for services in completing this assignment.) Indicate which service you have selected, providing its web address or uniform resource locator (URL). See if you can get your selected LLM agent to specify a model for The Diet Problem. See to what extent you can get the agent to develop computer code for The Diet Problem. Report on your success or failure. Provide a step-by-step review of your work. What prompts did you use? How did the conversation with the LLM agent go? Were you able to build on the conversation or to tailor it to your specific needs? As part of the GitHub repository for this assignment, include a plain text file of the complete conversation that you had with the LLM agent. Comment on your experience. Could an LLM agent be used to complete this assignment?
