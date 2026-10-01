import os
from PIL import Image
import img2pdf

def build_kdp_coloring_book(image_folder, output_pdf, dpi=300, bleed=True):
    """
    Combines coloring book images into an Amazon KDP compliant PDF.
    - Standard Size: 8.5 x 11 inches
    - Bleed Size: 8.625 x 11.25 inches
    """
    # KDP Dimensions in Inches
    width_in = 8.625 if bleed else 8.5
    height_in = 11.25 if bleed else 11.0
    
    # Target size in pixels at 300 DPI
    target_width = int(width_in * dpi)
    target_height = int(height_in * dpi)
    
    supported_extensions = ('.png', '.jpg', '.jpeg', '.tiff')
    images = sorted([
        f for f in os.listdir(image_folder) 
        if f.lower().endswith(supported_extensions)
    ])
    
    if not images:
        print(f"❌ No images found in directory: {image_folder}")
        return

    processed_images = []
    
    for img_name in images:
        img_path = os.path.join(image_folder, img_name)
        with Image.open(img_path) as img:
            # Convert to Grayscale / Line Art mode
            img = img.convert('L')
            
            # Resize image maintaining aspect ratio and fit into target dimensions
            img.thumbnail((target_width, target_height), Image.Resampling.LANCZOS)
            
            # Create a blank white canvas of exact target size
            canvas = Image.new('L', (target_width, target_height), 255)
            
            # Center the image on canvas
            offset = ((target_width - img.width) // 2, (target_height - img.height) // 2)
            canvas.paste(img, offset)
            
            # Save temporary file with 300 DPI info
            temp_path = os.path.join(image_folder, f"temp_{img_name}")
            canvas.save(temp_path, dpi=(dpi, dpi))
            processed_images.append(temp_path)
            
    # Convert processed images directly to PDF using img2pdf
    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(processed_images))
        
    # Cleanup temporary processed images
    for temp_file in processed_images:
        os.remove(temp_file)
        
    print(f"✅ KDP PDF generated successfully: {output_pdf}")

if __name__ == "__main__":
    # Specify your images folder and output file
    build_kdp_coloring_book("raw_images", "Tiko_Coloring_Book_Interior.pdf")
