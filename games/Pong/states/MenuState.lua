MenuState = Class {__includes = BaseState}

BUTTON_FG = {195/255, 200/255, 212/255}
LABEL_FG = {255/255, 255/255, 255/255}

NORMAL_BUTTON_BG = suit.theme.color.normal.bg
SELECTED_BUTTON_BG = {235/255, 64/255, 52/255}

BG_COLOR = {12/255, 13/255, 12/255}

function MenuState:enter()
    self.no_push = true
    -- There are two parameters: difficulty and useAI.
    -- Difficulty is a number from 0 to 1, where 1 is the hardest mode.
    self.params = {
        {
            name = "Difficulty",
            identifier = "lvl",
            type = "buttons",
            options = {
                {name = "Low"},
                {name = "Medium"},
                {name = "High"}
            },
            hit_func = function(param_no, option_no)
                self.params[param_no].selected = option_no
                gSounds["paddle_hit"]:play()
            end,
            selected = 1
        },
        {
            name = "AI",
            identifier = "useAI",
            type = "buttons",
            use_option_name = true, -- Pass "ON" or "OFF" instead of a number.
            options = {
                {name = "OFF"},
                {name = "ON"}
            },
            hit_func = function(param_no, option_no)
                self.params[param_no].selected = option_no
                gSounds["paddle_hit"]:play()
            end,
            selected = 1
        }
    }
    self.paramTextHeight = gFonts["param"]:getHeight()
    self.optionTextHeight = gFonts["option"]:getHeight()
    for i, param in ipairs(self.params) do
        param.text_width = gFonts["param"]:getWidth(param.name)
        if param.options then
            for j, option in ipairs(param.options) do
                option.text_width = gFonts["option"]:getWidth(option.name)
            end
        end
    end
    self.paramOrigX = WINDOW_WIDTH / 7 -- 'x' coordniates should be the same so that parameters are perfectly aligned.
    self.paramOrigY = WINDOW_HEIGHT / 7 -- First parameter's 'y' coordinate.
    self.paramMarginY = 100 -- The amount of space to leave between parameters.
    self.optionMarginX = 30 -- The amount of space between option buttons.
    self.paramCurY = self.paramOrigY -- The 'y' coordinate of the current parameter.
    self.startBtnFont = love.graphics.newFont(32)
    self.startBtnTextWidth = self.startBtnFont:getWidth("START")
end

function MenuState:update(dt)
    for param_i, param in ipairs(self.params) do
        love.graphics.setFont(gFonts["param"])
        param.label = suit.Label(
            param.name,
            {fg=LABEL_FG},
            self.paramOrigX,
            self.paramCurY
        )
        if param.type == "buttons" then
            love.graphics.setFont(gFonts["option"])
            local buttonCurX =
                self.paramOrigX
                + param.text_width
                + self.optionMarginX * 2
            for btn_i, btn in ipairs(param.options) do
                local button_bg
                if btn_i == param.selected then
                    button_bg = SELECTED_BUTTON_BG
                else
                    button_bg = NORMAL_BUTTON_BG
                end
                btn.instance = suit.Button(
                    btn.name,
                    {fg = BUTTON_FG, bg = button_bg},
                    buttonCurX,
                    self.paramCurY + self.optionTextHeight / 4
                )
                if btn.instance.hit then
                    param.hit_func(param_i, btn_i)
                end
                buttonCurX = buttonCurX + btn.text_width + self.optionMarginX
            end
        end
        self.paramCurY = self.paramCurY + self.paramTextHeight + self.paramMarginY
    end
    start_btn = suit.Button("START", {fg=BUTTON_FG, bg=NORMAL_BUTTON_BG}, (WINDOW_WIDTH - self.startBtnTextWidth - 80)/2, self.paramCurY + 30)
    if start_btn.hit then
        args = {}
        for param_i, param in ipairs(self.params) do
            if param.use_option_name then
                args[param.identifier] = param.options[param.selected].name
            else
                args[param.identifier] = param.selected
            end
        end
        gSounds["score"]:play()
        gStateMachine:change("start", args)
    end
    self.paramCurY = self.paramOrigY
end

function MenuState:render()
    love.graphics.clear(unpack(BG_COLOR))
    suit:draw()
end
