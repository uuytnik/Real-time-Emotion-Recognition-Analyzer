# 检查摄像头是否可用
import cv2

cap = cv2.VideoCapture(0)  # 尝试不同的索引
if not cap.isOpened():
    print("无法访问摄像头")
    # 尝试其他索引
    cap = cv2.VideoCapture(1)
else:
    print("摄像头可以访问")