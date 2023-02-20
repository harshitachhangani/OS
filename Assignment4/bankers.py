# A Python3 program to implement the Banker's Algorithm
 
# Function to find the need of each process
def calculate_need(need, maxm, allot):
    for i in range(len(need)):
        for j in range(len(need[0])):
            need[i][j] = maxm[i][j] - allot[i][j]
 
# Function to find the system is in safe state or not
def is_safe(processes, avail, maxm, allot):
    need = [[0] * len(avail) for _ in range(len(processes))]
    calculate_need(need, maxm, allot)
    finished = [0] * len(processes)
    safe_sequence = []
    work = [a for a in avail]
 
    while 0 in finished:
        found = False
        for i in range(len(processes)):
            if finished[i] == 0:
                for j in range(len(avail)):
                    if need[i][j] > work[j]:
                        break
                else:
                    found = True
                    for j in range(len(avail)):
                        work[j] += allot[i][j]
                    finished[i] = 1
                    safe_sequence.append(processes[i])
        if not found:
            return (False, [])
 
    return (True, safe_sequence)
 
# Driver code
if __name__ == "__main__":
    # Total number of processes
    n_processes = 5
    # Total number of resources
    n_resources = 3
 
    # Available resources
    available = [3, 3, 2]
 
    # Maximum resources that can be allocated to each process
    maximum = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
 
    # Resources that are currently allocated to each process
    allocated = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
 
    # Check if the system is in safe state or not
    is_safe, safe_sequence = is_safe(list(range(n_processes)), available, maximum, allocated)
    if is_safe:
        print("The system is in safe state")
        print("Safe sequence is:", safe_sequence)
    else:
        print("The system is in unsafe state")
