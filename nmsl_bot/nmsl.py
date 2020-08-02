import json
import jieba
import pinyin
from os import path


def text_to_emoji(text):
    def get_emoji(word):
        if emoji := bible.get(word):
            return emoji

        py = pinyin.get(word, format="strip")
        if emoji := bible_py.get(py):
            if emoji == "宁":
                print(word, py, bible_py.get(py))
            return emoji

        if len(word) == 1:
            return word

        return "".join([get_emoji(char) for char in word])

    text_split = jieba.lcut(text, cut_all=False)
    return "".join([get_emoji(word) for word in text_split])


jieba.add_word("爱了")
with open(path.join(path.dirname(__file__), 'bible.json')) as f:
    bible: dict = json.load(f)
bible_py: dict = {}
for word, emoji in bible.items():
    key = pinyin.get(word, format="strip") if word not in range(11) else word
    bible_py[key] = emoji

if __name__ == '__main__':
    print(text_to_emoji('我质疑你妈死了，我是抽象大师，这就是二次元吗，爱了爱了。'))
