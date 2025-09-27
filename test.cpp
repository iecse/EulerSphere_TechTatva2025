#include <fstream>
#include "../testlib.h"
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    string reverseVowels(string s) {
        int start = 0;
        int end = s.length() - 1;
        string vowels = "aeiouAEIOU";

        while (start < end) {
            while (start < end && vowels.find(s[start]) == string::npos) {
                start++;
            }
            while (start < end && vowels.find(s[end]) == string::npos) {
                end--;
            }
            swap(s[start], s[end]);
            start++;
            end--;
        }
        return s;
    }
};

void writeTest(int z) {
    string num = (z > 9) ? to_string(z) : "0" + to_string(z);
    fstream test, answer;
    test.open("StringInput" + num + ".txt", ios::app);
    answer.open("StringOutput" + num + ".txt", ios::app);

    Solution sol;

    int t = rnd.next(1, 100); // Number of test cases
    test << t << endl;

    while (t--) {
        int len = rnd.next(1, 50); // String length (adjustable)
        string s = "";

        for (int i = 0; i < len; i++) {
            char c = rnd.next(32, 126); // Printable ASCII characters
            s += c;
        }

        test << s << endl;
        answer << sol.reverseVowels(s) << endl; // Expected output
    }

    test.close();
    answer.close();
}

int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);
    for (int no = 0; no < 14; no++) 
        writeTest(no);

    return 0;
}