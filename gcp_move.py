from google.cloud import storage

def move_blob(
    source_bucket_name,
    destination_bucket_name,
    blob_name,
):

    storage_client = storage.Client()

    source_bucket = storage_client.bucket(source_bucket_name)

    source_blob = source_bucket.blob(blob_name)

    destination_bucket = storage_client.bucket(destination_bucket_name)

    source_bucket.copy_blob(
        source_blob,
        destination_bucket,
        blob_name,
    )

    source_blob.delete()

    print(f"'{blob_name}' moved successfully.")


if __name__ == "__main__":

    source_bucket = "dummy-bwt-123"

    destination_bucket = "my_bucketttt-123"

    blob_name = "newfile.txt"

    move_blob(
        source_bucket,
        destination_bucket,
        blob_name,
    )