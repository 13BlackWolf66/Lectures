def task1():
    numbers = [4, -9, 8, -11, 8]
    negative_count = len(list(filter(lambda x: x < 0, numbers)))
    print(negative_count)

def task2():
    players = ['Ashleigh Barty', 'Simona Halep', 'Naomi Osaka', 'Karolina Pliskova', 'Elina Svitolina']
    players[0], players[-1] = players[-1], players[0]
    print(players)

def task3():
    quote = "The reasonable man adapts himself to the world; the unreasonable one persists in trying to adapt the world to himself."
    words = quote.split()
    idx_reasonable = words.index("reasonable")
    idx_unreasonable = words.index("unreasonable")
    words[idx_reasonable], words[idx_unreasonable] = words[idx_unreasonable], words[idx_reasonable]
    modified_quote = " ".join(words)
    print(modified_quote)

task1()
task2()
task3()