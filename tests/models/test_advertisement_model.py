from unittest.mock import patch
from hdmdata.schemas.advertisements import RentOfficeSchema


@patch("sqlalchemy.create_engine")
@patch("sqlalchemy.orm.session.Session.commit")
def test_rent_office_model_saving(commit, engine, rent_office_data):
    rent_office = RentOfficeSchema(**rent_office_data).save()
    assert commit.called
    assert engine.called
    assert rent_office.title == rent_office_data["title"]
