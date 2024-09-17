class Agent:
    def __init__(self):
        self.__perceptions = None
        self.__actions = []
        self.__enabled = True

    def set_perceptions(self, p):
        self.__perceptions = p

    def get_perceptions(self):
        return self.__perceptions

    def get_actions(self):
        return self.__actions

    def set_actions(self, a):
        self.__actions = a

    def disable(self):
        self.__enabled = False

    def enable(self):
        self.__enabled = True

    def is_enabled(self):
        return self.__enabled

    def program(self):
        raise Exception("No implementation exists")
