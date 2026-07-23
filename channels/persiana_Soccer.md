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
<img src="https://cdn4.telesco.pe/file/YOxq070t0dZpYCmQekig9NwpN2t5iSn8K0puPFdDOuw6kYkM-iX5o93MwX78NngB6NM0MupEDeCkOhrk1WYB4Ep8Rc-yVOaJ6FDhhaT6ueRmlY7orW8ZStiwUUYv7ixUXvhDlc9UMfQE8BtvR-xSGDGBDQjc7jdQoLo9WYeF6AxAaF-z1OMkR4Qqhu2K5Z8nRSM2Dy0L5uelWHHXnhZE5YUo8JYWLqvck9Z8d0rOXCwYU8w6OEMoPChu4YUD9vBRNMVcX9KpEDsQ52S2msuZDz1Px0NMuLaDWn9TJCL8_-QI8rf1wYJhWtQmu2EuEy6RqR3lI3NZkxsXR9gFJ9txaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 552K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 01:27:42</div>
<hr>

<div class="tg-post" id="msg-26381">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHTWZYFZ5zD1ZWnRzLkslwLxINTQZ_jc9Pd06xVhj_Xbe8GOLlVxtMRM9pJj5IJhUJ4E8RSYAiTdYCgqpUFeWsZ2ADrkwIc8dbbKHpvnnNcTyqMKvT_vs3eVm09YFkNqWermI9e8wRKTNEHP-4YSZl7f2ZwuYPH0HMWfndH9XYd0J0fZaQoBd3i7AAnxph7zJAptF9_N58oGzYSQQyZTrkQ_HR_CBTCyZPPHkRb_ptQpX0pVVBXvBmoCq2IkWq2jXGKQV0cKLeFWKvZ3RmSkY6wqeqzB8mHUlgLMV5-0SI9HvJNF9C19HIKfe5FlQGeJRAFOILX3Q8r6CxZ_X6btEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/persiana_Soccer/26381" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26380">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ire9VSPqBY3GYMldU21AOm99mZbtV328E5wFi9VR_lHNwCvP0x8KqXao5qSXEvHOCTDCW9efg5ERg_v8aaW2flwkSBCsHh1-JSyhvs0uguC7eRooEhciUe-cwD8BdU5_1bngb4ZVw_XySIfyCo7D5vueKR81qkh061JxRD2phIrcX_WdKWaELe1BOaEohEBTrQd7RnlXqIeiDEIHwAHPHDRUQ-bN0ZfgLwCtJ9yRwP4qNpWSpC8x7ng5AT2yURESofn8WtKRuXpClVFbimiQfebFQi0XsgqQ8jEBOvt1C6iNvLGKsxlKIgr2QugjV1nqNwdHRZugssuwLwrp4YuqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/26380" target="_blank">📅 01:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26379">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fyf3LVEK4iLlQ78XC9DHqNFO5l_1YZBB0iBCFc_5sAGHT4ZVj6YpDDY2z9uK3_fSMZ-X_a4n1s00rxJBCj0YB0K5U1qGZrrq8u2tjumo0AJDPibTVFi-eseEsV8z4qGzstmvBetMpA-1B3TM6C-tuYNYdlQV7-euerhQdEvNd5JLBqvklF9p7AFQqxRmNUt8YorZYGLRhWzPs4qjV98u7XIDVt0lABn7sq7c7OS7U63J0HgP0jiExFh0_EkAuZBlmBrNN3BeLoTT8AQshfWSdQb2G4oWtAY3akaotzbVuMzJetR4zSusrZ1MdfdsC8jKYEfGJxr7bNSQBHvH_GLrfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان ظهر امروز جلسه‌ای دوساعته با نماینده مرتضی پور علی گنجی مدافع 34 ساله‌سابق‌پرسپولیس داشته و مذاکرات بین طرفین نیز مثبت بوده و احتمال اینکه مرتضی پورعلی گنجی بزودی با قرار دادی یک ساله راهی این تیم شود و شاگرد محرم شود…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/26379" target="_blank">📅 01:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26378">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bhgzm4nNDx9pJMFwTUSJXPQtw9ygaSvVqYGPlY-fHGeQgdwosvE33qNg4DJiG6E2GyDV0Zg_eKLh-cwxUz1e0iE_pejaLejyg6KcNIC7FTKQPAjMSDz4szajrFvXqKFajmqtbgxA0BBHHsDL8DHqGsFtKJkAPE_U1or4TcF_gUlIyy2LpMXROvRiVX385ke_qeYh_BD6y6xDtwS4eEAnZMrchKI2PvnMxLKt1jljjdos0xyE8fOKuosfsWKdkbQ4iPk_DevXlm4_MawlzqpktxKBubaRzCIGkzFMM8GA8mva_O58yeqoyG14rKc7PaOEyzRyu-ACs-iBxBBjcK_C-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/26378" target="_blank">📅 01:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26377">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chOSnbt9t7jMrdcBmOuI4p4GWUVulKFcOzch2KNBcncTcYq8Z1sHh7HFIiObK_kcp3yCyiWuplOqcIN-ArygJlb0PXT8d8lL5uYts10KqOpLrGPzwhK7iI3arBnbre0E5nx8vO6ujHesNBN4a_FQLzcJq0Da1IK74A6hTvswzUYOrRLPCtMf3iam7jAOAvdg5_Y4icAFl-Xrvb54Z4tWtCMN1Z09WUvKNokcf1uSHvxv7FPcWnIbPg-unpECSBcj07L2tWTlhoqinjHzcHdvjNdLqqxjjqDpbruFWhR1PbYABW1xG_vO7CxqlvvcvMtRv8Pk9TL9rUVuNDzGPOYA4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/26377" target="_blank">📅 00:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26376">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a867be5010.mp4?token=jYWjwUze9EwEX9N-MAiScBfdzYpeZ0IkRb4M5_oRpGcsHQv78hb6gugnHl9w6KyCpG9AaNiNSHtgZqkDVtA5Nio5Z8SA24npmYuZ9UcNhmYCE94KGnh_ITVwd-o8fdxx5iY5wtwsohfL4W3oyZj1shzdPkSK5j3ARzLLKd615yC-GHs3JhDLLsrrH4DAJ3R2xLAdrurOuMHPceyLkh4v8y_1FvwIwTga43L2O0K7eyHvbQlWJOmcicm90zt9Rerfd7bu9De--3LX78MxXwxx6-mQu3FIjyy86Tyy76IK81z3m7mSui0sAU5pmYCOrzdq9aGxDLz7_BO0q4dqmfb0QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a867be5010.mp4?token=jYWjwUze9EwEX9N-MAiScBfdzYpeZ0IkRb4M5_oRpGcsHQv78hb6gugnHl9w6KyCpG9AaNiNSHtgZqkDVtA5Nio5Z8SA24npmYuZ9UcNhmYCE94KGnh_ITVwd-o8fdxx5iY5wtwsohfL4W3oyZj1shzdPkSK5j3ARzLLKd615yC-GHs3JhDLLsrrH4DAJ3R2xLAdrurOuMHPceyLkh4v8y_1FvwIwTga43L2O0K7eyHvbQlWJOmcicm90zt9Rerfd7bu9De--3LX78MxXwxx6-mQu3FIjyy86Tyy76IK81z3m7mSui0sAU5pmYCOrzdq9aGxDLz7_BO0q4dqmfb0QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/26376" target="_blank">📅 00:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26375">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=tReC_iqAMh2Dhcb7mr1R1z3sPDdxU2EDGh_J2unvCqMMC7TLnKgUd5x76CUKuu0Ipq-VthzLPin6cim4duxnnRu_CZTvqKk5DlOge5nNl7y4ESH_orx02oKGmmKGDNYNBc2XFvRBEOQOZd7T_-y2KDLKYExBRyQXBp0wuGzPqNUrb4LfglmPIkiJUzuPOucdVpRIEli9B_yaW2wWFxN5dmjY9FOkpt0_JLtj3xoBhC6eDGcNUQA8e9vAhLDCMrt68NtnqMMtQ5SyVhqpCsat4drMsVzCMi3ABXm4feQ5FTz1DQ00DSbat8x-wI_79CX7TwfSzoS48eSCLCfqSjT94A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=tReC_iqAMh2Dhcb7mr1R1z3sPDdxU2EDGh_J2unvCqMMC7TLnKgUd5x76CUKuu0Ipq-VthzLPin6cim4duxnnRu_CZTvqKk5DlOge5nNl7y4ESH_orx02oKGmmKGDNYNBc2XFvRBEOQOZd7T_-y2KDLKYExBRyQXBp0wuGzPqNUrb4LfglmPIkiJUzuPOucdVpRIEli9B_yaW2wWFxN5dmjY9FOkpt0_JLtj3xoBhC6eDGcNUQA8e9vAhLDCMrt68NtnqMMtQ5SyVhqpCsat4drMsVzCMi3ABXm4feQ5FTz1DQ00DSbat8x-wI_79CX7TwfSzoS48eSCLCfqSjT94A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
عموپورنگ امروزتولدمادرش بوده که هفته پیش به‌رحمت‌خدا رفت. اینجوری براش تولد گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/26375" target="_blank">📅 00:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26374">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxup1R6uOgKsGrqptE3kRRbBI-fJ6ss4TJsnXNfu3rtieBoLBgyYZngo2jP7YzuqWjEUlfAW2eGOlmh33es47WoxYivHAH1vtkJPmCc7GwVP6qqqbvBvKel-xJqSP6JBLX67KInz78VcLG1IowsMY6L38RcgzhELNg9o664gPLCrTePdhNa0PY12irkQY4_riljRwvgI7erBsoMXQw-6AFvsmbVskK7ry6yxApRJMqiHZfxZ2KnOi2pkBWamffrGMq17QbPaajTAZFtIxQuSR0wttjzWafpIGrzFNmUzTV6Ak3Mg4LPRt9mPVFb5jWoJ5FSYR54Fcn6TRx-FRSEA2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/26374" target="_blank">📅 23:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26373">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOaozIsvkTSsCcY3W2hNl3EH63tCBs2QJ2GDkfnXfyMts518coiC6ZCYRmyM3xLk2Sqr4g8FYwq7a9qusTzVlA3lFzOslPnV8RB7b6aKb_WclSV3xjoX9yBdpvzaHD2lVgJppRnEGiyYCD1kYKuApJJiN6n4msxxsuGxqTnOx1Zu3OkFUk7209CG6DP0KHOFCYL8AiRisfNKlp2ppMVn_CgZXMrFwmF0sE-XeQ8IgojVf3uBszjLRWZx6ny3ieWti0B_MiB7Sd5j06tD4bHwDmKYC-JLIOm6PspsgONOuLVCyUvlkSpiF9Y66OzNsS9JTfdZgnJpyZWWuWk-LBmJ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇷
برونو گیمارش ستاره برزیلی نیوکاسل بزودی با عقد قراردادی چهارساله به آرسنال خواهد پیوست. طبق‌گزارش‌رسانه‌ها توافقات بین طرفین انجام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/26373" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26372">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uuh6kDsCfZoHAXKekzCB7vxvitITaKsJe9WldhQVzyM0lXeVcq9tlS0KVRJOlOQA5igFGynGfr0Y-7tvEHjt7cWSze6f82qJXYYghpZG_Rv3A2FrR7kdt1tdR8jfBxxqh-bEmCiB2Dltvb5n3Cb7CF-_iQmFshZtUglUFPzglsYq3JMZadMJzRgeLgXWiKskqaU-v64fL19tx8_23VW_t58UyKzGZR2WNfPgRN6IgNlVZAusLuGP6VnYv3zVoniJQ7DNs8wN1R-NTyQ_lcmwYhbeDDU9HrV2AJpIiiEGoLeGMio0QUhHsVPHrJIzURR0lp8sf5tu1OFs7adwl92g3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری به سران منچستر سیتی اعلام کرده علاقه‌ای به‌موندن در این تیم نداره و میخواد در این پنجره راهی رئال مادرید بشه. پرز حاضره برای جذب بود 40 میلیون یورو هزینه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/26372" target="_blank">📅 23:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26371">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKOpHwStnorTiK4Z-SiQk3FqSMhPZj2KkaObMHwuXKbM-BtoIRixA7FNWDCNeymbMFp7THu0M8K1UuAN1Zo-hWv2Oo9_uJzjuUeuR8o3jhaKOKXHxrHU0szKu-XGRb3xDcWySelafIePI_hdX-z_cN2bpDsq9hQqa8TERvcnd9Zqat32TSBtowqewfrdOzspALGFRgEcHucS0SIWbdkFf7xhuArxAIe5wqtx9lLOHeEYeojC8mnTNFQkbml_gMSy-t-8R2DwbR3w4bNf5dgikTxEmi9p4wtTbhNWq8USU5IMGbvwsXgDJyOd4Io6Za3uuMNfIRr1mUkpIOy3cJ4QIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/26371" target="_blank">📅 22:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26370">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ0v9ovUfAqxqcvK8roBfrKC3L52A4UjnoWDdTInLl1ulSAJrq7uuXxUnftPpl-7MU3M0Tlza3W-sNLFG53yKIsmOOUS06xsU3DcjFzWkWUM7jWujsJQmBYuAckM1cHIa-5BGv2upVzmkpaUj1p6Xb5gKE0RS9QXlqZ7L9MVV35IV6Rn-BJAMTpCn-NbbpGypY1RSz6PbBKTflArbn3noadlODambS4r2ahEOqv7Q06Z9WAPgueWqrFKC4cbh-aGkAe3SuIMJx5wFJ3viBK5P-s2F6MuIPACDZ_4_0i6q4nmctjwhd1L_TY9NTNXMVl_knb_tId44kgZ4YB5phiBLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/26370" target="_blank">📅 22:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26369">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZeTN5MrJMXgARW-TzZznfoYxqIrvBIIlOlSGc8scUPfI8-kED1v8dFpLJXDD7oqLx_dK4Keqgbi8xcVzy-eVlglEqwRyggo1ZgAQNKo5NK018vffRkcx6mmmz14N1ExxERRhbooVSLi5zUsGD3CCIfvbCZOew677OO4i0fP8hzn0eKy-21KBt_MTEb2mBqRSHf9JrN49ZdGBbZfDeOpgZCxNTy9A7kOJvYCBwoY2gj8y2AjJypNg54ownPyLvwobMkqqlUWKNFmOdeqzI0XBtRpj6YpRBuH1eUKLOtiq7gCFIswvLddm13YwH2zhbfI7Ddm63560i_JiAnsh2ADAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
مرتضی پورعلی‌گنجی‌درحال‌انجام‌مذاکرات نهایی با سپاهانه و به احتمال زیاد راهی این تیم میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/26369" target="_blank">📅 21:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26368">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5Jg4nNuwtWZ7HOpObUjAk05EC_1APtmdRdugAydHI2RNvFsDsNSO87ejxAbTdzaSeFfGqDWhqukqyZHg0SPEwOI_oXndmseMmuIMdQrzza_CVqxsPCZCvmAzOfLVOqdTkjn5kUtjIbNMEHb7VrdgpvO6bYyxcA6I2uK6HY5Hr1Q5EpvOlDaawoNY0wrAFSSx77TXOYrrEtfBe1g-sNRZLNjH9vjxyjrj4QVilzm9qsXFoo7L6iRsN_DN3Nc4Plb7RJxaxWII5R12Yppo57xuNLGaYZoldqdeuDHWa99qVUBKRan6d2dKpsE3SgvD7ce-WQEInMm7nAdOBhak_qOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/26368" target="_blank">📅 21:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26367">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdFwBPAmTSiZEgpavRRZzWR2na5_l6A7rkW7OegCTlXpaU8po4ir_Rk4OsBUJZdVJjycquv94I8oUq3aguXZLzvBhi-n94fW4bABu2UOGzeK5hFzE8Y1ajCE68UyJPHWpMuVNS_CZpmYfpkc9Pa0kjFktZHHHeHuqKU7mxosmgUAhI11EAe3_r61K7HoZUuySDW0rcMdOAcsPbWy4HZnQmgMd5grfzxQsec-SR7fMnRZn0MITF94WsV6-wGoR3iEHLNCxK54ieZMLY2UMU1ikzTK0tI9TyyavMELqJwSuni3-dkjAuF_672KYiodpIi1kSXoODJglIjcvr7Q2Nze3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب دوستان برگردید گویا کاور کیلیان امباپه فیک بوده و کاور اصلی FC27 این خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26367" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26366">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=tyHMOQdAWycA6sTyxlHyo9ExOYKLa7ZW7L_g5yJV6H78ysInXpXmqdwVPR6D8op65f05PnsbUKywglaMwWOGrOOONLVVSW40_NX9lUPOEwjQSK7XdjIr_41M_5Ky5lCFzGWNTmlnnM30Ng1TFX_9z_CTJFmGiIKe0kBQo7tZlf4dTRIg9tydbyvc1FzY1TbOvxXnjt2iEl_BZHWSMcYoFeKfIWXfWOpobnmb_JXxZbJTJtk1TEcQfIb9GoFdJIjONRQo15LjVRICakaCs1FdkozqAYmKUbdu0pRxcaFlF99qKs2LWn7UvQ94F2d-b6Y6qRP5bMvxVz8eltNSz8xzi01I6pIOowKsPEEPARZFj3etff2UlV5FN5IMN8Io09KDibO1MC4eof57KmP2roqcgwQ2AsgE3muEwndaFmGi7H1LxPPC1FXnAMMNb7FK9X4o8p52umCWZnakGg7OeEj_q0zVdR8CoYEJ4oo5_ZpJmkENi8yMMMxeZ-WgdUCGezuAi_6K6V9TcJDoldRw3kg7V4OvbGHjC3SjucAOqfEbbIRvafrMngWJe8OVPuZdBasz7mBrmBC6loFkdVh1j-5ef8GzmT3ZMRySPPGhG_dX_Idej9VtmIRqW2Hd5nC-9tug1BhTCGTlSyw8UjTOfvseaM6ujggT-82ZWgWtXFadvBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=tyHMOQdAWycA6sTyxlHyo9ExOYKLa7ZW7L_g5yJV6H78ysInXpXmqdwVPR6D8op65f05PnsbUKywglaMwWOGrOOONLVVSW40_NX9lUPOEwjQSK7XdjIr_41M_5Ky5lCFzGWNTmlnnM30Ng1TFX_9z_CTJFmGiIKe0kBQo7tZlf4dTRIg9tydbyvc1FzY1TbOvxXnjt2iEl_BZHWSMcYoFeKfIWXfWOpobnmb_JXxZbJTJtk1TEcQfIb9GoFdJIjONRQo15LjVRICakaCs1FdkozqAYmKUbdu0pRxcaFlF99qKs2LWn7UvQ94F2d-b6Y6qRP5bMvxVz8eltNSz8xzi01I6pIOowKsPEEPARZFj3etff2UlV5FN5IMN8Io09KDibO1MC4eof57KmP2roqcgwQ2AsgE3muEwndaFmGi7H1LxPPC1FXnAMMNb7FK9X4o8p52umCWZnakGg7OeEj_q0zVdR8CoYEJ4oo5_ZpJmkENi8yMMMxeZ-WgdUCGezuAi_6K6V9TcJDoldRw3kg7V4OvbGHjC3SjucAOqfEbbIRvafrMngWJe8OVPuZdBasz7mBrmBC6loFkdVh1j-5ef8GzmT3ZMRySPPGhG_dX_Idej9VtmIRqW2Hd5nC-9tug1BhTCGTlSyw8UjTOfvseaM6ujggT-82ZWgWtXFadvBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/26366" target="_blank">📅 20:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26365">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unGyYLy6hAegd0GC-jM4ifYQqQlkZZzCb9wncQTe8psRzl2BzsSAFMoVvEoJwByGWwHoyBcJdlggTQMdrOTY1lumAG-Js9D7jhAm6qjtO-GB1csbCwnzHMtlJN0ERNFbGCBSHXOsCCYsQHI-H8X3w07DV0okDGKgw1oto6FD8s8NYdrutBDvt6OEY89QnQHjg5OUB5yL_0zfDneSOIY956ixyOK5Er8Sp0u5VciecC_InVnAMMEH0wCJrtgMQFo0cX2t2OdjF60eOd40jHkGuhAHt5W8HTljr7AeuUHZ752nDIPdcDz9w7iJl3z089_RHl4fHf3NNsjLbr_XTk6ehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌جدیدترین‌اخباردریافتی‌رسانه پرشیانا؛ باشگاه استقلال شب‌گذشته دوباره با وکیل ایتالیایی خود ارتباط گرفته که ایشان اعلام کرده در باز شدن پنجره نقل‌وانتقالات تابستانی آبی‌ها مطمئن هست و بزودی این‌ پنجره‌ باز میشود. چیواله وکیل ایتالیایی حتی به تاجرنیا اعلام‌کرده…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/26365" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26364">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De9TkAfOOzAWELPk8s1n3Bpn-rH3M6TAmSpM6DvFF_mDnNjTYOXFORvp4SFJ7S22uH6gTaANKFEvGyaNmMf90DoFRdyFD9rYXt2J-A8EWQngkQRvFPmqAvgkU2XZmkRK2qM0fs-0PVnvxVg9pCV0YhJNGJYmxyPBVueROIM1uHvPmZam1CG6BEeosxPSnh3EU1Uk7T1nzDvch8a4HGQf-0WDH2N4RBxbmWlXnlt-crKzrgCGlDBwfDqy9QQxzFF5cUWBQtCZMlU4zLMWiR7NziBsDPCYtQZYnnav8BVb9CiHr0aaIBCsXJ1lqhdzBfIl0WDmTThLBgGgiraJaB0AeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛
فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/26364" target="_blank">📅 20:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26363">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bwc-7qyEft1wT-ndxx_hdiVXCU0qBnUEGoxI0WeZ6DX8gpo_OdFnxMb0oH0SPn6vAsZzpyYRxn07UM5ZR_1Kll5C4uXFn1_TOSEiNJytzTz8nvnw3HICAIwgBDPNo0PbOM-LV8qHeN1w2moRgs6YX-WvqmrPSD_iJ1Llo5CHBdt2xvm6VIbE_oaCH81VP1u18fsIFF87e0YnEjg6bgHTI5Zc_x1EyN-5kKj8bBFe8qhqPzNksleGEhzm-MnhfGMJEVGe2y4i3AHcvVhbZCOPn1182OuBEHDhK8WzcVGeM1lF9mADv1iDUkNAShR9HqC3xh-Zx-4oF87zkNY23yBtUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ برخلاف ادعای رسانه‌ها؛ قرار داد جدید کسری طاهری باباشگاه پرسپولیس قطعی و چهارساله خواهدبود. فردا هم قراره پول رضایت نامه او و ایری به حساب باشگاه نساجی واریز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/26363" target="_blank">📅 19:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26362">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎮
دقایقی‌قبل نخستین تریلر بازی فوق العاده جذاب و پرطرفدار FC2027 به این شکل رسما منتشر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/26362" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26361">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5eIEcnWQA65ZIy67PMpWw0HZnTE9hCnE8pQlf6JXJAuSk_YUw-e2_1AFXGSmjIeghB-LsQSdgnAxPL8ZBhgs-u_-accrEXlyVAKdZD8UIfXn--5X-kxSWnudiPIIABSgq9X2OqC-t8F6zsh7IEFbP4FpWoaFgkV0wmwOoNjwMhEUOEsA3V-G7eL11qj4lKo3MP3rjxqYTvy0HQZz_gdGtrNgtuJpJNDQCunwlQBRbPIjzYuAhDcEXdDzV4JPUTpNTKBmQk5CeqPuzfphG4DjFa2fqKzXgiaQWDPc4fPsiEzGLevtlNuwKyb1DakPfyvivAR4Fod7Vcu1JrodEPfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/26361" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26360">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_dIvFnbwakqCFLH7qW6wvDzmdsrvW4ykxVMshkBi14eLfeUQg3h2wUAGYN04ON9Cr5Erx8MHNJSEJUBUNxpl8gkJdHjtMR0OWUhBRPtyfIP6vcAIq9JnApU0iW1WDSzPSAa39Mon1qsg3pdht5bkZCQb_bRLPixBupO8nNe2jWvAVD04e1500O2Uy-4I9sEbMTjJVztChlblPiet_eDrSPvcvlrY-eWk9kI4mMYwN-b7Rqa3erVsSi9Fun2EVv1Xugmk7WlGsNwMTPtGTYVYwY-AugnsKJw52HewUTw7PocsTFYVIf4PoYQVrVeCFZGze818lUXO_XspeJr79olWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ باشگاه منچسترسیتی با پرداخت 150 میلیون‌یورو به باشگاه ناتینگهام‌ فارست الیوت اندرسون ستاره23ساله این‌تیم رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/26360" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26359">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1c92XWqokyFO_vcLOjnIm881no_60acVTJMrVFl162t4wksD-jb3kc1YVOtyLBGkLATeyvqb_ySc3gTwTeZXJ02qdqVGamBYK1-AYhyraKmMrvMQhGs8S9_OmNCoaRU178FAMMT8LEbyXKsfB9w5ibUgmgcxFBX6NH2Qvtq6fvMPWSmzqbOK5J0xC8xTkoOMPnbvLnSaZfGL1rR1wsMGtAPk5KdT4A28amamqq48-PJWVN3i_3mJ77Hx9yL96Cl7skg6TH2-kcQ0KyDgSncmM9YutT18puJABT0Wa1HJJyZHX-YPkGJsJR9uGgwmtslFhT3v-YCyHKoPQWfuqvoyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/26359" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26358">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3aD-yQv_td-0dLRb9X9WPIU1t2oNZLJNoCX24ahDb3HpNmX_Oj7Wpn_MSEMAlFDF6BG8_5JFgREiLi9ZTMf2_0X43eXETJK8Q2jD3EBJq97ayIGPGcy43jXH-PfNqOxrDkBgrFc2OY29Zuuq3Gxj8KuHYYJc0l21B8w7fz2cva4xW2PjkRherWaBAFX4mO0q4bcqmd-z2-6WElQRdxIk09FH5ryCly3Flwh_q_tFSk2_7t1BqFbx8h80Q9zxG6-eZcYXqZLOyb0RMDyqA9wlKqpHR1HUhevAzQHMLH4vP4FZYbAAT-TbOwcAmaVyO2Q8Xf-HoyrW8k3LWGFkn_p5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/26358" target="_blank">📅 19:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26357">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqO2jwoK0cZc3hik18ZHZRy7TlgkbFS_OG1KUxBxZdjc6o2OY14MOWGbGyN-uUU7GpCNeha6OQRyhxtvc56EYvaExFG9CPHT1ZWVFBUETuNN0313Q7nvxfjLeeIxoGOV9nJ0kIfftFKITD7CcO5wyPqwFYAoiSteMomWVez1Ys2Y2cWEMRb3QoJT_cwTJ47_ZZoo3AzSozFObHeW-EPnhgbdhVXrs87JSLHYySMZzHcAgceiRZGWOSOrn-BUdhRBHUdKhvH7DAtlQXYUHG8eNgezi4XTIs9F43A-hpbQg5QcoXAc1WGc_CPR5N9XzoD86xhOMlRjDnuRmAaPvtMe1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو تصمیم گرفته بعد از دیدار با ولز در لیگ ملت‌های اروپا در استادیوم خوزه آلوادا جایی که نخستین بار فوتبالش رو استارت زد از بازی های ملی و تیم ملی پرتغال خداحافطی کنه. خورخه ژسوس میخواد رونالدو رو منصرف کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26357" target="_blank">📅 19:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26356">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=kgdKe35U1HTFKrfD_qYsgKgMrDL2uNnldRbgc4XNjAV7c_LEMDaYsqTi2wCuz3nO85Kloxy2lbzg-tq5GoEyUBbj_Io5Ltf5m4vgRfO6LBMjXqMSQ1w4zSKOwl_HYFto2peTJ3O1FEoUcaIcaf-Qiz9mWWab2O9kGBQt4aJIW7RRS01gOCamAUt8ff3N59cIIueZWQq4m-E3q0npHKMg-eStc-vjpYtAjIzy5t9JCP9TeDFYM6n992_KNjM4dwrXVH7O7XIM5Ha9UT-Wg4WFYlW6yn83DpQW_7mYh8qTUEIXHl67_XvFpCg_ORT4KLM-umUEiUkyvd-7FTucIgKzjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=kgdKe35U1HTFKrfD_qYsgKgMrDL2uNnldRbgc4XNjAV7c_LEMDaYsqTi2wCuz3nO85Kloxy2lbzg-tq5GoEyUBbj_Io5Ltf5m4vgRfO6LBMjXqMSQ1w4zSKOwl_HYFto2peTJ3O1FEoUcaIcaf-Qiz9mWWab2O9kGBQt4aJIW7RRS01gOCamAUt8ff3N59cIIueZWQq4m-E3q0npHKMg-eStc-vjpYtAjIzy5t9JCP9TeDFYM6n992_KNjM4dwrXVH7O7XIM5Ha9UT-Wg4WFYlW6yn83DpQW_7mYh8qTUEIXHl67_XvFpCg_ORT4KLM-umUEiUkyvd-7FTucIgKzjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیو باشگاه بارسلونا برای رونمایی از کریم ادیمی فوق‌ستاره جوان آلمانی جدید آبی اناری‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/26356" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26355">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=Fo6UXcc_C_Q99PwzYfF6yGXFDytd6aRjcbzG_bho51epeK0vR3kNRa70O22MXvqV1UPsc-qsYoszcLoBDCWsq8YAOZ8QaC6k8Cs-KV-UoOp8W-nYT2NHhF5bHt1VxK0SGy_I-xO41JvM75ToqNHwhgLmqOTtYQPbTmu9SXQw7mSleTtSuP_4P-vu4h6n_0iDU7NdiR7vDtksXgXV55o4XoAW_zwo-ezqGuJqUeXbH8VA9Je69rHSj4eQc7GTFLCn0UtJqovHi1Io-GXF8cW0jm20Tfxzp3im1PBWoC4dPgn2YngkrgCuUaQEI5PQh1H0IksSZxsBoDNnCi1wmwUC7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=Fo6UXcc_C_Q99PwzYfF6yGXFDytd6aRjcbzG_bho51epeK0vR3kNRa70O22MXvqV1UPsc-qsYoszcLoBDCWsq8YAOZ8QaC6k8Cs-KV-UoOp8W-nYT2NHhF5bHt1VxK0SGy_I-xO41JvM75ToqNHwhgLmqOTtYQPbTmu9SXQw7mSleTtSuP_4P-vu4h6n_0iDU7NdiR7vDtksXgXV55o4XoAW_zwo-ezqGuJqUeXbH8VA9Je69rHSj4eQc7GTFLCn0UtJqovHi1Io-GXF8cW0jm20Tfxzp3im1PBWoC4dPgn2YngkrgCuUaQEI5PQh1H0IksSZxsBoDNnCi1wmwUC7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اسپویل‌از نبردتاریخی جواد
🆚
خداداد در ویژه برنامه‌رقابت‌های‌جام‌جهانی2030؛ جام جهانی بعدی قراره تو پرتغال، اسپانیا و مراکش برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26355" target="_blank">📅 18:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26354">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWxmBggWwQznbBepo12YLLjelbnCb8_hPGWlLv4mxlCm8eyxPWE-Fup52Dh7xwlt_2MNU09MgD9f9ag8CuR3DekXx0WQaHDy6x-nxj5E4VAx5PS5DrvFJWSUhCc6QUNWSnyIxPiIyY2i5GkLRdARYzndOUGrO07ZjEKEmCFyDs3_aceDPOqioncQOGSUvOx8KL9eS9qIWlXM5AWiaasqgwzqfjGZ5vviXWBB9hkHv6Zp2S6V200GLKu2bzdiO-POPzOoLZ4klWFd6_jcfBmWqHwo8Vz0p7jo8nV84m6PY1E4TDDQ4o2piifuFtMnXGws8vhEEwijGGkbMwrij_lHpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/26354" target="_blank">📅 17:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26353">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3hsx-5lUESpKLQTlj8idWdTVFXDTttmCSflYHDt1VR3pW4QHnEu6Ww1cbq08CeE6BASxRlcPR6u8fcxY1dBfr3cdMGf7p9zJmim4TUKdi0BPkzD0ArX6jWQua1cnvbNfrLzTPbdHaC_4kcMC-Ab-gp7JjeqcixIFnK7Y8YtMs1UrbiPiIavuFhEi2MO4By_cckpWTZuGVK8TcLOc5c52CJ2x6cQzF2jGqHO6jGUA4CTlYNqUg5tJ7vBXo53s5GJ3GbGuVz8lXroHCHl4J645xR2KoCaStpWcHEHdZmUlMQjvxvj5-dLpQA540KTD_ci5r_x7P2DWMxQfoyHWSUc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
بعد از انتخاب یورگن کلوپ بعنوان سرمربی تیم ملی آلمان؛ درصورت توافقات‌مالی باید شاهد حضور پپ گواردیولا روی‌نیمکت تیم دوست داشتتی ایتالیا باشیم. چه‌پپ‌گوردیولا چه‌روبرتومانچینی بیان قطعا تو یورو آتزوری باز پرچمش میره اون بالا بالاها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26353" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26352">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgHSp4FQPT5edCGRTVBS4QeTExlLZg2kkiMvoQDm2_uQyxSODprtlQzd-pCi6KasAlo2-Sjn9XQBV7v_9JOuN41texcBtD0mxF_3NPzGZlgJlf9ewYGTkwyUlewLYA0NcSRCiBzKeQZEY3foULEt2hOzOu4rYOQ-3eiA_qQg2YraEXsmBFY9r5VKweY4xzv6Ecgewu8ELjD4PLf9XSMs7cYpjOyjjmGpPWYI4f4khLuzR8pRp5hz3ibNsetVT1slA2rPIPOYMKKiP9x1OhEbkfRdhhybMmvNDTLHmiDaHJd7wHeaMc9ZTVfjJyNzNI5yxza-O6XjFafkSXQNit4u4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26352" target="_blank">📅 17:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26351">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voXfS-YhRjK86VpLbhCrWjLv0xUto9kt6PSW4f0w1YFa8cqfnJVC2FWSw9iSCD5K5gX8EDSz1VDmUcpSZYckxN9sTggw66OAo7EKuKUTzoQLw1yCaxGGHjI72SVtnBNyrZ-NtqcjDCG54ocXjsm2MgoM3e8FNMYJp8CsAsETzp4LN6AHB_jgapucI3iFqwigWBJId57BWwPRq8EJv35KbsM6SEgsab6KYdqhEBLraKYksZGVd5noXwQnPOZH_8si0dvIN4rOyrC3gDQgWs7fGrbiT-hxZqs_XN062NlQzuL8p30MthVhFoprZn-FC3-Rs3lC4cAB4KOnkH862ZgM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم دونده چینی‌به‌اسم لی میژن، در هشت کیلومتری پایان مسابقه‌ماراتن پریود میشه و علی‌رغم درد احتمالی و تغییرات ظاهری که داشته، به مسابقه ادامه میده و ماراتن رو به پایان میرسونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26351" target="_blank">📅 17:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26350">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMxXLjP7tuytREexuB-ZsYJ_AP4kYCbL_4hqS5ywH7X1rs9yfAOHQ2FUhSfGXiw_M5YxY8ubwh7ZY5s9ff_DJXaB8OGvPIK-L6gueY_6Lp8C8D6TSrima8xIH0iTQOB3wSRS06cjrCImBP8iE4Uy8HfQKB6dP8-IabpwIsfSR-Lk3w1IL0tnvi8pSydox6qlYfD4L6Iz7toQLOo7csPZMQyFtpfinUyuXyQu6EKbavmONuC7bvW2evFviyfRlsYTWxpuXBlTb4K5y3Fn5uytp2yghYU_AAbqgpbdD_ku3OxGavlxdswnzNE2C2z_bTckheNvgrCRuwojdDgoDvFxTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇬🇧
🇫🇷
#فوری
؛مسئولان بریتانیا و فرانسه در 24 ساعت اخیر سفارت خود در تهران را تخلیه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26350" target="_blank">📅 16:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26349">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjjI4Sz79ysutr64hbWXUgDLfRV8pKIPaj7jOmtST5EI0FF9dbVJScNZgfn8EIDDkxd86CzXkXxkAeXeyOUd4pKtMX-CUwT5XLjaNqyPt32-shXraFYebK_PiDPtez1gaklRx4xvEfoCrUBQePCr5Vy-LXnyRhnQUobPM7M_BRkaP9tSTtWfMJ06NRH-Iz-vrCXoVWjJ-NFmI9zP-xbU9orxrcihpeTYSJBuEtqZIvP1aVrL5xTG9fSQI5G41y6TDX5SwYke_K0UVg4--4kKPz6fNQF_iEfyxRew7eqoS8jbBAkTCI5o1kzuw5CIe5sbJ5QjjfWTrNIyhNKRFfs55g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26349" target="_blank">📅 14:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26348">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJFb7yQgoTuZtg50X1f2eXsWSiBQM-l4suzT6WYQvpGGmfyQnXal3gyatBAFkg7CgxrAImcA9iRyt5TYOhE_NW0f4RFLtIoN9hH1l-O1pM3L7QvxKCLPAxfXlC2Y2EavJP3dvwKqC0iQiNHoqK_NmoMGurZfNss1k_79mwcM0xOkbLE2aHy1fO16xMEKYAK-xPiJG39_Ee6n7fTitxI_XJTHRDe5rBlgRHB-OX3Uv7bjxy15cBM7CbVdaOPZHL6em9RlcvqqJ3outtzMEweeLWG3ON9a1R7z6wYx0FdGN7hlrWNyAEKDqToiXslBUVAToiaLeVqd_hbaMqaskJtnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26348" target="_blank">📅 14:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26347">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=oBq67LJqkBl8nD_PZcFwIzbimLlgVt4iDVz2RGFWLyALHgEMdT8hDOW8AIv22gOOXBVx69T_t61fVO4mE2P02HdkJz27FxZBhxQhdWUPtd0ujmcZ-Sq7CFfO0sP1_d6Iy0C5jtpngm9C9s6Jiw_D8gX2HHanZ6bUa1NQj3hWkIvBENh8pxCp2N27Ug4s-aUCLtR0RPQU5GydzPwc4pPZfMuopXy0jx3gkFYAyeb2gU9hArJ_QEgK9EZkoMZo9EfgFaF5olqXRINq7YpnjdIYQNMo3l-K5HCagPfI8Hwv1F9mXDfM1uYJXfzHh4yAtrhSdISuQLqplA_BrOqtRqJ_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=oBq67LJqkBl8nD_PZcFwIzbimLlgVt4iDVz2RGFWLyALHgEMdT8hDOW8AIv22gOOXBVx69T_t61fVO4mE2P02HdkJz27FxZBhxQhdWUPtd0ujmcZ-Sq7CFfO0sP1_d6Iy0C5jtpngm9C9s6Jiw_D8gX2HHanZ6bUa1NQj3hWkIvBENh8pxCp2N27Ug4s-aUCLtR0RPQU5GydzPwc4pPZfMuopXy0jx3gkFYAyeb2gU9hArJ_QEgK9EZkoMZo9EfgFaF5olqXRINq7YpnjdIYQNMo3l-K5HCagPfI8Hwv1F9mXDfM1uYJXfzHh4yAtrhSdISuQLqplA_BrOqtRqJ_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26347" target="_blank">📅 14:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26346">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWagqnPWTc2Rgnz37aT8k3zGW4d1jGTmGFZ8aIBdnKLNywpsxBMzm5ruXOWctfQZdfNghkhiIaqThmiqEopC-AbRrqvP2cJMHnkbL2WJmCV03IEmtw8BhdBeQF0WtPlSRVbSGl7Q6cmVjwglgNRbZQzD2s_ayPwElYqFM1SwtQjF08X7AfneA-yb2TiBdRgdQzaM93xjsShm9CtK3imDiwF0PEE2S545TUvwancZBhRhq__XFSq3Y3t5gjBUHV9fwlFEh02jwT6USsRfbyI7_0FIQH_TCwRuc5kqGSCfSfK04aZs6zFPxGm1mLTluq8Daa6IzOl1k7E8X0aPwXh9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26346" target="_blank">📅 14:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26345">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=lT9Ff4vYYJG9f8p2HWiVKKJAxp_A3bkD0nV1ij_AThBzUJlG7UVsV5odkh8-KEgZK7lsWFmSfNJ0DX--3aqFynhZ0Gr_KuBt4E1alY7uLWvo_oEcku0Es_HhtyNnd-1fe6oJMOW8UTqAyw3XJwtDnyCuyBAyeMpGcrFJKsLbWjJo21y2Or7aAqRjzG6ppeb8NtAeusM2rNZD-GD2wZ8Z9rcUF80w1b8tbjSh9k4XjWOx4rNCqw9jPyDbtxZG4xal-2dv1g5g-z_SJYXQmI0hpRDJovObcqFTpSyEMPjN29tCT5chJ_DCX4CaRSliSF6WTeD_4lSI8SNt5b7g_yHORA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=lT9Ff4vYYJG9f8p2HWiVKKJAxp_A3bkD0nV1ij_AThBzUJlG7UVsV5odkh8-KEgZK7lsWFmSfNJ0DX--3aqFynhZ0Gr_KuBt4E1alY7uLWvo_oEcku0Es_HhtyNnd-1fe6oJMOW8UTqAyw3XJwtDnyCuyBAyeMpGcrFJKsLbWjJo21y2Or7aAqRjzG6ppeb8NtAeusM2rNZD-GD2wZ8Z9rcUF80w1b8tbjSh9k4XjWOx4rNCqw9jPyDbtxZG4xal-2dv1g5g-z_SJYXQmI0hpRDJovObcqFTpSyEMPjN29tCT5chJ_DCX4CaRSliSF6WTeD_4lSI8SNt5b7g_yHORA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌ بدونید که‌ چرا مارک‌ کوکوریا مدافع‌ رئال موهاش بلنده؛ پسر بزرگ کوکوریا متاسفانه اوتیسم داره. ماتئو درتشخیص‌چهره‌هامشکل داره و این موی خاص تنها راهی است که پسرش میتونه او را هنگام تماشای بازی از میان ۲۲ بازیکن روی زمین پیدا کنه. کوکوریا بارها تأکید…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26345" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26344">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqOZGWiUSsTKHwQC5sB_khgQEj1I-qB4F4oZ3dw_6eLa1D5ECh4Xc4CU6yZlCwhPxq6WGHLmZs-c-an1SCbuZD3li0xHRqitd3HUhyJu64o36ru1yO6SN3tB5aJ-bYJ1xjL8R6dwQssbv47YpECPD4ZgblIXYntaItIHqepBjKzyNe0sqM9ZyFSgoP3b4StOKp9-XOFbcep3JTbFD3F3evxbCyT6FUIRuHvgv2DAS_x8pTVFTEkl-UssKeq97M9f9UjD9XwnOMS9It6Eeu87eUq1TVGOU3LEoXGxADhy3P_SS_BB8IBLmckJ_-cZkagf4ZNO5v0282wLRVIzaipoIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇮🇹
🇦🇷
#نقل‌وانتقالات
|
احتمال پیوستن فرانکو ماسانتوئونو ستاره جوان رئال مادرید به میلان بسیار زیاده. مورینیو از پرز خواسته که قرضی اون رو بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26344" target="_blank">📅 13:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26343">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=WP5cZfMvGM9T-_6xlIrPtU_D5oH9qVTGmzo3wWmnGet8N-u9GtguJKXOiB21rYTveNlQWEDdK5Rl-IMtt4KX5u8gsa1lggxiGnkNe-j2c2I4O3PXw2-eRb3HejzmNfC1wOrgHAIwVrBozNob6p2ACxRaCy-gaw6iRrjreTe3iU1sODyKxPy4pdsD97_0i7M7NY9yyXml1h4OZwB4oY3p_iCbLcTrVir3g1NwvSHXf2c7hDQ4Xc_l78Fy9Cc4sQ4MQOob7wiRPRzbtNyHsA7DucyMJWsEtbj1uTlJSXC9_iK_ZIxWF4PwBS9kZSjn9BbkmTaO6NkzsiR7qMqaRJzxVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=WP5cZfMvGM9T-_6xlIrPtU_D5oH9qVTGmzo3wWmnGet8N-u9GtguJKXOiB21rYTveNlQWEDdK5Rl-IMtt4KX5u8gsa1lggxiGnkNe-j2c2I4O3PXw2-eRb3HejzmNfC1wOrgHAIwVrBozNob6p2ACxRaCy-gaw6iRrjreTe3iU1sODyKxPy4pdsD97_0i7M7NY9yyXml1h4OZwB4oY3p_iCbLcTrVir3g1NwvSHXf2c7hDQ4Xc_l78Fy9Cc4sQ4MQOob7wiRPRzbtNyHsA7DucyMJWsEtbj1uTlJSXC9_iK_ZIxWF4PwBS9kZSjn9BbkmTaO6NkzsiR7qMqaRJzxVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26343" target="_blank">📅 12:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26342">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur1OfUBdn70HhtK5vDyYNONIbGvN9v67zx3ogAYV9i3AFjs4_y8O358j5ucieDLgmByhvRPK59j8onOUBztuQnIP11h_QhpYeUlqAZwp4CzCYQ_VUyECUaIxiVE1sDgQOyjNbvtp8hhToYtG_QU6RaYBVq_K0JLBuGVXkR-JVcwuwn2iMI1w5G7mO4dyhaMfjetBZ771dUyOfGnUv7Fn8ULra7UxsGITyJdVmhGtohQBhGGVLzHdBE1jlGenStg6aL7c5AZsHJuioiLNrXpmK_X287m1IwbkvtDKTFfn67sKty2X33__5Y9PeJ1jRHlL6Y-9dbU8ltQbp6jOTl_oNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26342" target="_blank">📅 12:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26341">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egMJ1DC6SxWTKeq5Lm0WQg_Rkmq_2Tc-6D3FI4DoVY-i90-ikfO38kkMZsV53zx3hDq1HGYwj1NFiWGUN_LDr1DSJwRZSP1D76cob3iOXeAE4_Lgo6HwOj-EkIV5BO6MhUUKkL-U0RR65iDU3AfhEQMLGMDa9lefDmxuLKL7Bi0tiegDAh3rAXDx3_rHXEAV_Awdcz-LYI9rLkiUvPsd-Lk4-SdU9zQKiNXYlSwSi32CrhnbvGm1RZhjBSoDX78Lsk3UKpbxogb_qqVk7-JVOcfr-FmroUuW0bv-87f8WsZOHKSyukmu_h1KKXRFoBg6ZHCZeGchwa146AEupLqPaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
یکی‌ازمسئولان‌تیم پرسپولیس: با دانیال ایری قرارداد امضا کرده ایم و بزودی از او رونمایی میکنیم‌. علاوه بر ایری چهار پنج خرید دیگر خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26341" target="_blank">📅 12:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26340">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXddQAdZVQApQvtIKorUJwma3ukGAkc2TKOVFtyDSf6Fzg9L-wLgwlwthCqdXm36lE_eQk3I2gf-0ap5w8xTiga3JyUozxVfLM8Gx2J9df224UMQXDPCn2BoeVf6lDN0OQhwLIZ2EthakqAuA1iTV2fbXe7THs8jPsUHQnOQlpu9Bl6cwYz9GC9q3j8CsZduXQ7oJAHePqAmzaMy38bJXIqtZ4ksr1eBSuQBGm1Guq2GuBIQdReoFaPD6yz0MkxDwEetg2fCo5cfL8YxAhOLmAM0A8B1vjezRZBlDY7qqAKKD13XScSsA3yI2ao7EfIOu00X7w_XJSlZ0OROmfF2kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26340" target="_blank">📅 11:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26338">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6BQ2CTzMycdQfKgUqs1yGsHdzUAqXA6-VdS-F2QcJIfzKQL6M8kdjOf_oCJZydW3-zf9Bz5u4H32hAMhcGF1zpixw82gG6NHDfbuTzUbb3zHXLnUKUMHVPNNGk3swBVWtZuBBlsAUTRXyiFAplekbbiEeeH8YhkF-6m8Rrgj6Is1cMu2_FtSfPku78vJKWYLLDM88clSkJqyXjzFz9h4w61NV9gaHQj2WsIoYYG3Ic-P7btHnJpEW2d7YTJlxCV6F4_L7CKQr7001y0ErJ_FOPejCO-vj1UFzG0_tkmXWPJaXh_3CEidJoAPRPIdYGPf7wtm__CxbO15DvFE3IU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q3knMjHRJgF-dclwOY-xooqhZ07T1LK2Q1-V_YDoM0QBaJYwWUcibeQVGatf86NOwlA7z-7k_lQ2uNIsTUzWj89rihc2BTfgVC4PnGtm92IZkGAUj9IFz2s7CrpAG4olSo1_k8T-YaM941uVDhu33v--zMCQlVBNUrJ4QIJedX2GlJOGJzGc4JfV7PEmY_RBMYk3bwhjauFpqN2ImYH3CIwm_uxEM7lGELZTvejPzLwoAEwxOoQOnILEzGRDo4RgatkMGGpWJgFA3RLaF3bHyLX3ukRdDddwz3YkW99I_kfUutCYH9bpc-HIXpHSWG2A41c6cloxtLWgdmpz7uKDdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی‌غیررسمی‌از کیت‌دوم تیم رئال مادرید در فصل جدید رقابت‌ها؛ فکرکنم باب‌میل هوادارانشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26338" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26337">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUAiyg11op--ytOQghfGqaBnUXCmvMAXbCjlUGQGNKJcdaEyRVRJwf9bsqmDxItU3xiYgCx-J5gCmxpI3L4kJfaTTvyCFuzrTd7YHFTHnhI5i0cxT115r7DzZr7mo0R9YXSai4Z8Fbw9Jq8MTBVBgovmy_4xCbr24hqrBEtAgNPg6AQnK99f8t3Wsyyu6RJMFx3wSxv8UJa6x2-V5JjIPlRB3CkTMO3LJZ8e0ypzavpfy-_c7XaM2JpRzqEZYPYBVOutcFXZaMCKl3wcJiFY4ZQYjb8C7iutXoWm8WFjq70ZMOg_RHPtEPxxH38QsjeiyKr4UysljYXt_WFBbRvH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26337" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26336">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=mEeNL4EHUh6RRMx6ja35dFYTzapGCl6THoBQ1KOa3DrjAg_ZZldZW7TVLJqj5SJXRaaIyFyr6mRiwTD2L5mWXDMSK6G3woGYk3bMzjJecmdgNg-hbcQFPVaQUcwtfmIDoSz2ExME3jAwyEx7Ie1dtx5y-l4f1nfIRNfOzlPIX8ka2QT93ur3G9yxgLxpgMHBcN4BjiaG_QFbZ5Pbc7p6R9WTDSPtuSiknH1h5E2a0a4eAfoRvQZTCjZSnyN8Tl-lVHJ6cvn_JFNYaH3KyDjfuq3KJBJGey_XcndbA9GknYMS6XxckmIbe5D4FgbCbqzDIsBlYfuHblJ2W5O5rrM8MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=mEeNL4EHUh6RRMx6ja35dFYTzapGCl6THoBQ1KOa3DrjAg_ZZldZW7TVLJqj5SJXRaaIyFyr6mRiwTD2L5mWXDMSK6G3woGYk3bMzjJecmdgNg-hbcQFPVaQUcwtfmIDoSz2ExME3jAwyEx7Ie1dtx5y-l4f1nfIRNfOzlPIX8ka2QT93ur3G9yxgLxpgMHBcN4BjiaG_QFbZ5Pbc7p6R9WTDSPtuSiknH1h5E2a0a4eAfoRvQZTCjZSnyN8Tl-lVHJ6cvn_JFNYaH3KyDjfuq3KJBJGey_XcndbA9GknYMS6XxckmIbe5D4FgbCbqzDIsBlYfuHblJ2W5O5rrM8MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26336" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26335">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKbK4wD3Fh6Kbk9HtkoT4SJZK1-66q4VMZK3AdYbEPv7ufuqITZb3qISMVmBK6bas3xQ302_V02_0K27KKCtEHzBwhqAcByst1dQFywYsQCPRwa0mdGRzfGuP6WDRZVEzTVPADDENdLOOWq7qtXD2dadXsS0elkz-H5CNi__XFxVQilY-oOf5X-MyP_2Fpcg0KvsBabeB10zvZy1JvX4GIZPzqNKNwg1Kpw_cZ6_iKmzNWF3KBsDXBYZTcZyNFK8-EqkZPEdBnzH8Ej7FjOyMOyaEiF9njTzdmnKkxcV0qTlSDPQ4MDGQc2RM7m2cV5IZmQmdK7vhBfEGjpmZUZCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26335" target="_blank">📅 11:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26334">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWs9wZ9uzv4O8kUclJKcTlkmEsHog6CsyTPQi7wCKnLqZSJy1pc8BazjHQOy9xBVo1Qk4dLZnQKi1060NbkPFV_pz1bgl7I43w2C0iD7qQoMTeV5QUji-IgCefyMpyu1x3H9uNHApJZCLLNHfUkyRisk2mS9nI4Bqw1u0gfg9BUemerdUTNQdsOEQx21jUpLbvR5nx4OVfeYK4QMrmuPjyqJbX6IkksEO6h-aUOL-cQJhs83HAP0aSgl0KtBWQYKGuYwAyCMDINY6-K97yOJqNxsdfctS8MtSJ4aWVWXoA8Xh0ucImiFsiUlE-G9DO-aDGByofRSsB3FHiag6RNWWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیرو خبری که ظهر امروز گذاشتیم؛ باشگاه پرسپولیس ظرف‌فردا و پس‌فردا و شنبه به تریبت از دانیال ایری، کسری‌ طاهری و محمد رضا اخباری سه خرید جدید خود بشکل رسمی رونمایی خواهد کرد.
🔴
عصرم‌گفتیم‌کسری‌مشکلی‌برای‌رفتن‌به پرسپولیس نداره. ایری هم‌داخلی‌بسته وکار تموم…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26334" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26333">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAHtHJhNR5qvSeyP-EoBkZhJKhM8VugqFVGNXB14gNwdaEJfu4cjt6QtrXfSIJGC_vo1lBG9VoYAKo0440vWBFDm-bJ9460ijR0hNTzjNT6zjxEHL4AVq4uiqFEpHqJZHcnXXJk0HGMf3O_FuPgaHeK_Bv1QzZST0n4wYYELc8eLBlEVXUVMbkBqirWY4tvDKpoRlB7l2XTtaN3c2-He5xZGCzCekBgm4-t060mjngmVbQn-QQ5zEOs3z7iwsCqhFQbOarCcAGdn4_2dX5xiMUcnNwyM8Zz0DuR5fqS0kip5wKaXLf1xW0SToXoD9U8V2cqpEIoidkjM9vWf_AzhAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
اسکواد کامل و فوق‌العاده بارسلونا در فصل آینده رقابت‌ها؛ بایستی‌صبرکنیم و دید هانسی فلیک به طلسم 12 ساله قهرمانی در UCL با این اسکواد خاتمه میده یا باز هم ناکام خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26333" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26332">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR042OOe5uyuusvjBPsnx-Eq0nL6KAKUsBgeTB6QLA8mgPUvNkOvzOxTheIEq-UnM9EBrs7EJoD-QIzGrCOq0yHUXBoqkgcNA16S7o0XlH8Rbkwu31nMc88W_BH_9-ujb_eov7VtiQNY_5ppRSNwzfXHFgB_DRVVianFHGPLh-EpqMSW7BRNDv9cg-Pykf5v3XYNow_TcKgv4dlk2YIX6jI1Ftp-w-voyjCXjDkOmUXGKGZgPe2HnT7K-y1TaqI5g-RA_9s9fUsCuub7qcsyR51dGlSrof_9G2hr3ownhN2sF2VclnqZ0SU0fykUpk5WkbsXn8ljgrU8GoXaEvmCO3_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR042OOe5uyuusvjBPsnx-Eq0nL6KAKUsBgeTB6QLA8mgPUvNkOvzOxTheIEq-UnM9EBrs7EJoD-QIzGrCOq0yHUXBoqkgcNA16S7o0XlH8Rbkwu31nMc88W_BH_9-ujb_eov7VtiQNY_5ppRSNwzfXHFgB_DRVVianFHGPLh-EpqMSW7BRNDv9cg-Pykf5v3XYNow_TcKgv4dlk2YIX6jI1Ftp-w-voyjCXjDkOmUXGKGZgPe2HnT7K-y1TaqI5g-RA_9s9fUsCuub7qcsyR51dGlSrof_9G2hr3ownhN2sF2VclnqZ0SU0fykUpk5WkbsXn8ljgrU8GoXaEvmCO3_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26332" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26331">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TudvMNuO2Ukk6PkXPQBUZno566PU96Cfb-SKAuWGQR2oo2vSsjXtVGYWXSxraDNJNdxwE2zBVm51RUYMETBccjSjJVMjyNRYZmqRzOlUbflg0p5gdADwJeKI7TEF6wQUOWGdxbGKfkNfc4QZgBl4UXLKR-I3vk8ZeL-CYLsu5BKPU5WDRei8vFaA3tmTYAveCGCf1wasr7ETIKKvCTuZtmkXkbqE4ImoIN_y4HOspjih7XF9f5cn5RnNg5vZ12cOQFyXBsOGe7DVvLz9qKhvh3F-0ZWw1NJhMIqSB3AE1HOHStSNSKnJD0FxYtIq6BsNYIKCvxbZ3zkspXjnNaECgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔊
با چرخ بخت وینرو ، برنده ی ایفون 17 پرومکس شو
🔊
💰
هر هفته شانس این رو داری که با چرخ بخت وینرو حتما برنده باشی جوایزی مثل گوشی آیفون 17 پرومکس ، جوایز نقدی و فری اسپین
✅
حداقل مبلغ شارژ برای دریافت شانس 10 میلیون تومان در هفته می باشد
🚨
ورود به چرخ بخت وینرو
🎲
با وینرو فرصت برنده بودن را تجربه کنید
💎
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr1
📩
@winro_io</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26331" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26330">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=Iq9vW2fFsg06-yffxgpISXRivBpqAFxQSLKlUG59-cZ7u90F6ODDXbgsfXfMsUzw9yf9CyihSX_0vSJCBJdegKfqHe-cp8aObUsBv-ayIKl2stjpbkIFGLV-y9sa4cPLOlkMUp-QJNwhsO-A_IMWj575PxB7BtbMeHMza9JzptU1o40q82iKPYzrnmorUSQNE56pVdA4MwyNQqLhCwVWZwxrt7mUrV1fEdxA-catRBj3OKM4gm9ejmgxKN0fJ_icA4JTadJKimNMOhv1j8mw0xJh30Oj-cYd8Xzsvs9PLTNz-dRjlSd_AYAhMbMt-ZDAWLvLIKPXEn9Pauul-2E3_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=Iq9vW2fFsg06-yffxgpISXRivBpqAFxQSLKlUG59-cZ7u90F6ODDXbgsfXfMsUzw9yf9CyihSX_0vSJCBJdegKfqHe-cp8aObUsBv-ayIKl2stjpbkIFGLV-y9sa4cPLOlkMUp-QJNwhsO-A_IMWj575PxB7BtbMeHMza9JzptU1o40q82iKPYzrnmorUSQNE56pVdA4MwyNQqLhCwVWZwxrt7mUrV1fEdxA-catRBj3OKM4gm9ejmgxKN0fJ_icA4JTadJKimNMOhv1j8mw0xJh30Oj-cYd8Xzsvs9PLTNz-dRjlSd_AYAhMbMt-ZDAWLvLIKPXEn9Pauul-2E3_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌مهدی‌قایدی درسال‌های اول حضورش دراستقلال: رحمتی و حسینی بشدت‌باهام بد رفتاری کردند. تو یه بازی درون تیمی به حسینی گل زد گفت دفعه آخرت باشه این کار رومیکنی‌ها! مهدی رحمتیم گفت این کار رو بامن‌بکنی شلوار رو از پات در میارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26330" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26329">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=Oafvx-awUitqM-MNMJDTGOQRg1KZ-lAwPtvHkSo__5GvWof6uRPAvZVDKS5d0chgzBtsYIDfcps93w76AO99VBCirFRsXQjw32BRbVMC4CmaAmxDbmngEXtihZyyyjSwZgVUFL_BwrHAVCA3-fsJ1Q0n9Ni5rvPnqAcyH1RN1VW9Vpu_fvlNsETjJi_gQGqVC9scceQXk7oCjbTXvUmypXg3ykFM4x7nNTFKACsgJ9Ct9XPDFcsGBX_v7FeVPfGsvXjfaPfYl6rvZxwIRuau_2JO6ZZ4KOsdweYsDiIXdaGskrdnzXc3aIM3AN0Jebl-jPkSzG3y2wH6DSQvhCrBUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=Oafvx-awUitqM-MNMJDTGOQRg1KZ-lAwPtvHkSo__5GvWof6uRPAvZVDKS5d0chgzBtsYIDfcps93w76AO99VBCirFRsXQjw32BRbVMC4CmaAmxDbmngEXtihZyyyjSwZgVUFL_BwrHAVCA3-fsJ1Q0n9Ni5rvPnqAcyH1RN1VW9Vpu_fvlNsETjJi_gQGqVC9scceQXk7oCjbTXvUmypXg3ykFM4x7nNTFKACsgJ9Ct9XPDFcsGBX_v7FeVPfGsvXjfaPfYl6rvZxwIRuau_2JO6ZZ4KOsdweYsDiIXdaGskrdnzXc3aIM3AN0Jebl-jPkSzG3y2wH6DSQvhCrBUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
بدل ایرانی مارک کوکوریا ستاره چپ پا تیم ملی اسپانیا و باشگاه رئال مادرید هم پیدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26329" target="_blank">📅 09:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26328">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=mGh-LaFUft7hsUQklN6TG-VeZNtlDg-gBZozEREQ8aq3g4AbWqD9KDXg2akPEJC99ORXbo4PE7nZzjDSWoJOytNwkpM40m4umHn53rP5xqpJkAznPqTVYXjNErHGvyh3PBL9_2P76Hzj5__VfXoVkW6ujYmP1VURqzmtDrnw1brA2fh4ORxBd6Mbt8ifEMD46aHhXUnk5dB8pGCkHgqpBl38bnhKICnQAkutF8xtLX489o1BiyBossL8FEzbFD97Wl-xYlnYm2cizqoXuRScWjGFzUd85i6SfmV4YcfjKc_BNGXHFWbVreX0mMHiFP6E--qTOzc8ZDe5QVIVcYzvrotRSGjulyJqu7LTXM5yJ3m4YFKU1Tiy4HsaDZD-1yHcP74wEo9WWvu_U3FKl1RlKOjw1fUYaX6ndjbQMM78AKbK-HLZvLHhY3ezS7fpsEjW-fsRgmsX2WlNaonUYqjZQJkLZygn-3Sz3xsp9CX5emYhhqGfvsK0lpq1tezFE7xwydbpbdeuC7Go0kKXPjqD28rMUBZGUwXijnN73wO0bewVal6ODlR86va9Tgi7hZ4VkbWBtQEIW0ZZZ_T5S2T6BGU0yse8MBVKZQEHW74ZcJZfzSQdea1h5dvY2_RgKWpQgQH4duuOKjMtUefVrwrctyl4yu-lNIwmhmVuQlokDe4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=mGh-LaFUft7hsUQklN6TG-VeZNtlDg-gBZozEREQ8aq3g4AbWqD9KDXg2akPEJC99ORXbo4PE7nZzjDSWoJOytNwkpM40m4umHn53rP5xqpJkAznPqTVYXjNErHGvyh3PBL9_2P76Hzj5__VfXoVkW6ujYmP1VURqzmtDrnw1brA2fh4ORxBd6Mbt8ifEMD46aHhXUnk5dB8pGCkHgqpBl38bnhKICnQAkutF8xtLX489o1BiyBossL8FEzbFD97Wl-xYlnYm2cizqoXuRScWjGFzUd85i6SfmV4YcfjKc_BNGXHFWbVreX0mMHiFP6E--qTOzc8ZDe5QVIVcYzvrotRSGjulyJqu7LTXM5yJ3m4YFKU1Tiy4HsaDZD-1yHcP74wEo9WWvu_U3FKl1RlKOjw1fUYaX6ndjbQMM78AKbK-HLZvLHhY3ezS7fpsEjW-fsRgmsX2WlNaonUYqjZQJkLZygn-3Sz3xsp9CX5emYhhqGfvsK0lpq1tezFE7xwydbpbdeuC7Go0kKXPjqD28rMUBZGUwXijnN73wO0bewVal6ODlR86va9Tgi7hZ4VkbWBtQEIW0ZZZ_T5S2T6BGU0yse8MBVKZQEHW74ZcJZfzSQdea1h5dvY2_RgKWpQgQH4duuOKjMtUefVrwrctyl4yu-lNIwmhmVuQlokDe4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
واکنش مهدی قائدی به حرکات عجیب و غریب قلعه‌ نویی کنار زمین؛ خودش از خنده رود بر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26328" target="_blank">📅 09:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26327">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=F6qVk-ZnBE5QKrMQ92n6N0_pQH3uoyt26fhPfZ4yEgKDMCuv99GeXy6AgidHkCgWaT1Ja2gYFOyfvVc_fEOM3x1bR4ZGTVeP7gijOIHptB_85ysl7W79nEwSjPHyRSNub9LsORFYWB0KKwX9_CoDcwsnGjDBUGdzqDvgMRwy0NhlPmfvWI2DwLyAFKeuEUzw0Q-fCwqObe1IE7ty50muaiVax4H9gf1-DMKzWceIB5mgsO7_b_JF4Ctob3Ik-4eeC7Hk6k5HyFyuJgD30cJMRdHUIt78rxo9ZNovZ597WJJ1D6nBmHXs8eM_9ZQqK79rKrrDrl0xiSmtqLb9JkhkQmxotOM3wNLlc720h0WLbfX9Ybac1cY70PjdIqxKiVPHAAU_doaKOCLK5d7xxdqn9CjgqcwV7xUX2hjYcterRzUFV0dXlAWYw3I6LiLIlh9bSn9pbYrCyOfV1D9rpEUsECjEIgMu20qd-6OQokJ9tLVgsWRkmCIbfsIpb_vvNHpKZ24zqMosbSbX1M6Hfz4DFx1FNj9Qtt03UeiiyL4t-a3mbeyEQwSSSAhcfunKbVMesQAo0XnVOQiqfQKpyMTZ_mNrmZh8oOigysGbacsRxP2veWb5q49uCqFKgwEJ53Ah3RS72xmmQ26CJ6Celhu5hIffKcR03SmDMA_GNXfD-Xo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=F6qVk-ZnBE5QKrMQ92n6N0_pQH3uoyt26fhPfZ4yEgKDMCuv99GeXy6AgidHkCgWaT1Ja2gYFOyfvVc_fEOM3x1bR4ZGTVeP7gijOIHptB_85ysl7W79nEwSjPHyRSNub9LsORFYWB0KKwX9_CoDcwsnGjDBUGdzqDvgMRwy0NhlPmfvWI2DwLyAFKeuEUzw0Q-fCwqObe1IE7ty50muaiVax4H9gf1-DMKzWceIB5mgsO7_b_JF4Ctob3Ik-4eeC7Hk6k5HyFyuJgD30cJMRdHUIt78rxo9ZNovZ597WJJ1D6nBmHXs8eM_9ZQqK79rKrrDrl0xiSmtqLb9JkhkQmxotOM3wNLlc720h0WLbfX9Ybac1cY70PjdIqxKiVPHAAU_doaKOCLK5d7xxdqn9CjgqcwV7xUX2hjYcterRzUFV0dXlAWYw3I6LiLIlh9bSn9pbYrCyOfV1D9rpEUsECjEIgMu20qd-6OQokJ9tLVgsWRkmCIbfsIpb_vvNHpKZ24zqMosbSbX1M6Hfz4DFx1FNj9Qtt03UeiiyL4t-a3mbeyEQwSSSAhcfunKbVMesQAo0XnVOQiqfQKpyMTZ_mNrmZh8oOigysGbacsRxP2veWb5q49uCqFKgwEJ53Ah3RS72xmmQ26CJ6Celhu5hIffKcR03SmDMA_GNXfD-Xo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26327" target="_blank">📅 09:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26326">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnjFQKbaj3i14ANioofJE8EkTpHTlGkuqLEzC1WPzK20Rn13e1Y5zOfowojLS5BbOs6HmhlF2SfN_dOiSAkdY5S1pwYrL0HI6J13tDtaRN6OwfsD4E8W8yhaANRkSjaUlJcoAXr9sF2aUTqR1GZ5hTPR6_ERjCw9dNEqUx91DCYhJg4uTlMHBzTF0VadbP5YJE8JTkbGZuLul3ZytMKSSqYSz_7U2QbHyiGF8h42sFl3hbJsDEfSYfUy8-cAPvkGlA9hoy4AOepMmGpf3Zx_vCDl7oAMbsngBDo0Ee1c8uXEZVeB74h8Eo2Fu2oo5w1v0XhzQxl_lGkW_Rgk_FE5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26326" target="_blank">📅 08:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26325">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=IJ2iKCyr3YPdZZLZvdb0DLkLJiCe5V87BpsIPQr8nfh1PxXxES1ANGfy_JneZS11r0_6G6pS5PyqPN7RW7pIWh0XbgJZDIxFc4zZNN-zLf8qPYML_AgrYga5DjzkqMjOAqgIZNWXtsnxdHnMaduaYF5RsMk8x80ZdAIz3Iq6d00orFtbE9RSKxosOCjPr129DQnkop999rqc9eBaMH7fnCVGym80RajRsLNR4__UzZsRbBAnpwWwEt93cPYVBTJ2TV5hpVU4aHLjrbMHz8Dvt_yA_6HqeRxy0JEq4RADg44KxtYCfxldABhfrjelb7uvXNCEO4r4uktr0aYDUuVPAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=IJ2iKCyr3YPdZZLZvdb0DLkLJiCe5V87BpsIPQr8nfh1PxXxES1ANGfy_JneZS11r0_6G6pS5PyqPN7RW7pIWh0XbgJZDIxFc4zZNN-zLf8qPYML_AgrYga5DjzkqMjOAqgIZNWXtsnxdHnMaduaYF5RsMk8x80ZdAIz3Iq6d00orFtbE9RSKxosOCjPr129DQnkop999rqc9eBaMH7fnCVGym80RajRsLNR4__UzZsRbBAnpwWwEt93cPYVBTJ2TV5hpVU4aHLjrbMHz8Dvt_yA_6HqeRxy0JEq4RADg44KxtYCfxldABhfrjelb7uvXNCEO4r4uktr0aYDUuVPAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
تیم بارسلونا دربازی چهار آبان‌ماه با رئال مادرید با این کیت جدید به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26325" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26324">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851f45a809.mp4?token=GLNCkKm67L0PnzaBOujKg2S1FN1uVzVp1nTB2ByebcA0BU2jc7hWwXFyxgOY0aaGLfZC3xhm0By84QHv9ZhnMMycJWCoxs_WVxA4VUcLfFps1YOpyUJbZSYDUyCP6iUMpArNqQ1lGk7cFuU2AGOzhTfZ8JFl8EgGVB-7i6xIion681n7oCpz7Zio47XtS3mLTtwU3y8Y4M-RVW2B5zi6lZPTA0KAQr3C_HLmsBI-vI2zETwrtctevn1rLXSeCjiNcKfvpeXFapbYtIDVB-UAyMaU3rOO0jxDkQJMVdeWsWGuM6pnjt85EqLYiOem43hJsCyGU5AxP54oBqosOj60Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851f45a809.mp4?token=GLNCkKm67L0PnzaBOujKg2S1FN1uVzVp1nTB2ByebcA0BU2jc7hWwXFyxgOY0aaGLfZC3xhm0By84QHv9ZhnMMycJWCoxs_WVxA4VUcLfFps1YOpyUJbZSYDUyCP6iUMpArNqQ1lGk7cFuU2AGOzhTfZ8JFl8EgGVB-7i6xIion681n7oCpz7Zio47XtS3mLTtwU3y8Y4M-RVW2B5zi6lZPTA0KAQr3C_HLmsBI-vI2zETwrtctevn1rLXSeCjiNcKfvpeXFapbYtIDVB-UAyMaU3rOO0jxDkQJMVdeWsWGuM6pnjt85EqLYiOem43hJsCyGU5AxP54oBqosOj60Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های‌ابوطالب‌حسینی درقسمت‌آخر ویژه برنامه جام جهانی؛ هرچی تو دلش بود رو گفت:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26324" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26323">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2n3aC8M0IbN005B-4kSwWTscvBMUSJNk5iXZY7NeOp82OnXPvcdy3Cjvmw7mWby-ptCqeesfZADlQtnawbUtYZyo59CH2I5t8viO2BjoOUH4XyP38zt07KCKmW3BKYeCX1p0192glpGX1JbnZMZQuAyE2UrbsyY0bm_QKDiRpLiv8JGZqjQzEh6ClvOUuAGWYQ1nD-0QTeqC7UsnXOQ5tsXEnZdP1ckED0ORlDKkYIR0MMx1YXY0mYCogqoSvaMvLrPfOL2MIdqX-bcTs1VTpHZGX2yDV47tO8jCwh3NOqJ0J7SA-7ddZ8dj3O5BPXExbqrjRgo-u5pW2aHA64oAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26323" target="_blank">📅 00:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26322">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=XkWlUTdkcIl-MD07lA1dkEbsB-SqsM1O-bTCanc943arVpP8sIuxppWhOVqSsXEqJr0Bcc0zTSQ97zvE-L6TqBIrEcVbs_r2r1Ge6k4EYsXvB9tXTzxfBLn7RoaR2JI2Kd-LJ71O0KJiY-vmMRZ1G0nEAGT_UMp4_jv2x5Ip7kCl31ZyQyLVXwM4VzgntmAu04VB1LfrtUVYK3-fFaxTpokVh6o6umbNTqEU7r0RNRVb1W2D1bVfvb3Dx0RCHPYmernJ1jA6y4MjfBo8X_hl9MZQYfCWmL-8r-Dq3O8ft6C8iy1TfGjaBJRRySqMEJu1vAfRyCnFhdSaSntNEZD_SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=XkWlUTdkcIl-MD07lA1dkEbsB-SqsM1O-bTCanc943arVpP8sIuxppWhOVqSsXEqJr0Bcc0zTSQ97zvE-L6TqBIrEcVbs_r2r1Ge6k4EYsXvB9tXTzxfBLn7RoaR2JI2Kd-LJ71O0KJiY-vmMRZ1G0nEAGT_UMp4_jv2x5Ip7kCl31ZyQyLVXwM4VzgntmAu04VB1LfrtUVYK3-fFaxTpokVh6o6umbNTqEU7r0RNRVb1W2D1bVfvb3Dx0RCHPYmernJ1jA6y4MjfBo8X_hl9MZQYfCWmL-8r-Dq3O8ft6C8iy1TfGjaBJRRySqMEJu1vAfRyCnFhdSaSntNEZD_SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چیزی بهت میگم قول بده به کسی نگی؛ دو ثانیه بعد: چه میم‌هایی از صحنه در اومده. بازی قبل اون حرکت مسی مقابل بلینگهام میم شد تو بازی دیشبم این حرکتش حالا حالا میم ازش میسازند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26322" target="_blank">📅 00:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26321">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی بینید از پاس‌های فوق العاده هری کین ستاره بایرن؛ مهاجم‌نوک‌باچنین‌قابلیتی به یاد ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26321" target="_blank">📅 00:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26320">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zzjva3pwwcJxpVk285feVlsZd7IP8IK7m4ooCoLhpZZM8hTV-iXLqn6cdd9WayY9KeeKSxvgHgAvPCFVoUc3Aakqeb2A-a6x1754nYD4FLHF5CU19X_swFxn02R7sqAXenihm7oF6cIkEld1nu6qKxjAmxGXxVYLCPXG2ADrZE33ZOG4vqcSFX9qmCXU0qLLpnH_rhsQYUgchKOO2fq1schs7hiiRO3ko1_4e6kFxcUAaWfqueZ9ollG09ztraAzTdqM8OENw0kQxeQjxSFrhcCc6GB-5bou24gOh-fIs06nzbecc1oNtRzQQG03hu960MF6zG4TWUZoqkYoISA2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26320" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26319">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBbxh8DBllw41_IYgKUxt8699pVkSzDoLERfTAmyeR2U_PlKuJ9MSHbaSXXbPyGlmvbqFq1Ep3neMUOvqBZ0RleSx3poKPxcm3pq6EzsSc8XjpdpC4b30lLRTIP7QEXfzRFMmeDHqh7e22o_vgwifK3EkNYJkr9goH9T-Tcm0bShQVv-42atYvzmAXTX0JRsA4KDwfW7WPmwBWXf7Oazb_nUkcJo6zs0Tnt1Gv_3UOy6znBwR6A6_4LAiHSNpBHhJd6mZeTL5jL3pB82VvXPL0j2EDPFr0bJ6m6rXxwDNqX2Ed5ZcKLdhK43UQS5QtAk3D71jhTrQS0kwFfuDeMY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبر اختصاصی‌پرشیانا تایید شد؛ تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: با مدیر برنامه‌های یاسر آسانی اختلافاتی‌ داشتیم اما درتلاش‌هستیم که او رو به‌‌تیم استقلال برگردونیم. آسانی فسخ قراردادش رو به‌فیفا تحویل‌ نداده و ماهم‌امیدواریم که او رو راضی کنیم برای…</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/26319" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26318">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G43dLUUJiHh651H5Ic7pPm9M8nk4PtiJVji0LGSfG2As_WNrzciA4tmfQNC7103cM2xBvEPygJrPIn1sr72ZOMFYxJS25Id9WSXNqW-UciD9WjfBUJ5bkSiEnlA-5KlksGYLtdxlEKPapXr5N11niVY5d_j36I9wYExc5fxhYHabNyV3k1BI-3s8ceyULFVVzX_oEHTp84_UfiT1pB05PXQG_h4SuNaMq57DQc_gGZ_bxTd2oklCtFv9X_0wnEuESKrtHw9zSmdQ_VG4fUmc2C1ONFxhmizVs9Xr-uNszqIK1q6LdETNOhFMjBdtg-WxQnXNx0s3_LhNNTKYWQdgNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/persiana_Soccer/26318" target="_blank">📅 23:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26317">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNtcj4VqD1ml9azcP7JbwWyJvqU5YGAFPemNdfMGBaLtIYQRW55Lhfb3JJpWm1vtLjWS-d5Muy7LkqYcFmIQ5KLkC3OdUUHLrUsSFPz4vthQ5nFKntVjPiS3I0_MkUC1bIXBVTSFAFBjTo_7jOwlHnmHgl96epbMGc5Hix5HDsFjKIJXZMpaMWRkvFqO-y_Eq8iF5ETTzWISFwAmJghzKNr7hr5A1s1NJ8-lBf2F2iYtI_Y3iOk4TH0mhTN6HeoJDWKLvfosmDymW9VGzuvLF4B_PZBKZbj6qAKPm6LIE7wcAQ79iO9QNbhi_n1cBkDPP9hnHtA5mTywqoGyULmHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آخرین وضعیت دو خرید جدید پرسپولیس؛ محمد رضا اخباری صبح امروز به پیمان حدادی قول داده امروزعصر یا فرداصبح برای بستن قرارداد خود راهی ساختمان‌ باشگاه شود. دانیال ایری هم دو شب پیش‌باشگاه پرسپولیس‌باهاش‌قرارداد داخلی بست و به‌محض پرداخت رضایت نامه از او رونمایی…</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/persiana_Soccer/26317" target="_blank">📅 23:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26316">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgsIabclTqxBKACE8dTfHi4s2x1yRx32Roa8guGsohZkXTSGIvNYwWFG6ZzSr0wzN-oP_tyYqTVC3KPdZXvRfGsYLf4bxirTfwZEPCUZXI59xu9lq7WuSYn-Db8pZifHqFwxTPIJdc2XTQH8WzGLclSfA7sJGVKC5W0USvsu4rDnn1pcuuRYwqc9YzJnv1aQgZ-HJx4RtgLT-Oqp3nwm1OfnFL41fIIrrAkk2hQcfvRfL-9LIE1pSmoA0sR9aj0MLeqyI6kqY08thhoNVK8ognc2DCPluFuEJvVyLtQskKMsKT3Isip0DwhXr_BzXiFKNgJYEtgC0_dHXk3oWULMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق اطلاعات بدست آمده؛ قراره امشب یا نهایتا فردا سامان قدوس پاسخ نهایی خود را به آفر باشگاه پرسپولیس بدهد. مدیریت سرخ ها پیشنهاد مالی سه ساله بالایی رو به قدوس داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26316" target="_blank">📅 22:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26315">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMPL0ZgNLTs754t_K0U53G7WGM42niZzVMLTc7CDTg8DReZXf4gcVmutfsDuSD67e98ATLQPczhyAUTgy32zBnVYhQ3UuMuO12w-vbzwAiALrvYqm9XomL27A-Z1_0qXIWvRWR-1cLxltx3Ghof5V7FY5frmEUdlj5_oc-Q6t7KA119-aD08kczihkTogXpM7z8HU8PnjUDzbAvuBsoEzdVmAOe6Gbp-FsDcTJKTaAVUa1ODhoDE6K0p2jBQq50xUSe4GKETDNmiOwAuWofF6uT2pQHnL7fDYv_66DN5aZMj7w3nN2QawuSGGdtXtvj23I8qv8Vbiq00KIgvlXqZFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زین‌الدین‌زیدان‌سرمربی‌جدید تیم‌ملی فرانسه روز به روز بیشتر داره شبیه بهنام تشکر خودمون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26315" target="_blank">📅 22:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26314">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rH9up0KflpoqTlulWfr-Z-wJGAYSMEFnxRFEJFYEwDeRaPnm8yAgcoFO3sJJAUYb7C61GyKqB3Kjfh2WGHZV4HHIWW6aPVwKE6jLghvGQ4vwdgvT4L2q-BZz3mJfW_KvLukg9oGjYgBsrmxtU0mtmHG10MedJl_VxwZZwiKi7D_1KwJAd1hEaoBMWeptlLUC41k6YOxThBRaLinzTC3OYKmMoCyjZTcI8VWNzO5yQNfkUsRBlpQd-nZqtuHloOqiGB71pZH23c8lEH34wBBNrmKvcamrS_WvPUJtejaYChnrfkpc-kqour9hHpUCVWLHLo6ezVT1RUOhGI5Afdjvfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: سه هدف اصلی فلورنتینو پرز در این تابستون که قولشو به مورینیو داده: تمدید قرار داد وینیسیوس جونیور، عقد قرارداد با انزو فرناندز و مایکل اولیسه دو فوق ستاره چلسی و بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26314" target="_blank">📅 22:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26313">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7xXWnmMHXpoYO18DPoJoM5MRfg48EmfL6XOJZEvrxeU5pEPKRGZPmKiYQYa3AmjHQjEeFHH7N7zjTd7LUkqL1VxAM8dvARrhqAO3APkWyijJ9Be0ENtEO_QI-bxwBtxGj3siqlURf2y3pvAwP_702Yioko0o-veSygYwy2iVZPZ9O-Zlwb-Y_nFM_JI58Rwk-66XtCS8trs53Ht8TNc1biHhommrhQFmKSVOFUneQbKDgZNWc9Od020gc3SCgWSDhWC0v9W-m3zinqpgbo7i1CLbXGJm8R__1FSnhlAGUH8Z8mLoHzNWOGx9mqGFyQg7x-FQ6GgD5irQq894UUSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26313" target="_blank">📅 22:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26312">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5gzjQM0UJyT10VrT9bOwOPNGrYkwe91D_DqpGVi6Qt3D_DpJXpnpIO1YDYbUEm5ybe-NS3O_QpvSl963HA7eWYaJaW4gC5n_t5xjijZ2w5doSXXmAd-vxqy56Eu5khLAgzphYay5rdHOJx6OwfPBnIv6L7x5NYWI4R_1ztcPQjJCg6aAQluTNPrAhYtkKk4ZOa3k9vYMrjlZuEHudOHidTx5oV2Z5CaAiy5KDvHVcUk_8o8_pQMW-hin7t_h-r9sc5i00IOAfB0e4bukjm3ydKFoSLlcYjTfrpAPDdT-HbK7QyNxFTjYMRzmNmvoNoLON21lHpPypkH-eAQFLPPqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فابریتزیو رومانو خبر داد:
کریسنسیو سامرویل، مهاجم 24 ساله و هلندی تیم وستهم با قراردادی به ارزش 55+10 میلیون پوند به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26312" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26311">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dl3hJ192i3sTRJ4esazacBwb8ZUJQvJLh0frELr_MJIfNwWkV7KquvambcOniAE27mr7N8ED46x6IXpV-GmMPpCHA_UYJ-Am14EzsW4h9QsEr-jN7jgGauDl4JZAhb-hxDF6-ANz7mJBdFg_E3r9PvgcJnIZGCQMKTGQShig7FFNA2kzhYAHzxgdTLrRLmoRFHKZLHMBmermZSGdk27OJ4U1Sv9PPRW3mQ6Hp8UL0urLpYcliu0rEMrUqWsMD6y9bXCgbhuNuhBhdHK4kuQkPgE5n7xD39mpvcs8edXe4OVXAOTKwJSMJrtc4jjwzsANxobqpLkZIrc9CE_mab8B7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26311" target="_blank">📅 21:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26310">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahV6eZgndlultqFWtvsF3pBQORf1rdyVgJzk4OGgqE--lYI07KKqR5_3bSviTo9feo3OM-xL7SFRG_gfp6g5hLue6zMbiDNqxQIPKPn_esGh0tpOGGV2KRyeNO4oO6REbd_xvtpF7WbKILJRTZrcyOGHfoJAoZE1PK9ouSgaanZPi1VsgmbJunxrLEybTe-xmKgyPDiSgsgMTJ_iXkdWQl-cmpLA8loxyWEzkkI-4SZ7I-mKSk_Ybl4ek18Ov0YoEPOquUAYVkl0gzVH9WlMUTtbZJ7XP9piyQjcHlRlowp8rKnoPFzcd4PCYh7nC5KsjKAbHi-dNiTFGS2kdHW_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج رقابت‌های لیگ آزادگان در پایان هفته سی‌وسوم؛ صنعت‌نفت بازی پایانی مقابل نیرو زمینی رو ببره‌میره‌پلی‌آف اما اگه تبره و سایپا بتونه پالایش نفت روببره سایپا میره‌پلی‌اف. اون سر بازی پلی آف شاگردان مجتبی جباری در مس رفسنجان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26310" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26309">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmsxrqnhhDn-GFObNvIoZj2djfO1BXUNPDvovOXfeSye8Kxw7oTtNHFy8NaCI56H_Q674bb_Lb4P5zQ-Lwv1eKTW-uNuLR3jzTa59PU_KLh4-3DTllzGyoafxUu-fDxsuAwLVqAAi_5_hpwV8PPDRejA9cgYmslZLbeBeSbHY_1e3bfO1SNhmAAkRIzNhp9wc0w3A4rJZy7TtLgJ6oTCQszIpu0HnbJe6ANhtfFUXg6455GM7iD4PXMS9ZqKC00iZsezjCfBR8wlvTkUI86r94TzFPJ_OGpQt8gJ7ARWzW6VlCo4_o0Wy2N26NhOwjYFz0Mopbz3Pwl0V_9EBJLrrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛درباره کسری طاهری ازمدیریت باشگاه پرسپولیس پرسیدیم که گفتن امشب یا فردا استعلام فیفا به باشگاه ارسال میشه. اگه منعی وجود نداشته باشه طاهری فردا شب با حضور در ساحتمان باشگاه قراردادش رو چهارساله با پرسپولیس امضا میکنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26309" target="_blank">📅 20:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26308">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142133503.mp4?token=SY9MSGeHZZjKKwvL1yLoGu6h_tkxwRFdLRYkgGcIaz7MvLZcN62zZJhKHd2ls-JSmLInyztIcUW71xVPqJDa7q6i81AncC70u24ZIOmj5dNMMhE9D4egdbnhO0GYKhRW6PE4rYNA5NsrhzUoq2swkO9TPeUOE3Wt1miVJXIgZB-LEclOficFNflNZvyxYQ3X_CVJu4hhgXqMCX87U1YlRcmN4aBwaxyL7c_BprYCfHb1jlEyf3eSE3JUZQcCqrDKq5mKax16HvTSKLl2BK_p0E3XRrJot9tqgMCI-zgJtsGoKsIel2JDlfEU0TPcev3KukrCbDdi9NoYKk61XOH-jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142133503.mp4?token=SY9MSGeHZZjKKwvL1yLoGu6h_tkxwRFdLRYkgGcIaz7MvLZcN62zZJhKHd2ls-JSmLInyztIcUW71xVPqJDa7q6i81AncC70u24ZIOmj5dNMMhE9D4egdbnhO0GYKhRW6PE4rYNA5NsrhzUoq2swkO9TPeUOE3Wt1miVJXIgZB-LEclOficFNflNZvyxYQ3X_CVJu4hhgXqMCX87U1YlRcmN4aBwaxyL7c_BprYCfHb1jlEyf3eSE3JUZQcCqrDKq5mKax16HvTSKLl2BK_p0E3XRrJot9tqgMCI-zgJtsGoKsIel2JDlfEU0TPcev3KukrCbDdi9NoYKk61XOH-jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پاسخ متفاوت و معنادار پیمان یوسفی به سوالی درباره گزارش نکردن بازی های جام جهانی این دوره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26308" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26307">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=n00i2rBfQ0_jr-UC2VCB-s3Lr8PaH9q2wO4h-mrlmwza32YW57zSA0o8Fcew59TG7BjI1zkUQo7v6ZaYEjyqX3Ol4vXUTdMxn7rnxJf2ykcVmNHEQVuzDjM_gbklMQbPdTmUvs_ywjLhcbiyH9Vp1AO6O-5ETDR_LGkG1RkM8mmgAZrGbSpGDcz6om75fuOvT0uUSZdgtDHmov_Xf9ntDu51liaLTpcSEaPgKpjWkd8yo6vLlQCxMqH-OvzBnzsHHhCnl0_9R3MNJbx1rt-lefPQjlRgbEC7WwGiPlOo--f7Zf3FTiFw-LgIRJghOaUf1tbohCT3yJbjLFB9DqenEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=n00i2rBfQ0_jr-UC2VCB-s3Lr8PaH9q2wO4h-mrlmwza32YW57zSA0o8Fcew59TG7BjI1zkUQo7v6ZaYEjyqX3Ol4vXUTdMxn7rnxJf2ykcVmNHEQVuzDjM_gbklMQbPdTmUvs_ywjLhcbiyH9Vp1AO6O-5ETDR_LGkG1RkM8mmgAZrGbSpGDcz6om75fuOvT0uUSZdgtDHmov_Xf9ntDu51liaLTpcSEaPgKpjWkd8yo6vLlQCxMqH-OvzBnzsHHhCnl0_9R3MNJbx1rt-lefPQjlRgbEC7WwGiPlOo--f7Zf3FTiFw-LgIRJghOaUf1tbohCT3yJbjLFB9DqenEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بادستورمسعود پزشکیان؛ مشکل پلتفرم و سایت عادل فردوسی پور در حال برطرف شدنه و عادل پر قدرت تر از قبل برنامه اش رو ادامه میده. مصاحبه مسعود پزشکیان رو تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26307" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26306">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1tWFkyd_Roegii6V3AWTfFwuhIAs8h9ATZEXsbiTJj74f2fwqP99HCWbd4OZlf9m0uVmYKT7GcDhMJ1d5UD37-zVKjD498wg70JusCCxkptxSpojGSEe0mFEPrjt78PTksU2TlBh-KgTUZpbDKwBdt8Fz0tT4QiO4Tj64MyNyNyVNHnD3WpmuWHf_EBIaXXG_lRAYodQDnFBtZC4X6V2sujW5S3VMZaNgNIV7U_9r-NMLlAFNCIicNEYS2TlI9h4LQ4InqFa_2crIPOiUjwFs9p2Ae4fCe3HScUE1t1gUv_LL1TY53xgg4dhGPJw8APKN7zqO0tfrXIveMvciBJAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇧🇷
رسمی شد؛ کاسمیرو ستاره برزیلی سابق دو باشگاه رئال‌مارید و منچستریونایتد با عقد قراردادی دوساله به اینترمیامی پیوست و هم‌تیمی مسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26306" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26305">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLMLu0i8qxvY9A_47t93OaYdM_gtOSfM9x8cazifxVrlO2kJtdz9m7HizZpfhyZ8C10txChyGl3C1_oLTx1IVHg3hKrVOWPVZnEnTdWZT0-t0b07HbiWgagYEj8fsVBM71A1PvXp836navxVIU2iJkCcrDmC-H9LA5dew6u0DBDpFuluoq7_flL3Pnpahc7Mtc4FMWQD7frqfMBYNQvpJkKoI9j_J0vc5SGqS0pdmSDziJWTaPeU-AgsyfzaJAXRFO-9e2m6RPtzlikjjp5NtnAymIoExS0p1fPAPHecRIdREtTFr1ArJhr9YOPqjHVwyFpE5dPVyhkwmA1v7BhmkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26305" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26304">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNy_GgxPYSKY-oPGuAUtTLalTNcGWytxeTLcyaPbLeKWHBoPX-oscrYymfNZO2Vq7a41XDqnL_HIu1COk1JP0nFAqLkujMAVxpqNbkP5tNEelJe7G1qWpSqic2-4r2V0te8un0SeVCimpwkOpMY7CJeeo-OjaJ45MCAFXHYKKgtzgn4Bo3oUoHdxfE21PpOeRgoPglmhfdqS29FdeVGh4SGUd759tOdzNzaHocdA7AuWzHmJBJkUiaP83dgx5axVWJbqYj8Vw8V7GSzVpSMqVQ-99XUvf1rdP6jgMqhyHsyVuNSISSc1vBPrOhPPL5CTzkNaHmZSXTD8woEO4Cspnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی 2026 از نگاه فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26304" target="_blank">📅 19:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26303">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiFJ70uBt6zcCXHfGPwddAffIK9vuk9Hs7ADeckpCqc2E1IkKzLfNvMcUyFlSC8IoXza4gGGOU0nODqs7fzvxsDbmKnX9RUTsZxGkcA0Mwaqo0Osux3IpEba30pcfatXovkDF1UQeUFcd0J36K2NW0KSyZeyJOwBNDeysxGPEM551zN_ckSt0r16dJyysXYQL57PC5PKGhcJKemfVHumUgTZ3MRhpsA_8Pfm-DSuf9y51l60IoKctcSzWpN1umKgRyt3HjzQrvnmvMT5B8rIvubDlvUBsSR3IufJKwIq1iGURIjwqx984i7WmOlfStwURPE0sMQiINJNs_SEmpE4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26303" target="_blank">📅 19:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26302">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEeLHIWPHKskmi8e19q4W55xVsInoH6fm00c5v1pr_tQ-K4dn0YSDo5tn3R0lIlzD-x0oXxt9vMSLNNsRTc56jxM1_EG0tl0wL0PZ_P_kexKdhfK4WtAEv5AFIcFH2XEX9c4p7as7NKg25zYxxzO3x1GsfbtyWmOO8gE1hUQ2AYglvP707LGOhygszXU9yZp54hBkzDmivQD9JgYtXEvRIqQPZuK18CRaxCuJZWmrw1BZpzV9AcT4M-VV8pnFZIXZw7vwh22BgRhqkQA1WlYO1-bKxykV6PwlycDMLsn1HFYb18ZWuOzeE4eSDOtfFLYRoiLbvIF3jCTaQ_DbR_i6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: کدوم‌پلشتی‌خایه‌اینو داشته سایت داداشم عادل فردوسی رو ببنده؟ ناموسا من در جریان نبودم و امروز صبح دستور دادم سایت عادل رو باز کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26302" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26301">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd3dv12_CFJWCom_2O6x1VTxdk-iYtl6fr_7ROQjq9v6JA_vaW-9nuV0XvI96-VDWSe_xOBaAa9LKqn-pKQUllhrqnRpXpG1ANq0sobrWsGknaOrciYlyyIEs38XD0ZXNOu3HIMJ5rur2T5Pb4ISDrLWexIOF8OVQkHtxqoxsbyFw1BbQXXT7bENhKaQ_vUev8o3Lb7Lg_Kb0EC5AhYL_WlbcbRKAzvHxekr0dCjz5QUPZP-4vcL3SbScOvKNT6qqwIaPxpKW1JZMdSaHNBSe201BmeUjwN4YWXDIXqA2n4RYmFWxifnwbas2SJ4UPnVPfVnUQ97pNjg5gzuSJNPdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌استقلال بجای محمدرضا آزادی خواستارجذب حجت احمدی مهاجم‌تکنیکی 22 ساله سابق استقلال خوزستان و پیکان شده. درصورتی که باشگاه با این بازیکن قرارداد ببندد و پنجره باز شود محمدرضا آزادی از باشگاه استقلال…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26301" target="_blank">📅 18:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26300">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f34_lyxlMWZDUbWhtOgQH7vuHyomw7trJz1LIajOsY5e9gHMwIEr4TqYg55ekIimOpuaDRMacPPdjuCE4aZeHIgpY4M-9ZSnkY7DN_ojhO3-iRdAwdOW69T9sKPrljJM_6bgHehJ34Kl2g94GzVj8Dmot29CVhL3zmMNzJwAEhccbKY1zD_lcee-k-wX6zeZ-Y-rQxuwa-j9Hu4WplboZZ-ksGENHB1NBnSOwZbc815OQCGWFvKNRw8KHUXD-9GD_3YwDxga8ynbUk_mCsqS4WJgdTnteCeDcUsqeCP9xQx5v1IkQgsM2zTA54qcaSu-gijnDOF80Q-usVoN-pZfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26300" target="_blank">📅 18:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26299">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzLe81kKhbDqPY0oeILVcypPA17AQFGFUGvp5MyNSOox9dYjce6C6YpcTsvlJLJN_r-HZM9HNpbU4ZGWzh0CRG7JBTi1Ep61WqQLLE6aI1_76zoRm3V6P3mTh3tfCM1YpNWXDXJlETJWn3O0zTsPQ7xykNrxE5Sk3eqzBcbkWcZ1sDivFY9HHnjbrfhnFxKJ9aUbv4vpNSLKM9UO-gMejitux9kmIGGMXVzY4hdCSlYedggsec9XpnicbQ-4zD2gFTRGrH6gjmYxxk0VGy_E8hhW00Lda_J43ugF8s9A0-JJZ0WRLLVgHCPjqnMPq1c4gat9xxCMj7SEnr3fHxquSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26299" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26298">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7_uQi8pJbCJUTSKO3888sC2AczHmHPiAMRFCV1YGQPzFGXcU4eCCtd9OvAgihih6UWDUo9wu-YS1ZlXNgK53zWMIvslPAaOP9io2ka0paBcKdzkz2iQhUJVdr2QLWLuxW5GSNVlzEjXe6dFCSNGmqEdFg69BAayi56B0nVl46scVSBa4WB1bBTMiqR76HPn_HHFAj_6e_4m4GDpSzr04dVqycRAwcLUNiVudsj0V0D-3gvzKAbjjjrFZxgVCVngUgvOkUil_yEYCWgXzCooX2MRWLDtRMGEHeFRsLT8m8sd2fIdrr7_oAPlg1s9VocG9sWzLKYEWN8znMEU0WC0tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26298" target="_blank">📅 16:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26297">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrdEhawuXrGOZN7PoT47S5TxB6QZwUgPxR-0SBHp0z2nV0icGhrNHDquQwoPYHTuXL0spg4fFi5R7vC_vJnT7FFGR9RdRt8y7TxLvwjnCCZbyva_-9je7NgnqIbCBESHJFOhIvqtXfk4LTqetO5gpDfhWEWqL_Y94X59eMpbT7FwmUji8a0y1_LE8hmvgenmDIHmFBYvKhXrFO2FOEiSX5z65QsLWdyYZ-FzEXs6Ee2V7PjMLPYn0g5oE3AwAPGFz_YuLIivuDX-6hjXgpU4LqJ54S0874DWDzR_VKTdxbdqozdeIEtm1QY07GT1TXw05jqfh_4mG02YqHW-dY2qQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26297" target="_blank">📅 15:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26296">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB7whU8QA-K0M8S97DVldVBKmOxHIK6iYJKyDQzQuvuLaMvQR0Ylumc3yYD7CZjajbW7-Dm1DMHhG_wUJXM10evxdErbkIrPrKmOQ0gIL_fwY1ds_o__SozJVtUlw3shU9llK2H0brz3uwrwuYrFsBR4YoOWqbPcB9bc4EEhXPAMW0Rt67BLSrhBIlhEoedLuSEF9PFNG3cW_skO9zJXREDzdw3uQIxNUhR5DiQgzsPtccRboHY5RqWj2wN5Zjik7s_tlZLCLlvyICGNsNIZTlQU9J1iVMx_TBue1UdXK3j-_fEKWqBnA6lbqc4vbWSGfGHSRToujgju9VvCW2mtWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#نقل‌انتقالات
؛رضا جعفری وینگرچپ‌سابق ملوان وگل‌گهر با عقد قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26296" target="_blank">📅 15:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26295">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVenc7B-n6_-oK-yxa5S-PL77Ptd6-gNuiHSXhqBy1UkI5S4MDeUshFn5ppgBPlIBtszsDFNz7lqbOnpDgFJBL1o0GCC3s0YE60M4Y-C_VX0rPTkgD6mzMBwb6dQwyuXvAeBtCW6PKsFHlHkY9lCuc1O53VCScIFCiKt0EjS3SBuypeblUO99XwpujaEYKqooD9fCy7XH-uKHbNHZmF9VUGZnZHKYqWRviWUhyUOUCWgxIqa7W1i6ynBpMhbfRCkhmrdExUIq17R5-jkViRE3oC2Lm5mvrrcPapU6f7jQSulyQ_uEmR3nxb_kiq5IOVN28lOoQR9NKx97WmUjd3CLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسانه‌ های عربستانی مدعی شدند؛ باشگاه الهلال پیشنهاد مالی بسیار سنگینی رو به فیل فودن ستاره26ساله باشگاه منچسترسیتی داده‌اند و قصد دارند این فوق ستاره انگلیسی رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26295" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26294">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kvu1Ig9jOYXo8d1sP5_BhA8C6yYW3tqDk-dt16LkW9aQAfHBQze76C2s4m37FAOyJmzzrGduiYGtPQo66pfWlb6hFkN-kcNF9mSGBm8QzfC9C-0bPS31U2GxFOwBaf6eas7l8XQMhFiY8DoNWKOIInS2EfvjZw1uQOeEj0jEbPlzefo5jiI12eadGlunM0TWXLKY_yug-fa_4rdZxl_hVW_0O9P7ez2nNP-3dxOQ4xkjXIJ_48zyLBc5DFsS9pUgytzDlmEAp6F2GVyVqHYu5clJEbVg_7x-lBpJczNGwXR7GayODiNCs0S5FS38X_2HBAv5pyC4WlEplUjPJEwJzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اگر اتفاق عجیبی رخ ندهد؛ باشگاه پرسپولیس ظرف 24 ساعت آینده از محمدرضا اخباری و دانیال ایری دو خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26294" target="_blank">📅 15:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26293">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMnNGH72Kn1aGlICjoxeM3742-8xAcKyuXxxegnwxN6OCRj5Oo26If0byutsjmvCKwIVOa-Wj93mm3CfGC9HaORFNUEl_5kWi0et_zqfW-LwTdJOZET0K11DZI7-2wujiaKuBAI4kknAdx3hr76MHf8JV5d7UWlbdHih2kHODtaQn2x0PwtHN9z8k8FpcKhe0C-zLlwKP1Be8UbsI98Y7tQ7IW25gytiuMCfy-jZVD3fKNQSeWlJVUHbK2awsw3Gf1HdyTOh7N7qhjwyzisrKZIgJb5rff_FeXrd6QoxBa8nsiCC0GLxNm262ix6DUt6g4FPodSkwj1FQUU15tcTWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26293" target="_blank">📅 15:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26291">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fBHfmqgahQmfMU0LcD69Ivf5FlPqQxztV_B1Tz6PCOkiP_fQUj-oYXFm76XHIctNOIXoKbehIBRzMnKp8b8efH-PZHOUZe_VAWy5kgGLvCicuS_jegoivc_OVXfSXNY2f1ijNKw8zmhjoE0SFy9unfGeg0WQB-keFLxzdloOpstrEeVKEns7jHJvG8P80WvxTTajt8Wka_v_p30fDJcpYaAthUQYwdyCrkwN6kRkZme7OP_fVYW3tAAmwVzWLlTJbhFfKfGhtg6KnJAwbwimqJZjEQcMd1JEgQGIf_XD8MhxNxHEAmES1ZADXZLfzxxbWI0mDx1W4ReUJ3brMKHsHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNRRtM8Ub5gatRxGDA1v-Ku3MKZGYSlp4r53akXdw0yXuUt91902D6-beEuNq7os5Xe0xcZGbCOhg25gS7thNo-iVCRuIxUpR02-k-i7zV-HghbDRjBx1eye6xV1IUf5Bb1LrbMX-3SJl5EGH9u08QzcnrZiT7kiZ5RwWNC-NyUL3ke357LFNuIfO_ussL3lYgyTxH8Cj7ap7yuYD6PXWFFJtGXSn_uZhuYCt_TatIA_Z5SHsPJBYZEJIBRsbfqcdogAoqzO38ZhzDblyZV3znp--Z9BBTgKi-E4CvoWAKmyVz0BTdQVZN_-dPa_orxlgRaqV1dH65o7x7IYBUU2Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇪🇸
ملکه‌های‌آینده اسپانیا فعلا دارند با کاپ جام چهانی که بروبچ تیم ملی این کشور گرفتن عشق و حال میکنن هرجامیرن‌اونم با خودشون میبرن و چند شات یادگاری باهاش میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26291" target="_blank">📅 15:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26290">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kguIzhuNYQGcVHYhjo0uAUc1Cvy13pwSyOzKGpvxFEW5LJTV7wpd-_DiEb3HZSuFvkeIuUtJ27CM5CyGWW98ePA6-OVnUAMf-eBpRJJi_uxzscsI-AlUQb3pahNWQfwGEGmIVq4qnBRoqDxh4r9xKEZw1uQ2Ohhi6-jWmdAzBoq0TepMQuPKFb1h8ZtB1kVQa5Yow2-3rWSmSBmYniBMdtTWcOwIQViHtHhRn7ZdR6bHqvuK9Si-k11qDPfnG3WMR3GSgNcJy-VRieggwFGsZzwi27W6AEXIPHsq2zT1Sb5KMekUgH3koyDIY62uh5MtWD-gxvLawFCfxGBpQ2azPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26290" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26289">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXB8SypnwLLQcVs_iyPMVpFiXv_8aNihrf-8cuEI3kPZHiuDp9NHh8-aAfcPIuRX21JTo-BeZ3NRjhBLeyG-eWzoqUAoIavNyB05tm5mxm-o2L99FREuxU9GKVKXfQUk5ub2XNFUNeA3nplGnu_F2SOixRCPglh7ioiRHH52JvG6gqti2anr4jy6weq6ov2hGzQKkAgR6_M8sYBq2WNvjTE8jPF96PNYFlDeSIPKBUQZmYRjZsbpB-Gj7khLBFxRBKCV9iVPnwV43tX99Y-cfg8CAdyfZe0iwdzbi0eVvt52PHPY9548IFgYRpLPk6w9Xcx8ewCYu3I7gkBywSRoJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمایی‌که تو جام‌های‌جهانی اخیر تو جریان بازی نباختن؛ ایران 2026 و نیوزلند 2010 با 3 مساوی از جام جهانی حذف شدند و شکست رو چپشیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26289" target="_blank">📅 14:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26288">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaZi2Z8ARrMUw4IF0JSmGkOi81v6WQbuOcwyxBpxuGQlrB8YYZ7bZUFaeb6KNc1XCzJN5MSyXJK0ozDk16LJfUNLNFE9979SwkmVjdUBO8t3xQBVRMjBrD3gNXFYfhkE9N-KNYxyjcQ09xf4Daeljw4cipV6gwH7vtoMPb2qMbgM1rrsF5hWP5qLuL16ds81bvwDZi6PBQPJU3_7Kro92mD9-wbnDCeGhJMiOn8nwG8QojxWEw0bmPY08TPYIY1KfztPoRmM8FpDkGfKFsohZxBRhDvBLSrbmj3YrbyLRHX1THhUR4WB74cStbNHzh0llIm1H-X4fVnT3lIjL3r7Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26288" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26287">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N877_43mz8hw-dV0ccW7719IISKZ6iO6Um5gtq2Q0KBWre2eHgwmRThikxv1IkYZFtXLjeAb8PSYb26STDnZzKIjb6ZeBAyhraG1OC8U8DoCyL4os6-QptchnkCT8vuq-NZ44GDPPoruyvyerHeJ4i5wBu36UD111aFFQGvuxAN_PxqvhclxEhkKXWyfgG9bhBUe9-2j7dBdvO2Stlr_6r66gum-lvBQbY4s3_ReI1JWIN_2qRfEB16QXOCuSgXTlIgbqHfT42p58KfFx1PVI656u3Sf3AS2hR8LXP3KnAF0r148jUXEcMInBeuvQntV1WVrO7eQ4xnG0qjAyks4yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26287" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26286">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jn_nyn4MzmaG6xBCNpEY0L1pZhw7gyriP1nCnUcpuyVikRB6E8JWKAFcSJgwojUDK9LHw3AtNX3LUKthrl5nzyLxzDHNAgZkOxhn0crR-tx4SwU0AcpnC1QZ3Pox3OvDGUe3YsvNy3ow_rYr4ioo5GOOtrjhCH10B4ik1GBp7oFS5eIIoygwpW40-1V8KzE4VGU4xCbyDblDtFzbEonscftRp0nAf3VHepz9hbsT_sNvUGzMToldtX76Gq4szR_LfSjomT8lyj53uCXYIt7n38LXIjLtzxG52Vaeulq-_NlZs6eJzQQzzGzDF2B4oJZVh9jVvX3bpQxu_bBNRuI5FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی
: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26286" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26285">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhCp8rJ6NmwCV3iPxjkOSIvkypBhmSkRkHH7Rz1xM2Rav-nSrtI61hsSRzkwf-sJ4jEXaJqLH0SBtUfcIt8M2kPi0TBBaRKjh0jIcRP4SA_QNGmK266TqSjvYjDnyZaC71o2r_vmtkLC7HhtdrNExeeZc7cdChVhxM_1r3g7c8iLoaXJ9FbtCPGJY2bRbQ1xAWt9sOHbFBrgYov8h_IfOyOlimqkyqhSCny7sPSyw-skt919oK1Drr4wdQH82G7Ti0TAvNF0KRvwKqn2a5fB4MM4H6zIyx5IVDGzzD3QN57-ct3sv9nZ2dS7MPdq3pE9wrmbVhbkR07n0-NrwxkatA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26285" target="_blank">📅 12:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26284">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaqOzuvGMq31sVn6rKTx9wgdBmSN95bCldwpXOl3IfbfttfJfF1ffSlPhf-pfCqYOWAlQ1r9_FhinGsnwNU4watGKPhgP1aRbPkbaEb75A7FxbqX1mfaMPgaA-RvaFuBcoqwLh-Q8q7UhamStgmjjnyAJ_0-V1HfXQByrw2WPXLCesx6KG1RRYKsQKuVMh0ihoslVsC7v6qmQq_JdMzO8GxWFt--3WubCTMkmhGcLPsxRFgcjHm0TALmGOaZoU6NTqDstthdQbiSBvEZ02fN0QNX1tO2k8rczGaTiqfvF4f1A7VDf7h_h_WYXhsxkpxljtwQ2XhxpeTKbPRQvFVmDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
با اعلام باشگاه منچستریونایتد آندری سانتوس هافبک برزیلی سابق چلسی با قراردادی پنج ساله تا 2031 به جمع شاگردان مایکل کریک ملحق شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26284" target="_blank">📅 11:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26283">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJPe8xxGys6G9KjbtpPQ7jTK6wjOOa4kn1nB44rT7rrnFEIcPgrqjuCSFYUC_06RvEWLnGN2jDPP0oPfhUxsJNbF_XulOo18Eg0aQk-wMb_8iJpdrXQT5yqRSGO1fWHjqebWFSXOvN48BDDROD-3wT9GSURNq5KeKbxKka3iONpMF23uKCkLCXfcpceePCBENXAtOtLjRYfNVD4zKm6DGUJ2dWHbAZmB3IgWb-uXD0UgPMCT4-IZvXl8wadWD8lA0KIdn2M7Fqa38Mwgg55j_0__nGsj1PdHhCDK8tGkdESsCHixrJv5CPl22Q1Or5XuidHk2HBoaIHzOBeNp6K_ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26283" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26282">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-AjlvNnCtCNwpcQ3OWxCbsdz96Ps_l6zfEGs-B_XzKEwjic94yvCZdoSvZeRBcM_Bs-E1vmtP9ZYXB-gJgm7Solhq3emfzyLbyH-I2GzdOUYZGvwpZiba_pEJw9yM-vMhuqW6tZba6v3LLH6iAi11iYmcj2MlMQcx1_0hoKadvvAJmcJSjIEko4euZunvEAU85pz6whJHBIaEdJNf8zyoEECOl2JiBWWvuttRhYs4gCeRn2QtlQ2iVHHMc0JcxDoVfpC-7ycJ7hPeieD7WQnV60pKKKPHOxziWyWZutsuH7XrSFhnBLiWEmDEzSTMqZ5V5-4_meESKip8s7v9seSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب‌کهکشانی‌وبرگ‌ریزون رئال مادرید در فصل جدید درصورت‌قطعی‌شدن حضور اولیسه و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26282" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26281">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPj2SYRctKbZ2xuGT7EJXgEFi5kiNoa1g_D69lZFvbKThPF0wINQIP26Z9n7hdjZH2jiiPD6rKR02KZmVObeG92ayAPZPRo5hPL-FhVVc2gdhpZtZDLdWCAuNqxJYTqqA6vpenvha0DqD7rlv9PeUdaWWyPOzj_XgUfQY1oDLq2j0YgjSdtoGaM2KTEoFoVNmyBQgFOetP4nZWySbtzYNU_c3SEW6vtoXXWBDM05IE8atWUS9SXHZOnguF0t3cfrr2kWJyYw8nTBKR9mVhIJZWW7ruIrAOPdDmbdIU28LT0C4G45Xtq1G1Yl5eS-N5UVIgXwzsNz9-YHHUNZVURiGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ دیمارتزیو: مالدینی مدیرورزشی تیم ملی ایتالیا مامورشده‌‌که پپ‌گواردیولا رو راضی کنه باقراردادی چهار ساله سکان هدایت آتزوری رو قبول کنه. بایستی صبر کرد و دید پپ قبول میکنه یا خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26281" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26279">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUfhnrPruCaoKF4wN-hDMsXqKHNuSfowv9DODiNCQ_VIzrGZLjIR35IBVYvunahFeA6iA9EOE8Kjn5UK_hoOYt1vFhZLxFGDfm4b5OsZBkOfvlBqcgzNXTH9xLzroCEnvP7Pcg6mutVuOseAkbjxIyb3X_5ZXj7IfHdASdylplAVzs4wrYZqe-htU73AD-ij_SBcMoiVuHJaKEEkdSyPn-H_O92k2fckVvIrvRHyIzOQHl4_ow-E7XNqlRu4Xsutyno2hbLVMqhVR-ZPG5a1wXB4jM-8onW_HUewMx0A-tcyh_23tLFbeWB86R9adAMzkGzhA8cMos1jPCLbO8-8dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26279" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
