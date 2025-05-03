import json
import requests
import pytest

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

def test_song_json_is_not_empty(client):
    res = client.get("/song")
    assert len(res.json) > 0

def test_post_a_song(client, song):
    res = client.post("/song", json=song)
    assert res.status_code == 201
    assert "inserted id" in res.json

    res = client.post("/song", json=song)
    assert res.status_code == 302
    assert f"Song with id {song['id']} already exists" in res.json["message"]

def test_update_a_song_by_id(client, song):
    id = song["id"]
    res = client.get(f'/song/{id}')
    assert res.status_code == 200
    assert res.json['id'] == id

    updated_song = song.copy()
    updated_song["title"] = "This is a test"

    res = client.put(f'/song/{id}', data=json.dumps(updated_song),
                     content_type="application/json")
    assert res.status_code == 201

    res = client.get(f'/song/{id}')
    assert res.status_code == 200
    assert res.json['title'] == updated_song["title"]
    
def test_delete_a_song_by_id(client, song):
    res = client.get("/song/1")
    assert res.status_code == 200
    song_id = res.json["id"]

    res = client.delete(f"/song/{song_id}")
    assert res.status_code == 204

    res = client.delete("/song/404")
    assert res.status_code == 404

