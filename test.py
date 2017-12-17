import hashlib
import glob


def create_hash(data):
    m = hashlib.md5(str(data).encode('utf-8'))
    return m.hexdigest()


def crt_prt_hash(h):  # 由子节点生成父节点hash值
    prthash = []
    if len(h) % 2 == 0:  # 如果此层节点时偶数，则一对一对的生成父节点hash值
        for i in range(0, len(h) - 1, 2):
            prthash.append(create_hash(str(h[i] + h[i + 1])))
    else:  # 如果此层节点是奇数，则最后一个节点单独生成hash值
        for i in range(0, len(h) - 2, 2):
            prthash.append(create_hash(str(h[i] + h[i + 1])))
        prthash.append(create_hash(h[-1]))
    return prthash


if __name__ == '__main__':
    txt_fnames = glob.glob('files\\*.txt')
    hashtable = []
    sumhash = " "
    for filename in txt_fnames:
        txt_file = open(filename, 'r')
        buf = txt_file.read()  # 将txt文件存入buf
        hashtable.append(create_hash(buf))  # 根据buf生成hash值
        txt_file.close()
    print(hashtable)  # 输出叶节点的hash值
    t = crt_prt_hash(hashtable)
    while (len(t) != 1):
        print(t)
        t = crt_prt_hash(t)  # 父节点hash表长不为1时，继续迭代生成父hash
    print(t)  # 输出根结点的hash值
