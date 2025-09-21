import cv2
import imutils
import numpy as np
import time

# Camera setup (USB or DroidCam)
def get_camera_index(max_tested=5):
    for i in range(max_tested):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            cap.release()
            return i
        cap.release()
    return None
# Put your IP here if yor are using DriodCam
# Example : 192.168.1.101
IP, PORT = "Your IP", "4747"
urls = [f"http://{IP}:{PORT}/video", f"http://{IP}:{PORT}/mjpegfeed"]

cap = None
for url in urls:
    cap = cv2.VideoCapture(url)
    if cap.isOpened():
        break

if cap is None or not cap.isOpened():
    idx = get_camera_index(1)
    cap = cv2.VideoCapture(idx) if idx is not None else None

if cap is None or not cap.isOpened():
    raise RuntimeError("Could not access webcam/DroidCam")

print("✅ Camera ready")

# Game variables
score, max_score = 0, 5
list_capacity, max_lc = 0, 20
l, flag = [], 0
apple_x, apple_y, prev_c, center = None, None, None, None

def dist(pt1, pt2):
    if pt1 is None or pt2 is None:
        return 0
    return np.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img = imutils.resize(frame.copy(), width=600)
    img = cv2.GaussianBlur(img, (11, 11), 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Place apple
    if apple_x is None and apple_y is None:
        co_ord = frame.shape[0] - 30
        apple_x = np.random.randint(30, co_ord)
        apple_y = np.random.randint(100, 350)

    cv2.circle(frame, (apple_x, apple_y), 3, (0, 0, 255), -1)

    # Detect green object
    mask = cv2.inRange(img, (29, 86, 18), (93, 255, 255))
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    if len(cnts) > 0:
        ball_cont = max(cnts, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(ball_cont)
        M = cv2.moments(ball_cont)
        center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])) if M['m00'] != 0 else None

        if radius > 10 and center is not None:
            cv2.circle(frame, center, 2, (0, 0, 255), 3)
            if len(l) > list_capacity:
                l = l[1:]
            if prev_c and dist(prev_c, center) > 3.5:
                l.append(center)
            if dist((apple_x, apple_y), center) < 5:
                score += 1
                if score == max_score: flag = 1
                list_capacity += 1
                apple_x, apple_y = None, None
    else:
        cv2.putText(frame, 'Show a Green Object', (150, 250),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

    # Snake body
    for i in range(1, len(l)):
        if l[i - 1] and l[i]:
            cv2.line(frame, l[i], l[i - 1], tuple(np.random.randint(0, 255, 3).tolist()),
                     thickness=int(len(l) / max_lc + 2) + 2)

    cv2.putText(frame, f'Score: {score}', (450, 100),
                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

    # Game over
    if flag == 1:
        cv2.putText(frame, 'Game Over !!', (100, 250), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 0), 3)
        cv2.putText(frame, "'ENTER' to Play", (150, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame, "'Q' or 'ESC' to Exit", (150, 350), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('live feed', frame)
        k = cv2.waitKey(0)
        if k == 13:
            score, flag, list_capacity, l = 0, 0, 0, []
            apple_x, apple_y, center = None, None, None
        else:
            break

    cv2.imshow('live feed', frame)
    prev_c = center

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()
