package tutorials.concurrency.ForkJoinPool;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class TreeNode {
  int value;
  Set<TreeNode> children;

  TreeNode(int value, TreeNode... nodes) {
    this.value = value;
    this.children = new HashSet<TreeNode>(Arrays.asList(nodes));
  }
}
