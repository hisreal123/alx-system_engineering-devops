#execute a command
exec { 'killnow':
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell',
  returns  => [0, 1]
}
