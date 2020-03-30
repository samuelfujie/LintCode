# 1534. Convert Binary Search Tree to Sorted Doubly Linked List
[ https://www.lintcode.com/problem/convert-binary-search-tree-to-sorted-doubly-linked-list/description ]

Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

Let's take the following BST as an example, it may help you understand the problem better:

![demo1](https://github.com/samuelfujie/LintCode/blob/master/1534_Convert_Binary_Search_Tree_to_Sorted_Doubly_Linked/demo1.png?raw=true)

We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.

![demo2](https://github.com/samuelfujie/LintCode/blob/master/1534_Convert_Binary_Search_Tree_to_Sorted_Doubly_Linked/demo2.png?raw=true)

Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.

The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

![demo3](https://github.com/samuelfujie/LintCode/blob/master/1534_Convert_Binary_Search_Tree_to_Sorted_Doubly_Linked/demo3.png?raw=true)

## Example
**Example 1:**

Input:
```sh
{4,2,5,1,3}
        4
       /  \
      2   5
     / \
    1   3
```
Output:
```sh
left:1->5->4->3->2  right:1->2->3->4->5
```
Explanation: 
Left: reverse output
Right: positive sequence output

**Example 2:**

Input:
```sh
{2,1,3}
        2
       /  \
      1   3
```
Output:
```sh
left:1->3->2  right:1->2->3
```