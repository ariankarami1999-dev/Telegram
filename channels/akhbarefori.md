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
<img src="https://cdn4.telesco.pe/file/qM9e5ac5KFnz9R3L3jqYpuXU5poVMLGVtrB7Qxt4Ny2AKy66TQ8Q8BIGMnbA8K_ANn4dv4rltuQzHV4Lf3_Zy5XekgSmGmOhJ6hHJf5xFAa_TvhcnHAU7pKC2eQWMcBAwNCiIzO_a-qlRpAXZaQsL-8iKuuGJcxRH988yT3z0fieW_kRiHVhOnlHY5AK7jbO2rszvLp3ZlbRXPbDJpGqO4qVm2aUEi_DzQuzMpNimFEgwMvJ1RUSgttNnf1OywZmzr9e3b3nBdErXZA6PZgcnt9Gur1JLtxHHE-Wx6BRcGhOL5IL22mCwdh9C3r2J6lqUz39yvWqClx-Ed2RxnIv3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.33M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 09:59:19</div>
<hr>

<div class="tg-post" id="msg-662827">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ll0ujVZjuPOYRoqQEDG0F61au3cx6AL7PeBtbdQdYWAVbr1vcvGwEDzycGsfExBEQo-F1m7ELErRqZOVhEmqh6sYb4kBEFqymUENIrXdTXAPjzfudCMiaU6sh7Wjl9RARggIuiUagu0Ucf5C1a0_u0UL9EKkBOgJtdCEvS2_-KHTsbArM5vUFH5PM5a6RNsYPwKiSgZx9eWtZysUNWCey_2IbN0wBbpXEUEU2ibFp_uhmPAh1gUyQZo0gmp6Ij9_TWxTe021aW7cMXZ-6VO7MdqMwrdvE0d4FcRYXd7c89tn1hjgkiSUgLUAe2tgrcA8YSC4beEXdEhZ9EZV8nevCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
انتقاد ترامپ از پمپ بنزین‌های آمریکا: قیمت را با کاهش بهای نفت پایین نمی‌آورند
ترامپ:
🔹
شرکت‌های بزرگ نفتی قیمت‌های خود در پمپ بنزین‌ها را به اندازه کاهش شدید قیمت‌هایی که برای نفت می‌پردازند، پایین نمی‌آورند.
🔹
این قیمت‌ها مثل سنگ سقوط می‌کنند! به عبارت دیگر، مشتریان «سوءاستفاده» می‌شوند.
🔹
من به وزارت دادگستری دستور داده‌ام فوراً به این موضوع رسیدگی کند. قیمت بنزین باید خیلی سریع‌تر از چیزی که من می‌بینم کاهش یابد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/akhbarefori/662827" target="_blank">📅 09:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662826">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔹
رژیم صهیونیستی در تدارک عقب‌نشینی از مناطق جنوب لبنان
🔹
رسانه‌های صهیونیستی از آمادگی ارتش این رژیم برای عقب‌نشینی از مناطق محدودی در جنوب لبنان و استقرار نیروهای ارتش این کشور در آنجا خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/662826" target="_blank">📅 09:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662825">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFfTGTQ9oYSn0XrcAsFX4YgTZk2sjNSGnYhV93asSQuUfINkKn22rYVl71nvRtbFIUTeEPuEMkRhMW6BzrCSVsYq9OTLmfJmWGNz661JYcGGWnAqIUrTiVKsFBxfRMm0vFVYOryRoKhQ39g1qySMQcIit6EQpPXyZkvcKdNrV94XMuCBosQjqr-5mAZKoYi7dwXMRjY4bG4MHZkOQp7KoQ0lCy9L6qOQg7oFGjxsOlNYeifV7O7ck4DgGRLYjqTUsNlsckoif-MqHctl5d0u00dEguzY6XlxjopF6gHkncA3FMGFhe3mSkyMhHBQf5kV-JESMAJxurLGm2OZfPraSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پوستر فدراسیون فوتبال ایران برای بازی بعد تیم ملی مقابل مصر
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/662825" target="_blank">📅 09:36 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662824">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGAacXbu4YB0q2vP-TV-lRRecd16aRCZdPNeWQjgw5CoNnpk97Zqqls8sGXcHLzDgDdW-FDZwsWmejYSigytspg-qAzrMXsyiAm3efkRGKgC-M__lon29iLOJNfw6IV0RLlMnhEtSvCkpwGV5TBxog-zeJOIXWC72TsbVpl4LWo7MApQMSsnQRw3Eb175kWbBURWaimdRu2ITDu8FjF4WnKpOORAb_6jv0CxTF8xn4uoyLu3RUbdTX3_8yx8iQBXaLLUlLJGdJ6p7908VqYX-jFsI84DUYa1L_rzQcEqQToGzgV4eoGLw7KUOW9eS7rAs1mLpMevCdWFdjVecnt0YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
جدول ۱۲ گانه مرحله گروهی جام جهانی ۲۰۲۶ پس از پایان دور دوم مسابقات
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/662824" target="_blank">📅 09:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662823">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔹
مکرون: برای تثبیت آتش‌بس در لبنان، نیروهای رژیم صهیونیستی باید از این کشور خارج شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/662823" target="_blank">📅 09:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662822">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔹
نخست وزیر قطر به فایننشال تایمز: مذاکرات سوئیس (ايران - آمریکا) زمینه را برای مذاکرات دائمی حل و فصل بحران فراهم کرد و کار تازه آغاز شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/662822" target="_blank">📅 09:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662821">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf527ff369.mp4?token=MuSsv0lhnG1pbJ8Q_zdLOPCAUMaVPEFFykJaYaIIz38pOzgquT-MArKwb6J0d7zV_FE7CANaaxn4q3Wj8g7UQFt6cScWEftm6_0xfYz11u28OkVIGVHjI49zmuMX2kOXP8SKRXmAyjVXOvUeyUrjpKh8LiNM6pUalbRn2CIuGAoK8U0V086pQfRr4x0AmBaPdRPo9v7H_JwtZtWRFS4egqRmQXRyGNz4jbiL5iLuGB2Q2ZQxAko36yMftEiTgvaeGZiLzjbnldL2j3nNFbn7W4Zdwy7X8wEydpF_u-EanpnsKUSrHsdOazbNyU951k_BgW9CvhOSc7uuX5nxe-kOWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf527ff369.mp4?token=MuSsv0lhnG1pbJ8Q_zdLOPCAUMaVPEFFykJaYaIIz38pOzgquT-MArKwb6J0d7zV_FE7CANaaxn4q3Wj8g7UQFt6cScWEftm6_0xfYz11u28OkVIGVHjI49zmuMX2kOXP8SKRXmAyjVXOvUeyUrjpKh8LiNM6pUalbRn2CIuGAoK8U0V086pQfRr4x0AmBaPdRPo9v7H_JwtZtWRFS4egqRmQXRyGNz4jbiL5iLuGB2Q2ZQxAko36yMftEiTgvaeGZiLzjbnldL2j3nNFbn7W4Zdwy7X8wEydpF_u-EanpnsKUSrHsdOazbNyU951k_BgW9CvhOSc7uuX5nxe-kOWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
نخست‌وزیر پیشین رژیم صهیونیستی، نفتالی بنت: جنگ طولانی‌ برای سال‌ها کاملاً برخلاف مفهوم استراتژیک اسرائیل است. این با اسرائیل سازگار نیست
🔹
ما کشوری کوچک هستیم، این اقتصاد را فرسوده می‌کند، نیروهای ذخیره را خسته می‌کند و جایگاه بین‌المللی ما را تضعیف می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/662821" target="_blank">📅 09:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662820">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbb7652a96.mp4?token=DBl7APyEUBLqnQpnzN03Sw2f9V6zl7xv1zIsSqyPUtD9OJXlnZ6oSffFLMuTZnpuJ13_gZdzdqYFBnAZRYxpc2-xnPGRpbzOrDSGUGMC7DEPRUn4vNffZOIBNx20YU41UizAN59Yqq0380BjaOTPaFLvwXGnHgb8F5CH0QUCMfrQ4GrKiJGP0RyuDBDhPaEghtkumns6jMpFcBUyxofNnYpSHab4gbJe2I3yC7bZVjIkbfVDXklyVxBVwsXRHH5cgRYo2GahtnRNSzFIzW0Zf423kOiDJ04FqRhM83cntitB42V3eQYqIiamlbhAinaJU7DMXQEe0IEyFed4B2bb6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbb7652a96.mp4?token=DBl7APyEUBLqnQpnzN03Sw2f9V6zl7xv1zIsSqyPUtD9OJXlnZ6oSffFLMuTZnpuJ13_gZdzdqYFBnAZRYxpc2-xnPGRpbzOrDSGUGMC7DEPRUn4vNffZOIBNx20YU41UizAN59Yqq0380BjaOTPaFLvwXGnHgb8F5CH0QUCMfrQ4GrKiJGP0RyuDBDhPaEghtkumns6jMpFcBUyxofNnYpSHab4gbJe2I3yC7bZVjIkbfVDXklyVxBVwsXRHH5cgRYo2GahtnRNSzFIzW0Zf423kOiDJ04FqRhM83cntitB42V3eQYqIiamlbhAinaJU7DMXQEe0IEyFed4B2bb6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اعتراض آلبانی‌ها به طرح جرد کوشنر برای تبدیل یک جزیره به یک اقامتگاه لوکس و تفریحی همچنان ادامه دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/662820" target="_blank">📅 09:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662819">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdCYWgC282n4qlMUGZrHj8DQzdAbBTpw0fwtvjIH1z3BJm2rKVjN2TuFQaSvYihrJQl18Y4n3JOYSLyy30EfxjqFdt37z_tyI9Yu5WF9iMUPH-rFpP6yu8ZLd8mL0BS_bYCx3wtLrEtnQejyYpDwpJ68R2HCDlt_DEi1yUIUE2zIlVA5rdIu9iAqwdD5yqAYRIJTl9ZoayGRds7frKVQjEZi5a65fICkmrzIo1A_XPlRnasFRe7X4p5Z1EdCCfNClSXfndkSZO-oBR1iVhtVLrW1C1OZAvL00Kf8DyItUULZB98L0Lb90tifjequxyGMZ2pc36P7flYwXX79Oc3TyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه مسابقات روز چهاردهم دور گروهی
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/662819" target="_blank">📅 09:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662818">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔹
ترامپ: همه از نتانیاهو خسته شدند
🔹
افشای محتوای یک تماس تلفنی محرمانه نشان می‌دهد دونالد ترامپ در اوج مذاکرات پایان جنگ غزه، با لحنی تند نتانیاهو را به تلاش برای برهم زدن توافق متهم کرده و حتی تهدید به قطع روابط کرده است؛ روایتی که از شکاف عمیق میان دو متحد سنتی پرده برمی‌دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662818" target="_blank">📅 09:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662817">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔹
اکونومیست: نتانیاهو در نهایت ناچار است با توافق تهران-واشنگتن کنار بیاید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/662817" target="_blank">📅 08:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662816">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔹
نیروی دریایی کره شمالی به سلاح هسته‌ای مجهز می‌شود
🔹
رهبر کره شمالی، اعلام کرد که برنامه تسلیحات هسته‌ای نیروی دریایی این کشور «دقیقاً طبق مسیر برنامه‌ریزی شده» در حال پیشرفت است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/662816" target="_blank">📅 08:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662815">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/490b048b6f.mp4?token=JnhPiXtdzrpXI0L-Ohp_jGMltDwqS3yoALlMj5wv0hTFW5nhAabe2ZO4CWzJ5usroYWbsTiIPpKRsn6E8di-ps9t8T7CdaiL0ccfvC_ybQtuC3J_08sbDO5YfhEqf0XPE5qUGLhbP753F36UIv0vQQRny5UlCwIfv8P3KekxtXlPwPcGaDUise6DT8jHwwPOtezMJ2wSzUgv2504cSsf2uWnkbMasE6IsOebZ0kKtDZsah1eTsInEOGcZ2Pl3UySBk0oeMfXiEZeGEsYaLbuFuXGJzAcjCF-OFw7iEAjJBRgOCNBJieNscVZLgnagv8yyWS_iSSA6yO1i7VXyunR2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/490b048b6f.mp4?token=JnhPiXtdzrpXI0L-Ohp_jGMltDwqS3yoALlMj5wv0hTFW5nhAabe2ZO4CWzJ5usroYWbsTiIPpKRsn6E8di-ps9t8T7CdaiL0ccfvC_ybQtuC3J_08sbDO5YfhEqf0XPE5qUGLhbP753F36UIv0vQQRny5UlCwIfv8P3KekxtXlPwPcGaDUise6DT8jHwwPOtezMJ2wSzUgv2504cSsf2uWnkbMasE6IsOebZ0kKtDZsah1eTsInEOGcZ2Pl3UySBk0oeMfXiEZeGEsYaLbuFuXGJzAcjCF-OFw7iEAjJBRgOCNBJieNscVZLgnagv8yyWS_iSSA6yO1i7VXyunR2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
​​
ای ساقی لب‌تشنگان، ای جانِ جانان، ای سقای طفلان و مظهر وفاداری...
🔹
هر جا نام تو می‌آید، عطش رنگ امید می‌گیرد و دل‌ها به یاد ایثار و مردانگی آرام می‌شوند.
🔹
السلام علیک یا اباالفضل العباس(ع)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/662815" target="_blank">📅 08:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662814">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxfLkGlTiaMr4Ohr8keVtKWRq9ifPoGGHZ-hGhG7DT05Fua2gT7Xdsj8hzpYp7mOvmnOH3jxGYOywxnPx5r9TmFoAHBPykU9rGA0f4bcK-GMmrshW8Dlrb-hbpbC3V_7sHKvg7Di8bkH0bngWO1IN-f2Q7Yg81Yntn_p4yJG0BBCCweeLKXnIjQC7VZfBjChcolLUgvN0AR2tWbSPGE5AceFgG1Nz_PZB8-Ql2pzcUkQ4106_R6iD3OVSqK7yfXLUF66u2zRhn4iValld8iVG4vQ6TXiU-nC8Mrmew0OSxOmiXWC29s9so6yXrItypa0QbKh5XnxH0OsVqX9fH_gzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویرسازی شبکه‌های اجتماعی درپی بازی کسل کننده انگلیس و غنا در جام جهانی
🔹
انگلیس و غنا در دیداری که انتظار می‌رفت بسیار پربرگ‌وبارتر باشد، به تساوی بدون گل رسیدند. با این نتیجه، هر دو تیم به ۴ امتیاز دست یافتند و یک قدم تا صعود فاصله دارند.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/662814" target="_blank">📅 08:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662813">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkVj2CwDvhmWG_t-yICE3osBQY-3h0t52vNAVQxa81_teaA07ye98j6kJkGs3sYMYvi9lNJV_XxUIchLWTp94CVkszrHCyznHDeWuhfvY_5ICCLitAL4x5dIBcurH3iDrFeFNSGGVSfoEog4hLQMctRLtvYZJf--kDMsgosxgAt9lN-8TkOtsmIGEatEl6OR2yjp4BTZ_o6lPLT-doeNRsJ5_XgInEQCJ41pA-Mb-9KNMMXBqgj4jUhsJ8LwNU2877yj87lpS2-NLfQJno-TbUG0Bey755VX2qWkRszY2jadfHW8hoCAn8QW6EjwOL3MJxuxx_B_0063Rc3f8HXoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم‌های صعود کرده به مرحلۀ حذفی جام‌جهانی پس از پایان دور دوم بازی‌های گروهی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/662813" target="_blank">📅 08:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662812">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58697aba5f.mp4?token=r63nGN_Eo0YInFmbxcSdtaKcJgcQs6W5EBXh-HihNszjn5TI1GRH5S73QEDmQrWAbKL3K2bYgpkJuAmpRB0rLEYNEeKMVaz_Y3mdBsVgI6C2uTnUjHg49o6QLyVzhcV8kKtQvQovWmOxYHqn8pV3fDJgSXtKzDD4epr498cMPdResKE2aFukCtMWKFGh00jOwQcjfzA_g9ejipU_ifHUZdL9bXT8E7h7QW-zErJOnlVxbVLf0I3VTTfhU2Hhi0rmo9ZlAHUJtqgzLe9c9rtkDdWnYjWEH30BUpQ1bo6t6PXgji1idFfzbujZzXDHyMMwnUSrtFDL0Xl7RtWNEv-3Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58697aba5f.mp4?token=r63nGN_Eo0YInFmbxcSdtaKcJgcQs6W5EBXh-HihNszjn5TI1GRH5S73QEDmQrWAbKL3K2bYgpkJuAmpRB0rLEYNEeKMVaz_Y3mdBsVgI6C2uTnUjHg49o6QLyVzhcV8kKtQvQovWmOxYHqn8pV3fDJgSXtKzDD4epr498cMPdResKE2aFukCtMWKFGh00jOwQcjfzA_g9ejipU_ifHUZdL9bXT8E7h7QW-zErJOnlVxbVLf0I3VTTfhU2Hhi0rmo9ZlAHUJtqgzLe9c9rtkDdWnYjWEH30BUpQ1bo6t6PXgji1idFfzbujZzXDHyMMwnUSrtFDL0Xl7RtWNEv-3Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ: همسرم به من می‌گوید لطفا نرقص، اما من عاشق رقصیدن هستم
🔹
رئیس‌جمهور آمریکا در ادامه درحالی‌که حرکات غیرعادی انجام می‌داد، گفت: همسر بسیار شیک‌پوش من به من می‌گوید؛ عزیزم، لطفا نرقص! این در شأن ریاست جمهوری نیست. اما من می‌گویم مردم عاشق رقصیدن من هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662812" target="_blank">📅 08:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662811">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
تایید حمله سایبری به سامانه‌های کارت‌محور بانک‌ها؛ اقدامات دفاعی در حال اجراست  فرماندهی سایبری کشور:
🔹
اختلال در خدمات کارت‌محور بانک‌های ملی، صادرات و تجارت ناشی از یک حمله سایبری هدفمند بوده و برای حفظ امنیت دارایی‌های مشتریان، بخشی از خدمات به‌صورت موقت…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/662811" target="_blank">📅 08:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662810">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔹
هشدار سازمان مدیریت بحران نسبت به احتمال وقوع سیل و گرد و غبار در سطح کشور
🔹
سخنگوی سازمان مدیریت بحران کشور نسبت به احتمال وقوع سیل در برخی استان‌ها و وقوع گرد و غبار شدید در مناطقی از کشور در روزهای آینده هشدار داد.
🔹
طی این روزها در استان‌های نیمه شمالی مثل آذربایجان شرقی و غربی، مناطق مرکزی اردبیل و خراسان شمالی و شمال خراسان رضوی، گیلان، گلستان و مازندران شاهد بارش باران خواهیم بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/662810" target="_blank">📅 08:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662809">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bded7ff74f.mp4?token=CNWrQao8kCWlMTanQ7-uGmSap3nah4UYB-gf03DW91xGpoweGRdHxtoFe5r3dMyq8_Fe7-XpS3YzFwnLk0wZAyt_7qTn5HPi3hLxMkUT-CC8ma7K8_RPpGdmspbGD5poIPrk_bKs5JZk_YY6qds-H3pALez--3reaNMsA4KpZm7qAU_qV324j3KdVqwh2K7TEcITUsVtlZ7YXoezyvTFXeA-VjA9NtoLRXx7q9CkL6D2j-R1ROXE6PpudN_JJCaOPx8fV4eyk4ca3E4f39HNNutwROLW1JS5TVxf7SdYLQ_1NSYD_rhtMstO0mt2aCZDrCmF34mKVUlLjczlHUI7kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bded7ff74f.mp4?token=CNWrQao8kCWlMTanQ7-uGmSap3nah4UYB-gf03DW91xGpoweGRdHxtoFe5r3dMyq8_Fe7-XpS3YzFwnLk0wZAyt_7qTn5HPi3hLxMkUT-CC8ma7K8_RPpGdmspbGD5poIPrk_bKs5JZk_YY6qds-H3pALez--3reaNMsA4KpZm7qAU_qV324j3KdVqwh2K7TEcITUsVtlZ7YXoezyvTFXeA-VjA9NtoLRXx7q9CkL6D2j-R1ROXE6PpudN_JJCaOPx8fV4eyk4ca3E4f39HNNutwROLW1JS5TVxf7SdYLQ_1NSYD_rhtMstO0mt2aCZDrCmF34mKVUlLjczlHUI7kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
حمله گردشگران اسرائیلی در اسپانیا به یک غذافروشی خیابانی به دلیل برافراشتن پرچم فلسطین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/662809" target="_blank">📅 08:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662808">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔹
لبنان و رژیم صهیونیستی امروز هم مذاکره می‌کنند
🔹
اولین جلسه مذاکرات لبنان و اسرائیل در واشنگتن پس از هشت ساعت به پایان رسید و قرار است گفت‌وگوها امروز چهارشنبه با حضور هیئت نظامی لبنان از سر گرفته شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/662808" target="_blank">📅 08:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662807">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔹
قالیباف: اجلاس باکو فرصتی برای تبیین تحولات پس از جنگ رمضان است
رئیس مجلس:
🔹
اجلاس باکو فرصتی برای تبیین تحولات پس از جنگ رمضان است.
🔹
بعد از جنگ رمضان، شرایط منطقه متفاوت شده و باید با نگاه دیگری به آن نگاه کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/662807" target="_blank">📅 08:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662805">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
عصبانیت ترامپ از مصوبه سنا که اختیارات جنگی‌‌اش را مسدود کرد: دموکرات‌های احمق به داشتن سلاح هسته‌ای برای ایران رأی دادند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/662805" target="_blank">📅 08:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662804">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔹
#چند_خبر_کوتاه
🔹
قالیباف دقایقی پیش وارد باکو شد.
🔹
هواشناسی: دریای مازندران تا جمعه شدیداً مواج و تعطیل است.
🔹
سازمان ملل: مواردی از نقض آتش‌بس از سوی اسرائیل در لبنان رصد شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/662804" target="_blank">📅 08:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662803">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qemF92qFv5XU5ZGRqLIkBR2fcbGu3-jbvbnvdBsb_BuEkAK2qS6GTTRnidzwmGZL4d10MxAGf1nPL_bb1ltGb6S0j6d9eb4CzMEkvKNijTKXqTJGGUHCNTuVtuFblSPRmNyI_oX3Er7MZy6QJvrTcSS6KNvJWnxL5diAliWmhAbqFMBNWzVL8RgwHMvQTKQNqrUKFLT-TjfIYAax9qJWFdKTZ4uXbjF3_-2-FY4EBLdudyhVWJWHu-qkjPia3fyBnPqeoN8cC2PrS3sR8WULP76QC0-3PzC60iAwO1QBk5UtGaJWeOid1hm9VI3zlPC5pFeqnFcq_J-kUTCcxBWbEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۳ تیر ماه
۹ محرم ۱۴۴۸
۲۴ ژوئن ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/662803" target="_blank">📅 08:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662802">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilCsi9szyx2yKi3kp9Gqd4HMipzR_IkvPXFy3Wz5NYa6LzizFYILe4hv_H7HwjFXCrAQUlFaSS_hlCguCARi-JooKdi_xAd-1i7WcOEAlR-mXibkJhjctBTjhMc0Hcs38baxvTvDVhEfv9pi7_2gOWM9bVX41Lni-5i5CvWiSUECk3kGKeBUdZ3V6xxiOVzUSnRrtNLA5B19f6GVJ7kOs9vewU8lAeSQrG6K3xVmFL3CVRASB7Tw2J31R7WgWzuFyXjco5S3ze8bODTpsfH9U4EHFWEv-3PkIFatiQ8WpAko7tMlb3hJuS5mxmFw2gJs3ByEzj__bx5iukjuZEJXnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پسته لیام؛ کیفیتی که می‌توانید به آن اعتماد کنید
🌿
مستقیم از کشاورز
💎
کیفیت ممتاز و صادراتی
💰
قیمت مناسب و بدون واسطه
اگر به دنبال پسته‌ای تازه، خندان و خوش‌طعم هستید، انتخاب شما پسته لیام است.
📲
سفارش و مشاوره:
@LiamPistachio2026
🔗
کانال تلگرام:
https://t.me/LiamPistachio
✨
طعم اصیل پسته ایرانی، مستقیم از دل خراسان</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/662802" target="_blank">📅 01:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662792">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFJISrUARMddKoPU0Qi4q_qZ6Tkiy4FG36uOLo56PrnUFvRNfiE2shj7hSU1DjWZG4CraHevZw2uOd9PTog8ErUSt5DpGI8hNL7HanyhWz9go5gDJihGQ6dQ3ZVD6Cl8_nxJ5lyQj5Y_-xKMSfpDFr9MmP30NanZmPbgr65cTCkECUAPD856CleVz2bO9hTcDzfU7UmkTBSbG9ynLzUbf33zVyZM8fztorZGHoWrD5E0tH4m2bEQDPa_nWoKHxBCAB9U_SmHdHHsUrmdFz09LY4lvZrILtiYfNUMdH7EqlVvuJht2gz2GOdS2xFjqSKYmzPPKFhNSKS3DT3oNMrFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bowqOBxW72zSMpKbUSsxFjg1wmTnIzBXqLgO550cPJUpIXSBf7Vns7bGgDxq6AV_sgP_jbbXOkVAJFhRCQ0FifvcKHulbi75at1836DYZ_jQo05gzNG_MFhyo4WUJbMozqaYB1UpnIhCw7G8XwOIVx5NbhvLjBArcvXK7u8Y-cAnOVcuttFtB7YwJGdcy61fze6fu41XsCB9-_MWwhcR2hE6hYsKzS-FzJTMjyZAbhx5bBNN5264aGCfFVbPCJ0Y1ysriF7vb6fadF0X1DVv4ysH4w1X0SAAK4JaKofdxXKwkxiqebBpBahi_Pi1J_ltt8kMyBlL-lBKr2K7SMXQaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GY-qG-hoTs_9ot93M1NbDwFmYbPydZOtU2q4tTlxkqeeXwDGNm-pa1kXocc3d1wEdaceY8KWIkQsnUteYHc-LWR_uGGCgm8ArhiOaevFyQ1PWHRszY83y5B469Ifd0VKjH5C_EJ1T2EZ5U2CsUYQ6w5Bljg3bkkEWdOQOy0-LZaYuv5o6UyJ-o_igoJafuijupIEGzXHEHkphF5bkIP1ZeW2u2EzqsRijD8fFcGpAVsr_t2VtnUgT7_E5TV0sfpiZvgdwvM_PhYvNOIiCRCQ9CtpMfb5KJVcc7Vsh_F5QFwT5tW9uq9JFDCjHNLBtFNuNKRXSzYNPEN1M-QJ-Y68Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UN-zBVjvwwZLx-YvqCdgu1XwrytuOT_fQphDNXt0om7-AW24N71Y3QLzh-6cWFixMdUquVbO2f5-n81e-A059z486qk8SEWKx3KIBPUmWtz8tnIlVbbQuTZnpMzmemOJa_OFY1AeXaHlOMAJdMw_dhlL3ajecN1PMp8DZ87ontt1dldvf7TlXBpnne9yx7h5fctqUymD_gvgpBzfjgFnq5_tcU0os2i1M4KK--X49FqTsCOVZhrcBbld1_Iq1HunhcHI7Jy6IlUo0a8rQR9yN_z-zf4XMzfHyTzagB4VJ-WhCecrKvuZLYE4-Na_2qaDLWiABQpwMfl6Gn7wEsoyXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAJSTQKwj0A5UfTkm5LMwfGrWmXF9Ew9eyq1-R2SnNbjO8Ai8pCVQAJa21CKlNk7_fyL4Ie7i1GJp7sYdsLjYHx5uypGrOzsrRIsjZV83WmV4k3qs61F7Iq1cBLWDKD9cYTQZ3ovmGUPDJoHkdjJx6DplpURRCNRua2E93Bv223HR840GHsePiuwD9m3x5Sz6eYuNHfG0ugNcgap25G_BrdBqLFzTAC0VER0HdR5l1dakF3M3L5sYuCpLerFTqwdz-DgJMUq2DVvvBUfS9XNvJlgl99Om0oCDtujkPGMbze4MfOtxMlbbCP6uF-umTpHg60RA9c5WLJ9MaWzM7BL8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQpFFwRNM9a_ZrlKixSSXV4zDA8uWe7H9eA9BuuWUr3OE1VYqecS6NPjjPwocjdibSgBK5wl0MQNCMq846DOliBdVVLEMTGCIDufLo7JutSRAn3TMQ1qER-0QEbVoy2zZWPd1xNcQHsR5izAaVpDCYCdmDhSf-r3xgV0yr-M-o-OGAr_2obbiN23OymG_MjCInGPBRaCvA5CqYnf87kTcXeN41gg_UzU0KavhuTgHYfkDVR0-YcJo3Ti-aLJ7wN6Pq4bOjObzqiZZ0JmnHfLGnE7LchDgZd5zzGJ4Ke6CNtT_7BAY_XUWLgSxAyjbOQ2jUBMcqDNQ2ReW-202k4dJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IgFJbon2uyjR-H25KU9Sq2VzOUlOy7t1wGrMVwRejETd0_Ag-ecX3lt63BwZaSd7EYgVywBsVMJmitool9WseILTR28ICKjMaiAgtTSQy9TNnF8NEmICRPAtyInB89xLdvgvrCUB6CmhelL0JWBYFJ3R7lusVSbnSbPG7BeV2C4W4UEywyjpUTf2ttxJs5_r3RKXCueCm7YGW3aI7eP2rlXb6I-p2DKSHAMH9BLYICdkBAnUxNEcdGeUI9lMQ6k3ocmn9Nm_bCW81d85EfHkGkldUHcxCQQCDWdG_LNP57BaG_YFICabMnsmRtEia3O63YyoNyO3hpY070nezjh8OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FCj-NPUOPiEbr7vcmm9FQPlpgvZ-cR40UjdxlBLnC5Ta55zMoGSc0WRMIgyQym317OEdTXQquQEwZtPSRLXRnTOuhnpeS0St9OemYSYuDq6k7GPv248snFzzr41AZuBVXwZ_c0u0CibedBZSLklfplBvZBi2TSm_tkjTlKGM6BHbTsXpJs2tHV7bLMrDzWZ0VUd5q5cvcmcuSQ-eJJBihNkpUMh28d6OfdBP7l0NmWqHyHhZ7mOSCv-xCTQpUcOt2Lwq0pwi_znEv20YqzMw08sWql9KblPlEYmNV-H0J-Qu69s83jzZUHbc-mEEb1V3gIXgP1fJjMZ-YU9BZjj9iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v9kk51-RFLivc6xy7fNIPZkfW387GwywN7z48FLy7WmGA2gbwRyMRl8ax3Za9cpY2A9FVCCpNwe47iv_p926VrQwDf44yi2QMIQ3-rGi5mOUhlRxiRYyw2KIHj01_TNQinEiXHZr4Ep8fl7RuqZaK24Tvffh4ADMv6WjmT_DzvQ3kZwuJQ0W7KUDJWSiEvQ7XBOxxEreiwL6C9Nose8EXbpaLrRKEMVQFV2l0QcXepvWvrQBuXCUPxhg6v92nDNTa8oxa_XWoRVLY-Zrg9gI-1Tx1HSnZYze21RqPxbnWwxZC6YHonde34w3GKi0eTNKQPUCg4cBHBe9U26m6ymdHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_B-7IqOceL3ze_-2JJdx-b7CU6pajpajhk5qm1KCg535SM-MhbAiKcWGHTCDtk3joNGiC-_N0TnHgAJ7WRs8uPibz3x_q0T0wJzyu1HMA9ToLljeK5Uq8cJH8ZweGJ9jvWlBv82R6y1u-LfMngJ5rlbUnHghAlc5c79zdrfH8CarLu5XbpxsYGcN5O7J8Zo6sTIa-1Gk39qZ5uw4fFexc0aOvblovkxITxINK_nk2OXLjBHyiyWPHFYe0B1euCYHW7i5wyA376xfZ5VvsRHiMzc4aHdQl-fqiKaq1RS4g376DYS4LlWP-X_6aKLRbm90BF0tCB1G8RkNms4zK6-uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فینالیست‌های سال ۲۰۲۶ مسابقه عکاسی Australian Geographic
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/662792" target="_blank">📅 00:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662791">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
عمان از ایجاد یک مسیر دریایی موقت در تنگه هرمز خبر داد
خبرگزاری رسمی عمان:
🔹
سلطنت عمان در راستای تضمین آزادی کشتیرانی و پیرو رایزنی‌های ایران و آمریکا، یک مسیر دریایی موقت در تنگه هرمز با هماهنگی سازمان بین‌المللی دریانوردی تعیین کرد.
🔹
عبور از این مسیر بدون دریافت عوارض بوده و کشتی‌های متقاضی باید هماهنگی‌های لازم را با این سازمان انجام دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/662791" target="_blank">📅 00:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662790">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4894112c41.mp4?token=GDjJTAsrnx4gy-NFBVx9R_JxTXBJ53r4D51QGhjFpHsg_dt2xm7Dcq1pUNLOsekCKZoccbx2s0NcB1y33tqaOqWlXldI7ysR-XM-7NRoTewfdLO7i7RBkPxZAPvyRxTyOLdMj-j3UIgtO755lG4qW9pAzfBvx6k9t6nH6ygilDCPa-QB3ps_yzgGVcRJV-MmTaHwORMU5mh4MDxHGNPNWRYZDg4282Z0WIfStrWZf7GsBaXP64YeNvPb-PyKnhgZDm7QzHR7WU27tzWtH2sO2e6KQ3we44o8eB9q1dbKTTgeQdx45HyWYkdUUvRlp_Lwbed1m7YTGeg49zjbVZJr1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4894112c41.mp4?token=GDjJTAsrnx4gy-NFBVx9R_JxTXBJ53r4D51QGhjFpHsg_dt2xm7Dcq1pUNLOsekCKZoccbx2s0NcB1y33tqaOqWlXldI7ysR-XM-7NRoTewfdLO7i7RBkPxZAPvyRxTyOLdMj-j3UIgtO755lG4qW9pAzfBvx6k9t6nH6ygilDCPa-QB3ps_yzgGVcRJV-MmTaHwORMU5mh4MDxHGNPNWRYZDg4282Z0WIfStrWZf7GsBaXP64YeNvPb-PyKnhgZDm7QzHR7WU27tzWtH2sO2e6KQ3we44o8eB9q1dbKTTgeQdx45HyWYkdUUvRlp_Lwbed1m7YTGeg49zjbVZJr1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارلسون: اسرائیل در معرض تهدیدی جدی است و آمریکا از آن فاصله می‌گیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/662790" target="_blank">📅 00:36 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662789">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔹
رئیس‌جمهور پس از انجام سفری یک روزه به پاکستان و دیدار و گفت‌وگو با مقامات این کشور، اسلام‌آباد را ترک کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/662789" target="_blank">📅 00:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662788">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
نگرانی ارتش اسرائیل از اسارت نظامیانش توسط حزب‌الله برای مبادله با نیروهای محاصره‌ شده
ادعای واللا:
🔹
ارتش اسرائیل نگران است حزب‌الله با اسارت گرفتن نظامیان اسرائیلی، قصد مبادله آن‌ها با نیروهای خود در تونل‌های کفرتبنیت را داشته باشد؛ در همین راستا، دستوراتی مبنی بر جابه‌جایی نظامیان در گروه‌های کوچک صادر شده است.
🔹
این در حالی است که حزب‌الله محاصره نیروهایش در این منطقه را تکذیب کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/662788" target="_blank">📅 00:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662787">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
مهم‌ترین حواشی و اتفاقات جنجالی ۴۸ ساعت گذشته جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/662787" target="_blank">📅 00:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662786">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8d2be7bc.mp4?token=mSgs_FwpIFLlgpTR-cZriJLUGpnz9oe-G9Vt21r767VHi0bE4UGkQ1bc3Pk3M8NFVp-hCQSlLz-_kbGF759jOnqh59OAtffyTCmpSo7mYfFsvASzfHyllDdRk_KGaxYxeHM3eMMLFPk43kvvcr_XK14nnnxRzXWp3VE424ewFkSro2SmP-dfvdv47ujLl4-q3x7A6ZAclywZIviBllar1I4vOH9Zbsu5A4NfnoI4XM0DMjbcIaMASd_H1OLCAiiCzFi5W8HNK8WwIdgaJ_H06Sa-dnWpH03b6htiDs0uXjhXKYa1M82PUyuf4B-G85w17Yb_Wb9QXUIPJ316TyDQ1XhKwM9-ZQcJIA1vKy-imF-8LSibrhvxONB82nfB8vIN2TmsOsjNNahnWJNlQWlYKZI-3-ME_yGANUC-tskmsj9DGMwy0sx3ste5qz5deNFQHg7MdChyEG4FeQCalF2K-Sc8iClU2Z5elAD6HP0f77UK8TZ77E7IyuKHGeNWFMyV3SysiFadtMuklXWY0YF4A0d24JpnOOkd8EctcgIMgdS9MCyjlfc2KMQqE_rSc5qI2vyytzMlQXiAEDn1EkNEoipUVU8quW3fNpFBt_ItL-w33qyFaEyOoPRpd3L9IIh-0FVNB6cpbN5cYW1wEXicd9W7ie0UWd8_oZqMZrbqX94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8d2be7bc.mp4?token=mSgs_FwpIFLlgpTR-cZriJLUGpnz9oe-G9Vt21r767VHi0bE4UGkQ1bc3Pk3M8NFVp-hCQSlLz-_kbGF759jOnqh59OAtffyTCmpSo7mYfFsvASzfHyllDdRk_KGaxYxeHM3eMMLFPk43kvvcr_XK14nnnxRzXWp3VE424ewFkSro2SmP-dfvdv47ujLl4-q3x7A6ZAclywZIviBllar1I4vOH9Zbsu5A4NfnoI4XM0DMjbcIaMASd_H1OLCAiiCzFi5W8HNK8WwIdgaJ_H06Sa-dnWpH03b6htiDs0uXjhXKYa1M82PUyuf4B-G85w17Yb_Wb9QXUIPJ316TyDQ1XhKwM9-ZQcJIA1vKy-imF-8LSibrhvxONB82nfB8vIN2TmsOsjNNahnWJNlQWlYKZI-3-ME_yGANUC-tskmsj9DGMwy0sx3ste5qz5deNFQHg7MdChyEG4FeQCalF2K-Sc8iClU2Z5elAD6HP0f77UK8TZ77E7IyuKHGeNWFMyV3SysiFadtMuklXWY0YF4A0d24JpnOOkd8EctcgIMgdS9MCyjlfc2KMQqE_rSc5qI2vyytzMlQXiAEDn1EkNEoipUVU8quW3fNpFBt_ItL-w33qyFaEyOoPRpd3L9IIh-0FVNB6cpbN5cYW1wEXicd9W7ie0UWd8_oZqMZrbqX94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جعبه‌سیاه پرونده انفجار بندر شهید رجایی
سوالات بی‌پاسخ کارشناسان حمل و نقل و صادرات:
🔹
چرا کسی از محوطه سینا (محل شروع آتش‌سوزی) اسمی نمی‌آورد؟
🔹
همه می‌دانند این محوطه مال کیست!
🔹
بیمه البرز دقیقا چند درصد خسارت ۱۱ هزار کانتینر سوخته را داد؟
🔹
مساله ساده است؛ ماجرا سر پول است/ مدار
ابهامات کامل این پرونده را اینجا ببینید
👇
https://www.aparat.com/v/laibjrj
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/662786" target="_blank">📅 00:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662785">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osv_XmAG5Ol5_Y1QieOwHMBZl4JuNISVOelCYKo1VZ5r9wBWfeOmNIg4Sx7jVu2zouetMEumdIdzml2D9FG-XxgO6XP1BgqOQ-ZwIELUWQGcj9sn179-sikK82qORD00k23wnTFbcWiNHj_NRPXhJhtTmzesLpz9nsEalqOoP1YLNOf4HK3CDFz0Jrg91ndIBcjOHylU-9QlV8TMlF257wS-0DUIbFxmpngewYFI6uUzcX8AqrclcEe30nj9hSNtoAoGErh0DC7jeXxC6dHUMJ1XAfmjtvIBSESmCV9Ub1fGhdbEuaVV-rhcdosA8U1WxsF42y3qI_5TyW-MxgF9IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
شب نهم محرم به نیت علمدار انقلاب شهید حاج قاسم سلیمانی
▪️
رحمت الله به عشاقِ ابی‌عبدالله
@Heyate_gharar</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/662785" target="_blank">📅 00:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662784">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_R_bVKcT1E3V9pDREZC_7LqYToDOhXSYmMc-h3l4sEpwD78dcUHR6mMeLDOtEUNaMtfgTgF8Rjcjqx1jdbmcgVcVFRPGe2Vl891Nh7CKN86bKG8_MO1mo_E5GzaYVwF902uStjWLjK297d0ATvoHgwmW5lq_UlYEHfTI7czNK_lLpx7bPiY_6yMAuFAcQxe4CVlyqf01nK0x_ZCdZgi0lwrlqAYpAnkpGS-abh3B_GvackZXsMmDyHEmQUsjB-90RxZTmo7PmLGPy7atcooZbrQOAzTSGQ8mwk83MEOFopsSRyddEBhoAa5xrcrvasZnEP_ePPWeRunVs5zQUNBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/662784" target="_blank">📅 00:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662783">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11f58aa93.mp4?token=Ox8z-z01zMxUuYshSEfV74IDcO7yrd5nF-vly0FWP4v1lTgc8CzGAFEmz8Z14E_CAlM8C_rloLidH9GDQ3RVRz0_VVOphzdu16VtpI_6RrjMp01kFjGKKSoQK1ckr0CLZki1D9BskcCx9BB27Pge5U8Kmglcy3IoW14tyEbnI8Ql8oFnhvenAL-iLRGeJf6HvJD9tNSp837aft3WJDyE48rdnjcT-cv_pIbW8fg2YhgOMiwQ10GxwB4nsl2fHuLLXqVO-KbgrnJorTe9EfNNmBAZotfJJIjzMWqEIR6or7uPHGnJ-jmf0MZ4EtL0rtGPANyNxL1kGUu0uPwVROsDNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11f58aa93.mp4?token=Ox8z-z01zMxUuYshSEfV74IDcO7yrd5nF-vly0FWP4v1lTgc8CzGAFEmz8Z14E_CAlM8C_rloLidH9GDQ3RVRz0_VVOphzdu16VtpI_6RrjMp01kFjGKKSoQK1ckr0CLZki1D9BskcCx9BB27Pge5U8Kmglcy3IoW14tyEbnI8Ql8oFnhvenAL-iLRGeJf6HvJD9tNSp837aft3WJDyE48rdnjcT-cv_pIbW8fg2YhgOMiwQ10GxwB4nsl2fHuLLXqVO-KbgrnJorTe9EfNNmBAZotfJJIjzMWqEIR6or7uPHGnJ-jmf0MZ4EtL0rtGPANyNxL1kGUu0uPwVROsDNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور رئیس‌جمهور در مراسم درخت‌کاری اسلام‌آباد با واکنش طنز کاربران همراه شد
🔹
بعضی از کاربران با اشاره به پشتکار وی نوشتند که اگر نخست‌وزیر پاکستان مانع نمی‌شد، پزشکیان تمام اسلام‌آباد را بیل می‌زد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/662783" target="_blank">📅 23:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662774">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGgQ3Sbzv1vVuy6eRmWHw9Pc_OX7UqZ6kKmiiTtDllJjQk2zfi4PbYjmA59Vk-Qalukz_PoJf-NJa0MQyvQQtMCARw-K8njDske4tvWs205JT878O9aTAkBUbNtTnwkRK5FT4nWyTRMI2odthYNu8b0hV6MsY4S18Ps_2NEh0YHjC4EkaIP42eIxWUQU0OHaU0zJwbncj5cS_fqAfeDW0Kj4g0YBSrRAoS61UPKc5QXSX4w63o_fpt3mKXMFIkTpD9KPzSCm7LUrmIGhatOw_KziGO6dh_X3seObp2TiuckjlMOGQ8u7vp3PZmJ-5f_QJT-t7qBMK5D1vXxu2kYwOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2M23nyPj68Orb9-YDVa4bgvreGB-T6tmHIVDmvHp-XC5DIo8kcjkL_ckqZ8nOzw2eE62POgDwnYV-qDaRud3KqU_8JZN8Jyqj6-96fHcVnWVr2wpz3THwmaCIP_-ofEApcVM4G5JAq_CgIisfwyGcHnMzHqifB7GRHweQQ2ttsMz12h1Zu0Nk7xPic1RPB71gsV2a1qlm1lTAIaL7fK3NYfMAK3WUlEhKQO__IM2lpYdmfxPqP4h9nVUGtH1F1R0DDz7G4NlFbvfV9isInk4oMZMCftmUIzHd7Z0ZN2OARO-5gwSyKQxvH5R8xdA2mk6nw5BYqf3DG8LBJmDrNX_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T051qxAQba91ektMTPGdfJq9r3CwZw15FUKVT6ue0XwU1T81m4WVNNHMlllGiiXPLX-x_h-XAdBt_RbOMWvK6pr39L6cvy4scrJD5a4gT4ABCtij3xP9yyT9bI3iXSjcIhlc7vlbz9Pb2ihNOP5f-SLOcbjgi2iuRVe5BuEGXagDMsykqU9b58N2TSjskPTlSJU1XbGZ4rIzjZAUkHwi8IUsY0mLhHFJOIeGEC6Tc2oYzZKNGVUPI_Gzr-NvA0fM3YtdL58dmTS718OgJpRqObAjBtl0exWZk2czEgMLCsI-k3tyMb_Fv4LZqD_hNYd5Uy3PvFdyIKdSFM6YelnMIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JR4JXnAnfy5cJ0TjPc9xXN9LmFNcPr-xiiIGyvy32_mohzoaFGb3ZOgvSUmcM38APfSP4bbpl5SSoR-dZ_M0gsRw5wRS42Iehm9fKnjSdw3M7SqP1XOmrWl8HhtvKh2DOzVXY2IhUQ3sa3uK31pb0MXrVaKhny0_pM79KOEW2X1dzm669NVmrzwXFo7-I-osqBSpOFRACtH9GGjLJWRkPJXsE9KIn-2M0YUWh77zG4F7w1mmnOzvdvPf11XrT8awd2_I4pZ3YjxiIc3GHCZVmUvfhrGcdW5wW5Dr8gLKdT6FL4Fq9vEQ5LQwfs_vvPw80yNZXMwshDME7jMSdeD6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p48biZcKgqhXp7_ASigKfMMETBi0ZuRfUcr4JSWoBYthgC8_yBKvmzf4TYtmDLIsOf9cHIT13zskDVodbMgJXMWrK2FAkKNCBvfcvBkDJdRA1L99ijTI8fJu-X8uwD-GCj0aR4q6XhZop3m6SvzivmEWl7Kt216hcVkZMNfBgYQOnLZ0hWBip6hJFXQfZTXg0pvhGRU3BrzM51KNtqMSpRdhREBovUyNE4bb0VSCWn87Rp1KbiHS-PoVsYj-w1QyEY6YVRV9kr2xDStOlvN_02vDNRjYOmB2HmrYZFv6Dw2McMeroYvH03qUveinVlQKkFSoEgUfy0HOgV1ejLAHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYSjzuQpxYfq3ZIirMvRGlkIqUqSuRdv7erfx1nKMgXlb-D83UvSo1hgFU3L6Ddl9AR5i-X1DsUxoD7Npm43hv50kHqcTrfNyKZtAMH4HTtKN7vf0fKx9Iv5Mx6Ty_ql-uHc2jLRLBlOF-VshEfSffqUu522vc_X2Y2h1DSII_tWnmfHO7yKFmXS-8D6gGjY4eZTK47VI5keDiigi_Zh2Nr7QZgdE8GFI1znAfhJ-uMlNGSesduylSLbC5_GFYsqU62vH2vQXaz0ehHXz-UCWjLa-FLZnNjb7036oQ1gvwXejzzClWc8caLor9kwdH8_-nlUgNUtqQeBgy3jCWNCfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5kKK08Wfs9LYk_dd6itJ935nRf-TDPpXJOYGnDEftp5gENIB59ywz0puWs4FLo_XD1sHA5VgET_ETq3k3xgfjZFXc5km5FDoQr-NRXZhY88YRDtNwWew5Qlny9gxWKY7zqXZ9M9k2dRUJY6cgofKX67GnXGKcZre7aPt7NsZcFF3z4AkF0FK3QhysHy8s8I6mQd3YNDrdXrm92baKUFfyvYHdSE-br6Hb4gb-mCF2OjlfADXr7A7K3RduzVyyGnZkT8HqsvHblb3GxyOUUqShoMiyO3Witazb8xh_tthGeh-Sc8SeeyRxBjPaSeZRLgmt_SG3XidBR0mMXeaW_--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4XgPf8WPfZg-YH6-Hq0_OFBxu8IzpM3EzwepvKZntmmw_3LhYiEHrOadUQKfxMNDYBD_mMgfR1xKbk2xlc5R1syDX7H_jS9gWlGxuLum4-7QmriviR1B5ddYgctOx5WzMC9dx87edg03qHuLbK0J6M3RRF4k71Kz7rvXasb8jne1cG99dHJwdWbwPyjV3JOoAH-qkPjJ4M9kAJ-P_PnUWCZh3vvzLap5wk2UdAcnFB4Ar_js87dC6574SXj1NEADP5PFP625lmpVUNRI7Vu0bJckEO7wCjjjCXd6Yb0fA9ZthwKA8hnSehCo8lU8tPV4bJswwu6CXAqdmYTaQMaFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSztffz923kn1zpFrCbPyHurvpy7mDvLr6OiHRsn99zbQShnhkXlDbsv76bOu9y5jTlEdViI3AgOTIKuZqzqcfLkvkHP6eOnr77QdiCLLLHbUJVwoiqyYitNEwh6pTEzglFK_YhRyTEom5b1uM6DhNbV8DhP_JSRM9Chkk-KUMnjkJqoozUcxO8oK7Ob6G1HPo2mvJXhwVD9nKP6THUm1997baCyosTDeODhZp-3_bnr73vNM4NzIadFq2hCTRxMjEXm9PN_vJjM3wFTNukfZAOHn2WuNSJNY61lUvsZiPjYqreHqX7cJz_1sJGNBY5x2-hOA8bqOXu99nuymshfNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
آنچه این روزها ادامه دارد، روایت دل‌هایی‌ست که با
#همدلی
، مسیر خدمت را در
#هیات_قرار
زنده نگه داشته‌اند.
💫
به برکت همراهی شما عزیزان، این راه هر روز با امیدی تازه ادامه پیدا می‌کند و خیری که رقم می‌خورد، حاصل حضور دل‌های بزرگی‌ست که بی‌نام و نشان، همراه این مسیرند.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/662774" target="_blank">📅 23:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662773">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
سنای آمریکا جنگ با ایران را منوط به مجوز کنگره کرد
🔹
سنای آمریکا با تصویب قطعنامه‌ای، هرگونه اقدام نظامی علیه ایران توسط دولت ترامپ را بدون دریافت مجوز رسمی از کنگره ممنوع کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/662773" target="_blank">📅 23:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662772">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
خودکشی دوومیدانی کار ایرانی متهم به تجاوز در زندان کره جنوبی
🔹
گویا یکی از دوومیدانی کاران ایران که در شهر گومی کره جنوبی در بازداشت به سر می برد دست به خودکشی زده که البته این خودکشی نافرجام بوده است.
🔹
«م.ک» یکی از متهمین پرونده تجاوز دوومیدانی کاران تیم…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/662772" target="_blank">📅 23:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662771">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
سنای آمریکا جنگ با ایران را منوط به مجوز کنگره کرد
🔹
سنای آمریکا با تصویب قطعنامه‌ای، هرگونه اقدام نظامی علیه ایران توسط دولت ترامپ را بدون دریافت مجوز رسمی از کنگره ممنوع کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/662771" target="_blank">📅 23:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662770">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e18c61de.mp4?token=SucIe1qyY0N3sxLBYqlwXNSusdyWkv3Ja9sWSjket6OU1I9XMuB-caXwWxradvM6eKsnye4f5Rq0BYfpgo5VBh4Rv29QrIP7va0SluHt0Ie_pFiGG-d61TkO1ELiuiF73-Od-G7-XcuCSLdDo18eERbEr9Slfd2-KCLFInm2s9BEqdQMdVL-TE7ajRQ5KFpeNQJ-KUsHZFm5NLWH4_jQtKqjU-ZAB8p2nKV4aXxfc7FvcBI97AsWk-d43JJcC0FzBbSZ-BTY45TjiBFFBEcdALbz4iqXirHSRkh-I218UBOyczg73YsNC-jQw4ZEkr6aXLionawtU7mQtteHeNxCiEeJGdNXQa0BAD9iAIM7v-RkzWWVcq_DrYnQZvGpkM09e_zM4ptWGbFApRFjaG38UPdu6GY3UKZZTPl7kOhIoT3mxKgXp8pxDsgxavnvxrhBMh8uMN08WTY19PI-4GGOvmRXG1GPJERDpGRQl54zWK63GVPl3z2JtY9izJBeCqOebbmy5a0G3RYn_jZXtjNV9cAd52HyyTH8rG_VmEFi_NYylEZ4pOwCKmm9CNJRPu1F7pvexth9PeWm6oK7nLFibYwuRz2mri1IV9AJ4NuVZl4oANTqe_we265eZCMer8tweKO38zx6mE3As7SQotoVdTbXZ8g0ZzyHP1KZxSJ2V4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e18c61de.mp4?token=SucIe1qyY0N3sxLBYqlwXNSusdyWkv3Ja9sWSjket6OU1I9XMuB-caXwWxradvM6eKsnye4f5Rq0BYfpgo5VBh4Rv29QrIP7va0SluHt0Ie_pFiGG-d61TkO1ELiuiF73-Od-G7-XcuCSLdDo18eERbEr9Slfd2-KCLFInm2s9BEqdQMdVL-TE7ajRQ5KFpeNQJ-KUsHZFm5NLWH4_jQtKqjU-ZAB8p2nKV4aXxfc7FvcBI97AsWk-d43JJcC0FzBbSZ-BTY45TjiBFFBEcdALbz4iqXirHSRkh-I218UBOyczg73YsNC-jQw4ZEkr6aXLionawtU7mQtteHeNxCiEeJGdNXQa0BAD9iAIM7v-RkzWWVcq_DrYnQZvGpkM09e_zM4ptWGbFApRFjaG38UPdu6GY3UKZZTPl7kOhIoT3mxKgXp8pxDsgxavnvxrhBMh8uMN08WTY19PI-4GGOvmRXG1GPJERDpGRQl54zWK63GVPl3z2JtY9izJBeCqOebbmy5a0G3RYn_jZXtjNV9cAd52HyyTH8rG_VmEFi_NYylEZ4pOwCKmm9CNJRPu1F7pvexth9PeWm6oK7nLFibYwuRz2mri1IV9AJ4NuVZl4oANTqe_we265eZCMer8tweKO38zx6mE3As7SQotoVdTbXZ8g0ZzyHP1KZxSJ2V4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا جلائی‌پور، فعال اصلاح‌طلب در برنامه «وضعیت»: بیش از ۵۰ درصد جامعه با تجمعات خیابانی همدلی می‌کنند؛ قدرت موشکی، شبکه‌های بسیج و هیئت، هم‌پیمانان منطقه‌ای و ساختار چندلایه حاکمیت باعث شد ایران از این گردنه عبور کند و در برابر دو قدرت اتمی بایستد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/662770" target="_blank">📅 23:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662769">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
رفع کامل اختلال کارت‌های بانک تجارت از ساعت ۲۰ امشب  شرکت خدمات انفورماتیک:
🔹
ظهر امروز، اختلالی در شبکه کارت‌های بانک تجارت، ملی و صادرات رخ داد که باعث  قطعی خدمات خودپردازها، پایانه‌های فروش و اپلیکیشن‌های موبایل این بانک‌ها شد.
🔹
اکنون عملیات مربوط به…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/662769" target="_blank">📅 23:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662768">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6bwI_kQfZyI-LUFBvsQl2_WPKUkHHvQ-kwXVD4Evy9W3AxbAuUPPMILxawgmgZYdrqDPCvLlOSUvsdEOHOj2n5T5YeobFpisq7rAKvcjDMWHuueQ2e4KixkT7WWz-juoPw0PXPZ0LbQJT3Aj_ac8sqo2eldrKEuJsODia--PZAnPRjiGoLdkBpYaz5fepehnWxowDLVmKeceQp9OffcypBiUv7KPSGvCuq487G7wXsZbHfVGBVO1VXTjIfwYU0Yvj1DaljdmCBJc9zqtSs05ESw-B5t5MP9cfxwM29iZu0ygbjd2Vosoospc4OlV4rM1KO1PqO-6abyy0Id26kYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسعود شریف
🔹
در ادامه تحرکات دیپلماتیک تهران پس از نهایی شدن تفاهم‌نامه اخیر، ‌مسعود پزشکیان با همراهی اسکورت هوایی ارتش پاکستان وارد اسلام‌آباد شد و در نخستین برنامه سفر خود با نخست‌وزیر این کشور، شهباز شریف دیدار کرد. همزمان، وزیر امور خارجه نیز وارد پایتخت پاکستان شد. پزشکیان هدف این سفر را قدردانی از نقش اسلام‌آباد در پیشبرد تفاهم‌نامه و پیگیری اجرای کامل تعهدات در راستای حقوق ملت ایران، تقویت صلح و کاهش تنش‌های منطقه‌ای عنوان کرد.
🔹
هفتصدوهشتادوسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/662768" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662767">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: ما می‌توانیم کارذرا در ایران در یک هفته تمام کنیم #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/662767" target="_blank">📅 23:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662766">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTYY4ArfIFiQvqc_pcRPrkzXq3xeXHjfe4OcfLqEgWDMBO9Azsmo7TdLWUwWJgso7HQ2m3XtoQHnpN5qC7503Oxv8BmBM_ZYKR3vEmR78Kxvi4tDEB69RXQts1UeLd2Ig7wZOy1_cVWO-CEgSpPODm0fsRMC592SP6yEz4iKH3JJFnzfAIyWKyXMy2ZHs9SM6EzOCaH5MHbyuDIZuMwx2wKp3uBwlciQluW3iYlqQgV4ztX_rCW5aoL8c46aKgoAwCR_MDtRMoR2G95zYAkX9DjqZF09U-ZIdc6qv3oA8PvO2-tl60kOXB3u1rPvjCnYxRXAxT8OygUUcps6lqo17g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سنای آمریکا جنگ با ایران را منوط به مجوز کنگره کرد
🔹
سنای آمریکا با تصویب قطعنامه‌ای، هرگونه اقدام نظامی علیه ایران توسط دولت ترامپ را بدون دریافت مجوز رسمی از کنگره ممنوع کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/662766" target="_blank">📅 23:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662765">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f776ff7918.mp4?token=cKTTLvrpCT9ky7CMcBjROm063KUImbW9m7hKZWfHDSwJ-lMubwSAxRywi8tCnMv9ho4NWdnBM19J2FqUL3lqIDkN69NWPX95UoM8weoRJIIYdSFGF5a3lXLnF-IKi2fcniiWZDrjxRclw5MCOh6eNR7-ztBjzXWlObrE1_qCvT_ZrBFHKn-15nuPPWzbf965_iqIrLWpOKFcIRWfMo5brDkW5IUaJWbQdzo9JaF9DD1DtLqyQAXdG8QVfX1HicYNpRBmpvIz3Ezopw1HRnNCW_pZV8ndL9m7uxvAZ1wpwkpy8TJqWpzOIMEKPp_31aIDIv_CX4Jk8p7Wi8CTpLhu5Jlbby6YnqrfgOpesDH1DgP9mdBudd9TkTsXIH-Y3XFuzNDg9j1-7qDxQHMwvm8J1dwrjNu5OpFAtqGiION6xrvu-wNV1fW-aPmKXL-0UaZw31XAiiCzT373VZUV7AtK11Xt0rTmJ_Va2qLdsCUvgtFtI2545Ppi2zXSFK9kUrJXtEkJhVMBh0fCBsuFIncSDsC1qRrRgxsYl-NdaoFbfLe4sMHzcndDH6dMolUwdFxVq2Am22JUvBdRPR8cUWLgWw3QD7ORZR6vkLDuFEURe9ZOPfxnQ5K9By4jq3COmtKKC-rSgkpHGhT5-5TwOOYK-mpIOgHJmy8S4RSL5fS9gY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f776ff7918.mp4?token=cKTTLvrpCT9ky7CMcBjROm063KUImbW9m7hKZWfHDSwJ-lMubwSAxRywi8tCnMv9ho4NWdnBM19J2FqUL3lqIDkN69NWPX95UoM8weoRJIIYdSFGF5a3lXLnF-IKi2fcniiWZDrjxRclw5MCOh6eNR7-ztBjzXWlObrE1_qCvT_ZrBFHKn-15nuPPWzbf965_iqIrLWpOKFcIRWfMo5brDkW5IUaJWbQdzo9JaF9DD1DtLqyQAXdG8QVfX1HicYNpRBmpvIz3Ezopw1HRnNCW_pZV8ndL9m7uxvAZ1wpwkpy8TJqWpzOIMEKPp_31aIDIv_CX4Jk8p7Wi8CTpLhu5Jlbby6YnqrfgOpesDH1DgP9mdBudd9TkTsXIH-Y3XFuzNDg9j1-7qDxQHMwvm8J1dwrjNu5OpFAtqGiION6xrvu-wNV1fW-aPmKXL-0UaZw31XAiiCzT373VZUV7AtK11Xt0rTmJ_Va2qLdsCUvgtFtI2545Ppi2zXSFK9kUrJXtEkJhVMBh0fCBsuFIncSDsC1qRrRgxsYl-NdaoFbfLe4sMHzcndDH6dMolUwdFxVq2Am22JUvBdRPR8cUWLgWw3QD7ORZR6vkLDuFEURe9ZOPfxnQ5K9By4jq3COmtKKC-rSgkpHGhT5-5TwOOYK-mpIOgHJmy8S4RSL5fS9gY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهدی رسولی: ائمه جمعه، نمایندگان رهبری و ذاکران پرچم خون‌خواهی را بلند کنند
🔹
امام‌جمعه‌ها، نمایندگان رهبری، علما، پیرغلامان و ذاکران سراسر کشور؛ روز عاشورا باید پرچم «یالثارات‌الحسین» و «یالثارات‌الامام» را بلند کنید.
🔹
این فقط یک نماد نیست؛ فریاد خون‌خواهی است.این پرچم باید از هر شهر و روستا تا تشییع شهید، تا اربعین و بعد از آن در گلزار شهدا دست‌به‌دست بگردد و بالا بماند؛
تا وعده انتقام نهایی محقق شود و بساط جریان طاغوتی از ریشه برچیده شود.
#خونخواهی
#WillPayThePrice
#هزینه_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/662765" target="_blank">📅 23:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662764">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89fa8a31e0.mp4?token=mSwTdv0stC9FlOwoEWLrnOhNFmF0VsCnyPRvSkT5xmOfr6C1dtTpb0X4-itzwXHBMqcssslr0fXHZyAwsNRlTzDLXnuHD4PvW4zJKMzDrVtJO7G5AvRRbn_fgI3Q1SMcRo9TMJIeoQNBOVh4wgmAjzEFSltfMZiL728_sTXxBhze9WC35fHcqmjZsznvr12D2Dgnbrf8mAqKO-GiffWlu5WqBz52UEnhASqO1KjHWiSfEPHZ32Eq97tu2cle1fjKJorxMfxOwVPx7MFKs5DToW4VCgtQBfY4KaDaBZWQsXIplRm8BEggUe4fbB-aeTbmvFx3I2u1ecsVMgt_9vSCLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89fa8a31e0.mp4?token=mSwTdv0stC9FlOwoEWLrnOhNFmF0VsCnyPRvSkT5xmOfr6C1dtTpb0X4-itzwXHBMqcssslr0fXHZyAwsNRlTzDLXnuHD4PvW4zJKMzDrVtJO7G5AvRRbn_fgI3Q1SMcRo9TMJIeoQNBOVh4wgmAjzEFSltfMZiL728_sTXxBhze9WC35fHcqmjZsznvr12D2Dgnbrf8mAqKO-GiffWlu5WqBz52UEnhASqO1KjHWiSfEPHZ32Eq97tu2cle1fjKJorxMfxOwVPx7MFKs5DToW4VCgtQBfY4KaDaBZWQsXIplRm8BEggUe4fbB-aeTbmvFx3I2u1ecsVMgt_9vSCLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکات عجیب و غریب رئیس دولت تروریستی آمریکا در حین سخنرانی امشب خود  #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/662764" target="_blank">📅 23:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662763">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tr95p9vZ6MzQtqE0jnNt30WUyi_2ZyS2qHJKsCqcUtAzSjXiM6eAEOeQpbfjLoEuXF7JSj2Rj-uVmRH_1G1oKjTjGrJXUJgfIMDZ8E3vmfTlc2bBzTgWVlU5ob1c7sKTu1Vb6nTbmkojJ6Fq2dsk7mRXoM50-e-HV6eqQq1TkmAG2kwfqXn0AI9YkXFDyKrVuv62Nl6cThKVooWI0ZY07EqX4lXMu2ZSDk_ICLTmoUX4qztb7Rh5I8Cuxammre_FWFFPUcpXtWtvAiURkYEC_wD4JtqF4rFIPl9Btae7hwZz5GVCvj1UK6TvbBeea8vo_JrAXIGh7K45_h06x-kdDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سربازان آمریکایی در حال پیدا کردن سلاح‌های کشتار جمعی در آشپزخانه زنان عراقی...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/662763" target="_blank">📅 23:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662762">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-J1oT9yb-SKt30o_155qasl_CqRLLTVFBBbLliCiR0wgitJaIKkKdh1MS_pKWp9AKPQcWcUOb1oEI5d1lKeUWOU6ffMJesoqrCh2NNfnILQDGHv5scH9EE53HAsMrIIdBBMNX-L0GZbyBa2UwErKXGgJefQh102vvFFW8gvg0xQlZmoIbdMuYkvE46McZq-0vNqEF8Ee_dTuyocwyiBHUooOxyegBwI3CmKtxq2p-bN6n5aO31elFdLqNQW4ftnC2pIlWwbq2lNuVIgeRt-3_b5JnIxAUc0MMXjX8daaXAbpLHAYDR4u2vW2io3MPM7YTabPBesRUbytq4qJYBldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از کجا قسطی بخریم میصرفه؟
بعد این پست دیگه حواست به خرید قسطیت جمع باشه!
❌
دیجی‌پی با ۸ درصد کارمزد، تنها شرکتی هست که روی اقساطش کارمزد میگیره.
یعنی اگر ۱۰ میلیون تومن خرید کنی باید ۸۰۰ هزار تومن کارمزد بدی به دیجی‌پی.
✅
تارا و اسنپ‌پی و ازکی‌وام هیچ کارمزدی ندارن.
یعنی برای ۱۰ میلیون تومن خرید، صفر تومن کارمزد پرداخت می‌کنی.
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/662762" target="_blank">📅 23:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662761">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUDOM4FVtZClo2DurMhMqfXpOUinhFnrC0tNk0WneDWViWSMfyro1keqc-n3Ifa7vhkXfx8x9V9SLqJkI8r8PMRmQyypzCv19KOEeWPHMVQD2h1EC1gsiEBmWmSCfBh2PupVTGpJK-R7oa4JGt7QiJ-tBOVnH46iBcWS1K5pRquPAgcKOUSdaY3CaQ2mD0IWmPZqYJkFK7pvhHT1jiOMmS6MIPfZgez1ePyn2chPnBHJu4MEf721mokvslRgP98AL7LCc5UKfR8RieDmPb96ZAoBMJzYDsTcZA0aIkjpjMVdRiOyn0x4OMVp105hZ7atgrlop5DJrSgGdP0wvVfiOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقق فرمان وزیر در سنگر تولید؛ پیشگامی
#بيمه_البرز
در بازسازی و جهش صنعتی کشور با ارائه بیمه زندگی و سرمایه گذاری پروژه محور
در پی تاکید صریح وزیر امور اقتصادی و دارایی در آیین تودیع و معارفه رئیس کل بیمه مرکزی مبنی بر لزوم ورود جدی صنعت بیمه به حوزه بازسازی و حمایت از بخش
#توليد
، شرکت بیمه البرز با تکیه بر راهبردهای کلان خود و توسعه بسترهای نوین سرمایه‌گذاری، آمادگی کامل و پیشگامی خود را در تحقق این مأموریت ملی اعلام کرد.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5051</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/662761" target="_blank">📅 23:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662760">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7P6ASAaDqGnT3EQQjRMG-0JWPnb-BGhSGfYyLQs_RBdaV6AohB2asE7SHoAVRrRzDgVjPx7e5sCDtONjDo8dGZaId4QPknMJWwISiUD7KFooAS7wiWrzvlIRZOTOtjy6ja3o-c5UMW1DgefLd3d2r4--3TBoIBNXul3surpGoRNNahS4FsMEe_9VBm6unH4tKZwqIMuTmegtQC3MdVocs3WElTWDpTjhMG1viGljY1Ftmipg5yCsE2MBc3ZQW2YS51SHjBkvN_QtzC8XC1fd4ZmGn8SgUpYUSJ_-78NG3sN5zHL3TQTSQuESH50RcWzqeZPz7fyB_f2FhgAyDVUWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴۶٪ فالورهای اکانت اینستاگرام رضا پهلوی فیک هستند؛ یعنی بیش از ۴ میلیون
فالور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/662760" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662759">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d32f65acc.mp4?token=ulsVYZcXDFjSrl-nSc0qBOc0kD7mqM2Vj1v2XPBgcpRZRP19OAXBfUzf5iHZ69Mt3VXwGwPm5fmG6mR9JNNl5ICuwnPowcmtfNNaq5CQo-YOIv7r5n22oPzOu9yivnNF0LJkpFRAUzmvLNU0xzhbuRMkJ6TlZUS5MAhnhPLl9MURCcAw-SZvYfDI9MNZRw-HLqf7D4ZvxxSa6F61jgWyBia5AXZ2K672-XnUWZXDlNm1ZM3MZrTsmcacoIdjl_5o4aIzUVlDwLazqyM3PQBaB-uorrCiBMhC3r2cSrIknmr-l6o5lPsvb9oKA3doNKbt7MhxGOWivazpmzJ_4mTvFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d32f65acc.mp4?token=ulsVYZcXDFjSrl-nSc0qBOc0kD7mqM2Vj1v2XPBgcpRZRP19OAXBfUzf5iHZ69Mt3VXwGwPm5fmG6mR9JNNl5ICuwnPowcmtfNNaq5CQo-YOIv7r5n22oPzOu9yivnNF0LJkpFRAUzmvLNU0xzhbuRMkJ6TlZUS5MAhnhPLl9MURCcAw-SZvYfDI9MNZRw-HLqf7D4ZvxxSa6F61jgWyBia5AXZ2K672-XnUWZXDlNm1ZM3MZrTsmcacoIdjl_5o4aIzUVlDwLazqyM3PQBaB-uorrCiBMhC3r2cSrIknmr-l6o5lPsvb9oKA3doNKbt7MhxGOWivazpmzJ_4mTvFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درباره ایران: ما در تلاشیم تا به توافقی عادلانه برسیم #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/662759" target="_blank">📅 22:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662758">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9iG7QNzjHmBMYTe7P0yBo2yYT0fm4ahwbjIM4l47Kq1xrL7lzJvmSZPGAROsOXWzAAC6I1u5f56jOlZhB22AGQAJ_Y5f72yqw4UYhdlQglZDmRobCakuB419KbbvKIjLCLy2UISZNHoSNFHqEsfJCrz0Ihr-n7X075M9qPAE1EFe4Go9jOhceWRxyqcI-EwouvSkgIDr5jxHOWVHBjwRI93t2Bvp4bS2stDT5PJbsYX-E-9y32TufDlJ6cvooR5gCUT9GMSXawgKgM6UQvt1u8-1EelDuuIsF-v-irmbQkux9t53mkmKz23pL2hiHwjJsN9cFvUhcSc1-6QslSAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریستیانو رونالدو به عنوان بهترین بازیکن دیدار پرتغال و ازبکستان انتخاب شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/662758" target="_blank">📅 22:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662757">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">✨
گلچین  مداحی های شور  ویژه
#شب_تاسوعا
🖤
👈🏻
جهت دسترسی به هر یک از مطالب زیر، روی اسم مداحی (آبی‌رنگ) کلیک کنید.
کار دست ابوالفضله
حسین طاهری
اباالفضل با وفا
حاج محمود کریمی
قمر الله
امیر طلاجوران
پناه مردم
علیرضا طاهری
ای یارترین یار من
وحید شکری
چه قیامتی
حسین طاهری
عاشورایت
حنیف طاهری
عجب جمع رجز
رضا نریمانی
عشق ازلی
حمید دادوندی
فالبرحل معنا
امیر کرمانشاهی
لک زده این دلم
جواد مقدم
مسیحا اباالفضل
حسین حدادیان
نیومده دستی
سید مجید بنی فاطمه
هوای من هوای تو
حسین ستوده
ساقی لب تشنگان
مجید بنی فاطمه
شمایل
حسن عطایی
محتشما
محمد حسین پویانفر
ای شاه غیور
حاج محمود کریمی
بریم کربلا
محمد حسین پویانفر
نامه خادم
مجتبی رمضانی
بالا بلند بابا
حاج محمود کریمی
آبروی من
روح الله رحیمیان
@Heyate_gharar</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/662757" target="_blank">📅 22:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662756">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔹
آمریکا محدودیت‌های سفر تیم ملی را برای جام جهانی تسهیل کرد
🔹
طبق گزارش آکسیوس، تیم ملی فوتبال اجازه دارد دو روز پیش از دیدار بعدی خود در جام جهانی، به ایالات متحده سفر کند.
🔹
تیم ملی برای دیدار سوم خود در سیاتل (۲۶ ژوئن/۵ تیر) مقابل مصر، می‌تواند دو روز زودتر…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/662756" target="_blank">📅 22:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662754">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3986f14144.mp4?token=bfQRTkcwNKm512ghfiyszha2GJt9a3ujqmp36Xa0c7qvwpGBPedO9xw2gBhB3ioNwR5qB5HUOeoKcm9mF93HktiyqS-VtpU-Gm_r54kQd58bW9z_hwwG5LgH7gHUriiRkhrTA9000_xKhpB_hDIP_RcsvEOTc6sr92yH9htff8BWZ3JFTFhsF2sF_n0X2R7DaBUV6zeiKchM9tvGH31iL2OBEkaN3KKQ7jm5m86kiuSVshr02Puk53dGnUOrwu6LzztD6WfIZWDR95a__OcjWlxdE3F2dg18Yc7g9mwn5W8jSgmxMts3YvLeA4J-CGBctGR68T1qwV1XxikHM9xMlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3986f14144.mp4?token=bfQRTkcwNKm512ghfiyszha2GJt9a3ujqmp36Xa0c7qvwpGBPedO9xw2gBhB3ioNwR5qB5HUOeoKcm9mF93HktiyqS-VtpU-Gm_r54kQd58bW9z_hwwG5LgH7gHUriiRkhrTA9000_xKhpB_hDIP_RcsvEOTc6sr92yH9htff8BWZ3JFTFhsF2sF_n0X2R7DaBUV6zeiKchM9tvGH31iL2OBEkaN3KKQ7jm5m86kiuSVshr02Puk53dGnUOrwu6LzztD6WfIZWDR95a__OcjWlxdE3F2dg18Yc7g9mwn5W8jSgmxMts3YvLeA4J-CGBctGR68T1qwV1XxikHM9xMlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: ما از ایران برنامه هسته‌ای را می‌گیریم و آنها موافق هستند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/662754" target="_blank">📅 22:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662753">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/608ebe465b.mp4?token=ezKM7UH4iDmd2px85b0er6-WAB-_WiWxTzYRPAHcDNVn3u2yq5CV9hwhYwrg6SWfB7LnN15R3RSws9owrv6ngCWc9_baUjNySX7uT7sp4LDeqZ4gGdZOyfA-0ZhvZ1OJvXrk3Iu4tBo-DBYS8W0QacPwHJk8149c3c2ikgxzVCh9HrT6zvflKd9wRm0xSIpyINBispVAbrQIMNpk3UQ9RckBV2niR19WpSz_pQn6iRLxye9bY0kBIYRmb_W9CrDXRbQ_o9QJ5BwYaAekHZcbpWGAuY_f7zyCeg4j2wkAI3b9PXIFRj7_97CV3tIx-X-AjYWwbDn8kPiW5nCquy4fzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/608ebe465b.mp4?token=ezKM7UH4iDmd2px85b0er6-WAB-_WiWxTzYRPAHcDNVn3u2yq5CV9hwhYwrg6SWfB7LnN15R3RSws9owrv6ngCWc9_baUjNySX7uT7sp4LDeqZ4gGdZOyfA-0ZhvZ1OJvXrk3Iu4tBo-DBYS8W0QacPwHJk8149c3c2ikgxzVCh9HrT6zvflKd9wRm0xSIpyINBispVAbrQIMNpk3UQ9RckBV2niR19WpSz_pQn6iRLxye9bY0kBIYRmb_W9CrDXRbQ_o9QJ5BwYaAekHZcbpWGAuY_f7zyCeg4j2wkAI3b9PXIFRj7_97CV3tIx-X-AjYWwbDn8kPiW5nCquy4fzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت های تکرای روزها و هفته‌های اخیر ترامپ: ایران نمی‌تواند سلاح اتمی داشته باشد #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/662753" target="_blank">📅 22:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662752">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8vUW-Y-C-d0oD67hXERnZkjbyKovQjmC3qm83SDz-Ho3KZJxM7YxaLxyvwJ6O3Bu1uFrlvFUR5BMmA04l716GRcAS7TNvmTI038FGrmwJvvZbXivAjOW0Iw9jTOzHajU8QsG7_frZEOHkMEAqwOerZKQDTT2De6-f1FzxjWEDylsR2O7Xz8s_lm8Oy3-tLFga4FlmZOqao1BnM1ihZ7OirylGl3RCULAhiLkk9Q345pBFfs8_AglPt3geFIv7f6Zjt9RzOHvLBBc9w7vh9rPEC6DK-UpVaHCr3Ei7jBAsC4COUt3wa5zcDYzg8OHwszcKFE4FN4kOfMb-KJe-hjLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل پنجم پرتغال به ازبکستان توسط لیائو در دقیقه۸۷
🇵🇹
5️⃣
🏆
0️⃣
🇺🇿
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/662752" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662751">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ادعای وقیحانه گروسی: اولویت اصلی آژانس، اطمینان از محل دقیق نگهداری ذخایر اورانیوم با غنای بالای ایران است
!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/662751" target="_blank">📅 22:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662750">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/321977f41f.mp4?token=oqPf1jeG82gmaAPj_elljmCrFY-rBjwkfn2hyG0mpTboWpSGOfbODNWIibTUKttdRsb4s65OkAnkmvcoMu2-PAEBzDw__Q6SHK2Mq9j2k9VZLx4R0q98KGk5I3VOdbNsiuweP9qbVcPgjflV-WZB0ngqVAYgGA9Qpc0R_jyvxW-ZPPF_43sqWNY5hRJldH3KI73ObYnf5L1Ak7CoT--7-ZjFCLykxpDpqYacdljotsdcCClIL1c2FtSh6ZHnrZV33YqpbY81ShtlTYelJLBryYjIamXQZ_6m_l2NoeGpWBlLydKODCCDvG1yRKrNAj8AMuRv3srWcISIoKuN1ilRnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/321977f41f.mp4?token=oqPf1jeG82gmaAPj_elljmCrFY-rBjwkfn2hyG0mpTboWpSGOfbODNWIibTUKttdRsb4s65OkAnkmvcoMu2-PAEBzDw__Q6SHK2Mq9j2k9VZLx4R0q98KGk5I3VOdbNsiuweP9qbVcPgjflV-WZB0ngqVAYgGA9Qpc0R_jyvxW-ZPPF_43sqWNY5hRJldH3KI73ObYnf5L1Ak7CoT--7-ZjFCLykxpDpqYacdljotsdcCClIL1c2FtSh6ZHnrZV33YqpbY81ShtlTYelJLBryYjIamXQZ_6m_l2NoeGpWBlLydKODCCDvG1yRKrNAj8AMuRv3srWcISIoKuN1ilRnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت های تکرای روزها و هفته‌های اخیر ترامپ: ایران نمی‌تواند سلاح اتمی داشته باشد
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/662750" target="_blank">📅 22:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662749">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c55523343.mp4?token=FWUCZ-6wu6u2oyX7HLFK8E9SnXi3lj1QDmpRxK5s2mCeguGxaSxq19wBJ97quxLfhZctMi2VcBdMiGxO3vY9gHbE6guwWcbD_4bGxzn8LysUVE4hE6q1zl_QPGjDbIkX4xwSy_zZcdufNwFR45P8jrUg0J0i-eXdIQz2dp1ay1wMW0li2IBkfPdID24upX9B3PyIgGWs9sQ6v9-Cj-Dr_E0TLMzzMkx6X8lW0QBRyPmDD5qes6AdQ94K2Ivrq5TOs43k3vh-RobNEkUSC9utmteFN-gqmbaHGpHZHHoBqUTUknCYkBq6GITxehSUj54-ghPdvIXrGN5s-DqgZPnmnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c55523343.mp4?token=FWUCZ-6wu6u2oyX7HLFK8E9SnXi3lj1QDmpRxK5s2mCeguGxaSxq19wBJ97quxLfhZctMi2VcBdMiGxO3vY9gHbE6guwWcbD_4bGxzn8LysUVE4hE6q1zl_QPGjDbIkX4xwSy_zZcdufNwFR45P8jrUg0J0i-eXdIQz2dp1ay1wMW0li2IBkfPdID24upX9B3PyIgGWs9sQ6v9-Cj-Dr_E0TLMzzMkx6X8lW0QBRyPmDD5qes6AdQ94K2Ivrq5TOs43k3vh-RobNEkUSC9utmteFN-gqmbaHGpHZHHoBqUTUknCYkBq6GITxehSUj54-ghPdvIXrGN5s-DqgZPnmnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل پنجم پرتغال به ازبکستان توسط لیائو در دقیقه۸۷
🇵🇹
5️⃣
🏆
0️⃣
🇺🇿
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/662749" target="_blank">📅 22:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662748">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
شهباز شریف: به دعوت رئیس‌جمهور پزشکیان هفته‌ی آینده به ایران سفر خواهم کرد؛ زنده باد ایران و پاکستان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/662748" target="_blank">📅 22:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662747">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roAE32vtpI88whmVVegfgxbv4j5j9XdOXbsH7O1d4rqGNAmKbCx-bJfgzHQQcgKbw0qL4KiNkvt1epfSTGDfpJ2_zAScoYzLuf5FYHAT9mu0gAnRYfW0wyLowZNdTHn002VDZOZYllpCIeYb-amO0sppfJT0mcmjAT4qqeinxvy0VpP-kjFYikiPvEgkYqLBe-h37l2JVgKixabzddK4SHEryxnTTuTUxnlkooI2U7oLVyTaEB_Zm7XCQCNDKjOnyA1_OkFHb7NfIPNyZrlslmMjqv1U2L_L6TMEZcJkTKUW0XAe-Ht4ZKUP5TxMS1wrisDiWcCL33SgB_ZvWims1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیگران آینه تمام‌نمای ما
🔹
امام می‌فرماید بهترین راه تربیت نفس این است که هرچه را در دیگران ناپسند می‌بینیم، در خود ترک کنیم. چون حبّ ذات عیب‌های ما را پنهان می‌کند؛ اما عیب دیگران را واضح می‌بینیم پس دیگران آینه اصلاح ما هستند. دوری از جامعه این آینه را…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/662747" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKmQDEABzTEzC_Jl8XT98Ibb5WpkuivJXHi4e7Q6Dnk3JzRJ6recIk975VJsNnIl4LKKoOeqMWE9Im7h9VIxXbM2L670wVodpQKpp9peo-IqzMSPudzewvh7Fe79-N2qlk2U6tJMXmDfDZSr7dd7UE4HAHWOr9LRJUlkHi-fKNOK7DWLUPlGHmBoZee75X-MsncGhs4uq3XfVcLCTtuywfXiQ3zPBGwMxieXQ7A_R0y05Bd4T1sx8ig9qJYkmTmSOJ9S_bEj4wdmw0eTzLRrR5um1lbz7PoOZ-ESRUH7-JMS-2G2tfFS_RnRQzt1QDH39ULx_0wfuaa8Jz-szao19g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ueASoJtaJqeG4_GsU419R_8Do9tYY-xR_nZDoExrJv3F8hLVeoyX3eBKzonwUJUiz950-MzSl8FoWN_I-cAfnHJih5wYSrX0XCKEPqsXSAbY8ypDSeYEnIOGS1yQjCHwDiKvLxAay63OpkuVoBW9NlLslew6tVvND1RyFdoQBJ1n1Jsc-7quJNycdydj7x6IGCtyPesjjSZ2WfMCxcFQ8aKjwbFr8dlXq7R-fqh3YQYRfd3v1iTjveiigi9nG460s0o7d7vWa9p7ymvy5h4bKLkzESH9BOAKmv06NLaAS7UGxvq47UVd51FAXTEPmYQmN85fJmAsgpPX_IjsQGacTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qxkH5_L-NvBJrklK12q0_nRWhrRgxFIHSnY-paXw48ART941u66uHJFDufc9MSlQMCNMBxjZZRlZXpw0Rwwn2IDMFY88yTwEgai2SBW4qluX1ysKFf0XhNMZMkAT12PwOkGiYk_omJ4wZNheGtcsDAumhzfeUy82psK42K-M74URzyjpYV1ZTkbwX6npoeKlBX3YMESVTXhoPbejZ3LxyUMHO97SjeU4KsJC9W4dTWJz0_DVI46tvAzfG3UZD1ASj-gKgqds6DUpVeptPAQFm9Kh2n6FFyDbtLhuKDAEIqITxdR2tGcjex3Z26RwL5g90mw_RwzpURK636ZtE4MRyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZSSC_ryqMnqqP7mABHx7yVaLP_Ykl2LhgJXMIW8o2ou1-zyxJsUknS-TUz5gYzEUGTH49q2WLm6w0YhvKh921lzRDIetpFkH8IxWUbnMuzEMaSK61IQWRMgZW0Nt1_8iGfGC2y3ZUyvgREstga53heFo9jheIIxuN81kvo98Bxk_FY1Johsm00ZWwRAh0o-S3-b05aRM7OTSDPiyXZQLxNBSCyTNZuy1tMFDGHz-x5ZMlkSIKvBYKPVDyC_E88EY7cmM0nC4MVKw2gtEqI5dOeGnjb3mlhqoAbXBkrkTiKE-bKuM0VoSVQdwXEIWLmm2M1gXjaMWQ2uswGb3zJcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EkGEljmASmZVKSD1sECTge4SQD1NrbVppOskWrURe_9x-m1sblX3T8J0jvEI9arvLcuIyr2WAEVNHOsjVfSFBDqc3uehPqvuohBLQ_bqUNh3hC0MSPfOLal_mxYRFj3sXkLpfQci5nRsbaYmq7EMRm3O7jqB05hmZChlT3xDyu6U08y7T6ybbO8WT4Odi4s_Kbp8THjRIMMgRpx3zvEZEMzeM2Co1mk8fi6rY76Br_moOEJBwj4oyMm8XxG8ym3pzAAUb1P6QjCuWLmjDIJQUY1YBXXAGkCRMTcZ_IxlQnrXTVNPbhTYZHN6xfYTqxSA4Q39uUKvKLhZYqNB7yO7vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pu9Vu7ScXXzuMfdSRGuFK-BrKbneBAICVDJvfJUxfpGpWCMD_AU7LNMWZEKLSP_4tw35aFWBd5_Jb6dS5PZER3jX_Sob4FtyOBuoSZD6iUZvawDZCa_CO1V2DxhPKCt4jcwcgfpbOY2hBFgBw3JGTpY2a4titadBMuPR5mNIt4khONfJc1r4uK-nMPL2jPNRcOmZEsxoCVzVoD3_f_n-25j_f2eIKXYIG_oCB51BSKKulJFANt3Q-ro1TBYl4-eiR7MLFyQsBE7faHufFCZuDQbNmcH_K_maw5eDU5aFFmksvIytzcjZWrkKDiagejShii_0l7_UrqUVu0747XTKTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hBu2AjF7tSZ-Dyi5fXat7mGQPaKFMacIkVkrKoDfe0jFbtH_ys-QVW4Nshs3e8z8-y6hWYeb3u_lAFRE5K0H_Hsf9lIOqFJBCfe7n6g_4eQNNkn7ADQLAgTcGvGzW8O2nfIs--67WzKsEgwEoNQP4OoFXQAClEOk2803YQ0FwEE2t0oKQgv4jzYofsEviHef1Z0020MObZIvUHMbZGFS8HPgANRBmKjDL_E_ElJcOYFv_B23J8Q66jtu91DIhvsOW9v8Bym4icIJLkhCg1LvBx9IOSJvYjSTz8LsCawRATOLy9vN1lTnmxrLRNB-VPW8NMV7A8BfGbXefuB34JIQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KnYRJN1l3a3YgJUkPotVdDO8mPnhsyVwe3hsH-cYrgLJ4wlfNw83hSylcYMgaZaQAfA5o___j9le6S7YaQYURVCLL3_fCTtVdDEzzdMAKE2LM6Bi-nZRvYPLs4vi4CnhnYaqwIonlFWfe5LZKFh9HbogY7HFazO-xH8kq1sO0-YC3NNdGY3qRYsDUse21CQcE3wbHf0UraTb9-7gff7giODyVg4QS25zGmZ75A7RXfw_WQhB02wQNXdGtvgGrd0nks6ExUuLj7yt6eQb7CU6GJkHFGTLGQ8z5CpbwuNEV0Jyvrr8E1ISFwsgCRxGbsnujBZwwXwALGq4FP8JUzhX4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نشان حسینی
🔹
تصاویر ارسالی همراهان خبرفوری از خانه‌ها و محله هایی که به نام امام حسین (ع) سیاه‌پوش شده‌اند؛ جلوه‌هایی از حال‌وهوای محرم و ارادت مردم به سیدالشهدا (ع) در سرتاسر کشور است.
🔸
تصاویر خود را با ما به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/662739" target="_blank">📅 22:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWKbcTPhcuTd9szdUv4AyKJDjU94BeIQ-toLvB5CQxT_3s2DTgahmRc4mHU2mZyVteSIMSchm1yQpyiUbyEZd1VhlUkDFEzN3sUfj-focNiaOxDee14ySGzUx7gs45kTCF2_YTqfaUJnfwiGuE4qit4SITrku1X3_-nUU8slCgoAYbSOErOt3YvmR6Ab2ryS-DE2eTvOTjEImuE9wZZEPte77uqQX45ROr5A3qva4j43W1eQsdzGh3an24wQYInyPTIcgXhBHbw6YpOnqivmqZF55JtAqJMsW6J0225fZtFuFnfxUd3nPiQrfM_12kHVCv-SOY1ueFn_sb_YIK8Epw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه روند رشد و پذیرش هوش مصنوعی، اینترنت و رایانه در بین مردم
🔹
پذیرش هوش مصنوعی مولد در بین مردم تنها در عرض ۳ سال به نرخ ۵۳ درصد رسیده است.
🔹
اینترنت برای رسیدن به بالاترین سطح پذیرش خود در این نمودار (۹۱ درصد) به حدود ۲۵ سال زمان نیاز داشت.
🔹
رایانه‌ها نیز پس از گذشت بیش از ۲۰ سال توانستند به نرخ پذیرش ۶۹ درصدی دست پیدا کنند.
@amarfact</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/662738" target="_blank">📅 22:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9aa6427e.mp4?token=utZDF4IaYrglNNUgMP1LKsWZD_lUgZBIrWJ7H_yMGBKQav1SVBa6pLrMaqTfKqON-YYPA5wUtMi28V6NqPuXIfCg2mz-kZt7boW4k6rV3jfqxcteDVARsvHBKcWlazPR0n-uSH8hsUOgTYcW1YCT1i1I5SCpZUVP8U41Z6hxNvwcTAkfZuA1iC3-UIqGXlqo_Sza3o-xecroTHyAU5Gsh_mXRfKYRX4MUGNu4Bspdk_JjST_sVp0uk8kplR_t4pa17HHtbLkTHkc_xfE8wOUHvkKopGRj8RzA7TRHrtKnCDULls7STBhwmUUeeL55bV0Mh8KhtYOaiGSZs6dzWIC6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9aa6427e.mp4?token=utZDF4IaYrglNNUgMP1LKsWZD_lUgZBIrWJ7H_yMGBKQav1SVBa6pLrMaqTfKqON-YYPA5wUtMi28V6NqPuXIfCg2mz-kZt7boW4k6rV3jfqxcteDVARsvHBKcWlazPR0n-uSH8hsUOgTYcW1YCT1i1I5SCpZUVP8U41Z6hxNvwcTAkfZuA1iC3-UIqGXlqo_Sza3o-xecroTHyAU5Gsh_mXRfKYRX4MUGNu4Bspdk_JjST_sVp0uk8kplR_t4pa17HHtbLkTHkc_xfE8wOUHvkKopGRj8RzA7TRHrtKnCDULls7STBhwmUUeeL55bV0Mh8KhtYOaiGSZs6dzWIC6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
بلندترین پل جهان که به یک آبشار عظیم تبدیل شده است؛ شاهکار تازه مهندسی چین
🔹
تصور کنید روی پلی ایستاده باشید که صدها متر بالاتر از کف دره قرار دارد و در کنار آن، دیواری عظیم از آب از دل کوه به پایین سرازیر می‌شود. این دقیقاً تصویری است که این روزها از پل «هوآجیانگ» در چین توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/662737" target="_blank">📅 22:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0934803d38.mp4?token=GHmtrkZteqT6K1ba11Ogt5leWy7o5NK9CmQ_eBF6Ld11vceFwNX0-lZ2Amc-ncTUApwjzF1dutpJTjo5vckETMlIBGjmTruBhzRf8FxLpjuENbVzBrq7UF2jSdfAUf_FE_NvPrzFHtaER_tWJK8dZMhmlwa4nsucnH3H_M4x7c8DQXOl3kkOlTORNiOnTgY8gc_Ktpxx3SlXz5RGh5MBWx_DyVQohypRz-JeNsy5p0-GZMghARiG3bJMVXp-nky9qMUD7LXsx9EuaLB-KJnuLK7PqKWS4oDTe6iUlgyVAJ2rwoK-dA6UQ7HfQU7HSxxn4SPESzFMLQM39KBlfbuo6FEgFBaFEqvcE08oqtqBsAKmiUSN_aO7XQhRIYaHQhWxvWA38-vuXJZLDWGb-R_9b2gNLRHnmRqcVJVUSnSG-w1epRnVfYG23SIrqh5AIrRO-8XselgQplOTrB44Z_gy11fY6Dt6qwPvZj9wwFU40yg9eZBPqK2Rk1bkmsNHTxoBqD63CltOEbzME8DycsMu5yqUP7tbCcCIpt50h5txmRL7BGFsPditpqbV29IH7p4au7cS0JXGL_2KCMMge1L3asto45Yh6OYOjc8_uAv9Muh9DTLuEHqlCtKhukJwTW3Y_UDrUi8FG-dFZWVvZJ4Uz9VlO_sFaVQm0PdBD_g1Eso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0934803d38.mp4?token=GHmtrkZteqT6K1ba11Ogt5leWy7o5NK9CmQ_eBF6Ld11vceFwNX0-lZ2Amc-ncTUApwjzF1dutpJTjo5vckETMlIBGjmTruBhzRf8FxLpjuENbVzBrq7UF2jSdfAUf_FE_NvPrzFHtaER_tWJK8dZMhmlwa4nsucnH3H_M4x7c8DQXOl3kkOlTORNiOnTgY8gc_Ktpxx3SlXz5RGh5MBWx_DyVQohypRz-JeNsy5p0-GZMghARiG3bJMVXp-nky9qMUD7LXsx9EuaLB-KJnuLK7PqKWS4oDTe6iUlgyVAJ2rwoK-dA6UQ7HfQU7HSxxn4SPESzFMLQM39KBlfbuo6FEgFBaFEqvcE08oqtqBsAKmiUSN_aO7XQhRIYaHQhWxvWA38-vuXJZLDWGb-R_9b2gNLRHnmRqcVJVUSnSG-w1epRnVfYG23SIrqh5AIrRO-8XselgQplOTrB44Z_gy11fY6Dt6qwPvZj9wwFU40yg9eZBPqK2Rk1bkmsNHTxoBqD63CltOEbzME8DycsMu5yqUP7tbCcCIpt50h5txmRL7BGFsPditpqbV29IH7p4au7cS0JXGL_2KCMMge1L3asto45Yh6OYOjc8_uAv9Muh9DTLuEHqlCtKhukJwTW3Y_UDrUi8FG-dFZWVvZJ4Uz9VlO_sFaVQm0PdBD_g1Eso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قسمت ششم مستند احیا و حقیقت | آیا هدف فقط یک مجتمع صنعتی بود؟
🔹
یا قرار بود با ضربه به قلب صنعت، نارضایتی را به خانه‌های مردم برسانند و زنجیره‌ای را که به زندگی روزمره مردم گره خورده است، از حرکت بازدارند؟
🔹
وقتی قلب صنعت هدف قرار می‌گیرد، پیامد آن تنها به…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/662736" target="_blank">📅 22:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662735">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AacY-pkvqtIb0ucGrYheF3UVn86JEpLvv1DS9cuNURep9yFrkI-dGKE3YVm6wJ4BVGrhIXExUdv-CqqYlEek8alus6hJkOWVAZs0d_7qP-vCu7s4fQkJhliWa44C_kAOy1EpQY2sKuXkwP-TSmF-BXq-3B_YQx-j041dgxhsEz2h4nuczBkYiVYhXafTVA64O-VjxQVlTFOonn7opvdXz6EvUyCvHa5K_k67oCJZEhB5jO9hdRR637F8cZv9DhNWf_Co9A9j9XqNZPK-klSOUhHG96TQCr_VOF1XA_q74ycAJvAUK-AOLtrLf7Lg73QQNplKnmWLkYxRW2gPEWJDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوک‌های رونالدو برای جام جهانی، اسم هر پنج تا بچه‌ هاش روش نوشته شده
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/662735" target="_blank">📅 21:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662734">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1786a48b9.mp4?token=bv_ITvBuJ4F147FSENqa7Vc_sTc4bJZcDpru3a34ALXchnLrcg6zVP95qG51Fj5vKPzFhe1PIZjeudJ6d0aCKE0chLniKMQwx2x6XySd3asTnV4JaJd0EqRdeJ4xtnzdqRXYr_iuS7HDtwJoKdVleUhm0p_jn84S0PDRxOUkJbkgMeIXYr72xf9ZW0tGWfCdJE2DLA5FPhxiU8XBiBSoz0_FhHj49dlMdFX5kgk4ABLHqXDM0n7hOVPKFfjiWTS2F45iPwzo60t2osgGofHb4XkINvUAEWwbM6fnUmtPDPLhLY0lg2Uzo6NqxSM-EAfSQGwZBP7wR0PIMpuK5Apcsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1786a48b9.mp4?token=bv_ITvBuJ4F147FSENqa7Vc_sTc4bJZcDpru3a34ALXchnLrcg6zVP95qG51Fj5vKPzFhe1PIZjeudJ6d0aCKE0chLniKMQwx2x6XySd3asTnV4JaJd0EqRdeJ4xtnzdqRXYr_iuS7HDtwJoKdVleUhm0p_jn84S0PDRxOUkJbkgMeIXYr72xf9ZW0tGWfCdJE2DLA5FPhxiU8XBiBSoz0_FhHj49dlMdFX5kgk4ABLHqXDM0n7hOVPKFfjiWTS2F45iPwzo60t2osgGofHb4XkINvUAEWwbM6fnUmtPDPLhLY0lg2Uzo6NqxSM-EAfSQGwZBP7wR0PIMpuK5Apcsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل چهارم پرتغال به ازبکستان توسط خوسانوف (گل‌به‌خودی) ۶۰
🇵🇹
4️⃣
🏆
0️⃣
🇺🇿
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/662734" target="_blank">📅 21:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662733">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f1536b91.mp4?token=EwVAkkkDTBu9Taxb7EsX5Z5TXbe6rqHk1Wpx71Cf0rThlbHB9Gdd5J3kTLv6XxSv_PCmES9Eu3KmyCGPavuMVxra-7wmti-SUsgfC6lW4XAy8BxEgXvGOC3esPJkhWDQx1vUHahlMwLh0a9SzThaU6fFjl2uHmbxzWH5W-s9qob5HNPx2rjZjIFI8qjoL_8uWEpU7IC-MIaaNjGch5gBMw19k3l_0o3a4Bpq2XQc9DuD5h1s8snOS13H3hjUmkAoK6IKuhKFDt2ks7wYkRWNZ9ZdGpi6n4XA3ALvkdHZGaDEkfX3m9zNJZ7wMDBgYs2IOGP9UMpT3eR79cAajMDrrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f1536b91.mp4?token=EwVAkkkDTBu9Taxb7EsX5Z5TXbe6rqHk1Wpx71Cf0rThlbHB9Gdd5J3kTLv6XxSv_PCmES9Eu3KmyCGPavuMVxra-7wmti-SUsgfC6lW4XAy8BxEgXvGOC3esPJkhWDQx1vUHahlMwLh0a9SzThaU6fFjl2uHmbxzWH5W-s9qob5HNPx2rjZjIFI8qjoL_8uWEpU7IC-MIaaNjGch5gBMw19k3l_0o3a4Bpq2XQc9DuD5h1s8snOS13H3hjUmkAoK6IKuhKFDt2ks7wYkRWNZ9ZdGpi6n4XA3ALvkdHZGaDEkfX3m9zNJZ7wMDBgYs2IOGP9UMpT3eR79cAajMDrrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما خودمان را بدهکار مردم ایران می‌بینیم!
🔹
صحبت‌های عجیب جانبازی که ۴۵ سال بی‌تحرک است در حسینیه معلی شبکه سه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/662733" target="_blank">📅 21:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662732">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a1a142a5f.mp4?token=ZfvFlixgHRQ-msHnHeFFTPcnyZPLRl7sbAspJC-b-S-lBszNVvcgmEKSOghHQnUgg9xHGDFDRdHw2289UNOI2faQl7aZ7XDhQ9E2Eo3D1hjUiSK7zUgia7MeMvnLiOSUiZJDPMxZezjvZmgnRbDazdwR3gxK3nhJtK9q3XD-Ld_5sB7CrrIwJ-WW1xBc-UbkJ2j2SC5qQ-vn0WVJDn8qcQYQAL8qyjYNrcZ59SvF0I_2emHfS0t6yZFwLgJNZ3T8Ty-JqqRGv98GZr2Ry1-CARzarxMKW94-WhEujXsr7LZWauazNvtyajPWqxOqWcTwDa5bwyaIEZBO2zgR1VIKAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a1a142a5f.mp4?token=ZfvFlixgHRQ-msHnHeFFTPcnyZPLRl7sbAspJC-b-S-lBszNVvcgmEKSOghHQnUgg9xHGDFDRdHw2289UNOI2faQl7aZ7XDhQ9E2Eo3D1hjUiSK7zUgia7MeMvnLiOSUiZJDPMxZezjvZmgnRbDazdwR3gxK3nhJtK9q3XD-Ld_5sB7CrrIwJ-WW1xBc-UbkJ2j2SC5qQ-vn0WVJDn8qcQYQAL8qyjYNrcZ59SvF0I_2emHfS0t6yZFwLgJNZ3T8Ty-JqqRGv98GZr2Ry1-CARzarxMKW94-WhEujXsr7LZWauazNvtyajPWqxOqWcTwDa5bwyaIEZBO2zgR1VIKAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ویدیوی اظهارات این زن درباره توافق، در فضای مجازی پربازدید شده؛
«با اینکه توافق شده، چرا هنوز ما تو خیابون‌ها هستیم؟»
🔹
ما تو خیابونیم که امام کشی باب نشه!!!
#خونخواهی
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/662732" target="_blank">📅 21:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662726">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b036d5e446.mp4?token=mGC7tAdw0H2ZhR9hZCSgMwRWimDbuAYjIDfpFaQgJiFvEfVkUKipc8SkkPCCf3WbFfJ2941vhLqUpb0r8oxVPKbuf-DZ4Fdus6eEGfLfAB9CHqrObHPilZXrAv9x9GTdSGLLgqXPA_n9RseGShDUnjDeAbTmoynoYhGkFB7RYhXX4gAd3jopmKUhYTmNqy-dsTEI8ctFxox_soDuTDlSQ7KxmjK6cwi30fXkeJIec6n9V2WsDy_FwPsqUK2_TVQ42yvcdJ1MeCzWCD1KDao5jz1QBef6zofv_rMK_d2HYl9Mpyg7dV2TEpUVJrMlVD2e1kpACwdJdWqTaBIerv-1wVrbsrXFBUmIXnaKm8Lnzs7FV7pbjXo69_iGeveeyoZe78n4mmuFG3aVK4o59XQqlwBHDAdLsBrUTnCdJZKQW6KUbc-dMlg7z9aJTa6cpBZr5r6lTCWdv5AZkpBX2t1jFLT27YPn2cS_YaLNi2AiBPAHU-SAOroNIenJO5DpaLbRRrRGZJ9zPCDUMrKAw3nT3V7QaRrF6ZYV9dPMscuWk5Veyk1h7bYcgaEC5dNF89UrrvIvnAc9wOfm3NZGGswuaZvfaOAwloIAk0o18yYXwo6OYpSsO-v6qREH3XKt6Xr51LNvMmv6DRn_LzXPtAp_yNHGOhlXIsQAidDoq5IsVa8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b036d5e446.mp4?token=mGC7tAdw0H2ZhR9hZCSgMwRWimDbuAYjIDfpFaQgJiFvEfVkUKipc8SkkPCCf3WbFfJ2941vhLqUpb0r8oxVPKbuf-DZ4Fdus6eEGfLfAB9CHqrObHPilZXrAv9x9GTdSGLLgqXPA_n9RseGShDUnjDeAbTmoynoYhGkFB7RYhXX4gAd3jopmKUhYTmNqy-dsTEI8ctFxox_soDuTDlSQ7KxmjK6cwi30fXkeJIec6n9V2WsDy_FwPsqUK2_TVQ42yvcdJ1MeCzWCD1KDao5jz1QBef6zofv_rMK_d2HYl9Mpyg7dV2TEpUVJrMlVD2e1kpACwdJdWqTaBIerv-1wVrbsrXFBUmIXnaKm8Lnzs7FV7pbjXo69_iGeveeyoZe78n4mmuFG3aVK4o59XQqlwBHDAdLsBrUTnCdJZKQW6KUbc-dMlg7z9aJTa6cpBZr5r6lTCWdv5AZkpBX2t1jFLT27YPn2cS_YaLNi2AiBPAHU-SAOroNIenJO5DpaLbRRrRGZJ9zPCDUMrKAw3nT3V7QaRrF6ZYV9dPMscuWk5Veyk1h7bYcgaEC5dNF89UrrvIvnAc9wOfm3NZGGswuaZvfaOAwloIAk0o18yYXwo6OYpSsO-v6qREH3XKt6Xr51LNvMmv6DRn_LzXPtAp_yNHGOhlXIsQAidDoq5IsVa8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ های شب نهم محرم تاسوعای حسینی
🥀
علقمه گفتم و دیدم که عمودی آمد
ناگهان در وسط معرکه سقا افتاد
شیری افتاد ز پا و همگی شیر شدند
گذر گرگ به آهوی حرم ها افتاد
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/662726" target="_blank">📅 21:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662725">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1cfe724f.mp4?token=PlJvcGYvnKttwwvHOXU98VpVSTKCUdpG58mNPbz2_GI77_jcOWF9s4ZurI9nzO0640UviuF02B3r22Gnq8j1YALgz0fMOQQ6sAe5qvAI8KONnS59hqnEGxk4-MS0qlNth7ADKXa1QXAZHsibhX2080AtOCPcYG2xGJsF8st_ezkds1eorpFsqczsjlpoi2mIR9jN_nUxGhVWIoiNKCSgtmwIRUmCE5snMIjh5UNCwuQTghxo0--Ic3bJDP_t0wMSD3G_uNW8S-HDn1khIf_Bow3nLdQl6EyOsaISxCHcCIz7anTRj1X5aHnTTgDwBMnK92nZElwZcCvAGDBKBMtGTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1cfe724f.mp4?token=PlJvcGYvnKttwwvHOXU98VpVSTKCUdpG58mNPbz2_GI77_jcOWF9s4ZurI9nzO0640UviuF02B3r22Gnq8j1YALgz0fMOQQ6sAe5qvAI8KONnS59hqnEGxk4-MS0qlNth7ADKXa1QXAZHsibhX2080AtOCPcYG2xGJsF8st_ezkds1eorpFsqczsjlpoi2mIR9jN_nUxGhVWIoiNKCSgtmwIRUmCE5snMIjh5UNCwuQTghxo0--Ic3bJDP_t0wMSD3G_uNW8S-HDn1khIf_Bow3nLdQl6EyOsaISxCHcCIz7anTRj1X5aHnTTgDwBMnK92nZElwZcCvAGDBKBMtGTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اظهارات تکراری و بی‌اساس ترامپ: ما با ایران به توافق رسیدیم؛ آنها سلاح هسته‌ای نخواهند داشت و قیمت نفت روند کاهشی را آغاز کرده است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/662725" target="_blank">📅 21:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662724">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔹
خبرنگار: بازرس‌های آژانس دقیقاً چه زمانی در ایران مستقر می‌شوند؟  ترامپ:
🔹
در زمان مناسب. هیچ عجله‌ای نیست.
🔹
این ادعا درحالی است که به‌تازگی یک منبع نزدیک به تیم مذاکره‌کننده ادعای بازگشت بازرسان آژانس را تکذیب کرده است. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/662724" target="_blank">📅 21:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662723">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwXrj8xH5eHTcIiDgTj0Tgu8G0wIIH_JjrZQeqijnRXwDo3u7_A-NjHtoz4GOsdE1Nj6QhvmyWKF_erNhoINC-vMwZy-MB1flEASrvlzWge6jjea9yb9WIBYJfMnoLZIaZIn-baSG43dQ2PBwcYeRiThdRgvtBhPPxOf4ORcw_P4B8zhRqjqV-S5yI2TM9nCsZtXXjk-tzBHY5GVjaQyUgSVwLofJFQN3EO94j3uYTX0eXkfOLR0-FOBc1BSM7DrCr-gCkqoJ0gfhzmiwXvNxtxV1orBYuWsjmXjc-fk7l0-ibvJoeqPjSbF2ZK_KM-JkOj4Vwo8nCXHJXIioVKJAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
آمریکا محدودیت‌های سفر تیم ملی را برای جام جهانی تسهیل کرد
🔹
طبق گزارش آکسیوس، تیم ملی فوتبال اجازه دارد دو روز پیش از دیدار بعدی خود در جام جهانی، به ایالات متحده سفر کند.
🔹
تیم ملی برای دیدار سوم خود در سیاتل (۲۶ ژوئن/۵ تیر) مقابل مصر، می‌تواند دو روز زودتر وارد آمریکا شود. با این حال، تیم همچنان باید در همان روز پایان مسابقه، کشور را ترک کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/662723" target="_blank">📅 21:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662722">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔹
نقض مجدد آتش‌بس؛ پهپاد اسرائیلی خودرویی را در جنوب لبنان هدف گرفت
🔹
منابع میدانی گزارش دادند رژیم صهیونیستی در ادامه اقدامات خصمانه خود، با استفاده از پهپاد، خودرویی را در جنوب لبنان مورد هدف قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/662722" target="_blank">📅 21:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662721">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682b273ff2.mp4?token=BfZqEHy6vZx-WsXXEBcHlqZLLceezJH0sqaqoK3UsuhWzuc_EkwOPN1Z1RZlAQUD91mjyH0dzJ1FkM4TMQeIPqb99ZOJhCAitehJpTx2TPIozrCl22fcZJvf_DxQr72mYyZonzWaLEE2dyz-KlhXEcg8EVeKvNG00Bz8OSfv_tIW_bib2NpXX34d0U51cO7Iv6vAQyk75_xAs0X3RShsZea1NN8EIlU0mDCc8XuydRVaFAWLoyZQYOvSSRoG5Ir2lx4EMEPG9HfIC6dWOthR5zyPsi05SrQ8lMzqs1DbnPojdaF2HzwHoQe7QHEvGh0RljiJGI6DawetKEn75t23RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682b273ff2.mp4?token=BfZqEHy6vZx-WsXXEBcHlqZLLceezJH0sqaqoK3UsuhWzuc_EkwOPN1Z1RZlAQUD91mjyH0dzJ1FkM4TMQeIPqb99ZOJhCAitehJpTx2TPIozrCl22fcZJvf_DxQr72mYyZonzWaLEE2dyz-KlhXEcg8EVeKvNG00Bz8OSfv_tIW_bib2NpXX34d0U51cO7Iv6vAQyk75_xAs0X3RShsZea1NN8EIlU0mDCc8XuydRVaFAWLoyZQYOvSSRoG5Ir2lx4EMEPG9HfIC6dWOthR5zyPsi05SrQ8lMzqs1DbnPojdaF2HzwHoQe7QHEvGh0RljiJGI6DawetKEn75t23RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
خبرنگار: نیروهای اسرائیلی امروز در جنوب لبنان آتش گشودند و ۲ نفر را کشتند. آیا اطمینان دارید که آتش‌بس همچنان برقرار است؟  ترامپ:
🔹
خُب ببینید، آن‌ها سال‌های سال، یعنی چندین دهه است که با یکدیگر می‌جنگند باید ببینیم چه می‌شود اما درست خواهد شد. #Devil
🇮🇷
…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/662721" target="_blank">📅 21:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662720">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab9551e892.mp4?token=DO3gY_Eu15yQPZ4fIIGRmwLRK4nW9exWEFaf4pbrAbb_ggOK5ViDm2a5KmcoDLDR4IgLRkPWhQkSYbAWQYyJNf_rfXYAOUstzox4exXMCU3J1wn-Yc7qwTakHYbXxZL6NUXOf-yuqhdmM8Ty2dZjSE1ViQOgj-DslrAYUeRVtfZVdcwbauXiK3k-aiQUoqPSYaE3k0Wb6llfmk9ixFn5M9iwoGzdFzG6D8eXI4hoPVsMdxiIYKMXKYFcd8WLkrjIpAIe5ax0NN1KYbXMkC54CR-uQlzl6qfMTV_OMiVYHekYZd7T7O-KKl33AXxqIH_i2drsyV7hdSau96pvabnRCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab9551e892.mp4?token=DO3gY_Eu15yQPZ4fIIGRmwLRK4nW9exWEFaf4pbrAbb_ggOK5ViDm2a5KmcoDLDR4IgLRkPWhQkSYbAWQYyJNf_rfXYAOUstzox4exXMCU3J1wn-Yc7qwTakHYbXxZL6NUXOf-yuqhdmM8Ty2dZjSE1ViQOgj-DslrAYUeRVtfZVdcwbauXiK3k-aiQUoqPSYaE3k0Wb6llfmk9ixFn5M9iwoGzdFzG6D8eXI4hoPVsMdxiIYKMXKYFcd8WLkrjIpAIe5ax0NN1KYbXMkC54CR-uQlzl6qfMTV_OMiVYHekYZd7T7O-KKl33AXxqIH_i2drsyV7hdSau96pvabnRCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اینفانتینو: جام قهرمانی را با ترامپ به تیم قهرمان اهدا خواهیم کرد
رئیس فیفا:
🔹
ما همراه با ترامپ در دیدار فینال حضور خواهیم داشت، از تماشای مسابقه لذت خواهیم برد و جام قهرمانی را نیز با هم به تیم قهرمان اهدا خواهیم کرد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/662720" target="_blank">📅 21:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662719">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f22bbcc771.mp4?token=sljSzuc11WUOYRkZyZoc83wGPD6prx_M3ElvN28ZRpFS9gpBV46hz-rCMlQlyjiObZAVKqGxNKHQg1ifO-gQl8-LAGg2Qwxk7dHbVbGeFQvhjwkDRY31K_mbmAa2lGxkEN2APhojooZluW6-UM7_wxRRB0PI-wkfW-tmmSuCbMv8Ir-o2EBjLdqiYVk_D91CCslnPN57ognIK44esahSr2XEmg_fbtVBUALTzqXBMApr19vQqJ77BNjdH7rWVeuPPpj_n6y5QSJYpoK3_SnlUeswOnx9NW9c6kPdSWRlJFhiAJeB2N9XMXqKOOSxVvkmTfBfcYSN-2HspKh6VnnsJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f22bbcc771.mp4?token=sljSzuc11WUOYRkZyZoc83wGPD6prx_M3ElvN28ZRpFS9gpBV46hz-rCMlQlyjiObZAVKqGxNKHQg1ifO-gQl8-LAGg2Qwxk7dHbVbGeFQvhjwkDRY31K_mbmAa2lGxkEN2APhojooZluW6-UM7_wxRRB0PI-wkfW-tmmSuCbMv8Ir-o2EBjLdqiYVk_D91CCslnPN57ognIK44esahSr2XEmg_fbtVBUALTzqXBMApr19vQqJ77BNjdH7rWVeuPPpj_n6y5QSJYpoK3_SnlUeswOnx9NW9c6kPdSWRlJFhiAJeB2N9XMXqKOOSxVvkmTfBfcYSN-2HspKh6VnnsJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
خبرنگار: نیروهای اسرائیلی امروز در جنوب لبنان آتش گشودند و ۲ نفر را کشتند. آیا اطمینان دارید که آتش‌بس همچنان برقرار است؟
ترامپ:
🔹
خُب ببینید، آن‌ها سال‌های سال، یعنی چندین دهه است که با یکدیگر می‌جنگند باید ببینیم چه می‌شود اما درست خواهد شد.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/662719" target="_blank">📅 21:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662718">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8499bbd275.mp4?token=cwpcj3rDWneEG5cBu7vjVf7j3izvPGi4-Z0igCz9gHrjBRJvUgiVyI7zBbpkYFUv6YccNOdRsBDUVa9SjqbK4BzVDc-vCWYGaxk0ug8TzeuNrkTLm8i0t3Ura8i4OJLeKaUfnN7VKSSaCY9atFIV6wuKTLnwQjo6BURHVweyvec_BUbSZum4WO1DAYFquFOAqSEY96-1m6arqlZZAiosrIlWIZqLu5PQ6VGSW4erTiMikiV59CiYV_-0cHZOQXfc6Bx4s0cL2FTTlZGciALTmDZiHA52m-VCyG49lNl1JcsSxT68htpUql89unAfnKLjVNZY-iDBle1MvhwyzOb91w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8499bbd275.mp4?token=cwpcj3rDWneEG5cBu7vjVf7j3izvPGi4-Z0igCz9gHrjBRJvUgiVyI7zBbpkYFUv6YccNOdRsBDUVa9SjqbK4BzVDc-vCWYGaxk0ug8TzeuNrkTLm8i0t3Ura8i4OJLeKaUfnN7VKSSaCY9atFIV6wuKTLnwQjo6BURHVweyvec_BUbSZum4WO1DAYFquFOAqSEY96-1m6arqlZZAiosrIlWIZqLu5PQ6VGSW4erTiMikiV59CiYV_-0cHZOQXfc6Bx4s0cL2FTTlZGciALTmDZiHA52m-VCyG49lNl1JcsSxT68htpUql89unAfnKLjVNZY-iDBle1MvhwyzOb91w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم پرتغال به ازبکستان توسط رونالدو
🇵🇹
3️⃣
🏆
0️⃣
🇺🇿
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/662718" target="_blank">📅 21:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662717">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbJK_i2hnPkr-SJolcON7-Ks-7sbsloKYO0rCcLQhPMo6by4zL8Fhdw4E3cjU9mdZGONn6lkKg_Iz9OZDWlUWRoYjFIQtMi_fjAgMOAelh4IA4pL96Rr_Tpva7Zn7TlONRsxaOODtlcmpqjntPn7lS20HLPZZcLdpXjuwIsmueDXDTuu4WiFqpailSNlzAZ7OovzcPKI35SbVY-Nt1BkVcerZMWSHtfQPUhyrkfvs4UjxQagHgNngt7vnj4yO5JIyJTHQQpTzhjVuGkIN4XZFrxd94rkF8nEJf71GmIxw7gsinfNYgzMrc-BOXUVJKr4nDzpLxKygq62n2o2comCag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«میدان مین هوایی» ایران | روایت خلبان آمریکایی از سقوطش در ایران | پهپادهای شبح‌گونه در آسمان؛ خلبان آمریکایی چه دید؟
🔹
خلبان آمریکایی که جنگنده‌اش بر فراز ایران سرنگون شد، روایتی عجیب و بحث‌برانگیز از لحظات پیش از سقوط هواپیما ارائه کرده است؛ روایتی که از مشاهده گروهی از پهپادهای ایرانی با آرایشی غیرمعمول و شبیه به «عروس دریایی» حکایت دارد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3225246</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/662717" target="_blank">📅 21:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662716">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
رفع اختلال تمامی بانک‌ها تا پایان امشب  بانک مرکزی:
🔹
اختلال خدمات کارت‌محور در اکثر بانک‌ها که اقدامی پیشگیرانه برای حفظ امنیت بود، برطرف شده است؛ خدمات بانک‌های ملی، صادرات و تجارت نیز در حال بازسازی است و پیش‌بینی می‌شود تمامی خدمات بانکی تا پایان امشب…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/662716" target="_blank">📅 21:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662715">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5fcDatMwulBa0oZxNKUcNINwf7fdNs-U9x9aXG6Zqtj7bdcTLmD1Va06TwvMGlHN0-EsMMxpKg6V1vw29DAQZeMB6YjrGINpRLKXMfYA43SVBdbqV5kZQ7W4wgw4C_AIFvyxF8Q1dmDjBI_W3bIXbO3GTLFvmaKDbVl9NeusTNk0WRi1GrCL23aF_5oua7pNcHZUEkJnedeE_rKFoCWSHYjtkQWFfHRm3jvpT_BW5NUYbQddvEUE4eMQ6W6G0qYuy_3G7ahPFElfqT3ptzyIjNP62P7YjHXe50oEera_-7aW0TnYAsaMQ-NDAInQksW64SeZLzHPUIXtc8uUwOPOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد تاریخی رونالدو در جام جهانی ۲۰۲۶
🔹
کریستیانو رونالدو با گلزنی مقابل ازبکستان در جام جهانی ۲۰۲۶، به نخستین بازیکن تاریخ فوتبال مردان تبدیل شد که در ۶ دوره متوالی این رقابت‌ها موفق به گلزنی شده است. این گل که در ابتدای بازی به ثمر رسید، به انتقادها علیه این ستاره ۴۱ ساله پایان داد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/662715" target="_blank">📅 21:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662714">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
فارس: منابع عراقی از شنیده‌شدن صداهای انفجار با منشا نامشخص در اربیل عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/662714" target="_blank">📅 21:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662712">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6de535625.mp4?token=Rtl59LzwnWfaxb7MAmT6o38djqvmzYXudtxVH4JHXZo0qCtQ9iQZcrFyhuNWQ_HTnKAXjGjz5BZXqGqhXZKj0fSxA-qVVeQYd2Fv8yiTpuazuCj7Qxl4afBrwLPi6eBCsJTvCV06-iOYpqnTJS6956af_1HvgkShg419SKX1I3IzTIv0E-WIJqME3dafwSvK6uJwU8o93aEMNuktIMf6-azu7D0DlSNGOAm8pOART5mhjwG-7ClEwgfGrGUGW5Q38a2x5-xHsRbeQCl3TnVH3nfhyRmfqWS2tiq35mHlFprDr1GBVA5_aYhC9L5Hescgb0r6h30djWkyRVSLOJST-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6de535625.mp4?token=Rtl59LzwnWfaxb7MAmT6o38djqvmzYXudtxVH4JHXZo0qCtQ9iQZcrFyhuNWQ_HTnKAXjGjz5BZXqGqhXZKj0fSxA-qVVeQYd2Fv8yiTpuazuCj7Qxl4afBrwLPi6eBCsJTvCV06-iOYpqnTJS6956af_1HvgkShg419SKX1I3IzTIv0E-WIJqME3dafwSvK6uJwU8o93aEMNuktIMf6-azu7D0DlSNGOAm8pOART5mhjwG-7ClEwgfGrGUGW5Q38a2x5-xHsRbeQCl3TnVH3nfhyRmfqWS2tiq35mHlFprDr1GBVA5_aYhC9L5Hescgb0r6h30djWkyRVSLOJST-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
️من عوض شدم ولی
تو حسین بچگی‌امی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/662712" target="_blank">📅 21:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662711">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f0e9c8ab.mp4?token=cO4KOe_LbJOUVzsjsXC31SJ5G-n8MNZPamNCkMPgnxi13XTUpmJnrpb1PySOhmD-DvU78X7S4b_AuLo-MymX4Bx4ECFb1hlVszhCtnvCDiaS8LgeUcBdc1bCCumN9EktE-BHzyO-enQ_GiMQutFNTECp4OUQYv8pTi1D4aOXovibuo3gXRsEIdTjW7Dz6MyoFiKvAFLMHj5QJPcWmIGlB3xkjJ4-giDMBfo0357NExwLptkX6HklU9t0iiVPSuM_1YUifkpZxdslteLdOhxM2OUxsZ4kEbqgkR54CP6SzD_HPSqkW1pOdyUJsL2P4HeDGk4PVoASVX9kZVXfZgrd5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f0e9c8ab.mp4?token=cO4KOe_LbJOUVzsjsXC31SJ5G-n8MNZPamNCkMPgnxi13XTUpmJnrpb1PySOhmD-DvU78X7S4b_AuLo-MymX4Bx4ECFb1hlVszhCtnvCDiaS8LgeUcBdc1bCCumN9EktE-BHzyO-enQ_GiMQutFNTECp4OUQYv8pTi1D4aOXovibuo3gXRsEIdTjW7Dz6MyoFiKvAFLMHj5QJPcWmIGlB3xkjJ4-giDMBfo0357NExwLptkX6HklU9t0iiVPSuM_1YUifkpZxdslteLdOhxM2OUxsZ4kEbqgkR54CP6SzD_HPSqkW1pOdyUJsL2P4HeDGk4PVoASVX9kZVXfZgrd5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
​​
ای اهل حرم، میر و علمدار نیامد...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/662711" target="_blank">📅 20:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662710">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4Q8cxdm7l4HExSxa5K2Pi7ezjUbZMhDKhJRr4xyGvsVJ0iQa_ZR0CcW0M_qr207CXkzaItZkK6d7UAjYWb47s0073ch3nwcmozyG5RfBNyKDiRuwQij2HqtvXa8tgjNLnCk7j_2LSnmxyPx2iy63zHUlsFVWOkCwiu-Qaj1IMlxthLaBGiMSxjEYPl3MHaRpEw74XatQVEj2wFgsRspJaJ1MpyvI_ikhANkKkDxk4nJj_oWAHOgquMM0QEvj6bUZOVMd6iSMvHaV4ewVDBmikRcOsuxMe9LNb-V4SQxJges397EG_PFQ2BlV5WYGaPsnlJxtLhazfz0vJQghnVsSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیچ کجا از چشممون دور نیستی...
Everywhere you go... you're being watched
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/662710" target="_blank">📅 20:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662709">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30c0253cb8.mp4?token=oPJ7_gOKVyBaCrreZbmR38K2O4zyHN2pPupFnXWfruXwodaxt4OsD3WwQMUwASGCrTF8dYdaTZAzpMFyghEkaSwS2Fch94i_9jvy0scw9dx3SPk_dkrNQKiw2zlXbHLYb1drndxHEyqAFUNWKZYEUk6COPqRylQqlZF6pS_wUmVIcrIWlFY85bxDnBOoAuq_4N_j5i2S3ejElxYqb2nVie6wIyuH_cWgvKT0fEwvFv023ueyxhhUV6H2Y1QRNjuq27onVTiV831nCwBGocjO4NSZV8P4YpAAeiCro9CC0wS7pe-T2Fs39KaMQdPeXa7QQCUM3XknF6u0RHPVxeo67Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30c0253cb8.mp4?token=oPJ7_gOKVyBaCrreZbmR38K2O4zyHN2pPupFnXWfruXwodaxt4OsD3WwQMUwASGCrTF8dYdaTZAzpMFyghEkaSwS2Fch94i_9jvy0scw9dx3SPk_dkrNQKiw2zlXbHLYb1drndxHEyqAFUNWKZYEUk6COPqRylQqlZF6pS_wUmVIcrIWlFY85bxDnBOoAuq_4N_j5i2S3ejElxYqb2nVie6wIyuH_cWgvKT0fEwvFv023ueyxhhUV6H2Y1QRNjuq27onVTiV831nCwBGocjO4NSZV8P4YpAAeiCro9CC0wS7pe-T2Fs39KaMQdPeXa7QQCUM3XknF6u0RHPVxeo67Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم پرتغال به ازبکستان توسط نونو مندز
🇵🇹
2️⃣
🏆
0️⃣
🇺🇿
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/662709" target="_blank">📅 20:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662708">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d170c843.mp4?token=JSbj4cEzeiuKHIrQe06RuJ3cQ-cW2MJxJ7St0amhmxicfOVxyA7Tbnq6kswHxwHLngIe3KDEUdhguBM5xkmwS4ilkWVbH3iFweqSmKEKd-Qe6MoQJL6bEv30_0jXeuU64gGHHfh_-UukKkk1DJbnn3Xnh2BP7VhBjaIk-BZgfE6AoQ9SIp8ao-Xrx65NOCvJFwPtKr0FmAI55Qz4KEIKYvdXBbZRy4aJ7ayGtLVg3eH3SpbtTV5U-_9l8HwHTO8pDWNVcIwP_bAw-OZnJTAX2QEl_mR0KDXYCzNpaO8HiUmcMkpMxw_kTsHL9YOJfl_yvHU6Dgdw0hn3J8y63yLcww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d170c843.mp4?token=JSbj4cEzeiuKHIrQe06RuJ3cQ-cW2MJxJ7St0amhmxicfOVxyA7Tbnq6kswHxwHLngIe3KDEUdhguBM5xkmwS4ilkWVbH3iFweqSmKEKd-Qe6MoQJL6bEv30_0jXeuU64gGHHfh_-UukKkk1DJbnn3Xnh2BP7VhBjaIk-BZgfE6AoQ9SIp8ao-Xrx65NOCvJFwPtKr0FmAI55Qz4KEIKYvdXBbZRy4aJ7ayGtLVg3eH3SpbtTV5U-_9l8HwHTO8pDWNVcIwP_bAw-OZnJTAX2QEl_mR0KDXYCzNpaO8HiUmcMkpMxw_kTsHL9YOJfl_yvHU6Dgdw0hn3J8y63yLcww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریستیانو با‌ گل برگشت؛ گل اول پرتغال توسط رونالدو در دقیقه۶
🇵🇹
1️⃣
🏆
0️⃣
🇺🇿
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/662708" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662706">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vOEyrKsOfUbDAft77WliF2EGJh47NJmG8nq9mTh8c7rUineQbXOFlV0xLbBxmF-bF99ucVJXIbbQEUtoal84sF8FKPNKIDgvabjdu46Fa4_hD2CShrX7oFnIOjKCzi1HNGyKKqeQ7MD8P9fhjMUWgyJkkGtRlr-LK8PIUrtG-8CR6XgoBDal3elwM8GdMQqLWAVlaPUNLuhT-aKHbXEGZKJ-1A9HD9p_AXxyzLsaWrExBmyEpz7YgQc_ARMmkkdVcM-pHMEY2JYtX7l04pEiCaeC5q-yAdid4TYrg-UZTXviQbvFloNuK2omhbEGFQb6tctTFmLEsAQvdYDEK0bQkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DlWKJiPEkiCH1LdnGuyLinUFdgVg_Q1JsZ5MjnKNfoyI7FxbFd90gvgdDBr9uvcy2dQWatOtpz4qOA2Zfs8yP8Nl3rjQG-wUpf2ZZK7hw-y18aG1eBTOUSlz3jfGqMfF99Oybk1IWdb5ufuMKNzEUwj4xVDZY47d9PpSPZ4UB6T06CgBFKCSEFnZaffOUM_TfxqArL29PHZT_kVUHbMz260f-03SiaXlB1GRa7yO3ETcKMJcAUY2OfiP2xwLqrZj2J2nNf0nGyE3Gzr8ZhkzEoee3pvHrvwZKHVZ8dAbG0_OpWJsZv4FsYZ1C6cdqeiAhn4q2ZYnQg_RtjcXNhOuMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آیا می‌دانستید هدف امام حسین (ع) از قیام عاشورا، تشکیل حکومت بود؟
🔹
کتاب «حقیقت عاشورا» محققانه‌ترین کتابی است که درباره اهداف امام حسین (ع) و علل عاشورا نوشته شده است. این کتاب بسیاری از تحریفات عاشورا را روشن و تلاش می‌کند تصویری واقعی از عاشورا ارائه…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/662706" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662705">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
هشدار دادگستری تهران درباره پیامک‌های جعلی خدمات دولتی
معاونت دادگستری استان تهران:
🔹
پیامک‌های مربوط به خدمات دولتی از جمله ثنا، یارانه و قبوض خدماتی هرگز از شماره‌های شخصی ارسال نمی‌شوند.
🔹
تمامی پیامک‌های مربوط به خدمات و اطلاع‌رسانی‌های دولتی صرفاً از طریق سرشماره‌های رسمی و معتبر دستگاه‌های اجرایی ارسال می‌شود./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/662705" target="_blank">📅 20:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662704">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
چرا با اینکه دنیای پس از مرگ را دیده بود، به اسلام شک کرد؟
🔹
00:03:20 عوامل محیطی که باعث شک من در حقیقت دین اسلام شد
🔹
00:08:20 حس خواندن نماز بعد از ترک یک ساله آن
🔹
00:22:00 تجربه درد وحشتناکی که ناخودآگاه مرا به ذکر گفتن وا داشت
🔹
00:35:20 درک احساسات همسر توسط روح از کشوری دیگر
🔹
00:38:50 خشم و نفرت دختری که مرا در کودکی با او مقایسه کرده بودند
🔹
00:49:00 التماس به پیشگاه خداوند برای بازگشت به دنیا در سومین تجربه
🔹
قسمت نهم (بی تو مهتاب)، فصل چهارم
🔹
#تجربه‌گر
: فاطمه سجادی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/662704" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662703">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVPQOXRH1qMVvL2-LFxJbHhbcjrYQW2_WmqBLkkIMlimiwMyk3LrGYtxPTKr4n5XzY6Z6U1idhzrV-cWy7dfGrR38pu7x5ENCDSby4AK6VchTEa4l1YpOxV7nIFOJy4RhxrBupOdSua7TIAvmqdT7XE4ihY4UOYMBgx_9gRR4OXkG6hJfxjLxk39Ze1pyaXdeSLLbgPFcvsxw4v6HA4a3M1asvdnXkahN4Acf7XRdXWBOTamHCwJr4vyYR4rANqbPISSRG2fZ381yHkkSHG7G69cwedgaKBk8wvxGkU8rIWN-OKHv3ZTyqCZiXpJYw3UTBLV5kkKt0DUgmx719yPNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایگاه بصیرت به نقل از
سعید جلیلی: به هیچ وجه منظور رهبری از بیان جمله «بنده علی الاصول نظر دیگری داشتم» مخالفت با اصل مذاکره نبوده
/
انتقاد سعید جلیلی به ارائه اسناد دارای طبقه بندی توسط یکی از نمایندگان مجلس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/662703" target="_blank">📅 20:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662702">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8e3aa64f2.mp4?token=bZmxdEjkMl4_AvsjKEnVwYloV14qqwrO4nB_PC6cCKfjxNodtMUs_P7hNGtk810UH4Y2fKqcsbF7zdR0EDINuHUce-2blaONvWjqcpQGRgpfahU4gzpxwboWFXiMo8X0ZSaJE0qlHRIDcn5Lzc8On4aDF-klrIo4JN0re8C21yY7D4k_TTL-Pcz7aHArLpfDflSDqCv5XVSHc1D5cn70uzJZ0YlbKdlnDji_7MVOhIuv7-uMIz-T6q12oOUNvCi11bmk58hDk6HJXJ2eFFisPQg7itxMaD9NxHoPZnqTPN_gxwclSY0geen44mDWsGip1mlnJepLZh_eMavDKJE6Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8e3aa64f2.mp4?token=bZmxdEjkMl4_AvsjKEnVwYloV14qqwrO4nB_PC6cCKfjxNodtMUs_P7hNGtk810UH4Y2fKqcsbF7zdR0EDINuHUce-2blaONvWjqcpQGRgpfahU4gzpxwboWFXiMo8X0ZSaJE0qlHRIDcn5Lzc8On4aDF-klrIo4JN0re8C21yY7D4k_TTL-Pcz7aHArLpfDflSDqCv5XVSHc1D5cn70uzJZ0YlbKdlnDji_7MVOhIuv7-uMIz-T6q12oOUNvCi11bmk58hDk6HJXJ2eFFisPQg7itxMaD9NxHoPZnqTPN_gxwclSY0geen44mDWsGip1mlnJepLZh_eMavDKJE6Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: هیچ‌وقت و ‌هیچ‌گاه برای توان دفاعی ایران با هیچ‌کس گفت‌وگو نخواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/662702" target="_blank">📅 20:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662701">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44278c8202.mp4?token=s6D1iV0DLOMlZr24GJLJBhbbn4DQRJGLhkqSTnU5OI9dhUKVZe76eeLZXx1VXyJaShVPuuY1QzRmRiNR6M3FtVLSxVd-RPrluyP-L0-6z918IdKD1p-UomO3VlbeC8Ng1ozYp0nDi9e1VRPAL-H7ik8-KYzPhl35CN3P3nJylQUAQcITxb1VMSga93X6yVS8ol6AJlopTPtpcJn97NHATzTDdoj1_gNFT4qWILrSkrtCK1iPk7vfFMa4KhwTeON27Yeza0WwBaHXKvblENCN8k_QKOXLodtebnSj9b56Vc92GpDlHPsEhMrlNs-TuPWNwBBCLpe4mwkNR6ZNSbvqM2S9gAcQT9VIB4t7xGUP8XddjYvga96D0j8w93Zo-WWqebdfHMzZ4G3lFH-6Wfx9mafN2ajsVKlMeDuz9F-psbUZkJKA4cZ9nG9OPtEHQ-cYS_DRIYTAYnR8L8AkWwbDsz5TMw5-Bc0r157Vkl7SOEVhFqPZBby6m8A-4QrqLNX8KyiYzUEVayUGeblu6oV_JJTnnLc28hWvVURwmRXQTW8-KAMQ91-DGEm7nt2OO8ht635nmgwFqy-DFvgCvY4IRbPSB9fxUF5vRhkyfAQCmur9YgaX87rEpZ1cGvqk1FuwHmOEWUwQeRCwFF8xIV7vgqpL97UAyQ-GKR81T21ZqFc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44278c8202.mp4?token=s6D1iV0DLOMlZr24GJLJBhbbn4DQRJGLhkqSTnU5OI9dhUKVZe76eeLZXx1VXyJaShVPuuY1QzRmRiNR6M3FtVLSxVd-RPrluyP-L0-6z918IdKD1p-UomO3VlbeC8Ng1ozYp0nDi9e1VRPAL-H7ik8-KYzPhl35CN3P3nJylQUAQcITxb1VMSga93X6yVS8ol6AJlopTPtpcJn97NHATzTDdoj1_gNFT4qWILrSkrtCK1iPk7vfFMa4KhwTeON27Yeza0WwBaHXKvblENCN8k_QKOXLodtebnSj9b56Vc92GpDlHPsEhMrlNs-TuPWNwBBCLpe4mwkNR6ZNSbvqM2S9gAcQT9VIB4t7xGUP8XddjYvga96D0j8w93Zo-WWqebdfHMzZ4G3lFH-6Wfx9mafN2ajsVKlMeDuz9F-psbUZkJKA4cZ9nG9OPtEHQ-cYS_DRIYTAYnR8L8AkWwbDsz5TMw5-Bc0r157Vkl7SOEVhFqPZBby6m8A-4QrqLNX8KyiYzUEVayUGeblu6oV_JJTnnLc28hWvVURwmRXQTW8-KAMQ91-DGEm7nt2OO8ht635nmgwFqy-DFvgCvY4IRbPSB9fxUF5vRhkyfAQCmur9YgaX87rEpZ1cGvqk1FuwHmOEWUwQeRCwFF8xIV7vgqpL97UAyQ-GKR81T21ZqFc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥀
شهیدی که دو بار جان داد!
▪️
در واقعه کربلا، فقط یک نفر است که «دو بار» جان داد! او «سُوَید بن عمرو» است آخرین سرباز عاشورا..
@Heyate_gharar</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/662701" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662700">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6f6170a9.mp4?token=u-forMilTHl_vbeSmYf7-DPmTGFi8kkIbHLL1UNySqARoxWelbLJ85ujvrB9DmuvDHKbR24LZOCKI7AqtKauskxqfO71XxL0D_ogNGiiTKO3JRQJyclH_6A2rXOHqjjUbG4kDTQP-_iPMsm7kSc5J1kVi0_QUkoA-__4-OKGY6DI6I32cLszy7rWs1ejtKhtWsQtLuFsJ4X8JAxr-c_z34BIW1HNv36n0f2kh2G4pkd8yIKiilDgc6JLrgqIOEpblzt7Hl7SWDYP4eYzTFl0wp5W1lIxefUS68kAldHhfJVxsVo1W7TRhTkyHpcDGfgTx7efNiP5j-XZGiPmSMCzdAJuxPfLJhQbCIWxXIBJUZ3Xx2vPqHsz_QbNK6CA-qwoqqW72S3IghwAXK7auh4yuYcOZE-MXMAt8U9o6kLTUcrrwMrv9VldNd__LFouNL0gbY-Dnyu-gWnfq3C2Sv2eC1fC4BoAKQfeBecuj1R8qB5z0gDYEeG-CiQ8SVSapCLIZLp-kpWVkyVwNaa0po49-oEQPx974DC29amtKYX39pVsecSvr7vPFAT9D0IxoDXaZDit5NMAFRFvCsQLdfzFfsajpcRxu1ysVxhWjJ44pL-TMn4TheyHXrJsiBcOwBYkL1W4CxOHu-i-0yupeW3L9tWhPI-99gZ7Ya_YY6ROZSI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6f6170a9.mp4?token=u-forMilTHl_vbeSmYf7-DPmTGFi8kkIbHLL1UNySqARoxWelbLJ85ujvrB9DmuvDHKbR24LZOCKI7AqtKauskxqfO71XxL0D_ogNGiiTKO3JRQJyclH_6A2rXOHqjjUbG4kDTQP-_iPMsm7kSc5J1kVi0_QUkoA-__4-OKGY6DI6I32cLszy7rWs1ejtKhtWsQtLuFsJ4X8JAxr-c_z34BIW1HNv36n0f2kh2G4pkd8yIKiilDgc6JLrgqIOEpblzt7Hl7SWDYP4eYzTFl0wp5W1lIxefUS68kAldHhfJVxsVo1W7TRhTkyHpcDGfgTx7efNiP5j-XZGiPmSMCzdAJuxPfLJhQbCIWxXIBJUZ3Xx2vPqHsz_QbNK6CA-qwoqqW72S3IghwAXK7auh4yuYcOZE-MXMAt8U9o6kLTUcrrwMrv9VldNd__LFouNL0gbY-Dnyu-gWnfq3C2Sv2eC1fC4BoAKQfeBecuj1R8qB5z0gDYEeG-CiQ8SVSapCLIZLp-kpWVkyVwNaa0po49-oEQPx974DC29amtKYX39pVsecSvr7vPFAT9D0IxoDXaZDit5NMAFRFvCsQLdfzFfsajpcRxu1ysVxhWjJ44pL-TMn4TheyHXrJsiBcOwBYkL1W4CxOHu-i-0yupeW3L9tWhPI-99gZ7Ya_YY6ROZSI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشریح جزئیات اقتصادی تفاهم‌نامه ایران و آمریکا از زبان
همتی
رئیس کل بانک مرکزی:
🔹
در جریان مذاکراتی که با دولت آمریکا انجام شد و دولت‌های قطر و پاکستان نیز به‌عنوان میانجی همراهی می‌کردند، دو تصمیم مهم در ارتباط با بخش اقتصادی تفاهم‌نامه در سوئیس گرفته شد.
🔹
اولین تصمیم، مربوط به آزادسازی منابع مسدودی ایران بود. بر اساس تفاهم‌نامه، مقرر شده بود که این منابع به‌تدریج و در جریان مذاکرات آزاد شوند که ۱۲ میلیارد دلار آن در مرحله اول و مابقی نیز در مراحل بعدی آزادسازی خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/662700" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662699">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
شیخ نعیم قاسم: اسرائیل راهی جز عقب‌نشینی از خاک لبنان ندارد
دبیرکل حزب‌الله لبنان:
🔹
پروژه نابودی حزب‌الله شکست خورده است.
🔹
اسرائیل راهی جز عقب‌نشینی از خاک لبنان ندارد.
🔹
صبر ۱۵ ماهه حزب‌الله به معنای عقب‌نشینی نبوده، بلکه بخشی از استراتژی آمادگی و آماده‌سازی برای مرحله‌ای سرنوشت‌ساز بوده است.
🔹
حزب‌الله با تکیه بر حمایت‌های تهران، قدرت خود را مضاعف کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/662699" target="_blank">📅 20:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662698">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
شهباز شریف: به دعوت رئیس‌جمهور پزشکیان هفته‌ی آینده به ایران سفر خواهم کرد؛ زنده باد ایران و پاکستان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/662698" target="_blank">📅 20:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662697">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
روبیو، وزیر امور خارجه آمریکا: ما مستقیماً با دولت لبنان سر و کار داریم و پرونده لبنان از ایران جداست
🔹
اگر نیروهای نیابتی ایران موشک پرتاب کنند، خصومت‌ها در منطقه پایان نمی‌یابد.
🔹
هیچ کشوری مجاز به وضع عوارض یا مالیات بر آبراه‌های بین‌المللی نیست.
📲
🇮🇷
…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/662697" target="_blank">📅 20:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662696">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_gy1JaoT9BaTDrk87Gabry03F5xWOuxklEhGnmlVfgaqzrBvBN7OhKf3S_JDjLAdrZC7v5TNKGy_M-_Oa_pNgRX-owGxU8x0H_0LyXTJdAKeBQQAe0eEA6x5p3okxd3s9edD8pfHoEWjs3GEzjGcqSFGBeAzALbB6eNuqho0urb1Yeooy-Mj5LIXt0bD7MJSqUcyNn9Yu6I-Rp1af5Tf65NVRlLOWdis4ry8U-CbJT73j0t9wCjjKYbH13x_SR98mbWREPBThm4ClRzqCRFOMtgTkdXDJMofEl35_WOzR_E5PWwWveVluW1cQfV1uYbdUTuo-ysX-I35ZT3lA5Hrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگترین مجموعه اختصاصی ساعت در ایران
❗
❗
بازرگانی ساعت امامی
🔸
ساعت موادو فقط 788 هزارتومان!(قسطی)
🔹
ساعت زنانه از 200 هزارتومان!(قسطی)
🔸
ساعت ست از 575هزارتومان!(قسطی)
🔸
ساعت مردانه از 250هزارتومان!(قسطی)
💎
وارد کانال شود و تنوع محصولات رو ببین!
👇
👇
https://t.me/saateemamii
https://t.me/saateemamii
⚠️
پرداخت در 4قسط بدون سود و کارمزد با ترب پی
📣
فرصت رو از دست نده و وارد کانال شو
👇
https://t.me/saateemamii</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/662696" target="_blank">📅 20:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662695">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/623a9a2ab6.mp4?token=bEjhaagOXUpZfdIQ-TIMsPzRU9T4CSkPNodRgw9U59HzsDJE7KgMnw1u1tPUpAE95VH6n9nldN5c-rSKGS7oKZbpSdH0ez7zS9Wi-7ANnDPrnqqGjKDunKZjtTNytQklbnQnskCkFx_WOuC7Pv5XEGmofMDbFUqy8AYMZ672064xTzYMXGkoC5yVyedCtnpc8XPQPNAroCyiHc6N4p_4av1kZlkLmshntU8awWPinmQ76GMn2z8053MHqQv_-bO7TbTsreSbwTCL1sMJV4DQyETzETEW2k5UVBhCFoONXvbP_GAkzIHTl35lKjXhpnbIGBXO47sw9lAnBUKZM5tfCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/623a9a2ab6.mp4?token=bEjhaagOXUpZfdIQ-TIMsPzRU9T4CSkPNodRgw9U59HzsDJE7KgMnw1u1tPUpAE95VH6n9nldN5c-rSKGS7oKZbpSdH0ez7zS9Wi-7ANnDPrnqqGjKDunKZjtTNytQklbnQnskCkFx_WOuC7Pv5XEGmofMDbFUqy8AYMZ672064xTzYMXGkoC5yVyedCtnpc8XPQPNAroCyiHc6N4p_4av1kZlkLmshntU8awWPinmQ76GMn2z8053MHqQv_-bO7TbTsreSbwTCL1sMJV4DQyETzETEW2k5UVBhCFoONXvbP_GAkzIHTl35lKjXhpnbIGBXO47sw9lAnBUKZM5tfCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیژن عبدالکریمی، فیلسوف، در برنامه «وضعیت»: اینکه فکر کنیم پس از توافق با ترامپ در مسیر توسعه قرار می‌گیریم، یک توهم است؛ هزینه مقاومت از هزینه سازش و تسلیم کمتر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/662695" target="_blank">📅 20:01 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
