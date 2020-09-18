import csv

def save_to_file(jobs):
  file = open("jobs.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "link"])

  for job in jobs:
    writer.writerow(list(job.values()))
    #dictionary는 값만 불러올 수 있음
  
  return
  