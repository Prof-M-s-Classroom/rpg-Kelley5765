class StoryNode:
    """Represents a node in the decision tree."""

    def __init__(self, event_number, description, left=None, right=None):
        print(f"TODO: Initialize StoryNode with event_number={event_number}, description={description}")
        # TODO: Initialize instance variables (event_number, description, left, right)
        self.event_number = event_number
        self.description = description
        self.left = left  # Should be None if no left child
        self.right = right  # Should be None if no right child


class GameDecisionTree:
    """Binary decision tree for the RPG."""

    def __init__(self):
        print("TODO: Initialize an empty decision tree")
        # TODO: Initialize an empty dictionary to store nodes
        # TODO: Set root to None
        self.nodes = {}
        self.root = None

    def insert(self, event_number, description, left_event, right_event):
        """Insert a new story node into the tree."""
        print(f"TODO: Insert event {event_number} with description '{description}' into the tree")
        # TODO: Check if event_number exists in self.nodes, if not create a new StoryNode
        # TODO: Assign left and right children based on left_event and right_event
        # TODO: Set root if it's the first node inserted

        # '-1' to None to prevent KeyErrors
        left_value = None if left_event == '-1' else left_event
        right_value = None if right_event == '-1' else right_event

        if event_number not in self.nodes:
            self.nodes[event_number] = StoryNode(event_number, description, left_value, right_value)
        else:
            # If node exists, update
            self.nodes[event_number].description = description
            self.nodes[event_number].left = left_value
            self.nodes[event_number].right = right_value

        # Set root as first event
        if self.root is None:
            self.root = self.nodes[event_number]

    def play_game(self):
        """Interactive function that plays the RPG."""
        print("TODO: Implement the game logic for traversing the decision tree")
        # TODO: Start from the root node
        # TODO: Loop through player choices, navigating left or right based on input
        # TODO: Print event descriptions and ask for player decisions
        # TODO: End game when reaching a leaf node (where left and right are None)

        current_node = self.root

        while current_node:
            print('\n' + current_node.description)

            # Check if node is an ending (both left and right are None), stop game
            if current_node.left is None and current_node.right is None:
                print('Game over')
                break

            # Ask for player input
            while True:
                choice = input('Choose an action (1 or 2): ')
                if choice == '1' and current_node.left is not None:
                    current_node = self.nodes[current_node.left]
                    break
                elif choice == '2' and current_node.right is not None:
                    current_node = self.nodes[current_node.right]
                    break
                else:
                    print('Invalid choice, please try again')


def load_story(filename, game_tree):
    """Load story from a file and construct the decision tree."""
    print(f"TODO: Read story file '{filename}' and parse events")
    # TODO: Open the file and read line by line
    # TODO: Split each line into event_number, description, left_event, right_event
    # TODO: Call game_tree.insert() for each event to build the tree

    with open(filename) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = [part.strip() for part in line.split('|')]
            if len(parts) < 4:
                print(f"Invalid line: {line}")
                continue

            # Extract and insert into tree
            event_number, description, left_event, right_event = parts
            game_tree.insert(event_number, description, left_event, right_event)


# Main program
if __name__ == "__main__":
    print("TODO: Initialize the GameDecisionTree and load story data")
    game_tree = GameDecisionTree()

    print("TODO: Load the story from 'story.txt'")
    load_story("story.txt", game_tree)

    print("TODO: Start the RPG game")
    game_tree.play_game()
