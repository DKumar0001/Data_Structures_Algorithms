// Check if the given number is power of 2 or 0

#include<iostream>
using namespace std;

int Check_Power2(int num)
{
  //If number is zero
  if (num == 0){
    return 0;
  }
  //If number is power of 2
  else if ((num & num-1)==0){
    return 1;

  }
  // If number is Neither Power of 2 or 0
 else{
 return 2;
 }
}

int main(){
    int num;
    cout <<"Enter a number";
    cin >>num;
    int what = Check_Power2(num);
    switch (what){
        case 0:
        cout<<"The Number is Zero";
        break;

        case 1:
        cout<<"The Number is multiple of 2";
        break;

        default:
        cout<<"The Number is Neither Multiple of 2 nor 0";

    }
}
