from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from dotenv import load_dotenv
from email_utils import send_email
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailSchema(BaseModel):
    address: str
    name: str
    message: str

@app.post("/send-email")
def send_email_endpoint(email: EmailSchema, background_tasks: BackgroundTasks):
    background_tasks.add_task(
        send_email, email.address, email.name, email.message
    )
    return {"status": "Wiadomość w trakcie wysyłania!"}
