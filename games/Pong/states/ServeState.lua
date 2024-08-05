ServeState = Class{__includes = BaseState}

function ServeState:enter(params)
    self.servingPlayer = params.servingPlayer
    self.p1 = params.p1
    self.p2 = params.p2
    self.ball = params.ball
    self.lvl = params.lvl
    self.useAI = params.useAI
end

function ServeState:update(dt)
    if not self.useAI then
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
    if love.is_pressed["space"] then
        self.ball:generatedirX(self.servingPlayer == 1 and 1 or -1)
        self.ball:generatedirY(0)
        gStateMachine:change("play", {
            p1=self.p1,
            p2=self.p2,
            ball=self.ball,
            lvl=self.lvl,
            useAI=self.useAI
        })
    end
    self.p1:update(dt)
    self.p2:update(dt)
end

function ServeState:render()
    love.graphics.setFont(gFonts["msg"])
    love.graphics.printf("Player " .. tostring(self.servingPlayer) .. " serves", 0, 20, VIRTUAL_WIDTH, "center")
    love.graphics.setFont(gFonts["score"])
    love.graphics.printf(tostring(self.p1.score), 0, 20, VIRTUAL_WIDTH / 2, "center")
    love.graphics.printf(tostring(self.p2.score), VIRTUAL_WIDTH / 2, 20, VIRTUAL_WIDTH / 2, "center")
    self.p1:render()
    self.p2:render()
    self.ball:render()
end
