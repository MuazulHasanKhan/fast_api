import cProfile
import os
import time
import datetime
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


app = FastAPI()

PROFILE_DIR = "profiles"

os.makedirs( PROFILE_DIR, exist_ok=True)


@app.middleware("http")
async def createprofile(request: Request, call_next):
    profile = cProfile.Profile()
    profile.enable()

    response = await call_next(request)

    profile.disable()
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    profile_file = os.path.join(PROFILE_DIR, f"profile_{timestamp}.prof")
    profile.dump_stats(profile_file)
    print(f"Profile data saved to {profile_file}")

    return response