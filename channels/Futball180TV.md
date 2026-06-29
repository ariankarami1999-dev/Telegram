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
<img src="https://cdn5.telesco.pe/file/Uo1KV1i3JQ99jogJx65kuC8P7tIK5U3iCG10r0xX-QB0oaC7QHtPQ6zw6THi-ra7gZIlEKFDK7DsbD1YJGzlcd64BZPVzNqNuzZkO44OdYSyZyKn-cbC0bBjUb4tUIBRiob9r411c-AsYJ_bQpQ5dbEr0ygtLULoAYPAz7EHxCKqCqc-mkQmRLx-h0A9Aa4EoQoTYnZsKnXU71WiygkawXfwTpFF5tZJ6zc9GRk42XJWpuFSkrGrYBnVaLU6w566eGPKZpi3KcFsuWa0XkTJULeAZF55dUU5fcFakpdlU8cgdV-8GvzDy-kxo1JdMadfCduQJgXvGoLvd7CrFPctOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 682K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 03:25:16</div>
<hr>

<div class="tg-post" id="msg-97002">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5899cc42f3.mp4?token=EEOhKwjxhXbmR5_trxjDcW12Kmgugwf_2lvE2l579lNp7-BEU3ms8NDchYIzRq7yLyblYeCuXj-I19PDfAwx2cSn_j4t8pnXbNKDlvn93FAOsiLUDoBdJ0p9xy6oNV6NKqaly1aNDR0VVW9iHJCbLF3_8RMovMmKyJexjzrV17JxdpvnzPg6iSnwkuWMqWHnkx3UuEPEcZx3-oKmvR5GMddFB4D5Tv7VfkMzdU4jtxIvjtY1UIoMyvDL8en6KPtsrCKH18F7fCslr1aOm38k7nNOhA6HHybD0oSrXmBT4uzFYu3mKQPajjQkJZYRlPC8B3pvcRE2IpPKok9UCb2G3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5899cc42f3.mp4?token=EEOhKwjxhXbmR5_trxjDcW12Kmgugwf_2lvE2l579lNp7-BEU3ms8NDchYIzRq7yLyblYeCuXj-I19PDfAwx2cSn_j4t8pnXbNKDlvn93FAOsiLUDoBdJ0p9xy6oNV6NKqaly1aNDR0VVW9iHJCbLF3_8RMovMmKyJexjzrV17JxdpvnzPg6iSnwkuWMqWHnkx3UuEPEcZx3-oKmvR5GMddFB4D5Tv7VfkMzdU4jtxIvjtY1UIoMyvDL8en6KPtsrCKH18F7fCslr1aOm38k7nNOhA6HHybD0oSrXmBT4uzFYu3mKQPajjQkJZYRlPC8B3pvcRE2IpPKok9UCb2G3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇻🇪
👍
در‌پی زلزله وحشتناک ونزوئلا، نیمار مبلغ ۲۵۰ هزار دلار و خانواده لیونل‌مسی مبلغ ۵.۵ میلیون دلار کمک بشر دوستانه به این کشور اهدا کردند
منبع: ال‌ناسیونال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21 · <a href="https://t.me/Futball180TV/97002" target="_blank">📅 03:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97001">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHZiv-DPXRerQOG-5ZY_R9RcaIlD0g1PPbL6GTMXanHJ0tsFZytA-f7C9ZN1swPa_iQsaoVj122aoyKOGNOhXd_ztR3YFzcYS7z7YawmWR6ddejcKUZypOyA3wDyA3zvA4Vr5LtWSrwn3txxTbgl-Ag9z8hRSxbq_LO_Ustrt-Fd47fCOX8jfuvl668EIWPOTeDSh6aBGOBfDXKzJpZIoPiD-T4cz7ZUv2QjiIgiP69TVsJ3whghCOgPK7c03vjuQhJCh7p7D3qtnt3fX8EcOcPHA2nl7MpBKTZzM51yhMB3tnARGMJoCeZ_XYRoy7I9GSvl98-pOQbD71cD_-zRQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#فوووووری
و
#رسمیییییی
؛ مانوئل نویر رسما بازنشستگی خود از بازی‌های ملی‌رو اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/Futball180TV/97001" target="_blank">📅 03:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97000">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یکی بود میگفت یورو از جام جهانی بهتره
🤣
میدونید کیو میگم دیگه؟
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/Futball180TV/97000" target="_blank">📅 03:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96999">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0f16wFN5DWue3IXoTN1P0hG7Z0SPEuYAa597WJOpcW1N16NX3qpFKeYKJP3lrFs2BMCFKRcvGj2e2fe9tkby4Kerht-LFfpq0RpiS42iVI8IRd0Xqnhy3yNECRIGYmfN_WXeYV2zQ5q6JzCm7bjCF0PeZWrUldR76qopQGn3bHdmGmXj9FxCnTin2PLLw2mitqMywfrXwrwcuSzRxyS0Q0abKhxOn2SFeywz2BndpyUV55lGJKGBKYERfjzTNir9e6TcUXZRI_diO3SOZCgL49x_G-u7BUa66R7skZVfCaw0Pp2T_1D2dQQhAMLMJuNn4OLp4HZRssAjvtraAU_Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه مسابقات مرحله‌یک‌شانزدهم
🇨🇦
کانادا
😃
-
😏
آفریقای جنوبی
🇿🇦
🇧🇷
برزیل
😀
-
😃
ژاپن
🇯🇵
🇩🇪
آلمان
😃
(
😆
)-
😃
(
😀
) پاراگوئه
🇵🇾
🇲🇦
مراکش
🆚
هلند
🇳🇱
سه‌شنبه ۹ تیر ساعت 04:30 بامداد
🇳🇴
نروژ
🆚
ساحل‌عاج
🇨🇮
سه‌شنبه ۹ تیر ساعت 20:30
🇫🇷
فرانسه
🆚
سوئد
🇸🇪
چهارشنبه ۱۰ تیر ساعت 00:30…</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/96999" target="_blank">📅 03:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96998">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJcxHrSKrcitqPxad12cn5SEt5zhYbASxpvJeudP3_D_shm2BFnWmh5nsggfZj3as5Tx5fNVtI294hVZcYPv2ZmDmchUG0c8mSFAP9ly6h8nrSkkZ8alIrH88goAUMv6T0zeozi8oj7jlIqgjroW0rpn3glcqqqBhcN494Qkv7gmDaxOQmPyWcJ7bdOaXBxgx9xiiLU0cy9onISQupFl6vjR6tDjCpZ-jPan1ttcwowS2iSn4xuhRFuigXyGbI1CmvU2TVopz6ycJb8zVqlExCDzOmCnpc1WblhhJ5HE8Y_LcBF67NmasJWXkCBWtndvMzyDY6RIiPcFctcoC5nxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
🤡
فقط ادایی. ادا ادا ادا.
به یه نگاه به کوچ کردن کارلتو تو بازی امشب تیمش بنداز شاید بفهمی فوتبال اونقدرا هم که توی کودن فکر می‌کنی پیچیده‌ اس پیچیده نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/96998" target="_blank">📅 03:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96997">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jd7v0hARsdVxxZIN_oUESzqPEVB-ckpnjCtTZyEOgVZfhEzCdyaHy8J2ioC3rkdlJpIhlPCM5HdMt3FxWlveLZL_d86UGJq3WtYrDC-3GIQ212biGULtn-F0-hQ4eu2zQTCUp6ZSv8hOccv0HsL6LR_zol8jYsgRwihW8Rw6CAajfS6nBwAJ-vhVqBG3ZT9Gsjs2wgDxz5bVRzrE9Hd7eL14SOeVF5Aj7qMv6JfGLmCQiHa02-9d3h6pCcbMv9XcyepGirY3AB1__VsjLi4t30Di1CpgciKMjNrGHiB_9jjKpdlqsxclpmYZxM8E7IEpZSMD84wk0srtF1ygzS_tgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاراگوئه قطعا حقش برد بود
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/96997" target="_blank">📅 03:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96996">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
‼️
🇩🇪
#فکت؛ تیم‌ملی آلمان در سه‌دوره اخیر جام‌جهانی به مرحله ⅛نهایی صعود نکرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/96996" target="_blank">📅 03:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96995">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddTwoBcfzyw4xZFjSscDstkgko23zSLfEflB0uyhQVHF6h3i8rxgq6bc973tOfMPnAj05e9ys6QTZr_idCL7_JNMrHU9v7vuFQMC0MJ4iFX1HxN2ZzmAP88aZpUdAfqMbL5JxM0qkuxj4eLatIM1UNT4tciJQGkkRSK3J2ghIgd-aWqmtCw-lUB4gxQnvLdcemAmMQg4jcB7ZESHMj3Yv4NQ1ZTcDiaTBH3kRIrIzF4rv9AQh4rSHBQoVrNsGCiriUB1KOsPuTzd88Gv67XmfyyMbRp1MokOzCO2amUhmPRmHvZ25QpaKj3N26dozgxSeAfuGb6XDbDkZarw89OGAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه پیش: هاورتز قهرمانی چمپیونز لیگ رو در ضربات پنالتی از دست داد
❌
امشب: هاورتز با پنالتی که از دست داد باعث حذف آلمان از جام جهانی شد
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/96995" target="_blank">📅 03:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96994">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZ14ModyPQZv462ylTBdFEp61W4Ghbk5ZRneBgBVMES4xfK6pRpbUr2PmO9UGM_-HvdZ_9U29BKMMtf8s0_adKy40aIeqmy8u3xWjfkFrFrMbC1cP2rDex7Q2nhF31_q7jwRXHNdtJlr8F3FM__MogdiTOll-3wmeODbHnodlvTAbaS3O_lCyBCPBBEnFkqzbyETQoOZfIGACL5dD5F9gu0NuesUPn17OcXFWQhI4-JJ38nPWVMOFySLTov7vx2x6MKOgXnma9JjB5TYiI63tPID9pG_-AQ6fpKzmo6NWtZXsduTc75vWvnDP4w_Q-fQ9VjQJApcCUkJiWDXUgBFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇲🇦
ترکیب تیم‌ملی مراکش مقابل هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/96994" target="_blank">📅 03:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96993">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA9JO3cyIstJBd_DjAktNn_9Qri5QQIw4TiKER3Ik7LVX3xBm3MyKyC-gCO0NOEDdfy26Y06wd9ETrwH9fuQJtiAPdblqK-tVTv37EsYDt2U8AyA-BUbMOotmcGQDVqj04x1NNI4VWB4yvCX4X4RMIGRUuI_M5d6kLhDIxnDiS2-YAfnvH5rrBRvslkrgMpDbF1IB97TSooTOyei51GMOBZFJceD96_VG_oaZtTJfSFh1Umza6xs4nnjQwjMwINZZYQRP_3iV4FvuF5S6VtL6V0wS9Ohc7IimQ4nYg6LeGWf_VlsglEF-PdOLdOOITNXCdWOQ11y4NYAteMmUmOHtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇵🇾
🏆
🇵🇾
🏆
🇵🇾
🏆
🔥
Respect
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/96993" target="_blank">📅 03:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96992">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-poll">
<h4>📊 فوری و سریع کی میبره؟</h4>
<ul>
<li>✓ مراکش</li>
<li>✓ هلند</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/96992" target="_blank">📅 03:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96991">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdZ0OWBGS_qZedWOxO6tWnhSuPDENv0_GiOQcWV55vU4yfOjNYzpDCohse3_SabPeQmb0P40sa6rKm0FjIIqJ333DyLANKgb3TzLH8ESTJt46BEIoggMC9QZMflpQlSraLdhwOwd38GmU8qkbbsNaO6s0H0nAiKERHgqVlvNF0EUzY3XFXg4QSyZ4zT4Q4-4_oKq12TeANAxnBsZ8FO8rpqGvF7BMdbn8dMRVjvh8PqIbak2xHd19bg_jwWvrKW97W74VELK_6ftcJz9ovuvJtbWlpjstnGpc9x3N-4mzXmuoLECHrXcHUBvQdVmCtJIeOkImq96xwC74L_xkqSsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
گریه‌های مانوئل‌نویر در آخرین جام‌جهانی‌اش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/96991" target="_blank">📅 03:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96990">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
‼️
🇩🇪
#فکت؛ تیم‌ملی آلمان در سه‌دوره اخیر جام‌جهانی به مرحله ⅛نهایی صعود نکرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/96990" target="_blank">📅 03:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96989">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqv0TzSnJr_4g1Q0CfZxRgfxh7qYdR_jU235VHcfO0P32z7cqZGHgGXvgU4_GsmCuU0XB3qvADaaCHvWJlY0M1ZiH5mtSz6sc06wn8ZPZ3HBT_b_e0bS21lrej0EVNHbqx2u3mOBEXGpUdXnbktm_aPChr9Id1RedLpL42snDUDoVNq1JDnw6y9Er7rcML5xAQiIm1KaSjt_n28RgbD37ExScXQETGOuLxdFkFTu3-XTodiTlD1CBI607m9UntL8RiteZMwlCN8aqLMM9IaDBHMyOlfnKJLpXLDEZBNZEK3IOLj1sIjy1WcWAnf_eWAw6y-6aQexKJtL3AaOmuIQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇩🇪
#فکت
؛ تیم‌ملی آلمان در سه‌دوره اخیر جام‌جهانی به مرحله ⅛نهایی صعود نکرد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/96989" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96988">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/96988" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96987">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QH2R-AH79ZX2Uw-YJ0YqxjmkGFZ5LfdlnU1St1aEared7Hy-XuQz4Tv-I3d8r_QqfUUrzkRCKjUEYc8n3Sp1MChZ-KZVYa8igF_PF-Hm0rAkaxKxDXYTCvaq-VSQQoSEyxWjK-vh-ty7SwDG_gv8EQPocmN6Iltrxk3ukLaonTT9Bx4jD1a2WGDhM0CxAWdI0lreVhCnl0sLtakZvM-7yZox2VkgWTI-ZBHCpfjwPUIQijBclsrMTDpXTS6LRs_iqYHWplOuOjYMj7qMIo_nMRjclDZnts0TrFv2MKYFJL05PCAkSxPW_IB631QYPD8IsfrBaSXTwmzrlizJKkMsUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/96987" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96985">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaUClrVNUzGZHh0RvEOUIwQqyoTlWxaVNyEAlg02ZqVYaf9IrjIrYvM5dOBNq2XLfVTnOQDD0DFcfCCgKRyhLG5xB0kL2koc3iRsZxbPePBQGPnNaKwxafBG12MCyJij1Isx_LqKUDeC6kzyHznDxumQiaI69WO9dlJDYYDKNk2dlLgsrBxANc7czaQTYucimzt315RbhG60pzdXKhdDQF4BExBQNHhHqZB3IAQjIJT03hOhqf5LuJRPU_aQQEWbJVyMQdtixlyLWQNqMPbpp8WDw80OXHifde4ORqQY7i15fqHPf043-D9hAnkSBt8mr4_y2qIX9hG2nn8H6ihO5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇲🇦
ترکیب تیم‌ملی مراکش مقابل هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/96985" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96984">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">همینه میگیم فوتبال پیرمون کرد🫩
منی که هوادار آلمان نبودم اینقد ناراحت شدم خود آلمانی ها چی میکشن الان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/96984" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96983">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4ceZNQV20b3lxu5Xq1JyP9f1FVpf3jhfrhDq1mMBlOP9QHQjx4V_cYs-uhtF5rpL9gy8HLbeM0XKx2avLyWkHUA7y7FJMvTOybN6cpM_dGcVDwUMmm0F49B-6-OG_RPpobagWSoBchv4xGqhzEzGuT6B7XFMChnB2n_dLsyZ6blt4JZGXqlVl_txDBUpbIjRup5DiZJgS868iEfCgQDK9TPTe1iGg6oWdA3bGH-cd21cEHtj3vyym8Omw5B-WMgCxJ6Swz6hqRW8KGf4IQq0f_tXzlL19kB4s24Ey-Qv9GpEQruJ66cdvn6AUNrzSTq_Bnh0xgZw_NSiIDXX9rclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنده دیدار حساس فرانسه و سوئد به مصاف پاراگوئه در مرحله ⅛نهایی خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/96983" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96982">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هیتلر آسوده بخواب که فرزندانت سفت تگری زدن.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/96982" target="_blank">📅 03:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96981">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نویر
💔
💔
💔
💔
💔
💔
💔</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/96981" target="_blank">📅 02:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96980">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G27H0Vmw44OI5RG1Cwq5I42CEsS7uw_tTdHJqMUA0Fdy99W8qR3sqZi5WqKjI86KP87ojdByHMQjS8m6ulnB-uNcIXjkkSp3aeXmewBFp5vce0uV77DZypgiWjP-IIhGiXRv2m_1OvC78VBsY9huRCZouu7Aw-PFTWe8h4ZwhJYd84R-zvbkjs0EwJpD5WYbonxn4Hb4ujkYcMgvzMIo5RC3TUKQlpL3UWG_4j_FlgsyIwMfHDNmGgrPkZSXqPHjw0TkdBQ_XhlslavwYvWsTk8S4HZBMvNip1x4NboHipt7nVuT-JASP6tYE2RlJxRmPcLN3lQ_b6pmWyM0qnUotQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#رسمیییییی
؛ پاراگوئه راهی مرحله یک‌هشتم نهایی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/Futball180TV/96980" target="_blank">📅 02:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96979">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پاراگوئه بزنه رفته مرحله بعد</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/Futball180TV/96979" target="_blank">📅 02:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96978">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">◀️
😀
آلمان
❌
✔️
✔️
❌
✔️
❌
◀️
🇵🇾
پاراگوئه
✔️
✔️
✔️
❌
❌
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/Futball180TV/96978" target="_blank">📅 02:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96977">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">جاناتان تاه پشت توپ</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/Futball180TV/96977" target="_blank">📅 02:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96976">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">جاناتان تاه پشت توپ</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/96976" target="_blank">📅 02:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96975">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آلمان برگشت</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/96975" target="_blank">📅 02:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96974">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">◀️
😀
آلمان
❌
✔️
✔️
❌
✔️
◀️
🇵🇾
پاراگوئه
✔️
✔️
✔️
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/96974" target="_blank">📅 02:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96973">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گرفتتتتتت
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/96973" target="_blank">📅 02:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96972">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پشماممم</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/Futball180TV/96972" target="_blank">📅 02:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96971">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نویررررر گرفتتتتت</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/96971" target="_blank">📅 02:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96970">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پنالتی آخر پاراگوئه</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/96970" target="_blank">📅 02:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96969">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پنالتی آخر پاراگوئه</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/Futball180TV/96969" target="_blank">📅 02:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96968">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">◀️
😀
آلمان
❌
✔️
✔️
❌
✔️
◀️
🇵🇾
پاراگوئه
✔️
✔️
✔️
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/Futball180TV/96968" target="_blank">📅 02:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96967">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گلگلگگلگل آلمان</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/96967" target="_blank">📅 02:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96966">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">امیری گلللللللل</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/96966" target="_blank">📅 02:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96965">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نویر اینجام گوهی نخورد خودش زد بیرون</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/96965" target="_blank">📅 02:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96964">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">◀️
😀
آلمان
❌
✔️
✔️
❌
◀️
🇵🇾
پاراگوئه
✔️
✔️
✔️
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/96964" target="_blank">📅 02:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96963">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پشمام خراب شد پنالتی پاراگوئه</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/96963" target="_blank">📅 02:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96962">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گل شه تمومه</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/96962" target="_blank">📅 02:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96961">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">این دیگه چی بود زد
😐</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/96961" target="_blank">📅 02:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96960">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">◀️
😀
آلمان
❌
✔️
✔️
❌
◀️
🇵🇾
پاراگوئه
✔️
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/96960" target="_blank">📅 02:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96959">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وولتماده پشت توپ</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/96959" target="_blank">📅 02:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96956">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وولتماده پشت توپ</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/Futball180TV/96956" target="_blank">📅 02:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96955">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه پنالتیم بگیر مرد حسابی شاید خوشت اومد</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/96955" target="_blank">📅 02:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96954">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
زنده از ضربات پنالتی(آپدیت خواهد شد)
◀️
😀
آلمان
❌
✔️
✔️
◀️
🇵🇾
پاراگوئه
✔️
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/96954" target="_blank">📅 02:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96953">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گلگگلگلگگل سوووم پاراگوئه</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/96953" target="_blank">📅 02:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96952">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
زنده از ضربات پنالتی(آپدیت خواهد شد)
◀️
😀
آلمان
❌
✔️
✔️
◀️
🇵🇾
پاراگوئه
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/Futball180TV/96952" target="_blank">📅 02:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96950">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلگلگگلگگلگل</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/96950" target="_blank">📅 02:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96949">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">موسیالا پشت توپ</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/96949" target="_blank">📅 02:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96948">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">موسیالا برای آلماننن</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/Futball180TV/96948" target="_blank">📅 02:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96947">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
زنده از ضربات پنالتی(آپدیت خواهد شد)
◀️
😀
آلمان
❌
✔️
◀️
🇵🇾
پاراگوئه
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/96947" target="_blank">📅 02:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96946">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گومز برای پاراگوئه</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/96946" target="_blank">📅 02:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96945">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گومز برای پاراگوئه</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/96945" target="_blank">📅 02:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96944">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
زنده از ضربات پنالتی(آپدیت خواهد شد)
◀️
😀
آلمان
❌
✔️
◀️
🇵🇾
پاراگوئه
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/96944" target="_blank">📅 02:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96943">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گلگلگلگگلگلگلگل زددد</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/96943" target="_blank">📅 02:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96942">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلللللل آلمان زد</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/96942" target="_blank">📅 02:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96941">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کیمیش پشت توپ</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/Futball180TV/96941" target="_blank">📅 02:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96940">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
زنده از ضربات پنالتی(آپدیت خواهد شد)
◀️
😀
آلمان
❌
✔️
◀️
🇵🇾
پاراگوئه
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/96940" target="_blank">📅 02:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96939">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گلگلگلگگلگل زد پاراگوئه موسیوووو</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/96939" target="_blank">📅 02:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96938">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
زنده از ضربات پنالتی(آپدیت خواهد شد)
◀️
😀
آلمان
❌
◀️
🇵🇾
پاراگوئه
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/96938" target="_blank">📅 02:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96937">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گلگلگللگلگلگگلگلگلگ نشدددددد</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/96937" target="_blank">📅 02:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96936">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کای‌هاورتز پشت توپ</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/96936" target="_blank">📅 02:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96935">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
زنده از ضربات پنالتی(آپدیت خواهد شد)
◀️
😀
آلمان
❌
◀️
🇵🇾
پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/96935" target="_blank">📅 02:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96934">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJdEqyKAKTJ0BluaJ6Gi7qvlH0f1NUxmSQmJYQ7XFPyDFrUdXQcU-DkFn86Tku4QwguJRGcfvPr76G0A5suNmKFghI4OHSTqr4BIJhx1pWMZjEt2oFgpNvbTBlRXoVHjTei1veriuUbjC8cHX5PMt-dF6a_YBTjmhQ1O9TaDtOL6RmgIJVyRVuAckY7ERXsx32bivPwpGN_XTyzx9phJtQhI0sT5zsrMnnmWFR7uGOV_LMiCe3y5dBSgUWst0rbwjSnktcMvXYfNl7_fgaAlYEzfq3_ytW-s1GreOv5Fr7kZPvRQ1PjXIO3t7fYwDjeTyWrkaI__72g513Sdw6BkHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد لروی سانه مقابل پاراگوئه:
0 سانتر صحیح
❌
0 دریبل موفق
❌
8 بار شکست در دوئل‌ها
❌
0 ایجاد موقعیت
❌
0 مشارکت در گلزنی
❌
23 بار از دست‌دادن توپ
❌
کسب امتیاز 6.2
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/96934" target="_blank">📅 02:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96933">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
▶️
🏆
🇩🇪
🇵🇾
زنده از ضربات پنالتی دیدار آلمان و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/Futball180TV/96933" target="_blank">📅 02:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96932">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🏆
پایان‌بازی در وقت‌های اضافی؛ ضربات پنالتی تعیین کننده تیم صعود کننده خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/96932" target="_blank">📅 02:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96931">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItZ_bhn8lG-E-2bVczTazWc6_4EK-3zJJ-6uEnBGa1X_pivaSusQnejSivH96gHZ3j0dEe3AHMQ9HIYlV6L32aSfZGAiSDufIog54bk6tpaXO_PilaBNVbJbsIraou33nzzqeXsOwO_Lf8YsRn8-0GFJ9Tx_gT4QNo5IzSbHaCzm4YFcJ5Zz1PC3xmLdEvPaR8yXFuZhUrF0PbsNAhlm1joTnz1lAtV5W2Df043XT5OhufnqQIrRsCdOstaZA-_qXB1lkGCQ4WPGMUZQVEsP_nbaVKOh72W_nFCWG6R2zyufA_QbIMBBSk7gkEKaxP04SHpbBR2MxRR2J8kUuMOVvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چی فک میکنم طرف حق داشت واقعا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/Futball180TV/96931" target="_blank">📅 02:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96930">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ناگلزمن شاید بتونه با کسکشی امشب از پاراگوئه بگذره ولی فرانسه رو کونم بدن نمیتونن ببرن</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/Futball180TV/96930" target="_blank">📅 02:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96929">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آغاز نیمه‌دوم وقت اضافه</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/Futball180TV/96929" target="_blank">📅 02:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96927">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گل آلمان رد شد
😐</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/Futball180TV/96927" target="_blank">📅 02:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96926">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جاناتان تاااااااه گل زددددد</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/Futball180TV/96926" target="_blank">📅 02:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96925">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آلماننننننن دومیییییب</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/Futball180TV/96925" target="_blank">📅 02:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96924">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گلگگلگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/Futball180TV/96924" target="_blank">📅 02:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96923">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🏆
پایان بازی در وقت قانونی
🇩🇪
آلمان
😃
-
😃
پاراگوئه
🇵🇾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/Futball180TV/96923" target="_blank">📅 02:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96922">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🏆
پایان بازی در وقت قانونی
🇩🇪
آلمان
😃
-
😃
پاراگوئه
🇵🇾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/Futball180TV/96922" target="_blank">📅 01:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96921">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">▶️
🏆
🇧🇷
🇯🇵
خلاصه‌بازی جذاب امشب دو تیم ژاپن و برزیل با صدای عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/Futball180TV/96921" target="_blank">📅 01:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96920">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">همچنان بازی آلمان و پاراگوئه در دقایق پایانی بازی مساوی دنبال میشه</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/Futball180TV/96920" target="_blank">📅 01:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96918">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BC3LXf6WvdPBQ_EspYT62980KiTAzDPpHbXucVQ2PdDs-zDDW7s3Xjb_8KqZhZZ84p0Dat4uHtgZN-q8KoFEDgudh4AViXDg3tkUipR1Pi-IOcgmjJvn5SiQ2Oa4DM9J1tjwsZmIv3mXM3VKr-CeaqeAcjs9_S5F0OCfS502GwbKUFx_51_U6TDzBfSiCDyGE6Qrt2T70ukrgWScBWOnEk46wAVmHQiPNbFbDL3BecW6HBbQsmhAJx7K9ew7fM90FiRJQYLWWC6Ximh5bo9G-wKuCRRqUyx9WgGnqYPH6YPWtwcMJa2lJUZw0U96pzsJw-8FK2lwQcLfUANZnQxdnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knomW7aIKk9p4KL4jj--Zr23AmxUQT2ocaXeNsapBZXufB2V1vqlIbX46LUv5unIwPcSwzLym0pws45jpnJ8BUJzEkjeR4boxB9FdPon6hnifyo0sCs9qijIm9iKIGC00xVjIP__mriJNE28Fi8YjQ7Pmi87cVRjvUILHWAPpqTPg5rMVQ90OUgN7FYy8Q1rK1iBmEEpzon2-YjbdASeCRD-UXI9ryyYNHYn57-04SqAx3Vz2F9Eja3Q_Wlsy1LuFZEVJ5DbKWZV5B0fJrLNYFSmXgSkGka5THoQVz1-dXAAZzMcnVhPVg4MqA7H9jDiu2B7Tj4Sc7-qgJ7JBJ8CKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
🏆
یه پیج‌خارجی ۲۴ ساعت پیش اومده مسابقات مرحله‌یک‌شانزدهم رو پیش‌بینی کرده که دوتا بازی قبلی درست در اومده و گفته آلمان هم امشب دو به یک برنده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/96918" target="_blank">📅 01:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96917">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پشمام چیو آلمان نزد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/96917" target="_blank">📅 01:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96916">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آلمان زددد</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/96916" target="_blank">📅 01:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96915">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/96915" target="_blank">📅 01:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96914">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUK1FYD9TZJUmqwillT1M2bDbJ7n7513CXm7unmWCNTgZXIL99OjT7b4Ks85u_rflJRpImj7QJc4oYT9zkNveS3upJPb7-3zj-aY7DNdSLy7kVE3u0W2MgY8WoWo1LFoNAOkdXyOHqE2OhbHVF1eSDMRJzmyMUveq7KLPWcsUS_yeBnyD14RH0RoiTuio6o62hz5cDFBPpKoQgDOEdZbPPLHVMAH36-3-haLCRH9IcZeUBQ7lyJCYcDplJlRzSMwiI_f7prEgrnkMPrZSaGDJM1Q03gtdI_aTEvfT4GgmrTUcxNzkgieEfTEM2kuDH_dCQZBoMP2yYONBXR8Qg7vaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نویر تو 10 بازی متوالی برای آلمان تو جام جهانی نتونسته کلیین شیت کنه!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/96914" target="_blank">📅 00:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96913">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaqmwbtfvMjwN0wnMZ08vqRDbVvYJWtigc_eeXePvGWRWKH6VHY4WzQcUtFtNRcisQBbCMzgcK9Td7LXcpXiLUzr9qBu_hfnkziuzMVfabvvSNtZB6_n0dLzSBusQ7yzDEdsJ3D5ppv-i8AjhrTDcWbq1GfryqIX9YwCNUAe5i679MMDP8Z_qYbd5pWg4aWeTVrhPDYRSdhBS1bw-FtIGr5aeP1N1K81poBvaYrN5WnCQqCN8LxbUlYdh2z7g2XTvsTUKAZxK11YUB-fy8ZrqUozRYStElj6gv0UUFnxgj-PxcM7HYAnvq53FbgYwhyxAkm8oKK9STbFo2F_DokkoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون آنچلوتی قدیمی برگشته..
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/96913" target="_blank">📅 00:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96912">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6aO-lE1MmOGCodTRx3R9s-LdJ_PyJFnaIFVuLaIadReBqwHDmPGqtfQxiv3q9sakbYP8O9kxBJLRPvP_J2t_v26GuoA2TQbY9Z8oICdttLWqqXGgPH_xUU8BKKXovpHG6WphUq_vcMbofPRlu1Vmok2OWAjrqmb9eatzNWi9fy1yxRhrKsj0YpxnNrTDfUc3Y2KMSktB9cj_cT64At1gqE8aZvWj6QzyqhX-qPlEhpMq0n1ymrAWMvvHpIbqO0YIuWNXrZL5wnSDQ7747mR251iJm3GAz3A9vdaw_FjmEOVgJgbgV70HhMkpwfLblk7nHmCRitp-Ya7_vYAQ0DFUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/96912" target="_blank">📅 00:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96911">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آلمان با این بازی کیریش بعیده کامبک بزنه</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/96911" target="_blank">📅 00:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96910">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پایان نیمه اول
پاراگوئه 1 - آلمان 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/96910" target="_blank">📅 00:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96909">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97406f3448.mp4?token=al2c1xvQNzR8_0sTVtTUG0SoQ1HsAw4_NuOTj1F0uGiIpWc_zHMoJZhC1x4C7eDnBke540t5fDQD9PxG5IUfyFT4rJtAwMW3IL-IMHGLjYUMCak1Oyt_GkL_OBP7skdDZ08b46cw6C8kbf7xb01_2mr9Q8QJ1bV-u_oAMpiU3aFBlAUNFCatV-llqU_DpZzgTHVYKRXSIGhLBTvPTCUAlTgyVgGtVdrZB15cV0c7y0t2fFpD_yEg3C-VfdP1Oldgu08t1FV6Iv8h4LX0lHxyUXEOSrCjQ9OKVHfOszb3uODkCXCrukZfhzuvBqKgAvqOd0n0YGdPUgtUPJvUznPFDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97406f3448.mp4?token=al2c1xvQNzR8_0sTVtTUG0SoQ1HsAw4_NuOTj1F0uGiIpWc_zHMoJZhC1x4C7eDnBke540t5fDQD9PxG5IUfyFT4rJtAwMW3IL-IMHGLjYUMCak1Oyt_GkL_OBP7skdDZ08b46cw6C8kbf7xb01_2mr9Q8QJ1bV-u_oAMpiU3aFBlAUNFCatV-llqU_DpZzgTHVYKRXSIGhLBTvPTCUAlTgyVgGtVdrZB15cV0c7y0t2fFpD_yEg3C-VfdP1Oldgu08t1FV6Iv8h4LX0lHxyUXEOSrCjQ9OKVHfOszb3uODkCXCrukZfhzuvBqKgAvqOd0n0YGdPUgtUPJvUznPFDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلللل پاراگوئه به آلمان
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/96909" target="_blank">📅 00:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96908">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نویر تو 10 بازی متوالی برای آلمان تو جام جهانی نتونسته کلیین شیت کنه!</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/96908" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96907">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این آلمان چرا اینقدر لوزر شده</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/96907" target="_blank">📅 00:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96906">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پاراگوئه زددددد</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/96906" target="_blank">📅 00:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96905">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/96905" target="_blank">📅 00:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96904">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پاراگوئه زد
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/96904" target="_blank">📅 00:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96903">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گللللللل</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/96903" target="_blank">📅 00:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96902">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d25973fec.mp4?token=uNSCIKPPSmAlTu6So-kFs9BIBXhQQrje5glkulMH6cdnk_TPHTOXk75MF2PQxB6z5KaRZf3oIWfLc0A4K4jgD519ghwQTIdjbC0QygYcwdG0OVC6Mf-i205QqpLN72JcThbDW7W9j-qkGzus9m01Ij9TevV6RiYlNRTrbkBZ5V4vGgxcwur4odeUtetiu4pD47HEcDRY8IiBm4Ad_EfJJnXyM3kUXNuniBShquAlk99pU5Rq2ueusnO38YYR1jd9M91YbA6TouxYLLAQDbPSQJ06NsSDSUr712EY10tKrpBsCg9Yjnb7oTkhbp4BaPQDQ1DcQXPhWuB3biY0Jc6KIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d25973fec.mp4?token=uNSCIKPPSmAlTu6So-kFs9BIBXhQQrje5glkulMH6cdnk_TPHTOXk75MF2PQxB6z5KaRZf3oIWfLc0A4K4jgD519ghwQTIdjbC0QygYcwdG0OVC6Mf-i205QqpLN72JcThbDW7W9j-qkGzus9m01Ij9TevV6RiYlNRTrbkBZ5V4vGgxcwur4odeUtetiu4pD47HEcDRY8IiBm4Ad_EfJJnXyM3kUXNuniBShquAlk99pU5Rq2ueusnO38YYR1jd9M91YbA6TouxYLLAQDbPSQJ06NsSDSUr712EY10tKrpBsCg9Yjnb7oTkhbp4BaPQDQ1DcQXPhWuB3biY0Jc6KIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منِ هشت ساله وقتی برای هایدریشن برک میرفتم خونه ولی دیگه مامانم نمیذاشت برگردم کوچه برای ادامه دیدار حساس با منتخب کوچه پایینی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/96902" target="_blank">📅 00:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96901">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بازی تو این ۲۵ دقیقه هیچی نداشته</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/96901" target="_blank">📅 00:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96900">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN0-_KFZWStEdxbEG6MkBaxjk8dnWVUP535RQA6D7Ia4ILA5zNhAVpxtNeRlXC6EA1-H4Rn8mTFwqg1F2G_DWxEabRedLAgGbHGUn7PKfuYIB_FeMKXAiAPUwW_6P3q6LHzJyrU_KaqB0-xmePfZv7RnaDN6IZ_lD7h48gqdX-jqTGcNhF2OeLUV_4YamZLPFMjUKGgAysQW4ZURii7fz64pWfALqIYnX29mR6YsTn_re-ClGcLmkVJbWXA4cEeaTxIRaPxIprUQF5Qd7FwvaFBjicfrprGE691CHfn4oMVBthJda7FwNUo9OzewXIPunvDqJAif1iQRAmgtd5sVpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بجامونده از برزیل - ژاپن و انگشت کردن یک هوادار ژاپنی
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/96900" target="_blank">📅 00:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96899">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fuyrqa640oYSXPONF26UX58RiXAOtl25DIM_wBhLn-89I-Lu3HvE8jD-wAgFT0q_OQfixfmmsbiARJr2UPvFMQmiejBw_dd2_0SP_mCR1Ff4GV1R1YyOoDiW0eFoTjGQXAK-2ERLsB-cOfdtX3Hrh0HELQirZKC2Ls9UGOHB2mx1IDemFTMIfPOcQ6h29QFo45SlKmKJy8tI0VBOz21Rz0r2_rbuGpCCEVw-OWUG01ozjYaCnWjJ2BeCxYrUy3d1J-8UqXKy2eck0KS4RSThO8-ApzLzV7i9Nh82-HXXyoukLyfjfN8V4roLD5YgzFMkBIKHTAls_wxruEc1vPn78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو: روبرت لواندوفسکی به شیکاگو فایر آمریکا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/96899" target="_blank">📅 00:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96898">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شروع بازی آلمان و پاراگوئه</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/96898" target="_blank">📅 00:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96896">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c7XugRdlZad0D6Pmgr10_ka7dSb3kLpdM2T54gcEU7TFOAm3rS00saBOLRAaAeb3z_H9gvRpiDN4HfwXC7nioQSoFZdeq_d_YupO4ZLC2VzMaI6Burp9fZu0kAlJ_7VTrQmaZehI-5WEK_TTtTvyI_p1Jwust9kjbhcMcmp4Mg1oi1gBZs_3tgc_-lKjoxlpC6hFrDZMmf1sLDoW5aDjv4IL5gZ81C9S3hgBuPT5leNfioSJVvSoV2ku1UjwcD_way6sHWNrtaM9y5YTIfpEAGbAXpl_tYemz-wwyCfQlhq8vZi-qNh87-xW811KgdVLkOREFBnn34B31lyl2EZ6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQ9kXEpZ987Nlfy6EH1KiVWLTUm7_WUlM-y15Lq9gbXCUvRQfVIAz41xy0sFL-MNzNaiCrA2r_0r-HWFWXqzElcoY8dIC2re1a-n9BFvTQxHZJ_eeCuIlnQCHG_WaCsN5_qZZDTvglR_S2FccIH8o7PQWrnE1zyxXe-X-o8l8428K4SLCNF-Xpp9Mis8xB0PaoGaDD2rVjF2Xeq2MmxmhGD9hCt63zs1JmjuvLQM0NxfOrVtgz2dd4K6TRyXY4jstR3vJFL8k9e-tmYTnnROJt-hPP3CTjk2FuVD06xT8hKeuFniiKbR4GdQzqvt9Wz9dw5ZR0iEAjvzgX8oQgwzHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇯🇵
بازیکنا و سرمربی ژاپن بدین شکل از هواداراشون عذرخواهی کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/96896" target="_blank">📅 23:40 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
