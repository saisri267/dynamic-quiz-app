
<!DOCTYPE html>
<html>
<head>
    <title>Smart Quiz Platform</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Smart Quiz Platform</h1>
        <form action="quiz.php" method="GET">
            <label>Category</label>
            <select name="category" required>
                <option value="web">Web Technologies</option>
                <option value="network">Computer networking</option>
            </select>

            <label>Difficulty</label>
            <select name="difficulty" required>
                <option value="easy">Easy</option>
                <option value="medium">Medium</option>
                <option value="hard">Hard</option>
            </select>

            <button type="submit">Start Quiz</button>
        </form>
    </div>
</body>
</html>
