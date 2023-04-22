// Set the duration of the quiz (in minutes)
const duration = 120; // 2 hours

// Calculate the number of questions based on the duration
const numQuestions = Math.floor(duration / 1.5);

// Define an array of questions
const questions = [
  {
    question: "What is the capital of France?",
    options: ["Paris", "London", "Berlin", "Rome"],
    answerIndex: 0
  },
  {
    question: "What is the tallest mountain in the world?",
    options: ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
    answerIndex: 0
  },
  {
    question: "What is the currency of Japan?",
    options: ["Yen", "Dollar", "Euro", "Pound"],
    answerIndex: 0
  },
  // Add more questions here...
];

// Select numQuestions randomly from the questions array
const selectedQuestions = [];
while (selectedQuestions.length < numQuestions) {
  const randomQuestion = questions[Math.floor(Math.random() * questions.length)];
  if (!selectedQuestions.includes(randomQuestion)) {
    selectedQuestions.push(randomQuestion);
  }
}

// Generate the quiz interface
const quizContainer = document.createElement("div");
quizContainer.id = "quiz-container";
document.body.appendChild(quizContainer);

selectedQuestions.forEach((question, index) => {
  // Create the question container
  const questionContainer = document.createElement("div");
  questionContainer.className = "question-container";
  quizContainer.appendChild(questionContainer);

  // Create the question text
  const questionText = document.createElement("div");
  questionText.className = "question-text";
  questionText.textContent = `${index + 1}. ${question.question}`;
  questionContainer.appendChild(questionText);

  // Create the options container
  const optionsContainer = document.createElement("div");
  optionsContainer.className = "options-container";
  questionContainer.appendChild(optionsContainer);

  // Create the radio buttons for each option
  question.options.forEach((option, optionIndex) => {
    const optionLabel = document.createElement("label");
    optionsContainer.appendChild(optionLabel);

    const optionRadio = document.createElement("input");
    optionRadio.type = "radio";
    optionRadio.name = `question-${index}`;
    optionRadio.value = optionIndex;
    optionLabel.appendChild(optionRadio);

    const optionText = document.createElement("span");
    optionText.textContent = option;
    optionLabel.appendChild(optionText);
  });
});

// Create the submit button
const submitButton = document.createElement("button");
submitButton.textContent = "Submit";
quizContainer.appendChild(submitButton);

// Add event listener to submit button
submitButton.addEventListener("click", () => {
  // Evaluate the user's answers and display the score
  let score = 0;
  selectedQuestions.forEach((question, index) => {
    const selectedOption = document.querySelector(`input[name="question-${index}"]:checked`);
    if (selectedOption && parseInt(selectedOption.value) === question.answerIndex) {
      score++;
    }
  });

  alert(`Your score is ${score}/${numQuestions}`);
});
