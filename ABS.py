import numpy as np
import matplotlib.pyplot as plt
import random

class Agent:
  # Defining class for individual agent
  # Contains information about status
    def __init__(self, is_addicted, is_rehabilitated, is_prescribed, is_susceptible):
        # Boolean variables, sotring what group an agent is a part of
        self.is_addicted = is_addicted
        self.is_rehabilitated = is_rehabilitated
        self.is_prescribed = is_prescribed
        self.is_susceptible = is_susceptible

        self.alpha = random.uniform(0.1, 0.2)   # Perscription rate per person per year
        self.epsilon = random.uniform(0.8, 8)    # End perscription without addiction (rate 0.8-8)
        self.beta_p = random.normalvariate(0.00266, 0.0005)  # Illicit addiction rate based on P-Class
        self.beta_a = random.normalvariate(0.00094, 0.0002)  # Illicit addiction rate based on A-Class
        self.gamma = random.normalvariate(0.00744, 0.001)  # Perscription-induced addiction rate
        self.zeta = random.uniform(0.1, 0.3) # Rate of A entry into rehabilitation
        self.delta = random.uniform(0.05, 0.15) # Successful treatment rate
        self.sigma = random.uniform(0.8, 1)  # Natural relapse rate of R-class


def simulate_agents(num_agents : int) -> None:

  # initializing the number of addicted, rehabilitated, prescribed, and susceptible agents 
  num_addicted = int(A_init * num_agents) 
  num_rehabilitated = int(R_init * num_agents)
  num_prescribed = int(P_init * num_agents)
  num_susceptible = num_agents - num_addicted - num_rehabilitated - num_prescribed

  # initializing agents
  agents = [Agent(False, False, False, True) for _ in range(num_susceptible)]
  agents_addicted = [Agent(True, False, False, False) for _ in range(num_addicted)]
  for agent in agents_addicted: agents.append(agent)
  agents_rehabilitated = [Agent(False, True, False, False) for _ in range(num_rehabilitated)]
  for agent in agents_rehabilitated: agents.append(agent)
  agents_prescribed = [Agent(False, False, True, False) for _ in range(num_prescribed)]
  for agent in agents_prescribed: agents.append(agent)

  # initializing storeage arrays for percentage of agents in each class 
  S[0, 0] = num_susceptible/num_agents
  A[0, 0] = num_addicted/num_agents
  R[0, 0] = num_rehabilitated/num_agents
  P[0, 0] = num_prescribed/num_agents
  
  # Run through time
  for i in range(Ndt-1):

      # agent-by-agent class changes
      for agent in agents:
        if agent.is_susceptible:
          # susceptible agents that get addicted
          if np.random.rand() < agent.beta_a:
              agent.is_addicted = True
              agent.is_susceptible = False
          # susceptible agents that get prescribed 
          if agent.is_susceptible:
            if np.random.rand() < agent.alpha:
              agent.is_prescribed = True
              agent.is_susceptible = False
        elif agent.is_prescribed:
          # prescribed agents getting addicted
          if np.random.rand() < agent.gamma:
            agent.is_addicted = True
            agent.is_prescribed = False
          # prescribed agents returning to susceptible class
          if agent.is_prescribed:
            if np.random.rand() < agent.epsilon:
              agent.is_susceptible = True
              agent.is_prescribed = False
        elif agent.is_addicted:
          # addicted moving to rehab 
          if np.random.rand() < agent.zeta:
            agent.is_rehabilitated = True
            agent.is_addicted = False
        elif agent.is_rehabilitated:
          # rehabilitated moving back to susceptiable 
          if np.random.rand() < agent.delta:
            agent.is_rehabilitated = False
            agent.is_susceptible = True
          # rehabilitated getting addicted again 
          if agent.is_rehabilitated:
            if np.random.rand() < agent.sigma:
              agent.is_rehabilitated = False
              agent.is_addicted = True

      # updating the number of agents in each class   
      num_prescribed  = sum([1 for agent in agents if agent.is_prescribed])
      num_addicted  = sum([1 for agent in agents if agent.is_addicted])    
      num_rehabilitated = sum([1 for agent in agents if agent.is_rehabilitated])
      num_susceptible = sum([1 for agent in agents if agent.is_susceptible])

      # updating the percentages of agents in each class       
      S[0, i+1] = num_susceptible/num_agents
      A[0, i+1] = num_addicted/num_agents
      R[0, i+1] = num_rehabilitated/num_agents
      P[0, i+1] = num_prescribed/num_agents
  # Plotting
  plt.subplot(2, 2, 1)
  plt.plot(t, S[0, :])
  plt.xlabel('t (years)')
  plt.ylabel('Susceptible Population')

  plt.subplot(2, 2, 2)
  plt.plot(t, A[0, :])
  plt.xlabel('t (years)')
  plt.ylabel('Addicted Population')

  plt.subplot(2, 2, 3)
  plt.plot(t, R[0, :])
  plt.xlabel('t (years)')
  plt.ylabel('Rehabilitation Population')

  plt.subplot(2, 2, 4)
  plt.plot(t, P[0, :])
  plt.xlabel('t (years)')
  plt.ylabel('Prescribed Population')

# initializing time parameters
t0 = 0
tF = 200
dt = 1
Ndt = int((tF - t0) / dt)
t = np.linspace(t0, tF, Ndt)




#initialize arrays to store simulation results
S = np.zeros((1, Ndt))
A = np.zeros((1, Ndt))
R = np.zeros((1, Ndt))
P = np.zeros((1, Ndt))

S_init = 0.9905                   # initial percent of population susceptible to addiction 
A_init = 0.00136                  # initial percentage of population addicted to opioids 
R_init = 0.1 * A_init             # initial percentage of population recovered from opioid addiction 
P_init = 0.008                    # initial percentage of population prescribed to opioids

num_agents = 10000                #number of agents 
# Running simulation
simulate_agents(num_agents)

# Show plots
plt.style.use('ggplot')
plt.tight_layout()
plt.show()



