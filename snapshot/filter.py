import cv2 as cv

counter = 0
video_cap = cv.VideoCapture("./rocket.mp4")
frames = [100, 150, 300, 350] #belirledigimiz frameler

if not video_cap.isOpened():
    print("Video acilamadi") #video acilmazsa
    exit()
while True:
    ret, frame = video_cap.read() #videoyu okuduk
    if not ret: #video bitince
        break
    
    counter += 1 #frame lerde kacinci oldugunu bulmasi icin
    
    if(counter in frames): #belirledigimiz framelerdeki resimleri almasi icin
        cv.imwrite("./" + str(counter) + ".frame.png", frame) #resimleri kaydetme

    gray_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    if (counter in frames):
        cv.imwrite("./" + str(counter) + ".grayframe.png", gray_image)
    
    gauss_filtered =cv.GaussianBlur(gray_image,(55,55),0)
    
    if (counter in frames):
        cv.imwrite("./" + str(counter) + ".gauss.png", gauss_filtered)

    """rgb_image = cv.cvtColor(gauss_filtered, cv.COLOR_GRAY2RGB)

    if(counter in frames):
        cv.imwrite("./" + str(counter) + ".rgb.png", rgb_image)"""
    
video_cap.release()
cv.destroyAllWindows()