#!/usr/bin/env php
<?php
if ($argc < 2 ){
	die('Usage '.  __FILE__ . ' </path/to/new/json> </path/to/deps/file> '. "\n");
}
require_once(__DIR__.'/packmanApi.php');
$api_user=getenv('PACKMAN_API_ID');
$api_key=getenv('PACKMAN_API_KEY');
$endpoint=getenv('PACKMAN_API_ENDPOINT');
$package_id=getenv('PACKAGE_ID');

$new_package_json=$argv[1];
$deps_file=$argv[2];
$new_deps=file($deps_file, FILE_IGNORE_NEW_LINES );
$new_deps_json='';
for ($i=0;$i < count($new_deps); $i++){
	$new_deps_json.="\t".'"'.$new_deps[$i].'":' . '"*"';
	$mydata=array(
		'package_id'=> 46,
		'package_type' => 3,
		'env' => 'NodeJS',
		'dep_type' => 1,
		'depends_on_package' => trim($new_deps[$i]),
		'depends_on_package_version' => '*',
		'needed_files' => '',
	);
	makeRequest('/packagedeps/add', $mydata, $api_user, $api_key, $endpoint);
	if ($i < (count($new_deps)-1)){
		$new_deps_json.= ",";
	}
	$new_deps_json.=  "\n";
}
$new_package_json_contents=file_get_contents($new_package_json);
$new_package_json_contents = str_replace('"@@DEPS@@" : ""', $new_deps_json, $new_package_json_contents);
file_put_contents($new_package_json,$new_package_json_contents);
?>
