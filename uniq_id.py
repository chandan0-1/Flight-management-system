import uuid

class UniqId:
    def __init__(self):
        pass

    # -------------------------------------------------------------------------
    # Generates a unique id for objects
    def getId(self):
        return uuid.uuid4().hex