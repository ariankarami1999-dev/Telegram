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
<img src="https://cdn4.telesco.pe/file/AbxtNlBvEhjx9eMuLQyE-CxnwSDAQIk78CZbOkb-qdWsYAA7P6u4R6hkL_6KgawT40Jc3jREp2vhRcfmxXPVEkmMewOJrnAbq-Wm1QrirCq9mj35s9JTSi01ohuNTVQbat1dWcICWH7L3j6h2hwcHcOZjJlcFqlgSZDFa9x2c5JDkz1BWWcKF_aUZNL97LC5WexyWCinpV4Qe6ABWO9imiE_g-m_G1WpZzYFYqTln_ApCUPfl0yk_Ys884yD2p89zBjlVkTBZrkVFxvhuLj-f7r-7JQbLZMTNAU6iCtmWe__AvsNarlpk8BGczIQTzoY48bv0Vxdt160gft4YvL0Bg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 21:56:26</div>
<hr>

<div class="tg-post" id="msg-20177">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده، درباره‌ی چین:  «ما می‌خواهیم امروز اینجا روشن کنیم که هیچ‌کس فراتر از دسترس تحریم‌های ایالات متحده نیست.  اگر آن‌ها تسهیل‌گر معاملات باشند و بخشی از اکوسیستمی باشند که نفت ایران را به پول و سرکوب تبدیل می‌کند، هدف…</div>
<div class="tg-footer">👁️ 281 · <a href="https://t.me/SBoxxx/20177" target="_blank">📅 21:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20176">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نتانیاهو: ایران تلاش کرد یکی از پسرهایم را به قتل برساند
کانال ۱۲ اسرائیل: سانسور نظامی ماه‌ها انتشار جزئیات تلاش ایران برای ترور یکی از پسرهای نتانیاهو را ممنوع کرده بود.</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SBoxxx/20176" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20175">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «خطاب به سربازان عادی حامی این رژیم: همچنان که حقوق‌هایتان بیشتر و بیشتر قطع می‌شود یا ظاهراً فقط به تعویق می‌افتد، از خود بپرسید که آیا فرماندهانتان کشورتان را برای پیروزی ترک می‌کنند یا برای ویرانی، و به یاد بیاورید…</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SBoxxx/20175" target="_blank">📅 21:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20174">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «ترامپ در حال برقراری تماس‌های تلفنی با رهبران جهان است و درخواست‌های مشخصی برای توقف تعاملات آنها با رژیم ایران دارد.  اکنون زمان آن رسیده است که رهبران جهان بین آمریکا و ایران تصمیم بگیرند.  هر نهادی که از طرف…</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SBoxxx/20174" target="_blank">📅 21:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20173">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SBoxxx/20173" target="_blank">📅 21:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20172">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
«امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.
ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه شریان اقتصادی است که این رژیم استبدادی را حفظ می‌کند تا زمانی که تهران به تنهایی بایستد.
از امروز، ما حلقه محاصره را تنگ‌تر کرده و هر منبع درآمد بالقوه‌ای را که سپاه پاسداران و رژیم ایران را تأمین مالی می‌کند، مسدود خواهیم کرد. ما در حال اجرای رویکرد «بدون نشت» هستیم.»</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/SBoxxx/20172" target="_blank">📅 21:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20171">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/20171" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20170">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB-F8t_gnmds70MwfYFqR2oGFAtx33yJmpHcGJsU5RfveIu35vnoUq1_gJhgTplyNHBYVuGMS9Juufy8BMwsR6lDveB2bA0G8kEJP4AyTkaPKOTxMMYo44wsKHGKhiQlGCx3ryfjoIU99JR62SGV-ltiBFdsx1EITPbTiK6kiyt7WVsz3v0s9DLoLbakwPA-QS7VAwIy5fuDbJeh6x-j3Ga1vi47c_QL3Px55FtGwt3_TQqsapwgvc33BpWfcpsBGikq6P3BfsTgXxHyOOVaGEfFd-yx9KGv8o5rbatGc8mvsZtckdQthjmS-1cEtmXxsm0LxPQeUnqMv2Yxc6-6YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 2.5 ماه پیش میداند که هدف درگیر کردن ترکیه چیست. بزودی یونان هم به اسرائیل خواهدپیوست.</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/20170" target="_blank">📅 18:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20169">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جلسه گذاشته اند برای بررسی وضعیت صنعت برق کشور بعد در همین جلسه برق رفته !</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/20169" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20168">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جلسه گذاشته اند برای بررسی وضعیت صنعت برق کشور بعد در همین جلسه برق رفته !</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/20168" target="_blank">📅 18:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20167">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c94f2d5d3.mp4?token=h-c2ylFpJNVxzvYv8nsPcOG5JrjvIUti0cpxEOP1DACZp_Myrj5GDC0AzU8xYB-ePotd5RFPe_G3fGX19_74SD-wLnaq38-DNjDGcGM0tOrOnDjWnAafEAECGBfLsYI-nLPgm_HLz7HEjaveLEUrvyYbo9tfIg9o6IRG8SqPnC6XaD6IwHDU2vaYB5mjoPvqvkAJMd1e1ZAAPV5XfXkUbtpOe4MaLNbtKz_UlJ-yCro-RPT4k4t9YhdIYcZaBZdh42ArQlJ9yJjKp-pveMI-YNI_Cm3NTqvwERR4v6Wdi3mKX_KbMU6lKMZ6epi3oL1EfyWgXDpBlj4TOTEqNCO9CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c94f2d5d3.mp4?token=h-c2ylFpJNVxzvYv8nsPcOG5JrjvIUti0cpxEOP1DACZp_Myrj5GDC0AzU8xYB-ePotd5RFPe_G3fGX19_74SD-wLnaq38-DNjDGcGM0tOrOnDjWnAafEAECGBfLsYI-nLPgm_HLz7HEjaveLEUrvyYbo9tfIg9o6IRG8SqPnC6XaD6IwHDU2vaYB5mjoPvqvkAJMd1e1ZAAPV5XfXkUbtpOe4MaLNbtKz_UlJ-yCro-RPT4k4t9YhdIYcZaBZdh42ArQlJ9yJjKp-pveMI-YNI_Cm3NTqvwERR4v6Wdi3mKX_KbMU6lKMZ6epi3oL1EfyWgXDpBlj4TOTEqNCO9CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  ایران به صورت کامل در‌ حال فروپاشی است.</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/20167" target="_blank">📅 16:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20166">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxAg5PqcZ2imTzc-pIheUJ6dn8-GcoK5w0Xc1shL_dhkVRYGz-51hKe1Y8dDKQK33sd-c9b1Xkqao2tXnMRbIdKF9iOJAXUDDJ2MKC3uytTVnApT4GjNbN5xD7C3Uf3dtMJiV6819lcCpnvbfDiOpLhZ3wLuZ6ZurTBG7MvbHrsnInF-CTN_FIIdMexRBZfVaoU9cBVBsnxJg4XwOqNRc60Phbo5AJOdt0MkJQF4kkwCRk2XnCWSPIJy1qnvGmTJ86xKbCzh9JVBINXh_Los6wIxCOnwrd-cUFarF0DzWsFhJanhzbp1hjl7nuhEyZ7zKiXcVtBTfnPHyM3bk7NcIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ایران به صورت کامل در‌ حال فروپاشی است.</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SBoxxx/20166" target="_blank">📅 16:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20165">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وزیر سابق دفاع اسرائیل، یوآو گالانت، درباره ترکیه:
باید درک کنید که وقتی ایران تضعیف می‌شود، آن خلأ توسط کسی پر خواهد شد.
نامزد طبیعی، با آرزوهای امپراتوری در خاورمیانه، ترکیه است.
ترکیه یک کشور قوی با میراث امپراتوری است. آن در پل میان آسیا و اروپا قرار دارد.
آن بزرگ‌ترین ارتش ناتو را به جز آمریکایی‌ها دارد، یک صنعت دفاعی بسیار قوی، مردمی سخت‌کوش و در عمل یکی از مناطق اصلی صنعتی اروپا است.</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/20165" target="_blank">📅 16:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20164">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-fd-cF1iHjj-wsMyBD_6thztT-Jg9JXN2jQQmkBrVVvCGJ8y0oN948XhJaR-Dp_JxboCqSywHWcpVq_YUsALQmloQUHcJh_7R5YWoKUWR1G78-hMbt-RxeYqRLjoa7Te0LuAQOv0LOAhFazC4EYengtC6JRa80wwQgLUOrzOQNufRYWURdBCGq3csRSQhPHdpQi_DP4Ybj6DT7nb-Fk9efFEo2An95Oa8xCYLrGGCK1eNYewVweYUR-UFl17wsboL75BtEReKu-D9a8F1OIfF1G2odOHNE3Ct11V8E21DxBW1QkV6aK1BIKwNK8KB0CZKYlKrsOG7Lk8SJ5Pgn5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک PL-15 و تحول در نیروی هوایی مصر  همانطور که در یادداشت پیشین گفتم، محدودیتهای شدید اعمال شده روی تامین موشک های دوربرد هوا به هوا برای مصر از سوی غربی ها، مصر را به خرید جنگنده J-10 CE چینی واداشته که مجهز به موشک دوربرد PL-15 است.  اما این موشک چه ویژگی…</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/20164" target="_blank">📅 14:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20163">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">Secret Box
pinned «
این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…
»</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/20163" target="_blank">📅 13:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20162">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">هر وقت پاکستان میانجیگری میکند یک جایی ازشان منفجر می شود</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/20162" target="_blank">📅 12:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20161">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bded5954b1.mp4?token=AHhtxqhv0Y01zYYjs1JQZEqrpValHPB-LJWQdVP5nGCWrxLpOHVlyt9kV1r2J78ZmHltrWbm4jBCMH7Uhf1HJCZ9-pBv_iM6XUpaY1N0B3Ri4Ylh-bNPI33p5_0fLesqtR5XK_CgUEmgx3v0BoYMzMLA1IfkW0Z_RE6S16dFtrXotQUex1OiKVEVw7lWW7Aerj8SMazwlwthvofq9FaTuJmodnlrHFcDDB4o32-cZq7EgeA1ZJuDcEZ-uTy43ryUmtOJZNwEyol26nA5UnVQfWWraNne9cmVTZLRLDZgeZJy0tQQy4bVWc9tiCf-5xJ4x13jgUZPKfwjABrGHmW0dlJraNe2dAuDnyxTZM1r0Psrofwv2H_KmaMH5IUYNqeSHYTyxzIEvkyoVds-TBR951frl4WSrUTP_s2gTWqykz2_T4mWDj7i6q5oiSmFTcNEUA_PNY_Iqxm6Js1TyAgV5ok_LRKvINYsb2G2ElCdqb4y3KdgdszVATvAw8JdbaB5OmY4hpefDf6WWm9rdghlzOPRLrcdoiYMLjcSCqg8yfIGGSB0MbOrIvo-1T_QyMt27uhYoHuDirQN-qA6Osxep0paQ19wyJ_E8QRec6r5HK1HgE93frgJlDttGnoNmv6wNE44J79F0F7bqEidXbecEV6pk2rGOdx_apr72iHh1ME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bded5954b1.mp4?token=AHhtxqhv0Y01zYYjs1JQZEqrpValHPB-LJWQdVP5nGCWrxLpOHVlyt9kV1r2J78ZmHltrWbm4jBCMH7Uhf1HJCZ9-pBv_iM6XUpaY1N0B3Ri4Ylh-bNPI33p5_0fLesqtR5XK_CgUEmgx3v0BoYMzMLA1IfkW0Z_RE6S16dFtrXotQUex1OiKVEVw7lWW7Aerj8SMazwlwthvofq9FaTuJmodnlrHFcDDB4o32-cZq7EgeA1ZJuDcEZ-uTy43ryUmtOJZNwEyol26nA5UnVQfWWraNne9cmVTZLRLDZgeZJy0tQQy4bVWc9tiCf-5xJ4x13jgUZPKfwjABrGHmW0dlJraNe2dAuDnyxTZM1r0Psrofwv2H_KmaMH5IUYNqeSHYTyxzIEvkyoVds-TBR951frl4WSrUTP_s2gTWqykz2_T4mWDj7i6q5oiSmFTcNEUA_PNY_Iqxm6Js1TyAgV5ok_LRKvINYsb2G2ElCdqb4y3KdgdszVATvAw8JdbaB5OmY4hpefDf6WWm9rdghlzOPRLrcdoiYMLjcSCqg8yfIGGSB0MbOrIvo-1T_QyMt27uhYoHuDirQN-qA6Osxep0paQ19wyJ_E8QRec6r5HK1HgE93frgJlDttGnoNmv6wNE44J79F0F7bqEidXbecEV6pk2rGOdx_apr72iHh1ME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که ‌وزیر کشور پاکستان در ایران است تا معامله تمدید آتش بس میان ایران و آمریکا را جوش بدهد، شهر دالبندین در این کشور بدست جدایی خواهان بلوچ سقوط کرد!</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/20161" target="_blank">📅 12:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20160">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/20160" target="_blank">📅 12:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20159">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaz0m4apLZtFSEPG0aTtGzkfjMdnI4xy4Q3Jn8_YxJOQpzCdZYukJcj0Na9Mcq6K3JmI8hWf5NKQj6crvtBIf5Vof_YEi-9AohizrjwOvE3NJmM1Bkp3AuQf0PvcfL5VALx0W_mKV6nfwc5XQFXFkZRS8YNLQd9Smo4PdgX3rHyToPsvtNUntLl8TvZBK4TOL3DvcnRvtadhmi3PPijzfc6nCobStaLLDVP2rniQdMl_rVKItOa5qa34y2w5Es2wGdYjKdtC0M_46WxPJ1WNZ90rliY0bAIpLGJARXz0fvJdoMn9GW5tLy9mcNEwiErImsKqBx2luz7SCvdLETFNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک مرکزی:
مشکلی برای تأمین ارز نداریم و هر کارآفرین هرچقدر اسکناس بخواهد تأمین می‌کنیم</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/20159" target="_blank">📅 12:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20158">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e31f970d.mp4?token=YQol51FxMiy_2OCDD5WQfRy2FTiVfPbkVMJ0TgDS_-qYfYuYT3V53cbBTlhLYFi9PrOL2yowBtE8-87asIZ0ehNDHhDSx_8UpULkGtif2fbLEJkSFrzvMDf3VZS4AB55YEPsw38fgDxepI4ExXzqyyxixPcqcrM7zw9nMaXHD3olNIlttHIV85ELqNKMEoxw5EYf9m6GjHeJK3j9qFPKwseHWdCyGcPuenDEc_0m_uBXNKNjG3p2sBPLYqaD2H38N-YMoWQHc3QOXk8j9piF-uXRhq8gau05ADaq_mfBjbY48C5Z6d9FW1_DxTXkSWwVLrfeQ_rbu1ss4VIyUYR4Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e31f970d.mp4?token=YQol51FxMiy_2OCDD5WQfRy2FTiVfPbkVMJ0TgDS_-qYfYuYT3V53cbBTlhLYFi9PrOL2yowBtE8-87asIZ0ehNDHhDSx_8UpULkGtif2fbLEJkSFrzvMDf3VZS4AB55YEPsw38fgDxepI4ExXzqyyxixPcqcrM7zw9nMaXHD3olNIlttHIV85ELqNKMEoxw5EYf9m6GjHeJK3j9qFPKwseHWdCyGcPuenDEc_0m_uBXNKNjG3p2sBPLYqaD2H38N-YMoWQHc3QOXk8j9piF-uXRhq8gau05ADaq_mfBjbY48C5Z6d9FW1_DxTXkSWwVLrfeQ_rbu1ss4VIyUYR4Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/20158" target="_blank">📅 12:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20157">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">درباره اینکه پول خرید واردات چطور پرداخت بشود نیز با توجه به اینکه ایران کشوری با بدهی پایین است، شاید چینی ها به دلیل نقشی که ایران دارد روی فشار بر مالیه و توان نظامی آمریکا وارد می کند، خطوط اعتباری درنظر بگیرند که بعداً (مثلاً بعد از رفتن ترامپ) تسویه بشود.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/20157" target="_blank">📅 12:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20156">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/20156" target="_blank">📅 12:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20155">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا مدعی شد:  امروز صبح بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد  روز تسویه حساب اقتصادی ایران نزدیک است  هدف ما قطع تمام شریان‌های اقتصادی است که ایران را سرپا نگه می‌دارد.  جایگزین برای کشورهایی که سرنوشت خود را به تهران…</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/20155" target="_blank">📅 12:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20154">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzWRXVjjaAAw_p2xBX2RcZ6VBUzPjj--rVVj-L2MVF6FVQTUjOS6d3r5meP1Q9OWoOnjkv3sf6hlKU-3Kvv8APbGfSFv6Lp3KhJwPik-BVXLdAKl_hFB66-r4y6N4-SCpV8gcX-64VW-5LXNqUvxqWSEmkfIkEAzah1VHT8i9SgQzFwH_rHmmr5CmSU7K5QRJoGpIwAf_ptyOsKkNlYPWoR5bwC-Ond0-eeYYBJFhLWJ3py7Ibpl3FGqTFkv8098WjdIhVFGMedBT6FDqTaBfxanUlCTHGlYtxXZKcos7GptCK1mAULn_3i0MUbsLJP5Fj2OYCWsvEIz1uxT9Hji3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز گزارش داده که صادرات نفت ایران در اوت به حدود
۵۳۴ هزار بشکه در روز
کاهش یافته، در حالی که میانگین سال ۲۰۲۵ حدود
۱.۴ میلیون بشکه در روز
بوده است</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/20154" target="_blank">📅 11:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20153">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ما بیشتر تیله بازان خوبی هستیم به نظرم.</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/20153" target="_blank">📅 11:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20152">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فعلاً این یادداشت را بخوانید؛ توضیحاتی درباره برنامه بازخرید اوراق قرضه که هفته پیش اعلام شد و سناریوهای پیش روی طلا ارائه داده ام.</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/20152" target="_blank">📅 11:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20151">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyfxab267TfFSQj6SbET5HtsUVFYXqvTCdGJJc_AMNMthk4HP6zkGYxgfhRd5oBcK_SWJSq29pCSRko45JLkcs-elT6Mt5oT5oMrkSjLGx72it7K2GEjD-8YqOW_6NOIRV5LLKvOGyCQ0kM45E5cnnPLlCiBgPgYUDDwY3of4b-at2jxv9ndY4ntd_N7qxDpBCiMHycaLEXIJPJvqEGnLul7qFt7CKvlGkW38tBR5j-XYW1nNPMir4EfDgeuFgLs5J3PxmigGnAP8Ty_tZrrWUWt_I1rDGhIqcXYAEuCWmRwdHVxp9IY6wJ3YqupPtD6MejqCrLdd0bbG2FeI7f5Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد.
دقت کنید که با آغاز برنامه بازخرید اوراق قرضه بلندمدت خزانه داری آمریکا، یک عامل جدید وارد محاسبات شده که در این شاخص هنوز آن را دخیل نکرده ایم که روی طلا موثر است.
ولی با این حال، پیش بینی می شود که شاخص های سهام امروز زیر فشار فروش بالایی بروند و نفت هم احتمال زیاد صعودی باشد.
برای طلا، احتمالاً از مومنتوم صعودی کاسته بشود و اصلاح داشته باشیم اما به یاد داشته باشید که اقدام اخیر خزانه داری زمینه بنیادی طلا را تغییر داده است و از این پس، معیار موفقیت شاخص GRI را روی دارایی های کاملاً ریسکی مانند شاخص های سهام تعریف میکنیم.</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/20151" target="_blank">📅 11:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20150">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbMOXXyHYVmK4NuTj6zr4IIDux84grdGLr-3G2Iku625qwW3U7NjrjVuGjZYMBz0S646a4v989a_B605U9YXmfCGyz1xyVTDcmj7DUHEBu9lnKhxh5StLnDLnk3ILPLcjXQXNM6fHPXNEJoJp9w-_XquQ8BGEP7OXqWOSymXjKeIwz4aVtSJiSaqKAKHr07KZLX9FgrJwOfb5Jl4PhwMq-C4NsuVDRkF_dAA6HFzIXny1Tkyr9kwlBAYAF2uFTVuQqqvGNtbXWqh-6OGYC2dWSw7AaI2WTUNYGyYPaS5ddMR59AR1yTEa9XO33qKsVlKIde-0wmfUJIqihlpHw_Snw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدف قرار گرفتن یک کشتی نفت کش در نزدیکی بندر ینبع عربستان</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/20150" target="_blank">📅 11:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20149">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا مدعی شد:
امروز صبح بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد
روز تسویه حساب اقتصادی ایران نزدیک است
هدف ما قطع تمام شریان‌های اقتصادی است که ایران را سرپا نگه می‌دارد.
جایگزین برای کشورهایی که سرنوشت خود را به تهران گره می‌زنند، بسته شدن هرگونه مسیری به سوی رفاه پایدار است.
هر کشوری که به عنوان شریان مالی برای یک نظام رو به زوال عمل کند، باید انتظار داشته باشد که انزوا را با آن تقسیم کند.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20149" target="_blank">📅 10:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20148">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یک مقاله در روزنامه اورشلیم پست اسرائیل خواستار آن شده است که اسرائیل، ترکیه را به عنوان یک تهدید نظامی در سطح ایران در نظر بگیرد، و این جمله تحریک‌آمیز را مطرح کرده است:  از ادلب تا استانبول، اسرائیل در صورت لزوم، حمله خواهد کرد، نه اینکه دفاع کند.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20148" target="_blank">📅 01:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20147">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJD7HZdFip5d8geq64795Qpg5BiF8ASy4RreDzliQPP0NuVsEpMdK0P2TVi0bimEpsZywoWMJvbnahoBTSc4LGUTdyLxUfQgSbqVAWHlhNXLG4ZvGpFvmMGjX8IsLzvWSGFqXEm0BOu_xS1nayUHsgkZ-Y7aGKbh9tJnCedk7Kz8qtJdiv7RNsSTNuNkbXybijTaDL34hJ8YWzDr4keTrnK4xW7xN9zihe6rgIIBX0UM0fIPQNtZRSKGeqJpX8UGOcTh5MYsOxy59ld9i_mCPc5-pq0Xb-3agpHGB79msO1Y24g_UiIpSHiao4__bS9sJHumC5UOlFDZzGIkG82s8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مرندی:
در روزهای آینده، درگیری نظامی به احتمال زیاد دوباره شعله‌ور خواهد شد.
با هر رژیمی که با ترامپ برای گرسنگی دادن به شهروندان ایرانی همکاری کرده باشد، به شدت برخورد خواهد شد. اقتصاد جهانی در آستانه سقوط است.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20147" target="_blank">📅 22:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20146">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c36a2627a.mp4?token=BXx_m4bqiyATC0yKdvz8HtihMx6ZzIJiCJ6KDKrmZVTkcyHx8vr45nMRdw8yt-d601E5RDxGA6TPrjYt57rvlIs_B1N7ccp4-6nds6CZaRlbGbVlY41zZlTwXLpgjoC7-K7A6OgzMcQZoUi3UOJ_jgltZBgMXNclF1p7KwR08K4o1kV0e-J-ov_9nkd3oB36hTAbOsAKELl4ASItJ8peOgfORIW4_47aBxgCv91G7EOFmMZGf5mgribawwoFs_zcm-wBFrklgrEOUMCM2atR9sCQJxV-gDAMXhk5SW2n7lCNZEisFO55oueQz2LFNI8WfmkYBDivYxRg22OogorM7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c36a2627a.mp4?token=BXx_m4bqiyATC0yKdvz8HtihMx6ZzIJiCJ6KDKrmZVTkcyHx8vr45nMRdw8yt-d601E5RDxGA6TPrjYt57rvlIs_B1N7ccp4-6nds6CZaRlbGbVlY41zZlTwXLpgjoC7-K7A6OgzMcQZoUi3UOJ_jgltZBgMXNclF1p7KwR08K4o1kV0e-J-ov_9nkd3oB36hTAbOsAKELl4ASItJ8peOgfORIW4_47aBxgCv91G7EOFmMZGf5mgribawwoFs_zcm-wBFrklgrEOUMCM2atR9sCQJxV-gDAMXhk5SW2n7lCNZEisFO55oueQz2LFNI8WfmkYBDivYxRg22OogorM7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو:   این هفته خاموشی‌ها تمام می‌شود</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20146" target="_blank">📅 21:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20145">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزیر نیرو:
این هفته خاموشی‌ها تمام می‌شود</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20145" target="_blank">📅 21:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20144">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/20144" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یک صوتی مفصل در این خصوص خواهم داد.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20144" target="_blank">📅 19:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20143">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آیا صادرات نفت ایران از مسیر ریلی می‌تواند جایگزین صادرات دریایی شود؟   در هفته‌های اخیر گزارش‌هایی منتشر شده مبنی بر اینکه ایران در حال بررسی استفاده از مسیرهای ریلی برای انتقال نفت خود به چین، به‌ویژه از طریق خاک افغانستان و آسیای مرکزی، است. این ایده در…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20143" target="_blank">📅 17:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20142">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/un1OQiVtuxdC0VDRhfUh7dTSEF3H_SjON1ii4JokdQO92NtTxIwqYdYGIhCFN7sbKiBbAHJ9ZsI7VoupWAi-Gp5PZwNQ0hrZCzn1uJWKer3uMhSC4_Q9xVBF2ZS9qXqJJLqdZiOyKAPweZYEDwhE72XImULKxW7QX8Q8G3Q6vO0BfVZ4omDHS6INy5uga-Hj7auMqolE-TUzXNOVUSuLicKevGGJcN5fEBM2blgexKS4rwRhS-xkjlyo4X2kL9FAu2P9JXIJxRX5bDG7kWRpr9dc0v9JywDG4Bnt0hXJjHlzKddtOi0LiMcM1X15b4uzYsal3vTLUrQAgzfXkLHeKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین
پس از آغاز نخستین محاصره بنادر ایران در
۱۳ آوریل
، حمل‌ونقل ریلی کالا از
شی‌آن چین به تهران
افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر
سه تا چهار روز
رسیده است.
این مسیر ریلی پیش از آغاز بحران نیز فعال بود.
نخستین قطار باری مستقیم از شی‌آن در
۲۵ مه ۲۰۲۵
در بندر خشک
آپِرین (Aprin)
در نزدیکی تهران تخلیه بار کرد. بنابراین، مسیر مذکور پیش از اعمال فشارهای دریایی ایجاد شده بود.
مسیر قطار از
قزاقستان و ترکمنستان
عبور می‌کند و سپس وارد ایران می‌شود و به آپرین می‌رسد. در این مرکز، محموله‌ها ترخیص شده و برای توزیع در سراسر کشور ارسال می‌شوند. حمل بار از این مسیر ریلی حدود
۱۳ تا ۱۶ روز
زمان می‌برد، در حالی که حمل دریایی در شرایط عادی حدود
۳۰ تا ۴۵ روز
طول می‌کشد.
افزایش تقاضا برای این مسیر هزینه حمل را نیز بالا برده است. قیمت حمل یک کانتینر ۴۰ فوتی در ماه مه به حدود
۷ هزار دلار
رسید که تقریباً ۴۰ درصد بیشتر از سطح معمول بود.
هر قطار حدود
۵۰ کانتینر
حمل می‌کند. محموله‌ها عمدتاً شامل قطعات خودرو، ژنراتورها، تجهیزات الکترونیکی و سایر کالاهای صنعتی و مصرفی هستند. قطارهای برگشتی که با ظرفیت پایین حرکت می‌کنند نیز هزینه حمل در مسیر غرب را افزایش می‌دهند.
بااین‌حال، ظرفیت ریلی قابل مقایسه با تجارت دریایی نیست. یک کشتی کانتینری بزرگ می‌تواند هزاران کانتینر حمل کند و انتقال نفت خام یا سایر محموله‌های فله‌ای در مسافت حدود
۱۰٬۴۰۰ کیلومتر
از طریق راه‌آهن از نظر اقتصادی مقرون‌به‌صرفه نیست.
در نتیجه، این کریدور ریلی نمی‌تواند تجارت نفت ایران پیش از محاصره را احیا کند یا جایگزین دسترسی آزاد به بنادر شود.
پس از آنکه آمریکا نخستین محاصره را در
۱۸ ژوئن
لغو کرد، این محاصره در
۱۴ ژوئیه
دوباره برقرار شد و اهمیت مسیر ریلی به‌عنوان یک کانال جایگزین افزایش یافت.
ایران همچنین از مسیرهای زمینی و ریلی دیگری استفاده می‌کند. خطوط ریلی در شمال به سمت
روسیه
امتداد دارند و گذرگاه‌های زمینی در شرق نیز امکان ارتباط با
پاکستان
را فراهم می‌کنند.
هیچ‌یک از این مسیرها از نظر حجم قابل مقایسه با حمل‌ونقل دریایی از طریق خلیج فارس نیستند، اما امکان انتقال بخشی از کالاهای مورد نیاز ایران از طریق مسیرهای زمینی و ریلی را فراهم می‌کنند
.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20142" target="_blank">📅 17:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20141">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">برخی اخبار تاییدنشده خبر از سفر عاصم منیر به تهران می دهند.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20141" target="_blank">📅 16:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20137">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">انسان‌ها_بحث_درباره_خودآگاهی_هوش_مصنوعی_را_برعکس_در_نظر_می‌گیرند.pdf</div>
  <div class="tg-doc-extra">328.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/20137" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یک بحثی که وجود دارد اینکه یک مدل «رایانش قهری زیستی» هم مدنظر ممکن است قرار بگیرد. (Forceful Biological Computing) که در آن مغز یک انسان بدون رضایت خودش از طریق کاشت ابزارهای خاصی (نانورباتها یا ....) در اختیار یک شرکت پردازشگر هوش مصنوعی قرار بگیرد.  در…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20137" target="_blank">📅 15:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20136">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترکیه، فاکستان، عربستان، ایران، بنگلادش!  به نظرم اسمش را پیمان «جده» بگذارند بهتر است.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20136" target="_blank">📅 15:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20135">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">المیادین به نقل از یه مقام ایرانی:   از ایران برای پیوستن به "توافق مکه" دعوت شده و تهران الان دارد این موضوع را بررسی می‌کند!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20135" target="_blank">📅 14:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20134">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">المیادین به نقل از یه مقام ایرانی:
از ایران برای پیوستن به "توافق مکه" دعوت شده و تهران الان دارد این موضوع را بررسی می‌کند!</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20134" target="_blank">📅 14:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20132">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVCcIt-pjQU2ecUlM-AbCqO0Fm7wKx5zNq5cxdkUvw4Dp44TDJ2JMQ7Va9MTlkdow3RP-zo3Ng6-hB2XiWcCtO1_noFppD0gB3bYlClGbbmGAP0MZdecc-9VhnZ7ECpwY9YGudtld1jUX5boL3e-yiDnGNGUEL1zz98tWaLA-SZZAj2MekibfrVJRCE32PyC_KsR_HXv-qtp9kJLHLzf--H08Z8kTwagpnH260tBeJVI1DZ36G1DTCDjrJS9Ug9TqrdFeW6sx0vbRuOg8wV-4up5AVkYeClBkaKESpARdDFdVXwRptdb2PBnCPQtkgdN-q0I0TrRcKgP3TgxTBWAnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04647b5b32.mp4?token=dZzsjYnAgtJy5LRzBjxo-28mMhJTLcapBSksH-qMG3Ne6NdElcPqxMHT4wfPK77C8c6uHlXDAx_J0c1WyjdTFSb581EGZ9OsWUhzkQIBC8ORxW8HrEL1V8Z2VuD360vEVJIKwFGuC7uaC6H3UJo-aCVW_UwS1QLX5mccU8_NgAyrvXgY3o9PKHBYEEzY3YlVICZWUuOx7tEYRmgiHNZBx3RSYw7YhjWr7yprE22eins83OOi1S3jIVrQtrPra-fIKXV12hVnNmGlTALwRjDEN0HcJDAXscJmNo_y-yBg1oNQtXy6PYdRWzq0sX362qQysQD5TvDYZ7Vxr7q4C-VoAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04647b5b32.mp4?token=dZzsjYnAgtJy5LRzBjxo-28mMhJTLcapBSksH-qMG3Ne6NdElcPqxMHT4wfPK77C8c6uHlXDAx_J0c1WyjdTFSb581EGZ9OsWUhzkQIBC8ORxW8HrEL1V8Z2VuD360vEVJIKwFGuC7uaC6H3UJo-aCVW_UwS1QLX5mccU8_NgAyrvXgY3o9PKHBYEEzY3YlVICZWUuOx7tEYRmgiHNZBx3RSYw7YhjWr7yprE22eins83OOi1S3jIVrQtrPra-fIKXV12hVnNmGlTALwRjDEN0HcJDAXscJmNo_y-yBg1oNQtXy6PYdRWzq0sX362qQysQD5TvDYZ7Vxr7q4C-VoAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاریکاتور اکونومیست با عنوان «کمبود رهگیرها» تصویری طنزآمیز اما هشداردهنده از یکی از مهم‌ترین آسیب‌پذیری‌های جنگ‌های مدرن ارائه می‌کند یعنی محدود بودن ذخایر موشک‌های پدافندی در برابر حجم بالای حملات موشکی و پهپادی.
در تصویر، سربازانی که ظاهراً نماینده آمریکاییها و متحدانشان هستند، در حالی که تعداد زیادی تیر دشمن ایرانی در سپرهایشان فرو رفته، زیر بارانی از تیرهای دیگر گرفتار شده‌اند.
دیالوگ بالای تصویر نیز به‌صراحت می‌گوید که جهان به رهگیرهای بیشتری نیاز دارد، اما بخش بزرگی از ذخایر موجود برای دفاع از آسمان خاورمیانه مصرف شده است.
نکته جالب‌تر، شباهت بسیار آشکار ترکیب‌بندی تصویر به صحنه معروف فیلم
300
است؛ جایی که سربازان اسپارتی در برابر سپاه عظیم ایران هخامنشی، زیر باران تیرهای پرشمار، سپرهای خود را بالا می‌برند. این ارجاع تاریخی، پیام کاریکاتور را تقویت می‌کند: مدافعان امروزی نیز با وجود فناوری پیشرفته، در برابر «اشباع» شدن سامانه‌های دفاعی با همان مسئله‌ای روبه‌رو هستند که سربازان اسپارتی به‌صورت نمادین با آن مواجه بودند.
طنز پایانی تصویر نیز تلخ است: سرباز سمت راست می‌گوید «امیدوارم دیگر چنین اشتباهی نکنیم»؛ اشاره‌ای به این واقعیت که مصرف سریع رهگیرها می‌تواند در جنگی طولانی، خود به یک بحران راهبردی تبدیل شود.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20132" target="_blank">📅 08:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20131">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خب دیگر بس است بخوابیم.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20131" target="_blank">📅 01:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20130">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هر ایرانی در سال یک بار معتاد بشود و 2 بار ترک کند تا اینطوری تعداد معتادان کشور کاهش یابد و وابستگی کشور به تریاک وارداتی کاهش یافته و صرفه جویی ارزی کنیم.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20130" target="_blank">📅 01:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20129">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هر خانواده ایرانی در خانه اش یک نفر را به عنوان سرباز آمریکایی اعلام کند تا ما دستگیرش کنیم و به آن خانواده 30 هزار دلار بدهیم.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20129" target="_blank">📅 01:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20128">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مردم در خانه شان تنگه های هرمز پرورش بدهند تا ببندیم و از کشتی های عبوری عوارض بگیریم!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20128" target="_blank">📅 01:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20127">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SP5zd8wTi_ekOS8K9ASTJInBITgZwMctYKbefR98IeP-sjRtN1-kqFUWre1HwfEE96Ew9_a6UVFLQutMKOvlJ38tkXQ5n7lul1eic0fTYVQE7KYMIoHmXfD1EHp6tf3xrx6l4kRwQcsSrybxKSJ21augQglbESEB_rITkEWKK-pa8qzPsk8kdU6QkBCc5VNt4p9TfMIuN6PRhMB1QmyIglqP_gfsBmSydLt-qMJ9Liof1WNTNTuW9bS-0yY0Zgpkjhm5Ocr0yuwZ3HqvLr8Fj8cJjm_Yrh8retjUiCU-0UUXqffAr0WAIvoKyxtt1McB9t0-FfkzNVx08STuq7dwsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20127" target="_blank">📅 01:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20126">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asckCTalTIzyOz0roAlP05cIBjFi_rx7eFBBPsgpxTupLg5c5n7eVv_jcQj9Kv4VODIUBGVd5sFZ3p6c99S84KPVu_ID9qFrHWBKFsqFQRKSFIy3zsX9vic76uLL56siHodlX8yLZOnlpVsWyTK4ca2dpxFp7YYaW5fqNETAnxnkL12UHT_msjNdlBSH04z5eRwH0MkGdmA_FCmGECC0IcHmVy9h2VwNGvmdktOxakjOOLY97GtCxOjeapExcMNmL6yivWydzzygPyK27zRVXWuDbXOR-_oNx_Y8WUjlXHiKYfehNC3eL7vFV1_pnNMkj3lzkCz20L_vexCr5mA9hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاربران اسرائیلی با انتشار این تصویر، به تهدید اردوغان پرداختند.  جالب است که این تصویر شباهت بسیاری به صحنه دستگیر کردن عبدالله اوجالان رهبر PKK دارد که اتفاقاً با کمک مستقیم موساد صورت گرفت.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20126" target="_blank">📅 00:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20125">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8jD-igw3rLD-fJp7wabwVQcM7YzlaIAbWDdYM0ahBGDp9AyZJ2-u17klcmnBYDf7Z_H9yn2zRoE8OQUWuN61ZphFFwnQ7vyfOCAnyGldIch2fDl3kaeT4ymq0DwADXY0HBxNk7yOGa-ln2F6VF57LyECEHaadqkrmvwWLqep2L88KW8e9s0iIOV28yy-nIYEKPWh3ggg7ffyLKlCELPKRfvQb7SLizqgS6FxH_hEh-P8q-Z6vQ4RtxN_Z2id66JLu-p804jLeBcI5JSKlQrGkaji_yiVJR_sgvJH5mk9BeIqspERH26JVrPel2IGSEEiya3An46LzK1s4rD7vAiMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاربران اسرائیلی با انتشار این تصویر، به تهدید اردوغان پرداختند.
جالب است که این تصویر شباهت بسیاری به صحنه دستگیر کردن عبدالله اوجالان رهبر PKK دارد که اتفاقاً با کمک مستقیم موساد صورت گرفت.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20125" target="_blank">📅 00:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20124">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.   اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20124" target="_blank">📅 00:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20123">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20123" target="_blank">📅 00:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20122">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مردم فلافل بخورند و در خانه شان نیروگاه بادی راه بیاندازند</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20122" target="_blank">📅 00:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20121">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8jI5_92vcfnHabWjZgJbImRCvQvwSK1EYiGzpTwNINbjGBpMf7Kb7dvyJEod_Su9_TYRwQPqF6EkDpA40wMQy3eC2tWNfL3FGcE9k_TlmWT6PRc-YfWxY-euy2k3A3trDMghU3_SZpiynQcUE858OcCd9gpAHpQDJsBOwdkK0e0S8dQ_l-V3y1QGv-MSfQ6logF5ovw_YvaBtjlvSPrpsOA6zD4HP8fDEyvZrwqKNYkMbVvJ4Hol7N7p6dBOEnLytVH54zoxA3oDJtWJG_-srgRzhb5LnRcg4aIW87A7yli0vkVMVHJmX9iWiPN5jMOmZSW3Fe8UJH2fgTFdx6s6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عن این مفنگی را درآوردید!
ولش کنید دیگر بگذارید بمیرد.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20121" target="_blank">📅 00:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20120">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7EtZ0AH3vhTTM-2axE5JMCkRdkAHhImKN3zcc63cxxuT-uMSrOEF8tYQNGqhaTXkVNDo42sIybTeSLkrAhAvtl5yVh7GjCeQ1tkwRiTdIbhuzo9glaDBmTadYGw2JLT3epabRfUJl0fLn__GajULbmogNhkU0bFZ9_H8LmWZbFeVYbit20sYaeRuTV_YbPGY13s6HJLLNwGyS-72pdqfAFfM7bZG5a7G0bDFgvhu1LnA39D0OVc-76mbSM-EgHwbLzhO4oH2V2BEsbf2HQarAjZl-3hph-AABhHMHMgAW1rmLIQIycnw3y0SYwmCTVk_P_mVyGyuvOIcfG7KcIWAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید یادتان نباشد ولی این نخبه نابغه کشورمان — دکتر حجت عبدالملکی — که حتی رییسی او را از کابینه اش اخراج کرد یک بار گفته بود با 1 میلیون تومان میشود کار ایجاد کرد!
یک نفر خوش ذوق هم زیر پستش کامنت کرده بود بله 700 هزار تومان دستگاه تقطیر با 300 هزار تومان کشمش!
البته الان با 1 میلیون تومان نهایتاً یک پیتزا با یک دوغ به شما می دهند و آبش را هم میدهند Meساکی بخورد.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20120" target="_blank">📅 00:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20119">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">باید در هر کوچه یک شیره کش خانه باشد و بعد کنارش یک کمپ ترک اعتیاد بزنیم تا مردم هر کوچه از هم پول بگیرند و گردش مالی ایجاد بشود و مالیاتش را هم بدهند به ما.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20119" target="_blank">📅 00:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20118">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">محسن رضایی:   مردم در خانه‌ها و محلات شروع به تولید محصولات مورد نیاز جامعه کنند</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20118" target="_blank">📅 23:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20117">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">محسن رضایی:
مردم در خانه‌ها و محلات شروع به تولید محصولات مورد نیاز جامعه کنند</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SBoxxx/20117" target="_blank">📅 23:18 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20116">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f676cce991.mp4?token=BqzdajyJZk8-CL61653Lkkkok4FUH6tnGx5XTzBLv1XzjNl3q3NPPAq7qk7fIQXTnmU8t0S02_RS8DMMjYoID8aQmLx7cB5G8iNGzrEepdRKxDKalcA1M24OLQLNL9SUFIK7ky6XOPA6O9_hNG1ZjitR5Rtteq22BlkQbKMFjj60KY91akAgiIojhKr3EKr_n3kCf-9Lcvjmfi_UzK91YIdv1aWdzePayh9LD22b2w4OUuI_V2huVUQJhG5ym9V7DUxLM1rfEHVB7vlUBkXpDWDkMncG82TnZQ-VZOT4KgQoQrdI0ixgjCL6_8DhJ2qIQm_aXCZCZ3PNNYht4XTNlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f676cce991.mp4?token=BqzdajyJZk8-CL61653Lkkkok4FUH6tnGx5XTzBLv1XzjNl3q3NPPAq7qk7fIQXTnmU8t0S02_RS8DMMjYoID8aQmLx7cB5G8iNGzrEepdRKxDKalcA1M24OLQLNL9SUFIK7ky6XOPA6O9_hNG1ZjitR5Rtteq22BlkQbKMFjj60KY91akAgiIojhKr3EKr_n3kCf-9Lcvjmfi_UzK91YIdv1aWdzePayh9LD22b2w4OUuI_V2huVUQJhG5ym9V7DUxLM1rfEHVB7vlUBkXpDWDkMncG82TnZQ-VZOT4KgQoQrdI0ixgjCL6_8DhJ2qIQm_aXCZCZ3PNNYht4XTNlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخستین تمرین رزمی جنگنده سبک یاک روسی در نیروی هوایی ایران    ‌
👍
جنگنده یاک در کنار دو فروند جنگنده میگ ۲۹، در عملیات رهگیری و منهدم کردن پهپاد هدف مشارکت داشت و خلبانان جنگنده‌های میگ ۲۹ با مهارت بالا موفق به شناسایی و رهگیری پهپاد هدف شدند.
👍
در ادامه، جنگنده…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20116" target="_blank">📅 22:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20115">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اسراییل در حال بمباران جنوب لبنان است.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20115" target="_blank">📅 21:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20114">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmhbOvFmv6HuLCqHZ-AMT4Cnz7HQMTgrlIMTY7T9tVDAx7EPaa_rw3K5PYeBmJRjIRQYjcJGK4-pwYw0zy7HevmRh_y1PWnwRmFpIlH4bIyQU8OB443u_ZSlZf2Wsfy--Nnaquz5UmUJ6mpc6BvzuzqwO9ocQaAUlM6yhKT3LoeRFvWMdhJPaBf3wNly2YavHyiszr-PA9w5zyfwkJCSb2bGaKtwJ_DTAzcNef0v-u62ZzaV5bgfn6EJE7MOqk69PclTRK8TpJGA7NpgXd7qrGHpMsX8nKTkzFCDIGDH6wboYuAYXTwgHe_3ugm-6iY0QMfHeVmtlqJuMwaIa97f3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقاله در روزنامه اورشلیم پست اسرائیل خواستار آن شده است که اسرائیل، ترکیه را به عنوان یک تهدید نظامی در سطح ایران در نظر بگیرد، و این جمله تحریک‌آمیز را مطرح کرده است:
از ادلب تا استانبول، اسرائیل در صورت لزوم، حمله خواهد کرد، نه اینکه دفاع کند.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20114" target="_blank">📅 20:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20113">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یک صوتی مفصل در این خصوص خواهم داد.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20113" target="_blank">📅 18:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20112">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اوه اوه!    بنگلادش در حال بررسی امکان پیوستن به پیمان مکه است!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20112" target="_blank">📅 18:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20111">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">باز سعودی ها دستکم کتک خوردن ترک‌ها در سوریه از اسراییل برای بار پنجم را محکوم کردند!  شهناز جوراب که کلا خودش را زده به کوچه علی چپ!   نه حملات یمنی ها به سعودی را محکوم کرد نه حملات اسراییلی ها به ترک‌ها را !  سبحان الله عجب پیمانی شد این پیمان ناتوی اسلامی…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20111" target="_blank">📅 18:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20110">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دلار فردایی تهران
⏳
192,300 تومان!  کاملاً مشخص است به صورت دستوری دلار را دارند بالا می برند تا جناح تندرو را به تسلیم وادارند یا دستکم گرانی ها را به گردن آنها بیاندازند.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20110" target="_blank">📅 18:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20109">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.   اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20109" target="_blank">📅 18:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20108">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خیلی عجیب است.   خود ترامپ در مارس ۲۰۱۹ منطقه جولان را به عنوان بخشی از خاک اسراییل به رسمیت شناخته آن وقت سفیرش در ترکیه صحبت از «اشغال» جولان می‌کند!  حدس میزنم عمر سیاسی  — و شاید زیستی — تام باراک (که عرب تبار است) بزودی به پایان برسد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20108" target="_blank">📅 18:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20107">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-poll">
<h4>📊 تاریخ شروع جنگ ایران و‌ عراق از دید عراقیها چه تاریخی است و چرا؟</h4>
<ul>
<li>✓ ۳۱ شهریور ۵۹ — حمله همه جانبه ارتش عراق</li>
<li>✓ ۳۰ شهریور ۵۹ — حمله هوایی ایران</li>
<li>✓ ۱۰ مرداد ۵۹ — سخنان تحریک آمیز رهبران ایران</li>
<li>✓ ۱۳ شهریور ۵۹ — گلوله باران مندلی و خانقین توسط ایران</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20107" target="_blank">📅 14:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20106">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این هم جواب آمریکا:  ایالات متحده در حال پیشبرد قانونی است که هلند را مجبور می‌کند تمام فروش و خدمات باقی‌مانده دستگاه‌های لیتوگرافی ASML به چین را ممنوع کند.  قانون MATCH به دستگاه‌های DUV قدیمی‌تر که هنوز تحت قوانین هلند مجاز هستند، هدف می‌گیرد.  چین ۳۳…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20106" target="_blank">📅 14:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20105">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">چین می‌گوید تهدید رئیس‌جمهور ترامپ برای آغاز «جنگ اقتصادی» علیه ایران و شرکای تجاری آن کارساز نخواهد بود.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20105" target="_blank">📅 14:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20104">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دنیس اشتایلرمن، رئیس شرکت فایر پوینت، تولیدکننده موشک‌های «فلامینگو»، پیامی با تهدید علیه ایران منتشر کرد.  این تصویر، فلامینگوهای صورتی را نشان می‌دهد که در امتداد مسیری که اوکراین و ایران را به هم متصل می‌کند، پرواز می‌کنند و لوگوی شرکت و عنوان زیر آن آمده…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20104" target="_blank">📅 13:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20103">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20103" target="_blank">📅 13:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20102">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ایران اجازه عبور چندین تانکر نفتی عراقی از تنگه هرمز را پس از درخواست عراق صادر کرد: ایرنا  چنین اقدامی در اوج فشارهایی که روی اوراق قرضه خزانه داری آمریکا آمده به صورتی که باعث شده اسکات بسنت دست به طرح عجیب و غریب بازخرید اوراق قرضه بلندمدت بدون تقاضا بزند،…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20102" target="_blank">📅 12:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20101">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.   اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20101" target="_blank">📅 12:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20100">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.   اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20100" target="_blank">📅 12:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20099">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy3UEsQLQa-WzALiv8EiJQ1b8Kci9FQhKIijaZyM7ORUsQxScl8MSX_7ExjkwVqfjlnk0q2AForGvgPlPiNuJtIB12oxriZbE2U7n_gZDppIjd9y4-lScFrBbQ_0g7eB96UPwucLg7AhuxINeq7VEdlLhA1KQ_pfirV1obZnhDRr859BBma2-3Iaux5Xf1jFs5fgc7iUK0CywrgNMO8zQNY1goqFLGSMBWq1ShmGXyj_1YCeP0_VSSbjgFQBWowgOUPHG1tMKSGQrAs3SGw9P8Aae0sY05kjyf_pRbwzM0lvNHRgn_FO6FW9EfIn8aNZJYVKO7aNzgAiTZg5BqnGBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.
اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد بخشی از حاکمیت بیش از گذشته به این جمع‌بندی رسیده که ادامه جنگ و فشار اقتصادی می‌تواند هزینه‌ای سنگین تر از جنگ برای نظام ایجاد کند.
پزشکیان دیروز صراحتاً گفت بهتر است جنگ در مقطعی پایان یابد و «اکنون» پایان دادن به آن ترجیح دارد. قالیباف نیز هشدار داد که حتی قدرت نظامی بالا، بدون گردش مالی، رشد اقتصادی و تولید داخلی، نمی‌تواند کشوری را که مردمش تحت فشار معیشتی قرار دارند، پایدار نگه دارد. مهم‌تر از همه، همتی اذعان کرد که صادرات نفت ایران تقریباً متوقف شده و کشور با کمبود ارز، هزینه‌های بازسازی و افزایش بیکاری جوانان مواجه است.
این اظهارات را می‌توان نشانه‌ای از شکل‌گیری یک کارزار هماهنگ در بخش میانه رو جمهوری اسلامی برای مهندسی افکار عمومی جامعه ایرانی در جهت باز کردن دوباره باب دیپلماسی و فاصله گرفتن از فضای پرتنش کنونی ارزیابی کرد.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20099" target="_blank">📅 12:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20098">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بالایی قرار دارد و پیش بینی می شود طلا یک اصلاح نزولی دستکم در حد 300 الی 500 پیپ داشته باشد.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/20098" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20097">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4df224890.mp4?token=S5qtbrdFLqIAhMHVBwZstDBx7VdQybK8whfNENFQ1c74m73qxfHVweHk8B-qdsvYsEf1QQZlXV3IeLxwKoNZ1JC58WoV76A7AKke_6aNHyYL-hwYBb889FwXHOJj7CCLKRCA6dBMkEunrv_kR3LoYWG8oblNx3d2OdT8LziHhX_4_SLdbC_9ged2VS2QBNZRbPD0tNIs1L3HbIkmGQKev7ar4CO4j7L47A5r-5pkX1gT78F1XRw_gbtTL-vXD535Idku-5iPvH-VPvpoIn7c6y8IQ3FT07g_4bs_z8lyQiplb2VhdK0TdM5QW7eRinImuj2XwVr3iESKxiN-JqTrtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4df224890.mp4?token=S5qtbrdFLqIAhMHVBwZstDBx7VdQybK8whfNENFQ1c74m73qxfHVweHk8B-qdsvYsEf1QQZlXV3IeLxwKoNZ1JC58WoV76A7AKke_6aNHyYL-hwYBb889FwXHOJj7CCLKRCA6dBMkEunrv_kR3LoYWG8oblNx3d2OdT8LziHhX_4_SLdbC_9ged2VS2QBNZRbPD0tNIs1L3HbIkmGQKev7ar4CO4j7L47A5r-5pkX1gT78F1XRw_gbtTL-vXD535Idku-5iPvH-VPvpoIn7c6y8IQ3FT07g_4bs_z8lyQiplb2VhdK0TdM5QW7eRinImuj2XwVr3iESKxiN-JqTrtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20097" target="_blank">📅 11:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20096">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مدیرعامل شرکت نفت ستاره خلیج فارس از عملیاتی‌شدن استفاده از متانول به‌عنوان جزء اکسیژنه در ترکیب بنزین تولیدی این پالایشگاه خبر داد.   این تغییر می‌تواند برای بخشی از خودروهای موجود در بازار، به‌ویژه قطعات لاستیکی و پلاستیکی مسیر سوخت، ریسک فرسودگی زودرس ایجاد…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20096" target="_blank">📅 11:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20095">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مدیرعامل شرکت نفت ستاره خلیج فارس از عملیاتی‌شدن استفاده از متانول به‌عنوان جزء اکسیژنه در ترکیب بنزین تولیدی این پالایشگاه خبر داد.
این تغییر می‌تواند برای بخشی از خودروهای موجود در بازار، به‌ویژه قطعات لاستیکی و پلاستیکی مسیر سوخت، ریسک فرسودگی زودرس ایجاد کند.
به گزارش شبکه اطلاع‌رسانی طلا و ارز، مدیرعامل شرکت نفت ستاره خلیج فارس روز جمعه ۳۰ مرداد ۱۴۰۵ (۲۱ آگوست ۲۰۲۶ (۳۰ مرداد ۱۴۰۵)) از
افزودن متانول به بنزین
تولیدی این پالایشگاه خبر داد. به گفته او متانول در حال حاضر به‌عنوان یکی از اجزای اکسیژنه در ترکیب سوخت مصرفی خودروها به‌کار گرفته می‌شود.
اکسیژنه‌ها ترکیباتی هستند که به
بنزین
اضافه می‌شوند تا احتراق کامل‌تر شود و عدد اکتان سوخت افزایش پیدا کند. عدد اکتان بالاتر یعنی سوخت در برابر خودسوزی زودهنگام در موتور مقاوم‌تر است؛ همین ویژگی باعث می‌شود پالایشگاه‌ها از این نوع افزودنی‌ها به‌جای ترکیبات گران‌تر مانند MTBE استفاده کنند.
چرا متانول نگران‌کننده است؟
متانول
برخلاف بسیاری از افزودنی‌های رایج، خاصیت خورندگی بیشتری روی قطعات لاستیکی و پلاستیکی سامانه سوخت‌رسانی دارد. اورینگ‌ها، شیلنگ‌های سوخت، دیافراگم پمپ بنزین و برخی مخازن پلاستیکی از جمله قطعاتی هستند که در تماس طولانی‌مدت با متانول، سریع‌تر از حد معمول فرسوده می‌شوند. نتیجه عملی برای مالک خودرو، احتمال نشتی سوخت یا کاهش عمر همین قطعات و افزایش هزینه تعمیر است.
کدام خودروها بیشتر در معرض‌اند؟
خودروهایی که سامانه سوخت‌رسانی آن‌ها برای درصد بالای الکل یا متانول طراحی نشده، بیشترین آسیب‌پذیری را دارند. این گروه شامل بخشی از خودروهای مدل پایین‌تر و برخی خودروهای وارداتی قدیمی‌تر می‌شود که استانداردهای سوخت انعطاف‌پذیر (فلکس‌فیوئل) در آن‌ها رعایت نشده است. خودروهای جدیدتر با قطعات مقاوم به الکل معمولاً ریسک کمتری دارند.
مدیرعامل
ستاره خلیج فارس
تأکید کرده است که درصد متانول در ترکیب بنزین در چارچوب استانداردهای مصوب کنترل می‌شود. با این حال، جزئیات دقیق درباره سهم متانول در هر لیتر بنزین و نظارت مستمر بر کیفیت آن، اطلاعاتی است که مصرف‌کننده هنوز به‌طور شفاف در اختیار ندارد.
استفاده از افزودنی‌های داخلی به‌جای واردات ترکیبات اکسیژنه، برای پالایشگاه‌ها از نظر اقتصادی مقرون‌به‌صرفه‌تر تمام می‌شود. این رویکرد در سال‌های اخیر در چند کشور دیگر نیز با هدف کاهش وابستگی به واردات آزمایش شده، اما همواره با هشدارهای فنی درباره سازگاری آن با ناوگان خودرویی موجود همراه بوده است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20095" target="_blank">📅 11:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20094">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این موشک های دوش پرتاب حرارتی صرفا برای زدن بالگردها، پهپادها و هواپیماهایی که در ارتفاع پایین پرواز می‌کنند مناسب هستند.  به نظر می‌رسد هدف از تسلیح ایران به این سلاح ها، ایجاد فرسایش در نیروهای آمریکایی است که محتملا در حمله زمینی به جنوب ایران درگیر خواهندشد.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20094" target="_blank">📅 10:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20093">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ:  آیا تا به حال کمونیست شاد دیده‌اید؟  آیا تا به حال دیده‌اید که یک کمونیست بخندد؟ من هرگز چنین چیزی ندیده‌ام. من با کمونیست‌ها آشنا بوده‌ام. آن‌ها افراد بسیار ناراحتی هستند.  ما می‌خواهیم شاد باشیم!</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20093" target="_blank">📅 03:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20092">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ:
آیا تا به حال کمونیست شاد دیده‌اید؟
آیا تا به حال دیده‌اید که یک کمونیست بخندد؟ من هرگز چنین چیزی ندیده‌ام. من با کمونیست‌ها آشنا بوده‌ام. آن‌ها افراد بسیار ناراحتی هستند.
ما می‌خواهیم شاد باشیم!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20092" target="_blank">📅 03:24 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20091">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سفیر ایالات متحده در ترکیه، تام باراک:  اسرائیل هنوز جولان را در اشغال خود دارد، برخلاف قطعنامه‌های سازمان ملل، برخلاف کل نظم بین‌المللی که جولان را متعلق به سوریه می‌داند.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20091" target="_blank">📅 03:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20090">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سفرای ترامپ مثل خودش متناقض حرف می زنند.  سفیر ترامپ در ترکیه یعنی تام باراک از اسرائیل شدیداً انتقاد کرده بود اما سفیر او در اسرائیل اینطوری قضیه را ماست مالی می کند.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20090" target="_blank">📅 03:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20089">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سفرای ترامپ مثل خودش متناقض حرف می زنند.  سفیر ترامپ در ترکیه یعنی تام باراک از اسرائیل شدیداً انتقاد کرده بود اما سفیر او در اسرائیل اینطوری قضیه را ماست مالی می کند.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20089" target="_blank">📅 03:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20088">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ درباره ایران:
نمی‌دانم با چه کسی در ایران مذاکره کنم. این واقعاً یکی از بزرگ‌ترین مشکلات من است.
هیچ‌کس نمی‌خواهد رئیس‌جمهور ایران باشد. می‌گویند: «چه کسی می‌خواهد رئیس‌جمهور باشد؟» «نه، نه، من نمی‌خواهم رئیس‌جمهور باشم.»</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20088" target="_blank">📅 03:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20087">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارشگر: با توجه به اینکه ایران به سمت جنگ اقتصادی پیش می‌رود، آیا این بدان معناست که گزینه‌های نظامی برای ایالات متحده محدود شده است؟
ترامپ: خیر، اصلاً.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20087" target="_blank">📅 00:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20086">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">روسیه برای اولین بار در بیش از یک دهه، هیچ کشتی جنگی در مدیترانه ندارد، زیرا مسکو کشتی‌ها را برای محافظت از تانکرهای نفتی تحریم‌شده از دستگیری توسط ناتو منحرف کرده است.
منبع: تلگراف</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20086" target="_blank">📅 21:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20085">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نماینده مجلس  ابراهیم عزیزی:
آمریکایی‌ها ثابت کرده‌اند که زبان دیپلماسی را درک نمی‌کنند، بنابراین نه تحریم‌ها را برمی‌دارند، نه منابع را آزاد می‌کنند و نه به دزدی دریایی در دریاها پایان می‌دهند.
اما تاریخ نشان خواهد داد که با زبان قدرت، نه تنها به این اقدامات مجبور خواهند شد، بلکه منطقه را با عذرخواهی از ملت بزرگ ایران ترک خواهند کرد.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20085" target="_blank">📅 19:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20084">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">افزایش تنش ها میان اسرائیل  و ترکیه    دولت ترکیه حکم بازداشت نتانیاهو را صادر کرد.  دولت ترکیه درخواست صدور اعلان قرمز اینترپل را برای بنیامین نتانیاهو  به دلیل جرایم علیه فعالان ناوگان جهانی "صمود"، از جمله جنایات علیه بشریت و نسل‌کشی، صادر کرده است.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20084" target="_blank">📅 18:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20083">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اظهارات  هاکابی، سفیر آمریکا در اسرائیل، درباره حملات اسرائیل به سوریه:  به نظر من این کار عمدی نبود. اگر به آنچه واقعاً اتفاق افتاد نگاه کنید، تعدادی از مهمات در یک فرودگاه قرار داده شدند. هیچ تلفاتی نداشت.  به نظر من، این بیشتر یک هشدار بود تا تلاشی برای…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20083" target="_blank">📅 16:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20082">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اظهارات  هاکابی، سفیر آمریکا در اسرائیل، درباره حملات اسرائیل به سوریه:
به نظر من این کار عمدی نبود. اگر به آنچه واقعاً اتفاق افتاد نگاه کنید، تعدادی از مهمات در یک فرودگاه قرار داده شدند. هیچ تلفاتی نداشت.
به نظر من، این بیشتر یک هشدار بود تا تلاشی برای ایجاد تنش.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20082" target="_blank">📅 16:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20081">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اخبار تاییدنشده از حرکت انبوه نیروهای زرهی و توپخانه ترکیه به سمت سوریه</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20081" target="_blank">📅 16:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20080">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترکها در ظاهر می گویند اردوغان موفق شده ترامپ را متقاعد کند تا از این طرح جلوگیری کند اما به نظرم این پلن A شان بوده و پلن B شان شامل ورود مستقیم نظامی به ایران همراه باکو برای اشغال شمال غربی ایران بوده که پیشتر اشاره کرده بودم.  در هر صورت، در راند بعدی…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20080" target="_blank">📅 16:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20079">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دولت باغچلی، سیاستمدار ملی‌گرای ترکیه، نسبت به حمله هوایی اسرائیل به پایگاه هوایی در سوریه، هشدار شدیدی صادر کرد:  وقتی ملت ترکیه قیام می‌کند، هیچ نیرویی نمی‌تواند در برابر آن مقاومت کند.  ترکیه، کشوری نیست که در برابر حملات به حقوق حاکمیتی خود، منفعلانه عمل…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20079" target="_blank">📅 15:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20078">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-text">🔥
نفت ایران در بازار چین کمیاب شد و تخفیف منفی!
🔹
رویترز: پیشنهادهای فروش نفت ایران به خریداران چینی کاهش و قیمت محموله‌ها افزایش یافته.
🔹
برخی محموله‌های ایران به‌جای تخفیف معمول، با قیمت بالاتر از شاخص برنت عرضه می‌شوند.
🔹
صادرات نفت ایران در ماه جاری به ۵۳۴ هزار بشکه کاهش یافته؛ در حالی که میانگین صادرات در سال گذشته ۱.۴ میلیون بشکه بوده.
🔹
همچنین ذخایر نفت ایران روی آب از ۱۰۵ به حدود ۸۰ میلیون بشکه کاهش یافته و پالایشگاه‌های مستقل چین برای تأمین خوراک به دنبال نفت جایگزین از کشورهایی مانند عراق و برزیل هستند.
@khate_energy</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20078" target="_blank">📅 14:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20077">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zj5Cs8_pshGDiE1OwRLMFuzZYGN6Fp9zV-8lxVrA6VAd9dm0JmcD8QvRqkqQw8xktgyUwwhVObrU7hCI5XI5wvB4kJcN92dvdd80HDJTNFSV77oFSHUTtLAuWpRIdPB93LBw2cydZ7t6wZQ2Bqw95xuAsCdftA3-1NbW5yCnhMQT8DK-LxDBvvGCHc0SsGsLFRiy5pi6SJ-3K3Oi4koI414EAwfe5BUlm0JMLPPgQRWgb5jTCOXpwlPi8vBHJ-THjImLFGTcqs1XLV8Rd-4o3ekp0BNwvpUgsI4kbQk4Ne9zIvbzlabH4EZNWDAIlCDdPExSJ5_rv5IrArW_X_9M-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعات استخباراتی اسرائیل حاکی از آن است که ترکیه در حال آماده‌سازی برای ارسال سلاح‌های تهاجمی و دفاعی به سوریه، از جمله سامانه‌های پیشرفته دفاع هوایی، است</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20077" target="_blank">📅 13:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20076">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTQdP6G3ixK-aYKQoAUNCy86jMAl1IRtjInkfcFCwSwAF0iJ1FInXUsSq1mg8vTblUxr1o0jdLptMewg42CEio9APE5gssPDd34XlDQ5ba0vYrVKiGPP2dB_K_STqduCG1ubZy_VRz-nLHB2wxei8_anIUIEPfwRQVfa1hVKdivEZj5wUm0AphAql6vGFbKd-br5xemCjBopB6v4_x7iICx4AFelAuv2SjBuuWtX-rYbiDDnAhjAcgvmsvUMCOYeJJR6pHbNAtHjNLgXGJl36clH-nMlNai7bKYJrzv6OjJTs2qN3v8AdgIqfqQkHLlUk8o5iptx1T31gqSdrl0iYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بالایی قرار دارد و پیش بینی می شود طلا یک اصلاح نزولی دستکم در حد 300 الی 500 پیپ داشته باشد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20076" target="_blank">📅 13:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20075">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">– طبق گزارش رویترز با استناد به داده‌های کپلر، تعداد کشتی‌هایی که از تنگه هرمز عبور می‌کنند همچنان در محدوده تک‌رقمی است.
فقط ۷ کشتی در روز پنجشنبه از تنگه عبور کردند که ۴ کشتی وارد و ۳ کشتی خارج شدند. برخی از این کشتی‌ها از مسیر ایران استفاده کردند، از جمله یک کشتی بزرگ حمل گاز. هیچ کشتی بسیار بزرگ حمل نفت خام (VLCC) در هیچ‌جا دیده نشد.
ترافیک در تنگه بابرالمندب نیز کند شده است؛ به طوری که تنها ۲۳ کشتی در روز پنجشنبه عبور کردند، در حالی که این عدد در روزهای سه‌شنبه و چهارشنبه ۳۴ کشتی بود.
این در حالی است که ترامپ و اکسیوس ادعا کرده‌اند که روزانه ده‌ها میلیون بشکه نفت با هدایت ایالات متحده از تنگه عبور کرده و به بازارهای جهانی رسیده است.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20075" target="_blank">📅 09:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20074">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">- یک مقام ارشد ایرانی اظهار داشت که ایران در حال آماده شدن برای آسیب رساندن به ریاست جمهوری ترامپ از طریق جنگ اقتصادی است، با هدف اینکه او در انتخابات میان‌دوره‌ای نوامبر شکست بخورد.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20074" target="_blank">📅 08:56 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
