/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var lRotate = function(nums, k) {
  for(let i=0; i < k; i++) {
     let temp = nums[0];
     for(var j=0; j<nums.length-1; j++){
       nums[j] = nums[j+1];
     }
    
    nums[j] = temp;
  }
};

var RRotate = function(nums, k) {
  for(let i=0; i < k; i++) {
     let temp = nums[nums.length-1];
     for(var j=nums.length-1; j>0; j--){
       nums[j] = nums[j-1];
     }
    
    nums[j] = temp;
  }
};