import os
import csv
import importlib

# NUM_QUESTIONS = 5

results = []

with open("code/cleaned.csv") as f:
    data = list(csv.reader(f))[1:]

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
        
        # import "test" from doctests_evaluator/p{question_index}.py
        test_func = importlib.import_module(f"doctests_evaluator.p{question_index}").test

        results.append((question_index, team_number, test_func(doctests)))

        question_index += 1

# save results to csv
with open("results_doct.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Q", "team", "score"])
    writer.writerows(results)
