# CSV Agent 

This project is made in collaboration with @

# What it does 
* Uses LLM to generate scripts for retreival of data from given CSV file based on user query and give answer to User

# How to run 
* Put your csv file in `assets/csvs/your_file.csv`
* Put a VectorDB on Pinecone named `test` with Embeddings `HuggingFaceEmbeddings->all-MiniLM-L6-v2` 
* Run `pip install -r requirements.txt`
* Run `streamlit run app.py`
Your app should be running on port `8501`

# Flow Chart of how it works

[](https://github.com/AyushSinghal9020/CSV_Agent/blob/main/CSV_Agent.jpg)
