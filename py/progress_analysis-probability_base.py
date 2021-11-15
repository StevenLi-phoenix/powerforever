#!/usr/bin/env python
# coding: utf-8

# In[1]:


from battery import battery, logger
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
#global config
log = logger("differenceSolarConsume", 100)
max_recharge_rate = 7000 # 最大充电速率7kw
max_solar_generation_rate = 20000 # 最大太阳能发20kwh
# batteries = [battery(max_recharge_rate, 100000, 0.96)]
base = "/Users/lishuyu/PycharmProjects/solarPowerEstimate/"
npy = f"{base}npy/"
plot = f"{base}plot/probability_base/"

solarrad = np.load(npy+"solarrad.npy")
spring24 = np.load(npy+"spring24.npy").reshape(-1,)
summar24 = np.load(npy+"summar24.npy").reshape(-1,)
autumn24 = np.load(npy+"autumn24.npy").reshape(-1,)
winter24 = np.load(npy+"winter24.npy").reshape(-1,)

plt.plot(spring24.T)
plt.show()
plt.plot(spring24[0])
plt.show()
plt.plot(solarrad[:24]*1000)
# spring24 = np.sum(spring24, axis=0)/1000
spring24 = spring24/2
plt.plot(spring24)
plt.show()


# In[5]:


def main(max_nopower_count, power_recharge_rate = max_recharge_rate):
    count = max_nopower_count

    #battery.battery()
    #max_nopower_count = 1
    for decline in range(40000, 0, -1000):
        status = True
        current_cap = []
        hour_count = 0
        max_nopower_count = count
        batteries = [battery(power_recharge_rate, decline, 0.96)]
        for day in range(len(solarrad)//24):
            # print("-", end="")
            for hour in range(24):
                hour_count += 1
                charge = solarrad[day*24+hour] * 1000
                discharge = spring24[day*24+hour]
                # print(charge, discharge)
                if charge > discharge:
                    remain = charge - discharge
                    for bat in batteries:
                        remain = bat.charge(remain, log=False)
                elif charge < discharge:
                    sum_cap_cache = sum([i.capacity for i in batteries])
                    if sum_cap_cache<0: raise IndexError("logic errror")
                    pull = discharge - charge
                    for bat in batteries:
                        pull = bat.discharge(pull, log=False)
                    if pull == 0 and not status:
                        log.write("count_reset cause pull is zero")
                        status = True
                    if pull > 0:
                        log.write(f"{charge}, {discharge}, {sum([i.capacity for i in batteries])}, note: battery is later for one")
                        log.write(f"No avaliable energy on day:{day} hour:{hour}")
                        if status:
                            max_nopower_count-=1
                            log.write("count_decrease, set status to false")
                            status = False
                        if max_nopower_count == 0:
                            log.write("Break as count == 0")
                            break
                else:
                    log.write("balance")
                current_cap.append(sum([i.capacity for i in batteries]))
            if max_nopower_count == 0:
                break
        if max_nopower_count == 0:
            sum_cap = 0
            for bat in batteries:
                sum_cap += bat.capacity
            current_cap.append(sum_cap)
            plt.plot(current_cap[-24:], label="battery")
            plt.plot(solarrad[day*24+hour-24:day*24+hour]*1000, label="produce")
            plt.plot(spring24[day*24+hour-24:day*24+hour], label="consume")
            plt.title(f"Last ppower supply at Day {day} at Hour {hour}")
            plt.ylabel("mAh")
            plt.xlabel(f"max count{count}; running {hour_count} hours ({hour_count//24} days);capacity:{decline};recharge_rate:{power_recharge_rate}", )
            plt.legend(loc="upper left")
            plt.grid()
            log.write(f"Save plot to {plot}Electric_decline_plots/Electric_decline{decline}_PRR_{power_recharge_rate}_{count}.png")
            plt.savefig(f"{plot}Electric_decline_plots/Electric_decline{decline}_PRR_{power_recharge_rate}_{count}.png")
            # plt.show()
            plt.close()
            return decline
        log.write(f"decline at : {str(decline)}")


# In[7]:


if __name__ == '__main__':
    all_cap = []
    for recharge_rate_var in range(10000, 1000, -100):
        cap = []
        for capacity_var in range(1, 11):
            cap.append([main(capacity_var, recharge_rate_var), recharge_rate_var])
            print(capacity_var, recharge_rate_var)
        all_cap.append(cap)
    for i in all_cap:
        plt.plot(np.array(i).T[0], label = str(np.array(i).T[1][0]), alpha=1)
    plt.legend(loc="upper left")
    plt.grid()
    plt.title(f"compareRelationship_{np.array(i).T[1][0]}")
    plt.savefig(f"{plot}compareRelationship_{np.array(i).T[1][0]}.png")
    plt.show()


# In[14]:





# In[7]:





# In[10]:


spring24[-1]


# In[ ]:




