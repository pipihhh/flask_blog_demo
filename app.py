from demo import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


if __name__ == '__main__':
    app = create_app()
    manager = Manager(app)
    Migrate(app, db)
    manager.add_command("db", MigrateCommand)
    manager.run()
