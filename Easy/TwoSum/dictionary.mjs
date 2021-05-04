/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
export default function twoSum(nums, target) {
    let hash = computeHash(nums);

    for (let i = 0; i < nums.length; i++) {
        const value = nums[i];
        const complement = target - value;
        const complementIndex = hash[complement];

        if (complementIndex !== undefined) {
            return [i, complementIndex];
        }
    }

    return [undefined, undefined]
};

function computeHash(nums) {
    let hash = {};

    for (let i = 0; i < nums.length; i++) {
        const value = nums[i];
        hash[value] = i;
    }

    return hash;
}
