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
	}
?>

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Video Maker</title>
  </head>

  <body>
  	<div class="container">
  		
  		<div class="row form-group">
        	<div class="col-md-4 offset-4">
	        	<div class="app-title">
		        	<p></p>
		            <h1>Video Maker</h1>
	        	</div>
	        </div>
	    </div>
      
    	<form class="form-horizontal" role="form" method="POST">
	        <div class="row form-group">
	        	<div class="col-md-6">
		            <label for="ESN" class="mt-3">Camera ESN:</label>
		            <input class="form-control 1" id="ESN" placeholder="ESN" name="ESN">
	        	</div>
	        	<div class="col-md-6">
		            <label for="frames" class="mt-3">Video Length:</label>
		            <input class="form-control 2" id="frames" placeholder="Number of Frames" name="numFrames">
		        </div>
	        </div>

	        <div class="row form-group">
	        	<div class="col-md-6">
		            <label for="start" class="mt-3">Start Time:</label>
		            <input class="form-control 3" id="start" placeholder="Enter time in the format of YYYYMMDDhhmmss.nnn" name="start">
		        </div>
	        	<div class="col-md-6">
		            <label for="end" class="mt-3">End Time:</label>
		            <input class="form-control 4" id="end" placeholder="Enter time in the format of YYYYMMDDhhmmss.nnn" name="end">
		        </div>
	        </div>

	        <div class="row form-group">
	        	<div class="col-md-2">
		            <select class="form-control" name="timeType">
			            <option selected>Timelapse Type:</option>
			            <option value="Evenly">Frames evenly spread over the time period</option>
			            <option value="Movement">Frames based on movement</option>
		            </select>
		        </div>
	        	<div class="col-md-2">
		            <select class="form-control" name="frameType">
			            <option selected>Frame Type:</option>
			            <option value="Thumbnail">Thumbnail</option>
			            <option value="Preview">Preview</option>
			            <option value="All">All</option>
		            </select>
		        </div>
	        </div>

	        <div class="row">
	        	<div class="offset-11 mt-5">
		            <input type="submit" value="Submit" name="SubmitButton" class="btn btn-primary">
		        </div>
	        </div>
    	</form>

		<?php echo $message; ?> <br>
		<?php echo $message1; ?> <br>
		<?php echo $message2; ?> <br>
		<?php echo $message3; ?> <br>
		<?php echo $message4; ?> <br>
		<?php echo $message5; ?> <br>
		<?php echo $testMessage; ?> <br>
		<?php echo $output; ?> <br>

    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
	</body>
</html>