# Image EXIF Data Extractor

Extract EXIF data from images and output them into individual text files.

## Features

- Parse EXIF data from various image formats (JPG, JPEG, PNG)
- Generate sidecar txt files with EXIF data for each image in the directory
- Perfect for ingesting images into Hydrus Network with EXIF tags

## Requirements

- Python 3.x
- PIL (Python Imaging Library)

## Installation

1. Install the PIL library if you don't have it:

   pip install pillow
   


2. Download the script and place it in the directory containing the images you want to process.

## Usage

- Run the script:

  python exif_data_extractor.py
  


- The script will process all the images in the directory and generate individual text files containing the extracted EXIF data.

## Contributing

Pull requests are welcome. Feel free to open an issue if you find a bug or have suggestions for improvements.

## License

This project is licensed under the MIT License.
