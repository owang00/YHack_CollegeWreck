<?php
	# ini_set('display_errors', 1);

	if(isset($_POST['SubmitButton'])) { //check if form was submitted
		$GPA = $_POST['GPA']; //get input text
		$message = "Success! Your GPA is : ".$GPA; 
		$testType = $_POST['testType'];
		$message1 = "Success! The type of testType : ".$testType;
		$score = $_POST['score'];
		$message2 = "Success! Your score is : ".$score;
		
		
		/*
		if(true) {
			$testMessage = "Reached this step. Executing python file for FFEMPG.";
			
			$output = shell_exec('python3 downloader.py '.escapeshellarg($ESN).' '.escapeshellarg($numberOfFrame).' '.escapeshellarg($start).' '.escapeshellarg($end).' '.escapeshellarg($timelapseType).' '.escapeshellarg($frameType) );
		}*/

		header("Location:https://owang00.github.io/results.html");
	}
?>
