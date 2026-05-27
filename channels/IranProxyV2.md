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
<img src="https://cdn4.telesco.pe/file/stJz97vneS5eqPgSMRq50ojLF_tKflX9pUd-q6YKeKn3_K2UM_uCIhZSrxN4Ju6b64sGdy-ZodBXx4snqqCG8TqobfNr7fNoP1OkuCfg42Q92gCNaX9TqmUl4Zx1tOc9wkgZYSxV7R-xiW26W8Zd7_tG6CEdRlsEKFgUBqXQv9G3CVukSACDA0MXQg5uxc87tpXF0Rd7U7y7dxhzMax2afcPulptshM342Yhb4ThMBtPJunyG-frzDpiwAJp2CHr6sRDa3iagmM2CZF7UZjMZWbr2aJKKKCwhnUNXicyobYejQ8uAUD61ML_eE4WoLSE4_pyfkXnnVPuFHeWFJunKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 40.6K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 23:32:33</div>
<hr>

<div class="tg-post" id="msg-8602">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺(2).ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8602" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
کانفیگ های جدید اختصاصی OpenVPN
با حجم و اعتبار نامحدود
🏅
تست شده روی ایرانسل، رایتل، شاتل، سامانتل(برخی نقاط ممکنه متصل نشه)
💥
بدون نیاز به یوزر پسورد
برای اتصال در تمام سیستم عامل ها کافیه روی کانفیگ کلیک کنید و برنامه OpenVPN را انتخاب کنید، یوزرنیم و پسورد را ست کنید و متصل شوید یا کانفیگ را سیو کنید و از داخل برنامه ایمپورت کنید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/IranProxyV2/8602" target="_blank">📅 23:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8601">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/IranProxyV2/8601" target="_blank">📅 22:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8600">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/IranProxyV2/8600" target="_blank">📅 21:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8599">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/IranProxyV2/8599" target="_blank">📅 21:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8598">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/IranProxyV2/8598" target="_blank">📅 21:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8597">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺(1).ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8597" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ های جدید اختصاصی OpenVPN با حجم و اعتبار نامحدود
تست شده روی ایرانسل، رایتل، شاتل، سامانتل(برخی نقاط ممکنه متصل نشه)
بدون نیاز به یوزر پسورد
📍
آموزش اتصال تصویری
برای اتصال در تمام سیستم عامل ها کافیه روی کانفیگ کلیک کنید و برنامه OpenVPN را انتخاب کنید، یوزرنیم و پسورد را ست کنید و متصل شوید یا کانفیگ را سیو کنید و از داخل برنامه ایمپورت کنید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/IranProxyV2/8597" target="_blank">📅 20:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8592">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❤
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/IranProxyV2/8592" target="_blank">📅 19:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8591">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
ترامپ درباره ایران:
آنها می‌گویند که بسیار تمایل دارند که به توافق برسند.
تا کنون به آن نرسیده‌اند. ما از این وضعیت راضی نیستیم، اما یا راضی خواهیم شد، یا اینکه باید کار را تمام کنیم.
آنها در حال مذاکره با جدیت بسیار کم هستند.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/IranProxyV2/8591" target="_blank">📅 19:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8590">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
ترامپ: ایران حتی اگه اورانیوم های خودشو هم تحویل بده هیچ خبری از کاهش و لغو تحریم ها نیست
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/IranProxyV2/8590" target="_blank">📅 19:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8589">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پروکسی‌های متصل
♥️
https://t.me/proxy?server=49.13.35.164&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=mt.corph.ru&port=443&secret=dd2ed7517b077ef414e24b106e0729335d
https://t.me/proxy?server=free-mtproto.flexiblenet.org&port=443&secret=4da47f00c2291d55696fa3ae954ffd78
https://t.me/proxy?server=ams1.tlgfast.com&port=443&secret=083fe0c452e2407d835537872f097c54
https://t.me/proxy?server=91.107.182.200&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=176.65.131.45&port=25565&secret=79e344818749bd7ac519130220c25d09
https://t.me/proxy?server=91.107.174.85&port=8443&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/IranProxyV2/8589" target="_blank">📅 19:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8588">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">https://t.me/proxy?server=87.248.129.129&port=15&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d
پروکسی متصل سرعت قوی
❤️‍🔥
⚡️
👀
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/IranProxyV2/8588" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8587">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اینترنت بین الملل در حال قطع؟
نت‌بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPN ها هستند. کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPN ها می‌باشد.
تندروها کار خودشونو کردن واسه همینه خیلیا نمیتونن وصل شن یا سرعت افتضاحه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/IranProxyV2/8587" target="_blank">📅 19:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8586">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epSlUDPbytBX2wCjqkup3ggjlLDUzcOu8Vsn1fvDmV9FNMLWWqVCU88wezvyQnfbHwqsNZuwHvPM8-RKedRUOus74pQBorlSzYhvxvf9QA_nX2-u7OT6I-dnNVceXWQRbssomO9nnasp9gt3dlizGJEwCpbv6SL0Vf_HRPrGFxCyPbr2IrvjGvNB8fJaNHTxFI4KfuGzqDce071Nr2ikHFqLLdIiNPDr45w5xF3VPLWoHn_Zb7SlewG1cxxVTF--GIh_zkq-HvTYB9gAF2k84Xrz3ZADOmAltFK57YWMMvb5ULEXWAmx26_RSwRWdDBvTtbi69viJXmBCIQgyutcUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که سفارش ثبت کردید تو ربات، دارم یسری آپدیت رو سرورا میدم، صبور باشید، اوکی شد همینجا اطلاع میدم و سفارشتونم تایید میکنم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/IranProxyV2/8586" target="_blank">📅 18:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8585">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❤️
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/IranProxyV2/8585" target="_blank">📅 16:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8584">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">این لیست پروکسی اختصاصی رو داشته باشید باید با خیلی از اینترنت ها اوکی باشه
پروکسی اول
پروکسی دوم
پروکسی سوم
پروکسی چهارم
پروکسی پنجم
پروکسی ششم
پروکسی هفتم
پروکسی هشتم
پروکسی نهم
پروکسی دهم
پروکسی یازدهم
پروکسی دوازدهم
پروکسی سیزدهم
بفرستید برای دوستانی که نیاز دارند، وصل بشن
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/IranProxyV2/8584" target="_blank">📅 15:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8583">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">vless://406d8436-0eb9-4eb2-84fb-960e076ffba6@162.159.38.183:2083?mode=stream-one&path=%2Fde&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=de.lezzatzone.ir&fp=chrome&type=xhttp&allowInsecure=0&sni=de.lezzatzone.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
همراه اول تست زدم، اوکی بود، مابقی نت هارو خودتون تست بزنید
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/IranProxyV2/8583" target="_blank">📅 15:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8582">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKcxbJ93qP-PsbWtI1JWURoeJLQBkrEVCcSIrlvWSEjPGDwibxRQTr12CoFoY5qUGw64lo9dwbeoFaybZuko2OoZATJm2zsnFq4S53ucY3HtvAM93Ps3ufm40gqGrl8-Lha8fSVvjUOPLUiDIlKjUVvDUUumYCR6AxRif0bMfzixyZpXu2ql1fK9iRkds45UukhzYo0dFzQLxqE-s-9P8UsGi1S_jO_JsqWlvRjhNf8sL0HCKdJW6zq2x9qWo2j3-4OEz8tKOOn7y5lyGukNlbUf9-NWN12OyAox_b0zwUtm6dUYIXTVe9n9l21OEMCWQHxunS2ltr8dkZDy-NaCRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همراه اول بعد از اعتراض کسانی که اینترنت  پرو خریدن و گیگی 40 هزارتومن بابتش پول دادن اعلام کرد در صورت تمایل میتونن  اینترنت خودشونو به حالت قبل برگردونن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/IranProxyV2/8582" target="_blank">📅 15:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8581">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o5-y09N8S7c8P4W7Q8VGX2hqZItAAXVEW3kR4DQBfcmOQ-0OMBwMHUkG4T-5t8DS3VdPdr2gyjo0fvUdY6E0RUbbl4LVgN19ssxuiDAv6UH15rD1jEwP1spsStymTe5z519EM6wkiitqfD4Rih9ZumdL_Mft8U1sPvhzd1fGmSygf9dyudZT3bea4rwUFcOAZfC-YDiRfWSCRtp4-vWGMnuKCR0_uK-uP40iv24fBwQjO7KzboCfr0dXVqT0nHZC8l4jE9-CwfZIxZSnSsPg8Nkz94LG-IKAUjr81wyYPgBfil0iBpdOgbR8jO2MK0IGqs_aCi7-X2Gr5idzPAEHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آخوند حمید رسایی: از وقتی اینترنت وصل شده قلبم درد گرفته، یه لحظه‌ام نتونستم بخوابم
.
وصل شدن اینترنت پایمال کردن خون رهبر شهیدمونه، با اینکار تن رهبری تو گور لرزید.
عوامل موساد باعث بازگشایی اینترنت شدن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/IranProxyV2/8581" target="_blank">📅 15:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8580">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">vless://406d8436-0eb9-4eb2-84fb-960e076ffba6@162.159.38.183:2083?encryption=none&type=xhttp&security=tls&path=%2Fde&host=de.lezzatzone.ir&mode=stream-one&sni=de.lezzatzone.ir&alpn=h2%2Chttp%2F1.1&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو همراه اول تست شده اوکیه
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/IranProxyV2/8580" target="_blank">📅 15:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8579">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🟢
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/IranProxyV2/8579" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8578">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🟢
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/IranProxyV2/8578" target="_blank">📅 13:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8577">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">vless://900ca7c5-6c69-4536-b0f8-efa4e3976016@51.79.89.68:443?security=&encryption=none&headerType=none&type=tcp#@V2rayngSeven
vless://ae0dd58e-e222-40bf-84ae-365a97532737@104.17.150.224:443?path=%2Falbum%2Fbt&security=tls&encryption=none&insecure=0&host=pagescm.freen15.cc.cd&type=ws&allowInsecure=0&sni=pagescm.freen15.cc.cd#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
وصله منطقه ای، تست بزنید کمی صبرکنید وصل میشه براتون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/IranProxyV2/8577" target="_blank">📅 12:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8576">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">Proxy
✅
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ%3D%3D
Proxy
✅
https://t.me/proxy?server=ui.geodns.info.&port=4455&secret=7nnjRIGHSb16xRkTAiDCXQk%3D
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/IranProxyV2/8576" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8575">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🟢
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/IranProxyV2/8575" target="_blank">📅 12:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8574">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🟢
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/IranProxyV2/8574" target="_blank">📅 12:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8566">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">DE🇩🇪- SpEeD🧨.ovpn</div>
  <div class="tg-doc-extra">3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8566" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ های OPEN VPN
