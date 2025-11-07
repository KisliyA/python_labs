from pathlib import Path
import csv
import sys

sys.path.append('/Users/alexk/dev/python_labs/src/lab03/src/lib/')
from text import normalize, tokenize

def main():
    input_file = "data/input.txt"
    output_file = "data/report.csv"
    
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    normalized_text = normalize(text)
    print(normalized_text)

    words = tokenize(normalized_text)
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    
    # Сохраняем статистику в CSV
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for word, count in sorted_words:
            writer.writerow([word, count])

if __name__ == "__main__":
    main()