from google.cloud import storage

def delete_blob(bucket_name, blob_name):

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(blob_name)

    blob.delete()

    print(f"Object '{blob_name}' deleted successfully.")


if __name__ == "__main__":

    bucket_name = "dummy-bwt-123"

    blob_name = "newfile.txt"

    delete_blob(bucket_name, blob_name)