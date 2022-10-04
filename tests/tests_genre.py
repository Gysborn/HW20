from unittest.mock import MagicMock

import pytest as pytest

from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_init = GenreDAO(None)
    genre_1 = Genre(id=1, name='name1')
    genre_2 = Genre(id=2, name='name2')
    genre_init.get_all = MagicMock(return_value=[genre_1, genre_2])
    genre_init.get_one = MagicMock(return_value=genre_2)
    genre_init.create = MagicMock(return_value="201")
    genre_init.delete = MagicMock(return_value="deleted")
    genre_init.update = MagicMock(return_value="201")
    return genre_init


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_all(self):
        assert len(self.genre_service.get_all()) == 2

    def test_get_one(self):
        assert self.genre_service.get_one(1) is not None
        assert self.genre_service.get_one(1).name == 'name2'

    def test_create(self):
        assert self.genre_service.create(1) == '201'

    def test_update(self):
        assert self.genre_service.update(1) == '201'

    def test_partially_update(self):
        genre_d = {'id': 1, 'name': 'name1'}
        assert self.genre_service.partially_update(genre_d) == '201'

    def test_delete(self):
        assert self.genre_service.delete(1) == 'deleted'