❤️
🕖
اعتبار : 30 روز
🌐
لوکیشن :
🇨🇵
🇩🇪
🇬🇧
👉
بدون محدودیت حجمی
🔋
تست شده و متصل  - روی ایرانسل
🟡
📧
Username:
SDPXCQLdnbnQiGi
🔑
Pass:
@SoonTeam
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/IranProxyV2/8566" target="_blank">📅 12:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8565">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوستانی که سفارش ثبت کردید تو ربات، دارم یسری آپدیت رو سرورا میدم، صبور باشید، اوکی شد همینجا اطلاع میدم و سفارشتونم تایید میکنم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/IranProxyV2/8565" target="_blank">📅 12:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8564">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">https://t.me/proxy?server=78.47.67.183&port=8443&secret=dd104462821249bd7ac519130220c25d09
این هم یه پروکسی دیگه، بدون فیلتر وصل بشین، فور کنید برای دوستاتون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/IranProxyV2/8564" target="_blank">📅 11:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8563">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺بمب.npvt</div>
  <div class="tg-doc-extra">4.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8563" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/IranProxyV2/8563" target="_blank">📅 11:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8562">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺.npvt</div>
  <div class="tg-doc-extra">4.2 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8562" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/IranProxyV2/8562" target="_blank">📅 11:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8561">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnuPqwJTNioBKL8STdws7nbdgsYFocg8m5BPLBmYiUvBg1quYH4gYehp-TxGyKwfHbS3pz5DfeLVQFp1n_DzFs7U04j85x9HExIiAyjS7mBWTDZCugANvZJTvd8a7ifwAnLdxeEYKJy8_68giuQ4NN0O997zW7fiZKNkSvhZLlUXUUjgaw-vogPxCCUTildw9M31-4cAhzu4-3ergRUSPoPE8XHgGuY02G91wfkWfhdFcmhJBx6itwke5BQtWGx10R0aMIBkiXE0eTOJj-E7E1feGbGFhBhWonNyDBbHBF3UHgLZogT92sAcvnspKzCOKAdjAwRT8wiZCUnnyZ2sjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">البته طبق داده‌های شرکت پایش اینترنت Kentik، که اطلاعات دقیقتری رو ارائه میده، میزان اتصال اینترنت کشور هنوز پایین هست و کماکان به وضعیت اینترنت قبل از دی ماه نرسیده.  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/IranProxyV2/8561" target="_blank">📅 11:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8560">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWSBlJu8MnfiOAvoNBdAyiPtgfRcyniOO4AM_hNJkgAe3MPKBuZHvaWJDKzpbihCj9aZfdmR6NO0NjHLQYK9JOYbPLN2kQ7WxJTfVwkBLQUxyJh-GtGDbriSk2AzPVcWCAuEeebZmPpVFofoPYMt8qSi04bevNL9mZArRcDEe9kRnUNVCoq0-5wVfY4WPNZXyynP7vqFwqwdHTS7kjJukMpMGmF628s-hdOZcOz9TqShFKpfBh5IdQ4IVZ2KfhkfPYYtdGkx7VNiMQFMMKn7pTUz5eTXFi45whe51_ObdEzJHTOCNc8EEWCMiEytJOIX5v8HRGLv2CCB14UheUsr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/IranProxyV2/8560" target="_blank">📅 08:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8559">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">فول وصل🔥.npvt</div>
  <div class="tg-doc-extra">22.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8559" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/IranProxyV2/8559" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8558">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chwnOV9sbbAgvFBpkXXAnnzRbjx17v63RhHfhHWzaasawT0878N0UXKEoA_jpTR35mpIPuLytSKlssI-qsSHJOTj182jAWw4cVsivVDQPDRNlcMOi4m4ZKrQiYBEQS0wmsORKH91m8553eD2OOwIi7n6B8Ao-7FodCse2-0DrxvGa8xmw-IgKhcrWHMsCgt-_WdobPBI_58zBdNTO7Jm_Ka-0HPUmm5W1QLKCtPEVKmt-f5YtIwlA5lwLyPtqYKbB42ez12Lpb9FJje9Zj7rFJsZidac_cM9GMIAAtoqsGA7Mn4fUqCLJ0pN81tmE9VFb_5suD_6qdhnW-6TyTAbaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رس
