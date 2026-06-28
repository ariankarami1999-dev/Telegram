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
<img src="https://cdn4.telesco.pe/file/W-oWaIb1jQiQ9U1NbQ0XQ3kHN4Suo_Izf943MYsQlPD1Yx7tUcbv8Ikk6Jz2tzp1u7838oI1Sk2IpXwnpFd-UTYvArV-WM29fbP8NBCwBev4m5AUwX20TJQybLzdR9zbxpQIe-cEvqvaqr2FSl2psHJVgupUswUfbXgoaLg6TBFxrPzxW_ejWak72IkOwNzOhX9KCA7k-_HEHs9xPcjrA7PDKXILNAQ9NyYjvT18W3emOM7RpPpY5FWc8efvkAUEbvkpYYCBI-Z-s7V3B9miKNGFjhc4lPoOsZOovdtABCBsH2o3giZ8wuOt2nmXTz-OcYlOq94YZDrlZoMj1lv34w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 187K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 19:15:55</div>
<hr>

<div class="tg-post" id="msg-78994">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pncOUK2r-cbCs8j23i0u9j-vXABV1PDabbmnADiLnSRMw6RblowX8Kdvw1yF9R0mIrO942aGNtEB2tlE9U9NzwOHvdGkNmEkHWzgoPMh7hr_WaXDGPBKTXbMQWLUkn6vwpShgzebLOQQput5iRaUzEznymx6G3VgfH1AbyBdq8y4258iQI4LyLBo6LkFWOJ8oYyD1m9PDNpyxapwefU_2riUE4OYSe8j1iRCQJHi5aJQzNV8ugLSoMUXPfJ1jmDh6YLYBlcGTfv6hb2MPDHtTNGvafLxVp78MkXgey_4Niwa1KV-2C7QGhX3_i1iPZw-BfRGm-7vbr3jnoDNhHdd3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب تکست کصشری داره ترک جدید پوری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/funhiphop/78994" target="_blank">📅 18:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78993">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-YVSj6gsbnp__vNiuyYYLArn3ARn8bRLADZ18QINDGFKUyRvs3_UTBMM0EytlVsIx1CSGyBMAE-7qEmOzF-D8OrPd8kUv9F_Hoy3LhckjtxEgarPD--cnso107C4oF6TBaZhCEXgerdRjsGyTDm18QM_uoGMk2wRwvn7mxf_e2D40A2QIHU91N2r-2MZKSvn0zwtzHAcZM5C3NP9ZUwwFoSPdpV5iyEzAXf0lSYC_ca6j-iJzNllFHZvn4LlC6gSusnK-bQO_LOHFzFg71lIPWZPXH2bd3pSpL4CE7sWfBTWDRX1PvrZijKxnBIW6Yv9AJfo53DEgNgMoEHflpV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید گوگل و تبریک صعود به مصر :
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/funhiphop/78993" target="_blank">📅 18:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78992">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">RitzoBet.apk</div>
  <div class="tg-doc-extra">53 MB</div>
