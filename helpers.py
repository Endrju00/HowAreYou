
# Screens
screen_helper = """
<MyTile@SmartTileWithLabel>
    size_hint_y: None
    height: "610dp"
    box_color: (0, 0, 0, 0)

<MenuScreen>:
    name: 'menu'
    on_enter:
        app.sync_icons_labels()
        
    MDLabel:
        id: sign
        text: "Andrzej Kapczyński @2021"
        halign: "center"
        font_style: "Caption"
        font_size: "12dp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.03}
    
    MDTabs:
        Tab:
            title: " WEATHER INFO"
            icon: 'sunglasses'
            
            MDIcon:
                id: weather_icon
                icon: 'white-balance-sunny'
                halign: 'center'
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                font_size: "135sp"
                pos_hint: {'center_x': 0.11, 'center_y': 0.82}
            
            MDLabel:
                id: weather_label1
                text: '22°C'
                halign: 'center'
                font_size: "32sp"
                pos_hint: {'center_x': 0.25, 'center_y': 0.84}
            
            MDLabel:
                id: weather_label2
                text: '22°C'
                halign: 'center'
                font_size: "20sp"
                pos_hint: {'center_x': 0.235, 'center_y': 0.79}
            
            MDLabel:
                id: hello_label
                text: 'Hello Andrew, how are you?'
                halign: 'center'
                font_size: "30sp"
                pos_hint: {'center_x': 0.65, 'center_y': 0.8}
            
            MDIcon:
                id: sunrise_icon
                icon: 'weather-sunset-up'
                halign: 'center'
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                font_size: "110sp"
                pos_hint: {'center_x': 0.1, 'center_y': 0.5}
                
            MDLabel:
                id: sunrise_label
                text: '6:26:53'
                halign: 'center'
                font_size: "32sp"
                pos_hint: {'center_x': 0.25, 'center_y': 0.5}
                
            MDIcon:
                id: sunset_icon
                icon: 'weather-sunset-down'
                halign: 'center'
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                font_size: "110sp"
                pos_hint: {'center_x': 0.1, 'center_y': 0.25}
            
            MDLabel:
                id: sunset_label
                text: '19:22:27'
                halign: 'center'
                font_size: "32sp"
                pos_hint: {'center_x': 0.25, 'center_y': 0.25}
                
            MDIcon:
                id: pressure_icon
                icon: 'elevator-down'
                halign: 'center'
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                font_size: "110sp"
                pos_hint: {'center_x': 0.55, 'center_y': 0.5}
            
            MDLabel:
                id: pressure_label
                text: '1000hPa'
                halign: 'center'
                font_size: "32sp"
                pos_hint: {'center_x': 0.7, 'center_y': 0.5}
                
            MDIcon:
                id: humidity_icon
                icon: 'weather-cloudy'
                halign: 'center'
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                font_size: "110sp"
                pos_hint: {'center_x': 0.55, 'center_y': 0.25}
            
            MDLabel:
                id: humidity_label
                text: '40%'
                halign: 'center'
                font_size: "32sp"
                pos_hint: {'center_x': 0.67, 'center_y': 0.25}      
                
            MDIconButton:
                id: menu_button
                icon: 'tools'
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                user_font_size: "35sp"
                pos_hint: {'center_x': 0.92, 'center_y': 0.1}
                on_release: 
                    app.sm.current = 'settings'
            
        Tab: 
            title: " SURVEY"
            icon: 'cloud-question'
            
            MDLabel:
                id: survey_label
                text: 'You should complete the survey once a day.'
                halign: 'center'
                font_size: "30sp"
                pos_hint: {'center_x': 0.5, 'center_y': 0.85}
            
            MDTextField:
                id: feeling_rate
                hint_text: "On a scale of 1 to 10 how are you feeling?"
                helper_text: "It's important to feel good about yourself."
                text: str(app.store.get('user')['feeling'])
                helper_text_mode: "on_focus"
                icon_right: "star-face"
                icon_right_color: app.theme_cls.primary_color
                pos_hint: {'center_x': 0.5, 'center_y': 0.65}
                size_hint_x: None
                width: 400
                
            MDTextField:
                id: sleep_rate
                hint_text: "How many hours did you sleep last night?"
                helper_text: "Sleep plays a vital role in good health and well-being throughout your life."
                text: ""
                helper_text_mode: "on_focus"
                icon_right: "sleep"
                icon_right_color: app.theme_cls.primary_color
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 400
                
            MDTextField:
                id: activity_rate
                hint_text: "What was your physical activity yesterday?"
                helper_text: "Type very low, low, medium, high or very high."
                text: ""
                helper_text_mode: "on_focus"
                icon_right: "football"
                icon_right_color: app.theme_cls.primary_color
                pos_hint: {'center_x': 0.5, 'center_y': 0.35}
                size_hint_x: None
                width: 400
            
            MDRectangleFlatButton:
                id: done_button
                text: "Done"
                font_style: "Button"
                pos_hint: {'center_x': 0.5, 'center_y': 0.15}
                on_release: 
                    done_spinner.active = True
                    app.save_survey()
                    app.update_plots()
            
            MDSpinner:  
                id: done_spinner
                size_hint: None, None
                size: dp(20), dp(20)
                pos_hint: {'center_x': 0.5, 'center_y': 0.22}
                active: False
                determinate: True
            
            MDIconButton:
                id: menu_button
                icon: 'tools'
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                user_font_size: "35sp"
                pos_hint: {'center_x': 0.92, 'center_y': 0.1}
                on_release: 
                    app.sm.current = 'settings'
            
        Tab: 
            title: " STATISTICS"
            icon: 'chart-bell-curve-cumulative'
            
            ScrollView:
                MDGridLayout:
                    cols: 1
                    adaptive_height: True
                    md_bg_color: app.theme_cls.primary_color
                    #padding: dp(4), dp(4)
                    spacing: dp(4)

                    MyTile:
                        source: "plots/feel-sleep.png"
                    MyTile:
                        source: "plots/feel-activ.png"
                    MyTile:
                        source: "plots/feel-temp.png"
                    MyTile:
                        source: "plots/feel-sens.png"
                    MyTile:
                        source: "plots/feel-humi.png"
                    MyTile:
                        source: "plots/feel-pres.png"

<SettingsScreen>:
    name: 'settings'
    MDLabel:
        id: settings_label
        text: "Settings"
        halign: "center"
        font_style: "Overline"
        font_size: "20dp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}

    MDTextField:
        id: username
        hint_text: "Enter your name"
        text: app.store.get('user')['name']
        helper_text: "or your nickname :)"
        helper_text_mode: "on_focus"
        icon_right: "white-balance-sunny"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        size_hint_x: None
        width: 420

    MDTextField:
        id: location
        hint_text: "Enter the name of your city"
        helper_text: "It can't be fake!"
        text: app.store.get('user')['city']
        helper_text_mode: "on_focus"
        icon_right: "city"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.58}
        size_hint_x: None
        width: 420

    MDTextField:
        id: feeling_rate
        hint_text: "On a scale of 1 to 10 how are you feeling?"
        helper_text: "It's important to feel good about yourself."
        text: str(app.store.get('user')['feeling'])
        helper_text_mode: "on_focus"
        icon_right: "star-face"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.46}
        size_hint_x: None
        width: 420
    
    MDTextField:
        id: set_color
        hint_text: "What is your favorite color?"
        helper_text: "Type: Red, Pink, Purple, Indigo, Cyan, Blue, Green, Yellow, Orange, Brown or Gray."
        text: app.store.get('user')['color']
        helper_text_mode: "on_focus"
        icon_right: "border-color"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.34}
        size_hint_x: None
        width: 420
    

    MDSpinner:
        id: save_spinner
        size_hint: None, None
        size: dp(20), dp(20)
        pos_hint: {'center_x': 0.4, 'center_y': 0.22}
        active: False
        determinate: False
    
    MDRectangleFlatButton:
        id: menu_button
        text: "Go to menu"
        font_style: "Button"
        pos_hint: {'center_x': 0.6, 'center_y': 0.15}
        size_hint: 0.15, None
        disabled: True
        on_release: 
            app.sm.current = 'menu'
    
    MDRectangleFlatButton:
        id: save_button
        text: "Save"
        font_style: "Button"
        pos_hint: {'center_x': 0.4, 'center_y': 0.15}
        size_hint: 0.15, None
        on_release: 
            save_spinner.active = True
            app.save_user_data()
            app.update_plots()

    MDSwitch:
        id: switch_button
        widget_style: "desktop"
        pos_hint: {'center_x': 0.9, 'center_y': 0.15}
        on_release: app.switch_theme()

    MDLabel:
        id: switch_label
        text: "Switch theme"
        halign: "center"
        font_style: "Button"
        font_size: "10dp"
        pos_hint: {'center_x': 0.9, 'center_y': 0.1}

    MDLabel:
        id: sign
        text: "Andrzej Kapczyński @2021"
        halign: "center"
        font_style: "Caption"
        font_size: "12dp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.03}

<Tab>
    MDLabel:
        id: tab_label
        halign: "center"
        font_style: "Button"

"""
