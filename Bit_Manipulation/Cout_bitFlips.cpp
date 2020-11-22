// Counting Number of flips needed to convert A to B

# include<iostream>
using namespace std;

int bit_manipulation(int A, int B){

  int c =A^B;
  int cont =0;

  while (c!=0){
      c &= c-1;
      count +=1;
  }
  return count

}

int main() {
  int A,B;
  std::cout << "Enter two numbers" << '\n';
  cin>>A;
  cin>>B;
  flips = bit_manipulation(A,B);
  cout<< "The number of flips needed are"<<"flips";

  return 0;
}
