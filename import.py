import requests
import shutil

image_url = "http://basescu.xyz/fileimg.txt"    
response = requests.get(image_url, stream=True)

if response.status_code == 200:
    # Get the content of the response
    image_data = response.content
    
    # Define the local file path where you want to save the image
    local_file_path = "image.jpg"  # You can change the file name and extension
    
    # Save the image to your local directory
    with open(local_file_path, "wb") as image_file:
        image_file.write(image_data)
        
       


image_url = "http://basescu.xyz/filevid.txt"    
response = requests.get(image_url, stream=True)

if response.status_code == 200:
    # Get the content of the response
    vid_data = response.content
    
    # Define the local file path where you want to save the image
    local_file_path = "video.mp4"  # You can change the file name and extension
    
    # Save the image to your local directory
    with open(local_file_path, "wb") as image_file:
        image_file.write(vid_data)
        
        