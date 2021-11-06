class battery():
    def __init__(self, max_recharge_rate, max_capactity, efficiency):
        """
        battery config and recharge rate
        :param max_recharge_rate: float max recharge rate in w
        :param max_capactity: float unit in kw*h/1000, max capactity
        """
        self.max_recharge_rate = max_recharge_rate
        self.max_capactity = max_capactity
        self.efficiency = efficiency
        self.capacity = max_capactity
        print(f"Battery set complied: max_capactity = {self.max_capactity}\nmax_recharge_rate:{self.max_recharge_rate}")

    def discharge(self, discharge_target, log=False):
        # discharge_target_real: 真实的电池放电，但是target减少self.efficiency倍
        # discharge_target: 用电器计划从电池要走的电量
        discharge_target_real = discharge_target / self.efficiency
        if discharge_target_real <= self.max_recharge_rate:
            if discharge_target_real <= self.capacity:
                self.capacity -= discharge_target_real
                return 0
            else:
                self.capacity = 0
                if log:print(f"self.max_recharge_rate < discharge_target_real <= self.capacity: \t remain: {discharge_target - (discharge_target_real - self.capacity) * self.efficiency}")
                return discharge_target - (discharge_target_real - self.capacity) * self.efficiency

        else:
            if self.max_recharge_rate <= self.capacity:
                self.capacity -= self.max_recharge_rate
                if log:print(f"discharge_target_real <= self.max_recharge_rate <= self.capacity: \t remain: {discharge_target - self.max_recharge_rate * self.efficiency}")
                return discharge_target - self.max_recharge_rate * self.efficiency
            else:
                # capacity_current = self.capacity
                self.capacity = 0
                if log:print(f"disorder all cap\t remain:{discharge_target - self.capacity * self.efficiency}")
                return discharge_target - self.capacity * self.efficiency

    def charge(self, charge_target, log=False):
        charge_target_real = charge_target * self.efficiency
        if charge_target_real >= self.max_recharge_rate:

            if self.max_recharge_rate + self.capacity <= self.max_capactity:
                self.capacity += self.max_recharge_rate
                if log: print(f"max_rate < target & batter could not full \t remain:{charge_target - self.max_recharge_rate / self.efficiency}")
                return charge_target - self.max_recharge_rate / self.efficiency
            else:
                capacity_current = self.capacity
                self.capacity = self.max_capactity
                if log: print(f"max_rate < target & batter could full\t remain:{charge_target - (self.max_capactity - capacity_current) / self.efficiency}")
                return charge_target - (self.max_capactity - capacity_current) / self.efficiency
        else:
            if charge_target_real + self.capacity <= self.max_capactity:
                self.capacity += charge_target_real
                if log: print(f"max_rate > target & could not full\t remain:{0}")
                return 0
            else:
                current_capactity = self.capacity
                self.capacity = self.max_capactity
                if log: print(f"max_rate > target & could full\t remain:{charge_target - (self.max_capactity - current_capactity) / self.efficiency}")
                return charge_target - (self.max_capactity - current_capactity) / self.efficiency



if __name__ == '__main__':
    libattery = battery(700, 10000, 0.96)
    libattery.capacity = 200
    libattery.discharge(10000000)




