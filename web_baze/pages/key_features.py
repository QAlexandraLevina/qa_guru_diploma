from selene import browser, have, be


class KeyFeatures:
    def __init__(self):
        self.key_feature_title = browser.element(".key-features__title")
        self.key_feature_tabs = browser.all(".key-features__item")
        self.key_feature_description = browser.element(".key-features__description-value")
        self.key_feature_large_preview = browser.element(".key-features__full-img")
        self.key_features_thumbnails = browser.all(".key-features__thumbnails img")
        self.key_features_progress_bar = browser.all(".key-features__progress-bar")


    """Клик по каждой вкладке в разделе 'Ключевые особенности'"""
    def click_feature_tabs(self, tab_name):
        self.key_feature_tabs.element_by(have.text(tab_name)).click()
        return self


    def click_specializations_tab(self):
        self.click_feature_tabs("СПЕЦИАЛИЗАЦИИ")
        return self


    def click_pvp_events_with_matchmaking_tab(self):
        self.click_feature_tabs("PVP ИВЕНТЫ С МАТЧМЕЙКИНГОМ")
        return self


    def click_leveling_up_character_tab(self):
        self.click_feature_tabs("ПРОКАЧКА ПЕРСОНАЖА")
        return self


    def click_exploring_the_world_tab(self):
        self.click_feature_tabs("ИССЛЕДОВАНИЕ МИРА")
        return self


    """Проверка отображения заголовка раздела 'Ключевые особенности'"""
    def should_display_title_section(self):
        self.key_feature_title.should(be.visible).should(have.text("КЛЮЧЕВЫЕ ОСОБЕННОСТИ"))
        return self


    """Проверка отображения прогресс-баров под вкладками раздела 'Ключевые особенности'"""
    def should_display_key_feature_progress_bar(self):
        self.key_features_progress_bar.should(have.size(4))
        for i in range(4):
            self.key_features_progress_bar[i].should(be.visible)
        return self


    """Проверка отображения и кликабельности вкладок в разделе 'Ключевые особенности'"""
    def should_display_key_feature_tabs(self):
        tabs_names = ["СПЕЦИАЛИЗАЦИИ", "PVP ИВЕНТЫ С МАТЧМЕЙКИНГОМ", "ПРОКАЧКА ПЕРСОНАЖА", "ИССЛЕДОВАНИЕ МИРА"]
        for tab_name in tabs_names:
            self.key_feature_tabs.element_by(have.text(tab_name)).should(be.visible).should(be.clickable)
        return self


    """Проверка отображения крупного превью в разделе 'Ключевые особенности'"""
    def should_display_key_feature_large_preview(self):
        self.key_feature_large_preview.should(be.visible)
        return self


    """Проверка отображения миниатюр во вкладках раздела 'Ключевые особенности'"""
    def should_display_key_feature_thumbnails(self):
        self.key_features_thumbnails.should(have.size(3))
        for i in range(3):
            self.key_features_thumbnails[i].should(be.visible)
        return self