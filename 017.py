from google.cloud import storage
 
# Create a client
storage_client = storage.Client()
 
# List buckets
buckets = list(storage_client.list_buckets())
for bucket in buckets:
    print(f"Bucket Name: {bucket.name}")
