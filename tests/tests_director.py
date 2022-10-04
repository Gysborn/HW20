from unittest.mock import MagicMock

import pytest as pytest

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_init = DirectorDAO(None)
    director_1 = Director(id=1, name='name1')
    director_2 = Director(id=2, name='name2')
    director_init.get_all = MagicMock(return_value=[director_1, director_2])
    director_init.get_one = MagicMock(return_value=director_2)
    director_init.create = MagicMock(return_value="201")
    director_init.delete = MagicMock(return_value="deleted")
    director_init.update = MagicMock(return_value="201")
    return director_init


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_all(self):
        assert len(self.director_service.get_all()) == 2

    def test_get_one(self):
        assert self.director_service.get_one(1) is not None
        assert self.director_service.get_one(1).name == 'name2'

    def test_create(self):
        assert self.director_service.create(1) == '201'

    def test_update(self):
        assert self.director_service.update(1) == '201'

    def test_delete(self):
        assert self.director_service.delete(1) == 'deleted'