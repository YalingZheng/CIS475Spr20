#!/usr/bin/perl -w

use strict;

print "Content-type: text/html; charset=US-ASCII\n\n";
print "<html>";
print "<head>";
print "<title>A Cookie Based Wealth Tracker</title>";

print <<SCRIPTEND;
<script type="text/javascript">
   function setCookie(name, value, expires, path, domain, secure) {
         var today = new Date();
         today.setTime(today.getTime());
        if (expires) {
                expires = expires * 1000 * 60 * 60 *24;
        }
        var expires_date = new Date(today.getTime() + (expires));
        document.cookie = name + "=" + escape(value) +
          ((expires) ? ";expires=" + expires_date.toGMTString() : "")

      }
</script>
SCRIPTEND

print "</head>";
print "<body>";
my $forminfo = '';
$forminfo = $ENV{QUERY_STRING};
$forminfo =~ tr/+/ /;
$forminfo =~ s/%([a-fA-F0-9]{2,2})/chr(hex($1))/eg;
print "$forminfo";

my $filename = '/var/www/cgi-bin/collect.txt';
open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";
print $fh "$forminfo";
close $fh;

print "</body>";
print "</html>";
