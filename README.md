
# Image Rotation and Cropping Script

This Python script processes images by applying random rotations and cropping them to their original dimensions. It's a simple yet effective way to create variations of images or prepare datasets for machine learning applications.

---

## Features
- Rotates images by a random angle between 0° and 360°.
- Crops the rotated images back to their original dimensions.
- Processes all `.png` images in the specified input folder.
- Saves the processed images to an output folder, maintaining the original file names.

---

## Project Structure
```
.venv/
├── script.py
├── Images/
│   ├── Before/
│   │   └── [original images here]
│   ├── After/
│       └── [processed images saved here]
```

---

## Example

### Before Processing
![Polska](https://github.com/user-attachments/assets/d55b0253-6b6a-4603-a4a1-788e8c79c618)

![Niemcy](https://github.com/user-attachments/assets/190e9d76-37fc-4dba-ac90-fe64687d907e)

![Senegal](https://github.com/user-attachments/assets/6a489e06-55d1-4b08-ae49-d0b3d1eda50e)

### After Processing
![Polska](https://github.com/user-attachments/assets/84c3fe55-35f9-4944-a625-079203172a49)

![Niemcy](https://github.com/user-attachments/assets/13f820d8-a908-4890-aa72-a941a25a2446)

![Senegal](https://github.com/user-attachments/assets/79609087-e812-4824-937b-05a4886217f7)

---

## How to Use

### Prerequisites
Make sure you have the following installed:
- Python 3.6 or later
- Required libraries: `Pillow`

To install the required libraries, run:
```bash
pip install -r requirements.txt
```

### Usage
1. Place your images in the `Images/Before/` folder.
2. Run the script:
   ```bash
   python script.py
   ```
3. Processed images will be saved in the `Images/After/` folder.

---

## Configuration
You can modify the folder paths in the script if needed. By default, the script assumes the following folder structure:
- Input images are located in `Images/Before/`.
- Processed images will be saved in `Images/After/`.

---

## Notes
- The script processes all `.png` images in the input folder.
- Ensure that the images are in the correct format to avoid errors.
