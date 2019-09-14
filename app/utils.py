from typing import List


def divide_notes(note_list: List, batch: int):
    """
    Divide notes in batches of `batch`

    :param note_list: List of notes
    :param batch: Batch size (default: 30)
    """
    counter: int = 0
    chunk_size: int = 0
    while counter < len(note_list):
        chunk_size = _divide(note_list[counter:], batch)
        yield note_list[counter:counter + chunk_size]
        counter += chunk_size


def _divide(note_list: List, batch: int) -> int:
    """
    Finds optimal number of notes in a single batch

    :param note_list: Subset of all notes for a batch
    :param batch: Batch size (default: 30)
    """
    fret_length: float = batch
    chunk_size: int = 0

    for _, _, fret in note_list:
        if fret % 10 == fret:
            fret_length -= 1
            chunk_size += 1
        else:
            fret_length -= 1.2
            chunk_size += 1
        if fret_length <= 0:
            break

    return chunk_size
