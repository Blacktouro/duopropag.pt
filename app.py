from flask import Flask, render_template
from datetime import datetime
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.secret_key = 'segredo_super_secreto'  # necessário se usares sessão

# Configurações de cookie seguras (HTTPS e proxy via Nginx)
app.config['SESSION_COOKIE_SECURE'] = True  # só envia cookies via HTTPS
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# Corrige headers quando a app está atrás de proxy (Nginx)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Injeção de ano atual para usar nos templates
@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

# Rotas principais
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route('/logos')
def logos():
    return render_template('logos.html')

@app.route('/tv')
def tv():
    return render_template('tv.html')

@app.route('/redes')
def redes():
    return render_template('redes.html')

@app.route('/empresas')
def empresas():
    return render_template('empresas.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6500, debug=True, use_reloader=True)

