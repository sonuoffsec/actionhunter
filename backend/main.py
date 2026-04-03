from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import requests, os, urllib.parse
from dotenv import load_dotenv
from scanner import scan_org

load_dotenv()
app=FastAPI()
CLIENT_ID=os.getenv("GITHUB_CLIENT_ID")
CLIENT_SECRET=os.getenv("GITHUB_CLIENT_SECRET")
FRONTEND_URL="http://localhost:3000"

@app.get("/")
def home(): return {"msg":"Running"}

@app.get("/auth/login")
def login():
    return RedirectResponse(f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}")

@app.get("/auth/callback")
def callback(code:str):
    token_res=requests.post("https://github.com/login/oauth/access_token",
        headers={"Accept":"application/json"},
        data={"client_id":CLIENT_ID,"client_secret":CLIENT_SECRET,"code":code}).json()
    token=token_res.get("access_token")
    user=requests.get("https://api.github.com/user",
        headers={"Authorization":f"token {token}"}).json()
    params=urllib.parse.urlencode({"user":user.get("login"),"token":token})
    return RedirectResponse(f"{FRONTEND_URL}/dashboard?{params}")

@app.get("/scan")
def scan(org:str): return scan_org(org)
