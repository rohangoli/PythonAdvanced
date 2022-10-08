// Subarray with given sum
#include<iostream>
#include<bits/stc++.h>

vector<int> subarraySum(int arr[], int n, long long s)
{
    // Your code here
    int currSum = arr[0], idx=1, begin=0;
    vector<int> result;
    while(idx<=n){
        while(currSum>s && begin<idx-1){
            currSum = currSum-arr[begin];
            begin++;
        }
        
        if(currSum==s){
            result.push_back(begin+1);
            result.push_back(idx);
            return result;
        }
        if(idx<n){
            currSum = currSum + arr[idx];
        }
        idx++;
    }
    result.push_back(-1);
    return result;
};