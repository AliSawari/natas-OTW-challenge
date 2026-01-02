<?php

$key = "$(grep ^.{5} /etc/passwd)";

if($key != "") {
    if(preg_match('/[;|&`\'"]/',$key)) {
        print "Input contains an illegal character!";
    } else {
      $cmd = "grep -i \"$key\" dictionary.txt";
      echo "Executing command: $cmd\n";
      passthru("grep -i \"$key\" dictionary.txt");
    }
}

?>