from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()
chave_api = os.getenv("OPENAI_API_KEY")

mensagens = [
    SystemMessage("Traduza o texto a seguir para inglês"),
    HumanMessage("Vamos automatizar tudo")
]

modelo = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()
chain = modelo | parser

# resposta = modelo.invoke(mensagens)
# texto = parser.invoke(resposta)

texto = chain.invoke(mensagens)
print(texto)