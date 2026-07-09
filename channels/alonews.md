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
<img src="https://cdn4.telesco.pe/file/qRS-uAkzLeqVWn50OxhChxm-wHS6G6XWyB9bIZKZAHeLP03JKx-bm3B2CBBjCOuHv13uOO39Kya2DeGEy9QprTUHHTQ7ck2Wef4AK9Z-oGbL8u7k34kSuASUGNUhu1AQ-nWBuNjPhubPQRr-YhfVLPryQsZSCHXgxYT12kh9GA3X_Iuo0jJdWr_aGh_HcJbbBd67zhOPPttWi8d76HRNSWbtDREJy8-lXNYznHXAx6eZdkWUWApogTHg-5VyVZuiUBY502wrR1H8XWfrieFCKUDVqTtYjERZttBjiPFcWSUkfVqR936iI054xBuWmDdCRU_xve6Eob99BvFw13mjSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 925K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 12:21:09</div>
<hr>

<div class="tg-post" id="msg-132725">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHZDMd_HOpQSNt_gIUL5miMgBnbBqqPLID4AVEY7vSEozBw8Z0L407uAWwm6k44b5VdrEcdXXW9AbcQ4_-4Zc6ip99EorHU1Oh2Gp_j9Ku9LbxrQp_LXf-6v1Kr7k3v_eFU33-RXCP7tJLPqzpuzrFy6wKlfK18NSx0mkF_u4E0QtBqMUJ5pWoM9pkEa5pD1GLJirbVC9XpLlshDkAJidRaIpWgqEkAgLY-z2bF532l6lhMm0jtFBUHD4mI-sYIEOq0uw2sFbMcIFAkEYkrmKOzadtb9p0SNpV_mgtzmf1b4DwDKpvJP2Odwx4ONdbFgBBP4TfqBaqbZhllhrInbiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین وضعیت پروازها در آسمان منطقه، امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/132725" target="_blank">📅 12:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132724">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری / بوشهر صدای انفجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/132724" target="_blank">📅 12:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132723">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbPFiwAR0txri9P6ZC2cyCeItdB57-Uy_en4Kg3mYQfPkOS2jSm0SbihCaiZ3zLDJEEacsHtMR-f5p4SO0OFgqL26pAz5H-0u_s-m2PJp4CH27rjV9Q7XDpM6ubJXsOZ2LRPS68B3DdnGF7fFBpeFMGgKq5Al1TRoDiAi0U60VQ7M45HtHsQEBlv-4bmaaXgFJvfJrzam8bdcF6ggezGxE5dFcFozcVsqfCPfTmaUzeKRRUW9o4o6hvzzAjmkgnaCU_l_vCSvc20bYCw0O1JZZTUWH8sYKNuHfed3CeepXZxgQmL778CpSrxIQPyEIp8_oEL1nKeJxZxS5rA-so6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آثار حملات هوایی شب گذشته ارتش آمریکا به پل ترانزیتی و مسیر ریلی آق قلا
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/132723" target="_blank">📅 12:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132722">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سفیر انگلیس در تهران احضار شد
🔴
اطلاعیه وزارت خارجه ایران: سفیر انگلیس در تهران در پی تکرار اتهام‌های مقام‌های این کشور علیه ایران، از سوی مدیرکل غرب اروپای وزارت امور خارجه احضار شد و اعتراض رسمی تهران به وی ابلاغ شد.
🔴
ایران با رد ادعاهای انگلیس درباره تلاش تهران برای اقدامات ضدامنیتی، این اتهام‌ها را بی‌اساس و ناشی از فرافکنی لندن دانست.
🔴
وزارت خارجه ایران همچنین انگلیس را به همدستی با آمریکا و اسرائیل، نقش‌آفرینی در ناامن‌سازی منطقه و میزبانی از شبکه‌های ضدایرانی متهم کرد و خواستار توقف حمایت از این گروه‌ها و تغییر رویکرد لندن شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/132722" target="_blank">📅 12:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132721">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
فرماندار بوشهر: حمله به نیروگاه اتمی و جزیره خارک صحت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/132721" target="_blank">📅 12:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132720">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9swKQohgZgMRv5Wgeregrl3xG4i1gI7wosvqD-OlcNX9NeJ6-okWH8yOmXhUQAYpPneOn3HshaZU5p9JONE1X5pTYTU7g_xh5ecXFG3OcxB8eWLzpm47agmG68K216MSZ0-Cc0_xIFYCrP4amzHHhopdoKV8z-5EnR7G7sAJtKSNdXJFVQ99seCdUTe3D6S-PqYhHFeY1yQG6oezFOIlj6_Mv_TXdiGE3BqxH_EAcQCxx8LjNq8dXNkWUjejBKrhknrxbJpbjzjgQJLXiaSlO--v8GY4W1f97WMW5oJof3Wck_e-jA-pRayM4nP8Oodt-8DmFqfKa2FZYUYRy1jxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهم‌ترین گلوگاه‌های نفت در جهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/132720" target="_blank">📅 12:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132719">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سنتکام: توی حمله شب گذشته حدود 90 هدف نظامی در ایران زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/132719" target="_blank">📅 12:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132718">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری / منابع خبری از وقوع سه انفجار مهیب و پیاپی در بحرین خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/132718" target="_blank">📅 12:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132717">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnMuArSSEtA-vMIiRE-pwCpYDCtKDazVnYbncUs54bkVTpcxJpJQngzUAR3gyKIcZYWINd16uOgyOjuSaVOSb-6XBBlAyvr56QWJmx0IbrTcCgeXu91wVFtz-CW5UdRRZSCal1rndRyYMc7o6eQLI6XHxDS2debDaYj8-ElopdBsPRZtoLgopFPP5chGkqulc5-Fdymcy5nWDt5gz3z-NpaC3ZbL3aKrzqKi1KgllP_CrS09JlqHkC332Em_b6KHZUkWhplXCDCU6Egb_05z6bzERJ_GCI3ryywU4rrCi4G20K_a1t7D5iCZjValls9z5iszWh_bSqkyB-5DYrON9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌اکنون حضور 5 سوخت‌رسان آمریکایی در منطقه
🔴
مبدا پرواز ها از جایی است که ایران بعد از آتش‌بس به آنها حمله نکرده‌است: بن گوریون و العدید!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/132717" target="_blank">📅 12:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132716">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فوری / منابع خبری از وقوع سه انفجار مهیب و پیاپی در بحرین خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/132716" target="_blank">📅 11:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132715">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نخست‌وزیر عراق:  برخی گروه‌های مسلح تصور می‌کنند نیروهای ائتلاف بین‌المللی از عراق خارج نخواهند شد. برنامه‌ای برای تحویل سلاح تدوین خواهیم کرد و پس از پایان مهلت تعیین‌شده، سلاح این گروه‌ها در اختیار دولت خواهد بود
🔴
به زودی با واشنگتن اطلاعات امنیتی سیاسی مبادله میکنیم‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/132715" target="_blank">📅 11:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132714">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUOZKGx7LhSTKYBLqKp2ROobQT5f_2Sdq_bz90m4BJJHJWvzcvD5nYaYJFh7iqaS9w9SbBEnIHZnIm6eLyB_g2yL4VBTOGhbl0nCFbbwWnDYdf9VV4CawxtvDsMZ9dqsXcAJun7e_IgpM4KXsm26KNlmZgeN9BDEpQsVkvmVeBYsg0kdNG0JMB79wdsrVQo5XTORnGaHtP4jL8NJjVmXWihCQmFayOWPuZVtB14aLrsIwVzdbCftvJLzXvXznZs5mXk-qgv2nFSVNdemB5B-p0gR1ob0VNL726Cjt6QSRmOfLtWfTGJXNSRoaWdPSqZhu2jXdAv6J2lIN6YeR858eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با وجود درگیری‌های شب گذشته ، قیمت نفت امروز کاهشی شد و به ۷۶.۹۵ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/132714" target="_blank">📅 11:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132713">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f85ee64a81.mp4?token=BjK3yCGq9sq5LttfaoJ2ras9BO83TBsMo7VV3ebvpcgH0xVVJjdjg9YJD3Xw3Bcc7E9FtaQc19G29z64nNKXUycxdLtj_NQNML42AMA0U2BuZWfaN_21-hk3SOEiCT9NJin9Jt-yndMXjaTdKBhIEE_6TsZzv25dbErCaQQs1ng0t3nsURX9DGjJm1daQwH8-fVG2bzdaFjdAieaw0EgbQQDKI1fCyD214hkVpx-ARfNwwRayqhJcwBLDmcyDcpDmMxgStCHpQcv8HeqMiIOVnU7YnwaOf6KanMRWUZpUrJBoeBJ6YUCQ4VRC0RULRjN4zYJfhg29kMPVJwv-uzHiw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f85ee64a81.mp4?token=BjK3yCGq9sq5LttfaoJ2ras9BO83TBsMo7VV3ebvpcgH0xVVJjdjg9YJD3Xw3Bcc7E9FtaQc19G29z64nNKXUycxdLtj_NQNML42AMA0U2BuZWfaN_21-hk3SOEiCT9NJin9Jt-yndMXjaTdKBhIEE_6TsZzv25dbErCaQQs1ng0t3nsURX9DGjJm1daQwH8-fVG2bzdaFjdAieaw0EgbQQDKI1fCyD214hkVpx-ARfNwwRayqhJcwBLDmcyDcpDmMxgStCHpQcv8HeqMiIOVnU7YnwaOf6KanMRWUZpUrJBoeBJ6YUCQ4VRC0RULRjN4zYJfhg29kMPVJwv-uzHiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام ویدیویی از چند حمله به ایران منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/132713" target="_blank">📅 11:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132712">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
فرانسه خواستار خویشتن داری و ادامه مذاکرات میان ایران و آمریکا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/132712" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132711">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjEwhYDwVFxCtYAXnZLLyK6Zn3jJCcgYDYw20LOwB1tuH0Ynp5bwv0KKYi2jF2H85Gwje3OilDMCQMSLk8P7FMeRf00Cx1wI6StYTsFWeJADC7BtDrdfhZw-yb1rBClWStnkk44ARVXbi_zVBM3eTSo6lV0DC749TjhMqiwDd0w3SSxAeVvmoSBZlvyNmDG0M--f1F44FkgCFol_FerltOmDWJDq693GkYV-NyKYLyW3jk88F5C5H96V5_GQD7aRzl6T881l3FTb7rSjLfLFFU-IaY3WS8RxBSDqdoRApcj-bmrL0-e5isGdGdeRVcws7DABkIRdKCuIymnLc_JU-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنری در مشهد ، ما ترامپ را خواهیم کشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/132711" target="_blank">📅 11:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132710">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
آکسیوس: ترامپ آتش‌بس با ایران را تمام‌ شده می‌داند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/132710" target="_blank">📅 11:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132709">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
قطاری که عصر چهارشنبه از یزد به سمت مشهد حرکت کرده بود صبح پنجشنبه به دلیل حمله آمریکا در ایستگاه تربت حیدریه متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/132709" target="_blank">📅 11:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132708">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری / وزارت کشور بحرین:
از شهروندان درخواست می‌شود به نزدیکترین مکان امن مراجعه کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/132708" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132707">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDYO2mpeE8WfmXDMticpI-pC8_WeLYssrgIes7kCc5S0K-dn-hnid8cPOhiw2qEbOeKhjpHrlbn5Cu_O7s2c6iPNmFEMo7kdQNFyyDJjipVybuX4wuGpm0wPW7RsZJZyT8m3i_Wcvk12KkUG1GFSgUqvJ3vVBFH65bw6xZECtGk1OXnPUdXSm0EusgU7iYx-VLx8_EgcTttFHiHSJL22L-7jnYANva5NoBC3ASgcsbSAHDpOJ4P_0BUuVwQ93TSRlNrdhWtLi77BGNL1RTPefHzD702nGAMKzw_kGgauEgl48Xctu5IWs9B1J3KZGFLva8vJGUBHUhko0LVB5l3_YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه: حملات آمریکا نقض فاحش بندهای یک و پنج یادداشت تفاهم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/132707" target="_blank">📅 11:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132706">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6rMYMwLA745BNKYeH7BgjOW9d6N75nF5Nn_cJSt5Rq7H5f_lKaQlvOMV787VyDQ2IfGFrKYj8XL_JA4sXlhYUU83xuAl1ZfxZYWchbf5zrDMIm90m9ssidb84b0H-i_1WIY20zbrK7LTpgSa170Y1LpRBuO34liSi1szm50Tkq__NMBtpzptsIo45pe-0MHD8VhPY1ymWvL4q1OvPQ-OtsMVmpo1b0lsdID3qI69YIz3JJuU5lYyQYhcsIAj3VczLCO_QcIg_IkrOD9rFtlJaEmYMAJ1rWGilApfESGJ6W0jU6NxebSjwVTZcZBuSkChFM70fpZWLl-689Kn82XvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنر نصب‌شده در مشهد: بی‌بی را بکش!
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/132706" target="_blank">📅 11:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132705">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
حمله آمریکا به استان همدان تایید شد
حمزه امرایی، معاون سیاسی امنیتی و اجتماعی استانداری همدان:  بامداد امروز نقاطی در شهرستان کبودرآهنگ مورد حمله آمریکا قرار گرفت.
🔴
این حمله خوشبختانه آسیب انسانی و خسارتی در پی نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/132705" target="_blank">📅 11:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132703">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTnJAIYwywab8w8KJtCxyO_Ni1UB-u-hJ7_anTFix-GmtEMNnlKf7gjEzYtdac2Zyr8HCA-XvHRkJ58S4b5zkAg45yFXxfb7ucBcDjqrG07lQjYxhdUzvtCj_-nc62aMphxa9_6kA8PeIIQlHqAh8uWG02uZEyDDmSgBZmffiIRhhdWH15tAMAJgs4Iv1lOHWvXL89dpv4InXXmjT62yOOD78WDrQ-74CyJsjf1LbWAi1L3djkGd3TLco9b1uoEvxi3-HPNSrOOhld5tW5mnSvTXZYe1oG6VFKgL6awuJeQW5F19YYLvd8sRsN8GwbbAzY8Z8Jrl6Jh9utEJTr1bQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K9G7H_mUC_m7LYgL8juQ_lejz_qrPSrhT7MiEMbGJcH_7pg_m2uyVEJ3Hld7Ph4Jk55l2K87SV7r4mgKmioo8LyxCiubw_Y3z6J4W3VvhJF5rVwSP99bosyYUYJAVN6zwsZKFS_LjOMQDZNgq2bdGZ968aE3qtMWKeokZ8Qv4ZLks0ldLBLfjj23OepGQikn-9HWSfL3xI_P7HPsfvwV2t8c7WCXnawRRz6dJGc2bC4cz0VXlG5noZ6x3gItvx-5IkVy6e4a09DPulbjxC97LGtPZw6GoM1-PjyNIZqiYYJ11QXQMBuSx_vw_nIAoJKe6vojSq8h9vDBTjlI8QluFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم اکنون آسمان بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/132703" target="_blank">📅 11:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132702">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
صدای انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/132702" target="_blank">📅 11:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132701">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTLijMKpc-LCzGXK1NRvN_4mEhxjQMWpqVnJStqC19AZuK4wzh4ozHamNWu74mvTbmeOq5VkHQtyIR9hiubgQfL-6UHgllPXU4xbnAvjkuZfLhUm5toPav5WVVn0AyRjc4vCvFfOyJKfC7N0w8rKiwT6lcfaKGV0dOGyAVE5mY4fwplwkuBuZoU1lR7igm_4FKyQ1dGVkJU3ePtSahAjCAr71oZAlBp14p-svXVMHyqbKZMpsHubh3cLf-5S7THHdaurv1AqFMapcj-HNATh6DBVLl5BbKut_f5cCkoDmcyWbwHrbgqoVtDBY-zchzJEXT7Fn39FADaQhJLvxqrS-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جواد لاریجانی: برای سر عاملان ترور رهبر انقلاب جایزه بگذاریم
🔴
هرکسی اقدام کند به بهشت می رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/132701" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132700">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
صدای انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/132700" target="_blank">📅 11:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132699">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabdf1b7f7.mp4?token=mK56iP8G-sc_8jGUajOcMFxTf9mA-QKmR_Dx8EXtk9ZjMCFhkAVM2xMqtGlrvkPLr5muwVM7C8w06_bliHBNHaTfOshMF0SPyzH3xEhEomaWIy59ZXoZbXyb56Bi18sa-4CGr4jIhyAew8wjmVHxrN4DB0QCwrfGARTsKQNIPw3vIw5OSrfzrAUpnIjnaFbwc87uFWpxr8AyIi5ogCED3PoLCEYrV_Vp7zNZ5LdnQl7T8h3RsszW5eE-nRuDvAKC8rK3YTK3sfkkmIhUAU2aDbNDdDxe698OIMcqUCnIVh4HajV26tnex-7uvjJQmKwPmPcEUd-9WrPAbZMMKT-ylQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabdf1b7f7.mp4?token=mK56iP8G-sc_8jGUajOcMFxTf9mA-QKmR_Dx8EXtk9ZjMCFhkAVM2xMqtGlrvkPLr5muwVM7C8w06_bliHBNHaTfOshMF0SPyzH3xEhEomaWIy59ZXoZbXyb56Bi18sa-4CGr4jIhyAew8wjmVHxrN4DB0QCwrfGARTsKQNIPw3vIw5OSrfzrAUpnIjnaFbwc87uFWpxr8AyIi5ogCED3PoLCEYrV_Vp7zNZ5LdnQl7T8h3RsszW5eE-nRuDvAKC8rK3YTK3sfkkmIhUAU2aDbNDdDxe698OIMcqUCnIVh4HajV26tnex-7uvjJQmKwPmPcEUd-9WrPAbZMMKT-ylQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوريه در قبال لبنان به ترامپ تعهداتی داده است
🔴
سوال: آیا الشرع تعهداتی به شما درباره کمک در مورد حزب‌الله در لبنان داده است؟
🔴
ترامپ: بله. اما قرار نیست به شما بگویم چه گفت. او عالی بود و رئیس‌جمهور زلنسکی هم عالی بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/132699" target="_blank">📅 11:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132698">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/132698" target="_blank">📅 11:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132697">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فرماندهی مرکزی آمریکا (سنتکام) اعلام کرد نیروهای مسلح این کشور دور جدیدی از حملات نظامی علیه ایران را با هدف کاهش توانایی هدف قرار دادن کشتی‌های تجاری و ملوان‌های غیرنظامی در تنگه هرمز به پایان رسانده است
🔴
«سنتکام» اعلام کرد نیروهای آمریکایی چهارشنبه 17 تیر حدود 90 موضع نظامی ایران را هدف قرار دادند. بنابه اعلام این نهاد، این اهداف شامل سامانه‌های پدافند هوایی، تاسیسات کنترل ساحلی، مراکز ذخیره موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیکی نظامی در امتداد سواحل ایران بوده است.
🔴
این نهاد نظامی اعلام کرد این حملات پس از آن انجام شد که نیروهای آمریکایی شب پیش از آن نیز مجموعه‌ای از حملات تهاجمی «موفق» را در داخل ایران اجرا کرده بودند.
🔴
سنتکام تاکید کرد نیروهای آمریکایی سه‌شنبه 16 تیر نیز حدود 80 هدف نظامی در ایران، از جمله بیش از 60 قایق سپاه پاسداران ایران را هدف قرار داده بودند. سنتکام تاکید کرد هدف از این حملات، تحمیل «هزینه‌ای سنگین» به تهران پس از آن بود که ایران با حمله به سه کشتی تجاری در حال عبور از تنگه هرمز، «آتش‌بس را نقض کرده است».
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/132697" target="_blank">📅 11:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132696">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سفیر آمریکا در بیروت: انتقال مذاکرات لبنان و اسرائیل به رم به دلایل فنی انجام شده است. نشست رم ماهیت هماهنگی و اجرایی دارد و چندین نشست دیگر نیز برای پیگیری اجرای توافق لبنان و اسرائیل در رم برگزار خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/132696" target="_blank">📅 11:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132695">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
حرکت قطار تهران- مشهد متوقف شد.
🔴
در پی حمله به یکی از نقاط مسیر ریلی تهران-مشهد، راه آهن در اطلاعیه ای از توقف قطارهای مسافری در این مسیر خبر داد و اعلام کرد که بازسازی محل آسیب دیده در دست اقدام است و تلاش براین است در کمترین زمان ممکن مسیر ترمیم شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132695" target="_blank">📅 11:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132694">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3kjmixY9J6VeEgrrcEZ5iLlZoYMRmPUXMhzBhJxle8llcHGDCO3t7og1Mj7j1GQCWF9PuRRiHn6RKxh334xMRZQ_R8-V8OcOZLcAgfmAHC9-8vGpJckxQ579G6xNKK0EAN_jjQDg0PjVubRXxUVxEj1RVMb8p-PkDi5x4EDinSQSWgkFCL8n14mQmni234jtNDAv-TljWY5Vum1utKieyd0FZbR4VbflSq6T8v2FPiGe5-ni9_jgeo7LHaD8_nDWKgaezgmyDEYlyhGvgetfac6X7RsepRaThL4zS6whx92dYvX5HbPqcVBvXUlvMfwWspRvRIdhox_nDPl25PirQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۴ سرمربی از ۴۰ تیم حذف شده از جام‌جهانی توسط کشورشان اخراج شده‌اند.
@AloSport</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/132694" target="_blank">📅 11:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132693">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdcihVl0Eko1M-Sg3lgxwvhuRrc4MBd60n8uCKBUf720ZYBy8bCGeFWd3Etlgn3rRwrd9aMdlYpx0T287Osu1oLdYL3AI89F6fSCtWdRijVJnE-P_ByZeULs5XtSqM-VrlojYzmjJ5lWWXGtNa1JKVOgyDYfKpijYVrcR8Hw5P7ZUAG0MBYvw32lHEg8-P41BFpkyUFcOj5BLU1mdDBB3hOMLlxwLLn6relmnDkFY16DpSlaH-X8BLCysH-Hqxlg84MeMcLagj4Febt3KU4npZd9u7E3DaGZwFe2EQvqIUiGpJcoG4z75VMmhDbmtakCXiT8d_P7LO_2QUEOopQGWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکارد در مشهد: به سر بریده ترامپ نیاز فوری داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/132693" target="_blank">📅 11:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132692">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏
👈
بلومبرگ: تردد در تنگه هرمز تقریبا متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132692" target="_blank">📅 10:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132691">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
باراک راوید ، آکسیوس :
کاخ سفید در حال آماده شدن برای چیزی است که می‌تواند به دور جدیدی از نبرد با ایران در اطراف تنگه هرمز تبدیل شود که چندین روز و شاید حتی چندین هفته طول بکشد. مقامات ارشد آمریکایی به من گفتند که مدت زمان این کمپین جدید و شدت آن کاملاً به گام‌های بعدی تهران بستگی دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/132691" target="_blank">📅 10:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132690">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2D0q7malWbNTL46Z8sXODwFcD90J25e9rEehYbIdfRHxFOhVLraeeCkASDcj6zXSPjbOLgQUCAAN6A_RNa0QEP26yII9BXJ0F_FxiD2_lcwjr83PgumvMGe8aoFqZMYAaSSgYy94D4qcmZR_ltB67mbgHBNfjZcXVxk3hNVaG0W09O5ea4PndOZ0aWxZ5fq9EuYH6SIQXYCRfXv0Iy0Efpk0AbfKsayT_WivXafzDcf8JewafRAr3fhv7Uze0v6Sdp13rd1qFpIGVzLb2gQ6JgljdRadzg-u28aYbx0TbpLTGfTX2cwe1FQzkcj75imreTfJF2P-d4iq9MkKZki-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله آمریکا به پل ریلی آق‌قلا در شمال ایران، می‌تواند فراتر از یک هدف تاکتیکی باشد. این مسیر ریلی تنها حدود ۴۰ کیلومتر با مرز ترکمنستان فاصله دارد و از اواخر سال ۲۰۲۵ به یکی از مسیرهای انتقال کالا میان روسیه و ایران تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/132690" target="_blank">📅 10:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132689">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ بر اساس گزارش‌های وزرای خارجه و جنگ آمریکا در مورد تنگه هرمز، این پرسش را مطرح کرد که آیا ایران هنوز به دستیابی به توافق متعهد است یا نه؟
🔴
پس از مشورت با مشاوران ارشد امنیت ملی خود، او به این جمع‌بندی رسید که چنین تعهدی وجود ندارد.
🔴
این نقطه عطفی بود که باعث شد رئیس‌جمهور آمریکا چارچوب آتش‌بس را کنار بگذارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/132689" target="_blank">📅 10:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132688">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxhJxuUOrA9p_b1izV1lLXFig9614C-S1bWR4ZEB_Z5p9JqyimgnGHFDfxW5k5S7M54MiDOYxQB3lHjgYR5OIQmFWQjpxN6pG9QkFyy7rjOsnQDB6yBEC9NvKza90frfDDLZEH4oZi1605k1TYFs1i4tTXB8x3DMhVTDAuUogKUU8UZb78jVYn7mnFLWSY3NjjqL3esOw-3vYD-qA2r1y7VIZga35bvFq14ocICVrWNH9IGw2L2aTvimjyidCoE-oZv6y942Fp3IAr0fdcULAPf5vaMgxDpI7WzAmwhikcOlA1ClaxmLT-VAT0JGgaljiV8Pxr9sFQTAiUd5lzp4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: آمریکا هنوز یاد نگرفته است که زورگویی و بدعهدی دیگر بی‌هزینه نیست. شفاف بگویم: بزنید، می‌خورید.
🔴
دست و پای بیهوده نزنید که بیشتر فرو خواهید رفت: تنگه هرمز، فقط با ترتیبات ایرانی باز می‌شود نه با تهدیدات آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/132688" target="_blank">📅 10:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132687">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده، «سنتکام»، با انتشار ویدیویی در شبکه «ایکس» اعلام کرد امروز، بیش از 20 ناو جنگی نیروی دریایی ایالات متحده در آب‌های خاورمیانه در حال گشت‌زنی هستند و سنتکام به برقراری امنیت و ثبات منطقه‌ای ادامه می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/132687" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132686">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
نماینده ایران در سازمان ملل:
ایالات متحده بار دیگر با نقض آشکار منشور سازمان ملل متحد و تعهدات بین‌المللی خود، حملات نظامی گسترده‌ ای را علیه حاکمیت و تمامیت ارضی جمهوری اسلامی ایران آغاز کرده است
🔴
وی همچنین تأکید کرد این اقدامات، نقض صریح بند (4) ماده (2) منشور ملل متحد و همچنین نقض اساسی بند 1 تفاهمنامه اسلام‌ آباد محسوب میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/132686" target="_blank">📅 10:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132685">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
متکی نماینده مجلس در مصاحبه تلویزیونی: قطر ۴۰۰ میلیارد دلار به ایران بدهکار است، نه ۱۲ میلیارد دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/alonews/132685" target="_blank">📅 07:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132684">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ویدیویی از لحظه انفجار تو آق قلا استان گلستان :
✅
@AloNews</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/alonews/132684" target="_blank">📅 03:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132683">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad7681e28e.mp4?token=Ornv4yXG9hlLpsJfsDibllaPEWR09AGyLn3bDTvfp3zIQsXQWlPfbVIvOy-iEu5LI6KS3h0YqztApHCj4ILe3gImPJFolYEhvzEmSDvosm5DbOmPCUXEcbdSX-p3EZYrfzHgGIUSMegfYUQ1ddrnUzjK6rCZ84a0Xzb5-6e7OG6jnW6XUs7zKZT8OR-ZrMcX66D4oC_7cUBg5IYd53pmuVQaFOmSY7d5frm2Hk5rx8bVZJsW32axPsyQfkV9npCLRE6hd_lZfuP_idnvdk3P7L8r9i6lWX8IPEfkaIsi2fRCx6m-9WRlF_YVjiR-9JQ2xwK20UmnybcNLtr2E4WqyT26uoKzniXJwzuqH4OQRZ3vC-4Yopn2P-h8A5RxxXWO3tKG5nyjeZ-VgUtQijAd0cdHZjd77evShY8ppFcvijRb7pUrXqYlMkUtJadYKtFLMSqcmrVOs37NagQ2vlPAqF-hRFXvvN941an9C_nfwKKzDm-qgydugK8a0IGervVBTLBBwp62vpykUgKfNqRFhjHOmJqK7RrLlBYUF4BZPv83_BvPkxOqxycWKmUa8ne1MnWdLHh9AoVbDJNZPId7L9VwV2eE0n_jk9-9fxjFwheqy49EPrVvok695vi904e1CUUx2RaQL7ThcY4TDctPQ6ukjdanXXQ1b4FG77vjWrs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad7681e28e.mp4?token=Ornv4yXG9hlLpsJfsDibllaPEWR09AGyLn3bDTvfp3zIQsXQWlPfbVIvOy-iEu5LI6KS3h0YqztApHCj4ILe3gImPJFolYEhvzEmSDvosm5DbOmPCUXEcbdSX-p3EZYrfzHgGIUSMegfYUQ1ddrnUzjK6rCZ84a0Xzb5-6e7OG6jnW6XUs7zKZT8OR-ZrMcX66D4oC_7cUBg5IYd53pmuVQaFOmSY7d5frm2Hk5rx8bVZJsW32axPsyQfkV9npCLRE6hd_lZfuP_idnvdk3P7L8r9i6lWX8IPEfkaIsi2fRCx6m-9WRlF_YVjiR-9JQ2xwK20UmnybcNLtr2E4WqyT26uoKzniXJwzuqH4OQRZ3vC-4Yopn2P-h8A5RxxXWO3tKG5nyjeZ-VgUtQijAd0cdHZjd77evShY8ppFcvijRb7pUrXqYlMkUtJadYKtFLMSqcmrVOs37NagQ2vlPAqF-hRFXvvN941an9C_nfwKKzDm-qgydugK8a0IGervVBTLBBwp62vpykUgKfNqRFhjHOmJqK7RrLlBYUF4BZPv83_BvPkxOqxycWKmUa8ne1MnWdLHh9AoVbDJNZPId7L9VwV2eE0n_jk9-9fxjFwheqy49EPrVvok695vi904e1CUUx2RaQL7ThcY4TDctPQ6ukjdanXXQ1b4FG77vjWrs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از لحظه انفجار تو آق قلا استان گلستان :
✅
@AloNews</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/alonews/132683" target="_blank">📅 03:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132682">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e566e26eb7.mp4?token=OOj2RYiz2CJsrHTQLxq3Z8t6o8HCcG6QTH5H6d5Khu1bU_PS9MbufIZqYXIVEvbi18XPLWbStxInLaHAUVfz0SDKtQFYpUVGZWlgKFAQuAe7H3oTopsXnRSvKNuzrB8C91X0AUgxwOBHf0Dcn0tlJ-VH0ksk-oEJS_EksFtQucYhhUNyo-plB_gmQD8RlalY0NjRFVbvhVV1LjoTXG7lgMKd0Fd21Mg6V-QA9WVp41cGpeqodmLZD1C_ZKBH7k68QJWY2jh3hkURuqhYOQQNiw8seba4bt6rx3PV1OFk0o8YgsnF6JFbnxQoBUcmYOY0-w0RxyXnUZbSGP2HHk4cRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e566e26eb7.mp4?token=OOj2RYiz2CJsrHTQLxq3Z8t6o8HCcG6QTH5H6d5Khu1bU_PS9MbufIZqYXIVEvbi18XPLWbStxInLaHAUVfz0SDKtQFYpUVGZWlgKFAQuAe7H3oTopsXnRSvKNuzrB8C91X0AUgxwOBHf0Dcn0tlJ-VH0ksk-oEJS_EksFtQucYhhUNyo-plB_gmQD8RlalY0NjRFVbvhVV1LjoTXG7lgMKd0Fd21Mg6V-QA9WVp41cGpeqodmLZD1C_ZKBH7k68QJWY2jh3hkURuqhYOQQNiw8seba4bt6rx3PV1OFk0o8YgsnF6JFbnxQoBUcmYOY0-w0RxyXnUZbSGP2HHk4cRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی تکمیلی از هدف قرارگرفتن پل ریلی دگونچی آق‌قلا در استان گلستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/132682" target="_blank">📅 03:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132679">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CYspl_n1mrVapD5Pj2vBranvERQtDGdmqikFMsQ3kV8Wl1DnFyTdTNnWiBd97JPRnCfaQ-wkyYXcfd3yB48Jz5TcGLxRCkXNxd9iBLTopVZw5IA76wXbXHQoPd1B_07R3op9QDiTjh2OrzdkS1WjP-fntYz2a4k_iXWu_hyA9kdQpAnGZG3YXrAYyCQ10NaISy8RTZKnLA8RXz5nFvPWy295YSBSE1zM8Oht1YQY6HCWTNS78YQZqMLswapQ2mLWm_D2_igCYbvBRNDxnAL1Jr3C6oyIxH-Uds0lge_xVYK8Sw71rHIKv4rwCPoWpVxGXaKh_9_5uXA_lZfCuQiJMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gqco355GSgt-QRd-1oiKU4sIssROsNbQueQAc83QwwPsclQaHWhpok0jRcnKlY2AWnIb6mxIa4D6Kp06w38EOQ4S8sfbNlhPVp-d0_skcFecWlL9WuGSeEPcvRJECzyp9q82eXS4R2o19XSPszKXhDVXw7FsGr_01r_flqPF8cRX0KhEQ-ro85pSGuDW5IGGscN7KMW5BkRu8xcFV_PN6CTcL_DNyzbG2IWlHekZpJwI7F3hAdR0h992YEjP_-wrDmzXnOa9X5unvNdEx-TDLjYt-_dbCLZ4B16-PPK57o6-ytlIbHMKtTAb9TbHHkU4cTrUQQmS69-8ssD9VlRiTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDabFI-y46WA7tU3xB87T-A8XH2NMoZfFD1eISdYoWrIVuxrnaIrlwwjlK1yhFJ_zwR5rsBsiBOtXIDaN04knWvR0B9NH9YV6iIStwjuRoic8UIU0A8o70EUNIamw7IkYwdBAInraqF__8zPbUjcbFk92M4VZA6tJF6ptaYLV9zB80jFHzUKrwNapggAwyNdXFmYDresgsbTOqIsZ02UfpyTDMukpSm2SXF5lDdH63InSYQBEgzWNYPNtH5XhWOJvwVoorrMdkC4gyuD0Ccf7zYmU_zARTRnQElOv5YZjzQq4_mPaBdQ5LGUR04DioBK0WfRGKivkKHTk7gmp-P_1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نزدیک آق‌قلا در گلستان، پل راه آهن هدف قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/alonews/132679" target="_blank">📅 02:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132678">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ هم اکنون: ما همین چند لحظه پیش یک تماس دریافت کردیم و ایران به شدت در تلاش است تا یک توافق صلح با ما منعقد کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/alonews/132678" target="_blank">📅 02:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132677">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ هم اکنون:
ما همین چند لحظه پیش یک تماس دریافت کردیم و ایران به شدت در تلاش است تا یک توافق صلح با ما منعقد کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/alonews/132677" target="_blank">📅 02:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132675">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
گزارشات از انفجار در گرگان
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/alonews/132675" target="_blank">📅 02:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132674">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa2c9022a2.mp4?token=ra__9VQd0anV-G5AKegDkYHkF1uXvSSms2UD6ZDkQrID1tOETLgOS-QAu_arfXJS-gIVV3jnm9LYOSi1NshoATdVPXSc3ObqV7MxtIKprnhYfykH6ZWfp5MyaRqDnLvARDaPW3eCjQGOyG5p24C5ull7OexQ_RUxJ_mxE88xYBWEhN0Bv62bNqHucOZwLmzfZZLb6a2FcW5IxLsfDIJy7N_CkvnKymAk5EdUr4-smsZZrZ6mw6yfRx5Gxn23DYDmLp_aVUEnhNXW0KKWEMHEseSx9ziO29-wkuCrWucoNsjLKJXJLcGsa8KPz44TVL-tFmbknlivj6_5crgFXcRX_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa2c9022a2.mp4?token=ra__9VQd0anV-G5AKegDkYHkF1uXvSSms2UD6ZDkQrID1tOETLgOS-QAu_arfXJS-gIVV3jnm9LYOSi1NshoATdVPXSc3ObqV7MxtIKprnhYfykH6ZWfp5MyaRqDnLvARDaPW3eCjQGOyG5p24C5ull7OexQ_RUxJ_mxE88xYBWEhN0Bv62bNqHucOZwLmzfZZLb6a2FcW5IxLsfDIJy7N_CkvnKymAk5EdUr4-smsZZrZ6mw6yfRx5Gxn23DYDmLp_aVUEnhNXW0KKWEMHEseSx9ziO29-wkuCrWucoNsjLKJXJLcGsa8KPz44TVL-tFmbknlivj6_5crgFXcRX_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار:
اگر ایران خواهان یک توافق است، به نظر شما چرا به کشتی‌های تجاری حمله کردند؟
🔴
ترامپ:
چون... راستش را بخواهید، آن‌ها کمی دیوانه هستند. آن‌ها کمی از کنترل خارج شده‌اند.
اما آن‌ها واقعاً خواهان رسیدن به یک توافق هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/132674" target="_blank">📅 02:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132673">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e0b078ec.mp4?token=bYcHmTZ7lxn7Yd8Jnd22b_8ZhpctBUzFLDvgoCOxL9hrJPbGWanZFqRWSVsuoGhuYDcY92dH7cIpY_u_5O_YXxU4bwI1f8PBtmqtfJO00exje6zXMDEPJYChsa-AIdPJ9kNlYwvLFvJbKMrnGqEteFBiR9ZU-1QRWRnL7g5CF3npPsiVkJ7lM036X2InuMBArmLmzN2Rrtg-kOVx6_ytVy9lOMBtf9-SurlSmbYkW27NPOp25dYODp1VGi3xHHlE8L0sa8iIuK46mh01iooMUZpARSEGcgPac7B-YaQBcFGkKvFm9REcqWrisRabJ6nTMQxz1PmLcQV9zPZVb1MJ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e0b078ec.mp4?token=bYcHmTZ7lxn7Yd8Jnd22b_8ZhpctBUzFLDvgoCOxL9hrJPbGWanZFqRWSVsuoGhuYDcY92dH7cIpY_u_5O_YXxU4bwI1f8PBtmqtfJO00exje6zXMDEPJYChsa-AIdPJ9kNlYwvLFvJbKMrnGqEteFBiR9ZU-1QRWRnL7g5CF3npPsiVkJ7lM036X2InuMBArmLmzN2Rrtg-kOVx6_ytVy9lOMBtf9-SurlSmbYkW27NPOp25dYODp1VGi3xHHlE8L0sa8iIuK46mh01iooMUZpARSEGcgPac7B-YaQBcFGkKvFm9REcqWrisRabJ6nTMQxz1PmLcQV9zPZVb1MJ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات ترامپ، رئیس‌جمهور آمریکا، درباره ایران:
ما از نظر نظامی، پیروز شده‌ایم.
چند وقت پیش با ما تماس گرفتند. آن‌ها چقدر مشتاق به امضای یک توافق هستند. اما من نمی‌دانم که آیا آن‌ها شایسته امضای توافق هستند یا خیر.
من مطمئن نیستم که آن‌ها به توافق عمل خواهند کرد. این مشکل اصلی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/132673" target="_blank">📅 02:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132672">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/271b9663ee.mp4?token=tFmm14aINfcoeTXh3bsYSd6Nms8ncH12QeUl7gvXOyM8C2hCqER7qfwIr8PBP435F_VtIela_jqCYrNUrZZfy-Y4B3INtLAM7fO1eciSObDr5kQBZ3J2wBXnYlhCJC3HBaOO89myA0C0bs5BJxepZ4CMV_z6RC9D3bTz4WGVlk1yk5NWzzlVZpdiyHhwZiYPXyFIHW6jgrwoJ2fv3l3CNGvSgizqnPqPgabWzXBJpz3vAEqORw1M5PoDqgLv499GquTRXp4C00X9Jfd515e8j7t2zE12p6wLOzIlh8Tn5aXAYl7-i86uNGhBXUIj0RH7r_d7W5Einc-FwOUQOE0RbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/271b9663ee.mp4?token=tFmm14aINfcoeTXh3bsYSd6Nms8ncH12QeUl7gvXOyM8C2hCqER7qfwIr8PBP435F_VtIela_jqCYrNUrZZfy-Y4B3INtLAM7fO1eciSObDr5kQBZ3J2wBXnYlhCJC3HBaOO89myA0C0bs5BJxepZ4CMV_z6RC9D3bTz4WGVlk1yk5NWzzlVZpdiyHhwZiYPXyFIHW6jgrwoJ2fv3l3CNGvSgizqnPqPgabWzXBJpz3vAEqORw1M5PoDqgLv499GquTRXp4C00X9Jfd515e8j7t2zE12p6wLOzIlh8Tn5aXAYl7-i86uNGhBXUIj0RH7r_d7W5Einc-FwOUQOE0RbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات ترامپ، رئیس‌جمهور آمریکا، درباره ایران:
ما به آن‌ها ضربه بسیار سنگینی وارد کردیم و من می‌گویم که ما به نسبت ۲۰ به ۱ به آن‌ها ضربه زدیم.
هر بار که آن‌ها به ما ضربه می‌زنند، ما ۲۰ برابر آن‌ها ضربه خواهیم زد.
وقتی آن‌ها حمله می‌کنند، ما با قدرت بسیار بیشتری پاسخ خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/132672" target="_blank">📅 02:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132671">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
یک منبع امنیتی آگاه ایرانی به المیادین: ما هشدار دادیم که هرگونه حمله با واکنش فوری و گسترده‌تر مواجه خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/132671" target="_blank">📅 01:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132670">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/132670" target="_blank">📅 01:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132669">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WozwwKwJ1pJaUt-etLjV28l3OI0a0mChgbgt6EcHeP_eaMu1ee7z8JAVvXb27uyS3sZMqSQizHa-FQM0LZylmtzcWedY44b_Rj_gWqckx0b2NSc_xtJftPtMSofBvCsJRPW8Ap70RPKb_PAO9Xv1L1z82ZkaKU5mZNW2gSvht9gIDi-GQyX1kzl30xkT_ViX2v5vTOSyV-OjH-nGfiCcjAWq7FQt7a1EEpXVYMOuApy2s_GTP0YVLoZZ4DNinfIzMUDwf6IGhW5kVCaOMEr0yFkQ9Pe60DyYWVdiBMHH8KjGaqz38AZA73grkqQd970aAc7gSt3K3vNzxvs0gmYQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا امشب تمام نوار ساحلی رو زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/alonews/132669" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132668">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری/ سی‌ان‌ان:
آتش‌بس موقت با ایران متوقف شده است و وضعیت همچنان بسیار متغیر است. احتمال انجام حملات بیشتر نیز منتفی نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/alonews/132668" target="_blank">📅 01:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132665">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UmxBM0U7YDYiYR7ipoclrEvk9uzBiYDPVmirL2gBkTBgSphKkjW0eM65N0S9b5ezj-0DnBRcuFygZiaWXaFTqU0VhQjYNcdYOjzQZW-YBjhj9ZMocNT-lU3UpGJ3CWcvF3L4Wb5HAFpWeJbX0p0F5WxWKGUEEhN9bv9WroDMnldsHcUlVPfCRiYf9gb6Qx1NPzjM6C-8u_EohTBfuX49QF88ufkSjmmdRFND5NNA8d9B-9JZYYP6dmc1_gagggL6vCD37L5RbrrgvdsAyYz6dokgbF0SSyrmwjHW-buyPvHFwEGO8rMSBprO_BQ71zbdVDLZhOIjeuI87hzXQGjvpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lauptj0v3-vzieKhqgyy2yPr_n9VWEqpToMRffQXFoChjLB48wDavoVvWIPPOql3YLeCCKj87sET20ZL4SSypTZmXPFe_G6ZCi64Lec-fwFaaLnRNZEjM6O5imkh_BLSIMejb2Rumx4vCowzxe07eNF5dSoqdDoJyNwA2CrFkbDc5vEh_sZ3arm9c5aSrkYss1jaGMFrSXVUKCnAH1W6FDyQsRtI1-_d2n5P8d2NkukteRx_oYeIXXRkfbx_jNMbekRb3bmOoXyqBwdXhBnPNQf6-mwQ6b5UwoSlbbh4ezEMT5wZr0SMCoqg9ECngrUjK1Q38W5kdMZ3KnyKeA7cJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vy2lERbgLmhr6yLvnIQNZCAQWv8aogKNrlRdeNfmcnpzB2qfKA83dNkWKRY_FEc6xylHT8FMPZEpklmxMWKwXwiNo1NTejfKqDORrJ4QZaPy-O9Fhixp_BDuYgiPYxaGjFcr1BslE3OyEm9mjdWf0QCxpKN5dZkGFdNAOlE8TLFS0_VAR6jleCJ_VOZPIfUOK3kl-BPvmj-6Cp9SqcTW7n-SuqO_C90ylQMpMaKdp74AMt1En6QboEuhvJ3vIGPlUPubaO7wKZaySIlIvOHZ8-7QTYRNigD7Xxdtjnkca5Bwyol9qW9q57Z5-975TdFaCV7SszlQeq0We46BHpnLow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ، تصاویر مربوط به حملات در ایران را منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/132665" target="_blank">📅 01:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132664">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوری/العربیه: بحرین در حملات امشب به ایران مشارکت داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/132664" target="_blank">📅 01:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132663">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jhqek97O4Llq0u9molfQaOMPkjZfww51Y7PSwe0-fov5ia4yTtxyATzwcGF7FLkOnxM7_uFzsBNrwvipUVj4hGMlZPV4ttJoUFcLSYd__KJDQqVf5hXulcSMorKe0oaFylKq8b2KeYtfxZh0yi2FxmHn99J7TY_MidY0aQIHkMlZMXmBViMkW8DG-c06kOs6tzcYNKvCDXvtaOK2h8Ahok3o_Ou0VRllxwQnBQOdwMcv5tcTMaBp-fdcEGxUG51lBYm6Y6H_K7BeiWr1VH0a0IALTZLQJ2nvgSPFtiLHgGdePvkd2dYcAw54pU0-GKtEAH0wS3gszHCt9uROks7nGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ ترامپ: «این اقدام، تلافی بمباران کشتی‌ها توسط ایران در دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار وخیم‌تر خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/alonews/132663" target="_blank">📅 01:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132662">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5jgvFjA3U6J1kP0vthL7cJYzPpYuD0LIvvMyUG9bGy03CB6frNcQ_-nO2p2FFCjigKKp8TwoW8G5g1TWQSN_pCswCIFm0qB3-bj1dmRVa76C01K8JyCz_wBsHCQk29MSQVVvEYeTc7tWPl-dVvPXPLGAqlhNYyNMCZ0bAsZuDYMbcr9kXljIFpR0lNt5jEttyd9vVxnnSp3BW0-sA5CFp6j_nidps_m4yTQRA1z4PpRHpuDrcq_MF20sL2N8bFGGgfTsgtehGqMYbOHfFguSZap_nmKaiUbrITKHSOi_kR-3csmh8aKU8GBBArSmUKh8ShJaqKH2hwIFcWCb_qrNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ ترامپ:
«این اقدام، تلافی بمباران کشتی‌ها توسط ایران در دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار وخیم‌تر خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/132662" target="_blank">📅 01:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132661">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سایت پدافندی نیروگاه هسته ای بوشهر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/132661" target="_blank">📅 01:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132660">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ue3j6ml47At1BGPeEp59Okx1rT1SaAVlKF28K_XycoZ_uBasyk8BoOO38z7CB7Ovosz593mugXfujNOTC358qGxQ7ykxTJzkkCpNCdiPwdnYUSB344cgVGNvQyDu7WYtgGfvGOcK5IoYOdwL_9Zw5YgSJkp42yvc55K8ZoYH_EFJPpWL45p3npe_1iOiCnRB0RkhcM8gIMcn13GotWxHS925E0X_mIlP4BYnG-saYzu2O4I5CYO-npL9r7GP9UV8jVCO_NfQekm-z7oIS2r152fx3b5kpofOKYAIc_UdzMiKUs7iDDfn6TLyvVOSBnV3IY2pGcKV86NIBXnCDdbItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
11 سوخترسان درحال رساندن سوخت به جنگنده های ارتش ایالات متحده
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/132660" target="_blank">📅 01:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132659">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc262f35c.mp4?token=Faryblbe7zvp373rozOJqynXo0km3-uLoqbypuQ88GtOGLRMigPsQ6hJ0mKcEGWzlTCno6fYkoY8MsSNmp-yCOkqDARRSMlqn3UDX0_evWeXxjfh_EA0HZ3q-J7c2fKZoBHJ0JF4eftF-DkoCaPzB7-4Hp4JIYebiF8n5Qhw-2cWtF45AihW3bIpL2HA7h6_DUIJjrjUY78PtRCcyfbsPdy3jJlTdkVTF7nLzCWSI8V_CTMAF5ulveaSOIL-clJm4tSzpe-PqCQoL55bpLV4FOsjpAPBWy9caHXKGcWT01k7CnPT41fVLlS_WHc6ss2oLpRRQdi3X9YqcSwAsmrrcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc262f35c.mp4?token=Faryblbe7zvp373rozOJqynXo0km3-uLoqbypuQ88GtOGLRMigPsQ6hJ0mKcEGWzlTCno6fYkoY8MsSNmp-yCOkqDARRSMlqn3UDX0_evWeXxjfh_EA0HZ3q-J7c2fKZoBHJ0JF4eftF-DkoCaPzB7-4Hp4JIYebiF8n5Qhw-2cWtF45AihW3bIpL2HA7h6_DUIJjrjUY78PtRCcyfbsPdy3jJlTdkVTF7nLzCWSI8V_CTMAF5ulveaSOIL-clJm4tSzpe-PqCQoL55bpLV4FOsjpAPBWy9caHXKGcWT01k7CnPT41fVLlS_WHc6ss2oLpRRQdi3X9YqcSwAsmrrcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش سپاه به حملات اخیر
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/132659" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132658">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlGD3W4-N9gW3w2RM632qEHsG4PRJNEPMT-q8ksnz6fN4pY1Md3Uyr4_aCoc4HvijvmlINKZljqvH6ub1ytJrEJqFpQ_6t1anF36LeTCEjkS5ky-Q1rvRxNPihcPpPhDaUCJR_UHoy5a8X4m5xuzCAjP9PQ2kodcyntX0Kn_GQgh7eNif4BUQoMjkAD07O7v5JckCkfnKChZ0AuWlYxHnk3kP6KJkY7uLTdD5jyrkYjoRax77GNqb0dFihOb91JN08gb2At8yzkXw_BrPkIx_xufAynByxaraqKD5id37Xps-Y326EjIRME7GppibJ2T-vy5siZsIV4zou6Pm2lLKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال
محسن رضایی:
دشمن به شدت تنبیه خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/132658" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132656">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پشمام
😐
بعد از برد دراماتیک آرژانتین گروهی از طرفداران زن این تیم در استادیوم لخت شدن
😐
⚠️
⚠️
مشاهده بدون سانسور فیلم</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/132656" target="_blank">📅 00:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132655">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
گویا مقر تیپ 110 سلمان فارسی نیروی زمینی سپاه در زاهدان بمباران شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/132655" target="_blank">📅 00:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132654">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
140 جنگنده تا الان وارد حریم هوایی ایران شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/alonews/132654" target="_blank">📅 00:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132653">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zs-H5ZU7Lc7q1e_d5EdAVyXTQdv7VCwflEvzFyf7pGjwA73SLn9-UNnCTZjpVpeTEwCu--7wBFTTau6prBegDJUhe_CHMiQsCIIiJ7n_IDvN7yhLyAG42-M_ja21i-u8rv-9NNDk4x18RY6sP-FO8zOMP8DR9_QAugHBFgLyBYM0lt2uxdyKiXCwxT4r1Syb1shdF-eWkkCOwnHll5mPr0YKWJg0gk6kobDxdSrIkOFD9ICGx3H0z59y36v0KD1NEVrVC2mPy8FgaI7VNh5a7ZknqwJezxqtUYeOXGuk74o3E0i97EhRrRzYvw0Il-Y4InzchApYYsqJzL4-XFHvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رائفی پور: باید واشنگتن رو با موشک بزنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/alonews/132653" target="_blank">📅 00:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132652">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNUFBiubXWPFh3JQ7gdWvr0r0DQ5B37O37DiYbiLnjPJRouFax7goJnGEi23yJvFZb9Yigs_RQJLeDLqM3yt3wWykbMgENYnAkJ2Dx49JOsGA8V0RnWpAU5f28zw1bWi950-O2F6NkQ0tb9tBrC8r0-5gvasdlYXrXWN4IMheaC4JxyAntdH-QbXDGrdHc4Vb5lLEhMfPE5eeRHF7BC7_wDXcF7Q3IXBGhPfTP9VkqLVT5WcCTDwTu0_DBNV4aPnSKXDfSVaR56JNZ5WqGzdWg-e0uDropAyyEfezMyjy-GaMFH1dmp2huo43U63XG4niznVwfz4WKVsjGIyL5LJ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ارسالی کاربران الونیوز از هدف قرار داده شدن برج دیده بانی چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/alonews/132652" target="_blank">📅 00:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132651">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=Iupk9o17mysQNNZgHMGq2RYhf-r7GlAC8sIlV1qpFrBXSalRdRx19szYL3Y4TKnaibeGkGvg_Yfi8DQCdvWZVkUi4uuCN1EFW6-LiPvpeoN2CrSplmObHX3-uCX23MJfF7ImoI6dP9sujvOVBPpd8BGgHxW4CgSCKyOgsPyYjSafGeleJLPGg_uOpjllWvpE_bf8EUun2tuFBmqqlSHPlQ-3QhhPicCiisME3TXcwSPdVyF-BjON9wEZvhSMpAdnNimac4dGfmegUy_mrBCsM_7n8x_FUoaX2e1S_nEPGJUo6ovzjRopmyF7hLJd9tbOCF-y7fD_qMzlpyPFObSUSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=Iupk9o17mysQNNZgHMGq2RYhf-r7GlAC8sIlV1qpFrBXSalRdRx19szYL3Y4TKnaibeGkGvg_Yfi8DQCdvWZVkUi4uuCN1EFW6-LiPvpeoN2CrSplmObHX3-uCX23MJfF7ImoI6dP9sujvOVBPpd8BGgHxW4CgSCKyOgsPyYjSafGeleJLPGg_uOpjllWvpE_bf8EUun2tuFBmqqlSHPlQ-3QhhPicCiisME3TXcwSPdVyF-BjON9wEZvhSMpAdnNimac4dGfmegUy_mrBCsM_7n8x_FUoaX2e1S_nEPGJUo6ovzjRopmyF7hLJd9tbOCF-y7fD_qMzlpyPFObSUSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس:
🔴
ما به آمریکایی‌ها پاسخی کوبنده خواهیم داد و امنیت رو از آن‌ها در هر کجا که باشن، سلب خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/132651" target="_blank">📅 00:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132650">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
انفجار در جاسک
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/132650" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132649">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">💢
فووووووووری/جنگنده در آسمان تهران  احتمالا جنگنده خودی است
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/132649" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132648">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری/پایگاه امام علی نیروی دریایی سپاه مورد حمله قرار گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/132648" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132647">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88d7ae0b90.mp4?token=tJwVqtMZrsBYhOsfEG2ov7DnR7Jwy1YjKDhgH9-UDE0Op-i9I7YvcXP8TmeivIYqdpE43AHdy3xczmZmrOhoy8TWvbH0ziY3t9aujIRuK_YGyr2kXv21I3LufA_VhN7D8JbmucchCupAqF_LdRZbSHXFLPGzOvte9jy84C6ZYbiQLjRTysnx8xDUbZwwdLJKuTg6xaqdSztujdILoD-tMvvypEu0KNnsUclKYczhSoktcLFE5X-zNycASLbp5E4Vo2Aj4Du1nOfvtmvLReUDI2CxsaKo6D9X-29aVrNd-eHtoqcTKUpKw16Noymyfos95xM5n-oy2WcXGlnrclmgmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88d7ae0b90.mp4?token=tJwVqtMZrsBYhOsfEG2ov7DnR7Jwy1YjKDhgH9-UDE0Op-i9I7YvcXP8TmeivIYqdpE43AHdy3xczmZmrOhoy8TWvbH0ziY3t9aujIRuK_YGyr2kXv21I3LufA_VhN7D8JbmucchCupAqF_LdRZbSHXFLPGzOvte9jy84C6ZYbiQLjRTysnx8xDUbZwwdLJKuTg6xaqdSztujdILoD-tMvvypEu0KNnsUclKYczhSoktcLFE5X-zNycASLbp5E4Vo2Aj4Du1nOfvtmvLReUDI2CxsaKo6D9X-29aVrNd-eHtoqcTKUpKw16Noymyfos95xM5n-oy2WcXGlnrclmgmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه حمله به اسکله شهید کلانتری چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/alonews/132647" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132646">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b53c23c50c.mp4?token=NuXW1uyK5yeEh4riXMNkfKY8W-UxXBtEPb1xDjJatPVVr76kzBincME_yLRBEYwcbTsqsXmDwWBrvtHrFVLUlQDBVsZdffqZPwhOp_OzB_E3GYauuMEdoXX_pbfcdOJDOD_-ZPnXuCdBQNd1jVmt81mLPjXMqwgpGWkV7s_kfBXaIQQCAbsNHCGIwlTlcuGg5L-n-U_5a5pdK4HMWJM1eWtUnPOJgCJNKzIS3fTX8sYN-RcAaoNG61h8yvH-wSHuYR5Nk_YVm3rkfJ0ZYhHVMTOF-pistvkCj0ZvZgIQHtG8OqoCTiz-1rknVZI-l0tMa2Dls-uttzYCY9zEpsOM1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b53c23c50c.mp4?token=NuXW1uyK5yeEh4riXMNkfKY8W-UxXBtEPb1xDjJatPVVr76kzBincME_yLRBEYwcbTsqsXmDwWBrvtHrFVLUlQDBVsZdffqZPwhOp_OzB_E3GYauuMEdoXX_pbfcdOJDOD_-ZPnXuCdBQNd1jVmt81mLPjXMqwgpGWkV7s_kfBXaIQQCAbsNHCGIwlTlcuGg5L-n-U_5a5pdK4HMWJM1eWtUnPOJgCJNKzIS3fTX8sYN-RcAaoNG61h8yvH-wSHuYR5Nk_YVm3rkfJ0ZYhHVMTOF-pistvkCj0ZvZgIQHtG8OqoCTiz-1rknVZI-l0tMa2Dls-uttzYCY9zEpsOM1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/وضعیت چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/132646" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132645">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری/بزودی حملات ایران شروع میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/132645" target="_blank">📅 00:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132644">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
جنوب کشور داره بمبارون میشه، شبکه خبر هم روضه پخش میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/alonews/132644" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132643">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
گویا برق بخشی از چابهار بر اثر بمباران‌ها قطع شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/132643" target="_blank">📅 00:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132642">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری/گزارشات تایید نشده از بمباران نیروگاه برق بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/alonews/132642" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132641">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XMTIcVM_lObqwBkt7XswhJdIds2ltFkUvQQG_frnK0lskMw-egb73tAcNEfXcrTCgVFvJ9KjwGloCC0rHpyAbgVGsTsQ5k74c8kPIkfHLc03unbWMK5UYz7a-SHBUstXdIr6fU6K_yxaTWypgxpg2HaNROPYTY_tq5W88q-PdREpm1x8xyGti6-ZLUku3C0Q97Pj_EGXLR0I8ekGaDr-DkDcWCS147dkQskDXkn9SWPE6wBs6kBrUjqIsAW4oJwQ0bZbkhatyus6UKuc9_qmAC8eRWbNtorbrQ0H0widJpjVXDqGrYLhlDYQ6OCNyjLB3CWi5QrGQFScg1DI6c2SIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/بر اثر انفجار، آسمان بوشهر روشن شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/alonews/132641" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132639">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری/بیش از ۲۰۰نقطه تا الان بمباران شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/alonews/132639" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132638">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
قضیه شده این: شعار بده، بمب بگیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/alonews/132638" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132637">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوووری/ایالات متحده تمام نوار ساحلی جنوب کشور را بمباران کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/alonews/132637" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132636">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGPVglXiuBbkSnA3h_-Hv08GI28EcrmM8sLdVLHaGkBAuRrFsSUSTWG9YaLr3Y6Gl_yaIhq5A_jzpcjk55bx4CR0lcbm1KHpPTbh9GysVCoIuGh8SgYcU7r2vMIDUgZrs9QSLWZzfJOMgWkHhJ_0GOkv4r0qcTFaGTqjouWmCMaBY5PFKRYZfa3wG_SpedInjeddxiqeWWzuWDBJcfNkorXYyaSfreTEGxxLLEpPLMbHNF6x0HuRCNR6hATdgPa8DrLZwDad8CwTPfFKnVhhDHgGYl0fBP14tsE43ZVa485jp3cWUujYiCQVqyF2sZNwo-6u9JTJNxLhNDmG8UtRDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ارسالی کاربران الونیوز از بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/132636" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132635">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری/انفجار در جزیره خارگ
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/alonews/132635" target="_blank">📅 23:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132634">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فوری/گزارش انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/alonews/132634" target="_blank">📅 23:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132632">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوری/انفجار مجدد در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/alonews/132632" target="_blank">📅 23:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132631">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8-DSrhlz9zwsQ0khGd-Y9Na9uAcYvS9VS4z_UQJy2XsdH98p0pPRaiyYfdSagJDNX4wDFQdbQWFoitrV6CC48LzE-c3wuIHAoqfCZqk1eZtrZJUz5zF_mFhdFmkv3mpRTMcTUTU5LI9L4fLxm720Msj_ekxHfsbYCF7_gMr3_iJ6u1NEVcRzrAs6zoxJm6LpSoVhaKQ6zgOKzmyzDar_x685lwjzcKu_aJw2eStCJZWlHDbiAGDHYZDIS_XGjqMXh5lcjWli4zqzRUd9pY4X4x6DxDhzjWHbjIlxIsSBzLDihysHsE_6I9Ox3obTJS_jDw42zW1pSPXDXp8l_G4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام
:
به دستور فرمانده کل نیروهای مسلح، نیروهای فرماندهی مرکزی ایالات متحده، حملات بیشتری را علیه ایران آغاز کرده‌اند تا توانایی این کشور در تهدید آزادی کشتیرانی در تنگه هرمز را بیشتر تضعیف کنند.
ایالات متحده، ایران را مسئول اقدامات تجاوزکارانه اخیر و غیرموجه علیه کشتی‌های تجاری و خدمه غیرنظامی که به صورت آزادانه در یک آبراه بین‌المللی حیاتی تردد می‌کنند، می‌داند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/alonews/132631" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132630">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=YBH3m0TTCP2CIgX0a7-RX0SEiaYqIg_wjKmGDvsnJXentEwM3e6-wAUDltYWuWWR3BgFJwf4abajfGG1p1JvbP3iDRDf6VLikLPukUw8-63tnbR73VSxojaF_4oefHkDjaBsKMG47Pq4zHNsRY_vyV_zdNamnm5-ZvdsCEfy1DgQETrXRbJtFBQEw_RXSo_9MTJTaJT2hOSTT8eadO5ZrP5tgC4xHl7zPrRwDWsuLhNBWlLEjWQrQLGha7lWodbVsZ1TKEdbJPDS3zbCNcxos2--t-VSyRzV36MpBOdpWhI-hc4qZ6fpuS_M2au_5I-7LoaaBJpwQ7Vfqp2R5sPgaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=YBH3m0TTCP2CIgX0a7-RX0SEiaYqIg_wjKmGDvsnJXentEwM3e6-wAUDltYWuWWR3BgFJwf4abajfGG1p1JvbP3iDRDf6VLikLPukUw8-63tnbR73VSxojaF_4oefHkDjaBsKMG47Pq4zHNsRY_vyV_zdNamnm5-ZvdsCEfy1DgQETrXRbJtFBQEw_RXSo_9MTJTaJT2hOSTT8eadO5ZrP5tgC4xHl7zPrRwDWsuLhNBWlLEjWQrQLGha7lWodbVsZ1TKEdbJPDS3zbCNcxos2--t-VSyRzV36MpBOdpWhI-hc4qZ6fpuS_M2au_5I-7LoaaBJpwQ7Vfqp2R5sPgaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/ارسالی کاربران الونیوز از انفجار در ۰ابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/alonews/132630" target="_blank">📅 23:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132629">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری/پالایشگاه لاوان مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/alonews/132629" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132628">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری/انفجارهای متعدد در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/alonews/132628" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132627">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27659d902.mp4?token=PcOobzIBhCL_iHWW_eI-EF02NNw-_CAkNsp_Dg4ySMPfepWUSoCb6TmY5jE9pIau7ckw1V070viubxSbvzZSjaP7Jn8ZXY9fieQflxIJYV2ALUp0BhUKPBdoMR8v823IpkY4qJFKBlaXjPL9uPkSJCx1PB5TZF2vZSIGvylOsXg3gROSjw771DE9qX7Dq40rviZJ7mimBvld5qWUxPtvVhC3JVt-it-HEm904PY0jrQ2_xu8DaxFd6z_SqZyi9NtT1mvg-rWcizDNmgLbA7ySNvU_scoJtqbWUNP7-8IJARQjCTM5jjTlPFSm89vZzCjqxCbUohHKVOziFylk-PxRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27659d902.mp4?token=PcOobzIBhCL_iHWW_eI-EF02NNw-_CAkNsp_Dg4ySMPfepWUSoCb6TmY5jE9pIau7ckw1V070viubxSbvzZSjaP7Jn8ZXY9fieQflxIJYV2ALUp0BhUKPBdoMR8v823IpkY4qJFKBlaXjPL9uPkSJCx1PB5TZF2vZSIGvylOsXg3gROSjw771DE9qX7Dq40rviZJ7mimBvld5qWUxPtvVhC3JVt-it-HEm904PY0jrQ2_xu8DaxFd6z_SqZyi9NtT1mvg-rWcizDNmgLbA7ySNvU_scoJtqbWUNP7-8IJARQjCTM5jjTlPFSm89vZzCjqxCbUohHKVOziFylk-PxRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این وسط
،
دلتنگی و گریه هادی چوپان برای علی خامنه‌ای
🔴
زیارتت قبول آ سید/ برگرد دلمون تنگه برات
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/alonews/132627" target="_blank">📅 23:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132626">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/alonews/132626" target="_blank">📅 23:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132625">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/alonews/132625" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132623">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فوری / حملات آمریکا به بندر کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/alonews/132623" target="_blank">📅 23:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132622">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/alonews/132622" target="_blank">📅 23:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132621">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری/پایگاه دریایی سپاه بمباران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/132621" target="_blank">📅 23:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132619">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
پدافند بندر عباس فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/alonews/132619" target="_blank">📅 23:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132617">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فوری / صدای برخی انفجارها از سمت دریا در محدوده ساحل غربی سیریک به گوش رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/alonews/132617" target="_blank">📅 23:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132616">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری/حملات آمریکا شروع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/132616" target="_blank">📅 23:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132615">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فوری/انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/alonews/132615" target="_blank">📅 23:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132614">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سفیر چین در ایران: پکن اصرار دارد که در مناقشه‌های ژئوپولیتیک دخالتی نکند
🔴
ما همواره از کشورهای منطقه حمایت کرده‌ایم که سرنوشت خود را در دست بگیرند و از طریق دیپلماسی مسائل خود را حل و فصل کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/alonews/132614" target="_blank">📅 23:18 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
