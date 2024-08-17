import json
import numpy as np


def generate_word_freq() -> dict:
    freq_map = {}
    with (open("Data/freq.txt") as fp):
        for line in fp.readlines():
            segments = line.split(' ')
            word = segments[0]
            # Use the 5 most recent freq values
            freq = list(map(float, segments[-5:])) if len(segments) > 5 else list(map(float, segments[1:]))
            freq_map[word] = np.mean(freq)

    # Store freq_map data in json_file
    with open("Data/freq_map.json", 'w') as fp:
        json.dump(freq_map, fp)

    return freq_map


# Loads pre-generated freq data
def load_word_freq() -> dict:
    with open("Data/freq_map.json") as fp:
        freq_map = json.load(fp)

    return freq_map


def get_word_freq(regenerate=False) -> dict:

    return generate_word_freq() if regenerate else load_word_freq()


# Returns numpy array of words sorted by increasing freq
def sort_word_freq():
    freq_map = get_word_freq()
    words = np.array(list(freq_map.keys()))
    sorted_freq = np.array(list(freq_map.values())).argsort()
    sorted_words = words[sorted_freq]

    return sorted_words


def sigmoid(x_vals):

    return 1 / (1 + np.exp(-x_vals))


def get_relative_freq(n_common=3000, x_range=10) -> dict:
    sorted_words = sort_word_freq()
    center = x_range * (-0.5 + n_common/len(sorted_words))
    x_vals = np.linspace(center - x_range/2, center + x_range/2, len(sorted_words))
    sigmoid_vals = sigmoid(x_vals)

    return dict(zip(sorted_words, sigmoid_vals))


if __name__ == "__main__":
    print(len(get_relative_freq()))
