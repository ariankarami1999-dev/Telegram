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
<img src="https://cdn5.telesco.pe/file/OZ0kO7YCOaPhZVJM_qAYITFKP-GQ9UlfiMZcIVc_7r0_QuK1_2pIqB99mHEcVlFPCmFIXPEloULgymVVa238xJETU1OrUXKYP13cGRcqu23592m5HkSwGE7x3IMWhoRoy8TJqSSae24QcxJ2dSX6rK2-BG6ZIPZOUEf4A9edlz-ju4KUTkydvvuFEgeskiETUcQYAoloZhWz-f6lKruLI04oU6SFSQassomQRIMXDwrv5B-wTg5o16Y8WdU7HLSUqTWTxw_Wwuj9YvgVR-sdR3pvVIwuwNSnEMPtApcomS4RdFDD7gGVCwpNreLjj8WGu9aoiUSJY5YOQI5UxSsWuA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 309K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 03:18:49</div>
<hr>

<div class="tg-post" id="msg-91792">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07800c01b2.mp4?token=sId5HnOVrV5gaX9Li5an-Pa25ree7rvbh_obIMEfBMWfhwgvCa7WZuvB-8sBNwSBtEV8t4JxPad_rDwBfim50ZdcJsQKtB8_Ob7PPM1unRydBNIrPRcBNDd3_jKqMotsa3hgpWRNlQn2gr6tdb66d9jYJQdHUtskwLWVfjbnBtk_zj0BNGPp0PmyQHDgWXoIyMHta5zeZoigicuK_kIHoB9d0MyLLkG88-iGkqR4BJlrPBR2n4CBkh67ixESYAhVmD6oq8Ei533csrSFxv8YQLo7-C9fHgZZgFvOIDPhh-dwCPXtzxW5I-CqmMgUMLJIlWvlokmhV1ajSXgOAl3seQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07800c01b2.mp4?token=sId5HnOVrV5gaX9Li5an-Pa25ree7rvbh_obIMEfBMWfhwgvCa7WZuvB-8sBNwSBtEV8t4JxPad_rDwBfim50ZdcJsQKtB8_Ob7PPM1unRydBNIrPRcBNDd3_jKqMotsa3hgpWRNlQn2gr6tdb66d9jYJQdHUtskwLWVfjbnBtk_zj0BNGPp0PmyQHDgWXoIyMHta5zeZoigicuK_kIHoB9d0MyLLkG88-iGkqR4BJlrPBR2n4CBkh67ixESYAhVmD6oq8Ei533csrSFxv8YQLo7-C9fHgZZgFvOIDPhh-dwCPXtzxW5I-CqmMgUMLJIlWvlokmhV1ajSXgOAl3seQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Amir Tataloo – Raftam Ke Raftam</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/Futball180TV/91792" target="_blank">📅 02:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91791">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RL2aw8x8lrb558ZDsPZ2hf8019L22srCnQbI34vRm_aX_aAKfBHuFmV3pVM-2IoI1l8S5VAHzT8SZDLvd1atvuQQa9Twh8K89myuR1FLHSotINc_WXalkZLIiSoZARQ86V34qttNIXbj3s4QpKfS_Hs5nyRXWnj17QHfxRn9ayXjhlgJ76u1lbpHdTC9Yeey-SyxuYY3xmfqIrzA-dSIbaDTnZmyc5LBGtqCgc3nuyQTz_CUhsAt1VGaJVMCAqpmj6CMrpdXidsrG4D_5_g8YY6usjVdhZJOXp8bx8XJx_P5j33gSq_XBrqdOaKcGRqym-q7LUX1VLLSwEFF7avxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔻
خوزه آلوارز خیلی نزدیک به لاپورتا:
🔻
آلوارز شخصا با یکی از مسئولین رده بالای بارسا تماس گرفته و گفته:
من نه با رئال مادرید مذاکره کرده‌ام و نه قصدی برای مذاکره با آنها دارم و فقط میخواهم برای بارسلونا بازی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/91791" target="_blank">📅 02:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91790">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Raftam Ke Raftam</div>
  <div class="tg-doc-extra">Amir Tataloo</div>
