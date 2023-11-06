## pipenv install mysqlclient error - how to fix

- Step 1: Identify keywords: "brew", "sub-dependencies"
- Step 2: Diagnose: would be version conflict of sql (pre-installed versions of mySQL are mismatched with the project dependency)
- Step 3: One possible solution is to update everything to the most updated `brew install mysql pkg-config`
- Step 4: Test

## Testing common practice

- 能用 assert.equal()就用 assert.equal()而不是 assert.true or false -> 直观表现代码内容便于 debug

- unit test:

  - dependency injection
  - 简洁性
  - mocking
  - stubbing: 屎山代码+private function

- coverage

- branch coverage

unit test 到 CI

action .yml file to fix the django version issue

django integration test 会 mock http response to test

## Ask

- 本地 automate testing
- customized scrips
