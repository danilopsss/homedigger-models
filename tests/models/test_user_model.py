from unittest.mock import patch
from hdmdata.schemas.users.users_schema import UserSchema


@patch("sqlalchemy.create_engine")
@patch("sqlalchemy.orm.session.Session.commit")
def test_user_model_saving(commit, engine, user_data):
    user = UserSchema(**user_data).save()
    assert commit.called
    assert engine.called
    assert user.username == user_data["username"]