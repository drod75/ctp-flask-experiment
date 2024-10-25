from flask import Flask, render_template

app = Flask(__name__ ,static_folder='static')

@app.route('/')
@app.route('/classify')
def classify():
    return render_template('classify.html')

@app.route('/metrics')
def metrics():
    return render_template('metrics.html', title='Metrics')

if __name__ == '__main__':
    app.run()