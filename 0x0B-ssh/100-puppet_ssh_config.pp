# creates an ssh config file on server
file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "#!/usr/bin/env bash\n# Configuration file for my local ssh client\n# Allows connection to server without password\nHost 100.25.161.102\n    IdentityFile ~/.ssh/school\n    PasswordAuthentication no",
}
