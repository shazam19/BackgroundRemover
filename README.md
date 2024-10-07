# Image Background Removal Script

This Python script removes the white background from an image, making it transparent. It utilizes the Python Imaging Library (PIL), specifically the PIL.Image module, to process the image.
### Features

- Converts the input image into an RGBA format to support transparency.
- Removes white or near-white pixels (based on a specified threshold) and replaces them with transparent pixels.
- Saves the processed image as a PNG file with a transparent background.

### Usage

1. Make sure you have the required libraries installed:

```bash
pip install Pillow
```

2. Update the imagePath and outputImgPath variables in the convertImage() function to point to your input and output image paths.

3. Run the script:

```bash
python script_name.py
```

4. The script will process the image, remove the white background, and save the result as a PNG file with a transparent background.

### Example

- Input Image: A signature image with a white background.
- Output Image: The same signature image with the white background replaced by transparency.
