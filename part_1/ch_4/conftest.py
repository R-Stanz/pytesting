import pytest

@pytest.fixture(scope="session")
def db(tmp_path_factory):
    '''CardsDB connected to a temporary database'''
    db_path = tmp_path_factory.mktemp("cards_db")
    db_ = cards.cardsDB(db_path)
    yield db_
    db_.close()

