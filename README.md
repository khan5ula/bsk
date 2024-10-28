# BSK

_BSK_ (_Bowling Score Keeper_) is an API that calculates the score of a bowling game.

Each turn of a bowling game is called a frame. A (bowling) game consists of 10 frames. A game can have up to two bonus throws.

You do not need to know more so far. The _User Stories_ section will provide further details.

## Instructions for You

- FORK this project and make sure your forked repository is PUBLIC. Then, IMPORT the forked project into PyCharm.
- You are asked to develop _BSK_ by following TDD.
- You DO NOT need to develop a GUI.
- You CANNOT change the signature of the provided methods, move the provided methods to other classes, or change the name of the provided classes. However, you CAN add fields, methods (e.g., methods called by the provided methods), or even classes (including other test classes), as long as you comply with the provided API.
- You CAN use the internet to consult Python APIs or QA sites (e.g., StackOverflow).
- You CANNOT use AI tools (e.g., ChatGPT).
- You CANNOT interact with your colleagues. Work alone and do your best!
- The _BSK_ requirements are divided into a set of USER STORIES, which serve as a to-do list (see the _User Stories_ section).
- You should be able to incrementally develop _BSK_ without an upfront comprehension of all its requirements. DO NOT read ahead and handle the requirements (specified in the user stories) one at a time in the provided order. Develop _BSK_ by starting from the first story's requirement. When a story is IMPLEMENTED, move on to the NEXT one. A story is implemented when you are confident that your program correctly implements the functionality stipulated by the story's requirement. This implies that all your test cases for that story and all the test cases for the previous stories pass. You may need to review your program as you progress toward more advanced requirements.
- Each time you end a GREEN or REFACTOR phase, COMMIT.
- If you need to handle error situations (including situations unspecified by the user stories), throw a `BowlingError`.
- At the end of the task, PUSH your forked project and fill in the following post-questionnaire: https://forms.gle/mEQJYurvsqzZaAfr7.

## API Usage

Take some minutes to understand, in broad terms, how the API works. If you do not fully understand the API, do not worry because further details will be given later in the _User Stories_ section. A typical API usage follows.

```python
# Initialize an empty bowling game.
game = BowlingGame()
# Add 10 frames to the bowling game.
game.add_frame(Frame(1, 5))
game.add_frame(Frame(2, 5))
game.add_frame(Frame(1, 1))
game.add_frame(Frame(4, 2))
game.add_frame(Frame(8, 0))
game.add_frame(Frame(2, 3))
game.add_frame(Frame(1, 3))
game.add_frame(Frame(1, 6))
game.add_frame(Frame(2, 0))
game.add_frame(Frame(10, 0))
# Set the first bonus throw (if any).
game.set_first_bonus_throw(4)
# Set the second bonus throw (if any).
game.set_second_bonus_throw(5)
# Compute the score of the game.
score = game.calculate_score()
```

See the provided source files to improve your understanding of the API before starting to implement the user stories.

## User Stories

Remember to read and implement the user stories once at a time (in the provided order). Therefore, do not read the next user story, if the current one is not implemented yet.

### User Story 1 -- Game

A single game consists of 10 frames.

**Requirement:**

- Implement `BowlingGame.__init__(self)` and `BowlingGame.add_frame(self, frame: Frame) -> None` to define a game consisting of 10 frames.
- Implement `BowlingGame.get_frame_at(self, i: int) -> Frame` to get the i-th frame of the game. Note that the index ranges from 0 to 9. This implies that 0 allows returning the first frame, 1 allows returning the second frame, and so on.

**Example:**

- The sequence of frames [1, 5] [3, 6] [7, 2] [3, 6] [4, 4] [5, 3] [3, 3] [4, 5] [8, 1] [2, 6] represents a game. [1, 5] is the first frame, [3, 6] is the second frame, and so on. Note that you can reuse this game from now on to represent different scenarios by modifying only a few frames each time.

### User Story 2 -- Game Score

The score of a bowling game is the sum of the individual scores of its frames.

**Requirement:**

- Implement `BowlingGame.calculate_score(self) -> int` to calculate the score of a game.

**Example:**

- The score of the game [1, 5] [3, 6] [7, 2] [3, 6] [4, 4] [5, 3] [3, 3] [4, 5] [8, 1] [2, 6] is 81.

### User Story 3 -- Spare

A frame is called a spare when all 10 pins are knocked down in the two throws of the frame. The score of a spare frame is 10 plus a bonus equal to the value of the first throw of the subsequent frame.

**Requirement:**

- Implement `BowlingGame.calculate_score(self) -> int` to calculate the score of a game containing a spare frame.

**Example:**

- Suppose that [1, 9] and [3, 6] are consecutive frames; then the first frame is spare and its score is equal to 10+3=13. The game [1, 9] [3, 6] [7, 2] [3, 6] [4, 4] [5, 3] [3, 3] [4, 5] [8, 1] [2, 6] (containing a spare frame) has a score of 88.

