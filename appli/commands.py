import click
from .app import app,db
    
@app.cli.command ()
@click.argument("username")
@click.argument("password")
def newuser(username , password, email):
    '''Adds a new user.'''
    from .models import User
    from hashlib import sha256
    m = sha256()
    m.update(password.encode())
    u = User(pseudoUser=username , mdpUser=m.hexdigest(), emailUser=email)
    db.session.add(u)
    db.session.commit()

@app.cli.command()
@click.argument("username")
@click.argument("password")
def passwd(username, password):
    """Changes the password of a user. """
    from .models import User
    from hashlib import sha256
    m = sha256()
    m.update(password.encode())
    u = User.query.get(username)
    u.mdpUser = m.hexdigest()
    db.session.commit()