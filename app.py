# Cloud-Resume-Uploader - Day 1 Project
# Is project ko kal hum AWS S3 se connect karenge

import os
from datetime import datetime

def main():
    print("--- Cloud Uploader Started ---")
    
    # Yahan tumhare certificates / resume ka folder check hoga
    folder = "./my_files"
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Folder ban gaya: {folder} - isme apne certificates daalo")

    print(f"Project Time: {datetime.now()}")
    print("Status: Ready to upload to GitHub & AWS")
    print("Next Step: git push")

if __name__ == "__main__":
    main()
