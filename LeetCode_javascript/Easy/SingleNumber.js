/*
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
*/

/*
So we use reduce() method which is used to reduce the array to a single value and executes a provided function
for each value of the array.In this example we check every single value with XOR operator so duplicates will be removed
at the end of iteration
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    return nums.reduce((prev, curr) => prev ^ curr);
};