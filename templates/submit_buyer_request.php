<!DOCTYPE html>
<html>
<head>
  <title>User Dashboard</title>
  <style>
    
    body {
      background-image: url('https://eco-farm-connect--sm2t1b.repl.co/static/truck.jpg');
      background-size: cover;
      background-repeat: no-repeat;
    }
    h1 {
      color: white;
      font-size: 36px;
      letter-spacing: 2px;
      margin: 10px;
      text-align: center;
      text-transform: uppercase;
      text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    .dashboard {
      display: flex;
      flex-direction: column;
      align-items: center; 
      margin-top: 50px;
      padding: 20px;
    }
    .button-container {
      display: flex;
      gap: 10px; 
      margin-bottom: 10px;
    }
    .logout-button,
    .post-button {
      margin-bottom: 10px;
      background-color: green;
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      text-decoration: none;
      font-size: 16px;
      cursor: pointer;
    }
    .recent-posts {
      background-color: rgba(255, 255, 255, 0.8); 
      padding: 80px;
      margin-top: 80px;
      width: 1000px
    }
    .post {
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <div class="dashboard">
    <h1>ECO- FARM-CONNECT</h1>
    <div class="button-container">
      <a class="nav-link btn logout-button" href="https://eco-farm-connect--sm2t1b.repl.co/">Logout</a>
      <a class="nav-link btn post-button" href="https://eco-farm-connect--sm2t1b.repl.co/buyer">Create Post</a>
    </div>
    
    <div class="recent-posts">
      <h2>Request board</h2>
      <table>
        <thead>
          <tr>
            <th>Product</th>
            <th>Requirement</th>
            <th>Price</th>
            <th>Contact Number</th>
          </tr>
        </thead>
        <tbody>
          <?php
            $file = fopen("data/buyer_requests.csv", "r");
            while (($data = fgetcsv($file)) !== FALSE) {
              $product = $data[0];
              $requirement = $data[1];
              $price = $data[2];
              $contact = $data[3];
          ?>
            <tr>
              <td><?php echo $product; ?></td>
              <td><?php echo $requirement; ?></td>
              <td><?php echo $price; ?></td>
              <td><?php echo $contact; ?></td>
            </tr>
          <?php
            }
            fclose($file);
          ?>
        </tbody>
      </table>
    </div>
  </div>

  <script>
    function logout() {
    
      console.log("Logout clicked");
    }

    function createPost() {
     
      console.log("Create post clicked");
    }
  </script>
</body>
</html>