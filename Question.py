from datetime import date


class Question:
    """
    Data structure for storing Question of a FragGabiEntry
    """
    title = str()
    content = str()
    author = str()
    word_count = int()

    def set_date(self, date_str):
        """
        Set date from a string in format dd.mm.yyyy
        :param date_str: String containing the year in format dd.mm.yyyy
        """
        splitted = date_str.split('.')
        self.post_date = date(int(splitted[2]), int(splitted[1]), int(splitted[0]))

    def word_count(self):
        """
        Count words of actual question content
        :return: Word count of question
        """
        return len(self.content.split())
