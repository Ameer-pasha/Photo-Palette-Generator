from flask import Flask, render_template, request
import colorgram
import io

app = Flask(__name__)


app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No file selected"

    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    if not ('.' in file.filename and
            file.filename.rsplit('.', 1)[1].lower() in allowed_extensions):
        return "Invalid file type"

    image_bytes = file.read()
    image_stream = io.BytesIO(image_bytes)

    colors = colorgram.extract(image_stream, 10)

    rgb_colors = []
    for color in colors:
        r, g, b = color.rgb.r, color.rgb.g, color.rgb.b
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        rgb_colors.append(((r, g, b), hex_color))

    return render_template('index.html', colors=rgb_colors)

if __name__ == "__main__":
    app.run()