</div>
<a href="https://t.me/funhiphop/78992" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
#شرطبندی
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/funhiphop/78992" target="_blank">📅 18:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78991">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKgLKHmWOkqCjyicvPRTXZcCRf1HFfAopvxdmyukkqudibwW-JoVMTRCAJCmp1TrnHBCWIyGmBJrQ8GC9miyY6cdJOy338LwOvqNlGtdskQ35d2K2_Pze_wd_7b5D-8A91uue4DkZr5Efch34BSjoD3RhjptHX92dxvca9ZtRYt8o-n_uMfN-YCy_wzZlrLNYgYY-3ikXeUC8dVCpoFViLfUnwidknRSxstElFDmRJZKxrVSLf6CrgezabdqYZKcK2PXxxMk-Bf-xecX_DGHadx1lhbnb35-ejwDdPe1z78_ZmErH_25ipdxuX9tVolrvI5hkrTdlVciYAyECh9kJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ادامه هیجان جام جهانی ۲۰۲۶ در ریتزوبت
🔥
⚽️
برزیل
🇧🇷
- ژاپن
🇯🇵
⚽️
آلمان
🇩🇪
- پاراگوئه
🇵🇾
⚽️
هلند
🇳🇱
- مراکش
🇲🇦
🌍
سه دیدار جذاب، سه نبرد حساس و فرصتی عالی برای ثبت پیش‌بینی‌های هیجان‌انگیز!
🎯
دانلود اپلیکیشن بدون فیلتر اندروید
🎯
لینک ورود به ریتزوبت
💎
امکان شارژ حساب با کریپتو ، انواع ووچر و کارت بانکی.
✅
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی جام جهانی 2026
G7
🅰
🆔
@RitzoBet_ir</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/funhiphop/78991" target="_blank">📅 18:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78990">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tP5SI1lDSS3Z_zCquetUvg8lSfMknk8IgLraPl7Wj_fLXmMXl8C7Q9iz5QT0jWwu0iuOuxiFGUplke7YmJwsH_Jy_Vt72jEdGwc6XmCa7nFnzxaRgTcCnJD7E1fFPRaP99JFNhPwLzFhXhTThjEmA8XLDk6Dp5k-COE-A9DIUCIbUD4L5Cr_xHSuPrANk9qSFN_frtxRVn-JLaDWfD9bTlrnkpk7hXFK4h3-SOm_KN-Vi4hn5XN2KVPLOv03jQwDQ8oQcoX_g0S9xWYnFQLQ7aIv76ub6RGnoHEropBtjmuR6loXdUcTyCi5GEZi_wQtaG54e4h3ePhPNpyEPdR7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری کوروش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/funhiphop/78990" target="_blank">📅 16:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78989">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ایران توی جام‌جهانی : ۳ بازی انجام داد، با ۳ مساوی ۳ امتیاز گرفت، ۳ گل زد، ۳ گل خورد، ۳ گل آفساید زد، ۳ تیرک زد، رتبه ۳‌ گروه شد، بازی ها از شبکه ۳ پخش شد و برای صعود باید منتظر ۳ بازی آینده بود و در نهایت با تساوی ۳ بر ۳ الجزایر و اتریش حذف شد  @FunHipHop…</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/funhiphop/78989" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78987">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTDSLs9OErkEwS_16p3ZmZkb3nXEbMP72lT_ORmouReOakZEXW2YHbl7KOWG2IfWVGIpG9IukK4Nwuf1GT4YuIwbP8Z8FEjzLRKMNaAaYgTpz3LOSeetXFby-v3lxlV-MnJRzRauSx5SGe3Ob7SgxszWcOTQ8kHqn6sN9tNhZcSW4wWA9dHUQiBaJ0gBuco21kbAZN4TkB1XMn4XFrrAroiwyCB_fMo6tQ_jpXAQeJYErzSOEkXGHNa1MHcPeyVcnnMswh3mLAV3TPOugd9YablNHy2zKmM2wNl9XecqhAwKhKhk5BuzYsEQ1x3asuC6Nq7zJL0Zx3WCTgGZwX-HvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز خبر اومد که رئیس‌جمهور عراق یهو زده به سیم آخر.
یه شِبه کودتا کرده و با لشکر کشی و تانک و... حدودا ۱۵ تا ۲۰ نفر از وزرا و نماینده‌های مجلس عراق که اکثرا حامی حشدالشعبی بودن رو دستگیر کرده.
با خودم فکر کردم که یعنی چی می‌تونه عامل این اتفاقات یهویی و غیر منتظره باشه تا اینکه با این خبر شاهکار روبه‌رو شدم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78987" target="_blank">📅 15:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78986">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm49WzfS6ClAYOjKfWUA9DxOONoZzw4v7Ft7_cWcJ_BO_itS2pIFLSmHLkA9cSWRT168ZonqFHDXTApH3gmOp12kDqGblWI5SYPwyuUlwapgdhrrElUn9A0Db5wgKLfLh_2TjjYlBDyjJnpHEjft-Km1fsxdrboyUWj_YiaSUu-a3rBDlvmtH4QM2fHeKc9hVD_KJ5BKX-JJIrlIqgwzpOrKs8k33beFLPHLkL4WQdGJeaW0qmzsO4ypneUKw8NoTcK7ZrB1K0_rR5dUM6xGplKBeQu0CoQnROQvHgvBDAlyK23ygZ0aOiZpqtM2Xd6b8NE1Tq5P3L072DXGFFb-RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری میثم پیرفلک پدر کیان پیرفلک عزیز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78986" target="_blank">📅 14:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78985">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1wDyK_bzi88r-vMYKA_WKAODW88A36EcHhEM14kKm9DoWAOFlkjVP0gcrDOaQu46ipLZ2SZTIFC3MCCUR8GtFTpZQsEuRJpAx4fx4ZIlKE-_E6jQxuh4BoTSgpsvzHBTMAh_JBGMgf-fvY7GcwXyoWmUwnfHpeqYCarCIIpjKqz2S93oJm1mAMBvcM6iqX_aE1GP8ZoouVjs6daxZXqfD3sr6op-XIhb79bJaS6jcVEUCpdb9qaBnKUfH9Mz_3t2m0pYrZG6XIxEqxS2FGtF7UncO_mpqb6q4_nKv-FnGgfz_j4rpn845btCQg4rfRVPI8tLLkkovuKnHID9Jg9ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیل زاده ببین کاراتو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78985" target="_blank">📅 14:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78984">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cac12d8a3.mp4?token=n8Fi8yLTJ5Jv5Nba-2ETxiRqhnsJHtxf3R_qKh7CRDLH2vr5aoz1empIyY8K6vB1cVlKMWxM5jYJpR66UrqwxWOmxhOebZI3cZUiFiF6fylfwQ-FaBiR5pPhuswIayQaFAqjVo0DjwHvs2EKF8e37rQENJbGjahEvUNtcSzWIqzuoKdsBAQeBo3UOaaCDUl1V4Hx_0rWIPHy2mCeEYl-W8r59fxZY1Lgs4gre4cHFeLK58Mx0_4kyMABlHjFLJlWFr6UIP60WSUnLglhJWstCNrr3UruOjWLs4_jpYiKCDaGH0bwDM6gyq3WuHykmPajn8r4fkfL0QHS8P6LURKKzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cac12d8a3.mp4?token=n8Fi8yLTJ5Jv5Nba-2ETxiRqhnsJHtxf3R_qKh7CRDLH2vr5aoz1empIyY8K6vB1cVlKMWxM5jYJpR66UrqwxWOmxhOebZI3cZUiFiF6fylfwQ-FaBiR5pPhuswIayQaFAqjVo0DjwHvs2EKF8e37rQENJbGjahEvUNtcSzWIqzuoKdsBAQeBo3UOaaCDUl1V4Hx_0rWIPHy2mCeEYl-W8r59fxZY1Lgs4gre4cHFeLK58Mx0_4kyMABlHjFLJlWFr6UIP60WSUnLglhJWstCNrr3UruOjWLs4_jpYiKCDaGH0bwDM6gyq3WuHykmPajn8r4fkfL0QHS8P6LURKKzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت هتل تیم فوتبال جمهوری اسلامی بعد گل سوم الجزایر
🤣
🤣
🤣
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78984" target="_blank">📅 14:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78983">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">"من برگشتم" رونالدو مثل "من اومدم که نرم" یلس نشه صلوات
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78983" target="_blank">📅 14:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78982">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">جدی چرا چیزی از ارزش هامون کم نمیشه هیچوقت، مگه چقد گرونیم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78982" target="_blank">📅 13:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78981">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">قایدی زن جنده تو که قرار بود یه دقیقه هم بازی نکنی همون نمیرفتی نمیریدی به محبوبیتت دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78981" target="_blank">📅 13:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78980">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اوووووو رامین رضاییان اووووو رامین رضاییان</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78980" target="_blank">📅 12:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78979">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-LeQTdPjU6yfkkjc3cQispa-YzR1RciA6hBKakqnxML2lePocBlVNXeVqAwUvifS8IcyQ_okf9abf5ef5pP4NsGmT265bmzE-SNoYKUe39Meqmq0KfEt8Wkcju7FESzIuXnQkFLUB0Le5UakJ6RrlZ_RChW6d2mv15bLiqq_s8IXnIFRR5UryeRV37MYgwbwWl94OSXjTKCvdXjbgkNhPa-WT08gFiKiSO-iQovnFi0rx5be5EZJhriatvCQdu9fHzrhkO4rvUyfo2f5BQ3NAA9cU3nCXOGwyffOR-ELzoamLRTKmkYXXHPZJtrA0D9dny5vn4tXqs4x9_8tH6KKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند: مسی هیچ‌وقت قرار نیست بذاره من کفش طلای جام جهانی رو لمس کنم
😭
😭
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78979" target="_blank">📅 11:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78978">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سنگال با دو باخت صعود کرد، ایران بدون باخت سقوط</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78978" target="_blank">📅 11:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78977">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">همه دارن خط حمله های آرژانتین و فرانسه رو مقایسه میکنن، ولی بنظر من کلید بازی دست انزو فرناندز و مک آلیستره</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78977" target="_blank">📅 11:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78976">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVwN_qJRjxzoCDFIDP8DSLtEPQ8WbpfxpRjD-xm09nrqOZ4CKUtf_Kduhsuu-bcQGyqU5Q0xwpTe-U6NoJLaklUyqghuNn_Eq-a6LYzNAGEk_lqeG5ZUVyzx49T8HKv2iJCdTsqAJ3aGlLHmous-7UkDhGCwvmiLeXu-yZGtRKfE893wp-bZZ9w9BBYmzL9BQvElxFXKzye28DVSAOBHC1NFQXam4VjuLnOZQSQQNkBMiWBWwX7R_jpAhlHmWkgzTCRQcP36-oWrxPCDZKyvg0gis1a2AcMTH3bGpu-jCDv85RsNHmakPjeHcmh4YvaZJ1iSIdPlg7r8BMCS70bIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا خود فیفا هم نمیتونس همچین مسیری تا نیمه نهایی برا یه تیم بچینه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78976" target="_blank">📅 11:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78975">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هفته دیگه قلعه نویی میاد برنامه می‌ثاقی میگه فودباله دیگه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78975" target="_blank">📅 10:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78974">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0E4vxo5VKDFpdxY5psI-t2FA_WdT_Uxd93uHeaEOFIJfpx6_q_YE1JjahHsU2sJnTc1MhYkvzZ230VrISdL_d5zdENfxzHLEXMXthYZc_ItjUY9Iy4nahXakN_r9-n0me5MD2jn2-RSpFZj9nZSYmC4si5ygk3TEUqFA1DuYtk_tbtzVQS8BoGOdNfiWDUNPFkhWlV1ObjDnttcwQpAFW37EObo7z7T3SJ1NF7DjJwrUuvNcUPmshaHL1p7CH30gd1dh4GCDMPjz_B1XIf3xFiabAEekrd29lgIROJTaatnbYnU1_IlKFjWLC2SrwKlPVRcGku0---eHraF-gb4ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب یک بار دیگه پروردگار و اسطوره بی همتای فوتبال جهان، حضرت لیونل آندرس مسی نشون داد کت تن کیه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78974" target="_blank">📅 10:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78973">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78973" target="_blank">📅 10:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78972">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_GOD2ytJo6lZmlOHkKfl7kIdaFNM_RSw7A3-_dNgk5JGsdWDGdh4wJ2FH2-SS4uQxA_eidOZ64UXAKpa1JuxUWaZN2EWtgyVvuAeEwKxUhKju9n4A1Qd9504fE-fe8-mcO2VFXjLBAcEmqPR78nDpD4DV68mpPUPlIlQ_X6_y8W96ummp2gAb60r2mmXmsvkYrrdLh9yFeM1oBkrkTHMBonxBfhR12N7IjPjL3nslzASVHpViwm-sR1rkRCQgpksrRx2Z_VuYFDudmkI37tFNgPGIroCcxNYnc6lqELkUTMOvSbbNt3W3sj5eB9VFhzSaYFtbGAKEClBhaX8yoLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران توی جام‌جهانی : ۳ بازی انجام داد، با ۳ مساوی ۳ امتیاز گرفت، ۳ گل زد، ۳ گل خورد، ۳ گل آفساید زد، ۳ تیرک زد، رتبه ۳‌ گروه شد، بازی ها از شبکه ۳ پخش شد و برای صعود باید منتظر ۳ بازی آینده بود و در نهایت با تساوی ۳ بر ۳ الجزایر و اتریش حذف شد
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78972" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78971">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">RitzoBet.apk</div>
  <div class="tg-doc-extra">53 MB</div>
