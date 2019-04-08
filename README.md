# Q-Learning-based-smart-based

Problem Statement:-
A smart city needs smart mobility, and to achieve this objective, the travel should be made convenient through sustainable transport 
solutions.  Transportation system all  over the world is facing unprecedented challenges in the current scenario of increased population,
urbanization and motorization.  Farewell to all difficulties as reinforcement learning along with deep learning can now make it simpler for
consumers.  In this paper we have applied reinforcement learning techniques for a self-driving agent in a simplified world to aid it in 
effectively reaching its destinations in the allotted time. We have first investigated the environment, the agent operates in, by 
constructing a very basic driving implementation. Once the agent is successful at operating within the environment, we can then identify 
each possible state the agent can be in when considering such things as traffic lights and oncoming traffic at each intersection. 
With states identified, we can implement a Q-Learning algorithm for the self-driving agent to guide the agent towards its destination 
within the allotted time. Finally, we can improve upon the Q-Learning algorithm to find the best configuration of learning and exploration 
factors to ensure the self-driving agent is reaching its destinations with consistently positive results.  
Our aim is also to find optimum values of parameters of the fitting function alpha, gamma and epsilon, so that the agent can work in an
optimized way with the most optimum parameter values. Hence, a comparative analysis has also been conducted.  

Methodology used:- 
The solution to the smart cab objective is deep reinforcement learning in a simulated environment. The smart cab operates in an ideal, 
grid-like city (similar to New York City), with roads going in the North-South and East-West directions. Other vehicles will certainly 
be present on the road, but there will be no pedestrians to be      concerned with. At each intersection there is a traffic light that 
either allows traffic in the North-South direction or the East-West direction.  We have assumed that the smart cab is assigned a route
plan based on the passengers' starting location and destination. The route is split at each intersection into waypoints, and the smart 
cab, at any instant, is at some intersection in the world. Therefore, the next waypoint to the destination, assuming the destination has 
not already been reached, is one intersection away in one direction (North, South, East, or West). The smart cab has only an egocentric 
view of the intersection it is at: It can determine the state of the traffic light for its direction of movement, and whether there is a
vehicle at the intersection for each of the oncoming directions. For each action, the smart cab may either stay idle at the intersection, 
or drive to the next intersection to the left, right, or ahead of it. Finally, each trip has a time to reach the destination which 
decreases for each action taken (the passengers want to get there quickly). If the allotted time becomes zero before reaching the 
destination, the trip has failed. The smart cab will receive positive or negative rewards based on the action it has taken. Expectedly,
the smart cab will receive a small positive reward when making a good action, and a varying amount of negative reward dependent on the 
severity of the traffic violation it would have committed. Based on the rewards and penalties the smart cab receives, the self-driving 
agent implementation should learn an optimal policy for driving on the city roads while obeying traffic rules, avoiding accidents, and 
reaching passengers' destinations in the allotted time.  Environment: The smartcab operates in an ideal, grid-like city (similar to 
New York City), with roads going in the North-South  and East-West directions. Other vehicles will certainly be present on the road, but 
there will be no pedestrians to be concerned with. At each intersection there is a traffic light that either allows traffic in the 
North-South direction or the East-West direction. 
U.S. Right-of-Way rules apply: On a green light, a left turn is permitted if there is no oncoming traffic making a right turn or coming
straight through the intersection.  On a red light, a right turn is permitted if no oncoming traffic is approaching from your left 
through the intersection. To understand how to correctly yield to oncoming traffic when turning left. 

Inputs and Outputs: 
For this work we have assumed that the smartcab is assigned a route plan based on the passengers' starting location 
and destination. The route is split at each intersection into waypoints, and the smartcab, at any instant, is at some intersection in 
the world. Therefore, the next waypoint to the destination, assuming the destination has not already been reached, is one intersection 
away in one direction (North, South, East, or West).  The smartcab has only an egocentric view of the intersection it is at: It can 
determine the state of the traffic light for its direction of movement, and whether there is a vehicle at the intersection for each of 
the oncoming directions. For each action, the smartcab may either idle at the intersection, or drive to the next intersection to the 
left, right, or ahead of it. Finally, each trip has a time to reach the destination which decreases for each action taken (the passengers
want to get there quickly). If the allotted time becomes zero before reaching the destination, the trip has failed. 

Rewards and Goal: 
The smartcab will receive positive or negative rewards based on the action it has taken. Expectedly, the smartcab
will receive a small positive reward when making a good action, and a varying amount of negative reward dependent on the severity of 
the traffic violation it would have committed. Based on the rewards and penalties the smartcab receives, the self-driving agent 
implementation should learn an optimal policy for driving on the city roads while obeying traffic rules, avoiding accidents,  and 
reaching passengers' destinations in the allotted time. 
 
Proposed Algorithm: 
In this work we are applying reinforcement learning techniques for a self-driving agent in a simplified world to aid it in effectively 
reaching its destinations in the allotted time. We are first investigating the environment, the agent operates in, by constructing a 
very basic driving implementation. Once our agent was successful at operating within the environment, we are then identifying each 
possible state the agent can be in when considering such things as traffic lights and oncoming traffic at each intersection. With 
states identified, we are implementing a Q-Learning algorithm for the self-driving agent to guide the agent towards its destination 
within the allotted time. Finally, we are improving the Q-Learning algorithm to find the best configuration of learning and exploration 
factors to ensure the self-driving agent is reaching its destinations with consistently positive results. The Q-Learning algorithm was 
implemented: 1. Set the γ and α parameter, and environment rewards in matrix R. 
2. Select a random initial state. If the stateaction pair has not been visited previously, set Q(state,action)=0.Q(state,action)=0. 5. 
Do While the goal state hasn’t been reached. - Select one among all possible actions for the current state. If a state-action pair has
not been visited previously, set Q(state,action)=0.Q(state,action)=0. for them. - Using this possible action, consider going to the 
next state. - Get maximum Q value for this next state based on all possible actions. – 
 
Compute:
Q(state,action)=(1−α)Q(state,action)+α[R(state ,action)+γ max[Q(next state,all actions)]]Q(state,action)= (1−α)Q(state,action)+α[R(state,
action)+γ max[Q(next sta te,all actions)]]- Set the next state as the current state. 
