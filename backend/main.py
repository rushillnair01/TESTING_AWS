import fastapi
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from simple_backend import response_for_user

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/greet/{user_input}")
def greet_user(user_input: str):
    return {
        "response": response_for_user(user_input)
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )