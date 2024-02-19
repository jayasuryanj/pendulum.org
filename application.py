from flask import Flask, render_template, send_from_directory, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resourse')
def resourse():
    return render_template('resourse.html')
@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/static/images/<filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)


if __name__ == '__main__':
    app.run(debug=True)