from main import get_config
import numpy as np

config = get_config()

def sporadic(event):
    if np.random.rand() < float(config["stats"]["sporadic_random"]):
        rng = np.random.default_rng()
        event["function_type"] = "weibull"
        event["lambda"] = 3600*np.random.randint(5,48)
        event["k"] = np.random.rand() * 5 
        event["points"] = np.array(rng.weibull(event["k"], 10000))
        event["points"] *= event["lambda"]
        event["points"] = np.cumsum(event["points"])
        event["points"] = event["points"][:np.searchsorted(event["points"],int(config["stats"]["max_time"]))]
    else:
        event["function_type"] = "periodic"
        
    return

def dependent():
    return

def gen_window():
    return