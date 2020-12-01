/*Given two strings, converting first string to second string.
allowed operations are insert, delete, update and all of the three operations take same cost.
for example converting string1= "sunday" to string2 = "saturday" takes 3 steps, raplacinf 'n' with 'r', insert 't' and insert 'a'*/

#include<iostream>
#include<string>
#include <vector>
using namespace std;

//finding minium of three given values
int min(int x, int y, int z) { return min(min(x, y), z); }

// Defining number of operations needed
int edit_distance(string str1, string str2){

int n = str1.size();
int m = str2.size();
cout<<n<<m<<endl;
int distanceMatrix[n+1][m+1];

for (int i = 0; i<=n; i++){
  for (int j = 0; j<=m; j++){
    if(i ==0){
      distanceMatrix[i][j] = j;
    }
    else if(j==0){
    distanceMatrix[i][j] = i;
    }
    else if(str1[i-1] == str2[j-1]){
      distanceMatrix[i][j] = distanceMatrix[i-1][j-1];
    }
    else{
      distanceMatrix[i][j] = 1 + min(distanceMatrix[i-1][j-1], distanceMatrix[i][j-1], distanceMatrix[i-1][j]);
    }
  }
}

return distanceMatrix[n][m];
}

//main Function
int main(){

  string str1 = "sunday";
  string str2 ="saturday";
  int editDisance = edit_distance(str1, str2);
  cout<< editDisance <<endl;
  return 0;
}
