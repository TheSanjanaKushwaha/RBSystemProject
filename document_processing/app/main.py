from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the document processing system!"}
    print("Main.py loaded successfully")
