"""Given two strings, converting first string to second string.
allowed operations are insert, delete, update and all of the three operations take same cost.
for example converting string1= "sunday" to string2 = "saturday" takes 3 steps, raplacinf 'n' with 'r', insert 't' and insert 'a' """

def edit_distance(str1,str2):
    m = len(str1)
    n = len(str2)
    distanceMatrix = [[0 for i in range(0,n+1)]for i in range(0,m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                distanceMatrix[i][j] = j
            elif j == 0:
                distanceMatrix[i][j] = i
            elif(str1[i-1] == str2[j-1]):
                distanceMatrix[i][j] = distanceMatrix[i-1][j-1]
            else:
                distanceMatrix[i][j] = 1 + min(distanceMatrix[i-1][j-1],distanceMatrix[i][j-1], distanceMatrix[i-1][j])

    return(distanceMatrix[m][n])




if __name__ == '__main__':
    str1 = 'sunday'
    str2 = 'saturday'
    edits = edit_distance(str1, str2)
    print(edits)
