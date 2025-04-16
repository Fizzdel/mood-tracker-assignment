import random

moods=['happy','sad','calm','anxious']
days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
for day in range(len(days)):
    mood = random.choice(moods)
    print(f"{days[day]} I feel: {mood}")