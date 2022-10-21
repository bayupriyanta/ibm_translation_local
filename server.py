from flask import Flask
from machinetranslation.transcription import english_to_french
from machinetranslation.transcription import french_to_english
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/englishToFrench', methods=['GET'])
def translate_eng_fr():
	content = request.get_json(silent=True)
	englsih_text = content['englsih_text']
	text_france = english_to_french(englsih_text)
	json_return = {"english":englsih_text,"french":text_france}
	return jsonify(json_return)

@app.route('/frenchToEnglish', methods=['GET'])
def translate_eng_fr():
	content = request.get_json(silent=True)
	french_text = content['french_text']
	text_english = french_to_english(french_text)
	json_return = {"english":text_english,"french":french_text}
	return jsonify(json_return)
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()