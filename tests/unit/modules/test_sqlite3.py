"""
:codeauthor: Jayesh Kariya <jayeshk@saltstack.com>
"""

import pytest

from saltext.sqlite3.modules import sqlite3


class MockSqlite3:
    """
    Mock sqlite3 class
    """

    version = "2.6.0"
    sqlite_version = "3.8.2"

    def __init__(self):
        self.dbase = None
        self.isolation_level = None

    def connect(self, dbase, isolation_level=None):
        """
        Mock connect method
        """
        self.dbase = dbase
        self.isolation_level = isolation_level
        return MockSqlite3()

    @staticmethod
    def cursor():
        """
        Mock cursor method
        """
        return MockSqlite3()

    @staticmethod
    def execute(sql):
        """
        Mock execute method
        """
        return sql

    @staticmethod
    def fetchall():
        """
        Mock fetchall method
        """
        return True


@pytest.fixture
def configure_loader_modules():
    return {sqlite3: {"sqlite3": MockSqlite3()}}


def test_version():
    """
    Tests if it return version of pysqlite.
    """
    assert sqlite3.version() == "2.6.0"


def test_sqlite_version():
    """
    Tests if it return version of sqlite.
    """
    assert sqlite3.sqlite_version() == "3.8.2"


def test_modify():
    """
    Tests if it issue an SQL query to sqlite3 (with no return data).
    """
    assert not sqlite3.modify()

    assert sqlite3.modify("/root/test.db", "CREATE TABLE test(id INT, testdata TEXT);")


def test_fetch():
    """
    Tests if it retrieve data from an sqlite3 db
    (returns all rows, be careful!)
    """
    assert not sqlite3.fetch()

    assert sqlite3.fetch("/root/test.db", "CREATE TABLE test(id INT, testdata TEXT);")


def test_tables():
    """
    Tests if it show all tables in the database.
    """
    assert not sqlite3.tables()

    assert sqlite3.tables("/root/test.db")


def test_indices():
    """
    Tests if it show all indices in the database.
    """
    assert not sqlite3.indices()

    assert sqlite3.indices("/root/test.db")


def test_indexes():
    """
    Tests if it show all indices in the database,
    for people with poor spelling skills
    """
    assert sqlite3.indexes("/root/test.db")
