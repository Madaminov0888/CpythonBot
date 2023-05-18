import subprocess
from random import randint


def check_1(user_solution):
    test_cases = [
        (lambda r1, r2: [r1, r2, str(r1+r2)])(randint(1,10**5), randint(10**5, 10**9))  for i in range(1, 5)
    ]
    for test_case in test_cases:
        a, b, answer  = test_case
        try:
            # Create a new process to run the user's solution code
            process = subprocess.Popen(["python3", "-c", user_solution], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # Send the test case input to the process
            out, err = process.communicate(input=f"{a}\n{b}\n")
            # Check if the output is correct
            output = out.strip()
            if str(output) == str(answer):
                pass
            else:
                return False
            # Check if there was any error
            if err:
                return False
        except Exception as e:
            return False
    return True




def return_problem():
    promlem_dict = {
        1: check_1,
        
    }
    
    return promlem_dict
