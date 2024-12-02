from datetime import datetime, timedelta
from random import randint

with open('test.log', 'w') as file:
    for i in range(1000):
        rand_time = datetime.now() - timedelta(seconds=randint(0, 1000000))
        start_dt = datetime.strftime(rand_time - timedelta(seconds=randint(0, 1000)), "%Y-%m-%d %H:%M")
        end_dt = datetime.strftime(rand_time + timedelta(seconds=randint(0, 1000)), "%Y-%m-%d %H:%M")
        file.write(f"FROM:{start_dt} TO:{end_dt}\n")