ایی: عوامل موساد دستور باز کردن اینترنت رو دادن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/IranProxyV2/8558" target="_blank">📅 08:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8557">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">https://t.me/proxy?server=ams1.tlgfast.com&port=443&secret=083fe0c452e2407d835537872f097c54
این پروکسی هم بدون فیلتر بزنید روش وصل میشه، استفاده کنید، فور کنید برا رفقاتون
❤️
😁
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8557" target="_blank">📅 01:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8556">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🇱🇷.npvt</div>
  <div class="tg-doc-extra">1.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8556" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">رو اکثر اپراتورها وصله، فور بزنید واسه دوستاتون
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/IranProxyV2/8556" target="_blank">📅 01:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8555">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
کارشناس صداسیما :
وصل شدن اینترنت متوقف میشه و دستور رییس جمهور اجرا نمیشه چون خلاف دیوان عالیه.
😐
😐
😐
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/IranProxyV2/8555" target="_blank">📅 01:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8554">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ED2mHFXgLsfpKLQUrQhSlzH9e2mXwkFGNNq5W4fJxx8p_PMVMOBhtgPbqYjY1Hw0nabVU_uqAbEycFEAQmimfKh5gadXSTqtbhBGoO0GO8kabNi1xmVTdP-rDhK27VIOhs-Hks9guWt9M5yDV8cdgCSy3_jiOLQ6-xpOoqlI0fe2Jj6NF0i9A25h2D8ITxXRQIFsZpceoZPyQQHq8Z8xaLfP78dgOyjZ7CUQ0Lrt4kt0ekuU-E3ITmMecXB6CZ7XxGLdyqgX92uHAJXiHDFyR_E7YTr3MPLt0hwLWFVaL01CMIPyoz0DkyRrPl0VLvJ5BAwoU3FngGJEJrTqEGMAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">البته طبق داده‌های شرکت پایش اینترنت Kentik، که اطلاعات دقیقتری رو ارائه میده، میزان اتصال اینترنت کشور هنوز پایین هست و کماکان به وضعیت اینترنت قبل از دی ماه نرسیده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/IranProxyV2/8554" target="_blank">📅 01:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8553">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@172.64.152.23:2096?encryption=none&type=ws&security=tls&path=%2F%3FTelegram%25F0%259F%2587%25A8%25F0%259F%2587%25B3%2540WangCai2%3D&host=sni.jpmj.dev&sni=sni.jpmj.dev&allowInsecure=1#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA…</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/IranProxyV2/8553" target="_blank">📅 00:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8552">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@172.64.152.23:2096?encryption=none&type=ws&security=tls&path=%2F%3FTelegram%25F0%259F%2587%25A8%25F0%259F%2587%25B3%2540WangCai2%3D&host=sni.jpmj.dev&sni=sni.jpmj.dev&allowInsecure=1#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
https://t.me/proxy?server=178.105.241.184&port=443&secret=99902e5742bd34a3f26434fadf88cde3
سرور وارد کنید، و بعد به پروکسی متصل بشید بصورت ترکیبی، رو همه اپراتور ها اوکیه، فور کنید دوستاتونم استفاده کنن
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/IranProxyV2/8552" target="_blank">📅 00:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8551">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📣
دوستان، سرعت جوریه که نت قطع بود، سرعت بهتر بود
😐
😂
📌
درضمن، اینکه سرعت سرورهای تانل ربات پایینه نگران نباشید، برای همه به همین صورته و اختلاله کلا تو کل کشور ، حل میشه ، ولی خب پایداره و وصله، خواستین تهیه کنید تو ربات سفارشتونو ثبت کنید
🏅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/IranProxyV2/8551" target="_blank">📅 23:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8550">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">https://t.me/proxy?server=ams1.tlgfast.com&port=443&secret=083fe0c452e2407d835537872f097c54
این پروکسی هم بدون فیلتر بزنید روش وصل میشه، استفاده کنید، فور کنید برا رفقاتون
❤️
😁
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/IranProxyV2/8550" target="_blank">📅 23:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8549">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">vless://b64ced11-143e-4ded-a985-a8de25461061@3.27.234.120:51808?security=reality&encryption=none&pbk=XHnwfyEySdx57QT_8P_7vDVFzdLHO4tO9BQOsHxxlEk&headerType=none&fp=firefox&type=tcp&flow=xtls-rprx-vision&sni=yahoo.com&sid=8810c789eea55c28#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
متصل به همه اپراتور ها، بفرستین واسه دوستاتون هم اونا وصل شن، هم از ما حمایت ریزی بشه
❤️
🍸
😁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/IranProxyV2/8549" target="_blank">📅 23:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8548">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">vless://28154b7e-afc2-449b-8a78-bf1eba31bd05@a.darafiq.ir:8880?path=%2F&security=none&encryption=none&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
متصل با همه اپراتور ها، فور نکنید حمایت نشه حلال نیستا
😁
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/IranProxyV2/8548" target="_blank">📅 23:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8547">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">۲ تا کانفیگ دیگ هم ساختم، رو یکی نباشین مختلف بزنید که سرعتشون نیاد پایین یا قطع نشن
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/IranProxyV2/8547" target="_blank">📅 23:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8546">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">vless://abe09a99-7346-4c5b-9476-16774c032ae7@104.16.89.120:443?path=%2FTelegram-%40IranianMinds&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=1&fp=chrome&type=ws&allowInsecure=1&sni=mcia.po2pco.top#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رایگان جدید رو همه اپراتور ها وصله، استفاده کنید بزنید، فور کنید برای دوستاتون چنلو داشته باشن، حمایتتتت
😁
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/IranProxyV2/8546" target="_blank">📅 22:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8545">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">vless://e8cbc051-e0ac-452d-9bd3-8ad46625573c@arvancloud.ir:8080?mode=auto&path=%2F&security=none&encryption=none&host=r.cafeplusstore.ir&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA  رو آرون کلاد هم براتون ساختم
😂
، این برا خودم سرعتش بهتره، تست بزنید،…</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/IranProxyV2/8545" target="_blank">📅 22:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8544">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">vless://e8cbc051-e0ac-452d-9bd3-8ad46625573c@arvancloud.ir:8080?mode=auto&path=%2F&security=none&encryption=none&host=r.cafeplusstore.ir&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA  رو آرون کلاد هم براتون ساختم
😂
، این برا خودم سرعتش بهتره، تست بزنید،…</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/IranProxyV2/8544" target="_blank">📅 21:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8543">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/495efbf3a1.mp4?token=PRnxk8cii9JCL5mhBpWY06Bkq-HMv39orKSU2MsU7B6PBFfzGSY33L7by1YNyZYq7LyjgutrogkVU87nkXjRGHRTvQo3wLo-SehuU2mS1FJDTm14NK27Mf5keaT8t9Lyfx5QpEJUffiaspZ3mqbMSNzvXpqVkW96Q3qwIOAa5v9tQsAspeG080PfN1bBUfGoB67ZPYouEhnktihDaVZS-1y4KjCiF6w7YUbx0tfmBLlIM1KVeFNvUOy16Dh2agTS0FNbFHOGtmXryifFXmjWILR9Yi5IzTwsPw_3cm4a6mQqM7pUz4Mw7eUF8Xa4yY9GeLtb0tYn9uHc8d0QNWhRRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/495efbf3a1.mp4?token=PRnxk8cii9JCL5mhBpWY06Bkq-HMv39orKSU2MsU7B6PBFfzGSY33L7by1YNyZYq7LyjgutrogkVU87nkXjRGHRTvQo3wLo-SehuU2mS1FJDTm14NK27Mf5keaT8t9Lyfx5QpEJUffiaspZ3mqbMSNzvXpqVkW96Q3qwIOAa5v9tQsAspeG080PfN1bBUfGoB67ZPYouEhnktihDaVZS-1y4KjCiF6w7YUbx0tfmBLlIM1KVeFNvUOy16Dh2agTS0FNbFHOGtmXryifFXmjWILR9Yi5IzTwsPw_3cm4a6mQqM7pUz4Mw7eUF8Xa4yY9GeLtb0tYn9uHc8d0QNWhRRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظ، خداحافظ
👋
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/IranProxyV2/8543" target="_blank">📅 21:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8542">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">vless://e8cbc051-e0ac-452d-9bd3-8ad46625573c@arvancloud.ir:8080?mode=auto&path=%2F&security=none&encryption=none&host=r.cafeplusstore.ir&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو آرون کلاد هم براتون ساختم
😂
، این برا خودم سرعتش بهتره، تست بزنید، خوشتون اومد فور کنید
🍸
😁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/IranProxyV2/8542" target="_blank">📅 21:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8541">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.7.70:2096?path=%2F&security=tls&encryption=none&insecure=1&host=sni.111000.indevs.in&type=ws&allowInsecure=1&sni=sni.111000.indevs.in#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
کانفیگ با پورت های متفاوت براتون میسازم، سعی کنید همرو تست کنید، ببینید با کدوم راحت تر هستین، حتما برای دوستاتونم بفرستید
✅
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/IranProxyV2/8541" target="_blank">📅 21:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8540">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">vless://406d8436-0eb9-4eb2-84fb-960e076ffba6@104.16.7.70:443?mode=stream-one&path=%2Fde&security=tls&encryption=none&insecure=0&fp=chrome&type=xhttp&allowInsecure=0&sni=de.xn--q9jyb4c.online#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
چند ثانیه صبرکنید وصل بشه، هنوز پهنای باند اونقدری زیاد نیست که پرسرعت وصل بشه، یادتون نره فور کنید واسه دوستاتون
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/IranProxyV2/8540" target="_blank">📅 20:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8539">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">vless://8b84b146-3405-44f2-98e4-f0ac7dbad0c0@104.17.147.22:80?mode=auto&path=%2FTelegram%40SoonTeam&security=none&encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&host=uk.im-eb.cc.&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
سرعت عالی، رو همه اپراتورها، بفرستید واسه دوستاتون وصل بشن، حجم نامحدودههههه
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/IranProxyV2/8539" target="_blank">📅 20:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8538">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">vless://48d1cb9d-bbd4-4444-b833-6720619a117e@104.16.89.120:8443?path=%2F&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=nl8.bioritalin.ir&fp=chrome&type=ws&allowInsecure=0&sni=nl8.bioritalin.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو همه اپراتور ها متصله، وصل شین لذت ببرید
✅
حجمممم نامحدودددد
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/IranProxyV2/8538" target="_blank">📅 20:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8537">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">vless://06ef598c-1555-4887-b3f9-08214a2f6792@172.64.152.23:443?path=%2F222.167.202.31%3A7443&security=tls&encryption=none&insecure=1&host=2026.hhhhh.eu.org&type=ws&allowInsecure=1&sni=2026.hhhhh.eu.org#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو تمامی اپراتور و نت های همراه وصله
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/IranProxyV2/8537" target="_blank">📅 20:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8536">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👑
اینترنت ایرانسل و همراه اوکی شد و باید فیلترشکن های رایگان برایتون وصل شده باشه
❤️
🛜
🛜
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/IranProxyV2/8536" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8535">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">vless://48d1cb9d-bbd4-4444-b833-6720619a117e@104.16.89.120:8443?path=%2F&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=nl8.bioritalin.ir&fp=chrome&type=ws&allowInsecure=0&sni=nl8.bioritalin.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو همراه اول متصله
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/IranProxyV2/8535" target="_blank">📅 20:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8534">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
اینترنت بین الملل روی خطوط همراه اول هم وصل شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/IranProxyV2/8534" target="_blank">📅 20:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8533">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کانفیگ رایگان برای وایفا
✅
vless://4493268e-2083-4a18-9c24-72c1f8f604d5@92.42.203.168:443?path=%2F&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=dl-server1.tpchat.ir&fp=chrome&type=ws&allowInsecure=0&sni=dl-server1.tpchat.ir#
%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/IranProxyV2/8533" target="_blank">📅 20:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8532">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد.  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/8532" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8531">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/IranProxyV2/8531" target="_blank">📅 20:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8530">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پروکسی وصل
✅
https://t.me/proxy?server=91.107.169.174&port=8443&secret=dd104462821249bd7ac519130220c25d09
💥
@RUSSIAPROXYY
🇷🇺
📌
آیدی فروشگاهمون
👇🏻
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/IranProxyV2/8530" target="_blank">📅 19:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8529">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">vless://fe23b0d9-ab91-4f7b-a5a4-89e4ae9b094e@www.speedtest.net:443?security=tls&sni=broken-mud-0a9a.rigacihir69.workers.dev&alpn=http/1.1&fp=chrome&type=ws&path=/eyJqdW5rIjoiZEFtaFJ6RlAiLCJwcm90b2NvbCI6InZsIiwibW9kZSI6InByb3h5aXAiLCJwYW5lbElQcyI6W119?ed%3D2560&host=broken-mud-0a9a.rigacihir69.workers.dev&encryption=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
متصله، رو وایفاها
✅
💥
@RUSSIAPROXYY
🇷🇺
📌
آیدی فروشگاهمون
👇🏻
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/IranProxyV2/8529" target="_blank">📅 19:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8528">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وزیر ارتباطات:
اینترنت همراه تا امشب وصل میشه، تا فردا اینترنت به قبل از دی برمیگرده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/IranProxyV2/8528" target="_blank">📅 19:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8527">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">📌
بزنید تو نپستر با ایرانسل تست کنید
🛜
ss://YWVzLTI1Ni1nY206WldZeVlUVTBZV1k0T0dNME5EUmhabU0xWkRRMFpqRTNNR0l5Wmpneg@ir.npvnot.com:10112#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/IranProxyV2/8527" target="_blank">📅 18:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8526">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⭕️
شرکت مخابرات: اتصال کامل اینترنت بین‌الملل مشترکان برقرار شد
🔸
کاربران سرویس‌های پهن‌باند ثابت شامل FTTH، VDSL و ADSL هم‌اکنون بدون محدودیت به شبکهٔ جهانی اینترنت متصل هستند و امکان استفاده کامل از وب‌سایت‌ها و خدمات بین‌المللی برای آن‌ها فراهم شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/IranProxyV2/8526" target="_blank">📅 18:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8525">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
آمار لحظه‌ای وصل اینترنت کشور
✅
مخابرات (منطقه ای)
✅
آسیاتک
✅
شاتل (منطقه ای)
✅
‌پیشگامان
✅
مبین نت TD-LTE
✅
صبانت
✅
پارس آنلاین
✅
زیتل
✅
‌افرانت
✅
ایرانسل (TD-LTE)
❌
ایرانسل (سیمکارت)
❌
‌همراه اول (سیمکارت)
❌
رایتل (سیمکارت)
❌
سامانتل (سیمکارت)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/IranProxyV2/8525" target="_blank">📅 18:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8524">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔸
چه ‌وب‌سایت‌هایی در دسترس قرار گرفته‌اند؟ /دیجیاتو
ویکی‌پدیا
اپ‌استور
پینترست (Pinterest)
کنوا (Canva)
نوشن (Notion)
تردز (Threads)
کالاف
CallofDuty.com
پابجی (Pubg)
یاهو
دراپ باکس
پلی استیشن
ایکس‌باکس
استیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/IranProxyV2/8524" target="_blank">📅 18:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8522">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">از اونایی که پرو خریدن چه خبر
😂</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/IranProxyV2/8522" target="_blank">📅 18:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8520">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✈️
دوستان اگه در راستای قطع شدن بودین و وایفا نداشتین میتونید از ربات ثبت سفارش انجام بدین، آنی تایید خواهیم کرد و اینکه درنظر داشته باشین،
اطلاعیه
رو حتما مشاهده کنید.
📌
در صورتی که نت بین الملل بازگشایی شد، تمامی کاربران که از ما سفارش فعال دارند، به دیتاسنتر خارج منتقل خواهند شد و به ازای هر 1 گیگی که خریداری کرده بودند، 3 گیگ اضافه خواهد شد
❤️
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/IranProxyV2/8520" target="_blank">📅 17:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8519">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">😼👊🏻.npvt</div>
  <div class="tg-doc-extra">1.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8519" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تست کنید، منطقه ای وایفا