</div>
<a href="https://t.me/funhiphop/78971" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
#شرطبندی
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78971" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78970">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaSCDQngI2iQpzfEJe8KeuJZ18BeDzQCfOTun1B191eG-MMlmJBBQr2KmcGpod7LjBfkEC74rC7159OJVSbCI52GTN3beLFzn1fgBTxIUB7anXh5Qd_nBIIggTGTc3GMHeq_X7GP-z9HcTf5M59D_CmsCtHaaKYHQR1529qgTiSXGrcI6RgE4OrF9WnM4qUb7ORAJ0uCKSZlduX8iXExSLIjdSPUMjw045O2mVVS_ztx_rNpMuqEOh5Y8hOmW_781iDTLweqJw3EMV-c_QCGIY6CSLmooF67Vm_nlmPXi8FGdos-Ao0KioJQYqtTG4TDibSJ3ikEAIE2aqkkTBpwhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
می‌دونستین توی
ریتزوبت
هرکی شرط‌بندی کنه، هر هفته بین
500.000 تومن تا 100.000.000 تومان
پروموکد می‌گیره
‼️
💰
باحالیش اینجاست که فرقی نداره شرطت ببره یا ببازه، تو هر صورت پروموکد بهت میدن
🔥
🎯
دانلود اپلیکیشن بدون فیلتر اندروید
🎯
لینک ورود به ریتزوبت
💎
امکان شارژ حساب با کریپتو ، انواع ووچر و کارت بانکی.
✅
R7
🅰
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی جام جهانی 2026
🆔
@RitzoBet_ir</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78970" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78966">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سلام بچه ها من تازه بیدار شدم، بازی ایران سوییس چه روزیه و ساعت چنده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78966" target="_blank">📅 09:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78965">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">با ریدمان پرتغال جلوی کلمبیا، پرتغال، کرواسی، اسپانیا، مراکش، فرانسه، آلمان، هلند و بلژیک همه رفتن یک سمت جدول حذفی</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78965" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78963">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lR2FqiWUXi38wH2we6IYJwKvxS-fVcLC8RD87kamBQ1LSBdSiBoHVWc8ZBaqRQHQZvqiAWszVAA0YepZpyQR9OXqk2s8Ke-e7kG-kz-hYqNJqfMZ1WXM8HtCLxR8dyl9wdjq4itGC4XV9wtKxCL_dF8Jtmybc6ZNAQxyWIdqFSM1yNtAzbn6dffJUnJ5c6vFuQr6FKdPbdOypmKz8q24hgRpFQJVe-8vwFcfOAp-Yjpa-Vjf7ds9KLEAfCWXYgdq9uELsrg3ED0cBxkvKCUTmKRjYoaM-bgbX6MntDqX8tP4VU46s61roMmwrFCsyOG_zjxhW7s2jGT8FwHUIp-lGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N5OLgTBS-qKM1w6RJhUpzgCEAHMlOMyxEzZ2p-omWXQByldSD_UOAwG16bHMRPjP6RSWUp-q08Q427_ooKwlWHOk-t5qmNHJKIghwbsesh_n5aKu_bhqvsfdMa0c1K7yXg4VT4XSLdhER2PoAZQpN2ZWUUsdrdSfwLIuWN9hi-gVgofldReynhBuADLF6qUZyj_IWSRzCsi-3dM9pU_zRP-8GGB7oHyQPvaOGUemUPg8W98yVf1bD2N0YqI8VaYpvDYSIk64W3l9ZRo-bHFh6_wpm7YcBIbbn0rmaFItad0eG9IwAZfRpzX4fhLDKpocj20O0K5EXTtVZQRVkSCXlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من برگشتم !</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78963" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78962">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgTuHHKNmzJalfMYjtW9o-Pn-mSyjLBxj0YezwdbPFG6vMwbAUQiQjg8xN8aW9g_rtktBvQFSIDamWnGpgdpfmsRDXKGzYbumorn8fXJ1EyWGtp77ayZ6dM3IkiogeDcOaztu7e45Rbr1LljGIGvsqdgRlIBG01cgzyR2gYQ7mrAqtNT8SNhWYspslYHoBZpMksZvJ9wKxvHwcbb_RCnsqm20Vv7XKxSjzjPj18e857kz2_Wm0oXkBQvvCwxMmJKHv6gw36Onfr1v_cltIG4AxuT0YGeUa2xnHszDhUAkKRSwSeB5FyveNB8otVM6Dyqx2prFTpNHVXTUrnefXjvVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78962" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78961">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">احتمالا نیمه نهایی انگلیس آرژانتین و فرانسه اسپانیا ببینیم</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78961" target="_blank">📅 07:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78960">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa8b89a24.mp4?token=APkgS-lOBBKlDpVF0StlY0RT85RDg18IfokeZdHJ5J2eciHhgkvasWQGbnOA4n_xww9kF-RZlZOZX3787zfLQwjWUsJHcPYh1KWgYmcvhc--WVediBOn3wImgMSfdgx7cGA3U0qc13WqPFiby0myK3HzFoAUtDvgYozSiN6PkM0tKBzRSstEpRUTaAen2uI5q5U41LzkMgHEl5VBDQ7m5bBKFUSG5s6JtKlxAb3J7uDruUcpv3tbkGfq5nV1TaUlPcHm0_IoPjF0THdl0MLd7BjTZCT3qwXLYsYoZCxlMy1Mim46EjO04jxqZMAXG6V9wrMoi18L4xPFAobDbeMSfoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa8b89a24.mp4?token=APkgS-lOBBKlDpVF0StlY0RT85RDg18IfokeZdHJ5J2eciHhgkvasWQGbnOA4n_xww9kF-RZlZOZX3787zfLQwjWUsJHcPYh1KWgYmcvhc--WVediBOn3wImgMSfdgx7cGA3U0qc13WqPFiby0myK3HzFoAUtDvgYozSiN6PkM0tKBzRSstEpRUTaAen2uI5q5U41LzkMgHEl5VBDQ7m5bBKFUSG5s6JtKlxAb3J7uDruUcpv3tbkGfq5nV1TaUlPcHm0_IoPjF0THdl0MLd7BjTZCT3qwXLYsYoZCxlMy1Mim46EjO04jxqZMAXG6V9wrMoi18L4xPFAobDbeMSfoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگری که میگفتی عزت اللهی رو برای بازی بعدی از دست دادیم، بیشتر از همه به تو خندیدم حال ندارم اموجی خنده بزارم</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78960" target="_blank">📅 07:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78959">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یچی میگم نخندید،
تیمِ رنک ۲۰ فیفا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78959" target="_blank">📅 07:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78958">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارشگری که میگفتی عزت اللهی رو برای بازی بعدی از دست دادیم، بیشتر از همه به تو خندیدم حال ندارم اموجی خنده بزارم</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78958" target="_blank">📅 07:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78957">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi8wRAyF1X07wTviqSSZQHa73nfxzxIW6koiJ3uVo9PjH51uefwnd_oBhtcRcIJ3Fe-4NVqyDH8FR9Xf92DE6OwZwt3UgsQvDM0_2gYkr6FOt2tNggnjd_A8ZiUdxMO4ukPbEpI5JYPxKcdzZqmH2vO06H5rW53IAwZf8ja8J4PHPbP-wNEf8B6eOt3ANGWO8fCw3Y4gfEx_5iluzaCFRM9tDFsAKpGQqvabDB2kfzieqzrBoUS1SEproajJwzPc3WKoZjpzOBrGxNQEIL5OOA7nS2LMuZxTDLbXfmYTuURuHZNFnya41Oh3CmaiCYcsYEC-Xzrhdh4IpoDPBPjYgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی داش چیا رو که از دست ندادی
😂</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78957" target="_blank">📅 07:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78956">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">صبح بخیر</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78956" target="_blank">📅 07:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78955">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ژنرال خارکصه تو چقدر گناه کردی مگه خدا هم نمیخواد تیمت صعود کنه</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78955" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78954">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">عجب سوپری زد اتریش</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78954" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78953">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یکی ژنرال رو نجات بدههههههههه</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78953" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78952">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وااااااایییییی</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78952" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78951">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ژنرال صعود کرد</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78951" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78950">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اتریشششششش حذف شددددد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78950" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78949">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تاااااااسسسسسسس سومممممممم</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78949" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78948">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تاااااسسسسسس سوممممممم</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78948" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78947">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78947" target="_blank">📅 07:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78946">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">این وسط یه چند تا آژیر و صدای انفجار هم تو کویت و بحرین شنیده شد که چیز خاصی نیست احتمالا حملات پهپادی سپاه به کارخونه‌های پرچم کرنر سازی بوده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78946" target="_blank">📅 07:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78945">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حضور ۵ دقیقه‌ای ژنرال در دور حذفی باز هم لغو شد.
💔
گل دوم برای نماینده‌ی رژیم صهیونسیتی در جام جهانی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78945" target="_blank">📅 06:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78944">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گل دوم برای تیم دوم ژنرال</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78944" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78943">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نمیدونم چرا اینقد بدشانسیم
۱ بار ۲ بار ۳ بار ۴ بار ۵ بار</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78943" target="_blank">📅 06:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78941">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پایان نیمه اول
خلاصه:
ژنرال ۱۵ دقیقه در دور حذفی حضور پیدا کرد ولی در ادامه به واسطه تبانی پرچم کرنر با رژیم صهیونسیتی این حضور لغو شد.
💔
#پرچم_کرنر_۲۵_سال_آینده_را_نخواهد_دید
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78941" target="_blank">📅 06:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78940">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">عجب چیزی زد بازیکن الجزایر</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78940" target="_blank">📅 06:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78939">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اتریش ناخواسته گل زد</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78939" target="_blank">📅 05:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78938">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">این همه تلاش اتریش و الجزایر برا وقت تلف کردن و زدن توپ به در و دیوار دیگه صرفا از سر تاکتیک برا مساوی کردن نیست؛ انگار با ژنرال مشکل شخصی دارن بی‌وجودا...
💔
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78938" target="_blank">📅 05:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78937">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یادش بخیر مانوک خدابخشیان ۱۲ سال پیش خیلی دقیق این روزا رو پیش‌بینی کرد و گفت یه ژنرال با سه تا تاس بازی می‌کنه...  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78937" target="_blank">📅 05:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78936">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کنگو هم ازبکستان رو برد الان فقط میمونه بازی اتریش و الجزایر  این بازی مساوی شه تیم ملی جمهوری اسلامی صعود نمیکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78936" target="_blank">📅 05:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78935">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78935" target="_blank">📅 05:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78933">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeBjRQMtxUcvBmCJU0X0wx-oCn3U_RoSC703RCstccSdJ0OtGIkdChxVyunQE3AK8xLabB8lj1eAv6oPEuqzkY3Z88YyVmwlc3VaN0QpxFCV6ZPNVed9JStx0Zm6MeJf3H-imJgpo2MOFJzpgK3qTDNlVHc89yr_Nn3Y1fHw5xIKbcUMmLryKAAaHN-ZrStiG1jsM6JaBkdox0JALz8Mn5_GRWCQkqHxTdWcMSJ4yK-EcXoZh_-NI8f4vtFQScLCQo7p5c3UHVtI4NllYNV1Dq-Ah9J_8uK9ZhM4Z8YNk9u5Y0gPUFxjD1Q4sa3UrAPwoxRRQmIfz2EN7aralCavYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
اگر این وضع ادامه پیدا کند، ممکن است زمانی برسد که ما دیگر نتوانیم منطقی باشیم، و مجبور شویم کاری را که بسیار موفقیت‌آمیز شروع کردیم را با روش نظامی به پایان برسانیم.
اگر چنین اتفاقی بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78933" target="_blank">📅 05:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78932">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">چیشد پس جادوگر مادرجنده</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78932" target="_blank">📅 02:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78931">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">طبق تحلیل من آمریکا دوباره مخفیانه داره کشتی هارو اسکورت میکنه ک از تنگه هرمز رد یشن
جالبه بعد از تهدید های سپاه قیمت نفت هیچ تغییر خاصی نکرده و این نشون میده که همه چیز تحت کنترل ترامپه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78931" target="_blank">📅 01:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78930">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سلام فرید جان وقتت بخیر
ما بندر لنگه هستیم اینجا چند بار صدای انفجار بلند اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78930" target="_blank">📅 01:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78929">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78929" target="_blank">📅 01:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78928">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ2hiHxd8_a8j7GaK_C8eLHIGHeTf99nGJ695d6Wrmt7ya_7CtSwA8OhNSLU6MSfJFUl2f_mNplaqJ-JuhnYkYrwTUplC4G9kFiFZEHwP4RY8TYkvpq8ggjFuiwZQx27R6Fc8QMY3sXocMc-LclkBt51ii9unaZhRH4nGn_tKLLVLL_VHVPkZMbVW2VEbEIUM1usSoyp35yCIedZ7HEErCRavWfLuNMCrLSoaeqtEohzrKJM6IgaGDtaxVO5DYkjBQQu7HVQvC5DbLcItQBXjfRjbmbK-okGXUvrU3WSevZHd54IzBLUfO__UvARr2c-N4ELRZfv8NMs2Bx7S8tfXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مودریچ چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78928" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78927">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نگران نباشید دوستان، ذراتا دارن تبدیل به پاپ کورن میشن برا همین سیریک صدا انفجار میاد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78927" target="_blank">📅 01:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78926">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مودریچ چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78926" target="_blank">📅 00:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78925">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کیروش گفته امشب میریم کرواسی رو برا ایران ببریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78925" target="_blank">📅 23:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78923">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43122e124.mp4?token=pogFcL2lvTzhRkFXNFGISDrQjUzYxe0Y-COvLJVT_W88qK7Jg-6ithvSlsAAKzXFqW4kaPECASbCbXahRvJsUXI81iro4WldkzgSvmSeIWyf8drKwzV-S_ahPeZ1al-PylmATLJ5mqXphHp2ZmmYRn13QxUtLplky29VJPX-FzXD94HjVUYYDIhh8ppQGyjQZH8DyIUXZ4TIURYECHEswj-chW2HqRBPp9doj3IoUJ-j1ptpfZzP2AJp4nh4bs4jjAAR8Qmw3Bbjd23eJN5r3MDCind9V7H4Hq1vegnArNPOTTDgN1l4_eNrVTxcDucWYoVMOj9sl1LLlttWXHZ_iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43122e124.mp4?token=pogFcL2lvTzhRkFXNFGISDrQjUzYxe0Y-COvLJVT_W88qK7Jg-6ithvSlsAAKzXFqW4kaPECASbCbXahRvJsUXI81iro4WldkzgSvmSeIWyf8drKwzV-S_ahPeZ1al-PylmATLJ5mqXphHp2ZmmYRn13QxUtLplky29VJPX-FzXD94HjVUYYDIhh8ppQGyjQZH8DyIUXZ4TIURYECHEswj-chW2HqRBPp9doj3IoUJ-j1ptpfZzP2AJp4nh4bs4jjAAR8Qmw3Bbjd23eJN5r3MDCind9V7H4Hq1vegnArNPOTTDgN1l4_eNrVTxcDucWYoVMOj9sl1LLlttWXHZ_iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم مصاحبه شجاع خلیلزاده قبل جام جهانی:
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78923" target="_blank">📅 22:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78922">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac246bd5b.mp4?token=vGQjM8mQXudYqxJDGxgnwRuI7fWwWEo8TMwsgv9y1FoMe_AXWv0qrozGkH2eHqnhrN8sMUeNRlT8wB3CQGafGvtA8O2_amHnm-cFlo9AGNzcw1-mUIFQTliq3UyBblaYQw57xRGyzjvsLGOCtpB9yPWVar6P_LG_RIwn0A0V5c5769z8m8w6aSX1ycNDfu8BKqm_zk6bsUX5gr1an__1YjRlJdVGytCIouEuGxGiUZwAAHg1x7EaKQBF4SC7YR0HypZWWyyAWYx3_24Gcrz8RFr4wlwv0b4EM5i1rSfTiyhpm1ZsivwVS8T-wAQg6uWEn9wXTx8NKVNFcPIWLNcK5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac246bd5b.mp4?token=vGQjM8mQXudYqxJDGxgnwRuI7fWwWEo8TMwsgv9y1FoMe_AXWv0qrozGkH2eHqnhrN8sMUeNRlT8wB3CQGafGvtA8O2_amHnm-cFlo9AGNzcw1-mUIFQTliq3UyBblaYQw57xRGyzjvsLGOCtpB9yPWVar6P_LG_RIwn0A0V5c5769z8m8w6aSX1ycNDfu8BKqm_zk6bsUX5gr1an__1YjRlJdVGytCIouEuGxGiUZwAAHg1x7EaKQBF4SC7YR0HypZWWyyAWYx3_24Gcrz8RFr4wlwv0b4EM5i1rSfTiyhpm1ZsivwVS8T-wAQg6uWEn9wXTx8NKVNFcPIWLNcK5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر رامین رضاییان در مورد هو شدن سرود ملی جمهوری اسلامی
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78922" target="_blank">📅 22:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78921">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اینم یه آزمایشیه خدا داره منو میکنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78921" target="_blank">📅 22:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78920">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">همه ۵ سانت و ۱۰ سانت و ۳۰ سانت
واقعا این عدالت نبود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78920" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78919">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نمیدونم چرا اینقد بدشانسیم
۱ بار ۲ بار ۳ بار ۴ بار ۵ بار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78919" target="_blank">📅 22:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78918">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بهترین ترک یکسال اخیر دورچی ریلیز شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78918" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78917">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">همین امروز با رفیقم نشسته بودیم داشتیم میگفتیم بلو کیری خفنه بیارم قطع نشده و کسایی که ملی داشتنو مسخره میکردیم</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78917" target="_blank">📅 20:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78916">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بلو هم قطع شد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78916" target="_blank">📅 20:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78915">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtGrAE2Tl4Mj1ATPHxodgwqUSKPIYIFOwvPLMrmwm4snL5nu8asYkeFX9k3tLoAGH2zXM289VDsjtZ-dTAM0i2vOr732eU1lxxxWj24L2OyHi1-KQd1WWLEU0rAt-dnuP7wRZ0TE2cIlKhPcIqqca8N-5CUpHA3cc7lwgqdmSK1pXHNfJSVB1NvnFkhk2WTJf8Iq1MPuT-AhpnNBhSav4Il5Q7W2kEpK-uHqhctDMFHYOFHgXxuZ1cRoL7I376Bt2v0Oor4iAbP_yKyOCaWojeX92E_4b8ZIp6ZPBxUryuS5gzTEw7pDHv5gWxgPfPnw-TWTTtHMM6GDcyPe_pKjxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتفاق بد برای هلندی ها
فرزند تازه متولد شده خاکپو درگذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78915" target="_blank">📅 20:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78914">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltkFN1h2KUoycdigOiMdX5oH_cJw-TsHRXj5QZ5MWHTyd5DEwXcoKTerbd_QOuV_xQtYKVWZ1S9gFZzv7XNI8yFnHo7nGYbT_syzo6xyMARBXzfuZSPU5rQcuf5N4RcJAvmN1UwIbPk679mUG2LYfHoKH--Tz7pFgho1P1BjCrjNy0VjO_cF9UGcXylXjdm9xvfKVvm2deUKT8FylkMVq5Exis_iD2grH3iqmMbNTA_xqOlSnl74Eul_ENfmVaN5oRLCXxNlZjMbgQTqgsTswGvam_dZ9FOq3jP6MgXuHk_x6HF7Q4q0D-5c5kd7IujHnx5DkSADXFpyFd3MnH3wRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجاع رو کل دنیا دارن مسخره میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78914" target="_blank">📅 19:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78913">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ij3S7tHATisuUVvBhWd34BKonKkaSss1Q6Msq4KoG-cGlXtfouoQRmuvdIRvE7siib8oevQtOwBw5H7C-zxkkRcFdNUDn5JmrlcTbqkTJ520Yi4U0nh7hSuODWLAaobgH30-EF6SLOUrjLs-v5E_X0fLuQi1wjozsbFQZcwiV6OOZyED226TGMTiuV1xitrVXkN5qFbrKWcTZc2i11_tbnLvrC8oWfwJCYMOUBd_QT2MMNKZh9gRH1qGjduMZ5Ws05P1eQ9kmv4DA_88JHY9lHvHv14_OaJbgnNsBTQQaCUzFxM_HtYdJmvPm4qEVLiadzIheMODdNK1pXl2FdsCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جام‌جهانی هر بازی داره منو سورپرایز میکنه.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78913" target="_blank">📅 19:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78912">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhia4n5fo3XD5q6AAsjyvHmoHgjz6WeDOalsbYRmskKzG39uxauns5_0a_7oee7rRpMHdnlmc-mlxD_KPt7RwalfWqk7b5Y6Wj2B6QdsPo_e5AdbBKQVvoM--OVLnQa6lOnwzpe_2NiY2NQIPUuivMaE5zt66ZA8C40knca0PNm-Zvulvo72lJG8r6y7DTHML7pxW7Oma8XoK9qB1x-yovG7Q09DvKl5a8O4KWJC9DxYie-AjpeXRLjQ2dyRiUTHJ0JccoqfADfEB_VIVh15nkuSr8-vn0H6PltnMw5jEbg-EvcGRTZkXcNrqz312ifbcF_oJO32KDL9CIDxUkx46Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی گفته ایتالیا به جام‌جهانی صعود نکرده؟
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78912" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78911">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">RitzoBet.apk</div>
  <div class="tg-doc-extra">53 MB</div>
