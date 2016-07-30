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
//var_dump($myarr);
//for ($i=0;$i < count($new_deps); $i++){
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
	echo "About to call makeRequest('/packagedeps/add', $mydata, $api_user, $api_key, $endpoint)\n";
	var_dump(makeRequest('/packagedeps/add', $mydata, $api_user, $api_key, $endpoint));
}
//$myarr=$orig_json_a->dependencies;
//var_dump($myarr);
//exit;
//var_dump($json_a);
//$curr_deps=( array_keys($myarr));
//var_dump($curr_deps);
//var_dump($new_deps);
//$result=array_diff($curr_deps,$unused_deps);
echo 'The following modules do not seem to be used in your code: ' . implode(', ',$unused_deps). "\n";
/*for @@TEST_SCRIPT@@ @@POST_INST_SCRIPT@@ @@MAIN_SCRIPT@@
# see if we already have them in the original package.json and if they exist, if so, use them, if not
# main is server.js if exists or index.js if exists, if neither exist, FATAL.*/
?>
