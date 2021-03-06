//===-- Endian.h ------------------------------------------------*- C++ -*-===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//

#ifndef LLDB_UTILITY_ENDIAN_H
#define LLDB_UTILITY_ENDIAN_H

#include "lldb/lldb-enumerations.h"

#include <stdint.h>

namespace lldb_private {

namespace endian {

static union EndianTest {
  uint32_t num;
  uint8_t bytes[sizeof(uint32_t)];
} const endianTest = {0x01020304};

inline lldb::ByteOrder InlHostByteOrder() {
  return (lldb::ByteOrder)endianTest.bytes[0];
}

//    ByteOrder const InlHostByteOrder = (ByteOrder)endianTest.bytes[0];
}
}

#endif // liblldb_host_endian_h_
