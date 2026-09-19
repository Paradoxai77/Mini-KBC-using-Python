import time
import random

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
      {
        "question": "Who developed the theory of General Relativity?",
        "options": ["A) Isaac Newton", "B) Albert Einstein", "C) Galileo Galilei", "D) Stephen Hawking"],
        "answer": "B"
    },
    {
        "question": "Which algorithm is used in Google's PageRank?",
        "options": ["A) BFS", "B) DFS", "C) Markov Chain", "D) Dijkstra"],
        "answer": "C"
    },
    {
        "question": "What is the time complexity of binary search?",
        "options": ["A) O(n)", "B) O(n log n)", "C) O(log n)", "D) O(1)"],
        "answer": "C"
    },
    {
        "question": "Who is known as the father of AI?",
        "options": ["A) John McCarthy", "B) Alan Turing", "C) Marvin Minsky", "D) Geoffrey Hinton"],
        "answer": "A"
    },
    {
        "question": "Which planet has the most moons?",
        "options": ["A) Saturn", "B) Jupiter", "C) Uranus", "D) Neptune"],
        "answer": "A"
    },
    {
"question": "Which sorting algorithm is best for nearly sorted data?",
        "options": ["A) Quick Sort", "B) Merge Sort", "C) Bubble Sort", "D) Insertion Sort"],
        "answer": "D"
    },
    {
        "question": "In which year did the C language appear?",
        "options": ["A) 1969", "B) 1972", "C) 1979", "D) 1983"],
        "answer": "B"
    },
    {
        "question": "What is the full form of HTTP?",
        "options": ["A) Hyper Transfer Text Protocol", "B) Hyper Text Transfer Protocol", "C) High Text Transfer Protocol", "D) Hyper Text Transmission Protocol"],
        "answer": "B"
    },
    {
        "question": "Who is the current CEO of Google (as of 2025)?",
        "options": ["A) Satya Nadella", "B) Tim Cook", "C) Sundar Pichai", "D) Jeff Bezos"],
        "answer": "C"
    },
    {
        "question": "Which logic gate outputs true only when inputs differ?",
        "options": ["A) AND", "B) OR", "C) XOR", "D) NOR"],
        "answer": "C"
    },
    {
        "question": "Which Indian scientist won a Nobel Prize in Physics?",
        "options": ["A) C.V. Raman", "B) Homi Bhabha", "C) A.P.J. Abdul Kalam", "D) Vikram Sarabhai"],
        "answer": "A"
    },
    {
        "question": "What is the capital of Kazakhstan?",
"options": ["A) Astana", "B) Almaty", "C) Tashkent", "D) Bishkek"],
        "answer": "A"
    },
    {
        "question": "Which country has the largest proven oil reserves?",
        "options": ["A) USA", "B) Saudi Arabia", "C) Venezuela", "D) Russia"],
        "answer": "C"
    },
    {
        "question": "Which number is neither prime nor composite?",
        "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "answer": "B"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A) Quartz", "B) Gold", "C) Diamond", "D) Graphite"],
        "answer": "C"
    },
    {
        "question": "Which Indian city is known as 'Silicon Valley of India'?",
        "options": ["A) Pune", "B) Bengaluru", "C) Hyderabad", "D) Chennai"],
        "answer": "B"
    },
    {
        "question": "Which programming language is used for AI the most?",
        "options": ["A) Java", "B) Python", "C) C#", "D) Ruby"],
        "answer": "B"
    },
    {
        "question": "Which planet has the longest day?",
        "options": ["A) Mercury", "B) Venus", "C) Mars", "D) Jupiter"],
        "answer": "B"
    },
    {
        "question": "Which Indian satellite was first launched into space?",
"options": ["A) INSAT-1", "B) Aryabhata", "C) PSLV", "D) Bhaskara"],
        "answer": "B"
    },
    {
        "question": "What is the full form of RAM?",
        "options": ["A) Read All Memory", "B) Random Access Memory", "C) Run Access Mode", "D) Real Action Memory"],
        "answer": "B"
    },
    {
        "question": "Who painted the famous 'Mona Lisa'?",
        "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet"],
        "answer": "C"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A) WA", "B) H2O", "C) HO2", "D) OW"],
        "answer": "B"
    },
    {
        "question": "Which country is known as the 'Land of the Rising Sun'?",
        "options": ["A) China", "B) South Korea", "C) Thailand", "D) Japan"],
        "answer": "D"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Pacific Ocean", "D) Arctic Ocean"],
        "answer": "C"
    },
    {
        "question": "In what year did the reunification of Germany take place?",
        "options": ["A) 1989", "B) 1990", "C) 1991", "D) 1992"],
        "answer": "B"
    },
    {
        "question": "Where is the Great Victoria Desert located?",
        "options": ["A) Africa", "B) South America", "C) Australia", "D) North America"],
        "answer": "C"
    },
    {
        "question": "Who sang the title song for the James Bond film 'No Time to Die'?",
        "options": ["A) Adele", "B) Sam Smith", "C) Billie Eilish", "D) Beyonce"],
        "answer": "C"
    },
    {
        "question": "Which country stands first in the generation of geothermal energy?",
        "options": ["A) USA", "B) Iceland", "C) New Zealand", "D) Italy"],
        "answer": "B"
    },
    {
        "question": "Daniel Radcliffe became a global star in the film industry due to his performance in which film franchise?",
        "options": ["A) Harry Potter", "B) Pirates of the Caribbean ", "C) Spy Kids", "D) Ted"],
        "answer": "A"
    },
    {
        "question": "Killing Floor started as a mod for which Unreal Engine 2 game?",
        "options": ["A) Unreal Tournament 2004", "B) Deus Ex: Invisible War", "C) Unreal Tournament 3", "D) Postal"],
        "answer": "A"
    },
    {
        "question": "Which is the most popular spoken language in the Southern Hemisphere?",
        "options": ["A) Spanish", "B) English ", "C) Portuguese", "D) French"],
        "answer": "C"
    },
    {
        "question": "Which of these weapon classes DO NOT appear in the first Monster Hunter game?",
        "options": ["A) Light Bowgun", "B) Bow ", "C) Heavy Bowgun", "D) Hammer"],
        "answer": "B"
    },
    {
        "question": "Which US state is nicknamed \"The Golden State\"?",
        "options": ["A) California", "B) Florida", "C) New Mexico", "D) Alaska"],
        "answer": "A"
    },
    {
        "question": "How many rivers are in Saudi Arabia?",
        "options": ["A) 0", "B) 3", "C) 1", "D) 2"],
        "answer": "A"
    },
    {
        "question": "What type of cheese, loved by Wallace and Gromit, had it's sale prices rise after their successful short films?",
        "options": ["A) Moon Cheese", "B) Cheddar", "C) Wensleydale", "D) Edam"],
        "answer": "C"
    },
    {
        "question": "In TF2 Lore, what are the names of the Heavy's younger sisters?",
        "options": ["A) Yanna and Gaba", "B) Anna and Bronislava", "C) Gaba and Anna", "D) Yana and Bronislava"],
        "answer": "D"
    },
    {
        "question": "In Disney's \"Toontown Online\", which of these species wasn't available as a Toon?",
        "options": ["A) Cow", "B) Pig", "C) Bear", "D) Monkey"],
        "answer": "A"
    },
    {
        "question": "When did O, Canada officially become the national anthem?",
        "options": ["A) 1920", "B) 1980", "C) 1950", "D) 1880"],
        "answer": "B"
    },
    {
        "question": "Who was Hannibal?",
        "options": ["A) Carthaginian general", "B) French explorer", "C) British serial killer", "D) Greek philosopher"],
        "answer": "A"
    },
    {
        "question": "Which actor auditioned for the role of Luke Skywalker?",
        "options": ["A) Laurence Fishburne", "B) Kurt Russell", "C) Christopher Lambert", "D) James Remar"],
        "answer": "B"
    },
    {
        "question": "Which stand-up comedian voiced the talking parrot \"Iago\" in Disney's 1992 adaptation of Aladdin?",
        "options": ["A) Robin Williams", "B) Pauly Shore", "C) Jonathan Freeman", "D) Gilbert Gottfried"],
        "answer": "D"
    },
    {
        "question": "Who wrote and directed the 1986 film 'Platoon'?",
        "options": ["A) Francis Ford Coppola", "B) Michael Cimino", "C) Stanley Kubrick", "D) Oliver Stone"],
        "answer": "D"
    },
    {
        "question": "What song originally performed by The Bee Gees in 1978 had a cover version by Steps 20 years later?",
        "options": ["A) Night Fever", "B) Stayin' Alive", "C) You Should Be Dancing", "D) Tragedy"],
        "answer": "D"
    },
    {
        "question": "Who is the lead singer of the band Coldplay?",
        "options": ["A) Chris Martin", "B) Chris Isaak", "C) Chris Wallace", "D) Chris Connelly"],
        "answer": "A"
    },
    {
        "question": "What year did the anime \"Himouto! Umaru-chan\" air?",
        "options": ["A) 2014", "B) 2012", "C) 2013", "D) 2015"],
        "answer": "D"
    },
    {
        "question": "Which superhero is known for his super speed?",
        "options": ["A) Batman", "B) Flash", "C) Spiderman", "D) Superman"],
        "answer": "B"
    },
    {
        "question": "What is the name of the very first video uploaded to YouTube?",
        "options": ["A) Me at the zoo", "B) Her new puppy from great grandpa vern.", "C) tribute", "D) carrie rides a truck"],
        "answer": "A"
    },
    {
        "question": "Who is the bassist of the British rock band Queen?",
        "options": ["A) John Barrowman", "B) John Mayer", "C) John Deacon", "D) John Major"],
        "answer": "C"
    },
    {
        "question": "In the Portal series of games, who was the founder of Aperture Science?",
        "options": ["A) Gordon Freeman", "B) Cave Johnson", "C) Wallace Breen", "D) GLaDOs"],
        "answer": "B"
    },
    {
        "question": "What does the \"G\" mean in \"G-Man\"?",
        "options": ["A) Government", "B) Going", "C) Geronimo", "D) Ghost"],
        "answer": "A"
    },
    {
        "question": "Which driver has been the Formula 1 world champion for a record 7 times?",
        "options": ["A) Jim Clark", "B) Fernando Alonso", "C) Ayrton Senna", "D) Michael Schumacher"],
        "answer": "D"
    },
    {
        "question": "In Norse Mythology, what is the name of the symbol commonly referred to as the \"Tree of Life\"?",
        "options": ["A) Odin's Roots", "B) Yggdrasil", "C) Ymir", "D) Tree of the Earth"],
        "answer": "B"
    },
    {
        "question": "In \"Star Trek\", what sauce is commonly used by Klingons on bregit lung?",
        "options": ["A) Gazorpazorp pudding", "B) Grapork sauce", "C) Grapok sauce", "D) Sweet chili sauce"],
        "answer": "C"
    },
    {
        "question": "In the Magic: The Gathering universe, the Fallen Empires expansion takes place on which continent?",
        "options": ["A) Terisiare", "B) Shiv", "C) Sarpadia", "D) Otaria"],
        "answer": "C"
    },
    {
        "question": "The heavy metal band Black Sabbath hail from which English city?",
        "options": ["A) Manchester", "B) Newcastle-Upon-Tyne", "C) Birmingham", "D) London"],
        "answer": "C"
    },
    {
        "question": "An organism described as \"heliotropic\" has a tendancy to move towards which of these things?",
        "options": ["A) Trees", "B) Water", "C) Pollen", "D) Light"],
        "answer": "D"
    },
    {
        "question": "In the game Half-Life, which enemy is showcased as the final boss?",
        "options": ["A) Dr. Wallace Breen", "B) G-Man", "C) The Nihilanth", "D) The Gonarch"],
        "answer": "C"
    },
    {
        "question": "Which famous military commander marched an army, which included war elephants, over the Alps during the Second Punic War?",
        "options": ["A) Hannibal", "B) Tiberius", "C) Alexander the Great", "D) Garmanicus"],
        "answer": "A"
    },
    {
        "question": "What is the name of the \"tool\" used to hit the white ball in snooker or billiards?",
        "options": ["A) Mallet", "B) Racquet", "C) Cue", "D) Bat"],
        "answer": "C"
    },
    {
        "question": "What nationality was the surrealist painter Salvador Dali?",
        "options": ["A) French", "B) Italian", "C) Spanish", "D) Portuguese"],
        "answer": "C"
    },
    {
        "question": "In 2012, which movie won every category in the 32nd \"Golden Raspberry Awards\"?",
        "options": ["A) Thor", "B) The Girl with the Dragon Tattoo", "C) The King's Speech", "D) Jack and Jill"],
        "answer": "D"
    },
    {
        "question": "What alcoholic drink is mainly made from juniper berries?",
        "options": ["A) Rum", "B) Vodka", "C) Gin", "D) Tequila"],
        "answer": "C"
    },
    {
        "question": "Coleslaw originated from which European country?",
        "options": ["A) The Netherlands", "B) United Kingdom", "C) Denmark", "D) Germany"],
        "answer": "A"
    },
    {
        "question": "What was the subject of the 2014 song \"CoCo\" by American rapper O. T. Genasis?",
        "options": ["A) Coconut cream pie", "B) Cobalt(II) carbonate", "C) Conan O'Brien", "D) Cocaine"],
        "answer": "D"
    },
    {
        "question": "Edson Arantes do Nascimento is the full name of which legendary football player?",
        "options": ["A) Ronaldinho", "B) Zico", "C) Pel\u00e9", "D) Rom\u00e1rio"],
        "answer": "C"
    },
    {
        "question": "What is the mathematician Euler's first name?",
        "options": ["A) Lionel", "B) Leonhard", "C) Ajan", "D) Andrin"],
        "answer": "B"
    },
    {
        "question": "Where was Kanye West born?",
        "options": ["A) Los Angeles, California", "B) Chicago, Illinois", "C) Detroit, Michigan", "D) Atlanta, Georgia"],
        "answer": "D"
    },
    {
        "question": "What is the full meaning of RAM?",
        "options": ["A) Rand Assist Mandate", "B) Random Assist Memory", "C) Random Access Memory", "D) Ram"],
        "answer": "C"
    },
    {
        "question": "What is generally considered to be William Shakespeare's birth date?",
        "options": ["A) April 23rd, 1564", "B) July 4th, 1409", "C) September 29th, 1699", "D) December 1st, 1750"],
        "answer": "A"
    },
    {
        "question": "What is the name of the queen's pet in A Bug's Life?",
        "options": ["A) Hopper", "B) Flik", "C) Dot", "D) Aphie"],
        "answer": "D"
    },
    {
        "question": "Which artist painted the late 15th century mural 'The Last Supper'?",
        "options": ["A) Luca Pacioli", "B) Piero della Francesca", "C) Leonardo da Vinci", "D) Paolo Uccello"],
        "answer": "C"
    },
    {
        "question": "What nuts are used in the production of marzipan?",
        "options": ["A) Pistachios", "B) Almonds", "C) Peanuts", "D) Walnuts"],
        "answer": "B"
    },
    {
        "question": "When was the Sega Genesis released in Japan?",
        "options": ["A) November 30, 1990", "B) September 1, 1986", "C) October 29, 1988", "D) August 14, 1989"],
        "answer": "C"
    },
    {
        "question": "Which famous 90's rap album is commonly referred to as \"The Bible of Hip Hop\"?",
        "options": ["A) The Low End Theory", "B) Enter The Wu-Tang (36 Chambers)", "C) Illmatic", "D) The Chronic"],
        "answer": "C"
    },
    {
        "question": "The New York Times slogan is, \u201cAll the News That\u2019s Fit to\u2026\u201d",
        "options": ["A) Print", "B) Read", "C) Digest", "D) Look"],
        "answer": "A"
    },
    {
        "question": "What amount of bits commonly equals one byte?",
        "options": ["A) 1", "B) 64", "C) 2", "D) 8"],
        "answer": "D"
    },
    {
        "question": "What is the final game of the \"Zero Escape\" series called?",
        "options": ["A) Nine Hours, Nine Persons, Nine Doors ", "B) Zero Escape Zero Time Dilemma ", "C) The Nonary Game: Sigma's Last Life", "D) Zero Escape Virtue's Last Reward"],
        "answer": "B"
    },
    {
        "question": "George Orwell wrote this book, which is often considered a statement on government oversight.",
        "options": ["A) The Old Man and the Sea", "B) 1984", "C) To Kill a Mockingbird", "D) Catcher and the Rye"],
        "answer": "B"
    },
    {
        "question": "Which of these bones is hardest to break?",
        "options": ["A) Femur", "B) Humerus", "C) Tibia", "D) Cranium"],
        "answer": "A"
    },
    {
        "question": "What does the D stand for in D-pad, found on most video game controllers?",
        "options": ["A) Directional", "B) Dynamic", "C) Dial-up", "D) Design"],
        "answer": "A"
    },
    {
        "question": "Which of the following is an album by punk rock band Anti-Flag?",
        "options": ["A) 21st Century Breakdown", "B) No Pads, No Helmets...Just Balls", "C) Infinity On High", "D) For Blood And Empire"],
        "answer": "D"
    },
    {
        "question": "What is the capital city of Bermuda?",
        "options": ["A) Havana", "B) Santo Dominigo", "C) San Juan", "D) Hamilton"],
        "answer": "D"
    },
    {
        "question": "What is the capital of Scotland?",
        "options": ["A) London", "B) Glasgow", "C) Dundee", "D) Edinburgh"],
        "answer": "D"
    },
    {
        "question": "Who won the 2015 Formula 1 World Championship?",
        "options": ["A) Nico Rosberg", "B) Jenson Button", "C) Lewis Hamilton", "D) Sebastian Vettel"],
        "answer": "C"
    },
    {
        "question": "In \"The Lord of the Rings,\" who is the owner of Asfaloth, the horse which brings Frodo to Rivendell?",
        "options": ["A) Glorfindel", "B) Haldir", "C) Arwen", "D) Aragorn"],
        "answer": "A"
    },
    {
        "question": "If soccer is called football in England, what is American football called in England?",
        "options": ["A) Handball", "B) Touchdown", "C) Combball", "D) American football"],
        "answer": "D"
    },
    {
        "question": "In the Yakuza series who is the Dragon of Dojima?",
        "options": ["A) Haruka Sawamura", "B) Sohei Dojima", "C) Ryuji Goda", "D) Kazuma Kiryu"],
        "answer": "D"
    },
    {
        "question": "Which of these game-based comics were published in 2011 by DC Comics?",
        "options": ["A) Prototype", "B) Kane & Lynch", "C) Infamous", "D) Left 4 Dead: The Sacrifice"],
        "answer": "C"
    },
    {
        "question": "Who is the lead singer of the band Coldplay?",
        "options": ["A) Chris Isaak", "B) Chris Martin", "C) Chris Connelly", "D) Chris Wallace"],
        "answer": "B"
    },
    {
        "question": "What is the name of the AHL affiliate of the Toronto Maple Leafs?",
        "options": ["A) Toronto Rock", "B) Toronto Marlies", "C) Toronto Argonauts", "D) Toronto Wolfpack"],
        "answer": "B"
    },
    {
        "question": "American illustrator and writer Maurice Sendak is most well-known for writing which children's book?",
        "options": ["A) Where The Wild Things Are", "B) The Neverending Story", "C) The Cat in the Hat", "D) Charlie and the Chocolate Factory"],
        "answer": "A"
    },
    {
        "question": "What is Pink Floyd's first album?",
        "options": ["A) Wish You Were Here", "B) The Dark Side of the Moon", "C) The Piper at the Gates of Dawn", "D) Meddle"],
        "answer": "C"
    },
    {
        "question": "Which of these words means \"idle spectator\"?",
        "options": ["A) Meupareunia", "B) Jentacular", "C) Gongoozler", "D) Gossypiboma"],
        "answer": "C"
    },
    {
        "question": "Which iconic Disneyland attraction was closed in 2017 to be remodeled as a \"Guardians of the Galaxy\" themed ride?",
        "options": ["A) Twilight Zone Tower of Terror", "B) Pirates of the Caribbean", "C) The Haunted Mansion", "D) Peter Pan's Flight"],
        "answer": "A"
    },
    {
        "question": "In Shakespeare's play Julius Caesar, Caesar's last words were...",
        "options": ["A) Vidi, vini, vici.", "B) Et tu, Brute? ", "C) Aegri somnia vana.", "D) Iacta alea est!"],
        "answer": "B"
    },
    {
        "question": "Which of the following is considered classical conditioning?",
        "options": ["A) Skinner box experiment", "B) Pavlov's dog experiments", "C) Harlow\u2019s monkey experiments", "D) Schr\u00f6dinger's cat experiment"],
        "answer": "B"
    },
    {
        "question": "Which franchise had a special event hosted in the popular MMORPG Final Fantasy XIV: A Realm Reborn?",
        "options": ["A) Buddyfight", "B) Yu-gi-oh", "C) Pok\u00e9mon", "D) Yo-kai Watch"],
        "answer": "D"
    },
    {
        "question": "What is the standard SI unit for temperature?",
        "options": ["A) Rankine", "B) Celsius", "C) Kelvin", "D) Fahrenheit"],
        "answer": "C"
    }
]

