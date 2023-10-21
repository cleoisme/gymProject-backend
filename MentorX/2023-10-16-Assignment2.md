# Assignment 2 - 2023-10-16

## Tasks

- [ ] Optimize data schema from the last week

  - [ ] `clients` -> user
  - [ ] `admin`: Inherit User Object

    - id: UserId
    - isAdmin: Boolean

  - [ ] `notification`:

    - no need to save in db
    - 但是后端需要以 model 形式存在

  - [ ] `posts`:
    - Staged publishment system: https://www.django-cms.org/en/

- [ ] Finalize the data schema into an ER (Entity Relationship) diagram (AHHHHHH)
- [ ] Start programming on endpoints
- [ ] Initialize the repo for the fronend in React
  - Start with the 'user' component, improve the component reusibility along the way
- [ ] Github **Project** Tab Setup

## Notification Mechanism

- AWS 接收端 SQS: FIFO Structure
- AWS 发送端 SNS: 后端 Django 监听看是否 Queue 中有内容，然后发给前端处理

## Industry Practice

- `package.lock.json`: 生成文件不要删除，npm 会尽可能的找最新的版本的 dependencies 导致 Incompatibility between the dependencies and codebase

  - define versioning 的时候尽可能 specific
  - typescript 自己不用 semantic versioning
    - Versioning convension: Major.Minor.Patch

- React components:

  - state 越少越好，能在 component 层面解决就解决
  - React 中 contextProvider 的出现或可替代 Redux 的功能
  - functional component: React 16

- Trends:

  - 后端在职责层面越分越细，getting more portable and serverless
  - 前端越来越复杂且需求越来越多

- There is always a tradeoff:

  - performance: django > nodejs > go/c++
  - learning curve: django < nodejs < go/c++

- Why return the newly created object after `POST`?

  - As a rule of thumb, after the POST there is a high probability that the newly created object will be used in the program.
  - Need to process the confidential contents of the object
