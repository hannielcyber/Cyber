#include <stdio.h>
#include <string.h>
#include <ctype.h>

int has_uppercase(const char *s) {
    for (int i = 0; s[i]; i++) {
        if (isupper(s[i]))
            return 1;
    }
    return 0;
}

int has_lowercase(const char *s) {
    for (int i = 0; s[i]; i++) {
        if (islower(s[i]))
            return 1;
    }
    return 0;
}

int has_digit(const char *s) {
    for (int i = 0; s[i]; i++) {
        if (isdigit(s[i]))
            return 1;
    }
    return 0;
}

int has_special(const char *s) {
    const char *special = "@$!%*?&";
    for (int i = 0; s[i]; i++) {
        if (strchr(special, s[i]))
            return 1;
    }
    return 0;
}

int main() {
    char password[256];

    printf("Enter your password: ");
    fgets(password, sizeof(password), stdin);

    // Remove newline character
    password[strcspn(password, "\n")] = '\0';

    int score = 0;

    if (strlen(password) >= 8) score++;
    if (has_uppercase(password)) score++;
    if (has_lowercase(password)) score++;
    if (has_digit(password)) score++;
    if (has_special(password)) score++;

    printf("Password Strength Score: %d/5\n", score);

    if (strlen(password) < 8)
        printf("- Make your password at least 8 characters long.\n");
    if (!has_uppercase(password))
        printf("- Add at least one uppercase letter.\n");
    if (!has_lowercase(password))
        printf("- Add at least one lowercase letter.\n");
    if (!has_digit(password))
        printf("- Add at least one digit.\n");
    if (!has_special(password))
        printf("- Add at least one special character (@$!%%*?&).\n");

    return 0;
}
