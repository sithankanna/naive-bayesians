# A few things


# 1) Create Nodes and Leafs


class DecisionNode:
    def __init__(self, question, true_vals, false_vals):
        self.question = question
        self.true_vals = true_vals
        self.false_vals = false_vals


def demo_decision_node():

    root = DecisionNode(question="Is Color == Red?", true_vals=None, false_vals=None)
    



    pass


if __name__ == "__main__":
    demo_decision_node()