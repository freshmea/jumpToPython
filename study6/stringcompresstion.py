def compresstion_str(data):
    temp_c = ''
    cnt = 0
    out = ''
    for c in data:
        if temp_c == c:
            cnt += 1
        else:
            if temp_c == '':
                temp_c = c
                cnt = 1
            else:
                out += temp_c + str(cnt)
                cnt = 1
                temp_c = c
    out += temp_c + str(cnt)
    return out

if __name__ == '__main__':
    print(compresstion_str('aaabbccddddeeefffffffffffff'))
    print(compresstion_str('afff bccdd          ffffff'))
    print(compresstion_str('aaabbccddddeeefffffffggggf'))
    print(compresstion_str('**********************'))
    print(compresstion_str('*&&&'))