from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"Trii": "Test ci/cd Trii"}


@app.get("/Dani")
def getdani():
    return {"Trii": "Pepe pepe"}
