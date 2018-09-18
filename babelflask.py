from flask import Flask, render_template
from flask_babel import Babel, gettext as _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
babel = Babel(app)

@app.route('/')
def hello():
    day = _("Saturday")
    return render_template('testbabel.html', day=day)

if __name__ == '__main__':
    app.debug = True
    app.run()