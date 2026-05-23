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
<p>@withyashar • 👥 271K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 20:25:29</div>
<hr>

<div class="tg-post" id="msg-12193">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وضعیت ما بعد از حمله ، به زودی</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/withyashar/12193" target="_blank">📅 20:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12192">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/withyashar/12192" target="_blank">📅 20:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12191">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وضعیت ما مردم ایران الان</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/withyashar/12191" target="_blank">📅 20:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12190">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9fecf1e31.webm?token=uM3wL2nSTXozrVWKitj9OmSdD7EcbYc9TWRVMCkdEmJRENQTy0yRNoUiwDJi5FWfhMhkS53gejwTbIeQ6bCGZbQfRzzijVQcInbt547p4QRILBPci0LnaONGaJ_kHA1cFfcyFfGMSeX_WyHi8FK7IXEo9-kf1WCGo-OUHcSby7mAdrg3umJe-LMeyYygntWW0KRYfw9eYKwjTtRuqlKOl38YcVWwodiDIm8InbZJCclW1lh62VJULcrUjGZTu6LdqPXDXBIhT-Hfy3wpNBHxQqXGdidqnOjv_K7SSJtWaz2vkj8P8pb4E1coIg1NcniTr4pWR9XgKl8zGb4ZNxF-QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9fecf1e31.webm?token=uM3wL2nSTXozrVWKitj9OmSdD7EcbYc9TWRVMCkdEmJRENQTy0yRNoUiwDJi5FWfhMhkS53gejwTbIeQ6bCGZbQfRzzijVQcInbt547p4QRILBPci0LnaONGaJ_kHA1cFfcyFfGMSeX_WyHi8FK7IXEo9-kf1WCGo-OUHcSby7mAdrg3umJe-LMeyYygntWW0KRYfw9eYKwjTtRuqlKOl38YcVWwodiDIm8InbZJCclW1lh62VJULcrUjGZTu6LdqPXDXBIhT-Hfy3wpNBHxQqXGdidqnOjv_K7SSJtWaz2vkj8P8pb4E1coIg1NcniTr4pWR9XgKl8zGb4ZNxF-QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/withyashar/12190" target="_blank">📅 20:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12189">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آکسیوس به نقل از منابع: تماس ویدیو کنفرانس بین ترامپ و رهبران کشورهای عربی در مورد پیش نویس توافق با ایران ساعت ۵ بعد از ظهر به وقت گرینویچ انجام خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/withyashar/12189" target="_blank">📅 19:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12188">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ به کانال 12 اسرائیل   :
به نتانیاهو گفتم نگران نباش چون من توافقی که به نفع اسرائیل نباشه نمیکنم ، نتانیاهو نباید نگران باشه ، بعضیا خواهان توافقن و بعضی جنگ و نتانیاهو مابین این دو گیر کرده
@withyashar</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/withyashar/12188" target="_blank">📅 19:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12187">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رویترز از شکست مذاکرات در تهران خبر داد،
تهران هیچ امتیاز بیشتری در مذاکرات نداده و این امر منجر به شکست مذاکرات و بازگشت هیئت های پاکستانی و قطری از تهران شد.
@withyashar</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/withyashar/12187" target="_blank">📅 19:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12186">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سی‌بی‌اس در گفتگو با ترامپ: من پیش‌نویس یک توافق با ایران را دیده‌ام که برای من ارسال شده است.
او می‌گوید: «نمی‌توانم به رسانه‌ها بگویم که آیا با آن موافقت کرده‌ام یا نه، قبل از اینکه ایران را در جریان بگذارم.»
@withyashar</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/withyashar/12186" target="_blank">📅 19:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12185">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ به آکسیوس: برخی ترجیح میدهند توافق را منعقد کنند ، برخی دیگر ترجیح میدهند جنگ را از سر بگیرند‌‌
@withyashar</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/withyashar/12185" target="_blank">📅 19:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12184">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هگست، وزیر جنگ آمریکا: ارتش ما عاشق غرق کردن نیروی دریایی دشمنه و من بهشون گفتم که تنها نیروی دریایی‌ای که درحال حاضر می‌تونید غرق کنید، نیروی دریایی ایرانه
@withyashar</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/withyashar/12184" target="_blank">📅 19:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12183">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ به اکسیوس:
شانس توافق یا جنگ 50/50 است. بعد از دیدار با نمایندگانم تصمیم میگیرم!
امروز با نمایندگان خود دیدار خواهم کرد و تا فردا(یکشنبه) تصمیم خواهم گرفت!
تنها توافقی را در رابطه با غنی سازی اورانیوم و سرنوشت ذخایر آن است را میپذیرم‌‌
یا چنان محکم‌تر از همیشه به آنها حمله نظامی می کنم که تا حالا مثل آن را ندیده‌اند، یا توافقی خوب را امضا می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/withyashar/12183" target="_blank">📅 19:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12182">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">العربیه : ایران پیشنهاد تعلیق غنی‌سازی اورانیوم بالای 3.6% را به مدت 10 سال ارائه داد @withyashar</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/withyashar/12182" target="_blank">📅 19:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12181">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">العربیه :
ایران پیشنهاد تعلیق غنی‌سازی اورانیوم بالای 3.6% را به مدت 10 سال ارائه داد
@withyashar</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/withyashar/12181" target="_blank">📅 19:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12180">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🤗</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/withyashar/12180" target="_blank">📅 18:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12179">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/withyashar/12179" target="_blank">📅 18:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12178">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مدیر شبکه افق: برای اولین بار اعلام می‌کنم که حضرت آقا تجمعات را از تلویزیون دنبال می‌کنند و از جمعیت زیاد تجمعات خوشحال هستند
@withyashar
یاشار : به عن آقا بگین پیج مارم ببینه
🤣</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/withyashar/12178" target="_blank">📅 18:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12177">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الحدث:ایران دو مسیر برای مذاکرات پیشنهاد کرده که با اعلام پایان جنگ و محاصره آغاز می‌شود.
ایران تأکید کرده است که در متن یادداشت تفاهم، به عدم تولید سلاح هسته‌ای متعهد خواهد بود.
ایران خواستار حفظ حق غنی‌سازی در هر توافقی شده است
ایران پیش از مذاکرات هسته‌ای خواستار آزادسازی دارایی‌های بلوکه‌شدهٔ خود شده است
@withyashar</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/withyashar/12177" target="_blank">📅 18:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12176">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/withyashar/12176" target="_blank">📅 18:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12175">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بعد از ممنوعیت پرچم شیر و خورشید در مسابقات جام‌جهانی توسط فیفا، نشریهٔ ایندیپندنت از مجاز شدن ورود پرچم فلسطین به ورزشگاه‌های جام‌جهانی خبر داد
@withyashar
😐</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/withyashar/12175" target="_blank">📅 18:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12174">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/withyashar/12174" target="_blank">📅 18:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12173">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/891feb9261.mp4?token=a549g4_X0tL6GFsDw2p4QJkWT67iUAtXYYHU0G4fCXmox1wa7IUYgL6XsGWawozAEcbXBlJIN7IJxp0bhLzcAS1AIY5rGqXWSQEb5zMqx2X_AJgzUmMeids4A-j0iWdA9-wu28Cwx_PBFJItekI0RIN7ff1Y6VJEBw9SlQ14qXlDOIckOCqg3O3Z5HvSvc72SHlVfrvJui0epVekVNoDItGj0nI_VZAPWB6bECXZBtbS2GXOAInrS1vhpk88zkH8GyJ90HMO5KQB_RUFzaM8tKLdRsmVMLHojDLmsJu0y522vCvtPhr2mMNWxfQs2lnWVurHyUmn7oYxM0N8rU7wBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/891feb9261.mp4?token=a549g4_X0tL6GFsDw2p4QJkWT67iUAtXYYHU0G4fCXmox1wa7IUYgL6XsGWawozAEcbXBlJIN7IJxp0bhLzcAS1AIY5rGqXWSQEb5zMqx2X_AJgzUmMeids4A-j0iWdA9-wu28Cwx_PBFJItekI0RIN7ff1Y6VJEBw9SlQ14qXlDOIckOCqg3O3Z5HvSvc72SHlVfrvJui0epVekVNoDItGj0nI_VZAPWB6bECXZBtbS2GXOAInrS1vhpk88zkH8GyJ90HMO5KQB_RUFzaM8tKLdRsmVMLHojDLmsJu0y522vCvtPhr2mMNWxfQs2lnWVurHyUmn7oYxM0N8rU7wBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورود جالب وزیر دفاع آمریکا، پیت هگست به وست پوینت معروف‌ترین آکادمی نظامی ارتش آمریکا، وی متولد ۶ ژوئن ۱۹۸۰ است و الان ۴۵ سال دارد.
همسر فعلی(سوم) او جنیفر راچت نام دارد؛ تهیه‌کننده سابق فاکس‌نیوز است. حدود ۴۰ سال دارد.
پیت هگست در مجموع ۷ فرزند در خانواده ترکیبی‌اش دارد از این میان، ۴ فرزند مستقیماً فرزندان خود او هستند:
۳ پسر از همسر دومش ۱ دختر از جنیفر راچت و ۳ فرزند دیگر (۲ پسر و ۱ دختر) فرزندان جنیفر از ازدواج قبلی‌اش هستند که با هم زندگی می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/withyashar/12173" target="_blank">📅 18:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12172">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ادعای العربیه: تهران در ازای پرداخت غرامت از سوی آمریکا به ایران، پیشنهاد بازگشایی تنگه هرمز را ارائه کرده است
@withyashar
🤣</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/withyashar/12172" target="_blank">📅 17:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12171">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اسرائیل همچنان درحال بمباران مواضع حزب‌الله
@withyashar</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/withyashar/12171" target="_blank">📅 17:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12170">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/12170" target="_blank">📅 17:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12169">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سخنگوی وزارت امور خارجهٔ ایران: این یادداشت تفاهم شامل ۱۴ بند برای پایان دادن به جنگ است و جزئیات آن طی یک بازهٔ ۳۰ تا ۶۰ روزه مورد بحث و بررسی قرار خواهد گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/12169" target="_blank">📅 17:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12168">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مارکو روبیو: مقداری پیشرفت در مذاکرات با ایران حاصل شده است.
همچنین این احتمال وجود دارد که آمریکا طی روزهای آینده دربارهٔ ایران چیزی برای اعلام داشته باشد.
@withyashar</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/12168" target="_blank">📅 17:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12167">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک مقام ایرانی به شبکه الجزیره: قطر نقش کلیدی در تهیه پیش‌نویس این یادداشت تفاهم ایفا کرد و بین میانجی‌ها و واشنگتن ارتباط وجود داشت
@withyashar</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/12167" target="_blank">📅 17:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12166">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حزب‌الله اعلام کرد که پیامی از وزیر امور خارجه رژیم جمهوری اسلامی دریافت کرده است که در آن آمده ایران به حمایت از این گروه ادامه خواهد داد و آن را رها نخواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/withyashar/12166" target="_blank">📅 17:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12165">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سخنگوی وزارت خارجه:  پیشنهاد ۱۴ بندی ایران که چندین بار رفت و برگشت شده و در خصوص بندهای مختلف آن دیدگاه‌های طرفین تبادل شده است و در این چند روز راجع به برخی نکات و عبارت پردازی‌هایی که راجع به آن اختلاف نظر کماکان وجود داشت بحث و پیشنهاداتی مطرح شد که همچنان برخی از آن در حال بررسی و اعلام نظر است.
@withyashar</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/withyashar/12165" target="_blank">📅 17:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12164">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/withyashar/12164" target="_blank">📅 17:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12163">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ادعای الجزیره: مقام ایرانی تایید کرد با واسطه پاکستانی به توافق رسیدند و منتظر جواب  آمریکا هستند! @withyashar یک مقام ایرانی به الجزیره گفت: این یادداشت تفاهم شامل پایان جنگ، لغو محاصره، باز کردن تنگه هرمز و خروج نیروهای آمریکایی از منطقه جنگی است.</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/12163" target="_blank">📅 17:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12162">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ادعای الجزیره: مقام ایرانی تایید کرد با واسطه پاکستانی به توافق رسیدند و منتظر جواب  آمریکا هستند!
@withyashar
یک مقام ایرانی به الجزیره گفت: این یادداشت تفاهم شامل پایان جنگ، لغو محاصره، باز کردن تنگه هرمز و خروج نیروهای آمریکایی از منطقه جنگی است.</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/12162" target="_blank">📅 16:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12161">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خبرنگار الجزیره در تهران:
شکاف‌های غیرقابل عبور در مذاکرات ایران و آمریکا وجود داره؛ لحظه بحران در راه است.
@withyashar</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/withyashar/12161" target="_blank">📅 16:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12160">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دیوید کیز، سخنگو و مشاور رسانه‌ای سابق نتانیاهو : 24 ساعت آینده تو ایران کاملاً حیاتیه یا هم شاید اصلاً نباشه، راستش خودم هم دقیق نمی‌دونم
@withyashar</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/withyashar/12160" target="_blank">📅 16:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12159">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رویترز:
رئیس تیم مذاکره‌کننده ایران به مقام‌های ارشد نظامی پاکستان توضیح داد که ایران قصد ندارد در مذاکرات با آمریکا هیچ‌گونه امتیازی بدهد.
@withyashar</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/withyashar/12159" target="_blank">📅 16:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12158">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOcocJuDisSRHFLfI0oUa5U9PH8uF80pIXUETk2wy5r7wu-Yjs7fbG6_sytcfeCjb43ELqsGwztfnksfruL4msbCmQU0iOFpIRb8Vj2Bab5aTHLJ3JLAb8EaBEwqFNioQGM8T48_cNMo0q9TU5IdwHhnWhZo6I1w09MfV4glghQFWpwaJKD3qN2Xz4mvh4-vYdiThRnwnZD62XGOr6YwWZP-eqNu0ShGWiqP1bFhUVTUgz0fLbNXaj93GEBBOyYmtIPMuLqkbuoT88X2Fnz_-XUX2CMD2Ea9N9LI9z3qocJN-rMGdxYtbiMhuP5-lrgUu5L3cXF0HejOK2LUnkf5Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث
@withyashar</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/12158" target="_blank">📅 16:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12157">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">Pishro x khalse x fadaei x tataloo x mj x ho3ein x erfan x sorena… – Minefield Remix ( IG @yashar)</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/withyashar/12157" target="_blank">📅 16:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12156">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/withyashar/12156" target="_blank">📅 16:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12155">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bchNM7Rj9BuRgsIGZGTseaQhZrKjSOM_EUsnEZifvop_kQdN82qCj8WKFbqESXD4FhvxdifAml6MQHuKPAiswv69gKIddmHoHLu4vtWIfVRVK8WoODpJCBLRxsDI_Gta-iIVufpPNW8FaB-bWu9uOKjIu-X5HvZD3GukqkSkn4FYJbcqYyeL1HlyEsGG6SLUTfZt1WkC1HGe9O7Lndv5cEC20SRJzUCXFF0urGlgDj2dssjzfv3DISW8X-xF-AzR15OlIZubvEIND8gl_fKmNwUZnC-pBmJuhVG2Pw-1nM3-SIwcpqR1m9RoQE-dd1xf_fL9PL62LsPurYTpiEnCeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیما دوم هیئت پاکستانی هم سیکتیر رو زد
😅
✌🏾
@withyashar</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/12155" target="_blank">📅 16:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12154">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ بیدار شد
😈</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/withyashar/12154" target="_blank">📅 16:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12153">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9df1f7b1.mp4?token=GPKbFgsNyJ6lyYLKkFJR6cuDz811tDBgi0nHBPdlmJOEYTBdeldv1pA8c1VLjMEIjwdjWyKNWNVR4yKGbpOnZw9oChhZNb4Ds1RwtG3IjRyq-v1-3k0YXu_aMuKUP0j3v3-Trea-MJmrDcN7hdC567aWLBQII8jBBEczd4Fm9M0QqDUdUalvHWOJ1G0KII8PEKpwf8cRSmGS8vH39qNq7e3fzp7HpxKa3_XNci_78uu6i4Zwe41fqOkKXhc5AJfntUwfCOSeyI4zI7gKxW9NZDZcDeYogA0gxdTQ1Q04hlu_QxMyT25Yi35-1NcATIu6PBrAqP43eiH09FFPwtThHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9df1f7b1.mp4?token=GPKbFgsNyJ6lyYLKkFJR6cuDz811tDBgi0nHBPdlmJOEYTBdeldv1pA8c1VLjMEIjwdjWyKNWNVR4yKGbpOnZw9oChhZNb4Ds1RwtG3IjRyq-v1-3k0YXu_aMuKUP0j3v3-Trea-MJmrDcN7hdC567aWLBQII8jBBEczd4Fm9M0QqDUdUalvHWOJ1G0KII8PEKpwf8cRSmGS8vH39qNq7e3fzp7HpxKa3_XNci_78uu6i4Zwe41fqOkKXhc5AJfntUwfCOSeyI4zI7gKxW9NZDZcDeYogA0gxdTQ1Q04hlu_QxMyT25Yi35-1NcATIu6PBrAqP43eiH09FFPwtThHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/12153" target="_blank">📅 16:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12152">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromam</strong></div>
<div class="tg-text">یاشار تو خرم اباد مردم جمع شدن دارن شعار میدن
چهارمحال بختیاری و لرستانم همینه</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/withyashar/12152" target="_blank">📅 16:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12151">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAdmin_suport</strong></div>
<div class="tg-text">شهرهای لرنشین یکی پس از دیگری دست به تجمعات اعتراضی زدن. فامیل داریم تو دورود که اونا هم کم کم دارن میان</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/withyashar/12151" target="_blank">📅 16:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12148">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Minefield Remix ( IG @yashar)</div>
  <div class="tg-doc-extra">Pishro x khalse x fadaei x tataloo x mj x ho3ein x erfan x sorena…</div>
