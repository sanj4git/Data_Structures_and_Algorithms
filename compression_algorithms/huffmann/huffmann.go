package main

import (
    "container/heap"
    "fmt"
    "io/ioutil"
    "os"
    "sort"
)

type Node struct {
    char   rune
    freq   int
    left   *Node
    right  *Node
    isLeaf bool
}

type PriorityQueue []*Node

func (pq PriorityQueue) Len() int { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool {
    if pq[i].freq == pq[j].freq {
        return pq[i].char < pq[j].char
    }
    return pq[i].freq < pq[j].freq
}
func (pq PriorityQueue) Swap(i, j int) {
    pq[i], pq[j] = pq[j], pq[i]
}
func (pq *PriorityQueue) Push(x interface{}) {
    *pq = append(*pq, x.(*Node))
}
func (pq *PriorityQueue) Pop() interface{} {
    old := *pq
    n := len(old)
    x := old[n-1]
    *pq = old[0 : n-1]
    return x
}

func BuildHuffmanTree(freqMap map[rune]int) *Node {
    // Handle empty input
    if len(freqMap) == 0 {
        return nil
    }

    // Handle single character case
    if len(freqMap) == 1 {
        for char, freq := range freqMap {
            return &Node{
                char:   char,
                freq:   freq,
                isLeaf: true,
            }
        }
    }

    pq := &PriorityQueue{}
    heap.Init(pq)
    
    chars := make([]rune, 0, len(freqMap))
    for char := range freqMap {
        chars = append(chars, char)
    }
    
    sort.Slice(chars, func(i, j int) bool {
        return chars[i] < chars[j]
    })
    
    for _, char := range chars {
        heap.Push(pq, &Node{
            char:   char,
            freq:   freqMap[char],
            isLeaf: true,
        })
    }
    
    for pq.Len() > 1 {
        left := heap.Pop(pq).(*Node)
        right := heap.Pop(pq).(*Node)
        
        if left.char > right.char {
            left, right = right, left
        }
        
        merged := &Node{
            freq:   left.freq + right.freq,
            left:   left,
            right:  right,
            isLeaf: false,
            char:   min(left.char, right.char),
        }
        heap.Push(pq, merged)
    }
    
    return heap.Pop(pq).(*Node)
}

func min(a, b rune) rune {
    if a < b {
        return a
    }
    return b
}

func GenerateCodes(root *Node, prefix string, codes map[rune]string) {
    if root == nil {
        return
    }
    
    if root.isLeaf {
        // For single character case, use "0" as the code
        if prefix == "" {
            codes[root.char] = "0"
        } else {
            codes[root.char] = prefix
        }
        return
    }
    
    GenerateCodes(root.left, prefix+"0", codes)
    GenerateCodes(root.right, prefix+"1", codes)
}

type HuffmanCodec struct {
    root  *Node
    codes map[rune]string
}

func NewHuffmanCodec(input string) *HuffmanCodec {
    // Handle empty input
    if input == "" {
        return &HuffmanCodec{
            root:  nil,
            codes: make(map[rune]string),
        }
    }

    freqMap := make(map[rune]int)
    for _, char := range input {
        freqMap[char]++
    }
    
    root := BuildHuffmanTree(freqMap)
    codes := make(map[rune]string)
    GenerateCodes(root, "", codes)
    
    return &HuffmanCodec{
        root:  root,
        codes: codes,
    }
}

func (hc *HuffmanCodec) Compress(input string) string {
    // Handle empty input
    if input == "" {
        return ""
    }

    // Handle nil codec (created with empty input)
    if hc.root == nil {
        return ""
    }

    compressed := ""
    for _, char := range input {
        compressed += hc.codes[char]
    }
    return compressed
}

func (hc *HuffmanCodec) Decompress(compressed string) string {
    // Handle empty input or nil codec
    if compressed == "" || hc.root == nil {
        return ""
    }

    // Handle single character case
    if hc.root.isLeaf {
        result := ""
        for range compressed {
            result += string(hc.root.char)
        }
        return result
    }

    decoded := ""
    current := hc.root
    
    for _, bit := range compressed {
        if bit == '0' {
            current = current.left
        } else {
            current = current.right
        }
        
        if current.isLeaf {
            decoded += string(current.char)
            current = hc.root
        }
    }
    
    return decoded
}

func main() {
<<<<<<< HEAD
    if len(os.Args) < 2 {
        fmt.Println("Usage: go run h.go <filename>")
        return
    }

    filename := os.Args[1]
    content, err := ioutil.ReadFile(filename)
    if err != nil {
        fmt.Println("Error reading file:", err)
        return
    }

    input := string(content)
    codec := NewHuffmanCodec(input)
    compressed := codec.Compress(input)

    fmt.Println("Compressed Data:", compressed)
    fmt.Println("Decompressed Data:", codec.Decompress(compressed))
}
//Main block to use initial implementation which takes a string as input directly
// func main() {
//     input := "Hello"
//     codec := NewHuffmanCodec(input)
//     var compressed string
//     compressed = codec.Compress(input)

//     fmt.Println("\nNormal case test:")
//     fmt.Println("Input:", input)
//     fmt.Println("Compressed:", compressed)
//     fmt.Println("Decompressed:", codec.Decompress(compressed))
// }
=======
    input := "Hello"
    codec := NewHuffmanCodec(input)
    var compressed string
    compressed = codec.Compress(input)
    
    fmt.Println("\nNormal case test:")
    fmt.Println("Input:", input)
    fmt.Println("Compressed:", compressed)
    fmt.Println("Decompressed:", codec.Decompress(compressed))
}
>>>>>>> d0935ffb3a186013e2e9ea1e5daa816b0fad5583
