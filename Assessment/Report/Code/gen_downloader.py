import requests
import time

# Example API query URL
#api_url = 'https://www.xeno-canto.org/api/2/recordings?query=gen:pica%20pica+cnt:United%20Kingdom'

#api_url = 'https://www.xeno-canto.org/api/2/recordings?query=gen:pica%20pica%20cnt:United%20area:europe'

print("Enter UK bird to search for:")
theBird = input()

print("Enter max downloads:")
maxDownloads = int(input())

api_url = 'https://www.xeno-canto.org/api/2/recordings?query='+ theBird +'%20cnt:%22%3DUnited%20Kingdom%22%20grp:%22birds%22'

print(api_url)


# Send request to xeno-canto API
response = requests.get(api_url).json()

# Example delay between downloads (in seconds)
# use to ensure no overloading of server requests
download_delay = 3

count = 0
for recording in response['recordings']:
    if (count > maxDownloads):
        exit()
    
    count += 1
    
    file_url = recording['file']
    #file_name = file_url.split('/')[-1]
    file_name = theBird + str(count) + ".wav"
    

    #use below as a starting point if the first n recordings have already been downloaded
    if (count >= 0):
        # Download the file
        print(f'Downloading {file_name}...')
        with requests.get(file_url, stream=True) as r:
            r.raise_for_status()
            with open(file_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        
        print(f'{file_name} downloaded successfully.')
        time.sleep(download_delay)