from flaskr import create_app
from .modelos import db, Cancion, Album, Usuario, Medio

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#prueba
with app.app_context():
    c = Cancion(titulo='Prueba-Cancion', minutos=2, segundos=25, interprete='Luis Solier')
    a = Album(titulo='Prueba-Album', ano=1992, descripcion='descripcion', medio=Medio.CASETE.name)
    u = Usuario(nombre_usuario='Prueba-Usuario', contrasena='contrasena')
    c2 = Cancion(titulo='Prueba2', minutos=2, segundos=25, interprete='Luis Solier')
    db.session.add(c)
    db.session.add(a)
    db.session.add(u)
    db.session.add(c2)
    db.session.commit()
    print(Cancion.query.all())
    print(Album.query.all())
    print(Usuario.query.all())