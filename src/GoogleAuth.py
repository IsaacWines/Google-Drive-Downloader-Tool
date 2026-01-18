"""
GoogleAuth.py

Header file for the Google Drive Downloader tool to authenticate user's google account.
"""
import pydrive2
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def main():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)

if __name__ == "__main__":
    main()
        