</div>
<a href="https://t.me/funhiphop/78911" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
#شرطبندی
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78911" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78910">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbdRUUoK5DrxA28uxOTETHEKYoU9xBpf5uaZB4maZefxXm2gg0lG6iUT2M3AmS83dms8BTdBSUZIc2_bl_-0FLfpPbyZZ_RqlgITbbpdYrxNfBY8pTpSmWqw5lToN1qb6CVbkKu5QJwRWnaryaQzJBn25pZKy7CWPAmiP_YsGpjN8YtOgX-IetSBhXPrNKGU8G-BpEiVE0uWGb6iyu6V8qpEx7hk5Ow3ZNLpmfMFIUXhL2ODzahZktdRGckmeL80R0G1afn6YQ0d51LMCkiOEmDhtX7O-dvW01wYmUpTdUFix7oKqfkJn2h45lgcvisnuNYuyIV6pFJpC-0spBZnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شبی پرهیجان از جام جهانی ۲۰۲۶ در ریتزوبت
🔥
⚽️
کرواسی
🇭🇷
- غنا
🇬🇭
⚽️
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- پاناما
🇵🇦
⚽️
پرتغال
🇵🇹
- کلمبیا
🇨🇴
⚽️
آرژانتین
🇦🇷
- اردن
🇯🇴
🌍
امشب ستاره‌های فوتبال جهان برای صعود به میدان می‌روند؛ شما هم شانس خودتان را با بهترین ضرایب امتحان کنید.
🎯
دانلود اپلیکیشن بدون فیلتر اندروید
🎯
لینک ورود به ریتزوبت
💎
امکان شارژ حساب با کریپتو ، انواع ووچر و کارت بانکی.
✅
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی جام جهانی 2026
G6
🅰
🆔
@RitzoBet_ir</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78910" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78909">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">همه ده سانت تا ۲۰ سانت نمیدونم ۳۰ سانت</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78909" target="_blank">📅 19:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78908">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترک جدید حسام تی‌ام و حسین تی‌ام به اسم " West Side " منتشر شد.   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78908" target="_blank">📅 18:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78907">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc8eGxuQO9SrMDozI4RvYuDKh14K1DvBRvTicvrT-D1WpG0nslLBhOiYhD2JMxxxKnYCwZY0dmoG8JSdmXbmT9CnzUhKKSOWUst-hMp9pukLw3lIQDZE_meKWc0PgmU-0AC79uN4JNeaZsAg0B33bq9EjxTJ76vfzKtwFbG1gw392MUuRj8mGjwKJjTShT_xaloEfBhLwQm7W7wLcQNEk2C29cA2PmtKJJF6sipjjNS42UNISWyXX8ZKMW4jpbxMRKs6F_Hr8N2A6KNqzjx0WNm_hnlp-eSHYAZSF6TKgFQjY0-TZ6FwBJXIQ50ZzG-LsA04xCvE-G5XzFrYiCpfBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید
حسام تی‌ام
و
حسین تی‌ام
به اسم "
West Side
" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78907" target="_blank">📅 18:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78906">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">موزیک و موزیک ویدیوی جدید مهیاد و دینا به اسم "ATISHSOOZI" منتشر شد.   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78906" target="_blank">📅 18:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78905">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izKZgJ4vyKvfuFHpNmtJ076D-KtZkdeIZUXlH7D5QvzDRtFX0NNkFDjAT2HWqSyG7Pdnq9uNugeiDzKPcc_nKxzG2VjLdZHnqPipucTkkgl6docI8cEjSu_9gXBkDpA9N0NEvmWqsEMli9n-zHO6gQdBoEF-gCb9kAcu0qvmtMwqaKdbNeE1NpnIlXLwg0U7LM8VKLLTjY2F3TU0qp_X4bZ4PUfTFN_vxnvWBE_ddi5OaB1fF5mCRP4VksRlHKNXQUsCMOXVL8Cgajs-Pfgd2IvSDLJYwkPt5S_DGmZcqU3Pa0AExUiqz22XbFQqvMCL2XPJGjYtU_z8571z2V4ivQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک و موزیک ویدیوی جدید
مهیاد
و
دینا
به اسم "
ATISHSOOZI
" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78905" target="_blank">📅 18:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78904">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🏳
سرور مولتی لوکیشن موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر و زمان نامحدود - 60000 تومان
🟡
سرور 20g - کاربر و زمان نامحدود - 120000 تومان
🟡
سرور 30g - کاربر و زمان نامحدود - 180000 تومان
🟡
سرور 50g - کاربر و زمان نامحدود - 300000 تومان
🟡
سرور 80g…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78904" target="_blank">📅 17:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78903">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pgga3Aq6BhTLhbssqlDk-eycIKHyzBv7nh7XFxpoak7dWFtEHABIod2vSL_zsnLzykYv3F8GtNwCtG7YQ6_P0Z__KIeEJaCg03RRH9GO6It6cKfrtNBe5rctp0guEW_Gfpz82zA3WL0TTcNIDj4oER5dmu95DkfLBYcLAc-U1QiZl4gpth_jBZh__fSkogMxw6RRMoXQvonvuemisoasKwskaHpyvvmRpKUEcJ26kVIKJUolcBF1j0XJywcfIEmVF_3QS9WRyGcSBCpKlY7oeYpTKC-s0er6CmUUK4F_A-R9vvSTFZdBJ7BKLBbj1H7PxHNpO8KoV4ZmMNLwMnb0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78903" target="_blank">📅 17:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78902">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سازمان دریایی بریتانیا اعلام کرد که یک نفتکش هنگام نادیده گرفتن هشدار های سپاه پاسداران هدف پرتابه توافق قرار گرفته.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78902" target="_blank">📅 14:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78901">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sI5PETdfX9iC9kvtBDQ8fdeszMGNuROlN8NwokKlFQxTrS2pP2iSnrwgndWwBiJezzDTLzm-mXbj3E7BgDvE6kK8TIJRclDEEUrvKcjQxyR4DfZ9sKyooy27DrsU7GQ-VcqyWYJaq1ekoTGZsDWsL-eEd9kUTTfrYSeIKpLAUA5bhfnC2IzT-bxi5zEMmeqhk6YeFnc7za6VWvM8CckdJ5TNW4JsHoxlapUN0KKZPsLRKNINW_PXO0rJdoH5kwNSgwgigFTJnbFBR5WhPgLhPRoweLrIeLXrsELS7ajHn11avliFb7M62s4Xc3eiAQaeJvJ4OVKQpgwNqyNLfeEgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی دیوار فلافل فروشی توی بوشهر نوشته بود
خدایا همه مارا ببخش به جز طارمی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78901" target="_blank">📅 13:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78900">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4960c204ca.mp4?token=TqPiLz5ZUYtQqEACTHSuKfTn1nmJlTrQSheS9BdrX8NG6BJx61D8y3HNcKYw83sZoQfUbZCXh6LnvQFHdOC8aoC8vQwhe_rzgM-PxgP7Uc-owZuCJWcQgAg7TG8PolpWjJ73T6BB8gyghgJ5H-X6ihsJ_LcvahNWsqRTzWO8VhOK9TPm_YDVVEafmBBsh0t1n9FOz7q4x5SQAPtFoeGf7SC56nMMYOrp27kaVkRo4B_Nm2X6v4rtK0pQ1Qh5jWmJX3byBUfUD_v5sgQ9NBrgrlfRgs4fAMmXaGQ1Grb9urN2Ao7hN6xzD4j6rr-mCqD7LTIKsN4PsLZMeuQ3t_9_pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4960c204ca.mp4?token=TqPiLz5ZUYtQqEACTHSuKfTn1nmJlTrQSheS9BdrX8NG6BJx61D8y3HNcKYw83sZoQfUbZCXh6LnvQFHdOC8aoC8vQwhe_rzgM-PxgP7Uc-owZuCJWcQgAg7TG8PolpWjJ73T6BB8gyghgJ5H-X6ihsJ_LcvahNWsqRTzWO8VhOK9TPm_YDVVEafmBBsh0t1n9FOz7q4x5SQAPtFoeGf7SC56nMMYOrp27kaVkRo4B_Nm2X6v4rtK0pQ1Qh5jWmJX3byBUfUD_v5sgQ9NBrgrlfRgs4fAMmXaGQ1Grb9urN2Ao7hN6xzD4j6rr-mCqD7LTIKsN4PsLZMeuQ3t_9_pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کونکش دیگه خیلی رو انگلیسی بلد نبودن مسلمونا حساب باز کرده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78900" target="_blank">📅 13:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78899">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNdzJI1gdb4Q-2_7H9B1U9zQ0HXGovqRPRHyaWnbfDbxoNqFGraU6rg6hhg3-uTVBfEi0pTcMhOoTn419j0IXL8yZjTYB_eHAsSlhS-pJi__OAdsWTqeoiG4U49Nn__WrldVYXc45XBAwl_-EoJnB3rP5JvK4sbMJGtGSKMnBPLx-Ioe_pwCDbb3p7x6yR-U1_AWk-eyykBh0mCSuQAmfFMr8_a8nbfITJRDxCOTufn_38OeL38hxiZ4oOju44GddV6MWVWh4F7mD1OMtv2BLFskoDa-WrfGMl_jsQ92G7qnwvgzPplRSd4hfxcFuRydXRTVIdksp5nen1UfzB-TzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی به کیروش زنگ بزنم براش آرزو موفقیت کنم فحشم میده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78899" target="_blank">📅 13:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78898">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">من کیری خفنم پسر</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78898" target="_blank">📅 13:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78897">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi🇵🇦)</strong></div>
<div class="tg-text">من کیری خفنم پسر</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78897" target="_blank">📅 12:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78896">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فک کنم تتلو کل درآمد یوتوبشو میده برا قبض تلفن زندان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78896" target="_blank">📅 12:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78895">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تتلو چند روز دیگه موزیک سومشم میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78895" target="_blank">📅 12:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78894">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9eMSOIWpmhbEgU6huV3urS4lBQkYTD_FmKD_KsSAaK30WfTiJ-Q3gXWalyjXFbc4Qf-ojvaLGPL-FFdy6TePht4_goA5xpJ21QEiFiTpDWUidRNtch_w1yOThyFP-dVPrE_o2yFvy3QJ-u5v56ldCHurLGwwh5EfAZjvYWkuOug1R3XTIgTGbj_XI9T9mz3vinFZzRA2zUHArICcZLaBDfAZiOBgWtrw0tNjD9jZcq3IbMLpU0AJ9At1Fank1oDHhsHb7_2NXNfwAw2VLyLsTkeWPesMfHQqfiWltMHmfLkj2yzCJtpSIQqqMxElNYX569C1zpY5MFxVLbU7mwjSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقد گفت بدویید، دویدن همشون رفتن تو آفساید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78894" target="_blank">📅 12:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78893">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEwDffaF_QYlxTzWgbZiJUXh4vCEToPvoAPctnzuY_DbE1DI70s6H6HSBgUTanapIE0wb75qCDwZydRX08C0JSotyoWAQQtdy4_OfQuyuuyJpidKBp1lbDp4-6bKkI2lWspIWd5nfusaMUwgcHcY_eZeO6dCFyRFn0XLW3aUjPX1XZVjnv9H4tkQtDX4h_y8v4VxuJijt85sOiOrJcSFu8JptQNxo2bTNOu8FJB6-dLfwwkbx7O24e8vU_JZ8x1z8uQFHhF6tTeJww_PAoZIUcpkuhA5H8bNpKAX-2_sS1cyuOPU4R_C7NV6A1FEwQhPqOINIXrJjYsjtx0wm6FvAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
می‌دونستین توی
ریتزوبت
هرکی شرط‌بندی کنه، هر هفته بین
500.000 تومن تا 100.000.000 تومان
پروموکد می‌گیره
‼️
💰
باحالیش اینجاست که فرقی نداره شرطت ببره یا ببازه، تو هر صورت پروموکد بهت میدن
🔥
🎯
دانلود اپلیکیشن بدون فیلتر اندروید
🎯
لینک ورود به ریتزوبت
💎
امکان شارژ حساب با کریپتو ، انواع ووچر و کارت بانکی.
✅
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی جام جهانی 2026
R6
🅰
🆔
@RitzoBet_ir</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78893" target="_blank">📅 12:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78892">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVyiOh6mVr9BqOLGPbZMSVXO6WDp24vdTMaPRBIoMaYKI3fyDiT2BtupElwe2aH00Yg6H31FIv8gAfq08jMJvDAm48mMT-O5QVacqERZsbGrraz0R-Vex9H546rsblmLVkkS36CpaVN9Iq8_Ye5x53lh7nsJ5O7vr3iJRxCZiTIwsKeWDFQFz9gvF9Yu1zhrVLtq6cxvKRZqqykTuyYg1POXHAP08TOSvitoZvQPxff2_az3GlbEiq20w_YwXCT6n-54E_8F4TNPL4HMZ8nDc6XVRx_nlXEoqo23hwDTJ5kodpBULSPhfRn6YWIVuu3OZtR7l946gUQDCinW85C7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثکه تیم باز یکم خوب بازی کرده و شانس صعود بالا رفته میبینم یسریا شل کردن خوشحال شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78892" target="_blank">📅 11:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78891">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حتی اگه این تیم رو دوست داشتم و حتی نتایج بهتری هم میگرفت خوشحال نمیشدم.
چون هرچی شده باشه از رو خوشانسیه و هیچ برنامه ای پشتش نیست و نتیجه ای نداره، تیمی که برنامه پشت نتیجه گرفتنشونه مراکش و ژاپنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78891" target="_blank">📅 11:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78890">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مثکه تیم باز یکم خوب بازی کرده و شانس صعود بالا رفته میبینم یسریا شل کردن خوشحال شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78890" target="_blank">📅 11:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78889">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سلام دوستان من تازه از خواب بیدار شدم مشکلی پیش امده؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78889" target="_blank">📅 11:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78888">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جدول حذفی جوری شده دیگه کم کم منم دارم به مسی شک میکنم</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78888" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78887">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اوووووو رامین رضاییان</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78887" target="_blank">📅 10:32 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
