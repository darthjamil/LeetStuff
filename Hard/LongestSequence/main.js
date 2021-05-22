/*
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

0 <= nums.length <= 104
-109 <= nums[i] <= 109

Follow up: Could you implement the O(n) solution?
*/
function getLongestSequence(arr) {
    const sorted = [...arr].sort((a, b) => a - b)
    let longestSequenceLength = 1
    let currentSequenceLength = 1

    for (let i = 1; i < sorted.length; i++) {
        let previousElement = sorted[i - 1]
        let currentElement = sorted[i]
        currentSequenceLength++

        if (currentElement != previousElement + 1) {
            currentSequenceLength = 1
        }

        if (currentSequenceLength > longestSequenceLength) {
            longestSequenceLength = currentSequenceLength
        }
    }

    return longestSequenceLength
}

function getLongestSequence_LinearTime(nums) {
    const largestAbsoluteVal = 109
    const bloomFilter = []

    for (item of nums) {
        const index = item + largestAbsoluteVal
        bloomFilter[index] = 1
    }

    let longestSequenceLength = 0
    let currentSequenceLength = 0

    for (let i = 0; i < bloomFilter.length; i++) {
        if (bloomFilter[i] !== 1) {
            currentSequenceLength = 0
        } else {
            currentSequenceLength++

            if (currentSequenceLength > longestSequenceLength) {
                longestSequenceLength = currentSequenceLength
            }
        }
    }

    return longestSequenceLength
}

const arr = [100,4,200,1,3,2]
const longestSequenceLength = getLongestSequence_LinearTime(arr)

console.log(longestSequenceLength)
