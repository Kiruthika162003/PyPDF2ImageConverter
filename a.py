!pip install PyPDF2 pdf2image
images = convert_from_path(pdf_path, dpi=300)
import os
from pdf2image import convert_from_path

def pdf_to_image(pdf_path, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Convert PDF to images
    images = convert_from_path(pdf_path)

    # Save images
    for i, image in enumerate(images):
        image_path = os.path.join(output_dir, f"page_{i + 1}.jpg")
        image.save(image_path, "JPEG")

    print("Conversion completed successfully!")

# Provide the path to your PDF file
pdf_path = "path/to/your/pdf/file.pdf"

# Provide the output directory path where the images will be saved
output_dir = "path/to/output/directory"

# Call the function to convert the PDF to images
pdf_to_image(pdf_path, output_dir)
