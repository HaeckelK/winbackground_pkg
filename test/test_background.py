import pytest
import os

from context import background
from background import Background

def mock_change_background(self, file):
    print('mock_change_background')
    return

#monkeypatch.setattr(PoliceAPI, "_get_response", mock_response_404)

@pytest.fixture
def bg(monkeypatch):
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
def test_check_file_str_path(file, expected):
    """
    Test is string, absolute path, exists.
    """
    bk = Background()
    result = bk._check_file(file)
    assert result == expected


def test_temp(bg):
    """
    """
    bk = bg
    file = os.path.abspath('fixtures\\image.jpg')
    result = bk.change(file)
    assert result == True
