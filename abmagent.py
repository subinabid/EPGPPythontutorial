"""This is an opinion dynamics model"""

FRIENDSHIP_THRESHOLD = 0.7

class Agent:
    """An agent with an opinion, resistance to change, and influence over others."""

    species: str = "human" # This is a class variable shared by all agents

    # These are instance variables
    # All variables are unique to each agent

    def __init__(self, id: int, opinion: float, resistance: float, influence: float):
        self.id = id
        self.opinion = opinion
        self.resistance = resistance
        self.influence = influence
        self.friends = [] # List to hold friends (other Agent instances)
    
    def add_friend(self, buddy):
        """Add a friend to the agent's social network."""
        if buddy not in self.friends:
            self.friends.append(buddy)
            buddy.friends.append(self) # Ensure bidirectional friendship
    
    def remove_friend(self, buddy):
        """Remove a friend from the agent's social network."""
        if buddy in self.friends:
            self.friends.remove(buddy)
            buddy.friends.remove(self) # Ensure bidirectional removal
    
    def update_opinion(self, buddy):
        pass # Dont do anything for now

    def interact(self, buddy):
        """Interact with friends to potentially update opinion.
        consioder influence to be their ideology
        + 1 is far right
        -1 is far left
        if influence is very similar, they will continue to be friends
        if influence is very different, they stop being friends
        difference in influence > 0.3 -> remove friend
        """
        higher = max(self.influence, buddy.influence) #.03
        lower = min(self.influence, buddy.influence) #-1
        influence_diff = (higher - lower)
        print(f"Agent {self.id} interacting with Agent {buddy.id}: influence difference = {influence_diff}")
        if influence_diff > FRIENDSHIP_THRESHOLD:
            self.remove_friend(buddy)
        

a1 = Agent(1, 0.5, 0.5, -1) # Subin
a2 = Agent(2, 0.7, 0.3, 0.6) # Vivek
a3 = Agent(3, 0.4, 0.5, 0.9) # Melvin
a4 = Agent(4, 0.9, 0.1, 0.7)
a5 = Agent(5, 0.3, 0.4, 0.5)

a1.add_friend(a2) # Subin and Vivek are friends
a1.add_friend(a3) # Subin and Melvin are friends
a2.add_friend(a1) # No effect, already friends
a2.add_friend(a3) # Vivek and Melvin are friends
a4.add_friend(a5)

print(f"Agent {a1.id} opinion: {a1.opinion}, resistance: {a1.resistance}, influence: {a1.influence}")
print(f"Agent {a2.id} opinion: {a2.opinion}, resistance: {a2.resistance}, influence: {a2.influence}")
print(f"Agent {a3.id} opinion: {a3.opinion}, resistance: {a3.resistance}, influence: {a3.influence}")
print(f"Agent {a4.id} opinion: {a4.opinion}, resistance: {a4.resistance}, influence: {a4.influence}")
print(f"Agent {a5.id} opinion: {a5.opinion}, resistance: {a5.resistance}, influence: {a5.influence}")


print(f"Agent {a1.id} friends: {[friend.id for friend in a1.friends]}")
print(f"Agent {a2.id} friends: {[friend.id for friend in a2.friends]}")
print(f"Agent {a3.id} friends: {[friend.id for friend in a3.friends]}")
print(f"Agent {a4.id} friends: {[friend.id for friend in a4.friends]}")
print(f"Agent {a5.id} friends: {[friend.id for friend in a5.friends]}")

# Simulate interactions
a1.interact(a2) # Subin and Vivek interact
a1.interact(a3) # Subin and Melvin interact
a2.interact(a3) # Vivek and Melvin interact

print("After interactions:")
print(f"Agent {a1.id} friends: {[friend.id for friend in a1.friends]}")
print(f"Agent {a2.id} friends: {[friend.id for friend in a2.friends]}")
print(f"Agent {a3.id} friends: {[friend.id for friend in a3.friends]}")