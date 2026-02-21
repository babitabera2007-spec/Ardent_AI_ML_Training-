import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)  # FIX 1: CAP_DSHOW fixes webcam on Windows

if not cap.isOpened():
    print("Error: cannot access webcam")
    exit()

print("Press 'q' to quit")
print("Press 's' to save images")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break   # FIX 2: break is now the LAST thing in the if block
                # everything below is OUTSIDE the if block (correct indentation)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # FIX 3: moved outside if not ret

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

    cv2.putText(
        frame,
        f"Faces Detected: {len(faces)}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Faces Detected", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        filename = f"face_{len(faces)}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")

# FIX 4: cap.release() and destroyAllWindows() are now OUTSIDE the while loop
cap.release()
cv2.destroyAllWindows()