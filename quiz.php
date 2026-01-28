
<?php
$category = $_GET['category'];
$difficulty = $_GET['difficulty'];
?>
<!DOCTYPE html>
<html>
<head>
    <title>Quiz</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="quiz-container">
        <h2><?php echo ucfirst($category)." - ".ucfirst($difficulty); ?></h2>
        <div id="timer">Time: <span id="time">15</span>s</div>
        <div id="question"></div>
        <div id="options"></div>
        <div id="warning" class="warning"></div>
        <button id="nextBtn">Next</button>
    </div>

    <script>
        const CATEGORY = "<?php echo strtolower(trim($category)); ?>";
        const DIFFICULTY = "<?php echo strtolower(trim($difficulty)); ?>";
    </script>

    <script src="quiz.js"></script>
</body>
</html>
