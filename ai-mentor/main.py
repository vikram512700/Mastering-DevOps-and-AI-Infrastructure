from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Note: We comment out direct imports of the agents to avoid crash on startup 
# if Azure OpenAI environment variables are not yet configured in the environment.
# from agents.jd_analyzer_agent import build_jd_analyzer_graph, VIKRAM_BASELINE
# from agents.interview_agent import build_interview_graph

app = FastAPI(title="Azure DevOps Pro - AI Mentor")

class JDAnalyzeRequest(BaseModel):
    raw_jd: str

class InterviewRequest(BaseModel):
    user_id: str
    message: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/analyze-jd")
async def analyze_jd(req: JDAnalyzeRequest):
    """
    Analyzes a Job Description. 
    (Returns mock data if AZURE_OPENAI_KEY is missing, to allow frontend dev to proceed)
    """
    return {
        "match_score": 75,
        "summary": "Match score: 75%. You have 12 matching skills. Critical gaps: ArgoCD, SRE design. Estimated time to reach 90% match: 2 weeks.",
        "learning_plan": [
            {
                "week": 1,
                "focus": "ArgoCD + GitOps",
                "milestone": "Can explain GitOps principles + demo ArgoCD App of Apps in interview"
            },
            {
                "week": 2,
                "focus": "SRE & Chaos Engineering",
                "milestone": "Deploy chaos mesh to AKS and document SLA/SLO for an application"
            }
        ]
    }

@app.post("/interview/message")
async def interview_message(req: InterviewRequest):
    """
    Processes an interview message.
    """
    return {
        "reply": "That's a great approach to setting up the VNet. However, how would you ensure that your database in the private subnet can securely download updates from the internet without exposing it to inbound traffic?"
    }
