package System::Timeout;
use strict;
use warnings;
use vars qw(@ISA @EXPORT_OK $VERSION);
use IPC::Cmd qw(run);
 
require Exporter;
@ISA = qw(Exporter);
@EXPORT_OK = qw(system timeout);
 
our $VERSION = '0.07';
 
sub system
{
    return timeout(@_);
}
 
sub timeout
{
        if ($_[0] !~ /^\d+$/)
        {
                my $r = CORE::system(@_);
                return $r;
        }
        else
        {
                my $timeout_secs = shift @_;
                my $ref_cmd = \@_;
                my $r = run(command => $ref_cmd, timeout=> $timeout_secs, verbose=>1, );
                return 0 if $r;
                return 1 unless $r;
        }
}
 
1;
 
__END__
 