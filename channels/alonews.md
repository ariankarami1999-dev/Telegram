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
<img src="https://cdn4.telesco.pe/file/jW8HgcMaa6S0DbXrCVgQtF4GWovb6N9K4yTh2LyIHiukXoU8HuQ4r-27uq988k649K0mJx6w_GaM1u-Lcau_9aTKr0IJJ9UGJfi-MVDdo0l-r8bS3YFG_je8Rm3wfKnIiRTTYUL_Lkncg0SfNX49vwYDJ2pwzVG6OjK2ynDqBr8t_m9OCic-66W0-gYi0AFyTyBX_VS8Lx_XxDEiQm_Qs-3kAbRwtiYF0mpeAvQSagsfTmjeGXUYjNlrvSkFFleFA8dVg0i5DqI6yy50rkqa1u3qgG1Ng5Hg0L-Dtf7znqvfnB3_zDaCpwMdlHjfhVj3Hjp-oiJNRjf6O3NtJkLxZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 969K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 23:10:48</div>
<hr>

<div class="tg-post" id="msg-142134">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏
👈
سپاه: پدافند هواییمون حتی ۱ پیچش هم خارجی نیست و ۱۰۰٪ داخلیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/alonews/142134" target="_blank">📅 23:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142133">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/In3FzauHw7N1x3amQLJhbTbX8p1YqHJ2pEKMNeW_R-Xau6Yc0sRhv_DFbOB7kD1wetm-3qcuv9gZ9b49NETYhVIZ5_68cRybunSpLChS9tWOpiHWHngPtQPhoKI28eJv7C_lzOWT1NCHlV0VkB6IW-VD4WwUe1L-GP_X4bwOw7dLgWs-_V3IQtTkH1Q-6Tvlz2ZnMD3jUAUHEV6x4zDlB8cC9nmixKY6ts5UCQAz4enIJ46JjSd-jiW0DZS1Rkafymipq8nbWmFYTM_FWIVHfRCvr2ybBjB_wvBO_O-pGYciOM1-q5kAn543nSWYlLobxkl3ruecj33xRYH0wLMzRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نظرسنجی سقاب اصفهانی در توییتر درمورد ۳ طرح بنزینی دولت
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/142133" target="_blank">📅 23:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142132">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7V5oEGCSeupZKCPl7PBNG_oOuS6ZJo2hhuCPKYkuZlXYiqjhaoyh8zAE6ia5pPjoXfH8mU20l8QbMutydtVQ-fJtCEPUH1dXSm6XJUNSTVFXV-38uzlzjfMmwf2x0lweH-2SLbFRyV5q4hHZjNT0xD6KPUPhdvXzLydfoSjfx5PJHPlBy1LzZ4JfDCJYweSAmXRGjghJBlnRa6yqHhjYzAf6-OnmaPEuRL2PgE9bhLmZK8SAoE4WeuZOhuoZxO7KAsKCtZg0Na7iQk-qKjj2SJWH69apZJtgUMNLSEOzZzYUrCoPzYOqXfEC4jJgbMkVVNchekgH1U_CYncEKie6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو با انتشار این پست در اینستاگرام رسما تایید کرد که مجتبی خامنه ای زنده ست و گفت اینا نمیخوان من تو انتخابات برنده بشم. نزارید اینا به خواستشون برسن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/142132" target="_blank">📅 22:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142131">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
قالیباف: ۹۰میلیون ایران حامی نظام هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/142131" target="_blank">📅 22:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142130">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f93f0bed1.mp4?token=IN0b_IIbxWtqQMWy6X4QGdX5ASkRRtwclESC1EriqsMP9Co1UbjW8Kf2Wh_yaBWw_yBAfP4MBHuMbVF3VNppzhopYwf1cViQTNK2jdbf5tad5Br-_VxqWbVyGuVP22IZuZYTATc9TTZ7ZLnuUJ9L55u5VBbAvjQ9Nph8YznsAgvqkiBsqU_N_jxnFogD80hfMeTePmuIBiA0oc87p804eI3jkLMkrNDScyC1fyHxRoD-e0viJ9XMV6gtNOqzqy1HTI94RshJr0IJof2V7m3uxfpv0uWDntjvRnvqu696ehfADtm2F1EVeI3pNrug0a7hhKEI_TeBh9KJqkG4g8SOnVGDM6EcpI6-kGJKTJgYIgUBrEWhbQkDbBNgIhbwXzytSpZbn4UrBBu2vUmGuvF7IXQ3oaruGfVGB62XcHBvrtKenI9v71o8JfyDU0AHvLQ7HKj9AClJiRyGSXrt04bN9jmTQKLYlTDPIyj8W2sGXazeDUDOVBAQYsau0xSOSBC9LNwiPV7dA0HIJ_o6XsdJ21wBU-6We9qP8JVhx5RyaX6DfJwCXucMgJ7OuJJBH5_FvD0ZHloaPI_qyy814WBLpqYdhTgTwOLgnOdQ9NCtbaFD_LdFyCdAdjSCW_cM56KltrlVCxBTdecRXaVoQJ7LeqhEUB5llUNQVu1RcuP7Mb4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f93f0bed1.mp4?token=IN0b_IIbxWtqQMWy6X4QGdX5ASkRRtwclESC1EriqsMP9Co1UbjW8Kf2Wh_yaBWw_yBAfP4MBHuMbVF3VNppzhopYwf1cViQTNK2jdbf5tad5Br-_VxqWbVyGuVP22IZuZYTATc9TTZ7ZLnuUJ9L55u5VBbAvjQ9Nph8YznsAgvqkiBsqU_N_jxnFogD80hfMeTePmuIBiA0oc87p804eI3jkLMkrNDScyC1fyHxRoD-e0viJ9XMV6gtNOqzqy1HTI94RshJr0IJof2V7m3uxfpv0uWDntjvRnvqu696ehfADtm2F1EVeI3pNrug0a7hhKEI_TeBh9KJqkG4g8SOnVGDM6EcpI6-kGJKTJgYIgUBrEWhbQkDbBNgIhbwXzytSpZbn4UrBBu2vUmGuvF7IXQ3oaruGfVGB62XcHBvrtKenI9v71o8JfyDU0AHvLQ7HKj9AClJiRyGSXrt04bN9jmTQKLYlTDPIyj8W2sGXazeDUDOVBAQYsau0xSOSBC9LNwiPV7dA0HIJ_o6XsdJ21wBU-6We9qP8JVhx5RyaX6DfJwCXucMgJ7OuJJBH5_FvD0ZHloaPI_qyy814WBLpqYdhTgTwOLgnOdQ9NCtbaFD_LdFyCdAdjSCW_cM56KltrlVCxBTdecRXaVoQJ7LeqhEUB5llUNQVu1RcuP7Mb4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تنها رهبری که میشه گفت هرچی بگه همونه، مابقی هیچ
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/142130" target="_blank">📅 22:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142129">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18fb8279c6.mp4?token=JDFQhHua79GB61QQ57BcoldDmiX4kamsIS6EPL5GdszQ906ggqRwxxtwEIOqW4B0IG3ROWMjcXBLGD3kCkg-FMt90zUI3CEM8j4PbyTD_Fre7lD80S4rRM4KWbWNsI-_XG7ZGlVVxuRFoleuDnlC8vu2HtcNe6lJnIYjsBHQryhaMycorS521Ey4fNoCSt5cmACcgo2xeUF0OZQW-dC1uI1YrNCiBPB2jbhQd1dDeJyHx_nGOwEyvpZPdCZvK4MNQ0VtJy1N4Oz0M8Q9FeR8xTCGo6bSInVLjZWYiY6ph0lM5h2-eO4UtEMFKfp8h6HHz2dtkl0MkQZKQC7YKjoSuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18fb8279c6.mp4?token=JDFQhHua79GB61QQ57BcoldDmiX4kamsIS6EPL5GdszQ906ggqRwxxtwEIOqW4B0IG3ROWMjcXBLGD3kCkg-FMt90zUI3CEM8j4PbyTD_Fre7lD80S4rRM4KWbWNsI-_XG7ZGlVVxuRFoleuDnlC8vu2HtcNe6lJnIYjsBHQryhaMycorS521Ey4fNoCSt5cmACcgo2xeUF0OZQW-dC1uI1YrNCiBPB2jbhQd1dDeJyHx_nGOwEyvpZPdCZvK4MNQ0VtJy1N4Oz0M8Q9FeR8xTCGo6bSInVLjZWYiY6ph0lM5h2-eO4UtEMFKfp8h6HHz2dtkl0MkQZKQC7YKjoSuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف(ممد سامتینگ): مردم حس پیروزی را آن‌گونه که باید، حس نکردند
🔴
پ.ن: حس که چه عرض کنم اما این پیروزی خیالی تا ۳۰سانت به مردم فرو شده فعلا، البته شماها سیر هستید و متوجه نمیشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/142129" target="_blank">📅 22:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142128">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ef704c6a9.mp4?token=ZlxNaGD_MpFGWvYOnYl8kYumQ1EI3T_sNJoPiVhz6iELrNDczRsM7m1bTQXmdq9PvEYseQHs_Y9aodgflVw3jRInNFim8MrhvS3s8DQqJLpjMO3GhlHQjJ8nufwWsScKRoMR-Kq8OmwY-3R3kxb2K5mpEA4_J8364Z0XDUh3jJoYFXX1QFGLZlKMeCWgn3mYAwF98es9uCersvWnHQyOTOesa5x4wBFyL8-Zf_DHF-InqX4YbPRiqzpB7XgIHoybXgI2QduNw_bNgiVv-_fptFmdmc3kcvyzlYadWt3Vzl0PewRAVZd6_Tidpo7Mk78cQf5Pnpef7AQjXaM98zKB6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ef704c6a9.mp4?token=ZlxNaGD_MpFGWvYOnYl8kYumQ1EI3T_sNJoPiVhz6iELrNDczRsM7m1bTQXmdq9PvEYseQHs_Y9aodgflVw3jRInNFim8MrhvS3s8DQqJLpjMO3GhlHQjJ8nufwWsScKRoMR-Kq8OmwY-3R3kxb2K5mpEA4_J8364Z0XDUh3jJoYFXX1QFGLZlKMeCWgn3mYAwF98es9uCersvWnHQyOTOesa5x4wBFyL8-Zf_DHF-InqX4YbPRiqzpB7XgIHoybXgI2QduNw_bNgiVv-_fptFmdmc3kcvyzlYadWt3Vzl0PewRAVZd6_Tidpo7Mk78cQf5Pnpef7AQjXaM98zKB6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی: تو نمازهاتون شاه رو حتما دعا کنید چون هرکاری کرد اما با دین مردم بازی نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/142128" target="_blank">📅 22:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142127">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
۲ساعت تا پایان آتش بس
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/142127" target="_blank">📅 22:23 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142126">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zo1X7vKTw36wh0CD_C2-ZGW9ELFeV7d3lnqlAJoMZrSyDfma6O9vFe8QX74uX2mxGj_A35C8Xr5ZO7Yxd-VjwAi0pwFTT5mr_1Zq2gXJFREO2wgUsd9pNfkyMhB9_gTC2ZzbiWNxR7hwJZ70sm9mD3i_XiGzefDRS4Av8Q610WUHAFnOoJfBH7Oo6-VSPpP84kkFlgF9mEdqvycP3W5eSd8BGF94fQ_ND6emNtJ-8isaVRCFy9NFAaNsKJHkYCSnTnbAikeuhasbXkIg4UfMx_0c2QZneV84i8GNWRENMcFAK5MeoiJowVwMc7HuLQnjT7jh6wFLaAuOuG6YnXcdtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عامل آتش‌سوزی عمدی مراتع هویر دماوند متواری شد
‏
🔴
عصر امروز آتش در ارتفاعات حاشیه روستای هویر دماوند دیده شد؛ حریقی که به گفته رییس اداره حفاظت محیط زیست دماوند عمدی بود و عامل آن پیش از حضور نیروها از محل متواری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142126" target="_blank">📅 22:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142125">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
جوئیل، بلاگر ایرانی آمریکایی: علاوه بر رامین رضاییان چندتا بازیکن دیگه هم اومدن دایرکت و شات گرفتم بزودی پخش میکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/142125" target="_blank">📅 22:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142122">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PK3_0kR6ufxgqwjhx9p-jJwZDl8SvhRjrKFDVSjn5RYGlBM9D-4CfjRZAdAj0sSI_MjHJHvEyvHkwmseX4zKYF-ilq9bqIRyQ_msSR3hbSczwA2JJzUZlbrOsdLX7m0oQtF1vwaN515eShW4et4omNQv7_oJF2Q4dKFudLTuoJ8BI7q6lLwO6h44izM65_gmadTy3JILb8hjo_5ezZjosnUa6h5caXUQgjfpOZeb5xl6L_vhVAoJZFbb5ZjIfvcyV1i7cPL4dczC519eEdU-7zCbUzg_pkXnrJGmw4ETWBTwINSHGhBr668XxGG6oaW2VccMlK89UEYYHjF_S-hsOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جوئیل، بلاگر ایرانی آمریکایی: علاوه بر رامین رضاییان چندتا بازیکن دیگه هم اومدن دایرکت و شات گرفتم بزودی پخش میکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/142122" target="_blank">📅 22:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142121">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
آکسیوس: جرد کوشنر، داماد ترامپ فردا با  نتانیاهو دیدار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/142121" target="_blank">📅 21:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142120">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoMVT9zY7wIMPqDc9t-8LrU92tE7nq-CAXabUiv9F3YknzqF7X42iHkbj6KyvSja57X39FC6Vi0QamNZZtcE8RmNfsklqfZCrlRYO6fbJ-nZbLcwjWAgWPLTnu5R3S7L-AHGhKuJ01u26ULyKGnfLVqYYw-CkzDfdRBY_bZGnLodqmgCVgSy7I6MZqp7ieEu8yjKIK4ecuiA0d4esDaVo85OJzlQ9tFiQekWJxfYYh-mQwViYew_ziVxVxm6pyTFH4uSLv55d6HB0AonioBCDnTIjQ9eBS73gwABzSWQ8MgUrBrAcF8fEVWamqmAXUVFbqxd-5brBkHCRg5ZeUVEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۴: «ثانیه‌ها به شماره افتاده‌اند.»
🔴
کمتر از ۲۴ ساعت تا پایان مهلت اولیه ۶۰ روزه برای صلح و مذاکره میان آمریکا و ایران که در تفاهم‌نامه ماه ژوئن تعیین شده بود، باقی مانده است.
🔴
این توافق موقت از ابتدا شکننده بوده و با مواردی از نقض توافق، افزایش تنش‌ها و ادعاهای پیشین هر دو طرف درباره پایان یا تعلیق آن همراه بوده است.
🔴
تاکنون نیز هیچ تمدیدی برای این توافق تأیید نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142120" target="_blank">📅 21:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142119">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
به گزارش واشنگتن تایمز، اسکات بسنت، وزیر خزانه‌داری آمریکا، از اعمال تحریم‌های جدید علیه ایران با هدف افزایش انزوای اقتصادی این کشور خبر داد.
🔴
این اقدامات قرار است هم‌زمان با ادامه محاصره دریایی آمریکا در تنگه هرمز اجرا شود..
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/142119" target="_blank">📅 21:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142118">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نشانه‌های ادامه پسرفت اینترنت ایران: اختلال‌های تازه و نارضایتی کاربران
!
🔴
اینترنت ایران در هفته اخیر نشانه‌هایی از ناپایداری و پسرفت دوباره نشان داده است. داده‌های فنی از اختلال‌های منطقه‌ای خبر می‌دهند و هم‌زمان گزارش‌های کاربران از کندی، قطعی و دشواری دسترسی حکایت دارد.
🔴
بر اساس نظرسنجی دیجیاتو درباره کیفیت اینترنت که امروز، ۲۵ مرداد ۱۴۰۵، انجام شده است، ۷۹ درصد شرکت‌کنندگان گفته‌اند کیفیت اینترنتشان در طول یک هفته گذشته بدتر شده است. تا لحظه نگارش این گزارش، حدود ۳ هزار نفر در این نظرسنجی شرکت کرده‌اند.
🔴
آخرین گزارش فصلی Cloudflare نشان می‌دهد پس از بازگشت اینترنت در خردادماه، ترافیک HTTP ایران در مقطعی تا ۹۰ درصد سطح پیش از خاموشی بالا رفت، اما بعداً روی حدود ۵۹ درصد سطح پیش از خاموشی ۸۸روزه تثبیت شد. Cloudflare تأکید کرده این سطح بیشتر شبیه وضعیت پیش از خاموشی اخیر است اما به معنای بازگشت کامل اینترنت به شرایط عادی نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/142118" target="_blank">📅 21:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142117">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/203d5aef6b.mp4?token=b8YLWyVpXD_c7rhN_rhixk1BZSfW19TcFus5dWtzvQ40h1yKktFRDtDZ9S0l14QK9_TLvBqX47bIeb2TSoPdmbHy_7S9KQP-MP0S_7hOAb0hY-HjYs-1g26uxOZQRIxoMriTwDDgXMt8eUqfwEVVtst8PaI_-LBh6Qglovmbpo-bb-TiA-QDViR9zosUffkzRicL0YbMGJmfI6rxDY-ppmi2c8cfSgrCiAD5m87bTEVImU04pt9yaK7QKjT3jqnVlW4gZW4Owy6dK1I-isyYtvmV96mrQzoy17cO4NfsMSpX63uwBU0_r1xqxGOnT614R4X-U1TbhcW3vU4Ojex_4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/203d5aef6b.mp4?token=b8YLWyVpXD_c7rhN_rhixk1BZSfW19TcFus5dWtzvQ40h1yKktFRDtDZ9S0l14QK9_TLvBqX47bIeb2TSoPdmbHy_7S9KQP-MP0S_7hOAb0hY-HjYs-1g26uxOZQRIxoMriTwDDgXMt8eUqfwEVVtst8PaI_-LBh6Qglovmbpo-bb-TiA-QDViR9zosUffkzRicL0YbMGJmfI6rxDY-ppmi2c8cfSgrCiAD5m87bTEVImU04pt9yaK7QKjT3jqnVlW4gZW4Owy6dK1I-isyYtvmV96mrQzoy17cO4NfsMSpX63uwBU0_r1xqxGOnT614R4X-U1TbhcW3vU4Ojex_4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال خطاب به جورج واشنگتن سازنده کاخ سفید: از شما، جورج، برای برخی از ایده های درخشان شما در مورد این مجتمع نظامی/اتاق باله بزرگ متشکرم! پرزیدنت دی‌جی‌تی
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142117" target="_blank">📅 21:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142116">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
به گزارش بلومبرگ، ۸۳ درصد از شهروندان چین معتقدند مزایای هوش مصنوعی از معایب آن بیشتر است؛ در حالی که تنها ۳۹ درصد از آمریکایی‌ها چنین دیدگاهی دارند.
🔴
این گزارش می‌گوید شکاف میان افکار عمومی دو کشور ممکن است بیش از آنکه به خود هوش مصنوعی مربوط باشد، نتیجه تجربه متفاوت چین و آمریکا از موج قبلی تحول فناوری باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/142116" target="_blank">📅 21:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142115">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
منابع دیپلماتیک به الجزیره گفتند که اسرائیل حملات اخیر خود به انصار و دیر الزهرانی را با بیان حضور مقام‌های حزب‌الله توجیه کرد و با ارائه عکس‌ها و اطلاعات به ایالات متحده، سبز کردن عملیات را به دست آورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142115" target="_blank">📅 21:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142114">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c241046bc.mp4?token=a2j8ph8YxaJxuFvUNYUbXEHAMEkcIQVAJO9eHmi7zRlpiUyFaZ3xF5ylyyt36eNuFS7QCT5xn1NBsPYonItUmvBMfO9b5YJm_VUjSe4AgBRH5Bjv2-eo1pcG1EVuCByOtkzyHggAHwqVr2rpFFAOgmSP_97zRPsSwsozuBXeivO11yyq1BO4Q8WCzuD4pc8SzCXvtMQnJ2XbO2fHnOXW4o7lev5IeeP4MnqoXK_ZCFucEKyTEsnHgh7uuGSOp7lFA8DVkbDlOiZ5Plv5coA14NXYZ2pRDqmTsdbGQI1VCqHDi-mE41Kt2QnwrSZ5Hn-AKb3gKtF91KgjTLtHuh7Oqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c241046bc.mp4?token=a2j8ph8YxaJxuFvUNYUbXEHAMEkcIQVAJO9eHmi7zRlpiUyFaZ3xF5ylyyt36eNuFS7QCT5xn1NBsPYonItUmvBMfO9b5YJm_VUjSe4AgBRH5Bjv2-eo1pcG1EVuCByOtkzyHggAHwqVr2rpFFAOgmSP_97zRPsSwsozuBXeivO11yyq1BO4Q8WCzuD4pc8SzCXvtMQnJ2XbO2fHnOXW4o7lev5IeeP4MnqoXK_ZCFucEKyTEsnHgh7uuGSOp7lFA8DVkbDlOiZ5Plv5coA14NXYZ2pRDqmTsdbGQI1VCqHDi-mE41Kt2QnwrSZ5Hn-AKb3gKtF91KgjTLtHuh7Oqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش ترامپ به استعفای سخنگوی کاخ سفید
🔴
ترامپ: من متوجه شدم که کارولین بچه‌هاش رو بیشتر از من دوست داره و من در این مورد خیلی نگران هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/142114" target="_blank">📅 21:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142113">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بلومبرگ: انتقال مخفیانه نفت از تنگه توسط اعراب
!
🔴
‏بلومبرگ نوشت: به گفته افرادی که از این محموله‌ها اطلاع دارند، انتقال نفت از طریق تنگه هرمز به‌صورت مخفیانه و بدون شناسایی، و سپس انتقال محموله‌ها به نفتکش‌های دیگر در خلیج عمان، با حداکثر ظرفیت ادامه دارد؛ این روند حتی با وجود حملات اخیر به کشتی‌ها متوقف نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142113" target="_blank">📅 21:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142112">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
امیر حاتمی،فرمانده ارتش: اخراج آمریکا انجام شده است و دیگر اجازه ورود به خلیج فارس، دریای عمان و تنگه هرمز را نخواهند داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142112" target="_blank">📅 21:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142111">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
حماس دفترشو از قطر برد ترکیه و این کشور شد پایگاه اصلی حماس
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142111" target="_blank">📅 20:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142110">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فرماندار شهرستان بندرلنگه: ۹ صیاد بندرلنگه‌ای پنج روز پیش با سه قایق جداگانه از اسکله بندرکنگ و اسکله گشه راهی دریا شده‌اند و تاکنون به خانه بازنگشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/142110" target="_blank">📅 20:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142109">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ان‌بی‌سی نیوز : ناو یو‌اس‌اس جورج واشنگتن اقیانوس آرام را ترک کرد تا در بحبوحه جنگ با ایران، جایگزین ناو آبراهام لینکلن در خاورمیانه شود.
🔴
این اقدام موقتاً غرب اقیانوس آرام را بدون ناو هواپیمابر آمریکایی باقی می‌گذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/142109" target="_blank">📅 20:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142108">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
پزشکیان در جلسه هیات دولت: محسن رضایی پیش از این همکاری خوبی با دولت داشت و امیدواریم در مسئولیت جدید نیز هماهنگی، همکاری و انسجام به خوبی ادامه پیدا کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/142108" target="_blank">📅 20:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142107">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db02877d6b.mp4?token=kY-l3XT4KV9vQ8VihQlqMYqkQR46fEpG1EtrtWRvCGJ495Dtb4iQ-9md0PP-Gvj9PJJ1MCZyPRl9UeliXNI8wPVkB72tmZ00kt9_hIa2fgty35bNS9yBt8sOd5XTlCJXRCGnhUfITOEB8SIhasAu4jq6MRzfHORj7PRZt0RK1miyHxjdg7pgtrDd6ts29K4JP2NnSspqoGwQojk206gjQuSEgJ8nrDxCaTw9Cy7RaDaiiiJlKcunQy1fF1t11kVNHw6AdBrg-DptP5fXLNbr1KgwUIaPjeJniJzqusjji1cu8Nua1_t-hxqtq1n_jRvuoToozhpMNPZUONtUQV282w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db02877d6b.mp4?token=kY-l3XT4KV9vQ8VihQlqMYqkQR46fEpG1EtrtWRvCGJ495Dtb4iQ-9md0PP-Gvj9PJJ1MCZyPRl9UeliXNI8wPVkB72tmZ00kt9_hIa2fgty35bNS9yBt8sOd5XTlCJXRCGnhUfITOEB8SIhasAu4jq6MRzfHORj7PRZt0RK1miyHxjdg7pgtrDd6ts29K4JP2NnSspqoGwQojk206gjQuSEgJ8nrDxCaTw9Cy7RaDaiiiJlKcunQy1fF1t11kVNHw6AdBrg-DptP5fXLNbr1KgwUIaPjeJniJzqusjji1cu8Nua1_t-hxqtq1n_jRvuoToozhpMNPZUONtUQV282w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دزدی خانوادگی یه خانواده از فروشگاه:از دختر بچه تا مادربزرگ، همه توی دزدی نقش دارن!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142107" target="_blank">📅 20:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142106">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dndjrdd0v--OSrNqco4CjptlVIlRaqB35jbqeg5c_r0SPiUeys_xYsA-MCIsTO8pgATuGBJdxlW6p_RgCSYLxKwjFtCaL_RwsP4keA-maw4_XXg1Gg7Hj8q1Ez2etG2Z5QwEc4MvTCl3VIgyDDRd4NcLBruitUtjhkFo2XmM8575u8-7sFaLCAd_6jWmtvE693qtdKFDn0aH8OmllFu4JsLQtBThVU9rMf1ZFxK_vYUiyDGXT4UZYCEk6sMjI1_U3jcD3wauhnDHRPozQlhI-bCjBrxJjc8XmM6VwQ4os5BRvshbB9bfSVvnha6zD7shiZ1S2YsF5Css_CJnO7QIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پدر مهسا امینی:
کلماتی که اریایی‌نژاد(نماینده کثیف مجلس) برای مهسا استفاده کرده سزاوار خودش و خانوادشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/142106" target="_blank">📅 20:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142105">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
کارشناس صداسیما: مشکلات فعلی کشور، ریشه در سیاست‌های دوران پهلوی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/142105" target="_blank">📅 20:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142104">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b6a1f4993a.mp4?token=emti-oiTB7_rPZWazCvP6cl_i1fjIg72Ro-2ve5yyO9zm7Sg0eDMK5uavWIq4D9pdFQTc7pQQhC5yuCx04mqNjihcfgAx-E6Ecn4MxOylhwfIwtanibTFS6dEfFCMvufeo6Nko4cKPUESmLG-f07S71Wj9jM04LdLKzFUQn7WRHfJXUAhtB9hgwUvGGfaxKcIDM92njPXiAOtpaqmA-ooCygxu1HFiV7JNI71NIyk-jlJHV9srK-byZZcCuJXrfYbAnqNToe3kgV-SxNjS-aZqmf0diz_5GVW4AwJ5OfKfLThndnHnyXfCVna888N-wh4t6WystOor_a2zQD_fnXdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b6a1f4993a.mp4?token=emti-oiTB7_rPZWazCvP6cl_i1fjIg72Ro-2ve5yyO9zm7Sg0eDMK5uavWIq4D9pdFQTc7pQQhC5yuCx04mqNjihcfgAx-E6Ecn4MxOylhwfIwtanibTFS6dEfFCMvufeo6Nko4cKPUESmLG-f07S71Wj9jM04LdLKzFUQn7WRHfJXUAhtB9hgwUvGGfaxKcIDM92njPXiAOtpaqmA-ooCygxu1HFiV7JNI71NIyk-jlJHV9srK-byZZcCuJXrfYbAnqNToe3kgV-SxNjS-aZqmf0diz_5GVW4AwJ5OfKfLThndnHnyXfCVna888N-wh4t6WystOor_a2zQD_fnXdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام همین الان ویدئوی سوخت‌گیری یک فروند F-35A در آسمان خاورمیانه را
منتشر کرد
🔴
سنتکام: یک جت جنگنده مخفی F-35A نیروی هوایی ایالات متحده در حین گشت‌زنی در آب‌های منطقه‌ای بر فراز خاورمیانه توسط یک هواپیمای سوخت‌رسان KC-135 Stratotanker سوخت‌گیری می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/142104" target="_blank">📅 20:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142102">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
تام باراک، فرستاده ویژه آمریکا در منطقه: حزب الله 40هزار نیرو دارد که هر کدوم ماهانه 2200دلار حقوق میگیرند
🔴
پ.ن: اینجا هم ماهی 7دلار سهم هر ایرانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/142102" target="_blank">📅 20:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142101">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
2دلار یارانه دهک ۱ تا ۳ واریز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142101" target="_blank">📅 20:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142100">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
یه سوال از دلواپسان
🔴
قِر دادن ۸الی ۱۰ شب مورد نداره؟ آخه هرشب شاهد رقص پرچم هستیم و من تحریک میشم والا
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142100" target="_blank">📅 20:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142099">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
جرد کوشنر فردا با نتانیاهو دیدار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142099" target="_blank">📅 20:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142098">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
پزشکیان: آن عده‌ای که نان خودشان را در دامن زدن به اختلاف، تهمت و دروغ می‌دانند، مطمئن باشند اختلاف فقط به نفع آمریکا و اسرائیل است
🔴
انتصابات مدیریتی باید بر مبنای شاخص‌های علمی و فارغ از ملاحظات سیاسی انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142098" target="_blank">📅 20:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142096">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuIkF9vhFv0HTvDh5Xq7edQRr_g7DmAy1NIqjVPMll1msrE5o_tX-4nhUI1xluMRDj-bAmNw4AUXUrcaJ5Ps39LYIHNt7E7NRAYjgjW12xqwTr41aYRh4cwX17-8vwE5biJPWzbaRjoc_h9HnmJULbXU-7N0-pMeRpULFq0skWhvAZWN4rhtIRwB_rm-kou_tyCHg-5gt3sNfyEKix9NADAenNC6Ue38-C6MmtaMGqqDlaZ6lugI1K5Sa08Ii46GeZp_iy6-bfbtFEzd3YFt3Yo71hp0sXmJbFwJoHSVyOpT3CxJrlnLj829pJNnFbOfX0gA8AylwRISsYrLl_n_sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجتبی خامنه‌ای به مجلس: هوای مردم رو داشته باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142096" target="_blank">📅 20:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142095">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UupJRY_WhCfeozITmd_oUvVx68qoyh8FfZJDdh18yF7_ied-WRGUwlpMexq4_lKGp65BbJ7C-G15WVwswlsqg0r3tqfE1zjezHsx4oKvhGMgfPQ2GfIjy_LgyY84J2hgBJLp1HaDOuavp8-r8wZA3a3S5fR05o9ymxOVEe0K7wMdF5yGOBBxD80H47uDh_2TOzDeyBDzNbRKHOp4glfTXa4k6XdTgubK3fAPiD4B7ioDAdCWZWG2I-4PIGVktOgciJGZEujDtJrKyznSfjuh1OyksEs3bBBlqZONlT8o237XQapvoZFN8uJ-644hIIQMgtt2hR9WQ5-rfliia8pp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله توپخانه سنگین به بیت یحون، جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142095" target="_blank">📅 20:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142094">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/269325e5d3.mp4?token=T1i1p9IxIhVBUED1mVaSyrNcwZGsKFZqVSVx7YReOm7RmFP-WOaNixKcGAAFkPdMcbAEFX3kEoP-8R52CuGo3HR6h3ksHtMYo5TavHQNqFSoFkfvJR2dj2vV2ACKT2PRxHuwEdeiuiYzj9z0XWQJW8bJM_oEIzKpdqkvOuZJK-Q__zGGtGIOkJApwLv4UGvS5msfaQwrwVd0OMkdx3fedey9CQgh2P-f0eB21Wolpl4zyjnuhevwn9mdpPMlK5zp9FlVbw-NmudLyfsBgHXuXh0U5NBhy8-ZB8w73fuKq_9HmB8uX8XAhAWffB44N8lNhu8ZbTRlMC_qx61Qxky01Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/269325e5d3.mp4?token=T1i1p9IxIhVBUED1mVaSyrNcwZGsKFZqVSVx7YReOm7RmFP-WOaNixKcGAAFkPdMcbAEFX3kEoP-8R52CuGo3HR6h3ksHtMYo5TavHQNqFSoFkfvJR2dj2vV2ACKT2PRxHuwEdeiuiYzj9z0XWQJW8bJM_oEIzKpdqkvOuZJK-Q__zGGtGIOkJApwLv4UGvS5msfaQwrwVd0OMkdx3fedey9CQgh2P-f0eB21Wolpl4zyjnuhevwn9mdpPMlK5zp9FlVbw-NmudLyfsBgHXuXh0U5NBhy8-ZB8w73fuKq_9HmB8uX8XAhAWffB44N8lNhu8ZbTRlMC_qx61Qxky01Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی پرچم‌های اسرائیل را در جاده ساحلی جنوب لبنان بین نقوره و صور نصب کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/142094" target="_blank">📅 19:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142093">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEw63_kBNUM84g_QXq43HtcEPLXjJ9y4PrWQ7rjomtDlG8XTLjiFV8GmyJ1-GwTX_5BiCOzGBPLcuxjbHmxsfy1SpMzSeOTQHAahOjrM0bDdQGblSILyqdFPOoMfQHxkbZ19TlJA64PIGtyTFJ9TFWkaEUGq-J76Zl0inENVGGC2D43V1MGk3cvAppQAuVSR02-2lmE7nwNsasS4K5Vsdhhx8yhJoPluTOFX9ZbbcuFjzB5aqGlomw11-UN15C6iEAkOn7yvwIrTSfhv2qE_3iW9E5bWovPZ_LI4XpnUgDK8MCmSYEAUY2P0TrAVt0o2oOPgFrtqx2CA81bRRSll1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند لحظه پیش، یک پهپاد اسرائیلی به منطقه "علی الطاهر" در جنوب لبنان حمله کرد.
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142093" target="_blank">📅 19:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142092">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کانال ۱۴: توافق ایالات متحده و ایران با انقضای مهلت ۶۰ روزه فرو می‌ریزد
🔴
مهلت ۶۰ روزه توافق‌های میان ایالات متحده و ایران در روز یکشنبه بدون دستیابی به توافقی برای پایان جنگ یا رسیدگی به برنامه هسته‌ای به پایان رسید. درگیری اکنون به یک نبرد اقتصادی بر سر تنگه هرمز، تحریم‌ها و وجوه مسدود شده ایران تغییر جهت داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/142092" target="_blank">📅 19:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142090">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e64058ea.mp4?token=H62gVzwhpK7E1Wi3Z5c-vnCUSx5n4Vz90e0gHI0EtyQ164vZ7gVCZNZ3bby8S0ID3aPF1U797knorE3frdq408ujSVAaijFvIpJImCj-Va-aYTAXCs-pDRae-zqxBJVGx-7USU2lswSsjClvUmY_3wE0xZsOwhulKns8EeNoZ4J5mKFfMI-ARTk4X8kErLHfiYb89-uzdXapn-qnCph5NgMmSEtD6V-FrBBlG_WszNA3hzWRReFelgeFUptzB5unRqx4e7wI1ZjuYhtnz223qIF4Bumj0tJ_9EeSj4_OFmRzTGKQ3FUZ1Oq3o0hoCTzz3N1H_8YHJyzR6w273SBB7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e64058ea.mp4?token=H62gVzwhpK7E1Wi3Z5c-vnCUSx5n4Vz90e0gHI0EtyQ164vZ7gVCZNZ3bby8S0ID3aPF1U797knorE3frdq408ujSVAaijFvIpJImCj-Va-aYTAXCs-pDRae-zqxBJVGx-7USU2lswSsjClvUmY_3wE0xZsOwhulKns8EeNoZ4J5mKFfMI-ARTk4X8kErLHfiYb89-uzdXapn-qnCph5NgMmSEtD6V-FrBBlG_WszNA3hzWRReFelgeFUptzB5unRqx4e7wI1ZjuYhtnz223qIF4Bumj0tJ_9EeSj4_OFmRzTGKQ3FUZ1Oq3o0hoCTzz3N1H_8YHJyzR6w273SBB7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ریحانه قاسمی زاده مجری صداوسیما:
جنوب ایران، فدای جنوب لبنان، اینو یادتون باشه!!
🔴
پ.ن: ک...... تو جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/142090" target="_blank">📅 19:36 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142089">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
رییس سازمان غذا و دارو:
هزینه حمل داروهای وارداتی که پیش‌تر با کشتی 3 هزار دلار بود، به دلیل محاصره دریایی، اکنون برای حمل هوایی به 30 هزار دلار رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142089" target="_blank">📅 19:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142088">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وزارت دفاع روسیه: یک تأسیسات اوکراینی تولید قایق‌های بدون سرنشین را در غرب اودسا هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142088" target="_blank">📅 19:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142087">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
روزنامه واشنگتن‌پست در گزارشی فاش کرد کشورهای حاشیه خلیج‌فارس به دلیل بی‌اعتمادی به راهبرد جنگی دونالد ترامپ در قبال ایران، در حال بررسی درخواست برای تخلیه پایگاه‌های نظامی آمریکا از خاک خود هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142087" target="_blank">📅 19:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142086">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBv1sOntsFutrBBC4WP45aqVDlqnJJ3X0xyRidUOJY7n78XMqEGkvMFGnZc9SUlMjAJrTP5uPR6xG3xzfLbHo70jQ96V3yNS4bkbdD8SYjeinFAdjHU1xFcuH_bnb53WS_ZQTE8PrWdJPPnwc-p3OlEBn52hIu0HDZTFM28xTclb_evJ4M-01CKVfr18Y9wVPsAPe4zTLyVAkFkKQTVmQgXBiE8iVe_6LLB7S8sgHt1fon6K_krOPXQAvQxo04HydHE_17tFMYQXfWK7HBF09BIR17RT3hro0g-H9zga46wAvQ9fzMIgQ5feu3laBJgF6lt9vbqs1lOIb0NJmyHLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
السیسی، رئیس جمهور مصر همراه با وزیر امور خارجه و وزیر اطلاعات این کشور با جرد کوشنر، مشاور ارشد ترامپ و داماد او دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142086" target="_blank">📅 19:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142085">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIWg7KrpSglxvzsdPsc6ehxrzE8rcsR9UofTpaJedx99PFQTEpOOPlNZcYMC9k84DU7ieOnZZiaBvThOPJsWbiAR4r-Mxhpihjr9UoXpe17-SXQ0DMycDjr50BA8cqvarUQ9ByrH2ahqpKL4IzYq2ZX-a4ugmYH_p9DjeWc2TsmY__05JSZzfJPr7w19D3Mrs-2haVOYAMRREk3rLz4QHqV9djXJrW1o3RGulPx58mwYwgn0KWenPA2qomNLCWQFAq9m8o70CL48f3IVCXFuDIYy8JnksmRu5mNHJt0y2qyaIIuEAm07oia-8Li0LgvMF6u-SHANBtxJwhIyhnH5vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تبلیغات انتخاباتی جدید نتانیاهو، مجتبی خامنه‌ای، زهران مامدانی، رجب طیب اردوغان و نعیم قاسم را گرد هم می‌آورد: «آنها می‌خواهند نتانیاهو شکست بخورد. اجازه ندهید آنها پیروز شوند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142085" target="_blank">📅 18:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142084">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePM2hvcVlENHdZYvM1nA8TAfYxsDrj-Jnn3uCGX3uqcpRxJlNUtu8OblkLpgzM3Yl33CH4PKJugxlF000Jz3eA6MPUUO7mbQCacVsalrH9Bmv580t_k1tVtL6rP17cGROkEpGWO3oQHXCmxtZzbnFBsTstbdPnbglvdSR2Z7RrO2mADzR8n2_rbACO_ZzswefV8M0CKAfhVI933tkQbQAiqf4tVA-qOg0b5ycYQZDwyjIgBdk8SACfSGcKHCq1LQ2-OTOYHV-FEZwX1RcbEYSdO_MqVu1iVp3E3Txn_G_Ao4HtvzSVGQWxk3jF67QwwNTs0F7i0e0HXUa4ai3oDMlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کریستیانو رونالدو در گفت‌وگویی با مجله «ووگ» درباره آینده دوران حرفه‌ای خود صحبت کرد و گفت: «احتمالاً این آخرین سال فوتبالی من خواهد بود و می‌خواهم میراثی فوق‌العاده از خودم به جا بگذارم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142084" target="_blank">📅 18:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142083">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
حدود ۴۰ دقیقه پیش، توپخانه انصارالله به مناطق روستایی ناحیه مقبانه در استان تعز غربی یمن، شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142083" target="_blank">📅 18:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142082">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پور محمدی: باید با تمام هوش و توان ملی از تفاهم‌نامه دفاع و آن را اجرا کنیم و طرف مقابل را تحت فشار سیاسی بگذاریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142082" target="_blank">📅 18:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142081">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
فاکس نیوز: حملات یمنی‌ها در باب المندب ترس از ایجاد «هرمز دوم» را برانگیخته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142081" target="_blank">📅 18:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142080">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
الجزیره: ماجرای تعویض هواپیمای ترامپ بزرگ‌تر از یک تهدید امنیتی بود
🔴
الجزیره نوشته ماجرای انتقال ترامپ از هواپیمای خود در آنکارا، بخشی از یک پرونده بزرگ‌تر امنیتی بوده است.
🔴
اطلاعات مربوط به احتمال هدف قرار گرفتن هواپیمای رئیس‌جمهور آمریکا از سوی اسرائیل ارائه شده بود؛ اما دستگاه‌های اطلاعاتی آمریکا نسبت به آن تردید داشتند و ترکیه نیز نتوانست شواهدی برای تأییدش پیدا کند.
🔴
با وجود این تردیدها، سرویس مخفی آمریکا سطح حفاظت از ترامپ را به‌طور استثنایی افزایش داد و هواپیمای او را تغییر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142080" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142079">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
به زودی جرد کوشنر داماد ترامپ با حضور میانجی گرانی از مصر، قطر و ترکیه، با نمایندگان حماس در قاهره دیدار خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142079" target="_blank">📅 18:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142077">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhwFRugiaTz5BLAoHeFjZKyaZbcLNY7KBmH8aNXypI6nleL1vFOMpqlPU28mecRDy1SWOv57kJIM5aKH94bI2R33SWU9uSBJQxfQKogcv1ToIyGpz7Cge7NQazFObP66W0Ef6vgXb1A_DhFLsvRY5LNkGO5wYrPOlHMNrouxKpxASltaqa5R2iKHDV9FziBNbNXhGQDm167LXqsTWt64AlrInAjmINwlhy52I0OshX4gNE0T8i8j0I2HqXt-kmig35ZgBKD22v5gIhqbw0KUcQsRsdaQp0wRtfu199Ukr4t-C0DA4YdTvv-T-0qq7YqrCmynP_D-eE1FhMVcVO62kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4b2f47057.mp4?token=R221Y2eImMH21r6qdw_SW51Vu5oPNA9scvg6cfyLIJsoa6vNNDztqIfuZqhCHMfftaC1F-VMPHdueITDoX5S4I8N5QTEIYa8CFSheWalqjoHIjhgNfmruYTtQvlpFLSSMCKzeQcW0p2C2kdIxObTmFulgPM98dfJENONwe8mDMheYwR8smLsxv5IgiBW8KmsGh4P4TgCUv8CxhR_o5BGMra2gG31IafA7KjmzswhKyRGF78iwh5w4soAu599f7LBTofa-oVbKGzi2_UmcfiwcGQ6T1V2-vS1PwLymvErC5zZyiz-Bu74NkjunvGsPWyMNy17fcUjNPicl2EX5J4YTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4b2f47057.mp4?token=R221Y2eImMH21r6qdw_SW51Vu5oPNA9scvg6cfyLIJsoa6vNNDztqIfuZqhCHMfftaC1F-VMPHdueITDoX5S4I8N5QTEIYa8CFSheWalqjoHIjhgNfmruYTtQvlpFLSSMCKzeQcW0p2C2kdIxObTmFulgPM98dfJENONwe8mDMheYwR8smLsxv5IgiBW8KmsGh4P4TgCUv8CxhR_o5BGMra2gG31IafA7KjmzswhKyRGF78iwh5w4soAu599f7LBTofa-oVbKGzi2_UmcfiwcGQ6T1V2-vS1PwLymvErC5zZyiz-Bu74NkjunvGsPWyMNy17fcUjNPicl2EX5J4YTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که 3 فروند هواپیمای آمریکایی تانکربندر سوخت در پایگاه هوایی العديد در قطر حضور دارند.
🔴
این هواپیماها به جای اینکه در کنار هم پارک شده باشند، در طول باند فرودگاه پراکنده شده‌اند، که این موضوع نشان می‌دهد آمریکا اقداماتی احتیاطی را به دلیل ترس از یک حمله احتمالی ایران اتخاذ کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142077" target="_blank">📅 18:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142076">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfPVA-DDBuNQJMe1lxgR1UG6l2uuc11R6m7Gzj8192ajC9XS6qZtQ4HsxzRjxK2jwF8WcIKZT7_eTzTx6T5gn6cCyNdrP-NHI43gmJOaiXMS1rSX2v6B0mpeHSPNTiiIyGJxyPionemAKfSOuHNP9S50BmoV7_xm2rC9VZL1KKkPLlxm6b1IsFJRAAuiwV_9bh9WeUJ0-YA0Bo2uJiy7tdQ6pldUQs5JtWY9bJwhaI2PK_nXs4mDNNNjC7ssUg6WHLmrGjRYmmVyDoBeswJmPeHDYoxZkec2YyZFIfTO0sEES0lJ4LJ9KNo9w5FGYtf_Dd5Sao7tivkarONCzvoftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق آخرین اطلاعیه مرکز مشترک اطلاعات دریایی (JMIC)، سه کشتی در حین عبور از تنگه هرمز از زمان گزارش قبلی ۷۲ ساعت پیش مورد اصابت قرار گرفتند
🔴
دو کشتی در آب‌های سرزمینی عمان در حال خروج بودند، در حالی که کشتی سوم در مکانی نامشخص در حین ورود مورد اصابت قرار گرفت. هیچ آسیبی گزارش نشد و هر سه کشتی سفر خود را ادامه دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/142076" target="_blank">📅 18:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142075">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
هشدار یمن به عربستان: خاک سعودی در امان نخواهد ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142075" target="_blank">📅 18:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142074">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
مقام‌های آمریکایی: کاخ سفید می‌داند بدون تحقق اهداف تفاهم‌نامه از مهلت روز دوشنبه عبور خواهد کرد
🔴
نیویورک‌تایمز به نقل از مقام‌های آمریکایی گزارش داد: کاخ سفید به‌خوبی می‌داند که مهلت تعیین‌شده برای روز دوشنبه سپری خواهد شد، بدون آنکه اهداف تفاهم‌نامه، از جمله بازگشایی تنگه هرمز، محقق شده باشد.
🔴
کاخ سفید آگاه است که درگیری با ایران تا حد زیادی به یک جنگ اقتصادی تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142074" target="_blank">📅 18:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142073">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33dd257936.mp4?token=DFzzs_uL054H9DR73d1hbn-h_qLvIgDQzTsZ3S79OUcVzBeazEa-TV3vCCPhO999SKN82Kr5FzDIh4of33HDgJSoVekCClALi_GLKnhjjfmiGUvKddrLXn9UUdUBI2LCh3J-Ntzvzp-twEy9WRcggd9uvAewx6GWIkMdcrKDBurOikFOwqPGOkpeFlxdhbkRMusWT70fY9gAoudShebvCfTjpqCMnYMY5KHLARYSfsnAa_2NRKWPbY7056LkdIK1evLbW9JVnUkHAslsET48ylqPVsa6jIah_iQS-G3kINHrDerGjmn9Nhm-u1mhRhEH5dtDce5cUWTIOdAcUCjaJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33dd257936.mp4?token=DFzzs_uL054H9DR73d1hbn-h_qLvIgDQzTsZ3S79OUcVzBeazEa-TV3vCCPhO999SKN82Kr5FzDIh4of33HDgJSoVekCClALi_GLKnhjjfmiGUvKddrLXn9UUdUBI2LCh3J-Ntzvzp-twEy9WRcggd9uvAewx6GWIkMdcrKDBurOikFOwqPGOkpeFlxdhbkRMusWT70fY9gAoudShebvCfTjpqCMnYMY5KHLARYSfsnAa_2NRKWPbY7056LkdIK1evLbW9JVnUkHAslsET48ylqPVsa6jIah_iQS-G3kINHrDerGjmn9Nhm-u1mhRhEH5dtDce5cUWTIOdAcUCjaJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرهنگ ارتش قطر: از خلبانان اسیر ایرانی بازجویی شد
🔴
درحالی دولت قطر اسیر کردن خلبانان ایرانی را تکذیب می‌کند، که سرهنگ ارتش این کشور در مصاحبه با الجزیره اعلام کرد که از خلبانان ایرانی بازجویی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142073" target="_blank">📅 18:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142072">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
اکسیوس: آمریکا [پیشتر] از بارزانی خواست در اربیل میزبان مذاکرات محرمانه میان مذاکره‌کنندگان آمریکایی و ایرانی شود
🔴
ایرانی‌ها این پیشنهاد را به‌طور کامل رد نکردند، اما درباره امنیت خود نگرانی داشتند
🔴
آنها معتقد بودند اسرائیل عوامل زیادی در اقلیم کردستان عراق دارد و اسرائیلی‌ها تلاش می کنند آنها را در اربیل، یا در مسیر رفت‌وبرگشت به این شهر، ترور کنند
🔴
در نهایت، نشست اربیل هیچ‌گاه برگزار نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142072" target="_blank">📅 18:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142071">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سازمان تجارت دریایی بریتانیا:
در 72 ساعت اخیر ایران به 3 نفتکش در تنگه هرمز حمله کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142071" target="_blank">📅 18:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142070">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏
👈
فاکس نیوز: تفاهم‌نامه ۶٠ روزه بین آمریکا و ایران تا چند ساعت دیگر منقضی می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142070" target="_blank">📅 17:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142069">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a573d5f9ab.mp4?token=o90uWrAWYzJw-GKSJ-ATTedyKdx-XFrDaUCpOWsHzvqWp5IqyxWZfyd_4rlVfKRiT8NMIPYeRA60rkmNE847Id5ZPazfi6Ih0Vkhx1Lu9FJZR8MvdxtxwXW9PJC7Hx9hdSvcoKbbKN3RC3qRQ5u-Bqz786SfzUL4Mx3moP3qGsfwqaiY1JgtdLRWgVhc__VdqnI655vR_QST8OZ6C5e_gg2TN5KlfD4JP4kxnocLCAa_VvWORv9QXjyhntHrBk2MTQlbu572rSZVMICq0KibBi_O868zDYZWXEJFlexS363qRQz5cMQi9DghpF0yODcEQaCz05-A4V15jSxstiUvwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a573d5f9ab.mp4?token=o90uWrAWYzJw-GKSJ-ATTedyKdx-XFrDaUCpOWsHzvqWp5IqyxWZfyd_4rlVfKRiT8NMIPYeRA60rkmNE847Id5ZPazfi6Ih0Vkhx1Lu9FJZR8MvdxtxwXW9PJC7Hx9hdSvcoKbbKN3RC3qRQ5u-Bqz786SfzUL4Mx3moP3qGsfwqaiY1JgtdLRWgVhc__VdqnI655vR_QST8OZ6C5e_gg2TN5KlfD4JP4kxnocLCAa_VvWORv9QXjyhntHrBk2MTQlbu572rSZVMICq0KibBi_O868zDYZWXEJFlexS363qRQz5cMQi9DghpF0yODcEQaCz05-A4V15jSxstiUvwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
متأسفانه دیشب عده‌ای عوضی بر روی سنگ نوشته باستانی شهر خرم‌آباد که قدمتش به دوران ساسانیان برمی‌گردد با اسپری رنگ نوشتند اللهم عجل لولیک الفرج و این اثر تاریخی را نابود کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142069" target="_blank">📅 17:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142068">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5610fd682f.mp4?token=O6VVFpkFgyyOeSOiDnaD6GJcYQU7D-PI-tl_2AwApou8H81_HavotZOcI34gqQyHNfhtIWbeuP3aaz8LtVJm1FemNRqsfNpbmE9Q-1GF-dXTTHwKYKojobjIYTQZHdMWnBGQ0XXK3NqXhIzaUMVqujSBeumRTARYlaPANJz3-hf79Ijhfu41e87MT0NQnh5LTRY_HUnZimJAFCyoPPFuy_ERaW_hir8UvOZyIroqZqslism0hv0gLxyILQA1y_eo6TQe7gHalGzCCJSh9BLNOiUsfhEC3ddl3VkE94P5LbmtDxvAnEX2oyqHUu36_111vrQ837mgxtTZuYlGSwRpXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5610fd682f.mp4?token=O6VVFpkFgyyOeSOiDnaD6GJcYQU7D-PI-tl_2AwApou8H81_HavotZOcI34gqQyHNfhtIWbeuP3aaz8LtVJm1FemNRqsfNpbmE9Q-1GF-dXTTHwKYKojobjIYTQZHdMWnBGQ0XXK3NqXhIzaUMVqujSBeumRTARYlaPANJz3-hf79Ijhfu41e87MT0NQnh5LTRY_HUnZimJAFCyoPPFuy_ERaW_hir8UvOZyIroqZqslism0hv0gLxyILQA1y_eo6TQe7gHalGzCCJSh9BLNOiUsfhEC3ddl3VkE94P5LbmtDxvAnEX2oyqHUu36_111vrQ837mgxtTZuYlGSwRpXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
پور محمدی: باید با تمام هوش و توان ملی از تفاهم‌نامه دفاع و آن را اجرا کنیم و طرف مقابل را تحت فشار سیاسی بگذاریم
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142068" target="_blank">📅 17:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142067">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Naa-EEdTtpdoeHNh0xb72Lib5EkCVrfykYHoJZtCt7rWhAOwQ_VaZhq2NiCiMmWaZJetD5mtyR6IlsAiy5-TmmSFKcyfwoVRgSBIcbNDM8sortldHH0zTPG3DJTjxSEqDowPt7odvO1UjbfBFzP_XMFpwu1TQl7qhLurNugug5IrodWSq7OUBxIN4CtvToQri8qvaAu8tUDNFEGMKA9IMO6EGaatqboOPA9lhtkKh2hgybP39YFlOeaLd7oFpO1YIYMXE1ZFOh6mTO9vtl7ehpYiYi3seHtIydrQFJdh7-PXmWdWW5yco0UOY5glG6k3OgB2ZFUgRFNU_CCuzO85_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
قیمت آیفون ۱۷ پرومکس حافظه ۱ ترابایت؛ از ۷۰۰ میلیون تومن هم عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142067" target="_blank">📅 17:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142066">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
آکسیوس: پیام‌ها میان تهران و واشنگتن ردوبدل می‌شود؛ اما بن‌بست پابرجاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142066" target="_blank">📅 17:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142065">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏
👈
رویترز: ترامپ به دنبال محاصره زمینی ایران است اما شانس موفقیت اندک است/ هزار تحریم جدید علیه ایران در دور دوم ریاست جمهوری
‏
🔴
برخی از مقامات آمریکایی و اسرائیلی احتمال محاصره زمینی را مطرح کرده‌اند که مستلزم کمک همسایگان ایران: عراق، ترکیه، پاکستان، افغانستان، ترکمنستان، آذربایجان و ارمنستان است.
‏
🔴
محاصره زمینی می‌تواند با متوقف کردن واردات مواد غذایی، انرژی و منسوجات، فشار بر مردم ایران را افزایش دهد، اما کارشناسان می‌گویند اجرای چنین اقدامی دشوار خواهد بود و ممکن است منجر به اعتراضات یا فشار داخلی نشود.
‏
🔴
سنا هفته گذشته لایحه تحریم‌های گسترده روسیه را تصویب کرد که شامل تحریم‌های جدید ایران بود و به ترامپ اختیارات تعرفه‌ای جدیدی می‌داد که می‌توانست به طور بالقوه علیه کشورهایی که به تجارت و تهیه سلاح ایران کمک می‌کنند، استفاده کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/142065" target="_blank">📅 17:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142064">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c6b0e3619.mp4?token=iinyLwbEuW2Kl79fwPs_0khTwKdr9z5PVbR4mKCRp4D9yu_bDdddON6gSyR2Kc0CFvosWdTFoJa4fTzhwh-uuPpDn-BrCjUEbM5kuwnrdk95lo5AHzBS2X_V4ozC7cHL7iAmmiRaTSdXQ0MVggKg4a5mN9qriOY0La-YHdfWkkEXTQz2z5XDQLTgW02F6_4aZ76aKdKM8JcZec9GNy1wrn9FPjaUKU09nHP6CtBeoUuBDKJbbIZ6RpmaJNe21dXbkQctWtjRX71hpJWf-Z9ulVPyA6CYYr63mHHSuk4ThGAHt4p35PAiW_WQjt9nPvbhBYSyFeiiLYzcYvp5yKc_K6j6XJ9OThFuSTOezSeJrjF9bngIgY4qXtK-D5o6keIl-yzZkmTu3Iqye5BFzvv8830TGqGdU96QwwdDNJK1XQV0egCCmE74qJmhOrCS9pCz7hjOYFTqSG9QpTFhJKW9_iEDcas6y37j2wey-NU334Ixv-eCaf3dy7QNJceRc4soZ3uJyyv2RSDRkmQVYmCtbVZpUgMTGPuxaAgR8C5pfwkDmDxda2SgwK7IthCIwVjLgM7Npa4RVwx2D2nM29D7n2o3EgFgb2X42J0DQLiq0bwrF7QGdYhX4sF2dCNHohCE4Y2QeUwxa--twRnuh5VysdwaWSM4aLwUUjc2rrgwE2k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c6b0e3619.mp4?token=iinyLwbEuW2Kl79fwPs_0khTwKdr9z5PVbR4mKCRp4D9yu_bDdddON6gSyR2Kc0CFvosWdTFoJa4fTzhwh-uuPpDn-BrCjUEbM5kuwnrdk95lo5AHzBS2X_V4ozC7cHL7iAmmiRaTSdXQ0MVggKg4a5mN9qriOY0La-YHdfWkkEXTQz2z5XDQLTgW02F6_4aZ76aKdKM8JcZec9GNy1wrn9FPjaUKU09nHP6CtBeoUuBDKJbbIZ6RpmaJNe21dXbkQctWtjRX71hpJWf-Z9ulVPyA6CYYr63mHHSuk4ThGAHt4p35PAiW_WQjt9nPvbhBYSyFeiiLYzcYvp5yKc_K6j6XJ9OThFuSTOezSeJrjF9bngIgY4qXtK-D5o6keIl-yzZkmTu3Iqye5BFzvv8830TGqGdU96QwwdDNJK1XQV0egCCmE74qJmhOrCS9pCz7hjOYFTqSG9QpTFhJKW9_iEDcas6y37j2wey-NU334Ixv-eCaf3dy7QNJceRc4soZ3uJyyv2RSDRkmQVYmCtbVZpUgMTGPuxaAgR8C5pfwkDmDxda2SgwK7IthCIwVjLgM7Npa4RVwx2D2nM29D7n2o3EgFgb2X42J0DQLiq0bwrF7QGdYhX4sF2dCNHohCE4Y2QeUwxa--twRnuh5VysdwaWSM4aLwUUjc2rrgwE2k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک شهروند تو غزه:
ایران عامل بدبختی ما و خاورمیانه هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/142064" target="_blank">📅 17:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142063">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epp0kEpuD3d63KB-rxIQgWuamzi3jn0aXU3fCiwdyrOI294P2L1legwYJq9USvraubwP9AJxXZTuSagp4fNs1kbSd9y5s5EfI2uK3Nk9IdOZVA30cxs9mNyR9AdGICaL7xyhuy0IgmcSRsYQF1gpQ_uBzdWPlkxMXybpXcBI1NFKXJsvHnTWeD7tdZ9wqHj_8m3uUyNFSGfg_4h2Ql65SgaOU4Z4gvMwhsxNAqIKgneULnvmYQ-rPsD6molcCncEQHoW04PtOSGE_AZLLZj8xeLUdkCWQT8FWhHaxcFQHrC43bKonygOPw2r2Fo_fEeARGtq0fLOZ1nfDPD2s9YbgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری که از صبح امروز ارزشیا باهاش مجازی رو پاره کردن، ساخته هوش مصنوعی هست و فعلا غیب صغری ادامه دار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/142063" target="_blank">📅 16:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142062">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dokWlUSuefjrOb-zF8vom_IWOD2yoaVIBJjQ8op3rPMSQkt8qdb8oXIzNZCwtojPHg7bPRilZP5oPyDo2eNT4SZw4q1zB7SBFYKZdBhqQlEfSppR5Hos7Vzd2im8lySnFcqhJMLSsmMFwjCNE9-G383JJUq-qZ6-VLv-7yyi2I2V1c2PSa4EtAFH94ycLnls2cDHtPybal_vIv8otarpFOF0i50WNnCuJuWz9Lew_kTCpi-HYucOhWCR4hC0-agY-gziC5Z-zfJRNSTkWxRo0NzDvK4bvL16w4OoqLECXWGvLcvrMRu4ximmmj-3na2KiTwfZawpNR_ScRS41BUrjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طی اتفاقی عجیب شهرداری الیگودرز لرستان، کف رودخونه رو آسفالت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142062" target="_blank">📅 16:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142061">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏
👈
هشدار های حمله موشکی و پهپادی در عربستان سعودی به صدا درآمدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142061" target="_blank">📅 16:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142060">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYsK78BCXiE1TioUivriY8Q2EzD3alYX8l1qYyLsnLOaMjTBzP-rwF4SB73p5Pq5KGUMDXD_e9ag5eCiJbdoY9ubEFLSU8MOU-HfAHowTI57Fz16sXwL5wrbtOQtt8RV-jv1Xj7Zbr9LU_onntdv7nBftQ8RUhdrkenn4P1xTPMISIZlvV6R_PAj0ECVpQAhb-dK11f037dSPRGQQasBxZQWPNH0kFBBg8SfBghl5wq79JgPU_qq2Retd2YrIJGEBjKjoYnoPV0b6Kl6AH77AQc1LpDO34oR92-k67WW01RSktvKWmviJyH7BhaSfngTtmzOe-1BaO-h7v8paUxIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیت الله خاتمی:
می توانیم با پرهیز از تنش مصالح عمومی و خیر جامعه و عزت ایران و آینده آن را تأمین کنیم و فضای زندگی را به روی مردمی که در تنگنای سخت زندگی به خصوص از نظر معیشت و نومیدی از آینده بهتر بسر می برند بگشاییم و به سوی ایران آباد و سربلند برویم؛ این است معنی «صلح شرافتمندانه».
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142060" target="_blank">📅 16:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142059">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏
👈
بنزین سوپر وارداتی از ۲۸ مرداد با قیمت هر لیتر ۸۹ تومن عرضه میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/142059" target="_blank">📅 16:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142058">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47e5fdbcf.mp4?token=KLTTNiZbHw067m1BZvhDH9o4p8ixm4X2-KAOxxA_Ta8hz-fdVU4RJHaWKCYP55I4hnzCAuTBmO3UPLw2xkjTNc5NsT3bELTOl-k3gd5M5uCFHJxrcrBxUqqdoyJYeVfGcS3vfw-fBhqZEQmreRRzS4xtds-p-Wko64owa_a63limTYL8MUndnVtaeEvKd6JF8vUJn-bOwCpyUylVWADC5PZ_8iDj3IV9HjRDjVGZCEgTw9xOWRrd6YszEgrTGiVPNHsUksqvKRbrs6DEQQdDCJBi2IBZLJV0NamTEPU8JgPX7Kk7A0LR8DktZr96HJIxwjtCL4BHXRxOOcjuCzOIFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47e5fdbcf.mp4?token=KLTTNiZbHw067m1BZvhDH9o4p8ixm4X2-KAOxxA_Ta8hz-fdVU4RJHaWKCYP55I4hnzCAuTBmO3UPLw2xkjTNc5NsT3bELTOl-k3gd5M5uCFHJxrcrBxUqqdoyJYeVfGcS3vfw-fBhqZEQmreRRzS4xtds-p-Wko64owa_a63limTYL8MUndnVtaeEvKd6JF8vUJn-bOwCpyUylVWADC5PZ_8iDj3IV9HjRDjVGZCEgTw9xOWRrd6YszEgrTGiVPNHsUksqvKRbrs6DEQQdDCJBi2IBZLJV0NamTEPU8JgPX7Kk7A0LR8DktZr96HJIxwjtCL4BHXRxOOcjuCzOIFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک ویدیوی منتشر شده توسط یک ملوان، تصاویر نامناسبی از سرویس‌های بهداشتی را نشان می‌دهد که گفته می‌شود متعلق به ناو جنگی USS Abraham Lincoln است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/142058" target="_blank">📅 16:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142057">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pbvi0tlYk7daGXU-aZQTc5xc3CgWwLZzvAf0aasyIq4QUHHM4WRGXd3LE-Fn3YOLKWPgVRvhlrLxaVEAI8uOitvOv8BCEGZJqJbwN7fNWOTDonIxBQE1bkx9GLqA5pxFZREfTo4Sr7mse8G-r282Zg6yKJpynO9Qy6R4WZ0-ceSJChF7mOyDi6gPuky8T4yFTkHfa1vbs9FT5_K2UGAREhfocNRcDFxGqwAIANEjZGWEnkVEkPk9czYFPaXgJexqWu4qXoSubekS0Vn27iD7W9azqoSagqkaH20f5xu8Y6e1hU4azmrYxUqJF3zw7pXYXdSPjgwh9881hY-p6X8V4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجری تلوزیون: وقتی آقا میگه عملیات تهاجمی دیگه حرفی نباید زد و فقط باید فکر مقاومت و جنگ باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/142057" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142056">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210fa698c1.mp4?token=G2OF9mPMh-VR442-6PDnfdWfR8N-8S9bZ8baaWi7hUUZzhCTKZXwF_PsMKoIyLGuNu3lseITj15IGsXEyTP9udil4MOD_dMqes6xtI4R8jSmM6qkbhbvYDDsYRBP--E1WvhgFYxEUmfcnLEJDj3scDHB_mnd6ta-oKQGYAn9HCeMSOwcehvVLBTKUhTs2J5_RAB9pROqQRpibIiV25m1ESXZin07cmkIRvtZGGEAidhD3XN0vnme-Ys9zpegZDljoZAonVzi1xXMVRWwjic3l5dzkwNYe_Q0KTwTs0qSsRUuN-N9l8ui0ey8XU1gEikL2K5jLy3RZEQqNXDt6DDSug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210fa698c1.mp4?token=G2OF9mPMh-VR442-6PDnfdWfR8N-8S9bZ8baaWi7hUUZzhCTKZXwF_PsMKoIyLGuNu3lseITj15IGsXEyTP9udil4MOD_dMqes6xtI4R8jSmM6qkbhbvYDDsYRBP--E1WvhgFYxEUmfcnLEJDj3scDHB_mnd6ta-oKQGYAn9HCeMSOwcehvVLBTKUhTs2J5_RAB9pROqQRpibIiV25m1ESXZin07cmkIRvtZGGEAidhD3XN0vnme-Ys9zpegZDljoZAonVzi1xXMVRWwjic3l5dzkwNYe_Q0KTwTs0qSsRUuN-N9l8ui0ey8XU1gEikL2K5jLy3RZEQqNXDt6DDSug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون ویدیویی از اقلیم کردستان منتشر شده که صدای پهپاد های انتحاری شاهد به گوش می رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/142056" target="_blank">📅 16:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142055">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYw3KSM8FL5nPI4V3Hx4nJ0qXEzgbCkz0MgM1Og48Unur6_Li9_jikHqtL5uMmac5722x9qBI_OKmddcW3CDDFP2uo7y83H7b4kxmrAXS4TkHeMRlSVFWSVlKcTDQwXxn6Nkq99z-cbOpC2fZMSiVT9MOwvHBiWzxChQq-PUvtW4-7xvwbInmpU0_2_PMIPNQ_4oKZxrq7LEh54ZvIqSibo1RN8deQ_CqipgbrhuULZB83b2eZaOx9sZvu6qEfCazaRV_cNz6QF6nQewmnUuca3OBtrBnaGxz3_AkUMDHkeV5voCgGBY_zy9vgBxP17d21crRQF3VHvL-4I3_9jcRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا دالمن دانشجوی دانشگاه شریف به دلیل اعدام نمادین یک موش از دانشگاه شریف اخراج شد
🔴
هنوز مشخص نیست که آیا اعدام نمادین یک عروسک چطور جرم انگاری شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/142055" target="_blank">📅 15:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142053">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
معاون برق وزارت نیرو در پاسخ به این سوال که چرا خاموشی ها طبق زمانبندی اعمال نمی شود، گفت: خاموشی های اعلام شده در اپلیکیشن برق من احتمالی است و وقتی زمانی را می نویسند، یعنی در این زمان احتمال دارد برق برود و آماده باشید اما لزوما به این معنا نیست که در آن ساعت مشخص برق قطع می شود!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142053" target="_blank">📅 15:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142052">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
میدل ایست آی: به دلیل «وخامت شرایط»، ناو هواپیمابر جورج واشنگتن جایگزین ناو آبراهام لینکلن در خاورمیانه می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142052" target="_blank">📅 15:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142050">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ooao2tlKJKTWOsTKDeDH5DMTLfTAIryjZdcZaFqKoA86BaiJrh2zBpS-PROKiKv8gm8Hm-G1Xxe4cCfTfkBE7nIobNolOXXeEKRgjrI6Ps5-E03EiBhpHn3bYNJsEztUC-2Szu0SY8QL2_Pjt3q0dQUODK6JoCuo7Dwl5nnm5Z2_SJdftBdeTrjQRttxcQd6aGaeYvCiZwj6twZhYgeAYHhGtfKcekLgp4n_3Df7UXscPaaB7YlFp3sSR_RcQXtsvTGIxqfM28oKfZBCnuyYmxSzaPajNaHQgqB-w0gcYWIytznC7HHGXXjW5C3OHtsoLokGnm8lB5d6myA0RxxPhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QfEvPVX55Y3o3PxehcD9pggw1hMJKAGF7FoL_EJQK7DPLSGO9_INOB-8BNCL68BElUVvkjFNUKE4Q6L_muLDc7CpjEkS4sBKyeFkg_SNrQtSlcgyNxAvTMffxWmE8QxbmPoqz6-snygPTLI3BzGNG_Iczjbn2YNrlhARNPoIWIs6uiOOCGm5T-4wuQzuK9jPueLUWqW7fRhXci7uJbbDvWTvbSSTIFUilAxhEQH6q0VC9rXTwJoMknRqn6vKw5ccF05qvk09UsAmTB7GD5VfogdqF8lMhzBhmkY5y43CCnsmY2a7rISohHCx3m2xkeqe1O1-pjcvMyox_ZoRhFFP8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حالا عکسایی که این خانم به رامین فرستاده هم منتشر شده که منشوریه و گذاشتیم تو بات تا ببینید
😐
👇
⚠️
مشاهده عکس‌ها
⚠️</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/142050" target="_blank">📅 15:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142047">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
متکی ، نماینده مجلس: ملت ایران منتظر صدور حکم قصاص برای ترامپ و نتانیاهو در ۱۰ روز آینده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142047" target="_blank">📅 15:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142046">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
هم اکنون حمله پهپادی اسرائیل به چند خودرو تو خان‌یونس، جنوب غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142046" target="_blank">📅 15:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142045">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
معاون وزیر نیرو: به دلیل سنگین شدن بهای برق در بازه‌های دوماهه، در دستور کار است تا دوره صدور قبض‌های برق به یک ماه برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142045" target="_blank">📅 15:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142044">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
معاون بهداشت وزارت بهداشت:
امیدبه‌زندگی کشور به ۸۰ سال رسیده درحالی‌که سال ۱۳۵۷، ۵۵ سال بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142044" target="_blank">📅 15:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142043">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWwr8Ed-Q9ZGvUl55KO-QJcXhxYMY59e57d2kl7Z0Tyn5pwQEhWG6LzgbWLJZKiYZjRJsAlX3kjfRQClebQBTRFGD1ct_TMf1rVNOcEc7sz_GPRWnzw1khm6wjSQgzg-oa6S5N-XPsuCIs16oIxbgK-VYeZjD_sReRkMyhlylE-mhTWrq_TYKSM1SFPbsDNTd7aP6sXYjl35vnM0krjxHLFwNVGcq3kad6QBVEuobM8vZB2ssTHqpEiwqmbD_3U5jYbZHXPJNafGb00KbJLfMRslol3LkKjSBOtHbJBdDmzlZ-ZE4W90lV2zKlY3SRzodHbZZlXDvVC0MJsky5BM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوتین ۴۳ هزار سربازش را در ماه اخیر در یکی از خونین ترین ماه ها از زمان شروع جنگ از دست داد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142043" target="_blank">📅 15:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142042">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
مجلس: ۵ تا ۱۰ سال زندان برای برگزارکنندگان دوره‌ها، کلاس‌ها یا کارگاه‌های آموزشی حضوری یا مجازی که با فرهنگ ایرانی ناسازگارند؛ ۶ ماه تا ۲ سال زندان هم برای شرکت در این دوره‌ها.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142042" target="_blank">📅 14:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142040">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egvh1SajPe2AZOJewufsqdtc8V4ynpl0U3MlLASY1Z4ZOkuhohpGrv80FhJIvdVterpRt5_LPkW0B3SuXyFzjB7giaKXW5MFCUwvkLYRUZVlP7HX3zJ9MKn5Kofgg3yls1fgQhRHxUMYz4Y7sMxY6hhfCUAU8QYoMcEAQHjxO9xBs-QOCcUhA6iOwRFAI2NChrufp3dHKoPVXDyKdKt4hjNMtmzVb76ibSFoe6ZI1wf4E8K-DQxU6za3JVhg1yqbD9DYCjEp97KxCnNzP5ppyxdG1404jfpd7-sM6IP12xc9rtdhFOd-kHpRAm1CJ_noEYzduC3Rqm0lre1eVRs3hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tMUIidycaKU3RuYYA6IfslzoqVoVhaf4lZFzsfJeU36OjajODg4t40to1gjNcMdgnZSdK96eY__Fqyz-4CJAxxZqGg7cVy3GNwJvwgjf2JMtcnY74xJUCSY_wyjDELPN8O9vMVqfxaPSKhv5ZOX6gaMuZKYes7EDXRM9ANsIffxSbemjMPnznPWm7K8_oSD8hxWV5fuBbUe0Ebm070KK1BQtvAiZNxSqpxbdFdHbIuEy4W1RO7M5tNQD_Sp8HHsGHXfaYpZheUPfhkVnuwG5xWQsltZPiZLfPiLz6H_8fQTvF-gZyWyG5CWtaKPdcnKw8aC9YpfQhyYsm8zISDnKow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک نشت جدید نفت خام در تنگه هرمز رخ داده است، و علت آن هنوز مشخص نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142040" target="_blank">📅 14:42 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142039">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaPbsooSe6fGXoF5CEwct3lZA2sYopY8lBIrGd_RSLdmAuQiQMD45URPExaviri8GPODA_lX5LDjYyXfVLZzm1rleOKpRfJ_C1njN9Xu9ZBM1j53arVCjEEdQw4kNirnkeE9Jd7gqF6k-TL08raK1ww_-IqfNvw4MZt2WaO8wrh1GDjSpfoydObciQANYQorS4WpC2Hw7om3fB5YpuICmJsAKuVhlE8gobwqfqQxgWtTGb5VJMi-NORgrI8ptCzxUlzzTqGUPouqpgUVnyghIkzNReirzyq6ONZgKOQSTV7edOulqt33JmDAV0vety-XBrgTekalZe4OhWFVC-vVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی جملات و عبارات “دشمن صهیونی” و “ اشغال اسرائیل” و “ مسلمانان هیچ وقت اورشلیم را تسلیم نمی کنند” را از کتب درسی مدرسه در چارچوب برنامه سعودی ویژن ۲۰۳۰  حذف کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142039" target="_blank">📅 14:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142038">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b1f639be.mp4?token=gvEK1LIzA88kZZCpXy3xDU7ikSGXkgUkyMg_ihTJKwavaCmyLIB0sKavFisORqhxly38_1N3Nmmu5PGVk2UUkb1iToATHunc2rfkYaIEORgki4YJ1BTfKzsb2ZElLCtjC2CsxkicVggRQ_nP1dH0DFlILzQTUFr06X1bOa8L9muq--eR-uzga61mgy2I6MzHxv_Jx_n_t7BZZMgvtTjuh-6W_i0CvQavCfs-5KnwQbcaTR6q4hl76I7W5wsIU6ZC3yABH15TgZvz7x7tPLiyul83nXOGX-bC3p4LswDYPy6ve0iUUqwMKcndFZQKSNnkdsNZkKmQtKiJa57hGSIqkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b1f639be.mp4?token=gvEK1LIzA88kZZCpXy3xDU7ikSGXkgUkyMg_ihTJKwavaCmyLIB0sKavFisORqhxly38_1N3Nmmu5PGVk2UUkb1iToATHunc2rfkYaIEORgki4YJ1BTfKzsb2ZElLCtjC2CsxkicVggRQ_nP1dH0DFlILzQTUFr06X1bOa8L9muq--eR-uzga61mgy2I6MzHxv_Jx_n_t7BZZMgvtTjuh-6W_i0CvQavCfs-5KnwQbcaTR6q4hl76I7W5wsIU6ZC3yABH15TgZvz7x7tPLiyul83nXOGX-bC3p4LswDYPy6ve0iUUqwMKcndFZQKSNnkdsNZkKmQtKiJa57hGSIqkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
سوال صداوسیما از رئیس‌جمهور: نوه‌هاتون بهتون نمیگن کاری کنید که مدارس مجازی بشن؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142038" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142037">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سازمان غذا و داروی ایران اعلام کرد که در جریان جنگ، ۴۴ کارخانه داروسازی و ۷ داروخانه آسیب دیدند.
🔴
بخش داروسازی همچنین با ۵۰ کشته و مجروح در میان پرسنل خود روبرو شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142037" target="_blank">📅 14:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142036">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
قالیباف: ما در بُعد نظامی و سیاسی جنگ پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/142036" target="_blank">📅 14:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142035">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وب‌سایت اسرائیلی والا: تخمین‌ها در اسرائیل نشان می‌دهد که حزب‌الله و حماس در هماهنگی با ایران تلاش می‌کنند تا تنش‌ها را افزایش دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/142035" target="_blank">📅 14:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142034">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
درخواست عضو کمیسیون عمران مجلس: حقوق کارکنان برای نیمه دوم سال افزایش پیدا کند
🔴
افزایش حقوق پرسنل با وجود اینکه در بودجه مصوب شده بود، دولت به طور کامل عمل نکرده و ۲۰ درصد افزایش داده است.
🔴
در حوزه معیشت و کنترل بازار، اقدامات عملیاتی ضروری است و دولت باید با جدیت بیشتری وارد عمل شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/142034" target="_blank">📅 14:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142032">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
قالیباف: ما در بُعد نظامی و سیاسی جنگ پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142032" target="_blank">📅 14:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142031">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
همتی ، رئیس‌کل بانک مرکزی عازم عراق شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/142031" target="_blank">📅 13:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142030">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG3wk31sAr0d4ftSxJ7BjTsGuY6n3HjZMLxc04f0MX07CC3vdVHSypsiF90-aNw0kb74kgVPtOnf26OHS2tXoS6kJ7nUewfQSnRebfnAOe53zTTk9Hhob6As1mhwx1PkmOHTaCiEfWOgrqgqubaE9TPq3YFMlsn6RCc6zVtWhejQXKNO-ejcPzecI5YfpfB7PMPAiYQa_Ayk98Gj5ctAcMJEvX84GLyni9yyod3AqM9wdD_0QHUuU04_44S8PhelkcSqXqMzbIrtxamhHAA-WvFoJeY2RWQeeF4v249jkLqHdDf94rXSLq7tZN-jf530A-_UFTBB8hAezkfZjkMb7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ورود مهاجران غیرقانونی به اسپانیا از مراکش همچنان ادامه دارد.
🔴
تصویر مربوط به شب گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/142030" target="_blank">📅 13:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142029">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxHbb23LEUqb5ge4pmdT0YhT94-b_lQVy0XS1Qwli3I4sq1ecBtD07JfhssXcGTvWHBvajNgdG9z6_yksO1T-JN5k1kuDhkDSXftM1R_gPGD5dp6ggTueRDzzzuZmOOE5Et4Kc24JWVigtUCblXo85Z7bPqWGT_vPFRgtK1pESXHd18kw7u-tdAC3vvvk6vhIOhsCSkYyhFtK84Px5_XlVAb6r3zLfgx9v40ukEitSLAFGD-EHEL4UUUocToOwkYA2FX_qYQhc2RBBprTFaDpJQ9oVR8St9hPTOQUzKjxV3qaV63n_cEkxS1IVWmjY80iRIO9glNBxGGXks4X9dkew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای مسلح دولتی یمن: در ۲۴ ساعت گذشته، ۱۸۱ عملیات نظامی علیه حوثی ها انجام دادیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142029" target="_blank">📅 13:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142028">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزیر امنیت ملی دولت اسرائیل از نتانیاهو خواست که فوراً حملات به بیروت را آغاز کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/142028" target="_blank">📅 13:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142027">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT9ux6klV7mqagHNk6ZM6Ci9wI5OcPL7e5S42ypyytVzqaZBVh0V45twQ16l2haUjMgzEZ5ERR3mSYQdfQyzZxWxAorDQwF4iiocWmK9GxcNPYOVtmIkGLpwPpLKit60vz9FMHH5zwzOueDVFb4uIFdMV2Ja26NLUlZe8WRya9QrBcbi5MLt9up05MErHoww03kQ0KhJZFY7MbHqG7HQY24mjJspyWe_uA4IvdujugnvLKn2dLIiCsdeYAo39CKwKZ6Eg6fgaDRNwHoWlf8cJF5Ww7tknEMhOwAWFyQyh2ZV5Zyt3tV1P-nJ21EM0CUBhRJN893Lw3bI3qdcRsk2ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: با تبدیل شدن جنگ با ایران به یک نبرد اقتصادی، استراتژی جدید آمریکا یادآور استراتژی‌های قدیمی است.
🔴
استراتژی فعلی شباهت چشمگیری به تلاش‌های قبلی آمریکا دارد که سال‌ها به طول انجامید تا ایران را منزوی کند، با این امید که او را مجبور به دست کشیدن از برنامه‌های هسته‌ای‌اش کند. این سیاست نتایج متفاوتی به همراه داشت و برخی از تحلیلگران معتقدند که فشار اقتصادی شدید به تنهایی نمی‌تواند ایران را مجبور به تغییر مسیر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/142027" target="_blank">📅 13:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142026">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
اکسیوس: مقامات دولت ترامپ، مذاکره‌کنندگان ایران را دور زدند و مستقیماً با رهبری سپاه تماس گرفتند؛ کانال ارتباطی آن‌ها نچیروان بارزانی، رئیس منطقه کردستان عراق بود که اعتماد رهبران آمریکا و سپاه را توأمان داشت
🔴
بارزانی در طول جنگ ایران و عراق در ایران زندگی و در دانشگاه تهران تحصیل می‌کرد.
🔴
او به زبان فارسی مسلط است و روابط شخصی با بسیاری از اعضای ارشد ایران، از جمله اعضای ارشد سپاه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/142026" target="_blank">📅 13:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142025">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ef6cee167.mp4?token=lSBAqwJMv_jzNvc53rsH_RfeCw0rN1ceEnep6yMMU4H3bmZ6R-nciso9fBCvpk5-hEV8iWFQpuUJUGFp_IfRsz39N8oI0S6eClw4kkYvq__nPSWxzCWeRxhCSMncWOML-1KVMBI3HU6CmnBizCGZkVOMe4IoPT7jqaL4AVPlB_jQnsNlX236TCwEBg82XTdOpWMIeQfmncsAnkjcE3X2VlglBZJqjTfzH1_fw45sZ7f9hoTaXWtcam-L53jB6iwaDCfX98ys4hrTHsx3elWiTF4ds3-_9wRxWKOfM1Dpk5EmWxbdzTFCc_OWbR9K7mP6yXv6HUbKEPkOk_JXV6BFxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ef6cee167.mp4?token=lSBAqwJMv_jzNvc53rsH_RfeCw0rN1ceEnep6yMMU4H3bmZ6R-nciso9fBCvpk5-hEV8iWFQpuUJUGFp_IfRsz39N8oI0S6eClw4kkYvq__nPSWxzCWeRxhCSMncWOML-1KVMBI3HU6CmnBizCGZkVOMe4IoPT7jqaL4AVPlB_jQnsNlX236TCwEBg82XTdOpWMIeQfmncsAnkjcE3X2VlglBZJqjTfzH1_fw45sZ7f9hoTaXWtcam-L53jB6iwaDCfX98ys4hrTHsx3elWiTF4ds3-_9wRxWKOfM1Dpk5EmWxbdzTFCc_OWbR9K7mP6yXv6HUbKEPkOk_JXV6BFxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در اوگاندا، گردشگران سفیدپوست ثروتمند به ساکنان محلی پول می‌دهند تا آن‌ها را مثل دوران استعمار روی یک تخت آهنی حمل کنند و به گردش در جنگل ببرند.
🔴
این یکی از تفریحات پر طرفدار در جنگل های این کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/142025" target="_blank">📅 13:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142024">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWp9aSaXE9UPSk8Vn-IzG2r-3hOYxb8i5ZTKTvniKkL5f7V1Ve7fEJVv4jprNzicVqS_vAbXo8Q0j9KqLkAtp5YI0dQeDzwU2in5WyMCjh9o4-GRpyaiAue4RTOmSMaiEiqn6CIwxNCQmi9D53uWIK_LE67ivaYkVHIFMliBz_pECqaaKTS87QeVOHzHUSurrofaIRchBKOQqA4vJAT2PF2USsuORgfYDGy2fMnc0vs-sOLMBUv0FSYpsI3ItWg30bz_0mBvp8I_9bndWT-YE3p8GXf5MeDYm5pi3I9dModsw90C_TQEf2Ly5Y_rOUuvteMGgwu63bdZ1W6CnV3rgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حالا که صحبت از ایران و نقشه ایرانه
ببینید نقشه ایران ( سرزمین پارس ) رو در زمان امپراتوری هخامنشی و پادشاهی خشایارشاه، نقطه اوج قدرت و امپراتوری ایران در تاریخ
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/142024" target="_blank">📅 13:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142023">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa-SFRkvsFDY_xK-CI9bNKaNh4HVh6T8jVWGekD8dxzDxjg5NLWZCwgFjjGu-dEKEYxyb9iSAmM5yu-cAK4yR5i4oiiIH3oT8e1BR6herq4o3eWQVHNKpk9FjZk8ZiZl-KkbUzZ3k2Z9ySzIqoOahQ9Qndz9RQQ2k-X5Pt0VL5xgsqolmBC9QbA7R2Y63Dssy-hrEhEvwndpUatyLmC2BRwAffimDf2Q5NOLdwWhLXTi8BPmu4onk56YycrQqBnehJesJ-Jp73zL5gawxc6mCPEGj_vLzkHeffW7DpdtJW55W1WhwhGdVkdKWFW00MOkqJuK7rPGM-D4J2_bi-n3IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین شریعتمداری: وظیفه جمهوری اسلامی در قبال مردم، فقط حجاب هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/142023" target="_blank">📅 13:00 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
