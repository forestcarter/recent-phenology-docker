from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api import create_app
from api.models import db
import os
# sets up the app
app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

# adds the python manage.py db init, db migrate, db upgrade commands
manager.add_command("db", MigrateCommand)
env = os.environ.get("FLASK_ENV", "docker")
if env == "prod":
    port_number = 80
    in_debug = False
else:
    port_number = 5000
    in_debug = True


@manager.command
def runserver():
    app.run(debug=in_debug, host="0.0.0.0", port=port_number)


@manager.command
def runworker():
    app.run(debug=False)


@manager.command
def recreate_db():
    """
    Recreates a database. This should only be used once
    when there's a new database instance. This shouldn't be
    used when you migrate your database.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    manager.run()
