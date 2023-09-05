/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node *ret = NULL, *ret_tail = NULL;
        Node *current = head;
        unordered_map<Node*, Node*> map;

        while (current) {
            Node *new_node = new Node(current->val);
            map[current] = new_node;
            if (ret_tail) {
                ret_tail->next = new_node;
                ret_tail = new_node;
            } else {
                ret = new_node;
                ret_tail = new_node;
            }
            current = current->next;
        }

        /* build random */
        current = head;
        while (current) {
            Node *ret_current = map[current];
            Node *random_node = map[current->random];
            ret_current->random = random_node;
            current = current->next;
        }

        return ret;
    }
};