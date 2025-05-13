import os


class S3Sync:
    # Uploads a local folder to the specified AWS S3 bucket
    def sync_folder_to_s3(self, folder, aws_bucket_url):
        command = f"aws s3 sync {folder} {aws_bucket_url} "
        os.system(command)  # Execute the sync command to upload files

    # Downloads a folder from the specified AWS S3 bucket to local
    def sync_folder_from_s3(self, folder, aws_bucket_url):
        command = f"aws s3 sync {aws_bucket_url} {folder} "
        os.system(command)  # Execute the sync command to download files
