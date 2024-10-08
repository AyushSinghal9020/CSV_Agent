from scripts.llm import runner

def classifiying_agent(query ) : 

    prompt = open('assets/prompts/agents/agent_1.txt').read().format(query)

    response = runner.run_groq(prompt)

    return response