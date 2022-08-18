from flask import Flask, render_template
from api import api_bp
from models import get_all, init_db, insert

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app.register_blueprint(api_bp)

@app.route('/',defaults={'path':''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__=='__main__':
    with app.app_context():
        init_db(app)
        if not get_all():
            insert('noriko', '2022-8-22', '2022-8-25', '結婚しました')
            insert('noriko', '2023-2-22', '2023-2-25', '離婚しました')
        app.run()