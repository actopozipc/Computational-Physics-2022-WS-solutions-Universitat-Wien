if __name__ == "__main__":
    palindromes = [];
    list(map(lambda x: palindromes.extend(map(lambda y: y*x, range(100,999))), range(100,999)))
    print(max(filter(lambda x: str(x)[::-1] == str(x), palindromes)))