</div>
<a href="https://t.me/withyashar/12148" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/withyashar/12148" target="_blank">📅 16:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12147">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">قدرت باورنکردنی سازمان اطلاعاتی موساد باعث شده است که نتانیاهو جزییات مذاکرات را از تهران متوجه شود نه واشینگتن
@withyashar</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/12147" target="_blank">📅 15:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12146">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پس امشبم بیداریم شانس هست
😂
🙌🏾</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/12146" target="_blank">📅 15:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12145">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3SLmRYc0hNqzVfhcBOLSwc0KNdLtpi13zf2vtqHrqIWA1jxrHDIgSRgzYWcU0JOpqKUb8abZ_p4XyG-GS4U-YXPiFes4emPoqxwmCMg3h3ZKlbmydtxVn5TF4_eK0yjVNZZ2SYEXoHOkODQYDYPuNr2mQ3h1XA_ddtXEoZLbNOlGPO-V8QSRH4EvkMJAWd6rBe4Bx81liTSXi51uvTJcPxHD5q3-OKTWuHZgc-VToLU0W_Ty_OWIHG0xkh8ErK_0aH5jaFNKpfBlI9sLIdGWgxqpDyqiTTEZkYf1fgRQGjHqquuU_YA8C-MExgCsmx_CVZH9xpgSeE_dAPU0KzcLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده ارتش پاکستان تهران را ترک کرد
@withyashar</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/12145" target="_blank">📅 15:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12144">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">@withyashar
تحلیل پوزیشن الان</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/12144" target="_blank">📅 15:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12143">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31857c4cba.mp4?token=OX69W9kjIpP4gGdk3n_n61sU81X_w9Nxe--1lRwDMqgeURWc0X74C5B57sicO-TctIIkJ2neV6KHU9dJhwF3dLS6BwZCzes0_w7cWpqJ8CSIc1JgEAjCWxh0bHwGll59kPm1sFDnhopsAw37HKvEsUS9Cy8dMqzQNKsIB5QLl3_059w4U3ksizee471ghdzNhhlq4mZSC4d_xhdVXXKuoMyzyaMdXs-p791lTNvOxTAWwQE0QixVOxwE1CmmpAjW8TUparLlLi6a4fyRRejK_OFO0u6Sdsj7khg3eMmDwzab6i4RGeJSP2S1hH4N5S2LvD8bXOPRQlg25Zo1JiqBOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31857c4cba.mp4?token=OX69W9kjIpP4gGdk3n_n61sU81X_w9Nxe--1lRwDMqgeURWc0X74C5B57sicO-TctIIkJ2neV6KHU9dJhwF3dLS6BwZCzes0_w7cWpqJ8CSIc1JgEAjCWxh0bHwGll59kPm1sFDnhopsAw37HKvEsUS9Cy8dMqzQNKsIB5QLl3_059w4U3ksizee471ghdzNhhlq4mZSC4d_xhdVXXKuoMyzyaMdXs-p791lTNvOxTAWwQE0QixVOxwE1CmmpAjW8TUparLlLi6a4fyRRejK_OFO0u6Sdsj7khg3eMmDwzab6i4RGeJSP2S1hH4N5S2LvD8bXOPRQlg25Zo1JiqBOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/12143" target="_blank">📅 15:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12142">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ادعای خبرنگار الجزیره: یک شخصیت بسیار بلندپایه منطقه‌ای از ایران دیدار کرده است
علی هاشم در پیامی در شبکه اجتماعی ایکس مدعی شد که ـیک چهره بسیار برجسته منطقه‌ای، بی‌سروصدا از تهران بازدید کرد تا آنچه را که بسیاری اکنون «شکاف‌های غیرقابل عبور» می‌نامند، پر کند.
@withyashar</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/12142" target="_blank">📅 15:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12141">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تماس تلفنی امیر قطر با ترامپ درباره کاهش تنش‌ها در منطقه
دیوان امیری قطر از تماس تلفنی امیر این کشور با ترامپ ،رئیس جمهور آمریکا خبر داد.
دیوان امیری قطر افزود که امیر این کشور درباره  تلاش‌ها برای تحکیم آتش‌بس و کاهش تنش‌ها در منطقه صحبت کرد.
@withyashar</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/12141" target="_blank">📅 14:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12140">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">قالیباف در دیدار امروز با عاصم منیر، فرمانده ارتش پاکستان:
جمهوری اسلامی از حقوق خود عقب‌نشینی نمیکنه و به طرفی که صداقت نداره اعتمادی نیست.
جمهوری اسلامی در حالی پای میز مذاکره بود که آمریکا جنگ رو آغاز کرد؛ در صورت شروع دوباره درگیری، پاسخ نیروهای مسلح کوبنده‌تر و تلخ‌تر از گذشته خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/12140" target="_blank">📅 14:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12139">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">العربیه: عاصم منیر پیام تهدیدآمیز آمریکا رو به تهران برد.
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/12139" target="_blank">📅 14:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12138">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">احتمال وقوع طوفان گرد و خاک در تهران
اداره‌کل هواشناسی استان تهران:
از یکشنبه تا چهارشنبه (۳ تا ۶ خردادماه) در مناطق شمالی استان تهران در بعضی ساعت‌ها وزش باد نسبتا شدید تا شدید همچنین در نیمه جنوبی، مناطق غربی، مرکزی و ارتفاعات در بعضی ساعت‌ها وزش باد شدید تا خیلی شدید پیش‌بینی می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/12138" target="_blank">📅 14:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12137">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">moamelegari-trump(@withyashar).pdf</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/withyashar/12137" target="_blank">📅 14:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12136">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/12136" target="_blank">📅 14:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12135">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الحدث : آمریکا به تهران پیام داده اگه توافقو رد کنه، عواقب بدی در انتظارشه
@withyashar</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/12135" target="_blank">📅 14:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12134">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e08d6a873.mp4?token=nsP0J1Dhbg_1xdrz6rgWQAZUSux5LunEW3e_JfoZh4y0mROLq15aPDPPtc9XqoSGD0oh-UFUkmLtspRzBFmlKRk8FVc-_A0KUGMOLNfqZW-jopdRXBWYdcNpj9Khow9zb9n1gWvAN-FUdSUIlRBRZO9lEnqP35yqtBkZwTjv0FAQbUVGbIpHfHkoC4qrTdRoTCqZ4kizsxofDMT53VNXavVYNpMp7-vsSNPleMXnRG8wKLWfuw3fcqiD5HqSp0nZM3z772XXIKel7iNGViWlN8Y3nbvR7L5awuU4vC6oA6INVnsiFMq9xoMcTXMi01TH5yaBTt7-7r4j_tIGa4XluQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e08d6a873.mp4?token=nsP0J1Dhbg_1xdrz6rgWQAZUSux5LunEW3e_JfoZh4y0mROLq15aPDPPtc9XqoSGD0oh-UFUkmLtspRzBFmlKRk8FVc-_A0KUGMOLNfqZW-jopdRXBWYdcNpj9Khow9zb9n1gWvAN-FUdSUIlRBRZO9lEnqP35yqtBkZwTjv0FAQbUVGbIpHfHkoC4qrTdRoTCqZ4kizsxofDMT53VNXavVYNpMp7-vsSNPleMXnRG8wKLWfuw3fcqiD5HqSp0nZM3z772XXIKel7iNGViWlN8Y3nbvR7L5awuU4vC6oA6INVnsiFMq9xoMcTXMi01TH5yaBTt7-7r4j_tIGa4XluQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنتاگون اسناد جدیدی از ufoها منتشر کرده که مانند یک انسان پرنده است و بسیار شبیه شخصیت “مشعل” در چهار شگفت‌انگیز در کمیک معروف هست.
@withyashar</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/12134" target="_blank">📅 14:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12133">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTemEkRO7Q3v2J5iui2BGSrtsUkkV0AsSoV8QNTuV7_AvkfAqeOTVDSp4wagkfAT4FfVzbWdOKDEShzjvJHk-2hxrf9nr8Ak9ITE4pjvHrFe8JRczGUdrc3MgizEydJNJm_sbS5U9zWyjvC2rinQGIGLCVMgq42EZbZgnri5NqMLDV8psy-iDbYAPuZzsV29MCh_e-JAlfEch5rYMRQ483AITBXF3Zlo8Dtu-jAYccLtiifHcxMRkMGd7AE1duLRzjcrxttr2pyT9_mY7YbKHP1g73eiG61aKpBxH7oRtTD-8a_7FOladnMwTUVsolV34bYS33UaJ-eK7ArpSjDsRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاصم منیر، فرمانده ارتش پاکستان با
زرشکیان
دیدار کرد
@withyashar</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/withyashar/12133" target="_blank">📅 13:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12132">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/12132" target="_blank">📅 13:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12131">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یک مقام دیگر پاکستانی به تهران می‌رود.
😒
یا دیشب اگه رفتن دارن بر میگردن جت نیروی هوایی پاکستان GLF IV SP reg J-755 @withyashar</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/withyashar/12131" target="_blank">📅 13:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12130">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Klor0zSBvtfRa9vxnY2PyNRytGGUkX0jzjBmF8UDnl9y8ERWFjo9jSj7cmkw_HZTCavRxcRaLEgBBW-CLTyaGUFw7BXd3n_PZ0iNLmeAjXt84u_IJq9FENvpI7KiKBwOjq7L-ce9W6A7nXiGXMiYIUnxa5vRBx46a0iJbhL-DPf3FfOeNDrn8YxLK30SC2M6IDIXAN4skqZngWv8_jdKBOIDzPlzjqmIS62CV-TskLx-jB55TRO_89hrIPfeLW2b6sJ--mVM2Y0WGu1mOCBdy0d-RjjHbCE5xdKdMaXXQGwuGFvqGh740OuTk138arcbV-2L__KWBTt-9UfVRFfJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاصم منیر، رییس ستاد کل ارتش پاکستان با محمدباقر قالیباف در تهران دیدار کرد
@withyashar</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/12130" target="_blank">📅 13:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12129">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نورالدین الدغیر خبرنگار الجزیره در تهران: وساطت‌ها بین تهران و واشنگتن به مرحله‌ای رسیده که یکی از سران منطقه‌ای به طور مستقیم برای پر کردن شکاف‌ها وارد عمل شده.
ظهور قطر در این لحظه حساس به طور مستقیم و بر اساس اطلاعات و منابع موجود، نه صرفاً به عنوان نقش کمکی برای پاکستان، بلکه به عنوان نقش محوری است.
منبعی می‌گوید که احتمال دارد یکی از میانجی‌ها به واشنگتن سفر کند.
@withyashar</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/withyashar/12129" target="_blank">📅 13:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12128">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/withyashar/12128" target="_blank">📅 13:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12127">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">@withyashar
به در میگم دیوار بشنوه</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/12127" target="_blank">📅 13:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12126">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHd</strong></div>
<div class="tg-text">یاشار جان درود و خسته نباشید.
به این رفیقمون بگو جمله ی سر سفره ی پدر و مادر بزرگ شدن یک استعاره از تربیت و پرورش درست و اخلاقیه ، ربطی به حضور یا عدم حضور خانواده نداره
انقد همه چیز رو فلسفی نکنن
این عادت چپ ها و گلوبالیست ها هستش</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/12126" target="_blank">📅 13:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12125">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 50K · <a href="https://t.me/withyashar/12125" target="_blank">📅 13:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12124">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/withyashar/12124" target="_blank">📅 13:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12122">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/withyashar/12122" target="_blank">📅 13:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12121">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSaya</strong></div>
<div class="tg-text">درود و وقت بخیر
سر سفره پدر و مادر بزرگ شدن یکی از جملاتیه که باید از بین ببریمش اگه ممکنه کم کم دیگه تکرار نکنید چون الان الگوی خیلیامون قرار گرفتین
🌹
شخصی که بچه طلاقه یا بی سرپرست می‌تونه خیلی بهتر از اونی باشه که کنار پدر و مادرش بزرگ شده
🤍</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/12121" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12120">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">منبع ارشد ایرانی به الحدث: آنچه تاکنون مطرح کرده‌ایم برای ایالات متحده قابل قبول نیست
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/12120" target="_blank">📅 13:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12119">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شهباز شریف نخست وزیر پاکستان امروز شنبه وارد شهر هانگ‌جو واقع در شرق چین شد و دیدار رسمی چهار روزه خود از چین را آغاز کرد.
@withyashar</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/withyashar/12119" target="_blank">📅 12:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12118">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">منابعی به اسکای نیوز عربی گفتن که میانجی پاکستانی موفق شده بر مانع پرونده هسته‌ای ایران غلبه کنه
@withyashar</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/12118" target="_blank">📅 12:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12117">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">علی کریمی : ببینیم کی قبلا چیکاره بوده و الان چیکارتست و دنبال چی هست؟!
ببینیم که چند چندیم؟!
بببینیم کی برای پول و صندلی مبارزه کرده، کی برای آزادی ایران؟!
این گوی و این میدان
@withyashar</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/12117" target="_blank">📅 12:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12116">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q55pRvyhp3erf6uTg3FCPTcWmkQkNDUSlNY563gisdoF7JQH-lBq-LUbhLr4w1Oht0PVhu9Jo5kQQGwflOhqJo72iu5KvNB3SaXrVc-WOWKnXa-bdlLxHuUSdHvjkh3rgN6N9w2O6Bj7MMNKiy3Z3sWoQq9KvDmkW5RoQjAeAz2R3rVzgQWoNQDO6p0UAAPJc-YDE8demJji1pXksqcfxWG2-uHXn6n4NIphvumdLJNB0hJXmtPKqXkkQ7-rgn-U37HyBa8ThZf_LgW3OneQwTwM3No2nzBDU26n2w4wfH0X9ZDJe2mFP5Rdr39CKz6Kceq5q6QisG_nREZyhLsTGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیرا شریفی مقدم:  آماده رفتن به جنگ هستم
@withyashar</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/12116" target="_blank">📅 12:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12115">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارشهای تایید نشده : ویزای شجاع خلیل زاده احسان حاج‌صفی و مهدی طارمی به دلیل حمایت از سپاه تروریستی پاسداران رد شدن @withyashar</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/12115" target="_blank">📅 12:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12113">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حمله ارتش اسرائیل به یک مجتمع بزرگ زیرزمینی حزب‌الله در اعماق لبنان و جنوب این کشور
@withyashar</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/12113" target="_blank">📅 12:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12112">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUL1fD_JWpVe5jAWigHDvV1NrF9FQ1-2qauqE6VUxXvaW5RG2dgdO0DsttrBLiy4-Fy0YvLK2bCedcS-s1_HoLH2f-7z_bxE-3anf2qASTA6RwPkKfCfgRfDx8s33s11kreImmWCChDQHlpGcslUXNM56j7IkS_wF6P4sn4awbWGHrudrq_U_nde9XDYNQUXQWkD1dQNiyJnGv_fMH37mQ-cKmXEO8fSRVFR_WwOZ2LqLcUfkw5O-NqYOpaG7OClmKeH-SjS2GjC0mTwJYBOJq8Ka7MlDQt5aIEqbnC26OAtAIXE9UgMCafvTG71zTvDNUdDE1hqRurSPKg1rXEC5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام دیگر پاکستانی به تهران می‌رود.
😒
یا دیشب اگه رفتن دارن بر میگردن
جت نیروی هوایی پاکستان GLF IV SP reg J-755
@withyashar</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/12112" target="_blank">📅 11:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12111">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ادعای کانال ۱۳ عبری به نقل از نیویورک‌تایمز: ترامپ اسرائیل را از مذاکرات با ایران کنار گذاشته است.
@withyashar</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/12111" target="_blank">📅 11:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12110">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سناتور راجر ویکر:  «الان تو مقطعی هستیم که می‌تونه میراث سیاسی ترامپ رو مشخص کنه. غریزه ترامپ این بوده که کاری رو که تو ایران شروع کرده، کامل تموم کنه؛ اما بهش توصیه‌های اشتباه می‌شه تا دنبال توافقی بره که حتی ارزش کاغذی که روش نوشته شده رو هم نداره. فرمانده کل نیروهای آمریکا باید اجازه بده ارتش حرفه‌ای آمریکا نابودی توان نظامی متعارف ایران رو کامل کنه و تنگه رو دوباره باز کنه. ادامه تلاش برای توافق با حکومت ایران ممکنه نشونه ضعف تلقی بشه. باید کاری رو که شروع کردیم، تموم کنیم. وقت اقدام گذشته.»
@withyashar</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/12110" target="_blank">📅 11:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12109">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گزارشهای تایید نشده : ویزای شجاع خلیل زاده احسان حاج‌صفی و مهدی طارمی به دلیل حمایت از سپاه تروریستی پاسداران رد شدن
@withyashar</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/12109" target="_blank">📅 11:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12108">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">روبیو وارد هند شد
وزیر امور خارجه آمریکا امروز با هدف تقویت همکاری‌ها با هند وارد این کشور آسیایی شد.
@withyashar</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/12108" target="_blank">📅 10:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12107">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کانال ۱۲ اسرائیل: درنهایت برآورد اسرائیل اینه که هیچ توافقی انجام نخواهد شد و ارتش دفاعی اسرائیل برای شروع موج جدیدی از حملات به ایران طی روزای آینده آماده می‌شه
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/12107" target="_blank">📅 10:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12106">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شبکه CBS به نقل از چند منبع آگاه از برنامه‌ریزی‌های نظامی اعلام کرد که دولت ترامپ در حال آماده شدن برای دور جدیدی از حملات علیه ایران است، هرچند هنوز به تصمیم نهایی نرسیده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/12106" target="_blank">📅 09:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12105">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سخنگوی وزارت دفاع ایران: ترامپ چاره‌ای جز پذیرش خواسته‌های ایران ندارد، در غیر این صورت متحمل شکست‌های بیشتری خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/12105" target="_blank">📅 09:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12104">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بزرگترین نمایشگاه هوایی نظامی بریتانیا لغو شد، زیرا گزارش شده است که از این فرودگاه برای ماموریت‌های مرتبط(احتمالا حمله) با ایران استفاده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/12104" target="_blank">📅 06:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12103">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">از دیشب تا الان نخوابیدم سربازم الانم دارم میرم سر شیفتم  جنگ قبلی ام توی شیفتم شروع شد اموزشیمم جنگ 12 روزه بود دعا کنین زنده برگردم
🥲
💔
😂</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/12103" target="_blank">📅 06:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12102">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromᴍᴏʜᴀᴍᴍᴀᴅ</strong></div>
<div class="tg-text">از دیشب تا الان نخوابیدم سربازم الانم دارم میرم سر شیفتم  جنگ قبلی ام توی شیفتم شروع شد اموزشیمم جنگ 12 روزه بود دعا کنین زنده برگردم
🥲
💔
😂</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/12102" target="_blank">📅 06:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12101">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/12101" target="_blank">📅 05:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12100">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">لارا لومر از معتمد ترین افراد نزد ترامپ ، خبر آماده شدن آمریکا برای حملات دوباره رو ریتوییت کرده.
@withyashar</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/12100" target="_blank">📅 05:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12099">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پست دن اسکاوینو از مشاوران ترامپ در شبکه اجتماعی X @withyashar</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/12099" target="_blank">📅 05:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12098">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsphYcsSLPmspkRGrFXBtbSQfPQEGRyBUDlGFky3p_9Mlx8BQn-Bpa151FrEpNBT_cSb0wP7sZI2xmPrQhrarozrlW_idZ4rzscxBzBYCumYuRlasG3X7pvuNlnjznGHYz0qD48TKeeUq2zPOarV4tucuQCaat4ja7cfCU9ssfwvUuSY1pvXqgUoz6P3V8rzgxCRvzMfsmmM1YnQAwxGS89B2GNxOBk1imv1VMgwu-rio3TG60Y5S_rimGwBevY5RJVypVD6Aveg7i7YUngUw4qjBhW-Q8AeVSzk5BgDlm7BkuWjD2V0WY069oecuKA7TQyf9-oF1eP_pGhhCo-nCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست دن اسکاوینو از مشاوران ترامپ در شبکه اجتماعی X
@withyashar</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/12098" target="_blank">📅 05:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12097">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تمام کنفرانس های خبری کاخ سفید لغو شد
@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/12097" target="_blank">📅 05:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12096">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خوب تا ۵ ایران نزد میریم برای ۹ صبح به بعد ، حالا خوابمم نمیبره
🥴
🤣</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/12096" target="_blank">📅 05:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12095">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/12095" target="_blank">📅 04:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12094">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/withyashar/12094" target="_blank">📅 04:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12093">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/withyashar/12093" target="_blank">📅 04:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12092">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/withyashar/12092" target="_blank">📅 04:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12091">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzNqpRgcJRb47FOJyB4X6JaZ7DLLyJzNzQiqU4E5FOkbPttSv95yrsvjDfg9tXk1lJuQASpT8ybthqO61vOIvO2261wQt85nmDGE9KpdB2zfiOUnTluixtWqCfcsDhNV4Bga4BvG3CKCozo_AakC6oAd58P07REHm7pFdbYjpU6L8QHoLGInItJAydJsMHRexeMxOAXgX2XLz-l1TfQZOV3q1BguBxVFGVfXZdTOO_Bu34rVphTT98U33K2dctMJbyoPX_dbQtne8F32IOCKUHIz4OVasSlDqSf3Hbw3Vna7SzNawhZLmvh1stq5BrsWpomOArke7FaOk1MHobd64g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/12091" target="_blank">📅 04:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12090">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/12090" target="_blank">📅 04:16 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
