class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        i = 0
        j = 1
        k = 2
        l = 3
        n = len(s)
        places = n - 1

        res = []
        for i in range(n-1):
            for j in range(i+1, n-1):
                for k in range(j+1, n-1):
                        print(s[:i+1], s[i+1:j+1], s[j+1:k+1], s[k+1:])
                        a = s[:i+1]
                        b = s[i+1:j+1]
                        c = s[j+1:k+1]
                        d = s[k+1:]
                        if int(a) > 255 or int(b) > 255 or int(c) > 255 or int(d) > 255:
                            continue
                        elif (len(a) > 1 and a[0] == "0"):
                            continue
                        elif (len(b) > 1 and b[0] == "0"):
                            continue
                        elif (len(c) > 1 and c[0] == "0"):
                            continue
                        elif (len(d) > 1 and d[0] == "0"):
                            continue
                        else:
                            res.append(a+"."+b+"."+c+"."+d)
        return res
