from scripts.services import services
from scripts.llm import runner

def beautify_response(query , rag_response , csv_response) : 

    history = services.get_history(n = 10)

    prompt = open('assets/prompts/agents/agent_5.txt').read().format(
        query , rag_response , csv_response , history
    )

    response = runner.run_groq(prompt)

    services.update_history(query , response)

    return response