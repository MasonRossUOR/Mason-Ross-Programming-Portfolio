#include <iostream>
#include <stdio.h>
#include <chrono>
using namespace std;
using namespace std::chrono;
using namespace std;

int GCFI(int intA, int intB){ //this code is iterative
    int result = min(intA, intB); // Find Minimum of intA and intB
    while (result > 0){
        if ((intA % result == 0) && (intB % result == 0)){ //if a%result AND b%result are both 0, exit
            break;
        }
        result = result - 1;
    }
    return result; // return gcd of intA and intB
}

int GCFR(int intA,int intB){
    if (intB != 0){//similar to the iterative "if intB%result==0"
       return GCFR(intB, intA % intB); //treating intA%intB as the new intB, and the current intB as the new intA
    }
    else{
       return intA;
    }
}

int main(){
    int numPair1[100000] = {};
    int numPair2[100000] = {};
    int i;

    for(int x=0;x<100000;x++){
        numPair1[x],numPair2[x] = rand();
    }

    auto start = high_resolution_clock::now();//start clock
    for(i=0;i<100000;i++){
        GCFI(numPair1[i],numPair2[i]);//work function
    }
    auto stop = high_resolution_clock::now();
    auto IterativeDuration = duration_cast<microseconds>(stop - start);//end and find duration
    cout << "Time taken by iterative function: " << IterativeDuration.count() << " microseconds\n";

    auto start2 = high_resolution_clock::now(); //start clock
    for(i=0;i<100000;i++){
        GCFR(numPair1[i],numPair2[i]);//work function
    }
    auto stop2 = high_resolution_clock::now(); //end and find duration
    auto RecursiveDuration = duration_cast<microseconds>(stop2 - start2);
 
    cout <<"Time taken by recursive function: " << RecursiveDuration.count()<<" microseconds\n";
    
    return 0;
}