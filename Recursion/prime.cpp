//Prime numer in cpp
#include<iostream>
using namespace std;

bool prime(int num){
  //Corner cases
  bool var= true;
  if(num == 0 ||num == 1){
    return false;
  }
  else if (num == 2){
    return true;
  }
  else{
    for (int i = 2; i < num/2; i++)  {
    if (num % i == 0){
      var = false;
      break;}
    }
  }
   return var;
}

int main(){
int num ;
  cout<<"Enter a number"<<endl;;
  cin >> num;
bool  var =prime(num);
switch(var){
    case true:
    cout<<"Number is prime"<<endl;
    break;
    default:
    cout<<"Number is not prime"<<endl;
    }
  return 0;
}
