<?php
    $commands = array("forward", "left", "right", "back", "pivotR", "pivotL", "help", "end");
    $msg_no_arg = "Waiting for command";
    $msg_invalid_cmd = "Invalid command";
    $cmd_fn = "controll.txt";
    if (!isset($_GET["cmd"])) die($msg_no_arg);
    $cmd = $_GET["cmd"];
    if(!in_array($cmd, $commands)) die($msg_invalid_cmd . ": '$cmd'");
    $ctrl_file = fopen($cmd_fn, "w") or die("Unable to open cmd file");
    fwrite($ctrl_file, $cmd);
    fclose($ctrl_file);
    echo "Command '$cmd' sent";
?>
