// Copyright 2017 Zulin Liu liuzulin@bu.edu
// Copyright 2017 Simin Zhai siminz@bu.edu
// Copyright 2017 James Fallacara jafallac@bu.edu
// Copyright 2017 Yu Zhao yuzhao95@bu.edu

#include <stdlib.h>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using std::string;
using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::ifstream;
using std::map;
using std::set;

// store the information of every node.
struct node {
 public:
    char me;
    struct node *parent;
    struct node *children[26];
    std::string word = "";
    bool END = false;
};

// global variable node
node *root;

// store the whole puzzle
struct puzzle {
 public:
    int dimension = 0;
    std::vector <std::vector <char>> grid;
    void clear_puz(int d) {       // clear puzzle
        dimension = d;
        grid.clear();
        grid.resize(dimension, std::vector <char> (d, 0));
    }
};


// recursion using node, puzzle, map and set to get the answer.
int solver(std::vector <std::string> wordtrie,
           puzzle *puz,
           node *trie,
           std::vector <int> Lengths,
           std::map <int, char> cell,
           std::vector <std::string> *words,
           std::set <std::string> *Sol);

// recurison also with every node's coordinate to get the answer.
int solve_puzzle(std::vector <std::string> wordtrie,
               puzzle *puz,
               std::vector <int> Lengths,
               node *trie,
               std::map <int, char> *cell,
               int x, int y,
               std::vector <std::string> *words,
               std::set <std::string> *Sol) {
    if (!trie) {
        return false;
    }
    std::map <int, char> newcell;
    newcell.insert(cell->begin(), cell->end());
    (newcell)[x + y * puz->dimension] = trie->me;
    for (const auto &pointer : (*cell)) {
        if (trie->END) {
            std::vector <int> NewLengths = Lengths;
            NewLengths.erase(NewLengths.begin());
            std::vector <std::string> Newwords = *words;
            Newwords.push_back(trie->word);
            for (const auto &pointer : (Newwords)) {
                if (solver(wordtrie, puz, root, NewLengths,
                           newcell, &Newwords, Sol)) {
                    *words = Newwords;
                    *cell = newcell;
                    return true;
                } else {
                    return false;
                }
            }
        }
    }
    int Min_x = (x - 1 > 0) ? x - 1 : 0;
    int Min_y = (y - 1 > 0) ? y - 1 : 0;
    int Max_x = (x + 1 < puz->dimension) ? x + 1 : puz->dimension - 1;
    int Max_y = (y + 1 < puz->dimension) ? y + 1 : puz->dimension - 1;
    for (int i = Min_x; i <= Max_x; i++) {
        for (int j = Min_y; j <= Max_y; j++) {
            if (newcell.count(i + j * puz->dimension)) {
                continue;
            }
            char target;
            try {
                target = puz->grid.at(i).at(j);
            } catch(std::out_of_range) {
                continue;
            }
            if (trie->children[target - 'a']) {
                if (solve_puzzle(wordtrie, puz, Lengths,
                                 trie->children[puz->grid.at(i).at(j)
                                 - 'a'], & newcell, i, j,
                                 words, Sol)) {
                    cell->insert(newcell.begin(), newcell.end());
                    return true;
                }
            }
        }
    }
    return false;
}

// load puzzle
bool load_puz(const int& puzzle_size,
             const std::vector<std::vector <char>>& result,
             const std::vector <std::string>& wordtrie,
             std::vector <int> *Lengths, puzzle *puz) {
    puz->clear_puz(puzzle_size);
    for (int i = 0; i < puz->dimension; i++) {
        for (int j = 0; j < result.size(); j++) {
            puz->grid[i][j] = result[result.size() - 1 - j][i];
        }
    }
    for (auto &k : wordtrie) {
        Lengths->push_back(k.length());
    }
    if (Lengths->size() == 0 || puz->dimension == 0) {
        return false;
    }
    return true;
}

