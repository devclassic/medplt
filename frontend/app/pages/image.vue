<template>
  <div class="wrap">
    <div class="title">辅助影像</div>
    <div class="top-box">
      <div class="result">
        <div class="item right">
          <div class="content">您好，我想让你帮我看看病情，可以吗？</div>
        </div>
        <div class="item">
          <div class="content">
            这是测试回答内容这是测试回答内容这是测试回答内容，
            这是测试回答内容这是测试回答内容这是测试回答内容，
            这是测试回答内容这是测试回答内容这是测试回答内容，
            这是测试回答内容这是测试回答内容这是测试回答内容，
            这是测试回答内容这是测试回答内容这是测试回答内容，
            这是测试回答内容这是测试回答内容这是测试回答内容，
            这是测试回答内容这是测试回答内容这是测试回答内容。
          </div>
        </div>
      </div>
    </div>
    <div class="bottom-box">
      <div class="input-box">
        <div class="toolbar">
          <div class="left">
            <div class="upimage"></div>
            <div class="updicom"></div>
          </div>
          <div class="right">
            <div class="status">正在录音...</div>
            <div class="speech"></div>
            <div class="clean"></div>
          </div>
        </div>
        <textarea placeholder="请上传片子并输入相关问题" class="input"></textarea>
        <div class="bottom">
          <div class="submit"></div>
        </div>
      </div>
      <div class="image-box">
        <div class="images">
          <img src="@/assets/images/img1.png" class="img" />
          <img src="@/assets/images/img2.png" class="img" />
          <img src="@/assets/images/img3.png" class="img" />
          <img src="@/assets/images/img1.png" class="img" />
          <img src="@/assets/images/img2.png" class="img" />
          <img src="@/assets/images/img3.png" class="img" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup></script>

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

  .top-box {
    border: 1px solid #e5e6eb;
    border-radius: 20px;
    position: absolute;
    top: 77px;
    left: 30px;
    right: 30px;
    bottom: 350px;
  }

  .result {
    position: absolute;
    top: 20px;
    left: 20px;
    right: 20px;
    bottom: 20px;
    overflow: auto;
  }

  .result .item {
    margin-bottom: 10px;
    display: flex;
  }

  .result .item.right {
    justify-content: end;
  }

  .result .item.right .content {
    background: #f5f5f5;
    padding: 15px 20px;
    border-radius: 10px;
  }

  .bottom-box {
    height: 300px;
    border-radius: 20px;
    position: absolute;
    left: 30px;
    right: 30px;
    bottom: 30px;
    display: flex;
    justify-content: space-between;
  }

  .input-box,
  .image-box {
    width: 49.5%;
    height: 100%;
    border: 1px solid #e5e6eb;
    border-radius: 10px;
    padding: 10px;
  }

  .image-box {
    padding: 25px;
    overflow: auto;
  }

  .images {
    width: fit-content;
    display: flex;
  }

  .img {
    width: 230px;
    height: 230px;
    border-radius: 10px;
    margin-right: 20px;
    cursor: pointer;
    display: block;
  }

  .img:last-child {
    margin-right: 0;
  }

  .toolbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .toolbar .left {
    display: flex;
    align-items: center;
  }

  .toolbar .right {
    display: flex;
    align-items: center;
  }

  .upimage {
    width: 100px;
    height: 36px;
    background: url('@/assets/images/image-upimg.png') no-repeat center center / 100% 100%;
    cursor: pointer;
  }

  .updicom {
    width: 120px;
    height: 36px;
    background: url('@/assets/images/image-updicom.png') no-repeat center center / 100% 100%;
    cursor: pointer;
    margin-left: 10px;
  }

  .status {
    color: #cccccc;
  }

  .speech {
    width: 16px;
    height: 16px;
    background: url('@/assets/images/icon-speech.png') no-repeat center center / 100% 100%;
    cursor: pointer;
    margin-left: 10px;
  }

  .clean {
    width: 16px;
    height: 16px;
    background: url('@/assets/images/icon-clean.png') no-repeat center center / 100% 100%;
    cursor: pointer;
    margin: 0 10px 0;
  }

  .input {
    width: 100%;
    height: 190px;
    margin: 10px 0 5px 0;
    border: none;
    outline: none;
    border-top: 1px solid #e5e6eb;
    padding: 10px;
    font-size: 14px;
    resize: none;
  }

  .bottom {
    display: flex;
    justify-content: end;
  }

  .submit {
    width: 32px;
    height: 32px;
    background: url('@/assets/images/submit.png') no-repeat center center / 100% 100%;
    cursor: pointer;
  }

  .submit:hover {
    background-image: url('@/assets/images/submit-active.png');
  }
</style>
