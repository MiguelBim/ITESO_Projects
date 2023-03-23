import boto3

s3 = boto3.resource('s3')

# Esta parte del código contiene la información del número y nombre de las imágenes que se cargarán al bucket de S3
images=[('image1.jpg','description1'),
      ('image2.jpg','description2'),
      ('image3.jpg','description3')
      ]

# Esta parte del código es la que tiene la información del bucket de S3 en donde se cargaran las imágenes del bloque anterior
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('my-bucket-for-images-miguel-ojeda','Imagenes cargadas con codigo/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
