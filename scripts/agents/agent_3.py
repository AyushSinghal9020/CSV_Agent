from scripts.services import services
from scripts.llm import runner

def simplify_query(query) : 

    prompt = open('assets/prompts/agents/agent_4.txt').read().format(query)

    response = runner.run_groq(prompt)

    return response

def run_csv_agent(query) : 

    simplified_query = simplify_query(query)

    prompt = open('assets/prompts/agents/agent_3.txt').read().format(simplified_query)

    response = runner.run_groq(prompt)
    code = str(services.extract_code(response))

    return code