import pandas as pd
import numpy as np
from typing import Tuple

# feature_1, feature_2, label
training_data = pd.DataFrame(
    [
        ["Green", 3, "Apple"],
        ["Yellow", 3, "Apple"],
        ["Red", 1, "Grape"],
        ["Red", 1, "Grape"],
        ["Yellow", 3, "Lemon"],
    ],
    columns=["color", "diameter", "label"],
)


def unique_vals(rows: pd.DataFrame, col: str):
    """Find the unique values for a column in a dataset."""

    return rows[col].drop_duplicates().to_list()


unique_vals(rows=training_data, col="color")

# The goal is to split these people into groups based on the features

# Step 1 Choose which question to asl
#   Step 1: Choose feature
#   Step 2: Choose question within the feature

# Randomly pick a feature (feature 1)

#  Is color == green, split

# split into sublist


def class_prob(rows: pd.DataFrame):
    """Counts the number of each type of example in a dataset."""
    n = len(rows)
    prob = rows.groupby("label").agg(**{"prob": ("label", "count")}) / n
    return prob


def is_numeric(value):
    """Test if a value is numeric."""
    return isinstance(value, int) or isinstance(value, float)


class Question:
    """A Question is used to partition a dataset."""

    def __init__(self, feature, value) -> None:
        self.feature = feature
        self.value = value
        self.is_numeric = is_numeric(self.value)

    def ask(self, example: pd.DataFrame) -> pd.Series:
        if self.is_numeric:
            cond = example[self.feature] >= self.value
        else:
            cond = example[self.feature] == self.value
        return cond

    def __repr__(self) -> str:
        if self.is_numeric:
            cond = ">="
        else:
            cond = "=="

        return f"Is {self.feature} {cond} {self.value}?"


#  Need to ask questions now


# for the leaf node ask
def gini(rows: pd.DataFrame) -> float:
    p_class = class_prob(rows)
    gini_score = 1 - np.sum(p_class["prob"] ** 2)
    return gini_score


def weighted_gini(left: pd.DataFrame, right: pd.DataFrame) -> float:
    n_left = len(left)
    n_right = len(right)
    n = n_left + n_right
    return (n_left / n) * gini(left) + (n_right / n) * gini(right)


def info_gain(current_score: float, new_score: float) -> float:
    return current_score - new_score


def find_best_split(rows: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """X """

    best_gain = 0
    left_node, right_node = None, None
    best_q = None
    current_score = gini(rows)

    # splits
    for feature in ["color", "diameter"]:
        possible_values = unique_vals(rows=rows, col=feature)
        for val in possible_values:
            # Ask the question for each training sample
            q = Question(feature, val)
            is_left_node = q.ask(rows)

            # Split the dataframe to left and right nodes
            left_, right_ = rows[is_left_node], rows[~is_left_node]

            # Find the information gain from the split
            gini_score_after_split = weighted_gini(left_, right_)
            info_gain_from_split = info_gain(current_score, gini_score_after_split)

            # If info gain
            if info_gain_from_split >= best_gain:
                best_q = q
                best_gain = info_gain_from_split
                left_node, right_node = left_, right_

    return best_q, best_gain, left_node, right_node

    class DecisionNode:
        def __init__(
            self, question: str, true_rows: pd.DataFrame, false_rows: pd.DataFrame
        ):
            self.question = question
            self.true_rows = true_rows
            self.false_rows = false_rows

    def build_tree(rows):

        best_q, best_gain, left, right = find_best_split(rows)

        if best_gain == 0:
            return

        left_ = build_tree(left)
        right_ = build_tree(right)

        return DecisionNode(best_q, left_, right_)

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.children = []
            self.parent = None

        def add_children(self, data):
            pass

    root = Tree


class DecisionNode:
    def __init__(self, question: str, true_node, false_node):
        self.question = question
        self.true_node = true_node
        self.false_node = false_node

    def print_tree(self, level: int = None):

        if level is None:
            level = 0

        spaces = " " * 2 ** level
        prefix = spaces + "|_" if level > 0 else ""

        print(prefix, self.question)

        if self.true_node is not None:
            self.true_node.print_tree(level=level + 1)
        if self.false_node is not None:
            self.false_node.print_tree(level=level + 1)


root = DecisionNode(question="is x > y?", true_node=None, false_node=None)


# Goal is to keep splitting until it can't split no more
# Goal is to build a tree based out of Decision Nodes


def build_tree_2(rows):
    best_q, best_gain, left_node, right_node = find_best_split(rows)

    if best_gain == 0:
        print(class_prob(rows))
        return

    left_best_q = build_tree_2(left_node)
    right_best_q = build_tree_2(right_node)

    return DecisionNode(question=best_q, true_node=left_best_q, false_node=right_best_q)


def classify(rows, node):
    if isinstance(node, Leaf):
        return node.class_probs

    is_true = node.question.ask(rows)
    # Split the dataframe to left and right nodes
    left_, right_ = rows[is_true], rows[~is_true]

    if len(left_) > 0:
        return classify(left_, node.true_node)
    if len(right_) > 0:
        return classify(right_, node.false_node)


# Actions: Classify new lables


