from flask import Flask, render_template, request


import openai

openai.api_key = "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"

def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_text', methods=['POST'])
def generate_text_route():
    prompt = request.form['prompt']
    text = generate_text(prompt)
    return render_template('generate_text.html', prompt=prompt, text=text)

if __name__ == '__main__':
    app.run(debug=True)
