from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
        <body>
            <h1>Pershendetje!</h1>
            <p>Ju lutem lejoni qasje në të dhënat e pajisjes tuaj.</p>
            <form action="/upload" method="post" enctype="multipart/form-data">
                <input type="file" name="file" accept="image/*, video/*">
                <input type="submit" value="Ngarko">
            </form>
        </body>
    </html>
    '''

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    # Këtu mund të bëni diçka me skedarin, si ta dërgoni te pronari i ueb sajtit.

    return "Skedari u ngarkua me sukses!"

if __name__ == '__main__':
    app.run()

