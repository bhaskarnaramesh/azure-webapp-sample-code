"""
Routes and views for the flask application.
"""

from FlaskWebProject1 import app
from azure.storage.blob import BlobService
from flask import redirect

def azureStorageList():
    urlPath = None
    block_blob_service = BlobService(account_name='azurestoragepractice',
                                     account_key='nAL6kanC+Y71Jfe1PRP8Z5V/8nrd/YVbGTd2gpF8tKZ45gndqI94WqUdZajdoFzO0geKWKA8OqAeA18mDt2Zcw==')

    generator = block_blob_service.list_blobs('azure-practice')
    for blob in generator:
        urlPath = block_blob_service.make_blob_url('azure-practice', blob.name)

    return urlPath

@app.route('/')
def home():
    """Renders the home page."""
    return redirect(azureStorageList())