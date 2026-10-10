from google.cloud import storage

def copy_blob(
    source_bucket_name,
    blob_name,
    destination_bucket_name,
    destination_blob_name,
):

    storage_client = storage.Client()

    source_bucket = storage_client.bucket(source_bucket_name)

    source_blob = source_bucket.blob(blob_name)

    destination_bucket = storage_client.bucket(destination_bucket_name)

    copied_blob = source_bucket.copy_blob(
        source_blob,
        destination_bucket,
        destination_blob_name,
    )

    print(
        f"Copied '{copied_blob.name}' from "
        f"'{source_bucket_name}' to "
        f"'{destination_bucket_name}'."
    )


if __name__ == "__main__":

    source_bucket = "my_bucketttt-123"

    destination_bucket = "dummy-bwt-123"

    blob_name = "newfile.txt"

    copy_blob(
        source_bucket,
        blob_name,
        destination_bucket,
        blob_name,
    )