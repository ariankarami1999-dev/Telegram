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
<img src="https://cdn4.telesco.pe/file/Z29MtDzD8kuVCuJ3wbN2RoolRIKGskGCZj8Ozjv9soqkW7eQTKkPEtj3G4r5i_rhUMHNL0Quz-gB5vRP2CG3eHoLIaLgFeLAMOisJzoucDBA2Y_KQKr9vaKKYF4IrXWN9HIEn3EVBhhbKh9QJ5DzhG2fr40VNv3ghKi020_B_2Ysl0SX11ngWVn0_j8dEejfC9u5PeHj_Q2GPXx36J3nY8W5An0KLRUtuTgdtPBh4Z1i4Rs76B0uI0JpSfbKpdgQ-jB2HfX7c4iQruq03uMe3fujVmsBb8R6BOoDZnB-BY7iMyNfPXp_gEPOw58hsB-MyQKCBpRAHqTzmOBqpBQR_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 213K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 21:52:34</div>
<hr>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=BLnDLM7iYokZ0G-vbEnQJvCIFyFwThRghtwx_ifl8pcCKdhpOS8x5yIMQQtC4taBtwrplzLq40LVOcqlax6w3yPFt2bMDnrc7BDA8OfXJe6osD-pNzxx2kLr6duNvcbEfizctxrr7wUJ3EatcZpd937BIuB2Ns93ZEp6vkFLRb1sZmr6-zZa7r8NThG0mBavGIg9WJqBcLGLbtzzBVvXKjwWLmfeVAciJzUPs2uvSa7Zg-wvHJyjUGNQJ4ug5H0mI4SZ3n89czpbScKTNEbD2ukK6Bvh0Zwro0hRvzGrzEfifFAI-tI9aGBVtZHdEHDJ7cGyHldmh_iNikE2L5b-_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=BLnDLM7iYokZ0G-vbEnQJvCIFyFwThRghtwx_ifl8pcCKdhpOS8x5yIMQQtC4taBtwrplzLq40LVOcqlax6w3yPFt2bMDnrc7BDA8OfXJe6osD-pNzxx2kLr6duNvcbEfizctxrr7wUJ3EatcZpd937BIuB2Ns93ZEp6vkFLRb1sZmr6-zZa7r8NThG0mBavGIg9WJqBcLGLbtzzBVvXKjwWLmfeVAciJzUPs2uvSa7Zg-wvHJyjUGNQJ4ug5H0mI4SZ3n89czpbScKTNEbD2ukK6Bvh0Zwro0hRvzGrzEfifFAI-tI9aGBVtZHdEHDJ7cGyHldmh_iNikE2L5b-_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایزه یک مداح برای کشتن ترامپ و نتانیاهو
100 کیلو طلا
@News_Hut</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVUfbS1-hRgUAA1U09dOnUIDCUQ9rEbCDlM2Z-VbJBDgN5Ilzny4dMlB0fQRKinANxP5kCWSnd3ipts8RtDQoY3JBXXPHLFda-fXdaxysXFcHMQVYg2gWT2Dht6Q_G8nAWVxgnPEsees5ub_v2e1i5Impm2_9rNbapjeDQFyACWHSOMGe_DBNjfyQA_qGaFQUEdpjx18urRITLmng53Mku8WVYuBAGJRAXzTMZTAiHXcAzpV2UUJX8xSEqaOGmRsZho8gz6w6LOfH8VF2gmqwQR2EdZ92V5VgPbdYzZVo5SMUEvJjtS8tqhljfWecRAnVsT8Kfcc9HKln-Z29LKeFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqK9xctnlVvPpnVbj5vOwRXurYw4pbleRflAbvDL0BxJadcqcI8CjQOiN4aA83loOTbsHbjEOCCrqpcE8IzaeOiJNdp-ifhNF86kimZKW-g-kifKaCpWamM-LapfBPY1qPK30y1U4jDl-LFgy2i-QBdMB55_Aq65fEzmB439HtzQAyLk8E8Y2G-JPzSHbWE6qbKjXlOAsBSIAojmFZWxcYxZYiVL5TYakQndZRZsOj5frVjug31kGx4xGNP_SuMPBa2CUgjY-6_JsFuEDaEyJWa_C0M8ll_PN_AFGRubL6a7-UAtzCHg5tVSp1XBoJ4Q8ybeOHZ4IGvP9G-uDutXZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjNho7JFd3r8kzA4IJUMJ62KFadGMiVLl2N2RQUiz9KOFfjeRKuDuAbIeJHCbDH_yup50ptX6xPvu7G7Kkk4P6cOGvKPIzS3WmbsTGFztL1hKcubppU6D2_RYJSFV0p1ozFdQiLr-8mXXFWtQVMMEGRRDhZaUtwlcqyJ9oPOmhZnal1wW-ojPLSyKyR_YKX6ChiKhL3h-VJjK5CvPy5ZsbYQYaESavMrsFD0bSAbCcPKaWp20MAQ3vxOMJzf587721AYNkkRmi3gw5JoWuJG0mLDOqCDHAQJrwA6wFw_a73fHtZA7bbUdCRN879WiXgmbZAekipWktep3sb8m5aSRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMuVB-8aYZWdmmtfl53F9taUrzrq4PCcWd0lYeAmSOfXVcopGPSo4K2P2p4lYWgWF93k1DLnykC8-SCSGhXqshJRUr8QIx6qBCgESVWoY28VsXAcTiAO9o-jh4szirza1fTPH15WIthedVhONyamvySvMCLIndKMRqfi1f_Fg3Gqlm2mxlF_WwhlkQkCFFOEej1tDWJSQPs1VXNBMAyk1gk1FWJ9iEQ_n6I5FZWMjPgiw3dEIM5fxzROGslmjUApkUFwwhU3G6SfV6L4dzvaMAkfz2-M90aZnroJj1-6grArvuKp4RQJxnJwORxVIM4NCjrdTslklYOO4bc07cXKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwIQveqeG1Hc_7YajuUyMYssWCsnuqcVv5IkF8p39qrQXZrke3cOrWsnfjwcMMie6YGj_L4KxB6BeYKr6HACHokWst4fA8le7Z1CmVTa1Zi-volX84JIwga1rk9oo4QvsMCXAOdAyJJw_dsadGt81TqC3VE-iSnoV2QZVDiuY6QOh9BsIJcVZ7pKs82d_9zgqNFBxe2fUE0gXJdl0X6t5s3k1BaHrWgajfb9VlHHvuUuxa3DmCaiAYCedLGDIEjh4xsLCsgl8KRiQjljOUT8KBe5PFLvJsjC9bvjmrGxzMwySIwNOVbHNh6tqMPZOS6Z5wUh3UuOQjsVDIgki48IXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=nKHqSo7U5wdMvElN0G4O45aPWh93xvoe7zo3HEZzJfrvAJo__opdPXeafZASIrMt_0WgLgGwqWJuFdEc_q-k1hixkbUt-ZDlTrmvf1cKQ_SafV4UKE2tbl3J-_JfyFmhnK7nuiYqqVfDRPhbWvEKZ0Kn1hC3Id2_ynD-F8Cyu1CgWzey5gftAoQUJr9Tx0WN-oPmbAwJW42OspWuDeQwq5d4lxTBjVAS7_5uWwbSchj4DAJTdRkdUzUEztfxuPx_jlWMZ-QmW91UBNxhV8uoMylGKQN0F9uM8VerPqCyo1rLbBthPaoBQKoMOGu4GaILdPJncsmV3ZIwCNWeEbjEpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=nKHqSo7U5wdMvElN0G4O45aPWh93xvoe7zo3HEZzJfrvAJo__opdPXeafZASIrMt_0WgLgGwqWJuFdEc_q-k1hixkbUt-ZDlTrmvf1cKQ_SafV4UKE2tbl3J-_JfyFmhnK7nuiYqqVfDRPhbWvEKZ0Kn1hC3Id2_ynD-F8Cyu1CgWzey5gftAoQUJr9Tx0WN-oPmbAwJW42OspWuDeQwq5d4lxTBjVAS7_5uWwbSchj4DAJTdRkdUzUEztfxuPx_jlWMZ-QmW91UBNxhV8uoMylGKQN0F9uM8VerPqCyo1rLbBthPaoBQKoMOGu4GaILdPJncsmV3ZIwCNWeEbjEpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=rt0NUHGLv8I0re6r7OQMmfw9lTLl7_mkr1JOC7T-vrzuOSpVvHGvh2GOMny0LauQdbaT-IhfSLCHPi5viBgR7defWenSc9du9lm4TWVmqrA76j6sWMLkdpLACs97JBUqQB0S7bxue-JfbG2RWdKAIAhzDw_BHvJJ3DzVmPfXL9fd_F2_Twp0iv4TKvOsUO2t2bJlFr1WCVBdq7vlMzUw7jEsBLPp1PJ6s0mfwS8hDC_uJC3FrMr3H5YBFpAa3R4iFQPbn1IinAKpsnZjyOJ2KFnGcf6PWKsBZDEOdinsG_c0Zn7RtCmQEs49CFAKQegTN80xG-16jdLuAooRBWlOmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=rt0NUHGLv8I0re6r7OQMmfw9lTLl7_mkr1JOC7T-vrzuOSpVvHGvh2GOMny0LauQdbaT-IhfSLCHPi5viBgR7defWenSc9du9lm4TWVmqrA76j6sWMLkdpLACs97JBUqQB0S7bxue-JfbG2RWdKAIAhzDw_BHvJJ3DzVmPfXL9fd_F2_Twp0iv4TKvOsUO2t2bJlFr1WCVBdq7vlMzUw7jEsBLPp1PJ6s0mfwS8hDC_uJC3FrMr3H5YBFpAa3R4iFQPbn1IinAKpsnZjyOJ2KFnGcf6PWKsBZDEOdinsG_c0Zn7RtCmQEs49CFAKQegTN80xG-16jdLuAooRBWlOmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=Gzmt4xOIlxonsa4r9jH5c5bhbN5EqPpnD1_q-kbGT7wFk4wVIUu94LUpjSPJ_jKZ11mpEOcjAcRZYp5SL-znPT1ceE625rkSksYGhl3tBXF9626VJpxyGK6VKIllUhQfqF4fuQXIia58bOWtLsngDQY_qufnue7MAJGVBbl82-nVlBsuqLZBGiZ3k61cqX6asZYHDHeAF-fCWGxH8DoVWD2zEEFCDl3c2AuGi9pv5AafpodvIecztbsF0ycqlyzl8xRwDr571Z-lr6WFTXBflpp-x_niXiI-6hSrod8lrrzGq11LTJnfUt4Vcf7QudSgyfIQNrTlr_TW0uvXHKw11A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=Gzmt4xOIlxonsa4r9jH5c5bhbN5EqPpnD1_q-kbGT7wFk4wVIUu94LUpjSPJ_jKZ11mpEOcjAcRZYp5SL-znPT1ceE625rkSksYGhl3tBXF9626VJpxyGK6VKIllUhQfqF4fuQXIia58bOWtLsngDQY_qufnue7MAJGVBbl82-nVlBsuqLZBGiZ3k61cqX6asZYHDHeAF-fCWGxH8DoVWD2zEEFCDl3c2AuGi9pv5AafpodvIecztbsF0ycqlyzl8xRwDr571Z-lr6WFTXBflpp-x_niXiI-6hSrod8lrrzGq11LTJnfUt4Vcf7QudSgyfIQNrTlr_TW0uvXHKw11A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AnhCD1ih_b0XXLpvBDIAZnB4fDiC5H8SeARPt5sTfjdSnyjh7c8SvaS22amE14lYKRALdiB1LUyndlGc7EIoSdodyk-Ix0JYYpNSTu2ESI-dyxzrG0qyzYLicA-oCr0CC2xCJ_4kEMn-oZIlH_rHa6SziBupIydZLbCPDGrTxq9e0npmBMyC-7bwNsDitoSKjVyF4qh3rNn4wd5sck8u5MRal18jsX20GRJij1ZXaYSXY4d2R4wqI2Qws0-PoAm6gdomI-mkgiGmVz2gCk-hCZaUiWFNBB9d4JBTsrXSTAVvsugLS0NYl_CdD4VS8tQuUzsNkAIL5fsjpqvLJVSu5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QqTkhnTZ41JnmVdIDMm5Y45F1mYe3vtoy7AaKuh7n_JVqeJ7iEUHMEvfLeD__GXNy7ulBHagzDoRqtRbWH_z2cN6XYbGJF-h0Eib26G4Z4lVYKYvMHOb4rdT6weZwNiN82AjruA_anoP9PTaKJAOmBQ5OAAop6liPSFC_hmKca35FpH7fq-m4STugYe7dMhxsOheTV4_tQaXnxiUJmsj9kcQHkVVnq8_o_iwrFXiVf_lbBxwY-6d1ILamDKKChAIBpfMkP6WN--Zeofe6qDsqWVnBaeUnlB1teM_2JP2xevHBpRe-LDIT1QGv_H7Sif_eYUNPMn-Ig_8ZQ8Ot6XNWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUSPj4vuyhkxsW-C7YOxTIkqqMTxNracE_iHXbUY6kd0bM1Ml0qVRD8ekCVyROl6OsrG45gJFCwbRUTGXMUClNgTs2ILMYPjqP4g-Y70JOiZ8sDOJPfGoeUCP76Xa46oFxdEfEyq3rdWWMPX9wA4NgTlYvDMwJtTQh2snM9mwmiB6_TJWX6vf9pjqNIQZzV3CVdL7xarFz4BmX-0huY0lEH7RAHoiK6u3uu8yPkEzitgBUjeeOc7sbwARb60WcV-oYSwHCkKAHzh86SI7cCWmRdKakXOuKGsEmLEasapscfBmUvgnhE_hG19aZ9Fav0VpRKYtFN_F6Y--3aNb7rp8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=Pt9pv8uvn9x4qAHmPdMCt0p5x_h-mVk_zwSNyT16xjXRkCewNzEdJ6D9Ny6IZjczopqmqtFonUiI_KFwqe7IFynHRXBuAAf4D1bd9f-AXji_FuuTF5CX3kRq1q-Z9Dv8LO436JkZ54m-jqA9vOrIb8WBeaBCOWzj00OPlxLEGw0NWk9bw6LcKEpbMeBJAo0Lxzs0CcssO5so-flZ5zLahLHWraqr_0TOdNvQ9fvrA0jBz5A4GWG9UCR9HhVyCVxiTA_FQKJD4Md_yFgjdO-IH5i2dVJYlh8vw_iK5GQ2g86nAIx0x1Zb_weaRCVSMVOQ_SPoKqZziBmUcnNJ0k0SNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=Pt9pv8uvn9x4qAHmPdMCt0p5x_h-mVk_zwSNyT16xjXRkCewNzEdJ6D9Ny6IZjczopqmqtFonUiI_KFwqe7IFynHRXBuAAf4D1bd9f-AXji_FuuTF5CX3kRq1q-Z9Dv8LO436JkZ54m-jqA9vOrIb8WBeaBCOWzj00OPlxLEGw0NWk9bw6LcKEpbMeBJAo0Lxzs0CcssO5so-flZ5zLahLHWraqr_0TOdNvQ9fvrA0jBz5A4GWG9UCR9HhVyCVxiTA_FQKJD4Md_yFgjdO-IH5i2dVJYlh8vw_iK5GQ2g86nAIx0x1Zb_weaRCVSMVOQ_SPoKqZziBmUcnNJ0k0SNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=oAFdhcQR-W6EoxvYh6HHto7yMn6iaO35qobyu_qUA7onTOvslggprGLIXFdzrUhdZj_irVHIH7irFB3hRLYmV2MIWv5B3nI9S2RTg4Z5asEAX2gXuYw71nw6dxykIX7o9fhYsw-Crt3XbEqtv6mAfSWS0XKfhQT6mKXzQawpt3kuJPdwomIJfXL8dOwAuFUCQDSzvNPoYHfGzKq8lovY69fVXQGCPUpO-0CIEJF2KJp_UIYHDo39H5C02aG8MvDkQ49r916BfFXJ0lMBIPt7leCblmhvPm84IGCAxhAdOTIVe1pT6_kRHh6db9zNlZ201LWystgfVMitglii2PEtIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=oAFdhcQR-W6EoxvYh6HHto7yMn6iaO35qobyu_qUA7onTOvslggprGLIXFdzrUhdZj_irVHIH7irFB3hRLYmV2MIWv5B3nI9S2RTg4Z5asEAX2gXuYw71nw6dxykIX7o9fhYsw-Crt3XbEqtv6mAfSWS0XKfhQT6mKXzQawpt3kuJPdwomIJfXL8dOwAuFUCQDSzvNPoYHfGzKq8lovY69fVXQGCPUpO-0CIEJF2KJp_UIYHDo39H5C02aG8MvDkQ49r916BfFXJ0lMBIPt7leCblmhvPm84IGCAxhAdOTIVe1pT6_kRHh6db9zNlZ201LWystgfVMitglii2PEtIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=Kl9HAPEDGqhINFhq4GTfEtJo7k21SaGHgFWQ6k93-HPNrKpWp_vG4tRaIsrHsAOpRBxN3jzbAei2q9y2C29L-dmb8skIVgQWjP5TnkR8Vi-xznKbem1o5b-7nWRqi5nZ8A5SSxkdB27HfM3gYptLGUTpY8e2M-TBjmb8HqftJmJNy3xC8WC8v47qTX7kM4j7aTyjFtcmRYDC5OCtJj0kBwI-x_MBXRaxhTCP8EDeaAdN2-Aa7xwezvXEOgWoA_yQGyRCeJVvgLbovsXtKTsn28iddpCE-FMurtxm4kRc6Y2lqEmKwzzxe5HT_ZWJ9Vzxld_lJjqrTcbtd_jOsAi6tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=Kl9HAPEDGqhINFhq4GTfEtJo7k21SaGHgFWQ6k93-HPNrKpWp_vG4tRaIsrHsAOpRBxN3jzbAei2q9y2C29L-dmb8skIVgQWjP5TnkR8Vi-xznKbem1o5b-7nWRqi5nZ8A5SSxkdB27HfM3gYptLGUTpY8e2M-TBjmb8HqftJmJNy3xC8WC8v47qTX7kM4j7aTyjFtcmRYDC5OCtJj0kBwI-x_MBXRaxhTCP8EDeaAdN2-Aa7xwezvXEOgWoA_yQGyRCeJVvgLbovsXtKTsn28iddpCE-FMurtxm4kRc6Y2lqEmKwzzxe5HT_ZWJ9Vzxld_lJjqrTcbtd_jOsAi6tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=pIv9bjCEaqNjU2Bv6mAd9tiWNGfh2XbasiwmrfBWBT0og7PkLLLfYy2Exq7I9DOGQFBbSFpX-GFkMArsfad-EA0tKVHAJw1-R5t-4yDeQGICHQH0yaQvihRbIPiwTcvqFxZxLfKJ8A6EDPaOixzuSVa_LB8n8JuTqpRowx0xxRYXz3nWnxms882Ms_625QfNYLuerOeyLzO37orpCwjof6UZZJCI_Yw7bc0Dto9wDx8o59IQIOSsdfP6GiJX9c3_SCyaL0MB_uCdd2kn07Slqim8uNJJY7AUvX1eq8JeKz2UTqvOYnXNTtf1XmRwetkozjX4vUA-iiZgiV1EcMQI7Ba0ePa7KuJwXpwqpjjtNEDt2zkzAeNwkEA62GYpR2PmZsI8Yq4lYgIGBH-OAPFJI9PESkt4PqBzPWLsTiAKR1Ob7M2FOq9TKMMFkJr-tO3tX7j3AIND_svuIF_ay7RwAkpFUu6LyvRu687qwyH3yf0DTGbfda1kY0E3OCZyQjbjKzneWIJZdLulNvTxBFEdlLmu2UUaOBr0MFIglaT4bBViboUiZrb2Nm4EvviPuOR2i3T45eNd83BjaVIHavcAz3bnvrYEDKeovw8X7E_TJzF-uklbtTNf06w7xxZ-RDQUYzag50qGGVdjY1kVvZ1v3bksBR7HIBTMvCfHB1ELcRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=pIv9bjCEaqNjU2Bv6mAd9tiWNGfh2XbasiwmrfBWBT0og7PkLLLfYy2Exq7I9DOGQFBbSFpX-GFkMArsfad-EA0tKVHAJw1-R5t-4yDeQGICHQH0yaQvihRbIPiwTcvqFxZxLfKJ8A6EDPaOixzuSVa_LB8n8JuTqpRowx0xxRYXz3nWnxms882Ms_625QfNYLuerOeyLzO37orpCwjof6UZZJCI_Yw7bc0Dto9wDx8o59IQIOSsdfP6GiJX9c3_SCyaL0MB_uCdd2kn07Slqim8uNJJY7AUvX1eq8JeKz2UTqvOYnXNTtf1XmRwetkozjX4vUA-iiZgiV1EcMQI7Ba0ePa7KuJwXpwqpjjtNEDt2zkzAeNwkEA62GYpR2PmZsI8Yq4lYgIGBH-OAPFJI9PESkt4PqBzPWLsTiAKR1Ob7M2FOq9TKMMFkJr-tO3tX7j3AIND_svuIF_ay7RwAkpFUu6LyvRu687qwyH3yf0DTGbfda1kY0E3OCZyQjbjKzneWIJZdLulNvTxBFEdlLmu2UUaOBr0MFIglaT4bBViboUiZrb2Nm4EvviPuOR2i3T45eNd83BjaVIHavcAz3bnvrYEDKeovw8X7E_TJzF-uklbtTNf06w7xxZ-RDQUYzag50qGGVdjY1kVvZ1v3bksBR7HIBTMvCfHB1ELcRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=qmFo3scwc71wqM2txzBLrcRbJlApWbStz4dNsk4Sac_xaWim3A45Z-XDUpKwBqnDGDup3BQFnpLVuw8VPRPc5rUh2WAQPcRTlDp1ntpjwE90bUyzvB3rSKYqKOoejZmhmN0PHVCKs32ZmMlf-ZuJVwxuvE32_-6CRygHRIgGmbl-gx0tKzOMhMzMi7-wCgoS9XQkxfX97SwOgxl6JRAAfVO1z7oA3NvWDzcejfj3z8psvEbu9_XC5JWkTeMeZXrxMYQEcURJbt_bukRITM5855WnBbm7x9cqAyse2f3_ocW_snQYtcwFCPZzAuqFJyNUHUJNgHJfc7NlIn_23NyelQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=qmFo3scwc71wqM2txzBLrcRbJlApWbStz4dNsk4Sac_xaWim3A45Z-XDUpKwBqnDGDup3BQFnpLVuw8VPRPc5rUh2WAQPcRTlDp1ntpjwE90bUyzvB3rSKYqKOoejZmhmN0PHVCKs32ZmMlf-ZuJVwxuvE32_-6CRygHRIgGmbl-gx0tKzOMhMzMi7-wCgoS9XQkxfX97SwOgxl6JRAAfVO1z7oA3NvWDzcejfj3z8psvEbu9_XC5JWkTeMeZXrxMYQEcURJbt_bukRITM5855WnBbm7x9cqAyse2f3_ocW_snQYtcwFCPZzAuqFJyNUHUJNgHJfc7NlIn_23NyelQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درتجمعات شبانه عرزشی‌ها:
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67187">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=XWi2iawMMrGQer4FcTB3QCtVPgyavb_MKVio1UF3eH0t1GZT_E6HZeZfSXx0iVzqsp7D-sR3m99aMaEXCIJ88xJ4vNpSXptk9EiKf6pGjm0N3fUGh6p7zvNokdzmzkq5Zx7KEvwuCDp1JJ6o5FXifJLVmS6X3jL_hrZunYSGUJ6J5k78kg8ZtfdzHdHpPLcBUk7u2HD7mtwECTedxrd8vqKdhT_3eDXhqCprj3qmVmBlDuQqI7BR60T0d0XVl1J8n2eYx7Scq8BjPwqnlTjAGm_D5D-VDiEJHvHARjEjPntwjTjfq7tY1PffTNtDi7wTlIboRF9wlu3gcUFBYcFGeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=XWi2iawMMrGQer4FcTB3QCtVPgyavb_MKVio1UF3eH0t1GZT_E6HZeZfSXx0iVzqsp7D-sR3m99aMaEXCIJ88xJ4vNpSXptk9EiKf6pGjm0N3fUGh6p7zvNokdzmzkq5Zx7KEvwuCDp1JJ6o5FXifJLVmS6X3jL_hrZunYSGUJ6J5k78kg8ZtfdzHdHpPLcBUk7u2HD7mtwECTedxrd8vqKdhT_3eDXhqCprj3qmVmBlDuQqI7BR60T0d0XVl1J8n2eYx7Scq8BjPwqnlTjAGm_D5D-VDiEJHvHARjEjPntwjTjfq7tY1PffTNtDi7wTlIboRF9wlu3gcUFBYcFGeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رسانه‌های اسرائیل: تصاویر ماهواره‌ای تازه از سایت هسته‌ای اصفهان؛
تصاویر ماهواره‌ای با وضوح بالا شرکت وانتور نشان می‌دهد ورودی‌های اصلی تونل‌ها در سایت هسته‌ای اصفهان، جایی که بر اساس برآوردها بخشی از اورانیوم غنی‌شده رژیم جمهوری اسلامی نگهداری می‌شود، همچنان با خاک پوشانده شده است. این وضعیت نزدیک به یک سال پس از آسیب دیدن این مجموعه در حملات هوایی اسرائیل در عملیات «با شیر» و عملیات آمریکایی «چکش نیمه‌شب» در ژوئن ۲۰۲۵ ادامه دارد. بر اساس این گزارش، جمهوری اسلامی در آغاز سال ۲۰۲۶ به طور عمدی دهانه تونل‌ها را با خاک پر کرده تا آن‌ها را در برابر حملات احتمالی بعدی محافظت کند و ذخایر اورانیوم غنی‌شده را در بخش‌های زیرزمینی پنهان نگه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s37eul_rWWdfDrZVmqFUsAh1dKNq9i0Uc_p1JU6Lk7eeTu9gZYoNLvX1AueoUDmEjfJpnWaycW9F29th1WUNxfEKeoBDFwpv6nqEfOv1K8XF8vHVNCJjl-oo0gC_Lk18b5K1rq02xPVL38jywoKLDmdIUfMwzxrycGpIPvumW-s3OjpIc4c5vyYv2-NzfazEh3tzcKPXuIsCjOiRiiqJG-s7guVS75UNAVpQM7MEnBGe-dFwLiS16hSR7JlyIXcU5GlAe9KJ8bKeDvTaaUIFF6eYRJRL419GjaWzdviQ8R6iq-E5I3BDGMVPy9PjJRemIYuifUAkXwGwc7D9IGGLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rH5MCve6-VJD_NCcpwXir5hyjGZCFnRqq1l2ORZM0pnyiFrZgg-DMW8V9gRPbWQTtbsu-WBD9zFsMd2RndOnd31yse-hyQczrEHDrb-rodx1_kV-1ztOT2dl_tftsT-Lxl0PA0Ht95sJQFv2we-NmP3nUFpS8Yc-1ScD40A-R9C3imAgdTyjPiIWSNmABMU1GGQh-DOxjUTyTHSKf_FNCiLYzsyeZnihTBIyb6WAChMlr9wwazIGziQ6m05UmEH3K3CZ83wCtIEj-z6O1DHNt2Ijy53cngu3zJDni5REY77KX8wGgK44RKTK923xyjebhXxNt300fN55Hpp6I5oD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=KKfe7eVcgOla_x6iMCOAV0ujHj9VCa0SELGh6X0YflXIU3YKv4MtK_7PFuLUDitdTTA_kTu3doiXNOWfqGU_ZR1kW5xNV53_u8juvr4bfacUs5P6xIxJo72HIR6XQqPFIe6R_F5LtWPK0bLPv2WsB_uu_79x_u5SQxYxlmG1iSU6APOvI2hLTON74m0CJQyFJVI6whC9SirlKew3ZfUJTPzHK1QilLfbkqQuB-u-9HmvfYrvnOyNdkryaGNq8WNaTm3AmnlG5vbChdjcaOXzxpPjQEVrXuaz19f3PF_41-352eB1W8BSg5DHcgtWtwUGWIVe6WHO9zONrjysFf1k2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=KKfe7eVcgOla_x6iMCOAV0ujHj9VCa0SELGh6X0YflXIU3YKv4MtK_7PFuLUDitdTTA_kTu3doiXNOWfqGU_ZR1kW5xNV53_u8juvr4bfacUs5P6xIxJo72HIR6XQqPFIe6R_F5LtWPK0bLPv2WsB_uu_79x_u5SQxYxlmG1iSU6APOvI2hLTON74m0CJQyFJVI6whC9SirlKew3ZfUJTPzHK1QilLfbkqQuB-u-9HmvfYrvnOyNdkryaGNq8WNaTm3AmnlG5vbChdjcaOXzxpPjQEVrXuaz19f3PF_41-352eB1W8BSg5DHcgtWtwUGWIVe6WHO9zONrjysFf1k2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز جنگنده های رادار گریز F-35 برفراز ورزشگاه Bay Area سانفرانسیسکو در بازی بوسنی و آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=FBba-p1Iy8UbZzOx0-jL50vBatmkc5pkQQYxpncurVimG6zI_Vepbra0kCEi0drDsEXC4AWVZNo_E05bkJvVQhqjgWoT-GAWkPNV-pPWs7V2PI3qW4xa0yeopODFddWvNsipdmuFhpVGrWuVludjDrtDpYys9qWNuxV4ag6dbaU2sTTRPJpGOLo3iFgYsmJZwbHBWpYKN5Cjec9-o0CpU0-L9DExhKD5QdGL2gaTGbUvUd3CV2WZaqtznTNfpbQPdCln_EgL1c1zPyN8-aMtn_t_cdXJV66aH0WCvH-CMGRp_GR4G3wBfLzwUFgI1R6Tdce3LNjSQNQogAQ2TIXkhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=FBba-p1Iy8UbZzOx0-jL50vBatmkc5pkQQYxpncurVimG6zI_Vepbra0kCEi0drDsEXC4AWVZNo_E05bkJvVQhqjgWoT-GAWkPNV-pPWs7V2PI3qW4xa0yeopODFddWvNsipdmuFhpVGrWuVludjDrtDpYys9qWNuxV4ag6dbaU2sTTRPJpGOLo3iFgYsmJZwbHBWpYKN5Cjec9-o0CpU0-L9DExhKD5QdGL2gaTGbUvUd3CV2WZaqtznTNfpbQPdCln_EgL1c1zPyN8-aMtn_t_cdXJV66aH0WCvH-CMGRp_GR4G3wBfLzwUFgI1R6Tdce3LNjSQNQogAQ2TIXkhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما دو بار به ایران وارد شدیم تا خودمان را از نابودی نجات دهیم. در صورت لزوم بار سوم هم این کار را خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=F6MJMNDu-aOdXrFnseqlYIShJm8wglwDEEtJe9zdciZyQJiB_go7d6Svr-N_urxzu8Xue41GSU3tKFhoU7-sQWqEdTQDjDzq8qOkCg2KPNByqNzXAi1LjVijX1xYzxmqHFX7w8Efy2whX_nJGAT_8TxLkyPR3CfDZe5XwKiB5JDJvcdqhjGcImotmxZcOVT0kediKqFulrXhlOOsitvX4GKG9fgwYnG0k7AmjK3v1BgI4eWqkbt0w_kVerIedU9UFO85VsXlMSDFD2n4u9q52OXj9PvdCSCiudDqidL_1GnisHm6PGOTPgWbM7t6n1dk_A6my_wGd5JJDr_9kWGEow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=F6MJMNDu-aOdXrFnseqlYIShJm8wglwDEEtJe9zdciZyQJiB_go7d6Svr-N_urxzu8Xue41GSU3tKFhoU7-sQWqEdTQDjDzq8qOkCg2KPNByqNzXAi1LjVijX1xYzxmqHFX7w8Efy2whX_nJGAT_8TxLkyPR3CfDZe5XwKiB5JDJvcdqhjGcImotmxZcOVT0kediKqFulrXhlOOsitvX4GKG9fgwYnG0k7AmjK3v1BgI4eWqkbt0w_kVerIedU9UFO85VsXlMSDFD2n4u9q52OXj9PvdCSCiudDqidL_1GnisHm6PGOTPgWbM7t6n1dk_A6my_wGd5JJDr_9kWGEow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
استمرار حضور جنگنده‌های آمریکا، با سرنشین و بدون سرنشین بر فراز تنگه هرمز، باعث ناامنی این آبراه می‌شود و امنیت منطقه را به خطر خواهد انداخت.
جمهوری اسلامی در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن دریغ نخواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_3qAxJfw6frwUUXVsZ-N_jqwSFNel5JK-E5pFTfOMB8nSQnO6AxpRE1JbQOH3kg42VySShNzWHyWU5CZIEA_PGA_oR5BbI59LxLl2BW4MAaELGE_CmWwhG1hFAGe7IoCcA-UcUQOSO8xDJeNQd09aoV9KnB9zE6EhShRa3NozRrXFQ70-8DnTadpKjwdwCbi8RfsEsY3DAqJLAwGWsUn9AqNgekghFhzxGXvCq_ZSQsiPP0sc8T_KFoMHjd8Mkghi-Maj27MHSq3qVr33A6iZl3vWKd3goNwyO40x2F-xMZNBxYet0uhiyc_mnGchEm-uVpZaCVqGTPce3XE_3cyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=nGSkGBGkcIi2EoscDpTAuCnGMlrBu6tNIVgNwPYuq-uZBcXwCL7066-nPuOzPV8BVj97_5OqOhKvYIa5bawhOfvZeVQX_65rqqB2aGK0ByDWt9O1VRdiHDXPJA5v7umpQY7h1mhB-lle_rt0ja76vywjmC4zOFdxi7PkALOMRcW163TS6v4M7MeqftuH0s9tPiP6C1Yreepm9Y0Cwzm8Fouyy9CMmEN566lsrLZ2DnBagjEDKjywgsBat7euRFZaQXdF3FlkATt3uuxcqkZUJhSqSIxEjhxcQb8uF1GogoOenLpXoAhaX_txBFUGK0dbd0-bwj0vbTTw584A542iFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=nGSkGBGkcIi2EoscDpTAuCnGMlrBu6tNIVgNwPYuq-uZBcXwCL7066-nPuOzPV8BVj97_5OqOhKvYIa5bawhOfvZeVQX_65rqqB2aGK0ByDWt9O1VRdiHDXPJA5v7umpQY7h1mhB-lle_rt0ja76vywjmC4zOFdxi7PkALOMRcW163TS6v4M7MeqftuH0s9tPiP6C1Yreepm9Y0Cwzm8Fouyy9CMmEN566lsrLZ2DnBagjEDKjywgsBat7euRFZaQXdF3FlkATt3uuxcqkZUJhSqSIxEjhxcQb8uF1GogoOenLpXoAhaX_txBFUGK0dbd0-bwj0vbTTw584A542iFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی‌دی‌ونس،خطاب به هوانوردان نیروی دریایی:
«رئیس‌جمهور ایالات متحده از شما خواست اطمینان حاصل کنید که توان نظامی متعارف ایران را نابود کرده‌ایم، و امروز که اینجا نشسته‌ایم، نیروی دریایی آنها در کف اقیانوس است و هیچ توانایی برای نمایش قدرت ندارند...»
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67178">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=k3HwIrf5RfQn0bN06M8CzKSFE9LFCUSSF5JTCpaBiUcnUwmHxD-rwENjg1SQtTeqCtOym-6o7SiwfZyuJatZf9Em1eGt_hoKtiKmTCYEONzz7Da8Q9DAwh3V9UsvlwX6zKGqUcsg1dITSg7jbwbVdQLJntEfuyETPOoD-HyUcAuo6mxTBW-emisWSE1831tephjSJ4jFGSZzefNiZdtsByyk76ySESaFRL23v3fETaPT7bsG7rWzX6Xy35gLwStw9ZDvKvKEVokM_r8NCKxsR1D54vK_GYopKWuyvqP3zOwZfXOM6FtU_T9-ae4z9dSmZK59pHWkr7tFKjzioX1rSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=k3HwIrf5RfQn0bN06M8CzKSFE9LFCUSSF5JTCpaBiUcnUwmHxD-rwENjg1SQtTeqCtOym-6o7SiwfZyuJatZf9Em1eGt_hoKtiKmTCYEONzz7Da8Q9DAwh3V9UsvlwX6zKGqUcsg1dITSg7jbwbVdQLJntEfuyETPOoD-HyUcAuo6mxTBW-emisWSE1831tephjSJ4jFGSZzefNiZdtsByyk76ySESaFRL23v3fETaPT7bsG7rWzX6Xy35gLwStw9ZDvKvKEVokM_r8NCKxsR1D54vK_GYopKWuyvqP3zOwZfXOM6FtU_T9-ae4z9dSmZK59pHWkr7tFKjzioX1rSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=Zm8eQJY13deQ1zWjUYpx3I0d7B1zzn31tHYC8p2MoKDmFVpdNDbzs4h8ld_cz3LoNJ_5nyHi-nsyozUtTiV4Bb7fqcGmL-42S5mjjMp5HO1tZmdLVedtDQr3KoKTxwvueMWpzjq4Ko2SBCqoNCeu0Giclxna2pT0f_8ahrQ4Z6D7ie1_bOnI__xhRJMJm7Aycot69jMxWj7RO_ClzOdbnUxuhc2WHMVtYwgKvWUnsAyfJl3t14ox1tARqWBXssj0K7EgexmfzwGGZThIl8E2QBMLQszzaNPA6DgjATW9rnkXvS75-LAxW16T9lorUHyFPTrJHh8HJfvTt0qTlXvcsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=Zm8eQJY13deQ1zWjUYpx3I0d7B1zzn31tHYC8p2MoKDmFVpdNDbzs4h8ld_cz3LoNJ_5nyHi-nsyozUtTiV4Bb7fqcGmL-42S5mjjMp5HO1tZmdLVedtDQr3KoKTxwvueMWpzjq4Ko2SBCqoNCeu0Giclxna2pT0f_8ahrQ4Z6D7ie1_bOnI__xhRJMJm7Aycot69jMxWj7RO_ClzOdbnUxuhc2WHMVtYwgKvWUnsAyfJl3t14ox1tARqWBXssj0K7EgexmfzwGGZThIl8E2QBMLQszzaNPA6DgjATW9rnkXvS75-LAxW16T9lorUHyFPTrJHh8HJfvTt0qTlXvcsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=SJ5fCjt_ZiIXpai5WGyJpvuyIj0xF4A9HquRQMHbPZT-lBe-cBlFxL_QMy5YDK9L0aO-DYukLKqxGAve0xEI9TEkd_Qpfohf8KxkdSdeLwIp8Lx4xKDTobsrhOxe19EON3q32241yw0k-KbbR4NL29e41eEN2AIBVORyVapvQSdjLbHX3X-QGqavBpCgacozNpmcedKDtkO0h2IsGe39LJFdy4UpQ2ux0agnzUWp1y8mo5ZwuNEntUNoFpHhras493fYVnJ-qTLPV_qyvhF0b_NRzsYLwJBubEbdDclvgs3rOWhNFEIVyn1N-lEtNc52AEY2Nin3YaBDlhlUgGBVkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=SJ5fCjt_ZiIXpai5WGyJpvuyIj0xF4A9HquRQMHbPZT-lBe-cBlFxL_QMy5YDK9L0aO-DYukLKqxGAve0xEI9TEkd_Qpfohf8KxkdSdeLwIp8Lx4xKDTobsrhOxe19EON3q32241yw0k-KbbR4NL29e41eEN2AIBVORyVapvQSdjLbHX3X-QGqavBpCgacozNpmcedKDtkO0h2IsGe39LJFdy4UpQ2ux0agnzUWp1y8mo5ZwuNEntUNoFpHhras493fYVnJ-qTLPV_qyvhF0b_NRzsYLwJBubEbdDclvgs3rOWhNFEIVyn1N-lEtNc52AEY2Nin3YaBDlhlUgGBVkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67175">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRAN ANKER</strong></div>
<div class="tg-text">.
☀️
هوا گرمه ؟
🔥
ما قیمت‌هارو
💲
خنک
🧊
کردیم...
🥳
جشنواره‌ی تابستانه‌ی ایران انکر شروع شد
🤩
برای دریافت لینک جشنواره به لینک زیر مراجعه کنید
.
.
🛍️
تمامی محصولات انکر در این جشنواره انقدر تخفیف خوردن که این گرمای تابستون رو خنک کنن برای شما
❄️
.
.
📍
فرصت جشنواره محدودِ ،
دیر نکنید که این قیمت‌ها حالا حالاها تکرار نمیشه...
👇
لینک ورود به جشنواره
🌐
اینستاگرام
🌐
@iran_anker
#anker
#soundcore
#جشنواره‌ی‌تابستانی
#ایران‌انکر</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=nYPns8tqWjYKXK5gXvYRx5nvt-wsE5Drwqxc3xFi8yB43lfUNpQRaLtnIU4AbJ0-9E-XaaUtliTueAoO_Jhw_2piDG7uUtNp4_ZNr5Jb_gZ6uIg5xYcrHme-1nPbhAVF6_M2ziwCXViC64Qq1BHWLFCTZ8gIEJrDgy2WvCC1i0pSlAtby8f05DBNMFlcCVLF4MALuW-vtFi7jf5ixsGyZDF3dTRmFux2AK0dWvVd8Kbnwx-sSkFIP9T3fk8C3qDnbVoF4y2sCT7tTMctCVd8ToUo0LecrM3kJxxVR51sGxgRT9ehFwvXb32OrDA59LEJbWMGjJyMV_IRk8DnywBrxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=nYPns8tqWjYKXK5gXvYRx5nvt-wsE5Drwqxc3xFi8yB43lfUNpQRaLtnIU4AbJ0-9E-XaaUtliTueAoO_Jhw_2piDG7uUtNp4_ZNr5Jb_gZ6uIg5xYcrHme-1nPbhAVF6_M2ziwCXViC64Qq1BHWLFCTZ8gIEJrDgy2WvCC1i0pSlAtby8f05DBNMFlcCVLF4MALuW-vtFi7jf5ixsGyZDF3dTRmFux2AK0dWvVd8Kbnwx-sSkFIP9T3fk8C3qDnbVoF4y2sCT7tTMctCVd8ToUo0LecrM3kJxxVR51sGxgRT9ehFwvXb32OrDA59LEJbWMGjJyMV_IRk8DnywBrxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=TRm2DulIlmWwx637s1lDB3E09uHCZfPUYEevmdIdI2yL9oIMn-ZPsT1Tt-iwXvswzpLjyOUc7YnIepxnm2uDTRsJQIE-ZSvpu17Ob59El7C0TcuKGtLT9EhrE4owP9VBrRP2rVruckcB8NNDIZv6WlywDz1iVGAEN3b4OPrys0FF22as5rRfn_Oqt8hnKWgT7tcMKk4qCF-8qMb4A3KJXQty5u-RJGtTtTw0chPH9gUmy_08y6G4chewpo7DuJf3h8ooZuXDXnayMUvu75AfsAmhEI7Rzxy4I7thSAvUVbZNzspyy46wkmaRpMzcNZiV6h9rbVXnlxj4O1TASdSdZ3_SL4j8zpQu4w-41mFYDOC0uO9IccDVAYmCy3mLScH2YSMY29dKpcPFupgy_X1ZuCQnAX_8YvekJyXxtgskUUxilH9VGrxGp97UEAHbDzg43hctY4Omtg1UyWix_f3pgCgZSC9YMNlS24sWhNZvJsNsVsWxZtLSyIcucnVgDESRHzOM006rg9f7goGixobOO-o7kpXqFVAC-C6YhSErxoNsXYdIOU1mRjhF-sq5Xkb9Uh2wgurgFrnSzeaXnPSTsGTuy82oC4i3Xx8IopHW5Z5QIREiVoOV_ZjETLI3hW5cFKU7TbMrDj4eO1r_iJUMaTpF8jwjAB4uVwPLDWfUjhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=TRm2DulIlmWwx637s1lDB3E09uHCZfPUYEevmdIdI2yL9oIMn-ZPsT1Tt-iwXvswzpLjyOUc7YnIepxnm2uDTRsJQIE-ZSvpu17Ob59El7C0TcuKGtLT9EhrE4owP9VBrRP2rVruckcB8NNDIZv6WlywDz1iVGAEN3b4OPrys0FF22as5rRfn_Oqt8hnKWgT7tcMKk4qCF-8qMb4A3KJXQty5u-RJGtTtTw0chPH9gUmy_08y6G4chewpo7DuJf3h8ooZuXDXnayMUvu75AfsAmhEI7Rzxy4I7thSAvUVbZNzspyy46wkmaRpMzcNZiV6h9rbVXnlxj4O1TASdSdZ3_SL4j8zpQu4w-41mFYDOC0uO9IccDVAYmCy3mLScH2YSMY29dKpcPFupgy_X1ZuCQnAX_8YvekJyXxtgskUUxilH9VGrxGp97UEAHbDzg43hctY4Omtg1UyWix_f3pgCgZSC9YMNlS24sWhNZvJsNsVsWxZtLSyIcucnVgDESRHzOM006rg9f7goGixobOO-o7kpXqFVAC-C6YhSErxoNsXYdIOU1mRjhF-sq5Xkb9Uh2wgurgFrnSzeaXnPSTsGTuy82oC4i3Xx8IopHW5Z5QIREiVoOV_ZjETLI3hW5cFKU7TbMrDj4eO1r_iJUMaTpF8jwjAB4uVwPLDWfUjhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLRo69gdUjH0_eh31KZDhefnn6jg22wG2ytliCSWil0vfp9nOkR9xvZuyAW551OQLjdF7TMC7CWRimSYA2noQdg0oM_vTcLe9Vpo8QzPdNe4mBIMPw6P9sCHQEiLnkC6bQdA1NYhFs2vnUyViEIR8YGyu-tFLqmhmCM0q5lThSkUZ21w3S-vwOYANuwb3oHNPXpyU7fUfIB2DLr9EdlKUZyeEhBYZ3690-VpYqSthuneY5TyBsrDFoxjEwpxvIWlOhGUf7HKNKcM2ymUcENjSTO24-rShJpLDPqu5vrO1VmnQ_QYPtR6lga9NT2DvHn9pR3BUUJsmKvNhGfgPGiKxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
‏اطلاعیه ناوگان پنجم دریایی آمریکا در بحرین در پی یک سانحه برای یک بالگرد امریکا که طی آن یک تن از پرسنل مفقود شده اند:
🔴
در ساعت ۳:۳۰ بامداد به وقت شرق آمریکا (ET) در اول ژوئیه، خدمه یک بالگرد MH-60S Sea Hawk که به ناو هواپیمابر USS George H.W. Bush (CVN-77) اختصاص دارد، در دریای عرب فرود اضطراری روی آب انجام دادند.
🔴
در حال حاضر هیچ نشانه‌ای وجود ندارد که این وضعیت اضطراری ناشی از اقدام خصمانه یا حمله دشمن بوده باشد.
🔴
سه نفر از چهار خدمه بالگرد نجات یافته‌اند و هم‌اکنون در وضعیت پایدار در ناو جورج اچ. دبلیو. بوش هستند.
🔴
نیروهای دریایی آمریکا در منطقه همچنان در حال جست‌وجوی چهارمین خدمه هستند که هنوز مفقود است.
🔴
علت وقوع این حادثه همچنان در دست بررسی است
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GjORkcn6qXYp3r-fF8SFfYaBZGj6QVzkBpE_ER1zCvFDo-DTRLkHHP2Pv0XhS_bes971cOE3W9excr_1Boih5nSFMnG6dGJ5m7-f-UeV3Rpqm3l4fHXkiYmwK6-ITJ7qQe1F_wgJSWE56hxxB5lUs1JEqQ-0Qm17_OKCmbz4X2bh6RXj-M3XhzeTXohBgWqotk65XPjnLzhkw0Y75kcHXvwC-IeCX4A8zY-iLbvlgtJhE3ciGS2kCVWd6nT1kUBLq6EOlIZ_ztsNgOMW6brZlKNU8Df_fzQQzR-jMUbEUH8Ea86NQ4rLjIxOeglIvDeqYKj-32xn4z_6JkDfNoPcLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2juPabSi6sPOC3vl6RIlb2bC5_wbvBmRvA_TmmJCphgYL-IjD760wotlVSdLphswzYX6wHZsyqeU3rAVcBJTAc17QW3x1w7zsQrBGpbKQYPDpMAiKFgeJ6Jzth8mSHRxG2-YC3OVlT1JCdTFriNwLXtLJnVxXCDP5xZo7YIlR7g1yam4OrzaH37VTl12IO5Gj0Rfv3_j-1dPi8pzznWmBCyi1wjw3GnPQoDSLFADJAvKkPwzKJBgvmnWXpqkN_0ND5Ym6GWWjy5GSJsCY7MA9J_Q0Z7kKjD0dnoxtiMH-KCjCa1o1SXLf2w3AMlpeNjoLVbUZk3jMGO_iDWNtWd2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=saS7XgrOdB_iPZUK76THY4Wiu82oic6d43jInxKs81ApLP2aJo34RZIXNJF-ntffcn9MsvxPD5lOUYvGK1171KG6dv-hYdy0uDbrUGp4z-H7-okXi2dhkigCgmrinumwR2TS1pKEmUsMkrne27xArQcafEESNjlDUb5TqT-Fw1DYKyCrIXx-J-Eu6TIacJQeC7Lq901HpJqoF4vXR1jD8zAqUs6-2tbNzJ4jVi91RJN3zc7box_cG4WGoKsPAEDXPHS8PBd1f0dQL_1VnGQzKYdz_iOFZ4YKBiallJJjYbxIb-9DyKhWnnqjEoS3N02ZQ1eRIXUEdHua_HgE5VPPRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=saS7XgrOdB_iPZUK76THY4Wiu82oic6d43jInxKs81ApLP2aJo34RZIXNJF-ntffcn9MsvxPD5lOUYvGK1171KG6dv-hYdy0uDbrUGp4z-H7-okXi2dhkigCgmrinumwR2TS1pKEmUsMkrne27xArQcafEESNjlDUb5TqT-Fw1DYKyCrIXx-J-Eu6TIacJQeC7Lq901HpJqoF4vXR1jD8zAqUs6-2tbNzJ4jVi91RJN3zc7box_cG4WGoKsPAEDXPHS8PBd1f0dQL_1VnGQzKYdz_iOFZ4YKBiallJJjYbxIb-9DyKhWnnqjEoS3N02ZQ1eRIXUEdHua_HgE5VPPRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=jwX4pReNjfAMMCTfVt1BmzzbbDvmso4mHyUsevWnwMr5aMiiK0_Lo9SxwSspPnvAd0FQ0v4yKNxZkGMPsMFB_ameegvB_Kfqqr6D6zih5sgEe7ptkHwntBYvnU5-eY_gzxv5IMYv7dXWyiTb1iznw5WplYS1g-BOOpE5nnvaHIb-l-vnmp2OASRMmloZ-cTvM8b6t8yv8BSG355j-eMkthaXkoL_9RlYFhft0Ki2zM26E1R_rEHI1fYzZab2S4yDbzdXSvMxNfLje4nED2PhEaK81NNqJuLtBrcevuBy45ZjkWbly7DtwnbeCYWbCZHpAWSCVQK3SBE6mqjTBmoo5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=jwX4pReNjfAMMCTfVt1BmzzbbDvmso4mHyUsevWnwMr5aMiiK0_Lo9SxwSspPnvAd0FQ0v4yKNxZkGMPsMFB_ameegvB_Kfqqr6D6zih5sgEe7ptkHwntBYvnU5-eY_gzxv5IMYv7dXWyiTb1iznw5WplYS1g-BOOpE5nnvaHIb-l-vnmp2OASRMmloZ-cTvM8b6t8yv8BSG355j-eMkthaXkoL_9RlYFhft0Ki2zM26E1R_rEHI1fYzZab2S4yDbzdXSvMxNfLje4nED2PhEaK81NNqJuLtBrcevuBy45ZjkWbly7DtwnbeCYWbCZHpAWSCVQK3SBE6mqjTBmoo5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=pQL-gTzSUv75j6nJoxzeGVFBx5HVYYaELSLUooOJqPow_vzxJSYVc81vOQ5luGbaBG9yZ8Kr9IOXLvOMWkfkKzlIby_U2SVg5OIuUwLrvl0v583ZtJdSEdCxf0hNyDsXHCj5Fgc-H6JYuVFDVMUArSdPBcIpHSFQrwzPtc8w6P6N5EjzYxtMznAfbWVzpQmVz9UAIETt9xAdnWUNNUU833vjufujEOD39qLWlpNdzkrAhYRD4UIJcCy1DGPKpqesKGbmTzsE1Dc2IqUOiA1-OoNn0eYh5yoLeaxQ9hx9z31heX2LmrAYFT8YP0JXuhTLi3sG6W5baC8hUC0PI77C0TzLd2ij_s9R7JlLWQlbr5ziYcx3L19jkaucpAvTqUCAQVj-H27z7JpRjWLNT5bRQZ365vYGmwy5CzgNke5dYIwYhvsKpfRvv7c3aO20uwpcpI2omrZQAoJGdapg5XY730VaShIYgc9kOunagKHDjjjp0CojamM9XfPCGqyPI3gp5GPFVpI4SglG9T-pPCflqw24kd0mSwFhOfF93rviyCcl4h---UFsZeJms50GBRlx_5yaGWWOov2GwbT3oZQqBVfw2_zaxzYSqc1L6XvLRmoGH2LqiCYF0NKZ_9ruwELvACtj8KRsQHpULHnFVZ_iW5nO7DiSP00QIShtNl-HNsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=pQL-gTzSUv75j6nJoxzeGVFBx5HVYYaELSLUooOJqPow_vzxJSYVc81vOQ5luGbaBG9yZ8Kr9IOXLvOMWkfkKzlIby_U2SVg5OIuUwLrvl0v583ZtJdSEdCxf0hNyDsXHCj5Fgc-H6JYuVFDVMUArSdPBcIpHSFQrwzPtc8w6P6N5EjzYxtMznAfbWVzpQmVz9UAIETt9xAdnWUNNUU833vjufujEOD39qLWlpNdzkrAhYRD4UIJcCy1DGPKpqesKGbmTzsE1Dc2IqUOiA1-OoNn0eYh5yoLeaxQ9hx9z31heX2LmrAYFT8YP0JXuhTLi3sG6W5baC8hUC0PI77C0TzLd2ij_s9R7JlLWQlbr5ziYcx3L19jkaucpAvTqUCAQVj-H27z7JpRjWLNT5bRQZ365vYGmwy5CzgNke5dYIwYhvsKpfRvv7c3aO20uwpcpI2omrZQAoJGdapg5XY730VaShIYgc9kOunagKHDjjjp0CojamM9XfPCGqyPI3gp5GPFVpI4SglG9T-pPCflqw24kd0mSwFhOfF93rviyCcl4h---UFsZeJms50GBRlx_5yaGWWOov2GwbT3oZQqBVfw2_zaxzYSqc1L6XvLRmoGH2LqiCYF0NKZ_9ruwELvACtj8KRsQHpULHnFVZ_iW5nO7DiSP00QIShtNl-HNsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSx5286fo1g567CaVtpCzy3Z-2WeKbhedsDdAS3SwK5HOKZ6QlpWhnoUWLpm7ja_5-ZWEVdlt7Z6MpPQ3X1IUYBA4vkCBc5-AqKZwVVtoOOodxt5g0LJ6tu3pzu-7luBd65tRMkPEZw9tAvQvAgAKOfi9RpPnTCMcIqfXrG_PC1vycr7GpOfCzIgrB9hFS6F--oQ3F4qbCkL0ugq3wnBCzOAbjWXcP2eQcJ87g0J3yV7xZU1FP_05OrPhL6__tMecOUkD0meGK9aYBC7lQz9MjzvA4VLUtINDWu9lG9ubr4aplLq0dt3YAdDqvYMzUcw0klHpsPWw-Z013L25W-_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=JX3XrY8V5JFSqUuYKRU8aRck5BGsX4owAhMXama6syaB8LTwpA-q4FtOf_9TEFL6qKmohtgcjjkjbs--knIknDjpMSAm3h8rCrKuaJK4o_Qi0BfRlriZCsfBfD0D4QGbwgP1AAnnPmJSdUdnV-x9KYXWuoRCIuJJGNSvcPuK49AGCKN6OT_0d1NLxuI5h8nmI-KVWKMfqXQChf7bM7dDcUfqg9gSKHtCadZiAVz5ZG0z5Q7cOJIlU_SdM6cA2WgBXCkONMzhlRmP0uZLFSc5v9y3FwZ9Rjm2DdALQ6FWaOO-5qQGjp5ObuetI0-xaTBavJH3l-GhPxt60iku64ftBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=JX3XrY8V5JFSqUuYKRU8aRck5BGsX4owAhMXama6syaB8LTwpA-q4FtOf_9TEFL6qKmohtgcjjkjbs--knIknDjpMSAm3h8rCrKuaJK4o_Qi0BfRlriZCsfBfD0D4QGbwgP1AAnnPmJSdUdnV-x9KYXWuoRCIuJJGNSvcPuK49AGCKN6OT_0d1NLxuI5h8nmI-KVWKMfqXQChf7bM7dDcUfqg9gSKHtCadZiAVz5ZG0z5Q7cOJIlU_SdM6cA2WgBXCkONMzhlRmP0uZLFSc5v9y3FwZ9Rjm2DdALQ6FWaOO-5qQGjp5ObuetI0-xaTBavJH3l-GhPxt60iku64ftBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله پسر سردار طاهری به پزشکیان:
مگه نفت بابات بود که می‌گی ۲۰میلیون بشکه نفت دادیم به نیروهای مسلح تا بجنگن؟ اگر نیروهای مسلح نبودن ما نمی‌تونستیم اینجا شعار بدیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=G-zX7kPHWSkRBPWEcBBR36RLenr-GMxnEw6dwnrEeAirnxkeKHTFLNmzkjpiMOlsmC7MuMv_UBVam_jInHCns8JNn6jnEu4Jp2kYMhW2SWY2qmBGsizcd_j_k4E7p3l0vdN9M3nxHbYK1gYWtFj0F6oSyafX58fUWi2myAMckY4oVVRxhHbtoGDSq9kX8yc5GGGctWFPdjPYtBe1HnpcKIOiBGM8dauIAvnA5yYSt1wg_GnqL1AHKjx6Dy1v-dTmcHXOOKCS2GytiLt2yqfLp1nuerDKYr7N40t8cd-FXLb35d6lqExFhto0uCyS2E93FaPuvY4sYJ9ct-EEBiM4Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=G-zX7kPHWSkRBPWEcBBR36RLenr-GMxnEw6dwnrEeAirnxkeKHTFLNmzkjpiMOlsmC7MuMv_UBVam_jInHCns8JNn6jnEu4Jp2kYMhW2SWY2qmBGsizcd_j_k4E7p3l0vdN9M3nxHbYK1gYWtFj0F6oSyafX58fUWi2myAMckY4oVVRxhHbtoGDSq9kX8yc5GGGctWFPdjPYtBe1HnpcKIOiBGM8dauIAvnA5yYSt1wg_GnqL1AHKjx6Dy1v-dTmcHXOOKCS2GytiLt2yqfLp1nuerDKYr7N40t8cd-FXLb35d6lqExFhto0uCyS2E93FaPuvY4sYJ9ct-EEBiM4Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=E71ecVoSGfnHtpXcCuivoPNudOTJGT9Jk4lcjQs7p8RnZlOlvhSHSz_BdUtcqNwOdtuO2A3cxxtiep37ApPc_mVpumZMzHKqpx85RsNYPi00hNlW0on-TSZV8DSsdpLaAtuQIYYOeUTOJxyC_GW8-mQ3uJbJ06l-ibceGuE9BuCEeqkpVjzLil8z42coTo2zSAW-l4H6wDm1naURJKC81TjyJwWd2MRJlhZbL4cZNYeOykuh4NYT0eUotS84fSZ0UzdSHbEy3D1b93ar95YCI2Ke-RqNN9jmgpel1LerAI4bxO9UmEGpJ4-ALBKQM2cTaB-Ikdh0qi_n62I3FpM3bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=E71ecVoSGfnHtpXcCuivoPNudOTJGT9Jk4lcjQs7p8RnZlOlvhSHSz_BdUtcqNwOdtuO2A3cxxtiep37ApPc_mVpumZMzHKqpx85RsNYPi00hNlW0on-TSZV8DSsdpLaAtuQIYYOeUTOJxyC_GW8-mQ3uJbJ06l-ibceGuE9BuCEeqkpVjzLil8z42coTo2zSAW-l4H6wDm1naURJKC81TjyJwWd2MRJlhZbL4cZNYeOykuh4NYT0eUotS84fSZ0UzdSHbEy3D1b93ar95YCI2Ke-RqNN9jmgpel1LerAI4bxO9UmEGpJ4-ALBKQM2cTaB-Ikdh0qi_n62I3FpM3bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bv8q9opiQ2VcgBrNg_LnGSlwP44JERLKSxDVu8U_7WkHbwEBq7cTg5DC-YyADiXQQsbF01A2NL6a3P0okXrID01ZiKLqh4CFlSpl1MvY66W2z1T7N5RCZIvxbv4YoqnzXwJxdQJ2J-rnWktkcl9vTiREVUptASNG57b2BPdemg4DZSlfY21JtEwjcodcvW3136lRr4B30LDTAuRsP_tOAoBG6XACUeTMe8kHSHQlSEyBlzskLCqaWrbf8eEBXLjVih2lpbP7RdZa-KIdDxMSxk7Sapa-6xwaenhfZWWGA9Yj5wiLCBYPUS1DuYSJv5CP5BPKhx1Ymy1r-r55hrwrxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=k-YYyFlV5owPwIEJIVO7PFRYoF1yBkC5dacYNm3uGJqPL-GFcJVa9MPofRsEMDW0W3D5ZIFajhCrZC_BULN1bnMvfx3X3_G8b-ALlUK-Ge3o-G1mcVyMzIjHZ9iNi-ZFIkADlbsEfQWNhCUz2-mT6UqKoUXIeW5yGIndkkPbB6peWWjPQ5UUuewSG3pc-IiBcn82EULLBlBohYxVfxBfSU4RakYc7Zjpa3u0zSPIlMCVfHOMxjB0T0RsWDQU275mN9wS37t3VqdBO6vrHzVpU_No-jGPnCMcjnfHMu1OGLgl9AK1wJKn9MzPSNvH0QVbdxssdzrQY_6lcZpqA0yPRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=k-YYyFlV5owPwIEJIVO7PFRYoF1yBkC5dacYNm3uGJqPL-GFcJVa9MPofRsEMDW0W3D5ZIFajhCrZC_BULN1bnMvfx3X3_G8b-ALlUK-Ge3o-G1mcVyMzIjHZ9iNi-ZFIkADlbsEfQWNhCUz2-mT6UqKoUXIeW5yGIndkkPbB6peWWjPQ5UUuewSG3pc-IiBcn82EULLBlBohYxVfxBfSU4RakYc7Zjpa3u0zSPIlMCVfHOMxjB0T0RsWDQU275mN9wS37t3VqdBO6vrHzVpU_No-jGPnCMcjnfHMu1OGLgl9AK1wJKn9MzPSNvH0QVbdxssdzrQY_6lcZpqA0yPRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=ac8cyeD1KwL7q9DxlYFA_WdTaI4H-eMfFnkfRPpV_xg4qFo7uC2tdn_WttMFU1UUAkrZ9DLk9T5eJNs_g0GVH63WPm6Gvp7hVeMiIbQVsnCNgHb7kcg0XrgTn8CFPsa6LcSN4eXbUF-YH4V7MMtD6efCi_JdP3Iz0nHfyL2fMaFlr9xL63DUT_MJXXQ9oF1NuhUP03XECoFToCQdG3Qv0iDMAvV7ChVurTRLwKOXtLpyT4zTU3L5a92rLUw-LEZYXKgmgXIzekDAl8FjIKoCTm_wJ48bp0rofv0F-UpLsmQycCVG98sYDMar7EC-xK5IhL1c2SDLKSnplR3s5ersCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=ac8cyeD1KwL7q9DxlYFA_WdTaI4H-eMfFnkfRPpV_xg4qFo7uC2tdn_WttMFU1UUAkrZ9DLk9T5eJNs_g0GVH63WPm6Gvp7hVeMiIbQVsnCNgHb7kcg0XrgTn8CFPsa6LcSN4eXbUF-YH4V7MMtD6efCi_JdP3Iz0nHfyL2fMaFlr9xL63DUT_MJXXQ9oF1NuhUP03XECoFToCQdG3Qv0iDMAvV7ChVurTRLwKOXtLpyT4zTU3L5a92rLUw-LEZYXKgmgXIzekDAl8FjIKoCTm_wJ48bp0rofv0F-UpLsmQycCVG98sYDMar7EC-xK5IhL1c2SDLKSnplR3s5ersCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=O8y0OqPgcA82UwAhafCgDgc6ESXIxDpemB5cw8iVVUnZO6-BTo0J_HTU03yNJ9m4dxmXU5q_QjsoV--YRqYV5-1ByUULTRJ5xUtxm1UNE6bS_bFIsCQpgO39GpWpz_DCyWzPB3xPtkkz2DI3FpPh4ssB5o83WMvgjkYFTh0NSaYqNhgvb5Pk_LH1U7Qr88l0Wgkc7v5up1jdJNmVLV0oKWKzGZLxFYNTdTqYUO_w8tIT4FQCox1s5kfZD9tgJkMoN5Y0Q-pSS9vSGVK0Vjzo4ElgHBdu3l0ZfCT_7eSE33uS7M4H-SKPrCcpVazlSuQPfr_2Qq5BA7fpP0kvQ3gMx6uLQaftZtH-ZcOyJ4sYCeGgSonB86dDJGcYK2ygJaV79t-6rhdTDkSYRA-xV-HEdv8cjA0Mf8RgHii7KeeOlgcn6wqCZdHTtP79IWWjfdMUtC7_1D0T4b_xworgqTJhXUXprTJ44Ria2JXeUX2W-Db-94GmHYhqcF1q0I0dSfEc_zwrCG2EiLU8nyfNtd06vDbX2p1bMX0archfsLSRsEMF8qjR9dYecyfji3N-a1h8Kfv1wQGmO1YVJ6Vs7zVtXfN_jytUFm9hLqwlSJloj18UFc-bFBdynEK0nn6Ku00Bbjq9LBehaRLoPxZ7Gleiop1bf5V43Z4AfKtGwtBtj8U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=O8y0OqPgcA82UwAhafCgDgc6ESXIxDpemB5cw8iVVUnZO6-BTo0J_HTU03yNJ9m4dxmXU5q_QjsoV--YRqYV5-1ByUULTRJ5xUtxm1UNE6bS_bFIsCQpgO39GpWpz_DCyWzPB3xPtkkz2DI3FpPh4ssB5o83WMvgjkYFTh0NSaYqNhgvb5Pk_LH1U7Qr88l0Wgkc7v5up1jdJNmVLV0oKWKzGZLxFYNTdTqYUO_w8tIT4FQCox1s5kfZD9tgJkMoN5Y0Q-pSS9vSGVK0Vjzo4ElgHBdu3l0ZfCT_7eSE33uS7M4H-SKPrCcpVazlSuQPfr_2Qq5BA7fpP0kvQ3gMx6uLQaftZtH-ZcOyJ4sYCeGgSonB86dDJGcYK2ygJaV79t-6rhdTDkSYRA-xV-HEdv8cjA0Mf8RgHii7KeeOlgcn6wqCZdHTtP79IWWjfdMUtC7_1D0T4b_xworgqTJhXUXprTJ44Ria2JXeUX2W-Db-94GmHYhqcF1q0I0dSfEc_zwrCG2EiLU8nyfNtd06vDbX2p1bMX0archfsLSRsEMF8qjR9dYecyfji3N-a1h8Kfv1wQGmO1YVJ6Vs7zVtXfN_jytUFm9hLqwlSJloj18UFc-bFBdynEK0nn6Ku00Bbjq9LBehaRLoPxZ7Gleiop1bf5V43Z4AfKtGwtBtj8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=psQMaDAnWYCFQMu28dKGqR1q2GR9LoiLc463kO3tbWVKlWQbtArWOkiUehCWokjl4ukd8MZS08CAK3No6av0csj1MzIyuQFSAgA98GfINSoqMRG3QeTwrFaiqRLzpV_pkfhH0UlOg76NT6-0nU0clKfImg1728NY3feBKJSc8RjZuysEUGrgp9uh_JJZ4Q61P--aRez49mzFtd1G2qL9cF2PWmogT8hQUJEWvfNp9DXtpfRyLuLceN1tmYz8rntIifKH0iVj8cXWw2wkYVlsKWwwkVxz9eNbZSSNYiE03jZo9azRBuxkZyVw9WEpmNSkDA4DuhF_fKC0FsG8p9l4NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=psQMaDAnWYCFQMu28dKGqR1q2GR9LoiLc463kO3tbWVKlWQbtArWOkiUehCWokjl4ukd8MZS08CAK3No6av0csj1MzIyuQFSAgA98GfINSoqMRG3QeTwrFaiqRLzpV_pkfhH0UlOg76NT6-0nU0clKfImg1728NY3feBKJSc8RjZuysEUGrgp9uh_JJZ4Q61P--aRez49mzFtd1G2qL9cF2PWmogT8hQUJEWvfNp9DXtpfRyLuLceN1tmYz8rntIifKH0iVj8cXWw2wkYVlsKWwwkVxz9eNbZSSNYiE03jZo9azRBuxkZyVw9WEpmNSkDA4DuhF_fKC0FsG8p9l4NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxk72Agjsr4p74oAXHLFoUrh4F1d2Agl2udvTh9pmJ-bH7tmxsjydqk4OfJ8jr09qTtE5JxOz3RQY3YQ1EunYeoL1JbS_nJxN0VMGkCBkKJL8RWRCCwYB63-s4e_jkMl1BIbi28hO_W2EcGbnRafPa3v6sSu7Slts-5mpL567bei8qw4vLGEtiNOM8DMFL9_uwNFhk_oZX4nM7QmO3G-b-hXkVvOf3gU5OdeTk3kAuYQCLQ68gMIEAdfVP9C9Nk7VQhhHT05aKUm6m4pWx5B141Bb6LubEVXIU79eDzxzOoJpYO-UGnOT5HzCoSRImqKa16ZmGJBWseLljxpY8nTyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=ctIeKKbFZ88BOHQN39nNjeoGvwrcMOFRsQZgO26UqgVZVWx-ntD2xWk3AyMJlaz9rVYCVQwQ4sk3iVri2SnOzNeBi6kJnW0a5OAzORiyPtNQ-NpT_IsdLFvDRrfzGgSzjWCz_l7LKvg-Rk-9KAl9voe_gqHWI4zt-6yyibFPDYhxWckqxEnzAbSxmDTwq5l4phqXoX8C9lYDaSqmPp63Ot4CYoFfoUdPNwAgZNpGP6p2T6kv8Zbrf5R2prjce1UDm8eQ6LB9E_Wz-x4HcX5qDfMpFzxt5o0gtM99iczx_NGdtwFr_j2NYQXFhgmXypwzcTgw2eMoyNd9047ev7Zwkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=ctIeKKbFZ88BOHQN39nNjeoGvwrcMOFRsQZgO26UqgVZVWx-ntD2xWk3AyMJlaz9rVYCVQwQ4sk3iVri2SnOzNeBi6kJnW0a5OAzORiyPtNQ-NpT_IsdLFvDRrfzGgSzjWCz_l7LKvg-Rk-9KAl9voe_gqHWI4zt-6yyibFPDYhxWckqxEnzAbSxmDTwq5l4phqXoX8C9lYDaSqmPp63Ot4CYoFfoUdPNwAgZNpGP6p2T6kv8Zbrf5R2prjce1UDm8eQ6LB9E_Wz-x4HcX5qDfMpFzxt5o0gtM99iczx_NGdtwFr_j2NYQXFhgmXypwzcTgw2eMoyNd9047ev7Zwkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=c4H6NSswI10QRK6M4WxZ0gOaIilt74ve_fNhxpKSUdy4deMTv6K6tU5pNiN-0nQgiC6B2pe-mxqd503Ab0iy8kU2AFGc9axgHbOjekm2MbaILdfhWEZv-64EHsBNoQJJh_n4JUZx9ovtMt-FeGwIVLb6_1Q3l13IhTybRcmNHNxLwbinMIEaOtwZ1PJzD90rW-o6s35m05LbvTHIGU9AG-uoK7w8cJrGmW1g_SCEHB93SP1QNwnoeKVJ6hv_dQZLDj-ARInK3Zfdp1af2QkFKSSPnEOz5RNzasMtbmLoBMM2K_zSMVu9qsHF9RtPLLxa-KDa2MiwVVe9MU91Ary2vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=c4H6NSswI10QRK6M4WxZ0gOaIilt74ve_fNhxpKSUdy4deMTv6K6tU5pNiN-0nQgiC6B2pe-mxqd503Ab0iy8kU2AFGc9axgHbOjekm2MbaILdfhWEZv-64EHsBNoQJJh_n4JUZx9ovtMt-FeGwIVLb6_1Q3l13IhTybRcmNHNxLwbinMIEaOtwZ1PJzD90rW-o6s35m05LbvTHIGU9AG-uoK7w8cJrGmW1g_SCEHB93SP1QNwnoeKVJ6hv_dQZLDj-ARInK3Zfdp1af2QkFKSSPnEOz5RNzasMtbmLoBMM2K_zSMVu9qsHF9RtPLLxa-KDa2MiwVVe9MU91Ary2vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت‌ترامپ :
روند خلع سلاح هسته‌ای ایران به‌خوبی
پیش می‌رود… بازار سهام تقریباً هر روز رکورد تازه‌ای ثبت می‌کند.
برای سه شب هم محکم بهشون حمله کردیم
الان هم روند مذاکرات خیلی خوبه.
قیمت نفت به‌شدت کاهش یافته، حتی نسبت به  زمانی که حمله به ایران را آغاز کردم ،
الان نفت رسیده به ۶۷ دلار،  پایین آمده.
هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=TZfmQMSjvWyuDfjtDzUDnPgEjx6GbUCTB0DdiuVC1eXA4s6z2y1z06ZetLlWi2AdMAQED9LNZ-e5Tr6zhN1cMQNQUGwGYEFyKqcsozcMvfsiii4ezKEGcYCTjVb3391Hc8pJd9L35KA-zdSlpzwE4Se9mFbr6SVTad6X7dzcApTLQINO45-1DFMa6SwPhcPocOfgt6a5ke1kxLegy4Udrhkm-iyUBs6SV1Ghqy2Bk8LlWLWX2nlnvFR9KhtCzlnTNOkEKzVyi5-H5CktkVk59o5J_LxNecKrTxEzMNxXZHG74jZwXLwThBXWckL-4Wc5laiNmQxAtu3kcvf7H2EuLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=TZfmQMSjvWyuDfjtDzUDnPgEjx6GbUCTB0DdiuVC1eXA4s6z2y1z06ZetLlWi2AdMAQED9LNZ-e5Tr6zhN1cMQNQUGwGYEFyKqcsozcMvfsiii4ezKEGcYCTjVb3391Hc8pJd9L35KA-zdSlpzwE4Se9mFbr6SVTad6X7dzcApTLQINO45-1DFMa6SwPhcPocOfgt6a5ke1kxLegy4Udrhkm-iyUBs6SV1Ghqy2Bk8LlWLWX2nlnvFR9KhtCzlnTNOkEKzVyi5-H5CktkVk59o5J_LxNecKrTxEzMNxXZHG74jZwXLwThBXWckL-4Wc5laiNmQxAtu3kcvf7H2EuLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67147" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67146">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nB6tCq7Fiuwqp2X9wyGPmVM7wp_ulDzSz_tz60_JEjaNqUdK_gEiklNEyNn5gzZrtr0jtHi8bqWNv0p04ImGqNo9eEsz7Gvd9b0KA4EyNHavOZca1TqBJkAGH_rNUnTzyuw0qfl29OzIoued9fDFaSjRbOr6MgZAfJTJqUK3-ZF8PeqwGPebJ81VOl6eYzYfN6V_n-hLHzKhbSJHG7mGYmNdDwewSkDlpIYh1_TQQXnDLxHVZF_tgJ4FjW6WVvioYRXwLGxIh_QLQus3gFOT_P-25_Xn8QNmKDoMAJv0NLslyJdMdiSOJGNuOYd-zKVej5sQWFjFJGkx7vt2Vi8v-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67146" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=HLCQ4np3VXX0MjhEFQpvm0TYxMrhThrd2Bu_O5dyYUmYeb9Iw5P-llH3O0HT_Yo8l0HhoOd8u9dcwRhChYJYzPjxpdwmOvAiTbPa-KkUViff0YxWDR_ATe-eTuqFwPZU1QldDDNb_NNBQ15wTCvrOcejm9A_nXsJf2hd3Fv-HDMVmFzkP4JI8VICZ5EhgiHFBxtvZ4jUElWIwL8fTdJDTA13PxIWUz47hhc_A4CbOopkRT1NKlu4rQHJauQwoVEY3qBUY_nDXA-PRNn9ePOAWVbQXK80jqL2Hakh59CFlsJzcSRtXtqN8CB7XdtRQHlrvpFcVM5kZ1ZLOb3n5_vRNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=HLCQ4np3VXX0MjhEFQpvm0TYxMrhThrd2Bu_O5dyYUmYeb9Iw5P-llH3O0HT_Yo8l0HhoOd8u9dcwRhChYJYzPjxpdwmOvAiTbPa-KkUViff0YxWDR_ATe-eTuqFwPZU1QldDDNb_NNBQ15wTCvrOcejm9A_nXsJf2hd3Fv-HDMVmFzkP4JI8VICZ5EhgiHFBxtvZ4jUElWIwL8fTdJDTA13PxIWUz47hhc_A4CbOopkRT1NKlu4rQHJauQwoVEY3qBUY_nDXA-PRNn9ePOAWVbQXK80jqL2Hakh59CFlsJzcSRtXtqN8CB7XdtRQHlrvpFcVM5kZ1ZLOb3n5_vRNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=c_KIrqRo8eqW3xFPHMmcuRDQ99r-LWTrhpylcWY29aO53KVQwlZxPeQPPCktsw8zt2jfR6gftm63RkPZZjFQ-buJKJvTQEqITUn0gmszDBwAGfeDSpiyp4IyC_CdioSSE171rZNR4XusMiES8sZ8KTl_8_KYCee-m_5qSY2qiO2Pa0Lo5-Kee05vNz7F4I2aQWeLq-s2Hg2aZvk5E477DkwbIEoOBTT4Za3xM_Z6ckTnhKclSOuBTZscQEA0fVJNztkVE9AIGfHDE4HyxVFtNtDEBsNlgVBXNS9G55tFTS8aOO2RfPd12Y7L_Adh8EKoabAwRcduUiFZYDJztm6zvg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=c_KIrqRo8eqW3xFPHMmcuRDQ99r-LWTrhpylcWY29aO53KVQwlZxPeQPPCktsw8zt2jfR6gftm63RkPZZjFQ-buJKJvTQEqITUn0gmszDBwAGfeDSpiyp4IyC_CdioSSE171rZNR4XusMiES8sZ8KTl_8_KYCee-m_5qSY2qiO2Pa0Lo5-Kee05vNz7F4I2aQWeLq-s2Hg2aZvk5E477DkwbIEoOBTT4Za3xM_Z6ckTnhKclSOuBTZscQEA0fVJNztkVE9AIGfHDE4HyxVFtNtDEBsNlgVBXNS9G55tFTS8aOO2RfPd12Y7L_Adh8EKoabAwRcduUiFZYDJztm6zvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
🔴
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
🔴
پسر بچه: آره، جونم مهم تره
🔴
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
🔴
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
🔴
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
🔴
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67144" target="_blank">📅 17:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67143">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=DUFFY2wNOvYb49ZZVBUaOkAvPICvURVlqd4vX8wuPfH8hQBpThdzaV5tjiLKqYBTa8dNd-jX8svR6vKzOsmPeL8G4XEty36l6Jlj1_A9NRAHOXdxpOOzq4nPQpxKjG2FvaH9qEoSicSEZHOolszRrIb_NzbFSajvsv_wH6rrIk2glbgmBQ2SBnbT2z1RkyKSR0_s_stfMNMb0Px9gdl2NeuLWrscrAxGcTrGxcfzZuk7SJNblw8Kn3D4i3MFbAdHBkejs4v8aVp81Cj6o4XmuzIdW1NJksv9Y2TEWfQv9DEoXEUKh2eeInwad6OwrKylai-vNkNz-nri4luFefJh8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=DUFFY2wNOvYb49ZZVBUaOkAvPICvURVlqd4vX8wuPfH8hQBpThdzaV5tjiLKqYBTa8dNd-jX8svR6vKzOsmPeL8G4XEty36l6Jlj1_A9NRAHOXdxpOOzq4nPQpxKjG2FvaH9qEoSicSEZHOolszRrIb_NzbFSajvsv_wH6rrIk2glbgmBQ2SBnbT2z1RkyKSR0_s_stfMNMb0Px9gdl2NeuLWrscrAxGcTrGxcfzZuk7SJNblw8Kn3D4i3MFbAdHBkejs4v8aVp81Cj6o4XmuzIdW1NJksv9Y2TEWfQv9DEoXEUKh2eeInwad6OwrKylai-vNkNz-nri4luFefJh8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=cOirNMt5ZCqJv_kt4SVTgmlzjzlNniFyrUiD-YQlE1p22Dhhl2PHvcrF38ozJZMOnI8PY6lbBZBh9F-nmmglal1QNiM5ZV_eAnxdN00qasDZZ0zkxDblUjSZjisY0Z8C50EHtbk9BCkaLliJg38bpUuVIZTg1FvAg1JN6O0PYpH0eKGCYh552gwhmar8w8b8Uolo4U23v05M1RpCI5YtZuzmmDZy-NT56eDS8ODoIoJo6zi23WBUA486TDUhPGxbGmiwBTpK8evmrKJ4w8Ri9svhQc4aVR73rKXlb07fXkY0hJrmCLWcVvvI2GUn0PahGgf_q1reXM671SVJ255VKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=cOirNMt5ZCqJv_kt4SVTgmlzjzlNniFyrUiD-YQlE1p22Dhhl2PHvcrF38ozJZMOnI8PY6lbBZBh9F-nmmglal1QNiM5ZV_eAnxdN00qasDZZ0zkxDblUjSZjisY0Z8C50EHtbk9BCkaLliJg38bpUuVIZTg1FvAg1JN6O0PYpH0eKGCYh552gwhmar8w8b8Uolo4U23v05M1RpCI5YtZuzmmDZy-NT56eDS8ODoIoJo6zi23WBUA486TDUhPGxbGmiwBTpK8evmrKJ4w8Ri9svhQc4aVR73rKXlb07fXkY0hJrmCLWcVvvI2GUn0PahGgf_q1reXM671SVJ255VKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hFDHO8Wbp3mS0mGDJN3lPV9yIZYwESbp-1ASjMl5hRCXExU7XZRhwDRuTakg24dYoILNlE8pUAobA8iePNXtJTy4IWsbphhrFIC2QE3IcPAv1xKh1cyazTH8jFGO26pbtJNOw_nxZVU9C9VQ_t1cpzo-haDzYmwTB4wllLAiQJTpi-HVDu3Lu3XuQX1IKuSeOkDJmus63QSQRz9jDvHllYwOiRcvyJo5Ni7F8uY3Iu3YnH9UrtumJHHs4ryT6RMA6wAXwg7S_WMgqA32lvKg3_UaRwx9f19OnfQRCAZZ1vglqBN_MPTn8-er-XWt8OIRlbrzwEcjwcMyMtRw3fsTow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPRi34RG8dn26TahT8M_woJ4JgtGigqsqbEG3ANaobsitCiHGthUQBXBwf30JXfVUR8MMFzw4CpeionkXdIOF9-TZ4K91jsobaioLJZlQaMXwYNwwhm17u-GMq27JThPM_jiZIG5_YS5nVVaNDd5hFELyvJ875EoJocZNOMGByv-q7RIE8aZHch_oivsH1EY2J5y8Om_FkeVzVCq-U2HGH3VWfKUQWxVu2h4bbTc2IE5C7izxtUfyd6g6qRx61cnP-q7S9I-gA4Dkis2XUdWe65qeZY5r3cTQhZuwNG_02_LebsJnR6fkmqWPA34cfaaB3A11fCWY0714tscWjPQyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کاتز وزیر دفاع اسرائیل:مجتبی خامنه ای برای کشته‌شدن نشان‌گذاری شده.
عباس عراقچی:هر تهدیدی علیه مردم و رهبری ما، پاسخی قدرتمند و فوری دریافت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67140" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB73Pz3gvolKivxgP98xeMF-7mnTmt7kh8All56x58KHNudQLXGHaQgpdtzPGUFT4kZhusg6o7LFnnnb9EeqDcVtetQ9KUeCosp14qRcJ7rFIJkqKeCJStJ-C-pRDpdEEyNumu_vpb2DHDDDk9IA4llkAh_QfSz4oEgjxpmm-4R2C9o21eR1K9f7gjYUtYNlRnMb11cOEg6CLusVrKB4vE_N7KnNjnOiTrBVKf5sdddxHwpCPBRDGK9lyeRieg-Fzi0_YLBQ1_0pKPUhpy8XGzciyNT3vAVSYQLC4B8RIKuantYIIOqEXYtc55nA3mo0M6KXdBIaJDbzLvBMREhT7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIBtvC4y4TblLEC36NiERRfe7UuQ0wYu1Kp7CsWVWhwemmci6UNsy1wn3DsKUCxwlmAyMpHl6T41jLXFrApAqv1vT47qvEUgqiOp6r0PGHAFLhj_CAywGOkuF6DyI9z5uLfigFCTQ6jI4AJ4Kp1OMTFISBl3tgaq4L8dK9KAb1NVoNAFPmOSEDbSF2Y6eSRlCvH2ZUx-gdIlRXTS3E96d5o3H-PTx6Ol-qdsNcb0Mnm6_o3XCzFuRdl2gRY6z6DclLKjs68F4rzhApx09bsG10kddBrMqP0utNCU9nsc8vCeZTdfFyCcJKdyK2z7uXnjkDFxlmGjAykSSaBYSQMBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RX3lGh7LbTGj8yI1BF_ThaI0f9rW0C0ZtJN0zoUkg2lvVU0RC5Xhp3Ex6Li0sM6P6AcQqj2U_C2nXW0DQ75W5pJwKO3gBFLvQWokr6csPFAoonuVQh1CcG1zR0t_IrVtms7N_HxKgG5vKJJfRrcxJaV8B2qCXYzMvU9ed9pfBSYC5HmcROhRr_YzrKVA2lG7UrnfvNV8Wwj0Q3F-TKhq84LIi1akdoFw4TC0x3Fq4F2Sk-v7m26-nII95hEQ6m4tWUgv46n7edmkC1vpkKoOd05AW-ZXbsn42TrgiJlO8bZglrTjazD390N2uGxpPnjh34QcSygtwEQPf0uqVkhe8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=j1nMK7XvFoHFluQEDLUEq46pN6AU_L2mbSLEdUC5Gq_G_TEOvgP7yIO4-h9NPo0iUgYmiIgqhMXYbyoo-aNlP8U6amcptfiDkeIuZxLqZWIB-UlN5caa1csHrAbuUZvHzgUQ_l_93E5WU6ne-oDFWdTxRCwOYnIa6THFLsx5sTk5YAjkZXnKtWO5vNX5poVOZuBSIUsiywz9EypcJwWfhDuwEjFYw6YhrlcRDJdS7zTRWEcBpIebxfy2yFTHdY5D_VAJWldRa1BN-iO3CIT1Hhi2hlMtTo-n9RC5YuqehFOMsc10B5B7vj6_49ifCejFg1nZrasgFwFYOcaBdWUeSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=j1nMK7XvFoHFluQEDLUEq46pN6AU_L2mbSLEdUC5Gq_G_TEOvgP7yIO4-h9NPo0iUgYmiIgqhMXYbyoo-aNlP8U6amcptfiDkeIuZxLqZWIB-UlN5caa1csHrAbuUZvHzgUQ_l_93E5WU6ne-oDFWdTxRCwOYnIa6THFLsx5sTk5YAjkZXnKtWO5vNX5poVOZuBSIUsiywz9EypcJwWfhDuwEjFYw6YhrlcRDJdS7zTRWEcBpIebxfy2yFTHdY5D_VAJWldRa1BN-iO3CIT1Hhi2hlMtTo-n9RC5YuqehFOMsc10B5B7vj6_49ifCejFg1nZrasgFwFYOcaBdWUeSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r4tTADTf_NsqRiVw_2yeLFFuDkjf0Sms2WGls0yf06BBALJs3w_Fq04rXejr3tSS8pthii4GeKsu-ZHyg-uS1w8sdQabLbaUgMZ1qahmZ7GkelI8yxoWGX7aAqejSuKI1gq2_WHxoskjkcoB4_bkXkduf4vU39ggk66puB9BwbHY4zv31fx4n9sPWf0FGI-rBxRQvPWO0fBOGC9fPXcMDKxhQc3bda_M5BdCz0CrK8zX3bT7qUUYnOHH1ubtMjsseFVrlQcNARdZIArYaRdXwvyOR_slAZyuU1D9SyH5uws3C82w2eEJnaS1XoodONvoxJE2JM_m0rQrSa9Ydk18Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QrPXNXVd9JDIvea-DWseWdW6SMnvVA05PPsz5VdAlyPKIoXQXuKrWCRllOWNW-Uvz0cO2EXsCVHKWA1pl6hJDn2e5FSUp_Sey1L4Gb6bUEOOMtsDzWoHAl-CCDV2odk1kfpNaD3a1IJwIFUWCr02MIOvNBqeqCnu_JqEZy9zbLCIPAWyb3yPX7_JzplnjxOFOl8Qr_d_2Lt5_csf2jLgmJmaBgOzplt4_56xy8BQn0F-q6EswvMFUkFObH18hqMpWBAttz3XDytn9tCf0n9wr6bPuk_-9zTLyMVcjrehYfck6vMNVX_D0MKujmxWSXf8BD14W0h6hWjsIrnf4U8v3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=SGSttmhJ5OJygS75S88FBq42jD6080koNA_iXnZI2WEsNn_0fzFi7JRLNgOS2g0-_L2lD07xrNU7aJDVFXZ0MRLbGAvKY_MFk4W4P18l_JUeR8vTbb2TEFq_26qUzkarh9yJ7sO_kglAxeqcoZ-PzfH6KIQG48J0KXIK1a053nM0obz79rkyvs64i7IEwpW80y-0ZD1scaXcgGmSKn2wZroGCm4QcgbKVFGR4DYcoCyoM8zdNtgSt10hl6hqPk1rx0ebiC4yoyI5kQdBoJuBvF_S9jn3AiIbBl_-grZoPxPMiGFy-n0TWZIB7zCXMJYmgZ2Lkk6BRkzifRXYRb0VZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=SGSttmhJ5OJygS75S88FBq42jD6080koNA_iXnZI2WEsNn_0fzFi7JRLNgOS2g0-_L2lD07xrNU7aJDVFXZ0MRLbGAvKY_MFk4W4P18l_JUeR8vTbb2TEFq_26qUzkarh9yJ7sO_kglAxeqcoZ-PzfH6KIQG48J0KXIK1a053nM0obz79rkyvs64i7IEwpW80y-0ZD1scaXcgGmSKn2wZroGCm4QcgbKVFGR4DYcoCyoM8zdNtgSt10hl6hqPk1rx0ebiC4yoyI5kQdBoJuBvF_S9jn3AiIbBl_-grZoPxPMiGFy-n0TWZIB7zCXMJYmgZ2Lkk6BRkzifRXYRb0VZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=oxMPwDO08jwbkRn7SaQ6BCz0QBXlR2ogx4kPKvV5d6SmWjGM6dey1WZsBmk2NaTbx5-Vi0sRm6NDA8NZ-yMgZ6l_vduhfgt0QwtOAkkoJXkMBGjXlWvWY-6IrDfpK41l18QSoWUBCe9gLEm7CncYu-XKwFGhRxiM2U8vQu3_iRuquH_c1YQhQqkp8aAWXxxctrXbuUj2nTIE-6STtF8UurytorCbrh0VaJzST8UjNp69M3VffQERt10iYHsXX8eNrbqn7iIBQr8ge6fQUpUE9dvAHdBGxVqPM0cgsFTWFCtSSQa2QMFnJZS4FislvV7f-Rjo2n-70I11aEpo0dJafg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=oxMPwDO08jwbkRn7SaQ6BCz0QBXlR2ogx4kPKvV5d6SmWjGM6dey1WZsBmk2NaTbx5-Vi0sRm6NDA8NZ-yMgZ6l_vduhfgt0QwtOAkkoJXkMBGjXlWvWY-6IrDfpK41l18QSoWUBCe9gLEm7CncYu-XKwFGhRxiM2U8vQu3_iRuquH_c1YQhQqkp8aAWXxxctrXbuUj2nTIE-6STtF8UurytorCbrh0VaJzST8UjNp69M3VffQERt10iYHsXX8eNrbqn7iIBQr8ge6fQUpUE9dvAHdBGxVqPM0cgsFTWFCtSSQa2QMFnJZS4FislvV7f-Rjo2n-70I11aEpo0dJafg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی
:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67128">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=vN3fCiTX-4qMgeMuVSs4Cy1hdpYlL9VRYKttY7QroQYhRfV75EOFuZb8WNbB2nVXsAW7UdLvEZnEHs7KfNhVFgUzDA1A2S04nRt9HT9X-ZtQ9Rl86l9ijBFn9Sf6hu8uDEqQBRJpTHokTu7SeDCBGs36GXGEhuL_rgxbj0qbMryBi1k6jwNqahzprVBTnZVdVC9JLXmmPov0UBATGhBEtOfbmS805ewNNi40YBP-vR67PsfUSNJqQJiMCYfmOnk6ljFhfVjDsEHRmWqN5wj4Hbt30RQCoaNfHXYBmSDJbsx0_K0vpo2AFCxKTI_S6pw0yoqe3d1dqdXUneUi-Z6m4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=vN3fCiTX-4qMgeMuVSs4Cy1hdpYlL9VRYKttY7QroQYhRfV75EOFuZb8WNbB2nVXsAW7UdLvEZnEHs7KfNhVFgUzDA1A2S04nRt9HT9X-ZtQ9Rl86l9ijBFn9Sf6hu8uDEqQBRJpTHokTu7SeDCBGs36GXGEhuL_rgxbj0qbMryBi1k6jwNqahzprVBTnZVdVC9JLXmmPov0UBATGhBEtOfbmS805ewNNi40YBP-vR67PsfUSNJqQJiMCYfmOnk6ljFhfVjDsEHRmWqN5wj4Hbt30RQCoaNfHXYBmSDJbsx0_K0vpo2AFCxKTI_S6pw0yoqe3d1dqdXUneUi-Z6m4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=FhFCRskfkdSPj8zK6-A3CyDIAFASlZgnMYkX74BT7j0HWMCXPxgdagWXPJJ3F-2UpSUSrBnnxv5CoMnK7DzZpWTnPDQ3IT_-GX2kGpZQAVt_W4qtx4PUAtKW-9s2vibbfZr9rRXLSXha-aZmQUDRT7hYJTDjdcE3Xie8w6Whl7iv75Rl1YQxpaXzMyIKBP84_9pUHnWw-eenEX5UYzGK3SiamfpWE5OPd0hUMyfRmWGo8kelJEp6GTmiACAiE0z44vVWuGxZDPDixuyxFHCqBIDvhtxCGCaImtKiznLQjnHv3jKwx-0ZZQGbKAGIyXCI9Vcqb1GcSHaFAG81GTqsLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=FhFCRskfkdSPj8zK6-A3CyDIAFASlZgnMYkX74BT7j0HWMCXPxgdagWXPJJ3F-2UpSUSrBnnxv5CoMnK7DzZpWTnPDQ3IT_-GX2kGpZQAVt_W4qtx4PUAtKW-9s2vibbfZr9rRXLSXha-aZmQUDRT7hYJTDjdcE3Xie8w6Whl7iv75Rl1YQxpaXzMyIKBP84_9pUHnWw-eenEX5UYzGK3SiamfpWE5OPd0hUMyfRmWGo8kelJEp6GTmiACAiE0z44vVWuGxZDPDixuyxFHCqBIDvhtxCGCaImtKiznLQjnHv3jKwx-0ZZQGbKAGIyXCI9Vcqb1GcSHaFAG81GTqsLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=V2CvuWlK0e0zzY9gM3L-e56LfdM0sgDVJW9Tw1NhGkkRPNvgAsJ_RT6jY-_3KULnIYTHIXGh7leGdXWRrZuR0zUTPYi6SSIWThbL-R2SoiIQDmXItFB8BSGaDwY-16fFpZZNF2CZJzPKS7_aD1X1H_Xpi9FSQ8OJCo-FZWKDOVl4E0vH2VIWDvgaOiqwp_lhBjbNMJ97JBSGqlx0kgqEKTUkZx9ps7BuvltjPZvclk7rlkHsHlC9QAPtuf3k4F64CmvRT3RsjkZGEq7T46PQnotVnDi5axyGvjGd5q2omla1ma7dFFqIlblsM655OQ7gSoIAvB1vPyfkw69AO91TWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=V2CvuWlK0e0zzY9gM3L-e56LfdM0sgDVJW9Tw1NhGkkRPNvgAsJ_RT6jY-_3KULnIYTHIXGh7leGdXWRrZuR0zUTPYi6SSIWThbL-R2SoiIQDmXItFB8BSGaDwY-16fFpZZNF2CZJzPKS7_aD1X1H_Xpi9FSQ8OJCo-FZWKDOVl4E0vH2VIWDvgaOiqwp_lhBjbNMJ97JBSGqlx0kgqEKTUkZx9ps7BuvltjPZvclk7rlkHsHlC9QAPtuf3k4F64CmvRT3RsjkZGEq7T46PQnotVnDi5axyGvjGd5q2omla1ma7dFFqIlblsM655OQ7gSoIAvB1vPyfkw69AO91TWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFIrT-XDuz80ahVjkyKnqJQQvRzMtacScXTePDG876AxufIldON7wgKwEuupUWOWupsovbFg1F-aCcmsfsPh98TrZjVybh86jYy-9lm6-L1WujRiMboBgv7XgRTQ48NQP2cOHy-mKwq-Jr6dn0i-1o255jWrUE78yKFXuPN18G-4UKcoOtS9UjY7JSh_xDbYigfbc3uQ4y8BlyZGBcRQpVWl_26skzdMjr-Yd02Qy3EPGObmR4PIwqoDH_KMJjP5ABeKErJOBcV8hPPFF0GSGrxYmcH2tx8zhRI80yTAE1VeBCa1QpuI0iZPF7k0Tml41ACQIZw9u7x_0WHWAtt6Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8gQ9JlvVr_LeSpx0P242f6a93PaZtMXSj-kglBIp6Ela6Bz0kbxPilCWGFYnhFdtrvOm7UQcAnRS7Aq3oBcGrdavL_-ZciNVWz2Uv5KvcPWarlhg0lQFzoArIVWt5KoWnwBPaFMKAI-qGeZ6WVH_ZHwrl4A9E1f5HR4nu04dUMa-Nq0O3desS6Zym0QfjC6LN-cIZeqJ2zgSlpvdPYMQiwcGmSoNsXy6eGvhPlPNJrLSKApdDrcFIIdPL6mmjQ9cFAg5-tFQHpUA7eLBPQFI-SI1KZFGZ25oRWkDDthiRw_MY6oqwCbXpubA-k5cyGUSSaJKj3WTy1d6miiygIYUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MuedbOA8kjTa1AHMRTDGkd57rAEP8-txLuZ8xgZQcktCuSVBrRUl94ODwT4K292ilFIz4Kpk8VlXYI1Ylh7cQuBpc_sBVypd5wkvLeMECLFqn5iBtOKrmsAGrgKcE3lJX3h3qvQmIR8Q04bWGVD3OhVaiq6VkL_CUfg9NPqPuVFSoxR55dl6VdZWtx9QmwdjlAguqAQ7I9QVrx3h9M4yt-VkSmDXUXnD-wj4CgGIBsiGNHpp9BNhVRRxWbhqbRSQ0s--KUkSrGN_O9WnuJHfIeeM9OO6CZ1kv_LXuTvuCqBcCtMl11d3FNkvVA5SuO17YMVHRVQjo77velPtVceehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67121">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=AYzmEp8dbRROP6qW5VMMZGgoTxZKFNkgVG4dXZ3viv7SsuLNTrYTZGVOTRthxt99fFM52HhrrAUIyo5ScrFWHcO6If1FgI19DvTIpgfQp-ZnYujAZ0cQYFNy_LR4jWTNP07Y9phB0mFHMRV1JFINhr5GYkLZf6zRg_HwkFTgGokY7gAIXt0dtMnOn_5Ozi8eCRq1c-Cn2B1S6xZSr_6-ofCKIuBkh1Qc4RMS0785SF2_9OAJKzLUo2QkhnuJlJaqp_8-N3vinoE0_ix_5yslilDlMKFOLKImJe6TI0XsFBB5JfxD6Q60JfOffUVlPDg_TylMARWUGX6PE4CGcPIsmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=AYzmEp8dbRROP6qW5VMMZGgoTxZKFNkgVG4dXZ3viv7SsuLNTrYTZGVOTRthxt99fFM52HhrrAUIyo5ScrFWHcO6If1FgI19DvTIpgfQp-ZnYujAZ0cQYFNy_LR4jWTNP07Y9phB0mFHMRV1JFINhr5GYkLZf6zRg_HwkFTgGokY7gAIXt0dtMnOn_5Ozi8eCRq1c-Cn2B1S6xZSr_6-ofCKIuBkh1Qc4RMS0785SF2_9OAJKzLUo2QkhnuJlJaqp_8-N3vinoE0_ix_5yslilDlMKFOLKImJe6TI0XsFBB5JfxD6Q60JfOffUVlPDg_TylMARWUGX6PE4CGcPIsmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKab6OWvXrit-DZvreSKb9bZQ2W3Me14DQFCTZc8hkG-sPxjoSRjiHCQGUE-0oY_MLBpF0DOIQAs6Fr_TZMX2s3ii5v7do15D3Pm6k4eAg8sxdlwVFtoiyve6Z-4YGZTMCzorbpKd7bVo2xGmApE3m0Z4pYdyLSi8rlNU9BMWMySZQqY603gh6hPf5toAmCFKr1fNVw1HnweojXVnPrVQlbwb0S0P5WUIZVp3UtmFpR7Mu6t8a94O3AFJ14JkUQWLXw8CYioYIw8_eRYWHXniyqxL3cPPx-nK02fEji8_r5__IkAFJZ00T-8M1lFQVhd7Y51up68nhOwjxaxZ6LZEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67119">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=XgQsgG6-5S_uqF8gHb2a1LLImMmVkKsw82xA6PPUHp_UQ84tU_k5wWn3_IStwAwkqQqbLZjUzeCtx-Qg-XCb6PM1mZZqBMsquQRntXFcrRl7-0O6nrGbC-t9CZsj794BXl7Cne20zEgm6awb9sdirud9vB-KOE_AI7xZea9qgqO-XVNMprkE4Z9G5Mxoonp-WArv_qBiOILr8HY_QQHwrxYz3t-t56g6Ci0xqN3SF_CTGDQoAd-E97DuOgGfOtVkDzKoOK1Bd2zqH3Nku1QBONA4eEKO353kDV4qMKFQHoJ-nNJjZfn81lkO1qsqlpyIR_rMe0_VhxFagrj-cieNUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=XgQsgG6-5S_uqF8gHb2a1LLImMmVkKsw82xA6PPUHp_UQ84tU_k5wWn3_IStwAwkqQqbLZjUzeCtx-Qg-XCb6PM1mZZqBMsquQRntXFcrRl7-0O6nrGbC-t9CZsj794BXl7Cne20zEgm6awb9sdirud9vB-KOE_AI7xZea9qgqO-XVNMprkE4Z9G5Mxoonp-WArv_qBiOILr8HY_QQHwrxYz3t-t56g6Ci0xqN3SF_CTGDQoAd-E97DuOgGfOtVkDzKoOK1Bd2zqH3Nku1QBONA4eEKO353kDV4qMKFQHoJ-nNJjZfn81lkO1qsqlpyIR_rMe0_VhxFagrj-cieNUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بخش سانسور شده صحبت‌های قالیباف در صداوسیما:
قالیباف در قسمت پخش نشده این سوال، می پرسد: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوفک صادرات نفت انجام می‌شود.
​
🔴
این قدرت جمهوری اسلامی است به آن افتخار کنید و پای آن بایستید. این سند شکست آمریکاست و ما با عزت آن را انجام دادیم.
​
🔴
گویا حداقل ۲۰دقیقه از این مصاحبه پخش نشده که نکات مهمی را در خود داشته است.
​
🔴
برخی قطع صحبت رییس مجلس را با بازگشت روزی‌طلب به معاونت سیاسی مرتبط می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67119" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67118">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=WCAY5cyS_C5DsHagbN6sh29RpVeJc9m3li1DLDRzSUXqTwDf1_KhckV6ngXyvOQaC906ri-OnfZkglU6R6QH47-TjkJD5PXPamcz_uRDHeKBu9tKtRkwebr3eGhzgoEF2W---qoNXfoMzzB1FEl2wXGrGrW6wTfjcj5LFEfTGoSn2JdBOp8jo5AGpolVlOcmQDDh-5dQA8JUcNNljWBo0Ydv0WdZIrQGucdvIc2qafMvebLb-GS-JP4LjlbH0QfflqOY_xjByi2fFowq5Wq3dHrop_z0Jm4yp5aeyg8zKyvW_hLLF6LLsmnWYs_5yiscvRc4f4ER3XgFmAzRl33Mjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=WCAY5cyS_C5DsHagbN6sh29RpVeJc9m3li1DLDRzSUXqTwDf1_KhckV6ngXyvOQaC906ri-OnfZkglU6R6QH47-TjkJD5PXPamcz_uRDHeKBu9tKtRkwebr3eGhzgoEF2W---qoNXfoMzzB1FEl2wXGrGrW6wTfjcj5LFEfTGoSn2JdBOp8jo5AGpolVlOcmQDDh-5dQA8JUcNNljWBo0Ydv0WdZIrQGucdvIc2qafMvebLb-GS-JP4LjlbH0QfflqOY_xjByi2fFowq5Wq3dHrop_z0Jm4yp5aeyg8zKyvW_hLLF6LLsmnWYs_5yiscvRc4f4ER3XgFmAzRl33Mjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پول های بلوکه شده برای دولت سیزدهم بوده است، مصاحبه اش در صداوسیما قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67117">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=Q3hQ0raukA6x5ZhP7GfhXa83gyzxQQ8AygE2qonQVfy4iEvWgzWl3xAOzQprPCTCDFAeqLszw_ym1ySA51AyKiLjA-f2lg38iguStYeHdezOf-esrmVQ0risDZOJWKtPXbKmdS2eQ4DDj0Sfae73K_ArvuZzSmeZPEjL6H3U-mvDFWEOVB5O2ke1kwjMhBzCnp9OeuNri2VYgCjnexSB986uTZulKz4hZS4uF7mbuuhaR146ZbwsyM0M-lPam4SNU3OXg6I7eQD9UYRJ1qcc12MHnBxV5gCDnbWuuC-Ttd84Nm2g8gnQ2mywRZxi8IbwXsV9-eKpMwqFS8eLzLL5Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=Q3hQ0raukA6x5ZhP7GfhXa83gyzxQQ8AygE2qonQVfy4iEvWgzWl3xAOzQprPCTCDFAeqLszw_ym1ySA51AyKiLjA-f2lg38iguStYeHdezOf-esrmVQ0risDZOJWKtPXbKmdS2eQ4DDj0Sfae73K_ArvuZzSmeZPEjL6H3U-mvDFWEOVB5O2ke1kwjMhBzCnp9OeuNri2VYgCjnexSB986uTZulKz4hZS4uF7mbuuhaR146ZbwsyM0M-lPam4SNU3OXg6I7eQD9UYRJ1qcc12MHnBxV5gCDnbWuuC-Ttd84Nm2g8gnQ2mywRZxi8IbwXsV9-eKpMwqFS8eLzLL5Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظه قطع شدن گفتگوی محمد باقر قالیباف، توسط صدا و سیما
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=enGcy3Qe10DsFKPb8do8BGRLdAI3XR5Y0inqkhy_tCvUX-0VeZekXfPx3U9OYRNWTrs6SbgQl4w9XWIj1J92jA61AIOprdjYT3wIBwUfABXGXQuRO-YNNPIv5HgGevUvlKpcoYh3sRsBnG_fSskxW76zNvTPkX0ZsxmbPjxYmR4t1vh8-_hiN9uv-9IVPMbTQCBqkdko_w3BIixCZG0xz5UvQxLRWRwpMOq9IS5G-mZ3RWgx1htHazpz5Obb8dQm15Dtg0yiiU918CFbHUxbasp58E3cUQIu07Yxuc5v9EMpMBai-BeyTNJKi03N5ySWyl5noP7DZce--5Fmt2VMjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=enGcy3Qe10DsFKPb8do8BGRLdAI3XR5Y0inqkhy_tCvUX-0VeZekXfPx3U9OYRNWTrs6SbgQl4w9XWIj1J92jA61AIOprdjYT3wIBwUfABXGXQuRO-YNNPIv5HgGevUvlKpcoYh3sRsBnG_fSskxW76zNvTPkX0ZsxmbPjxYmR4t1vh8-_hiN9uv-9IVPMbTQCBqkdko_w3BIixCZG0xz5UvQxLRWRwpMOq9IS5G-mZ3RWgx1htHazpz5Obb8dQm15Dtg0yiiU918CFbHUxbasp58E3cUQIu07Yxuc5v9EMpMBai-BeyTNJKi03N5ySWyl5noP7DZce--5Fmt2VMjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=FQT0t5Ham6hYnTJ_V1iT5qZ_xc3eU4FCfs1v3IQM5OGLHrQoXXPk_GJ9jmPOV7ZbPj8NGo_4ufE7U3TiYtJxaAUzqH2_0qaNTUC-hoJECctWdNSHJdwZ_a8PChQBwieqx0ct3Iavvpff4LgUoJ9I2Qd5Hj-ER8Y53waBrC4ECg7Yh3Bx5HAiSXqBkygy1QRfWdLSbSaIWtGVmgYbaLANUGChGYs2jUt3ql4_jc69LEEjXIoY_l5PIBjl4RnDGkWA-zlTrLHJ87c16da--VgDhIyuWure5I0kbhBCECo04L3TRoyjmq_sM0FyK0mGptFksU9sHTiNVabmtfWQYzS5iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=FQT0t5Ham6hYnTJ_V1iT5qZ_xc3eU4FCfs1v3IQM5OGLHrQoXXPk_GJ9jmPOV7ZbPj8NGo_4ufE7U3TiYtJxaAUzqH2_0qaNTUC-hoJECctWdNSHJdwZ_a8PChQBwieqx0ct3Iavvpff4LgUoJ9I2Qd5Hj-ER8Y53waBrC4ECg7Yh3Bx5HAiSXqBkygy1QRfWdLSbSaIWtGVmgYbaLANUGChGYs2jUt3ql4_jc69LEEjXIoY_l5PIBjl4RnDGkWA-zlTrLHJ87c16da--VgDhIyuWure5I0kbhBCECo04L3TRoyjmq_sM0FyK0mGptFksU9sHTiNVabmtfWQYzS5iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBsLaQn4lDVTFZeiA-2dKgXKQi4-RveM8eLMxwWHFOhNuaYyg0r4lbc7OaMIS25nGGPXYSguoLiiKn0No5Um_yW6SCTTpnAZcu4F09z5kkTVLtJPT51AasJvIuaDnE7kICAdrNLk5Se7mg5NLV55D-MPsfMI6nYjhKuhb9LGokBGQVeeJkzwxRQW5Zrkl_x7dW65vZI_RpxK4TNAKGm_aJzk6_CJsppUOnU-bVC5Poy-lC3Os3CgBbeJDry1KLEYPnygaYveAEwcn7vbUCKgQoZ0NRnoJjeMS2jnYsf0DDAjVN0NUNCGnz4gdhbRcn-fXZreu9Htu0X4C9ZIoi0rCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
جدیدترین روش ترک اعتیاد  گیاهی
بدون درد، بدون خماری، با انگیزه‌ای نو برای زندگی
🌟
✅
ترک فقط در ۵ روز
✅
درمان کاملاً طبیعی
✅
بدون داروهای شیمیایی
✅
بدون بازگشت
✅
همراه با پشتیبانی روانی و انگیزشی
💚
بازگشت به آرامش، بازگشت به خود واقعی‌ات
💪
تو می‌تونی! ما کنارت هستیم تا دوباره بدرخشی…
♦️
جهت مشاوررایگان فرم زیررا پر کنید
👇🏻
https://app.epoll.ir/74570725
عدد 6 را به شماره زیر ارسال کنید
👇🏻
🆔
@Sahar77631
☎️
09923413672</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67113">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY1Xl0ZY17aTqMH93TrLj8e9ghL9y6hjekX6VsqT2M6eRxPu0O0pF9IcpYITo4f5Tqm0bfu_-lhdzNQ55Qj8XoZnVgSOys-i2kcK9LFll_3Cf14cfpp-43PcN-_iOINPjKpxME3yOqO2sbcGoTwxj9ElOUIlOJ2naBXPlIvNeVvdfDASo1MShnIZPF6LHsYGoIwfKaxw7pcCWJTAMwiUuR86h33H24uuums21wxX76zCmGxbFIuJVhv8OnZ7Qs45kI--DnkCREYMvW8ZbwbgZKsi5Qp6rDJzrG7fQlyCy9ClfDQaQH1vnJkXidb57g0Ya4XX2-tWJW1h4JznolyK_9xk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY1Xl0ZY17aTqMH93TrLj8e9ghL9y6hjekX6VsqT2M6eRxPu0O0pF9IcpYITo4f5Tqm0bfu_-lhdzNQ55Qj8XoZnVgSOys-i2kcK9LFll_3Cf14cfpp-43PcN-_iOINPjKpxME3yOqO2sbcGoTwxj9ElOUIlOJ2naBXPlIvNeVvdfDASo1MShnIZPF6LHsYGoIwfKaxw7pcCWJTAMwiUuR86h33H24uuums21wxX76zCmGxbFIuJVhv8OnZ7Qs45kI--DnkCREYMvW8ZbwbgZKsi5Qp6rDJzrG7fQlyCy9ClfDQaQH1vnJkXidb57g0Ya4XX2-tWJW1h4JznolyK_9xk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=tCNMcw4KuEP-uLFO5DqBw-dlexwImqoVmGYt2_UbtcChZjeo-hhsP_SgCJmyPtqFpComTDU-I9JJ2pOR883Jl-XcTM2t6d_2Z2Rj6PUwP_bx-baROR0XMxMvhI1HajrkgUCeolNQCeSwVFJqKAZR7sjBr7-f5vD-Cqd-weWWCW0bHLDuzmPAxZ-SLU0Iu0CeEVamlFt1WYPmbcKsEV7GRbELoekjthuDPoFUQpWWApg4v-gBAggPp91NFI2YIHoUbMDTb4qoNmZ0MD2GN7Zbj0tVWrDEjNDJEH1bo5U_SnGi13-X1R-RtLVJ77GPW8NMKY-gIISizCUjppuTVOyUGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=tCNMcw4KuEP-uLFO5DqBw-dlexwImqoVmGYt2_UbtcChZjeo-hhsP_SgCJmyPtqFpComTDU-I9JJ2pOR883Jl-XcTM2t6d_2Z2Rj6PUwP_bx-baROR0XMxMvhI1HajrkgUCeolNQCeSwVFJqKAZR7sjBr7-f5vD-Cqd-weWWCW0bHLDuzmPAxZ-SLU0Iu0CeEVamlFt1WYPmbcKsEV7GRbELoekjthuDPoFUQpWWApg4v-gBAggPp91NFI2YIHoUbMDTb4qoNmZ0MD2GN7Zbj0tVWrDEjNDJEH1bo5U_SnGi13-X1R-RtLVJ77GPW8NMKY-gIISizCUjppuTVOyUGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=k2tKoeFpl8f6I7WLAW1XPEsWGT3JdoHws08733bfIB_sUQat6aYs98FDNlpB4MeVbMsFTBIrC1SRKFspwTD0-E0W3yf4E6wGMI4WxvbALcYrFRNo7Q8yrAWe8cS4Inua0prB2f9FuzcBx65lj9OIL_PCRduYgs69LR2USvafgd_9U9fJz2J2iJYmhoNy2m58GdIOIxvoYa3Rjpg1diyaMDtmkcvX-jggqxxv62-tuFg-jjJ9SGl-GA7gTcmojDE6nOU2JsYNo5zp-UH6dxGaBE6HPpaNP9wwzAiMWZcAKhcNyIRHiv-41zBGqQuRqAraqgtplLd_HS2brWcmM-59e5u-5G-Bj8iuCUmBkPrSKd_r16iZKkQzQ5fHZVJ5pu6DGmCrE8fYtREBffUVoT0d5apSoA135p3d1u4wZ6E-pbQdc51Ih2W4X2ovPSkvX94A73J9T57dYm6AQygrV3eg8dkwO-E14EebPmmgFdTv7hDT86pNodDm84eVD6WXKC9m1NyhDs3Tia8AAlid3qqqheVbQV8KAoomo72CAHqmud7eYpwn8o8BiEt3iBrRKHwF91Zfl5OLEQz0F7nnrU9scx6thXkgKxifovQJRJzQhjc4DvgV18jTqXphWvDagg8hzVAXAXEnbOR9SYvrmv3o59PLcOWioekj9OvzqY2RasA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=k2tKoeFpl8f6I7WLAW1XPEsWGT3JdoHws08733bfIB_sUQat6aYs98FDNlpB4MeVbMsFTBIrC1SRKFspwTD0-E0W3yf4E6wGMI4WxvbALcYrFRNo7Q8yrAWe8cS4Inua0prB2f9FuzcBx65lj9OIL_PCRduYgs69LR2USvafgd_9U9fJz2J2iJYmhoNy2m58GdIOIxvoYa3Rjpg1diyaMDtmkcvX-jggqxxv62-tuFg-jjJ9SGl-GA7gTcmojDE6nOU2JsYNo5zp-UH6dxGaBE6HPpaNP9wwzAiMWZcAKhcNyIRHiv-41zBGqQuRqAraqgtplLd_HS2brWcmM-59e5u-5G-Bj8iuCUmBkPrSKd_r16iZKkQzQ5fHZVJ5pu6DGmCrE8fYtREBffUVoT0d5apSoA135p3d1u4wZ6E-pbQdc51Ih2W4X2ovPSkvX94A73J9T57dYm6AQygrV3eg8dkwO-E14EebPmmgFdTv7hDT86pNodDm84eVD6WXKC9m1NyhDs3Tia8AAlid3qqqheVbQV8KAoomo72CAHqmud7eYpwn8o8BiEt3iBrRKHwF91Zfl5OLEQz0F7nnrU9scx6thXkgKxifovQJRJzQhjc4DvgV18jTqXphWvDagg8hzVAXAXEnbOR9SYvrmv3o59PLcOWioekj9OvzqY2RasA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف: اگر می‌توان گره ای را با دست باز کرد چرا با دندان باز کنیم؟
🔴
کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد.
🔴
ما در شرایطی با جنگ و آتش اقدامات تلافی جویانه ای را علیه رژیم انجام داده ایم.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67110">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=MWb48fDvF2sNsHrpIS9P5twkPy4cgKNGjShBw0NzM0APFUW7fHwLlwSf73Cuf_pmN-IIuvexXesBofEGtW7lnR4vp0EDz79tLOlQkapPsNC5nMKwoed5BP1ZV07Ii5J0l46MRVnevY3HMqBznSAjOfRA_hlIRZL79SU6eUdmXM_taCkzkHJiKY_PGKJ3OLC_bsNEF-zeSfZ2E2HNlaKsubZhOWFbe0gwr0L6XxNfoeG3qqcnhovfxg-v83nZ_Yf_SexIsgicry74vebKc8mgD11OvohQGMcsEgrnvIx68II1Us-FMwArVCNcvY5Q1mE2fcL3DVWVZHmfubxIQuWc7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=MWb48fDvF2sNsHrpIS9P5twkPy4cgKNGjShBw0NzM0APFUW7fHwLlwSf73Cuf_pmN-IIuvexXesBofEGtW7lnR4vp0EDz79tLOlQkapPsNC5nMKwoed5BP1ZV07Ii5J0l46MRVnevY3HMqBznSAjOfRA_hlIRZL79SU6eUdmXM_taCkzkHJiKY_PGKJ3OLC_bsNEF-zeSfZ2E2HNlaKsubZhOWFbe0gwr0L6XxNfoeG3qqcnhovfxg-v83nZ_Yf_SexIsgicry74vebKc8mgD11OvohQGMcsEgrnvIx68II1Us-FMwArVCNcvY5Q1mE2fcL3DVWVZHmfubxIQuWc7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
تعهد ما نسبت به باز کردن تنگه هرمز و ادامه مذاکرات منوط به پایان جنگ در لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67108">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=t5I736XIoK-bdbIP0x1ddbjpwPF5pkzkBmgHjOyBBJMF8fifCHeqcYbIZPG6qv0oFE6eTa3h8GsRaPdWlwyLWzsIjieWSUFwkzrka8b847ohRqvOEBOWIwjOdRTefUG_4Vq-zZWdy0EFjTFOgtb4al2OUSGzgioRAgvLD6UkVp4tEA4vS8YylTzB46psUWdLmHtETBuUJw7HdYXBNHrnAxPIExR7m-orpykd2Q7mwkAeQwe2BUnIzKYhBi6GAKTyJKLTIZI0BYXDl1ArlSKowHEAc9axUURdOX8ifOMbHxW2_fhonenu4D21v8BDgpr3DDM3bUaW7ZIqJfxDE4679Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=t5I736XIoK-bdbIP0x1ddbjpwPF5pkzkBmgHjOyBBJMF8fifCHeqcYbIZPG6qv0oFE6eTa3h8GsRaPdWlwyLWzsIjieWSUFwkzrka8b847ohRqvOEBOWIwjOdRTefUG_4Vq-zZWdy0EFjTFOgtb4al2OUSGzgioRAgvLD6UkVp4tEA4vS8YylTzB46psUWdLmHtETBuUJw7HdYXBNHrnAxPIExR7m-orpykd2Q7mwkAeQwe2BUnIzKYhBi6GAKTyJKLTIZI0BYXDl1ArlSKowHEAc9axUURdOX8ifOMbHxW2_fhonenu4D21v8BDgpr3DDM3bUaW7ZIqJfxDE4679Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم.
🔴
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش بس می‌دانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67107">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=EnpzhdCMbZXr-e9GxynRl8LHMAgyJWjhMgkGF1Ihvj77SLmHL6u3WPgcZQGZErnhqNUG8d0Zm41i1eUubcTa6ibugWqJUNSSrNNyeUtWrTNIBxIQ83tTEljK4jIZ7CwXgWJC6bdGIEx5TiOaGUq74EZ2P4cfsYS1nXHkDJzv48vapUHFd5Awx1uXzgDZld62HnuTa0g94tqFZc6mMhazEWTuDOEtT7fZtZ9AKwGvMkkjJlWx1ZJVA_20sjx5zQ3diJHKWarEvH37d6UrqGoguaMUN_s37MvIuMyohbsy3_8oxpPKuzer7rU3pOSclj8A6zhMpGQuFnzaBF1HbdaO8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=EnpzhdCMbZXr-e9GxynRl8LHMAgyJWjhMgkGF1Ihvj77SLmHL6u3WPgcZQGZErnhqNUG8d0Zm41i1eUubcTa6ibugWqJUNSSrNNyeUtWrTNIBxIQ83tTEljK4jIZ7CwXgWJC6bdGIEx5TiOaGUq74EZ2P4cfsYS1nXHkDJzv48vapUHFd5Awx1uXzgDZld62HnuTa0g94tqFZc6mMhazEWTuDOEtT7fZtZ9AKwGvMkkjJlWx1ZJVA_20sjx5zQ3diJHKWarEvH37d6UrqGoguaMUN_s37MvIuMyohbsy3_8oxpPKuzer7rU3pOSclj8A6zhMpGQuFnzaBF1HbdaO8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
دو اقدامی که پس از امضای تفاهم‌نامه، در شامگاه ۲۴ خرداد رخ داد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود که از اتفاقات مهم تفاهم‌نامه به شمار می‌رود.
ما در حال دنبال کردن دوران گفت‌وگو برای تحقق ماده ۱۳ تفاهم‌نامه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67105">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ov3wrpCVh5KsiMAQoBxEoYqOh3ZY0dBwqxxYrDSLncQSH4RjZLEkfY7VyfpaOtFvcKWWuPA8WgOt-XHLpla3Upyh30JUT5tRp82xUucSeiBECx9J1i4W0CREyvqY70Of9SyHgg4NLI_BOBfMVqBT6va8dbM83YV8oE28RGQ9OlsAuvCZmHHsWgcDoD2RVegcAZd1SkIgh4yiYhBncHzbUq9ACQ9QQhgkKs5HyLuwk0Ikt8kl09RwddtIiWAz_T88rCJnnXpKwG5EJU3xKtWkIo41T_JYn0WfNCXtHPcKb4d3L88U0U3A301KWRfjCWwO-4S35Yw206Xp67bX5AOPmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ak8kxwtKndkHu6wrkJLUFsg2_8OQjcxMGVeoc3jvOfSmDHPKXq5emmuC9zgNK-9L7nwdLV-fvkVEZRIxW8PsrQYHW6iGmJa-RnS8PA5jWkOLJWVagxGgsSUnKUEbUKUAJdbwa__lk7ZI4I00gEyshWn8hfWE_LL7WGBrxeQfaPeeAe3cAGJa-Nd-dkWYSdcNx1OVvEX-wohmxuNcjQLO87Ki_MtW_jtDvc0o2zyuBdneEKSArvzc1mnN4QEghZC4qWUjJd6-A8w9cW9uVWpp2s-NkgxEKg_pg8qsRYGVG5TlWX_VsXOvGVrD2pleTAzAqrEAA0x97YYD3SWtHmubGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صفحه اسرائیل به فارسی:
چرا هر کجا این تصاویر به دیوار است، دزدی و فساد هم هست؟
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWZkbPMyFUQkM6MoYyGkPzAOvekIevOtsrZHfg0jCp6posSsIc1jpHLuXEUbJ10EHynf8e4Y-1sivBDBLxIpPzxZwr2LcDzyqxws9_Yf12PXJ-qCilWLfCnrRK_8R3suj9WiDxTD5nak5vOMyzA0aANNJZFkgZJ2PPZDhRQxEAmt5mdDZGanLSXrSwS38UIxjbE2J4Q0jXQq00E0gAedDkJ1yNkv5N2TGY4jJJHALqC2FykD1iRczBLlsgkIwA9d4xYZCKQFonqZicNxIU3hcYsoiTft4Cr3yEXm_-6uYpgsLoOxqLgu2Dttsgc9zfWTNmyBYwIlST43TTlUIWlECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ExtZjYEWUG-4EoYUf6WN87VX339QpYYxFUy-rUD5DrVoHftfzbs2wL7ONlDoJO99ICVuXEaHpFKTxi_sSCQ2mRKJKqaSMRAqUva3HmZSZ4ch8qeRVnEoi5gJW4Ad7PF0sW_aeESJs59LH9OD72QSVUWIE3Y6_A6TO15rPituADFlxJvhRDEsdRTwxFRE0FvQ6yfBgfnNxqsb6dy3SIsrbT-prQRBnmik2kE3eucyRDiUV1Un9zOKUqHwv1phsZrgp4Ga0uLCT5bZDSngQmmpFCyGIXiMzbMyekmxILw7HmmPJ5y305CR6O2ZeTiZ6M0b7wRoXw2wOe3vBrNxe-SznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CcHxjNX2HXlUaRd0bgsVlYS8s1CtVuxHXpk4zwKF8V3AAsHzx9FjL5C3BX3dg24J6i_eOCGHAwED3A3ZAMBv5oF_yEpL_a6YgvFCEk_pt10i8zZvauMIj79kXSjOBeoUOYWgIduFyy1imZiiKB554dazoZY9FUw1KUUzqS7CWOkQxnSy8elksXBEBnpuewGo-oFAh68ptVw6O9mG_r8YhdIZbBEoXyKd6L21gvgjZcGDNg9FIQHMAiuqCrbkop180W9_SXjHiLd1R9xD_3J3zH2Zqf74kCrJpANLazL1W-UJOvsMpwLpmRGJPpj2WzewC9udx3YQRAqXIYAuP9chTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUH9AxLoy65iCZWOz-42qGzEwUW-5vOG0Ipg1vTNY1XHXzGKrLBtLaCw735DZZruVMKrmNLAVQ9Wa_Qi5_2RL_ehbtOm6IpMIM0ddMUxyMskyIxNEUwiNfQEsBnKLGgtIvYaxCFq6sNiYLkTq-u2EwoBVwi9DTs8PkmuRQLpjIItVz6bccd81UjQ-0R5kxt7bftvNFhGAnuNV6WiwY7Bw7qFLCmQ-qTgq4Hy4U_wSZPRDi3w5i8OWApyzdF8cCg2Ezayu0HQV9F4sceOTYZvWjSgw6or-WVuut-o9ECG5F9i9ZNmO1xHV9kEk5AOinu02bwNdjJG8j0vHklJWrd04A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67100">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=SbdfGkCkfeVsQAMrJD5VdKiMbV2Jp2Ix8FCZXldR9bB955CFd2zOLBkhT9wWHxLIz_1INHLu0fi4NIPkHP4B80VSAWWuBcJFZenmQqIzA_XJYlRCvwvde-ZR7MPJQIk2BpDcT-jJtvcLZXLDik5HkJH3IzHC587LbGYMe7uNhsTZq4jfhdPrX9QuboxYZr3Ssm_S72zhLT7e31PtMqVOtbbVRmV6rRWBTSXwn5LjBZCzqD-PINVdj9gCi0B4CdeIcH5BjPTD2fiJFA3dnwINZk7BUP43elW_eEP3cWWj6LnAcDaemBWxxIK_9dAHwDB6dsfaJKav_ZGKZdtlR28rhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=SbdfGkCkfeVsQAMrJD5VdKiMbV2Jp2Ix8FCZXldR9bB955CFd2zOLBkhT9wWHxLIz_1INHLu0fi4NIPkHP4B80VSAWWuBcJFZenmQqIzA_XJYlRCvwvde-ZR7MPJQIk2BpDcT-jJtvcLZXLDik5HkJH3IzHC587LbGYMe7uNhsTZq4jfhdPrX9QuboxYZr3Ssm_S72zhLT7e31PtMqVOtbbVRmV6rRWBTSXwn5LjBZCzqD-PINVdj9gCi0B4CdeIcH5BjPTD2fiJFA3dnwINZk7BUP43elW_eEP3cWWj6LnAcDaemBWxxIK_9dAHwDB6dsfaJKav_ZGKZdtlR28rhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با مدیر داخلی بهشت
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=YXSFN93OrmPkX82xpiecp_cAVuhknVa46gkX5WeMnkHhp54_mCGLOieLCX3dHmVjTnGm04ba0arAqt7zo7H2lVH3fofMZVB3985aSSipXWVACxFjalRP1CF9fsML2ZXHtZbipMxsGHKGbGlUrO0IRmfjyotyIIfjMEpdtB1eZ7v8cfZAKPWeUt85DAhsmCVp4DQLSQ-PmhXFo4JK-jmaA0IUJKxJRPf7pWpclbVvx6aamo0QaFNMaOHIBDxWjw_kqUajtj9DMveVd1R79terWSUmf6M7MsIW-aEExQwJuLl6Gls0QdjP-D5UMWQrgfaZjN6SaqIKNxrzpGMR5Sk1MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=YXSFN93OrmPkX82xpiecp_cAVuhknVa46gkX5WeMnkHhp54_mCGLOieLCX3dHmVjTnGm04ba0arAqt7zo7H2lVH3fofMZVB3985aSSipXWVACxFjalRP1CF9fsML2ZXHtZbipMxsGHKGbGlUrO0IRmfjyotyIIfjMEpdtB1eZ7v8cfZAKPWeUt85DAhsmCVp4DQLSQ-PmhXFo4JK-jmaA0IUJKxJRPf7pWpclbVvx6aamo0QaFNMaOHIBDxWjw_kqUajtj9DMveVd1R79terWSUmf6M7MsIW-aEExQwJuLl6Gls0QdjP-D5UMWQrgfaZjN6SaqIKNxrzpGMR5Sk1MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67098">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG46F3TFbI6UDrQm15UD2ysfahlc4b2oD1qxn9R_phGileOYz0Znj4AQjJl_KKPhUMvaYG7KkoShKY2tOasmPuwyPB5T6h0a7X0FXrl6uGhn1dnlWkcDkldZr60uhplujU417F8C1VpjXlK1SaYfAzdAprcKruNk75BUJQa-Gnad4ECt11P2-FSuTsH_L7TJJGdBTKYYGxKr6nqy74RONIu4-Em9Un_UFcThuG3JUOKwJGlk-EBIjnRsglMkljhbFDr5_SVae_-d-oEKT1wd9pWD5EoTYElAuz1H6qBSzB0aYkONsArllhDRE7Ztye555A-36g9BMzFfD4eNFsOL_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی حسین قاضی زاده تحلیلگر اینترنشنال:
‏ایران اینترنشنال نسخه‌ای از دستورالعمل محرمانه شورای عالی امنیت ملی را مشاهده کرده است که از مدیران رسانه‌ها می‌خواهد طی ۴۸ ساعت منتهی به آغاز مراسم تشییع جنازه علی خامنه‌ای اخبار مرتبط با مذاکرات و توافق را از اولویت پوشش خارج کنند و بر پوشش مراسم متمرکز شوند.
ساده اینکه از بازماندگان نظام می‌خواهد که چند روز تکه‌تکه‌ کردن یکدیگر برای تصاحب حکومت را رها کنند و به چال کردن رهبر ملعون‌شان مشغول شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmnW7r40WtC9swyYtpaNqd6YshSDlXH4lUL1qO_zKV4IC2TziIkOnQi31KpPKmqz40x6_66xGA0o3bFFb2QOTA_dA83B4oZnR9A8hI3HB_O_TQuUH8MwDBumA8qarVrTGPzWNf-vq-choKWA9dbHDEWXNaU6jxOLRdN3BvSohNGrJYXvPn5q2YurwtrDrRrIXDj2lr8qaN5sEJ8TYzyZV1HfalfRPFGda0ubjGpO8qBBPDZwBTc7l9J_LIVGwzNPxoHrKWRut-CSLYHy_i1eC4O3_C8SS8Stv_DukU7PvhzfEaJylxlMQimcP49Ad7G21K6zWUMJOpLaQaguroK3JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67096">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=gC2HUQv_QEPLCDL84h3El6meSV8vHltqfi8wfjKwVOzAQ2P9xl12TmmUjj0OeX1Nr3e6j490JB8wPsVgmvOvnPQ6NgX3pkPs9NzkqP74Ez-Hgr05Aoc0pfGwkeMAI1Ttcoljkl5GPnyxDVCMIpCD65__nvbSeAoODV190HP7HeozdgZOfD6MVIIaN3wo_ClXGv3itA9RHZtLpMxzS6a63i-uYfz0ADeiUy-xM-abnwA838bWIivSZSYq5p8wZj7BptqMIhB3K6mG4n3oNL_jZGvqdW4RzQR5fBJrHEa6pMcKlEqWLjx19j2FnPZBTdx_khIbJpUQ9B0lcmHt2vbNuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=gC2HUQv_QEPLCDL84h3El6meSV8vHltqfi8wfjKwVOzAQ2P9xl12TmmUjj0OeX1Nr3e6j490JB8wPsVgmvOvnPQ6NgX3pkPs9NzkqP74Ez-Hgr05Aoc0pfGwkeMAI1Ttcoljkl5GPnyxDVCMIpCD65__nvbSeAoODV190HP7HeozdgZOfD6MVIIaN3wo_ClXGv3itA9RHZtLpMxzS6a63i-uYfz0ADeiUy-xM-abnwA838bWIivSZSYq5p8wZj7BptqMIhB3K6mG4n3oNL_jZGvqdW4RzQR5fBJrHEa6pMcKlEqWLjx19j2FnPZBTdx_khIbJpUQ9B0lcmHt2vbNuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
مارکو روبیو:
تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود،
اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛
متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=iqYs4tiWJxJX4jVO5o2mYOpte0JA_5dwRBWdHSKWAT5Alttqzo-XfxEj5mN2R0xLbqpDG4HxDUPneb3D2EsiAHb5CrXVdiCyP9A3dLgwUxyvgtN6XOGv44ZP2bPrlvK61Uw4YQ3v9n1Reto4CjpuEGGGm4rixws17IvB5mejkB2UvsCuEBLPqxBqKzEGKGn4gc3yG7eKsCslQjUmMk2B8LoLDEuya0QTcWTvR4Acvi5fYFFaEYbAhcmKrbld-n3baZ1CL0cYHF90tsOW5yqq-JfIcpa6h5Canq0VHOwE5vw3fejRGv4WOAsseuawqCLZxMlULVop2c7aDNdDrXSfAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=iqYs4tiWJxJX4jVO5o2mYOpte0JA_5dwRBWdHSKWAT5Alttqzo-XfxEj5mN2R0xLbqpDG4HxDUPneb3D2EsiAHb5CrXVdiCyP9A3dLgwUxyvgtN6XOGv44ZP2bPrlvK61Uw4YQ3v9n1Reto4CjpuEGGGm4rixws17IvB5mejkB2UvsCuEBLPqxBqKzEGKGn4gc3yG7eKsCslQjUmMk2B8LoLDEuya0QTcWTvR4Acvi5fYFFaEYbAhcmKrbld-n3baZ1CL0cYHF90tsOW5yqq-JfIcpa6h5Canq0VHOwE5vw3fejRGv4WOAsseuawqCLZxMlULVop2c7aDNdDrXSfAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=L_Clt6vZD302Jugl3wAITUEMX4qXTr3L1vuMQAZLgWvS3nGdKbC3BGZFf-5gdqJUdSM7IWrIaG7Vi9UqwqRNJP4OJK8Dwcjs0LlSP3G9ZDJciPIyWrQDQcj_poRm2uRcNAahBNN1vqanA8FOyp9kIE_dfTZGzGDSXBBxuU8UGWWNPsxKS4HdrXojcYV50UckJlK7R5SjKFyODZToV2NCCXCWoWWRQWnOtcHM0eSZtTtYCD3xIhiaOppclDbyf6ZxD7FHnVb_9Oiw36yJMyjuw0pxsDClGwUeHz4PHMpJtJrxad76HktkGo9FKRNT0tnuzW5UInfo3rERKCg8_c4nNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=L_Clt6vZD302Jugl3wAITUEMX4qXTr3L1vuMQAZLgWvS3nGdKbC3BGZFf-5gdqJUdSM7IWrIaG7Vi9UqwqRNJP4OJK8Dwcjs0LlSP3G9ZDJciPIyWrQDQcj_poRm2uRcNAahBNN1vqanA8FOyp9kIE_dfTZGzGDSXBBxuU8UGWWNPsxKS4HdrXojcYV50UckJlK7R5SjKFyODZToV2NCCXCWoWWRQWnOtcHM0eSZtTtYCD3xIhiaOppclDbyf6ZxD7FHnVb_9Oiw36yJMyjuw0pxsDClGwUeHz4PHMpJtJrxad76HktkGo9FKRNT0tnuzW5UInfo3rERKCg8_c4nNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
