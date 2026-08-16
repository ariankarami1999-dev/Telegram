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
<img src="https://cdn1.telesco.pe/file/FqXQVqAtQrjEp1ZTcshg1l9JVNjTVbRvtj7TyFWYuah98IrbkOT1pfeBCRj0iSw4VpzM845uh_4gCOXHQwgv1Oi3l9u9m6az4X8VnGa1tJaSGK_JiNdBGchnaEZs5dxQm0TKfxqJhm2eMf-kpEA1Z9zS-gztC9F-_BIqaVbn0ZCQuUX9wZuZz9c4VzfLeGc9J1kJcK_DQI9TL4HTXCGA9I9AKZ0E60kMGe_cTDOmHexDJbquX4Kp_Xb8TgJjWV_p4crJ01eMnbAox0msFM_84LSpUElQd8xoKJnr9FTn5uGeR32EtKZjfjj3kk_uTRnik8iYZD9HPn9DidYI0ojpUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 01:11:09</div>
<hr>

<div class="tg-post" id="msg-4971">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ویدئوی رفع مشکل آپلود کانفیگ‌های کلودفلر و دور زدن فیلترینگ
Workers.dev
در حال ادیت توسط ادیتور عزیزه و به محض اینکه تموم بشه، آپلود می‌کنم واستون</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/MatinSenPaii/4971" target="_blank">📅 23:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O5vnlPPWxlKOKUotVipa5TK0pGDWuBuOLU8BlvmZ2xC33s3B69wcvtT082gbIkqbFfciD7w_mvnWzhMyj2iN5oEq7qOvv7Q41_ej6Xh7eCPrRNUIn6Bc2fj2jIKSYStOal1sZM5kiEni8cqfcbPStgBYkcmtSTDt1FyT7aTd1LJrFY9xH4ndbhmOdyybGVMnU0F_sHto2SS2WWrZBTVqkNwYrUAdRDamJUlNKVhyIOZBDUf99-1sO_13We8Ys0PC7StMeQEUNXQcnfF560k4fh_-EFDxuQIQW8ZGBsYSliDltvsRDc_c_Agp34_cDvxEm_TcayuvDEK5v6N6oNpPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزهای باحالی قراره داشته باشیم به زودی
🔫
از
🟩
می‌تونید فالو کنید اگه دوست داشتید:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/MatinSenPaii/4970" target="_blank">📅 19:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">با این آموزش، نه تنها محدودیت سرعت آپلودی دیگه وجود نداره، پلکه پایداری خیلی خیلی بیشتره روی همراه اول هم هستم</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/4969" target="_blank">📅 15:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RDv6lv5ePp65JomKMz2GTyMQHIL4c3Jz9Ep7-0jX_MRQlbinYWLsRB6enX6yTfy1T_IXQwPZDPDsT92TTC-XhrfAXD1QzaERemLbK-35ij-995TwrJ39MIUPnuxcx6FF2lNmcH-37AMCnUudPJ96VO9ckaJDHEGy127f74xyCCvLyehRJCS2k6pN8RR01A4jCMIToeRjdTvm7VBq4Hppa44FG2-FBWunfUJZ1ImcdgrankgoM22Cuy3F4mUAs8Fj5ZvAcaO7PZsZ_2mdnPfRQTQUiWspzxkNxcasRgYkgzcp0xt64Rb1lVWP3YDUQ1snCipsmfe4lMRo_CObVazl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/4968" target="_blank">📅 15:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/H4m84MfuwndS5JMf2opLDP-0E9EO4MMlzpmbqrOVL73ZUHWy23NCFHQ5aDsaZ7CJ2z53Oij7NAANNuAKfcXGr5mbsJ1xW0DagRV8s0bf2rZovZWUYiwm3rkYaN85mDnCA84_sbOCt7omDN1g0qdX91DLRrW2Oj7eLH3wan4EoHmzgDJ78IbSjtJnJs6javXSg8FGI4qemK7NZJzvl5ROsZ-NeEn88CeEGeJtT_o_3FR9Gu0FNXnf90OcEcBmqjVkdVzzimGUsFCNz_EHaeKMtMvBUa0ipGjJvFV0R8lLQY6qi1a3y36DNN0qALvgUs8XCbgUpISiwEN1pCHDdj2Z7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/4967" target="_blank">📅 07:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/4966" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:
Android
:
https://t.me/patt_channel_x/91?single
Windows
:
https://t.me/patt_channel_x/101?single
Android/Windows/Mac/iOS/Linux
: Use Xray-core custom-json-config and change/add --> address, finalMask, fingerprint, cipherSuites</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/MatinSenPaii/4965" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4964" target="_blank">📅 00:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4963" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تمام #نکات واسه مشکل فیلتر شدن worker رو داخل این پست میگم:</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4962" target="_blank">📅 22:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:  1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴): https://github.com/2dust/v2rayNG/releases/tag/2.3.4 یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید برای آیفون هم Sterisand آخرین…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4961" target="_blank">📅 22:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dxTevpzxWYxQWbNblAd3PGtr4h0khPt6BUYdMfcYCvSUkDMIQnxfWS1MKwE9qp2cASmQX-WhcebsRlLZk21TzmBYZMDYa6dt7tquA1cC7CqWZ6jnWwS62iIZZq_xumtUVyB1t7-TeaJ2SMf4F9buhBarahGffSIhNzGNrxdATisL0x3ybCKCee5JVE74kz74DVB8imgqkq_cqy9BW_J2u7F1-Gz-V10oekXIk7eUObWTpREF0k9IIRYaxjGhvsPHSsulb1Qi_st6422DArInfaCztw1rJUIHHdGqUtUA3bvcioKnU-j-3klU53vHwp2rTTIORqzzRXjmHPIUP04u-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:
1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴):
https://github.com/2dust/v2rayNG/releases/tag/2.3.4
یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید
برای آیفون هم Sterisand آخرین نسخه کار می‌کنه
2-
این پروژه
از دوست عزیزمون Hidden-Node با الهام گرفتن از نکته‌ای که Patterniha
اینجا
گفته بود، نوشته شده و اوپن سورسه و کانفیگتون هم جایی ذخیره نمیشه:
http://hidden-node.github.io/proxy-builder
3- وارد سایت بالا که شدید، روی بخش Fragment + Fingerprint کلیک کنید
4- کانفیگتون رو کپی، و اینجا Paste کنید
5- پایین، روی Enhance بزنید و بعدش کانفیگ جدید رو کپی و توی
v2rayNG  2.3.4
v2rayN   7.24.7
برای آیفون هم Sterisand نسخه آخر
پیست کنید و به راحتی کار می‌کنه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4960" target="_blank">📅 21:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l7cac912oVLH2p0ID315ieu9pcC4zRQGq8AMIHEXarbbixGx7UpTVuLNuVw95YKNSg2iPT73zG014j-_3_9Bvpv8ikUhKcCYMkpCssWocYWSTUUi0gLoypYTq2-69wLtgcLQGA_LpzzExDegNsHj5tkONIb9elInS_2Wq9tULgyWrQPBuuJlo0DIlVA-iYiDc-WrKr5h-ajZ09zOgn_ZgvLdXhDDQQpQtZnQVKkRe6q7x8j13arKag82pzE1FpVxs6KzFaJw6ctn2Wd5_3hz7P8uCoAlOGFjEFWxzW8VIzB9mi0i8usC_tJtyqARFrqv5ZOhQBVlSaSDaJQLLRCEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست پترن عیان شد
پنل ما جوان شد
مشکل رو حل کردم با کمک Hidden-Node عزیز. الان آموزششو می‌ذارم</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/4959" target="_blank">📅 21:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR18OJ0IeKbhHcYAXVdLYnQQ0LY2p24qtRTJGIjkAwqCh6DV3_zfjkYY_6qjIpkKVsOcByXOwKVH1SqonxeStmdYWSDuIfGaemoiTIAEIyKWaKqNbL_oEyni-j4vHua26jtKoJ69W0hPPTTtr0PBnp1XzWC554sTyqyMPIgZG7oMEbuT3JHOAmdiEUd_pWF-_lrwCRLjmMjfICC_dlGQEXzSDokYgLkhNMSAK0ndj7qMh8o4OFOLlAjxSX3aDRD-IVFkktrU_YFtZskDjvRfzpn5xGDU3_aFcfd6-yc0dbXw1j_r2VUlVZL4DTKXyHgcBFDc5xG7HjJ5NIavdqMBZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/4958" target="_blank">📅 20:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=nSmQfJ0ow_YIbNUtPZPA2BOu2zrPKjsTmDEZmPQQhHC5A8jQ08P3SOzZMsCBMXAmOK0oEVxr7ShIAWfKjY6DodzylQpe_sIUNduh9KD_NPYnvveS_oe4AfhTvV6vOAsRVWyJeWzEflw7Haa2Skn3SCDlFbP57EIDdgphdRs_BFalEIOLdDVBr8h5lBin3i9tpA2ZcHraujn5RC9JY3bxSZU-ZBthJ9AoN8T6G_K0tDZxC2Eub0XZTNqp96ggcofVvUT0T0Jc1A-FMPnCDQa9R1CcrRIg_IDKxIjH-z1gqY11n8RG101KqFUaNu1hiJucVzmvbadHQioB_h6DrcMSZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=nSmQfJ0ow_YIbNUtPZPA2BOu2zrPKjsTmDEZmPQQhHC5A8jQ08P3SOzZMsCBMXAmOK0oEVxr7ShIAWfKjY6DodzylQpe_sIUNduh9KD_NPYnvveS_oe4AfhTvV6vOAsRVWyJeWzEflw7Haa2Skn3SCDlFbP57EIDdgphdRs_BFalEIOLdDVBr8h5lBin3i9tpA2ZcHraujn5RC9JY3bxSZU-ZBthJ9AoN8T6G_K0tDZxC2Eub0XZTNqp96ggcofVvUT0T0Jc1A-FMPnCDQa9R1CcrRIg_IDKxIjH-z1gqY11n8RG101KqFUaNu1hiJucVzmvbadHQioB_h6DrcMSZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/MatinSenPaii/4957" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4952" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/MatinSenPaii/4952" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sD6PVj-ffgYKtVH_aHdDcrR3pCuZkw77tMcal9d7FcvUcvlj0kALzQ7kTTaXPnbaPQl4PxrNCg2qNJYfF0ia3zWSU0jVkdWUbh0R97VArPt9NzzeGFJUjnJvYk4e3Bz5jW_sajsORO0YyGwVuFIOK8ACmdswjEXwvza0HcSp8GooAzkhmeWnKUbJJJpATNaN1ujMRDHOC8Uc9ORC6KtHy0cUocGMHRJuGX-7KT0MUjLp_usyXWMQE6lpgSlwqoHrvWRZE1D8zVhAJREtLQxubQP3DeOtcwGF05KsFVs26TMxhlXPX5ZpqkarLejpVT6d91YTMS_igLq0-WJcI2DPJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0
• ظاهر جدید و مدرن اپ
• بهبود اتصال بعد از قطع شدن
• حل مشکل VPN Mode & Proxy Mode
• بهبود تست اتصال. حالا میتونید کشور رو فیلتر کنید و بعد تست کنید. تست هم به دو مرحه real delay و تست سرعت  تقسیم شده.
🌎
دانلود آخرین نسخه از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/MatinSenPaii/4951" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اپ Defyx وصله
متد Aether هم وصله
کانفیگای رایگان MahsaNG هم وصله
کانفیگای مستقیم هم وصلن
پیشنهاد می‌کنم پول به فیلترشکن ندید. defyx و mahsa رو هم از گوگل پلی می‌تونید بگیرید</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/4950" target="_blank">📅 18:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EYHs5f17qynANa6oLupPnUUWqffe1iho5FlW5yCJw1-BBDq9-c0Nz_lixdek2-k0vcnGg-_Tq67N9NDLlnVCjQLBg9VwPr5mG_f_rdeHtdSkMBenXk2KJGbfLCy-Rco3JkhmFJM9JiY6QHwUrFaVUr-i4W3ZhS92hTHSXR2nKaQhm2LpHZnPxECiwu6ecsxGvHkO0h779OENxiB0hRWWHPITd7rpIRiTwm7e8ENqDFxwa8xjRpcBE18jis7VukUX5FckyH7xp7jxx6es-JrzXx0jBN-MVf5ZNhMdaMmNNctrje3KlK7a43YEMiOE-uZ0woxnnNqKEU2PVd6iNbBXfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4949" target="_blank">📅 17:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پروتکل MASQUE از Aether-GUI متصله. از اینجا می‌تونید آموزش اندروید و دسکتاپش رو ببینید:
https://youtu.be/2h6qlA1pJFw</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4948" target="_blank">📅 17:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/4947" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/4946" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">من خودم به لپ تاپم دسترسی ندارم الان. اما Sni Spoof باید جوابگو باشه قاعدتا. اما اون متد تغییر دامین رو هم الان چک کردم و بستن</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/4945" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L4Wop0iy4ZdrJ1LhtU7Gp6bImPSeL5BGosT-Cje9T-gLnTzG3C05qGvXQSCrZf7x8Wpd2XWO7WiG5_8delFYNUYnNwvmV6ahT0ydXXvK0wBiIlCmSiLQfj6qh-5agXgiUU4mHYmzSNaKvbJWSo_1OlTv23ci0xwdlnliRV2_1OMTtioCn8NUR9v2O0E5QnvvyR1ddrsHH2ZA9mduPHd9pXEbqHRnXzh14eiFblX3Lm5IB2NjMyYZQ1IZHi0dr4tGEa6i1oCooRn0J240ZxII0y5sYdBF3K1Sm55unIMd60Va0NnGQtDZMz7MC6sBKwEi6sceyDcEHh3wSGu21aOWDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SakRQ0-X-isuSTomWR1P5glohdQeGTw4ovuCZOOtzTpbYR_yU88MICCkZmzyUvTv3jtcWpCFeb_2P-4n4f7-P-cyIGamgz9eFGlIO5W0nOWoFeIrhXniVhIZsi54WCbr4mcAZ7dyINgLMzeHLsnRIf7qRl-SGwsQYp_5Gn-B2ITyYt3Q5dmOhSam9vKypugH5akHDHLb0AjyXsoUT-bAkuEkliqmOuO8Cw9APGlfEYfu3pqNkoi2sqSCku_0ReBW3r_BWA6L2Tmu2_GH7GUTUJUM2o_ytSeWjNrF24rN9wHr475B8Jj1Kqma-5OIbcd4hxnsPwK02Ywf1b-UfCg3wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد فکر کنم که ساب‌دامین‌های *.Workers.dev فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4943" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد
فکر کنم که ساب‌دامین‌های *.
Workers.dev
فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4942" target="_blank">📅 17:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-poll">
<h4>📊 کانفیگای کلودفلر شما هم قطع شده؟ (چه Worker چه Pages و هر پنلی)</h4>
<ul>
<li>✓ آره❌</li>
<li>✓ نه. وصله✅</li>
<li>✓ نداشتم. دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4941" target="_blank">📅 17:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">برای نجات یوتوب فارسی و درصد تشخیص ویورها، برنامه‌هایی داریم. و طبق تست‌های کاملی که دیشب گرفتم، خبرای خوبی دارم واستون و توی یکی دو روز آینده می‌بینید دوستای خوبم</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4939" target="_blank">📅 11:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AkmVtOk7Tg9rUgkh8QBVs4jRH3bnSKixIHpE4uIKv_PBfMUva5KKB7vrU2OLiUrA_4SafDp2e1gahKPKm1HHUoLN1sz3Bx6OsdQ0kmxXZ1dpIMNUf9IVwayLls5LE7USjtd8rmQQKliR9AcBnu8RIdFlVgxmmq4Q-MVURTa9H--ufD7C5Cba_94QVLUu_bY4-eRwU_6u-iWJdlLo9bg_fdaIERpoqKFAn_VCwEebEQZ7rZstUu0g7e8TTnoTZ9M5IzTt_jj98bY3cDffhcowv6pxbMZjsG-S4tuYx2AhXStinTJ8pU5KLUJmZuisMAFuOIppNp0dzwhvUkbN9oSDLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4938" target="_blank">📅 23:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OmcpCESxcRvUBGUbBDvCIN8dBhlpOhBCIKGstFFnqa2-Xcz-IE4WWwzWCmmrbVCgfwkcaSU3ErnLwRxdpCMgq0YAKAm5fqTrh3G_q4G0V10Un3wODN5SKoixFKBXFQFmQQLsFNh1YwUN3-jjY3kCTabIXvHaFe9VCXNDS7J_oUTznIl46m3q49mRDTTmbTPQYjittJo9V5-BNijRkJttlfahOONvw_mghCOYcDb4lnCjmEPVQXLtVaRsnJtaW526Wm8HO9v-EetcJ44VYM1hYjJVdWHODgpxZQaaO0eEcpI9DYac6jjv6yKjav1mCXa2Bx8wWsUGJMy8GsDPg3eBZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4937" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به همین راحتی.
تموم شد و رفت</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4936" target="_blank">📅 21:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4935">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SGcZ9ym3VpKDKg2DMHaO2kwBrOJTONMjejW9WfsU8xikkB8swMfED5jfbfyeRFQpvWonkQkk2iuv4ulOucJmlQW5dVtQsWatW64xBAPAZIOyOdkjm0R-wdWMVsReiGVrYMr5F3A4w9jGQYubEfZ8MUVr4FaPxNKKoJlfqwnTrjXCBHIw4_9rqVuk8_jBfqT1c9frrt7ZbcsW34OYFZuQUikiPtWwmX7iU9JvUywQFcOgRE55TZugNc23ai6NVBV5aSfxJF1HVqQEKcij0ZOtXVNVjNVTl4BPFb3-utcYrZT1eszK0BSlOyxc2dtEQh52TJzajJgUDKiw__o2NdFkyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط عادی :
•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
شرایط قطعی اینترنت :
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین نسخه CoreForge برای آیفون
@whitedns</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4935" target="_blank">📅 21:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4934">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OXES-otr4ypbeLJ1Y_Di5qMLbQgJUM5FpZTE6CinIzZxidtbdeiOHZDy4e9f5Dgp5BVftGIP1ubetYDhz6D3x1H0TbjyGmbKnMd0Fs23tzdPr6oh-e9o1omY8mmc69L6qOgT5Utws5RyGtr7RElzzTtaQR_FYzJXUjMx7bpqAB64yqOc2LPlA0pxS36WeVA8iovUkYAg3THFjua9pINJAFupndC7ZpvmsKpMdJk4aU5JdtuUOsaeGP2gybqGCuphUZAmrXDFB0b-_q6Qun95_gCkqfUxNS9ppnIsS9VPCCPm_Yb4JMHrMjKE-YJlO_cAL74BZ4i6xuc65KIoS0ETxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4934" target="_blank">📅 21:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jr6-MOF6w5P3hHijgzKmDnj3bYFuKW5ebwHbd99yNpZ8MmANCVexETOFjXoIkPGZyv39g-TpU9b4_Z1jkQ3onDiJhHpc_dRznVf2l_5Qz8aLnJHOCAUkiqsxwVx9D9G3QMDtUaIECngamgCI05ANYsOtqVqJYRqlXjpV1cGNCpLGLEnwndevm5tErpaKeGj54BUm2RkMz6iiXSj7Bi2_MsjYNIYW6Vs9sf8tjeACVX47Qy0aU2cT7m6SbMsopn3VLr72h5vKJGeqml3pjP5aX2L_7YwtE-66zFksdDt_pH-yq6vu_lPo_Czob4-cwYYKlUMfbkJQxmli9lw-3HE1vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4933" target="_blank">📅 20:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4932">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZCs30Ezlqq_KfihLaFJFv6z3AoNowMTLcfpRBQA8sA6QMEBjrwLvwgx0-QUYh8YgFX-DP0QVaG6XDKFlJwNaDJSBdpKqWu1QnjDCDP7djMNQNJtgqJYN9AgjqaXH754BdW6vzX2jZU1m9FAq3mrp4JsPnDf81m8K8-73betFU7PKCdNn6dJQ1Kwehp4OFih1UZeTQfnrVXJgVNl0s0n5vFafRhXitTI6oNFwbKJLIEKwwu-yzq0pdETNhLgTDM8xEUo_YKe2AlJgrl9eEMPors8rx0gEWP_dCmlZUjoXwGRUHGP5EPl4NjcnldTqwl5SzDYPli5329jWwsjhFb3acg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله
محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود.
باحالترین قابلیتش اینه که میشه Mode شخصی ساخت.
و از معایبش هم که بگم، درسته UI سبکه اما کاربر عادی ممکنه یه کم گیج بشه
و همینطور فعلا توی فاز تست هستش
و ساب ایجنت‌هاش هم مشکل دارن
پیشنهاد می‌کنم ستاپ فعلیتون رو ول نکنید بچسبید بهش، صرفا در حد تست
مدل سفارشی هم که می‌تونید اد کنید طبیعتا. من الان OpenCode Go اضافه کردم</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4932" target="_blank">📅 20:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fx9C6IkRHf7Nb2MYu1DAwbWn6RvzCD7iRLT7tvl2lhUVmTzan1YDShZSjpJzpYJ2TaSlcjYVl7Ar5z7_k4WNMSmMWtBrUAUg4vmZcIFYAFS354Bt02zD3Nuw59ISE_vkyf4hFlvEEpodiUxR33kgqVtMcx783J3Hrfh4kpwW-tpsxUvFJU54j6-JG7UhukVB4yDdXM2FbG-x1Llan26KSU2bhCjrLT-8IRLADTHS3_AkvafpfOIgQyK6KmsmC0yumkLh359fpvnkS9wr9FGFCAllNuKs7p85iBlEpmXG8Spi8K9LiccL9ZQxs46CelgrFxpkIuEkeUG_7nGBdzOZ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود
😂
😭
اینو چرا پوش کردین مسلمونا</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4931" target="_blank">📅 18:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔺
ابزار کدنویسی متن‌باز DeepSeek Harness برای رقابت با Claude Code معرفی شد</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4930" target="_blank">📅 18:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4929">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMJQ2pvtyIF2mPbQkg4c3NrJrhDMS1INbp8XK3ljcJth5L_nZNPjLHF-nfGC6spCBvRxCkTZjYC-Uthq3BYtQADMwn4xRlHan7b3lx48kNiV1lcYGNzgsnvjomwQabHNd34eCs1YeAJAumjXPST6njpuu4kFFXaPBZaTvwYIGqyYQmtTt0dDpzi25CtnFiyOrZizkXOCSKadnE35ZuwXCXqZmEdcAnu1UFXVpg_w2jhZIH0ig1EH8HWyNOUJptFcLhrDSYcCsmGhWbMCSNqSf-v_bR5lRvr8JUWcDoSfNp4_DOTqqfrqhuaBn5OvKpRi0ALxgEO9hork6I60X8dsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه قابلیت خفن برای هرمس ایجنت معرفی شده به اسم Bot Mode
به جای اینکه هر بار سشن جدید باز کنی، می‌تونی چند تا بات جداگانه بسازی.
هر بات پروفایل، عکس، توضیح و کار مخصوص خودش رو داره و حتی می‌تونه با بقیه بات‌هات حرف بزنه و همکاری کنه.
https://github.com/NousResearch/Hermes-Bot-Mode
@RepoFA</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4929" target="_blank">📅 18:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جالبه که من دقیقا سر Kimi3 هم همین مشکل رو داشتم توی کلاد کد.
الان توی OpenCode + DeepSeek V4 pro این مشکل رو دارم
سر دیپ سیک فلش هم داشتمش اینو توی کلاد کد</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4928" target="_blank">📅 12:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LhjaYcd-1Coa7-CEyTlLWov0RjeYVvSdbN2csSS1qAGV6m_SL9VXvsct05ddxRAaIUcfdAccpE9VUlD8-E4_2C5-b91ydf9B3e9q2ZgY39SDiwE74fM-pOwbxve1cfm-dMwLsSEdDbCm9E6yETqufhthKmuefQuzJ3WG5aRTJkluh7wTMMyyESR8JahIhJrWNRsXO0JhDWT5iwHhib9-KXZc4oqk9f5KwoDoSrNWVZamuXo8arKb8LF6aTx2soUJA0ZJE0LUi8SyF9xoqpIcomNJk3-VaU-fc08ohiJlP7mzfEhXM5E6CJrty3xsFF81vOGCVxRIpkA2qiWhqRKy6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا عوض کردن VPN فقط باعث میشه که از اول شروع کنه به Think و من اشتباه می‌کردم</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4927" target="_blank">📅 12:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4924" target="_blank">📅 12:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4923">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C5c0HLOciFCVVC3a79NhaqVXrIfo2Cn_XFvedCz-60d1UlRBfZuwLXcl_QBzSQRzkFkSmdpTmMYWPAzq6n2p0ytP57Rtfa9wLAd67AdVy-kIfgkf5eiSWtUT6a0zJEUP0z85r5zAe97TWK16XX9lW0YnGgUlFWFcezfwDhab-4y2qgQ1lB7gMnfCgBUy1benOliya_8nVlO1EPF3NmRdgdQNoqC-j39s0VUt9oe1FI56xxJheiuITqgvl2Bli1CmWMuHFwHrrf91yyqMemsMse7E9v7SQHnwScmW5xlpHr5bhk6QX89EnlFtiyX9jE5VhX_bnIvfJHlu1kHDfXWVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو
تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4923" target="_blank">📅 10:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Iea-XwW9xe5NG4rf6xq01hVoZ7MSdP6IphsAhyRXcIgk5eRNPU7zObCsw-oBZRiximbnrb1MoWlkuPkhVzqFHxK0gSrkpSrGeKc8jTm0sXfoVHAfDKKEzJlL-B69BAYnUiQwIt8sAaMO1WcSXy0hY-8wt059bqeQ9sqAA02GVbI4-4Mbmot5yKWtHnr_fKxsgr8vHMQOxNngKw1ffCJzmTXSXeCn3FXdfbHh1A7kiDaSBSb-XD1se-G_pdn8eSs82I63XOsIbBFkUUFooSHymFZLGiRab4UMFksi-w4s1GBTRw3ZoB_yb2nZRCRegF3cnpetZYW8C_7tIUBwtwH0zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم از پلن فری هرمس که گرفتم</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4922" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SFabza7jgRIvvinb2pDi9xw4dPIN88KqqVuLoc2VZViAMvu3rjzMl5uZ1A8eDA7nIcWPa2tI_cl2o9Xw53R-hocaulpb7gDMXZAO6-Gu9t4qGnm31PgBB_FWkCAaeSgMvkEkWk-1xo6HzMI1lVRiqlFnlykxVI5Wo4ftwuvoLRu-yJNiEP9pbA9brqNUrNvfDZqTwjZ3kkGD8BCag8cIW_TcoKnovpbxqMl27uY5rEAmnCTPwwqmqFWdGfHhZd16kZovcRFW1zeREy0Cd48NVSKaf5qWrY1n1Z2gaKRZaRiAVVageMuAGVmCcRsjcR6hBUAW49Vv0d_s0xhhxvmlgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4921" target="_blank">📅 20:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اگر روی 9Router+Antigravity به ارور 403 می‌خورید، یه بار اکانت رو حذف و دوباره اد کنید درست میشه</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4920" target="_blank">📅 20:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4919" target="_blank">📅 20:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jrJFyiP6LLSln_ky10Fs7SgGSFGmEJy7vaMGz3faco4IDpI-jqMstBEMne1QnS6a_i-EqW_PRI3i0E4dCSUfm0oN23PEkdKUAMMVOwZkJlyGgGsGd81QDsrPeuKEFVrh3-cbh9cJ2Gu8_-LUmENgfEaFpefA_4LWge5aiYoKi4BkxMC8nJYGu_srIABLqlA_oS3_07qqey_XfnD8Pe4RY2016B3VPyL6Wdwd2EcXeL_-DJ0qEKsrKNp4Fq0XFVNZl5teOSL4_Icdf6T64OgwEciwiPaOlTV-ydJCdV1uAoeIhDgoTCuPZCCFGLz8WfsAwxUZfcPeol782gwEXCtC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4918" target="_blank">📅 19:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VxcwqI2Jv24nZpucLsESGWjc3c7utfutNexcUwFevSWjZdDIl-TlJNleoTXhhRjgd4EzIBEYQRIbIl1vQRyXLd04tQk_rloPKn0xv5fNHXrHYqbCC7c8CbuhD0Oh_QuGm_Ktn8aX-XKg1_kgZiWOJFm4FAE_XWpQOWP9k_2EynShqSqETKo9vDESIzwk1v7cgdFWPmhe83Y51T4mGaTqqzIsUJq13aF9ewIkhzVs2kW25NPoriaXamyeUF88gyBSKTo6nZVzDQK2U_Edx56jp4WKhOs6WoPtDjGlE-LWdyrTJGP5CnB21YqN_I6WStpj4JRUL33YW5JQoB-i8vWrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oS1zTownpUtRFl-GCkgPS_2xOajIveMOgX8s0bqq7UQrhoZr2dOi4_Dp4NkMJc4NHv-21X4Ml4C_K65fxnu3slFDPLb2p77mSUyrn-7_y0Z6kP3kIMZPt2whLbL-qRr5s7Wd77rGSm6IbHE5Vme-V2eX4pEFAUbg9MGBts24X4rvH-JBWtipKDja-4jC8VrTtAkHV5ZUgun4j7SmDlPi_bCjjPg5u_b1JFsMb3tZYuDMgDwjqMy6AOVoa4EkBepoiq-f6Dx6ZnUqvjtR_ORK749UZmPEwrq78R3oHH_kL40QcWu94fTjq-o_P3Fz4sbUBWeSgSTQWQrnlndDvlS-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xhk4QE3XeBCLIY9cyAH7RyOlxAtINwzOvIqCIik78YBaxDtSIUaHZmkWWjutBYalzfq73XrHgFl474jkdVpzadjvBSYwpX1jax666bid6eDrFiDXczQ3awyg6pKxA7nJyZVk5fSygPVWR0gVuwmnzbmPxzNGISf9qYN5YghkjM1u4Cv7vSi9nI1ZmlTL_QDzy_cni1KcSZjngEvXgjbWdElj9Xk9HRT3sFh3_2PbNcTHQOn1ufdcm7WAZw6T0X3hyZhebWL5QX0lFh9WRWJa_hKtDVtATyvNfxTcJmxgFILrpHWr9m4a3pwYqfhJvBt1DzUb4dhUkxuKnuntIV3FYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی
خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید:
https://app.mpay.cards?startapp=ref_PzwXZ8
(لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید)
1- بعد از اینکه وارد وبسایت شدید، Next بزنید تا با تصویر  اول رو به رو بشید
2- روی Apply بزنید
3- با ایمیلتون لاگین کنید. دقت کنید که تمام هویت کارت‌های اعتباری شما روی این ایمیل هستش
4- بعد از اینکه وارد شدید، با کریپتو 5 دلار پرداخت می‌کنید و کارت برای شما فعال میشه. از USDC و تتر و... هم پشتیبانی می‌کنه. برای آموزش پرداختش با نوبیتکس و...، می‌تونید یوتوب رو بگردید. من خودم با Trust Wallet زدم USDC و مشکلی نبود.
5- تبریک می‌گم، شما Visa card دارید به اسم خودتون!
مزایا:
- می‌تونید توی تمام سایت‌هایی که نیاز به کارت دارن و رایگان، اعتبار خوبی میدن، ثبت نام کنید(من توی Nous Research پلن free رو فعال کردم)
- می‌تونید برای OpenCode و سرویس‌های بین‌المللی، با شارژ کردنش پرداخت داشته باشید(کلاد رو هنوز امتحان نکردم)
- و تمام چیزهایی که سالها از ما گرفته شده و ازش محروم بودیم.
- ایرانیکارت و سایت‌های مشابه، با مبلغ‌های فضایی و میلیونی فعال می‌کنن همین رو. و به نظرم 5 دلار، منصفانه‌ست
معایب:
- برای واریز به حساب، باید اول 25 دلار شارژ کنید اکانت رو و بعدش می‌تونید به کارت منتقل کنید. تنها محدودیتی که بهش خوردم همین بود
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4915" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zfyj4MLPytKZ9YUbWjmZ_B1mhCmr5PuGmRsRt1yP4N3a2g7xTDPkeduZcfRf1dJBarPsavwNalZ5LmmxzZfiUa3GF65EmLDMRQawnt4VLtUmClXX7-nrR5dHdXKTqRjrFLuP7oUsWfqbN82M41jD7f0dPZ-kLuUeRma_hddPg_t66OfIzwM84o-hGCXrZegcxC8xVR4OQMc2WgYhXPfLkfdUTxm3ZlQ5qMDuv-pDiynRfRqEar7xwVP9qDsVg3q3sqrN4-lpkAktHPF3FfV3rKlGaxkRstiM5BEdlFlxbJa3gu5wpHvZhOIUywj6OFg1vy-2zZ2coMHV09b1_IqNMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.  از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4914" target="_blank">📅 19:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">همینطور روش رفع تحریم آنتی گرویتی هم چون یه کار کرک ماننده، باید همینجا آموزش بدم و اصلا نمیشه یوتوب گذاشت:) چنل سر دو دقیقه استرایک میگیره</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4913" target="_blank">📅 19:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.
از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم به صورت متنی</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4912" target="_blank">📅 19:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">این دسته‌بندی جدید کاناله، با ادیتور جدید عزیزمون محمد.
پلی‌لیستِ "قصه‌های مدرن"
قراره چیزای باحالی با همدیگه بخونیم و یاد بگیریم
🤝</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4911" target="_blank">📅 18:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O-8sNtF0uxgCHU5Eu4QfRL1lxZD5MEzwH5hWJXt26idPu0NrNtWOL-fZzkc3ZThxtbeHjTIdcAScmlrEwVa0bSpMenSgKvj0gRhX0m-MgJ3gNB-PZCzZmkr_qIzM9KeEp3OGAQOvNhglbbW358H1ROn87AxAWOUJzRS8HSQxaNRW86yRzWSaXN_InUcH4iYfGvWpiD0DY_SK8gHjjWa48Cqu4FzSVKGHZV2yC2JgJRdt6mK1OC4j3ACNy4YraBtwRmfS1xEexA1J3ushdQzsimOK-0cskb9gxT8Vq1ZLOJKK2vWe0ClEyw3Gta3EcXpV2s-cbNr_xCludPrqWPYKTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
قصه بارکد، خطوط سیاه و سفیدی که دنیا رو عوض کردن
هر بار که کانفیگ V2ray اسکن می‌کنید یا یه چیزی می‌خرید، دارید یکی از هوشمندانه‌ترین اختراعات قرن بیستم رو استفاده می‌کنید. اما داستان اختراع بارکد اصلاً شبیه چیزی نیست که فکرش رو می‌کنید؛ نه آزمایشگاهی، نه تیم مهندسی‌ای، فقط یه دانشجوی بی‌قرار و چندتا خط روی شن‌های ساحل!
توی این ویدئو با هم می‌ریم سراغ:
➖
اینکه بارکد اولش دایره‌ای بود
😂
و اینکه چرا تا دهه ۷۰ روی زمین موند؟
➖
لحظه‌ی اسکن شدن اولین بارکد دنیا روی یه بسته آدامس
➖
بارکد دقیقاً چطور اطلاعات رو مخفی می‌کنه
➖
چرا و چطور QR کد به‌عنوان نسخه‌ی پیشرفته‌تر بارکد متولد شد
📹
تماشا در یوتوب:
https://youtu.be/PAHA55mHLWs</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4910" target="_blank">📅 18:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">و اینکه مدل رایگان Hy3 خیلی از Nemotron3 ultra قوی‌تره. از اون استفاده کنید</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4909" target="_blank">📅 14:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HznEZGPzd5_elNXFW1HU7YlvN6AXVir7IEfSXanGEYIFrLCyEK-HbXd7bENzsiOQzHuq3ltYOc_XUvzzgjnC7BLKGPhReu_Euu51rm07fKf-pgXThiKwTKFa3XFBot6EQFSNBUJoHfChbwdze__g1YHJUX_qmxrLuOJg7c3Qsa10vEPe6OnNDgCrW0MoF9urlhRAKKcjmQpX2Egr8vwUWpSSb43IeRm_uVM5NPKNXXxvARljzT63VhIUIFDju-LR9j5CEUOEr2jJ3AVCCCx3ojabBIJIA0WUJaUVfeEii-G7d3ThZBZvsCAzcKVNNeZqkD5OCgPWjA5LB_gowiiclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا به آیپی‌های کلودفلر حساس شده کانفیگ‌های کلودفلر رو با آیپی‌های دیگه chain proxy کنید باید درست بشه</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4908" target="_blank">📅 14:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده و فقط روی خود OpenCode در دسترسه واسه‌ی خودم احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4907" target="_blank">📅 13:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده
و فقط روی خود OpenCode در دسترسه واسه‌ی خودم
احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4906" target="_blank">📅 23:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حالا که شماره مجازی و کارت گرفتیم، هرچی سایت api رایگان میده باید شماره چینی تایید کنی و پیامک بیاد برات
😑</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4905" target="_blank">📅 22:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4904" target="_blank">📅 20:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b6ukjXkRC6jRRNbGa7p9kKqbYr8BqM0vnG_dda28VeFCSBaLDhpaS84nX2ztmlRp_cqRpHUMdd5zEnFt9O1qPJxzr-rx0LcSUsWjSvpvuZFJx4XCinxtSdKN_ndowb9uIMx5KsYe8VsGB4Z7-FKMfCq-d6KdVqgiiKIg1hesd3USgP6_KYRqFkziWNeLC4peNpMUjFEXoOlol9GM26WvDrqB4agIcjKLYJBapOPww3R4vZI_yNcdZd3iiUj8Z9vV1Wi6EiM45os7aByJHFz_tIA7H1rTa2hCi9apS0JHcl0og2oga2s8vgyLeRjb-2VHGEbLDWrlzvwFETLn55F8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4903" target="_blank">📅 20:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یه مقاله از 404media نشون میده یه شرکت پزشکی که ادعا می‌کرد تحقیقات و peer review‌شون 100% توسط انسان نوشته شده و ابدا AI نیست، در واقع کلا از AI استفاده کرده. طنز تلخ روزگار ما
😂
https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai/</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/4902" target="_blank">📅 15:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aoXspSau3Y2dycgfsc3-LHklp1xqNC5-aHrYL2ntelq-zCYauUXLfZTKp_jAZ9S2UOqoKk49bi7yKaf8X9ghRoYb-UhvD2esByul51Wwu2e_Mli3Q6GRz1IpWSv-63CUf2W6qrIqnl_mqViEhpzXAEKKOeOSpok433-jdgE2GZQzYkN2FURRu8ge18mCRahBS7L1QYYDOXWQjTZoua5IhYbF6gpB1ovTvvPEFjFHMcRmqDpg7O1nzpPCzJRS0YVtiWHfF20R079VStftDtHmgqdMesQmYScZStSfiP3albTKfVRXoAuH71R2Y-uRb2Odd6oV93l6h7yzP5PXG6ntfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اینا تروله دیگه ایشالا؟</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/4901" target="_blank">📅 00:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گویا ChatGPT قراره تبلیغات داشته باشه داخلش
😂
تا بتونه دسترسی رایگان همه رو حفظ کنه:
https://openai.com/index/testing-ads-in-chatgpt
اتفاقا به نظرم خبر خوبیه. کمپانیا می‌خوان ضرردهیشونو جبران کنن و طبیعتا بهتر از گرون شدن اشتراک یا محدود شدن دسترسیه
اتفاقا با این روش، شاید بتونن مانوردهی بیشتری روی دسترسی رایگان به مدل‌های جدید داشته باشن(مثل رایگان شدن GPT Luna)</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/4900" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">از این به بعد، همراه هر شمع لیرا یک تگ بذر هم براتون می‌فرستیم؛ تگی که با کمی رسیدگی می‌تونه به یک گیاه زنده تبدیل بشه
💚</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/4899" target="_blank">📅 17:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOJP1cyoi5UNbppuRVkohUCP89vHsDwNJ6RkmzBBNUU8vbvQz3ZBCt_GuB1_q3CtJSu0KUmEne966-Z-N4hTga0brwwsK6zAT-kdxO1eHxDsHw6uHF4DJanAiqfaOCHfxx03NcfH2h67oaeFVmil4I9NV8o2nDrhsoCltSDHJwl67XJw83_adiEDFVCH3uC7CQ3QPHG5mpfkhoqki7BFhgmu3TanxlDj91W3uMfrb3cPUYrzuD-bgKeWZfhh7FMtF7JWzgEV1gK1cWlogGHwU2t4w3M7-G0aL95xwavt5IuYhlmafkNM1URohOLeP2iv_pESBt0t1n6mirFwfaJ7EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون حرکتی که برای کلاد زده بودم رو برای آنتی‌گرویتی گوگل هم زدم
از لینک زیر می‌تونید استفاده کنید ازش
[راست چین شده و استفاده از فونت وزیرمتن به یاد صابر راستی کردار
🕊️
🤍
]
https://m4tinbeigi-official.github.io/Antigravity-RTL/</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/4898" target="_blank">📅 13:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4897">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/4897" target="_blank">📅 01:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا
جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/4896" target="_blank">📅 01:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4895" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">Building_Applications_with_AI_Agents_Designing_and_Michael_Albada.pdf</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4894" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شاید بپرسید پس چه کاری؟
حالا برنامه‌نویسی آره یا نه؟
باید بگم که نمی‌دونم حقیقتا. تخصصش رو ندارم واقعا که بتونم تحلیل کنم
و به نظرم باید ببینیم AI به کجا میرسه
اما یادگیری رو متوقف نکنید حداقل. به قول جادی، یه چیزی یاد بگیرید(هرچند جادی میگه ai، استخدام برنامه‌نویس‌های تازه کار رو replace نمیکنه که به شدت مخالفم در حال حاضر. به نظرم تا حد زیادی نیروی برنامه‌نویسی کم شده و فقط متخصص‌ها یا کسایی که واقعا علاقه دارن یا ایده‌های طلایی داشتن باقی موندن. حیطه‌ی برنامه‌نویسی هم مهمه)
اما خب حواستون به حرف‌های غیرمنطقی و امیدهای واهی هم باشه.
و سعی کنید خودتون تصمیم بگیرید. و توصیه می‌کنم حتما علاوه بر مهارت‌های نرم‌افزاری و پشت سیستمی، یکی دوتا مهارت فیزیکی بیرون از خونه هم یاد بگیرید
❤️
نه تنها وضعیت دنیا معلوم نیست، بلکه وضعیت ایران صد پله بدتر معلوم نیست</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4892" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DTyje6uqJYI_-BYqEY4AJYHWMIiMYQm9ONw6IzjC8LOAKrMk04XOBQJ800NGUTabZAbYyvTvIP2kd0gEAJe-q9QvWEZiE0mxDq1sI161gj6hTnoEbfCSok4EBRg-c8ov5Gc6vBbMMa2pbTPeWxokYhpIsuP8NWaECABLhnh529d5sjpwBo_37oDMATRGvjKaltMYHGjJsPtYOhU6mq0xDH1QVo5pWamHBoWbjzjPtINoHNOThlWnxq-S6oItjT8r9THyjSeDHqTaGwbPguz017H2wyJmFj7NDfyl-1vutGTnu2-zJWk__4OfKCSSPR2B_g7K_kb_0GcgzAuy0Sjxlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">21 سال تجربه توی گرافیک دیزاین، UI/UX و Product Design دارم، الان هم که چند سالیه با AI سر و کله می‌زنم.
از زیر پله تا شرکت‌های اروپایی و امریکایی رزومه دارم.
سن‌ام هم دور از این 35 نیست.
بدترین زمان برای ورود به UI/UX عه، قبل AI شانس زیادی نداشتید، الان که اصلا شانسی ندارید!
✍️
Diego JR</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4891" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IVZsFdsPxfO1Iv1ySAogCEN1aQsrPoBZGmkjpgBnOOw4OocT9aWqT3BsN4oispfgM8cBbeIFa5Dh3r4b6v1I_5-fFd-5MWgov0FSLlPeBKHSI1lJH653tcHKMjl4Yjs7gdTGhElwcR_DLe5MoDKJPsXpVZEIDEfMBker8w_i1LKqDGg_uncx6aEqVxbnfI81w8y9f7NhjfI10d8Mu-OX48BjnlPVZS6Co13BNrp2crY18bzGc5sGqa_yEiWEDEUqvSfpP0up7ETU1P_wFZFQdP21iG0jmwfasp5cM34s76DByA0hTMXmhCT0yIPvuMYrd2y7zGhkx1n4jesCu16YKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نشستم با Hermes و WinDirStats سیستم رو یه کم پاکسازی کردم</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4890" target="_blank">📅 20:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کاملا موافقم و به نظرم هیچکسی "عقب" نیست
با کلا یکی دو هفته می‌تونید به ایجنت‌های جدید و api هایی که هست و... مسلط بشید اصلا نیاز به تلاش خاصی نداره</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4889" target="_blank">📅 17:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">به نظر من کسایی که هنوز نرفتن سمت هوش مصنوعی آنچنان ضرری نکردن، چون الان استاندارد خاصی نداریم هر شرکتی چهار تا Agent برای خودش راه انداخته و داره باهاش پروژه هاشو جلو می‌بره ابزار های هوش مصنوعی یه دو سه سال دیگه پخته می‌شن و شرکتا یه همگرایی به سمت یه استانداردی می‌کنن اون موقع دیگه یادگیری هوش مصنوعی اجباری می‌شه، ولی اگه هنوزم کسی نرفته باشه سمتش با یکی دو هفته شایدم کمتر بتونه تمام ابزار های ترند (نه استاندارد چون چیزی هنوز استاندارد نشده) رو یاد بگیره
عجیبی ماجرا اینجاست یهویی یه ابزاری چیزی میاد توی یه ماه 50 هزار تا ستاره گیتهاب می‌گیره بعدش فراموش می‌شه و یه چیز جدید تر می‌اد!
@Linuxor</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4888" target="_blank">📅 17:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نمی‌دونم واقعا یه سریا، کی می‌خوان بزرگ بشن
کی می‌خوان به بلوغ برسن</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4887" target="_blank">📅 16:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4886">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">«الو بابا این پسره منو اذیت کرد بگو سایتشو بزنن فیلتر کنن.»
خیلی سایتای فیلم و سریال و انیمه و... همینه وضعیتشون.
تازه من دورادور در ارتباط بودم در جریان یه بخش کوچیکیش هستم فقط</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4886" target="_blank">📅 16:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4885">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">با ابلاغ مصوبه جدید هیئت دولت، مسدودسازی و اعمال محدودیت برای پلتفرم‌های آنلاین از سوی دستگاه‌های اجرایی ممنوع شد. از این پس، تعلیق فعالیت سکوهای مجازی تنها با تأیید رئیس‌جمهور امکان‌پذیر است و مسئولانی که خارج از این چارچوب عمل کنند، ملزم به جبران خسارت‌های مالی وارده خواهند بود.</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4885" target="_blank">📅 16:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LFAzFCWxzvrE9OZ6-s31WvBrhSHIKK7W6iEsKvHPZAE_aQinobxKMbCKY6dYPzxcSD3t-O14hJQejEQtAbA23agK5I4NHdv7fu5itUKRdWyGS_eTdQFB66y6A65hGQzN0_aQw4wzjDuwqN0WIcgY1zBaM4FRuzZZJsr2VCFwuCKFCfu7-p-T71cpeA3NPraDTfoeqvk1OAcO-OtTjxwxQ46ovMxVuv4Mvw0xE7_eR3kwPWRIsfY-YXStvwyhWToTlUpHhDFpnp7AKi7N4bIQY_ZyMzL1nCaU-lihDLiijUTK19gQpb61a5pPrC2YSOez-5YLwiiuLl_8Pyn8RsE5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Free Movie هم بامزست. دو نفر می‌تونن با همدیگه، رایگان فیلم و سریال ببینن
https://freemovieir.github.io
هر فیلم و سریالی بخواید، لینک مستقیم دانلودش رو می‌زنید اینجا  و Room میسازید و می‌بینید.
در واقع استریم نمیشه. Time Code کنترل میشه و چیز باحالیه</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4884" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4883" target="_blank">📅 15:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=ftkCX6TpsnABdic8vd-0zTd8zJlS9r99TxWcs1ev9yxKA9kLmOwZcHsoBOsXFA03xrlTr1nmqb_GMkW4e1pu3YFLTsxoBuUjZzf0x6hd3lw7hcka9YAbTJBYxdV0zU4NzqJsT5PuoYxCf-J1NTbXYRtGPGzPrLBiNC5KFQv2YMljB_VlY63G0Gw7ExZUC-zhqKQkgXNvuNbmL7nMuYcMsZjj6opgSHoo0ipbwIEz7s3cpcHsrEh7elImGYg71TxHtBoMFXN74Jd3nvAqpGzpNiwFNZnrugfqHkZIZUD31roYrvbvi8MhhMnl361LeMF_l5HppwLCZTgLfU0DfEHQmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=ftkCX6TpsnABdic8vd-0zTd8zJlS9r99TxWcs1ev9yxKA9kLmOwZcHsoBOsXFA03xrlTr1nmqb_GMkW4e1pu3YFLTsxoBuUjZzf0x6hd3lw7hcka9YAbTJBYxdV0zU4NzqJsT5PuoYxCf-J1NTbXYRtGPGzPrLBiNC5KFQv2YMljB_VlY63G0Gw7ExZUC-zhqKQkgXNvuNbmL7nMuYcMsZjj6opgSHoo0ipbwIEz7s3cpcHsrEh7elImGYg71TxHtBoMFXN74Jd3nvAqpGzpNiwFNZnrugfqHkZIZUD31roYrvbvi8MhhMnl361LeMF_l5HppwLCZTgLfU0DfEHQmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی
این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب
https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/4882" target="_blank">📅 14:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست قابلیت های هر پیام رسانی رو داره:  - چت های شخصی و ایجاد گروه ها - تنظیمات پیشرفته پنل کاربری - پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ  نصبش ساده ست و با یک کامند انجام…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4881" target="_blank">📅 13:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromZethRise</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EZohOdv-0hhYFCuBRMgb1o_ef4KOJaSBtDPXZ3dKkqPM-XpAjZ7Cft9dBq7u961zCF1dtnQnF0yGHSWcclZj5kAEtRt07705unxo7S_qKNJEYmXB-GeoISUSwiwdS8TTPN_pufYmjr8DcQn7PxTwtt5n25bD70EU4xLz2rMzMLlWak-CMCrB2Oiny8mVY7shzQ2NmEg1s8wn_yCmIUqVFVtlDljgak73wv9OyRNnkkLsghL2vZmMJjkGgsTxFSXT7Ouaa4RDMoIgIZsH0b-Z8MQrVvi9JLRvv_3OZywSGA10MaUWuV5hUZzv7AozO8ziMvqY4FfM-78WCK1jP8P3vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست
قابلیت های هر پیام رسانی رو داره:
- چت های شخصی و ایجاد گروه ها
- تنظیمات پیشرفته پنل کاربری
- پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ
نصبش ساده ست و با یک کامند انجام میشه:
curl -sL https://git.diastom.xyz/ZethRise/FelFelChat/-/raw/master/install.sh | bash
و سپس با کامند
felfel
در ترمینال سرور میتونید اون رو مدیریت کنید!
درحال حاضر فلفل چت ممکنه مشکلاتی در UI داشته باشه و همچنین در backend چون نسخه اولشه (v1.0) پس اگر به مشکلی برخوردید توی ریپازیتوری issue باز کنید!
👩‍💻
Git Self-Hosted Repo
📱
X Profile
🚀
Developed By
Zeth</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4880" target="_blank">📅 13:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دو تا از دوستای خوبم امروز همراهم اومدن و اذیتشون کردم و کلی تجهیزات گرفتیم
🥰
🥰
به زودی خبرهای خوبی در راهه</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4879" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4878" target="_blank">📅 08:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4877" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
امروز اومدیم با یک
#آموزش
کوتاه از کلاینت/اپلیکیشن incy
🔥
داخل ویدیو به چه چیز هایی اشاره شده؟
. ایمپورت کردن کانفیگ ها
. وصل شدن اتوماتیک
. تغییر dns داخل اپلیکیشن
. تنظیمات مربوط به تست پینگ(مشکل پینگ فیک کانفیگ ها رو رفع میکنه)
. وصل شدن به پروکسی لوکال(باگ کانکتینگ تلگرام رفع میشه با این روش)
🔛
خلاصه:در قسمت dns از quad9 مقدار گفته شده استفاده کنید،تایم اوت کانفیگ رو بالای ۶ ثانیه بزارید در صورت باگ تلگرام از قسمت پروکسی استفاده کنید.
دانلود اپلیکیشن اندروید
دانلود اپلیکیشن ios
دانلود اپلیکیشن ویندوز
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4876" target="_blank">📅 19:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fAyECfwiVdqglNcaqpDNgkTeZsaXS6_gskdWIOsjgeccvnYW4O-SM_NA8Kxa7X2zQOygwVo8hYKDIxavCvzPvueQW-37TPgg6fH8i5cgPXBzI7URhdiOflgCjaF4NHL-diF4EnZigdUCFQM5VFAb-JP9D8awa7rq2NeXdH5Hs3p4FrkHDFVgV0hggIGe-KG18D6F3CSFtlfuXxbbhGUZryce6RQMJsi_gsgDbuhIkAoxJmEk4uNxLGDwuJcTg6VWtz-WQ3UE9JmwU_hjcTbuFeEjf488CQwzF3EvjVSkYql7JQtIgbevZprS0Tt7VgucoEU4nOvfw3p3gnyhs5Pjag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مغز دوم و هوشمند برای ایجنت‌های هوش مصنوعی؛ پروژه‌ی متن‌باز Synapse
🧠
حتماً دیدید هوش مصنوعی‌ها بعد از یه مدت حرفاتون رو فراموش می‌کنن یا اطلاعات قدیمی و جدید رو با هم قاطی می‌کنن. پروژه متن‌باز سیناپس، مثل یه سیستم‌عامل حافظه‌ی طولانی‌مدت عمل می‌کنه که روی دیتابیس محلی SQLite سیستم خودتون بالا میاد. این ابزار فکت‌های مکالمات شما رو استخراج می‌کنه و فکت‌های متغیر (مثل شغل یا محل زندگی) رو به شناسه‌های مشخص وصل می‌کنه تا با تغییر اون‌ها، مقادیر جدید بدون قاطی کردن جایگزین قبلی‌ها بشن. سیناپس اطلاعات قدیمی رو کمرنگ می‌کنه، تداخل‌ها رو رفع می‌کنه و به صورت خودکار مانع ذخیره پسوردها و توکن‌ها می‌شه
👍
این پروژه به صورت سرور MCP ارائه شده؛ یعنی می‌تونید اون رو مستقیم به ابزارهایی مثل Claude Code، ادیتور Zed یا Cursor وصل کنید تا یه حافظه واقعی و تحت کنترل خودتون داشته باشید. سیستم بازیابی حافظه‌ی ساینپس ترکیبی از سرچ معنایی، متنی و فاکتورهای زمانیه که همراه با هر حافظه، یه شاخص میزان اعتماد (Trust Qualifier) هم به ایجنت می‌ده تا بدونه اون فکت چقدر معتبره.
که به نظرم یکی از مهمترین قابلیت‌هاش هست.
با سیناپس، ایجنت هوش مصنوعی شما به مرور زمان با بازخوردهاتون هوشمندتر می‌شه و تمام داده‌ها هم کاملاً آفلاین دست خودتون باقی می‌مونه
✌️
🔗
لینک ریپوزیتوری پروژه:
https://github.com/Danialsamadi/synapse
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4875" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MjKfOBxItnGCpiGB1EOUxWInaaEUcC5mg9w2e1OlM_lw34-51dq-pOmXKqdJ7R65v2mryQxRLZm8hCDjOoQ2rNEKFCoyPOY_BROUQGCRpU-_jwx2Y3rxczMDcJQqDXOXuIQ8BkmZZspqFfanLh2q1m_fbAGXNg_pR4u350Whgv8hZg0u9JU5kRviohcz1ZuwYlpCroyt1nZtnlR4R-onclEJNranQwUHbXKE7ZV92tOUPavKU3x68RM0K2fYBjAzs4eKuRede0oJQyTP3XzwbGEncHplYD4zzEj5sUOCRqgk4265ZeLlL5Is3zdK4hW6-rvuVNjBVE4xknKVoqZuoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاملا درسته این صحبت.
به محتوای ویدئو کاری ندارم، اما خندیدن به اینکه "آموزش «چگونه وایرال بشیم» خودش 60 تا دونه ویو خورده، هر هر" قطعا از کوته‌نظریه
و صحبت این دوستمون کاملا درسته.
اون شخص داره این ویدئو رو برای یه دسته‌ی بسیار کوچیکی درست می‌کنه، و کد تقلب نیست که بگی نگاه کن خودش نتونسته:)</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4874" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نسخه‌ی جدید Grok-Build هم اومده که زیاد چیز خاصی اضافه نشده، همون بهش نپردازیم بهتره فعلا</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4873" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V7BuYg7MpFT0veYIWgKmxi44lMr8BN-el01MPfRUza4hRV3GDdA06Kpd_ZNCsIrWlrQfxIWkwI_t2g3TISUUXBXaMfJW4837P8aXoWNMExZwFM1DEzRykPUkA3TUrhX6TgRzTMHvaHui_xAbiUuVaHAvLeMRvY2GnpSvDnPbmuc1Iod5_Svo92ztpR7ya-oTCjMNVVOlS0dR9Hgfohnq9obys0cxZ0c6dWRbwsOiXHzveDO8BlDIv4bC07h9dQV-sFiwL_u66odJl9NgrU1i2rVyutKT7XFthNQGMhH062Ia1NmNl0vJRDDwx3b2X7RJcLMjLBUmlAMAbVD0J1Eqew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fXAfArlyhyas_gx8wh6bm3fgHd7W4zjOyrAuqVeQ07x7EO48QANxPNu1Z4IKEHZ5SbwATQM5yDKnJP7aUD9Zv0iuJb_g25eoH2Rtz5J2HSPagxbGJjcCuUYYLNqR0SRKKgYpXFGFbL4Y3Za97603MvvQCPqsYcj85EMAxRInBjfSKpFwag7PcvJDmRz5XDkXx_M44XqftTaZDQdGeuZkSEqU7davCg916Gr6XpBE9dVCq4PNzB-d2ZVdbDdYXR3HOoog8hsVZ6ixbhmkDIt2cNQSeqO_S4Uxhk6WxCwGgIjsj4Bp7AaYcDhFMoj3-F-vgOgAdcNS8s3xT3ZOlUX1TA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دسترسی رایگان 14 روزه به تمام مدل های zed code
ادیتور Zed اشتراک ۱۴ روزه Pro خودش رو به همراه ۲۰ دلار اعتبار رایگان ارائه میده!
​مراحل دریافت: وارد سایت بشید تیک Free trial پلن پرو رو بزنید
zed.dev/pricing
با اکانت گیتهاب ( قدمت حداقل 30 روز ) لاگین کنید
✍️
CypherDeveloper</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/4871" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یه مدل‌های خفنی در راهن که باید وقت کنم بشینم راجبشون بنویسم</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/4870" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انقدر اخبار جدید از AI میاد زود زود که به قول یکی از بچه‌های توییتر نیاز به گزارشگر فوتبال داریم دیگه تولید محتوا کافی نیست</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4869" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4868">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hjCXDLd9GifzfDftiDXpASbXpFlnPyDDRHygP8ctQ8CgwNRbE1Zplr5Hi2YQczw2m1eJQb4J5AQYqKUA--43YraCegtR9AqKGuA45aS8v1cCa8BRtQLz3QE9IoSWNdaOKKJz7pA80zlrnrefXCDWKqE4YDtYozaEYAlU1n1xQkdEImn-CF3XeZ31Y03KcRM73wIXjWWA6B-uY94YH6t56ZwV2zjfJWka7f3n3KI-U7rqueJiKvXapzNRKbz7neGUcfn96oWhvNLc5Y1X_B1KRO2u4O8enckZpwx-lFViNLiV18AVfm3JptVyqRIExHyc7QlgFOgtAZQ_oZBnCzqddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین اپلیکیشنی که برای نوشتن چیز میزایی که توی ذهنم میان استفاده کردم، TickTick هست. ساده، راحت، بین گوشی و سیستم هم سینک میشه می‌تونید توی گوشی به عنوان ویجت هم اد کنید. خیلی هم سبکه در عین مدرن بودن و چشم‌نواز بودن طراحیش، هیچ چیز غیرضروری‌ای نداره. پلن رایگانش هم از کافی، یه چیزی اونور تره</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/4868" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4867">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مارک زاکرچیزبرگر هم muse coder داده که تستش میکنم. سرگیجه گرفتیم از بس بین ایجنتا چرخیدیم.
اما جدی مدل‌هاش قیمتشون عالیه اگه بنچمارکا درست باشن</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/4867" target="_blank">📅 05:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/4866" target="_blank">📅 05:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4865">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=AZgOSGd1t81uc_5UsKIvk6iqibb1wkj_oW3HCyLxid3w78rNxKDcCWpVydcigAvbmARIQXBpfFHt_nffuUdRzHL1WVSL1DzlTYMXweMc8JNANZ_eLpxQN-Pz7TnQRWXgWWO5FhWBKYgMEQl5dO9pkc9TIbdLMIgk4Yh0G5SkEJULTzBYfHp3-N4qMLjoyVdhH9B18rf_2RDxtKoq9pqkE9JvRMD2bkb5jKOcA4IUJC5rmfM5qZNasS80W2oZlbjYOND5Re9MRiMrH631AlPgFCqOTtfIFbiKoF7GGHVYxzBhZPtz4AxJosvTQRx706XtPOUDgv_DuchUAA_fS-4A3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=AZgOSGd1t81uc_5UsKIvk6iqibb1wkj_oW3HCyLxid3w78rNxKDcCWpVydcigAvbmARIQXBpfFHt_nffuUdRzHL1WVSL1DzlTYMXweMc8JNANZ_eLpxQN-Pz7TnQRWXgWWO5FhWBKYgMEQl5dO9pkc9TIbdLMIgk4Yh0G5SkEJULTzBYfHp3-N4qMLjoyVdhH9B18rf_2RDxtKoq9pqkE9JvRMD2bkb5jKOcA4IUJC5rmfM5qZNasS80W2oZlbjYOND5Re9MRiMrH631AlPgFCqOTtfIFbiKoF7GGHVYxzBhZPtz4AxJosvTQRx706XtPOUDgv_DuchUAA_fS-4A3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4865" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4864">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یکی از دوستام برای رفع لیمیت اوپن کد روی 9Router، حذف و نصبش می‌کنه و درست می‌شه.
به زودی واسش یه اسکریپت می‌نویسیم که این مشکل حل بشه</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/4864" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4863">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=Q-dYPThWZBt-TvY5v1Qcf-yNWcIDLS8M2M7oesGvWB3T-47Yg-Nkhy3pMQra7Wb4-VSP_cKcwU-k8uOb4NTj97SmzZkY_xA4HcQsGw06jMWSOunqjBbTKQjS7Gp0YirVVxesNOKJTE4Oo4PdwGaaVTIuAS4PIqOr1kRQQnndFLpr_8zdtsP_hvBCMmKU7kS1suRhOdWQ-FPfTSkJb7cvbXX_lIeXS113R3JFG7xotbUfdt5JfYektfjk1xQDAg4Z4mHTwWWJj5RwOM5NrP9OAfqCpiSNpH9y2bKwp-sVSGutQapcgiiPlnopRdN6Igyei7Sw_pr6ZXTAPXu7LcQY6g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=Q-dYPThWZBt-TvY5v1Qcf-yNWcIDLS8M2M7oesGvWB3T-47Yg-Nkhy3pMQra7Wb4-VSP_cKcwU-k8uOb4NTj97SmzZkY_xA4HcQsGw06jMWSOunqjBbTKQjS7Gp0YirVVxesNOKJTE4Oo4PdwGaaVTIuAS4PIqOr1kRQQnndFLpr_8zdtsP_hvBCMmKU7kS1suRhOdWQ-FPfTSkJb7cvbXX_lIeXS113R3JFG7xotbUfdt5JfYektfjk1xQDAg4Z4mHTwWWJj5RwOM5NrP9OAfqCpiSNpH9y2bKwp-sVSGutQapcgiiPlnopRdN6Igyei7Sw_pr6ZXTAPXu7LcQY6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/4863" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4862">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qOBqF6O90v1Ryh0-MVODIBiwUsHgebPBJgbATg9l9pjsPXJ-KEBHyuB6nQouQ4gjkQZsW5qLrfTGBQcXdalRDRrkHdURLDUeiFoOMwvkmmvj0KwjKwh_8LVa4NkBx8FgT6HB57wKIbAJM9Zo5zrJpJ0o7J1VrVFPsfQ7P-9DCE1xGF-rfhoU3ObOGL-_-pqyPJcfzwQxQMZWe1gyXa3CoVmr2FYR7_WXMogmzDfgAsOm_fi-XY7uvb7mMeVFT4jJg_-jeMaqiKkn0Jy9Asus06FehW99LVTCd4jwnduhaEJTRyAjfMheyR6AdX4JdW05IBT17BRyEJOyya8Igpfhgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه جوری ما رو دعوت کرده به سان فرانسیسکو، انگار حالا ما میریم
😏
😏</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/4862" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4861">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">Matin SenPai
pinned «
خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید: https://t.me/Editor_MatinSenPai شرایط کامل توضیح داده شده
❤️
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4861" target="_blank">📅 21:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اگر وسط آپدیت کرش کرد، یک بار دیگه باید re-deploy کنید</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4860" target="_blank">📅 19:31 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
