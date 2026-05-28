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
<img src="https://cdn4.telesco.pe/file/UwLzxKDyoMrIOnWuiH6GcBpUqBQku_jGqESgnVuqkzRQWu3kigKogRhVKLA83Q9rHBia1IqP8gn0be_3gDfRdz4AVOO4WFLvCo0N9xjz_WcYz6QiQPa5nyrkGlrDz-8ccOcw0mn9Yz-qs60ZF3bfOUclx8LQVaSP5T3x5KcJm98j1iUBtqiPK6VOMatDlTSlehoIDwoqnrITd0z41n7g3sJOoaW_3P_-4bRUR0tU4Oya6meGHZ8DQDOdYbUQk8kg3-k4e5IOfK64Qw4u4CRDCYseS1NktARFuv71mWJfyvBJtGkUZUjNeQluKxhrceLluvrIzN0tbT_oydoAfVFShA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 40.8K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 01:45:09</div>
<hr>

<div class="tg-post" id="msg-8648">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/IranProxyV2/8648" target="_blank">📅 23:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8647">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺(4).ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8647" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👑
کانفیگ OpenVPN-VIP
🌐
📶
آیپی ثابت بدون نشتی DNS
🇵🇪
🛡
متصل برای مخابرات و یکسری وای‌فای‌ها(منطقه‌ای)
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/IranProxyV2/8647" target="_blank">📅 18:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8646">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">درحال بررسی و آپدیت جدیدی برای سرورا هستم، کمی طول میکشه ولی سوپرایزی در راهه
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/IranProxyV2/8646" target="_blank">📅 18:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8645">
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
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/IranProxyV2/8645" target="_blank">📅 18:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8644">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔻
نتانیاهو: ما باید ماموریت در ایران را تکمیل کنیم و من تقریباً هر روز در این مورد با ترامپ صحبت می‌ کنم./الجزیره
✅
با ما اخبار جنگی بروز باشید  @russiamilitery</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/IranProxyV2/8644" target="_blank">📅 17:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8641">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
سنتکام: حمله ایران به کویت با موشک بالستیک نقض آشکار و فاحش آتش بس بود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/IranProxyV2/8641" target="_blank">📅 14:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8634">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Openvpn.ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8634" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📍
کانفیگ برنامه Open VPN Connect
Password:
@KurdConfing
🌐
تمامی نت‌ها
📲
اندروید و ios
❗️
اگه وصل نشد چندبار retry بزنید حل میشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/IranProxyV2/8634" target="_blank">📅 14:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8633">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ایفونی های عزیز جامپ جامپ استفاده نکنید اپل ایدیم لاک شده سر این فیلتر فیلتر دیگ استفاده کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/IranProxyV2/8633" target="_blank">📅 13:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8630">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Openvpn.ovpn</div>
  <div class="tg-doc-extra">54.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8630" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟠
