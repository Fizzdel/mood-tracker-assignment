import random

moods=['happy','sad','calm','anxious']
days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
times=['morning','afternoon','night']

for day in range(len(days)):
    for time in times:
        mood = random.choice(moods)
        print(f"{days[day]} {time} I feel {mood}")