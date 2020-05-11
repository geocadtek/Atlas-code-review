from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command("db", MigrateCommand)

# manager.add_command('runserver', Server(host='localhost', port=app.config['PORT']))
manager.add_command("runserver", Server(host="0.0.0.0", port=app.config["PORT"]))

if __name__ == "__main__":
    manager.run()
