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
<img src="https://cdn5.telesco.pe/file/OAxTyiHN6sKTwToIxIwrZbD1lvMktJOo22y8pyLOwWD6iWTTho8Gpt0I6apwGLaYmU51R24dCoCzuYFM3aEX-lwCOuH0tkQ5fMOey-tgcFK7Dzexu7unDH4KhgtEBiBqR3j3XVL5X9JToGguQj2aTk-VCo6XroyiFc93kCL2FBtBgY4daXMSuYNEiMxUlJbpyca7izHr_cKut2ZzNRQ5i4wy9ZTO7-zxc6xDmvagtfOKNKrPm3emlP5r0iU5rrQq1qkHstxcDS9B4TgtDF-QS0gqUR7fDrfsfeMNbQA4CQLAFyurvUJoBFRQTvXvmdJ9Vi4HW5n1H2Qvbm2LzNlJsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 108K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 15:11:43</div>
<hr>

<div class="tg-post" id="msg-1496">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/e-Ys2aJLSOXvN4QVCuL9wl-RjnO-wJHShwUvXbIBMkau4ruAGGYBg17bhXAK5eqY2r9evq063ilsv8Ok6iqkRykwtXSpmurTEUpN0YSgPuaIeTxsnhwrnbVE51cCWG3DFTEG_LQr28D6mnxuSYIAUY7cmhrVkJ-nHAHdYJJRz48Jh6uccSng3ot-Jj2cTdVmzHv9UJB-71dOV3koMkPduan2NKnkq7QjLb87-fGglOkzFKIgi1jGa72GaaOYizduMMwxhFQ8i7EQA7oyJpaqyrLRaaQrHJwXsy7PFghJJmUSL1bW9kdxTzBRxdaOx6nE0q2eIT_hc0MP6jsJsBGJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/whitedns/1496" target="_blank">📅 07:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1495">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/voxQvXVasNR7LR8qHGNm8BuUXZDVWAHtQ1lbuKNu1BJGfR7AnopXVLJagi218lNgaUKCzdhfUzH8hvrodOoA8h5yjBIzf4pgvwse7yjmf_Y8iNHloanHpJckWS2ClSdQTlKqiJDuMsdrygmDGQn5gxuG6mfT_RL7yFjR1mpwxlYwzJw5QikFh0oDD02n5Dz8MOq9U7iXkxtre3hbM4iJkomNCwWRIetx_zIXuVZZo_J6ivodvFxPeMNS-cJqAueChRaDXwJDMo2zKgo513LrALt_DPSwxCWoI7KM2n7abjStNNq_mfHooCNEipxtQ7y6Z8IrTRBWqvdznjnf0qHFuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/whitedns/1495" target="_blank">📅 07:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1493">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NIdR6P2ZoqBticK4N55xQuLVPzBgM4dJAwtLFy6vIHos7hVSlgF_9FjZqZPivta8GTJxSeq7nTg9Uabdx-CNKesiW3S75_YKlclEPZMi9t2quKNYMbTvedwxPNdbUPBbQE5_ZcLFSD3FAupZzb-JYLZjgYtEaelXNvkiZcfxUct-4jpUJM-llBipY6emI9VlZ5nLYxZqBh8338-IlKsUIS1yL7C81wmxtHRyB8JQlo49aEuHrzK5CJMsvxQiXz56O-odWGf9uCGoWQVQHHCyUxu7Bwq0uB4edgPm3nVvXNQVLP4JJcFcEfhz1Fql7Skdmhu49QshndIxIGg4NOefaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام :
برای حل این مشکل توی ورژن دسکتاپ و مبایل whitevpn لطفا ساب زیر را دستی وارد کنید
اگر به هر دلیلی ساب برای شما اپدیت نمیشه اول یک فیلترشکن روشن کنید که ساب را بتونید بگیرید و اپدیت کنید بعد استفاده کنید
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
@whitedns</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/whitedns/1493" target="_blank">📅 05:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1491">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
تمام
#نکات
واسه مشکل فیلتر شدن worker رو داخل این پست میگم:
👽
💻
طبق آموزش هایی که قبلا دادم با اپلیکیشن pattng و همچنین v2rayn در ویندوز میتونید مشکل فیلترشدن ورکر رو حل کنید و کانفیگ های -1 رو مجدد متصل کنید.
آموزش مروبطه:
👇
https://t.me/xsfilterrnet/3642
📱
داخل ios هم طبق تنظیمات یه ip تمیز پیدا کنید داخل کلاینت incy یا hiddify بزنید و فرگمنت رو روشن کنید متصل میشه.
یه روش دیگه بعد از بالا اومدن پنل استفاده از کانفیگ های فرگمنت برای bpb هست که با مقادیر low (1-1) رو متصل کنید
🔥
🔗
در مورد لینک ساب های raw هم به گفته خود bpb:
بچه‌ها اگر ساب Raw و کانفیگ TLS استفاده میکنید از این روش در v2rayNG/pattngاستفاده کنید، معلوم نیست تا کی کار کنه، اگر پایدار بود پنلو تغییر میدم.
این رو دو جا وارد کنید:
https://8.8.8.8/dns-query
۱. قسمت Remote DNS تنظیمات برنامه.
۲. ویرایش کانفیگ قسمت echConfigList.
با Mux خاموش
یه نکته دیگه از بچها اینترنت آزاد که جواب داده:
با ECH و استفاده از آدرس udp://1.1.1.1 میتونید فیلترینگ
pages.dev
و
workers.dev
رو دور بزنید.
💓
نکته ای هم که متین سنپای گفته:(همراه با ابزار جدید)
https://t.me/MatinSenPaii/4960
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/whitedns/1491" target="_blank">📅 22:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1489">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E58lVtM0wad1Av8--tVrIVd8HH9ttHo7tm0MoZ8sg8qXBCsGDeeeTCuWWgOnt27Whi0z14tXLRxW-HcO2vNFTcGNCwFlnvEHCodmFjTgQHEK6WacaShnzwFZmlSSfUquqDJzZ9eB6c_2TiiK2tdss6dtZAOkR4vvcDN0vuJ9Gncfn6y5jCG7qZiK36jFnGHuBHUbPUtW1gcIkYF4PeM-P_XRMh6Jp-SFbP-zXgaXG8p8uHBGzLwdB__krkCLMe7XKm-Q94GUh5wVwSmOUE53yQwH2CpUj_ymX8TrmY-RdHCAN-kaau5N3PF1aEzOScJR1rDFc-M0NcbM5z6A81zO9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟   میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro و باقی Wireguard ها وصل بشید.  این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/whitedns/1489" target="_blank">📅 21:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1488">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjXcKeoZVTvbRj_VKTYU6navQE8mD5KVr273uR6a_2PEtaOEzAMBSuM3--nFPg60_F9p-VeNg9Gyll9Z4KITYiUDxG6h6vFjLdoZceySQLJt4F7rhOSUSAjm9HQQ4wgJOv-G7t6RL_0wAzMTuaHbLfsI3-o0jIo40wIkFtVx0cGOdUlTUMKrkrHxFw3BniUXrs_hjbRki8Xwk0r39gBc6nmXO3NwrwDrnSf0GIW_CVoPgU1XPUYF1BV-3awB2jt0m_kCoPTM0cfzQpvXpdCxFitcocgcanSJsvteODGggvZ3ITacFtlcElgLo8yayS6Uci7BvLShtvVwGwYVVUQjug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro و باقی Wireguard ها وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN
لینک ساب Mihomo رو داخل WhiteVPN وارد کنید.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/whitedns/1488" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1487">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=t8RADgyOh5kYGTPI64qCkN-4ypgqX13exnzw4ZR0riHV9QivZM64nqOC2wlYaz_2u25LT81Ts_dFwUMGV5YeFf5kWFsPJ6eiYKgMaPYTXt4YqjcmVq4MnOUkS1zmBWlNi1SpVs-r5PaXfyjZQ7o5K1RywBDxpshL1v8OUhh64t88MTtPYKDBgIgVgiJsz6Ad6J8coF9_J4Xmat01eVdRFDhKg7_yF5rhrLByMGzdpljG2_gC_CjgvNy8vz-U_SA_5Y9LqJslnkmaX4_2dUPSg2vXzEB44l2LDD6BA7TuXQc3pMBVQvt0faTEq2ljAE-CCwPiuRMJO3LCZLc-j-b6jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=t8RADgyOh5kYGTPI64qCkN-4ypgqX13exnzw4ZR0riHV9QivZM64nqOC2wlYaz_2u25LT81Ts_dFwUMGV5YeFf5kWFsPJ6eiYKgMaPYTXt4YqjcmVq4MnOUkS1zmBWlNi1SpVs-r5PaXfyjZQ7o5K1RywBDxpshL1v8OUhh64t88MTtPYKDBgIgVgiJsz6Ad6J8coF9_J4Xmat01eVdRFDhKg7_yF5rhrLByMGzdpljG2_gC_CjgvNy8vz-U_SA_5Y9LqJslnkmaX4_2dUPSg2vXzEB44l2LDD6BA7TuXQc3pMBVQvt0faTEq2ljAE-CCwPiuRMJO3LCZLc-j-b6jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/whitedns/1487" target="_blank">📅 19:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1486">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/whitedns/1486" target="_blank">📅 19:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1481">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/whitedns/1481" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/whitedns/1481" target="_blank">📅 19:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1480">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVbIcnx1JHJBTUIYPS0xkwDYr-baZrhUwYcfRx_VoIVom7WHcV9LJakAHAEIOk5vgpl6wMCDf2sO6IrDD5FuurOAQQfHRyhP7MflF9vvjkXPtNRzJu3Da4XbctMDiF95n74mufcZ0aeA5YQJAa4tkOjOxxlzRT0C-XiDQEUZOnigJvQfzctkPsqYSM8u9azBCLpco7VXAn7prn09cDyM7RBV_98p_cSiYbeXMo6hDYGGxyVufQUjWL5Su6XLhsmYSbEtXZmJRRBd1Yfvlh9K_lRk1XPHM49p2_Susyzah9Xugf_Ia1WCvIcmyPU-Kt5Dp3G6Ya_D2He39D8C9o-8_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0
• ظاهر جدید و مدرن اپ
• بهبود اتصال بعد از قطع شدن
• حل مشکل VPN Mode & Proxy Mode
• بهبود تست اتصال. حالا میتونید کشور رو فیلتر کنید و بعد تست کنید. تست هم به دو مرحه real delay و تست سرعت  تقسیم شده.
🌎
دانلود آخرین نسخه از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/whitedns/1480" target="_blank">📅 19:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1478">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/QK7OAgITg9gTemzCrd8KceGsjOneZp7ysNRNNJF6xJMFV-HrphpVjyJfy__R7dASRn34QqhaE49atAt21lhEpbzRfvzrvZ3zOMGKyV3xeyi-0abhGM4kxUE4o0V2dox0zY6Csdm_mGd3xWDyRQky9fEvyPeDimjwod5Ns_K_kCXWVQW-D-virTFGPRB45XQDeodZxLo0NXJYEM9kzxieAUEL0pAnhBQQSMv_76q8wmTXuSLijtn58Byf4reK4gdoXibPPfR2BE0LbL9Fpec1NTrjLiEvUPHuEldKTb_zvS05eElLjfRpwldKbn8JxL0eg8OYSg1FSxVXdyJFz_cOLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
وایت‌استر  —
نسخه‌ی دسکتاپ بتا
WhiteAesther Desktop V1.3.1
یه کلاینت رایگان و متن‌باز برای عبور از فیلترینگ، ساخته‌شده روی هسته‌ی Aether (همون هسته‌ای که تو اپ اندرویدش هم استفاده می‌شه). برای ویندوز، مک و لینوکس؛ کاملاً رایگان و بدون نیاز به کانفیگ دستی.
✨
امکانات:
🔎
جست‌وجوی خودکار مسیر — به‌جای اینکه شما دنبال کانفیگ سالم بگردید، خود برنامه بهترین دروازه رو پیدا می‌کنه (با MASQUE H2/H3، WireGuard و WARP-in-WARP)
📊
نمودار سرعت و تأخیر زنده — تست سرعت واقعی داخل خود برنامه + نمودار پینگ لحظه‌ای
🖥
دو حالت اتصال — «فقط این برنامه» (پراکسی محلی) یا «کل سیستم» (همه‌ی اپ‌ها از تونل رد بشن)
🛡
کلید قطع اضطراری — اگه تونل قطع بشه، ترافیک رمزنشده لو نمی‌ره
🔍
جست‌وجوی تنظیمات با Ctrl+K — هر تنظیمی رو در چند ثانیه پیدا کنید
🧩
چندپلتفرمه — ویندوز، مک (اینتل و اپل‌سیلیکون) و لینوکس، هم x86_64 هم arm64
📖
متن‌باز، برای همیشه — کد کامل زیر مجوز AGPL-3.0 روی گیت‌هاب
⚙️
نحوه‌ی استفاده:
1️⃣
از لینک زیر، نسخه‌ی مخصوص سیستم‌عاملتون رو دانلود کنید
2️⃣
نصب کنید و برنامه رو باز کنید
3️⃣
دکمه‌ی Connect رو بزنید و چند لحظه صبر کنید تا مسیر سالم پیدا بشه
4️⃣
اگه خواستید کل سیستم از تونل رد بشه، پایین صفحه گزینه‌ی «Whole machine» رو بزنید
5️⃣
برای تنظیمات پیشرفته (پروتکل، DNS، حالت جست‌وجو…) روی Advanced بزنید یا Ctrl+K رو بزنید و اسم تنظیم موردنظرتون رو تایپ کنید
📥
دانلود:
github.com/WhiteDNS/WhiteAesther/releases/latest
💬
نکته: چون برنامه امضای اپل/مایکروسافت نداره، ممکنه هنگام باز کردن هشدار «ناشر ناشناس» ببینید؛ کافیه روی فایل راست‌کلیک کنید و Open رو بزنید (تو مک هم از System Settings اجازه‌ی اجرا بدید).
#وایتاستر
#ضدفیلتر
#متنباز
نکته مهم :
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
گزینه whole machine همان system proxy هست - این گزینه فقط اپلیکیشن هایی مثل گوگل کروم که امکان ان را دارند پراکسی میکند - برای همین ممکن هست بعضی از اپ های شما پراکسی نشود
تلاش خواهیم کرد در روزهای اینده امکان TUN را اضافه کنیم
@whitedns</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1478" target="_blank">📅 18:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1477">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دوستان عزیز سلام
مثل اینکه آدرس های ورکر کلادفلر فیلتر شدن. و آدرس ساب اپلیکیشن ما داخل ورکر ها هستش. تا آپدیت بعدی، میتونید ساب مارو از لینک زیر وارد اپ WhiteVPN بکنید
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/1477" target="_blank">📅 16:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1476">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/IBXAhJDFvfjv-5vmbkNiSKh4feWH59RF06AVpHnI95p_rKrwuSzYVlSQwvNOHHuFut40WJHXDVe08SmjvXv2pqDyrpyYZM2_WUUaNLpr4aF-YvzgP8z0K-VevUuOM2m7MbTXiAkNm5RZn6OM6ed33KaQqaVdFnd1YWVMsKqDqH0aDfnLtJEtVGgtE3PY_RiyxhvdQZTmiF-g-iWRCGaeI-sNRxzTbxUmfCyMDdJ4hDaeo6k9mhGZFu-o7vc0OgYl8X8eGWG-2Zwe9bjxi0nRLiW-8Q7imKR3gcl7zVCzDfOkvB92REkhrX4-e8WOtm9EezuJ4qikbYJcHu5R5vGvcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther V1.0.2
دوستان سلام :
ما روی هسته Aether که حاصل زحمت دوست عزیزمون
CluvexStudio
هست یک کلاینت**
آزمایشی ورژن بتا
** درست کردیم . که اگر دوست دارید تست کنید و لطف کنید فیدبک بدید.
پیشاپیش ممنونیم
❤️
❤️
❤️
اموزش :
📖
**راهنمای WhiteAesther**
**۱ — نصب**
فایل **arm64-v8a** رو بگیر (تقریباً همه گوشی‌های ۲۰۱۷ به بعد).
مطمئن نیستی؟ **universal** همه‌جا کار می‌کنه، فقط حجمش بیشتره.
**۲ — سه تا نکته اول**
▪️
**Traffic** → گزینه Coverage روی **Whole device** باشه
⚠️
حالت Proxy only خودش هیچی رو رد نمی‌کنه! به‌نظر می‌رسه وصل شده ولی عملاً هیچ ترافیکی از تونل نمی‌ره.
▪️
**Routes** → پروفایل روی **Adaptive**
▪️
**Settings** → اجازه اجرا در پس‌زمینه رو بده، وگرنه با خاموش شدن صفحه قطع می‌شه
**۳ — اگه وصل نشد، به این ترتیب امتحان کن**
**قدم ۱ — پروتکل**
Routes → Advanced → Preferred transport → **MASQUE over HTTP/2**
📌
روی **همراه اول** مدتیه QUIC (یعنی UDP) کاملاً بسته شده. یعنی H3 اصلاً وصل نمی‌شه و فقط H2 جواب می‌ده.
از نسخه ۱.۰.۲ اپ خودش این کار رو می‌کنه.
**قدم ۲ — تیکه‌تیکه کردن TLS**
⭐️
Traffic → Advanced → **Split the TLS handshake** → روشن
فیلترینگ معمولاً فقط تیکه اول بسته رو می‌خونه تا ببینه کجا وصل می‌شی. وقتی تیکه‌تیکه بفرستی، نمی‌تونه بخونه.
اگه با H2 وصل می‌شی ولی کنده، **حتماً اینو امتحان کن**.
**قدم ۳ — پروفایل**
Routes → Profile → **Strict network**
(برای شبکه‌هایی که خیلی چیزها رو می‌بندن)
**قدم ۴ — خاموش کردن IPv6**
Traffic → Addresses → **IPv4 only**
روی خیلی از شبکه‌های موبایل ایران IPv6 نیمه‌کاره‌ست.
**قدم ۵ — مبهم‌سازی**
Traffic → Advanced → Obfuscation → **Aggressive**
💡
اگه قدم ۲ مشکلت رو حل کرد، **Off** رو هم تست کن — شاید پدینگ اضافه فقط داشته سرعتت رو می‌گرفته.
**قدم ۶ — اند‌پوینت دستی**
Routes → Endpoint → Specific address → دکمه **Find endpoints**
⚠️
گزینه Fall back automatically رو روشن نگه دار.
**۴ — گزارش مشکل**
Settings → Diagnostics & logs
۱. Detail level روی **Verbose**
۲. دوباره سعی کن وصل بشی
۳. برگرد و **Send** رو بزن
قبل از ارسال دقیقاً متنی که فرستاده می‌شه رو می‌بینی، و IP‌ها پیش‌فرض مخفی می‌شن. هیچی بدون اجازه‌ات از گوشیت بیرون نمی‌ره.
**نکته:** اون خط خاکستری کوچیک زیر متن بزرگ توی صفحه اصلی، پیغام خود موتوره. برای فهمیدن مشکل همیشه اول اونو بخون.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.0.3
@whitedns</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/whitedns/1476" target="_blank">📅 13:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1474">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OGo2yRDihCpBdvXhLiIzGe5xXWdQqUOnGWOY8ZmlYVGvaHRuiwLjTKDk0wa2japVe0t0rZM7VMoZHMXg5Vel1Ty5Pdv1e4q1c46ycx93tdxiqUmyr33uf2n70slmDOJLguUBgQNfyxsfH2v2FxJ2rZeQeXLjbW3a4r6ZUnUBj4DNYFvDvmByFm4E_z--5c1-YnJz3_BH2jxoDjQORy_1m9FeRNSpEvIgR5ThDDRRUWvMUZR7F8aeiqu3gWXGLxDkvHdP-HX7Zg0MZ1Z2MbVEvZCboEHaeKGQjac6uXpTGZZ3WwSRO4RgXOHB7UFv8eDR6ebMWyDE7LwGQgY6Sr-FaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS Clean IP Finder 1.3.7
نسخه جدید WhiteDNS Clean IP Finder با تمرکز روی افزایش سرعت پیدا کردن DNS Resolverهای سالم در Desktop و Android منتشر شد.
⚡️
مهم‌ترین تغییرات:
• اجرای همزمان تست‌های DNS Transport و TXT Passthrough برای کاهش Timeout
• اجرای Parallel بررسی‌های NXDOMAIN Hijack
• اضافه شدن Fast Scan با حفظ بررسی‌های اصلی A Record، Recursion، EDNS و TXT Tunnel
• حفظ Full Scan به‌عنوان حالت پیش‌فرض برای بررسی کامل
• بهبود دریافت و Cache اطلاعات Reference DNS
• اضافه شدن UDP/53 Only و TCP/53 Only در Android
• گزارش دقیق‌تر DNS Poisoning، Injection و Hijack
• بروزرسانی دیتابیس Iran & Global ASN شامل IPv4 و IPv6
💻
پشتیبانی از Windows، Linux، macOS و Termux
📱
نسخه Android شامل APKهای مختلف، Universal APK
✅
برای آپدیت نیازی به تغییر تنظیمات قبلی نیست.
📥
دانلود WhiteDNS Clean IP Finder 1.3.7:
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3.7
⚡️
WhiteDNS Clean IP Finder — اسکن سریع‌تر، تشخیص دقیق‌تر و دیتابیس به‌روزتر
@whitedns</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/whitedns/1474" target="_blank">📅 02:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1473">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vg8d58Jv22_q1U2BIlxKTsn3N2TOF8J9NmVMbVa-nAQoJrppNn5UWc-OtgOk-s-VYGSVyEpUx46aykSAdzudJVp5kizlSIS0hoXgCZbCDSgbpRKRtCfPONM7wkDnzTwES3f9Jee9yl9akeVO-GLzPzsxsU8UeVLNfzPyvZCIs_5aAUT3QKqvp32LgHoIoHLSIHyd2B0L6va6SnlyLNrM-2sDdLl46KBwS_JfMDaA0VtMOnjMPMiYYqkATVhqrzcuCO70zJyQeRdG8CYTovfkQtXJx8ZQxl-08Vemb8TXrAvs72iBhi0XmrW8-wLRXygQIWg4e1YYP_ox0nlZuGMQug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏯️
آموزش ساخت کانفیگ V2Ray با سرور رایگان!   توی این آموزش با استفاده از Wasmer یه سرور رایگان می‌سازیم و در نهایت بدون نیاز به خرید سرور، ۳ تا کانفیگ V2Ray برای مصرف شخصی دریافت می‌کنیم.
⚡️
⏯️
تماشا در یوتیوب  https://youtu.be/EAjOhvuMw8Q</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/whitedns/1473" target="_blank">📅 21:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1472">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⏯️
آموزش ساخت کانفیگ V2Ray با سرور رایگان!
توی این آموزش با استفاده از Wasmer یه سرور رایگان می‌سازیم و در نهایت بدون نیاز به خرید سرور، ۳ تا کانفیگ V2Ray برای مصرف شخصی دریافت می‌کنیم.
⚡️
⏯️
تماشا در یوتیوب
https://youtu.be/EAjOhvuMw8Q</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/whitedns/1472" target="_blank">📅 21:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1471">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HGsPDqV1AZXTMovdbc9zRiGoomK-kKJTiHsCud5EuG3o0dC1KvXaG7R1Aa57Fwz9qHqrJ9L8FwSk6pnaiewO4RVHLVHf1G1Z1BCcMU93XenvF12RKj0vxodLFE_ES_w-8P4q-cnuYHnKEmbADQg7IDEz3QM00iU1jmRnr2qczexlJbaZnabWCRcuxHTJSew5qhOabnBgN6vNI3scRtk1ymE80AQvnBnnQk06uzOOLOvcDAJqSFkuoAeMxYx-m5RtsjLlnhghcL6W6M2y0hTgwEJFbDQ-C65Dx4pHjKBXWXZoKLZhwrX6vDjyI7XphYqsezAdRg0XsIoF3XwVUJG4eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط عادی :
•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
شرایط قطعی اینترنت :
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS دسکتاپ
•
دانلود آخرین نسخه CoreForge برای آیفون
@whitedns</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/whitedns/1471" target="_blank">📅 18:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1470">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromUAC Sni Spoofer(Behrooz)</strong></div>
<div class="tg-text">🛡
نسخه‌ی 2.0.1 اپلیکیشن UAC SNI Spoofer برای اندروید منتشر شد
در نسخه‌ی 2.0.1 تمرکز اصلی روی این بوده که برنامه در شبکه‌ها، اپراتورها و مناطق مختلف، مسیرهای سالم‌تر و سریع‌تر رو پیدا کنه و در صورت افت کیفیت یا از دست رفتن مسیر فعلی، بتونه مسیر مناسب‌تری رو جایگزین کنه.
⚡️
یکی از مهم‌ترین قابلیت‌های این نسخه، تلاش برای زنده‌کردن کانفیگ‌هایی هست که در حالت عادی دیگه قابل استفاده نیستن.
🔹
اگر کانفیگی دارید که IP سرورش روی اپراتور یا شبکه شما بلاک شده
🔹
مطمئن هستید کانفیگ سالمه ولی در برنامه‌هایی مثل v2rayNG متصل نمی‌شه
🔹
کانفیگ فقط روی یک اپراتور خاص کار می‌کنه و روی اپراتورهای دیگه از دسترس خارج شده
🔹
کانفیگ قبلاً کار می‌کرده ولی به‌دلیل تغییر محدودیت‌های شبکه دیگه متصل نمی‌شه
UAC SNI Spoofer می‌تونه با بررسی ترکیب‌های مختلف مسیر، DNS، Edge، Fragment، MTU و سایر پارامترهای اتصال، برای پیدا کردن یک مسیر قابل استفاده تلاش کنه.
در تست‌های انجام‌شده، برنامه تونسته بخش بسیار زیادی از کانفیگ‌های سالم ولی محدودشده رو دوباره قابل استفاده کنه و در بعضی شرایط میزان موفقیت تا حدود 98٪ هم رسیده.
البته نتیجه نهایی به نوع فیلترینگ، اپراتور، منطقه، وضعیت سرور و کیفیت اینترنت شما بستگی داره.
تغییرات نسخه 2.0.1:
🔹
برنامه برای هر شبکه یک اثرانگشت جداگانه ایجاد می‌کنه و تنظیمات موفق همون شبکه رو ذخیره می‌کنه تا دفعات بعد سریع‌تر به مسیر مناسب برسه.
🔹
بخش Route Speed Test حالا می‌تونه ترکیب‌های مختلف Edge، DNS، Fragment و MTU رو بررسی کنه و بهترین مسیر فقط براساس Ping انتخاب نمی‌شه.
🔹
مسیرها در چند مرحله از نظر اتصال، سرعت، پایداری، نوسان و میزان موفقیت بررسی می‌شن و بهترین نتایج بالای لیست قرار می‌گیرن.
🔹
امکان توقف Route Speed Test و ادامه‌دادن اون در زمان دیگه اضافه شده.
🔹
می‌تونید هر زمان که خواستید مسیرهای سالم پیدا شده رو به مرحله بعد بفرستید و لازم نیست منتظر پایان کامل تست بمونید.
🔹
برای هر کانفیگ و هر شبکه، یک مسیر اصلی و یک مسیر پشتیبان ذخیره می‌شه تا اتصال سریع‌تر انجام بشه.
🔹
اگر شبکه تغییر کنه یا کیفیت مسیر فعلی افت کنه، برنامه می‌تونه سراغ مسیر پشتیبان بره و برای بازیابی اتصال تلاش کنه.
🔹
سرویس‌های مختلف DNS مثل Cloudflare، Google، Quad9، AdGuard و OpenDNS در دسترس هستند و همراه مسیرهای مختلف قابل تست هستن.
🔹
بخش Config Maker دارای دو حالت Quick Scan و Deep Adaptive Test شده؛ یکی برای بررسی سریع و دیگری برای تست دقیق‌تر و گسترده‌تر مسیرها.
🔹
امکان وارد کردن کانفیگ از متن، Clipboard، فایل و Subscription Link وجود داره.
🔹
لینک‌های جدید بدون حذف نتایج قبلی به لیست اضافه می‌شن و کانفیگ‌های تکراری به‌صورت خودکار حذف می‌شن.
🔹
کانفیگ‌های VLESS، VMess و Trojan پشتیبانی می‌شن و مشخصات اصلی کانفیگ تا جای ممکن بدون تغییر باقی می‌مونه.
🔹
برای برنامه‌های گوشی سه حالت Routing در دسترسه: عبور همه برنامه‌ها از VPN، خارج‌کردن برنامه‌های انتخابی از VPN یا استفاده از VPN فقط برای برنامه‌های انتخابی.
🔹
حالت Tunnel و پروکسی محلی SOCKS در دسترس هست و تنظیماتی مثل Fragment، FinalMask، MTU، Mux، Keepalive و کنترل QUIC هم قابل تغییر هستن.
🔹
Ping، میزان دانلود و آپلود، کشور، IP خروجی و اطلاعات فنی اتصال به‌صورت زنده نمایش داده می‌شن.
🔹
بعد از اضافه‌کردن برنامه به Quick Settings اندروید، می‌تونید بدون بازکردن برنامه VPN رو مستقیماً روشن یا خاموش کنید.
⚠️
نکته مهم:
محدودیت‌های فیلترینگ در هر منطقه، اپراتور و حتی در زمان‌های مختلف می‌تونه متفاوت باشه. به همین دلیل ممکنه کانفیگ داخلی برنامه برای بعضی کاربران متصل نشه یا روی بعضی شبکه‌ها کیفیت متفاوتی داشته باشه.
در حال بررسی مسیرها و محدودیت‌های شبکه‌های مختلف هستم تا روش‌های بیشتری شناسایی بشن و برنامه بتونه در مناطق و اپراتورهای بیشتری محدودیت‌ها رو دور بزنه.
همچنین حتماً مطمئن بشید اینترنت اصلی شما سرعت دانلود و آپلود قابل قبولی داره. VPN نمی‌تونه ضعف شدید یا ناپایداری اینترنت پایه رو جبران کنه و کیفیت اتصال نهایی به کیفیت شبکه شما هم وابسته است.
━━━━━━━━━━━━━━━━━━
📥
دریافت نسخه 2.0.1:
https://github.com/Floxu1/UAC-SNI-Spoofer-Android/releases/tag/2.0.1
💻
گیت‌هاب پروژه:
https://github.com/Floxu1/UAC-SNI-Spoofer-Android/tree/main
جهت حمایت از من اگر دوست داشتین وارد لینک رفرال من در NotHolidaySeasonBot بشین
❤️
:
https://t.me/NotHolidaySeasonBot/app?startapp=tr_aFLKAgxVq8ezM310c0sS
📢
کانال:
t.me/UacSniSpoofer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/1470" target="_blank">📅 15:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1468">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XFvQS_LrTL153Wsd0IDridJuPbDKf1HWW3Af88vKs8NDxlZJoh4f-9_rfTe4V0Ai9NUoHX96Eh2Ln_KcqTZghlWuEB7qTJfssoRkH7rxnLhRiEvHRyqTBgEGegHFRDBtSyKvkcuwmfCWKy9kGGH8rE0SuPrD6QsfvCN4Wwuymu0o2kIgvG7Ip0o8MYPZHm_4fGs7GaZALWvKpwNqxpj_-6RuO1-EEEpnCUGqTYcpedQJEMow1sg6ZYMLCiZtrw-BG9YxkJJfqK--BuBnyDEG78oebNKlW-lX09tlhGabQw0bNDhX9CSn9mrDEq594bT13q8oofYvJDiVCr2bGPDlWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/whitedns/1468" target="_blank">📅 11:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1467">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/X8AtNreZKzuUP-5Sb5qaE3GfHoMKwQWpSe-j2pvCxBm5U08AuMQsys5UoDd9fTcb9JkWVUdtVj2viqxWn60LcD2a5nY5gIFecaaVoUXVoIqVWwjrBL-pPt04y07BgXMjdNZ_veRIMjXK7VmxWSuPBVWAZ5kNzke_UAmYzhA7JckBdJumjZH9FIXK-3TtE1NcN3ejTq-H7eZyIpj1IH7TntFmaI2fcZSUXWTYUdIG2IT3eQ9GC0TK2SQfFGpqoXWyKD8jpBhD8QcB8BEqLqyPXRh5nGDVsP3D0_rjouJFK4XOCy64ACiVyJF5hr4lpylGXl1HEdPDlCfuiXpjJw5hdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Coming soon............
WhithAester desktop
😍</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/whitedns/1467" target="_blank">📅 09:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1466">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌎
پروژه WhiteVPN رو اوپن‌سورس کردیم و در گیتهاب میتونید بهش دسترسی داشته باشید.   https://github.com/WhiteDNS/WhiteVPN  همراه با پابلیک شدن پروژه، نسخه ۱.۳.۱ هم ریلیز کردیم
⛏
در این نسخه امکان • آپدیت اتوماتیک اپ  بعد از یک ورژن جدید • امکان routing برای…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/whitedns/1466" target="_blank">📅 09:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1464">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🌎
انتشار نسخه ۱.۳.۱ اپلیکیشن WhiteVPN
پست قبلی پاک شد. یک آپدیت کوچیک داشتیم به ورژن ۱.۳.۱
😆
از این به بعد آپدیت هارو اتوماتیک از داخل اپ میتونید بگرید</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/whitedns/1464" target="_blank">📅 08:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.3.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/whitedns/1459" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1459" target="_blank">📅 08:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1458">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nED7pbbjEKdW1masu89SaDQNHDKL2LwyzzRwCvOMGKtS7rcPwVM2K4v4Ze3VYmlUSEumcRr_xNxqbGXx2yDAKlFNdffMNLOaif1eIpxYAHEYmzIYnzVwduE6_k3wemprBjy7dPQ9xiY6wlhAx8Uf6grUPx7_Ek7vgCcWrI1WtCfGmIxJKxJ7Ogoew_sgrKQ0bAp9y5jOk99hRJVGCS7iQkcWVhdaLEeX4VvkgDJeJhlfXfOl_-zWgWnbff0vLF90DGWTwieKa3GCb93-hlC-4uD-k9eUBe7R9go0OEgsS6RQm17Z2yoYDR8WgObJH0olP2xdyBYv9T6KK4S0RWkwzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
پروژه WhiteVPN رو اوپن‌سورس کردیم و در گیتهاب میتونید بهش دسترسی داشته باشید.
https://github.com/WhiteDNS/WhiteVPN
همراه با پابلیک شدن پروژه، نسخه ۱.
۳
.
۱
هم ریلیز کردیم
⛏
در این نسخه امکان
• آپدیت اتوماتیک اپ  بعد از یک ورژن جدید
• امکان routing برای سایت ها و آی‌پی های ایرانی به تنظیمات اضافه شده تا دیگه نیاز نباشه اتصال رو برای سایت های داخلی قطع کنید.
• اشتراک گذاری WhiteVPN در شبکه اضافه شده.
• حالا میتونید اپ پروکسی اپ در داخل اپ های دیگه مثل سایفون استفاده کنید.
• تست سرعت به سابسکریپشن اضافه شده
دانلود نسخه جدید از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.3.1</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/whitedns/1458" target="_blank">📅 08:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1449">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/q10npR743vJ8dJtPFs5-Qxj7sRuLRQQtHujPqnT6qE8KyT7ITZ-4LCiREXqCae57FQcy5QE6HO5xw0w9YlnEpp-vWmqu0jINiew8Z31rHhQetx7xHjcY6mrh4v7xpUdilI9AmGoNnLrY3hRl2qX6C_pBOylkaVWLLI5tVRGGDpmxAF3emzvbTnxaKJMahkMbh6INJlFBQj6CjogWP3IAGeIlzQ8AxRpLaSsTEtDPocM0mTMMr5EGKUcswZZUEeCyAuSCkxO-rj-lWh03iTbJSCNIYl6dEMAOb75UdSbDgb2WWVn7TIItdfvl1b-qesLgD1PFg1JbOuOOSrQ0MZrNDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther V1.0.2
دوستان سلام :
ما روی هسته Aether که حاصل زحمت دوست عزیزمون
CluvexStudio
هست یک کلاینت**
آزمایشی ورژن بتا
** درست کردیم . که اگر دوست دارید تست کنید و لطف کنید فیدبک بدید.
پیشاپیش ممنونیم
❤️
❤️
❤️
اموزش :
📖
**راهنمای WhiteAesther**
**۱ — نصب**
فایل **arm64-v8a** رو بگیر (تقریباً همه گوشی‌های ۲۰۱۷ به بعد).
مطمئن نیستی؟ **universal** همه‌جا کار می‌کنه، فقط حجمش بیشتره.
**۲ — سه تا نکته اول**
▪️
**Traffic** → گزینه Coverage روی **Whole device** باشه
⚠️
حالت Proxy only خودش هیچی رو رد نمی‌کنه! به‌نظر می‌رسه وصل شده ولی عملاً هیچ ترافیکی از تونل نمی‌ره.
▪️
**Routes** → پروفایل روی **Adaptive**
▪️
**Settings** → اجازه اجرا در پس‌زمینه رو بده، وگرنه با خاموش شدن صفحه قطع می‌شه
**۳ — اگه وصل نشد، به این ترتیب امتحان کن**
**قدم ۱ — پروتکل**
Routes → Advanced → Preferred transport → **MASQUE over HTTP/2**
📌
روی **همراه اول** مدتیه QUIC (یعنی UDP) کاملاً بسته شده. یعنی H3 اصلاً وصل نمی‌شه و فقط H2 جواب می‌ده.
از نسخه ۱.۰.۲ اپ خودش این کار رو می‌کنه.
**قدم ۲ — تیکه‌تیکه کردن TLS**
⭐️
Traffic → Advanced → **Split the TLS handshake** → روشن
فیلترینگ معمولاً فقط تیکه اول بسته رو می‌خونه تا ببینه کجا وصل می‌شی. وقتی تیکه‌تیکه بفرستی، نمی‌تونه بخونه.
اگه با H2 وصل می‌شی ولی کنده، **حتماً اینو امتحان کن**.
**قدم ۳ — پروفایل**
Routes → Profile → **Strict network**
(برای شبکه‌هایی که خیلی چیزها رو می‌بندن)
**قدم ۴ — خاموش کردن IPv6**
Traffic → Addresses → **IPv4 only**
روی خیلی از شبکه‌های موبایل ایران IPv6 نیمه‌کاره‌ست.
**قدم ۵ — مبهم‌سازی**
Traffic → Advanced → Obfuscation → **Aggressive**
💡
اگه قدم ۲ مشکلت رو حل کرد، **Off** رو هم تست کن — شاید پدینگ اضافه فقط داشته سرعتت رو می‌گرفته.
**قدم ۶ — اند‌پوینت دستی**
Routes → Endpoint → Specific address → دکمه **Find endpoints**
⚠️
گزینه Fall back automatically رو روشن نگه دار.
**۴ — گزارش مشکل**
Settings → Diagnostics & logs
۱. Detail level روی **Verbose**
۲. دوباره سعی کن وصل بشی
۳. برگرد و **Send** رو بزن
قبل از ارسال دقیقاً متنی که فرستاده می‌شه رو می‌بینی، و IP‌ها پیش‌فرض مخفی می‌شن. هیچی بدون اجازه‌ات از گوشیت بیرون نمی‌ره.
**نکته:** اون خط خاکستری کوچیک زیر متن بزرگ توی صفحه اصلی، پیغام خود موتوره. برای فهمیدن مشکل همیشه اول اونو بخون.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.0.3
@whitedns</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/1449" target="_blank">📅 11:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1448">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان عزیز،
در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.
🔗
https://www.youtube.com/@WhiteDNS
ممنون از همراهی همیشگی شما
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/whitedns/1448" target="_blank">📅 11:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1447">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXUEGlg7YnKoqkp57eGQzRBvp2EJB5Pv1yB2vsQK7gvNEy9iIQpoHpOySzXhm6Lh6cEGm3pPi0SXSn8UU1JxIUJBVOVsRWchFY_isKzzTcbSgD2B8RT81ODQQuKcDE7LpGfXzH7DzwLRvWJuXxuFMkcAoQb4fDisQNaqQh8TQ6YMgpGGkAy6-FJh1xHGJKHvpvHYJoOjAdq5fCVjoiH9Law7OLzeG1r9ZdUZb-UwTbvv7926R1ghVC00YrtoVR5uKujyI7Dct3etHnoYivleJWvzrJHw_YjGW3gDXW_sDxFqhvmiXPXP0hrNRKlL41bKn7LHcdjNzUKmnczG6K1k6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین نسخه CoreForge برای آیفون</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/whitedns/1447" target="_blank">📅 09:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1446">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌎
سلام خدمت همه دوستان عزیز
در آخرین آپدیت سرویس ساسبکریپشن WhiteVPN ما مشکل کشور هارو حل کردیم.
حالا اگر از اپ اندروید یا دسکتاپ کشوری رو انتخاب کنید، کانکشن به کشور درست وصل خواهد شد.
⛏
دانلود آخرین ورژن WhiteVPN اندروید
⛏
دانلود آخرین ورژن WhiteVPN دستکتاپ
اگر اپ رو دارید، اول ساب خودتون رو رفرش کنید.
اگر مشکلی دیدید، حتما با ما به اشتراک بگذارید.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/1446" target="_blank">📅 09:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1444">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">موقت
⚠️
هشدار مهم برای همه اعضا
⚠️
⚠️
⚠️
⚠️
دوستان عزیز،
بارها گفتیم:
به هیچ‌کس—چه ناشناس، چه آشنا—برای فیلترشکن، VPN، کانفیگ و… پول ندهید.
دلیل اینکه ما اینجا شبانه‌روز وقت می‌گذاریم همین است که شما
بی‌نیاز از پرداخت پول
باشید و گرفتار افراد سودجو نشوید.
اگر بدون پرسیدن از ادمین‌ها رفتید پول دادید و طرف کلاهبردار از آب درآمد، بعدش پیام می‌دید که «چی کار کنم؟» واقعاً ما در این مرحله کاری از دست‌مان برنمی‌آید.
چرا قبلش نپرسیدید؟
ادمین‌ها ۲۴/۷ پاسخگو هستند.
ما نمی‌توانیم در تک‌تک چت‌های خصوصی شما مراقب‌تان باشیم. لطفاً قبل از هر پرداختی، یک پیام ساده بدهید و سؤال کنید.
کلاهبردار پیام داده 1000 گیگ فیلترشکن BPB - به مرغ پخته بگی خندش میگیره
پول را واریز کرده - اونم در کسری از ثانیه بلاکش کرده -
حتما با تگ کردن ادمین ها افرادی که تبلیغ فروش VPN میکنندیا در خصوصی به شما پیشنهاد میدهند را گزارش دهید
این مکان با کمک و همراهی همه فقط میتونه امن و سالم باقی بمونه
ارادت</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1444" target="_blank">📅 07:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1443">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">Whitevpn dekstop v1.0.16
🍎
🐧
راهنمای استفاده روی مک و لینوکس
حالت TUN فعلاً فقط روی ویندوز کار می‌کند. روی مک و لینوکس دو حالت دیگر هست که برای اکثر کارها کافی‌اند.
━━━━━━━━━━━━━━━
🖥
روی مک — ساده‌ترین حالت
تنظیمات ← اتصال ← «پراکسی سیستم» را انتخاب کنید و وصل شوید. تمام.
مک تنظیم پراکسی را در سطح سیستم اعمال می‌کند، پس تقریباً همهٔ برنامه‌ها (سافاری، کروم، فایرفاکس و بیشتر اپ‌ها) خودکار از تونل رد می‌شوند.
━━━━━━━━━━━━━━━
🐧
روی لینوکس — یک نکتهٔ مهم
«پراکسی سیستم» روی لینوکس تنظیمات گنوم و KDE را عوض می‌کند. ولی این یک ترجیح است، نه اجبار: برنامه‌هایی که این تنظیم را می‌خوانند رد می‌شوند، و برنامه‌هایی که نمی‌خوانند نه.
معمولاً کار می‌کند: کروم، کرومیوم، فایرفاکس
معمولاً کار نمی‌کند: تلگرام دسکتاپ، ابزارهای ترمینال
برای آن‌هایی که کار نمی‌کنند، سراغ بخش بعدی بروید.
━━━━━━━━━━━━━━━
🎯
وصل کردن یک برنامهٔ خاص (روی هر دو سیستم)
اگر می‌خواهید فقط یک برنامه از تونل رد شود — یا برنامه‌ای پراکسی سیستم را نادیده می‌گیرد — این راه مطمئن‌ترین است.
آدرس پراکسی، بعد از وصل شدن، در صفحهٔ اصلی نشان داده می‌شود. روی آن کلیک کنید تا کپی شود. معمولاً:
127.0.0.1:2080
این آدرس هم SOCKS5 و هم HTTP را می‌پذیرد.
📱
تلگرام دسکتاپ
Settings ← Advanced ← Connection type ← Use custom proxy
نوع: SOCKS5 — آدرس:
127.0.0.1
— پورت: 2080
🦊
فایرفاکس
Settings ← Network Settings ← Manual proxy configuration
SOCKS Host:
127.0.0.1
— Port: 2080 — گزینهٔ SOCKS v5
⌨️
ترمینال (curl، git، npm و…)
این‌ها هیچ‌وقت از تنظیمات گرافیکی پیروی نمی‌کنند و باید دستی بهشان گفت:
export http_proxy=
http://127.0.0.1:2080
export https_proxy=
http://127.0.0.1:2080
(فقط برای همان پنجرهٔ ترمینال اعمال می‌شود)
━━━━━━━━━━━━━━━
💡
اگر نمی‌خواهید کل سیستم پراکسی شود
تنظیمات ← اتصال ← «فقط پراکسی» را انتخاب کنید. در این حالت هیچ چیزی روی سیستم شما تغییر نمی‌کند و فقط همان برنامه‌هایی که خودتان تنظیم کرده‌اید از تونل رد می‌شوند.
━━━━━━━━━━━━━━━
📥
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.16</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/1443" target="_blank">📅 16:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1440">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">Whitevpn desktop V1.0.15 ( linux 24+)
🐧
راهنمای نصب روی اوبونتو ۲۴ و بالاتر
بعضی از دوستان روی اوبونتو ۲۴ به بالا موقع نصب با خطای dependency روبه‌رو شده‌اند. مشکل از برنامه نیست — فقط باید فایل درست را دانلود کنید.
━━━━━━━━━━━━━━━
📌
اول ببینید نسخه‌تان چند است
در ترمینال بزنید:
lsb_release -a
یا از مسیر Settings ← About نگاه کنید.
━━━━━━━━━━━━━━━
✅
اوبونتو ۲۴.۰۴ و بالاتر (شامل ۲۵ و ۲۶)
فایلی را دانلود کنید که در اسمش webkit41 دارد:
WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.deb
و نصبش کنید:
sudo apt install ./WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.deb
⚠️
حتماً ./ را قبل از اسم فایل بگذارید، وگرنه apt دنبال آن در اینترنت می‌گردد.
━━━━━━━━━━━━━━━
✅
اوبونتو ۲۲.۰۴ و دبیان ۱۲
فایل بدون webkit41:
WhiteVPN-Desktop-1.0.15-linux-amd64.deb
sudo apt install ./WhiteVPN-Desktop-1.0.15-linux-amd64.deb
━━━━━━━━━━━━━━━
🎯
ساده‌ترین راه: AppImage
اگر نمی‌خواهید درگیر نصب و وابستگی شوید، فایل AppImage را بگیرید. اصلاً نصب نمی‌خواهد و به هیچ کتابخانه‌ای روی سیستم شما وابسته نیست:
WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.AppImage
بعد از دانلود، اجازهٔ اجرا بدهید و اجرا کنید:
chmod +x WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.AppImage
./WhiteVPN-Desktop-1.0.15-linux-amd64-webkit41.AppImage
(این فایل برای اوبونتو ۲۴ به بالا است)
━━━━━━━━━━━━━━━
💡
چرا دو تا فایل هست؟
اوبونتو در نسخهٔ ۲۴ کتابخانه‌ای که برنامه‌های گرافیکی از آن استفاده می‌کنند را عوض کرد. یک فایل واحد نمی‌تواند هر دو را پوشش دهد، برای همین دو نسخه می‌سازیم. فایل webkit41 مال نسخه‌های جدید است.
📥
دانلود همهٔ فایل‌ها:
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1440" target="_blank">📅 13:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1438">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۵
🐧
رفع یک اشکال مهم روی لینوکس
روی لینوکس، بستن پنجره باعث می‌شد برنامه ناپدید شود اما در پس‌زمینه اجرا بماند — بدون هیچ آیکونی برای برگرداندنش. تنها راه بستنش، kill کردن از ترمینال بود.
دلیلش این بود: برنامه فرض می‌کرد آیکون نوار وظیفه ساخته شده، در حالی که خیلی از محیط‌های دسکتاپ (از جمله گنوم بدون افزونهٔ AppIndicator) اصلاً چنین آیکونی نشان نمی‌دهند.
حالا برنامه واقعاً بررسی می‌کند که آیا آیکونی نمایش داده می‌شود یا نه. اگر نه، بستن پنجره یعنی بستن برنامه.
📡
اشتراک اتصال روی شبکهٔ محلی
حالا می‌توانید اتصال این دستگاه را با دستگاه‌های دیگر روی همان شبکه به اشتراک بگذارید — گوشی، تلویزیون، یا هر چیزی که روی همان وای‌فای یا هات‌اسپات است.
تنظیمات ← اتصال ← «اشتراک روی شبکهٔ محلی» را روشن کنید. بعد از اتصال، آدرسی که در صفحهٔ اصلی نشان داده می‌شود را در دستگاه دیگر وارد کنید.
⚠️
توجه کنید: هر کسی که روی آن شبکه باشد می‌تواند از این اتصال استفاده کند و از کسی رمز پرسیده نمی‌شود. این را برای هات‌اسپات خودتان یا شبکهٔ خانگی روشن کنید، نه روی وای‌فای عمومی.
📤
خروجی گرفتن دسته‌جمعی از کانفیگ‌ها
اگر کانفیگ‌های خودتان را وارد اپ می‌کنید و تستشان می‌گیرید، حالا می‌توانید آن‌هایی که تست را پاس کرده‌اند یکجا خروجی بگیرید — به‌جای اینکه یکی‌یکی share بزنید.
تست بگیرید ← موارد سالم را انتخاب کنید ← «خروجی انتخاب‌شده‌ها»
خروجی را می‌توانید کپی کنید یا در یک فایل ذخیره کنید تا به گوشی یا تلویزیون منتقل کنید. حالت Base64 هم موجود است، چون بعضی کلاینت‌ها همان را می‌پذیرند.
━━━━━━━━━━━━━━━
⚠️
اگر نسخهٔ ۱.۰.۱۴ نسخهٔ مک (Intel) را دانلود کرده‌اید
فایل آن نسخه ناقص ساخته شده بود و احتمالاً درست کار نمی‌کند. لطفاً نسخهٔ جدید را دانلود کنید.
📥
دانلود:
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1438" target="_blank">📅 12:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1437">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-poll">
<h4>📊 با whitevpn desktop وصل هستید ؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1437" target="_blank">📅 11:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1436">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوستان، یه توضیح مهم درباره پروژه X4G که توی ویدیوی بالا معرفی کردیم:
بعد از انتشار ویدیو متوجه شدیم که به نظر می‌رسه بخش قابل توجهی از پروژه X4G از پروژه RVG گرفته شده، بدون اینکه اعتبار مناسبی به سازنده اصلی داده شده باشه.
🔗
پروژه اصلی
(لطفا برای حمایت استار بدید)
https://github.com/arvin341az-glitch/RVG
✍️
برای اینکه از سمت WhiteDNS حق و اعتبار سازنده اصلی تا جای ممکن رعایت بشه، این کارها رو انجام می‌دیم:
- اسم RVG رو به عنوان ویدیو اضافه می‌کنیم.
- توضیح مربوط به این موضوع رو در کامنت‌های ویدیو پین می‌کنیم.
- لینک گیت‌هاب داخل توضیحات ویدیو رو به ریپوی اصلی RVG تغییر می‌دیم.
این جور اتفاق‌ها متأسفانه توی دنیای Open Source پیش میاد. ما قبل از ساخت ویدیو با هیچ‌کدوم از توسعه‌دهنده‌های این پروژه‌ها در ارتباط نبودیم و طبیعتاً تشخیص اینکه یک پروژه از پروژه دیگه کپی شده، همیشه از قبل ممکن نیست.
ممنون از دوستانی که این موضوع رو به ما اطلاع دادن.
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/whitedns/1436" target="_blank">📅 03:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1433">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی  این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/whitedns/1433" target="_blank">📅 20:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1432">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=lDYmRzmF-7SvxHXrWUyrx5hm44aQUk7gSxAnHidO1CHLobUIp-Y64QpIR0u9LtCWL89XdHTNL6e7JpVGodXkyh2t8iFuy-rikbDnk1a1VkRofZ-KMHF81TOcvntawil2Ye2pkbn7oUKjWycGhX5sPQ43YZbRakUfJTzEhiAiWGywq5C65pU-zn10fpj6wGEo8yClejd4c8PYBcloMdsGov4sk5WSutjpEqKPQ66H6e30ZZeqKMDvJiKdOWwx3x0jhUuDm2STpebe7-U4MXXsU7ygZQQGvW1lD4E3-M85ETGhpGUR3dzm5T3VAQM37h0lO96zzn2Fr8neMHMCiTleSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=lDYmRzmF-7SvxHXrWUyrx5hm44aQUk7gSxAnHidO1CHLobUIp-Y64QpIR0u9LtCWL89XdHTNL6e7JpVGodXkyh2t8iFuy-rikbDnk1a1VkRofZ-KMHF81TOcvntawil2Ye2pkbn7oUKjWycGhX5sPQ43YZbRakUfJTzEhiAiWGywq5C65pU-zn10fpj6wGEo8yClejd4c8PYBcloMdsGov4sk5WSutjpEqKPQ66H6e30ZZeqKMDvJiKdOWwx3x0jhUuDm2STpebe7-U4MXXsU7ygZQQGvW1lD4E3-M85ETGhpGUR3dzm5T3VAQM37h0lO96zzn2Fr8neMHMCiTleSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی
این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب
https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/whitedns/1432" target="_blank">📅 19:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1431">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/whitedns/1431" target="_blank">📅 16:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1430">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">White DNS
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1430" target="_blank">📅 12:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1428">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">White DNS
pinned «
دوستان عزیز،  در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1428" target="_blank">📅 12:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1427">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان عزیز،
در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.
🔗
https://www.youtube.com/@WhiteDNS
ممنون از همراهی همیشگی شما
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/whitedns/1427" target="_blank">📅 12:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1426">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(Dᵢₐₙₐ🍓)</strong></div>
<div class="tg-text">📚
آموزش اسکن Resolver و استفاده در WhiteDNS (cottendns)
اگه دنبال یه Resolver مناسب و پایدار برای راه‌اندازی WhiteDNS هستی، توی این آموزش قدم‌به‌قدم نحوه اسکن و پیدا کردن IPهای مناسب با Clean IP Finder و استفاده از اون‌ها در CottonDNS رو توضیح دادیم.
⚡️
🔍
کاربردها:
• اسکن و پیدا کردن ریزالور های مناسب
• بررسی پایداری و سرعت Resolverها
• استفاده در WhiteDNS
• بهبود کیفیت و پایداری اتصال
📥
دانلود ابزارها:
🔹
Clean IP Finder v1.3.6
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.6
🔹
WhiteDNS v1.6.0
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚡️
ابزارها رو دانلود کن و طبق آموزش پیش برو.
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/whitedns/1426" target="_blank">📅 08:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1424">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۴
🔧
رفع اشکال آیکون نوار وظیفه (taskbar)
در نسخه‌های اخیر، منوی راست‌کلیک روی آیکون کار نمی‌کرد و امکان بستن برنامه از آنجا وجود نداشت — تنها راه، Task Manager بود.
مشکل از حلقه‌ای بود که پیام‌های آیکون را می‌خواند و روی رشتهٔ (thread) اشتباهی اجرا می‌شد.
اگر نسخهٔ ۱.۰.۱۲ یا ۱.۰.۱۳ را نصب کرده‌اید، این به‌روزرسانی را حتما داشته باشید
📥
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.14
@whitedns</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/whitedns/1424" target="_blank">📅 10:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1423">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/b10yYDgYrrfu_Zzfgm5XLbUl78pfybafRh_qQRNxo-LUwllAHLBjKE6PuK144v-tszNKtb8q3RPBQTLQRSuATmB_sMnd2Xi84mAQ8qdCkY3mKgnxRo-TikD6Oiovrs36xgOOs-QsORQWAc0Pxy9Xect2vWiftBG7qei2wDreSbAwrZySG2sGQytfJCYGByfEnJiFhNpDU2QqgIXgv8TI7kvCgmMqsZAsB2xZ0ZNRg3svRlWNs6A6b2tssITWBWJaOqOt2Ei0IZb_hRrOYQCA1rX4hPEwxpyqZRdklaBgumKts5IMJAKomLcev6rGGsEBg6LIpkGuDrYxVmU9x0lmRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۳
Stable
🎯
حالت «فقط پراکسی» اضافه شد
تا حالا دو حالت بیشتر نبود و هر دو کل سیستم را از تونل رد می‌کردند. حالا سه حالت دارید:
• پراکسی سیستم — کل دستگاه (مثل قبل)
• فقط پراکسی — هیچ‌چیز روی سیستم شما تغییر نمی‌کند
• تونل TUN — کل دستگاه، حتی برنامه‌هایی که پراکسی را نادیده می‌گیرند
در حالت «فقط پراکسی» برنامه فقط گوش می‌دهد و شما خودتان تصمیم می‌گیرید چه چیزی از تونل رد شود. مثلاً فقط تلگرام، یا فقط یک افزونهٔ مرورگر — بقیهٔ سیستم دست‌نخورده و با سرعت عادی.
📌
چطور استفاده کنید
۱. تنظیمات ← اتصال ← «فقط پراکسی» را انتخاب کنید
۲. وصل شوید
۳. روی آدرس پراکسی در صفحهٔ اصلی کلیک کنید تا کپی شود
۴. همان را در تنظیمات پراکسی تلگرام وارد کنید
هم SOCKS5 و هم HTTP روی همان یک پورت کار می‌کند.
🔒
پورت دیگر عوض نمی‌شود
در این حالت پورت ثابت می‌ماند و خودتان می‌توانید تغییرش دهید. اگر برنامهٔ دیگری آن را گرفته باشد، همان موقع به شما می‌گوید — نه اینکه بی‌سروصدا پورت دیگری بگیرد و تنظیمات تلگرام شما یک روز بی‌دلیل از کار بیفتد.
━━━━━━━━━━━━━━━
⚠️
نکته برای کاربران فعلی
سوییچ TUN در تنظیمات جای خود را به یک منوی انتخابی داده. اگر قبلاً TUN را خاموش داشتید، روی «پراکسی سیستم» قرار می‌گیرید — یعنی دقیقاً همان رفتار قبلی. تا وقتی خودتان چیزی را عوض نکنید، هیچ فرقی نمی‌کند.
📥
دانلود:
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/whitedns/1423" target="_blank">📅 19:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1422">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔵
WhiteVPN Desktop —نسخه 1.0.12
*stable *
🔋
از نسخه ۱.۰.۴ تا حالا تغییرات زیادی انجام  شده.
━━━━━━━━━━━━━━━
🔓
اشتراک‌هایی که باز نمی‌شدند، حالا باز می‌شوند
مهم‌ترین تغییر همین است. روی بعضی شبکه‌ها، اشتراک اصلاً دریافت نمی‌شد و خطای مبهمی دربارهٔ TLS می‌داد.
دلیلش این بود: نام سایت در اولین بستهٔ ارتباط بدون رمز فرستاده می‌شود. فیلترینگ همان یک بسته را می‌خواند و ارتباط را قطع می‌کند — قبل از اینکه اصلاً چیزی رد و بدل شود.
حالا آن اولین بسته به قطعه‌های کوچک شکسته می‌شود، طوری که هیچ قطعه‌ای نام کامل را در خود ندارد. سرور همان چیزی را دریافت می‌کند که همیشه، ولی دیگر چیزی برای تطبیق باقی نمی‌ماند.
این کار فقط وقتی انجام می‌شود که مسیر عادی شکست بخورد، پس روی شبکهٔ سالم هیچ کندی‌ای ندارید.
🔄
اشتراک‌ها خودشان به‌روز می‌شوند
اگر اشتراکی روی شبکهٔ شما باز نشود، فقط وصل شوید — اپ خودش آن را از داخل تونل دوباره می‌گیرد.
🔐
گزینه برای اشتراک‌هایی که گواهی‌شان تأیید نمی‌شود
روی بعضی شبکه‌ها چیزی وسط راه گواهی خودش را جای گواهی سرور می‌دهد. برای این حالت گزینهٔ «دریافت بدون بررسی گواهی» اضافه شده — فقط برای همان یک اشتراک، و فقط وقتی نشان داده می‌شود که واقعاً به کار بیاید.
⚠️
توضیحش را حتماً بخوانید: نشانی اشتراک کلید حساب شماست.
━━━━━━━━━━━━━━━
🔔
اطلاع از نسخه‌های جدید
اپ خودش بررسی می‌کند که نسخهٔ تازه‌تری منتشر شده یا نه و به شما اطلاع می‌دهد. دیگر لازم نیست دستی سر بزنید.
━━━━━━━━━━━━━━━
⚙️
تنظیماتی که حالا واقعاً کار می‌کنند
چند تنظیم بودند که ذخیره می‌شدند ولی هیچ اثری نداشتند. همه درست شدند:
• Split Tunneling —
اپلیکیشنی که کنار می‌گذاشتید واقعاً از تونل خارج می‌شود
• بررسی سلامت TLS — اتصالی که در آن دخالت شده باشد رد می‌شود
• نویز اتصال (Amnezia) — روی اتصال‌های WireGuard اعمال می‌شود
• پراکسی سیستم روی لینوکس — روی GNOME و KDE تنظیم می‌شود
━━━━━━━━━━━━━━━
🛡
حریم خصوصی و امنیت
• نشانی اشتراک دیگر در پیام خطا نمایش داده نمی‌شود. قبلاً اگر از صفحهٔ خطا اسکرین‌شات می‌گرفتید، کلید حسابتان هم در آن بود.
• روی ویندوز دیگر دسترسی Administrator نمی‌خواهد، مگر برای حالت تونل.
━━━━━━━━━━━━━━━
🐞
رفع اشکال
• پنجرهٔ مشکی PowerShell که هنگام اتصال در حالت TUN باز و بسته می‌شد
• نشتی DNS در حالت TUN
• در نصب تازه، لیست سرورها خالی نمایش داده می‌شد
• گزینهٔ پاک کردن اطلاعات برنامه و بازگشت به حالت اولیه در تنظیمات
• پیام‌های خطا حالا می‌گویند دقیقاً چه کاری باید بکنید
━━━━━━━━━━━━━━━
📥
دانلود برای ویندوز، مک و لینوکس:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.12
@whitedns</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/whitedns/1422" target="_blank">📅 14:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1420">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=wBGvXxe4-JAjxhUa0aXUGvUQLAK0OhFQW7HWgVmeSB0CUp5mFCmhRWiqglOwLqEO6XQATq5X9Kris3SyC6oSCIhOek-JwMHxduy1Fk4Nr8KZinCfCjzl0W65Smi23NzaxJQIFQFLj0BY6o_MqqP4fUdyGX39AJmg3yH2XPl3I3GN2NGlZEOaNhytcXyWJKRm3yz87u25wkctMRceGWNYIgNJ41N1bz5_AUJh3VgLnjU0ZdLQj1FeBy3GCI-nxg_uiWw6e234a2lf6iOMYREjfGxSZrd0Zb9nI7-kXAay7FFZVJOYHGn0PUsYsk7AixTuRLQpGFaXSFRkZ36udBP9xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=wBGvXxe4-JAjxhUa0aXUGvUQLAK0OhFQW7HWgVmeSB0CUp5mFCmhRWiqglOwLqEO6XQATq5X9Kris3SyC6oSCIhOek-JwMHxduy1Fk4Nr8KZinCfCjzl0W65Smi23NzaxJQIFQFLj0BY6o_MqqP4fUdyGX39AJmg3yH2XPl3I3GN2NGlZEOaNhytcXyWJKRm3yz87u25wkctMRceGWNYIgNJ41N1bz5_AUJh3VgLnjU0ZdLQj1FeBy3GCI-nxg_uiWw6e234a2lf6iOMYREjfGxSZrd0Zb9nI7-kXAay7FFZVJOYHGn0PUsYsk7AixTuRLQpGFaXSFRkZ36udBP9xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/whitedns/1420" target="_blank">📅 11:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1419">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔒
WhiteVPN Desktop نسخهٔ ۱.۰.۴ منتشر شد
🚀
۱. رفع نشتی DNS در حالت تونل — مهم‌ترین تغییر این نسخه
🔒
در نسخه‌های قبلی، وقتی روی حالت
TUN
وصل می‌شدید، خودِ ترافیک از تونل عبور می‌کرد — ولی درخواست‌های
DNS
از تونل بیرون می‌رفتند و مستقیم به مودم یا سرویس‌دهندهٔ اینترنت شما می‌رسیدند.
🌐
یعنی محتوای ارتباط شما محافظت می‌شد، اما
فهرست سایت‌هایی که باز می‌کردید برای ISP قابل دیدن بود
.
👀
علت پیدا و برطرف شد. حالت پراکسی هیچ‌وقت این مشکل را نداشت.
✅
⚠️
اگر از حالت TUN استفاده می‌کنید، حتماً بروزرسانی کنید.
🔄
۲. صفحهٔ Servers
🖥
•
انتخاب همه
اضافه شد
✅
•
کپی به کانفیگ‌های من
— یک سرور از ساب را به لیست خودتان کپی کنید و بعد آزادانه ویرایشش کنید
✏️
•
مخفی کردن
— سرورهایی را که نمی‌خواهید از لیست و از مسیر اتصال کنار بگذارید. بعد از بروزرسانی ساب هم مخفی می‌مانند، و هر وقت خواستید برمی‌گردانید
👻
• رفع به‌هم‌ریختگی ستون عملیات
🛠
⬇️
دانلود برای ویندوز، مک و لینوکس:
💻
🍎
🐧
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.4
@whitevpn
📲</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/whitedns/1419" target="_blank">📅 05:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1418">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=qx9wcGi5fMOeM0Od2X6Z9-l5HSQbX2rk55WDl0a2fS8FRHTIBO5-oLCylKDCB0bqZSM4HLvykHprrCreJlaSifo3TMZpTM3e-Jao53ObJoYkTU23VNHpH4N3pxlQwv2JEzFbAr91X76f0jJPEi9_KT6XzFLZnPJ4gJTI9o9BrXTWT3rDpYa4qwZT8l7CIXaNF1Na_8jM9pFprxk1xFRjP26mLEwlZ4jm3Hk1jAdmcbzUq3rpzuj5FSyeJYK-rrN8eAudE6IDr5IDMZoX2pL7Ob27TWRYb417ZI-3nrMqqv3jM-TiPdhZuphR8R_ldOTIbog_T620_xQ08Nzn29BMSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=qx9wcGi5fMOeM0Od2X6Z9-l5HSQbX2rk55WDl0a2fS8FRHTIBO5-oLCylKDCB0bqZSM4HLvykHprrCreJlaSifo3TMZpTM3e-Jao53ObJoYkTU23VNHpH4N3pxlQwv2JEzFbAr91X76f0jJPEi9_KT6XzFLZnPJ4gJTI9o9BrXTWT3rDpYa4qwZT8l7CIXaNF1Na_8jM9pFprxk1xFRjP26mLEwlZ4jm3Hk1jAdmcbzUq3rpzuj5FSyeJYK-rrN8eAudE6IDr5IDMZoX2pL7Ob27TWRYb417ZI-3nrMqqv3jM-TiPdhZuphR8R_ldOTIbog_T620_xQ08Nzn29BMSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/whitedns/1418" target="_blank">📅 01:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1416">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚀
WhiteVPN Desktop نسخهٔ ۱.۰.۳ منتشر شد
۱. اتصال خودکار از پایه بازنویسی شد
✅
حالا دقیقاً مثل نسخهٔ اندروید کار می‌کند: اپ دیگر خودش نودها را یکی‌یکی امتحان نمی‌کند، بلکه انتخاب را به موتور می‌سپارد تا از بین صدها نود، بهترینِ در دسترس را بردارد — و اگر نودی از کار افتاد، خودش روی نود دیگر می‌رود.
نتیجه: اتصال در چند ثانیه
⚡️
، و خطای «could not connect» که خیلی‌ها می‌گرفتند برطرف شد.
۲. رفع مشکل حالت تونل (TUN)
🛠
مشکلی که باعث می‌شد روی بعضی سیستم‌ها کانفیگ در حالت پراکسی وصل شود ولی در حالت تونل نه، پیدا و برطرف شد. کسانی هم که IPv6 سیستمشان را غیرفعال کرده‌اند دیگر با خطا مواجه نمی‌شوند.
۳. حذف و ویرایش کانفیگ در صفحهٔ Servers
✏️
کانفیگ‌هایی که خودتان اضافه کرده‌اید حالا قابل ویرایش و حذف هستند. برای اصلاح یک کانفیگ دیگر لازم نیست همه را پاک کنید و از اول وارد کنید.
۴. پیام‌های خطای واضح‌تر
📢
اگر اتصالی برقرار نشد، اپ دلیل واقعی را نشان می‌دهد نه فقط «ناموفق» — هم برای شما روشن‌تر است، هم گزارش مشکل را خیلی راحت‌تر می‌کند.
⬇️
دانلود برای ویندوز، مک و لینوکس:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.3
@whitedns</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/whitedns/1416" target="_blank">📅 19:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1415">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/iIhFwmP7bj7-1x-FcKT5jVCn4HqPKLIU37fCDZvxp4Yh0Wx3gcvV5LWGuFITs_WGE4N_VaFLbAbh_TtGQzikXTjQTng7YHRydCe5At_CFdw8q_dDISTCQoyIUvnYHLSLKodsAzIn8iDvtEf42ZcjDSlZLO1oWatQhai-euSjWDvnEjCIyfMirwNBQLrhqRwkrOrlitVTRzWX7nfNaQj_rNkhbmPvGYYm-XbvV8useORZK8uNAlBEWT9lwM1yQ2xLkG6NjvK3vgtpyLO2YZ09aR8Iu1E8iJY804lKIpXuUaqQgu5r0dddZMEZwJmvll7IVtKmFFEVGIWvqU_-3t2yyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN
Desktop
نسخه 1.0.2 منتشر شد
🎉
مهم‌ترین تغییر: حالا هر نوع لینک اشتراکی را می‌شناسد
🔓
تا نسخهٔ قبل فقط لینک‌های اشتراک معمولی (vless، vmess، trojan و…) اضافه می‌شدند. اگر پنل شما خروجی Clash یا sing-box یا Xray می‌داد، برنامه خطا می‌داد
❌
از این نسخه این‌ها همه کار می‌کنند
✅
:
- لینک‌های اشتراک معمولی و base64
- کانفیگ Clash / mihomo (چه YAML چه JSON)
- کانفیگ sing-box
- کانفیگ Xray و v2rayN
- و حالت base64 هر کدام از این‌ها
فرقی نمی‌کند پنل شما کدام قالب را بدهد
📝
. سرورها مثل همیشه در صفحهٔ Servers می‌آیند و می‌توانید پینگ و سرعتشان را بگیرید
📶
، مرتب کنید و یکی را انتخاب کنید
🚀
.
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.2
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/whitedns/1415" target="_blank">📅 15:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1414">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🌎
نسخه‌ی دسکتاپ WhiteDns منتشر شد!
📤</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/whitedns/1414" target="_blank">📅 11:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1413">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚀
معرفی اپلیکیشن WhiteDNS Desktop
کلاینت قدرتمند تونلینگ DNS برای کامپیوتر
اگر به‌دنبال ابزاری حرفه‌ای برای تونلینگ DNS، مدیریت پروکسی و عبور از محدودیت‌های شبکه هستید،
WhiteDNS Desktop
یکی از کامل‌ترین گزینه‌های در دسترس است.
این اپلیکیشن یک کلاینت محلی DNS Tunneling را روی سیستم شما اجرا می‌کند و در کنار آن، امکانات پیشرفته‌ای برای مدیریت پروکسی سیستم در اختیارتان قرار می‌دهد.
✨
ویژگی‌ها و امکانات کلیدی
🔹
پشتیبانی کراس‌پلتفرم
قابل اجرا روی Windows، macOS و Linux
🔹
پشتیبانی از موتورهای مختلف
امکان انتخاب بین موتورهای:
• CottenDNS
• MasterDNS
• StormDNS
🔹
پروکسی محلی کامل
دارای پروکسی‌های محلی SOCKS5 و HTTP، همراه با قابلیت تنظیم خودکار پروکسی سیستم
پس از قطع اتصال نیز تنظیمات پروکسی سیستم به‌صورت خودکار به حالت قبلی بازگردانده می‌شوند.
🔹
مدیریت پیشرفته پروفایل‌ها
امکان ساخت و مدیریت:
• پروفایل‌های اتصال چنددامنه‌ای
• پروفایل‌های Resolver
• Import و Export تنظیمات
• تهیه بکاپ از پروفایل‌ها
🔹
پری‌ست‌های آماده
تنظیمات از پیش آماده‌شده برای شرایط مختلف شبکه:
⚡️
Speed
— برای دستیابی به بیشترین سرعت
🛡
Survival
— برای پایداری بیشتر در شبکه‌های محدود
🔒
TCP Survival
— برای اتصال پایدارتر با استفاده از TCP
🔹
مانیتورینگ زنده
نمایش لحظه‌ای:
• وضعیت اتصال
• آمار ترافیک مصرفی
• اطلاعات نشست
• لاگ‌ها و رویدادهای برنامه
⚠️
هشدار امنیتی بسیار مهم
نسخه‌های رسمی WhiteDNS Desktop فقط از طریق ریپازیتوری رسمی پروژه در GitHub منتشر می‌شوند.
برای حفظ امنیت سیستم خود، برنامه را از سایت‌ها، مارکت‌ها، کانال‌ها یا منابع متفرقه دانلود نکنید.
📥
دانلود آخرین نسخه از GitHub رسمی:
https://github.com/WhiteDNS/WhiteDNS-Desktop/releases/tag/desktop-v1.2.0
📢
عضویت در کانال رسمی تلگرام پروژه:
https://t.me/whitedns
🤍
WhiteDNS Desktop</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/whitedns/1413" target="_blank">📅 11:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1412">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🌎
نسخه‌ی دسکتاپ WhiteVPN منتشر شد!
📤</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/whitedns/1412" target="_blank">📅 09:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1410">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AL4pE_QXbNMfbHc3SvEOA6Te1oYtbKFAoRMhb26x2holpVKetf9m0Q02bLIncehmu82CTKqA2hCB92uIJzmq7oQWAJsSQFyOazEslenYG2oNwFWtGtiB4Ur7bhtkpTb7KoApcatnAYTnO_7UcPapVCt4Q-Z1P7DqQAhoGBCc06mG3ycDGQW-jQEg62D_JTAauEl3rD7BR7WElSwyZlZ-IwlqxJy8ucW-wtRv4LlwwmWuIiuMw-U2w6X4YOyLIj64ReXDPhONegw4zbLXWEkj-CBnaKV0IKIgPaKqDiaZLLrr0CRHskv9vibQ4JjEi12WPDwG48NehDDRNnbBCgHjNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
نسخه‌ی دسکتاپ WhiteVPN منتشر شد!
اگر می‌خواهید روی کامپیوتر بدون درگیری با تنظیمات پیچیده به VPN وصل شوید، WhiteVPN Desktop برای شما ساخته شده است.
💻
قابل استفاده روی:
• ویندوز
• مک، هم Apple Silicon و هم Intel
• لینوکس با بسته‌های AppImage، DEB و RPM
⚡️
اتصال ساده و سریع
• اتصال با اشتراک آماده WhiteVPN
• اضافه‌کردن اشتراک شخصی
• انتخاب خودکار بهترین سرور
• انتخاب دستی کشور، نوع اتصال یا سرور دلخواه
• نمایش IP و کشور واقعی اتصال
• بررسی خودکار سلامت اتصال و جایگزینی سرور خراب
📥
واردکردن کانفیگ شخصی
• پشتیبانی از VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard
• امکان واردکردن یک یا چند کانفیگ به‌صورت هم‌زمان
• فقط کانفیگ را کپی کنید و Ctrl+V یا در مک Cmd+V بزنید
• کانفیگ‌های شخصی در بخش Manual و بالای لیست قرار می‌گیرند
🚀
تست کامل سرورها
• بررسی سالم بودن سرور
• تست پینگ واقعی
• تست سرعت دانلود
• مرتب‌سازی بر اساس کشور، پینگ، سرعت و نوع کانفیگ
• تست‌ها بدون قطع‌کردن اتصال فعلی انجام می‌شوند
🛡
تنظیمات حرفه‌ای، با ظاهر ساده
• حالت Proxy برای ویندوز، مک و لینوکس
• حالت TUN برای اتصال کامل ویندوز
• تنظیم DNS و حریم خصوصی DNS
• Split Tunneling برای مدیریت مسیر برنامه‌ها
• تنظیم IP Fronting به‌صورت خودکار یا دستی
• مشاهده گزارش‌ها برای پیدا کردن سریع مشکلات اتصال
🧰
ابزارهای کاربردی
• White IP Generator: ساخت کانفیگ با White IP و اضافه‌کردن مستقیم به برنامه
• Validator: بررسی تعداد زیادی IP یا آدرس و ذخیره نتیجه‌ها
• Full Backup: پشتیبان‌گیری کامل از تنظیمات، اشتراک‌ها و کانفیگ‌ها و بازیابی آن‌ها
🌍
رابط کاربری کامل فارسی و انگلیسی
• نمایش صحیح راست‌به‌چپ
• فونت فارسی Vazir
• محیط ساده و مدرن
• ادامه اتصال در System Tray حتی بعد از بستن پنجره
📌
چند نکته درباره نسخه اول
• حالت TUN فعلاً فقط روی ویندوز فعال است
• در لینوکس ممکن است لازم باشد Proxy سیستم را دستی تنظیم کنید
• برنامه هنوز امضای دیجیتال ندارد؛ بنابراین ویندوز یا مک ممکن است هنگام اجرای اول هشدار نمایش دهد
🔓
WhiteVPN Desktop متن‌باز است و تحت مجوز GPL-3.0 منتشر می‌شود.
⬇️
دانلود آخرین نسخه:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
اگر برنامه برایتان مفید بود، لینک آن را برای دوستانتان هم بفرستید
❤️</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/whitedns/1410" target="_blank">📅 09:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1409">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سرور های فعال WhiteDNS داشته باشید برای تست و زمان قطعی (کلیک کنید روش کپی میشه)
کلاینت اندروید و IOS از CottenDNS پشتیبانی میکنن و به زودی کلاینت ویندوز هم آماده میشه
Server #1 thx to LordofCinder
♥️
Location: Turkey
🇹🇷
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HufCfh7cgdGh4IHRvIExvcmRvZkNpbmRlciIsInNlcnZlciI6eyJkb21haW4iOiJ2LmFzaGVudGFqaXIuc2JzLCBjLmFzaGVudGFqaXIuc2l0ZSIsImVuY3J5cHRpb25fa2V5IjoiZTU1NGI4ZmI4ZGU4Mjc4ZDJmMTFlODcwNDA0NDI2OWEiLCJlbmNyeXB0aW9uX21ldGhvZCI6M319fQ
Server #2 thx to Bamdad
♥️
Location: Germany
🇩🇪
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HqfCfh6ogdGh4IHRvIEJhbWRhZCIsInNlcnZlciI6eyJkb21haW4iOiJjLmJhbWFrLnh5eiIsImVuY3J5cHRpb25fa2V5IjoiMmRkZWI5ZGYyYzJiYTRkMyIsImVuY3J5cHRpb25fbWV0aG9kIjozfX19
Server #3 thx to Araskhatare
♥️
Location: France
🇫🇷
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-Hq_Cfh7cgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InBhcmlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI1MjViNjkwYjU4ZmU0MTI0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
Server #4 thx to Araskhatare
♥️
Location: France
🇫🇷
2
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-Hq_Cfh7cgMiB0aHggdG8gQXJhc2toYXRhcmUiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiYS5hcmFzLmRwZG5zLm9yZyIsImVuY3J5cHRpb25fa2V5IjoiNzFkM2MwOWYyYmY1NmVkYSIsImVuY3J5cHRpb25fbWV0aG9kIjozfX19
Server #5 thx to Coreforge
♥️
Location: Turkey
🇹🇷
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7nwn4e3ICAgdGh4IHRvIENvcmVmb3JnZSIsInNlcnZlciI6eyJkb21haW4iOiJ2LmFub255bW91cy5vYnNlcnZlciIsImVuY3J5cHRpb25fa2V5IjoiYjI3NTAzOTE5OWIxYzhjOSIsImVuY3J5cHRpb25fbWV0aG9kIjozfX19
Server #6 thx to Araskhatare
♥️
Location: USA
🇺🇸
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7rwn4e4IDIgICB0aHggdG8gQXJhc2toYXRhcmUiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidXNhLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI5MzY5NjVjZWYzOWQzMmE5N2JlMWEzZDA4YzhiZmM5MyIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
آموزش استفاده از برنامه اندروید
👇
https://www.youtube.com/watch?v=tz8cj7HzHVI
آموزش استفاده از برنامه ios
👇
https://www.youtube.com/watch?v=filwdiPKN90
آموزش استفاده از برنامه ویندوز
👇
https://youtu.be/Mc--GlKw2wg
@whitedns</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/whitedns/1409" target="_blank">📅 04:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1407">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/3ae84e81b7.mp4?token=VQz7poP_MayPTBqx0nmDJyYsMAYoP-YGz-2Ms0nSx6sqTZi3c_MOKympHb6yNpakHVq9WRkACINkUgITTN2rkn6Omk4tK5mm2teDzJxZrmOVl8dooi4qOj1BLqHOIHDXsb43NkvX5aHXu7QnJjcbvpnwUZSbpkqBa1lx2eIo7rAxpQfb_pp2u2U6f6MeqFVk5coqjzlcfxT879aneD8bU7sVH-JvNMmt5mPd0bKiiACVbPE9bCuwTauKwjalYgtpnURSt2ccJlI7syjdB_qUaOLykwNv9C99aXb5SvHPuETACVNOOAMBwKvuvdvFOKOpm3EWvixkK0_zUbZtfGjzuw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/3ae84e81b7.mp4?token=VQz7poP_MayPTBqx0nmDJyYsMAYoP-YGz-2Ms0nSx6sqTZi3c_MOKympHb6yNpakHVq9WRkACINkUgITTN2rkn6Omk4tK5mm2teDzJxZrmOVl8dooi4qOj1BLqHOIHDXsb43NkvX5aHXu7QnJjcbvpnwUZSbpkqBa1lx2eIo7rAxpQfb_pp2u2U6f6MeqFVk5coqjzlcfxT879aneD8bU7sVH-JvNMmt5mPd0bKiiACVbPE9bCuwTauKwjalYgtpnURSt2ccJlI7syjdB_qUaOLykwNv9C99aXb5SvHPuETACVNOOAMBwKvuvdvFOKOpm3EWvixkK0_zUbZtfGjzuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
نسخه دسکتاپ
whitevpn
اماده شده است و به زودی بعد از طی مراحل آزمایش منتشر خواهد شد
@whitedns</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/whitedns/1407" target="_blank">📅 19:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1403">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
پترنیها یه اپلیکیشن مشابه v2rayng زده که به نظرم از خود v2 هم بهتره چرا؟
هسته بروز که توسط خود پترنیها داخل اپ قرار گرفته و بروز بودنش حتی از v2 هم زودتره(بیشتر آپدیت هسته v2rayng از سمت پترنیها بوده)
رابطه کاربری روان تری داره.
مهم ترین نکته اش اینه با قابلیتی که واسه
#فرگمنت
اضافه کرده شما دیگه محدودیت آپلود داخل کانفیگ هاتون ندارید(بیشتر کلودفلره) ولی بعَی سرور شخصی ها هم مشکل آپلود دارن که طبق تنظیمات پترنیها اکی میشه
🔥
دانلود اپ از گیتهاب:
💓
https://github.com/patterniha/v2rayNG/releases
تنظیمات مربوطه به آپلود:
📝
https://t.me/patt_channel_x/94?single
💡
دوستانی که پترنیها رو نمیشناسن:پتنریها خالق sni spoof و شیر و خورشید و همچنین کلی از کارای بزرگتری بوده و داشته از جمله خود v2ryang و...
@xsfilterrnet
👑
@patt_channel_x
✅</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/whitedns/1403" target="_blank">📅 15:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1402">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال  سریع‌تر و پایدارتر بوده است.  امکانات و بهبودهای جدید: •  شروع اتصال سریع‌تر •  انتخاب هوشمند بهترین سرور •  جابه‌جایی خودکار در صورت اختلال سرور •  کاهش خطا و نیاز به چندبار زدن دکمه اتصال •  بهبود Real…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/whitedns/1402" target="_blank">📅 15:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1401">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(Dᵢₐₙₐ🍓)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS_Setup_Servers.md</div>
  <div class="tg-doc-extra">3.8 KB</div>
