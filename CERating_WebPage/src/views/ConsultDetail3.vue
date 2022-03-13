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
          <div class="subtitle-in-text"><strong>征集背景</strong></div>
          <br>

          <div>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;实现碳达峰、碳中和，是党中央统筹国内国际两个大局作出的重大战略决策，是着力解决资源环境约束突出问题、实现中华民族永续发展的必然选择，是构建人类命运共同体的庄严承诺。
          </div>
          <br>
          <div>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2021年10月出台了《中共中央国务院关于完整准确全面贯彻新发展理念做好碳达峰碳中和工作的意见》，进一步明确把碳达峰、碳中和纳入经济社会发展全局，以经济社会发展全面绿色转型为引领，以能源绿色低碳发展为关键，加快形成节约资源和保护环境的产业结构、生产方式、生活方式、空间格局，坚定不移走生态优先、绿色低碳的高质量发展道路，确保如期实现碳达峰、碳中和。
          </div>
          <br>

          <div class="subtitle-in-text"><strong>征集意义</strong></div>
          <br>
          <div>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为进一步助推碳达峰、碳中和目标实现，2022年中国能源报将联合专业权威智库机构推出《2022中国能源企业碳中和贡献力报告》，该报告具有权威性、公益性、公正性等特点，对能源行业碳达峰、碳中和具有重要的参考借鉴价值，是能源企业低碳绿色可持续发展的重要指标。

          </div>
          <br>


          <div class="subtitle-in-text"><strong>征集标准</strong></div>
          <br>
          <div>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;征集范围：中国能源企业
参考指标：碳减排量、碳市场交易额、碳排放强度、绿色投资额、碳核查、碳管理、碳金融、碳减排技术、碳中和时间表、路线图等有关指标，综合评估。

          </div>
          <br>

          <div class="subtitle-in-text"><strong>征集日期</strong></div>
          <br>

          <div>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;即日起至2022年7月31日

          </div>
        </div>
        </div>
        <div class="vertical-bar"></div>
        <div class="navi-box">
          <h3 style="color: #74b9ff; margin: 30px">相关链接:</h3>
          <a style="margin: 60px 30px" href="/consultdetail">碳达峰、碳中和的经济学解读</a>
          <div style="height: 30px"></div>
          <a style="margin: 60px 30px;" href="/consultdetail2">新鲜出炉 | 中国企业碳中和社会责任研究报告</a>
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
      title: '启动！2022中国能源企业碳中和贡献力报告企业材料征集',
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
  height: 800px;
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
  height: 700px;
  border: 2px solid #74b9ff;
  border-radius: 6px;
}
.subtitle-in-text{
  text-align:center;
}
</style>