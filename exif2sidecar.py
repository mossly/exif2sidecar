import os
from PIL import Image
from PIL.ExifTags import TAGS

def parse_exif(filename):
    image = Image.open(filename)
    exif_data = image._getexif()
    exif_tags = {}
    for tag_id, value in exif_data.items():
        tag = TAGS.get(tag_id, tag_id)
        exif_tags[tag] = value
    return exif_tags

def shutter_to_fraction(seconds):
    return f"1/{round(1/seconds)}"

for file in os.listdir():
    if file.endswith((".jpg", ".jpeg", ".png")):
        exif_tags = parse_exif(file)
        with open(f'{file}.txt', 'w') as tag_file:
            tag_file.write(f"Camera:{exif_tags['Make']} {exif_tags['Model']}\n")
            tag_file.write(f"Focal Length:{round(exif_tags['FocalLength'])}mm\n")
            tag_file.write(f"Aperture:f/{exif_tags['FNumber']}\n")
            shutter_speed = shutter_to_fraction(exif_tags['ExposureTime'])
            tag_file.write(f"Shutter Speed:{shutter_speed}s\n")
            tag_file.write(f"ISO:{exif_tags['ISOSpeedRatings']}\n")
            tag_file.write(f"Year:{exif_tags['DateTimeOriginal'][:4]}\n")
            tag_file.write(f"Month:{exif_tags['DateTimeOriginal'][5:7]}\n")
            tag_file.write(f"Day:{exif_tags['DateTimeOriginal'][8:10]}\n")
            tag_file.write(f"Hour:{exif_tags['DateTimeOriginal'][11:13]}\n")
            tag_file.write(f"Minute:{exif_tags['DateTimeOriginal'][14:16]}\n")
            tag_file.write(f"Second:{exif_tags['DateTimeOriginal'][17:19]}\n")
            tag_file.write(f"Date:{exif_tags['DateTimeOriginal'][:4]}-{exif_tags['DateTimeOriginal'][5:7]}-{exif_tags['DateTimeOriginal'][8:10]}T{exif_tags['DateTimeOriginal'][11:13]}-{exif_tags['DateTimeOriginal'][14:16]}-{exif_tags['DateTimeOriginal'][17:19]}\n")
