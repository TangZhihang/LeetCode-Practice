def KMP_algorithm(string, substring):
    '''
    KMP�ַ���ƥ���������
    �������ִ������ִ����ַ����п�ʼ��λ���±꣬���߷���-1
    '''
    pnext = gen_pnext(substring)
    n = len(string)
    m = len(substring)
    i, j = 0, 0
    while (i < n) and (j < m):
        if (string[i] == substring[j]):
            i += 1
            j += 1
        elif (j != 0):
            j = pnext[j - 1]
        else:
            i += 1
    if (j == m):
        return i - j
    else:
        return -1


def gen_pnext(substring):
    """
    ������ʱ����pnext
    """
    index, m = 0, len(substring)
    pnext = [0] * m
    i = 1
    while i < m:
        if (substring[i] == substring[index]):
            pnext[i] = index + 1
            index += 1
            i += 1
        elif (index != 0):
            index = pnext[index - 1]
        else:
            pnext[i] = 0
            i += 1
    return pnext


if __name__ == "__main__":
    string = 'abcxabcdabcdabcy'
    substring = 'abcdabcy'
    out = KMP_algorithm(string, substring)
    print(out)

'''
ģʽ����ABCABEABCABD
�Ӵ�	ABCABD
KMP�㷨�ľ�����Ҫ���ڼ���ƥ���
ͨ�����Ӵ�ǰnλ�ֱ����ƥ��ֵ
��������Ӧ��ǰ׺���ͺ�׺�����ȵĳ���
����
ABCABD
A 	    ��ǰ׺���޺�׺��ƥ��ֵ0
AB 	    ǰ׺{A}����׺{B}ƥ��ֵ0
ABC	    ǰ׺{A��AB}��׺{BC��B}ƥ��ֵ0
ABCA	ǰ׺{A��AB��ABC}��׺{BCA��CA��A}ƥ��ֵ1
ABCAB	ǰ׺{A��AB��ABC��ABCA}��׺{BCAB��CAB��AB��B}ƥ��ֵ2
ABCABD	ǰ׺{A��AB��ABC��ABCAB}��׺{BCABD��CABD��ABD��BD��D}ƥ��ֵ0
���ƥ���Ϊ[0,0,1,2,0]
'''