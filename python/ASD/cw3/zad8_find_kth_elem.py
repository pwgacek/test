def find_kth_elem(T,k):
    q = partition(T)

    if q == k - 1:
        return T[q]

    if q > k - 1:
        return find_kth_elem(T[:q],k)

    return find_kth_elem(T[q:],k -q)
