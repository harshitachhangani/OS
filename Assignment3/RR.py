# Python3 program for implementation of 
# RR scheduling 
  
# Function to find the waiting time 
# for all processes 
def findWaitingTime(processes, n, bt, wt, quantum): 
    rem_bt = [0] * n
  
    # Copy the burst time into rt[] 
    for i in range(n): 
        rem_bt[i] = bt[i]
    t = 0 # Current time 
  
    # Keep traversing processes in round 
    # robin manner until all of them are
    # not done. 
    while(1):
        done = True
  
        # Traverse all processes one by
        # one repeatedly 
        for i in range(n):
              
            # If burst time of a process is greater 
            # than 0 then only need to process further 
            if (rem_bt[i] > 0) :
                done = False # There is a pending process
                  
                if (rem_bt[i] > quantum) :
                  
                    # Increase the value of t i.e. shows 
                    # how much time a process has been processed 
                    t += quantum 
  
                    # Decrease the burst_time of current 
                    # process by quantum 
                    rem_bt[i] -= quantum 
                  
                # If burst time is smaller than or equal  
                # to quantum. Last cycle for this process 
                else:
                  
                    # Increase the value of t i.e. shows 
                    # how much time a process has been processed 
                    t = t + rem_bt[i] 
  
                    # Waiting time is current time minus 
                    # time used by this process 
                    wt[i] = t - bt[i] 
  
                    # As the process gets fully executed 
                    # make its remaining burst time = 0 
                    rem_bt[i] = 0
                  
        # If all processes are done 
        if (done == True):
            break
              
# Function to calculate turn around time 
def findTurnAroundTime(processes, n, bt, wt, tat):
      
    # Calculating turnaround time 
    for i in range(n):
        tat[i] = bt[i] + wt[i] 
  
  
# Function to calculate average waiting 
# and turn-around times. 
def findavgTime(processes, n, bt, quantum): 
    wt = [0] * n
    tat = [0] * n 
  
    # Function to find waiting time
    # of all processes 
    findWaitingTime(processes, n, bt, 
                         wt, quantum) 
  
    # Function to find turn around time
    # for all processes 
    findTurnAroundTime(processes, n, bt,
                                wt, tat) 
  
    # Display processes along with all details 
    print("Processes    Burst Time     Waiting", 
                     "Time    Turn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
  
        total_wt = total_wt + wt[i] 
        total_tat = total_tat + tat[i] 
        print(" ", processes[i], "\t\t", bt[i], 
              "\t\t", wt[i], "\t\t", tat[i])
  
    print("\nAverage waiting time = %.5f "%(total_wt /n) )
    print("Average turn around time = %.5f "% (total_tat / n)) 
      
# Driver code 
if __name__ =="__main__":
      
    # Take user input for process IDs and burst times
    n = int(input("Enter the number of processes: "))

	 # Process id's
    proc = []
    for i in range(n):
        proc.append(int(input(f"Enter process ID for process {i+1}: ")))

    # Burst time of all processes
    burst_time = []
    for i in range(n):
        burst_time.append(int(input(f"Enter burst time for process {i+1}: ")))

    # Time quantum
    quantum = int(input("Enter time quantum: "))
    findavgTime(proc, n, burst_time, quantum)

# OUTPUT:

# Enter the number of processes: 3
# Enter process ID for process 1: 1
# Enter process ID for process 2: 2
# Enter process ID for process 3: 3
# Enter burst time for process 1: 10
# Enter burst time for process 2: 5
# Enter burst time for process 3: 8
# Enter time quantum: 2
# Processes    Burst Time     Waiting Time    Turn-Around Time
#   1              10              13              23
#   2              5               10              15
#   3              8               13              21

# Average waiting time = 12.00000
# Average turn around time = 19.66667



   
