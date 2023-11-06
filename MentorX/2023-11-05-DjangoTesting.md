---
title: Django Unit Test、Integration Test和最佳实践
---

# 为什么进行 Unit Test？

- Unit Test 的重要性：代码质量、错误预防、可维护性。

---

# Unit Test 如何加速问题识别和修复

- 问题识别加速：
  - 自动化测试快速发现问题。
  - 提供快速反馈，帮助尽早识别和解决问题。
  - 集成到 CI/CD 流程，自动运行 Unit Test 以加速问题检测。

---

# Unit Test 如何加速问题识别和修复

- Accelerating problem resolution：
  - Unit Tests Pinpoint the Root Cause of Issues
  - Prevent Regression Issues and Ensure Problem Resolution
  - Reduce Debugging Time and Improve Issue Resolution Efficiency。

---

# 设置的开发环境

- 使用虚拟环境来创建干净的开发环境。
- 安装和配置必要的 Python 包和工具，如`virtualenv`和`pip`。
- 避免 dependency conflict，确保项目的隔离性。

---

```
from django.test import TestCase
from gymCMS.models import User, Address

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create an Address instance for testing
        cls.address = Address.objects.create(
            street="123 Main St",
            city="Example City",
            state="Example State",
            zip_code="12345",
        )

        # Create a User instance for testing
        cls.user = User.objects.create(
            is_admin=False,
            first_name="John",
            last_name="Doe",
            username="johndoe",
            password="securepassword",
            email="johndoe@example.com",
            phone="123-456-7890",
            birth_date="1990-01-01",
            address=cls.address,
            membership=User.MEMBERSHIP_BRONZE,
        )

    def test_user_model_fields(self):
        # Retrieve the User instance from the database
        user = User.objects.get(username="johndoe")

        self.assertEqual(user.is_admin, False)
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.username, "johndoe")
        self.assertEqual(user.password, "securepassword")
        self.assertEqual(user.email, "johndoe@example.com")
        self.assertEqual(user.phone, "123-456-7890")
        self.assertEqual(str(user.birth_date), "1990-01-01")
        self.assertEqual(user.address, self.address)
        self.assertEqual(user.membership, User.MEMBERSHIP_BRONZE)

    def test_user_model_str_method(self):
        # Test the __str__ method of the User model
        user = User.objects.get(username="johndoe")
        self.assertEqual(str(user), "John Doe (johndoe)")

    def test_user_model_membership_choices(self):
        # Test that the membership field only allows specified choices
        invalid_membership = "X"
        user = User.objects.get(username="johndoe")
        user.membership = invalid_membership
        with self.assertRaises(ValueError):
            user.save()

    def test_user_model_unique_constraints(self):
        # Test the unique constraints for username and email
        with self.assertRaises(Exception):
            User.objects.create(
                username="johndoe",
                email="johndoe@example.com",
                address=self.address,
            )

    def test_user_model_default_membership(self):
        # Test the default membership value
        user = User.objects.create(
            username="newuser",
            email="newuser@example.com",
            address=self.address,
        )
        self.assertEqual(user.membership, User.MEMBERSHIP_BRONZE)

```

---

# 运行 Unit Test

```
python manage.py test gymCMS
python manage.py test myapp.tests.UserModelTest
```

---

# 测试数据准备

使用 fixture 来创建和加载测试数据，以便测试不同的场景和情况。 Fixture 是一个包含了数据库数据的文件，通常是 JSON、XML 或 YAML 格式。

---

# 创建 Fixture 文件

```
[
    {
        "model": "gymCMS.user",
        "pk": 1,
        "fields": {
            "is_admin": true,
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "password": "hashed_password_1",  # Replace with a hashed password
            "email": "johndoe@example.com",
            "phone": "123-456-7890",
            "birth_date": "1990-01-01T00:00:00Z",
            "address": 1,
            "membership": "B"
        }
    }
]

```

---

# 创建 Fixture 文件

---

从 db 里提取

```Python[1|2]
python manage.py dumpdata gymCMS.User
--indent 2 > User_Fixture.json
```

---

# 在测试中使用 Fixture 数据：

```
from django.test import TestCase
from gymCMS.models import User

class MyTestCase(TestCase):
    fixtures = ['User_Fixture.json']  # 指定要加载的fixture文件

    def test_scenario_1(self):
        # 使用fixture数据执行测试场景1
        obj = User.objects.get(id=1)
        self.assertEqual(obj.some_field, expected_value_1)

    def test_scenario_2(self):
        # 使用fixture数据执行测试场景2
        obj = ModelName.objects.get(id=2)
        self.assertEqual(obj.some_field, expected_value_2)

```

---

# Assertions 和 Test Cases

- 常用 assertion，如`assertEqual`和`assertTrue`。
- 每个方法以 test\_开头， 并包含要测试的功能。
- 使用@classmethod decorator 来定义类级别的 setUpClass 和 tearDownClass 方法，如果需要在整个测试类的开始和结束时执行一次性设置和清理操作。

---

# 编写可测试的代码

- Function 简洁性
  - Loose Coupling and Dependency Injection
  - Single Responsibility Principle
  - Test-Driven Development (TDD)

