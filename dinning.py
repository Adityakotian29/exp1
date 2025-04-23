import threading
import time
import random

num_philosophers = 5
num_forks = 5
meals_per_philosopher = 3

forks = [threading.Semaphore(1) for _ in range(num_forks)]
mutex = threading.Semaphore(1)

def philosophers(index, meals):
    meals_eaten = 0
    while meals_eaten < meals:
        print(f"Philosopher{index} is thinking...")
        time.sleep(random.randint(1, 5))
        
        mutex.acquire()
        left_fork = index
        right_fork = (index + 1) % num_philosophers
        forks[left_fork].acquire()
        forks[right_fork].acquire()
        mutex.release()
        
        print(f"Philosopher{index} is eating...")
        time.sleep(random.randint(1, 5))
        
        forks[left_fork].release()
        forks[right_fork].release()
        
        meals_eaten += 1

threads = []
for i in range(num_philosophers):
    threads.append(threading.Thread(target=philosophers, args=(i, meals_per_philosopher)))
    print(threads)
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("All philosophers have finished.")

        