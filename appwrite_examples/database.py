from appwrite.id import ID

from appwrite_base import AppwriteBase

class Database(AppwriteBase):
    def __init__(self, client):
        super().__init__(client)

    def create_database(self, database_name: str) -> dict[str, any]:
        """Создает базу данных в Appwrite"""
        try:
            result = self.db.create(
                database_id=ID.unique(padding=16),
                name=database_name,
                enabled=True
            )

            return result

        except Exception as err:
            raise RuntimeError(err)
        
    def get_database(self, database_id: str) -> dict[str, any]:
        """Получает инфу о базе данных по ее Id"""
        try:
            result = self.db.get(database_id=database_id)
            return result
        
        except Exception as err:
            raise RuntimeError(err)
         
