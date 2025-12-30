from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="LangChain API using Ollama (LLaMA2)"
)

# FREE local LLM (Ollama)
llm = Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} in 100 words"
)

prompt2 = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} for a 5 year old child in 100 words"
)

add_routes(
    app,
    prompt1 | llm,
    path="/essay"
)

add_routes(
    app,
    prompt2 | llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
