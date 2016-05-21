from pymongo import ReturnDocument
from bson.objectid import ObjectId


class BaseDAO(object):
    def get_by_id(self, document_id):
        return self.collection.find_one({'_id': document_id})

    def get_all(self):
        return self.collection.find()

    def create(self, **kwargs):
        document = kwargs
        allocated_id = self.collection.insert_one(document).inserted_id
        document['_id'] = allocated_id
        return document

    def delete(self, document_id):
        return self.collection.find_one_and_delete({'_id': ObjectId(document_id)})

    def save(self, document_id, updated_document):
        return self.collection.find_one_and_replace(
            {'_id': ObjectId(document_id)},
            updated_document,
            return_document=ReturnDocument.AFTER
        )

    def update(self, document_id, partial_document):
        return self.collection.find_one_and_update(
            {'_id': ObjectId(document_id)},
            {'$set': partial_document},
            return_document=ReturnDocument.AFTER
        )