<template>
  <div class="grade">
    <div class="title">
      <p>模拟评级导航</p>
    </div>
    <div class="textarea-box">
      <textarea placeholder="介绍模拟评级的作用和流程"></textarea>
    </div>
    <div class="" style="display:flex;justify-content: space-between;">
      <div></div>
      <div class="" style="display:flex;">
        <button class="el-button el-button--primary el-button--default" style="" @click="$router.go(-1)">返回</button>
        <button class="el-button el-button--primary el-button--default" style="margin-right: 20px;">模拟评级入口</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "grade"
}
</script>

<style scoped lang="scss">
.grade {
  padding: 30px;
  height: calc(100vh - 60px);
  overflow: hidden;

  .title {
    font-size: 30px;
    color: #0096ea;
    font-weight: 600;
    border-bottom: 5px solid #0096ea;
    padding-bottom: 20px;
  }

  .textarea-box {
    height: 60%;
    width: 100%;
    padding: 20px;

    textarea {
      width: calc(100% - 80px);
      height: calc(100% - 40px);
      padding: 20px;
    }
  }

  .el-button {
    --el-button-bg-color: #409eff;
    --el-button-border-color: #409eff;
    --el-button-hover-bg-color: rgb(102, 177, 255);
    --el-button-hover-border-color: rgb(102, 177, 255);
    --el-button-active-bg-color: rgb(58, 142, 230);
    --el-button-active-border-color: rgb(58, 142, 230);
  }
}
</style>
