<html>
<head>
    <title>JSP Request Flow</title>
</head>
<body>

    <h1>User Details</h1>

    <%
        int id = 101;
        String name = "John";
        String email = "john@gmail.com";
    %>

    <p>ID: <%= id %></p>
    <p>Name: <%= name %></p>
    <p>Email: <%= email %></p>

</body>
</html>