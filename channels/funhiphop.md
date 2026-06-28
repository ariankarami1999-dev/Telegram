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
<p>@funhiphop • 👥 188K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 23:20:52</div>
<hr>

<div class="tg-post" id="msg-78999">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نیمه اول بازی کانادا آفریقای جنوبی از کل بازی پرتغال کنگو خسته کننده تر بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 893 · <a href="https://t.me/funhiphop/78999" target="_blank">📅 23:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78998">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مثلا بازی با سوئیس بره پنالتی و بیرانوند همه پنالتی هارو بگیره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/funhiphop/78998" target="_blank">📅 22:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78997">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بازی امشب میره به ضربات پنالتی
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/funhiphop/78997" target="_blank">📅 21:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78996">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThBhZG6FqZLQbb6Bau8HnnfeESGSJaKdADqbphhaMDxOG2IS1xXqQK_REr7UjmZHZCZRGSWqXsrjBdpJdPxzSmtbLtndE9SqfV_mzv8a9I1dEyERNljBs6LxIl0zsByUIPhotffzzJFM4DWq4uRag491KYpplhWRtCqRVTzsykrwvMX0c6p55lvJyueO08770Zg1WHP3KoJmuv5_CnkwJEQ7q0Atf1vLUXsImbCLHyZtKKbIEOxnPG3D9iy1J-_M5uhlyzqgZgMPdax8vjkjnvHFKCwtAmfKM6404as0ycveKpmRwypdeq8kPm-Gkv8yZ1urdmb9NMsFb2sVRFY68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگیتونو بفروشید بزنید رو صعود آفریقا جنوبی، دریک رو کانادا زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/funhiphop/78996" target="_blank">📅 20:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78995">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t73CVhWf77goagBvec5s3vQyK65IL4ZUcbK0wBxUBt7ykcvBIU5OtWX3n_JcirONpYA72BmXyMprqEuwuwhn44fx9l1MYAAPfzGsJ-8HIXTYETfAmowTy-4mH-w2HSX6Dcy1zp1oeKuVd8ry_QgwaStkIl6SMGUcAP6MG2USJSu6xExwO0S3wcskIRPyaxwf7F6fppqbDvK9E1t2wurY8bTjC_TulKXGSLIOPdMmzAemgCe_khZ3q3B3keLoya6Xpxs42m_g3Jp_4M2Q3ps-lp_dS1coAx6nYVup0Ru6j7xZQ0XU6tdwioFu1hu-OyTLFZhgIHfeXe10lnW2MXM4Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو افشاگری جدید برنامه Jeremy kyle مشخص شده این زوجِ گی بعد از اینکه 3 سال باهم رابطه جنسی داشتن فهمیدن با همدیگه برادرن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78995" target="_blank">📅 19:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78994">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pncOUK2r-cbCs8j23i0u9j-vXABV1PDabbmnADiLnSRMw6RblowX8Kdvw1yF9R0mIrO942aGNtEB2tlE9U9NzwOHvdGkNmEkHWzgoPMh7hr_WaXDGPBKTXbMQWLUkn6vwpShgzebLOQQput5iRaUzEznymx6G3VgfH1AbyBdq8y4258iQI4LyLBo6LkFWOJ8oYyD1m9PDNpyxapwefU_2riUE4OYSe8j1iRCQJHi5aJQzNV8ugLSoMUXPfJ1jmDh6YLYBlcGTfv6hb2MPDHtTNGvafLxVp78MkXgey_4Niwa1KV-2C7QGhX3_i1iPZw-BfRGm-7vbr3jnoDNhHdd3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب تکست کصشری داره ترک جدید پوری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78994" target="_blank">📅 18:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78993">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-YVSj6gsbnp__vNiuyYYLArn3ARn8bRLADZ18QINDGFKUyRvs3_UTBMM0EytlVsIx1CSGyBMAE-7qEmOzF-D8OrPd8kUv9F_Hoy3LhckjtxEgarPD--cnso107C4oF6TBaZhCEXgerdRjsGyTDm18QM_uoGMk2wRwvn7mxf_e2D40A2QIHU91N2r-2MZKSvn0zwtzHAcZM5C3NP9ZUwwFoSPdpV5iyEzAXf0lSYC_ca6j-iJzNllFHZvn4LlC6gSusnK-bQO_LOHFzFg71lIPWZPXH2bd3pSpL4CE7sWfBTWDRX1PvrZijKxnBIW6Yv9AJfo53DEgNgMoEHflpV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید گوگل و تبریک صعود به مصر :
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78993" target="_blank">📅 18:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78992">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78992" target="_blank">📅 18:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78991">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78991" target="_blank">📅 18:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78990">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tP5SI1lDSS3Z_zCquetUvg8lSfMknk8IgLraPl7Wj_fLXmMXl8C7Q9iz5QT0jWwu0iuOuxiFGUplke7YmJwsH_Jy_Vt72jEdGwc6XmCa7nFnzxaRgTcCnJD7E1fFPRaP99JFNhPwLzFhXhTThjEmA8XLDk6Dp5k-COE-A9DIUCIbUD4L5Cr_xHSuPrANk9qSFN_frtxRVn-JLaDWfD9bTlrnkpk7hXFK4h3-SOm_KN-Vi4hn5XN2KVPLOv03jQwDQ8oQcoX_g0S9xWYnFQLQ7aIv76ub6RGnoHEropBtjmuR6loXdUcTyCi5GEZi_wQtaG54e4h3ePhPNpyEPdR7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری کوروش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78990" target="_blank">📅 16:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78989">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ایران توی جام‌جهانی : ۳ بازی انجام داد، با ۳ مساوی ۳ امتیاز گرفت، ۳ گل زد، ۳ گل خورد، ۳ گل آفساید زد، ۳ تیرک زد، رتبه ۳‌ گروه شد، بازی ها از شبکه ۳ پخش شد و برای صعود باید منتظر ۳ بازی آینده بود و در نهایت با تساوی ۳ بر ۳ الجزایر و اتریش حذف شد  @FunHipHop…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78989" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78987">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTDSLs9OErkEwS_16p3ZmZkb3nXEbMP72lT_ORmouReOakZEXW2YHbl7KOWG2IfWVGIpG9IukK4Nwuf1GT4YuIwbP8Z8FEjzLRKMNaAaYgTpz3LOSeetXFby-v3lxlV-MnJRzRauSx5SGe3Ob7SgxszWcOTQ8kHqn6sN9tNhZcSW4wWA9dHUQiBaJ0gBuco21kbAZN4TkB1XMn4XFrrAroiwyCB_fMo6tQ_jpXAQeJYErzSOEkXGHNa1MHcPeyVcnnMswh3mLAV3TPOugd9YablNHy2zKmM2wNl9XecqhAwKhKhk5BuzYsEQ1x3asuC6Nq7zJL0Zx3WCTgGZwX-HvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز خبر اومد که رئیس‌جمهور عراق یهو زده به سیم آخر.
یه شِبه کودتا کرده و با لشکر کشی و تانک و... حدودا ۱۵ تا ۲۰ نفر از وزرا و نماینده‌های مجلس عراق که اکثرا حامی حشدالشعبی بودن رو دستگیر کرده.
با خودم فکر کردم که یعنی چی می‌تونه عامل این اتفاقات یهویی و غیر منتظره باشه تا اینکه با این خبر شاهکار روبه‌رو شدم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78987" target="_blank">📅 15:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78986">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm49WzfS6ClAYOjKfWUA9DxOONoZzw4v7Ft7_cWcJ_BO_itS2pIFLSmHLkA9cSWRT168ZonqFHDXTApH3gmOp12kDqGblWI5SYPwyuUlwapgdhrrElUn9A0Db5wgKLfLh_2TjjYlBDyjJnpHEjft-Km1fsxdrboyUWj_YiaSUu-a3rBDlvmtH4QM2fHeKc9hVD_KJ5BKX-JJIrlIqgwzpOrKs8k33beFLPHLkL4WQdGJeaW0qmzsO4ypneUKw8NoTcK7ZrB1K0_rR5dUM6xGplKBeQu0CoQnROQvHgvBDAlyK23ygZ0aOiZpqtM2Xd6b8NE1Tq5P3L072DXGFFb-RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری میثم پیرفلک پدر کیان پیرفلک عزیز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78986" target="_blank">📅 14:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78985">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1wDyK_bzi88r-vMYKA_WKAODW88A36EcHhEM14kKm9DoWAOFlkjVP0gcrDOaQu46ipLZ2SZTIFC3MCCUR8GtFTpZQsEuRJpAx4fx4ZIlKE-_E6jQxuh4BoTSgpsvzHBTMAh_JBGMgf-fvY7GcwXyoWmUwnfHpeqYCarCIIpjKqz2S93oJm1mAMBvcM6iqX_aE1GP8ZoouVjs6daxZXqfD3sr6op-XIhb79bJaS6jcVEUCpdb9qaBnKUfH9Mz_3t2m0pYrZG6XIxEqxS2FGtF7UncO_mpqb6q4_nKv-FnGgfz_j4rpn845btCQg4rfRVPI8tLLkkovuKnHID9Jg9ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیل زاده ببین کاراتو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78985" target="_blank">📅 14:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78984">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78984" target="_blank">📅 14:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78983">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">"من برگشتم" رونالدو مثل "من اومدم که نرم" یلس نشه صلوات
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78983" target="_blank">📅 14:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78982">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">جدی چرا چیزی از ارزش هامون کم نمیشه هیچوقت، مگه چقد گرونیم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78982" target="_blank">📅 13:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78981">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قایدی زن جنده تو که قرار بود یه دقیقه هم بازی نکنی همون نمیرفتی نمیریدی به محبوبیتت دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78981" target="_blank">📅 13:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78980">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اوووووو رامین رضاییان اووووو رامین رضاییان</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78980" target="_blank">📅 12:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78979">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-LeQTdPjU6yfkkjc3cQispa-YzR1RciA6hBKakqnxML2lePocBlVNXeVqAwUvifS8IcyQ_okf9abf5ef5pP4NsGmT265bmzE-SNoYKUe39Meqmq0KfEt8Wkcju7FESzIuXnQkFLUB0Le5UakJ6RrlZ_RChW6d2mv15bLiqq_s8IXnIFRR5UryeRV37MYgwbwWl94OSXjTKCvdXjbgkNhPa-WT08gFiKiSO-iQovnFi0rx5be5EZJhriatvCQdu9fHzrhkO4rvUyfo2f5BQ3NAA9cU3nCXOGwyffOR-ELzoamLRTKmkYXXHPZJtrA0D9dny5vn4tXqs4x9_8tH6KKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند: مسی هیچ‌وقت قرار نیست بذاره من کفش طلای جام جهانی رو لمس کنم
😭
😭
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78979" target="_blank">📅 11:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78978">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سنگال با دو باخت صعود کرد، ایران بدون باخت سقوط</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78978" target="_blank">📅 11:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78977">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">همه دارن خط حمله های آرژانتین و فرانسه رو مقایسه میکنن، ولی بنظر من کلید بازی دست انزو فرناندز و مک آلیستره</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78977" target="_blank">📅 11:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78976">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esT099IJ5nPC2lQVfduzUKKYPwpJqQ10DBoMCysaDW-qX7r1rl7ceSXhPmiJ5Ahwq_PzkT1Mvr-mu3y1vkP7sO97CwM2O7do7agwcZkobQz95Vj2LeMMYAcaVsMOBjLCTqAX-fgHDRvdxN3gd7A1X5zcfmBXw7zbS7YTxbECnJwUN2-b5f3QBtjVDIoiKYJ80CspIJ27zfdYsBfb6F8bXhpnCXIrfulfcVvAJgumSVNpibJW6D2MQiaGPjhQDaj8BJgdX-Pb3RhlZFFHBV5CcCwXGs_z71U5lF3HFJhMTIfA6mDTcbHevRtL96vFdWv2b_UswnQG44-vDprkYThFJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا خود فیفا هم نمیتونس همچین مسیری تا نیمه نهایی برا یه تیم بچینه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78976" target="_blank">📅 11:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78975">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هفته دیگه قلعه نویی میاد برنامه می‌ثاقی میگه فودباله دیگه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78975" target="_blank">📅 10:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78974">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbdEngTbzTArhGBmXYOkXPCG8dpiNQBS49xnInCdcuXxjlVHLz4ItLWeovM2C8F5Zphy63t-wCbQMBL8hLVqXp0uWBm8h6DOvKppxSdaCukCrMzJoOzIPe6w1FU_3snsu1YSFZglknGgcnxmnnf5gqjSDHC6yGZcK8vyCnlaU_cF0plbiRCeYVC2PqPQ8qIJmdd_fsE2zKEg2V2pUPW93s6z8uDSvYiysdbCXtEja3iu9BPaaKotg57JMwf1Nri7sOo56fr2qHj_2GcJ20SGEoYlTZQamtL8uhvfYL6Tj_aO9Mq__pXY0mxc5GWUgLtpKhbNlFirgQ9uuhswDbD01g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب یک بار دیگه پروردگار و اسطوره بی همتای فوتبال جهان، حضرت لیونل آندرس مسی نشون داد کت تن کیه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78974" target="_blank">📅 10:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78973">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78973" target="_blank">📅 10:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78972">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRUBRh3S3x48lsp_naxLt-WbthsekUBr5BVUmkWR7oiitbqUR1HTP_23Z5dFP1qIvWGrA9EspoMrCDrGVhq678nr1LyF1nnsbnx5_6prSoshm4xfJ2YsmX8zM08yp13Smz-S753AJa7sWwe2evnx-RNuzSLoTkfpLZnvghw7j5BKlDwhCF0PSNDWgf9YNK2UXh9KBSvS82g7vFH9IfxAoppxK6mzMRPFqYjBSKfkcfMp3mzS5RJPTm_2gu9j5CT4HdazkBvCv9KGBP1WR02gL589_2JdUPcp8qBO9cl3s6SoWb4zJI5CJaBO1kbdcXnqjx9kFtRR6T8c8c1P3pQC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران توی جام‌جهانی : ۳ بازی انجام داد، با ۳ مساوی ۳ امتیاز گرفت، ۳ گل زد، ۳ گل خورد، ۳ گل آفساید زد، ۳ تیرک زد، رتبه ۳‌ گروه شد، بازی ها از شبکه ۳ پخش شد و برای صعود باید منتظر ۳ بازی آینده بود و در نهایت با تساوی ۳ بر ۳ الجزایر و اتریش حذف شد
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78972" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78971">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78971" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78970">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ers-B1_5cV3t4U8WnJK_TqRdhk2jN63ah3lrVSJOiPSfGE-DSubAW5YsrQE5Q1txAWkyjIxeA4D_cbz9Bkl9d4kNsA287Maknnvfh5sBK8Au_D8z6fqhI6wONu180cqmDzNP8Uc4oiR4G-gOXQe-PekMi3lIf7SaGpF4EiGYy4FP0MeHmNWUwstLsTwqUAoztUkqC1Fic5VnKvTVUQVouL2dPLOcWOxh8TKklGG3S2Y_HNX-Elj2vGDPa-6epLsXXG4qXoQzbU2APgLiOU8wsfGgOQyo06yD4JxMLavGVl2-96w7ZbyqjN1uH0ipSW4X15c4G7f8aLlx0Bz53dPmBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78970" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78966">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سلام بچه ها من تازه بیدار شدم، بازی ایران سوییس چه روزیه و ساعت چنده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78966" target="_blank">📅 09:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78965">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">با ریدمان پرتغال جلوی کلمبیا، پرتغال، کرواسی، اسپانیا، مراکش، فرانسه، آلمان، هلند و بلژیک همه رفتن یک سمت جدول حذفی</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78965" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78963">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOOEp5QcwG5o9VAlcthqpxM_0iT8eC3-KRKUhwDATBn3gxVm4o-H6zbjr-Vp43VNMHhsXIwT0om1vg1le5Mn2j028XHoz6F_B-aT8qnmrK2vdNqVImzVO4akbITKnNmw2Mbc3TyqSVuAC5lzo9xeAZWW6ilQozUOVzG9ALouTjsp3_kauVXAbm_-zntlCNixVpAjs97YRT_u3ZYv5TxaipkGOgpridTdwwATj8NlB_s46nV2qIUfhvp_3LMwXsH9-_KDU1ltgRqZ7XZ2maZy2wwfnWorEuS9GdLMcqW6hc6DYWFqjYWNC6VclW3-0N360vet59Nun91Gj8QH-46JeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v7fUQZOj0Qtdd3tOoaUNHtEveDI6MJ9d-dvBOzlApshFOx9xaB5da2p0jdqL-5hIPd5DcTrH7dlVYHXb0x0suthN93WAu8BKtPut80klwZSmoOXUUg8e3MB7b_MCrappIIycD9SAwUiiPI9f9w_E2CzsNdc-c1XvLyd6PVZPYv8FLXAmi88m7MVMfnZqy13f4xz89JZyEIhQmxzYjvlciF8E9iWjR1r5Qr4eUpY15eLRKvn4bUE5vO9H5s2vWDi3ULlLzmWiAMiDlkExU-yEO6oXs-m8thZcBarYniC4k4pnWfIQcMlxnY0aWwBZqebNiXltl1v0MZNV9kcwU6qD4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من برگشتم !</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78963" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78962">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3ngg55BY7FWh7XmEBuvL8mv2N315vsnK60Bpz7KiRzs90vFnkk1I_bCw6EzVg_cOgpvP2gGF1N3jXjkgIfZqREyaoAA3Uwte5FSpvAXl8vNuUVTppfwxRT46BEcKCekV1wYhHH0gmQdLau3gufascsevi8UVrExwQQfBSx3k5WnUzgOQ1-UfXpRhHhBKIAM022wuBEh41p6HZl2_gxFIw-6fQmaNuKu_nN9tLIBgMf6EZa8BCia_KxU89AK3JejkCM2OrIjr9CHdP_emxNWhfQY1LgwQbvxJiIPygH8gLUAe5YxsL5nNy7-ea3WPi5t3M-RCPM3dJAKgvmp6FsF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78962" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78961">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">احتمالا نیمه نهایی انگلیس آرژانتین و فرانسه اسپانیا ببینیم</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78961" target="_blank">📅 07:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78960">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa8b89a24.mp4?token=vXw7hS9mmHR4BnIlz8SZwpp8qbuPoNkUh8x5ZPqhHX_20lvhy2y7KGbF89NTj0yWqRj0dLclSCsNVFa4AJdD3yt9kN8wWnxgM2CEr8kJQ9fI8HH8BeJ-d9J-d6T6v-j82boSF65WNKB-97JlXvyGVE_7b4a3ONfOns_f7EBUQKLau6G8ROnZ188gVHR0YZRjAMdPlhFlTdWTru9peYvN_LVLzsRIoUwTAU0mCyUzSLbBFrOh1-Sn4PVDcDtmAmgVQUdRwcYrNIbKmJ1hynOaxX6goeWmvjy1lkffJe9jZl0zhfzxt1k13NCFSPNgaTtUngmk7sXZ0WQcl9i5gCacLzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa8b89a24.mp4?token=vXw7hS9mmHR4BnIlz8SZwpp8qbuPoNkUh8x5ZPqhHX_20lvhy2y7KGbF89NTj0yWqRj0dLclSCsNVFa4AJdD3yt9kN8wWnxgM2CEr8kJQ9fI8HH8BeJ-d9J-d6T6v-j82boSF65WNKB-97JlXvyGVE_7b4a3ONfOns_f7EBUQKLau6G8ROnZ188gVHR0YZRjAMdPlhFlTdWTru9peYvN_LVLzsRIoUwTAU0mCyUzSLbBFrOh1-Sn4PVDcDtmAmgVQUdRwcYrNIbKmJ1hynOaxX6goeWmvjy1lkffJe9jZl0zhfzxt1k13NCFSPNgaTtUngmk7sXZ0WQcl9i5gCacLzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگری که میگفتی عزت اللهی رو برای بازی بعدی از دست دادیم، بیشتر از همه به تو خندیدم حال ندارم اموجی خنده بزارم</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78960" target="_blank">📅 07:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78959">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یچی میگم نخندید،
تیمِ رنک ۲۰ فیفا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78959" target="_blank">📅 07:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78958">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گزارشگری که میگفتی عزت اللهی رو برای بازی بعدی از دست دادیم، بیشتر از همه به تو خندیدم حال ندارم اموجی خنده بزارم</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78958" target="_blank">📅 07:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78957">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKPRQglAMK2kODTjJzc4o7_xORf9Q79NV5e3Ozv81Z1YoKVydPXb_h1HM1Gze8vfjSIJJmJ4B95M5hS_hDlpBRjr0hLMZRQ2S1k4X88J7tCrQZOTpUlhyajvM61SRZr04UOKa2nPRfCbps_6RELsgujzuRJ-zNryoH4PCepTK3RoBdUdSOuilxRmQTzKfTWPX7CIjgC2ICHW5VIgEmYsj7N2MpfkolcJ6KKMzzdzfdtBbRFg5P6qHBHaMkhFiKFXDmdyBT2lXHpm_amqONiMP1wknU48t4K54H3cuEBG_ZxA9qtH05c044y7Em_xjkZ13CT19xATUdvSDvaehWScsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی داش چیا رو که از دست ندادی
😂</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78957" target="_blank">📅 07:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78956">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">صبح بخیر</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78956" target="_blank">📅 07:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78955">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ژنرال خارکصه تو چقدر گناه کردی مگه خدا هم نمیخواد تیمت صعود کنه</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78955" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78954">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">عجب سوپری زد اتریش</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78954" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78953">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یکی ژنرال رو نجات بدههههههههه</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78953" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78952">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وااااااایییییی</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78952" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78951">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ژنرال صعود کرد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78951" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78950">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اتریشششششش حذف شددددد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78950" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78949">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تاااااااسسسسسسس سومممممممم</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78949" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78948">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تاااااسسسسسس سوممممممم</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78948" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78947">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78947" target="_blank">📅 07:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78946">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">این وسط یه چند تا آژیر و صدای انفجار هم تو کویت و بحرین شنیده شد که چیز خاصی نیست احتمالا حملات پهپادی سپاه به کارخونه‌های پرچم کرنر سازی بوده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78946" target="_blank">📅 07:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78945">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حضور ۵ دقیقه‌ای ژنرال در دور حذفی باز هم لغو شد.
💔
گل دوم برای نماینده‌ی رژیم صهیونسیتی در جام جهانی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78945" target="_blank">📅 06:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78944">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گل دوم برای تیم دوم ژنرال</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78944" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78943">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نمیدونم چرا اینقد بدشانسیم
۱ بار ۲ بار ۳ بار ۴ بار ۵ بار</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78943" target="_blank">📅 06:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78941">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پایان نیمه اول
خلاصه:
ژنرال ۱۵ دقیقه در دور حذفی حضور پیدا کرد ولی در ادامه به واسطه تبانی پرچم کرنر با رژیم صهیونسیتی این حضور لغو شد.
💔
#پرچم_کرنر_۲۵_سال_آینده_را_نخواهد_دید
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78941" target="_blank">📅 06:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78940">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عجب چیزی زد بازیکن الجزایر</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78940" target="_blank">📅 06:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78939">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اتریش ناخواسته گل زد</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78939" target="_blank">📅 05:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78938">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">این همه تلاش اتریش و الجزایر برا وقت تلف کردن و زدن توپ به در و دیوار دیگه صرفا از سر تاکتیک برا مساوی کردن نیست؛ انگار با ژنرال مشکل شخصی دارن بی‌وجودا...
💔
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78938" target="_blank">📅 05:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78937">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یادش بخیر مانوک خدابخشیان ۱۲ سال پیش خیلی دقیق این روزا رو پیش‌بینی کرد و گفت یه ژنرال با سه تا تاس بازی می‌کنه...  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78937" target="_blank">📅 05:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78936">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کنگو هم ازبکستان رو برد الان فقط میمونه بازی اتریش و الجزایر  این بازی مساوی شه تیم ملی جمهوری اسلامی صعود نمیکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78936" target="_blank">📅 05:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78935">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78935" target="_blank">📅 05:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78933">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BF1_2C899tDIv_J_Sm6ySQb30iVABT9b2Vk4qfeBcviAk-LXpYO3q2wuxQEVIUCHNO6hpIKMBK8O24ULUZ25d2FfQ8Ct74ntm2jHavmeAUhrmUwvilO3QbGRc0ERfx488zcIrFQwrlDYL32ssIL_ZNlxDTWxcAW1dIijX8YDgX1VgS95uwP13LdYWzIcwF_ggt-0zXdTwe7VK_wsLRM-HMZQdG-a6dGchiiyD4CXIEB-F5wwEHxJ0pGtfTJDDeODeVUh77Jz0Wc0NxnUjQlLSG3F0_-0_Rskdd0u2YkLQYMVdk6TiqjMcXbjaxjEDhc3a79sGsq2geZoWWQBN4Mhnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
اگر این وضع ادامه پیدا کند، ممکن است زمانی برسد که ما دیگر نتوانیم منطقی باشیم، و مجبور شویم کاری را که بسیار موفقیت‌آمیز شروع کردیم را با روش نظامی به پایان برسانیم.
اگر چنین اتفاقی بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78933" target="_blank">📅 05:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78932">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چیشد پس جادوگر مادرجنده</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78932" target="_blank">📅 02:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78931">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">طبق تحلیل من آمریکا دوباره مخفیانه داره کشتی هارو اسکورت میکنه ک از تنگه هرمز رد یشن
جالبه بعد از تهدید های سپاه قیمت نفت هیچ تغییر خاصی نکرده و این نشون میده که همه چیز تحت کنترل ترامپه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78931" target="_blank">📅 01:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78930">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سلام فرید جان وقتت بخیر
ما بندر لنگه هستیم اینجا چند بار صدای انفجار بلند اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78930" target="_blank">📅 01:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78929">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78929" target="_blank">📅 01:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78928">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8EswLy6PZa71vNEwcu_kCdhACnAWUKqDfB0Ld2Nlegd-hafbo6VYDQDoFpRZyvGz_jXIxQ-xYSG8avFNJWi0g2biPQlz9QRPcJskPqdJuidaJNNbubcbLOzZlcyycdmCAE4DzQc0nk8EEInBWVuKj2lalE_kPBG_SARHNQHDeyElBLRo07hy0Vdaa0uHlMyBbZny_HG2VUbS5qMpacuuXiYzKbiTmIJVDXOf8rqmn9D80iR89mz-I0t_3565OtBel-5vUo4Wy2NOiwUk_L5tsR9Q5bCSXLXSKqpgRNSV5aRYnt4yYbk732dSsPEMhGAMzOrNdZtyPO9JxemPvE-ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مودریچ چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78928" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78927">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نگران نباشید دوستان، ذراتا دارن تبدیل به پاپ کورن میشن برا همین سیریک صدا انفجار میاد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78927" target="_blank">📅 01:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78926">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مودریچ چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78926" target="_blank">📅 00:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78925">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کیروش گفته امشب میریم کرواسی رو برا ایران ببریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78925" target="_blank">📅 23:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78923">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43122e124.mp4?token=W3k-bPZwDDUrkt6ZTfzD9lJ8lU0Oq6y_ygdc4EbYg-a7qRzJJibhc93cr89nbMxuBLwOv5-6zNSu4JxnIpsdtrwcd36Elm2FRo4M4U_-iOPa4z-H3JZriP_7alcMbVvjlld4DY1qs49comc0O3X25LFF_szFMhPFQX6tTTjcm0dLcsUz6HUgge1FJPjc_n8ai3UomCBpxlxndZl7eCVhiY9KfztoHxcJ4_zgjOCRTfU_Tn5WPTdWrI__5GLDKiJqUMPAZqtYCKkKnKn5RQtLJfYFXPjTMbn4cYHmExkwOCHzdhGXivviSzHI3V0_V-1kMQQedBPxcKraaxEJhTyxzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43122e124.mp4?token=W3k-bPZwDDUrkt6ZTfzD9lJ8lU0Oq6y_ygdc4EbYg-a7qRzJJibhc93cr89nbMxuBLwOv5-6zNSu4JxnIpsdtrwcd36Elm2FRo4M4U_-iOPa4z-H3JZriP_7alcMbVvjlld4DY1qs49comc0O3X25LFF_szFMhPFQX6tTTjcm0dLcsUz6HUgge1FJPjc_n8ai3UomCBpxlxndZl7eCVhiY9KfztoHxcJ4_zgjOCRTfU_Tn5WPTdWrI__5GLDKiJqUMPAZqtYCKkKnKn5RQtLJfYFXPjTMbn4cYHmExkwOCHzdhGXivviSzHI3V0_V-1kMQQedBPxcKraaxEJhTyxzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم مصاحبه شجاع خلیلزاده قبل جام جهانی:
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/78923" target="_blank">📅 22:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78922">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac246bd5b.mp4?token=YfFFKh5u73P0iEhkJ63Uc7khbUvf82BgNIk9A3unj22WrHwUjuFFJPUuiYSe5sLvXevs5WM8eSb549pbd5UTFKrLrMJyE_Sh8zgpg0a0r-MDiPOnbQo_isTIq4qh6_BaWI_H1LYC7ehK2oDqqF6vKxr-S9vgeIEzmYG5uA5DzzHIKetCWsmGCM27X2xHjQ17KmxUZNb4kMLanAkB2eyisHRfs1Ppf_9q_OdeWIeoavGx2VohqBXA2GxSR41AvC86YnfOBE-B2U5TafRZOz43Neh7u0g7FsWeTX4docM3SyQ2CwxmoiZ37YuYeMhwmKXi502uf-73utX3ttg0tgznWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac246bd5b.mp4?token=YfFFKh5u73P0iEhkJ63Uc7khbUvf82BgNIk9A3unj22WrHwUjuFFJPUuiYSe5sLvXevs5WM8eSb549pbd5UTFKrLrMJyE_Sh8zgpg0a0r-MDiPOnbQo_isTIq4qh6_BaWI_H1LYC7ehK2oDqqF6vKxr-S9vgeIEzmYG5uA5DzzHIKetCWsmGCM27X2xHjQ17KmxUZNb4kMLanAkB2eyisHRfs1Ppf_9q_OdeWIeoavGx2VohqBXA2GxSR41AvC86YnfOBE-B2U5TafRZOz43Neh7u0g7FsWeTX4docM3SyQ2CwxmoiZ37YuYeMhwmKXi502uf-73utX3ttg0tgznWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر رامین رضاییان در مورد هو شدن سرود ملی جمهوری اسلامی
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78922" target="_blank">📅 22:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78921">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اینم یه آزمایشیه خدا داره منو میکنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78921" target="_blank">📅 22:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78920">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">همه ۵ سانت و ۱۰ سانت و ۳۰ سانت
واقعا این عدالت نبود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78920" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78919">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نمیدونم چرا اینقد بدشانسیم
۱ بار ۲ بار ۳ بار ۴ بار ۵ بار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78919" target="_blank">📅 22:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78918">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بهترین ترک یکسال اخیر دورچی ریلیز شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78918" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78917">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">همین امروز با رفیقم نشسته بودیم داشتیم میگفتیم بلو کیری خفنه بیارم قطع نشده و کسایی که ملی داشتنو مسخره میکردیم</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78917" target="_blank">📅 20:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78916">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بلو هم قطع شد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78916" target="_blank">📅 20:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78915">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1mAbB3NLbXICkfWXLxUrCAzNcVcJF9wN0MPiTzzldDq0uLeMcltQozNPjPg4yckY9C2eVTO8UMSv9aYFypwcDDyhqN-HoxWLzmPbEhUerLMuazRhEoGk9flsKVvUsF0Ui8px7x64gTqAUBmD0Q6m2_Gs7GEn0mz3GwFtfzjaDwsjY6TsQWE25nz9py2hODtBO2xc03MO6ZamHqt_XXJuqeN6mPL0CJb01UNJGOOdntR7E1w2JQQ31ct9_Jl3uZgQeOJfgukq3ex7tpQtQIK_cg1xH5OWgZ1TWaj1jGAe4elvYOd3jkT0xcui17xknpEDwULYZFBCzZr9feSPiAlQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتفاق بد برای هلندی ها
فرزند تازه متولد شده خاکپو درگذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78915" target="_blank">📅 20:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78914">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1LoqHK0qpPPXmljJthvVI96ZoGbMpwoMUkGipWzfdkUoCmCqG3snwbNm5iYni46Vdxow-42Nf4F5g63NUm0CSiXm1-iAZ1_xYmbeokZcdIgwyxVvhz6haDvZTY8ER5lnMAE1qqCcxdqseD07jySADchDnIksGBCsFSnkwbXhozvfR1GegQw_8bYZ_cQQhSNUYIYAu2QW4RzHY68AtZaoelBWkw921wb6hctbdyDXarXhYdgpb1ofJTLFRPHG-d0Q8fuKfzBWkG7851pDJtWKK5qrjgT3TqJcw3X9tyTVBFQR0eFnC2UxTg2WyCRUCfbGIiQv8tVE9G7YKWQ-HYoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجاع رو کل دنیا دارن مسخره میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78914" target="_blank">📅 19:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78913">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmlpnfRIgt2AzmCI1Nt8Cwg5Wo9DXhlWMlxIHVsK5TGV8rZeob4oBP0Y3pRYvmnwjWs3h111ct5Qgvam_okChnGhm7BAd7NNbB3XC-ge8Pk8Xv9n2eWnj9Pbv_amvYmDGn-9sORU9AbOxCLC3KCXtvU9bd75pZk8CiMjv2O_Ukz8wR5OqqLJTTrydt_6I2mBrryncmEZOPc1LgjiuE0TwpPkfmaMqimFVXnOFmVszWLOCGGRMNEICAkfIFY0ZYqZZYi_je06OT_pvs6TCufsmYmuPvl6Ebw0SMNup74wNGGWmpRbCBTDmyZ3ud-xDI8L3p21pxj4vESqRoO-q9TNMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جام‌جهانی هر بازی داره منو سورپرایز میکنه.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78913" target="_blank">📅 19:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78912">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4WvMoUhlPa7ERjqMpIlu95tx6TtBrA7QPMTLfw1tBSXJ2IVuSyVRXctiguMoicx7Yt5gdtPmiM6YX09wgm1B-veyZfllEaDQQg-XpTlTme9TFrXNLKDKS-udGwdoCK255Iu3Ihqlm1-JnqahqXJnWUMxqy5A7vgn0U0NAqGzyfYj65wJEyjifLgQZfnfnAn69r-6GKyGdwlvhx9vEYIJNsp_swojMYjyVa40pm8r2gDdbjOSraIAI65lQpnDcm3F8KY6V6-8O7-2nGesm1Ypj0L9y6LBlqufcCx_8Pim6fzSII81USU5QH21xk1CaCac-ErNm5T64VFkgh_qBvBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی گفته ایتالیا به جام‌جهانی صعود نکرده؟
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78912" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78911">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78911" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78910">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ-MnWsnrA8iz-ptvadqw5IiL-_fyNpzomLNe4icex6_lnfOEjjXh5VZMqVtlcXANwkyjfRD4_DlZA9DnakU5oIbj-dqpt5gHkeRMVlAgUCKhXVjPa-BmttOdFhyEsauYXi22oD8OO_ZxcHKFH9qMptZq0i1kjPp4NBcYAa_e3yqTvF-fSnMmNoYlprCA0WIBnbFRB8LTrrACd1aGSVa4DlReFz51O9ZMHd3F86nafy7CcpyYaY5hum1nG4gWwfeb_T0y1tPGf1bDds-6B5WX8NDFnjrAfO5vxgZPFnqiZe8iHLKlrCK_AAU6KY8z6h0DfH8AlePZuoLNrrEVy-XZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78910" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78909">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">همه ده سانت تا ۲۰ سانت نمیدونم ۳۰ سانت</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78909" target="_blank">📅 19:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78908">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترک جدید حسام تی‌ام و حسین تی‌ام به اسم " West Side " منتشر شد.   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78908" target="_blank">📅 18:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78907">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1kgj2beHxn2P6i0EFqnx0qgHUkTbeDB1tbl0SaHWLS1dKzjIPTYfikRQi19CVz5SS55cTAGm9KjVy0_dkxGm5LLFrn-41sv5ZrkcO-bh5Jn8QRxYbSSrMEZSfnRth1WN1B8EwKQJhoJH5dYrWGj_o_mYqeJmCT9MoXEa96GVlKEP1CQFLJeHhKxkoznj7SPqqgB6eKzUSXQdJf6WcijJDZE2tnRwpSci0mmcA_VwAK1TodLMiYFRnUkkjy9TgJl9y_6V1OXYRTkUAOa418cDXIEmSH1VWCrFowFg6dTCyxSF_Iuew9RS3KgXZsmxx-LJ9iYZiUwr5iT50VvfU1ivQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">موزیک و موزیک ویدیوی جدید مهیاد و دینا به اسم "ATISHSOOZI" منتشر شد.   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78906" target="_blank">📅 18:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78905">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMmndbpUXry39bM_1wbL3rGp6iYdM8W-_qencrcNGHs71O5Pq9tUbbYcCrEz17c64Ab-hDhO0PvIvWn_h6Xngq07zv8RuCkTw-y7scTB3ecaWqv1WK0Vc_caaKxLiHfYna5g0UmUXT20JiTWV9wJeCYLxZw5BPaZRaYG32meJzYGeLJaNqjzVT7zKvS5zY5tuZua-MHTMTQtCVwzDQqb4Z6RbmM__eukhzR0HaYO8AvMRrc09Ufb9cxUn8XIwhPesCBEL0DwYTG8E3rJ19i3aZMRWT53lsp3ttk7tOSx6E57-cloNAKVJeu16WBuYwruk5MAgl4ouLJDc6MZqRulCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78905" target="_blank">📅 18:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78904">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78904" target="_blank">📅 17:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78903">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_9LvBX34G6IK5EOYPFr4OUxy5Qfulek7lg8T2glP079KtKZGGq_XumEVSRfmY-IUwFR1-GFGIagGayRGf79Lcd9-lz0SJtOmUhFG3OUDD61-RRyJ54kuK8Oig7qKk7JAjv7i-SU-Z0J9hCkTaKdTvTs1q3OLEnldVXoDN34XLjCYsqkZrTzNFpgYrwBh_bKUh0tOx5Wyiz7sfuP7clhQ6OC3mQQQaV3UJbk9sZbtl77MbRx2YRrJlxI9mW1yjUxr13gLPCGcn3Y8SAv0LL2QZS32ivMffKyI9N1MedAddmoIjufg5UgbayMPYySMIx0yboeiRhk-EQWluue1N6ZeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78903" target="_blank">📅 17:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78902">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سازمان دریایی بریتانیا اعلام کرد که یک نفتکش هنگام نادیده گرفتن هشدار های سپاه پاسداران هدف پرتابه توافق قرار گرفته.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78902" target="_blank">📅 14:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78901">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7ndqFvMOmFFeIOzZ4YVAZHpLr-bVnm7eQKzR6AcVRI8ORSNGIptUE3WWZIRL7iHXzEsHboLodH6EzFQAx_vQUM5KBDjK--Si5UZnXVge-NitMs34Cd4BAWZSqO7DTe9gVLxhr6mk8AeJo159LzY9OmVoBYrDb-g2OMz92FPloY4GkcRvguxx7L_z9hnsG-XvFiUsTLOcUiQKkobTRmV3Frw5vxNA1Jysybm8SRaSc9U65auIZ3sVM5BkMYXHowYv2n1m0ljicHrt9dW8VAZhhcbIR2jEjUY1l7z0MOaZMyKtccj87OuW1PE4JcoeSw-Tvh9UvSWDUf6Oe-kTBdm9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی دیوار فلافل فروشی توی بوشهر نوشته بود
خدایا همه مارا ببخش به جز طارمی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/78901" target="_blank">📅 13:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78900">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4960c204ca.mp4?token=n2vH6kZEzYNaFl5YwIYbBqiSB9uelaQxGHWrKAKI08RpmCYfdXdgPHTUlgsps8MiBIu_q8vM_0kx3BkSzf6WTK74b84l6aX0WUFlO_W3fWbz6CFeZhmMjZ60foLij7DOExteULICwrmLCQ8uB9r9CusTiuf67dhDLGokin9ubmX1nc_YxMQ-8Ebk-Y6t5WkP1dQTxl_Z5RuVJIXOlnWkbpDvy1wf_CKjkVCwwDIYeHBNqdz-r_GAMJL711C-_b2DeKEF1FerReajRTIhGrDsTE3_iKIBSjFvsnv8YO0UHx7NdKtf2hBii180q48yJC-xap-6fetw7xGFavFuXO3ENg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4960c204ca.mp4?token=n2vH6kZEzYNaFl5YwIYbBqiSB9uelaQxGHWrKAKI08RpmCYfdXdgPHTUlgsps8MiBIu_q8vM_0kx3BkSzf6WTK74b84l6aX0WUFlO_W3fWbz6CFeZhmMjZ60foLij7DOExteULICwrmLCQ8uB9r9CusTiuf67dhDLGokin9ubmX1nc_YxMQ-8Ebk-Y6t5WkP1dQTxl_Z5RuVJIXOlnWkbpDvy1wf_CKjkVCwwDIYeHBNqdz-r_GAMJL711C-_b2DeKEF1FerReajRTIhGrDsTE3_iKIBSjFvsnv8YO0UHx7NdKtf2hBii180q48yJC-xap-6fetw7xGFavFuXO3ENg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کونکش دیگه خیلی رو انگلیسی بلد نبودن مسلمونا حساب باز کرده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78900" target="_blank">📅 13:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78899">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPVYA1Tm6WJWCdjeopScwb-LDIWXAXBpTrmVbPOhQx01m6MmDXooPVIN-YXYXxIsx2EVDF85gmwPHF_spp-9wtTDqRR4PSjzcW_NxbKxTra8qHMhZGUV4RmAOHbuLo69G3iwTO9gzK0oS03TCWq3SzknneSpoY59bAkie5wcZnG_zbQD0E3m62dxQvDZxyVKCGwY6rQoxCn49w5F728p6_mYFXNMpPZdn9anMdTVHEv8L39PfFkyqidMqXfY3oIRCsDyf2GkVtMmqnpAeDdKh9sWcIECO0T5NLIf2x8VkfQq1elHuE0DPNszTf5ZUD3-YErONwVJ21Uhr0gK2Onb9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی به کیروش زنگ بزنم براش آرزو موفقیت کنم فحشم میده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78899" target="_blank">📅 13:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78898">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">من کیری خفنم پسر</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78898" target="_blank">📅 13:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78897">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi🇵🇦)</strong></div>
<div class="tg-text">من کیری خفنم پسر</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78897" target="_blank">📅 12:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78896">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فک کنم تتلو کل درآمد یوتوبشو میده برا قبض تلفن زندان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78896" target="_blank">📅 12:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78895">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تتلو چند روز دیگه موزیک سومشم میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78895" target="_blank">📅 12:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78894">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8vX9Zfi7Vg3ke2bLmwV_KvnAPlePGF9lKqNTt1L0Rlml563EFFuytgCbQCrXyUR8Oih7QGq-Zxn1y2-FIlbfdN8IXXiTWO8T6XSO9RP1irfI-kxBRS40O9zg0aTwQIAWQBBkbpIXmBrrFAxoDdfPIKrEpl-z5kAU5tCHt2IJ-k56Rn6mPTla3dy9PjhvpaKXBh1An4sVR09F0Mj6hBy8biB7SxdQzTFbzUfksqZLZTlW-YLBB_jWZlljlPPXkXvXZuO0Kzxz5uo6HNqt6D23OCO2OivDWij59UUwjQm50YgrxKBwPnPrfpBiz0svE-oHqN6TyWYq9rYR79Ew-EZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقد گفت بدویید، دویدن همشون رفتن تو آفساید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78894" target="_blank">📅 12:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78893">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFmz-UL7hEhRfn-E-q8rHT2pKJwDqfcVDDniqWJ7lkjYQuuttJEWnnbks2ULDY-ppIasd5pwCpqHEpJPHaEw1V3IjeJMeFW5On8f5JifrJzE358PA0S3Rb888TwimijW9rF2_KhvJ6P6L33AK2fPOyTA5VvaEOpuiPRbItvq4cNBzzsH0ok-uIbVHkvZpqUhV7u_YoZY2ljcFCQ8F127Q-dGL2ZjQE0S2pM9We-4Mf64oOcS756fxAE_cOAoMdjF2rbJ-8R_iVdj6MQe_DQx6IH_Cb-FEPBVu1LmKf_TM1ROyS_HfFToq-8PzDGMI0PJF0yWguweafqv69TlY2-G0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5nLM5jhX8NEIKeXJPoJgavjyJmI_DnIzP7Mr1Btu2vxouSjbfjRzXWA_kgOmQN3_sO_YS1kPNxi7V3Muz8nchBpDJMYVJEjeYsF4oUl8zxmqjagU64isZ5bfnt1m_x-RhGpJbvqEBpmk09roSu6QXGd9ampjG5fjLEVJ8o6dstch6Dni0MELik93xOSpG6PGv-1iM9lWMZ7YVlUi_POjHS_uT8lIyyazK5z-HF8xO68Agp47weMRVw2d9nc15kIpKVOrqfTcnYhwWhtWhQhaUYn_VX_rHC4CxNmYSttUvFmHxdGNulfll83x0o81d3AIbcc9PXbyej4Ym39YrLy9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثکه تیم باز یکم خوب بازی کرده و شانس صعود بالا رفته میبینم یسریا شل کردن خوشحال شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78892" target="_blank">📅 11:48 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
