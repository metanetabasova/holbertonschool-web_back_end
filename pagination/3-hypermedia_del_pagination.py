from typing import Dict, List


def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
    """
    Return a page of data that is resilient to deletions.
    """

    dataset = self.indexed_dataset()

    assert index is not None
    assert 0 <= index < max(dataset.keys()) + 1

    data = []
    current_index = index

    while len(data) < page_size and current_index <= max(dataset.keys()):
        if current_index in dataset:
            data.append(dataset[current_index])

        current_index += 1

    return {
        "index": index,
        "data": data,
        "page_size": len(data),
        "next_index": current_index
    }
