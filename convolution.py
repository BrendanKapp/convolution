class Polynomial:
    """
    A class that parses and stores polynomials.
    """
    def __init__(self, f, N):
        self.f = f
        self.N = N
        self.F = [0] * N
        if f != "":
            self.parse(f)

    def parse(self, f):
        """
        Parse a string @f of the format:
        CxM where C is the coefficient
        and M is the power. Store it in
        the @self.F variable.
        Ex:
        f = "3x2 + 2x1 + 1x0"
        """
        f = f.replace("-", "+ -").strip()
        f = f.replace("- ", "-")
        f = f.replace("-x", "-1x")
        terms = f.split("+")
        for term in terms:
            if term.count("x^") != 0:
                c = term.split("x^")[0].strip()
                m = int(term.split("x^")[1].strip())
                if (c == ""):
                    c = 1
                else:
                    c = int(c)
            elif term.count("x") != 0:
                c = term.replace("x", "").strip()
                if (c == ""):
                    c = 1
                else:
                    c = int(c)
                m = 1
            else:
                c = int(term.strip())
                m = 0
            self.F[m] = c
    
    def getc(self, m):
        """
        @return the coefficient of F at power @m
        """
        return self.F[m]

    def setc(self, m, c):
        """
        Sets the coefficient of @m to @c
        """
        self.F[m] = c

    def print(self):
        """
        Print the polynomial
        """
        first = True
        for i in range(self.N - 1, -1, -1):
            if (self.F[i] == 0):
                continue
            if (not first):
                print(" + ", end="")
            first = False
            if (i == 0):
                print(str(self.F[i]), end="")
            elif (i == 1):
                print(str(self.F[i]) + "x", end="")
            else:
                print(str(self.F[i]) + "x^" + str(i), end="")
        print("")


def convolution(f, g, N):
    """
    Print the results of a convolution operation on
    a set of polynomial strings @f * @g of size @N.
    """
    hpoly = Polynomial("", N)
    fpoly = Polynomial(f, N)
    gpoly = Polynomial(g, N)
    print("f(x) =", end="\n\t")
    fpoly.print()
    print("g(x) =", end="\n\t")
    gpoly.print()
    for i in range(0, N - 1):
        val = 0
        for j in range(0, N - 1):
            for k in range(0, N - 1):
                if (j + k % N == i):
                    val += fpoly.getc(j) * gpoly.getc(k) 
        hpoly.setc(i, val)
    print("h(x) =", end="\n\t")
    hpoly.print()



g = input("Enter f(x): ")
f = input("Enter g(x): ")
N = input("Enter N: ")
convolution(f, g, int(N))