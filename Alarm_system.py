import cv2
import winsound
import threading

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

_, ini = cap.read()


ini = cv2.cvtColor(ini, cv2.COLOR_BGR2GRAY)
ini = cv2.GaussianBlur(ini, (21, 21), 0)


alarm = False
alarm_mode = False
alarm_counter = 0


def beep():
    global alarm
    for _ in range(5):
        if not alarm_mode:
            break
        print("ALaRM")
        winsound.Beep(2500, 1000)
    alarm = False


while True:
    _, frame = cap.read()

    if alarm_mode:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.GaussianBlur(frame, (21, 21), 0)
        diff = cv2.absdiff(frame, ini)
        thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
        ini = frame

        if thresh.sum() > 300:
            alarm_counter += 1
        else:
            if alarm_counter > 0:
                alarm_counter -= 1
        cv2.imshow("cam", thresh)
    else:
        cv2.imshow("cam", frame)

    if alarm_counter > 20:
        if not alarm:
            alarm = True
            threading.Thread(target=beep).start()

    key = cv2.waitKey(30)
    if key == ord("f"):
        alarm_mode = not alarm_mode
        alarm_counter = 0
    if key == ord("q"):
        alarm_mode = False
        break

cap.release()
cv2.destroyAllWindows()
