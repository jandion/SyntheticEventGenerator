import configparser
import numpy as np
import scipy as scp
import eventGenerators

def get_config():
    config = configparser.ConfigParser()
    config.read("./config.cfg")
    return config

if __name__ == "__main__":
    config = get_config()
    events = []
    for i in range(int(config["stats"]["num_events"])):
        event = { "index": i }
        if np.random.rand() < float(config["stats"]["sporadic"]):
            event["type"] = "sporadic"
            eventGenerators.sporadic(event)
        else:
            event["type"] = "dependant"
        events.append(event)
    print(events)