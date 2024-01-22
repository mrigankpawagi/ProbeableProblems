import os
import csv
from collections import defaultdict
import importlib

NUM_QUESTIONS = 5

results = []

with open("code/cleaned.csv") as f:
    data = list(csv.reader(f))[1:]
    tests_data = defaultdict(dict)
    
    for team in data:
        team_number = team[0]
        tests = team[2:7]

        question_index = 1
        for test in tests:
            doctests = []
            lines = test.split("\n")
            
            start_flag = False
            for line in lines:
                if line.startswith(">>>"):
                    if start_flag:
                        doctests.append((temp_args, None))
                    
                    start_flag = True
                    i, j = line.find("("), line.rfind(")")
                    temp_args = eval(line[i:j+1])
                    if not isinstance(temp_args, tuple):
                        temp_args = (temp_args,)
                else:
                    if start_flag:
                        s = line.strip()
                        
                        ### Some special cases
                        # inf
                        if 'inf' in s and not ('float("inf")' in s or "float('inf')" in s):
                            s = s.replace("inf", "float('inf')")
                        # nan
                        if 'nan' in s and not ('float("nan")' in s or "float('nan')" in s):
                            s = s.replace("nan", "float('nan')")
                        ### End of special cases
                        
                        res = eval(s)
                        doctests.append((temp_args, res))
                        start_flag = False
            if start_flag:
                doctests.append((temp_args, None))

            tests_data[team_number][question_index] = doctests
            
            question_index += 1

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
                s = os.popen(f"python evaluator/p{Q}.py").read().strip()
                output = eval(s)
                
                # import "eval" from doctests_evaluator/p{Q}.py
                doctest_eval_func = importlib.import_module(f"doctests_evaluator.p{Q}").eval
                
                aic_doctests = []
                for doctest, given in tests_data[team][Q]:
                    try:
                        if doctest_eval_func(doctest, given) != set():
                            aic_doctests.append(doctest)
                    except:
                        pass
                
                missed_from_self_doctests = []
                for doctest in aic_doctests:
                    # print(f"python evaluator/p{Q}.py \"{doctest}\"")
                    output_doct = os.popen(f"python evaluator/p{Q}.py \"{doctest}\"").read().strip()
                    if output_doct != "":
                        missed_from_self_doctests.extend(eval(output_doct))
                
                # write to results
                results.append((Q, team, attempt, output, status, missed_from_self_doctests))
            
# delete the file from evaluator/
os.system("rm evaluator/submission.py")

# save results to csv
with open("results.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Q", "team", "attempt", "score", "status", "missed_from_self_doctests"])
    writer.writerows(results)
