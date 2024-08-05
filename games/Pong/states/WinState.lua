WinState = Class {__includes = BaseState}

function WinState:enter(params)
    self.winningPlayer = params.winningPlayer
    self.p1_score = params.p1_score
    self.p2_score = params.p2_score
    -- Save parameters in case another game is needed to start.
    self.lvl = params.lvl
    self.useAI = params.useAI
end

function WinState:update(dt)
    if love.is_pressed["space"] then
        gStateMachine:change("start", {
            lvl = self.lvl,
            useAI = self.useAI
        })
    end
end

function WinState:render()
    love.graphics.setFont(fonts["msg"])
    love.graphics.printf("Player " .. tostring(self.winningPlayer) .. " wins\nPress SPACE to restart", 0, 20, VIRTUAL_WIDTH, "center")
    love.graphics.setFont(fonts["score"])
    love.graphics.printf(tostring(self.p1_score), 0, 20, VIRTUAL_WIDTH / 2, "center")
    love.graphics.printf(tostring(self.p2_score), VIRTUAL_WIDTH / 2, 20, VIRTUAL_WIDTH / 2, "center")
end
