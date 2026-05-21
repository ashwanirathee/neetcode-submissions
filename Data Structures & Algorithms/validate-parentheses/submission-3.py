class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for idx, i in enumerate(s):
            print(idx, i)
            if i in ['(','[','{']:
                st.append(i)
            else:
                if len(st)>0 and ((i == ')' and st[-1] == '(') or (i == ']' and st[-1] == '[') or (i == '}' and st[-1] == '{')):
                    st.pop()
                else :
                    return False
        if len(st) != 0 : return False
        return True