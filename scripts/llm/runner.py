from groq import Groq

def run_groq(prompt) : 

    client = Groq(api_key = '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')

    try : 
        chat_completion = client.chat.completions.create(
                messages = [{'role' : 'user' , 'content' : prompt}] , 
                model = 'llama3-70b-8192'
            )
            
        return chat_completion.choices[0].message.content
    except Exception as e : 
        
        print(f"Error occurred: {e}")
            
        return None    