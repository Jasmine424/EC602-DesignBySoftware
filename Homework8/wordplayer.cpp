// Copyright 2017 Jamesjafallac@bu.edu
// Copyright 2017 Liuzulinliuzulin@bu.edu
// Copyright 2017 SiminZhai siminz@bu.edu
// This is the C++ code for wordplayer

#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using std::string;
using std::cout;
using std::cin;
using std::map;
using std::set;
using std::vector;
using std::ifstream;

set<string> readfile(string text, int& longest) {
    set<string> word_set;
    string x;
    longest = 0;
    ifstream inFile;
    inFile.open(text);
    while (inFile >> x) {
        word_set.insert(x);
        if (longest < x.size()) {
            longest = x.size();
        }
    }
    return word_set;
}

vector<map<string, string>> list_organize(set<string> word_set, int longest) {
    string key_sort;
    vector<map<string, string>> list_d;
    list_d.resize(longest+1);
    for (string const& key : word_set) {
        int length = key.size();
        key_sort = key;
        sort(key_sort.begin(), key_sort.end());
        list_d[length][key] = key_sort;
    }
    return list_d;
}

bool match_test(string word, string l, int length, int l_l) {
    int j = 0;
    for (int i=0; i < length; i++) {
        while (word[i] != l[j]) {
            j = j + 1;
            if (j == l_l) {
                return false;
            }
        }
        j = j + 1;
        if (j == l_l && i != (length - 1)) {
            return false;
        }
    }
    return true;
}  // namespace mynamespace

vector<string> scrabble(map<string, string> dic, string l,
    int length, int l_l) {
    vector<string> word_list;
    bool match;
    string word;
    for (auto const& x : dic) {
            word = x.second;
            match = match_test(word, l, length, l_l);
            if (match == true) {
                word_list.push_back(x.first);
            }
        }
    return word_list;
}

int main(int argumentcount, char **arguments) {
    string text;
    int longest;
    text = arguments[1];

    set<string> word_set;
    word_set = readfile(text, longest);
    vector <map<string, string>> list_d;
    list_d = list_organize(word_set, longest);

    map<string, string> d_desired;
    vector<string> word_l_desired;
    string letters, l;
    int word_length;
    while (true) {
        cin >> letters >> word_length;
        if (word_length == 0) {
            return 0;
        }
        int l_l = letters.size();
        l = letters;
        sort(l.begin(), l.end());
        if (l_l >= word_length && word_length <= longest) {
                d_desired = list_d[word_length];
                word_l_desired = scrabble(d_desired, l, word_length, l_l);
                sort(word_l_desired.begin(), word_l_desired.end());
                for (int i=0; i < word_l_desired.size(); i++) {
                        cout << word_l_desired[i] << '\n';
                    }
            }
        word_l_desired.clear();
        cout << "." << '\n';
    }
}
