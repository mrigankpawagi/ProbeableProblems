import os
import pandas as pd
import importlib

for Q in range(1, 6):
    # get all files in the directories code/q{Q}/buggy and code/q{Q}/ok
    submissions = []
    if os.path.exists(f"code/q{Q}/buggy"):
        for f in os.listdir(f"code/q{Q}/buggy"):
            submissions.append({"filename": f, "status": "buggy"})
    if os.path.exists(f"code/q{Q}/ok"):
        for f in os.listdir(f"code/q{Q}/ok"):
            submissions.append({"filename": f, "status": "ok"})
    
    for submission in submissions:
        # get the submission information
        name = submission['filename'].split(".")[0]
        team_id, submission_id = name.split("_")
        
        submission["name"] = name
        submission["team_id"] = team_id
        submission["submission_id"] = submission_id
        
        # copy the contents of the submission to evaluator/submission.py
        with open(f"code/q{Q}/{submission['status']}/{submission['filename']}") as f:
            code = f.read()
        with open("evaluator/submission.py", "w") as f:
            f.write(code)
            
        # run evaluator/p{Q}.py and record the stdout
        pipe = os.popen(f"python evaluator/p{Q}.py").read().strip()
        result = eval(pipe)
        
        submission["result"] = result

    # convert the results to a pandas DataFrame, unrolling the result dictionary
    df = pd.DataFrame(submissions)
    df = pd.concat([df.drop(['result'], axis=1), df['result'].apply(pd.Series)], axis=1)
    
    # unroll all the nested dictionaries, but the new column names are prefixed with the original column name
    for col in df.columns:
        if isinstance(df[col].iloc[0], dict):
            df = pd.concat([df.drop([col], axis=1), df[col].apply(pd.Series).add_prefix(f"{col}_")], axis=1)
    
    # save the DataFrame to a CSV file
    df.to_csv(f"results/q{Q}.csv", index=False)


# delete evaluator/submission.py
os.remove("evaluator/submission.py")
