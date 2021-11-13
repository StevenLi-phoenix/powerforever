# author: Stevenli
# time: 2021.11.12
# final main V0.1


import csv
import json
import sys
import threading
import time

import numpy as np
import pandas as pd


class calculate:
    def __init__(self, avg_data=True):
        # global config
        self.log = logger("batteryChoiceEvaluation", 1000)
        # self.max_recharge_rate = 7000 # 最大充电速率7kw
        # self.max_solar_generation_rate = 20000 # 最大太阳能发20kwh

        self.max_thread = 8
        self.threadLimiter = threading.BoundedSemaphore(self.max_thread)

        self.base = "./"
        iter_file_path = f"{self.base}iter.csv"
        self.npy = f"{self.base}npy/"
        self.plot = f"{self.base}plot/"

        # load consume and produce data
        self.solarrad = np.load(self.npy + "solarrad.npy")
        spring24 = np.load(self.npy + "spring24.npy")
        summar24 = np.load(self.npy + "summer24.npy")
        autumn24 = np.load(self.npy + "autumn24.npy")
        winter24 = np.load(self.npy + "winter24.npy")
        if avg_data:
            spring24 = np.sum(spring24, axis=0) / 1000
            summar24 = np.sum(summar24, axis=0) / 1000
            autumn24 = np.sum(autumn24, axis=0) / 1000
            winter24 = np.sum(winter24, axis=0) / 1000
        consume = []
        for name in [spring24, summar24, autumn24, winter24]:
            for i in range(80):
                consume.append(list(name))
        self.consume = np.array(consume).reshape(-1, ) / 1000

        # load iter data
        self.iter_data = pd.read_csv(iter_file_path)

        self.write_list = []
        with open("battery_evaluate_ouput.csv", "w") as f:
            self.writter = csv.writer(f)
            self.writter.writerow(
                ["max_nopower_count", "Evaluate Score", "name", "max_cap", "other_info", "year_round_status",
                 "current_cap"])

    def evaluate(self, batteries=None, ret = False):

        max_nopower_count = 0

        if batteries is None:
            batteries = [battery("default", 7000, 10000, 0.96, 100)]
            # self.log.write_error("No battery option input try default instead")
        current_cap = []
        status = True
        year_round_status = []
        for hour in range(320 * 24):

            # extraxt data for power consume list and power produce list
            charge = self.solarrad[hour]
            discharge = self.consume[hour]
            # calculate current capacity of batteries & add list
            sum_cap = sum([i.capacity for i in batteries])
            assert sum_cap >= 0
            current_cap.append(sum_cap)
            try:
                if charge > discharge:
                    pass
            except Exception as e:
                raise KeyboardInterrupt(f"\n{charge}\n{discharge}\n{e}")

            if charge > discharge:
                # put power to battery if chaege larger than discharge
                remain = charge - discharge
                for bat in batteries:   remain = bat.charge(remain)
                # reset status to true
                status = True

            elif charge < discharge:
                # pull power form battery if discharge larger than charge
                pull = discharge - charge
                for bat in batteries:   pull = bat.discharge(pull)

                # if power can not suppply the use of user
                if pull > 0:
                    # self.log.write(f"{charge}, {discharge}, {sum([i.capacity for i in batteries])}, note: battery is later for one")
                    # self.log.write(f"No avaliable energy on day:{hour // 24} hour:{hour}")
                    # if not status: pass
                    if status:
                        max_nopower_count += 1
                        # set status to false and max_count -1
                        status = False
                        # self.log.write( f"No avaliable energy on day:{hour // 24}, {sum([i.capacity for i in batteries])}, count_increase, set status to false")

            else:
                self.log.write("balance")
            if status:
                year_round_status.append(1)
            else:
                year_round_status.append(0)
        # raise KeyboardInterrupt("I am down")
        # "max_nopower_count", "Evaluate Score", "name","max_cap","other_info", "year_round_status", "current_cap"
        if max_nopower_count <= 10:
            score = self.choice_analysis()
            self.write_list.append([max_nopower_count, score, json.dumps([i.name for i in batteries]),
                                    sum([i.max_capactity for i in batteries]), json.dumps([i.info() for i in batteries]),
                                    json.dumps(year_round_status), json.dumps(current_cap)])
        self.threadLimiter.release()
        # print("End thread")
        print("\t"+str(max_nopower_count), end="      ")
        if ret: return year_round_status, current_cap, max_nopower_count

    def choice_analysis(self):
        """
        todo：这里加大刘的程序
        :return: 
        """
        return 0

    def checkCSVwritter(self):
        """
        todo: 检查文件导入顺序，是否与默认排序相同
        :return:
        """
        while True:
            time.sleep(1)
            if len(self.write_list) > 10:
                with open("battery_evaluate_ouput.csv", "a+") as f:
                    write_list_copy = self.write_list
                    self.write_list = []
                    writer = csv.writer(f)
                    writer.writerows(write_list_copy)
    def write_all(self):
        for i in range(self.max_thread):
            self.threadLimiter.acquire()
        with open("battery_evaluate_ouput.csv", "a+") as f:
            write_list_copy = self.write_list
            self.write_list = []
            writer = csv.writer(f)
            writer.writerows(write_list_copy)

    def main(self):
        """
        todo: 梳理结构，优化运行
        todo：尝试使多线程返回东西
        """
        name_arrange = pd.read_csv("iter.csv").values
        battery_data_namedic = {}
        for i in pd.read_csv("BatteriesCSV2.csv").values:
            battery_data_namedic[i[0]] = i[1:]
        threading.Thread(target=self.checkCSVwritter).start()
        threads = []
        for f in range(len(name_arrange)):
            bats = []
            for i in name_arrange[f, 0].split(";")[:-1]:
                obj = battery_data_namedic[i]
                capacity = obj[5]
                cost = obj[6]
                efficiency = obj[4]
                power = obj[7]
                bats.append(battery(i, capacity, power, efficiency, cost))
            self.threadLimiter.acquire()
            t = threading.Thread(target=self.evaluate, args=(bats,))
            threads.append(t)
            print(f"\rStart thread {t}", end="")
            t.start()
        self.write_all()


