class Matrix():
    def __init__(self, matrix):
        #check square
        if all (len (row) == len (matrix[0]) for row in matrix):
            #convert rows to matrix row class (for row operations)
            self.matrix = []
            for row in matrix:
                self.matrix.append(MatrixRow(row=row))
        else:
            raise Exception("Matrix must be square!")

    #matrix accessing
    #get MatrixRow
    def __getitem__(self, index: int) -> list:
        return self.matrix[index-1]

    #set matrix row
    def __setitem__(self, index, value):
        if value == None: return
        if not (isinstance(value, list) or isinstance(value, MatrixRow)): raise Exception("Value must be either list or MatrixRow object")
        
        width, height = self.shape()
        if not len(value) == width: raise Exception("Row must be same width as matrix!")

        if isinstance(value, list):
            self.matrix[index-1] = MatrixRow(row=value)
        else:
            self.matrix[index-1] = value

    #addition
    def __add__(self, other):
        if self.shape() == other.shape():
            return Matrix(matrix=[[self.matrix[i][j] + other.matrix[i][j]  for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])
        else:
            raise Exception("Matrix's must have same shape for addition!")

    #subtraction
    def __sub__(self, other):
        if self.shape() == other.shape():
            return Matrix(matrix=[[self.matrix[i][j] - other.matrix[i][j]  for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])
        else:
            raise Exception("Matrix's must have same shape for subtraction!")

    #dot product
    def __mul__(self, other):
        #if other is an integer or float
        if isinstance(other, int) or isinstance(other, float):
            return Matrix(matrix=[[other * elem for elem in row] for row in self.matrix])
        #if its a matrix multiply by matrix
        elif isinstance(other,Matrix):
            if len(self.matrix[0]) == len(other.matrix):
                return Matrix(matrix=[[sum(i * j for i, j in zip(r, c)) for c in zip(*other.matrix)] for r in self.matrix])
            else:
                raise Exception("Matrix A's columns must be equal to matrix B's rows!")

    #scalar multiplication
    def __rmul__(self, other):
        return Matrix(matrix=[[other * elem for elem in row] for row in self.matrix])

    #printing
    def __str__(self):
        result = ""
        for count, row in enumerate(self.matrix):
            if count == len(self.matrix)-1:
                result += str(row)
            else:
                result += str(row) + "\n"
        return result

    #total matrix elements
    def __len__(self):
        return len(self.matrix) * len(self.matrix[0])

    #width and height
    def shape(self):
        return (len(self.matrix[0]), len(self.matrix))

    #transpose - convert NxM to MxN
    def transpose(self):
        self.matrix = [[row[i] for row in self.matrix] for i in range(len(self.matrix))]

    #swap 2 matrix rows
    def swap(self, row1:int, row2:int):
        row1 -= 1
        row2 -= 1
        self.matrix[row1], self.matrix[row2] = self.matrix[row2], self.matrix[row1]

    #generate an identity matrix
    @staticmethod
    def identityMatrix(size):
        return Matrix(matrix=[[1 if i == j else 0 for j in range(size)] for i in range(size)])

class MatrixRow():
    def __init__(self, row):
        self.row = row

    def __str__(self):
        return str(self.row)

    def __len__(self):
        return len(self.row)

    def __getitem__(self, index):
        return self.row[index-1]

    #row operations

    #row addition
    def __add__(self, other):
        #must be either list or MatrixRow object
        if not (isinstance(other, list) or isinstance(other, MatrixRow)): raise Exception("Other must be either list or MatrixRow object")
        
        #must be same length
        if not len(self.row) == len(other): raise Exception("Rows must be equal length!")

        self.row = [self.row[x] + other[x] for x in range(len(self.row))]

    #row multiplication
    def __mul__(self, other):
        #if other is an integer or float
        if isinstance(other, int) or isinstance(other, float) and other != 0:
            self.row = [x*other for x in self.row]
        else:
            raise Exception("Other must be a non zero integer or float")

    def __rmul__(self, other):
        self.__mul__(other)