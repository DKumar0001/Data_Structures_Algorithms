#include<iostream>
using namespace std;


int main()
{
  int num;
  cout<<"Enter a number";
  cin>>num;
  int fib_series[num+2];
  fib_series[0] = 0;
  fib_series[1] = 1;
  for (int i = 2;i<num+2; i++)
  {
  fib_series[i] = fib_series[i-1]+fib_series[i-2];
  }
  for(int i = 0; i<num+2; i++){
      cout<<"element"<<fib_series[i]<<endl;
  }
  cout<<fib_series;
return 0;
}
