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
<img src="https://cdn4.telesco.pe/file/Yu8IiDtjtDBz6CJlqh-OZ8aUXrfjmQRoYRmSET3mXIxa2rCI167tw8Ef6aQF4UmU1-Bousy9mx0ZU1-PrzuNJAkTzUq-A9CajtVP_Mq-QOonHJ01_YfljT34rOWNUZ_KyNx3kUnx4jM6l3RpOcN48FkdxArvsoK-ipeebp6-Y5UI5DG4AFLVXX5d3f3yuRJSHQcedTjRGhOJa9VzW7NpFIt-ojkG2SKbcfNqfGfvGZcXcfuCysB-vEOdO-xe63Lr5-OBv_bSMfJW6ezwmxsB9c8om4gHeOqGMyfJOljS72rjNtlnN72TaCOKN9rlViywMmaaRIF0SNSV_OTREiDXTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 606K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 19:04:48</div>
<hr>

<div class="tg-post" id="msg-26889">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5bZUij1esGCDgbfEaPt-S5rSyC9T_ZklJxkrcI3BmA6LAjouWUXNQluIga8j28ik83BGj3ro1PdP91-PXb7g_kTSS4r9QuI5q-qmxvPdnU6Nk7X6b9dsqlMXP0qMfOOJwWX5jCWaxEUToHHJsrQEyGcbssPfgIThCRVuFJUHYaVdnwqxH7XmrAq2fhcMljFq1NbJlm5qMWykeK2o1Cxd2WtW_T_flqYGUFPZRUSgwHbHrJJs-CXqAjjizXI_owMs7dVgg3rGvcxaSUV2c9n6heihK5lLBGnaUoECUNmzaxcBYpRmY36438WYMCobQsIW9_GqbjuF3jQWcXjUuYMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
همسرایرانی‌خوزه"ممد"مورایس هستند سرمربی پرتغالی سابق باشگاه سپاهان اصفهان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/persiana_Soccer/26889" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26888">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obkhzRifX4xqtgXeZKoZjgSyiNkgm3QETFg6MYELNmdS9VaCpwnxtbCR68hzmE8HnCMjBv-juozO4hsSHPn7hS1ZK0d8NY1TGFFZ5upsW5ZgvdBY-rT5RmRzya1CT9CxKqn02QwnQpJjY1HNkhbh1Qh2m-ymTidsmsdtDLCLhlY3KtWSeFi5qw-AosgTQ4ALlR07swRB_jkp_E1FNhGwda-7b_w23yFJJl4h5gL27d0gTGk5YqSAJQgFMDRDi6k3QHPQtvePHEl8TbisGfCh4YlH4fNzabg_egqjtrDunFOhbbi5xva5AunXRks197dAXzhj5QAlJqYnMqeSX_tSWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇺🇦
مارکا: میخائیلو مودریک‌ ستاره‌ محروم‌ چلسی تصمیم گرفته که در رشته دو میدانی فعالیت کنه و هدف او نمایندگی اوکراین در بازی‌های‌ المپیک ۲۰۲۸ لس‌آنجلس است. او تصمیم‌ گرفته‌ که کفش‌ های فوتبال خود را با کفش‌های دو و میدانی عوض کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/26888" target="_blank">📅 18:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26887">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی از مراسم عروسی کریس رونالدو و جورجینا  که‌توسط AI ساخته شده؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/26887" target="_blank">📅 18:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26886">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRsXn0Thoirc1qME_j6azLanNC3JJIgOm53NF4e3g6H2seKZ8jzlZ68HPznQZxVHB_fvGMgVwPl_D8COugNNaltqeYvS-FE_J8J13BqcX1dDzKrkfuzcSHiW6W3lsrzw0l8R-QaSj99gmPoUguRKxf6dDLykiWuqbbb7PvLnBPgL-DPz6r8UkROFJIH0OfqysMFfHjaEu1-waRo6fswNqbulGpMi9Lu7e1WU309l80p2-PS_1xjcJqo2J0JO80wAZBdNG6wWXHeTCVPlFdDJhcjCKR-TRZ8oMMQOlNQQx-hyWBYGYRMs_ZJXEKsEB4wrFR4mD9pc_6x54j4rWzTpFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ESPN: رودری به سران من سیتی اعلام کرده که به‌هیچ‌عنوان دیگر علاقه‌ای به ماندن در این تیم ندارد و قصدداره‌راهی رئال مادرید شود. شماره رودری بعد از عقد قرارداد به رئال 18 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/26886" target="_blank">📅 18:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26885">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Se4weCwH7EoFuSTiz3q5Efmj4M5rc8_lLQ8grjdE0zee1hats2QzAlxjs_tlTJZMdBN0myItlDXVwDPfInwDI76fS-A_Aw2leBIwYrY5TDrGKOyCRFQBpNWM9hnO5mGY2Y9UIKflwxmj5H2wzyc0uUNZ6XEJhiXhVeoHr0mWrGqNoBefSbr0dyktBJCnI6pKw4ukyyQeTRJD3kfXHHmnCfqOTMMha8fM2UnEqBwxyxa24BGPJLkgse1bS4KS9-cyCPzqAQ4X3uBHsrabdNjW9pW5KApOE9DgVA0aUeeUuLxn5NMmYyPv1vp0P2y4UCBP1hJuNB_Frc6vmkOoSRwosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمارمعکوس تاشروع‌رقابت‌های داغ فوتبال اروپا؛ تنها 27 روز تاشروع‌جذاب‌ترین‌لیگ‌دنیا "لیگ‌جزیره"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/26885" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26884">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHVJExY66ALXLUAP_OjvS6dMXfygEe_CVOLw4O4nNFeXawMrqUAXR1S4X59rmKQ56v7g9Jo_Bgc1YP-eDsIlxjcr600VlHya3Grp0iGyBgGX9EvokOAkDnJsoGOJpiKMgayCNza8QWUgLrumCLVgbcAwJsR-mYm4L_eej3F6WxX3iEWGu_mUCBpS8hDK7dsLNmHonzbXVndHkxXWizUIZDufJHDxvnNHQIc7o5bHUBLzxF3oQztT8mg7MRys2u9OZIgA_6dqpoEubay3txaK8KSEnEpd8FeXIPFNrJkmpdSYun1I1COTk4RgK7C_AJJGeFUM2s2dvd-zax_58I401Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/26884" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26883">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S36U-SXrmB4x52wxoHHpXMx7U82w5mh0zCyQ9hCillqQTN4RMZjh5Xa4wx57EGgr0UtgU91aeAGN1rwJnf-IRcdN9tqa8Epe8cDrOWiBthGFBNFpZkN-s6VHxl-r8LGbkuwEj9AzkTcrondwlwmkBVn20aGk0uZzMxCv89m3dkmINNRWw-8x3yA0xyRAlXq6O2MMWFnxYt9oqu2BjZaUuBav-9IsrhZMXWWdA1sSEyakJRakHBDWPzBnIc6SXSACV2gSMribwJ1zh9BSS4XMfbJC9D4ktoj8Yo8qo98L3JOTuGGe_wELL_JleZC9k5vcI0MpbeQQALA34ulLTddLEw.jpg" alt="photo" loading="lazy"/></div>
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
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/26883" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26882">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uICKIFQ1Ycfn1QXWIBmX07jXr-c8Hvp3Dz_XKj5yMXqx8wXfR9MlVyFjdnvrcWykVpiB1U93gcyjdcOBAJPJEtVPgyR7EF15Kbl2pgxFUotvsg9Fw8Lu8Lu2OkRSTiEjWxPgfW1QpXPsuzVEtjJzq92ibAWr2gqv1iLYobC2Y4qseqO0NHns_9pA_mlDLNFzjkKGaD567IOII_be4W34Lee_XDSzoZHaM-DT_ghq8ST4oOHq9fXNLGf9hoMO3ksQWe_iofOuKVItl3Umar0-sRqFa_n_hB7TlOlYvoCRtpaNTBLN5IoY2zfW12pJNUzduGXBawp0qWCrReteO0xi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
وحید امیری کاپیتان سابق پرسپولیس برای عقدقرارداد یک ساله با فولاد خوزستان به ارزش 25 میلیارد تومان بامدیریت این باشگاه به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/26882" target="_blank">📅 17:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26881">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2AVn02hpHWgYrWVaLGZjFDrEizLE7wYiAKV2s5wuOtbQE4mXMrDYCrx8zK1CjJd1IQhjlHb92aOytvGlgjBX9OvNMJDzhXZAc-1xlblsDKvnRxfP6gEZL1V_kWbLeQPuxpB57VXTtxrEl5d9T6ScM7g_MazIYRPYlvPMW7mNK-BStR7WNeAMhYpJHYoftRiLjDLqec_lUBfYlS-Ij9i8-CvYTr4olMS_BTrAbmO4RGAsLDeu-lqEbbzoYnct-KSwEQTlg0yfmL1LIjOxIbUI4Ba2nAZ-nqAPkjqxVBI5SA1VKbtoU_TOdlIjY9xmngdtWGJj1yoXA36FTjunhDk0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوتامندی‌ مدافع‌آرژانتین:
دخترای‌خوشگلِ زیادی بودن که عاشقِ دیبالابودن‌ میدونستم‌ که اونا از دیبالا خوششون میاد، گاهی دخترها میان دایرکتم میپرسن "دیبالا پیشته؟ رفیقِ نزدیکته؟" سرِکارشون میزاشتم و میگفتم:«آره بابا اتفاقا الان خونم مهمونمه! میگفتن میشه ببینیمش؟ توروخدا، میگفتم آره آدرس میدادم و تا میومدن خونم میگفتن:"کو دیبالا؟" میگفتم رفته بیرون مغازه خریدکنه الان میاد، بعد از یک ساعت باز میگفتن پس کو دیبالا؟ چرا نمیاد؟ میگفتم کار براش پیش‌اومده‌رفت‌متاسفانه دیگه خودم مخشونو میزدم و باهاشون دوست میشدم. دیبالا واقعا رفیق خوبیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/26881" target="_blank">📅 17:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26880">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbxdk8mnyaudSxvPPC37bGpX8cc7cmfDZjpPO4ObjEnqO0NsQ-0AVIpllseaVS-sWvxyvcCkMHem8BhiBMBETf3UCSOm9P8PEWJu-sQ6Xe7-NRNhnWgconb53usVhM_9i92skJglhzIRgOCsOiHH57SmGySlJ1Z9uD_3GcWxlgIlQaNHHywQHZ9a_5WVk7l-2h6hLXUVGQNAbe-5nlrxDzRc0C1aG42H3eVt3IKhv0R3QMfVCPDgRTinZm41cvl0DwWl1Q3kCyrUqeGSBuJMiU-c2igSCDGI5gtXwt9uf7juf5Thada1eXba4ZIOy70aSXtopil0B0mLPqSJziP8Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
#اختصاصی_پرشیانا #فوری؛ امیر رضا رفیعی دروازه‌بان جوان پرسپولیس که در آستانه عقد قرار داد با تیم‌ گل‌گهر قرار داشت با باشگاه شمس آذر قزوین واردمذاکره‌شد و به توافقاتی نیز رسیده که به احتمال فراوان بزودی پوسترش منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/26880" target="_blank">📅 16:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26879">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=hUxtuggM9yKRrgxDBdNMz3_HlPmvPgXw0KYtrshL5PDRj8atdGVfcDYslbISAJ2AuZhewmHA-f2PK-OHVXh5cqtU9E7aqc1SuPgUcgw_PQKeCxgG0jpWpRKJ3lU9qRNyWFTUOjFZDXMBw4348yljuGZLlr_-yLZ87JA-WBA0tAd3y88K58ehLwvHc-ImLwS7pGaB_SWzdUUk3eENMIMmkP9eAGcu56gwBWhT7FmDUH8nrDuj8rwAhzulcR5-mAsWlr-us_HHLAnAFNb0xdgM7bBxuJAnqykgOzzgETZ6JntLLZrbEqHXeOPAP4wZrqzeYmJR77JPHUrEq9f5AYjSdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=hUxtuggM9yKRrgxDBdNMz3_HlPmvPgXw0KYtrshL5PDRj8atdGVfcDYslbISAJ2AuZhewmHA-f2PK-OHVXh5cqtU9E7aqc1SuPgUcgw_PQKeCxgG0jpWpRKJ3lU9qRNyWFTUOjFZDXMBw4348yljuGZLlr_-yLZ87JA-WBA0tAd3y88K58ehLwvHc-ImLwS7pGaB_SWzdUUk3eENMIMmkP9eAGcu56gwBWhT7FmDUH8nrDuj8rwAhzulcR5-mAsWlr-us_HHLAnAFNb0xdgM7bBxuJAnqykgOzzgETZ6JntLLZrbEqHXeOPAP4wZrqzeYmJR77JPHUrEq9f5AYjSdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛ فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/26879" target="_blank">📅 16:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26878">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=QWtXW4ckxMS_Z8LxcjzR6tOjnMTj3QAptbwYDD5_DcmqiyLcgtXEQ6sEPu0yqUFD2YilgV6E7Mrz-j62ubBbyF7PSEl-wAMC_l2_yn6jv1FJiGfKpL2T0PaA_uO2GBUTZwix4Uu3GdzM5zj3PcJX1v39b0ai4datnyHGvvm5OnsnoDX2gdJvzeEwbwQftggPiVrqp374inqbzVKpA1YFlhNphcD_KFfePWb5WPcOUMkHOLZW5MlgFfLF2x59uTo3ap-sx2TagrdBTgm9T21X36s1_WXAHx38MPXHpoA-36cC9kWqsbBA8HdoF-F_4zgj6oTSMLcfHeDqM_dxBIlbgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=QWtXW4ckxMS_Z8LxcjzR6tOjnMTj3QAptbwYDD5_DcmqiyLcgtXEQ6sEPu0yqUFD2YilgV6E7Mrz-j62ubBbyF7PSEl-wAMC_l2_yn6jv1FJiGfKpL2T0PaA_uO2GBUTZwix4Uu3GdzM5zj3PcJX1v39b0ai4datnyHGvvm5OnsnoDX2gdJvzeEwbwQftggPiVrqp374inqbzVKpA1YFlhNphcD_KFfePWb5WPcOUMkHOLZW5MlgFfLF2x59uTo3ap-sx2TagrdBTgm9T21X36s1_WXAHx38MPXHpoA-36cC9kWqsbBA8HdoF-F_4zgj6oTSMLcfHeDqM_dxBIlbgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی کوتاه از یه مسابقه والیبال محله ای در زمین‌های خاکی؛ جدا از بازی‌خوبشون و اون دریافت خیره‌کننده‌بازیکنه به‌وضعیت داورای بازی نگاه کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/26878" target="_blank">📅 16:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26877">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjkcygl8AV4TBXK66UHkx5XMnaQSTUR-ugJ8irgPfywmI_YhcQu96aqj0H-sM_f93Jo4lS2GowU6ALO4thz-Mfo586guwTc7HP9V4t3W2dhyOvBaOsxTc11ARvxjW3SfPqOvyjZ_C3aYpg-ahLBVBx0u9CsVWndXxRlmrx4Ly8UDosf3Q4Jiey0KqZen19aDXd-qKW8KRSpaHJmMkY2guOjB_zPpoBa7DygWRHqvkvdl9eVYwsHO2iUjmjLOhk8TKKSfOPmomajdMap2y5Ukhd9dmA-w1-evuaCZmz6S4BZM9zem-rFZRaZhhfhQgWZNESLHHMPwoR-OCWnfumN_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|وحدت هنانوف، برایان دابو و ابوبکر کامارا ۳ خارجی سپاهان از این تیم جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/26877" target="_blank">📅 15:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26876">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kp9_ZXi--1k39GArbIrWmB085UNhO3q0un8a4hTWoREpaaosP5YFxl52MNBZnJ6sJ0duBHSHSL_t4OSbv-dpV6p3wgAQf4e0z39jMMeLE-E158_oQQmMe8Y3cx-Hz1x9zVRNq_NVlOT4JwGSKSfZ7--Y8C2he0h1mXTEXMkRQj73GzkzF5DHLCw-CnCSUVCBmCS33ZBri2uXSHz3tw7lhhB19MXwiWR7HiY7dGK8xpo8tfM_qS-MlxEh1OJZr6gk84Xlnq1toqmpPLTLHKZ9CCEDxeXCFzzgLWgS47_IK1U2gWJMJuIrf3FsKCaVKZjziVxaQMknta6FH_I9ChcEJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه تراکتور ظرف 48 ساعت‌آینده‌از محمد قربانی خرید جدید خود رونمایی میکنه. رضایت نامه این بازیکن دقایقی پیش از سوی الوحده امارات صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/26876" target="_blank">📅 15:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26875">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=J4LGHYhb1eM6gDjGWgXEw-jh27vUYGMR4WC1IfwLUZDIv_JobhnVfCYC7CJiESltiMfNrKQ3t5SbftDzySNcBQj1H-pwzg0Y3ulnh8VpheeVUABb20etxqDDrFXDBJfN7h0HevIsxj0-J8l8GShGN8ra1Dh68QQmaZNVon0rC6ekt-kf9YA9EblOMThb65CRW883vXkg-u3AQWkTXEF85xtAtPM1e-_lpt-JbAg_BiQV0iwJZpaF3vnhLSCAX-V4E5ne48RoNVctewSvnQfmHiwS_40mzL4Il9Pk5AsvaHMfHd3UEmzPZYqnL0IAmPV-hxiPa6fOH6unYLL6oTGwqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=J4LGHYhb1eM6gDjGWgXEw-jh27vUYGMR4WC1IfwLUZDIv_JobhnVfCYC7CJiESltiMfNrKQ3t5SbftDzySNcBQj1H-pwzg0Y3ulnh8VpheeVUABb20etxqDDrFXDBJfN7h0HevIsxj0-J8l8GShGN8ra1Dh68QQmaZNVon0rC6ekt-kf9YA9EblOMThb65CRW883vXkg-u3AQWkTXEF85xtAtPM1e-_lpt-JbAg_BiQV0iwJZpaF3vnhLSCAX-V4E5ne48RoNVctewSvnQfmHiwS_40mzL4Il9Pk5AsvaHMfHd3UEmzPZYqnL0IAmPV-hxiPa6fOH6unYLL6oTGwqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇧🇷
پوستررونمایی‌رسمی‌باشگاه اینترمیامی برای کاسمیرو خرید جدید خود؛ قرارداد یک ساله همراه با تمدید خودکار به مدت دو فصل امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/26875" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26874">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzESNnSo9XWyeJxAMsPfHHJfBJHbAt1OE4I8lTPF8ndQ_0IQC37gw3h5GMw90TeEuPTEyR9ImD_MHD8-3XeSRIcLqMb9FdFboDl-nQJwoXgIAZrXIEcRR8NGwYRNvzd4U4HaPpmtlJXzN8e8at5duLei2Uhhr1nuatljG0gJKPWigGal1t4Y9rOjs6ZkE67J-iqm0aJFPlsKLqbE80HvqmAoY44MtlG6WNsbCZeEi_H6j04cwvHPOJsKYcJgr55zHsYC36qy34UfPw_5Oc-39SuDz8dSYcPtQhy1meJPCun2JfVP6TVfHwsn4JgmrSVthuet7_R44rHKtUQZinAUMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارلینک توکشورعراق‌فعال‌شده. قیمت‌ها هم با دلار ۱۹۳۰۰۰ تومانی: ۹ میلیون‌برای‌سرعت ۱۰۰ مگابیتی و دانلودنامحدود.۱۵ میلیون‌برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود. میانگین درآمد ماهانه مردم عراق: حدود ۵۰۰ دلار که میشه تقریبا ۹۵ میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/26874" target="_blank">📅 14:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26873">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0molnG4jUPPGvf481j3SMYcg3D5BpYoPPtYu2_eUYhy1ojzPhW875Lxhu-E7Wm994kl8u9hE77Ev_AzppxgDmcdkFVZGFbRs-aGNbJb_lrinjFOrqHDjW4eR694OlbcaOaeLwq-h0Z9cJOjpAs_0otICIbwwPJn_okadG9xjVCuCpQ8kXhKhrTAJTsuQkqojLBVJnB_l1RdKK-jR9jyPjEp_fuI0SXp75WNJzwS9GID0njRzzNpOXd9-h--bkSVEOi_Ui04KxnE1TGTla1M9LOJQLs8kOjQr-DQSiPxxsnBY7LkctRmLZqT0aV43NR9UTRQyR9CtHOypJ6v3f4mkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
باشگاه آرسنال بزودی بندفسخ قرارداد برونو گیمارش روفعال‌میکنه و از خرید جدید خود به شکل رسمی رونمایی میکنه. تمام توافقات‌انجام‌شده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/26873" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26872">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=iY5NcvczBePxJ7_8x4kbmtqReYJA-f2i2eIyPrjidL1vIPPv1_u59sQ9ai2iY7CqJaVRW5KMKHx8szCW0YI-OZwcYkZl_lwT-VyLjJla7G30o234WKAM9CFCoaQ1LvRfQQm7BbB3QYH66GA2gDehZ7vWguMzVXRwbRynvvJcsov3MudjjbGrmzIkl5YC-_-7DBaD524Ygxkjit9zw2K3K5HuC_8ZLhDK0SBdHZ1YL5hO_lZM47FtjgOIssas5Ma9vOn1o48BeukCV9lOlw6tgtHCRNt6K7tZxNE5qwJbTQTvN8JliT-nmFlh5CcYzGxXWWNBJ4pvHnVczQ4kTDjNIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=iY5NcvczBePxJ7_8x4kbmtqReYJA-f2i2eIyPrjidL1vIPPv1_u59sQ9ai2iY7CqJaVRW5KMKHx8szCW0YI-OZwcYkZl_lwT-VyLjJla7G30o234WKAM9CFCoaQ1LvRfQQm7BbB3QYH66GA2gDehZ7vWguMzVXRwbRynvvJcsov3MudjjbGrmzIkl5YC-_-7DBaD524Ygxkjit9zw2K3K5HuC_8ZLhDK0SBdHZ1YL5hO_lZM47FtjgOIssas5Ma9vOn1o48BeukCV9lOlw6tgtHCRNt6K7tZxNE5qwJbTQTvN8JliT-nmFlh5CcYzGxXWWNBJ4pvHnVczQ4kTDjNIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/26872" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26871">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9k9j7dI6Xr1X-K4DlWcTPF02avDCMl5h3BRaAVPkoeWy6_Yn83KjcVayEP3hkCKL6s78gGDhGoKpmJ1QFwhVc9UbArWqgQhmkcTvnpnA-6njd7wRqSYGRJxeipkccypn6SF2PLWYqtUcJ-Po26aOnIDE9_e5-ut6j9fhcgVpL2Q1ZvoFYd3teboQY53L2U8e_Bz5xJsCh_rAx78UTBtURZP5zsiYPZFL1yHMa4tst8YITcsbdX0rlCybdGuuXsqui2OW-euVcJkKr-2DO_9ylaWXVFQbqdZDyNWkmKoZFmHPb9eqOgZzHH6kR-LisqZrS2as52hOPMS1SRDmJCqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه که علاقه زیادی به پیوستن به رئال مادرید دراین‌پنجره داشت تو تعطیلات در حال خوش گذرونیه. ویدیو مثبت 18 بود تو کانال دوم گذاشتیم. بزنید روی پست ریپلای‌شده کانال‌دومم‌داشته باشید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/26871" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26870">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=r_KcXMcOl2rB5CgEwNBvTmrkKZd_-C1ldWBImZlbZ30plCPkTNTghHhrLLSHHGc3yQAcPcsWKDxyCBkYCw5wbdZf0yFtiKMpugDzRqIYf6WHuM7h2XyUseeTY4aWLQZsiXlw1_pwmXJsluwV2M57zqim7IcIy-s_4rgqX63kH324PsbqpvXpsazWgQhrhVJ8RoQsnlIg5IMB-wQ_bcQ2hTjMBdYft4KqyigY0moezYw45xmPI8NgbiVqCfXh_eGicmoccerVO69pmxghCxOgmc6l0jWTDwRQaklChC8DDdQ9CeuxcUihaLTmZk_BqzwX-k-zlL36vqdWizs0UNOrrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=r_KcXMcOl2rB5CgEwNBvTmrkKZd_-C1ldWBImZlbZ30plCPkTNTghHhrLLSHHGc3yQAcPcsWKDxyCBkYCw5wbdZf0yFtiKMpugDzRqIYf6WHuM7h2XyUseeTY4aWLQZsiXlw1_pwmXJsluwV2M57zqim7IcIy-s_4rgqX63kH324PsbqpvXpsazWgQhrhVJ8RoQsnlIg5IMB-wQ_bcQ2hTjMBdYft4KqyigY0moezYw45xmPI8NgbiVqCfXh_eGicmoccerVO69pmxghCxOgmc6l0jWTDwRQaklChC8DDdQ9CeuxcUihaLTmZk_BqzwX-k-zlL36vqdWizs0UNOrrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیحات و عذرخواهی میلاد کرمی ملقب به وضعتان چونه درباره تبلیغ مرز ایران اربعین:
‼️
یک بلاگر معروف در فیلمش گفته بود در مهران ماشینش دزدیدن از این مرز بد گفته بود خیلی هم وایرال شده بود خیلیا دیگه برای رفتن به کربلا مرز مهران انتخاب‌نمیکردن؛خیلی از مردم ایلام…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26870" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26869">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFygl9nbpfW4LYY1SGGnIzGpnzZBNQ7lJG1o20GVJQ8pcVuGUwy44hfLsfiwn9d53tY6huk0oxnSdTZ9cwV1_7uXpTkipPoQAPFNolPO7Vlxy2YMWhREKCMLGJg0NNCZ76LpNMxrR0O13lMmIXEY6FBvDDzrjOvEg6XRoGheOZBWvNXwzr6ZY2RsUFK3lWxjXe0oSjJcl72KM3aDbGy8zvNtE-sUCpFRvAWt35Bo-DigEKQJJILIlK5ZAWt6dDzMa2gDNS4THztWh7l2qt2ExcKGfddDeMMiVzPONbe9wr2xYaaX_f_tj3_Un5saz_QHjjWKr5gPIVqRunFxqjxMiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26869" target="_blank">📅 12:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26868">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1C-xEwKIcGOCadr_r5wWKttIryor2CDyx_F_PCNB1e-mopaNzQ-Y3WRymA6GYD0-A9Q7FzYwsj6o-s_eEln0wnLYFvJfr60-Q_GNQNvopT0eRPhopRVckGPdRz549CzojZaAsySyi97uhsX7nm_cfxNUR_iwYRbkdP8MkpkdBia24mC3ThgznhhCbtO8Fwo3eiOsM0VFAH7uYYX74dNFh7LWdMo_CgHRbV_HteQsr_yhRR4VIJ3UGnUM91lNwI5HajUJ9BnjAaDRlBPaRi7mTdSiCPKk8MmT5afr_ocwKqe8BiPqNvmH1vmTXxGeXkxr6NYN3PNtqfTp7GWIaSxEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شکیرا خواننده کلمبیایی: جدایی من از جرارد پیکه بهترین تصمیم زندگیم بود. اون با خیانت‌ هاش بارها به من‌ ثابت‌ کرد که لیاقتش رو هم نداره حتی باهاش هم صحبت بشم چه برسه به زندگی کردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26868" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26867">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLcR2tJxq4mOEyLGgDcj_hb_MMgQrbQzdqn52nxxA1Ni3G_uxBgJlXpmla61MqtDOLIa3LWvomjRZ_RKcAvChZ9bzqUMdLL1Eur39UtswWKaW74s26fgP80TYfT-cLdHDyRwer1SzYZDrnmbVb47LdopTp0QtX4f-FLWN8EFpeD9R9IgCHtnEIjTBiA0qVA-4H75Y-WLiDL9xySjHa9Eau6W53KpWV1GIgGVJknacTuNRP7qDbquRZOoS5WLyugCPKFzw5jkyaGHD6YHpvmT_lmsQ2yBgyhC-0X5wViXo5cNb_1Hgqisy2Kmx9bGTatQ7jm9N1nDtY2mJxhD7fwV8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیمار داخل یه ویدیو به محله‌ای که توش بزرگ شده‌بود برگشت. یه پسربچه بهش گفت: «من پادشاه این محله‌ام» نیمارم‌گفت: «یه زمانی منم همین‌جا به همین اسم صدام می‌کردند بیا باهم عکس بگیریم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/26867" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26866">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyX2IGHyMHMB_oNF1LJ9y8Lj_XlcEMJhw-qWxrv1g4XXNTNC8yNZrEnNJc6HNIC3ZCBnT9ifotR9aMW_R390lWib5KAqpZ70lsdJZUMLEtGB7zsX382GHwfmU5zgkF6R7GAGzLyxGEBGYACxuwxakl09yHiV_SoWFcgGlZWCs_lyC0HgR1TH2eqYkMVLS9xGjAFjO7ZAeAlV6H3TIcrQJH50BATzXMQ8CA2OenqOm5NsA8wa0Notq3Gs3Z5DhL-9GcHYMtAV4-1jgRzsVpCoPm6Q3JeeaT1T-QbBndJ-4pqo2brickcY42YKJc4cu3ykUfgoxoyNQgc8s6sG1wzDaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
💵
اینجامیتونی‌روزانه درامد داشته‌باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/26866" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26864">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzyuQMJQnvnXzrDHUmwb_FdZsmZ_QW9JU7zJny9UtHV6woJEHZgzcPWvswytBAiBgrJsyrGwWei8fCk-AfEV0jhAG-qvDTv8bbeLIcECPNvcgUw_QkWvOA56wqenpR795UCkNc4yhfKbDxHtJK8H55NKExnOkd9j3NXHPMlyUuBLNP26Herw3KVVcPz2-kPNI7pcbQz0jJ4TljuVUFCNlN1YjM6EaYA2ShkcEHBOCNvJ-7OPpII48FF58vKrCpLU3Mqhteq56lQIVc3bzHDSNorKpzLjeyWh1WTmn4Pwez0VMRsn1RZX4QkMYHumdkO_9yJkGTzAQG8C0Oepfr5KIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0DBquqXkg9-fH6kfWY6STeAogrWexUYxPqaPiyOz-RXjGGcMz8VFh6-1LoE73rTZyxqpKCDmexvgIhq1iEfuokR1MVuStY3Yz_qaqDSnD9br5lPHleeGSAmeks9HE4xSjvsG7KXDppIDrU_RG1PU9s9EiQZfIh3vJHd1u5tJgr5qiw3RRcq-0Fwnae9E0Q1RnGxCKaXXZlckz9NNuGQpZUBLJm37fk9NnyWWzVgY4h-cHn-8NzC0sZmfpC-WwsmbvXg4VVDspji9wlpCaqrys_v8-xgLXwru9Hhn3HQGVSxKz3NF3Ymsx9xEoZOzVnflCXWycszcUa1bPmgHQez3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رنکینگ بندی جدید فیفا برای تیم‌های ملی و باشگاهی؛ لاروخا و PSG در صدر قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26864" target="_blank">📅 11:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26863">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpLi7fWpS1y3tqqDepO4mwp4Emu_N9Vb25t2uwqGQ0IpoWYPfW9RnEEcA_X8E8U7V-4zreiRkeI7zbKI1oMUwJpJfyY5vIUykYZ9wuYqK5QiJ-XLQqYS-h6HzX4MU4OOk-z5ZANV7WBxAyzwZf9MCg75NyHuTulYLFNVR430sj4u6m5yUI0m8-_cW5OsZ2GtLnS8FTGOiqnrxnxiiBPMrXcgm8AhyGw3TOD2gKlxABaKMv8Pq1tOyXlNmeJzpwEi1Cb9swnwMRLnMX_ndiKoV4hhNICUrGJdKXLEboq1WmQE9bXDvqolmSXLLbSGUhTq825Se4oa7pjZtX_fTEzP1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سعیدمهری هافبک‌میانی‌سابق‌تراکتور، استقلال و پرسپولیس با مدیریت باشگاه پیکان برای پیوستن به این تیم به توافق رسیده است. رقم قرارداد مهری در پیکان برای دو فصل 25 میلیارد تومان توافق شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/26863" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26862">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4UZka2AF3bEJVIseKfllpqgHVgh_mLvOxLk8MbHgZqjpvKKqWcpBzWMScvfOj3JiIYXC0cAlhYRKlAiZ3kYMn4M8uAX0HNuflXf5PBLQi5h_6pVwi9xTsQSg__4olUozkmD00RR0UWSkuq-ITrRAjwAKkiyS3H9F9n-N43V7CDg5K73_IJWTuj2h2f3Mxg14q70vEfq-YaiSOOKyWAH1-7SrX4OoNRHBjCg79ADavEs0y1JGX3q20wcR9Sbm-fgz1chcBlXNXLfQM1ubrZhT9aTc27Owh3RYK-SEoRFYjtwBYb4TRHaRaJ1SdXKqzC0W8MpspzzMeKHhl63Nr37dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عیسی آلکثیر: به خاطر دلخوری از بعضی مدیران و بازیکنان در پرسپولیس، به استقلال رفتم. با خسرو حیدری و ریکاردوساپینتو مستقیما صحبت‌کردم‌ و هر دو هم موافق اومدن من به باشگاه استقلال بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26862" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26861">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=MEqY8QjD3tivHJS1bkEIIcZ7zd9rRtAXajP8RtSsgkAdStPlPqa5r3LsLe65KFrkmPF_6mH4p-rMssooyxvyqLMdhQkZKiWImJ6nXEjN2VZfYCexIttuzRSp9c4sFpeo4hgulIaclVQtNQfx4Y3owE_36sejAzqXRkWdS1ePuqXnm0klt5hqT03J5U7XT8U3IgBR4wHR7nZ5NYVxjpG9CrvGjAK8RnDMEgK0JcRA8fnW6hWSE1jLGBIgX0pyq4C6ibu4VgAe5DwpFK7FLAl6q7YdcsuDbJS_eqU5gEL24ceg29CN0z7nYyBnrGpkPvcRgElMGCMwxxyO2jKKp8_IYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=MEqY8QjD3tivHJS1bkEIIcZ7zd9rRtAXajP8RtSsgkAdStPlPqa5r3LsLe65KFrkmPF_6mH4p-rMssooyxvyqLMdhQkZKiWImJ6nXEjN2VZfYCexIttuzRSp9c4sFpeo4hgulIaclVQtNQfx4Y3owE_36sejAzqXRkWdS1ePuqXnm0klt5hqT03J5U7XT8U3IgBR4wHR7nZ5NYVxjpG9CrvGjAK8RnDMEgK0JcRA8fnW6hWSE1jLGBIgX0pyq4C6ibu4VgAe5DwpFK7FLAl6q7YdcsuDbJS_eqU5gEL24ceg29CN0z7nYyBnrGpkPvcRgElMGCMwxxyO2jKKp8_IYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26861" target="_blank">📅 11:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26860">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkQqy4djgLRpd_-Fm4fix8l02kU2neTYwbVnOIuGb4Hl-btHaySIYIRU5YST_aSJ8YPPleAMY_SOjG9lI96_d39pHaqtcPMNTZTgBHdTVxVbSHd7OM_EKmOVwDp2zZmLdgmJXEIaf0jII3_H0hn8VG43rLeHneoBezzB4uYB5ojUULaon7W6-7Ac5pLgJfBGwfDLmqgfOZtzs3oNahnGVv_bxhceYwiSvtAiY0RxH2HwPkcrIJJDd3khhVNp2c0fdJlz5v77T7_rUlqdRWr3rnqWJA0QhQWdI16SbjkiDp7ALnmE6j3e21G4aq65g1rzu4PWntE0D--a8qgTCkgStw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه خیبر خرم‌آباد رقم نهایی رضایت نامه و فروش مهدی‌گودرزی و مسعود محبی دوستاره 22 ساله خود را 150 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26860" target="_blank">📅 10:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26859">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGs2SvYp1RHi-gxBD7eu6TtQh1LwUN8oaDmC2QELf_-5hrDtNP7UbcVHDmlepE4lWsOmMXNV5krEYl1o58odEex_qAT8xVSsxu3mMDHxZyCjEuNa3MdRtNZwGHOIYol3UtaWBSNp4voEOtHylIjJriXIMgmy5OvVRB4WBiUL4DWyOcHlsnexXQX4oQCd2nblBWEajmHQ46U2fCjwjR9P8U3kKqe8XbXPQ_XTdYfgPwTZ6jkQoQVapJvpuzk9WgQoaeoZ1VgdxP1D7oKHZEJ5XnzQEy2caj5zfZTRWt-Y1RljvGI9uqOeEkKGNKxzr9NpM1znJ_dxAUfCBEdX3rIC8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ عثمان اندونگ مدافع‌سنگالی 26 ساله سابق گل گهر از طریق ایجنت ایرانی نزدیک به خود آمادگی‌اش روبرای‌پیوستن‌به پرسپولیس اعلام کرده است. تارتار به‌مدیریت سرخ‌هااعلام‌کرده که قرارداد دنیل گرا رو فسخ کنند و اندونگ رو جایگزین کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26859" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26858">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oP88x0qWpNpiKIQw5SV6CNa_DANesxDU6HpK4Jv7MM9UFw7JWlOCvjP1Tigteq-QcMinG0mRrhqpWi71uQn6vTc0LgowfGm1jEwbvEseDweBA1xFHik8WzEOvHFQA3ZpXwmp1BGxUbTRHzNAat5vJcZz6TghZmPvIlEEAElWToZdJAymHurpGJpQgXhApZ-7-aaBfbjRlalUffEkkTQSouBJW1SC7HHqn-XUSEXyO0SEepA8FI5co_7U5IHPmtQbJsi_mudFbgXXmO7p4nCCLHnKqaHLVAMQx3fO1rlKJj9ShRa42KKhAqajIEvL7f7copjt-nm_7L7O4nR8NE8uPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌فابریزیو رومانو؛ باشگاه رئال مادرید 25 میلیون‌یورو به لوانته پرداخت و باعقدقراردادی پنج ساله کارلوس اسپی ستاره تیم لوانته رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26858" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26857">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCQcJPkl5F5-GWMsZ7kywbeLk4ZraK-im_-_cUYc2vWOFk7uEQHM77gKFIHB61TfbM7XAr8LeUmDm76GC3YnRUX8GMk5oFEQIIajl2DGLS_AokTgJ6pOpACBqfQSAbXZkHvGEyNJu0Y5NYFyLXoEzSaWZYbeYN5SgOcsPja4lX6rdAi8A2KD_XZaJxRfwHmBtQViPEMjyabDo4sq3zJELLBVA6P3K898AagwhCPxBHSeewaH_Fqa6ie4SjwNMn8Dkcqtzn41KnU1iOC6P-H4UVGJsEffE0R9R7tXe9YKJvTRmTfOJOiQWd4ySbd4Jz0FDUT7wNRF3R2eKiXlzfWVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛
فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل به ثبت رساند. سه قهرمانی لیگ قهرمانان اروپا، شش قهرمانی سری آ، دو جام‌بین‌قاره‌ای،سه سوپرجام‌اروپا و ۴ سوپرجام ایتالیا از افتخارات این اسطوره محسوب می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26857" target="_blank">📅 09:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26856">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEBfIZUvSYVpmDOITsuevUypkRZHBWTq1b2OMgNT0ewtO8KISRaZyABLZ8oKdf-hKK_jxuP4wCYLO1PEGoG6VTPTk8XDsvI6drB09s8oBBqtcsIENMEroE5Bt3q9j8CXa8hNPRmAl0hbEx0ws0JJyYmicveE4ISns67sDz4pYmJwmsehPJQ9eEpFQqX5FKqDnjopKcAg7qfGuF9H7PeabZ7Ra0ZQsY0-3k_R_LW6gMQU9GUBzv9VhSmxWBj_uoOtr274ZonHnpDKCidWYejGtErdO-lcbIlEHGcyT01WY9h28v8ltvokQ25InT3Kjx-2PqfWfCuPZyAlnDEtVdSbgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26856" target="_blank">📅 01:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26854">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WImjLnNt5UeCH0BToDXwKum0u59GMZWcDUHopBzEuSTUFk_AP3IKUYZrPhnbdG0nUCZ0AHp2458ci6IkMp3HXQ9u3PiV6NUmwKWAlAUR06SenJy765VSTSXwQArgD6IuygAtxZp7i7Z7uE7hy3H4XZEZWgeNPzvF5loIPLrOjmmC_4S-D7hRlLK_zeImv7a5Ii_EaRLJ8lANWrjLqKm12V9HmAugB866dJu-qY-bvELDHw8BwK1X8_Ce1oMz3Sl4BSkhdwdsSLp6MYGvwfFLbSAUSYflx8EE8uJKLL7iQmL3iKGUZCrzkbUX4ckXItLlr5_F2z7fyqCA5bdEwrgXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbzTQzFRShsfuU0jF6BT29zR9fo1sEPeytsEvcLVnQL9gUtxWMEUZY1kTgmV09lJm4vfqmTBSuMCvF4eONf7D54zwc_RTUl52K-Ea57LDe8gaGnh-6KDwD5wYqcXYfHSjgkkYpiSka7ElN-GTSan2Kwh6hQwbnd7gUmqSqVdqVEWuws4WbVQoslbsUTWmzwIflC4hVP9dYIBWjkp_s3TmDYtS01ryhYaHM0RBWMI6AvMrVw4X_o1Mmi7HcNFHlZzHerOToDtqilBD_69ywB7Hzj5xk98XaKq1JH7QNL3NJdso69pBlQ69kg85leXhWgujrSJfZa4bgU-WZQbokY2zA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26854" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26853">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kgvg3tsI2p1aYppqQElMeYe0OWUMgKxuw4h2V_fz6xs5NP9dNHC7JIpU-03aM6RD8Uc9RbvnqmcPlscWQdtGJlFzr90Ey-2ZQPep8knsoQVcYOoPuA4WZ3Btbti867xDuOLRT8rhhZ31TqRrAAY-03PbkyNlJ37CtqtpcFj81enPcu5e9g2NC5zy3Xt2ksZ--KjQe2O3adLaKsanapSgpJCRXpBBLSTMDmWYydRHSR8wmzjVFlc7OzBX11OOF_DcEiSGkLakW4aUCfdunnNlPOQqxTxTx63lnJ8MEsV_NmsCM6_Wk8YRBCe9BqHmcs0t9ZlLq32zAWpt3HGvEAKU3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال امروز پیشنهادمالی جدیدی به رامین‌ رضاییان داده‌که 15 میلیارد بالاتر قراردادیه که درنیم‌فصل امضا شده‌است. باشگاه به رضاییان گفته ظرف 48 ساعت آینده پاسخ نهایی خود را بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26853" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26852">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeEuZk1ZZxKFi7XbF9uge8FcSzwVsDm_krsWRt-FtYXcba4W73tLTFFFJGe3nkWB7tsAsNIQ6Ze4PJ9JvbsO0A2sMcXOSGDXeMvkV7-cmTBovFMhN_Lmfo4iikue30enYyX0ZOrVHPgEyND5ZSeWaSyxJAfis_SmjyQuq0q5h6cD64yrh1aYaN30FCSRz9e3ykCTKtikbIgQlapAlcPhqip8WI3u9x3XwcJ6s-MWb-CvOO92cQhY73gFhZzF8GMlGcM6Ztv_bIpuooEWubvnkpXxXcbDSZgmCkmn6aMBWGMKNIihdvRQya3AYTdEfAi6SrmrPy5elj7cWuO_C3NpVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26852" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26850">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3Cm-a00gHu2KpJDfSNWwa5CjWuxCxCGchkEt6P5CIhnzmgzb8BrF0TcnhRcjnkTBmtNlN7oQu_k89gywwzkYMCBzBpgAxbk1bo1uMlbjzPQ4kEl7_BY40e4QgYmK_R1qd3GwT_LZOybQvt3V-NS0cQrpIcLICA_eBspUzA7ZVBRlHkdh1-HNPMHunQvyEuBl99dv4dkp_qlBynh_KUbgj0su0vhH_3sa6_BIwWOD0XpaxBfxesVIOKKZrqYJh89Ei58OJXr7CcoZUaee6LnVVYWaxZ_iAI63nD5-CZbttSHjzM1A0cCTQ5Ea7qRVEs9jOY98uQZoiBqv2ZfxzLcSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس درتماس با مدیریت باشگاه پرسپولیس‌خواستارجذب عثمان اندونگ مدافع میانی 26 ساله‌باشگاه‌اخمت گروژنی‌روسیه شد. مهدی تارتار از بین ایری و اندونگ یکی رو حتما میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26850" target="_blank">📅 00:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26849">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t867-Mud6YJ1kDKTBLNZo2sZ6q40PGsaGg13--JTPUcS0-63lTQhVfPHv9-wYmEyGTh_p_0saBNge0f5I8pnlRYZVA_2U9hUYvQQkaquFWfsIXhmJiisz-wK4Gi-WcGPZG-LemLnLPRI-4O_roAsn3fHd__dAU2DrauhglIYkGeggnml3GQofv1C-gJ5e4eULPG3YW_awUMRpYigari97_afE_1cJuG0eMW0Vyl5qHeAfGO7a07SlpQqYFMcoDHpRaadMiuEtXee3sRN2HqG9HbOgn32W1z2M7ObO9CFdZsfoGrGeKKg8f8IUw_GRAkAo0MSG7OQWf2pl3Fn3mM5NrDc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t867-Mud6YJ1kDKTBLNZo2sZ6q40PGsaGg13--JTPUcS0-63lTQhVfPHv9-wYmEyGTh_p_0saBNge0f5I8pnlRYZVA_2U9hUYvQQkaquFWfsIXhmJiisz-wK4Gi-WcGPZG-LemLnLPRI-4O_roAsn3fHd__dAU2DrauhglIYkGeggnml3GQofv1C-gJ5e4eULPG3YW_awUMRpYigari97_afE_1cJuG0eMW0Vyl5qHeAfGO7a07SlpQqYFMcoDHpRaadMiuEtXee3sRN2HqG9HbOgn32W1z2M7ObO9CFdZsfoGrGeKKg8f8IUw_GRAkAo0MSG7OQWf2pl3Fn3mM5NrDc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26849" target="_blank">📅 00:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26847">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbmLXw_CPlfSHfcqmj4m9dIkA5cPp0kGZ63rs8nO1v_azSlzvpXcKSmldmf-vnenPgS0OjYnOt4DWvtuz3vclrjwG5Q2B76hDsyktfm29JQovPQx1YorxqGeOhRZLU5r8ctR5NI0xRSckoQtM6H_FpZLyy3UxN_hntRX9iuM5-MyBw0KO_D2eqyClaZ0xh5LVPrcuykIeAMu_2KIWR_BBum1cABT8cRzZd-O3CiND7NSTRdQzizjtwVG3bM6vJCT-LC1Iy462onXiMG7TiIFzjPo_mEFTVop0KUJXSa3IympoHmCIAO1ty6n_x3974zt_LrKn0ifdQbzWCWDoLVTCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26847" target="_blank">📅 00:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26846">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZZbRV3NRYpewv042ZCdI1RqvLTrtwtcuwW-T0QWNJciBDDdriCGjs89GN9Uxe2r7Lj-nX-5Ah3qfZNCi0YWEOOi2MMg57zDEjzCaJyFMcLks55Bm_cx6vOQ7uCNHVnECpgIO637_-zSkOSrJw7154Up0bCk2xgJQ3px_wSolk9pDETRl48lUfAQNK2clHX4WzuFn8VG8ia9XiZMrdHwAikn1XTyr4OCXhxUaDZSZRD_SBYaHoTKwTQm42_HftGQdfDqfeVzbu44_szf2o_9qbWeBV1aIqA_zuEAfIag9hQk_gQrgFtH_y0JUSROWxXwID5eyc4n9IckiEAztlVryA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ کارلوس اسپی مهاجم 21 ساله لوانته بزودی با قراردادی 4 ساله به رئال خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26846" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26845">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-lvtBwmUkIWWoJzCN8zIEyEcZcvEUyFpzIdQ2Aa-QmaIKlcdbYOVPvLeJByiSvuY8GUGi5FYDDLGSo9favoSjNvA8DBtYyH0U0vtjGaMnLeZJtHHTVEXM5anIp3AaN4vRefpEgCB_KqoBHJNGULqZbxXN4YyIbcw0HNSZVNS3GJjtGs96sbxwoi5R_FOdBzymNpK8hZSRieJmlczWk9StRXSEx3-yZQfKZGHUky9C0Tz5LgtO4cqUZHwAjUwB0UWLbZ-MUs8YoDAsdLAuN5DESTFdi5-3ZR_fGhQUBV72oA_z4CwjZE_E7fKu4HsRrmkWyMGXCk-GBWUYTptKbxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26845" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26844">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeCPrh-BZt4-YKwFfHVlhu-54ZULoap9fVjFooIn604u4a7h4zougMHYR0fpdNOqICq6FUxYtGOzKk4YEoqhYt03o2TIJwWLW4OeaLJPLGkL2jOmkGe70TdEsiMEbXx-7-yTQkK6AhrnuaMlN0kPR9b_nMBlYy2Ipe3zRFJba6D8mpvjTjZ2xI3dsHZathwnTYaE6KeAFeat1UlcLDEdHL2UKI_i3nyi0VW3O-EiT7G1Zpt8vkdSCIyqfy14WZBm-4hSfbqPy1TnGsfzah6zP7MIxLD592IX6z4Gs8dkoOZ4-xdP3tKVLyBMX2t8EG9nrBzdFvKDHq32SHOCAbAmAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26844" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26843">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3XFYC9bJ2MrpPc2fGJuWYM7OAgldABVdecDmYerCaF6UwWXWEFFFGZGdKHR61KJXpEh3VO0MAjKAq4WDBB6gXAoa_zxkf4nRXRoOPdbO9J8M53MP_238G0pA9zksO-DaN0YPW0Fn-PFaWOV6lKmzVVbXsnhuB9qLoBU0jo4yOuEiNhu2ri7ZSH8NUPF2s7mhIP3n7dY9vPt8QlIQoLn9wHt-b2ErETmBiKVDT4_MKqKW94gufhaIogM04zPoTo4biY3elgsCfgKFHbogUkCyI2hYHYCK7IhjLblZnRKII6ouFzq4eFpPypSuaM5eaxx3uLLVQ5b-9rS53IW36-Anw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی رسانه پرشیانا؛
سعید دقیقی سرمربی جوان سابق پیکان مذاکرات مثبتی با باشگاه‌صنعت‌نفت‌آبادان داشته و احتمال اینکه بزودی قرارداد دو ساله‌ای با این تیم امضا کند زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26843" target="_blank">📅 22:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26841">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAuYBtxoJigFdTbCZOBEs8j3azAOlrT0UfMpbiZ-2HkeEXb5eOaxPyuW4uFi41GMyRi2ATibteX55F-H4ruN3OUt7e87cP4zqqyTVzbtf-7w7Z2yCsXdXaxDhjhseDLjwZSPv3iyaj3t-ah8TmZs5fuG2uG1PiNjMXnqOxba_PvjStHanjiHQ4r0oEcYgwlTiyUfywvsy8Z8D03wAYNI3fXtJbw6YLFnmxeSvqB-Nw4P3RMDahg4P5MdHVU2KY96xq4fTmJUQPtPXxQ9vnVMD8Ckq8ogsCk4lhvf_f3uAUtIfx6LSRk3UBAQi4J50Xye7MwaPEJ8tF59__7D2BUdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل در یک فصل برای بارسلونا در رده دوم این جدول قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26841" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26840">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bt70MGzifeiF4zOnQsBrs-YI4GuiRkKqHvS19773jpEk_cOdHpddIEXs0ok3HHoFmUf3SwIb-CF1WnHGUhLLcljBmg5MTJkIU0aSYJchOjS7vm_m876wCBNHTkUgDGHzG0f5G98chXnqSkW8EXnemZ8lOnjRL7MmmYIU4cZA3VeE1eWor16at5J5zFThNf6-2Gwfwlpze-EAZEZOLSK6O18_pTjwXPBxsYHOKvOg41BW3GPkucGuN7m8Aom-99U782bnt2Zy7LkT6ZtrYQlPtkpGoJlMdd9Enmd7LybfGfcOQ_5YzW84A2USmHfHT2tHXcPnLXmzX1xeIt2n3oUs5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26840" target="_blank">📅 22:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26839">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKxEBAS_5ichLcNLmxdE7Wbc5o9ftTnzN1FaGkyxaIs4vvHl4Rsh8cA8urPgtL5le7EbLcehwxEWH3XB3JGksf6wQyJwYP3RYv7DTfFbxoq_yT_94XjgsPF-h7DeYD6foQfE9lkQ-qz_cFQW4o5Gq-A77VEsFMQXBPy4VsTMA4ZtK6rQLJRZla-48GJbcpjGMpyaNIClKF4zQBpvlqpWkg9PUTOjFLvNWuEEAQRLMlIKuy-7f-7km1WFibJSOdAb41Gxg_plOH9TXBTk_QcRdqcTuUFBov5OwyIfsBVBYHSohr5pSkwl_urr-ta6JNY-gsqtYUYbXMC42FDE5RHiOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26839" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26838">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNsCnzUKYyWJEpytetB14pzwCmRQ2mTZVNT-g8OAPscOG-JtICMCcytprjI3ygNx59nQuHxH5DAKtLP1mdOjLz9M2MMxQE58wVO3yNcXXQJ5NQPJKjAJv-RF5ye0OozapwEwHGMsYwF4xsU6UnJZdRMeMHRLIBgzkPq2cnuKO-n_nAAioKSHKq4u7srcLWWlrw7JgYvfE4agMLzjU7mnjzF4atyCtPjrDSwIDcT5lKL0M_nn93zB1M7b0cYnuy028Tv0WWtTiw_l9GJu_3-bS-M4WZ8mNdqbJoYBuVwxG-g6zoU7VvapS02tjl0voZedeBhfamndXxCUp9lZ6jeS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26838" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26837">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKtT0fVYP23gJ5wBb4-QQSbwuhN7Kq4VGYqf8kt0NBm3xKccV_q9bC_GIuUuBYRwZCfGM3_EfUNJR9ZEFklwCmkT46vmIsv3vVD1eNRAypiDE_DaXpzoEaPWBrtcOnBiOgWRsy_zDHA2MIiaEYcjW6hVxB6Yxtj53H3r-vr2wYcnDDwz9fCjxOHjO9TG6Fp41pEAZmBO1IYdOsnV-xhv2tDVEs49UdH4NSqoaO5tgf8YkT-7NODN_jbr_EGI0ms7jEo7UdO_P1G7iLyLUI3JNEa2OwxNsVuP_nuwJfp7llUZAUmI7m2glDa10Rb8Bdcdkv7Y7qW9RMk6gClgu9TECw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26837" target="_blank">📅 21:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26836">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlDk293MaRXgQtpEUrSEicUvPHRDKCkynHLMHUbFE-xFEE7GNgsKW-5awu6iv8cnjVj2tYdnAPdmF2-ruTqiiYzAPR41tFjU1VbO2fxRI50V4Kg8xZUlkFD8DryiUon7LK61jVgaQTtblVta6BRNxfdC6N0UILPi7p-GPxkajWgSZAzfo0qJFNbohHuZSRuy4pzxnT_XhUFBx2lSRC5hcu-QrK5YVEOeno4i652bcn77UQQfLUDB9raK1fzwVA3d0JPJCwK8qiD5nbWVXtOpSwBxf5_CZE9gnvijBdFjE_MVBbc9XaaXoeV_5A7nkoNi_lG15MsQGhub6rSkI41OFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی‌رسانه پرشیانا؛ روزبه‌چشمی‌کاپیتان‌اول‌استقلال شب‌گذشته با رامین رضاییان تماس‌گرفته و ازاو خواسته‌دراستقلال بماند.
❌
پ.ن: دربین‌تمام‌آفرهای رضاییان رقم تیم استقلال بااختلاف خیلی‌زیاد از بقیه بیشتره. تاجرنیا گفته رقم مابالاترینه…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26836" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26835">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=hvD_48tOK5yJ7SQ0kFygcVDdgThgmfYVYLK1HnhtOTbIUPxWD6OlvjyBUbSnmFfjZ2S4llVTtsd37RYz03cr3PHZevWMvE0uLvWxF-vQXQWrF7P_nPqXoMuVl4Mgtb7cxw5TDt0RCrz1otWqPOCYWuYaRHXTU193DO8rqAKPuEWDpaEcaMV8horFfurfAanu7eM7AHdPjOt6yuXWp7ve-dUkioFLUjZ36pSfClReXFfMtDp4Q652yLhhHid53eRLeoTgy1sfpPO1fdYAAaqSyuT5zB3qInGBOGRgEDfqBdQ02Ts9I4aTR6tHf6dQiGYWbHNWe2tjHx2sqz1VZ4F85Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=hvD_48tOK5yJ7SQ0kFygcVDdgThgmfYVYLK1HnhtOTbIUPxWD6OlvjyBUbSnmFfjZ2S4llVTtsd37RYz03cr3PHZevWMvE0uLvWxF-vQXQWrF7P_nPqXoMuVl4Mgtb7cxw5TDt0RCrz1otWqPOCYWuYaRHXTU193DO8rqAKPuEWDpaEcaMV8horFfurfAanu7eM7AHdPjOt6yuXWp7ve-dUkioFLUjZ36pSfClReXFfMtDp4Q652yLhhHid53eRLeoTgy1sfpPO1fdYAAaqSyuT5zB3qInGBOGRgEDfqBdQ02Ts9I4aTR6tHf6dQiGYWbHNWe2tjHx2sqz1VZ4F85Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
کریستیانو رونالدو:
در باشگاه رئال مادرید اگرموقعیت یا پنالتی خراب میکردم، در اتاقم رو میبستم و توی تاریکی با خودم حرف میزدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26835" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26834">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2dS3LjOaQhSB-6-N6N90L9sQx8lA-jC2kpzYXI19qgyNN7PlmV4Juvbx0XvFKd2atGIQYoTUu9d0yelZfnAjdwytf-s12CXA_9XSY6ZS2MjMCachQHcu5wPTr2cpzUje6DcaM_CR0Oi_NLiz_g5-ZCEmzLbUffrYbAO1RMwU1aHZA4B0Eb6-W52bn_oXEDH_vk2SW11ZDfKec5QUhasvLSaSEiB8z6tiaLMaVwjcPoSZKKn5mfa_W-xZR8QZIl_H1hl9xGyjOg3gxJboCRto0X_4V7X6Y_DDmx-tSM8Vx2JeBSLyO8MPUPQ6pDkD9d_9wURV_DBfCkA_tlRoYC7dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26834" target="_blank">📅 19:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26833">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdOvaNnzvbS3qN8kuPJ4QsueZoATWzYXA8i0JslaWiK13pLNuvvHNGCXdnMDFmmpI8xUmiyuq7gH5l2ZtcKxPnGPAuHYSyxNI5h17QzmEkpwcWzYy4K8PLwl0sAjIWBndM7wHjd758h5mSIA29ITXqObGsWYkuj7vKCMxmaKBstI2WAssDfDCwpBIw0ge0UVwFT8AXTdJMMSFQVigKZZ-WwLpHBpE79erXWTMNkaM05vZevTCFU4cUkeJ0pl5iGVMXWzyKUS1s18GG6NxZSZ_6KbppNFSvyOR7dXama1_S_aJ8XIXJxNi91E_JbIveGrvO6i710gRXb4syQHUP5Xxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛محمد رجائیان مدیرعامل‌سابق‌آلومینیوم‌اراک یکی دیگر از گزینه‌های علی تاجرنیا و هلدینگ خلیج فارس برای مدیر عاملی باشگاه استقلال به شمار می‌ آید. علی فتح الله زاده، سعید آذری و محمد رجائیان سه گزینه فعلی هلدینگ برای سمت مدیرعاملی…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26833" target="_blank">📅 19:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26832">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbfLxAW2UVRBt4Q2QEM0At0jlwm3ovKdF68OD19NbHz9ln0Evxm9B_Q2_1qG1mvv9A_zDR7dX0wERk2Fw6hWloVIrLQNqIBPHSIEHxfyA6jvy7IajcauAV91PvK7urA9YM9WM2ZTCt2L6JxP1I7aeLaSi-nfohFWi7gGtE1okHwdduSzAY5xVDPHlXevGurUHNy7n_IRXTNhlg4ESMdr-jwlpIJ5g8o2v8pnxJadWHQ3tDMPFqlzfuZ3tvDOAzRNQr_ndEQHA4KgBL6wX5uqLBLDCmBTniMol9uj-Lod8akvHjTV0-hXHBawUCCvLgdGgGOVo7jbSBYgNa1dGZahHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26832" target="_blank">📅 18:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26831">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=QZk53nz2Q1l0sXw8Fw10_4mrdA1RpUH6hUYdOfP52xW1HFicYl7oax8gPpMzd-z-IrAeyYfiHl2Xot25X9fGWHzE1nmxCCuBtrJ3U-5zXElY6SbmnUL4dw3Fj2mukw28ikOqpmvqo0NUUuai55yXyVcDAUotl7foQvTgUnrlcVXB3GVKNNYM2EWNqOkSNjGHcYM70b0bxqNbg1-qdXDqXpveRyi7mu0j2sxXw6PpAWrmELMWIGb1sOMNDhqWL1-eB5_VJIPJtb9IGNlPvfJ0eWqGviLc3dN8fTM2yM8guh_MdcLNAvy_EOVRlNe6en3XynxEGThaof6SodUZ2c44qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=QZk53nz2Q1l0sXw8Fw10_4mrdA1RpUH6hUYdOfP52xW1HFicYl7oax8gPpMzd-z-IrAeyYfiHl2Xot25X9fGWHzE1nmxCCuBtrJ3U-5zXElY6SbmnUL4dw3Fj2mukw28ikOqpmvqo0NUUuai55yXyVcDAUotl7foQvTgUnrlcVXB3GVKNNYM2EWNqOkSNjGHcYM70b0bxqNbg1-qdXDqXpveRyi7mu0j2sxXw6PpAWrmELMWIGb1sOMNDhqWL1-eB5_VJIPJtb9IGNlPvfJ0eWqGviLc3dN8fTM2yM8guh_MdcLNAvy_EOVRlNe6en3XynxEGThaof6SodUZ2c44qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
نصحیت‌جالب‌کریس‌رونالدواسطوره پرتغالی فوتبال جهان به کیلیان امباپه ستاره رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26831" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26830">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aanmSd0Xn0fVgEks7IgbdPHWEOqrcQAIjrerUf_q3QYhZwVdEQVhKbsAxug_N_RrgKc2fQFXeNDzZlAs8nEZKx-mt4Wki2I94VaRSyU8YZ363Xyo45cCqydJaxcK72aVaP2ghnkOQTM1AweU4AWCNy1fuUn3kO0Ic43OnUgIVqNezFGY0-T7DVOWn-HtuSeolvnET7-LUsXolihPxeZw7oaWRJyoa78pnuuxIC92pZ9vmokbeV6PGDjL9FZTeMiJGnMKLrmbHJNvL6CzxVj-aH9-vfQOWa7btXwj2ziG1WFvIVFbRsgIIF9z7vxO1hZJ0L5XH5xq5BAe97Pf9F4WSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26830" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26828">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz__aCb7g8GMUHMkYz4zr6zcapVsVITqtWH_lzLmFdUyBYr9xhoVx2lTDNCbzvc7HwVwbstH9kS6hxihkoanACx0xJHL3DS5g6BUhbVvz30t_RzC9OWQyqhiDzpyhLQB_Oh4NDx_pZrfnC6Yv3hADOm0umG9bfshIc4JWdcROc1IOR7zI6ViigndOV3UxxcuxZjS27VlWYGbPycNNL0snZi2HaKlupEAdM4D6TTlpo_qw-S_pibMA_yzWtVJYD-zsBrZ1_7eg0em-pf7rbLa8JZ50FnKQ3utcTnc1DFHoI_vvGEPo2AeCExH8r9vB0qhi2_Jy8BeHsYNHdQ0Umricg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مصاحبه‌احساسی همسر انزو فرناندز ستاره چلسی:
تو 16 سالگی باانزو آشنا شدم و بعد یکی دو سال قرارگذاشتن باهمو شروع کردیم، وقتی که دیگه باهم بودیم.تویه‌خونه کوچیک که ایجنتش کرایه مارو میداد زندگی می‌کردیم؛ وقتی دخترمون به دنیا اومد ماهنوز اونقدردرآمد نداشتیم و براش‌ لباس‌های دست دوم میخریدیم صبحامیرفتیم‌ایستگاه اتوبوس و اون میرفت تمرینش منم گاهی وقتا پیاده تا سرکار خودم میرفتم. ماخیلی‌تو اون‌دوران سختی کشیدیم و گاهی وقتاغذاواسه‌خوردن کم‌می‌آوردیم ولی تلاش هممون بود که به اینجا رسیدیم‌. روزی که انزو خواست مارو ترک کنه بهش گفتم به یاد بیار چقدر سختی کشیدیم باهم الان‌که‌وضعمون خوب شدع زندگیمون رو خراب نکن که خوشبختانه‌خرابش‌نکرد و باهم‌زندگی میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26828" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26827">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAoQ7JBjjoXqDGGuI7J9SGAqaG_vp2DUrk69GH6T8HOsDws98hLg-9oFxoZfmoWKFx1xbG-VQ7ZmF31gOsywT_XO5Eze6q7Mwt45vWtmRosp9FAIjCBJZ5y6ZSf90zSX4mzwal_zRpPzVR6K8MJYl6oGSDLNIbdWBnjY0zJa--82JHf70wCevj57ZJP5z7s8u6kbWsdc8ocnCofY5il1S-onPrCM8VBTyrquaBhB72I5vf338aG979G0ZfDQynGaNsfIpgn6xPvubiOhpPGpzcjRZ7zAYCE9QqoiQ_Xr66Y_mqXpjOjFRtRxq6iqXznCBzVBOtBHCRso1SznzlcuPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26827" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26826">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=cSRWRfttVR7P4gQeMayyXe4aQcQ2moDEVREtNvcA5vbzXLjZU_05lWXjz0-mE2opKchexyV_vSbmz03t3h0bUcQeCSO8dgtzQPhNC-6cNeS17PQBgIL6xTjQ1H0Z1Di4V_WkFDp4weXPievDop0-xghrradRLo3VrGiq7bfbszJRsSUXUJ54eDWuOAhLEwSMbuWzSMQ7-H8er3emJjYEKSKmvZTYnCunhd3_1pib9ZwWJddsPiZdK3XeKdobtG_UsS03G7iBQrCSgIOEPf-L1T0U8wQxMu9qF7gAH35ZizyhYw_80_XjJCM6O9yB4CG6L8k1BuKYaa2eLJmmARgofQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=cSRWRfttVR7P4gQeMayyXe4aQcQ2moDEVREtNvcA5vbzXLjZU_05lWXjz0-mE2opKchexyV_vSbmz03t3h0bUcQeCSO8dgtzQPhNC-6cNeS17PQBgIL6xTjQ1H0Z1Di4V_WkFDp4weXPievDop0-xghrradRLo3VrGiq7bfbszJRsSUXUJ54eDWuOAhLEwSMbuWzSMQ7-H8er3emJjYEKSKmvZTYnCunhd3_1pib9ZwWJddsPiZdK3XeKdobtG_UsS03G7iBQrCSgIOEPf-L1T0U8wQxMu9qF7gAH35ZizyhYw_80_XjJCM6O9yB4CG6L8k1BuKYaa2eLJmmARgofQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های حامد حدادی اسطوره‌بسکتبال ایران درباره علی آقا دایی بهترین ورزشکار تاریخ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26826" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26825">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN8GUTxw0mTr_OUogyUfCqj3jl6nDmTfCvMTi0_PHxVvWs2m8UFVgPyAVhYh1BaUYAhZyZMzv6vjsOIiIn7-ML9oquwgZXqmnnIR54L9gOZZ6DS00Ie_M_nfjv_FAcMwxudbn6QnVUEvedFlPmahclG4HkuDP7t3i2AF_52fbfrjtW9jtFsaLUJV4wQEcZt_13WZqiP8gtrovBRMXeLF33G0xZBRhKc3sGBNaWgqTj_CyfVxko9WDONC-8XFLhJoX7Ur_z0ts91nPgfG758UMh47k5rSfYvowIsu4XqIu0kOhkQllWLuKQgIX7NvEndUIATlRt2ne8upxMdXfbMoMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26825" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26824">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=bv3z76CDDWC27bWbMqDv1W7ksRmxqrIdR61a9GqlLXx9iZlZtT8fX7aqN59o2eEPE1Bt1LvAatBbfrNIYzu_enpAgozsiOnI7PmVc34J2qjMhcr4Dodn54ZjXCB825rVdSlb-A4wBxfifL1pOog8abjBg2oGefhEFq6PmlQgF7f5yy7QP9cEYvkmF5mhRsxzIXbv1x0zZudMcYkyRxsL7WBlcy8O8p3EmfBAQWroUQAhUa52RX0KUUA88XuQ_jdkejjhQI0LlyJyQrp9Y42bO91nb2Q4cWLlg73rehWKGhr2rtahAwnVZ4meKnE3iAC_8YxGgRNmqU2Mfu2-6euyQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=bv3z76CDDWC27bWbMqDv1W7ksRmxqrIdR61a9GqlLXx9iZlZtT8fX7aqN59o2eEPE1Bt1LvAatBbfrNIYzu_enpAgozsiOnI7PmVc34J2qjMhcr4Dodn54ZjXCB825rVdSlb-A4wBxfifL1pOog8abjBg2oGefhEFq6PmlQgF7f5yy7QP9cEYvkmF5mhRsxzIXbv1x0zZudMcYkyRxsL7WBlcy8O8p3EmfBAQWroUQAhUa52RX0KUUA88XuQ_jdkejjhQI0LlyJyQrp9Y42bO91nb2Q4cWLlg73rehWKGhr2rtahAwnVZ4meKnE3iAC_8YxGgRNmqU2Mfu2-6euyQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26824" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26823">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUwBuae8oCZU-UGTk0z-0tpXVHTJPyFFOIXrbJIVarH-46bGFVhtBgmMLnAJiHoaPXqq4FsSDpcCFg7xltttzCZ4FXjbv6_l79MmwYy30REWQFcJvxAf3tLR9kyBohFtlrciJT8LRroWViR_p2YX1hPE7XlK9pffkes1_drIxkLdMhbUpqGUDIEPJ0azsZi7AU-ptHUPpheE3xfEBhcEia6jlk0_o1QugrlQvNdAJpyzsOzK9Xk-WCJ0kpqBZGydgsPra2QVb0L3LV4h33shpcCpFSFI-5jVH1T_1rb4SMVHG6KWiWY7I19KJDisvw9nNiNtNShtaKXxPxgLHTLobg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدئوی جدید یامال و دوست دخترش؛ یامال: اگه یه دختر جذاب‌تر و خوشگل‌تر از این پیدا کردید من ابروهامو میزنم. پارتنر من از همه خوشکل تره:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26823" target="_blank">📅 16:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26822">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKlrlLdfScjAkwir7pSvgREhw33Q45nsgT1NDSqwMlLRD1jGm16u_IHdacIUdRAz4MVRAhtOZpbpcJhne5F9HVCY91Vb6T1kxmIDvFy3g8MAJ2dv_j4m4F-TxyYAh3WDqDp2Oo6CnXcgJi0jU59BNRarBQRelF01VQ5n6K5g_VV2Wg0Wi1xx-u5OsFjtK_OsXD0RSfAleHszcQJMemENe17v4lCnCCFHsws4Owm9eUuVLHqr9dY5PE5HMPLG8qzhrf1hJQXmLZD1RJU2vNdzfvgOo-2w7aIvCwNv0Vr95Ass5DU6gjLXf0qfTmKqbb1WabmdOU2vnpq16bZl2zS20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26822" target="_blank">📅 16:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26821">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=FAH3JpcdyjfosxgP4tWZg0f3irK2DB-_Ef8Qqg5a5TKHaucusjQJqI0i7IHeotgwpa5kCYXhwXnzf4eS5349w6jGhwf_z0a8zv9PRk7lvCU9gVG7afbUPTBr5710Upcm0wC8rOYabFZYLb0G6amthQciR71mGT0SVGIVFqtPB9En_bqloYKb00X_jSZCb9PWJiQgsJPH9X1-9cFfdDe05DTwm-RDrKuEw7JjQHXi5xSzRfSy_tnpEvky8o-ePYB6baAoVZqpgBIyFdFO-yXnKgTdoJxMblH_9UE6JPvAjPXmZfJyVPK3oTkTiiR3VoKAVupja9z7q3Z8T24L6Ju3PRuZ_9QQpl2cVtbpkQGkgbykVKc4-GD4KrzQc31Qp9sIrGwDg11gQTkfXC8SghSK6j6KTzF4F_OI7JDHhUsgeys7Rpvnh3RLxEMy0fjPI99qYm8eHlkeqnwqvvJW_sc5RPQ0Y4vCf4c6KixKiygEOqGXzSOCLGw_Qx-5roy2lG4FXtSJicfg6l6ne0STYGNUbFNlw1kRFUzrRAmaHpBT23DbPqJMy0wl2D_s-omXlAN922v-i17x_MEI1pxuMRSPiqbIZ0aCKsx6cC7Do-Bb3mTiNZvs3lJIl6msyDxnumsMEPCWFvTwgbuEVcfEgHcWBGJVtXozO38D9Iwmt5p863Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=FAH3JpcdyjfosxgP4tWZg0f3irK2DB-_Ef8Qqg5a5TKHaucusjQJqI0i7IHeotgwpa5kCYXhwXnzf4eS5349w6jGhwf_z0a8zv9PRk7lvCU9gVG7afbUPTBr5710Upcm0wC8rOYabFZYLb0G6amthQciR71mGT0SVGIVFqtPB9En_bqloYKb00X_jSZCb9PWJiQgsJPH9X1-9cFfdDe05DTwm-RDrKuEw7JjQHXi5xSzRfSy_tnpEvky8o-ePYB6baAoVZqpgBIyFdFO-yXnKgTdoJxMblH_9UE6JPvAjPXmZfJyVPK3oTkTiiR3VoKAVupja9z7q3Z8T24L6Ju3PRuZ_9QQpl2cVtbpkQGkgbykVKc4-GD4KrzQc31Qp9sIrGwDg11gQTkfXC8SghSK6j6KTzF4F_OI7JDHhUsgeys7Rpvnh3RLxEMy0fjPI99qYm8eHlkeqnwqvvJW_sc5RPQ0Y4vCf4c6KixKiygEOqGXzSOCLGw_Qx-5roy2lG4FXtSJicfg6l6ne0STYGNUbFNlw1kRFUzrRAmaHpBT23DbPqJMy0wl2D_s-omXlAN922v-i17x_MEI1pxuMRSPiqbIZ0aCKsx6cC7Do-Bb3mTiNZvs3lJIl6msyDxnumsMEPCWFvTwgbuEVcfEgHcWBGJVtXozO38D9Iwmt5p863Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26821" target="_blank">📅 15:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26820">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=X9HrGUQ_Wo1PC5_Xqoa3CtsMBE5CkVMlncKuT4dU4VeSFip1mC6v8Tz4_EhbKpBSXlC5EQBAl_wzFcMB9Pf5jZD-A3reHe-riepT-8kDXEllYiCUbGzC-GMHa2_GS_MPiV33g58-bRy8u0A-n727_wGv0-gX-8FbMpi4AeYL8nyCci-Jqzonhr6MAtUJoLpTe5T_9rQWfliIc7h9T2bOnjd4Msk2GCNlR4i6DTWIAaiJsewHWMxK3A6W4MRfcKd_HVXPFHq7TlDFp5a2cHtCt07Y9vaHNzuOWpCRzFFqXJyWyQ-sDEsH1d9UvwQaMhMxEKMt13Jo0z1p5RQYkOSiLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=X9HrGUQ_Wo1PC5_Xqoa3CtsMBE5CkVMlncKuT4dU4VeSFip1mC6v8Tz4_EhbKpBSXlC5EQBAl_wzFcMB9Pf5jZD-A3reHe-riepT-8kDXEllYiCUbGzC-GMHa2_GS_MPiV33g58-bRy8u0A-n727_wGv0-gX-8FbMpi4AeYL8nyCci-Jqzonhr6MAtUJoLpTe5T_9rQWfliIc7h9T2bOnjd4Msk2GCNlR4i6DTWIAaiJsewHWMxK3A6W4MRfcKd_HVXPFHq7TlDFp5a2cHtCt07Y9vaHNzuOWpCRzFFqXJyWyQ-sDEsH1d9UvwQaMhMxEKMt13Jo0z1p5RQYkOSiLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارگردانیکه‌سال‌هابهمون‌رکب زد؛
ویدیویی که از گواردیولا درمجازی‌وایرال شده بود، طوری تدوین شده‌بود که انگاراوروی‌نیمکت برای یک صندلی خالی در حال توضیح دادن تاکتیک‌هاست و همین موضوع سوژه کاربران شد. اما تصاویر کامل نشان داد ماجرا کاملاً متفاوت بوده؛ پپ در واقع مشغول صحبت با اعضای کادر فنی تیم خود بوده و کات دوربین باعث شده چنین برداشت اشتباهی شکل بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26820" target="_blank">📅 15:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26819">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h78a2wuoy-MOAuB93XIdljue70jPPpt6G2U3IRM8F4PvDIJZH48gzdEcnW2NtkLfxpjQGqohVGdVH5sbJXMoKUy7duvI7f4Pg731ZSI56w-XlbrOpI4voVNlfH43gdghdXBsRGbzwJgv_LLs5-E0I0pg0lOpIQ9grZdcmB0XJpjPAnXdELgrdT6IEFh59k8y5Ffk3FQpFSPrREMZK_qCqeDBZYL-XxqMTPluMe2HUmN8tODLA7JaGpi477mtZlL7GWuzH5IgChHr0fQ7kyJIj-YDxS1lGXIwT7Vb63lz2QYpSH3JE_7k9kvz6uOTChF7OOMKVq1vx4uUVWsn_r9XCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26819" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26818">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kkv6ki9akGCB5PtQjtEMFM23Wh1ApTTO-K0Tj6eGPbp9fCNxrms_dofwgJQHwZ7zwQ4daAiAQbjh4Z66qXAQ3_EHSZ236l2w_nn29fXMsyqBNfaGZeHfpfR06A7uODpxNv7-ZB8-BrHBcKAKy6zuSaPuAccKg0llniFjLCnmDdu5NwA8FXVSHHzeOvQ4O9_nRSAPB1kcO0ZdJwz6LL1vi8vxw9pS9sN96O8QEX3D_IwSQxKhLbzVkwAAhw-pPAI49BWdTj9ZmTcQERTSub70PcRO2CdzXGX7GdTh20i3EGQYnkaDChMO6iyVis3-rpcUJ2TX1gJvCunFmce3LeD2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26818" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26817">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rviBuRN7OJzHdSB_cXzw-jeYZeC255DwHTMLClGq_oKDQ3XdL8Lqm7D2yxG6hC6UolzLAIuOLWTzN4MnZ7zywNOhy1WaaGzzEFTEqeHnYrOyPlwKzVw-8DR9bYVB72F0Tz0gbmOVNVjr5-MyJzIWzO-fSgVjwBvtrb4Jqrci9V6m6gQ143oy-iR062rziXxrYLEYCrahNQfZqgM5uePugYeJzb56M90EoWDUvuKjceBgCiQWC2RfeGVL5T0V5wb_JGOCFuaR6awf4UtU8IFtSLx1jBO26ARV2vL04rj3GwEybSmxaBbI6nZlwyH_D_bqi7xCQReuYQO6Z9pm5zddvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه نفر راموس و پارادس روبه‌مبارزه دعوت کرده راموس انگار بدش نیومده و پست رو لایک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26817" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26816">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFxJxyw_avIQhmKQPHTuTauwrqhpSaDjbazUUaeetp_PB8beJGXF4QEhNTzU7GRV9hWZVILP1QPci7WhdPzTQi6U02Is1Xi6_-Og16sF-rW1QBFl1RRHFL-aciXW1Uq7j8yeJneNV4A0Irbq3JyhsVdwciioTBrgj0tzIu2y05K0Ye5_4d7_N_TbxzyH2INhEo0hrb5O1AHVCD4jGyg1HNk5qjHwZMfIyBb6IpQxdcUOS-YPjVUaGEXOdCAc_jZeZKdp-Wp_0nNbOWo_Y4hUJAhYlwXjx-re3wHLKZ8o9xs1a_DC6O5wrOKE07QtVIETIoT67DInH2bu1vtDwafaQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26816" target="_blank">📅 13:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26815">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i128YMOCG6ntNWy_8rgvfIgyJ8AlKXwUQD7tSwxXx20IP9VlcL2pSuReh91ciAYWWZdnxDvNVIu6UOUmbufdmRN7qjw34jspbxTWnU7tVn6cDJrOwxjPn4HAF9xW8d9enNAb9UfrIBHvnGqZXxRd3JVcnxyQxwAy7QD23HMioHzF1k3lY5QV6hhbUlaGGhQPQUxx9YfBCmN0kV-I8MDsmEL0zlr8NtKwygcCXZf0tOVgislP0oE-1nWQ8-RCC-2JTg1sglCUW3JRXGSQxOncpkpag375SPBgnfeyX0k9t5y_xOEW764F8uNi3uzcnMBhhr-gJcnWkUMOO-IdSXGhVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛روزبه‌چشمی‌کاپیتان‌استقلال ساعتی قبل قرارداد خود را به‌مدت‌یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26815" target="_blank">📅 13:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26814">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQf61Hplhnh8gJujPjMQvowrFdCxfupBbSvMvuDNvPeePxv8SCxhgz2LR-rNAiar76_L0SjysAUjCzvWDOkl8WQIGj7ixDUzswna-lc-8PCwJtoI7NjGVl4hAz1sV41JGerNGpOyuFQWVpj29sKgTw4sgQu2SkZadHzAsJx5guYyrkfJr8khlcxRyp_4508tIEWJlLonrzleuPuPdm3nQqJiP_4Wc1Vu--bzjJYyJ1yPPvfVNaFg9GuXrn6qdXztg_Gmw5EA6DlAq5oR5K0tTn8W4TrwaU3OOEBsROp9wxWE_dwXOtSRm1tzYeLjpIRmz1z0Z0VAyLtAI8pxT7p3EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26814" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26813">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kP39cE9tB2OjvDKijjdyF85k9gm9CBMkeeyf3qigdqwdoyOSmoeaqUPNDJPLJb3JM07mb53d2Gphe2MIIyyJ3m8bScWDy0O8cHGahRVMizB7UX1LCVda9IMTcSnrskWuTLeAk61QMvPTP5rhr8vqxhWKsjJOKHp0o2sXLXyhDsWtRq45M3nsH0fWxUlhcgb52ed7gbsBXZkGAWE5lE3nuHhgq6rGQxbzTPwEAmh8zvvuD0M4HgOZcdzkVYBNdqaoP5s9wPAeNeS6cs1l89VREpzbcNptq08awx8J60sMIr9ewjj1rhWNQntSnuNTvFjNqKaQe4We_H1Jyx-eqlwP2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26813" target="_blank">📅 13:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26812">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcR75f4HpiCOTDtj39NLb3WRN5-dTCReJ04f7xb2Gw7J0LxDBIWiyByRpXENkga_b4ZJVg5ZanXpWYfwhvCHLYpQCfqEJiSFu1E560dyA7BNEF32qQZtcn6OrB-Rt-il03Qi43ZcNxgMjokNnmhQmVdg1pQEz-2As6UuaooeFIt7O0Yx6pmnAkukRyHyXgffygZuo-Dmm37eyOeqyagfBQCs6Iimy38gx_kGG19utKxdcUcA2zMfDBcgq4GEsiIrCFRp2-9_1YDaTX2LVeLTyu-bnZ-uEyHIAP_mfvZyE265W7PUCHFjZoeGdL5QJajM6y-Bh55pDvhHl3Q9KXvMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
"بچه"بالاخره‌کارخودش‌روکرد؛ باشگاه پیکان از عقد قرارداد با جوادنکونام منصرف‌شد و قرارداد یک ساله باساکت‌الهامی سرمربی سابق تراکتور و نساجی امضا کردند. نکونام دو شب پیش با باشگاه پیکان به توافق کامل رسید اما تماس های محمود رضا بابایی باعث شد که قید قرار داد…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26812" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26810">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKoU1amHRIAGaBXW6F1WNeVhAesdc-9PgjT2gSb0kuK6HfCTAR3CohkGAqqDS8brTpOKwBdNuTG_uiGQ33BqGBiI1o8AN6CIMyXxblYAwSZM7mLl6fQ4wd62rOZy19PrYZ-Z2aYs5t_5NYmuGxGPTJHrfU3hbuTOVDziJAvENVorxazw5nmz7aLYbeuVa6ylesKCFAszol1TP2NYuF6D7WL38aY0pfp-Yq9cgy-Q7q-4_8q2XeSbGV6RODvylaAU2z7NrtqgxI9e6fEPXjGWGdOSb-URIzAX_on0SRnHF6e3qmp6Ejs9Qj_NMGGOdhXVJTAjnFa_iKIOpvFHHjv4YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای‌اولیسه‌بازیکن‌بایرن‌مونیخ‌هستن در تعطیلات که ویدیویی ازش وایرال شده؛ به قول خودش اگه رسانه میداشت حسابی دهنشو سرویس میکردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26810" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26809">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwZOOMhUCHNcAepLnHBkhZXFcsO3KEmjYfBHv9gdCqsodmExm-DgC6BSo0s3ziEeSLgOZsyJ39N4sgQaRFjCjygBZtAOmiIsYwa-iR-x85DZ7BA0S5Nraue__xgthU7_udQfeUycLv02wtaCu4RcqZacGTBKLR86t91LTfRJ26CYKzXKwtYktdTDgUxXVQG-F9_HIcFp876ocbw3hRy5D62oqWW_2XSmmYfUKQZS77Ty8kIhd0KHPVJTbX_U3IjCG9kyo6j3Vr0Mvf1Y9bO62noIoG-ZH2hx5c_mLRL3ap1F3KlvVtdn5bxnLo7YMFqiCK96SxtqNEnC8mzQQP3iGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مسعود عبدی مالک‌باشگاه خیبرخرم‌آباد: باشگاه پرسپولیس سه‌بار برای‌جذب مسعود محبی به باشگاه مانامه‌زد و مذاکرات‌خیلی‌خوبی هم داشتیم اما خودِ بازیکن علاقه‌داشت‌لژیونرشود و ماههم به تصمیمش احترام گذاشتیم. محبی راهی روسیه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26809" target="_blank">📅 12:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26808">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2FLsZlXxCBJJjC5dAoVOCk8f4gYDfDvTd6Y6uxOcueuiou7J1BjBVBLDyz_zEbn1AHdFU780KYbVCekw1_5tCF4_Q4PHAQBYwj--V5lwUJ8W6G8tW9cF3KeA-77Qt6JVjA6Itw5O6aFRslz0NwM_oW-OwcOxZTJCtbHKaTOJNRx1OVAeLcE0-yq6dKnCPCMUbQhND3J-0YyPAeXH7ni7aFoYkaLxxLaF1mXox5IodhPOuPwn9eoZETMYc0yY6I9xprT1dDJXU9wleJdGq9BUt7jlQIY5nZuHgpVuKfQGnxshTTOR8XKt8JoBltIkBD7Pajvqi5B6RoPyrcs-dzxLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا:
ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26808" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26807">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=PrRQ-m1v04DmiqKlfyBRMcsC82K2vuBUcc6TSSv9Xurs3yGgasZtVjHNyL-RpIr00mnkOs28Wh-Z0-u4RECx69_j6iNl7_iwABRXL7loup-a9VkgQ6HgN5oMhOaN3tcAdo-rMnofP89kARPW4BGHBevRWSt9oZW8xiB1Xfo5Ua0C2YN1f9BImT6jXRfFfk6pbrU-v0QfYHON35jcBGa346fiAqSryT8-oE7kQwgP5lskMamQU2sximUeHzCSsLydynOxpp04csQR76HENM3FV3S5LH9denQYAaoQqeUaozUeNXtUrhE1_64Gx-2zItnXEKtUK_Zo0HbIRthbpwgqPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=PrRQ-m1v04DmiqKlfyBRMcsC82K2vuBUcc6TSSv9Xurs3yGgasZtVjHNyL-RpIr00mnkOs28Wh-Z0-u4RECx69_j6iNl7_iwABRXL7loup-a9VkgQ6HgN5oMhOaN3tcAdo-rMnofP89kARPW4BGHBevRWSt9oZW8xiB1Xfo5Ua0C2YN1f9BImT6jXRfFfk6pbrU-v0QfYHON35jcBGa346fiAqSryT8-oE7kQwgP5lskMamQU2sximUeHzCSsLydynOxpp04csQR76HENM3FV3S5LH9denQYAaoQqeUaozUeNXtUrhE1_64Gx-2zItnXEKtUK_Zo0HbIRthbpwgqPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26807" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26805">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJBCcENfyrPSnMBegMeR-Gk5go0MG6HFpdNSbPWqLyg6zonZ3qWDBAb0hvnUk8ASxdFzM46WnQ7AEOrbyXYgP5G2_fPLZhQCIMVLBJtyl5rfKbKhFe74HH9qpHju0Oa-ZCM3YbEAmWpyt0aQBbgsmQj6GkwF5-k857G-ylC9-AZ8ycYJUMntBAUg1Ox5zFFCao-4k62H06QdqkfrpiAjxkS-KFan_0pCXlNLAp9GbqcrW5v8G4LV_DKXu-H5EQM4tHHU8kDMYt_vcYeJ3fXjKM_76vpDHCQbb7R-eO4QiVeqtrm1sUuZRwb-qIss-T5lwEvp_w4DKBQ0-8X4vUT5ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا
؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26805" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26804">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjrZ6nDZ4T_oVzIakMvOxB4AkHceN62O9GKaOjWdHFYgTcCZV2E_mtP30lTvj1QIxjjb5CSP_AWWcUQbNTjGNybadJtlHnWUjxvOwk4rKvnuh5d-BX7m7wugiaI07E6SD7kIg8-U6FWtAazt2sTlwX4w9qZPvEPhFEVSdm7Gkjnu7zfYqq8DZxaq4l7C6JQBfkh-QQPx5ZwC4ngjeXXao8BX6hvLqt6SBPxZGaL2vwqFD5kQHii_BhERH_30ReCE3BGG6qi3KH7-T2qlp6tSPYpBRXQ0o-Hj_3tpfW9XwUB33P-FTFXxGN15O8rh_x0yDtcK7A3nLdbehafUFodufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با مخالفت مهدی تارتار؛ باشگاه پرسپولیس با وحید امیری برای‌عقدقرارداد یک ساله بعنوان بازیکن به توافق نرسید و به این بازیکن اعلام شده دیگه در تمرینات سرخپوشان پایتخت حضور پیدا نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26804" target="_blank">📅 11:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26803">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
ویدیوکلاس‌رقص امین حیایی سوپر استار سینما وتلویزیون به‌همراه پسرش در فیلم جدید «استخر»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26803" target="_blank">📅 11:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26802">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSbI25K03vlNwNSNbtyMJF2Rq5x6xlnBoMdqgzJAksYP1fOP3hl-vYKbeNtBTECHQGoNgf0UaMg49ng3UKWhIEropqU5shTy2xfVFwymgIjz26NpcpborUoHJvB3P07UW8j0BWoKqXqd1IYdej2bu_FFcTkLSSB4fV56CH0fXXdojI1vDgfFxEubart-2PmMMCA7hmLin6SIc4LikbRHGek0hddyzplYIJsJAe_IIlz1KSa7c-ZjLLTgYsg1PWHGSx1aCN8ZHieNpFo9HkJt3zdEVAWstPusTonKRTMq1ES2NEzhdMWmk6EN_HTj8VhALnv1jdnvL3e7Zcx7QNw-3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:ظرف 72 ساعت‌آینده‌انتقال رودری کاپیتان تیم‌ملی‌اسپانیا به رئال مادرید نهایی میشود. سران منچستر سیتی تمایل خود را برای فروش این بازیکن با رقم 70 میلیون یورو نشون داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26802" target="_blank">📅 10:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26801">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=M6GyWp7sEvpKyMzHHFQbOMYthsjq4CLsLjJZ0a8d9FI1nHEdGGVn-qE_6CEsJGcVdsvcgVCIN17wQtnybtYtmLvpno5wCXE8LjxuH1eFdTvoWMTMQnEQ6GJ8l4LUs7MOhasHI0cguetLEHD07nQkJ0bXag3UTlHM30HjbTUCK_WBjoJxLfMD710jn3UxsX1frVfqat_9eRFfRPyJWoYOAzMhUhUAUCMy2GQ6fwXw2HacPEm2HUdaGu-3YwL-WHQrxu4gpANxYMG5w8XjX--LbaMLCJ0-s3RyS-5f_tL_Vxm78KHubz9FqeJWjD8wjNQ_WWXxk31n_mv-xB0iSWwSYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=M6GyWp7sEvpKyMzHHFQbOMYthsjq4CLsLjJZ0a8d9FI1nHEdGGVn-qE_6CEsJGcVdsvcgVCIN17wQtnybtYtmLvpno5wCXE8LjxuH1eFdTvoWMTMQnEQ6GJ8l4LUs7MOhasHI0cguetLEHD07nQkJ0bXag3UTlHM30HjbTUCK_WBjoJxLfMD710jn3UxsX1frVfqat_9eRFfRPyJWoYOAzMhUhUAUCMy2GQ6fwXw2HacPEm2HUdaGu-3YwL-WHQrxu4gpANxYMG5w8XjX--LbaMLCJ0-s3RyS-5f_tL_Vxm78KHubz9FqeJWjD8wjNQ_WWXxk31n_mv-xB0iSWwSYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته اونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26801" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26800">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇧🇷
نیمارجونیور ستاره برزیلی سانتوس شب گذشته به این شکل برای دختر دومش جشن تولد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26800" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26799">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M79DkBwEnYPH5Q_LJJDTmPpb9RkNIdHzxspwaeExc4YGlBqLRlkcasP-KgPdFvCdhNB7OX424vvSAb1U9TO73w9_H5DXd59eMgQIhxmIH1dVBSR5_dinaEzzTaQE_Fuc_TXiqzvoi2eJi1zlkKxvKegmOTF1idnyt3oSPtGpOFiNbxKF5GxJpIkbh-ywyLHNt-x9CLKLJVMc_2s8VflpOgD9smOrGfhDbS2Qtc0uw3njKaAnvs-KjLsBmoTRHW6AOvv7bgnw62fbEc3t76LbOxcThkjUhf5E344ylve2Pqaqt_aAxslIb6Y3herxGAk2tOcpHg5vEQLXVxlUA2LcLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26799" target="_blank">📅 09:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26798">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e__QpgMrqcBuekH68oAvHXXEFJf1ZVM4vlWf8khlHWTHA_zJey2xyRLBmPJj7p2mKlNrde8svW9ISugTZxN9XYFeSk-ZI9bucEdSf0pDcKgWi2I1Kync4KNr39KOXaDO2YakFVq_aYRchnO2uyEndmBDZtepDkj5Dj3JhCIl7fqFBELPTdUQ_KNu3A-sTpbmMlKRlJaEIaynIWcR-Gup0Jqsz_hJpu_glF2_Uv4dqVuXKNgUzNsgL2lnbLOjPlarA6hpiv1cXrKPHS18bA6AK5UAA2IelDSEMnIetqhjDXvLsmsl6tpeqncbTO4PHBcVPxujoMXqheqeQ2jjJBB1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار های‌ دیروز؛
شکست دورتموند مقابل تیم ژاپنی و برد سانتوس در حضور یک نیمه‌ایِ نیمار
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26798" target="_blank">📅 08:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26797">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jChgCRXinY5y4j79ta5IMwHVy64WRC82J1wcBhefMQTYeM2w8HykAY0IpFwiOh-NFYcqpQffIU88vFm-244rzawV-KyBKNZ2OV7NNJ864bwgdNrjQjFBhEP9zLbMRx6jBfIGMUUDaMIAqfDuO-6M2JjuGb9JeZv8syCwHtL-MPIrTG21s7iQ-G3Nai-n2Vw6coO0l0kR9keGDG7GpYdQJ0OFWL7V9AABDK9QgC9NKrTpWsUETvmOEX9LTPGn135oJWZZEE0kPc66jkAa5Fya654eBhFKj3ybyYq7kqzyK_FfHL-xh0qAw7nhC8y7zUyMSaPGszmGHNZs_DgFErglhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26797" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26795">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=LusqKOcfpY0gRD91z-rx8k3znUxvvhK0S_Lm2K0Ofn0ixjn86VnHmeNpM2ZSZup485SQ3QN4LA8gGkYNvmk1-IXVgtvcPcOEd1XuzUPLdSfb9b1i0Y9M1mwcul8w9GuzSXoRDopSp8qO4GnAq3SxLaVy56VJbIQSHZlyzH7NmvjQMeVZYfgcyJV8Hm9WSHrCg0uD88nkB9Urwch0e02q66oge9jvL0Rfbv-dIsmDMQ1d21X-9_jXJlEYFROs0-9s-G2q3igVjy2djiC6ySoWhbR7EdLjQ3r6S_tpgbDWeSOPCyoH-D3FLYbgU94fHN-bHe1v9yVh1RA9Q8FaTuKWfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=LusqKOcfpY0gRD91z-rx8k3znUxvvhK0S_Lm2K0Ofn0ixjn86VnHmeNpM2ZSZup485SQ3QN4LA8gGkYNvmk1-IXVgtvcPcOEd1XuzUPLdSfb9b1i0Y9M1mwcul8w9GuzSXoRDopSp8qO4GnAq3SxLaVy56VJbIQSHZlyzH7NmvjQMeVZYfgcyJV8Hm9WSHrCg0uD88nkB9Urwch0e02q66oge9jvL0Rfbv-dIsmDMQ1d21X-9_jXJlEYFROs0-9s-G2q3igVjy2djiC6ySoWhbR7EdLjQ3r6S_tpgbDWeSOPCyoH-D3FLYbgU94fHN-bHe1v9yVh1RA9Q8FaTuKWfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوگل خاطره‌ انگیز از ارسلان مطهری و وریا غفوری به پرسپولیس و استقلال در زمان حضور در نفت؛ هر دو گل هم در دقایق پایانی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26795" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26792">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHHWxx6ZcGmKHdbAt-pNr3NIjAk6P_P3Q_BC8G1s57QBUCyHW-rXMy3k2g8DH7IR24MERWuPoQIieL2wfKzoGHPReZHgN5YyuaxxMldXufDBUmiHfxfNTRypeMohoXvi1YbbLnTRFXbhPTh1mNeJbK9g141kLQBG5mJkhscTp_2ftGjezLJPQox50UpVKmHIPi-XVWHSU0XRTIO7h9RmGgwX4Bu3WUbOpkN4nIET35QZtThjTi1d6c5MK_r1tojMP4zjuVl4_YmbTL1AdFICY6PM90OWQJjw_7fatKlrRSfoPUtiRt7TMcbpf6j3gQM_h7aw0ZYc5zeOM_kCYm2a8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستین تیو:
وقتی بچه‌دارشدم، همه برام کادو آوردن بجز مسی. اون‌بهم‌گفت‌که کادوی منو تو زمین مسابقه‌بهم‌میده. کریستین‌تیو توی بازی مقابل لوانته هتریک کرد و هر سه پاس گلش رو لئو مسی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26792" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26791">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIJ83mkhf85Td6PB-pqK-1JEzOOzTctD1FbhMeMFj58zq8C1iKOYzCQaFBk1cl1xRVSuK445sQBMlW_BT_XEqcprA26uJmkicLzPN2wmPc-DaQFTP_2Q-um_B_qDUfOdei1LJIMaJjETfO1kIp_sHE2rmvfOuruVKS9q8vHSmc5U2PQHHsbTnejg2pf8nJWv_ixy5en02s_AwUhRsG5OyRVsNQJIgAQCo_pQaMlu5ABTqKi_ql3LJGG4SaEBN3E6eJvCUF6ddyrvZ3m_vH8AOggPM29ZrUjemC4sy5SiHvVIoZsHT3J0sQNsKhNMRFkLKZ6pz98Savyqe4YXMWiosA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26791" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26788">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QkB5dU4mMXMk_bHEmP3hG_Bp-u8ZGBixVXMPWN-eK4TUW0istS_-uLEJRzDuO3FDHeKK4D5Z8JD9PKo8shhg0LfBPf1iKvpkOQ0HKP39boCDbovHNf-y5UXEKdWquAPVB_bAUPdOckFLhkd_UfoxQzOrpBlrCnkghhaS3DavJ2xAOYQNnOAG91GeB5pzOXRezhlhvhtbQn0nibMx1OvYE2GgMdxfRVrh-ezWgerIm7QPwh8QE2uZYkA0kHmFuhcjd0uRcYqC8CPW86yDoTY_l0Qte7EfwvK0NOqKpKpFrKHtjenmt7RfLMaH6fsytPocaV66-CdF1kn1-ZuxXC3GBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CBY5p4gyq2LBxPsTZvzN58lOaVnXCcYJMWeR4nKUW33wEyZTysg767sqjj9fi370JBk2DX1jx2-0TEqu-xEg3Qusd61-M9JskxzcQ6Uk8HqR8S5UvmRa4Y0VGLsnCngrz6DLnqOru2_aBUGH_oMcIoOk4aefrkcDRr1C8U_27cFU8m1z7X6QESUWRrOSArCXz3PaagEEsRkoHjI24Q8xV94J1Y20p0DYFW6tQiQqudORSQO9jVnaFX15aUqHxt4wvf8BovbohrMs0wQ1C_yz8KuWarsr6mqvO8ow7v_P7IBk9YW_DSjC3WhDZHCayql77H16G9NgCPvGcCwrBGcS5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26788" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26787">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=adJRFb9q5WP46HcvYFuFOdbCwDSV_c0QLD-hi-nb6t_8KVEKRBXp8_BvvvjQ0S7RsnSsME9P4HbS3e_0psU38WHRyNgy67XN5-3gtMxNpxtTEeCNsFlZtjleW9iee1rf09A-RU8buNCIk2qNUNoYXWuZOPjBWFcYWTwegQQ8OREt-hyUe8CnlaK7nl5rJAJeXNlMXC3hGdNXasd25A5BtRqjh4BmXW49z4MyKFHzup1-YKlHJ-B6RRihuFE1PssCfN0PYmbU8Kl1C-7XR2siraXeyEGCCs77a5nB765US2zck7JuVaWnTNTY9WXsrXuaffLlmpdXXILnOVc2wUc2qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=adJRFb9q5WP46HcvYFuFOdbCwDSV_c0QLD-hi-nb6t_8KVEKRBXp8_BvvvjQ0S7RsnSsME9P4HbS3e_0psU38WHRyNgy67XN5-3gtMxNpxtTEeCNsFlZtjleW9iee1rf09A-RU8buNCIk2qNUNoYXWuZOPjBWFcYWTwegQQ8OREt-hyUe8CnlaK7nl5rJAJeXNlMXC3hGdNXasd25A5BtRqjh4BmXW49z4MyKFHzup1-YKlHJ-B6RRihuFE1PssCfN0PYmbU8Kl1C-7XR2siraXeyEGCCs77a5nB765US2zck7JuVaWnTNTY9WXsrXuaffLlmpdXXILnOVc2wUc2qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛عصبانیت‌آزیتاحاجیان‌ازسلفی‌بگیران در حاشیه مراسم ختم زنده‌ یاد اکبر عبدی؛ مگه عروسی اومدین؟ که لباس‌های سفید پوشیدین و دارین سلفی میگیرین؟ خجالت بکشید بابا. مثلا الگو هستین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26787" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26786">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=Kje47WH9ggkEqJXoo3bBRMZ79Mm3_mHKgetKH70ScJ4UFD2FYXCf8Do1BfOwejxMwDG2Ad2lADO2LDRK8U7goB57ol6n1X-T5OTRrtV05f88LjvBnQeWmhl7mS05I5GAzyHSfTaE5W3jR5L6ftWCBf9bJiH8xXrTJKH8IesfTVYeAv7kT1nxhuK_0k7reBLafA9hCqrhKIfRQyXQnTJykNTzHMiFEsuAMgc5Mohj--mRGE-e7gF0_OWQa-Tzvq9RDlUFbzPruCquHKjXWxGuW3IlXJk_aacs43CS0lRmIfq4St-A2Ushs-K7ooYHrEY7oGpBaai7gAA1RyPHL0AleA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=Kje47WH9ggkEqJXoo3bBRMZ79Mm3_mHKgetKH70ScJ4UFD2FYXCf8Do1BfOwejxMwDG2Ad2lADO2LDRK8U7goB57ol6n1X-T5OTRrtV05f88LjvBnQeWmhl7mS05I5GAzyHSfTaE5W3jR5L6ftWCBf9bJiH8xXrTJKH8IesfTVYeAv7kT1nxhuK_0k7reBLafA9hCqrhKIfRQyXQnTJykNTzHMiFEsuAMgc5Mohj--mRGE-e7gF0_OWQa-Tzvq9RDlUFbzPruCquHKjXWxGuW3IlXJk_aacs43CS0lRmIfq4St-A2Ushs-K7ooYHrEY7oGpBaai7gAA1RyPHL0AleA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26786" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26785">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNB3CDLHJdz-zQ3s0atkP5_yxS5tz47TXooPWRNanyOraL2mVMiq8RABJnlz8_h_LKmsSbrtfcZ0QOvExwJrl9txfvggo_mwrpR0vL8Am_tFmqNcGft1M3iyPzPp8xh7ofPx5szfNReq_iunLbuMj2_b1L6QwRi3i-psKLbYN48DkODkWG1aZB8yqakxl6VbQnWvB01Xjd1YJQIrvyyq6fG_r1ubM7hsj-_YQhjFOf-6Q_Zp3E1QExbIdDXqZ1bY-d5lCzwrClRp3yYhbG0tlrRLYccl2VqY9UDng6HkSigEarOJIs54KaEWdzdtiCDi64YSDOGotmf9Y3-S5ai29g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26785" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26784">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAII90hB0Rp87TAJfzZ3Ead-aCNu0e-3rxQrIzgTynM_YbPlHr232p9jeslwv-xQggaPswdmDn86JmXDSWganxQWMoXatNJfYS8og5_RbBuuFHMFJ9etapPAjXQcgwbVtk1-4ltAdF7A6ovAhUDkTev3rObdGQBG8sHVlahTmHVCAlGj9b1CnDKwXJOyoeFPCEm5KPYknEJvPHJwpEXbJRRXyLxPI-vyGEiiSP4_2-soy8AyTXG6tv1w6aVoZFCxszq5TeEafltDD3bTYk7ClnaSec1VcA17AvZxQeMQLlGhGEWGBlPgCflQMm5Sk_MYaUJjwT-teqcUFobVm7bQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛
مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26784" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26783">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787ac45905.mp4?token=kh2NQn1cEuQPzrgzTw8Pob3by2LDFLknmFNMKsDDRCDeoLhvLyVaAt5J2vn4xmgiv81g1y3Gf7D2l3bBloYC0innGh7I_AF95tyQ1QtKwtCaENemJcJZ-ByxDI88nphCsduG91EnHvv8f4f-LoM-dAwF9p9Xn7UNdmJXaY0Ee1ssSW4PS-_uhJuqi1YUjjmxgzlGiD3d4zaVEDnAhBkxAW5526shTjKYAYEtm40q3K39qoYzbZITwBYaHdeSe_FThE_MdZgB2dFMHor1Lr0nwrfhiRwrSJ_Jhp9RV-lv0Do9Q0ZNt-tR0uMVCbxH2GC3Wkn8qQtBpLRlzKZEqvOTbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787ac45905.mp4?token=kh2NQn1cEuQPzrgzTw8Pob3by2LDFLknmFNMKsDDRCDeoLhvLyVaAt5J2vn4xmgiv81g1y3Gf7D2l3bBloYC0innGh7I_AF95tyQ1QtKwtCaENemJcJZ-ByxDI88nphCsduG91EnHvv8f4f-LoM-dAwF9p9Xn7UNdmJXaY0Ee1ssSW4PS-_uhJuqi1YUjjmxgzlGiD3d4zaVEDnAhBkxAW5526shTjKYAYEtm40q3K39qoYzbZITwBYaHdeSe_FThE_MdZgB2dFMHor1Lr0nwrfhiRwrSJ_Jhp9RV-lv0Do9Q0ZNt-tR0uMVCbxH2GC3Wkn8qQtBpLRlzKZEqvOTbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ازاین‌گفتگوی تاریخی بچه‌های غلامرضا عنایتی با عادل فردوسی پور که عنایتی به بچه‌هاش گفته قبلا مربی بارسا بودم؛ عادل از خنده غش کرد.
امشب غلام رضا عنایتی با عقد قرار دادی یک ساله رسما سرمربی تیم لیگ یکی پالایش بندر عباس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26783" target="_blank">📅 23:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26782">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=Dg4ktBHS5syxNFPVX12598OfRAfhUAtxkhjwStpDNXj5ki_6TdKpVD6ZWuFJ4g0cXoU_1PcivQeTpHbyBDavGSEDUFKdxMP1Xo4ofYbTbnexK0PPWJB0yGM8yyO95DrC5YfCvNLOAnojMBAJr0Oa4sa36-lEf1v_tm7ww5tJF6zWPU4It6XTzOcCBtigRKwMz9WS9dXPVWDHLcwBZfvIxXTdZ2KHEWTGNl4zJfMvmyrDoU26psc32tujmUX7IWzc5AoF72JKxRCspGCRJTGAMPWN4SIqLCzRASL0RvcyaS7xTbHevlEbVJg6GPR_eHazr_c5fJWk42KG-Hfofv-QIhIsN1A6NUsfRAzHYSM9dov_-CUTXrTndV76eTduFu1nA1CPi6J2rsjcFPo2pC8sn0wT_lRXgyxb7rJQQ8Bd_QQSxYpoMN69bQ6ty-0T_SdiK6haxBwAoTOsJieXrNN1gVFohmBGEz2VE-gbphBweou8z1S-t9NnZDWw0k_7MR-0OBz9DdTBRUJEyTlT5ZTTEKpaWV4rm4nKdhHgOZXKQg5GOHh5A_iBLqemsT3ybLrJRY2DhMeCH5sCXBiQXTLYyIolc0QK0eYdtrevH2WKIPpkzaB-B2jJuoizI73Z-q5deHvVCNSnrFYoBRFbZaWN_DUaYgtT8trg3_S7tD8WH68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=Dg4ktBHS5syxNFPVX12598OfRAfhUAtxkhjwStpDNXj5ki_6TdKpVD6ZWuFJ4g0cXoU_1PcivQeTpHbyBDavGSEDUFKdxMP1Xo4ofYbTbnexK0PPWJB0yGM8yyO95DrC5YfCvNLOAnojMBAJr0Oa4sa36-lEf1v_tm7ww5tJF6zWPU4It6XTzOcCBtigRKwMz9WS9dXPVWDHLcwBZfvIxXTdZ2KHEWTGNl4zJfMvmyrDoU26psc32tujmUX7IWzc5AoF72JKxRCspGCRJTGAMPWN4SIqLCzRASL0RvcyaS7xTbHevlEbVJg6GPR_eHazr_c5fJWk42KG-Hfofv-QIhIsN1A6NUsfRAzHYSM9dov_-CUTXrTndV76eTduFu1nA1CPi6J2rsjcFPo2pC8sn0wT_lRXgyxb7rJQQ8Bd_QQSxYpoMN69bQ6ty-0T_SdiK6haxBwAoTOsJieXrNN1gVFohmBGEz2VE-gbphBweou8z1S-t9NnZDWw0k_7MR-0OBz9DdTBRUJEyTlT5ZTTEKpaWV4rm4nKdhHgOZXKQg5GOHh5A_iBLqemsT3ybLrJRY2DhMeCH5sCXBiQXTLYyIolc0QK0eYdtrevH2WKIPpkzaB-B2jJuoizI73Z-q5deHvVCNSnrFYoBRFbZaWN_DUaYgtT8trg3_S7tD8WH68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ سراسر سم از گفتگو جواد خیابانی و خداداد در ویژه برنامه جام جهانی؛ خداداد خواست کاری کنه خیابانی کم بیاره ولی ببینید چیکار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26782" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26780">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcG_1QM_QjYtIlEaHatkMcFPJjvB52lRwXR6WtGmg0FVmJqdn0wluP101CZit9cIxSfCSyEFDeXr4tj20cRaX4PxSaCpO8Ev1TLk-4C8Widry4yLYUZrMETnpWWxmPdBSkbUmSgUv7QSfeFJEVYIBBa0IAvlVlholP8V77KzmUAkbpbWFTHSzhFLcFKH4IS-p_5ek57-y-5qsbwZ3hb7ICQLakSWYRVPia3iYRN4QGJBtmvxEomWzUxMWSXq-3NmXsZUZDWXXEE7cCH-wrXo-_rgK4KkFqBlea3Zxay7HN7LyvQlthTHVLhpmA8mBnXTvdjjsFfxRMuBlMolE2Lyrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjgYtBibynVsDloYFvW_NyVLjzo9bsVITE_hINj0oil_4PhjymAQrtu0A4nB6N9ZYWY_wu49mPXbWvbRg-p5R12t99XAdgjJJQJpLnuvJNvcg0_RBeX2qF7Y8esQ0HEbVbmtQdGbAr9Mt5Uyq4vMu0SmaXTP3yuGZ76s5cdjIk_wwkrq87sDO9Zm10IkSv51oAAyZKh0-vAvXcM25ucJ5HR3hqqAyaYQQ7FQVn7Tpd_m4_zc6KSh_bk0pwbdwJ-0hXE_7KflELaYZsQUe02hjAKinDf8duG2eVjqjN8cDGv65n0QalhqKunXbyox6-T7T65Io5QmsMFcJb19n3b-Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم‌وزیبای تیم منچستریونایتد انگلیس برای فصل جدید رقابت‌ها که استقبال ویژه‌ای ازش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26780" target="_blank">📅 22:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26779">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzF7bAYNjtIU8TuMBARM8NDCqRVUMrqiLjtsX74D-f_5hDfaYXb4Qhm5l5yd9wUB_XSXOdGvSNufvsutFdtqqMrmocoP_yt2GzVY0OJYOJDTzbeBeLNjNdoBibasOqvwfHyNqu7FB2BtP5za83CPMeMqq748is0XU4CXHsXS5PFEn7wqHdvreV-AnKikthx9QsPni4OvuHolYBnmBE01dtwBP7uA9RZ1L5H-6kzXrND54FR_BQcpalY5VtN2x8P2D8UW3IeaNaLL08tPGl3eSat8omwb_k9ywlzzc4mSIERay5xt2b24_X2VDKqu_xD738ifJ96OVk-uWRMXsUpfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال بامدیربرنامه‌های جلال الدین ماشاریپوف‌ برای‌تمدیدقرارداد دوساله‌ستاره 30 ساله آبی‌ها به توافق نهایی و کامل دست پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26779" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26778">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJgrwVGh9eqALH6wsJ4Y9EP_dBhDyGDi4gCADSzmnmiaw0uHIR9X1ThoLjt59UVUOkmQaP7G1dah02USgsn2_Wad_McQEIe-9kEqv4y3HVcJ_wv_wPMqAR-jPHvGGUnNfBHGB3rKyWgOT7_qxyPk5vwpLaEbqHv0zAbMWuYA1v6ECvlDn_tbWFcHbVkP1dlT-ioWjnSg8luWvDvggQzAo8QuqJRWyfHC_Pah4Wr8emiga0C1LIrHqXRZgF5R3y2Pda7zMuE2KbKjwtCX0eJRvVrXkPzyBrCk6dAPZigvZ9tagkDb-c1wYYwLtjWOuPlfq_Kkzfbg2LSaOXmiG0S49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26778" target="_blank">📅 22:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26777">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQCKUxwPTYfkjT3_o78fmRjdOPco_x7TTsCmqcm9lyS4EqOsxOjVsCIMf7DAoL7D9Z9-VUKsLpsZTLb_IaY-Bn9qq9tWwD7WXq-FZfi0adtl4WLJylmaA--aaGgslDEM9UrPmslcp-Uu45BnJoVSITlTB7mn4GSNC-kepsGCR9gs2BfJboEyugnhpheppn4iWI6exgFETlvcE1cuRdgxVCK-wjbUUh0b9QaGRseeLs8D3Zqm_flPgNK8S_C63rXVRV3gldSVl2cmiU2wa3ggbgbuIye-nlOnbKGpC-hwJELCYeLuSHWOIWAL4NEJXR4vJ7BF30DAZRadcsLMKUhpGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا
: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26777" target="_blank">📅 21:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26776">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGcimjdFH-qBBnlaL6_6wCqfXUMsR0gCP3e-7PienMfCBaJnu5J4aoYYartmWtT8pCCZC5o5p9lj7FrOy2kJmEDfUXtzb-z2g1Q-Xo0macrEzr1f-K9y7_ia2pNOvKQJ6E5_hqLnIEQvNb5oaA3Gka6ZopfvrUEuZDFZ8ZAH0tCXXoM7ASRLSReyDVj5QQEAnl5LZWZtvaioyuNdwfpffpUDE0ylD18j_TyYKIlWgeW6nC6ky-bJ_HO2WfEjNRIETSuqZx7qVrRteVyikzzD0OSyL4obGWs1vEndSDTT9u42YcjwIPX_DZ8OqmiyrZD15m_qphlvS9Nsb0F-uWOnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26776" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
