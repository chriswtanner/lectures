def plus(a, b):
    a = 2 * a
    b = 3 + b
    c = a + b
    return c

def main():
  a = 3
  b = 5
  c = plus(a, b)
  c += 1
  print(a)
  print(b)
  print(c)

if __name__ == "__main__":
    main()
