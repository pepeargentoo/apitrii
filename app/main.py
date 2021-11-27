from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"Trii": "Test ci/cd Triii"}


@app.get("/Dani")
def getdani():
    return {"Trii": "Pepe pepe"}


@app.get("/felipe")
def getfelipe():
    return {"Trii": "open"}
