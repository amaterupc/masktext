import cv2
import numpy as np
from moviepy.editor import VideoFileClip

def remove_text_from_frame(frame):
    # Define the area where the text and phone number are located
    # Adjust these coordinates based on the specific location of the text in the frame
    x_start, y_start, x_end, y_end = 1000, 700, 1280, 720  # Example values, adjust them
    roi = frame[y_start:y_end, x_start:x_end]

    # Create a mask of the same size as the ROI, initialized to all zeros
    mask = np.zeros(roi.shape[:2], dtype=np.uint8)

    # Define the condition to detect the text region (you may need to fine-tune this)
    mask[np.sum(roi, axis=2) < 255 * 3] = 255  # Assuming text is darker than the background
    
    # Ensure roi is a proper BGR image and mask is a grayscale image
    if len(roi.shape) == 3 and roi.shape[2] == 3 and mask.ndim == 2:
        inpainted_roi = cv2.inpaint(roi, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
        # Replace the original area with the inpainted area
        frame[y_start:y_end, x_start:x_end] = inpainted_roi

    return frame

def process_video(input_path, output_path):
    clip = VideoFileClip(input_path)
    
    # Apply the remove_text_from_frame function to each frame
    processed_clip = clip.fl_image(remove_text_from_frame)
    
    # Write the processed video to a file
    processed_clip.write_videofile(output_path, codec='libx264')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python remove_text_from_video.py <input_video_path> <output_video_path>")
        sys.exit(1)

    input_video_path = sys.argv[1]
    output_video_path = sys.argv[2]

    process_video(input_video_path, output_video_path)

