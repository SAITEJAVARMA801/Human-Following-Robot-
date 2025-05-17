import cv2
import RPi.GPIO as GPIO
import time


# Define motor driver pins
LEFT_MOTOR_FORWARD = 17
LEFT_MOTOR_BACKWARD = 18
RIGHT_MOTOR_FORWARD = 22
RIGHT_MOTOR_BACKWARD = 23

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEFT_MOTOR_FORWARD, GPIO.OUT)
GPIO.setup(LEFT_MOTOR_BACKWARD, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR_FORWARD, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR_BACKWARD, GPIO.OUT)

# Load Haarcascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize Camera
cap = cv2.VideoCapture(0)

# Get frame dimensions
FRAME_WIDTH = int(cap.get(3))
FRAME_CENTER = FRAME_WIDTH // 2

# Motor control functions
def move_forward():
    GPIO.output(LEFT_MOTOR_FORWARD, True)
    GPIO.output(LEFT_MOTOR_BACKWARD, False)
    GPIO.output(RIGHT_MOTOR_FORWARD, True)
    GPIO.output(RIGHT_MOTOR_BACKWARD, False)

def move_backward():
    GPIO.output(LEFT_MOTOR_FORWARD, False)
    GPIO.output(LEFT_MOTOR_BACKWARD, True)
    GPIO.output(RIGHT_MOTOR_FORWARD, False)
    GPIO.output(RIGHT_MOTOR_BACKWARD, True)

def turn_left():
    GPIO.output(LEFT_MOTOR_FORWARD, False)
    GPIO.output(LEFT_MOTOR_BACKWARD, True)
    GPIO.output(RIGHT_MOTOR_FORWARD, True)
    GPIO.output(RIGHT_MOTOR_BACKWARD, False)

def turn_right():
    GPIO.output(LEFT_MOTOR_FORWARD, True)
    GPIO.output(LEFT_MOTOR_BACKWARD, False)
    GPIO.output(RIGHT_MOTOR_FORWARD, False)
    GPIO.output(RIGHT_MOTOR_BACKWARD, True)

def stop():
    GPIO.output(LEFT_MOTOR_FORWARD, False)
    GPIO.output(LEFT_MOTOR_BACKWARD, False)
    GPIO.output(RIGHT_MOTOR_FORWARD, False)
    GPIO.output(RIGHT_MOTOR_BACKWARD, False)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        if len(faces) > 0:
            x, y, w, h = faces[0]  # Use the first detected face
            face_center = x + w // 2
            
            if face_center < FRAME_CENTER - 50:
                turn_left()
            elif face_center > FRAME_CENTER + 50:
                turn_right()
            else:
                move_forward()
        else:
            stop()
        
        cv2.imshow("Frame", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    pass

finally:
    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
    
