from pig_latin import app
from pig_latin.translator import translator
from flask import request

    
@app.route('/', methods=['POST'])
def translate():
    try:
        data = request.data.decode('ascii')
        return translator.translate_paragraph(data)
    except:
        return "Can not translate non-English text", 400
