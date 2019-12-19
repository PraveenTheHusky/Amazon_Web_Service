import boto3 
import io
from trp import Document

bucketname='extracttext'
filename='Cropped_type-1/iCard_021873_1_Daba_Ayehush_H.jpg'

s3BucketName = "extracttext"
    # Amazon Textract client
textract = boto3.client('textract')
response = textract.analyze_document(
        Document={
        'S3Object': {
            'Bucket': bucketname,
            'Name': filename
            }
    },
    FeatureTypes=["FORMS"])

doc = Document(response)
for page in doc.pages:
    for field in page.form.fields:
        print("Key: {}, Value: {}".format(field.key, field.value))
    print("\nGet Field by Key:")
    key='AGE'
    field = page.form.getFieldByKey(key)
    print(field)
    if(field==key):  
        print("Key: {}, Value: {}".format(field.key, field.value))
