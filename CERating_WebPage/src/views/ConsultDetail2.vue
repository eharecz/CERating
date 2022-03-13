<template>
  <div>
    <NavigationBar></NavigationBar>
    <div class="head-title">
      <h1>{{ title }}</h1>
      <p>{{ slogan }}</p>
    </div>
    <div class="main-wrapper">
      <MainTitle></MainTitle>
      <div class="content-wrapper">
        <div class="content-box">
          <div class="rich_media_content " id="js_content" style="visibility: visible;">
            <div>
              《中国企业碳中和社会责任研究报告》将重点研究中国企业碳中和社会责任的概念、重要性及其内涵，
              研究中国企业践行碳中和社会责任的应用案例，
              通过桌面研究、专家访谈、专家评估共同编制出中国企业碳中和社会责任评价体系及使用指南，
              以此衡量企业的碳中和社会责任履行的情况，并对高耗能行业电力行业的A股上市企业进行应用测评，以作示例。
            </div>  
              <br>

            <div>
              1、报告介绍了中国企业社会责任的起源与发展背景、中国企业碳中和社会责任的概念、驱动因素，中国企业践行碳中和社会责任所面临的挑战与机遇以及现状。
            </div>
            <br>

            <div>
              2、报告指出，中国企业碳中和社会责任包含企业自身实现碳中和的责任，企业以其技术赋能社会实现碳中和的责任，企业发声与披露、意识影响区域、行业、民众端的责任，企业在国际上发声并积极参与国际标准的制定的责任，企业作为确保双碳目标完成的后备保障的责任。本章将对五种碳中和社会责任内涵进行详细说明。
            </div>
              <br>
            <div>
              3、报告通过桌面研究、专家访谈、专家评估，亿欧智库与中国节能协会碳中和专业委员会共同编制出中国企业碳中和社会责任评价体系及使用指南，以此衡量企业的碳中和社会责任履行的情况，并对高耗能行业电力行业的A股上市企业进行应用测评，以作示例。
            </div>
              <br>
            <div>
              4、报告指出，践行碳中和社会责任的中国企业包括已制定双碳目标、时间框架、实现路线及保障措施的企业或为企业提供技术、模式等赋能政府端、企业端、民众端实现双碳目标的服务商。本章将践行碳中和社会责任的企业分为四类，并对四种分类中应用的技术进行了说明。每一种分类选择1-3个企业作为案例进行详细的说明。
            </div>





          </div>     

                    
                    
                    
                  



        </div>
        <div class="vertical-bar"></div>
        <div class="navi-box">
          <h3 style="color: #74b9ff; margin: 30px">相关链接:</h3>
          <a style="margin: 60px 30px" href="/consultdetail">碳达峰、碳中和的经济学解读</a>
          <div style="height: 30px"></div>
          <a style="margin: 60px 30px;" href="/consultdetail3">启动！2022中国能源企业碳中和贡献力报告企业材料征集</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MainTitle from "../components/Consult/MainTitle";
import NavigationBar from '../components/NavigationBar.vue';
export default {
  name: "ConsultDetail",
  components: {
    MainTitle,
    NavigationBar
  },
  data() {
    return {
      title: '新鲜出炉 | 中国企业碳中和社会责任研究报告',
      slogan: '此处可添加内容'
    }
  }
}
</script>

<style scoped>
.head-title{
  background: url("../assets/consult_pic1.jpg")fixed center no-repeat;
  width: 100%;
  height: 60vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  /* position: absolute; */
  left: 0;
  /* top: 0; */
}
.head-title h1{
  position: relative;
  top: -30%;
  color: white;
}
.head-title p{
  position: relative;
  top: -20%;
  color: white;
}
.main-wrapper {
  overflow-x: hidden;
  position: absolute;
  width: 90%;
  left: 5%;
  top: 35%;
  background-color: #fff;
  border-radius: 12px;
}
.content-wrapper{
  display: flex;
  margin: 50px;
  align-content: center;
  justify-content: center;
}
.content-box{
  border: 2px solid #74b9ff;
  /* background-color: #bbbbbb; */
  border-radius: 6px;
  width: 60%;
  height: 500px;
  display: flex;
  /* flex-direction: column;
  justify-content: center;
  text-align: center; */
}
.vertical-bar{
  height: 600px;
  width: 2px;
  background-color: #bbbbbb;
  margin: 20px;
  margin-left: 30px;
}
.navi-box{
  width: 30%;
  height: 500px;
  border: 2px solid #74b9ff;
  border-radius: 6px;
}
</style>