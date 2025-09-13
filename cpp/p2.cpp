#include <iostream>
#include <map>



class LRUCache {

public:
class ListNode {
public:
    ListNode(){
        next_ = this;
        prev_ = this;
    }

    ListNode(int k, int v):k_(k), v_(v){
        next_ = this;
        prev_ = this;
    }

    class ListNode* next_=nullptr;
    class ListNode* prev_=nullptr;
    int v_;
    int k_;

public:
    void insertHead(class ListNode* node){
        node->next_ = this->next_;
        node->prev_ = this;
        this->next_->prev_ = node;
        this->next_ = node;
    }
    ListNode* removeTail(){
        if(this->next_!=this){
            ListNode* tail = this->prev_;
            tail->prev_->next_ = tail->next_;
            tail->next_->prev_ = tail->prev_;
            return tail;
        }
        return this;
    }
    void moveToHead(class ListNode* node){
        class ListNode* prev=node->prev_;
        class ListNode* next=node->next_;
        prev->next_ = next;
        next->prev_ = prev;

        node->next_ = this->next_;
        node->prev_ = this->prev_;
        this->next_->prev_ = node;
        this->next_ = node;
    }

};

public:
    LRUCache(int capacity) {
        cap_ = capacity;
        curCap_ = 0;
        listHead_ = new ListNode();
    }
    
    int get(int key) {
        if(map_.find(key)!=map_.end()){
            listHead_->moveToHead(map_[key]);
            return map_[key]->v_;
        }else{
            return -1;
        }
    }
    
    void put(int key, int value) {
        if(map_.find(key)!=map_.end()){
            listHead_->moveToHead(map_[key]);
            map_[key]->v_=value;
        } else {
            ListNode *node = new ListNode(key,value);
            if(curCap_<cap_){
                listHead_->insertHead(node);
                map_.insert({key,node});
                curCap_++;
            } else {
                // del last
                ListNode *removeNode = listHead_->removeTail();
                map_.erase(removeNode->k_);
                delete removeNode;
                // insert head
                listHead_->insertHead(node);
                map_.insert({key,node});
            }
        }
    }
    void print(){
        for (auto it: map_){
            std::cout<<"["<<it.first<<","<<it.second->v_<<"] ";
        }
        std::cout<<std::endl;
    }
private:
    int cap_;
    int curCap_ = 0;
    std::map<int,ListNode*> map_;
    ListNode *listHead_;

};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

int main(int, char**){
    std::cout << "Hello, from leetcode!\n";
    LRUCache solu{2};
    solu.put(1,1);  solu.print();
    solu.put(2,2);  solu.print();
    solu.get(1);    solu.print();
    solu.put(3,3);  solu.print();
    solu.get(2);    solu.print();
    solu.put(4,4);  solu.print();
    solu.get(1);    solu.print();
    solu.get(3);    solu.print();
    solu.get(4);    solu.print();
}
