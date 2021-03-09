#!/usr/bin/perl -w
use strict;
use warnings;


my $pid = fork;
if ($pid > 0){
    while(1){
        print "Main has child $pid\n";
        sleep 1;
    }
}
elsif ($pid == 0){
    while(1){
        print "child say\n";
        sleep 1;
    }
}
