import re
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from project.services.database import get_db, Base
from project.main import app


class DbTest:

    def __init__(self, database_uri) -> None:
        """Creates the engine and the session_factory getting the url from the config file."""
        self.engine = create_engine(database_uri)
        self.override_get_db()
        self.create_db()

    def override_get_db(self):
        testing_session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

        def override():
            try:
                db = testing_session_local()
                yield db
            finally:
                db.close()

        app.dependency_overrides[get_db] = override

    def create_db(self) -> None:
        Base.metadata.create_all(self.engine)

    def truncate_all_tables(self) -> None:
        """Truncate all tables from database."""
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)

    def execute_file(self, path) -> None:
        with open(path, "rt", encoding="utf-8") as fd:
            sql_file = fd.read()

        with self.engine.connect() as con:
            # Each time it finds a semicolon, the lookahead scans the entire remaining string,
            # making sure there's an even number of single-quotes and an even number of double-quotes.
            statements = re.split(""";(?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", sql_file)
            for statement in statements:
                if statement.strip() != "":
                    con.execute(text(statement))

