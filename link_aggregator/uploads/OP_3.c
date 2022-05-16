#include <stdio.h>
#include <stdlib.h>

int check_have_element(char const array[], char element, int length){
    for (int i = 0; i < length; ++i)
        if (array[i] == element)
            return 1;
    return 0;
}

void insert (char* string, char word[], int len_str, int len_word) {
    string = (char*) realloc(string,len_str + len_word);
    for (int i = 0; i < len_word; i++) {
        string[i + len_str - 1] = word[i];
    }
    string[len_str + len_word - 1] = '\0';
}

char* tokenize (char* const string, char* tokenize_string, int len_str) {
    int len_token_str = 1;
    tokenize_string = (char*) malloc(sizeof (char));
    for (int i = 0; i < len_str - 1; i++) {
        if (string[i] == '.') {
            insert(tokenize_string, "DOT", len_token_str, 3);
            len_token_str += 3;
        }
        else if (string[i] == '+') {
            insert(tokenize_string, "PLUS", len_token_str, 4);
            len_token_str += 4;
        }
        else if (string[i] == '-') {
            insert(tokenize_string, "MINUS", len_token_str, 5);
            len_token_str += 5;
        }
        else if (string[i] == '=') {
            insert(tokenize_string, "EQUALS", len_token_str, 6);
            len_token_str += 6;
        }
        else if (string[i] == '*') {
            insert(tokenize_string, "MULTIPLICATION", len_token_str, 14);
            len_token_str += 14;
        }
        else if (string[i] == '/') {
            insert(tokenize_string, "DIVISION", len_token_str, 8);
            len_token_str += 8;
        }
        else if (string[i] == '(' || string[i] == ')') {
            insert(tokenize_string, "PARENTHESES", len_token_str, 11);
            len_token_str += 11;
        }
        else {
            insert(tokenize_string, "DIGIT", len_token_str, 5);
            len_token_str += 5;
        }
    }
    return tokenize_string;
}



int main() {
    FILE* input_file;
    char* user_str = NULL;
    char* token_string = NULL;
    int len = 1;
    char c;
    char alf[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
    int len_alf;
    char signs[] = {'.', '+', '-', '=', '*', '/', '(', ')'};
    int len_signs;
    int user_step;
    int flag_str_not_valid = 1;
    int flag_user_enter_data = 0;

    while (1) {

        printf("Chose your step\n"
               "1: Enter string\n"
               "2: Tokenize\n"
               "3: Enter string from file\n"
               "4: Output into file\n"
               "5: Output\n"
               "6: Exit\n");
        if (scanf("%d", &user_step) != 1)
            while(fgetc(stdin) != '\n')
                continue;

        switch (user_step) {
            case 1:
                len = 1;
                flag_str_not_valid = 1;
                user_str = (char*) malloc(sizeof(char));
                printf("input string: ");
                c = getchar();
                user_str[len - 1] = c;
                user_str = (char*) realloc(user_str, len);
                while((c = getchar()) != '\n') {
                    user_str[len - 1] = c;
                    len++;
                    user_str = (char*) realloc(user_str, len);
                }
                user_str[len - 1] = '\0';
                len_alf = (int) (sizeof(alf) / sizeof(alf[0]));
                len_signs = (int) (sizeof(signs) / sizeof(signs[0]));

                for (int i = 0; i < len - 1; ++i) {
                    if (!(check_have_element(alf, user_str[i], len_alf) || check_have_element(signs, user_str[i], len_signs))){
                        flag_str_not_valid = 0;
                        printf("invalid string\n");

                        break;
                    }

                }
                flag_user_enter_data = 1;
                if (flag_str_not_valid == 0) {
                    flag_user_enter_data = 0;
                    continue;
                }

                printf("%s (%d symbols)\n", user_str, len - 1);
                break;

            case 2:
                if (flag_user_enter_data == 1) {
                    token_string = tokenize(user_str, token_string, len);
                }
                else {
                    printf("not have date\n");
                }

                break;

            case 3:
                input_file = fopen("input.txt", "r");
                if (input_file != NULL) {
                    free(user_str);
                    len = 1;
                    flag_str_not_valid = 1;
                    user_str = (char*) malloc(sizeof(char));
                    while((c = (char) fgetc(input_file)) != '\n') {
                        user_str[len - 1] = c;
                        len++;
                        user_str = (char*) realloc(user_str, len);
                    }
                    user_str[len - 1] = '\0';
                    for (int i = 0; i < len - 1; ++i) {
                        if (!(check_have_element(alf, user_str[i], len_alf) || check_have_element(signs, user_str[i], len_signs))){
                            flag_str_not_valid = 0;
                        }

                    }
                    flag_user_enter_data = 1;
                    if (flag_str_not_valid == 0) {
                        continue;
                    }

                }
                else {
                    printf("Error can't open file\n");
                    continue;
                }
                fclose(input_file);
                break;

            case 4:
                if (flag_user_enter_data == 1) {
                    input_file = fopen("output.txt", "a");
                    if (input_file != NULL) {
                        fputs(token_string, input_file);
                        fputs("\n", input_file);
                        fclose(input_file);
                    }
                    else
                        printf("Error can't open file\n");
                }
                else {
                    printf("not have data\n");
                }


                break;

            case 5:
                if (flag_user_enter_data == 1) {
                    printf("%s\n", token_string);
                }
                else {
                    printf("not have data\n");
                }

                break;

            case 6:
                free(user_str);
                return 0;

            default:
                continue;
        }
    }
}