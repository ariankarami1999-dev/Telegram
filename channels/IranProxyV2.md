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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 17:31:58</div>
<hr>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 292 · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvstZCMnb3Lg6Xe5cHSl-dMcMwukDyea2pB99Xfgn63DUKtdQXUH_iAXIu5WdCMk3FbKBbeIwwC8ZQ7hsHgMW8TT1TZcdn0GG-1lMVwrHMzoE3mzA0RH5slvdZxTavC-VoB89t69CAKmgA75O2WILyiUabLXBT1gQvFvC6yEActbxoc4q6_VX6z01IRYmcBJ4Zo5qDdNV1N0oY2aeZMahQzIG-L_TNclCuAVONays3tCdyI6dveH78d0D1P9nR4PaUyayepyce95Znk7Y8Ihc6tvg0ab86J6RSlgWVWWsiCAkewfidIRKH-S-RQ8bC-07YIJQDN5GwYkWZmgPmdJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار داده شده و حجم مصرفیتون، حجم باقی مونده، مقدار دانلود و اپلود و تاریخ انقضا کانفیگتون مشخصه
2⃣
پایینتر لینک ۲ تا سرور با لوکیشن های متفاوت قرار داده شده ، خواهشا لینک هارو از جایی که vless نوشته تا جایی که vless بعدی گذاشته تا قبلش، سرور اولی کپی کنید و وارد v2rayNG یا هربرنامه ای که دوست داشتین بکنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jugvo_YcIRb8bKDeVzM1nxUEPa34JrjmphHrCyzoIroo9p52Zt3a6127inxdxEQmJihS5m6kTDWYDojNzrQd9Lb8cleZEiqxWscKdUctbozmCLjcB9ocNhdgRbzqmiYvoTdYEl_qV_S-9LMmghJj7TZPuHHSS9PBEu0N8jkbMxfKOk4r-RF7TCeJ-2nVOhFfl8vSF4BQM0YXg_4qB3K-3NE0BeABrV3tbNgj5V0pbFD1Bx5Ms9PQbu0BeNdLVe5O2U6pjMkU48E3ovAoSDhhYH7hiINfES-3XAiIyeCxP02hvBpaM_Te29n8DMiqI1V0bv1J3bt2fJFf7ZHa7WohJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpl8j352nYqzH5_d22Kl82n90O7A7vxeDgca5iut4_VuKI2jNR4FZSBrurQp_6FfaOTX_f-yToKVpbXpYLeA36u-F-cQuMoCALvpp0WArcMEZFiesYzqBuB0Ayo9n5W6PeZWuW6fZuH_-89BiyJUCuHdEZvO98ZaQPfiidAWWmVRconYaHbfqEn2pkfGQgIdm5DchuRDqnFQDmmBGzVgfXbfZZyQ_U5j0j9okjdoKTC_gBaFU1Vx9gWw6njmhPBjWYjaYMQ59l6zbtX598labNVd2bLZEWLtOpQlD37FTs5qTxoZlIz5jOA0f9kqgVxYYx7Hzk-RKkqADpTtqPs9pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=HzwdssDOEuxy1BDI4dQnTXZs-E_XuS-hBl9u-kyuSTMVGD3sB5IB8oK3xdnvfpay-2bYh_egMYAjS7FK2kd6aSpLC7rnmxSb6Aj91eRKI8MQRMwLgKRw_4CYWD4LGqcZTbdy1vvlV3H2S_WZzQcPaJQRuzXRTk0ydkbwLbNSZswElqDybejhA1plmXqO2q5dukjJ5xR2hjv2RrDIb6UmPcwd6tn3lMbVKEHzxD-6aK31C8QZYSYpUyB_3dBymzrj6-0js1s6xC-1gu4mm7ZG9-gmu_E13s0vN9ZVp_D71Wv7ZFVgU1p98qL_2mr7MW1Mzwr53aqZ4RFT2Q2DXNhL3RPjgJPDPGl-FzR7cn7deEwFU0-mJ2Rlg8N0RFBkCiK9Vlghi7Ot9rZKscfu5RbmoqXXQWsr9KkUgPayJJqSL0at9HXSfiXSrG4jPm0VOG5l2TTGwGTzZtZVQZvV2Xf_i9XcieaRqvdCm561WVmq_-LUqASIdnbfWUi4pQYucSJdKgl5FCaqcxciOPkAYpIfXQLu3mw8d4sGZ_gwPP7leX4y6CGRCWe5wzLDfNvCMFtyDx9nu6KqYkiueWVfiP7P1yGAb2T7RYui-cnmixXUT9q2xkGyi4tvXSBznPaNTg4PQ83pjVa1wI7qNl2iD9YnbEbZZmlFH03WuuEpSKWPGBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=HzwdssDOEuxy1BDI4dQnTXZs-E_XuS-hBl9u-kyuSTMVGD3sB5IB8oK3xdnvfpay-2bYh_egMYAjS7FK2kd6aSpLC7rnmxSb6Aj91eRKI8MQRMwLgKRw_4CYWD4LGqcZTbdy1vvlV3H2S_WZzQcPaJQRuzXRTk0ydkbwLbNSZswElqDybejhA1plmXqO2q5dukjJ5xR2hjv2RrDIb6UmPcwd6tn3lMbVKEHzxD-6aK31C8QZYSYpUyB_3dBymzrj6-0js1s6xC-1gu4mm7ZG9-gmu_E13s0vN9ZVp_D71Wv7ZFVgU1p98qL_2mr7MW1Mzwr53aqZ4RFT2Q2DXNhL3RPjgJPDPGl-FzR7cn7deEwFU0-mJ2Rlg8N0RFBkCiK9Vlghi7Ot9rZKscfu5RbmoqXXQWsr9KkUgPayJJqSL0at9HXSfiXSrG4jPm0VOG5l2TTGwGTzZtZVQZvV2Xf_i9XcieaRqvdCm561WVmq_-LUqASIdnbfWUi4pQYucSJdKgl5FCaqcxciOPkAYpIfXQLu3mw8d4sGZ_gwPP7leX4y6CGRCWe5wzLDfNvCMFtyDx9nu6KqYkiueWVfiP7P1yGAb2T7RYui-cnmixXUT9q2xkGyi4tvXSBznPaNTg4PQ83pjVa1wI7qNl2iD9YnbEbZZmlFH03WuuEpSKWPGBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
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
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=WNDDcsdpFpf86QtxLDuJjnDqdndxKGSr-RR80HMwswjGMF3d9MeyCwyEC9GJJUA1iToC6btj64Wd9msUdi_UiXjHn_IO15eRCPeh0ZqfBUpWBUpHPTE2bKCUjo1m82WGN0RFls2Kk_tLyCiRtyv5Y_Agre23n4O9pHQROzGslWuSXKO-Y2zzRNbXe8O9j_sLKMF42ulYj4G_Dz2KNHTVoN6p0LboJkkj5Qk3V9fdOUjt4ss5uLbCOH83mq51F_HwdmLzeBF39Zp_QFBcjk7dklXpIhnZr80tDXGGB3W4JM4WDrTqDnjHJOJv_P-kRxq0n1GbpbCJzwa11jtY0aQriQjKyNrrJEXgPmNAfU_t359pgvZSdh-MWX2GWGDWa4TZ0NagzPGfesh44I_f65f6CG1INXGjS5PGeAYXlYosQu_FO9FwjZ9k84Lcs0rZWl5jkM79d60gBRD6ddKFGxNFjBKG-R019Vz11NM8R1G6FXW4yv-Au2GfIDjU97TqFaqPcuOUFilJSHbGUeYwLN7IGTvQv80gl0dKrKIxld5Z1nB0h8Yn9uPpUduJ5WdeJzcIVnNpkUH93EH22eayxw9Qtyp_QGEWh9II53BZaFebcUb5D4pVXt2oqUG8lfbVK4Hn69FoSIb7_hzdoWNvnB92WkzUGfG7brR7MS7G1pJAHNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=WNDDcsdpFpf86QtxLDuJjnDqdndxKGSr-RR80HMwswjGMF3d9MeyCwyEC9GJJUA1iToC6btj64Wd9msUdi_UiXjHn_IO15eRCPeh0ZqfBUpWBUpHPTE2bKCUjo1m82WGN0RFls2Kk_tLyCiRtyv5Y_Agre23n4O9pHQROzGslWuSXKO-Y2zzRNbXe8O9j_sLKMF42ulYj4G_Dz2KNHTVoN6p0LboJkkj5Qk3V9fdOUjt4ss5uLbCOH83mq51F_HwdmLzeBF39Zp_QFBcjk7dklXpIhnZr80tDXGGB3W4JM4WDrTqDnjHJOJv_P-kRxq0n1GbpbCJzwa11jtY0aQriQjKyNrrJEXgPmNAfU_t359pgvZSdh-MWX2GWGDWa4TZ0NagzPGfesh44I_f65f6CG1INXGjS5PGeAYXlYosQu_FO9FwjZ9k84Lcs0rZWl5jkM79d60gBRD6ddKFGxNFjBKG-R019Vz11NM8R1G6FXW4yv-Au2GfIDjU97TqFaqPcuOUFilJSHbGUeYwLN7IGTvQv80gl0dKrKIxld5Z1nB0h8Yn9uPpUduJ5WdeJzcIVnNpkUH93EH22eayxw9Qtyp_QGEWh9II53BZaFebcUb5D4pVXt2oqUG8lfbVK4Hn69FoSIb7_hzdoWNvnB92WkzUGfG7brR7MS7G1pJAHNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDo0_4rXcnPNIU0y4FwidVobqjbIJVM4ay9RJ1DPlBRTfS1xLq2Zb0BQsGWgyurn-25Vm96Pw3F1cUUrPOYVVd82wO-_JZh6NhS2idVvGDfnT2rqhryMNMqjI2LQScwgNDyYtC0pQaoeWRqOVPtmZjrA6ZEGalviMNGJ2sWBY30UbimewxgEgOYVT5-IUEYnueZ8cN82ryBXV-6DcFnCEfMXRWCxXCgGyTJbujjHDZyM2AaTh31EJAC9B3Uuap-xKAVkGNPmOn1EVGC2kvzjOqWMW3SavbyXb-LK-ePwnvtJmSHH2J_i0NiTcbd_z53pnaQpZvzNGW8nrHfg4TEdmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=seTlMZVI1e0_sktLGl2YYCj38jifQ1GZAH2aCPY360Ooiofj4aVPTQPwhPrwwCjo1W7y7mzhwT6kyWYTHeOuy9RvCq6FFYcbAIGpnplwdCfX6HUdxHaZWKddeG3Kn9RpQtAvcl7l_-JG73Ln9sLDFXsJfHk7Kg6nImZENzrJP0KfkLiFXeswUxrwtx7WTIoPob-OnFVTdO4sD1rT-N0eeClDzqtS_pnY5bdsd5jY7B0hxOJ6XXsT8bKT02vvy_EWA84WRmpjKwe8QBepcJBB3j85jtx0ereZolJcNJEvAkEMtEx7xagJSLo_BqsslLJQxXHWV8MDpgdTVioCGnWIsho9hgy1xq8CTAhJAmLonjzT6qDV9mdPfvRM5pAXxR0HDBpjwol6wc6WtYBkZ8mjqvZCYIOBhP-WauHnAm0rN8aOfe10WOdyheR7tz0nhbi0YJvG_BNFByfagVK53_DTz9Qxc0xzZOPX57QyzE7bQqurgDyWQ1rFFc7FTD_JMWT3ukctgI1E93WEoYj0-Pfn5W1BnbNbVAdLVs560Ory8K5irRqqMiv9N1OyRZsOLqIPma0PoMpEr5GGMZ5dbCeuDRHNOAYdnGDMxqYAPFGEdSYhlqpEuZSvBU9d9tUDjL-q3F-nypWYT8oVepMsYNo2nnEx2QAhSOPxb-iUZ5jljD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=seTlMZVI1e0_sktLGl2YYCj38jifQ1GZAH2aCPY360Ooiofj4aVPTQPwhPrwwCjo1W7y7mzhwT6kyWYTHeOuy9RvCq6FFYcbAIGpnplwdCfX6HUdxHaZWKddeG3Kn9RpQtAvcl7l_-JG73Ln9sLDFXsJfHk7Kg6nImZENzrJP0KfkLiFXeswUxrwtx7WTIoPob-OnFVTdO4sD1rT-N0eeClDzqtS_pnY5bdsd5jY7B0hxOJ6XXsT8bKT02vvy_EWA84WRmpjKwe8QBepcJBB3j85jtx0ereZolJcNJEvAkEMtEx7xagJSLo_BqsslLJQxXHWV8MDpgdTVioCGnWIsho9hgy1xq8CTAhJAmLonjzT6qDV9mdPfvRM5pAXxR0HDBpjwol6wc6WtYBkZ8mjqvZCYIOBhP-WauHnAm0rN8aOfe10WOdyheR7tz0nhbi0YJvG_BNFByfagVK53_DTz9Qxc0xzZOPX57QyzE7bQqurgDyWQ1rFFc7FTD_JMWT3ukctgI1E93WEoYj0-Pfn5W1BnbNbVAdLVs560Ory8K5irRqqMiv9N1OyRZsOLqIPma0PoMpEr5GGMZ5dbCeuDRHNOAYdnGDMxqYAPFGEdSYhlqpEuZSvBU9d9tUDjL-q3F-nypWYT8oVepMsYNo2nnEx2QAhSOPxb-iUZ5jljD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z69iOoPtACPkidNRD6SJyeT8ImcRGQ1vXYkvHstS5dxQS7uowT7gT8epQe08k1iNeB_s4CmfDTJWqVBYCCzqVWlXGeIXGXcXTgXUawtlQTBS3Yr8Owbk5anoJIWKe6UrrxcQW1y2bevW3Kk8suJO7731GhjJM3ES13TEJEOKYfXzqd4d8yavm1ixF2A9q4DeIsd4N0lfb3SWZmvivwwIldF3sVcQ_lRuzgTYObruV85BTqsrnLyuyzh7RvBGIxkI7AE_q924SiBOrc_PfFECeeNdgGw-y-iYnSGjENl1OWySPAB0PJYYDafVv0ejNDEseJ9_5ZZDUbw0lp3ue8Z5IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJLoQ5MiBmBVvfBp2gVZRRbAHtxwq8qXTUlnJeLWxDriazjYwHjk4Bky-2hdppK7x-VILBsazqQxmi6HPKK6NZ5Y8RAq5Tgxo9wF_JK_FJWfTnZ36hLTRmEwi_imrtwhFx4uBxpOodlB0M4XiHTYB99fEIwfowRUiRD0TIaZzbmg3BUHUpyKX8Td7Sgowgwo2L0s0Co3Lboi33iknOWxpzUJaQoary1qbZeFAxIXjtd0sQofLI2Z6G4Y-xGTy5t1UKKl5oXV8QQknmtuCTj60ZAM71uow6EN8L1OhZQ_h_OND7hTBWzqKyQZNiW74UoKvHjsA7gyekvAmMmZlCIdHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=ewcGJct_J6bD9tERGdm7Ik2k9HakksagWYdILOY0QLUHR6_OwFmcdJATsJXqlUvm8c8yWPNsoazmhL4qy4PfNFYCxOdcJn8-iEBbC4ndK04h7s8lxrzaCJUTBKmosy3sGnwRkZkqr7gn45kfMiv3W0v6bRbRLFhQ_xNyx8vM-5rTAJPl_H3c357TGJNCAfuoacPFJ1bUeo5dB4fA63zodxLF7Qn0F_KGUj9cIQIEvzt6sKCdIJV6JD2VJN5DaiQTG1Nx0MxFeqRaroZf5pm7Y1o-TlNYCkM7naNz5B_7JtnZrEWq6yBfy-qDifZ3DhUmQ1cuLWY58K3YRzqeyHaMKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=ewcGJct_J6bD9tERGdm7Ik2k9HakksagWYdILOY0QLUHR6_OwFmcdJATsJXqlUvm8c8yWPNsoazmhL4qy4PfNFYCxOdcJn8-iEBbC4ndK04h7s8lxrzaCJUTBKmosy3sGnwRkZkqr7gn45kfMiv3W0v6bRbRLFhQ_xNyx8vM-5rTAJPl_H3c357TGJNCAfuoacPFJ1bUeo5dB4fA63zodxLF7Qn0F_KGUj9cIQIEvzt6sKCdIJV6JD2VJN5DaiQTG1Nx0MxFeqRaroZf5pm7Y1o-TlNYCkM7naNz5B_7JtnZrEWq6yBfy-qDifZ3DhUmQ1cuLWY58K3YRzqeyHaMKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oASMuGhugE_tsOjVdJK0KbrkKF8am96BHqa9pcN3w5fnnA0V57Tx9sZrnRzB5-8DmrXkQGLMMx57dIzzK8_NS_NUdkmNbGf2oIaYOapc8j0V6nna9rx6YQH6FXFLYgfLJQiiQckmVSiHcAaTMqMya8WkZyVnt2J2c6lwEMVSbKxwptIOMoQmzOYf75O-3gGa0OXRNMCZX8UcaIVR_KE33DaCPRuhGQV_K6thjKjTJW9GNdUbzeRUisqO73UIh5Y3Czu144w5W0LIhkcwI43QBOai-vSJqB9RyXNBvinUORchJV8Lt3fTmcuq0iTPlRewyabdplliOOCgtMpKX0Njmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbnrDzMXyfPAhZMISBtKXeCZt81HLIN9NiVFw3KIG1jX1HglgCWeJebWbp1-eYEL60WKKbq-sqL9-LX33Fqv_g2nuL6T8v16uduRCSscVC6rca0lq7tNuYMF5Rml0wwkFzjWumBtw3qEHRVMyj48hMI7FeRErdgnGUzbdvD8SOFui6aVaXFS3Ac5-VE4ZPQ45r0pWxDI23jbTeLa461Tver6g2ir74XXGcpdBH2kj0zRMiusr3lFnRD8y6KnMwxe6cvh-i772-TxT8QZJbHTantfeYN5D5I0eXL9YSOvh338s021lONUZEPQOd-cCf-phuEgw6H9Wx-dlHVJ14doZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E70ReEgNfjbUulguYpsMd0efILdzCpv7aC74hBsILHV-esrVjGjnfD6MkKw0vDLiF6S7VnLyitNG9Tr1TjxmJ4p2UJgw_-saKMipDDacAiSVZwhGUzSFpp3IewZFCpBzkL5jM7JbnivZw2p9964XfXsthT-VSgrdgJy7_o9AjhTm46Ixaz66ut1vI8T6vXsC5mfMtwlDVc5LD_y81JvfhR1g_wXlvij7_X9Y_UdhhHdJ2PFdgYHq7pGLpEZ4ZZOb0BwPReVTy0MsrSqOWRTlgqCNUi02qALnNOm_zPznCE3Z3-Z_bTn60PDMojsi7cwtFkpMUJ6dmON1JmgN4q1diA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=Wnj4ZBWaGuB5_k_bXzP-j8XIxaBR6JhEbBMu_ryar7Pwt8v06rKgbiajLSJUm9zz48ZSj1NoNcVL6iXDFy8Bjy3d_QmYaetmdoFyO7Ar246pkMsmV7SXDENaouUfPyAh641lUqDu7BduSyKI15sKqqT8FfEV2az5umnUTR3Mk0uOkiw9OHGCfoyI89uMb-gBw0zIm3yeNWUkB-uYMZ1g6kcrjclzWpQJe2W2oqdVL_5zoa61bDBmpBK9Klph-R2lYN7gZk8H9e0xFyhWFVuAqm7RW5TFIsT3lqCguafbQ9nhs2PA68VUnJUOTupzQxQye0HSuPchbkuOBkbOXpOkbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=Wnj4ZBWaGuB5_k_bXzP-j8XIxaBR6JhEbBMu_ryar7Pwt8v06rKgbiajLSJUm9zz48ZSj1NoNcVL6iXDFy8Bjy3d_QmYaetmdoFyO7Ar246pkMsmV7SXDENaouUfPyAh641lUqDu7BduSyKI15sKqqT8FfEV2az5umnUTR3Mk0uOkiw9OHGCfoyI89uMb-gBw0zIm3yeNWUkB-uYMZ1g6kcrjclzWpQJe2W2oqdVL_5zoa61bDBmpBK9Klph-R2lYN7gZk8H9e0xFyhWFVuAqm7RW5TFIsT3lqCguafbQ9nhs2PA68VUnJUOTupzQxQye0HSuPchbkuOBkbOXpOkbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=FJ58AQvHQPm0Z6T8TjZXWYUma6qTUK1AiABNPvICpmobXLDnMB0sMaXvH0e0Okdq1NQgd6uluMU-YdjNzGitINvf0h5FGS7ZnXTub8Z0eTSTS1Urg6TE2qKPGybAal4O2HQ02_-ssJj3jACiEL6vxS7SmcHItQuNhQXENE2Hj7_idgU64XaeLY0LEkdOqxNqNk_8YnRcUxXXU1DwCGflQRs7X7OTwMKkkuxmHFxyREfyAsBg5CJA3kNXIapO-CwdFXI6yiX8sYlIvhsrmhvXkkzzIFJQW_clXRfDXWyc39HPXispkEbmjahkc_tsaSFu8BqBqvA4qssysp-pyNtCCQf0EXNP4lnrTzt0uzyRwmuX9YmptrYbkLSrABRVU-kegFXeLVqC7_hfyNhNqIWiMVb4duwuNET9_KVUpRDPpYGuL7W5nAN1f-oZv7oprfRqZj-06U7dJKLidznNI9yUGrcnPXznb3QNfxrBLW1VX40pV2Lt1rpwuE6yi4uzuejXnqdWik93-ZgDqZXy2Cv7n98t2ZOGgCqJJHI6OoGs-TjRuNHkTVhLoMtlQ6x0EsEUMLI54hLX-vbIarW9U1qWy3tESkrc8LY5wx8w1_nT1UnjIsU7r5X6GbcuWTPgFXQi1dmq7_MzJy2GPLXnAM-qcfYc1dWbAGoUNAhkmIXa2ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=FJ58AQvHQPm0Z6T8TjZXWYUma6qTUK1AiABNPvICpmobXLDnMB0sMaXvH0e0Okdq1NQgd6uluMU-YdjNzGitINvf0h5FGS7ZnXTub8Z0eTSTS1Urg6TE2qKPGybAal4O2HQ02_-ssJj3jACiEL6vxS7SmcHItQuNhQXENE2Hj7_idgU64XaeLY0LEkdOqxNqNk_8YnRcUxXXU1DwCGflQRs7X7OTwMKkkuxmHFxyREfyAsBg5CJA3kNXIapO-CwdFXI6yiX8sYlIvhsrmhvXkkzzIFJQW_clXRfDXWyc39HPXispkEbmjahkc_tsaSFu8BqBqvA4qssysp-pyNtCCQf0EXNP4lnrTzt0uzyRwmuX9YmptrYbkLSrABRVU-kegFXeLVqC7_hfyNhNqIWiMVb4duwuNET9_KVUpRDPpYGuL7W5nAN1f-oZv7oprfRqZj-06U7dJKLidznNI9yUGrcnPXznb3QNfxrBLW1VX40pV2Lt1rpwuE6yi4uzuejXnqdWik93-ZgDqZXy2Cv7n98t2ZOGgCqJJHI6OoGs-TjRuNHkTVhLoMtlQ6x0EsEUMLI54hLX-vbIarW9U1qWy3tESkrc8LY5wx8w1_nT1UnjIsU7r5X6GbcuWTPgFXQi1dmq7_MzJy2GPLXnAM-qcfYc1dWbAGoUNAhkmIXa2ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT6NBqKm1FObb9F2bC5VXhD0p5Ly71LWCNs-JwPKHnCmFNXnaruahZCKKuonFaPzguI7gV974L0bjTg_vv5QlmKukDrqzdnvcE6gVeMKgOS_SxOu_0bHQdcjCNb9WEpURXn92IyGRSLSbpqZiczvoUNKhSS0T6NpSOr3JXrQXYZm1iPeIfpdbuRIInWJ6ZmF4GvlWSaP33yq4GMsOgA16WUQcVfC5Pnkb0a1eBRJnhkNh1HQ3dBpWG4oiASasqONqtcKGEKDPv4tbZp3V1fpSDjrQGcstHY6P17O_uMqnf54G-4mv2vDJWzfNbfiGfyDLksa4fsQ69LZADaL_eB0nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJOmG9rzubkf3vTpkKk8-rpmqxndw29UXuQBccyusZWa1BjOYx0g5VHAmkhGa5GVi_R4HQKkSMjTrv0StxYqhaZgZyvwyme7bFaNiZvvqe5mMr75LIpWNDiRulNjZxQSVydxfx6Npw2-s4S9ooFhPFnVvhknVnS1o8VO2nNNHFyV2Gy0ICixd6CnHQKh3EXdJCdQyVgHaMZzDFgOyUBTAOQvhnGRkxagtP-KghZciWE2evzIm7ZOOE_VZwcrRahZwDrrL8sDENio7mOBj5mfvrLBRbDFpKq7j6w6FGeor0PrwOU80P1eI-R_jAxjpHZu2-zcpbV2m8ODg8Sx9vqjDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X5ApIOg4DvE20Zgvax9gJPJGDxMwxOrc19k3KByvcjc6MV6-ak4Ku-cuImy1H_c0j0Wu6rRDuBhhhVFcvJZ4UcoAExBVe5P0upfijmyfaQOl48Uj2pa0QYjezs7QXkKix7o87Eini3Tl-yzKIYeWHsHZy5mHlYY9N58WdiUOoyS--CS_xXufMjrGleiGZeuLGXmSJXS5hTFQwGzaGM23rANs9GCiCtrMYVi4WwGnPHjIFABL_yWo0Ex3DBfXpH-PqkVJkAT6F_tuyzzNNXm90GWVmL3l_az1vxXs2PPHhjpFZHqoyU6liUENOJcnIBauwTaIAmsXcymPOqDtfzf-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=udfcQwHd0ZxW8DalmfDO_-UAVF_0-Pai-BoISLeyX-KQtAV_m6t5dMRSuxEkYFTjIZqLIig4gw992rFqQmWS8Tcb6tmHdR57qdGWpWQls87kHKfcpTfUeVh58PEcZUy9WGgbyRHTas8CONuXcGWNQbdHCDqgVQ4Wjc9zEj6ll1cDzXNK_X38kxeLCedAE5A6lIaZsgzjBoK8cs4n7NKYNLEDBzjBSh_sPyYamCM0nWvL4-yDdjAxZzKw4ASuZXb0KnjdRBlp-9ZUju5UIjy4eLL5KPln4Nl2pQHoUB9kJ-b8yaCjkINuiaLxISP0P6jb2buqWv1Oze3Trohq9SwOBXrl_P9BgaGMyMGoq3Np5MZQVrrOrFk5Tkw0mxEs8949Iq2s_ZcSgtPu6dqyy2_bfCrAYO6MH9gkE6jCPNX6C9uOyjNplj0y2yjXsmWFMOuvs7tJng_w9aJi-MqvZncTTy8akFuSPjNubo5CmhgUV6e4RT5Ll37oJVG0mFxNaEuEQerWsNIU2Iy6LgqzMPvyb-DNxWKiJ6egjsLcXav5dN3tUwApOLW-jo-OMrr5hh1mZZ4O0i8_tRR2-cM51cg9g2oRkgyonnIGjYggRxEybUIY7XVoGMJnUwh9hh5lK4XOxwC-ckruhK4A9AFTH5ANZfr6fRgLq2jxb2ghMlM3IaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=udfcQwHd0ZxW8DalmfDO_-UAVF_0-Pai-BoISLeyX-KQtAV_m6t5dMRSuxEkYFTjIZqLIig4gw992rFqQmWS8Tcb6tmHdR57qdGWpWQls87kHKfcpTfUeVh58PEcZUy9WGgbyRHTas8CONuXcGWNQbdHCDqgVQ4Wjc9zEj6ll1cDzXNK_X38kxeLCedAE5A6lIaZsgzjBoK8cs4n7NKYNLEDBzjBSh_sPyYamCM0nWvL4-yDdjAxZzKw4ASuZXb0KnjdRBlp-9ZUju5UIjy4eLL5KPln4Nl2pQHoUB9kJ-b8yaCjkINuiaLxISP0P6jb2buqWv1Oze3Trohq9SwOBXrl_P9BgaGMyMGoq3Np5MZQVrrOrFk5Tkw0mxEs8949Iq2s_ZcSgtPu6dqyy2_bfCrAYO6MH9gkE6jCPNX6C9uOyjNplj0y2yjXsmWFMOuvs7tJng_w9aJi-MqvZncTTy8akFuSPjNubo5CmhgUV6e4RT5Ll37oJVG0mFxNaEuEQerWsNIU2Iy6LgqzMPvyb-DNxWKiJ6egjsLcXav5dN3tUwApOLW-jo-OMrr5hh1mZZ4O0i8_tRR2-cM51cg9g2oRkgyonnIGjYggRxEybUIY7XVoGMJnUwh9hh5lK4XOxwC-ckruhK4A9AFTH5ANZfr6fRgLq2jxb2ghMlM3IaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBjpX9yw_gLOUWNzxy4MTR0BBJ0L-LYxj2aR6DRvKeKtisplh8CPWPQjFuyBT5zU2w1TZM5qLeSLf0LtgmaQnyIWivxnFkRP_GHENE0P2_GRqvvDRzjFZWWWHFKWXZBzxJ_XUty9HDWmytcL01tNlBdKtuS-W75NlavAlBOK1ukWqJwZ_LTNlNsxyyoYV5C0nV6KZrBnWBsGq_Q3hbzIwKxQWut6AxQlEkyhQ2_IdJKtigIkbHSWCfAEokTvtmx3Le2gtDSFM68xFqc8wVBnFIh2BmnnnlYf5a0BH4nzZ00FStErBN6d-i_CFSZWgZZ17py20QXcpJP6ioG3ZKmWrhvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBjpX9yw_gLOUWNzxy4MTR0BBJ0L-LYxj2aR6DRvKeKtisplh8CPWPQjFuyBT5zU2w1TZM5qLeSLf0LtgmaQnyIWivxnFkRP_GHENE0P2_GRqvvDRzjFZWWWHFKWXZBzxJ_XUty9HDWmytcL01tNlBdKtuS-W75NlavAlBOK1ukWqJwZ_LTNlNsxyyoYV5C0nV6KZrBnWBsGq_Q3hbzIwKxQWut6AxQlEkyhQ2_IdJKtigIkbHSWCfAEokTvtmx3Le2gtDSFM68xFqc8wVBnFIh2BmnnnlYf5a0BH4nzZ00FStErBN6d-i_CFSZWgZZ17py20QXcpJP6ioG3ZKmWrhvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oT0MHrluTEhAOZOVqtODpy8IUB2ig44df5oRpCpkfCtyARHEGP5-RCVLL2OFrn-TIjL2SBvsFXDLifOn9fv2M7PNv0R98Rya2yPQnMgYwPNzVmwFfsUxkp1M5K9Nim5ehGZn5ua2rKEGn_m95ca1cfikPLdCS5z6LPZ8qKyRPYZISWwpco78115lHmt8ro4DDy4HUoqNmU_Alx_wANUWAXAW5862ohxrxMNv3kP7lF3Bof96bt1sdur9d6B0OboPjMnHNVWtYdfNWMzoQMTqjV_mejslnCfIj_P7RNlmm0THZ5HWi6YgOQ1NbvsFoJz0rFZpztKSdNd9KD0WV82PBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
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
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
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
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_iABSulQ6Dnd6vB6nmW1a_IBjIh2RaDKW0SEP5X0d9sra5LZA_lymSSVLioyQDcwwTqYKTIZqwBpoA4Dtbdu-4bn3YzvjZzPg_FnWeVXzFYZepbhuyy7r0b1JBc70FYwAvuTp9Y5Ek1aZU5Y4pwAcD7lyeORwJ-xhJFsQwQ8eK36B4WYMTg9lVdPXacPbNxbSj4jSbmXqpmmJuf0GHTaKB1m5KXHWbFtrAWUwu3d9U45pPdx9e33d_AVy2bo4IWxnm1ELSTZ-LwvMhUtIkCn811_caFTaDRXcYobRvVuh64_DM0UztCBId8jiWXfFj7s527NdnyokbWpEKVsNInig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=XQgrOoHVsCnQLw1ySPV5DaQTOiCJtyVSCpkUl2DrO_7HyXtRWPFBgYiVSAKWbdZ96Fafg9T0I3HMTzeMG4FXhhU2chjiSHRYkrdEuTz6Kx7qWQ1gB9BE_ed1fT8TMGXjx0F64_YLsNTVRayLbq50xDl_r298TVbj2OybJUQVFO2yNMVRhph19i6Q7P5coDbXr61hLdfDoY-hL8eIM_Pmn9hbNVRAh_CcGOSJzxWN368y5wFtvqiQ5FZx1YPlks24pJ8ew7_qZgHDX_buOeGcDZ2p7fh1Mx9XgiYj_z2eG5sB5zRF97jWpILTpGXM34F7e_kjO_Y78rIxNLhaIl1E_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=XQgrOoHVsCnQLw1ySPV5DaQTOiCJtyVSCpkUl2DrO_7HyXtRWPFBgYiVSAKWbdZ96Fafg9T0I3HMTzeMG4FXhhU2chjiSHRYkrdEuTz6Kx7qWQ1gB9BE_ed1fT8TMGXjx0F64_YLsNTVRayLbq50xDl_r298TVbj2OybJUQVFO2yNMVRhph19i6Q7P5coDbXr61hLdfDoY-hL8eIM_Pmn9hbNVRAh_CcGOSJzxWN368y5wFtvqiQ5FZx1YPlks24pJ8ew7_qZgHDX_buOeGcDZ2p7fh1Mx9XgiYj_z2eG5sB5zRF97jWpILTpGXM34F7e_kjO_Y78rIxNLhaIl1E_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینک از وضعیت سرعت کانفیگ ها که بخاین تبدیل کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8343">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">محمدرضا عارف از سوی مسعود پزشکیان به‌عنوان رییس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/IranProxyV2/8343" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8342">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن
ایدی ادمین
@RUSSIAPROXYY_Admin</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8342" target="_blank">📅 19:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8341">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کانفیگ های پروکسیو یه تست بزنید مستقیم وصل بشید بدونه هیچ پروکسی بیایید تل ببنید بالا میاره و اینکه احتمالا ۲.۳ روز دیگ کانفیگ هاتون کلا عوض کنیم  یه تست بزنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/8341" target="_blank">📅 18:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8339">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rs--j-zZhhW7hnB8lQ-zVz7JiMc6nZlQHDJd_DI3LK9UF1lkaz3Nv3iWvPfKqabDv12ugGZ1lcHDixj9NIVQ05t7HYRkHF8mpU8Ll3aIceICF5Evphr5RRidpTFAs3itbdozaKgOthUh4XZMIUmsFrY21hcS7z4cvhBvNcr1oAQNyOwpBGsxH4jDUqxF_AxyTB8ZK3MVqlepWYTvzwK4cA6vkxs-VXJwbzaOdv8E_VSuMwQO4gNBIQGkYPWrogN6s8P5AnhSgq9oIcY3fVE_X2FX1AdBgG9yzisR4sY9sQ3sPbIR9QrhSxJP3q8xt6vOHVfg409how8P9tBx-QhlaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
خدایا شکرت؛ دیروز اپل به صورت رسمی اولین نمایندگی خودشو در افغانستان افتتاح کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8339" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8338">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران: اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/IranProxyV2/8338" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8337">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/IranProxyV2/8337" target="_blank">📅 13:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8336">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دوستانی که تو ربات ثبت سفارش انجام دادند، صبور باشین پلن های یک گیگ و دو گیگ و سه گیگ موجودی کانفیگ تموم کردیم، فعلا فقط ۵ گیگ هست، باز مجدد شارژ میکنم تا چنددقیقه دیگه و رسیداتونم تایید میکنم
❤️
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8336" target="_blank">📅 11:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8334">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCDLmtEb6mG3yG4UYz1Wpat-FokDMmt5BU3yHbMoLJJCIoXxAtW7meL3TKchYPNm48NMy5Jg0746-WhKdQuF1bExzluxZv8T2YbdQx_lZuKiBnzbiPpwGfOyUhE5s8o2uWV_jJO2_Fft4gAHV6IB4BiPjpf0SetGKYkRYkqkFxYrWWhHS-RSgE00B50I2asdBmtBr7218l8xOwwsnt5NlqawMLJAVhDTzo6jX56QnKwdPFn9l5B5BQlPcTVO60frGeL6m3IDDPVnUw8WeHRVbIY5x1aPOfx3iZbeztodwUSgEpUXwn17sEIJSsScwmVqoSMMbnhrZUuzD75Kugeo_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CF6s2eKjSEu_fRsdbR1zOvkhmzPwgftUAbzbdae4GJjRMuKj7uVxCvId2uX4mjKlwu1YC7JqDWKQw0OyQqi1WDEhGipdMrumx7Q_mpwF8nvNc5A7j2EUsTP2xXr2njZIoS_Wy5Y7V0HCYVVmLfHW1RxYHyYRakvLOHIphdFJCoYQUbF-zzvR-WKeUhF03A2oTwinYbP13Xm-IfEbHSeCozY4gbxst0uIolLLZeuaxAnnGu_mW3oN3pOlHXoDu74k3mhURwe9TEJKbkn5Z4wF2QIcB2eQBR9fGaH5RyyGN6uUJpxLM7vOyHI-wGKRvKX2OpO9HOSfSv8GCr_LnL8PVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صنف کفاشان و اغذیه فروشان هم شامل دریافت اینترنت پرو شدن.
به‌زودی کل مردم ایران شامل اینترنت پرو میشن که دقیقا همون اینترنت قبل از جنگه فقط به جای گیگی ۵ هزار تومن باید گیگی ۴۰ هزار تومن پول بدید.
و فقط اونایی که توانشو دارن میتونن از این کالای لوکس بهره‌مند بشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/IranProxyV2/8334" target="_blank">📅 11:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8333">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/IranProxyV2/8333" target="_blank">📅 10:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8332">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✈️
Slipnet
slipnet-enc://AcwwsvYl4r7DajFRU6wa12enHS94jGWcw63dYwNxwSzZZDO03mNtFG6vROd+UO8opWIgDZkjjnUHlVvSaj/HvKW+p2HLBc4ETWvUWsMZpCwiUmAeEORd+qfA089iU7PBEHuvMqTIeRqwCA6OyylmfHRyIlB+dS4avIQQAJLxeW6G0ZMnp8HZ4VPpuiN2Vs3U7StRqxSwEP7f8wUXQy1DHgcCE9WD74CKd5RxaHADsaaT4Qj56xDB+DTB8l41JtvrbtjUVSNCS349vS8XyPhXi12t/YaAupzBKzSkPCXi8UjM8Ft2AyUuvLKTPgSMjJgI+vBT+16sztR9Q5n88GbrLNNWKD31CXYgjS4YNk8tLooUjYBgOKWmoBPVWCHej1RPyjs3lg64enMfTyX+WKjZ/fxrqH/8uGQZGj7qLjcGhGaohjHujN+ODCfxxAlK+6Y6eQFfld7UtXfyz9cTmhkk7mebn5exSrIv9o1auX6VVjUQ8xLMvhf6wwsD6vwQsblA6QeIvDoD8NUOfeKZFKrraoPjEdJexjOxcn9gbWSEM/QeqZB/lQ4LnfH6zHtP8PmH63PRZJTZUv6VlAovbrtWUp0ziB5fgISZTC4akBfBPTO32WXUTj+Wo1sSSeCH1rfVQAYoMqoQusLWWSHLm5Llfz5jW8qGwROFKxCq6HYzt4gLRZixvL44Dluxo+oyG14jHwsAmPVh05xydwjCI2XcpiJgX5De91xk+x39xMt7AwApPsraUbzuBscA/TU90Ehahp5NbRa0nr1Z44yGL0dC78sWZrPT5XtXbIE+Ydpd5qq3F1Y=
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8331" target="_blank">📅 03:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8330">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
اطلاعیه سرویس سرور های تلگرام
⚠️
به دلیل شرایط پیش امده و قطع سرویس های تلگرام توسط دیتاسنتر خارج سه راه برای برطرف کردن مشکلتون وجود داره، دقت داشته باشین که این مشکل فقط رو سرویس های تلگرام هست و سرویس های تانل تو ربات هیچگونه مشکلی ندارند.
1⃣
- روش اول…</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/IranProxyV2/8330" target="_blank">📅 03:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8329">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8329" target="_blank">📅 23:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8328">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
تهران زلزله اومده (دارین چه گوهی میخورین؟)
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/8328" target="_blank">📅 23:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8327">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سوال اینجاس اینا از بازی ها هم میترسن باز نمیکنن حداقل مردم حوصلشون سر نره
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/IranProxyV2/8327" target="_blank">📅 23:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8326">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✈️
علی قلهکی، خبرنگار:
🔻
تا امروز بیش از ۴۹۰ هزار سیمکارت پرو فعال شده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8326" target="_blank">📅 22:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8325">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">💎
𝗩𝟮𝗿𝗮𝘆𝗡𝗚 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻 or MahsaNG ( Psiphon)
vless://799f939b-964b-4416-84ac-18a6ace7fe70@camp.nahidapp.com:443?path=%2FIF_VPN_Bot&security=tls&encryption=none&insecure=0&host=camp.nahidapp.com&type=ws&allowInsecure=0&sni=camp.nahidapp.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/IranProxyV2/8325" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8322">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ6_x4Jx_fXd3UD2zGcQ7CCj5lET5XJFezCNLsioOf3ILfSdRIdTXmjt00Cw1c9NljQFTcJVpGwiO3sksG-9pHUKeYTtd36W2QycyCS0jcZqPhXP9-SwsTPKxy7Wrju345sCi5EriSrr9SGcNaSnRCBQgFTi4o9Ff4l4P5AFKz4XGo6lKiPG04umHeXAuftQyLn9NEz3PnziRL18dAYm6dMtTlCwX_zBZzz9i8j-5lNumhuS2rci7fFJOCeF2cn8F-Xf7pcvy6nwmkBigw8eIh-0Cu4n-TisddnymA5MJQNAXUpUL8ot-wsYoLB9IfzzJJwoqq_896ZHNjD9OMQJJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
وعده پزشکیان بالاخره درباره اینترنت :
◀️
ارتباطات و اینترنت به بخش جدانشدنی زندگی مردم تبدیل شده
‼️
به آقای عارف ماموریت دادم با لحاظ حساسیت‌های حکمرانی، نظر رهبری و وعده‌ای که به مردم داده بودم، در قالب ساختاری چابک موجبات خدمت‌رسانی بهتر دولت و تحقق انتظارات عمومی رو فراهم کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/IranProxyV2/8322" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8321">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/IranProxyV2/8321" target="_blank">📅 20:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8320">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHHieqvyMr-6tmmTTMKRDYCbrpiS8vVvhNlLf8JmACZpvXUN-6zCYxAONcTtKRl3EEnGF1u5a3PnklmGyeXE1U7AgjZU_5ILn9G1PceZSN_InStUKVvhdACU6yoAfZWPJ7vSjEcGFbJEM8KpBVKiPzz0vbflYGYilSw_7vICPwQL_WlH4WReIyouAgGAIRazv7_ANdmzeKL_CJ4GqBTz2sbUiF0YIh_rkcbKkpCpTk8ojKVAbwDZ01DYXBQgvAEJeBuX7OayOr1P54-gmGkftnymKGcIM5Kpiq3rppHwMi3gTTqHtFsCC8qvwO7LKfPA4aZu5D12rMi7I1mRPsWXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت اینترنت پرو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/IranProxyV2/8320" target="_blank">📅 20:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8319">
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
