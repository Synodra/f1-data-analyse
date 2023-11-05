import pandas as pd

def get_driver_info(session):
    for idx, x in enumerate(session.drivers):
        if idx == 0:
            drivers_name = pd.DataFrame(session.get_driver(x)).T
        else:
            df = pd.DataFrame(session.get_driver(x)).T
            drivers_name = pd.concat([drivers_name,df])
    
    return drivers_name