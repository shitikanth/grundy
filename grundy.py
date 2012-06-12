def mex(s):
    l=sorted(s)
    i=0
    while(l and (i==l.pop(0))):
        i+=1
    return i

def main():
    print(mex({1,3,4,0}))

if __name__=="__main__":
    main()