</div>
<a href="https://t.me/Futball180TV/91790" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آهنگ جدید امیر تتلو به‌اسم «رفتم که رفتم» که از پشت تلفن تو زندان خونده و وسطش گریش میگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/Futball180TV/91790" target="_blank">📅 02:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91789">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201d3221ec.mp4?token=lWJP6lsmBOa0Wv9JF8rIZQUO9GbzNhxIhkLbMhLW2l_tR7pkk27SVGhFMD_JpDdZjwpcfzRL3FKKsFgEXHwO42f_SnbQYpcS5vRhXEKgR_NgUng3UkBid8sGLyfzOZu64Lkh8wnjTOn1ufhHLIJ1LoPqSpuVgR6dv1pfvRSdadyDFXzbDKvoIF0m_K4Bliygoc9wb--JxkWfA0v3besF4Sa10De0fTkZ3EDa35DuwPqSBoFK4v1ljGeAQOkbTsA5va9ZmF4n9f13Ody7kWToV1VUtr6O-7zBfOehxe_NlwdPsRA0YoJYGWiHbULz2vQgqYR-Zeh0iq3UJZ6T4QN7nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201d3221ec.mp4?token=lWJP6lsmBOa0Wv9JF8rIZQUO9GbzNhxIhkLbMhLW2l_tR7pkk27SVGhFMD_JpDdZjwpcfzRL3FKKsFgEXHwO42f_SnbQYpcS5vRhXEKgR_NgUng3UkBid8sGLyfzOZu64Lkh8wnjTOn1ufhHLIJ1LoPqSpuVgR6dv1pfvRSdadyDFXzbDKvoIF0m_K4Bliygoc9wb--JxkWfA0v3besF4Sa10De0fTkZ3EDa35DuwPqSBoFK4v1ljGeAQOkbTsA5va9ZmF4n9f13Ody7kWToV1VUtr6O-7zBfOehxe_NlwdPsRA0YoJYGWiHbULz2vQgqYR-Zeh0iq3UJZ6T4QN7nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات دیوانه وار اوکراین به خط لوله گاز اصلی روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/91789" target="_blank">📅 02:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91788">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
وضعیت الان اینجوریه که:  آمریکا داره ایرانو میزنه ایران داره پایگاه های آمریکا رو میزنه پاکستان داره افغانستانو میزنه اسرائیل داره لبنان رو میزنه ترکیه داره عراقو میزنه یمن داره اسرائیل رو میزنه اوکراین هم داره روسیه رو میزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/91788" target="_blank">📅 01:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91787">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
وضعیت الان اینجوریه که:
آمریکا داره ایرانو میزنه
ایران داره پایگاه های آمریکا رو میزنه
پاکستان داره افغانستانو میزنه
اسرائیل داره لبنان رو میزنه
ترکیه داره عراقو میزنه
یمن داره اسرائیل رو میزنه
اوکراین هم داره روسیه رو میزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/91787" target="_blank">📅 01:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91786">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
حملات هوایی پاکستان به پاسگاه مرزی افغانستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/91786" target="_blank">📅 01:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91784">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🇺🇸
آکسیوس: نوبت بازی آمریکا تموم شد و دیگه خبری نیست. حالا منتظریم ایران بازیو از سر بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91784" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91783">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🇺🇸
آکسیوس: نوبت بازی آمریکا تموم شد و دیگه خبری نیست. حالا منتظریم ایران بازیو از سر بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/91783" target="_blank">📅 01:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91782">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
حملات هوایی پاکستان به پاسگاه مرزی افغانستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91782" target="_blank">📅 01:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91781">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
حملات هوایی پاکستان به پاسگاه مرزی افغانستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91781" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91780">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfUB-1qqEaddmABPm7CIVEiJIB0vZmMRFvz64pB_iTHZ8belA5Hr-7w_1DEyiqJFxQja5sNRRogY8BYSvgrPdzSk_c8kW0SGNb5cIe9BrqQklBwsrhjZ7SK2H6j2gGXBvrjYPxb09q0XGaE3xICJmnpBRGZqGUBNUTbCgU-Y1ZB95m_eg53GOgsOin32YZXq76dMcTMfvHkRMLkf6iEojGQ_GNiGu8Gab8GKYTSK04MAuPlKxi4EQnY5sN4wAdsQfchUQYpzZcHD2wPfeoqpI7GdToQ6AULP9EdaHKF440mb1CDeuCmz-P4Oxm2H2LT-LF9mUKMgsaRPewvZDDS0xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙁
سید مجید خواب بود کی بیدارش کرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/91780" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91779">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
فهرست اولیه اهداف آمریکا در حملات فعلی به ایران:
-پایگاه دریایی سیریک
-پایگاه دریایی جاسک
-موقعیت پدافند هوایی بندرعباس
-موقعیت موشکی ساحلی میناب
-موقعیت موشکی ساحلی قشم
-بندر تجاری قشم
-کوه مبارکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91779" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91778">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
خاورمیانه امشب تو اوجه : اسرائیل دقایقی پیش به لبنان حمله کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/91778" target="_blank">📅 01:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91777">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یه خبر از آلوارز بریم؟
🙁
🙁
🙁</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91777" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91776">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یه خبر از آلوارز بریم؟
🙁
🙁
🙁</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/91776" target="_blank">📅 01:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91775">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aca6ef1dd.mp4?token=LkWdaWIV8zjO46V-fwcXRs1at2Oui3RxCx47pGUgouTn4W2R0UbN0aCsGD_CGLbQMuU8iJB3OrWJZGJ--HH2EJVMoZL2B3Q35dov4IZDRWGJFfA96YjNI0WR8ujzPYAzwiS-H5cbS3W-RAwiejZSUaniQzbrVB4qf0rPt3zRVUQQ93_vPyo36ZWtZ9SUysmigkmiTM6WZqL2CkjrsZOFkwb1J4eNlxR8mGQlFPppzgysH3Ihd0WCxW3Zx3QELmi_2NObpRMZsAKB2aunsjSUOSGKNcJA2OREhrHDUItmsszWWbbnsHeBjWLTOl-VGIDzd45PALPVoMs0kFzOsXYOZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aca6ef1dd.mp4?token=LkWdaWIV8zjO46V-fwcXRs1at2Oui3RxCx47pGUgouTn4W2R0UbN0aCsGD_CGLbQMuU8iJB3OrWJZGJ--HH2EJVMoZL2B3Q35dov4IZDRWGJFfA96YjNI0WR8ujzPYAzwiS-H5cbS3W-RAwiejZSUaniQzbrVB4qf0rPt3zRVUQQ93_vPyo36ZWtZ9SUysmigkmiTM6WZqL2CkjrsZOFkwb1J4eNlxR8mGQlFPppzgysH3Ihd0WCxW3Zx3QELmi_2NObpRMZsAKB2aunsjSUOSGKNcJA2OREhrHDUItmsszWWbbnsHeBjWLTOl-VGIDzd45PALPVoMs0kFzOsXYOZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی از بحرین و کویت هم‌اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91775" target="_blank">📅 01:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91774">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
صداوسیما: کشورهای عربی شب بیدار باشن. باهاشون حسابی کار داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91774" target="_blank">📅 01:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91773">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خاورمیانه اونقدر عجیبه بعید نیست نتانیاهو توییت بزنه از آمریکا می‌خوام شلیک رو متوقف کنه و به میز مذاکره برگرده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91773" target="_blank">📅 01:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91771">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
حملات شدید به مناطقی از میناب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91771" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91770">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
ترامپ : فکر می‌کنم پاسخ دادن بسیار مهم است،آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند، من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91770" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91769">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
سنتکام: در حملات امشب از چندیدن موشک‌کروز استفاده کرده‌ایم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91769" target="_blank">📅 00:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91768">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: آغاز حملات موشکی سپاه بزودی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91768" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91767">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇺🇸
⭕️
سنتکام: پاسخ دفاعی ما علیه جمهوری اسلامی در مواجهه با سرنگونی بالگرد آپاچی آغاز شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91767" target="_blank">📅 00:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91766">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🇺🇸
⭕️
سنتکام: پاسخ دفاعی ما علیه جمهوری اسلامی در مواجهه با سرنگونی بالگرد آپاچی آغاز شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/91766" target="_blank">📅 00:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91764">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYBonctKPMc5W3DVznby2R8oL5EPDbB0yQ8oP3BLTNzuAB0R6LAcP9s6ZXNyT2TzpHqM2-GDk5FZRbaQ-OfeaqIYJoQjJIuK99m-HynZJyD2iPu9AfS9z8p50inEHbqEcNGmo1nrUUJdI2FHWe6eErz4zBKPQN5sYxwxu7CrcGHb-L9BFIDDgDQJ_1OajLGc11VQ1WIc3PzKklFuwz0ZcMoEMPS9us96J069fvHyk5FIa3Bvx3FK8h_A2pLsk1FlXWy1pmDZ84S6kYnv-OuhN8EClW1D84qEJ1UbozTj1w3sCwvJk7pPNrbrK6-N2j4azsp7RybiE5zQndzz4xAIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حداقل چهار انفجار بزرگ در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91764" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91763">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
💪
بسم‌الله الرحمن الرحیم  گزارشات از انفجارهای شدید در سیریک و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91763" target="_blank">📅 00:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91762">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
💪
بسم‌الله الرحمن الرحیم
گزارشات از انفجارهای شدید در سیریک و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91762" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91761">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
پشماممممممم خبرو داشته باشید افسردگی بگیرید
😐
😐
😂
تیم‌ قلعه‌نویی در آخرین بازی تدارکاتی با منتخب شهر تیخوانا مکزیک فردا بازی میکنه
🙁
🙁
🙁
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91761" target="_blank">📅 00:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91760">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
پشماممممممم خبرو داشته باشید افسردگی بگیرید
😐
😐
😂
تیم‌ قلعه‌نویی در آخرین بازی تدارکاتی با منتخب شهر تیخوانا مکزیک فردا بازی میکنه
🙁
🙁
🙁
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91760" target="_blank">📅 00:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91759">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trQtLmmJfy7prQn3scSMLWyXxpSiI_9T9LwYn8a2nixPEVZ0Po5pw24GLydoqVmWRdeCR0FkXGiRXfNUSN_O-8p9YanX_FTbdI_kUu6b2wBban23L7K-yOKIplnGUYAZPfnFIiFJ_NLs04h3It4o5sBKtNZWSP0ew9mtshAFmZwE8QKXmjgh8q21Vme50PIx00hgwAy3A2hO9deiya7rGVe_vpBBaVzmbzcEeignJpfPnR7jgGcMj8jVsMoS9oBlpcsfXHuCqVaPf9T3EmUuDrRmeqmBT5n3QWO-4K03Z_S1DEHXH3vSyHbRfXd3jLIv9cEFXxtkgw6MnnkDttLoUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
موریگی دومین گلزن برتر فصل لالیگا به فنرباغچه ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91759" target="_blank">📅 00:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91758">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtaTOEPT8-o2CEc0J3Gueo45Dv7046iV6Wmveip9d4UdQK0hHPT8eux8tgMdDe6fl7_NENgNXI3RPF_B0rQ-XAkG1GN99z12jWmtwtpwU_qJB7nkjDehbtt93Nrl5UxYC1jZmyrDm85qCH-HvdOI19SvcroheF-4zs0RInf1AguOQC7BzsSY88bt7BRJzfMjd25cE1qhXnqncEizDdScmNl3EwVjnUAo21JgK0FPwy3-oAWV6W-M0hwQSkXmli4aTA2ZV9uzFFs6BW2yJNwLYsAcoX0NUB4q8rgHmkRsvS5jInEe6AP45nZc43LEw6ccz3jugXuMWt69U3KOrGiaPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🏆
#فکت
؛ هیچ بازیکنی در تاریخ جام‌جهانی به اندازه لیونل‌مسی پنالتی نزده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/91758" target="_blank">📅 00:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91757">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1wJEu7gwC_3u96BfIBEItg7muUQesDccbolsqmbcr7TnNivohW0aGfQqdR5CIaldeH1nCjmXEOEg0cAQF1WiEe3JkXFR85vQ03Ol-QeeASBMXCXuR7nepiWTf0Ms8i4Fh5v51BOjq_-j4ATIYv6YK5c5urS3uVKmM_w_PQ1rWUPkuTI-hZkCJTs1RnQuB_PXeagxyJtoVsas5ZCXzO886pFchb6_-3udKns4PuaheJRLbhznuDkCKQlzXzTat4mmL6vlJfFVlXmW4lrY1foBBxqUmDVVFY3DIIWJ-0RV1FNmMlqTR35j_rasLTmtmFOTMbGxbJH_dHNcVuK_Y4-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇳🇬
نیجریه
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
چهارشنبه ساعت ۲۳:۱۵
🏟
ورزشگاه دکتر ماگالهیز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
نیجریه در
۱۰
دیدار اخیر خود،
شش
برد و
چهار
تساوی کسب کرده است.
📈
میانگین گل در
۱۰
دیدار اخیر پرتغال
۳
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نیجریه
۲
.
۶
گل در هر بازی بوده است.
🧠
اگر دنبال جبرانید، یعنی از مسیر تحلیل خارج شده‌اید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/91757" target="_blank">📅 00:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91756">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوست دختر بعدی وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/91756" target="_blank">📅 00:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91755">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAhRxgPrhPqWcIeYC6wgqx2jhqi2gS06sULNjdRfzfaVTT9IG8G8NbxqlMdVM8067WL8_bHPr4GoQzhBsD5g8T-0UtVkZkTTKkMTXETZ7XyBT_6rWzYYfegechV1riY3hl4A5-hjeH8zuixpjJX5auyyWPUr4J1ZLd52xicvHKl3MfrySH8ALHWTp4T5LlX5O35NbHOFvtIpoDLHEdxipRoaxOHnDGEC6BtioD7U2V4iKK9ySwKSWRvBL3V1pWNp7zZF0p5VNVeLPAmh8lMFXW-VWeWsUtflNsbGePe4ktGKshnSIq806pcJaAO1y3FVIYlC4HF__G8I5wcdTL6Bfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوست دختر بعدی وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/91755" target="_blank">📅 00:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91754">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07e18ed18.mp4?token=pjIx4KbDU0joMWEDNaTdLlYW14M96SZPISJfeiKP3IdEFli2FNfU2plObHa7TUAQ0yVoS7xaBlFNFlB500oTYne-LkG1Wd7aS_f5Vm7ZqTMze_ApmUaujBMvDB1v7P8DYAQ_av5dHWhszxd26jWrQqTUJhZAXGE9m6lZYGoSIMBN2lglBS1S81t3lQZqWP0K4CjY0h1jSAw1ltXmqF8-LJ3rsBEwkk2l0Z5jiN-0GxKDPLySnUxKZQ0PPf-T5oeLaKcjKblmw-wc5fbf_ObDRuO_3GgHn8yAis2_3jTs4iL7Q6Q8zUYo5TZPtDB6NZDQeFRQeYeKEaRS6Jz0ejtEWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07e18ed18.mp4?token=pjIx4KbDU0joMWEDNaTdLlYW14M96SZPISJfeiKP3IdEFli2FNfU2plObHa7TUAQ0yVoS7xaBlFNFlB500oTYne-LkG1Wd7aS_f5Vm7ZqTMze_ApmUaujBMvDB1v7P8DYAQ_av5dHWhszxd26jWrQqTUJhZAXGE9m6lZYGoSIMBN2lglBS1S81t3lQZqWP0K4CjY0h1jSAw1ltXmqF8-LJ3rsBEwkk2l0Z5jiN-0GxKDPLySnUxKZQ0PPf-T5oeLaKcjKblmw-wc5fbf_ObDRuO_3GgHn8yAis2_3jTs4iL7Q6Q8zUYo5TZPtDB6NZDQeFRQeYeKEaRS6Jz0ejtEWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به جام جهانی ۲۰۲۶ هم رسیدیم ولی همچنان با اختلاف رو دست این مصاحبه نمیاد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/91754" target="_blank">📅 00:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91753">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e12c65af.mp4?token=j620HgrCMBeYc-5igaqk1CkJSFgK105R-axFL0mPadGEHJ6yVgaU2Nibpq_DgGwDj8_YRp7t6cwPovjuQqfJwyD9OG7NuFGbNwpt4L1_EWMMWSYKvThXRU6LMpF5RASFrY-UrxNwqaMD4BlzWln37L527y0kdTqEAGxZ7OjDzpDyh5_C_7tHs33qEIykHQOFWRNO1pBPONobpTKh9ogWTcbQRzqZ5U11HqMjn20cC9dJAr7rgV5ajLV0DUY7Fo3myGy2Bt7Rjxv0VOnYaAxL7587l2o5KOTv3mXja9v4w_PfqRku6cGjJxKbEuAM4gf6zgmcDsHD2JzAyKWS2E6D1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e12c65af.mp4?token=j620HgrCMBeYc-5igaqk1CkJSFgK105R-axFL0mPadGEHJ6yVgaU2Nibpq_DgGwDj8_YRp7t6cwPovjuQqfJwyD9OG7NuFGbNwpt4L1_EWMMWSYKvThXRU6LMpF5RASFrY-UrxNwqaMD4BlzWln37L527y0kdTqEAGxZ7OjDzpDyh5_C_7tHs33qEIykHQOFWRNO1pBPONobpTKh9ogWTcbQRzqZ5U11HqMjn20cC9dJAr7rgV5ajLV0DUY7Fo3myGy2Bt7Rjxv0VOnYaAxL7587l2o5KOTv3mXja9v4w_PfqRku6cGjJxKbEuAM4gf6zgmcDsHD2JzAyKWS2E6D1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کول پالمر و ژائو پدرو ستاره های چلسی تو موزیک ویدیو جدید و مستهجن مدونا حضور پیدا کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91753" target="_blank">📅 00:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91752">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الان توییت میزنه و میگه: جنگنده‌های فوق العاده زیبای ما در راه ایران بودن که فیلد مارشال عاصم منیر بهم زنگ زد و به همراه چندین رهبر کشورهای عربی ازم تقاضا کردن که حمله به ایران رو متوقف کنم و اجازه بدم تا توافقی صورت بگیره. منم قبول کردم و همین الان به خلبانانمون…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91752" target="_blank">📅 23:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91751">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325c4beb65.mp4?token=cWi2wTsEPPY1VIf6BRXk2OVgIQibUD-HnOtXqaLW6pv1UTix9jT-lM_C4VUjdbYGgrHfOg1DYuwCieSjGP3t7UPsj5e8mHzSpEpkcYiT7VSL7MVtLl2eK1PPVzyfazJL7mP_JTQgqWUcHcAp2OXfR7YXvRPi_aFvj4v4eBvuxhePpRQvOuUl44pcq2jyuYN3lg4sOkXYlasC_LwJRrDJ6_PkbMBWZxtN2IGTvjh1woKJR9d0jW3aK3HX7o3kzkzkuP1ssBV9y9m9Q2zP4SjaItyuBYnoW6C4Sps5VEzu51gzIuLK8wT1tUare8KXLj7eiWMsVtRzkyITR6HYwoxipg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325c4beb65.mp4?token=cWi2wTsEPPY1VIf6BRXk2OVgIQibUD-HnOtXqaLW6pv1UTix9jT-lM_C4VUjdbYGgrHfOg1DYuwCieSjGP3t7UPsj5e8mHzSpEpkcYiT7VSL7MVtLl2eK1PPVzyfazJL7mP_JTQgqWUcHcAp2OXfR7YXvRPi_aFvj4v4eBvuxhePpRQvOuUl44pcq2jyuYN3lg4sOkXYlasC_LwJRrDJ6_PkbMBWZxtN2IGTvjh1woKJR9d0jW3aK3HX7o3kzkzkuP1ssBV9y9m9Q2zP4SjaItyuBYnoW6C4Sps5VEzu51gzIuLK8wT1tUare8KXLj7eiWMsVtRzkyITR6HYwoxipg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
فوری از ترامپ:  «همین الان ارتش به من خبر داد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی ما رو سرنگون کردن. دو خلبان داخل بالگرد بودن که خوشبختانه هر دو سالم هستن و هیچ آسیبی ندیدن. با این حال، آمریکا چاره‌ای جز پاسخ دادن به این حمله نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91751" target="_blank">📅 23:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91750">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961fad6eab.mp4?token=RlZBjAJKuL2Bux1HLcw548BVBherpNFOtigWR6fFPJQWVBi4gltRUIhYmQ_HJRF1FSN1DipaYN-9Eb9u4tuN950O83i_EsPvkCxVUwF7VH3HvR_Y-7a068P2twzyq0MmVP9OjeTmt4Tv35oaesvTECSOiILX7fSxKQqI_3zLJ3mO4NpDEazSZAM13i7eJ5xj0eqr0h0TeW_aDr1iRf6qhNaaXpLbZlsYNF1rTyRSgnQaDwhxbKTE9yXaqUeKvN38yOn3vywpG4ETBw-eXz_iQnmigEykIZdHwgMdMsurLFXzgbGTQj02-hASr7o7bn5tRHOsZCiIOGfQXVVqNl9RUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961fad6eab.mp4?token=RlZBjAJKuL2Bux1HLcw548BVBherpNFOtigWR6fFPJQWVBi4gltRUIhYmQ_HJRF1FSN1DipaYN-9Eb9u4tuN950O83i_EsPvkCxVUwF7VH3HvR_Y-7a068P2twzyq0MmVP9OjeTmt4Tv35oaesvTECSOiILX7fSxKQqI_3zLJ3mO4NpDEazSZAM13i7eJ5xj0eqr0h0TeW_aDr1iRf6qhNaaXpLbZlsYNF1rTyRSgnQaDwhxbKTE9yXaqUeKvN38yOn3vywpG4ETBw-eXz_iQnmigEykIZdHwgMdMsurLFXzgbGTQj02-hASr7o7bn5tRHOsZCiIOGfQXVVqNl9RUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🚨
🙂
سوال روز از رئالیا؛ دامفریس رو پرز فرو کرده به رئال‌مادرید یا نه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91750" target="_blank">📅 23:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91749">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📌
۱۰۰ میلیون تومان جایزه نقدی - بدون قرعه‌کشی!
📌
​
​
✅
قهرمان جام و آقای‌گل رو دقیق پیش‌بینی کن و کل جایزه رو برنده شو.
​
⚠️
ظرفیت محدود:
فقط برای ۱۰۰ نفر اول.
به دلیل حجم بالای درخواست‌ها، اولویت با کسانی است که زودتر پیش‌بینی‌شون رو ثبت کنن.
​
🔸
برای مشاهده شرایط و ثبت پیش‌بینی، همین الان وارد کانال زیر شو:
💵
​
https://t.me/+5uTOXJ02mftjNzQ0</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91749" target="_blank">📅 23:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91748">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cUM30ZKtVLdmiunf8Q-n3E2MXmMnFqzYVSOgwKqrAef-VTAtI7tvosnXr00vTJgXQ1U9g1VTuBuBKjaNx1p9lwzxVQJj9eAEFwo6946Xppnq3E0G6oiN8Foy4SfavCFXBiHYGDShZ_gTHLwdxhbxsNeaY4z9Z-52WmBXe9dYnTWdVPJfCXS5NgyYVswC9W5cBIK4YzHGUnwfIvl4Qy5a6RB4HxONB3YsXUJqjyAabA7utQLRkgvcBh6KUUmW1rLZKvjW8a4xUO418_yHXeu7rlvpA1JANQ19uC9k_imky-irR8xy-qvOUO0PD9Q2h-6e2eQGoCFZs8XFU4vwHT8zkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
۵۰ بازیکن برتر جام جهانی ۲۰۲۶ از دید ESPN
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/91748" target="_blank">📅 23:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91747">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXLMrBk98tU303dm0C_fLuo53tRHs-kXm18ZcVIsYCjDvaB46jALW4b0OJfoHK5v6NO6lBG4bI9nsm8olmflQ71YqjISN8XOJm4pvGiodcrDcEmC_nPd-ijNzxMrDl-DYd9WjhVYOru9NDVzIyU8rVVEfNhebLdGZpEehOOa2rjaTjVDSGGOIlZr3hIPCElYUzwGRY-WAfYsHn2bHqrzBUpBUbeSUX8AtTjsbPYGI3_PvsVj36CNxgHxAdn38AB41ETNg6w_x1oYUzmMbeud7A6pnmk7b10Vp2g6c4kj5yNMLeL0lNQoUAqxnrgFCBNvw4JnLa5uDcFfJ4YUBR08sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💪
🇮🇷
🇺🇸
فضای پروازی ایران کلیر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91747" target="_blank">📅 22:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91746">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
کیه‌لینی رسما رید به رئال :
⬅️
فکر میکنید اینکه رئال مادرید هر سال توی لیگ قهرمانان یا میرسه فینال یا جام رو میبره، فقط یه تصادفه؟ توی دنیای فوتبال همه میدونن قضیه چیه، ولی هیچکس نمیتونه درباره‌ش حرف بزنه.
⬅️
حتی اگه توی زمین همه کارها رو درست انجام بدی، وقتی طرف حسابت رئال مادریده، فقط با بازیکن‌هاش نمیجنگی؛ باید با یه قدرت نامرئی هم بجنگی. همه‌مون میدونیم وقتی داورها اون پیراهن سفید رو میبینن، دستشون چطور میلرزه و موقع سوت زدن چقدر تحت تأثیر قرار میگیرن.
⬅️
توی لیگ قهرمانان، بزرگ‌ترین رقیب شما یوونتوس، بایرن مونیخ یا بارسلونا نیست؛ بزرگ‌ترین رقیب‌تون نفوذ و لابی خیلی قدرتمند رئال مادریده که توی زمین روی داورها اثر میذاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91746" target="_blank">📅 22:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91745">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
بیانیه باشگاه اتلتیکو مادرید:  - اون قسمت ویدئوی پاپ رو بریدین که می‌گفت طرفدار اتلتیکو هست!  - ادب و احترام رو با تشکر اشتباه گرفتین؛ برای اینکه سوءتفاهم نشه، هیچ تشکری هم ازتون نداریم.  - نه پیشنهادی برای خرید خولیان رو بررسی کردیم، نه اصلاً بهش فکر کردیم.…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91745" target="_blank">📅 22:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91744">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGqg9ncPNTWJ4oMY_qwa0Wvst1Rpx6V5r8hXKnSongtUS0UHju6vHr3Y47HWAMusR4mVdlGx7q7MR2QiOBFlBdg1-Y7TweRAQk1y13kdN26ib4lzebQ-NClgsiNkT_UhgoqFYONyHkrLPgRFkYJT0ZJTAVWM4Ve0EyE1_71ZV0W1_BWJjxWX8_V5xukfpUhQAhP3effV5hlRyappCO7m7qCI4zHVeoTRLkdur18y_Vooecg5RhDL2TM6_IHQkra-yoCkEpcurishRtnpRVPBMUao1BZxAW1ykjR6jqftbM_B8_89ufli9zcayF84a_ELZaBpCwe_w8u4U4yh8aRLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بیانیه مجدد اتلتیکو مادرید:  «پی‌نوشت: با استفاده از رابطه خوب با رئیس جدیدتان، بیایید ببینیم که آیا از «دزدیدن» بازیکنان از آکادمی ما دست برمی‌دارید یا نه. خیلی ممنون، رئال مادرید!»
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91744" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91743">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
#فوری توییت اتلتیکومادرید:
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91743" target="_blank">📅 21:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91742">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LQ5q_PEpIz77sYlQuoMAv2JybnI5DD13NNh_OgMiTxBKIxnvQ7kTY2FbpRI1jV1RMv-4yiab1UrTZHBNBmcUrBKv9YXZ1wAQEkVgYpOEP3ACYTj3N0ychl43KUtw2T1f-HauYbg-Lgk5uXng0FSEPPWHV05SWpPJ55vHAGoKP36bdrlov2FuC5dfzJljvKytv5khZlH2DqQeT82agaau-XviBXPjoJjs5JL7LiLoUKGLY4eDREW9bZgLIC_UnlYdGEPeKbHMtpX_I08HewbGx19xjlQ2qx-0Qhvnrv44GYxNlSbLcHIbJlBejfIE7XUYVYEHIKm5As84Mm0rM4iKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توان مقابله با این طوفان و این حرفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91742" target="_blank">📅 21:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91741">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adQPFJsfE5nsszSW_3rmNYurMl0bihsJge5i3o0jmjYosjv70AYCjG3okgKna8tcy0MikSTGFeD5TYLalkCiiSYT3WApPsxfwwELiTdv_0BHODA_WAW_ASpbEiwohkHK-aw37x503B3nlFdCFYhiIMy6V7ZJXKS43ApQdTOZXXE5ia04cFBk-DFb0KWr2zUxP_L_QpL_ijNrmQ7VEr9I1IeGUMFjdUDtuAzpusEl518VWYAoukYjoE35uUg7pjETQh-PvJZ_k82cRsmk1QV1mUKlK1oKtObJoCaJw4ntPrchcrEo_UhRMREljv2qwkPQ7cA5phyX-EGvAi30Nc-GQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91741" target="_blank">📅 21:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91740">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0NDnAF5rOV0Z1lR_IH_fXSGlQ50nzzqDQM3DIggX6IBc1oyhPCXhy3B6ANOqAmTn2rcELb51zK6-3mpFMxSgDYP0zz96AsUSINfP3saLocEeF1myPXWlWdM9A5dnBQ7v-xJ27kbF5SsNjl9Kgifq0Vem5SY2j0gXkNLxt7rKhXcF5hzyPMMZA4fReL6fecvB_f2enavYV4Uj4282je2t4rmxl68fFlC6p-48Jlr1vP9_Rwkjcf-X0zp7Mt03FdIVPXOxk-oEZjnNwUcFrRE0hH8dognKIJRZ2bUq0bJ4lwl4KaTntWuHlyQ-YplzvZ5MPtNxOiPl6ibk3wbK92s7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
روزنامه Ser:
در بارسلونا تأیید می‌کنند که مدتی است می‌دانستند رئال مادرید این اقدام را در مورد جولیان آلوارز انجام خواهد داد و این پیشنهاد رد خواهد شد.
و معتقدند که این موضوع تأیید می‌کند فلورنتینو پرز بیشتر مشغول آن چیزی است که بارسلونا ممکن است در بازار نقل و انتقالات انجام دهد تا تمرکز بر تقویت تیم خود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91740" target="_blank">📅 21:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91739">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91739" target="_blank">📅 21:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91738">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
حمید رسایی: از آن فرد بی‌خردی که اینترنت را وصل کرد در مراجع قانونی شکایت می‌کنیم. در شرایط جنگی و حتی پساجنگ بازگشت اینترنت یعنی خیانت به جمهوری اسلامی!!  +منظورش مسعود پزشکیان هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91738" target="_blank">📅 21:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91737">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
بیانیه جدید رئال‌مادرید بعد سه هفته: با نهایت احترام اعلام می‌کنیم که قرارداد آربلوآ به عنوان سرمربی به پایان رسیده و‌ از تیم جدا شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91737" target="_blank">📅 21:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91736">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تو تاریخ‌فوتبال بین باشگاه‌های بزرگ هیچ تیمی روز اول ارائه پیشنهاد بیانیه نداده که پیشنهادم رد شد و تمام. پرز با این حرکتش هم یه ذره میخواست رئالیا رو آروم کنه هم کیر سفتی حواله بارسا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91736" target="_blank">📅 21:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91735">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXZo6JGkfwlMVH5LI0t0GLsOU6iGfCfLdaohJ_lwDWt_4QiApD2wXbbOtKeufFWrvrUNnake6Z1oWHbgLxLCF4DH0mRvly4PwZfXiqk_hWltyP0b2UqRQYB_aHXHMR9qLTfqGRYVdAFvRJDGQYe1MM6TiqGrmhSR-O_KnG7Tle8O3FeVhiUvzM_BOOmDJegNoWviYHdAJ1J8EPfohCNPPdtbfKcDVbGI_tkw0ASXseuXcIqL-ZPz6dwyVXqTNwPzEjQq26JFUtdfPkNvX6C8_EsHDc_Y9yyhNfsvy3nqMGAYNhXhnrZvWcBc6P5HMxlE06RUKYBErNq19gKlPr57TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
لامین‌یامال: نظرت راجب مسی؟ امیدوارم اونقدری بازی کنه که نخوایم به بازنشسته شدنش فکر کنیم و‌ بابتش اشک بریزیم
وقتی به کمپ نو می‌رفتم تا مسی را بازی کند ببینم، چیزی بود که شاید مردم به درستی قدرش را نمی‌دانستند، و آن این بود که در هر بازی که می‌رفتی تا او را تماشا کنی، بازیکنی بود که باعث می‌شد از جای خود بلند شوی.
همیشه عالی است که هر بازیکنی گل‌های زیادی بزند و پاس گل‌های فراوانی بدهد، اما کاری که لئو انجام می‌داد بسیار دشوار بود، و آن این بود که در هر بازی چیزهایی به عنوان یک بازیکن منحصر به فرد ارائه می‌داد.
فکر می‌کنم مردم وقتی او بازنشسته شود این را درک خواهند کرد، و این چیزی است که آرزو دارم هرگز اتفاق نیفتد، این چیز باور نکردنی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91735" target="_blank">📅 21:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91734">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ولی عجب کی,ری زد پرز به رئالی های که بهش رأی دادن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91734" target="_blank">📅 21:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91733">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91733" target="_blank">📅 21:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91732">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🚨
رسمیییییی :   اولیسه ، وتینیا ، نوس ، پدری هر کدوم با ۱۵۰میلیون یورو به رئال مادرید پیوستند
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91732" target="_blank">📅 21:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91731">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🇪🇸
#فووووری؛ اتلتیکومادرید اعلام کرد که فروش آلوارز در گرو پرداخت ۵۰۰ میلیون یورو از سوی باشگاه خریدار هست. در غیر اینصورت زنگ نزنید مزاحم نشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91731" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91730">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91730" target="_blank">📅 20:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91729">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🇺🇿
#فوووووری
؛ ماشاریپوف بازیکن استقلال بدلیل مصدومیت جام‌جهانی رو از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91729" target="_blank">📅 20:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91728">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91728" target="_blank">📅 20:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91727">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qw3CqJb3g_VO4oIYzRHkgkjphRmHfHNo6wkZRUFmhaiOh2lDIQUzU8BnuaWvumgn1smIiSaq1bwslk6AkRYfuRn7bIVr68ReBKYDxPXir4zcJUgWle6amMtRRtDbL6th2ITmEScPFXLgxEx4XkDP4YFW6tyo6stHouUkPIdMpZ7ASeLLixjeoZOXHWFxNQXHFm9ldvWK9HbwRMfFTbZpUWu2Jbbe2vKSUoRIEtLRSH25EkbJ8DWFLA5U2Gm3jN2bGorVsG-Kx3rUxHdL81DCu5WSn2ZkNsgcZ-ukm5KuoT4Ub1xYHJBVWevXby0WENv8U3hjbuddyUXMlPpZrrgbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91727" target="_blank">📅 20:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91726">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ol29XM3-8cw09S0gOlE9YCuv3JXLQGZDpsLUtMoNAFGWJ_TlYaNM35X0AnEDeEJexQ9Zrfn7Z99Rw5PXRGjIX9SuqrhXt5tdlWo1H88BXDLUWu9gBEmTZxlzXrzTmifkyscKfzCSjAm43VpDM12-krMQldSlgM6ahdtQep0m5w4lewzr-lO2ogCEDSnQ6suMQfsVWN33tEc8R46kbXEveThLKGG9JaN0aY6rmla4EHgQu2OZwpyL8yvDkRjtv-Wp0Odeq56K3uvUzdQSiVtMtrPfoUOPXJUDADA6tBLYp-RacHO4xiSD0LHKQCao4-Mr8jhIZufWOqRcCpQLg_0XSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری
؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91726" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91725">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvZFJd-gra8HQwOEB3QipviotTLIuNDlwV0H4ko6N1zDrZCl4lT26nX27WHGbXKG9TPvMCmkXCur1rUZoVweaRy9G1j9Phitl5tdEyovapTThC8AOHQBqF51ay1C-AtV_4B3BBxc5AKX4gdtqv5aNmaduVMYZD37-jl8Xenj9IKQMf0sygL9x5FGiTvbV2cUXs0hnmPB0giCOl8_1zCpKjBzrJrdyKfZrIV-W0Z70mNjxVWPL2Yh2awjesfG7459dkMGkTC788wXMdKSgALs_dvN2E7ANd_09kyDRSqK3ME8tzjQI5HCTGS7UBJ534oFxX9MqcU73D4p5CpRmG1o7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو ناتالیا اکس نیمار
چه جواهریه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91725" target="_blank">📅 20:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91724">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇺🇸
فوری از ترامپ:  «همین الان ارتش به من خبر داد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی ما رو سرنگون کردن. دو خلبان داخل بالگرد بودن که خوشبختانه هر دو سالم هستن و هیچ آسیبی ندیدن. با این حال، آمریکا چاره‌ای جز پاسخ دادن به این حمله نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/91724" target="_blank">📅 20:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91723">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5kjlJU8_fIZEEHGGa0TT-gmB_XjUgvh_n3BY4DbcTaAl8Xh5VtB_iLQ2eZ9-5TmiC33-maLFNe8mV92DXY49X3Rk1xOjZn9oYYz7wPXc0C5hGeA3-sBwnTqdeWHpbOemnU3Rj8Ns4Ik_ARzRqa6nucIAzrVsyVe5ufkRyW2JpKo-E3E2kio0VHdFIC2sm3s0EHq34rMvg4d959xzmqxFtwc0_5w0uC_r8ujjC9ZRz1I3A6zXrFFGDtKnX998tEGbSZc47aJ3-85Ge6eS19zqjNqYNfrvhbkok6_3QfTok2ZbWfNxfRT4ckM8WVoRfljA3wYhzU-8Qg8DxpkhrNz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
فوری از ترامپ:
«همین الان ارتش به من خبر داد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی ما رو سرنگون کردن.
دو خلبان داخل بالگرد بودن که خوشبختانه هر دو سالم هستن و هیچ آسیبی ندیدن. با این حال، آمریکا چاره‌ای جز پاسخ دادن به این حمله نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91723" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91722">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgeExQTIDGEQH_g3LewxxiUssl51JXyh4tlC_l9RJAPIMsxUgmcpE-GvR6hrbgm0W2sfWoZGghAIgt_bTLPzEUQ5o0OO1BKyVc0yf1JzVSovC7HqI-avCVa6DE6E1mrO3osYQEJOMB-lilF_4aw6UkD9NkgJTyeox7y25qHhuTm2wQgPJPSuvhXrZx0aY_pC7aQrWdtEffco42JCcl89k2hgF4hmV4-j2yZ7IvHmojOv_5FZT0bBw-_d7pI_SO-_0gSt_S0Wi3xk7VCwZG0UaauZh4Z3jDkZ5lZWri2xQKWA8oed47Kbe47C1Bh7K5ggB9xwNgkmkZK93SSlc0QdjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برندها با بیشترین تیم در جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91722" target="_blank">📅 20:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91721">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/itCNQ8gL7P-auI0udxrpdGTuKNGpZLBPehy4ukUg-Hcrj3TS5Y2yaOpaYs3onydo1aeFdk17fHw6M30x7d_2FcVKNte3hedSC9irjisoZRsK_t9ZAqLx9Gy_JoKckF_EW3trxKDL9CjQDDcyzJspcDrsCGwtoRLZ-h3FEJeYsvyWuLDQjJhR8sNU1JquIVi_jHQeYVurLCxpaITfL5qzZtrh9QIfIQAlyBBrX70J2DBBbUHyw5tTKEnSTag4IPyfEetypqQZtxBQePEnfyMqbfsyp0RLIA5mtd9HXhJnqTdV6rRsPuTXTMlPZQy8xPOk2b0lWENC92AObF7XH_2Lkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
فرناندو پولو خبرنگار موندو:
⭐
-
برناردو سیلوا هرگز اولویت بارسلونا نبوده. برناردو خودش رو به بارسلونا لینک کرد و گفته که رویای بازی در بارسلونا را دارد.
بارسلونا سیلوا را فرصتی در بازار می‌بیند اما بدون فشار یا عجله! مدیریت دوست ندارد بازیکن از نام بارسلونا برای بهبود سایر پیشنهادها استفاده کند، اما این به آن معنا نیست که او به بارسلونا نخواهد پیوست
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91721" target="_blank">📅 19:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91720">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7285144264.mp4?token=AJaHQPkoRSwe8wAhoupnjE3pe-W7mp2PFzp_JbpeBNwNCFGV-JQzsEkGyfksmBaTfkFX18pukKU-uilcsK3zTcApYpXeOL6CE_qu6lWD5R5b--0Ba7I_mgR0o0YIbHYo5w1r2rX9DrldfOiMo5H9S3F5UyoXN6N5lEFgJ17C5wRZiELB9lsy-4kqbDXfsBVG5YZSvlmawTXDLlRPFfG1QiSF1C4CahWQ8BsDJMpc-d-6nKDpW4nkAkbiqpcHAb8XW8fcft038fFUF__sehq7fCxv3qTMvivGNL-qFL9J9s2cCIJ51Y5wYPVk__QaqPKtju5DhGwKBMAOjEX_G_7i6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7285144264.mp4?token=AJaHQPkoRSwe8wAhoupnjE3pe-W7mp2PFzp_JbpeBNwNCFGV-JQzsEkGyfksmBaTfkFX18pukKU-uilcsK3zTcApYpXeOL6CE_qu6lWD5R5b--0Ba7I_mgR0o0YIbHYo5w1r2rX9DrldfOiMo5H9S3F5UyoXN6N5lEFgJ17C5wRZiELB9lsy-4kqbDXfsBVG5YZSvlmawTXDLlRPFfG1QiSF1C4CahWQ8BsDJMpc-d-6nKDpW4nkAkbiqpcHAb8XW8fcft038fFUF__sehq7fCxv3qTMvivGNL-qFL9J9s2cCIJ51Y5wYPVk__QaqPKtju5DhGwKBMAOjEX_G_7i6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔥
این سوپرگل تر و تمیز رونالدو به عنوان بهترین گل فصل لیگ عربستان انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/91720" target="_blank">📅 19:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91719">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
وزیر ورزش:
به فیفا اعلام کردم اگر تو ورزشگاه‌هایی که در جام جهانی بازی داریم پرچمی غیر از پرچم جمهوری اسلامی بیارن یا شعار علیه تیم‌ملی شریف ما بدن قطعا بازی رو متوقف میکنیم و از زمین خارج میشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91719" target="_blank">📅 19:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91718">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNTy1o1gKSap6KOtIkDkYWpstzSgY_w_bAhZbvJWuyyLceBR3Euv0LgkNf7YXvdJOUkaa2aiwZGRfZsNBgnQNVRPAEdyQbQQ3eCXfQLuxGL35ugTdbxers2hax0IE4Z7C6KVjUYMoPjUiUTFpMhzCJjbXMJSOKNQo2NVE-55zmXjb2MSFGvdFyth2_4DToA-1w5sDko_EO0P9_0jZw-kZ0tJ74DZAu6lniJ4H4ZpVWirJQMcUVMP8APfnATnuaPLIC9VlhJ3dhk9gIzPQjSsEeZuUhvfZbm9KnWa_JNv24B8afyUVYqsouwXhTjYaXFPA6qMBvB6--ZhXtXcSJKngQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورانیوم غنی شده که تو پات نداری داش دیبروینه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91718" target="_blank">📅 19:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91717">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
فوریییی
❤️
🇪🇸
یه خبرنگار نزدیک به اتلتیکو خبر زده آلمانی مدیر ورزشی اتلتیکو به دکو گفته از جذب سیلوا کنار بکشید تا ما آلوارز رو با ۱۲۰ میلیون بهتون بفروشیم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/91717" target="_blank">📅 19:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91715">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PenFtPvUyRB6rlI48eTpIFURySt2LPbsz1eWQPxwBIhchx5K1pU1OclPzOSO7Vkr5_rDdcSuHXsotsD13cD_3suFAU9aPLKapLlYxmuslfhg0LqITBP4PB42E15QGach-cK7OWBsQXVAm2S_pYR-Wq9GOltvqLg_UCs8Kl6qbdPP7PPRL_uu_n-XhZpIypIn13fAyKK7BHWQJu71A4Mz228RJJ3FsKZYDPPC6VHVeKmFItGmq1lJgmikj_UDRY2eaUrQW6rKNks32vzfL-QlwLro4ACxdFKrWcxEEHx1A-D1MySuyHUjVO57UMVjzl_PNM6LJV7AGtMhr7gQiLZ5Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qgUxyv85noRDZEZ1hB0XZp-GB2XL9x-MBUxWu9Mp0B6Fn_-NXaSUST9cWAefj2PYqkgfdFtp-rx7FIdQZQEHgux1lAs_MEEY5PJ1dZLGMMm-Tykb4oqbk19BObbrZA5W8x54EcH16Tc3YA9CNSmiPNJ9H5d0TOVe2VFKpWv2oru5E8rTDbwYVa932WQnmqclZMXAx4-AWwRkbcthGezFiPtPdCo6tr4GpwGCqpl18reD5vf3gZ50l9k4m2jCOQuVl1nGl_SFNLUKx4A75cLKLiGKVywCm0a68O48VuUUcXRob3jgzNlCohN728RajF6SqmL7TkYrt5Fu2U9WcbMcjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😀
🏆
- ورزشگاه مونتری (Monterrey Stadium):
مکان: مونتری، ایالت نوئوو لئون
افتتاح: 2015
ظرفیت: حدود 53.500 هزار نفر
🗣
با منظره کوه‌ها پشت جایگاه‌ها، به‌ویژه کوه Cerro de la Silla، که یکی از برجسته‌ترین طراحی‌های بصری در مسابقات است، شناخته می‌شود.
🗣
استادیومی بسیار مدرن در مقایسه با سایر استادیوم‌های جام جهانی (کمتر از ۱۵ سال پیش ساخته شده).
🔺
چهار بازی در جام جهانی میزبانی خواهد کرد (۳ بازی در مرحله گروهی و یک بازی در مرحله یک شانزدهم‌نهایی).
🔹
مهم‌ترین بازی‌هایی که در این ورزشگاه برگزار خواهد شد:
🇸🇪
سوئد × تونس
🇹🇳
🇹🇳
تونس × ژاپن
🇯🇵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/91715" target="_blank">📅 19:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91714">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حالا فکر کنید روی بازوبند مشکی حاج‌صفی اگه به فرض محال که اجازه بدن، قرار باشه بازوبند رنگین کمونی ببندن. چه شبی بشه اون شب
😂
😴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91714" target="_blank">📅 19:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91713">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3648d1bt7mkzOTu2Km4FrGH_FGXfHI5Mk6Z2GcmGURad-rn6JcRPx6Z2zRvHsmmzDy-wSy_k-8lEJprSR2WlbXAg3vHHUakwGsG6fcjdSNzxImaHierPLu8BOkVAy7WFErgf-2IUK419PBjx_EsSNvuvCgZlK-lLVofPf4S5_RVgEUBT_SByA-57-2I4yhS7vIQfWdUKSsi-Wjc5Jt5akg4zmNw5J9Oa4PlfNHx9ZARXUKLp0OnpUvuUzF6qC2gK-IphDhCNKnN17etmzSXcw7-QLsNEk1FHQxs3yigumFTEGp7I3MLNzKvJa6w9_yT5cm9JlxMx6sSYOSJ5MAWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
مسابقات افتتاحیه جام جهانی:
◉ بزرگترین پیروزی در بازی افتتاحیه:
🇷🇺
روسیه ۵-۰ عربستان
🇸🇦
(۲۰۱۸)
◉ بیشترین گل زده شده در بازی افتتاحیه:
🇩🇪
آلمان ۴-۲ کاستاریکا
🇨🇷
— ۶ گل(۲۰۰۶)
◉ معروف‌ترین شگفتی افتتاحیه:
🇨🇲
کامرون ۱-۰ آرژانتین
🇦🇷
(۱۹۹۰).
◉ از جام جهانی ۲۰۰۶ به بعد، کشور میزبان به طور رسمی بازی افتتاحیه را برگزار می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91713" target="_blank">📅 19:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91712">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcYCMDuMQmimkEUKiNFWHEGzLHYc9Kvo12oKwhWfmtsIfUGFC33a3J93clY57AL2BY2KEkRorPAo9Vn5F3JzE93Rv8eQFH9yxPWEbHxtqBM-aKnKO4cQAedeS7ThqadofAJOfwH7WZxTYAg2PaAD8fJTiDsMV34RX5Ib8OYiLg5RWuYTOXFMWEHXKD8FBcZAzQFE0K3Dl6WVackEBLwyFlJs-vYat_dE2i1yWGN6QE99nH38zj3mWqZBGH0OJP4YZmlaOvK9DClq7YisJC1vzQuXk2Z7DSmzoNwywWbpd-GpVdNn5cdZER6jpk1MC03cap9hnat8U-KqZkJK1KKO5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
| آیا می‌دانید؟
👀
از جام جهانی ۱۹۳۸ تا جام جهانی ۲۰۲۲، تیمی که برزیل را حذف می‌کند، در سه تیم برتر مسابقات قرار می‌گیرد.
🤯
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91712" target="_blank">📅 18:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91711">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYzOPOvYFX1Kx9nwhcTh2l_q2Zd1H4z2LLOYyoGj8alNQeSjukbO0OoVg9UC6NmD3q0MvOvQC4WEJiOlQFTi-x_tzDq5a21mcSm2N0-mSjZ3B0CLdDHfqfZ8nZlpFmO4Ki4PcAd7n5qhyuy-e_2A-yBtGqfAOyaJa1cXXJUrQ4c7JBSJmgQcd3SXRmdncl1l2kktzijeFeD97MIZXRl2oONl-XxWHjFXzhVH3j2kxonwFxvLm4obBSR8kKaILeUpS2RHFFzCzZqfjYFRWiWmkP5ZNdNUSCKGejJMxmIeNNZ_HaibG7OTKjDkqMlZWsiDmxYc_i9yndwDaHF9bOq82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رونمایی رسمی فیفا از جایزه بهترین بازیکن زمین جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/91711" target="_blank">📅 18:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91710">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqcMINlpeOOpkby8v_O9cdCe7qaxTL_oFs4of08ExyQOkBQt2RIR9bMjHtcDd9QWVv5tP5UC24CRPUyjeoLlUOcsQpqC60cVNZXFyfcbK7l48L5c0Vj5vUmAyB-gANt7C9FGKXxkW0wst5FaVsVseTY2M0ALJ5OIhPfBl1buW_m-M6v6KB7UOdy-5Y9XfBsFbaKTE5qRCqR_rupLBp1TrHts0pI0RHUbx9NxkJvy8y3o5U0FPZ1DORKxlfSOXnECBjy6DjnYycGcRyzUSxEs2gHnhhGlJ3h4-9nY98O5zVUhLxmJL5k8CFAZCCGE2piQJQ217phh_RIbKHSA7w82mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو :
🇪🇸
🇮🇹
یوونتوس خواهان جذب براهیم دیازه اما تمرکز بازیکن روی رئال مادرید مگه اینکه نظر باشگاه دربارش عوض بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/Futball180TV/91710" target="_blank">📅 18:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91704">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJE5UmgIdCbBOXlbaRR0tuP8GCtEH_spAOMRVJavsRYy5jc1p3XMkNDnZrP9ouU-yuXr-1v-dkMNXPYyJKpd-gezQEVd3j-HfFQ6zI5Qt8JNRYiCN9m8JJa0hP-oa2TX3cIdOtftj4YI4AjPAp3PGz_ZdT2k_eIPY-F_jopoxKsRmjVXK2OZRx2fH8LiAE3XJcn4DeCVDp3Z8hPUnK4oipfu2gS-89E42BWFhjdVmTs1wPCb2Y8F-JbubNGGtPg-Fm3yXPo-LIPMTCXPI4BiM-6yC5SMK3Dw6DIWvDh31rXScJPsGw0p6glhTMAK2vAoDnKb_6NUbltwUFG8CGUd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6vuGVqjnt2GrcPyFSpF_1wIXc9ITXC-Z9ArZ8xuU_pzPn3G9rox_iJVAQ3kmqMRF-VmiE8L54BofSc-SlIpFIPeQuIjK3QHAVrBxp44lkN2q5JYFocDMiRsAK1POgDxKFoEgx95HBHPufJ6aasr-p6X-_gucocXEcV3lCMQBf8ca5oqkyyfDubJ3ZTK6GEcTZSBluNKNruPg-epyF8Ul2CvyiMohH3lMqfShdx8FOXfls2hziIhFQ7Kv8oH4_OPa6o-SIj3E7jIhPH2PIr-uYXXba5MkIKu5X0Ikk1uZq9vlm_6U39vfYCq-KK2CZMi2veN8nEZfyZRZGXWWNc4Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/An_2pUkQeRblHAyI5adBc9ABOZEssIbt8pzbU4huOdyz-tYMLLXO2qIXUdan7KfDHdQjCVhoOYg3KoRrKno91zqpN315x0db4H7cr2GGnx97FSofxocFEabdzwIo_6___kPbNXOVeoi-OAswMxPNxaOe6DdQ-DbbLqXw7_s03UgC4MBQxYGVFFSDKplWslpmeKky4pKu8TV1mr0DBg4bSV3oFnw7iwi1QRfIeGQR4Mj3yDWehhmIV3gv5vSJQ7zEZ6tnz4WqAcDTOHAGpZj69hhCllR2nOObRKyc0-ekXqDts0L090UV9CFgq2EIQM2b4J1Tu8LOc4rbxaCRJM814g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این دختره توی اونلی فنز فیلمای لختیشو میذاره بعد یه پسر برای قدردانی و تشکر از اینکه دختره باعث شده خود ارضاییش لذت بخش باشه یه BMW آخرین مدل براش خریده!
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/Futball180TV/91704" target="_blank">📅 18:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91703">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69522e0ec.mp4?token=AHzskiuIprI4USxGvuaqsZqbnMi7DDRsT2aqLAeoI7Hwp4fhia4ekXpIEfzb831mYAFa_uiSMc5BbOu8gzgPEyjtzjAv0wxGna5FikYbVw2wi3hvk8OeFPEZNTJehL1MixPsnk2kyQVJ1kTmqzP1gqJ-4XL6LgjW7iGpQzMyrEkF_lVqCl82CBCTYedJ4BskboMUgK-pfy1bFDzj3kUvLQziQkhfQm1zW_6y6rFx3HUKYFZraLc5gM3F-DtKa6vg4dJNT1yqWRr1e4UMMj4V3Ubi5iGa_GWP4a-wKe9VX7F6GTkAe3PJx6LjauJogrNd6JMMzkNc8l0A5oKsWHqTUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69522e0ec.mp4?token=AHzskiuIprI4USxGvuaqsZqbnMi7DDRsT2aqLAeoI7Hwp4fhia4ekXpIEfzb831mYAFa_uiSMc5BbOu8gzgPEyjtzjAv0wxGna5FikYbVw2wi3hvk8OeFPEZNTJehL1MixPsnk2kyQVJ1kTmqzP1gqJ-4XL6LgjW7iGpQzMyrEkF_lVqCl82CBCTYedJ4BskboMUgK-pfy1bFDzj3kUvLQziQkhfQm1zW_6y6rFx3HUKYFZraLc5gM3F-DtKa6vg4dJNT1yqWRr1e4UMMj4V3Ubi5iGa_GWP4a-wKe9VX7F6GTkAe3PJx6LjauJogrNd6JMMzkNc8l0A5oKsWHqTUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
۸ سال گذر زمان و تفاوت از زمین‌تا آسمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/Futball180TV/91703" target="_blank">📅 18:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91702">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4wu-OnAWMDXlqufqhNF00n35WHCqaRp-C97gcnYtW0O-257HpZlRglLUNUti2K_8jtErOvsD9AbOsykgQbqvhKm0er4p2sEZ28X1rB8cadQMkRzJaCC9373J1j1AHx8tKWUlFvr9QvxckYKuoL1k9n1btmDpB3TS3iJan1P52317eWVedGUDbp1cOqHNsiZfpdnmc6wlm8Hip7Wnq-N4A0IRN2Xufp88ju84AI8ZiLQs3lETVoEl2E-q_1lPkEc6ohinfxKn6RRBCznIt_2xfBLOR2XBnhmFvXGgvTAjofyWppvaJsxDIl-kLAsNQMWp4QIW11YcLFISoQf9G2g1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوریییی
از رومانو:
⚪️
🔵
نیکو پاز ترجیح میده به جای اینکه الان به رئال برگرده یک فصل دیگه هم در کومو بمونه!
تصمیم نهایی با ژوزه مورینیو است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/91702" target="_blank">📅 18:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91701">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtgQdtYLCwaJErx1119mk9nhaSfhmDWc1DQ1MTg5haD-eNGQgq0fpGQ_SLTpNLMTHelqnz53pGqVVsLGDarjQfUpYxRan229yqmj0EkMBSH7Q8O1xzzcL7PjHIdYqwOv13RUcMP8rNGs0MBfU3xPq7NY4Xp2N5vgRp3goQdaJOiZwbcGu5GTvdDR_Y_lznhPlzbC9kB0bN-Ce_x1oeQAdTyZauewLEf8CbYt7YPQMIZqJcGmpjprwCthz2WrdgjxY2Pqztb58qAUQCxYU_OpHJhDdu4cqA2Cby02jprtWslcd25dVy9yRvB6e_E4cCU8b9WPpGTxjK1Hy9AzaYRyTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توتواسپورت:
پاریسن ژرمن طی چند روز گذشته افتاده دنبال جذب لامین یامال و میخواد شانس خودش رو برای جذب وینگر بارسا امتحان کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/91701" target="_blank">📅 17:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91700">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8M9_a-Re0O9XDbnfZvNUVMlu3jWQDGPTSeTIK5PE3a3FHntSX4AgUARV4apofPgIAsP2pyEpvZyAl3FCkiW8mrvJrNzKWAtEGs6PXfVyQU4D9ObuGpOg03-dDdhAeD7S-mu3hysb8LXrzYbLyAWsB89-qXqagn4My55_NiVFWcKg-3QHNWHeSZBOGC0kFPGzpfJBMJ5abx79x2q0L0hsvuUSkdhAhdxCXQLA8DOwblEHDgv35kwTVZJ85gbo9q2Eqn-s1TPr60OY7S_TzAQApBTKYIyvEopFtbQed1tBEtu9CLivZtD0pb7W54mLNZhqmWqlNgO4ttHKWdyT6RIDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
تیم‌ملی ژاپن کمپ تمرینی خودشو که داخل مکزیک بود بخاطر شرایط بد و‌ امکانات ضعیف به آمریکا تغییر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91700" target="_blank">📅 17:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91699">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fba6ae20.mp4?token=GmSgRqWp8jhfYAwoNuj5UpdkBz5rCPSwK1ZuRuRlZm70Bl1yA2PCQUu9o8bE_h3_l77xneVq60vvOCf5YWU-7OkpdqUjWZYy8eRKbakZVhZUX37uIYhFJZOeabjHyIIo0MVlzyD9BPofVskVMMNxi-wBQsj4plB0qXslJ0P2G-TlwY-HWTA724arozxy3byRbZHhiIgCRsFrG51YiZSzrRT_hb_VDqyZrKGrE-eoS6ZsaOjvSfI-F7TUh6DHxUq9Atd3DeSWZRJkZSZls6JJ4ncGNl8NfC6Tod2MGrxf8YzPSNAn2_CZG2Uva7CN6X7MktbSlmrZ_kG_WwCoaYAGHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fba6ae20.mp4?token=GmSgRqWp8jhfYAwoNuj5UpdkBz5rCPSwK1ZuRuRlZm70Bl1yA2PCQUu9o8bE_h3_l77xneVq60vvOCf5YWU-7OkpdqUjWZYy8eRKbakZVhZUX37uIYhFJZOeabjHyIIo0MVlzyD9BPofVskVMMNxi-wBQsj4plB0qXslJ0P2G-TlwY-HWTA724arozxy3byRbZHhiIgCRsFrG51YiZSzrRT_hb_VDqyZrKGrE-eoS6ZsaOjvSfI-F7TUh6DHxUq9Atd3DeSWZRJkZSZls6JJ4ncGNl8NfC6Tod2MGrxf8YzPSNAn2_CZG2Uva7CN6X7MktbSlmrZ_kG_WwCoaYAGHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو تیم ملی نروژ برای جام جهانی به سبک وایکینگ‌ها
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91699" target="_blank">📅 17:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91697">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9dyeHqB_GKfs9NwxQIiwp2YRVQOmqSxH4Su-Ju0kRHXf1YA_VnYmZnuE-4XNVDyW9SPU1ZRfg7xTKpZ6E0l5NrOlivt-dBapGpd6UlMQ--dJekRFzMUKT_IKY-sg3uFCH52Rz4Qp-zXYddBwEEJZrQd9myfFvvJh9VoXcdZXzfe04R-JidgRf0x4JEih-zILVCIv7MupJHI9w8FXyoTCRPgge2HmfzFuG5e5weECl0fJx5DxAvFofM7PzsSs10QB4JwXAd_eo2NVwpCxrzIwQIj0bWSX3sZUuuEMGMiG72fbALvvT07fveYwNnEGWPM1f3eAnvZn-ydgZGEEdvlvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmHeAskCCNQJPZ28qs8du10XasWEyT_N00-pa88QA4oNNJFu1cfSxib25QEIeQ3wQVS3napGhxxiTvXIOg21Aog4sFsjl_ON93Mq0q0j6VMLyRn-34NEeyiSUeWNPMi8RF9nmEveRZrIkPVpAanqzjwaiqYRdV2swwhxFZDZVgMqviJ2fTaM0Z1pPoLA1Pt_5zSwSCihf3qNVi2vd4L9bjYYh9MbuoM9XJwyUYT-3t7GZqWpv9Z4BBMU6iLtF9LKbsETOjIA-79Ie0T2z1bu9wmvAWNaycqzm9sqtvFRxqUj3_RunY14LE1Jjo8LW79aZ_ozVwi-z0wUuXZDJa0okA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Newcastle
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/91697" target="_blank">📅 17:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91696">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGyakcYs_iqF2Yz6tjAjl1i-rS5u-VSuIVn-VcxeiyyL2bPiunBPKO02eLSOKePr73teeRYhd97DZdVba5FkJAAKESu7gJL4aX44Y2YK8JBiXodRmJRbROpr4CI5N5wBt7nDUSsaoNTmVqIktQY_FB0DnkTVEEZaJuAdlAb0rJbz4TiTwwl5QrXPMMhkSDfUjymlmyaStI_4uyeE3tHFk81uHULIyzLthmVVHExPVQpjgyij7dWpe5rbxU1Kt06X1U48IMk2uIUlk9LMRFSIYrFHN32z_AW0dBWuhjU9kOscLY93IiBIUnEJ5ZRrYZW7jZYMxn_6aeDLIgCMW0fDRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گلوبو: نیمار ممکن است مقابل مراکش به میدان برود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91696" target="_blank">📅 17:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91695">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc3ct75_ftNgaUXh4a9ZmO1Kc6mjAwmYHQbs9eBUq4vRa-oip4CHluR7P21ZHKQjij-xVBuZXwcty79YkbkqZE-7XmZgrl-8ie_PEJBexOyraoJC0GGif9pBiuLIRk80fzMiruJ_YCVXX4QOA0ekN9WkjMI2D8vvG9sXlfomq0W3nBpPcyEuAEZwS_Pn0h97EPTY4CiNttplS9VY-YmqYGfqPe3n_fJaIVFtYCthdonSt2FUys-NAZopINmBes75xTV9rp-08xUI3rwVfxadrHLwcNly9Y_SiYXFuifusKqgDgAFV6LynS26XZS2yXqnSbi5nOYAsDQGuYvtWFd_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: منچستریونایتد درحال مذاکره فشرده با وستهام برای جذب متئوس فرناندز هست. رقم درخواست وستهام ۸۵ میلیون یورو هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91695" target="_blank">📅 17:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91694">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jY8SFNV-UibqR6rPQiLE0gBOLREdB2_1fTnbf2MjdYXrXW-QR55acfjc2UD9aXv7I2HnXSg2FVyYXT9L6gUPWpgAIqWwNwm2s_f2ZqIkcYACSN6jIuUJWnoh6UVAWNocBaYJrQVu7fpy13_49j95Ru9o03Xau7GyMaOF6_08NBQZYJg8s1kLZQ8IBiPEZKnt8N7roAuzawpW_oHhDBzW9w7vKFDNXHa5hNEGhBn5SSDIFa8sUsN1tu2KvQyrTdRNE0SOtNUSkY-vwvitublFE4XcPKduvFnK7P5M0SAm78avBVBHvP14UkCCi18PT6S2z-axPrFzUQ2FShffWp3-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
⚪️
رومانو:
براهیم دیاز میخواهد در رئال مادرید بماند و برای جایگاهش سخت بجنگد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91694" target="_blank">📅 17:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91692">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bp-REOOU7t8FX3b-bwd1wwxeP51_FgQxUiZsztwyWVq_AWHy-rH_ZQqyjbdHRmVXZ0A7Eqx0uHi-qtYYsdPuvHhQV_fQ9ANV2A2tEJG-dH2qLehNkJRaS3ac5L9JYSTucziF_OIjRSC-Lapu8dqdcnpbOquFYo_-o55clkpzN0vN5DDKrqh8g4ymyUUJtZUrIA0YxFqaDQhotZQ6WYowjcuE7pPwSap1tyibTmSi8KEdeCx5VN-Qrko25MBbG7cbSPFpYxk5j5x_4TvKxXGDvd55_8lVgtsL2MeYJFtze-SIL8VR6rqkHxzqn0EU2w4drXYQn6CwJD1X1wDDT1niUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYfXNifr4TunRmYHvDikRRGHHEwLdAF8A-eesclgd3nzbzcovaHqazDSQcOq6ptjqZ3F5OPe2SODkQ3N6fUE_rllpusDOoDitwrfoITSpiDekG_3rH4XLATHN5REc7S5d-UZUEPAIBskazB99Caeh0fBGOK5dC4gGwOj349pqexXy_doFrWCjcBjWXQVMMn6F4uS5Fd-P1A2gSFL73dWOHAviHGodpNSu4UgNfiKvpig8N0CuqdKv_el6CaMTdeWvTPxNcICLvdG8vTQtcUqAxaW1LInX_Qh443eynaZyJgvyFabSoTHXKBpPkYFL1x9yE_Mwms7H4pQw7t0Xc7xTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاینات پزشکی رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/91692" target="_blank">📅 17:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91691">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
#
فوری
؛ پس از اعتراضات اخیر دانش‌آموزان، تاثیر معدل سال یازدهم در کنکور مثبت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/91691" target="_blank">📅 16:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91690">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f1cc690c.mp4?token=gZJB5BIfFh-0pNsmD7S5cBXfB9UDcgGTqQfkncDTfzXdny9OfhUg4Om97Zv0f-H7mtaBlJ2LWAYaqgECyffVtngk_jP6lcVvWTuVm3AT2iwllnMtqBu6hizqtpHi6-E_Rj-X7YeefKefDhwGOPluBevjeNlOXxBsZRqIWA8WqTqGUU6z9PRtYltpYCDyTuG4DzXMfEanOiTbMfUII9iuOqWIYG6YfxvV9vPOZeXny5c0RDpOkxET0m0HQgh_5kE6hk93ukrjg-yHFjyLVoyGKHrh21IvQtEoB_i0dWwZjhwqSKkHDEFZMHZLNb7Dju2DPUCsjWASfGuKhpIjJk-kIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f1cc690c.mp4?token=gZJB5BIfFh-0pNsmD7S5cBXfB9UDcgGTqQfkncDTfzXdny9OfhUg4Om97Zv0f-H7mtaBlJ2LWAYaqgECyffVtngk_jP6lcVvWTuVm3AT2iwllnMtqBu6hizqtpHi6-E_Rj-X7YeefKefDhwGOPluBevjeNlOXxBsZRqIWA8WqTqGUU6z9PRtYltpYCDyTuG4DzXMfEanOiTbMfUII9iuOqWIYG6YfxvV9vPOZeXny5c0RDpOkxET0m0HQgh_5kE6hk93ukrjg-yHFjyLVoyGKHrh21IvQtEoB_i0dWwZjhwqSKkHDEFZMHZLNb7Dju2DPUCsjWASfGuKhpIjJk-kIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دیروز وسط‌تمرین یوگا‌ کف تهرون و صدای پدافند؛ چه ترکیب متناقض و عجیبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/91690" target="_blank">📅 16:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91689">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871f3caa0a.mp4?token=OpusWXNsfyLXbgnb2YaPHVI7gSNZ-H7aym90QNzXpRlwKYjayFaFwOrdithf0_UR0FAwWCjiw4iiBvCYXiATd0EBKyFM27UNlrCes9JHcqUEr1vl1sKN6uiPbfrlErdQl4tbpplVz14I4ZFfsyai9sSUqS8R3FFUiqdu91-RFykw5RJzmpa1zyLqC4kY_b6ykOQ3ZT31LMJMTNd1jpElblCiBThf72fCg6k64lWw9OnSVL-Gf-F3VqgQ5cEz_dJelXUvBbKZ9i7Jqy0-pMYk_6fsr69AVLUpNGJvZs9Wp3y_WsxiW5s9s8m7jXrK_a_yY3uu5ujP3UfQh55TrSrYZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871f3caa0a.mp4?token=OpusWXNsfyLXbgnb2YaPHVI7gSNZ-H7aym90QNzXpRlwKYjayFaFwOrdithf0_UR0FAwWCjiw4iiBvCYXiATd0EBKyFM27UNlrCes9JHcqUEr1vl1sKN6uiPbfrlErdQl4tbpplVz14I4ZFfsyai9sSUqS8R3FFUiqdu91-RFykw5RJzmpa1zyLqC4kY_b6ykOQ3ZT31LMJMTNd1jpElblCiBThf72fCg6k64lWw9OnSVL-Gf-F3VqgQ5cEz_dJelXUvBbKZ9i7Jqy0-pMYk_6fsr69AVLUpNGJvZs9Wp3y_WsxiW5s9s8m7jXrK_a_yY3uu5ujP3UfQh55TrSrYZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ازبکستان روی سکوهای استادیوم یه‌ پسره اومد اینجوری از زیدش خاستگاری کرد که دختره کاسه کوزشو شکوند و جواب رد داد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91689" target="_blank">📅 16:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91688">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9aa48bcb.mp4?token=AquwbKSTQZQlOGUoyj0cA4dHrRXolHGierK0WQdFzRX_adFZsS6X__YOdyjDQtlreGNaTZuHjyY0OjWX8R71c18Ec2_fd7jP5ZvEhDxaHBmX1ZnCkayyHwgh8HYpv1AVHE3Yp2on6AI-YLffpIHu922x8f_HuA6ZTRdOJ-_-v77ha6PV2i0GM5FF7G4w78cVZBLfA-zmGcN0abOFkSRs3sqF9zEyfIzF_XE8xsNZNIKtX6rvGcJdreCxYKcSOlbyieoXGJEbbw3WU1XM7Iub8tolvlRe13Tzug9UR-NvKoIRmfHw3kNNyc_rMPjRfDU_-Sug8w8VrEijW9JvmaFsUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9aa48bcb.mp4?token=AquwbKSTQZQlOGUoyj0cA4dHrRXolHGierK0WQdFzRX_adFZsS6X__YOdyjDQtlreGNaTZuHjyY0OjWX8R71c18Ec2_fd7jP5ZvEhDxaHBmX1ZnCkayyHwgh8HYpv1AVHE3Yp2on6AI-YLffpIHu922x8f_HuA6ZTRdOJ-_-v77ha6PV2i0GM5FF7G4w78cVZBLfA-zmGcN0abOFkSRs3sqF9zEyfIzF_XE8xsNZNIKtX6rvGcJdreCxYKcSOlbyieoXGJEbbw3WU1XM7Iub8tolvlRe13Tzug9UR-NvKoIRmfHw3kNNyc_rMPjRfDU_-Sug8w8VrEijW9JvmaFsUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکم رونالدینیو افسانه ای ببینیم
❤️‍🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91688" target="_blank">📅 16:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91687">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/813a70ddec.mp4?token=PDpslp62kaY9sNEvDmtIhe2ZfRniig8u3T5UbjuaH898L9HDeOVx9UXgHxI4etRR241LnM3Eg6TqRKSMdYfkd84kpfbqep9FxdevuKgZQLD48bIWyL8ysDdV8rxXdLU2tlVK-9Vh1igNsMdiMb9ktyGPBTsKleSksfzWA3ou_gPahj0pZaralGgD8XURK7aJ4BeW3xQckClhIMy1Zz_R7uWt5q4czMN-F--lCyLSglhwPA4hf97G-hVIalZaIjCOeGHA8TCroinjJUnARKX4I5aguXv3Qj05cBOVjFala2NV87Wy12_OmGB0D9vdlInBp5EnO7jf-6xG1l7-mjIBrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/813a70ddec.mp4?token=PDpslp62kaY9sNEvDmtIhe2ZfRniig8u3T5UbjuaH898L9HDeOVx9UXgHxI4etRR241LnM3Eg6TqRKSMdYfkd84kpfbqep9FxdevuKgZQLD48bIWyL8ysDdV8rxXdLU2tlVK-9Vh1igNsMdiMb9ktyGPBTsKleSksfzWA3ou_gPahj0pZaralGgD8XURK7aJ4BeW3xQckClhIMy1Zz_R7uWt5q4czMN-F--lCyLSglhwPA4hf97G-hVIalZaIjCOeGHA8TCroinjJUnARKX4I5aguXv3Qj05cBOVjFala2NV87Wy12_OmGB0D9vdlInBp5EnO7jf-6xG1l7-mjIBrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
الهه منصوریان بعد زد و خورد شدید و فدراسیون ووشو: من در برابر بی عدالتی سکوت نخواهم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91687" target="_blank">📅 16:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91686">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ea15ec78.mp4?token=XH2zYA1s6_U20oJ_sZxsYpoNywjwMGMMdubwJtyM3sPqleTP9RXEccVkqHhhGYrxI303b_8YkVkqsy03K-ri20gPigToRVI6QcMu9azB6LVFPi9GQRBsnFywO5MU-1fD1t-s3hoKYe0_vtgvIftpQ0xbd9YIvxxl06LFEZjmR8-vGco8gpmuH2xXr8oJEqI6VJIIS7p6IbQ-fF7n6-QFmu6U055E41KRSDwtU_45GvH9lob0zM1vBovWOU0TK8K8-AN2FT3XPrsa21T3OlazsYNJAntkvUTTI49f8-lpZCigMPEjJVW_G3LyYegPsYjXtDkJUTJrdWjO7c3IJh5UNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ea15ec78.mp4?token=XH2zYA1s6_U20oJ_sZxsYpoNywjwMGMMdubwJtyM3sPqleTP9RXEccVkqHhhGYrxI303b_8YkVkqsy03K-ri20gPigToRVI6QcMu9azB6LVFPi9GQRBsnFywO5MU-1fD1t-s3hoKYe0_vtgvIftpQ0xbd9YIvxxl06LFEZjmR8-vGco8gpmuH2xXr8oJEqI6VJIIS7p6IbQ-fF7n6-QFmu6U055E41KRSDwtU_45GvH9lob0zM1vBovWOU0TK8K8-AN2FT3XPrsa21T3OlazsYNJAntkvUTTI49f8-lpZCigMPEjJVW_G3LyYegPsYjXtDkJUTJrdWjO7c3IJh5UNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بازیکنای برزیل یه دروازه خالی گل میکنن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91686" target="_blank">📅 15:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91685">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e53jS1xeuk1p39ptdh7JEk7Yu1MltsMK-ZZaLb6CxiDUvmU8puJ5cCceS4-sQSiazdglFGSx_lDqww7wvbUFdHIB6uZSnUrza7ecNWrEt0v3uBaVza3pKOa4Le_tI8psjQ-Fmo261JzHaGRcPjr9ZJKSqnA4B55BFvoTUF_ZWJahWQWnIXA7lLRNPkXCU5envzXAUldaq21Z3ZPAeJfv4t8xwtyZZENzFZRkm4Kh-AaRcVeE0h1I6ET0lQn5o_vC9sxKTipu1S67yVszT7ctl7UCjCB3d_PuTSLXJ-b-A0rmEivjpZJbbsyvFFm5p5pf-oaedeht6dKzMcWQBuWYrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مورینیو وارد مادرید شد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91685" target="_blank">📅 15:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91684">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd169632cc.mp4?token=YwFJGaTot-JwcnuEEOuc8qtK9onwha8vRV07WHn4WNXJ8vn7DFdmrF0XB_5G2WGqr7RrBYo1BIxdjXDxg_PK5Ef0uxlO5eOf9Sy1YdjEj64P3KpwJTzmU_9E87zHXjE0y0qxPpJKCeZ8tguX17QBgP-S_JkYRDqO00r2jcGB6V9Hi26SCPT6QTuazk2JW7tSEGDBkPQtURDLU3YGKCwUtbwQJsW-wiY5no1VMlRG6-m80XJqKLkwiUemTT3osrSFnBTZOVp60y1imLno5RtAzJ09R-gWlmqi56f0ccHdXOzHBdZgOAg4zmBaYbWc7Nh_gki4ithNOPJaYzIqgdo6Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd169632cc.mp4?token=YwFJGaTot-JwcnuEEOuc8qtK9onwha8vRV07WHn4WNXJ8vn7DFdmrF0XB_5G2WGqr7RrBYo1BIxdjXDxg_PK5Ef0uxlO5eOf9Sy1YdjEj64P3KpwJTzmU_9E87zHXjE0y0qxPpJKCeZ8tguX17QBgP-S_JkYRDqO00r2jcGB6V9Hi26SCPT6QTuazk2JW7tSEGDBkPQtURDLU3YGKCwUtbwQJsW-wiY5no1VMlRG6-m80XJqKLkwiUemTT3osrSFnBTZOVp60y1imLno5RtAzJ09R-gWlmqi56f0ccHdXOzHBdZgOAg4zmBaYbWc7Nh_gki4ithNOPJaYzIqgdo6Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گاوی اینو با این افکت صدا توی تیک تاک آپلود کرده:
صبح بخیر عوضی فوق العاده؛چه حسی داره به عنوان خفن ترین
مادرجنده
دنیا بیدار بشی؟
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91684" target="_blank">📅 15:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91683">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIJrIwI27FJyq6hcvCs_82c_A3HJvpf10BjR94VdMa3YyvvQbOjR1fd36fH6qNBtXv8azTOXrV-c1btUdmMWp5U7CCiS9sR4lxfwrAPn6lfq-7RO-oUIQCdmIfz-D4es0kSVUfVXnFioKyyBEYqh3QGlLWuHFd2Vn0BXd0IXx2RXPwdMUj-xe3WtHP4snayFyZgDymgAD3PJ5NrX5IQtjeV8TY5a3rbzBTUSCl0ryeFyenvAE4nvtVrKINAe6-zGIxXEY3JjBT6obDL4Jl2p4m0YhJ7DwgyJHl_G9otW---90fGWNUW5NvsXiBzynZAiArajE0EXw29vFdXdeiSAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔻
خوزه آلوارز خیلی نزدیک به لاپورتا:
🔻
بارسلونا همچنان روند جذب آلوارز رو دنبال‌ می‌کنه. ۱۲۰ میلیون دلار حداکثر پیشنهاد بارسلونا برای آلوارز خواهد بود. مذاکرات در روزهای آینده انجام خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91683" target="_blank">📅 15:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91682">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-vtG75SMfXcpAEMkXgUXOEWWQL3CFFY083zXf7qfvGEc2JFlCKxoSIK1nHMZ6vyS5oEQVrIFVnN1hQsHF94_YkvWTNXeOYJJF1576LrUx5nVcKVhbyCgBcvM4PsgDM0BHGYCGQr7pVsTragNN31u0RSJ9ReTqPGHholYEsyzjzIWryEfGCfY3C6I3Bc_PQyOQnLySoVo_jyoU7q1gUWLEm-bleA4cqs-VasDWyP_hzIUnJKUtr1ovudDD7r40__WzVn9jBOnRQFmUudhI6ATrGCP5Bj2KOeq8r9__LAXfi-8e2ScHXG7XN_a9ocUhZjnziHnQ8m2nUHWz96CWGJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
خدای جام جهانی؛ زاگالو با ۴قهرمانی جهان با برزیل
🥇
۱۹۵۸(به عنوان بازیکن قهرمان)
🥇
۱۹۶۲(به عنوان بازیکن قهرمان)
🥇
۱۹۷۰(به عنوان سرمربی قهرمان)
🥇
۱۹۹۴(به عنوان مربی و مدیر فنی قهرمان)
🥈
۱۹۹۸(به عنوان سرمربی نایب قهرمان)
🏆
اوبه عنوان بازیکن، سرمربی،مربی، مدیر فنی قهرمان جام جهانی شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91682" target="_blank">📅 15:20 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
