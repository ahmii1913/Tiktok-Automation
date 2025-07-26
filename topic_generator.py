import random

trending_players = [
    "Messi", "Cristiano Ronaldo", "Mbappe", "Haaland", "Neymar",
    "IShowSpeed", "MrBeast", "Vinicius Jr", "Bellingham", "Modric"
]

funny_actions = [
    "goal celebration fail", "rage moment", "funny dive", "angry coach reaction",
    "savage tackle", "winning moment", "epic comeback", "funny VAR decision"
]

def generate_topics(num=10, language="en"):
    topics = []
    for _ in range(num):
        player = random.choice(trending_players)
        action = random.choice(funny_actions)

        if language == "ur":
            template = f"{player} ka {action} 😂🔥"
        elif language == "hi":
            template = f"{player} ka zabardast {action} 🤯"
        else:
            template = f"{player}'s {action} went viral! 😱⚽"
        
        topics.append(template)
    return topics
