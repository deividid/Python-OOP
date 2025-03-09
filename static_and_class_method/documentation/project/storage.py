from typing import List

from project.category import Category

from project.topic import Topic

from project.document import Document


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, cat: Category):
        if cat not in self.categories:
            self.categories.append(cat)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, doc: Document):
        if doc not in self.documents:
            self.documents.append(doc)

    def edit_category(self, cat_id, new_name):
        for category in self.categories:
            if category.id == cat_id:
                category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_folder):
        for topic in self.topics:
            if topic.id == topic_id:
                topic.edit(new_topic, new_folder)

    def edit_document(self, doc_id, new_name):
        for doc in self.documents:
            if doc.id == doc_id:
                doc.edit(new_name)

    def delete_topic(self, topic_id):
        for topic in self.topics:
            if topic.id == topic_id:
                self.topics.remove(topic)

    def delete_category(self, cat_id):
        for category in self.categories:
            if category.id == cat_id:
                self.categories.remove(category)

    def delete_document(self, doc_id):
        for doc in self.documents:
            if doc.id == doc_id:
                self.documents.remove(doc)

    def get_document(self, doc_id):
        for doc in self.documents:
            if doc.id == doc_id:
                return doc

    def __repr__(self):

        result = ""
        for doc in self.documents:
            result += f"{doc}\n"

        return result






