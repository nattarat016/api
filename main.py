from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    novelId: str | None
    chapterId: str | None
    content: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","https://writer-assistant-pied.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello Backend!"}

@app.post("/analyze")
def analyze_content(data: AnalyzeRequest):
    return {
        "message": "Analyze successful!",
        "novelId": data.novelId,
        "chapterId": data.chapterId,
        "content": data.content
    }