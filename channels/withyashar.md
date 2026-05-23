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
<img src="https://cdn4.telesco.pe/file/USzuQ-_WMO9EQ7m1ivOsIlqfykWAj9Uamf8sRrY3kYd5GROKWz5NpHCF33fkprbMclC55NaplaLw-VuVdXp6rcJsLLrLlkvS2rvXMbJy6E3PwfPYEpb3Eo_Nn1Wg6bK47IoXIyzy6WDY6kK7bRRTa0EFOwMPeinOpYwvQ1eiLu85racfOh0yNTzrBwHieQshJBNYxDmb2h6nxOU6AdKMbLCAx9Z-pik0-FteLpI9E6QKzpx97ZGwBtqscRy05o5wSQ1h-x4_-zw2H1_lSuKVqFKLBh1hFN1aOnqJG-nM-Vey-Usg54YnVt7YPXmUwq-eCNxtYQGgud1DLaRuad2yHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 270K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 15:25:22</div>
<hr>

<div class="tg-post" id="msg-12144">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">@withyashar
تحلیل پوزیشن الان</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/withyashar/12144" target="_blank">📅 15:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12143">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31857c4cba.mp4?token=OX69W9kjIpP4gGdk3n_n61sU81X_w9Nxe--1lRwDMqgeURWc0X74C5B57sicO-TctIIkJ2neV6KHU9dJhwF3dLS6BwZCzes0_w7cWpqJ8CSIc1JgEAjCWxh0bHwGll59kPm1sFDnhopsAw37HKvEsUS9Cy8dMqzQNKsIB5QLl3_059w4U3ksizee471ghdzNhhlq4mZSC4d_xhdVXXKuoMyzyaMdXs-p791lTNvOxTAWwQE0QixVOxwE1CmmpAjW8TUparLlLi6a4fyRRejK_OFO0u6Sdsj7khg3eMmDwzab6i4RGeJSP2S1hH4N5S2LvD8bXOPRQlg25Zo1JiqBOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31857c4cba.mp4?token=OX69W9kjIpP4gGdk3n_n61sU81X_w9Nxe--1lRwDMqgeURWc0X74C5B57sicO-TctIIkJ2neV6KHU9dJhwF3dLS6BwZCzes0_w7cWpqJ8CSIc1JgEAjCWxh0bHwGll59kPm1sFDnhopsAw37HKvEsUS9Cy8dMqzQNKsIB5QLl3_059w4U3ksizee471ghdzNhhlq4mZSC4d_xhdVXXKuoMyzyaMdXs-p791lTNvOxTAWwQE0QixVOxwE1CmmpAjW8TUparLlLi6a4fyRRejK_OFO0u6Sdsj7khg3eMmDwzab6i4RGeJSP2S1hH4N5S2LvD8bXOPRQlg25Zo1JiqBOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/withyashar/12143" target="_blank">📅 15:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12142">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ادعای خبرنگار الجزیره: یک شخصیت بسیار بلندپایه منطقه‌ای از ایران دیدار کرده است
علی هاشم در پیامی در شبکه اجتماعی ایکس مدعی شد که ـیک چهره بسیار برجسته منطقه‌ای، بی‌سروصدا از تهران بازدید کرد تا آنچه را که بسیاری اکنون «شکاف‌های غیرقابل عبور» می‌نامند، پر کند.
@withyashar</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/withyashar/12142" target="_blank">📅 15:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12141">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تماس تلفنی امیر قطر با ترامپ درباره کاهش تنش‌ها در منطقه
دیوان امیری قطر از تماس تلفنی امیر این کشور با ترامپ ،رئیس جمهور آمریکا خبر داد.
دیوان امیری قطر افزود که امیر این کشور درباره  تلاش‌ها برای تحکیم آتش‌بس و کاهش تنش‌ها در منطقه صحبت کرد.
@withyashar</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/withyashar/12141" target="_blank">📅 14:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12140">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قالیباف در دیدار امروز با عاصم منیر، فرمانده ارتش پاکستان:
جمهوری اسلامی از حقوق خود عقب‌نشینی نمیکنه و به طرفی که صداقت نداره اعتمادی نیست.
جمهوری اسلامی در حالی پای میز مذاکره بود که آمریکا جنگ رو آغاز کرد؛ در صورت شروع دوباره درگیری، پاسخ نیروهای مسلح کوبنده‌تر و تلخ‌تر از گذشته خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/withyashar/12140" target="_blank">📅 14:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12139">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">العربیه: عاصم منیر پیام تهدیدآمیز آمریکا رو به تهران برد.
@withyashar</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/withyashar/12139" target="_blank">📅 14:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12138">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">احتمال وقوع طوفان گرد و خاک در تهران
اداره‌کل هواشناسی استان تهران:
از یکشنبه تا چهارشنبه (۳ تا ۶ خردادماه) در مناطق شمالی استان تهران در بعضی ساعت‌ها وزش باد نسبتا شدید تا شدید همچنین در نیمه جنوبی، مناطق غربی، مرکزی و ارتفاعات در بعضی ساعت‌ها وزش باد شدید تا خیلی شدید پیش‌بینی می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/withyashar/12138" target="_blank">📅 14:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12137">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">moamelegari-trump(@withyashar).pdf</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/withyashar/12137" target="_blank">📅 14:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12136">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b3ee075f.mp4?token=YfVfjvUbTVU6MOPPWyrJ1IsWUDGj7w9vBNwpO3Wr9_TuAZj7T4NJn4Zj3zBXhk4EGue-CK0nBZZQdymIMbP7mGxpOj-sbqSnFR0X-yXatxmwBy4ZyycpyLkYIOrQLi_0B0WFvgxrpC_kb3G-Lgpcjes2HK8TZCBu4DA3tp1TRhaOUHsERWLC0d8ZZXXxQfJLJb6-NtH3o8zxPxmAHV2vERz2o0utHZNh7CWW9NuUeyqXY4vWF1VfYzKHPS1OhBRPKoScieUXW-KuX1WrWuuCnuM91tZxwojahPyrnA9LYMYnLDXnSBFXwRZpR0U1ap9JHipsHVs_wx4nEMvJIuyujg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b3ee075f.mp4?token=YfVfjvUbTVU6MOPPWyrJ1IsWUDGj7w9vBNwpO3Wr9_TuAZj7T4NJn4Zj3zBXhk4EGue-CK0nBZZQdymIMbP7mGxpOj-sbqSnFR0X-yXatxmwBy4ZyycpyLkYIOrQLi_0B0WFvgxrpC_kb3G-Lgpcjes2HK8TZCBu4DA3tp1TRhaOUHsERWLC0d8ZZXXxQfJLJb6-NtH3o8zxPxmAHV2vERz2o0utHZNh7CWW9NuUeyqXY4vWF1VfYzKHPS1OhBRPKoScieUXW-KuX1WrWuuCnuM91tZxwojahPyrnA9LYMYnLDXnSBFXwRZpR0U1ap9JHipsHVs_wx4nEMvJIuyujg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامیون براش بوق میزنه اتو بزنه
🤣
🥴
@withyashar</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/withyashar/12136" target="_blank">📅 14:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12135">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الحدث : آمریکا به تهران پیام داده اگه توافقو رد کنه، عواقب بدی در انتظارشه
@withyashar</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/withyashar/12135" target="_blank">📅 14:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12134">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e08d6a873.mp4?token=nsP0J1Dhbg_1xdrz6rgWQAZUSux5LunEW3e_JfoZh4y0mROLq15aPDPPtc9XqoSGD0oh-UFUkmLtspRzBFmlKRk8FVc-_A0KUGMOLNfqZW-jopdRXBWYdcNpj9Khow9zb9n1gWvAN-FUdSUIlRBRZO9lEnqP35yqtBkZwTjv0FAQbUVGbIpHfHkoC4qrTdRoTCqZ4kizsxofDMT53VNXavVYNpMp7-vsSNPleMXnRG8wKLWfuw3fcqiD5HqSp0nZM3z772XXIKel7iNGViWlN8Y3nbvR7L5awuU4vC6oA6INVnsiFMq9xoMcTXMi01TH5yaBTt7-7r4j_tIGa4XluQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e08d6a873.mp4?token=nsP0J1Dhbg_1xdrz6rgWQAZUSux5LunEW3e_JfoZh4y0mROLq15aPDPPtc9XqoSGD0oh-UFUkmLtspRzBFmlKRk8FVc-_A0KUGMOLNfqZW-jopdRXBWYdcNpj9Khow9zb9n1gWvAN-FUdSUIlRBRZO9lEnqP35yqtBkZwTjv0FAQbUVGbIpHfHkoC4qrTdRoTCqZ4kizsxofDMT53VNXavVYNpMp7-vsSNPleMXnRG8wKLWfuw3fcqiD5HqSp0nZM3z772XXIKel7iNGViWlN8Y3nbvR7L5awuU4vC6oA6INVnsiFMq9xoMcTXMi01TH5yaBTt7-7r4j_tIGa4XluQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنتاگون اسناد جدیدی از ufoها منتشر کرده که مانند یک انسان پرنده است و بسیار شبیه شخصیت “مشعل” در چهار شگفت‌انگیز در کمیک معروف هست.
@withyashar</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/withyashar/12134" target="_blank">📅 14:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12133">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTemEkRO7Q3v2J5iui2BGSrtsUkkV0AsSoV8QNTuV7_AvkfAqeOTVDSp4wagkfAT4FfVzbWdOKDEShzjvJHk-2hxrf9nr8Ak9ITE4pjvHrFe8JRczGUdrc3MgizEydJNJm_sbS5U9zWyjvC2rinQGIGLCVMgq42EZbZgnri5NqMLDV8psy-iDbYAPuZzsV29MCh_e-JAlfEch5rYMRQ483AITBXF3Zlo8Dtu-jAYccLtiifHcxMRkMGd7AE1duLRzjcrxttr2pyT9_mY7YbKHP1g73eiG61aKpBxH7oRtTD-8a_7FOladnMwTUVsolV34bYS33UaJ-eK7ArpSjDsRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاصم منیر، فرمانده ارتش پاکستان با
زرشکیان
دیدار کرد
@withyashar</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/withyashar/12133" target="_blank">📅 13:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12132">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/596c4b1e4c.mp4?token=MJ5SIOstTSb96Kn5BXFR9AXBrxac3dJ6XiqjE4sup9-s0JhwLjIYuRCfQN_px_UyZErUJ4-ozamOTjFDtT8zBWG7oyDXoX-eQ03Be-lOuHU0XFEvkp9B7yT3zEeSjvTjVN_NhjDEkAR4TDl3JW-dYUHL4GayWDIn4vxMQjsLGmYRePmRWQJiEaCpnba9wYNYFygnTihoRTerhJiE3hFHJlkqqLAXJJvek3sGW5dNqEXfsYnWR7i9Q0Gog-F3LU0jFMmuwMkSLAn3Kluq5TPdfU0ZrL2zFS4KPZ7_086jSek0b4pGG2UXbmbjmf8MRB58kbnfGLiYIWpyyd5Jv1JJlw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/596c4b1e4c.mp4?token=MJ5SIOstTSb96Kn5BXFR9AXBrxac3dJ6XiqjE4sup9-s0JhwLjIYuRCfQN_px_UyZErUJ4-ozamOTjFDtT8zBWG7oyDXoX-eQ03Be-lOuHU0XFEvkp9B7yT3zEeSjvTjVN_NhjDEkAR4TDl3JW-dYUHL4GayWDIn4vxMQjsLGmYRePmRWQJiEaCpnba9wYNYFygnTihoRTerhJiE3hFHJlkqqLAXJJvek3sGW5dNqEXfsYnWR7i9Q0Gog-F3LU0jFMmuwMkSLAn3Kluq5TPdfU0ZrL2zFS4KPZ7_086jSek0b4pGG2UXbmbjmf8MRB58kbnfGLiYIWpyyd5Jv1JJlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی و پاکستان در نهایت…
😂
🙌🏾
@withyashar</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/withyashar/12132" target="_blank">📅 13:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12131">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یک مقام دیگر پاکستانی به تهران می‌رود.
😒
یا دیشب اگه رفتن دارن بر میگردن جت نیروی هوایی پاکستان GLF IV SP reg J-755 @withyashar</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/withyashar/12131" target="_blank">📅 13:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12130">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Klor0zSBvtfRa9vxnY2PyNRytGGUkX0jzjBmF8UDnl9y8ERWFjo9jSj7cmkw_HZTCavRxcRaLEgBBW-CLTyaGUFw7BXd3n_PZ0iNLmeAjXt84u_IJq9FENvpI7KiKBwOjq7L-ce9W6A7nXiGXMiYIUnxa5vRBx46a0iJbhL-DPf3FfOeNDrn8YxLK30SC2M6IDIXAN4skqZngWv8_jdKBOIDzPlzjqmIS62CV-TskLx-jB55TRO_89hrIPfeLW2b6sJ--mVM2Y0WGu1mOCBdy0d-RjjHbCE5xdKdMaXXQGwuGFvqGh740OuTk138arcbV-2L__KWBTt-9UfVRFfJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاصم منیر، رییس ستاد کل ارتش پاکستان با محمدباقر قالیباف در تهران دیدار کرد
@withyashar</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/withyashar/12130" target="_blank">📅 13:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12129">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نورالدین الدغیر خبرنگار الجزیره در تهران: وساطت‌ها بین تهران و واشنگتن به مرحله‌ای رسیده که یکی از سران منطقه‌ای به طور مستقیم برای پر کردن شکاف‌ها وارد عمل شده.
ظهور قطر در این لحظه حساس به طور مستقیم و بر اساس اطلاعات و منابع موجود، نه صرفاً به عنوان نقش کمکی برای پاکستان، بلکه به عنوان نقش محوری است.
منبعی می‌گوید که احتمال دارد یکی از میانجی‌ها به واشنگتن سفر کند.
@withyashar</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/withyashar/12129" target="_blank">📅 13:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12128">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/withyashar/12128" target="_blank">📅 13:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12127">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">@withyashar
به در میگم دیوار بشنوه</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/withyashar/12127" target="_blank">📅 13:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12126">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHd</strong></div>
<div class="tg-text">یاشار جان درود و خسته نباشید.
به این رفیقمون بگو جمله ی سر سفره ی پدر و مادر بزرگ شدن یک استعاره از تربیت و پرورش درست و اخلاقیه ، ربطی به حضور یا عدم حضور خانواده نداره
انقد همه چیز رو فلسفی نکنن
این عادت چپ ها و گلوبالیست ها هستش</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/withyashar/12126" target="_blank">📅 13:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12125">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Mehmooni (iG @yashar)</div>
  <div class="tg-doc-extra">Amir Tataloo (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/12125" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/withyashar/12125" target="_blank">📅 13:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12124">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/withyashar/12124" target="_blank">📅 13:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12122">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/withyashar/12122" target="_blank">📅 13:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12121">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSaya</strong></div>
<div class="tg-text">درود و وقت بخیر
سر سفره پدر و مادر بزرگ شدن یکی از جملاتیه که باید از بین ببریمش اگه ممکنه کم کم دیگه تکرار نکنید چون الان الگوی خیلیامون قرار گرفتین
🌹
شخصی که بچه طلاقه یا بی سرپرست می‌تونه خیلی بهتر از اونی باشه که کنار پدر و مادرش بزرگ شده
🤍</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/withyashar/12121" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12120">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">منبع ارشد ایرانی به الحدث: آنچه تاکنون مطرح کرده‌ایم برای ایالات متحده قابل قبول نیست
@withyashar</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/withyashar/12120" target="_blank">📅 13:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12119">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شهباز شریف نخست وزیر پاکستان امروز شنبه وارد شهر هانگ‌جو واقع در شرق چین شد و دیدار رسمی چهار روزه خود از چین را آغاز کرد.
@withyashar</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/withyashar/12119" target="_blank">📅 12:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12118">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">منابعی به اسکای نیوز عربی گفتن که میانجی پاکستانی موفق شده بر مانع پرونده هسته‌ای ایران غلبه کنه
@withyashar</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/withyashar/12118" target="_blank">📅 12:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12117">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">علی کریمی : ببینیم کی قبلا چیکاره بوده و الان چیکارتست و دنبال چی هست؟!
ببینیم که چند چندیم؟!
بببینیم کی برای پول و صندلی مبارزه کرده، کی برای آزادی ایران؟!
این گوی و این میدان
@withyashar</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/withyashar/12117" target="_blank">📅 12:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12116">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q55pRvyhp3erf6uTg3FCPTcWmkQkNDUSlNY563gisdoF7JQH-lBq-LUbhLr4w1Oht0PVhu9Jo5kQQGwflOhqJo72iu5KvNB3SaXrVc-WOWKnXa-bdlLxHuUSdHvjkh3rgN6N9w2O6Bj7MMNKiy3Z3sWoQq9KvDmkW5RoQjAeAz2R3rVzgQWoNQDO6p0UAAPJc-YDE8demJji1pXksqcfxWG2-uHXn6n4NIphvumdLJNB0hJXmtPKqXkkQ7-rgn-U37HyBa8ThZf_LgW3OneQwTwM3No2nzBDU26n2w4wfH0X9ZDJe2mFP5Rdr39CKz6Kceq5q6QisG_nREZyhLsTGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیرا شریفی مقدم:  آماده رفتن به جنگ هستم
@withyashar</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/withyashar/12116" target="_blank">📅 12:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12115">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارشهای تایید نشده : ویزای شجاع خلیل زاده احسان حاج‌صفی و مهدی طارمی به دلیل حمایت از سپاه تروریستی پاسداران رد شدن @withyashar</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/withyashar/12115" target="_blank">📅 12:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12113">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حمله ارتش اسرائیل به یک مجتمع بزرگ زیرزمینی حزب‌الله در اعماق لبنان و جنوب این کشور
@withyashar</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/withyashar/12113" target="_blank">📅 12:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12112">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUL1fD_JWpVe5jAWigHDvV1NrF9FQ1-2qauqE6VUxXvaW5RG2dgdO0DsttrBLiy4-Fy0YvLK2bCedcS-s1_HoLH2f-7z_bxE-3anf2qASTA6RwPkKfCfgRfDx8s33s11kreImmWCChDQHlpGcslUXNM56j7IkS_wF6P4sn4awbWGHrudrq_U_nde9XDYNQUXQWkD1dQNiyJnGv_fMH37mQ-cKmXEO8fSRVFR_WwOZ2LqLcUfkw5O-NqYOpaG7OClmKeH-SjS2GjC0mTwJYBOJq8Ka7MlDQt5aIEqbnC26OAtAIXE9UgMCafvTG71zTvDNUdDE1hqRurSPKg1rXEC5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام دیگر پاکستانی به تهران می‌رود.
😒
یا دیشب اگه رفتن دارن بر میگردن
جت نیروی هوایی پاکستان GLF IV SP reg J-755
@withyashar</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/withyashar/12112" target="_blank">📅 11:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12111">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ادعای کانال ۱۳ عبری به نقل از نیویورک‌تایمز: ترامپ اسرائیل را از مذاکرات با ایران کنار گذاشته است.
@withyashar</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/withyashar/12111" target="_blank">📅 11:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12110">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سناتور راجر ویکر:  «الان تو مقطعی هستیم که می‌تونه میراث سیاسی ترامپ رو مشخص کنه. غریزه ترامپ این بوده که کاری رو که تو ایران شروع کرده، کامل تموم کنه؛ اما بهش توصیه‌های اشتباه می‌شه تا دنبال توافقی بره که حتی ارزش کاغذی که روش نوشته شده رو هم نداره. فرمانده کل نیروهای آمریکا باید اجازه بده ارتش حرفه‌ای آمریکا نابودی توان نظامی متعارف ایران رو کامل کنه و تنگه رو دوباره باز کنه. ادامه تلاش برای توافق با حکومت ایران ممکنه نشونه ضعف تلقی بشه. باید کاری رو که شروع کردیم، تموم کنیم. وقت اقدام گذشته.»
@withyashar</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/withyashar/12110" target="_blank">📅 11:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12109">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گزارشهای تایید نشده : ویزای شجاع خلیل زاده احسان حاج‌صفی و مهدی طارمی به دلیل حمایت از سپاه تروریستی پاسداران رد شدن
@withyashar</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/withyashar/12109" target="_blank">📅 11:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12108">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">روبیو وارد هند شد
وزیر امور خارجه آمریکا امروز با هدف تقویت همکاری‌ها با هند وارد این کشور آسیایی شد.
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/12108" target="_blank">📅 10:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12107">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کانال ۱۲ اسرائیل: درنهایت برآورد اسرائیل اینه که هیچ توافقی انجام نخواهد شد و ارتش دفاعی اسرائیل برای شروع موج جدیدی از حملات به ایران طی روزای آینده آماده می‌شه
@withyashar</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/12107" target="_blank">📅 10:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12106">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شبکه CBS به نقل از چند منبع آگاه از برنامه‌ریزی‌های نظامی اعلام کرد که دولت ترامپ در حال آماده شدن برای دور جدیدی از حملات علیه ایران است، هرچند هنوز به تصمیم نهایی نرسیده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/12106" target="_blank">📅 09:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12105">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سخنگوی وزارت دفاع ایران: ترامپ چاره‌ای جز پذیرش خواسته‌های ایران ندارد، در غیر این صورت متحمل شکست‌های بیشتری خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/12105" target="_blank">📅 09:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12104">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بزرگترین نمایشگاه هوایی نظامی بریتانیا لغو شد، زیرا گزارش شده است که از این فرودگاه برای ماموریت‌های مرتبط(احتمالا حمله) با ایران استفاده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/12104" target="_blank">📅 06:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12103">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">از دیشب تا الان نخوابیدم سربازم الانم دارم میرم سر شیفتم  جنگ قبلی ام توی شیفتم شروع شد اموزشیمم جنگ 12 روزه بود دعا کنین زنده برگردم
🥲
💔
😂</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/withyashar/12103" target="_blank">📅 06:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12102">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromᴍᴏʜᴀᴍᴍᴀᴅ</strong></div>
<div class="tg-text">از دیشب تا الان نخوابیدم سربازم الانم دارم میرم سر شیفتم  جنگ قبلی ام توی شیفتم شروع شد اموزشیمم جنگ 12 روزه بود دعا کنین زنده برگردم
🥲
💔
😂</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/12102" target="_blank">📅 06:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12101">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ca021662.mp4?token=N0Yg3PPO3wkOgGV9EPmhO3g5L6W5td3pVXTjM03uo6UeBo2OvBSWJp8sHYw0sCMc9Ke-hjSOl-3l3ARF0UtaOOYLsnjPlZzZV0bSk-dkT33xNKTTkWb9ZQ7GHlVy7GzWJuTRZaXK3eoqGEXH5QILUKVJJIgNezg5DrHVu7tW2_P9aCCHtSmFtOtvfr9iZj2oOkK3V_73qAAB76o3kMDcGIiWcj0Rm2uz3bG6ye5zJ0G9i50Yl905HNmCSOzaovdr9TaUEJQ-Cyy0Mz7Chtgspqc7vdikBf1bNA1iX1FcZOb3wtbDbx55eBwowP-KOBjCOSawJF0xaX_epTt0FpEeFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ca021662.mp4?token=N0Yg3PPO3wkOgGV9EPmhO3g5L6W5td3pVXTjM03uo6UeBo2OvBSWJp8sHYw0sCMc9Ke-hjSOl-3l3ARF0UtaOOYLsnjPlZzZV0bSk-dkT33xNKTTkWb9ZQ7GHlVy7GzWJuTRZaXK3eoqGEXH5QILUKVJJIgNezg5DrHVu7tW2_P9aCCHtSmFtOtvfr9iZj2oOkK3V_73qAAB76o3kMDcGIiWcj0Rm2uz3bG6ye5zJ0G9i50Yl905HNmCSOzaovdr9TaUEJQ-Cyy0Mz7Chtgspqc7vdikBf1bNA1iX1FcZOb3wtbDbx55eBwowP-KOBjCOSawJF0xaX_epTt0FpEeFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو مربوطه …
😬
@withyashar</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/12101" target="_blank">📅 05:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12100">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">لارا لومر از معتمد ترین افراد نزد ترامپ ، خبر آماده شدن آمریکا برای حملات دوباره رو ریتوییت کرده.
@withyashar</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/withyashar/12100" target="_blank">📅 05:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12099">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پست دن اسکاوینو از مشاوران ترامپ در شبکه اجتماعی X @withyashar</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/12099" target="_blank">📅 05:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12098">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsphYcsSLPmspkRGrFXBtbSQfPQEGRyBUDlGFky3p_9Mlx8BQn-Bpa151FrEpNBT_cSb0wP7sZI2xmPrQhrarozrlW_idZ4rzscxBzBYCumYuRlasG3X7pvuNlnjznGHYz0qD48TKeeUq2zPOarV4tucuQCaat4ja7cfCU9ssfwvUuSY1pvXqgUoz6P3V8rzgxCRvzMfsmmM1YnQAwxGS89B2GNxOBk1imv1VMgwu-rio3TG60Y5S_rimGwBevY5RJVypVD6Aveg7i7YUngUw4qjBhW-Q8AeVSzk5BgDlm7BkuWjD2V0WY069oecuKA7TQyf9-oF1eP_pGhhCo-nCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست دن اسکاوینو از مشاوران ترامپ در شبکه اجتماعی X
@withyashar</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/withyashar/12098" target="_blank">📅 05:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12097">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تمام کنفرانس های خبری کاخ سفید لغو شد
@withyashar</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/12097" target="_blank">📅 05:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12096">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خوب تا ۵ ایران نزد میریم برای ۹ صبح به بعد ، حالا خوابمم نمیبره
🥴
🤣</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/12096" target="_blank">📅 05:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12095">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/withyashar/12095" target="_blank">📅 04:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12094">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/withyashar/12094" target="_blank">📅 04:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12093">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/12093" target="_blank">📅 04:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12092">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/12092" target="_blank">📅 04:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12091">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzNqpRgcJRb47FOJyB4X6JaZ7DLLyJzNzQiqU4E5FOkbPttSv95yrsvjDfg9tXk1lJuQASpT8ybthqO61vOIvO2261wQt85nmDGE9KpdB2zfiOUnTluixtWqCfcsDhNV4Bga4BvG3CKCozo_AakC6oAd58P07REHm7pFdbYjpU6L8QHoLGInItJAydJsMHRexeMxOAXgX2XLz-l1TfQZOV3q1BguBxVFGVfXZdTOO_Bu34rVphTT98U33K2dctMJbyoPX_dbQtne8F32IOCKUHIz4OVasSlDqSf3Hbw3Vna7SzNawhZLmvh1stq5BrsWpomOArke7FaOk1MHobd64g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/12091" target="_blank">📅 04:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12090">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/withyashar/12090" target="_blank">📅 04:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12089">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/12089" target="_blank">📅 04:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12088">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-text">درود داداش شما میدونی چه اتفاقی افتاده این همه تفرقه تو پادشاهی خواها افتاده؟
چمونه اینا الان ۹۰روزه اتحاد دارن هر شب میان راه پیمایی پس ماهایی که هدفمون نابودی ایناست چرا اینقدر اختلاف داریم...</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/12088" target="_blank">📅 04:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12087">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/withyashar/12087" target="_blank">📅 04:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12086">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شبکه الحدث به نقل از منابع مطلع گزارش داد فضای مذاکرات میان تهران و واشینگتن «مثبت» ارزیابی می‌شود،
اما دو طرف هنوز به توافق نهایی نرسیده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/12086" target="_blank">📅 04:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12085">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نیروی دریایی اسرائیل در حال ارسال پیام های رادیویی است.
@withyashar</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/withyashar/12085" target="_blank">📅 03:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12084">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ارتباطات رادیویی ارتش روسیه از کار افتاده است.
@withyashar</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/withyashar/12084" target="_blank">📅 03:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12083">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ایوانکا ترامپ، دختر اول، هدف ترور توسط یک تروریست آموزش‌دیده سپاه پاسداران انقلاب اسلامی (IRGC) قرار گرفت، در یک نقشه پیچیده برای انتقام‌گیری از رئیس‌جمهور به خاطر حذف مربی‌اش
نیویورک پست : محمد باقر سعد داوود السعدی، ۳۲ ساله، که اخیراً دستگیر شده است، «تعهد» کرده بود که ایوانکا را بکشد و حتی نقشه خانه‌اش در فلوریدا را داشت.
این شهروند عراقی ظاهراً خانواده رئیس‌جمهور دونالد ترامپ را هدف قرار داده بود در پاسخ به کشته شدن فرمانده نظامی ایرانی، قاسم سلیمانی، در حمله پهپادی آمریکا در بغداد شش سال پیش.»
@withyashar</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/withyashar/12083" target="_blank">📅 03:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12082">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/withyashar/12082" target="_blank">📅 03:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12081">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دوستانی که فوحش خاستن تست کردن و خوردن و بلاک کردم
😃
دیکتاتور خشن یاشار</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/withyashar/12081" target="_blank">📅 03:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12080">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دایرکت بی مورد ندید مخوصوصا کسی بپرسه امشب میزنه یا بپرسه بخوابم یا نه …. خستم و با شدیدترین پاسخ ممکن جواب میدم !</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/withyashar/12080" target="_blank">📅 03:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12079">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/12079" target="_blank">📅 03:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12078">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">منابع دولتی گزارش می‌دهند که ارتش جمهوری اسلامی به بالاترین سطح هشدار رسیده است.
@withyashar</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/withyashar/12078" target="_blank">📅 03:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12077">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnVTCymq-9WZY4iOt0eaG2C4odvNdNWmJS1t73xC8VY5RRTmo-JUevRqe7Sn3Wpydd2u-ZRT2qkzVi-ohNwUZ8Ad9YNg7KEOzOHudtMGybK0JAyoA29STI8yfeGVgiJRNFFSs-s0dIQaA0SQlTw9Y_HVkz4LBxVlh6t2a1u3-5GhtPKvZIhjG4rVrJ5nsQYSGnGscZPqlY6VDaSIShax2nCMrrS1XjCM7McbPJbxdkeHc-Hlphrruj-NzoaBfRyE6YMflu0THYGg53vPDOywXkbkMa8lQYT0DUYdiAVLF2hVXIQbFus0wbWaQs-E4y8yM0RS-mcZki2IPeKPqxgczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه فعلی اختلالات مداوم GPS در خلیج فارس
GPS Jamming
یعنی فرستادن پارازیت روی سیگنال ماهواره‌ای تا پهپاد، موشک، هواپیما یا موبایل نتواند موقعیت دقیقش را پیدا کند.
این کار را معمولاً اطراف مناطق حساس نظامی انجام می‌دهند تا سلاح‌ها و پهپادهای دشمن دقتشان کم شود یا مسیر را گم کنند.
نوع پیشرفته‌ترش «Spoofing» است که موقعیت جعلی نشان می‌دهد و هدف را به مسیر اشتباه می‌برد.
@withyashar</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/withyashar/12077" target="_blank">📅 03:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12076">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a4e7387eb.mp4?token=qBil3FS-n9j9Z6A_a9H23X9hMFCW7B73f392p0MNbxy3JEwZHHmq6vwf5ocT5kK0_ZFSiWfe3Rze1zXKPBG3kE4KWNHZ91eQVLJl1El6efzzxZoMShCictakhPTmmwZfk38xMrn2b28AiXh65EmbMkyPXhZB7BcyRN6in-G6K7-56dGdGjGhxIDL_W19LsW45O09E6tFszbk5AklmnTW5da6wCnYN4Kak_qwxttCUIQjTcypapb-M9mNKaBvJrOzPtualWO4hP1TAdX5bTtGFzsBPhKlEk6386y1NR9_DHKzdwoLpmQxwe8IOqF7Q45hvWMN4SPTW_eoJyeKn8d6XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a4e7387eb.mp4?token=qBil3FS-n9j9Z6A_a9H23X9hMFCW7B73f392p0MNbxy3JEwZHHmq6vwf5ocT5kK0_ZFSiWfe3Rze1zXKPBG3kE4KWNHZ91eQVLJl1El6efzzxZoMShCictakhPTmmwZfk38xMrn2b28AiXh65EmbMkyPXhZB7BcyRN6in-G6K7-56dGdGjGhxIDL_W19LsW45O09E6tFszbk5AklmnTW5da6wCnYN4Kak_qwxttCUIQjTcypapb-M9mNKaBvJrOzPtualWO4hP1TAdX5bTtGFzsBPhKlEk6386y1NR9_DHKzdwoLpmQxwe8IOqF7Q45hvWMN4SPTW_eoJyeKn8d6XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به کاخ سفید رسیده است و به تیم خبری رسماً اطلاع داده شده که ترامپ در بقیه روز هیچ حضور عمومی، بیانیه یا فرصت عکسبرداری نخواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/withyashar/12076" target="_blank">📅 03:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12075">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">طبق گزارش CBS نیوز:
دولت ترامپ در حال آماده‌سازی برای دور جدیدی از حملات علیه ایران است، علی‌رغم تلاش‌های دیپلماتیک در جریان، در حالی که چندین مقام نظامی و اطلاعاتی ایالات متحده برنامه‌های آخر هفته روز یادبود خود را لغو کرده‌اند با انتظار اینکه اقدام نظامی ممکن است دستور داده شود.
@withyashar</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/12075" target="_blank">📅 03:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12074">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/withyashar/12074" target="_blank">📅 03:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12073">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9121089b0a.mp4?token=hALyvO80n9OJ9qSWbNryhtzMXt3jbzmwyATCsA0vjGFF8_md8-nyduZh_V3vUqJVmZaWJPeSnqvfvRnHaz8u4C6DZVHqKiZeQ3QvacChmYmYtCWYR45d_3euFvRlLxDquZAfh_aHIJChGgkDeIQRjma47SW8zNsodX637jePcW8tZLYzF98T_nSHRj1kLQT6_LisgxDP_NcIvY4e8gHsw-WgEZUcyjkfuJyLWY4NBgNVjQC-Yxn-sy3EbbKiyogb_VFdXOKHk-gmo2KhOt1gFMb_2YwMeTomoLZEO_chS10zKje-EMYgSEIpiVUjvcLu7e3mFvciSsaZRWIMMmAGDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9121089b0a.mp4?token=hALyvO80n9OJ9qSWbNryhtzMXt3jbzmwyATCsA0vjGFF8_md8-nyduZh_V3vUqJVmZaWJPeSnqvfvRnHaz8u4C6DZVHqKiZeQ3QvacChmYmYtCWYR45d_3euFvRlLxDquZAfh_aHIJChGgkDeIQRjma47SW8zNsodX637jePcW8tZLYzF98T_nSHRj1kLQT6_LisgxDP_NcIvY4e8gHsw-WgEZUcyjkfuJyLWY4NBgNVjQC-Yxn-sy3EbbKiyogb_VFdXOKHk-gmo2KhOt1gFMb_2YwMeTomoLZEO_chS10zKje-EMYgSEIpiVUjvcLu7e3mFvciSsaZRWIMMmAGDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
🤣
@withyashar</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/withyashar/12073" target="_blank">📅 02:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12072">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تعطیلی مراسم یادبود آخر هفته(دوشنبه) برای برخی از نیروهای نظامی آمریکایی لغو شد.
@withyashar</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/withyashar/12072" target="_blank">📅 02:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12071">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6458715c79.mp4?token=dqzwOkcHQ1YSAlHN-3FqCX2aeCbA18kytKbCCc4CidSaZcppeGjACol8T71D00GEAIjl22j5GYRG8SmmHsaNyZOv5E1YRnmkjQjZEQVN-IKfCDsPXK7RD5EKVzJVRLt1xQEdqxtim6kmBXv7i69LvIJI949O6RChc-AvyDJhffNgKWCciqYtg3dL9kOwTC__Fabkkvfoj9LZV-ElQ_nTVYg3nXyiZWwxO7VLXyiBxBrIH8X9vFH8I2dkfczrBIWsHbgnikg9i4ZL-M2f6fllv7hRB4_IT5OSa-fmWXGZzih7AcbpN6ykKBhB9vetWFUUHugLs9jS7umeN3Xuy42UHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6458715c79.mp4?token=dqzwOkcHQ1YSAlHN-3FqCX2aeCbA18kytKbCCc4CidSaZcppeGjACol8T71D00GEAIjl22j5GYRG8SmmHsaNyZOv5E1YRnmkjQjZEQVN-IKfCDsPXK7RD5EKVzJVRLt1xQEdqxtim6kmBXv7i69LvIJI949O6RChc-AvyDJhffNgKWCciqYtg3dL9kOwTC__Fabkkvfoj9LZV-ElQ_nTVYg3nXyiZWwxO7VLXyiBxBrIH8X9vFH8I2dkfczrBIWsHbgnikg9i4ZL-M2f6fllv7hRB4_IT5OSa-fmWXGZzih7AcbpN6ykKBhB9vetWFUUHugLs9jS7umeN3Xuy42UHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/12071" target="_blank">📅 02:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12070">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مهدی طارمی نمیدونم کیه ولی میگن به اردوی آنتالیا تیم‌ملی اضافه شد
@withyashar</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/withyashar/12070" target="_blank">📅 02:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12069">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/withyashar/12069" target="_blank">📅 02:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12068">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">جت های جنگی اسرائیلی به صورت گسترده در حال پرواز به سمت آسمان عراق و عربستان مشاهده شدند.
@withyashar</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/12068" target="_blank">📅 02:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12067">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">توجه کنید این خبر فعلا فقط توسط رسانه های اسرائیل گفته شده هنوز تایید نشده</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/withyashar/12067" target="_blank">📅 02:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12066">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارشها حاکی از این است که هیئت پاکستانی با عجله تهران را ترک کردند. @withyashar</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/12066" target="_blank">📅 02:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12065">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کلاً یه دونه تانکر سوخت رسان تو آسمون اسرائیله. من نمیدونم چرا یه خبر فیک میزنن همه هم همونو کپی میکنن همه جا پخش میکنن.</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/withyashar/12065" target="_blank">📅 02:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12064">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کلاً یه دونه تانکر سوخت رسان تو آسمون اسرائیله. من نمیدونم چرا یه خبر فیک میزنن همه هم همونو کپی میکنن همه جا پخش میکنن.</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/withyashar/12064" target="_blank">📅 02:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12063">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یه هم زبون افغان نیست اینجا ؟
😃</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/withyashar/12063" target="_blank">📅 02:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12062">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گزارشها حاکی از این است که هیئت پاکستانی با عجله تهران را ترک کردند.
@withyashar</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/withyashar/12062" target="_blank">📅 02:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12061">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خبر‌ فورررریییییییی
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/withyashar/12061" target="_blank">📅 02:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12060">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/withyashar/12060" target="_blank">📅 02:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12059">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⚜️HoSsein⚜️</strong></div>
<div class="tg-text">یاشار حاجی استیکر حامله رو چیکار کنیم آزاد کنی؟
😂</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/12059" target="_blank">📅 02:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12058">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/withyashar/12058" target="_blank">📅 02:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12057">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/12057" target="_blank">📅 02:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12056">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/12056" target="_blank">📅 02:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12055">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/withyashar/12055" target="_blank">📅 02:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12054">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کسایی که بلاک میشن بیان محترمانه عذرخواهی کنند بدون حرف اضافی آنبلاک میکنم
قوربان شوما دیکتاتور مهربون یاشار
🤣
❤️‍🩹
🙌🏾</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/withyashar/12054" target="_blank">📅 02:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12053">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بیتکوین شلوار خودشو خیس کرد  داره میریزه
🥴
@withyashar</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/12053" target="_blank">📅 01:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12052">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a36ce8317f.mp4?token=dEPyOdhK240U0G3NKi-mnxcFLt-sQT1x62lXYsLLMUKY0ADKiaNBURYGNZ-bay_VRD6KJ_XhAlR6OLi4UPu8ifvpOR06nLizkE-BvIWja1Ly_xEO4fDQ6lFPFRbVOe-BJyO-xpASvMChiWForqzfxQBD6fUswntARvaA_1a9Az1jo5yz3Vh8ORVpquW_SFvuHbPmBQO1lEJy0k6IzvdQcr9WcTrXY1BELKa5D9Yowh5O2dMWIDjQvpEYyZ7UYoXldrVsp1ItdfG3Nswpmf5FKWM9nqibSgMoMut6JSbbAZut_6Pp-UeOm4N82ZCQdOmN5AeQkJ59V4C1nuJ-nZRZHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a36ce8317f.mp4?token=dEPyOdhK240U0G3NKi-mnxcFLt-sQT1x62lXYsLLMUKY0ADKiaNBURYGNZ-bay_VRD6KJ_XhAlR6OLi4UPu8ifvpOR06nLizkE-BvIWja1Ly_xEO4fDQ6lFPFRbVOe-BJyO-xpASvMChiWForqzfxQBD6fUswntARvaA_1a9Az1jo5yz3Vh8ORVpquW_SFvuHbPmBQO1lEJy0k6IzvdQcr9WcTrXY1BELKa5D9Yowh5O2dMWIDjQvpEYyZ7UYoXldrVsp1ItdfG3Nswpmf5FKWM9nqibSgMoMut6JSbbAZut_6Pp-UeOm4N82ZCQdOmN5AeQkJ59V4C1nuJ-nZRZHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ خیلی فوری‌ نیویورک رو ترک و مستقیم برگشت کاخ‌سفید.
او پیشتر خبر از کنسل کردن تعطیلات اخر هفته خود و رفتن به عروسی پسر ارشدش رو به علت مسائل ایران داده بود..
@withyashar</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/withyashar/12052" target="_blank">📅 01:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12051">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">لطفا از ‌دایرکت بی مورد پرهیز کنید در زمان شلوغی … دایرکته محل کامنت و احساسات شما نیست ، هواپیمای هیئت قطری هم میره ترکیه ! قبل از ارسال خبر ببینید که در چنل نیسن بعد بفرستید ، دایرکت فقط یک پیغام ارسال کنید هر چند خط شد … ممنون از توجه شما به این موضوع</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/withyashar/12051" target="_blank">📅 01:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12050">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvhmWdKjomT95P2vLSDfLmcDVITwH62sZ7nL4jO98ThMFC64LMvTvTd4dRZRytYm9yWqCa7EzasSKXoqx2D9F92-nAObR2aY3lwugEgQCLlfoVA56y7sPCdLu_YCaI3wXLygf_7CQsM6eHNRxL7tzLtiZ2c0wRDJm1aEacKa7K1Pj969yNodX--PHejpgnHc2_lcYwpt-2nsZSsCp1I87upLtxJ-SqId6hXOkm6G89yEYgC4vd6VkKTXiDdQhLWyMrfO74_ZYIh4whfzP2jBeDle1a9rkR2HdtDGBa1jJlJUzzysyyUbze_BsBc10EovhuI15ZVAJyxLB-6rrZVhRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگندههای ایرانی که از مهرآباد بلند شدند برای اسکورت هواپیمای مقامات قطری بودند.
@withyashar</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/withyashar/12050" target="_blank">📅 01:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12049">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iO5fU3UdtqWWW48VNWwrTowQMHjcrsZ99_FQpQ-q_O2radkfY_Z9AeH5Xnwuw16qEl6OOivbVmw32Mcd3gQHmwMxlvgUx2Sy3oUtMOVfR9yUkUEflGiaPRSvTQZCMwknbsjyt5OXZnUnGRW0uIwF56yFZ8hMRrHVkrPIGNk6bIj_LUjzB5wRgKASAlshOBYYYUDjw0P3ElO9NLB7DNdGhNUUg5Lg05H15VLG6CXHKt_RXH4WYA2IqhECXFFl-qtMfD_FzkUSITT2SBGWh8j0UXrIvKVClYwZbk3WimkSY-9b7HmmNlfBQTn2gXXc6_ziZHSCLigTeY0Cm2pP73wJRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون هواپیمای گشت دریایی چندمنظوره (بویینگ P-8 پوزایدن) و یک پهپاد  ناشناس بدون شک آمریکایی بر فراز خلیج فارس !
@withyashar</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/12049" target="_blank">📅 01:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12048">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هیئت قطری تهران را ترک کرد
گزارش‌ها حاکی است هیئت قطری پس از رایزنی‌های دیپلماتیک، تهران را ترک کرده است.
این سفر در حالی انجام شد که قطر در کنار پاکستان و چند کشور منطقه، در تلاش برای میانجیگری میان ایران و آمریکا جهت دستیابی به توافقی برای پایان جنگ و ادامه مذاکرات هسته‌ای بود.
@withyashar</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/12048" target="_blank">📅 01:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12047">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گزارش‌های متعددی درباره برخاستن اضطراری (اسکرامبل) جنگنده‌ها از فرودگاه مهرآباد، تهران دریافت شده است.
@withyashar
جنگنده های خود رژیمن از ترسه …. شانه کسکم</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/12047" target="_blank">📅 01:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12046">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromK h</strong></div>
<div class="tg-text">کردان سمت هشتگرد صدای جنگنده میاد</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/withyashar/12046" target="_blank">📅 01:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12045">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑆𝑒𝑝𝑖𝑑𝑒ℎ</strong></div>
<div class="tg-text">یاشار جان کرج صدای جنگنده میاد
ساعت  01:06</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/withyashar/12045" target="_blank">📅 01:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12044">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RT9xuCs-DuoZDDLSFtP80fl9Gi4_1Cq3s5H0s29Qb3cQC-yJ--rVu3ZuFfuwCzXrN20iHp5rtirDtGw3OgAHP-EqTJsKeir71TUF1kzd5YcyitWQcmxUhc-l8xgM2Wfr-NfSXudDjCvtmyjUemr4GKiRsGtyHFyStWHNrmrDvZXvurDITJ0gkW65lrkaKwFAGGwqfd-dGnN9twgsrXJwB_u13oqtAmAKp2MC48dVmDOFyVjnvTIt-C2U45TX1aS-7wjeZJXBFlCGQbwc-tTvip07EnlnyDoR4T8FoSidmhNVQO6JRbWhmg3ZXIDxoCpNtlc-DZxZlYQMghgG2KV6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فضای هوایی غرب ایران طبق یک NOTAM جدید تا صبح روز دوشنبه بسته شده است، به‌جز پروازهای روزانه (در ساعات روشنایی روز)
@withyashar</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/withyashar/12044" target="_blank">📅 01:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12043">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">۸۹ ساعت و ۳۰ دقیقه دقیقا الان خوبه ؟
چون ویس و حتی تکست ها رو که بالا هست نمیری ‌نگاه کنی
…
🤬
۵۰ بار گفتم</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/12043" target="_blank">📅 01:08 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
