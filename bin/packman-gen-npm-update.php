#!/usr/bin/env php
<?php
if ($argc < 6 ){
	die('Usage '.  __FILE__ . ' </path/to/orig/json> <api id> <api key> <api endpoint> <package id>'. "\n");
}
require_once(__DIR__.'/packmanApi.php');

$orig_package_json=$argv[1];
$api_user=$argv[2];
$api_key=$argv[3];
$endpoint=$argv[4];
$package_id=$argv[5];
//$unused_deps=file($deps_file, FILE_IGNORE_NEW_LINES );
$orig_json = file_get_contents($orig_package_json);
$orig_json_a = json_decode($orig_json);
$deps = json_decode(json_encode($orig_json_a->dependencies), true);
foreach ($deps as $dep => $version){
	$mydata=array(
		'package_id'=> $package_id,
		'package_type' => 3,
		'env' => 'NodeJS',
		'dep_type' => 1,
		'depends_on_package' => $dep,
		'depends_on_package_version' => $version,
		'needed_files' => '',
	);
	makeRequest('/packagedeps/add', $mydata, $api_user, $api_key, $endpoint);
}

$dev_deps = json_decode(json_encode($orig_json_a->devDependencies), true);
foreach ($dev_deps as $dep => $version){
        $mydata=array(
                'package_id'=> $package_id,
                'package_type' => 3,
                'env' => 'NodeJS',
                'dep_type' => 2,
                'depends_on_package' => $dep,
                'depends_on_package_version' => $version,
                'needed_files' => '',
        );
        makeRequest('/packagedeps/add', $mydata, $api_user, $api_key, $endpoint);

        echo "\nINFO: Installing NPM module $dep to satisfy dev dependecies...\n";
        exec ("sudo npm install $dep", $out, $rc);
        echo (implode("\n",$out));
	if ($rc != 0){
        	echo "ERROR: Exited with $rc\n";
	}
}

//echo 'The following modules do not seem to be used in your code: ' . implode(', ',$unused_deps). "\n";
?>
