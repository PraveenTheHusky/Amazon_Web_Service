

import logging
Files=[]
def list_bucket_objects(bucket_name):
    

    # Retrieve the list of bucket objects
    s_3 = boto3.client('s3')
    try:
        response = s_3.list_objects_v2(Bucket=s3BucketName)
    except ClientError as e:
        
        logging.error(e)
        return None

    # Only return the contents if we found some keys
    if response['KeyCount'] > 0:
        return response['Contents']

    return None





objects = list_bucket_objects(s3BucketName)
if objects is not None:
        # List the object names
        #logging.info(f'Objects in {bucket_name}')
    for obj in objects:
            Files.append(f'{obj["Key"]}')
else:
        # Didn't get any keys
    logging.info(f'No objects in {s3BucketName}')







