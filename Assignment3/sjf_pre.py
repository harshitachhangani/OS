n = int(input("Enter the number of processes: "))

burst_time = []
arrival_time = []
for i in range(n):
    arrival_time.append(int(input("Enter the arrival time of process {}: ".format(i+1))))
    burst_time.append(int(input("Enter the burst time of process {}: ".format(i+1))))

processes = []
for i in range(n):
    processes.append([i+1, arrival_time[i], burst_time[i]])

processes = sorted(processes, key=lambda x: x[1])

total_time = 0
for i in range(n):
    total_time += processes[i][2]

completion_time = [0] * n
remaining_time = [processes[i][2] for i in range(n)]
current_time = 0
queue = []
t = 0

while True:
    for i in range(n):
        if remaining_time[i] > 0 and processes[i][1] <= current_time:
            if i not in queue:
                queue.append(i)

    if not queue:
        t += 1
        current_time += 1
        continue

    next_process = min(queue, key=lambda x: remaining_time[x])
    remaining_time[next_process] -= 1

    if remaining_time[next_process] == 0:
        queue.remove(next_process)
        completion_time[next_process] = current_time + 1

    t += 1
    current_time += 1

    if t == total_time:
        break

turnaround_time = [0] * n
waiting_time = [0] * n
for i in range(n):
    turnaround_time[i] = completion_time[i] - processes[i][1]
    waiting_time[i] = turnaround_time[i] - processes[i][2]

print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
for i in range(n):
    print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(processes[i][0], processes[i][1], processes[i][2], completion_time[i], turnaround_time[i], waiting_time[i]))

average_turnaround_time = sum(turnaround_time) / n
average_waiting_time = sum(waiting_time) / n

print("Average Turnaround Time: {:.2f}".format(average_turnaround_time))
print("Average Waiting Time: {:.2f}".format(average_waiting_time))
