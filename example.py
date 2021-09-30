from Generator import Generator

if __name__ == "__main__":
    config = {
        'seed':123 ,
        'num_robots':3,
        'num_tasks':4,
        'map_size':10,
        'workload_lb':1 ,
        'workload_ub':4 ,
        'battery_lb':2 ,
        'battery_ub':10 
    }
    generator = Generator(**config).get_problem()
    for i in range(10):
        print(generator.__next__())