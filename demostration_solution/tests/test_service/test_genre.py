from unittest.mock import MagicMock
import pytest

from demostration_solution.dao.genre import GenreDAO
from demostration_solution.dao.model.genre import Genre
from demostration_solution.service.genre import GenreService
from demostration_solution.setup_db import db


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)

    jonh_evan = Genre(id=1, name='jonh_evan')
    kate_mody = Genre(id=2, name='kate_mody')
    max_harden = Genre(id=3, name='max_harden')

    genre_dao.get_one = MagicMock(return_value=jonh_evan)
    genre_dao.get_all = MagicMock(return_value=[jonh_evan, kate_mody, max_harden])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()
    return genre_dao

class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre != None
        assert genre.id != None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_d = {

            "name": "Comedy",
        }
        genre = self.genre_service.create(genre_d)
        assert genre.id != None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        genre_d = {
            "id": 3,
            "name": "Comedy"
        }
        self.genre_service.update(genre_d)