from abc import ABC, abstractmethod


class ObjectManager(ABC):
    def __init__(self, object):
        self.object = object


