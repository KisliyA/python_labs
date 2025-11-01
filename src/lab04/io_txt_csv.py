import sys
from collections import Counter

sys.path.append('/Users/alexk/dev/python_labs/src/lab03/src/lib/')
from text import normalize, tokenize

def main():
    with open("data/input.txt", 'r', encoding="utf-8") as f:
        text = f.read()
    
    words = tokenize(normalize(text))
    word_count = Counter(words)
    
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    

    with open("data/report.csv", 'w', encoding='utf-8') as f:
        f.write("word,count\n")
        for word, count in sorted_words:
            f.write(f"{word},{count}\n")
    
    # Вывод статистики
    print(f"Всего слов: {len(words)}")
    print(f"Уникальных слов: {len(word_count)}")
    print("Топ-5:")
    for word, count in sorted_words[:5]:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()