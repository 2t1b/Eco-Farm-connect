<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $firstName = $_POST['firstName'];
  $lastName = $_POST['lastName'];
  $username = $_POST['username'];
  $password = $_POST['password'];
  $country = $_POST['country'];
  $town = $_POST['town'];
  $phoneNumber = $_POST['phoneNumber'];

 
  if (empty($firstName) || empty($lastName) || empty($username) || empty($password) || empty($country) || empty($town) || empty($phoneNumber)) {
    echo "<p style='color: red;'>Please fill in all fields!</p>";

   
    echo "<script>
      setTimeout(function() {
        window.location.href = 'https://eco-farm-connect--sm2t1b.repl.co/user'; 
      }, 5000); 
    </script>";
    exit;
  }

  $data = "First Name: $firstName\n"
          . "Last Name: $lastName\n"
          . "Username: $username\n"
          . "Password: $password\n"
          . "Country: $country\n"
          . "Town: $town\n"
          . "Phone Number: $phoneNumber\n";


  $directory = 'user_profiles';
  if (!is_dir($directory)) {
    mkdir($directory);
  }

  $timestamp = time();
  $filename = $directory . '/' . 'form_data_' . $timestamp . '.txt';


  file_put_contents($filename, $data, FILE_APPEND);

  
  echo "<p style='color: green;'>Successfully registered!</p>";

 
  echo "<script>
    setTimeout(function() {
      window.location.href = 'https://eco-farm-connect--sm2t1b.repl.co/user'; 
    }, 5000); 
  </script>";
}
?>