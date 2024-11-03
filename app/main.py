import os
import uuid
import uvicorn
import firebase_admin
import yagmail

from fastapi import FastAPI, HTTPException
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
from google.cloud import firestore
from pydantic import BaseModel
from firebase_admin import credentials
from firebase_admin import firestore

from dotenv import load_dotenv

load_dotenv('dev.env')


SENDER_MAIL= str(os.getenv('SENDER_MAIL'))
SENDER_MAIL_PASS= str(os.getenv('SENDER_MAIL_PASS'))
CRED_CERTIFICATE_PATH= str(os.getenv('CRED_CERTIFICATE_PATH'))

cred = credentials.Certificate('secret.json')

app = firebase_admin.initialize_app(cred)


app = FastAPI()
db = firestore.client()

class User(BaseModel):
    username: str
    email: str
    project_id: str

@app.post("/add_users")
async def add_user(user: User):
    user_id = str(uuid.uuid4())
    user_data = user.dict()
    user_data["user_id"] = user_id
    db.collection("users").document(user_id).set(user_data)
    return {"status": "User created", "user": user_data}

@app.get("/get_users")
async def get_users():
    users = [doc.to_dict() for doc in db.collection("users").stream()]
    return {"users": users}

@app.patch("/update_users/{user_id}")
async def update_user(user_id: str, user: User):
    user_ref = db.collection("users").document(user_id)
    if not user_ref.get().exists:
        raise HTTPException(status_code=404, detail="User not found")
    user_ref.update(user.dict())
    return {"status": "User updated", "user": user.dict()}

@app.delete("/delete_users/{user_id}")
async def delete_user(user_id: str):
    user_ref = db.collection("users").document(user_id)
    if not user_ref.get().exists:
        raise HTTPException(status_code=404, detail="User not found")
    user_ref.delete()
    return {"status": "User deleted"}

body = """
<!DOCTYPE html>
<html>
<head>
</head>
<body style="font-family: Arial, sans-serif; margin: 0; padding: 0;">
  <div style="width: 100%; padding: 20px; background-color: #f4f4f4;">
    <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
      <div style="background-color: #3b82f6; color: #ffffff; padding: 20px; text-align: center; font-size: 24px; font-weight: bold; border-radius: 10px 10px 0 0;">
        API Documentation Invitation
      </div>
      <p>Hello,</p>
      <p>I am excited to invite you all to view our User Management API documentation on ReDoc.</p>
      <p>You can access the API documentation via the following links:</p>
      <ul>
          <li>
              <a href="https://check-app-508284549488.us-central1.run.app/docs" style="display: inline-block; background-color: #3b82f6; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-size: 16px;">View Swagger Documentation</a>
          </li>
          <li>
              <a href="https://check-app-508284549488.us-central1.run.app/redoc" style="display: inline-block; background-color: #3b82f6; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-size: 16px;">View ReDoc Documentation</a>
          </li>
      </ul>
      <p>For more information, check out our GitHub repository:</p>
      <p>
          <a href="" style="display: inline-block; background-color: #28a745; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-size: 16px;">Visit GitHub Repository</a>
      </p>
      <p>Look forward to your feedback.</p>
      <div style="margin-top: 20px; font-size: 14px; color: #666666; text-align: center;">
        Thank you,<br>
        Mohan Raj B<br>
        <i>If you have any questions, feel free to reply to this email.</i>
      </div>
    </div>
  </div>
</body>
</html>
"""



@app.get("/send_invite")
async def send_invite():
    yag = yagmail.SMTP(SENDER_MAIL, SENDER_MAIL_PASS)
    receiver_email = "mohan16457@gmail.com"
    subject = "API Documentation Invitation"
    html_content = body
    yag.send(to=receiver_email, subject=subject, contents=html_content)
    print("Email sent successfully!")
    return {"status": "Invitation mail sent successfully!"}


if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)

