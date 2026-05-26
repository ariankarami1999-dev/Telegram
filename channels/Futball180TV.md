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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 01:19:54</div>
<hr>

<div class="tg-post" id="msg-90255">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otW_lbD7_zKRILGsNTJiDsO4xPkC9nMAGHL5kZTz8PX_j1potRSAp9r8zD950KViOYF0OCD_HXxYeLQX8gzuGEkDQbPCuSXeQwYBqYTOpcgaubvQKuBow37BGpsXlS5PVM7bRkwaZ5PSqkcQQBP2fInHgQ2opNf-YXTSvt47LjBIP5nHpDc14PNxa7cJyDDZnh09NqxB2-DSNYeGwu38JMz_jqkaIhrZGchK1Clc1KLQt22eMRLd1yBAWTE6IjBtuxkS0E_jerEqJGmgsJMzqRRR4XrdVT2j2os5cjECvBMasEcQXncUWY9f69PL8MIZTF_hdmPflCJwAchJ3VDAZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکل آرتتا بهترین سرمربی فصل لیگ‌برتر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/Futball180TV/90255" target="_blank">📅 00:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90254">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔥
برترین گل‌های این فصل سوبوسلای در لیورپول
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/Futball180TV/90254" target="_blank">📅 00:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90253">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsjaYvtQcrNXuEXtUjP3r392s-b1I0c8pNv70lLZOQORh6soYezQXLs3GDtSRyW2amFxf7PkN6yOxlm0j8MnyaXa0-wlJNh0CxBdPuE332I9qVXKWYXxackOUfeiQmU9UwwFxDOm7MXH7j1Amm0VJoifIhZPjIfZEFMZ2zwLA816q_-Pio1VTq6wil3lgaSMVP8IIqmrY28d2iYLkxbijfRYm2N1v1-2xrCp--jbsvokOZhCNkmg9CIEqJVIDxVH37KNEKLTIOPoXwqookXPMZ26DmIS1lcIIgjtDy0zzFXPGMKb_7gi8xuDUq6zjVCGhepev0eBThFr72EmikXixQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الکسیا پوتیاس بعد از ۱۴ سال از بارسا جدا شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/90253" target="_blank">📅 21:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90252">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/90252" target="_blank">📅 21:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90251">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/Futball180TV/90251" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90250">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/Futball180TV/90250" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90249">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/Futball180TV/90249" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90248">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yvp_bRKf5rSoZnkPqyyb_SLKn8SMPgWB2FONvjUNRu4mtwOJ0g4uhF6Oojv6h1Gp21gcmBkTcTu_CiosdFmPAOCBf0XdBj_lt1IcoEnzQvNDhN452hrFmOFPsrbcPSAI8FLQ3XvxqwEWpuLpQ2ifoBd1P8uNtiyX22b5Agzto1K3SnwrmwVFJMk8tqGageM59IoYjjLBwfo8PUIY2jQQNoMopfnL_CY5JA2YpOunD4BldiHaCAVcHEUKztjhctMmwqpThac4igOavQnQBaDW_WRQchwTRuCEe9w-7sV6vouVdQQbPWwDR2P7UcfGBO_zRS4RB8PUrZmLWRrc9s9yRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اعلام رومانو، قرارداد آنتونی رودیگر با رئال‌مادرید یکسال دیگر تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/Futball180TV/90248" target="_blank">📅 20:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90247">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🔺
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/Futball180TV/90247" target="_blank">📅 19:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90246">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niWTgW7LtW2Q4b0unV5XEkhOTTwz36IEklDrlUGtBMWPztzYdybuFzd5eFqULS7KAiINklAXuhH2DMkuM-A5a10upxBZqhXc5bwV557N4j7OYpG4kLxHeAvC5OrFog8-m-8T-ZEwpSPKRgFgoZoemnStMLhWTGAJIsT_YM68_-REs-ZiZMJXIhZrHLhorMKtT1Wdml3HGc1ILmzW5aCLLxJJJBTg_bR2v-J3dElA9wx3WQSYfeoROG8aL2K7-kMuZieqaFWzntdC0PkW8cxOAkVHweJIW4XoHl5ZZDyuVTn_MNiNVD5kkyIqHpi6g4Avd76kgReoZybealISAembbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیدبندی فصل‌آینده لیگ‌قهرمانان مشخص شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/Futball180TV/90246" target="_blank">📅 19:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90245">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تا ۲۴ ساعت آینده سطح دسترسی به اینترنت به حالت قبلی برخواهد گشت. درحال حاضر اتصال وای‌فای درحال بازگشت به شرایط قبل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/Futball180TV/90245" target="_blank">📅 19:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90244">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تا ۲۴ ساعت آینده سطح دسترسی به اینترنت به حالت قبلی برخواهد گشت. درحال حاضر اتصال وای‌فای درحال بازگشت به شرایط قبل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/90244" target="_blank">📅 19:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90243">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbyxTqmG7rkw-aB0CI_Y33FF93gYMV_URbGdBsGVs1i-Ewz-MdhzrmeZpObPjJkFJHbqvqLBxkT-sa0SwMKJESgc4T-xGShGEWYy8BnFFD1w1VNztuOTts3jZRfXpyoWV22VM6N6QGIQ6RxOCHJErjjElXTVNAk4nDHU_KTGqz7Ohn-cUtXAwao-1Otsh1CWQtVEhsXXoUXACQS5ztgdEG7LRrnRwslw4hUIGYHJnX51H0Rlaf3JdumeanCLUC47GvDmLhfOA9ctZXldE8BPt8TO6mpW2dOcpM9fgBjPB49d9q98ccxZjsUS08hTsHhNQ0KXvi5KcisgD2Tsr80CvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ‌فصل 2026/27 سری‌آ ایتالیا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/Futball180TV/90243" target="_blank">📅 18:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90242">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtPVb823pNJV9rPvV3rp1LEXk36Md0QnFpz0cY367RLb5giKv5u7MxnJKLTmK1wxwaydW1LgQxGU6gDDRNj2kQUWNkUNAtmCIBtJ0o7xhBvkfBOlhR_rpTwcF9IHuEt7NflIbRap9OqbyFHWgs_6EM9LY_4rt7XpKLVJxcE6ZCnE7MPJBGp5GRpJfaApEhuSFtZiJjJXBV9VawInL81n1Z6urvYC_DXZvJSkWndVMDVxMrRAaRWMfI4wpK5jLoOKpBZU8rYkWc3TYm4AU1lQjDoeJ0S8gHaNfMJ3LVsTYa6OWOSHiGxDCUnMHhqe0xxLPRo8YoJe5XXiZ8qhRw88Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل 2026/27 لیگ‌برتر جزیره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/90242" target="_blank">📅 17:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90241">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxT6aj6UXE_F93jeoilM8jP4El7OUgoLdsbFG20Mi6mV8KYmTDvvsnbA04pXSdpDa7WfW8AKaJ3c1pDtRG8c1Bf6OejUKDBHSqDPP80y4Kq_B9Ij76HkyoUc0qP_DBF2QPjnxG5VgwPw76stp-1LN8t8oE1Gxrg4hvrRZXVoFJHebfp3G5Tabd6eW0MTJZhpxGgW814gqgU351cMO38GXrFP_wu9fxIPAMF01Wtjht8IUFBSwmQEioXYaD-8ugTt0cKt0A9lCArF99O9MArjVgJTBzs_oO-nIWqKRkzTGlCCccmX1b3Q3ju3MD6wcTd8QInWBF8e8Ps0X1tcuudXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه بارسلونا برای جذب آلوارز پیشنهاد پرداخت ۱۰۰ میلیون یورو + مارک کاسادو را به اتلتیکومادرید ارائه کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/Futball180TV/90241" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90240">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdLJdzcvDyb8E0n8Pr7FH1jNHQ1B6BHJwX98nK6ZVAuf7EyvtzbBIaGW-5J0QYK9xqpaqdih2Qz3VoftFEW-QdnA0sdLqD6AsomntC6Azr35TuodTAdwEiJ0e5QSApDKqTNA35jFG9vucaSoud3Hpvfb-pn7BRQ_rHobPn-XDSX03SkyLj0N2PXMj5HASomUEwQ0RJvFvb5cK8WXHxM_arJZXzykXc7vKFSv_Q-QBHql8beO3eJ5qVN5npcdrwT5ltIsyMT3VzRAzunFWM_OdHj4dwgz-OabWs_deIYZdj5yhm6_QcYpTs9-DBnCeaWoP61Xu6iJ0EhVPphAQgztnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ ورزشگاهی که میزبان بازی‌های جام‌جهانی هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/90240" target="_blank">📅 17:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90239">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0e6MZtwTp3OsNdu2ob7pqlesHH8g6uCYZJidgSawb88rOB_buoUAh8RqDcviaiJ6PpbYS_3cW3i5PsDs8XCZTx79xBZwCdyED7MGS-jL83HCcAHGoQfeSKCF6qHR6hVxwD5nMHV9DOhaivDoQdbybpFrjQP7BELDWxIVh7w7biRxJL4PzY07mruF5HDWgmbylSa9DfDVSgaZKyyEXAuMOELMeYkGw89HuJKSJt0sfrRolMGzAoqtEreAIreXgrogkf8xCBTPB1W0kUZfz-1t_Sq_cpnNsEY0weD24NfCw6KENbQp0Ko6ody4coKe6YCWGJat-FCyBqS-lQ_QJ0hDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمدرضا عارف معاون اول پزشکیان: اینترنت بین‌الملل در دسترس قرار گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/90239" target="_blank">📅 16:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90238">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مخصوص وای‌فای :
https://t.me/proxy?server=87.248.129.199&port=25565&secret=79e344818749bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/Futball180TV/90238" target="_blank">📅 16:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90237">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4MOMxwtYBQA74Uzo5G5h9iOA3dthJGRI3rk5XmoQE13PjYVNJFQqDO5keUek80MiqmZ4hyXf45DR2ntz9dXKC7rk4qG3c4qZyvk9jKDuD2iSQmddrapleJbGZyzUIft8NKQKT1D4GXCWVTccMHjVCft-KysvFeuBTIEKcsRSMD6-7LDGdyXzT5yAMgstgH54rgsPRp0goyJW7s49wNmuQA4mq41ikVSMtSf2F_qjraqXc21YsK2ouMc_0cVX4u5Uc36uwkhY6UNrHknn56C4CfKC-D4vndZdW7fu-1vHnfSuysTUs0G5TOGJKF8rzOQnqwUIfm67no5T80DyEdWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/Futball180TV/90237" target="_blank">📅 16:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90236">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGL69um6NUdbpOTiZCih067x5jPAMApR-ZbO_K5KuaXhDNGk9A4AAdW0fc5YTXU_PXvfWAGuSLmywTt4uhL6MBYObqw_M5OTOzEcyLkIW01sKxgY-fGeJY55oNvzztProIW9x_FnkIIBvczYZPSPByoyCp34O_wXxdS2-PBc5PoMYFZgiIlAa9JkcGXjtbzM3nKxPyiVWfXn_CirnTQASR8dkNyf8hnzADKv0ysVtrt-oKZmHdxPLS4aSAQyeejoVssNL4kogpEEEV934cW0KYGspkcRfZEhe72zGVSpIwoEgNSMJH6sSUeRfsoNXST5qdL7w47KqYRbLmjpxolgHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور خوسلو در مراسم خداحافظی کارواخال؛ این دو نفر باجناق هستن و با خواهران دوقلو ازدواج کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/Futball180TV/90236" target="_blank">📅 14:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90235">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/Futball180TV/90235" target="_blank">📅 14:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90234">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
وزیر علوم اعلام کرد که تکلیف امتحانات پایان ترم دانشجویان کارشناسی طی چند روز آینده مشخص و اعلام خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/90234" target="_blank">📅 13:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90233">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
#فوری؛ سیتنا:
🔸
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا 24 ساعت آینده
🔸
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/Futball180TV/90233" target="_blank">📅 13:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90232">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/Futball180TV/90232" target="_blank">📅 13:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90231">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/Futball180TV/90231" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90230">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/90230" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90229">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/Futball180TV/90229" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90228">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d9611d964.mp4?token=gQpBSQXfMsIENneXhMS8hS-GpK25LHobqbqHATWPON19hh_WWMKwtzrNfmfr9D0b1XgKjko1YcqZJzepSuGijAZy7aMoJ004HDVLIi-8CSckYpGoZvWGsjSibUCVf7oa8YxfByMGFI4VIL0P0v-T48e-RmQ7dbjijCawjzZNaf0FMVYXxMwZiWBA2605d3bNqzLagewhz6QHaw0K1chdhMl5vVdT6ST_nbz1p6g9Tvx3bPyE3YGoqRLij0nY-_AV2igZmCsDi8679S-bOPBHYyTLQhLeBb_1UVddpz43O9-naFwTnNfFTEQPxIWp_ydDv8rpshrfSFTIky2fMH-1yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d9611d964.mp4?token=gQpBSQXfMsIENneXhMS8hS-GpK25LHobqbqHATWPON19hh_WWMKwtzrNfmfr9D0b1XgKjko1YcqZJzepSuGijAZy7aMoJ004HDVLIi-8CSckYpGoZvWGsjSibUCVf7oa8YxfByMGFI4VIL0P0v-T48e-RmQ7dbjijCawjzZNaf0FMVYXxMwZiWBA2605d3bNqzLagewhz6QHaw0K1chdhMl5vVdT6ST_nbz1p6g9Tvx3bPyE3YGoqRLij0nY-_AV2igZmCsDi8679S-bOPBHYyTLQhLeBb_1UVddpz43O9-naFwTnNfFTEQPxIWp_ydDv8rpshrfSFTIky2fMH-1yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریکشن گاوی و لامین‌یامال پس از حضور در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/Futball180TV/90228" target="_blank">📅 11:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90227">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
آیت‌الله مجتبی خامنه‌ای: رژیم صهیونیستی مطابق گفته پدرم، ۲۵ سال آینده را نخواهد دید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/90227" target="_blank">📅 11:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90226">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/90226" target="_blank">📅 11:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90225">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UncP7O5Oi1Z0MEbXTPUOtEOyV58pgfotvQPcrjv-6f8tfm1RBoRRl_ufPGKtKWQp8EMdCKOaYb0XYI8hlhfsB4e9NyBOVvLoatxMnDnvRb_bkDygFUMnZU66dI9M_4k0g-ZPLV6HB9Lb7Wc1_kxHhIkrh_oAXLmmpSY3hr9AvBJutUmAA1aSmS1RdM6A504mtnDIsTsY-vLYmEdn1Kq9sDWjjwKkudBeH34hDH-dwzTSKlnujRbDgl8pFw2rUiIPQqDCuw7WzXkkUu8VG_1fuAb3hh-2uNLmNOnq-tjibkKsp9YuS6b7ShKfjvdGiyz5DCjZfLmoa7IB9HlOEnzMjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C قرار داشتند. برزیل مهمترین تیم گروه C در جام‌جهانی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/90225" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90224">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dt4bEe5TI7h2DkyizJaPUaiLjfT0MWx26QkotumHjZt4Ihb5f4FYw2hwVFbnWmNhZxk9Y5jZ_GhBVCTUrvqRMEURkBAzSIb_drlbUWXW_lzbk8FGi11zsRCYagGtPwH5HmyVevVLOPgdafeHDFy3vNvL-DVZLL3-SjCladgfUrlA4w1J3A20GpK60FrggF0-5DH3gmF7VESnERx2_UThk_coYreHGxv2ztzuC4M6Ny419OnIOrldsJVTQwbOHX0PVC-PgnRkCH20Gku6mkAl7RFQ-EszUb4O5F1FtBy7OM-dCUSr9dNRZ0eAliQL6LeHeUuM1LFU860Sfdmh57bE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با آغاز اتصال احتمالی اینترنت بین‌الملل؛
ساعاتی است جیمیل در دسترس کاربران ایران قرار گرفت.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/Futball180TV/90224" target="_blank">📅 10:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90223">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/Futball180TV/90223" target="_blank">📅 10:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90222">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/Futball180TV/90222" target="_blank">📅 08:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90221">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/90221" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90220">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLso4Xx4CkoP9oJq5kDhh14N0dI4dYOBqQoQtEvcfc48IllKv3zYtct4SH7Za7rIR9Zxbcl_wZMWCjODbdCNSOteeOhXa-330NNPc1kUALcmYaw6iooQCNf8GFxEChCA6DVRqAsTFB1LYGiQV4DUfJI28WJhsgtlKaCugJhL7X-gMdGtSXxDzu9-KXHHpdSYDisDlno5nkptk4OMEeDabkTWIHzZSnEVrnp9tdXq3tPebsgsmy1pC2kkqZVY8SO7CeWNGOtWBQLbhRx7xqveG8_5LzDtjnIOvdacrCymCF7AzJddnc8f0bvYzayj7pJz88diOEJCu0fHORjHJEX25Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/Futball180TV/90220" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90219">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuABEr23abHGi_iuO5ht7uTo4e0SvabaT_YdnAFzClsPlApnX_5GEbMMpJGwfupH8fDQKVW1ckg9T54uYPCF2QBMFlzT7FWiaaAuCJqQ0mnDQGQQMoEW7E2rhY3HBfrxl6gh5yfCNQ-T_-rsnFaSEIVxS2Wy0mYRiRIZ74t-KZJ0EPdmJa-JxeU1aKvVFhql1-UDq9wPIzncQnG71H7RpO0LrhDzJ6gWrQnqow9yPppvoR4rYUWMwHxIkhGcesxfJwjrtpEkwqTsJ2q3BBl3uPpcXlCGjWhLZgWBi_qXPI2sbMWjkpzLuP-qySpE5ijP-OfVkNCm7qeAte8SR17L8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇴
لیست تیم ملی کلمبیا برای
#جام_جهانی2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/Futball180TV/90219" target="_blank">📅 23:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90218">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdh5mDyGkFs6R8YjbsiAJ9B-bjLcgvjMvWH_XRZuDMBOIIO3xs8Dtdy3z_ck3C5juK0qLNP2Hl0CraLz5kqvKodrkvmY_zzRc1MEh1ib2A5ZXeSSAF_ZuGcg-4XElHM3EChVsxARCrs7114wwMu6u2NjBjngd50HC3apHA3v3ywIW3FeH7Md8xjBvx5lf3pppeqRrlfHcneSjfEyIRFWL3jdOsAY5KXuk3IOKYVeIixd1-7a7yXi93i1D558hTJi4ZaO4Hcq9q-h9rzrpxKCqguL9tKX3U42mh0acKSPoTiUEEDp2E4wwRP7Z3TGgdXpLUMxbhi08le47ZqqX0n_jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکس آلگری از هدایت میلان برکنار شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/Futball180TV/90218" target="_blank">📅 23:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90217">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/90217" target="_blank">📅 21:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90216">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/Futball180TV/90216" target="_blank">📅 21:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90215">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/Futball180TV/90215" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90214">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/Futball180TV/90214" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90213">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/Futball180TV/90213" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90212">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🔷
جواد نکونام سرمربی سابق استقلال از طریق ارتباطات خود با افشین عبداللهیان مجری سابق شبکه ورزش که نفوذ گسترده‌ای در هلدینگ‌خلیج‌فارس دارد، خود را برای سرمربیگری فصل‌آینده استقلال معرفی کرده هرچند که در این میان تاجرنیا قصد دارد با سهراب بختیاری‌زاده در فصل‌آینده ادامه دهد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/90212" target="_blank">📅 16:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90211">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPhiENCmPmoaatWU75ox5ivF5UbnZdBUGiH_H73pCt7V7JOduAZ538VIRb-abHUecnGzBlv7KgBFdhMgO2OP-oJm9h7jWgd6WwybD_GiKQ1g7zk5sCmEkavSrtZ3SpIQqiwt6u1wqDV0-TOcwwfvXIzYJS7i1IXc06POTX7iinkyRkMiXC8jppsryYf1zlRAVBG7aI5u8VZf1eVjJhvoLDTPxqJeNcN6_NZ57aGQ8gss62WZ75yhzV1scbnM76NBh5PHKBTq1Yk533kH69vjz6htIh8ZtdEq51dWPK8lQ3qnOreOuZUBOwxPQNzEJP_HGqufs-sFECf5mmgVw6n90Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست تیم‌ ملی اسپانیا برای جام جهانی 2026؛ بدون حضور حتی یک بازیکن از رئال مادرید!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/90211" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90210">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/Futball180TV/90210" target="_blank">📅 13:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90209">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
ستاد راهبردی فضای مجازی صبح امروز موضوع اتصال اینترنت بین‌الملل را مشابه دی‌ماه سال ۱۴۰۴ مصوب و به رئیس جمهور ابلاغ کرد تا در صورت تایید نهایی،‌ وزارت ارتباطات موضوع اتصال اینترنت را اجرایی کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/Futball180TV/90209" target="_blank">📅 12:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90208">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa22a668b.mp4?token=LJcshljLliOrkYKFOCYxgdAQWduM7yaTNsoYpXv_zz_ldhUXu0dtT5VeR4EfFSdXuCBUk6M67V6nQbO_HS_6B1LLn8xDRW_loHRguzV4Urtwn9RcCOcQO58mt4eeVWdho9japBFRoX21bLt4RtkiAFfD5wwkuVETklODdlzXEKgbT_E2mnSJQ9ZWvjLDy582kcS9sSbdkr92_16ut0NCFJ_uXoeD4-KKsLIo_lpBUy3Ry8__m_BUgTGkNfrbbBCk75A3GR6nzCILJU7DNCxO7ce8PFGdrmZmhoWWYb1FBD8sDDbJjL3SThcI-j6rUV-tATBEw6Ui_MLB92ibV0UgCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa22a668b.mp4?token=LJcshljLliOrkYKFOCYxgdAQWduM7yaTNsoYpXv_zz_ldhUXu0dtT5VeR4EfFSdXuCBUk6M67V6nQbO_HS_6B1LLn8xDRW_loHRguzV4Urtwn9RcCOcQO58mt4eeVWdho9japBFRoX21bLt4RtkiAFfD5wwkuVETklODdlzXEKgbT_E2mnSJQ9ZWvjLDy582kcS9sSbdkr92_16ut0NCFJ_uXoeD4-KKsLIo_lpBUy3Ry8__m_BUgTGkNfrbbBCk75A3GR6nzCILJU7DNCxO7ce8PFGdrmZmhoWWYb1FBD8sDDbJjL3SThcI-j6rUV-tATBEw6Ui_MLB92ibV0UgCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین ریکشن‌های پپ‌گواردیولا در منچسترسیتی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/Futball180TV/90208" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90207">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/90207" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90206">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVu3yjZDzPxpG3dYi0-Gx5K3DlWt8SK3n0YI1iDaWXFFZ6SdsjKgXo-TGmLkAgkTszPliTumqI2RZ41VgG9yd0S14ZdAM1VZ_v1fI1aUECnbPRgk1us3ab1jlH76qVsSXj89v94OfQJDj6JsUfSrbiWidI6wFaBIB5PBGDII7_wvD9Wi5IFsBtPMv0AtNn0xA_2k-3TclyeX4VY7u_vndxxE2i---uZ-Bs9QOaeLg4C-PmGarE4Evb7MF6QCIY_XT6B1kPoTzj0XSUKAwB4-neEKUWUK_UdDjioBaOAqGgOot_cgJUC2qxlkrB1WdXSDzWbtIFmn-9C9QUxAfH7NlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/Futball180TV/90206" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90205">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940870b589.mp4?token=rM6xOH0kCLSmblL59XNOK8EShPr0MZr7QxYqMq43UAZVabdJWmLRxM3A0Ahj6wgEdosf5yBdBuYrFP4CXFOBlLj-1vUONjx8CzdBWCHf-vhnRcLYfD1_w_ON1qQ_CP-PI2-ZlEj3w628hhk64iwhkM7tpoXQkkLj9bWuhIZo-rQ8VNWV3pK1HxqQ4nMN3McPyA0aj9mHiydKVDN2mN3jY3YwHvBUWJaZ-_INMQ0lrCTtxdgGKATDg-_FfFeJcwHqMyS-hCJvfssBX2iPsjpcfn_oQCFvxcTKaQBgX_5Kfgp1qUUkDIcpLCFMV5yWgRXb3ERH2pf3G-6hlz_lohDY_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940870b589.mp4?token=rM6xOH0kCLSmblL59XNOK8EShPr0MZr7QxYqMq43UAZVabdJWmLRxM3A0Ahj6wgEdosf5yBdBuYrFP4CXFOBlLj-1vUONjx8CzdBWCHf-vhnRcLYfD1_w_ON1qQ_CP-PI2-ZlEj3w628hhk64iwhkM7tpoXQkkLj9bWuhIZo-rQ8VNWV3pK1HxqQ4nMN3McPyA0aj9mHiydKVDN2mN3jY3YwHvBUWJaZ-_INMQ0lrCTtxdgGKATDg-_FfFeJcwHqMyS-hCJvfssBX2iPsjpcfn_oQCFvxcTKaQBgX_5Kfgp1qUUkDIcpLCFMV5yWgRXb3ERH2pf3G-6hlz_lohDY_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و دیگه محمد صلاح تنها قدم خواهد زد.
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/90205" target="_blank">📅 11:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90204">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392ebb3ce3.mp4?token=cqJDBv7R9WluO0g-yb5EemYX4GdRBMVg_qyckLg24-o0s5QNomhnwbHJhjSCoVj49fX9iwwnLLMjUTN0VYhj1O9lKIrxO8ZcgdkAldnvAgj1VXLgY--x8nMGmtESp_np2g8L2A4CeMVQKh5OtsJCokYvzGGO4hHjQD3b4LT0x14ck094j_PJSvdQzQJv0XD2Fy-PS26TXR_Bn1PcBroQ7cRfVdHYu8hmnjg3oeygSpRP3cAQqn7fU57TQmQfE80Hg9Q3gpah8elrKt7S8hTSmLgDaYdJ3M7txsW0NcXXiAbbYgLxXLj07Vm-rYoleUHOVSZHW3zP4LZZElVptVLzeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392ebb3ce3.mp4?token=cqJDBv7R9WluO0g-yb5EemYX4GdRBMVg_qyckLg24-o0s5QNomhnwbHJhjSCoVj49fX9iwwnLLMjUTN0VYhj1O9lKIrxO8ZcgdkAldnvAgj1VXLgY--x8nMGmtESp_np2g8L2A4CeMVQKh5OtsJCokYvzGGO4hHjQD3b4LT0x14ck094j_PJSvdQzQJv0XD2Fy-PS26TXR_Bn1PcBroQ7cRfVdHYu8hmnjg3oeygSpRP3cAQqn7fU57TQmQfE80Hg9Q3gpah8elrKt7S8hTSmLgDaYdJ3M7txsW0NcXXiAbbYgLxXLj07Vm-rYoleUHOVSZHW3zP4LZZElVptVLzeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدومیت لیونل‌مسی در فاصله ۱۷ روز تا جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/Futball180TV/90204" target="_blank">📅 09:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90203">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76980eb486.mp4?token=WVtS6_Inr3hG8jli4GEGeqlf7rF51yr3WSRYar7i_gWLLGGYMr4O3G2LY91flWJe9B04J7y2YzYVl2f1TpKgJlZHYcuc31UVbbsTEd5pig5QHttTaX-Tb8ovo7XPMO4LhGxqC_meOYx9x4mVfB0akkuCfd0PLHjDZjt4ZwYtBqGHZCk2iLlAFkR4tRLeQzZ3q8jtVoja_C2avYHCcxcFSGZbu1x3DqNq5ZS0NB6Tcdm0w5VJvshZ4qy1g48als4n3ZZnC6Y0BC8M-iJ5YVHS7Z-w3YiE4HbnFcvxS30lncP03uwtTj-OJKAPqc90Nizm2PvfbyFKYG-TfC6ZaEKWOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76980eb486.mp4?token=WVtS6_Inr3hG8jli4GEGeqlf7rF51yr3WSRYar7i_gWLLGGYMr4O3G2LY91flWJe9B04J7y2YzYVl2f1TpKgJlZHYcuc31UVbbsTEd5pig5QHttTaX-Tb8ovo7XPMO4LhGxqC_meOYx9x4mVfB0akkuCfd0PLHjDZjt4ZwYtBqGHZCk2iLlAFkR4tRLeQzZ3q8jtVoja_C2avYHCcxcFSGZbu1x3DqNq5ZS0NB6Tcdm0w5VJvshZ4qy1g48als4n3ZZnC6Y0BC8M-iJ5YVHS7Z-w3YiE4HbnFcvxS30lncP03uwtTj-OJKAPqc90Nizm2PvfbyFKYG-TfC6ZaEKWOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید قلیچ در گفتگو با بهاره افشاری: امیر قلعه‌نویی واقعا غیرت و معرفت دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/Futball180TV/90203" target="_blank">📅 09:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90200">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HICxMW56v_PBWPSAPmrmLJRKqXRQaQPX1tSYCqdaiwqrCzY2L-17GaQw6Rik75NyawmvlEpXDf8c5lb2jv1jFAYV4UbcOgnNAb_jKVySyhuBUz99uezSmGkxs1juj3VXKY4bzEGNReRsoJS6BWhIBmvGO8W4CSFmBh16BlT0BnyFv751Pkt4imLh7cWEojCcjamsVHI0hRj26CXMaL49bOem1E0_cB0Eu7XKhQ_lQf6XLfinn7lSy5Qe_Zs-vLHWpmQCdszxJLsnLSjGoLZZc00YMwiyTnXcKbu5ccwiBfJX6GhtVzaYOfafQz0i18If8hMCDTgtg1VMoZJKIxLrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخشش کومان ستاره النصر در دوران باشگاهی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/Futball180TV/90200" target="_blank">📅 00:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90199">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/Futball180TV/90199" target="_blank">📅 21:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90197">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028fa17067.mp4?token=GRSEVLXvSfH6b5VB7DuZSjO6vuEPviGD0jFnFRbehhzFk5y8st8AsAhRFD3hckCjOMvaYZAXdTM0oXh9ijF_dOmvw1NrcENJswoLwgaPttYcvwO_AM0tMJ3Fqqb96PjSouldbRzM2KPHQyplgsSRShsWGAjw6M4YaHwL2g84DdAovrFsCqRkgs3dQNWHKt0XGw1qxYnwLCLQ-gsTRYk01k4U9JvW5Dshkjq7b1yssSo_-UueyOsFdFgJ4EDJTTWDfkzUsJy8QkoUih_e6DUsR7msf2zAPqwKNJ1ZJALUe3LC-SSUsnC_4N1pZFovcn5UHgzrOHgBYqv1vXkpCo8HIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028fa17067.mp4?token=GRSEVLXvSfH6b5VB7DuZSjO6vuEPviGD0jFnFRbehhzFk5y8st8AsAhRFD3hckCjOMvaYZAXdTM0oXh9ijF_dOmvw1NrcENJswoLwgaPttYcvwO_AM0tMJ3Fqqb96PjSouldbRzM2KPHQyplgsSRShsWGAjw6M4YaHwL2g84DdAovrFsCqRkgs3dQNWHKt0XGw1qxYnwLCLQ-gsTRYk01k4U9JvW5Dshkjq7b1yssSo_-UueyOsFdFgJ4EDJTTWDfkzUsJy8QkoUih_e6DUsR7msf2zAPqwKNJ1ZJALUe3LC-SSUsnC_4N1pZFovcn5UHgzrOHgBYqv1vXkpCo8HIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و دیشب آخرین بازیِ دنی کارواخال با پیراهن رئال مادرید بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/Futball180TV/90197" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90194">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=uFafZG4HHckX1NbsK_Dlx5FO5ZsKuOKUef-hkJ7zhwr7JB7pJLxTD7WiEALoLwrzUzWs4ACShLepsae1Zmq1dh_P-S05kLLd4-x48ItLuOIB9-EIkdD4tZiZTlbwDtKN5WefmN-1Hd0VBGud2JkaH_Fr2oV6iERlA-dBFw1cW3ts4MxIJsU8Vi7U-5AVWes7Bhj41nnzhUf59UHsC0sbQ8DlYX-bL4dUY-kxLdMs5fOOeNkzIjd4NvNyAgcEQxiTJWKUzL9L9lo_9oOzxWONKOH0a2axii8xb1OZmy1mf2yJ7i6bbqOG3hZP-DITHZnF80ym5nvYLsCY8uM3RMavbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=uFafZG4HHckX1NbsK_Dlx5FO5ZsKuOKUef-hkJ7zhwr7JB7pJLxTD7WiEALoLwrzUzWs4ACShLepsae1Zmq1dh_P-S05kLLd4-x48ItLuOIB9-EIkdD4tZiZTlbwDtKN5WefmN-1Hd0VBGud2JkaH_Fr2oV6iERlA-dBFw1cW3ts4MxIJsU8Vi7U-5AVWes7Bhj41nnzhUf59UHsC0sbQ8DlYX-bL4dUY-kxLdMs5fOOeNkzIjd4NvNyAgcEQxiTJWKUzL9L9lo_9oOzxWONKOH0a2axii8xb1OZmy1mf2yJ7i6bbqOG3hZP-DITHZnF80ym5nvYLsCY8uM3RMavbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهناز شفیعی :«می‌گفتم ناصرخان یک کم کلاس بگذار و با زنگ اول تلفن را جواب نده اما ناصر قبول نمی‌کرد!»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/90194" target="_blank">📅 19:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90193">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/Futball180TV/90193" target="_blank">📅 17:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90192">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgVSkzSJe68eK6tmwDvjLC0RCEcevKhIIIbMkR7bsbaGBw_waK7oo24AqBmMr-hqkMrxN526Ox1fcxIPVxBEJZ1PX_tvvwRrqbqe6jBif4HWl8CLb1I_KyQcQpRV6YrARBPp2CHd_Q52Itih0_m-m0tPQi9twv52Xhz8SxGuxXwVorXA6JEZ0wbuP7phZ3K4xOwYprwL9Ful-ihDKfDTOml_mNJiFRRssZRUsFJLvQg58DzQWV58p4GBbVwriw5U85XbHQFZ-SrN2rH6faIyd33A3FPPQRCwKaA2LoxDgJyj-pFuqYLOxjbYMKK4UNKxBQvlfDZ6EP_t14F5Ps4RIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاب مشترک داکنز نازون مهاجم استقلال و روماریو اسطوره فوتبال برزیل در پاریس؛ هائیتی و برزیل در یک گروه جام جهانی 2026 حضور دارند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/Futball180TV/90192" target="_blank">📅 17:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90191">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgU9A0UtZDNVgE8vBuc6El0Rnb-IYZrok_SkB2Ht4YbNgsnodGixj0hVOz15BGJ-faPMGF8zPyVyqYb-ITsNcBCcWcuBrsRAC9QhoFs-NknuUmN1ysY67zsnrFK85DpZlK1uwzu3swcsuSe7IttYJq-Fc-dnpBdVQfwNwaYMtq2CdGB666YCVlGFAH3YbSHyigejsTORcje33hSTRNeaHtPC5WiM0GAB-ZLEy1NCb1UULZyVK46R7mDrwppO4z-VW-uohWVeJ3UWGd0K5sisRnezH4BcCFQAeLZLxPoBl6a34-f1u6W4GKMCofjf1JT8Pzm8qomDzshD2UmPzkRlIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ: خدانگهدار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/Futball180TV/90191" target="_blank">📅 16:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90190">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67618efab5.mp4?token=Sw_yVBAi3ArqpiTn10wMWT3H_QHcOTFronCq62kO6yBD3rkJY4b4Zxa8P2hRtz49SRUqdv-7QegsXXm0EI2aXvvl_cSfxVI_MQ3o-4xfAdL58Ciboa6g_d-kQ-9Pm1CfqgUZIlZP_3AwhdtnyofI0AhXu8DcRKR_2fL4tqByc_vWyVwjFJA8LoujUXPUUal4OmoqiKn6VHz85UFp-AtadFcUvSuBEKO_KohogLcEA0wweHS0OEcDfH7BF_XBBDQTMYn2vSkmKakA1PAkUkrjFpFUodieTzj1d54Ojgo5oyLMnOX2A2KVbSDtOEq28O2sKMAy_j1I-egfHLG5r0v_1DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67618efab5.mp4?token=Sw_yVBAi3ArqpiTn10wMWT3H_QHcOTFronCq62kO6yBD3rkJY4b4Zxa8P2hRtz49SRUqdv-7QegsXXm0EI2aXvvl_cSfxVI_MQ3o-4xfAdL58Ciboa6g_d-kQ-9Pm1CfqgUZIlZP_3AwhdtnyofI0AhXu8DcRKR_2fL4tqByc_vWyVwjFJA8LoujUXPUUal4OmoqiKn6VHz85UFp-AtadFcUvSuBEKO_KohogLcEA0wweHS0OEcDfH7BF_XBBDQTMYn2vSkmKakA1PAkUkrjFpFUodieTzj1d54Ojgo5oyLMnOX2A2KVbSDtOEq28O2sKMAy_j1I-egfHLG5r0v_1DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همسر حجازی: دامادم گل زد، تیم ناصر سقوط کرد، دخترم گفت طلاق می گیرم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/Futball180TV/90190" target="_blank">📅 13:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90187">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fbdde7379.mp4?token=kBfGDKr1OCwLWoJOKZqsI6hVlttexDrSHdPHKCy0q35LkSko59zE60wNUlr6n-c7t7jh_-gmLdWibgFcKai25lJNEg8iDMPZSc5o-_syWZ_7zuOVdYlpPnnHok7UFovVLnwimUw65A-28wxGXo1a8Wxe5_FYiZdtT6sQ7FDTvVAqmHavc3udJUxeBLHyuzmD2Z6Bd5qE-OmkNxFQay_XEM1ZdRKpMvHYmFjTy66vMaDpXPXNfJd34ZXbL4ij5PSaGkwD11d1Wavg_mGSlnMUsefeCkcC1FrefCwMLC8nWQwFqPZ2gRG2OKWbDfSfb1Zrs9S0ha5DnFDjf-2Bb7NBunW4i2TQHX4W5McpJTXElVGr4fMwI9lF9ZWcydy68K-VfCl0S4KukHRlXTRpxjTbsF9tYU9e1rE5m5g69zgyCWa_NT9PhYTmTZqD_t9zR-7j_TliQ_repcCq3GeN75K6kjv6GUJkQ3MeKYyWc635TjYToUhrz32QDmZWcL57Sm3jBEe7MO3xogu7Q6uwmclBZXuC6dnvNeoIEqGm9vzwB4iPv0g6JevAtMPd-TKg7lJPKKZLsGOGce5mks8BeXx4IAHKnc3QpbjczId7A6NiEwTukM_Ul-wLCpbEvFUTbjyE0chCD_WHy1tTWiZ3GAOCc1v3ckSqASoc8nF764R4Hxo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fbdde7379.mp4?token=kBfGDKr1OCwLWoJOKZqsI6hVlttexDrSHdPHKCy0q35LkSko59zE60wNUlr6n-c7t7jh_-gmLdWibgFcKai25lJNEg8iDMPZSc5o-_syWZ_7zuOVdYlpPnnHok7UFovVLnwimUw65A-28wxGXo1a8Wxe5_FYiZdtT6sQ7FDTvVAqmHavc3udJUxeBLHyuzmD2Z6Bd5qE-OmkNxFQay_XEM1ZdRKpMvHYmFjTy66vMaDpXPXNfJd34ZXbL4ij5PSaGkwD11d1Wavg_mGSlnMUsefeCkcC1FrefCwMLC8nWQwFqPZ2gRG2OKWbDfSfb1Zrs9S0ha5DnFDjf-2Bb7NBunW4i2TQHX4W5McpJTXElVGr4fMwI9lF9ZWcydy68K-VfCl0S4KukHRlXTRpxjTbsF9tYU9e1rE5m5g69zgyCWa_NT9PhYTmTZqD_t9zR-7j_TliQ_repcCq3GeN75K6kjv6GUJkQ3MeKYyWc635TjYToUhrz32QDmZWcL57Sm3jBEe7MO3xogu7Q6uwmclBZXuC6dnvNeoIEqGm9vzwB4iPv0g6JevAtMPd-TKg7lJPKKZLsGOGce5mks8BeXx4IAHKnc3QpbjczId7A6NiEwTukM_Ul-wLCpbEvFUTbjyE0chCD_WHy1tTWiZ3GAOCc1v3ckSqASoc8nF764R4Hxo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت همسر ناصر حجازی از روزی که شُهره به همسرش پیشنهاد شام مشترک داد
همسر حجازی: هم خودم را باور داشتم، هم به ناصر مطمئن بودم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/90187" target="_blank">📅 10:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90186">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
روزبه‌چشمی بدلیل مصدومیت از اردوی تیم‌ملی جدا شد و به دبی رفت تا مراحل درمانی خود را طی کند. احتمال خط خوردن این بازیکن از لیست تیم‌ملی برای جام‌جهانی وجود دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/Futball180TV/90186" target="_blank">📅 10:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90185">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xk_A3A-8xc9WbeZX0qztytWaBoGB9LdVS3fPKxCUzpMvIYHrQnzaoRtbAn-dLuFmTSCB9oVWv8Q9apHAmG8Gp8HS1gql41hpZEniis0eTqJ7nEr7U3nTk_2C_KnAAX8fV-XIVvz4CBTZ0IOrFVaTZfZI_h32GQOeJfzH1hUt3Z0TC3YYE9rprfrSCHVRmgfKElBsXzeYc1drVzqR_gpxBr6fwBZtb9vDgFV58H_4U31QZiNjAVe2anLTAG9V6lkjHuZtAXRxn9YbOJFgAzP3NKAEh30gvJ8cCRd39yCrCNLHi4TuWG7CsR8n55vDqPkGwklvSC8Sa1pbTuIzyOjl7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بورس ایران پس از شایعات توافق:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/Futball180TV/90185" target="_blank">📅 09:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90184">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f849fc0fcc.mp4?token=XB5SHG4A_qz5ByXhIpba1FZ0IMmO1engMDk0DNsoC5L_8gJ4XCc0pvqjcBF-nKAG2NH3sTnTxRyjcnx0GrtlwYdj9j_12DgPRxmO3RjWfHoPjAIFJkmNBL4CjCaUXrS8wHkUwZo2uLcy6KBd60G6uZCljDFcNpaPbnHFoRFGLDHJHh8vICwl4c3ijpoPjRToah_2Ve_Nd0tu1UZh0W3wbjbIrRf-FGhfIWTRzYAJ802AOcNqekxwkOtkwh78VVxcNWzZ1npmKRc62Mjt-V1Onggxk5GxhaI8EGjxN-1ir76cQuspCShjATk3SsYpQM1ennO5nWT28dr4sxHjtyIwvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f849fc0fcc.mp4?token=XB5SHG4A_qz5ByXhIpba1FZ0IMmO1engMDk0DNsoC5L_8gJ4XCc0pvqjcBF-nKAG2NH3sTnTxRyjcnx0GrtlwYdj9j_12DgPRxmO3RjWfHoPjAIFJkmNBL4CjCaUXrS8wHkUwZo2uLcy6KBd60G6uZCljDFcNpaPbnHFoRFGLDHJHh8vICwl4c3ijpoPjRToah_2Ve_Nd0tu1UZh0W3wbjbIrRf-FGhfIWTRzYAJ802AOcNqekxwkOtkwh78VVxcNWzZ1npmKRc62Mjt-V1Onggxk5GxhaI8EGjxN-1ir76cQuspCShjATk3SsYpQM1ennO5nWT28dr4sxHjtyIwvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظی باشکوه کارواخال از رئال‌مادرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/Futball180TV/90184" target="_blank">📅 09:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90181">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-jKGJxCo7-UR00KzOkRzVVHzLdaOUpdZxRYaoQC0Jg8fOm0DbqmrlDdX0ihluNbtb8guyeKd-drPEzPJTPe1j60-cZUbra9roO8EQM-0pJi-nc5alOM-mFgcrocq1noZRZ1w5yo4ZvdGuCGU4bIO0ObNLrxYFynKdxTEhrB0TPSyc5bpMZODZo9byV9vyGwqaF3Pxy5IE4qraEdqUMMp2mMcDPUpSRg-ZIBYa0zAB-TDjOdcQnzAvKiDgYKHA0iVNoBaNl1VOrxJ4kxUImvykFZa_yC4QBJJMqvjX_CPw9ASIhy7LpYEZCh8rKsmt5X50x_nx3Ac4Sn6_75NJCUgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/Futball180TV/90181" target="_blank">📅 00:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90180">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZWOcD73Ml9ADZToWnLKDuNUEOhtNCbYkf0Obv9Iy1Zbo-V4HJJhWXXTXGDGYjIdNQ8DzeLNTGKk43VpYwA80KSjCOQcBxKXlqcVxIKTfZXMKvyo0FkgUqqKduG0-f4ppwjLsyWjwkW3BmCcxFAfJZt6JUBziZ7Eh6SZS_u7PifZfO1BSq-P0nhKxLfP30hchHBNXV65w6uFsWfwIYYO8CPdZjO8-0klEYDRT3PBv_8WFRXMb9ztyX5_9ACwu0o-yTLJdzSxM420S7qCIYBxBaWUY4xvDsY52vzkLJEvgbDd1IK53hLSKAVMtnNMcsh8iDqSjMcSmeAzIL9AeY_cEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تیم‌فوتبال زنان بارسلونا با برتری قاطع مقابل لیون قهرمان لیگ‌قهرمانان اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/Futball180TV/90180" target="_blank">📅 23:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90179">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss_tZoig6BRpff4LOi9vaQ11Oknw02V45Oxw9m_cZS7aHnVj2TEpZQDQgw_Jvu124kDzvFxK8athj33v4YbVaxJSKoFSs80TZSFkpsqPEh14v6_Q0lzp1m1mKorp4EbrbuDVc4Tw4ghNLLlpqchvdfQ6CWuPbHjpufS_E6vmcoIc0WTsPdT_-0R3cca8289Ql5doOods2ci0ll7ASG_NwEOXZvIvV0RDo0sotevTD5xL3uTvKoCNlocFh9GuWlmuwwanmT220asQo6HVj5X4IWFSJa41JBeAmUJoAGI8pnZtbulnv8tnI6Ymx_KB8th8hPcKhDw4-m9r3mdks61k5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون درگذشت پرویز قلیچ‌خانی را تسلیت گفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/Futball180TV/90179" target="_blank">📅 22:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90177">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b1b20643b.mp4?token=VKJH3OICIbW34zJKNc1qq2AdWTyLisdVWn26UaUM8Ln4rUadOhFkU9rAfJXF8Tp1W9C-K3QoVNMlw72BnjnsORvCzmz9ezPd3a35ehEO36m2eaJw8lRpewvU_JDCKrHfkfMIsPNx62B8LKecsRm1IC9XKbniYjryc-1hBrBJA2_0dxrRC6yDgwAD7ghuN5T4Ig1TVJDbYLPF7mgG1hItconOQ_kklnTc_N4Vmj9TEXb633D6BGAg9xYpK5hjv5OzNEWQoXA4lZcKDhhq6mb5uy74k8ROOQruQoip8GEXMtXP0ZvA8lHFRdWT_QFZPEnmgpBObvEmtXIGXJIQ4uvDLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b1b20643b.mp4?token=VKJH3OICIbW34zJKNc1qq2AdWTyLisdVWn26UaUM8Ln4rUadOhFkU9rAfJXF8Tp1W9C-K3QoVNMlw72BnjnsORvCzmz9ezPd3a35ehEO36m2eaJw8lRpewvU_JDCKrHfkfMIsPNx62B8LKecsRm1IC9XKbniYjryc-1hBrBJA2_0dxrRC6yDgwAD7ghuN5T4Ig1TVJDbYLPF7mgG1hItconOQ_kklnTc_N4Vmj9TEXb633D6BGAg9xYpK5hjv5OzNEWQoXA4lZcKDhhq6mb5uy74k8ROOQruQoip8GEXMtXP0ZvA8lHFRdWT_QFZPEnmgpBObvEmtXIGXJIQ4uvDLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
افشاگری همسر ناصر حجازی؛ علی دایی تمام هزینه‌های درمان را پرداخت کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/Futball180TV/90177" target="_blank">📅 20:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90176">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3Vu0sDCiYBZ9nSDdmEshj69hT9mfVGq5sC2Y-A__goEyOPUIpkg_hJLW37HYVc-1_CpELl-AeB5GLrbnP3HRdpv8-JCQenxnchkAXdwEZZ8_z69V_eZEBQ6leDcUn8MhUYN4LXBfPGOxsxanSXkT6ksMFp6zWB1gm4DzFTflBU0ez6AZLLLuAT06rzGnO2VL9WcJZKVSJYFf7I14DjNV_Fs_5kMHNMqYf5SqZt30eweuR3_UdcJJh-XD4nG_D4P3CbWgvoaVo2SGUbJh1tuShJ2TfQhyFRzpXEuoLBDa27t8YhZwnGr0xDl_PVq895XYalGYy41EgtMCOhgfrLVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مائوریتسیو ساری با جدایی از تیم فوتبال لاتزیو سرمربی آتالانتا در فصل‌آینده شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/90176" target="_blank">📅 20:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90175">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa5fa3b89.mp4?token=rWpCFNR_F0FlveqhyuN8CSr6wo0fGdIXSTxCqjo4bySZzIWij18GJsyDxJqrWg0005yMsOmvy8wB0aDnUDSLakUkNCkDF-8rFByErTUCHV40_M5wAvrNBhOVFea7CFnnFAoYTnrUGGt_LgdwwUUsT_SVkFaDC2lNpbyx0AI3YjwsQgxfUchlGJ33xv3ikS1L0gCBu0lqbAkjzEp2TJBlBVdqvCEfXR6Rh-eCHUBVClNkKIcfTuTw2kzUJl6vSOvfyyftj2T1iikpAWFXnLNC5P-M7JxC2Bd9jVPXXLZ-b_WSbTqO3Qj2DRpz7jZvDhIVBR7lsY8Rk-zYSI0sDh-L1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa5fa3b89.mp4?token=rWpCFNR_F0FlveqhyuN8CSr6wo0fGdIXSTxCqjo4bySZzIWij18GJsyDxJqrWg0005yMsOmvy8wB0aDnUDSLakUkNCkDF-8rFByErTUCHV40_M5wAvrNBhOVFea7CFnnFAoYTnrUGGt_LgdwwUUsT_SVkFaDC2lNpbyx0AI3YjwsQgxfUchlGJ33xv3ikS1L0gCBu0lqbAkjzEp2TJBlBVdqvCEfXR6Rh-eCHUBVClNkKIcfTuTw2kzUJl6vSOvfyyftj2T1iikpAWFXnLNC5P-M7JxC2Bd9jVPXXLZ-b_WSbTqO3Qj2DRpz7jZvDhIVBR7lsY8Rk-zYSI0sDh-L1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهناز شفیعی، همسر اسطوره فوتبال ایران ناصر حجازی، گفت حقوق بازنشستگی او ۲ میلیون تومان است.
او در ادامه با انتقاد از وضعیت مالی در فوتبال ایران گفت چرا باید کارلوس کی‌روش با پول این مردم به سطحی از درآمد برسد که بتواند برای خود در پرتغال جزیره‌ای بخرد، در حالی که ناصر حجازی در آن زمان حقوقی بسیار پایین دریافت می‌کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/Futball180TV/90175" target="_blank">📅 19:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90172">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba990f9ec.mp4?token=t0kYcvYUWyHuK0WoohQIxLHJpc4elHPvoRVexZzNpgNxgX0qO72dknPqlnnrY7secvaqGeYbsN2NfnU8YZ3lVOAq_InG_7kBYAtheVJn21jaR7-GHdGvh-3RooAnPtKQBLxgvLxIbxVvaixoKyAAteqC546n79bFltCxP3rnKnK_yRUQk9uxywnQVaE6TP331ACfD3A5MlFvo5P1jCPtVd15AYOX1cbkAWqiLsi28GqKEHqjo88EJ-pmtcU5Qa97TNF3viqWotx_IHUeessuPeXOVYQCOFLNqX53YSdBenMk_g03gxvu0aXC9wthWDOSw0vPE_o0bjqeCQ9a1GW-fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba990f9ec.mp4?token=t0kYcvYUWyHuK0WoohQIxLHJpc4elHPvoRVexZzNpgNxgX0qO72dknPqlnnrY7secvaqGeYbsN2NfnU8YZ3lVOAq_InG_7kBYAtheVJn21jaR7-GHdGvh-3RooAnPtKQBLxgvLxIbxVvaixoKyAAteqC546n79bFltCxP3rnKnK_yRUQk9uxywnQVaE6TP331ACfD3A5MlFvo5P1jCPtVd15AYOX1cbkAWqiLsi28GqKEHqjo88EJ-pmtcU5Qa97TNF3viqWotx_IHUeessuPeXOVYQCOFLNqX53YSdBenMk_g03gxvu0aXC9wthWDOSw0vPE_o0bjqeCQ9a1GW-fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
دوم خرداد، سالگرد زنده‌یاد ناصر حجازی، اسطوره باشگاه استقلال و فوتبال ایران است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/90172" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90171">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAcekuuqayNNYYTzEaVuWL2dA_mo-f1i-nMDL2LsuJJFnse4cOYuTdQxd_3EnkJQP2S4uGUeVgxm08xQC504wxEv0yHV5izGbLMYD7-yEoTi7ITb4jJednP91HqBG583iChJFzSaKn3VTD7iov6WN233p1vbH6Bz9GAMAl7T2iGpz9qSTOekwFFTqQyZcxlxQdVdbEbkpcMhK2Dm_CwG-qpjYUWGvR5j_vG9OAK5pKyiRBg-FxZCKKJ6pogugHXwIKVjKEw8ST17qZBTfQqubB7lBVQsTpkCrevp5y7Vb3IZUnzWXQm8jyGx8V6fjCmRBINa_438p1Pfgd-pXp3Lkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
تلخ و ناگوار؛ درگذشت چهره افسانه‌ای فوتبال ایران
پرویز قلیچ‌خانی، چهره تاریخی فوتبال ایران و یکی از بزرگ‌ترین تاریخ این رشته ورزشی ساعاتی قبل در حومه پاریس جان به جان آفرین تسلیم کرد. قلیچ‌خانی متولد ۱۳۲۴ و در 81 سالگی پس از ماه‌ها تحمل بیماری از دنیا رفت. او تنها بازیکن تاریخ فوتبال ایران است که سه بار به صورت متوالی قهرمان جام ملت‌های آسیا شده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/Futball180TV/90171" target="_blank">📅 18:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90170">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMbDo1QsyjhkcRnAhupA8O98AyS0tkPylSkwsPijgJg8B68cOSjHswcQ4bmY8MVgAXB5yLFKk3ukmSSqpuux3AmNHWkJjj2LxO-Jnsfld3XJcG1Xw3M9f5pWbnvdOmaKkmN_b7IC7mlP5Hx2OpKDHa8BlUCGsUnymcpaBjwOMPx4aO5QZL7QXduhnQtSYE2g7nfUlUSi2hVm2fIRYtnRzKhD_rSnQjUO8flgnlN6VBQDVhxVcg_AEXirPCQb0qd4pNEIVECBViZcogzu6B1VNCs0PT1zPxXuHJQwOFqOn3nh5Y5GAI0Gx5xHB-ODIe2nv4I8l5eOGWFVlZm4PYO3QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
عکس جدیدی که ترامپ منتشر کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/Futball180TV/90170" target="_blank">📅 17:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90169">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=UzvVxgzOm-QM5xDuHRunB30_OMaKtGkegdYcnM4H7rwzfaz5npNPuyMD2iw37SOXxR-CnSGJqMlYjZGcvQ19-9RBz4CPi6gPD99BgiA_iWahsuAkzAqIP71q2LLKQ4RYjNcQaBVKDRvJpbTOARwpAAWHLonDqNddHjffU83yCGNCmmaDxizsDMlJWNMn_7tQ7g08xWIF5OBA6Lxw1M9MHL-Z3uYQOlGVUermBAkUrIRAGEnEnCTidkG8OSCb8iPVOqkD_M-AakZSNdn2Q-YH5yiNs3WKI9R7Zzw9nxlngsZ9-LKHbwsAemg5T-NnIfBCvHSfNsdHTQVTJQJ68nNQ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=UzvVxgzOm-QM5xDuHRunB30_OMaKtGkegdYcnM4H7rwzfaz5npNPuyMD2iw37SOXxR-CnSGJqMlYjZGcvQ19-9RBz4CPi6gPD99BgiA_iWahsuAkzAqIP71q2LLKQ4RYjNcQaBVKDRvJpbTOARwpAAWHLonDqNddHjffU83yCGNCmmaDxizsDMlJWNMn_7tQ7g08xWIF5OBA6Lxw1M9MHL-Z3uYQOlGVUermBAkUrIRAGEnEnCTidkG8OSCb8iPVOqkD_M-AakZSNdn2Q-YH5yiNs3WKI9R7Zzw9nxlngsZ9-LKHbwsAemg5T-NnIfBCvHSfNsdHTQVTJQJ68nNQ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پادرمیانی همسر ناصر حجازی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/Futball180TV/90169" target="_blank">📅 14:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90168">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGeKcDrQLVMrb7LaXnAWHeuPHOBVD4pq6iUg7ZZ7ZE9N2Y5ITwuC7fxgnz1TVaNntAHbvR0lR3blp7ZtF5WezEK-ElHzf46J4RlqFkusqFkPeuF9DqMeidvWQ6V9xz8PHrcn1Ragrg3SSwoeDkmIhtWgpRsm_2jFrhuH7k0Dvx_8ZoY5tembwoH1b_XRQmvUaUvd-zCispD8Ut7YtYm_0N6bPQZTo1gJCYk9SHdfeqxrLIVM-Yv2LHDbtHBrQplKVqt-2CidhX7IOIY_8rGTYxvThQ3lwcKr3UEjv7N3p0fQyY_G3_krrsVNn3k5PyqrbpdvR5-mXk2mFDlbouF9cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برونو فرناندز به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ پرمیرلیگ انتخاب شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/Futball180TV/90168" target="_blank">📅 14:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90167">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7ETCM5yuTWL7lJkrKzXgt5jsjIdAKEIYQFBnFJYdHai0WnX5nqne6iArRUT2r3o6itt71-kln__E2_WQE6XSTBKq_T5LO4E437QA6Das6pEw7w5plKEzIzXIadMyr-ei2n8pfZ9dtuuNSY-1TgaqPFN1_ye7an-mv0AmPsh8MpyFymt91miaEVztSPXMv0rfq3qReLf2N0frbZm1DZxB76vj0phY8oMSyz0ygfIOS-XZekw8UqWnShqorWo5C83licaZ5k7vJckm9BIL_Grps80--ep2xegxRm5Cva97Baa3_IXOPrstdOohC2xlA2Uzmvp9eONnFwirMv4-HTG7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/Futball180TV/90167" target="_blank">📅 12:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90164">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=ZmXs_2Va5MQXSBdRAYNgHlRNzxGnmkabOk2Ul2vGbPzqkTxdAVoJ3UDmZMgciWANuMGKCEjyyx_2CqM8d8mXY6p8ifHysSiJYWcVo8dH30R8kDqLFMkf3BxisXo_xVyfBuYkOv1hYsg-dMNCq4Lwc3mLR7Rdk3fH1j9xCemBn_l8rbIVsYh9YGrs5ObgY1CVLECSlIbcGj7ipUgn50in3kiJ5auMDUtn47KgYcAa-SKiPuYr-2j8BpLP6SEyRKxQ0XalIKL3gRtIMT8eEoahd9cE6VL3AefHQ0snaVQIv3QrR0V4XBqNIMvifR4GDEpYBOp-sS0_ldzCNhX6wYhO2iZPjit_Zkl_2VI7GGbW_stJbkNYnHmgUMB9JrcL9NfGby4jEe7CSPXLvTUJpD7nmP6oQ7NANjLGBl1RYMlohDFmNuYpM3hLIHycTyTh3BdQGAGdXjZtBDhyHjNc2IHczwR822tSMnmL8XPd-cRt1bMjDEcRnlzMvRyXR47KnI5COmW29wZWYjX_IVPLMlPVTaUf1ri72Jv4iYXdrN0CvXDbtSOlh_NLOOddcb7dyphsWeKy0p9JlA01LQgh2Wvs7PujeiDjo1fLeE2JJvcXA0BuFVmI_9-toVqLVZd0GbKBY0uulCHg2u7w8yeX8o_ztvKyl_ZTC6Hzq3G-ROwpW_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=ZmXs_2Va5MQXSBdRAYNgHlRNzxGnmkabOk2Ul2vGbPzqkTxdAVoJ3UDmZMgciWANuMGKCEjyyx_2CqM8d8mXY6p8ifHysSiJYWcVo8dH30R8kDqLFMkf3BxisXo_xVyfBuYkOv1hYsg-dMNCq4Lwc3mLR7Rdk3fH1j9xCemBn_l8rbIVsYh9YGrs5ObgY1CVLECSlIbcGj7ipUgn50in3kiJ5auMDUtn47KgYcAa-SKiPuYr-2j8BpLP6SEyRKxQ0XalIKL3gRtIMT8eEoahd9cE6VL3AefHQ0snaVQIv3QrR0V4XBqNIMvifR4GDEpYBOp-sS0_ldzCNhX6wYhO2iZPjit_Zkl_2VI7GGbW_stJbkNYnHmgUMB9JrcL9NfGby4jEe7CSPXLvTUJpD7nmP6oQ7NANjLGBl1RYMlohDFmNuYpM3hLIHycTyTh3BdQGAGdXjZtBDhyHjNc2IHczwR822tSMnmL8XPd-cRt1bMjDEcRnlzMvRyXR47KnI5COmW29wZWYjX_IVPLMlPVTaUf1ri72Jv4iYXdrN0CvXDbtSOlh_NLOOddcb7dyphsWeKy0p9JlA01LQgh2Wvs7PujeiDjo1fLeE2JJvcXA0BuFVmI_9-toVqLVZd0GbKBY0uulCHg2u7w8yeX8o_ztvKyl_ZTC6Hzq3G-ROwpW_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
یکی از جذابیت‌های فصل آینده لالیگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/Futball180TV/90164" target="_blank">📅 11:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90163">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
⭕️
شنیده می‌شود کشور آمریکا ویزای مهدی طارمی، احسان حاج‌صفی و شجاع خلیل‌زاده را بدلیل گذراندن خدمت سربازی خود در سپاه صادر نخواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/90163" target="_blank">📅 11:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90162">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hd5Sdugy6dF1UPNg0vfYRtYdNvonnk4YeiHd8t3DJJBZeGHRFFyEnZE7FxXJSuQrUy5SMK8rILdx7EfksWeWP5T9FPr9_VG-_LQTmc9o-YN2E1h8N7E2os7UsmLoKJprbyI7Dtwd6Lmf1jv9NzlbyWfYooUa3YCTToBD7v2zzI-GX9KUKjlbsrKZQbrq466b-e6Bd8Iyi3gZumaVFXmL8dBpHm28-RGkBmhG0Wi5pr5XOFsisq2-5zJcJEHX-jzhmp7tJ00Bg2fBPLcgTkgkzi_um4qmhr0y9KScO1O9lL2ofg-xe73BDU-0YS_lFTOOXmxiF8J8gIJcuZ-0Nb-czg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توخل: این فقط یک مسئله ساختاری برای ایجاد تیمی متوازن است تا پنج بازیکن در پست شماره 10 نداشته باشیم. حتی اگر این تصمیم دردناک باشد، معتقدم که برای تیم ملی انگلیس تصمیم درستی بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/Futball180TV/90162" target="_blank">📅 09:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90159">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=ngY6aNTUotfta03oxvs1B79JQXDM24xHoqN2XI9RSMe_iDnbMpFUVncqiIW7YiKP_s7wBCuDiAasx_pqZV5HWLcVsuh1b2NT-vtE3u8_sXuZ3XQS25PMxtHtk-XegevuuNYLMAIrnlHXv9PeZ8ElnYrwn_22tA-_5NfKV4gfjyEz4RBP-JfEuvPDJLi31DJEbAUlVsSt9VgkonfRQJSYxEqeS3pLDvTIvx6VMqVm7B30Tz8ZHcKP61eIfTwplcrQ05494bCRoWd8fcitn_GEc8Y8fzNEy3c6MJFwA_1hecjFcgUSmigvlXJPEkj7Bh6mKyIrMkvJpeBrHWMaC09Siw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=ngY6aNTUotfta03oxvs1B79JQXDM24xHoqN2XI9RSMe_iDnbMpFUVncqiIW7YiKP_s7wBCuDiAasx_pqZV5HWLcVsuh1b2NT-vtE3u8_sXuZ3XQS25PMxtHtk-XegevuuNYLMAIrnlHXv9PeZ8ElnYrwn_22tA-_5NfKV4gfjyEz4RBP-JfEuvPDJLi31DJEbAUlVsSt9VgkonfRQJSYxEqeS3pLDvTIvx6VMqVm7B30Tz8ZHcKP61eIfTwplcrQ05494bCRoWd8fcitn_GEc8Y8fzNEy3c6MJFwA_1hecjFcgUSmigvlXJPEkj7Bh6mKyIrMkvJpeBrHWMaC09Siw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ترامپ در سخرانی امشبش:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/90159" target="_blank">📅 00:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90158">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gcn3BkFwOzE73glp-cy4fbQ2z4raE2NdWtKT3D1nxhHyoNStuGKkx2t_FokLGoK_CqH9w7q5Fe6TvDaNyCr98QP0SQ4916X4ZYlrQMj_GcCyl3ctMv-OnDWbxOTyc6w2byS9nciPaL-bBS9xb0KAVC3j3e9HorAv59v7Y4ISzC101GW4WcDbVk74o2y37cQ8042w86bXUWYvm5jM-4wRuxOWzp3YFgOifk4dgjjIL29mbhF5UynFpJj7yior-aO6EWDJN7hYeI-HYKRnSRhatwR00DAdx9cW6s-PeKgLz2D-bn5DqBIS1ngb6MOre8PbbzXcpUm0RtRQ76GL1091kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی کریمی خطاب به شاهین نجفی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/Futball180TV/90158" target="_blank">📅 23:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90154">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HHToZdzpXI-UkKni0sNFscfLOs2rkD_hjc27kosRoa-7r2AVKIBsMuBkq81AugvCcu3RCQxcND5umQJIiIGRhS4H7mxhsV0mh0_Y9vnfJ6pSSQZ3jeQx2N1kQmMPgMz7VNVsHsWdbSkryp1s6PhVpnEjnPgc0_YKa4TioV33KVXTBXLVe6gSlnje3omxC0IIaZjvB_H6_MmM1a6Bo2MuPNvvEu24uKgsdwI9Ljo2wAWN87zpsu4ETEvkqVDTE-4RQONYLJ9QHC8cNNZZ6R1RXLzB1HfGrHghoK6Emeb2Ury5YV1I7JslTjg3-ksPuxMNf8CRwWD9oMxA3VZWdrGx6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_xOv3pXLN4PEE8lcTLX62at6qSeRQpvr-ouz1LePCfAxk8g3wt400oCpZYxuIz6cTHBWQ53dXiBIL6VzTsnEZT8BQoPLqkKVcM_bXZ6UzlmPTlOMBiK-XephZbOXFDG-Oraik-r0UWqTzMLuOTl2Nf8pgcMgVsXshIMFCAnsXM209sbq3ydfzac9w5C1Qbvl4ge_cbNspSvCfQThDDRRuiUGwgR6CMg-zrTAM-paL8g2x5MtzrEK9hUxGGNZckxU1hNHcTb3cGlD70sAqMJ4OsiYCqKJX0Ea94jHCBMQNFDXD-3edJ-mwiEldNaijQvGd2wYnPT8g3ExTZmhO2ovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qPy16PEYMpKRwiwkMJkbqxkC9rZUSOWfhY_N3fC_rEMPGsv1Yl3aM-X_vLEorxzZWx08pYbrj_TXjLTdBPYvabiJw7VTJCMlfyBCR--Huv8zhwygYHGSvppiSWT1Mpi6gwKgg1cA1yy-_fR3R-ZsvIWkG_gltKtCpHdc_eCd_Aepi5g3qPyskgINOOQuXpPIjPbO550Iq1ppkpcqWSevwWQ7kV2UWT8tZ6KBjB-dIlSR2n42gPPG6DRDGV0BC-e7B1f28ze-84yvCWQlQxItGWIIfGiOzRpHMA_Idhb8jifTX8-wbLQ6Gp90EjgXfD7quq6GRTtLyuGy1PlcaBFRjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عناوین برتر سری آ تو فصل 2025/26
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/Futball180TV/90154" target="_blank">📅 20:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90151">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
العربی الجدید به نقل از منبعی در وزارت خارجه پاکستان: واشنگتن و تهران انعطاف کافی در پرونده‌های اصلی از خود نشان نمی‌دهند/ سفر فرمانده ارتش (پاکستان) به تهران ممکن است آخرین تلاش برای جلوگیری از بازگشت منطقه به جنگ باشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/Futball180TV/90151" target="_blank">📅 19:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90150">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU545WmK9_mNVkeqf05chZiK8utyoHWzCFlWnNYIL31DvY32f4C95lKX-_sPBgmG4x0bC9DPHythOuSwRyvNbyZ49K9Lzzp2iuK4xe4DE-ekPYFw7bYFjEcej7LnelIConkmrFoRT3IkNXxXCYsh4JtkEBweh-_9vrT955nv6P9apMrV98BFIIVNojyjgQmvczCe4IK9EBxzFDzxMoDfNZHbHw2oDvPNLjTTNhixHvbQLKyxSLJvfJnbZOB6xOUGPAX93R6H1shkw8EUjq-6Pfx3t_bLh4XzQCVew_-18k7ejHCNNXt4TRs8BCMddCGSiTL1sMlnPWknHC4vm8Jo0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ کیت اصلی بارسلونا برای فصل آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/Futball180TV/90150" target="_blank">📅 19:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90148">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🔵
باشگاه استقلال مذاکرات مثبتی با آلومینیوم اراک برای جذب محمد خلیفه سنگربان جوان این تیم انجام داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/Futball180TV/90148" target="_blank">📅 17:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90147">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLBDnFheucr8YUr6c2HL2-YZcDhePA19I_kLx2hhVsa_eBJKF0o2nd5dxHkHZmsRkMmlSy8cbixbYAF9igaiXrhPPGUL7HpjtR5TAlNGAoyg4echXiXUcmqQ5IPV8oVlHTwA76lShQfzeJ7mx73p84T1e5Xy08SO0hffXuz8hLhCNdZwnTMDfv-ZIUtWy2oo2be420B4v6wf_6VZLnmii1hyXHrSrM2pHgN79h5ERD0xLOkwdlhigEkCfZ120GocGuxbvuG8rqsdyJKkzowrp_415g-d_ybMhsH4pXu0pLkklZnW33kE7rN8lEXdVJNi87E52nDImWeLoeg60f0ebQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNFrKtVZfGd50fpx50YZY2sTFWP9mhPOI7KP9-d9HK1xpyFqTryyze6iFPe1AryA0FTzm3jp_Um8TPHHVF0LGaXma-MzvH4nq7etrLwJvhn2mZLI7tncAtkKTeQJw3aN6sXzRPWm9Xa8tMI1YoWgx3msxNF45AvzhrgHeceyLBmf63AcGAWSmlekFkQi94FkQMC5IW-xTyAHUKv1JH6zewmeU3JK9fxjnUADx5oLek-mlDLKhAOImG5k7Dw9NG33jOdvSaXQnMfWAHi_sYoXx-Rk27ZXY__A2x3Bjp9qtE94765SbmYErBfD7qvkvWpiQxS6aE2XOqatpOeaZx0szA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی دوساله رسما سرمربی دائم منچستریونایتد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/Futball180TV/90146" target="_blank">📅 14:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90145">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLEDsT3Ddnzr2BcsW-jQb3_vD5bKt2eJFvPZz5UUXSpnKLrmus3Ggbljho2RIjxv3gd5Xi7HBaU-BAO1VzAmtbLaj6AveJgiNh9YhvN4eMvJc2HJwhgaXPqI4EVXhqCEs2FrdmveoaS3EdRHleVVcOWq8m1s9DnWFQ56fENp668gIAVKCmCIcZ7efROdohvWVZ2aJqNLBHlYf2nmJ6HfvaHaOwu3k2Lvw6iqOoI_twrliA53IucNx9Uzvc--uWUUr4aE5f4K2wT92nqGyazJZPbfqXCw1ANxr9Xg_SxcTSTvNCUb9-O69QG1pcwqzngsLKxmOvh4yTXIH-hEdV9BGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمی
؛ پپ‌گواردیولا از سیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/90145" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90142">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست تیم‌ملی انگلیس برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/Futball180TV/90142" target="_blank">📅 12:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90141">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwjQUkmzg-Ad9nNSeUGKVpKr5FURKpJ4NuFlV84JZ3HpYDxIgo8j8sT7Q_hca3nuPxIbPKCwX6wo4naZHZqRVpOJvOfSz_W00HEvOmjtTvvu7IvtSZHWgqFf2X19QZh8ZFEtmEJ-3Ky-Q1EvOXDhF1QgwOichxIucrvJi8YFKzx_n-PLD-voWlb_cv380T9-Mn4CuQMohbvrSwL_a4WJsPYOJQtzoc1Xjrq10iFe1T24vGX_HBm1fFkJF2SwymSdbtydn5BjAjrysgRmSpQDb-sFCl_D0_VjJTN1LhfJz7oYLD5-H7bNiLaigZLx1nZbLIdwGFy-VV5D1GBhh0xXaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🇪🇸
آربلوا: با عشق و احترام فراوان،‌ فرداشب پس از بازی رئال‌مادرید را ترک‌ خواهم کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/Futball180TV/90140" target="_blank">📅 12:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90139">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🟡
باشگاه سپاهان با انتشار اطلاعیه‌ای با کنایه فراوان به سایر تیم‌ها، عدم صدور مجوز حرفه‌ای خود را تایید کرد و بدین‌ترتیب باید شاهد تیم جایگزین برای طلایی‌پوشان در آسیا باشیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/Futball180TV/90139" target="_blank">📅 12:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90138">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
❌
در صورت عدم کسب مجوز حرفه‌ای توسط سپاهان، یک تیم از میان گل‌گهر، چادرملو و حتی پرسپولیس راهی سطح دوم آسیا خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/Futball180TV/90138" target="_blank">📅 12:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90137">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4rgNY28Xe2k-yW6_r1Vz77gGBuBBt-Ax0ZM7VwW0yP0KmbSp2FEIrYnK1KMCx8T7u-T_L-h4tn6mWtMQmls7cV0x5fGtV1otsTKik8i-sEyvUHzCPD8dCkzY_HghNkkRBiVjErxYas528buQO8dnAEBnVamAX-BxT0W92dWEnAt1zRYHmMYCy0rQUFqCWZPqhkvyMKUi0RNnw4leXtdfgCZXWghiI9SnMuxcx5x8DAEcYEevxOqckMmXa5_DI8TRtrTAEULc1RhYqJfYN_E_sPWhMRkdD8JsEHyM_Z5BOUAR0DxrtDUH7sVNUyKWMlccRzPBNGzr_uasQ913FvzSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کیت‌اول تیم‌فوتبال میلان برای فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/Futball180TV/90137" target="_blank">📅 11:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90136">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SESPs1aRs5yUz-mB2oEJB8zMxEvRN7wlicFgZDA1CyejuVgmEDKWtRYFhELh7B2CUJsFv7uLSRBL4CsImKOEhxtvwSmANvRNtOmabTVmRjIMb5R6MPgMaPjjdgL5p432-Yg3P4iHcYHahG8FyOdYBipylDzcHJvapxBgPL7MM70muWWeDZSQSXcq0MXxD7aw3T3Z2wro5Hgn1AUikigpoLQGD6OkXvlDTf31cjVMa4wFl773BfgCp4srnEhk0_FmG8dO9XJYs-HYTG_9wA2tgleWj56C58xf3yqwpzYzNPmyrUj8cdVsQYhaBIA0O7Fwv0DmWf5hCt7fRfxPKrmrzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exxI0veCKsp6zG3Uhjzb8WLenWbM4H6SjjsVfJx-1PIRca8aHMHhxxgW1VwJvvEDhWMJrOnZoaRSH03DYbfJ8F3YWIIV6Bk9YDIHznWd5rP0z_xwaOJgkdGqakiz-9744W6c7jRUd2EVMs-ahLw8SI28C9_3eEhmf2E7YT0molcs3yPH_806cJhPfwtei3T672TPBLhOK_By6FP42iogZAfXv0PAzliu2tt5-D9GwWV0MAuXCPgvFCFs_JdUVqtexbljGR-yjQkzHKnYEHEWadvHDO25IvmCrHlbcsh1jwonf58gTIx5H8YCRHYElpxZro7eYrsrjvt3rDjV49sZ3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=qiSdl1k1nixEFO40w8SpTqwTSg3Ie9uSgZubKoSTsoj-wnW0CLSiJ7RFR1PNc9MVMnRhIpqcEWreFLkfq8gBPCeY7laUIaTMh-IXeMiQyqACJk4qjBXNdAzT_fPr7iRuhZIIAYL23a6quWQWZ0Ejxa89fPwid53-HGXmfMQorNTL6UWYxHnFquTTIstG_JU6Jrhapr9_y9UKGOV8KdVlxbaZKUx9pem1-ph_rUaHHJ1218L-5NJ-j7gOGZ_pKCo_El9Zcrmprq6OZaI2CK2biIQskn9FbtY_OfcVaWxs4pohINiJOr1aUlV3mMQOgTXiKXrqTuJkSAnBZgGP4Qnfjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=qiSdl1k1nixEFO40w8SpTqwTSg3Ie9uSgZubKoSTsoj-wnW0CLSiJ7RFR1PNc9MVMnRhIpqcEWreFLkfq8gBPCeY7laUIaTMh-IXeMiQyqACJk4qjBXNdAzT_fPr7iRuhZIIAYL23a6quWQWZ0Ejxa89fPwid53-HGXmfMQorNTL6UWYxHnFquTTIstG_JU6Jrhapr9_y9UKGOV8KdVlxbaZKUx9pem1-ph_rUaHHJ1218L-5NJ-j7gOGZ_pKCo_El9Zcrmprq6OZaI2CK2biIQskn9FbtY_OfcVaWxs4pohINiJOr1aUlV3mMQOgTXiKXrqTuJkSAnBZgGP4Qnfjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی فوق‌العاده رونالدو پس از قهرمانی در عربستان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/Futball180TV/90130" target="_blank">📅 00:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90129">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0_3oFLFJBp7cPYj6B6Ch6day5IK1zzsXMYDleU3ip5QceecMw8JuI9PM0F0uBqH6xOCOakUBkT6uAtGQBruNwxd2MNi1FnGaPV64SA1TEdTcZXIWvl2_d5u0OZFGeNioWe9k5C3IKdglMBO8jN5dv2SiGyK6fVUvvuE0VZSwc4rLv1HIRQzjdr_MuoZAsLCHvj9ysYs3siNBZ3OhpBSyuj-Hfthh9UpsU_pBMAf6ho0qZwK7GUpu68k9J009dEmTf3zwzcqNzO-Ka0dNAPEgjdqawf6Dc_cPCjKXcTEGnqWepuiz8JjJ8feEOfnFOok3P0eI8a3_X_otW1kV4stCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
النصر قهرمان لیگ‌عربستان شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/Futball180TV/90129" target="_blank">📅 23:27 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
