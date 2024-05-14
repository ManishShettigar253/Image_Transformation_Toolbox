import cv2
import os

def create_unique_folder(folder_name):
    suffix = 1
    new_folder_name = folder_name
    while os.path.exists(new_folder_name):
        new_folder_name = f"{folder_name}_{suffix}"
        suffix += 1
    os.makedirs(new_folder_name)
    return new_folder_name

def capture_and_transform():
    # Start video capture
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the captured frame
        cv2.imshow('Capture', frame)

        # Wait for Enter key to be pressed
        key = cv2.waitKey(1)
        if key == 13:  # Enter key
            # Create a folder to store transformed images
            folder_name = "transformed_images"
            if os.path.exists(folder_name):
                folder_name = create_unique_folder(folder_name)
            else:
                os.makedirs(folder_name)

            # Save the original captured image
            cv2.imwrite(os.path.join(folder_name, "original_image.jpg"), frame)

            # Convert the captured image to grayscale
            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(os.path.join(folder_name, "gray_image.jpg"), gray_img)

            # Convert the captured image to HSL
            hsl_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
            cv2.imwrite(os.path.join(folder_name, "hsl_image.jpg"), hsl_img)

            # Convert the captured image to HSV
            hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            cv2.imwrite(os.path.join(folder_name, "hsv_image.jpg"), hsv_img)

            # Convert the captured image to LAB
            lab_img = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
            cv2.imwrite(os.path.join(folder_name, "lab_image.jpg"), lab_img)

            # Convert the captured image to YUV
            yuv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
            cv2.imwrite(os.path.join(folder_name, "yuv_image.jpg"), yuv_img)

            # Add more transformations with different color filters
            # Example:
            for i in range(1, 21):
                transformed_img = cv2.applyColorMap(frame, i)
                cv2.imwrite(os.path.join(folder_name, f"transformed_image_{i}.jpg"), transformed_img)

            print(f"Images saved in folder '{folder_name}'")
            break

    # Release the video capture
    cap.release()
    cv2.destroyAllWindows()

# main module starts ...Call the function to capture and transform the image
capture_and_transform()
