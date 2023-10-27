from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile
import numpy as np
import cv2
from modules.full_pipeline import FullPipeline

async def file2opencv(file):
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

app = FastAPI()
pipeline = FullPipeline(reconition_device="cpu")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

front =r"samples/front.png"
left =r"samples/inner_left.jpg"
right =r"samples/inner_right.jpg"
back =r"samples/back.png"

@app.post("/")
async def extract_info():
    front_image = cv2.imread(front)
    back_image = cv2.imread(back)
    inner_left_image = cv2.imread(left) 
    inner_right_image = cv2.imread(right)
    data = pipeline(front_image, inner_left_image, inner_right_image, back_image)
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000, host="127.0.0.1", workers=1)
