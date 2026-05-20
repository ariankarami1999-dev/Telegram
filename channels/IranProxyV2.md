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
<img src="https://cdn4.telesco.pe/file/bIxvR_Ldr-GnFhlKeRWWWbhtUoHLAHylvHpDJONiCn2uXm6lHfUzY3RhHIzazWUy3rbpDj9f6xhEYVbYotBULEhOqASMc1gbTnOdfvzTrgOXEhYBmalfagDvySPORsu42ZyAvwuQrj2dS0x_uVv3V-vujp5CTlQwZclo1lGnvn8IbmcI991N0gG0GGzjkPE9FtkYS98Le6fkw0MUpZ2nX5wUvkXIZR1M8ikJuRBvhUdZGpXNeSB-Bv2-uGP-RA4787nkVHY7xbg1tH02AGX1Nye346tbeCm-88oHCJVJnzmo5SnaZil6n0d9eT0LR6DVuwGHw61jhKpqcFhzVb4ZDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 38.7K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 03:34:16</div>
<hr>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 189 · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jugvo_YcIRb8bKDeVzM1nxUEPa34JrjmphHrCyzoIroo9p52Zt3a6127inxdxEQmJihS5m6kTDWYDojNzrQd9Lb8cleZEiqxWscKdUctbozmCLjcB9ocNhdgRbzqmiYvoTdYEl_qV_S-9LMmghJj7TZPuHHSS9PBEu0N8jkbMxfKOk4r-RF7TCeJ-2nVOhFfl8vSF4BQM0YXg_4qB3K-3NE0BeABrV3tbNgj5V0pbFD1Bx5Ms9PQbu0BeNdLVe5O2U6pjMkU48E3ovAoSDhhYH7hiINfES-3XAiIyeCxP02hvBpaM_Te29n8DMiqI1V0bv1J3bt2fJFf7ZHa7WohJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=B2dR3uNVzrxkY1rXTNelXXxp_T-K8OnttFkHQcZeebiw1GvxJsBclIN8xp_p9hzO4RqY0CqpFuk6_sLz0XBX5ep8rAo7mYKRMdhGz4IZ16oNDFdHGh3DIh_kAcYchNKnPhyKvQkgekMyjmSLHkhwmpV-BMtwppwWzg8aTG007wq3YXPhpzA2c8KBShmHTvZ_RTaGn0qq5q3Teyk2BR5_q5wEdnOEEH67MQmplz7SyViF3KskOOmhlNBRCdhHzDSfYk5-EfHz91W9LYbqXQGyso_YFkW_yYeFqui-yElGOSTkTxYlsj2DGQPb7Gwm9lrLAXI9QypFo6w95vag45Hl3HgdbjD23gX7oMxQB0NscJF910moB1_Wf-uyy8P35tBAG_MSxL8tkcAEk7ZLaMrbzDlME6zy9OR6Fr4N2K19Mbb4QAjL2BzsUNsp2m2r6H-LKA_mXTZglGISB-8u7r8lEtkv13ejtHTDc5jDr3BleYhQbyNQHgFCa-mkqHicNTRUeGZq6qCQVSE5BMA4RtwyLVItaIHBYmWtoq-CGKWB5wDK7jp8GEQ1aEQjQKZLXwnpt8lQOF2wBPPOsmvpoYh6tuLBua-WsGT9cvfoKxRg0ElE303w52vdFGxQbF8LdAN82FnFxxXN0nl6WVrtcnscXfyQ4thsBdZ4bdsee_1YwOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=B2dR3uNVzrxkY1rXTNelXXxp_T-K8OnttFkHQcZeebiw1GvxJsBclIN8xp_p9hzO4RqY0CqpFuk6_sLz0XBX5ep8rAo7mYKRMdhGz4IZ16oNDFdHGh3DIh_kAcYchNKnPhyKvQkgekMyjmSLHkhwmpV-BMtwppwWzg8aTG007wq3YXPhpzA2c8KBShmHTvZ_RTaGn0qq5q3Teyk2BR5_q5wEdnOEEH67MQmplz7SyViF3KskOOmhlNBRCdhHzDSfYk5-EfHz91W9LYbqXQGyso_YFkW_yYeFqui-yElGOSTkTxYlsj2DGQPb7Gwm9lrLAXI9QypFo6w95vag45Hl3HgdbjD23gX7oMxQB0NscJF910moB1_Wf-uyy8P35tBAG_MSxL8tkcAEk7ZLaMrbzDlME6zy9OR6Fr4N2K19Mbb4QAjL2BzsUNsp2m2r6H-LKA_mXTZglGISB-8u7r8lEtkv13ejtHTDc5jDr3BleYhQbyNQHgFCa-mkqHicNTRUeGZq6qCQVSE5BMA4RtwyLVItaIHBYmWtoq-CGKWB5wDK7jp8GEQ1aEQjQKZLXwnpt8lQOF2wBPPOsmvpoYh6tuLBua-WsGT9cvfoKxRg0ElE303w52vdFGxQbF8LdAN82FnFxxXN0nl6WVrtcnscXfyQ4thsBdZ4bdsee_1YwOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knCkEY3XzxSfKy8BRnxpmItpMRIXrSJchKSPrkjpRbuDaYncx5bJIluSQdif6A2L_AkEraQgRoc9E1QMifEuiZjstl3u7Cpz8jeazNAJx3q1e4WHfx6UGKOCVj1k6KvzxKxX86I9m9so5FXW3mfVR29Ia8aX3uZu350ZudYpKPe44FMnyNWvELfI2cy271oFtNaHFRAPZTRVu5lH0pjd3WArkIOTI-eVFGfMM-GkapE3tuu0phmTyau_jbstbytkyPP2k4x2Irt6RoWXUsBb6rmeCtKQpKwoe6akOpgLkWGdQm2pvCbIJaQb_0cvC0aqojiDmTYFrzBg9bQg7ULJDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIoy-Jk_JSRO-aqUDQqyLf5ZTRoiAWYUv2S12GDV4vptXMPt_pPOz1EvNZ2bqBff1dCdexxvUA2VrfEoYgIJx9XCjhgMuh1ToLYTGlHVSF4b6oUaqo7z5YfvwxZ0aRg6u0eCkNFWNfWm7U4hdy8AGjhuNSEhXU5FGy8aCeNKTt3QcAFutNy8ib5uxpeQjO0T-aiLEBTlTMqv-OdRk57A_4RGp9Rx812Ca24gWvzEdEZYMZ3A4EtRJpIKdIVzmNJoP_ptVWsVMe58C-Zo0i4SjYVrqgIsrmWfF1fowArbTyR0SnANno7qAlrhk3HnUUvHvxkxMT5oBmUBQ99zBVsSnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS9hCTIBfORE5lG0phRhdxxHgRO6QySbrgBfFz70qJaRtGnce1D2D-MaK-636C6MQKll_6uTb-ppTjMihl_iUhjZC64cxtIRwzdlpBrlEhNNL9T6-0UEBkt2qgrpdO5K9IGroWKefdRuqGoY6z38iNwZoKem_4bwwT602p9Zn4t60d37gtrkTL3h4Pb1qPWAGA2wc0OnFbmDA09ZI2zaYuSLzfTuoLI-S_fX1RZcS8-TnlQBvKoyvGdh73PQKpm_xqk9_01cXe86Qe0gR8kLq9zL-faKfq2-7Q_KB7aLPYSTwVc67w630fbXKGcrTuPR_Vk_QP29cgfrghvJWCM-tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=p1K5_6D9_dZulsQIC1Pq8KdYqSA1h3qu1tz_zzAiLJA5Sfb-US62m8pgplssil61Ie08wFV559ON4hp7bbDW4ekdiZ_07_8AEnV_YX85zyxMPGu7AK4-S1T7UFFGheEo5DjIbWISYd2AtWeEtAFECxG-GslUc4LuuKeAkW7q5VgX47ZBylUayYj3GoReoeVb7hodPUJwLqSyAdEIEFz3Wl-v-CtiZAjNgSkKmC7oGytch-a9sEV5UmapqCP6mX5BKcG15UnVVbd7bqVDEUOP46EdXJT5QIBMOHWwsctyQkalz8ZOeaFgxexi77dOUBcbPLRP_BGUP4XJQJv2fjG-Y0YQzEVa0pJ79aoqaSwynCI569kDwv29HqvT2ftxBdd5fi_g95VDLcU0isu7vOrNjl_ePjNdZFkiJA9XmhkqnOFJpEXovSbbP36umk3tDu9QRw323R8JB-UNVEbOf519ecF7kaDPGmPYNT5-333_ARPwnFMHrXNWx02BOvOuKuUX1jNRLufX5ABhZrM9ZtCSPwN6uUoW6Gc8VtZjIcuG7zh0dpjOygFITbCseFhC5bnypkqCmskHS6zgXfiVOUT7fYnzPwsBLlJckNZ27XQ9h0Uu7pVQN0MOZWt8-9E77ruRwCnY7p5zVf7o0XO5iyPqESqYwsuIlXKqtq4-oKLD10I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=p1K5_6D9_dZulsQIC1Pq8KdYqSA1h3qu1tz_zzAiLJA5Sfb-US62m8pgplssil61Ie08wFV559ON4hp7bbDW4ekdiZ_07_8AEnV_YX85zyxMPGu7AK4-S1T7UFFGheEo5DjIbWISYd2AtWeEtAFECxG-GslUc4LuuKeAkW7q5VgX47ZBylUayYj3GoReoeVb7hodPUJwLqSyAdEIEFz3Wl-v-CtiZAjNgSkKmC7oGytch-a9sEV5UmapqCP6mX5BKcG15UnVVbd7bqVDEUOP46EdXJT5QIBMOHWwsctyQkalz8ZOeaFgxexi77dOUBcbPLRP_BGUP4XJQJv2fjG-Y0YQzEVa0pJ79aoqaSwynCI569kDwv29HqvT2ftxBdd5fi_g95VDLcU0isu7vOrNjl_ePjNdZFkiJA9XmhkqnOFJpEXovSbbP36umk3tDu9QRw323R8JB-UNVEbOf519ecF7kaDPGmPYNT5-333_ARPwnFMHrXNWx02BOvOuKuUX1jNRLufX5ABhZrM9ZtCSPwN6uUoW6Gc8VtZjIcuG7zh0dpjOygFITbCseFhC5bnypkqCmskHS6zgXfiVOUT7fYnzPwsBLlJckNZ27XQ9h0Uu7pVQN0MOZWt8-9E77ruRwCnY7p5zVf7o0XO5iyPqESqYwsuIlXKqtq4-oKLD10I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=HwVkJrMjs2qPV98jd_6fo4uebuQDFnrBQuTPFovEnkUVz2FQtrccQWahZwj-7eo0B-_dtKYLrSATK8ePIhbWEdMXBz6Qiv-z0wnACZ9HRljvLxmlpW5kQwzrFF97zEuTvgtjMie9bZVN-ANENbG4YnRRpqpffSPVShD-mCW6G44pyt5_LDeq6hbx5PO1M7IY7EgzwgIJ1eZb5vN82c2h9Gtl4Xzn4afd_3UaUa_Bwqf5yDMaFyvAc0utHJ77pxyFwHEB_Al7AMvILFn7V0PdErC0TAXd0y24o8FWsZimTY64ebTTa_kq5TldK-KqqG44bGuiorR68ar9JCyjy3aWzhxo6Q_vKRg5VfrgjCvy7L-37bc4B4MbNqI__MGVQto9vZN_qfX3j4WsnD1PjQ5HPWTcwM5i8TZbvY-A9H62-MHAEuCFdfvNIEfEtkjWsvdCLebKgIdEDb60wbKuIjsOjBdPxp9PrsLAdxzf1MHuFfnmc0GBpmjdFN5ByY6C3u5trsYx0LrN1oFR5JRge9RstwyGRTUGfaap4yneVw7e2f837t94Ov9kVw36d5SkEpse9R2IFnTds_l7uWPi0UZZA5wc_bxpeoKGIEgmRa_qykrkFE7ze_gBlWLpSCe-yLqe2T9QUnhkYQSz96ql7-4dhnh8dM19LkLeiZ5Oq_2eg6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=HwVkJrMjs2qPV98jd_6fo4uebuQDFnrBQuTPFovEnkUVz2FQtrccQWahZwj-7eo0B-_dtKYLrSATK8ePIhbWEdMXBz6Qiv-z0wnACZ9HRljvLxmlpW5kQwzrFF97zEuTvgtjMie9bZVN-ANENbG4YnRRpqpffSPVShD-mCW6G44pyt5_LDeq6hbx5PO1M7IY7EgzwgIJ1eZb5vN82c2h9Gtl4Xzn4afd_3UaUa_Bwqf5yDMaFyvAc0utHJ77pxyFwHEB_Al7AMvILFn7V0PdErC0TAXd0y24o8FWsZimTY64ebTTa_kq5TldK-KqqG44bGuiorR68ar9JCyjy3aWzhxo6Q_vKRg5VfrgjCvy7L-37bc4B4MbNqI__MGVQto9vZN_qfX3j4WsnD1PjQ5HPWTcwM5i8TZbvY-A9H62-MHAEuCFdfvNIEfEtkjWsvdCLebKgIdEDb60wbKuIjsOjBdPxp9PrsLAdxzf1MHuFfnmc0GBpmjdFN5ByY6C3u5trsYx0LrN1oFR5JRge9RstwyGRTUGfaap4yneVw7e2f837t94Ov9kVw36d5SkEpse9R2IFnTds_l7uWPi0UZZA5wc_bxpeoKGIEgmRa_qykrkFE7ze_gBlWLpSCe-yLqe2T9QUnhkYQSz96ql7-4dhnh8dM19LkLeiZ5Oq_2eg6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHnkJlNA6SlqNKSIzPwMO62ch2-vn78L0ghdm58d3vjFabXcoHFENFGfgNZk9iIaLq9aFXpEiD-ET7BegodHRK4vhv2jKP-luJcPq_T5dNnDG2tty3hxQp9F6hzzSFta-qTzbvaKB0WubzdLBhbT2C5kBkVhtjzeNtFXEW0hf1mmI14AlDGGcN4mONWGf6vMJeRla9jEnW9TH9aRTZP3LEQcEuRLRetOE5hSe6yJTlUmhCFZ6Di8n-gtkvI5UkxBBp4EC-zNA5-kH8HzPpqSLOMjPp3EPlwW5wz3QQkZTk1FJo9Sg9tkqmklTNigQgTFk-na7ccmVQJjDv5WeoOF8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=FZJlwzITC6EZ531GEh6iX_XsmocDeVgVOrb41sGe0ZY8ao0Svalp2SdxwYu7TYa-YYoM4EgCD7O_p3GDcnNZbY8VmE1tQFvjqFt0TMnXdjcSXHscXjGJ74VGEUtoG73sQLUXK5sggYwWpKm_vAb1uG8HNJE8K0OkjlG5wJA8srYMJK6LII7nkWBlv_MtkA7_9YuxCuj9yWBB_sxOhTxWIEkNjOoEn8tbq42P3F3xKbfhs8rd5siSFYSBufyhzPPm3ODWg9m104R5gP_0QCYsisG7w9oUrSH4wdmOB1hCrv2KIQWH51a3DWJjTkm8XW-ecTm7Ov1_5HgA1QexphEAd7Xq-1uXMtURbzn50__fWIkPDqUPl8laO47rnmnPF8I3n_nVycu5F0Sk6_QbHXds2SoC5DhlOzhrhuXpvwF4XN-6_uZwMNCeVExK73TJqMu3rW7cB7cYRZORnt_3MdETCn_rmTJnDqTWlH_qmWDDSU2LQO03pom832OuTU6tePFqKbOAGocGN9A7hgjqL30VMOt1GvLiUrOk779cnvu-Gq5ByMDV-fSOiNBPk4N8me-evA1ihpdIpEMvMSmSNrCp77oEgFfaQabagdCKhNrgqphN6Uy62fBzmiB6WtrtUXW5NFAQh9EmwWHeRINdQ1ETwlQE8Qk4AO3tsbVNOwR9A7M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=FZJlwzITC6EZ531GEh6iX_XsmocDeVgVOrb41sGe0ZY8ao0Svalp2SdxwYu7TYa-YYoM4EgCD7O_p3GDcnNZbY8VmE1tQFvjqFt0TMnXdjcSXHscXjGJ74VGEUtoG73sQLUXK5sggYwWpKm_vAb1uG8HNJE8K0OkjlG5wJA8srYMJK6LII7nkWBlv_MtkA7_9YuxCuj9yWBB_sxOhTxWIEkNjOoEn8tbq42P3F3xKbfhs8rd5siSFYSBufyhzPPm3ODWg9m104R5gP_0QCYsisG7w9oUrSH4wdmOB1hCrv2KIQWH51a3DWJjTkm8XW-ecTm7Ov1_5HgA1QexphEAd7Xq-1uXMtURbzn50__fWIkPDqUPl8laO47rnmnPF8I3n_nVycu5F0Sk6_QbHXds2SoC5DhlOzhrhuXpvwF4XN-6_uZwMNCeVExK73TJqMu3rW7cB7cYRZORnt_3MdETCn_rmTJnDqTWlH_qmWDDSU2LQO03pom832OuTU6tePFqKbOAGocGN9A7hgjqL30VMOt1GvLiUrOk779cnvu-Gq5ByMDV-fSOiNBPk4N8me-evA1ihpdIpEMvMSmSNrCp77oEgFfaQabagdCKhNrgqphN6Uy62fBzmiB6WtrtUXW5NFAQh9EmwWHeRINdQ1ETwlQE8Qk4AO3tsbVNOwR9A7M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlcGkE0sKr8QNHeo-eP0j-EIrfR234WaJXM73js5zlP9Uj2ENJMUMdU4bOUyoI75gdX-11fT3nUyV0Pj4wTmzl4J7t4yDCOVJcZJqe0yRs51jvmS5Mni57JHeAO_fGi4Dok_mKrjLPU1w3KFGq4L7THzkd88yfWUi2oW1KoDjOFqgsGilyzED2VKUpifg3-V5uwZilrxlFe02kKX9MClPZRwcp_h7MtDZkER76cHtvax63TWRtZrQRS74osQg6FS-CE0OJMPX0nCIQUeZu7EueLst8tHD6o60VqfojgwsQ-0MK1ggQizl1okt7hePhUlG5tZkixa2h7g0SU9THOLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cowUeMi2tDuol6ATy20bVVUsj1oj09ijcEiFBQA6VywTrxwvRWRI9ip0HfkpkJwS7EQe5nc5L9ZJNoMfKhZithtFX3yoTlNJV9MTwdgpMlSbhvn-cUsukyX6TbRXxHBzGaSin3-1Gl8JwuHQWlTbNcCm_f3anoFSuooDnJYozvLc19yLrrup7bcdT8Tt3uTI17Nn7NH6uWajkuKHqu34qUbPK-Vk7LUDDSk1Nezd-fo4pg-eLTV6Jpv_LLodStyM6Kb-dFHbSwTOm67Ywi8cXEsGyKBRUGM-bLZ5HFocdSqD4p9RVl36Ql8MCHnPos-hvxZ2IFa6_uECtTqrhPJbiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=180T
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
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=lOjEO-Jf2F_EALaKTPN-wkDqmj65jEG8rOFrI5yYcuHI9YX4HAZs_20fu978IM__Bj54fiLIgWIBgi_oE15vCWPjtr8pRXnKleoEr9ih_ZzpzMYIgKUDRyP4IFgg16xhwx_oN7nJoXYMEEcISdqc1pZGjRdF6KY3lueBoEROLGpXiNzENDkJcj-4NgoZNO1UdsCbJbVTUIs016ERMuGEHu2LIhPofxnFbGDAxq0MoShj2KZE0MKFJuRlOpiU4MlbDFoSo8gJnbT9gi19_e0bfvt3K_mwbZOaVKLnwMKsjFxb2XXJTQa5SGKGY9bQeMZeXl0FWUCY27y5NC1reESwMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=lOjEO-Jf2F_EALaKTPN-wkDqmj65jEG8rOFrI5yYcuHI9YX4HAZs_20fu978IM__Bj54fiLIgWIBgi_oE15vCWPjtr8pRXnKleoEr9ih_ZzpzMYIgKUDRyP4IFgg16xhwx_oN7nJoXYMEEcISdqc1pZGjRdF6KY3lueBoEROLGpXiNzENDkJcj-4NgoZNO1UdsCbJbVTUIs016ERMuGEHu2LIhPofxnFbGDAxq0MoShj2KZE0MKFJuRlOpiU4MlbDFoSo8gJnbT9gi19_e0bfvt3K_mwbZOaVKLnwMKsjFxb2XXJTQa5SGKGY9bQeMZeXl0FWUCY27y5NC1reESwMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1Vy1dRuNwUTAFkG-MjwWIsb9iINagsOhYigHuRpg6LYoyvWwVyq3Zi5eTYYGbKzIBX0GykgfpzC6-5Gt8H1yqx0BAbAkw4pli8yeVbQWhKOUYykXToB6Xhe_Kwikw84WIKOuavklcE2E_8hGBuJKPqNatY4Gc0cGso5iSBPpwxCAfoRnFM0iwsxnrmKrxiaFGzvWtZuvrvmTdnIkRzmi8J3uOy3ErgCIHhALrVXxOW9SsA3NK5kLocLR1Q3T7ru6yV-TI_WsvR7r45P49kDeJ4qYfXnI0fcduXdfPsJ5_qevDIhNxenxSmW6vTZgqaDfJPtHPH3hsqjk45mNDmavg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=180T
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
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWQzeAgmkgHKtO409nnAQWatWBtvX6H51BDcnC7MjgOasVidyjAOQFwty6uPbcDvw0QAoWuE_XVO66Z3MrKqp_c93AJVIJWVAMSAHamz3HtS5X-1lkMkUDMpdHyb-4Hz9jDWA2j3Cjsiy-EykcNOaDeYWOQ4Av3zCbIQmuX7D38oA-fCPxqS8DpXmHSMzlzxnyw6fUbpvzPpIbXIKSHlm93ecXHHVl8CWOdZDpjcaWumY0AznjQIOhlITsMuyD8NsSYZZsrhs0GPD6rqwsFsjfy61UFYb2V7RDXR41_OZ1cPvp6f7Ppjd44qHDT8T9bKWcYtqyVrUSmsxn0PXUBvrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏چالش دو گزینه ای با موضوع  اطلاعات عمومی
📚️
‏
🥇
🥷
Sara: ‏(۱۶۵
❣
)  ‏
⚪
❌
⚪
⚪
✅
✅
❌
⚪
✅
✅
✅
✅
✅
✅
✅
❌
✅
✅
✅
⚪
‏
🥈
🥷
Freya: ‏(۱۳۸
❣
)  ‏
⚪
⚪
✅
❌
✅
⚪
✅
⚪
⚪
✅
✅
✅
✅
✅
❌
✅
✅
❌
❌
⚪
‏
🥉
🥷
hossein: ‏(۱۳۶
❣
)  ‏
⚪
❌
✅
✅
❌
✅
⚪
✅
⚪
✅
✅
✅
✅
✅
⚪
✅
✅
✅
⚪
❌
‏۴ )
🥷
Dystychiphobia: ‏(۱۳۴
❣
)  ‏
✅
❌
❌
✅
✅
❌
✅
✅
❌
✅
✅
❌
❌
✅
❌
❌
✅
✅
❌
✅
‏۵ )
🥷
- Amin -: ‏(۱۲۹
❣
)  ‏
✅
…</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏چالش دو گزینه ای با موضوع  اطلاعات عمومی
📚️
‏
🥇
🥷
Sara: ‏(۱۶۵
❣
)
‏
⚪
❌
⚪
⚪
✅
✅
❌
⚪
✅
✅
✅
✅
✅
✅
✅
❌
✅
✅
✅
⚪
‏
🥈
🥷
Freya: ‏(۱۳۸
❣
)
‏
⚪
⚪
✅
❌
✅
⚪
✅
⚪
⚪
✅
✅
✅
✅
✅
❌
✅
✅
❌
❌
⚪
‏
🥉
🥷
hossein: ‏(۱۳۶
❣
)
‏
⚪
❌
✅
✅
❌
✅
⚪
✅
⚪
✅
✅
✅
✅
✅
⚪
✅
✅
✅
⚪
❌
‏۴ )
🥷
Dystychiphobia: ‏(۱۳۴
❣
)
‏
✅
❌
❌
✅
✅
❌
✅
✅
❌
✅
✅
❌
❌
✅
❌
❌
✅
✅
❌
✅
‏۵ )
🥷
- Amin -: ‏(۱۲۹
❣
)
‏
✅
✅
❌
❌
✅
✅
❌
❌
❌
✅
❌
✅
❌
✅
❌
❌
❌
✅
✅
✅
‏۶ )
🥷
𝐑𝐚𝐝𝐢𝐧.𝐳𝟐𝟎𝟎𝟕: ‏(۱۲۳
❣
)
‏
✅
❌
✅
❌
❌
⚪
✅
✅
❌
❌
❌
✅
✅
✅
✅
✅
❌
⚪
✅
⚪
‏۷ )
🥷
Matin: ‏(۱۱۸
❣
)
‏
⚪
❌
⚪
✅
⚪
✅
⚪
✅
❌
✅
✅
✅
✅
✅
✅
❌
✅
❌
❌
❌
‏۸ )
🥷
𝘿 𝙀 𝙑 𝙄 𝙇: ‏(۱۱۵
❣
)
‏
⚪
❌
❌
❌
❌
❌
❌
✅
❌
✅
✅
✅
✅
❌
✅
✅
✅
⚪
✅
❌
‏۹ )
🥷
Paranoid: ‏(۱۰۸
❣
)
‏
✅
✅
✅
⚪
✅
⚪
❌
❌
❌
✅
❌
⚪
✅
❌
✅
✅
⚪
⚪
✅
⚪
‏۱۰ )
🥷
Robert: ‏(۱۰۲
❣
)
‏
⚪
⚪
✅
✅
⚪
✅
✅
⚪
❌
⚪
❌
❌
❌
❌
✅
✅
⚪
✅
❌
✅
‏۱۱ )
🥷
♧: ‏(۹۹
❣
)
‏
⚪
⚪
❌
✅
❌
⚪
❌
✅
✅
✅
❌
⚪
✅
✅
❌
❌
❌
❌
❌
✅
‏۱۲ )
🥷
Zaker: ‏(۹۷
❣
)
‏
✅
✅
✅
❌
⚪
✅
⚪
✅
⚪
✅
✅
❌
⚪
✅
⚪
❌
⚪
✅
⚪
❌
‏۱۳ )
🥷
✗ᏦℕiႺℍᎢ✗: ‏(۹۵
❣
)
‏
⚪
❌
✅
❌
⚪
✅
❌
❌
⚪
✅
❌
✅
✅
✅
✅
✅
❌
❌
❌
❌
‏۱۴ )
🥷
❥sheyda☙: ‏(۹۴
❣
)
‏
✅
⚪
❌
⚪
❌
⚪
❌
✅
⚪
⚪
✅
✅
⚪
✅
❌
✅
⚪
✅
⚪
✅
‏۱۵ )
🥷
Ахмед: ‏(۹۰
❣
)
‏
⚪
✅
❌
⚪
❌
✅
⚪
✅
❌
⚪
⚪
⚪
❌
✅
✅
✅
⚪
✅
✅
⚪
‏۱۶ )
🥷
Ali Moheb: ‏(۸۹
❣
)
‏
⚪
⚪
❌
✅
✅
❌
⚪
❌
❌
✅
✅
❌
❌
❌
❌
✅
✅
✅
⚪
❌
‏۱۷ )
🥷
Vista: ‏(۸۴
❣
)
‏
⚪
⚪
⚪
✅
⚪
⚪
✅
❌
⚪
❌
❌
✅
✅
❌
⚪
✅
⚪
✅
⚪
⚪
‏۱۸ )
🥷
ㅤ: ‏(۷۵
❣
)
‏
✅
⚪
✅
❌
❌
✅
❌
⚪
❌
⚪
✅
❌
⚪
❌
❌
❌
✅
❌
✅
⚪
‏۱۹ )
🥷
Mohammad: ‏(۷۴
❣
)
‏
⚪
⚪
⚪
❌
✅
⚪
✅
✅
⚪
✅
⚪
✅
⚪
✅
⚪
⚪
❌
⚪
✅
⚪
‏۲۰ )
🥷
✨
𝒫𝒶𝓇𝓂𝒾𝓈
✨
: ‏(۷۲
❣
)
‏
⚪
⚪
⚪
❌
⚪
✅
⚪
❌
❌
❌
⚪
❌
✅
⚪
✅
✅
⚪
✅
❌
⚪
‏
👥
و ۶۳ بازیکن دیگر با امتیاز (
❣
) کمتر از ۷۲
❤
خسته نباشید
❤
‏</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvAXUleiaaE9uV4-NI42Cu6jTvW0r-u40lOC7QwHoFnSrgBv6A_efqpk9PJz0OfY6HFHtQLp_vMvaIzm7GpGJ_ef87g202pogp4pKLvSlWZDoI-ORSbyw12xcNr0zdJP9YgJWzjsHnU2ztnkpEDqHQlQXhYoGS9Dft63W44D5a78JBQpL5rKSbR-7X_Xao_GZtXIZ6TtV9YfiY2r8-8cup-o-k7WOkdF5a7UIsVHS_5ed9P_P9wkaGA4Ak9G6oMG-LlBoXu7pehjAi05RV64hqbxEvirerZ2u0pkB2zMg14Dv2vrhGJ3_Pews3nxlED0aGNgiGwGeZKf-oMyUpxdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=S7KGXPFjI5hugaQJ5qGBzEclPM1DJdmuooa03tRXapNlCgnl8YtnVAC5UyS6fYxcOxoX5lkQzXRKHRqsm37NQA3DQooj68hO0gNOhb1ngnsOCNRyePU_V_zex1RJMUbGTli8f_dYTq4vItEeX9cfgREMTyDK6DAXy6i9T3amowx5gFRm4gu0Npv-ZYLHiLNGQX0yWBpy5X-PU8dmVsl_Ldh7ULvBxenS71Xb0vfo7Q5PErqpnk_Kjw9OVObLFDGjeRLbP6c2h0ML9DqcJrMfUenLIBxSizm6QNKq9Y7gAguu5wJ43tGr_7jBwdyL3YQxayeH2OA5bUwXQDycnO6W-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=S7KGXPFjI5hugaQJ5qGBzEclPM1DJdmuooa03tRXapNlCgnl8YtnVAC5UyS6fYxcOxoX5lkQzXRKHRqsm37NQA3DQooj68hO0gNOhb1ngnsOCNRyePU_V_zex1RJMUbGTli8f_dYTq4vItEeX9cfgREMTyDK6DAXy6i9T3amowx5gFRm4gu0Npv-ZYLHiLNGQX0yWBpy5X-PU8dmVsl_Ldh7ULvBxenS71Xb0vfo7Q5PErqpnk_Kjw9OVObLFDGjeRLbP6c2h0ML9DqcJrMfUenLIBxSizm6QNKq9Y7gAguu5wJ43tGr_7jBwdyL3YQxayeH2OA5bUwXQDycnO6W-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=E7MFTRekRCv_t-XNOV35TSi1MD0GTEfjf4HN5DN5gSiO5IXZ_YymL-2yoq_NgzWtu3owJS5CkxtFKtWnNN6-T2sg8aNgNJXN4fK6yyHup4th3meMKmgkR0j58-Zdfxwdebo281qllX_ZIGAvNBQMslNrCjGetXwVap1YrPE4xTUkpuC12BSeL8zuliX1Zlb2Pkw4P8GOHZB-u4rG7FZ8hLRSnxpgJ_HguDTm3PwLYqD-VRwP7WIzxir-1wkxrSvS3TuAXj4SI5tXXGqBRIa-pCxaxhMd40YNQtlrF90d2Uz85ytpaY5343ON7pDHHNBobla23xY33a_Hm4Rz75qDDUnduWDe0QjIUJ5B-WpvFmGm39eb5Wesi5znIAlKRkVZvZzETF5nK0A0iOlNzHCsgv4PZgVVDjj7-oc_jYp7r3FxiVD0uQq0WhsEmBuZEBdACiX-UOKJ8rT3XL8y9TIf2d8i4HJf2sW9VK9hu46CjpwGx58JSKKGTb2KftdJwkpwqiedUgCeQOwSZBrKFaRXJ641M70PDZYZes5ddDGCs0G6FdBEf8JLBZ06h7aWEe3tjgqk4PKZmSxhqmavGKU3kbFxe7W9SHREJonODs8_QuIr5Lqk0rPLJJvyuA3mG9qb5uqXvGDhz3YCXdIue6aolLsyykDgri5ngyZ4EeG_4NU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=E7MFTRekRCv_t-XNOV35TSi1MD0GTEfjf4HN5DN5gSiO5IXZ_YymL-2yoq_NgzWtu3owJS5CkxtFKtWnNN6-T2sg8aNgNJXN4fK6yyHup4th3meMKmgkR0j58-Zdfxwdebo281qllX_ZIGAvNBQMslNrCjGetXwVap1YrPE4xTUkpuC12BSeL8zuliX1Zlb2Pkw4P8GOHZB-u4rG7FZ8hLRSnxpgJ_HguDTm3PwLYqD-VRwP7WIzxir-1wkxrSvS3TuAXj4SI5tXXGqBRIa-pCxaxhMd40YNQtlrF90d2Uz85ytpaY5343ON7pDHHNBobla23xY33a_Hm4Rz75qDDUnduWDe0QjIUJ5B-WpvFmGm39eb5Wesi5znIAlKRkVZvZzETF5nK0A0iOlNzHCsgv4PZgVVDjj7-oc_jYp7r3FxiVD0uQq0WhsEmBuZEBdACiX-UOKJ8rT3XL8y9TIf2d8i4HJf2sW9VK9hu46CjpwGx58JSKKGTb2KftdJwkpwqiedUgCeQOwSZBrKFaRXJ641M70PDZYZes5ddDGCs0G6FdBEf8JLBZ06h7aWEe3tjgqk4PKZmSxhqmavGKU3kbFxe7W9SHREJonODs8_QuIr5Lqk0rPLJJvyuA3mG9qb5uqXvGDhz3YCXdIue6aolLsyykDgri5ngyZ4EeG_4NU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XE9LdUfz_riAu0UJ6Kr7heawM57sXBmW1L_iBK3tFDapAQrCGpz6EF5pTazTCFVgvwHrnadxkWlOSQ7S6mvjItTLmGEh144nMHo22B1xzjBLR3duv_jFICC_6PQcalxUKXNssE8RO_4_9_FG5xri4FTUc9hRejyJdZj1FOk0o1sm0e9sU351f7BPtrOibINBOGDqBkHyZYgE1_v4p8uU--nEDbjECVGtk5IWqd4_hZkMt0296CWOpwPCYMYURMo85W0mt1h0Je7B1qHzmG_HBtr2ovXSLZxiu1iCdRYVnCKiGey7rwk7vqUyjGqdSb1FfJuIYYs372KY95SuzsttVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLuTmbrKbkpg5h7HvA8Pb9xUt353FXLHk-fJFJRUn_OzPrqrmgp9H2ewlBarQRP37d4JVKW72EjXZ57TZ-rr0tDjTLSsxsfw9F1BQvEKNCgYbe6BqAnNYZuSRawbxOJaDwM9EinIk1Dck07BIfARzl-4HqCgnrJzuli9wOG-UnOyG_gUUirU_YZDmIL-2BWSeGiRIJ8iETztGwb7EPczPkDeVU7xaJIIv7matvBL01qKIjasnfHryO_O23PRHXnujCDPyuWUm5p4bJ3tIBJKAR7guS8prj78jH9sJPAavMzFJ51wiYRFMDhn4-sxcF64JUvPPsa4TZ8Mayt6ex_Myg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
کد تخفیف حذف شد برای راحتی قیمت هارو آوردم پایین راحتر بتونید خرید بزنید
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fpRuV0xZwBZb4ik89fkJJS67k8kz_RXoRJ3zDdrb22_fqlPdCnNMLa4BOoUZ4nCxqoWF4QppLCRVZ8Ta27PYxD2yfSW5gqHF04m3H7RVKa4x2ugP-Md1XGQWkgjYO6DXRDzjJa4gZIiurxKYZWWM8YpwsctZzB2llxm-pY8PzXOVj30_Ir4yG30t-81IKkPTdH9RJicJ9aXVEXQSYSZQchWMcqc5c-3XA1oeHK0B8re5t-KZybN9txZpIFBU4CcOKd2yD3v5jCzQMwvIk08W4Hsb8ioGxronSptlYvs17Gy0O2zxL49BLT3xXOvpzJc75WH7rtGdQqR8fW5A5Jt9Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=iGL5gUgZWvnXTfbuCl76JRugGsFBgfXh_mExwESaGVC3lskSup-8hPLF425e_wxuc9qrX2yvda_dsUnIaABTzXBMLVexZpc7_RqGIosQVew4zjr2jZnA4zeMX6der_pKfyLI6uUcgPrY0dRSz1C2V5SxuAq5_I9rdjJDcp8q7rJIHPZIVZRccNPljWq1Uia-ZtVLKWafjBeru9YQYk0DxX7iKERq-Do5_Tbuug-eReJMdy8c0q3lUQ3eLzMdZLlUlG4YfJXVT0yFXBU2FaWdjXqoccKLherMhIB-qypk9hYSBEEh97UbZeN5vL3-xYUMB7jdU4MIEB20qIEK15-HdWVkaRQ7PQpq-Edhjz2xw0CWkDznSjBKizHiEF-gYq4i_6spHhYjKNRJO_E3w4NOlg-vG-aq-MFKBcVuB1W223D4cxlN9a8dH8cHsvmlb18tRiN48f_Jxwu6p10l7hPoQnqgHdTn68QIsvhSUoIVH7g6im66fNZxK1A0dj1psHITAq8rLL3qiCi4jGZhlkT3Wj1Q2A7pGOWpGGVos-Uoii-gxCqpdBCU48jJyAPu1goHKAAmmEyYykhxihblNgt_KFNMQ_kmwpnoIYQ9pflrY17nw66MeaQNRRSlmWEhCem_odnv8RW92Y6Pl8AOc7CSEGs13pj2849b-WErn-IJglM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=iGL5gUgZWvnXTfbuCl76JRugGsFBgfXh_mExwESaGVC3lskSup-8hPLF425e_wxuc9qrX2yvda_dsUnIaABTzXBMLVexZpc7_RqGIosQVew4zjr2jZnA4zeMX6der_pKfyLI6uUcgPrY0dRSz1C2V5SxuAq5_I9rdjJDcp8q7rJIHPZIVZRccNPljWq1Uia-ZtVLKWafjBeru9YQYk0DxX7iKERq-Do5_Tbuug-eReJMdy8c0q3lUQ3eLzMdZLlUlG4YfJXVT0yFXBU2FaWdjXqoccKLherMhIB-qypk9hYSBEEh97UbZeN5vL3-xYUMB7jdU4MIEB20qIEK15-HdWVkaRQ7PQpq-Edhjz2xw0CWkDznSjBKizHiEF-gYq4i_6spHhYjKNRJO_E3w4NOlg-vG-aq-MFKBcVuB1W223D4cxlN9a8dH8cHsvmlb18tRiN48f_Jxwu6p10l7hPoQnqgHdTn68QIsvhSUoIVH7g6im66fNZxK1A0dj1psHITAq8rLL3qiCi4jGZhlkT3Wj1Q2A7pGOWpGGVos-Uoii-gxCqpdBCU48jJyAPu1goHKAAmmEyYykhxihblNgt_KFNMQ_kmwpnoIYQ9pflrY17nw66MeaQNRRSlmWEhCem_odnv8RW92Y6Pl8AOc7CSEGs13pj2849b-WErn-IJglM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBmLxz1iNTg8CsbyeLkE1Jl_gd4qRok_XlgzE1P2Vb8B0NjW8ziMZVCt7pcCulY_ahv1Wh6dq_Q6xRM7AG9wy2CirLARCQEt5H0MSnh8lSfJ_Fs7nNSMFk0JQiAN1cX_LV_Gp0u3R3JqHTGqwqAKMWYwh1TmKJf4jlL5RQfadWzt2Au0gAfBSYoJSJxaU9pGnmh3fEDHoDMXFms1QOISHDdoITtGFSo8SdcW3aNtHmfGRJsrQu2TQSGB5CKZ94UILrjSaovTxyTno3VarB9KOm0yPI05265MQTd3ZBoBimfGR4seuWC6I-wsfd9wyENauTHGb1LtXZtx-z0Sk4U4lLT4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBmLxz1iNTg8CsbyeLkE1Jl_gd4qRok_XlgzE1P2Vb8B0NjW8ziMZVCt7pcCulY_ahv1Wh6dq_Q6xRM7AG9wy2CirLARCQEt5H0MSnh8lSfJ_Fs7nNSMFk0JQiAN1cX_LV_Gp0u3R3JqHTGqwqAKMWYwh1TmKJf4jlL5RQfadWzt2Au0gAfBSYoJSJxaU9pGnmh3fEDHoDMXFms1QOISHDdoITtGFSo8SdcW3aNtHmfGRJsrQu2TQSGB5CKZ94UILrjSaovTxyTno3VarB9KOm0yPI05265MQTd3ZBoBimfGR4seuWC6I-wsfd9wyENauTHGb1LtXZtx-z0Sk4U4lLT4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
وضعیت سرعت سرورها
@RUSSIAPROXYY
🇷🇺
📌
آیدی ربات جهت ثبت سفارش
👇🏻
✉
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AKxorROtgf8gJnH6cXMO9JmAG0jBy0NdO0DKyuwRlQB2tiALJ2NZ3fr7bNSUKvaZXL30PyKI1ZaD49iVghrgGyUM8vLujfbyTIlGdz5osxpawwr8Y6K5DpGBTj0BQQt-EDOVWAqy10J9cwnXKaQ0LghXftqJ-NZGLwKjZCvqPwLZnFkhMXy3qqWvlP7Qi2N21p146ap2xZVm_nxmPp3j27n92pZMDhYGVX9YBUe3ghH0HhSJR5nniqYJPfTS1rj8bMbajrU0MQd9Gr4M40aArCu6nGxnR6kwlZ7z30NUUs7sTXuQ0i5a7wKpPidokY7iUT8MAEWwtonNg5nEc2X-zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pbwuadbi9omXXWEsMto1VqI8xkRdjsM79ModG93X3-bW0mUrCozyPQCdIaqOVRPV6tklWCLOmIq9AO5AnkiNEHb7RFUPXXl1pgo2zf95SrCPqKzLW5sD0fy10LnIlqi1H13hL33Q-GfSSLsiBcHdF7ywoAvoI-7uUX1o6IAa9jVd8l6fl2rMA0qIvZ_4Wq5JgIWoUkGFt8yQofxcwqeTLs2FRY8P34RobMEF6vpELToe3cEoY1hGuv2OJhOyoxP5MHvyxXhlk9-QsTThrlh7maeLQ-kxPsy5X6-fsU9PhqfMYZDxPxyg0JwqFuL5xK6bSP7uu4SF_GIktWk7VMzA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=JZw3lMukpXqo1UIYQAUx2qhGRzVzr-ZQJzBMpikjX0vmHD0eODMkEPN_595m1G_2uODVzluKbBUadbvA4hgJxF_eIzVYi3NssLx0HfHWzeBtvB33hgEmLz5z1cm7Ajx0uTLzw1uVc8KNggvT5vtIAyEC79zUdqdZerZ90frqmnkbnHaVbcwWsJCsLD0AXGyyVY2CaTZcE5NAOE747lOuzInNggX6ED7hNKgeRlGEpIvG_WO15zcglRWTCeObEG_zBZrN9B2700cbefNe3IHt0WZCIoMiOgkmim5KR-M3qVVeBc_zopiaATYJ4FF8p5HR3wy0_wpuWtNfYlV1Sej-Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=JZw3lMukpXqo1UIYQAUx2qhGRzVzr-ZQJzBMpikjX0vmHD0eODMkEPN_595m1G_2uODVzluKbBUadbvA4hgJxF_eIzVYi3NssLx0HfHWzeBtvB33hgEmLz5z1cm7Ajx0uTLzw1uVc8KNggvT5vtIAyEC79zUdqdZerZ90frqmnkbnHaVbcwWsJCsLD0AXGyyVY2CaTZcE5NAOE747lOuzInNggX6ED7hNKgeRlGEpIvG_WO15zcglRWTCeObEG_zBZrN9B2700cbefNe3IHt0WZCIoMiOgkmim5KR-M3qVVeBc_zopiaATYJ4FF8p5HR3wy0_wpuWtNfYlV1Sej-Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینک از وضعیت سرعت کانفیگ ها که بخاین تبدیل کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MTfNPCjhtacQsVQ9SPWNY4wELH04MIQoEuqrb2gzeiHWCaD0QlvR4YSyv2C1eH_CVh0N6SzcxVGad9vGN_yAlFNoDzlyRQMgyrVcE300oJgEbeyUttznsDRqnTTtEmQrtTUxHlWDdAFSx4Ur8bxhdtT2Js0x_gtnjPvQzbfoXxik8Q08uPUR1PhsxAOQyY1dxh1syf7VcnfAXQgXntRWdScYBrPQIe_qUCF4Mhxys7UEB5Cw8AEty8c9aLh32jW0EtPdaRVuuAjOLc4DE4-269fS52eCcCF-q5KbkyuSxn5vx0wu2kwShABWgfKZrn8QKHJrKfPw9hZLvG9ERSacEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dEkzxQMen3KZwk0Cpf0HnCciGFByC9G3nHvlUnrhKsAuMQQlq_4Zur0AK5D_WZEXaqOabYokxKMdKwn-hy7mHzGQbIMp4wLLOLX06R-MCD6NAflkHvTFJrqfeZyQCIUqFiNmGq7GbrtNxk14ZVmBCEETrSPNIMre1q1rMlTQ6kfq-Pqp5fUKnEGZW9qhyZPfZpru3IwIeJ3XbM_mv6XbEp675gkr7li01ub8G02a1KH7ZsZ8nf1QWxU6QhaJeY3N4EqAIExkJ3ME_yxYeJjyh49gAsVP0TlfSQwSiQVbzj3drt_Hz9JTDhxC81tekNB4J9cppQZ1wXzJaC7x5O22hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FG7VZQCzZH7BtvmRaVelxIA-3kOjMD_pzvXfpLnK0_7OKydjDQFPZNe6Tmv6UoGiKarpR3F38APqBffaldIr-RMRaB9VresknE1roiDHO3M4Fg3LqPcPX2JraBSc15RWXNTfZJMPsCj7TMGR9B4ev0mVzLxM-E04fxts4gIc4HU5eIxG0A0217D80c1AZIwCj89Z_vYF-54K0fll-oV0bgtE28TBRfGuxyE4Uw9s2KifsvHfYqyqBXveY_G3E5kVnyXHOByOfOPH-xENcSNImZS0VRAXbRjREUIW0omy3MdAv2bm89vQhaPof2MLro8sjRFh6tfACkOR26RBiyIIfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8333">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قیمت‌ «سیمکارت سفید» و «اینترنت پرو» در بازار سیاه چقدر است؟
🔹
اینترنت پرو و دسترسی بدون فیلتر از طریق کانال‌های غیررسمی و بازار سیاه فروخته می‌شود.
🔹
قیمت ۵۰ گیگ اینترنت پرو در بازار سیاه تا حدود ۱۲ میلیون تومان اعلام شده است.
🔹
سیمکارت‌های سفید با وعده اینترنت بدون فیلتر با قیمت‌هایی بین ۴۴ تا ۱۲۰ میلیون تومان فروخته می‌شوند.
🔹
فقط اقشار مرفه توان دسترسی به اینترنت بدون محدودیت را دارند و این مسئله شکاف دیجیتالی را تشدید کرده است.
🔹
کسب‌و کارهای آنلاین و دیجیتال از محدودیت اینترنت و هزینه‌های دسترسی آسیب جدی دیده‌اند /اقتصادنیوز
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/IranProxyV2/8333" target="_blank">📅 10:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8332">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://45cd71df-7b23-4568-8677-fdc4a0daa76e@protectnet.cloudinohost.com:443?security=tls&sni=protectnet.cloudinohost.com&alpn=h2,http/1.1&fp=chrome&type=ws&path=/&host=protectnet.cloudinohost.com&encryption=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/IranProxyV2/8332" target="_blank">📅 03:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8331">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✈️
Slipnet
slipnet-enc://AcwwsvYl4r7DajFRU6wa12enHS94jGWcw63dYwNxwSzZZDO03mNtFG6vROd+UO8opWIgDZkjjnUHlVvSaj/HvKW+p2HLBc4ETWvUWsMZpCwiUmAeEORd+qfA089iU7PBEHuvMqTIeRqwCA6OyylmfHRyIlB+dS4avIQQAJLxeW6G0ZMnp8HZ4VPpuiN2Vs3U7StRqxSwEP7f8wUXQy1DHgcCE9WD74CKd5RxaHADsaaT4Qj56xDB+DTB8l41JtvrbtjUVSNCS349vS8XyPhXi12t/YaAupzBKzSkPCXi8UjM8Ft2AyUuvLKTPgSMjJgI+vBT+16sztR9Q5n88GbrLNNWKD31CXYgjS4YNk8tLooUjYBgOKWmoBPVWCHej1RPyjs3lg64enMfTyX+WKjZ/fxrqH/8uGQZGj7qLjcGhGaohjHujN+ODCfxxAlK+6Y6eQFfld7UtXfyz9cTmhkk7mebn5exSrIv9o1auX6VVjUQ8xLMvhf6wwsD6vwQsblA6QeIvDoD8NUOfeKZFKrraoPjEdJexjOxcn9gbWSEM/QeqZB/lQ4LnfH6zHtP8PmH63PRZJTZUv6VlAovbrtWUp0ziB5fgISZTC4akBfBPTO32WXUTj+Wo1sSSeCH1rfVQAYoMqoQusLWWSHLm5Llfz5jW8qGwROFKxCq6HYzt4gLRZixvL44Dluxo+oyG14jHwsAmPVh05xydwjCI2XcpiJgX5De91xk+x39xMt7AwApPsraUbzuBscA/TU90Ehahp5NbRa0nr1Z44yGL0dC78sWZrPT5XtXbIE+Ydpd5qq3F1Y=
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/IranProxyV2/8331" target="_blank">📅 03:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8330">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره، دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول…</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/IranProxyV2/8330" target="_blank">📅 03:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8329">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8329" target="_blank">📅 23:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8328">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8328" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8327">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سوال اینجاس اینا از بازی ها هم میترسن باز نمیکنن حداقل مردم حوصلشون سر نره
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/IranProxyV2/8327" target="_blank">📅 23:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8326">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✈️
علی قلهکی، خبرنگار:
🔻
تا امروز بیش از ۴۹۰ هزار سیمکارت پرو فعال شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/IranProxyV2/8326" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8325">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">💎
𝗩𝟮𝗿𝗮𝘆𝗡𝗚 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻 or MahsaNG ( Psiphon)
vless://799f939b-964b-4416-84ac-18a6ace7fe70@camp.nahidapp.com:443?path=%2FIF_VPN_Bot&security=tls&encryption=none&insecure=0&host=camp.nahidapp.com&type=ws&allowInsecure=0&sni=camp.nahidapp.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8325" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8322">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJeOrSoq9oSu2mrsS0WT8mDH8-cKtmMfeF2_eyqesx2GWzUtKwYgwCQvVj9vU4T6VxsOof1GBVYQAXK9FMtItZDqB1cjwM8D53T0s-dXnQ8JAxKWwjxAAl3ekXy8H6g0pMFE2AY-9sOon9lHg0lS4xpi5NCPfQ3KPE4UENtH_xDQfYoD9uxqdRuIuuxt7yzdtaaZA30aqwOP4l51-dubvVrtuvVgVA-kYKMjGP863WRDIFm_06gsXXoNYmR6HwXxMYQaCfaJ6LxEoEtTIVFXtY8aHVLC8Tp8cpQ1sTOHahkPzJCOb3NukO5ZgQPQJIU8O5NFpR4G-w1ZM01Y5ZAi9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
وعده پزشکیان بالاخره درباره اینترنت :
◀️
ارتباطات و اینترنت به بخش جدانشدنی زندگی مردم تبدیل شده
‼️
به آقای عارف ماموریت دادم با لحاظ حساسیت‌های حکمرانی، نظر رهبری و وعده‌ای که به مردم داده بودم، در قالب ساختاری چابک موجبات خدمت‌رسانی بهتر دولت و تحقق انتظارات عمومی رو فراهم کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8322" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8321">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره،
دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول بدین صورته که شما کانفیگتون رو برای پشتیبانی ارسال میکنید و همون حجم باقی مانده براتون با ضریب دیگ چنج میشه به سرور ثابت البته با سرعت کمتری
2⃣
- روش دوم سرورتون تبدیل میشه به سرور تانل با سرعت بالا مث سرویس هایی که درحال حاضر در ربات هستند ولی، ما به تفاوتی باید پرداخت کنید بلا عوض
3⃣
- روش سومم اینه که کانفیگ هاتونو نگه دارین بعد از این شرایط نت از حالت ملی به حالت بین المللی تغییر کرد به ازای هرگیگ، ده برابر اضافه تر حجم دریافت خواهد کرد
🔻
@RUSSIAPROXYY_Admin
📌
به این آیدی جهت رفع مشکل پیام بدین
👆🏻</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8321" target="_blank">📅 20:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8320">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIZ68IPEcPDHtD5AbqIHAcArMEgeAwhC3Uet5adPdQrgrLQfM00zOMZQSDTK2CkKyEEMBl-kR6VyMWzUwiR6qNe9LC5Gs9CaeYDQ_2hYGhHnRtjrjz4W5ZCcpNV4mPAPrQlHwCoGfgeYhKcnpXmKW1cBzOIYJmni1qALN5M8sySEoHZtbS3sVotB6Ng9I7VWEmQDHcYEaB9y8AflrUTP8nEPpPpCwsefrbSJecIMY7dymyl8utOzTELHt-gWGFH5rVq57TW5523ogE3IQYvyJ1j42aU45hq4MBedzSFRuPPiCI4lWL00-pL9VZuB7PrfzjJDbJM3ZhBLOJ6gy2ZefA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت اینترنت پرو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/IranProxyV2/8320" target="_blank">📅 20:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8319">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✈️
دوستان نهایت تا امشب سعی میکنیم سرویس سرور تلگرامو اوکی کنیم، هواتونو داریم همونطور که وقتی هیچکس وصل نبود تو دوران جنگ با کمترین قیمت ممکن و کمترین سود ممکن بهتون بهترین سرویس ارائه میدادیم، سعی میکنم از جیب خودم هزینه کنم تا مشکلتونو برطرف کنم نگران نباشید
✈️
سرورای ثابت برای نت بین المللی و کلیه اپلیکیشن ها و سایت ها و... براتون تو ربات با کمترین قیمت ممکنه قرار دادم بازم امروز
قیمت هارو کاهش
دادم که دوستانی که شرایط مالی مناسبی ندارن هم بتونن کانفیگ تهیه کنند.
✈️
🎥
📸
💬
👾
📞
🤖
🔍
🕹
📱
⚡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8319" target="_blank">📅 18:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8318">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de826422e1.mp4?token=PYVNYcyZd6g0kMmHUbR-cKvyvyTW9e-1PoE2v2Xp94bOkfMCKbDsISmz8Zz_Z_rNCBFgMhybM_Uxh9KuiYURQGtQxnrvigD__pbC1yMYGodD7W1Gtkhp-Sl9n5-lHE4ILAQlKV0zxBAP3nEykGFAvngcQp8pP9B4P8Ni0LfN0MArj38leP7cdsPopuoyABfYkm4kNyEBSLB8qxZbURMmUlUHukEkzxepC7ht_r4NuO6RQGM3ynj3MrCT_KM3gw7snDeEg1sLbGKS0Q1g98yPcKOAFskByv1aihUY80F13PMM7Q9Qn0NbjdQosxVz4K22BxwLyBtSWMRwnnv6Ho6Q_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de826422e1.mp4?token=PYVNYcyZd6g0kMmHUbR-cKvyvyTW9e-1PoE2v2Xp94bOkfMCKbDsISmz8Zz_Z_rNCBFgMhybM_Uxh9KuiYURQGtQxnrvigD__pbC1yMYGodD7W1Gtkhp-Sl9n5-lHE4ILAQlKV0zxBAP3nEykGFAvngcQp8pP9B4P8Ni0LfN0MArj38leP7cdsPopuoyABfYkm4kNyEBSLB8qxZbURMmUlUHukEkzxepC7ht_r4NuO6RQGM3ynj3MrCT_KM3gw7snDeEg1sLbGKS0Q1g98yPcKOAFskByv1aihUY80F13PMM7Q9Qn0NbjdQosxVz4K22BxwLyBtSWMRwnnv6Ho6Q_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شهبازی مجری صداوسیما خطاب به مردم ایران:
اگه اینترنت 5G که افغانستان داره و مسترکارت که سوریه داره اینقد براتون مهمه؛ خب برین همون افغانستان و سوریه زندگی کنین!
﻿
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/IranProxyV2/8318" target="_blank">📅 16:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8317">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ایران اینترنت ندارد، روز هفتاد و چهارم …
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8317" target="_blank">📅 13:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8316">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⭕️
اطلاعیه:
وزیر ارتباطات گفت در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم.
همچنین طی پیگیری‌ از ISP اعلام کردند که اینترنت بین المللی شبکه خانگی متصل شده است اما هنوز زمان مشخصی در مورد اتصال دیتاسنترها به اینترنت بین المللی وجود ندارد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/IranProxyV2/8316" target="_blank">📅 12:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8315">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=PV22tqunz4CPWW2A-mHAD9c47NDojV3EoAHmN0NW_EzFdobyroLs9DCzvYXT5nj3rK7cWpbQbPCIqysx0KaTLVXU6pbJ5dCdOvr8ZiSNGBdHPoXFBKW9dQjlO_7rq7pYfXVlrgdoRv_n7SP8BlyQ9UCo1rl--Z1gFhm2n9Pau71uS1YSTZSHRZ1aZQn57Y4GH1VqQXrQo1PPJNsFyOgjSMQ-L2ScHBRHQZghlKYZUrtNybhrV2oMcZ3ClkbUBy7bL4by8VRgxEvdw1UKvf9W-iPf1Zt37iSMY4_gMQH37yI2B6cmMZgjsfHtaZ829ombhgBY6gKObUqUV76913fBWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde1d5a77d.mp4?token=PV22tqunz4CPWW2A-mHAD9c47NDojV3EoAHmN0NW_EzFdobyroLs9DCzvYXT5nj3rK7cWpbQbPCIqysx0KaTLVXU6pbJ5dCdOvr8ZiSNGBdHPoXFBKW9dQjlO_7rq7pYfXVlrgdoRv_n7SP8BlyQ9UCo1rl--Z1gFhm2n9Pau71uS1YSTZSHRZ1aZQn57Y4GH1VqQXrQo1PPJNsFyOgjSMQ-L2ScHBRHQZghlKYZUrtNybhrV2oMcZ3ClkbUBy7bL4by8VRgxEvdw1UKvf9W-iPf1Zt37iSMY4_gMQH37yI2B6cmMZgjsfHtaZ829ombhgBY6gKObUqUV76913fBWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی:
اینترنت حق مردم است؛ عصبانیت مردم کاملا درست است/ عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8315" target="_blank">📅 11:59 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
