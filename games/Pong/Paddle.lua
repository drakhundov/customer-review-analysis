Paddle = Class{}

PADDLE_SPEED = 200  -- TODO: Add an option in the Menu State.

PADDLE_SIZE_BY_DIFFICULTY = {
    {10, 50},
    {5, 25},
    {5, 15}
}

function Paddle:init(x, y, width, height)
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.score = 0
    self.dy = 0
end

function Paddle:update(dt)
    new_y = self.y + self.dy * dt
    if self.dy < 0 then -- upward
        self.y = math.max(0, new_y)
    elseif self.dy > 0 then -- downward
        self.y = math.min(new_y, VIRTUAL_HEIGHT - self.height)
    end
end

function Paddle:render()
    love.graphics.rectangle('fill', self.x, self.y, self.width, self.height)
end
