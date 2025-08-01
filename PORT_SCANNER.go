package main

import (
    "fmt"
    "net"
    "sort"
    "sync"
    "time"
)

func scanPort(wg *sync.WaitGroup, hostname string, port int, results chan int) {
    defer wg.Done()
    address := fmt.Sprintf("%s:%d", hostname, port)
    conn, err := net.DialTimeout("tcp", address, 500*time.Millisecond)
    if err == nil {
        results <- port
        conn.Close()
    }
}

func main() {
    var hostname string
    var startPort, endPort int

    fmt.Print("Enter hostname or IP to scan: ")
    fmt.Scan(&hostname)

    fmt.Print("Enter start port: ")
    fmt.Scan(&startPort)

    fmt.Print("Enter end port: ")
    fmt.Scan(&endPort)

    var wg sync.WaitGroup
    results := make(chan int, endPort-startPort+1)

    for port := startPort; port <= endPort; port++ {
        wg.Add(1)
        go scanPort(&wg, hostname, port, results)
    }

    go func() {
        wg.Wait()
        close(results)
    }()

    var openPorts []int
    for port := range results {
        openPorts = append(openPorts, port)
    }

    sort.Ints(openPorts)
    fmt.Println("Open ports:")
    for _, port := range openPorts {
        fmt.Printf(" - %d\n", port)
    }
}
