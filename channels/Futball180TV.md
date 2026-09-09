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
<img src="https://cdn5.telesco.pe/file/V4lToKpjSDviDx3cL2dVUVl_BlVhYAOIAzmvbMWO2IwWQ4ZnQMiV5mPQrKwhdZseFAnRx_Kdyp4qUfDYmaiLuAPef37Wx6oicsKyX8VEGzByvNrWQs-bLlLiOBjPU0zfSdseHBx3wTcmkgrj3zkqZWr9NW6iLlUSIZ0ojH9G6FpIEzIzvff9zxgFt0R7TUmiQMHzGJaPMphIHvuR3b3KsfTftKIrlL4_8KjOONKLGf6gHzhFOQKoNpGSQwKru9VtBcShUFvc9X3HxVGA8w7xQUxs26fY1VwELmJWslRjdqjBWm9w7nSevNID7fHgOrmFTZhsIw0siuBInRdJRYtmYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 421K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 19:06:53</div>
<hr>

<div class="tg-post" id="msg-106006">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3Yn8xMc2p7ToIvdZJkPtmsM1atDObDe52gMZUHtQpVgXIlhpPSNoJpDFDWCbbIqc4O6jfaBj0ulsL9EmulPPl0RZhqD4C9102JYueZXNY_nCDfb3D0wVIinRDd1vODmsRClZVboDpnIrQDPHsUSiEPJRVFsWCX8hi_A-CkzLFPIzDvQBlSx4QW7JZL1yzL-Lrqso0oYQo81pTZpCEv65M8vzFus5cZ9Ej_si02shLizxzbeP9LvDSECFfztwE-F27I2oUQk6dP5oEjBMkZAP5-gZxwwgnJvVJCrZxI2xzbPjGMNpiUbK6rIOnzHWT0S9AnjEfj9zu-mXsi51pryZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
ترکیب بارسلونا مقابل فاینورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/Futball180TV/106006" target="_blank">📅 19:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106005">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2045d20cc.mp4?token=QUz2amp6NkQF7Id-S2vFenUps46aLZeU8m9C9qXUkuuLW4c_6SkJ98PBUdDJkZevAJ8x4mxM-cXoXOuBTe3WVzbmIuG9CeNmtXrpF0bVg73H93qLgLyuozp1C27tuIY-SzIUiM1TInFABVsYbl67DmI2TjyamBLS8gPLd_fxplwWeQV9kxfX5jq5vP72GvgfPOiC6u5SahwxaSwQU-G6hBdStMq_NMHVQFwPXQ2eC4GxTq-0QE2V5FFN_IvVoFU3b_YsKGTIG6DC9f2t4wqc5Yw9GzaRTX-PWqo5CxC6jliHKzN6yvqWOWzZfZFXehNVMstU_W8x8fQeCkQI8RPqJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2045d20cc.mp4?token=QUz2amp6NkQF7Id-S2vFenUps46aLZeU8m9C9qXUkuuLW4c_6SkJ98PBUdDJkZevAJ8x4mxM-cXoXOuBTe3WVzbmIuG9CeNmtXrpF0bVg73H93qLgLyuozp1C27tuIY-SzIUiM1TInFABVsYbl67DmI2TjyamBLS8gPLd_fxplwWeQV9kxfX5jq5vP72GvgfPOiC6u5SahwxaSwQU-G6hBdStMq_NMHVQFwPXQ2eC4GxTq-0QE2V5FFN_IvVoFU3b_YsKGTIG6DC9f2t4wqc5Yw9GzaRTX-PWqo5CxC6jliHKzN6yvqWOWzZfZFXehNVMstU_W8x8fQeCkQI8RPqJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیزر جذاب از بازی امشب اتلتیکومادرید و لیورپول در لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/Futball180TV/106005" target="_blank">📅 18:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106004">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCPF6Xny5AqqHffPzDPUT56u8TCCYyGYt63TUPkM6Bg5oLyuhi4-6kBM7K_MXz2aR_tKHgK0VcMpQgPtMIIdo4A8rJABiISYCIzT3d1hPmxzvHIkaERFaCdIJ63_mqWlyr2PMwh3xscNIdPctPvs81rFkwvRvP29XUqYkDC4X7vWfZSJmPhnoBLWZf6HsQxnYRRRC2sbp-rark8i7Fh0moqJh0vQXorfsTMD_4tO22nKaz6ua2iW4gvWXMvwOdwWzo7MlZOQX_BEkzEhGfSeA27xUCD5XamddmMXjPSFEW4TVjjzZJZEeJ_YQEnqvb0UwQA36G2ISdiW13kRR1GywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
😳
😳
مدل موی جدید مارکوس رشفورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/106004" target="_blank">📅 18:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106003">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c95f05bffb.mp4?token=SWXhphi4X4q005x0JMNfEUR9TU8quNXLylV2xmjKJqzQaU3qijdcfSzI9EEPZaFjWs5ZYBB8Q5bxNGT-tcjcp3aLPDDw12kUD432u-0_J4B79PV5-8cQQxvzKH7VQRyk2o63ZCFRn4YyAswxh5wC6090r7nut5w_tsoyoxqq2sY41NRrXwfeufLFJ4VKlv-Q9ni_DIwX2wTgOEBL3W7thQL5zJXtOvnwq8GrKv8lnIDAW5QaJSa_Sr4r07RS_eThYeLNmAWjcV3kIOe69DiTGYC74d2xPwsmsuuHGYS-tpRwsGG7ppIOKNxEiVNmkQiqGUM-PH54hrsVZ8EhcREfHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c95f05bffb.mp4?token=SWXhphi4X4q005x0JMNfEUR9TU8quNXLylV2xmjKJqzQaU3qijdcfSzI9EEPZaFjWs5ZYBB8Q5bxNGT-tcjcp3aLPDDw12kUD432u-0_J4B79PV5-8cQQxvzKH7VQRyk2o63ZCFRn4YyAswxh5wC6090r7nut5w_tsoyoxqq2sY41NRrXwfeufLFJ4VKlv-Q9ni_DIwX2wTgOEBL3W7thQL5zJXtOvnwq8GrKv8lnIDAW5QaJSa_Sr4r07RS_eThYeLNmAWjcV3kIOe69DiTGYC74d2xPwsmsuuHGYS-tpRwsGG7ppIOKNxEiVNmkQiqGUM-PH54hrsVZ8EhcREfHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
✅
سه‌قاب و سال‌ها خاطره‌سازی برای مردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/106003" target="_blank">📅 18:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106002">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsJVw0mcfe6eKNmfKmyLuikzU0dySK5BmPPlbOEmxZwDO7XCKgoWlfUa_5HIertvyiIoE1bpgFw_Q6rPeMVmwNR6MpF_dHusNUnJtrhz-T4vA0MZXMFO4o1u_KjbleN-tH3Zp6qtLxOnPh5I43NyNnuDXkg81RHR4rINYDS5zxvis1E2W4JC3msB5R-hrxhTc48JSOQd9epsSvPcdFRCZh8wHEiqE3jjJE4yTSnDa59oB4zon0d6iD-sKHrq8eSNdOTOvZA4DUXN2NSXAuyAfkevOnUVsUoSigvpyEU2FxLeP5QC3nOguvFiRR4AnLqx9pZGwDlLarhq8IxzvBRDIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
❗️
تصویر جدید از استایل فاطمه‌پسندیده و عاطفه رمضانی دو بازیکن سابق تیم‌ملی بانوان ایران پس از پناهنده‌شدن به استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/Futball180TV/106002" target="_blank">📅 17:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106001">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8mC5S0hlrX1vC_aUptiIO4F--_Q-WPA2xiHKcIeyzWIgcyW-AnbLAQ08RzeuGlXtJ-tuRmvod23kgkfSHvGUxuZ19BsMEDmo9WKakvevVNcBKwdzQTzWjmN6ytqBJQcGEzVpmKvkdbwAYhcf5fuo9YKv4uWhFTNlnmmtXkF5d1owBFfMuVzlUMdt0bnkF4D9J6DN_EV9sUS97CvP4-mtJ1_NJ1Lx82T6M7ZNyVo1zs5VFjXDWv0OV4hjn_pp_2RaIJ9vxSPcITKgM3A78aPOMLRVng_rj_ybbuWHA9TtYruY_HzJNRRjyok7OkKKkHl4IdRHM3v1-gXmVYdDkWz5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
برنامه مسابقات امروز لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/Futball180TV/106001" target="_blank">📅 17:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106000">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106000" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/Futball180TV/106000" target="_blank">📅 17:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105999">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-SzeAXM8frUtHsvky9PqfTIgWXxsc5N6GN6z2FUr9VLY00NwfGkYN_Uw7moRNuLfzIpuXxFVMYGpo-rBH-1cVeCOP7bUB6TQsr8IvYDKCMVmbdDNxclEK4Z3Yt96sITyTT_bCg4NINLsi6Hkn4R8Q-hZZaVRRIXBpvzwcwVzDex69oMNGCxVBOj_cjssK5BGXcZvcGzJkW_jQx0rl4x23G3NNsFrBN_lyn6ZBR_r8xawoXZOK9IgfLH5LnbIc-tx6o6mNm9GgH3r-UmqP1Fqso6U5D_qqR_DN6wMqvF_XvYiHJ7ov7MnkQbctJaeEjXJElPHTnAPsD9qc45ad-z_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرسنال
🆚
ناپولی
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
آرسنال: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
⚽️
ناپولی: ۵ بازی ۱ برد، ۱ تساوی، ۳ شکست و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/Futball180TV/105999" target="_blank">📅 17:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105998">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a6458393.mp4?token=Bec12cq3MVoBMHUNnjgx24g5c3ilxb_EQ2hxrwZjC3p6RnYUUcigpcMK7-Wy24A_MEmqVvHimuaEgZ_zqQfjbtVsDDqwV6OtBulExVRRk86vtbrBDXzUyJ2SIQjnLMpMdq7VBbL-sqOqtUm8hz1NrEZwMSempI6yF9goFYHAjDRuzjPjhYnPtj3Q7j3GVVApah9Fub-J8wYspQ6IEqHd0YjrY4NO03ZVFI2Z8hGrJfVWZrYuktfwNjrgcpPZ0ujFYJvYeeObCFsnuWvoyHRXvqoto_l4rGAxv8yCQ95l839yLQYMyTgmLFDgIAEzFh_DWcDvrXKz9Bs5g-sZJVVxNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a6458393.mp4?token=Bec12cq3MVoBMHUNnjgx24g5c3ilxb_EQ2hxrwZjC3p6RnYUUcigpcMK7-Wy24A_MEmqVvHimuaEgZ_zqQfjbtVsDDqwV6OtBulExVRRk86vtbrBDXzUyJ2SIQjnLMpMdq7VBbL-sqOqtUm8hz1NrEZwMSempI6yF9goFYHAjDRuzjPjhYnPtj3Q7j3GVVApah9Fub-J8wYspQ6IEqHd0YjrY4NO03ZVFI2Z8hGrJfVWZrYuktfwNjrgcpPZ0ujFYJvYeeObCFsnuWvoyHRXvqoto_l4rGAxv8yCQ95l839yLQYMyTgmLFDgIAEzFh_DWcDvrXKz9Bs5g-sZJVVxNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇮🇷
🇮🇷
تیکه‌به سهراب بختیاری‌زاده به سبک‌ جالب مهدی تارتار سرمربی پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/Futball180TV/105998" target="_blank">📅 17:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105997">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04d5f7ca29.mp4?token=knbUBaGXZSOVFeAkLoOUQsvWRgz01_FeDlIujLG3XIRM3-g-pd49wftZMBJMEDWMClKIbJX3VS1UapuSUbnZjvmFkFJzwkUbVeiyUaoZFnJkfxVoWcli1O3ghZyGVP3X-VEB_5in5burGKAcqe596wzfeoHyxihiFd-LH5UIM_B09SqnEOSlClrbkaeNJa0FJYIlf0lT1ZmoDa5feT9NbcF4Q9i92O6UYPLOthEJReZznnuoEEK4SoZiAFCNbUMMFqshIYfRVDPiuhh91UYpClj_dA8x07MMXogm9Py3DMzKlue7bpKHou_XNuzJf1QXH0-0fBe7dPft-fd-UFERTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04d5f7ca29.mp4?token=knbUBaGXZSOVFeAkLoOUQsvWRgz01_FeDlIujLG3XIRM3-g-pd49wftZMBJMEDWMClKIbJX3VS1UapuSUbnZjvmFkFJzwkUbVeiyUaoZFnJkfxVoWcli1O3ghZyGVP3X-VEB_5in5burGKAcqe596wzfeoHyxihiFd-LH5UIM_B09SqnEOSlClrbkaeNJa0FJYIlf0lT1ZmoDa5feT9NbcF4Q9i92O6UYPLOthEJReZznnuoEEK4SoZiAFCNbUMMFqshIYfRVDPiuhh91UYpClj_dA8x07MMXogm9Py3DMzKlue7bpKHou_XNuzJf1QXH0-0fBe7dPft-fd-UFERTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✔️
یامال:
🔻
"فقط کافیه تیم‌هایی که این اواخر جام بردن رو ببینید؛ تو پاری سن ژرمن همه پرس می‌کنن، اینجا تو بارسا هم سعی می‌کنیم همه‌مون پرس کنیم. در نهایت تو فوتبال امروز اگه ندوی، هر کسی هم که باشی، همه تیم‌ها میبرنت."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/Futball180TV/105997" target="_blank">📅 16:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105996">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94734143dc.mp4?token=RfMHFCZge-H7R9e5NENJt75Nkd3bpUGYIxXP5nezvGPMOe19w95BlIziEHvMKJse0HxOLWkiCVmfF_PLwTEfT_SIEBby2S69fRf_uKzw2dkoaqsahUviuLQ9pGGHKZl9O1cwz73yVlzSryvqGqzGg7ZF-dq3A5Fp1SSBrNTosrdqlVAjNhZX5BEWIf50LLMFZvqJlpqDJL0k7fTx-_p6vA4W0JAqcDV6V31rJfU7kZ5jV3HFS8b1CRfGZmT_UB4QRpFgdNHT6DuyW8Yw47W197OZE2KyFQPzmRn02YyAvOLYKGb-cTcQUSkfHNNIlfCTkTbFAwN_8M5DJZDaCEW70A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94734143dc.mp4?token=RfMHFCZge-H7R9e5NENJt75Nkd3bpUGYIxXP5nezvGPMOe19w95BlIziEHvMKJse0HxOLWkiCVmfF_PLwTEfT_SIEBby2S69fRf_uKzw2dkoaqsahUviuLQ9pGGHKZl9O1cwz73yVlzSryvqGqzGg7ZF-dq3A5Fp1SSBrNTosrdqlVAjNhZX5BEWIf50LLMFZvqJlpqDJL0k7fTx-_p6vA4W0JAqcDV6V31rJfU7kZ5jV3HFS8b1CRfGZmT_UB4QRpFgdNHT6DuyW8Yw47W197OZE2KyFQPzmRn02YyAvOLYKGb-cTcQUSkfHNNIlfCTkTbFAwN_8M5DJZDaCEW70A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
بانوان جذاب ایرانی در استادیوم‌های مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/Futball180TV/105996" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105995">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a6a8f2ee.mp4?token=lzRF3QFqcErzGmDvOLUBVkg0zLKAyDBHK0CSJz1584SAHKDHxzt2cJj-5nGvwi9_aiPr0dBCpz2anzadmcsmlxtH5fFDhFziDwX5EzZHVCDYO3bgHNF3ixHcO8C6H9j--hRUhv7mnvvS7mltg9rkvQ_qbjfhsXU0w59kUxy68YZGWIkZinA4wbj1vhiWTdgskwb47LwJW8CUrsoUl65naka1SRj84ZtYNv-fhBEIgUKIj6cKXw2wWFQDHowwUDZVo_UrwRGzNz2QCryXz981_-iTCsbu9WfLZ7AR-f2HrK1LwObCew6xyLJfnnRJnlXU6z3G2Oy4o7K8NHzdn318cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a6a8f2ee.mp4?token=lzRF3QFqcErzGmDvOLUBVkg0zLKAyDBHK0CSJz1584SAHKDHxzt2cJj-5nGvwi9_aiPr0dBCpz2anzadmcsmlxtH5fFDhFziDwX5EzZHVCDYO3bgHNF3ixHcO8C6H9j--hRUhv7mnvvS7mltg9rkvQ_qbjfhsXU0w59kUxy68YZGWIkZinA4wbj1vhiWTdgskwb47LwJW8CUrsoUl65naka1SRj84ZtYNv-fhBEIgUKIj6cKXw2wWFQDHowwUDZVo_UrwRGzNz2QCryXz981_-iTCsbu9WfLZ7AR-f2HrK1LwObCew6xyLJfnnRJnlXU6z3G2Oy4o7K8NHzdn318cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
🏆
لامین یامال: «لازم نیست کسی را قانع کنم که من شایسته توپ طلا هستم. هر کسی نظر خودش را دارد و من فقط به کاری که در زمین انجام داده‌ام افتخار می‌کنم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/105995" target="_blank">📅 16:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105994">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f3510400.mp4?token=V9KiznLSxXSgtQailzJ_9rV48n7EdfV5-J1kKIja4_WDFYPaj_aMG0PyWOnhzDM03vcLFfYsCC9skjniRRmzfmzem9X3FJBpiCMFpU96tCvq8idqAP8tKUUW3g708sqsxaJhXr36Ib8VM2-XDctVZvt91kM-_8TgLxvLOYGbfUrvxMWjmDRWn23Nstpe3DWzPHqftwK0i_fZJe_Z4tWSJHSHQFa1A1ugJefCD5mtfFEQYcqBJvllhTiJLr9eCVFZsSrgi_xtTXIdScUySxplyPhM282J7Mjno_WR5dEaWhVSId3w08e_SezpPVDToXVFjuvAceC9E8eR3ok9cRl0Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f3510400.mp4?token=V9KiznLSxXSgtQailzJ_9rV48n7EdfV5-J1kKIja4_WDFYPaj_aMG0PyWOnhzDM03vcLFfYsCC9skjniRRmzfmzem9X3FJBpiCMFpU96tCvq8idqAP8tKUUW3g708sqsxaJhXr36Ib8VM2-XDctVZvt91kM-_8TgLxvLOYGbfUrvxMWjmDRWn23Nstpe3DWzPHqftwK0i_fZJe_Z4tWSJHSHQFa1A1ugJefCD5mtfFEQYcqBJvllhTiJLr9eCVFZsSrgi_xtTXIdScUySxplyPhM282J7Mjno_WR5dEaWhVSId3w08e_SezpPVDToXVFjuvAceC9E8eR3ok9cRl0Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏆
نظر هانسی‌فلیک درباره توپ طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/105994" target="_blank">📅 15:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105993">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d749e34c6.mp4?token=LPQjF-JpRun6KGwrgY5yynRaEhuFl59fgMBcZJoImG7_J-8cnH5PsQ8QqfboiBQcO4HXgDhVbC7hSROhjgTTRZBMxRwZrb_mxu6asi5MJYUw2ak5J8OOp6VwCd2mUpDFAgy00QPo5s-aP3Ds63lPUpwo6fdTA2M-IBFpg0UlrgXfVlJu0-i5l3FF4uZ78CRFkjjr9_0tOU2eqGBPUxcPOKms-llpH8oAkBT8Nku9MoWi_bbh5-orECyRU5rsR8kUT9NtRTJPVKaAY054yAwhfbf3U6YCtQdtu00bXk_LY6YEQozRTI7kqI9syHxR-EOTZdTFV50LURUtFs5ULMCRRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d749e34c6.mp4?token=LPQjF-JpRun6KGwrgY5yynRaEhuFl59fgMBcZJoImG7_J-8cnH5PsQ8QqfboiBQcO4HXgDhVbC7hSROhjgTTRZBMxRwZrb_mxu6asi5MJYUw2ak5J8OOp6VwCd2mUpDFAgy00QPo5s-aP3Ds63lPUpwo6fdTA2M-IBFpg0UlrgXfVlJu0-i5l3FF4uZ78CRFkjjr9_0tOU2eqGBPUxcPOKms-llpH8oAkBT8Nku9MoWi_bbh5-orECyRU5rsR8kUT9NtRTJPVKaAY054yAwhfbf3U6YCtQdtu00bXk_LY6YEQozRTI7kqI9syHxR-EOTZdTFV50LURUtFs5ULMCRRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇪🇸
🇪🇸
لب خوانی صحبت های رودری در جریان دیدار بارسلونا مقابل والنسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/105993" target="_blank">📅 15:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105992">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f76b6880.mp4?token=sqCOUg-nYJGZ4EytkRUcDdnhqsADBa_lVnbrS2vm0YB2jZwHD291a3145UdEDfW9J_ezZ6ovdO2v5gtlxQfGPzNoOHSMTanMoUWjuOW5OWNv4ElwICNU-OUoU5J-JnbeocDd8QuY-ledI9Vg0PMxi4fjY_ch069mWy3S_sMTCBfB0iOIkTx5TWvkbL9HNaQruEo-dfzxulVPQi4G_kRg1jwB6fQAkb_uIrh6-AMZGNCChd4AwnFCW7I9pDAK-pJ7QuVcJtUd7lC0HZ3NPrixGSzwEdhzIDP1xL30KqNmIW06ybrI_cDVVfgC9zHIvH7sxbAv6RqHxpDlXiuTURbCAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f76b6880.mp4?token=sqCOUg-nYJGZ4EytkRUcDdnhqsADBa_lVnbrS2vm0YB2jZwHD291a3145UdEDfW9J_ezZ6ovdO2v5gtlxQfGPzNoOHSMTanMoUWjuOW5OWNv4ElwICNU-OUoU5J-JnbeocDd8QuY-ledI9Vg0PMxi4fjY_ch069mWy3S_sMTCBfB0iOIkTx5TWvkbL9HNaQruEo-dfzxulVPQi4G_kRg1jwB6fQAkb_uIrh6-AMZGNCChd4AwnFCW7I9pDAK-pJ7QuVcJtUd7lC0HZ3NPrixGSzwEdhzIDP1xL30KqNmIW06ybrI_cDVVfgC9zHIvH7sxbAv6RqHxpDlXiuTURbCAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
ماجرای صفرهای ثابت پمپ بنزین‌ها مشخص شد؛ جدیدترین شاهکار مسئولان برره‌ای مملکت
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/105992" target="_blank">📅 14:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105991">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6385fe8792.mp4?token=AkhsA3B1Jtad_fIttjuqY3Ai8IeQPIA2ZAN7uYZeWNZ4JCdSMHctyH1-atOUH5YdZoE-uoNn9HBW498pp5Led6CH7b_e26-dh4JLjGgaRKuZK7ZSRiF8vy_SSPFC8ku1t11dUviuXNVireyIWNLQRJtRRyN7fxeKI2LTvNIgZr7Znm6thuy7e4N3MqkWkxKx0os2Yjj0-E9jh5atCUCOgJ2ONvLHZUasmDpnbD-_G_tQYWtJ7kx3vc5DWHvEnBHzZkijPOXKukmLn-orxZh9NnuBSXc5CgBaaCPIrhT0RsPZuZrVnQzcIoSCFtVIUGoRJkfLdLUi2HACqLEkcAx-TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6385fe8792.mp4?token=AkhsA3B1Jtad_fIttjuqY3Ai8IeQPIA2ZAN7uYZeWNZ4JCdSMHctyH1-atOUH5YdZoE-uoNn9HBW498pp5Led6CH7b_e26-dh4JLjGgaRKuZK7ZSRiF8vy_SSPFC8ku1t11dUviuXNVireyIWNLQRJtRRyN7fxeKI2LTvNIgZr7Znm6thuy7e4N3MqkWkxKx0os2Yjj0-E9jh5atCUCOgJ2ONvLHZUasmDpnbD-_G_tQYWtJ7kx3vc5DWHvEnBHzZkijPOXKukmLn-orxZh9NnuBSXc5CgBaaCPIrhT0RsPZuZrVnQzcIoSCFtVIUGoRJkfLdLUi2HACqLEkcAx-TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇮🇷
🇮🇷
رشوه مادربزرگ استقلال به نوه‌هایش که شدیدا به تیم فوتبال پرسپولیس علاقه‌مند هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105991" target="_blank">📅 14:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105990">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBUuZYnpWp8PcE8WQSaQc9vOZb3vNqVERQRWcrU6l6JWMWGfYBM9-39mD6Wu-hKwV66NHfsN4p0LCHyAK7D9p-XNbf8j-S-EibtnGyPnq-IlJZUWJ1jy19_GQAtxZ0KZBi3tujwzRM39bu72uGQcFt2oVYAXvJPGPaJYUcRuskDr3ImO6riwNZhh1hgfbRkZkYqPqK8RaWEesIbgKLn3I5itDO3fKqxpXrGTFh1lVI57KPI8m7A7vr3rTUKHjtmqRbRhK-vE3A7xzWk6fEjj5UPyAkL6vfxpnPd-0lHmmYBNgd7SsO4xap6_DumUYqvXh20f0Yzh9PupmpyyB6kBQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
رقبای بارسلونای تحت هدایت هانسی‌فلیک که بیشترین گل‌رو از این‌تیم دریافت کردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105990" target="_blank">📅 14:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105989">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a4352655.mp4?token=kmhlS8e-s-j4M2xiH48KRo5SANETYD8mLyri9Af1aji9iPZnnzBYT4QL5PvoHVRhznrxuHEelQwQjMMxJLVRh7GEqY7QLvbmRCMa297A2TzfUVCgarfHeo4R8-lk5vgfafzzZdQvdvNBw5WvN659Il8xlOT-YQ-kLghdquCV84uzJ4fjoTq7686Yk-tVeBqBQoYrfu5-Y6AoGZ5wJJ8pUApPLH4eEUE-eciEaZuf4JNP-zo4VNiiB6iiL1aCi8YW6zCbrLf4TDzeNNHSy42p0mcf-g7jZyzc185UobHIt0VPm440G1E-FF9lAjpbTpmTkoAradERdqgCg4lVvGkiLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a4352655.mp4?token=kmhlS8e-s-j4M2xiH48KRo5SANETYD8mLyri9Af1aji9iPZnnzBYT4QL5PvoHVRhznrxuHEelQwQjMMxJLVRh7GEqY7QLvbmRCMa297A2TzfUVCgarfHeo4R8-lk5vgfafzzZdQvdvNBw5WvN659Il8xlOT-YQ-kLghdquCV84uzJ4fjoTq7686Yk-tVeBqBQoYrfu5-Y6AoGZ5wJJ8pUApPLH4eEUE-eciEaZuf4JNP-zo4VNiiB6iiL1aCi8YW6zCbrLf4TDzeNNHSy42p0mcf-g7jZyzc185UobHIt0VPm440G1E-FF9lAjpbTpmTkoAradERdqgCg4lVvGkiLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
فرق زندگی در ترکیه و ایران از نظر خواننده ترکی؛ عایشه‌گل: مردم ایران به دنبال پول جمع کردن هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105989" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105988">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3185992aac.mp4?token=U7HSTdOFjkQ-CPtUy4rNVn98qkPhYgAWHNXMj1mK2FqondM8WsMf_bmvdxWLOL_ZuSJmp8P_0hEK1478B8vl0i5GgoTyVJCg6wDSN76PA7OUv0dfZ8nVRoqzJu_mHMN-QvAKVq5Dpe1klFm8ED7wKx4qE0VOpYOBD6v-T1pYZlWO8I4P1pE_vz1TvJ_HQG3YD5tok0sy4CcE7oMw8fBY7pk_hRmAolrHG29XnBqBH4iQTWHL5ZFIpiT6_yBxO-injURTnd_wMxfi1I10LNXwY9HQJBVID3m9Y9uyL3UUBAVkK86Dvm3pmirmQexrVgR-jHR_jFmpcAwLcoTMsNmWNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3185992aac.mp4?token=U7HSTdOFjkQ-CPtUy4rNVn98qkPhYgAWHNXMj1mK2FqondM8WsMf_bmvdxWLOL_ZuSJmp8P_0hEK1478B8vl0i5GgoTyVJCg6wDSN76PA7OUv0dfZ8nVRoqzJu_mHMN-QvAKVq5Dpe1klFm8ED7wKx4qE0VOpYOBD6v-T1pYZlWO8I4P1pE_vz1TvJ_HQG3YD5tok0sy4CcE7oMw8fBY7pk_hRmAolrHG29XnBqBH4iQTWHL5ZFIpiT6_yBxO-injURTnd_wMxfi1I10LNXwY9HQJBVID3m9Y9uyL3UUBAVkK86Dvm3pmirmQexrVgR-jHR_jFmpcAwLcoTMsNmWNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
توصیف عادل فردوسی‌پور از ریدمان فوق پشم ریزون دیشب رئالیا در بازی با اینتر!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105988" target="_blank">📅 13:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105987">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/058b97f620.mp4?token=sfEGUGlUGzQBAwzgcfk_p_sidZN0aSzGiTFltVIx1lFbIRydHyQ8v_jLFaHUhQXfaSrLT3KyDJtBU23dYxczaAEGTRxy1kiWdBKwrWVpe5TXLig2ABd8_GCvTTcsx7rkS3ifcl-wJ92QCkjOsYppwfPk8TD5HR7LbfonWdLr8O-3PEpNuRMWRMZTieP7-rC79w6y6AfDMay_J_b31jewBqrFY7Cxool37oNc42F04fdXNlMbiOQaRsGj3WbQc6iCXJZolKjZQUw3sdAynUxKYbTktnuoc0eugeZVS8A_mjuG5Nu8l7wnjyd3NGbojcrtdoOA_1pu1lYgsevhVP5iV7Sve25PBYtiQYpwCaY2Gdl-rgqFAvCvgyeIQ2woM-BwDLz-rtOnndc_sJr1CYNZteG9cnYwSgGLTm3exa2Gw1DP1F6U_Wn6pRfT-qYZFORaeFMnLC5PZeyKHekIxAhdeOY2hdMQIOaaGT51SR6nZml1D0LFZ0OtLQk2JVrgloFji2mXDf33SJoL2tiHfECI2xvG3X-1add2kT9YOa6FGrQmYwUgm3TiEkqvC2Jlra8_0fQAnJ2Cdfo3DeiOqkXPibs1rbyKWmlz4RchpvGnZMOkyeJoJ9shN75q10IzO3VPiRsagQhNNLF_NWvGxtB8xhrmtfHf-uf92Hx5zfTfa5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/058b97f620.mp4?token=sfEGUGlUGzQBAwzgcfk_p_sidZN0aSzGiTFltVIx1lFbIRydHyQ8v_jLFaHUhQXfaSrLT3KyDJtBU23dYxczaAEGTRxy1kiWdBKwrWVpe5TXLig2ABd8_GCvTTcsx7rkS3ifcl-wJ92QCkjOsYppwfPk8TD5HR7LbfonWdLr8O-3PEpNuRMWRMZTieP7-rC79w6y6AfDMay_J_b31jewBqrFY7Cxool37oNc42F04fdXNlMbiOQaRsGj3WbQc6iCXJZolKjZQUw3sdAynUxKYbTktnuoc0eugeZVS8A_mjuG5Nu8l7wnjyd3NGbojcrtdoOA_1pu1lYgsevhVP5iV7Sve25PBYtiQYpwCaY2Gdl-rgqFAvCvgyeIQ2woM-BwDLz-rtOnndc_sJr1CYNZteG9cnYwSgGLTm3exa2Gw1DP1F6U_Wn6pRfT-qYZFORaeFMnLC5PZeyKHekIxAhdeOY2hdMQIOaaGT51SR6nZml1D0LFZ0OtLQk2JVrgloFji2mXDf33SJoL2tiHfECI2xvG3X-1add2kT9YOa6FGrQmYwUgm3TiEkqvC2Jlra8_0fQAnJ2Cdfo3DeiOqkXPibs1rbyKWmlz4RchpvGnZMOkyeJoJ9shN75q10IzO3VPiRsagQhNNLF_NWvGxtB8xhrmtfHf-uf92Hx5zfTfa5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
💙
بختیاری زاده: بازیکن به تیم امید نمی دهیم/ تیم امید مهم است ولی شرایط تیم ما مانند تیم های دیگر نیست/  فقط آن زمانی که قانونی باشد بازیکنانم را در اختیار تیم امید قرار می دهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105987" target="_blank">📅 12:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105986">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx2-7pu1dhP8W7xYhRIW2zEPoXSpTbuWiBSlhN59NVUUGoLEXJiE_gkzrq2HEUA-p--xPUjDGa0jBSWwc36h3df7cAbnr8XDdD2gRyclUxjw9eIRnPHvD61kcmGgFEu7yEQjZAb4Aj5KVQEYi_PKlfgquoeveaOVnEw-l2iKgSIYrw0tFX0rRXT3pAZsvLTmF9oXLaFA9vw3UQoN24HOi-TXdGZo6mhSfE7D5PlDil-sAcvs9TATMKeCjLlZZRYrWjPF9Bs7Wl7Ml5NWJpVmzZUBuLmI65N-jGx4lmcyn_jl00BmEpESTyPSAoTDa77DyP94hrwGpUZKDbSTOWImMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
⭕️
⚪️
یاشار سلطانی فعال رسانه نوشت: ‏در پرونده فساد فوتبال⁩، برای تعدادی از مدیران ارشد و چهره‌های فدراسیون فوتبال به اتهام اختلاس⁩ کیفرخواست صادر شده است
مهدی تاج⁩
‏محمدمهدی نبی
‏احسان اصولی‌صفا
‏تهمورث حیدری
‏خداداد افشاریان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105986" target="_blank">📅 12:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105985">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105985" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105985" target="_blank">📅 12:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105984">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z026uW3CunrBYV1BYH69uKYViT0FAXIFBluk0pIAHR3pmK5Yq_8VFYE3rKNa6YjmRKg5fvWfRaqFMmBFnDjyuNO6_jDFGhRmXeniI51MVGtJboEcQ-CPGrFRg3Sl0Cz7rYxmkVf-rlRoUe5WJ8-Dgeld6x01RzV-rePpoQEtd-UBxw1FN7PSm2OR3AM-mAyKEsajaFIxxISoRlNik4dYgVFJhqF1IDgp26AxhWXpKeqrV2YoWOGrYKI6J7MUWFwV3DDGMSd3UVFXryoQJ16JnKLHFsuSTccE0DJBuJ6GWNoVwFFI5b3Y2Gve7IkdWBUqPtMAYnwhuErkW6SpBPtM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
اتلتیکو مادرید
🆚
لیورپول
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
اتلتیکو مادرید: ۵ بازی، ۲ برد و ۳ شکست، ۸ گل زده
⚽️
لیورپول:  ۵ بازی، ۳ برد و ۲ شکست، ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105984" target="_blank">📅 12:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105983">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cd51b2d93.mp4?token=bhDwR3jApRuwb9-lYiOYy5_w5oti8htsbQsTJ0akkz7-_swaQtugn8AXA5FlLU9Wzjz48QYdJqMqtmVRtaHL6NBGMsW1xbBpyYuiZTz77MkqM5b3JjYmwCdyh6BIlXos--C3cnAz-SvvSTDBHC1AX9v_2mDspVJ9Rt4LjscPGogPSrxpPWgjkkBhzc2BsolYZUJSGb1GpF-I48ZeRz0JYVhCvLEZ7GJEC4rtW16DGlEejpy1V4Q-W4B6L_U2IJjVwo2FfAvj2Utfs_Yw7-zN8u5NFTuR2LmxBAxH0qAUhmzapSisUkXBNSTnFCuSMIydtfNun9viRnTsT8cxax2WN28XnbYSzqmddAfvpEoHUsTXfp6Pud7AoS2SeJ9rcxvWXf3LsffGPBAdQ42CsCzS3LKBvUGc-rP88QoK_lm6j_mW_3rjjJYPEpDQSMjMJVt4wol2ilfaYmxTh6grYo8nMsOBnkpxFS6gPlWz3cb_gheFLce_GM7G83qOjZAUrxkQvkHfdIAi-EZzFVQ-8v0FPIII37Ha7oBEGTEF27tx2dhqln5aUrai-5cBs5mSldsO5_twF1uAWvMvjTx4wuT5vO3WZTkSsQFoRqH835p9G19IK8wwEr8LwICW5T75Gry5lWvvaRk47spD0TaKsUwAaDO7jLG-pbs7-yE76YzgeTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cd51b2d93.mp4?token=bhDwR3jApRuwb9-lYiOYy5_w5oti8htsbQsTJ0akkz7-_swaQtugn8AXA5FlLU9Wzjz48QYdJqMqtmVRtaHL6NBGMsW1xbBpyYuiZTz77MkqM5b3JjYmwCdyh6BIlXos--C3cnAz-SvvSTDBHC1AX9v_2mDspVJ9Rt4LjscPGogPSrxpPWgjkkBhzc2BsolYZUJSGb1GpF-I48ZeRz0JYVhCvLEZ7GJEC4rtW16DGlEejpy1V4Q-W4B6L_U2IJjVwo2FfAvj2Utfs_Yw7-zN8u5NFTuR2LmxBAxH0qAUhmzapSisUkXBNSTnFCuSMIydtfNun9viRnTsT8cxax2WN28XnbYSzqmddAfvpEoHUsTXfp6Pud7AoS2SeJ9rcxvWXf3LsffGPBAdQ42CsCzS3LKBvUGc-rP88QoK_lm6j_mW_3rjjJYPEpDQSMjMJVt4wol2ilfaYmxTh6grYo8nMsOBnkpxFS6gPlWz3cb_gheFLce_GM7G83qOjZAUrxkQvkHfdIAi-EZzFVQ-8v0FPIII37Ha7oBEGTEF27tx2dhqln5aUrai-5cBs5mSldsO5_twF1uAWvMvjTx4wuT5vO3WZTkSsQFoRqH835p9G19IK8wwEr8LwICW5T75Gry5lWvvaRk47spD0TaKsUwAaDO7jLG-pbs7-yE76YzgeTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
بختیاری زاده، سرمربی استقلال:
صالح حردانی و وساطت دیگران؟ این جلسه برای بازی با پیکان است و قبلا در موردش حرف زدم. تنها چیزی که روی آن متمرکز هستم پیکان است. همه بازیکنان برای من عزیز هستند اما نام استقلال برایم مهم تر است و اجازه بدهید روی بازی فردا تمرکز کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105983" target="_blank">📅 12:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105982">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72b7d3e3a6.mp4?token=dcmPxbcPOrzAbq11Bvwafo-VN9AzUCyrT35PUFjZTgRrcV6YQToRl3GhIc72v76If-7GIYmasZswqJXROaCJDGZD4DtHrwPUXwFwkPZ31bOQQ_tP2DAhAsZVtPcLWKmxQfRl4mKu1Trt2-Iuj4cwhsuGac-XxD6IvH2KBgFnAWX6g4dPKKKSvdF1xgZm9jjC6RiFk009mO91CpifagTg_zFEeBwClKU3dpmnuFqBfsfh-RQ26ccsyWjPipiYAl9c_-sBQb7LI0y0Kbz13Ml7PlRqwS25vHlF9ahKaVz696JRUgL3bvQQgiFhAgKbtC_H3iaDNdTtIH51YsOcVNLxFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72b7d3e3a6.mp4?token=dcmPxbcPOrzAbq11Bvwafo-VN9AzUCyrT35PUFjZTgRrcV6YQToRl3GhIc72v76If-7GIYmasZswqJXROaCJDGZD4DtHrwPUXwFwkPZ31bOQQ_tP2DAhAsZVtPcLWKmxQfRl4mKu1Trt2-Iuj4cwhsuGac-XxD6IvH2KBgFnAWX6g4dPKKKSvdF1xgZm9jjC6RiFk009mO91CpifagTg_zFEeBwClKU3dpmnuFqBfsfh-RQ26ccsyWjPipiYAl9c_-sBQb7LI0y0Kbz13Ml7PlRqwS25vHlF9ahKaVz696JRUgL3bvQQgiFhAgKbtC_H3iaDNdTtIH51YsOcVNLxFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
🇩🇪
🇪🇸
دیشب چهار هزار سکو برای هواداران ویارئال تو ورزشگاه دورتمند اختصاص داده بودن که خالی مونده بود. فقط ۳۹ نفر از ویارئال حضور داشتن که طرفداران دورتمند اونارو وسط خودشون جا دادن تا از تماشای بازی نهایت لذت رو ببرن و البته خیلی دوستانه تا آخر بازی کنار هم نشسته بودن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105982" target="_blank">📅 12:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105981">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d0af12019.mp4?token=Gntqr2F2jjqkC8MbH_Yf8G2Nu67o7O_FVrnpVfnj3_0wSTfRaMRQBtXLz69KQgYUW5qaRuUoOuekbLy8bO0Yt2KyUB53BAq1Ql7r4rr4KP2Y-dvmKTLctTca4G_NhYW3hLLs_IWjIYxI_wZpONyzzMa0Z69bKBVQ2jC-8-RRvwkk3yfroOaY-nvLbvL0B6FnCvjk8s1yhes6dlMOPCCxkmFUf_YDrfWgQBjZgZwjwcDwCCTpnYm9_qQoIAXPxuciB9KYvlXn9gMh4CVrOxFVrrETf7HgYr99TSAy-cu5ZKFi-oYOZvCttgdhLEfkbzGKQTFHty8TfXYvW2imLWUq0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d0af12019.mp4?token=Gntqr2F2jjqkC8MbH_Yf8G2Nu67o7O_FVrnpVfnj3_0wSTfRaMRQBtXLz69KQgYUW5qaRuUoOuekbLy8bO0Yt2KyUB53BAq1Ql7r4rr4KP2Y-dvmKTLctTca4G_NhYW3hLLs_IWjIYxI_wZpONyzzMa0Z69bKBVQ2jC-8-RRvwkk3yfroOaY-nvLbvL0B6FnCvjk8s1yhes6dlMOPCCxkmFUf_YDrfWgQBjZgZwjwcDwCCTpnYm9_qQoIAXPxuciB9KYvlXn9gMh4CVrOxFVrrETf7HgYr99TSAy-cu5ZKFi-oYOZvCttgdhLEfkbzGKQTFHty8TfXYvW2imLWUq0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🔴
یادته آن شب ماله‌کشیدی؟ شاید اگر آن شب با خداداد برخورد می‌کردی امروز می‌توانستی پاسخ پسرت را بدهی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105981" target="_blank">📅 11:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105980">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎙
🇪🇺
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نظر هالند درباره اولین بازی ایوب‌بوعدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105980" target="_blank">📅 11:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105976">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzaDtV-DnlkZrVzo_fovfsVUR4OHLlX8MACrucV5A_G0QPk4C_4qwGPjFPQmz-wSod-W0Ives7vLInLKMM3Hc5uEWKn2_IGLloJiOVKhYGsJzT6ZsYYIoF3wIaCdROBzd1TmV40bzafGh_6t-NeUkuZwmyQQY2KcWg6L2ZggfYbL5vvHIu1A2d8qVDclXxzCaBsewMHreGrRDYaqa0O3gMTwP-51HkHkYJTsfuQRZjTGHh0QTK0r4KEjPR8pPTanlPgTlKYPel025uNVzox6w6B7GPbV5Qh9WJ5a1m_07YSbj2jjB2TWqfR-qoFhFFCr2JeStJN55rCJbDqYjgw5VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tPOn-GOZxx6BYzzsp_k7BrU0CQ4G7ERqSs9NiOL8z2nwDzuF_wvZSAazH9-EMaW63faGaxMP9roCv-jRn_OnN70zViUxMkNxQgs75xZNL_tJ6F7Eguzp5wRbD0e696hV9OgaFXI60hEceVeAZuCLSUn58KJ7lwoUQIdnQGwRoBirxlKa5n9f9xLVhlqjnzFKWXfajdBXHNLnaq5_0raIqJfs45NoTfyK8KB25gJhIjDmQylT_x14HnSN6AA2BWABKb3hI8H9woAotgY2dU9PxmyUrBWVpmi_Hxk1MSA_0QrUub6PtY0X4wzpEnJQyNR6GU3XDiSC-cun7TV_oo38qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S-R4ENLxYdd1dcofDGfGN3CcOhtjbdPIQYlzm4Osfj-RvG8fH9gYppHDhJeiGl8gregBRwwp48nR7szX2A0lPM_34KdUPGhbzAO3seRtNX9nj-yusZFF0H2lTgrFQbnc3s2MZhKCcGtQBK7c7Y3oAK9FJAtUdPPw0GLl_dEqOi50PlrWYHh_4D8cw9_AacMFNt9Gqwh2wpyqXcFHmDSigB4zrrGLJ9R2AdWfr9GWPUj_TbvlNqwZ0yD6vJpbuUDJuUkluhWBjO8lKv-teOpruiojTTfHpnBtcGQ6U-cmVO84X_VAlJ51YsVGIHIm2Kfve62hCzD66cp9nlLdNHbAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUPdWcEsqZ78_42BokBn_rc2LlAgqr-UyF8IGY2fuuv09zCQlm2Sh0rrb31tg4nv94wB5jUM0N3CgCcuThGDztL1umvNqPPbNzDUZACDbT_wOnGQqFz_K6AMVGvsIUoQQBevuMpw1Pfe_5f2b4mzPAj_Tdhr0ScCsTYXYTa22-DVernpJskpLXVWpDH2fPrjFJQPxXMjcM_xUhXfwxW1wtQyv-k2gPkgL43mB2tjsUXRLQ-H5XqmbQmhC2nLOrnd4at23YKHmNWyU0ECVJmuZWtgthe94TJJf4jeX_S5dIcwP4CbsD0LzGdjQ3-mdohVYuoAoIXK-sSUAsm9rDnt6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
✔️
🇮🇷
تمیز کردن سکوهای شهرقدس توسط دو بانوی بافرهنگ پرسپولیسی پس از بازی با ذوب‌آهن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105976" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105975">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5rvpErIHOJEnSN3OzppyGJuTvcSWuaRSWjXrehwk8aEj_vYKl4TsqRAbqf18LqcaaH18Vz-Et-B3McYgzQFDoYdlXCicWYleI-maua3XPNzT71vkmz_lUQBDWCQHTKy11TKwUy2RJ4X1X2O9AE82TQs-LDSR2Ar61cZqoFdJfEvCKJmovTIQpZGGJM-IVEcG72EV0ztQjbZ9VVtmN4IF0vQUidXtX15YMR2gt1WGh1UZXIYKTT0xRvYbs34DlAMhBWjN1KYQZcnDAiZpkNOJCc2y8ACF-0kpn5DIIX0P_FN7a4TD2iWGPVQleGx2vgHJfKs6IIKQZZ9BYqe_qdoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
تصویر جدید مهدی‌قایدی و خانوادش؛ عکس زنشو هم سانسور می‌کنه تا مثل قبلی بگا نره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105975" target="_blank">📅 10:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105974">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d195a639.mp4?token=gRZgHRJ3eXafP4xzPmDqyBV_-qMVlAKUis3b9y92sa28BDGcA6ugFNbZ245borYLq26DMd0gYS1Dwp1sx59YotrzxlsMavLjBkKuPACIc264LvCqm2TIZGmKOYPpjVhEcnRENGPd_CKCuSQdkf2JoMwusZPlT7OEDgCkotys-ehVbpJAjjX04sw5qTuVYGXAnuts5KEfOO0m-AjszjHGwEkSnwFRXuoJqGmoJClK76gLIcMDRMHBgpFjMbF4HlNt5h_O1wp-Xnm2mawq_TODVNysZtiFa-Px3wmhvzhy2aX9XA2VzC7bfhPSHKiYEYNi_UH2XHLIOhURIV1JyiKf9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d195a639.mp4?token=gRZgHRJ3eXafP4xzPmDqyBV_-qMVlAKUis3b9y92sa28BDGcA6ugFNbZ245borYLq26DMd0gYS1Dwp1sx59YotrzxlsMavLjBkKuPACIc264LvCqm2TIZGmKOYPpjVhEcnRENGPd_CKCuSQdkf2JoMwusZPlT7OEDgCkotys-ehVbpJAjjX04sw5qTuVYGXAnuts5KEfOO0m-AjszjHGwEkSnwFRXuoJqGmoJClK76gLIcMDRMHBgpFjMbF4HlNt5h_O1wp-Xnm2mawq_TODVNysZtiFa-Px3wmhvzhy2aX9XA2VzC7bfhPSHKiYEYNi_UH2XHLIOhURIV1JyiKf9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان خداداد عزیزی و عالیشاه با صدای علی دایی
😂
‼️
🚫
حاوی الفاظ نامناسب.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105974" target="_blank">📅 10:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105973">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32b4f4b4bf.mp4?token=Mxada3QFpM6Hph9Akrp1WWFQJjdIKl6lYPfQAptWgtYaoafht_7C0iVB82d731VcCF29I7v33tmZbIvFh-TMwJGggb_SpWhVZ5u2JuE5PeFxTdZ-p3jNTmPCwhmltNxMuxIER2kEVqKJS1ZTzl5U8lrzVkc1D9SoyVJyR58CoNK9pEeL9YYIM1oM65wPXRiVZwtH7u17W_tB0CQd8fjtW-jFqvUimXdCOSOwLr0dHmGiTpJBGagSjZPTFCIeufZKwlXVkMSCrTgL4jMrdAiElPiybOt9PA8K19CE5gnJlx2W__icxtO5as1Bo__2p-KYlnNdmZivhQwtrQTgYNPMcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32b4f4b4bf.mp4?token=Mxada3QFpM6Hph9Akrp1WWFQJjdIKl6lYPfQAptWgtYaoafht_7C0iVB82d731VcCF29I7v33tmZbIvFh-TMwJGggb_SpWhVZ5u2JuE5PeFxTdZ-p3jNTmPCwhmltNxMuxIER2kEVqKJS1ZTzl5U8lrzVkc1D9SoyVJyR58CoNK9pEeL9YYIM1oM65wPXRiVZwtH7u17W_tB0CQd8fjtW-jFqvUimXdCOSOwLr0dHmGiTpJBGagSjZPTFCIeufZKwlXVkMSCrTgL4jMrdAiElPiybOt9PA8K19CE5gnJlx2W__icxtO5as1Bo__2p-KYlnNdmZivhQwtrQTgYNPMcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
🇪🇸
شعر مایکل ریچاردز در وصف امباپه پس از درخشش در بازی دیشب مقابل اینتر
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105973" target="_blank">📅 10:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105972">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf52ab1a36.mp4?token=dWHux1f34gEkg638O-FD2zrank3mTOGIf3vuTB1LuEviKTecrfLcZnmSfxUgOxkyPvG4sYCAbpCD0qJfKHqYxmdFa3gYXAVe2fNs_IuqlUKPd7vdQwhQlZAUUOCbZP6qrNknL7tu0f15sNc-aMjMhuxm4DlNRMDVc2SsYOxL9_Xc2ou_0NRXzsy2_0u-gsdtvpW1WUzayMXm6DDBpSYyFfSQA5dGfYRIxAKGIZv-zwEByi0j2iq7Tk8PD0gFL4gPJ6K4ikueSsQgcRT66-PbZnzGH1-cM9Tvj9uHcMJLlOCQ8mU0d6EsSSZEvpibHA39Mc_GV1RGIRJsOddaxk-8yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf52ab1a36.mp4?token=dWHux1f34gEkg638O-FD2zrank3mTOGIf3vuTB1LuEviKTecrfLcZnmSfxUgOxkyPvG4sYCAbpCD0qJfKHqYxmdFa3gYXAVe2fNs_IuqlUKPd7vdQwhQlZAUUOCbZP6qrNknL7tu0f15sNc-aMjMhuxm4DlNRMDVc2SsYOxL9_Xc2ou_0NRXzsy2_0u-gsdtvpW1WUzayMXm6DDBpSYyFfSQA5dGfYRIxAKGIZv-zwEByi0j2iq7Tk8PD0gFL4gPJ6K4ikueSsQgcRT66-PbZnzGH1-cM9Tvj9uHcMJLlOCQ8mU0d6EsSSZEvpibHA39Mc_GV1RGIRJsOddaxk-8yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
نادر محمدی دیشب برای سومین بار با اوت دستی تو روسیه پاس‌گل داد و حالا اکثر رسانه‌های ورزشی جهان کرک و پرشون ریخته و گفتن که این بازیکن قشنگ به سیستم آرتتا تو آرسنال میخوره
😂
😂
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105972" target="_blank">📅 09:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105971">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d2267479.mp4?token=VC2nw6_mpOW8C0smenGGq38k1IuhF09_6elSQQWsm-MToB3hC2-XLDXcf7Kwzmfdy-Oi8r2rRftIKMmT2TpgrMfPtpIIrtq76E23QXinnXNL8MDRSEUyCD6dVRitO6ZvC0aQyOlpiMSAbi1GEnlRrk2cl0GvgjSHQSiTlAJu7l6qBbEEKIiI0LDznN6T1PnALTUC0ye8IIohbXhGIOT8wP7SVgBvfkBrmMgxZ6-pZqQwcikOVXLBw2A_UYApWwlteOmwbkpLyPTbcHghnU2HzsFctaG0tQYQgTdyM1On8cj4vNNftjAEEoapHYtEUClYTn3S0QOFCauKQqqu1ISaeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d2267479.mp4?token=VC2nw6_mpOW8C0smenGGq38k1IuhF09_6elSQQWsm-MToB3hC2-XLDXcf7Kwzmfdy-Oi8r2rRftIKMmT2TpgrMfPtpIIrtq76E23QXinnXNL8MDRSEUyCD6dVRitO6ZvC0aQyOlpiMSAbi1GEnlRrk2cl0GvgjSHQSiTlAJu7l6qBbEEKIiI0LDznN6T1PnALTUC0ye8IIohbXhGIOT8wP7SVgBvfkBrmMgxZ6-pZqQwcikOVXLBw2A_UYApWwlteOmwbkpLyPTbcHghnU2HzsFctaG0tQYQgTdyM1On8cj4vNNftjAEEoapHYtEUClYTn3S0QOFCauKQqqu1ISaeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇺
🇪🇸
اینجا لیگ قهرمانانه رفیق! قلمروی پادشاهی رئال مادرید.
🔥
☠️
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105971" target="_blank">📅 09:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105970">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15481b67bd.mp4?token=UvHbxnXDCTjXOkjXC-Dg25v9JCfRQt5ESrY03x6j5iTTpg6jtH-iJDxXT4jTqwolWE_OZDd59aeN_NVpXFP-uwXFijTHQVWHjADvlMvAzw9WqyhecUUbxigBn_Ezfz5TjHAcweWBE8XMrEEmYujV5cfQ1n2Xra6C9SWoxN70xTUyl_de58NUMI6LAxAwPWWXdR4hs_hISyw3TIGIYqSk5jeiYeNuTGcTyrDkqYI4EXZC0IXqZTV5CB8RijDL9oI_mgXZ1Vh3OxvMjl6VyxatyvsKL6Wo0qeWWrJeNGV-5Z5lZhYQ_P2cAJmaAO7TATWUmQlkQfYEKDdL3PT5U7U3-nbr8FbL3VV0lkPBDwD-4D4QuVgVOciJUDkVLCiJM2T0O4eMvc1DZGK345wcqu2lEZEbmnSwF9Ws2CPb4B_PQgEy2ljy9BomRx7AhHFCCyIMUXuXiZj5WCWOQCWgPD6ypUnC_de40-6TjZfSROX2XXD9HxA9TNEq5VW4H-pIPdLsRVzmlmD4LuoLNlrmoCTY_GvKIdt38OphqSgaQb6S6CWOz2eaCw_UP7nMFNWEEaagL0BJXvkJZA3wVBcjdo_7Asbv_7jJvmgV9fe3CRiDPbDZlJXSX4Q8QRCi0vaZXMlNv_H445amd8HcZhVAKrw8I-lpLZUz6z7k-klkWdoVtUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15481b67bd.mp4?token=UvHbxnXDCTjXOkjXC-Dg25v9JCfRQt5ESrY03x6j5iTTpg6jtH-iJDxXT4jTqwolWE_OZDd59aeN_NVpXFP-uwXFijTHQVWHjADvlMvAzw9WqyhecUUbxigBn_Ezfz5TjHAcweWBE8XMrEEmYujV5cfQ1n2Xra6C9SWoxN70xTUyl_de58NUMI6LAxAwPWWXdR4hs_hISyw3TIGIYqSk5jeiYeNuTGcTyrDkqYI4EXZC0IXqZTV5CB8RijDL9oI_mgXZ1Vh3OxvMjl6VyxatyvsKL6Wo0qeWWrJeNGV-5Z5lZhYQ_P2cAJmaAO7TATWUmQlkQfYEKDdL3PT5U7U3-nbr8FbL3VV0lkPBDwD-4D4QuVgVOciJUDkVLCiJM2T0O4eMvc1DZGK345wcqu2lEZEbmnSwF9Ws2CPb4B_PQgEy2ljy9BomRx7AhHFCCyIMUXuXiZj5WCWOQCWgPD6ypUnC_de40-6TjZfSROX2XXD9HxA9TNEq5VW4H-pIPdLsRVzmlmD4LuoLNlrmoCTY_GvKIdt38OphqSgaQb6S6CWOz2eaCw_UP7nMFNWEEaagL0BJXvkJZA3wVBcjdo_7Asbv_7jJvmgV9fe3CRiDPbDZlJXSX4Q8QRCi0vaZXMlNv_H445amd8HcZhVAKrw8I-lpLZUz6z7k-klkWdoVtUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❗️
🇮🇷
باشگاه پرسپولیس دیشب طی یه حرکت سوپر و عجیب، تمامی فحاشی‌های اخیر خداداد عزیزی رو در قالب یک ویدئو تو لایو باشگاه پخش کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105970" target="_blank">📅 09:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105969">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0U8Cn28Wm4mCnYQ_JYK5_VbECtVlz0P1_qV07u9yJqrp5z650IadL5ZCZsErwRiifhcRuF34Emqf2NMD1Szqb6WmwYeLeIqaK2e8IhqzpcG_Xp2K-BJ8Seep6_XofE44QdPy4aEh8QVcgPZwyHwUaHDrQWdZZDKB9BztNN-vWUj65qv1G-3pxgZ9D4w1gV8XkmGTv1pV6xbpzi0Uwlt355tIFAQVvE5dhtO6pAyNK3rp3xuM-EELgACH9BXLcMBONCOHHvdOJsTp3dvYGcY6ccI_jA2v-4-ICRiZmxof8ZzbwZbixG13f99w3VU2QW61d4LTI73-R-duMEjtAoqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🇪🇸
مقایسه اسکواد دوره اول رئال‌مادرید تحت هدایت ژوزه‌مورینیو و ترکیب‌فعلی در اختیارش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105969" target="_blank">📅 09:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105968">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105968" target="_blank">📅 01:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105967">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYqYepU2n98kMU46HxqqguFnUEU0WjoV4l36dkfVzAWmUZMHUBHEl-l4edImunBZ1FjCn4bI1x_p5wRzlW8kHhKMkRaAm_YSx1CqEqVPOGZPWlt244u5m7jeKY880h8-sZpN6iUqNUWQXhpG2dwqXtAr9TBC7Flgt-zF-1JmUkuXAAxmtGbER3num0hcH8W_rwA4t63M_11QrzMQq1lJaIv1elPUbWG7XFMLs603sREcKlVpnDW3eUJ44o4kp-qwKT8UedyN-jcryud_7MChnitl-AVlCWL45q8uAcNoBpUYErF5Gd0MEuSJ5oEKXCSVMT8wZaYnGx67iCVOVyn8Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105967" target="_blank">📅 01:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105966">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105966" target="_blank">📅 01:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105965">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خب دیگه بگیرید بخوابید. تا وقتی بی‌بی دست به کار نشه این موشک زدنا اسمش ترقه بازیه
🚬
🚬
🚬
🚬
🚬
🚬
🚬
🚬
🚬
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105965" target="_blank">📅 01:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105964">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=UooiTrV5aHL9eskj8_v1LL--PhGlANeQErnJXQQWQ_F6K3dMQ3HEQ9VHREDdTMdADquP3F9JoDYvEYm3PZbbL2qTzFLS-MAoMeXe5nYv2o01qIXXyKF3Jt45Ew2Y_IYVebQgLjQRN4UttcsoAIWTPr1042MLVD2D7OBIkErnlQ3oiVC-bJQOsNq4rh4n8Vbwmo_o9Y6V-TtH4AlvE2ijfKL3-WjBDkDdUpda1rsOC4M3P0a_cdvrvduwEipv4v4XwbHxyfhJ4Stgl3k3p3Qjc-dGlsMd5m-grOqIFd4Ei5pGs5ccrmxzhZtlGRnBT9h2X3Fmmeg2YdGIYDRZJcCiRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=UooiTrV5aHL9eskj8_v1LL--PhGlANeQErnJXQQWQ_F6K3dMQ3HEQ9VHREDdTMdADquP3F9JoDYvEYm3PZbbL2qTzFLS-MAoMeXe5nYv2o01qIXXyKF3Jt45Ew2Y_IYVebQgLjQRN4UttcsoAIWTPr1042MLVD2D7OBIkErnlQ3oiVC-bJQOsNq4rh4n8Vbwmo_o9Y6V-TtH4AlvE2ijfKL3-WjBDkDdUpda1rsOC4M3P0a_cdvrvduwEipv4v4XwbHxyfhJ4Stgl3k3p3Qjc-dGlsMd5m-grOqIFd4Ei5pGs5ccrmxzhZtlGRnBT9h2X3Fmmeg2YdGIYDRZJcCiRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
لحظه باز شدن موشک با کلاهک خوشه ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105964" target="_blank">📅 01:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105963">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
⭕️
⭕️
⭕️
یک منبع ایرانی نزدیک به سپاه جمهوری اسلامی: امشب از موشک‌های خیبرشکن استفاده کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105963" target="_blank">📅 01:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105962">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c52f8bf8.mp4?token=LBL4L1RHuwKs5SUID3p3mrqf8c-rDcMIZjuQ0mr_VNMNaitu-HP-POMDyh86vq3qAp_kIMr7ktrGuoIOzbNWozmDC1zcuZ8k9vDxvxAGyZDv6U9wbSXdeJ6afpytBhQ66v_b0H0zjPi8MB7S0SEUGYr0GrKBdexNOg_90zyvyH8ibwq58MsXskw7Y3_bGhQ0xtBrqHY5FZR7n_dp97YuAthUmHTI31kzikaaSujyYZmOEE6GfpM5b8L2YKfs4h-kmlMDNv5RdcLJWQKrGNkLAzm1krP0O9M2PjFnlK_GVeWTgNgSW3bobYEOsXqQ7S2cPb5eV6CngdeQtqrI81h3ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c52f8bf8.mp4?token=LBL4L1RHuwKs5SUID3p3mrqf8c-rDcMIZjuQ0mr_VNMNaitu-HP-POMDyh86vq3qAp_kIMr7ktrGuoIOzbNWozmDC1zcuZ8k9vDxvxAGyZDv6U9wbSXdeJ6afpytBhQ66v_b0H0zjPi8MB7S0SEUGYr0GrKBdexNOg_90zyvyH8ibwq58MsXskw7Y3_bGhQ0xtBrqHY5FZR7n_dp97YuAthUmHTI31kzikaaSujyYZmOEE6GfpM5b8L2YKfs4h-kmlMDNv5RdcLJWQKrGNkLAzm1krP0O9M2PjFnlK_GVeWTgNgSW3bobYEOsXqQ7S2cPb5eV6CngdeQtqrI81h3ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
تصاویر منتسب به حملات دقایقی قبل سپاه به مناطقی از اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105962" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105961">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
حداقل ۲۰ موشک به سمت اردن شلیک شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105961" target="_blank">📅 01:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105960">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXB6m2hnuFmfnUatvwHm6Go15NHTbzt77qN-yB8Cwl-P9w_uKIi7nLpd4BGuqCSHHN4k4gZXCv8NOM8RytViFBnChf1u3gidDGaZZFQtXGrPqEffd04nwaEYDshHnUNrMONT2VG_5YUNiWi0W8zlxHNuz52Ar0h21nP84T8jLhjyUwUhSRRQLuPoSwY0jjIOEExWe0IeuTKMrw717Tb5wJIgJ8fkOTfs8xO5cipYkCW89-FKGzQ9zoQPVcueWE4OZPaJ-nilAtQl-XzBqOXytW_ow0WbCxnC4cqaifAH8sID808OeN-FOd3BG4c_IQTjBamOby8OwitCVUWnQz-KXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
حداقل ۲۰ موشک به سمت اردن شلیک شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105960" target="_blank">📅 01:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105959">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b19aa63524.mp4?token=sBcsgfIxDxEHhGXpaTgN3HyD09tJGWY6J5WwJ5gjJQfGB0MEwdTId83DbzZ45USsb8lR7Fd-7UzghuXox-8uPVyifk8dvwksK60tgmfJzJRIgtyVNyoPqWNWTsD5ZGgfC9OZThxrSObuek942lpuxeI0MDdIzSdROApOMMTuquAIbfIZv3OPgn1SK4IvbrqnjDL2u0mGcZwBXQ_EuNrbsYdtb5zII8rSwZPDtZ6ALlvBuzGvelo3FbP7cAktcU5cHBryB8kwzUZseok_sdn2WZelOpU6GZxO5KWopFC58NHJ4LcZJg9imMgf4St1orNgpCZ4pUQSJ7sURQ4iWEap-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b19aa63524.mp4?token=sBcsgfIxDxEHhGXpaTgN3HyD09tJGWY6J5WwJ5gjJQfGB0MEwdTId83DbzZ45USsb8lR7Fd-7UzghuXox-8uPVyifk8dvwksK60tgmfJzJRIgtyVNyoPqWNWTsD5ZGgfC9OZThxrSObuek942lpuxeI0MDdIzSdROApOMMTuquAIbfIZv3OPgn1SK4IvbrqnjDL2u0mGcZwBXQ_EuNrbsYdtb5zII8rSwZPDtZ6ALlvBuzGvelo3FbP7cAktcU5cHBryB8kwzUZseok_sdn2WZelOpU6GZxO5KWopFC58NHJ4LcZJg9imMgf4St1orNgpCZ4pUQSJ7sURQ4iWEap-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
⭕️
گویا یه دونه موشک به پایگاه آمریکا تو اردن خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105959" target="_blank">📅 01:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105958">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شلیک مداوم موشک‌ از مناطق مختلف ایران به سوی کشورهای عربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105958" target="_blank">📅 01:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105957">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🏆
ژوزه مورینیو: برنده توپ‌طلا؟ بنظرم کسی که یک فصل هیچ‌جامی نگرفته هم میتونه برنده بشه. نظرم بدون شک امباپه هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105957" target="_blank">📅 01:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105956">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d6b878d2e.mp4?token=oVgfbiWXKH_anjTsHsTURhZa1J_Qp-p0E1WMtQzkGWqxI3qoU3NLKRlBTrA5amXPMKA9CLB3825zPxcq6iUuaSJs2omTyvUuodVTfegAvRXGA94_bIGxqBUb-Py7r6lHCpgN47lXSS8ls4Oj93T7XezcuwSVGZKCLkmwOv6gdoBUYDtilcG2PbkfjHzXD1hW6jjJms8nhYbKj36Tae5wz4l6CbgbvRWni90PrZl_hoq6whHRFRV8AL__VP_SxgKz4FU8fbQ1gDItxnKrwePdOVEwEAIJpeIdS8NnFgpmIMd9L8oXDmn2vguKKFKO3drTAws6scGNO-CVIpaek39NUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d6b878d2e.mp4?token=oVgfbiWXKH_anjTsHsTURhZa1J_Qp-p0E1WMtQzkGWqxI3qoU3NLKRlBTrA5amXPMKA9CLB3825zPxcq6iUuaSJs2omTyvUuodVTfegAvRXGA94_bIGxqBUb-Py7r6lHCpgN47lXSS8ls4Oj93T7XezcuwSVGZKCLkmwOv6gdoBUYDtilcG2PbkfjHzXD1hW6jjJms8nhYbKj36Tae5wz4l6CbgbvRWni90PrZl_hoq6whHRFRV8AL__VP_SxgKz4FU8fbQ1gDItxnKrwePdOVEwEAIJpeIdS8NnFgpmIMd9L8oXDmn2vguKKFKO3drTAws6scGNO-CVIpaek39NUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شلیک مداوم موشک‌ از مناطق مختلف ایران
به سوی کشورهای عربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105956" target="_blank">📅 01:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105955">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
⭕️
لحظاتی از شلیک موشک‌های ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105955" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105954">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721dcb7629.mp4?token=ZVvq_Nme4gTbdX9x4aSdcqYT97wj00Q7eqHiewOUQNKW9F60RSIF2b1OBSu1eaNEaXhzB6kpVyhdOB6x85aazoCa98e0TdGL4_O3Iz_3whCOULXc7uzeGySAe0zOyxWcn4EfBRxd4ouiNtuXAe7X5ZoCNmBJKrQ7qxRGbFgWGxKOnV0C_WqYJHy--SkQdV0JQKVCGll8SsHaJf87nbaqPxGeTJvAp3OIR8q3tkz9k5AfIwaaBdyI0Vj6MNxpGbYLL3U0MCLYkyLBXkLQtRYWqmiN7LJuNpUC1ScPz7ohuGkfU0vlatQiIB9E2q9beIOdRWMGJ7j6XPtzB1_Q3ashnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721dcb7629.mp4?token=ZVvq_Nme4gTbdX9x4aSdcqYT97wj00Q7eqHiewOUQNKW9F60RSIF2b1OBSu1eaNEaXhzB6kpVyhdOB6x85aazoCa98e0TdGL4_O3Iz_3whCOULXc7uzeGySAe0zOyxWcn4EfBRxd4ouiNtuXAe7X5ZoCNmBJKrQ7qxRGbFgWGxKOnV0C_WqYJHy--SkQdV0JQKVCGll8SsHaJf87nbaqPxGeTJvAp3OIR8q3tkz9k5AfIwaaBdyI0Vj6MNxpGbYLL3U0MCLYkyLBXkLQtRYWqmiN7LJuNpUC1ScPz7ohuGkfU0vlatQiIB9E2q9beIOdRWMGJ7j6XPtzB1_Q3ashnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
لحظاتی از شلیک موشک‌های ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105954" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105953">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
📰
صداوسیما: دقایقی‌پیش ارتش آمریکا به یک شناور تجاری در نزدیکی جاسک حمله کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105953" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105952">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSgICVKToHSbQrAYSPoTxBEMxh3Q5PgskxJ4LTkwdSeN3brdONqnDCH8GAcct9e0yvEuBNke355nBaynIeDKgC2OvQawg0lMowYJJ-TUZty7NN5JAEA5BogSwIH5_HHozYWYLGD13bRRbj2k9DG1DDi-_FThEDrVJktqbDBi28HB4qWTt9Xlag-1gN2aHHKp319yP-IfR9dGlLQf7yuEVw3fqNwKqYbZhQi5opAEz1Wh9KeYiYgyGrrVRxxw_U0HbS-kDEPSe0fGejabrO3fOXdEZS4lfBIKrUWn3p28VGJNoqDCIksHmLNAgXNos5nJNFaKyWe5f5jjbgdhgpe4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موشک‌های سپاه به سوی بحرین و کویت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105952" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105951">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pO9t9jPtBQlhpK6breBoWc9U_l3R0WMVqgV4cRpTUJTPywZ0lRwO1FHzomJCMVR0D1zKtLW3drS6c-gm6eo20w_CoxIsocoGagC7Z0qBd5cfYBEQ7C4Q4ZGMizD0NDBu2tS4DH_OYwbpywepTijIto0rcIzELHihSY0-sAvlWvYlSDEXngVyHDlkDIbUeTmcgXcHcL1r31Sm5t6YaYpqUPX9qhJv_uFXy9_thAjqD54qkBnZoNtWZ6Wy357biyybeoW4MfZqeoI86dqrY2g0E3XSlJheny2yLakv0E6ZACEwQsOLblyeInup1VenRvfWzO23ljwZIWEE2k4hg5N2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارش‌ها از شلیک موشک از مناطق مرکزی ایران به سوی اهدافی در خلیج‌فارس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105951" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105950">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گزارش‌ها از شلیک موشک از مناطق مرکزی ایران به سوی اهدافی در خلیج‌فارس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105950" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105949">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pfhv1Py-LNEAq2rh7EqGM_2YDoZhmM6IszXu1y8JrDx4xk1gSwS2tKtBvSxG_7ULYownNq5BPxfHW4K-qLodZt5-66vyStWg6hjTOgHAKDrDKTwzXqwWblenJqi4ais1mCGE8bKIEe-tHJlwodjCzAzhsockYry1saK28Y2_FtfB9r5vS8Wls7iBkGZ9eoTwXbfc_J2WEhQYUPn5KtT6-ZS-QRSXWvLrNCHkg9oeoaAm1Mm2FliU251ek_Rv7SOygjOUy4P33cy7ssDIb7C7xcjrMSDES_E3ltnFPg7wzLawCJDiv1AI1kBBhSqmH2iHrpFyuBT7BaEe_Rv3-XZXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⏸
🇮🇹
🇪🇸
هایلایت بازی جذاب و تماشایی رئال مادرید مقابل اینتر با گزارش ابوالفضل عامری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105949" target="_blank">📅 00:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105948">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXHlPHGcGY5XMm8GK0f8i38tJCZbmJlcSZ0hULWTNhjAhVzd0febTNvVTX9VXvOnntHt-11ODDdvCsXvurOrdnhzW8yxN4wxmwXld5gqd1niEy5IZWOULXCPbGpdANjjOoZ1MdkAAjmCTBDBGWrz3UmMiyYi0WTNkyt_o-x8YMvNf6xAQXtPb13qDtDhxHTR0fULXzgXKHUwArh_FgLPtSeZ7kIzvIaF-hqpvIG--tU8w6ou7d4WSyCTdl4SoKBNXtCMsqvPso3iXl3b9GJ3gkWDLSEtomVdDYVMlEQhpYDMMaarv4lcnLLDM8lijt1Gm8jdXt-1U3SzzreQEMLFSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🇪🇺
📊
ارلینگ‌هالند در لیگ‌قهرمانان اروپا:
‏59 بازی
؛
‏59 گل.
👀
🐐
اسطوره، لیونل مسی، برای رسیدن به 60 گل در لیگ قهرمانان اروپا به 80 مسابقه نیاز داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105948" target="_blank">📅 00:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105947">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
⏸
🇮🇹
🇪🇸
هایلایت بازی جذاب و تماشایی رئال مادرید مقابل اینتر با گزارش ابوالفضل عامری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105947" target="_blank">📅 00:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105946">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYgq7fQkwEpKIPxuzaSrhxnlFGcBeE3ig3tebW2OwB9xFE0S4mnRAXv9sIh50taH_Wud3Y9JLphI5kVdclqHx9Q0hA2qujWlo2Nif0r7nMb5pY__SC2CV8sTiWhIdiH0hSyHwscvV-IIrEEvXoZlk9TFWWJ9ZxyUQFM28VMUoB0MvkMJDflc5mGwlNlDd5aUYOo90Va0Wr01XkpxnzY_VHY40ARq_JLLZJulRyhV5ubc8Ur0iuVpEpXgeEGXS9FMVDd4Tz5qlVf90ewoUlStWoBDXsSrxXvqKvqOPIbQ-tI_FhNj1dIHgX1_c9xJLTVVeqK9b2plRKhFwuikzwFK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇮🇹
🇪🇸
والورده بهترین بازیکن دیدار اینتر و رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105946" target="_blank">📅 00:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105945">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ieFs2D6x0HDN0La0jvTMxWy4eQDL3siglezVb6HjgjTikH3hCTkV9wHCEZYUAUwfBL0aZI82fCqGkIGe8bNYeaTa8lti5AdHMGb8CfOW01vSwvl3UPLJgepzfd3end1gI1BLD8Gb9hxnweXO4HFP7f6jSV8y-o6rjKgxMPg3FUFmcfPc6vrWIOPD7AadF4sdk2mAwUv1EqJbmhuZqO5CV9eMy8K44rrQM5AiqraQ592kuTNnbNOQDQL0TRs-FEjRlFN2Ju7HFoKqXygpx77BaPnUdmBUb39Gk3GbCMZhTqrmn2OJWKRbX6-5MXVv4xlv5dWUC4UHRrSqmTov5Qsncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
نتایج بازی‌های شب‌اول لیگ‌قهرمانان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105945" target="_blank">📅 00:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105944">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/275f4f92c8.mp4?token=Nh1dYjtcsvw-gmnuacGOpUbogWq8Ta2GC_GwqyjlMAGLSxpL0ggJIy9XI7Ji4hrYFrbcFh6Q8rsDOCiy8Kkf1kOB53DcnG4cwFGsDSiJJ9_NGPsohWqbPF0ns2nlHwiQ8HKtArxWBCPhxUWvQ7NnXYJQhm2m8cYHBvJySTbAndF1TyU9VsI49wkVP3WNgb7V5L8tod1KyQqftliWbigrKGhsaZWg1oBATF00qSmGb4Dcq5LG89pY2yYqE15ll2MSqzpoK5xB494qJPY-mJLzi9DyHo9JDdAj39u4aH0uP0GYXxN_JS5f5jiJo9CC5aTB8aDHzWCvMZpSMsEk8asSSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/275f4f92c8.mp4?token=Nh1dYjtcsvw-gmnuacGOpUbogWq8Ta2GC_GwqyjlMAGLSxpL0ggJIy9XI7Ji4hrYFrbcFh6Q8rsDOCiy8Kkf1kOB53DcnG4cwFGsDSiJJ9_NGPsohWqbPF0ns2nlHwiQ8HKtArxWBCPhxUWvQ7NnXYJQhm2m8cYHBvJySTbAndF1TyU9VsI49wkVP3WNgb7V5L8tod1KyQqftliWbigrKGhsaZWg1oBATF00qSmGb4Dcq5LG89pY2yYqE15ll2MSqzpoK5xB494qJPY-mJLzi9DyHo9JDdAj39u4aH0uP0GYXxN_JS5f5jiJo9CC5aTB8aDHzWCvMZpSMsEk8asSSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم منچسترسیتی به پورتو توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105944" target="_blank">📅 00:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105943">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF6AhWJO11Pvob35f0RsaSInrJCF-k5xa305Nob15QVhQfypMPqtPdVe1yuyE4HWCIyP0krsW1XSvqIMkucN8M93opzfMaevlmZ-pVP70nPg_Ji7mvo4PYt5gXNOakYYnpyyNm7b5VNkcLflyN6PqUsmMAdkcH4QrlhBBJfu0H1c_hkGixfvjlnbfidP23gEFBKOAs77Uf_fRdIdR5tCcIW5xLEy4YgHAz7sgMCqhahDdbkST7BlbNSx8z2Mjk5n-KIWmhznq3Et4YuOsGaz4wPDJcpZD7F3Y4CxNDReaAmU_kZi96gIVrzvCP31yTpnNGRb9tjt4fPPcVe7enbFWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
هفته‌اول UCL؛ برتری سخت و نفس‌گیر کهکشانی‌ها در خانه؛ درخشش دروازه‌بانان و فرصت‌سوزی مهاجمان باعث رد و بدل شدن گل‌های کمتر شد!
🇮🇹
اینتر
😃
-
😀
رئال‌مادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105943" target="_blank">📅 00:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105942">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c99ae7fc.mp4?token=a-G7svvHvwa1H9GbyiFMFGyEIHPh12hWdn1GPP8nyyo-Rbwg2ZfMTYSL6kxTJSxYK9yJXlZUyDLzR5KL07mRXkk7KlGW5QtUVmjFsXlh81L4_iiMR_H9R-UjwBQTtuEJFejyla0_UANPsuPkBXVi3fWKZEOUjUWdnmqDujsHAi2l0dpivDM0U8Ml1Nza6UL5drqXfoSvxZY-SU4Jm7y3_O9I1b_3-a5KGRgWP4WUJWciEX3LQd5UOQjJRVk76Z3w3853VRrcEHtR63Lmz5QfJFaErXCz3sRrpgDfceC5E1t1V2E1167mo3HpFrgIgXHDVhTkjGoaLOnhZfcDGGVxvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c99ae7fc.mp4?token=a-G7svvHvwa1H9GbyiFMFGyEIHPh12hWdn1GPP8nyyo-Rbwg2ZfMTYSL6kxTJSxYK9yJXlZUyDLzR5KL07mRXkk7KlGW5QtUVmjFsXlh81L4_iiMR_H9R-UjwBQTtuEJFejyla0_UANPsuPkBXVi3fWKZEOUjUWdnmqDujsHAi2l0dpivDM0U8Ml1Nza6UL5drqXfoSvxZY-SU4Jm7y3_O9I1b_3-a5KGRgWP4WUJWciEX3LQd5UOQjJRVk76Z3w3853VRrcEHtR63Lmz5QfJFaErXCz3sRrpgDfceC5E1t1V2E1167mo3HpFrgIgXHDVhTkjGoaLOnhZfcDGGVxvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
گل اول اینتر به رئال مادرید توسط آگوستو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105942" target="_blank">📅 00:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105941">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رئال کیری بازی در بیاره مساویو میخوره</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105941" target="_blank">📅 00:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105940">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">لائوتاروووووووو</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105940" target="_blank">📅 00:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105939">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">لائوتاروووووووو</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105939" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105938">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اینتر یکی زددددددددددددددد</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105938" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105937">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گلگلگلگلگلللگگلاگا</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105937" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105936">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
سپاه پاسداران: تا لحظاتی دیگر تمامی بنادر بحرین و کویت هدف حملات قرار می‌گیرد. منتظر باشید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105936" target="_blank">📅 00:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105935">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رئال بازم نزدددددددد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105935" target="_blank">📅 23:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105934">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105934" target="_blank">📅 23:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105933">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گلر اینتر با اینکه کیری بازی در آورد ولی حداقل ۵ تا گل خریده برا تیمش</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105933" target="_blank">📅 23:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105932">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">امباپه بازم نزدددددد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105932" target="_blank">📅 23:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105931">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کورتوا نبود الان بازی چهارتا گل بیشتر داشت</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105931" target="_blank">📅 23:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105930">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utVoXwc3sY7DtXLb017mFpaCef1FahyZry7jaz3vI0SnCES_OwjaTP008foZXkZ3ZpSA6C8UVCK9-ljz6Kys_ijYjK6Dgt0kU8J_zTiW3rxR75HXkN2gwedVmy591FXE4s9LmcpI6vDZahcHNp9ogDUJOfBKuCc4NhZj4hM0ae94iVT6xJqxL309rggirA3akW_oxsJhLjGiMvRfwE6bErAz4ayK5m22LixL_qeH2I1KtaZ5ncHZzXISnxx2eqkO0taIO5Q9J6hu8X-vVgMSukc5D0ok2i5JmqOIzQXXEUjhLCZrmWQrSJjI7teu9DB0jV_6s0RaqT4cG4jU_p0lnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلینگهام جقییییی
😐
😐</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105930" target="_blank">📅 23:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105929">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بلینگهام جقییییی
😐
😐</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105929" target="_blank">📅 23:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105928">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">چه دروازه خالی نزدددددد
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105928" target="_blank">📅 23:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105927">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105927" target="_blank">📅 23:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105926">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105926" target="_blank">📅 23:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105925">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGYlS9vtvWxziz-ffFLUCra9pYCNlYiiuYhaeROg7sFiiwWhI_CWVd8o0Xp5YG2ze0l3BvMYZHCp0gNtUHIcrD3gSDUErz6GCO2PctPnT-FylIEwwyXGDKq5vXWzdQGn8GMjkNOUO1m7wRXMIVSmNzyuLDtoQQfxKXimZrnPwKHt5z676eqjLWsJlipn0MaZKU2M-DYxxekkiA6wBuamJi73WM35eV6VL9APr1bk4RQJsu64OeDZytjSZF0iDPOetL5tJSIcTeMz1PiLHRx20zNongkDFjTXMVF2VPDUyb-vZELA_cq6LzKCrERAEKpDZlnKSU-z943j4jjcWv4teg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
وضعیت نتایج تا دقیقه ۵۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105925" target="_blank">📅 23:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105924">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کورتوا خداااااسسسستتتتتت</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105924" target="_blank">📅 23:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105923">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/baae1563dc.mp4?token=POVV63KuFB_rRj0eZCdScYrScVkNwe9gpbgpsjup1L2TDPsqi-pRbVGjs7TcGTnRhWXyR0qb3Q3jMn9ezfWcMTOMKXYz-ZcJlonKd7o4p9H7vqsRC242jq1RdPhhAID3UVmJO_qyyIgGGj5X__TTSiQ9TYWRj8fWQK4LVz60PI7JQ7PxdaDUNQgMEPdklhkbIaHeoO11ynKNfs4g6sWxeajV5PsbxUNLeWuxOMvkwNyDbpeaiU-P1ej0XIGhQN_ktOEBjNUoW5RoUPs1ZwsLC51YIhdv_3ZOrhDWCSMbX3vMpJpC7Gb-WvMhxH4FjMnfs0O8FRObKVixQcIK8FcSkw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/baae1563dc.mp4?token=POVV63KuFB_rRj0eZCdScYrScVkNwe9gpbgpsjup1L2TDPsqi-pRbVGjs7TcGTnRhWXyR0qb3Q3jMn9ezfWcMTOMKXYz-ZcJlonKd7o4p9H7vqsRC242jq1RdPhhAID3UVmJO_qyyIgGGj5X__TTSiQ9TYWRj8fWQK4LVz60PI7JQ7PxdaDUNQgMEPdklhkbIaHeoO11ynKNfs4g6sWxeajV5PsbxUNLeWuxOMvkwNyDbpeaiU-P1ej0XIGhQN_ktOEBjNUoW5RoUPs1ZwsLC51YIhdv_3ZOrhDWCSMbX3vMpJpC7Gb-WvMhxH4FjMnfs0O8FRObKVixQcIK8FcSkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول منچسترسیتی به پورتو توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105923" target="_blank">📅 23:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105922">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">امباپه چه تک به تکی ریددددددددد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105922" target="_blank">📅 23:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105921">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105921" target="_blank">📅 23:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105920">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلگلگلگلگلگگلگل برای سیتی توسط هالنددددد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105920" target="_blank">📅 23:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105919">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
📰
فاکس نیوز: امشب برای سربازان امریکا دعا کنید  نیروهای آمریکایی به طور فعال در حال حمله به نفتکش‌های ایرانی در اطراف جزیره خارک هستند، به نقل از فاکس نیوز  ایران گفته است که در مقابل به پایگاه‌های آمریکایی حمله خواهد کرد، اما بدیهی است که ایران *خیلی…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105919" target="_blank">📅 23:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105918">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
📰
فاکس نیوز:
امشب
برای سربازان امریکا دعا کنید
نیروهای آمریکایی به طور فعال در حال حمله به نفتکش‌های ایرانی در اطراف جزیره خارک هستند، به نقل از فاکس نیوز
ایران گفته است که در مقابل به پایگاه‌های آمریکایی حمله خواهد کرد، اما بدیهی است که ایران *خیلی حرف‌ها* می‌زند
امشب برای نیروهای آمریکایی در منطقه دعا کنید
و برای خانواده‌هایشان که بدون شک نگران پسران، دختران، شوهران و همسرانشان خواهند بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105918" target="_blank">📅 23:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105917">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzvlDN1crAbKYm-6wPIJEvnqG2VJ4RRMxobOL-O96tvFtsIuKF8OXhsS94xhWHNkAD_mWL19vvNdPqtSb71tODJggOkCPQCRdbM5bi71e0TDM9Ohz8HRBCwLMZRFwO16pGKtGIO1WFTWBXiRFsS1cWwe8ACzkp0LTsH-A4Pe4-WNBqJ_u9tQpbUV0mBCNvlUqTdWyiUyojveUzZrA4BmScDzM-9TRMVz8581uGddWMpvVTLkTOoLGzWeL8PMOx132CsMr-6biCUmxRRm4lN8VqFA4QyHPiLsSGMA_zcFokMPWByz3qwqc3pEOL8R5Wfm7VIT1hMWENwsijKbZcqK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت آخری که رئال‌مادرید گل نزد
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105917" target="_blank">📅 23:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105916">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کورتوا مصدوم شده</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105916" target="_blank">📅 23:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105915">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کورتوا مصدوم شده</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105915" target="_blank">📅 23:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105914">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلگلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105914" target="_blank">📅 23:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105913">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گلگلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105913" target="_blank">📅 23:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105912">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23f212f578.mp4?token=alF2wBg_W9cK2Yb8Fo5UJwzuzC9qd0wdOfTPdu4XitbXEETOpp0wzNyMrb49sgiz6iBTAeoS_fkPimzTlq-ifp7WsUveDlfJx7aGacMCr0iJNDmkvcTpQYbx0FlJdRmKHPlLWqeggKmQpxwzecOUuN8OEMSJZc1DzOGKL-Um5UL8M2kZuvbAIX0hm0C7DuDzAVwvFSnsjmrbt6pyrAbbPb4J_hntBQTiAy2Hj2B4-g35oRvSsZpVCnrk9P4znWSpd46_l2nAUbdK_HiFFkM04nrWpGGylKVZg6YYN8nnAx66V_DgZGoVuRLmdiI7--6chlbTqYXyRm2o_ZViouq3dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23f212f578.mp4?token=alF2wBg_W9cK2Yb8Fo5UJwzuzC9qd0wdOfTPdu4XitbXEETOpp0wzNyMrb49sgiz6iBTAeoS_fkPimzTlq-ifp7WsUveDlfJx7aGacMCr0iJNDmkvcTpQYbx0FlJdRmKHPlLWqeggKmQpxwzecOUuN8OEMSJZc1DzOGKL-Um5UL8M2kZuvbAIX0hm0C7DuDzAVwvFSnsjmrbt6pyrAbbPb4J_hntBQTiAy2Hj2B4-g35oRvSsZpVCnrk9P4znWSpd46_l2nAUbdK_HiFFkM04nrWpGGylKVZg6YYN8nnAx66V_DgZGoVuRLmdiI7--6chlbTqYXyRm2o_ZViouq3dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
اشتباه فوق‌العاده کیری گلر اینتر در صحنه گل دوم رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105912" target="_blank">📅 22:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105911">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انتقام بارسا رو قراره مورینیو از اینتر بگیره
😆
😆
😆
😆
😆
😆
😆
😆
😆
😆
😆</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105911" target="_blank">📅 22:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105910">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اشتباه فوق‌العاده کیری گلر اینتر
😂
😂
😂
😂
🤣</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105910" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105909">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رئال‌مادرید دومییییییییییی</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105909" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105908">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105908" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105907">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25403f5ba8.mp4?token=oLT8NR_aTfZlFxu1Wh5qtRCFrONnHpwgDALfdhrcXbLS5o115-u3bbaiobJ0pB762-IQ6Qw9aRYmXwQWkb-Uy1F41G_sFZgdhFhnybVQeJdLCrNh12W2P4bAi-o25wlggNGNGm9mloWc-wOtARKFIdPF4vqigQa03SbFMTFmPuVzXXRxzVzCOjJmciKyLYZBzPrWmDhGZNxubR9F_1pALnYXOjrnMH1viUH6eNLu-RtuWTSWpDzfeYJE1jNR20HXge2MCt20x47rq5QyBj9CQLu8E2LHj5ddaFeOfgP3TrDOCWQyjCaKHgaPiBnM8eIJpRmFonAX9i_ULvzqN_DgZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25403f5ba8.mp4?token=oLT8NR_aTfZlFxu1Wh5qtRCFrONnHpwgDALfdhrcXbLS5o115-u3bbaiobJ0pB762-IQ6Qw9aRYmXwQWkb-Uy1F41G_sFZgdhFhnybVQeJdLCrNh12W2P4bAi-o25wlggNGNGm9mloWc-wOtARKFIdPF4vqigQa03SbFMTFmPuVzXXRxzVzCOjJmciKyLYZBzPrWmDhGZNxubR9F_1pALnYXOjrnMH1viUH6eNLu-RtuWTSWpDzfeYJE1jNR20HXge2MCt20x47rq5QyBj9CQLu8E2LHj5ddaFeOfgP3TrDOCWQyjCaKHgaPiBnM8eIJpRmFonAX9i_ULvzqN_DgZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
گل‌اول رئال‌مادرید به اینتر توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105907" target="_blank">📅 22:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105906">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">امباپههههههه زدددددددد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105906" target="_blank">📅 22:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105905">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105905" target="_blank">📅 22:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105904">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWA683hIgztbSBK4KOSiVuwBefIx8ed0loLUXyVtrwHUx6TRoRPiYSUfCacJsAukxW6EYwqXQvlR7RwpA8-yixK3QnNK7L5icUqsnj268v_6PbWK8KATGyl075DjuIB0EUjW9HGegqWkj4eqaYpYKq-ArJGd2fUPyWnaDECy6vwXiw5JhuxUVVgLxHiVVAbuJgqNmB-soLeD8H2viO-D8Zy8ODT4pbKftFKBQ3skui-5lT_hmRrqgodRVJ29afXFYql-QSgg2E2O8TaEbBChIj6TkRu6gdgeuomog6sPE1LVB0kcXpyJfnDbCfaILy9bMdsaRVKPqs1ZrDdTQrtrjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نتیجه اخلاقی از فوتبال ایران:
فحاشی ناموسی در رکیک ترین حالت ممکن ۴ ماه محرومیت داره.
جمله "شاشیدم تو این فوتبالتون" ۶ جلسه محرومیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105904" target="_blank">📅 22:07 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
