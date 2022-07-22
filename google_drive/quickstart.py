from __future__ import print_function

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

def upload_basic():
    creds = google.auth.default()

    try:
        # create gmail api client
        service = build('drive', 'v3', credentials=creds)
        file_metadata = {'name': 'download.jpeg'}
        media = MediaFileUpload('download.jpeg', mimetype='image/jpeg')

        file = service.files().create(body = f)
    except :
        pass