</div>
<a href="https://t.me/whitedns/1401" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
آموزش نصب DNS اختصاصی برای WhiteDNS
آموزش کامل و
قدم‌به‌قدم
نصب و راه‌اندازی:
🟢
CottenDNS
🔵
StormDNS
🟣
MasterDNS
از تنظیم دامنه در Cloudflare تا نصب DNS و دریافت
Encryption Key
🔐
📚
آموزش به‌صورت متنی آماده شده و
لینک آموزش ویدیویی
هم داخل پست قرار گرفته.
🎥
📥
فایل آموزش رو دانلود کن و برای روز مبادا نگهش دار!
🚀
@WhiteDNS
·:¨༺
@BlueKnight_Net
༻:</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/whitedns/1401" target="_blank">📅 16:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1398">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/whitedns/1398" target="_blank">📅 12:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1397">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc0b81933.mp4?token=F7GGVzjmddtN1svWSyoYCF8gy6riVpy_xuNDHX3R4YzbsHjoIioncyQlxzbTrEzrL5qO3g64ArrPwq5V8NwHQ7oN-lQKHFSAeCrInvLfhnDfYxPvaMYK2qkLWBjN0sc_maiCOJiGVPSZBRopW8iHB_VLwXYdsLSkHXs8WqUQKl1ofw2VJYxHrJUOTc5C6I3qWKTK3k4oqx8i_1_R40XuJiP3cpwl-UI8yziHG1xvnBpTJsjHRUUW1zryfWqXNA3e6DhJhOHKqNSUM_In6HdKJm_K0zfc1wW3yNw8_4IV4ujXiO4gjVuuBgo_lDky08K1CwFv6_1JWtsiC9tNkkLr06lfZhODjsst1_VXOcdqSEvhV8O5ZR2cxO9XvOTTdCQfkb7nkswHhL7kX3LOMPxOpWwTr2khDp47o3vtiW7OaduL85mS7BFlGPK1f0ofd1C75_8VM0P3TgrTEMvey23C86wu9x2Oab0ixUbjF9OjPjSR4DSIw9WUuVvuorO7K1dXAXeXfdWN4HBosf74zdmSLgrA46rjWzezICHN8TRZbeD6vaqGiUn0xP1J8N09FKZtoAZItdffCYHOolZ5BUtcP1Li_9OtFVqdJXA4GuJV2GoCCnjzap5Dv0k_86Kil9llwRCGTGfKTeuJTXohYXArBPqsCDs64AqzQdqFIYLRHQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc0b81933.mp4?token=F7GGVzjmddtN1svWSyoYCF8gy6riVpy_xuNDHX3R4YzbsHjoIioncyQlxzbTrEzrL5qO3g64ArrPwq5V8NwHQ7oN-lQKHFSAeCrInvLfhnDfYxPvaMYK2qkLWBjN0sc_maiCOJiGVPSZBRopW8iHB_VLwXYdsLSkHXs8WqUQKl1ofw2VJYxHrJUOTc5C6I3qWKTK3k4oqx8i_1_R40XuJiP3cpwl-UI8yziHG1xvnBpTJsjHRUUW1zryfWqXNA3e6DhJhOHKqNSUM_In6HdKJm_K0zfc1wW3yNw8_4IV4ujXiO4gjVuuBgo_lDky08K1CwFv6_1JWtsiC9tNkkLr06lfZhODjsst1_VXOcdqSEvhV8O5ZR2cxO9XvOTTdCQfkb7nkswHhL7kX3LOMPxOpWwTr2khDp47o3vtiW7OaduL85mS7BFlGPK1f0ofd1C75_8VM0P3TgrTEMvey23C86wu9x2Oab0ixUbjF9OjPjSR4DSIw9WUuVvuorO7K1dXAXeXfdWN4HBosf74zdmSLgrA46rjWzezICHN8TRZbeD6vaqGiUn0xP1J8N09FKZtoAZItdffCYHOolZ5BUtcP1Li_9OtFVqdJXA4GuJV2GoCCnjzap5Dv0k_86Kil9llwRCGTGfKTeuJTXohYXArBPqsCDs64AqzQdqFIYLRHQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش دریافت دامنه رایگان و نامحدود
دیگه لازم نیست برای کانفیگ های شخصیتون دامنه بخرید.
https://youtu.be/Tiods_aCJX8
@WhiteDNS</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/whitedns/1397" target="_blank">📅 11:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1395">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دوستان عزیز،
در حال حاضر تنها مسیر درآمدزایی و تأمین هزینه‌های تیم WhiteDNS، کانال یوتیوب ماست.
❤️
برای حمایت از ادامه فعالیت‌ها و توسعه سرویس‌ها، می‌تونید کانال ما رو سابسکرایب کنید و ویدیوها رو تماشا کنید. همین حمایت ساده، کمک بزرگی به ادامه مسیر ما می‌کنه.
🔗
https://www.youtube.com/@WhiteDNS
ممنون از همراهی همیشگی شما
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/whitedns/1395" target="_blank">📅 10:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1394">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/whitedns/1394" target="_blank">📅 08:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1393">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
لطفا تست کنید و نتیجه رو با ما به اشتراک بگذارید.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/whitedns/1393" target="_blank">📅 07:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1388">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/whitedns/1388" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/whitedns/1388" target="_blank">📅 07:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1387">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lj7ATmW2RRc1UogJgUbw1gmjkVEeUrIAEIaqoiZXfVVmsJG01wovJ3epRWRsEMzIUeOc_RmZTDMejB0URPLuiXE3njlDTo5p6uTiw296N9h-nCBxOUWbGNmiZbjSaleCh50jkhoo4Y83HRHhE5NHs0rwv0ht122lR2CxSmL3g-AGOg6WEMU5qSvCKy_moZ0Wj43EL3snVG-4utIG3uqFcjDxoshB-PW3uvY32F1fr5_IehLwAWnocz8VZHCc3AEaA_C_GWgm5GRr8CfKZ3GLtMKHFSDyzMK8jxtxf6l6i3cNojOHO6NHTpeR5oQnZr8yEixCL-h-_BH6whhNis_22A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال
سریع‌تر و پایدارتر بوده است.
امکانات و بهبودهای جدید:
•  شروع اتصال سریع‌تر
•  انتخاب هوشمند بهترین سرور
•  جابه‌جایی خودکار در صورت اختلال سرور
•  کاهش خطا و نیاز به چندبار زدن دکمه اتصال
•  بهبود Real Delay Test
•  رفع مشکل متوقف‌شدن اتصال در مرحله شروع
هیچ تنظیم خاصی لازم نیست؛ فقط برنامه را به‌روزرسانی کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/whitedns/1387" target="_blank">📅 07:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1386">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⛏
اگر در اتصال به WhiteVPN مشکل خوردید مراحل زیر را اجرا کنید
۱. به صفحه تنظیات برید
۲. از گرینه حریم خصوصی DNS گرینه DOH را انتخاب کنید
۳. مقدار زیر را جاگزین کنید
https://doh.whitedns.workers.dev/dns-query</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/whitedns/1386" target="_blank">📅 17:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1378">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1EwcuX31TGqyJGOL0nryVrShrkEjLZO5xEhL0hZRNOSCsVrM48JLqUYdrvYdBNZHQ7mxUumJy_nYKgVFraDiFde9n542bqLtP7f2mYmVRo0fgayG0jQEy4FAshKZUOHqfWzej0yxq3BYZqllo7NQVr-IIl41VEYk3O37YJih-X-UEP7ngRStVLuDLQIMT3LVyv9r3nQCfkKQmeukUWA-ncq1gxv94Se3CZ9KrtzCI4OK_pSqFv0ml5glqimHBPr1Lf2wpfpxqfPiwxTvE3kyr0CDs-eup9VjA3GVFcRFoCVIAirVxCHbCM6sxulEPVxNjGuLYZdW9iTt6gr2CpaQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای  ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/whitedns/1378" target="_blank">📅 11:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1377">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpHJ6FNQOlTuFrTKdUvkq7u1peN6nQBwu8w2xN54qaH8-WhLLbaAXIOEIfouNSoJrhyAxTGSeJnzRaTM38f_1O-PbbMWk0OCA1kIVO6WaWjdgtPvW9A18HnxdMnUQECzpmBVG0Y2xi2IEYE5xE3B3mNY5jUBlENXYazDdoPq-FcAc6Z46y2nvh0_38YD2dqd_q4G5wwfqYOLF6ATkKjM15JBWZvsKHw71BL23uEkX_PsipgysKCpPOop1lFOWmohXeKSj1N0i2xx0ZjXNrQb8IolLCYcp4I_mG2KMagHUEI1HsSncdAlOWrq9gz5DQnlDe7E0SEDDQcbxv2gUgoa-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
در این نسخه، پشتیبانی رسمی از موتور
CottenDNS
به WhiteDNS اضافه شده است.
CottenDNS برای اتصال پایدارتر در شبکه‌های دارای فیلترینگ، پکت‌لاس، DNS Poisoning و اختلال شدید طراحی شده و در هر دو حالت
Proxy
و
Full VPN
قابل استفاده است.
مهم‌ترین تغییرات
* اضافه‌شدن موتور CottenDNS
* پشتیبانی از چند دامنه در هر پروفایل
* تنظیم مستقل MTU، FEC، Duplication، رمزنگاری و روش انتقال
* بهبود Import و Export پروفایل‌ها
* بهبود رابط کاربری و دسترس‌پذیری
* سازگاری بهتر با Android 15
* ادامه پشتیبانی از پروفایل‌های StormDNS و MasterDNS
این نسخه انتخاب و مدیریت روش اتصال را متناسب با شرایط مختلف شبکه ساده‌تر و انعطاف‌پذیرتر می‌کند.
📱
دانلود WhiteDNS ورژن ۱.۶.۰
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚠️
⚠️
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
@WhiteDNS</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/whitedns/1377" target="_blank">📅 04:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1375">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-text">پروژه دفید روی گوگل پلی قرار گرفت
میتونید از قسمت تنظیمات از چت ها و .. فایل پشتیبان بگیرید و بعد حذف کنید و بعدش از طریق گوگل پلی برنامه رو نصب کنید و دوباره فایل پشتیبان رو بازیابی کنید
https://play.google.com/store/apps/details?id=com.thefeed.android
میتونید با امتیاز ۵ ستاره دادن به پروژه از من حمایت کنید
🙏
❤️
❤️
❤️
ویدیو آموزشی پروژه:
https://t.me/networkti/516</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/whitedns/1375" target="_blank">📅 19:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1374">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📱
آموزش ساخت رایگان، شخصی سریع پروکسی تلگرام کاملا رایگان و بدون نیاز به سرور   https://youtu.be/epG70Xl1xGI   @WhiteDNS</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/whitedns/1374" target="_blank">📅 11:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1373">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=cB4uvrCPBc_Au0anMERWbI3I69tSd4Ruo-f_g544xzOkailoI2OB8_8bxiNtw37sI3uCdz6kg-5Du1AOJwampKDV7syTp9FGFRZuh82rJlFxEKj6TUeNC9WTmstSG09YKQscWuOnRfxKSgO5spLK-O-B9os-4LvW_o-bT5PJY_WW6DOuQhLT7ii4PPcsIbJHSPjwhxA185EfxvGvYC42BRDpG9fmBlrbQmynYCeXgAIB6XLy6ky72Y-Gm-J1xbqIDb3A8uO8BcULhJ-yF-ZjESpP5KRgC3a3Vb0o-FeEt8Y1-iPCHQnIaJcPBxjqvS72AZ1sX8MepflXcTy1GhDMSIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=cB4uvrCPBc_Au0anMERWbI3I69tSd4Ruo-f_g544xzOkailoI2OB8_8bxiNtw37sI3uCdz6kg-5Du1AOJwampKDV7syTp9FGFRZuh82rJlFxEKj6TUeNC9WTmstSG09YKQscWuOnRfxKSgO5spLK-O-B9os-4LvW_o-bT5PJY_WW6DOuQhLT7ii4PPcsIbJHSPjwhxA185EfxvGvYC42BRDpG9fmBlrbQmynYCeXgAIB6XLy6ky72Y-Gm-J1xbqIDb3A8uO8BcULhJ-yF-ZjESpP5KRgC3a3Vb0o-FeEt8Y1-iPCHQnIaJcPBxjqvS72AZ1sX8MepflXcTy1GhDMSIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
آموزش ساخت رایگان، شخصی سریع پروکسی تلگرام کاملا رایگان و بدون نیاز به سرور
https://youtu.be/epG70Xl1xGI
@WhiteDNS</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/whitedns/1373" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1371">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">3 سرور اهدای CottenDNS
لطفا تست کنید و نتیجه رو بهمون بگید ( کلیک کنید روش کپی میشه )
Server #1 thx to Araskhatare
♥️
Location: Germany
🇩🇪
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HqfCfh6ogdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Imdlcm1hbnkuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjI5ODQ0NDhjZDRkZTYxZjgiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
Server #2 thx to Araskhatare
♥️
Location: France
🇫🇷
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-Hq_Cfh7cgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InBhcmlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI1MjViNjkwYjU4ZmU0MTI0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #3 thx to Araskhatare
♥️
Location: Israel
🇮🇱
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HrvCfh7EgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiIyMjRiOWU4MjVlMzFkNWY0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
@whitedns</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/1371" target="_blank">📅 23:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1370">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/et2GHICBC7vx6sD9uTjo3-Jn-8LGU62xyVfKyubli6qxMTaaOwXDqLJT3p4gRr9CUz_uwR3Oz8UtMWE3TyFfjXeyJMyhl-y-Ylx2isXlY3P2Knl8TZ1feSbLO_1ZIEkFVN4c5LwqmtPdke_KQjV8cq8S_wt16HrqtvT9vnSuICybaGGQKMTA0Jrptc3sDWkzad8SvAIttKcN9OXJtsCwBEr-TX5kbXh7NW2G4XPwz7evCZu_kpo4kPouTTwPSn74uvf-81YO-B5tegxzWruKBdEOeQEmdJgFqK92jlO8a4DeCUx5_5JJ4IwAarbGZUSJN4-CA0VVEeLzf1nYW8cNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه مهم درباره وضعیت ممیزی امنیتی پروژه‌ها
از این پس، هر پروژه‌ای که از برنامه ممیزی امنیتی
WhiteDNS Security
خارج شود، دیگر تحت نظارت امنیتی ما نخواهد بود.
این موضوع به این معناست که:
آخرین نتیجه ممیزی تنها مربوط به نسخه‌ای است که در زمان ارزیابی بررسی شده است.
هرگونه تغییر در کد، تنظیمات، زیرساخت، وابستگی‌ها یا به‌روزرسانی‌های بعدی می‌تواند وضعیت امنیتی پروژه را تغییر دهد.
پس از خروج پروژه از فرآیند ممیزی، WhiteDNS هیچ تضمین، تأیید یا مسئولیتی نسبت به امنیت نسخه‌های جدید یا وضعیت فعلی آن پروژه نخواهد داشت.
ادامه استفاده از پروژه، صرفاً بر عهده توسعه‌دهندگان و کاربران آن است.
در صورت بازگشت پروژه به برنامه ممیزی و انجام ارزیابی مجدد، نتیجه جدید به‌صورت رسمی اعلام خواهد شد.
آخرین وضعیت معتبر هر پروژه، تنها از طریق اطلاعیه‌های رسمی WhiteDNS قابل استناد است.
@whitedns</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/whitedns/1370" target="_blank">📅 11:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1368">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">این روزها شاید همه استرس داشته باشیم
🤯
، بی‌حوصله باشیم
😑
و حالمون خوب نباشه
🥀
برای همین درست نخوانیم
📖
، درست نبینیم
👀
، ...
ولی برای اینکه نه به خودتون
🙅‍♂️
و نه به ما بد بگذره، لطفاً متن‌هایی که توی کانال می‌گذاریم را با دقت بخونید
✨
👀
ممنون
🙏
😊</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/whitedns/1368" target="_blank">📅 05:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1367">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WmWy7vm6kM6dB8SwyAj8DJrsLAcw6yVr_DSwDdfLDuCZAqS53BvWM2PtdYX3mM2Wpx-gRoUmlWy7dNsDmvHWtYK4snj7flCeKiultOdaksYTOGVdibkXaptgbBAEoObvC-YFfEgDdhKRqCWSLx58jSVljKCm0sbEO_Cq_b5sdjdNfJJT3LFtGGWWO6Rxim1gVBP3JxbdQ3UE0Wab4_kU1hzhXjEdfU81k_xzuYi3k7X0bKqAC267MXxEY5GPeqiWKZUViXZOYaYp1ZgSwWeaX2m2c3tke4ll3-7yQHuuseiVZe3LfguTzlKSYMn6ae6NZNmD6vgCqZ8tab_N5rUzOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!
هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده.
منم یه مشارکت کوچولویی روی خود هسته داشتم.
تغییرات اصلی این آپدیت:
1-
امنیت در پروتکل MASQUE:
قبلاً وقتی وصل می‌شدید، کلاینت هیچ تاییدیه‌ای از سرور نمی‌گرفت و اگر کسی وسط راه سعی می‌کرد با یه سرتیفیکیت فیک گولتون بزنه، برنامه متوجه نمی‌شد. اما الان اتصالات MASQUE سرتیفیکیت سرورهای کلادفلر رو به صورت دقیق (از طریق هش‌های SPKI) بررسی می‌کنن تا دیگه کسی نتونه ترافیک رو شنود کنه.
2-
پایداری WireGuard و Gool:
قبلاً بعضی وقتا برنامه بهتون می‌گفت متصل شدید، در حالی که دیتا اصلاً ردوبدل نمی‌شد و فقط روی یه پروکسی SOCKS5 گیر کرده بود. اما الان یه سیستم بررسی سلامت (Health Check) مداوم داره که اگر دیتایی از سمت سرور برنگرده، خودش به صورت اتوماتیک اتصال رو قطع و دوباره وصل می‌کنه.
3-
اتصال مجدد خودکار در Gool:
تو نسخه‌های قبل اگه تونل بیرونی Gool قطع می‌شد، کل فرآیند کِرَش می‌کرد و خارج می‌شد. الان Gool هم مثل بقیه پروتکل‌ها خودش هوشمندانه دوباره ریکانکت می‌کنه.
4-
فیکس شدن نشت مموری (Memory Leak):
یه باگ رو اعصاب بود که وقتی اتصالتون زیاد قطع و وصل می‌شد، تسک‌های قدیمی تو بک‌گراند باز می‌موندن و آروم‌آروم رمِ سیستم پر می‌شد. این مشکل تو تمام پروتکل‌ها کامل برطرف شد.
5-
هوشمندی در مصرف منابع:
از این به بعد Aether همون اول کار، تعداد هسته‌های CPU و مقدار رم سیستمتون رو می‌خونه و میزان اسکن همزمان (Concurrency)، بافرهای شبکه و صف‌های داخلیش رو بر همون اساس تنظیم می‌کنه. این قابلیت برای کسایی که می‌خوان ابزار رو روی روترها و بردهای ضعیف‌تر بالا بیارن فوق‌العاده‌ست.
لینک گیت‌هاب برای دانلود(نسخه‌های مک، لینوکس و ویندوز):
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.6.0
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/whitedns/1367" target="_blank">📅 05:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1362">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn-v1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">20.1 MB</div>
</div>
<a href="https://t.me/whitedns/1362" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/whitedns/1362" target="_blank">📅 05:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1361">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6JO4gNGE-i8dM7fgXGFc4_CFzOpk6COiHcAKl0hsmUdEZcIOn56mpUJkukaiFOcW4ZCLnuPwM5dhXxikz3ahMI0NfUBTqyK90BWTHc4TgGth69T-4nAQQ12bsU8KYyRq1giM1hbnvs91Y2Ic4p58HhiMYZ4H7mRuZZDRwAfjTF4e_9NecV95xvG4u_Gi38ceVMtbM0FxUVqgV60sJcvV9LjB634OcXfiUADF5mNYA9QOASYPNfUU9h5wT6h8Wp1OWP6RLn3YMYtnT9S3IT0Y7b1w5_Dsg1IIYlKNw_yld5vo5ufXI03BmuYMlKzb28PXF-7JNgBd7wmQXu9S99lBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN 1.1.0 منتشر شد!
در این نسخه چند قابلیت کاربردی اضافه کردیم تا اتصال راحت‌تر، سریع‌تر و امن‌تر باشه:
🛡
اتصال همیشگی VPN
می‌تونید WhiteVPN رو طوری تنظیم کنید که همیشه فعال بمونه و در صورت قطع شدن، دوباره متصل بشه.
🔒
امکان Kill Switch
اگر VPN قطع بشه، اینترنت هم موقتاً متوقف می‌شه تا اطلاعات شما بدون محافظت منتقل نشه.
⚡️
قابلیت Real Delay Test
حالا می‌تونید تأخیر اتصال‌ها رو بررسی کنید، نتیجه‌ها رو ببینید و سریع‌ترین گزینه رو راحت‌تر انتخاب کنید.
✨
طراحی جدید صفحه اشتراک‌ها
صفحه اشتراک‌ها ساده‌تر، مرتب‌تر و خوش‌دست‌تر شده تا مدیریت و انتخاب اشتراک‌ها راحت‌تر باشه.
همین حالا WhiteVPN رو به نسخه 1.1.0 به‌روزرسانی کنید
🤍</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1361" target="_blank">📅 05:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1360">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/FZ1whZpz2q1U6u_67DTy7uRYhVREZmvS5jtdtCYLhE90yt7Ss2nsUd2a-vu7cUn4O5Rb7wLIfnglXJkdMKpoIsdmYAK1yA3mfAjIB4LsU8Nsxpm9zS8jG7BeGLaNkTrwHnH2KftM1zVAtDBZt20nSnXba1JVFn_embahSDVNBq0PazuGCCHcNKyf7yIJSMfKhbZ5oXqjrQg6IBtUQ-oYkCF8NcPGyOWTCGgUZcXtnStawGB8vYNybFZaMNMszgutCxz7BhmDAoZFILfSZtE3W_arPGcGjsAHPKv1k4wIINOPB0RD2ZyEJbsYEAxtvsxw1xKGn_fGtozHmkBqIuKuOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام دوستان
👋
کلاینت Aether  در دو نسخه اندروید و ویندوز که به تازگی توسط کانال ما منتشر شد -دیگر توسط تیم whitedns بررسی امنیتی (audit) نخواهد شد و ما از این لحظه امنیت این کلاینت را تایید نمیکنیم
⚠️
لطفاً با مسئولیت خودتان از این کلاینت استفاده کنید و یا کلاً این کلاینت را حذف کنید
🗑
لینک نسخه اندروید و ویندوز در زیر این پیام برای شما قرار داده شده که بدانید در مورد کدام کلاینت حرف میزنیم
https://t.me/whitedns/1315
https://t.me/whitedns/1335
نکته:
کلاینت مشابهی که توسط Matin senpai انجام شده مشکلی ندارد و میتوانید با خیال راحت از آن استفاده کنید
✅
@whitedns</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/1360" target="_blank">📅 04:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1359">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1359" target="_blank">📅 10:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1357">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pFHx292dxHDSjIDrxxL-WyK1SlE6Xx7kvGxp-L3j2dVOJa9kf4nI1vaaKAEDFsOdcpv83_1zrUEvqWBQN2A9IbDT_JtGbOtjpolAweMNoX_6qBM66icioClhMDZ-7KqopFyy8JklFhGKg597DMMODVahinU34Hg7uimud8b6z8NnsKUGsU-n94bRvDIg-Ivybt6vDPTRMPgUO35XeGW6V9CZ1wVsnf-RToKi_PQRXuCTlkl4SaLdPUcB4GPNewNvuZ-KAO_M1sDDwy4bBbFVl1O3s05WnFYnWOLgJvnHz265Tfc5vnUd9jwVJmx93V8hJD91DdRT8QAAOJvs6chOrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی کانال یوتوب WhiteDNS
🌐
اگر به دنبال آموزش‌های تخصصی و کاربردی برای دور زدن فیلترینگ، پیدا کردن آی‌پی‌های تمیز و ساخت سرورهای شخصی هستید، این کانال یکی از بهترین مراجع آموزشی است!
🎓
در این کانال می‌آموزید:
🔹
آموزش صفر تا صد V2Ray
و راه‌اندازی پنل‌های ثنایی (3x-ui)
🔹
پیدا کردن آی‌پی تمیز با
WhiteDNS Scanner
🔹
راه‌اندازی
پروکسی MTProto
برای اتصال بدون قطعی تلگرام
🔹
معرفی ابزارها و کلاینت‌های مختلف (مثل CoreForge برای iOS و FlClash برای اندروید)
🔹
راهکارهای ارتباطی برای زمان قطعی کامل اینترنت
📡
و .................................
برای یادگیری ساخت فیلترشکن‌های امن و پرسرعت، همین الان به این کانال سر بزنید و سابسکرایب کنید.
👇
🔗
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/whitedns/1357" target="_blank">📅 04:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1356">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">خب با کمک دوست عزیزم Mr Arrow مشکل سرورلس (فرگمنت) هم تو نسخه
48
برطرف شد.
https://github.com/patterniha/Serverless-for-Iran
* نیازمند:
Xray-core >= 26.6.27
(v2rayNG >= 2.2.6)
* برای آپدیت کانفیگها کافیست سابسکریپشن را آپدیت کنید.
* نکات استفاده را حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/whitedns/1356" target="_blank">📅 02:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1355">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">3 سرور اهدای CottenDNS
لطفا تست کنید و نتیجه رو بهمون بگید ( کلیک کنید روش کپی میشه )
Server #1 thx to Araskhatare
♥️
Location: Germany
🇩🇪
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HqfCfh6ogdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Imdlcm1hbnkuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjI5ODQ0NDhjZDRkZTYxZjgiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
Server #2 thx to Araskhatare
♥️
Location: France
🇫🇷
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-Hq_Cfh7cgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InBhcmlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI1MjViNjkwYjU4ZmU0MTI0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #3 thx to Araskhatare
♥️
Location: Israel
🇮🇱
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HrvCfh7EgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiIyMjRiOWU4MjVlMzFkNWY0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
@whitedns</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/whitedns/1355" target="_blank">📅 18:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1354">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS   cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcn…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/whitedns/1354" target="_blank">📅 13:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1353">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/whitedns/1353" target="_blank">📅 10:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1348">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.6.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.8 MB</div>
</div>
<a href="https://t.me/whitedns/1348" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/whitedns/1348" target="_blank">📅 10:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1347">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwfaVmV0SFUtInyIuKJQVYILD8XAevHAr5bHpUuHIP7C4ie9XN2-5cavpjDft-TG_-3G2j48_WO33rBwmrU-fX3R1cWKVIQoAjdjpbjGcZj9Pnl46_n5DeaOU6VgUGEritTGBGNr4gnsQhBdSARkCjHwuDFR8tpRq9ldH763bbG05Sg4oDHUIMaDM9Ev_CddwLlrLskH-R0aLNGj8gscYoEAo3xTglFZGX5dTra8H945JG8rdLMc_KeaQP3Tkz1R6c0A0NVBSksWKD6UAGi9XpfVyjk9lEmbxK2qGpM1DRPK-t2eZQ8YW0Wsw9FPIs-qtcytS0EMssHyl1S1ZcoKGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
در این نسخه، پشتیبانی رسمی از موتور
CottenDNS
به WhiteDNS اضافه شده است.
CottenDNS برای اتصال پایدارتر در شبکه‌های دارای فیلترینگ، پکت‌لاس، DNS Poisoning و اختلال شدید طراحی شده و در هر دو حالت
Proxy
و
Full VPN
قابل استفاده است.
مهم‌ترین تغییرات
* اضافه‌شدن موتور CottenDNS
* پشتیبانی از چند دامنه در هر پروفایل
* تنظیم مستقل MTU، FEC، Duplication، رمزنگاری و روش انتقال
* بهبود Import و Export پروفایل‌ها
* بهبود رابط کاربری و دسترس‌پذیری
* سازگاری بهتر با Android 15
* ادامه پشتیبانی از پروفایل‌های StormDNS و MasterDNS
این نسخه انتخاب و مدیریت روش اتصال را متناسب با شرایط مختلف شبکه ساده‌تر و انعطاف‌پذیرتر می‌کند.
📱
دانلود WhiteDNS ورژن ۱.۶.۰
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚠️
⚠️
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
@WhiteDNS</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/whitedns/1347" target="_blank">📅 10:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1346">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🌎
دوستانی که با جزئیات فنی پروژه آشنا نیستند، به زبان ساده
CottenDNS نسخه‌ای کامل‌تر و پیشرفته‌تر از پروژه‌های MasterDNS و StormDNS
است.
تیم ما طی چند ماه گذشته، با استفاده از تجربه‌هایی که از قطعی و اختلال گسترده اینترنت به دست آوردیم، روی توسعه و بهبود این پروژه کار کرده است تا اتصال پایدارتر و سازگاری بیشتری با شرایط مختلف شبکه داشته باشد.
نسخه جدید اپلیکیشن
WhiteDNS
که تا ساعاتی دیگر منتشر می‌شود، از سرورهای CottenDNS پشتیبانی خواهد کرد.
هم‌زمان با انتشار نسخه جدید، یک سرور عمومی CottenDNS نیز در اختیار شما قرار می‌دهیم تا بتوانید بدون نیاز به راه‌اندازی سرور شخصی از آن استفاده کنید.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/1346" target="_blank">📅 10:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1345">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚀
معرفی پروژه CottenDNS
https://github.com/WhiteDNS/CottenDNS
نسخه پایدار CottenDNS با تمرکز بر اتصال بهتر و پایدارتر در شبکه‌های دارای فیلترینگ، اختلال DNS، پکت‌لاس و تأخیر بالا منتشر شد.
در معماری جدید، سرور به‌صورت پویا با تنظیمات هر کاربر هماهنگ می‌شود. یعنی کاربران می‌توانند بدون تغییر کانفیگ سرور، روش انتقال داده، نوع رمزنگاری، MTU، فشرده‌سازی و قابلیت‌های بازیابی بسته‌های ازدست‌رفته را متناسب با کیفیت اینترنت خود انتخاب کنند.
مهم‌ترین قابلیت‌ها
🔹
سازگاری با شرایط مختلف شبکه
اتصال می‌تواند از طریق UDP و TCP روی پورت 53 و همچنین DoT و DoH انجام شود. اگر یک مسیر مسدود یا دچار اختلال شود، کلاینت می‌تواند از مسیر جایگزین استفاده کند.
🔹
مقاومت بیشتر در برابر پکت‌لاس
CottenDNS با استفاده از ارسال مجدد هوشمند بسته‌ها، Duplication و فناوری FEC تلاش می‌کند اطلاعات ازدست‌رفته را بازیابی کند. این قابلیت‌ها بر اساس وضعیت شبکه به‌صورت خودکار فعال یا غیرفعال می‌شوند تا سربار اضافی ایجاد نشود.
🔹
مدیریت هوشمند Resolverها
Resolverها از نظر سرعت، تأخیر، پکت‌لاس و سلامت بررسی می‌شوند. Resolverهای خراب به‌صورت خودکار کنار گذاشته شده و پس از بهبود دوباره وارد چرخه می‌شوند.
🔹
تنظیم خودکار MTU
کلاینت اندازه مناسب بسته‌ها را برای آپلود و دانلود پیدا می‌کند تا احتمال شکسته‌شدن یا ازدست‌رفتن بسته‌ها کاهش پیدا کند.
🔹
مقابله با DNS Poisoning
با استفاده از روش‌هایی مانند Transaction ID تصادفی، EDNS Cookie، تغییر شکل درخواست‌های DNS و ارسال از چند دامنه مختلف، مقاومت اتصال در برابر پاسخ‌های جعلی و دست‌کاری‌شده افزایش یافته است.
🔹
انتقال داده با فرمت‌های مختلف DNS
داده‌ها می‌توانند با رکوردهای TXT، CNAME، A، NULL و HTTPS/SVCB منتقل شوند. کلاینت می‌تواند بسته به محدودیت شبکه بین این روش‌ها جابه‌جا شود.
🔹
امنیت و رمزنگاری
روش‌های AES-GCM، ChaCha20، XOR و الگوریتم‌های قابل تنظیم پشتیبانی می‌شوند. نوع رمزنگاری هر کلاینت به‌صورت امن و مستقل شناسایی می‌شود.
🔹
سازگاری با نسخه‌های قبلی
کلاینت‌های جدید CottenDNS و کلاینت‌های قدیمی MasterDNS و StormDNS می‌توانند هم‌زمان به یک سرور متصل شوند. بنابراین کاربران قدیمی برای ادامه استفاده نیازی به تغییر فوری ندارند.
در مجموع، سرور CottenDNS امکانات مختلف را فراهم می‌کند و هر کلاینت بر اساس شرایط اینترنت خود، بهترین ترکیب اتصال را انتخاب می‌کند.
❤️
Thanks to
@masterdnsvpn
@WhiteDNS</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/1345" target="_blank">📅 10:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1344">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Q9_adATeITqEoOKgz_HmnsWDUk23gNNcBO2oZDbqYyLriwMECgKQnBvkg5lAYw7Gqz1_65vwQ1SRLqxVaAFiLnsRtrG73wzts_tVcza6bLjCOGzyOojerocup8taw8TTdgLjhhiQaM89e5KQz5UW8PiWGgOWExfY_aXD9AhzOAZ8ZVpX7Qo_p2a-tnrGwB-Lz0LKaEjq2cFDrWcGPJbUSVf0YrBZYAxVj6s6zDFJ0BEL2woLTnsULDu-PmUJlyYDUoZ5kloADq7upFs13GambTqS_v_TqveQhK4meJLvoqf7KMV-if3KCSOrVIKHkIjo1f-t7ARAMnkdEtysxGrT6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضویت
در گروه whitedns
در گروه اختصاصی ما عضو شوید لطفا
🤝
@whitedns</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/whitedns/1344" target="_blank">📅 09:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1339">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn-v1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">20.1 MB</div>
</div>
<a href="https://t.me/whitedns/1339" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/whitedns/1339" target="_blank">📅 09:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1338">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l89Pip7wAE722dHbPBDlEv5E2I-xQw3GDwaY6-ltrjhFtjqtSukLmvM1IZc43jMLez1ZUB5aGTwOWxnFb6LMVPYAe8SVNCqUhc2w_v3GYhHp3L8ETxNEQCFROATVtBjIBmpkY80KXgGi3OoGWY82iONhJTFNRKCxI0KxD8uXPCU8eQIQhE8tkZTgqEHtJS3mwAYVyoQs1CxUhik_SbzcIBe8YxDVDgsgdNK4QlNODn0YnsaqrN-WzV0x-7l7yGkrGVGU1v1YGirZf_TZxYkD68102LeV8uOt_dOTJFdcxbmO8X1GZR2QyOTg6SiDNpGWYosWNxC54GuNF6VAjrVzEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN 1.1.0 منتشر شد!
در این نسخه چند قابلیت کاربردی اضافه کردیم تا اتصال راحت‌تر، سریع‌تر و امن‌تر باشه:
🛡
اتصال همیشگی VPN
می‌تونید WhiteVPN رو طوری تنظیم کنید که همیشه فعال بمونه و در صورت قطع شدن، دوباره متصل بشه.
🔒
امکان Kill Switch
اگر VPN قطع بشه، اینترنت هم موقتاً متوقف می‌شه تا اطلاعات شما بدون محافظت منتقل نشه.
⚡️
قابلیت Real Delay Test
حالا می‌تونید تأخیر اتصال‌ها رو بررسی کنید، نتیجه‌ها رو ببینید و سریع‌ترین گزینه رو راحت‌تر انتخاب کنید.
✨
طراحی جدید صفحه اشتراک‌ها
صفحه اشتراک‌ها ساده‌تر، مرتب‌تر و خوش‌دست‌تر شده تا مدیریت و انتخاب اشتراک‌ها راحت‌تر باشه.
همین حالا WhiteVPN رو به نسخه 1.1.0 به‌روزرسانی کنید
🤍</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/whitedns/1338" target="_blank">📅 09:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1337">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gokWFAEV8UvPqRsLWHb4C4OqHIijdxoCxe2mam_g128McVFz_984-7lmw3rWKQdw64sbN4hQcAlOEA1Ixls0a9x_tpC3C_Zn0XrYagFUtP3mYP6AZ-kOr7jDZ9t2FrUv4csuDTocfpEDjyKjMRyA8GlQ0uabtD_5oVZ82tvkJd1E-DFEKzifXOFiF7ffO_weMWr_LG-FKd7KCnBdGfUFTyzxKFjAxJlN78Euu8naNDtVFTHGeC_9-o_QojsK3PeRdW7uuQlgF7VOlnB855UEDPANMHX2ZwEJOXW8CaXbbkzr5UbOFBNi2uY7nYUEuYf9Dcky9JuVYmDUL8M6Bome-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
👋
:
حالا همیشه هم پست برنامه و توضیح نگذاریم، بعضی وقتها یکم حرف بزنیم با هم، اینجا همه با هم داریم کار را جلو می‌بریم
🤝
✨
برای اینکه یک پروژه درست بشه ساعت‌ها وقت و هزینه صرف میشه تا به دست تو برسه
💸
⏳
، وقت و هزینه‌ای که میشد گذاشته نشه، زمانی که میشد در کنار دوست و خانواده بود و یا اصلاً رفت عشق و حال کرد
😔
💔
. اغلب دولوپرهای این تیم کلاً نیازی به بودن اینجا ندارند، فقط احساس دین می‌کنند
🙏
.
شما میتونی با لایک
👍
و دیس‌لایک
👎
، پروژه را تایید کنید یا ردش کنی و یا با قلب
❤️
حمایت کنی و ....
خطاب به اون چند نفر :
اینکه تو اینقدر بی‌شخصیت هستی که آیکن
🤮
می‌گذاری این فقط یک چیز را می‌رسونه، تو لیاقت این را نداری که کوچکترین خدماتی حتی با دریافت هزینه بهت داده بشه
🚫
🛠️
. تو همون کسی که اصلاً برات مهم نیست چی به مردمت می‌گذره، برات هیچی مهم نیست
🤷‍♂️
.
متاسفانه تو جرات نداری بیای توی گروه‌ها خودت را نشون بدی و بحث فنی کنی
💻
🛑
، والا تکلیف مشخص میشه.
یک تعداد زیادی از شماها که همراه ما هستند یکی از یکی خوب‌تر و مایه انرژی ما و بقیه هستید
🔥
⭐
، دلیل اینکه ادامه می‌دیم شماها هستید، والا کار ما خیلی وقت هست که تمام شد
🏁
.
ارادتمند
👋
ویسپر
🎤
تیم whitedns
🛡️</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/whitedns/1337" target="_blank">📅 08:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1335">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/snENz85gMJNYOxWjxHJsBlR_KimC-qLG3JOAWmVjA6MxxCd21ysOwtk4e8pK0b-M7JATjyIzLcOqKXktUZSfYKmV5oYFTIutGgiTgwc8JaJnILHLM_5o10iu_C4c88IJWjt7FR9rKqzIE8T36F-EoGDkFXPkNGF2eGKtrJPAVl1JZkC5mxhuuebp_aNZF6JriBub2kMOw4QrMlDpBjgxM8X5Egwk_rt2a0iIIsXcE3OAAJV36spbadL6EF8njQhFQXZSika_dt0Woj1ono1KFJoTNCsiWaGNxUGutOk41S5u9Ul3bOcnt98PeAxUfJ1yqapQXiW363Pl0JyjYJbq-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Aether Desktop اومد! — آزادی، با یک لمس
🔥
بالاخره نسخهٔ ویندوزی Aether رسید!
🎉
همون اپ محبوب اندرویدی، حالا روی ویندوز — با همون ظاهر، همون آیکون و همون هستهٔ قدرتمند. نسخهٔ 1.0.0 اولین انتشار دسکتاپه و هیچی از نسخهٔ اندروید کم نداره!
✨
چی داره؟
🔌
اتصال قدرتمند:
▫️
۴ پروتکل: Smart (انتخاب خودکار) · MASQUE · WireGuard · WARP×2
▫️
۵ حالت اسکن: از Turbo تا Ironclad
▫️
اتصال مجدد خودکار تا ۵ بار + انتخاب هوشمند پروتکل اگه یکی جواب نداد
▫️
پشتیبانی IPv4، IPv6 یا هر دو باهم
▫️
نمایش زندهٔ سرعت، پینگ، سرور و IP با پرچم کشور
🏳️
🎨
رابط کاربری خیره کننده و زیبا :
▫️
کاملاً دوزبانه (فارسی و انگلیسی) با پشتیبانی کامل راست‌به‌چپ
▫️
تم تیره با طراحی دقیقاً مثل موبایل، بهینه برای مانیتورهای بزرگ
▫️
نوار عنوان به سبک ویندوز ۱۱
⚙️
تنظیمات پیشرفته:
▫️
نویز (از سبک تا تهاجمی و GFW) · MTU دلخواه · Fragment · ECH
▫️
تونل تفکیکی (Split Tunneling) — انتخاب کن کدوم برنامه‌ها از تونل رد بشن
📡
اشتراک با بقیه دستگاه‌ها:
▫️
SOCKS5 روی پورت 10810 و HTTP روی 10811
▫️
هر دو پورت خودکار پروتکل رو تشخیص می‌دن — هر کدومو هرجا بزنی کار می‌کنه!
🛠
عیب‌یابی حرفه‌ای:
▫️
تست زندهٔ اتصال + بررسی ۶ موردی محیط سیستم
▫️
کنسول لاگ زنده و رنگی با دکمهٔ کپی
🪟
مخصوص ویندوز:
▫️
تونل واقعی سطح سیستم با درایور رسمی و امضاشدهٔ مایکروسافت (Wintun)
▫️
پروکسی سیستمی خودکار تنظیم می‌شه و موقع قطع، برمی‌گرده سر جاش
▫️
نیازی به Visual C++ نداره؛ WebView2 هم نبود، خودش نصبش می‌کنه
📦
دانلود:
▫️
نصب‌کنندهٔ گرافیکی برای ویندوز ۶۴ و ۳۲ بیتی
▫️
نسخهٔ پرتابل بدون نصب — هیچ ردی روی سیستم نمی‌ذاره!
👌
▫️
فایل SHA256 برای راستی‌آزمایی سلامت فایل‌ها
⚡️
ساخته‌شده با Rust + Tauri 2 — یعنی حجم نصب فقط چند مگابایته، نه ۱۰۰ مگ مثل اپ‌های Electron! کل بیلد و انتشار هم صددرصد خودکار با GitHub Actions انجام می‌شه، بدون هیچ دخالت دستی.
📋
پیش‌نیاز: ویندوز ۱۰ (نسخهٔ ۱۸۰۹ به بالا) + دسترسی Administrator برای ساخت آداپتور شبکه
📄
لایسنس: MIT — کاملاً متن‌باز و رایگان
💙
⬇️
همین الان از بخش Releases گیت‌هاب دانلود کن و آزادی رو با یک کلیک تجربه کن!
📥
دانلود مستقیم از گیت هاب
https://github.com/QW-AI-Code/Aether_Desktop/releases/
سلام دوستان عزیز
✋
یه یادآوری مهم که حتماً بخونیدش
👇
برای اینکه اپ (چه نسخه اندروید چه ویندوز) براتون وصل شه، این چند تا نکته رو رعایت کنید تا بهترین نتیجه رو بگیرید:
⏳
رو هر پروتکل ۱ تا ۳ دقیقه صبر کنید تا وصل شه. بسته به اپراتور و منطقه‌تون این زمان فرق می‌کنه، عجله نکنید.
🔄
پروتکل‌ها و تنظیمات مختلف رو تست کنید. چرا؟ چون DPI هر سیم‌کارت با سیم‌کارت دیگه، هر منطقه با منطقه دیگه و هر شهر با شهر دیگه فرق داره.
📱
اگه با موبایل وصل نشدید: چند بار گوشی رو ببرید رو حالت هواپیما و برگردونید تا رنج آی‌پی‌تون عوض شه، بعد دوباره پروتکل‌های مختلف رو تست کنید. خلاصه باید قلق DPI اپراتور و منطقه خودتون دستتون بیاد
😉
📶
اگه با وای‌فای هستید: مودم رو ۱ تا ۲ دقیقه خاموش کنید تا رنج آی‌پی عوض شه، بعد دوباره با پروتکل‌ها و تنظیمات مختلف امتحان کنید.
❌
اگه بازم وصل نشد، یعنی این وی‌پی‌ان با نت شما جواب نمی‌ده و باید برید سراغ وی‌پی‌انی که با نت شما سازگاره.
⚠️
و نکته آخر: بعضی از کاربرا میگن این اپ مشکل داره و واسشون کار نمیکنه.
اگه مشکل از خود اپ بود، نباید برای هیچ‌کس کار می‌کرد! همونطور که می‌دونید برای خیلی‌ها داره کار می‌کنه و هر کسی تجربه متفاوتی داره.
پس اگه برای شما وصل نمی‌شه، مشکل از Aether نیست؛ مشکل از DPIایه که رو اپراتور شماست و جلوی کار کردن اپ رو می‌گیره.
#VPN
#فیلترشکن
#Aether
#ویندوز
#متن_باز</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1335" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1334">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8d366d7.mp4?token=okDUd7y6IGnztdY15zYEalcrvMsaCegR17KfKdB_b3VQMdySbTB4004HgzdGmOrDN-lazOoInO7PxglxOqVqDPKOgVes6cZww-7kxeXeYz0MjHtIGD8LnMnbPwBXBMsP8uYia0xGg0OdGNpNWmdXUcnTkg74jUolwUyi7zrRz0M4MyO_rX7XZcAOUbnFvrUJPXnwuq1KG8dkMvvNHjhu7PAhCmZVuN2iW3Tl5sgvd0q-CBppCYx3Vi9Re7JW6mg7i-v5m8PwLB-QY5WKkbe_NAPoB96u0lKugIFSEgIrtTr7bT-9PLzlf2MClKPqxcIlPYNVRE17kpSAIC_RLp7FjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8d366d7.mp4?token=okDUd7y6IGnztdY15zYEalcrvMsaCegR17KfKdB_b3VQMdySbTB4004HgzdGmOrDN-lazOoInO7PxglxOqVqDPKOgVes6cZww-7kxeXeYz0MjHtIGD8LnMnbPwBXBMsP8uYia0xGg0OdGNpNWmdXUcnTkg74jUolwUyi7zrRz0M4MyO_rX7XZcAOUbnFvrUJPXnwuq1KG8dkMvvNHjhu7PAhCmZVuN2iW3Tl5sgvd0q-CBppCYx3Vi9Re7JW6mg7i-v5m8PwLB-QY5WKkbe_NAPoB96u0lKugIFSEgIrtTr7bT-9PLzlf2MClKPqxcIlPYNVRE17kpSAIC_RLp7FjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">UAC SNI Spoofer Desktop
نسخه 1.0.6
━━━━━━━━━━━━━━━━━━
تغییرات جدید نسخه 1.0.6
• قابلیت Mobile Gateway اضافه شد. دستگاه‌های متصل به شبکه وای‌فای مشترک می‌توانند بدون تغییر تنظیمات Proxy، IP یا DHCP از VPN کامپیوتر استفاده کنند.
• امکان پینگ‌گرفتن از کانفیگ‌های موجود در تب Configs و مرتب‌سازی آن‌ها براساس کمترین پینگ یا کشور اضافه شد.
• باگ‌های جزئی بخش SNI Config Maker برطرف شدند. اکنون کانفیگ‌های بیشتری از مخازن شناسایی، دریافت و پردازش می‌شوند.
• مشکل فعال‌نشدن دستی کانفیگ‌ها، به‌خصوص هنگام استفاده از Auto Mode، برطرف شد.
━━━━━━━━━━━━━━━━━━
لینک دریافت نسخه 1.0.6:
https://github.com/Floxu1/UAC-SNI-Spoofer-Windows/releases/tag/1.0.6
لینک گیت‌هاب پروژه:
https://github.com/Floxu1/UAC-SNI-Spoofer-Windows
t.me/UacSniSpoofer</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/whitedns/1334" target="_blank">📅 00:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1333">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🌎
نسخه جدید WhiteVPN 1.1.0 منتشر شد!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1333" target="_blank">📅 17:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1328">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn-v1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">20.1 MB</div>
</div>
<a href="https://t.me/whitedns/1328" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/whitedns/1328" target="_blank">📅 17:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1327">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba164guDsFCeh9L5NoTVuPgikvPR9_UXe5t9aBGDjzYSmfpOHpVXDki_dCTB1O-WCDUQskpMC55udYFtyggHlWIXn5tko8_L7ZbQADciLVkXFEN5v01DHvO-NCe0U70Grx_mu38lzv-KZO42yQYIGlHogPrRy0c0nacskImy4hNRsTbTiUn13aO0EMwgMiyr7N4Nh9DaE6RQ-m3VlI1K_hHkSM48nEueTY9cZ4PqIUcEUAu8lld269wNdA3SE-OUGACa9lZLDmLRspxPNhLm-kil7ZHdrnBnD4BZ-jA33Z6SDXkc_ERYXU5PF_iLRIevOg6SGAvu6BMqgug5zf3Qmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN 1.1.0 منتشر شد!
در این نسخه چند قابلیت کاربردی اضافه کردیم تا اتصال راحت‌تر، سریع‌تر و امن‌تر باشه:
🛡
اتصال همیشگی VPN
می‌تونید WhiteVPN رو طوری تنظیم کنید که همیشه فعال بمونه و در صورت قطع شدن، دوباره متصل بشه.
🔒
امکان Kill Switch
اگر VPN قطع بشه، اینترنت هم موقتاً متوقف می‌شه تا اطلاعات شما بدون محافظت منتقل نشه.
⚡️
قابلیت Real Delay Test
حالا می‌تونید تأخیر اتصال‌ها رو بررسی کنید، نتیجه‌ها رو ببینید و سریع‌ترین گزینه رو راحت‌تر انتخاب کنید.
✨
طراحی جدید صفحه اشتراک‌ها
صفحه اشتراک‌ها ساده‌تر، مرتب‌تر و خوش‌دست‌تر شده تا مدیریت و انتخاب اشتراک‌ها راحت‌تر باشه.
همین حالا WhiteVPN رو به نسخه 1.1.0 به‌روزرسانی کنید
🤍</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/whitedns/1327" target="_blank">📅 17:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1326">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/iME62ARKMot2lXLJVboFaUiX4O862-GAxfhtwz_B2P4fFep1BXuUV3FH0-JxfTIjdIraLKEw48UN3h4p2fAjCj1X2o-JSGEAU1i4kkz6CeVUDvZhkVMjnkAU093bhr_0QC9gmHV5QuBd7kcyw5T8Ad1aRRuw4QSIyKXhjhQxo0xjfUPINheVWk9Yj4ygGqoxMWt29wcG8vZynJPd7r7tuo2ca8g3CnTCz-YRHjf_VuGc7qeOzsYi_b7XhiEFETBoRwz2D1YL-qjKKUCUOVxBB4uSbbOl7gQ1gYXBoyyvcK9lQQZMhWBtyZiY0PU91M8zhWJCBy-0kTbH3o1xTSivmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1326" target="_blank">📅 10:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1325">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-poll">
<h4>📊 از چه دستگاهی استفاده میکنید ؟</h4>
<ul>
<li>✓ اندروید</li>
<li>✓ اپل</li>
<li>✓ مک</li>
<li>✓ ویندوز</li>
<li>✓ لینوکس</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/whitedns/1325" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1324">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ARf1dBivdC69BxYCpIQn-SlxDBixB0-46s8eDqpsXyhlypYBPjGLxTkGnHpVqjU311rNyYdApJS4qQZMUAaJABFOgjdrQpIRGCAcC8JioZChUe_JbsXSxtbmwC_me4LLK24CYAMSJAjtJSx3CmeChN4pCz2XHwpyK3_o04ojmK9yqn1Sts9mc5zbvGvS3Wg3xBSKgbDu0oeXFRqNoJZTi5PBoa0cLnmPcPCF4IGn6sx6qOnXfAitE9VayJD2qE2_kwuaTK3rqRHGRXA2gx22QrXhTHVvq7bFNnSAjooC4um3zFpr-PHXg7Z-TnTPC8hcGTR2uSwiZLHqChwtriWB7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/whitedns/1324" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
