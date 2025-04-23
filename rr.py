def round_robin(processes, quantum):
    total_turnaround_time = total_waiting_time = 0
    while processes:
        process = processes.pop(0)
        if process['burst_time'] > quantum:
            print(f"Process {process['id']} executed for {quantum} units")
            total_waiting_time += (process['burst_time'] - quantum)
            process['burst_time'] -= quantum
            processes.append(process)
        else:
            print(f"Process {process['id']} executed for {process['burst_time']} units")
            total_turnaround_time += process['burst_time']
    num_processes = len(processes)
    avg_turnaround_time = total_turnaround_time / num_processes
    avg_waiting_time = total_waiting_time / num_processes
    print(f"Average turnaround time: {avg_turnaround_time}")
    print(f"Average waiting time: {avg_waiting_time}")

# Example usage
processes = [
    {'id': 1, 'burst_time': 10},
    {'id': 2, 'burst_time': 5},
    {'id': 3, 'burst_time': 8}
]
quantum = 2
round_robin(processes, quantum)


def shortest_job_first(processes):
    total_turnaround_time = total_waiting_time = 0
    sorted_processes = sorted(processes, key=lambda x: x['burst_time'])
    for i in range(len(sorted_processes)):
        process = sorted_processes[i]
        print(f"Process {process['id']} executed for {process['burst_time']} units")
        total_waiting_time += sum(p['burst_time'] for p in sorted_processes[:i])
        total_turnaround_time += sum(p['burst_time'] for p in sorted_processes[:i+1])
    num_processes = len(sorted_processes)
    avg_turnaround_time = total_turnaround_time / num_processes
    avg_waiting_time = total_waiting_time / num_processes
    print(f"Average turnaround time: {avg_turnaround_time}")
    print(f"Average waiting time: {avg_waiting_time}")

# Example usage
processes = [
    {'id': 1, 'burst_time': 10},
    {'id': 2, 'burst_time': 5},
    {'id': 3, 'burst_time': 8}
]
shortest_job_first(processes)

