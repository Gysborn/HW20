import pytest
from unittest.mock import MagicMock

from dao.movie import MovieDAO
from service.movie import MovieService

movie_d = {
            "id": 1,
            "title": "bla",
            "description": "description",
            "trailer": "trailer",
            "year": 2000,
            "rating": 17.5,
            "genre_id": 1,
            "director_id": 1,
        }


@pytest.fixture()
def movie_dao():
    movie_init = MovieDAO(None)
    movie_init.get_all = MagicMock(return_value=[{'id': 1, 'name': 'name1'}, {'id': 2, 'name': 'name2'}])
    movie_init.get_one = MagicMock(return_value={'id': 2, 'name': 'name2'})
    movie_init.create = MagicMock(return_value='201')
    movie_init.update = MagicMock(return_value='201')
    movie_init.delete = MagicMock(return_value='deleted')

    return movie_init

class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_movie_get_all(self):
        assert len(self.movie_service.get_all()) == 2
        assert self.movie_service.get_all() == [{'id': 1, 'name': 'name1'}, {'id': 2, 'name': 'name2'}]

    def test_movie_get_one(self):
        assert self.movie_service.get_one(1).get('name') == 'name2'
        assert self.movie_service.get_one(1) == {'id': 2, 'name': 'name2'}

    def test_movie_create(self):
        assert self.movie_service.create(movie_d) == '201'

    def test_movie_update(self):
        assert self.movie_service.update(movie_d) == '201'

    def test_movie_delete(self):
        assert self.movie_service.delete(1) == 'deleted'


        



