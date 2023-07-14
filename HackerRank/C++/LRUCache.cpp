#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
using namespace std;

struct Node{
   Node* next;
   Node* prev;
   int value;
   int key;
   Node(Node* p, Node* n, int k, int val):prev(p),next(n),key(k),value(val){};
   Node(int k, int val):prev(NULL),next(NULL),key(k),value(val){};
};

class Cache{
   
   protected: 
   map<int,Node*> mp; //map the key to the node in the linked list
   int cp;  //capacity
   Node* tail; // double linked list tail pointer
   Node* head; // double linked list head pointer
   virtual void set(int, int) = 0; //set function
   virtual int get(int) = 0; //get function

};

class LRUCache : public Cache {
    private:
        int current_length=0;
    public:
        LRUCache(int cp){
            this->cp=cp;
            tail = NULL;
            head = NULL;
            cout << "Capacity is set to " << cp << endl;
        };
        
        Node* insertNode(Node* temp){
            if(head!=NULL){
                head->prev = temp;
                temp->next = head;
            }
            else if(current_length==0){
                tail=temp;   
            }
            head=temp;
            current_length++;
            return temp;
        }
        
         Node* deleteNode(Node* temp){
             Node* node=temp;
             if(tail==temp){
                tail->prev->next = NULL;
                tail = tail->prev;
             }
             else if(temp && temp->prev && temp->next){
                temp->prev->next = temp->next;
                temp->next->prev = temp->prev;
             }
             current_length--;
             node->prev = NULL;
             node->next = NULL;
             return node;
         }
 
        void printDLL(){
            Node* temp=head;
            cout << "HEAD:" << head << " TAIL:" << tail << endl; 
            cout << "LRU Cache:" << endl;
            while(temp){
                cout << " ["<< temp->prev << "|" << temp->key << ":" << temp->value  << "|" << temp->next << "] <-> ";
                temp = temp->next;
            };
            cout << endl;
        }

        void printHM(map<int, Node*> HM){
            cout << "Hash Map:" << endl;
            for(auto it = HM.begin(); it!=HM.end(); ++it){
                cout << "[" << it->first << "|" << it->second << "]" << endl;
            }  
        }
    
        int get(int key){
            cout << "****************************" << endl;
            cout << "Get " << key << endl;
            printDLL();
            printHM(mp);
            if(mp.find(key)!=mp.end()){
                if(head!=tail && mp[key]!=head){
                    Node* node = deleteNode(mp[key]);
                    cout << " ["<< node->prev << "|" << node->key << ":" << node->value  << "|" << node->next << "] <-> ";
                    // printDLL();
                    // return 0;
                    mp[key] = insertNode(node);
                    cout << "After Node Insertion" << endl;
                    printDLL();
                }               
                return mp[key]->value; 
            }
            else{
                return -1;
            }
            cout << "****************************" << endl;
        };
        
        void set(int key, int value){
            cout << "****************************" << endl;
            printf("Set node[%d:%d]\n",key,value);
            if(current_length>=cp){
                mp.erase(tail->key);
                deleteNode(tail);
            }
            mp[key] = insertNode(new Node(key,value));
            printDLL();
            printHM(mp);
            cout << "****************************" << endl;
        }
};

int main() {
   int n, capacity,i;
   cin >> n >> capacity;
   LRUCache l(capacity);
   for(i=0;i<n;i++) {
      string command;
      cin >> command;
      if(command == "get") {
         int key;
         cin >> key;
         cout << l.get(key) << endl;
      } 
      else if(command == "set") {
         int key, value;
         cin >> key >> value;
         l.set(key,value);
      }
   }
   return 0;
}
