// Count Triplets with sum smaller than X

#include<iostream>
#include<bits/stdc++.h>
using namespace std;

long long countTriplets(long long arr[], int n, long long sum)
{
    // Your code goes here
    sort(arr,arr+n);
    int result=0, i=0, j,k;
    while(i<n-2){
        j=i+1;
        k=n-1;
        while(j<k){
            if((arr[i]+arr[j]+arr[k])>=sum){
                k--;
            }
            else{
                result = result + (k-j);
                j++;
            }
        }
        i++;
    }
    return result;
    
}