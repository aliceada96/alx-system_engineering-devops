#Install flask from pip3
Package { 'flask':
  ensure  => ' 2.1.0',
  provider => 'pip3',
}
