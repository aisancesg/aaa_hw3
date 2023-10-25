from typing import List


class CountVectorizer:
    """
    Преобразует список текстов в терм-документную матрицу
    """

    def __init__(self):
        self.vocabulary = []

    def fit_transform(self, corpus: list) -> List[list]:
        """
        Выясняет, каков список всех встречающихся слов (терминов) в корпусе,
        и возвращает терм-документную матрицу (в виде списка списков)
        """
        for sentence in corpus:
            words = sentence.lower().split()
            for word in words:
                if word not in self.vocabulary:
                    self.vocabulary.append(word)

        count_matrix = []
        for sentence in corpus:
            words = sentence.lower().split()
            count_in_sentence = []
            for termin in self.vocabulary:
                count_in_sentence.append(words.count(termin))
            count_matrix.append(count_in_sentence)
        return count_matrix

    def get_feature_names(self) -> list:
        """
        Возвращает список всех встречающихся слов в корпусе
        """
        return self.vocabulary


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
