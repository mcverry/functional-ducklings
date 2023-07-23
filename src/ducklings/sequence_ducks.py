def get_2_from_list(seq: list):
    return [
        (seq[i - 1] if i > 0 else None, seq[i + 1] if i < len(seq) - 1 else None)
        for i in range(len(seq))
    ]
