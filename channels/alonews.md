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
<img src="https://cdn4.telesco.pe/file/e6jl1dYsBZ9azK4PTMlG0qUNCGQ0njZ7HlM0oKxDhUrMXUwMpt50G8-4V5QwQ2UFpHcd2Gvpgw9E1-gMcman9ooMshQQumGURn1educ4WY4HuCGOOXd8YDpDBs1mNcznSCAQUw7WyUrc8B-RM7zHtBZEaLYFKnAVOLymFU26MD-fSQXV22aFwzCsWRz1xeFK1DmSV-9uT3owYeHUfQwM5iIwKSyghDSFM56Iwxnu6AmgV5kfLR0jm95-WyOKR9OVW3QqRQlzCrEIC_Dqaej5HOCpgvwk-PneUKFDXPFl00_dFWq2lzaHYSPxBM7rdS7IyQ9ih48DqJApWvYy3XO_eg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 981K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 10:53:40</div>
<hr>

<div class="tg-post" id="msg-127067">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
رسانه‌های عبری: اسرائیل امروز به لبنان حملات بیشتری خواهد کرد اما از حمله به ضاحیه بیروت خودداری می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/127067" target="_blank">📅 10:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127066">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b649d4c9d9.mp4?token=uDmnDX5cP9sJrBt0ELi0-QA8KSRAvlKM05CBEGeugXEEJEyA3ILW9yyVv9BJpm9hsPCOwg9kzl8TNFdocADDpAIaUrohvCmJ_zBCfy05b80z_xFF74RN3Hr4NHgAjAwKgrgzLNfz3AjhwQ9U8ADGei2XO-laeH6zUFpXkW7o-8FjIVZ2hDSdFIG2caVwXgnTCsP3qi85KR_sXb0jDn71KRRHnNQ3tlmCpYY44W5eaRqXjxzZzYeoP4A0fDhQLrmXAhHBU24Uca8bzol5W1Hwxk3iwMo8FaM8wFiYCkcZcmCuWGUjHXOR3BCCkkAf2uTzhTOWKZUBpuRZjaHNpwg0VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b649d4c9d9.mp4?token=uDmnDX5cP9sJrBt0ELi0-QA8KSRAvlKM05CBEGeugXEEJEyA3ILW9yyVv9BJpm9hsPCOwg9kzl8TNFdocADDpAIaUrohvCmJ_zBCfy05b80z_xFF74RN3Hr4NHgAjAwKgrgzLNfz3AjhwQ9U8ADGei2XO-laeH6zUFpXkW7o-8FjIVZ2hDSdFIG2caVwXgnTCsP3qi85KR_sXb0jDn71KRRHnNQ3tlmCpYY44W5eaRqXjxzZzYeoP4A0fDhQLrmXAhHBU24Uca8bzol5W1Hwxk3iwMo8FaM8wFiYCkcZcmCuWGUjHXOR3BCCkkAf2uTzhTOWKZUBpuRZjaHNpwg0VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدن این ویدیو برای همه مناسب نیست
🔴
شلیک مستقیم طالبان به یک خانم تنها بخاطر شرکت در تجمعات اعتراضی بخاطر حجاب و تحصیل
🔴
پ.ن: سخنگوی طالبان گفته بود عوامل بیگانه در تجمعات اعتراضی شرکت دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/127066" target="_blank">📅 10:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127062">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kA6ksxFpJE3vrdQtfHZCR2kpkMwfcjPsCdu9K34azUuHJOY6bUI2bsQJ1ELMz9U_wAgeSj7NLvHB08bu0LLNlnFQR9If4cxRYztM_LRklA1-q541_fgAjiWjGs6mYW-B6GqT5KzK4kowysQNjqn-5KOrvFs2pH-zwKYhRHqfdDMZz4wlHfrm8Bqjbrv8v_jpFIMbPG050thgy4kJY5G92TkPJEstoTEmGtyJ4ocK0_B-gIZUdOw07PKgJ7_GjUFFa6VI2mzIOtKsbwaYVq5aJfHV43U-YlZvy2LVTGBA2qzZTW_AwrNkPCOEfbjKietSwMaBnkIUcMVlqq-nsTf4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rWee5PU2l-tICfUiS6R8PI33wV_ZkQJUQLmUK17kWRltGN6k572WhmPxrpc7FAnRVqSwnhmFg0aPCSZGxbR0a8B-sHRrTbNQ_t3l7d-OB7-OQcrdyQ7SFwu2EkweCV-hBJGGfOsEqTopI9BJpO5aPpsYoiSXIhhSNOJje_lv_C6xYBbIMjypV1juGSYd2zKsgP6rBgxP1Uhg8XBKdi9UFnCtziyv_dXVrfaH9triWAbEUrbukPR7-7U_sXKW32qPXuW4sWTsyJ9A53HeVzbQmlGpelPy8Bbvuooq17JDh12Q4rH2TDmPhTqVBEbGOtpjvakuVdPBR5vL1W5b2kXM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mHCfP5Yem457xrEry_YPvsHghYzR16FgtVVjswtNK_uBCUsAS3t79noTlO8eD4TTtROR6YGUu3PRNfT8SJJO117Lttb8S_kZadxUxkqcl6fniHKGdEDu2EflEsZt76t8ci31m7Wt8NKtu2S8RrjYoYxRwqQnppY2L1PwkpVTYQLsDda7nNtfkR0epPVK0rrFwOxWeBNSJSSrkubw0Yk67LkSkouNpKhhDr4ISxXcVtyuF1D_rb7tFMvuKQwwBwsNLDMySxPkQHBqi-hIgQtqtFEgVhq6SOK2arELXc58ENHVtR9PzY7PLBFGx1wifDRyLOJlM6lWbmwL6NV0PbcmQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
خسارت وارده به مناطقی از شهر منامه پایتخت بحرین بر اثر اصابت موشک فیل شده پدافند پاتریوت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/127062" target="_blank">📅 10:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127061">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BX319zTGJF0N-EyU9IAr4YQbRvgFM2ZFVuPwXmwxocU06fEMxgZLvLvFKBLt1xRKn1b8T4AuLEGbPxADn2BiwpeLq0JAQZtx5DNTZu7hjCs4sEphctJDCAxV5tObk0ybR3KAu3iecOu69lFbG03ygfpeROOu0g5YUk72NNXIcnDqhGnPWsIdOmb3Yk_mUf3t5UbtZe0v0DH4ja8QRCRTcOfKmu4u077zGxwItb9cSB2pGvYhH0Bu28qLfSEYtcbn4yJ-D65C8EVzZEeYYieoKz_5zAetGMR-ebgXZo9zEpiR4gtHk7rN_7Ab-j2rNk-P0bRDX5rkyk18s5dx01-3fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یوکی‌ام‌تی‌او گزارشی از یک حادثه در ۲۱ مایل دریایی شمال شرقی صحار، عمان دریافت کرده است. مقامات محلی گزارش داده‌اند که یک نفتکش در موتورخانه دچار آتش‌سوزی شده است. هیچ تأثیر زیست‌محیطی گزارش نشده است.
🔴
مقامات همچنان در حال تحقیق هستند.
🔴
به کشتی‌ها توصیه می‌شود با احتیاط عبور کنند و هرگونه فعالیت مشکوک را به یوکی‌ام‌تی‌او گزارش دهند.» - یوکی‌ام‌تی‌او.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/127061" target="_blank">📅 10:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127060">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
رسانه‌های عبری: اسرائیل امروز به لبنان حملات بیشتری خواهد کرد اما از حمله به ضاحیه بیروت خودداری می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/127060" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127059">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ta2JU0tKTRXHP8nZEZc7wW9sWDOy8BgAxLwJZ94spi_dwahAg0AzGGfF-6mGIm9BNcipnXbhzvD6_gkPajdbjAn_T1NQK_HnlT36gfbNvVMQoBtGBuRqtajoTJ3v8MYBpYDgGRfE-tB_IPj0ZcTmdB3aTtGJO92NFmkuHHcgFGYyW0vUMDJuTK7paggNWZsNYv4tNFGmSYcmBHYI-um5JhZfLcfj0UHXDNV0xkFp4w4yrtWGiSQwC7QGdCCYb6ENCQse3hr7txGyWqreWCNVdxQ-h9RA7h9Qg3wJaWpBKuN1FwL9fK1fJoSiVzXimFSZeIGjOHJCBxjsc9wDP8UZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: تولیدکنندگان بیشتری برای رساندن انرژی به بازارها در حالی که تنش‌ها در خاورمیانه ادامه دارد، به تاکتیک‌های مخفیانه روی می‌آورند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/127059" target="_blank">📅 10:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127058">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۴ ریشتر  حوالی نورآباد در استان فارس را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/127058" target="_blank">📅 10:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127057">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8GNFhykcv1-LKVsg4WBsY3h4NyUuaWUdEc92QfsQdzEJqna3hD2ilDkOjE6SH3TQ1QdpNJn15MlR7wmahy-8epILs8C_8HG5ZrRSjn5F2VRr_i09UDs_ltFlLp0__H8vuSHjPsHUlWrcVvnFS8k8MqcbKNzBaksBOWsdkoXOeQk7rgcPXvudurZNuDewfV2kfI3GT5jqP7xk2BzsdTRrp8BTQTnaflD41Y7HCEZqsbEJugwlhFi9xKuYfgJE6tTU7kCgGuhdGTF5ljLsVHKb3_vnRHeJO_HT0uJTVh52aOj8_1M3n2ELxfs9KQ-MP7cr1DeWkP67gZxTxWQO8ySIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
اینترنت رو قطع کنید تا دشمن سواستفاده نکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/127057" target="_blank">📅 10:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127056">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fabf4cc4f.mp4?token=l5HseysWIkrohuxwryrHsh9TTZII3tMRxjcJe6A9wEpXyUPR2e5MQIvtcrPq171EYq81r1uTkjDGikmzcCBjPk0-06c5f0rmU-EG1mvuu_lZNSjr9p0kww5EzovCtCUcKTWIuivIVcxJgkbigJcobH6y0LBNXPFcEUh5ibF0KJHOj_UNjSX2FYJces7UcW9I_AtB-0CLTQiofXP2NLEeAwtWoz3ny-Mju21AeZX1lNxNluKt_0I7lMzxmbglikXGVXHtvZtnlS-830iBHx0kgk4Fbv6XTbzT76qRXS60kDtzi2rfNqnooekFFYNer_as9WRzC_W34fWtLXqyhW13ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fabf4cc4f.mp4?token=l5HseysWIkrohuxwryrHsh9TTZII3tMRxjcJe6A9wEpXyUPR2e5MQIvtcrPq171EYq81r1uTkjDGikmzcCBjPk0-06c5f0rmU-EG1mvuu_lZNSjr9p0kww5EzovCtCUcKTWIuivIVcxJgkbigJcobH6y0LBNXPFcEUh5ibF0KJHOj_UNjSX2FYJces7UcW9I_AtB-0CLTQiofXP2NLEeAwtWoz3ny-Mju21AeZX1lNxNluKt_0I7lMzxmbglikXGVXHtvZtnlS-830iBHx0kgk4Fbv6XTbzT76qRXS60kDtzi2rfNqnooekFFYNer_as9WRzC_W34fWtLXqyhW13ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از انسداد کامل تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/127056" target="_blank">📅 10:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127055">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5ceee7bed.mp4?token=oHsL0lPOkbi_jCsb6W_-eXF7397Ad222OdFLTf4duk-Pqw5CHfMUdNqHnq2-ozZDCEObjjm64F2uZtX5xlK5SS9IFUhZDrmuq3hqWRS_ejJsrbAzNJS04iEoxWksXitiHH-eYKoSpL4wOB9LHPaV7fOfdC893NITWuV1jYz4jKmeAG2T3kdhn-KjHer95PYNPjqkC0_hFtbknQZHOT7mbCCv7ACyete9qgmhLj45oqIhCYdP7R98-nll4Wo2C_I5jtC_CZZgCmET6nTDIoQlLN0HbmHOBMadPHFq_nwwvDY1mrpC1uV_VxyeEjChA-GA7JllHTSNfA6yHp8i6_fgRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5ceee7bed.mp4?token=oHsL0lPOkbi_jCsb6W_-eXF7397Ad222OdFLTf4duk-Pqw5CHfMUdNqHnq2-ozZDCEObjjm64F2uZtX5xlK5SS9IFUhZDrmuq3hqWRS_ejJsrbAzNJS04iEoxWksXitiHH-eYKoSpL4wOB9LHPaV7fOfdC893NITWuV1jYz4jKmeAG2T3kdhn-KjHer95PYNPjqkC0_hFtbknQZHOT7mbCCv7ACyete9qgmhLj45oqIhCYdP7R98-nll4Wo2C_I5jtC_CZZgCmET6nTDIoQlLN0HbmHOBMadPHFq_nwwvDY1mrpC1uV_VxyeEjChA-GA7JllHTSNfA6yHp8i6_fgRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صبح امروز یه شاهد هم تو کویت دیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/127055" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127054">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
کویت حریم هوایی خود را بازگشایی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/127054" target="_blank">📅 10:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127053">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
نیویورک تایمز: حمله آمریکا به مخازن آب هرمزگان می‌تواند مصداق جنایت جنگی باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/127053" target="_blank">📅 10:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127052">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیر دریانوردی هند: سه ملوان هندی دیروز در حمله ارتش آمریکا به یک نفتکش نزدیک تنگه هرمز کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/127052" target="_blank">📅 10:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127051">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سفارت آمریکا در اردن و عراق امروز از اتباع خود خواست تا در اماکن امن پناه بگیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/127051" target="_blank">📅 09:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127050">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
اسرائیل هیوم: شرکت هواپیمایی ایر کانادا تعلیق پروازهای خود به تل‌آویو را تا ۲۴ اکتبر تمدید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/127050" target="_blank">📅 09:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127049">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_s7L0UR-toZnhvopEPQIlXrxRKqrdNhX19Dun2pPZQXN4YuV4hW_TTe90B-XJzksqHRGKJnpxTEYdk_er1Xs79igs_-I665r-i50tcBH5ShjeZ4L-S4zuDjn9FsQxvX74bDwuHKztizGkdJGvGbIVVti8gG1ejRPtjkNVt1aHlEeIM23aTQI7gNR-3_UjptpjHXRNrNfjxhcPik8Z00jbXD2KM0ils8Qc7KroePyef_Uci2Dgt8dMVf304wM6wQG5_0EmNEvHKxc7M_q3r_JH2WqnuqlA6NR_ReeCYBIoVlSaL_cWMxBGiijhzibtdFkVdjDoWV36-dxpsOId1O4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل تخریب خانه‌ها در روستای غندوریه را آغاز کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/127049" target="_blank">📅 09:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127048">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سی‌ان‌ان: میانجی‌گران قطری همچنان در ایران هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/127048" target="_blank">📅 09:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127047">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
هم اکنون حملات حرب الله به شمال اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/127047" target="_blank">📅 09:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127046">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZksRryjrrDoA6LSbrn06mENDcJWT8L9lG36B1klSJSUzDNuaHD9aHUhNvCzZ9rG688Hs59CNvyao16E7_JCfM1i_nZiMwtFddkZRzS7NB1NjQT1kQQT2QqZBYTYUJ-4qxpXIXUbBhG4UZmSc2a7RxMuBMlC5yhsq_TtOCgrCHyi3oAXRuf8z-IykDvmQkjHfQ3QcfxB4E3pdLHXn7eksVdn49fReCPFQoACqy-IMMbzD6MGYd-DJM0UaI_8q6d5oNmQP9DR1GLLGLxgC2IGramlfuxXrmnq-3HpEosWfQYOKvDuCcwMpSb7tBcTwJukWA9mplNLZR5sPkKo7qYwQEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/127046" target="_blank">📅 09:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127044">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFeUjPdT2BmspYSeZTrSP2u7vykikhrgtWk473P_CJHgZDWRSeW4rkGcm2wX1Dsg5dsk7oTDCzb1CpYFkS60k1oyrQ-LD3WxU4Z4mRUh14PPXjfXpTgS4fTSAoJKdu3XxLS8DC7sfZoNdrnYvUgsizVVHH7wQZufnCeCVzZbYOM5MuHXj0VVVboXst2b5DyHePPWg7xk6NcqPgxaXzvNsRi7YtpZQSf5RUOsM1CcKTfsAu7OkiL9Sy3gPez-HehApfUv0g2PdMxXsd2whOdQG2HzCt7u50EqEuKrtPTXo9OXus07iq-0ZhQo6pji5cVLn8I2vDEqY0XiFIdRAJM5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cMhFViEfldfYprkJF_YU7LYYeiOriEp9fRy6_aIZCpvZfsxnqspl8vUcPkmQSZm6_5vqhOl-vMXxkNJQ0cltk97e-SJEbxWlY6EPjNfocX39sxxcmocEQPeG5xKJ2qyL16Ot_iGxDpKEPnza_klyOLGpNcyb-RTve0URgsePuI79btlPHpmmvcs9Pwxhn7QvZg1jfU9EWhsdhFnV3b_wMNn4Wfup8nGGoF4z-YQ0zxzqTJFivQYkJWdmpyHTTtLfrAyea9L08Zsjm5jngCnyCNt3BvZ9mMhSEGbyRYvXe_S7oYlOxc-Ac4isomzx0A6hKQ88iKgoX9ovH52dulCY3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تی‌آر‌تی: آمریکا در جنگ با ایران ۴ میلیارد دلار تجهیزات هوایی از دست داد؛ یک فروند اف‌۳۵، چهار فروند اف‌۱۵، دو فروند اواکس، ۱۰ فروند از انواع هلیکوپترهای نظامی و ...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127044" target="_blank">📅 09:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127043">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KfyQYhOv6f1JtErtKCEyyPHXncq818wVE_ZWzo81KCg6HYqGLqV_egOhRDN7_Q3c_sY40KHlASOUtLhoU0WKoAOI08m8mDTzyVvqsVzhMdjyqZfR8IhfxQki9ji11gqlfGY7M0fDxUfoZW_vGeCqdFomRzagf4Ynm9eEqNNR6mDwv7MPMGQTEhxQtIbyCNrGrD0y5wtWHslJE7PU4ANlOXbqQpUQWXwX1CoGhIwTWKCsoxhswzHEJo4cYOPFmfn2oQ4pb8ZYjHjvAexxSx5xfjSQ_X1dkVASw5za6ug-QxPvckoop4NbIG_tvKbgSd7IWpiZ8O5Xkak64zHO7NAeDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، رئیس جمهور آمریکا:
«اگر ایران توافقی که ما می‌خواهیم را امضا نکند،فردا(امشب) نیز اهداف نظامی آنها را بمباران می‌کنیم»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127043" target="_blank">📅 09:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127042">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار در محدوده شرق اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127042" target="_blank">📅 09:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127041">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIMBYhi_UcE8B4rSJkdjBEQpYHdkPB3Vr1PpxW9jONs3YlP9tcTWGJSBlPrlRo3SlQcakbI-JPff4F9OLAqa6q0qXhbEsSeK4qE1nPHaag9gmbuXlkraX-h_ZxdaPYssQYYxHgLTaEw_ivi7GC7OCTa29yWcdeYWBk5Cx3CCY-G0rSYCzoyAdE352BwGzsHwxg6j2TqC5KrNI-LHCtwTn8dlmrIDnlkT9JSl0f-xS9ixuW0hQakTeUhcTq-qSQyAqWmGXWIQQKA6o5JhhALsZhQRY1JER37Ff5TPone6I7DjxbllQpbM2y3wz_kXmGxvmPJj3Q4L0EDfAOTZZyC8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های ناسا از احتمال آتش‌سوزی در نزدیکی پایگاه هوایی عیسی در بحرین پس از حمله موشکی ایران حکایت دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127041" target="_blank">📅 09:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127040">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
صدور حکم دوومیدانی‌کاران ایرانی در پرونده اتهام تجاوز به دختر کره‌ای:
🔴
حبس ۴ ساله دو نفر از ورزشکاران؛ دو نفر دیگر نیز تبرئه شدند و می‌توانند به کشور بازگردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127040" target="_blank">📅 09:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127039">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
گوترش، دبیرکل سازمان ملل متحد، گفته است که آتش‌بس در خاورمیانه «بیشتر شبیه به یک آتشِ کمتر است تا یک آتش‌بس واقعی.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127039" target="_blank">📅 08:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127038">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/758c0424e9.mp4?token=hKTs0I5lYTHGwBmrUP6PMAK5t2A1j6qcQV3Y5kaOOze8b9VCUoSgf6-PMIEiyqvxorT1kEt3a-VHo9zBzi4dGyZxMlAUpwmHufeRkQSqeaNedW-KJoggqWb-B7dNLnZ7M_3CKdTa-p3Ovrabr_aPFtWpqE3xO_uSvPIM0I5B7pmzpVVCXnKXKNwNd8y152TRQ4AyRfM8M5_s2XGe26r8Lf01oI1K2HvGFUGSSkKXzlV47cdyGyHIgJOCdAFOnpACZcVp96phv27vvWJGfv-eYvggUuzx6YmWEaUFR09kdL7atTonzcE94jrtojpxLPyU4pQ6qsb477ldpfq5dTdAFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/758c0424e9.mp4?token=hKTs0I5lYTHGwBmrUP6PMAK5t2A1j6qcQV3Y5kaOOze8b9VCUoSgf6-PMIEiyqvxorT1kEt3a-VHo9zBzi4dGyZxMlAUpwmHufeRkQSqeaNedW-KJoggqWb-B7dNLnZ7M_3CKdTa-p3Ovrabr_aPFtWpqE3xO_uSvPIM0I5B7pmzpVVCXnKXKNwNd8y152TRQ4AyRfM8M5_s2XGe26r8Lf01oI1K2HvGFUGSSkKXzlV47cdyGyHIgJOCdAFOnpACZcVp96phv27vvWJGfv-eYvggUuzx6YmWEaUFR09kdL7atTonzcE94jrtojpxLPyU4pQ6qsb477ldpfq5dTdAFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حملات موشکی سپاه به پایگاه‌های «الازرق» و «موفق السلطی» به عنوان محل استقرار نظامیان آمریکا در اردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127038" target="_blank">📅 08:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127037">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وال استریت ژورنال: فشار نظامی آمریکا تا زمانی که ایران شرایط مورد نظر ترامپ را نپذیرد، افزایش خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127037" target="_blank">📅 08:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127036">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f4542baba.mp4?token=qehispqIVsLptsNE0MIKVjFg0QcQtJVQDkExtKFfsYk3abZzOkw9V6Hq18bF558Yv7LTty6UBTCvbYOmkBfA5rM-RCYc_qDKEy72Dn2I9TMlz5EXUxWq_4oOugAADDsub1KQ65eDkYgGw-eS9Mr_e1j9oS9_NMBa7DDls0a-cZO09xLVMm1w527udm74zQA3CL7SbMvrQzWlrG2KQV4mBYEJIm3PHQ_3xqyXtsfl653dWo5R49O02hHPzKBknaVRZ4kygOZwl_IdzzVKBhyn1fhVe5mcoOnpomqgHjg7bbCD_rNGQKLgKNmPkVtcOp8ihjjGQhDQ1aUZs_J0gulFcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f4542baba.mp4?token=qehispqIVsLptsNE0MIKVjFg0QcQtJVQDkExtKFfsYk3abZzOkw9V6Hq18bF558Yv7LTty6UBTCvbYOmkBfA5rM-RCYc_qDKEy72Dn2I9TMlz5EXUxWq_4oOugAADDsub1KQ65eDkYgGw-eS9Mr_e1j9oS9_NMBa7DDls0a-cZO09xLVMm1w527udm74zQA3CL7SbMvrQzWlrG2KQV4mBYEJIm3PHQ_3xqyXtsfl653dWo5R49O02hHPzKBknaVRZ4kygOZwl_IdzzVKBhyn1fhVe5mcoOnpomqgHjg7bbCD_rNGQKLgKNmPkVtcOp8ihjjGQhDQ1aUZs_J0gulFcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی پیش انفجار در نزدیکی سفارت آمریکا در بغداد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127036" target="_blank">📅 08:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127035">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6UY2AuTKOOANocFVXy8a8tviW-WkGHfCZzmermkFpsUeZk53HFxO2rUyb8hud81EqHQ45moOH5W5Yk6tAcyr04LM8VpmrMUYUonA6HQmmSqqO9Yn8t5Zia4Kzgig2MkjVF5jThAchju1VxaroeEtCpobE_Wq3fMuAG0Bra15z0Z89ij2E1LnNnkNx2VhFsLdOzN3Omz7bVld0iHdurUq2KFFFeDXeJyFjaLZH2xSuPPFJOzvvC1WcMWRGyrAed1jRojI7rWEpZ1fzMXYmFzSNcqsOgot34ZXdv4Ire-EAwwkXuxVkcCvjM0ofkZfZz2UOHnurdevJjKE30LwisP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سه هواپیمای سوخت‌رسان آمریکایی برفراز آسمان عربستان در حال فعالیت هستند، احتمالا برای پشتیبانی از گشت هوایی جنگنده‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127035" target="_blank">📅 08:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127034">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGWX1eAwZvEajoeA77Q_cGoDDpXpd4hRxpSzAZRJ1fLGWlaII9K0pwwN87c8NZ6GiemCam09eZn-klWSIXLnt2X7B0YnyXt6-pkxvcD3isA0ipWyl5h6sTH1SEWCt7jisogOCy2CUQxPj8EGrcc_kl0ARMVGKkpchcQ-G5jr58ROumFNQkRaYKEZdU5fHLTPmkZEfuYpZtZi8FNitnVk5gr5Gzp2Ziyv_12wU00A6urzt_zgYTdKvs0qxyCNrPsA_PKaCU3QOjV_LQi1Ikv_zwwFSJcz71ByYZd4yGDPqPf5dsjr28hIcwqD4yNap_EhPug67KuPQUNI0B1CQLVVeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ سخنگوی دولت به تهدیدات ترامپ: تهدید زیرساخت‌ها، تهدید زندگی مردم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127034" target="_blank">📅 08:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127033">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b0e7a0127.mp4?token=akmPzVJdE9e2qavLt6yn-_6r7EjKGwXtDEZHkKJuqLZsdiqx7pA_cnibP9CuWEMSG6qpLx4AtqTLRVPA55gWPsKfX1BRqAQmQDkQkx-tlfjWmSUgUMb5Zhi_C_SND9fpeH3_0x6QaqQve8qFVQEbTnAGUS4K5Pqn2VIndClHgxeoEHbPY_ej2tKN4kCfxc8g5EvUIO5kUJXmSsd_S72yFzv3EazHz_Kj1xN1bC5AiCjOBmwcyOUr_ylk-spEGhDwOWmePKma0FmDckbSENodh-WhJceVGcneuHyUkd4yPs2JPyVKNMGMvDHU3iNNK6eY8_AC-gaBBeE1i1pSs_My0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b0e7a0127.mp4?token=akmPzVJdE9e2qavLt6yn-_6r7EjKGwXtDEZHkKJuqLZsdiqx7pA_cnibP9CuWEMSG6qpLx4AtqTLRVPA55gWPsKfX1BRqAQmQDkQkx-tlfjWmSUgUMb5Zhi_C_SND9fpeH3_0x6QaqQve8qFVQEbTnAGUS4K5Pqn2VIndClHgxeoEHbPY_ej2tKN4kCfxc8g5EvUIO5kUJXmSsd_S72yFzv3EazHz_Kj1xN1bC5AiCjOBmwcyOUr_ylk-spEGhDwOWmePKma0FmDckbSENodh-WhJceVGcneuHyUkd4yPs2JPyVKNMGMvDHU3iNNK6eY8_AC-gaBBeE1i1pSs_My0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیک موشک از ناو جنگی مایکل مورفی ارتش آمریکا به سمت اهدافی در ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127033" target="_blank">📅 08:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127032">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4500df2fbe.mp4?token=GwiDgI6wiEHbIWPQAuai653yMKM2IDbDme_9RJUVOpBNc6S4btRMymIFqWAwJXQw3HiW4CaPBECyvE7sNkPBli_yyqTI8xkonqWa6VrBJc4Fk6W20tuNW1ytrVIh8PUlCGmw2btOXXCs9Zrfryf_t_trvLSDV0H0SZM9Yt9InaGYPHqfAOJqy_Z2JGBZ2Re23XHXEih1Ujsd7HnnvFu9xWI91BkMemrqhun4ttF8mcEjv1LPaY0LCw47YV0KyuUJzRA6Ed0i3JNOk9W__2bh6ZD0EHv4_6T93501Um0WygwxuMgp1tJe9QXGwQimgVJi3rhnd7wpZb9UFJsStI02Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4500df2fbe.mp4?token=GwiDgI6wiEHbIWPQAuai653yMKM2IDbDme_9RJUVOpBNc6S4btRMymIFqWAwJXQw3HiW4CaPBECyvE7sNkPBli_yyqTI8xkonqWa6VrBJc4Fk6W20tuNW1ytrVIh8PUlCGmw2btOXXCs9Zrfryf_t_trvLSDV0H0SZM9Yt9InaGYPHqfAOJqy_Z2JGBZ2Re23XHXEih1Ujsd7HnnvFu9xWI91BkMemrqhun4ttF8mcEjv1LPaY0LCw47YV0KyuUJzRA6Ed0i3JNOk9W__2bh6ZD0EHv4_6T93501Um0WygwxuMgp1tJe9QXGwQimgVJi3rhnd7wpZb9UFJsStI02Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گلوله‌باران توپخانه اسرائیل دیشب در نزدیکی بیمارستان دولتی در نبطیه، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127032" target="_blank">📅 08:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127031">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده(سنتکام) : ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی شده است که تنگه هرمز بسته شده است.
🔴
حقیقت: کشتی‌های تجاری امشب همچنان در حال تردد به داخل و خارج از تنگه هرمز هستند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/127031" target="_blank">📅 03:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127030">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rm41bJV40h5RPAqtCgopENdJ_KsGI7cekJcqpXqaO7Pr01Pdbc0lst2mzO5J0DCOES1YIDYlhjWx1aZD_EnCHXXwpWmpUQ4Ggs6UlPU7fV2yHlGGhQ60Y3YLDJj6lJMI27TpqarhZ4Qnjg9kv1IgNNYU7ecZ2XEkKpPJ84zWtjVfIVjJ3eR2XTFwraTQI2UrVT7TAAWb5OKp979dAlZ3GbRRfSTBZ6zhAQvw-FRXvKxvVWJwKKzMq0PNFzcPAQ3Ev6WrHDvsDjGQ9vnMrR0QCcJ6SgYSL7R82gkTQugF3DIpls8A7-pg7DRpHRF9ad7UD-emjHnS253P9mLh1Ypudg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده(سنتکام) :
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی شده است که تنگه هرمز بسته شده است.
🔴
حقیقت: کشتی‌های تجاری امشب همچنان در حال تردد به داخل و خارج از تنگه هرمز هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/127030" target="_blank">📅 03:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127029">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
صداوسیما: ترامپ بازم دروغ گفت و عقب نشینی کرد و ما پیروز شدیم، الله اکبر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/127029" target="_blank">📅 03:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127028">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ در گفتگو با فاکس نیوز:
آتش‌بس با ایران، نقض‌شده‌ترین و ناقض‌ترین آتش‌بس در تاریخ جهان بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/127028" target="_blank">📅 03:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127027">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز:
نیروهای آمریکایی ۴۹ موشک تاماهاوک شلیک کردند که به اهدافی در عمق خاک ایران اصابت کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/127027" target="_blank">📅 02:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127026">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ: اگر ایران توافقنامه رو امضا نکنه، فرداشب به بمباران آنها برمیگردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/127026" target="_blank">📅 02:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127025">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-IlvNmjLbCb_3GIupRsKRg3kj-tdiQ5qdoUnjAYzU0zuaE2gUPPAEJfRe6FxSIg6BUrXZuUJonZTJA0ltphyduLFgh_5EW_uZpcf-1bJrG2V3RW34aGWq_heisshQFbsK2duDdr7U1h_yjpmSGJ5xgoXY7UujcN0Ge_2Ls-TfqWqxTt3LBRdcSnEb7I__zVWKzOrw4q8p8NldaivguLOF6zzqgs02JpvztBhOXTPNM3dX2ilu2gyBvW398OrexHk_uRSgthkdaArEDhOX89BIku4vS6gW97u2mfa-wXVuKH5wbGz6FmT9_QEh4iribv2bk8_0KIF_JsEmgUpemRqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به فاکس : ایرانی‌ها ازم خواستن بمباران رو متوقف کنم
🔴
مستقیم با مقام‌های ایرانی صحبت کردم
🔴
جنگنده‌های آمریکا در حال پرواز روی آسمون ایران هستن
🔴
حملات هوایی به زودی تموم میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/alonews/127025" target="_blank">📅 02:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127024">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
هنوز هیچ حمله ای به‌ مواضع آمریکا صورت نگرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/127024" target="_blank">📅 02:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127023">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a20952ebaf.mp4?token=BuMGM629ba4-GbDnV5LRtBkjcfCZDr3W2H4ZZE3GxFhayDCinKqZ21_M6jj7igUHLp7cjt__vpOXoOBACtSOfV_-RH_8njCDGxpQ1ldKmm-5CN8AvOvSItZfjdCk1sDWrE-aeXnHJw9zLwa0Y37_v3YPr_WVKxp6FdgIBGC0uQnF92yDuzqgsyLrufnS6VQzw-y4HJXUX6C44LxlFHcuudq_MHn__Qra-pEo1BI60ChKa1TjdWjIydYxs4fAqOAeUEB--cX7D1pzIhR4Q0Iltobgm29gUHndRzmguMsqwY_vOzTWCA6yT97ocHJrtxA4PcIhnXCIm-UbKq2DA22SDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a20952ebaf.mp4?token=BuMGM629ba4-GbDnV5LRtBkjcfCZDr3W2H4ZZE3GxFhayDCinKqZ21_M6jj7igUHLp7cjt__vpOXoOBACtSOfV_-RH_8njCDGxpQ1ldKmm-5CN8AvOvSItZfjdCk1sDWrE-aeXnHJw9zLwa0Y37_v3YPr_WVKxp6FdgIBGC0uQnF92yDuzqgsyLrufnS6VQzw-y4HJXUX6C44LxlFHcuudq_MHn__Qra-pEo1BI60ChKa1TjdWjIydYxs4fAqOAeUEB--cX7D1pzIhR4Q0Iltobgm29gUHndRzmguMsqwY_vOzTWCA6yT97ocHJrtxA4PcIhnXCIm-UbKq2DA22SDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدای جنگنده های آمریکایی برفراز قشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/alonews/127023" target="_blank">📅 02:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127022">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
انفجار مجدد در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/alonews/127022" target="_blank">📅 02:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127021">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری/پاکستان: به آمریکا اعلام کردیم که دیگر دست از تلاش برای میانجیگری برمی‌داریم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/alonews/127021" target="_blank">📅 02:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127020">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlaatpSAlaxPlW_lXbX8aZUYBChcdC2zmewmFBeuoIiH8bCdJrjDeaCgBIWWoskXrQA36ovmwA_L09cStVGP1tfkYnfHK-VHTOteL3pFRQwr2CgI7DqkkuPNTxkqzNyoGUwfjTZiqS74C6wkcsjITgeIvpTCkhgowfjg-P0CkAj_-l72xQAtB7c6GLe_5gQo9x3eUAJWXkVhU-HtyVKPyumycvJTnbb2jhv4jBu7JlwhHjoKPn3ZuvuecLggJO8BDnbcVuZX1qQy0-euPlQDYqAKM9mNw6bGSs-uccYqeKL8eoLaNhEK7H_-is10u6rXgNIh-MjwFFrbYndIkvf0Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارشات اولیه از حملات هواپیمای جنگی A-10(گراز وحشی) آمریکا به قایق های تندرو سپاه در جزیره لارک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/alonews/127020" target="_blank">📅 02:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127019">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZoj_HVhXFAa8xUd61tnoDyFNjX2bUgRRaYr8dtWXHrAQvnKz1psQtvsKbp4144kvokc_yJMEYGC7Pm_QZT9Gde4tpAIhg3drvEI9nRhEKnlxZaUvJqLTPGQWnEuyA9vuG8eVZ7iEneLS0dEYCYnup0UVZTw_gFPSE17u0nc2vGdhiygqsp7mESpHJmNuCjIvdeCUnmaz4vmHlNpWHIWtJuPpBz1jXoPN1FHPeyo-Qp0cxra8zkEKMvSfwnu1552b5xygF_6WiJIEAAWS5lADWYikm6oOWzp8QofWSayRuFEiOfeyxAFniBB2IEPa8UyzF-l0BHu07JV2WcEpyR2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
اینترنت رو قطع کنید تا دیر نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/alonews/127019" target="_blank">📅 02:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127018">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aly-3PIFcVZVEoiCGbOTbj7mVhajqIY4Wxjo_NxKWypnnr9yr7pKTiYliRmWKfCVrPnoPEcjDU3zQQ4Hl8sOVUsOd8JA3apF9rUZBs3coOgqN4HL73plujh3dyKfFZMfSaGLxBsfj5MU0L2jS8MYoMf1A8mFSHjYXOtanTKxut-azurdq7qfq2GPMU_0QQDsfxxqPdxSARqbEB_FTnpRuNQP2xzK27g8abuAU6DScCx5hInyV30fVj44C3epVg22JHpUt4KLtfxN-vzXHpBNX9GfQQJbgfmRkiIPVzGgKjh5Z5TCieG5SdvNOFrjYcTZew4yTNohm41iTXSDp_3eqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیرنویس شبکه خبر
🔴
تنگه هرمز به صورت کامل مسدود شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/127018" target="_blank">📅 02:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127017">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
مقامات آمریکایی به وال استریت ژورنال گفتند که ترامپ دیپلماسی با ایران را رها نکرده است، اگرچه صبر او به طور فزاینده‌ای کاهش یافته است.
🔴
حتی پس از تأیید حملات جدید در اوایل این هفته، ترامپ به دستیارانش دستور داد پیامی را از طریق واسطه‌های قطری به تهران منتقل کنند که این حملات پاسخی به حادثه پهپاد است که تقریباً خدمه آپاچی را کشت، نه آغاز جنگ تمام‌عیار.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/127017" target="_blank">📅 02:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127016">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aDlDaU_v0ENcJ1P5PkUS_ulv1NplzA7J8_UClD3K0kAWMAHW1Qhd0OjxJyXCyisdQOo8PeapwrMk_T5F58XURI7bmwVb6f3aRvFfchOPv36lGta78u79fkRN8pBN3KyMXeRmxnSdcS7dXdErfeyM047T2iGQ9MWtcnAflGVVaDzw8_k0T16UQL5hncozBtUeKU6mfyf_qD_NnUtcEJUeIYv2mn60jJ3bEQioxX_-6HuoAVYZLkIeTTR_lKn2t0jz3Bzj6ta2QQucQYqRIppUCeBbN03qtG4ESVhCk_tpiaXF6UoEmOpyMs3SIjYfjFfcCcpM4AwcEiAMuRJkgkj4uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت آمریکا پس از حملات جدید نظامی آمریکا به جنوب ایران، به بالای ۹۲ دلار در هر بشکه رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/127016" target="_blank">📅 02:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127015">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhjAAP7reoPBKAKh6JB0W_2g7bh4a9GkM5trn6_P6NtIOB_2V87lSQenEfZSdBvbMDV6OYSUyswDAD0hhn6hoJMRdXtWfHGItiqQpIplkbhqsQnLpYkdcmdrnjECXwNLrYUtRo6hfpffnIssUQThve4zFmE57-dopJj3NYO3imuH6Y1XePpiBknbvGMOXE3p-mAJfc28MxWaMSp6doYAMJEU21qiQTOfZ2zNTOF78qnDC5lBMzficKRBH7ikfn02xO5X-c4lQH1zOA3R2BdKwa2AaXcIptQ6DIe4qn1eERGRoUIiR0MFOtHKWRQiBN465iQJb_ABwMgHXpK-rq5tRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی خبرنگار :
اگه آمریکا بخواد زیرساخت های مارو بزنه و بندازتمون توی بحران برق و بنزین ما هم کاری میکنیم که اسرائیل هم دچار این بحران بشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/127015" target="_blank">📅 02:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127014">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری/ قرارگاه خاتم الانبیا: تنگه هرمز از این لحظه برای تمام شناور ها بسته اعلام میشه و هیچ شناوری حق عبور نداره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/127014" target="_blank">📅 02:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127013">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/127013" target="_blank">📅 02:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127012">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Za8okkyx_JX7NvUsZytSiegutkS9CYOuTFUhxXqi46HguS1OJuftz-MjxpYaapjrCt1tlSwGxlHuYb7R04xM_rXipdKShzDYczGbcgU6YsqDYeJaeVfU8peH2_ayPQSk9fz02ivBcZac361NabQUlvicFlh84egPUey4-rG1tKCCPheQXqF1K11dxaT0e-P6VZlucD2Y5bWeXVHxS_RLmOfKD_X_rVNOn8jAkBgmAj9BzUF17cFkWc3heTua9e3AgM_0KwSgzqo4OyHHAwiXuXc4_TL6OaMhDaO8-Mu1r1f43VpEP610QoRSGby8rJubTL18f1zlCq61z-dwMEbp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۱۵ اسرائیل : موج اول حملات به ایران؛ به پایان رسیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/127012" target="_blank">📅 02:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127011">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری/فاکس نیوز: اهداف بعدی ترامپ ، نیروگاه ها و پل ها هستند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/alonews/127011" target="_blank">📅 01:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127010">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
انفجار مجدد در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/alonews/127010" target="_blank">📅 01:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127009">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
به گزارش آکسیوس، مذاکرات ایران و آمریکا به طور کامل فرو پاشید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/alonews/127009" target="_blank">📅 01:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127008">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نیویورک تایمز:
چشم‌انداز پیشرفت دیپلماتیک در مذاکرات آمریکا و ایران زمانی تیره‌تر شد که یک هیئت میانجی‌گر قطری عصر چهارشنبه بدون هیچ پیشرفتی در مذاکرات، تهران را ترک کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/alonews/127008" target="_blank">📅 01:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127007">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
گزارشات از تحرکات شدید در اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/alonews/127007" target="_blank">📅 01:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127006">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوووووووری/زود بیایید اینجا
⬇️
https://t.me/+4Sqp5RRoEUE5ZGM0
https://t.me/+4Sqp5RRoEUE5ZGM0</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/alonews/127006" target="_blank">📅 01:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127005">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فوری/فاکس نیوز به نقل از یک مقام ارشد آمریکایی: امشب چندین موج حمله دیگر نیز وجود دارد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/alonews/127005" target="_blank">📅 01:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127004">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری/فاکس نیوز به نقل از یک مقام ارشد آمریکایی:
امشب چندین موج حمله دیگر نیز وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/alonews/127004" target="_blank">📅 01:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127003">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
یه موشک خورده تو فرودگاه بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/alonews/127003" target="_blank">📅 01:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127002">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
صداوسیما:برخی منابع از رهگیری یک پرتابه کروز دشمن در عسلویه خبر می دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/127002" target="_blank">📅 01:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127001">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
یک مقام آمریکایی به Axios گفت: تمام اهدافی که مورد حمله قرار گرفتند در جنوب ایران هستند و شامل سامانه‌های پدافند هوایی، رادارها و واحدهای فرماندهی و کنترل پهپادها می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/alonews/127001" target="_blank">📅 01:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127000">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
اکسیوس به نقل از مقام‌های آمریکایی:
هدف از این حملات فشار بر تهران برای امضای توافقه، اما ممکنه به تشدید نظامی منجر بشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/127000" target="_blank">📅 01:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126999">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13dc5f5965.mp4?token=qXrgo9oMOZWr9O_0p9e55bi_T8wnb4mTZrkhvOKNSJjfF_XE_Mw84LyMFcbb4uJSDciUDOdNFrfBp286z7RFTkPMSS5PpCU5Tw8xtxU3xCPFcr_O0SiV4cFMi06k0HzMpIemNN6RrHwHj_0rzBykwjg9YgSWzkOZ135SHmO5lYcbGTLrnj41RWf7aI_-g0GDIjPpfLNtJrAJuc8FhsAfkTTpHlHv4DeolvSMHXxcf32eJZRhnCEA7ujHGBbkzlHH_HJPXpADbQo7Z8SBNRDdXTNsVm6wGkRwkNot7RE6Af3Luf0RrDLerfC6fJ5SNe79ix6zsemN9FsQlepqB-wzAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13dc5f5965.mp4?token=qXrgo9oMOZWr9O_0p9e55bi_T8wnb4mTZrkhvOKNSJjfF_XE_Mw84LyMFcbb4uJSDciUDOdNFrfBp286z7RFTkPMSS5PpCU5Tw8xtxU3xCPFcr_O0SiV4cFMi06k0HzMpIemNN6RrHwHj_0rzBykwjg9YgSWzkOZ135SHmO5lYcbGTLrnj41RWf7aI_-g0GDIjPpfLNtJrAJuc8FhsAfkTTpHlHv4DeolvSMHXxcf32eJZRhnCEA7ujHGBbkzlHH_HJPXpADbQo7Z8SBNRDdXTNsVm6wGkRwkNot7RE6Af3Luf0RrDLerfC6fJ5SNe79ix6zsemN9FsQlepqB-wzAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قدرتنمایی جنگنده‌های ارتش جمهوری اسلامی بر فراز تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/126999" target="_blank">📅 01:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126998">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
طبق گزارش‌ها، پایگاه نیروی دریایی کنگان برای چندمین بار هدف قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/alonews/126998" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126997">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
چندین انفجار در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/alonews/126997" target="_blank">📅 01:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126996">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده امروز ساعت ۵:۱۵ بعد از ظهر به وقت شرق آمریکا، به دستور فرمانده کل قوا، حملات دفاع شخصی بیشتری را علیه چندین هدف در ایران آغاز کردند. این حملات در پاسخ به تجاوز بی‌دلیل و مداوم ایران انجام می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/126996" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126995">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: ارتش آماده پیوستن به ایالات متحده در کارزار جدید علیه ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/alonews/126995" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126994">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فووووری و رسمی/حملات آمریکا شروع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/126994" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126993">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
پدافند عسلویه فعال شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/126993" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126992">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رسایی: اینترنت رو فورا قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/126992" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126991">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری/گزارش شلیک موشک از غرب کشور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/126991" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126989">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
خط ساحل جنوبی ایران زیر آتش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/126989" target="_blank">📅 00:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126988">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
انفجار مهیب در میناب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/alonews/126988" target="_blank">📅 00:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126987">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
گزارشات از انفجار های گسترده در برخی از شهر های جنوبی کشور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/alonews/126987" target="_blank">📅 00:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126985">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/126985" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126984">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/alonews/126984" target="_blank">📅 00:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126983">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری/انفجار در سیریک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/alonews/126983" target="_blank">📅 00:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126982">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوری/پدافند غرب تهران فعال شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/126982" target="_blank">📅 00:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126981">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
جنگنده‌های آمریکایی بر فراز عراق درحال پرواز هستن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/alonews/126981" target="_blank">📅 00:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126980">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
صدای انفجار در حوالی قشم شنیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/126980" target="_blank">📅 00:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126979">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
تسنیم:  ایران به ایالات متحده هشدار داده است که هرگونه اقدام نظامی جدید با پاسخ فوری و قوی روبرو خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/alonews/126979" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126977">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
گزارش‌ها از انفجار در کیش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/alonews/126977" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126976">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزیر دفاع آمریکا: ما از آتش‌بس برای توسعه اطلاعات و به‌روزرسانی بانک اهداف خود در ایران استفاده کردیم
🔴
بانک اهداف و قابلیت‌های فعلی ما بسیار فراتر از آن چیزی است که در آغاز عملیات خشم حماسی وجود داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/alonews/126976" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126975">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سفارت آمریکا در بغداد به تمام شهروندان آمریکایی در عراق هشدار فوری امنیتی صادر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/alonews/126975" target="_blank">📅 00:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126974">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری/ترور آلارم: شماره معکوس شروع شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/126974" target="_blank">📅 00:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126973">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a221ec730a.mp4?token=GQZELLLUCXBH-vFNSpZ8OJ0p3_AEW0z0zi-981hdBWKZglK3Vd8YY2ErfdpuKW2SpzWMXXErYq019DqijyQTkcTL1ekanFqMIVXQEu3jGk4b9vzZQNWQvBXBlr7_PQ6BVZ_YNNC5lKnxt7ohxjz_Z1ehkVqaY5R8xJWMZkibvlOekno4XY5ozNqD9kzhgEq2llvlE9mQIXvcIsQLiMfp9QHs0gEQ6QQcXLkCsGKihHG2AqSndwJthmkLuI382zJw3NOmJoeYTkH708A6eL7cN2QhqXcm7l_WMbSJQV9lPICjP2QCO06psp31dNX50Hdzs9Mj6O73QFpbMB7Mkwgk1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a221ec730a.mp4?token=GQZELLLUCXBH-vFNSpZ8OJ0p3_AEW0z0zi-981hdBWKZglK3Vd8YY2ErfdpuKW2SpzWMXXErYq019DqijyQTkcTL1ekanFqMIVXQEu3jGk4b9vzZQNWQvBXBlr7_PQ6BVZ_YNNC5lKnxt7ohxjz_Z1ehkVqaY5R8xJWMZkibvlOekno4XY5ozNqD9kzhgEq2llvlE9mQIXvcIsQLiMfp9QHs0gEQ6QQcXLkCsGKihHG2AqSndwJthmkLuI382zJw3NOmJoeYTkH708A6eL7cN2QhqXcm7l_WMbSJQV9lPICjP2QCO06psp31dNX50Hdzs9Mj6O73QFpbMB7Mkwgk1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگِستِ : تپ‌تپ بمب‌هایی که روی تأسیسات کلیدی ایران از طرف ایالات متحده فرود میاد
- و این به این خاطر نیست که ما بخوایم چیزی رو دوباره شروع کنیم که لازم نباشه شروعش کنیم؛
- بلکه چون وزارت جنگ آماده‌ست شرایط رو طوری تنظیم کنه که همون توافقی که رئیس‌جمهور ترامپ انتظار داره بهش برسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/alonews/126973" target="_blank">📅 00:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126972">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزیر دفاع آمریکا: ایران طرف ضعیف‌تر است و حمله‌ای که امروز یا فردا انجام خواهیم داد، قدرتمند خواهد بود.
🔴
تأسیسات کلیدی در ایران را بمباران خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/126972" target="_blank">📅 00:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126971">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزیر ارتباطات: از سرعت اینترنت راضی نیستم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/126971" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126970">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ادعای منبع پاکستانی به الحدث: ما امروز از امضای توافقنامه صلح، دور شده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/alonews/126970" target="_blank">📅 00:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126969">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2770689aa.mp4?token=aFmsJGHrmVwIP9wKAwhMi0guhJRLVz0mzzaU6FkKR7qAfN11xki8AXTCxmYsHb_xsDLt9eRw0UonDamQ24JR4erqvkK5LIyc_n2-i2sPlbqJbFtcz3uQNvVZKGvRjqL_6axZ396MxDJeLDuIo5UJoqLwcDpWWRsTiIN4SU0urkL-rUFYBa196lQylcJPazmHDdg-BEgcep8O4FBe5BJyfBEJcoKJ_pi-5pYVRa8iJGFGOXgDj3ZTrI81EF8XWQz0e03WiL8szWH_3PPzthn137ak0Sa3LOeEjQsHb7h0bypNmAwiERppoi0vD7-q-z7ghZdAlJz1KZeKopn9TVCAng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2770689aa.mp4?token=aFmsJGHrmVwIP9wKAwhMi0guhJRLVz0mzzaU6FkKR7qAfN11xki8AXTCxmYsHb_xsDLt9eRw0UonDamQ24JR4erqvkK5LIyc_n2-i2sPlbqJbFtcz3uQNvVZKGvRjqL_6axZ396MxDJeLDuIo5UJoqLwcDpWWRsTiIN4SU0urkL-rUFYBa196lQylcJPazmHDdg-BEgcep8O4FBe5BJyfBEJcoKJ_pi-5pYVRa8iJGFGOXgDj3ZTrI81EF8XWQz0e03WiL8szWH_3PPzthn137ak0Sa3LOeEjQsHb7h0bypNmAwiERppoi0vD7-q-z7ghZdAlJz1KZeKopn9TVCAng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ؛ هگِستِ : اونا قرار نیست به توافق برسن و ما هم با قدرت روشون فشار میاریم
🔴
سنتکام این کار رو خیلی خوب انجام می‌ده، بهتر از هر کسی تو دنیا، و ما هم همون نتیجه‌ای رو که می‌خوایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/alonews/126969" target="_blank">📅 00:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126968">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb62aa25a5.mp4?token=Y7XW_dyrOfnRUAMkV5erLVwlzhGaNblbwhZlc5qi72CrTgn7OKeSHef_YDmP5balyYIAQ8plRaQf-jL3pFSrFTxlIN1Es3prBQNHcgH6gaGLMLq59_mAqnsgNXnQB2JWt9qDjQeusgkSAk3n5Xs6tkOno-GXRk6PB0ES25JEal2T_AYXfXC6dIvibIT_HqvnKyfUjnw111Y4ITgzyZeEYsT-RwC3SYP6ULigICZUb7FXEX04eHzlLjzJtXg8QboEHWrNGqLqskg2aVS4Be06G_7njMOtq4GDECGuHe21MNFgRmCO5GxLSrcR0hgcgZWSuMtVEFLYrVwTWir4FluPzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb62aa25a5.mp4?token=Y7XW_dyrOfnRUAMkV5erLVwlzhGaNblbwhZlc5qi72CrTgn7OKeSHef_YDmP5balyYIAQ8plRaQf-jL3pFSrFTxlIN1Es3prBQNHcgH6gaGLMLq59_mAqnsgNXnQB2JWt9qDjQeusgkSAk3n5Xs6tkOno-GXRk6PB0ES25JEal2T_AYXfXC6dIvibIT_HqvnKyfUjnw111Y4ITgzyZeEYsT-RwC3SYP6ULigICZUb7FXEX04eHzlLjzJtXg8QboEHWrNGqLqskg2aVS4Be06G_7njMOtq4GDECGuHe21MNFgRmCO5GxLSrcR0hgcgZWSuMtVEFLYrVwTWir4FluPzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگِستِ خطاب به
سرباز‌های سنتکام
:  این به مأموریت مهمی که شروع کردین و هنوز دارین ادامه‌اش می‌دین؛
🔴
تا مطمئن شین ایران هیچ‌وقت به سلاح هسته‌ای نرسه، باید خیلی افتخار کنید به خودتون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/126968" target="_blank">📅 00:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126967">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
منابع ایرانی به الجزیره گفتند:
«هرگونه حمله منجر به پایان مذاکرات خواهد شد».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/126967" target="_blank">📅 23:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126966">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
اکسیوس: دو منبع آمریکایی گفتند: ترامپ بعدازظهر چهارشنبه جلسه‌ای در اتاق وضعیت (Situation Room) برگزار کرد تا درباره حملات احتمالی جدید علیه ایران بحث کند، این جلسه ساعاتی پس از آن برگزار شد که ترامپ به خبرنگاران گفته بود آمریکا «امروز دوباره به سختی به آنها حمله خواهد کرد».
🔴
منابع گفتند یکی از گزینه‌هایی که ترامپ در نظر دارد، انجام عملیاتی با مقیاس بزرگ ولی کوتاه‌مدت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/126966" target="_blank">📅 23:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126965">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
جی‌دی‌ونس در پاسخ به این سوال که آیا نتانیاهو در نحوه مدیریت رابطه خود با ایالات متحده درباره ایران اشتباهاتی داشته است یا نه گفت: «او قطعاً در برخی موارد اشتباه کرده است.»
🔴
ونس از ارائه نمونه خودداری کرد و گفت این گفت‌وگوها «بهتر است در محافل خصوصی باقی بمانند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/alonews/126965" target="_blank">📅 23:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126964">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
جی‌دی ونس: منافع ایالات متحده و اسرائیل همیشه با یکدیگر همسو نیستند؛ رابطه ترامپ با  نتانیاهو بر سر جنگ ایران تحت فشار قرار گرفته است.
🔴
گاهی ما [و اسرائیل] در یک مسیر و هم‌نظر هستیم و گاهی نیستیم. و هر جا که این دو از هم جدا شوند، ما، باید جانب مردم آمریکا را بگیریم، و همیشه همین کار را می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/126964" target="_blank">📅 23:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126963">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
آکسیوس: ترامپ در حال بررسی انجام عملیات نظامی جامع و سریع علیه ایران است.‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/126963" target="_blank">📅 23:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126962">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c5dfe9eb.mp4?token=K7IEv2_jpmp8LY0Th5MkoeQLrtWpE9hYiw2eR7KgVyYXhTzMJnpYLBhlTVY0HTYFDDtEN4V6PEYEDetvcs8FbOrKgHv9tPnDH7IPsr8KSQH1gZK5t3GaMDB1UCcP6sWVZwSCP2r9rtbyybzmpu_PHHkuu1xy716bDhCf-euwDG2X0ZPA2PsDORPCb6oTEhWcMcnudhIMRtKBSCIPVrSxBbTHQwuj98VPmu-rTb1-X3V-ewB0A1sQedWEsWI5bB7kFoa0xKh1mbWp-pqChZ0axK7dUBglmuCrnE8poi8EXdpzov2ZYU2Me519l8pf0klKwJbJIzbBVWgi-jJIhbij6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c5dfe9eb.mp4?token=K7IEv2_jpmp8LY0Th5MkoeQLrtWpE9hYiw2eR7KgVyYXhTzMJnpYLBhlTVY0HTYFDDtEN4V6PEYEDetvcs8FbOrKgHv9tPnDH7IPsr8KSQH1gZK5t3GaMDB1UCcP6sWVZwSCP2r9rtbyybzmpu_PHHkuu1xy716bDhCf-euwDG2X0ZPA2PsDORPCb6oTEhWcMcnudhIMRtKBSCIPVrSxBbTHQwuj98VPmu-rTb1-X3V-ewB0A1sQedWEsWI5bB7kFoa0xKh1mbWp-pqChZ0axK7dUBglmuCrnE8poi8EXdpzov2ZYU2Me519l8pf0klKwJbJIzbBVWgi-jJIhbij6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/ پیت هگست:
همانطور که رئیس‌جمهور ترامپ امروز گفت، آنها معامله نخواهند کرد، پس ما به شدت به آنها ضربه خواهیم زد. سنتکام این کار را بسیار خوب انجام می‌دهد، بهتر از هر کس دیگری در جهان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/alonews/126962" target="_blank">📅 23:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126961">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری/ترامپ : به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن ( یک ساعت و نیم دیگه )
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/126961" target="_blank">📅 23:41 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
