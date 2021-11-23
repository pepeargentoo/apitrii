from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Trii": "Test ci/cd Trii"}
