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
<img src="https://cdn4.telesco.pe/file/IZgFYV1Q5_nQsn5dmYSDx0WQtMMPmzET3ggE4V01UXwBL_JYrkByZjdAuPFLjLJaLZqReprC_SWaTF0_bx_-NOCIIH35g3u5HUWW_EYSYd4RGwVQWW7Dhf46IUhE2JPatGZbiWMJ_FkRwrONoDFoc8XwVl9lWxcHAduYSpOm8xlAturOYXY-dP7uABF9ekzp8mhYos_jwrgT-Ov4ZhrYiE-x423BbxDJt6MWTJ98DoEL7bJX8hgvMsLEQTVJl_cJ4jk-RXM0WI21svxAggVfQl2uwxWzURDPVtBJF32-rGLhFlNwetOspN0-fDKED8vFL9ElkURnoIc7XZ228G1EvA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 125K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 23:28:31</div>
<hr>

<div class="tg-post" id="msg-90253">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsjaYvtQcrNXuEXtUjP3r392s-b1I0c8pNv70lLZOQORh6soYezQXLs3GDtSRyW2amFxf7PkN6yOxlm0j8MnyaXa0-wlJNh0CxBdPuE332I9qVXKWYXxackOUfeiQmU9UwwFxDOm7MXH7j1Amm0VJoifIhZPjIfZEFMZ2zwLA816q_-Pio1VTq6wil3lgaSMVP8IIqmrY28d2iYLkxbijfRYm2N1v1-2xrCp--jbsvokOZhCNkmg9CIEqJVIDxVH37KNEKLTIOPoXwqookXPMZ26DmIS1lcIIgjtDy0zzFXPGMKb_7gi8xuDUq6zjVCGhepev0eBThFr72EmikXixQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الکسیا پوتیاس بعد از ۱۴ سال از بارسا جدا شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/Futball180TV/90253" target="_blank">📅 21:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90252">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea61c87680.mp4?token=oXP73a7yRfLXcqW90WVqm4UPDXJdkm6giFjsb46Tgy09fAztdRKDbvIGNsw6uF8k7Ws6zFsIMYkzWAwhqxwmkeWyPvknnBcA48I0KNz8LhHdqyONeAUFzz1cq-EvcXA_bifD-4HdbXQeisFYyA4iUIeNlvC9jHWurP1p4WvmH_wJLq277Fl17LmCTLES_cJRY7CIk4-7JqyN1rwyWjS1THN5ovPy1Km8lYKYua3C4WyEWwYAvbj53sdd94wcQ0OOih_YCZa-smf4YYBMHZyUkxsBPOywI8YL0Y5o_rmTNoQeUtVHE1VYXk7EZzbeqMi_A77NT5ok41WtL7YAd8MTdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea61c87680.mp4?token=oXP73a7yRfLXcqW90WVqm4UPDXJdkm6giFjsb46Tgy09fAztdRKDbvIGNsw6uF8k7Ws6zFsIMYkzWAwhqxwmkeWyPvknnBcA48I0KNz8LhHdqyONeAUFzz1cq-EvcXA_bifD-4HdbXQeisFYyA4iUIeNlvC9jHWurP1p4WvmH_wJLq277Fl17LmCTLES_cJRY7CIk4-7JqyN1rwyWjS1THN5ovPy1Km8lYKYua3C4WyEWwYAvbj53sdd94wcQ0OOih_YCZa-smf4YYBMHZyUkxsBPOywI8YL0Y5o_rmTNoQeUtVHE1VYXk7EZzbeqMi_A77NT5ok41WtL7YAd8MTdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش ناصر حجازی به پیشنهاد گرین کارت؛ آمریکایی ها باید به دستبوس ما بیایند!
همسر مرحوم حجازی: وقتی بهش پیشنهاد گرین کارت آمریکا رو دادم چنان فریادهایی میزد که ستون خونه می‌لرزید!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/90252" target="_blank">📅 21:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90251">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90251" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/90251" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90250">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFHiFk-5QS-c0z-3t3otl7d6bVIPiWprqOgzenRHv72gIdxosxbiziDORJsKwdMdEGemTqPfUniTgw94CyNjY0kgX0PHdMHMWIt62WbHllPCvpVu41wTsDwk-fo08rem2xy4fN5SuhELaBgDPlooojwzVo13Qi8TH-mTuog0DN-QXFKmqcAwO-bIzjP6Pt6qAzcBVVMcDgTFkypV0z81eMpKrT7TxNG0IF-CBP-V5GksFi8Eg2ILL06hTSxbmcUGoBi2cBDYvjktL_UsU9Zuwt2RqAygBO5oCHhZ_DFl4211nScTy8uilkwG-QtJJU1xw70jfiTTa8GbqfcUacAQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/Futball180TV/90250" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90249">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baad93a3a8.mp4?token=f7fLfoLQsOl6ygnGNpIQidxjIjtiXpzUkz6lLUqWuC30kSAvLpUKl6PoQn1Xgq5H_P-oDLjKZaP8QwHfHOLNz8CsLV-hb5PLu6bn3r-CyqBmcHIECP07oZH_JrjJTLXCp6c2isn05HuOuYBkXe1gfrzfIEI8yxOllPcrMINsm4HykjObaU9mNUnjG4bZTpa3LMjl5MSw_EF3P0fp8B98VMfLeYDD3EaXlU0oZK78xk7wuZMSxRhcBRyaUILRzTF_Hs68N7nkpY1LemW0KabcswHaTJcyNcatFY07uhZJLTw84GultCgA2FJZDrvRQEjd3SwgUSQAtot3whA2nwX0_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baad93a3a8.mp4?token=f7fLfoLQsOl6ygnGNpIQidxjIjtiXpzUkz6lLUqWuC30kSAvLpUKl6PoQn1Xgq5H_P-oDLjKZaP8QwHfHOLNz8CsLV-hb5PLu6bn3r-CyqBmcHIECP07oZH_JrjJTLXCp6c2isn05HuOuYBkXe1gfrzfIEI8yxOllPcrMINsm4HykjObaU9mNUnjG4bZTpa3LMjl5MSw_EF3P0fp8B98VMfLeYDD3EaXlU0oZK78xk7wuZMSxRhcBRyaUILRzTF_Hs68N7nkpY1LemW0KabcswHaTJcyNcatFY07uhZJLTw84GultCgA2FJZDrvRQEjd3SwgUSQAtot3whA2nwX0_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازبک‌ها آماده حضور در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/Futball180TV/90249" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90248">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yvp_bRKf5rSoZnkPqyyb_SLKn8SMPgWB2FONvjUNRu4mtwOJ0g4uhF6Oojv6h1Gp21gcmBkTcTu_CiosdFmPAOCBf0XdBj_lt1IcoEnzQvNDhN452hrFmOFPsrbcPSAI8FLQ3XvxqwEWpuLpQ2ifoBd1P8uNtiyX22b5Agzto1K3SnwrmwVFJMk8tqGageM59IoYjjLBwfo8PUIY2jQQNoMopfnL_CY5JA2YpOunD4BldiHaCAVcHEUKztjhctMmwqpThac4igOavQnQBaDW_WRQchwTRuCEe9w-7sV6vouVdQQbPWwDR2P7UcfGBO_zRS4RB8PUrZmLWRrc9s9yRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اعلام رومانو، قرارداد آنتونی رودیگر با رئال‌مادرید یکسال دیگر تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/Futball180TV/90248" target="_blank">📅 20:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90247">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🔺
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/Futball180TV/90247" target="_blank">📅 19:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90246">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niWTgW7LtW2Q4b0unV5XEkhOTTwz36IEklDrlUGtBMWPztzYdybuFzd5eFqULS7KAiINklAXuhH2DMkuM-A5a10upxBZqhXc5bwV557N4j7OYpG4kLxHeAvC5OrFog8-m-8T-ZEwpSPKRgFgoZoemnStMLhWTGAJIsT_YM68_-REs-ZiZMJXIhZrHLhorMKtT1Wdml3HGc1ILmzW5aCLLxJJJBTg_bR2v-J3dElA9wx3WQSYfeoROG8aL2K7-kMuZieqaFWzntdC0PkW8cxOAkVHweJIW4XoHl5ZZDyuVTn_MNiNVD5kkyIqHpi6g4Avd76kgReoZybealISAembbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیدبندی فصل‌آینده لیگ‌قهرمانان مشخص شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/90246" target="_blank">📅 19:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90245">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تا ۲۴ ساعت آینده سطح دسترسی به اینترنت به حالت قبلی برخواهد گشت. درحال حاضر اتصال وای‌فای درحال بازگشت به شرایط قبل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/90245" target="_blank">📅 19:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90244">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تا ۲۴ ساعت آینده سطح دسترسی به اینترنت به حالت قبلی برخواهد گشت. درحال حاضر اتصال وای‌فای درحال بازگشت به شرایط قبل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/90244" target="_blank">📅 19:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90243">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbyxTqmG7rkw-aB0CI_Y33FF93gYMV_URbGdBsGVs1i-Ewz-MdhzrmeZpObPjJkFJHbqvqLBxkT-sa0SwMKJESgc4T-xGShGEWYy8BnFFD1w1VNztuOTts3jZRfXpyoWV22VM6N6QGIQ6RxOCHJErjjElXTVNAk4nDHU_KTGqz7Ohn-cUtXAwao-1Otsh1CWQtVEhsXXoUXACQS5ztgdEG7LRrnRwslw4hUIGYHJnX51H0Rlaf3JdumeanCLUC47GvDmLhfOA9ctZXldE8BPt8TO6mpW2dOcpM9fgBjPB49d9q98ccxZjsUS08hTsHhNQ0KXvi5KcisgD2Tsr80CvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ‌فصل 2026/27 سری‌آ ایتالیا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/Futball180TV/90243" target="_blank">📅 18:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90242">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtPVb823pNJV9rPvV3rp1LEXk36Md0QnFpz0cY367RLb5giKv5u7MxnJKLTmK1wxwaydW1LgQxGU6gDDRNj2kQUWNkUNAtmCIBtJ0o7xhBvkfBOlhR_rpTwcF9IHuEt7NflIbRap9OqbyFHWgs_6EM9LY_4rt7XpKLVJxcE6ZCnE7MPJBGp5GRpJfaApEhuSFtZiJjJXBV9VawInL81n1Z6urvYC_DXZvJSkWndVMDVxMrRAaRWMfI4wpK5jLoOKpBZU8rYkWc3TYm4AU1lQjDoeJ0S8gHaNfMJ3LVsTYa6OWOSHiGxDCUnMHhqe0xxLPRo8YoJe5XXiZ8qhRw88Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل 2026/27 لیگ‌برتر جزیره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/90242" target="_blank">📅 17:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90241">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxT6aj6UXE_F93jeoilM8jP4El7OUgoLdsbFG20Mi6mV8KYmTDvvsnbA04pXSdpDa7WfW8AKaJ3c1pDtRG8c1Bf6OejUKDBHSqDPP80y4Kq_B9Ij76HkyoUc0qP_DBF2QPjnxG5VgwPw76stp-1LN8t8oE1Gxrg4hvrRZXVoFJHebfp3G5Tabd6eW0MTJZhpxGgW814gqgU351cMO38GXrFP_wu9fxIPAMF01Wtjht8IUFBSwmQEioXYaD-8ugTt0cKt0A9lCArF99O9MArjVgJTBzs_oO-nIWqKRkzTGlCCccmX1b3Q3ju3MD6wcTd8QInWBF8e8Ps0X1tcuudXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه بارسلونا برای جذب آلوارز پیشنهاد پرداخت ۱۰۰ میلیون یورو + مارک کاسادو را به اتلتیکومادرید ارائه کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/90241" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90240">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdLJdzcvDyb8E0n8Pr7FH1jNHQ1B6BHJwX98nK6ZVAuf7EyvtzbBIaGW-5J0QYK9xqpaqdih2Qz3VoftFEW-QdnA0sdLqD6AsomntC6Azr35TuodTAdwEiJ0e5QSApDKqTNA35jFG9vucaSoud3Hpvfb-pn7BRQ_rHobPn-XDSX03SkyLj0N2PXMj5HASomUEwQ0RJvFvb5cK8WXHxM_arJZXzykXc7vKFSv_Q-QBHql8beO3eJ5qVN5npcdrwT5ltIsyMT3VzRAzunFWM_OdHj4dwgz-OabWs_deIYZdj5yhm6_QcYpTs9-DBnCeaWoP61Xu6iJ0EhVPphAQgztnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ ورزشگاهی که میزبان بازی‌های جام‌جهانی هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/90240" target="_blank">📅 17:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90239">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0e6MZtwTp3OsNdu2ob7pqlesHH8g6uCYZJidgSawb88rOB_buoUAh8RqDcviaiJ6PpbYS_3cW3i5PsDs8XCZTx79xBZwCdyED7MGS-jL83HCcAHGoQfeSKCF6qHR6hVxwD5nMHV9DOhaivDoQdbybpFrjQP7BELDWxIVh7w7biRxJL4PzY07mruF5HDWgmbylSa9DfDVSgaZKyyEXAuMOELMeYkGw89HuJKSJt0sfrRolMGzAoqtEreAIreXgrogkf8xCBTPB1W0kUZfz-1t_Sq_cpnNsEY0weD24NfCw6KENbQp0Ko6ody4coKe6YCWGJat-FCyBqS-lQ_QJ0hDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمدرضا عارف معاون اول پزشکیان: اینترنت بین‌الملل در دسترس قرار گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/Futball180TV/90239" target="_blank">📅 16:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90238">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مخصوص وای‌فای :
https://t.me/proxy?server=87.248.129.199&port=25565&secret=79e344818749bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/90238" target="_blank">📅 16:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90237">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4MOMxwtYBQA74Uzo5G5h9iOA3dthJGRI3rk5XmoQE13PjYVNJFQqDO5keUek80MiqmZ4hyXf45DR2ntz9dXKC7rk4qG3c4qZyvk9jKDuD2iSQmddrapleJbGZyzUIft8NKQKT1D4GXCWVTccMHjVCft-KysvFeuBTIEKcsRSMD6-7LDGdyXzT5yAMgstgH54rgsPRp0goyJW7s49wNmuQA4mq41ikVSMtSf2F_qjraqXc21YsK2ouMc_0cVX4u5Uc36uwkhY6UNrHknn56C4CfKC-D4vndZdW7fu-1vHnfSuysTUs0G5TOGJKF8rzOQnqwUIfm67no5T80DyEdWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/90237" target="_blank">📅 16:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90236">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGL69um6NUdbpOTiZCih067x5jPAMApR-ZbO_K5KuaXhDNGk9A4AAdW0fc5YTXU_PXvfWAGuSLmywTt4uhL6MBYObqw_M5OTOzEcyLkIW01sKxgY-fGeJY55oNvzztProIW9x_FnkIIBvczYZPSPByoyCp34O_wXxdS2-PBc5PoMYFZgiIlAa9JkcGXjtbzM3nKxPyiVWfXn_CirnTQASR8dkNyf8hnzADKv0ysVtrt-oKZmHdxPLS4aSAQyeejoVssNL4kogpEEEV934cW0KYGspkcRfZEhe72zGVSpIwoEgNSMJH6sSUeRfsoNXST5qdL7w47KqYRbLmjpxolgHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور خوسلو در مراسم خداحافظی کارواخال؛ این دو نفر باجناق هستن و با خواهران دوقلو ازدواج کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/90236" target="_blank">📅 14:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90235">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQk1NKMDRFt0J9nq3ByaSt4-BpIeIhX-iNq_eTJ1V_sU2TJsApkwswQUu_hqQ_Af8BXlO0ZapHwo6th9oDO8VCSCDlG7hErFl4JNPuEmfQ3OQkKm1rSBweY1xHUVHs1vCWWTyEReri79ENsdhPxDDNjxhWtD6lrRt96usQZK-0qGRTWrKLrTzsexXtlTv1qtMFZu_RP-FDHvtoLiR4HCf3UOMGz82oRy60W5uuQ2GNAGDtIoCKrxzgtFhC9eDAyqaMwI-MKC22fYca9TzDAVqEcYq4EmPZ7tCV3WDzKUG-rw95yfqNlUEu3GOObnkefBi5cka9rA_oFoWckEEF6wgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این ۴ نفر، شاکی قضایی «اتصال اینترنت بین‌الملل» هستند
خبرنگار «انتخاب» دقایقی پیش کسب اطلاع کرد که ۴ نفر شاکی حقیقیِ «توقف اتصال اینترنت بین‌الملل» هستند. این ۴ نفر که گرایش سیاسی آن‌ها کاملاً مشخص است و تحت راهبری یک مقام ابقا شده‌ی دولت رییسی، دست به شکایت زده‌اند، عبارتند از
کامیار ثقفی، رضا تقی پور، رسول جلیلی و محمد حسن انتظاری
. / انتخاب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/Futball180TV/90235" target="_blank">📅 14:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90234">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
وزیر علوم اعلام کرد که تکلیف امتحانات پایان ترم دانشجویان کارشناسی طی چند روز آینده مشخص و اعلام خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/90234" target="_blank">📅 13:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90233">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
#فوری؛ سیتنا:
🔸
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا 24 ساعت آینده
🔸
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/Futball180TV/90233" target="_blank">📅 13:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90232">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOtnfsdVBul5-2aq4i4MULShb6MnvLTIk7yAmMacvi_mDAgL-Quwr_T2fxC_Debv9XxhmpAgaWi5RH2_M2T493rA7I2_2dS8JhmJh1QSBQgCbDZgKoGbXdY5OIn46lRIKFAQVtS1nxiRR_j9hErZWxp8leVY7aY0dbGNMrJY6Dl3dOyXfl5OFw5CLT8q5boQO-oaNBR590WVENsFACeLt9YLQHjxVjkbSp-Xe70on6QwlELhffLv8v_IpoGqALCrJWVEoPCRXZCGm_DEtmkI_nXxqy6v53jJiMBZyQXEt2Sb7sX2rknzpTrnc16u9bUEFtkEMDpGyQxPdRQjy6w0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ سیتنا:
🔸
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا 24 ساعت آینده
🔸
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی تدریجی اینترنت تا دقایقی دیگر خبر داد و گفت: دسترسی کامل مردم به اینترنت تا 24 ساعت آینده میسر می شود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/Futball180TV/90232" target="_blank">📅 13:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90231">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edb93becd.mp4?token=qdNxl4TOTlfXIlUHBb1wGdwG0wPG7Mqn-sHVjr0WJjDXmUcVv7EQ2zo_unGTbOS97FJ59z1Ca0qvHh37ONCB9i67ERtPC9paMXHAm3Cg2m-3oVStOO32yXuzbv9aIxNZpaI448kU0k40o33tch7SPN7pD_Bn-bf_VAcdp6nA_SkwoVfpxCYOKo8F3xINXQpMiAqD9GQg2KC7kjjotMggZw9D6fMNPHrpVoQ1ul0mJTpxY0Y6gvMODs8ep7Yv4OKbSc5d28kkMYC_wsjs1SzdCgKD7w1LlQa471_XChgrS2NgV5LivUBmb31NoluZDffk7nq-niUp6HN2tEyEkwJy_hA1rkDa2XyWwnFu58TNInWy6T6KDlZJR7i6Bz1Zo8Rhbs9lhlaTLU2MGCwm5idfVfyo7enS80SI9m213DcsK7Y-pzV8LMqjx0eVZHAMh1lySb0NGAwxolz0CZt9aylzI2D9LSQQwOHAvoOSH4vIWQpGGhx-cpS_nyrqo9qQHo8DQlgeAX85bKAl_DZx3bf7qXXPtcRo5HWFk06E7QR9pCM0IlDVf_Lf2MDuT01zVnJpCQDG-imtZSRLaJbs5D1UIHGwobTaHUns-FbZc5j4O7JvMKG6FWOk-UKepFQvHh6qK1v0GXptzhphkaHDxbXB9w-u9c97DNUNdIPe48EqSzs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edb93becd.mp4?token=qdNxl4TOTlfXIlUHBb1wGdwG0wPG7Mqn-sHVjr0WJjDXmUcVv7EQ2zo_unGTbOS97FJ59z1Ca0qvHh37ONCB9i67ERtPC9paMXHAm3Cg2m-3oVStOO32yXuzbv9aIxNZpaI448kU0k40o33tch7SPN7pD_Bn-bf_VAcdp6nA_SkwoVfpxCYOKo8F3xINXQpMiAqD9GQg2KC7kjjotMggZw9D6fMNPHrpVoQ1ul0mJTpxY0Y6gvMODs8ep7Yv4OKbSc5d28kkMYC_wsjs1SzdCgKD7w1LlQa471_XChgrS2NgV5LivUBmb31NoluZDffk7nq-niUp6HN2tEyEkwJy_hA1rkDa2XyWwnFu58TNInWy6T6KDlZJR7i6Bz1Zo8Rhbs9lhlaTLU2MGCwm5idfVfyo7enS80SI9m213DcsK7Y-pzV8LMqjx0eVZHAMh1lySb0NGAwxolz0CZt9aylzI2D9LSQQwOHAvoOSH4vIWQpGGhx-cpS_nyrqo9qQHo8DQlgeAX85bKAl_DZx3bf7qXXPtcRo5HWFk06E7QR9pCM0IlDVf_Lf2MDuT01zVnJpCQDG-imtZSRLaJbs5D1UIHGwobTaHUns-FbZc5j4O7JvMKG6FWOk-UKepFQvHh6qK1v0GXptzhphkaHDxbXB9w-u9c97DNUNdIPe48EqSzs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
جزئیات درگیری علی دایی و علی کریمی در مراکش:
🔺
رضا جباری: فکر نمی کردم اینقدر علنی و شدید با هم اختلاف داشته باشند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/90231" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90230">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90230" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/90230" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90229">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh2O1SEiULrXLD1HzZo5PpDcAi5WGw3ItSWdv5eyhjsJs5kEdatjPMWvSzu6IXVY7SR5op_eXzYq7kB2HYwZTtKC26okyTDyHswzAzGP_aJnmbbRExnItoqPkhz3VzAFnBBPJr-kAiCESzsEbCK4D4eP4aYyBuaxIE6Nh3fje7sHzwXSgCdMHYcXMvT0Oy618sPtmyQ7i3xBGOWpL-nf6VqaLY5jqPumJ9jgYE3ADpML2I4_6JJG__aHMmDKvFhZD31nFjOAIvoEVm2F1t40ZZAaBpS2lbDkBtxG-VjUkH1Bn94myiRAbwAmzBh_f8vjsyhv_CX0jc3zLjkxI9AWBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/Futball180TV/90229" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90228">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d9611d964.mp4?token=pxQpQPvxm0RHnXxkEu7M7tNjuXqtRmaQBjphwnxMaSm5XZw0Ai-KP5CU9Bjn61o1uC9wuLuHbMVH1Z2bZTKVzTlYXWJbzd9Z7dASbNWDHH7PQ5rsPUF67NSrxzGENX5Y2QLfkjy2Wx6MEXtc8PsB-DJqLRaom-Lz4EcxR5nnepX_91zAyHak4viXwMjUVFiWgqdv7IlGVRs6Km4fAxwY6vHXSKy4ZQ8q_2Nua1qxuUvDGCBABxJaQwxBxPe-eIL2OkqiXLxjY8VCvNMxLaMByyDupOwIwxXVBI79IrnXu-tMJpJuB4cJYzDw5dZwY72Ypa6Tv9kPQNMYJc-lt2pUMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d9611d964.mp4?token=pxQpQPvxm0RHnXxkEu7M7tNjuXqtRmaQBjphwnxMaSm5XZw0Ai-KP5CU9Bjn61o1uC9wuLuHbMVH1Z2bZTKVzTlYXWJbzd9Z7dASbNWDHH7PQ5rsPUF67NSrxzGENX5Y2QLfkjy2Wx6MEXtc8PsB-DJqLRaom-Lz4EcxR5nnepX_91zAyHak4viXwMjUVFiWgqdv7IlGVRs6Km4fAxwY6vHXSKy4ZQ8q_2Nua1qxuUvDGCBABxJaQwxBxPe-eIL2OkqiXLxjY8VCvNMxLaMByyDupOwIwxXVBI79IrnXu-tMJpJuB4cJYzDw5dZwY72Ypa6Tv9kPQNMYJc-lt2pUMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریکشن گاوی و لامین‌یامال پس از حضور در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/Futball180TV/90228" target="_blank">📅 11:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90227">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
آیت‌الله مجتبی خامنه‌ای: رژیم صهیونیستی مطابق گفته پدرم، ۲۵ سال آینده را نخواهد دید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/90227" target="_blank">📅 11:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90226">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d0834d346.mp4?token=Bk7B8vUKe8Q3I09Mb5gBrCIrwQPREZZuJJbBdRjTKYDrg_-_fAKLnCE7_5kar_8thc5836K2jnzopSShyaGsoPuBZklcgS-UPqD2512EmRATj0bXK1H5jG9p1_lkQ3svc-COho-wIrpcg5gmXbc3gfNn3MMKLCFOdNUfR6__EFJQztTbtiZWaY6HldWx1sOkoLGfxl7MIlwSE48SuBgKOXPVTPhaR9unyylvrUi7w-cj1TJys8YHp7Fpj-0CYvGtHooNZ1166HFwcTm63ChGXAgCxY-zlQJoQQUYu-xnxJyerFntYnTD3aIUk4MAZvu26CeTSQRDLefb7XDR3FXN6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d0834d346.mp4?token=Bk7B8vUKe8Q3I09Mb5gBrCIrwQPREZZuJJbBdRjTKYDrg_-_fAKLnCE7_5kar_8thc5836K2jnzopSShyaGsoPuBZklcgS-UPqD2512EmRATj0bXK1H5jG9p1_lkQ3svc-COho-wIrpcg5gmXbc3gfNn3MMKLCFOdNUfR6__EFJQztTbtiZWaY6HldWx1sOkoLGfxl7MIlwSE48SuBgKOXPVTPhaR9unyylvrUi7w-cj1TJys8YHp7Fpj-0CYvGtHooNZ1166HFwcTm63ChGXAgCxY-zlQJoQQUYu-xnxJyerFntYnTD3aIUk4MAZvu26CeTSQRDLefb7XDR3FXN6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینترنت بین الملل چه زمانی وصل می‌شود؟
🔘
سخنگوی دولت: امیدواریم با ابلاغ رئیس جمهور ظرف روزهای آتی اینترنت بین الملل بازگشایی شود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/Futball180TV/90226" target="_blank">📅 11:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90225">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UncP7O5Oi1Z0MEbXTPUOtEOyV58pgfotvQPcrjv-6f8tfm1RBoRRl_ufPGKtKWQp8EMdCKOaYb0XYI8hlhfsB4e9NyBOVvLoatxMnDnvRb_bkDygFUMnZU66dI9M_4k0g-ZPLV6HB9Lb7Wc1_kxHhIkrh_oAXLmmpSY3hr9AvBJutUmAA1aSmS1RdM6A504mtnDIsTsY-vLYmEdn1Kq9sDWjjwKkudBeH34hDH-dwzTSKlnujRbDgl8pFw2rUiIPQqDCuw7WzXkkUu8VG_1fuAb3hh-2uNLmNOnq-tjibkKsp9YuS6b7ShKfjvdGiyz5DCjZfLmoa7IB9HlOEnzMjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C قرار داشتند. برزیل مهمترین تیم گروه C در جام‌جهانی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/90225" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90224">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dt4bEe5TI7h2DkyizJaPUaiLjfT0MWx26QkotumHjZt4Ihb5f4FYw2hwVFbnWmNhZxk9Y5jZ_GhBVCTUrvqRMEURkBAzSIb_drlbUWXW_lzbk8FGi11zsRCYagGtPwH5HmyVevVLOPgdafeHDFy3vNvL-DVZLL3-SjCladgfUrlA4w1J3A20GpK60FrggF0-5DH3gmF7VESnERx2_UThk_coYreHGxv2ztzuC4M6Ny419OnIOrldsJVTQwbOHX0PVC-PgnRkCH20Gku6mkAl7RFQ-EszUb4O5F1FtBy7OM-dCUSr9dNRZ0eAliQL6LeHeUuM1LFU860Sfdmh57bE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با آغاز اتصال احتمالی اینترنت بین‌الملل؛
ساعاتی است جیمیل در دسترس کاربران ایران قرار گرفت.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/Futball180TV/90224" target="_blank">📅 10:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90223">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7673ee9149.mp4?token=Ur-HgUaksCTe7AUQQzQCnBcSvDI1ckprNSb5qpErE_oUj7JFJBZq_2Ud_5k-ddnr-jMhyFLqLotrCS7a4VrDCBVAoATnAubfKmv0HswHOBlb2u3RuvozOErMdB-iciG3UWbA1Db-ZhxYc9bBcZXsOYlR5rqZrPv2AMTA8iUYC--OF3oRSqYJyc46UHA3E0ftwkt4A6jmgBkSUnniqeCKizVyM-FN4ojknpcqWGblh0kCaK9JhjhWTNVL0B3rCV9GJ-Fyn9LUI5P-cMHReTXbDch8mUnj5c9RPzY7gg05FR-4a6SgVgL5da9WVeO2tInDMJpd0LI1RP6LjlUzOYZJ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7673ee9149.mp4?token=Ur-HgUaksCTe7AUQQzQCnBcSvDI1ckprNSb5qpErE_oUj7JFJBZq_2Ud_5k-ddnr-jMhyFLqLotrCS7a4VrDCBVAoATnAubfKmv0HswHOBlb2u3RuvozOErMdB-iciG3UWbA1Db-ZhxYc9bBcZXsOYlR5rqZrPv2AMTA8iUYC--OF3oRSqYJyc46UHA3E0ftwkt4A6jmgBkSUnniqeCKizVyM-FN4ojknpcqWGblh0kCaK9JhjhWTNVL0B3rCV9GJ-Fyn9LUI5P-cMHReTXbDch8mUnj5c9RPzY7gg05FR-4a6SgVgL5da9WVeO2tInDMJpd0LI1RP6LjlUzOYZJ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران ترکیه در آستانه جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/90223" target="_blank">📅 10:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90222">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed589fd9b.mp4?token=jjQPaoQlw57IVT4nSqE4NLxD7s9ku3CjMMyb5UgydGC0OeDIO5J2KDMso2Syc2E3mGL3LDztfqCQ7m2NP6rizs4LHUeE3UgNPsLL4F8NDQjlEFxfZLiU-LhTHg5i7LAOBvy292FkZryjp-4TaxFx_daTpglCITFV0WuOUKj0_6EqdpbN2RMol0AFbxOFdY8ZwRmzrvQJ-Yp5kNNdfN2lZF36M6oUhz_-YAlFiYpGaqGGocmcrpRQHAAl2JCs-htlhRdyDWxN_N2xpOTiL2cWQrzlwm0RQEB9atLABU9aBnPy8DVkgRMH1U6uSjMpZP6GztsrBNWSQwdSRjRVr0Qkdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed589fd9b.mp4?token=jjQPaoQlw57IVT4nSqE4NLxD7s9ku3CjMMyb5UgydGC0OeDIO5J2KDMso2Syc2E3mGL3LDztfqCQ7m2NP6rizs4LHUeE3UgNPsLL4F8NDQjlEFxfZLiU-LhTHg5i7LAOBvy292FkZryjp-4TaxFx_daTpglCITFV0WuOUKj0_6EqdpbN2RMol0AFbxOFdY8ZwRmzrvQJ-Yp5kNNdfN2lZF36M6oUhz_-YAlFiYpGaqGGocmcrpRQHAAl2JCs-htlhRdyDWxN_N2xpOTiL2cWQrzlwm0RQEB9atLABU9aBnPy8DVkgRMH1U6uSjMpZP6GztsrBNWSQwdSRjRVr0Qkdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
سیاوش اکبرپور: جرمی دوکو رو می‌شه مهار کرد!
😁
محسن مسلمان: ولی نمی‌شه؛ فکر نکنم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/90222" target="_blank">📅 08:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90221">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/Futball180TV/90221" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90220">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idxc_ejw8dwFLmFVPOkxKZRLxfgpNtAKbtPsLHRmlzOU5ImokpEPGcgohxcGVzbxlppZuumRJCWat8qlmI9foIruMxsqBg4bBL95veiNsl-UnBlAlEPqzZgZz_532IcXbbpEb4nVNyVH__pb-9z5lV4Cmab6Ve01BTNUKjpiz5WCxhF-z2bU1Y7LjvoaRs2R-CH7MT-8vg6-_V7Grxx0OQVbulERaMgEEZYhwd9hvYrcJ6wwCRv3Ui9KUlcJl_NOp-emvF5yVIJJquCymHQy6xRwv5xhyR2X6D3a5X6VI6CQLz98T73qrtRbf_W-d6vk8sOEzKXOrx1gnNXAQNRXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/Futball180TV/90220" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90219">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuABEr23abHGi_iuO5ht7uTo4e0SvabaT_YdnAFzClsPlApnX_5GEbMMpJGwfupH8fDQKVW1ckg9T54uYPCF2QBMFlzT7FWiaaAuCJqQ0mnDQGQQMoEW7E2rhY3HBfrxl6gh5yfCNQ-T_-rsnFaSEIVxS2Wy0mYRiRIZ74t-KZJ0EPdmJa-JxeU1aKvVFhql1-UDq9wPIzncQnG71H7RpO0LrhDzJ6gWrQnqow9yPppvoR4rYUWMwHxIkhGcesxfJwjrtpEkwqTsJ2q3BBl3uPpcXlCGjWhLZgWBi_qXPI2sbMWjkpzLuP-qySpE5ijP-OfVkNCm7qeAte8SR17L8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇴
لیست تیم ملی کلمبیا برای
#جام_جهانی2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/Futball180TV/90219" target="_blank">📅 23:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90218">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdh5mDyGkFs6R8YjbsiAJ9B-bjLcgvjMvWH_XRZuDMBOIIO3xs8Dtdy3z_ck3C5juK0qLNP2Hl0CraLz5kqvKodrkvmY_zzRc1MEh1ib2A5ZXeSSAF_ZuGcg-4XElHM3EChVsxARCrs7114wwMu6u2NjBjngd50HC3apHA3v3ywIW3FeH7Md8xjBvx5lf3pppeqRrlfHcneSjfEyIRFWL3jdOsAY5KXuk3IOKYVeIixd1-7a7yXi93i1D558hTJi4ZaO4Hcq9q-h9rzrpxKCqguL9tKX3U42mh0acKSPoTiUEEDp2E4wwRP7Z3TGgdXpLUMxbhi08le47ZqqX0n_jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکس آلگری از هدایت میلان برکنار شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/90218" target="_blank">📅 23:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90217">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3602a6e5c9.mp4?token=d3BttHlJhxAc9_6M9vNt5CpVhv2rp4f0aH_HD8DGn4tSE-QRx4dfQCVEKyqLrVf5CyjQFwftzk8S7OXsXjJaLtGTAOlxjDps1sfWsKalsTIFLiy3vt7plBTxXSsns1q0nkk1uq32tMMh8lDgphAX3mUAikplCKAthrtlBC3HbMMt3WYxv_8SUH5xFncOeC9k1u6oLdInGHbH3PqBt1lhqPuhsSkZ1I0EFLVkyN8ix6X-Ha_57znv_bH-FlK55nae2WA3CqZqAV8ve87vQxCUztV6Yg_h0DuX1dyqDHGzR68s116OQKKysnJ54_It_GMBJeASHmusQPU9-KDEnJi2ySdOx5InQxRaguwB6v8tLrAbH7VsuPZu8LESU1kAcGgaQL-4dxXs4x803vpDi-UqEDGmSTFyZi6vAfy6VKXSwebfNfmkzt1Oin5haLXvnl0EHf9-6VhUVPIzYLiJxi71xJJOnQoPUVRO2ktbsnC6j-DleZw8wHsA-O7NPpqf34ZXbA5ZqzfGdhExeLMXTS25a1nEMAOp2joY7iwDpVPr0xDwyk2HzH_awBpJlGSCp4ShX0eskzcImt2aK0eaTBupWAQijZNpLOyQqIx_5Do7hxITZ622vy-Tzvo1gt9j_LgE30GniXEdUnTxCkqRn4PGorL_pqbv1SfIX9wkpA8QLHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3602a6e5c9.mp4?token=d3BttHlJhxAc9_6M9vNt5CpVhv2rp4f0aH_HD8DGn4tSE-QRx4dfQCVEKyqLrVf5CyjQFwftzk8S7OXsXjJaLtGTAOlxjDps1sfWsKalsTIFLiy3vt7plBTxXSsns1q0nkk1uq32tMMh8lDgphAX3mUAikplCKAthrtlBC3HbMMt3WYxv_8SUH5xFncOeC9k1u6oLdInGHbH3PqBt1lhqPuhsSkZ1I0EFLVkyN8ix6X-Ha_57znv_bH-FlK55nae2WA3CqZqAV8ve87vQxCUztV6Yg_h0DuX1dyqDHGzR68s116OQKKysnJ54_It_GMBJeASHmusQPU9-KDEnJi2ySdOx5InQxRaguwB6v8tLrAbH7VsuPZu8LESU1kAcGgaQL-4dxXs4x803vpDi-UqEDGmSTFyZi6vAfy6VKXSwebfNfmkzt1Oin5haLXvnl0EHf9-6VhUVPIzYLiJxi71xJJOnQoPUVRO2ktbsnC6j-DleZw8wHsA-O7NPpqf34ZXbA5ZqzfGdhExeLMXTS25a1nEMAOp2joY7iwDpVPr0xDwyk2HzH_awBpJlGSCp4ShX0eskzcImt2aK0eaTBupWAQijZNpLOyQqIx_5Do7hxITZ622vy-Tzvo1gt9j_LgE30GniXEdUnTxCkqRn4PGorL_pqbv1SfIX9wkpA8QLHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما ۱۳ نظامی در عملیات خشم حماسی از دست دادیم تا مطمئن شویم ایران به سلاح اتمی دست پیدا نمی‌کند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/Futball180TV/90217" target="_blank">📅 21:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90216">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POcuLBtdo_ZB3o8K1EWHBYUfEc8H9RsGvCNxosGJbpAAXVdw779bPPjh9AVxEWqBmfM8voo23ykwfblSEImyM4o99p9Vsdj36jXqNUk_H_KQz4smijl1GYL67k3bFxentVgTqPKXBzHv3RPBgWYKuLQ_gpQFAIuHMI44zburk5TcOJCCpRAWYpQhr2buor2ZNfWjemyasbxdrW5FXoLQ6aGB1NEKxHQONZwq2dj6hwAUeP778FOT6gi_jKnqtoFv4V93B2TOb4tPFArpz187h7os4qzevasnp7BYQQWoqn4vKj2dtbmqwcdy2QuOCXHcUe7TdZSTHgOkb3Fu0iSONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سن-اتین - نیس
🏆
پلی‌آف لیگ ۱ فرانسه
🇫🇷
⏰
سه‌شنبه ساعت ۲۲:۱۵
🏟
ورزشگاه جفری-گیشارد
🎲
با بیش از ۴۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
سن-اتین در
۱۰
دیدار اخیر خود، چهار برد و سه تساوی کسب کرده و در سه بازی شکست خورده است.
✅
نیس در
۱۰
دیدار اخیر خود،
پنج
تساوی کسب کرده و در
چهار
بازی شکست خورده و تنها در
یک
بازی پیروز شده است.
📈
میانگین گل در
۱۰
دیدار اخیر سن-اتین
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نیس
۲.۳
گل در هر بازی بوده است.
🧠
اطمینان صددرصدی نشانه خطای شناختی است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/90216" target="_blank">📅 21:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90215">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7263cfb5.mp4?token=VPt2D3ruMChfQ_5JwcGUL77MLHcVKcDGb4W1k5kV--wK5huB7_PQVxdcTqNh55i9m--BIeCFhT6AuT7Ayhcrp3F3bOvzV-MLXA4zMjzqv77bfb_MeGyP1xPoxALXSzhhoSPao9qcGxnlLyMZF7klEJ7oaM7YYxHGYDyWRqLRULCl3ibASBDewdB-S_34Ti-A795RXaaL4EvS6UD8n81oOCIlA6HHG4HDmp5PaLvfzJ6I3rw-hA8y314AhdYVVX1Q0f0gShHjBNj6MeM-mQlS7M7SgwILRkwGCTzy_cmHALF_8NWZchfj7t_oWa0pDaWusDE6kucq8gXmCRFHWW7Kag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7263cfb5.mp4?token=VPt2D3ruMChfQ_5JwcGUL77MLHcVKcDGb4W1k5kV--wK5huB7_PQVxdcTqNh55i9m--BIeCFhT6AuT7Ayhcrp3F3bOvzV-MLXA4zMjzqv77bfb_MeGyP1xPoxALXSzhhoSPao9qcGxnlLyMZF7klEJ7oaM7YYxHGYDyWRqLRULCl3ibASBDewdB-S_34Ti-A795RXaaL4EvS6UD8n81oOCIlA6HHG4HDmp5PaLvfzJ6I3rw-hA8y314AhdYVVX1Q0f0gShHjBNj6MeM-mQlS7M7SgwILRkwGCTzy_cmHALF_8NWZchfj7t_oWa0pDaWusDE6kucq8gXmCRFHWW7Kag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن‌روشن: فيتيله ترامپ رو بكشيد پايين وگرنه با "اسلحه ژ ٣ "ميريم آمريكا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/90215" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90214">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/90214" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90213">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lHdR15plks81JZdTlR4A_f68p2w-kcI4tEJPW4FNToTE4aS0Yp2skPZ9AJooq6XADRtBoMob1Ti3e2BlI2pLScFjHJQXwOeB2jJD6Rs4jcoSCZFMQTi4lbvJ0o4frojlHrJSOXD6kwnYXMYRAhiWW-KySc_HP_TROUZCYFzNjLQ-NL71m6Knbpp0ApjJyGwEF4HaD5Nhqh1HDmCkcGdf01gp3d5i9WonSsbLmd2GxJ34JHCl4O7ndYGEgVuQ8jBnBhj-ImjxdB6tZFSVrD5iEYt3eCDeGflLx0DWRyrtXc81gmHR-2sIRl0RTOgafRPHupcrD5Zir340sT4KSPVIvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/Futball180TV/90213" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90212">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🔷
جواد نکونام سرمربی سابق استقلال از طریق ارتباطات خود با افشین عبداللهیان مجری سابق شبکه ورزش که نفوذ گسترده‌ای در هلدینگ‌خلیج‌فارس دارد، خود را برای سرمربیگری فصل‌آینده استقلال معرفی کرده هرچند که در این میان تاجرنیا قصد دارد با سهراب بختیاری‌زاده در فصل‌آینده ادامه دهد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/Futball180TV/90212" target="_blank">📅 16:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90211">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltYrzwvfHEguGO8sh6AeVhIeOiAq010Owh9udRDJ_L-8WhLSrka4vqd_dWpM2upAaVgDV5piZ_P9NmwN2_H1k8mWakmp50ZHxWtb059ABbvkfRnxLeBdC_U4yyorHtiFyMmkTD5ojB3CEKeczkwFlSO_Z8rrZ-iT5ntHYZ0yt38RM2JAgjvdGIQyEkWFkrIq1luEd80fIxil48CKQ_xBCRRABbGL9c1tEptVRFbjp2UVlxkYVH2ea7Otcp0pkpbko03NUDCfVBy3ETTVIsuDXEkRIt_9bNVkxt0xhTv6do1OU98-6gq7IJI1rwcQC5p_eJCQ4W57nLF-E6CzFp-xcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست تیم‌ ملی اسپانیا برای جام جهانی 2026؛ بدون حضور حتی یک بازیکن از رئال مادرید!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/Futball180TV/90211" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90210">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2rayYar</strong></div>
<div class="tg-text">🔐
سرور اختصاصی با پینگ فوق‌العاده پایین
مناسب گیم، ترید، استریم و استفاده حرفه‌ای
✅
سرعت و کیفیت عالی
✅
آی‌پی ترکیه واقعی
✅
پایداری بالا و بدون قطعی
✅
مناسب استفاده 24/7
✅
بدون محدودیت زمان و بدون ضریب
💰
قیمت تک: هر گیگ 150 هزار تومان
🤝
قیمت همکاری: هر گیگ فقط 120 هزار تومان
با ضمانت عودت وجه در صورت قطعی
🙏
برای تست و ثبت سفارش پیام بدید و از طریق ربات هم میتونید خرید هاتونو انجام بدید
✉️
:
@V2rayYar_bot
@V2rayyar_sup</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/Futball180TV/90210" target="_blank">📅 13:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90209">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
ستاد راهبردی فضای مجازی صبح امروز موضوع اتصال اینترنت بین‌الملل را مشابه دی‌ماه سال ۱۴۰۴ مصوب و به رئیس جمهور ابلاغ کرد تا در صورت تایید نهایی،‌ وزارت ارتباطات موضوع اتصال اینترنت را اجرایی کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/Futball180TV/90209" target="_blank">📅 12:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90208">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa22a668b.mp4?token=HkMArxnC30EtytFCvNthS022ZK8kU5qn2rQr4ZuT2NY3PnMTzu0-MWLHLiL1FBLu_8w6ZV8Ljc5z4TZ74b0GZtO6bFaaOBQ4xIhwfrUIQTuUd1yqFnZdYbafCdjbBF5V-kEaT1jQEX4m4iSTgJQ0zpzqofw0UfFQHX86jt2ZiFUF-oafTvxegj0yqZJtU00EQoOdHT9fgev2Bv0Snv2Eh4HEgdryEGZ7gDXl8WMoqXsB48SBNWr3s1Me3e0OgBDprX7Xo5fG2tZbm2WT6_UjE8l-gGZBoDK5qFQwwJhkVK0EMoZAYBGlTsdfxgfjVSqbNJP4evOiPO4cxJMeaoE_9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa22a668b.mp4?token=HkMArxnC30EtytFCvNthS022ZK8kU5qn2rQr4ZuT2NY3PnMTzu0-MWLHLiL1FBLu_8w6ZV8Ljc5z4TZ74b0GZtO6bFaaOBQ4xIhwfrUIQTuUd1yqFnZdYbafCdjbBF5V-kEaT1jQEX4m4iSTgJQ0zpzqofw0UfFQHX86jt2ZiFUF-oafTvxegj0yqZJtU00EQoOdHT9fgev2Bv0Snv2Eh4HEgdryEGZ7gDXl8WMoqXsB48SBNWr3s1Me3e0OgBDprX7Xo5fG2tZbm2WT6_UjE8l-gGZBoDK5qFQwwJhkVK0EMoZAYBGlTsdfxgfjVSqbNJP4evOiPO4cxJMeaoE_9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین ریکشن‌های پپ‌گواردیولا در منچسترسیتی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/Futball180TV/90208" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90207">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90207" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/Futball180TV/90207" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90206">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLwfWwKPIeNtbo4z23JsEpxj_ujTSwRzJ19AHTEFrQjLK6dZ6n6TtgM_YrgowLGcLgPl_1--QbrZdxNXPfLb_rVPDFwXhdT-DYrb0Jw-gAGCls73wlCcXzP3Aha6du5GIu90MtmvRThh-ISczFQvUOvtIcPTYRjUp_VTIKawDOy4WUEOdou5s03ruMYkXCQXOPTVDOALBYobZIg9Jq6M7GHIJytCaJsX555zHCf_V6YVwazCp5VtqYK9szGqoDnjdDsu_3Y3p66pv3ubjyHbkL8O5bOiDp4owxAeY7mkRseQL-roSAfySptJuK4YeGIWzV23RG21guEvfFsj-4uFzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎰
با 1XBET راه خود را به سوی ثروت بچرخانید و از سرگرمی های بی وقفه لذت ببرید!
🎁
تنوع گسترده از اسلات ها و جوایز فوق العاده را از دست ندهید!
💸
فقط کافیست ثبت نام و واریز کنید تا از جوایز و بونوس های فراوان 1XBET جا نمانید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/Futball180TV/90206" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90205">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940870b589.mp4?token=EsqeU1TbPbnQe1DFF17RurD3moDMhqGpMZx_Tglqwj1nRYaMMuKtO0qp_XuL4RzLDTWzT1pL2hDPSTqGCU57D_03YQSX1j2Ov9rR2iktJld85P33DhZeZJHoGlTxB_5mq4hnCd3AtLMvx-984Wc0ujmMwpehsqAiZsqVgoFR3e_zIa_XCuC6wGQo5yrP2vB2MGCtUiVWXTE2Zef_Ky2XmrsjI04Ffed-W_nwElqKoLrruvaJQhIR0cTY2NRcQhDvzu3P3ZTQJ-hLqosDrzaG-5Qrz_drBy34I_XHuAdfOQ8SzZLI1-UmnF1p2kauWyil2r8hKwWQ-YBsSfp8GOCaBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940870b589.mp4?token=EsqeU1TbPbnQe1DFF17RurD3moDMhqGpMZx_Tglqwj1nRYaMMuKtO0qp_XuL4RzLDTWzT1pL2hDPSTqGCU57D_03YQSX1j2Ov9rR2iktJld85P33DhZeZJHoGlTxB_5mq4hnCd3AtLMvx-984Wc0ujmMwpehsqAiZsqVgoFR3e_zIa_XCuC6wGQo5yrP2vB2MGCtUiVWXTE2Zef_Ky2XmrsjI04Ffed-W_nwElqKoLrruvaJQhIR0cTY2NRcQhDvzu3P3ZTQJ-hLqosDrzaG-5Qrz_drBy34I_XHuAdfOQ8SzZLI1-UmnF1p2kauWyil2r8hKwWQ-YBsSfp8GOCaBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و دیگه محمد صلاح تنها قدم خواهد زد.
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/90205" target="_blank">📅 11:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90204">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392ebb3ce3.mp4?token=RJoDOXIwNsWz8jl8dT0lVut-sj1pDOAc_1ocMyM8mQe6oUa-ZgzrUV5essnfvhkZo2zBAZ4jQijPqUreK5GdUydLfnRNDRL6QkQuFnI-SiJ3TOznQSWyBAgIl9VQkHb6VAi-WFSVolsOxXPZD9BIZwnVU6b5i6KrgWgTtxLCmLgjd-ENClV2xZ7Agf-e_sQ1LTJHw48Ue9uOYVAs4LxHlxQ6sbIFRDn6uIkE_pr6hSqR3VG3NK2F9-jAbj_2CIjMqx-R7STBg0EhmowPKgSQ3TbkcSdXQ-L9csZSGAJ5tNkJUrZ3PlRMAib5llnwczFH8wnhcMdMrAZwLWrwN0AfwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392ebb3ce3.mp4?token=RJoDOXIwNsWz8jl8dT0lVut-sj1pDOAc_1ocMyM8mQe6oUa-ZgzrUV5essnfvhkZo2zBAZ4jQijPqUreK5GdUydLfnRNDRL6QkQuFnI-SiJ3TOznQSWyBAgIl9VQkHb6VAi-WFSVolsOxXPZD9BIZwnVU6b5i6KrgWgTtxLCmLgjd-ENClV2xZ7Agf-e_sQ1LTJHw48Ue9uOYVAs4LxHlxQ6sbIFRDn6uIkE_pr6hSqR3VG3NK2F9-jAbj_2CIjMqx-R7STBg0EhmowPKgSQ3TbkcSdXQ-L9csZSGAJ5tNkJUrZ3PlRMAib5llnwczFH8wnhcMdMrAZwLWrwN0AfwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدومیت لیونل‌مسی در فاصله ۱۷ روز تا جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/Futball180TV/90204" target="_blank">📅 09:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90203">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76980eb486.mp4?token=QHKNopueYM_m7Sl_iVNrRgO1FJRIRhfJFAkPvlr-6g7JaoM0D52dj5lTeYLVXqAYc4-iQ8mTD51iw1ggz7sHrT_08A9kChU8t885B2NE-END6U5ubuLTwFnSgUrR6Wk4BG_uERGqz9IiY-g7qJ8pii7FEV7GBEMN7Uge5oM2bHnX8VjCYBpiM7a_Nzkb4lhjSMaOWRHx00aztk5sTACaJ7GAcwUgpJLEQ36ns43OaJcpx9hMTRxLr1lHRHdHxS1_mYeDCHRJ-NDhnp16p9RSfMWCSwoYyCG7qNr1a_JiPRZG0zTJiLIs28_V7EdAh_ObXjb8qLVABdIpqMECBH5PJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76980eb486.mp4?token=QHKNopueYM_m7Sl_iVNrRgO1FJRIRhfJFAkPvlr-6g7JaoM0D52dj5lTeYLVXqAYc4-iQ8mTD51iw1ggz7sHrT_08A9kChU8t885B2NE-END6U5ubuLTwFnSgUrR6Wk4BG_uERGqz9IiY-g7qJ8pii7FEV7GBEMN7Uge5oM2bHnX8VjCYBpiM7a_Nzkb4lhjSMaOWRHx00aztk5sTACaJ7GAcwUgpJLEQ36ns43OaJcpx9hMTRxLr1lHRHdHxS1_mYeDCHRJ-NDhnp16p9RSfMWCSwoYyCG7qNr1a_JiPRZG0zTJiLIs28_V7EdAh_ObXjb8qLVABdIpqMECBH5PJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید قلیچ در گفتگو با بهاره افشاری: امیر قلعه‌نویی واقعا غیرت و معرفت دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/90203" target="_blank">📅 09:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90200">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4l_MlOE7F7Q4CfCv2fSIFnVnyrgVgv5e9BKf1UQ2-rnU0D2y3g3iQP7VrG-6h3RmDxqWHPUqwuhlYi8IH0hL9B8dSPCNHP8vfZiJxx931FVTMzaE8S34lBNqQCh4xu_9HxoOj4sSYoSu-DHUANOXAtYD-4NrFYORfwtRnwNp98oaBRV1v6pWw5V0hQkE11b0zB7x-IS1-uJPHlDLMJl7ihxh84K2nzm139M_ih-4D90Ea3kNEzX7avnR_JoM84BPzwKZzBzD9iwP4Cwx1_NgzJwIARvxQyFetD1wPXZNvigzrlO9Ht4sAo9U4xG1oj-cMf0szhZ26_W9rh42nTyVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخشش کومان ستاره النصر در دوران باشگاهی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/Futball180TV/90200" target="_blank">📅 00:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90199">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf21c6839.mp4?token=gefP5GD5OHmHe9LvDGiSDxEGIFkRZ0eyAJMDG9Le-z88eTC_EAB8n7uBXjGzLzSoa-LxMExCpNRG3O7WjtGaZ1Mgjt43Kz3BRj0Zw5lX__ZvkifBGJ7AOHmxcN0yvOtUYXhAad0enjlVLI0TDBPn8d9LH_WyABSZEiFhUelrK28lbi0zeyNIfruKfsuPevE8u9A7tfiohN6sma8DxIldPh7KONQM9eyk-A9TjKBYTbhou1XJZ8Bsn9js482Jfg3IH4RroGW-2Ezl2nnDwSXC-sqvcqm3dAqXKWxA-vxdsUVfxUYLoNw52aKEaXTAmpQAgmu1NTjoA0M-Qn3Gr-5MFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf21c6839.mp4?token=gefP5GD5OHmHe9LvDGiSDxEGIFkRZ0eyAJMDG9Le-z88eTC_EAB8n7uBXjGzLzSoa-LxMExCpNRG3O7WjtGaZ1Mgjt43Kz3BRj0Zw5lX__ZvkifBGJ7AOHmxcN0yvOtUYXhAad0enjlVLI0TDBPn8d9LH_WyABSZEiFhUelrK28lbi0zeyNIfruKfsuPevE8u9A7tfiohN6sma8DxIldPh7KONQM9eyk-A9TjKBYTbhou1XJZ8Bsn9js482Jfg3IH4RroGW-2Ezl2nnDwSXC-sqvcqm3dAqXKWxA-vxdsUVfxUYLoNw52aKEaXTAmpQAgmu1NTjoA0M-Qn3Gr-5MFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
بازیکن تیم‌ملی والیبال ترکیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/90199" target="_blank">📅 21:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90197">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028fa17067.mp4?token=D8urnWqKz4kwD9mxs0600rN_eHX_tqf0ZIcZqXm3kmLpUdi5SPKBqOpYlbnf2HLcCK2Mc58pwtKkh0xZTcZ3I_EeNskhdxEUfpCPo2BfLWd5hJeqEvoiMJf9Q7tnPRvB0fUVqavGHhUJOh0gv8bI2QpkWBkYML75Vjlfq0Xcb1FhoQq9Hk30WNCXBJZxPBfGSDhchY8L-gWcQgAICDXGgEa89EBluI1nqXFLrk0d-u2xJmjNeZbOP37PmwX5-MzZYFCvjBWTQS3GmCLMxxKIPB8oNS32gcEjplRsikvcuHeGGgjIGwlgTjBADgtCUjU9Y8n99nezUX2akxyeqsBZHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028fa17067.mp4?token=D8urnWqKz4kwD9mxs0600rN_eHX_tqf0ZIcZqXm3kmLpUdi5SPKBqOpYlbnf2HLcCK2Mc58pwtKkh0xZTcZ3I_EeNskhdxEUfpCPo2BfLWd5hJeqEvoiMJf9Q7tnPRvB0fUVqavGHhUJOh0gv8bI2QpkWBkYML75Vjlfq0Xcb1FhoQq9Hk30WNCXBJZxPBfGSDhchY8L-gWcQgAICDXGgEa89EBluI1nqXFLrk0d-u2xJmjNeZbOP37PmwX5-MzZYFCvjBWTQS3GmCLMxxKIPB8oNS32gcEjplRsikvcuHeGGgjIGwlgTjBADgtCUjU9Y8n99nezUX2akxyeqsBZHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و دیشب آخرین بازیِ دنی کارواخال با پیراهن رئال مادرید بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/Futball180TV/90197" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90194">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=lgTRC5tWsUGzAthMmjfld2rAw3yjtxlq23Dqd8G2ElVSw5NXbxPYAnn7sd8tummcy_mCQMo5bE9_jYlEb8sPo4b8S3o_SrOY0bBI0QvnJkM4AqaCHFoJ_H1g_W6nBCmWC1mO9sNsSsK8T0oHl6YpjO-bOCyazDVoNtLI5V06Ye549gxsNN0gz6JXTfIqbkAE9vdBNM1WGNIfucwAeJgzfrfjJtEsTdEA1bUCYEpN1K0tRDgkugD-Uy79sue60Z35z-Nlrk4238QTTo_VqKnI1PG8oJEbAgbyltPqcbL7CTcYff3ThJNDm67tEdr7Bkk55zL-dcZdAc6YpQhRCPWavQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=lgTRC5tWsUGzAthMmjfld2rAw3yjtxlq23Dqd8G2ElVSw5NXbxPYAnn7sd8tummcy_mCQMo5bE9_jYlEb8sPo4b8S3o_SrOY0bBI0QvnJkM4AqaCHFoJ_H1g_W6nBCmWC1mO9sNsSsK8T0oHl6YpjO-bOCyazDVoNtLI5V06Ye549gxsNN0gz6JXTfIqbkAE9vdBNM1WGNIfucwAeJgzfrfjJtEsTdEA1bUCYEpN1K0tRDgkugD-Uy79sue60Z35z-Nlrk4238QTTo_VqKnI1PG8oJEbAgbyltPqcbL7CTcYff3ThJNDm67tEdr7Bkk55zL-dcZdAc6YpQhRCPWavQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهناز شفیعی :«می‌گفتم ناصرخان یک کم کلاس بگذار و با زنگ اول تلفن را جواب نده اما ناصر قبول نمی‌کرد!»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/90194" target="_blank">📅 19:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90193">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
آکسیوس: تفاهم‌نامه ایالات متحده و ایران:
🔴
- تمدید آتش‌بس به مدت ۶۰ روز.
🔴
- هیچ عوارضی از سوی ایران بر تنگه هرمز دریافت نخواهد شد.
🔴
- ایران ابتدا تمام مین‌ها را پاکسازی کرده و محاصره خود را برمی‌دارد. ایالات متحده محاصره خود را تنها پس از برآورده شدن این خواسته‌ها توسط ایران به پایان خواهد رساند.
🔴
- ایالات متحده برخی معافیت‌های تحریمی مرتبط با صنعت نفت ایران را صادر خواهد کرد.
🔴
- تعهد ایران به اینکه هرگز به دنبال سلاح هسته‌ای نخواهد بود.
🔴
- ایران متعهد می‌شود که در مورد تعلیق کامل برنامه غنی‌سازی اورانیوم و حذف ذخایر اورانیوم غنی‌شده خود مذاکره کند.
🔴
- ایالات متحده متعهد می‌شود که در مورد تدریجی برداشتن تحریم‌ها از ایران و بحث درباره دارایی‌های مسدود شده ایران مذاکره کند.
🔴
- ایالات متحده هیچ نیرویی را از اطراف ایران پس نخواهد کشید. خروج نیروها تنها پس از رسیدن به یک توافق نهایی در پایان ۶۰ روز رخ خواهد داد.
🔴
- جنگ بین حزب‌الله و اسرائیل به پایان می‌رسد – به اسرائیل اجازه داده می‌شود اقدامات پیش‌دستانه‌ای برای جلوگیری از بازسازی سلاح‌های حزب‌الله انجام دهد؛ این شامل حملات هوایی و پهپادی به لبنان خواهد بود. «اگر حزب‌الله رفتار مناسبی داشته باشد، اسرائیل نیز همین‌طور خواهد کرد.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/Futball180TV/90193" target="_blank">📅 17:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90192">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnqXFuUmeYlOmPTotvpTNlZFBI60hldjLwIs6zrRCH5bgkT589vYbKOOYskBeedaPuxus2HHnIg9lkEtl_gc21lQ82sslUPXVLxCaOHAd1RH9Womsza9UYO55MmLKNbF8Xs-vj-GfzKujISj4F3mSd5br2zHw77J0EvcX3Cebs0HTf--ik9flSKtvWU-eGKhGG8NSYvCaI-aS51lODbPHvQWvFVZR2K2P-pePN36u_fVgLN2gP-KnRVGsz3DyvpBxf-JTtHdhmMbA3mS0jS0oPqAIfrCtxgXF-hsMBcY_74eKYKftLrUeazQeFRW8pxM0cawkQMPzxJU6fgCLdkr8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاب مشترک داکنز نازون مهاجم استقلال و روماریو اسطوره فوتبال برزیل در پاریس؛ هائیتی و برزیل در یک گروه جام جهانی 2026 حضور دارند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/Futball180TV/90192" target="_blank">📅 17:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90191">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UR5aKuAi6Jw7hRpKfSNIO7sM8KSKTisOThh6tXNeN_Lr258nKPt0bau8fZOVIrt2802E1QOhUJhjq5_QFKXv38xDJ0pn_3pQ1sa8kcW89j0PUlJKrR-XEWUhYJANlmdIt_UmIM91MhvxBYirCz4puippqQJbu7O8Cw2sCaXfGHOD185tWphWZFprx3MeSppGpfxbtOXMt8HUriRB7vN6yEX80ciO3wFvzCyo_lFvNekaqvkQMNFXQcPT2W9I_8o-_R8kiyV39glAAiqlxUEVJ25wK7X3_J0kImRunBCo1_A11rd79bzNxRbTzd-l5emnrscGIpUW1qjYMBkenBDvkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ: خدانگهدار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/Futball180TV/90191" target="_blank">📅 16:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90190">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67618efab5.mp4?token=tj1iijCZGXdNJqJYubZNA0DgWbrk2OiEypTfVJbPTkKcisH1cXEBcEpcjfTo-pO_j6Ld7FQt3bbasH48DKVXLcd5Ub5I-g5kBMKkAw2vgfUz7CEXNR5ZbN6da-GLdfxIw1SjP4TlrsWmdLur1wb1DZkcnoKwegVLoTMzbIRDdnR2Hd7rnXSg7Uxf9QUCA4et-yQ90LT8CJBwr7FRikJXKIxQ66kNs-aKIhMhMx7ICY2WL8gfI7m4MP75YdXsf4hL7WMbITSJClvkg2-iiXN3lMJyNBHFe3BTgh_PXtTC0nPUM19knkezHhMRP1ZSJI9qpzcl_1d3i21tNnSndD_BVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67618efab5.mp4?token=tj1iijCZGXdNJqJYubZNA0DgWbrk2OiEypTfVJbPTkKcisH1cXEBcEpcjfTo-pO_j6Ld7FQt3bbasH48DKVXLcd5Ub5I-g5kBMKkAw2vgfUz7CEXNR5ZbN6da-GLdfxIw1SjP4TlrsWmdLur1wb1DZkcnoKwegVLoTMzbIRDdnR2Hd7rnXSg7Uxf9QUCA4et-yQ90LT8CJBwr7FRikJXKIxQ66kNs-aKIhMhMx7ICY2WL8gfI7m4MP75YdXsf4hL7WMbITSJClvkg2-iiXN3lMJyNBHFe3BTgh_PXtTC0nPUM19knkezHhMRP1ZSJI9qpzcl_1d3i21tNnSndD_BVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همسر حجازی: دامادم گل زد، تیم ناصر سقوط کرد، دخترم گفت طلاق می گیرم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/Futball180TV/90190" target="_blank">📅 13:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90187">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fbdde7379.mp4?token=gsW4AuhjN2pGabPVrE8CeG_ZntAjPXFtsndQnI_Xcc_wAl561PemUkuHJcOkV-1eBMDYTSVm8F3p-C-GbNGu4bdKGqflwCwTdPy2sOG5ZnAElf5K9dvsiMkQ1jZqjPPTS1XMOvBTDd_ZRrmVxhDTsbG2OMXs2yGExggsGXZ99WdHKXhGy3mWaAaKoN7K1lN9H6LsJ30F3R8X8Q1iugN0Q6zQC3blIQc-L66X6L0gDyawE135hYW5JUH0dB9M8Xf6Y8aC6iaEVFG_rvzwKxhSu3rdqV1ZutSGIFRFZ33QQnJ6fR8coUPw2pNr61t7CZOMF-oRCnJeRc6MKWA2jjIlQJWXQrFqY46iIlYzanXQ9jm3GI5PpkvHkWjq4W00yiR1PJvRjtiM-Yxcc6QCJecIFut_GZaCOyvnBUBinkunB7eRZ1iySF9xrK0BYHkJc6ETMCqMuaoK_6Sj9KO7IaAMCWoiRBfyZVPw3oZXLXq088G5meVHPBvlm01FGAA5Yad8iwnFk9134p-bgO0XwzuhHBP8tOAHwK8E3Mz6-jDym7F8GGPs-pjtbkc6tToFtUBNIq0X8Eyo22uV56roRPvcb77PMHi4vFtH1kxtGwBwabHsQCEX2VenFlejIITfrfbLv9XypewcBw0TY9YddGw8ZTdivMzZnw8AUhdumYZpLxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fbdde7379.mp4?token=gsW4AuhjN2pGabPVrE8CeG_ZntAjPXFtsndQnI_Xcc_wAl561PemUkuHJcOkV-1eBMDYTSVm8F3p-C-GbNGu4bdKGqflwCwTdPy2sOG5ZnAElf5K9dvsiMkQ1jZqjPPTS1XMOvBTDd_ZRrmVxhDTsbG2OMXs2yGExggsGXZ99WdHKXhGy3mWaAaKoN7K1lN9H6LsJ30F3R8X8Q1iugN0Q6zQC3blIQc-L66X6L0gDyawE135hYW5JUH0dB9M8Xf6Y8aC6iaEVFG_rvzwKxhSu3rdqV1ZutSGIFRFZ33QQnJ6fR8coUPw2pNr61t7CZOMF-oRCnJeRc6MKWA2jjIlQJWXQrFqY46iIlYzanXQ9jm3GI5PpkvHkWjq4W00yiR1PJvRjtiM-Yxcc6QCJecIFut_GZaCOyvnBUBinkunB7eRZ1iySF9xrK0BYHkJc6ETMCqMuaoK_6Sj9KO7IaAMCWoiRBfyZVPw3oZXLXq088G5meVHPBvlm01FGAA5Yad8iwnFk9134p-bgO0XwzuhHBP8tOAHwK8E3Mz6-jDym7F8GGPs-pjtbkc6tToFtUBNIq0X8Eyo22uV56roRPvcb77PMHi4vFtH1kxtGwBwabHsQCEX2VenFlejIITfrfbLv9XypewcBw0TY9YddGw8ZTdivMzZnw8AUhdumYZpLxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت همسر ناصر حجازی از روزی که شُهره به همسرش پیشنهاد شام مشترک داد
همسر حجازی: هم خودم را باور داشتم، هم به ناصر مطمئن بودم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/Futball180TV/90187" target="_blank">📅 10:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90186">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
روزبه‌چشمی بدلیل مصدومیت از اردوی تیم‌ملی جدا شد و به دبی رفت تا مراحل درمانی خود را طی کند. احتمال خط خوردن این بازیکن از لیست تیم‌ملی برای جام‌جهانی وجود دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/Futball180TV/90186" target="_blank">📅 10:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90185">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmT4lYyywi89fxl--loiGuWS4Xw0ITh831bXHtAiTCv-XqMf8RP6NtDmRW8NSPn0ulIx4pUrhwYavmSqI9U3n8FXdUvhZ6Jf8m9vcDetmunIAff7r00tRnoX5GP7A_L1vENg1Q9K_DNLsyos9UKwV3jzKBHj_9MCA1Yt3IXz0OpQMfDmhTZDwOmXVMk_QxTtNKM6i3PgxIy36Co0cQE9IGqEQdjjWVwdFKlJcVAN6-N0KNYkr7TWDkU5ecDamSCR4bFL3qfOPGUIx6_Zyw_L8KxB8bcwNn_FonAC1WVa7iw3TEaBc8RgX9ftcNmaJRJDlkN8MgwUZeSCDn6gUKOAGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بورس ایران پس از شایعات توافق:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/Futball180TV/90185" target="_blank">📅 09:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90184">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f849fc0fcc.mp4?token=tPBmppDsj2aF-4gY7NYKF9zBD7gkrwZIkFVs-dEUkbN8YnxmB1KkViGeDCUoa-TedMiArAWIV18_ONAs8PAMPyDc-52nrIeHUmxC6HxeKhaK8aSrhVJ0XjUM1Fc-e5Btq6K5ExA4xRoXAi5mfzoPUHuPxosOAC-6Zujwau2RKdhaOCNRTcMeWg8IZr9D436Y0CNsYLJEGmsNG1aVASp70URA_UY1vDJ3DN-2c25yUnEVlXTDAgTTHJ5N37ytsuLgbsHZWBLtHHgOQSnHnnz7jtJ7YSWuyy04wDeZGz7alIjDS_ORXeoxLxi5mxJbJpNPjmIE9KPXOqrdIiRXJp-XnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f849fc0fcc.mp4?token=tPBmppDsj2aF-4gY7NYKF9zBD7gkrwZIkFVs-dEUkbN8YnxmB1KkViGeDCUoa-TedMiArAWIV18_ONAs8PAMPyDc-52nrIeHUmxC6HxeKhaK8aSrhVJ0XjUM1Fc-e5Btq6K5ExA4xRoXAi5mfzoPUHuPxosOAC-6Zujwau2RKdhaOCNRTcMeWg8IZr9D436Y0CNsYLJEGmsNG1aVASp70URA_UY1vDJ3DN-2c25yUnEVlXTDAgTTHJ5N37ytsuLgbsHZWBLtHHgOQSnHnnz7jtJ7YSWuyy04wDeZGz7alIjDS_ORXeoxLxi5mxJbJpNPjmIE9KPXOqrdIiRXJp-XnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظی باشکوه کارواخال از رئال‌مادرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/Futball180TV/90184" target="_blank">📅 09:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90181">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEfuIyWo8QWgj-VhOgZ86q2zRiZLk-9-YvNVOxQSYuWcot1meN7NYv53_ngxbB2uyP_QBP3ilYC2sJLfJDXTgcWsUKUhpx4hOD1IYKNxlNFwjCc9AoZoGRlZMJsuFJP4QOdXzeq24UnweDZGyWk1RxOy0WTSKUk-RmNJ1wxzeJSdVD-0XQ7CNYUNZIpLH-GnTRVZudQ7PYwYPAHlBUzTI2-XYFTX2P2_h2qLW9sHNtIBCb6HDOwGBCoWjgLygUf0UvEDEBBallAz0yJ7uxUuBv9KTBZDJ_ZsFPwjeTt0LPQcRyghAmOO3ncrGZ8K7DnlDCCZABhCVY9aoSVBT8kHxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
ترامپ: یادداشت تفاهم با ایران تا حد زیادی مورد مذاکره قرار گرفته و در حال نهایی شدن است و به زودی اعلام خواهد شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/Futball180TV/90181" target="_blank">📅 00:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90180">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYJHQW3abhtd0nSxh7E4fynOAx-Y77AgkzxjKR_RW-W5lc5zI8Ms8hyqgHv_Pd67Kmt7uTPHkvoWDFbrwW6LJG-ZXcbOYEVL4Z1hFe1obhVqAe1-SJUYeElzxAD4zPahpYcou9ty8RfuFJoUDsRq-szyjRhuIRv6koOadfPQdJxNS0MUC_PN0NUT9BI8OeOukDMatFxDN1JRCKNAV63Xtqg3_Xm0gk2J-1W3CEjm0EJ6MIhYPMcE5muL52UhDPtpWsr4U4Capr7FOjxwKBa8CBrhux8NJqC-meMifaN6hj7HHyjfGNonqOebQWU3yhimOe6hxuwqdSPbl3_A1l3xVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تیم‌فوتبال زنان بارسلونا با برتری قاطع مقابل لیون قهرمان لیگ‌قهرمانان اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/Futball180TV/90180" target="_blank">📅 23:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90179">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdWpKnPGd0Zc1ZsJZVkxUgVU7Yji94NcZxTjBbQtix1NZIZYlufqeVVeuOVU2GFpe7As8a03iqqziQWi9bxq5CPioXhhPLeVyNHOv78qu_6goQaKSQ60Jc7MoEbAzcZ9Xc1b1pmxXZuAcBwOOZVVWrUNppjsXElKGDVGAuVAXPnM42ZqGfFLzQm7EpmrMBVwwP8Vh-nZxO0G0TOJEXUBfy46vvbL4i41OILD6hsDBVNNE8_UPAeG-koZziyN3-9T5v33i6H3q7KluQB3YUENveLv8RKyABfuBs2fHjfLRiKH2DC5FURbB8nWbOqWcwieGZxlEQ65iTkM5vQuoYujng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون درگذشت پرویز قلیچ‌خانی را تسلیت گفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/90179" target="_blank">📅 22:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90177">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b1b20643b.mp4?token=BWITqOpqh7SyjuypcCStiHREaj0Wg6spifb7rrx8qB3SRjlJhd4vpIB43rbfqzZ3jqFn4mP6Ibb2mU6AaTt19Orns7Gq-rsHkB6Rl392nyDL86WRyniFnctaWLp61guY7BJ78uPKtM0SkaWUtkemI-_lwMiyU0-FzDjr_qYqI9lNZueRwvy7siFTzxTR-W1xstzBflJ286SkyUpuneq51rc0nEe7zzsMH5XhqIHvMvrjCVRWwtWbh50DxVMrAEJhulTtM4LmQwZAIbRwb3ynzc1H_U7JTwKOHHetQEiDlS59Ecg3_pB-DLYqPgjzyLm5w5_ErOUsCLMt1VTOVJbTIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b1b20643b.mp4?token=BWITqOpqh7SyjuypcCStiHREaj0Wg6spifb7rrx8qB3SRjlJhd4vpIB43rbfqzZ3jqFn4mP6Ibb2mU6AaTt19Orns7Gq-rsHkB6Rl392nyDL86WRyniFnctaWLp61guY7BJ78uPKtM0SkaWUtkemI-_lwMiyU0-FzDjr_qYqI9lNZueRwvy7siFTzxTR-W1xstzBflJ286SkyUpuneq51rc0nEe7zzsMH5XhqIHvMvrjCVRWwtWbh50DxVMrAEJhulTtM4LmQwZAIbRwb3ynzc1H_U7JTwKOHHetQEiDlS59Ecg3_pB-DLYqPgjzyLm5w5_ErOUsCLMt1VTOVJbTIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
افشاگری همسر ناصر حجازی؛ علی دایی تمام هزینه‌های درمان را پرداخت کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/Futball180TV/90177" target="_blank">📅 20:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90176">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS7Vapa7fdbu-_Wvln24Vb77u1aG4lRU9F40FAWK9Ph1txJXGl36F7axHVWJtr9Nox20INLx590ZG4p-y9XgVWLHzcxtNm2C3lgTFrdXmnepXD6IoqR-KWWgs-iLNUoIDunfqu9oMPRd64Sa2c-F5o5LzqYdZa2XrKl5Xv3c0wz5dRegYZ5GhNAT6bmNZBAZCIi6g2sc77q7Q_3KPL2rO8WvUMxrH1VOvRtMo_JWbHF-9gBIbS3mo_0cxE6d04Wgo0zyjND0JDvz_-CI_yE9OgmNC6Xtjq0aBN930-mzoF30OHfPrP-c6kOsPzp6tuNtwQH_DnYMJJrrJxyQoW_CcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مائوریتسیو ساری با جدایی از تیم فوتبال لاتزیو سرمربی آتالانتا در فصل‌آینده شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/90176" target="_blank">📅 20:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90175">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa5fa3b89.mp4?token=YAUUhfUDxKdoFNGqNOFZT84oYwoZ9RP55JtibgYsB_UD0DcBS3ZxqJ-0sJ0eim9DKqn4MpchJtLUEgC5PQ-4qCHobISwz9Xo_3W4KhZkgMB8W2B3utGQTAhRCzddKSd66xz6lYDIIOySQXTSwrl4uUnbudtVNCOMTJfbCNuJfTeexcQeUfWZ-YOM2gKr4sFrNtxU2Lw3ZR0weWuLuZQROwqr_cKOglW1dYgfMlkkYxTewHQlAF8sdpIv74iyNv-t1qRk2ojyqpNMVqnxFpMN8-Jo0vTVhtHBu1un6YtaXoYoW93mN1-0NLrr0wlRV47taXE6JgpfzBh2I6d8MQidwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa5fa3b89.mp4?token=YAUUhfUDxKdoFNGqNOFZT84oYwoZ9RP55JtibgYsB_UD0DcBS3ZxqJ-0sJ0eim9DKqn4MpchJtLUEgC5PQ-4qCHobISwz9Xo_3W4KhZkgMB8W2B3utGQTAhRCzddKSd66xz6lYDIIOySQXTSwrl4uUnbudtVNCOMTJfbCNuJfTeexcQeUfWZ-YOM2gKr4sFrNtxU2Lw3ZR0weWuLuZQROwqr_cKOglW1dYgfMlkkYxTewHQlAF8sdpIv74iyNv-t1qRk2ojyqpNMVqnxFpMN8-Jo0vTVhtHBu1un6YtaXoYoW93mN1-0NLrr0wlRV47taXE6JgpfzBh2I6d8MQidwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهناز شفیعی، همسر اسطوره فوتبال ایران ناصر حجازی، گفت حقوق بازنشستگی او ۲ میلیون تومان است.
او در ادامه با انتقاد از وضعیت مالی در فوتبال ایران گفت چرا باید کارلوس کی‌روش با پول این مردم به سطحی از درآمد برسد که بتواند برای خود در پرتغال جزیره‌ای بخرد، در حالی که ناصر حجازی در آن زمان حقوقی بسیار پایین دریافت می‌کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/Futball180TV/90175" target="_blank">📅 19:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90172">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba990f9ec.mp4?token=eA1BjnpEy8XhUANK5b2yeMnxdbgB2HYCW-l5kMjbAaYzltogxt149vRhir0yERYYWEvPZIV2gwx7gfTai5AQFam53icQsWwGnDgZqnguCXPCuls2vcxEyk9tD4eFVR04BW_1HLDvyoxN0V3WVmOo-CqVxdezB1tYZZgdJ_Ss2fikPIoZZNiwh_VP-9iEBXaMg-MMI_xvmKIXnhW8Y_ScKIsfFh4ICkM9w_ie3HDiVcAbm6YVjuQ6pMIOahyLNffmllXrFNMBg1iBxmI1iShbfJoAilZe_6xdRMvQKWcOX045MBDV2yC9DvSceuWbM7Nl9v5lCtSlVsM5nxxdDzIngQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba990f9ec.mp4?token=eA1BjnpEy8XhUANK5b2yeMnxdbgB2HYCW-l5kMjbAaYzltogxt149vRhir0yERYYWEvPZIV2gwx7gfTai5AQFam53icQsWwGnDgZqnguCXPCuls2vcxEyk9tD4eFVR04BW_1HLDvyoxN0V3WVmOo-CqVxdezB1tYZZgdJ_Ss2fikPIoZZNiwh_VP-9iEBXaMg-MMI_xvmKIXnhW8Y_ScKIsfFh4ICkM9w_ie3HDiVcAbm6YVjuQ6pMIOahyLNffmllXrFNMBg1iBxmI1iShbfJoAilZe_6xdRMvQKWcOX045MBDV2yC9DvSceuWbM7Nl9v5lCtSlVsM5nxxdDzIngQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
دوم خرداد، سالگرد زنده‌یاد ناصر حجازی، اسطوره باشگاه استقلال و فوتبال ایران است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/90172" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90171">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFs7tRcDan3H-fDeZPZphcEdDFC7ZOPHBJkvxynZmWj8_3o7XUs93Iwtqww7dUfHsdaI_YTlt5vQjNYjjVKrgf5mfGJ7-vR5o1etXzSDRS-ubpC6qXoRrKB8OFGMkCQuB6ZP6oplDb4uELBDgPQB_5VJhGV7DBBbP1IGi8q7e9FOJyfHJRtUGJ-V_w9Uwl4cnKLdt3ZZCMi9W-TVIgwuU7CzoY1twbJCiEoLBA4y9AKzQm3JMN8Akimhv84xnzLw_EHZHNv9DjD2Y5NvdAUUFbVSdIIyP-a5cIZUEuQv1ENCCodSwbJ5X51Vrkl50v4B30PvuI_OCSbqRcHkYCbbjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
تلخ و ناگوار؛ درگذشت چهره افسانه‌ای فوتبال ایران
پرویز قلیچ‌خانی، چهره تاریخی فوتبال ایران و یکی از بزرگ‌ترین تاریخ این رشته ورزشی ساعاتی قبل در حومه پاریس جان به جان آفرین تسلیم کرد. قلیچ‌خانی متولد ۱۳۲۴ و در 81 سالگی پس از ماه‌ها تحمل بیماری از دنیا رفت. او تنها بازیکن تاریخ فوتبال ایران است که سه بار به صورت متوالی قهرمان جام ملت‌های آسیا شده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/90171" target="_blank">📅 18:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90170">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bc3k5mEzTLg2ssE4vziPPBl1ja0GGounmzS489JA_14-7q2iIJJmihmJv2zVsQueKcaLpxJxKEwnU32ChMfm6NFp7gtqrSbO4fHqjlFMnGB0Tsu_GvsEwO08E2f8YVgI-thFrPZAGdw-iL4gcRk75Zx4xnszJLxms0WS9TXEKUe-3pk6gzhGR1h5RGJEWN2wfY3Lj5aMQyjipNPh2zx39zg8RkiL8TUtPVtgQwE8_NVnvNIjgqaG1d0UwXeqw78-f9iV6eXpA5EpdZ6CvlIiEuLVTd2e0wmcWliPiKLQXFr7wJIF9yFHMiapOWEGfY33Jm0PFTDFQxMl5Eh8Pr-NjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
عکس جدیدی که ترامپ منتشر کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/Futball180TV/90170" target="_blank">📅 17:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90169">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=Dv1C7pBOvYgR03lSGXej4xnR8290H7Zqa4OiKEjY8030u5M1N3KZUe6VhhEomgxb4g-2wu-_6ueviJzMa4VKtAJs_KTEHyhpQkPS44b8RucdEGxQKOscPMdGeS7-3r9mpsNJIn082qNdYHiDGCHf05evtf7KkZvHE--A9iCf-j0aAGF7d20Gkqui2II-ewgZhYCMKTJV-HRXPCSB6Cy5bwRiJpm05OUhrFlgyX3kzcLk-YqMFJ_7-RmsneWsrNsxpXEMaov0qXWio-q9iLCvD5tis6HtM53bxUJAsyEc9e6eV7-PPo2lsiX-IidxPgxwLl8jlUDb897JxTfBjVxZPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=Dv1C7pBOvYgR03lSGXej4xnR8290H7Zqa4OiKEjY8030u5M1N3KZUe6VhhEomgxb4g-2wu-_6ueviJzMa4VKtAJs_KTEHyhpQkPS44b8RucdEGxQKOscPMdGeS7-3r9mpsNJIn082qNdYHiDGCHf05evtf7KkZvHE--A9iCf-j0aAGF7d20Gkqui2II-ewgZhYCMKTJV-HRXPCSB6Cy5bwRiJpm05OUhrFlgyX3kzcLk-YqMFJ_7-RmsneWsrNsxpXEMaov0qXWio-q9iLCvD5tis6HtM53bxUJAsyEc9e6eV7-PPo2lsiX-IidxPgxwLl8jlUDb897JxTfBjVxZPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پادرمیانی همسر ناصر حجازی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/Futball180TV/90169" target="_blank">📅 14:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90168">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-TsjEis0fNt4NBnRTtsX5ChZxSDoJnN6Ik3DXwu0tOng5DEjok_M3UV0E-ln-zn8xDI2qx1jRW61VA2S1X-yufQtS5oHenasdI5nhs-7f6w3pT5dtb3q_3LPuIltAWogFIspQA5Z1VjIN86GiKTP4VQKe6HVdlus0SO3h6LZoqPYOFPGKhE6r_uzW0Fp-V_3HxE0s-of7GCACfAeCQ7VJf6hibnsgjdUY3Cy9wFkCftpXPBIlfEX3TgbpEl29tbx5cyld_x_PLkHijMCV2amGElQSQK6uAb6NROzx2038dtZc7aDurQRM1Ng1p1UVtYjt-1x4vTidTRQnfhMLItAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برونو فرناندز به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ پرمیرلیگ انتخاب شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/90168" target="_blank">📅 14:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90167">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw8FgnZMhX_PHCx2KzHhOQdYAih1NZ0UXyPZTaIHeeT_5MRp_-kBWj3VnJtewwe9aknpeuDPy3Gsfjuh5Z59g2ssimuLx4ABQ0KHvPuZSg3kDCbtKAot5NorrB9-T5S9Jp_NN0sFBjrUj4xuSLYQ7RLDcwfoX9ieUulYx3kr5pB-RPMarQDj0g4FFB3ok2fM-Lvc4Uo_ru_d3g8f4BSwWnKkCdnK3qy9HEY8QNva_5tNNIoGba_pohPB_8kHvapoivnL97IzkhTganjVVGSEQ13K8XVSS3wfedjl_4qOA_Rii2cmU9eaE7CJq_WJGfPseEH8If26j8FIl2VoXBLn7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گستون ایدول (روزنامه‌نگار آرژانتینی):
🔻
فکر می‌کنم ۲۰٪ احتمال داره بره آرسنال، ۳۵٪ پاری‌سن‌ژرمن، و ۴۵٪ بارسلونا.
🔻
اگه بارسلونا واقعاً می‌خوادش، باید این رو با یه پیشنهاد قوی ثابت کنه. تنها تیمی که واقعاً قدم برداشته پاری‌سن‌ژرمنه. بهش قول یه حقوق خوب دادن و پول کافی برای مذاکره با اتلتیکو مادرید رو هم دارن.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/Futball180TV/90167" target="_blank">📅 12:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90164">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=lFnokj5EMzTVYz2F4nQUmbqM7Prh5IZ2tI6chn3qDs7Fh1AqC3hvHEfw81wVizrR2iRmwOizYPPKIY3tgrVw4jnzGteDxFBIDdtBZfMj-GLY6HFCI4DjnOdHFZmPgzYuRgRcrOXFnHw3wraobinlYXOFVkNMJMYpBqb8s053-g4obmyAybRjlbe2rwtc4r_9Ju0yPwPHW9NCS675VvKlHsCthHrg4fD_0rCqtfAF2eDmlSG_Deq3-xATl5E6QN7QaDrIkS3sCXuA-zA-8CES8vTVW7U_Lx8rLDHOxNgpxleglDneKkSiKNDMyA3tvnfh-fVfxHO-bj7louzL3jzIr0U-_WsvFJUSNGlHHDAw9UEmO6tVP0tNGgn6VrsDgvgLxlJn2inPoXqelt9dWNUPEDwMFD2rhibKP2RP5Cq_i6dl1Gqa-US_tshDHj-O4CbBkTKYQcc5_OeSDFZpEfglQ1LqhTeKQ2KAQpBNDNiKn7FMzD7ZvhG20vFvfqkwZZvF0FylVg-71Mhi-hjg-qypUhjsPYqylFX1SPg5GJbeUemFlQcFMNMMHiWlBx9noOFn9UCNi0suAbGlzkj0UChv7C_hD4oLXDlPE5fp1RkqWqmPnyPiX6r2nn9I2OspF8PZ_XO98FJS7pp_voUotD5aK1BNCIiVVupaTQSJdB2yhbM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=lFnokj5EMzTVYz2F4nQUmbqM7Prh5IZ2tI6chn3qDs7Fh1AqC3hvHEfw81wVizrR2iRmwOizYPPKIY3tgrVw4jnzGteDxFBIDdtBZfMj-GLY6HFCI4DjnOdHFZmPgzYuRgRcrOXFnHw3wraobinlYXOFVkNMJMYpBqb8s053-g4obmyAybRjlbe2rwtc4r_9Ju0yPwPHW9NCS675VvKlHsCthHrg4fD_0rCqtfAF2eDmlSG_Deq3-xATl5E6QN7QaDrIkS3sCXuA-zA-8CES8vTVW7U_Lx8rLDHOxNgpxleglDneKkSiKNDMyA3tvnfh-fVfxHO-bj7louzL3jzIr0U-_WsvFJUSNGlHHDAw9UEmO6tVP0tNGgn6VrsDgvgLxlJn2inPoXqelt9dWNUPEDwMFD2rhibKP2RP5Cq_i6dl1Gqa-US_tshDHj-O4CbBkTKYQcc5_OeSDFZpEfglQ1LqhTeKQ2KAQpBNDNiKn7FMzD7ZvhG20vFvfqkwZZvF0FylVg-71Mhi-hjg-qypUhjsPYqylFX1SPg5GJbeUemFlQcFMNMMHiWlBx9noOFn9UCNi0suAbGlzkj0UChv7C_hD4oLXDlPE5fp1RkqWqmPnyPiX6r2nn9I2OspF8PZ_XO98FJS7pp_voUotD5aK1BNCIiVVupaTQSJdB2yhbM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
یکی از جذابیت‌های فصل آینده لالیگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/Futball180TV/90164" target="_blank">📅 11:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90163">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
⭕️
شنیده می‌شود کشور آمریکا ویزای مهدی طارمی، احسان حاج‌صفی و شجاع خلیل‌زاده را بدلیل گذراندن خدمت سربازی خود در سپاه صادر نخواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/Futball180TV/90163" target="_blank">📅 11:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90162">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwlXRK1n0oKJiwALUFTl9RdaNYjDshZbGIiuMux8NCy9KROWZATt-czHQvM0eBLv4YYeZf3fSRcb0moYxupGikp-w9vvArtN2JYzvvcFtHUSGYHBkKwm0BkeLGhswsqnfyleKpyuolSnatpjt_CrqK9CwRchjmeK1zMM0ADbnCE8hvoVmnwTwXYs1xCitC4cnn93vr5cs_MlrCo55nsZaIr_62xZB9GpEKuvbHD4tCw0q7M40rQtQKNhC1QRZQJcoJCZBzq9_ohN05SngUgCAD0FfHUSKxXPiGOyzp6JoGg_dnnKiWLevk-b7pejvPVffkoeqIYvxc6yy0p7mmuCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توخل: این فقط یک مسئله ساختاری برای ایجاد تیمی متوازن است تا پنج بازیکن در پست شماره 10 نداشته باشیم. حتی اگر این تصمیم دردناک باشد، معتقدم که برای تیم ملی انگلیس تصمیم درستی بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/Futball180TV/90162" target="_blank">📅 09:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90159">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=gln4m3vP87fvesYddGN0Zfuodufw67hoh3C1Sm3OfVOf-ghwpF6h6-I2G2NR5tRjB9_9-PlFVpcJybUZyXj-yp0Eh21WuYXt402ZlDxx_w87HafH5GOMgmO0gVE3XaTcA2iVB5O90z3PGxxnahSGp14rEyXm0G8odEAxa3m3T2CPqknsRQBYO34q9asrt2fHlpNUaog9rqNSIrIRVHBoEZRAiVx3wW_vnRdAeVy-A7Qh1CNYa6XsbTyGTUnDPV96PeyPsSi9oGBFLyG63TLMA0MvB6tm3dDsv-K3W7RVoS1p33hzJ-G63ejaL4NKWi4yZVTELs01tGfs7aHjlcyEhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=gln4m3vP87fvesYddGN0Zfuodufw67hoh3C1Sm3OfVOf-ghwpF6h6-I2G2NR5tRjB9_9-PlFVpcJybUZyXj-yp0Eh21WuYXt402ZlDxx_w87HafH5GOMgmO0gVE3XaTcA2iVB5O90z3PGxxnahSGp14rEyXm0G8odEAxa3m3T2CPqknsRQBYO34q9asrt2fHlpNUaog9rqNSIrIRVHBoEZRAiVx3wW_vnRdAeVy-A7Qh1CNYa6XsbTyGTUnDPV96PeyPsSi9oGBFLyG63TLMA0MvB6tm3dDsv-K3W7RVoS1p33hzJ-G63ejaL4NKWi4yZVTELs01tGfs7aHjlcyEhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ترامپ در سخرانی امشبش:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/Futball180TV/90159" target="_blank">📅 00:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90158">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tv4e7GUTaeWMX7pERO1eTgPM2-bIKQUcmo6O_vb-pi1YZ_8abXYw0cd30zexVtITB5BmmjHirCKKIJD6BrpEOzRhuK7qOBuEQDtwuIBUeWFDdp0h7otnz-RlzITNUO0PkZsA27FxV0Rpoeu3d0MsxMqTrr41WV5N8SmpJMEkC37r71X8h4HhnFujkFM6URfRoHlZAmFcQY24wxtrJPYQpAvforTeKr-1GcnLnr55HW9_VAWPpGlHxNQgg6xmc8HSU2CDs4Kg5_LpeucLODvkTYUMY_BSpVp62WNbUqL6npTCg3F_je8Brt6l1p_o7kUmBwQbQ0BdyDZMUDnNBns7iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی کریمی خطاب به شاهین نجفی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/Futball180TV/90158" target="_blank">📅 23:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90154">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sD8MCUWM3qVTa1cH1wnHANh3gr1WHAEMiDydZw-SpzsepSlSv6MVhIfCPeu6k8XLFeqyf6dYb-aN1OMsQDWoBv9VZ9Na6173FcDgKwBBrLtNoz1i9dh2UFbFvdAjyIhM0uvB9oVAPKqAW774ZfO69XV2Z3-yHdLcq_9_u4XU-fieHO8pc0QjsAuyIKiYekoxreym-Ao50I_eIfIFq2Msy1mTR1tEqhVCvPGzoJ_LOYXyiDNCzZu3eJOG4sCjlADCiE83mfusVd7ikPAK9Dt9kPiGv6VG93R4kZq2oqgvDeCpeghAUkreElOh1LFKRjzWR1NELGOz1o3X8k3pVrXbVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmaNyRrDaIyRAB86Q0Oy3G8xRsZEcN5jnR65okZ9JuyI58kRTaPjF4qR9o_IKnZK7HTDlCT5vtizZq3HsNRaJis0sxiRxcYUOSLpunXUYAMhAQTJba6ES7Bg_hZu2mnvuI-XTgBHo7VwYamcgRR_QVfFpGz2SjNoLKEtsERxlFlcoSf8y12U_YHqf06aE4UGgDKcZQPbDTLguJkVLoURA_6splEWOVn4-JIIDrw44KvAeNVUw5B7pKBW7fw4mkaVVw354DHGmpMoH4etS_hunfU2UCKd0JUVUV4cOBlA7fNsAAvuOWOPc4mQvE_e0VnaHJxXmf1sNbXLpWwSof_4lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YJDY64AVA0KRDlCRALA5mTvbpPR5m6tt3hLXDikVGkaozFwf9YPY2Ub_yTTu8m9Mh5lRk43AW10WeY5ra_VfIpGO3h2ppAVPtizYYC4rmFZNE1Gj0B-3RfWrJKNaoelf2uGcq8aNTGL_rm9xBcqsG2Xq_bGTDls5LNoAEPTDpVT_Nogci2rFbJrkkkvXj19yzTNH9axaagpEpP1_PuHVM05HAjO5OIeroesBRTZakAOnNGUOqrtgDrWehzF-GK4pIHwt5Jt3pb4ke0Q5sviEqLcepf2MhY8LM9xvjOKEwwa4g09141tGmw0yW_5rMhz8MK-ZurEbvA6ahdcpJ9FI7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عناوین برتر سری آ تو فصل 2025/26
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/Futball180TV/90154" target="_blank">📅 20:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90151">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
العربی الجدید به نقل از منبعی در وزارت خارجه پاکستان: واشنگتن و تهران انعطاف کافی در پرونده‌های اصلی از خود نشان نمی‌دهند/ سفر فرمانده ارتش (پاکستان) به تهران ممکن است آخرین تلاش برای جلوگیری از بازگشت منطقه به جنگ باشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/Futball180TV/90151" target="_blank">📅 19:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90150">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHXMXs_g6ykSsScKMkAzgBHZsIZTenQk2nAYuSWl6c1xu0AqSTY9-PcSI-_qQH3z-JwvHgm8L8AeAGQ5Gt6koiRN1V_VLPXa0U1zEnf195csjYHRd71x81Al0ZRyhncPeuxpDy-b14EgCNFU6hkR-VTekPhiunoeYb9VmDrXg-FgC5PmihtLtT3sFpI5ANSwunZsS2J6oEJWwA4wejkynvCG_E8_h0awxE2meSyAarT59OG_ZI1mA_y4lbrXCYxqFsMyj5XL9NOdHeixdEh5hZQhUDaiiZoe5R-kcZQ4rBBQ49ETP7NzPc0lisKBTEWrSbRMMaqy6awiCY7mmKS8TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ کیت اصلی بارسلونا برای فصل آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/Futball180TV/90150" target="_blank">📅 19:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90148">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🔵
باشگاه استقلال مذاکرات مثبتی با آلومینیوم اراک برای جذب محمد خلیفه سنگربان جوان این تیم انجام داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/Futball180TV/90148" target="_blank">📅 17:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90147">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2EsIF5UGDz8W5ui6sgnQPexWFDK6duTSfqOGqEHxsxxWrweFtpZHOnLv3pPxxCA6YdDKr0vD4Fzf33Xcjx8MozRtkMz21Y2LkDxtbWGJZ6k7xq-mwtE6HlqB8_zR8w1cmvSWzIO7ElusYCxQw29zG_dt_1lkzA9VyBGlY6q9Wg3cMZBxWMUHN6-RL5FjfrKHtaWhicz4A5s-WNGdgm5Y4M2r-WWu08ytOVejJXUFF7RK6rbnhzcl4DPvjt8YaHOAyFk0j4ZUQIgZ3BrwYqJrgZbPAoYMYb89fqG6_JmAqeLKsJUJTnhFU8LPBFYlnTwLQjqkMNJUUlsruQTuPmE6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب‌منتخب بازیکنان خط‌خورده انگلیس از فهرست توخل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/Futball180TV/90147" target="_blank">📅 14:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90146">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnEP3XV3CZZbNLETYm1v-p0GkWwf5k42oZSiPuMUGd2htgbg1kFa2vuXqQ8mgEMMul6BwS3wqN72v8WkXoQJ7-bKmEQGTR-DC1Fpqvt47nfP4rn7LgMH_uQErounoJgRbcevIXWsgJE_rLzkoScGkAaz606g7nmaLuGZu97kbTVQKVBmZTA8AVkD6_533aTeHTDLE_zGrVu3bYGluAaxJDuxevevXYmm3bn1Cng7-nslJ3TtnM5sCxBA7_2xXoWxMBdwXSP5I9u-s1By3He6eRgElYvzog9mXWLUVSlGu3sOKr_yEbmhFC0dBMAUIsxZiVh_B2BWh9Lb2Qjg0AgTRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی دوساله رسما سرمربی دائم منچستریونایتد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/Futball180TV/90146" target="_blank">📅 14:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90145">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clqX-RGfRx0HXQjLLPFTpw9GqVMJ17JmyOCb0oqO9cuK7fW0JAN0hibUx-30kCu6Dks5lamZF5g8sU-F1XKkCV-GGblkQXhDZ-e-lZ_A3WrRoZ4_Hky48ONzielGaAIGspLX-_jeBfuAPOa1KRMMHOPDbbhWTHoSw-ChXPKOxBeVj68v879WrpVkYc4366pEBnEkJfiz_QyDjL8GKmURw8llHwG978j6jQD59S6cbDb3_B2M6Kg4c5hvLwuZuwheVRZM7Bc3TnRRKHpfq3HhgIk4FpDYcIPbL5knFRTlTzRKn_9TMPLcQcVU6lbD8oEfnAWM2nWjvHaO7PD7XT9i0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمی
؛ پپ‌گواردیولا از سیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/90145" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90142">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست تیم‌ملی انگلیس برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/Futball180TV/90142" target="_blank">📅 12:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90141">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1gNTtZ0evG2K2Wvrqhh1Eyb8rd79J53dr6VAO0pH4La0ksz0AxN12p1OzseagLtOFM2EZQvY9zt65L00pBMWN3RIUpSl89a1gp5aI4SetapmpS1HL0dkyPiWmq5ZIGwGdzGfDRmniGFwe1x46LQCcUEam1sTTXW-TisbvZKPS4I4vAr5kGUEBfPWYYHt-FuYA3SLsFPVroY1s92iGosXJsoreSwk5iD-d8no-MfxoTwvg065dCPdV0dAt9nGawMZK--wJ_TryHf-9Xm-XIOdU0ibmi0FHcvkQuH2bskRgud6sW00Hygb-xOOkXC8sBlnYQzb4ju1sjwOJ7xHYIgqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست تیم‌ملی انگلیس برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/Futball180TV/90141" target="_blank">📅 12:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90140">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🇪🇸
آربلوا: با عشق و احترام فراوان،‌ فرداشب پس از بازی رئال‌مادرید را ترک‌ خواهم کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/Futball180TV/90140" target="_blank">📅 12:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90139">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🟡
باشگاه سپاهان با انتشار اطلاعیه‌ای با کنایه فراوان به سایر تیم‌ها، عدم صدور مجوز حرفه‌ای خود را تایید کرد و بدین‌ترتیب باید شاهد تیم جایگزین برای طلایی‌پوشان در آسیا باشیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/Futball180TV/90139" target="_blank">📅 12:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90138">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
❌
در صورت عدم کسب مجوز حرفه‌ای توسط سپاهان، یک تیم از میان گل‌گهر، چادرملو و حتی پرسپولیس راهی سطح دوم آسیا خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/Futball180TV/90138" target="_blank">📅 12:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90137">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFrhcBqUhGoLUQk-Dyqu0uCwrF_BQMtbHuLHgzNSKynVcAVdpBtpEVNBEEySFpGn7_lNpkDdiQzJZIbJBZLTJ_VeH_AS8T1UG2GK_aPNxwl05EpVB1lLyYexy-YeAdWtL4dmBjpdZnZnHbzA1GEqivzatn1A5bUUd_oY8OG2A8aa__9MjGnvELyVfbdr1d9U9V0sl0FiuwYXgctAEMrjmOtDLbAKXo3fHWbPEplUKUqNICHyVHNoDCHI66XF4hAYmSUCB9rJyNmTR8xAdtRaAktjjAtfP8r-pyXtqKTBAwQU4t6-BKe4rzllridrMRlAsaejb1M7KINefOx9jdjIXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کیت‌اول تیم‌فوتبال میلان برای فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/Futball180TV/90137" target="_blank">📅 11:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90136">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
❌
در صورت عدم کسب مجوز حرفه‌ای توسط سپاهان، یک تیم از میان گل‌گهر، چادرملو و حتی پرسپولیس راهی سطح دوم آسیا خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/90136" target="_blank">📅 11:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90135">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZTdlZTBg-V6D6YNkQjz4GCs7EWQlJ8qoKjBf66_RM6t7AeTs8VAGWYrUGRH-rEr75wRcnkK_FkAh-a7t7YTBKH14eCDbAGqxxANOyhCudB32VP_dcMdvvRG9Hglj88E0JgF3egLOJgheBrirIkDlUaGWM0gVrUbKmOIaUZTrFhMoOs3H0sNfdFaZ3DpL_uzcRZO6nBxKru5_d5tlyWaW0ACENjSUP2RIMeb8PPGH0WhNl9CkM8Dg5CGbPtp6ylJDL__C_Tv_3Di7A8qWu7kLXQFngU2zr5mFnE7EVxdEn9aED46kI46OC3yAGZPX5fUtG2iJbn59Vyrluzgp8DBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
آرنولد ستاره خط دفاعی رئال‌مادرید از لیست انگلیس برای جام‌جهانی خط خورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/Futball180TV/90135" target="_blank">📅 10:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90134">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWmAr_QZj86uIHpmilFVfspFkbl9Ik94uCMWDtVHAMOUxP9TiIkaqwGfZG2TnMqJ5R6J7HvZmd4ASzzmiJa6TpsPg3RGsmNHlUKIq9abII431oZaHijQBXVBA7pyirvEwk3-jljGebAKpS86JPv4ednYinnCFU4Ev56UZI1HNqEeLgEWwu7Vdc57L8_9RBsGI1fYq7UaMgR6HltbuN7tcgSm_HirQX5osyNkJROMT5NXIbmckvME3D88Ec0hUarCQc3lvaaC8m1ruAjT_uvlrCkQosNmZbaCVkHyFgB3S5uEkIW7HvxA59PH7pjRmR9ZWERSYtV7axQFxics1QFvUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کارنامه بازارهای کشور در اردیبهشت ماه:
دلار ۱۸%+
💵
طلا ۱۱%+
🥇
بورس ۱.۷%+
📊
مسکن ۱۷%+
🏠
خودروی داخلی ۴۵%+
🚗
خودروی خارجی ۲۲%+
🚘
بیت کوین ۱%+ دلاری
🪙
اوراق بدهی ۳.۳%+
📜
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/Futball180TV/90134" target="_blank">📅 10:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90130">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=XeJMnIJp1bGQVwc7VjaofG6UvN2HYi79RLigUnBpOfvkIhox_rZbrcnnQCR9hmyvA1-9LVL4tfM37td6e9DuZwcIueqaPJiChDGogzqC6O2BDqTk2HfcEpnbqRbONOiB5FH3KiTCLp49ec7BwCPtcH2lhLtsEALCWqnbT0SOBQBPMC1AtZ4qsA7ywc1CV8XGPCKa9-0xU3iNoC67KhBRXD8lDwW9Ps24IQAfMVKxOerbpMcdL7iFZrYqtEwu0AbocImSxYBce5RrcG1NTbvwShMdqytOVKJY9T0Dntp3eM_tJ9BPC5b4YF4oHzjn54kWyujr8gZofeu_2ZMDh_t3Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=XeJMnIJp1bGQVwc7VjaofG6UvN2HYi79RLigUnBpOfvkIhox_rZbrcnnQCR9hmyvA1-9LVL4tfM37td6e9DuZwcIueqaPJiChDGogzqC6O2BDqTk2HfcEpnbqRbONOiB5FH3KiTCLp49ec7BwCPtcH2lhLtsEALCWqnbT0SOBQBPMC1AtZ4qsA7ywc1CV8XGPCKa9-0xU3iNoC67KhBRXD8lDwW9Ps24IQAfMVKxOerbpMcdL7iFZrYqtEwu0AbocImSxYBce5RrcG1NTbvwShMdqytOVKJY9T0Dntp3eM_tJ9BPC5b4YF4oHzjn54kWyujr8gZofeu_2ZMDh_t3Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی فوق‌العاده رونالدو پس از قهرمانی در عربستان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/90130" target="_blank">📅 00:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90129">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPfwp1TpjhDZ1PCcofcvWYp1xS8edvyqtoW_WwfzXfxjiWdDLGvuKAJ2ZZvrH8jibYnJddEFSOpOxtcD23sV16dQxKTJ7qpcjpDexSmUbjYn59jH-7i7QyOwyz5JQ5FBjMu_zyg0pm270efFQdF6dfAvZ7SJExD1frMhR_e6ulzn-5P6dPyZn_HWWqoNFNWovtz411Zd44PIYWTEWq4VaeknyX1s1X5CN2jbiIp_bey24yQf48Ep9jPQmbpdhgVp6s_dwrJu6xgZvl8PAyEWy3DvZfrgKCZbZRyyK17y0zQoIJA5E0RdqJwPx7ZzRa5N96oFh6xd4RcuOUljVW_UGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
النصر قهرمان لیگ‌عربستان شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/90129" target="_blank">📅 23:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90128">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtDzuiaoOacWV0FovTYVHQwUUCKd_rMADTxIACo1g-DatKzVdZ18ACmVA0TAX15HoYa2wDAetTQpAJwNZqKHLBLQib_Vb3Svlp1NqHxJ0HZ_zo58FU9KmQDFEzC6z3ow4ofaXIJVvdU26WDKSUUllwLg6_yvW1uKz4lMa92NJAYxcWcXyl8ZoovRinFSALA9vxWfL8Nj2G7KGTUv2JcFj6lZLYvf5VPAiG-9pJZWehoMH_ZwPrDHxD3NpmY5aE-SI8i4uAjEsSLCLJ1I-aHDBHh_4IOKcEHM8mVT_kG3JNm03jGxenLAIko9CZPRMwkzWcMyWp9XL6Pn4uAf9SnyVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقدیم گل کریس‌رونالدو به جورجینا همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/Futball180TV/90128" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90127">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=Y8xsAy4WHfBmjTG-KteYP8Qsn2rBaSrqtT0loJIwyC1csoNuudbXjCcFiOscsb25CrE2AGedFVBqGAzWEOHSlBhaH4dBB1vhlbiWgJKbOc2Vk4oj6VN3M9Krt0ZuwBMcRqBeet3iNsG-1sYfwSYm3foBDpaIZjl7QVILujXtJn1wAGKlF4oJOEmCWA5A8CLkEiHe4uamO-JQCZ5C7KNRBgl2B2cdqsy1bNZ_Kdi_ALIfHBmfqhI9Fzn4uOGWFj20wd30sZSypYH1LgMi_YPwElHiSO4pjwWF_5bQDsCDmghgu4YryPibY4CeMMre1AseMTHj1-CtosTaVR-84XFNemwqNHasJl2OSq0EJeqhmnWRXvUcDhYeXiUUFhIgTKSt6_P527rMIIMpYboovC7IBl5FX1GXzBhVRe3av84fuiR6VHGdBRm69Q4OqWGZqxSQJYsNK1EHgELQ1h-mYPmgygBDT_Hob34V_EL7X0_OswNe7K-mEVheregHKTcXo8g3He6b3Z8-QB4y7lTu7LT8QXePnOiK2qzcaCNSSWXHF_o_G1RBrz8ebE3jo2qoCEcyZhz294AF4F7A-5ic3u9lsLq-rUGPrl8Xl_Vsp-LhBFaPZ_oPPKYNoINqj4bfrb3fSDhcHAMQTYQrTzUklAiyBBW-4aLW62qIcPqfgQ4ajrE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=Y8xsAy4WHfBmjTG-KteYP8Qsn2rBaSrqtT0loJIwyC1csoNuudbXjCcFiOscsb25CrE2AGedFVBqGAzWEOHSlBhaH4dBB1vhlbiWgJKbOc2Vk4oj6VN3M9Krt0ZuwBMcRqBeet3iNsG-1sYfwSYm3foBDpaIZjl7QVILujXtJn1wAGKlF4oJOEmCWA5A8CLkEiHe4uamO-JQCZ5C7KNRBgl2B2cdqsy1bNZ_Kdi_ALIfHBmfqhI9Fzn4uOGWFj20wd30sZSypYH1LgMi_YPwElHiSO4pjwWF_5bQDsCDmghgu4YryPibY4CeMMre1AseMTHj1-CtosTaVR-84XFNemwqNHasJl2OSq0EJeqhmnWRXvUcDhYeXiUUFhIgTKSt6_P527rMIIMpYboovC7IBl5FX1GXzBhVRe3av84fuiR6VHGdBRm69Q4OqWGZqxSQJYsNK1EHgELQ1h-mYPmgygBDT_Hob34V_EL7X0_OswNe7K-mEVheregHKTcXo8g3He6b3Z8-QB4y7lTu7LT8QXePnOiK2qzcaCNSSWXHF_o_G1RBrz8ebE3jo2qoCEcyZhz294AF4F7A-5ic3u9lsLq-rUGPrl8Xl_Vsp-LhBFaPZ_oPPKYNoINqj4bfrb3fSDhcHAMQTYQrTzUklAiyBBW-4aLW62qIcPqfgQ4ajrE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبل رونالدو در دیدار امشب النصر مقابل ضمک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/Futball180TV/90127" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
