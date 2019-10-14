class Problem1:

    def answer(self, word):
        """
            Write A Program To Find The Longest Substring
            From A Given String Which Doesnt Contain Any Duplicate Characters.

        """

        if word:
            word = word.lower()
            longest_substrings = []

            for pos, letter in enumerate(word):
                longest_substring = ""
                next_pos = pos

                # while all the string is not completely read and there is repeated letter
                while next_pos <= len(word) - 1 and word[next_pos] not in longest_substring:
                    longest_substring += word[next_pos]
                    next_pos += 1
                longest_substrings.append(longest_substring)

            # return the value of maximal string size
            max_length = max(len(item) for item in longest_substrings)

            # return all substrings with maximal size
            return list(set(item for item in longest_substrings if len(item) == max_length))

        else:
            return []
