import pytest
from mystructures.hashtable.SeparateChainingHashtable import SeparateChainingHashtable

@pytest.fixture
def hashtable():
    return SeparateChainingHashtable(max_length=10)

def test_insert(hashtable):
    node = hashtable.insert("key1", "value1")
    assert hashtable.table[hashtable.hash("key1")].data["key1"] == "value1"

def test_insert_duplicate_key_without_update(hashtable):
    hashtable.insert("key1", "value1")
    with pytest.raises(Exception) as excinfo:
        hashtable.insert("key1", "value2")
    assert "Key key1 already exists in the hashtable" in str(excinfo.value)

def test_insert_duplicate_key_with_update(hashtable):
    hashtable.insert("key1", "value1")
    node = hashtable.insert("key1", "value2", update=True)
    assert hashtable.table[hashtable.hash("key1")].data["key1"] == "value2"

def test_update_nonexistent_key(hashtable):
    with pytest.raises(Exception) as excinfo:
        hashtable.update("key1", "value1")
    assert "Key not found" in str(excinfo.value)

def test_search_existing_key(hashtable):
    hashtable.insert("key1", "value1")
    result = hashtable.search("key1")
    assert result == {"key1": "value1"}

def test_search_nonexistent_key(hashtable):
    with pytest.raises(Exception) as excinfo:
        hashtable.search("key1")
    assert "The key was not found in the hashtable" in str(excinfo.value)

def test_delete_existing_key(hashtable):
    hashtable.insert("key1", "value1")
    result = hashtable.delete("key1")
    assert result == {"key1": "value1"}
    assert hashtable.table[hashtable.hash("key1")] is None

def test_delete_nonexistent_key(hashtable):
    with pytest.raises(Exception) as excinfo:
        hashtable.delete("key1")
    assert "The key was not found in the hashtable" in str(excinfo.value)

def test_repr(hashtable):
    hashtable.insert("key1", "value1")
    assert repr(hashtable) == str(hashtable.table)
