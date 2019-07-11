# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        #return base**exponent
        r=1.0
        p=abs(exponent)
        while p:
            if p & 1:
                r*=base
            base*=base
            p>>=1
        return r if exponent >0 else 1/r