open vpn
🛜
برای ایرانسل رایتل مخابرات چک کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/IranProxyV2/8630" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8629">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دیشب آمریکا به بندر عباس حمله کرد ایرانم در جواب به کویت حمله کرد اما هنوز اتش بس نقض نشده
به این میگن یه توافق درست حسابی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/IranProxyV2/8629" target="_blank">📅 13:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8628">
<div class="tg-post-header">📌 پیام #90</div>
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
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/IranProxyV2/8628" target="_blank">📅 13:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8627">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URlFkNWWtrUUJsGahrMtb-Coqq7kTCN-F4Om3t0ug5w5Anj8fH9dcN6b4b0OMndMzOzAGv8X1x7KH_wP-WWPYhWARLvxnwxHMSCjBvGyeCcRWKdkKqN--soY_2zN8m5JZyftU0CozEpCTCrZBIx7NW95FqTHJ6WlYhLqFvxzcc5UwJXFE6fIX7burgPD_JoePT3SRK72HgkKvaGLMecFgQcnlM2_Te2_QAHhwetq4-8begdFh8qY4Kr9ttC97nNfWxJw4xGbEIHaL9NAtEw5JhURbiMMt-uiR9WCTN5LXb4RNo4xEEsoNFOIgj6ZLHVLGulfxDHMTOlJNX03qXdFNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آخرین آپدیت از وضعیت اتصال اپراتورها به اینترنت بین‌الملل!
+ طبق این لیست ، ایرانسل با 38 درصد بالاترین اتصال رو به نت بین‌الملل داره و باقی اپراتور ها و شرکت ها همگی زیر 30 درصد اتصال دارن!
++ یعنی اگه اینترنت رو مثل یه دریچه در نظر بگیریم ، الان فقط به اندازه رد شدن هوا این دریچه باز شده!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/IranProxyV2/8627" target="_blank">📅 12:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8626">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGSAtsfk77LdRwRInQwJwn4QThHbw6eGOjVpVyqGPKG5u-SLkGJLZ7Ht8dI6PZvVr_DkJ28TjLzM2aqfHHXK55df_h4kQxAuZlvA9rY_xS51t26Rl_TptWdnjAdb6Rrc-dZcNtc593fuiphWUAEIwEt1hmdom4fWBWI4s0lk_qg2JSShCCzk0k5yMk1BCuMhyS6_RiOwde5Qk0vVZK64qdwaNfQRyILLsdM-03HBdgkFTDzyTaW3l0wrTjm4g2Hgq1S86GEobP6x3YR_owBHEVuZrq42AD7QUWPqpimpNt7yGLJQdYnviJ7r41gD8kNPKBql_fQyt2OSjGx-yx0HoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍽
فعلا درحال حاضر تونستم تانل جدیدی بزنم رو دیتاسنتر جدیدی که پیدا کردم و تهیه کردم براتون از خارج کشور پینگ میده، با قیمت مناسب و پینگ بینظیر، باز مجدد اگه سطح دسترسی ها افزایش یافت تانل های جدیدی با قیمت هایی پایینتری براتون موجود میکنم حتما،نگران هیچ موضوعی نباشید تا آخرین مگابایت مصرفیتون پشتیبانی انجام خواهد شد
👀
🔐
1GB
➡️
60T
💥
◀️
جهت ثبت سفارش میتونید از ربات اقدام کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/IranProxyV2/8626" target="_blank">📅 11:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8625">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🟢
پروکسی متصل با سرعت خوب
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ%3D%3D
https://t.me/proxy?server=tg.capycore.ru&port=443&secret=27ebe852539fb8ec5f327c73262bb721
https://t.me/proxy?server=87.248.129.129&port=15&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d
برای اتصال به پروکسی ها حدود 10 ثانیه صبر کنید
⚪️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/IranProxyV2/8625" target="_blank">📅 10:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8624">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">vless://f172c28c-14f7-408b-b41e-838f4f32a15f@185.143.234.122:2082?path=%2F&security=none&encryption=none&host=tl2.axepart.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
وصله دوستان استفاده کنید
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/IranProxyV2/8624" target="_blank">📅 09:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8623">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/IranProxyV2/8623" target="_blank">📅 09:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8622">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">❤️‍🔥VIP❤️‍🔥.npvt</div>
  <div class="tg-doc-extra">3.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8622" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/IranProxyV2/8622" target="_blank">📅 08:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8621">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺(3).ovpn</div>
  <div class="tg-doc-extra">5.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8621" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/IranProxyV2/8621" target="_blank">📅 03:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8620">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/IranProxyV2/8620" target="_blank">📅 03:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8618">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
یکی از دلایل اصلی اختلال و کندی شدید اینترنت، سقوط سهم IPv6 در شبکه ایرانه؛ سهمی که از حدود ۱۲٪ به فقط ۰.۱٪ رسیده.
این افت باعث شده فشار شدیدی روی IPv4 بیفته و نتیجه‌اش رو حالا کاربران به شکل اینترنت ناپایدار، اختلال VPNها، ضعف شبکه موبایل و لگ شدید در بازی‌های آنلاین می‌بینن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/IranProxyV2/8618" target="_blank">📅 02:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8617">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
⚠️
گزارش‌های اولیه حاکی از آن است که ایالات متحده یک عملیات دفاعی را در بندرعباس ایران انجام داده است
.
🔴
یک مقام آمریکایی گفت: «ایالات متحده برای حفاظت از منافع منطقه‌ای خود اقدام خواهد کرد و این بر آتش‌بس تأثیر نمی‌گذارد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/IranProxyV2/8617" target="_blank">📅 02:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8616">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⭕️
خبرگذاری فارس صدای انفجار رو تایید کرد
🔴
شنیده‌شدن صدای ۳ انفجار از شرق بندرعباس
🔹
حوالی ساعت ۱:۳۰ بامداد صدای ۳ انفجار از شرق شهر بندرعباس شنیده شد.
🔹
هنوز محل دقیق و منشأ این صداها مشخص نیست و پیگیری‌ها برای مشخص شدن آن ادامه دارد.
🔹
همزمان برای دقایقی پدافند شهر بندرعباس نیز فعال شد.
🔸
طی ۴ روز اخیر نیروهای مسلح کشورمان یک پهپاد آر کیو ۹ و یک پهپاد اوربیتر‌ دشمن آمریکایی صهیونی را در منطقۀ هرمزگان منهدم و همچنین سامانه‌های پدافندی نیز یک اف ۳۵ و یک پهپاد آر کیو ۴ را نیز رهگیری کردند.
📝
اخبار تکمیلی متعاقبا منتشر می‌شود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/IranProxyV2/8616" target="_blank">📅 02:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8615">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
مث اینکه بندر عبارسو میگن زدن و صدای جنگنده میاد
🧐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/IranProxyV2/8615" target="_blank">📅 02:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8614">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
مث اینکه بندر عبارسو میگن زدن و صدای جنگنده میاد
🧐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/IranProxyV2/8614" target="_blank">📅 02:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8613">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/IranProxyV2/8613" target="_blank">📅 01:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8609">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کافه پروکسی💥.ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8609" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اوپن ویپن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/IranProxyV2/8609" target="_blank">📅 00:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8607">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Openvpn.ovpn</div>
  <div class="tg-doc-extra">5.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8607" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ open vpn
