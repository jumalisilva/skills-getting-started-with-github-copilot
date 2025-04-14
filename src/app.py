"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Practice basketball and participate in tournaments",
        "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "mia@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore various art techniques and create masterpieces",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["isabella@mergington.edu", "amelia@mergington.edu"]
    },
    "Drama Club": {
        "description": "Learn acting skills and perform in school plays",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["elijah@mergington.edu", "charlotte@mergington.edu"]
    },
    "Math Club": {
        "description": "Solve challenging math problems and prepare for competitions",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 10,
        "participants": ["lucas@mergington.edu", "harper@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["evelyn@mergington.edu", "jackson@mergington.edu"]
    },
    "Tennis Club": {
        "description": "Learn and practice tennis skills with peers",
        "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 10,
        "participants": ["grace@mergington.edu", "henry@mergington.edu"]
    },
    "Swimming Team": {
        "description": "Train and compete in swimming competitions",
        "schedule": "Tuesdays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["ella@mergington.edu", "james@mergington.edu"]
    },
    "Photography Club": {
        "description": "Learn photography techniques and capture stunning images",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["scarlett@mergington.edu", "leo@mergington.edu"]
    },
    "Music Band": {
        "description": "Join the school band and perform in events",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["nora@mergington.edu", "benjamin@mergington.edu"] 
    },
    "Debate Club": {
        "description": "Engage in debates and improve public speaking skills",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["zoe@mergington.edu", "logan@mergington.edu"]
    },
    "Robotics Club": {
        "description": "Build and program robots for competitions",
        "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": ["aaron@mergington.edu", "chloe@mergington.edu"] 
    },
    "Track and Field": {
        "description": "Train for track and field events and compete in meets",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 25,
        "participants": ["ethan@mergington.edu", "sophia@mergington.edu"]
    },
    "Volleyball Team": {
        "description": "Practice volleyball and participate in tournaments",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["lily@mergington.edu", "mason@mergington.edu"]
    },
    "Painting Club": {
        "description": "Learn painting techniques and create beautiful artworks",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["hannah@mergington.edu", "lucas@mergington.edu"]
    },
    "Dance Club": {
        "description": "Learn and practice various dance styles",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["ella@mergington.edu", "jack@mergington.edu"]
    },
    "Astronomy Club": {
        "description": "Explore the universe and learn about celestial objects",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["oliver@mergington.edu", "ava@mergington.edu"]
    },
    "History Club": {
        "description": "Dive into historical events and discuss their impact",
        "schedule": "Mondays, 3:30 PM - 4:30 PM",
        "max_participants": 10,
        "participants": ["amelia@mergington.edu", "liam@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists  
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specificy activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
