import cv2
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry


sam = sam_model_registry["default"](checkpoint="D:\Develop\\ai_models\sam_vit_h_4b8939.pth")
sam.to(device='cuda')
mask_generator = SamAutomaticMaskGenerator(sam)

image = cv2.imread("D:\Develop\segment-anything\images\GettyImages-587358024.jpg")
masks = mask_generator.generate(image)

print(masks)