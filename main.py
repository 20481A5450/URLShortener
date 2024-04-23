from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Define variables to pass to the template
    title = "My Flask Application"
    content = "Welcome to my Flask application!"

    # Render the template with variables
    return render_template('landing_page.html', title=title, content=content)

if __name__ == '__main__':
    app.run(debug=True)
