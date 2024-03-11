import cv2

def main():
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = None 
    is_recording = False

    contrast = 1.0
    brightness = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        adjusted_frame = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness)

        if is_recording:
            cv2.circle(adjusted_frame, (50, 50), 15, (0, 0, 255), -1)

        cv2.imshow('Video Recorder', adjusted_frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord(' '):
            if not is_recording:
                is_recording = True
                out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame.shape[1], frame.shape[0]))
            else:
                is_recording = False
                out.release()
                out = None

        elif key == 27:
            if not is_recording:
                break  

        elif key == ord('['):
            contrast -= 0.1
        elif key == ord(']'):
            contrast += 0.1

        elif key == ord(';'):
            brightness += 10
        elif key == ord("'"):
            brightness -= 10

        contrast = max(0.1, min(3.0, contrast))
        brightness = max(-255, min(255, brightness))

        if is_recording:
            out.write(adjusted_frame)

    cap.release()
    if out is not None:
        out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()