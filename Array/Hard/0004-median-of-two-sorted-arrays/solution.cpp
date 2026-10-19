// 4. Median of Two Sorted Arrays
// https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int size = nums1.size();
        size += nums2.size();
        if ((size % 2) == 0) {
            int pt1=0,pt2=0;
            int mid = size/2;
            double count=0,sum=0;
            while(pt1<nums1.size() && pt2<nums2.size()){
              if(count == mid-1 || count == mid){
                 if(nums1[pt1]<nums2[pt2]){
                    sum+=nums1[pt1];
                    pt1++;
                    count++;
                 }
                 else{
                    sum+=nums2[pt2];
                    pt2++;
                    count++;
                 }
              }
              else{
                if(nums1[pt1]<nums2[pt2]){
                    pt1++;
                    count++;
                }
                 else{
                    pt2++;
                    count++;
                 }
              }
            }
            while(pt1<nums1.size()){
                if(count == mid-1 || count == mid){
                    sum+=nums1[pt1];
                    pt1++;
                    count++;
                }
                else{
                    pt1++;
                    count++;
                }
            }
            while(pt2<nums2.size()){
                if(count == mid-1 || count == mid){
                    sum+=nums2[pt2];
                    pt2++;
                    count++;
                }
                else{
                    pt2++;
                    count++;
                }
            }
            return sum/2;
        }
        else{
            int pt1=0,pt2=0;
            double count=0,sum=0;
            int mid = size/2;
            while(pt1<nums1.size() && pt2<nums2.size()){
              if( count == mid){
                 if(nums1[pt1]<nums2[pt2]){
                    sum+=nums1[pt1];
                    pt1++;
                    count++;
                 }
                 else{
                    sum+=nums2[pt2];
                    pt2++;
                    count++;
                 }
              }
              else{
                if(nums1[pt1]<nums2[pt2]){
                    pt1++;
                    count++;
                 }
                 else{
                    pt2++;
                    count++;
                 }
              }
            }
            while(pt1<nums1.size()){
                if( count == mid){
                    sum+=nums1[pt1];
                    pt1++;
                    count++;
                }
                else{
                    pt1++;
                    count++;
                }
            }
            while(pt2<nums2.size()){
                if( count == mid){
                    sum+=nums2[pt2];
                    pt2++;
                    count++;
                }
                else{
                    pt2++;
                    count++;
                }
            }
            return sum;
        }
    }
};
