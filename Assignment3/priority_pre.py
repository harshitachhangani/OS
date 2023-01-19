from tabulate import tabulate

def preemptive_priority():
    n = int(input("Enter the number of jobs: "))
    jobs = []
    for i in range(n):
        print("Enter details for job ", i+1)
        job_id = int(input("Enter job id: "))
        burst_time = int(input("Enter burst time: "))
        arrival_time = int(input("Enter arrival time: "))
        priority = int(input("Enter priority: "))
        jobs.append((job_id, burst_time, arrival_time, priority))
    jobs.sort(key=lambda x: x[3])  # sort jobs by priority
    completion_time = 0
    waiting_time = 0
    turnaround_time = 0
    data = []
    while len(jobs) > 0:
        i = 0
        while i < len(jobs):
            if jobs[i][2] <= completion_time:
                break
            i += 1
        if i == len(jobs):
            completion_time = jobs[i-1][2]
            break
        jobs[i], jobs[0] = jobs[0], jobs[i]  # bring the next job to be executed to the front of the list
        completion_time += jobs[0][1]
        waiting_time += (completion_time - jobs[0][1] - jobs[0][2])
        turnaround_time += (completion_time - jobs[0][2])
        data.append([jobs[0][0], jobs[0][1], jobs[0][2], jobs[0][3], completion_time, completion_time-jobs[0][1]-jobs[0][2], completion_time-jobs[0][2]])
        jobs.pop(0)
    header = ["Job ID", "Burst Time","Arrival Time","Priority","Completion Time","Waiting Time", "Turnaround Time"]
    print(tabulate(data, headers=header))
    print("Average waiting time: ", waiting_time/n)
    print("Average turnaround time: ", turnaround_time/n)
preemptive_priority()

       
