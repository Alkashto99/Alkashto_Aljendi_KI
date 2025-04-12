import cv2
import torch
import piq
from halo import Halo  # Importing Halo for loading spinner

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

    # Start a spinner animation while processing the image
    spinner = Halo(text='🔄 Calculating result...', spinner='dots')
    spinner.start()

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

    # Stop the spinner after the calculation is completed
    spinner.succeed("✅ Calculation completed!")

    return brisque_score.item()

if __name__ == "__main__":
    import sys

    # Start a spinner animation to indicate the script is launching
    spinner = Halo(text="🚀 Starting Image Quality Assessment...", spinner="dots")
    spinner.start()

    # Ensure the script is executed with an image path argument
    if len(sys.argv) != 2:
        spinner.fail("❌ Error: Missing image path!")
        print("Usage: python image_quality.py <image_path>")
        sys.exit(1)

    # Stop spinner after validation
    spinner.succeed("✅ Image Quality Assessment started!")

    # Get the image path from command-line arguments
    image_path = sys.argv[1]

    # Run the assessment function
    score = assess_image_quality(image_path)

    # Print results
    print("\n Image Quality Assessment Results:")
    print(f" BRISQUE Score: {score:.2f} (Lower is better)\n")

    # Interpretation guide for BRISQUE scores
    print("===============================")
    print("Interpretation Guide:")
    print("0  - 20 : Excellent quality")
    print("20 - 40 : Good quality")
    print("40 - 60 : Fair quality")
    print("60 - 80 : Poor quality")
    print("80 - 100: Very poor quality")
    print("===============================")

