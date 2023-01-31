import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

eps = 0.1  # epsilon value
i = 0      # counter for the number of days, i.e., 300

R_lapinoz = []   
R_tacobell = []   # arrays storing rewards offered by each restaurant 
R_mcd = []

values_lapinoz = []   
values_tacobell = []    # arrays storing averages of utilities of each restaurant, i.e., values
values_mcd = []
all_vals = [0, 0, 0]    # array holding most recent values of each restaurant

def reward(rest):
    if rest == "lapinoz":
        R_lapinoz.append(np.random.randint(low=4, high=13))
        values_lapinoz.append(np.mean(R_lapinoz))
        all_vals[0] = values_lapinoz[-1]
    elif rest == "tacobell":
        R_tacobell.append(np.random.randint(low=5, high=16)) 
        values_tacobell.append(np.mean(R_tacobell))
        all_vals[1] = values_tacobell[-1]
    elif rest == "mcd":
        R_mcd.append(np.random.randint(low=3, high=8))
        values_mcd.append(np.mean(R_mcd))
        all_vals[2] = values_mcd[-1]
    else:
        print("Error, invalid restaurant")

while i<=300:   
    prob = np.random.rand()    
    if prob<=eps:
        rest_val = np.random.rand()
        if rest_val<=0.33:           # when exploration is chosen, there is a 1/3rd chance of going to each restaurant
            rest = "lapinoz"
            reward(rest)   
        elif rest_val>0.33 and rest_val<=0.66:
            rest = "tacobell"
            reward(rest)
        else:
            rest = "mcd"
            reward(rest)

    elif prob>eps:                
        rest_ind = all_vals.index(max(all_vals))    # when exploitation is chosen, we go to the restaurant with the max value up till that point
        if rest_ind == 0:
            rest = "lapinoz"
            reward(rest)
        elif rest_ind == 1:
            rest = "tacobell"
            reward(rest)
        elif rest_ind == 2:
            rest = "mcd"
            reward(rest)
        else:
            print("Error, invalid restaurant for exploiting")
    i+=1

print(all_vals)
print(R_lapinoz)
std_lapinoz = np.std(R_lapinoz)
std_tacobell = np.std(R_tacobell)
std_mcd = np.std(R_mcd)

mean_lapinoz = all_vals[0]
mean_tacobell = all_vals[1]
mean_mcd = all_vals[2]

xaxis = np.arange(-10, 20, 0.01)
plt.plot(xaxis, norm.pdf(xaxis, mean_lapinoz, std_lapinoz))
plt.plot(xaxis, norm.pdf(xaxis, mean_tacobell, std_tacobell))
plt.plot(xaxis, norm.pdf(xaxis, mean_mcd, std_mcd))

plt.plot(mean_lapinoz,0, marker='o', color='b')
plt.plot(mean_tacobell,0, marker='o', color='orange')
plt.plot(mean_mcd,0, marker='o', color='g')

plt.legend(["La Pinoz", "TacoBell", "McD", mean_lapinoz, mean_tacobell, mean_mcd])
plt.xlabel("Utility/Reward by each restaurant")
plt.title("Utility Distributions")
plt.show()
