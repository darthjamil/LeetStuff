import java.util.LinkedList;
import java.util.Queue;

/*
https://leetcode.com/problems/deepest-leaves-sum/
Given the root of a binary tree, return the sum of values of its deepest leaves.

Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
*/
public class DeepestLeavesSum {
    public static void main(String[] args) {
        Integer[] input = new Integer[] {1,2,3,4,5,null,6,7,null,null,null,null,8};
        
        Tree tree = new Tree(input);
        int sum = tree.getDeepestSum();

        System.out.println(sum);
    }

    private static class Tree {
        private TreeNode<Integer> root;

        public Tree(Integer[] input) {
            // TODO build the tree
        }

        public int getDeepestSum() {
            int maxDepth = populateDepthsAndGetMaxDepth();
            int sumAtMaxDepth = getValueSumAtMaxDepth(maxDepth);

            return sumAtMaxDepth;
        }

        private int populateDepthsAndGetMaxDepth() {
            Queue<TreeNode<Integer>> queue = new LinkedList<>();
            int maxDepth = 1;

            root.depth = 1;
            queue.offer(root);

            while (!queue.isEmpty()) {
                TreeNode<Integer> node = queue.poll();

                if (node.left == null && node.right == null) {
                    continue;
                }

                int newDepth = node.depth + 1;

                if (newDepth > maxDepth) {
                    maxDepth = newDepth;
                }

                if (node.left != null) { 
                    node.left.depth = newDepth;
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    node.right.depth = newDepth;
                    queue.offer(node.right);
                }
            }

            return maxDepth;
        }

        private int getValueSumAtMaxDepth(int maxDepth) {
            Queue<TreeNode<Integer>> queue = new LinkedList<>();
            int sum = 0;

            queue.offer(root);

            while (!queue.isEmpty()) {
                TreeNode<Integer> node = queue.poll();
                
                if (node.depth == maxDepth) {
                    sum += node.value;
                }

                if (node.left != null) { 
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }

            return sum;
        }
    }

    private static class TreeNode<T> {
        public T value;
        public TreeNode<T> left;
        public TreeNode<T> right;
        public int depth;

        public TreeNode(T value) {
            this.value = value;
        }
    }
}
