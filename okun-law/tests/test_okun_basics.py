import os

def test_readme_and_writeup_exist():
    assert os.path.exists('okun-law/README.md')
    assert os.path.exists('okun-law/writeup_okun.md')

def test_data_mapping_table_present():
    txt = open('okun-law/README.md', encoding='utf-8').read().lower()
    assert 'data column mapping' in txt
