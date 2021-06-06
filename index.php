<?php
	$timestamp = "";
	$conn = mysqli_connect("remotemysql.com", "hwW4R6cA0s", "9bVe4xsxvX", "hwW4R6cA0s");
	$sql = "SELECT * FROM SecuRest order by id desc";
	$result = mysqli_query($conn, $sql);
	if (mysqli_num_rows($result) > 0) {
    while($row = mysqli_fetch_assoc($result)) {
        	$timestamp = $row['time'];
        	$id = $row['id'];
          $link = $row['link'];
    }
  }
?>
