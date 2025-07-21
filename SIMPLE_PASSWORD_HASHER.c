
#include <stdio.h>
#include <string.h>
#include <openssl/sha.h>

// Function to hash a password using SHA-256
void hash_password(const char *password, unsigned char *output) {
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, password, strlen(password));
    SHA256_Final(output, &sha256);
}

// Helper to print the hash in hex
void print_hash(unsigned char *hash) {
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++)
        printf("%02x", hash[i]);
    printf("\n");
}

// Compare two hashes
int compare_hash(unsigned char *hash1, unsigned char *hash2) {
    return memcmp(hash1, hash2, SHA256_DIGEST_LENGTH) == 0;
}

int main() {
    char password[256];
    printf("Enter your password: ");
    fgets(password, sizeof(password), stdin);

    // Remove newline
    password[strcspn(password, "\n")] = '\0';

    unsigned char hash[SHA256_DIGEST_LENGTH];
    hash_password(password, hash);

    printf("Hashed password: ");
    print_hash(hash);

    // Example: simulate a stored hash (for password: "secret123")
    unsigned char stored_hash[SHA256_DIGEST_LENGTH];
    hash_password("secret123", stored_hash);

    if (compare_hash(hash, stored_hash)) {
        printf("Access Granted ✅\n");
    } else {
        printf("Access Denied ❌\n");
    }

    return 0;
}
