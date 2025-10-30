<h1>Программирование и алгоритмизация (Лабораторные)</h1>

<h2>Лабораторная №3:</h2>

**Задание №1:**
```python
import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")

    while "  " in text:
        text = text.replace("  ", " ")

    return text.strip()

def tokenize(text: str) -> list[str]:
    pattern = r'\b\w+(?:-\w+)*\b'
    return re.findall(pattern, text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    counts = {}
    for i in tokens:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    freqSorted = sorted(freq.items(), key=lambda item: [-item[1], item[0]])
    return freqSorted[:n]


```
![exe1!](/images/lab03/image.png)
-------------------------------------------
**Задание №2:**
```python
from lib import text
from sys import stdin

# считываем все строки из stdin
lines = []
# Python 3.7 and newer
stdin.reconfigure(encoding='utf-8')
for line in stdin:
    lines.append(line)

# получаем весь текст
all_text = "".join(lines)
# нормализируем
normalized_text = text.normalize(all_text)
# считаем токены
all_normalized_tokens = text.tokenize(normalized_text)
# словарь уникальных
freqs = text.count_freq(all_normalized_tokens)
# находим топ-5
top5 = text.top_n(freqs, 5)

print(f"Всего слов: {len(all_normalized_tokens)}")
print(f"Уникальных слов: {len(freqs)}")
print("Топ-5:")
for key, value in top5:
    print(f"{key}:{value}")



```
![exe2!](/images/lab03/task2.png)


-------------------------------------------

-------------------------------------------
