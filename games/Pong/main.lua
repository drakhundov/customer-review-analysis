push = require "push"
suit = require "suit"
Class = require "class"

require "StateMachine"
require "states/BaseState"
require "states/PlayState"
require "states/MenuState"
require "states/StartState"
require "states/ServeState"
require "states/WinState"

require "Paddle"
require "Ball"

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 576

VIRTUAL_WIDTH = 345
VIRTUAL_HEIGHT = 194

WINNING_POINTS = 10 -- TODO: Add an option in the Menu State.

love.is_pressed = {}

function love.load()
    love.window.setTitle("Pong")
    -- Use old-school pixel graphics.
    love.graphics.setDefaultFilter("nearest", "nearest")
    push:setupScreen(
        VIRTUAL_WIDTH,
        VIRTUAL_HEIGHT,
        WINDOW_WIDTH,
        WINDOW_HEIGHT,
        {
            fullscreen = false,
            resizable = true,
            vsync = true
        }
    )
    -- Functions are used so that every time a new state object is returned.
    gStateMachine =
        StateMachine {
        menu = function()
            return MenuState()
        end,
        start = function()
            return StartState()
        end,
        play = function()
            return PlayState()
        end,
        serve = function()
            return ServeState()
        end,
        win = function()
            return WinState()
        end
    }
    math.randomseed(os.time())
    -- Assets.
    gFonts = {
        msg = love.graphics.newFont("assets/font.ttf", 8),
        score = love.graphics.newFont("assets/font.ttf", 32),
        param = love.graphics.newFont("assets/font.ttf", 64), -- Font for menu parameters.
        option = love.graphics.newFont("assets/font.ttf", 48) -- Font for menu options.
    }
    -- static - load file into memory
    -- stream - stream file from memory
    gSounds = {
        paddle_hit = love.audio.newSource("assets/sounds/paddle_hit.wav", "static"),
        score = love.audio.newSource("assets/sounds/score.wav", "static"),
        wall_hit = love.audio.newSource("assets/sounds/wall_hit.wav", "static")
    }
    gStateMachine:change("menu")
end

function love.update(dt)
    gStateMachine:update(dt)
    -- Reset the list of pressed keys.
    love.is_pressed = {}
end

function love.draw()
    -- -- Start rendering at virtual resolution.
    if not gStateMachine.current.no_push then
        push:apply("start")
    end
    love.graphics.clear(40 / 255, 45 / 255, 52 / 255, 255 / 255)
    gStateMachine:render()
    -- End rendering at virtual resolution.
    if not gStateMachine.current.no_push then
        push:apply("end")
    end
end

function love.keypressed(key)
    love.is_pressed[key] = true
    suit.keypressed(key)
    if key == "escape" or key == "q" then
        love.event.quit()
    end
end

function love.textinput(txt)
    suit.textinput(txt)
end

function love.resize(w, h)
    push:resize(w, h)
end