lifelines = {
    "50:50": True,
    "Audience Poll": True,
    "Phone a Friend": True,
    "Flip the Question": True
}

def use_lifeline(q, ans):
    print("\nAvailable Lifelines:")
    lifeline_mapping = {}
    i = 1
    for key, val in lifelines.items():
        if val:
            print(f"{i}. {key}")
            lifeline_mapping[str(i)] = key
            i += 1
            
    if not lifeline_mapping:
        print("No lifelines left.")
        return None
        
    choice = input("Choose a lifeline number or press Enter to skip: ").strip()
    if not choice:
        return None

    if choice in lifeline_mapping:
        selected_lifeline = lifeline_mapping[choice]
        if selected_lifeline == "50:50":
            lifelines["50:50"] = False
            wrong = [opt[0] for opt in q["options"] if opt[0] != ans]
            removed = random.sample(wrong, 2)
            print("\n50:50 Lifeline: Remaining options:")
            for opt in q["options"]:
                if opt[0] not in removed:
                    print(opt)
        
        elif selected_lifeline == "Audience Poll":
            lifelines["Audience Poll"] = False
            print("Audience Poll suggests:", ans)

        elif selected_lifeline == "Phone a Friend":
            lifelines["Phone a Friend"] = False
            print("Your friend thinks the answer is:", ans)

        elif selected_lifeline == "Flip the Question":
            lifelines["Flip the Question"] = False
            print("Question flipped!\n")
            return "flip"
    else:
        print("Invalid lifeline choice.")
    return None


score = 0
prize_money = [0]
questions_asked = 0


while questions_asked < 10:
    if not questions:
        print("No more questions left!")
        break
        
    q = random.choice(questions)
    questions.remove(q)
    
    print(f"\nQuestion {questions_asked + 1}: {q['question']}")
    for opt in q["options"]:
        print(opt)
    
    lifeline_result = use_lifeline(q, q["answer"])
    if lifeline_result == "flip":
        continue  
    print("You have 20 seconds to answer...")
    start_time = time.time()
    
    # Simple input logic
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    
    if time.time() - start_time > 20:
        print("Time's up!")
        break

    if answer == q['answer']:
        score += 1
        if score == 1:
            prize_money.append(1000)
        else:
            prize_money.append(prize_money[-1] * 2)
        print(f"Correct! You won ₹{prize_money[-1]}")
    else:
        print(f"Wrong answer. The correct answer was {q['answer']}. Game over.")
        break
    
    questions_asked += 1

print(f"\nYour total winning amount: ₹{prize_money[-1]}")
print(f"Total Correct Answers: {score}")