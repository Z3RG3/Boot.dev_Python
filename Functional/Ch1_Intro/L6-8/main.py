def get_median_font_size(font_sizes):
    if font_sizes == []:
        return None
    sorted_sizes = sorted(font_sizes)
    n = len(sorted_sizes)
    mid = n // 2
    if n % 2 == 0 and sorted_sizes[mid - 1] < sorted_sizes[mid]:
        return sorted_sizes[mid - 1]
    else:
        return sorted_sizes[mid]
