import operator


class Problem3:

    def answer(self, list_1, list_2):
        """
            Given two sets of numbers,

            set 1 = [3,5,768,3,6,23,98,38,32,45,34,234]
            set 2 = [10,12,43,74,25,56,37,98,29,10]

            get the most frequent digit, even if it is part of a number and how many times it repeats (two values)
            those will be the positions in the second list, sum values from those positions in second list

            (43 + 37 = ?)

        """

        # convert the int list into string list
        list_1_str = list(map(str, list_1))
        # create a dict with each number and its initial frequency (1)
        frequency = dict(zip(list_1, [1] * len(list_1)))

        for pos1, number in enumerate(list_1_str):
            for pos2 in range(pos1+1, len(list_1_str)):

                # verify if the number is part of a number
                is_substring = number in list_1_str[pos2]
                # verify if the actual number was already validated
                is_not_repeated = number not in list_1_str[:pos1]

                if is_substring and is_not_repeated:
                    frequency[int(number)] += 1

        # return the number with the maximal frequency
        positions = max(frequency.items(), key=operator.itemgetter(1))

        # access the second list elements based on the most frequent number
        # number
        value_from_first_position = list_2[positions[0] - 1]
        # frequency
        value_from_second_position = list_2[positions[1] - 1]

        # return the sum of two elements from list 2, based on the most frequent number
        return value_from_first_position + value_from_second_position
