import os, sys

def test_files_exist():
    assert os.path.exists('unemployment-forecast/README.md')
    assert os.path.exists('unemployment-forecast/writeup_forecast.md')

def test_conformal_import():
    sys.path.append(os.path.join('unemployment-forecast','src'))
    import conformal
    assert hasattr(conformal, 'split_conformal_intervals')
