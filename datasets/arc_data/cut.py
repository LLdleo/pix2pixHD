import cv2
import os

list_dir = ['train_A', 'train_B']
for fold in list_dir:
    for file in os.listdir(fold):
        img = cv2.imread(os.path.join(fold, file))
        print(img.shape)
        cropped = img[24:1080, 0:1920]  # 裁剪坐标为[y0:y1, x0:x1]
        cv2.imwrite(os.path.join(fold, file), cropped)
