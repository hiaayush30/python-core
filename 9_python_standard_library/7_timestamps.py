# we have basically 2 module for working with date and time => time(gives us timestamp) and datetime

import time

print(time.time()) # seconds after Jan 1 1970

def send_emailS():
    for i in range(10000):
        pass

start = time.time()
send_emailS()
end = time.time()
print(f"thhe method took {end-start} seconds")