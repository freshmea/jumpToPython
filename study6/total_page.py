def get_total_page(m,n):
    if m % n :
        result = m // n
    else :
        result = m//n + 1
    return result

if __name__ == '__main__':
    result = 1