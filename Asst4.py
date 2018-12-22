import sys


def longest_common_subsequence(string1, string2):
    rows = len(string1) + 1
    cols = len(string2) + 1
    position = [[0 for x in range(cols)] for y in range(rows)]
    path = [[(0, 0) for x in range(cols)] for y in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            if string1[i - 1] == string2[j - 1]:
                position[i][j] = position[i - 1][j - 1] + 1
                path[i][j] = (i - 1, j - 1)
            else:
                if position[i - 1][j] >= position[i][j - 1]:
                    position[i][j] = position[i - 1][j]
                    path[i][j] = (i - 1, j)
                else:
                    position[i][j] = position[i][j - 1]
                    path[i][j] = (i, j - 1)

    length = position[rows - 1][cols - 1]
    string = []
    row = rows - 1
    col = cols - 1

    while row > 0 or col > 0:
        prev_row, prev_col = path[row][col]
        if position[row][col] != position[prev_row][prev_col]:
            string[k] +=
        row = prev_row
        col = prev_col
    string = string[::-1]
    return length, string


char Sequence[length];
	i = m-1;
	j = n-1;
	k = 0;
	while( i >= 0 && j >= 0){def main():
		if(X[i] == Y[j]){    string1 = "ABCBDAB"
			Sequence[k++] = X[i];    string2 = "BDCABA"
			i--; j--;    length, string = longest_common_subsequence(string1, string2)
		}    print(
		else if (C[i-1,j] > C[i,j-1])        "The longest common subsequence of " + string1 + " and " + string2 + " is: " + string + "  ,and its length is: " + str(
			i--;            length))
		else
			j--;
	}main()