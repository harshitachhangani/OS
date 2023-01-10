def FCFS():
  # Create an empty list to store the processes
  pro = []

  # Prompt the user to enter the processes
  while True:
    name = input("Enter the name of the process (or enter 'done' to exit): ")
    if name == "done":
      break
    time = int(input("Enter the time it takes to complete the process: "))
    pro.append((name, time))

  # Get the number of processes
  n = len(pro)

  # Determine the waiting time for each process
  wait_t = [0] * n
  for i in range(1, n):
    wait_t[i] = pro[i - 1][1] + wait_t[i - 1]

  # Determine the turnaround time for each process
  turnaround_t = [0] * n
  for i in range(n):
    turnaround_t[i] = pro[i][1] + wait_t[i]

  # Determine the average waiting time
  total_wait_t = sum(wait_t)
  avg_wait_t = total_wait_t / n

  # Determine the average turnaround time
  tot_turnaround_t = sum(turnaround_t)
  avg_turnaround_t = tot_turnaround_t / n

  # Print the results
  print("Process\tWaiting Time\tTurnaround Time")
  for i in range(n):
    print(f"{pro[i][0]}\t\t{wait_t[i]}\t\t{turnaround_t[i]}")
  print(f"Average waiting time: {avg_wait_t}")
  print(f"Average turnaround time: {avg_turnaround_t}")

# Test the FCFS function
FCFS()
