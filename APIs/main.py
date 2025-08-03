import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],   # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],   # Allow all headers
)

@app.get("/")
def home():
    return {"message": "FastAPI running on custom local port with CORS", "name": "quddus", "age": 12, "class": "12th"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)
