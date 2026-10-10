from google.cloud import storage
from pathlib import Path

def upload_blob(bucket_name, source_file_name, destination_blob_name):

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(str(source_file_name))

    print("File uploaded successfully.")
    print("Bucket:", bucket_name)
    print("Object:", destination_blob_name)


if __name__ == "__main__":

    bucket_name = "dummy-bwt-123"

    current_folder = Path(__file__).parent

    source_file_name = current_folder / "newfile.txt"

    destination_blob_name = "newfile.txt"

    upload_blob(bucket_name, source_file_name, destination_blob_name)