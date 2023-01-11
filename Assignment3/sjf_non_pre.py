def non_preemptive_sjf():

    n = int(input("Enter the number of jobs: "))
    jobs = []

    for i in range(n):

        print("Enter details for job ", i+1)
        
        job_id = int(input("Enter job id: "))
        burst_time = int(input("Enter burst time: "))
        arrival_time = int(input("Enter arrival time: "))

        jobs.append((job_id, burst_time, arrival_time))

    jobs.sort(key=lambda x: x[1])  # sort jobs by burst time

    completion_time = 0
    waiting_time = 0
    turnaround_time = 0

    print("Job ID\t\tBurst Time\t\tArrival Time\t\tCompletion Time\t\tWaiting Time\t\tTurnaround Time")

    for i in range(n):
        if completion_time < jobs[i][2]: 
            completion_time = jobs[i][2]

        completion_time += jobs[i][1]
        waiting_time += (completion_time - jobs[i][1] - jobs[i][2])
        turnaround_time += (completion_time - jobs[i][2])

        print(jobs[i][0], "\t\t", jobs[i][1], "\t\t\t", jobs[i][2], "\t\t\t", completion_time, "\t\t\t", completion_time - jobs[i][1] - jobs[i][2], "\t\t\t", completion_time - jobs[i][2])

    print("Average waiting time: ", waiting_time/n)
    print("Average turnaround time: ", turnaround_time/n)

non_preemptive_sjf()
