import os
import csv

NUM_QUESTIONS = 5

results = []

for Q in range(1, NUM_QUESTIONS + 1):
    
    # check if code/qQ/buggy exists
    buggy_path = f"code/q{Q}/buggy"
    if not os.path.exists(buggy_path):
        print(f"q{Q} buggy not found")
        continue

    # iterate through all the files in code/qQ/buggy
    for filename in os.listdir(buggy_path):
        if filename.endswith(".py"):
            buggy_file = os.path.join(buggy_path, filename)
            team, attempt = filename.split("_")
            
            # copy the file into evaluator/ as "submission.py"
            os.system(f"cp {buggy_file} evaluator/submission.py")
            
            # run the evaluator and capture the output from stdout
            output = os.popen(f"python evaluator/p{Q}.py").read()
            
            # write to results
            results.append((Q, team, attempt, output, "buggy"))
            
# delete the file from evaluator/
os.system("rm evaluator/submission.py")

# save results to csv
with open("results.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Q", "team", "attempt", "score", "status"])
    writer.writerows(results)
