from app.list_directory import list_directory


def test_directory_does_not_exist():
    result = list_directory('/this-directory-does-not-exist')
    assert result['success'] is False

