import cv2
import torch
import piq
import threading
import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk

def assess_image_quality(image_path: str):
    """
    Assess image quality using the BRISQUE metric.

    BRISQUE (Blind/Referenceless Image Spatial Quality Evaluator) is a no-reference
    image quality assessment metric. Lower scores indicate better quality.

    Parameters:
        image_path (str): Path to the image file.

    Returns:
        float: BRISQUE score (lower is better).
    """

    # Read the image using OpenCV (default format is BGR)
    img = cv2.imread(image_path)

    # Convert from BGR to RGB since OpenCV loads images in BGR format
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Convert the image into a PyTorch tensor and normalize pixel values to [0,1]
    # - .permute(2, 0, 1) → Changes shape from [H, W, C] to [C, H, W]
    # - .unsqueeze(0) → Adds a batch dimension, making it [1, C, H, W]
    img_tensor = torch.tensor(img).permute(2, 0, 1).unsqueeze(0).float() / 255.0

    # Compute the BRISQUE score
    # - data_range=1.0 ensures that the function correctly handles normalized images
    brisque_score = piq.brisque(img_tensor, data_range=1.0)

    return brisque_score.item()


def select_image():
    """
    Open a file dialog to select an image and start the quality assessment process.
    """

    # Open file dialog and get image path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    # If no file is selected, return
    if not file_path:
        return

    # Update result label while processing
    result_label.config(text="🔄 Calculating...")

    # Start processing in a separate thread to avoid GUI freezing
    threading.Thread(target=calculate_quality, args=(file_path,), daemon=True).start()

    # Load and display the selected image
    img = Image.open(file_path)
    img.thumbnail((250, 250))  # Resize image for display
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img  # Keep reference to avoid garbage collection


def calculate_quality(image_path):
    """
    Calculate the BRISQUE score and update the result label with the score and interpretation guide.

    Parameters:
        image_path (str): Path to the selected image.
    """

    # Compute the BRISQUE score
    score = assess_image_quality(image_path)

    # Format result output
    result_text = f"BRISQUE Score: {score:.2f} (Lower is better)\n\n"
    result_text += "Score Interpretation:\n"
    result_text += "============================\n"
    result_text += "0  - 20  : Excellent quality\n"
    result_text += "20 - 40  : Good quality\n"
    result_text += "40 - 60  : Fair quality\n"
    result_text += "60 - 80  : Poor quality\n"
    result_text += "80 - 100 : Very poor quality\n"
    result_text += "============================\n"

    # Update the GUI with the result
    result_label.config(text=result_text)


# GUI Setup
root = tk.Tk()
root.title("Image Quality Assessment")
root.geometry("600x600")

# Title Label
Label(root, text="Upload an Image to Assess Quality", font=("Arial", 12)).pack(pady=10)

# Select Image Button
Button(root, text="📂 Select Image", command=select_image).pack(pady=10)

# Image Display Label
image_label = Label(root)
image_label.pack()

# Result Display Label
result_label = Label(root, text="", font=("Arial", 12), wraplength=350)
result_label.pack(pady=10)

# Start GUI Main Loop
root.mainloop()
