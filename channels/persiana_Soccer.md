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
<img src="https://cdn4.telesco.pe/file/CiZGMBNWMltb52ip6FFVQ_MdPlrw446EJCS2fInK8He-cmh35qVVrv5qRFzT8dRUXgf4nxKz5EcQJ942ev-oQpn3Qd67Z9o__p7n5FUUHZ0J50uXGBiufluMo-bYUE1v1Y2DSghfpZIVXEiEU7reW0ukZzq09n34joeapxxJthATJPyvJ235-Wtia9gtDbFLgJhhnRBqsSygkCCFfExnmUtko5yh6YUtffsTQKQeB_UD34qlP_3qG-365qp924abFFBfp0xKrzcweyHx1Od-TEyVY8jDvdbVaVzKME6G4aFrjOkGj23KYzm_hfvWCbNXfSs154KaG3t7d7MC9PGnpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 18:56:49</div>
<hr>

<div class="tg-post" id="msg-25371">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXwN6hgWZFhSTWPN20AzxPkvNGG3kzxZRyQQIdbnz8Dd2RtkRTstFw4gKFAOuWOwQf3JGCERoV02wvCx7ImH6nCL-rB9b6CfyhHAPqT4NNMOkWWOHGX3t1dYRqaoQ2MLzBEUqdBBwwocY4M_sxUk3BufZ-f0QV-Y9VXQT-pgqJgfs2EEIk5yk0YEZlP2cehapjEVM7iToYr1o2V_dG-vhHPT5_R01BX4h0ssT7oFO9x3IoctzUPc2PD5vF4y9PN8GKm8KBgdg4AGx6t4ghShA4FPAMo0fPIibwwxkpk9t5Up5xZ4au6XEQBHblJYsV0EJx1whnCz1tz1enP9e_GiRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برترین‌گلزنان‌تاریخ‌جام‌های‌جهانی؛ رقابت برای شکستن رکوردها همچنان ادامه دارد، اما فعلاً لیونل مسی با۲۱گل در۳۱بازی در صدر جدول برترین گلزنان تاریخ جام‌ های جهانی قرار دارد. کیلیان امباپه با ۲۰ گل در تنها ۲۰ بازی، تنها یک گل با صدر فاصله دارد و جدی‌ترین مدعی…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/persiana_Soccer/25371" target="_blank">📅 18:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25370">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9gj53_q5yyry9-fN3nN0ico5zvDajE4eIKxfAMX9l-B02YZm1-2Lzz_d-fbysdAEAtT1ZoKWidqCAR71t-wVtcYXeXtQfbdqIg-UY5aAi0eiud8TfWZ738v3-rbNmup95J-1Fe6JgPA8l9CrKBtG1RGlVk2Lx-yUf9cZRMjzIyDX4iAOmW84CHx8ZIXSH_7BDj6PWGAUa7X_WcStPLOG92QZRGh1qri_Z1hAmDFYRVWi8t4FgXBKsxv2FgOlf6VWG2MFXUm0C6C_qJMCczbbZZdwZX0lsLs4x6xuiUZRsx31AEw1Kv6ZONmHpLx7F_U7LNiW19UM6mPULFVePbluQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/25370" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25369">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHHRdTIFgR71E9FumqwYrqK55ctAUq3QZxqYYKB_0AX7hwL6BaPY_dNiLigMaTx9SmTngIC_-rpEO1GY9as9KbU2HGKna93vSRiyq70TrXN1vYmQ0kjgrXeJc3qnH-i8P2pgJ8I4btnDmwD5Ta3xkyuk7ItzxT08XrSaABaMEGIQv9cvqQHrS9LL5kibMHg83A8GEZg7vgcgVcKvAkLywH__4OuJonqZqTGdDZiHEcdKbh15u6Y3euC0X_BGFIeYG-VU7DlwFAOIanaHMH3PyDb_5xEI4x8nBMrVr3QnYHhpI_xVrlX8BxnWBK9n_y1FUhr4ktzbaAhsUp7TsPBJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/25369" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25368">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqpBT0rwS8c8zYrJfRD0RetmB1LQBjIA3_7ZosRw5ZB-kHqoWFnbVhp2FMo7VYWC9gQIWb1xWXeIl46a1Kc-5NbD9_ne_RGVso2y6ImLNXxNLpirP0QPjrm12LC9gbv97Pwik66GMpUnNaHMPvmB_TV0bJ_jQO2O_gl2MmDibpieoq_0opyBW4-MFCCqF4HoFpfXD9S2TL3Bz5jt2Ih_iVaZyA_4Xw1Vu8GfQxJ7g1momgK4oti4563ElAl-bwQ4VqWHl8cxzXbK_CBb0cgQvnussE6einqkQj0ewr6dkRpvbfXUWqML-eHlwa7aw0oDX2hX_xcFYe5W3FdDnF-yVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌توخل‌به‌بازیکنان تیمش گفته در هر زمانی نیاز به رابطه داشتن‌میتونن با پارتنراشون برقرار کنند که جود بلینگهام بیشترین رابطه رو این مدت با دوس دخترش داشته که باعث شده بلینگهام غبراق‌تر وارد زمین بشه و برای این تیم در جام جهانی بدرخشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/25368" target="_blank">📅 18:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25367">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVYl2LQl9KmD63vP5ikxA2_cauwvK-o-L1zyUBJ4409QJ9E32_2LexFOdjsY6SnTGXo24Ssm6mUdRF9oQ56ikePyVFIRziY0HpPb5DJvGY10bEXCFTC0E9udRzG6-dr_zntyy9RQGtzRgmtOklY3h3CWdkltpXj1iYe02Re8_Cj_H7A_EYBY7eqgDxkYyFh3j-Pb39vcrFLvMnwm7RxnliF7nfRGvKGhYTFTU56X_WCzhvIHjz2LBlJCBv0AzNVz64zBVoIn2indbqrXhpNJu_1-A1lpYXJSE61RfFgNWxmuoYHdBW9cBoOVqow7jPhQ6eayeWnIQH5LFPlk8b4qXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/25367" target="_blank">📅 18:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25366">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdCvWLbE1sf7jeIynz_YbPUCd7dj0UwAlCk09pHPw1KlzApYWsQRPuHHwVUEuBuIVg0BVByKwVIezhXPMYpA7vOVRmq00MDST-1FO7dUp9nqKkJwzFV_ctLUnVVugBk5GFJGWh1oX85dboZplUZt90TCCWMeeGQ9StgBl8TAGr2j9kMnv2rf8tsiTJsUAxUMUkEGF73tvplia3CwKDkEQFaEkaQfy1v9ZyV3AU6zFBf0FIEbvYc0IIXe5ATrxTq_r3DmV7kgiLXLTHwC5UnVKvZYwX2W4-RTJ6ixwHPc3XsrVX_3WYvASuZxbjUiuLtls-EqYXL7iZ-S0RS9MaS4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
به احتمال فراوان جام باشگاه‌های جهان 2029 درکشور قطر و فصل زمستون برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/25366" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25365">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnRXMh42vrZyUHVzHslSQvW-gTrbf6eg41Sq1CHUVa-ydnSSwnvlDU2qxkkroNLI5NUE2nWnDMrLoq6G9Ar4YlHLZBbkFAOtWP27Fv09_RdzNOPgoTG2LsC-mg2QAhb53SIPqyaFv2zklxr4-hgZvAX_ku-75KULH8fietMDur9F26lM9DB9HyFHQXNckqnfYeCmKwA8YrqdOt9HWdhwreNckwOr_LkKfMTypAL_RBLmYVwooRh4zR9-OA3Z-vKNSUXWUnk4BJmXha1i7kE-4cHKM_rPWFK75uC99SsEZcaV5zfeTfBETagMzMAwpABiXJb9qWHB9-9KTk3LX3TPnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعدِ بازی، امباپه بازوبند کاپیتانی رو از مانیان گرفت، بازوبندی که خودش بعد از مصدومیتش به اون داده بود؛ الکی نیست بهش میگن دیکتاتور.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/25365" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25364">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ohnPCYgumw_Euy8KoA8Yj0tsfmD0vbhQEB-PClghLSg4lqPCyDsjGeDcOTARTs7G-d-Hq-5lek9ZScM274aeHCX2LAGeuqR5BMVyARCvqZjITVI0WYpWlNBQ4sy3jNOI8ShRzlDW7PpqxvRs24T-tXtwxmsJwPpm78t6qGEgPFlRJnExICddY9LN0R_h0exSVZhS7dHfWuycxFa8HM27s3N-hwF2VYszMy4twr-RHWMqu58i7MiFoE70sdcdLLzAHHLRh18CWot3FGwnD7qnqAG_xvRZp1t4-3q3DeeIlqqP2aMMu7knIx1QrZBAuxwLnUxLkq2D1Egg7KTOdglDng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
دیدار فوق‌حساااس
اسپانیا
و
بلژیک
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
▶️
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس جهانی پیشبینی کنید!
برای ورود به‌سایت‌فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/25364" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25363">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAaVZwZp7iLZj7TCkO9PsWZ3ehw4ibxPe8ek_WjqpJU_Bao1ODSuAkNqayM_sMUk-CDsv_8NptwacT3rG8GNbHFCScigHKEQu5g29SWnWjhUu6k0SSDar2QhOJcXRgwjWef7_T9LGspZkDoXxxiIRGuSFXeL3eGEA06l4oawz6gdos8iXKmXc3qKMjzvcbslZdsHTtJ5MSt0Y44TgLiUHXITx63p7RjqptrQvTqp_dBWWnxrolxnGn5HJFKplM1CrFIAFmwjDYidjhkeJP9ZVyuiG6aDJqb3sMB815dIphs8IvkB-xoz2D-XuL2CV1xHV0kCopfsGHK6t49Uj6uDRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛ فرداشب‌فرصت دوهفته‌ای باشگاه استقلال به‌محمد محبی به‌اتمام‌میرسه و این بازیکن درهفته پیش رو تصمیم‌نهایی خود را خواهد گرفت. تابه‌این‌لحظه آفر رسمی از باشگاه های خارجی برای ستاره تیم ملی در جام جهانی ارسال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/25363" target="_blank">📅 17:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25362">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0Pw97BBplcLHo85UCDtSwd-aEFpGcY4bDD-Vu6efnjCrxg5oNz-cxeFgGz_P0w1h7ZhEFKfh4AeAydGWqecZ5hxX8EWuP9a8piz2cQL2n8vIV_mrPn60VshSC7QslFf-ONq0QYjPwxiG8tv0FKmIhsCCL8Ph-S95CAMUWmG77mWK_WUcvJMFlC_wcg8tfYfxif7CLBI5_WS4q2UWEfyGDcUGWaiIFc8HTEoeSycNsKogSy0uZ1KiRwyOlhyU59Q5f0xUHxRP9GCnyN5MTzglXqBjfkqYZ0tQ1ZZ5HRXH8sm0SLfdmBd6WUx_oLjRK2fZjxZGJWIFuu-Q-CKxJD29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇮🇷
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال امروزصبح باردیگرپیگیر جذب محمد محبی شده که این بازیکن ملی‌پوش از طریق مدیربرنامه‌اش به مدیریت‌آبی‌پوشان گفته‌بزودی‌برای‌انجام مذاکرات نهایی به‌ساختمان‌باشگاه خواهد رفت. محبی گفته اگه تا20 تیر آفری دریافت نکنه…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/25362" target="_blank">📅 16:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25360">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDt6snOSzH1kQ4wi8smsJGwbBYWrG6rEvBvJS-1c1bvF5uSA3ch_PhxUGjUzktlZ9O97RZxsHGUiS-XsrXrY5deOv5szzjuiVDm6C6YP0smbdg_T8VdzcxjP7nd9cJlzhgag5pK5Hn_XkNhR4cru664fm6y-DgCKCmMGwbOdZf1OGLo5EpqAxpSoIF8tZe-3md-s06I5YInw04F4pj6q2CwKZ6ZLctzp-7N5U027vbYS-CFrHvtLkCgL6oGPzeXok9HKKv6q2a9EQ7s1ebRr04aPQ74bg_e_wMWJ3JsHU_aBSpQrXcUzf3_uX1h6fYryafbmecj08z6kMFMNMzk1JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مدیریت تیم استقلال بعد از این ایمیل وکیل ایتالیایی که امروز به‌باشگاه داد مذاکرات رسمی خود را با گزینه‌های مدنظر شروع کرده و با مسعود محبی مدافع میانی 21 ساله خیبر خرم‌اباد نیز وارد مذاکره شده تادرصورت توافق نهایی با او قرارداد امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/25360" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25359">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqvNrUWa9zLCqijb1p_4nQM_9R41WWLgxVGo9zW98KWNcBgmFy8xtiUUiR2pHUQylFV89O0nW8R7SmcpTcVkF0ybrxxXcNTrvPUBUyR37pCpNIGQ0zGjjMfBNb3-B2qzoXV4EMWoEJ_4P0VyXj1la_yomAkxh_spDPPCbpX3Isq4j9Ocv2jcXKZW-twEaZgRVNu_4YTdaHmMuYpWcJtb55kZ2rs4Ci_qA-uBbNHfRTc_AbVfaaQ-yRhFHG7ICpgB22NUtNBFnOzO2rdgUVyITNY9oFAvTgvGXAMNsH8ektobksvOaONNFCrrPq6MWYFBT_t4hUNfaPx7RlfTYuvnRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی که در یک دوره جام جهانی +8 گل به ثمررسانده‌اند؛ امباپه و مسی به لیست اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/25359" target="_blank">📅 16:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25358">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇵🇹
10سال‌پیش‌درچنین‌روزی
؛پرتغال‌باشکست دادن فرانسه میزبان تو بازی که رونالدو مصدوم و تعویض شد موفق شدن به اولین جام تاریخ خودش برسه.
🇵🇹
رونالدو درباره‌اون‌بازی‌تاریخی:اون‌روز با اختلاف بهترین روز زندگی من بود هیچ جام یا افتخاری برای من به اندازه یورو بردن با پرتغال ارزش نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/25358" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25357">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGdpjqhm0a3mztTx5vdxE5UTOtx-bvJ4ZCcDm8DQmhxRvRcfVEZMjxaWN1hZ1vkN2edWjLUGXi-9Aqwqh2beuvi2ZShyuqvD5K4oErF08IczvfE44qykW9hUqbPHNPEICC8HAALDTRyfOZT-QxQ45vKRHYH-CHud_kBE4hLKw_UVU6_tDX1UjC6oClSbAk9kRk0F-d1D-qANqg06hKGRalPZi-ARYCFFt3Sh68iB3iJ3-y4LwB-e_xpV5mC8ClpChzXTL7u6ZaPUeMDaRfLNPlG1wdi9L2VL6-PwlICkqVpjGAt7K_ZCkNkqxqgH-P90L60VwG82BYDMzglh-DTHjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/25357" target="_blank">📅 15:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25356">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=lUYGlGUb1h3T3T1ziJFqZxJpbonp93yv84nLlLRD47yLI96iSvYwbPWxQYkhlzjz6PSsN_h3ZlROF7hwQtB384q6GzYHO5cb_uQVqLrAXlSGtD9ir4LNjOxVbH7ejmyGBa-jIuDmB7iC2aF64EAmyfawcjn8ordNz4vAVXhmlRNlKf1yL9GrD6_QOap5NRD6uArO5oxNkcyWakhjGkybSSODIGNnE7ZAeFuCWFR8jb_mSu5AYxnKuhUAeKiKlDvlb4tiraJOQWWsn-eiqa-WjCBFdMLEkeGL6Uy8a467n303I1abOPbk_M64DSIP5hvAUOzn3w1o9yQmFikmMPtz_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=lUYGlGUb1h3T3T1ziJFqZxJpbonp93yv84nLlLRD47yLI96iSvYwbPWxQYkhlzjz6PSsN_h3ZlROF7hwQtB384q6GzYHO5cb_uQVqLrAXlSGtD9ir4LNjOxVbH7ejmyGBa-jIuDmB7iC2aF64EAmyfawcjn8ordNz4vAVXhmlRNlKf1yL9GrD6_QOap5NRD6uArO5oxNkcyWakhjGkybSSODIGNnE7ZAeFuCWFR8jb_mSu5AYxnKuhUAeKiKlDvlb4tiraJOQWWsn-eiqa-WjCBFdMLEkeGL6Uy8a467n303I1abOPbk_M64DSIP5hvAUOzn3w1o9yQmFikmMPtz_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیویی‌ازکریس‌رونالدو
🆚
لیونل‌مسی که به پر بازدیدترین ویدیو چندروزاخیر دراینستا تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/25356" target="_blank">📅 15:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25355">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=LL1g89JSDtZd6Za2usVjjjrqJ12aOaldEpdrUDyPh38iHwrydBESAxJ0opTkgcCdBiCAxh2Rv98TLuKFGyVHSKBkaePhU80TWk759PCw2rNYmIB-g4_MUHyjIXq5KRl5mJjJJVjZCNZcFqaxSehg7N7smJV105cgUL10VzUAYHUhmFvRl_86FJh67Xc0NMAvy9GP-wfiOcIceDa2AiZbH0SQ-X2QPggEU2JVWEZebci1QOwijDt5pBsYlKi1FbmGYtHMBqfE-elqfNBRkQKBZSGZkMkg0cPlng-QTlSNrR9a9OctASc0ptcXG1jB0ScY89g5BYwsx421FFvoqkWQag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=LL1g89JSDtZd6Za2usVjjjrqJ12aOaldEpdrUDyPh38iHwrydBESAxJ0opTkgcCdBiCAxh2Rv98TLuKFGyVHSKBkaePhU80TWk759PCw2rNYmIB-g4_MUHyjIXq5KRl5mJjJJVjZCNZcFqaxSehg7N7smJV105cgUL10VzUAYHUhmFvRl_86FJh67Xc0NMAvy9GP-wfiOcIceDa2AiZbH0SQ-X2QPggEU2JVWEZebci1QOwijDt5pBsYlKi1FbmGYtHMBqfE-elqfNBRkQKBZSGZkMkg0cPlng-QTlSNrR9a9OctASc0ptcXG1jB0ScY89g5BYwsx421FFvoqkWQag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/25355" target="_blank">📅 14:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25354">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-XymLA0rXiPAqJw6Vs_eXKndH0rUpsSsqZseVgMAwSYUUA2aH3JqHlejbZ3ihRUuGBX7xs58FMDZTpAqwZjKRPcAsM-k-kb6wZEFrkvpLvFbKtDWAk3P5mt4R-fg32fVmWS4I7vSkvnsE7Ro_c9uaWHOAP6cR_MZAKslb6o0SR3bDX3aqdjt4inr_414p5jHYJ8-__vgP0MDEykCMD4FXnmxIn6ehqIa8agPINHPGuvBawW5VodYZILFJS-_CstjoSO7EIffaESzG8ws_Zm2fqZ0mH5nTpwONrlUw2MSdmu6zknV6xHDHYOflA6SDqzTMKwMFaaL56SnoeKINljFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
ابوالفضل‌جلالی‌مدافع‌سابق استقلال با عقد قرار دادی دو ساله رسما به باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/25354" target="_blank">📅 14:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25353">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoohAQJP7iP0aPAl9IBVAb2cO35qWPYby6QELzDjcktNxS8_M60T3SmOKeuOr2V_9JAmLPht7ugoItQn1Cry8ceTaaOBlge2tcLuv5NzO-JnQoPWSVaP93038JJcBHbuAoN1e2kCULv4Gz92AnBAI_mnLZ9k2CG2c21rdsjemM_dIoKVGgwyWANDrHPxDK7PMRRQUkeQ3PKdYJGDexyQDfJESU8iy5GwfeINLQ60IPkNGZO-yp6E5TNQofNRz5EUqVB26dHB43ad9v_UmXZouD-QRAx-it3U9u6vcG9ofkhrFnliaYvk72kX-1P7gkYu8xkd1ohXjjI1sgxg8B9ZzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/25353" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25352">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOA9gG1o2zhW0yfwT06DSHxEiOBsBxWx7nALrAy3pL4OK_68Px94P9kjPKqvhABnCrZdnj-qYodhdWwoAZyUqDt038YJ_c6HKIpIEqJJpaXhLWmtkQOer5xnx336pf5Io72ftnZRKpfqWVpkt96X0TVkgxQ8HmjDxfQmZHItUWQhSaUiyh2NtzGfnSZC2Z_BFgUzEUqfsRFHFNTb19hoqu-l3KYOzjQ_9IHzJzIbFBYJcvSg1sKm9EHWtVWHi8YUepTM_FY1563eA6dqpNaI1VohZzMpHHlylt-Usl6-t6LuO6aflIiHDdfm8bySvQGo4NQhpkJSPDW4UP48XGQFyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
نماینده اوستون اورونوف به مدیریت باشگاه پرسپولیس اعلام کرده یا رقم قرارداد این بازیکن رو برای‌فصل‌جدید افزایش بدهید یا با فروش اورونوف موافقت کنید. مهدی تارتار هم در این باره به پیمان حدادی گفته اگه با ترابی ببندید مشکلی با فروش اوستون اورونوف ازبکستانی…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/25352" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25351">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjbceL5nbJFzaHeR-X_0sIiNPAvHOPoFayEZ5Wvb2XAGC-p_zFBrCcDg4oePR5oT4MGmIzW5rHGgl1ZrrvfWqzgrU3kN785E0yN_kRpDvGSmrPMHQLsUvyswGcliR6JRSRUnPYzmjyeV1-20kD28Ks6PMkeBHAMsH-CiVBFj1MSwYoCk2W8Gt6-KxviPCWSF6w1UF6Ca4ACFXK8dWLLhmi51pz_ySkvgworWx_AjvE_V4ymSuHiXEOrDfdYtCvXhrztgg0Rdq5NScAHaGhq3zf67ClA0MWeL9HGXja07bJDMj447RpUyGlTYr-5jl8Cwo52UOFJe8K0Nfzq6LtMinA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25351" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25350">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVjrPLcUGhViC4Xdn3s5ljrZL4hhHzeMof5X1euJgBUjd_I3Bln2FKQmc7ibm5QnuwHma4uuwa9jEj6vJPiFcS4UbFv8Iva348eBUejd3LgGXLTbF-8nyHvGtXoKWfHsaW8AVp0pFGQZcVoHX4K-edRDswU6sAPA5x-ZgoKmIX2ULWPkoniSL3-cJswEPWkhreQ1DEUThFgCPJpYeMgelzoZmGewiAMNQdLLIMg5KYCbjMrpuKoB1CX_7E6OXSWJA9zPOZg3zWGCg3i8FIebTn3KLtk2eGreGst-b8zMzXu3aDJ1xxdeL6he0Fw-XLZrc4XQAUji4YAM1ITtXFRBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/25350" target="_blank">📅 13:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25349">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VR4u6ejCdOHPKxH33cF4bV4Xa3beSQNhD_XVhLXaiWFTSRx20JLkVgp1WE3wCQIn5cNwbtyK7SORtRG8g3yC2B85V56JjQX2E7WrLV05h5LgJJK_YdxFZNTO7-hSLYe8wUE7k-JTL1tyNbPDZql7GJY0eD6-EOMKa4luNwyhmHBRBqQr3CkegRswu_07cqgzWk6BXJMX7WY5OiPJml4-TbdUKIruE_-LiN1zadUm2xbBgFBgfCEPQfHvnODipNCekIsAcjLC0GuwSsaOHmVlKxzQIs4IEfgNEabAJxWkpJ1rL8PNiz7Gw0E3LeqNQ-Yd3OQWYF-4-o4kwr8rjU3CAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25349" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25348">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBNkh_stvNK6hNnSBABKwqCe0lHryqqwP9BiY-0UhnJJCO_N8lTZH2vngaKPwbRk9GKS_oh3_i4-Ev2f8VKaGX4MM1l0GacutDW-Ahk1vFwtkTYDJ1ZiEwz6ki3JTNQAlR9fNgl6RUedio1FuLVxrSI1y3KWilsIM6N4FZEp8Y-IUpjaxZ0mcQPEhaxG2MYUdnla5ymY1jguRGfFBf3jSwV4pf58xWRCaV1odxaAluGkf4XKHjIxqa1YucmugMykjaYFU20ksvqobkPhRx-jPlU_ifdPZwJcDwKawVGw6iz8xu2ejma6biov2S_eY1wH3FJIFmQJpd3pzHiVwC2uxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/25348" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25347">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN0kcgVjIRl0N9OXtFFAKmrEFwDooGG85X98Ks-kefAaHj-Kcukeq6D0d6AFou3ZncXK893aTL7JEhagGmlY7NY2lE85vJez9AbHC7fg8eot2AO7yrhZOq7VFDhSTlUWxROMeOHqWKexeRJDYFrJTBEJ5celCP1mhTb68JCTPyNG9b5RpI2L5Q4NwF8gXiSX0wNKN4EiLZzFp5HVQ7WjRSYv0H0EooRXu7lTXMvGr2LM_uRDdXoMPvGFAEYCA595CONeFnGEGULULIUOy3MsLhDAhiRpl-gbgmHxGf7r8OLSTEMl9P7DczhVJr8pxDQCWAIbedeW2H73e8IsijbbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره استقلال ازباشگاه الشارجه امارات که سرمربی‌آن‌مورایس‌است پیشنهاد دریافت کرده اما به مدیریت باشگاه استقلال اعلام کرده درصورتیکه کادر فنی آبی‌پوشان به‌سبک‌بازی او اعتقاد داشته باشند به قراردادش با آبی‌ها…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25347" target="_blank">📅 12:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25346">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">📱
اینستاگرام دراقدامی‌عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند! اگر اکانت شما پابلیکه این قابلیت هم به‌صورت پیش‌فرض فعاله؛ به این‌صورت آن را خاموش کنید که مشکلی پیش نیاد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/25346" target="_blank">📅 12:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25345">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmABbc4rhwADA5JBexbIQA3s3E8Kyz2_sMFpRiYGJvTBjKDSQniNlYWs-mjp6Vl4oJ8LlDaQaFUMIXdywNOttzIMmR29ABgnDuQUtCaDgPzVVHUBGkfL5PtV80Oul46F2dp-hfi9FvvjFOVJkHsrvTLOEjNTJZpjCNrsRQp-nyH7gRdl-mv-YsFXLsthCoOsk3ZSt02QjCRXYbDB1VTYrYFvKfCEI8JhLRfjbw5voOrlgO3aU2Og83D4CahFvDabzcRJDwLPnTylIcwXlDZQ9CnNQarpYyJ7N-aUw2O8mL68c9reppUiiC-1JhMtWEBM5rWw6y9cE5mgTJrCOYsgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25345" target="_blank">📅 12:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25344">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1IIOYSsnNm6eHigd5uFKglqDxNt-UzEw63oAQWvdmqIikA4FO8jcPqiFdLebjIK_PAWciAtXoN38xlUTfvrKeMMbF67wCYtKRv1B080XIZsQPs47l_MsJORYCMm4SpXXt6ZgEYXCY7xOdi4saH7KGFBkfi88Y2FpQPSAHgPRNg-b5twkMl4usK3dzLysok21RI5QMrt2f8-S6m93uDvroyL8ucRd2Uc_V5JMilc9mA3WtBndxdYXAFij070KsBiProwrIFVIqlPtr01-_1iaJ0hQX7vLG7dUr9vXwP4lqQzuLBkrnPDAnLUW-jlqVHi0BN6j35jxfxStExkQGBwVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25344" target="_blank">📅 12:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25343">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c669eea570.mp4?token=fqRwsCoiAW4NWqCNvkA9BeMLJPze5flfmfHWpWuSZrzBM-oWT_zNgz-Lj0oFeTaSiY8QOUC-POSW0Xasod8DqAvWxVs-xskRbzOZgt0BwkSHRzy2_V-1tOuBreeJZr5cqa9QL_BiEckhL3O2dsDxDtCqjISFO6HUx_klgzO4ejd7VwYrC7Og8xYKHeiBgp4WPez8mwTFD0bhpuIfmqMm_gw_gxVcmfWvGpLUBhAwAfbVgaDg8NNbnpK5Ci37zIymOq2iO4nZojtnOgmBpJEkxx6xSD8S-ilIRO9OlIsjp-ITqzgj7le0iprGOtnX3roLakFR9IpfsGZZqKwI3C3AArUvAFAUU4LxCpW7izg1hnJ5skceJXDZCIS28pj95ThrUuusPDzv56kjx6-_BM7b9ye9JMy4B1Afl7Ad06xB9XYblM6H0YgRpynMNFrcvXVgUOwdN3KSXJqI_iYZWX4P6FLq56ySF1aQDounzlfxk5O7oF6pQvbC8eZnBRI1NaNzix7bVo0_tscq4JkhehcxPQG3vQktZYRsT9WEbX7UEFooZG2wF9o3SPb2Bg2TMFqQoUCiZdTm1qwwTK2lW7zULzgVvQx6zw-PzMgAys28DAO1s_1orDorN2aV9jDx5MVBnOaS830zLvtQoRr__xFSRb12Ky01Z3Y4J7jlGZAn45k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c669eea570.mp4?token=fqRwsCoiAW4NWqCNvkA9BeMLJPze5flfmfHWpWuSZrzBM-oWT_zNgz-Lj0oFeTaSiY8QOUC-POSW0Xasod8DqAvWxVs-xskRbzOZgt0BwkSHRzy2_V-1tOuBreeJZr5cqa9QL_BiEckhL3O2dsDxDtCqjISFO6HUx_klgzO4ejd7VwYrC7Og8xYKHeiBgp4WPez8mwTFD0bhpuIfmqMm_gw_gxVcmfWvGpLUBhAwAfbVgaDg8NNbnpK5Ci37zIymOq2iO4nZojtnOgmBpJEkxx6xSD8S-ilIRO9OlIsjp-ITqzgj7le0iprGOtnX3roLakFR9IpfsGZZqKwI3C3AArUvAFAUU4LxCpW7izg1hnJ5skceJXDZCIS28pj95ThrUuusPDzv56kjx6-_BM7b9ye9JMy4B1Afl7Ad06xB9XYblM6H0YgRpynMNFrcvXVgUOwdN3KSXJqI_iYZWX4P6FLq56ySF1aQDounzlfxk5O7oF6pQvbC8eZnBRI1NaNzix7bVo0_tscq4JkhehcxPQG3vQktZYRsT9WEbX7UEFooZG2wF9o3SPb2Bg2TMFqQoUCiZdTm1qwwTK2lW7zULzgVvQx6zw-PzMgAys28DAO1s_1orDorN2aV9jDx5MVBnOaS830zLvtQoRr__xFSRb12Ky01Z3Y4J7jlGZAn45k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوهی‌های‌بامزه هاشم‌بیگ‌زاده با حسین ماهینی دو مدافع‌چپ و راست سابق استقلال و پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25343" target="_blank">📅 11:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25342">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLGO_WDIU_a2pRpio-TbGNFiHu4DBhXvPDzR7jOmFht9xvMcEQ9kx88zkh3foOCpcCZOlU_MgPNonRY5uzq-w95sMxJ4c0MdnO689WAX3lz28c0m3509cPZUVij4rxB194LAI2jCuF_S6I0xTTB76Tji_CBXU3SEyNJBSdW8r3_srxmXfjbu6EgsS7acgBNM3mUB_xt2AmvPrN42T2BFp0Sc3JPS2gpdwi-i712t9X2C9KSiXptwYeJs-oGNCj3pEvlCdKnC1t5odXhHHTKZsnv21Jdmd-7J9L22A6iVTZ3wmQ9T1pZBr8qCKKct5fOAD416YC55omYc75Xdv_ULxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25342" target="_blank">📅 10:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25340">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQDFW3jZXZI00GUoNnZdEKwdfv79-T1o4mNc9DkSEKSPfByQOP2DYRYYFgLzl2Izz-Id6sPMwNE1MOX9sEBHzfFQ2vtP7VaS6ZQrIZGdZkFx1yVmAKAcv0huYC7tggTktqGTbyiEI6Xu_BMhJ5aKvTqFWq0O6PFYku5-EAs3yI0Mmv7LpGpLrNRkNx_bkS7Be4UFtPG0J7Wwaeu_E1oXUKFjtwjsyUgWiQKsrE3adoEUBRtiHU_dhQ5W-C3-1RGoH1aj4ywoiXXe2ps8lC7ea8oAJnDEkLN8LPlEKm1X3XOmtY3bA_kYiWNTn9HEqPsSIT0ECKogxEYK09SLr3sq9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی جدید پرسپولیس بعداز منصرف کردن پوریا شهرآبادی برای‌رفتن‌به استقلال؛ ساعتی قبل با دانیال ایری مدافع 22 ساله تیم نساجی تلفنی صحبت کرده و از او خواسته بافشار به‌مدیران نساجی کمک کنه تا رضایت نامه اش رو صادر کنند…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25340" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25339">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnbfHlIyBs5xyjR7M1P-P5HaIYSAkGbOoYjdAn0q07soGKIwcv8OVse2ztTYgrwFSqWIPcCAcoWDCdRca7-d5dsbPSwEVAZ8IfU_X8r5ueMSEt-ax7PG7QjoU4P6O6a3MqfXZzABiVjGHj6HZW336B7e02Yssbz6i0nyF0pssKKwm0KAcR4kKVZxIdludqi1UZTmJIDL0DPs6FwET49t69uDW18ScY3YYfXO8nBMv6zrb2thsm3iNiJj_FnmGsYIX8d-DfhIzx1d_mPZRtkClIdjtjMzRKvC8l6jw6X1OAX_z-ymHxC7mpvIKYEQhZVraj7ljVQWrix_UtSFAsDnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«وزینا»همبازی مسی میشود؟ براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25339" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25338">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45277758ee.mp4?token=UHIG_Ho7NjTA7MHAHHgp_NLI9pNqRooaDkve0A8nWO8mUCvMz1Kr8NsnSxRRZ5iE-O2vwm6WpqcW6alhndh6gUbvI7ItECayTjOxMDUx9ceDmd1MsemP8jtlxQLjlL-BR6PjORDDInFe7r0vLLD-dG_iPJFKzpu1cGtkWdbFIBRw4ujBM3dn7K2HeZQ7409qChBy0oVcmoOC-iCqk51T_xf6M7IgEan1qblp-dR4In_NbqMVWEyK2uFTvsNqn0lTSjfK9DNaiqusAPOzki8EM9MWj3MJL7q7fYSahnbBWi0i3cV1zjOiN0wgkYiIGj8Iyhj9bHlEPcm1eVoZnQmU5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45277758ee.mp4?token=UHIG_Ho7NjTA7MHAHHgp_NLI9pNqRooaDkve0A8nWO8mUCvMz1Kr8NsnSxRRZ5iE-O2vwm6WpqcW6alhndh6gUbvI7ItECayTjOxMDUx9ceDmd1MsemP8jtlxQLjlL-BR6PjORDDInFe7r0vLLD-dG_iPJFKzpu1cGtkWdbFIBRw4ujBM3dn7K2HeZQ7409qChBy0oVcmoOC-iCqk51T_xf6M7IgEan1qblp-dR4In_NbqMVWEyK2uFTvsNqn0lTSjfK9DNaiqusAPOzki8EM9MWj3MJL7q7fYSahnbBWi0i3cV1zjOiN0wgkYiIGj8Iyhj9bHlEPcm1eVoZnQmU5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی بعد از دیدار برابر مصر: خدا سر ناسازگاری با ما داره. شایدم خدا داره من رو می‌کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25338" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25337">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEdXilpWtSSQ3saVbsamFzdS22FM_pjxkqsq12he-XPJvwiVlG2_vXcWcoFAjA1NzgEXHa97oo2npC3mSntJY5ew-R8lq3YL7q2BaF41vd37LFpp0KeTeUVN1lkzLoqvgEUn3oHNi22DcHMiU4LSANy4JRvIhY6A0IejgWh5E4KnDa38UznogVvfGxJKJ0uf74Jv2cm2Qxkq34KsDrU2lfIlU2gdHMb6WhWgmFgpBr7wEa-xiFWsAl1hcWxAz4uSPqQUtKP1DDIy7e2KKv8hGdY4lvambACuup5yMeEXpOMLh5NYTTFBS4MIARSfhdJOlK8CZaoSrvjdX9jjNTvHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی
⚽️
⚽️
اسپانیا
🇪🇸
✖️
🇧🇪
بلژیک
⏰
امشب ساعت 22:30
🚨
ورزشگاه سو فای
💰
در صورت پیش بینی اشتباه مسابقات جام جهانی ،
5️⃣
میلیون ریال فری بت دریافت کنید
🔥
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr19
📩
@winro_io</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25337" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25336">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NL8jMqpmbwp_hLiytT5NL5JmedkcG0mlthckqsjXJ4vy3TsCOZlIRZyPdlnYlFJeWHqL09n4xQIhPn57Sdr31FDKOxFt-Z_Sm84fxcsl2AzpRAmksT_Yi5tmNm8UllCuqLeQjvF7NiocB22Ok8QZ0eDH71nnw6eTx2wp_HR1jFUnp0oInJsFTygEnSi_UlNXnlNoysjm8eM44nH1weMbL4fN0GbqLi2Oyk4cmojIW2vBrD3vW1iDba_VdkJncnTsg7j8XvmgtvLNcs2PhreB0WFMc5gkzkjhTICVkk_T_IgciOySWOIW7gbUQDQ_zsBsr6l20h7wvAS94Yl5AabbqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دوستان میگن امکان داره مشکل سربازی مهدی ترابی برطرف شود؟ باتوجه به عقاید او و همسویی‌اش‌بااین‌نظام بله یه تبصره‌ای همچون تمدید معافیت تحصیلی پیدا میشه و خدمت سربازی او تا یه مدتی به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25336" target="_blank">📅 10:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25335">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sES2dzWw07tQpPgCa4YOC4UjtfN7JO-IChEnyx5sCnSCQsDE-VOUZ8tizPxA-0nsIOmMMt_gAphO4Krz69SfxkXRzsXgMmawI0hCHdVhDjrCFw3RSVE1FCH3oo3QOf9oCTSW7OntOCSG2kcDYMwntI4YYn0SuIIzVtq291rEzZxg4HrXbjql4a-EroIvfenew5CZ43Z9kz5zlLg0cKzo69wDbpxUrU5zL_iOfInroEHhjkMRbJp5B6r8viIEjlp8z9NpOufpgXRa6T3bMPKuk73pzAntJzWKLeqKcBxGzjbd99LhS2HoODyfxMOWG2n07LDk7he7_EXg9XHcu6rC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
ابوالفضل بابایی و سروش رفیعی دو بازیکن دیگری هستند که بااعلام‌رسمی مدیربرنامه‌هاشون در ترانسفر مارکت از جمع سرخپوشان جدا شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25335" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25334">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PM2uc9qT6d2i5OMm9bKSsf3iNPnFQxxtpAAw_OgMQ69-q2rZOXKkEOju7vtoUqtP37I6FHz-kLXI8QNr3cXy0ZCDRbyikdBmPH74RJdnaVbjPfrQm97Mq92y-VLiZvF7rsIU-UsJEg5g9UOe0fdMSgqLISOvp8vnRQV-Pympv1tHKALPA2QynkZvFL_T5rJRl_gQvi4X1ewx-VG2Gm8UHha_6M6r3sJaYFAv5XOaNLWtNlTpVJPaz9vnutIQr71pG6XLZ3_rt1Xi03dZ7GGbeMw60PYho28fMMsCetoeqnnwwm48B_cYBEt6lfW_rcDTiQiuU-qbO_A0ngcm1ayQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25334" target="_blank">📅 08:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25333">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyqZRwNaWgoIpKhd_ew3Hda2GUA97pQtGtaNAtk-rcLfPRA43OOjfvS7--WQdPXBgoR436mlyi7cdC9m_X4G9uOBYAa_0KDVM-hJdCg-smwIegl6z8aQv0BAIZ6upMQraFU7NRMmbyzwive8X8nzEwLxghJj1ZfQMkMQT5aNIcGwKtwbXH9VoMa8Z9r6lVCExZAFAcq7nF3lYoWbxLJlLzfTpl_MvvTAot2Addivs0_Q2v2t-7P3c8mABouVuyQ40lFSh6Te9eGEFUpB4oLbb0EYkVLxOmuR8GnJPKm-GxqAiLQs2_mqhZfEvGd8A5H4lEs_RrqhI0nWUDFcuIYuDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25333" target="_blank">📅 08:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25331">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jy8uf6VDiaUAetwkMJuGH26YnJt24UWfcT4RQEs1X4ww42SfrCEBKBX7-RAJDPhpAJQWYoxg0m76sLVqx4GN_LKI6q_ScKznbHyubMBapJZtIOdYLmjpZ2zjKOK8zwgPyJmNr4F5pu9bxRDLVlMOsl2XvHSbhvOe4v2cCwAOOBCOXGrQDwK8IIPbw9v6kpf3CCMf1KP4gTsdBBFxEOQ7oGyS2dZI0f3uF7q2LAeNKCT4xIBpVyS2sMPAJkF1t3iSoI9G4DkRlfq2chZ7a-F1f70FoGJSeK7byeqPs0bVPv4QnlFs9jdNIHEis89DD99Id2yaX931TA7Ll-FOh0_mew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0EaA1K1FyVVtH0wqv_xTFVLuA13iNZyeZb80fxfijF35GFFY6mkHW0Jv_XBjNE-g5wMOVzf0kjI3OYyUbEyzjUj_oeOOioId1kxYnsQNoVBzTw3gVvDYGal5ARdy8jaOBMpL-4L54wHadoFieZrrA6B3xfByaqz-VhhmKpUYn5gqgBYC7P9bjDJ5YDXqcf3dC4NXek1MfCLtQJjWOUrJ8mOczsThrxfe2Rz_VCeHEwKHIGQiYo9KEqF2dVI9JN9Q9abrZDphgCcC4S8HC96xAVRHMLFDf2vSW5c0TD0YTx3lkljaRyPjPjPQb_OTDZ0ej0jc2FxmaKcd4DFYZ40Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم؛ 10 سال پیش درچنین شبی؛ تیم ملی پرتغال با کاپیتانی کریس رونالدو به اولین قهرمانی خود در رقابت‌های یورو 2016 شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25331" target="_blank">📅 02:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25329">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INualOs1OICUr2htQAgE1LDp0vvqBy3s0xQ-d619M3JmbP0rYlV-3xpF8OK6jUCsOnDvFDW0OS2VY5r6kwLpzKzzuSvTAsSf3mx7SyuR6Gy7-Gtts65itj5_TehZOOTXSesj-hKoxocp6-Nlr5hNlyR5YClIpHBytejxuBlr96HYIdzYbqwSWatsMXLzh62KnjuhEfU6NMuSf1-elTkiNKEWXlHu7S9l5xayCOXL2rQ90t29qqk63a6q6sTuf37RbdJ21VfSWPNc8WTGwS-Kpu875OkL7P8TlcrSeke6kLAFSU0eni-U_4xL4f-9MpuVMcZ2ZINGLVvhZb-0ugUQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_ZqPyE2Tim9v5g7U2v2AI2zrMrESfMdtFnC9mtGcBKEbwdUkMa8fT-AWiBB-Y7YQp8GLbQd16U4CaArIdltKKk9yWJE1ZhXEhvFURZsMVrR6eGccY-BcsJyQQSY-HboVsuWZF29zuuP5k6bcN8rDCcHfoVpTH7yNRkY8Saq5AwMhDKWXe2JsFcIf7B0tgNcU7UfP7_GPsPEM5Lp78Rh54Jf8FvOajKikU1YIFv4FAaiqRY-UklJVqMRd2bxW4dO2XcvqilmpKLwXLSeEeiCSRrE_KnN5Zrhao2l4CfLEPoXNLWN1EnawU2FzJtT_vY_M9nwIX7ezAXhqyQxMC8glA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی‌زیباوالبته تلخ در وصف کریستیانو رونالدو کاپیتان پرتغال بعد از حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25329" target="_blank">📅 02:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25328">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnuYNuyoL_H_cL7bD2MTbg4_Wtb0mSUEVaEuMPlgK6Ufe2f818vZ_eHOj_K2NvLZ6-D-VbhNZgJDtMVlE7yHZ6UL12zxUeWyrRwfB9s0H-iiX3VeRQeDIpGKOj-sTRUCK6ar4bmTPla5iUbpDrrU9K6_ItbBhCB4QBcpxA-ys6cnpq7q8nb2rqXzZasBCDBjROs1EFEl3jAOAolPvGRWNG-OSAjRHcExrHTbqQc9QYfEuRQXD0o_CcqTcRYY05qEtCREFtjRIeae_ku6mtO0388Ps8FJ8C4rJYzewDHMQgcjQXSiy2jnyxYh8Ha0xcIDBiTgPd-5JG527PofO_Kg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25328" target="_blank">📅 02:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25327">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PI5WslbtJxvR3BT4A6U3IWJjFM70gKD8SoJNofe0STmHzryfJtUKnIRzXO6Q90S4aKYZWDMOJ_EUlZQbm7QngGGIKoIrt6cJoVSZaHGyy-fh8qK50WY1-u8r9ejLfRWhSL4qGmlNWJ9Eww3LaQFIeclU9pa-Iaz9om4Xu1Ce-Qcc6GD6ZDfXbWWobSjL2VGf8Uy2lQog9tjD4cujtjdL4ICKC4miIo9wIhw55GM2lOuGFy_aKSKICwFnq2bUI-AT481gPEh8D6vNKSL2L2cl0L6GBGgHM9zZNDj9A5EntMygpokxeRbl0F_Hfp1t07UJFQH2Jeitudk9pl9odYlH6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25327" target="_blank">📅 02:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25326">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxPGP52yYg0P7HjBCETHVwis7WRzJj06W5z0cUn1FKhV8EXS7JPvZdIJU-65w0EV-0OqV8my_F5sM1KB9AVHC2tk_rxZS2x9eMsXzc-MAjOpgeyprMvHxycQhs1h6ngIiZJw76sD4EotqwZocN6WzI6EkqGjUhqwDoPc8UTYyEzZCL-EqK7_wSm_qawoN1UyfEB2TXWLy_RpYz3DeGZlb_WoZK4X02jHzyONMU65XvdZpB56dkDlXy-W7YHuaNn86cDIr9Yft8vPsolK86gjBk7wjMUbINW7d73LVny_nzXII1C9NIzcnxCyeLCO3QI29virDCNubLeJZd553Mjicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25326" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25324">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXiCztBeqAilM5x99lRfnfIx5cAVjyJGcs72x8AViNB9_4jp9d-jP_M2xPZtsb6DLRmZwy_J_Buv-kyo5j1rLK9ishFrW7oKR_RigIXnJPEXPW1xPctCfo-kqHANvQQVcJU_f5Q8d4tNHJbCKOJXhEpdbduGaSC41WgeCy7SbqJitvCDxp6d5sHBTmyqy-w6TvFDVB3SV5OcnNcnd6ImY91DCdx4Bxk-qmSl1jBF9xxMfrtHwMx2lsd9HPLnR2if8ufTJacKIei0_UuNTWIJ2gpSiz2VtfO2IWrIBarQzzP0igmrdp7MblFbgA1d-hNdXK7TXubeHf0yKVVqASMcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQACht17pXG9Y3MLg6cGxOAJRR8Vk0JMASmg5fMKh06iby8vzRctc84TwlvsCYF_Awbt5I6wXpC4OUWfRFTMtn7iZiKLNp4IN-o1ABuLO2WWKvPyKOP1eAz6anB348IuiB_OBPfNe8iVs3QjRHpdzQncVT3e2myghQTgPAdkXl9J8F88WuHLSIXJ2M-v9F66c8eU82zdoyCJo3lYiKV8uwVd7GtLvFql00Z68MwD6PgIE5aiuuriq_BDpXGrHlOLjXLduHxplhUE-h-gcvzePiqbD40ZnsPu_b7CrV53IjcDEt6qiBtiFlLu6eL_Uq_NdClxNV3y0O5RaRyM3iihEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25324" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25323">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4nzHa9mQR2VA-EviIMx759Hk6SoF90ZVjRY4okxKeFtgpUiTAkq_ceAxMUEq2qWDWWcb7z8Iqw2ryc1QPPHAm-BycgHDXhvVzQrVn37U7PMTkSjOD54q0StJb06gcyoJ_1qIWeR7U-q2iP7PtEtQvQFuEw4dbKIdPLXuvZRZQlOgHILqR_H2zyt6uPrlPC0DeVqWK2uEthoPBGmnzXSif2erlcAn6X1MwkJFAGHruikrsaEQtenRWRlv1olXeiDR19NY7r1EgLAM68q3TrM419zjjCfgKiPiKpG9UGXjjNBXcmwXMAwwbRp8l00MLB74CI_UD_I2yTipdKnOsi3xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
جدال‌اسپانیایی‌ها با یاران دی‌بروینه برای رسیدن به فرانسه در نیمه‌نهایی جام‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25323" target="_blank">📅 01:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25322">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5n-kXotPKii1XZM7o-H56mXzq4N4rWwEdmuRHZAUiQpSRriY6Tjh1gf526ZmWanT5xE3XIQWmjiwEMPTV1yPhIRoF2PhX2jIDl5Vj5CDWC-bUCr_LAaSQhiEeRJuIsO193afieXSnGlkFL5D2oSoEIJ6LU7xFkuirlPYW-By4gyJOfRakEG7b1eIkMxnjFTMKUc8UI3DZchdG6KtRag-5zyGMA8kzqUMk2VCKipJSKbsj6tMEXabw6TebHDKItmEkGck2cZ4trvWDmA-bJmlR3AGPsA3b-9xvUsWtZr_cfD88RUCNwZuVHLUwpWkWMwohK_bGS4yNkF-yUs5vOttA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برتری شاگردان دشان مقابل مراکش با درخشش همیشگی کیلیان امباپه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25322" target="_blank">📅 01:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25321">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoXdYjJLR8UqKi_XtTEH_mobmqnN9c1J8DRdZhKJaOII_WOJd7Ki6a9yi9RtEZsLa2zltSKFNQyunKT_jr8_1b27iskkhxAJcotTRFKWPlIV1mHpHq4TdgVL8kMfIqE3N_y6lF4vDYoeO9oc9GEAZ5oJf36MQR9y7-X4fjT-LXc-mu1fJAd-WSmfULY8exun9oeNZc0JKtMdWz1ZYoSxSQLxQigMgJzYU-k59CHdBtYBqeTKXEwVpdd33fgSSO_b_8PITchr8Uqiy10ttI2Z7gL5oTcjyj-o2JUWiufr8sOV4lhJFYcjiESK7PNIAmxHX6sSoNTHMICIVvXkZ-Gsww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ مدیریت باشگاه پرسپولیس بعد از عقد قرارداد با ابوالفضل جلالی و پوریا شهر آبادی از آن‌ها خواسته هیچ مصاحب‌ای مبنی بر عقد قرارداد قطعی باسرخپوشان دررسانه‌ها نداشته باشند تا زمان انتشار پوسترشون‌توسط باشگاه؛ بخش رسانه ای هم پوستر رو اماده کرده و بزودی…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25321" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25320">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0VcKfGDR8JF4m8JO4miEEcrRcbGk_I_S-SZ6E8XqSMx0Ta4XJf3yZI5FV1Y-A2RKuGq-hea2HGqVvP2wRGCUSTDPRxuWYhCnQKhplzucC7lFilnKHioMzaVv3cNqqhpOrNyHBJ-mjjYoYthcBTjbvgrIx5vxujoLUU6vyKgrUSkd_PbvL-vTy2aIv_kfxjvWEjDululOAQPwLs896qy4Nk1rCnOoAMP6v24lhTAC_NJzziN8Y9ib3RKgwvLpZ_dt_RX8xsW8H8ApGwJr0B8lz0mIT5Rz9YZIiXPfhUoMoX2jWK2oDAfTrtc5DN_X1VTKc35VWXon3oi5ZvJLSQ13Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25320" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25319">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et9P9PDbqx75HFYEofWgSQ5lNiYC08VkZqm3pvkYOz7Y8WY6FpB48LfKNFjggf4HJ62wt28zu3Jp6DfaPkBh1tz13rpNuQ0JQNJxoC1HFDoLoq9qecL9K_shocnT7FoYrCZSW-oQBUr-DJeDNP_zxrx4XFXUOfCUuwIq14p_tkYKItri_ogHZGv60cPn4AhT9ppvrrz6-TKOhzYVsYYnwaotQ9PEvc8_u6TGNwt7QiPIekIKSH4OvK4nU0C6ePwaKSvjqMp4QNa_trAzqvzMqHJkRYnX0MNJRN9L78ZywRUwx1XJURRBdukFpYcW3qx6rcRlh09b_Pju6HvafDylmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25319" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25318">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2548666d77.mp4?token=WNWjarGycA-zVYtd1ml6a1pcPI7qTKffKB_PIauxYXioxhmln7CAr-YcUgqLlGchiq7BhHVhw2qp0IBlACQ-Zk0VgNjqXnoHXSOp_lNTgEebmb5s4OfVs_bu0Bq_XvLMGmZWh_pMng_116E5CYjH_PdrzIVe7Rs6c7k_B4CxzSaTL6juHSQ5Z-Fhu7WM3_OvhgI7tuolEhUIsaPdR-kDeMHVx6aYy1Xkns89PqACohM3UebJg_kmZwjly94VZVlLN0dApjbCtlWiDPtzdaNmilA2YHSdyLBLAZg8nhWzA0C65MgldYTJCimhmM9vlwQFptd_EimKb_raMtrgwIrZjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2548666d77.mp4?token=WNWjarGycA-zVYtd1ml6a1pcPI7qTKffKB_PIauxYXioxhmln7CAr-YcUgqLlGchiq7BhHVhw2qp0IBlACQ-Zk0VgNjqXnoHXSOp_lNTgEebmb5s4OfVs_bu0Bq_XvLMGmZWh_pMng_116E5CYjH_PdrzIVe7Rs6c7k_B4CxzSaTL6juHSQ5Z-Fhu7WM3_OvhgI7tuolEhUIsaPdR-kDeMHVx6aYy1Xkns89PqACohM3UebJg_kmZwjly94VZVlLN0dApjbCtlWiDPtzdaNmilA2YHSdyLBLAZg8nhWzA0C65MgldYTJCimhmM9vlwQFptd_EimKb_raMtrgwIrZjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
شما حتی خارج از زمین‌بازی‌هم لایق احترام هستی آقای کریس رونالدو؛ شخصیت بینظیر و قلب بزرگی که داری رو هرگز فراموش نخواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25318" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25316">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=ckl9Y3KICsBVYxqF7zg0dyOzkYX6rikeAUfiBMSrpPGh7MLQziYE86jqDJjptO-dLze3R0X_YykLXvw1FgN6KN5gC9REi8L7os_FUtr4eNigSVNLwGNmXVcXAXJmF_GeEhlbhO_MhDNgHi9eio8B6Ob8VVZp9_ziSbLsa5Qibd1ven0YqlsCzMyZTK5LvZvslAI1qxJbtAR33LEVHx6bnFRXeDj0RlJAbMCXS9gUAV8n7Exi3wKhXMcJB1BylSnwwemheI8o3zdADC3iKCINfTdBis4FwgSm6wmAA_y6xCC8t8B4OrI7RKC16FdhsoSSMM53J45W_oyUqDkQOsG-rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=ckl9Y3KICsBVYxqF7zg0dyOzkYX6rikeAUfiBMSrpPGh7MLQziYE86jqDJjptO-dLze3R0X_YykLXvw1FgN6KN5gC9REi8L7os_FUtr4eNigSVNLwGNmXVcXAXJmF_GeEhlbhO_MhDNgHi9eio8B6Ob8VVZp9_ziSbLsa5Qibd1ven0YqlsCzMyZTK5LvZvslAI1qxJbtAR33LEVHx6bnFRXeDj0RlJAbMCXS9gUAV8n7Exi3wKhXMcJB1BylSnwwemheI8o3zdADC3iKCINfTdBis4FwgSm6wmAA_y6xCC8t8B4OrI7RKC16FdhsoSSMM53J45W_oyUqDkQOsG-rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25316" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25315">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=WR9YnEaj40VbV28rnpG2FCIHLmdqM9jcza43XDjykT6lQZImJe5sfhWXIlnN2Y253MrF-ihKiKbVPcY0p_iHsXpXY3GL0G8RwvjXyB1mO0g-BoD6n2THU0cjAjSO5rkyeb2AyJHza2SCV5acwmmyvJ0sgdyxoyheN5XzLKMopkW09574FIgFigUo8qtIDkNWiXqrbn3N06mF7QAcY3UJ_5IYIIBy5lpT8S8blew0ZvsZOdlDwuUmragAz9DIBmk59LY0xZa5Id2MZgzXs5qakUF9BRKCKs7VsDNm6YVCw57LgVJW63m2OLSua3U-4fXBKJwD1bfebMrqpPztg1eKqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=WR9YnEaj40VbV28rnpG2FCIHLmdqM9jcza43XDjykT6lQZImJe5sfhWXIlnN2Y253MrF-ihKiKbVPcY0p_iHsXpXY3GL0G8RwvjXyB1mO0g-BoD6n2THU0cjAjSO5rkyeb2AyJHza2SCV5acwmmyvJ0sgdyxoyheN5XzLKMopkW09574FIgFigUo8qtIDkNWiXqrbn3N06mF7QAcY3UJ_5IYIIBy5lpT8S8blew0ZvsZOdlDwuUmragAz9DIBmk59LY0xZa5Id2MZgzXs5qakUF9BRKCKs7VsDNm6YVCw57LgVJW63m2OLSua3U-4fXBKJwD1bfebMrqpPztg1eKqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25315" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25314">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbePbxVG4LbMOiW3QRnUp411ttZhMmzvNLQdh5Ri6OwGkdwnuijPM7fhoc6fTVcQHszg5qoBa5uWIMRgOsF_L0HKbRgldoNPHDiuzzO1jnCge-BJsmzLGWY8VPltci-cRAmHHEPVk3R1CuW9y-HQxe4tgzzyQTEh9qDFRD3lGO2bIgXlTlDvR0DMg0xtkiq7K2CDcaYa2ejYCnHwZoUw7l4K2ee6zqcApoRjU6Veqk7n4V6mOLKAE-Vn_juzqJE-jtKbAfavAPvam-2PsOdoQdB-OnftLWJMwI8DZ0mPJksjFSmCj60ee5HrWSgv0KIlWsYMj-qV5z7CqiN39eTxsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25314" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25312">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MA9J0Q91Qp_0CVab2vlR3osAnxapua9dOmn4uiVfHWxQhARx3xkbWP5YYagXvexOdk0-bMz2ZOrEVU0QvQ1URsASqOpd6Y1jsJflN98n-eRyyXRhS7_wG0am5AadhvGrEqEpKylh8MqZ5dRhAz1ySRJJES87GSvtjq4PanxA2f25zMx6fb1Rxp-qcaMMFWh0XggCAyas1L0M0WyoI5WRUqCcMYygVOszelVmi9nwrjZaGYc1vejtyi8qZfOexlBqUP1E0Qn0cgmzGGpUYtO-LP56okhBge0koLFyir2nmfFhxTU1kVQ_2esaIXTUymMUSvjH1FHzLkqYJtZo3QcOdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25312" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25311">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=Lisi55yKDxzGC6XDtLkswvjplANcc4PEdH43Zeo70DaNVBvDVNTHydllH8iMCCkOabirm64qBnWLnI-MtU1-LRh7RcEt3Et3PsRb-bVKzTfCxje4y03B0jnGfqL1ezm-Jlwj7CgXfvp1LHPjav2DJjCrHJ49jRkuY5dSYn9C6skYPkhynEUimwAOs163SFCZ8z7qoFo9iHc1EbN1ftZOm_xShStBnYgDFyX2aCT8kjzddOYlRuluIRDxkpHmh7ZahLx3ZcOE8_-gKDcdRPQ5mPFBq9nOlyieTXE24Ren6frZudrQLxZYya02F68UV4niM71haN4T9QENxDmgpIU_1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=Lisi55yKDxzGC6XDtLkswvjplANcc4PEdH43Zeo70DaNVBvDVNTHydllH8iMCCkOabirm64qBnWLnI-MtU1-LRh7RcEt3Et3PsRb-bVKzTfCxje4y03B0jnGfqL1ezm-Jlwj7CgXfvp1LHPjav2DJjCrHJ49jRkuY5dSYn9C6skYPkhynEUimwAOs163SFCZ8z7qoFo9iHc1EbN1ftZOm_xShStBnYgDFyX2aCT8kjzddOYlRuluIRDxkpHmh7ZahLx3ZcOE8_-gKDcdRPQ5mPFBq9nOlyieTXE24Ren6frZudrQLxZYya02F68UV4niM71haN4T9QENxDmgpIU_1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم نهایی‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم فرانسه - مراکش؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25311" target="_blank">📅 00:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25310">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsLRu9TDDHFExFPddNFXNEoH6sDgMzf02N93Iah8dwmdLRpf41B2wSOjJyZp0ifzdFUi9RS0uQ40Go8ZZ1CIPgyFr86Kqnz1IEeVaGpvWAotUKjNhdg_-iFTy9TD89QgBIz8DwjV616f0OOZKPmCwTpWf6Ub9I2vc-6ZWJFBhcz4yiUjMofHlnsWW-u9oWYvHL2ol7ifwtFwdCt7PA1gb5ORUlpKuUKROwt4NNNTwJ6kvpCMIPXJucgLYcap6rcRn9km_B5lC5dXOUul1TlvMdJtRU3K3NlHnUuqOD9k0n3pQDLv4yq7JeLS5ocsXke6CjBJ1W1wc0XlnAv5oQiVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌مقدماتی جام جهانی در آسیا. علی دایی با 35 گل زده در صدر و سردار آزمون با 29 گل و کریم باقری با 28 گل در رتبه دوم و سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25310" target="_blank">📅 23:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25309">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCBxbU-kpyTf7ks80naPdGdHrsi_64LpPQRpQn8zChwfammn9ZfirEKmi43AR8ICNoQpbYWjpaNiM7nAdXJUpnIMyu1FClL2ZKCezg6A8IYjLINi2OhLjpZuCBHD2IGhOKPaaVE9YAmMAe3BoMMZsaRf00B2iC2q5z-7HzqmjRZnGhfb7ZTQHTXIN0YKB5MpBEcNVbRudO4rATw9wni2ns8T7tggnVWmXunL2QzWn3zjPso_ZfiV81XRiGSAczcrqg483hUxyp_QSITWmq8-xBNRKBpohCRvMcpQN7Haf-6Z9G8EvkOKUa9GeACTaXNP5Y5dL_ODs67GSGgdniu0xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ترانسفر مارکت؛ باشگاه پرسپولیس برای جذب پوریاشهرآبادی20ساله؛ سهیل صحرایی مدافع راست جوان‌خود + 500هزار دلار حدود 90 میلیارد تومان به باشگاه گل‌گهر سیرجان داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25309" target="_blank">📅 23:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25308">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYVUY2epKQzh98Ke8FsqRK571slvTDYezv0VH05MVO8iNvha0wTqogYuGcefzsCGHNoZ-uge-chfSNeK72ov-ZzzqNT0u_aHNxi039SrfouFvj0QsPIdwk6QnW7LYFt9bHRn-bPIj_naXO3Mf4h_PiMzp4FqnMHDQfSv9HsqjR5rOOwEGNYtfJmjfqHOgiNIRd98Y0KrbyB24iwU3JzplkWMhkgVSdPiG07Yzy9CEFkorVYX8sNYfbI6Borvari-DXxzyeqH_WNLgJybwOz50u98PpPpam4yCgH5O8PJMDtZc2oVCZ9ti68EFBQkjOMWZ1p18gopvnXndur8m-k79A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛ میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25308" target="_blank">📅 23:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25307">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbzUuNy1wGaIqBgtiXeNtPXuzqXyivYIEfnB1fvtNVT5Rwrntj3kbXmfOEMJE-TjgtUWHeBNCL9T9a0DsK0oIFg-iwmTLm4_HGoadEqMshNUusiOvGsTdVK7xL8ludjxTpg_-8POwYd4ojJutM6f8ZrjhQ7tVAoZ2mHa8or1zIAfJkUHuM3UqWBnovVniCqEziolXdwhcOrXoPv63sw9Zp80d29Tz_QS8n3ASqh-6Tfq0a3pjRoC1zASWKH-d5sWT9rc1fFmoShBUQBC8wW8tHAfxuKFWY93Wz7myivmuF54gvIfrZuMpUBUToj-7DzU5Tx2ZuHZmvFZzFsnBACymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25307" target="_blank">📅 22:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25306">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1gqSmc7HQjuKRvh7MydaP-6RhoL-5TIowqQ5JhjZjgwvFWIHR68o_Qal2bGOfa2aMyxFjKOh-BMucAuaQ-4Yr3eafR3QehLokHml2AkhLlyrlWY9v0QLvq80ko5tuKZ1qajnHb6RC7IxUcyKp4wY1GLT-VI8HDDCjfKF4A-ahcqJ6WeFNCAF_nOwfBHST2WcmiU2l6AKu3zbHUplSJZA5oiK5MBMRD4IQ3tL7tL1trcDxn08JhqbjT9fTGuFHkXvXVfrjO1rINx2kNA7Sc9D3oos60p3yTQXQPCKROIB722S0KRAQ7uE1Dko9oYxzIgqg-dWSfSTcnViXt3iUXTtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/25306" target="_blank">📅 22:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25304">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYexeUMBHEePdBarggmy7_aywNUYQ5em8Bj-5Pn6LytdgpSzDzKzWsu5YVtkNIQFYoLjrvjkhAwH9Bu48G9s5V9G05IKHEyUD_7qxt3rBG8ghO696NncmSFDOO_w9bEQInuAsaRK6P3Sv7IrvE5TBM6gfL3-R1ShglIOcqqeSUs-wjpMZw0mkZcZ1UYxsBoiG5JPTLWbwtuRdSYGtrEOppDzlQnuCVktY8v2ZQoI5rVajCx0RYy5otR2AzJaMZL6_q4BvVP__E11ek3Eq5VcYGTPmUn1zcy5jzAqVR4dE5Sk-HYQ_iF4CP5y-iCZymF8MBPNgW-1wgiI_SLcvBM7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DOD9Sc_-Mi155AgmryKYCogfQTyBP8cOJmICtVuhv0mDrngxweRi5QAyMsOs7eIg8jo8ppAZVXSZzO1Su8BIAdq_YQA3wTcXiV8X2a86jQuUH184qhexQDMvHZcL2Ga3__JZ2HiEW74DTHwVHXdAoqlXCIrsuwAaEdokPXmfy_rGrkQ94gBa4kQ2h8Rij2kP5kcE7oHNhsaxOlzWqsCxbhqwvXFljskw4ZaqLF9T_uqY46ro_LdHfHLxwIYL7jGH4G1uLtQ7d_gVIqOWDoo8Un3q-6f7hI55WwJEKRmn11mo-nxiDYBk_l-YhWwaPJt1ALUXTf7msAemOn_qzewfOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ازترکیب دوتیم‌فرانسه-مراکش در جام جهانی 2022 فقط 9 بازیکن همچنان در این دو تیم باقی‌موندن. بقیه‌خداحافظی‌کرده‌اند از بازیهای ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/25304" target="_blank">📅 22:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25303">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXgkSZdCvJ6piHMNqTZ99U4vUrBWwxUsK5ZWMaZNvTttGvC7Lvd4ZzHv15ze6yF9y1DQGVURFvPFj7Ud68Z4ePd3r-28ag7gCwz24ZM_kdaWtjBR40u06e3p8247cA5O2GkYftHQW6zDSUtkcoAalNUpSkJ7PvrtSD8EaubP0DDBCp8q18AKkQTbrny_mpJwruCcsTRSaytkMfArGXiP5I1I1Z4quW1fZNy94UlXDKzmDTin7EAWZuCAJEvJ1DDfaRUrSrwxsbJCa1zliJ_8PVWCftotDZY-uzkT1EPwgMAmRbw7RU9Mkgq1_Hbvmpevf7LUoEV670ymtffKmIp7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/persiana_Soccer/25303" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25302">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4CY7nkwMk-ZppdPhlisVA-w7qou9v-fNUx4Vm8ICcSDTZv0WJnVzAZ6rIgF61_DJV2aeWxVHnKBSY7g6BG3_EKtfD1goo1S8OSHJ3N_GfLZ62Of44CxI9c1898zo3Ckk-rmCs41yL7rdfTLmg5SvhQ64gPhrWlT9gW1vSalchD6S8G5HJP7FAIGJJf1MGSmbSMODvjJXvt9y9hj0c4kz1aNM22xeS9m1SxTIg2l-2Frco7EQxNaB7z194PdlE5kh-TT-dql2zfvIkjpFWVQGK4MMU9BtQw1663Pi59sEkQNDZuTC09w9rSmdLLET9UCdhNPij906R-to9lYiOS-fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌مدیران باشگاه پرسپولیس با مهدی ترابی و نماینده اش شروع شده است. تا ساعات آینده تکلیف ترابی با مدیران باشگاه پرسپولیس مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/persiana_Soccer/25302" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25301">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2iwToPo8pln3TvykotJrvFkZyiwE58ilhq8FyVUDxzug-KrWyX9Y9X6jG0gjdZ1IstYEbGhmWT7fw93Ve2Via6ICfzf4AwrlsXkceWEYPDSDKS7t9ujDGINO9Lrwu_R0zWWXWmkAz9etZlZ4AoRRh_IRf5x2ZYvE2VI7qdz-0XPXAGyqGKlxAAgcvMc1nbJ0uyvAf7gqaY4dGigDBfypwwJgawXdZDb3GWU1oBEXbZQmxritxrIdB-8Ml6dRU9Mfj0dPViXjfBQdfL05M8uUr7sScFfBTbicQPOCfyCMaQrsx8vCaNjy0BXXo8ZUa2Eei1QgsXcx_jcYLPizx8QMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیدارامشب‌ دوتیم‌‌ ملی‌ مراکش
🆚
فرانسه در ¼ نهایی جام جهانی رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/persiana_Soccer/25301" target="_blank">📅 22:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25300">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHtaZJ2sQoQAolTDPm5QuUobLWyqkN_xoPdOoOal7Yyjs18Z63WtAQrv-S7HE0uIf-Q-nc1hq6Klfg7fhC5RZYTX_blgCVPH6yITSy8Wxi2ygVS-QfjJNYbPosRgUntDUZrVAYEKFC0OEFk1UGY1sf7cO0gjYqK1WPgJp0tEbrsutplWBqLDRZ82psdPLly4Ize69U-AEINWUdtEfLVMAs2_iwNsdRhSv1WFlI9a4rvZ9YSX97ZRvDdR0VwK_4ylVAp1cjBClkyx6wsB_MR8LUfyzsKKr11sUmsu7Wg51sp74XuypwxieAAyd5K2y6AW9lEMh2h-BxL4MEvsgepxIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25300" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25299">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZ2MXJpdZnK_Q8gRzQmHCL0_nSKhN2t-PR-ZOSRRPXV1FE_TX5wkfbF9UfQ7ArIzuLI-Gy8z0uYTV4TxSVKaBpKJ9cdxNlwxJJ8pSCJ9jkAUX7m-XdPH4lLVKCEnRe3h-zWGbnAnLvKDYjs6EwZ5ju1l6j-Vh1W-Y1_O4IpGWv8d3Co4ORMQDH_R3btOjFRiUkGN7zIgWnLxZaogZIr7PwdmU6xhZfAO8uQoViLzXJtGCc8HlameH30rmFaJHor0I6jZz1G-4KeYe4MxTZZuYXYgBJhsmAxjwXu11tc0xAQsT0fjovUAJ2AOJNAG2O1kEzMNrHp4nXYf1JzDt4NWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25299" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25298">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLhuJ75zD7ciTBJ5r_iZMSgtCaQ0M_KQBxwslvNX5OHInryaSyMR5Oyz3CX0leq4Nv8MEqdHxrP5SJKJLoja1cm0L6XR-BLfE4PLoZlp9B6Zw5rK0WiBQQ822QD-sHcUewMz2oS0FOw7Y0ZNRdDBRF2QhUyHkypUcVR2Ys-r67xhS43fIUbfH0G53R4tgLKKAGzyTefWzNMcIN9JGBTzzZ9gzkbw4NXBwSLneGulbDDL8Zv5TRSJgo07iaGDDmkYlGABfapVfYeYPxgfmSyKmkMWOMd6_I2ALmVUTeUbbfy6c0KAKD4kNXfB3N54Z_ni7Sm7w70m7NOfLBn1_E2xzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
🇫🇷
فرانسه
فکر می‌کنی کدوم تیم برنده می‌شه؟
👀
🎁
۵۰۰ دلار جایزه
بین تمام افرادی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، طبق قوانین سایت تقسیم می‌شود.
👇
همین حالا پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p4_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/25298" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25297">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArN3WBS82uM0doG4z-TgiJ98M-HyGUfRlF50CKhvBwR-aCljINpZQ_ASowE-4PMhOpnNAQ2XDspa6i8dCJoQLSBFJ7X1LpuFRf5pqZ6Gb7qoRxM1MyfGHEX-hHSnug3hkXkPCEGcQpfGBGR_BwlLge7sFDwuM_CxEh0uH0F25D2cPg4t5MbzI6X5rod946s_Nev_g5qWBCsruZt35-YVxrnXKZgycRJrjmlLVGYGfWpa-7P_4PZO1wliMcWEHzcoQjP8HrmyqyuRC12U5w-HO_WkLvdZBFAvQsno_tzkqwMCLKSAxHo2U-U--dKHBheJrSb12Ave8gsa50YUoYQ8JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25297" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25296">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l63_9G42CNluWO8JGzB8rY345BI_frEphWztuwWmph5Dk7bDuIrrL-w3Lx5nEdfV4Sgu79p1uor_jVKhw_FzBtK7EDxorDyeDL9nm1QMqBdy3afpD1oJneMYfIhNPZweor3k4Th6an4jp0CIfIyBnrFzzIqGgfwh75fG2Sm1LxR-4-gjN9qdB3liG-WwUw8wIus2lGWbewtowD7bVnzjaHzwpZq7zOn-nas-x0lw2pNXlt1PVxMcuSG7OLf5Mzsh9RfW0YRFcMnHdyv9FSAICHBrs_vDwXRAPt2OBKve3KMqRURm-CQwAhzZNxJPU3J0EA59dFDx6-ThlgPG-6_4Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بنیامین تانیاهو
: راستش‌روکه بخواین لیونل مسی 39 سالشه و اون قبلاً هر چیزی که میخواست توی فوتبال به دست بیاره رو به دست آورده و بارها شجاعت و بزرگی‌خودش‌رو ثابت کرده. ولی واضحه که هنوز حرف‌های زیادی برای گفتن داره. من در جام جهانی طرفدار آرژانتین هستم؛ حالا از فردا بازی های آرژانتین از صداوسیما پخش نشد تعجب نکنید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25296" target="_blank">📅 20:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25295">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeMsgO_ryDVvj_g1UeHC-AB-eTB3QQKz8h9VCE8ZZ0xpHubG_jURKEAcPtGQTTAqzY4TUzFNiMxhCk5DqH4hReU0jHlExMEDkkDmb7Fh94IoaGw4zfOGwX7Ho74kfkVuBx8CzW2BDqw6dhZNrvKeSJ6QIoCxykUjegf9BPNuneynG5mOzh_jkiR5idhrtbTilEJg5bEYujKY6LE98ds1Dgm8xroDzFP6Kh81ZWOdj5XKObtfhlnfiGickeaFd26_d1Z6YRqazNn1hd3m1YiVfxPQ680qykWmWdFeaoXW8wwVff_XLVShcrcYJC_5FVD1bYHdzl8ROI5N1QjDj-HdEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25295" target="_blank">📅 20:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25294">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMK8nQFjMSEira_lLOpToZOkC0rFJ27cYOXC8d5mtm6BZhJ6gRI3T549KR1oOrXWGx5RoUpxaTbxtyRZGoj6CNGaAYpQHi5eqqtFrNGC7aiB0Jr5SIv4NWiBpIBx22W3wkYz8baJh6Z2e_pwxP7UYiNU8E-ee3nYUYkNlfGqoTthlVFNkm7TjNRBhnNnCvQt7EpShXzNzPg0raS71A1kyepR_t22m6T9CYJXPgS6UscudvuZmUTxynkpM6yZchnPi3o7Z6gIlAgAkj8NB9M17IORQKzFnWOekbaPAe8BQIKpHUzZHDdbuCUNSrzLrPun5QRomX9VL0z5qHNlL2HoRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ طبق اخبار دریافتی پرشیانا؛فرداشب‌حوالی‌ساعت 21:00 مدیر عامل باشگاه پرسپولیس در منزل مهدی ترابی جلسه مهم و سرنوشت‌سازی خواهد داشت و احتمال اینکه قرارداد 2+1 ساله امضا شود بسیار زیاد است.
‼️
پ.ن: دیگه داریم لحظه تمام اخبار داغ نقل…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25294" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25293">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5cLlz0mSKwuSoBFxfzO0hqEvX6Am95CT76uiD5Y2W9SEsDP_wWmiFuYolIdVfJUfkGOoFClZQU1amyswnxsSecPFcRFFA1W90cXAghGPQndfu4E7h_1TBlFsV8aQkUHEsNFK-bQBZX5oOy9Mx39RWxwlu5ErWS4OlHQdRbMpKMFx-j3tbNGg7DLrfYDj3Y9XJGKmF1EUDWxumbwmtj5ZKfzyBR2EHhJooWRjSkpP3g0sTfnCgt3lUYqTmkiCkyLPlI7KlExoSCpU4DQ3lhlHQ_yMYJTm8McR723L2fVQ84kVf7W3YEkPn2-JFiR-11DIeoNYha3MDsaZ-8-GIPF7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25293" target="_blank">📅 20:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25292">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxAFyrpH-jI0U2CtJ5hJBTVo83LCfzMu_Tj7LEHMbNLen5hY9wzK637Itpxcq1ysCJArg2KbKZ2dun2gPX83xl2xLoJC9G0KB6kohyST7LORMQDfDm_8ZQzYuQ2d7ZohN_-A5khwytFyDPGgmTbZx7adUJf9gD4eHzCbIaXZ86UhCd_3EexvJXY65a5nUGJE2dRWzFNCi6mPgBj2OhVxZpE8H8Pq-GHCQAY2CZwJRQeJBmzbNGpE4UxvsiYdVitcFvHKdrnesE69LFLOCLboEMoDunS1nWH0lRuZaEmHpdV1gJV_j3KCCnN9cYA5dKSEkWU-515Yw0hfmw3Mq2VthA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هادی حبیبی نژاد قبل از اومدن تارتار مذاکرات مثبتی باسران‌پرسپولیس‌داشت امابعد اومدن تارتار و درخواست جذب مهدی‌ترابی دیگر قید این بازیکن رو زدند و او با قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25292" target="_blank">📅 19:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25291">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMBAHfOpdSXHdTWBqkuTfhVnYM8LS0KhYdbV191mUaA1_tabQch9gDXlbHwslRLmwt9t1rnNZLJoVFm2RExr4bzJeThoB1dzkDyY9pguJ_wA9wNQ543Zm84mLOGtBFlmnDBhrqpEi7cmrc31FPz5Jpe_ETwLaDhWjbyMDvDoPTa2PKacUR0E9JgmO2YKyzLrSNF00-Kq-yN7W0hLas2f5Nz1Yze83u9-0GMrs5PonT5hVs9XDzVHAMORTpxg4fBH2ql_qspX7uvNCs7KGu6JELJ9x5d_GaWZ1Cin-dIZ667c7uTC8dDFRaNxAHDXXb1pXomrfNLjCTjwAnHlYgO-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرورزشی باشگاه‌الوحده به محمد قربانی گفته هرباشگاه ایرانی دو میلیون دلار پرداخت کنه رضایت نامه ات رو براشون صادر میکنیم. همانطور که دیروز گفتیم باشگاه پرسپولیس گفته ما تا 1.5 میلیون دلار حاضریم بابت رضایت نامه پرداخت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25291" target="_blank">📅 19:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25290">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqIJmMhIjEZoaOkURveDSMbTELL2jioR9Qy46EOOcgsw5o-aj7eVRdpbR7-gqLeKJ-AIxwnSqT1PI63n5J0WfO3jyVw0BNgwwiSLdhS5XWM2u1dD1pDx5j5x_DO2Ql3wNxNlujZQxqrvUYUQZxpD2f4NBRG4e8D-14Y9f976a0eBeGJPhPrs8bUY4FlnfNM8WyNylOdAEVISxWzDJnVVZZWUQKOfOIKBbELkMGGvAPCaGhrHrMxJlgAMMUQEIi4ljsEroB2-mxefn9NZI-qGqvaPYrnUyjr11gP77RudfWdZUEIQQMNy8cqbK7T7PRLQPcWvzKQp6D2PjVp3i6vQIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
تونی‌کروس اسطوره باشگاه رئال مادرید:
مردم همیشه دنبال‌بهانه‌اند. تکلیف‌فوتبال‌در ۹۰ دقیقه تعیین می‌شود، نه یک‌لحظه. مصر نیمه‌اول عالی بود اما بعد از اینکه ۲-۰ پیش‌افتاد کنترل‌را از دست‌داد و آرژانتین استفاده کرد. این تخصص تیم‌های نخبه است.
🔵
مردم مدام درمورد داور و VAR صحبت می‌کنند، اما دلیل‌بازگشت‌آرژانتینی‌ها کیفیت و ذهنیت‌شان بود. مصر نتوانست‌سطحی‌که ابتدا نشان داده بود را حفظ کند. اینکه مسابقه "دزدیده شده" یا به آرژانتین هدیه داده شده تئوری‌ توطئه است.
🔵
بخش‌سخت‌فوتبال پس از باخت، پذیرفتن اینه که حریف بهتربوده. آرژانتین‌شایسته تقدیره. مصر باید به عملکردش افتخارکند اما از اشتباهاتی که برایش گران تمام شد، درس بگیرد. فوتبال همین است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25290" target="_blank">📅 18:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25289">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeO2Kjwbza46UdtdYpbdJEqLWm_VKpgXPrzkvaQfL48QdT5FCHDkc7wgJ_8cigmiKEMsLEvSRSHaKhBU4hrRhnH5X_lnrrIn_eZeR27ZhujzKnLuwTOWs1ciCoxjKgq8XLq8BvR0Nb3mPOaso-K3Lr05ofrFCF4oQuWkbSPC06Ff1wCGFnWnrc0S6PB-KcmHg0pl_N3J1ZVCgzigOfSeiXzlg6Z6QdpBOn8m7a59Kdr1dO70RHdiun47iPoj_34juvY-OmSM-EftU16Aq0u3lk0nJuP6sfSIpoPhuwz2CpdSWUR0_kb5yFBM6BdIk9FoNI0pwbWQ8kWAk2lRQPBE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25289" target="_blank">📅 18:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25288">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CahCF737lpmTCJLylHTEWYEM_Mc-noyufawAKsFgGHf9WiibXCP9uMjfdMirKJYu_HpHeg4evR0iFSoJud2ZwoUQ9cdw68xRVLsoriPuD532I5lmmUiZx1L_ZPm-laVxRHtv4oorcB0j2SkrLiNMLuTU0qWSHRGjnHj9TcihlWuCSdEC11ojSRcUyZ1Mxn2O0YAW-aKIUAH5XwkW98cm3zyTXjqAqyTOLBdGNwIRM5BcAsv_LqPqWv_PuGfHb9nFYamsrj5Fbv_C-l0qQ5w_MMWS45XmBcd0bQyDQcAGFO9g3Z_40-bJG7UKuGs6zSNFLaV0sstEwYavZmgEi8eBhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم
؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ توجیهی برای اون کار ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25288" target="_blank">📅 18:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25287">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ6F7iMbWUc8FtSfeRw0ZYXjPdBPkdEf1L-GcWAIcBVjozzxRtNfWLWfT28VS4N_jK0pAe4i5aUuywCWBtk6b_jX3gB6dHypLApuQnKXlT5c-SqQQv7_dPjYGQEOJw5sJ61lIAikGCK5521ZBgD48rDFdyb_y3I4sqOfTbwv9DTDuUxCjX0sBaL9K-nwl-vL-IvTm-J66JnFCwNX4c6aKmpoUVCfmZxyLPKeAcgyQXOVj87i5ZsjhPNkXDEba4-ndQ1iv60YwqB62AYwawNZ8Ttyn05luHuK4dwnb7Qmrn-eEtXNUZ4pDor2wuryrdjFkmaFUGeIW_B4TIkjB3MVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ طبق‌شنیده‌های پرشیانا؛ مدیریت باشگاه سپاهان درتماس بامدبربرنامه های علی نعمتی خواستار جذب این‌مدافع ملی پوش شده و به نعمتی اعلام‌کرده‌حاضره‌برای دوفصل‌حضور دراین تیم رقم مدنظرش که 150میلیاردتومانه روبه‌او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25287" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25286">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjmBaInMst0zIbIa0KYs4Z-2geNFftnBuOvwoMV8XjHUGD2KtbsOFs5mmPo7br_RMyy8kfC8o9bdRgMYrCGSTo3qzbcI4j9vtNwwsG_oDDHPTuSRvWVN-DUCWdBc9SV5REl4f_WFyX4lJnt2MdaKk0klWnZYEST06CpT1Uyf9aJ7OXIAyzSI7yxCx5OuE57kT-VdxpgTOSfCKsJdQUd3D1v5i3XfB-QuRajOYlBoOlv9ezJZ0AClaoWhc-Dnnx7p03FWdAoNvY_IHCZlwfY9RtyNv2Ig6WX-B_lhBXC4EMCXukjiZhqx405UHVcIIbRLu7ai_v4odGGgZCnjgiu_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
درخصوص اوستون اورونوف هم پنج روز پیش خبردادیم که چندپیشنهاد از جمله پیشنهاد الشمال رو‌ی‌میز مدیریت‌سرخ‌ها قرار داره و با توجه به‌ چراغ سبز مهدی تارتار برای فروش ستاره ازبکی درصورت پیشنهاد مالی مناسب؛ احتمال جدایی اوستون اورونوف از جمع سرخ ها وجود داره.…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25286" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25285">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RefV23OZb6stnEU-MwnDOnR_je58ZU7PeoNjApKAUScZsQRlV1PAgM1JQ0uxSEL0lHVDNj3Jk_AGXUsSWaj-V7uhf9MKvuAO5AZDkHrmgxgM7ZtjNeWU5-Lqwp4xTVZ5oY8ghSTHW2L82_E0Was5rp6AQ4r5dACqB09TaY5aIPpzBw2X7wGpoQO0xBQL07T1zWfFKZs-n3fS1rzQnJmdv1LyL06oLAN0SJV1Ka3cHDY1p52chVrntwzdxG5pL8-Rj6Xzu-V_vUPlGAYpJxot4w3gkw-x6ZJPsu2IesbATfNX6FWIthOzIlBhKk5knZbKxrSQCmQD_I1n15tL19fY4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه خرس غذا می خوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25285" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25283">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgFlGGyFWKOURDzcI1rcQhKxxWmvFlmwGKmCatp0MrccgliA-Cb9GrMigdSBQK6GuP0nUOZmmkFvCfwbjKOdV0cqCW4gIzp388y5ng39-u36wa5_NkM2phaQDnmQhFVDA2a4VPP2NEO_C3GpKXsZ91__MHq8twvWHbB7lEXqcYtYApEFIoBO-4aDxvHkH7BoErc7F500pyDVml_yRdOiURBU-1yHyV3N47x5zWUo8VqDfGykoEEsyD4ZkAKA1u8_vUsOg7Be9-4VhABOxvAyy0qF4Uav8Yq2bFTAR5hheSEKtF7epgm4dLHnYpW7v3U__zks7Lhoh6m0n7-GJjdnMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25283" target="_blank">📅 17:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25282">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd7OEpmnZWYV2F5bzQ9RwOUxlF8l3X7XMnALzJ-knAoQhucGx7L3H-ajLe99JqyTzvQFmaR3-E-2PSzXKsRIzIJPxJr0Clcw81Fjwv6lK0cRAe8zTrWnMZA9dxHncAWztEgLUkHLH9QwMv8A-daGkMN65FQGlhcdxQ2h8LQHO1u9ts3l4ouUSiTHFwa6fdHe05JWwMkqH0bwn3WvsNeoQaOBFpUuiWx2Bon9svdGPHtqH6RD_zSyUT2pO0zu5GXrjNOZzvQbVADbbuBaYFGv6ndt5cc2SW1GFBKfUrXEeLYB-KX1Gv_KptXiHw9ITIGw6DJXD0ig-3Sbfo5hejRPWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25282" target="_blank">📅 16:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25281">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tpb58TH2k36nK3uT4lVZl4sA1oUqRjvi5bp4oJYuJiaW96BSGWPweQqB50R4RQ7DE627oOodgsh-BYfBN08FM8rdVwUdybZC8Kpom-3zUfsK5lKlelazd50WBnLxpri-8rsaLfNskIXG6ztVprTXPftpN2F-nyB24FpnG0mfpihh0UK055GibhnVrDzhA9h7roKsD92QiGCmbNeXOXgl3JIbAWCmYMmmG6IeG5hhBBXgD0o5egmJwapYSJlK_QJ_cYZtVYBmBhUPRLIYzATTD7plgjW1eUbpRi9BY1W-ABN4BXGtrJxJDVt7KmiVDu6cg4B0sOsLyfGjJ3dVWt5Ezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ پیرو خبر روز گذشته پرشیانا؛ پوریا شهرآبادی مهاجم 20 ساله تیم گل گهر سیرجان دقایقی‌قبل درتماس با مهدی تارتار اعلام کرده که قید حضور در تیم استقلال رو زده و اماده عقد قرارداد با باشگاه پرسپولیسه. بدین ترتیب شهر آبادی ظرف 48 ساعت آینده با حضور درساختمان‌باشگاه…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25281" target="_blank">📅 16:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25280">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
رونمایی‌از تاکتیک‌اصلی تیم قلعه نویی در رقابت های جام جهانی 2026 که سه مساوی بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25280" target="_blank">📅 16:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25279">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftV_3cfgI7lmjQl-80CcFO417F0c1ce5up_vGuyq1qG2kg2SO7K1VDnqXNwUPjw3xuQCb0L1uy2W5AysQ-ofhcbH9TKmZaHJ2H7uxgLSecYE5j2sFHOqoi_2hF-rjcrU0KTgJNnEeTx7RlRR9PUaWlKk2xx9V7qAAYUeo1a3ulFeCPSCJ2chzNw0apOnBbJ__6ROLULc-eWb8h1F4qzQ1NQL9amgRv3T8ipP4a_JugWA5izt6Bcri221Hyirz4Nf7EazGryvKFESHbZyThEqonO7pdUNyjAxsavvwkmuwh9App4eqFL6c8cyf3iZNfO_Z9m7cAOA1FytDukWhGVPkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25279" target="_blank">📅 15:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25278">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmqaH733-4tehFXidXk1Wm0PBx2gfJ306wrOTvpFm7rmlH6r1c_qM3DuuSxUCsxVoTmWwNFQ8NizyyoQS8g1YuZTetGl5Z9hulZAuGU62APqbXBo5l0nrMefIDVUbMiG3WmEWceSlQaaSjXxYlwwoH5lRSPVxAr6Lu7tvuitc_dLAwqIdwalcRt0Dh8IqKJdBdAYIj8aSnxJrGcHWCNDfV2Kyk1sG3q6xTf7Kertnr2zbaSnTce7uZrBMcOLwya9UEe7nZPu-UeS0YwQ2W46zhA-V55uJ3MCg3I7tnLxe5zTxavklNzqdVEcvEp4Sc4rwvu2hvJD6mkpsU6oc3vIGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛مدیریت‌باشگاه‌استقلال میخواد بعد از تمدیدقرارداد یاسر آسانی قرارداد رستم آشورماتف مدافع 28 ساله خود را نیز تا سال 2029 تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25278" target="_blank">📅 15:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25277">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWu1b56bObwq_YQ3mJ7_Kfu9c4Ir22R2i40VwfcKKPI3-zmC9-7nt38aExyjn39mFw4fYrS01es1foRqANP8aG7NhqOULVqn9X0HckS4lD1RUywZDdBgkhnGK6VJjwhmwR2dSCmpk9z16yhW-JerWYtsDpr-I7BQjyPsSroBISVj227j9GiEQxD9_7KeeJk374LVI0RuLe5cqHMFdyY1a2z2ZDYoQV-ewuxn-M8sqZdlvK65-zCGja4rtmg5y9dM3jpOy6O9sWTV2msHekS73_QVd9ZiB_8XP62BEsUZNhcJgLuZ6MAUPYPZI9JsqCRWPIDtwP_XCQwNbPJGegU3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25277" target="_blank">📅 15:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25276">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQyrqjFaR6f_91w4sBbzvY-ETJmLiL5DdGos7AM4Mnt0PR7JD_vTDaJ_DlMUNir_WgHVads36iUgzUJmLyvAtayCSk2mWZL24rS9iXylGlcaiOMUJlBtDQjPFiRdTIHTuK9Uv8e5ycKfzr4oFSGOx-9AlzYRm3GrMNMHxMUBNSlmbpwA0XELFoaCKRburRG2JGf-GuP2D03wiAY2C15tJI33M7YEcghU2cxRGxLTW38bJh7CoaA9cjmWQy8XXrpYBG7d3w0rPxGIjkY4-jy_wTLng0AzuVWN44dG5ph1n4e32HcrjW9n7bGdx_wTE_pF-JQatXvUAxlNOvJC8SU-jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25276" target="_blank">📅 15:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25275">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5Jgn1-fitDTWBbsqqJggxcwYemATCo1IoXNEoxv01QRIbOeEgsrY5a25hgnULej25lTC0qDtgnuNV_bU7q9eOkRHG1aFjUfGaS5cqHhurm-hUiFHl2hKsJTqa-qgks4qWruQVXnDnEhOpVwMaeDKlXEBdfrQJ0ygTo96BSyg58wj5CpI33pN14CUXBEuCH5TzxqCY6NGxlODtsswQx9zg0NsGlPcwJ_SdeU-1Rry-eMm5KGWNkpSVot4G4sNT4coH0R0YT2zdmGLrRICxm49a0Dl7_lTFrQlqza-gTYKxoNezH2l9CnOg8t5vIq1ulazMs0QsewxPJ2WuDTNsWWlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ ایگور سرگیف مهاجم ازبکستانی تیم پرسپولیس‌نیز درگفتگوبارسانه‌های ازبکستانی اعلام کرد که به قراردادش با سرخ‌ها پایبند خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25275" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25274">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOFVabCCWA0owxg8ziX3FGhbSLxu55SJgiaSij07OEaljDJrCKeZYiFlDE-nZPCL_dwJTe55zvkTmTeGLupzvqDZxhC4QYzF2nd-VdF7TaadXG7fg7aNuaCPV9cBik-tPbqD5FzRSB93OsCipXrEz3FHMuDu_osVp8cpVcu3Wocf9sWoeIg_qW8oGVM7rlO-eLdxrgS-gSTVnMFUybD4BTck32pj8OoxN8W1gQu4kWkk5jkGT39WeLipJxj6Mr19T95Jz864jfSt5UHVswhmuFNf0ysidOFE8hbgaPH4VRNFsPwxFwjLZRzzePX8-7QvWUpNqFZKqzXlVq_y73Vc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آمار فینیشینگ و ایجاد موقعیت بازیکنان جام جهانی؛
همه چیز خوبه تا زمانی که گوشه راست بالا رونگاه‌نکنید. رامین‌رضاییان هم تو این لیست هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25274" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25273">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANulHfCx5hnva2RPqRmSa2NA39PJ_7M9cq2fXJy6sK5VxCUqsdTXE4tMGjQuX8D-vMJjx2pgeb8CSf9xH7Gl_D83z-v18bYLk0gqjU5mGtbo7lMfJFHLC0AJxSKRmUVSk1MaBFHcraBvogH6uVmK8HujZwfJ9fde2eCx6OyASzWdrHnAv9yYzN0dmYcP0ZyPNVJsqAwD6-jHZvyTf8jeVQHKKpA18Mcgq0DK5I4J6FPkTmiJoQr0V-jxMr89FK15fHhcgPMZ8PaINrpqjK47sWh0iYvc0msqJURMxjZ2TB-IV5aQMISNyCB1T8fD9iRg0qnBWQ4FQ8_Dq4ReWHS4GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25273" target="_blank">📅 14:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25272">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hj-vIKt1mIDciJR1_6IiIUaVZ6bwpWsff20YzuECrE7rClujlVVgFUztC09TUrYK6aR82TMt10H_NwWd6EAnb3mNRxJmNl3_HidJlQqgdELDlwNajkTMpXriw6XRPcPeYTdNpeC0raaKxltbwOgylS2gc4URvZZgrAU6ZiRt6XxxYClHm-aMj-tW8RxT7qFoW-1a0xh6_NvA9AhyyzgiS_h2jZsaIfj7lFz2DBQot94Ziu3MSFaKdvHxgcT9_Q7gUeExR_UT-MffVLFUaV25QFJeEnEVNyWjyBesKucPBAad65RHTOZABI5jXdqvMuqtBukHKyE2VOzo5YK4wMHSJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25272" target="_blank">📅 13:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25271">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC-cj8ZvfgMMt6uPA5aSCmfXddLQWb0GPnqUhhRcGMnsyQAcBjL0o_oTrZzfpjnTdTWy-XxEj9QU0u6_RwwDpf0AUo8ASbRUzeYuS0N0H35ab0GGgClg2eLE-IkYu5lS4liT4-ipg6PHd1Etk3M7zAMNTPHNUzR6QWHCmTbjDFDhq_71wwLP98aqqUHDPRlqoGZVBoQdUECqbMAeIe93c_W_mMamrKdH73fINv0OfvJbztrxWPK7v0w6aqLYXNGBphKQmkVwFZZ-UpLcZrU96tgD5rGkb0S-3YQZJ1nkE0Dytm1kTnKRPKz3M3h5M3dvrRFUsjAuG2dvMMjHJdx-FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه استقلال باشخص امید نورافکن برای عقد قراردادی 3 ساله به توافق کامل رسیده و هافبک سابق استقلالی‌ ها برای بازگشت به این تیم منتطربازشدن پنجره آبی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25271" target="_blank">📅 13:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25270">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1uOHeQq7DSFlmTKQFSPEf8ArqTnX2akS5-EDMfL_Yeg0hegvYfoaziS71lYXYHkYY2t-DJB3rZpjo2gbnIrOa7RefnOqXrp-DZ9vLdOUYvEMIyzSV4x4-lwwHpPueEkWo5Eeq9-pRCm4Fu5T3WUPH8ciPJ7hR-UKApWeUI9IcTUpedMUKbS9K3SuQYjNUXSyYIo8_QEzeLN8uBYBsmrqSQo0y5P-bdFZ48IGhhnnqLtua7RpE64fcUt8oxyTnBCV35s4__n3uOyU88ftEjvzLWIRYaXrhwW2DAhXkghcskP1u6k5QxmHcIkDK-jkGRbSNzxv-3dm4ofHhHwYU-ASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25270" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25269">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoR_oy8-pE1wDK9V9fMmEHOtpk7QHVrvLfBJmjagrYCWa2il1o05WTk0UNS_wTKNv4nNPaSWL09y52Ftpypeea9dfrlHhhCtjwnMNYd-CPcpWs466X1nZ8bk2m8GzdfOKoft1hk3N5YnQwdhmkGvl_yUpp8JfwJ2f2szGqurNNC7Nv1gCVop-qGp8QOPyWWrCALKKxX3WhPF_p2a6bSPdinT21sbDbBKd52eowdRdgO6Sb7Xe1SrokmUUtuAZmasYxtSo9O2vAOH1z2g7lU7YWFxfXZlivD0zaBaoxgqZBtVbXvZkcpWhbHeg9uvO8qSEHtYuuzq-sWoCYMYSmvMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کریم آدیمی‌درسال۲۰۲۱: بارسلونا یکی‌از بهترین باشگاه‌های جهان است و برای من مایه افتخار است که‌آن‌ها خواهان جذب من هستند. در خودم میبینم روزی به این باشگاه بزرگ بپیوندم و بدرخشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25269" target="_blank">📅 12:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25268">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qM9cKF0ziSBdkF46DQM22s5vK3nB5T2FQLhlmaKyo5o48Q_Tmk6tQdKQDbFZHBKuWx8M6Wjn1k3Ue1GfkIKZW9zZpQZF4cyjXHedJnTowxkOby1udVlQiE5dFEJHxq5GZrpC25ADPY_mpEF0bpfwQwOdWJseviih5QbLoPwt9x9QYv_JUZCPSk54eRN_XhNtiAEx2hPUbrDSSX2iwNPhLzcmeOwehuSI6-fGHckzkduvW5TAmgQxxLtG2NDK2ses6si-UobKz5U57cwomqENaloxI7lmEmPqSnktmWchOt8D-P2sMoJas1U0DfFLXfWgz6uPFL6nERr-CbeO-R6EJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت‌عملکردکلی لئو مسی فوق‌ستاره آرژانتینی 39 ساله فوتبال جهان در کل دوران حرفه ای خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25268" target="_blank">📅 12:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25267">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=Kqy4AZx17Ty5cU5KEE47beXPSh8lMdmD4nrN_dSe9jMBiwtAlS2wlhC-9-S092DAUZ5m5bh57ob6i4JtUl3kjXxfqTnABU-XGhzgTUadrFYLTA8zWgtKiGGDJCVA8KtNrIFf4210gTJFohdJFWOPK5la8uLtrtGcyEujALuDgRRvnaqaplH1tMZpUUsL8avPOF6Cfx4sBFlVotK-yHN8dQz75xdpN8mNAzzRq3tl1DjiBLGIVPznku90-hZ6mOsmOtQJu_nUhADUKTgHNaTMBrGPJU6ny-DNAX8oNexhu1iOcjFmoj4Lhp4PFv6Hlyj5MBVFKUeYtlfGX3KeY966Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=Kqy4AZx17Ty5cU5KEE47beXPSh8lMdmD4nrN_dSe9jMBiwtAlS2wlhC-9-S092DAUZ5m5bh57ob6i4JtUl3kjXxfqTnABU-XGhzgTUadrFYLTA8zWgtKiGGDJCVA8KtNrIFf4210gTJFohdJFWOPK5la8uLtrtGcyEujALuDgRRvnaqaplH1tMZpUUsL8avPOF6Cfx4sBFlVotK-yHN8dQz75xdpN8mNAzzRq3tl1DjiBLGIVPznku90-hZ6mOsmOtQJu_nUhADUKTgHNaTMBrGPJU6ny-DNAX8oNexhu1iOcjFmoj4Lhp4PFv6Hlyj5MBVFKUeYtlfGX3KeY966Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25267" target="_blank">📅 12:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25266">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irvMzwdsFEUqJh8lp98ZLwNRPYRyYvUpJ_zvS8G1VguwVvMmEXgEJqbRIblSqQCLl7wJfIJ8Q1X4auPDVvhCVhM7w8vnRdQ8KWkR8Se09vWmPwGYBqtYfdo-J0epjtl1Ky4-gW6F1NqswfhLLT265Rp2vUZfNLUCfySSqbsB8Do34gPzcplW_ludRlhykV8hNyjotQDPuPq0UwhMR3Mr_f9N9IL4elseEwgP-a9EXfuWMXJuiUDaDVa_OM3zSUoa5tDwgbrVS4dyN4WFAdFPAXTXHROqOecUfwPlbiRfgdQdDKZZ6hEH825n3KoJGm0VXqI9ZcBPv37_Wqh21tM4OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25266" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25265">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ln18TSmz0zoJ8WbPJV3zvOkBL_ngN2yy6yI-oYTLhszfmG7o_Gq_TxC1oWEa080QdaTfIfyoHdww9uSaXifeGQ0AgaAhdqQzQQBq5-bmo2jSCyLFqf3Hk5yViwxmUiT-HcphsmouV_vSbVqe1WwpDU_2iFkm9I-M3_u6DuDyNV50PfiGkGrlmvNbZVnGwlvqiA00-Gt2u2ljXX_SitiR8b18oYovHRPM_p3oTD4umnCPNfy71sMLk45ChFMOuquh0A5v3oODPYbTo3298ukCZqA4zOzE7U14NWMifD4VvKMXxI_dOYdEytb2vmrMiMknl4AAUFJN4YZTkaRf1zM9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی: شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25265" target="_blank">📅 11:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25264">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9ZTCi5SNzemuh9yzAejvG-v1IW6oImS33bPOHblbRyhgSu9D1gmHCHzXRho8OWCTJ24vEQN8z5GJRH3ScamlO8Tlbj1aXC6eU8rwxBDu0-2NbTz86AiadC-2uF8jRyxtUZ-qUy6w2F8_gGlkJkj90cf53ZJZu4aBS_8pYTFxZZKelNEMNcUwL2qlPO6PnTxrXEJ61AOWk5B3sdh9iQXt_ScR_6K-fryYgQe0DYdYfkJvwKYpJ637LZKRYwPOuprjUaRgv9JaqoXUAx9UwK1vUvqaNad8xOX05gWPUn4SxAUK_ff2UIuTNXTBrHrx0OQa6g5diVhBqXv392RwD6Yvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
‼️
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25264" target="_blank">📅 10:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25263">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=gvwWysPCj9pptSQdafdL2EUrkVXZfur-_j75AyYdCKIl-_KJdHQAvej0s-AIvB0ifFrGamPKVqtw-frAtISqqrOpBLnqiq5Hwiga4nS0mBTlF4jPO2cbBaJBQrYvz81jFagmmgub1DMcmrfl7BeK18RAQ_YDoYFSfktukDFKg1jfY7VhQzfiRoRvUR-CWHjuVIMcUefe1NaEZI_Eq3e1G8P9nc6ybGFt3BEUmZHBZhCKb0_zN70qZiP1PaI_mQmMoMiqh0Lz1apsdmDuE2G2NTAoX_sPwDoVNv-6bWdEJPbJG-vBvDbkhijcvainycpamqL0PwnlII3Oldm5W_7T6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=gvwWysPCj9pptSQdafdL2EUrkVXZfur-_j75AyYdCKIl-_KJdHQAvej0s-AIvB0ifFrGamPKVqtw-frAtISqqrOpBLnqiq5Hwiga4nS0mBTlF4jPO2cbBaJBQrYvz81jFagmmgub1DMcmrfl7BeK18RAQ_YDoYFSfktukDFKg1jfY7VhQzfiRoRvUR-CWHjuVIMcUefe1NaEZI_Eq3e1G8P9nc6ybGFt3BEUmZHBZhCKb0_zN70qZiP1PaI_mQmMoMiqh0Lz1apsdmDuE2G2NTAoX_sPwDoVNv-6bWdEJPbJG-vBvDbkhijcvainycpamqL0PwnlII3Oldm5W_7T6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس‌خاص‌وعجیب‌وغریب از 18 سالگی جواد خیابانی؛ خیابانی به خداداد میگه تعجب کن ببینم چطوری میشی. زنوزی‌هم به خداداد گفته بعد جام جهانی اول باید یه ماه تو تیمارستان بستریت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25263" target="_blank">📅 10:48 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
