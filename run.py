import os
import csv

NUM_QUESTIONS = 5

results = []

for Q in range(1, NUM_QUESTIONS + 1):
    
    for status in ["buggy", "ok"]:
        # check if code/qQ/status exists
        path = f"code/q{Q}/{status}"
        if not os.path.exists(path):
            continue

        # iterate through all the files in code/qQ/status
        for filename in os.listdir(path):
            if filename.endswith(".py"):
                file = os.path.join(path, filename)
                team, attempt = filename.split(".py")[0].split("_")
                
                # copy the file into evaluator/ as "submission.py"
                os.system(f"cp {file} evaluator/submission.py")
                
                # run the evaluator and capture the output from stdout
                output = eval(os.popen(f"python evaluator/p{Q}.py").read().strip())
                
                # write to results
                results.append((Q, team, attempt, output, status))
            
# delete the file from evaluator/
os.system("rm evaluator/submission.py")

# save results to csv
with open("results.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Q", "team", "attempt", "score", "status"])
    writer.writerows(results)
