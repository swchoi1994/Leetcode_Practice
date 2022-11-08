# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.sum_freq = {}
        self.max_freq = 0
        
        def find_tree_sum(root):
            if not root:
                return 0
            return root.val + find_tree_sum(root.left) +find_tree_sum(root.right)
        
        def pre_order_traversal(root):
            if not root:
                return
            
            curr_sum = find_tree_sum(root)
            self.sum_freq[curr_sum] = self.sum_freq.get(curr_sum, 0) + 1
            self.max_freq = max(self.max_freq, self.sum_freq[curr_sum])
            
            pre_order_traversal(root.left)
            pre_order_traversal(root.right)
        
        pre_order_traversal(root)
        max_freq_sums = []
        for sum in self.sum_freq:
            if self.sum_freq[sum] == self.max_freq:
                max_freq_sums.append(sum)
        
        return max_freq_sums