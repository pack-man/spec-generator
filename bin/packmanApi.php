<?php
function makeRequest($route, $data, $api_user, $api_key, $endpoint)
{
	$data_string = json_encode($data);                                                                                   
															     
	$ch = curl_init($endpoint);                                                                      
	curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");                                                                     
	curl_setopt($ch, CURLOPT_POSTFIELDS, $data_string);                                                                  
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);                                                                      
	curl_setopt($ch, CURLOPT_HTTPHEADER, array(                                                                          
		'Content-Type: application/json',
		"X-API-ID: $api_user",
		"X-API-PRIVATE-KEY: $api_key",
		"X-API-ROUTE: $route",
		'Content-Length: ' . strlen($data_string))
	);                                                                                                                   
															     
	$result = curl_exec($ch);
}


?>