💥
@RUSSIAPROXYY
🇷🇺
📌
آیدی فروشگاهمون
👇🏻
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/8519" target="_blank">📅 17:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8518">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این پروکسی های تلگرام هم داشته باشید فعلا با مخابرات و برخی اینترنت های خانگی متصلن:
https://t.me/proxy?server=176.65.128.238&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=87.248.129.5&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
ممکنه منطقه ای باشه، بهتره تست کنید.
💥
@RUSSIAPROXYY
🇷🇺
📌
آیدی فروشگاهمون
👇🏻
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/IranProxyV2/8518" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8517">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎁
بفرستید واسه دوستاتون
❤️
vless://27d6de57-240b-400e-a036-192608ae0459@mbv.followern.ir:443?encryption=none&security=tls&sni=tino.protag.ir&fp=chrome&insecure=0&allowInsecure=0&type=ws&host=tino.protag.ir&path=%2F#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
متصله رو وایفاها، قلب بزنید ببینیم چندنفرید، برا دوستاتون بفرستید که وصل نیستن تک خوری نکنیدا
😶
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/IranProxyV2/8517" target="_blank">📅 17:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8516">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">درنظر داشته باشین که فعلا درحال حاضر تنها وایفاها وصل شدن مث مخابرات و آسیاتک، شاتل و... اونم بصورت منطقه ای، مشخص نیست اینم اختلال باشه یا اپدیت فایروال باشه، پس صبور کنید تا همچی مشخص بشع، فعلا اپراتور های همراه مث ایرانسل، همراه اول و رایتل و... وصل نشدن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/IranProxyV2/8516" target="_blank">📅 17:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8515">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
پروکسی متصله، رو وایفا و مخابرات منطقه ای دوستان عزیز، اگه وصل نشد تو منطقتون ذخیره کنید داشته باشینش، صبور باشید شایدم اپدیت فایروال مشخص نیست هیچی
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/IranProxyV2/8515" target="_blank">📅 16:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8514">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.21.7.21:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو وایفا و مخابرات وصله
😁
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/IranProxyV2/8514" target="_blank">📅 16:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8512">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مجدد بستن پهنای باندو
😐</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/8512" target="_blank">📅 15:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8503">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIhSOzU3A16AWlMm5OVXQbsPs-x_lnUuzNVCh84VIxnNBJQ8aBm8TL62c1Jj0sYvMaTHjREITFh4y64OtpAq0K1O-w6dLYpwlmG5fg1ePLcxHoB1FrfpLrMscU0ncAl5e-yRMnHAKC-JhpSGBpNTE1W9CZD5UeMzalRRGYR-08mUoxaPro46eNnTK_kefmnbVHDoc7bjsj-mda3vx3dggIBK-EA5yEEAiva2FPTqFzVyLAZssyZuXcn6UzVSP9FLWkpuLFrRb5k1Ku5eZvPYcHNoglbh_enar9wtQgz8-gko6_0pbameC45EA4H2qkug0m1zGTP5NgMHYfe12Yj-rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=130T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/IranProxyV2/8503" target="_blank">📅 14:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8502">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">روح و روانمون بگا رفت، از بس حرفای چرت و پرت تحویلمون دادن، رسما دارن مردم خر فرض میکنن و پاسکاریمون میکنن، من یکی که دیگه مخم نمیکشه حرفای اینارو باور کنم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/8502" target="_blank">📅 14:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8501">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-auztfZM7JU1-pos4wIcb4Y33FTWzWIIIUKB7z4hAIRIDUSc81mCAcGUdn-FVqloiPvbUXuqrIcY_ZVxc4DAbfjAYkiFwMBPQPNMeQXGUzk7cR3hyLwtFDyIHCgYxbzMPI6xuCXM1pIQ2_1Fr8SBuKjFjm1M0gq3zJRQsrR1d6lBOEDccFQQIqvvLsD4p3QVJsLjwIk0paibweLVAjZGTF3saPWWM2bBVoagjOkCEFcQXbE82y8HdSd5Yix5uHGIdJ2F4oYRA1LQOesESHzkSkFBvYlEyf5hJSB5OpLGlIOEOwl3GJvZytFVgkvatNEBn0J7YqMA6VVjg7Fi6_SnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینا حتی ذره ای تکنولوژی سردرنمیارن با اون کلشون
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/IranProxyV2/8501" target="_blank">📅 14:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8500">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرگزاری فارسی هم این موضوع موقت تاخیر در بازگشایی رو تایید کرد، درکل میگن که فعلا تاخیر خورده اینکه باز بشه یا نه
😬
وقتی مملکت بیوفته دست سپاه همین میشه دیگه، هیچکس دیگه هیچ کاره ای نیست
🥲
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8500" target="_blank">📅 14:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8499">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رئیس جمهور کشور اگه تا آخر هفته اینترنتارو باز کرد که کرد اگه نتونست بنظرم استعفا بده بهتره چون نه اونوریا حسابش میکنن که ترورش کنن حتی نه اینوریا حسابش میکنن
اونور دنیا رئیس جمهور یه کشور ناو میفرسته یه دنیارو بگا داده بعد اینجا رئیس جمهورش اینترنتم نمیتونه وصل کنه
جدی اگه نتونستین وصل کنید خودت و کل کابینت بنظرم استعفا بدید یه موز بزارید رو صندلی بجای خودتون حداقل فایده اش اینه موزه پتاسیم داره ولی شما همونم ندارید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8499" target="_blank">📅 14:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8498">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فارس: چندین نماینده مجلس که عضو جبهه پایداری و تندرو هستند درمورد مصوبه شورای فضای مجازی شکایت کردند و دیوان اداری دستور داد اجرای بازگشایی اینترنت متوقف شه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/8498" target="_blank">📅 13:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8497">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پزشکیان داداش نقش تو چیه دقیقا تو کشور</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/8497" target="_blank">📅 13:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8496">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9GQWr0Mzw_v2sUnMnKq869cuSVdLLvD-TdlAV9C9DgzF48_r5qLilVSFphcBz-WdAO5-W-a8Xnhu_aLOc-QzpxMCmjuG44bbgErqHh0b_H-l01Bc3ZZKyq-rkez84lfXIV2ZzepvyxxFcC3tG7K_DvCoH4oQh9Vj7IeGVb4hWY_T9RTbnBnmqr2lAYh5EsK_I9g4wSbwv9iXx2yvH5naEDrZ2bWVHvkz1bcFSh7P_wg6Di984zd2LedMAk_-tPQ_GnOlt9Hhzsfz5tmPIqp4vfbrM5vbD8wwgz_LZSNBYbGhA8pz14DleHYv6U7IfpzzJZxsg_8Q0QA8OjgZFaNrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارسی هم این موضوع موقت تاخیر در بازگشایی رو تایید کرد، درکل میگن که فعلا تاخیر خورده اینکه باز بشه یا نه
😬
وقتی مملکت بیوفته دست سپاه همین میشه دیگه، هیچکس دیگه هیچ کاره ای نیست
🥲
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/IranProxyV2/8496" target="_blank">📅 13:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8495">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">در پی شکایاتی از مصوبه تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور»؛ دیوان عدالت اداری دستور موقت توقف اجرای مصوبه را صادر کرد
😐
🔹
مصوبات و تصمیمات ستاد تا زمان رسیدگی نهایی به شکایت، قابل ترتیب اثر نیست
🔹
دیوان عدالت اداری اعلام کرد، در پی طرح شکایاتی…</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8495" target="_blank">📅 13:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8494">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">در پی شکایاتی از مصوبه تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور»؛ دیوان عدالت اداری دستور موقت توقف اجرای مصوبه را صادر کرد
😐
🔹
مصوبات و تصمیمات ستاد تا زمان رسیدگی نهایی به شکایت، قابل ترتیب اثر نیست
🔹
دیوان عدالت اداری اعلام کرد، در پی طرح شکایاتی با خواسته ابطال «سند ایجاد ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» مصوب ۱۴۰۵/۲/۲۲ رئیس‌جمهور، هیأت تخصصی صنایع و بازرگانی دیوان عدالت اداری با احراز ضرورت و فوریت موضوع، دستور توقف اجرای این مصوبه را تا زمان رسیدگی به شکایت مطروحه صادر کرد.
حرومزاده ها یعنی چی، هی پاسکاریمون میکنید، بخدا خسته شدم دیگه
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/8494" target="_blank">📅 13:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8493">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-3ldHF_JNDTSmvAhlfNbvM5wQtqIAb3eSAx-SNzla_lOaG4inouHo2BEBOaQOut6bA3PFsG9Sgi9LGQaBpgPVF2vl_g38ar3lSYkpJa5gFn6JhI_64_59VU2xqZv87zWbtqXb3bTKW4uV6ZR6lO5Kw-PinzhnhRT2rtQhNiyP07iPODhvf3Y9ev6lLUXbabdXsKNtM9SGzdb_pW7k_YydlNzlQWppv7PWYCSPsiRVLxqobhVDwkk6mfUOfVYk0iT-w8DYVQebxpakuNMwoyS514VcUYGGv6tw1a16cd-a0gcyMhQd69Qe14kxS8OUVCT8s773v80X1ZFRv1BGOCQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=130T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8493" target="_blank">📅 12:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8491">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⚠️
اطلاعیه، درصورتی که نت بین الملل بازگشایی شد، مجموعه روسیه پروکسی تصمیمی گرفته که به همه دوستانی که از مجموعه ما خرید داشتند به ازای هر 1 گیگی که خریداری کردین، 3 گیگ بصورت خودکار به کانفیگ هاتون اضافه خواهد کرد، پس حتما لینک ساب هاتون یا سروراتون رو یه جایی ذخیره کنید داشته باشید حتما
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/IranProxyV2/8491" target="_blank">📅 12:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8490">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دوستان درصورت باز شدن و در دسترس گرفتن نت بین المللی و برگشتن نت به حالت عادی، حواستون به چنل باشه سرورای عمومی و رایگان براتون میزاریم حتما برای دسترسی راحتتر
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/8490" target="_blank">📅 12:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8489">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وضعیت نت بلاکس هنوز هیچ دسترسی باز نشده، این چرت و پرتا که چنلا میزارن رو باور نکنید میگن نت بلاکس گفته باز شده  منبع:سایت رسمی نت بلاکس  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/IranProxyV2/8489" target="_blank">📅 11:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8488">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbtMUKzkQovjBQXCOOg-_RLIFAKBjehCMI6bcNpVSj0G8wkvfH7bJ-96hI2NCVP8TCmUsTFHTq77I5FddDvwlnxrpUiVVeQ6Ocf5oTn24lhO66pa1eA_0ri62EvdsfzVaTIYLLj_kellLzkGm6GTTGEmpyecXGtwdwusou1GEFb6ixFga5z2bHffFdTdAu1-2H-VKRJleUaudLxbKhHG-f_BFPB5UxLPmH6UuOFkL9_qqsZEB8FXg1E7KanX0qy0jBFbo7yjJu_5H7WL7UA9Z_dwD_JMQHYcbFzUCwlPR7TS4xP4Cog8mqd1L7ASb8dY-zPg3OuqLAhsGaw3CunILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت نت بلاکس هنوز هیچ دسترسی باز نشده، این چرت و پرتا که چنلا میزارن رو باور نکنید میگن نت بلاکس گفته باز شده
منبع:سایت رسمی نت بلاکس
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/IranProxyV2/8488" target="_blank">📅 11:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8487">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ادرس
mail.google.com
باز شده ولی
gmail.com
باز نیست ، اینطوری قراره نت باز بشه؟
😐
اینکه وایت لیستو دارن ادامه میدن اسمش نت باز کردن نیست عجبا
😐
!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/IranProxyV2/8487" target="_blank">📅 11:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8486">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
trojan://humanity@193.151.132.136:40443?path=%2Fassignment&security=tls&insecure=1&host=www.ignitelimit.com&type=ws&allowInsecure=1&sni=www.ignitelimit.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/IranProxyV2/8486" target="_blank">📅 11:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8485">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsqORZ-IY5jV_hQUMSQH66duB0sB7PoTyDgFJyiLI2rfj525qgzyEirsAUW24WhBHwLmkOFhqV5h15-i5Is-2qwIoNqIJlPx2FTMN7Ih_7Ik52r244t4fMGkVlnEWIRdI5L6F0lLShBUMXW2Xb9fKgdVtPPnNMJsbjBEV6Gzos3vBQoX4klqI6oTJf97o6qNJj48KzzTdbbtt-EPLXYqQK1XtClcwb_9nPIL0EndcVYCCvQAWF9-6OT3wuBQfI2kHtJl-jZCR0yNdYgtb-AxQ9DqXggkmMWPp2oR4PuUUA3Ciw4RweLrkL-DNlC8yRUpER13fGh0GmyV39OSwl3_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/IranProxyV2/8485" target="_blank">📅 10:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8484">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
trojan://humanity@193.151.132.136:40443?path=%2Fassignment&security=tls&insecure=1&host=www.ignitelimit.com&type=ws&allowInsecure=1&sni=www.ignitelimit.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/IranProxyV2/8484" target="_blank">📅 10:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8483">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نیویورک پست:
ترامپ نظر خود را تغییر داده و احتمال توافق اکنون به طور قابل توجهی کاهش یافته است؛ تماس ترامپ با نتانیاهو تأثیر بسیار زیادی داشته است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/8483" target="_blank">📅 10:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8482">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مذاکرات طوری داره پیش میره که احتمال اینکه ایران اورانیوم غنی شده آمریکا رو بگیره بیشتره
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/IranProxyV2/8482" target="_blank">📅 10:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8480">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rC4rPuhXzPpYApFZS6wtr1aqKOPslU0FQnsEt3AI5h8W9uRFKRCOneoZHtX7IZmYcMk7GRhTDVEWtWq10lEEmeDcYdrmxbdYKIjxsIUQqPxs6lIesn-hCyzhKPHG2eYwpcaMQjbrrSvL8pzclhQOZ1gzfhhDM69_A0NYTShr0HDvhwh_OL2bFKttxtXbYsfO8lIkf1qKotw47UVIaALdyz8vu6ZMJ2dqUXK9s7MOKcrCxiJFNytgqy8kMgz-IMqcByQSyxI_xm4CPwFfTuRtMNyRplCcLW8Ozu0QrJgQclMVlf9t8K8hM0rauZNz8u0TouGs16wMG23UvOoWAOTEFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/IranProxyV2/8480" target="_blank">📅 10:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8479">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IE7ntSb_xDddy0b4z9nRp0XHQjfoE3z9ZoTC9--JO3X5Lzzgf7deyvGnnQhNaTnKoV_HlDsBtmArilqzO7infFo438fyoovnyw0idMg2-1JUTKBtzc_FZnysmZUBEzytsNpjj8C-83FcaeEc2tv7hAP2nAwmUtLsh5C75zrrZzCI5wjBfB-3OYTNCOgsk83HxP8K7PdUb7z_ZTJxJmQluPqenbmbcxwJsPD6qPHa0FwZPXbg8fVszFDXl8z2m1uDrYeZdzUBeXnkdHqoWzmRnVta8gr8Jl7GKqulivKVzPTUwwfF142_Ai1_3qyVF_H__YASYcSJb6HkJJOv2hOK8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی خواب بودین، آپدیتی رو سرور ها اعمال کردم، که هم بهینه شد و هم از همه نظر فیکس شده باگ هاش
🍸
❤️
➡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/IranProxyV2/8479" target="_blank">📅 09:25 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
