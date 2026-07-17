#!/usr/bin/env python3
"""
Modul sənədləşdirməsi (Module documentation)
Kolleksiyadakı sənədləri siyahılamaq üçün funksiya.
"""


def list_all(mongo_collection):
    """
    List all documents in a collection.
    Return an empty list if no document in the collection.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
