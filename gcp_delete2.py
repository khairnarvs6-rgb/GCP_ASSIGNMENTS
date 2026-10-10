from google.cloud import storage

def delete_bucket(bucket_name):
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    bucket.delete()

    print(f"Bucket '{bucket_name}' deleted successfully.")

if __name__ == "__main__":
    bucket_name = "dummy-bwt-123"

    delete_bucket(bucket_name)