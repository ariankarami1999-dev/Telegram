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
<img src="https://cdn4.telesco.pe/file/i8YK43z2eXTE5KeXgvS0kEYH8oPa8dGmhvM80gb9P29YPlqClGS_c4-i2J0OfNveJcQ7c59vgN8dWHk7aDJnyVQ4mZFyKX1QXt9paeD83s0lrfBdTw_--B5dOr3VWZa1Yc2722IYxri-xn8KqqBu3D1Tcz4vZ4UUt6a_v4a0xzXmWhYeuZ_j3YZ-ChAeyrgzKOvBVBzEeR5baLietXKMi_Zs3BjZqU6oQtpDrendq0UHLfoLDep_yqjGSEFjW92ofFrETUnJaKPwIMs6lSbabt4Hgb6XVvJk14KQee_PfQRVomAycKTMpFpPBfG-DTRCp2ZILHOqP6OvjD2P4jMsvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 919K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 15:05:09</div>
<hr>

<div class="tg-post" id="msg-133747">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزارت امور خارجه دولت صنعاء اعلام کرد که عربستان سعودی اعلام جنگ کرده و باید مسئولیت کامل این اقدام را بر عهده بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/133747" target="_blank">📅 15:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133746">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وزارت دفاع یمن: شبه‌نظامیان حوثی مانع از فرود هواپیمای ملی یمن در فرودگاه صنعا شدند و بر نقض حریم هوایی یمن توسط ایران اصرار ورزیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/alonews/133746" target="_blank">📅 15:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133745">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
تصاویر دیگر از فرودگاه بین‌المللی صنعا
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/133745" target="_blank">📅 14:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133744">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوری / صدای انفجار در پایگاه بن زاید، امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/133744" target="_blank">📅 14:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133743">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری / صدای انفجار در پایگاه بن زاید، امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/133743" target="_blank">📅 14:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133742">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6kPVhmQtOOQh6iutEgvShDhYqp8zSQVJptjFPJ8SS_yiz170VS0fbt7rI14_e8y6y_FbQRM6HXJuQImeOtc9CoGOGRh9kYD1UdR99kQRmzpVankiMdkZtE2W3J-nn9CC70MtxW7SugY-3vHzL1GVwCzMpWbekqaBG9_iFHfvsvsEg0APrXdO4qJIB06mk2DJctnQHs0va4ocpQL_EZqQJejRp9jzDpVAI9y1szNRw5dfTiUr30Po2_FAQtMmBXES8jopjSSQaS0h9jzOIfeMDr_HBd32Gmt1K2RVqJXRaK0twlzAXmohNnRbs_g6f6YdLclmA1oB_kxTpsbM1tz3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیش از ۳۳۰۰۰ نفر درحال مشاهده حرکت هواپیمای ماهان به سمت یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/133742" target="_blank">📅 14:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133741">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
هواپیمای ایرانی اصلا به هشدار های عربستان دقت نمی‌کنه و درحال کم کردن ارتفاع برای فرود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/133741" target="_blank">📅 14:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133740">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح یمن: عربستان به مرحلۀ کاهش تنش‌ها پایان داد
🔴
حملۀ عربستان به فرودگاه صنعا بدون پاسخ و مجازات نخواهد ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/133740" target="_blank">📅 14:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133739">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kmrv2NPMB89h_AsUlAihEZuB6sVBWvx0KHwaXqj5k-0p28aLkQtqyWy5djMYXATxsdq7jozkgGon91exHgZcekARdukA-x50S3AXpDEkxUimx_JlLi99rvvPmiK4q6wF4No7lWaw1NYTLVSY6nVwlLVzlXVb_D9ykEECX0T8spAkwCzgfkw_Nm3p3BMiDQcaNNDX4WEyGjqYrTaxy83xHgxlOicCbieGcQeGG-GMK9K1R2vNvKSkYk6SV9vQ4nZZg5iaaofSe4Jnyc-geDKEKNZf4zou8Jbe8uu3fdFiiYXITI0NuNOn_B4v_C6rDhnmIh5NnBWeUf-5fCQN72iuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای ایرانی اصلا به هشدار های عربستان دقت نمی‌کنه و درحال کم کردن ارتفاع برای فرود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/133739" target="_blank">📅 14:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133737">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oEaW_QLCyjMwHMVd-s6irPdZFFE4851sJuR1bfqOz2Xn43paKJPT6FOGzA_04__o_S6bNJM8nX4kukBaZVYgZWe53pYJripcmSPK4Jm2z7sdb6owSpnhMdOx7SlfsRNOQJ6DpcLB8IWjOSe155vkaxa_8WCeVIjG8gVnoDSAQodfJo71o8qg5lT_fUamS-7_BvxmAexXGqnwuFYKmNRgH6qA2vnxlmrTsERO_4iYKLzHUh2dNHRBPlA4rB51hblBkgTiMFS2AhnoF2Kbz3aKq0yznCcNisZKuMShUsIP7YYzUUu8Q_k0iwd68ttHQx9koY2oIkNvdcFRuugaFT0k5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HiMZMT69Pmb7qY7y-O1uGr28CowRiCRK3JxHlYHx8zPp-bNv8GZDH_SeKm2_MZLUD6iVYgT0xl4arK_vQIH7BaGzw7ksNIz43YeXYh2qrgDrISI2YSk26a71JlNv5hASB0gFBKhXjIV-1X5n-pRF9VDiuv8IFEQEvYZczyikjapQl2Ll8XQszpBQ4lVOAwe5CGD9EIFSALfi2rs33DaJIGYJlNvYp88UEHP9Y8BmNQl7LMw2YeKpBmZwc0i1OKcuz0weP4KpczAZcHnd1eOvX3r0GklYPviSBG9JaYLdd4PSXhHG1iRlfPsAOzOYy15YpNVZZOoJOOk4ALl-cm8jmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر دیگر از فرودگاه بین‌المللی صنعا
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/133737" target="_blank">📅 14:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133736">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TypotTyIuj3bEKeFAIPLG03wPXRHHj27iMQh5XoKv0Y2gwlkrzeE060q7TKNOnae5D-v-4QNJIMEE-GAMpHwZvWHinUuZvyX5UtMXq_vKlqET1DhhQI7QYjVTp82HykiMyGi-r8buFZAgvXJZSNP3c4_pzSD81AYTygOTxWPg5BWc3I3AP4nuzH_3kXh3CJHDEaFJZP2PEFlIZbYpa5k5BhjFGbXL8wTgjb_XHRiWhEjISY0nzZXmfo8qv03zpor2v-52vBuRYQekwN1OItI3qst4JTDZUN5M49n8ENZfRczF4BKc-jdMmbcavaTd-70yjpqSW-FM22OsCvDvUcfZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنگنده‌های سعودی، فرودگاه صنعا را بمباران کردند و دود بر فراز این فرودگاه دیده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/133736" target="_blank">📅 14:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133735">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری / شبکه المسیره از بمباران فرودگاه صنعاء توسط ارتش عربستان سعودی خبر داد.
🔴
همزمان وزارت دفاع دولت وابسته به ریاض نیز خواستار تخلیه فوری این فرودگاه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/133735" target="_blank">📅 14:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133734">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
چین: تردد از تنگه هرمز باید به درستی مدیریت شود، تنگه هرمز یک آب‌راه بین‌المللی برای کشتیرانی است
🔴
از سرگیری هرچه سریع‌تر تردد آزاد و ایمن در این تنگه به نفع تمامی طرف‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/133734" target="_blank">📅 14:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133733">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
صداسیما: تنگه هرمز به دلیل نقض تفاهم‌نامه توسط ارتش آمریکا، همچنان بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/133733" target="_blank">📅 14:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133732">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزیر دفاع یمن: با تمام توان با هواپیماهای متخاصم ایرانی مقابله خواهیم کرد
🔴
ما ایران را از نظر قانونی و اخلاقی مسئول نقض حریم هوایی یمن می‌دانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/133732" target="_blank">📅 14:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133731">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
صدای انفجار در آبادان
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/133731" target="_blank">📅 14:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133730">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7c6c71e3.mp4?token=OxVou1YjIXsaIirGz3I2DgrRuN2WmcRM6sXaxMOhEzPzq3y04UcXsnNqhFFWaC-0FBEl9uA7C3_0269GYnK8MRSpJWMg7a_YEABWFNne2ZLga2UK_jMBUgXRjN2nvah1U1zWmr7-MV4Xy_xNpS4Gflb7cNyVOJI90QQSCgnJp64XWYhUOQ-z3q4D_h_8YIUulGvsKG0S-_3SYin_tRY9F6CL8cjUE7ftnrqghfH87uc3robCZrPTaYrHgDQtbjn_vwiWD_uMvJ9I2v1A30GzBFhchBPnq_YvQ38EdJwSMffS50jN2jfRVxt-sntDHSS7J5cVJshrsD8_UHhUVVSR1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7c6c71e3.mp4?token=OxVou1YjIXsaIirGz3I2DgrRuN2WmcRM6sXaxMOhEzPzq3y04UcXsnNqhFFWaC-0FBEl9uA7C3_0269GYnK8MRSpJWMg7a_YEABWFNne2ZLga2UK_jMBUgXRjN2nvah1U1zWmr7-MV4Xy_xNpS4Gflb7cNyVOJI90QQSCgnJp64XWYhUOQ-z3q4D_h_8YIUulGvsKG0S-_3SYin_tRY9F6CL8cjUE7ftnrqghfH87uc3robCZrPTaYrHgDQtbjn_vwiWD_uMvJ9I2v1A30GzBFhchBPnq_YvQ38EdJwSMffS50jN2jfRVxt-sntDHSS7J5cVJshrsD8_UHhUVVSR1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل ویرانگر در شمال شرقی چین، خودروها همچون اسباب‌بازی با خود برد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/133730" target="_blank">📅 14:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133728">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfb74VW4f2oJF5MHbYjlH1GL6uoBBXyQNw0yKg8PHlGbt-U0CD-pVxn3uOq2008xgrhpC7oq0K7oTwrqvhsdegk7W1Zx3x6kdJr1pHBUarIgDo-_Hqqk-AF0Jn_xfd1xebXI_NGh4alw-jwdBYtKoAvt6sU0bzpR486rr-yE8IhuIJLY16DI711QpwWtlPWvFpZ5puF-HEkh99TkxJFQPh8JnMK7NmBsX8NFuaAPffPW_ymqYl4kfvijJuZDV-sF9rSOuqD4_tiYpO6SF2cpfN56ELAmDGayskHnfKanvZ_-pbYMAXCMuqmMQaMrg43pFpLhl7IHxmT5Hym3vBP3aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تولید قطعات بمب هسته‌ای جدید B61-13 آمریکا زودتر از موعد به پایان رسید
🔴
دیفنس بلاگ گزارش داد اداره ملی امنیت هسته‌ای آمریکا (NNSA) فرآیند «شکل‌دهی الماس» تمام قطعات بمب گرانشی هسته‌ای جدید B61-13 را سه ماه زودتر از برنامه در مجتمع Y-12 تنسی تکمیل کرد. این موفقیت پس از اتمام اولین سری از این بمب‌ها در می ۲۰۲۵ (حدود یک سال زودتر از موعد مقرر) رخ داد و این برنامه را به یکی از سریع‌ترین برنامه‌های تسلیحات هسته‌ای آمریکا از زمان جنگ سرد تبدیل کرده است.
🔴
بمب B61-13 با حداکثر قدرت ۳۶۰ کیلوتن (حدود ۲۴ برابر بمب هیروشیما) جایگزین بمب‌های قدیمی B61-7 شده و قرار است بر روی بمب‌افکن‌های استراتژیک نسل ششم B-21 Raider نیروی هوایی آمریکا نصب شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/133728" target="_blank">📅 14:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133727">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YocaDMnwynSgV_J5FrDCnz-s9QrQOUQM62h1mXV-RaIbXxlf1fR5Rz7p18M6o3zvKUrT2YoNaFrbyZ5kN9ZB2HoeEKIkXRyyhILZl-JaEXYHLFnV70MFUVNZm7h40cbhYuR88mxPI4dqQi-x6rXGUuspBwRfhh0kaVlDVM8BjnMJAqn0lzJRw1V5E-yl2Gx4nGjgPIY6D-eHgy6IMr-QmBQyQzRorjEQOJ1OUrOVhVAbLRUC15xW0j8cjojpYcer7qMADIjs4fGoHqlfTqqMjapzQrYCwr_uD6VQcFqjqT4RGG7O0L6y6S018zOL9vZzpoQC751KFQHhjt6y_4OSZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون یک هواپیمای ماهان ایر بر درحال حرکت به سمت صنعاء است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/133727" target="_blank">📅 14:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133726">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
گزارشاتی از شنیده شدن صدای انفجار در شهر جم بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/133726" target="_blank">📅 14:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133725">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
عراقچی: در سفر کوتاهی که به مسقط داشتم با وزیر خارجه عمان دیدار کردم
🔴
به همراه هیئت‌های حقوقی و فنی، درباره هماهنگی دو کشور ساحلی تنگه هرمز برای مدیریت این تنگه و تردد کشتیرانی به گفتگو پرداختیم.
🔴
این گفتگوها را در سطوح سیاسی و فنی ادامه خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/133725" target="_blank">📅 14:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133724">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
صدای انفجار در آبادان
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/133724" target="_blank">📅 14:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133723">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136347dee7.mp4?token=GRRwM0i44l67ehjXWZM3hDfrcVBjH8WXD0z5MiHwGRHyaDMYgQzcpk06wWMYwqXGi9etU3Rs1a23XEVUl-bcj_wnvvFRaXun1XP56veJc2PmSsqEtrWBF8QwWjZSggMEm96AqUp5_2r2deJBMw_d2kSf3Q58fyourOe9ZtoIsDNrTQ6ekp9F7MX7R4bPoxuMSoNU63m6eOybTy-ifN6UzTCooAwXLM48YNMEqzIC8KqLISWAAT3DFrHEB8TpU-jEmdkG1AY4dji3wCcjuwKrJi_KOehOZXWQiQHUgBaBIgVPJc3DBKk-1MgdPrZtgLsL_kSimY2IN0mDyQp6txyWSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136347dee7.mp4?token=GRRwM0i44l67ehjXWZM3hDfrcVBjH8WXD0z5MiHwGRHyaDMYgQzcpk06wWMYwqXGi9etU3Rs1a23XEVUl-bcj_wnvvFRaXun1XP56veJc2PmSsqEtrWBF8QwWjZSggMEm96AqUp5_2r2deJBMw_d2kSf3Q58fyourOe9ZtoIsDNrTQ6ekp9F7MX7R4bPoxuMSoNU63m6eOybTy-ifN6UzTCooAwXLM48YNMEqzIC8KqLISWAAT3DFrHEB8TpU-jEmdkG1AY4dji3wCcjuwKrJi_KOehOZXWQiQHUgBaBIgVPJc3DBKk-1MgdPrZtgLsL_kSimY2IN0mDyQp6txyWSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاسخی مراد ویسی به مخاطبی که گفت باید حرم امام رضا هدف باشد: حساب آخوندها و امام رضا جداست، امام رضا اعتقاد قلبی میلیون‌ها ایرانی بوده و هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/133723" target="_blank">📅 13:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133722">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfDbVqRgrBuTwx2IYYWWTizQcBWHsXXaXjbQLjHLvjrRX4FWouXn2X1IJcRIxNRTMlOyLDedH3FKLqcwFxlF-IR58seM5Pi7ylfdLLxeCTIYwWhM_UynqorEGQRWOfdVS0mpTfDdqgIbRujAUhrZ3NG83-OtDcHWwHnxZ3XEB9tfo12afCoCjvVQMnuupXqpbFg6seQlE0rMK593QETidpiWjaIiOSYOPk5hR5H4EIQGIZZE0GKwzQbRVZ_Oj3fL9T-lNGfCSHGqiR99drJJhC1k8zSAw3yUKDX2F0JlpyeXrgGUZSTdbn5C2fEiQ0PXuPwPRvi0Yi4ePkPx8VRXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن مرتضوی، خواننده و آهنگساز ایرانی، با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/133722" target="_blank">📅 13:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133721">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری / رسانه عراقی از هدف قرار گرفتن شناورهای جنگی آمریکایی در تنگه هرمز خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/133721" target="_blank">📅 13:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133720">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
بقایی: لبنانی‌ها از جمله مقاومت لبنان، بهتر از هرکسی می‌توانند درباره سلاح حزب‌الله تصمیم بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/133720" target="_blank">📅 13:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133719">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری/گروه‌های مسلح وابسته به عربستان در یمن: صبرمان تمام شده و به نفوذ ایران و حوثی‌ها در حریم هوایی یمن پاسخ خواهیم داد
🔴
با تمام امکانات موجود در برابر هواپیماهای ایرانی که به سمت فرودگاه صنعا می‌روند، درس خوبی خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/133719" target="_blank">📅 13:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133718">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: انتظار ما از دوستان عمانی این بود که در صیانت از امنیت و حاکمیت ملی هر دو کشور ساحلی تنگه همکاری لازم را داشته باشند
🔴
ما خود را ملزم می‌دانیم که تدابیر لازم را برای جلوگیری از تکرار فجایعی که موجب حمله به ایران و ایجاد ناامنی در منطقه شد، اتخاذ کنیم
🔴
برای کسی تصمیم نمی‌گیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/133718" target="_blank">📅 13:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133717">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سه ضلعی مرگ
‼️
🔴
پوتین، نتانیاهو، تندروها
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/133717" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133716">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_WzLg-tK-FegzVwSaE0MzeccQEQs3KsDOOOucvggTHZv0XsY9hO3QRCXhv3r2FavJGqP8zNFmObieqVQIzYakhuQItfve-yHeBl0h_y78miDojONzHijYTxt7hPEs7xSDb8bXmc5NTZvysAXdjdPjWqkgVPJFZTsMIPkMAcaryXXALj4kYZVnptIOhWYbsZWnOQpmNOWA6kOZb91nMIgUmSxQwwVC1IWhBTN9aESo6-IA9WbCSWXSxD4IAFNgcVrOFLybI0CfIBuLDdLGhXt8DwhlVJG9O_VtT-rRW4PQiZB8MBfgwtw1lDE8g7YT_hfBSBbELMv1HBwJFVeq9Ygg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای اولین بار از زمان آغاز جنگ داخلی سوریه، کشتی‌های جنگی نیروی دریایی ترکیه از بندر لاذقیه سوریه بازدید کرده‌اند.
🔴
وزارت دفاع ترکیه اعلام کرد که فرمانده نیروی دریایی ترکیه در جریان این بازدید در کشتی TCG استانبول حضور دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/133716" target="_blank">📅 13:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133715">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc8cbaf417.mp4?token=P1WKBMiYs3oif5lSuFGuRWSK2brYWhvfua1KcKZoBwNorvobEqICuOfUA0xRNf4Nx9VPT2XrVM7k3lxzlhbaQXIT93u3wD6qAaIGjKZ0VHSRwo8ZeKgaXOo8GDdY1LLDZxX3LZyrWjZhIX_GKIz7jEk_c8VfmNpwRKtyWLp2TFj4dSuHc31SCjLEQvAtfUT84WLWO-SEejMV7_Wo7Q91j-ANCSnvnQ7z4Tp8sOgnkCs_zsKxZMtJb9obYFb7TUEw049tnVhklbB4I0UEIJBueQLCsIQRKuPAZZgzpWMuL5_mBZZnuifIyNRWhgUp9VAWru74HTPoL5Ptjt81ZoCbtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc8cbaf417.mp4?token=P1WKBMiYs3oif5lSuFGuRWSK2brYWhvfua1KcKZoBwNorvobEqICuOfUA0xRNf4Nx9VPT2XrVM7k3lxzlhbaQXIT93u3wD6qAaIGjKZ0VHSRwo8ZeKgaXOo8GDdY1LLDZxX3LZyrWjZhIX_GKIz7jEk_c8VfmNpwRKtyWLp2TFj4dSuHc31SCjLEQvAtfUT84WLWO-SEejMV7_Wo7Q91j-ANCSnvnQ7z4Tp8sOgnkCs_zsKxZMtJb9obYFb7TUEw049tnVhklbB4I0UEIJBueQLCsIQRKuPAZZgzpWMuL5_mBZZnuifIyNRWhgUp9VAWru74HTPoL5Ptjt81ZoCbtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در پی حمله های اوکراین به زیرساختای روسیه، صف های بسیار طولانی بنزین و دعواهای جالبی تو جایگاه های روسیه دیده میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/133715" target="_blank">📅 13:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133714">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d1010c6d.mp4?token=WkaHStxJCn5NLPNX5qDex8Np_W0CrVspcjU-3lhbvph8et3aHHSGG-hJ0dMSN3Ohx-ONw5NkJnOgrn74yzG0iE8VoC9VjbNmIivdVVuS5R8D2LuKjqkYcZmzHS7lXOwA-h7RjXDQJETeS1F3FbbJBkaLmG46sUQmR9TyHS7dnnWn4QEmYbRM4yUTeFGqvU35I-GDJra2qakGueEb-iadwi0Yl6Sst0W4Zz5b5nZ5FQ1yqabddh3QSXZT63TRiWylNxjVhQNlLQje4oDR4LIqW-QqbuQbLx-WeWqriwsB4DK9SZANlL4PG7rbMtEcU_7ZL1VQroBHyGhWWTbZPoZ20Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d1010c6d.mp4?token=WkaHStxJCn5NLPNX5qDex8Np_W0CrVspcjU-3lhbvph8et3aHHSGG-hJ0dMSN3Ohx-ONw5NkJnOgrn74yzG0iE8VoC9VjbNmIivdVVuS5R8D2LuKjqkYcZmzHS7lXOwA-h7RjXDQJETeS1F3FbbJBkaLmG46sUQmR9TyHS7dnnWn4QEmYbRM4yUTeFGqvU35I-GDJra2qakGueEb-iadwi0Yl6Sst0W4Zz5b5nZ5FQ1yqabddh3QSXZT63TRiWylNxjVhQNlLQje4oDR4LIqW-QqbuQbLx-WeWqriwsB4DK9SZANlL4PG7rbMtEcU_7ZL1VQroBHyGhWWTbZPoZ20Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسانه‌های اوکراینی گزارش دادند که یک پالایشگاه بزرگ نفت در شهر سیزران روسیه هدف حمله پهپادی شبانه قرار گرفت.
🔴
به نقل از «کی‌یف ایندیپندنت»، این پالایشگاه در ۸۰۰ کیلومتری مرز اوکراین واقع شده و در پی این حمله، آتش‌سوزی رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/133714" target="_blank">📅 13:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133713">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
دستور پزشکیان درباره طلب ۴ میلیارد یورویی تامین‌کنندگان کالاهای اساسی
🔴
با پیگیری اتاق بازرگانی تهران، رئیس‌ جمهور دستور رسیدگی به مطالبات ۴.۰۷ میلیارد یورویی تامین‌کنندگان کالاهای اساسی را داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/133713" target="_blank">📅 13:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133712">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری / به گزارش برخی منابع: شلیک موشک‌های کروز از جزیرهٔ قشم به سوی کشتی‌ها و ناوهای جنگی آمریکا در تنگهٔ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/133712" target="_blank">📅 13:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133710">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYctIdcyL3OAI74pyfDxMJXwTlA2bs8FmZGwio3dzJ9aAXhLj33NG4MKSw8r168uR5hZV0-QFyWptaoo64gqOob6eL8eN57aALfI7tqUo14BAivfBxgyW17wChAMa-LdP2OshSPsYL9ESP3lCQbHIietOwyQPPF2n42OH4cojNm9i0QqqngzU1G5VqzxiuBrmSQizvNY9Yh-OzEfpnoq69WKBJcd7QhuSCbLQvG89pQVXFtZEv18Jfon6NehYmx3RFfWT4E1uWxnB0BOHpr1HnAK476XjoADC0SAxh5upHk3K8VEAVLSmMn0lxJLt7jm-QE6ggvsBgoHbZioeJF_zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWfSz78ApxhZHXgNkbJgISS4fQ2nJOU9wp24Tj3liaWUfqbcmWRdmXT0f7LSvuSeu5M0jRdcMLWhPpsRDy4g8Xee714ErqfbTBneIcWhr35NvhoMg4GtgbRMtYvJ1EkYsPS-BW9ZEkhFabelQnlNcljLOr3D4NNt8ci6z1Ix2nnf1bGiFa9P23RfzR7O2vbM_959Q5fzb8skoJyUxCleTKYVwOCltWdy4Wme4dTFTeVSwa76k9KReskLmOxa86PT5vN-FcXnbfASE8YyqRANPD77DrHj_DDjw_lmd-xK_ZwQyWdkef6tlC3QjS3fr3FUEwbmr-P0P5hE2HWS4Q85xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تانکر ترکرز:  در حالی که برخی از رسانه‌ها از وقوع آتش‌سوزی در جزیره خارگ خبر داده‌اند، بررسی تصاویر ماهواره‌ای نشان می‌دهد که افزایش حرارت مشاهده‌شده نه ناشی از حملات آمریکا بلکه نتیجه‌ی مشعل‌سوزیِ معمول و برنامه‌ریزی‌شده‌ی گاز در تأسیسات نفتی این جزیره است که نسبت به اوایل ژانویه ۲۰۲۶ تغییری نکرده است.
🔴
بدین ترتیب، گمانه‌زنی درباره‌ی حمله به زیرساخت‌های نفتی خارگ تأیید نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/133710" target="_blank">📅 13:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133709">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c8802cbe.mp4?token=ESlTAh-4SwH_EtCVXO9OwN7-aBYCRcOaZbmoCfbj0PbZDqC5wXULuuXE9hg6_qe1Pu_BtQnapn0A1vPqdckGcYMGG-gMI2F2kaUfNZFjU5FKYajiAJT3z7xYWMkgdzpOtgYflbqC0dB_7mnrfX24UeSzuozxHdn-lhcKpUHdjgxdP1_EaPJXdBeGOQUTcOVKYnfmz9b9LcAexSMtU8IM14PWGxVt4lvN918N5r8N5sDZrsZFmj3sYJSEw1kj9GQIjppg6CfiAR8BeWVQJutuFpCj4zST192Pen054t36W6ygy3MDMBOFDBOtncRFtNjEjMAEwTFfDmXRRXdnnFH3yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c8802cbe.mp4?token=ESlTAh-4SwH_EtCVXO9OwN7-aBYCRcOaZbmoCfbj0PbZDqC5wXULuuXE9hg6_qe1Pu_BtQnapn0A1vPqdckGcYMGG-gMI2F2kaUfNZFjU5FKYajiAJT3z7xYWMkgdzpOtgYflbqC0dB_7mnrfX24UeSzuozxHdn-lhcKpUHdjgxdP1_EaPJXdBeGOQUTcOVKYnfmz9b9LcAexSMtU8IM14PWGxVt4lvN918N5r8N5sDZrsZFmj3sYJSEw1kj9GQIjppg6CfiAR8BeWVQJutuFpCj4zST192Pen054t36W6ygy3MDMBOFDBOtncRFtNjEjMAEwTFfDmXRRXdnnFH3yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرمانده پیشین سنتکام در گفتگوی دیروز CBS News درباره برنامه تصرف جزیره خارک گفت و آن را هدفی دانست که باید در برنامه ارتش بررسی شود تا دست آمریکا در مذاکرات بازتر باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/133709" target="_blank">📅 13:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133707">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
مهر: شنیده شدن صدای انفجارهایی در حوالی بندرعباس و قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/133707" target="_blank">📅 13:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133706">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
دلیگانی، نایب‌رئیس اول کمیسیون اصل ۹۰ مجلس :  تحویل (ترامپ و نتانیاهو) به ایران، باید یکی از بندهای مذاکرات می‌بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133706" target="_blank">📅 13:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133705">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / گزارش ها از حمله به پایگاه شکاری بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/133705" target="_blank">📅 12:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133704">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
توزیع کارت ورود به جلسه داوطلبان آزمون کارشناسی ارشد سال ۱۴۰۵ از طریق سایت سازمان سنجش آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/133704" target="_blank">📅 12:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133703">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سخنگوی حزب آزادی کردستان:
ایران صبح امروز با سه پهپاد به مقرهای ما در استان اربیل در شمال عراق حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133703" target="_blank">📅 12:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133702">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری / گزارش ها از حمله به پایگاه شکاری بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133702" target="_blank">📅 12:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133701">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2Nw1ilR4agGG96nHnTfty7KwVeDkbmGgCDL2j2pmNMKomh9-x5exNcCQd4u7pKNVPDi2NxZdK9ZciNJc9fa8jb9MvrFN-NQ79XHLgVd3KZjhgzwJM3_ThfgwR36_tI4xBApyiA_X7dBPFD8fTvNjQpuSAk4-hffUdHsBUTkfLmCkn2JRWMzJ9cEc5hVFIAMo7hPxCLN_SlnpdUwKwDWS5bV341GKUDt6VOxyuqhV-sPBfIQaADqy4vHo3MbvN9KVqqpL8mIanmh9lM6juC22KO1qbAa8-uFzuzi3m9Pq-msEf6p0Bl-dhfYANe104zYpzHkcy_1-FyNNaOv1x-_ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ریزش بورس به زیر ۵ میلیون
🔴
شاخص کل بورس در پایان معاملات امروز با ریزش ۸۹ هزار واحدی به ۴ میلیون و ۹۶۷ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133701" target="_blank">📅 12:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133700">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
علی‌اف: باکو با جدیت در حال بررسی خروج از شورای اروپا است
🔴
رئیس‌جمهور جمهوری آذربایجان امروز گفت که باکو با جدیت در حال بررسی روند خروج از شورای اروپا است که پس از تنش‌های اخیر میان باکو و این نهاد اروپایی در سال ۲۰۲۴ کلید خورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133700" target="_blank">📅 12:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133699">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00d0b613f7.mp4?token=Xg12ziz0Ye2qWlNPa3SF-cQ7_ylJoCYuhcv_iaXkrHBx7fufZoLv7k9w-IqjKYYxIesmxe8sbkmFx9bxMTqxTcS0AUM7WoIWve359i4_pKAXCWaWET2pRYBbulvDixDp3zVtEzOmzzOWfiyG9zisQxXeVH7DAVmNQAbQlOOxrKA5DTfWIC5H_1wHaDlE-FkIKALvtKVM7kCiGID7edn3zXKa909uZXZ9BUP-mebArBMyFOmPZT9DT-HK9I-U5PcBMUMd0itdnKV7XiG5LtqUFp4BdrDiCmCZ1qh4NqRSL-eEd5HoQ6d34fcWj3LBKvJqyMa5gIrbQrtRoN97fRcVjoSxslscxSu2d0msOYcJSee1e0N0AVI1rQEk3EGMOOJxXZ_aFCpd15GKbpRFNTeDQM3hKRRbdIJ4LYZmRiE9EbCNw7qrdB5jEW4y_2kMkW6QVl0k8zS8VhNysC40avtKzDQt5vX2FiGxMm1CraFAQlCfay2mekLpITPS9LdhtT5sJxlBaCwb0fqxAAM_0JoiqsZVnHcPdMM-hxDjQRO8Swk_AgT7RNvQ8QNtrHrmfbSB_yEwgUZyzh0EOlmq-efBmVwMLzbSREPrUnNTNg7HySy-E5Y1hTI8_Wn4p58te08VmksAgMEkHYQTwIwHXQeoZUN9AMwp5BJ2-iW_Ry15GO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00d0b613f7.mp4?token=Xg12ziz0Ye2qWlNPa3SF-cQ7_ylJoCYuhcv_iaXkrHBx7fufZoLv7k9w-IqjKYYxIesmxe8sbkmFx9bxMTqxTcS0AUM7WoIWve359i4_pKAXCWaWET2pRYBbulvDixDp3zVtEzOmzzOWfiyG9zisQxXeVH7DAVmNQAbQlOOxrKA5DTfWIC5H_1wHaDlE-FkIKALvtKVM7kCiGID7edn3zXKa909uZXZ9BUP-mebArBMyFOmPZT9DT-HK9I-U5PcBMUMd0itdnKV7XiG5LtqUFp4BdrDiCmCZ1qh4NqRSL-eEd5HoQ6d34fcWj3LBKvJqyMa5gIrbQrtRoN97fRcVjoSxslscxSu2d0msOYcJSee1e0N0AVI1rQEk3EGMOOJxXZ_aFCpd15GKbpRFNTeDQM3hKRRbdIJ4LYZmRiE9EbCNw7qrdB5jEW4y_2kMkW6QVl0k8zS8VhNysC40avtKzDQt5vX2FiGxMm1CraFAQlCfay2mekLpITPS9LdhtT5sJxlBaCwb0fqxAAM_0JoiqsZVnHcPdMM-hxDjQRO8Swk_AgT7RNvQ8QNtrHrmfbSB_yEwgUZyzh0EOlmq-efBmVwMLzbSREPrUnNTNg7HySy-E5Y1hTI8_Wn4p58te08VmksAgMEkHYQTwIwHXQeoZUN9AMwp5BJ2-iW_Ry15GO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آسیب وارد شده به یک واحد زرهی از تیپ 63 ارتش اوکراین توسط یک بمب FAB-3000 در منطقه کیف
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133699" target="_blank">📅 12:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133698">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
هاآرتص: در گفت‌وگوهای محرمانه در داخل نهادهای امنیتی اسرائیل، نگرانی‌ها درباره ماهیت دور کنونی تنش میان آمریکا و ایران رو به افزایش است
🔴
در اسرائیل این احساس وجود دارد که امریکا دیگر همان میزان قاطعیت و اصرار گذشته را درباره برنامه هسته‌ای ایران نشان نمی‌دهد و دور فعلی درگیری‌ها عمدتاً بر باز نگه داشتن تنگه هرمز متمرکز شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133698" target="_blank">📅 12:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133697">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
دلار در تهران از 180 هزار تومان عبور کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133697" target="_blank">📅 12:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133696">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
بقایی: ما به هیچ کشوری در منطقه حمله نکردیم و حمله نمی‌کنیم، ضربات دفاعی ایران صرفا علیه پایگاه‌ها، امکانات و مواضع آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133696" target="_blank">📅 12:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133695">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
داده‌های رسمی نشان می‌دهد که کشورهای اروپایی در جریان موج گرمای بی‌سابقه‌ای که اواخر ژوئن غرب این قاره را فراگرفت، بیش از ۱۰ هزار مرگ مازاد ثبت کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/133695" target="_blank">📅 12:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133694">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما هر جا که لازم باشد، از ابزار نظامی برای دفاع از منافع خود استفاده می‌کنیم و هر جا که اقتضا کند، هر جا که مصالح کشور ایجاب کند، از ابزار دیپلماسی استفاده خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133694" target="_blank">📅 12:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133693">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: اگر مشاهده می‌کنید که دیدگاه‌ها و نظرات مختلفی درباره مذاکرات مطرح می‌شود، به این معنا نیست که مخالفان مذاکره، طالب جنگ هستند. ملت ایران، ملتی صلح‌جو و خواهان آرامش است.
🔴
هر جا که دیپلماسی تأمین‌کننده منافع ملی ایران باشد، قطعاً همه یک‌صدا از آن حمایت خواهند کرد.
🔴
در مورد شیوه و کیفیت انجام مذاکرات، طبیعی است که دیدگاه‌ها متفاوت باشد؛ اما درباره اصل موضوع، الحمدلله، اجماع نظر کامل وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133693" target="_blank">📅 12:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133692">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfahtM1GYT1fwSp9QO4dVzyawGEOw_GlkprByKtx7mEGO0DZZZSIR44uowS5v-Ao-atGQl1PjsEpmdcHuoW3R1GL8Z3-OngxM-WQdbL-b3LaDPK1wpvFRVK0hJb1Zwq-dBvEpbJo8m0_Bhi9Ra7JXp7cs7vfoUTIOtBoDZ2cut9hHlT-YXzCjSWpbTSeDG5tLNcads1_IZfneyDdBd1yqWrY20NWoccG1ZOP1EoMFBgaq5rtb66j2-BjqCPYyOLmbCSK26RCiVIlx8GsF2WKoTfnej3rIUsaKcU2Vh3AbYBBko0iAX1vQeJvNt1zGWP4PVUwgFwkqRa4_6C6tIY1lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرود یک هواپیمای دیگر در فرودگاه صنعا
🔴
شاهدان عینی در صنعا از فرود یک هواپیمای مسافربری در فرودگاه این شهر در ساعت ۹ صبح امروز به‌وقت محلی و خروج آن یک ساعت بعد خبر دادند.
🔴
برخی کاربران می‌گویند «این هواپیما متعلق به شرکت ایرانی ماهان است» اما مقامات یمنی هنوز خبری دراین‌باره اعلام نکرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133692" target="_blank">📅 12:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133691">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
روزنامه هاآرتس به نقل از منابع: حملات ایالات متحده به ایران، بر اساس اطلاعات جمع‌آوری‌شده توسط سرویس‌های اطلاعاتی اسرائیل استوار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/133691" target="_blank">📅 12:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133690">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما مدت‌هاست از دوران مهدکودک فاصله گرفته‌ایم، اروپایی‌ها اگر دوست دارند در همان دوران بمانند و به همان شیوه در برابر قلدری آمریکا رفتار کنند، به خودشان مربوط است.
🔴
ما ورودی نداریم؛ اما حق ندارند این رویکرد مهدکودکی خودشان را در رابطه با کشورهای دیگر، مشخصاً در مورد ایران، تسری دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/133690" target="_blank">📅 11:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133689">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
بقایی اعلام کرد که سفر لاوروف به تهران در حال برنامه‌ریزی است و زمان و تاریخ آن به محض مشخص شدن اعلام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133689" target="_blank">📅 11:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133688">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مقایسه ایران با اسرائیل از سوی هاکان فیدان حیرت‌آور است
🔴
ایران هیچ نیابتی در منطقه ندارد
🔴
دوستان ترکیه‌ای ما باید در این زمینه توضیح دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133688" target="_blank">📅 11:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133687">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfbi_Kk6DI5Wkrns4sQj-0METgddQdkrguUJ-vuCxUVIZlKrRHBpcrInr33fQsz1ne6SUKPzX1oQQiMzjXvYCJT9wS3ohm2QswGQ0TXwfk0c4HQ7kK9zYsULVsSwPIjl1BQpv9ZJfZj_whout8M3kfxWY2D_WW8ttJLDIeA1M5GOw2TjZdmKrWAMgr3IpHCM8JiKi81ToU_3flgevqdL7GneXdQgLzH4xfxMsbgD-e2MLYVKtSvLeg0E3lMNHS4frGOLElGH7u37n4j0BweqL_7hbphAl6zc9lPYQI6bUuCz7FyRYZ54lu0xriWz3z5j3la66V_3L3qCSYpvzoIHwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشف و ضبط 375 کیلوگرم طلا در پرونده فساد معاون وزارت نفت عراق
🔴
دستگاه قضائی عراق 375 کیلوگرم طلا در پرونده فساد عدنان الجمیلی معاون وزارت نفت عراق کشف و ضبط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/133687" target="_blank">📅 11:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133686">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: آمریکا با تحریک کشورهای منطقه سعی کردند مسیر امن تنگه هرمز را دور بزنند و بند ۵ یادداشت تفاهم را نقض کردند و امنیت کشتیرانی را در منطقه به خطر انداختند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133686" target="_blank">📅 11:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133685">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ایران با درخواست آژانس برای دسترسی به تاسیسات هسته‌ای ایران موافقت نمی‌کند
🔴
ما به هیچ کشوری در منطقه حمله نکردیم و حمله نمی‌کنیم، ضربات دفاعی ایران صرفا علیه پایگاه‌ها، امکانات و مواضع آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/133685" target="_blank">📅 11:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133684">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96903b5d85.mp4?token=qwYcaEQuNNfmBwKTF3VmLlPEY1J3BDqvyWo66eW79UHU6JHnHPsOdwp05Z8LR9FbFOXEUVx2YaGzMK8hK1Sz_E957JnmdgOmFIaEXuqIeuRn8lT6tkOQTes1to2HNh9h_XKYGMAx4V_KSC8iwD_F5GRG6nXOuJzw_d141yx_KzxVHdl_m-WFUTdtsD_sfdLTQMzWTHrOMgY35CMwacc09CCoPlEhdsWOqzFAvCtN-QqqSB6NsN2RpdkB75ebf4BtYEwKphpUEOO7epo5ySkHA7f1Srs5AcFfnqbYp8XKlR1u30PIwbqszXTd1aphRKnoFQjL3tv8DOd7xc1P7ORVWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96903b5d85.mp4?token=qwYcaEQuNNfmBwKTF3VmLlPEY1J3BDqvyWo66eW79UHU6JHnHPsOdwp05Z8LR9FbFOXEUVx2YaGzMK8hK1Sz_E957JnmdgOmFIaEXuqIeuRn8lT6tkOQTes1to2HNh9h_XKYGMAx4V_KSC8iwD_F5GRG6nXOuJzw_d141yx_KzxVHdl_m-WFUTdtsD_sfdLTQMzWTHrOMgY35CMwacc09CCoPlEhdsWOqzFAvCtN-QqqSB6NsN2RpdkB75ebf4BtYEwKphpUEOO7epo5ySkHA7f1Srs5AcFfnqbYp8XKlR1u30PIwbqszXTd1aphRKnoFQjL3tv8DOd7xc1P7ORVWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه در واکنش به مرگ لیندسی گراهام: حضرت عزرائیل، عادل است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133684" target="_blank">📅 11:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133683">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133683" target="_blank">📅 11:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133682">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ادعای ترامپ درباره توافق ایران در مسقط مطلقاً واقعیت ندارد
🔴
دروغ‌گویی بخشی از الگوی رفتاری هیئت حاکمه آمریکا شده
🔴
مذاکرات روز شنبه در مسقط صرفاً متمرکز بر موضوع تنگه هرمز، در چارچوب بند ۵ یادداشت تفاهم، بود
🔴
تلاش ما این بود که با مشورت عمان به سازوکاری دست پیدا کنیم که عبور ایمن کشتی‌ها از تنگه هرمز را فراهم کند.
🔴
متأسفیم که به دلیل فشارهای پیدا و پنهان آمریکا بر عمان، این امر محقق نشد.
🔴
ما در مسقط راجع به هیچ موضوع دیگری نه قرار بود صحبت کنیم و نه صحبتی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/133682" target="_blank">📅 11:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133681">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2509b9fff.mp4?token=Zo4DT4s5JA59kD3r_XOqnullrnrJZKucmWrDvA3fpSHCvDsseonJXZEk0T7KrRlPjJX5I0k22iFs3OwvOcAxrksh8u6akt7VF1ShLU4xP0rx2XUvG2yKpPBqSuBwOV4pjrhzUtgg8YocowpelNr400CAH4ca7sSCYZiQgtCZabhL-b1lzEe5nhFUUAlHhZ_z_3XJ951B4dDKWDujXsGet8MfClcdS4E6w-KmzxcnSawjnVEEGAWMADUpKU_qjbC6AnLoo8qidBTOTPAogNhknhIiNlpBS55wUxRPA3p_n7Km3CLGmaFdXBPV2xBv8g2Mr-CRGXURpN2QUBXRYLYgKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2509b9fff.mp4?token=Zo4DT4s5JA59kD3r_XOqnullrnrJZKucmWrDvA3fpSHCvDsseonJXZEk0T7KrRlPjJX5I0k22iFs3OwvOcAxrksh8u6akt7VF1ShLU4xP0rx2XUvG2yKpPBqSuBwOV4pjrhzUtgg8YocowpelNr400CAH4ca7sSCYZiQgtCZabhL-b1lzEe5nhFUUAlHhZ_z_3XJ951B4dDKWDujXsGet8MfClcdS4E6w-KmzxcnSawjnVEEGAWMADUpKU_qjbC6AnLoo8qidBTOTPAogNhknhIiNlpBS55wUxRPA3p_n7Km3CLGmaFdXBPV2xBv8g2Mr-CRGXURpN2QUBXRYLYgKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: بیانیه سه کشور اروپایی مطلقا هیچ وجاهتی ندارد/ کشورهای اروپایی اصرار دارند که واقعیت‌ها را وارونه ببینند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/133681" target="_blank">📅 11:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133680">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه در نشست خبری: هیچ‌کس نمی‌تواند جمهوری اسلامی را متهم به نقض عهد کند. در همه موارد، تکالیف ما و طرف مقابل روشن و به‌صورت مستند قابل اثبات است که طرف مقابل با بهانه‌های گوناگون بخش‌های مختلف این یادداشت تفاهم را نقض کرده است.
🔴
در ادامه مسیر هم به همین نحو عمل خواهیم کرد؛ مادامی که طرف در روند استمرار نقض تعهد باشد، جمهوری اسلامی  نیز متقابلا از اجرای تکالیفی که برعهده گرفته، خودداری خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/133680" target="_blank">📅 11:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133679">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه درباره تفاهم‌نامه اسلام‌آباد: در اینکه [تفاهم‌نامه] دچار مرحله بحران شده تردیدی نیست.
🔴
ایران هیچ وقت پیشقدم در نقض تعهداتش نبوده است.
🔴
طرفی که مستمرا مرتکب نقض عهد شده طرف آمریکایی است.
🔴
اینقدر کم صبر در پیمان شکنی بودند حتی اجازه ندادند حتی بازه زمانی یک ماهه در بند پنجم درباره تنگه هرمز دوره‌اش انجام شود.
🔴
از همان روزهای نخست شروع کردند به دبه درآوردن.
🔴
اگر ۱۴ بند یادداشت تفاهم را در نظر بگیریم اجزای مختلفش را آمریکایی‌ها در این مدت کوتاه مثله کردند
🔴
ما از ابتدا گفتیم تعهد در برابر تعهد. مادامی تعهدات خود را اجرا خواهیم کرد که طرف مقابل به تعهداتش عمل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133679" target="_blank">📅 11:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133678">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما در مسقط صرفاً دربارهٔ تنگهٔ هرمز با عمان مشورت کردیم و اصلاً قرار نبود موضوع دیگری مطرح شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133678" target="_blank">📅 11:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133677">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
هزینه هر واحد از پهپادهای انتحاری دریایی آمریکا در حملات اخیر به ایران بیش از ۲ میلیون دلار برآورد می‌شود
🔴
سنتکام همچنین از پهپادهای هوایی «لوکاس» استفاده کرده که نسخه‌ای الگوبرداری‌شده از پهپادهای شاهد ۱۳۶ ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/133677" target="_blank">📅 10:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133676">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
مسئول سیاست خارجی اتحادیه اروپا:
تفاهم‌نامه وجود دارد اما رعایت نمی‌شود
🔴
اروپا آماده کمک است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/133676" target="_blank">📅 10:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133675">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزیر امور خارجه فرانسه: تحریم‌ها علیه ایران لغو نخواهد شد مگر اینکه این کشور برنامه هسته‌ای خود را کنار بگذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/133675" target="_blank">📅 10:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133674">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
مدیرکل امور مشتریان توانیر : اطلاع‌رسانی در خصوص برنامه‌های احتمالی اعمال محدودیت برق در سراسر کشور، دو روز پیش از اجرا صورت می‌گیرد و بر این اساس، اطلاعات مربوط به قطعی‌های احتمالی تا روز چهارشنبه نهایی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/133674" target="_blank">📅 10:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133673">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وزیر خارجه بلژیک اعلام کرد که این کشور خواهان تحریم کابینه اسرائیل و شهرک‌نشینان به دلیل افزایش خشونت‌ها علیه ساکنان کرانه باختری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133673" target="_blank">📅 10:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133672">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزیر امور خارجه فرانسه: تحریم‌ها علیه ایران لغو نخواهد شد مگر اینکه این کشور برنامه هسته‌ای خود را کنار بگذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133672" target="_blank">📅 10:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133671">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
دولت مرز ایران-ترکیه را برای واردات خودرو باز کرد
🔴
براساس ابلاغیهٔ جدید گمرک ایران، گمرک بازرگان از ۲۷ تیر به‌عنوان گمرک مجاز برای ترخیص خودرو تعیین شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133671" target="_blank">📅 10:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133670">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
آلن ایر، عضو تیم مذاکره‌کننده آمریکا در برجام: نظم جدید در خلیج فارس نیازمند گذشت زمان است تا به تعادلی تازه دست یابد، اما قطعاً در این تعادل جدید ایران به مراتب خطرناک‌تر از قبل ظاهر می‌شود
🔴
واشنگتن برای دستیابی به توافق هسته‌ای جدید، ممکن است ناگزیر از پذیرش «افزایش نقش و کنترل ایران» بر تنگه هرمز باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/133670" target="_blank">📅 10:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133669">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikmvURwr9CFGPIidu44OP5u7WTkxyq-flI5MLbv-FTjD9ZoZsVtnrCOKq43MczhLYzBVwup_d2q8E0tVPxZ2l4IjJkMv-5mDfDcmYwz8SyqCc2oZxz46P2qsziRQY2DP0Ep43In2yix9qB4_l8WXQiC0tb-O4SdBTVivHQk5lyDfEPoKA42pvjqL_VK99s6ZN-rHX2QpvH_Bt0b9VkLYivfwZVqDfK3x5U3QNOx3Nh0gFRcdkudKfKpNXyJse8eXwl3roXkywisUfRHWEtOUVLa4AxcYRqHWZYogr8tjvc3oIrhsJv5lIZi1ypuBc-f4EF6vL_DLhjCcBgMNLulkFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: ضروری است شعام یا مجلس مقرره عملی را مصوب کنند که پاسخ نظام درصورت هرگونه سوءقصد علیه رهبر انقلاب، مقامات لشکری و کشوری از قبل مشخص شده باشد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/133669" target="_blank">📅 10:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133668">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ts_LbUwL5cBqrfv_Vonl9RBSzrQ4rH2K5PfULgSZv3XgkLNJ6Wr2Eox-iLcli_qc8jDIEM766EpB7qiFOfbojzuUIQ-abDzIBqHU6IIgo9BDS5qRMOYmlWl3zAmg0EnOBHztVBX41skue7e7moeRdL6dKJPzhp9UJRVjI7CWMMaqtiHj1nhDQYMsWSoJ1o_5vGjCpHtzLOx4-norANCzF_4VAn2F29RrwbOGHhH3seKFpVoOkVacKQOsYs85gctS9Q7Nw1vRBfica13n3DXnbreUOjlvOTFaKxKuNMWQoItkyPX7XeL9bWybYNxH2EPhbQNNjtEDEqpV0PmcDkCJTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست وزیر عراق عازم واشنگتن شد/الزیدی طی سفری رسمی و در راس یک هیئت بلندپایه عازم آمریکا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/133668" target="_blank">📅 10:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133667">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
انتقال سهمیهٔ سوخت به کارت بانکی کلید خورد
🔴
براساس مصوبهٔ جدید هیئت وزیران، وزارت نفت و بانک مرکزی و وزارت ارتباطات مکلف شده‌اند که زیرساخت‌های لازم برای انتقال سهمیهٔ سوخت از کارت هوشمند سوخت به کارت بانکی را ایجاد و بهره‌برداری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/133667" target="_blank">📅 10:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133666">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IntNMHGZCZjxxa9tcfVCWt8LMZ_-hIBWeyjzAxnIGndhgE7I3GfaXVWN-ewm1IdJSp0YIjeMwv5ul2M8Jn93oJrBFcm-JjWnB1atBwZ4lHeG5Z5jxkl0piaLpBEkooSr6mybdbKrqAXelvzA_Y4--Sqg2HQzbYaXtOXiBTdgYwsXQIZkXWcSVBlR9yU4txXsHew_nIc5stflECy3DzYBZFWNAagNxoznpMowbMnLE7mFfojwHErCthdnh2JwaDaJzWoyFrm8Jgvm2Rs6kqcvXd4UOo8dgh0Ce3mqsxmw3WSeteqQiUVJt60ovbS1TBYr-NT6EgTmQu_3l8N7tPueNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارس: تو بندر پهپاد پیشرفته آمریکایی زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/133666" target="_blank">📅 10:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133665">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9627a64323.mp4?token=PzStnIfxzpSjorvD1g3K2U8Kj63RtCGMZ3Ra5umBWg2OZ7MDDTWxN7hoW9UccgXxnJ6e4G-w64tXg7VjvkBiaedxOLfzL28SEgqulpmEPRFAxxm7EPHWAtblpwEgfs41il9ggCjrxGNvPRQbTkBUnPfculs9fqc02KeodpGpY9VnhyM9zZYNHU0zwWWC9IzEPP54syLZrr23q1Lvv68K6pjXAl4QDXyFZFuwWR5nuVDX8y_StALShLnkyKyXEUqVE1lTicSzVOcOHZloBTQdWETqF55Xw1hskaJPHxn2FSMVxs-PQ7KdmQM9a5-CahK1x2cpvV53ml4P2WJnwuEBYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9627a64323.mp4?token=PzStnIfxzpSjorvD1g3K2U8Kj63RtCGMZ3Ra5umBWg2OZ7MDDTWxN7hoW9UccgXxnJ6e4G-w64tXg7VjvkBiaedxOLfzL28SEgqulpmEPRFAxxm7EPHWAtblpwEgfs41il9ggCjrxGNvPRQbTkBUnPfculs9fqc02KeodpGpY9VnhyM9zZYNHU0zwWWC9IzEPP54syLZrr23q1Lvv68K6pjXAl4QDXyFZFuwWR5nuVDX8y_StALShLnkyKyXEUqVE1lTicSzVOcOHZloBTQdWETqF55Xw1hskaJPHxn2FSMVxs-PQ7KdmQM9a5-CahK1x2cpvV53ml4P2WJnwuEBYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از مراسم ساده تشییع جنازه امیر سابق قطر بدون هزینه میلیارد دلاری
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/133665" target="_blank">📅 10:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133664">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سنتکام فیلمی از حملات جنگنده‌ها/پهپادهای تهاجمی یک‌طرفه و موشک‌های کروز به اهداف نظامی جمهوری اسلامی منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/133664" target="_blank">📅 09:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133663">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzJ3suYszzsH2C26zQHCXWGqXlQGqbi8CNy9WU93b0guURd3tNonrdU36KyzPIGT2CrVpoyMAwvTJOiW6xWcwBbZrGVv_2ZOtUgE8YiWvjBu57oSRjlCXnw-iJB3q0NZtIRI9UGeBs0AhAqTlBK7N0sT8QE6uhmBR2C8bb8ve31NXA6WcoAVGwbgZsg04RTjzvYpmMKZEbH-GgynlQdJq63EzmirdV6H63_CPLrLZqwm5e7jXNlVk86wWm0vAd8LSMMKwkAjS8OOiz8HxCH8qBq4HAWMcLmK2A2vV0CAXwMdGMmr1KXfzoPo4bq_WjW6Sx83fQEbgFD-ZZL3aHAX5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تنگه هرمز همچنان بسته است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/133663" target="_blank">📅 09:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133662">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سپاه: تاسیسات و زیرساخت‌های ارتش آمریکا در بحرین، رادار دوربرد هوایی FPS و رادار کشف شناوری در پادشاهی عمان منهدم شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/133662" target="_blank">📅 09:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133661">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری/ وزارت کشور بحرین از به صدا در آمدن آژیرهای هشدار خبر داد.
🔴
این وزارتخانه از شهروندان و افراد مقیم در کشور خواست تا به نزدیک ترین مکان امن بروند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/133661" target="_blank">📅 09:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133659">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e6c1cd43.mp4?token=RJxLxk0_Lp3hQJ7h_52cGasUEgBw8ssAQUmFubFvQLO94N8vZrStXy--7XIK8m8nXSou0b2gsxCdbjRCCn_ELo3ui3jSgl2B3X0MAnO8gyEM50CNt2S26z6OtXzAQwbCT9pYWoKoTmAJIR7c8ocnLV9eLa6TESPW35Fej7eVvhamguOZd1yHEuVaa-b3vHAxigJIbzngn9bdUAUK_xMNjSSYxNpPikQWXl0pZU8biTsv7QyTALmEZ0QiRI__QThN_B4-JdrZMIP2h35DgT5J975KrNh7J-z0yr9iH_CjkYFFBftjuVRNcIM-rN1t4kLxzfEN1Eg7WqIvFjDOwg8hGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e6c1cd43.mp4?token=RJxLxk0_Lp3hQJ7h_52cGasUEgBw8ssAQUmFubFvQLO94N8vZrStXy--7XIK8m8nXSou0b2gsxCdbjRCCn_ELo3ui3jSgl2B3X0MAnO8gyEM50CNt2S26z6OtXzAQwbCT9pYWoKoTmAJIR7c8ocnLV9eLa6TESPW35Fej7eVvhamguOZd1yHEuVaa-b3vHAxigJIbzngn9bdUAUK_xMNjSSYxNpPikQWXl0pZU8biTsv7QyTALmEZ0QiRI__QThN_B4-JdrZMIP2h35DgT5J975KrNh7J-z0yr9iH_CjkYFFBftjuVRNcIM-rN1t4kLxzfEN1Eg7WqIvFjDOwg8hGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای شاهد در حال حرکت به سمت پایگاه‌های نظامی آمریکایی در منطقه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/133659" target="_blank">📅 09:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133658">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ2dnNuaZ1APNo1yAhTSGRGdSnxL4BTZlkjyfUfR0R3Lkxd0EIz55z5xjg_hLRN_LfbNR6nKSsoIP7z2jsfXBQIHRSCVvJijtIJFrQoGves9Wwgr4ytfKKtVE9Iqb5S1YUJzWizOhezMfJBSonKY-RoQLdlSePI7CNllPAgOm6JTFKsC4Plt7fEV5NZUyuW62GctVvhogtlLggt4QOSj5cLE1Q0ouqTTNq8RzofJSayBwFbIPfNyO9w07BtAE_PZA70Tc7ltDxT13dnajUQ8-vuskxMgIMlIONR8aPZteqrfpTzi-4uua98-E7EUCmrg-4YQVMBfmeVBspE31f9FdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نامه برادرانه شریعتمداری به عزرائیل!
🔴
شریعتمداری: ممنون که پیام انتقام را شنیدی و جان سناتور آمریکایی را گرفتی اما گله‌ای دارم که چرا صبر نکردی ما خودمان سراغش برویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/133658" target="_blank">📅 09:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133657">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
شرکت کپلر اعلام کرد روز یکشنبه تنها ۶ کشتی از تنگه هرمز عبور کردند که کمترین تعداد در پنج هفته اخیر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/133657" target="_blank">📅 09:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133656">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/133656" target="_blank">📅 09:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133655">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
تسنیم : پدافند هوایی ایران، یک پهپاد انتحاری یک‌طرفه "لوکاس" متعلق به نیروهای مسلح ایالات متحده را در نزدیکی بندرعباس رهگیری کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/133655" target="_blank">📅 09:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133654">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8c21ebc3.mp4?token=Cjm6r5YHOmXxgoIBriEnwi2ScPbigp60uBd-6qxRHtU_eWC6c0qkcUzNchBADsXBUVR9jPkRMcn3cqLSrY03XO-k9b3B1E0Vq0OLEFUvDkpxlRIVUSxzM8kv8YF9E2QMdMHJMdV6wOxR4X4eZ6yCgeNmZOlQ1BlTuv88TXMHkINSwg7Zw26LPJPz2h1t_J7n_sAQnpRhGP6fAZ5X16HPRfUtR2__TrZurHyjZLw5KC9j6xKdySVyqEN-DFQUurm4lDRv1ZmijjEbJyL-XhCyZr_r3DiYNcINrbN1b5LKRDdMHU-uHCoZNV9cSKOWCTkmdtrUiI5WdU9aEAPWGfv-hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8c21ebc3.mp4?token=Cjm6r5YHOmXxgoIBriEnwi2ScPbigp60uBd-6qxRHtU_eWC6c0qkcUzNchBADsXBUVR9jPkRMcn3cqLSrY03XO-k9b3B1E0Vq0OLEFUvDkpxlRIVUSxzM8kv8YF9E2QMdMHJMdV6wOxR4X4eZ6yCgeNmZOlQ1BlTuv88TXMHkINSwg7Zw26LPJPz2h1t_J7n_sAQnpRhGP6fAZ5X16HPRfUtR2__TrZurHyjZLw5KC9j6xKdySVyqEN-DFQUurm4lDRv1ZmijjEbJyL-XhCyZr_r3DiYNcINrbN1b5LKRDdMHU-uHCoZNV9cSKOWCTkmdtrUiI5WdU9aEAPWGfv-hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ی عبور و برخورد موشک بالستیک سپاه به‌هدف خود در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/133654" target="_blank">📅 09:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133653">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ارتش اردن اعلام کرد که چهار موشک بالستیک ایرانی که به سمت این کشور شلیک شده بود را رهگیری کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/133653" target="_blank">📅 09:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133652">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
الجزیره: حرف‌های ترامپ درباره تنگه هرمز با واقعیت زمینی تفاوت زیادی دارد
🔴
تناقض در این است: رئیس‌جمهور آمریکا مدام از چیزی می‌گوید که آرزویش را دارد، اما واقعیت در میدان کاملاً فرق می‌کند.
🔴
واقعیت این است که ترامپ گرفتار شده است. او سعی دارد القا کند که تنگه باز است و این موضوع بر بازارهای مالی جهانی تأثیری ندارد، اما ایران به‌وضوح بر موضع خود پافشاری می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/133652" target="_blank">📅 09:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133651">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1591411fc9.mp4?token=gxj5hmrYise492BDx7ltJ-ftn_sdXIBXGFSsb10Ic_FKGuQ7Pj3O1sW6Bvwjet2j8iH4DLdrdI_RqA3CAd8ezix8n3eyu2utopHUhTGeu9Ko1kxJRWMpPM6MRbGUbj43aF4yNdgCaN7H1VPQGOBaR0ZVVDr1HsGpclNyEkeYlZTw6t2nKpwhtgQs5zniwmpEKZMXLFugLxaASYOJzOsCJFs39zFOfg7t-Pdx77sklAfWRWnzLZU5gO4OmVFaomcXsfjXpSqkPIEhfdP0YaG8papIBxLIds0CO0qKb95-ObE3XfHxFpa39wNtn8qr6MTDQXEjlGwibGIEy4knM0CotQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1591411fc9.mp4?token=gxj5hmrYise492BDx7ltJ-ftn_sdXIBXGFSsb10Ic_FKGuQ7Pj3O1sW6Bvwjet2j8iH4DLdrdI_RqA3CAd8ezix8n3eyu2utopHUhTGeu9Ko1kxJRWMpPM6MRbGUbj43aF4yNdgCaN7H1VPQGOBaR0ZVVDr1HsGpclNyEkeYlZTw6t2nKpwhtgQs5zniwmpEKZMXLFugLxaASYOJzOsCJFs39zFOfg7t-Pdx77sklAfWRWnzLZU5gO4OmVFaomcXsfjXpSqkPIEhfdP0YaG8papIBxLIds0CO0qKb95-ObE3XfHxFpa39wNtn8qr6MTDQXEjlGwibGIEy4knM0CotQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد های اوکراینی شب گذشته به یک انبار نفت در شهر میخایلوفسک روسیه حمله کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/133651" target="_blank">📅 08:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133650">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Epg1rbiv9bEM1Zg8knH_6Xbh6BV-q_dnk9l5SEsdEuqIYHMZDdLMavWW7UHIoxCIUF0ZyrTWoVlvc0ll8lAWedXEofoPU-9QLP1EUnCP0bvsnQghFuo0mfaOWfyiU-3K4GQQWFJT2LPSfVz0uIRX9-Riv3iIJ2ccWpULw_m1UW2eim3geFBunpTc-kPv00Bd96EaZyMVgSdb08hFuo-DanYSb2YL4p4fyKi2kX-3zfThaRt5c29UEmGw-zB2IQXCTjaKZSeeZC0ZEEK67ND2E1U9ZB7VfqW87P8zGDj7tHgqHfMCvrd5P-mA4oXu7xoKdV8evyxO-fOe43itdGTbHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال
:
59% امتیاز تایید. کاهش قیمت ها همراه با کاهش قیمت نفت و گاز متشکرم، پرزیدنت دی‌جی‌تی
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/133650" target="_blank">📅 08:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133649">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L66l9fwMWNLpXobD0YHkiehd93vZ7ApH3LWiHid5kVvTIUSTmuhd1rGGyvaOAS2w7HCCy9Sx11aeDFGWHB1u2dE5zYiGfuvJSeIxGwvjt6d8IEZNMn_7ZiOv33KxJYRbyMJODru2_Bg_m6y4w3l_4oisCTe4QoPsiHDSQnYP4gDmDec6RLbZt9JOWM8mVk7s43IYbOHd4OSkwHg3uONhiC_v-l4MH6WQft19xztorRn67_oai-R9OYkt2zC122SoclcBfOwHeJY-GWQbu4zstHpUYjcjIJgVmjFKFI_9Tk4K8xVA7l7Kye7VU36CcU1_jzdkIvHQN6HIduFRqdodEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت به مرز ۸۰ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/133649" target="_blank">📅 08:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133648">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
منطقه المینا کویت هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/133648" target="_blank">📅 08:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133647">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
تکذیب شایعه قطعی برق اهواز و حمله به فرودگاه اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/133647" target="_blank">📅 08:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133646">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
دفتر پزشکی قانونی واشنگتن: لیندسی گراهام بر اثر پارگی آئورت ناشی از بیماری قلبی‌عروقی ناشی از تصلب شرایین جان باخته است.
🔴
پس از تکمیل آزمایش‌های سم‌شناسی و بررسی‌های میکروسکوپی، علت رسمی مرگ و نحوه طبقه‌بندی آن به‌صورت نهایی مشخص و در گواهی فوت ثبت خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/133646" target="_blank">📅 08:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133645">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
برخی منابع مدعی شدند که مقر یکی از شرکت‌های تجاری آمریکایی در بحرین مورد هدف موفق قرار گرفته و درحال سوختن در آتش است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/133645" target="_blank">📅 08:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133644">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
منطقه المینا کویت هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/133644" target="_blank">📅 08:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133643">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5EPP_8i34LQCKvSRes4cEfZLrG6t4yEQlkIRUuREFpzSMpj0Mw37D10WzYi-03mo7alz2uGwfOQrZDgly4bFQoOEqW-gsQD9xX5swDBb_Rt18A5E3Fl8Mnc2UibCkyXPCUoOxHjBYrr262tWRhZ9HoMaLFXMYITJWVrPQsuV4d3sXta95ezY_2mKU3sIy1y-XLMEjr78Jd-DWK3p7hiM6iXNA0siZs9fT2nRP4JZwqbF4wcYsQxh8eKixU7a5DTNnrTmspYEDUq1gW162D-mGB9lrWHLMiilD5z5a62ZHBct8daCSc0qheem8AmTYt6kviq5I_SEAeiUWPCW1n88g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه: حملات امریکا به ایران در ۲۴ ساعت گذشته را به شدت محکوم می‌کنیم/ آمریکا با مداخله در اجرای ترتیبات لازم در تنگه هرمز توسط ایران، موجب بازگشت ناامنی و اختلال کشتیرانی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/133643" target="_blank">📅 08:38 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
