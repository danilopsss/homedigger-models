from unittest.mock import patch
from hdmdata.schemas.advertisements import RentOfficeSchema
from hdmdata.types.get_by_type import by_


@patch("sqlalchemy.create_engine")
@patch("sqlalchemy.orm.session.Session.commit")
def test_rent_office_model_saving(commit, engine, rent_office_data):
    rent_office = RentOfficeSchema(**rent_office_data).save()
    assert commit.called
    assert engine.called
    assert rent_office.title == rent_office_data["title"]


@patch("sqlalchemy.create_engine")
@patch("sqlalchemy.orm.session.Session.execute")
@patch("hdmdata.database._methods.get_by")
def test_rent_office_model_get(where_definer, execute, engine, rent_office_data):
    RentOfficeSchema(**rent_office_data).get()
    assert execute.called
    assert engine.called
    assert where_definer.called


@patch("sqlalchemy.create_engine")
@patch("sqlalchemy.orm.session.Session.execute")
@patch("hdmdata.database._methods.get_by")
def test_rent_office_model_get_by_id(where_definer, execute, engine, rent_office_data):
    id_argument = by_("id", 1)
    name_argument = by_("title", "some title")

    RentOfficeSchema(**rent_office_data).get(by=id_argument)
    assert where_definer.call_args[1]["by"] == id_argument

    RentOfficeSchema(**rent_office_data).get(by=name_argument)
    assert where_definer.call_args[1]["by"] == name_argument

    assert engine.called
    assert execute.called
