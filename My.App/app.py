from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
# Use one consistent folder. 'static/uploads' is best for showing images.
app.config['UPLOAD_FOLDER'] = 'static/uploads'

def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS images (id INTEGER PRIMARY KEY, filename TEXT)')
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Ensure the directory exists
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            conn = sqlite3.connect('database.db')
            conn.execute('INSERT INTO images (filename) VALUES (?)', (file.filename,))
            conn.commit()
            conn.close()
            return redirect('/')
    return render_template('index.html')

@app.route('/files')
def list_files():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT filename FROM images')
    files = cursor.fetchall() 
    conn.close()
    return render_template('list.html', files=files)

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=8080)