🎀
آموزش اتصال:
⬇️
کانفیگ رو وارد برنامه کنین
بزنین روی connect
بعدش ۲ تا گزینه میاد بزنین روی continue
عشق کنین
🍒
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/IranProxyV2/8607" target="_blank">📅 00:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8606">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkttAHrBReQXbbb-SMTpJ8JtJgB-lu4OxHpajKX3jGP4PSq_es9gA6PQu3hLpcolGOvhcS1PZJC1RHy53OOCKBwgLO9KgXhn0_hpdG08RVrBgMWAnC6U48M9tsfB7wxpu7QqHIaSHl3V0IVdlbgNCTfjld6SOVvwzyLNs9_t59mT6cdReENmelmMos7fYMC-Vgia8M9ALdul601H3DhqerXNtXxCsXAfyptshirQ2mwQyGR9kCQ4Wfx7tjX29vvN_-8HhwrwWUE9VQxQBvP3gKiiu45OUxqsPuk4r2z7BjEBkOyZQ07smUnQoPMbxa-tYRqbs3et2ZZ34NU2JPn5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت :
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/IranProxyV2/8606" target="_blank">📅 23:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8605">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/IranProxyV2/8605" target="_blank">📅 23:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8604">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اپ استور هم رفع فیلتر شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/IranProxyV2/8604" target="_blank">📅 23:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8603">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
گویا گوگل پلی تو اکثر مناطق وصل شده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/IranProxyV2/8603" target="_blank">📅 23:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8602">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/IranProxyV2/8602" target="_blank">📅 23:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8601">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/IranProxyV2/8601" target="_blank">📅 22:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8600">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/IranProxyV2/8600" target="_blank">📅 21:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8599">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/IranProxyV2/8599" target="_blank">📅 21:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8598">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/IranProxyV2/8598" target="_blank">📅 21:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8597">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/IranProxyV2/8597" target="_blank">📅 20:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8592">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/IranProxyV2/8592" target="_blank">📅 19:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8591">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
ترامپ درباره ایران:
آنها می‌گویند که بسیار تمایل دارند که به توافق برسند.
تا کنون به آن نرسیده‌اند. ما از این وضعیت راضی نیستیم، اما یا راضی خواهیم شد، یا اینکه باید کار را تمام کنیم.
آنها در حال مذاکره با جدیت بسیار کم هستند.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/IranProxyV2/8591" target="_blank">📅 19:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8590">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
ترامپ: ایران حتی اگه اورانیوم های خودشو هم تحویل بده هیچ خبری از کاهش و لغو تحریم ها نیست
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/IranProxyV2/8590" target="_blank">📅 19:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8589">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/IranProxyV2/8589" target="_blank">📅 19:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8588">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">https://t.me/proxy?server=87.248.129.129&port=15&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d
پروکسی متصل سرعت قوی
❤️‍🔥
⚡️
👀
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/IranProxyV2/8588" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8587">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اینترنت بین الملل در حال قطع؟
نت‌بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPN ها هستند. کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPN ها می‌باشد.
تندروها کار خودشونو کردن واسه همینه خیلیا نمیتونن وصل شن یا سرعت افتضاحه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/IranProxyV2/8587" target="_blank">📅 19:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8586">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ha8B7FQYt7bxpjmhL8swhKC0YtydL4MUcsNTqopLve918N9lgCp0Xcvsl-HSl0LPpNU2DZdhP60MBSMXc1IY9uHKlDPnKBzyoZA68LG4P9pYCq06-3ZxNLcyzHA92D0zUqYNDLYL5oMBz8uY68sHTuoy2SgmwZh62LP8FHLchMwLpqLgQw7UA57KCoPzBkjDt8gbR7kYiUA9OCBS3dJJ3P80DHDQRsB9Hj2PYeDh0vuuD6I16UFTLmUnTmCFzNTv9NvIuZTCI4OO5sRNVe1BJJAbBIOE3xRVE_hsJ-6tZhKRm5MTWAsbbqpQrcrp9GJRWIzllQjaGnmw0Aeoj-kLXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که سفارش ثبت کردید تو ربات، دارم یسری آپدیت رو سرورا میدم، صبور باشید، اوکی شد همینجا اطلاع میدم و سفارشتونم تایید میکنم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/IranProxyV2/8586" target="_blank">📅 18:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8585">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/IranProxyV2/8585" target="_blank">📅 16:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8584">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/IranProxyV2/8584" target="_blank">📅 15:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8583">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">vless://406d8436-0eb9-4eb2-84fb-960e076ffba6@162.159.38.183:2083?mode=stream-one&path=%2Fde&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=de.lezzatzone.ir&fp=chrome&type=xhttp&allowInsecure=0&sni=de.lezzatzone.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
همراه اول تست زدم، اوکی بود، مابقی نت هارو خودتون تست بزنید
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/IranProxyV2/8583" target="_blank">📅 15:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8582">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZy3qeB9APgRIg0MtPHmt5WPAME8l9VTqL8nHTqxozKrqB4m9ZV1TULqQstqo-dbiN_JrlCsJr5i1s96MlJ_SDFC4Sv-_pl3-TEMo_L6T4HYfJzzOienIwOvjRvgu-zGc3HA9ui1Py6ucKhioEoa5gkkQaDa7A0vekoss-avZnXzD838hnvVhh7kyCPuiXzi2Mfn7P5DAg15GzHRpqqW6i37S9QhHYXcOaZNTYVIqx0qDt8vsYJYaI45w4084TX87SJtZXRfPxCgjwiAxRlZ9UXdA9Qx0aPvlHNa_Rol6e3CaPk6aNdAmMYAkVMfEHraaCH_kFzvu6D4kFY_QPD_dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همراه اول بعد از اعتراض کسانی که اینترنت  پرو خریدن و گیگی 40 هزارتومن بابتش پول دادن اعلام کرد در صورت تمایل میتونن  اینترنت خودشونو به حالت قبل برگردونن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/IranProxyV2/8582" target="_blank">📅 15:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8581">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hcU1aulaqljoJUXUGx52CrZhbXiMEXUNoe0wdoxFBqSXwKrzMbdEGsZJ4ebmyu78iVBQgMl9vhm_Vorw7SvpeP-JvscNlT05fmjByjim0WOToWaqvTV3yjZ5DD1WMRK9dbcBTddKp3OcKpCmc3oCM-Ci4geeV3_13TO2q5pdlF538CcS0PgRYFXluzsMxTNtAFiesAly7Cm92jUeGlEeVlxI9sS8cowJvrOxAGVqZ0WwLZbuH9Ng6WjgQHr2mBAfB_nFrvQZvmwQuldrHTT2be4PRWiiOHeOD_YU9W9JMbssm_CaCEvE7JpYgjIu3JtcsqJW3tJ4dMOMUzkG0rAFOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آخوند حمید رسایی: از وقتی اینترنت وصل شده قلبم درد گرفته، یه لحظه‌ام نتونستم بخوابم
.
وصل شدن اینترنت پایمال کردن خون رهبر شهیدمونه، با اینکار تن رهبری تو گور لرزید.
عوامل موساد باعث بازگشایی اینترنت شدن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/IranProxyV2/8581" target="_blank">📅 15:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8580">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">vless://406d8436-0eb9-4eb2-84fb-960e076ffba6@162.159.38.183:2083?encryption=none&type=xhttp&security=tls&path=%2Fde&host=de.lezzatzone.ir&mode=stream-one&sni=de.lezzatzone.ir&alpn=h2%2Chttp%2F1.1&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو همراه اول تست شده اوکیه
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/IranProxyV2/8580" target="_blank">📅 15:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8579">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/IranProxyV2/8579" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8578">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/IranProxyV2/8578" target="_blank">📅 13:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8577">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">vless://900ca7c5-6c69-4536-b0f8-efa4e3976016@51.79.89.68:443?security=&encryption=none&headerType=none&type=tcp#@V2rayngSeven
vless://ae0dd58e-e222-40bf-84ae-365a97532737@104.17.150.224:443?path=%2Falbum%2Fbt&security=tls&encryption=none&insecure=0&host=pagescm.freen15.cc.cd&type=ws&allowInsecure=0&sni=pagescm.freen15.cc.cd#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
وصله منطقه ای، تست بزنید کمی صبرکنید وصل میشه براتون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/IranProxyV2/8577" target="_blank">📅 12:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8576">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">Proxy
✅
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ%3D%3D
Proxy
✅
https://t.me/proxy?server=ui.geodns.info.&port=4455&secret=7nnjRIGHSb16xRkTAiDCXQk%3D
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/IranProxyV2/8576" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8575">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🟢
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/IranProxyV2/8575" target="_blank">📅 12:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8574">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🟢
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/IranProxyV2/8574" target="_blank">📅 12:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8566">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/IranProxyV2/8566" target="_blank">📅 12:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8565">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دوستانی که سفارش ثبت کردید تو ربات، دارم یسری آپدیت رو سرورا میدم، صبور باشید، اوکی شد همینجا اطلاع میدم و سفارشتونم تایید میکنم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/IranProxyV2/8565" target="_blank">📅 12:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8564">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">https://t.me/proxy?server=78.47.67.183&port=8443&secret=dd104462821249bd7ac519130220c25d09
این هم یه پروکسی دیگه، بدون فیلتر وصل بشین، فور کنید برای دوستاتون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/IranProxyV2/8564" target="_blank">📅 11:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8563">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/IranProxyV2/8563" target="_blank">📅 11:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8562">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/IranProxyV2/8562" target="_blank">📅 11:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8561">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oW__LcyaWm2fbsdMEFc6AM1bx3CG2eybaV3rLFjGqFGvvtBwwxbJk7MpKyqBdGcnpraJs4bT5EljCFb7O4m5cjJYgr08QWMH27PIBejlBFV3wmXsqhYEN90xCRFYvh60nbtpyyXw4O9QjXXZOefhw6mM4Qe6dYjTAmgCXwPtgg4Cr72H4PKiw6T35NHr6rbnjw7D323mQlecOE1t03Z-g1GY9yb7FWj7qjcy3huuZnkGDUm1M8mPcu5ccepxxVBkE1hYWpNe6KiFFs-m78hCb-l9P0mw465yfpdJMjWQQRzoZ6LgkIAWmyJ0_OOnQP2vfUyNrIt_UWrmFrsD47Bxyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">البته طبق داده‌های شرکت پایش اینترنت Kentik، که اطلاعات دقیقتری رو ارائه میده، میزان اتصال اینترنت کشور هنوز پایین هست و کماکان به وضعیت اینترنت قبل از دی ماه نرسیده.  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/IranProxyV2/8561" target="_blank">📅 11:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8560">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sE_zcjnRp9Nnn9mt7aXD7uZJqCT7FkkxVwpQyTIgNxgQOg6p0IbIp-CkUlnbXdK900YM0K0eQ0OrpWP0_d3duJLW-R6AQAvv3KyOX8khPSN48qxEy11gIpsrHHE9nukV8Do6syBiJkImk50bq5mizwoTtPtrfroxJuTQIpz0WeSC5vC59JKLq6zFgkgsn6bk-GtXWCzSJMMHiURZjWaoKseQTsG2_5aGMEDRPFerukA5DjFIlgP73t_t4yZluD4jtnyumrN0qFXX3uIMQh1BDAjV4iuqVG-62YXYWNunAgAR00ondCZn0ysKEsPPUqKEH68thoYSdUPhy6oIDLPZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/IranProxyV2/8560" target="_blank">📅 08:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8559">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 9K · <a href="https://t.me/IranProxyV2/8559" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8558">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROrhm12g9HM7Ik1frinWKSEsoPxrTAUSQIKkCy6-OxLauxuawMBsOHOA5CEBVjJ9vOQqgb-yKKQyObIFnj9T_ykcXAaSWnpSibpxRV5sdw60t__sTKPI8snmSBjyh6kXHoeNi95jhzEMo3aTRtMcHQlgsQeTOO-E3WWUgc45olBzyJNKbJNrE0lc_Nhrz5irw5xdkTNSQuarqtoXkAWtOWo2darHyK_H7aF6Cyk0wUTWOcvv5aJaiAN9S4s0q7ROMVsKVXSBRBI6G-q7zxyEJorB1MEltgLjqaqk41-uY7YRAY4239YunN9P7DcJjZlj8HKY5vwJEE-14u9QulD-iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رس
ایی: عوامل موساد دستور باز کردن اینترنت رو دادن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/IranProxyV2/8558" target="_blank">📅 08:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8557">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">https://t.me/proxy?server=ams1.tlgfast.com&port=443&secret=083fe0c452e2407d835537872f097c54
این پروکسی هم بدون فیلتر بزنید روش وصل میشه، استفاده کنید، فور کنید برا رفقاتون
❤️
😁
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/IranProxyV2/8557" target="_blank">📅 01:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8556">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/IranProxyV2/8556" target="_blank">📅 01:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8555">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
کارشناس صداسیما :
وصل شدن اینترنت متوقف میشه و دستور رییس جمهور اجرا نمیشه چون خلاف دیوان عالیه.
😐
😐
😐
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/IranProxyV2/8555" target="_blank">📅 01:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8554">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s43fbFbY7VR9MSbz2pv1bAhWYy3KVBuwhZYDWeyjBYHsIF2o4swqTl9PS0ZljYGFPUn3h55q_8qctNRMtQrEdznYuDqAxdxDPV_kM-gXR4atDtshqF1T161c2QyGcwysc8HcfhJ_P3EHt_iWChvFYqyCNaXNk-3vxxvWnGTqarvhCdYTdr3PRypUMqpLuTDv1VDz7xPuvCiVndRxDPQC97aV8jHrNnRGNx53O7rgHzJRm5gkdDOlNVXcakNGj6nnlGXCRijxraV5xOFN1IlzZj23cjfy1UI03fViTht4h9Jrwi-PbLZLFKPP76s-2iyHmu_mTqv9UHQp3uj-rBi6Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">البته طبق داده‌های شرکت پایش اینترنت Kentik، که اطلاعات دقیقتری رو ارائه میده، میزان اتصال اینترنت کشور هنوز پایین هست و کماکان به وضعیت اینترنت قبل از دی ماه نرسیده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/IranProxyV2/8554" target="_blank">📅 01:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8553">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@172.64.152.23:2096?encryption=none&type=ws&security=tls&path=%2F%3FTelegram%25F0%259F%2587%25A8%25F0%259F%2587%25B3%2540WangCai2%3D&host=sni.jpmj.dev&sni=sni.jpmj.dev&allowInsecure=1#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA…</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/IranProxyV2/8553" target="_blank">📅 00:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8552">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@172.64.152.23:2096?encryption=none&type=ws&security=tls&path=%2F%3FTelegram%25F0%259F%2587%25A8%25F0%259F%2587%25B3%2540WangCai2%3D&host=sni.jpmj.dev&sni=sni.jpmj.dev&allowInsecure=1#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
https://t.me/proxy?server=178.105.241.184&port=443&secret=99902e5742bd34a3f26434fadf88cde3
سرور وارد کنید، و بعد به پروکسی متصل بشید بصورت ترکیبی، رو همه اپراتور ها اوکیه، فور کنید دوستاتونم استفاده کنن
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/IranProxyV2/8552" target="_blank">📅 00:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8551">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📣
دوستان، سرعت جوریه که نت قطع بود، سرعت بهتر بود
😐
😂
📌
درضمن، اینکه سرعت سرورهای تانل ربات پایینه نگران نباشید، برای همه به همین صورته و اختلاله کلا تو کل کشور ، حل میشه ، ولی خب پایداره و وصله، خواستین تهیه کنید تو ربات سفارشتونو ثبت کنید
🏅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/IranProxyV2/8551" target="_blank">📅 23:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8550">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">https://t.me/proxy?server=ams1.tlgfast.com&port=443&secret=083fe0c452e2407d835537872f097c54
این پروکسی هم بدون فیلتر بزنید روش وصل میشه، استفاده کنید، فور کنید برا رفقاتون
❤️
😁
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/IranProxyV2/8550" target="_blank">📅 23:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8549">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">vless://b64ced11-143e-4ded-a985-a8de25461061@3.27.234.120:51808?security=reality&encryption=none&pbk=XHnwfyEySdx57QT_8P_7vDVFzdLHO4tO9BQOsHxxlEk&headerType=none&fp=firefox&type=tcp&flow=xtls-rprx-vision&sni=yahoo.com&sid=8810c789eea55c28#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
متصل به همه اپراتور ها، بفرستین واسه دوستاتون هم اونا وصل شن، هم از ما حمایت ریزی بشه
❤️
🍸
😁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/IranProxyV2/8549" target="_blank">📅 23:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8548">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">vless://28154b7e-afc2-449b-8a78-bf1eba31bd05@a.darafiq.ir:8880?path=%2F&security=none&encryption=none&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
متصل با همه اپراتور ها، فور نکنید حمایت نشه حلال نیستا
😁
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/IranProxyV2/8548" target="_blank">📅 23:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8547">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">۲ تا کانفیگ دیگ هم ساختم، رو یکی نباشین مختلف بزنید که سرعتشون نیاد پایین یا قطع نشن
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/IranProxyV2/8547" target="_blank">📅 23:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8546">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">vless://abe09a99-7346-4c5b-9476-16774c032ae7@104.16.89.120:443?path=%2FTelegram-%40IranianMinds&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=1&fp=chrome&type=ws&allowInsecure=1&sni=mcia.po2pco.top#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رایگان جدید رو همه اپراتور ها وصله، استفاده کنید بزنید، فور کنید برای دوستاتون چنلو داشته باشن، حمایتتتت
😁
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/IranProxyV2/8546" target="_blank">📅 22:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8545">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">vless://e8cbc051-e0ac-452d-9bd3-8ad46625573c@arvancloud.ir:8080?mode=auto&path=%2F&security=none&encryption=none&host=r.cafeplusstore.ir&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA  رو آرون کلاد هم براتون ساختم
😂
، این برا خودم سرعتش بهتره، تست بزنید،…</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/IranProxyV2/8545" target="_blank">📅 22:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8544">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">vless://e8cbc051-e0ac-452d-9bd3-8ad46625573c@arvancloud.ir:8080?mode=auto&path=%2F&security=none&encryption=none&host=r.cafeplusstore.ir&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA  رو آرون کلاد هم براتون ساختم
😂
، این برا خودم سرعتش بهتره، تست بزنید،…</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/IranProxyV2/8544" target="_blank">📅 21:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8543">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/495efbf3a1.mp4?token=AVEH2velnrOJrHIQJGNmhePCPn0zgyzjPs5Tmm6LKkqnM_c_PiwtdMa65ut6ztJNWwZVl4qfii7thwWEuxTQsEsKTC2L3tVllEl--kLK7EktuOn2fu7TQC7DNezAfXmAuVmiqlHsTOb5LQTSGdObzF6zkbkRT4SWB8MrmPeXSEQKYYi7O2DUh636tK99lnPmiWsFyX9nmIkyGFiZI0phAftSaPUCI-5fAvrfrFE2U6zpCJBBdcobt1GY93i9pxUFFa0ImIOj7W7UliFnQH-HnPOH7N9eI9sSakFV3uqYUf2xc3OfePcHXpMgh5lB993d8vQQ3y5AjI97vg2IG--3rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/495efbf3a1.mp4?token=AVEH2velnrOJrHIQJGNmhePCPn0zgyzjPs5Tmm6LKkqnM_c_PiwtdMa65ut6ztJNWwZVl4qfii7thwWEuxTQsEsKTC2L3tVllEl--kLK7EktuOn2fu7TQC7DNezAfXmAuVmiqlHsTOb5LQTSGdObzF6zkbkRT4SWB8MrmPeXSEQKYYi7O2DUh636tK99lnPmiWsFyX9nmIkyGFiZI0phAftSaPUCI-5fAvrfrFE2U6zpCJBBdcobt1GY93i9pxUFFa0ImIOj7W7UliFnQH-HnPOH7N9eI9sSakFV3uqYUf2xc3OfePcHXpMgh5lB993d8vQQ3y5AjI97vg2IG--3rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظ، خداحافظ
👋
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/IranProxyV2/8543" target="_blank">📅 21:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8542">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">vless://e8cbc051-e0ac-452d-9bd3-8ad46625573c@arvancloud.ir:8080?mode=auto&path=%2F&security=none&encryption=none&host=r.cafeplusstore.ir&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو آرون کلاد هم براتون ساختم
😂
، این برا خودم سرعتش بهتره، تست بزنید، خوشتون اومد فور کنید
🍸
😁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/IranProxyV2/8542" target="_blank">📅 21:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8541">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.7.70:2096?path=%2F&security=tls&encryption=none&insecure=1&host=sni.111000.indevs.in&type=ws&allowInsecure=1&sni=sni.111000.indevs.in#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
کانفیگ با پورت های متفاوت براتون میسازم، سعی کنید همرو تست کنید، ببینید با کدوم راحت تر هستین، حتما برای دوستاتونم بفرستید
✅
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/IranProxyV2/8541" target="_blank">📅 21:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8540">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">vless://406d8436-0eb9-4eb2-84fb-960e076ffba6@104.16.7.70:443?mode=stream-one&path=%2Fde&security=tls&encryption=none&insecure=0&fp=chrome&type=xhttp&allowInsecure=0&sni=de.xn--q9jyb4c.online#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
چند ثانیه صبرکنید وصل بشه، هنوز پهنای باند اونقدری زیاد نیست که پرسرعت وصل بشه، یادتون نره فور کنید واسه دوستاتون
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/IranProxyV2/8540" target="_blank">📅 20:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8539">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">vless://8b84b146-3405-44f2-98e4-f0ac7dbad0c0@104.17.147.22:80?mode=auto&path=%2FTelegram%40SoonTeam&security=none&encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&host=uk.im-eb.cc.&type=xhttp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
سرعت عالی، رو همه اپراتورها، بفرستید واسه دوستاتون وصل بشن، حجم نامحدودههههه
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/IranProxyV2/8539" target="_blank">📅 20:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8538">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">vless://48d1cb9d-bbd4-4444-b833-6720619a117e@104.16.89.120:8443?path=%2F&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=nl8.bioritalin.ir&fp=chrome&type=ws&allowInsecure=0&sni=nl8.bioritalin.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو همه اپراتور ها متصله، وصل شین لذت ببرید
✅
حجمممم نامحدودددد
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/IranProxyV2/8538" target="_blank">📅 20:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8537">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">vless://06ef598c-1555-4887-b3f9-08214a2f6792@172.64.152.23:443?path=%2F222.167.202.31%3A7443&security=tls&encryption=none&insecure=1&host=2026.hhhhh.eu.org&type=ws&allowInsecure=1&sni=2026.hhhhh.eu.org#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو تمامی اپراتور و نت های همراه وصله
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/IranProxyV2/8537" target="_blank">📅 20:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8536">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👑
اینترنت ایرانسل و همراه اوکی شد و باید فیلترشکن های رایگان برایتون وصل شده باشه
❤️
🛜
🛜
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/IranProxyV2/8536" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8535">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">vless://48d1cb9d-bbd4-4444-b833-6720619a117e@104.16.89.120:8443?path=%2F&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=nl8.bioritalin.ir&fp=chrome&type=ws&allowInsecure=0&sni=nl8.bioritalin.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو همراه اول متصله
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/IranProxyV2/8535" target="_blank">📅 20:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8534">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
اینترنت بین الملل روی خطوط همراه اول هم وصل شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/IranProxyV2/8534" target="_blank">📅 20:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8533">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کانفیگ رایگان برای وایفا
✅
vless://4493268e-2083-4a18-9c24-72c1f8f604d5@92.42.203.168:443?path=%2F&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=dl-server1.tpchat.ir&fp=chrome&type=ws&allowInsecure=0&sni=dl-server1.tpchat.ir#
%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/IranProxyV2/8533" target="_blank">📅 20:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8532">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد.  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/IranProxyV2/8532" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8531">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/IranProxyV2/8531" target="_blank">📅 20:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8530">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/IranProxyV2/8530" target="_blank">📅 19:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8529">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/IranProxyV2/8529" target="_blank">📅 19:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8528">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزیر ارتباطات:
اینترنت همراه تا امشب وصل میشه، تا فردا اینترنت به قبل از دی برمیگرده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/IranProxyV2/8528" target="_blank">📅 19:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8527">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">📌
بزنید تو نپستر با ایرانسل تست کنید
🛜
ss://YWVzLTI1Ni1nY206WldZeVlUVTBZV1k0T0dNME5EUmhabU0xWkRRMFpqRTNNR0l5Wmpneg@ir.npvnot.com:10112#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/IranProxyV2/8527" target="_blank">📅 18:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8526">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⭕️
شرکت مخابرات: اتصال کامل اینترنت بین‌الملل مشترکان برقرار شد
🔸
کاربران سرویس‌های پهن‌باند ثابت شامل FTTH، VDSL و ADSL هم‌اکنون بدون محدودیت به شبکهٔ جهانی اینترنت متصل هستند و امکان استفاده کامل از وب‌سایت‌ها و خدمات بین‌المللی برای آن‌ها فراهم شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/IranProxyV2/8526" target="_blank">📅 18:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8525">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/IranProxyV2/8525" target="_blank">📅 18:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8524">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/IranProxyV2/8524" target="_blank">📅 18:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8522">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">از اونایی که پرو خریدن چه خبر
😂</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/IranProxyV2/8522" target="_blank">📅 18:23 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
