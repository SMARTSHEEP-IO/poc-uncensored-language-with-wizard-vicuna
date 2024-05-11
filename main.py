from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate
from functools import lru_cache


class QuestionRequest(BaseModel):
    question: str


app = FastAPI()

template = """Answer the following question clearly and concisely:
Question: {question}
Answer:"""

prompt = PromptTemplate.from_template(template)

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

llm = LlamaCpp(
    model_path="./models/Wizard-Vicuna-30B-Uncensored-GGUF/Wizard-Vicuna-30B-Uncensored.Q5_K_M.gguf",
    temperature=0.75,
    max_tokens=2000,
    top_k=40,
    top_p=0.95,
    # device='cuda',  # Add this to target GPU
    n_threads=8,
    repeat_penalty=1.1,
    callback_manager=callback_manager,
    verbose=True,
)


@lru_cache(maxsize=250)
def get_cached_response(question: str):
    return llm.invoke(question)


@app.post("/ask", response_model=dict)
def ask_question(request: QuestionRequest):
    try:
        response_text = get_cached_response(request.question)
        return {"answer": response_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
def read_root():
    return {"Hello": "I'm ready to answer questions!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
