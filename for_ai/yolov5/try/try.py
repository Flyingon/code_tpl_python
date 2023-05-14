import torch

# Model
model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # or yolov5n - yolov5x6, custom

# Images
img = "D:\Develop\segment-anything\images\GettyImages-587358024.jpg"  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
print(results)
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.