---

# Mocking

- Mocking 是一个对象，用于 Mocking 真实对象或组件的行为。
- Mocking 用于验证被测试的代码与其依赖项之间的交互。
- Mocking 可以记录和验证方法调用、参数和返回值。
- Mocking 可以用于检查特定方法是否以特定次数或具有特定参数被调用。
- Mocking 通常用于 behavior driven 的测试，其中重点是对象之间的交互，而不仅仅是返回值

---

# Stubbing

- Stubbing 是一个对象或函数，用于提供预定义的响应或行为以响应特定方法调用。
- Stubbing 用于将真实对象或组件替换为简化或受控的版本，以供测试目的使用。
- Stubbing 不验证被测试的代码与其依赖项之间的交互，它们仅仅返回预配置的结果。
- Stubbing 主要用于隔离被测试的代码，使测试更加可预测。
- Stubbing 通常用于 state driven 的测试，其中主要关注的是被测试的代码的行为和逻辑。

---

# Example

```
from unittest.mock import Mock, patch
from django.test import TestCase
from myapp.models import User
from myapp.views import list_all_users

class TestListAllUsersWithMock(TestCase):
    @patch('myapp.models.User.objects.all')
    def test_list_all_users_with_mock(self, mock_user_objects_all):
        # Create a mock for User.objects.all() to simulate database query
        mock_user_queryset = Mock()
        mock_user_objects_all.return_value = mock_user_queryset

        # Call the function being tested
        result = list_all_users()

        # Verify that User.objects.all() was called
        mock_user_objects_all.assert_called_once()

        # Assert the result (e.g., check if it's rendering the correct template)
        self.assertEqual(result.template_name, "user/user_list.html")
```

---

```
class TestListAllUsersWithStub(TestCase):
    def test_list_all_users_with_stub(self):
        # Create a stub for User.objects.all() to simulate a queryset
        class UserQuerySetStub:
            def all(self):
                return "Stubbed User QuerySet"

        # Replace the actual User.objects.all() with the stub
        original_user_objects_all = User.objects.all
        User.objects.all = UserQuerySetStub()

        # Call the function being tested
        result = list_all_users()

        # Assert the result without verifying interactions
        self.assertEqual(result.template_name, "user/user_list.html")

        # Restore the original User.objects.all()
        User.objects.all = original_user_objects_all

```

---

# 测试覆盖率

- 使用`coverage.py`工具来测量代码覆盖率。

```
pip install coverage //安装
coverage run manage.py test //运行测试
coverage report //生成代码覆盖率报告
```

---

# 持续集成（CI）

- Unit Test 如何集成到持续集成（CI）流程中。

```
    - name: Run tests
      run: python manage.py test
```

---

# Unit Test 和 Integration Test 之间的区别：

- 范围：Unit Test 专注于测试单个组件、函数或类的行为，而 Integration Test 测试多个组件之间的协作和交互。
- 依赖：Unit Test 通常使用 Stubbing 或 Mocking 来隔离被测试的组件，而 Integration Test 通常涉及真实的依赖项，如数据库或外部服务。
- 目标：Unit Test 的目标是验证一个特定组件的功能，而 Integration Test 的目标是验证应用程序的整体行为。
- 复杂性：Integration Test 通常更复杂，因为它需要处理多个组件之间的互动和复杂性

---

# 编写 Integration Test

- 如何编写 DjangoIntegration Test。
- 创建测试场景、进行 HTTP 请求和验证响应。
- 测试视图行为和表单提交。

---

- 选择使用集成测试取决于以下情况：
  - 测试整体行为：当需要测试应用程序的整体行为，包括多个组件之间的协作时，使用集成测试。
  - 验证集成：如果需要确保数据库、外部服务和其他依赖项与应用程序一起正常工作，集成测试是必要的。
  - 模拟真实场景：集成测试有助于 Mocking 真实使用情况，以确保应用程序在生产环境中的可用性和稳定性。
  - 完整性和可靠性：如果关注应用程序的完整性和可靠性，集成测试可以帮助发现潜在的问题。
  - 性能测试：某些性能测试也可以被视为一种集成测试，以验证应用程序在负载下的性能表现。

---

# 如何编写 DjangoIntegration Test

```
from django.test import TestCase
from django.urls import reverse
from .models import User  # Import your User model
from .views import list_all_users, show_user_details, create_a_user, update_a_user, delete_a_user

class UserTestCase(TestCase):
    def setUp(self):
        # Create a User instance for testing
        self.user = User.objects.create(username="testuser", email="test@example.com")

    def test_list_all_users_view(self):
        response = self.client.get(reverse("list-all-users"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")  # Check if user is in the response

    def test_show_user_details_view(self):
        response = self.client.get(reverse("show-user-details", args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")

    def test_create_a_user_view(self):
        response = self.client.get(reverse("create-a-user"))
        self.assertEqual(response.status_code, 200)

    def test_update_a_user_view(self):
        response = self.client.get(reverse("update-a-user", args=[self.user.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_a_user_view(self):
        response = self.client.get(reverse("delete-a-user", args=[self.user.id]))
        self.assertEqual(response.status_code, 200)

```
