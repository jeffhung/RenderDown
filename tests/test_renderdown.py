import sys
import renderdown

def test_renderdown(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv',
        ['renderdown', '--assign', 'var1=abc', 'tests/input.mako']
    )
    renderdown.main()
    captured = capsys.readouterr()
    assert 'abc' in captured.out

