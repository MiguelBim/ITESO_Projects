import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image1.jpg','description1'),
      ('image2.jpg','description2'),
      ('image3.jpg','description3')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('my-bucket-for-images-miguel-ojeda','Imagenes cargadas con codigo/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
