class MaxSubArray {
    public int maxSubArray(int[] nums) {
        int currentSum = nums[0];
        int maxSum = nums[0];

        for (int i = 1; i < nums.length; i++) {

            if (currentSum + nums[i] > nums[i]) {
                currentSum = currentSum + nums[i];
            } else {
                currentSum = nums[i];
            }

            if (currentSum > maxSum) {
                maxSum = currentSum;
            }
        }

        return maxSum;
    }
    public static void main(String[] args){
        MaxSubArray msa = new MaxSubArray();
        int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
        int result = msa.maxSubArray(nums);
        System.out.println("Maximum Sub Array: "+result);
    }
}
