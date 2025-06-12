from fastapi import FastAPI

app=FastAPI(title="Auth-Microservice")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Auth Microservice!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}