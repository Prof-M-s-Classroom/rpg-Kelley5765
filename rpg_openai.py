import openai
import os

openai.api_key = "I used OPENAI key but removed before pushing"  # TODO: Paste your OPENAI Key here


def generate_rpg_story():
    client = openai.OpenAI(api_key=openai.api_key)

    prompt = """You are an AI that generates structured RPG stories in a binary decision tree format.  
The story follows Titus, a fearless and relentless Ultramarine serving in the Deathwatch, conducting a mission aboard a xenos-infested space hulk.  
The tone is intense, grim, and true to the Warhammer 40K universe. Titus never hesitates, never fears, and makes decisive choices in battle.  

Instructions for the Decision Tree:
- The story must be formatted as:  
  [Node Number] | [Narrative] [Numbered Choices] | [Next Node for Choice 1] | [Next Node for Choice 2]  
- Titus must be portrayed as brave, relentless, and unwavering in the face of danger.  
- Each decision must have clear consequences, and the paths should be varied:  
  - Some paths should lead to victory (good endings).
  - Some should end in honorable but tragic defeat (bad endings).  
  - There should be no cowardly or retreating options, Titus always fights to the end.
- Each event should be brief yet impactful, fitting within one or two sentences 
- Ensure numbered choices (e.g., "1) confront it head-on or 2) lure it into an ambush?") for clarity.  
- Mark good and bad endings (e.g., "(Good Ending: Tactical Triumph)", "(Bad Ending: Heroic Last Stand)").  
- Each ending at -1 must be conclusive, showing either triumph, sacrifice, or destruction. 

Decision Tree Structure:
1  | [Starting event]   | 2  | 3  
2  | [Decision point]   | 4  | 5  
3  | [Decision point]   | 5  | 6  
4  | [Decision point]   | -1 | -1  
5  | [Decision point]   | 7  | 8  
6  | [Decision point]   | 8  | 9  
7  | [Decision point]   | -1 | -1  
8  | [Decision point]   | 10 | 11  
9  | [Final confrontation] | -1 | -1  
10 | [Final choice]     | -1 | -1  
11 | [Bad ending]       | -1 | -1  

1. Do not change the format. Ensure output follows the given decision tree structure exactly.
3. The narrative should be brief yet impactful. Each event should fit within one or two sentences.
4. Ensure the file is fully formatted for use in an RPG decision tree.
5. Make sure -1 endings are conclusive
"""  # TODO: Prompt engineer to get the exact story format you want here.

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are an AI that generates structured RPG stories."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def save_story_to_file(filename, story_text):
    # TODO: Store the generated text into story.txt
    with open(filename, 'w') as file:
        file.write(story_text)


if __name__ == "__main__":
    story_text = generate_rpg_story()
    save_story_to_file("story.txt", story_text)