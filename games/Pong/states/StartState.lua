StartState = Class {__includes = BaseState}

function StartState:enter(params)
    self.lvl = params.lvl
    if type(params.useAI) == string then
        self.useAI = params.useAI == "ON" and true or false
    else
        self.useAI = params.useAI
    end
    self.paddle_width, self.paddle_height = unpack(PADDLE_SIZE_BY_DIFFICULTY[self.lvl])
    -- Players.
    self.p1 = Paddle(
        10,
        (VIRTUAL_HEIGHT - self.paddle_height) / 2,
        self.paddle_width,
        self.paddle_height)
    self.p2 = Paddle(
        VIRTUAL_WIDTH - self.paddle_width - 10,
        (VIRTUAL_HEIGHT - self.paddle_height) / 2,
        self.paddle_width,
        self.paddle_height)
    self.ball = Ball(
        (VIRTUAL_WIDTH - BALL_SIZE) / 2,
        (VIRTUAL_HEIGHT - BALL_SIZE) / 2)
end

function StartState:update(dt)
    if love.is_pressed["space"] then
        gStateMachine:change("play", {
            p1 = self.p1,
            p2 = self.p2,
            ball = self.ball,
            useAI = self.useAI,
            lvl = self.lvl
        })
    end
end

function StartState:render(dt)
    love.graphics.setFont(gFonts["msg"])
    love.graphics.printf("Press SPACE to start", 0, 20, VIRTUAL_WIDTH, "center")
    love.graphics.setFont(gFonts["score"])
    love.graphics.printf(tostring(self.p1.score), 0, 20, VIRTUAL_WIDTH / 2, "center")
    love.graphics.printf(tostring(self.p2.score), VIRTUAL_WIDTH / 2, 20, VIRTUAL_WIDTH / 2, "center")
    self.p1:render()
    self.p2:render()
    self.ball:render()
end
