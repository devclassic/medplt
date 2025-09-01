<template>
  <div class="wrap">
    <div class="title">多人语音</div>
    <div class="box">
      <div class="left">
        <div class="counter">
          <div class="header">
            <div class="text">剩余次数</div>
            <div class="count">
              <strong>596</strong>
              次
            </div>
          </div>
          <div class="blocks">
            <div class="row">
              <div class="row-item">
                <div class="block">
                  <div>
                    <strong>50</strong>
                    次
                    <br />
                    多人语音
                  </div>
                </div>
              </div>
              <div class="row-item">
                <div class="block">
                  <div>
                    <strong>500</strong>
                    次
                    <br />
                    辅助诊疗
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="row-item">
                <div class="block">
                  <div>
                    <strong>500</strong>
                    次
                    <br />
                    辅助质控
                  </div>
                </div>
              </div>
              <div class="row-item">
                <div class="block">
                  <div>
                    <strong>500</strong>
                    次
                    <br />
                    辅助影像
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="repass">
          <div class="bg">
            <div class="form">
              <div class="form-item">
                <div class="label">原始密码</div>
                <input type="password" placeholder="请输入原始密码" class="input" />
              </div>
              <div class="form-item">
                <div class="label">新密码</div>
                <input type="password" placeholder="请输入新密码" class="input" />
              </div>
              <div class="form-item">
                <div class="label">再次确认</div>
                <input type="password" placeholder="请再次输入新密码" class="input" />
              </div>
              <div class="submit">确认</div>
            </div>
          </div>
        </div>
      </div>
      <div class="right">
        <div class="header">历史记录</div>
        <div class="list">
          <div class="list-item">
            <div class="text">2025-12-23 12:22:12</div>
            <div class="count plus">+200次</div>
          </div>
          <div class="list-item">
            <div class="text">2025-12-23 12:22:12</div>
            <div class="count minus">-200次</div>
          </div>
          <div class="list-item">
            <div class="text">2025-12-23 12:22:12</div>
            <div class="count plus">+200次</div>
          </div>
          <div class="list-item">
            <div class="text">2025-12-23 12:22:12</div>
            <div class="count minus">-200次</div>
          </div>
          <div class="list-item">
            <div class="text">2025-12-23 12:22:12</div>
            <div class="count plus">+200次</div>
          </div>
          <div class="list-item">
            <div class="text">2025-12-23 12:22:12</div>
            <div class="count minus">-200次</div>
          </div>
          <div class="list-item">
            <div class="text">2025-12-23 12:22:12</div>
            <div class="count plus">+200次</div>
          </div>
          <div class="list-item">
            <div class="text">2025-12-23 12:22:12</div>
            <div class="count minus">-200次</div>
          </div>
          <div class="list-item">
            <div class="text">2025-12-23 12:22:12</div>
            <div class="count plus">+200次</div>
          </div>
          <div class="list-item">
            <div class="text">2025-12-23 12:22:12</div>
            <div class="count minus">-200次</div>
          </div>
          <div class="list-item">
            <div class="text">2025-12-23 12:22:12</div>
            <div class="count plus">+200次</div>
          </div>
          <div class="list-item">
            <div class="text">2025-12-23 12:22:12</div>
            <div class="count minus">-200次</div>
          </div>
          <div class="list-item">
            <div class="text">2025-12-23 12:22:12</div>
            <div class="count plus">+200次</div>
          </div>
        </div>
        <div class="pager">
          <el-pagination background layout="prev, pager, next" :total="1000" />
        </div>
      </div>
    </div>
  </div>
</template>

<style>
  .el-pagination.is-background .btn-next.is-active,
  .el-pagination.is-background .btn-prev.is-active,
  .el-pagination.is-background .el-pager li.is-active {
    background: #13a5c7;
  }
</style>

<style scoped>
  .wrap {
    position: relative;
    height: 100%;
  }

  .title {
    line-height: 1;
    font-size: 22px;
    color: #011f3c;
    padding: 30px 30px 25px 30px;
  }

  .box {
    border: 1px solid #e5e6eb;
    border-right: 0;
    border-bottom: 0;
    display: flex;
    position: absolute;
    top: 77px;
    left: 30px;
    right: 30px;
    bottom: 30px;
  }

  .left,
  .right {
    width: 50%;
    height: 100%;
  }

  .left {
    border-right: 1px solid #e5e6eb;
    border-bottom: 1px solid #e5e6eb;
  }

  .counter {
    height: 50%;
    border-bottom: 1px solid #e5e6eb;
  }

  .counter .header {
    height: 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #e5e6eb;
    padding: 0 20px;
    background: #f8f8f8;
    font-size: 22px;
    color: #1f2129;
  }

  .blocks {
    height: calc(100% - 60px);
  }

  .row {
    height: 50%;
    display: flex;
  }

  .row-item {
    width: 50%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
  }

  .row:nth-child(1) .row-item {
    padding-bottom: 10px;
  }

  .row:nth-child(1) .row-item:nth-child(1) {
    padding-right: 10px;
  }

  .row:nth-child(1) .row-item:nth-child(2) {
    padding-left: 10px;
  }

  .row:nth-child(2) .row-item {
    padding-top: 10px;
  }

  .row:nth-child(2) .row-item:nth-child(1) {
    padding-right: 10px;
  }

  .row:nth-child(2) .row-item:nth-child(2) {
    padding-left: 10px;
  }

  .block {
    width: 100%;
    height: 100%;
    border: 1px solid #e5e6eb;
    display: flex;
    justify-content: start;
    align-items: center;
    padding-left: 30px;
    color: #5e5e5e;
  }

  .block strong {
    font-size: 36px;
    color: #262626;
  }

  .repass {
    height: 50%;
    padding: 20px;
  }

  .bg {
    width: 100%;
    height: 100%;
    background: #f8f8f8;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .form {
    width: 400px;
  }

  .form-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
  }

  .form-item .label {
    font-size: 14px;
    color: #262626;
  }

  .form-item .input {
    border: 1px solid #e5e6eb;
    width: 325px;
    height: 44px;
    line-height: 44px;
    padding: 0 10px;
    font-size: 22px;
    color: #1f2129;
    outline: none;
    font-size: 16px;
  }

  .submit {
    height: 44px;
    line-height: 44px;
    text-align: center;
    background: #13a5c7;
    border-radius: 5px;
    font-size: 14px;
    color: #ffffff;
    cursor: pointer;
  }

  .right .header {
    height: 60px;
    line-height: 60px;
    border-right: 1px solid #e5e6eb;
    border-bottom: 1px solid #e5e6eb;
    background: #f8f8f8;
    text-align: center;
    font-size: 22px;
    color: #1f2129;
  }

  .list-item {
    height: 50px;
    padding: 0 30px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 14px;
  }

  .list-item:nth-child(odd) {
    background: #ffffff;
  }

  .list-item:nth-child(even) {
    background: #f8f8f8;
  }

  .list-item .count.plus {
    color: #47c662;
  }

  .list-item .count.minus {
    color: #ed5c58;
  }

  .pager {
    display: flex;
    justify-content: end;
    margin-top: 30px;
  }
</style>
