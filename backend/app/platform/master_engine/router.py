from fastapi import APIRouter


class MasterRouter:

    def __init__(self):
        self.router = APIRouter()

    def build(self):
        return self.router