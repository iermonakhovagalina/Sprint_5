# Sprint_5

## О проекте
Тестирование сервиса Stellar Burgers - космический фастфуд для сборки бургеров.

## Тесты

### Регистрация (`test_registration.py`)
- Успешная регистрация - `TestCheckNewRegister.test_registration`
- Ошибка для существующего пользователя - `TestCheckingCreationExistingAccount.test_existing_account`
- Ошибка при пустом поле "Имя" - `TestCheckRegisterNoName.test_registration_no_name`
- Ошибка при коротком пароле - `TestCheckingErrorPassword.test_error_password`
- Ошибка при пустом поле "Пароль" - `TestCheckingNoPassword.test_no_password`

### Вход/выход (`test_check_exit.py`)
- Вход по кнопке "Войти в аккаунт" - `TestBigMainButton.test_check_entrance_by_big_button`
- Вход через кнопку "Личный кабинет" - `TestCheckRegister.test_login_password_recovery`
- Вход через форму регистрации - `TestCheckEntranceFromRecoveryPage.test_button_inscription_login`
- Вход через восстановление пароля - фикстура `start_from_recovery_page`
- Выход из аккаунта - `TestButtonCheckExit.test_check_loging_out`

### Личный кабинет (`test_move_to_personal_accaunt.py`)
- Переход в личный кабинет - `TestCheckPageProfile.test_transition_to_profile`
- Переход в конструктор - `TestTransitionByConstructor.test_check_transition_by_constructor`
- Переход по логотипу - `TestTransitionByLogo.test_transition_by_logo`
- Выход из аккаунта - `TestButtonCheckExit.test_check_logging_out`

### Конструктор (`test_move_to_desing.py`)
- Раздел "Булки" - `TestCheckChapterBread.test_check_chapter_bread`
- Раздел "Соусы" - `TestCheckChapterSauce.test_check_chapter_sauce`
- Раздел "Начинки" - `TestCheckChapterFillings.test_check_chapter_fillings`

## Запуск тестов
```bash
pytest tests/ -v

