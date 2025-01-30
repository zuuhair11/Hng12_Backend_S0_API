from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
import pytz

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {
        'email': 'zouhairsahtout66@gmail.com',
        'current_datetime': datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        'github_url': 'https://github.com/zuuhair11/Hng12_Backend_S0_API'
    }


