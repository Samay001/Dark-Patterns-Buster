from flask import Flask, request, jsonify
from utils import create_pipeline
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
pipe = create_pipeline(
    pretrained="bert-base-uncased",
    path_to_trained_model=os.path.join(basedir, "pytorch_models/bert_trained/pytorch_model.bin")
)


@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        data = request.get_json().get('tokens')
        pred = pipe(data)
        return pred


if __name__ == '__main__':
    app.run(threaded=True, debug=True)

