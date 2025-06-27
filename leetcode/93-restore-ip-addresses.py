class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def getIpParts(s, part, ipaddr, res):
            if part < 0 or len(s) == 0:
                if part < 0 and len(s) == 0:
                    res.append(ipaddr[1:])
                return
            if part == 0 and len(s) > 3:
                return
            if part == 1 and (len(s) > 6 or len(s) < 2):
                return
            if part == 2 and (len(s) > 9 or len(s) < 3):
                return
            if part == 3 and (len(s) > 12 or len(s) < 4):
                return
            getIpParts(s[1:], part-1, ipaddr + '.' + s[0], res)
            if len(s) > 1 and s[0] != '0':
                getIpParts(s[2:], part-1, ipaddr + '.' + s[0:2], res)
            if (len(s)) > 2 and s[0] != '0' and s[0:2] != '00' and int(s[0:3]) <= 255:
                getIpParts(s[3:], part-1, ipaddr + '.' + s[0:3], res)
        res = []
        getIpParts(s, 3, '', res)
        return res
