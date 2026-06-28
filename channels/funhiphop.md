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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 20:29:22</div>
<hr>

<div class="tg-post" id="msg-78995">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t73CVhWf77goagBvec5s3vQyK65IL4ZUcbK0wBxUBt7ykcvBIU5OtWX3n_JcirONpYA72BmXyMprqEuwuwhn44fx9l1MYAAPfzGsJ-8HIXTYETfAmowTy-4mH-w2HSX6Dcy1zp1oeKuVd8ry_QgwaStkIl6SMGUcAP6MG2USJSu6xExwO0S3wcskIRPyaxwf7F6fppqbDvK9E1t2wurY8bTjC_TulKXGSLIOPdMmzAemgCe_khZ3q3B3keLoya6Xpxs42m_g3Jp_4M2Q3ps-lp_dS1coAx6nYVup0Ru6j7xZQ0XU6tdwioFu1hu-OyTLFZhgIHfeXe10lnW2MXM4Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو افشاگری جدید برنامه Jeremy kyle مشخص شده این زوجِ گی بعد از اینکه 3 سال باهم رابطه جنسی داشتن فهمیدن با همدیگه برادرن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/funhiphop/78995" target="_blank">📅 19:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78994">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pncOUK2r-cbCs8j23i0u9j-vXABV1PDabbmnADiLnSRMw6RblowX8Kdvw1yF9R0mIrO942aGNtEB2tlE9U9NzwOHvdGkNmEkHWzgoPMh7hr_WaXDGPBKTXbMQWLUkn6vwpShgzebLOQQput5iRaUzEznymx6G3VgfH1AbyBdq8y4258iQI4LyLBo6LkFWOJ8oYyD1m9PDNpyxapwefU_2riUE4OYSe8j1iRCQJHi5aJQzNV8ugLSoMUXPfJ1jmDh6YLYBlcGTfv6hb2MPDHtTNGvafLxVp78MkXgey_4Niwa1KV-2C7QGhX3_i1iPZw-BfRGm-7vbr3jnoDNhHdd3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب تکست کصشری داره ترک جدید پوری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/funhiphop/78994" target="_blank">📅 18:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78993">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-YVSj6gsbnp__vNiuyYYLArn3ARn8bRLADZ18QINDGFKUyRvs3_UTBMM0EytlVsIx1CSGyBMAE-7qEmOzF-D8OrPd8kUv9F_Hoy3LhckjtxEgarPD--cnso107C4oF6TBaZhCEXgerdRjsGyTDm18QM_uoGMk2wRwvn7mxf_e2D40A2QIHU91N2r-2MZKSvn0zwtzHAcZM5C3NP9ZUwwFoSPdpV5iyEzAXf0lSYC_ca6j-iJzNllFHZvn4LlC6gSusnK-bQO_LOHFzFg71lIPWZPXH2bd3pSpL4CE7sWfBTWDRX1PvrZijKxnBIW6Yv9AJfo53DEgNgMoEHflpV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید گوگل و تبریک صعود به مصر :
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/funhiphop/78993" target="_blank">📅 18:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78992">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/funhiphop/78992" target="_blank">📅 18:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78991">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/funhiphop/78991" target="_blank">📅 18:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78990">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tP5SI1lDSS3Z_zCquetUvg8lSfMknk8IgLraPl7Wj_fLXmMXl8C7Q9iz5QT0jWwu0iuOuxiFGUplke7YmJwsH_Jy_Vt72jEdGwc6XmCa7nFnzxaRgTcCnJD7E1fFPRaP99JFNhPwLzFhXhTThjEmA8XLDk6Dp5k-COE-A9DIUCIbUD4L5Cr_xHSuPrANk9qSFN_frtxRVn-JLaDWfD9bTlrnkpk7hXFK4h3-SOm_KN-Vi4hn5XN2KVPLOv03jQwDQ8oQcoX_g0S9xWYnFQLQ7aIv76ub6RGnoHEropBtjmuR6loXdUcTyCi5GEZi_wQtaG54e4h3ePhPNpyEPdR7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری کوروش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/funhiphop/78990" target="_blank">📅 16:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78989">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ایران توی جام‌جهانی : ۳ بازی انجام داد، با ۳ مساوی ۳ امتیاز گرفت، ۳ گل زد، ۳ گل خورد، ۳ گل آفساید زد، ۳ تیرک زد، رتبه ۳‌ گروه شد، بازی ها از شبکه ۳ پخش شد و برای صعود باید منتظر ۳ بازی آینده بود و در نهایت با تساوی ۳ بر ۳ الجزایر و اتریش حذف شد  @FunHipHop…</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/funhiphop/78989" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78987">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTDSLs9OErkEwS_16p3ZmZkb3nXEbMP72lT_ORmouReOakZEXW2YHbl7KOWG2IfWVGIpG9IukK4Nwuf1GT4YuIwbP8Z8FEjzLRKMNaAaYgTpz3LOSeetXFby-v3lxlV-MnJRzRauSx5SGe3Ob7SgxszWcOTQ8kHqn6sN9tNhZcSW4wWA9dHUQiBaJ0gBuco21kbAZN4TkB1XMn4XFrrAroiwyCB_fMo6tQ_jpXAQeJYErzSOEkXGHNa1MHcPeyVcnnMswh3mLAV3TPOugd9YablNHy2zKmM2wNl9XecqhAwKhKhk5BuzYsEQ1x3asuC6Nq7zJL0Zx3WCTgGZwX-HvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز خبر اومد که رئیس‌جمهور عراق یهو زده به سیم آخر.
یه شِبه کودتا کرده و با لشکر کشی و تانک و... حدودا ۱۵ تا ۲۰ نفر از وزرا و نماینده‌های مجلس عراق که اکثرا حامی حشدالشعبی بودن رو دستگیر کرده.
با خودم فکر کردم که یعنی چی می‌تونه عامل این اتفاقات یهویی و غیر منتظره باشه تا اینکه با این خبر شاهکار روبه‌رو شدم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78987" target="_blank">📅 15:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78986">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm49WzfS6ClAYOjKfWUA9DxOONoZzw4v7Ft7_cWcJ_BO_itS2pIFLSmHLkA9cSWRT168ZonqFHDXTApH3gmOp12kDqGblWI5SYPwyuUlwapgdhrrElUn9A0Db5wgKLfLh_2TjjYlBDyjJnpHEjft-Km1fsxdrboyUWj_YiaSUu-a3rBDlvmtH4QM2fHeKc9hVD_KJ5BKX-JJIrlIqgwzpOrKs8k33beFLPHLkL4WQdGJeaW0qmzsO4ypneUKw8NoTcK7ZrB1K0_rR5dUM6xGplKBeQu0CoQnROQvHgvBDAlyK23ygZ0aOiZpqtM2Xd6b8NE1Tq5P3L072DXGFFb-RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری میثم پیرفلک پدر کیان پیرفلک عزیز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78986" target="_blank">📅 14:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78985">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1wDyK_bzi88r-vMYKA_WKAODW88A36EcHhEM14kKm9DoWAOFlkjVP0gcrDOaQu46ipLZ2SZTIFC3MCCUR8GtFTpZQsEuRJpAx4fx4ZIlKE-_E6jQxuh4BoTSgpsvzHBTMAh_JBGMgf-fvY7GcwXyoWmUwnfHpeqYCarCIIpjKqz2S93oJm1mAMBvcM6iqX_aE1GP8ZoouVjs6daxZXqfD3sr6op-XIhb79bJaS6jcVEUCpdb9qaBnKUfH9Mz_3t2m0pYrZG6XIxEqxS2FGtF7UncO_mpqb6q4_nKv-FnGgfz_j4rpn845btCQg4rfRVPI8tLLkkovuKnHID9Jg9ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیل زاده ببین کاراتو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78985" target="_blank">📅 14:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78984">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78984" target="_blank">📅 14:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78983">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">"من برگشتم" رونالدو مثل "من اومدم که نرم" یلس نشه صلوات
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78983" target="_blank">📅 14:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78982">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">جدی چرا چیزی از ارزش هامون کم نمیشه هیچوقت، مگه چقد گرونیم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78982" target="_blank">📅 13:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78981">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قایدی زن جنده تو که قرار بود یه دقیقه هم بازی نکنی همون نمیرفتی نمیریدی به محبوبیتت دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78981" target="_blank">📅 13:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78980">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اوووووو رامین رضاییان اووووو رامین رضاییان</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78980" target="_blank">📅 12:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78979">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-LeQTdPjU6yfkkjc3cQispa-YzR1RciA6hBKakqnxML2lePocBlVNXeVqAwUvifS8IcyQ_okf9abf5ef5pP4NsGmT265bmzE-SNoYKUe39Meqmq0KfEt8Wkcju7FESzIuXnQkFLUB0Le5UakJ6RrlZ_RChW6d2mv15bLiqq_s8IXnIFRR5UryeRV37MYgwbwWl94OSXjTKCvdXjbgkNhPa-WT08gFiKiSO-iQovnFi0rx5be5EZJhriatvCQdu9fHzrhkO4rvUyfo2f5BQ3NAA9cU3nCXOGwyffOR-ELzoamLRTKmkYXXHPZJtrA0D9dny5vn4tXqs4x9_8tH6KKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند: مسی هیچ‌وقت قرار نیست بذاره من کفش طلای جام جهانی رو لمس کنم
😭
😭
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78979" target="_blank">📅 11:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78978">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سنگال با دو باخت صعود کرد، ایران بدون باخت سقوط</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78978" target="_blank">📅 11:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78977">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">همه دارن خط حمله های آرژانتین و فرانسه رو مقایسه میکنن، ولی بنظر من کلید بازی دست انزو فرناندز و مک آلیستره</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78977" target="_blank">📅 11:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78976">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVwN_qJRjxzoCDFIDP8DSLtEPQ8WbpfxpRjD-xm09nrqOZ4CKUtf_Kduhsuu-bcQGyqU5Q0xwpTe-U6NoJLaklUyqghuNn_Eq-a6LYzNAGEk_lqeG5ZUVyzx49T8HKv2iJCdTsqAJ3aGlLHmous-7UkDhGCwvmiLeXu-yZGtRKfE893wp-bZZ9w9BBYmzL9BQvElxFXKzye28DVSAOBHC1NFQXam4VjuLnOZQSQQNkBMiWBWwX7R_jpAhlHmWkgzTCRQcP36-oWrxPCDZKyvg0gis1a2AcMTH3bGpu-jCDv85RsNHmakPjeHcmh4YvaZJ1iSIdPlg7r8BMCS70bIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا خود فیفا هم نمیتونس همچین مسیری تا نیمه نهایی برا یه تیم بچینه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78976" target="_blank">📅 11:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78975">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هفته دیگه قلعه نویی میاد برنامه می‌ثاقی میگه فودباله دیگه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78975" target="_blank">📅 10:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78974">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0E4vxo5VKDFpdxY5psI-t2FA_WdT_Uxd93uHeaEOFIJfpx6_q_YE1JjahHsU2sJnTc1MhYkvzZ230VrISdL_d5zdENfxzHLEXMXthYZc_ItjUY9Iy4nahXakN_r9-n0me5MD2jn2-RSpFZj9nZSYmC4si5ygk3TEUqFA1DuYtk_tbtzVQS8BoGOdNfiWDUNPFkhWlV1ObjDnttcwQpAFW37EObo7z7T3SJ1NF7DjJwrUuvNcUPmshaHL1p7CH30gd1dh4GCDMPjz_B1XIf3xFiabAEekrd29lgIROJTaatnbYnU1_IlKFjWLC2SrwKlPVRcGku0---eHraF-gb4ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب یک بار دیگه پروردگار و اسطوره بی همتای فوتبال جهان، حضرت لیونل آندرس مسی نشون داد کت تن کیه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78974" target="_blank">📅 10:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78973">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78973" target="_blank">📅 10:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78972">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oN91W8-2RhYXgxH37qBSU0P193E7UHHp7rhnsyqeLdrIXCMPe0nlo2K62r3Rh6S7qLZxzL6AkIWr14a5pAO93JQA-GysSkcRXs1L8Mnmf2KF9kSgyj9oNsTgVR2HjYCeqQ7rND_PsJkuJr5Nl-Hl60F8kmvRcXmwoBWk5ijT-cV1PvuLlXLn6t-gP0aDyXsEE8kOeIj2X814bASZe1RnxY7Rd4xmDLDyM0-L8ZZVs7KQynqf3EJaTf6ggiI3JOssq5Y7pbEKUpYDjauSqKLMxhQwrQIt_iRtKH5t1OMNRplSr23oqmMLaMREBl6ZXe5hvHOWS-qovXXLWa5lwURmvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران توی جام‌جهانی : ۳ بازی انجام داد، با ۳ مساوی ۳ امتیاز گرفت، ۳ گل زد، ۳ گل خورد، ۳ گل آفساید زد، ۳ تیرک زد، رتبه ۳‌ گروه شد، بازی ها از شبکه ۳ پخش شد و برای صعود باید منتظر ۳ بازی آینده بود و در نهایت با تساوی ۳ بر ۳ الجزایر و اتریش حذف شد
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78972" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78971">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78971" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78970">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8PmjkcDkR6WRXlrd6yi9hqlWSd2qPThrqEPI4WJwE9pmYT-kcFHiNO56m6fUtpoqUn2uGMzJJ8m0sVt4ufmteaniTqyWVLYql1N690Y_rCoUdPVNjnWKCcofxhl1nq9HsQwLfu74TDDpx65wSPMn_2O6TSNvdaroKwRh2vj8oNo88n0OEUHQk7y2wh8QcYTXm_51ikzdBq4s61gHKGLDrgTPQ1eyjE0pfCbQ1shwLcpix5h7aEszG9jaaDGXAbXOhUv-c7hrlTmdFufJpV4v4JZtjH_2GuLEIWF9yk0JdJ7F_uqyJ7oJB_fssb9OmfOIJ_qxaTj4OfBPExqqj9RQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78970" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78966">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سلام بچه ها من تازه بیدار شدم، بازی ایران سوییس چه روزیه و ساعت چنده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78966" target="_blank">📅 09:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78965">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">با ریدمان پرتغال جلوی کلمبیا، پرتغال، کرواسی، اسپانیا، مراکش، فرانسه، آلمان، هلند و بلژیک همه رفتن یک سمت جدول حذفی</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78965" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78963">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CIkFU8QQR8IhZXup81mS-gLlsXTXCYQe7yzm3HyFZGF4yyrRq2X22f1P2B4-y8gWq9_92Ddee7JO9Zx4uVIlJyg9rLSdxEpI6qXTLFNV5ox36G8Tu7RuioiDG46kEPCK8n-z9FdK5HtDccGPS7IlsLVZhouK2ynuMmt6UzjZe3k_5ybdWhCj61RjDlX-FZ-8NleXdoHP5nnr0kXuqh0Nyh8iVLKr47zBmpxGQczWpkoGH_LVqd2ISCTmAIqAkg5mkhhTbXnpbVYPHjMlbPd2HP2RgJEhhQ9bgrULYUF29iSu4Y2gd6i2eXHEQnEzfnJpHjr8--D4p2x3BF8rhr7Ngg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9QZt8CL9yi05_Y8wCfS7wEcLijpYFoRDv_HN4k3WIE8oHweIYsUYgGWhQuT03pA2w5j2CA6NMx8yTB3u2L5-vpiRFRV9zER5zV9Tl93WCcFxULcCtWjhQ1h9HZvEzMbFg3Jh_u2BwKL4DKyLNrD0suwk4zJBIxoR794exjFVolaMAs7BKCT79jUe16jr5toWwNe1d1IUldJ1zKlTfBm3t4mzi-ORmEx0zWaENBwjwwZs60d2CJUKGd9cygiUiX2DEi4ecnQj7sCJVwO8RZhHPFnnpVr0qrtMnO6Sg0y6Zl_2doIrW7qUqstD9SJHDhke9FQEhVbHcUP_Eey51cLnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من برگشتم !</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78963" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78962">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmeYlU8DQ-LysvgEL57EvqTMgPPZwwY8gHJFFk3hTpFdVldHTKQedc0nf_wfOY7BArzO9ESUsnJ9yjfsjeGD1tNljaex_P4Z1owytTcRGVfZkZTMWdytNR2SiOqXkKXc5E10QHH8GxxcFoPSksepNnq8hvug1yEw4r58DOOTQtHCM0Fv9ZNMC_CtXkp2hK2FwFv9xxVUxZbt60lSCH-H9WreriKPTYeWenx_Cvn_CHxqlOaJzF2O_SK737pmCA3uEsZUw7w3BEy0fhnDShqNnzMU8hLBLKF6kE9_ryy-v14_uTBsIP50gjl-MkbGY_MEcI9XR6yZLXr53AYj3Q71HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78962" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78961">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">احتمالا نیمه نهایی انگلیس آرژانتین و فرانسه اسپانیا ببینیم</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78961" target="_blank">📅 07:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78960">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa8b89a24.mp4?token=YZorXA0qpYoNvUozJ9X9mtJiNRXUP-xeBehnztUAtcJbqM_aQT112z_lEjfsoz00o1n1uZRfoiM1eDl5jZt0qtXPeIZYn48_3X-EpcmqwwA-hRjc9rSjvxpk-hUdRwVBXqUubLJgHOHYrRkLgxA_bRr-VByJs88fP0obkQUWiST2ox6zRVK0_LDmzqLZ-tqjxVc0Zkp2Ry1OvRRRIX2-T9-Z-9bmEXU2z4qU6xosnbZSssMkun-CCIR0zaLfsklrzQ1Qfpqa1MpHd5AsSQF06XtOFHBkIl226l-e9jaGfQuSMqB6z3ygT4CMlUxIqQQX5IoXVXHGSSPzJ9wlOo6kIjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa8b89a24.mp4?token=YZorXA0qpYoNvUozJ9X9mtJiNRXUP-xeBehnztUAtcJbqM_aQT112z_lEjfsoz00o1n1uZRfoiM1eDl5jZt0qtXPeIZYn48_3X-EpcmqwwA-hRjc9rSjvxpk-hUdRwVBXqUubLJgHOHYrRkLgxA_bRr-VByJs88fP0obkQUWiST2ox6zRVK0_LDmzqLZ-tqjxVc0Zkp2Ry1OvRRRIX2-T9-Z-9bmEXU2z4qU6xosnbZSssMkun-CCIR0zaLfsklrzQ1Qfpqa1MpHd5AsSQF06XtOFHBkIl226l-e9jaGfQuSMqB6z3ygT4CMlUxIqQQX5IoXVXHGSSPzJ9wlOo6kIjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگری که میگفتی عزت اللهی رو برای بازی بعدی از دست دادیم، بیشتر از همه به تو خندیدم حال ندارم اموجی خنده بزارم</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78960" target="_blank">📅 07:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78959">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یچی میگم نخندید،
تیمِ رنک ۲۰ فیفا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78959" target="_blank">📅 07:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78958">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارشگری که میگفتی عزت اللهی رو برای بازی بعدی از دست دادیم، بیشتر از همه به تو خندیدم حال ندارم اموجی خنده بزارم</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78958" target="_blank">📅 07:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78957">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFEmchQOA2LWQatIajxA7nJS7hqbJeRCwnOsNnjdG2TbOScAH56cnsF2r_StHkI1Pd0CJ91bv_ofrUl1GnHr6dS_0NfF51EkfnCrdjnPw0nI6Oj_pPnmncbbriobAe-xLBuRkIwnaTNfID7XRbbCoTppyA3qBh6clue4xxBBCtAzpG3UN188HSSRg1AsHXMMGnbOKAtlqhppO3cuvkPxAgfQbXPsdZUwa5bf5TC-414nF0BAz_SQRKsNRx5rS0WTfzYNx-8Vguv4gNI-g_TkGVDYxPfYAfNlRtcNTnsxlr5oGWjfl7wkh6BaYscMMiBFaXEeDqJYHadBhPmBcvfVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی داش چیا رو که از دست ندادی
😂</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78957" target="_blank">📅 07:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78956">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">صبح بخیر</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78956" target="_blank">📅 07:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78955">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ژنرال خارکصه تو چقدر گناه کردی مگه خدا هم نمیخواد تیمت صعود کنه</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78955" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78954">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">عجب سوپری زد اتریش</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78954" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78953">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یکی ژنرال رو نجات بدههههههههه</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78953" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78952">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وااااااایییییی</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78952" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78951">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ژنرال صعود کرد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78951" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78950">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اتریشششششش حذف شددددد</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78950" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78949">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تاااااااسسسسسسس سومممممممم</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78949" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78948">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تاااااسسسسسس سوممممممم</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78948" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78947">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78947" target="_blank">📅 07:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78946">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این وسط یه چند تا آژیر و صدای انفجار هم تو کویت و بحرین شنیده شد که چیز خاصی نیست احتمالا حملات پهپادی سپاه به کارخونه‌های پرچم کرنر سازی بوده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78946" target="_blank">📅 07:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78945">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حضور ۵ دقیقه‌ای ژنرال در دور حذفی باز هم لغو شد.
💔
گل دوم برای نماینده‌ی رژیم صهیونسیتی در جام جهانی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78945" target="_blank">📅 06:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78944">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گل دوم برای تیم دوم ژنرال</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78944" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78943">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نمیدونم چرا اینقد بدشانسیم
۱ بار ۲ بار ۳ بار ۴ بار ۵ بار</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78943" target="_blank">📅 06:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78941">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پایان نیمه اول
خلاصه:
ژنرال ۱۵ دقیقه در دور حذفی حضور پیدا کرد ولی در ادامه به واسطه تبانی پرچم کرنر با رژیم صهیونسیتی این حضور لغو شد.
💔
#پرچم_کرنر_۲۵_سال_آینده_را_نخواهد_دید
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78941" target="_blank">📅 06:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78940">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">عجب چیزی زد بازیکن الجزایر</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78940" target="_blank">📅 06:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78939">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اتریش ناخواسته گل زد</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78939" target="_blank">📅 05:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78938">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این همه تلاش اتریش و الجزایر برا وقت تلف کردن و زدن توپ به در و دیوار دیگه صرفا از سر تاکتیک برا مساوی کردن نیست؛ انگار با ژنرال مشکل شخصی دارن بی‌وجودا...
💔
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78938" target="_blank">📅 05:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78937">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یادش بخیر مانوک خدابخشیان ۱۲ سال پیش خیلی دقیق این روزا رو پیش‌بینی کرد و گفت یه ژنرال با سه تا تاس بازی می‌کنه...  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78937" target="_blank">📅 05:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78936">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کنگو هم ازبکستان رو برد الان فقط میمونه بازی اتریش و الجزایر  این بازی مساوی شه تیم ملی جمهوری اسلامی صعود نمیکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78936" target="_blank">📅 05:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78935">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78935" target="_blank">📅 05:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78933">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0fsHwmdYMgfsz0NpIMbYD7DyE-pHquW1Dvr-bOwEqw-aA9K8tBjOjm90oUpQ7oY1Rc5kxFRJc7M7RHx5IkIZkd7Qi7MkftxfykXEK-oxCORCypAZO9mtosHGrKc61-15hBLnGh-rGHcdJidzVN_X_xQtFTM6mgazSIEiU4BJ7ADzRX_1OpE7QyQcORQUs0BnUHq3UlHHZiA_ApzozMAc8jZDc54NTDuOKIK4cMy6tZpDnl2FJ0SRalKKLxVLUHhLnlrL_p69oxQhTsAY_9SLUTiKeVyj4MB50s4RPjMohpIVoYiEEWtSFpTDy-LD6YayCTifqAuWAzVmMh4Xy8Zew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
اگر این وضع ادامه پیدا کند، ممکن است زمانی برسد که ما دیگر نتوانیم منطقی باشیم، و مجبور شویم کاری را که بسیار موفقیت‌آمیز شروع کردیم را با روش نظامی به پایان برسانیم.
اگر چنین اتفاقی بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78933" target="_blank">📅 05:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78932">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">چیشد پس جادوگر مادرجنده</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78932" target="_blank">📅 02:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78931">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">طبق تحلیل من آمریکا دوباره مخفیانه داره کشتی هارو اسکورت میکنه ک از تنگه هرمز رد یشن
جالبه بعد از تهدید های سپاه قیمت نفت هیچ تغییر خاصی نکرده و این نشون میده که همه چیز تحت کنترل ترامپه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78931" target="_blank">📅 01:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78930">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سلام فرید جان وقتت بخیر
ما بندر لنگه هستیم اینجا چند بار صدای انفجار بلند اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78930" target="_blank">📅 01:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78929">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78929" target="_blank">📅 01:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78928">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbDgWdBOWS4BZcEIyrBSwPPkgzrrXkeEI4HynnXSX3iCximTI4bZHlvOOLeBaYaHYO2WswLYKs6W8MwyxMpy7jJesg6hLdH0Mp1xgQLsI8cCssaMrInbXCJos4wMliYrtkW0Df1ZpnnDUc9qXwGSResfKWsyB45_R4bj6A-HqGEDap5qBjX8VJ6YLfn5bjmahh2B995e4hQnMr_qBFEhNOgUdkMtauzTMCMK452P93-pSMskh1l7JJHrb_4DRggcxcsFjgaULl6P-o3yDC6EbnRUGrUOfzvFcXcL_7OjJvq0BBMzDRM8NYDyF3w3qhGskY6J_GWOaHksbW_Hw5rWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مودریچ چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78928" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78927">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نگران نباشید دوستان، ذراتا دارن تبدیل به پاپ کورن میشن برا همین سیریک صدا انفجار میاد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78927" target="_blank">📅 01:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78926">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مودریچ چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78926" target="_blank">📅 00:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78925">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کیروش گفته امشب میریم کرواسی رو برا ایران ببریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78925" target="_blank">📅 23:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78923">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43122e124.mp4?token=ZxgLXH5ThWvXGCI9jrDnMtaR08AuWd0Ie4Q9N9fNyV2dMnKcbqkEAVX4SR_ZdbqS0VTbfBbVgJVq0OBEnB7jXhGtM1YN4arDLKTxISxBV0RIMSji6e_2bWBGQPSH53BxiNDewqWe_dO367CeQhfcKWM-MJPuMe4mDAeGjxd7nEbjBWpl1EL9-MBC1qGUsmO7F9GAW5IO7MsSEU8Cjh45fPkA2JMlm9UaqByNQ0fgWyMly5CaLHFryqrfkQflO3HqVIOe3aVmyl_dd68zrZvJ7UZMLa3azdluP8EkR5WSYyQPX8yBTm4x7ZmtgRRj7niu5zfIhqT_yG27mZEUqRxRQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43122e124.mp4?token=ZxgLXH5ThWvXGCI9jrDnMtaR08AuWd0Ie4Q9N9fNyV2dMnKcbqkEAVX4SR_ZdbqS0VTbfBbVgJVq0OBEnB7jXhGtM1YN4arDLKTxISxBV0RIMSji6e_2bWBGQPSH53BxiNDewqWe_dO367CeQhfcKWM-MJPuMe4mDAeGjxd7nEbjBWpl1EL9-MBC1qGUsmO7F9GAW5IO7MsSEU8Cjh45fPkA2JMlm9UaqByNQ0fgWyMly5CaLHFryqrfkQflO3HqVIOe3aVmyl_dd68zrZvJ7UZMLa3azdluP8EkR5WSYyQPX8yBTm4x7ZmtgRRj7niu5zfIhqT_yG27mZEUqRxRQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم مصاحبه شجاع خلیلزاده قبل جام جهانی:
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78923" target="_blank">📅 22:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78922">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac246bd5b.mp4?token=oAVdF98hzMALHSe64qZwb7hOurndhRN-veo0HgGOuNjfbXH60r9bPpwGq94OlehoNcMEFfSMuEOrSzlu1_7OWZy-W3KerbT2ghbAaoKBPs__gjq6ektif1PSD0bPm1VGoqAcdqNQgdhLHscurJodkI10sfT3I2GWBY2YG_okMyuahJsblPymzGTpkdkKGE7nTq5918YnVLtlIiWjECcd9mhJtzIk2awvz4CHnPgrPUNLoXgFdoTBFFCaGk1dgXD8MlJvcJ67Xvh96i67rJKvOvRAm3okd8EYjSsXUSAaxeAYFuIxBXmlGtVBtPgBj38axWpYJtJsXQcPPu0rHyGXWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac246bd5b.mp4?token=oAVdF98hzMALHSe64qZwb7hOurndhRN-veo0HgGOuNjfbXH60r9bPpwGq94OlehoNcMEFfSMuEOrSzlu1_7OWZy-W3KerbT2ghbAaoKBPs__gjq6ektif1PSD0bPm1VGoqAcdqNQgdhLHscurJodkI10sfT3I2GWBY2YG_okMyuahJsblPymzGTpkdkKGE7nTq5918YnVLtlIiWjECcd9mhJtzIk2awvz4CHnPgrPUNLoXgFdoTBFFCaGk1dgXD8MlJvcJ67Xvh96i67rJKvOvRAm3okd8EYjSsXUSAaxeAYFuIxBXmlGtVBtPgBj38axWpYJtJsXQcPPu0rHyGXWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر رامین رضاییان در مورد هو شدن سرود ملی جمهوری اسلامی
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78922" target="_blank">📅 22:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78921">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اینم یه آزمایشیه خدا داره منو میکنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78921" target="_blank">📅 22:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78920">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">همه ۵ سانت و ۱۰ سانت و ۳۰ سانت
واقعا این عدالت نبود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78920" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78919">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نمیدونم چرا اینقد بدشانسیم
۱ بار ۲ بار ۳ بار ۴ بار ۵ بار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78919" target="_blank">📅 22:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78918">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بهترین ترک یکسال اخیر دورچی ریلیز شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78918" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78917">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">همین امروز با رفیقم نشسته بودیم داشتیم میگفتیم بلو کیری خفنه بیارم قطع نشده و کسایی که ملی داشتنو مسخره میکردیم</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78917" target="_blank">📅 20:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78916">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بلو هم قطع شد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78916" target="_blank">📅 20:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78915">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLKyZLPYsuhjeCvd2sCA24FX_Kf4v94n6nEmTVUrPqWWH0pCZ02sbHbtoODSC8lmMpoGx6ZmUnIIjQeO4keC2KqqfMeNVA_iO8QCIKky4U_U8U9G_yfczGqer32smKWwZVXHHZkcO5XMT9EicQmBHNmS5oJ-DF7mE9ZV-0JjQfBv5v1dlmC3k5DYfnFtDQzbDHkl9sl4RKJmgI4762S52_bu-49lvMIe7m3cQ0qC70lDUXWTKxBDYzpH8aPTgHbbtr3FBFpjkXF71kdDWDkhJakaxXFP5Vz2yO16Dnq1tqeecuJ6JQRjU7xetLA2DGpkClJk4abLvHZLBhTPDjUFsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتفاق بد برای هلندی ها
فرزند تازه متولد شده خاکپو درگذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78915" target="_blank">📅 20:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78914">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRirUrho2ERdUBItqWRSS0WCIr0Ag41YSp2AqXoecWRMUwBzm6L9n1kl71EF6feN2FeD9LFRFeilGhZZ0XCZ53ELT31ufo9GK0aDleinVwlelkgeYXhshUpMEA4aTbuowlmdQLS7vzQbqMrV4bcCyBNosmr7-EaxFC9HxsqhOvrgawmeN6g8Xx45Pudyx9R38_lHrOufMr59BMsXFBl4IZSc5f9kgDZPVqgVzF1NQVmtsdajoSvl49nxt57jya5WrbhQ9RFKl4bJSILFx1pFu5w3eGwzSOHCmgULmq6mvo2Q-oFeOAaaZbNI96ce978APB_gR-sbYFKeaFHx3ebxEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجاع رو کل دنیا دارن مسخره میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78914" target="_blank">📅 19:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78913">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4kY3Z1APXCyeXfSfzHaRidzLsFKgjy2IXItXoPt3vZkVxfBZUDhKR1gVxRoO_WP6pbItT5BGnDrWJwfHuVItVZZLp3g6n33NoxJ7S94zHyMiSNlC2hZcRNDK-i9_hneBppDXjz5LPUnJbl_oCZ8JitKpUhwkgnVGBGAzyghV0S9a4VQiADuhxEUyT0oKPqJ02uLDdJfXxfc-St0sjt09z4CbMkCQvpqBtdvwpejqxwQEEao7LHleUC5-qTmVPc6EmmBph-HzemqibSKOANtn2ZuMozx0V2iMi_80iZW-UasoAtUbayMC2vW8N87CBivOCNlC09zd2fApr0MbobwRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جام‌جهانی هر بازی داره منو سورپرایز میکنه.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78913" target="_blank">📅 19:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78912">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JB_06CCGa35OADSVc0z7CR-YWJk8GnCGGkY35soOrTrGYbK6myVwzJ5PTONLNOvgYRu42PGX2XINU4floaQadwApAfF1MMc0rBPe90jijQL6mHlbiBHJNBDw6WV8SDX-A5BK3LA9rpfjU_TBQkAYzWFMrHnKHwwsMbH3EvAAFFlFBx_qETCKEsuUWD4yAFKTTB1utRTmqlReN0Sj8grj2g4vy_BLBoqOLUK6_YWvSDA52zr4D3fPsSH9tvSlTxBqgrWERLknnY6ehxr-8MI_vIudQvYAjWYzT3Dymx8vGiHAy7mYRC7kF7Rb5PFIJb4mvzIAx7vWBaHq3ZwFbBWHGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی گفته ایتالیا به جام‌جهانی صعود نکرده؟
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78912" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78911">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sh0cKTQ6oyoGyTtfpShTN_EcP1RqfRfeyLNuHebn3woGdF8s4LGCU7NyvnqIJCXdgT7JgnY_emK_aW4-84qeKHgsS2TO24KsiubI-9p0o4aYmOO0upaaH1p8R_eBt1UsEJD653UMMrTBqPgwwEy2YqBsP0tNcbJGS8EapZnuOZmZdQooFVmsi3uYjnrJEhcuYtdfiXIVN2WeRea4fDoAuiCUV-GPVomWvQ0fuLHPv_rFxEoKe3tRv8mZuDUxpxCw5HOBbcPkfXj6rzz8Jd_wAH_gSkXMXigmcWUBrINJKnOA3WMMfZ-7ku0VyLQHOkkAmLzARFaOlAJDgz5q7FUXaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">همه ده سانت تا ۲۰ سانت نمیدونم ۳۰ سانت</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78909" target="_blank">📅 19:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78908">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترک جدید حسام تی‌ام و حسین تی‌ام به اسم " West Side " منتشر شد.   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78908" target="_blank">📅 18:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78907">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLYgG--KGujM6cB7iUAjnyK2tuil_PwkIv_gnhoQFheHdQEjQCS0i7pGwsmKgYNpiFLlpF9TsLifwsOo86XOhf7cGvBLScEM1MjeoEzfVWThpiPHdahmOw9_v5dO72vUkb0qy1kMYuCg3kyrtx2w96Bw1Iv4yb0QjnIFAKXHeoaSYSCOcK74D9V_fUV2zNePX79UzC4AU0aOf8RGq0nGQd_poRr4A7WmJR_mbWywFooB5Go0oH1_cta-lwIi_lvZqkijEEtsImAeGCG-x7zWWIz_UsI5yXI0ykLrIN1Zv2d5O72EyQ-8c1MEcj8Nt1l2qzaz3IDbcK9fV8AONgMhjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78907" target="_blank">📅 18:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78906">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">موزیک و موزیک ویدیوی جدید مهیاد و دینا به اسم "ATISHSOOZI" منتشر شد.   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78906" target="_blank">📅 18:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78905">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0nvw8OZyHgNhv93Sxn4h8BBI2F-ge1MxoVELCZnOVpXcBhvISTLOxyHM86ktutpt0qsjzbPyHANIHHumXgtWIY_im2BhhMfguL4xk_SZMdxwIjZP3j1YdKBECX3dXPQyTDL3FjbC32gsIvrGMOD-Nb_znIzZ2bWFNjAKpKkAel10Y7gzHcljB-sW6B_rZX_Upeh5cbZpfyRRFi5SgC77v9A0MLaLjZdT3dyvUrbGXPy0eUlmkt4DoefHNhh-SRUQPHto4Xnr7loBN9o9jFdQBZk1jdLeDVt6tJMsy52lkThsbmE6NmSMES8ifOdq63Jv_sSK45jNHZ37KcIwE-YNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZVJNceb-OtWjlQMXwB1Fi1nFGtSIIGLe09PWj8iQBBUr-60Q0lhM-M3Nwni61X-bHrbvv4aP1hPsxzZ7T-w_o_CGNMjCpsoYrwQqqapyaYLqlQssd8Dn13Du1x_AF0bu05EyAC7Y9VTpwToJMIgG6v9JI-NO9ZWy_cEIA_L_rucpcR4FswEAeIx5bGEZIOCzkxM0f9FuGFcbfLkV6j9pL9x0kIrJ8k02JEZ2MQ5rioqon4pggrK-Rdz9-vSWEB8kyRK5rIl8lBguO3XGu4T-J5ia8NX6LRE8omsLLK425Y6w1-xtJODEaEq76T_fuQYClT_bUwJAnAXyh7bcf9Y9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78903" target="_blank">📅 17:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78902">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سازمان دریایی بریتانیا اعلام کرد که یک نفتکش هنگام نادیده گرفتن هشدار های سپاه پاسداران هدف پرتابه توافق قرار گرفته.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78902" target="_blank">📅 14:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78901">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsCC1r3TnseIL-VSA-sFM-bEMGGJobq1AfSefdKK9TJ-SUV8RFJtOgqMdMCUCPrF6eDksZaaon5ytucegwEAyhdD0-_LBjToRaxf8a1SIRo5-FsyuKRWtqcjobyOfqbVaSXCrsXxX34FwxIpLKhbQJRBbpwU3KE2PixGFmgNWCczSS92UE68S9a0XQbtt0i0AN6jgRGulET5Qx4LCWKfMRKCB0bSib0p87KaviowyWW9HTJ8j7ZMI93ezGKsnp6inwVSb8N60nYXBOqt4K0T4t2uT2wTApRYW2FWOgHT_R2XnY816HqGXAKSIMS7gnf5r4dblHTIbkI97zK341ly8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی دیوار فلافل فروشی توی بوشهر نوشته بود
خدایا همه مارا ببخش به جز طارمی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78901" target="_blank">📅 13:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78900">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4960c204ca.mp4?token=iy0bBsnRyU-FJ4fTo5HssU_dBrujD4eXKdLPnFF8rr0DrTNgZYi1n-u0fmW0lAHWU7tMAh-6WRnySTAPxgaQWBFaUD61GbAuO8G-w0PTNITfKw1U3v2SxgE8H6kw0SmwkTOsVcP6Pw6jLNlI0_q6e_HsIu7AOZMXmId8rcd7CLMxyQibTFCwTnmsjkKGW0K8sT2i0BGjfNqCrDrf5H97b_OuIxvm5_Qkw8mOm1WPpKq_7QUqA2ZL6dIf2J3uF5AKYhjSC-1OcsTbQdLvXmg5_UfxGlho0sY7Jtc4aCDhihV__JDvrkHfOLUflWJE0Z3r9Cc27-eGwcre2G84D8teZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4960c204ca.mp4?token=iy0bBsnRyU-FJ4fTo5HssU_dBrujD4eXKdLPnFF8rr0DrTNgZYi1n-u0fmW0lAHWU7tMAh-6WRnySTAPxgaQWBFaUD61GbAuO8G-w0PTNITfKw1U3v2SxgE8H6kw0SmwkTOsVcP6Pw6jLNlI0_q6e_HsIu7AOZMXmId8rcd7CLMxyQibTFCwTnmsjkKGW0K8sT2i0BGjfNqCrDrf5H97b_OuIxvm5_Qkw8mOm1WPpKq_7QUqA2ZL6dIf2J3uF5AKYhjSC-1OcsTbQdLvXmg5_UfxGlho0sY7Jtc4aCDhihV__JDvrkHfOLUflWJE0Z3r9Cc27-eGwcre2G84D8teZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کونکش دیگه خیلی رو انگلیسی بلد نبودن مسلمونا حساب باز کرده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78900" target="_blank">📅 13:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78899">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZFDp4Zlausad8Knfo5aE7NHRQDepyETR11PcqNdZKgwA6RDIc6bWBP_3AMG3ykykWuQ6P-8YK7elnRPXhLry1gxY5Hgr0KIHxPr5pMgSrhHUe0XPJdafq5YzDsaTNopcFNiXZnWOlP03gi2-3-GXPxb0UKTecx-Jal15ZWBK71mqu-w1WtCFHGuoOago-wOMRYX0rVx4THyeultBfsHQ8B3fqptsUGhIpj-6QMdsIGO5PtHh_XNJRlhPErKD9ylGcY7PkakLViPEUeVTXhdVWkAL_ot_vPhaRYIU2dGKkXWHUL8qShJY0taKkqyGIqLvX1R72i_XNWbX4-hSdPMYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی به کیروش زنگ بزنم براش آرزو موفقیت کنم فحشم میده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78899" target="_blank">📅 13:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78898">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">من کیری خفنم پسر</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78898" target="_blank">📅 13:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78897">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi🇵🇦)</strong></div>
<div class="tg-text">من کیری خفنم پسر</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78897" target="_blank">📅 12:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78896">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فک کنم تتلو کل درآمد یوتوبشو میده برا قبض تلفن زندان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78896" target="_blank">📅 12:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78895">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تتلو چند روز دیگه موزیک سومشم میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78895" target="_blank">📅 12:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78894">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZHvS7E5fupWlmnDWaWOcIUZRmRaF7I0fZHYF2j9DZpuoZKLr8lubFvE5uImG4c9XHjUYiPYhGYsUO06djDAXwEWC05G707rUJ5rZojEh2-i1KoALKcQxiixBLy5rPpnSxB0G-beWJKNj5MOLi-PCxMFUh-2slottQAI9pg5Bx2Db5jk61rVrm67IXjPMTuQW-0pf5F9qnH1WSx-y2s0uG-bbfzBUUBarqr-edvnPWQh1Ywlaay9xkyNjqPGEczhKWEHn-jzQaG9i68fyEZpKhP8YbDZXg8_x_XTudh8nstQmWBWNoVUBxXfsW4uf_skfskBLV0Fc-RBBO3J7srDQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقد گفت بدویید، دویدن همشون رفتن تو آفساید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78894" target="_blank">📅 12:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78893">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncKSYgo4PdoE0sY1G1pe9D65m_SRNfpTGkTXsXOb2qLZ_WzDMqBxOBW507BQXlLHyA0SpgbsBtGog64JPJifbLrXdKI5RokxqeLDs0n1OrXWIxMGF1Y73z0WOttpBNDtH1PyRDt4P-pD83jUghzt3fe_nmc8altjgAKIOvHpBGfYMVfYTJmxBr_sfOL7uerT3n2wCiW8Z4bBybhj_pIj7yuYWBSBWGXZAzdbTXfq-LFiKwnlMUS93qTqDLqxbj6HSVi1_-ELcU8PLB9oMPEVpc8EpEa0j0D6OWHExZRy4id-4LUs_V59RSVKDB4KOAEEGuFJvhcYFuI0jwecOUKqdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2s-F6jdWzlXZj5NyF8wYcW5jZVXnEoJxrlrrbVvCNdqJCb_hWBt71rGD1h0fORPcS9xlJlY_BRcz52hv_a9V7UH1IMuSVD8r0d0-8hKM_UArKnYxnQa5skTcBdyS21--19HwBBsGDgcHF2m_5v7qVz0ctWsw2h3kY9I2dx0pAEWfzutIjxdSrpFT_jd5-5MzWiRTJqRF0pALm1W1ROal7f6Y5hGvU0IMus-X0gg0hoyx3oQFdRFAAvic9G6dJLnHSjT_f1sVoi7qDi-MNrGqxyMClg8YCIvsxlbnPlOtlMefbVUC4t4yhhCngRGnN2eSdzz7xkcaYuVdaXdlivc9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثکه تیم باز یکم خوب بازی کرده و شانس صعود بالا رفته میبینم یسریا شل کردن خوشحال شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78892" target="_blank">📅 11:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78891">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حتی اگه این تیم رو دوست داشتم و حتی نتایج بهتری هم میگرفت خوشحال نمیشدم.
چون هرچی شده باشه از رو خوشانسیه و هیچ برنامه ای پشتش نیست و نتیجه ای نداره، تیمی که برنامه پشت نتیجه گرفتنشونه مراکش و ژاپنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78891" target="_blank">📅 11:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78890">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مثکه تیم باز یکم خوب بازی کرده و شانس صعود بالا رفته میبینم یسریا شل کردن خوشحال شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78890" target="_blank">📅 11:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78889">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سلام دوستان من تازه از خواب بیدار شدم مشکلی پیش امده؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78889" target="_blank">📅 11:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78888">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">جدول حذفی جوری شده دیگه کم کم منم دارم به مسی شک میکنم</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78888" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
