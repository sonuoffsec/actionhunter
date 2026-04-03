import requests, base64, os
GITHUB_TOKEN=os.getenv("GITHUB_TOKEN")
HEADERS={"Authorization":f"token {GITHUB_TOKEN}"}
def github_get(url):
    r=requests.get(url,headers=HEADERS)
    return r.json() if r.status_code==200 else None
def analyze(content):
    issues=[];score=0
    if "@master" in content or "@main" in content:
        issues.append("Unpinned action");score+=5
    if "secrets." in content:
        issues.append("Secrets used");score+=5
    return issues,score
def scan_org(org):
    results=[]
    repos=github_get(f"https://api.github.com/orgs/{org}/repos") or []
    for repo in repos[:10]:
        owner=repo["owner"]["login"];name=repo["name"]
        wf_url=f"https://api.github.com/repos/{owner}/{name}/contents/.github/workflows"
        workflows=github_get(wf_url) or []
        for wf in workflows:
            file=github_get(wf["url"])
            if not file or "content" not in file: continue
            content=base64.b64decode(file["content"]).decode()
            issues,score=analyze(content)
            if issues:
                results.append({"repo":f"{owner}/{name}","issues":issues,"risk_score":score})
    return results
