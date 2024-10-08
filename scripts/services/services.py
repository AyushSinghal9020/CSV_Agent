import sys
from io import StringIO
import re
import time

def update_history(query , response) : 

    open('assets/chat/history.json' , 'a').write(str(dict(query = query , response = response)) + '\n')

def get_history(n) : 

    '\n'.join(open('assets/chat/history.json').read().split('\n')[-n :])

def extract_code(text) : 

    try : 

        code_pattern = re.compile(r'<<(.*?)>>' , re.DOTALL)
        match = code_pattern.search(text)
        if match : 

            code = match.group(1).strip()

            code.replace('python' , '')
            code.replace('```' , '')

            return code

        return 'No code found.'

    except Exception as e : 
        
        print(f'Error occurred while extracting code: {e}')
        return None

def execute_script_with_retry(script , data , max_retries = 5 , delay = 2) : 

    retry_count = 0

    while retry_count < max_retries : 

        old_stdout = sys.stdout 
        sys.stdout = StringIO()  

        try : 

            exec(script)

            output = sys.stdout.getvalue()
            sys.stdout = old_stdout

            return output

        except Exception as e : 
 
            retry_count += 1
            sys.stdout = old_stdout
             
            if retry_count == max_retries : return f'Execution failed after {max_retries} attempts. Error: {e}' 

            time.sleep(delay)
