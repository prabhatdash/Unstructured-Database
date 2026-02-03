import exifread
import json
data={}
with open('Unstructured-Database/image_metadata_extraction/img.jpeg', 'rb') as image_file:
    tags = exifread.process_file(image_file)
    for keys,value in tags.items():
        data[keys] = str(value)
print(json.dumps(data, indent=4))