section .data
    numbers db 20
section .bss
section .text
    global _start

_start:
    mov ecx, 1
next_candidate:
    mov esi, 1
check_divisibility:
    mov eax, ecx
    xor edx, edx
    div esi
    cmp edx, 0
    jne not_divisible
    inc esi
    cmp esi, 21
    jne check_divisibility
    jmp found

not_divisible:
    inc ecx
    jmp next_candidate

found:
    mov eax, 1
    mov ebx, ecx
    int 0x80

;232792560