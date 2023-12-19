#include <iostream>
#include <algorithm>
using namespace std;

class Node {
public:
    char name[16];
    Node* next[16];

    Node(char input[]) {
        for (int i = 0; i < 16; i++)
        {
            this->name[i] = NULL;
        }

        for (int i = 0; i < 16; i++)
        {
            if (input[i] == NULL) break;
            this->name[i] = input[i];
        }

        for (int i = 0; i < 15; i++)
        {
            this->next[i] = NULL;
        }
    }

    void printName() {
        for (int i = 0; i < 16; i++)
        {
            if (this->name[i] == NULL) break;

            cout << name[i];
        }
    }
};

short compareString(char str1[], char str2[]) {
    short res = 1;
    
    for (int i = 0; i < 16; i++)
    {
        if (str1[i] == NULL && str2[i] == NULL) return 1;

        if (str1[i] == NULL) return 0;
        if (str2[i] == NULL) return 0;

        if (str1[i] != str2[i]) {
            return 0;
        }
    }

    return res;
}

short compareOrder(char str1[], char str2[]) {
    short res = 0;

    for (int i = 0; i < 16; i++)
    {
        if (str1[i] == NULL) return -1;
        if (str2[i] == NULL) return 1;

        if (int(str1[i]) == int(str2[i])) continue;
        
        if (int(str1[i]) > int(str2[i])) {
            return 1;
        } else {
            return -1;
        }
    }

    return res;
}

void sortNodes(Node* arr[]) {
    int arrSize = 0;

    for (int i = 0; i < 1001; i++)
    {
        if (arr[i] == NULL) break;
        arrSize++;
    }

    for (int i = 0; i < arrSize - 1; i++)
    {
        for (int j = i + 1; j < arrSize; j++)
        {
            if (compareOrder(arr[i]->name, arr[j]->name) == 1) {
                Node* temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

void printNode(Node* node, int depth) {
    for (int i = 0; i < depth; i++)
    {
        cout << "--";
    }
    
    node->printName();
    cout << "\n";


    for (int i = 0; i < 16; i++)
    {
        if (node->next[i] == NULL) break;

        sortNodes(node->next);
        printNode(node->next[i], depth + 1);
    }
}

char name[16];
Node* cave[1001];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    
    int N, K;
    cin >> N;

    int caveSize = 0;

    for (int i = 0; i < N; i++)
    {
        cin >> K;
        cin >> name;
        Node* now_node = NULL;

        short is_exist = 0;

        for (int j = 0; j < caveSize; j++)
        {
            if (compareString(cave[j]->name, name) == 1) {
                now_node = cave[j];
                is_exist = 1;
                break;
            };
        }

        if (is_exist == 0) {
            Node* node = new Node(name);
            cave[caveSize++] = node;
            now_node = node;
        };

        for (int j = 1; j < K; j++)
        {
            cin >> name;
            is_exist = 0;
            

            for (int k = 0; k < 16; k++)
            {
                if (now_node->next[k] == NULL) {
                    Node* node = new Node(name);
                    now_node->next[k] = node;
                    now_node = node;
                    break;
                };

                if (compareString(now_node->next[k]->name, name) == 1) {
                    now_node = now_node->next[k];
                    is_exist = 1;
                    break;
                }
            }
        }
    }

    sortNodes(cave);

    for (int i = 0; i < caveSize; i++)
    {
        printNode(cave[i], 0);
    }

    return 0;
}
