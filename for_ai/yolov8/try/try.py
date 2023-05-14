import cv2
from ultralytics import YOLO

# Load a model
model = YOLO('yolov8x-seg.pt')  # load an official model

res = model('D:\Develop\\ai_assets\images\GettyImages-587358024.jpg')
res_plotted = res[0].plot(pil=True)
cv2.imwrite("D:\Develop\\ai_assets\images\\result_GettyImages-587358024.jpg", res_plotted)
