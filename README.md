Part 1. 

This assignment involves creating a proposal for a software development project for a group of restaurant owners in Marlborough, Massachusetts. The main deliverable is a consumer-focused recommendation system for over a hundred restaurants, with data sourced from Yelp reviews. The system will be updated monthly for the list of restaurants and daily for the Yelp reviews.
As the owner of my own data science and software engineering firm, I will be involved in all aspects of the recommender system. My team includes a project manager (myself), frontend developer, backend developer, data engineer, data scientist, and database administrator.

The project consists of eight general tasks, one of which includes eight software development subtasks. An Excel spreadsheet outlines these tasks along with their immediate predecessors. The spreadsheet also includes columns for the workers assigned to the project, which will be useful for future task scheduling. 

My team has determined best-case, expected, and worst-case estimates for the number of hours needed for each of the sixteen tasks, as well as the hourly rate of $55 for each worker role. Using these estimates, we have specified a linear programming model with a minimum time objective for all three scenarios, and used the solution to determine the minimum cost, identify the critical path, and develop the Gantt charts. 
The figure below shows the activities, their predecessors, the estimates of hours required for each activity in the three different scenarios, as well as the number of different types of workers assigned for each activity. Note that the hours assigned for each task under each scenario are the total hours to be split among all the workers working on that task.

![image](https://github.com/nsharma12345/msds460/assets/166173519/dffc7f81-d217-41e5-b70f-d6f2e9689d18)

Some uncertainties the team had related to this assignment were around the Yelp API, the chosen technologies, and the availability of the different workers. Additionally, the estimates for the best-case, expected, and worst-case number of hours needed for each task are based on assumptions and could vary. The hourly rate for each worker role is assumed to be $55 per hour, realistically this rate would vary based on factors like experience level, market rates, etc. However, for the purpose of this assignment in specifying the objective function, we are making the simplifying assumption that all contributors to the project charge the same hourly rate.

The figures below show the directed graphs for each scenario, with the values on the arrows being the total duration of a task in hours. 

![image](https://github.com/nsharma12345/msds460/assets/166173519/0ceed7c3-ad5a-446d-9b50-ab2319578c70)

![image](https://github.com/nsharma12345/msds460/assets/166173519/477fe49c-86b3-4d6a-ab86-22a6776f993a)

![image](https://github.com/nsharma12345/msds460/assets/166173519/56276406-9f75-48f7-a499-9334e5c8df45)

 
Tasks that do not have any predecessors or whose predecessors have been completed can be done in parallel. From the given task list, tasks A and B can start at the same time as they do not have any predecessors. Tasks C and D1 can be done in parallel as they both depend on task A. Similarly, tasks D2 and D3 can be done in parallel as they both depend on task D1. Tasks D5 and D6 can be also done in parallel since they both depend on task D4. 

A linear programming model was specified and implemented for each scenario with the minimum time objective, using the Python PuLP library. This code has been posted to the Github repository for this assignment. The implemented code to determine the solution for the start and end hours for each activity with the critical path analysis is shown for the three scenarios in the following files posted to the Assignment 2 branch of this repository. These files are the following: best_case_scenario_CPA.py, expected_scenario_CPA.py and worst_case_scenario_CPA.py. Once the solutions for the activity hours and the critical path duration were determined for each of these scenarios using the aforementioned python prorgramming scripts, separate programming scripts were created using these hours to determine the minimum cost for each scenario. These files are the following: best_case_min_cost.py, expected_case_min_cost.py, and worst_case_min_cost.py. 

For the best-case scenario, the critical path duration was 351 hours and the minimum cost was $26,180. For the expected scenario, the critical path duration was 499 hours and the minimum cost was $38,060. For the worst case scenario, the critical path duration was 832 hours and the minimum cost was $61,160. For all three scenarios, the critical path included the following activities: A, D1, D2, D4, D6, D7, D8, G, H. 

The figures below show the Gantt charts developed for all three scenarios, where the yellow bars represent the duration of the activity and the green bars represent the amount of slack an activity has, in hours. 

Worst case scenario: 
![image](https://github.com/nsharma12345/msds460/assets/166173519/338bfbc0-08e1-4e86-9164-cd5defc9f1a4)

Expected scenario:
![image](https://github.com/nsharma12345/msds460/assets/166173519/c73b9e00-9d57-4458-bb90-a55baf1e5a83)

Best case scenario:
![image](https://github.com/nsharma12345/msds460/assets/166173519/5ee7d1ed-6dd2-4ef8-818c-ce7ac9136e21)










