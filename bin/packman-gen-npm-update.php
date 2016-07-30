#!/usr/bin/env php
<?php
if ($argc < 6 ){
	die('Usage '.  __FILE__ . ' </path/to/orig/json> </path/to/unused/deps/file> <api id> <api key> <api endpoint> <package id>'. "\n");
}
require_once(__DIR__.'/packmanApi.php');

$orig_package_json=$argv[1];
$deps_file=$argv[2];
$api_user=$argv[3];
$api_key=$argv[4];
$endpoint=$argv[5];
$package_id=$argv[6];
$unused_deps=file($deps_file, FILE_IGNORE_NEW_LINES );
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
echo 'The following modules do not seem to be used in your code: ' . implode(', ',$unused_deps). "\n";
?>
