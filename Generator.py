import numpy as np 

# Problem Generator Class. 
class Generator:
    def __init__(self, 
                    seed=123, 
                    num_robots=3, 
                    num_tasks=4, 
                    map_size=10, 
                    workload_lb=1, 
                    workload_ub=10, 
                    battery_lb=10000,
                    battery_ub=100000
        ):
        
        self.set_seed(seed)
        self.num_robots = num_robots
        self.num_tasks = num_tasks 
        self.map_size = map_size 
        self.workload_lb = workload_lb
        self.workload_ub = workload_ub
        self.battery_lb = battery_lb 
        self.battery_ub = battery_ub

    def get_problem(self):
        while True:
            robots = [[0, 0] for _ in range(self.num_robots)]
            tasks = [[0,0]] 
            while len(tasks) <= self.num_tasks: 
                p = np.random.randint(1,self.map_size, size=(2,)).tolist()
                if p not in tasks:
                    tasks.append(p)
            workload = [0] + [np.random.randint(self.workload_lb, self.workload_ub) for r in range(self.num_tasks)]
            battery = [np.random.randint(self.battery_lb, self.battery_ub) for r in range(self.num_robots)]
            yield robots, tasks, workload, battery

    def get_manual_problem(self):
        not NotImplementedError()
 
    def set_seed(self, seed):
        self._seed = seed
        np.random.seed(self._seed)

