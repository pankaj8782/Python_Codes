import time as t
print()
user_input = int(input("Count Till: "))

start_t = t.time()
for i in range(user_input):
    # print(i+1) 
    # if you add this, this will make the code slower
    i += 1
end_t = t.time()
print()
print(f"Time taken {round(end_t - start_t,2)} seconds to count till {user_input}")
print()