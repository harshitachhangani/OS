def sjf_non_preemptive():
    # Get the number of processes from the user
    num_processes = int(input("Enter the number of processes: "))

    # Create a list of processes, where each process is represented by a tuple (name, time)
    processes = []
    for i in range(num_processes):
        name = input(f"Enter the name of process {i+1}: ")
        time = int(input(f"Enter the time for process {name}: "))
        processes.append((name, time))

    # Sort the processes by their execution time (the second element of each tuple)
    processes.sort(key=lambda x: x[1])

    # Initialize lists for finish time, turnaround time, and waiting time
    finish_time = [0] * num_processes
    turnaround_time = [0] * num_processes
    waiting_time = [0] * num_processes

    # Calculate the finish time, turnaround time, and waiting time for each process
    for i in range(num_processes):
        if i == 0:
            # The first process finishes at its execution time
            finish_time[i] = processes[i][1]
        else:
            # The finish time of each subsequent process is the sum of the execution times of all previous processes
            finish_time[i] = finish_time[i-1] + processes[i][1]
        # Turnaround time is the time from arrival until completion of a process
        turnaround_time[i] = finish_time[i]
        # Waiting time is the time a process spends in the ready queue waiting for the CPU
        waiting_time[i] = turnaround_time[i] - processes[i][1]

    # Calculate the average turnaround time and average waiting time for all processes
    avg_turnaround_time = sum(turnaround_time) / num_processes
    avg_waiting_time = sum(waiting_time) / num_processes

    # Print the results
    print("\nProcess\tFinish Time\tTurnaround Time\tWaiting Time")
    for i in range(num_processes):
        print(f"{processes[i][0]}\t\t{finish_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")
    print(f"\nAverage turnaround time: {avg_turnaround_time:.2f}")
    print(f"Average waiting time: {avg_waiting_time:.2f}")

# Call the function to run the program
sjf_non_preemptive()

# output:
# Enter the number of processes: 4
# Enter the name of process 1: p1
# Enter the time for process p1: 8
# Enter the name of process 2: p2
# Enter the time for process p2: 4
# Enter the name of process 3: p3
# Enter the time for process p3: 9
# Enter the name of process 4: p4
# Enter the time for process p4: 5

# Process Finish Time     Turnaround Time Waiting Time
# p2              4               4               0
# p4              9               9               4
# p1              17              17              9
# p3              26              26              17

# Average turnaround time: 14.00
# Average waiting time: 7.50
