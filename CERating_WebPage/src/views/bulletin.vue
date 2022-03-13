<template>
  <div class="announcement bulletin">
    <div class="box">
      <!--      <div class="title-box">
              <p>一线大厂在线讲解</p>
            </div>
            <div>
              <div class="title">
                <p>1，百度在线网络技术（北京）有限公司介绍：</p>
              </div>
              <div class="dec">
                <p>百度在线网络技术（北京）有限公司，是中国大型互联网公司百度的全称 [1]
                  。百度（Nasdaq简称：BIDU）是全球最大的中文搜索引擎，2000年1月由李彦宏、徐勇两人创立于北京中关村，致力于向人们提供“简单，可依赖”的信息获取方式。“百度”二字源于中国宋朝词人辛弃疾的《青玉案·元夕》词句“众里寻他千百度”，象征着百度对中文信息检索技术的执著追求。</p>
              </div>
            </div>-->
      <div data-v-93c81e66="" class="overflow-hidden mt-20" style="">
        <div data-v-93c81e66="" class=" overflow-hidden pb-5" style="background: rgba(255, 255, 255, .7)">
          <div class="logo-box">
            <img src="../assets/logo.png" alt=""/>
            <span>CERating</span>
          </div>
          <p data-v-93c81e66=""
             class="md-title text-center" style="font-size: 30px">
            产品公告</p>
          <div style="width: 50px;border-bottom: 5px solid;border-radius: 15px;margin: 20px auto 20px"></div>
          <p data-v-93c81e66="" class="md-title1 text-center" style="font-size: 35px;">产品公告</p>
          <div class="gg-box">
            <div class="title">
              <p>尊敬的用户：</p>
            </div>
            <div class="dec">
              <p>本平台自2022年3月投入运营，基本功能有正式评级展示、模拟评级和资讯展示，我们将拿出100%的信心与诚心为您提供服务，同时也希望您能对我们的平台给予肯定和支持。现将几点注意事项说明如下：</p>
            </div>
            <div>
              <div class="title-bt">
                <p>一：评级合理性</p>
              </div>
              <div class="dec">
                <p>
                  本平台的正式评级以及模拟评级均是采用行业内较为先进的算法而得，由专业教授团队指导把关，具有相当的专业性；数据来源真实可信，团队人工搜集和计算机爬取技术相结合，均取自官方披露文件，并经历了多次复核；数据处理过程严谨细致，处理方法科学合理。因此，本平台的评级具有可信性。</p>
              </div>
            </div>
            <div>
              <div class="title-bt">
                <p>二：定价合理性</p>
              </div>
              <div class="dec">
                <p>模拟评级的定价参考了本行业内的平均水平，您将获得的评级内容会与你的支付费用相匹配，希望你能支持我们的知识产权付费。</p>
              </div>
            </div>
            <div>
              <div class="title-bt">
                <p>三：资讯来源</p>
              </div>
              <div class="dec">
                <p>本平台所展示的资讯是由团队层层筛选并对内容严格把关的，来源均是具有行业权威性并且内容具有一定深度，能让您从中了解到碳排放相关的各行业资讯，无论在增长知识和探寻投资机遇方面都具有相当参考性。</p>
              </div>
            </div>
            <div>
              <div class="title-bt">
                <p>四：更新频率说明</p>
              </div>
              <div class="dec">
                <p>本平台对于评级方法采取不定期更新法，本团队会实时关注业内最新动态，对评级方法做出适当更新，以维持评级的科学性。对于资讯展示采取实时更新的方式，保证您能在本网站获取碳排放资讯最新实时动态。</p>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "announcement"
}
</script>

<style scoped>
.announcement {
  background: url("../assets/login_background.jpg") no-repeat;
  background-size: cover;
}

.box {
  width: 1200px;
  margin: 0 auto;
  text-align: left;
  min-height: 100vh;
}

.box .title-box {
  width: 70%;
  padding: 50px;
  border-radius: 15px;
  background: #fff;
  margin: 0 auto 50px;
  font-size: 28px;
  color: #eb0019;
  text-align: center;
  font-weight: 600;
}


.box .title {
}

.md-title {
  font-size: 32px;
  font-weight: 400;
  color: #151515;
  text-align: center;
  padding-top: 40px;
}

.background-FFFFFF {
  background: #fff;
}

.md-title1 {
  font-size: 16px;
  font-weight: 400;
  color: #888;
  text-align: center;
}

.color-2B6BFF {
  color: #2b6bff;
}

.font-size-16 {
  font-size: 16px;
}

.list {
  line-height: 40px;
  margin-bottom: 20px;
}

.gg-box {
  padding: 50px;
}

.gg-box .title {
  font-size: 24px;
  color: #444;
  font-weight: 500;
  margin-bottom: 30px;
}

.gg-box .dec {
  /*color: #b8bcc8;*/
  text-indent: 24px;
  font-size: 16px;
  line-height: 30px;
}

.gg-box .title-bt {
  color: #ff9100;
  font-size: 18px;
  text-align: center;
  font-weight: 600;
  margin: 20px auto 20px;
}

.logo-box span {
  margin-left: 10px;
  font-size: 30px;
  font-family: Times;
}

.logo-box img {
  height: 50px;
  width: 50px;
}
.logo-box {
  position: fixed;
  left: 7%;
  top: 10%;
  color: #fff;
  text-align: left;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.logo-box span {
  margin-left: 10px;
  font-size: 30px;
  font-family: Times;
}

.logo-box img {
  height: 50px;
  width: 50px;
}
</style>
