PlayState = Class {__includes = BaseState}

function PlayState:enter(params)
    self.p1 = params.p1
    self.p2 = params.p2
    self.ball = params.ball
    self.useAI = params.useAI
    self.lvl = params.lvl
    if self.useAI then
        -- Speed of AI will be reduced to make movements smoother.
        -- Every time the ball bounces off, the speed factor will be reduced (AI will move slower).
        self.ai_speed_factor = 0.65
        self.ai_speed_reduction_factor = 0.98
    end
end

function PlayState:update(dt)
    if self.useAI and self.ball.x < VIRTUAL_WIDTH / 2 + 25 then
        local dist = self.ball.y - self.p1.y
        if dist > 0 then
            self.p1.dy = PADDLE_SPEED * self.ai_speed_factor
        elseif dist < 0 then
            self.p1.dy = -PADDLE_SPEED * self.ai_speed_factor
        end
    else
        if love.keyboard.isDown("w") then
            self.p1.dy = -PADDLE_SPEED
        elseif love.keyboard.isDown("s") then
            self.p1.dy = PADDLE_SPEED
        else
            self.p1.dy = 0
        end
    end
    if love.keyboard.isDown("up") then
        self.p2.dy = -PADDLE_SPEED
    elseif love.keyboard.isDown("down") then
        self.p2.dy = PADDLE_SPEED
    else
        self.p2.dy = 0
    end
    self.p1:update(dt)
    self.p2:update(dt)
    if self.ball:collides(self.p1) or self.ball:collides(self.p2) then
        gSounds["paddle_hit"]:play()
        -- To ensure collision won't be detected infinitely when it occurs on the top or the bottom of a paddle.
        -- If it occurs on the side, ball will be updated (its X coordinate will be changed) anyway.
        if self.ball.x < self.p1.x + self.p1.width or self.ball.x > self.p2.x then
            if self.ball.dx < 0 then
                self.ball.x = self.p1.x + self.p1.width + 3
            else
                if self.useAI then
                    self.ai_speed_factor = self.ai_speed_factor * self.ai_speed_reduction_factor
                end
                self.ball.x = self.p2.x - 3
            end
        end
        -- It increases speed every time.
        self.ball.dx = -self.ball.dx * 1.03
        local coef = self.ball.dy < 0 and -1 or 1
        self.ball:generatedirY(coef)
    end
    -- If the ball hits the walls.
    if self.ball.y < 0 then
        gSounds["wall_hit"]:play()
        self.ball.dy = -self.ball.dy
    elseif self.ball.y > VIRTUAL_HEIGHT - BALL_SIZE then
        gSounds["wall_hit"]:play()
        self.ball.dy = -self.ball.dy
    end
    -- If one of the players scored.
    if self.ball.x <= -BALL_SIZE then
        self.p2.score = self.p2.score + 1
        gSounds["score"]:play()
        if self.p2.score == WINNING_POINTS then
            gameStateMachine:change("win", {
                winningPlayer = 2,
                p1_score = self.p1.score,
                p2_score = self.p2.score,
                lvl = self.lvl,
                useAI = self.useAI})
        else
            self.ball:reset()
            gStateMachine:change("serve", {
                servingPlayer = 1,
                p1=self.p1,
                p2=self.p2,
                ball=self.ball,
                lvl=self.lvl,
                useAI=self.useAI})
        end
    elseif self.ball.x >= VIRTUAL_WIDTH then
        self.p1.score = self.p1.score + 1
        gSounds["score"]:play()
        if self.p1.score == WINNING_POINTS then
            gameStateMachine:change("win", {
                winningPlayer = 1,
                p1_score = self.p1.score,
                p2_score = self.p2.score,
                lvl = self.lvl,
                useAI = self.useAI})
        else
            self.ball:reset()
            gStateMachine:change("serve", {
                servingPlayer = 2,
                p1=self.p1,
                p2=self.p2,
                ball=self.ball,
                lvl=self.lvl,
                useAI=self.useAI})
        end
    end
    self.ball:update(dt)
    if love.is_pressed["space"] then
        gStateMachine:change("start", {
            lvl=self.lvl,
            useAI=self.useAI
        })
    end
end

function PlayState:render()
    love.graphics.clear(40 / 255, 45 / 255, 52 / 255, 255 / 255)
    love.graphics.setFont(gFonts["msg"])
    love.graphics.setFont(gFonts["score"])
    love.graphics.printf(tostring(self.p1.score), 0, 20, VIRTUAL_WIDTH / 2, "center")
    love.graphics.printf(tostring(self.p2.score), VIRTUAL_WIDTH / 2, 20, VIRTUAL_WIDTH / 2, "center")
    self.p1:render()
    self.p2:render()
    self.ball:render()
end
