import json

import pytest

import sysfacts


@pytest.fixture(scope="module")
def collected_data():
    return sysfacts.collect_facts()


def test_imports():
    from sysfacts import collect_facts


def test_return_type(collected_data):
    assert isinstance(collected_data, dict)


def test_keys_are_present(collected_data):
    keys = {
        "timestamp",
        "os_release",
        "lsb_release",
        "distro_release",
        "uname",
        "cpu_info",
        "memory_info",
        "swap_info",
        "cpu_usage",
    }
    collected_keys = collected_data.keys()
    assert keys == set(collected_keys), keys.symmetric_difference(collected_keys)


def test_is_json_serializable(collected_data):
    out = json.dumps(collected_data)
    assert isinstance(out, str)
