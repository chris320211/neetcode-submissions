class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    // array of heights, heights [i]
    // area = (i1 - i2) * (lower one of height)
    // need to check each area so keep updating two pointer
    maxArea(heights) {
        let area = 0
        for (let i = 0; i < heights.length; i++) {
            for (let j = i + 1; j < heights.length; j++) {
                // so say i stays on 0
                // lets check which one is less
                // j index always more so width is j - i
                let width = j - i
                let temp = Math.min(heights[i], heights[j]) * width
                if (area < temp) {
                    area = temp
                }
                
                
            }
        }
        return area
    }
}
