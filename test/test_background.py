import pytest
import os

from context import background
from background import Background

def mock_change_background(self, file):
    print('mock_change_background')
    return


@pytest.fixture
def PatchBackground(monkeypatch):
    monkeypatch.setattr(Background, '_change_background',
                        mock_change_background)
    bk = Background()
    return bk

@pytest.mark.parametrize('file, expected', [
    ('', False),
    ('x', False),
    (int, False),
    (float, False),
    ('test\\a.jpg', False),
    (os.path.abspath('fixtures\\image.jpg'), True),
    ('fixtures\\image.jpg', False)
])
def test_check_file_str_path(file, expected, PatchBackground):
    """
    Test is string, absolute path, exists.
    """
    bk = PatchBackground
    result = bk._check_file(file)
    assert result == expected

@pytest.mark.parametrize('file, expected', [
    ('', False),
    ('x', False),
    (int, False),
    (float, False),
    ('test\\a.jpg', False),
    (os.path.abspath('fixtures\\image.jpg'), True),
    ('fixtures\\image.jpg', False)
])
def test_change(PatchBackground, file, expected):
    """
    Show that .change(file) only passes if check file passes
    """
    bk = PatchBackground
    result = bk.change(file)
    assert result == expected
