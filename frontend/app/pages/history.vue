<template>
  <div class="wrap">
    <div class="header">
      <div class="title">历史记录</div>
      <div class="types">
        <div class="type active">多人语音</div>
        <div class="type">辅助质控</div>
        <div class="type">辅助诊疗</div>
        <div class="type">辅助影像</div>
      </div>
    </div>
    <div>
      <div class="list">
        <table class="table">
          <tbody>
            <tr class="head">
              <td>编号</td>
              <td>问题</td>
              <td>答案</td>
              <td>时间</td>
              <td>操作</td>
            </tr>
            <tr>
              <td>1</td>
              <td>测试问题</td>
              <td>测试答案</td>
              <td>2023-01-01</td>
              <td>
                <div class="view">查看</div>
              </td>
            </tr>
            <tr>
              <td>2</td>
              <td>测试问题</td>
              <td>测试答案</td>
              <td>2023-01-01</td>
              <td>
                <div class="view">查看</div>
              </td>
            </tr>
            <tr>
              <td>3</td>
              <td>测试问题</td>
              <td>测试答案</td>
              <td>2023-01-01</td>
              <td>
                <div class="view">查看</div>
              </td>
            </tr>
            <tr>
              <td>4</td>
              <td>测试问题</td>
              <td>测试答案</td>
              <td>2023-01-01</td>
              <td>
                <div class="view">查看</div>
              </td>
            </tr>
            <tr>
              <td>5</td>
              <td>测试问题</td>
              <td>测试答案</td>
              <td>2023-01-01</td>
              <td>
                <div class="view">查看</div>
              </td>
            </tr>
            <tr>
              <td>6</td>
              <td>测试问题</td>
              <td>测试答案</td>
              <td>2023-01-01</td>
              <td>
                <div class="view">查看</div>
              </td>
            </tr>
            <tr>
              <td>7</td>
              <td>测试问题</td>
              <td>测试答案</td>
              <td>2023-01-01</td>
              <td>
                <div class="view">查看</div>
              </td>
            </tr>
            <tr>
              <td>8</td>
              <td>测试问题</td>
              <td>测试答案</td>
              <td>2023-01-01</td>
              <td>
                <div class="view">查看</div>
              </td>
            </tr>
            <tr>
              <td>9</td>
              <td>测试问题</td>
              <td>测试答案</td>
              <td>2023-01-01</td>
              <td>
                <div class="view">查看</div>
              </td>
            </tr>
            <tr>
              <td>10</td>
              <td>测试问题</td>
              <td>测试答案</td>
              <td>2023-01-01</td>
              <td>
                <div class="view">查看</div>
              </td>
            </tr>
            <tr>
              <td>11</td>
              <td>测试问题</td>
              <td>测试答案</td>
              <td>2023-01-01</td>
              <td>
                <div class="view">查看</div>
              </td>
            </tr>
            <tr>
              <td>12</td>
              <td>测试问题</td>
              <td>测试答案</td>
              <td>2023-01-01</td>
              <td>
                <div class="view">查看</div>
              </td>
            </tr>
            <tr>
              <td>13</td>
              <td>测试问题</td>
              <td>测试答案</td>
              <td>2023-01-01</td>
              <td>
                <div class="view">查看</div>
              </td>
            </tr>
            <tr>
              <td>14</td>
              <td>测试问题</td>
              <td>测试答案</td>
              <td>2023-01-01</td>
              <td>
                <div class="view">查看</div>
              </td>
            </tr>
            <tr>
              <td>15</td>
              <td>测试问题</td>
              <td>测试答案</td>
              <td>2023-01-01</td>
              <td>
                <div class="view">查看</div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="pager">
        <el-pagination background layout="prev, pager, next" :total="1000" />
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

  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    line-height: 1;
  }

  .title {
    font-size: 22px;
    color: #011f3c;
    padding: 30px 30px 25px 30px;
  }

  .types {
    display: flex;
    align-items: center;
  }

  .types .type {
    font-size: 16px;
    color: #86909c;
    margin-right: 30px;
    cursor: pointer;
    padding: 10px 0;
  }

  .types .type.active {
    color: #13a5c7;
    border-bottom: 2px solid #13a5c7;
  }

  .list {
    padding: 20px 30px;
  }

  .view {
    color: #13a5c7;
    cursor: pointer;
  }

  .table {
    width: 100%;
  }

  .table td {
    padding: 10px 20px;
  }

  .table tr:nth-child(odd) {
    background-color: #f8f8f8; /* 奇数行 */
  }

  .table tr:nth-child(even) {
    background-color: #ffffff; /* 偶数行 */
  }

  .table td {
    font-size: 14px;
    color: #5e5e5e;
  }

  .table .head td {
    font-size: 16px;
    color: #1f2129;
  }

  .pager {
    display: flex;
    justify-content: end;
    align-items: center;
    margin-top: 20px;
    padding: 0 30px;
  }
</style>
