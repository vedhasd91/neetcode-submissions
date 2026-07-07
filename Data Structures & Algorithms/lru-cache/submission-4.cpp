class Node{
public:
    int val;
    int key;

    Node* next;
    Node* prev;

    Node(int key, int val): key(key), val(val), next(nullptr), prev(nullptr){}

};

class LRUCache {
private:
    int cap;
    std::unordered_map<int, Node*> cache;
    Node* left;
    Node* right;

public:
    LRUCache(int capacity){
        cap = capacity;
        cache.clear();
        left = new Node(0,0);
        right = new Node(0, 0);

        left->next = right;
        right->prev = left;
        
    }
    
    void remove(Node* node){
        auto prev = node->prev;
        auto next = node->next;

        prev->next = next;
        next->prev = prev;

    }

    void add(Node* node){
        auto prev = right->prev;

        node->next = right;
        node->prev = prev;

        right->prev = node;
        prev->next = node;

    }

    int get(int key) {
        if(cache.contains(key)){
            auto node = cache[key];
            remove(node);
            add(node);
            return node->val;
        }
        return -1;
        
    }
    
    void put(int key, int value) {
        if(cache.contains(key)){
            //update
            auto node = cache[key];
            remove(node);

        }

        Node* new_node = new Node(key, value);
        cache[key] = new_node;
        add(new_node);

        if(cache.size()>cap){
            //evict
            auto lru = left->next;
            remove(lru);
            cache.erase(lru->key);
            delete lru;
        }

        
    }
};
