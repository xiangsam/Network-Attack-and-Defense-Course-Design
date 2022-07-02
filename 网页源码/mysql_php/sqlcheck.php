<?php
function safe($sql)
{
    //sql injection blacklist
    $blackList = array(' ', '#', '=', '<', '>', '^', '$', '-', ';', '&', '+', 'or', 'and', 'select', 'insert', 'update', 'delete', '`', './', '/*', '*/');
    foreach ($blackList as $blackitem) {
        if (stripos(strtolower($sql), $blackitem) !== False) {
            return False;
        }
    }
    return True;
}
