import time, sys, threading


class battery():
    def __init__(self, max_recharge_rate, max_capactity, efficiency, cost, log=False):
        """
        battery config and recharge rate
        :param max_recharge_rate: float max recharge rate in w
        :param max_capactity: float unit in kw*h/1000, max capactity
        """
        self.max_recharge_rate = max_recharge_rate
        self.max_capactity = max_capactity
        self.efficiency = efficiency
        self.capacity = max_capactity
        self.log = All_battery_log
        self.logstatus = log
        self.log_main = True
        self.write_to_log = False
        self.cost = cost
        if log: print(
            f"Battery set complied: max_capactity = {self.capacity}\nmax_recharge_rate:{self.max_recharge_rate}, eff{efficiency}, cost{cost}")
        self.log.write(f"Battery set complied: max_capactity = {self.capacity}, max_recharge_rate:{self.max_recharge_rate}, efficiency:{efficiency},cost:{cost}")

    def discharge(self, discharge_target, log=False):
        # discharge_target_real: 真实的电池放电，但是target减少self.efficiency倍
        # discharge_target: 用电器计划从电池要走的电量
        if self.logstatus: log = True
        if self.log_main: self.log.write(f"Discharge {discharge_target}， current cap : {self.capacity}")
        discharge_target_real = discharge_target / self.efficiency
        if discharge_target_real <= self.max_recharge_rate:
            if discharge_target_real <= self.capacity:
                self.capacity -= discharge_target_real
                return 0
            else:
                self.capacity = 0
                if self.write_to_log :self.log.write(f"self.max_recharge_rate < discharge_target_real <= self.capacity: \t remain: {discharge_target - (discharge_target_real - self.capacity) * self.efficiency}",verbose=log)
                return discharge_target - self.capacity * self.efficiency

        else:
            if self.max_recharge_rate <= self.capacity:
                self.capacity -= self.max_recharge_rate
                if self.write_to_log :self.log.write(f"discharge_target_real <= self.max_recharge_rate <= self.capacity: \t remain: {discharge_target - self.max_recharge_rate * self.efficiency}",verbose=log)
                return discharge_target - self.max_recharge_rate * self.efficiency
            else:
                # capacity_current = self.capacity
                self.capacity = 0
                if self.write_to_log :self.log.write(f"disorder all cap\t remain:{discharge_target - self.capacity * self.efficiency}",verbose=log)
                return discharge_target - self.capacity * self.efficiency

    def charge(self, charge_target, log=False):
        if self.log_main: self.log.write(f"Charge {charge_target}， current cap : {self.capacity}")
        charge_target_real = charge_target * self.efficiency
        if self.logstatus: log = True
        if charge_target_real >= self.max_recharge_rate:
            if self.max_recharge_rate + self.capacity <= self.max_capactity:
                self.capacity += self.max_recharge_rate
                if self.write_to_log: self.log.write(f"max_rate < target & batter could not full \t remain:{charge_target - self.max_recharge_rate / self.efficiency}",verbose=log)
                return charge_target - self.max_recharge_rate / self.efficiency
            else:
                capacity_current = self.capacity
                self.capacity = self.max_capactity
                if self.write_to_log: self.log.write(f"max_rate < target & batter could full\t remain:{charge_target - (self.max_capactity - capacity_current) / self.efficiency}",verbose=log)
                return charge_target - (self.max_capactity - capacity_current) / self.efficiency
        else:
            if charge_target_real + self.capacity <= self.max_capactity:
                self.capacity += charge_target_real
                if self.write_to_log: self.log.write(f"max_rate > target & could not full\t remain:{0}")
                return 0
            else:
                current_capactity = self.capacity
                self.capacity = self.max_capactity
                if self.write_to_log: self.log.write(f"max_rate > target & could full\t remain:{charge_target - (self.max_capactity - current_capactity) / self.efficiency}",verbose=log)
                return charge_target - (self.max_capactity - current_capactity) / self.efficiency


class logger():
    def __init__(self, name = sys.argv[0], array_limit = 10000):
        self.logaddr = f"{name}.log"
        self.verbose = True
        self.array = []
        self.array_limit = array_limit
        with open(self.logaddr, "w") as f: f.write(
            str(time.strftime("%H:%M:%S", time.localtime())) + str("\tLogger init\n"))

    def write(self, content=None, verbose=False):
        if verbose: print(content)
        self.array.append(content)
        if len(self.array) > self.array_limit:
            if verbose: print(f"update log at {self.logaddr}")
            t = threading.Thread(target=self.append_log)
            t.start()

    def append_log(self):
        array_copy = self.array.copy()
        self.array = []
        with open(self.logaddr, "a+") as f:
            for content in array_copy:
                f.write(str(str(time.strftime("%H:%M:%S", time.localtime())) + "\t[info]" + "\t" + content + "\n\n"))

    def write_error(self, error, content=None, verbose=False):
        if verbose: print(error, content)
        with open(self.logaddr, "a+") as f:
            f.write(str(str(time.strftime("%H:%M:%S", time.localtime())) + "\t[error]" + str(error) + "\t" + str(
                content) + "\n\n"))

All_battery_log = logger("battery", 100000)

if __name__ == '__main__':
    libattery = battery(700, 10000, 0.96)
    libattery.capacity = 200
    for i in range(100):
        libattery.charge(1000)
        libattery.discharge(1000)
