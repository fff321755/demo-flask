from application_services.BaseApplicationResource import BaseRDBApplicationResource
from database_services.RDBService import RDBService


class PostResource(BaseRDBApplicationResource):


    def __init__(self):
        super().__init__()
        
    @classmethod
    def get_data_resource_info(cls):
        return 'post_comment', 'posts'

    
    @classmethod
    def get_by_title_substr(cls, title_substr):
        db_name, table_name = cls.get_data_resource_info()
        res = RDBService.get_by_substr(db_name, table_name,
                                      "title", title_substr)
        return res


    @classmethod
    def post_posts(cls, resource_data):
        db_name, table_name = cls.get_data_resource_info()
        return RDBService.create(db_name, table_name , resource_data)

  
