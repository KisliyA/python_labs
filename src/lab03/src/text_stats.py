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



    