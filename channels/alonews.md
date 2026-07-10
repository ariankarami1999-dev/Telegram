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
<img src="https://cdn4.telesco.pe/file/t-ntRuMLm1TDik2h166rImzeEhnqVseHb8kNpeQG2Tqsf22YWyOZhmSBGMzBoTRtTDMAE3nJY0uxRP2XctEDIO5MCrCiZEwK5vFLh4isulif_Hh_bh-tynZirV-RFhe8rKljUNi7yJgmTyrsCG0ruO4ImiSgB-zVUWrfCYu_5jmcdfHrZqPwKeU2OSVJ1_DVHR-ICDt9ROO56XVQr27h9haOAIhlt_5rU3v44OEXtSn7r5iLqgwfo58uJQiB9ywpEWFyjQQc_VFVRGqg472E6qnWMwVurAXsv_SeQiCK4g1nF_TOXs32gDpKS7eod2vsIj03qKJ1aiXs9JMTBAjcjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 923K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 22:25:00</div>
<hr>

<div class="tg-post" id="msg-133121">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
العربیه:
وزیر کشور پاکستان احتمالاً به زودی از تهران بازدید خواهد کرد
🔴
العربیه از قول منابع خود از احتمال برگزاری یک تماس تلفنی چهارجانبه بین آمریکا، ایران، قطر و پاکستان خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/133121" target="_blank">📅 22:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133120">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری / وزارت خزانه‌داری آمریکا تحریم های جدیدی را علیه ایران اعمال کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/133120" target="_blank">📅 22:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133119">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ef9e8b4c7.mp4?token=UIUf8z3f8n9Uz6zfa6N8oc1PeKqt29ncA230FUYRciIh1yc67Brh3KY4B0G8NC913nrGrsPkl1h2r0kQ5iKq_BayrrLrY99yI14X3nqx3H_6zPVkWmajBW6232HHFcpnCSP1jE0TAT2jimlo-YYoGDPS_ubpAbG2vtLZs8kGybeMg8E4LOVIsAhTmeXN_TKFQgVzpVDfabx4TqhOljfvPSnLJeZNAxyJGUpXOqdFJWtedUfQMjWUcKmW5TvcKi2EBkqsnw1iDiHLMdhEuYZd6UQxSfIXRE2SC7zOWv1sg-gXxem9K4-3RXwYwLXts1HbhXk-eK3rCwu4GXZ4doqgkGEhyFgug8f5_1tk_sMnBi3erQJLDDLiqKhR9MkbkTKfN0F2FvxcDW085RZPlv53FpewfpLrp513FmbsZjQJkgYUrt0NjP-fs7GJAc6rXFpgWt3maPn2Xbg3OlCvys_D1SCLRwueyZf7sQdp0mul-afqOp3KXjZeNf62zwZ0m8aMpAdsDC0hRiW5QSb72xtEY2eKVTCYoCfIPstiYDXFHitAR0_KGWcF2fZhpdmE7d3PpuzPzDyWCkSSTlCXAm9jU3Cn_YnY_1O_y1h02H5hJEB1n-oVNhtoV6KVZcTwkYz6gBm1_T_JMx7mtxNbfPTaLfib_s2y6ZTHJx2aElgnNeY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ef9e8b4c7.mp4?token=UIUf8z3f8n9Uz6zfa6N8oc1PeKqt29ncA230FUYRciIh1yc67Brh3KY4B0G8NC913nrGrsPkl1h2r0kQ5iKq_BayrrLrY99yI14X3nqx3H_6zPVkWmajBW6232HHFcpnCSP1jE0TAT2jimlo-YYoGDPS_ubpAbG2vtLZs8kGybeMg8E4LOVIsAhTmeXN_TKFQgVzpVDfabx4TqhOljfvPSnLJeZNAxyJGUpXOqdFJWtedUfQMjWUcKmW5TvcKi2EBkqsnw1iDiHLMdhEuYZd6UQxSfIXRE2SC7zOWv1sg-gXxem9K4-3RXwYwLXts1HbhXk-eK3rCwu4GXZ4doqgkGEhyFgug8f5_1tk_sMnBi3erQJLDDLiqKhR9MkbkTKfN0F2FvxcDW085RZPlv53FpewfpLrp513FmbsZjQJkgYUrt0NjP-fs7GJAc6rXFpgWt3maPn2Xbg3OlCvys_D1SCLRwueyZf7sQdp0mul-afqOp3KXjZeNf62zwZ0m8aMpAdsDC0hRiW5QSb72xtEY2eKVTCYoCfIPstiYDXFHitAR0_KGWcF2fZhpdmE7d3PpuzPzDyWCkSSTlCXAm9jU3Cn_YnY_1O_y1h02H5hJEB1n-oVNhtoV6KVZcTwkYz6gBm1_T_JMx7mtxNbfPTaLfib_s2y6ZTHJx2aElgnNeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فحاشی های هانتر بایدن پسر بایدن به دونالد ترامپ: چطور ترامپ از این کارها جان سالم به در می‌برد؟
🔴
چرا هیچ‌کدام از همکاران سابق شما به او نگفتند: «برو در ماتحت رو بزار، آقای رئیس‌جمهور»؟
🔴
عذر میخواهم... پدرم واقعاً می‌گوید: «توهین نکنی ها، هانتی»
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/133119" target="_blank">📅 22:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133118">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوری / وزارت خزانه‌داری آمریکا تحریم های جدیدی را علیه ایران اعمال کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/133118" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133117">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
فایننشال تایمز: آمریکا یه هیئت فرستاده بیروت
🔴
تا به حفظ آتش‌بس بین اسرائیل و حزب‌الله کمک کنه و نذاره این آتش‌بس به هم بخوره
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/133117" target="_blank">📅 21:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133116">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سناتور ارشد جمهوری‌خواه لیندزی گراهام: ما با کاخ سفید بر سر نسخه‌ای از لایحه تحریم‌های روسیه که آن‌ها از آن حمایت خواهند کرد، به توافق رسیده‌ایم. این بدان معناست که این لایحه به قانون تبدیل خواهد شد.
🔴
من همراه با سناتور بلومنتال به نزد رهبران جمهوری‌خواه و دموکرات خواهم رفت تا ببینیم آیا می‌توانیم زمانی را برای پیشبرد این بسته تحریم‌های روسیه پیدا کنیم که ابزارهایی را به رئیس‌جمهور ترامپ بدهد تا به پایان دادن به این جنگ کمک کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/133116" target="_blank">📅 21:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133115">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
بزالل اسموتریچ، وزیر دارایی اسرائیل، اعلام کرد که طرح‌هایی را برای ساخت سه شهرک اسرائیلی در شمال نوار غزه آماده کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/133115" target="_blank">📅 21:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133114">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
صندوق بین المللی پول IMF پیش بینی کرد رشد اقتصادی ایران امسال منفی ۵.۴ درصد خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/133114" target="_blank">📅 21:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133113">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
پهپادهای اوکراینی شب گذشته به ۱۳ شناور در نزدیکی کریمه، از جمله ۱۰ تانکر، یک کشتی باری، یک کشتی مسافربری و یک یدک‌کش، حمله کردند.
🔴
در ۱۲۰ ساعت گذشته، به ۴۸ شناور حمله شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/133113" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133112">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oL0Froa6X-JiD5QVtT5Ex_Zai60TlN-uLOwESIUyXMm-hUQCHqRMt2jO20am4d6a73IQENpGdzoKxVqq75Q4DjOMFkHHLY8bbWDARdUa8LiKrAqjbdYosSitRc7SyvnYb-mXc38EM0VJHuIlPLhu8_WaM6cjXRPQRXKhEkVE4tzKOrJYwp3WHZqddndjcwzOqsv7G5RWuT9aaATScH9WwRVqDme-2gZ2EygWjUx62kmI461iJaN-Ru_-U5QkkHkavcb1piCAVDqlhpEvwkJ-mq1_8bON_WRQaaaK8D3UwG-6MEmFWvAE7b-gugIEKGTPTY8AHH14YqQr6BEpJPtR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار CBS: مقام‌های ایرانی روز شنبه برای گفت‌وگو درباره تنگه هرمز و اختلاف بر سر مسیرهای کشتیرانی که از آب‌های سرزمینی ایران عبور می‌کنند، به عمان سفر خواهند کرد.
🔴
میانجی‌های قطری به‌تازگی مشهدِ ایران را ترک کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/133112" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133111">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
شهباز شریف در تماس با پزشکیان: ایران و همه طرف‌ها خویشتن‌داری کنند.
🔴
بر ضرورت پایبندی به مفاد تفاهم تاکید می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/133111" target="_blank">📅 21:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133110">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
منابع خبری اسرائیلی از سقوط یک هواپیمای سبک در فرودگاه این ورد واقع در منطقه شارون خبر دادند.
🔴
بر اساس اعلام این منابع، در جریان این حادثه دو نفر مجروح شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/133110" target="_blank">📅 21:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133109">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d149dc62f3.mp4?token=H2ExFIBl8F7B2weNIVm7VMQmNKWLIBQKYInzBU7qvoE6UR0ec8l4Sv3AnldHiouYtbPkCjk2OlwGEk-tUCJjChXNXDibrALl8QLyryAN6cX5QhAz9l0bDQt605eAxAa1JACfmhZ7k_c8Xb4wjlZ3JZqaLHwh7rbqz4OdmxHm82B3jAfhG5NtTtsq31d48Yu21JlXHbBCvmUyiSj3NjdFs9hC3v2HQRUct2jM8_qbJlowqu5HLfFKeLmcFLeXvcG28Hf5Hf8kZJ_w3gGWWRiaOAIlv0giF3fqWmyR9PdqGWL9sI6izHu8Sh8NpbxndJAoHDMhhotjVV-y41-mcGK6BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d149dc62f3.mp4?token=H2ExFIBl8F7B2weNIVm7VMQmNKWLIBQKYInzBU7qvoE6UR0ec8l4Sv3AnldHiouYtbPkCjk2OlwGEk-tUCJjChXNXDibrALl8QLyryAN6cX5QhAz9l0bDQt605eAxAa1JACfmhZ7k_c8Xb4wjlZ3JZqaLHwh7rbqz4OdmxHm82B3jAfhG5NtTtsq31d48Yu21JlXHbBCvmUyiSj3NjdFs9hC3v2HQRUct2jM8_qbJlowqu5HLfFKeLmcFLeXvcG28Hf5Hf8kZJ_w3gGWWRiaOAIlv0giF3fqWmyR9PdqGWL9sI6izHu8Sh8NpbxndJAoHDMhhotjVV-y41-mcGK6BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
داده های ماهواره‌ای امروز دو اصابت آشکار در باند فرود در فرودگاه بوشهر در ایران را پس از حملات اخیر ایالات متحده نشان می‌دهد.آثار سوختگی نیز در اطراف باند قابل مشاهده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/133109" target="_blank">📅 21:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133108">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
تسنیم :  انفجار در قائمشهر را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/133108" target="_blank">📅 20:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133107">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
کان: ایالات متحده از اسرائیل خواسته است که از انجام هرگونه اقدام غیرمعمول در جنوب لبنان خودداری کند. بر این اساس، رده سیاسی به نیروهای دفاعی اسرائیل (IDF) دستور داده است که تمام عملیات حساس در جنوب لبنان را متوقف کنند. این دستورالعمل به IDF تا اطلاع ثانوی و تا زمانی که مشخص نشود تشدید فعلی تنش بین ایالات متحده و ایران و مذاکرات بین اسرائیل و لبنان به کجا منتهی می‌شود، معتبر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/133107" target="_blank">📅 20:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133106">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiSWS1InBAvwfbSb7cYdb9GedIfXBuQQz4H0sGRIS4_ac5eDPIJCKVfVXyl7pPh14UJrk4Gsc7q7ZhEJAXnhqb6o67CqocpufXIzVM5xkEa49GXthsPc3aR7Hsscvhh3358L6I71Ej3Mn6KhWyw9N-78labPZ7FFh50zEdzBbZwI3IJhCgwIxzD-wGeEMJdRDjL3DXxrAK55ps24N86EG2WakUQfzM4dnkIoZwm7fcVJGU5IV8aZWjAfBshWjGDD3nhKMeFdoRLVGUnE45O-TVNcvGHH7mfnYzX10NDqT8k34gKnBI0YIfPTug4EAVqHoolZXnRqOkC-crttDHnA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شورای اجرایی «سازمان بین‌المللی دریانوردی» (IMO) در نشست روز جمعه ۱۹ تیر، با صدور تصمیمی، تلاش‌های ایران برای تحمیل حاکمیت بر تنگه هرمز و ایجاد نهادی جهت کنترل تردد در این آبراهه را به‌شدت محکوم کرد. این شورا از تمامی کشورهای عضو خواست تا حاکمیت جمهوری اسلامی ایران بر این تنگه و صلاحیت قضایی آن بر مناطق دریایی کشورهای ثالث را به رسمیت نشناسند.
🔴
این تصمیم در حالی اتخاذ شد که تنش‌های نظامی اخیر میان جمهوری اسلامی ایران و آمریکا و حملات متقابل دو طرف، نگرانی‌ها را درباره امنیت منابع جهانی انرژی و ایمنی کشتیرانی افزایش داده است. پیش‌تر، نهادی تحت عنوان «سازمان تنگه خلیج فارس» در ایران اعلام کرده بود که تردد کشتی‌ها منوط به دریافت مجوز از این نهاد است؛ اقدامی که از سوی شورای سازمان بین‌المللی دریانوردی «مداخله در ناوبری بین‌المللی» خوانده شد.
🔴
در مقابل، هیئت نمایندگی ایران در سازمان بین‌المللی دریانوردی، ضمن رد این اتهامات، آن‌ها را «سیاسی و فاقد مبنای قانونی» خواند و تاکید کرد که ایران به دلیل عضویت نداشتن در کنوانسیون حقوق دریایی سازمان ملل (UNCLOS)، خود را ملزم به رژیم حقوقی مبتنی بر این معاهده نمی‌داند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/133106" target="_blank">📅 20:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133105">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
قالیباف : تنها با کسانی می‌توان با آمریکا مذاکره کرد که برای جنگ آماده باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/133105" target="_blank">📅 20:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133104">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
قالیباف : این درگیری با تسلیم شدن ایران تموم نمی‌شه
🔴
اگه آمریکا به تفاهم‌نامه عمل نکنه، ایران برای دفاع کامل آماده‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/133104" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133103">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رویترز: کاهش فروش نفت ایران به دلیل تغییر رویکرد شرکت‌های چینی که به سمت خرید از بازارهای دیگر در منطقه گرایش پیدا کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/133103" target="_blank">📅 20:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133102">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: ترامپ مدیریت پرونده ایران را در دست دارد و اسرائیل در این معادله نقشی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/133102" target="_blank">📅 20:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133101">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e41Xk20WT-zVxmLf_i-tILz-mVLRN2IbZG91-skDhXxk1SC_-8MgetdACWqNZ9BcyRCMvb6eBI-Vl6coYj1sm27zp2nKtyhPeXNBd59aUz2iVfHroKgy711GyuuzsTwpE5jl4evSEWNPzs9le2Hw2glajcinxzvhmqgFHqv2sqovkNvh2KaKhR6Gq5RYZkbjK4opxlkqXKwnXWo3ylJHbMlxnmAl8pFuPoEft-lo2Sp-ADC6LH8Teeh_P6DPiD0WdU4cdizqz85MlK1cx4-BCGz-gkqpzHslYv1Pq5mTwNsbXdohbzgF5qEMXJLmE6CJOXqUwzNGI6xtQqghnpf4cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیلی : ترامپ بوزینه‌ای است که نام انسان را سرقت کرده و مانند یزید، به زباله‌دان تاریخ خواهد افتاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/133101" target="_blank">📅 20:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133100">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزارت بهداشت لبنان : بر اساس آخرین آمار، از آغاز حمله اسرائیل در دوم مارس، ۴۳۲۱ کشته و ۱۲۲۰۰ مجروح شده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/133100" target="_blank">📅 20:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133099">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
جوزف عون ، رئیس جمهور لبنان: مذاکرات مستقیم با اسرائیل ادامه خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/133099" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133098">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=clpxHV5l5a5ZnVvWmK5704QFABP1Juwm0KjJHtVZsqWTvYazeaRHiJ62Nw69gXihcSoEqzJ6WpN-46H0Zsnrl_mglt0Y94ybenoD7EEJzVoxWcO0NHwu83SMklZoNG1TXmeht0tGWmihRGPA_szXj0tjpRmSbl_btSXMngzpk6Uldv3Q6YWBkumRm8wQLJRnL8j0xQ4Yp4k7_JKfzw3aD9Ondk1DFZqF65yfLM_frapf6SWN9ieyWvrfXdtYr6WPj77K4YMiWfTPBuV8M-ZRCEXFVIUtFZt3Etxw4zFV9Ja_dSQgqDx0dxgi7Beu4KB7Ses-4KgKmOS4r6HEr3w1Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=clpxHV5l5a5ZnVvWmK5704QFABP1Juwm0KjJHtVZsqWTvYazeaRHiJ62Nw69gXihcSoEqzJ6WpN-46H0Zsnrl_mglt0Y94ybenoD7EEJzVoxWcO0NHwu83SMklZoNG1TXmeht0tGWmihRGPA_szXj0tjpRmSbl_btSXMngzpk6Uldv3Q6YWBkumRm8wQLJRnL8j0xQ4Yp4k7_JKfzw3aD9Ondk1DFZqF65yfLM_frapf6SWN9ieyWvrfXdtYr6WPj77K4YMiWfTPBuV8M-ZRCEXFVIUtFZt3Etxw4zFV9Ja_dSQgqDx0dxgi7Beu4KB7Ses-4KgKmOS4r6HEr3w1Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در شرکت اکسین پالایش پلدختر
🔴
فرماندار پلدختر از وقوع آتش‌سوزی در شرکت اکسین پالایش سراب حمام خبر داد و گفت نیروهای آتش‌نشانی و امدادی در حال مهار حریق هستند.
🔴
به گفته وی، آتش‌سوزی از انبار مواد دفعی آغاز شده و تاکنون هیچ تلفات یا مصدومیت جانی نداشته است. علت حادثه در دست بررسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/133098" target="_blank">📅 20:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133097">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نماینده آمریکا در سازمان ملل: در دیپلماسی با ایران همچنان باز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/133097" target="_blank">📅 20:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133096">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
الحدث: ‏تماس تلفنی نخست‌وزیر پاکستان با پزشکیان و بررسی تحولات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/133096" target="_blank">📅 20:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133095">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
نماینده روسیه در سازمان‌های بین‌المللی واقع در وین : روسیه خواستار تفاهم کامل ایران و آمریکا و حل‌وفصل جدی مسائل موجود است.
🔴
ایران و آمریکا باید راهی برای برون‌رفت از وضعیت کنونی پیدا کنند، در غیر این صورت وضعیت در منطقه خلیج فارس بسیار پرتنش، ناپایدار و خطرناک خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/133095" target="_blank">📅 20:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133094">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فارس: درپی انتشار اخباری از سوی العربیه و فاکس‌نیوز درباره برگزاری دور جدید مذاکرات ایران و آمریکا در هفته آینده، پیگیری‌های خبرنگار فارس از یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایرانی بیانگر این است که این ادعاها صحت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/133094" target="_blank">📅 19:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133093">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
شورای شهر تهران: رایگان بودن مترو و بی‌آرتی در تهران تمام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/133093" target="_blank">📅 19:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133092">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
چین و روسیه قطعنامه شورای امنیت درباره برنامه‌ هسته‌ای ایران را مسدود کردند
🔴
روسیه و چین پیش‌نویس قطعنامه‌ای را که با هدف بحث درباره تحولات برنامه هسته‌ای ایران و اقدامات مرتبط با آن تهیه شده بود، مسدود کردند.
🔴
مسکو و پکن تأکید کردند هرگونه اقدامی در شورای امنیت باید با هدف حمایت از روند دیپلماتیک و تشویق گفت‌وگو باشد.
🔴
هر دو کشور معتقدند که رسیدگی به موضوع هسته‌ای ایران باید از طریق مذاکرات و آژانس بین‌المللی انرژی اتمی انجام شود، ضمن اینکه امکان احیای توافق هسته‌ای نیز حفظ شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/133092" target="_blank">📅 19:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133091">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xz_zjn6AqzquCoNLtrytKY4H3MNbGc25UfYVJ1tKK8ObJybnCU5t5HunIdrEwbXSfZmpittOplaNRGSDEwMHBoqTPXLUCwAS6_LQnJEWACDDu-b79RjvEmAvlYCCiSotJ7xKXgYP5OqHuwvA55jp17q4KL0R6YhIM3-mv0S-Z9bD-HmLbJ22yDcklbRyykmnNMyHA3TvcwtUppcXMC1-N3a6XVnzAcvodBrrma6jegU-kudlQ3odsDN9iIA4ylHzxx8B-vlPMcCOUBKwj5D9nBHzoxKeVchUm9bzhs5UjN3_2KE7fr2sOhekIWg4eopr6W3Axd5i_jVrqj_NbAP3Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی، نزدیک به تیم مذاکره : ترامپ و آکسیوس رو نادیده بگیرید
🔴
تا وقتی دولت ترامپ به تعهداتش عمل نکنه، هیچ مذاکره‌ای انجام نمی‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133091" target="_blank">📅 19:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133090">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
اف‌بی‌آی جزئیات جدیدی درباره یک طرح تروریستی علیه رویداد یو‌اف‌سی در کاخ سفید فاش کرد:
🔴
«ما متوجه شدیم که این گروه به‌طور ادعایی قصد داشت حمله‌ای با تلفات انبوه را با استفاده از پهپادهای مسلح به مواد منفجره و سلاح‌های آتشین برای شلیک به مردمی که در میان جمعیت فرار می‌کردند، انجام دهد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133090" target="_blank">📅 19:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133089">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ngPf_gq2HfzrQTiu4ClWlSy409MB7W6X9TNjCriweZBuNoyxgYXWnEPZ1MgHfYZvEYmAMpwWtsCt3nWlOWfurr9NGVZfGxYd1WqEonuwuhT_RkG988p9GkROdjNf41CYL-dBAj348tT0n3zJnoWZDIaeszJpf6RcHv-jw-AX0RJXi_9HpyUWyntK2kvNu5Vy1uC3FTcvixlzE-iunSUcyxfruifxPzmraicJzSc-0Gqg3s8YFOiEDeZdRhGAVAJsNMMWzlZtswWXzG-r-_I1pwqcrdcVlHloH3E8tHa1_HHm5vMajORiNtmnlZE7mYvWv0lTZn5-CXTHiVYzY0epiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: دور جدید مذاکرات ایران و آمریکا، هفته آینده توی سوئیس برگزار میشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/133089" target="_blank">📅 19:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133088">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
نماینده پاکستان در شورای امنیت: ما به دنبال دستیابی به توافقی جامع بین آمریکا و ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/133088" target="_blank">📅 18:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133087">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سی‌بی‌اس: ونس، ویتکاف و کوشنر در تماس با مقامات قطری در چارچوب تلاش‌ها برای تقویت دیپلماسی با ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/133087" target="_blank">📅 18:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133086">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ به نیویورک پست: من دستور دادم که در صورت موفقیت در ترور من، ایران را در سطح بی‌سابقه‌ای بمباران کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/133086" target="_blank">📅 18:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133085">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdB0ePw6FjYSVF2PV9-dNM7VffqhDEXs3DCZl7ugq5plhtIongHtwgm5P3hP3v0Z5Gg84Q2iLsOJ-5fpYt0WH79Gdx7ysBDg_74fgs6z3Ul7XMDZWuVmx_o0x_f7c5dYh629xYyLesc9usTdHNmEjtnYoLL9-s0OBG-3Oskur8rEEcUizCLPMLpZ6BF7HVLDhxC6M_ofgnHUdx3QeJIp1SuQG4yG84Gpxin5vzgfaNqMhIT5-znHIPGSZTa4WrMiGTtd2tNoicyWxVQY_7QRSDXGVsJcwbtXPr5g4vmnciich-q6fZG3ImLeFEzub2OjTMnU-BazU92tYF20U4ZiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری منتسب به کنارک
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/133085" target="_blank">📅 18:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133084">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری / ترامپ به نیویورک پست: در صورت موفقیت ایران در ترور من، دستورالعمل‌هایی برای اقدام صادر کرده‌ام!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133084" target="_blank">📅 18:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133083">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
گزارش‌ها از انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133083" target="_blank">📅 18:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133082">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/391b205ef7.mp4?token=kgw7vk0rMR1EBdos3ch0hpdA9JLk4AAdi0vW7eY2TQO9Qw3v_5F_GirqLCwIn0IJSKFc4m64i13w-r1qRyrt1uKUvX5NV2VllJvQjtDLd6kWfK4GmDt_ReiivAXCidpyRxDHgA4ZKNOoAPSK1aTfcOrp_2Fa6vZI4yjkRzACBcwJlPjvQ0UaCYQx-d-fpUzqlmxsZsOhjrlmjnJSevpS5R13lCn5WvoaAhNcHn0ILcliGe_8u3xdkipxe_50hgGS_5z1mfvvl8XGGZ5Y73uVj_yjq9g8oChY1Uu3Zl1j6L3Iq2gSsGpM8am-IYrRGbvdRTfqm0VbtkeBswqQz89kkw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/391b205ef7.mp4?token=kgw7vk0rMR1EBdos3ch0hpdA9JLk4AAdi0vW7eY2TQO9Qw3v_5F_GirqLCwIn0IJSKFc4m64i13w-r1qRyrt1uKUvX5NV2VllJvQjtDLd6kWfK4GmDt_ReiivAXCidpyRxDHgA4ZKNOoAPSK1aTfcOrp_2Fa6vZI4yjkRzACBcwJlPjvQ0UaCYQx-d-fpUzqlmxsZsOhjrlmjnJSevpS5R13lCn5WvoaAhNcHn0ILcliGe_8u3xdkipxe_50hgGS_5z1mfvvl8XGGZ5Y73uVj_yjq9g8oChY1Uu3Zl1j6L3Iq2gSsGpM8am-IYrRGbvdRTfqm0VbtkeBswqQz89kkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از بین ۱۲ فروند جنگنده رادارگریز F-22A Raptor نیروی هوایی ایالات متحده که در پایگاه هوایی اوودا در جنوب اسرائیل حضور داشتند، ۱۰ فروند در حال انتقال به ایالات متحده هستند. تصاویر نشان می‌دهند که هواپیماهای F-22A در پایگاه هوایی RAF فیرفیلد در بریتانیا فرود آمده‌اند، که احتمالاً یک توقف موقت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/133082" target="_blank">📅 18:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133081">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری / ۳ انفجار سنگین در کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/133081" target="_blank">📅 18:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133080">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری / ترامپ به نیویورک پست: در صورت موفقیت ایران در ترور من، دستورالعمل‌هایی برای اقدام صادر کرده‌ام!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/133080" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133079">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
براساس آخرین آمار پایگاه بین‌المللی هواشناسی «Ogimet» که وضعیت دمای ایستگاه‌های هواشناسی جهان را رصد می‌کند، بندر دَیّر در شبانه‌روز گذشته در صدر فهرست داغ‌ترین نقاط زمین قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/133079" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133078">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7c4e411a5.mp4?token=G1r2rS_AKXckRlBILt85yXm4eT2EWv-kIh__PwDkolEkLq_E7ArIjN2laBETuSeDZJrWgdpPNA1gvtNUsFnLPZGylR-ZDLIyXnw8-TZmBhyvT0NX1RdEAK9QnHl-GF_l2a3hb3WFJTIFlmv0R0r-Xw4rec9vUyrJ54UnDojWxAfD27cyOGNI6SMn22y37WviA0PLirdbX0eUII47_sgbFz1iET630-CMnmvb7_wRAxtFFz8OLuv5-mrxKZ_dtmMekuQmrmxxSOGI0UIaUmuw6eUFANGs7kHW5V0PgKTuUwE0u1GvqeaADBTzCosQ2VqZXqy7YpZPn9pzLlKv68TeSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7c4e411a5.mp4?token=G1r2rS_AKXckRlBILt85yXm4eT2EWv-kIh__PwDkolEkLq_E7ArIjN2laBETuSeDZJrWgdpPNA1gvtNUsFnLPZGylR-ZDLIyXnw8-TZmBhyvT0NX1RdEAK9QnHl-GF_l2a3hb3WFJTIFlmv0R0r-Xw4rec9vUyrJ54UnDojWxAfD27cyOGNI6SMn22y37WviA0PLirdbX0eUII47_sgbFz1iET630-CMnmvb7_wRAxtFFz8OLuv5-mrxKZ_dtmMekuQmrmxxSOGI0UIaUmuw6eUFANGs7kHW5V0PgKTuUwE0u1GvqeaADBTzCosQ2VqZXqy7YpZPn9pzLlKv68TeSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده چین در شورای امنیت: قطعنامه ۲۲۳۱ منقضی شده و بررسی پرونده هسته‌ای ایران پایان یافته است
🔴
قطعنامه ۲۲۳۱ در ۱۸ اکتبر ۲۰۲۵ منقضی شده و رسیدگی شورای امنیت به پرونده هسته‌ای ایران پایان یافته است.
🔴
اصرار برخی کشورها برای برگزاری نشست درباره موضوعی که از دستور کار شورای امنیت خارج شده، فضای مذاکرات را تضعیف می‌کند.
🔴
سیاسی‌کاری در شورای امنیت، اختلافات درون شورا را تشدید کرده و روند دستیابی به راه‌حل سیاسی را با مانع روبه‌رو می‌کند.
🔴
چین از کشورهای ذی‌ربط خواست با حسن نیت، مفاد قطعنامه ۲۲۳۱ را اجرا و از اعتبار شورای امنیت و دیپلماسی چندجانبه صیانت کنند.
🔴
نماینده چین با حمایت از موضع روسیه تأکید کرد که شورای امنیت دیگر مأموریتی برای بررسی موضوع هسته‌ای ایران ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/133078" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133077">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
نماینده فرانسه در سازمان ملل: ایران باید به طور کامل غنی‌سازی را کنار بگذارد و به آژانس اجازه بازدید از تاسیسات هسته‌ای را بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133077" target="_blank">📅 18:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133076">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نماینده فرانسه در سازمان ملل: ایران باید به طور کامل غنی‌سازی را کنار بگذارد و به آژانس اجازه بازدید از تاسیسات هسته‌ای را بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133076" target="_blank">📅 18:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133075">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری/ترامپ:  با ادامه مذاکرات با ایران موافقم اما آمریکا به ایران اعلام کرد بدون تردید آتش‌بس پایان یافته!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/133075" target="_blank">📅 18:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133074">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXTVjzhv2olwccUxQyA9LPrYk6IMJOPbT4pRFjmfgot4buWCaPDdZ2rFNy40ecmOQJg-HLUmEjgmeBG_ZmhTOKuZTlI9XEgANgw4YZSvgjmGt3qLF5ZMKlBA352G9_Izcd6OuWPy9uWp_tD4naVwtnAJuVG50vlDtWWhzEGmD6A6zAp6FQEPoKlgvLJzHIoGwwukHbyAn9j-7b8aqlNGb97I6WX_OZW1qQCRA6sc8zWCU_03501Wr1qXei56oKjlSeUMXKbAw24MAlxMFeKxZSbwg675YmNCC-Mo9oFjyLcNF1Hk8Kiikc6zYu85zmbbugiDHpOxN2C5Kbgr3ngRHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره‌ای به تاریخ امروز از ناوهواپیمابر ابراهام لینکلن در حوالی دریای عمان و ۵۰۰ کیلومتری تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/133074" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133073">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSCKxP5oDHeQqE3AqPtpCHM0Pa42manTE3hp6WtkSA2j55mjCd3m85yByXoac-ogx94Zv1fMrnZYRGVqBjysu4ZGIcB0G8EcJN_Q_UqciqRaNBLqPZmNoze9OiMUB-f-J434iw6pKM_2Nm9IubL0qaKgGeSK7IWsxEwmALJDRasZX1XaVqhD2ggqiluuUiSEZpot0Cc1uylfYrZJo7Xdl7MZEE9WpR6hSuqRbCPMBHb16lhlOwc1ksz4rDCIrhbOZqmngSluoF79kJau7BADJBo2BnBlSrNbs95Qx7L1iB5dVu7jZ3sdaOcYIhAyuVEzCPzhSt5oK1gSFooy_wN0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور مجتبی خامنه‌ای در مراسم
‼️
🔴
امشب، موقع برگزاری نماز میت برای علی خامنه‌ای تو مشهد، یه فرد با صورت پوشیده و ماسک، سمت راست تصویر و بین جمعیت دیده شد
🔴
اطراف این شخص هم چندین محافظ ایستاده بودن و همین موضوع باعث شد توجه خیلی از کاربران فضای مجازی بهش جلب…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133073" target="_blank">📅 18:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133072">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlHAf15YX-dez7DIbqUKVpoQqScihuRvOZWbxYlWuzpavwJLq5OsfVC-RK8dUlHcIEOXZfmA5Gdi-s1Wc3n7m_nmttSQXT8fC3Vc3xI9-LJ5VbDm3W3iCi1F7-bieqTPMUD2qFGBRQedCvKpLhMT81_zHpx7uus1TR39ID3qhM3xZnJzwON-Tyji4-ObetMnS94tnMTFMWhyt7iqqXUFcZgjGX_3EGIKEZE-QJ_1d9HKmDuYXRO7fWUi_q3sGLep2Dxu6Dykpes1QnDreISQlqL81_WFux35I8rP_agH0znZN8bNNjMIWeQ6V_48zTVIE9-vYNbQFNtkVgSgHp9Qjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره ای از پالایشگاه ساراتوف روسیه که واحد اصلی تولید بنزین آن تقریبا نابود شده است
🔴
این پالایشگاه تا اطلاع ثانوی فعالیت خود را متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133072" target="_blank">📅 18:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133071">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
روس‌اتم: ۶ نفر از کارکنان ما بازگشت به نیروگاه بوشهر را آغاز کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/133071" target="_blank">📅 17:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133070">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmvI3xjcoT6m-DVirIO1PnySV3MYck8Q2Q4ZSrxwbBvMz6oqON43L_Fw-ILjoInNTPY5gChSu8bE1gC-oKWHjyfnWGFoXq12zELBaS0Zl0wGcmJxNP1RLq2DEsqJS85MlCQ9YrFahIzhwrSYlWa6zKhKH3lcgycTqp7Zd8uxmrt5a3db2uml9NiBiea0uhV3EDgZtBunf82-axLwNVbExyG8dL4Jg2oJkQUrWEEMylOXxH2BfBPMJHE8iw4UFRI2pzcsC1MM_EFFtM5EaMi30hbxKRXuKXPOJZLVM2YxqhufUt3Pcx5Tw7IWzb-nDrjt3rhXxPDhnYlJA1XzC5x_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد هواپیماهای نیروی هوایی ایالات متحده که امروز در پایگاه هوایی شاهزاده سلطان در عربستان سعودی مستقر هستند، به کمترین میزان خود از زمان آغاز این استقرار در اوایل ماه فوریه رسیده است.
🔴
آخرین هواپیمای نظارتی E-3 در اوایل این هفته از آنجا خارج شد. در حال حاضر، یک فروند E-11 و ۹ فروند تانکر در آنجا باقی مانده‌اند.
🔴
به نظر می‌رسد که ارتش ایالات متحده بار دیگر فشار خود را بر ایران افزایش داده است، و به همین دلیل، بسیاری از تجهیزات حیاتی مورد نیاز برای انجام عملیات‌های بزرگ، از این منطقه خارج شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133070" target="_blank">📅 17:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133069">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
طبق تصاویر ماهواره‌ای یک ناو هواپیمابر آمریکایی به همراه حداقل 3 ناو جنگی در اقدامی عجیب به فاصله کمتر از 300 کیلومتر از سواحل ایران رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133069" target="_blank">📅 17:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133068">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
رویترز به نقل از سه منبع نزدیک به کرملین : حملات اخیر پهپادی اوکراین به پالایشگاه‌ها و بنادر روسیه، عزم پوتین را برای ادامه جنگ بیشتر کرده
🔴
پوتین در زمینه تصرف باقیمانده منطقه دونباس اوکراین پایش را محکم کرده و مشاورانی را که پیشنهاد آتش‌بس در امتداد خطوط مقدم فعلی را داده بودند، توبیخ کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133068" target="_blank">📅 17:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133067">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjxBry6Gf9YZ2dzVFli4WJhPbiW0ziiD-mi89i3rc_YyYCFGCi0a-mpPYjNbaSBDvcWnWhVKnZuXHBmhvkUviAQWl614ombuNSBg3FfjVPbAJNfIs1c1rLCbxRFXwEF_w-U1IExRB6xiOooFLErBq_1HsetjOXzj9s4SRMCdRBPGfYmkqiOTbJcqISHdcxehyZYiEyXJKZ8eseXzgnkfJonJewYU8Bhqq1YjMZXYaZ1wNqlRcNa8bilmHMkcbVy2wYVMD3vPuZhXwePzw3O49q2jwI3uiJTHlAAEv4yrgWtJTnLWKYmqrYydo3BNmjkRBBINjgSVxWvgsJdseY3YrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق تصاویر ماهواره ای منتشر شده؛ ایران مسیر های منتهی به سایت هسته ای فردو با تپه های خاک مسدود کرده تا مانع حرکت سریع با خودرو به سمت این تاسیسات شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133067" target="_blank">📅 17:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133066">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
شرکت ردیابی دریایی کپلر: فعالیت کشتیرانی در تنگه هرمز به شدت کاهش یافته و تنها ۲۲ تردد تأییدشده در روز پنج‌شنبه ثبت شده
🔴
تنها یک شناور از کانال متعلق به عمان استفاده کرده و مابقی از مسیر دریایی تعیین‌شده توسط ایران تردد کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133066" target="_blank">📅 17:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133065">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ti3Q_g-3auUfqmsOtBRWcb7b3n47FmocPMdhWYli0xloXKfCdZamL9b2JKFhqa7aQcHeRGGXY3k_IQeEyyP6JkYQwh7G05q_mZkl-ZwfFXdIGVclS1AioJo1xLSqLViwl0hI541x05m4BADSZxJAKnLLHIguP2J4S6-FcvMXJgrCXAtmDb7KBHAzGkwdvWra7wChfk3C27XTorQsx_NHrwNhSWOZwrM4rji12d_nrLGr6hzwJwO965t5nnEuWOqgqam0QPpyOr8Tx9-PYgcedAT7qtSmleR3JDkI8PLx4_ol4tCmvGQrREL1yfrcsXNNEgKByVEEwmDvOGOAsdlQZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لیویت، سخنگوی کاخ سفید:
جوون‌های نسل Z که از وضعیت اقتصادی و زندگی تو آمریکا گلایه دارن رو بفرستید ایران؛ خیلی زود قدر آمریکا رو می‌دونن و دلشون می‌خواد برگردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/133065" target="_blank">📅 17:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133064">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-DABUYM_vyW80kqCWsRK4IcYOhGyvx4YNJK90pOvy7m_PLRInmiW3O2PARoWwIv2NwB7ZrdmWNFjkuE0YqV94gicDvxaeen4Os2UTqTqLj4iS-QV2x9emIEsschY-48Ulw3NslrfKuTePX0dciZqSIm1cb_OY8YtvPS0FQkefXpH51G_qQQ-Dx0cYiqnw_GAOSR7qys4_gLog3k_0MWEN7v2zPplOnVSleXqolJChEjA_xAs9Qx84jtBj9opDa0VcwywR9RsSinMIZrCw1AraxjviH2-gkLucPF50K9rsFzddCjtrQT9e4Ozq2A3hbYrGqiV1Jbn13vujnXD8FhgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام جمعه اهواز(مگامن): هر کی موشک و پهپاد داره، ترامپ رو بکُشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133064" target="_blank">📅 17:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133063">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پشمام
😐
بعد از برد دراماتیک آرژانتین گروهی از طرفداران زن این تیم در استادیوم لخت شدن
😐
⚠️
⚠️
مشاهده بدون سانسور فیلم</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/133063" target="_blank">📅 17:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133062">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری/ خبرگزاری CNN:
دولت ترامپ در حال بررسی آغاز مجدد محاصره دریایی علیه ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/133062" target="_blank">📅 17:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133061">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnKaTNErB2Vo2PVPoh0w1RXCAPcr7O9fYHK1yeUr8c9Kb8PlkV9Vo1p7nh1abtxOAW55Z9PfO1k7Z8B5LYMbV2OKcC0b3PPEQXbaSwjKwJxokiqQvUsnJsXPZvc44K7SK0kiaOOyhbzt-Up3q3mxY_B7X102S-hnnlzNa3ZbKOqokozC2KMZBc-FpgYqgftpqd-35eO_aIQhGk7Q2SEvor3w0uRAkLnS-Qa9l6UX1HXo9lcWV5PsMhdW2NV7q8P9q5qntvvvyWGB9CtDkcrVctM6rC3aKvEYFuPDrh-CIv2EsavATDncrmX5RQR9mrdbHN76r6UxzrDlXZcV8Bmldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله آشنا به جلیلی:
انتقام اول شد؛ نان و زندگی مردم چندم است؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/133061" target="_blank">📅 17:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133060">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwbLQBVjfpptnIg7URbz7gHUdvQrIfklYzdzbKpfGuTRS4o4SZuDVNuegmVtWNkxt83q1eHXcWDOirygho-20hGIVe7igYmvx1afCx3f7x664jSn9YnqBaDOLccRi7xNdl4Nhc2AqhFNjwr9zoeRKZo71H4hsz32hqY6wVx1NX1vgCRxgglPrar9yF6aTA3XVq-D5S1QKWY9opCOAWr6zsl9TqQe9Gs-dA23mx-iloifHYUvHwzhoIu0ksHLVijSHL5iHWRdBlj4GoVlgE5QJzRrAle8OQLoE47L00Bu0azSAjmzPylYbMgiXxEaSxXIUw8ci4IzAd3_G5gQBloa0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اولین تصویر از محل دفن علی خامنه‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/133060" target="_blank">📅 17:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133059">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc5b51f6d.mp4?token=luO0F9EIquuD6rCpJepeWyRNS8FwFP3un1RdbAVm_EA56fk-cLM49OPdCd8CuQXrSkfJJpZMwSBH63uFHh2fFVtNdp3BL7AIQFA0jLo46OqOZbfOeoEaLX98Euf1nO5FGjWaZ4DuhiApLepjvN5aHOXVzOS93CKnQSoMChYwUisRtSSJGUWP3S48CKlxHL80aFIQjw4YW1a4bHu9u9sUZoKuJR66E0VtovAoWsykAJ7DYj301Jr26yHXN4OhNjwHzJ6aa1AamkUcjQydzEnts6TJ0orRKGUlIDKNdZDSCpDiwkPEuuVt0RocnHtzOfq_q5KnbjRRD2OaBSRU9BgKTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc5b51f6d.mp4?token=luO0F9EIquuD6rCpJepeWyRNS8FwFP3un1RdbAVm_EA56fk-cLM49OPdCd8CuQXrSkfJJpZMwSBH63uFHh2fFVtNdp3BL7AIQFA0jLo46OqOZbfOeoEaLX98Euf1nO5FGjWaZ4DuhiApLepjvN5aHOXVzOS93CKnQSoMChYwUisRtSSJGUWP3S48CKlxHL80aFIQjw4YW1a4bHu9u9sUZoKuJR66E0VtovAoWsykAJ7DYj301Jr26yHXN4OhNjwHzJ6aa1AamkUcjQydzEnts6TJ0orRKGUlIDKNdZDSCpDiwkPEuuVt0RocnHtzOfq_q5KnbjRRD2OaBSRU9BgKTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
افشاگری رضا جاودانی از علت کناره گیری خودش از مردان آهنین :
🔴
درگیری بسیار شدیدی میان همراهان شرکت‌کنندگان رخ میداد، به طوری که یه روز نیروهای ویژه دور تا دور محل مسابقه مستقر شده بودن و تعداد زیادی سلاح سرد و شمشیر ، قمه و چاقو از همراهان شرکت کنندگان مردان آهنین کشف شد، منم ترسیدم از اینکه این فضای خشن و خطرناک تو مسابقه وجود داره و دیگه کناره‌گیری کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/133059" target="_blank">📅 16:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133058">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4zo1Qy_GrPXM4FQvusYOH1Z9gw2LLAGLitWrY4icnA4srG7zKLH8caUkSzvzDEKpCYGZRMvyjjpy1oI8sUZNc5GCVUsHgzkrze-h3Nifvto27uQEzn_wd_rSvoIbBdzak6MV6Czaz8LTrEKid8r7aYf-meUaFC8nFjz_od6gdA3AHrZbFwqdDd-Lstss-I1cemuyi44yJ86OANJeTIi0UVHa7pUIEX1UDwXvO05CGwDTWU8Y4itGBLYZzFZKS0GcNfJZuCuiofIZLTau0nVVd8zUKUfDgtbGdgQYgfAmoX5gyp6w-X_kMKSdXeZJ3Vhpv-4ravCFvREODFMRFN64A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی ان ان: ترامپ نمی‌خواد اسرائیل تو حمله‌ها به ایران مشارکت کُنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/133058" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133057">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
تهدید آمریکا به انجام حملات احتمالی بیشتر علیه ایران
🔴
یک مقام آمریکایی امروز به سی‌ان‌ان گفت که واشنگتن فهرستی از اهداف در ایران را به عنوان اهرم فشار علیه تهران حفظ می‌کند.
🔴
وی در این‌باره مدعی شد: «وضعیت [با ایران] متغیر است و در صورت لزوم، حملات ممکن است از سر گرفته شوند».
🔴
این مقام آمریکایی ادعا کرد: «واشنگتن عمداً حملات را متناوب انجام می‌دهد و سپس برای جلوگیری از تشدید تنش و دادن فرصت به دیپلماسی، آنها را متوقف می‌کند»
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/133057" target="_blank">📅 16:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133056">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP_UZAQc5q7f5syHe8An6zSw4NYH_SJtmzg8qLYcyuYVQIvQ-A2LiVLUOkgCFraZC43UUyffXOzB39VkIL4xWFDnpZrscNmshGnecV9WaZg20I2TTzD5yYLELBbK23Z9aknYMzFOyQRBj8bAD0QoqU5oMBVD7Yihy_vyq4RWY078FVSzwM1zHeMTLAgvtlsmampVYO1XGpOozz41edRsibIAiSKmv7JJ3tHcPXKozdKdbq9XZUz9ZVb8tf4wv9ECka38_GECUqy0Xp4DXJe6oKEKHD_XzxJvvSzQoJvrxkkZYRS3h4xjf0WQlcEq5-MSfxP6QQ5HNJyDHLeyLNKI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
فهم امثال ما از زمان فعلی بیشتره
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/133056" target="_blank">📅 16:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133055">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
رویترز:
مذاکره‌کنندگان قطری برای کاهش تنش و تلاش برای ازسرگیری مذاکرات در ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/133055" target="_blank">📅 15:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133054">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
هواشناسی: تو روزای آینده دمای جنوب به ۵۰درجه و تهران به ۴۰درجه میرسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/133054" target="_blank">📅 15:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133053">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
زیدآبادی: قلاده تندروها رو باید مهار کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/133053" target="_blank">📅 15:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133052">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
معاون وزیر آموزش و پرورش: دانش آموزها بجای کافه گردی برن درس بخونن
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/133052" target="_blank">📅 15:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133051">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kl2jEhS1NAr61jlipbtRsJ6stfDl2asCMBkNef9lm8OuATyqQ49oWnAe1GlUputNZCI5ID_MJVVy1QW7jSB3Ss62z5iA0irYIV2a8E5JJrfa15cyoQzjDSA1bOx8BecedlzQi-T1Dp1bV26rUboqDagTTs7p3-WeaJcaV6RWfRVFTklEB77-Bv2GhF6nZOazK1LYP5n-L0dtPP9ktq2AE-CUERTqqsx86CjzdhudGP7h_mDnfFkC-ZcpGEqWYipogRVP8pudxZJlDYpbgcnY2nuP8g0KvGGUIvhPbd96lAh06KDNPBUQBGWBUv65gB7O7gpKSWFipNGLi6VBvf2zTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیلی:
برخی می‌گویند ما باید اموال ایران را آزاد کنیم؛ بزرگ‌ترین دارایی ملت ما رهبری عزیزش بود و باید انتقامش را بگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/133051" target="_blank">📅 15:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133050">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5c47f340.mp4?token=md5LuruiJS83sHUS9_6kJ3bLMKLi3EJJvKAGBRoi99LJuR_P_e7EtDO68WlYRneJLpxXztRuvvsafJ9McyCYAekUCL23bLgQPXAIylPs2yLlSqw8rQ1gWDquO3EEWhR2_Owl23cPANSBEYElCC27NJn1BchGQWxuvUtkeCN7PqQcRSSWmHYz2fm4Ns8TOr4ZsorKzmSV-KW0_gko5Bm9kKmlc76uEx6zu_6V8bDH5Rd5nRwyFzedxo2Xkj0Sy8ZH956rZWEOHb4aCh-TVAkexMSRG7DaupVysAiyjNIvxkUvvD0A7coUHTWr-vmrMJElH_f7WTyMn2qpdHyXbVaHJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5c47f340.mp4?token=md5LuruiJS83sHUS9_6kJ3bLMKLi3EJJvKAGBRoi99LJuR_P_e7EtDO68WlYRneJLpxXztRuvvsafJ9McyCYAekUCL23bLgQPXAIylPs2yLlSqw8rQ1gWDquO3EEWhR2_Owl23cPANSBEYElCC27NJn1BchGQWxuvUtkeCN7PqQcRSSWmHYz2fm4Ns8TOr4ZsorKzmSV-KW0_gko5Bm9kKmlc76uEx6zu_6V8bDH5Rd5nRwyFzedxo2Xkj0Sy8ZH956rZWEOHb4aCh-TVAkexMSRG7DaupVysAiyjNIvxkUvvD0A7coUHTWr-vmrMJElH_f7WTyMn2qpdHyXbVaHJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی مراسم تشییع آقای خامنه‌ای، یکی از حامیان حکومت سعی داشت مثل اسپایدرمن، جلوی ماشینی که تابوب خامنه‌ای رو حمل میکرد، بگیره اما موفق نشد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/133050" target="_blank">📅 15:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133049">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d349e1e2a.mp4?token=dYpW7-9YiG9PqmUEw8-bx03HHvi4mV85Y95wd_7UdOJVChHR9m-mrQ4J6jY_mEfCI0MZ6xP58m7q-JOg39I5QvtlVfoOAdY0cCZa_XjmeYBc3U6Pj1yfGDVsOP2N7HdwNhMIxbrXpks905gmSKntxHPH1mrFkI-DzcQk-uBKDgW3MTDaYxgT7nfay7B4npaWM3tqY3ow3qnEq7zq4vOk3pCPXqs15sbGYGjM9Hqz79L1i3qn_OespzCGR1eoF1FwmxBpQhlMzLNm24yITUK1K1yfAq9GtWFYwFqEakNBhEW5seEbxrO2p0b_lSQ4vJzDeBa4C09pfWzxhkh5UPnNiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d349e1e2a.mp4?token=dYpW7-9YiG9PqmUEw8-bx03HHvi4mV85Y95wd_7UdOJVChHR9m-mrQ4J6jY_mEfCI0MZ6xP58m7q-JOg39I5QvtlVfoOAdY0cCZa_XjmeYBc3U6Pj1yfGDVsOP2N7HdwNhMIxbrXpks905gmSKntxHPH1mrFkI-DzcQk-uBKDgW3MTDaYxgT7nfay7B4npaWM3tqY3ow3qnEq7zq4vOk3pCPXqs15sbGYGjM9Hqz79L1i3qn_OespzCGR1eoF1FwmxBpQhlMzLNm24yITUK1K1yfAq9GtWFYwFqEakNBhEW5seEbxrO2p0b_lSQ4vJzDeBa4C09pfWzxhkh5UPnNiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سید علی خامنه‌ای، ۲۲ مرداد ۱۳۹۷ :
به طور خلاصه در دو کلمه به ملت ایران بگم : جنگ نخواهد شد و مذاکره نخواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/133049" target="_blank">📅 15:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133048">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTs0TONOiKNC2nqyjorjYr2OYJ_6MRTW7oqTl7-a122JZrOZR9PKDgdceFBtxSy0JgMG6urxuuNzC5O0tfYcb_xG0Bot2FykhADfDg37M7rLAdaJ-ln-HcxC4UMczMisojB-LiPSdqgW6B6qw9fwhYTH-gbqu5Xoh8Ny-uUWtmo2paVklTnV4wurMSovPUXLqsyRJtx6cttkvgkuquxGbPJYmTsrR8HgpRsUCIysQCIcRNehqIwEkJE9tKe5xDoNkggN9A3Cvx7Md_Blgswj6FSULT4XoC9lrZ5SbiAK8AbPlRRGivt5Vdlgo2ymzNnGNaFnde9VXzTcCKYEDc9zxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیر شورای‌عالی امنیت ملی: با حمله به زیرساخت‌ها مقابله‌به‌مثل خواهد شد و رژیم تبهکار صهیونی هم از پاسخ رزمندگان در امان نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/133048" target="_blank">📅 15:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133047">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
به گزارش بلومبرگ، اتحادیه اروپا در آستانه توافقی است که به اوکراین اجازه می‌دهد از بخشی از وام ۶۰ میلیارد یورویی اتحادیه اروپا در زمینه دفاع، برای خرید سلاح از شرکت‌های بریتانیایی استفاده کند.
🔴
احتمالاً این خبر طی چند روز آینده، و احتمالاً از روز دوشنبه، در جریان جلسه ائتلاف کشورهای داوطلب به رهبری بریتانیا و فرانسه در پاریس اعلام خواهد شد.
🔴
بر اساس این طرح پیشنهادی، بریتانیا هیچ هزینه ثابتی را به عنوان حق دسترسی پرداخت نخواهد کرد. در عوض، لندن کمک‌های مالی را بر اساس ارزش قراردادهایی که به شرکت‌های دفاعی بریتانیایی از طریق این برنامه وام اعطا می‌شود، ارائه خواهد داد.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/133047" target="_blank">📅 14:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133046">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44c5dfe512.mp4?token=Y4LJV-zcyfctykinHNHziXWhCGJKaliXOW8HcK-7afxov1DTY22kVo7gJiRHyA48o5jSCKFnmHLoOFtHtucQSqpPE-v61_Mo3MvF9Av4tLa2NSUL6rNT_VqFVHHT93P9z1UkMad5PnH_cOGFlJI1uPmegxvYK2GXpSlHezC72hmH9FjA4Xu9FNXBeB_Ak8JpfU0GPhA8ZQz5eGqrtspCbfRUckdYUNjEg87LZAuPWjgI3CLiI92rsCwKf6X-vvP-RTGIyJzECWBmjgTEIzAd_J8lKcsuZWly0_Fz7Rk7M7Ye9ZNwTPUAYvfBdcaHmsDM_-Z2nY9iFwweIqBuId2Wog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44c5dfe512.mp4?token=Y4LJV-zcyfctykinHNHziXWhCGJKaliXOW8HcK-7afxov1DTY22kVo7gJiRHyA48o5jSCKFnmHLoOFtHtucQSqpPE-v61_Mo3MvF9Av4tLa2NSUL6rNT_VqFVHHT93P9z1UkMad5PnH_cOGFlJI1uPmegxvYK2GXpSlHezC72hmH9FjA4Xu9FNXBeB_Ak8JpfU0GPhA8ZQz5eGqrtspCbfRUckdYUNjEg87LZAuPWjgI3CLiI92rsCwKf6X-vvP-RTGIyJzECWBmjgTEIzAd_J8lKcsuZWly0_Fz7Rk7M7Ye9ZNwTPUAYvfBdcaHmsDM_-Z2nY9iFwweIqBuId2Wog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیروز تو پرواز یونان به آلمان، یکی از پنجره های هواپیما کنده شده و یکی از مسافرا تا ناحیه شانه از پنجره به بیرون کشیده شده!
🔴
همسرش حدود پنج دقیقه با گرفتن پاهای او مانع از بیرون افتادن کامل وی شد تا بالاخره نجاتش دادن و هواپیما هم فرود اومد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/133046" target="_blank">📅 14:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133045">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
به‌گزارش یسرائیل هیوم، دونالد ترامپ به‌دلیل نگرانی از کاهش شدید محبوبیت خود در آستانه انتخابات میان‌دوره‌ای، قصد ندارد جنگ با ایران را ازسر بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/133045" target="_blank">📅 14:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133044">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
به گزارش نشریه "بِیلد"، سرمایه‌گذاران قطری، مانع از مشارکت پیشنهادی شرکت فولکس‌واگن با شرکت "رافائل" اسرائیل برای تولید قطعات سیستم دفاع موشکی "گنبد آهنین" در کارخانه "اُسنابروِک" این شرکت شده‌اند.
🔴
شرکت فولکس‌واگن در اواخر ماه آوریل، یک توافقنامه اولیه با این شرکت دفاعی دولتی اسرائیلی امضا کرد، به عنوان بخشی از برنامه‌هایی برای بازسازی این کارخانه که با مشکلات مواجه بود. با این حال، "صندوق سرمایه‌گذاری قطر" (QIA) که ۱۰.۴ درصد از سهام فولکس‌واگن را در اختیار دارد و ۱۷ درصد از حق رای شرکت را کنترل می‌کند، با این توافق مخالفت کرده است و دلیل آن، روابط پرتنش بین قطر و اسرائیل است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/133044" target="_blank">📅 14:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133043">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8H0lcrUakxNmtUNSdPohYVC7G0TQWZTCXPsdscCz_AuqEyq083jT5_OGt48QnDSXekBYSTF95J7NILVs7Y1UE6qxbsyajCt58iwwy04qAQ7LjofzFPi1sxzcWtv8_K8v86lRatOxxBD4rHrnamwgt20-0AzG7kLc1uX_9i-5n5qJMYLhQzHV0aUPH-tnt4hyD66WZ6ot_MNPxhadtpiq1LfRBCbAHkitVR-yKa9rhZ3tbIC9eDMBCMwu6xMbOYqPvLCDbRlPA8bjvxkvLIIQm5EmlTRayzIsiEvuw3FZ0aSeH8kiITUaQH9nwRywcBH_Hivwpxqrq3cavF23_m8tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو: تصویری شیطانی از من ساخته‌اند که سزاوارش نیستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/133043" target="_blank">📅 14:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133042">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوری / سی‌ان‌ان به نقل از مقامات آمریکایی: گزارش اسرائیل درباره طرح ایرانی برای ترور ترامپ ممکن است تلاشی برای وادار کردن او به تشدید تنش‌ها باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/133042" target="_blank">📅 14:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133041">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۴.۳ ریشتر کهنوج در استان کرمان را لرزاند.
🔴
در ساعت ۱۰ و ۵۹ دقیقه امروز جمعه ۱۹ تیرماه زمین‌لرزه‌ای به بزرگی ۴.۳ ریشتر کهنوج در جنوب استان را لرزاند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/133041" target="_blank">📅 14:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133040">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
طبق داده‌های انجمن اتومبیل آمریکا (AAA)، میانگین قیمت هر گالن (۳.۷۹ لیتر) بنزین در آمریکا در بحبوحه تشدید جدید تنش ها در خاورمیانه، پنج سنت افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/133040" target="_blank">📅 14:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133039">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
شورای عالی قضایی عراق: روند پیگرد مفسدان مالی و اداری و بازگرداندن اموال دولت را دنبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/133039" target="_blank">📅 14:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133038">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
خبرنگار الجزیره گزارش داده است که یک پهپاد اسرائیلی به خودرویی در شهر کفررمان در منطقه نبطیه در جنوب لبنان حمله کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/133038" target="_blank">📅 14:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133037">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
رئیس کمیسیون امورداخلی کشور: تنگه هرمز به شرایط قبل جنگ رمضان باز نخواهد گشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/133037" target="_blank">📅 14:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133036">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
نخست‌وزیر کره شمالی به چین سفر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/133036" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133035">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93d1fc7f0e.mp4?token=mYBTFE8WYW0PuzUhIAKYKzy49zSzJJcBgD6PyiFrwtdp_r8ZQNMd7IUyu6eBoBDSc98Oinna9IXhFUn6X5dWGY-NLbomUSRH7iu6XgW7JXkEdn-6FU9XoVYEhHdx4Bd4Y8wuD6qRhEAD6cRwPGW3qRneg9admV1OmB2eC-bgdHpSr8bYPQzuC0fH6MelE6PtcQH60aU0yEkdqsOiVTuUp0MxmR7QT8dP_htAhkhvwKVym_8MNvsgkS3mXCFNR4dXb16ud2L9baTQYyxCkbtDaGs-FRLcCpcyduOF2N34RGKe1jzHDfPlFMvRooT0ZQrAHQYrJXqPQE56h1EBiu6CUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93d1fc7f0e.mp4?token=mYBTFE8WYW0PuzUhIAKYKzy49zSzJJcBgD6PyiFrwtdp_r8ZQNMd7IUyu6eBoBDSc98Oinna9IXhFUn6X5dWGY-NLbomUSRH7iu6XgW7JXkEdn-6FU9XoVYEhHdx4Bd4Y8wuD6qRhEAD6cRwPGW3qRneg9admV1OmB2eC-bgdHpSr8bYPQzuC0fH6MelE6PtcQH60aU0yEkdqsOiVTuUp0MxmR7QT8dP_htAhkhvwKVym_8MNvsgkS3mXCFNR4dXb16ud2L9baTQYyxCkbtDaGs-FRLcCpcyduOF2N34RGKe1jzHDfPlFMvRooT0ZQrAHQYrJXqPQE56h1EBiu6CUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله یک مداح به قالیباف:
بی غیرت، بی شرف، عمرسعد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/133035" target="_blank">📅 14:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133034">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔔
تبلیغات قفل ربات الونیوز
هفتگی 250$
میزان جذب: 30kالی40k باکیفیت
سفارش دایرکت</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/133034" target="_blank">📅 14:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133032">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
بلومبرگ: مذاکرات فنی بین آمریکا و ایران در مورد توافق صلح دائمی ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/133032" target="_blank">📅 14:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133031">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHa0diNEvQq6Tz5R57Fytm1a0ZQWDdCBJSctqHomfyb2Ie29szzNd41Udp8KYBGjXbi4MfeCYEwEOgLpAWXfuyydc47HsL2BCd1SB2UgEX4MvAkss-AOn-g3AkWaisXwvldtskrhjW7I83CTkRAXRIH5j7bMQ_Zfirvny_P6isbAHVqjLa7nm1z_yovaFdNykhtu-ZM1omuCOGOPlPNlBwrCBpaNCTQwY1bwIuhixrlReSF0iJg6t5xVxjhr9F-5Tfjm7-N6dviJx7-11AqdNZNSBheENVOsLRFgn-IzIEZtV2OyeLrsI24T4yvFPEhQMI2awhNjk4ylRIeERv2wJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارزش یک میلیون تومن در طول سال های مختلف
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/133031" target="_blank">📅 14:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133030">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترکیه اس-۴۰۰های روسیه را به کشورهای خلیج فارس فروخت
🔴
یک روزنامه نزدیک به دولت ترکیه گزارش داده که آنکارا سامانه‌های پدافند هوایی اس-۴۰۰ خریداری‌شده از روسیه را به یکی از کشورهای حاشیه خلیج فارس واگذار کرده تا راه را برای دریافت جنگنده‌های اف-۳۵ از آمریکا…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/133030" target="_blank">📅 14:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133029">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
رویترز: پوتین آتش جنگ علیه اوکراین را شعله‌ورتر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/133029" target="_blank">📅 14:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133028">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
روز گذشته نیز ارتش اوکراین دست‌کم 10 کشتی تجاری روسیه از جمله 7 نفتکش را مورد اصابت موفقیت‌آمیز قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/133028" target="_blank">📅 14:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133027">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
عملیات دریایی بریتانیا: سطح تهدید امنیتی دریایی در تنگه هرمز همچنان در بالاترین سطح خود قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/133027" target="_blank">📅 13:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133026">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
کاخ کرملین اعلام کرد که ولادیمیر پوتین، رئیس‌جمهور روسیه، تا کنون با دونالد ترامپ، رئیس‌جمهور ایالات متحده، تماس نگرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/133026" target="_blank">📅 13:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133025">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkiuCCuHfM9Hp0TvwQK6w1yqScRu1yAknShIioAWhSzEuZtbzyi4K_CyDhOAfD3mUhFD39VFGGq154PthEE9AwZgoMuBk1qnuTnFXDb4Fd6a_CLFz9l8IgUCums_ZuYzK5gmRLidTSbgUsZJZ_8IK_7H3ESeWjCMi6XkKKAd-lfQye6eUoXBBb4eUHQWk1MMXomp6vGHOecoN_El1P3Ejkd31NQmUTzTi0-suuBUrK94szGQaDcK5SqH4p9DWueRYbfRJtiY5-PLm9kF6Xy8U0bKG64N26gQoNVHUoQRND_YSzqOLv27k7HQgYAf1xY_8Gbg-YNzZ4oBM2J59eEDEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قائم پناه، معاون پزشکیان: بعضی مداح‌ها یه میکروفون بهشون رسیده هرچی دلشون میخواد میگن
🔴
اونا هیچی نیستن اما جو گرفتشون و فکر میکنن تئوریسین دین و سیاستن
#مداح_بیسواد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/133025" target="_blank">📅 13:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133024">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
گویا فرمانده نیروی دریایی سپاه به دلیل حملات به کشتی‌ها، توسط شورای عالی امنیت ملی توبیخ شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/133024" target="_blank">📅 13:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133022">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری/اکسیوس:  ایران و آمریکا از طریق میانجی‌ها توافق کردن فعلاً به همدیگه حمله نکنن و برای حل اختلاف‌هاشون، به‌خصوص درباره تنگه هرمز، دوباره پای میز مذاکره برن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/133022" target="_blank">📅 13:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133021">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aONlm2Em96GFrmyQlJ7XMyliKp8a0Xy8O1eo100L8oiKIwW_ZbWNMdHKmHnawWkHEqKZ3x2nk6UyRO4q-P4RDG08qpGw0d3PrGSW7GoFqcLGy9L-mjAHWVpU2KHh-QZ7mvFWrL10wEvVx58x3XNRJMzJOq7gUkYDe0Tx19yJKxo_VGbKsVfws4By0PvbRGq2wFhdbTWKa5J1zGkykU2S6m1mE2ds8ANHNOg-N_T1Lrq4uvitwH81uRkqzD0LFtyPthHuMsY9zHyK-MPiPCjG6MnIrhc3vTzgCvzRrw0jwmD7EuEZuZKswY_XNxOhEfw9OKCxiphKEgDw7l9HtWmB-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: یه انتقام مشتی از ترامپ تو راهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/133021" target="_blank">📅 13:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133020">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
مدیرکل هواشناسی خوزستان گفت: تا پایان هفته آینده روند افزایش دما در استان پیش‌بینی می‌شود به‌طوری که از روز دوشنبه وقوع دماهای ۴۹ درجه و بالاتر در اغلب نقاط استان مورد انتظار است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/133020" target="_blank">📅 13:29 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
