<?php
	#if(isset($_POST['SubmitButton'])) { //check if form was submitted
		$GPA = $_POST['GPA']; //get input text
		$message = "Success! Your GPA is : ".$GPA; 
		$testType = $_POST['testType'];
		$message1 = "Success! The type of testType : ".$testType;
		$score = $_POST['score'];
		$message2 = "Success! Your score is : ".$score;

		$output = shell_exec('python3 parser.py '.escapeshellarg($GPA).' '.escapeshellarg($testType).' '.escapeshellarg($score));
		header("Location:/results.html");
	#}
?>
