def restore_documents(originals, backups):
    # 1  map(lambda x: x.upper()   map(lambda x: x.upper(), backups)
    # 2  list(filter(lambda x: not x.isdigit(), originals.upper()))
    # 3  set(a + b)
    return set(
        list(filter(lambda x: not x.isdigit(), map(lambda x: x.upper(), originals)))
        + list(filter(lambda x: not x.isdigit(), map(lambda x: x.upper(), backups)))
    )


"""
zip(a, b) pairs elements by position: [("A", "B"), ("C", "D")]

a + b concatenates two lists: ["A", "B", "C", "D"]

set(a + b) removes duplicates from the concatenated list.
"""