### User Story 4 -- Strike

A frame is called a strike if all 10 pins are knocked down in the first throw of the frame. In this case, there is no second throw (i.e., its value is 0). The score of a strike frame is 10 plus a bonus equal to the sum of the next two throws of the subsequent frame.

**Requirement:**

- Implement `BowlingGame.calculate_score(self) -> int` to calculate the score of a game containing a strike frame.

**Example:** Suppose that [10, 0] and [3, 6] are consecutive frames; then the first frame is strike and its score is equal to 10+3+6=19. The game [10, 0] [3, 6] [7, 2] [3, 6] [4, 4] [5, 3] [3, 3] [4, 5] [8, 1] [2, 6] (containing a strike frame) has a score of 94.

### User Story 5 -- Strike and Spare

A strike frame can be followed by a spare frame. When this happens, the score of the strike frame is not affected by the score of the spare frame.

**Requirement:**

- Implement `BowlingGame.calculate_score(self) -> int` to calculate the score of a game containing a strike frame followed by a spare frame.

**Example:**

- Suppose that [10, 0] [4, 6] [7, 2] are consecutive frames; then the score of the strike frame is 10+4+6=20 while the score of the spare frame is 4+6+7=17. The game [10,0] [4,6] [7, 2] [3, 6] [4, 4] [5, 3] [3, 3] [4, 5] [8, 1] [2, 6] has a score of 103.

### User Story 6 -- Multiple Strikes

A strike frame can be followed by another strike frame. When this happens, the computation of the score of the first strike frame requires the values of the throws from the two subsequent frames.

**Requirement:**

- Implement `BowlingGame.calculate_score(self) -> int` to calculate the score of a game containing a strike frame followed by another strike frame.

**Example:**

- Suppose that [10, 0] [10, 0] [7, 2] are consecutive frames; then the score of the first strike frame is 10+10+7=27 while the score of the second strike frame is 10+7+2=19. The game [10, 0] [10, 0] [7, 2] [3, 6] [4, 4] [5, 3] [3, 3] [4, 5] [8, 1] [2, 6] has a score of 112.

### User Story 7 -- Multiple Spares

A spare frame can be followed by another spare frame. When this happens, the score of the first spare frame is not affected by the score of the second spare frame.

**Requirement:**

- Implement `BowlingGame.calculate_score(self) -> int` to calculate the score of a game containing a spare frame followed by another spare frame.

**Example:**

- Suppose that [8, 2] [5, 5] [7, 2] are consecutive frames; then the score of the first spare frame is 8+2+5=15 while the score of the second spare frame is 5+5+7=17. The game [8, 2] [5, 5] [7, 2] [3, 6] [4, 4] [5, 3] [3, 3] [4, 5] [8, 1] [2, 6] has a score of 98.

### User Story 8 -- Spare as the Last Frame

When the last frame of a game is spare, the player will be given a bonus throw. However, this bonus throw does not belong to a regular frame. That is, the bonus throw is used to calculate the score of the last spare frame.

**Requirement:**

- Implement `BowlingGame.set_first_bonus_throw(self, bonus_throw: int) -> None:` to set a bonus throw.
- Implement `BowlingGame.calculate_score(self) -> int` to calculate the score of a game when the last frame is spare.

**Example:**

- The last frame in the game [1, 5] [3, 6] [7, 2] [3, 6] [4, 4] [5, 3] [3, 3] [4, 5] [8, 1] [2, 8] is spare. If the bonus throw is [7], the last frame has a score of 2+8+7 = 17. The game has a score of 90.

### User Story 9 -- Strike as the Last Frame

When the last frame of a game is strike, the player will be given two bonus throws. However, these bonus throws do not belong to a regular frame. That is, the bonus throws are used to calculate the score of the last strike frame.

**Requirement:**

- Implement `BowlingGame.set_second_bonus_throw(self, bonus_throw: int) -> None:` to set the second bonus throw.
- Implement `BowlingGame.calculate_score(self) -> int` to calculate the score of a game when the last frame is strike.

**Example:**

- The last frame in the game [1, 5] [3, 6] [7, 2] [3, 6] [4, 4] [5, 3] [3, 3] [4, 5] [8, 1] [10, 0] is strike. If the bonus throws are [7, 2], the last frame has a score of 10+7+2=19. The game has a score of 92.

### User Story 10 -- Best Score

A perfect game consists of all strikes (i.e., a total of 12 strikes, one for each regular frame plus two strikes as the bonus throws) and has a score of 300. Note that the computation of the score of the ninth strike frame requires the values of the first throw of the tenth frame and the first bonus throw.

**Requirement:**

- Implement `BowlingGame.calculate_score(self) -> int` to calculate the score of a perfect game.

**Example:**

- The game [10, 0] [10, 0] [10, 0] [10, 0] [10, 0] [10, 0] [10, 0] [10, 0] [10, 0] [10, 0] with [10, 10] as the bonus throws has a score of 300.
