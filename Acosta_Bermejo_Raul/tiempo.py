#
import time 
print("Medir tiempo de ejecucion")

start_time = time.time()
print(f"Start: {start_time}")

#----------------
#time.sleep(3)
time.sleep(0.75)
#----------------

end_time = time.time()
print(f"End: {end_time}")
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.2f} seconds")
#--------------------------------------------------
print()
print(f"Started: {time.strftime('%X')}")
time.sleep(0.3)
time.sleep(5)
print(f"Ended: {time.strftime('%X')}")

#-------------------------------
print()
start_time = time.perf_counter_ns()
time.sleep(2)
end_time = time.perf_counter_ns()
elapsed_time_ns = end_time - start_time

print(f"Elapsed time: {elapsed_time_ns} nanoseconds")

elapsed_time = elapsed_time_ns / 1_000_000_000
print(f"Elapsed time: {elapsed_time:.2f} seconds")
