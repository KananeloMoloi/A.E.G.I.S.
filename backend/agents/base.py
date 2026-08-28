class Agent: 

    def __init__(self,name, description):

        self.name = name
        self.description = description

    def run(self,task):

        raise NotImplementedError(
            "This Agent does not have a run() method yet."
        )