from scripts.llm import runner

def run_rag(query , vc) : 

    similar_docs = vc.similarity_search(query , k = 5)
    context = '\n'.join([doc.page_content for doc in similar_docs])

    prompt = open('assets/prompts/agents/agent_2.txt').read().format(context , query)

    response = runner.run_groq(prompt)

    return response