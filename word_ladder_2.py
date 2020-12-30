# Author: Harsh Kohli
# Date created: 12/1/2020

from queue import Queue
import copy


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def findLadders(beginWord, endWord, wordList):
    if endWord not in wordList:
        return []
    nodes = []
    first_node = Node(beginWord)
    adj_map = {}
    nodes.append(first_node)

    adjacents = []
    for index in range(1, len(beginWord) - 1):
        adjacent = beginWord[:index] + '.' + beginWord[index + 1:]
        adjacents.append(adjacent)
    first, last = '.' + beginWord[1:], beginWord[:len(beginWord) - 1] + '.'
    adjacents.append(first)
    adjacents.append(last)
    for adj in adjacents:
        adj_map[adj] = [first_node]

    for word in wordList:
        if word == beginWord:
            continue
        new_node = Node(word)

        adjacents = []
        for index in range(1, len(word) - 1):
            adjacent = word[:index] + '.' + word[index + 1:]
            adjacents.append(adjacent)
        first, last = '.' + word[1:], word[:len(word) - 1] + '.'
        adjacents.append(first)
        if len(word) > 1:
            adjacents.append(last)

        for adj in adjacents:
            if adj not in adj_map:
                adj_map[adj] = [new_node]
            else:
                for node in adj_map[adj]:
                    if node.next is None:
                        node.next = [new_node]
                    else:
                        node.next.append(new_node)
                    if new_node.next is None:
                        new_node.next = [node]
                    else:
                        new_node.next.append(node)
                adj_map[adj].append(new_node)
        nodes.append(new_node)
    q = Queue()
    q.put((first_node, []))
    q.put((None, None))
    ladder = 1
    found = False
    valid_paths = []
    seen = {}
    while not q.empty():
        node, path = q.get()
        if node is None:
            ladder = ladder + 1
            if q.empty() or found:
                break
            q.put((None, None))
            continue
        if node.val in seen and seen[node.val] != ladder:
            continue
        if node.val == endWord:
            path.append(node.val)
            valid_paths.append(path)
            found = True
            continue
            # break
        if node.next is not None:
            for child in node.next:
                if child.val not in seen:
                    path_copy = copy.deepcopy(path)
                    path_copy.append(node.val)
                    q.put((child, path_copy))
        seen[node.val] = ladder

    if found:
        return valid_paths
    else:
        return []


