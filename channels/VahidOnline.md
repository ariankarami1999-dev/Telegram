<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn1.telesco.pe/file/obvX0CH09Z3BTM1XYPcrBaHChPR4apsSftw8SH8kg_71RD46aoQBwQGYgIv-rrdKGHHyRnSgBPkaqHfuiPCStL8_fObZ1MDwpqPNhWSvuckhAkF9HE78AHxhottA6pAp4eA24ZW110f0QjoYko37b9tLDWJh1Y_M4KAZjb0iUWPHMxIMUg25h8OcFwcEQuQ_B1tjrXY4irnfS0jMmJNnKHCTkVY4PZGDFz6fZLpzEFCdABMH1EfjLojlbuiJ43s3onznJvP4HI9QXj7mR3PCU9Ux4vM-YqfCFpAP7HQdaTi0GvZUIVs55NyN_11r6eedN9j3hpTsDWrwEGvEBEc6uw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.42M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 17:17:09</div>
<hr>

<div class="tg-post" id="msg-77470">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U2OSwxsphK6JWXfb3N-p2AaTELOGm7CJs6KnuDUKpOfOsX8j9dmLg2U95YzhP2WDGug8yZCy_GFbalIABOkKbMS0O9nroC4G7hOb1zixzfIhXsQBAV_D72xfMbgwU6zJN62T84Ldgaz0gam6tBjCFWxzGkl-F2MEJm0k4Q4J_o9tRRO2CrPIgSoIVOAjLDSPYw1-emaNObTt7r05OAOGO8FvQvUaZ3ZDY6jOQaPo9rcB0S1b7TbPB2WesU3L-bTsvKJwzP5gprrD63S83GWB7mg39PNUhTB7zI3lue4M3afk5RE9_AJUoKrULopesBAFUJeBTHBZCKcsfSFLo3xwww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ نوشته بود:
از این پس  خسارات حمله به کشتی‌ها از پول‌های بلوکه شده ایران پرداخت خواهد شد
واکنش عراقچی، ترجمه ماشین:
مصادره دارایی‌های یک کشور دیگر برای پرداخت مطالبات نامرتبطِ آینده، بدعتی آتش‌افروزانه است.
کسانی که از چنین منابعی استقبال می‌کنند یا از آن سود می‌برند، باید به یاد داشته باشند: وقتی دولت‌ها مصادره را به امری عادی تبدیل کنند، دیگر دارایی هیچ‌کس در امان نخواهد بود. هرج‌ومرجِ متعاقب آن نه زیبا خواهد بود و نه مسالمت‌آمیز.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77470" target="_blank">📅 06:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77460">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u8S9YALhdBVK-apVopRePOqTdqqkDgI9iEDRzL8A5Nee44lcw6gLXk3snNK2KJ_ppZ553dyEeXzIJFaoFYL_VpUBUC0J2jMqd7jbzSVfKLTKr9CkpvHLt2NMLHr-ExMEYlbV3NKroK7iOzBcCY98B9rIEGLknybLMKpU77flMGFXrv5oXhWfan7Mjr_MOzrmJ3Z3RFBik7AB3cseaoWp-X570Y5eHjYWhbaYArlmBHqPMvt6C3POEPlY8WEzDlSv7CYLT3h4xr3RmrMjahnxY1IEPb1aWM3NFikXf6xe-1weMZ_RAaEy7k9ivHI9sUg_ACxQbC0GscFBj5-Y8bD3hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QjxSCbJ1cG5FUHiQmJBnoNjt-Eeb38OpYtgze_1IebKWU0wB5_KSanIOP62OJassCd9LHRmJ1PtUkHyWYJ3kf4mqYAtsY3edPJGQ6uzyWOBS60diK28eNarQHJ44_Eq8rg66abZqx0bss6KVa7nRNl7_MkbCJa0ttnS_BgEGTGd1ieRwvLQN_lWEcr61aDqk4DwIX-NoSXkGPyRnB0-y3fPrOLsZSRBCj5Io6nSDIZqHrSzmp0_wr0l0wE2AOQRY9twQw19FYJrfjJ-LIeRXgaj7oxk-II6UcnQ_Q2j8zzzaqfxQv7M6qOTjmYGwi9odeMje3dGQ7yfodgVLM_RA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uA3fd1QuiImiV1Elf7wenXgjN8vuzuTX2h1Yvd1psiS0bRlBpMn98ECWlMtJM6AIYcatrfRRebU2ood6Jd5ObupaCDZToOxsZMsnRhiNOXa1s_SJg2_zXNlWA2YLYW8U5WkbZGICcrcT7WntpzSQVATe_0GkUE0mRuVCOODwWsacemQUhMta9mEN8DyhTIe96xspowTbX2G_gKlB4v8GlK5GlpiKA45dFfsIRom4AanJFgnYb6xZ4WROeM5a6b3Mx-GhH-uBKD1qUZ_Uv8GapWgGtwf6scxf7LQA0H5e6K63DlJapJBEvqkOF-TrAP8O8iCPR4ltjZUkERkSzYA3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BtoxMDdisan8xWX1-NmrWMFpnEOgZfRFkP3B6z-ciT8Cq7csdOM6Lep6xDZDZC1hvK_QHJa9nBiYJ9HfIQP5CEELeHM13n3cIQZ-HS0YmDkHNxDFxG4d9AFb23kiztVTkaKemUTzcQkrT5Hp_ztmFnCDg7BvqxIE63RsvoO9m8wCLM51ZQV_08QnfYrCn4Nnb2GWmGdY8zp0dn-nUS7u6acIJfT-rPgyqa2cJv4x9RGn_43uKmhTO1hlv4YIMbebTNMc7xd32YzILrFeXRrPJZ6Jloa3NAuIsm4kmKrlgRbkcapRrg0_1QOkeddVFXXanMWC_KEvRdlN1a3wG6rBTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hDvGMjKqY9UK5S5B8R7wAQtXD19z4NtaBnghMjt6Jt5XgGMTuw6JdVi7RrC2Ovk8SsOpjWGLMYihri53g2o0shOTlc_gR9nk0DGdTH2ZQvneFXkkH7P5BRIS_q1y_fMe3e4EpBjiCWpuAxoOM_4FzrcSOlDtTKWKyU9zWiHvW9EVdc2Zoalgz01Of65Kgo9Bags4FvekPVuhuigREt5CoxbCJ4FCL3uEWuFUfQ8cG8RyOGL2P5v6LIYVJ7u4sD5ubePwSU7zUmBXfv52tK6qZVr9W5idDmr6NTHpDwGJCQcxpArzAUgi9wsDfIXbkSJqrWx9gxErpngPI8J5huVr5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o6kVlEKcx97qTGhxkFcM04gSDI5GoVi8yj9_JI8BtuEle6-SuY1xCTdoJdMjjos5duRh5Z2uzLQERG1zmRQdNBQOeH2zqT0HiOO61f2SaBXcD1cllI9IVRsLVMuOr84ZZ5IUfG6ZgXmTOuskO-8cZZSV7tNDI_XGCT1JFAQSzcVLPI8Ic2wwbHa8ozfSOEO56oq75Q-GLaaHlbXrAFbzT_dgaq21FtkohNhwAqX25X7LfVZ3mhJL_TMa47xWwqSi1cjU_TcEXq4Kfp0eRaiFX89KPtt-Ovi0k1BFP92hMNLovin1gD9Mu6_S69di_XOQ6WrMw0bDzXu7z8xE4izxtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a1c04c15b.mp4?token=tvsNyvJg--GLdmZpVAEzuNT-TOWwSSxRPlTgvlilXeEN3UARzH7qc44nkkSj_Md4oXkbjiHL9XuOUmgL5nTqDmAiWVuCol99i_t2biETROz_CS7ZfLSi2JcwRy-1CJ8mNb-EVBpRUGoX6KadnxvzcO_fhjKP5YgfS_PIL5p7VtV1qTA52FsCGYxhMTYWR-vpjQN1-d_vQPGceGDBinP6GE0FhLcxnvTpqM-gpU1U3cRKQvS3X7wSCKHByW4LZ1rqniYxSToRRww5OhJ6BaI_0WKz1VfTwpkfOJWcaKHJiUSMzJS5sFyt13-xY02wewXb9rj4X3o_7qNDzmNpeLRspw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a1c04c15b.mp4?token=tvsNyvJg--GLdmZpVAEzuNT-TOWwSSxRPlTgvlilXeEN3UARzH7qc44nkkSj_Md4oXkbjiHL9XuOUmgL5nTqDmAiWVuCol99i_t2biETROz_CS7ZfLSi2JcwRy-1CJ8mNb-EVBpRUGoX6KadnxvzcO_fhjKP5YgfS_PIL5p7VtV1qTA52FsCGYxhMTYWR-vpjQN1-d_vQPGceGDBinP6GE0FhLcxnvTpqM-gpU1U3cRKQvS3X7wSCKHByW4LZ1rqniYxSToRRww5OhJ6BaI_0WKz1VfTwpkfOJWcaKHJiUSMzJS5sFyt13-xY02wewXb9rj4X3o_7qNDzmNpeLRspw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آپدیت: پرتاب موشک از بیدگنه، خمین، نجف‌آباد، شاهین‌شهر و...
تصاویر بالا و پیام‌های دریافتی از استان تهران:
همین الان از ملارد موشک زدن
همین الان ساعت ۵:۵۲ از بیدگنه موشک زدن
سلام وحید جان همین الان موشک از رو پرند رد شد
سلام همین الان 5:51 از ملارد موشک شلیک شد
از بيدگنه موشك فرستادن الان ساعت ٥:٥٠
شلیک موشک از بیدگنه ملارد ساعت 5:50 بامداد
۵:۵۰ دقیقه از بیدگنه موشک زدن رفت بالا
سلام وحید جان از [....] بیدگنه الان موشک هوا کردند بعد جنگ ۴۰ روزه این دومیش بود
سلام وحید ما فردیسیم همین الان از سمت بیدگنه فک کنم موشک پرتاب کردن و صدای شدیدی اومد و لرزید ساعت ۵.۵۱
5.52 از کرج موشک فرستادن ردش هم تو اسمون افتاد
اشتباه نکنم از بیدگنه
وحید جان سلام.  رد موشک از سمت اندیشه  شهریار خیلی صدای مهیبی داشت همین الان ساعت  ۵.۵۲
آقا وحید سلام ساعت 05:50  از بیدگنه ملارد موشک رفت
سلام. روز خوش از بیدگنه موشک فرستادن
جمعه دوم مرداد ساعت ۵:۵۳ شلیک موشک از [...] بیدگنه واقع در ملارد به سمت جنوب غربی
🔄
وحید جان همین الان دومی هم فرستادن ساعت ۶:۰۰
سلام وحید جان همین الان موشک از رو پرند رد شد
شلیک دومین موشک پیاپی از ملارد
از ملار یکی دیگه شلیک شد  6:00
دوباره موشک زدن از ملارد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77460" target="_blank">📅 05:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77459">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/08e419bbe8.mp4?token=oYioFfo0aHYfsEGbEtiJX-r2E_4QEWJ1jAqfcZ1wnYKH8pDiza9QmJf1I4j24srgVOvF2aF5NogyyVDEwi_wLBDoROGSejdUA2FtfpkvnGRHGimn3Fq54xumaN0mrJJz0HKB3ZXWewfLJK_Kis3tx1H_0W2Gt5_TlOkU__-r5VhRXx7jERcMEPXuFrVue02kKBCK8w5O4K4cMCCWRIfMZh_ctUvk1Y-tVhyqpEUWkUVvtpvtmdovy5c2k9oOJPGeAWAeMCW4HdZCc1UHjidlGWI1yK3ABCkKgWGfY7lSpYKOLc1LZ0xeolHx3tk7yodsdmdQDR5BQlLsBTXAktBrdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/08e419bbe8.mp4?token=oYioFfo0aHYfsEGbEtiJX-r2E_4QEWJ1jAqfcZ1wnYKH8pDiza9QmJf1I4j24srgVOvF2aF5NogyyVDEwi_wLBDoROGSejdUA2FtfpkvnGRHGimn3Fq54xumaN0mrJJz0HKB3ZXWewfLJK_Kis3tx1H_0W2Gt5_TlOkU__-r5VhRXx7jERcMEPXuFrVue02kKBCK8w5O4K4cMCCWRIfMZh_ctUvk1Y-tVhyqpEUWkUVvtpvtmdovy5c2k9oOJPGeAWAeMCW4HdZCc1UHjidlGWI1yK3ABCkKgWGfY7lSpYKOLc1LZ0xeolHx3tk7yodsdmdQDR5BQlLsBTXAktBrdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"آمریکا سیزدهمین شب حملات به اهداف نظامی ایران را به پایان رساند"
پست سنتکام، ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) ساعت ۹ شب ۲۳ ژوئیه به وقت شرق آمریکا [۴:۳۰ صبح به وقت تهران]، سیزدهمین شب پیاپی حملات علیه ایران را با موفقیت به پایان رساندند.
سنتکام مراکز فرماندهی نظامی ایران، تأسیسات نگهداری پهپادها، شبکه‌های ارتباطی، سایت‌های نظارت ساحلی و توانمندی‌های دریایی را هدف قرار داد تا تهدید ایران علیه دریانوردان غیرنظامی و کشتی‌های تجاری در حال عبور از تنگه هرمز را بیش از پیش کاهش دهد.
این آبراه بین‌المللی، با وجود حملات اخیر سپاه پاسداران انقلاب اسلامی ایران، همچنان برای عبور و مرور باز است. کشتی‌های تجاری با پشتیبانی نظامی ایالات متحده همچنان آزادانه در این تنگه تردد می‌کنند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه در حال فعالیت هستند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77459" target="_blank">📅 04:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77458">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان همین الان صدای انفجار خرمشهر
درود خرمشهر صدای انفجار ۴:۴۰
خرمشهرو زدن
سلام وحید خرمشهرو همین الان یه موشک زد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77458" target="_blank">📅 04:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77457">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پیام‌های دریافتی:
سلام الان یزد صدای انفجار اومد
سلام یزد رو الان زدن
یزد یه صدا انفجار اومد ساعت ۴/۴۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77457" target="_blank">📅 04:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77456">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">چند پیام دریافتی از فیروزآباد در استان فارس:
سلام فیروزابادو هم ساعت ۳:۴۵ زدن
صدا اومد فیروز آباد فارس خونمون لرزید
نزدیکی فیروزآباد فارس چیزی شبیه انفجار رخ داد و موجش بد جور گرفت مارو
الان صدای انفجار فیروزاباد
ساعت ۴ صبح
انفجار مهیب
سلام  فیروزآباد در خونه داشت از جا کنده میشد
دوسه نفر  میگن پل احمدآباد بوده که راه ارتباطی هستش به سمت جنوب
آپدیت ۴۰ دقیقه بعد: صدا و سیما
شنیده شدن صدای انفجار در فیروزآباد فارس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77456" target="_blank">📅 04:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77455">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان ساعت 3:43 صدا پدافند شرق تهران اومد ولی کم بود
ساعت ۳:۴۵ صدای پدافند شرق تهران فعال شد. از حکیمیه صداش میاد
پدافند شرق تهران فعال شد
سلام صدای انفجار در پردیس تهران [لابد انفجار شلیک‌های همون پدافندهای ضدهوایی است.]
الان هم پدافند زد
پدافند پردیس فعال شده.
شرق تهران صدای پدافند
[+ پیام‌های دیگری که با تفکیک اسم محلات مختلف شرق و شمال شرق تهران دارند فرستاده میشن و دیگه نقل نمی‌کنم چون همین محتواست که هی داره تکرار میشه.]
آپدیت:
بعد از چند دقیقه تموم شد.
🔄
ساعت ۴:۱۰
دوباره صدای پدافند شنیده شده در شمال شرق تهران
🔄
ساعت ۴:۲۲
پیام‌های دیگری درباره شنیدن صدای پدافند در شمال شرق تهران
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/77455" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77454">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iv8Z2PmRAyjIrJyLUKFID9qgxtZ36uShZgVunGAn8JeF-xWCS7QKtQzIMVeeB--jz7_JcqPJYRjLDIloVr9_lhgu45itDADwypDeVqs2ObRxiZed8Lf07Wj813zTpEigyuC7wxnHKdJQLAyYVWlRbH46hcQsM80lHL5wO-X8kvTk810Qn31hQ3HsLvdUSPnvauYTrfRE5a17I0BcsYmovTrqwc02yzX5nLSUW6GiV0tlkFvvS53a22zqVmEm_mpzjISv2bUjfGyh6QYYQllpPkIeBrHHxgXLd5VIU2WWKhvRpX8Uvp_zEtTXBPBXFy7PKXqLmRTNa-lZL47MdZKSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: تفت در استان یزد
پیام‌هایی دریافتی و تایید نشده درباره مناطق مرکزی کشور:
ساعت ۳.۰۵ دقیقه شهرستان خنداب صدای انفجار خیلی بلند اومد
سلام خنداب و زدن 3:05
نزدیک خنداب صداهای وحشتناکی میاد
آپدیت: منابع حکومتی
معاون سیاسی، امنیتی و اجتماعی استانداری مرکزی گفت: یک نقطه در خارج از شهر خنداب دقایقی پیش هدف ۲ پرتابه دشمن قرار گرفت.
———
سلام وحیدجان همین الان پایگاه نیروهوایی انارک نایین را زدن
آپدیت چند ساعت بعد: منابع حکومتی
معاون استانداری اصفهان: ساعت سه بامداد امروز منطقه‌ای در شهرستان نایین مورد تجاوز دشمن متجاوز آمریکایی قرار گرفت.
———
تفت از یزد هستم
از سمت بام تفت - شیرکوه رو بد زدن
خیلی صداش بلند بود
ساعت ۳.۳۰ دقیقه تفت صدای انفجار امد.
دکل تفتکوه رو منفجر کرد
سلام ۳:۳۰ تفت استان یزد صدای انفجار مهیبی اومد که از خواب بیدار شدیم. از کوه های اطراف نور و گرد و غبار شدید بیرون آمده.
داخل شهر نبود
سلام وحید جان .ساعت ۳.۳۰ تفت یزد صدای انفجار شدید اومد و خونه ها لرزید.
صدا از تفتکوه محل منطقه گردشگری در حال ساخت بام تفت بود که از اول جنگ کلیه نگهبانان و پرسنل را سپاه تخلیه کرده و هیچکس اجازه رفت و آمد ندارد
خبرگزاری‌های محلی میگن موشک بوده و جنگنده اصلا صداش شنیده نشده
آپدیت: صدا و سیما
صدای انفجار در خارج محدوده شهر تفت در استان یزد
———
بروجرد انگار زدن صدای انفجار اومد. دو انفجار پیاپی
بروجرد زدنننن
صداش وحشتناک بود
بروجرد صدای انفجار شدیدی اومد
دو تا پشت هم
آپدیت:
در بروجرد فقط صدای عبور جنگنده شنیدم
اما صدای انفجاری نشنیدم
از باقی همشهریان هم پرسیدم نشنیده بودن.
صدای جنگنده شبیه  جنگ ۴۰ روزه بود که بعدش خبر بمباران خرم آباد اومد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/77454" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77453">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rs2r6eibGRTEbPH15OU-CfMU5i5OqQbmHJUSzWV9-7VwXncLU0pOF5-AKbY4l9FMGT5WifVjsUYOCqIyZHyVxBmks35I6_hBZhO4Ux2b6nbygdwc6VI2M8o5OHTnne7FXoBDoNPBnMq_eF9ktwJsV13V24CXwMH6RO-tHSPs4v2d8DyxOtzQUh1BQlwlTTjHMnai3-eex3cwHQ4KWu7Icnhxqk_4sAkjmjjKfh1NiX-GmJaHbJscNXu7bYdwTGruzThF9ctEoFQojxxRzghKaPQ7uWViywfyyDsUbKUhh6L1lfoaOGi-uAXJxxtwhN4Q0f4ucocj2YGREy0-7BsO6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش تسنیم، معاون امنیتی و انتظامی استاندار خوزستان اعلام کرد که ساعت ۲:۵۰ بامداد جمعه، نقاطی در اطراف شهرهای اندیمشک و امیدیه هدف حمله موشکی آمریکا قرار گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/77453" target="_blank">📅 03:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77452">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پیام‌های دریافتی:
خرم‌آباد ساعت 3:19 دقیقه صدای انفجار شدید.
خرم آباد الان انفجار شدید
همین الان صدای انفجار خرم اباد ۳:۲۰
سلام خرم آباد همین الان ساعت 3:19 دو انفجار شدید
سلام خرم اباد وحشتناک پنجره لرزید
خرم آباد زدن یه حالت لرزش هم داشت
خرم اباد وحشتناک شیشه هامون لرزید
سلام همین الان از خرم اباد موشک پرتاپ شد
آپدیت: منابع حکومتی
معاون سیاسی، امنیتی و اجتماعی استاندار لرستان گفت: یک نقطه از شهر خرم‌آباد دقایقی پیش هدف پرتابه دشمن قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77452" target="_blank">📅 03:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77449">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KUH8i6_5blVyK_bP09ppM41FosTTlY_nwnO8rsHYCGTcU5yX3Et-a9SrhyFUtQ-2Kga6V7-FP3w-GIKQCiIX03aHQNUuybvvdmUaoaDSJnA-3opfxudRv8IGfusALGt0Ne0PIqswkgurZNZIEkLbdYlyaWVqQGMZUYoXS6GNQ8Zt9P07F_wxiIY0CBegvAUJ6hMqRXiR4A7XkXvjr2zQSjpwzoBVEs6IOTpKs5fcSqil9z00v6VrViwTxm22JvlreQAAOAOtQd64um7yjUDKcgCnnlKsXRG34gR-TpYL1Ko-qJqGx1j3wivCZ1hd3NaZruv22gYL-RgrvDd79dylyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/77449" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77448">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gPyD4-w42je2L1Xdr3uEfrJG3IE2Q--xMCdIQoJ53AvbFlusLribAHVX5LEEutG4q6HhoxegSmom1jUp-6bC4Ppv4em1Xp0yRqF7VWbvP1vjyP05PKDsfWa0la0x4n6IMh8tRlBxEvxHOKFt55MOQVbAnq9RbgIz2idpZY1GQBDVfRF5gkm7alETTz_H-p4J1DUVyr3APS07w3RMIeuWDGgVii6z917GsV25uXXxn1qRaDOZPhHalsCNOKwIt_uukHvgf9U-qTUKD5t7U0mFBueKMqYHJZxFcleixj9XwLlb2UmPjz4Gm-RyyDTfwAPwJRTxa4ocf4LZaXAjEJybog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: سیزدهمین شب حمله را آغاز کردیم
ترجمه ماشین:
نیروهای آمریکایی امروز ساعت ۶:۴۵ عصر به وقت شرق آمریکا [۲:۱۵ به وقت تهران]، دور دیگری از حملات شبانه به اهداف نظامی ایران را آغاز کردند.
این سیزدهمین شب متوالی حملات است که با هدف پاسخگو کردن ایران و کاهش تهدیدهای سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77448" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77447">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a1bff03107.mp4?token=XOcDpdDVA04EZnExX6Od4pwZ1Ej5tlgrtPNC6Ea7pJXLWJc1K83vXnHcqqTpcJxzbcDIdaWMeKHcLSa2j-lm1aqmmZ4XIfq1a4WdBt-_3rH-oMtUlX9U0DdndJr9lu8AawGJORE6xGhqRHVrgQ1e-8EcJFpp6GY9ivSBYQkB5jUFs6beDC7fVydu-KVvtikb5WDZ6dp38k7lko1S-WMBJUat_eIT2_lJijRk_83NwELIJQKv_cs8YvpRLN8Y-Z1EkjC0IKEZL77-dwf-otW9omjiRIBE8gu2ovWPAAPg-fSx0muGk9ZAMWceVdlbiMzuyui7Z7LMKJVTiWffcOIM6g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a1bff03107.mp4?token=XOcDpdDVA04EZnExX6Od4pwZ1Ej5tlgrtPNC6Ea7pJXLWJc1K83vXnHcqqTpcJxzbcDIdaWMeKHcLSa2j-lm1aqmmZ4XIfq1a4WdBt-_3rH-oMtUlX9U0DdndJr9lu8AawGJORE6xGhqRHVrgQ1e-8EcJFpp6GY9ivSBYQkB5jUFs6beDC7fVydu-KVvtikb5WDZ6dp38k7lko1S-WMBJUat_eIT2_lJijRk_83NwELIJQKv_cs8YvpRLN8Y-Z1EkjC0IKEZL77-dwf-otW9omjiRIBE8gu2ovWPAAPg-fSx0muGk9ZAMWceVdlbiMzuyui7Z7LMKJVTiWffcOIM6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
داداش
بندر
زد
همین الان
بندرعباس
سلام بندرعباس همین الان صدای چندتا انفجار پشت هم اومد
ساعت ۲:۴۱ دقیقه صدای انفجار بندرعباس
سلام بندرعباس انفجار های شدید پیایی غرب منطقه ۴
بندرعباس 2 انفجار
سلام وحید بندرعباسو زدن 2:41
بندرعباس ٠٢:٤١ يه صداي انفجار خيلي بلند كه مركز شهر  قشنگ حس شد
سلام بندرعباس همین الان چندتا زدن خیلی بدد برق قطع شد صدای انفجار بد بود
🔄
بندرعباس صدای انفجار بلند ۲:۴۱
2.42 چند انفجار بندرعباس پشت سر هم سنگین
3تا دیگه
٠٢:٤٢ سه تا ديگه پشت سرهم
صدا و موج زيادي داره
سلام وحید بندرعباس انفجار وحشتناک
دوباره داره میزنه خیلی بد میزنه
بندرعباس ۲:۴۲ صدای انفجار دی در پی
دوتا دیگه پشت سرهم زدن
۵ تا انفجار شدید  بندرعباس مجدد منطقه ۴ ۲:۴۳
سلام یه صداهایی میاد بندرعباس فکر کنم صدای انفجاره اما دوره
وحید بندرعباس ۲:۴۲ صدای انفجار بدجور میزنه
ساعت ۲:۴۱ در خونه دوبار لرزید
غرب جزیره قشم
بندرعباس همین الان هفت تا هشت انفجار خیلی قوی داشت
آقا وحید بندر خیلی شدید بود بیش از ۵ تا بیشتر.</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77447" target="_blank">📅 02:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77446">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab7e6ef3aa.mp4?token=RvIevNtSLYzdnsFuq-thoXGiayt6KefmAkPdNDQZa3GYYfbLtpf2oEqHaDusAtcPyxjdM3n-W1O9ULC7cFBzr6gPAI7l7W7OBs0ZgePMqN0uFBObhXtaADd-Flehd8OyYeQ_01ADYmDXGTFrtxKjDMX0hdM02SdQ8dO6nXxg7mA74WVs6lgoGWwxA86iRvQNj7T3w5AEdfLc-qJ0J-FRUuA2ohQQyaXFm6bAnfI5f9Q_Cftlkz4EX7tEB2_2LWQ57dvvpyz0r5t-6kh0wJEDY1bmdz4J3cRmKYSETZQYazpm5g3HweMxkx-2ZmFgC217iWfbnr3tkkiVH6T8B3NtiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab7e6ef3aa.mp4?token=RvIevNtSLYzdnsFuq-thoXGiayt6KefmAkPdNDQZa3GYYfbLtpf2oEqHaDusAtcPyxjdM3n-W1O9ULC7cFBzr6gPAI7l7W7OBs0ZgePMqN0uFBObhXtaADd-Flehd8OyYeQ_01ADYmDXGTFrtxKjDMX0hdM02SdQ8dO6nXxg7mA74WVs6lgoGWwxA86iRvQNj7T3w5AEdfLc-qJ0J-FRUuA2ohQQyaXFm6bAnfI5f9Q_Cftlkz4EX7tEB2_2LWQ57dvvpyz0r5t-6kh0wJEDY1bmdz4J3cRmKYSETZQYazpm5g3HweMxkx-2ZmFgC217iWfbnr3tkkiVH6T8B3NtiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌‌های دریافتی:
اهوازو زدن
شدید زدن
سلام وحید صدای برخورد اهواز
اول ۳ تا خیلی دور بود
الان هم ۳ تا نزدیک بود
اقا وحید همین الان اهوازو بد زدن
اهواز انفجار ولی دور بود
اهواز ساعت ۲:۲۰ صدای انفجار اومد
اهواز صدای برخورد اومد 2:21
وحید رگباری زدن اهواز
ساعت ۲.۲۰
ساعت ۲:۲۵ یک انفجار شدید اهواز
سلام وحید ساعت ۲:۲۰ اهواز رو زدن
داداش اهواز صدا انفجار قطع نمیشه تقریبا ۲  دقیقس پشت هم داره بمبارون میکنه یجایی رو
اهواز ساعت ۲:۲۱ خیلی زدن بیشتر از ده تا
۰۲:۱۹ اهواز زدن
آقا وحید اهوازو شدید بمبارون کردن هنوزم ادامه داره
ساعت ۲:۲۵ یک انفجار شدید اهواز
انگار یه چیزی خورد زمین و ترکید
انفجارش طنین داشت
چیزی مثل رگبار
انفجار در اهواز 2:25
سلام ۲:۲۱اهوازو زدن از گلستان اهواز پیام میدم دور بود خیلی ولی کاملا صدا و لرزشش اومد
سلام وحید جان، اهواز رو زدن
خیلی شدید بود ساعت ۲:۲۲
سلام اهواز شیشه ها کامل لرزید مثل یه باد شدید بود
🔄
ساعت 02:24 مجددا شروع شد.
مجدد ۲:۲۴ انفجار شدید
یکی دیگه دوباره زد
انفجارش موج داره
ساعت ۲:۲۴ یه انفجار دیگه شدید بود
۲:۲۴ دوباره اهواز زدن
وحید دوباره صدای چندین انفجار
اهواز هنوز داره میزنه
اهواز رو پشت سرهم دارن میزنن
درود وحیدجان، ۴ ۵ تا انفجار عجیب در اهواز رخ داد، انفجارهاش با همیشه فرق دارن، با اینکه دورن و صدای کمی دارن ولی زمین و شیشه‌ها رو میلرزونن به یه صورت دلهره‌آوری
سلام اهواز ساعت ۲:۲۴ دیقه فرهنگ شهریم صداش اومد هرچند کم بود صداش ولی مشخص بود بمبه
انفجار ها توی اهواز همچنان ادامه داره
خیلی شدتش بیشتر از روزای قبله
کل خونه و پنجره ها دارن میلرزن
اهواز زاغه مهمات انفجارات پی در پی
اصلا تمومی نداره
۲:۳۲
۲:۳۳
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77446" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77445">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tz74IVsGgKHbGqZiHlv0OR7KoXHOh2LarCq2G8NfrpM0MBIY8s2ymgWg6iDNI1xZW3u96CrEK_0dPKVra4gYjnnkxLaoe3VvAZ9C0zLbNke4MrPzrY-u3R44mAHi_ojejJqgPREBr7ZQYedlyWpcZx8-Kyu7Wo0QxdV4nD6obN9oD2YreHNBuzRckcBVNoYdh1XE3aATBYYRlEkGhXy_6LXAV1UoFPrpB2-fPb6mWc5-pL8s-zXqPP9J-3aq-uMj6_T4Oe-JB9KqvzAi2eQgFMeTHVGo534Tk_BnAC7ArcE6tqmBTOIQWsTJjHbz6Tv8Dw6vWNmSVZ_-9PghLTskQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: خسارات حمله به کشتی‌ها از پول‌های بلوکه شده ایران پرداخت خواهد شد
ترجمه ماشین:
لطفاً این بیانیه را تا اطلاع ثانوی به‌منزله اعلام این موضوع تلقی کنید که
از این لحظه به بعد، هزینه هرگونه خسارت واردشده به کشتی‌ها، محموله‌ها یا هر چیز مرتبط با آنها، از محل پول‌های ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
این خسارت‌ها ممکن است بسیار قابل‌توجه باشند، اما با وجود این، این کار منصفانه و عادلانه است.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/77445" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77444">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mtNvWBgHEDGTY1SZDt4HP0hVm-qzEWKbLR6RcHXnwx1Sxxy3fFCjiQr0d1HXl6xXqNo3jkQnoruT2_DkTfd45ukgJKWs5BnFi0imIcPuEimFPVdIBo7Lmf-6TAOSDlEi-KLglywU2tpLMo4X-5rEv6iQZvoaJym4fPENLv3A60cyyWlVxAlYuiEiivtmTYvr3n71aMkmmdS-SKgG4_xeOHp3BK44l7cYQn0azJ9S5NC4Bf8nE3FdeC8nKsAvg3a7eUo0ytxDYbnFee77a8jdmus032Fnp9NNWcqnMLul1M12OY08a0U9qoaOnoADd0VrXgavu3WgnuJBa7ewHu_-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم: اصابت ۲ موشک آمریکایی به محدوده روستای مسن قشم
گزارش خبرنگار تسنیم:
🔹
ساعت ۲۳:۵۰ دو فروند موشک در جریان حمله دشمن آمریکایی به محدوده روستای مسن در جزیره قشم اصابت کرد.
براساس اطلاعات اولیه، این حمله در محدوده روستای مسن رخ داده و دستگاه‌های مسئول در حال بررسی ابعاد حادثه و ارزیابی خسارات احتمالی هستند.
من یک پیام داشتم ولی اون رو هم ساعت ۲۳:۳۳ دریافت کرده بودم:
سلام وحید جان
ساعت 23.30 صدای دو انفجار شدید  ذوالفقار قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77444" target="_blank">📅 01:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77443">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77443" target="_blank">📅 00:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77442">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=MlXaUPxX6vyLMY-7SQvGv8J1cX8Ec4dKInGNAsUg4HZFOcgZqQOanABCuxI7r_aHDbgkUqgvImTYJonVipLvs4Yh8tCRw20sx6uHgtrujwf-3z0Y2LPf5WTbBCWjxAflL3WovbCa8PhxSqNi0XEA_KS1AH2ynNy1vXdnaHNGDX9-70SWtAIS-GoEbSvVnh01G8OcE2SAhYqjzZpXE2zU-QFWf9WgVY23X6FtgNVranDI_9dlXUQV_0Ti2p9GUi-q8P4LA821nLQuoVK2B7UBD-HSmR3r9TQFhW2HIsceXr0b-7-NKR_tFcolnlMzp9tVXxz1RVj7-AEz57bSDw8Z_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=MlXaUPxX6vyLMY-7SQvGv8J1cX8Ec4dKInGNAsUg4HZFOcgZqQOanABCuxI7r_aHDbgkUqgvImTYJonVipLvs4Yh8tCRw20sx6uHgtrujwf-3z0Y2LPf5WTbBCWjxAflL3WovbCa8PhxSqNi0XEA_KS1AH2ynNy1vXdnaHNGDX9-70SWtAIS-GoEbSvVnh01G8OcE2SAhYqjzZpXE2zU-QFWf9WgVY23X6FtgNVranDI_9dlXUQV_0Ti2p9GUi-q8P4LA821nLQuoVK2B7UBD-HSmR3r9TQFhW2HIsceXr0b-7-NKR_tFcolnlMzp9tVXxz1RVj7-AEz57bSDw8Z_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی ترامپ، بخش‌هایی مربوط به ایران، ترجمه ماشین:
ما در برابر جمهوری اسلامی ایران بسیار خوب عمل می‌کنیم. عملکردمان فوق‌العاده خوب است. آن‌ها دوست دارند کاری بکنند، اما من می‌گویم هنوز آماده نیستند. به مقدار بیشتری از همین رفتار نیاز دارند. هنوز آماده نیستند. نیت‌های شومی دارند.
نمی‌توانیم اجازه بدهیم سلاح هسته‌ای داشته باشند. اگر همهٔ این کارهایی را که درباره‌شان صحبت می‌کنم، از جمله کارهای مربوط به مراکز دادهٔ شما، انجام دهیم، مگر این موضوع مهم نیست؟ وقتی شروع کنند جوامع را یکی پس از دیگری نابود کنند، نمی‌توانیم اجازه بدهیم حتی به داشتن سلاح هسته‌ای فکر کنند. دقیقاً همین اتفاق در حال رخ دادن است. در دوران من هرگز سلاح هسته‌ای نخواهند داشت.
ضمناً، این کار باید به‌دست دیگران انجام می‌شد. تقریباً سه سال است که می‌گویند ۴۷ سال گذشته، اما این کار باید ۵۰ سال پیش به‌دست رؤسای جمهور دیگر آمریکا یا کشورهای دیگر انجام می‌شد. لازم نبود ما این کار را انجام بدهیم، اما ظاهراً اگر ما انجامش ندهیم، هیچ‌کس دیگری هم آن را انجام نخواهد داد. من انجامش می‌دهم و هیچ‌کس دیگری توانایی انجام آن را ندارد.
ما در دورهٔ نخست ریاست‌جمهوری من بزرگ‌ترین ارتش جهان را ساختیم. کمی بیشتر از آنچه فکر می‌کردم از آن استفاده می‌کنیم، اما اشکالی ندارد.
ونزوئلا را داشتیم. کریس در آنجا کار فوق‌العاده‌ای انجام می‌دهد. هزینهٔ آن جنگ را چندین و چند بار جبران کرده‌ایم. میلیون‌ها و میلیون‌ها بشکه نفت برمی‌داریم و آن نفت به هیوستون و لوئیزیانا می‌رود. خودتان می‌دانید؛ آن کشتی‌ها را می‌بینید که صف کشیده‌اند.
باز هم می‌گویم، هزینهٔ آن را بارها و بارها جبران کرده‌ایم و رابطهٔ بسیار خوبی با ونزوئلا داریم. مردم ونزوئلا اکنون خوشحال‌اند و نمی‌توانند آنچه رخ داده را باور کنند. بزرگ‌ترین شرکت‌ها و بزرگ‌ترین شرکت‌های نفتی جهان وارد آنجا می‌شوند و به شکلی تجارت می‌کنند که هیچ‌کس تصورش را نمی‌کرد.
ما هم سهمی برمی‌داریم؛ باید هم برداریم. آن‌ها هم سهمی می‌برند. بسیار جالب است که اکنون پول بیشتری درمی‌آورند. کریس ارقامی را به من نشان می‌داد. ونزوئلا اکنون بیشتر از هر زمان دیگری پول درمی‌آورد. ما هم پول زیادی درمی‌آوریم و فکر می‌کنم حقمان است.
بنابراین واقعاً اتفاقی بود که [نامفهوم]. یک جنگ یک‌روزه بود؛ یک روز طول کشید. مردم می‌گفتند: «قرار است آنجا برای همیشه گرفتار شویم.»
اما می‌دانید، ما ۲۰ سال در ویتنام بودیم و در آن جنگ هزاران و صدها هزار نفر را از دست دادیم؛ دست‌کم هزاران و هزاران نفر. سال‌ها در افغانستان بودیم. در تمام این جنگ‌هایی که درباره‌شان شنیده‌اید، سال‌های سال حضور داشتیم. این‌ها همان جنگ‌هایی بودند که من آن‌ها را جنگ‌های بی‌پایان می‌نامیدم.
اما این بار چهار ماه است که درگیر هستیم. دیروز روز بسیار غم‌انگیزی داشتم. به دوور رفتم. چهار میهن‌پرست بزرگ آمریکایی کشته شدند. این یعنی ۱۸ کشته در دو جنگ. حتی یک نفر هم بیش از حد است، اما شمارشان ۱۸ نفر است.
در حالی که در ویتنام ۲۰۰ هزار نفر را از دست دادیم. هزاران و هزاران نفر را از دست دادیم. در افغانستان و در هر جنگی هزاران نفر را از دست دادیم. در جنگ کره نیز هزاران نفر کشته شدند. همهٔ این جنگ‌ها سال‌ها طول کشیدند.
ما می‌خواهیم این را تمام کنیم و می‌خواهیم درست انجامش بدهیم. اما باید کاری را که برایش آمده‌ایم انجام دهیم. نمی‌توانیم اجازه بدهیم این افراد بسیار خشونت‌طلب به چیزی که می‌خواهند، یعنی سلاح‌های هسته‌ای، دست پیدا کنند.
[...]
بنابراین فقط می‌خواهم در پایان بگویم که حضور در اینجا افتخار بزرگی است. اکنون می‌روم تا دربارهٔ موضوعات گوناگون صحبت کنم. یکی از آن‌ها جنگ ایران است که باز هم می‌گویم در آن بسیار خوب عمل می‌کنیم؛ بسیار بسیار خوب. می‌گویم بهتر از چیزی که هر کسی انتظار داشت قابل انجام باشد.
نیروی دریایی و نیروی هوایی‌شان را از کار انداخته‌ایم. تمام رادارهایشان و بخش عمدهٔ توانایی‌شان را در زمینهٔ تولید از بین برده‌ایم. توان پهپادی‌شان ۸۴ درصد و توان موشکی‌شان ۹۱ درصد کاهش یافته است.
بعد روزنامه‌ای نوشت: «آن‌ها اکنون در موقعیت قوی‌تری نسبت به چهار ماه پیش قرار دارند.»
نه، این حقیقت ندارد. درست نیست. باورم نمی‌شود حتی اجازه دارند چنین چیزی بگویند. نیویورک‌تایمز نوشت: «آن‌ها اکنون در موقعیت قوی‌تری قرار دارند.»
آن‌ها ارتشی ندارند. نیروی دریایی ندارند. کارشان تمام است. ۱۵۹ کشتی داشتند که همهٔ آن‌ها در کف دریا هستند. ۲۱۲ هواپیما داشتند که همه از بین رفته‌اند. رادار ندارند. پدافند هوایی ندارند. هیچ‌چیز ندارند؛ جز اینکه خشن و باهوش‌اند و هنوز مقداری توانایی دارند.
اما چهار ماه پیش، باور کنید، بسیار بسیار قوی‌تر بودند. متوجهید؟ می‌خواهم خبر واقعی را به شما بدهم.
The White House
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77442" target="_blank">📅 23:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77441">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
افراد نفوذی در دولت آمریکا سرشان را زیر برف کرده‌اند.
آن‌ها واقعیت‌های میدانی را نادیده می‌گیرند و به نظر می‌رسد فقط روی سال ۲۰۲۸ تمرکز کرده‌اند.
تجاوزگری بی‌فکرانه‌ای که از آن حمایت می‌کنند، تنها باعث خواهد شد رئیس‌جمهور آمریکا برای توافقی که در تلاش برای دستیابی به آن است، بهای سنگین‌تری بپردازد.
Compromised individuals in the U.S. administration are burying their heads in the sand.
They ignore the realities on the ground and seem focused only on 2028.
The mindless aggression they advocate will only ensure that POTUS pays heavier price for deal he's trying to achieve.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77441" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77440">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vg62Dh5jkwEDrbw5x3nWofpmoh61fNHjqjgmr7i43NEHjiRCS74bO5fxpixz0Uq9hqKhT3y-Bucy-RrWCEFgT-Y5WCDizYSGZrOAD-BCv9laN7dC_bFFYwz7hWYeJthImyLGVBpedYY5QGTuIHlV8ny6UZinK1sS7u-XHyvVbz8Xw9rChUYeFb5PJiT6kOvseS78XTCJ7lSmtwd6d44LPfk0ENQK6hQtT5kMv7jQchVar-5wDA2RFQ2zRoQw6KTN4dtVqQNVS0zvwkqPfHFfsLL5UA-jHNp1TeiasB8uxWkq39RLZGmVDfbDocKVArbFi7UJLZKPcX7ZWND-mRoBlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: هشدار در کویت
هم‌زمان با پیام‌های دریافتی درباره پرتاب موشک از اهواز
آپدیت:
ارتش کویت پنج‌شنبه شب اعلام کرد که نیروهای نظامی ایران بار دیگر خاک این کشور در حاشیه خلیج فارس را هدف گرفته‌اند.
رسانه‌های حکومتی در ایران نوشته‌اند که هدف این حملات تازه پایگاه علی السالم کویت بوده است.
در همین زمینه ارتش کویت در شبکه‌های اجتماعی از جمله شبکه ایکس خبر داد که موشک‌ها و پهپادهای ایران توسط ضدهوایی‌های این کشور رهگیری شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77440" target="_blank">📅 23:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77439">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=MqvS9BqjGUxMUQiyM7Ss9C2H56pCo-Do_QEzv_eJxy5vthY6PZSvitDQ510KXDn1g5ELS79SZyO-HIHWAI27UKUn3x2GnPbn-e5XyfQnOcklEMzelNNC8wNltDSEOMB_BowTGSxbNwdPXybQN7NpVZEmibjS5hQQke8O-vsks4f0jKHQDA0vnzM9C33MoyZRo49kw9xl4is8vNMMu6tt7h5ojIc2zjnqxeOwXbZtkWsKwsdX6jAU2CwlrzVg5BI9Qrxgr8b7z_o17PyW4G05xKswLRsRjBPTmsjNTwcP4XdlYEtkoON31vkyikN27sAeFKUM-TgVWumLICWywoc-1wEvVRRk1oOh6SJx2Ev_0seDwTk7mfdl-jk3ks3wK_k5hqCzmkb7PN1rCM_ab3hECKqcrfpetxDXZAI88WGS5UZVKRr_20XWVWpKdfStxSFrUpLoUQas2VifNNliuzF7zH1wO5KCSNUxyEeOHJEqgdP874BZwZo0rC7AO95YckWlbkCMqgBSxyN12ufir8TUICQ0Zg8gZrMahdrpkVjHWMAEdbqN7FtuOz34mMgn_fXk7MBkm80pdWOyc-SHCjMLAsxGUo9Qi0uiqD6UFQskc5a6FgEb_xWVgO2loQOssLb4r9_u6VIiOQs2saAN-Drp4DV-_ZkaObg_neyhsAbqeo0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=MqvS9BqjGUxMUQiyM7Ss9C2H56pCo-Do_QEzv_eJxy5vthY6PZSvitDQ510KXDn1g5ELS79SZyO-HIHWAI27UKUn3x2GnPbn-e5XyfQnOcklEMzelNNC8wNltDSEOMB_BowTGSxbNwdPXybQN7NpVZEmibjS5hQQke8O-vsks4f0jKHQDA0vnzM9C33MoyZRo49kw9xl4is8vNMMu6tt7h5ojIc2zjnqxeOwXbZtkWsKwsdX6jAU2CwlrzVg5BI9Qrxgr8b7z_o17PyW4G05xKswLRsRjBPTmsjNTwcP4XdlYEtkoON31vkyikN27sAeFKUM-TgVWumLICWywoc-1wEvVRRk1oOh6SJx2Ev_0seDwTk7mfdl-jk3ks3wK_k5hqCzmkb7PN1rCM_ab3hECKqcrfpetxDXZAI88WGS5UZVKRr_20XWVWpKdfStxSFrUpLoUQas2VifNNliuzF7zH1wO5KCSNUxyEeOHJEqgdP874BZwZo0rC7AO95YckWlbkCMqgBSxyN12ufir8TUICQ0Zg8gZrMahdrpkVjHWMAEdbqN7FtuOz34mMgn_fXk7MBkm80pdWOyc-SHCjMLAsxGUo9Qi0uiqD6UFQskc5a6FgEb_xWVgO2loQOssLb4r9_u6VIiOQs2saAN-Drp4DV-_ZkaObg_neyhsAbqeo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجریان فاکس‌نیوز، متن زیرنویس، ترجمه ماشین:
مجری:
بیایید نگاهی بیندازیم به نیروگاه‌ها و مکان‌هایی که ممکن است بتوانیم هدف قرار بدهیم. لوکاس، وقتی به این‌ها به‌عنوان اهداف احتمالی نگاه می‌کنی، فکر می‌کنی اول از همه کجا را ممکن است بزنیم؟
لوکاس:
خب، نمی‌دانم نخستین هدف باشد یا نه، اما نیروگاه دماوند ۴۰ درصد برق تهران را تأمین می‌کند. نیروگاه هسته‌ای بوشهر هم احتمالاً هدف قرار نخواهد گرفت. روس‌ها آن را ساخته‌اند و هنوز هم اورانیوم با غنای پایین در اختیار ایران می‌گذارند.
مجری:
چون، لوکاس، باید بگوییم که منفجر کردن یک نیروگاه هسته‌ای خطرهایی دارد.
لوکاس:
بدون تردید. میدان گازی پارس جنوبی هم روی بزرگ‌ترین میدان گاز طبیعی جهان قرار دارد. نیروهای اسرائیلی در ۱۸ مارس، در آغاز جنگ، آن را هدف قرار دادند و ایران هم با حمله به بخش قطری همین میدان گاز طبیعی پاسخ داد.
مجری:
اگر بخواهیم در همان تنگه‌ای که آن‌ها در آن به کشتی‌ها حمله می‌کنند پیام بفرستیم، آیا آنجا جایی نیست که باید سراغش برویم؟
لوکاس:
چرا؛ فقط سؤال این است که پاسخ ایران چه خواهد بود. دیده‌ایم که ایران تلافی می‌کند. تأسیسات گاز طبیعی قطر و میدان‌های نفتی امارات، نگرانی اصلی همین است.
مجری:
یعنی اگر ما یک نیروگاه را بزنیم، آن‌ها هم پاسخی مشابه خواهند داد؟
لوکاس:
بی‌تردید. تمام این مدت ماجرا همین مقابله‌به‌مثل بوده است. نکته قابل توجه درباره اسرائیلی‌ها این است که آن‌ها پاسخ‌هایی نامتناسب می‌دهند. احتمالاً یکی از دلایلی که اسرائیل دوباره وارد جنگ نشده همین است. ایران از اوایل ژوئن به اسرائیل حمله نکرده است.
مجری:
ارزیابی تو از شیوه‌ای که اکنون عمل می‌کنیم چیست؟ فکر می‌کنی پاسخ ما نامتناسب است یا می‌توانست نامتناسب‌تر باشد؟
لوکاس:
پاسخ ما نامتناسب نیست. نکته قابل توجه این است که نیروهای آمریکا، پس از آنکه یک پایگاه آمریکایی در اردن هدف قرار گرفت، به پادگان‌های ایران حمله کردند؛ همان حمله‌ای که سه سرباز ارتش آمریکا را کشت.
مجری:
پس این همان نیروگاهی است که ممکن است هدف قرار بدهیم. این مهم‌ترین مورد است. برویم آن طرف نقشه؛ اینجا «کوه کلنگ» یا Pickaxe Mountain است.
لوکاس:
ارزیابی اطلاعاتی آمریکا این است که ایران احتمالاً چند روز پیش از عملیات «چکش نیمه‌شب» در یک سال قبل، بخشی از اورانیوم غنی‌شده خود را از فردو به کوه کلنگ منتقل کرده است.
این محل بسیار عمیق‌تر از دیگر تأسیسات هسته‌ای است. همچنین اینجا کوه‌های زاگرس است و با سنگ دولومیت بسیار سخت روبه‌رو هستیم؛ بنابراین حمله هوایی به آن بسیار دشوار خواهد بود. این یکی از دلایلی است که شاید از نیروی زمینی استفاده شود.
در واقع، چنین مأموریتی برای نیروهای مأموریت ویژه ارتش آمریکا است؛ نیروهایی مانند دلتا، تیم ششم سیل و اسکادران ۲۴ تاکتیک‌های ویژه نیروی هوایی.
ریسک ماجرا این است که هیچ‌کس دقیقاً نمی‌داند داخل آنجا چه وضعی دارد. هیچ نقشه فنی‌ای از داخل کوه کلنگ وجود ندارد.
مجری:
درست است. همین را می‌گوییم.
لوکاس:
آژانس بین‌المللی انرژی اتمی هرگز به این محل دسترسی نداشته است. بنابراین با اطمینان نمی‌دانیم آیا سانتریفیوژها و اورانیوم با غنای بالا به کوه کلنگ منتقل شده‌اند یا نه؛ اما این محل زیر نظر است.
شنیدیم که رئیس‌جمهوری ترامپ گفت به‌زودی کوه کلنگ را هدف قرار خواهد داد. بمب‌افکن‌های B-1 را دیده‌ایم که از بریتانیا پرواز کرده‌اند و البته بمب‌افکن‌های B-2 از پایگاه هوایی وایتمن در میسوری برای همان پرواز دور دنیا که در عملیات «چکش نیمه‌شب» دیدیم، برخاستند.
مجری:
و نطنز هم هدف قرار گرفته، درست است؟
لوکاس:
نطنز هدف قرار گرفته است. فردو و اصفهان هم هدف قرار گرفتند. این‌ها سه محلی بودند که در عملیات «چکش نیمه‌شب» در یک سال قبل هدف قرار گرفتند. با این حال، کوه کلنگ تا این لحظه دست‌نخورده مانده است.
[جملاتی که در ویدیو هست ولی برای جا شدن متن در پست، اینجا نقل نکردم.]
مجری:
و حالا تا جایی که می‌دانم، این نیروگاه برق [دماوند] دو میلیون نفر را تأمین می‌کند.
لوکاس:
بله.
مجری:
و خارج از تهران قرار دارد.
لوکاس:
اگر رئیس‌جمهوری بخواهد پاسخی بدهد که تا حدی نامتناسب تلقی شود، نیروگاه دماوند را هدف قرار می‌دهد. باز هم می‌گویم، این نیروگاه ۴۰ درصد برق تهران، یعنی برق پایتخت، را تأمین می‌کند.
تنها سؤال این است که آیا می‌خواهید برق میلیون‌ها ایرانی را قطع کنید که با آرمان آمریکا همدلی دارند؟
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77439" target="_blank">📅 21:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77438">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlyCmcUaOtc_DrFnR6AaAeFbHcRFq8f4MAxBD-qB0RY_rjkWrSz2StJR36hiQPJjqQ6jCuIPBH-IuoaI7IFEsoCGNoCTZ7yX2e2ouljsXMCslZ16-H2y3GZE_FLMBNxMXjPX2p-YxsNbXJuSHFhfVXjS1oEYDwtsLVc4Kgb8mG7mOHZ546hZmMFhslkHBJRGnE5NKgcd_g1DIyGT7TLuphdtNV6REbDrqI2KOAuPcfDNPb8Nl82sXGiLOMWBSVHFKpXyPffGLz5MhwlVR_nlVJdByAt_FPW5cUgmUwMQT2P6xl72GaL27O_ejfJ-57nD5IcQDia-oSz1YQk8GEClBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش کویت عصر پنج‌شنبه اول مرداد اعلام کرد که یکی از گذرگاه‌های مرزی این کشور با عراق برای دومین بار در یک روز، هدف حمله پهپادی قرار گرفته است.
ستاد کل ارتش کویت با انتشار بیانیه‌ای در شبکه اجتماعی ایکس (توییتر) اعلام کرد: «گذرگاه مرزی العبدلی عصر امروز بار دیگر هدف حملات پهپادی دشمن قرار گرفت که خسارات مادی بر جای گذاشت، اما هیچ تلفات جانی نداشت.»
ساعاتی قبل کویت اعلام کرده بود که آتش‌سوزی ناشی از حمله صبح پنجشنبه، مهار شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77438" target="_blank">📅 21:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77437">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kGmFnLM8uENjjqdL5djNK7b8vMACjgHWu66Ell7FA0rwE65drJMGBF_UI1xkt55wbq_9dKR75K3wyRuiKPv9CILZ1-H-xxbrqHKrK2QxL8lrBlWpXjnSWHZ8sHge6px6n8AJmhXMP4mUY_Cq8yrwkT2hl4B7I3DzO2DdcHQz_w90rWvDYYE_sgCCpehv3A_F-S69GMpkRYV3lC-ImMBedZBSgF33-wpYd3GNh51aVVn3AvixgPbz87qkNhfublt2MFSh9EMOURHh1ED0hxlbEV78gIPOWuNaJHxgxj2jeXIgFL1P2yU0-4FH-tF_wD0qIEPTQaZSYOHM385Uin6mmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره
این پیام‌های دریافتی
:
خبرگزاری تسنیم، وابسته به سپاه پاسداران، گزارش داد ساعت ۱۸:۵۰ عصر پنجشنبه در پی حمله ارتش آمریکا، یک فروند موشک به نقطه‌ای در ساحل شهر سوزا در جزیره قشم اصابت کرد.
تسنیم نوشت که بررسی ابعاد حادثه و میزان خسارات احتمالی از سوی دستگاه‌های مسئول در حال انجام است.
خبرگزاری صداوسیما نیز از شنیده شدن صدای انفجار در قشم خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77437" target="_blank">📅 19:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77436">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtRBTFV0KWXHV0UNjyD-lqkyq4hnAQ9sFlW75lbF4EgbZ0jLrL7xK3lYNexkKA-sp2xGMYNarW-VkoNA-0xfjyIsruad8b-takFn2BeBjDDukgtdn9exXyz8AP1S-wAhYza57LVuWdjHceKWZtlnN0_x5JsFedF-R6HGY6OEQswhSHo8rjjBP8FaP35khtvFXDNOuq4_jQGujrIecD0jRjos9bSHAmE0bYtcHknkpTgNIqI-NmMkVLtODjEvpqsq_C9_VmK-2xJyxa-Grlgfsdi_hY7GbviU9Flb4ZbJUwEvfD6yVSsymdb7KINM5j9UEPv58rW8brvk5l01oFDzdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران روز پنج‌شنبه ادعا کرد که پایگاهی را در خاک بریتانیا که بمب‌افکن‌های ب ۱ آمریکا از آن بلند می‌شوند برای حمله «هدف مشروع» می‌داند.
وب‌سایت اکسیوس پیشتر به‌ نقل از مقام‌های دولت آمریکا نوشته بود که ارتش این کشور در دور جدید حملات به ایران، روز سه‌شنبه برای نخستین بار از یک بمب‌افکن دوربرد «ب ۱» برای حمله به اهداف متعلق به سپاه پاسداران انقلاب اسلامی استفاده کرده است.
اکسیوس نوشته بود که بمب‌افکن به‌کارگرفته‌شده در این حمله از یک پایگاه هوایی در بریتانیا به پرواز درآمده بود. اشاره این سایت خبری به پایگاه فِرفورد در جنوب غربی انگلیس است که در حال حاضر ۱۸ فروند از بمب‌افکن‌های ب ۱ آمریکا در آن نگهداری می‌شود.
حال سپاه پاسداران در پیامی این طور نوشته است:‌ «هر پایگاهی که برای حمله به خاک ایران از آن استفاده شود برای ما هدف مشروع است.»
سپاه در پیام خود ادعا کرده است که در پی ازسرگیری حملات، آمریکا ابتدا با موشک‌های کروز از روی ناوهای خود در اقیانوس هند به ایران حمله می‌کرده، اما در پی خالی شدن انبار موشک این ناوها، به استفاده از بمب‌افکن‌های خود در بریتانیا روی آورده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77436" target="_blank">📅 19:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77435">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NEDMJt_iFegT6rI47cTzYoe9-uGPE0QYxMjwngRQfc9YXcCyMtVEbM2AnJo0W8f5hRhmXoKDCeARl_6zhUl2ITgjXg7NViJ8tZ1g3sBGPrndJvnVVAuKQb3_zdX2RJObUcLy5MJx6NJrYAiql8htVehgix_C1VNQdwxEUwoPjk5CA4G9kfGF0jqmJJXzS_FEbJJ89z-WE-TWr4HhBdhdAaOcNK19islb2U08VEbIdBXO-lZWvjUI2XMshUV43JVvZLCwnQpkfMRJQimv8ZDPj10hnva-Yq9QPnNjDi2czzgL0Lwh7DdQ7RvC2XosMhzbESCjQeZNTT5OVo0eL2Flnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس: ترامپ می‌گوید به تصمیم‌گیری درباره «حمله‌ای عظیم» علیه ایران «نزدیک» شده است
ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنجشنبه به آکسیوس گفت که به‌طور جدی در حال بررسی ازسرگیری عملیات رزمی گسترده در ایران است؛ از جمله حملاتی که از عملیات «خشم حماسی» بزرگ‌تر خواهد بود.
چرا مهم است: ترامپ در مصاحبه‌ای کوتاه اذعان کرد که چنین تصمیمی پیامدهایی خواهد داشت و تأکید کرد که هنوز تصمیم نهایی را نگرفته است.
ترامپ برای تصمیم‌گیری خود مهلتی تعیین نکرد. دو مقام دیگر آمریکایی نیز تأیید کردند که هنوز هیچ تصمیمی گرفته نشده و هیچ دستور تازه‌ای به ارتش داده نشده است.
تشدید تنش‌های کنونی تاکنون باعث شده قیمت نفت از بشکه‌ای ۱۰۰ دلار فراتر برود. بازگشت به جنگی تمام‌عیار در آمریکا به‌شدت نامحبوب است.
آنچه او می‌گوید: رئیس‌جمهوری آمریکا گفت: «من در حال بررسی یک حمله عظیم هستم؛ بزرگ‌تر از هر حمله‌ای که تاکنون انجام شده است. به تصمیم‌گیری نزدیک شده‌ام. ما کاملاً برای آن آماده‌ایم.»
ترامپ گفت اسرائیل «اگر از آن‌ها بخواهم، ظرف دو دقیقه وارد عمل می‌شود»، اما افزود که برای آغاز عملیات تازه علیه ایران «به هیچ‌کس نیاز نداریم».
او همچنین گفت پیوستن اسرائیل به این حملات «پیامدهایی» خواهد داشت و تلویحاً به احتمال تلافی ایران علیه اسرائیل اشاره کرد.
تصویر کلی: ترامپ گفت ایرانی‌ها «می‌خواهند مذاکره کنند»، اما در حال حاضر آماده توافق نیستند.
او گفت: «هنوز به اندازه کافی درد نکشیده‌اند.»
دو منبع منطقه‌ای مطلع از تلاش‌های میانجی‌گرانه گفتند رهبری ایران تازه‌ترین پیشنهاد ارائه‌شده را نپذیرفته است.
یکی از آن‌ها گفت: «داریم تلاش می‌کنیم، اما ایرانی‌ها همکاری نمی‌کنند.»
محور خبر: آمریکا طی ۱۲ روز گذشته حملات خود را تشدید کرده است تا حملات ایران به کشتی‌های تجاری در تنگه هرمز را متوقف کند.
ایران تاکنون هیچ نشانه‌ای از تمایل به تغییر مسیر نشان نداده و خود نیز حملاتش در منطقه را تشدید کرده است.
شورشیان حوثی مورد حمایت ایران در یمن حمله به کشتی‌های سعودی در دریای سرخ را آغاز کرده‌اند؛ اقدامی که تنش‌ها را در یکی دیگر از مسیرهای حیاتی انتقال نفت تشدید کرده و بازار جهانی انرژی را بیش از پیش بی‌ثبات کرده است.
ترامپ در حساب خود در تروث سوشال نوشت که اگر حوثی‌ها بار دیگر به کشتی‌ها در دریای سرخ شلیک کنند، «ایالات متحده ایران را مسئول خواهد دانست».
او گفت حوثی‌ها نیروی نیابتی ایران هستند و بنابراین «مجازات نظامی سنگینی علیه ایران و البته خود حوثی‌ها اعمال خواهد شد».
آنچه باید زیر نظر داشت: ترامپ جداگانه گفت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، قصد دارد هفته آینده در مراسم وداع با سناتور فقید لیندزی گراهام در واشینگتن شرکت کند.
ترامپ گفت: «روابط با بی‌بی بسیار خوب است. اگر او اینجا باشد، با او دیدار می‌کنم.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77435" target="_blank">📅 19:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77434">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید قشم صدای انفجار
الان دریابانی سوزا رو زد وحشتناک
جزیره قشم ۱۸:۴۰
ساعت 18:40 دقیقه قشم صدای انفجار شنیدیم
وحید جان قشم صدای دو انفجار از راه دور اومد ..
🔄
صدا و سیما:
شنیده شدن صدای انفجار در سوزای قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77434" target="_blank">📅 18:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77433">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n9j6gI1JTNL3Dze92KuM0KwPG208oQSfoatIrj7v7Xlxch8cu6IHQfD9DMojnfIuGm-gQdsTEWpM1V3br6RhECyX1i20f0t7Ioj8dH9J1Wa1UFdX1hn9_PdtkikvTRpMqNzkpXzLmVjstnW91HAJ4Oxwd0gH-z59k3GKIYav34M_JlsMCfbgtbseaOnOIRbYqRGOf8zn2i4EziHSUFdLX5yVGh_Xer7pDc633js89NWo2AAKU4WxIdXMO1L-3d93x1yXlLGQu1sNOVfPp1-JYF-PvALLmfCHibhO6FmvYgU2bd-RGm_Yqa5hTt8UYjEBhtq6_thyiJ2WR48pSG-vKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف، ترجمه ماشین:
می‌خواستند ایران را تنبیه کنند.
در عوض، خودشان را با قیمت سه‌رقمی نفت تنبیه کردند.
استراتژی ۱۰ از ۱۰
👏
👏
👏
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/77433" target="_blank">📅 18:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77432">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfVHpN1auBLqfeOTYKljzz43y18eD0oxI3LHThTAOGauBW044DxABZGeqg62DD6UpWYYcwG3-qQ3BVh8BiJMLHhrCfoFFMAW37RkqyvwRYxDtlvylXuCRE5ktlw8eOoai5UwSt5jrIiawPCy7-S2YinLuLVYa5gR-Q30MKenjQhgsS2VqzT8GnJQ2AU2FuF2tfiGmlf056PKoX4APigRYkLuR2T-YTV0SmeIDZ7PtUBAwUXxwTlkX7X0XfO9QSbHaq6RI3fU-Sqq0wUm041nUr4F-LTYomrI9WSFOcw0gQWd51wT0i2unLtAkeo990sxQXGGYy4UVApbRylfLRs-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ روز پنجشنبه اول مرداد، در پیامی در شبکه اجتماعی تروث سوشال با یادآوری حملات نظامی ایالات متحده علیه حوثی‌ها که سال گذشته انجام شد، نوشت: «حوثی‌ها از آن زمان و در جریان درگیری با ایران، رفتار مسئولانه‌ای داشتند، اما متاسفانه با تیراندازی شب گذشته به دو کشتی عربستان سعودی، بار دیگر دست به حملات زده‌اند.»
ترامپ هشدار داد که اگر این اقدامات تکرار شود، آمریکا جمهوری اسلامی ایران را به عنوان حامی حوثی‌ها مسئول خواهد دانست. او تاکید کرد که در این صورت، مجازات نظامی بزرگی بر ایران و همچنین خودِ حوثی‌ها تحمیل خواهد شد؛ گروهی که به گفته او، تا پیش از این حرفه‌ای و هوشمندانه عمل کرده بودند اما اقدام اخیرشان مایه «تاسف» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77432" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77431">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osj-GIjKkzwKd0cioMIdr3NtOKLoPG3nS2v7Ah-f-gIkYT444xOuEKsimMwdFLYfNh_beopkSVo5S0aMPqDpJDsnfiPMWO3vv2n0WXLi8o33amnSQ0yhP33nudUXL9tNLyDVDi2ASylIDZloGMJZVRVGj8nizdYkzkM8tjsGY3bCGlT28-SLHQUbRdJb4McW5YC5kGN8TMy6jcwUTbkYswidKCjrKJBTYv7eFmCU9Ra4XV_UvPZ-4Uo74apKRUS3vkYonyO98viXAtxW9Tm1pWvBHkLoMN-j05wWQXsrvJcaUmQ-rIDgoB7wTSo_DWfq0pYjlsFtZKkvfe1hxtHILQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد امیرحسن اکبری‌منفرد، زندانی سیاسی ۲۷ ساله محبوس در زندان اوین، با حکم شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، از بابت اتهام «بغی» از طریق عضویت در سازمان مجاهدین خلق ایران به اعدام محکوم شده است. بر اساس این گزارش، حکم دو روز پیش به او ابلاغ شده است.
هرانا همچنین گزارش داد امیرحسن اکبری‌منفرد زمستان ۱۴۰۳ همراه با پدر، برادر و خواهرش در کرج بازداشت شده بود و سه عضو دیگر خانواده بعدا با تودیع وثیقه آزاد شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77431" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77429">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SmC6i7z1ULu0asfG_Dvj4bf-M41kf8LqkFxCNrT2qWFxcHg6pidbCU3ZFy5LDMCTEF0vj6a_lu0nH2xTZrq5-zN_PeBWD8s6ywK4Grxnldsbjce9OtX7l2VvDXNJjYZJHjBqPD32U7V-q1ez7Vn82JdRhi6a5e_gAwjEa1ihMfNedYKxWDjh79ETDxXIxjZBP2peCl2kYebPlo6swz17e1bVcr5bZgvwsAiKuZ5OkkjZzhrcKZjLnfaFkhD0dbr_aB7MLdQjhlxNaO2wSJDxzhIPNbUPDBcFoFcA-4v61C1Gq4BtLRCuuA3ORgqRG1uYrBXTAhsCdeFj-TMNV0zWZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dvD3_BkQpba5mGogSQzZ1a0oraVeM0OPCE8yZk24gaVTAtwqJuGwcsLF9k__14fXmOuo_E6SQJh1csP19ThmvJuofAv8hmPhe-_tQJxCLZ9lNdkDDQoU_1leq_e62dS-D7mm4qXPqpOAPJlB9BDyPcw_jqYh9GTrRhLTjisPux3RehGeWZyDIhnYVdCwVmGoeD16P5tBaG0DQC0ngb2Qmxdm4tMiP6KxZVMo6cmijrCw77rmpbkPO57CU5_JT8vUM-EopI1jPLFGkn_YGMiM15yKSnf7MErNJvVDayrMaP8oUhZkVDOndtPxGwRB5hFGxACVNTB84j8odr65mvrJzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه اول مرداد ماه، در پیامی در شبکه اجتماعی ایکس اعلام کرد توافق هسته‌ای غیرنظامی میان وزارت انرژی آمریکا و عربستان سعودی تصویب خواهد شد، اما این توافق مشروط به پیوستن ریاض به توافق‌های ابراهیم است.
ترامپ در این پیام با اشاره ناگهانی به «غیرنظامی» بودن برنامه هسته‌ای ایران نوشت: «توافق هسته‌ای غیرنظامی که میان وزارت انرژی ایالات متحده و عربستان سعودی در حال انجام است، تنها به استفاده‌های غیرنظامی، مانند برنامه‌هایی که ایران، امارات متحده عربی و دیگر کشورها دارند، مربوط می‌شود. اما این توافق کاملا مشروط به پیوستن عربستان سعودی به توافق‌های ابراهیم است.»
رئیس جمهوری آمریکا کرد در این توافق «هیچ غنی‌سازی مواد [هسته‌ای] وجود نخواهد داشت» و آمریکا با تاسیسات هسته‌ای غیرنظامی و بدون غنی‌سازی مخالف نیست
@
VahidOOnLine
دفتر بنیامین نتانیاهو، نخست‌وزیر اسرائیل پنج‌شنبه اعلام کرد پیوستن عربستان سعودی به توافق‌های ابراهیم، تحولی تاریخی در مسیر صلح در خاورمیانه خواهد بود.
دفتر نخست‌وزیر اسرائیل افزود اقدام نظامی مشترک آمریکا و اسرائیل علیه جمهوری اسلامی و تضعیف محور «تروریستی» تهران، زمینه را برای گسترش دایره صلح فراهم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/77429" target="_blank">📅 17:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77428">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAAT_LwkkxM1B5q7Gl6yZt8XZPk130UvAhzlk1A3rPcSxYAZDiwR1r2baBrwtPOyY3THVAl-163SPSdUC1Vn8qsl6y5IrPGwmC6p1zVOS54Bj3GkpHMq4OPmqPDGAc0VcHZbykyzwUCHdhukpKCh8PkWm0ilaJgVw-kwyJ1IsalIccrUJzTwOsxl66CQzt6Ju4jkz900qYk72f_AnGbdx_QNvzYEwW-N2bpvEZdOxrTBjyfHhCHpXdpkZGX36DgKWK2jW31OpYvYegYLnxnUVSEVPVqo6_QU2ka8wOiqSo07x_00vnrCuKUYytXa7Co3Abr1x17l9qoUlZZR_KjJrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایلنا در گزارشی از ادامهٔ بحران کم‌آبی در زاهدان و برخی مناطق استان سیستان و بلوچستان خبر داده و نوشته است که شماری از شهروندان در برخی محله‌های این شهر با قطع آب تا سه یا چهار روز متوالی روبه‌رو هستند.
بر اساس این گزارش که روز پنج‌شنبه یکم مرداد منتشر شد، بسیاری از خانواده‌ها برای تأمین آب ناچار به خرید آب از تانکرهای خصوصی هستند و برای هر بار پر کردن مخزن خانه بین یک تا یک‌ونیم میلیون تومان پرداخت می‌کنند.
ایلنا همچنین به نقل از شهروندان گزارش داده است که برخی خانواده‌ها به دلیل ناتوانی در پرداخت هزینهٔ خرید آب از تانکرهای خصوصی، ناچارند چند روز را تنها با چند دبه آب سپری کنند.
محمدرضا کوچک‌زایی، عضو شورای اسلامی شهر زاهدان، نیز در گفت‌وگو با ایلنا با تأیید بحران کم‌آبی گفته است این شهر با کمبود حدود هزار لیتر آب در ثانیه، معادل نزدیک به یک‌سوم نیاز آبی خود، روبه‌رو است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77428" target="_blank">📅 17:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77427">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSUC6aDG-i1Xb16B4k_o5PKNFXg6hii6Qp3poMn7Q_RQ1aHJnNQEt6eJ2VYFd90HK7GXBqgEHJXtSg8J88uofiuShvLj5UYPRMjDUCa29nCu2wNnCAIkS8LlrgrhWZHP1HQKOArikebHPpPMFZyD8GINaHkb6_a4EGQZls8MfzI01WbAxZQKnUCsF866WtcyX3yuw8nfvv_VqPGPbqiIk3lBbOS895JKDtc9tCG-4CX9P2T92i806gi6nl_bV_xK0XIBdT6_9CwAVD-b1tUY4bZoASTRkJOlu3hHiMkOiPxklosz6SIBJlqp9xS_R1LQxTwlr5GdqWl6RDPkH31Mfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما و خبرگزاری تسنیم، روز پنجشنبه یکم مرداد ماه از شنیده شدن صدای چند انفجار در شهرستان کنارک در استان سیستان و بلوچستان خبر داده‌اند.
خبرنگار صدا و سیما در گزارش زنده اعلام کرد، صدای پرواز جنگنده‌ها نیز در این منطقه شنیده شده است. به گفته این منبع خبری،َ انفجارهای روز پنجشنبه، اولین حملات آمریکا در طی ۲۴ ساعت گذشته به این شهرستان بوده است.
@
VahidOOnLine
من هم حدود ساعت ۱۰ صبح پیام‌ها و عکس‌های مختلفی درباره کنارک دریافت کرده بودم + کلی پیام از چند شهر دیگر درباره پرتاب موشک
پیام‌های زیادی هم از دزفول و اندیمشک داشتم که در اون مورد پیش‌تر اعلام شده بود قراره  مهماتی کنترل‌شده منفجر بشن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/77427" target="_blank">📅 17:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77426">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAg7-xDit7xwDVCiqnoEm9l9JAKIkLWd11GEezvC2OQrNBDUp6AAJBZH1j36HcnUyxi56safr9lMy_NHgEjuJ3mDpSrP9uwVj225edntw6U8oHbz-GEv4YOb32Nwa6ZCCeMUueTn5inUPt3Qxly8gc03EeepOfkGXPjLAoSbcFlHHNOuHL4LBBsBELE8-bRQdMdIQE10bZ0jHc6_IAsQhV0bfixradfAQ_K71g6URp2BUqvx7EIFc-q7scDkI4goZK-p8DgQFclsPuGbeTjg2yvyjoyrfWDRwSGhtXqjh2z_aaw7CD9g4pmADRImhz7cffQNVmTKyFVjsDJUnWcgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماری
از داوطلبان آزمون کارشناسی ارشد در شهرستان‌های بستک و بندر خمیر استان هرمزگان به‌دلیل تخریب پل‌ها و بسته شدن مسیرهای ارتباطی پس از حملات آمریکا، از حضور در جلسه آزمون بازمانده‌اند. به گفته آن‌ها، با وجود اطلاع مسئولان از وضعیت منطقه، هیچ راهکار جایگزینی برای برگزاری آزمون یا انتقال داوطلبان ارائه نشد.
کانال تلگرامی «
دانشجویان متحد
» خبر داده است که شامگاه ۲۶ تیرماه ۱۴۰۵ و هم‌‌زمان‌‌‌ با برگزاری آزمون کارشناسی ارشد، پل‌های محور بستک–بندر خمیر–بندرعباس در حملات پهپادی سنتکام هدف قرار گرفت و مسیر ارتباطی این دو شهرستان با بندرعباس به‌طور کامل مسدود شد.
در حالی که حوزه امتحانی داوطلبان این مناطق در بندرعباس تعیین شده بود، بسته شدن جاده‌ها باعث شد هیچ‌یک از آن‌ها نتوانند خود را به محل برگزاری آزمون برسانند.
به گفته این داوطلبان، آن‌ها تا آخرین ساعات پیش از آزمون بارها با اداره راهداری و دیگر نهادهای مسئول تماس گرفتند، اما هیچ راه‌حلی برای انتقال یا تغییر حوزه امتحانی در نظر گرفته نشد.
این دانشجویان می‌گویند ماه‌ها برای شرکت در آزمون آماده شده بودند، اما در نهایت به‌دلیل شرایط جنگی و نبود تدبیر مسئولان، فرصت حضور در کنکور را از دست دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77426" target="_blank">📅 17:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77425">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDfLtZWrKrgXmBSTS9x7TvRlyJI7BXPTDjY-3T3E9kJhuYZfhzzokdbEL_66TknI3Mczw8Yf35Zs4dDr9Y_v1YI3LKrhFSEpZrCrxsJYXSXN2VRHeSmDNssMl0i85JRAqDEVCY1pz18g9_YeViVWFn95wCct7TtCnMy24m9bPZ1VcRRlmTUvIcOegEvabXqx10pTGrXEjmbSbcVe9bCTmuNoWTQZ97KZ0V1elb80luuRftmc_Lob-zfMO6HHGWK0L2SDMUOWTm8jyKyTrrm6Up4qGOEe6bBJjZqDtZwNClrtpQkS62MyXv4OrWrN7g3noP3GD-De7OseA7ypq73kMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه آمریکا، در حاشیهٔ نشست آسه‌آن در مانیل، با تکرار اظهارات پیشین خود مبنی بر «آماده نبودن ایران برای توافق» گفت: «آن‌ها هزینهٔ این موضوع را خواهند پرداخت.»
مارکو روبیو روز پنج‌شنبه یکم مرداد گفت «هزینهٔ ایران هر شب بیشتر می‌شود تا زمانی که به خود بیایند» و افزود: «با وجود جسارت ایران، آن‌ها به‌شدت در عذاب‌اند و این رنج همچنان ادامه خواهد یافت.»
وزیر خارجه آمریکا در عین حال ابراز امیدواری کرد که حکومت ایران «احتمالاً به‌زودی» آمادهٔ توافق شود، اما تأکید کرد در حال حاضر به‌وضوح آمادهٔ توافق نیستند، «حداقل نه توافقی که حاضر باشند با آن کنار بیایند».
روبیو در پاسخ به سؤالی دربارهٔ اظهارات اخیر دونالد ترامپ دربارهٔ پرداخت هزینه از سوی ایران در ازای کشته شدن سربازان آمریکایی و حمله به کشتی‌ها در تنگهٔ هرمز نیز گفت سیاست ترامپ «سر در برابر چشم است و ایران هزینهٔ سنگینی خواهد پرداخت.»
وزیر خارجهٔ آمریکا همچنین با ابراز امیدواری نسبت به توقف حملات حوثی‌های یمن گفت: «امیدوارم آن‌ها تنش‌زدایی کنند، ایران آن‌ها را فریب داده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/77425" target="_blank">📅 17:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77424">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZnNNTT6JyGfo8s4cWhBNm5uYDDGfw2nPqX5K3MsUwEdVaUnsNa0nKtZTkAu_9_NdvHm36bIZpYdb48K0_hWJe-yYl6jDmIDPHNLp0Q-vDCXPYJhvW2DNuaDgEuE1P8aflJsuY5AG1LiwwnO1PeJrDKHUWZWGdk2I_iJwDhAtYsoPse_tz6EL7zuHeQ_xjMG5AVAvT9ET9tL0uAn2W0pqP2cW9lQTddYN61K04blHsXnnaOjI0lKVn-jQwtGVcn-8_gS5RccTsRbun6lXS72gzY2k6pq8GothZ5Fc7zweWWmvrEViOu9s89azXUjFPSomZ_XORXB5aCGlgsxcp2HsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگاه قضایی جمهوری اسلامی برای دو نفر از بازداشت‌شدگان اعتراضات سراسری دی‌ماه ۱۴۰۴ احکام سنگینی صادر کرد؛ مهنام نواب‌صفوی به اعدام محکوم و حکم ۱۰ سال زندان علی صانعی نیز در دادگاه تجدیدنظر تایید شده است.
مهنام نواب‌صفوی، محبوس در زندان دستگرد اصفهان، از سوی شعبه پنجم دادگاه انقلاب اصفهان به ریاست قاضی همتی‌نژاد با اتهام «محاربه» به اعدام محکوم شده است.
در پرونده او اتهام‌هایی از جمله «محاربه از طریق مشارکت در تخریب اموال عمومی»، «تبلیغ علیه نظام»، «اجتماع و تبانی علیه امنیت کشور» و «تشویق مردم به کشتار یکدیگر» مطرح شده است.
هم‌زمان، حکم ۱۰ سال حبس علی صانعی، دانشجوی ۲۲ ساله رشته کامپیوتر، در دادگاه تجدیدنظر تایید شد.
صانعی اسفندماه ۱۴۰۴ در ملارد بازداشت و به زندان تهران بزرگ منتقل شد. شعبه ۲۸ دادگاه انقلاب تهران به ریاست قاضی عموزاد او را با اتهام‌هایی از جمله «توهین به رهبری»، «اجتماع و تبانی علیه امنیت کشور»، «تبلیغ علیه نظام» و «همکاری با اسرائیل» به ۱۰ سال حبس محکوم کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77424" target="_blank">📅 17:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77423">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ciyOE8ROpSAEj4XODHnlu_p2QPx80wh1v5FU3QeZJvBGGyY-Uy6YIQbEw3bFQCNPimTWD5Kn5dofjhUB9HF6Kc0R1HbkQ50osuttI7E3Uq6aRAG36sDBAShzLQEqJLt9KrWbtvsGi41Pz_on_9l0KaszbuJB0frTqHFeqUfoYBn8h8HBAl7yfjQQF6LxakRZ8SaEMHU0YsrTmhFJm7_DasnNasa9SJkuTa_81fst253ZdGA000X7F7Wz-EJ8493znxGuvibESMJjuBDospLi7XMln0nY6Szid-vJdIJsTDkRZ1ZYkJ32V0UUqgPhXrYNX2RoVGcDCyHZ8wGQE_cfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس: آمریکا هم‌زمان با تشدید حملات به ایران، بمب‌افکن B-1 را به‌کار گرفت
ترجمه ماشین:
مقام‌های آمریکایی گفتند ارتش ایالات متحده روز سه‌شنبه برای حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران از یک بمب‌افکن دوربرد B-1 استفاده کرد.
چرا مهم است: این نخستین بار از زمان ازسرگیری درگیری‌ها با ایران در ۱۲ روز پیش بود که آمریکا مأموریتی با بمب‌افکن B-1 انجام داد.
استفاده از بمب‌افکن‌های B-1 که می‌توانند ۲۴ بمب ۲٬۰۰۰ پوندی یا ده‌ها موشک کروز حمل کنند، نشان‌دهنده تشدید و گسترش قابل‌توجه کارزار نظامی آمریکا بود.
‏B-1 می‌تواند در ارتفاع پایین با سرعتی بیشتر از سرعت صوت پرواز کند و در میان همه انواع بمب‌افکن‌ها، بیشترین محموله بمب را حمل کند.
هم‌زمان با ادامه افزایش حضور نظامی آمریکا در منطقه، رئیس‌جمهور ترامپ همچنان در حال بررسی بازگشت به عملیات رزمی گسترده علیه ایران است. مقام‌های آمریکایی و اسرائیلی می‌گویند این اتفاق ممکن است ظرف چند روز رخ دهد.
اصل خبر: بمب‌افکن B-1 مأموریت خود را از یک پایگاه هوایی در بریتانیا آغاز کرد و در وب‌سایت‌های آنلاین رهگیری هواپیما مشاهده شد.
فرماندهی مرکزی ایالات متحده (سنتکام) در بیانیه روز سه‌شنبه خود درباره حملات آن روز، به مأموریت B-1 اشاره نکرد.
در این بیانیه آمده بود: «دارایی‌های سنتکام مراکز عملیات نظامی ایران، توانمندی‌های دریایی، آشیانه‌های هواپیما، تأسیسات نگهداری پهپاد و زیرساخت‌های لجستیکی نظامی را هدف قرار دادند تا توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز بیش از پیش تضعیف شود.»
مشخص نیست B-1 چه هدفی را مورد حمله قرار داده و آیا این مأموریت عظیم از دیگر حملات چند روز گذشته مؤثرتر بوده است یا نه.
آمریکا در جریان عملیات «خشم حماسی» چندین مأموریت با B-1 انجام داد و پایگاه‌های موشکی، مراکز فرماندهی، تأسیسات نگهداری سلاح و سامانه‌های پدافند هوایی را هدف قرار داد.
وضعیت کنونی: با وجود گسترش حملات آمریکا، به نظر نمی‌رسد حکومت ایران موضع خود درباره تنگه هرمز را تغییر داده باشد. ایران همچنان به حملات علیه پایگاه‌های آمریکا در منطقه ادامه می‌دهد.
برخی مقام‌های دفاعی آمریکا می‌گویند توانایی نظامی ایران در اطراف تنگه هرمز «تقریباً از بین رفته است»، اما برخی دیگر می‌گویند ایران همچنان قادر به حمله به کشتی‌ها در این منطقه است.
رئیس‌جمهور ترامپ روز چهارشنبه تهدید کرد که اگر ایران به حملات بیشتر علیه کشتی‌ها در تنگه هرمز دست بزند، پل‌ها و نیروگاه‌ها، از جمله تأسیساتی در تهران، را بمباران خواهد کرد. ایران نیز در پاسخ، زیرساخت‌های کشورهای حاشیه خلیج فارس متحد آمریکا را تهدید کرد.
نمای گسترده‌تر: همچنین روز چهارشنبه، شورشیان حوثی برای نخستین بار از زمان اعلام محاصره بنادر عربستان سعودی، به کشتی‌های سعودی حمله کردند.
یک مقام دفاعی آمریکا گفت حملات حوثی‌ها، پس از چند ماه که تقریباً به‌طور کامل از جنگ دور مانده بودند، ممکن است با تحریک ایران انجام شده باشد.
این مقام گفت ایران می‌خواهد با استفاده از حوثی‌ها، علاوه بر خلیج فارس جبهه جدیدی در دریای سرخ ایجاد کند و بر یکی دیگر از مسیرهای حیاتی بین‌المللی حمل‌ونقل نفت فشار وارد کند.
روز چهارشنبه چندین کشتی تجاری در حال عبور از دریای سرخ دیده شدند که از بیم حملات حوثی‌ها، مسیر خود را تغییر دادند تا از تنگه باب‌المندب عبور نکنند.
آنچه باید زیر نظر داشت: مقام‌های آمریکایی گفتند میانجی‌های قطری همچنان با مقام‌های آمریکایی، ایرانی و عمانی گفت‌وگو می‌کنند تا به توافق جدیدی برای بازگشایی تنگه هرمز و توقف درگیری‌ها دست یابند؛ این موضوع را منابع مطلع اعلام کردند.
یک منبع منطقه‌ای گفت رهبری ایران تازه‌ترین پیشنهاد ارائه‌شده از سوی میانجی‌ها را نپذیرفته است.
مشخص نیست ترامپ چه مدت به تلاش‌های دیپلماتیک فرصت خواهد داد. ترامپ چهارشنبه‌شب در سخنرانی‌ای در جورجیا گفت: «آن‌ها به‌شدت زیر ضربه هستند و می‌خواهند توافق کنند.»
«اما من می‌گویم آن‌ها آماده توافق نیستند، چون هر بار توافق می‌کنند می‌خواهند آن را عوض کنند و همه‌چیز را تغییر دهند. آن‌ها آماده نیستند. خیلی زود آماده خواهند شد.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/77423" target="_blank">📅 07:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77422">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sgyuUWLyI75-7B3YTHbQCvR4386n8T7ivEx5JEmNIhgseAQVOaEPzjJof5Dbco3j1DnqL8-caZbW7BuDpDvv0g1h_tbfUXP7x4UvjN-XhHPR4YLPrj1euu-CF78wL5hOArSfK4ta-TlINYAaL--2fQDdkv8hinsD5iET71G_W4PxRWetXMQzNmVhIS2YR7gFxc9gy5Y7bgjLyg2sg-KHeueyG6CVOWbVJVX-nczg-OuNZhGl9otmWq6opk_0G7s7vBQxtHKZVQzQoSLvSr-83OEzkKcepuTKJQgU-T-VozxtZxaUo7m8pI-Pnnhn_Xh1Bm1cN_rOrEjI2Cx5FfNx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عربستان (واس) تایید کرد که کشتی «انسیلیا» متعلق به یکی از شرکت‌های سعودی در دریای سرخ هدف قرار گرفته است.
به گزارش واس، در پی این حمله، آتش‌سوزی در بخش جلویی کشتی رخ داد، اما همه اعضای خدمه سالم هستند.
یک منبع در سازمان حمل‌ونقل عربستان نیز اعلام کرد نهادهای مسئول اقدامات لازم را برای تامین امنیت کشتی «انسیلیا» انجام داده‌اند.
پیش از این، حوثی‌های مورد حمایت جمهوری اسلامی اعلام کرده بودند که دو نفتکش عربستان سعودی را هدف قرار داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/77422" target="_blank">📅 07:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77421">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/111a8149da.mp4?token=I3UGsL4W-5hgp4ymd8z-8sY6QRuIpqO83_qFuprFJyDFFgSafAn77y8tVzUwFVlRJj2y8GZX6TPGL6WJI2RmU4UZdcJM6Sd5mOwipFOl0LzrDcI1Kko0wbFqNNSn3wq0fvb-3PtEFFAyetDjCZci4rxip3_fspgMa0an82kiJhBxYJRGJqa6bbgdEPwjI4qrER465b_QLL8TyOS0Z80irGXw74lWpW0meg5oYjV8xrn8xR1B6rtxrdlCqVgWbktz4CHTadFFl-fYQD_xn8gZ_Hy1cP6eGTJ3PfBtStzQRm_BZdp16a9irm7smxJE4LZBtUfXXUu63VwLJg6Grr6SgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/111a8149da.mp4?token=I3UGsL4W-5hgp4ymd8z-8sY6QRuIpqO83_qFuprFJyDFFgSafAn77y8tVzUwFVlRJj2y8GZX6TPGL6WJI2RmU4UZdcJM6Sd5mOwipFOl0LzrDcI1Kko0wbFqNNSn3wq0fvb-3PtEFFAyetDjCZci4rxip3_fspgMa0an82kiJhBxYJRGJqa6bbgdEPwjI4qrER465b_QLL8TyOS0Z80irGXw74lWpW0meg5oYjV8xrn8xR1B6rtxrdlCqVgWbktz4CHTadFFl-fYQD_xn8gZ_Hy1cP6eGTJ3PfBtStzQRm_BZdp16a9irm7smxJE4LZBtUfXXUu63VwLJg6Grr6SgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
سنتکام تازه‌ترین حملات علیه ایران را به پایان رساند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۱۰:۳۰ شب به وقت شرق آمریکا [۶ صبح به وقت تهران] در ۲۲ ژوئیه، برای دوازدهمین شب پیاپی، دور دیگری از حملات علیه ایران را به پایان رساندند.
نیروهای آمریکایی اهداف نظامی ایران، از جمله توانمندی‌های دریایی، تأسیسات نگهداری موشک و پهپاد، مراکز نظارت ساحلی و تجهیزات پدافند هوایی را هدف قرار دادند. این حملات توانایی ایران برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری را بیش از پیش تضعیف می‌کند.
در ماه جاری، نیروهای آمریکایی ده‌ها مرکز نظامی ایران در خشکی را هدف قرار داده‌اند و هم‌زمان محاصره دریایی علیه ایران را از سر گرفته‌اند. تا امروز، سنتکام برای جلوگیری از ورود کشتی‌ها به بنادر ایران یا خروج آن‌ها از این بنادر، مسیر ۹ کشتی تجاری را تغییر داده و یک کشتی را از کار انداخته است.
بیش از ۵۰ هزار نیروی نظامی آمریکا در سراسر خاورمیانه در حال فعالیت هستند و همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77421" target="_blank">📅 06:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77420">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OpGPQbDetYRm0BEq1qtl8sr1jjT6GLhdVbFbqmc2ccoSEKVlX2xLS3QzQxhQhI6tkSR240QZHULYtMZr4X7gGLzeNNXXFLb4mklGa9crV46JTLt69bnJrTXkgdgxRl6xL5NiZ9HjNbwvZd8hg68GUyMnbl3iSL5xEYY2nCL_ZA2h303I8sDQpvsEUNT7j_jK4Cj2LXhKGIFloxovElIhC2xP2Des5aik3YMkn3fEg3tFw22bVK1j2P9DvpSmP9WgGDIMWbaD85ZkaAJ3NNUE6rQ5LE4b_xVwbmeNpSGEniJcJv8wy6XjogdPGZiXdi3OlE2gRyyHlwwRgxxwa9LFQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه پیام دریافتی از ساعت ۵:۱۳:
دوتا انفجار سنگین پایگاه دریایی ارتش جاسک
جاسک ۲ بار زد
جاسک چند دقیقه پیش دوبار زدن . سلام
🔄
دوباره زدن
صدایی شبیه به جنگنده هم میاد
یک صدای وحشتناک انفجار جاسک 5:30
همین ۱ دیقه پیش دوباره جاسک زدن، نمیدونم دقیقا کجا ولی صدای خیلی شدیدی داشت
باز انفجار مهیب در بندرجاسک ۵:۳۱
جنگنده بالای سر شهر در حال چرخیدنه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77420" target="_blank">📅 05:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77416">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BLhXu24PtYGPtZ4W2_NVhMzoELAfhPcD7rqwyKmD2Goh_NVuQlqV1H8YqVvU_J5frqOt6U7tyXSfO-d2p39P-OFHAv-hI2qj-vV9y_o5Y-RPCDOLetc1TQHbWGthq7jiyf6BIT6px_0Z9iedW9I-8e2zvsxXbZgW3FKuKi2rp7XQ_8VRt8EVcHCP23IjISEPPUzV2Ylir7u1vxm14C71vKK4IjfuJerVz1WGTIB7ekoTXT63z7Q_s6SSFU2uaosO3D_iwaVffQBMo1vuxJLGfQZBnCn-ml-JRfkekPMT_VRXqdC76kwvkxrGSGaa4WFGO559kzlvC7aAPWz35KZBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FBRmBDnrLXHaosCGRMxqvPmDlW1oKh6sEmMzlXWPss10JbKrk7LUiWqR4NjXoqAMj2RnViPq5WPiRH-l3tB1WrjLrLAxcvuDGK7F6VYuccG_z-fKAZRAFZzR5lIxnWGB3HpmjaYC8LbUFHH5o4Q1NRz-lSkpkdZW7i0Z5Jai8w0AiRtOTTbqn8zjTHIGE-39GOr3h7Kt_hL77D0BMhxU_X6ryhbveLjdz8N3oKwZcQRJhB72YY7sdgCZHlysnbAC9sEP5Gv7iAvisZW_HZoPfAg4hJSIYAB6NvWFMztdxApup-QiA5RM6ktJumkmlzY-pY-mSzi2PD7_afLM_DLtIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/reMnsgmhLjnNGifB_1t0m52GofZPwqsSRqYxft2LJWjoQSgh23p5zbTZzhtj7Od3j1bYQiJynXEP4yedw-RMpoo1t-6lNjg8iQqnJW-TJ2gblwpIrk2My33OANlHrwpliW1xz6GwlH_uE8i5PxYUv7IwtEsu3-Q5OmZAhGA00gl6doeLKTw09UH_pGHx7EK2ESDpF1-S9KS-4MYxn3W-JNZTpQSTXvHaw1L3SvOAoR0FEvGSalFbhPeKbdpvbcwsN9x-bI847H1fz_Fcnwkbp_UoQ26ndvNhj45bOKYf66LRhi10rrfDU5R8tR0Y99SyNv6zMJCKl47SY26N-FFb-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Aq8e1Z2JNDQqbtPoi23IsF1wqNJI8T4HUvWaV58RFd9KtorhPuaJLjnVt28NyjfPE2BREgqSWD8oANZqVqKli2bL2DuRgj7AiUGfH36VK4gyx01QZvNoLnLzY0LKCK6LiSvuJ8BUlpMHKXIwDmxj3QMU0X9U9f6jUjUhQwS_JwEiMva0xngF_gHbJeUaEy2tSu1DXHYiuxVZsQjiTdU6CrJfTm1cMCMUeag6EdTNUmb2aI8Terx19pJcRkIk9NQ5ocJ5FBjBM_ldtTOOky3Z8ufii5Hu4-DiTZi8O__u3Kj4EN8PzIJkGmM6CC3yuctN4Xiawu28VjY_F7Px0FDoXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر پخش شده با شرح: انفجارهای حمله به  اسلام‌آباد غرب در استان کرمانشاه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77416" target="_blank">📅 04:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77415">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCIiPHEPDp7XGvZKz2cMCPUHfKFvntLcvkMXMFknSORbD0dbtAcNQe3HpHG0PNuWz3rxooSl3DY00HNnGaun_HUzV4Qph2cvhw0qY3UZoIvxn18DeHZ7GvbxI0E2yztVUc_Ahl_JkoWLdUhanIuSX87KyBRm1rbsdFJuIpfvZyoGJ4vhOzxMZZxTdALz9GbVTpsdhsgggmm5dmb-4--7pdECz54725-XoxellHl-b3KErF-9OAzOGzqyUGi7M4Duu4tYtphZp0mQFhlw01KztEVPl7Px0C0bPvRSHTMBmpOEoqHYGsgukd9ZxciBLEQoanndyMhTLdIM_JcR9Zpg2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش تسنیم، معاون استاندار خوزستان اعلام کرد یک نقطه در اطراف شهر اندیمشک هدف حمله موشکی قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77415" target="_blank">📅 04:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77414">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9aaff68657.mp4?token=afECZNYYjamYHXKw7EK5avGXPzQZhHIpTnzOf7D1MenyxrxKioro40f6wzBYaqcfLv5A_b1W3pjhR12Fse_7amVO6OJTy_ULsc3xvnbviU_dYLv7x-DBvBXh8CK8zN_OMAKFxBJOjAaWtzfuI56wTLhQvlLn1bq-wyjEbTg-uUg03bNDlAtPNLSvUp6e8JFswtZKHxIsmGbuudM3CM7Q4qmEbaTOZG2tFW3ESQ9teBGchte3CDqgEGdBwDn6r3UH6DrcW85Kx3wVtLehu5zoxaI1pbbkj6D6yup0fFKNTU7Rv7qQpufUtab2cu68tgjc3Mgfnomu11nNOrK4Kib16Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9aaff68657.mp4?token=afECZNYYjamYHXKw7EK5avGXPzQZhHIpTnzOf7D1MenyxrxKioro40f6wzBYaqcfLv5A_b1W3pjhR12Fse_7amVO6OJTy_ULsc3xvnbviU_dYLv7x-DBvBXh8CK8zN_OMAKFxBJOjAaWtzfuI56wTLhQvlLn1bq-wyjEbTg-uUg03bNDlAtPNLSvUp6e8JFswtZKHxIsmGbuudM3CM7Q4qmEbaTOZG2tFW3ESQ9teBGchte3CDqgEGdBwDn6r3UH6DrcW85Kx3wVtLehu5zoxaI1pbbkj6D6yup0fFKNTU7Rv7qQpufUtab2cu68tgjc3Mgfnomu11nNOrK4Kib16Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
وحید بوشهر زدن بدددد
بوشهر انفجار خیلی شدید
😐
دستم میلرزه بزرگترین انفجار
سلام وحید همین الان انفجار خیلی شدیدی بوشهر از قبلیا خیلی بدتر بود
وحید بوشهر زد ساعت ۳:۵۹
بوشهر چند انفجار وحشتناک همزمان ساعت ۰۴:۰۰
بوشهر زدن ساعت ۳:۵۹
سلام وحید الان بوشهر رو زدن و خونه لرزید یه صدا خیلی زیاد هم اومد
انفجار سنگین شهر بوشهر ۴:۰۰
سلام وحید جان
ساعت 3:59 بوشهر رو زدن صداش متوسط بود
بوشهر صداش خیلیی بلند بود
همین الان وحشتناک بوشهر زد
همین الان بوشهر زدن ۴:۵۸
وحید جان بوشهر پایگاه هوایی باز زد الان
درود، همین الان
3:59
بوشهر رو زدن صدای مهیبی داشت
وحید جان بوشهر
همین الان زدن دقیق ۳ و ۵۹
یک انفجار نسبتاً شدید ساعت ۳:۵۹
۰۳:۵۹ بوشهر صدای انفجار خیلی شدید و خیلی نزدیک اومد
سلام بوشهر رو الان زد
همین الان یک دقیقه پیش انفجار وحشتناک بوشهر خونه لرزید
از بوشهر همین الان یه صدای خیلی بلند انفجار دقیقا نمی‌دونم چی بود اما خیلی بلند بود همه از خواب پریدیم
ساعت ۴ صبح انفجار مهیب در بوشهر
چندین انفجار بوشهر
یکیش خیلی بلند بود و لرزش داشت
داش بوشهر بغل خونمون انگار بمب اتم زدن
بوشهر صدای وحشتناک انفجار، گمانم پایگاه هوایی بود... ساعت ۴ صبح
همین الان خیلی شدید
از خواب بیدار شدیم
بوشهر
صدای انفجار خیلی شدید از پایگاه هوایی بوشهر
سلام همین الان بوشهررر صدای بدی اومد که همه بیدار شدن
تک انفجار ساعت ۴ ولی جوندار زدن
آپدیت:
پیام‌های ساعت ۴:۴۱:
صدای پدافند بوشهر
وحید بوشهر انفجار
ضدهوایی هم کار می‌کنه
بوشهر پایگاه هوایی صدای پدافند
بوشهر ۴و ۴۰ پدافند پشت سرهم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77414" target="_blank">📅 03:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77413">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">استان کرمانشاه
فقط سه پیام دریافتی در ده دقیقه:
انفجار کرمانشاه ۳:۳۶
اسلام آباد کرمانشاه رو زدن
سلام ۵دقیقه پیش اسلام آبادغرب در کرمانشاه را زد ۲تاانفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77413" target="_blank">📅 03:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77412">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppkocPz2Q104_OjTOXUrY42SfXxqa92EeWJjnWROcUc5gZjZMpeO_0hCIKuKvKhlVCBow2iTnIY_XOSORzQ1-q-1355xDoK1actshiFb3RGvUMd3qCxDF2gJxQHks7chFRjwPB5ngh7wR2AjzxoLpTKVd02RXBBy5IYCBVSh7xVUrAZylYdJt4iuRIOgOhGmfIurAes44F53P8SI_CUrA-j-uwG8fQaF0zACCX8uP9Qlbo7jgY_lZNTPQURQMHgP2mi04fHFaIATXn1UQHxVu1UqfV62Zyn0ZfQ1EbWTbgt7URhRTxrkhEQqRLT29jf_RsfHef5NWUosArQLjg9x2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران صبح پنجشنبه در اطلاعیه‌ای گفت که سه کشتی قصد عبور از تنگه هرمز را داشتند که یکی از آنها آتش گرفت. سپاه دلیل آتش گرفتن این کشتی را برخورد با مین عنوان کرده است.
سپاه در این بیانیه تاکید کرده که کنترل تنگه هرمز را در اختیار دارد و هیچ کشتی از این تنگه عبور نمی‌کند. در عین حال ارتش آمریکا می‌گوید تنگه هرمز باز است و هفته‌های اخیر ۹۰۰ کشتی از آن عبور کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77412" target="_blank">📅 03:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77411">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/733c9968e4.mp4?token=Nr0sN44WU0LFb13P-_byB-dXDo4Tu8g7C4cba7D9yCuBbhoHo5Gys1Knx-S8ni8JLYv3qfrgX6gPnfsQTLKA5N6048Hd_5rDuZCEjT8Uh1srqlP-gEYReEo30aRqpzdZe38MCoOtl6dfz1FQmcwSExPl6GD32X-Z5y5LvvzIBiafZiDlzy3WtGkMFx7HTnreYmu0GPcuTrGRYLlGSXQYqkzLIoGb-q_jqu37xo-04QNawy-H_7_p37ume-E37ATOB6Tm6r4vdeU2HiwJAmhyHmFTGUsTvOlz92O3uTAQLCL3cD1LzGL5ogj58mEbM5yDrsrLRnP7e05ou1gMMK8UEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/733c9968e4.mp4?token=Nr0sN44WU0LFb13P-_byB-dXDo4Tu8g7C4cba7D9yCuBbhoHo5Gys1Knx-S8ni8JLYv3qfrgX6gPnfsQTLKA5N6048Hd_5rDuZCEjT8Uh1srqlP-gEYReEo30aRqpzdZe38MCoOtl6dfz1FQmcwSExPl6GD32X-Z5y5LvvzIBiafZiDlzy3WtGkMFx7HTnreYmu0GPcuTrGRYLlGSXQYqkzLIoGb-q_jqu37xo-04QNawy-H_7_p37ume-E37ATOB6Tm6r4vdeU2HiwJAmhyHmFTGUsTvOlz92O3uTAQLCL3cD1LzGL5ogj58mEbM5yDrsrLRnP7e05ou1gMMK8UEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای منابع حکومتی: حمله موشکی به اطراف پایانه مسافربری در مرز شلمچه
ولی الله حیاتی معاون امنیتی و انتظامی استانداری خوزستان اعلام کرد: دقایقی پیش اطراف پایانه مسافربری در مرز شلمچه مورد هجوم موشک های دشمن تروریستی آمریکا قرار گرفت.
به گفته وی، تردد زائرین بدون مشکل در حال انجام است.
منابع حکومتی: کشته شدن دو نفر
معاون امنیتی و انتظامی استانداری خوزستان اعلام کرد: تاکنون ۲ نفردر حمله دشمن آمریکایی به مرز شلمچه به شهادت رسیدند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/77411" target="_blank">📅 03:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77410">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SDHn8YDNJPDuRkMap2Q2CFh2gh2PDMnyxrxFbtIlrDfGI7JFekGeW8EZu3qEL0DeYga0gLMkC-nIQejd33ErvGT0CO0m4tTaL79FJFEk5E-0PRQCoZQzRi-2YNTLCcgHpz5uAI9V7sb6dSwM1nwH0Ex77eSqBkvgrHuHL--2UnfU5bPWN9YIC-x-y7Ax93Xwma0wfbbpp36PBln5mUTuCXJwKsXM4uKKYX0c7sCMrGAjKUNxm-AtxGTWr7gAKBACy_a-QpftPkXhWt7CaeOCWVwGoKRezDFLLKCWkf-z1uVbzC0NS7vQFch0XpTmzeyp68wXnZys2E8QB7gv3Xp-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا گفت تفاهم‌نامه با جمهوری اسلامی بر پایه پایبندی به تعهدات بود، اما تهران آن را نقض کرد و در نتیجه این توافق دیگر معتبر نیست.
او افزود تفاهم‌نامه شامل بازگشایی تنگه هرمز و تضمین آزادی کشتیرانی بود و جمهوری اسلامی باید حدود یک هفته و نیم پیش بیانیه‌ای در این باره منتشر می‌کرد، اما در همان روز به یک کشتی حمله شد.
وزیر خارجه آمریکا همچنین گفت واشینگتن همچنان از دیپلماسی و راه‌حل مذاکره حمایت می‌کند، اما به نظر می‌رسد جمهوری اسلامی در حال حاضر در این زمینه جدی نیست.
روبیو افزود، چین نیز با اقدام‌های جمهوری اسلامی در تنگه هرمز و اعمال عوارض بر عبور کشتی‌ها مخالف است.
به گفته مارکو روبیو وزیر خارجه آمریکا، جمهوری اسلامی با مشکلات اقتصادی جدی روبه‌رو است و شهروندان ایران با تورم بالا و افزایش شدید قیمت مواد غذایی مواجه هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77410" target="_blank">📅 03:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77409">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سخنرانی ترامپ در ایالت جورجیا، بخش‌هایی مرتبط با ایران، ترجمه ماشین:
...
اما میلیون‌ها و میلیون‌ها بشکه نفت در راه است و ونزوئلا هم اکنون بهتر از هر زمان دیگری عمل می‌کند. شرکت‌های بزرگ نفتی وارد می‌شوند و قرارداد می‌بندند. کریس رایت روی آن کار می‌کند، داگ برگم هم روی آن کار می‌کند، اسکات هم با آن‌ها کار می‌کند و واقعاً فوق‌العاده بوده است. آنجا ذخایر عظیم نفت دارد.
در واقع، اگر آمریکا و ونزوئلا را با هم حساب کنید، حدود ۶۲ درصد بازار نفت جهان را در اختیار داریم. بنابراین ما به تنگه‌ها نیازی نداریم؛ به هیچ‌چیز نیاز نداریم. به تنگه هرمز نیازی نداریم، اما وارد عمل می‌شویم، چون مجبوریم؛ چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.
در قبال جمهوری اسلامی ایران نیز در حال پیروزی هستیم و تضمین می‌کنیم که آن‌ها هرگز، هرگز نتوانند همان کاری را که با بسیاری کرده‌اند با ما انجام دهند. می‌دانید، آن‌ها بیش از ۵۲ هزار معترض را کشته‌اند. افرادی که اعتراض می‌کردند کشته شده‌اند؛ ۵۲ هزار نفر در چهار ماه گذشته. هیچ‌کس نمی‌خواهد درباره‌اش حرف بزند. رسانه‌های جعلی آن عقب هرگز به آن اشاره نمی‌کنند.
[ + جملاتی مربوط به مراسم سربازان کشته‌شده آمریکایی که در ویدیو هست ولی در پست جا نمیشه.]
---
بازار سهام رکورد زده است؛ آن هم در حالی که این درگیری کوچک در جریان است. من آن را یک «درگیری کوچک» می‌نامم. این درگیری کوچک ما با جمهوری اسلامی ایران است.
دلیل اینکه آن را این‌طور می‌نامم این است که، بگذارید بگویم، آن‌ها چنان سخت هدف قرار می‌گیرند و می‌خواهند توافق کنند. اما من می‌گویم هنوز برای توافق آماده نیستند، چون هر بار توافقی می‌کنند، می‌خواهند آن را تغییر دهند و چیزهای دیگر.
هنوز آماده نیستند. خیلی زود آماده خواهند شد. با وجود اینکه این وضعیت همچنان ادامه دارد، بازار سهام رکورد زده است.
---
نفت نیز پایین خواهد آمد؛ قیمتش سقوط خواهد کرد.
سه هفته پیش فکر می‌کردند توافق کرده‌ایم. گفتم: «فکر نمی‌کنم با این‌ها توافقی داشته باشیم. آن‌ها هر توافقی را که می‌بندند، نقض می‌کنند.»
اما مردم و نابغه‌های وال‌استریت فکر دیگری می‌کردند. قیمت نفت خیلی پایین آمد، بعد کمی بالا رفت، اما دوباره پایین خواهد آمد؛ شاید حتی پایین‌تر از زمانی که شروع کردیم. فقط کمی به من فرصت بدهید.
من همیشه می‌گویم: «کمی به من فرصت بدهید.» به کشاورزان هم گفتم: «کمی به من فرصت بدهید و ببینید اوضاع کشاورزان و مزارع چطور پیش می‌رود. این کشور با قدرت در حال پیشروی است.»
---
فقط در ۱۸ ماه، این کشور را به شکلی متحول کرده‌ایم که هیچ‌کس پیش‌تر ندیده است. فکرش را بکنید: مرز ما امن است، اشتغال افزایش یافته، تورم به‌شدت پایین آمده و کارخانه‌ها در حال افتتاح هستند.
سرمایه‌گذاری به کشورمان سرازیر می‌شود. گفتم: ۱۹٫۲ تریلیون دلار. ارتش ما با فاصله‌ای بسیار زیاد از همیشه قدرتمندتر است. می‌بینید؟ ونزوئلا، ایران.
آمریکا بازگشته است. از همیشه قدرتمندتر است و به شما می‌گویم که فقط در یک جهت حرکت می‌کند: رو به بالا.
تا زمانی که همین طرز فکر و همین نظام کنونی را حفظ کنیم، رو به بالا می‌رویم. اگر راه دیگری را بروید، هیچ‌چیز موفق نمی‌شود.
یک بار گفتم: «در کمونیسم، همه‌چیز به گُه تبدیل می‌شود.»
بسیار خب؟ حقیقت دارد. چیز وحشتناکی است.
The White House
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77409" target="_blank">📅 03:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77408">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EB2954JhsFhfwNHoVRml5TBqDwV4umvyhYIdiDsyvOyvp2KyBs3mEpw1fOwAih_XBoOCD9p6yiBo5whbj4g4zAaJQeOZAzY8lGnOyrN5nI5zAtTF9mJba9Y5vKslXnwmNSBXjGTI7D2tQQ9MGE70IK_xv04PFr-Lp2dG5ivo0VAqtNoBZh-XPBhP61R_9OPRX3NvEcUgKtkhhBrOvevGZ4uOEbLmg4TJR1wXy7An1rLgUFnKY6FIikSsdBsbG-gqJEPLrnCTdUMmKi4eqkHfXe0n8viZ2xHRANc8scBArrF-WJlNeA34fUCyH4G0WOkpI9hgENY1xuSmD2v398CGNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ستاد کل ارتش کویت، بامداد پنجشنبه اول مردادماه، با صدور بیانیه‌ای اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات پهپادهای «متخاصم» هستند.
در این بیانیه، این حملات تاکید شده است که صداهای انفجار احتمالی، ناشی از رهگیری و انهدام این اهداف توسط سامانه‌های دفاعی کویت در پی حملات «تجاوزکارانه ایران» است.
ارتش کویت همچنین از شهروندان خواست ضمن حفظ آرامش، دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای مسئول را رعایت کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77408" target="_blank">📅 02:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77407">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lzlsg68GchvoCpgyr45vFNQTAwnP56aSmi1G3qk09Bcj4R-d8-AZySmAM3Z7Z88U1kBIShCj9HtKvrDmrJtYfOu5uXxzKxoqXzzuNdFOKbvT7w4s0H1Jy8Iltf0o6vHEhCZsYKP0X6JB3Ay1_0KSueTSurHU5CK7i4qTX24iJZuu_S-rqMXyDGC9DAj22HHk1HABpFrZOgt9ZVuhzcvQDzjcByupQa4s1_e7uH4PdvM0b5KCnxWIEt85GT2sP0ZSuCfKP-OFIA0mm0EoIZamU7AqLRUAz9YMCEz91JZ-4JL3c2_D2YjYPIj0pB82M35rzOarupunHJ6yrMoyV16lWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۵:۳۰ بعدازظهر به وقت شرق آمریکا [ساعت ۱:۰۰ بامداد پنج‌شنبه به وقت تهران]، نیروهای ایالات متحده به دستور فرمانده کل قوا دور تازه‌ای از حملات علیه اهداف نظامی ایران را آغاز کردند. این عملیات ادامه خواهد یافت تا توانایی ایران برای تهدید دریانوردان غیرنظامی و کشتی‌های تجاری در حال تردد در آب‌های منطقه بیش از پیش تضعیف شود.
CENTCOM
نکته قابل توجه این که همه گزارش‌های امشب درباره صدای انفجارها مربوط به پیش از ساعت یک بامداد بودند!
حالا یا ساعت رو درست ننوشتند یا اون حملات کار آمریکا نبوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77407" target="_blank">📅 01:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77406">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cmboHNT3nQLSew5MgAnrmR90ALqHb-jzWVWyrzc-6i0iouX_T3uEVdaFU9Myupbk4qnUmgwbqanbyhILNaBYLzwz-oWwq960BGRwBbcgzTIYxOvb1bc3mkvbjTr4FVGP5uRkiOismfg097pqNP1hZCEVdcWKr07qhfhKU61-FKbsN1BwPCtlZyxeS7qs1op2c-yanNqlsIOCUmaqYK2m9XMD3WGSzH-Dra4IOKpdPVN_LlKtcrp6tycN7ocfdxep4xM8My0qaAAV2yWIvn6qPYz8pu2fVtjrHLppHrOXYk-7-6tb_Qo9nCgGq9NbuRI7eBUpjcyL570OoTDMp2u80Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت گزارش در تصویر: ۲۳:۳۰ چهارشنبه به وقت ایران
یعنی قبل از گزارش‌ها درباره شنیده شدن صدای انفجارهای خوزستان و هرمزگان در بامداد پنج‌شنبه
ترجمه ماشین:
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از وقوع یک حادثه در ۷۰ مایل دریایی جنوب‌غربی الشقیق، عربستان سعودی، دریافت کرده است.
ناخدای یک نفتکش گزارش داده است که یک پرتابه ناشناس به کشتی برخورد کرده و باعث آتش‌سوزی در عرشه شده است؛ خدمه در حال حاضر مشغول مهار آتش هستند.
هیچ تلفاتی یا پیامد زیست‌محیطی گزارش نشده است.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/77406" target="_blank">📅 01:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77405">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پیام‌های دریافتی:
سلام بوشهر دو صدای انفجار ساعت 12 و 49
صدای دو انفجار بوشهر 0.49
بوشهر و زد همین الان
سلام وحید بوشهر همین الان دوتا پشت سر هم بد زدن
وحید بوشهر زد دوبار ۰۰:۴۹
خود بوشهر زدن ساعت۱۲:۴۹ دوتا پشت هم
دوتا انفجار خیلی شدیدبوشهر
پایگاه هوایی الان
همین الان بوشهر ساعت ۱۲.۴۹ سمت بهمنی رو زدند.
وحید بوشهر پایگاه هوایی زد
سلام،۱۲:۴۹ دقیقه دوبار بوشهر رو زدن
بوشهر ساعت ۱۲:۴۹
سه صدای انفجار
۰۰:۴۹ صدای دو انفجار شهر بوشهر
بوشهر دو سه انفجار بود خیلی صدا داشت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77405" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77404">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تسنیم:
شنیده شدن صدای انفجار در بخش بمانی شهرستان سیریک
همچنین دقایق پیش صدای چند انفجار در اطراف روستای زیارت شهرستان سیریک شنیده شد.
دوباره، تسنیم:
بر اساس گزارش منابع محلی، ۵۰ دقیقه بامداد صدای انفجار در سیریک شنیده شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77404" target="_blank">📅 00:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77403">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">در اهواز صدایی شنیده شده.
آپدیت: چند پیام هم از رامشیر، ماهشهر و سربندر داشتم.
پیام‌های دریافتی درباره اهواز:
وححححيييد
زدن
بعد از روزها..
اهواز ساعت ١٢:٠٩
اهوازو زدن
اهواز انفجار ۱۲:۹
وحید جان اهواز ۰۰:۰۸ صدای انفجار شدید
آقا اهواز زد دو بار
اهواز انفجار ۱۲:۹
سلام ساعت ۰۰:۰۹ اهواز صدای انفجار اومد
سلام وحید اهواز همین الان صدا برخورد اومد
۰۰:۰۸ دقیقا
سلام وحید اهواز یه صدایی اومد ۱۲:۰۹
اهواز ۱۲:۱۰ صدای انفجار
وحید همین الان ۱ ۱۰دقیقه بامداد انفجار شدید اهواز
وحید داداش ۲ تا انفجار ۰۰:۹ اهواز
اهواز به نظر میاد ساعت 00.10 یه انفجار مهیب بود. فقط لرزش رو حس کردیم.
سلام وحید جان اهوازو زدن
00:08  اهواز انفجار
وحید اهواز ساعت ۱۲:۰۹ دقیقه ۲ بار صدا انفجار اومد
سلام اهواز صدای یک انفجار شنیدیم
اهواز دو تا صدا اومد
وحید الان اهواز ۲بار پشت سرهم صدا اومد
تو اهواز دوبار صدای انفجار اومد
🔄
منابع حکومتی:
ولی الله حیاتی معاون امنیتی و انتظامی استانداری خوزستان اعلام کرد: یک نقطه در اطراف شهر اهواز توسط دشمن آمریکایی مورد حمله موشکی قرار گرفت.
‌
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77403" target="_blank">📅 00:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77402">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sxAAyRvke6P1Oqq848g9YIFvPHlrM3L37P1KR7Q69397VuptmDYnScZgzDPVx1HrsYTePnoH1Zhv4MglM2ao1cpF58UaCg1VvqZyZ07P1jWS269H74Zlj5vIW1pjMRqFSrG8g-UbykbZkDOqAtce-cBM7hQ_UcyNqiSXs3l7HLXNT6UV6G2X-6WH-dBsaj2coS8REEqtyd6u49zI5lHrfcoxLLCsFT0soxFOCybG7oG6owTNzOx3WA7ysPy4cV6zPjNx4v6LARO1Msvz_SaqyAVd7N5pZs1gE0_Xgf3yZ2q2-tRWFY5_vlos1C4Q6g0lSFdcmGnZQa_AHS6i1tdegg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: امروز نیروی دریایی سپاه پاسداران انقلاب اسلامی ایران مدعی شد که ورود و خروج از تنگه هرمز را کنترل می‌کند؛ ادعایی که نشان می‌دهد دریانوردان بین‌المللی فقط می‌توانند از مسیرهای مورد نظر سپاه استفاده کنند. این ادعا نادرست است.
✅
واقعیت: ایران تنگه هرمز را کنترل نمی‌کند. این آبراه بین‌المللی، صرف‌نظر از تهدیدها و حملات سپاه، همچنان برای عبور و مرور باز است. کشتی‌های تجاری با حمایت نظامی آمریکا همچنان از این تنگه عبور می‌کنند. از اوایل ماه مه، نیروهای آمریکایی به عبور بیش از ۹۰۰ کشتی از تنگه کمک کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/77402" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77401">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
دکترین دفاعی ما روشن است: چشم در برابر چشم.
هرگونه تجاوز علیه ایران، از جمله علیه زیرساخت‌های ما، با پاسخی قدرتمند و قاطع روبه‌رو خواهد شد.
کسانی که به هر شکلی در چنین تجاوزی مشارکت داشته باشند، آن‌ها نیز اهداف مشروع تلقی خواهند شد.
Our defense doctrine is clear: eye for an eye.
Any aggression against Iran, including our infrastructure, will compel a powerful and decisive response.
Those who contribute to such aggression, whatever the kind of support, will also be considered as legitimate targets.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/77401" target="_blank">📅 22:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77400">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اکسیوس:‌ رئیس جدید موساد با رئیس سیا درباره ایران دیدار کرد
ترجمه ماشین:
به گفته دو منبع مطلع، رومن گوفمن، رئیس جدید سازمان جاسوسی موساد اسرائیل، دو هفته پیش برای گفت‌وگو درباره جنگ در ایران و برنامه هسته‌ای ایران به واشنگتن سفر کرد.
چرا مهم است: گوفمن یکی از نزدیک‌ترین مشاوران بنیامین نتانیاهو، نخست‌وزیر اسرائیل، است. این نخستین سفر او به واشنگتن از زمان تصدی این مقام در ماه ژوئن بود.
خبر اصلی: سفر رئیس موساد درست پیش از تشدید تنش‌ها در تنگه هرمز و ازسرگیری درگیری‌ها انجام شد.
یک منبع اسرائیلی گفت یکی از اهداف سفر گوفمن، هماهنگی با کاخ سفید درباره مذاکرات با ایران برای دستیابی به یک توافق هسته‌ای بود.
پشت پرده: منابع گفتند گوفمن با جان رتکلیف، رئیس سیا، و همچنین مقام‌های کاخ سفید دیدار کرد.
در حلقه نزدیکان ترامپ، رتکلیف یکی از صداهای تردیدآمیزتر درباره یادداشت تفاهم با ایران بود.
او پیش از امضای این یادداشت تفاهم هشدار داده بود که ایران این توافق، از جمله مفاد مربوط به تنگه، را متفاوت از آمریکا تفسیر خواهد کرد.
سیا و موساد از اظهارنظر خودداری کردند.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/77400" target="_blank">📅 21:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77399">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پست قالیباف:
معادلهٔ این جنگ مشخص است: یا همه یا هیچکس!
در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت. اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود و امنیت تنگه در نبود نیروهای آمریکایی است. بارها گفته‌ایم که وضعیت تنگه به قبل از جنگ باز نمی‌گردد.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77399" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77398">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fdcc2765ea.mp4?token=YDU_8e6uXHK7-qkdo3-MkJRqvqkmB_DnlmgP8gKh8wmb2AB7Tzs3nN0hFITrbqWNPveJgliICsmlVfVTUp5XSb_RistZ3MX4M0U0DgoU_JzPQ9syqylPuVl935K2Snwf-vBp5PpgvCKPL1HBcYe8cg2cbue8X73Pjc04tcAvCZd65lp_PN7LVlxva52i7xDgIr9n80nNKaZHRL0u6A0Ef-lvbbhReWOKb1ONlExqrj4bjMKQC76uMePAE6u4gEti57uAftlkyVgwjRT-NasyHn62RhYSJ6Rt-hAAcwkbISiDcSWohXcNdiAzTKH8X2-hdSCIY-38pOEBFz00eMTNpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fdcc2765ea.mp4?token=YDU_8e6uXHK7-qkdo3-MkJRqvqkmB_DnlmgP8gKh8wmb2AB7Tzs3nN0hFITrbqWNPveJgliICsmlVfVTUp5XSb_RistZ3MX4M0U0DgoU_JzPQ9syqylPuVl935K2Snwf-vBp5PpgvCKPL1HBcYe8cg2cbue8X73Pjc04tcAvCZd65lp_PN7LVlxva52i7xDgIr9n80nNKaZHRL0u6A0Ef-lvbbhReWOKb1ONlExqrj4bjMKQC76uMePAE6u4gEti57uAftlkyVgwjRT-NasyHn62RhYSJ6Rt-hAAcwkbISiDcSWohXcNdiAzTKH8X2-hdSCIY-38pOEBFz00eMTNpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ کاخ سفید را به مقصد پایگاه نیروی هوایی «دوور» ترک کرد تا در مراسم رسمی مربوط به سربازان آمریکایی کشته‌شده شرکت کند.
تشخیص و ترجمه ماشین:
ترامپ:
برای ادای احترام به قهرمانان‌مان می‌رویم؛ و آنها واقعاً قهرمانان بزرگی هستند. واقعاً. آنها گفتند، و همه‌شان با قاطعیت گفتند: «نمی‌توانیم اجازه بدهیم ایران سلاح هسته‌ای داشته باشد.» آنها سلاح هسته‌ای نخواهند داشت.
بنابراین می‌خواهیم به آنها ادای احترام کنیم. این برای من یکی از سخت‌ترین کارهایی است که یک رئیس‌جمهور باید انجام بدهد، اما باید انجام شود. فکر می‌کنم، همان‌طور که برای ادای احترام به این سربازان می‌رویم...
خبرنگار:
آیا درباره تحقیقات، اطلاعات تازه‌ای دارید که مشخص کند [چگونه آن‌ها در اردن کشته شده‌اند]؟
ترامپ:
نه، دارند روی آن کار می‌کنند. نتایج منتشر خواهد شد. می‌دانید چیست؟ ایران...
خبرنگار: [گفته می‌شود ایران پادگان‌ها را هدف قرار داده].
ترامپ: نمی‌دانم. خب، آنها بهای سنگینی خواهند پرداخت. دارند... در حال نابود شدن هستند.
خبرنگار:
قطعاً در میان خانواده‌های این سربازان، کسانی هستند که با این جنگ مخالف‌اند. به آنها چه می‌گویید؟
ترامپ:
خب، آمریکایی‌ها مخالف جنگ نیستند. یک نظرسنجی... یک نظرسنجی همین حالا منتشر شده. آمریکایی‌ها نمی‌خواهند قیمت بنزین بالا باشد، اما مخالف جنگ نیستند. این موضوع در آن نظرسنجی کاملاً روشن بود.
هیچ‌کس نمی‌خواهد ایران سلاح هسته‌ای داشته باشد. شما می‌خواهید ایران سلاح هسته‌ای داشته باشد؟ فکر می‌کنید خوب است؟ بفرمایید.
خبرنگار:
[نامفهوم]؛ به آن چه پاسخی می‌دهید؟
ترامپ:
تنها چیزی که خواهم گفت این است: «دوستتان داریم. فرزندتان را دوست داریم.» و آنها برای خانواده‌هایشان همین هستند؛ آنها فرزندان‌شان هستند. هیچ بازی‌ای در کار نیست، هیچ‌چیز. او فرزندشان است. و تنها کاری که می‌توانید بکنید این است که هرچه در دل دارید نثارشان کنید.
متشکرم. بسیار متشکرم.
خبرنگار:
پس مذاکره با آنها در بحبوحه جنگ چه فایده‌ای دارد؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/77398" target="_blank">📅 18:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77397">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l9nX8PSyBDh3lg93QkU44RN21ztG7ITrX-tdy3z3v0JBpG-l_FnmIEjDMLyhZK6a37fIyI3RKhX3PAbobrfOFk5BE11VYgEW931utxc0F5LmvIrZzK4N5bmd0jLjGaiLThBdEG2nWAoDThO8YrcyuQ2_LsPodZiMsZRv67Tq5gNUpYQ1rNDuA-4mCW4iuzjSi--tpQGINf51xUhYfpnBqOBj1J2rQYY3syjTWXkSnd-ca1yLjjIyCsP-DcEgWeVU_C-x83qVfCW81NgMDuKIJnn9trvx-3ajL70sXk5l-pzXII9QwPqSQYZoUcDVeAiZOtsEv2HaRhlYSEdJRvBG7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز چهارشنبه ۳۱ تیر، گزارش داد جزیره لارک در تنگه هرمز ساعت ۱۴:۴۸ هدف حمله موشکی آمریکا قرار گرفته و به گفته ساکنان منطقه، صدای انفجار شدیدی در حوالی این جزیره شنیده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77397" target="_blank">📅 17:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77396">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eubOsOY-17Fq5l66kFce5Uweri5lNGeEvO39IiCcPC5Y7g64y20jkz8Vy5l2efdK2tzUAK79G1r1WeUzeqUU1KzB5fopel-bGBqalWue96bIT6BA7ScKL0G9Hy8Vh4cfCf9fBvbZEoEreVUwT-TTAgOxY4vWw4LohQYG1S_KXXQ5SnGlh3M18H5ZqMmzf3jEUmrlsn16iSHeVyx-A3ru54uttIwaDM1AZA33gu2alR80brtWSoUNUyNi0zy46jmTLTsF5l76NTFUcBR4Eony0b8EPzG67Lg4hPqeO_mRtYHw9VVq6zMVz4UswhoeXj-6mIhf7O6f4uhp4pgBppP9GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ:
از این لحظه به بعد،
هر بار که جمهوری اسلامی ایران به یک کشتی در تنگه هرمز شلیک کند
ــ چه با موشک، راکت، پهپاد یا هر وسیله یا سلاح دیگری ــ
ایالات متحده
یک پل یا نیروگاه برق
را بمباران و نابود خواهد کرد؛
از جمله پل‌ها یا نیروگاه‌هایی که در نزدیکی یا داخل پایتخت، شهر تهران، قرار دارند.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
From this point forward, any time the Islamic Republic of Iran shoots at a ship in the Strait of Hormuz, whether it be by Missile, Rocket, Drone, or any other device or weapon, the United States will bomb and destroy ONE BRIDGE OR POWER PLANT, including those located next to, or in, the Capital City of Tehran. Thank you for your attention to this matter! President DONALD J. TRUMP
realDonaldTrump
پل و نیروگاه برق رو با حروف بزرگ تایپ کرده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/77396" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77395">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BsvVgnLa9Gt2PMJeUv4DmfnOO8Gy95tuoQIf5zs1t9DJ_AoP4csFPc9ekr0O870WFtpKllmOrlED4oL3ecxjH2nBX5yPRQ8-si9tk8Q8kVUTpdThiyPKzB-2wC80arLhVmnnBoNY-l0F56KEiQh19wC_8jI9EAr50PFIF0uEvMEIlRg_z20D9WekUolvkSVO_Sy2R-WKOfn-XXyB5uR654frPE-2GbT49ZUVTWdeYxf5PDircrt8WFdQIHD6C-2VfvAR8s1uYfsIeZ1ePnK9K1KtOU2E9rDLwbQVLG5TjkFbu7oJQEuSGnoLH7Xso9lNskdIRb-tOLwzRRIUrFCRRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز چهارشنبه ۳۱ تیرماه با انتشار پیامی در اکس نوشت که ایران هیچ فعالیت هسته‌ای در «کوه‌گلنگ» ندارد.
این نخستین واکنش رسمی یک مقام جمهوری اسلامی به گزارش‌ها از انتقال هزاران سانتریفیوژ به کوه‌کلنگ در پاییز سال گذشته به شمار می‌رود.
بقایی در این پیام نوشت:‌ «حملات و تهدیدات مکرر ایالات متحده علیه تاسیسات هسته‌ای صلح‌آمیز ایران نه تنها نقض آشکار اصول اساسی منشور سازمان ملل متحد، حقوق بین‌الملل و قطعنامه‌های شورای حکام آژانس بین‌المللی انرژی اتمی، کنفرانس عمومی و شورای امنیت سازمان ملل متحد است، بلکه دشمنی ریشه‌دار ایالات متحده با پیشرفت علمی و توسعه فناوری ایران را نیز آشکار می‌کند.»
دونالد ترامپ، رئیس جمهوری آمریکا روز گذشته و در جریان دیدار با رئیس جمهوری لبنان گفته بود فکر می‌کند به‌زودی ضربه سختی به این تاسیسات هسته‌ای ایران خواهد زد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77395" target="_blank">📅 17:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77394">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6910775c10.mp4?token=mlvT1vpWGMa309iF6WxppPSyWXc5JqzggdloBvQoLMIFmzjH19AmLMeRkfpczLuVMFqZcLtt3XLFWdvPZMiiezRQwGwBxP7Kfxk91GmrculPvz-9b6G0L6NdNvSUPUeuJHNHZqwOzYrRB7V4J7OTHeaEJ0iigWD8rYt3bDZ4QZX92eaKbCvfA22uBQks3_kaNDnv6VFq2hibly0c9Ze-ZJ2itWH0LKnvDa25byzbuP8e3iU08mV_evKCzWi9ZZ6yizK29i1-tDPyU4Kt_mXhAf5cPLUZ4DYdWd5JLgzzj6JMl3Dis_jVAsdSWO4UaZ2CGLaUsJpFm9xUoJeBue0A5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6910775c10.mp4?token=mlvT1vpWGMa309iF6WxppPSyWXc5JqzggdloBvQoLMIFmzjH19AmLMeRkfpczLuVMFqZcLtt3XLFWdvPZMiiezRQwGwBxP7Kfxk91GmrculPvz-9b6G0L6NdNvSUPUeuJHNHZqwOzYrRB7V4J7OTHeaEJ0iigWD8rYt3bDZ4QZX92eaKbCvfA22uBQks3_kaNDnv6VFq2hibly0c9Ze-ZJ2itWH0LKnvDa25byzbuP8e3iU08mV_evKCzWi9ZZ6yizK29i1-tDPyU4Kt_mXhAf5cPLUZ4DYdWd5JLgzzj6JMl3Dis_jVAsdSWO4UaZ2CGLaUsJpFm9xUoJeBue0A5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجۀ ایالات متحده می‌گوید واشینگتن برای تعامل و گفت‌وگو با ایران با هدف حل‌وفصل اختلافات آمادگی دارد.
مارکو روبیو که در مانیل پایتخت فیلیپین به‌سر می‌برد، گفت مشکل این است که «تهران در مورد گفت‌وگو جدی نیست».
وزیر خارجۀ آمریکا در دیدار با همتایانش از کشورهای جنوب شرقی آسیا عضو آسه‌آن، که نسبت به دور جدید درگیری‌ها بین آمریکا و ایران ابراز نگرانی جدی می‌کنند، گفت: «اگر ایرانی‌ها جدی باشند، ما هم جدی هستیم. اگر آنها جدی نباشند، آنوقت برای حفاظت از منافع‌ حود و متحدانمان به هر اقدامی که لازم باشد، دست می‌زنیم».
مارکو روبیو در این نشست همچنین گفت باز گذاشتن دست ایران برای کنترل تنگۀ هرمز، «سابقه‌ای خطرناک» را بوجود خواهد آورد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/77394" target="_blank">📅 17:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77393">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0ShxsoPFfdXNSs0AYq0X9PFFGYEs8hhA8BoqNJd-AlHwBRgqnSL7ZR2HvmUeWTB2C5vBPyq3Nz7aH02O_gdHm9ye6wsHnrSfvGWMdNL7KuooolEr-Mxc4X95kLZlIqxWJ2MvdDJ8wGZZstz9Gf22oMrQgQAbpZk36a9jBuq7KZUW0LlJjrxOBoEng2DVGteRDFaDQpQjHyLgQI6MHAKTXE24CJdO6FwyxMm0ZnGqb9HFUn0tf25-8Iq-vBzwWBNaqCTY6O1P0MEpFfLGHsTiWpDcQ6N8lfxy01ZgTPN_bic8PXgwhnUDez4A_OsOp60T4rdA3ED3lT5gXklZ5GX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اعدام آقای مهدی خانکی؛ از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴
🔸
مرکز رسانه قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام آقای مهدی خانکی، از بازداشت‌شدگان مرتبط با اعتراضات سراسری دی‌ماه ۱۴۰۴، خبر داد. این نهاد اعلام کرده است که وی پس از تأیید حکم در دیوان عالی کشور اعدام شده، اما زمان و محل اجرای حکم را اعلام نکرده است.
🔸
قوه قضاییه مدعی است که آقای مهدی خانکی به اتهام «اقدام عملیاتی به نفع اسرائیل، آمریکا و گروه‌های متخاصم» و همچنین «ساخت، تهیه و نگهداری اسلحه، مهمات جنگی و استفاده از آنها» از سوی دادگاه انقلاب کرج به اعدام و مصادره اموال محکوم شده بود. این نهاد همچنین ادعا کرده که وی در ۲۱ بهمن ۱۴۰۴ در کرج بازداشت شده و در بازرسی از منزلش سلاح، مهمات و مواد منفجره کشف شده است.
🔸
با این حال، جزئیات مستقلی درباره روند دادرسی، مستندات پرونده، نحوه اخذ این اعترافات و دسترسی وی به وکیل مستقل منتشر نشده است.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/77393" target="_blank">📅 17:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77392">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">معاون استاندار همدان اعلام کرد در ادامه حملات آمریکا، ساعتی پیش نقاطی در شهرستان کبودرآهنگ هدف حمله هوایی قرار گرفت.
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
پیام ساعت ۳:۵۹
آقا پادگان نوژه همدان شخم زدن
پیام ساعت ۴:۰۸
سلام پایگاه نوژه همدان صدا انفجار پی در پی اومد
خبرگزاری تسنیم، وابسته به سپاه پاسداران، گزارش داد آمریکا ساعت ۰۲:۵۵ بامداد چهارشنبه ۳۱ تیرماه یک نقطه در خارج از محدوده شهری بانه در استان کردستان را هدف حمله قرار داد.
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
وحید بانه رو زدن
صدای انفجار همین الان اومد
بیرون شهره نمیدونم کجاست
بانه صدای جنگنده اومد
بعد صدای انفجار ازدور  میاد
همین الان‌۲:۵۸ دقیقه
برای سومین شب متوالی
گردنه خان بانه رو زدن
همون تایم
پیام قبلی ایشون (شب قبلش):
رادار گردنه خان بانه رو زدن
ساعت 2.20 نصف شب
چوار، آبدانان، انارک و دینارکوه در استان ایلام نیز هدف حمله قرار گرفتند.
فرماندار آبدانان گفت این حمله‌ها هیچ تلفات جانی نداشته است، اما حمله هوایی به منطقه انارک در چوار باعث آتش‌سوزی در زمین‌های منابع طبیعی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 514K · <a href="https://t.me/VahidOnline/77392" target="_blank">📅 05:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77391">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پیام‌های دریافتی:
من تهرانم دوباره صدای پدافند داره میاد
پدافند مشیریه
دوباره پدافند داره کار میکند شرق تهران
صدای پدافند شدید افسریه
فعال شدن مجدد پدافند همین الان خ پیروزی
فعالیت پدافند شرق تهران. ۴:۵۱.
ساعت 4:52 دقیقه فعالیت پدافند شرق تهران
جنوب تهران پدافند 4:51
وحید من منطقه ۱۵ ناحیه ۴ تهران هستم محله مشیریه ۶ انفجار اومد پدافند به شدت فعاله ساعت ۴ و ۵۰ دقیقه
[صدای انفجار لزوما به معنای برخورد نیست. توپ‌های ضدهوایی هم با صدای انفجار شلیک می‌کنند.]
🔄
سلام وحید جان منطقه ۱۵ تهران همین الان ساعت ۰۵/۱۵ پدافند مشغوله
ساعت 5:15 دوباره صدای پدافند در مشیریه
سلام باز مشیریه همین الان صدا اومد
😂
😐
سلام الان ساعت ۵:۱۴ دقیقه صدای توپ های ضد هوایی و پدافند از جنوب شرق تهران
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 483K · <a href="https://t.me/VahidOnline/77391" target="_blank">📅 04:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77390">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82b30de17d.mp4?token=pTR6eaDe2_9Zpca6SRbTexIdPoir2t-UYZDO5eOgKnPVKAqNQawukCKzI1M6hct9h0N6TrvJ9eqhGn_JRJmD5682QwlN_TnCpFF1Ov5pVSMCJPTNmdM9_As__kWmsCytxSXeu7dqagczhnJzzHE6aJ0KesCrWFFSyNVylN-hCsRf8P4KfVHDmVDwf_fw03tX5IqKcPi6vrea7nQxecFxaTfatXAx-ZG9HCrx25Mx-0dlKouY1RLWyFv7-EAUgTGTBQZv24iorcWU2a4vemOI40cp878YaCv9-CC3ag6ewMkLrsSvo8nG6t5Gu7ijnoY4PIhLuknCJTH3oFBrdYXbPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82b30de17d.mp4?token=pTR6eaDe2_9Zpca6SRbTexIdPoir2t-UYZDO5eOgKnPVKAqNQawukCKzI1M6hct9h0N6TrvJ9eqhGn_JRJmD5682QwlN_TnCpFF1Ov5pVSMCJPTNmdM9_As__kWmsCytxSXeu7dqagczhnJzzHE6aJ0KesCrWFFSyNVylN-hCsRf8P4KfVHDmVDwf_fw03tX5IqKcPi6vrea7nQxecFxaTfatXAx-ZG9HCrx25Mx-0dlKouY1RLWyFv7-EAUgTGTBQZv24iorcWU2a4vemOI40cp878YaCv9-CC3ag6ewMkLrsSvo8nG6t5Gu7ijnoY4PIhLuknCJTH3oFBrdYXbPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا یازدهمین شب حملات علیه ایران را به پایان رساندند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۸:۱۵ شب ۲۱ ژوئیه به وقت شرق آمریکا [۳:۴۵ به وقت تهران]، یازدهمین شب متوالی حملات علیه ایران را با موفقیت به پایان رساند.
تجهیزات و نیروهای سنتکام مراکز عملیات نظامی ایران، توانمندی‌های دریایی، آشیانه‌های هواپیما، تأسیسات نگهداری پهپاد و زیرساخت‌های لجستیکی نظامی را هدف قرار دادند تا توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز بیش از پیش تضعیف شود.
ایران طی سه ماه گذشته به بیش از ۳۰ کشتی تجاری در حال عبور از این آبراه بین‌المللی که برای تجارت منطقه‌ای و جهانی حیاتی است، حمله کرده است. این حملات بی‌دلیل، صدها دریانورد بی‌گناه را به خطر انداخته و آزادی کشتیرانی را تضعیف کرده‌اند.
با وجود اقدامات تجاوزکارانه ایران، تنگه هرمز همچنان برای عبور کشتی‌های تجاری باز است. از اوایل ماه مه تاکنون، نیروهای سنتکام به تسهیل عبور حدود ۹۰۰ کشتی تجاری و ۴۵۰ میلیون بشکه نفت خام کمک کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 460K · <a href="https://t.me/VahidOnline/77390" target="_blank">📅 04:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77386">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec4c08a6e7.mp4?token=vFJlTibnePhLwuObg2GC66xxtGfz8XJv58q_25nFxEYwWfUaOacqe-NDsLSfNh_dDZAKiDwvUydnZxcgpD9NzgLKkHXAe4n6In0YRoaHLMEhBXC7ASf7ZdKzC3YVz2f8_XKL6IIlJ-iDUPDrBMToNdb1r88Oux1DehMotMnU5tnfMjIx6iyQ6fQBEDY4Vgdpp67AwPzFOHWEqRT8vnT-xMs1xJdey6gbieTxngIVWOk7L2HDA15b5Vp2-YYVBbc8afjxV_gnlZ5Ivn0DiGB6Y6GA9n3EO_Q9mkXFFV_HQ7jOYvgjF_diYbMvZU_D4gqPFl8kAyUNF20ymt8UCsZzIg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec4c08a6e7.mp4?token=vFJlTibnePhLwuObg2GC66xxtGfz8XJv58q_25nFxEYwWfUaOacqe-NDsLSfNh_dDZAKiDwvUydnZxcgpD9NzgLKkHXAe4n6In0YRoaHLMEhBXC7ASf7ZdKzC3YVz2f8_XKL6IIlJ-iDUPDrBMToNdb1r88Oux1DehMotMnU5tnfMjIx6iyQ6fQBEDY4Vgdpp67AwPzFOHWEqRT8vnT-xMs1xJdey6gbieTxngIVWOk7L2HDA15b5Vp2-YYVBbc8afjxV_gnlZ5Ivn0DiGB6Y6GA9n3EO_Q9mkXFFV_HQ7jOYvgjF_diYbMvZU_D4gqPFl8kAyUNF20ymt8UCsZzIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای دریافتی با شرح شعله‌های انفجارهای حمله به 'پادگان بخردیان در بهبهان خوزستان'
چهارشنبه ۳۱ تیر، حدود ساعت ۲:۳۰، هم‌زمان با آغاز اعلام حملات از سوی آمریکا
Vahid
📍
میگن
اینجاهاست:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/77386" target="_blank">📅 04:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77385">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پیام‌های دریافتی:
سلام اصفهان صدای پدافند اومد
پدافند اصفهان فعال شد . سمت بهارستان و صفه
اصفهان صدای انفجار اومد الان چندتا پشت هم ولی از خیلی دور
ساعت ۴ صبح صدای پدافند جنوب شهر اصفهان
جنوب اصفهان شهر موشکی رو به روی بهارستان پدافند فعال شد ساعت 4:5
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77385" target="_blank">📅 04:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77384">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/47e213b66e.mp4?token=PZ1sUu2JRRGqKEkWd4cdfqRQn4hBpbRxSna8yZFchu19Tsv-azKO9ACv3MYLHUTMsgOQBuh0djyI-_s5gsP_89A-1S_IgDmFBUp77pELxAt2KoDkzB4xsGneZNv9velWsXNHEnMV7miElELNuqN6cTEK1Npf9ywsYmcNKfhww1QfkPGRZywrXkyDdJ8YVuUEAtn6mBeE4k3LwXk8SBN4X3Aa1nJPwAS0mOUmYPQPRfe7SeGBdk6wkUQEEkOdY1RXkKwIBoHm_3vL9iK1X6bqmATy_IplHBP7lDxjnGakVbizKcB_sOujDEUPC_ex1jpLjJ5toScZbglVUTvqxWYPRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/47e213b66e.mp4?token=PZ1sUu2JRRGqKEkWd4cdfqRQn4hBpbRxSna8yZFchu19Tsv-azKO9ACv3MYLHUTMsgOQBuh0djyI-_s5gsP_89A-1S_IgDmFBUp77pELxAt2KoDkzB4xsGneZNv9velWsXNHEnMV7miElELNuqN6cTEK1Npf9ywsYmcNKfhww1QfkPGRZywrXkyDdJ8YVuUEAtn6mBeE4k3LwXk8SBN4X3Aa1nJPwAS0mOUmYPQPRfe7SeGBdk6wkUQEEkOdY1RXkKwIBoHm_3vL9iK1X6bqmATy_IplHBP7lDxjnGakVbizKcB_sOujDEUPC_ex1jpLjJ5toScZbglVUTvqxWYPRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی ۳:۱۰
دوباره پدافند شمال شرق تهران فعال شد. شدیدتر از دفعه قبل
شرق تهران صدا پدافند
+ ده‌ها پیام مشابه از شهروندانی که همین صداها رو در محله‌های مختلف شرق و شمال شرق تهران شنیده‌اند.
🔄
ساعت ۳:۲۶:
ده‌ها پیام رگباری دیگر درباره صدای فعالیت پدافند
من حتی نمی‌رسم بازشون کنم فقط از پیش‌نمایش دارم آخرین پیام هر کسی رو می‌بینم باز هم کلی عقبم.
پیام‌ها رسیده به مرکز شهر و حتی مناطقی در غرب تهران
گرچه همیشه هستند کسانی که هر صدایی رو به برخورد تعبیر کنند ولی از حجم پیام‌ها واضحه که صدای پدافند شنیده میشه در مناطق مختلف تهران
آپدیت ساعت ۳:۴۰:
تا الان به طور پیوسته در هر ثانیه کلی پیام میومد. الان داره به حدود یک پیام در ثانیه کاهش پیدا می‌کنه.
همچنان درباره صدای پدافند در همه مناطق تهران
آپدیت ۳:۵۰:
سکوت نسبی برقرار شد. میزان نوتیفیکیشن‌ها هم به حالت معمول برگشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/77384" target="_blank">📅 03:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77383">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای سنتکام امروز ساعت ۷ عصر به وقت شرق آمریکا [۲:۳۰ به وقت تهران]، برای یازدهمین شب متوالی حمله به اهداف نظامی در ایران را آغاز کردند. این حملات با هدف ادامه تضعیف توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77383" target="_blank">📅 03:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77382">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فعالیت پدافند در شرق شهر و استان تهران:
پردیس صدای انفجار و پدافند
همین الان شرق تهران
پدافندداره روی شهرک خمینی اتوبان بابایی کار میکنه، فعلا انفجار بزرگی نشنیدم، ممکنه هدف خجیر یا پارچین باشه
صدا پدافند زیاد میاد
ما سمت پردیس هستیم
سلام پردیس صدای انفجار از راه دور اومد
ساعت ۲:۵۰
سلام وحید جان از پردیس چندین انفجار شنیدیم الان
وحید صدای انفجار و پدافند شرق تهران همین الان
سلام تهران حکیمیه ۲:۵۳ دقیقه صدای پدافند میاد
سلام وحید جان همین الان  ساعت ۲:۵۰پدافند پارچین فعاله از پردیس مشخصه
صدای هواپیما میاد
همین دو سه دقه پیش
بشدت پدافندا فعالیت داشتن
پنج شیشتا صدای انفجار اومد
چندبار صدای پدافند سمت شرق ته
ران ۰۲:۵۰
پردیس صدای پدافند و انفجار اومد
شهرستان پردیس فاز ۱۱ از استان تهران صدای مکرر پدافند.  ساعت ۲:۵۵ صبح
شرق تهران(لواسان) صدای پافند ۲:۵۲
پردیس شرق تهران، چهار پنج تا صدا شبیه انفجار واضح ، ولی با فاصله شنیدیم ، حدود ساعت ۲:۵۳ صبح
سلام وحید جان  ساعت ۲.۵۰ دقیقه صدای حداقل ۱۰ انفجار از خجیر  که از حکیمیه شنیدیم
درود وحید جان ساعت ۲:۲۰ دقیقه ما پردیسیم
یه صدایی اومد گفتن سایت هسته ای پارچین زدن
پدافند شرق تهران فعاله
ما پردیسیم
اطراف (احتمالا پارچین)صدای انفجار و پدافند
[+ ده‌ها پیام مشابه دیگر از مناطق مختلف شرق و شمال شرق تهران که دیگه نقل نمی‌کنم و ازشون عبور می‌کنم چون تازه رسیدم به پیام‌های ۱۰ دقیقه پیش و از پیام‌های تازه‌تر بی‌خبرم.
هم‌زمان دارم همه پست‌های قبلی مربوط به شهرهای دیگر رو هم آپدیت می‌کنم با پیام‌های تازه‌تر]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/77382" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77381">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر انفجار
همین الان بوشهر صدای انفجار
بوشهر یکی سنگین
۰۲:۴۸ بوشهر صدای انفجار اومد
سلام خسته نباشید بندر گناوم چند بار موج انفجار اومد ولی نمیدونیم کجاست
بوشهر صدا و انفجار خیلی مهیب اومد
بوشهر صدا اومد ۲:۴۸ ریشهر
بوشهر صدای دو انفجار ساعت 2:48
بوشهر  انفجار فوق فوق سنگین ۲:۴۸
وحید الان ۲:۴۷ بوشهر زد زمین لرزید
وحید جان همین الان بوشهر عاشوری صدای وحشتناک بمب اومد تمام خونه لرزید
همین الان بوشهر دو انفجار بزرگ
بوشهر الآن صدای انفجار اومد، ساعت ۲:۴۷
ساعت ۲:۴۸ بوشهر صدای انفجار اومد!
انفجار وحشتناک بوشهر ۰۲:۴۸
خود شهر بوشهر صدای انفجار
۲:۴۷ بوشهر، یه انفجار خیلی وحشتناک و مهیب
سلام وحید جان همین الان بوشهر صدای انفجار ناحیه پایگاه هوایی و دریایی
سلام بوشهر ساعت دو و چهل و هشت دقیقه تک انفجار
بوشهر 2:48 یک انفجار مهیب محدوده بهمنی
ساعت ۲:۴۸ دقیقه بوشهر رو زدن صداش خیلی بلند بود
سلام آقا وحید، بوشهر ۲:۴۹ یه صدایی اومد و در های خونه کمی لرزید
بوشهرو الان ۲:۴۸‌‌بد زدن پایگاه هوایی
سلام بوشهر ساعت ۲:۴۸ دقیقه انفجار شدید
من یه سر شهرم.. دوستم یه سر دیگه شهر
جفت خونه هامون لرزید
بوشهر - چهارمین انفجار «مهیب» در ۲:۵۳
برازجان (استان بوشهر) تک صدای بلند و لرزش زمین. 2:54
وحید صدای انفجار شبیه شلیک موشک برازجان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77381" target="_blank">📅 02:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77380">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c6ad0edf20.mp4?token=awzJ6Gou0vmgDeF-WanWhqD9ZDQG0t5QLYhepyWyVFfhPZZY4Tve94MltopeM4vv9QzOZytnFSiaHa-GNiPRQCrWKfP1q2x8FLVDYZfZL_dRjQcZOXaqPs7U22J9lqn_DOMn-FDB0q0x8hX9XK1Z9bwNSjH-sDcp4E5blghnfdBgaI0NzIupQuWsgEBIbhzNE9SXcwT9zLVNbF2ctvWimSI5CVrqAivQ9wTqiAOTQqQTMcdlQKNvgPgkNhBgMzNWJklQYjgbPWkJYxfJKVnQuGqIWPMhHY9MCpORI2mrg0XS9Ji3HGvZjNFosssPTcKgXxSkdXJDVWTAHA61k9-O7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c6ad0edf20.mp4?token=awzJ6Gou0vmgDeF-WanWhqD9ZDQG0t5QLYhepyWyVFfhPZZY4Tve94MltopeM4vv9QzOZytnFSiaHa-GNiPRQCrWKfP1q2x8FLVDYZfZL_dRjQcZOXaqPs7U22J9lqn_DOMn-FDB0q0x8hX9XK1Z9bwNSjH-sDcp4E5blghnfdBgaI0NzIupQuWsgEBIbhzNE9SXcwT9zLVNbF2ctvWimSI5CVrqAivQ9wTqiAOTQqQTMcdlQKNvgPgkNhBgMzNWJklQYjgbPWkJYxfJKVnQuGqIWPMhHY9MCpORI2mrg0XS9Ji3HGvZjNFosssPTcKgXxSkdXJDVWTAHA61k9-O7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
تبریز ۶/۷ تا همین الان  زدن شدید
همین الان شیش تا صدای انفجار تبریز اومد
پشت سر هم
۲:۴۲ از تبریز ۴تا صدای بلند انفجار یا پرتاب موشک اومد
سلام همین الان ۸ تا انفجار تبریز
سلام 5 انفجار شدید تبریز
سلام ساعت ۲:۴۲ بمب باران تبریز بیشتر از ۱۰ تا
۷ انفجار تبریز ۲:۴۰
از تبریز فک کنم موشک زدن
صدای انفجار از تبریز ۲:۴۲
وحید جان انفجارهای خیلی شدید اطراف تبریز ۲:۴۲ دقیقه
همین الان تبریز ۶ ۷ انفجار شدید
ساعت ۰۲:۴۲
ساعت ۲.۴۰ دقیقه تبریز رو زدن،حداقل چهار پنج تا صدای انفجار اومد
تبریز صدای ۵ انفجار توسط جنگنده بود
سلام تبریز ۴.۵ تا زدن
سلام همین الان صدای ۶انفجار سهند تبریز
ساعت ۲.۴۲
۷ تا انفجار شدید تبریز
همین الان2:43 دقیقه
پنج تا بیشتر زد تبریز رو و مشخصه سنگین بود و عجیب به مرکز شهر نزدیک
صدای انفجار از تبریز
۳ یا ۴ تا با فاصله خیلی کم
سلام وحید جان تبریز 2.43 شش هفت تا انجار وحشتناک بلند خونه لرزید و از خواب بلندم کرد
وحید تبریز ۸ تا صدای انفجار اومده
شدید و مهیب
تبریز موشک نبود. رادار رو زدن
سلام همین الان ۲:۴۲ بامداد ۶ بار سنگین زدن تبریز رو احتمالا سایت موشکی باشه
🔄
وحید دوباره تبریزو زدن
تبریز دوباره دو تا شنیدم اما دور بود صداش ضعیف میومد
دوتا انفجار دیگه تبریز ولی دورتر بود
تبریز دو تا صدا اومد
ادامه انفجارها در
#تبریز
سلام. الان تبریز پدافند کار کرد.
بازم تبریز رو زد، ۵ انفجار، شدتش کمتر از قبل بود ولی؛ ساعت ۰۳:۰۴
۵ انفجار یا بیشتر تبریز ۳:۰۴، یا شاید فعالیت پدافند ،(غرب تبریز)
تبریز بازم داره می‌زنه ساعت ۳:۰۴
۵ تا انفجار پشت سر هم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77380" target="_blank">📅 02:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77379">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان
چند تا صدای انفجار چابهار شنیده شد بنظر کنارک بود
چابهار صدا اومد.
سلام وحید جان چابهار صدا جنگنده و بمب اومد چند تا هم اومد از 2/5 شروع کرده
صدای انفجار در چابهار
چابهار همین الان چهارتا زد ساعت ۲:۳۸
چندددیقه قبلشم یکی زد
چابهار وحشتناک. داره میزنه
۷ انفجار رگباری پشت سر هم
ساعت 2:30 چهارشنبه چابهار یه صدای انفجار سنگین شنیده شد
الان دو سری 4، 5 تایی پشت هم زد
چابهار همین الآن صدای چند انفجار پشت سر هم
خود چابهار نبود
صداها دور بود
ولی تعدادش زیاد بود</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77379" target="_blank">📅 02:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77378">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بندرعباس الان سه تا پشت هم زیادد زدن
بندرعباس پشت سر هم داره میزنه
بندرعباس سلام صدای چندتا انفجار ساعت ۲:۲۷.
سلام وحید جان بندرعباس صدای 3 انفجار
سلام وحید جان همین الان  بندرعباس صدایی وحشتناک از سمت اسکله باهنر اومد ۲تا صدای وحشتناک
وحید جان دوتا انفجار پشت سرهم بندرعباس 2:38 دقیقه، دور بود
بندرعباس ۲:۳۸ چند صدای انفجار شنیدم
سلام صدای انفجار بندرعباس سه تا پشت سرهم همین الان
بندرعباس ۲:۳۷
سه انفجار
بندرعباس ۳ تا انفجار پشت هم الان
سلام آقا وحید ساعت ۲:۳۷ دقیقه بندرعباس صدای ۳ تا انفجار اومد که اولی از همه بلندتر بود
سلام بندرعباس الان صدای ۳تا انفجار شدید ۲:۳۷
سلام بندرعباس 2:37 حدودا ۴ تا صدای انفجار اومد
بندر عباس صدای ۳ انفجار ۲:۳۹
بندرعباس صدای انفجار اومد الان
میگن سمت اسکله باهنر زدن</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77378" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77377">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سلام صدای انفجار یا پرتاب موشک از کنگاور
سلام ۲ و ۳۵ صدای انفجار و لرزش کنگاور
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77377" target="_blank">📅 02:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77376">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان ماهشهر دو صدای انفجار از دور
همین الان یک انفجار دیگه
سه چهارتا انفجار ماهشهر همین الاننن
ماهشهر ۴تا موج از دور ولی حس شد
بندر ماهشهر ۴ انفجار
سه چهارتا انفجار ماهشهر همین الاننن
سلام ماهشهر الان ۳ انفجار
وحید خسته نباشی بندرماهشهر الان چند انفجار اومد
سلام صداها مثل ویبره هستن انگاردورازماهشهره به فاصله 2ذقیفه
ماهشهر صدای انفجار ساعت ۲:۳۱
🔄
اقا وحید ماهشهر دوتا دیگه زد همین الان 2.48 دقه
باز ماهشهر دوتا زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77376" target="_blank">📅 02:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77375">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پیام‌های دریافتی:
سلام خسته نباشید همین الان بهبهان رو زدن
چهار بار زدن
خیلی بد زدن
خونه ها خیلی لرزیدن
وحید
بهبهان رو زدن
۴ انفجار محکم
بهبهانو چنان داره میزنه که هبچ وقت اینجوری نزده بودددد
انفجارها انقدر قوین که تا حالا همچین چیزی ندیده بودمممم
بهبهان ۳ یا ۴ تا صدا انفجار خیلی شدید
پشت سر هم
۲:۳۲ دقیقه
خیلی شدیده
🔄
سلام بهبهان همین الان ۲ و ۳۰ بامداد ۴ انفجار بسیار سنگین
شد چهار بار دوباره اومد
بازم زد
بهبهان 4 موج انفجار 2:30
4موج انفجار نزدیک تر 2:34
۷ بار زدن بهبهان رو
سلام منصوریه بهبهان هستیم
همینجور صدای انفجار میاد پشت هم
سلام توی همین ۴ دقیقه ۸ انفجار داشتیم
همینطوری داره صدا میاد
درود وحید جان ۷ تا انفجار پیاپی و سنگین بهبهان احتمالا سمت پادگان بخردیان
دود از سمت پالایشگاه بیدبلند میاد نمیدونم کجا رو زدن
حاجی ۱۰بار زدن در خدی که زمین لرزید
بهبهان وحشتناک دارن میزنن
سلام ، تا اینجا حدود ۹ صدای انفجار اومده بهبهان
از ۲:۳۲ تا ۲:۳۵
بهبهان ۲:۳۵
صدای ۶ انفجار
همین الان بههبهان زدن صداش خیلی بلند از استرس تو کوچه ایم
سلام سپاه روبروی بیدبلند بهبهان رو حدود هفت بار زد
سلام صدای های مهیب موشک در آسمان بهبهان
شایدم انفجار
بهبهان درب خونه ها از موج انفجار چند بار لرزی از خواب بیدار شدیم وحشتناک
🔄
پیام‌های حدود ساعت ۲:۵۰
بهبهان بازم صدا انفجار
قطع نمیشه
خیلی شدیده
حاجی هنوز صدای انفجار میاد
بهبهان بازم صدای انفجار میاد
۴ تا پشت هم
بهبهان دوباره داره صدا مياد، 4 بار
دوباره دارن میزنن
بهبهان دوباره زد
۴ تا انفجار
۴ بار دیگه الان بهبهان رو زدن آقا وحید
۳ انفجار بزرگ دیگه همین الان
داداش وحید سه موج بخردیان بهبهان رو زدن
۲:۳۰
۲:۳۵
۲:۵۰
همین الان بهبهان،جدای از اون ۸ تا الان ۳ تا دیگه شدیییید زد
ساعت ۲:۵۰
بهبهان دوباره دوتا انفجار شدید
ساعت ۰۲:۴۹..دوباره ۳ انفجار شدید دیگه بهبهان.
سلام رگباری دارن بهبهان رو میزنن
بهبهان تا الان 11 تا انفجار شده وحید
وحید جان از ساعت ۲:۳۲ تا ۲:۴۷ دقیقه صدای ۱۰ انفجار داخل بهبهان اومد
سلام وحید 2و50دیقه دوباره 2انفجار  بهبهان زدن انفجار خیلی مهیبه
باز هم همونجا رو حدود چهار بار دیگه زد بیست کیلومتری شهر هستش
بهبهان پونزده بار تا حالا زدن همین الان صدا ۵ انفجار دیگه اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77375" target="_blank">📅 02:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77374">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">در بخشی از نارمک تهران صدایی شنیده شده که معلوم نیست مربوط به چی بوده.
پیام‌های دریافتی خیلی کم:
سلام شرق نارمک صدای خیلی بلند مثل انفجار
من سمت نارمکم الان یه صدایی شبیه به انفجار پهپاد شنیدم
شرق تهران نارمک شیشه ها لرزید و صدای انفجار
تهران الان صدا اومد فکر کنم زدن
ساعت 02:01
سمت نارمک ساعت ۲بامداد صدای انفجار اومد
سمت نارمک صدایی شبیه به انفجار  بود ساعت ۲:۰۰
ما هم شنیدیم ولی انفجار نبود یه صدایی مثل زمانی که پدافند می زدن
🔄
پیام‌های تازه:
انفجار گاز بوده
سلام انفجار گاز بوده میدان ۹۵
انفجار نشنیدم اما ده دقیقه پیش صدای آتش‌نشانی اومد تعداد زیاد
نزدیک نارمکیم، گلبرگ
نارمک میدان ۹۵ کوچه مهدی
ظاهرا ترکیدگی گازه
کسی صدمه ندیده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/77374" target="_blank">📅 02:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77373">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7gXjOyquLos38ruNbdj94qiZ6ygEHzPS44tzAAt1dNBEqo5XNufFMjAiTNFNaCq8u0Q5fblvPyblVI3PtrMCH344rJUYEivHuHmcbJmaOPkistH6VyaYB2mjC2GV6-2MNjeSsPHxYdW57cTh7j7QHNEyqTkm-pdDAwSsOt42XOkU6WP5NPMZpByYU1G6mv0XBLt5YdlnXhGHux6KJtSjTNn03zfR1llIyskA0AqyElB4_LqYWLRlZIOI-ZxxqU2zgf787aOSHVaO-NLYBSEOTk0zk-ta1EUpju0nat3N8Br6a-_BSneAX8n2D9DssqX6ozPvtQD7X7Kei5RMuWGSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد کل ارتش کویت، بامداد چهارشنبه، با صدور بیانیه‌ای اعلام کرد که پدافند هوایی این کشور در حال حاضر در حال مقابله با حملات پهپادهای متخاصم در پی «تجاوز گستاخانه ایران» است و تصریح کرد صدای انفجارهای شنیده‌شده ناشی از رهگیری این اهداف توسط سامانه‌های دفاع جوی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77373" target="_blank">📅 01:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77372">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">منابع حکومتی:
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): تعرض به مراکز هسته‌ای ایران، پاسخ گسترده نیروهای مسلح را درپی دارد
🔹
آمریکای جنایتکار مراکز هسته ای و حساس ایران اسلامی را تهدید به حمله نموده است. اعلام می‌گردد چنانچه ارتش متجاوز و تروریست آن کشور وارد چنین مرحله ای بشود، آن را به‌عنوان توسعه جنگ در منطقه می‌دانیم و همه منافع آمریکا، هم پیمانان و حامیان آن کشور یاغی و شرور، هدف هجوم قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار خواهند گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77372" target="_blank">📅 00:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77371">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_aQAFIOZuLQjjZvpBl58nkfhd6AXMBR911P8r7Ra-6LYmSuHkSxFGdBlnOPOwHsIoN8kKw7Uq8L5AGBx3NFBMKsCYtpcxNhgyfEa79eNuXZIxLDDLRDkbyUJtzLFMn_1mT3S-l2jfV4yNJuFfGBvvHG8OFShrMDmjHOZVjDMSbtQD9Wqb5dlIwyZV_TWfQjSexeuLxFzaIMXuxsH3aT-Yj3yhZGpOIHhqqz-kilwWOHdeGApDoOEtlBukmecDKxPplaJxpKaahxt6SoKc_Bo9-5RHYFX7Snpqgtv29LRrRvm8S0zp3d-zk5bFCl4W28bZeYIcA232-U4o4r0QWSSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع ایالات متحده می‌گوید جنگ با ایران تاکنون ۳۷ میلیارد و پانصد میلیون دلار هزینه داشته است.
پیت هگست این موضوع را خطاب به اعضای کنگره اعلام کرد؛ آماری که از افزایش نزدیک به ۸ میلیارد دلاری هزینۀ جنگ، نسبت به ارقام قبلی که دو ماه پیش اعلام شده بود، حکایت دارد.
وزیر دفاع آمریکا البته تأکید کرد که این رقم تازه، هزینه‌های پیش‌بینی‌شده تا پایان سال مالی جاری، یعنی ۳۰ سپتامبر مطابق با ۸ مهرماه ۱۴۰۵ را هم شامل می‌شود.
از زمان آغاز مجدد درگیری‌ها بین ایران و آمریکا، این نخستین بار است که پیت هگست وزیر دفاع ایالات متحده به همراه ژنرال دن کِین رئیس ستاد مشترک نیروهای مسلح این کشور، با حضور در کمیتۀ تخصصی کنگره، ویژۀ تخصیص بودجه، به سوالات اعضا پاسخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/77371" target="_blank">📅 00:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77370">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T03L50STKC-rGhyNPXSdGaLy6VWPstKpWHDYomy82ao0jSoiAs7_4D5fNHmjqEoB7dzLr3ymwcGpV1GMcmUp6P5NaS1W7XqTBSS2DP0v-eNmkYttVLCIBsOI1pfGWioVpkgJfGzqJRWOQaqRzWrjLLeHC2DPOYZbXyvBAmTMGEiqsm6myGY2JUpQ7Fy5jbARf3wrNs9c2GFH4WXRGkTLRjZaWXXOsMg3ytbwCN1xLvyW15_L1J5ESgMuUMovSspAC8q0VkAQ5vcK86oP-0gneiIa0s2UJ6_FdQ9vDhB9JVAyjsV-K1u0XU0oe-epGkaXaNbBw4VsZi_3V8obgzGdRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
جنگ افغانستان: 20 سال، 2,000 کشته.
جنگ عراق: 9 سال، 4,600 کشته.
جنگ ویتنام: 19 سال و 5 ماه، 58,220 کشته.
جنگ کره: 3 سال و 1 ماه، 36,574 کشته.
جنگ ونزوئلا: 1 روز، بدون کشته.
درگیری نظامی با ایران: 4 ماه، 18 کشته.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77370" target="_blank">📅 23:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77369">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5abf96fd5e.mp4?token=O5axC5QHnNDmo3iH6HmW3K7_qTor6y4htTW8nOWkeOuMwd5sFyOlC4jKAyz7zoUiQRnRUWCAxwQ3rDTrMD_-BU64EWNFiXNmkLNcs8WCknwUfDcc2-4rwD330nzltMke8ZlE6uaXnL6m098zq5uvZlvIYjGHVWPYD0sBECbR9S3l9rmCVAzE7WJO-UIuEqUVLK9HVLINX7DG2un9tl8q28U1JBgKBsFNqfx_bC75RFk3ecLLDWC2qJ2SqXtN1R4AVCcmNoyMtxmWgGmEQ-_Xh646dI5KkjTcTeCVu6gSkky0GKwDxcYtW27F9cmTH-WZkISRBTl24I9lzsqZz1wWkA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5abf96fd5e.mp4?token=O5axC5QHnNDmo3iH6HmW3K7_qTor6y4htTW8nOWkeOuMwd5sFyOlC4jKAyz7zoUiQRnRUWCAxwQ3rDTrMD_-BU64EWNFiXNmkLNcs8WCknwUfDcc2-4rwD330nzltMke8ZlE6uaXnL6m098zq5uvZlvIYjGHVWPYD0sBECbR9S3l9rmCVAzE7WJO-UIuEqUVLK9HVLINX7DG2un9tl8q28U1JBgKBsFNqfx_bC75RFk3ecLLDWC2qJ2SqXtN1R4AVCcmNoyMtxmWgGmEQ-_Xh646dI5KkjTcTeCVu6gSkky0GKwDxcYtW27F9cmTH-WZkISRBTl24I9lzsqZz1wWkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز، ترجمه ماشین:
خبر فوری: معترضان چندین بار جلسه ادای شهادت پیت هگست، وزیر جنگ، در برابر مجلس سنا را مختل کردند و پلاکاردهایی با نوشته «نه به جنگ با ایران» در دست گرفتند.
صدای یکی از معترضان شنیده شد که فریاد می‌زد: «دست‌هایت به خون آلوده است.»
پلیس کنگره هر چهار معترض را از جلسه بیرون برد.
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77369" target="_blank">📅 23:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77368">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MY_rTb0Sd9ETUweedTtT-etuYyYJuiFaRXlDoJ4hXSGozDu5j7f4eNY1fjlkp4bYrzntmxtfSzoIvc983oxsdUqArZVi-78vPXNgl3H0jbhufgy-0B4NsSDTuj8F6cNyDyggePbgK76mQ53HnqvUz5DceeCHSJ-SP2tRdJj6EnoEIHA2JthwU56VQuVt4gEGnPXHKz_4UFpihBuh0psXt9zVONBMrfjPkoLR0NG-OljAH0D05-A7x_HLnFdRXaXT4Tu8w6vGf1AY4Oj0yej1O3ECQGa9n4fGTiq3Y10jPQVL794PyzSQq7IOp4HPam2g5cywJdhoQxXFO4u76RLPJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ روز سه‌شنبه ۳۰ تیرماه گزارش داد اندی برنهام، نخست‌وزیر جدید بریتانیا، با استفاده ایالات متحده از پایگاه‌های نظامی بریتانیا برای آنچه لندن «حملات دفاعی» علیه ایران می‌نامد موافقت کرده و بدین ترتیب سیاست سلف خود، کی‌یر استارمر، را ادامه داده است.
این خبرگزاری به نقل از منابع آگاه نوشته که استارمر روز ۲۶ تیرماه نشستی با وزرا و مقام‌های ارشد برگزار کرد تا سیاست بریتانیا پس از ازسرگیری عملیات آمریکا در اوایل این ماه بررسی شود.
این منابع افزودند که در آن نشست، وزرا تصمیم گرفتند سیاست موجود ادامه یابد.
بر اساس این سیاست، پایگاه دیه‌گو گارسیا در اقیانوس هند و پایگاه هوایی «آراف فیرفورد» در گلاسترشر انگلستان می‌توانند در اختیار هواپیماهای آمریکایی قرار گیرند که مأموریت‌هایی برای مقابله با تهدید موشکی ایران و نیز اهداف مرتبط با تنگه هرمز انجام می‌دهند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/77368" target="_blank">📅 22:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77367">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vs-MK__46RkPV1qqm2Uo7ye37E-25pJ6WaNJtUvKi-eNvKLcL0pnt51epz1lsn2BjpnOoscoX8FgZoTAzVFck5g98dJuwYrjBdl0nLmy5SppaWrN3tOqX_aCZ9VSmKNbI6d2dwVFIktg0ny_G5czm67R-D2JvYUEh89PtgOeSn36RFw_akBd0PZx841z7EvEkip3nqadfynOObTYlk57fJdwtPJxGAR00YoPDmA-JZqhMBjwMJKawLz6PLvz_ulzWGgIRHx0hGDccLpwMyjqjJcQAX7qON6oh3Zkl5rW1TzmeW3VGvPDL8jBQFXhF4yVUGya9pC1xNwlFcTxphEOyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیته دفاع پارلمان بلغارستان روز سه‌شنبه ۳۰ تیر با طرح دولت برای استقرار موقت هواپیماهای سوخت‌رسان و نیروهای نظامی آمریکا در پایگاه هوایی بزمِر موافقت کرد؛ اقدامی که با هشدار جمهوری اسلامی به صوفیه همراه شد.
بر اساس گزارش خبرگزاری رسمی بلغارستان، کمیته دفاع پارلمان از پیش‌نویس مصوبه شورای وزیران حمایت کرد که بر اساس آن، حداکثر هشت فروند هواپیمای سوخت‌رسان آمریکایی و ۲۵۰ نیروی نظامی این کشور می‌توانند به طور موقت در پایگاه هوایی بزمِر در جنوب شرقی بلغارستان مستقر شوند تا از عملیات آمریکا در خاورمیانه پشتیبانی کنند.
بر اساس این گزارش، آمریکا درخواست کرده است این استقرار از ۲۴ ژوییه تا اول اکتبر ادامه داشته باشد.
فرماندهی مرکزی آمریکا، سنتکام، در پاسخ به پرسش شبکه سی‌ان‌ان درباره این استقرار اعلام کرد: «به دلایل امنیت عملیاتی، درباره جابه‌جایی نیروها یا آرایش احتمالی نیروها در آینده اظهار نظر نمی‌کنیم.»
ساعاتی پیش، جمهوری اسلامی به دولت بلغارستان هشدار داد از خاک یا تاسیسات خود برای حمایت از عملیات نظامی آمریکا علیه ایران استفاده نکند.
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی، گفت هرگونه مشارکت در برنامه‌ریزی یا اجرای چنین عملیاتی به منزله همدستی در «جنایت تجاوز و جنایت‌های جنگی» خواهد بود. او همچنین از پارلمان بلغارستان خواست با این طرح مخالفت کند.
بلغارستان که از اعضای ناتو است، بر اساس توافق‌نامه همکاری دفاعی دوجانبه با آمریکا که در سال ۲۰۰۶ امضا شد، پایگاه هوایی بزمِر را به عنوان یک تاسیسات مشترک در اختیار نیروهای مسلح دو کشور قرار داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/77367" target="_blank">📅 21:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77361">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N_gXLLGBwtmfUHcHcSgr201K61nhJ8rnXIKoSBU7FonUkZ8vTFg-tSuR98H1f3mq7CH6b1mGhOaHfpwnHYJmdDmlGRx7nVPnlwLMbJ1KEI2jTp6_9tQC_zZa0TOFXjOTqFUMsxPZZ2BoU7WhnwTXzK37bc2VDJmL4eCnFmX3s1UasifAaOchvoHjDqFqho4jW3INOuQfA1ts5Ev0ne939pjtt8UYiC8lzYwrUf6sOYw-uFaY9eSbFECo0p2J57D3YYagHFomylMMqoTKPzKtJDcosarckIBscieTMfgmIT5bGMXqdzpmu81ruE8qtC2qkFHdy76TkYNyS3KlCXiv3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gt2rMpJsz3eLY56xSvkAGkN-lIepuTQWkjJitkxCwSwJup5nTpJaz37-KMQ4vQ8o6VbA8iLVKZBOoXJK3ImsbSsKqg7gUg9F1o2YqIEG4-1-dJUglKA8AYhhfzrnobScNZjx5DAoutXzX_BoAN5V4rW-bMCZiyCQYnzUook6axr3PAkf6GVRbfnjOr5UtCwwraXNdrS1xMk7s_p6thc43cKjhFkcCZhOB-quVfpiAweiXamlXUKnm4iI-VAJ3jWNRL2bg1F90EaFBLL7NBfJVWcvYEwVU3QBY1S6IbBj6E3WHY642z0MrAm6cx92i2FQWAJ_QsDTY-G5RUJ0JsNzbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JrG5J2cGGhLxqObCGT3AxjPo3r3HFcOospbMI08Qo1yhtOcbKRdI-pB6_p2ymZdzjZDIdNTD7H0mi4g1sym70cxLCWksb3eYWdB0Orqc07uvyDZDRTxk4fLLN0kKlzBxEIZ98GGC0r7_g5jSDlkuECdxcSB04j7WvLsYINVOmx0pLxB0clqzXlsBxGlyWdgMS3TkdJY1gRCuWAtW-_I0nb8BZ95oQ3rP17YVw5ZNoExWf_ZmQsIz1JNwgopGz8IoLkQ4zr_B7L3UyvXIPlKyOgVYHNiPVvozM3L01S9tIEL1BZAZbuBv1IkROSdm57QbB_2ZfcP1JNLbMVAJ3YdAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pg9ODgU9PQ_6z8o1WWtrWNAZfGNZVs6PlTLlwSdx9Xpduplvxb42N78crWTjjZELing9XWH9uTBfumFWLCvwKZnQ9-wHmeDtsk3rVgrI4Dc3xrDw5mjZSuNwGpKwOhegXVOxmnF_qY5cdCBmBNzOGOy8C2G4Ewjc_QoqM2Vbzz8msfhOEcslCmkbSqBHh4RSWQZ6eJ3VUfjt7kF89C1zuj7u4OXmYaqLMvVKFqSjq723ech69jFh7pKyTbAc5vYiOUjVERwdvnDZRuUepa-cBTkbODVVyGJJjf8GWPOAsaPIpZRsOwhH3BLRsNaKmfkWyX5rlUGCKpPWrvqrTdA_pQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4477673f76.mp4?token=O6vFSFR_UeeBhVXTK_7FT4dJXPUUMTBhx4CnAIcPK0K8CPYes6O2eJVZN-fo9qSV3RuYKZMn4XluRwgT01Aq_jKc_tjyxCGgTCj7qQ047Et_Cs_Tx0kMJyL0CZWXCjUMD-X83_qtIHyUMNTBGjLVFreya2E553oDRMEJt6TAHbn7ql6WLETwg0ECGy2bUTQ-GiDeN1PTKmEg7z_BAH8AOvoiqf4niytiWYVo7YBqwALC4IjCL7-rzWB3Osk8eYMT4v8CYaLIJFPdDF9djy34J1e8NHzKbxgWvRvrdT9CskXgUcX6p2RMlO6FPDOTapL9f83jrw1A0gMN3SEzL6pp3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4477673f76.mp4?token=O6vFSFR_UeeBhVXTK_7FT4dJXPUUMTBhx4CnAIcPK0K8CPYes6O2eJVZN-fo9qSV3RuYKZMn4XluRwgT01Aq_jKc_tjyxCGgTCj7qQ047Et_Cs_Tx0kMJyL0CZWXCjUMD-X83_qtIHyUMNTBGjLVFreya2E553oDRMEJt6TAHbn7ql6WLETwg0ECGy2bUTQ-GiDeN1PTKmEg7z_BAH8AOvoiqf4niytiWYVo7YBqwALC4IjCL7-rzWB3Osk8eYMT4v8CYaLIJFPdDF9djy34J1e8NHzKbxgWvRvrdT9CskXgUcX6p2RMlO6FPDOTapL9f83jrw1A0gMN3SEzL6pp3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی  در شیراز
دو تصویر اول منتشر شده در سایر منابع
سایر تصاویر دریافتی از شهروندان،
سه‌شنبه ۳۰ تیر
گویا تصاویر بالا دو نقطه مختلف شیراز رو نشون میدن: کوه دراک و کوه نزدیک دروازه قرآن
آپدیت:
به گزارش رسانه‌های ایران عصر امروز سه‌شنبه(۳۰ تیرماه) آتش‌سوزی گسترده در ارتفاعات دراک شیراز رخ داده است که همچنان ادامه دارد.
خبرگزاری ایرنا گزارش داده است که شعله‌های آتش، مراتع ارتفاعات دراک در شمال‌غرب شیراز و کوه‌های نزدیک به دروازه‌ قرآن را در بر گرفته است و «زبانه‌های این آتش‌ از نقاط مختلف شهر به وضوح قابل مشاهده است.»
رئیس سازمان آتش‌نشانی شیراز گفته است: «۵۰ آتش‌نشان به همراه دو تیم تخصصی کوهستان در حال تلاش برای مهار حریق هستند.»
هادی عیدی‌پور به خبرگزاری مهر گفته است: «به دلیل صعب‌العبور بودن منطقه کوهستانی، وزش باد و وجود پوشش گیاهی خشک که موجب گسترش و شعله‌ور شدن آتش می‌شود، عملیات مهار حریق با دشواری همراه است.»
دلیل این آتش‌سوزی هنور اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/77361" target="_blank">📅 21:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77360">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf4d005f22.mp4?token=CMw1c-W4-kFXxun1RNps-3LlxFzosT_Gc1ejQcnFkR6qYE-yVVZLT855wTvlu145eRgYYE3JnlmYea3bUPSCWyGN8dm_XHn0khd8tvj0NIg70_RcZWd4iCqiilbUP7BG00T0Hilxh95dOq7_-c2IuVzzmxcGNmh1digUOBgUDFfn1HF_iprkZla5vXLKDAEXLk_UdyWiA3xZCP1d_AD33lUDlnb-fI5BQ_-8Oglze1Opifj6Ye9kyEnAlONNiXQjA_-vct2vJTbJXFM9bZqeU921JXJEI_KhRG0KHcQwDa-5Q6wCiunGa_p-sbZXxrHPW3LWWcbIwo9HeZDbrBXaQDEyGs6MXS8NZ0QAirFsI0HpJRqex13wTkrHGxdPAINsiV3wwkFLuDfPv75zH1tgaIJ4e55lq3E9BUL0N7niWrIPTDQC7REUZ43tAZ-fXBNvBKOtlpYFIPqQWCIzDw0QxdlkbsY63frJcQBd761QwpEQvUuxjJBoXwZlibGwv8IA8B3Gru_ZgqKhdbkfN50DIWRcQA4g5qfiNKMMOspcJjCSlB_pQPJiibhTTASEQLDtbTD51icnZgzNsDnla5ZLgnNy93n2JWNL9Yi08KESBJmhs8gWuXkYImS44XHtuS2WhdoZ8Xp2LR9BTneHT_N4s7RC2O6uaNLUQJUyRtbUXQI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf4d005f22.mp4?token=CMw1c-W4-kFXxun1RNps-3LlxFzosT_Gc1ejQcnFkR6qYE-yVVZLT855wTvlu145eRgYYE3JnlmYea3bUPSCWyGN8dm_XHn0khd8tvj0NIg70_RcZWd4iCqiilbUP7BG00T0Hilxh95dOq7_-c2IuVzzmxcGNmh1digUOBgUDFfn1HF_iprkZla5vXLKDAEXLk_UdyWiA3xZCP1d_AD33lUDlnb-fI5BQ_-8Oglze1Opifj6Ye9kyEnAlONNiXQjA_-vct2vJTbJXFM9bZqeU921JXJEI_KhRG0KHcQwDa-5Q6wCiunGa_p-sbZXxrHPW3LWWcbIwo9HeZDbrBXaQDEyGs6MXS8NZ0QAirFsI0HpJRqex13wTkrHGxdPAINsiV3wwkFLuDfPv75zH1tgaIJ4e55lq3E9BUL0N7niWrIPTDQC7REUZ43tAZ-fXBNvBKOtlpYFIPqQWCIzDw0QxdlkbsY63frJcQBd761QwpEQvUuxjJBoXwZlibGwv8IA8B3Gru_ZgqKhdbkfN50DIWRcQA4g5qfiNKMMOspcJjCSlB_pQPJiibhTTASEQLDtbTD51icnZgzNsDnla5ZLgnNy93n2JWNL9Yi08KESBJmhs8gWuXkYImS44XHtuS2WhdoZ8Xp2LR9BTneHT_N4s7RC2O6uaNLUQJUyRtbUXQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: به زودی «کوه کلنگ گزلا» در نزدیکی نطنز را هدف حمله‌ای شدید قرار خواهد داد
06:33
دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۳۰ تیر در دیدار با جوزف عون، رییس‌جمهوری لبنان، گفت جمهوری اسلامی با «درماندگی» به دنبال مذاکره برای پایان دادن به جنگ است و هشدار داد آمریکا به‌زودی «کوه کلنگ گزلا» در نزدیکی نطنز را هدف حمله‌ای شدید قرار خواهد داد.
@
VahidHeadline
رئیس جمهور آمریکا در پاسخ به این سوال که آیا ممکن است ایران سانتریفوژهای خود را به داخل تاسیسات کوه کلنگ منتقل کرده باشد، گفت:
«ممکن است کرده باشند ... ما اطلاعات مستندی نداریم ما فقط در اخبار جعلی این چیزها را می شنویم. اما سانتریفوژ بدون مواد هسته‌ای اهمیتی ندارد. ما مواد هسته‌ای را دنبال می‌کنیم که اصل قضیه است. آنجا را می‌زنیم، احتمالا خیلی زود. معمولا این چیزها را اعلام نمی‌کنم. اگر فکر می‌کردم می‌توانند جلویمان را بگیرند نمی‌گفتم.»
@
VahidHeadline
ویدیوی بالا: قطعات مربوط به ایران به تشخیص ماشین
متن زیرنویس ویدیوی بالا (ترجمه ماشین
)
تیترهای پیشنهادی چت جی‌پی‌تی درباره متن زیرنویس ویدیوی بالا:
▪️
ترامپ: ایران عاجزانه خواهان مذاکره است؛ هر تأسیسات هسته‌ای تازه را به‌شدت هدف قرار می‌دهیم
▪️
ترامپ: اگر امروز هم خارج شویم، بازسازی توان ایران ۲۰ تا ۲۵ سال طول می‌کشد
▪️
ترامپ: ایران هنوز چیزی ندیده؛ به هر محل فعالیت هسته‌ای حمله خواهیم کرد
▪️
ترامپ: محاصره ایران مانند دیوار فولادی است؛ هیچ‌کس عبور نمی‌کند
▪️
ترامپ: ایران سلاح هسته‌ای نخواهد داشت؛ برای حملات سنگین‌تر آماده‌ایم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/77360" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77359">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5ebdb6d740.mp4?token=TbPgMJKuUFkOvEQWzEklV6MYobKehcPWNuBbk_tqs9O57jKi_Ar14czbwAgwCFfSs-WD3FwK0WKCoutzN9o3x1ITBL05ZZzZOFPOkqvTwZXKV8MSKaiejoeHIhSBKoxIDzCwv-exRQ7_0uxUfcU6foYVkBU8pdbL1wy-K2WvNGBktNNpaazzPuRMl7G7e4VY368qR761M-q_lQTv6S2k50y-909KUahnM1w9y9j46o7OTrdKMKD2zPmnf4lOXFl7e_gduoGYAYI4jFIQ-ht26a-HLcj6eoxDGSr-LnJRBRVZkCh59VI29XmP3K6ee1wSBer0rPpLGt9CVVwHSy4XbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5ebdb6d740.mp4?token=TbPgMJKuUFkOvEQWzEklV6MYobKehcPWNuBbk_tqs9O57jKi_Ar14czbwAgwCFfSs-WD3FwK0WKCoutzN9o3x1ITBL05ZZzZOFPOkqvTwZXKV8MSKaiejoeHIhSBKoxIDzCwv-exRQ7_0uxUfcU6foYVkBU8pdbL1wy-K2WvNGBktNNpaazzPuRMl7G7e4VY368qR761M-q_lQTv6S2k50y-909KUahnM1w9y9j46o7OTrdKMKD2zPmnf4lOXFl7e_gduoGYAYI4jFIQ-ht26a-HLcj6eoxDGSr-LnJRBRVZkCh59VI29XmP3K6ee1wSBer0rPpLGt9CVVwHSy4XbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، روز سه‌شنبه ۳۰ تیرماه در یک مراسم عمومی با بیان این‌که «سطح دسترسی» به مجتبی خامنه‌ای افزایش یافته، گفت تمام اقدامات مربوط به مذاکره «بر اساس رهنمودهای» رهبر جمهوری اسلامی انجام شده و از «اظهارنظرهای نادرست و بی‌توجه به ابعاد مختلف» در این باره انتقاد کرد.
مجتبی خامنه‌ای حدود ۱۰ روز پس از کشته شدن پدرش در نهم اسفند ۱۴۰۴ به‌عنوان رهبر جمهوری اسلامی معرفی شد، اما از آن زمان نه تنها هیچ فایل تصویری که هیچ فایل صوتی هم از او منتشر نشده است.
عباس عراقچی، وزیر خارجه ایران، به‌تازگی اعلام کرده که «هیچ‌وقت» مجتبی خامنه‌ای را از نزدیک ندیده و در دورهٔ رهبری او نیز جز معدودی او را ندیده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/77359" target="_blank">📅 18:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77358">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjHIkY_AAAd_eMjxcSgDZNjJtsUAU0YrX3a3o4_2SF7h4Tfj7mbiKoyFM6Cr2ZfflZ6kgs2LsFyjnxwoGiEN_y7QJgGxaFH-gGCTx8NrjY1yUtA8JpmJ3dlrJg4-hPLV_K25FT8ydlvcezy3AXzh7CFjF3OKr7QtQJeWPW5NFhoxR78zGNvDf_WYzR-7pqZhNjhRPcg4Bs6c_pKoayLW8y5W6KTdtns6mWpmcU8fS8fWDj9vMIKKEZVqCL9RV7fEnE4z1mghJzWQXqUNcNhTAYEqBZKhDKxzNljo_h_ES9JQDa7wMrHBrqbyHgatM2gHMs_Z4eBGDEB007XrleSE7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، «شیده توکلی»، شهروند بهایی ساکن تهران، را به ۱۱ سال حبس تعزیری، جریمه نقدی، محرومیت دائم از اشتغال در خدمات عمومی و دولتی و مصادره بخشی از اموالش محکوم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77358" target="_blank">📅 18:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77357">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad05dc08a.mp4?token=F_u1CvMbrJKBZsG2MEBkKH7EcKd5zZfEFadLGXYbnbaQaPPr8XzmEdLrIOzz8c5V1EKTE5D4pUBjnD5hCJuQLPiwX-wxoJqnRKfHpmPTY37Blchx40rM_BmpW00foWDD3e6dY668kuHRkWFc1LmrqoGA6Cr0hn72c5_j4xRJrf3Oiw5JjOKwflYuTpO34RPf97M5VJvCTqx_CmQfniX8dUSYGWQvE_vLfQqSumlY9v_IDNL7jj2oVp9nmaSGUCnMYnaMzwVVigjRVFIOJ9E41bljLVms4-SxL2tMddEIitC6v947IBbeqxVy-6PAjPa_ntTTtCv2QTQMEitxM95wUTg9PPsbd8Oo41xIDwxn1dOs2FV1DyQmYeQSCYHVVARTRpx9BvzsIEmtjEpHQQjWo8mDjU7c8mFepS1L4ehDDbFWDJrAj-_djQ4BX69fPPMmAHZIvjNLjRroilDsGbTREolI-cWgxLnLgoGDcvo0xfXFVKcPGfS72f3JUNx_ySpM5MYJuW_FTl57GfdTM8Ba3a1PjnzLmGTvAAEUiCBmNzrR2-gy9AicYLk1-_mwIdYtrsQDlriUE7UDKtiC5x8O6IrR5hC7hiQ-57OZwFftL2Bif5w10hhH50cQxQ1m8aitvl8XWbonooPiMkr4ml9UH_wmkxLOkBIudUZhFicidrY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad05dc08a.mp4?token=F_u1CvMbrJKBZsG2MEBkKH7EcKd5zZfEFadLGXYbnbaQaPPr8XzmEdLrIOzz8c5V1EKTE5D4pUBjnD5hCJuQLPiwX-wxoJqnRKfHpmPTY37Blchx40rM_BmpW00foWDD3e6dY668kuHRkWFc1LmrqoGA6Cr0hn72c5_j4xRJrf3Oiw5JjOKwflYuTpO34RPf97M5VJvCTqx_CmQfniX8dUSYGWQvE_vLfQqSumlY9v_IDNL7jj2oVp9nmaSGUCnMYnaMzwVVigjRVFIOJ9E41bljLVms4-SxL2tMddEIitC6v947IBbeqxVy-6PAjPa_ntTTtCv2QTQMEitxM95wUTg9PPsbd8Oo41xIDwxn1dOs2FV1DyQmYeQSCYHVVARTRpx9BvzsIEmtjEpHQQjWo8mDjU7c8mFepS1L4ehDDbFWDJrAj-_djQ4BX69fPPMmAHZIvjNLjRroilDsGbTREolI-cWgxLnLgoGDcvo0xfXFVKcPGfS72f3JUNx_ySpM5MYJuW_FTl57GfdTM8Ba3a1PjnzLmGTvAAEUiCBmNzrR2-gy9AicYLk1-_mwIdYtrsQDlriUE7UDKtiC5x8O6IrR5hC7hiQ-57OZwFftL2Bif5w10hhH50cQxQ1m8aitvl8XWbonooPiMkr4ml9UH_wmkxLOkBIudUZhFicidrY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بنیاد عبدالرحمن برومند  از ابتدای سال ۲۰۲۶ تاکنون اعدام دست‌کم ۸۵۱ نفر در ایران مستند کرده است که ۳۲ مورد آن تنها در ماه ژوئیه انجام شده است.
🔸
بر اساس قوانین بین‌المللی، مجازات اعدام تنها به «شدیدترین جرایم» — که به معنای قتل عمد تفسیر می‌شود — محدود شده است؛ با این حال در ایران، جرایم غیر خشن مرتبط با مواد مخدر، بیشترین سهم را در آمارهای اعدام با این‌گونه اتهامات دارند.
🔸
طبق داده‌های گردآوری‌شده توسط بنیاد عبدالرحمن برومند، نزدیک به ۴۵ درصد (۲,۹۴۶ مورد) از کل اعدام‌های ثبت‌شده در بازه ۱۰ ساله ۲۰۱۶ تا ۲۰۲۵، مربوط به اتهامات منتسب به مواد مخدر بوده است.
🔸
سوءاستفاده حکومت ایران از مجازات اعدام به حدی وخیم شده که زندانیان واحد دو زندان قزل‌حصار ، بزرگ‌ترین زندان دولتی ایران برای دومین بار در سال جاری دست به اعتصاب غذا زده‌اند و حتی برخی از آن‌ها لب‌های خود را دوخته‌اند. با گذشت هشت روز از آغاز این اعتصاب، هیچ‌یک از مسئولان پاسخگوی وضعیت آنان نبوده و به خواسته‌های اعتصاب آنها توجه نکرده‌اند.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77357" target="_blank">📅 18:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77353">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gS-m1-cb9ZVwJI_CmFD1NARnoVUq5s85rXtLAM4lDVGd8lK0Ui_pOO8rxN9aOAr1iC2zUhiOTwXMxk7WjLp-pqBR1ICEw95J-zoD9vANPXIp0oSSfXmU11OZyOI0HnrJqYqr3URmv7r3mIJlo7iq1fd7x-rli6-61Z6JzMO_DEpWvziRCnn32Ekostlx-ojPNbK4gUmv9wRf7KxeGo6Vg5g3x1IiQlQiIum9RPFDF8ZWzkZqJ-ttwrInh9cWl03WrmbaLpB04c8p53qyHYGzV8zBeWZeZ4eT0VfLcjM8FwMpg0rEqnNBcRH1SRZov2sgbbMJJH47_BqybiQ25lmLXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EV7oyNuGIqUJhW-rh-Ph41ibXDP9SZq9TpA9sM_6jjJ3cS434Z2vTDL1WClHS_OQlykFXDwB7V17JO1oeafkmEEmueUt3XAN76gF2vVFFZAT9z_j79nuOb5-mLjV9lmTdukxpTUQiZN_rHU3e1-VYhdXalFvhIHM2MI_NAahBx_50WB4l8TUyJy9sOg1JMmGApQDUmy9bwQLFoVXSuzTSHRMMMBV1o5dn4LAhn4i6AEzI8bpiqeB3HMYIYJRRR5Xdc93n44CfUkkWR6EXi1U9YZe5nXNfy9OfLhPmBuWRKlorBTK-SJ602PJHvnafIN0ccUvxJPceqRlYGTRr8eBgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UvVX08lBySoYev95EURagEjyeh1TMG7yavU1OlZwQRf3GGyKkznHb-aI9fdsddcelsMImUDC3XAaQ2l75cqBkZik175wwcjIdbx14tWNJUZW_BmlAAx9VP8tn4_uNQypwxJHaJGaUywL0qU1xI1bfJbLRZaFoLjol-DpucDI17zGmjNsnooVXxyjNNKZ_MhLgYjm3o7AarQjeK7chTqvaEI-bT-b4DKzn4TgJ0XNpOJtPt0vtSZgYHmvDOmp7WnHebdlawZMeyONgA2WXmb36PzAI_0jtKNSpBMzNwgbb-AJhHwIgZ71wH1xe7btmeFK8LzjY9v0s7rvcvAlJNdsqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nmadj8WO1zVn8xT7tuzlnYueU9G3drnQG8Zv2pbk6XyMxQfUbQVWhtLX_xkvqXaf0RkYlpwSWew1PDHOGSbaoV14cJE61XpBziKvtZYkG4THzJD8WSWVV9vpVtGRD_JY8PmqPi_-QiJx0x3qTvbmWJhU1283I0kmumKXeiLOzOrVk-Mh_FEbhnP5FncmgbxAxVEYYyFCCHsIExDtTy0LiAgyx1EJjbdVbP2NoGJbXz_q54suL_aOUQ2--kfsUXf389_DmA-XnRD5SBoswMCDBCyUdWGNeTJjwtKw-WnMXUaN8fZ28ez6Ehhl9NTpTTaFtLg2KLyRU7MXZev6i6LU3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا روز سه‌شنبه ۳۰ تیر با انتشار چند پست مختلف در شبکه اجتماعی تروث‌سوشال با بازنشر تصاویر و نوشته‌هایی از دو معترض به تازگی اعدام‌شده در ایران، مقام‌های جمهوری اسلامی را «وحشی‌» خطاب کرد.
دونالد ترامپ در یکی از پیام‌هایش با انتشار تصویری از یک پیام منتشرشده در شبکهٔ اجتماعی ایکس که به اعدام گل‌محمد محمدی، یکی از معترضان پروندهٔ موسوم به «میدان علیخانی اصفهان» اشاره کرده، نوشت: «آخرین مورد از ۵۲ هزار معترض بی‌گناه، و حتی بیشتر. وحشی‌ها!!! دموکرات‌ها کی از خواب بیدار می‌شوند؟؟؟»
رئیس‌جمهور آمریکا در پیام دیگری تصویری از یک پیام منتشرشده کاربری در شبکهٔ اجتماعی ایکس را منتشر کرد که در آن در کنار تصویری از عرفان اسفندیاری، معترض ۱۹ ساله اعدام‌شده در پرونده علیخانی اصفهان، نوشته شده که «لطفاً کمک کنید. لطفا صدایشان باشید».
آقای ترامپ در پیام دیگری، تصویری از یک زن گریان را بر حاشیه‌ای از پرچم در حال سوختن جمهوری اسلامی منتشر کرد که پلاکاری با این جمله را در دست دارد: «ما را نکشید».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77353" target="_blank">📅 18:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77352">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پیام‌های زیادی از اصفهان دریافت می‌کنم درباره شنیدن شدن صدای انفجار و لرزش شیشه‌ها
پیش‌تر اعلام شده که:
صدا وسیما: صدای انفجارهای کنترل شده مرتبط با مهمات عمل‌نکرده از ساعت ۹تا ۱۶ بعدازظهر امروز در جنوب و غرب شهر اصفهان، بهارستان و محدوده‌های صفه و شهر ابریشم شنیده می شود
مردم نگران نباشند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/77352" target="_blank">📅 09:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77351">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NlITH3aXGAe2SLAmk-PBkueu1DVs9d5lr4wvE-ReipfUWcDU80AuKgKGe0BkkjmzCbX7LHwwo_hodamtDjK9i1vxVd1B0fvKMFZpsCJKqrsywjFPJjovTzo-vBxIiRzkKPUw0-jIOZVJ7KpOemFGjmL_rqiBfh7yVFbfHyjlZRZPJ88qK_x5PSv74odkuB2pBypw3jdWzsdj9VdGiunOGlnUZP3Hmp5HWq6_Q6pVvoNliuiufay3w9wlFwxBHsiG8F9eni27sDglWQTEl7Smo9QaD0ouS3pgGUR1-4CnxIz5JqpAFGOwrLBltoR3Q-hoJxvRfiiZfnmSJEkV6wk0yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای سپاه: سامانهٔ راداری دفاع موشکی و یک هواپیمای اف ۱۵ در آشیانه دشمن در اردن منهدم شد
خبرگزاری فارس:
🔹
روابط‌عمومی سپاه: ملت عظیم الشأن ایران اسلامی! با استعانت از خدای متعال، در ادامهٔ عملیات پاکسازی منطقه از رادارها و سامانه‌های پدافندی و هموارکردن مسیر حملات موشکی و پهپادی گسترده‌تر و تکمیل شب سیاه راداری دشمن آمریکایی، رزمندگان غیرتمند نیروی هوافضای سپاه در ادامهٔ موج ۲۴ عملیات نصر ۲ در حملهٔ موشکی به پایگاه آمریکایی در اردن یک سامانهٔ راداری دفاع موشکی را تخریب و یک فروند هواپیمای اف ۱۵ را در داخل آشیانه منهدم کردند.
🔹
این منطقه جای متجاوزان آمریکایی نیست، ارتش کودک کش آمریکا برای پیشگیری از تلفات بیشتر باید منطقه ما را ترک کنند.
📝
گزارش تکمیلی این عملیات تنبیهی به استحضار ملت شریف ایران خواهد رسید.
ادعای سپاه: زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون در بحرین ویران شد
خبرگزاری فارس:
روابط عمومی سپاه: با توکل به خدای قادر متعال و در هم کوبنده ستمگران، رزمندگان هوافضای سپاه در ادامه موج ۲۴ عملیات نصر ۲ در پاسخ به تجاوز و تعرض روز گذشته ارتش کودک‌کش آمریکا به تاسیسات در دست احداث و غیرنظامی دارخوئین، زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون را در بحرین با چند فروند موشک کروز مورد هجوم قرار دادند و آن را ویران نمودند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 462K · <a href="https://t.me/VahidOnline/77351" target="_blank">📅 09:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77350">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فرماندار آبدانان: آمریکا با موشک به نقطه‌ای در کوه‌های اطراف آبدانان حمله کرد
خبرگزاری جمهوری اسلامی، ایرنا:
🔹
به گفته فرماندار آبدانان، ساعتی پیش دشمن متجاوز آمریکایی با چند پرتابه مناطقی در بیرون از این شهر استان ایلام را هدف گرفت.
🔹
بهزاد نورمحمدی صبح سه‌شنبه در گفت‌وگو با خبرنگار ایرنا اظهار کرد: دشمن آمریکایی با پرتاب موشک، به نقطه‌ای غیرنظامی در کوه‌های اطراف آبدانان حمله کرد.
🔹
وی افزود: خوشبختانه این حادثه هیچ‌گونه تلفات جانی در پی نداشته و دستگاه‌های مسئول در حال بررسی ابعاد موضوع هستند.
🔹
نورمحمدی یادآور شد: دستگاه‌های امدادی به محل حادثه اعزام شده و مشغول بررسی دقیق ابعاد تجاوز دشمن هستند.
پیام‌هایی که من از یک شهروند دریافت کرده بودم از ساعت ۲:۴۱:
سلام وحید جان صدای دو انفجار اومد چند دقیقه پیش
ما آبدانان هستیم ولی صدا خیلی دور بود بیرون شهر بود.
ظهر هم رد موشک تو آسمون دیده میشد
الآنم یکی دیگه
2:49 دوباره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 457K · <a href="https://t.me/VahidOnline/77350" target="_blank">📅 06:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77349">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e6445e1dc2.mp4?token=sW7cN0H13h1Dxq60tmHXP2wYumAn2Plmwo3Ru3sjI5mSV4uSGVa2_GeiI2dIwgxUDKgiZ1Sk1bNA6UA_3009YKCaX5bTmFsM7p_mvvOGCjiAl8KpAl0cKnynpjr6HXPvNtOHJPAHWFvIsJ2L_YGcaS96ChJnC5iWwT3LWfLoO9FyGzaEwyvRMeU7PNIVTdo-rj2iiKgAP2l9pHhf_EaWsKyy6KYoNHP98wlZjV1zU317bSb2E6ce7sVtAzAt69yQvAFRgK5niqIpwE1_ZDN_lMmlFQIKw-laKlnSNcAYNj9MxzhoktjsViEcky6p3RPQkb5O3K2wBMwwbgPU8X0pcA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e6445e1dc2.mp4?token=sW7cN0H13h1Dxq60tmHXP2wYumAn2Plmwo3Ru3sjI5mSV4uSGVa2_GeiI2dIwgxUDKgiZ1Sk1bNA6UA_3009YKCaX5bTmFsM7p_mvvOGCjiAl8KpAl0cKnynpjr6HXPvNtOHJPAHWFvIsJ2L_YGcaS96ChJnC5iWwT3LWfLoO9FyGzaEwyvRMeU7PNIVTdo-rj2iiKgAP2l9pHhf_EaWsKyy6KYoNHP98wlZjV1zU317bSb2E6ce7sVtAzAt69yQvAFRgK5niqIpwE1_ZDN_lMmlFQIKw-laKlnSNcAYNj9MxzhoktjsViEcky6p3RPQkb5O3K2wBMwwbgPU8X0pcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع حکومتی با انتشار ویدیوی بالا: سه پایگاه مهم آمریکا در کویت، هدف حملات پهپادهای انهدامی ارتش قرار گرفت
مرحله نوزدهم عملیات صاعقه ارتش
روابط عمومی ارتش:
🔹
در پاسخ به شرارت‌ها و نقض عهدهای مکرر شیطان بزرگ، بامداد امروز و در مرحله نوزدهم عملیات صاعقه، ارتش جمهوری اسلامی ایران، ساختمان‌های اداری  و آنتن‌های جهت‌یاب در پایگاه عریفجان، پارکینگ گروهی بالگردها در اردوگاه العدیری و ساختمان اسقرار نیروهای ارتش تروریستی در پایگاه احمدالجابر کویت را هدف حملات پهپادهای انهدامی خود قرار داد.
🔹
پایگاه عریفجان از بزرگ‌ترین مراکز استقرار نیروها و ستاد فرماندهی نیروی زمینی آمریکا در جنوب غرب آسیا و پایگاه العدیری محل استقرار بالگردهای آپاچی، شنوک و بلک هاوک نیروهای دریایی و هوایی  آمریکا است.
🔹
پایگاه احمدالجابر نیز نقش محوری در آماد و پشتیبانی ارتش متجاوز آمریکا در غرب آسیا دارد و تاثیر عمده‌ای در عملیات‌های هوایی و نظارتی این کشور ایفا کرده است.
🔹
ارتش جمهوری اسلامی ایران اعلام کرد، امنیت منطقه در پی شرارت های نیروهای تروریستی آمریکا مختل شده و  نیروهای مسلح جمهوری اسلامی تلاش می‌کنند در نبرد با آمریکا، امنیت و آرامش را به منطقه بازگردانند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 449K · <a href="https://t.me/VahidOnline/77349" target="_blank">📅 06:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77348">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/841c527612.mp4?token=cy6zCZZgz5jCUQ1YTF4y47LVpjtGeR4vZGK24PE8oonJViGd4pNRxF2NCy4u0RDTvPikDXsG7oX7jsreaXP6_zEIAmTLau8l2JBnhsWoInxbZhpzpWTy2HSXOtPRBlj_-OrPqFgG0DDPujSP7dA3IECRPRhFse6RTriy_WT74bzn0SRjAG45aInPytPRdDQ-QgvhrcI1F9Zqb6svslZ5al72Mrx--h96-TvCOlM0uN7IHr8__e8_NBC5o3xp4doq1CpHFUYC-xWL1tRp_Dmb2tTYV8_ovoFiN56vvhwg4k6hRK8qwqq0g7wkT5eqnXD3FcQ8SM-uhVcsRBvkY_MJig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/841c527612.mp4?token=cy6zCZZgz5jCUQ1YTF4y47LVpjtGeR4vZGK24PE8oonJViGd4pNRxF2NCy4u0RDTvPikDXsG7oX7jsreaXP6_zEIAmTLau8l2JBnhsWoInxbZhpzpWTy2HSXOtPRBlj_-OrPqFgG0DDPujSP7dA3IECRPRhFse6RTriy_WT74bzn0SRjAG45aInPytPRdDQ-QgvhrcI1F9Zqb6svslZ5al72Mrx--h96-TvCOlM0uN7IHr8__e8_NBC5o3xp4doq1CpHFUYC-xWL1tRp_Dmb2tTYV8_ovoFiN56vvhwg4k6hRK8qwqq0g7wkT5eqnXD3FcQ8SM-uhVcsRBvkY_MJig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: نیروهای آمریکایی مراکز فرماندهی نظامی ایران، توانمندی‌های دریایی، محل‌های پرتاب موشک و پهپاد و سامانه‌های پدافند هوایی را هدف قرار دادند.
ترجمه ماشین:
پایان تازه‌ترین حملات آمریکا علیه ایران
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) دور دیگری از حملات علیه ایران را در ساعت ۹ شب ۲۰ ژوئیه به وقت شرق آمریکا به پایان رساند.
نیروهای آمریکایی مراکز فرماندهی نظامی ایران، توانمندی‌های دریایی، محل‌های پرتاب موشک و پهپاد و سامانه‌های پدافند هوایی را هدف قرار دادند تا توانایی ایران برای ادامه حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز را کاهش دهند.
عبور کشتی‌های تجاری از این گذرگاه حیاتی دریایی بین‌المللی همچنان ادامه دارد. از اوایل ماه مه تاکنون، نیروهای سنتکام به تسهیل عبور حدود ۹۰۰ کشتی تجاری و ۴۵۰ میلیون بشکه نفت خام کمک کرده‌اند.
نیروهای آمریکایی همچنان در موقعیت و آمادگی لازم برای پاسخگو کردن ایران به‌دلیل تجاوز بی‌دلیل علیه دریانوردان غیرنظامی که در پی عبور آزادانه و بدون مانع از این تنگه هستند، قرار دارند.
CENTCOM
اطلاعیه شماره ۳۵ سپاه:
شب سیاه رادارها و سامانه های پدافند هوایی آمریکا در منطقه
روابط عمومی سپاه:
🔹
ملت عظیم الشان و مجاهد ایران اسلامی؛ حماسه حضور در میدان و ۱۴۰ شبانه روز ایستادگی بی‌نظیر و پرشور شما چنان روحیه ای به رزمندگان اسلام و مدافعان از جان گذشته وطن بخشیده است که با لطف و امداد الهی هر روز حماسه‌ای نو خلق می کنند.
🔹
ساعاتی پیش عملیات بزرگ رزمندگان اسلام برای تنبیه ارتش کودک کش آمریکا به خاطر برهم زدن امنیت تنگه هرمز و تجاوز به نقاطی از میهن عزیزمان آغاز شد.
🔹
فرزندان شما در نیروی هوا فضای سپاه شب سیاهی برای رادارها و سامانه های پدافند هوایی آمریکا در منطقه رقم زدند و در موج ۲۴ عملیات نصر۲ با رمز مبارک یا رقیه (س)، به منظور هموار کردن راه عملیات گسترده آینده و از میان برداشتن موانع اصابت دقیق اهداف یک سامانه پدافندی و یک رادار آمریکایی در المحرق بحرین به طور کامل تخریب شد و از مدار عملیاتی خارج گردید و همچنین یک سامانه پدافند هوایی پاتریوت آمریکا در اَلرفاع بحرین هدف حمله همزمان موشکی و پهپادی قرار گرفت و نابود شد.
🔹
تنبیه متجاوز ادامه دارد و گزارش آن به استحضار شما ملت عزیز و قهرمان خواهد رسید
و ماالنصر اِلا من عند الله العزیز الحکیم
اطلاعیه شماره ۳۶ سپاه:
یک سایت راداری برد بلند، یک مرکز مخابراتی و سامانه های دریافت ماهواره ای، یک رادار دفاع موشکی و یک سوله آشیانه پهپادهای MQ9 منهدم شدند
روابط عمومی سپاه:
🔹
ملت عظیم الشان و قهرمان ایران اسلامی؛ در ادامه عملیات تنبیهی رزمندگان هوافضای سپاه و در راستای هموارسازی مسیر، برای دفع موانع عملیات هوایی و موشکی گسترده در مرحله دوم موج ۲۴ عملیات نصر۲،  امشب یک سایت راداری برد بلند، یک مرکز مخابراتی و سامانه های دریافت ماهواره ای، یک رادار دفاع موشکی ارتش کودک کش آمریکا مستقر در کویت مورد اصابت موشکی و پهپادی قرار گرفت و منهدم شد.
🔹
همچنین یک سوله آشیانه پهپادهای MQ9 نیز در پایگاه علی السالم مورد اصابت واقع و تعدادی پهپاد منهدم شده یا آسیب کلی دیدند.
🔹
عملیات تنبیهی فرزندان شما ادامه دارد. التماس دعا.
و ما النصر الا من عند الله العزیز الحکیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/77348" target="_blank">📅 04:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77347">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o3VdusX4wDEepc8LUF2OiJTs5AEEu5o4MBr0rp9dbiqwij18w5ig4JcWjfc8Dt2KUnsBmVaYjX_cbLwUmRr-G_wbAVDWQzybQDUilIOICGguAe3n11BOBUnahkxb7FH3E6n_xRQLHMnidYtV7U3RpMaWijMlTfAKQ2bSHrk7WlsL8zNFs9PX0a6GS3MR7hkcI8IB4YcNepXitR_D3nswaG4Eywe37hhszNC7spJFVX9X1RnjrRwAVwZ7TgdJF3t64wJ05vKI-shcOzD3C4Vdrs0QJqReDO-gDmxz-rGSR_8DpHt46GFA_sAlciBet9c7W5i7RApPHtaK4IrCwRjYWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
خبرنگار صداوسیما: حوالی ساعت یک بامداد در برخی نقاط شیراز صدای انفجار شنیده شد که بر اساس گزارش‌ها یک نقطه در شرق و دیگری در غرب شیراز مورد هجوم دشمن قرار گرفته است.
چند پیامی که من دریافت کرده بودم:
شیراز رو باز زدن
یجوری شیراز رو زدن که شیشه ما بدجور لرزید
سلام صدای دوباره انفجار در شیراز
شیراز دوباره زدن
خیلی بد زد
شیراز 1:21 صدای دوتا انفجار خفیف دیگه اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/77347" target="_blank">📅 03:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77346">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNuv-BHYbSxSOd6ShXHNTaK2peJsucBmhoGwxMCakJFGVnBtuHbap1_hyXUByce4SLLaknSiPMs95rUkH_QuN32YAk7U_kzR50U140ivr_9aq4T09vt5QwObz-Z-oLtjzRzkR8j_8ABf4F2514qT-5rPSp4cE6ruUnVCAKBbC9vy3ElFynzqrCT3cFsXfAsRxXxAxIxh_gcvIQImh0_lxXO-1HF1uRutCEYBqu6OIJ4K4AGbQ6U1rzBhK5-bzCaZ83K_BqOAMJIfNyyGlmGvnkQSrcLa03UhbOZB1gfICuGhm76SMVZlRAxBP_MITGu3WCUfY03aW8xzZx6tALNryQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درباره تماس با نخست‌وزیر تازه بریتانیا: درباره نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌روبی تنگه هرمز و بسیاری موضوعات دیگر گفت‌وگو کردیم.
ترجمه ماشین:
گفت‌وگوی بسیار خوبی با نخست‌وزیر جدید بریتانیا، اندی برنهام، داشتم. درباره موضوعات بسیاری گفت‌وگو کردیم، از جمله روابط فوق‌العاده‌ای که با بریتانیا داشته‌ایم.
در آینده‌ای نه‌چندان دور برای گفت‌وگو درباره موضوعات مورد علاقه مشترک دیدار خواهیم کرد. نخست‌وزیر کار بزرگی پیش رو دارد، اما قادر به انجام آن خواهد بود و البته ایالات متحده آمریکا نیز برای کمک در کنار او خواهد بود!
درباره نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌روبی تنگه هرمز و بسیاری موضوعات دیگر گفت‌وگو کردیم.
این تماس جالب بود و بسیار خوب پیش رفت. برای نخست‌وزیر برنهام آرزوی موفقیت کردم: موفق باشید و خدا به همراهتان!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/77346" target="_blank">📅 02:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77345">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaYwFCbIRiqzzwJ4hSxrfuK7qoSVU7ueXwOtuXaXyMju-0_pKI378u7USfIgRlkh9V836aSryHZvLUfXAjcei6GwdKP88ADyYxLANvXSAR-07tGLI7A8lXviU6NwqsBEvlqSyB32zXgZ6rNQYKf-DEzX1ANPIn21GmkqLwv1SXpc53gnbSlczEkO3J9urDzK_QqWlKvu0NW49ePl-WGET3XnB4CekgmtZ-gcntgk5QAuI-O-t-wwdQ6H8g8U3QChMf_8R6cYX4lKgvyxmoFmZbdVJ5XdylmGIFKdQFMIBNdQFL0zHdSKOqameTLjqP3pnlwvC-_9SUg05msgNbtBhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد گزارشی از یک حادثه در فاصله ۸ مایل دریایی شمال شرقی لیما در عمان دریافت کرده است.
این سازمان افزود گزارش‌های متعددی دریافت کرده که بر اساس آنها، یک نفتکش از طریق کانال ۱۶ رادیویی VHF اعلام کرده در تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/77345" target="_blank">📅 02:01 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
