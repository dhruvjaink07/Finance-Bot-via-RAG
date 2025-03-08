from flask import request, jsonify, Blueprint
import os
from langchain_mistralai.chat_models import ChatMistralAI
import chromadb

os.environ["MISTRAL_API_KEY"] = "236mWUjffs24Rg2pkQNfQiJNxg9EUxNO"

client = chromadb.PersistentClient(path='db')
collection = client.get_or_create_collection('collection')

os.environ["MISTRAL_API_KEY"] = "236mWUjffs24Rg2pkQNfQiJNxg9EUxNO"


template = """
You are an experienced financial consultant who helps clients with in their investment and financial planning.
you have to follow the following guidelines:

1. You should provide financial advice to clients based on their financial goals and risk tolerance.
2. You should help clients develop a financial plan that meets their needs and objectives.
3. You should explain complex financial concepts in a clear and understandable way.
4. Short and concise answers are preferred.
5. You should provide a clear explanation of the financial concepts and terms.
6. You should provide examples to illustrate your points.

"""


finance_keywords = [    
    'stock', 'market', 'investment', 'bond', 'interest rate', 
    'economy', 'financial', 'bank', 'currency', 'inflation','Economic growth',
    'Economic development', 'Economic planning', 'Economic policy', 'Economic reform',
    'Economic system', 'Economic model', 'Economic theory', 'Economic indicator',
    'Economic geography', 'Economic history', 'Economic sociology', 'Economic anthropology','banking',
    'financial planning', 'financial advisor', 'financial consultant', 'financial management',
    'financial services', 'financial analyst', 'financial institution', 'financial market',
    'financial economics', 'financial crisis', 'financial risk', 'financial instrument',
    'Equities','mutual funds','commodities','derivatives','forex','cryptocurrency',
    'investment banking', 'investment management', 'investment fund', 'investment trust','debt',
    'interest rate','interest rate risk','interest rate swap','interest rate cap','interest rate floor',
    'credit','credit risk','credit rating','credit default swap','credit spread','credit crunch',
    'tax','salary','details', 'income tax', 'tax rate', 'tax bracket', 'tax deduction', 'tax credit',
    'taxable income', 'tax return', 'tax planning', 'tax evasion', 'tax avoidance', 'tax haven',
    'State','Government','Public finance','stock market','stock exchange','stock price','stock index',
    'ctc','insurance','insurance policy','insurance premium','insurance claim','insurance company',
]
                    
                          

def generate_response(prompt: str, model_name: str = "mistral-small", temperature: float = 0.7) -> str:
    try:
        if not any(keyword in prompt.lower() for keyword in finance_keywords):
            return "Please ask finance-related questions."
        else:
                   
            generator = ChatMistralAI(
            model=model_name, 
            temperature=temperature,
            mistral_api_key=os.getenv("MISTRAL_API_KEY")  
        )

        response = generator.invoke(prompt)
        response_str = str(response)
        return {"message": response_str}

    except Exception as e:
        return f"Error: {e}"

