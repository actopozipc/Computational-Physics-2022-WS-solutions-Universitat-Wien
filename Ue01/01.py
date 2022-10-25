if __name__ == "__main__":
    n=100;
    print(list(map(lambda x: "FEM-BEM" if (x % 3 == 0 and x%5==0)  else ("FEM" if (x%3==0) else ("BEM" if (x%5==0) else x)), range(n))))
