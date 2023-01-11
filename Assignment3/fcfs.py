def FCFS():
  pro = []

  while True:
    name = input("Enter the process name or number and 'finish' to exit: ")
    if name == "finish":
      break
    time = int(input("Enter the time it takes to complete the process: "))
    pro.append((name, time))

  n = len(pro)

  # Calculating waiting time for each process
  wait_t = [0] * n
  for i in range(1, n):
    wait_t[i] = pro[i - 1][1] + wait_t[i - 1]

  # Calculating the turnaround time for each process
  turnaround_t = [0] * n
  for i in range(n):
    turnaround_t[i] = pro[i][1] + wait_t[i]

  # Calculating the average waiting time
  total_wait_t = sum(wait_t)
  avg_wait_t = total_wait_t / n

  # Calculating the average turnaround time
  tot_turnaround_t = sum(turnaround_t)
  avg_turnaround_t = tot_turnaround_t / n

  print("Process\tWaiting Time\tTurnaround Time")
  for i in range(n):
    print(f"{pro[i][0]}\t\t{wait_t[i]}\t\t{turnaround_t[i]}")
  print(f"Average waiting time: {avg_wait_t}")
  print(f"Average turnaround time: {avg_turnaround_t}")

FCFS()
