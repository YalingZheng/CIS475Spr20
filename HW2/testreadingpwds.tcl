#!/user/bin/expect -f
set fd "possiblepwds.txt"
set fp [open "$fd" r]
set data [read $fp]
foreach line $data {
       send_user "$line\n"
}
