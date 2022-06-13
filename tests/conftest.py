import os
import pytest
from testcontainers.mysql import MySqlContainer
from project.main import app
from fastapi.testclient import TestClient
from tests._tools.database.db_test import DbTest

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="session")
def app_testing():
    with MySqlContainer('mysql:8.0') as mysql_container:
        db_test = DbTest(mysql_container.get_connection_url())
        test_client = TestClient(app)
        yield AppTesting(db_test, test_client)


@pytest.fixture(scope="function")
def sql_cleaner(app_testing):
    yield app_testing.db.truncate_all_tables()


@pytest.fixture(scope="function")
def sql_loader(app_testing):
    yield SqlLoader(app_testing.db)


@pytest.fixture(scope="function")
def _sql_cleaner(app_testing):
    yield
    app_testing.db.truncate_all_tables()


@pytest.fixture(scope="function")
def sql_loader_cl(app_testing, _sql_cleaner):
    yield SqlLoader(app_testing.db)


class SqlLoader:
    def __init__(self, database) -> None:
        super().__init__()
        self.database = database

    def load_file(self, location):
        self.database.execute_file(f"{BASE_DIR}/{location}")


class AppTesting:
    def __init__(self, db: DbTest, client: TestClient) -> None:
        self.db = db
        self.client = client
