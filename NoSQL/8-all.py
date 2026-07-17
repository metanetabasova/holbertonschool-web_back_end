def list_all(mongo_collection):
    """
    Kolleksiyadakı bütün sənədləri siyahı şəklində qaytarır.
    Əgər sənəd yoxdursa, boş siyahı ([]) qaytarır.
    """
    if mongo_collection is None:
        return []
    
    return list(mongo_collection.find())
