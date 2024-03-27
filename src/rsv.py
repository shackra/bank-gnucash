﻿# (C) Stefan John / Stenway / Stenway.com / 2023

import json
import os


def encode_rsv(rows: list[list[str | None]]) -> bytes:
    parts: list[bytes] = []
    for row in rows:
        for value in row:
            if value is None:
                parts.append(b"\xFE")
            elif len(value) > 0:
                parts.append(value.encode())
            parts.append(b"\xFF")
        parts.append(b"\xFD")
    return b"".join(parts)


def decode_rsv(bytes: bytes) -> list[list[str | None]]:
    if len(bytes) > 0 and bytes[-1] != 0xFD:
        raise Exception("Incomplete RSV document")
    result: list[list[str | None]] = []
    current_row: list[str | None] = []
    value_start_index = 0
    for i in range(len(bytes)):
        if bytes[i] == 0xFF:
            length = i - value_start_index
            if length == 0:
                current_row.append("")
            elif length == 1 and bytes[value_start_index] == 0xFE:
                current_row.append(None)
            else:
                value_bytes = bytes[value_start_index:i]
                current_row.append(value_bytes.decode())
            value_start_index = i + 1
        elif bytes[i] == 0xFD:
            if i > 0 and value_start_index != i:
                raise Exception("Incomplete RSV row")
            result.append(current_row)
            current_row = []
            value_start_index = i + 1
    return result


# ----------------------------------------------------------------------


def save_rsv(rows: list[list[str | None]], file_path: str):
    with open(file_path, "wb") as file:
        file.write(encode_rsv(rows))


def load_rsv(file_path: str) -> list[list[str | None]]:
    with open(file_path, "rb") as file:
        return decode_rsv(file.read())


def append_rsv(
    rows: list[list[str | None]], file_path: str, continue_last_row: bool = False
):
    try:
        file = open(file_path, "rb+")
    except FileNotFoundError as e:
        file = open(file_path, "bx")
    try:
        file.seek(0, os.SEEK_END)
        if continue_last_row and file.tell() > 0:
            file.seek(-1, os.SEEK_END)
            if file.read(1) != b"\xFD":
                raise Exception("Incomplete RSV document")
            if len(rows) == 0:
                return
            file.seek(-1, os.SEEK_END)
        file.write(encode_rsv(rows))
    finally:
        file.close()


# ----------------------------------------------------------------------


def decode_rsv_using_split(bytes: bytes) -> list[list[str | None]]:
    result: list[list[str | None]] = []
    if len(bytes) > 0:
        if bytes[-1] != 0xFD:
            raise Exception("Incomplete RSV document")
        for row_bytes in bytes[0 : len(bytes) - 1].split(b"\xFD"):
            current_row: list[str | None] = []
            if len(row_bytes) > 0:
                if row_bytes[-1] != 0xFF:
                    raise ValueError("Incomplete RSV row")
                for value_bytes in row_bytes[0 : len(row_bytes) - 1].split(b"\xFF"):
                    if len(value_bytes) == 1 and value_bytes[0] == 0xFE:
                        current_row.append(None)
                    else:
                        current_row.append(value_bytes.decode())
            result.append(current_row)
    return result


def load_rsv_using_split(file_path: str) -> list[list[str | None]]:
    with open(file_path, "rb") as file:
        return decode_rsv_using_split(file.read())


# ----------------------------------------------------------------------


def is_valid_rsv(bytes: bytes):
    byte_class_lookup = [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        0,
        0,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        6,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        8,
        7,
        7,
        9,
        10,
        10,
        10,
        11,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        12,
        13,
        14,
    ]
    state_transition_lookup = [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        0,
        0,
        0,
        3,
        4,
        6,
        5,
        7,
        8,
        9,
        1,
        10,
        11,
        0,
        2,
        0,
        0,
        0,
        3,
        4,
        6,
        5,
        7,
        8,
        9,
        0,
        0,
        11,
        0,
        0,
        2,
        2,
        2,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        3,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        3,
        3,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        3,
        3,
        3,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        6,
        6,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        6,
        6,
        6,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        6,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        11,
        0,
        2,
        0,
        0,
        0,
        3,
        4,
        6,
        5,
        7,
        8,
        9,
        1,
        10,
        11,
    ]
    last_state = 1
    for i in range(len(bytes)):
        current_byte = bytes[i]
        current_byte_class = byte_class_lookup[current_byte]
        new_state_lookup_index = last_state * 15 + current_byte_class
        last_state = state_transition_lookup[new_state_lookup_index]
        if last_state == 0:
            return False
    return last_state == 1


# ----------------------------------------------------------------------


def rsv_to_json(rows: list[list[str | None]]) -> str:
    result = "["
    if len(rows) > 0:
        result += "\n"
    result += ",\n".join(
        [
            "  ["
            + ", ".join(
                [
                    "null" if x is None else json.dumps(x, ensure_ascii=False)
                    for x in row
                ]
            )
            + "]"
            for row in rows
        ]
    )
    result += "\n]"
    return result


# ----------------------------------------------------------------------


def load_file(file_path: str) -> bytes:
    with open(file_path, "rb") as file:
        return file.read()
