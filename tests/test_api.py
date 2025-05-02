import json
import requests

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200

def test_count(client):
    res = client.get("/count")
    assert res.status_code == 200
    assert res.json['count'] == 20

def test_list_all_songs(client):
    res = client.get("/song")
    assert res.status_code == 200
    assert len(res.json['all songs']) == 20

def test_list_all_songs_check_content_type_equals_json(client):
    res = client.get("/song")
    assert res.headers["Content-Type"] == "application/json"

def test_get_song_by_id(client):
    id = 1
    res = client.get(f'/song/{id}')
    assert res.status_code == 200
    assert res.json['id'] == id
    res = client.get('/song/404')
    assert res.status_code == 404

