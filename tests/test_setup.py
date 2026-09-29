import json

def test_json_roundtrip(tmp_path):
    data = {"message": "I was charged twice", "label": "billing"}
    file = tmp_path / "example.json"
    file.write_text(json.dumps(data))
    loaded = json.loads(file.read_text())
    assert loaded == data