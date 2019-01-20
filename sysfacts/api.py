# from __future__ import annotations

import platform

import cpuinfo  # type: ignore
import distro  # type: ignore
import pendulum  # type: ignore
import psutil  # type: ignore


# TODO @##@#$! mypy
def _to_dict(named_tuple) -> dict:
    return dict(named_tuple._asdict())


def get_timestamp() -> str:
    return str(pendulum.now())


def get_os_release() -> dict:
    return distro.os_release_info()


def get_lsb_release() -> dict:
    return distro.lsb_release_info()


def get_distro_release() -> dict:
    return distro.distro_release_info()


def get_uname() -> dict:
    return _to_dict(platform.uname())


def get_cpuinfo() -> dict:
    return cpuinfo.get_cpu_info()


def get_memory_info() -> dict:
    return _to_dict(psutil.virtual_memory())


def get_swap_info() -> dict:
    return _to_dict(psutil.swap_memory())


def get_cpu_usage() -> dict:
    return _to_dict(psutil.cpu_times_percent())


def collect_facts() -> dict:
    """
    Return a dictionary with data collected from various source.

    """
    data: dict = {
        "timestamp": get_timestamp(),
        "os_release": get_os_release(),
        "lsb_release": get_lsb_release(),
        "distro_release": get_distro_release(),
        "uname": get_uname(),
        "cpu_info": get_cpuinfo(),
        "memory_info": get_memory_info(),
        "swap_info": get_swap_info(),
        "cpu_usage": get_cpu_usage(),
    }
    return data


__all__ = ["collect_facts"]
