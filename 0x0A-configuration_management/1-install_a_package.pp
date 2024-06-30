#install a package
#install.packages("flask")
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
