#!/usr/bin/perl
if(!defined($pid = fork())) {
   # fork returned undef, so unsuccessful
   die "Cannot fork a child: $!";
} elsif ($pid == 0) {
   print "Printed by child process\n";
   exec("date") || die "can't exec date: $!";
} else {
   # fork returned 0 nor undef
   # so this branch is parent
   print "Printed by parent process\n";
   $ret = waitpid($pid, 0);
   print "Completed process id: $ret\n";
}
1;
