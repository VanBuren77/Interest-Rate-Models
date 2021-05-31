import numpy as np
import matplotlib.pyplot as plt
import math


maturity = 1
starting_price = 100
strike_price = 100
volatility = 0.10
risk_free_rate = 0.05

time_periods = 500
dt = maturity / time_periods
mc_simulation_count = 10000

payoff = 0
premium = 0

# np.random.seed(2021)

import random

# Box-Muller Uniform Transform:
def generate_normal(mu, sigma):
    u = random.random()
    v = random.random()

    z1 = math.sqrt(-2 * math.log(u)) * math.sin(2 * math.pi * v)
    z2 = math.sqrt(-2 * math.log(u)) * math.cos(2 * math.pi * v)

    x1 = mu + z1 * sigma
    x2 = mu + z2 * sigma

    return x2

payoffs = np.zeros(mc_simulation_count)

# Monte Carlo Simulation Loop:
for i in range(mc_simulation_count):
    simulation = np.zeros(time_periods)
    # print(np.size(simulation))
    simulation[0] = starting_price

    # Time Integration Loop:
    for j in range(1, time_periods, 1):
        epsilon = np.random.normal()
        # epsilon = generate_normal(0, 1)
        simulation[j] =  simulation[j-1] * (1 + risk_free_rate * dt + volatility * math.sqrt(dt) * epsilon)
    
    diff = simulation[time_periods - 1] - strike_price
    payoff += max(diff, 0.0)
    print("Simulation: " + str(i) + " Payoff = " + str(payoff))
    payoffs[i] = max(diff, 0.0)
    plt.plot(simulation)

    # if i > 25:
    #     break

plt.show()
# plt.scatter(x=range(mc_simulation_count), y=payoffs)
# plt.show()
print("-----------------------------------------")
premium = math.exp(-risk_free_rate*maturity)*(payoff / mc_simulation_count)
print("Premium1 = " + str(round(premium, 5)))
print("-----------------------------------------")

# print(payoff)

