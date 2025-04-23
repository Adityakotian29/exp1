# class BankerAlgorithm:
#     def __init__(self, processes, resources, allocated, max_claim):
#         self.processes = processes
#         self.resources = resources
#         self.allocated = allocated
#         self.max_claim = max_claim
#         self.available = resources.copy()

#     def is_safe_state(self):
#         work = self.available.copy()
#         finish = [False] * len(self.processes)
#         need = [[self.max_claim[i][j] - self.allocated[i][j] for j in range(len(self.resources))] for i in range(len(self.processes))]
#         safe_sequence = []

#         while True:
#             found = False
#             for i in range(len(self.processes)):
#                 if not finish[i] and all(need[i][j] <= work[j] for j in range(len(self.resources))):
#                     work = [work[j] + self.allocated[i][j] for j in range(len(self.resources))]
#                     finish[i] = True
#                     safe_sequence.append(self.processes[i])
#                     found = True

#             if not found:
#                 break

#         return all(finish), safe_sequence

#     def print_available_resources(self):
#         print("Available resources:")
#         print(self.available)

#     def print_remaining_need(self):
#         print("Remaining need:")
#         need = [[self.max_claim[i][j] - self.allocated[i][j] for j in range(len(self.resources))] for i in range(len(self.processes))]
#         for i in range(len(self.processes)):
#             print(f"Process {self.processes[i]}:", need[i])

# # Example usage
# if __name__ == "__main__":
#     processes = [0, 1, 2, 3, 4]
#     resources = [10, 5, 7]  # Available resources
#     allocated = [
#         [0, 1, 0],  # Allocation matrix for each process
#         [2, 0, 0],
#         [3, 0, 2],
#         [2, 1, 1],
#         [0, 0, 2]
#     ]
#     max_claim = [
#         [7, 5, 3],  # Maximum resources each process may claim
#         [3, 2, 2],
#         [9, 0, 2],
#         [2, 2, 2],
#         [4, 3, 3]
#     ]

#     banker = BankerAlgorithm(processes, resources, allocated, max_claim)
#     safe, sequence = banker.is_safe_state()

#     if safe:
#         print("System is in safe state.")
#         print("Safe sequence:", sequence)
#         banker.print_available_resources()
#         banker.print_remaining_need()
#     else:
#         print("System is in unsafe state. Deadlock detected.")


def banker_algo(processes,allocated,available,max_need):
    finish=[]
    need=[[0 for j in range(len(available))] for i in range(len(allocated))]
    for i in range(len(allocated)):
        for j in range(len(available)):
            need[i][j]=max_need[i][j]-allocated[i][j]
    print(need)
    while(len(finish)<len(processes)):
        for i in range(len(processes)):
            if(processes[i] in finish):
                continue
            safe=0
            for j in range(len(available)):
                if need[i][j]>available[j]:
                    break
                else:
                    safe+=1
            if safe==3:        
                finish.append(processes[i])
                for k in range(len(available)):
                    available[k]+=allocated[i][k]
    
    for i in range(len(processes)-1):
        print(finish[i],end='-->')

    print(finish[len(processes)-1])
processes=['P0','P1','P2','P3','P4']
available=[3,3,2]
allocated=[[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
max_need=[[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
(banker_algo(processes,allocated,available,max_need))


            
            
# import copy

# # Check if the system is in a safe state
# def isSafe(processes, available, allocation, need):
#     numProcesses = len(processes)
#     work = copy.copy(available)  # use copy to avoid mutating the original list
#     finish = [False] * numProcesses

#     while True:
#         found = False
#         for i in range(numProcesses):
#             # Ensure the 'need' condition is met for the unfinished process
#             if not finish[i] and all(need[i][j] <= work[j] for j in range(len(available))):
#                 found = True
#                 finish[i] = True  # Mark this process as completed
#                 # Release resources from this process
#                 for j in range(len(available)):
#                     work[j] += allocation[i][j]
#                 break
#         if not found:
#             break  # No more processes can proceed 
#     return all(finish)  # Return True if all processes are completed

# # Banker's Algorithm
# def bankersAlgo(processes, available, allocation, maxDemand):
#     numProcesses = len(processes)
#     numResources = len(available)
#     # Calculate 'need' based on max demand and current allocation
#     need = [[maxDemand[i][j] - allocation[i][j] for j in range(numResources)] for i in range(numProcesses)]

#     if isSafe(processes, available, allocation, need):
#         print("The system is in a safe state. Safe sequence:", processes)
#     else:
#         print("The system is in a deadlock state.")

# # Main block
# if __name__ == "__main__":
#     # Consistent process names
#     processes = ['P0', 'P1', 'P2', 'P3', 'P4']
#     available = [3, 3, 2]
#     allocation = [
#         [0, 1, 0],
#         [2, 0, 0],
#         [3, 0, 2],
#         [2, 1, 1],
#         [0, 0, 2]
#     ]
#     maxDemand = [
#         [7, 5, 3],
#         [3, 2, 2],
#         [9, 0, 2],
#         [2, 2, 2],
#         [4, 3, 3]
#     ]

#     bankersAlgo(processes, available, allocation, maxDemand)  # Call the function
    

        
        

