
def print_loading_bar(current, len_bar=16, max=100000):
    i = int((current / max) * len_bar)
    bar = "\u2593" * i + "\u2591" * (len_bar - i)
    print(bar + " " + str(current) + " of " + str(max), end="\r")