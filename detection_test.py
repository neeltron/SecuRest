def detect_faces(path):
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()
    exist = 0

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    if faces:
        exist = 1
    else:
        exist = 0
    
    return exist

    


exist = detect_faces("2.jpg")
print(exist)
