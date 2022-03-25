from azure.storage.blob import BlobServiceClient
import os
import requests
from PIL import Image
# os.environ['AZURE_STORAGE_CONNECTION_STRING'] = "DefaultEndpointsProtocol=https;AccountName=uploadable;AccountKey=a9hpbeMTgoKu7a3mxd5eF2DnJTyYS/mfaXr5bNPOVvu21UVGwQxcMcF1Fc7KM7tdTEBzq7ECk4YLiosn2Ux6zg==;EndpointSuffix=core.windows.net"
# connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING') # retrieve the connection string from the environment variable
# # container_name = "vitwouatcontainer" # container name in which images will be store in the storage account
# blob_service_client = BlobServiceClient.from_connection_string(conn_str=connect_str) # create a blob service client to interact with the storage account

def addtoblob(container_name,filename,file,cnstr):
    os.environ['AZURE_STORAGE_CONNECTION_STRING'] =cnstr
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING') # retrieve the connection string from the environment variable
    # container_name = "vitwouatcontainer" # container name in which images will be store in the storage account
    blob_service_client = BlobServiceClient.from_connection_string(conn_str=connect_str) # create a blob service client to interact with the storage account
    try:
        container_client = blob_service_client.get_container_client(
            container=container_name)  # get container client to interact with the container in which images will be stored
        container_client.get_container_properties()  # get properties of the container to force exception to be thrown if container does not exist
    except Exception as e:
        print(e)
        print("Creating container...")
        container_client = blob_service_client.create_container(container_name)
    try:
        print(f'uploading {filename} to {container_name}...')
        container_client.upload_blob(filename,file)  # upload the file to the container using the filename as the blob name

    except Exception as e:
        print(e)
        print("Ignoring duplicate filenames")  # ignore duplicate filenames


def downloadblob(container_name,dest_path,cnstr):
    os.environ['AZURE_STORAGE_CONNECTION_STRING'] =cnstr
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING') # retrieve the connection string from the environment variable
    # container_name = "vitwouatcontainer" # container name in which images will be store in the storage account
    blob_service_client = BlobServiceClient.from_connection_string(conn_str=connect_str) # create a blob service client to interact with the storage account
    try:
        container_client = blob_service_client.get_container_client(
            container=container_name)

    except Exception as e:
        print(e)

    blob_items = container_client.list_blobs()  # list all the blobs in the container
    img_html = "<div style='display: flex; justify-content: space-between; flex-wrap: wrap;'>"

    for blob in blob_items:
        blob_client = container_client.get_blob_client(
            blob=blob.name)  # get blob client to interact with the blob and get blob url
        try:
            print(f"downloading {blob.name} to {dest_path}......")
            with open(f'{dest_path}/{blob.name}', "wb") as data:

                blob_data = blob_client.download_blob()
                data.write(blob_data.readall())
        except OSError as e:
            print(e)
def deleteblob(container_name,cnstr):
    os.environ['AZURE_STORAGE_CONNECTION_STRING'] =cnstr
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING') # retrieve the connection string from the environment variable
    # container_name = "vitwouatcontainer" # container name in which images will be store in the storage account
    blob_service_client = BlobServiceClient.from_connection_string(conn_str=connect_str) # create a blob service client to interact with the storage account
    try:
        container_client = blob_service_client.get_container_client(
            container=container_name)  # get container client to interact with the container in which images will be stored
        container_client.get_container_properties()
        blob_items = container_client.list_blobs()
        for blob in blob_items:
            blob_client = container_client.get_blob_client(
                blob=blob.name)
            blob_client.delete_blob()

    except Exception as e:
        print(e)
def delfile(container_name,file,cnstr):
    os.environ['AZURE_STORAGE_CONNECTION_STRING'] =cnstr
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING') # retrieve the connection string from the environment variable
    # container_name = "vitwouatcontainer" # container name in which images will be store in the storage account
    blob_service_client = BlobServiceClient.from_connection_string(conn_str=connect_str) # create a blob service client to interact with the storage account
    try:
        container_client = blob_service_client.get_container_client(
            container=container_name)  # get container client to interact with the container in which images will be stored
        container_client.get_container_properties()
        blob_client = container_client.get_blob_client(
                blob=file)
        blob_client.delete_blob()
    except Exception as e:
        print(e)
def downfile(container_name,file,dest_path,cnstr):
    os.environ['AZURE_STORAGE_CONNECTION_STRING'] =cnstr
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING') # retrieve the connection string from the environment variable
    # container_name = "vitwouatcontainer" # container name in which images will be store in the storage account
    blob_service_client = BlobServiceClient.from_connection_string(conn_str=connect_str) # create a blob service client to interact with the storage account
    try:
        container_client = blob_service_client.get_container_client(
            container=container_name)



        blob_client = container_client.get_blob_client(blob=file)
        print(f"downloading {file} to {dest_path}......")
        with open(f'{dest_path}/{file}', "wb") as data:
            blob_data = blob_client.download_blob()
            data.write(blob_data.readall())
            data.close()

                
    except Exception as e:
        print(e)
def blobname(container_name,cnstr):
    os.environ['AZURE_STORAGE_CONNECTION_STRING'] =cnstr
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING') # retrieve the connection string from the environment variable
    # container_name = "vitwouatcontainer" # container name in which images will be store in the storage account
    blob_service_client = BlobServiceClient.from_connection_string(conn_str=connect_str) # create a blob service client to interact with the storage account
    l=[]
    try:
        container_client = blob_service_client.get_container_client(
            container=container_name)

    except Exception as e:
        print(e)
    blob_items = container_client.list_blobs()
    for i in blob_items:
        l.append(i.name)
    return l
# deleteblob('purchase-output')

# with open(r'C:\Users\ACER\PycharmProject\handwriiten\Madan-Mitra.jpg','rb') as d:
#     addtoblob('blob1','madan.jpg',d)

# downloadblobimg('blob1','ne1')
# for i in os.listdir('ne1'):
#     with open(f"ne1/{i}","rb") as f:

#         addtoblob('blob2',i,f)


