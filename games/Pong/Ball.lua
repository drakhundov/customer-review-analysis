Ball = Class{}

BALL_SIZE = 4

BALL_SPEED_MIN = 100
BALL_SPEED_MAX = 150

function Ball:init(x, y)
    self.orig = {
        x = x,
        y = y
    }

    self:reset()
end

function Ball:reset()
    self.x = self.orig['x']
    self.y = self.orig['y']

    self:generatedirX(0)
    self:generatedirY(0)
end

function Ball:generatedirY(coef)
    if coef == 0 then
        coef = math.random(2) == 1 and -1 or 1
    end
    self.dy = coef * math.random(BALL_SPEED_MIN, BALL_SPEED_MAX)
end

function Ball:generatedirX(coef)
    if coef == 0 then
        coef = math.random(2) == 1 and -1 or 1
    end
    self.dx = coef * math.random(BALL_SPEED_MIN, BALL_SPEED_MAX)
end

function Ball:update(dt)
    self.x = self.x + self.dx * dt
    self.y = self.y + self.dy * dt
end

function Ball:render()
    love.graphics.rectangle('fill', self.x, self.y, BALL_SIZE, BALL_SIZE)
end

function Ball:collides(paddle)
    if self.x > paddle.x + paddle.width or self.x + BALL_SIZE < paddle.x then
        return false
    end
    if self.y > paddle.y + paddle.height or self.y + BALL_SIZE < paddle.y then
        return false
    end
    return true
end
