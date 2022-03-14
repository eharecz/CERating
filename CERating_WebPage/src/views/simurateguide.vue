<template>
  <div class="grade">
    <NavigationBar/>
    <div class="title">
      <p>模拟评级导航</p>
    </div>
    <div class="textarea-box">
      <div>
        <span style="font-family:黑体; font-size:16pt; width=100%; display: block; text-align: center;">模拟评级导航简单介绍</span>
        <span style="height: 60px; display: block;"/>
        <span style="font-family:黑体; font-size:14pt; display: block;">一、进入模拟评级页面</span>
        <img src="../assets/a.png" style="height: 250px; display: block; margin: auto;" />
        <span style="height: 60px; display: block;"/>
        <span style="font-family:黑体; font-size:14pt; display: block;">二、填写相关指标(注意单位填写)</span>
        <span style="font-family:宋体; font-size:12pt; margin: 20px 60px; display: block;">
          输入想要进行模拟评级的企业以及相关信息，单击确认按钮后即可查询。注意查询需要消耗一次模拟评级次数，若当前模拟评级次数余额不足，则会跳转至充值页面。
        </span>
        <img src="../assets/b.png" style="height: 600px; display: block; margin: auto;" />
        <span style="height: 60px; display: block;"/>
        <span style="font-family:黑体; font-size:14pt; display: block;">三、查看评级结果</span>
        <img src="../assets/c.png" style="height: 300px; display: block; margin: auto;" />
        <span style="height: 60px; display: block;"/>
        <div class="" style="flow: right;">
          <button class="el-button el-button--primary el-button--default" style="float: right;" @click="$router.go(-1)">返回</button>
          <button class="el-button el-button--primary el-button--default" style="float: right; margin-right: 20px" @click="$router.push('/simurate')">模拟评级入口</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavigationBar from "../components/NavigationBar.vue";
export default {
  components: { NavigationBar},
  name: "grade"
}
</script>

<style scoped lang="scss">
.grade {
  padding: 30px;
  height: calc(100vh - 60px);
  // overflow: hidden;

  .title {
    font-size: 30px;
    color: #0096ea;
    font-weight: 600;
    border-bottom: 5px solid #0096ea;
    padding-bottom: 20px;
  }

  .textarea-box {
    height: 60%;
    width: 80%;
    padding: 20px;
    margin: auto;

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
