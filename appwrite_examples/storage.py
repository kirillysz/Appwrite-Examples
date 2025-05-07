from appwrite.client import Client
from appwrite.id import ID
from appwrite.enums.compression import Compression
from appwrite.input_file import InputFile

from appwrite_base import AppwriteBase
from config import Config

class Storage(AppwriteBase):
    def __init__(self,  client: Client, cfg: Config):
        super().__init__(client, cfg)

    def create_bucket(self, bucket_name: str, 
                      maximum_file_size: int = 50000000,
                      compression: Compression = Compression("gzip")):
        
        """Добавляет новое хранилище (maximum_file_size указывается в байтах числом)"""
        try:
            result = self.storage.create_bucket(
                bucket_id=ID.unique(padding=15),
                name=bucket_name,
                file_security=True,
                maximum_file_size=maximum_file_size,
                encryption=True,
                antivirus=True,
                compression=compression,
                enabled=True
            )

            return result
        
        except Exception as err:
            raise RuntimeError(err)
        
    def delete_bucket(self, bucket_id: str) -> dict[str, any]:
        """Удаляет хранилище по его id"""
        try:
            result = self.storage.delete_bucket(bucket_id=bucket_id)
            return result
        
        except Exception as err:
            raise RuntimeError(err)
        
    
    def create_file(self, bucket_id: str, file_path: str) -> dict[str, any]:
        """Создает новый файл"""
        try:
            result = self.storage.create_file(
                bucket_id=bucket_id,
                file_id=ID.unique(padding=15),
                file=InputFile().from_path(path=file_path)
            )

            return result
        
        except Exception as err:
            raise RuntimeError(err)
    
    def delete_file(self, bucket_id: str, file_id: str) -> dict[str, any]:
        """Удаляет файл по его айди"""
        try:
            result = self.storage.delete_file(bucket_id=bucket_id, file_id=file_id)
            return result
        
        except Exception as err:
            raise RuntimeError(err)
    
    