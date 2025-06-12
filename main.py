from fastapi import FastAPI, HTTPException

app=FastAPI(title="Auth-Microservice")

#in-memory database
users=[]
seq_id=1

@app.get("/")
def read_root():
    return {"message": "Welcome to the Auth Microservice!"}


@app.post("/register")
def register_user(email: str, password: str):
    global seq_id
    #check if user already exists
    for user in users:
        if user['email']==email:
            raise HTTPException(status_code=400, detail="User already registerd!")

    user = {"id": seq_id, "email": email, "password": password}
    users.append(user)
    seq_id+=1
    return {"message": "User registered successfully", "user": {"id": user["id"], "email": user["email"]}}


@app.post("/login")
def login_user(email:str, password:str):
    for user in users:
        if user["email"]==email and user["password"]==password:
            return {"messsage": "Login successful",
                    "user": {
                        "id": user['id'],
                        "email": user['email']
                    }}
    raise HTTPException(status_code=401, detail="User not found! Please register first.")

@app.get("/health")
def health_check():
    return {"status": "healthy"}