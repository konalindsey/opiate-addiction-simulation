# opiate-addiction-simulation
Agent-based simulation modeling the opioid overdose epidemic.

In Modeling the Prescription Opioid Epidemic by Battista, Pearcy and Strickland developed a system of differential equations that modeled opiate addiction 
by rates at which people are prescribed opiates. This prescription rate in turn affects the percentage of the population that is susceptible to addiction. 

The model assumes various parameters: 
1. Prescription rate per person per year
2. End prescription without addiction 
3. Illicit addiction rate based on Prescribed class
4. Illicit addiction rate based on addicted class
5. Prescription-induced addiction rate
6. Rate of addicted entry into rehabilitation
7. Successful treatment rate
8. Natural relapse rate of rehabilitation class
9. Natural death rate
10. Death rate of addicts

The system of differential equations proposed in Modeling the Prescription Opioid Epidemic is easily solved numerically using Euler’s method. 

A model based on solutions to these equations with Euler's Method can be found in diff_eq.py

An agent-based simulation model is also available in ABS.py 

To make this ABS model, all the parameters are used in the differential equation model with the exception of the natural death rate and death rate of addicts.
The results of the agent-based simulation are verified by comparing the outputs of the models. Good agreement is found between the two models. 
The parameters are added to the Agent class such that the parameters are stochastic for each agent. They are initialized using a uniform distribution. 
Although using different distributions for each parameter would produce more accurate results, there is no data to determine what input distributions would be most
appropriate for this model. If these distributions are found in the future, the implementation would be easy, as just the initialization of each parameter in an agent 
would need to be changed. Additionally, there are death rate parameters that could be added to increase the model's accuracy. 

