from pig_latin import app
from pig_latin.translator import translator
from flask import request


def has_alphanumeric(s):
    for c in s:
        if (c.isalnum()):
            return True
    return False


@app.route('/', methods=['POST'])
def translate():
    data = ""
    try:
        data = request.data.decode('ascii')
    except:
        return "Can not translate non-English text", 400
    if (not has_alphanumeric(data)):
        return "Request has to contain at least one word", 400
    return translator.translate_paragraph(data)