beginWord = "cet"
endWord = "ism"
wordList = ["kid", "tag", "pup", "ail", "tun", "woo", "erg", "luz", "brr", "gay", "sip", "kay", "per", "val", "mes",
            "ohs", "now", "boa", "cet", "pal", "bar", "die", "war", "hay", "eco", "pub", "lob", "rue", "fry", "lit",
            "rex", "jan", "cot", "bid", "ali", "pay", "col", "gum", "ger", "row", "won", "dan", "rum", "fad", "tut",
            "sag", "yip", "sui", "ark", "has", "zip", "fez", "own", "ump", "dis", "ads", "max", "jaw", "out", "btu",
            "ana", "gap", "cry", "led", "abe", "box", "ore", "pig", "fie", "toy", "fat", "cal", "lie", "noh", "sew",
            "ono", "tam", "flu", "mgm", "ply", "awe", "pry", "tit", "tie", "yet", "too", "tax", "jim", "san", "pan",
            "map", "ski", "ova", "wed", "non", "wac", "nut", "why", "bye", "lye", "oct", "old", "fin", "feb", "chi",
            "sap", "owl", "log", "tod", "dot", "bow", "fob", "for", "joe", "ivy", "fan", "age", "fax", "hip", "jib",
            "mel", "hus", "sob", "ifs", "tab", "ara", "dab", "jag", "jar", "arm", "lot", "tom", "sax", "tex", "yum",
            "pei", "wen", "wry", "ire", "irk", "far", "mew", "wit", "doe", "gas", "rte", "ian", "pot", "ask", "wag",
            "hag", "amy", "nag", "ron", "soy", "gin", "don", "tug", "fay", "vic", "boo", "nam", "ave", "buy", "sop",
            "but", "orb", "fen", "paw", "his", "sub", "bob", "yea", "oft", "inn", "rod", "yam", "pew", "web", "hod",
            "hun", "gyp", "wei", "wis", "rob", "gad", "pie", "mon", "dog", "bib", "rub", "ere", "dig", "era", "cat",
            "fox", "bee", "mod", "day", "apr", "vie", "nev", "jam", "pam", "new", "aye", "ani", "and", "ibm", "yap",
            "can", "pyx", "tar", "kin", "fog", "hum", "pip", "cup", "dye", "lyx", "jog", "nun", "par", "wan", "fey",
            "bus", "oak", "bad", "ats", "set", "qom", "vat", "eat", "pus", "rev", "axe", "ion", "six", "ila", "lao",
            "mom", "mas", "pro", "few", "opt", "poe", "art", "ash", "oar", "cap", "lop", "may", "shy", "rid", "bat",
            "sum", "rim", "fee", "bmw", "sky", "maj", "hue", "thy", "ava", "rap", "den", "fla", "auk", "cox", "ibo",
            "hey", "saw", "vim", "sec", "ltd", "you", "its", "tat", "dew", "eva", "tog", "ram", "let", "see", "zit",
            "maw", "nix", "ate", "gig", "rep", "owe", "ind", "hog", "eve", "sam", "zoo", "any", "dow", "cod", "bed",
            "vet", "ham", "sis", "hex", "via", "fir", "nod", "mao", "aug", "mum", "hoe", "bah", "hal", "keg", "hew",
            "zed", "tow", "gog", "ass", "dem", "who", "bet", "gos", "son", "ear", "spy", "kit", "boy", "due", "sen",
            "oaf", "mix", "hep", "fur", "ada", "bin", "nil", "mia", "ewe", "hit", "fix", "sad", "rib", "eye", "hop",
            "haw", "wax", "mid", "tad", "ken", "wad", "rye", "pap", "bog", "gut", "ito", "woe", "our", "ado", "sin",
            "mad", "ray", "hon", "roy", "dip", "hen", "iva", "lug", "asp", "hui", "yak", "bay", "poi", "yep", "bun",
            "try", "lad", "elm", "nat", "wyo", "gym", "dug", "toe", "dee", "wig", "sly", "rip", "geo", "cog", "pas",
            "zen", "odd", "nan", "lay", "pod", "fit", "hem", "joy", "bum", "rio", "yon", "dec", "leg", "put", "sue",
            "dim", "pet", "yaw", "nub", "bit", "bur", "sid", "sun", "oil", "red", "doc", "moe", "caw", "eel", "dix",
            "cub", "end", "gem", "off", "yew", "hug", "pop", "tub", "sgt", "lid", "pun", "ton", "sol", "din", "yup",
            "jab", "pea", "bug", "gag", "mil", "jig", "hub", "low", "did", "tin", "get", "gte", "sox", "lei", "mig",
            "fig", "lon", "use", "ban", "flo", "nov", "jut", "bag", "mir", "sty", "lap", "two", "ins", "con", "ant",
            "net", "tux", "ode", "stu", "mug", "cad", "nap", "gun", "fop", "tot", "sow", "sal", "sic", "ted", "wot",
            "del", "imp", "cob", "way", "ann", "tan", "mci", "job", "wet", "ism", "err", "him", "all", "pad", "hah",
            "hie", "aim", "ike", "jed", "ego", "mac", "baa", "min", "com", "ill", "was", "cab", "ago", "ina", "big",
            "ilk", "gal", "tap", "duh", "ola", "ran", "lab", "top", "gob", "hot", "ora", "tia", "kip", "han", "met",
            "hut", "she", "sac", "fed", "goo", "tee", "ell", "not", "act", "gil", "rut", "ala", "ape", "rig", "cid",
            "god", "duo", "lin", "aid", "gel", "awl", "lag", "elf", "liz", "ref", "aha", "fib", "oho", "tho", "her",
            "nor", "ace", "adz", "fun", "ned", "coo", "win", "tao", "coy", "van", "man", "pit", "guy", "foe", "hid",
            "mai", "sup", "jay", "hob", "mow", "jot", "are", "pol", "arc", "lax", "aft", "alb", "len", "air", "pug",
            "pox", "vow", "got", "meg", "zoe", "amp", "ale", "bud", "gee", "pin", "dun", "pat", "ten", "mob"]


# beginWord = "red"
# endWord = "tax"
# wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
ll = findLadders(beginWord, endWord, wordList)
print(ll)
