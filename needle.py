def buildDirectionalString(matrix, N, M) :
    """ Build the directional string based on the N x M matrix """
    dstring = ""
    currentrow = N
    currentcol = M
    while currentrow != 0 or currentcol != 0 :
        if currentrow == 0 :
            dstring = dstring + 'H'
            currentcol -= 1
        elif currentcol == 0 :
            dstring = dstring + 'V'
            currentrow -= 1
        elif matrix[currentrow][currentcol-1] + gap == matrix[currentrow][currentcol] :
            dstring += 'H'
            currentcol -= 1
        elif matrix[currentrow-1][currentcol] + gap == matrix[currentrow][currentcol] :
            dstring += 'V'
            currentrow -= 1
        else :
            dstring = dstring + 'D'
            currentcol -= 1
            currentrow -= 1
    return dstring
            
            
            
infile1 = open("sequence1.txt", "r")
infile2 = open("sequence2.txt", "r")

firstline1 = infile1.readline()
firstline2 = infile2.readline()
print firstline1
print firstline2

s1 = ""
for line in infile1 :
    line = line.replace("\n", "")
    s1 = s1 + line 
s1 = s1.upper()
print "s1 = ", s1

s2 = ""
for line in infile2 :
    line = line.replace("\n", "")
    s2 = s2 + line 
s2 = s2.upper()
print "s2 = ", s2

# N = length of s1
N = len(s1)
print "N = ", N
M = len(s2)
print "M = ", M
# M = length of s2

# matrix = array of size [N+1, M+1], filled with zero's
matrix = [[0 for i in range(M + 1)] for j in range(N + 1) ]
for row in matrix :
    print row
# gap = gap score, let's say -1
gap = -1

# mismatch = mismatch score, say 0
mismatch = 0 

# match = match score, say 1
match = 1


for i in range(1, N+1) :
    matrix[i][0] = matrix[i-1][0] + gap


for j in range(1, M+1) :
    matrix[0][j] = matrix[0][j-1] + gap
print "-------------------------------------"
for row in matrix :
    print row
print "-------------------------------------"



for i in range(1, N+1) :
    for j in range(1, M+1) :
        if s1[i-1] == s2[j-1] :
            score1 = matrix[i-1][j-1] + match
        else :
            score1 = matrix[i-1][j-1] + mismatch
        score2 = matrix[i][j-1] + gap
        score3 = matrix[i-1][j] + gap
        matrix[i][j] = max(score1, score2, score3)

print "Matrix"
for row in matrix :
    for element in row :
        print " {:>3} ".format(element),
    print ''
print "-------------------------------------"



dstring = buildDirectionalString(matrix, N, M)

print "Directional String: " + dstring


seq1pos= N-1 
seq2pos= M-1 
dirpos = 0
alignment1 = ''
alignment2 = ''
matchline = ''
matchcount = 0

while dirpos < len(dstring) :
    if dstring[dirpos] == "D" :
        alignment1 = s1[seq1pos] + alignment1 
        alignment2 = s2[seq2pos] + alignment2
        if s1[seq1pos] == s2[seq2pos] :
            matchline = '|' + matchline
            matchcount = matchcount + 1
        else :
            matchline = '.' + matchline
        seq1pos -= 1
        seq2pos -= 1
    elif dstring[dirpos] == "V" :
        alignment1 = s1[seq1pos] + alignment1 
        alignment2 = '-' + alignment2
        seq1pos -= 1
        matchline = ' ' + matchline
    else : # it must be an "H"
        alignment1 = '-' + alignment1
        alignment2 = s2[seq2pos] + alignment2
        seq2pos -= 1
        matchline = ' ' + matchline
    dirpos += 1

print alignment1
print matchline
print alignment2

