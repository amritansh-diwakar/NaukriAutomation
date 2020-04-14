def close_all_popup_windows(driver):
    main_window = driver.current_window_handle
    window_handles = driver.window_handles
    for window in window_handles[1:]:
        driver.switch_to.window(window)
        driver.close()
    driver.switch_to.window(main_window)
