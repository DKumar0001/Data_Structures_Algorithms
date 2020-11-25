#include <bits/stdc++.h>
#include <string>
using namespace std;

// Complete the repeatedString function below.
long repeatedString(string s, long n) {
    long count =0;
    int s_size = s.length();
    if (long (s.length()) > n){
        for (int i =0; i < n; i++){
            if(s[i] == 'a'){
                count++;
            }
        }
    }
    else{
        for (int i = 0; i < s_size; i++){
            if (s[i] == 'a'){
                count++;
            }
        }
        long repeats = n / s.length();
        count = count * repeats;
        int rem = n % s.length();
        for (int i = 0; i < rem; i++){
            if (s[i] =='a'){
                count++;
            }
        }
        }
    return count;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    long n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    long result = repeatedString(s, n);

    fout << result << "\n";

    fout.close();

    return 0;
}