// recursion using node, puzzle, map and set to get the answer.
int solver(std::vector <std::string> wordtrie,
           puzzle *puz,
           node *trie,
           std::vector <int> Lengths,
           std::map <int, char> cell,
           std::vector <std::string> *words,
           std::set <std::string> *Sol) {
    if (Lengths.size() == 0) {
        std::string str_x = "";
        for (const auto &pointer : *words) {
            str_x += pointer + " ";
        }
        Sol->insert(str_x);
        return false;
    }
    puzzle new_puz = *puz;
    for (std::map <int, char>::reverse_iterator it = cell.rbegin();
          it != cell.rend(); ++it) {
        new_puz.grid[it->first % new_puz.dimension].erase(
            new_puz.grid[it->first % new_puz.dimension].begin()
            + it->first / new_puz.dimension);
    }
    for (int i = 0; i < new_puz.grid.size(); i++) {
        for (int j = 0; j < new_puz.grid.at(i).size(); j++) {
            std::map <int, char> newcell;
            std::vector <std::string> Newwords = *words;
            std::string s0, s1;
            if (Newwords.size() != 0) {
                for (int ii = 0; ii < Newwords.size(); ii++) {
                    s0 = Newwords[ii];
                    s1 = wordtrie[ii];
                    int count = 0;
                    for (int jj = 0; jj < s0.size(); jj++) {
                        if (s1[jj] != '*') {
                            if (s0[jj] == s1[jj]) {
                                count++;
                            }
                        } else {
                              count++;
                        }
                    }
                    if (count != s0.size()) {
                        return false;
                    }
                }
            }
            if (trie->children[Lengths.front()]) {
                if (solve_puzzle(wordtrie, &new_puz, Lengths,
                       trie->children[Lengths.front()]->children[new_puz.
                           grid.at(i).at(j) - 'a'],
                       &newcell, i, j, &Newwords, Sol)) {
                    *words = Newwords;
                    return true;
                }
            }
        }
    }
    return false;
}

// Load dictionary
int load_dic(std::string str0, node *trie) {
    std::ifstream infile(str0);
    std::string str;
    int count;
    while (infile >> str) {
        if (str.length() > 26)
            continue;
        count++;
        if (trie->children[str.length()] == NULL) {
            trie->children[str.length()] = new node;
            trie->children[str.length()]->parent = trie;
            trie->children[str.length()]->me = '0' + str.length();
        }
        node * traverse = trie->children[str.length()];
        for (auto target : str) {
            if (traverse->children[target - 'a'] == NULL) {
                traverse->children[target - 'a'] = new node;
                traverse->children[target - 'a']->parent = traverse;
                traverse->children[target - 'a']->me = target;
            }
            traverse = traverse->children[target - 'a'];
        }
        traverse->END = true;
        traverse->word = str;
    }
    return count;
}

// Split string
std::vector <std::string> word_split(const std::string& str,
                                     const std::string& target) {
    std::vector <std::string> str_split;
    std::string::size_type m, n;
    n = str.find(target);
    m = 0;
    while (std::string::npos != n) {
        str_split.push_back(str.substr(m, n - m));
        m = n + target.size();
        n = str.find(target, m);
    }
    if (m != str.length())
        str_split.push_back(str.substr(m));
    return str_split;
}




int main(int argc, char **argv) {
    node trie = node();
    node Ltrie = node();

    // Load dictionary
    load_dic(argv[1], &trie);
    load_dic(argv[2], &Ltrie);
    while (true) {
        puzzle puz = puzzle();
        std::string str;
        std::vector <std::vector <char>> result;
        std::string Hint;
        std::string line;

        // Get the standard input
        while (std::cin) {
            if (std::cin.eof()) exit(0);
            getline(std::cin, line);
            if (line == "") exit(0);
            if (line.find("*") == std::string::npos) {
                std::vector<char> data(line.begin(), line.end());
                result.push_back(data);
            } else {
                Hint = line;
                break;
            }
        }
        int puzzle_size = result[0].size();
        std::vector <std::string> wordtrie = word_split(Hint, " ");
        root = &trie;
        std::map <int, char> cell;
        std::vector <int> Lengths;
        if (!load_puz(puzzle_size, result, wordtrie, &Lengths, &puz)) {
            return false;
        }
        std::vector<std::string> words;
        std::set<std::string> Sol;

        // Try the small dictionary first
        solver(wordtrie, &puz, &trie, Lengths, cell, &words, &Sol);

        // If small dictionary doesn't have the answer, try the bigger one.
        if (Sol.size() == 0) {
            root = &Ltrie;
            solver(wordtrie,
                &puz, &Ltrie, Lengths, cell, &words, &Sol);
        }

        // Output
        for (const auto &pointer : Sol) {
            std::cout << pointer << std::endl;
        }
        std::cout << "." << std::endl;
    }
}
