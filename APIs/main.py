# Import required modules
import uvicorn  # ASGI server to run FastAPI app
from fastapi import FastAPI  # FastAPI framework
from fastapi.middleware.cors import CORSMiddleware  # Middleware for handling CORS

# Create a FastAPI app instance
app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Allow requests from any origin (use specific domains in production)
    allow_credentials=True,     # Allow cookies and authentication headers
    allow_methods=["*"],        # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],        # Allow all headers in requests
)

# Define a route for GET request to the root URL ("/")
@app.get("/")
def home():
    # Return a JSON response with some dummy data
    return {
        "message": "FastAPI running on custom local port with CORS",
        "name": "quddus",
        "age": 12,
        "class": "12th"
    }

# Run the app only if this script is executed directly
if __name__ == "__main__":
    # Start the server using uvicorn on localhost at port 3000 with auto-reload enabled
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)
