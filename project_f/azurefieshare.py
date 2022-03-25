from azure.storage.fileshare import ShareServiceClient, ShareClient,ShareFileClient
import os
from pathlib import Path
import shutil
os.environ['AZURE_STORAGE_CONNECTION_STRING'] = "DefaultEndpointsProtocol=https;AccountName=uploadable;AccountKey=a9hpbeMTgoKu7a3mxd5eF2DnJTyYS/mfaXr5bNPOVvu21UVGwQxcMcF1Fc7KM7tdTEBzq7ECk4YLiosn2Ux6zg==;EndpointSuffix=core.windows.net"
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
def addfile(fileshare_name,dir_name,filepath,filename,f):

    service_client = ShareServiceClient.from_connection_string(connect_str)
    share = ShareClient.from_connection_string(connect_str, share_name=fileshare_name)
    try:

        share.get_share_properties()

        dir_client = share.get_directory_client(dir_name)
    except:

        share.create_share(access_tier='HOT')
        share.set_share_quota(quota=1)

        dir_client = share.create_directory(dir_name)

    # with open (f'{filepath}/{filename}','rb') as f:
    dir_client.upload_file(file_name=filename, data=f)
    print(f'done uploading {filename}...')

def downloadfile(fileshare_name,dir_name,dest_path):
    service_client = ShareServiceClient.from_connection_string(connect_str)
    share = ShareClient.from_connection_string(connect_str, share_name=fileshare_name)
    try:

        my_files = list(share.list_directories_and_files(directory_name=dir_name))
        new_dict = {item['name']: item for item in my_files}
        for i in (new_dict.keys()):
            print(i)
            my_file = share.get_file_client(f"{dir_name}/{i}")

            try:

                with open(f'{dest_path}/{i}', "wb") as data:
                    
                    stream = my_file.download_file()
                    data.write(stream.readall())
            except OSError as e:
                print(e)
    except:pass


def copyfile(account_name,fileshare_name,dest_dir_name,src_dir_name):
    service_client = ShareServiceClient.from_connection_string(connect_str)
    share = ShareClient.from_connection_string(connect_str, share_name=fileshare_name)
    try:
        share.get_directory_client(dest_dir_name)
    except:
        print('creating dir....')
        share.create_directory(dest_dir_name)
    my_files = list(share.list_directories_and_files(directory_name=src_dir_name))
    new_dict = {item['name']: item for item in my_files}
    for i in (new_dict.keys()):
        destination_file = share.get_file_client(f"{dest_dir_name}/{i}")
        source_url = "https://{}.file.core.windows.net/{}/{}".format(account_name,fileshare_name,f"{src_dir_name}/{i}")
        destination_file.start_copy_from_url(source_url=source_url)
        print(f'done copying {i}......')



def deletefile(fileshare_name,dir_name):
    service_client = ShareServiceClient.from_connection_string(connect_str)
    share = ShareClient.from_connection_string(connect_str, share_name=fileshare_name)
    try:
        my_files = list(share.list_directories_and_files(directory_name=dir_name))
        new_dict = {item['name']: item for item in my_files}
        for i in (new_dict.keys()):
            my_file = share.get_file_client(f"{dir_name}/{i}")
            my_file.delete_file()
            print(f"deleted {i}..")
    except:pass



# deletefile('fileshare11','dst1')
#copyfile('uploadable','fileshare11','dst1','dir5432')

# downloadfile('fileshare11','dir5432',r'C:\Users\ACER\PycharmProject\handwriiten')
# addfile('fileshare11','dir5432',r'C:\Users\ACER\PycharmProject\handwriiten','rotated.jpg')
# downloadfile('fileshare11','pin','s1')


# # # downloadfile('fileshare11','pin',r'poject3/p1')


