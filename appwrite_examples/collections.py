from appwrite.client import Client
from appwrite.id import ID

from appwrite_base import AppwriteBase
from config import Config

class Collections(AppwriteBase):
    def __init__(self, client: Client, cfg: Config, database_id: str):
        super().__init__(client, cfg)

        self.database_id = database_id

    def create_collection(self, collection_name: str, document_security: bool = True) -> dict[str, any]:
        """Создает коллекцию в бд (таблицу)"""
        try:
            result = self.db.create_collection(
                database_id=self.database_id,
                name=collection_name,
                collection_id=ID.unique(padding=15),
                document_security=document_security
            )

            return result
        
        except Exception as err:
            raise RuntimeError(err)
        
    def delete_collection(self, collection_id: str) -> dict[str, any]:
        """Удаляет коллекцию из бд по id"""
        try:
            result = self.db.delete_collection(database_id=self.database_id, collection_id=collection_id)
            return result
        
        except Exception as err:
            raise RuntimeError(err)
        
    
    def add_document(self, collection_id: str, data: dict) -> dict[str, any]:
        """Добавляет запись (документ) в коллекцию по ее id"""
        try:
            result = self.db.create_document(
                database_id=self.database_id,
                collection_id=collection_id,
                data=data
            )

            return result
        
        except Exception as err:
            raise RuntimeError(err)
        
    def delete_document(self, collection_id: str, document_id: str) -> dict[str, any]:
        """Удаляет запить (документ) по его Id"""
        try:
            result = self.db.delete_document(
                database_id=self.database_id,
                collection_id=collection_id,
                document_id=document_id
            )

            return result
        
        except Exception as err:
            raise RuntimeError(err)
        
    def update_document(self, collection_id: str, document_id: str, new_data: dict) -> dict[str, any]:
        """Обновляте записать (документ) по его Id"""
        try:
            result = self.db.update_document(
                database_id=self.database_id,
                collection_id=collection_id,
                document_id=document_id,
                data=new_data
            )

            return result
        
        except Exception as err:
            raise RuntimeError(err)
        
    