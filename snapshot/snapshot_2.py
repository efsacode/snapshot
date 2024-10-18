import cv2
video_cap = cv2.VideoCapture("./rocket.mp4")
frames = [100, 150, 300, 350]

if not video_cap.isOpened():
    print("Cannot open camera")
    exit()

for i in frames:
    video_cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, frame = video_cap.read()
    cv2.imwrite(f"./{i}.frame.png", frame)
    print(f"{i}. frame kaydedildi")

video_cap.release()
cv2.destroyAllWindows()