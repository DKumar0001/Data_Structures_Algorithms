
#include <iostream>
using namespace std;
int main() {
    int arr[] = {2,3,4,5,2,3};
    int n = sizeof(arr)/sizeof(arr[0]);
    int sum = 0;
    int first = 0;
    int second =0;
    for (int i = 0; i < n; i++){
      sum = sum ^ arr[i];
    }
    sum = sum & - sum;
    
    for (int i = 0; i<n; i++){
      if((sum & arr[i]) > 0){
        first = first ^ arr[i];
      }
      else{
        second = second ^arr[i];
      }
    }
    cout <<"First non repeating element is: "<<first<<endl;
    cout<<"Second non repeating element is:"<<second<<endl;
    return 0;
}
