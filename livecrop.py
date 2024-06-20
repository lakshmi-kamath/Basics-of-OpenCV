import cv2

# Define the coordinates for the region of interest (ROI)
x, y, w, h = 100, 100, 300, 300  # Adjust these values as needed

# Open a connection to the webcam (usually device 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture image")
        break
    
    # Crop the frame to the defined ROI
    cropped_frame = frame[y:y+h, x:x+w]
    
    # Display the original and cropped frames
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Cropped Frame', cropped_frame)
    
    # Exit loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
