<!DOCTYPE html>
<html>
<head>
    <title>PHP Form Validation</title>
</head>
<body>

<h2>User Registration</h2>

<form method="post">

    Name:
    <input type="text" name="name">
    <br><br>

    Email:
    <input type="text" name="email">
    <br><br>

    Password:
    <input type="password" name="password">
    <br><br>

    <input type="submit" name="submit" value="Submit">

</form>

<?php

if (isset($_POST["submit"])) {

    $name = trim($_POST["name"]);
    $email = trim($_POST["email"]);
    $password = $_POST["password"];

    $errors = array();

    // Validate Name
    if (empty($name)) {
        $errors[] = "Name is required";
    }

    // Validate Email
    if (empty($email)) {
        $errors[] = "Email is required";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Enter a valid email address";
    }

    // Validate Password
    if (empty($password)) {
        $errors[] = "Password is required";
    } elseif (strlen($password) < 6) {
        $errors[] = "Password is too short";
    }

    // Display result
    if (!empty($errors)) {

        echo "<h3>Errors:</h3>";

        foreach ($errors as $error) {
            echo "<p>$error</p>";
        }

    } else {

        echo "<h3>Form submitted successfully</h3>";
        echo "<p>Welcome, " . htmlspecialchars($name) . "</p>";
    }
}

?>

</body>
</html>