def word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def charecter_count(book_text):
    # lower_text = book_text.lower()
    # count = {i: lower_text.count(i) for i in lower_text}
    count = {}
    for i in book_text:
        lower_text = i.lower()
        if lower_text in count:
            count[lower_text] += 1
        else:
            count[lower_text] = 1
    return count

# Reporting funcation
def report_char_num(num_char):
    final_report = []
    for letter, count in num_char.items():
        if letter.isalpha():
            final_report.append({"char": letter, "num": count})

    def sort_on(final_report):
        return final_report["num"]
    
    final_report.sort(reverse=True, key=sort_on)
    return final_report
        



    
