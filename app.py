from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='assets')

# Route untuk melayani file statis dari folder 'assets'
@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('assets', filename)

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk halaman tour
@app.route('/tour/<page>')
def tour(page):
    return render_template('tour.html', page=page)

if __name__ == '__main__':
    app.run(debug=True)
