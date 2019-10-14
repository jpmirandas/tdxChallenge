class Problem2:

    def answer(self, words):
        """
            Write Code To Sort The List Of Strings
            - (for example inputList = { "January", "February", "Mar", "Apr", "May", "June", "Jul","august", "Sep",
            "Oct", "nov", "December" }
            - java? python? c#? indifferent for me after all
            - nice to have it in alphabetical order for all, in alphabetical order consider capital and non capital
            letters, or any other order that candidate can think about

        """
        if words is not [""]:

            result = []
            for word in words:
                # collect the ascii value of the first letter from given words
                result.append((ord(word[0].lower()), word))

            # sort the words list based on the first letter ascii code
            sorted_tuples = sorted(result, key=lambda tup: tup[0])

            # return a list with sorted strings
            return list(map(lambda tup: tup[1], sorted_tuples))

        else:
            return [""]
