def indexOf(s, characters):
    for index, c in enumerate(s):
        if (c in characters):
            return index
    return -1


def translate_word(s):
    if (len(s) == 0):
        return ""
    lower_case_vowels = ["a", "e", "i", "o", "u", "y"]
    upper_case_vowels = [e.upper() for e in lower_case_vowels]
    vowels = lower_case_vowels + upper_case_vowels
    index_of_first_vowel = indexOf(s, vowels)
    if (index_of_first_vowel == -1):
        return s

    if (index_of_first_vowel == 0):
        return s + "yay"

    prefix = s[:index_of_first_vowel]
    suffix = s[index_of_first_vowel:]
    return suffix + prefix + "ay"


def translate_paragraph(paragraph):
    # We expect the paragraph to be ascii only, error handling is
    # handled from the caller of this function
    current_word = ""
    result = ""
    paragraph += " "
    for c in paragraph:
        if (not c.isalnum()):
            translated_word = translate_word(current_word)
            result += translated_word
            result += c
            current_word = ""
        else:
            current_word += c
    return result[:-1]
