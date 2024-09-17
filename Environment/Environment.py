class Environment:
    def __init__(self):
        self.agents = []

    def get_perceptions(self, agent):
        raise Exception("No implementation exists")

    def execute(self, agent):
        raise Exception("No implementation exists")

    def evolve(self):
        if not self.finish():
            for agent in self.agents:
                self.get_perceptions(agent)
                self.execute(agent)

    def run(self):
        while True:
            if self.finish():
                break
            self.evolve()

    def finish(self):
        return any(not agent.is_alive for agent in self.agents)

    def insert(self, agent):
        self.agents.append(agent)
