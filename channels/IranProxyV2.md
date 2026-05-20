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
<img src="https://cdn4.telesco.pe/file/OlQqS6egUC9pjFtoAQ2EnpqFCq1t6tnBNjo3a5VB2QLbxmFP1UiAvH2dWVsJymzJ4z00GufhgEJKLvhUCMBoXOqiRL5TYDpsN9_gzk5WCWHkBeUEVHx-AMm9lEGS-pRN9Y7g0dulTXUR_gOzsRG3FA7SbFH9DrObBtEmM7Kf4OJu2KhbMvI715MKQLmoQfY0FExakeRkYdndFuhIX6kvFuIO0mbu2k0vGiZ4h48fdnmiMbUB2XQtT6lVldZiwWyxO9sKwoq0_Wqhpy0blmNEEkQpEeqJX1qW3ayaFfxanQHD2EvneI67eRYqVyc7Es-jBmhdIR3QuvR_Z87n83-BFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 38.8K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 14:55:14</div>
<hr>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C304P-nsLVKM-von7U7xm02ayAZlLbRbtcXFehuWmxWlgEPDdY3vLhJicDzD-L495UnaTs_MQVA6BgpHsda3IRGYBg_1sU2m29Zq5DGMUHY6sUG3O02byYU33ujsyF7_E6ydXWXoRxsNlcizfVjxe_zy1OgarT8JIAZxSsUXQuqG7FD-meZ4DcZqdc4glr9ytthkCju_CVUgRQkBJNO9KkiD0X11NdjiTGz8g9ErGJkyDt6h8-sJyNbwb7x18lLdkQtzyMQePdACv6z47ULiuV416LluFekWW-GwfoL0VR61EP3A4yUgtQ0GwZUZm9sVUbGIay3WHeMd59vOkLV_Lw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jugvo_YcIRb8bKDeVzM1nxUEPa34JrjmphHrCyzoIroo9p52Zt3a6127inxdxEQmJihS5m6kTDWYDojNzrQd9Lb8cleZEiqxWscKdUctbozmCLjcB9ocNhdgRbzqmiYvoTdYEl_qV_S-9LMmghJj7TZPuHHSS9PBEu0N8jkbMxfKOk4r-RF7TCeJ-2nVOhFfl8vSF4BQM0YXg_4qB3K-3NE0BeABrV3tbNgj5V0pbFD1Bx5Ms9PQbu0BeNdLVe5O2U6pjMkU48E3ovAoSDhhYH7hiINfES-3XAiIyeCxP02hvBpaM_Te29n8DMiqI1V0bv1J3bt2fJFf7ZHa7WohJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFtnLSz2OXuD4F-G1UsNGYRfN-ZFv4A4chglejPMpJU0DGEEsKKCYiYlozu73xMeaFCOoDSU7u_VbVMuloJcjWO-0Fler4jKdc0NQqx7Ac55Ltgsz7a9URfKzjPMwNSDoL2TB5eHP5tp0XvHdUwvDufYoQsvdyFbdjRTLDnePQ2ypBQwplfqpdMiZkhHnC7SgjJ4fH4SCO1FXicdVJymXmibRug9TYfe1YPF4lkYH3dt-KeIbHWTozi1kuJx5lwxDVurcZ0aIOj-FaTn7fRUkrzyjAkevb7YBTHrktCAX7x54VPlMkHjHBinllhe9hCJvvo8bJYBIERZzp5m18I9ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=o50j5r8-h5IBPzVLxiWKfelKZIlSuSzGYxXCnarZtfDSWp1B76N55R_PzO4L4-sKemDYWjU_oaGP3k7udPUuo__CmhCR9JN95W9YgKGzw2WVqf18vVJ4ULemNAPZxpCQN-0x7BE99Z5z8sOEO7QeF9yDUoCxp8w7zfbX52v7dUtCMHsnBsikSN0_J1A20bde1Y4c5_twDyMcK53PutfMAQgE4U9P-raz4wyNaBgQQxnHUzHAtuSlHzI_TXQ6jBZ9y6P3lLwgkYAqVxWrR_se_Jov2gjLZVTbxK6Tc9ln2vTfOfLmuQ2sxfL5aZVq_K8cfVIO8ArEWT_5YoGS1pmzK3voFkfLSHG4gBqB1hO127rJfBsZnfu77X-NXSlQw6mCtnOxO9pe8hQ88Q8o2xvN0PyjZLelLAXAgQisZVCYwBFFU5EB2unOfs8zAmFple-Z9M8RqpxL5W3jAXXpxmm70Tzo_XvrM2WE7AklKzBDfuYoaZ3f5q4rlYyJhO7a5Y3dD2hWQo-H5SDrPtLtwHlCEbjKkzIsRW-hSxK9FPS0PWqWkQrP64120nnf345cFdkvzIvwO6ykDjq7zEwC2LE1NyW3aXUQRoSmIqxBhj-RY8Wqmd48zzl8UBwTjywsa2uknnP5ir1WP5HzZaV47hM7eBMIBloLlqqPqrW8yNN0CAE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=o50j5r8-h5IBPzVLxiWKfelKZIlSuSzGYxXCnarZtfDSWp1B76N55R_PzO4L4-sKemDYWjU_oaGP3k7udPUuo__CmhCR9JN95W9YgKGzw2WVqf18vVJ4ULemNAPZxpCQN-0x7BE99Z5z8sOEO7QeF9yDUoCxp8w7zfbX52v7dUtCMHsnBsikSN0_J1A20bde1Y4c5_twDyMcK53PutfMAQgE4U9P-raz4wyNaBgQQxnHUzHAtuSlHzI_TXQ6jBZ9y6P3lLwgkYAqVxWrR_se_Jov2gjLZVTbxK6Tc9ln2vTfOfLmuQ2sxfL5aZVq_K8cfVIO8ArEWT_5YoGS1pmzK3voFkfLSHG4gBqB1hO127rJfBsZnfu77X-NXSlQw6mCtnOxO9pe8hQ88Q8o2xvN0PyjZLelLAXAgQisZVCYwBFFU5EB2unOfs8zAmFple-Z9M8RqpxL5W3jAXXpxmm70Tzo_XvrM2WE7AklKzBDfuYoaZ3f5q4rlYyJhO7a5Y3dD2hWQo-H5SDrPtLtwHlCEbjKkzIsRW-hSxK9FPS0PWqWkQrP64120nnf345cFdkvzIvwO6ykDjq7zEwC2LE1NyW3aXUQRoSmIqxBhj-RY8Wqmd48zzl8UBwTjywsa2uknnP5ir1WP5HzZaV47hM7eBMIBloLlqqPqrW8yNN0CAE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=nmHHndobToo0RoXfqvQIwbtwyR7-8ctaHpY6e6fLFn_av5TOBMYLuaFd-mR5xL5G0Ge2W4TbzpFYZFUb6mcod842wLnnt_day93By_WRH3mDa-hhL5M8cUv2W8fUmuKVQdHXslMdXcSieaB7Crzgu5tyIypXfkKsIREhXXX6bTKdTqZXiIYb7Nfr014WJ8bEt0ONtGG_GQNlqWJHM1c-lgUlqngWcnqcBfWfVQb9U2uoptiBBN2YvK6vN17zQdu661b8MBSYDF-sJDxOd_XbMk7Us7jrS-nCMisirxgdCn2BIbvUbBZsNMlaLN8VlF0NLFPUSBn48eYMRynOLS8vzq9tKL0wQ8qvclR4DP_QnaIREBj6Vzxpg-XsBZzj0q8jQHQIFycrnTTUtU8ahBlzXdnTKbZ3wgcHRjut3cd0rbkPM1tl0bZd8e4_gj2ewMZfqIUuv8YuH-lmpyx6J6FsYmLBulAl-VYuBjxrG4mD3Ch_YBCnlFQMm51weDR1RCzyTzkN2CuaxDzFEdpmH2OHgHz2ctF0r2DRFUhJO1zzu11gVH1o9T9BOyxd-LUakfeUWeEHi5rv960RwwZZdNAd2f1wg5wsHn1BQ44w7NqykCIloZQcKJl-Vs21itxYtSvbwKmShtrmJikKvbUs5-guZqjtwoN4bh81lxgjn3l0S2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=nmHHndobToo0RoXfqvQIwbtwyR7-8ctaHpY6e6fLFn_av5TOBMYLuaFd-mR5xL5G0Ge2W4TbzpFYZFUb6mcod842wLnnt_day93By_WRH3mDa-hhL5M8cUv2W8fUmuKVQdHXslMdXcSieaB7Crzgu5tyIypXfkKsIREhXXX6bTKdTqZXiIYb7Nfr014WJ8bEt0ONtGG_GQNlqWJHM1c-lgUlqngWcnqcBfWfVQb9U2uoptiBBN2YvK6vN17zQdu661b8MBSYDF-sJDxOd_XbMk7Us7jrS-nCMisirxgdCn2BIbvUbBZsNMlaLN8VlF0NLFPUSBn48eYMRynOLS8vzq9tKL0wQ8qvclR4DP_QnaIREBj6Vzxpg-XsBZzj0q8jQHQIFycrnTTUtU8ahBlzXdnTKbZ3wgcHRjut3cd0rbkPM1tl0bZd8e4_gj2ewMZfqIUuv8YuH-lmpyx6J6FsYmLBulAl-VYuBjxrG4mD3Ch_YBCnlFQMm51weDR1RCzyTzkN2CuaxDzFEdpmH2OHgHz2ctF0r2DRFUhJO1zzu11gVH1o9T9BOyxd-LUakfeUWeEHi5rv960RwwZZdNAd2f1wg5wsHn1BQ44w7NqykCIloZQcKJl-Vs21itxYtSvbwKmShtrmJikKvbUs5-guZqjtwoN4bh81lxgjn3l0S2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joM-OsNcUxpyiqxoVAFL3mg732qcgnP1ZhPtdDOkNN4Y3dk7olG2sZn3svMrNHrFP3nIfJtfoyE9enUONeCIF_HT_L6eaBI0Rny4u9MUnZ8ok-0WtFeMvj1H8OxPUWYN-dUHMUN2ULa1tgnx8NeNRi1pQOCuaCxkCD-Rbyhv53tngwwQ1gS298nRWKTvwBJY2PXdo73THiQ6ksuQfovIeTnqsaZvDhdwXaBugpp94M2KGGc6usPoKoaDE4-qvULP5vtktGNsRp-qXZANL7TpQXa5x5vDjukIim-oykGIkQFq-D0ohCOiOYuJ4oUMf8hfGUDMGPAXkcs7JXzHx6QazQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=sS5y-nQb456Roo66ZM00C7T72GlLjt8hgSrHSVRkSBEt64buXDQVc8MtqE-naxxINUuwhr-w4dLmIfbU_9cemDgpgfSRGNZRkvkdluyTsnGjOCre88TWiibR9ZCDv4QW8qR8QjRM9sfTLTV6xf4gjssJXtEXnfI0XP1IbadbrnwaKqQtHPT152Nok8coF2f3F-ANtA-Z07YURPBLc0g3veY9vkAYZovoq5aevBZukI_Vxf6sMrw05H_mblcpXNV0rLVp5IC0e4SKYTGjLMFbMaSUBobrOG8Tam3OMXPZtjEU_R1fNnWfHbm8pYQEyk9xrK_4hhEsHlrTTnbSWJTlODx3IFWniUauxbAMEejO4kDj6-dbGDFjNyZBWx0NyGSbStAN1dByh4cM8anBk5toR_Lijwhya99AgnpGNJ9ZTFi64gTAm08E5YB-9dZUoM8n5h01qJuANWpju30QRBUUyMktIYrgqAUJh3gLlpWwkOpSFE3RzIdZ2gkX18ZStDayH9X8x08yXhgkGHoz1-vP6Z06NY-4wDGn4ExpPJ47fIcRQT6c-u0Ebxoj2kGUnK4aUJcqK-BOXkmcxdb-ss7ROmmIa09P14aBO2UcoY2SZWJZiXVn96DgMrOrtWu9BPxFfdOETaYyWvRyhcaIHIe0cqaRSFXWWlQGho-c9V5DWXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=sS5y-nQb456Roo66ZM00C7T72GlLjt8hgSrHSVRkSBEt64buXDQVc8MtqE-naxxINUuwhr-w4dLmIfbU_9cemDgpgfSRGNZRkvkdluyTsnGjOCre88TWiibR9ZCDv4QW8qR8QjRM9sfTLTV6xf4gjssJXtEXnfI0XP1IbadbrnwaKqQtHPT152Nok8coF2f3F-ANtA-Z07YURPBLc0g3veY9vkAYZovoq5aevBZukI_Vxf6sMrw05H_mblcpXNV0rLVp5IC0e4SKYTGjLMFbMaSUBobrOG8Tam3OMXPZtjEU_R1fNnWfHbm8pYQEyk9xrK_4hhEsHlrTTnbSWJTlODx3IFWniUauxbAMEejO4kDj6-dbGDFjNyZBWx0NyGSbStAN1dByh4cM8anBk5toR_Lijwhya99AgnpGNJ9ZTFi64gTAm08E5YB-9dZUoM8n5h01qJuANWpju30QRBUUyMktIYrgqAUJh3gLlpWwkOpSFE3RzIdZ2gkX18ZStDayH9X8x08yXhgkGHoz1-vP6Z06NY-4wDGn4ExpPJ47fIcRQT6c-u0Ebxoj2kGUnK4aUJcqK-BOXkmcxdb-ss7ROmmIa09P14aBO2UcoY2SZWJZiXVn96DgMrOrtWu9BPxFfdOETaYyWvRyhcaIHIe0cqaRSFXWWlQGho-c9V5DWXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLncD_-ucc5Fff7dx56r6EKQD_RDZbbg7fh17sJsV7zr4GOti1UjUJUKos_rzruOvZlplfvSR86Bxj3xB3urj8d0yFwwyEG3Jdbqw78IMZY_zoarMToK8h5Sr_c425WyFR4PPmh1poYzB0iNb7S7BNRffLpkBNjgDu3FZKd0o5fHi_NeQob41GxNx2orJFXiNovof3hsaM6VSkokD6WkMbzShB6yuAyCgy1aEPHce2PGHZ8uWUMscK6kX2A9dbmufd9Wnm6X6eScDySPtmSGHSLHjuz_TqA1JCCUyeB49oCUcF4C5dp2n9QxEZC1NAqUzf1rArYkr81gF9Vrjd_e9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sot9F4vBgf8J96VpoJrzRFTbw9eCG7ggiwHP-EDMXQhT61FVKxj0behH0KwB6SESgmS85L8tOY2umiUSz3jAWXEERgCKQ3o1gKSACiZyo6abCKNXNq-owxSwC0fVs_MqZPppcZ-QqP6rVDAX_XKBoMXFJkGDLjUpsYrbOG0ERoR3QSqTRt5NALing_5O8LvfbOuhu1qgSQgbi-1SooVFTUX6An8cBavpGmo0Qw3xcfJu8tclYksRuNBknWdcnIonOtWBHC6bJOGPK0YOZiibaGiQ-iEiCnrAV2CZYq7mJBdY1N4kFPxHSDo6sP-rkVp4ls3Ua5gpc4AvwNukerqzcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=WCg_S2EV9ywgrC3BbgBEVXz_6LmyF8cTy1ZIY_80LCZ0G4CJUuIicSpFbq-GkSAsyALC5NQaNMpOgBJLBvY4MjMJRJqmp7Wt0HlBUNKPJnF1udeqH9txNvjHYyJ79YdLgpGP64CJMpRCLkaw6syE6HKQ97OL10hHQ0Af_NcWT-UAE1nx4AJbfcWxq75vCSC2W5lIq-HBEhl6N8uMyG3JvJVXtNMBc1zewfbpneLkGQl2Awjo3PwSfjfliwgnPqQQnMDAzYd2nccBh0YM3o_x6OsGCoT3VFvyqM8lGKn_M961qCcLkD4oWAGM4O2jNwvQ5shwXARiU39gbZGEA0XKig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=WCg_S2EV9ywgrC3BbgBEVXz_6LmyF8cTy1ZIY_80LCZ0G4CJUuIicSpFbq-GkSAsyALC5NQaNMpOgBJLBvY4MjMJRJqmp7Wt0HlBUNKPJnF1udeqH9txNvjHYyJ79YdLgpGP64CJMpRCLkaw6syE6HKQ97OL10hHQ0Af_NcWT-UAE1nx4AJbfcWxq75vCSC2W5lIq-HBEhl6N8uMyG3JvJVXtNMBc1zewfbpneLkGQl2Awjo3PwSfjfliwgnPqQQnMDAzYd2nccBh0YM3o_x6OsGCoT3VFvyqM8lGKn_M961qCcLkD4oWAGM4O2jNwvQ5shwXARiU39gbZGEA0XKig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWMNQ8inlRQkcuo3F8kwzDwjxUm6mxctkWwMfmAdCPN9xPL78LRytKJ3uoNH68oGwS6teau29dux9FEjmOcWNINEENUxQOqKKxH9hngtdFmaAGgy2UH-GMEjeD4SrezYD7PGlhlVYMANMOL5JL2lZt6mHEM5wqvuHSmYN148HygvlUehWTiKq3DyIAQLWfYgGotT4DJLJ8Nb9smgZ2xRmbhtGwt1fMFOEQf6DTC-F7toR92uZs1Dh5CVORZLeJXbKHVmgTZ523i2lzWizWsTsdOWbhCzwdmE16XqjW9wPrD-se_v12A4EM-CEcqNQuBQiERxRGgIOgk5Lju3FqTuCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uc0TxDMtLUJTWPg95LgWv0lpSt0Uzwl2jcNrHtKWDvx_ONbOLVoei_PmJbJQYvquH6b1V1wlfHMEaq6Q6mkoAmi477sWBS4E6plqwFQGEkVrPxy8idkEPV2rpa1XnoHywmUV38zaaLn89K1aqM0I7__htlwNgvTENBizKLyBggQnFxUoH-Fdc3DeQuRRRiqHXLYJfj4Ovthi5eI3mF3HAr4EzX5iqBrVeJABbDdmiy3kMQz0X35Kupm8ixVfH_5yPHjNvbhnqr7WwpQYO6xGJD0mF_lT3M3iSgxz0AfQhvZfk7AVhNedehuhxBPo2Q3SBGzaQgo6VNeFZWLGJgG8HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=Uos7xrmFTiYYniDFtfCwAnyOrkkOuIMX48EdGcThOun3eIT5CNQaH_9HGapNu_tS9-7Adet_KaiHl2EKrWBe1lDXmDZsFMMtv5h7zvQb5OQB-NYpJDI596yPyYW04VTjLpPsTwCOhsk1eJ6d9ToL7Lm6dukHO2K5zf6PAysZoOYK9AIAYfhbR9qnvrPMhBZpB_3PthUOFaWWRSka5kHe7-k-0PAYkgEnbB5xbF5PAqXRGKmKTOJXrLMEueXXss5y_zDzODuYRHXkHdQbWyQSIuqZ0VzdJiTAlRExMNTXaSgKrp5M7yBsfFMLCyi1ig8l1nZiBpTJ0q3BFU6uIwz55Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=Uos7xrmFTiYYniDFtfCwAnyOrkkOuIMX48EdGcThOun3eIT5CNQaH_9HGapNu_tS9-7Adet_KaiHl2EKrWBe1lDXmDZsFMMtv5h7zvQb5OQB-NYpJDI596yPyYW04VTjLpPsTwCOhsk1eJ6d9ToL7Lm6dukHO2K5zf6PAysZoOYK9AIAYfhbR9qnvrPMhBZpB_3PthUOFaWWRSka5kHe7-k-0PAYkgEnbB5xbF5PAqXRGKmKTOJXrLMEueXXss5y_zDzODuYRHXkHdQbWyQSIuqZ0VzdJiTAlRExMNTXaSgKrp5M7yBsfFMLCyi1ig8l1nZiBpTJ0q3BFU6uIwz55Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=p_7pj5M2-6Ybo3as0BqOGR3n__cHIlaTPgZ91hmGXJNDLtKesA2Kubty7P8O3-BGIeeeHjFZztG1j8X6k9zMFTrmGZIb1zeV3St-4LRbuwMInxMq2G3HCDLCoISPy88Sh94JtX6UrChRyj2LYzQFHakd1NeCFLSLTT5d90hiimSKBxdBlPwJP_YZMfHpCB9hUpMYPysJZdxWCx_fbvzk4tTYNRRO4ICAAw9uIOcvPLm0qyCRGdW27U3JwA9QA73FoVPp3uDKZZDFI_pmxPs_2EOuy-FmIkG_HAPdF3YP7rbFer_Q9ZSuszlwIu1ZEtq5kY9sG0XOMLlhKRyQtprhxbL0Qx20XnW7WKSDb8WGG_ZV4zOA4VoBYWroYKWkLqVS6Oa-1k39TsKIq77N4K4t_rj9R7uW9cQoTN8Txr2sZAY5GBUIDCmgMeaH0CDXgKHEryxYMCh-Gb47jsyI3TNTb3Lz6WgX7aA17gfxGGO-f1CYekxXCRNNcL5U_thLOL30C-4Pv45iCYcb_a6RBHP_dQ7eReHiSXQLYlkIS03hHhHMbeV-LXvXdNKMVx8VaVWOPZnK6TGT-1wHcg3IV4Yr_NnaCF-eAe46IwZMA-v8ovKjZ5sh0NOmrOoqbnFbuibbMYxUE39cZQutgQ-vVw605KlHkYyQu7Rj28onckK1JLk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=p_7pj5M2-6Ybo3as0BqOGR3n__cHIlaTPgZ91hmGXJNDLtKesA2Kubty7P8O3-BGIeeeHjFZztG1j8X6k9zMFTrmGZIb1zeV3St-4LRbuwMInxMq2G3HCDLCoISPy88Sh94JtX6UrChRyj2LYzQFHakd1NeCFLSLTT5d90hiimSKBxdBlPwJP_YZMfHpCB9hUpMYPysJZdxWCx_fbvzk4tTYNRRO4ICAAw9uIOcvPLm0qyCRGdW27U3JwA9QA73FoVPp3uDKZZDFI_pmxPs_2EOuy-FmIkG_HAPdF3YP7rbFer_Q9ZSuszlwIu1ZEtq5kY9sG0XOMLlhKRyQtprhxbL0Qx20XnW7WKSDb8WGG_ZV4zOA4VoBYWroYKWkLqVS6Oa-1k39TsKIq77N4K4t_rj9R7uW9cQoTN8Txr2sZAY5GBUIDCmgMeaH0CDXgKHEryxYMCh-Gb47jsyI3TNTb3Lz6WgX7aA17gfxGGO-f1CYekxXCRNNcL5U_thLOL30C-4Pv45iCYcb_a6RBHP_dQ7eReHiSXQLYlkIS03hHhHMbeV-LXvXdNKMVx8VaVWOPZnK6TGT-1wHcg3IV4Yr_NnaCF-eAe46IwZMA-v8ovKjZ5sh0NOmrOoqbnFbuibbMYxUE39cZQutgQ-vVw605KlHkYyQu7Rj28onckK1JLk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJ6Q0l635ji1JADsV7QEJAKSNXvS8z4t22luGQouEa2kEGCeR-m6-CODqLDv5kiep1qntEoSNlKr2hMGFa3fmv6aP8pc3pd1NIZHCsnSe9TX3hEjauntNcR38JUoUkaLDDLERLb8BMoijTf8UzToGaVWT4N5lv_00zf6FV2iPTJvIKktghOCOme-cLWcvtFJM4i8vDtjdql7eAAxxExR2IIMLAKO2lIlZMBA1fqhHFNNZeU97VEVbbpjaNyzHLcyHB01p6C6elz1afUiJDCJ7cuyoNJ3IK_ST7ylJndZC53h0_JaiRUfLO55anhp1mZ0phuBLQ7OhkfiHW0Gg4cDdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTGyllC8JqQU2sr-31vyQIszLtjTl2DLZFVMixMn3gDAfgXeoBFtDH-oq9nOLobfJpGuv6ni9Z1qezmGlse869qyl41_k1res5WpoGuDB3U-ZmVcqFChrgAufjLhqW9NDCtLeLLRK3Ry6cH06vDNY5N3q3Ai4449WGkyEmqzljdeFMk7HJxOlkZxvJk85zqb3m2ogj3vHkq0QxDAbuC7rJx50l0xoiRT1RfszeJK12UCMtDp-dtfSdwXouyfLGGfNprfpnKZ0seYmHNfpY2fY6uCDKZPyPlTPSgQxd_qx_ovv0fFqwS2j3CdcK5si2wL1TuCw0RKomch50pKqODKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f5s6FstdCsDmPwvzaY4H2PyHDjrfEXeOyyw7BczYBY_ANkSQOZQEqrQjLxCrnV5I7YpXNYfwbSYtg9OLAXem2EcHyosBJsZPGk5mVOyUKgHEKUSKsc4ZCXOE3PNx3I8FgtW2AUn-dOhucaXNAL3em-75m4jVG65wdPYQk72Csyp5vJWxdrO87uZUmXpnDn3A1YWGqs-T7IUTanzM2G7dK_XHUvrN27rNwFjGb7gTbuXKbaRpxIUfKE7nxkAFnOzWmPxPNlHTPbArQgDe14XvBB0mdq4y5eKTksRD03MBQXBV12to_lqnjMzWiKLVpmw_sLGDaC0txPH6TYDMzariaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=D2hmKwq8X8WZSBfUpfsHToSvugQulcCI98InZqXK8fxkbV3YNKhvIDiizxVVhbYiz3tJxb1GMeN7ZYPTkwUGqAOITIyLFhlqxX9K2GnhcyMOkUY6gKMbmy1vKg2MpWqVZCc13LnczqxB02uSGAhO6vvRe_v5a9jaO0VhIK94utbPH5w1eDL2h0W9sl1MX7z1kz2gTVDru8WDDcErE5vf0v3BMCuK-fNcp2Sm6gpbyx0ywwjR-wLcHkV3FW-gAvPk0mU8dNMlcuvZhbsHs3HGt2gxH-dOw03xN0IaIDcmygfpkbV3C9D7C1mguou8yQJn7IB8wePAzyUQBjYkTVyxv4xaIWOaW2eEGUw7eIc4mU99qY0iqJqE6OWbX5u_dsK-eXoRi9Ky1nGAMqdUC_naeb2H-F4VE7v34TT5abZP9B8q4f8jdjQe4-vz0Dw4wGtzx-fncD9RkiOPXvMr3_0N71y29cECmlhPRlIb9uA83hSPtZ6NqvmCrvl4s-EFK573WATmIxnp0YtYrHL95G7cATIYjXyZw9U04pOfxyAI5ByLO4bQN5bQMpvky4tdP-CCM1eIEZbkKzhtWGJtuS2ifWm64FStRrDLdrMnaENNRK_XynBuqPqaYDHdJc3sQ8HEGttmfKM9jURjZXsT8-TYsTNBIT7vY6YNfJUqk5zKLYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=D2hmKwq8X8WZSBfUpfsHToSvugQulcCI98InZqXK8fxkbV3YNKhvIDiizxVVhbYiz3tJxb1GMeN7ZYPTkwUGqAOITIyLFhlqxX9K2GnhcyMOkUY6gKMbmy1vKg2MpWqVZCc13LnczqxB02uSGAhO6vvRe_v5a9jaO0VhIK94utbPH5w1eDL2h0W9sl1MX7z1kz2gTVDru8WDDcErE5vf0v3BMCuK-fNcp2Sm6gpbyx0ywwjR-wLcHkV3FW-gAvPk0mU8dNMlcuvZhbsHs3HGt2gxH-dOw03xN0IaIDcmygfpkbV3C9D7C1mguou8yQJn7IB8wePAzyUQBjYkTVyxv4xaIWOaW2eEGUw7eIc4mU99qY0iqJqE6OWbX5u_dsK-eXoRi9Ky1nGAMqdUC_naeb2H-F4VE7v34TT5abZP9B8q4f8jdjQe4-vz0Dw4wGtzx-fncD9RkiOPXvMr3_0N71y29cECmlhPRlIb9uA83hSPtZ6NqvmCrvl4s-EFK573WATmIxnp0YtYrHL95G7cATIYjXyZw9U04pOfxyAI5ByLO4bQN5bQMpvky4tdP-CCM1eIEZbkKzhtWGJtuS2ifWm64FStRrDLdrMnaENNRK_XynBuqPqaYDHdJc3sQ8HEGttmfKM9jURjZXsT8-TYsTNBIT7vY6YNfJUqk5zKLYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBrvJjtjX1BXyasxdSixOxFtMdsEWBNt1ArgH27Pi63AblfJLSRs1FCsqX6fmKUu_XeNPk-4vpYZFD_IwE4sulOO7zxDQ1aUlIiySGQ3GY4a0gZXsmzla-zCoEfh9gswU-1Lot7D8szg57V9ZaFZWapKT8Qt8gfqfYDilSA3xY5iq5SbUB4M93INTo42urGbxA3n00z0eBtSdlkVlJmGXJSJU1aKWwInLMVpDTAoVpFfvFyJpcMubhAepaMuFyWRj8LgxcbLq8VkHgeOuA4TeCbjpL6eLXdIsb6PjCqkRq-chpamtYUEg3-GjP8gtcXyLoGPidYZkaYLgSJSClWevACg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBrvJjtjX1BXyasxdSixOxFtMdsEWBNt1ArgH27Pi63AblfJLSRs1FCsqX6fmKUu_XeNPk-4vpYZFD_IwE4sulOO7zxDQ1aUlIiySGQ3GY4a0gZXsmzla-zCoEfh9gswU-1Lot7D8szg57V9ZaFZWapKT8Qt8gfqfYDilSA3xY5iq5SbUB4M93INTo42urGbxA3n00z0eBtSdlkVlJmGXJSJU1aKWwInLMVpDTAoVpFfvFyJpcMubhAepaMuFyWRj8LgxcbLq8VkHgeOuA4TeCbjpL6eLXdIsb6PjCqkRq-chpamtYUEg3-GjP8gtcXyLoGPidYZkaYLgSJSClWevACg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rZv2QJIqcZkH0fTauw6_TSeSKPx4seSqCgRnFqFcacDCjdjpt_nmHyUS_Jdt8gM1K0dDa-jVJgpXhrulm2OSFf-KDRMBXyVYASbXcqWCPDtKENx0DmWhcffxRBAmZz62l4Vn5jotJU-4dz7HQ6hVWfYhMSQ8LN_9WxHBgVHi_eaYPpRvZZPaM1mo0ODPDcgHY9Wgf4tImkcXADLsF0sPbeqilwGhSUwnYlEqAa4X7KusV0O3PGMWYlj8r8uxzkNRsAh5w8UABq7TGFXYbIWda2VWDWFSH_apxKYsO4x8eHSqkiWejX3jKWeNGcczVkMwioTaCNkuMBCCBpeGUmv52g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
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
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
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
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2DEvugSD0wB7dakTZMDs4HQ4xK55X2O0rBzEoyFxXV19biT7XylnslNX44LWtn0nqOZgxtZXVgsHCOG1kS20Eq8VUoacz--Pk0qx1Uz-54VVHyZHZaKteksT_KXpTGLLp0Ewerk0xAsFJHj5HblUI79tAgASGh4SP5PhUtOxg0z3apKXsAmheaTbXFWvwgCwBx6Lo0tbKTxSfWsqarlIIIFI6znZJoAml5rf_z76ACtGwe7px5GWap2juVOKdBnUAT4BOuRj1Xt0Dd_N5vwnJC5We65PvEPaPWfgP48IE_FGqZkj6s1r9Oc_w-X5E9kaPVJ69BVvmpMO6QhbVHlPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=hphY4Pct0b5Fpcgf7QCCtmGlIHPutoYKo4rgvyUTiH2WEaar9sp-JrtHWvZpbGiDxOhb9U06JBkOP_pDk9a1NBzxJMp77Apvt_0w0lU78vXsTB9aY7Ueq2_sakuJICzT7vu70bdeeGwgy2bBHI5llDbtqXEN-MboKTLS8mXVRtSJoD6mfO4QuHfYQTw_JIW7R9KQyv36OzCmEzfvJauFrBb3oPu4WgmTi437hVVqKpoQHOVK8vXzDTN-GupiAgpgQwCYkhHvmandLm95u_4XS-4onOV-DF8BYb20hBauAyg6bJS7FsLAqKM25iA35JaWrHfxzVd4Xtk7Y5WuroNiOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=hphY4Pct0b5Fpcgf7QCCtmGlIHPutoYKo4rgvyUTiH2WEaar9sp-JrtHWvZpbGiDxOhb9U06JBkOP_pDk9a1NBzxJMp77Apvt_0w0lU78vXsTB9aY7Ueq2_sakuJICzT7vu70bdeeGwgy2bBHI5llDbtqXEN-MboKTLS8mXVRtSJoD6mfO4QuHfYQTw_JIW7R9KQyv36OzCmEzfvJauFrBb3oPu4WgmTi437hVVqKpoQHOVK8vXzDTN-GupiAgpgQwCYkhHvmandLm95u_4XS-4onOV-DF8BYb20hBauAyg6bJS7FsLAqKM25iA35JaWrHfxzVd4Xtk7Y5WuroNiOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینک از وضعیت سرعت کانفیگ ها که بخاین تبدیل کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ez62lUVSuWHy3v0DOJCGeiB8wwEGbyT1bLXsNnqUKqsD894mqO7BxPrmXbQJpQkBc4UKppTP2YtOpA7GPV05enF7KSUIadejAFhTbfgkXnErmEbp9qoFYi1drLTvy0H0Jefv2-_daYZyG4FtWSD8q0XkazRFvxQlHRoz1J3GPQOMnq-6d6mx8uAYFaXgLfEc1IkOU-v1ZjtWQ3BYtXBWoU6wfOpHQXQLd-4g7TQ0BhWcKbECBynpnsPizA_rfCrkOMMeZ4vrNuWCC-Nine6LOQqEiJMq-EzuJWGhQagkOSLI_3wKLtugg4F34ZSRVih9F4H3gmgdT_mfGYxSsd1qOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r4CxsNaSf4QHg6a-uC6XYNNp3fdYBGbuPCVSkXxEJ0sJiepoKe-27kTsFSdswS-SnLO2GtnkJFpdWBL5ItH4WUzFVK-yBSV_VJO7Aem1kyCDipwTxgvbLeIizrhNEnRG_ydTHcN5FmlRnAkj5z6mogm0P6cpjpJv0CWFvGaU6ipZPZILt4HtfYfrLlqrwMmhNXwKUx1O5OMt8UEIEWJuwlfZs0B2yxUG8z0xPmtwZONAhqoSbUYotniFIYDYQ8f_9lrKPEULbazALd34POjKKJMtUPz2gg3oE7IdnhYr1VLAcoGqmx-rR_dAWJ87dsfdpzHhxcQh3a_CdHNhip4WLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tHMI_C8MRT-BeB3M8r1FtWajNdRSHCr1kSwtvvExYnK5Kl2b5v0_7RdNKXip5du8BQevddQTx4r7pzhnGN-DPRtedGLaO112atZZXAgVvOXBBUM89JmKERH_jGjXcQi70ff9ApA0_X5rZh4YnUacTB5WQHUdXb4jk1529zUPawmEvypMOCzr-R_O-xPd0C0pl_207kq-Ow0BLt9uzlx-yuaofTOyDw1Sjq_9UmkeHMGIIgSRx1i__kl97CzO_gi4a1Q3MTs7yaQXJvj8oNO-uq3op9OK8seJaW3Kh8gVm2XS1fOI9IFB9ByD0K8NNz5qMyjVfokwOCup1ew6Onj--w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8333">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/IranProxyV2/8333" target="_blank">📅 10:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8332">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://45cd71df-7b23-4568-8677-fdc4a0daa76e@protectnet.cloudinohost.com:443?security=tls&sni=protectnet.cloudinohost.com&alpn=h2,http/1.1&fp=chrome&type=ws&path=/&host=protectnet.cloudinohost.com&encryption=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/IranProxyV2/8332" target="_blank">📅 03:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8331">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✈️
Slipnet
slipnet-enc://AcwwsvYl4r7DajFRU6wa12enHS94jGWcw63dYwNxwSzZZDO03mNtFG6vROd+UO8opWIgDZkjjnUHlVvSaj/HvKW+p2HLBc4ETWvUWsMZpCwiUmAeEORd+qfA089iU7PBEHuvMqTIeRqwCA6OyylmfHRyIlB+dS4avIQQAJLxeW6G0ZMnp8HZ4VPpuiN2Vs3U7StRqxSwEP7f8wUXQy1DHgcCE9WD74CKd5RxaHADsaaT4Qj56xDB+DTB8l41JtvrbtjUVSNCS349vS8XyPhXi12t/YaAupzBKzSkPCXi8UjM8Ft2AyUuvLKTPgSMjJgI+vBT+16sztR9Q5n88GbrLNNWKD31CXYgjS4YNk8tLooUjYBgOKWmoBPVWCHej1RPyjs3lg64enMfTyX+WKjZ/fxrqH/8uGQZGj7qLjcGhGaohjHujN+ODCfxxAlK+6Y6eQFfld7UtXfyz9cTmhkk7mebn5exSrIv9o1auX6VVjUQ8xLMvhf6wwsD6vwQsblA6QeIvDoD8NUOfeKZFKrraoPjEdJexjOxcn9gbWSEM/QeqZB/lQ4LnfH6zHtP8PmH63PRZJTZUv6VlAovbrtWUp0ziB5fgISZTC4akBfBPTO32WXUTj+Wo1sSSeCH1rfVQAYoMqoQusLWWSHLm5Llfz5jW8qGwROFKxCq6HYzt4gLRZixvL44Dluxo+oyG14jHwsAmPVh05xydwjCI2XcpiJgX5De91xk+x39xMt7AwApPsraUbzuBscA/TU90Ehahp5NbRa0nr1Z44yGL0dC78sWZrPT5XtXbIE+Ydpd5qq3F1Y=
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/IranProxyV2/8331" target="_blank">📅 03:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8330">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره، دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول…</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8330" target="_blank">📅 03:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8329">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/IranProxyV2/8329" target="_blank">📅 23:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8328">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/8328" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8327">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سوال اینجاس اینا از بازی ها هم میترسن باز نمیکنن حداقل مردم حوصلشون سر نره
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8327" target="_blank">📅 23:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8326">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✈️
علی قلهکی، خبرنگار:
🔻
تا امروز بیش از ۴۹۰ هزار سیمکارت پرو فعال شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8326" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8325">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">💎
𝗩𝟮𝗿𝗮𝘆𝗡𝗚 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻 or MahsaNG ( Psiphon)
vless://799f939b-964b-4416-84ac-18a6ace7fe70@camp.nahidapp.com:443?path=%2FIF_VPN_Bot&security=tls&encryption=none&insecure=0&host=camp.nahidapp.com&type=ws&allowInsecure=0&sni=camp.nahidapp.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/IranProxyV2/8325" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8322">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOGoD2OY56plLp-KWLoDgPkqLOUrMGqb-SVE3yi5xe4wLdjA7SAtfsu5rZwiQtk5mbP9w3CxSQcNNRqGFxFl4nvg3QWWlSEA_iX4KJAYIzcKNnQffvxmUP3O2rncflkSti--TGznhFMPFR2LbXWWFJ7chIVorGGpeaC2gXH2oUT3OwjmWWRl8PqmosXytfMJAw_pVpn2Hj94b0kXlGDqOQym4oX605yyXlbn3-E-5o8uHk3xjlJ0MiUM8guiv_2sxuWliZEY8NuXes1Vh-X8vx3F1Qy_0IucosKKcJPZ0OHPz2f3G8qSw3I3F8X2R1OlBFIvPJtkXBgieo5ahbm0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
وعده پزشکیان بالاخره درباره اینترنت :
◀️
ارتباطات و اینترنت به بخش جدانشدنی زندگی مردم تبدیل شده
‼️
به آقای عارف ماموریت دادم با لحاظ حساسیت‌های حکمرانی، نظر رهبری و وعده‌ای که به مردم داده بودم، در قالب ساختاری چابک موجبات خدمت‌رسانی بهتر دولت و تحقق انتظارات عمومی رو فراهم کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8322" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8321">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8321" target="_blank">📅 20:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8320">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXpo1tOI_BPNODyGWiUB-1HDjJEGplX38dGOYgK4RW3R3UyyTzt5HW_lvZIiS2HyErrJSJldohmTUhqPJvH1oOn4tEacs0eI7Z7nzvulCVy76-jrQKHZ-J95_GAGBE0ZOTBeQLBTPKNLddIEtkv-Ptf9Q_jSHOBQ_YOHnGgDFqSWtEwebtAz5tO4bjfk_UZMCrwAMnXbHcGD93B-Z5yeLBz5q9h_LzZjt4BvKpY8vE6vqpckr9Fn9E9noBtPgXqSYxxbwz5VTeGpa8K9qJntXEWfX-4_spAKivlHa7re1WgnS_rQeOAuImYZcKuS9BLK9ZxCWSUlg_Vb0czHyifnUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت اینترنت پرو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/IranProxyV2/8320" target="_blank">📅 20:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8319">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8319" target="_blank">📅 18:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8318">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de826422e1.mp4?token=YEL49Q9_pj2g1V_X5V0RySILkthVaZLPLTcPugAaA9LtAjZ-1T32eNOqYCUJxhEnxLJ1ovBMujQT9TuuoFrXn1oKAr3Iux5e_V0p2L48U95rKZLDrP6s9n_Gr4nKgpzLUcdzdAKKGurvwmdQGzPG81FEIugXxkJmbKqPYm9ZeezBoRnY99cv4o6XILt8qvxqTpSATx7SIU23_2gjURn8lbdCnCM78C4wiplJr_x8DwfgTnB26WJaqb62U9SqzqavSJ8PFWiZJ-hQD52zNtnRsu-QpNKX1zaflZzogBqh93wastZwfVVNYIPQXBokLzJovg3vFywmLOixvzmaGWzgtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de826422e1.mp4?token=YEL49Q9_pj2g1V_X5V0RySILkthVaZLPLTcPugAaA9LtAjZ-1T32eNOqYCUJxhEnxLJ1ovBMujQT9TuuoFrXn1oKAr3Iux5e_V0p2L48U95rKZLDrP6s9n_Gr4nKgpzLUcdzdAKKGurvwmdQGzPG81FEIugXxkJmbKqPYm9ZeezBoRnY99cv4o6XILt8qvxqTpSATx7SIU23_2gjURn8lbdCnCM78C4wiplJr_x8DwfgTnB26WJaqb62U9SqzqavSJ8PFWiZJ-hQD52zNtnRsu-QpNKX1zaflZzogBqh93wastZwfVVNYIPQXBokLzJovg3vFywmLOixvzmaGWzgtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شهبازی مجری صداوسیما خطاب به مردم ایران:
اگه اینترنت 5G که افغانستان داره و مسترکارت که سوریه داره اینقد براتون مهمه؛ خب برین همون افغانستان و سوریه زندگی کنین!
﻿
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/IranProxyV2/8318" target="_blank">📅 16:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8317">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ایران اینترنت ندارد، روز هفتاد و چهارم …
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/IranProxyV2/8317" target="_blank">📅 13:58 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
