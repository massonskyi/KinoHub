package main
import (
    "log"
    "net/http"
    "io"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        r.URL.Host = "localhost:8000"
        r.URL.Scheme = "http"
        resp, err := http.DefaultClient.Do(r)
        if err != nil {
            http.Error(w, err.Error(), http.StatusInternalServerError)
            return
        }
        defer resp.Body.Close()
        for k, v := range resp.Header {
            w.Header().Set(k, v[0])
        }
        w.WriteHeader(resp.StatusCode)
        _, _ = io.Copy(w, resp.Body)
    })
    log.Fatal(http.ListenAndServe(":8080", nil))
}