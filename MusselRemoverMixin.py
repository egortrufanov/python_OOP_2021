class MusselRemoverMixin:
    def __init__(self):
        self.ingredients = []

    def remove_mussels(self):
        self.ingredients.remove("mussels")
