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
<img src="https://cdn4.telesco.pe/file/BCbA99rckAyKz2GUIxK4n71XL3x2mQYFDupAxHeCekMjFIzYziLS5kITo4WSQrRd0aSKY_Y3kr4i-InYzeFCNN-x_mer4qJ1d4_UpcGREWErMNA5-fvghmWC2oKvX0eB0VCeaG7SckV7N_tVi67TvDKaxfXxORHQwpy6E0WxHGdAYSbguh7NKXoLzt5gSXRQHJzHsX0MWAZ-__vEc0Q1JKOlJ9Lg5fBy8NtJnh8KLA8ZltSWHp1NCeWcZ_osCe_dVe4roiB6xSngN7piXZqAXiuU6rs__ILQvjJ8ShjJhcADycnDKp7A2b7pxmy5Ryy63B1jUTXG25h8cq285G7v7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 349K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 00:11:03</div>
<hr>

<div class="tg-post" id="msg-16962">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8816f1f59b.mp4?token=YdUmnZlsXFusG0dgEpfwdFOK9YBtwW1IZODF2BD6FqROcOMCLTWCf93WpKG0a2JZxgmWIDNlMJrA9mBkOKqQgr9SP__4dXyckD2XfdClOm2PSZtPp8HHxnFU4nJGEfmzdiva5gwl-fJ5CbCYHDozvQDeZ5tCyRGL4Ayh5GabX-hPO6ZYBPfSho767lQ_HN8PLX5q0_u7_2U74-6iEUKTwdYjmcqEQGpOxJyWuSGQbn6LVpjeVsBuQr8y6JspUB8F5VqI-SoUfhAq1_UQVIlRhQgSFRYB2Wumj4khTMa_UvP8GIohN-S5ymoLSbmav8FDly5hSXzAYHmIj6lV1jXVrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8816f1f59b.mp4?token=YdUmnZlsXFusG0dgEpfwdFOK9YBtwW1IZODF2BD6FqROcOMCLTWCf93WpKG0a2JZxgmWIDNlMJrA9mBkOKqQgr9SP__4dXyckD2XfdClOm2PSZtPp8HHxnFU4nJGEfmzdiva5gwl-fJ5CbCYHDozvQDeZ5tCyRGL4Ayh5GabX-hPO6ZYBPfSho767lQ_HN8PLX5q0_u7_2U74-6iEUKTwdYjmcqEQGpOxJyWuSGQbn6LVpjeVsBuQr8y6JspUB8F5VqI-SoUfhAq1_UQVIlRhQgSFRYB2Wumj4khTMa_UvP8GIohN-S5ymoLSbmav8FDly5hSXzAYHmIj6lV1jXVrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چابهار
@withyashar</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/withyashar/16962" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16961">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8914bb721.mp4?token=PNQ1yeiNXhnsHSxgRyIcbkQJapOy16p7l_7VBG478W7yHvthqh9bgRPU2ZeO3c4Mq76s8JORZBEHI5d2h-2JtXIXFSGh-6qUBBa26vz_cUxwpDylGbFcNGI3uxx6BYHeQFrvoaDVhKPhcvEuOy3R5ztlF9MC1ABkD5gwCs5S3lbkFGx5KBSlnoHN5EsCTGXSSW-o1SiQThZEDJovYOvYQejsoxiaVk_YoCf6iqt_lQtqzvYA4xnGspOs_qxLXewP03dV_xgCvA2KZRMNuBYBC0846ZIndEK0VsSF8L6TpuI7gemP_pSqFBL0N0nhYWC8oUcoQe1BPhtOXVb3BESzrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8914bb721.mp4?token=PNQ1yeiNXhnsHSxgRyIcbkQJapOy16p7l_7VBG478W7yHvthqh9bgRPU2ZeO3c4Mq76s8JORZBEHI5d2h-2JtXIXFSGh-6qUBBa26vz_cUxwpDylGbFcNGI3uxx6BYHeQFrvoaDVhKPhcvEuOy3R5ztlF9MC1ABkD5gwCs5S3lbkFGx5KBSlnoHN5EsCTGXSSW-o1SiQThZEDJovYOvYQejsoxiaVk_YoCf6iqt_lQtqzvYA4xnGspOs_qxLXewP03dV_xgCvA2KZRMNuBYBC0846ZIndEK0VsSF8L6TpuI7gemP_pSqFBL0N0nhYWC8oUcoQe1BPhtOXVb3BESzrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بوشهر الان
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/withyashar/16961" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16960">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hay8NV4TVVipOpvkc0219E8FBk37f8GuDhdE3OjgGoq1Gm1BBIS-yltDOpTuXFqXX4-RdtPSUFG6RwUsIJnocvpIb_oXKpxZ79XOKXyKwSdt75YopguA8wOU-dX91NPT2VABlgB3R6-XefxF3dS-m08MJN5cjfrNJUwXrNw3OfnoywlVj0MyapZEv6LVbiKt4zD-nR_ZkCiXpG7MHHPRS_4OQBgvLBvG7fYBwPyKXPN48pSaCcxCm7w1n1XdtNETng0MNkbQBf2yLZ4bqtmp6PyVTRbCQuOTpz31USCguUBR5gmrpnUfzzatylF5frVLEGFsRliajL7HvvWVZMdrZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی سازی سمت اسکله باهنر بندرعباس رو دارن میزنن
@withyashar</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/withyashar/16960" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16959">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انفجارهایی در نزدیکی نیروگاه هسته‌ای بوشهر @withyashar</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/withyashar/16959" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16958">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فرودگاه بندر چابهار مورد هدف قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/withyashar/16958" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16957">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8befa662e.mp4?token=YZ57Rh6Kco0rHmyaBMHh2Mm6RN5cPQL-KohaybN6Zgoe1twOJK6-fdNNwtu71oQpHZw1ySQ8IDKaS_rdYZ26DhGvkmqw7l3o0uAJyhzkYrcYflqR0tLntMnXsja_74DMVmEimyNTk0hpKXxOQ5q8OB_Sn1xWthEzy_t14bwe_IFPx7v9agBJJ0WZtMS9JM1xEH_cAlz8CemdIn01eWoOmSinNUx2gBy8rJzoYoMuvsLklh8Js9g8uO82ysaxZfDvdmDbDOg9bam_pDuX3Ntl6eOFhZifVBFG4z2461AOQEJCP2SQIm1Lq7HRjjBA8S7XCBoOXwSnLMmkz1ZhwHsy2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8befa662e.mp4?token=YZ57Rh6Kco0rHmyaBMHh2Mm6RN5cPQL-KohaybN6Zgoe1twOJK6-fdNNwtu71oQpHZw1ySQ8IDKaS_rdYZ26DhGvkmqw7l3o0uAJyhzkYrcYflqR0tLntMnXsja_74DMVmEimyNTk0hpKXxOQ5q8OB_Sn1xWthEzy_t14bwe_IFPx7v9agBJJ0WZtMS9JM1xEH_cAlz8CemdIn01eWoOmSinNUx2gBy8rJzoYoMuvsLklh8Js9g8uO82ysaxZfDvdmDbDOg9bam_pDuX3Ntl6eOFhZifVBFG4z2461AOQEJCP2SQIm1Lq7HRjjBA8S7XCBoOXwSnLMmkz1ZhwHsy2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بوشهر الان
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/withyashar/16957" target="_blank">📅 00:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16956">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گزارش انفجار در قشم
@withyashar</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/16956" target="_blank">📅 00:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16955">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">صدای ‌جنگنده در‌آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/16955" target="_blank">📅 00:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16954">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">۶ انفجار سیریک
@withyashar</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/16954" target="_blank">📅 00:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16953">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجارهایی در نزدیکی نیروگاه هسته‌ای بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/16953" target="_blank">📅 00:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16952">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گزارش
بیش از ۲۰ انفجار در چابهار و امتداد ساحل
@withyashar</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/16952" target="_blank">📅 23:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16951">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9xyqqxGkrzjfDdvNX2QlJPdIk3UKyH1K8rQ_OeODT_9wVs4DQIdzIHXpCnebsLo-DV_ifJaQRMQbIKrwjHBRc_EUG5uw4QxSvSS9NqX6C39QYbTpnjym3O6pzDhGpyBkVY8Yt_7r2dzKquxIv356WMeGAGky-UL48cjTkkhpzz24EeiPtsmPpBK4xc3LW7x-HRj2ZMKVV-l-8RRxU9txjn6k9vEopXoBq7lCBhqTaaFIly24SBEgAIhvQdSK_EvbJuP9KHtRauEJyq7arNAP8vTwbX8tdOi7oVHqjyk8J_44L1iaLjAzuvf20Ilr6kSqL_IMc1oIGoecq-5ZRFGVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر عباس الان
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/16951" target="_blank">📅 23:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16950">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vizTIZdaFhy_kUYkaje0ONkw4akiyG5AxlqMzMk02R792PRgzWD5ddcamRd3QEjdLxRwW5lwuDmnIqQ8I_MZsGEnimqB8eyVfT4Ugbmox__AxSGFXLTGHE2Bnf3iQmuRRYKNB5MCSLjVZm766iIyb3YO9uWB4SSHpeiejAHQMXhkBJIV1Q6ZoktBrlPyxAX6M57mGPKA5wFxlJELXP7qOKDI90et_W7W7547y6ZMo6d0d6GqGx_SfTQciXL5ZUGx9u3MwsZJ1jLULHHffXm0sihwrzNI4nHO1Y3SxFcxAwTOWZ27R8qiaeAx64P8AIrHyox4HZZ9OPqgbQOiIoWiFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‎سنتکام: به دستور فرمانده کل نیروهای مسلح، نیروهای فرماندهی مرکزی ایالات متحده، حملات بیشتری را علیه ایران آغاز کرده‌اند تا توانایی این کشور در تهدید آزادی کشتیرانی در تنگه هرمز را بیشتر تضعیف کنند.
ایالات متحده، ایران را مسئول اقدامات تجاوزکارانه اخیر و غیرموجه علیه کشتی‌های تجاری و خدمه غیرنظامی که به صورت آزادانه در یک آبراه بین‌المللی حیاتی تردد می‌کنند، می‌داند.
@withyashar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/16950" target="_blank">📅 23:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16949">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دو انفجار الان بوشهر
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/16949" target="_blank">📅 23:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16948">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گزارش انفجار‌ از‌ بوشهر و خارک
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/withyashar/16948" target="_blank">📅 23:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16947">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeYwuCfC_6RuJIE0QXgfwFWXRnoJqwWCCL-aPUpNbOnWerQwsq2jtZ5bhi3-cTrTzF77WNNnLNdDHh90bEyg9-33svIByejn30GaTrOlZs_xHjQsrY8GspFgWZIrQvBmNVRsHujHAOI9B-Qi2T6EbPUpeZ_dVPyJrK07hnCEKfXrK3v6bYaRC6_HWitgFDX4hmqD1UdjVvLC6rFZibmBUt-PPXk456t-N_wu3HdsyB6qVkNcxIqVDBH9PrvO78jQTzi64T5YNbxz5cnSOCtNjlL-eafofi_pDO6xgU1-3xeSEMN9TgyBISmMGXCEwFify-DjEfjJo6uKgCTb1N2vog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله چابهار الان
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/16947" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16946">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارش پالایشگاه لاوان رو زدن
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/16946" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16945">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بندر عباس دوباره زددددد
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/16945" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16944">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1750d26e0b.mp4?token=FtRb0NBp3HlmTWMSLJJVEE6FdA024GHSelYvgVFX6a2goizA7cITKujS407ibn-u6tgMGVnk-g1SfRbpbrm2_cfunuV7sLgOQUZn8EKHRiue6wtIZstcNe98nueQvECYitqOCj1VWT8PCivj2NCkx2YfX4gtnXolfU74oIZ9Xw2D30hsj_HO3br4-0osxnRCyDIY8e5Kkl0j9_f7kwyN-8zzjNpTuv3gKiu-MLQzsnWIzuQkGQWWRgbtVCaRQfPcERrykXZDxauF2R2IAAsMMhdcaBU2Dh7zSAjyWz6N6ENSdMIuJ3b5AS-8LxDRD9eK2vZA600-OUwptgMhUFWqCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1750d26e0b.mp4?token=FtRb0NBp3HlmTWMSLJJVEE6FdA024GHSelYvgVFX6a2goizA7cITKujS407ibn-u6tgMGVnk-g1SfRbpbrm2_cfunuV7sLgOQUZn8EKHRiue6wtIZstcNe98nueQvECYitqOCj1VWT8PCivj2NCkx2YfX4gtnXolfU74oIZ9Xw2D30hsj_HO3br4-0osxnRCyDIY8e5Kkl0j9_f7kwyN-8zzjNpTuv3gKiu-MLQzsnWIzuQkGQWWRgbtVCaRQfPcERrykXZDxauF2R2IAAsMMhdcaBU2Dh7zSAjyWz6N6ENSdMIuJ3b5AS-8LxDRD9eK2vZA600-OUwptgMhUFWqCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین فیلم چابهار گویا پایگاه امام علی بوده
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/16944" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16943">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارش انفجار‌‌ پادگان ارتش در‌کنارک
@withyashar</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/16943" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16942">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خبرگزاری آکسیوس : حملات امشب ارتش آمریکا بسیار سنگینتر خواهد بود @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/16942" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16941">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش انفجار لا‌وان
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/16941" target="_blank">📅 23:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16940">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">۳ انفجار دیگه چابهار / اسکله چابهار
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/16940" target="_blank">📅 23:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16939">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انفجار بندر کنارک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/16939" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16938">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/16938" target="_blank">📅 23:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16937">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">۳ انفجار چابهار
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/16937" target="_blank">📅 23:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16936">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">چابهار رو زددددد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/16936" target="_blank">📅 23:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16935">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خبرگزاری آکسیوس : حملات امشب ارتش آمریکا بسیار سنگینتر خواهد بود
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/16935" target="_blank">📅 23:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16934">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">منابع محلی از مقابله پدافند هوایی با یک پهپاد متخاصم در آسمان جنوب کشور خبر می‌دهند
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/16934" target="_blank">📅 23:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16933">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یک پایگاه دریایی سپاه پاسداران در سیریک مورد حمله قرار گرفت
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/16933" target="_blank">📅 23:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16932">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">صدای جنگنده ها  در نوار ساحلی خلیج فارس به سمت ایران شنیده میشود</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/16932" target="_blank">📅 23:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16931">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارشات از تحرکات موشکی سپاه در مناطقی از کشور</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/16931" target="_blank">📅 23:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16930">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارش انفجار‌ سیریک
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/16930" target="_blank">📅 23:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16929">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پدافند درگیر شددددد</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/16929" target="_blank">📅 23:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16928">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جنگ بندر‌عباس با آمریکا شروع شد
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@wirhyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/16928" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16927">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یه دونه دیگه بندرررر عباسسسس دومیش‌
🚨
🚨
🚨
🚨
💥
💥
💥
💥
@withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/16927" target="_blank">📅 23:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16926">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گزارش انفجار‌ بندرعباس
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/16926" target="_blank">📅 23:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16925">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">زددددددد</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/16925" target="_blank">📅 23:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16924">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وال استریت ژورنال: دولت ترامپ و عراق به توافقی برای تشدید کنترل‌های مالی با هدف جلوگیری از رسیدن دلار آمریکا به ایران و شبه‌نظامیان تحت حمایت تهران دست یافته‌اند.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/16924" target="_blank">📅 23:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16923">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مقامات ارشد آمریکایی به CNN: حملات آمریکا به ایران ممکن است در ساعات آینده آغاز شود، تیم امنیت ملی ترامپ در حال تصمیم گیری در مورد دامنه و گستردگی حملات آتی می‌باشند
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16923" target="_blank">📅 22:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16922">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رویترز: قیمت قراردادهای آتی نفت برنت با افزایش 5.2 درصدی، در پایان معاملات به 78.02 دلار به ازای هر بشکه رسید.
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/16922" target="_blank">📅 22:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16921">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ونس معاون رئیس‌جمهور آمریکا: عملیات نظامی آمریکا ادامه خواهد داشت، مگر اینکه ايران از شلیک به کشتی‌ها دست بردارد.
@withyashat</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/16921" target="_blank">📅 22:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16920">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اگه با روال همیشگی پیش بریم مهمونی باید دقیقا حدود ۳ ساعت دیگه شروع بشه بچه ها دارن میان کم کم و حضور ۲ هواپیما p8 poseidon  هم دلبری میکنه @withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16920" target="_blank">📅 22:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16919">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/16919" target="_blank">📅 22:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16918">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Obj6VCVNldX04o62HXA_X01T2vWN4XZzq1chFah7dc0hbZhPFZ8w9J4Oc6onExeB3The-KgZI9QoCvQYVS46Qmpot_bBF2i-2ebFSqWZxbeufmOOQYAzBvtTQ6I_FkOTMaTusndxZz4QrR2iPVh1SDLsZPlcF6kp7wJ0ASOLs9JI15ZB8LhcPJr33eQiSykLQZb2YPRj5TXZQGdXYhzVHtLdw75AsEfH6O7fSa7tlqJK9G9SlhW5amz2EBloHLkC6qsVE1RsnDjEByHU1_wQcK9A2PojqceH7Q4Wc9GBAbQRvFpWKSJs0qEu-oySdLQa86UZueo6ILGcjJq8xauxGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صیادان امید عربی و مرتضی هرمزی که در پی حمله ارتش آمریکا به اسکله ماهیگیری بندرعباس به شهادت رسیدند
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16918" target="_blank">📅 22:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16917">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">درگیری در منطقه‌ی سردست و کشته شدن یک پاسدار
یوسف محمدی ازپاسداران تیپ ۳۶انصارالمهدی زنجان دردرگیری با مهاجم‌ها درمنطقه سردشت کشته شد رسید.
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/16917" target="_blank">📅 22:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16916">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وزیر خارجه آمریکا: رئیس‌جمهور ترامپ امروز به کنگره اطلاع داد که دولت او قصد دارد طبقه‌بندی سوريه را به عنوان کشوری حامی تروریسم لغو کند.
@withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/16916" target="_blank">📅 22:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16915">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b9720f86d.mp4?token=KabeapQYQFm3tPXLk8UXhKJlX_h-cfmrT9xMNhjW1_GVrqAOWhVzb6qS7I3ncLBhg7aJh0OuP3INFxK78R2_RpvhME-aBWtME39fjHRigFoXqwbDRLjdDmt0gectTwkZDMhWl8lFlK24ueP_TutBYbLyph8D8Of0b88fFY0h1dFl4hL6EUuz31YnRDpVU4F-v-DVmME6X1xsBVvbG70rNyCtgTCRLnUKuUMIayzBEaGguyIq7PH8T-vbcUAvwMsiSBmeRuZWADKH7HMm1BxB4maQ321YDvLYaC_cjil844rngh4Glf7fQ0gE_4L-I8fr4LdO0jtyUYa1ncBLKs6gGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b9720f86d.mp4?token=KabeapQYQFm3tPXLk8UXhKJlX_h-cfmrT9xMNhjW1_GVrqAOWhVzb6qS7I3ncLBhg7aJh0OuP3INFxK78R2_RpvhME-aBWtME39fjHRigFoXqwbDRLjdDmt0gectTwkZDMhWl8lFlK24ueP_TutBYbLyph8D8Of0b88fFY0h1dFl4hL6EUuz31YnRDpVU4F-v-DVmME6X1xsBVvbG70rNyCtgTCRLnUKuUMIayzBEaGguyIq7PH8T-vbcUAvwMsiSBmeRuZWADKH7HMm1BxB4maQ321YDvLYaC_cjil844rngh4Glf7fQ0gE_4L-I8fr4LdO0jtyUYa1ncBLKs6gGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، پس از پایان اجلاس ناتو، ترکیه را ترک کرد.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16915" target="_blank">📅 21:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16914">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cN5ggsCncPTkn_NsbShe8ZjgqtfioNtoMgTR2rAOO022skB4y0IHarpq9NpR3AkJiHl6IZ7scWxq3JfvhXVVY3Qd76BZ5nN9XpJr4OZoTAUtkQt7MNhU3vAndYtD3bEo3zt5jEKfwSlOK1cfST0XxV5WLKC8OfKLh-aCC6HG9l0wCMf4DqvYBLGQ3yVAT9IjrX5mEg4J5GUEo7z41osTHG6ZrBIqFDNqnlhpYHwYokW5TkadBwHuBWfzgLyoLZ61uiwI_j_cVQD3gXCz96RO-x1SSU38xfNuIFB7GrjE0XoKkQK6RVN-Gl8BjAjscQ0L7hQqMFv3_KoIczzHIqq7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه با روال همیشگی پیش بریم مهمونی باید دقیقا حدود ۳ ساعت دیگه شروع بشه
بچه ها دارن میان کم کم و حضور ۲ هواپیما p8 poseidon  هم دلبری میکنه
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16914" target="_blank">📅 21:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16913">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اسرائیل: اسرائیل در حالت آماده‌باش کامل قرار دارد و رئیس ستاد مشترک ارتش، جلساتی را با حضور مقامات ارشد نظامی برگزار کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16913" target="_blank">📅 21:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16912">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کان نیوز
:
بازگشت سوخت رسان های آمریکایی به منطقه آغاز شده است
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16912" target="_blank">📅 20:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16911">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">@withyashar
فرهنگ سازی</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16911" target="_blank">📅 20:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16910">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c89ffde203.mp4?token=rwmc5MHD2yoF3fw-egIWprV_ODUNFCZwaDbcdZbs6Z9Rw0SwfG-Iaqc3UstWC-YtB0H9iriTdRy6ajOhCoxQAGynABDDWl0ll0r3ayxULF66SvsPDvlOOu7eFwaxdgYSOFQ07UTE5JKtjL2tUvZrRs8tOP3YaSztXGNFv8G9_xgx_M8oimBCJMo9J7XoZxQxEViszOEYhqekGkqWNJV0kzNYIOFqV9mdUtvWcwnEG38UNw_9DCbswOkU86m-_XQtDf08JWiI0EniJ7KKUD_C11QqJmLA9kjq2IeMlp9BKvAiYWKpBY9s6OQPbCW9M5Tei-MxOgaisw9DKBaL6RL-zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c89ffde203.mp4?token=rwmc5MHD2yoF3fw-egIWprV_ODUNFCZwaDbcdZbs6Z9Rw0SwfG-Iaqc3UstWC-YtB0H9iriTdRy6ajOhCoxQAGynABDDWl0ll0r3ayxULF66SvsPDvlOOu7eFwaxdgYSOFQ07UTE5JKtjL2tUvZrRs8tOP3YaSztXGNFv8G9_xgx_M8oimBCJMo9J7XoZxQxEViszOEYhqekGkqWNJV0kzNYIOFqV9mdUtvWcwnEG38UNw_9DCbswOkU86m-_XQtDf08JWiI0EniJ7KKUD_C11QqJmLA9kjq2IeMlp9BKvAiYWKpBY9s6OQPbCW9M5Tei-MxOgaisw9DKBaL6RL-zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ خطاب به محمدباقر قالیباف درباره اورانیوم : محمد چی چی محمد چی‌چی آنجا با بیل‌هاست.
بیل‌ها شما را به آنجا نمی‌رسانند. بزرگترین ماشین‌آلات جهان شما را به آنجا نمی‌رسانند
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16910" target="_blank">📅 20:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16909">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe30e74b8.mp4?token=riOf4BR5Bovc2IHLJFT4moEwew0ZjX7B1nLEme0BA_HQWFwa1Xyqs7GSBx03dRVZh7uTGbc1WdPLPbki0XwibsHAvLWtnaoSHsawH7Rqejp9BZQImS7B7KtP4CXCBCgBIq0A7SDvXI8ChL93NtjnbA7cieXou5OIkXtYypreVcncCOqs6iogl2IdLanojDX0fwg-goSXdChL6z18MNpSaK6_82Tk5sli0uic9lMi6xwLTe2CSzoINhYj17WRP-1w6lpof_BaauI4JX7wTbeY-264k05cl3DgIGQ38PiMbreCvG5K6WojnhTP2Ozh8yfemW9dE3QfCqdmbw6ZegwkhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe30e74b8.mp4?token=riOf4BR5Bovc2IHLJFT4moEwew0ZjX7B1nLEme0BA_HQWFwa1Xyqs7GSBx03dRVZh7uTGbc1WdPLPbki0XwibsHAvLWtnaoSHsawH7Rqejp9BZQImS7B7KtP4CXCBCgBIq0A7SDvXI8ChL93NtjnbA7cieXou5OIkXtYypreVcncCOqs6iogl2IdLanojDX0fwg-goSXdChL6z18MNpSaK6_82Tk5sli0uic9lMi6xwLTe2CSzoINhYj17WRP-1w6lpof_BaauI4JX7wTbeY-264k05cl3DgIGQ38PiMbreCvG5K6WojnhTP2Ozh8yfemW9dE3QfCqdmbw6ZegwkhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد جمهوری اسلامی : هر اتفاقی قرار است بیفتد، بسیار سریع خواهد افتاد. ما به دنبال بلندمدت نیستیم.
@withyashar
ترامپ : من مطمئن نیستم که بخواهم با آنها معامله‌ای انجام دهم.
فقط بیایید کار را به پایان برسانیم</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16909" target="_blank">📅 20:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16908">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ: من شماره یک لیست ترورِ جمهوری اسلامی هستم.
واقعاً برام مهم نیست، دارم کارم رو انجام میدم
فکر نمی‌کنم جنگ ایران دوباره شروع شود
هر اتفاقی قرار است بیفتد، بسیار سریع خواهد افتاد. ما به دنبال بلندمدت نیستیم
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16908" target="_blank">📅 20:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16907">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/166026afde.mp4?token=Lyjy27L-VR_AIwQf54Au_Qddhi6fZJaLUqAjTO2ZhLn-WxhlTlDLgR39KPp_EsI64KWO95iL-nWYVKJbWXVKWA0c2EazwTwPEpmKsnSTBQFP4vWFrP1i85e_1MvD9_MPbh_4B7h_YI6MTpzWw1bRGT4XHhWitZdUnU6ypKBCTkqu0BEkjHtcILCOpTrGjnzSfP7L8QsgBmxVda7QHQ6U0XMoAwlDZqoX3sZ9185l6Uh6C8IEAI34V74609uJZlrPT3P6SoSh9NzQJa18wtrDicfGZur9ct_UJCAYWqzGPW62rey__MAeJPdq81vLG_iRdGT52_aM8okoiNkLGci82klhYN1X3rVPO2oSwWniu0dy6IGqYQK-UqY5izriLi322YJXI0w8tfIzASYo4iBEnpJRirNmW-OfPAiFCa6f4DiYyE-bCq_jI_rEzfdsAE-iSEY8vgpQc0ikFDZ5knv02cN99-4lXLZvtmX5ri1NA9NkQMNr-tI1wpacjiGKyrqt2rGmBuv0iPm75znLyBr6B98MYajgBt6anOcBtDj8DvgULyRCYDg04nOd_9hVnDfKXy7NxgahtUzLVhDVXTGnKQQ6MQ2WatC2qzzhsHFkqh0hCnDP128cAmE7qfVXmO858Y_qFDZZ54kjMBQCLYExoFeqeo1OlosP8bVg93GptNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/166026afde.mp4?token=Lyjy27L-VR_AIwQf54Au_Qddhi6fZJaLUqAjTO2ZhLn-WxhlTlDLgR39KPp_EsI64KWO95iL-nWYVKJbWXVKWA0c2EazwTwPEpmKsnSTBQFP4vWFrP1i85e_1MvD9_MPbh_4B7h_YI6MTpzWw1bRGT4XHhWitZdUnU6ypKBCTkqu0BEkjHtcILCOpTrGjnzSfP7L8QsgBmxVda7QHQ6U0XMoAwlDZqoX3sZ9185l6Uh6C8IEAI34V74609uJZlrPT3P6SoSh9NzQJa18wtrDicfGZur9ct_UJCAYWqzGPW62rey__MAeJPdq81vLG_iRdGT52_aM8okoiNkLGci82klhYN1X3rVPO2oSwWniu0dy6IGqYQK-UqY5izriLi322YJXI0w8tfIzASYo4iBEnpJRirNmW-OfPAiFCa6f4DiYyE-bCq_jI_rEzfdsAE-iSEY8vgpQc0ikFDZ5knv02cN99-4lXLZvtmX5ri1NA9NkQMNr-tI1wpacjiGKyrqt2rGmBuv0iPm75znLyBr6B98MYajgBt6anOcBtDj8DvgULyRCYDg04nOd_9hVnDfKXy7NxgahtUzLVhDVXTGnKQQ6MQ2WatC2qzzhsHFkqh0hCnDP128cAmE7qfVXmO858Y_qFDZZ54kjMBQCLYExoFeqeo1OlosP8bVg93GptNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام با انتشار این ویدیو نوشت: امروز، بیش از ۲۰ کشتی جنگی نیروی دریایی ایالات متحده در سراسر آب‌های خاورمیانه گشت‌زنی می‌کنند در حالی که نیروهای سنت‌کام به ترویج امنیت و ثبات منطقه‌ای ادامه می‌دهند.
ماه گذشته، کشتی‌های جنگی دریایی و هواپیماهای ایالات متحده در نزدیکی هم از دریای عرب عبور کردند و قدرت نظامی و آتش بی‌نظیر آمریکایی را به نمایش گذاشتند
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16907" target="_blank">📅 20:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16906">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638d05d744.mp4?token=EcjUzXXXOSvt3cudTTMp4pvkBVj5e1y3ejH49taK7bUDCF9bfFRr8aBhcHKWQsTzL0ttp0h_wIm7neqdtCt11EG3CPpYGxskXV77lMrG6TXFV_70ywhfzrUBP7rGb3SDEac2TndH-1pikzn09OhCG4ddlAuP-tFBzxeVdn8oxRJczYhKebfJSY1cGvb5ZOqEn9mfLpkzR9WnTAuWGeQzeBF4j37Q1AvcvbcIQlKO38Wi6SnCGRTJQBsu-MMw-R6aJELrMFRLZEjahoDg7JvpL4Bjf_J-SaEv7WpwlmHBtXAOQsTr_fx2AiFD2iqHIqvWYIRn8NS067oKiuJJL94OvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638d05d744.mp4?token=EcjUzXXXOSvt3cudTTMp4pvkBVj5e1y3ejH49taK7bUDCF9bfFRr8aBhcHKWQsTzL0ttp0h_wIm7neqdtCt11EG3CPpYGxskXV77lMrG6TXFV_70ywhfzrUBP7rGb3SDEac2TndH-1pikzn09OhCG4ddlAuP-tFBzxeVdn8oxRJczYhKebfJSY1cGvb5ZOqEn9mfLpkzR9WnTAuWGeQzeBF4j37Q1AvcvbcIQlKO38Wi6SnCGRTJQBsu-MMw-R6aJELrMFRLZEjahoDg7JvpL4Bjf_J-SaEv7WpwlmHBtXAOQsTr_fx2AiFD2iqHIqvWYIRn8NS067oKiuJJL94OvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی سنگین در کرج الان
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16906" target="_blank">📅 20:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16905">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cr1EDsAxkWJsUiOEdQwISb2Ub7T2TTR-qaIa_4Dw5B6uz4cpNbeWfjevi82Z4YbWYDFdPWUKmjlRgecL7VJqjU8Nj3WCpLXtivQMStyzL5EKOh--WqEafdvR3lFGoBZ36SwwBykCWeO1U2IMBgY_vYAueJmE4-YNAXAcVr2z8r6ktwuJw-JRn3bysrOQ1_jivRlJC-xSjYThTeGZ3xyC_pkwqtB06-9SyOTgvhMhS3NKqWVJmY494bIDSZGh-Ua6ZbgGe4s3WkUiz7XNJbB1REfPciIsITkfb0-8DjRo4zYEujO6syTivsJne3USkJTFZWB953YOTy-AokxzMPiuVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش سوزی کرج الان
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16905" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16904">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ در اختتامیه نشست ناتو در آنکارا:
ایران صدها هواپیما داشت. همه آن‌ها رفته‌اند
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16904" target="_blank">📅 19:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16903">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مراسم تشییع علی خامنه‌ای بازهم تاخیر خورد؛ دفتر مکارم شیرازی: با توجه به اینکه استقبال مردم ایران و عراق از مراسم تشییع علی خامنه‌ای خیلی زیاد بوده و ممکنه مراسم خاکسپاری دیرتر انجام بشه، مجلس ختمی که قرار بود 19 تیر برگزار بشه، به شب 25 تیر موکول شد. @withyashar…</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16903" target="_blank">📅 19:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16902">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1wZJTGk3qaxRBROMMfg3XeaEjeJwjldcFvDlbdV711JN1QXV_xCjOI5J71jP32yckSDfMk0jD5wq0qJAYB2coskygk3jBNO2E893BRscKs8kTp5BLvGItsTQncb3KHgDoB9XkE6sINTwuLxmzpZ7c4mzJvjKanHJhKgMY5titxrzn6N3a1PKotbZBsXM5Pj1jeIunzzcODJImJ1uKA-zjeKoTeai34PjIby21z-XJSHc2jjMunjKk72No3KM37T41kXMfJd8zizj5lSbsSxtyLsjoGI9IA1VnHQQW13psC-OJ6X5GXMFT7XMSWe04Wj5SBYLeXXF4SqZ7dRFnf1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هشدار زودهنگام و جاسوسی E3A با رادار آواکس ناتو دوباره در ترکیه بلند شده. این هواپیما طبق الگوی منظم همیشه قبل از اتفاقات مهم برمیخیزد. قبل از ترور قاسم سلیمانی، قبل از جنگ دوازده روزه، قبل از جنگ چهل روزه و حالا دوباره پیدایش شده. معمولاً حدود دوازده…</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16902" target="_blank">📅 19:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16901">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس: حملۀ مجدد آمریکا با تغییر دکترین هسته‌ای پاسخ داده می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/16901" target="_blank">📅 19:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16900">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دقایقی پیش ارتش اعلام کرد : هشت نفر از پرسنل نیروی هوایی و نیروی دریایی در بندرعباس و بوشهر در جریان حملات صبح امروز آمریکا به جنوب ایران، کشته شدند.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16900" target="_blank">📅 19:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16899">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مراسم تشییع علی خامنه‌ای بازهم تاخیر خورد؛
دفتر مکارم شیرازی:
با توجه به اینکه استقبال مردم ایران و عراق از مراسم تشییع علی خامنه‌ای خیلی زیاد بوده و ممکنه مراسم خاکسپاری دیرتر انجام بشه، مجلس ختمی که قرار بود 19 تیر برگزار بشه، به شب 25 تیر موکول شد.
@withyashar
🎉</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16899" target="_blank">📅 19:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16898">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مژده بدیدددددددد
😍
💥
💥
💥</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16898" target="_blank">📅 19:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16897">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نتانیاهو: ایران قطعاً دارای تسلیحات شیمیایی است و اگر بتواند، ذره‌ای برای کشتن صدها هزار آمریکایی اهمیت نمی‌دهد. ایران در استفاده از سلاح‌ های کشتارجمعی هیچ ابایی نخواهد داشت!
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16897" target="_blank">📅 19:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16896">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5HO6uYT7fnjsmznvomF_KH8spkAtLV91fsmp5AdpUZiYvQL3HZiYiEgzoAOBQiCdeFrpxyAwyQOjrWb5af3f1JPBWESPhjKQTu9V7kOeJefm_QHlPFTCMa3lD7uk82k1MR7vU-bMYjom1CTNMapz84XJ4kbRHnY8sdwHaBFTZomKeFCEtZWbLOt-RSJWIkJzYr1gY5VA5g8HGY2NIDDAO7W4O61VlYcsaNeD8cW6gqA4Mc47XQ8YleAwsJNd1NQOfrqzaSRus2ot5sZf_ywjA1fpw0Di-4tA3ubEbftOy8xbMp4CPNjUCIC3gXz2vW5rDMEWjP0bEFE7RCz3vF_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت ترامپ اعلام کرد که هواپیمای موقت ریاست‌جمهوری VC-25B Bridge به پایگاه هوایی نیروی هوایی ملدنهال در بریتانیا ارسال خواهد شد تا به پرسنل نظامی ایالات متحده حاضر در پایگاه اجازه دهد از هواپیما بازدید کنند. از VC-25A برای انتقال ترامپ از اجلاس ناتو در ترکیه به پایگاه هوایی ملدنهال برای استفاده از هواپیمای جدیدتر استفاده خواهد شد.
با این حال، دلیل واقعی این تغییر احتمالاً به امنیت ترامپ مربوط می‌شود. به احتمال زیاد VC-25B Bridge دارای همان قابلیت‌های امنیتی VC-25A نیست، زیرا یک هواپیمای اهدایی قطری است و از ابتدا اصلاح نشده است. احتمالاً VC-25A به دلیل احتیاط در برابر یک حمله ایرانی خریداری شده است.
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/16896" target="_blank">📅 19:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16894">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_Y2p3FsquPulLQTsslakE5QK8y1koMGuNA---9YiNKD6xiUFBuydka9YbNgCO6WLAYElHvSqm0Z1lsLSjPOVd_YZPb2Xa_rawk5zu-WLIYCF78JXs4lNvWHe4wDMahsxkgyoTSX4OkpoLyWITwbxMoKG8ArJxY7im9aX4UAroiYBm9z3apUYeVJK3J3duBBO32E-v5EeAzW-gUgiHhpJtk4sJSdknq3h4VKtg4aKmyJ975c_2b1z0CKeizpyVzNuA6nTA3c8iUGZsBsriM0sqBfE9QpLQ7NQLJ0xexz0WKPbzVYt3FrriFgo6obImDwBrb3k7ssRHgFTVGIO_T5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b98e4f876.mp4?token=fZ4UHwQPA6aeNCVbVF2eP7cXGdQ9mH3qsUr2HC072IZQqgROSYgPpAIS4nfRDZiEalw6FJPCJgI5vlQguRrvKgfHbXEQZmKSF2QcvXeFLpgBdf-wdXI_-cpy85VTlVQwt4MXr9m1NnlWTtQ-QDCcDXAHbqixLNhQDiLPbEdE_ven9ipTPQjB-PPxo0DM8pZndj_taYv4vtIdsxOg2z3cCwzecRrtrWfhbj7C1hT-hovDV1YWoZD5XgGje0EuL9s-aKRiJlNqt2uN48AGOkhrOnzCHqgoHFo4uSvC1I29yYzi8_AKGiGZoo7ifLuzu5sshW1Wx3AEGW-MDu68CxgqAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b98e4f876.mp4?token=fZ4UHwQPA6aeNCVbVF2eP7cXGdQ9mH3qsUr2HC072IZQqgROSYgPpAIS4nfRDZiEalw6FJPCJgI5vlQguRrvKgfHbXEQZmKSF2QcvXeFLpgBdf-wdXI_-cpy85VTlVQwt4MXr9m1NnlWTtQ-QDCcDXAHbqixLNhQDiLPbEdE_ven9ipTPQjB-PPxo0DM8pZndj_taYv4vtIdsxOg2z3cCwzecRrtrWfhbj7C1hT-hovDV1YWoZD5XgGje0EuL9s-aKRiJlNqt2uN48AGOkhrOnzCHqgoHFo4uSvC1I29yYzi8_AKGiGZoo7ifLuzu5sshW1Wx3AEGW-MDu68CxgqAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدونستم یه جا این صحنه رو دیدم.
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16894" target="_blank">📅 19:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16893">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ درباره احتمال اعزام نیروهای زمینی به ایران:
«چرا باید الان وارد عمل شوم؟ زمانی وارد می‌شوم که یا آن‌ها کاملاً از بین رفته باشند یا توافقی حاصل شده باشد.!!»
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/16893" target="_blank">📅 18:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16892">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">لحظه سقوط هواپیما باری پاکستان @withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/16892" target="_blank">📅 18:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16891">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سی‌ان‌ان: تردد نفتکش‌ها در تنگه هرمز عملا متوقف شده است
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16891" target="_blank">📅 18:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16890">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c41cc5c19.mp4?token=RfuqAqX3pya4hqu76F8-DIFMCuWAcNoreFLZ6xeLMAHMP0n33JAxb371tmBUnSJxyzwvXQf5EG88H352LvKPbqB3MVgjIR--NwBlvRGtBQeIdG-9nNxhz_W_nYVJH7h5-I8oZz-weCqowSIDLeySqVeMnWjtx1-qebkZp-MKHvLSUpefTfYS5uhjzjJ6vWhpX1U7wlXXQlnj9A6yAdhL2DPYdQaVjbgyM0f8xNRsnIyc3aj9HGsWD4ICsxERIkTkk0FjMCXAeEDKabNG0jkEy8vBAjUoMPJpl-_tuxW7Qm2jFh4zNyF25JD_9BlU_010kmBfPoL-hzeAe8KO8CizsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c41cc5c19.mp4?token=RfuqAqX3pya4hqu76F8-DIFMCuWAcNoreFLZ6xeLMAHMP0n33JAxb371tmBUnSJxyzwvXQf5EG88H352LvKPbqB3MVgjIR--NwBlvRGtBQeIdG-9nNxhz_W_nYVJH7h5-I8oZz-weCqowSIDLeySqVeMnWjtx1-qebkZp-MKHvLSUpefTfYS5uhjzjJ6vWhpX1U7wlXXQlnj9A6yAdhL2DPYdQaVjbgyM0f8xNRsnIyc3aj9HGsWD4ICsxERIkTkk0FjMCXAeEDKabNG0jkEy8vBAjUoMPJpl-_tuxW7Qm2jFh4zNyF25JD_9BlU_010kmBfPoL-hzeAe8KO8CizsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهپاد (پهپاد دريايي) اوكراين به يك نفتكش ناوكان سايه روسيه در درياى سياه حمله كرد
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/16890" target="_blank">📅 18:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16889">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7-rCVBiMtk73f-3AGK-vDFORzf-tqgynn2x2cZqg99HRN10VvpA7huWL1og6cmBMVjaO6tQjf9tdRBbFzbSuuc1oqGcryfwI8MuLgYkEg0v0BeiL6Gv1tcXscqcglG2z0Z-uSDl2WoHSV6K2bRL5qV1XSRom9l-FsxjetXGFiVeXOxtSuQmVvtRKcvYLdk7QIC8E34rcq2CBgjylXtZSt8MW9Uz1xTOLuGbCMjoUvm4BSA702wxzF2QOnxKSRZ1h88GfMu3oshZ3CJJNV8lXfe48u97OC4N7xNjupacGkPyi-3s2fZN-A2eyvao6SKFqTE5Xz_mM8hpq3Yrdyb3jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت غیرمعمولی نیروی هوایی آمریکا در‌دریای سیاه مشاهده میشود، به طوری که دو فروند هواپیمای تانکر سوخت‌رسان KC-135R، هواپیماهای ناشناسی را اسکورت می‌کردند که احتمالاً بمب‌افکن باشند. این در حالی بود که دو فروند دیگر از همین مدل، از خلیج سودا به سمت فضای ترکیه پرواز کردند. این مسیر، جنبه غیرمعمولی این حرکت را نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/16889" target="_blank">📅 18:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16888">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/255dda7e3b.mp4?token=D6sHqXbe-SBb7RcjCcKVvHSmXRZhG48cuda0FE2KnszWt50BIHc0KoUahrdm56Fe8Zi_TeUp2C2BfIGuS7U0Ws5rgjY8QYqXkEpCPbPjo7YOPZyeooBoqS7b3LyWuM8987DPRQncT9ZJ1RpSl29wY6pyXGRNcrSMoFKljQfg_iEd5_mCXqP5M_y3HsY0DPTuUsQol17WQGd_dQWWV0m01if-P6kzUZWnSeMja1EboFELfqwAAmzNf6b5uvS5asygtJgt5jBRXbb5NTOc4hpxM-T2KgfB6aMlTWfziv7biZ5l2BbexODLIY2yURnXMba4k78ynq-3mpRSoNDMRSYhuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/255dda7e3b.mp4?token=D6sHqXbe-SBb7RcjCcKVvHSmXRZhG48cuda0FE2KnszWt50BIHc0KoUahrdm56Fe8Zi_TeUp2C2BfIGuS7U0Ws5rgjY8QYqXkEpCPbPjo7YOPZyeooBoqS7b3LyWuM8987DPRQncT9ZJ1RpSl29wY6pyXGRNcrSMoFKljQfg_iEd5_mCXqP5M_y3HsY0DPTuUsQol17WQGd_dQWWV0m01if-P6kzUZWnSeMja1EboFELfqwAAmzNf6b5uvS5asygtJgt5jBRXbb5NTOc4hpxM-T2KgfB6aMlTWfziv7biZ5l2BbexODLIY2yURnXMba4k78ynq-3mpRSoNDMRSYhuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره اسرائیل:
اگر نخست‌وزیر دیگه ای (بجز بی بی) داشتید، اکنون اسرائیل توسط ایران به تکه‌های کوچک تبدیل شده بود.
و اگر من به عنوان رئیس‌جمهور امریکا نداشتید، اسرائیل امروز کلأ وجود نداشت!
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16888" target="_blank">📅 18:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16887">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f22ec3f9c6.mp4?token=A4l4xgP7bVN6fKOAoEREesbr77E3DFpJ6Q3bGxu3hoWgL37HgCdLEAZA54V-dcJ5pYwdXaN8WPac6weMCceYTSTj48EnmVeQuCBYb6EtnLgUqVFr8FfAT9F78cH7YL0F5hGYzKaNfeCGEEIXaMsAyFEEq2IwianVc0ASY5m7_FKqC7JDMLY_jJSiyDP8tGUE6Kd6J3pO3QGzLcRBQl4CgpJBtKmtlnG1ocHKw9yRgU_fto9i34mdfOuiAPUUK3Y7rdBmNA48OjXebg5rz1pWK0gJyDeREwEEEqTyroByrj31HtEBFAvuZDP8GdFGzHQttAhjp-kE0V7Isb_SGXCgIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f22ec3f9c6.mp4?token=A4l4xgP7bVN6fKOAoEREesbr77E3DFpJ6Q3bGxu3hoWgL37HgCdLEAZA54V-dcJ5pYwdXaN8WPac6weMCceYTSTj48EnmVeQuCBYb6EtnLgUqVFr8FfAT9F78cH7YL0F5hGYzKaNfeCGEEIXaMsAyFEEq2IwianVc0ASY5m7_FKqC7JDMLY_jJSiyDP8tGUE6Kd6J3pO3QGzLcRBQl4CgpJBtKmtlnG1ocHKw9yRgU_fto9i34mdfOuiAPUUK3Y7rdBmNA48OjXebg5rz1pWK0gJyDeREwEEEqTyroByrj31HtEBFAvuZDP8GdFGzHQttAhjp-kE0V7Isb_SGXCgIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: مکان‌های مدفون شدن مواد هسته‌ای در زیر کوه‌ها را شناسایی کرده‌ایم @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/16887" target="_blank">📅 18:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16886">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ: مکان‌های مدفون شدن مواد هسته‌ای در زیر کوه‌ها را شناسایی کرده‌ایم
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/16886" target="_blank">📅 18:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16885">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بلومبرگ : ترکیه در صورت لغو ممنوعیت فروش توسط دولت آمریکا به آنکارا، قرار است در یک معامله اولیه، ۶ فروند جنگنده F-35 از ایالات متحده دریافت کند.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16885" target="_blank">📅 17:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16884">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هم اکنون مهرآباد دارن هواپیما هارو خالی میکنن !
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16884" target="_blank">📅 17:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16883">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8669368d.mp4?token=ssZlpyZDLe707nIIDbOY5MCfwekno6X3jeBKCviREhGcbg7LKmDEg06LHG3MTlC85cEdhYHsmHmvxycOc51CDjCuWPrG6b-8aqpLixv9ZRJKFjcXuwJMwIr0PfpNzzRnMMFUX_b9ZyXXURL8zbj4JYEfU9knb_PN1Uzj_K1uAkTCGXjKIw-4Tqdmr0EOOcrBjRO6DaeukzkKZf3ZyNFUQBOWp4jbXdyiY0roy-z5Vegjl2dGKzFjFPkHhj6-BmEn8fwpz38m5P8TTVnDGSHh0zZoD1TT0ziDwguauunXIukUG29x6GLTeXtRyiPg20Zhvovg53wfml_t1i-HCm5tAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8669368d.mp4?token=ssZlpyZDLe707nIIDbOY5MCfwekno6X3jeBKCviREhGcbg7LKmDEg06LHG3MTlC85cEdhYHsmHmvxycOc51CDjCuWPrG6b-8aqpLixv9ZRJKFjcXuwJMwIr0PfpNzzRnMMFUX_b9ZyXXURL8zbj4JYEfU9knb_PN1Uzj_K1uAkTCGXjKIw-4Tqdmr0EOOcrBjRO6DaeukzkKZf3ZyNFUQBOWp4jbXdyiY0roy-z5Vegjl2dGKzFjFPkHhj6-BmEn8fwpz38m5P8TTVnDGSHh0zZoD1TT0ziDwguauunXIukUG29x6GLTeXtRyiPg20Zhvovg53wfml_t1i-HCm5tAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داریم به این لحظه نزدیک میشیم. گفتم از الان داشته باشین، سیو کنین، چون اون موقع ممکنه اینترنتتون قطع باشه و نفهمین چی شده. @withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16883" target="_blank">📅 17:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16882">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دبیرکل ناتو : تنگه هرمز را باید باز کرد
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16882" target="_blank">📅 17:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16881">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ: وزیر جنگ هگست، از ایده‌ی ترور مسئولان ایران در مراسم تشییع [آیت‌الله] خامنه‌ای استقبال کرد
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16881" target="_blank">📅 17:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16880">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ: میتونستم همه رهبران ایرام رو در تشیع بکشم. اونا از من خواهش کردن که قربان مارو نکشید. منم گفتم باشه. بعدش به سه کشتی حمله کردن.
در یک روز می‌توانیم تمام پل‌های ایران را تخریب کنیم. نیروگاه‌های برق آن‌ها، جایی که برق تولید می‌کنند را در صورت لزوم نابود خواهیم کرد. آن‌ها تاسیسات تصفیه آب دارند. در صورت لزوم، این تاسیسات را نیز نابود خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16880" target="_blank">📅 17:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16879">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ: من قصد دارم به ایرانی‌ها یک هشدار ساده بدهم , امشب به آنها ضربه سختی خواهیم زد.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16879" target="_blank">📅 17:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16878">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ff4e7c6e.mp4?token=lxsq_eGpJV7GkTLjdOTDjvO4hdN6jC5Mcb2ZY0wv8s_5SQEIhfM3S6OxrZSZtDpxLmosNYyz_4zAkjPTlLgiZoVlm08HxYfImF-2ABDR-ZBgBLqVAn-d19zUMAFsLuQ_aA1CeUgVwdffc56aJtLUH7UW2Ke8anQiDbff2FdjVzFNua3IK5bI4ZlxZbdASQhJiDYtpUeGy4YZAd9ZvOfnd2SonDQpZ54wgQdOEIw4qCUSPnP5_r-JtMfVDWNCnmNcuOpM7KNePXguAwA2BY0j3YSXBMD4V2uamLr1pn1Djjm79iliDeKwhhD-xJmtxWQkybZC0tTmOGfMGmX8fCPijw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ff4e7c6e.mp4?token=lxsq_eGpJV7GkTLjdOTDjvO4hdN6jC5Mcb2ZY0wv8s_5SQEIhfM3S6OxrZSZtDpxLmosNYyz_4zAkjPTlLgiZoVlm08HxYfImF-2ABDR-ZBgBLqVAn-d19zUMAFsLuQ_aA1CeUgVwdffc56aJtLUH7UW2Ke8anQiDbff2FdjVzFNua3IK5bI4ZlxZbdASQhJiDYtpUeGy4YZAd9ZvOfnd2SonDQpZ54wgQdOEIw4qCUSPnP5_r-JtMfVDWNCnmNcuOpM7KNePXguAwA2BY0j3YSXBMD4V2uamLr1pn1Djjm79iliDeKwhhD-xJmtxWQkybZC0tTmOGfMGmX8fCPijw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران: ممکن است محاصره را دوباره اعمال کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16878" target="_blank">📅 17:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16877">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرنگار : امشب هم قایق‌های ایرانی بیشتری رو هدف قرار می‌دید؟
ترامپ : معمولا بهت نمی‌گفتم ولی می‌دونی چیه؟ هیچ کاری از دستشون برنمیاد پس جواب احتمالا آره‌ست
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16877" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16876">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سی‌ان‌ان
: خدمه ناو هواپیمابر «یو‌اس‌اس آبراهام لینکلن» می‌گن پایان آتش‌بس و ازسرگیری احتمالی درگیری‌ها برای آن‌ها غافلگیرکننده نبوده و هفته‌هاست در آماده‌باش ۲۴ ساعته قرار دارن.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16876" target="_blank">📅 16:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16875">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مدیر فرودگاه‌های هرمزگان در ایران: فرودگاه‌های استان تا اطلاع بعدی بسته شده‌اند و پروازها به دلیل شرایط موجود در جنوب کشور لغو شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16875" target="_blank">📅 16:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16874">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">l
تایمز اسرائیل: "ارتش اسرائیل اعلام کرد که انتظار چندین روز درگیری با حکومت ایران و احتمال ازسرگیری کامل جنگ را دارد؛ ارتش اسرائیل همچنین از «هماهنگی کامل» با فرماندهی مرکزی آمریکا، سنتکام، خبر داد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/16874" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16873">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یک مقام آمریکایی به NPR گفت: «به دستور رئیس جمهور ترامپ، آتش‌بس با ایران پایان یافته است. رئیس جمهور صبر خود را از دست داده است. از این لحظه به بعد، واکنش نیروهای آمریکایی در خاورمیانه نسبت به ایران به طور قابل توجهی تشدید خواهد شد.»
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/16873" target="_blank">📅 15:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16872">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2j_n33KdsM7f1M3ZlwBYSRXt1dYmy4pqaBEY0Rj9ab9nuWkK096NIfn10wMTTACp6BkXDMyB4g8rq21FDdLE95dmz4Pu7TfKnfUqo2HwWbN26V67q894xH93psVoCzrIJNcWYlPABFF5XiKmp5ewyVjZhtfwJCJ7zoVEva8b6zeKLn-l9dT26iDpyhoDTbVumNqL-IeGHhr5E5yBVyJxFBIi1TLdMDnisb2FES9ABq5punpMVHE9Z7VDT_YEAEyUt7W1jBy-2OI815g5XDDbejRugvouzFqJcx9uLJqY3oUwmKWVzJHK4XD-SZ70rf4O-UsjiX_S37uG3wR2PUhQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه دو صیاد در حملات دیشبه سیریک کشته شدند.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/16872" target="_blank">📅 15:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16871">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTc2ZRujdFWA90K2PdyMNGSXntUOdVK6enRqvg2hKc0__1st_GjAG3YoGWfT0wG-4O_UttzLg55v779nK0EIxK0MwDB2Ll4zKnCUeK2CO_6aj8Oht3dDni3vDp-a1CX7KCPSKCxktPpNCarF2Nn5grecXz1LnDLfTskZ576yE0Lx9x06XNOw8EAq39l27A8w_vH_wrcf6HweDsaRNPgT-nJI53SXCoF3aXr6NyFdvyOA0cwG9V8q8qYgoKyXAAXtDmm2K6SKp6UEFXuBDnYzUlnH_vBxj2UneEmDk6cwyrMChLHmfVGwBBpSqtJsCCQWAgb6dyeC_0Jq7EBJZtSA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیریک الان بعد از‌ حمله دیشب
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16871" target="_blank">📅 15:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16870">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">موبایل در امتحانات دانشگاه آزاد، آزاد شد
بر اساس اعلام دانشگاه آزاد، همراه داشتن تلفن همراه در جلسه آزمون پایان ترم تحصیلات تکمیلی با رعایت ضوابط و تحت نظارت مراقبان مجاز است. همچنین در امتحانات نظری دوره دکتری (غیرپزشکی)، استفاده از ابزارهای هوش مصنوعی نیز بلامانع خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/16870" target="_blank">📅 14:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16869">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فارس: ایران باید پایان رسمی تفاهم را اعلام کند
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16869" target="_blank">📅 14:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16868">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ : به نظر من، اردوغان هم از ایران خوشش نمی‌آید
اردوغان شخصاً فردی عاقل است، در حالی که ایرانی‌ها(مسئولین) دیوانه هستند
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/16868" target="_blank">📅 14:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16867">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">توییت یک عرزشی : به ۱۴۰ نقطه در جنوب ایران حمله شد.
معافیت تحریم باطل شد.
کریدور عمانی ایجاد شد.
عوارض ایران از تنگه هرمز هوا شد.
قیمت نفت نصف شد.
تجاوز به جنوب لبنان ادامه دارد.
پول‌های بلوکه آزاد نشد.
۳۰۰ میلیارد دلار سرمایه‌گذاری هیچی.
رهبری به ترور تهدید می‌شود.
خدا قوت به پزشکان و قالیباف!
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/16867" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16866">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دریادار سیاری: سواحل ایران را برای‌ دشمن جهنم می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16866" target="_blank">📅 14:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16863">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g8jH8EzTLjdjUKjPRU2IpwncrnMdfqfpzoBSgO7sNoWnGj3TymlJqCMeu7-P2vLkhV_LGiYz7AJVg7B0R0o_2b34Nx6xTw7i9rcsC59Mczvbtl1eb3CYlVrkYxAFNpQ8bhemUzS64Xr5VscjvaAzjevktelYU5LfyrpEpc4ol9ZcJqvnCxKo5kYNPHJ_1ShagiOVJ0DG2bUB_QLXlorN0Aw19wGwFrLG5stvTuEZm77n4cpodtmOXev9WYL7p-jelhi_To4_qLJt29t0RI3SbGH0sVx1zBDEuODfjZOYJBtMsXYKzyre2ROnURnJ1wxbMszZFqo34WIc8JEDL2pxsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kVncFBQArXOZIpvcdDKcSB0NZJdL2pzMHqsMY6n0MJeiO3ybusDssHPUyYbfspfgxCUjvykKtZe5rMOfISlt0T4S6xBYgRi8P_jXtWU5UjialIKSDicCMdrlxjhyY8hEzbQxBbTXcZGW-12Dnor5vxGsZO63WpX5M5NW5td0xRK22o_6MEDePw9qKnS4qpBGYV0QHkM2Qs8vWfM7pNjGoUoDGZfjTxG2QT5z6ryOGYpO9a4C1slKPwln6-0GuwqyemPbQXV3YEy_UrinfWlTbqWP_YCLbEG9qMAwB3VmnjM-smGfKF1Bh8YSzcaH5eNNMeC0B9GcB4yEsp7Rsuv5cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pL3UpFgUnrJucp4Firac_LTYTTv9yzwUQR7W4ugcUuw4Is2RYCZ1V5urbg0l5BAmcjg68l0G__KfWLhw17yL1ilpQZo8Rai7_mdLwyn6pHi05tJkcLrLMknR-6cvLb7Mt3Knn6kLlvFTvQPxSDteIvzjVGs4IGH3cnaQ_38SkAgfoQiMyVA98yT8ahaXGqN8HMG0AvOkjivpsMpbDjNrt-0G07zsQLkuWr3zwc4IdUv1VDYdz0cKkvdNlXTCwcagsvhwVFC-R-hpHMTzvmochi9pDrSHeWJ15H6cmMDIPMZq8XYCLN2uWRMm0ot6mshu2KX7FGArb-IX7dtarLpifw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری تسنیم اعلام کرد یک پهپاد تهاجمی MQ-9 آمریکا در آسمان بوشهر سرنگون شده است.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16863" target="_blank">📅 14:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16862">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7OKXKnd_WjUwNBXeNIPbMfs_Uo6LEYXcU4BEz5kLzvzHllLBeId6ASIP9THdhbvhjHYsZ7M4Wt40BUeUpcZELIIoE64P9_7x1rnzfsRqM_jWSmAsPgONKCTFER6lkoD94LMLqOcihmYPNyIOYtKlr787OrT7zTldmg6Vaxd9o6qT5Lx6t4bRZodMVZZ2ZKJdzzEZfz7xKBFxMfWDvAh2RiEHEaJMM9d_9QnZ9kzMzjUr12iybfUEs7axbTxmbZ5OMavhC3yBp1L85CFDyOMuuu34zOismeubllI_61Vx8Gy310OpjSW1egVt3ZZ42fU3qic_3WyUecRwvvimm_hWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای انفجار و ستون دود جدید در بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16862" target="_blank">📅 14:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16861">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رویترز: نفتکش آمریکایی شورون در دریای سیاه هدف قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16861" target="_blank">📅 14:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16860">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هیچ چیزی تو دنیا مهم تر از سلامت روان شما نیست  !</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16860" target="_blank">📅 14:06 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
