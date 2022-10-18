# import multiprocessing
def fembem(n):
    s = n;
    for i in range(n):
        if(n % 3 == 0):
            s = "FEM";
            if(n%5==0):
                s = "FEM-BEM"
        elif(n%5 == 0):
            s = "BEM";

    print(s);
    return None;

if __name__ == "__main__":
    # pool_obj = multiprocessing.Pool();
    # pool_obj.map(fembem, range(1,100));
    fembem(100);