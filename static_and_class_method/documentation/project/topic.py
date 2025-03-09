class Topic:
    def __init__(self, id, topic, storage_folder):
        self.id = id
        self.topic = topic
        self.storage_folder = storage_folder

    def edit(self, topic, folder):
        self.topic = topic
        self.storage_folder = folder

    def __repr__(self):
        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"
