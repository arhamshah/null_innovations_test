def extract_text_file(path):
    with open(path, 'r') as f:
        return f.readlines()


def capital_words(lines):
    return [line.capitalize() for line in lines]


def count_word_occurrences(lines):
    count = dict()
    summary = list()
    for line in lines:
        words = line.split()
        for word in words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
    for key in count:
        summary.append(f'{key} -> {count[key]}\n')
    return summary


def write_text_file(path, lines):
    with open(path, 'w') as f:
        for line in lines:
            f.write(line)
