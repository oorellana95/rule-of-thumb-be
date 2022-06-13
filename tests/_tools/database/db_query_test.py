from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def literal_query(query):
    import sqlalchemy.orm
    statement = query.statement
    if isinstance(statement, sqlalchemy.orm.Query):
        statement = statement.statement
    return statement.compile(
        compile_kwargs={'literal_binds': True}
    ).string


class DbQueryTest:

    def __init__(self) -> None:
        """Creates the engine and the session_factory getting the url from the config file."""
        self.engine = create_engine('sqlite:///:memory:')
        self.session = Session(bind=self.engine)
