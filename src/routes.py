from fastapi import FastAPI, Request
from typing import Optional
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .models import ImageRequest, PredictionResponse
from fastapi.logger import logger
from PIL import Image
from io import BytesIO
from fastapi.middleware.cors import CORSMiddleware
import base64
from .ml_models import DigitClassifier

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="template")

@app.get("/", response_class=HTMLResponse)
@app.get("/index", response_class=HTMLResponse, name="index")
def index(request: Request):
    return templates.TemplateResponse("index.html",
                                      {"request": request})
    
@app.post("/predict", name="prediction", response_model=PredictionResponse)
def predict(request: Request, image:ImageRequest):
    im = Image.open(BytesIO(base64.b64decode(image.image_data.split(",")[1]))).convert("L")
    prediction = PredictionResponse.parse_obj(DigitClassifier.predict(im))
    return prediction