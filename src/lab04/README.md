<h1>Программирование и алгоритмизация (Лабораторные)</h1>

<h2>Лабораторная №4:</h2>

**Задание №1:**
```python
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
```
![exe1!](/images/lab04/terminal.png)![exe1!](/images/lab04/file_input.png)![exe1!](/images/lab04/check.png)
-------------------------------------------
**Задание №2:**
```python
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
```
![exe2!](/images/lab04/terminal2.png)![exe2!](/images/lab04/report.png)
-------------------------------------------