class battery:
    def __init__(self, name, max_recharge_rate, max_capactity, efficiency, cost, log=False):
        """
        todo: 优化导入和battery的注释
        todo: 检查当前充放电逻辑
        battery config and recharge rate
        :param max_recharge_rate: float max recharge rate in w
        :param max_capactity: float unit in kw*h/1000, max capactity
        """
        self.name = name
        self.max_recharge_rate = max_recharge_rate
        self.max_capactity = max_capactity
        self.efficiency = efficiency
        assert type(efficiency) == float
        self.capacity = max_capactity
        self.log = All_battery_log
        self.logstatus = log
        self.log_main = False
        self.write_to_log = False
        self.cost = cost
        if log: print(
            f"Battery set complied: max_capactity = {self.capacity}\nmax_recharge_rate:{self.max_recharge_rate}, eff{efficiency}, cost{cost}")
        self.log.write(
            f"Battery set complied: max_capactity = {self.capacity}, max_recharge_rate:{self.max_recharge_rate}, efficiency:{efficiency},cost:{cost}")

    def info(self):
        return {
            "name": self.name,
            "max_recharge_rate": self.max_recharge_rate,
            "max_capactity": self.max_capactity,
            "efficiency": self.efficiency,
            "cost": self.cost,
        }

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
                if self.write_to_log: self.log.write(
                    f"self.max_recharge_rate < discharge_target_real <= self.capacity: \t remain: {discharge_target - (discharge_target_real - self.capacity) * self.efficiency}",
                    verbose=log)
                return discharge_target - self.capacity * self.efficiency

        else:
            if self.max_recharge_rate <= self.capacity:
                self.capacity -= self.max_recharge_rate
                if self.write_to_log: self.log.write(
                    f"discharge_target_real <= self.max_recharge_rate <= self.capacity: \t remain: {discharge_target - self.max_recharge_rate * self.efficiency}",
                    verbose=log)
                return discharge_target - self.max_recharge_rate * self.efficiency
            else:
                # capacity_current = self.capacity
                self.capacity = 0
                if self.write_to_log: self.log.write(
                    f"disorder all cap\t remain:{discharge_target - self.capacity * self.efficiency}", verbose=log)
                return discharge_target - self.capacity * self.efficiency

    def charge(self, charge_target, log=False):
        if self.log_main: self.log.write(f"Charge {charge_target}， current cap : {self.capacity}")
        charge_target_real = charge_target * self.efficiency
        if self.logstatus: log = True
        if charge_target_real >= self.max_recharge_rate:
            if self.max_recharge_rate + self.capacity <= self.max_capactity:
                self.capacity += self.max_recharge_rate
                if self.write_to_log: self.log.write(
                    f"max_rate < target & batter could not full \t remain:{charge_target - self.max_recharge_rate / self.efficiency}",
                    verbose=log)
                return charge_target - self.max_recharge_rate / self.efficiency
            else:
                capacity_current = self.capacity
                self.capacity = self.max_capactity
                if self.write_to_log: self.log.write(
                    f"max_rate < target & batter could full\t remain:{charge_target - (self.max_capactity - capacity_current) / self.efficiency}",
                    verbose=log)
                return charge_target - (self.max_capactity - capacity_current) / self.efficiency
        else:
            if charge_target_real + self.capacity <= self.max_capactity:
                self.capacity += charge_target_real
                if self.write_to_log: self.log.write(f"max_rate > target & could not full\t remain:{0}")
                return 0
            else:
                current_capactity = self.capacity
                self.capacity = self.max_capactity
                if self.write_to_log: self.log.write(
                    f"max_rate > target & could full\t remain:{charge_target - (self.max_capactity - current_capactity) / self.efficiency}",
                    verbose=log)
                return charge_target - (self.max_capactity - current_capactity) / self.efficiency


class logger:
    def __init__(self, name=sys.argv[0], array_limit=10000):
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


if __name__ == '__main__':
    """
    :todo: 梳理日志写法，梳理文件结构
    """
    All_battery_log = logger("battery", 100000)
    calculate().main()
