import time as t


n = 10000000

init_time = t.time()

for i in range(0,n):
    a= 2

end_time = t.time()
time = end_time-init_time

print(time)
