def genSeq(st, s):
    
    if(len(s) == 0):
        return
    
    if s not in st:
        st.add(s)
        
        for i in range(len(s)):
            t = list(s).copy()
            t.remove(s[i])
            t = ''.join(t)
            genSeq(st, t)
    
    return

if __name__ == "__main__":
    
    x = "xyz"
    st = set()
    genSeq(st, x)
    
    print(st)