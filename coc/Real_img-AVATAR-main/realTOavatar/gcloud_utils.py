import os
import datetime
from google.cloud import storage

# Google Storage Client
client = storage.Client()

def upload_image(bucket_name, source_file_name, destination_blob_name, content_type='', algo_unique_key=''):
    """Upload an image to Google Cloud Storage.

    Args:
        bucket_name (str): Google Storage Bucket Name.
        source_file_name (str): Local absolute file path to upload.
        destination_blob_name (str): File name used to store in the bucket.
        content_type (str, optional): The content type of the file being uploaded.
        algo_unique_key (str, optional): Algorithmia Data Source Bucket Unique Key.
        
    Returns:
        str: Google Storage Object URI.
    """
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name, content_type=content_type)

    data_uri = blob.self_link

    if algo_unique_key != "":
        return os.path.join("gs+{}://{}".format(algo_unique_key, bucket_name), data_uri.split("/")[-1])

    return os.path.join("gs://{}".format(bucket_name), data_uri.split("/")[-1])

def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()
    print("Blob {} deleted.".format(blob_name))

def generate_signed_url(output_uri):
    expiration_time = datetime.timedelta(minutes=5)

    blob = storage.Blob.from_string(output_uri, client=client)
    
    signed_url = blob.generate_signed_url(expiration=expiration_time, version='v4', response_disposition='attachment')

    return signed_url
