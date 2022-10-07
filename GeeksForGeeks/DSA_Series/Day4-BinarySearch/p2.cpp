#include<iostream>
#include<bits/stdc++.h>

using namespace std;
class Solution:
    public:
    int binarySearch(int arr[], int low, int high, int x){
        while (low <= high){
            int mid = (low + high) / 2;
             
            if (arr[mid] == x)
                return mid;
            else if (arr[mid] > x)
                high = mid - 1;
            else   
                low = mid + 1;   
        }
    };
    string isKSortedArray(int arr[], int n, int k)
    {
        //code here.
        int temp[n];
        for(int i=0; i<n;i++){
            temp[i]=arr[i];
        }
        
        sort(temp,temp+n);
        int j;
        for (int i = 0; i<n; i++){
            j = binarySearch(temp, 0, n-1, arr[i]);
            // cout << j << endl;
            if(abs(i-j)>k){
                return "No";
            }
        }
        return "Yes";
    };