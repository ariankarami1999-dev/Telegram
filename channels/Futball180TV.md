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
<img src="https://cdn5.telesco.pe/file/QiVnFq6pQeUGCSTv6-K8IeAUwFEGF6XFGiU7uwKJ3Z-hjBoNMJ18Ks4020A-NVlDzGXbpni9vCO7PQqcbc6JcWedc-aW2hx2N4LOSUuiJL6a1Cc55f3vBPbJY0b_GC8f-9AE2gIBG4VYY0H57fup8_puLdlA05IOwdstjiNen0UlWVyEXfZUf11sBa1oT2ex_tBfBpTcOiml3fJDb_ti_Df0skIs7LMGsvYkTv4z_-M3vwlnde9JmJHgtL-x-I_HM1aGhGFsjB2pWJxbCrFIYeT0rR71EOtwyEZE6R9R-xUXx9hRTPlhzNij4eqUfIDL1CiQu0Kcdcc-U_4z4ZjnIw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 447K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 01:12:39</div>
<hr>

<div class="tg-post" id="msg-104524">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZsIVVpOfVzWeu89nQLwjrcteyHJg9nRDEfniyP3MGL5HHWuSD-guFZ4EfgEzuwR8bgCR5HgQWgBmNYzOLESskW8CRH6nOdtYcD0kngstfy7yfpCdT0h0AL9G45ApKyPkP66io6hChQ5jZhh-2hEn5PaC8FYlzaOPZTEGvlkbcmHzf9dTDzO0BL-hFVlI_kMbkYg4JDi64yVkJ2IoP_ULLxqJfdUJAfuUUpoM95_QHMzMCw2cmLXwLtuzyU2mVU_kt2OhmQdCz4MnUdownaoLOB8ptUN2IdCopHJ5fOVnAcnruFdU46YeuBvmapFj9HQ45FZnWYJj-9Br2WFJchgXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
هفته‌دوم‌
لالیگا؛ بارسلونا با گلباران الچه برای رقبا خط‌و‌نشان کشید
الچه صفر - بارسلونا پنج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/104524" target="_blank">📅 01:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104523">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1623eb570a.mp4?token=RJZG_wG71Gq3mc75R3jBsIjk3XDUi5H6JZTmex7hzixVHAD1TTJVu7uFn_YkRkSNwiJzXBkFAtmwETcJz__9zODAOVBN1Wp9ot5kluGwfzr7jidbfXYU11AcczUEYJs_Tk3Vv56AoIDd3c_kgy9cM-UADiMhoqBAp3Lpb37tEbLKNWZ4GcY_AAeveh7IiIeVpRrh-YCXcGjeKZWSGH0GDwBd4FiDWtVzCkWv-ueZwNdIEBrfdltwlpvBLCGKg2IUb3Rq8dmFYJ5ZzjPxM7uABGWct40F4grQ_LMhMQm8h7rPWtLXf4V8dbTj7Nh9wwatTwT6NX-g853EUxOv5bgkqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1623eb570a.mp4?token=RJZG_wG71Gq3mc75R3jBsIjk3XDUi5H6JZTmex7hzixVHAD1TTJVu7uFn_YkRkSNwiJzXBkFAtmwETcJz__9zODAOVBN1Wp9ot5kluGwfzr7jidbfXYU11AcczUEYJs_Tk3Vv56AoIDd3c_kgy9cM-UADiMhoqBAp3Lpb37tEbLKNWZ4GcY_AAeveh7IiIeVpRrh-YCXcGjeKZWSGH0GDwBd4FiDWtVzCkWv-ueZwNdIEBrfdltwlpvBLCGKg2IUb3Rq8dmFYJ5ZzjPxM7uABGWct40F4grQ_LMhMQm8h7rPWtLXf4V8dbTj7Nh9wwatTwT6NX-g853EUxOv5bgkqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل پنجم بارسلونا مقابل الچه توسط فرمیییییین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/104523" target="_blank">📅 00:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104522">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">این الچه بنظر خیلییییییییییی بیش از حد تصور کیری میاد. دفاع کردن بلد نیستن اصن
😐
😐</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/104522" target="_blank">📅 00:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104521">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گلگلگلگلگل پنجم بارسلونا فرمین لوپز</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/104521" target="_blank">📅 00:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104520">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff874a3d34.mp4?token=CebpsPAzb-WuTSOzyuwazsJmLthYUeLb5M3moeycjsqZ3aFH5kWhR18kaEGXEQqsJHsFT2TTUP-3Rv6vyFGqChEw3go5NAepmu5FER7PuNTsorTiAt_dkVp5fe4NkXXj42Bu5KEDo32te0WB16LPa8NZFh-_Q0kd_-39TvZ1bOMjgNNKOrXaO1aEBNMFIR6bmYjokmACKCSLyEOkATLale4ePlV7mqntEnW91xwnB4TnT8tM0fP6Pume9XWNbf32djyKipx7UAi-zfj8SuMnP-pXTSVrIIj5hElG9W5VFMqibQ8bkK5qkF3NPwuNf7xv2Zxz3L0OShp242PusEE9vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff874a3d34.mp4?token=CebpsPAzb-WuTSOzyuwazsJmLthYUeLb5M3moeycjsqZ3aFH5kWhR18kaEGXEQqsJHsFT2TTUP-3Rv6vyFGqChEw3go5NAepmu5FER7PuNTsorTiAt_dkVp5fe4NkXXj42Bu5KEDo32te0WB16LPa8NZFh-_Q0kd_-39TvZ1bOMjgNNKOrXaO1aEBNMFIR6bmYjokmACKCSLyEOkATLale4ePlV7mqntEnW91xwnB4TnT8tM0fP6Pume9XWNbf32djyKipx7UAi-zfj8SuMnP-pXTSVrIIj5hElG9W5VFMqibQ8bkK5qkF3NPwuNf7xv2Zxz3L0OShp242PusEE9vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم بارسلونا مقابل الچه توسط فرمین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/104520" target="_blank">📅 00:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104519">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گلگلگلگلگلگل چهارممممم بارسلونااااا</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/104519" target="_blank">📅 00:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104518">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گلگلگلگلگلگل چهارممممم بارسلونااااا</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/104518" target="_blank">📅 00:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104517">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ac58b5d2d.mp4?token=Yw8v1qQReg9VCpSBo4egIVUt8pt-r1ZZhYFoNvVLr3_6jhldPJgKnoyQqNJj5-PCmswKXV0lc0oiFpc_Ll9pTECVe6kmmyeB9sL6LzV6YVgkIJhJQYGah-7RaNDJOxLAfCW530VWXvMc065o75KlyhHXKnM28IjktPqCBQYknzuV9VME-xJvi3198ZJFjYSW-QWzl_zHkxGYAloJpoojVsM99xYz1IBCuvFYN2a-wt-9zsPEFGj8_bY8DHBlQgDMhAAIR3xS0ef-jrQin5b44JSh1cW7kZr_C3tIB7-zt6qfjuabCxjfatG9G8ygps-mI-xBNv2nvkiiWkPMzCAZpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ac58b5d2d.mp4?token=Yw8v1qQReg9VCpSBo4egIVUt8pt-r1ZZhYFoNvVLr3_6jhldPJgKnoyQqNJj5-PCmswKXV0lc0oiFpc_Ll9pTECVe6kmmyeB9sL6LzV6YVgkIJhJQYGah-7RaNDJOxLAfCW530VWXvMc065o75KlyhHXKnM28IjktPqCBQYknzuV9VME-xJvi3198ZJFjYSW-QWzl_zHkxGYAloJpoojVsM99xYz1IBCuvFYN2a-wt-9zsPEFGj8_bY8DHBlQgDMhAAIR3xS0ef-jrQin5b44JSh1cW7kZr_C3tIB7-zt6qfjuabCxjfatG9G8ygps-mI-xBNv2nvkiiWkPMzCAZpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم بارسلونا مقابل الچه توسط رافینیااااا
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/104517" target="_blank">📅 00:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104516">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91d25fa697.mp4?token=V_wDaiaY7lc4jGHONTK0f-UfflpFBv6wJpvMTpgoEcIm-7xIGMEVSQuU1LhS8q2c5bG3D2SgKFqu55dMnyowUGZjcpV__mvFfoCPruI9NDYw2zlZFdZ8-b6lkLQTJ0r2elRIZvOFUkpugjZN-Z5PoSRYkcNs35P5LtU9ZNBLy_TLyJU0N3KOjfDoCI3hA-_DejBt3KHSIVFL4jn0FFx5-SeJChtAcLVCJsA2Sj6WTT3Mu37uSGE31Kibmk1F5GN9jOaDO2dcRSVjs5bz4MfGZAknFjCKnV6lZjqu1ZT0pMMbNvY2QQtR3pDTcqJOarbsLMxBn9LP69mRRe5Uv9NMTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91d25fa697.mp4?token=V_wDaiaY7lc4jGHONTK0f-UfflpFBv6wJpvMTpgoEcIm-7xIGMEVSQuU1LhS8q2c5bG3D2SgKFqu55dMnyowUGZjcpV__mvFfoCPruI9NDYw2zlZFdZ8-b6lkLQTJ0r2elRIZvOFUkpugjZN-Z5PoSRYkcNs35P5LtU9ZNBLy_TLyJU0N3KOjfDoCI3hA-_DejBt3KHSIVFL4jn0FFx5-SeJChtAcLVCJsA2Sj6WTT3Mu37uSGE31Kibmk1F5GN9jOaDO2dcRSVjs5bz4MfGZAknFjCKnV6lZjqu1ZT0pMMbNvY2QQtR3pDTcqJOarbsLMxBn9LP69mRRe5Uv9NMTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
🇮🇷
تمسخر گویش کنعانی‌زادگان توسط هوادار تراکتور: تونستید بایسا و یئال رو ببرید؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/104516" target="_blank">📅 00:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104515">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d106b59a1d.mp4?token=hyPCozUjrdF_ca1egKxYxk_jZwKSkV0cPpdr6vLOjtEj5Hjq2cMPklcCuQrmbH7kPu90meEyxl_QrupQkDwcu-chXndcePNrdAv5yINid_zqHveTOqmXSeuQ4Jp0OzF1zDTtLCr7RPFrYeeiYa3-RVV6xcjZL3nzPbM-770FybirsVg02EtFutK3F9mlUhVidK1Mx-AYoTOaPkye9QZOydbZ5owOQfz24pRELBXA-Fc9KPwXimFRok9Yb50t9vCOr07li020ZB7NO9xEJ7rTE_T-iSHip-v6yS0vJXZc5jxtM9-Blau9Fuj85BjyN5VNpqeA-vNyjAF37rG7OkrqC3B4-DFVskcE-sBn_9I8KnJ2cLYdVZehDw-wzc3zZHvWjUHmlim6gz4DozK9OSt1PWHn7xlm6fBV2YyXW7sN2wCBQs1PCpJ7tssHYTpD9lj-xg_TnlNBWm02TZUsbAsZXZrraY4kz-H3haMPUO6P-ll6oZKrzWwbcNfygW2ZC7ES11JTIcQ9UXnDY_nHzutJvuTVNN2nQW1ulukqjKbM9StLo4VGY_c0XYfZlMnMb3JAvIXYGL3b7NuDAEWIHIm8vloMbBkNQrWA0Tu9Nj1QgSL01ot1lUupLhHtxaiRUzkxPqVUQTkinzqlwX08cl4XtbQ5EDPo02GnJ_vzOib2Dxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d106b59a1d.mp4?token=hyPCozUjrdF_ca1egKxYxk_jZwKSkV0cPpdr6vLOjtEj5Hjq2cMPklcCuQrmbH7kPu90meEyxl_QrupQkDwcu-chXndcePNrdAv5yINid_zqHveTOqmXSeuQ4Jp0OzF1zDTtLCr7RPFrYeeiYa3-RVV6xcjZL3nzPbM-770FybirsVg02EtFutK3F9mlUhVidK1Mx-AYoTOaPkye9QZOydbZ5owOQfz24pRELBXA-Fc9KPwXimFRok9Yb50t9vCOr07li020ZB7NO9xEJ7rTE_T-iSHip-v6yS0vJXZc5jxtM9-Blau9Fuj85BjyN5VNpqeA-vNyjAF37rG7OkrqC3B4-DFVskcE-sBn_9I8KnJ2cLYdVZehDw-wzc3zZHvWjUHmlim6gz4DozK9OSt1PWHn7xlm6fBV2YyXW7sN2wCBQs1PCpJ7tssHYTpD9lj-xg_TnlNBWm02TZUsbAsZXZrraY4kz-H3haMPUO6P-ll6oZKrzWwbcNfygW2ZC7ES11JTIcQ9UXnDY_nHzutJvuTVNN2nQW1ulukqjKbM9StLo4VGY_c0XYfZlMnMb3JAvIXYGL3b7NuDAEWIHIm8vloMbBkNQrWA0Tu9Nj1QgSL01ot1lUupLhHtxaiRUzkxPqVUQTkinzqlwX08cl4XtbQ5EDPo02GnJ_vzOib2Dxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بارسلونا به الچه توسط کریم‌آدیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/104515" target="_blank">📅 00:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104514">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb0b5f685e.mp4?token=UG0v5dHDHA1uoaLjMwZQmsDROYgrDR7_k_lpOxUn2HAL63RJyO-4u4Wh7RCyo9KwE0J9j7AVu4Z4pmJfudO0pR71vGIJaPGmRxXV7X_qN_Q79iqtAar2DX6wsHCx90ICit2nNEhfspm975zmaNVN95Mc4qEUdUd8iFBGZ_KBIPICcaZDfLGTGsmG3hXmjy64DUO2MCn4eUpGMK7xwIzoZlvDITpUSstGrJBxTFNW7x3HE1wBKNzEvga1XxRT34sGn4XzTNT-MCwRbspsvMx1LG5I7EjWijdejxPUQBYeFebNzhkXE4t5Ysrd2sv3a6Hysp0fLKUdzKNHpKwgpkyhU4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb0b5f685e.mp4?token=UG0v5dHDHA1uoaLjMwZQmsDROYgrDR7_k_lpOxUn2HAL63RJyO-4u4Wh7RCyo9KwE0J9j7AVu4Z4pmJfudO0pR71vGIJaPGmRxXV7X_qN_Q79iqtAar2DX6wsHCx90ICit2nNEhfspm975zmaNVN95Mc4qEUdUd8iFBGZ_KBIPICcaZDfLGTGsmG3hXmjy64DUO2MCn4eUpGMK7xwIzoZlvDITpUSstGrJBxTFNW7x3HE1wBKNzEvga1XxRT34sGn4XzTNT-MCwRbspsvMx1LG5I7EjWijdejxPUQBYeFebNzhkXE4t5Ysrd2sv3a6Hysp0fLKUdzKNHpKwgpkyhU4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گلزنی فران‌تورس در بازی امشب پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/104514" target="_blank">📅 23:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104513">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50615b177d.mp4?token=SHRZQ9l_wTx9irEOQAnXhREeAKRSmEEn2eR1BLzGdrrdSPEZZYAua9SKLkcDLTdZBcE0gTkBAKJL_hmYVloXG6FpB7S0O3erQhZaUgmRlIWtl2scatyLoy8FhZpCPk8Ud4SjGfo6X6c1SBoNPA4k34GAiXrVFqOmSl_o_o2Yp_iJiXP9C5Kvbk94KxpSN-hFGXxqcYkoSPtRd4ilCw19qSPW4x9R5gc2qEJbwg79rzCdcTC9KdVJLvISKDYgHyVABgkxgCEfAmJMd6LhqVFshrLC8-a2BIY1UxjROsbub-MCqixryHr5cyn78TlTt7oyIRvBg6GJqs9g6EbmAwKp51EBQVNHA2b7xoAt6zYMM54nJenAiKtBDT3AZBTLgIL43npDPTzNWWrNx1yv2JgJoyi9vRradqi8ZZbLruc3GUeggFuEstXbTan2vmHa_t42lAqaYXEFOqRgnnwHeTV39m1nWsdQxUBwG9fR0KgT4yWYG0KR8ymXuMKzWu5BNq1hapKG36nJ_PLggXbYHPNkhNZXpENN6DsGUVF-60hUTWyy1iiG7G7rNQxVVupOvpNNIDYLCZ5bZlee6IEQOyZjBdVWmH0Q0O8qyvFz3OqTMQHaDGXvwrYlq8x7XT4FPwgV1Usr6KN2xV4g38aAMboud45qRLbv70YHTTwk7ig6ZZo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50615b177d.mp4?token=SHRZQ9l_wTx9irEOQAnXhREeAKRSmEEn2eR1BLzGdrrdSPEZZYAua9SKLkcDLTdZBcE0gTkBAKJL_hmYVloXG6FpB7S0O3erQhZaUgmRlIWtl2scatyLoy8FhZpCPk8Ud4SjGfo6X6c1SBoNPA4k34GAiXrVFqOmSl_o_o2Yp_iJiXP9C5Kvbk94KxpSN-hFGXxqcYkoSPtRd4ilCw19qSPW4x9R5gc2qEJbwg79rzCdcTC9KdVJLvISKDYgHyVABgkxgCEfAmJMd6LhqVFshrLC8-a2BIY1UxjROsbub-MCqixryHr5cyn78TlTt7oyIRvBg6GJqs9g6EbmAwKp51EBQVNHA2b7xoAt6zYMM54nJenAiKtBDT3AZBTLgIL43npDPTzNWWrNx1yv2JgJoyi9vRradqi8ZZbLruc3GUeggFuEstXbTan2vmHa_t42lAqaYXEFOqRgnnwHeTV39m1nWsdQxUBwG9fR0KgT4yWYG0KR8ymXuMKzWu5BNq1hapKG36nJ_PLggXbYHPNkhNZXpENN6DsGUVF-60hUTWyy1iiG7G7rNQxVVupOvpNNIDYLCZ5bZlee6IEQOyZjBdVWmH0Q0O8qyvFz3OqTMQHaDGXvwrYlq8x7XT4FPwgV1Usr6KN2xV4g38aAMboud45qRLbv70YHTTwk7ig6ZZo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حضور هواداران مقابل هتل پرسپولیس!
🔴
تعدادی از هواداران تیم تراکتور مقابل هتل محل اقامت پرسپولیس تجمع کرده و شعارهایی سر دادند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/104513" target="_blank">📅 23:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104512">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/66baa2f686.mp4?token=IeUnIoYg48n4GkpX4qsfxCWvocwgaPBwdj9lVVNRKxFMd3kqnOPUF8X3eT4fEtshLGyd7otnnXTm9y1j-edxKYGEY6O5rbdDuzgZaTMleqALU1OlMqiH53MemUr5qix8LAhH8mivB0Igyg3s-mCfCkFgzRdYWREwCouqNPCH0-ZGljyQaOgqfkrAzUTy_BzSx27wvJVFPMLYHlFbqiEcI35FFURbMQQZYYjjUJj5FD15Lwlhzp_Uinl59tz8sJzP2AfCPXz2zK5W3YvCaI5-oZKGl19TVgfKUoeiZZUuGEdYnhthjuMvuERH3WMSm1KrjE2zqqyAFBKaB0tF_I8U9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/66baa2f686.mp4?token=IeUnIoYg48n4GkpX4qsfxCWvocwgaPBwdj9lVVNRKxFMd3kqnOPUF8X3eT4fEtshLGyd7otnnXTm9y1j-edxKYGEY6O5rbdDuzgZaTMleqALU1OlMqiH53MemUr5qix8LAhH8mivB0Igyg3s-mCfCkFgzRdYWREwCouqNPCH0-ZGljyQaOgqfkrAzUTy_BzSx27wvJVFPMLYHlFbqiEcI35FFURbMQQZYYjjUJj5FD15Lwlhzp_Uinl59tz8sJzP2AfCPXz2zK5W3YvCaI5-oZKGl19TVgfKUoeiZZUuGEdYnhthjuMvuERH3WMSm1KrjE2zqqyAFBKaB0tF_I8U9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول بارسلونا به الچه توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/104512" target="_blank">📅 23:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104511">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d8a179a36.mp4?token=o-hl9ThgImiokJoRoez8ToM1BoRgXxUaTTlfp8zRVrZxdX4IN0PWVOMcVRYHUqlgFkKNgs8_nKU1f2WvCoPp93MuJixgUTLASEBnhK5p1IJ9mN95rBLYjzhe5lmd8WdiXZX00IzfuXNQzzL42u3oBdrx81NeM5zSySiE1rBP24xDEHldN5kwJzlNKhMe5fNM_exyZZFJc1Y5rr7woYBjAQ990NWS9m7lLsDxmU9i53G2yM3QSXDeddX7VLZFaIaC-XUx2ppfAuSf0Gb3u9-oLnagCoHktV582iVxeag0A2BSzr7VE4peHJLVY6RNWSu4YbqsZkq_e5nmNT-wU1S3H5AYYvq9MApZAM8kdRSqeLxYhOkd1o8rSPFQbFr3lqwlLe-4jPPE7YA5--DDWkpyg2SFNGhxfaw4ZJ68llzLo6CPEpjs5vo4kouj5xeagDz-dVMq-aYSmOfP3QBuOo5Bu8Dn7DRpp8E3lOuz4c3oI7ZQSDtDJKcDJZRi0q7t-qoNdI8sx3tIgBcFqGXlr13fkchhhLBmlNbMTesCus82TOn1Ffjr3Gj7vsAjcAYqStKjdxBMOge4QVonvVCntoL1WLWVzCN_gIBumZV_pw-t542sP5HuTvntqrL_aedImLzkBPnyNJ2ZL0o7ApB1lTn7eFbC1ifzjF73F6Jc3vvTNZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d8a179a36.mp4?token=o-hl9ThgImiokJoRoez8ToM1BoRgXxUaTTlfp8zRVrZxdX4IN0PWVOMcVRYHUqlgFkKNgs8_nKU1f2WvCoPp93MuJixgUTLASEBnhK5p1IJ9mN95rBLYjzhe5lmd8WdiXZX00IzfuXNQzzL42u3oBdrx81NeM5zSySiE1rBP24xDEHldN5kwJzlNKhMe5fNM_exyZZFJc1Y5rr7woYBjAQ990NWS9m7lLsDxmU9i53G2yM3QSXDeddX7VLZFaIaC-XUx2ppfAuSf0Gb3u9-oLnagCoHktV582iVxeag0A2BSzr7VE4peHJLVY6RNWSu4YbqsZkq_e5nmNT-wU1S3H5AYYvq9MApZAM8kdRSqeLxYhOkd1o8rSPFQbFr3lqwlLe-4jPPE7YA5--DDWkpyg2SFNGhxfaw4ZJ68llzLo6CPEpjs5vo4kouj5xeagDz-dVMq-aYSmOfP3QBuOo5Bu8Dn7DRpp8E3lOuz4c3oI7ZQSDtDJKcDJZRi0q7t-qoNdI8sx3tIgBcFqGXlr13fkchhhLBmlNbMTesCus82TOn1Ffjr3Gj7vsAjcAYqStKjdxBMOge4QVonvVCntoL1WLWVzCN_gIBumZV_pw-t542sP5HuTvntqrL_aedImLzkBPnyNJ2ZL0o7ApB1lTn7eFbC1ifzjF73F6Jc3vvTNZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
نویدکیا: از اینجور تیم‌ها حالم بد می‌شود
. امروز نمایش هفته پیش را شست، برد. هیچ بازیکن باکیفیتی امروز نداشتم! امروز هیچکس را نداشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104511" target="_blank">📅 22:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104510">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7icfMK2fCciLDKi4QoA4OJqcD5aqJGdNApr7_4j6sDcNi149HLY_-xRp-rKfl5Z9tGawQVW6jFrMsY_Bjo_tsRvLG46Hs7MKrXn3wLU0QPYZxIUaesItfnFprvshSm3hczZ19bP4qSMYVj8JnEHl0sBZVv5gBIc7hTIJSjg3d3L6Idm1zMIkVzoBjq1dwHosomtHvSNmNd9c64WCgViROOlGnhru96L045h1Hy9RsHsKlENCNB5lD5-V0GSSxnWiOBoaq7LvYHV0FV84a7jLoOTZSCqqU1Yz1suIu5qf__74JZPTmJAvfBzthXXC_lj3DzOpBnm0BveY_7E4SEa1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
#فوووووری
؛ باشگاه سپاهان از استقلال بابت استقلال از یاسر‌آسانی شکایت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104510" target="_blank">📅 22:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104509">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
‼️
🎙
بختیاری‌زاده سرمربی استقلال
:
🔵
من هرگز صحبتی از پنجره بسته نکرده‌ام چون اول فصل گفتم که بازیکنانم را باور دارم و تجربه نشان داده تیم‌هایی بوده‌اند که با نفرات کم، نتایج بزرگی گرفته‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104509" target="_blank">📅 22:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104508">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a46aea259.mp4?token=CBtBWmrVpfmTme1ITUgjw4NLhC1SazBU0-xQQU_sXI0FRkKQUNIM3gHNn4fOGuCldgcqvAwrUFEdQmUpjYVPuhN78h0tqE3_R0q2neHey0La1Ep-tNZwNJ3Q9dW3ZaKaa4GhBok9rPsEf18pK50WgOpxZkTpUUMJyK2FghKPidGOGFHKt5bIzA20rHPN97kU9qLj3h8rW6kG050j8BIM8U1iIfL5qx5JyOQX8ZP9gep0hz5I7_ad5sqNI5zNYSfYrfL_S2d9BUn-IXJrVcdODuR9xsqOfZOZ2S2dXjc-dB0xNF_QGDlyKkhk1EdGuLUjP3xpr6VzmYws1XWkIcmGzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a46aea259.mp4?token=CBtBWmrVpfmTme1ITUgjw4NLhC1SazBU0-xQQU_sXI0FRkKQUNIM3gHNn4fOGuCldgcqvAwrUFEdQmUpjYVPuhN78h0tqE3_R0q2neHey0La1Ep-tNZwNJ3Q9dW3ZaKaa4GhBok9rPsEf18pK50WgOpxZkTpUUMJyK2FghKPidGOGFHKt5bIzA20rHPN97kU9qLj3h8rW6kG050j8BIM8U1iIfL5qx5JyOQX8ZP9gep0hz5I7_ad5sqNI5zNYSfYrfL_S2d9BUn-IXJrVcdODuR9xsqOfZOZ2S2dXjc-dB0xNF_QGDlyKkhk1EdGuLUjP3xpr6VzmYws1XWkIcmGzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
آسانی : مهم فقط 3 امتیاز بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104508" target="_blank">📅 22:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104507">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f173b09f.mp4?token=Xr8U453H3xELGpPkMXd304eP4zcQDry7Usp0qCLl5hiX5-UAO_VKA35V5KY8YyiZefm-ENHFOJqA7hKe9fdomw6FO5sB7tWGpvWh1sOh84L5TZyTs2aWBX3bMA6bM1kjeRHiAA4uv1VgWcj4n5uQjBg9nWr7uC74c_15_vb-y7Z-V-BlV7DCPl9kXwk4yvctvbNIuntTkteCwPtREj-d1TogjrB24Hqb7zZj8FRIIzVOCGXJanm6EWTdDeiXj0V6AzVlE7iXw7KRxUApShYa3dEFpwkYYaFqkh6i4tztVXZW0-t3_g9Certk9UpH8hfH6OAoEW3B1aJAbchqxErDLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f173b09f.mp4?token=Xr8U453H3xELGpPkMXd304eP4zcQDry7Usp0qCLl5hiX5-UAO_VKA35V5KY8YyiZefm-ENHFOJqA7hKe9fdomw6FO5sB7tWGpvWh1sOh84L5TZyTs2aWBX3bMA6bM1kjeRHiAA4uv1VgWcj4n5uQjBg9nWr7uC74c_15_vb-y7Z-V-BlV7DCPl9kXwk4yvctvbNIuntTkteCwPtREj-d1TogjrB24Hqb7zZj8FRIIzVOCGXJanm6EWTdDeiXj0V6AzVlE7iXw7KRxUApShYa3dEFpwkYYaFqkh6i4tztVXZW0-t3_g9Certk9UpH8hfH6OAoEW3B1aJAbchqxErDLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
رستم‌آشورماتوف که در پایان بازی با لنگیدن از ورزشگاه خارج شد، مشکلی برای بازی بعدی استقلال مقابل فولاد خوزستان ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104507" target="_blank">📅 22:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104506">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4773567450.mp4?token=sGea9d5NwG2_b4vA6KP2TPMevheiyCUN0wRXFN7qKOBCkj1NLwyDBt2hFKo_RMy8emM5aFMrb_qAQoCY62az_0EiM2nlUOw_yiKVNTNHjg_72-bs7SHuw-MHvWNpDWICLBVOvm0BqB-1odbzjxdsdWkLfnJToTGyKpdqTqs0lZd-k-tec6iq6f3pGMOY2W4mU9eKHmeCUgpnmGUPz-N3iH1Nuep82NnxGk0F_WujnCglfLU3uzkcHRGPL-c4ORoJq7Voi8XUGVpfz9bqtIBdowqyl_LrTLMkAxv7TcHNRpVgQM0nCBpPVVSKXzVDKp6blNKm5uYdte4T3f-nQc1uzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4773567450.mp4?token=sGea9d5NwG2_b4vA6KP2TPMevheiyCUN0wRXFN7qKOBCkj1NLwyDBt2hFKo_RMy8emM5aFMrb_qAQoCY62az_0EiM2nlUOw_yiKVNTNHjg_72-bs7SHuw-MHvWNpDWICLBVOvm0BqB-1odbzjxdsdWkLfnJToTGyKpdqTqs0lZd-k-tec6iq6f3pGMOY2W4mU9eKHmeCUgpnmGUPz-N3iH1Nuep82NnxGk0F_WujnCglfLU3uzkcHRGPL-c4ORoJq7Voi8XUGVpfz9bqtIBdowqyl_LrTLMkAxv7TcHNRpVgQM0nCBpPVVSKXzVDKp6blNKm5uYdte4T3f-nQc1uzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
🇮🇹
🇮🇹
یوونتوس در هفته‌اول سری‌آ با تک‌گل برمر مقابل فروزینونه برنده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104506" target="_blank">📅 22:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104505">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d5a7c170.mp4?token=voVH5PWizndORMonj1dWKsENRDWnPuCgzKzqPRLQKHdCL55DLtuVVEIpInqJ58SixPwlJNR_3i5OClBUSThqPtO_a_JMxySgwqEO3bfqDxYThPMJIJKB0MZyZmgbjocxPtJPDcHBVBiRFMZ2YOXhixQLv31UVH6ZtlnN9xRQx0k3aNk3EtwFuWWyRF2WM302d_LvDuFtuzIB_rBiKWZVEvc8QY-YBPeWq0CS8Kftdb1D2aOCIaW4dVxSFWQ4K500ibOq42DkGjlS45BcyfxuOHYpPqr2q5uilIN779AVfElyuLujG6-xt5OaSWjkWdOx-D9QTdJDqQow1OmrrnO6W0JygkbZFGa3E3a2T8OH8SBq0GXy7OdlkyabSZnwnbdqsgpYssMoPvxOVElPsOFx367kxha92jydyK2nBeFpJVUiX92XQ4GathJgepf9MNtu7oSkq8WeKCQVsGpj9SdHePcPNKRhPK6tdmoS0IJhQzY49xjr2sXXm9ilpUOx-i4OKBdv9cb89xn_-6l9mtOBfVuKz4OSDfsaR_8h1cuIrWJVO62_0kC9nqyn4eT_Sx4_2ht5OQL658AFuPiqiyQh70MV5lzu6thN5d9TkjHqDiF0p5m8H50k3o6JUYlwVMigCGGu6bqAn4LHSNyuBCfcvRLKTsjZpImisxJnMN67ebE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d5a7c170.mp4?token=voVH5PWizndORMonj1dWKsENRDWnPuCgzKzqPRLQKHdCL55DLtuVVEIpInqJ58SixPwlJNR_3i5OClBUSThqPtO_a_JMxySgwqEO3bfqDxYThPMJIJKB0MZyZmgbjocxPtJPDcHBVBiRFMZ2YOXhixQLv31UVH6ZtlnN9xRQx0k3aNk3EtwFuWWyRF2WM302d_LvDuFtuzIB_rBiKWZVEvc8QY-YBPeWq0CS8Kftdb1D2aOCIaW4dVxSFWQ4K500ibOq42DkGjlS45BcyfxuOHYpPqr2q5uilIN779AVfElyuLujG6-xt5OaSWjkWdOx-D9QTdJDqQow1OmrrnO6W0JygkbZFGa3E3a2T8OH8SBq0GXy7OdlkyabSZnwnbdqsgpYssMoPvxOVElPsOFx367kxha92jydyK2nBeFpJVUiX92XQ4GathJgepf9MNtu7oSkq8WeKCQVsGpj9SdHePcPNKRhPK6tdmoS0IJhQzY49xjr2sXXm9ilpUOx-i4OKBdv9cb89xn_-6l9mtOBfVuKz4OSDfsaR_8h1cuIrWJVO62_0kC9nqyn4eT_Sx4_2ht5OQL658AFuPiqiyQh70MV5lzu6thN5d9TkjHqDiF0p5m8H50k3o6JUYlwVMigCGGu6bqAn4LHSNyuBCfcvRLKTsjZpImisxJnMN67ebE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📊
عملکرد سید‌حسین‌حسینی مقابل سرخابی‌ها:
🟥
پرسپولیس: ۱۵ بازی، ۶ باخت، ۹ تساوی، ۲۱ گل خورده و فقط ۲ کلین‌شیت!
🟦
استقلال: ۵ بازی، ۲ باخت، ۳ تساوی، ۱۰ گل خورده و بدون کلین‌شیت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104505" target="_blank">📅 21:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104504">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7ToHGZWsrSrPyufo_FmdzdtV4NhI8fC2TLPoN7-lT2WiLDS3c89KUCcsUdYE1PUaSYG_3LR60IP4EuFSdgdeAh4Wh59KDiqIjS1kpJXuQJw1RrWVjGW-50JToJb1xrQT3Vx3Z9b-Q3h1GoF4dD3e83ky21CxrunJef8pmsmJ1AGdf0ndihIaWYFv_rGK_tmIUFwjgDoMsKXK9lurx6ggMtLO5x-9IesgBvn6CInhYiz1cYbZNA44zdSIr0wBadgEv3sR3rGkHfXRhXU_J6gV7mWeZg0_wC9IhVcKFke8P3PUlWct5ZUImLzP51lP9OmMkEZPhuA9aleM0FWal-J1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
از کیت‌دوم باشگاه پرسپولیس رونمایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104504" target="_blank">📅 21:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104503">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wk_oXfnl1LHxucNHG9ZPg0KAHS-5j5eMP7X1zMVsCbxRDIobVeJXdXfk82My2ZHp7YHGVdXZqRVFcqmNVC6JrLum0JYyE2NrS4z1tbLxi6R4qTyuOpojueUA-m34G1Ke9xWdEgGntl5t29XjlKnz1aE2xIfgvGa4W9lHiI3j_7RwZQ4mbQcgXmHQXp_3223szeFL5uVnXF0E9TNX_BH5VdOf4ScolaWotyIZ7SK5CjJY7u1ANRhYfKzZo5TxkJLwmTte3XzMnELd1_9e3DZ7WYSkFNyFgXSIOCEczxdLgvbczNtZBaLcOfjmelUvwmZtozCa-WiiryhlCCuYra0c1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
ترکیبببب بارسلونا مقابل الچه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104503" target="_blank">📅 21:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104502">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNhCjL6S9Giti8vpzSjWsjDHJeerB-5MPuHOcJWtBRTeagtqiPf7bR6aW_8pfNUhMfUZ3GEfa1m1BrBTUEG5jYvzIbZw8ASqm_BosaQLB_CVA_vpPa9kipTubffAL6ulMRgvhfdkfzqkP1f9HoUFSDpuhJAzZJwI9tWVNcQ8epaXGs_1ZHRq443zxR8ORCCwCXi0RTR0fT_U_a2HuzumFbSHkpe0nuwLVLEQ4u5-E4yNNbW4qt8wP8Vi8scsWsQxEBNaYfvsosITSzgus12-5ErRnT7KYoNo9wxv1aXQQyxLtrBsjBliyXTF0cic8Du48aLs1sJB9IueDagJ_3OWrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
ترکیبببب بارسلونا مقابل الچه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104502" target="_blank">📅 21:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104501">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8eXddpNDd_iXjGbjz-t03tUySXKKGqVb8f4iBASVShKfdV79Iqz0EmnEVXE_AzDIRtTU_yQQSF3tGETiO5dDukUSpPbCCs0iC2lsyyoH6RixR8Nw-PyVVvP1zPjlwweMVhU68p6nhPwV_RHb6exwWIBMI9RxL6wRzFI2Lug4Fnh-AvduUZjVk9TK4qOLtrT6tQ3_gpCE9ezTEIwrXW4SnWcRYBn3-xWxztJUoaj8SuO9o_iVJ2Cx3bK8uBbFqcwdER6c-Fws1zUyH26XW3pFiLkvjpRC0clWaAutLE-Gec7RhqsUUoGxF8rzLfSupCyknR3_xeGvicPHgy_7FO3uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته دوم لالیگا اسپانیا
🇪🇸
الچه
🆚
بارسلونا
🇪🇸
⏰
ساعت ۲۳:۰۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ ‌‌بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104501" target="_blank">📅 21:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104500">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ec3ad2dc.mp4?token=bSZMNNzQDSGfXApWNZ_-IpJtO4P3D1JEHC-cIllXSXPGPTzWMxMt_giqjJUvohd0TOyosxj-rCZ4bIC-LvNf-WNzdB8Jm-Yi7oFe7zvew73qakQHrazx30sDZHbYImwf6Rlpx86xL4_yyhCVBxyi7RlAeJebguMmSDLmpwAW8LthVfg6H2t6njSwmsQ_JzC4egPVUf_VepXyrk_n0iRu20iHzyiA29plRPeJnMNXTjSWi59E71TkOYaKrC_GkueTw_Bvr867I-B2y5jVmq_L4w9k1wn2lCOltDX0n6QVKZ5MiSnbK0ht-mcKYe2o0WDnmqyW44Z0tX1KGzS6zDwb6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ec3ad2dc.mp4?token=bSZMNNzQDSGfXApWNZ_-IpJtO4P3D1JEHC-cIllXSXPGPTzWMxMt_giqjJUvohd0TOyosxj-rCZ4bIC-LvNf-WNzdB8Jm-Yi7oFe7zvew73qakQHrazx30sDZHbYImwf6Rlpx86xL4_yyhCVBxyi7RlAeJebguMmSDLmpwAW8LthVfg6H2t6njSwmsQ_JzC4egPVUf_VepXyrk_n0iRu20iHzyiA29plRPeJnMNXTjSWi59E71TkOYaKrC_GkueTw_Bvr867I-B2y5jVmq_L4w9k1wn2lCOltDX0n6QVKZ5MiSnbK0ht-mcKYe2o0WDnmqyW44Z0tX1KGzS6zDwb6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اعتراض شدید هواداران سپاهان پس‌از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104500" target="_blank">📅 21:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104499">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b1603e46.mp4?token=MVKSedKhOBXDP0kLEEAywe9--k1sjGCBbxUXxuB7fWVIxjHppfpxzmoju-rb9UrY6P9peJDN-mSFWeHn2HWr65ChZA7h05zWSMUfgzS_Ofbfcy0s3l84_MISZwJK9_1s_vuNM_qocJnRGkx_Rw3r_Cgi79ObNFGekrouIU-HJXGJ_DuFywId5Pusk_MOuAhN3KLo6QezstJmRcDoT_sXQb3_v7fxdMH5lndXbTi_3VNjvNKZ88IzlO0WPNOCVSGIC9owA9PstmaC0gHTGUflf_Oymv-C8hJVJqdhEwoytdjUFcuXN6IiC4N8_m9JGdC00aV3IEyZipDuTbzHMc09mHCMQKLpNdzZq1aTjmbW74APjDvFS3zONJEg7Cn4zXKynqf3WDwQXUQ-iDPXQrP_5rKPk6bv_YrV1aaaFeny38FJqUNaJNX_RR7MQdmbfWVyWJNxAsZ9qQ0paZCABvR_vZN5AYdMCEN37BIfnW-9pOuLPq87VkIQt3sbuS0ZLpfL4KMpAS4dcp39IykW5LNYXZ57HaYeYLrV4yeLNtd0voB_gjJNIVB8H3tNmS0o1kzpwTZnIhjiNm4etAoORnT7N595lvA8Ua1N8brMzBZ4UnOm1d4XV8U-6eym9Uz9CmV4Fz5mH9A_xXVf0KjELoZV_muRKJBIV4l1L7jomdigE5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b1603e46.mp4?token=MVKSedKhOBXDP0kLEEAywe9--k1sjGCBbxUXxuB7fWVIxjHppfpxzmoju-rb9UrY6P9peJDN-mSFWeHn2HWr65ChZA7h05zWSMUfgzS_Ofbfcy0s3l84_MISZwJK9_1s_vuNM_qocJnRGkx_Rw3r_Cgi79ObNFGekrouIU-HJXGJ_DuFywId5Pusk_MOuAhN3KLo6QezstJmRcDoT_sXQb3_v7fxdMH5lndXbTi_3VNjvNKZ88IzlO0WPNOCVSGIC9owA9PstmaC0gHTGUflf_Oymv-C8hJVJqdhEwoytdjUFcuXN6IiC4N8_m9JGdC00aV3IEyZipDuTbzHMc09mHCMQKLpNdzZq1aTjmbW74APjDvFS3zONJEg7Cn4zXKynqf3WDwQXUQ-iDPXQrP_5rKPk6bv_YrV1aaaFeny38FJqUNaJNX_RR7MQdmbfWVyWJNxAsZ9qQ0paZCABvR_vZN5AYdMCEN37BIfnW-9pOuLPq87VkIQt3sbuS0ZLpfL4KMpAS4dcp39IykW5LNYXZ57HaYeYLrV4yeLNtd0voB_gjJNIVB8H3tNmS0o1kzpwTZnIhjiNm4etAoORnT7N595lvA8Ua1N8brMzBZ4UnOm1d4XV8U-6eym9Uz9CmV4Fz5mH9A_xXVf0KjELoZV_muRKJBIV4l1L7jomdigE5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇷
یاسر آسانی پس از پایان بازی امشب، پیراهن خود را به نوجوان استقلالی اهدا کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104499" target="_blank">📅 21:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104498">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC1A0Y2F0pfj6k0a3yESuiUpf73VxKktIa5UdFKzKbVLcXh-XJWlUZ9jMZKmo91-2r2dQqeiGhPSY5sZuEr0xSb0y8MbfXtsz3PPd9y-rjcelXxVnOmuG4CBF0xIdWV2vCdyWYCF7keNtrPQb5K4R21kQDmgNZKJA04c2tsoT4EZILge6OFFtzUguXdxeoR3EHwkQrJvvyiAfw9dCaU3y7Q2Iui0OE5qahwl-sFcBwMx5GAQ8jyWeaqvYJbP5RHT-SZwl3Fx-CioxQua_QbbkrwfaL0QB9e6YzTPYuQcz0mQrlnlSPP2bRp9P3ux9NfB0TXVsySZbALtrYVTet4GNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🇮🇷
هفته‌سوم لیگ‌برتر فوتبال ایران؛ سومین برد سهراب و تیمش با چاشنی سومین کلین‌شیت؛ ده دقیقه توفانی برای شکست طلایی‌پوشان کافی بود؛ محرم بازهم در یک بازی بزرگ شکست خورد!
🇮🇷
سپاهان
😏
-
😀
استقلال
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104498" target="_blank">📅 21:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104497">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prQAIMpqzyXq8HsfG6DynXSicCKWpJdZgTajknci41kOtWq43y4NjjDkkbnTlqCrJP9Tu8oFYbF3jQ5deL1t5dNbfSUMZ3YrpEkuLYf7eQVW-P1APrkT9_VU7lsD5ls9S60sRk_V0iibuB0O5-uQ3py_LI9g4t9U_ZT41JB3bNZtVW9KrvUhhBurwLBYq4glM5H4oQP3FGQC7dTDaoH-8vf9KcBnA0eGjcE59G1mqHhF81jXn4SbbVzarml_W7LymLN9QlDpmLb7EpTLZ-GMtCxzNT9Ojxj4sbzbvMnilhXw9A2iQGdj1Ew-pLBirIwFvLiT4zquEnv65khlkUyfcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🇮🇷
هفته‌سوم لیگ‌برتر فوتبال ایران؛ سومین برد سهراب و تیمش با چاشنی سومین کلین‌شیت؛ ده دقیقه توفانی برای شکست طلایی‌پوشان کافی بود؛ محرم بازهم در یک بازی بزرگ شکست خورد!
🇮🇷
سپاهان
😏
-
😀
استقلال
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104497" target="_blank">📅 21:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104496">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vwl9CfOPg7rbLx15gvHDUulMWPQ9MyO0qz3cj_7Gl14ut8BMWHI2iB_8Gd-hb9GfetPW7WS_dtOqzVuejbXcLv4faZZw52e9IhoCWtWhglERjLuQBUKlH0cZjbZGYRuqRF4g4nE6gkvbjrNOURprtFkO76LfkynNmtjX5_tthWo16ofAlTTshWbcJpKqL-19zSCB-fx5CeSZ1gOqVZ1mOhtDBwn8HcbLyY5Y1nct9GoB-JWVIcOOXNRtCgxGL829aDqErRW05ir-g-QRei8jIJzD011bEMYcBgjggwud_QLTrguf4QhDqUOfY7xIvWxzBBQqrviixuCjSm51iHNz-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🇮🇷
هفته‌سوم لیگ‌برتر فوتبال ایران؛ سومین برد سهراب و تیمش با چاشنی سومین کلین‌شیت؛ ده دقیقه توفانی برای شکست طلایی‌پوشان کافی بود؛ محرم بازهم در یک بازی بزرگ شکست خورد!
🇮🇷
سپاهان
😏
-
😀
استقلال
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104496" target="_blank">📅 21:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104495">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRadiS-mVWHIHHFC8_s1EFIe3XoTjggXj6FicG_BRoQ_tDxwq-oYoVwtmqTF2jgvZPql46VQrjiu2eGAPOdZmocKviEJPDVr9uNiQq6srA9IEsBN6vtWM3uBtRIWHz5F3SlSl0ZP8h35edqoTO4T6h2O4OSk77HxAbQhtusI1yTTFJvK5ODLW_Y1P5yKb3S0p0KdNlPmJn1kjRzqetBAoKvEvsOs_FqSkSU3Z8_oRDBPh87iGh9-qKrJyq4n6AE8-achkR7lqNV3ncTw4Fb1rRTmgTiM2TzjMnWNn79EYWoirz-oiRFDdH6_eWV7FF-2RXsyRp7w_E5s12f0ZpOzpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب پاری‌سن‌ژرمن مقابل رن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104495" target="_blank">📅 21:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104494">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaSYGi8bIOTEvsTGo0ef3mfqeg3708zXSUPPopNQNI3cyhOrWWbnuTKpLsz_T7VPtltEawf-NvCECMgGkqcsKRob5aa6mOSn3gad-lmUCusuK4vxqzLBNNKu2xMFVvxBApmXPNWaOsK7q7n2LmcD2Y4pP1nEF5U-p3nRrYZ5FC6vzEvbPmpbtt6OWFBTgovsjI6xvHhq8_OzOBQHo4oIqSFei7VLtKYVcHM3ZgFJ5-aVOIjA6w7MJDnRWFSwPooajsg7-2Tr_N_hBwPo_4uJdQOqpcC6almE-_RQj1r9QDgY3BMDfjNIcQJMcnU4oJ-ajwtlXcENYdGmU13a8Agi6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تا ۲۰۰ میلیون وام بگیر فوری!
🔥
‼️
با اسنپ‌پی می‌تونی بدون نیاز به ضامن و فقط با یه برگ چک صیادی تا ۲۰۰ میلیون تومن وام بگیری و تو اقساط بلند مدت تا ۲۴ ماه پرداخت کنی
😎
تا ۶ شهریور ۲۰٪ هم تخفیف اشتراک داری
🤩
پس همین حالا از لینک زیر وامت رو بگیر:
👇🏻
https://l.snpy.ir/zj65d
https://l.snpy.ir/zj65d
https://l.snpy.ir/zj65d</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104494" target="_blank">📅 21:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104493">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbRrNK6LqPSIYVvlaPJO5cLgEJ6oqZlAz9p0dFoTipLEh2dNlO8rnRaMu8-BJvF-uqMoAwx49M0tlOPybs4iXOUbdRDo8LGxJkrloW15VIdA95Drr9hs8otFeY7bgpb8GMqAJJ_ZMU1K_AfwGITS0VyKMYY3rgWQF8tMDEMApHnDjC1-wcQzASQOPSfFb934IFMLaUFNMJkS-Y1xe97iqodcNFIoPtHL3d4DNchM3xqDzys9Npr-Jq-52hwNI6JWaid1UnwEJGKtB39F_ZxqhYQJu5jf2LoJRo1NqxxcSQAa114TAXxbEdKA_h1jHyis76adXax_LWAV2jG3TLpEvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گسترش فرصت‌های سرمایه‌گذاری در وال‌گلد؛ نقره به میدان آمد!
💎
تنوع، کلید موفقیت در بازارهای مالی است. پلتفرم «وال‌گلد» در گام جدید خود این امکان را فراهم کرده است تا کاربران بتوانند در کنار طلا، روی «نقره» هم سرمایه‌گذاری کنند.
🔸
روند یک سال اخیر نشان می‌دهد نقره بازدهی‌های چشمگیری در بازار سرمایه داشته است.
🔸
با این امکان جدید، سرمایه‌گذاران می‌توانند با ترکیب طلا و نقره، یک سبد مطمئن‌تر، کلاسیک و پربازده بسازند.
ورود به بازار جذاب نقره
ورود به بازار جذاب نقره</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/104493" target="_blank">📅 21:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104492">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/905068b238.mp4?token=rUIWU2Nax_rQa5kRs6hKIo3zS6zpwg5OsAMo1IwtiTfn-7LDwKYuHBhsUlcNQfokrbKnnVafQbB2HV-r4O-i0PmIDGY1sBzxLHzpIcxsaPjcvbbZDmud4h3x_E4T4lf98QD7eK4ZUTaHXZqLvJETYvrs4AlxX-nCAv1A_7iWVMy92GWsmhf5xZOBwY9UWUUWEdM8ghDV1EwZ_MtQoamOWjUedS-kvZ2xeKzveNyzVNqU6n4VMK275b3pBF8TXxIxgH7sIF-Hkt-1h_pw3hXtvVd294goVwYT1clNA6DLla9SA1cZeqgLbBIqvzC0-F1XGMTHyhYRTHbCJGo4rkILtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/905068b238.mp4?token=rUIWU2Nax_rQa5kRs6hKIo3zS6zpwg5OsAMo1IwtiTfn-7LDwKYuHBhsUlcNQfokrbKnnVafQbB2HV-r4O-i0PmIDGY1sBzxLHzpIcxsaPjcvbbZDmud4h3x_E4T4lf98QD7eK4ZUTaHXZqLvJETYvrs4AlxX-nCAv1A_7iWVMy92GWsmhf5xZOBwY9UWUUWEdM8ghDV1EwZ_MtQoamOWjUedS-kvZ2xeKzveNyzVNqU6n4VMK275b3pBF8TXxIxgH7sIF-Hkt-1h_pw3hXtvVd294goVwYT1clNA6DLla9SA1cZeqgLbBIqvzC0-F1XGMTHyhYRTHbCJGo4rkILtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
وزیر نیرو: این هفته خاموشی‌ها تمام می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104492" target="_blank">📅 21:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104491">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
خولیان آلوارز بعد سوت پایان بازی در میان فحاشی و سوت‌های اعتراضی با سرعت راهی رختکن شد و در کنار سایر بازیکنان اتلتیکو باقی نموند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104491" target="_blank">📅 21:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104490">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c64a302233.mp4?token=O5QscGpxU6SMW6KLQOkoBC8E6eJs42qa0mM9CqhjvJQRmhtQ3PE4H06ppCIYhAETpg1kvzAqgniyxxWOlalG0GUffyNpl_1rXgOf7KX7QhtO1uDzXXoLIm57DITasZWafM7W8wPuMYwvau5p0OxHV0CZLv8iojOrKtwiQRlrdqg63l08bjymmq_bdh6SZb6j1ruXUoWUVAMUuxfp25mGR33rUw-_awBbIAvmSSbqYvChC_ZhEyGqKkqK-ZP1JAjkq9FUZFVNCw1eDEUFPlU3yMEbYqljGG9jUbWGwJ-R4Ed890hLa1wVXXMwLlCbO21tRQbwUiSW4chFOObt3pJF-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c64a302233.mp4?token=O5QscGpxU6SMW6KLQOkoBC8E6eJs42qa0mM9CqhjvJQRmhtQ3PE4H06ppCIYhAETpg1kvzAqgniyxxWOlalG0GUffyNpl_1rXgOf7KX7QhtO1uDzXXoLIm57DITasZWafM7W8wPuMYwvau5p0OxHV0CZLv8iojOrKtwiQRlrdqg63l08bjymmq_bdh6SZb6j1ruXUoWUVAMUuxfp25mGR33rUw-_awBbIAvmSSbqYvChC_ZhEyGqKkqK-ZP1JAjkq9FUZFVNCw1eDEUFPlU3yMEbYqljGG9jUbWGwJ-R4Ed890hLa1wVXXMwLlCbO21tRQbwUiSW4chFOObt3pJF-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇹🇷
دبل محمد صلاح در بازی امروز ترابوزان‌اسپور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104490" target="_blank">📅 20:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104489">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c757fb622.mp4?token=b1Wyu3DneBvr_6KjvuFMbUh_KZ6t6hLbpBrZgaLAKoSztRirLnP31-KcEmtghZftEuaf2Sv1KE3TcwPH-a-WHMrNc3v8fej7zDkR6o7cftWKZaKuN8qGHfijey4n0JSGF6BW110MCe4bXGQrHpBdpYvYzx_sQN-uRehr-WV_b2F3OFnA1eu_2kI-E-8c1Uo93q8bFOwo-oLRtWM6H4nqpKLtYe_MEwe91lEyXHojynWXTE0GOaIGE0WJAvkYqLs_nc6hx0-ZmoHNxQ0yb0pToeLwkjH0YZcVjMoBRk686erjMqt62p1MqstIs-HRhRt3qMdtEwKjm4cZXErBgeoA6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c757fb622.mp4?token=b1Wyu3DneBvr_6KjvuFMbUh_KZ6t6hLbpBrZgaLAKoSztRirLnP31-KcEmtghZftEuaf2Sv1KE3TcwPH-a-WHMrNc3v8fej7zDkR6o7cftWKZaKuN8qGHfijey4n0JSGF6BW110MCe4bXGQrHpBdpYvYzx_sQN-uRehr-WV_b2F3OFnA1eu_2kI-E-8c1Uo93q8bFOwo-oLRtWM6H4nqpKLtYe_MEwe91lEyXHojynWXTE0GOaIGE0WJAvkYqLs_nc6hx0-ZmoHNxQ0yb0pToeLwkjH0YZcVjMoBRk686erjMqt62p1MqstIs-HRhRt3qMdtEwKjm4cZXErBgeoA6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
اقدام عجیب آلوارز پس از پایان بازی اتلتیکومادرید در میان فحاشی طرفداران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104489" target="_blank">📅 20:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104488">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L384RgrZL634_vM-DR06smm8NCmUi41ibfDTeKkrXuNHQap42h4P8e4OgHyupFlnGOwCnvbQA8HMVKwmdUhJVmaIPWWO6w00l4ejL-6c71SaCAA75BSphh_iAZkbGPOE0NfJ7VdcKj5P6-QXSwxc9854rioMvUROQEBLHY3qABErNOGM6ozjAaLpd_etioBSCnDbZ19fpJXEPWrl7G-yOz6f7Nt3MmM4M98Iqxtyk_9ks928jJBMawjFkQH07EGTu2tKu65nO0vJUoyctBQxtMLm35siyS-MkTL7YdRN2B9wrvvXgS2y8GbYoHi47pXb_xGXct7sJ8w5bWpe2xGG-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
جو وحشتناک متروپولیتانو علیه الوارز هنگام ورودش به زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/104488" target="_blank">📅 20:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104487">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9059eaf0a0.mp4?token=ENIq7-_QmF_a7NuYdW3LVfxhMKc0AyYSXcMX6x8sWpd-bG79Ej_2AoRXF6JANd9Sr4-SSUyk0i-cBpjvK7txFoMiGJyh8q-LWu9QRBibCZYzlWtzFKC7r8ziOdgXF457OYaRBDYPzQr34ITGpXB5y9Ee0ywGkkHLVoXCyQW5Boltb2GLA08SAS3BlUFcJmxnDr3-T3ejCuPg1iIOifa4ts6qXJ0-lWqd0IiPqtmun0CZ2AoJKba2NcEqoIflFwo9ctvERjyjkBawBXxO8aG3T1Svti93q5QLgoAbNLt0oSbHg1M6qk3IvKmJ7c_c-f1pNKqjedI5AlQhDDAexzkekg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9059eaf0a0.mp4?token=ENIq7-_QmF_a7NuYdW3LVfxhMKc0AyYSXcMX6x8sWpd-bG79Ej_2AoRXF6JANd9Sr4-SSUyk0i-cBpjvK7txFoMiGJyh8q-LWu9QRBibCZYzlWtzFKC7r8ziOdgXF457OYaRBDYPzQr34ITGpXB5y9Ee0ywGkkHLVoXCyQW5Boltb2GLA08SAS3BlUFcJmxnDr3-T3ejCuPg1iIOifa4ts6qXJ0-lWqd0IiPqtmun0CZ2AoJKba2NcEqoIflFwo9ctvERjyjkBawBXxO8aG3T1Svti93q5QLgoAbNLt0oSbHg1M6qk3IvKmJ7c_c-f1pNKqjedI5AlQhDDAexzkekg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
استقلالی‌ها بعد از دریافت دوگل خطاب به حسین حسینی: سید دوست داریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104487" target="_blank">📅 20:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104486">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/660b601000.mp4?token=j9QGEwkLXWkeblTW3ujUhMnNwzL2_5sm-FYiPZ5_A0Ca7TISAe20a5B5CIfnHgjTx9LeI25mSfPm7ENuHf1o98_yIZ0VWADPLVRY8dIOHojYL4DIBjI6AmdGP5lkEE3nEFvPleyiXjE3NvdTAnvz5yImP-NDO__RsIb0uhSLmgG-v1HcwYMKItaE45hvcvXmSwAuTrJ5YqVqksCw8uNumKIXdoJwrDPCp7Le_EFQBbO9J4iDdC4FWakxWPqM64chirwXuNMQXy6kwiKt1b4DAgiFdR0GK0_w62NN7VahRtIEpyFL-ix99rllKu305Jm8AIA3cKpZ3GknosaoQU0j4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/660b601000.mp4?token=j9QGEwkLXWkeblTW3ujUhMnNwzL2_5sm-FYiPZ5_A0Ca7TISAe20a5B5CIfnHgjTx9LeI25mSfPm7ENuHf1o98_yIZ0VWADPLVRY8dIOHojYL4DIBjI6AmdGP5lkEE3nEFvPleyiXjE3NvdTAnvz5yImP-NDO__RsIb0uhSLmgG-v1HcwYMKItaE45hvcvXmSwAuTrJ5YqVqksCw8uNumKIXdoJwrDPCp7Le_EFQBbO9J4iDdC4FWakxWPqM64chirwXuNMQXy6kwiKt1b4DAgiFdR0GK0_w62NN7VahRtIEpyFL-ix99rllKu305Jm8AIA3cKpZ3GknosaoQU0j4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
سوپرسیو فوق‌العاده محمد خلیفه در بازی آلومینیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104486" target="_blank">📅 20:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104485">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbd110fb25.mp4?token=Oz754A0Ayg7fX_bAyxBSdew8C9QoyAgwsXP-8BX0wM_HVEGWVR6idtbg34G1zqzPYj_nA2xnUKlXstNsRWMiTXEVdHrV30QqBpNGdUCzHdZo1J1YoIfIloJ67Nenay4m2kV_hizGCAgZYC9GHzmPucJHNa_ZYr3XfPGkuRmTDPZZ4i3TGtXGxoQwIEtAWT3l0zi8eZzj1oAWOYoE9js7FiSOF-K0kokh9h_kNyJLpG1O09JzQsD1TV98GaFuG2R4a5uZ_bhlt_I3L0D7OULnKN94Kv27Osgs4u7BiYDSW-nobnw_BEhmeCeEYEtBG6u8ziVpNUs6-GFYGBEIWrx-Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbd110fb25.mp4?token=Oz754A0Ayg7fX_bAyxBSdew8C9QoyAgwsXP-8BX0wM_HVEGWVR6idtbg34G1zqzPYj_nA2xnUKlXstNsRWMiTXEVdHrV30QqBpNGdUCzHdZo1J1YoIfIloJ67Nenay4m2kV_hizGCAgZYC9GHzmPucJHNa_ZYr3XfPGkuRmTDPZZ4i3TGtXGxoQwIEtAWT3l0zi8eZzj1oAWOYoE9js7FiSOF-K0kokh9h_kNyJLpG1O09JzQsD1TV98GaFuG2R4a5uZ_bhlt_I3L0D7OULnKN94Kv27Osgs4u7BiYDSW-nobnw_BEhmeCeEYEtBG6u8ziVpNUs6-GFYGBEIWrx-Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🔵
شعار استقلالی‌ها: "جدول رو خوب نگاه کنید، قهرمان رو اعلام کنید"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/104485" target="_blank">📅 20:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104484">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/176f995cf4.mp4?token=Qs_KMY2EcF6DYVjhgceIuXWORJ1nvB0g0aRNCOuEP5MnIVTRiijJWVKmiiV_UyK4Dc_f3aRapi6MhJpYX2GYZ-ExLhIL63-9jeK9-XDQAbZSW-5kQjOIuejfxovLUGKWx4sqwFlswEnp_vApUPsqs4rPaZ66SigRs8_qkU_erIGgVg_Pw2HJmbZl_iIZQWg8IiH8H3gchunga7omXkJUL6VdmBWUf73jRwzfKnz4uq-WIshwEIu86NGHLOt59xHcBArFiK_j_UMIeXug3AbjgtQxadQbCtu5MKsL97f0U_Ad2kp8aKOMa5jtaUwNm86p_aHYkgPdb1ohlVRfS-MnVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/176f995cf4.mp4?token=Qs_KMY2EcF6DYVjhgceIuXWORJ1nvB0g0aRNCOuEP5MnIVTRiijJWVKmiiV_UyK4Dc_f3aRapi6MhJpYX2GYZ-ExLhIL63-9jeK9-XDQAbZSW-5kQjOIuejfxovLUGKWx4sqwFlswEnp_vApUPsqs4rPaZ66SigRs8_qkU_erIGgVg_Pw2HJmbZl_iIZQWg8IiH8H3gchunga7omXkJUL6VdmBWUf73jRwzfKnz4uq-WIshwEIu86NGHLOt59xHcBArFiK_j_UMIeXug3AbjgtQxadQbCtu5MKsL97f0U_Ad2kp8aKOMa5jtaUwNm86p_aHYkgPdb1ohlVRfS-MnVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
درخواست هواداران استقلال در شهرقدس
💙
جام بدید، قهرمان؛ قهرمانی حق ماست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/104484" target="_blank">📅 20:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104483">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78becda813.mp4?token=R3AQ_6YEOKeLq7yNoFO7qdNPmByxNyBRL8fvWMiHIXg6JBtG8FsukxU23R2AXGG1JEXPgRd4EUEImhyHr0KXlUJlqPb47vaUO3J3xqk3Ku3z-_5CEsDsw6Q1ic45l50_aAsDu8GMAichn2LQzNZlQAgJT_oMHBcM4NqYxQWt5Gmyc-Jaw85rG-Uc6VXYkEs9Cv5Cy6cBc9EODA5-vJrFN-YnVH1q23JAjCb5texSWR7vYkZNLD0FZM4R4uU_kCUD_4hWlzcQdWqxPFMGl9y_9NliL4pnaoe0h5QrOM6TBm0o1zmJdgP05l4tQBNId0dFugZLSZ_bAto8H4bcipZi0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78becda813.mp4?token=R3AQ_6YEOKeLq7yNoFO7qdNPmByxNyBRL8fvWMiHIXg6JBtG8FsukxU23R2AXGG1JEXPgRd4EUEImhyHr0KXlUJlqPb47vaUO3J3xqk3Ku3z-_5CEsDsw6Q1ic45l50_aAsDu8GMAichn2LQzNZlQAgJT_oMHBcM4NqYxQWt5Gmyc-Jaw85rG-Uc6VXYkEs9Cv5Cy6cBc9EODA5-vJrFN-YnVH1q23JAjCb5texSWR7vYkZNLD0FZM4R4uU_kCUD_4hWlzcQdWqxPFMGl9y_9NliL4pnaoe0h5QrOM6TBm0o1zmJdgP05l4tQBNId0dFugZLSZ_bAto8H4bcipZi0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
جو وحشتناک متروپولیتانو علیه الوارز هنگام ورودش به زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104483" target="_blank">📅 20:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104482">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEzCStUTiTCZaYc1qFgvgT-zhrKshrWTjF0UzI4L1Pi94Q63rO0gYCkwArxoJjTtHeBHqYOo078gsEZhPyc4ZqryLnFA-NWCb-AFLD4ooCWRYh7kWxZDV5PwFMAEhAQySiN_uqGn2vMOV8mWiL4ONR62BZrJILSrh_JrPod-_FfFP7o63GW2juwyDjM4HMiU8HzwMSeJyfHPWxfkeAYXmy6abIaQhSiFiQn1dnbvhmgauupHt1hdY10cHj1kbbVbzpdfYGJf-N7r-CYnYut_lWEUiYJTSeJAdG_zLoZ7uwhXOCLdRF4u1dbMi8ZEYF1O_xjr7qOpQnHvKDQgj3duTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
هواداران اتلتیکو فریاد می‌زدند: به او بگویید برود، برای همیشه برود،
کسخار
بارسا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104482" target="_blank">📅 20:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104481">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d7870a8f.mp4?token=AiCcYRgE477zmetdvtBHI4RTMRbZIJBF7Vsdf097q9Oe_z3oT_dtjvz66IyYutJCPdmr_lO90MnuA8zvtbbZcwQk4hbVYesomHQv8o3b7iOYVrIHN-JOWpJQPJAPguzce0rWusyjcz8_ZEofU5IEWae5FgeumXdefnwcdiypU9sBigvBQ_eyELNJps9bPjWVqGbtuWCrRk7gD9UK3nZzzTWFyLVnl5o0yeCj8i2OliLK2svh2bD7O7JEs3sjtngLMFopIZVyiQR3Sl9iLVhJlWing_34gHKwyPfZi9tGqphX7ISXRPFIt1L8C-JLrHnkUKy-JNkySTdtgIfWUmGHUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d7870a8f.mp4?token=AiCcYRgE477zmetdvtBHI4RTMRbZIJBF7Vsdf097q9Oe_z3oT_dtjvz66IyYutJCPdmr_lO90MnuA8zvtbbZcwQk4hbVYesomHQv8o3b7iOYVrIHN-JOWpJQPJAPguzce0rWusyjcz8_ZEofU5IEWae5FgeumXdefnwcdiypU9sBigvBQ_eyELNJps9bPjWVqGbtuWCrRk7gD9UK3nZzzTWFyLVnl5o0yeCj8i2OliLK2svh2bD7O7JEs3sjtngLMFopIZVyiQR3Sl9iLVhJlWing_34gHKwyPfZi9tGqphX7ISXRPFIt1L8C-JLrHnkUKy-JNkySTdtgIfWUmGHUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇹🇷
گلزنی محمدصلاح در بازی ترابوزان‌اسپور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/104481" target="_blank">📅 20:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104480">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a48f53f5c.mp4?token=mcBKEyI_IcOqTCKLDrTDEClErIYxy8yRHYLDzoZ4iFMgyCc9PeXd8UnN3nmu-hasLfxnSCFusMdTLfJ8GsTfAvQnZxnOB_WwfgENoULKXiYpH1ofAkQoVruRrM_ehnbKmpxQBGW4rYF9nw7tt-hytlxtEObDuSFJ_LPM13kuh6Y0321_-G5vvzYoRA13pYes__mwlhNqFFIBLb-rsBRAsXDcnEsAdalp90pQ42_P5Zwje7dO8Bs91hCvqvHEyhWs4P9yIvyxriH7l0ENmoZeqUBgDrfMcI6mwJS_D_fZ_lEqZ-58W-32NPTWaCOYOLlIo3rm378egQnPBKHgbqsqfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a48f53f5c.mp4?token=mcBKEyI_IcOqTCKLDrTDEClErIYxy8yRHYLDzoZ4iFMgyCc9PeXd8UnN3nmu-hasLfxnSCFusMdTLfJ8GsTfAvQnZxnOB_WwfgENoULKXiYpH1ofAkQoVruRrM_ehnbKmpxQBGW4rYF9nw7tt-hytlxtEObDuSFJ_LPM13kuh6Y0321_-G5vvzYoRA13pYes__mwlhNqFFIBLb-rsBRAsXDcnEsAdalp90pQ42_P5Zwje7dO8Bs91hCvqvHEyhWs4P9yIvyxriH7l0ENmoZeqUBgDrfMcI6mwJS_D_fZ_lEqZ-58W-32NPTWaCOYOLlIo3rm378egQnPBKHgbqsqfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
سوپرسیو فوق‌العاده محمد خلیفه در بازی آلومینیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104480" target="_blank">📅 20:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104479">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J8Hjt3nMsL7p8_ORyvSiHozxc3gH7iLyEC4wRNNgfcmSK9yKkRXe7trfLitc_0aG8yUHrJn70x_pE9sC5kme3XX5geyDtU1QSbcQt2Ht4zSzhbOP-DL9IIuxJ8dWWHe2PuG8Z59_un88-g6qV19g2V4BbCklehiMgkl4NsnR4ZjxM5boaWQygW9diFL83GYiFhfoRuIR7VHNLzH9p3h5FI1uoRI5Bzb8ebIoI3vEGBESjNFATn1jVm84ljtJ0_5SBxVGbVS6zDoXqIxal_Qde5_Q9He_ANEvoyPi59SvZNldreRkWXxaAWJhidCskHCVhFmpFYrCHGtDH6tVz_IY9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
هواداران اتلتیکو فریاد می‌زدند: به او بگویید برود، برای همیشه برود،
کسخار
بارسا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/104479" target="_blank">📅 19:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104478">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QksP_xDf7vGPN4k1HVrZY69G9bqUshDZty6UmsVjSoDGVdZQzosRIztnm1gR8dKSOpnPP6M9Gy9Rm-F_jxhAp2FzfKH6zb5ukgfe7rA6tbPryqk4HKAxTtvWs2zV8s06orQOeW-43kvbYBL-opCMMUXdAo8PHQjZq2CMqsElKNvOodI63ZBI7IK_Y25_dUhIE558Jk6r7ARV_1ZPVfQtZGGo_Nh9hyVgrHiMi9WXzUpesahZ5MfFZcC8nCBjkS-LskGjtt_SeSaRkM6lb8MNKGxti_hNtwgGVWYhyeWVJ-gm_3ryE8uOG6qorc4Gjektfy4QFdA5iWuCah_HksS-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
گل دوم استقلال به سپاهان توسط قلی زاده(10)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104478" target="_blank">📅 19:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104477">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb3d0d855.mp4?token=jeyax6f_k6XrygaGWNh6RgKSUG-xGZzSgZiaZ_lo37fTkN3Oy-H1EtuVolzL0P_h9w2zcYAvAwj-7VNfy9oUJrTYRLtY17cgD9SCsqTsP0_30k9hq5vMS4D9DJCnpUymov6zRWVanP0rZ4BS0YeAxieb3YcyYORbK1wV3yZsCGac_nFx2QXN6z8dZZuVorSnm8DB2FSEUuFFCxFVzLfJHJw9ksJA9f-1R7jlxQ1CZ0QFud5cboGYmoXdWrf6KFiysWoAybfYwpxqEF6BO2_X8xVrr0kkn1oiztKAbkwbsi-26zktVCvyesDzrQ-o7pnrw6Keh_nWjQQ8Tewnw0er2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb3d0d855.mp4?token=jeyax6f_k6XrygaGWNh6RgKSUG-xGZzSgZiaZ_lo37fTkN3Oy-H1EtuVolzL0P_h9w2zcYAvAwj-7VNfy9oUJrTYRLtY17cgD9SCsqTsP0_30k9hq5vMS4D9DJCnpUymov6zRWVanP0rZ4BS0YeAxieb3YcyYORbK1wV3yZsCGac_nFx2QXN6z8dZZuVorSnm8DB2FSEUuFFCxFVzLfJHJw9ksJA9f-1R7jlxQ1CZ0QFud5cboGYmoXdWrf6KFiysWoAybfYwpxqEF6BO2_X8xVrr0kkn1oiztKAbkwbsi-26zktVCvyesDzrQ-o7pnrw6Keh_nWjQQ8Tewnw0er2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
گل دوم استقلال به سپاهان توسط قلی زاده(10)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104477" target="_blank">📅 19:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104476">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اسماعیل قلی‌زاده</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104476" target="_blank">📅 19:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104475">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">استقلال دومیووووو زدددد</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104475" target="_blank">📅 19:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104474">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گلگلگلگگلگل</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104474" target="_blank">📅 19:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104473">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f589e085ba.mp4?token=pln-Jh7fvP6dsyjD8NXWwIzNfgU62h2pg3MJvLayV7JUR7A2rVg8LnySzX70jebieawN29iSXsy1SrOoEgk3dD7PF1GMtvUZu-YxivU1LXYxLSP9PeZQjZdGU87ZNl94PKzM1v-2Qs6p1SiRXzXOOmw16QBMvJ8E5UnmeFrD3aMmtIzEvpvMKagE-Q7eeO3L1hk0FuFsk6Bn3lmLfr2n9F2hSdwhoOhJjfxoUMnWqdCbW5aKmQtYLUH0mWijyKBl2B4yO1XRFRHfuONaGBF70uv4f-DiK1l31X7Zhy77Uc0LBm3w8SdISIHOuChEIzXOH0poBEjfphucGEbemJzg7YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f589e085ba.mp4?token=pln-Jh7fvP6dsyjD8NXWwIzNfgU62h2pg3MJvLayV7JUR7A2rVg8LnySzX70jebieawN29iSXsy1SrOoEgk3dD7PF1GMtvUZu-YxivU1LXYxLSP9PeZQjZdGU87ZNl94PKzM1v-2Qs6p1SiRXzXOOmw16QBMvJ8E5UnmeFrD3aMmtIzEvpvMKagE-Q7eeO3L1hk0FuFsk6Bn3lmLfr2n9F2hSdwhoOhJjfxoUMnWqdCbW5aKmQtYLUH0mWijyKBl2B4yO1XRFRHfuONaGBF70uv4f-DiK1l31X7Zhy77Uc0LBm3w8SdISIHOuChEIzXOH0poBEjfphucGEbemJzg7YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
سوپررررر گل یاسر‌آسانی مقابل سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104473" target="_blank">📅 19:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104472">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یاسر آسانی</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104472" target="_blank">📅 19:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104471">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">استقلال زد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104471" target="_blank">📅 19:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104470">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلگلگلگگلگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104470" target="_blank">📅 19:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104469">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCXF-hFnvFQKveRODY2pKWTFlqDnWEPrKx-tOKKEjH65VxNmBDoqpQBsTlt-JAnEKlYP4w1lSvLhAX8AbP4TSY8Y2e4k96gb7sGxQ5Vt_4etbyi1GGN9G9YNhP0-gIoUUkSYkQVQ-zbS2xgc6J-yMNGR2qP2186SoOiid1v7lT-YxxGdOtNGUmIvTO4_JHo-peO0XwcLCtdSV_tMpLCNnrRTtSTaq1qvZy9NdzDCR3h-hN4i_g8MdjlR2ZGvbhoNqegGRi7snI51Rt--Kr0t4VPk8dklkEuJW1GKdf30__ktZKYcNuwLkL-jsc_VJCPC5Fj1Wjhz5635cBqSEGb0bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
هو شدن شدید آلوارز در بازی امشب اتلتیکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/104469" target="_blank">📅 19:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104468">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ae17874e.mp4?token=PxTF403O4LTWgzv0BvHCpG-NZQ7WG2zjM-ZY4h5Rf4wwlAgQAnu-nwcOtQjxucA8h1yZ0cM-jDsgfGm5jOcbWKtqv5W1tImYjdtRZetT4H9k6gmAOJSVA3JSKOcBMKMNGDo5DC69LidpZYkwRnJpfTfhzDvqTS9l4duTX6-_mzopLvrNWrKuQ8608t8lRFugSoQisTjgv6V2pHPyt5aM08ROj_rSxf-cvwMl9_5FRH6s4Bj_t1IfPSeLFgobvrXexjyLAxfK5biwvEzLQziivXYafiAyRRHXLoG8bMS5XXBqwoNjVKP0eDurPbM7W_6Ocwoi49-BIWJCy5XIfGOyQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ae17874e.mp4?token=PxTF403O4LTWgzv0BvHCpG-NZQ7WG2zjM-ZY4h5Rf4wwlAgQAnu-nwcOtQjxucA8h1yZ0cM-jDsgfGm5jOcbWKtqv5W1tImYjdtRZetT4H9k6gmAOJSVA3JSKOcBMKMNGDo5DC69LidpZYkwRnJpfTfhzDvqTS9l4duTX6-_mzopLvrNWrKuQ8608t8lRFugSoQisTjgv6V2pHPyt5aM08ROj_rSxf-cvwMl9_5FRH6s4Bj_t1IfPSeLFgobvrXexjyLAxfK5biwvEzLQziivXYafiAyRRHXLoG8bMS5XXBqwoNjVKP0eDurPbM7W_6Ocwoi49-BIWJCy5XIfGOyQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🇮🇷
شعار هواداران استقلال در ورزشگاه: سپاهان دوست داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/104468" target="_blank">📅 19:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104467">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
صحبت‌های هوادار استقلالی که برای تماشای بازی تیم محبوبش، خودش را از آلمان به ایران رسانده: ما مثل بعضی تیم‌ها کاپ پلاستیکی نگرفتیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/104467" target="_blank">📅 19:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104466">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/141a2ee698.mp4?token=hEuIgqs8o78mluXAj1kLN8A27n491g9bYTmAyFSIrrByDpQE10Bzc0MyJZihkqQB7eSuCGShGRXyNhEaUEBa_YPQdXP0tANpL6TQs9vk3vFc-woPDDwWXIhqrt9dctrML47BEWaKU27Q3O5ziUNfiiprCMi5zST9tV-EBx9FBh6Yp_g-1BihUuUPeONEIyFmv9A5EVg-MFIGWvTUxS_b5M9I36rxZgLEpNEF99BzFoSX8mLURqOc7GHEGu2P56tZ3TfSdIAnhGy5eQjvF85E_6J0DB1zrx7UrMbz7KXWD0RJVSeWF37HYvkgTMtM3up8irJgc2M3z8cVi-FuqOOKww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/141a2ee698.mp4?token=hEuIgqs8o78mluXAj1kLN8A27n491g9bYTmAyFSIrrByDpQE10Bzc0MyJZihkqQB7eSuCGShGRXyNhEaUEBa_YPQdXP0tANpL6TQs9vk3vFc-woPDDwWXIhqrt9dctrML47BEWaKU27Q3O5ziUNfiiprCMi5zST9tV-EBx9FBh6Yp_g-1BihUuUPeONEIyFmv9A5EVg-MFIGWvTUxS_b5M9I36rxZgLEpNEF99BzFoSX8mLURqOc7GHEGu2P56tZ3TfSdIAnhGy5eQjvF85E_6J0DB1zrx7UrMbz7KXWD0RJVSeWF37HYvkgTMtM3up8irJgc2M3z8cVi-FuqOOKww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول نیوکاسل به لیورپول توسط الانگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/104466" target="_blank">📅 19:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104465">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d702269fdb.mp4?token=pT91E6KNQA2NifnDpyS5uAZ495H0Mk5rgKTV9LVMULRNbsn-GnsRsK67n5qnKthVGHTzECL5mILTktscDo6Qs__2nRr6QvMDjbxM6JlDSGKJNSEzxThW-RuQI7EmT_ZuOyRqFs9cYPNDoNBMsN7u7lqclZzac60hERPpbehWGS_xKANKBtBnokmHknLzOUShdaCnBRTPj2Q8vw0QMxK0Xxz-rrEmjKGdS8kEsazQ7HETAjy8yIX1DnRscH50It4_Di_uFmll93FeVJ1y_LEDGBjy5EhilifYrQA6WVrMgIYqivCxvhHBmMvCVExcfFRoAcR-CMPiCpF94beqz_q63w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d702269fdb.mp4?token=pT91E6KNQA2NifnDpyS5uAZ495H0Mk5rgKTV9LVMULRNbsn-GnsRsK67n5qnKthVGHTzECL5mILTktscDo6Qs__2nRr6QvMDjbxM6JlDSGKJNSEzxThW-RuQI7EmT_ZuOyRqFs9cYPNDoNBMsN7u7lqclZzac60hERPpbehWGS_xKANKBtBnokmHknLzOUShdaCnBRTPj2Q8vw0QMxK0Xxz-rrEmjKGdS8kEsazQ7HETAjy8yIX1DnRscH50It4_Di_uFmll93FeVJ1y_LEDGBjy5EhilifYrQA6WVrMgIYqivCxvhHBmMvCVExcfFRoAcR-CMPiCpF94beqz_q63w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
هو شدن شدید آلوارز در بازی امشب اتلتیکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104465" target="_blank">📅 19:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104464">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nr0jgVVOmkUeeljHuiJN9fXUmNpxVuGYsBO9MvGV0E0zkTXalNgTDCEtVvoAcnj88VI3qJiisNOlqJfm_qT3I72vonja8eOkqg-zxDcIp9316payKGkz3PomTv9F96q1vq1qvAHd7LWC7moEL6AYjP69yzGOWHgWQPq9TckOc6Dp5u0mA3kh_EgvT1_IP0Tbxh4pi9NafbbVQMZUfUxf8pvFrdKKINaz3Y5jhc_LZ8gmDxkWwmmhddLRPqsMuxytO41gnIoRF33wIayVTAARGoHNEWZksn5o_n3w6sErGtmY8Jvvf3Mdk7Amh67hlyRC-GPpH6A0-mCDt3DdGv4Zgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
شماتیک ترکیب استقلال مقابل سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/104464" target="_blank">📅 18:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104463">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF2ORrMbu6AoLDu7xUCytupC8cTQeOQZ06ltDCSxz4CSaq-KI2cTPgcf8sro279VpchxxvN6kqwkyRlV6kUVxDaao7ZG6r_qdFjsoB3Z1cqCAORRE1-r2-nEQPxHhYcyLor9vltd469bEzsG6maWlksXA-8fU12w8b6gJMbhB79dAVnus5_ts3odb4r_a3Gli7HRtY7rXNISyzHatDhul7b_Ovfgd_b_26Nc6lfl4B5mgNqZ4SaNm4crK6_uYAASBUpfrniUrgklq82QWJn6E-7zU5SFfZtN5UOt1IJyschVO4x2UZyOET6F4HLsQDgwh2paglP_FQBSgM83DPytjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
ترکیییب استقلال مقابل سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/104463" target="_blank">📅 18:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104462">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUOCsuj35VIxdJn8xnqNFiB-AaNIeTu7Dvuk1oWuLlZS9cfHYjXU5bemJrvgfWh7fUBIXZNXfLQyqr968NnPC8Xje0Z7v986rb2SeNXZxuwBFlZJVOH9qKczE8oFmRd7iWVEWK1b5ooaN6uab_n_oK4BTF_XylWXPxdAYzsNIhrCPeh4CRsRoPXZbXTk73Q6IvGDkQt2DzYv5-A6tnW45ruECD5Lxus9otpcpxhxCw1cxyb8_Q6y6lm3oAHV9y2YthcLwKV2Dg2MohX8g_GxxZ6g692JSlcsd5WZxF1dz2lDgZaHvSDsjdslV3h2w8ONttpiaiXyYQT7bD_yd-gwcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
ترکیییب استقلال مقابل سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/104462" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104461">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDWpvNglNQvncdL6RBu71hblFSC03e72yQq-yvN5_acVWimhDH6Ru8vZjWgiH0HsegyA5MkMKn-1DvccnTLs3fCCtQFfhnJwIE1fkrKo7BbGf20HcgvHNgQzmTMBDAHGluJhiJMtN9v_Br75qwMMyIsLgrk4XuwURzrJxHoTSCKjC27W7CxUE05k1dLiW433zIB70p35kcIt-CQ1DJPzLdVnOwQb2HBR7DM0HQpbq7EWPOsz6q4qEWtCTTe54s2LEP2L4nAYv1r5k3r9Vr8VZP-2054prYyxF9hH2zi6kueN-PHmxUkiHdCwRXqYNsaVs_VXk5OMkC_b15CbSbZWnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لیگ برتر انگلیس| مدافعان کار را برای مارسکا درآوردند؛ کامبک منچسترسیتی برای گرفتن ٣ امتیاز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی دو - بورنموث یک
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/104461" target="_blank">📅 18:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104460">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dba451e740.mp4?token=Kdtw2YoB67WYNC3DjgmHaQMNXwpe8WPn44Oi6vgRo1h4cjn-m9fiwzUVS_twQ8tLb6oEycjty7l4Sh7pEw0NKSkxYc96jsqHOoQEmtORkL7du1s4_cakYRkM53llH7IDyxusquRvHWuX2v89HQf6RXKQr5OLO2z6yzltDUMDvxIWryaVb8rF-BsYegdO8coTdxMhWnkmht68vwMP6Cp1xioNAMvYgDZv0wN2yTLCOYN5Qe9LQZYcIWta7gM45rsfSYrI_5WQcvyoBWST3STPPLqVJMXHdvdu2EtINZienlR7fPb8np5ctjxBXT9gyXax-ipA4Llq06i7fpe4bsmzIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dba451e740.mp4?token=Kdtw2YoB67WYNC3DjgmHaQMNXwpe8WPn44Oi6vgRo1h4cjn-m9fiwzUVS_twQ8tLb6oEycjty7l4Sh7pEw0NKSkxYc96jsqHOoQEmtORkL7du1s4_cakYRkM53llH7IDyxusquRvHWuX2v89HQf6RXKQr5OLO2z6yzltDUMDvxIWryaVb8rF-BsYegdO8coTdxMhWnkmht68vwMP6Cp1xioNAMvYgDZv0wN2yTLCOYN5Qe9LQZYcIWta7gM45rsfSYrI_5WQcvyoBWST3STPPLqVJMXHdvdu2EtINZienlR7fPb8np5ctjxBXT9gyXax-ipA4Llq06i7fpe4bsmzIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💙
هوادار استقلال از تصمیم بختیاری‌زاده حمایت کرد
🔵
هوادار استقلال تصمیم سهراب بختیاری‌زاده برای کنار گذاشتن علیرضا کوشکی به‌دلیل مسائل انضباطی را تحسین کرد و آن را نشانه اقتدار سرمربی در مدیریت رختکن دانست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/104460" target="_blank">📅 18:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104459">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join
Join Join Join</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/104459" target="_blank">📅 18:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104458">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐇𝐚𝐉 | 𝐅𝐢𝐱𝐞𝐝</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1QnVATW19crtdafnArQlqZP7_KzWwvDd9QEQJ_E5Wfg8YmrOv50WoOaibp0EXjK-wE_u__KzCyVMWWbK2vtY3mzg7RtSsvvV14KHLyUCzHQF2zWRfHMjnK85DuX0bk6Irv0TgrLZzkszZDrJ-H85ROVh_iuXw8YmYyeDCJRLLb6_CuqXM6lEfXQZmOOHqyv8po4N14LU6EMYUwZQxKNhE5IthgwsJGpwFFrzxfzhFsZ37czoY1ZI2qxyQW_Oe3gkd7IYVTiz4ALZN3RegZlXzap7LSU_1GpUNhwP4NJ_laFm5ANmBN9gCPHIr0mqY6G6w35DkUylhSQZ7K-I1ixSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@HaJFixed</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/104458" target="_blank">📅 18:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104456">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nUPdIFe_qVaW7Ketds_P0e__Zz8v3wnvVYCtLni_5YgOVtkWj8Eh0fzmXuoLyFsmDVLfACoHmJCSoBHYa1ZJ9kbS4WWrXpycdgXYF31fk12mRHphjQhJghyj6L6L2fgH6DWybbev2F5dFyp_3ark4rvsEjZ6i1G1E91cXFdRJmVvLxnQJ7n7VlsrzPOm7pr518zHHlYjIJF_imFn1lIyJix5_ElzVvR-WJkpx2QW9dHaI6yh1cC_B05BjBvpQ5HeaBtEuMdIHJrwzcap4ZBfndEsMsSsgekwyOkvXXp5Jp7kaOrAtHSqPRUQNXYXxMQaUBeHr-0jK_5jO58ssmhyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhN7pSbWQj7G4WavL0ZDKORyPMfqDVUeO7kgoLvGu0xJ8xZUbFt3aDPwFbKod9zImKtXgGeb7q2NPlVhP5p0S-p6NRAaFevRGyhuatSx-yht6W4oT7tVv3tT_XLsGUTgWZrATJOru8eD6Rezyzf-_cRfnZx_mchhbniQQhB8ClxuOe4qA0mnBQ0CcII8sLXG7AqD4TZD2gzo01mSOR5S2F0i0ekxU5uCn-kzWU-07z7Y7fo6BqhGu2--Nu99TOcvnNqfH_SuLTtrAbRYeVJLas5bMS47MSDL4_HYCOSKYmPfKwfcmHxxJQtzFQ6OuR_fO9EOdE-8QIU_KwO0no_1iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
⚽️
ترکیب تیم‌های نیوکاسل و لیورپول
⚽️
لیگ جزیره/ ساعت ۱۹:۰۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/104456" target="_blank">📅 18:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104455">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇮🇷
هوادار استقلال در واکنش به برگزاری داربی در اصفهان: امیدوارم آزادی آماده شود تا باخت و گریه پرسپولیسی‌ها را در تهران ببینیم/ ان‌شاءالله سال بعد می‌گوییم سه افتخار در آسیا حسرت پرسپولیسی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/104455" target="_blank">📅 18:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104454">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca7ecc06eb.mp4?token=oAySrLg2qqjs9IYMM6Lov0MYGfPLrxVxQTirmcC4QiODkxu16fPCrbuc9C2MR0YorXOgnzCYSiZezJp72rGgzQqV4zQsjskLhd0xZtx5_wWU3C01fPYlJBjGBfheJHvxcAdAH3Dj_kwBhgab1EMIImjvZyOPn4P49iIiJ1xDK8924YKmJk2cxTiETxRbvUVhbRWyQrxeChTkNMtPsb6N2TpuiCBXngPkqbjSFBd51QXnj4eTLzoaSqwAEIrMRnxIUlpMlR_zjMGB7f5P3oBBSM-7E0Zy9ih6eP77fF8y_EFzoAhijRLrPQ2RQRvW0b1UrLCSG5yUaY1whUVFucW70AqSeFC4E17hsqCiBC04k7Jue_E1CSJUhE3jUfR-0ARbsnGp2RJRYCpOGpJEXxGtYkXefTt-FVdwDMWxBgXUs8ObXml6agyA6FetD6-AhY59tevFSG3TDxFfL5LRpCOH8FXUyxd5BcopUB5EC3LdsFkWsjCNQVouXIlaTon0jAQoZCeo_pPxr1hkj3CgRc2uCJsQpIcDxS_CB7GdiuErhatbLmlAxR60Ck_9eG1UM6FXo0jHe3qitLkYwUH2hrNqOve2Z43U7O355KD2Hz31ITYv6lRPNW0fcjDu_CYP0uAVAZ2WvAq6Gw_v7EL0fEPUaP95cvfXU0YEXSRE-xbHLyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca7ecc06eb.mp4?token=oAySrLg2qqjs9IYMM6Lov0MYGfPLrxVxQTirmcC4QiODkxu16fPCrbuc9C2MR0YorXOgnzCYSiZezJp72rGgzQqV4zQsjskLhd0xZtx5_wWU3C01fPYlJBjGBfheJHvxcAdAH3Dj_kwBhgab1EMIImjvZyOPn4P49iIiJ1xDK8924YKmJk2cxTiETxRbvUVhbRWyQrxeChTkNMtPsb6N2TpuiCBXngPkqbjSFBd51QXnj4eTLzoaSqwAEIrMRnxIUlpMlR_zjMGB7f5P3oBBSM-7E0Zy9ih6eP77fF8y_EFzoAhijRLrPQ2RQRvW0b1UrLCSG5yUaY1whUVFucW70AqSeFC4E17hsqCiBC04k7Jue_E1CSJUhE3jUfR-0ARbsnGp2RJRYCpOGpJEXxGtYkXefTt-FVdwDMWxBgXUs8ObXml6agyA6FetD6-AhY59tevFSG3TDxFfL5LRpCOH8FXUyxd5BcopUB5EC3LdsFkWsjCNQVouXIlaTon0jAQoZCeo_pPxr1hkj3CgRc2uCJsQpIcDxS_CB7GdiuErhatbLmlAxR60Ck_9eG1UM6FXo0jHe3qitLkYwUH2hrNqOve2Z43U7O355KD2Hz31ITYv6lRPNW0fcjDu_CYP0uAVAZ2WvAq6Gw_v7EL0fEPUaP95cvfXU0YEXSRE-xbHLyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
شهربانو منصوریان: برای ما دام گذاشته بودند؛ کاری می کنم ووشوکاران ایران به ترکها ببازند
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/104454" target="_blank">📅 17:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104453">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/836636a573.mp4?token=lToROset1oJ8wukIJ-nk5Zd4zG_06S11ENBRAlBE5H6akmoWRYxdlCsoG839U2MKQp3DoEIK8ZINJrBkaM7M060pYtnS8INuWVdutpgwoTpbuBoJ667B82cU1Y1o6j-Xuare1A7NPOEHZdyC6b755qMwl8domyyZe0xMJZs0UR11gYr-QcWD89rMDlk6rL5mbXkeCjLdT-GPAso8hwete4NzdV_y6wntVQxGj_n-Ai18WdAxsenAaGUNsBob53rOaoGeERs56wU1NevAcLq0I3xGhxF6Oobvw4DhobTQ7_uPhJhBZGU7YAhyF-f5YVIpwYpoXgNSn3qi7ecGELkOFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/836636a573.mp4?token=lToROset1oJ8wukIJ-nk5Zd4zG_06S11ENBRAlBE5H6akmoWRYxdlCsoG839U2MKQp3DoEIK8ZINJrBkaM7M060pYtnS8INuWVdutpgwoTpbuBoJ667B82cU1Y1o6j-Xuare1A7NPOEHZdyC6b755qMwl8domyyZe0xMJZs0UR11gYr-QcWD89rMDlk6rL5mbXkeCjLdT-GPAso8hwete4NzdV_y6wntVQxGj_n-Ai18WdAxsenAaGUNsBob53rOaoGeERs56wU1NevAcLq0I3xGhxF6Oobvw4DhobTQ7_uPhJhBZGU7YAhyF-f5YVIpwYpoXgNSn3qi7ecGELkOFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟢
سوپرگل ترینکائو ستاره جدید الاهلی عربستان در نخستین بازی شب‌گذشته خودش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104453" target="_blank">📅 17:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104452">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/653b7ca74c.mp4?token=kHUSfULW0cKBEaJWTTgR28SEq-ZR8GUzxZ2Tnpwqycu2CNAoRPSCEU0J8RVTcPBI89ILPQqfNJf5kgG1lbyx5MMuhk4Tlx15ezgXBqOkneVqkvrs-aCbyFIHHtgc1v1S2CSUlnPICh29T3GPZxucAF80VQ36h5Hkv9WMEYGFZqvDzh8CgkFTc2caGGci0whHgr_pQK8ofg41aipzeK11VgQHPyMhPtA5INMgR4g6vmR5xGKNkZ4IWIAmgJ3KrXLlq56p42zKPIrhRg5CuWicOxTw-kLti--3_8Rqc7gwZwD4kKpqaZFcnWrn6bQVLmWjwnJmWYWrH9ELRTX58C80pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/653b7ca74c.mp4?token=kHUSfULW0cKBEaJWTTgR28SEq-ZR8GUzxZ2Tnpwqycu2CNAoRPSCEU0J8RVTcPBI89ILPQqfNJf5kgG1lbyx5MMuhk4Tlx15ezgXBqOkneVqkvrs-aCbyFIHHtgc1v1S2CSUlnPICh29T3GPZxucAF80VQ36h5Hkv9WMEYGFZqvDzh8CgkFTc2caGGci0whHgr_pQK8ofg41aipzeK11VgQHPyMhPtA5INMgR4g6vmR5xGKNkZ4IWIAmgJ3KrXLlq56p42zKPIrhRg5CuWicOxTw-kLti--3_8Rqc7gwZwD4kKpqaZFcnWrn6bQVLmWjwnJmWYWrH9ELRTX58C80pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤯
🐐
یک ربات انسان‌نمای چینی در جریان مسابقات جهانی ربات‌های انسان‌نما در پکن، مسافت ۱۰۰ متر را در ۹.۳۹ ثانیه طی کرد؛ زمانی سریع‌تر از رکورد جهانی دوی ۱۰۰ متر مردان که در اختیار یوسین بولت است
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104452" target="_blank">📅 16:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104451">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2308ddcaed.mp4?token=DCfyU0pgf-OFWACOi9etNegfXoCYIEUHsu1CJp3zPtv6nlPPVqj1vfsKWKK1yUmqUo037HnHAkKo9VDdvmQAX1wBotaBackNPMylx9fwTicFGwm4yx4PwmzNeoo83PJpXsaU_xBoiCl3NveMQoFr9a7Otv0xOaL1jKd0WXaOeZiOwB-ANc0D7GKZXt1OYg_mWtI_9se7TZNUVgjSSoIzyoNrNIkD8T57mJq6dqlSIFVI4Bzfzt9FEuXDk0eclYsAunZLnRKNUvQLUrdB4c_3uR1QVkiuG82iRTinF4b-sNSBas6q7bzM1wTgrzX0VzBkh_qBgo6RN6UTJ-Eov78h4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2308ddcaed.mp4?token=DCfyU0pgf-OFWACOi9etNegfXoCYIEUHsu1CJp3zPtv6nlPPVqj1vfsKWKK1yUmqUo037HnHAkKo9VDdvmQAX1wBotaBackNPMylx9fwTicFGwm4yx4PwmzNeoo83PJpXsaU_xBoiCl3NveMQoFr9a7Otv0xOaL1jKd0WXaOeZiOwB-ANc0D7GKZXt1OYg_mWtI_9se7TZNUVgjSSoIzyoNrNIkD8T57mJq6dqlSIFVI4Bzfzt9FEuXDk0eclYsAunZLnRKNUvQLUrdB4c_3uR1QVkiuG82iRTinF4b-sNSBas6q7bzM1wTgrzX0VzBkh_qBgo6RN6UTJ-Eov78h4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
هالند نادان با موهای تراشیده در بازی امروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104451" target="_blank">📅 16:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104450">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da4f666bc.mp4?token=i6Z3cCYtZZGLxYpkBTyDCCoEAtQ4NthnNO-R695XLV6PZuRUvy5HLXs0xA2Qb-Jle7foLu7AW6ZP0AntHwb-4wAnsb2mK-bESyasJE2e0469GFwC6uByuMd4SjSyBpcfYSNb7o3baOzgV3lygBUrHDWYfF0Dph7NAj9xEaBDIFgIaKDH9ts5FjP187nnslnbNnzeyqoddHUwizUeg1KbHYbd96xKdo_x-h1G8OJXFNEGz_um4Cx0E8VDPe2PmS91tLDDuz6CWHZkWC27LNHeUsn3GPwv92EFdS600xCjmc2-jz0EpYNBowwNQ0QQS4rbWAVago_82jdHtkI2LLiCeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da4f666bc.mp4?token=i6Z3cCYtZZGLxYpkBTyDCCoEAtQ4NthnNO-R695XLV6PZuRUvy5HLXs0xA2Qb-Jle7foLu7AW6ZP0AntHwb-4wAnsb2mK-bESyasJE2e0469GFwC6uByuMd4SjSyBpcfYSNb7o3baOzgV3lygBUrHDWYfF0Dph7NAj9xEaBDIFgIaKDH9ts5FjP187nnslnbNnzeyqoddHUwizUeg1KbHYbd96xKdo_x-h1G8OJXFNEGz_um4Cx0E8VDPe2PmS91tLDDuz6CWHZkWC27LNHeUsn3GPwv92EFdS600xCjmc2-jz0EpYNBowwNQ0QQS4rbWAVago_82jdHtkI2LLiCeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیخ‌منصور قشنگ سیتی رو خالی کرد
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104450" target="_blank">📅 16:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104449">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ynlw_FAcM2ydff496f5UX1G4Rqwd6JEbMgz5M1hkS5QIET35caGNWYy8nuo7rBfMuSKLpgtP8_bU0imS4zJkC-E0ZdsDOT4952sHUXJBBHx3V6wowRV3HPCtVKC-QbuMlJKcQJQHgA4IXPAP20ql-VH4pCrHJt8nsa5qor06K1kTAbPnMn7MdPxjwP-SIq0yH133-2vy_0DKrIeHMWmxIwaRvWCVGRso-2r2CJwIprU5XFvis7TrM4uXGLBVDgW90pIhbe-6VC1dP9pENf5TzICp1GyIMFs4-ih__CIEtU_pIE4e71zPYfDIH0DjKqN8WibrZpWvINTo7lNwS_f1jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⚽️
بهترین بازیکنان یازده‌فصل اخیر پریمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104449" target="_blank">📅 16:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104448">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87c342598b.mp4?token=qBrpY4AKjcqWziTQ7tGqRuNo0E9LXnAbqsgaYdJ4wdmE5hO18hxvZNDcHi-qsrx1-sG6sSwUs3-TnSiKfZf1XxPYzwmbzsomQ1-hUNBqVAwDdUZkErbJDScodqQ4sUcvc9gdz4urVPSnD54cY6CCBiQ1YfUxbXs1UjXRf8DqAG9ROhR8_yBrH1d5pDnhICKcmIHe8Xf_WGZ7FVfJurrCkdDTQJpdcw8QKZuRQmkUGmX7wJufAlP-8p2bgRVRTe1vU6JcWaiUoQKo0okaRMK-jRBPBu-yAxvRdC26aoktB_8qhFY1MjISVCtday1lzgXqtLGrtLIbRw1eREEDxoBYeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87c342598b.mp4?token=qBrpY4AKjcqWziTQ7tGqRuNo0E9LXnAbqsgaYdJ4wdmE5hO18hxvZNDcHi-qsrx1-sG6sSwUs3-TnSiKfZf1XxPYzwmbzsomQ1-hUNBqVAwDdUZkErbJDScodqQ4sUcvc9gdz4urVPSnD54cY6CCBiQ1YfUxbXs1UjXRf8DqAG9ROhR8_yBrH1d5pDnhICKcmIHe8Xf_WGZ7FVfJurrCkdDTQJpdcw8QKZuRQmkUGmX7wJufAlP-8p2bgRVRTe1vU6JcWaiUoQKo0okaRMK-jRBPBu-yAxvRdC26aoktB_8qhFY1MjISVCtday1lzgXqtLGrtLIbRw1eREEDxoBYeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇳🇱
دومین‌نمایش درخشان ترشتگن در تیم‌آژاکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104448" target="_blank">📅 15:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104447">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd1e841a3.mp4?token=hFcuyBHKgqVfYR4u18TmiS-tJWFGOXqyGM0L3-5_61KANXqqxXXEvz82kTs4crixOCyjibWxGKEDT1OepvQGf6bnxvq2Vn7adbWUBU2FXWsZagfhVPSaaakKJ9gXr8IAyGl8tOp0--PDLwxJCvII8JDcMSqSjA3Kw5Lfn_CLkM360KaNk7_0BNqngVsgC9PpR7X2179v-8zZKLTu_a2i4qKHSJAq_jvmUn2pcBiT-qxUxk52whP0VV-r0Q9msDolF1pdXNq_ZZHZ74N1BFdPL7IHzeHvu0Lbd_EApwg0MsFuHF-oMHUqNOnDkOEu5dL3IIT6xGuO_jsIn47wQeZ1vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd1e841a3.mp4?token=hFcuyBHKgqVfYR4u18TmiS-tJWFGOXqyGM0L3-5_61KANXqqxXXEvz82kTs4crixOCyjibWxGKEDT1OepvQGf6bnxvq2Vn7adbWUBU2FXWsZagfhVPSaaakKJ9gXr8IAyGl8tOp0--PDLwxJCvII8JDcMSqSjA3Kw5Lfn_CLkM360KaNk7_0BNqngVsgC9PpR7X2179v-8zZKLTu_a2i4qKHSJAq_jvmUn2pcBiT-qxUxk52whP0VV-r0Q9msDolF1pdXNq_ZZHZ74N1BFdPL7IHzeHvu0Lbd_EApwg0MsFuHF-oMHUqNOnDkOEu5dL3IIT6xGuO_jsIn47wQeZ1vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
👀
امیرحسین اصلانیان: در رستوران عابدزاده همبرگر خوردیم؛ غذای احمدرضا رو هم من حساب کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104447" target="_blank">📅 15:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104446">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d764ecc24.mp4?token=j0a2aWS40_anWajTAwEUsl_rK7YbYjsHNMuIDUv7FkQiURRCG8DHhaXyLNlo3r0Rc114LD2gnf5QT0ID_tEhhpk5C47toI5ZWwaMopldnit82YAAXYaGauOvxBhOiCMr9Q0DSHs4f0eNzAcfN8peYYDaZ0myjIdOXpn-b0UiOVCBjvNMViASzwPhbnOyCPxTJzSLMLTlNQhVsKIIjtNHPcae4ZgfcyuDv_bogg341mdMIwMOsKhn2RHB8oqLUpb6BtV4GeZ_gBEEJpoI6-0JhVD6yL7wa-Djfv7P0xN0aCp6_KefTGRW-0htF7pnbonT-EC6g36Ommxwq51VNUcx0mNAYwGZSUTs8TLTyo-A7Tj9EeS2S6ipm_qElAB6gGdomXBYuRY-DxlDxwJ5ACGRM3XWJKVCPah4ir0ydO9gb3hphRzekQcDo4n2BDoq9O4tDCDWLo5QYD9Zb6MpkEyRtMK8uVeJSxIU9mx4Aa_mzvJiZqsJ6ttgaQZoSAMnDkalNZh6m-6wlfQlkUqvY6T1dV1tSCyZE7W7okvhhNXZXFP7Jbmd56k6PbzvmG5K9SJgOOSGaMUyBYncGSjQd9yIDlyq7CnyVLXsCX2kBRXmGkChGJ_e3uvZXHZDKZokoR_jUjweNFYtCZy2OA_smOZwDNDX8-HEW1Y2weeED8wJivM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d764ecc24.mp4?token=j0a2aWS40_anWajTAwEUsl_rK7YbYjsHNMuIDUv7FkQiURRCG8DHhaXyLNlo3r0Rc114LD2gnf5QT0ID_tEhhpk5C47toI5ZWwaMopldnit82YAAXYaGauOvxBhOiCMr9Q0DSHs4f0eNzAcfN8peYYDaZ0myjIdOXpn-b0UiOVCBjvNMViASzwPhbnOyCPxTJzSLMLTlNQhVsKIIjtNHPcae4ZgfcyuDv_bogg341mdMIwMOsKhn2RHB8oqLUpb6BtV4GeZ_gBEEJpoI6-0JhVD6yL7wa-Djfv7P0xN0aCp6_KefTGRW-0htF7pnbonT-EC6g36Ommxwq51VNUcx0mNAYwGZSUTs8TLTyo-A7Tj9EeS2S6ipm_qElAB6gGdomXBYuRY-DxlDxwJ5ACGRM3XWJKVCPah4ir0ydO9gb3hphRzekQcDo4n2BDoq9O4tDCDWLo5QYD9Zb6MpkEyRtMK8uVeJSxIU9mx4Aa_mzvJiZqsJ6ttgaQZoSAMnDkalNZh6m-6wlfQlkUqvY6T1dV1tSCyZE7W7okvhhNXZXFP7Jbmd56k6PbzvmG5K9SJgOOSGaMUyBYncGSjQd9yIDlyq7CnyVLXsCX2kBRXmGkChGJ_e3uvZXHZDKZokoR_jUjweNFYtCZy2OA_smOZwDNDX8-HEW1Y2weeED8wJivM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
صحبت های مهدی توتونچی در مورد شادی شجاع خلیل زاده مقابل سپاهان اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104446" target="_blank">📅 14:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104445">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b843ddc780.mp4?token=qwMt9XAV7eK96wjosQ8j_9oZlrY2Y_Yme9RgVDyHuU4cy3DdCL4xT4DfELezuD3LjvEmIdyoOmo1vpxVrHV1TryrkSqnCPZ_VsOgFM3c1_GfWpWrZ66nb80wrO_ZpnvGrpddQgqvX5ZgI4hp3dBMuPHkRLxBQEO9ohSHLY3rOEZEfxHN0vw-uEGjgFYmNnRmo98dqMlwSPieO3KxJBXNqu2VKIRfZCV9ECArpC0yoyGMG1v1QRHHMOi-8s5rpXdKqB9SM44VRf5r8tlRsiiFThhadzVMyn5qsOUpb7ix48UqbPyuAwqiQfMjoJNSnSHvFIOznxlD1UkARW7bo6iFoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b843ddc780.mp4?token=qwMt9XAV7eK96wjosQ8j_9oZlrY2Y_Yme9RgVDyHuU4cy3DdCL4xT4DfELezuD3LjvEmIdyoOmo1vpxVrHV1TryrkSqnCPZ_VsOgFM3c1_GfWpWrZ66nb80wrO_ZpnvGrpddQgqvX5ZgI4hp3dBMuPHkRLxBQEO9ohSHLY3rOEZEfxHN0vw-uEGjgFYmNnRmo98dqMlwSPieO3KxJBXNqu2VKIRfZCV9ECArpC0yoyGMG1v1QRHHMOi-8s5rpXdKqB9SM44VRf5r8tlRsiiFThhadzVMyn5qsOUpb7ix48UqbPyuAwqiQfMjoJNSnSHvFIOznxlD1UkARW7bo6iFoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
ناراحتی شدید همسایه ورزشگاه وطنی از شعارهای رکیک هواداران در بازی‌های نساجی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104445" target="_blank">📅 14:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104444">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90391f76b.mp4?token=rplt0aoXnyU5bLqrsPjsBqK4McjV8NeM1-w1eEs27S_JdVu1DqyD0vCGvyY2wBA4Lzbo6p7HtVMf0rq6RWPyobm-vzzMZbgsgqKjV4Z5U_fhu8zAhMgZhvs1sYxHDnGlBF_6SiPMONJu_P-aoxjfZTqIL-DkIZDRsnPMOjstW-cDV4rbEYuH2kf8IEkPdl9rfmJDh82kQQp39cCAqx6_98Fb97DwzzClkX55UFfAJg4Bav9jG7O4b6B0HkknsxwOxkybuQF0hgGJAGkjJrttyl73fkGYrCrZbU5M0_vuO-0jo8MqUEuvXi3NzjMLWTG7HplBSwgh7AZHsphIeyyfGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90391f76b.mp4?token=rplt0aoXnyU5bLqrsPjsBqK4McjV8NeM1-w1eEs27S_JdVu1DqyD0vCGvyY2wBA4Lzbo6p7HtVMf0rq6RWPyobm-vzzMZbgsgqKjV4Z5U_fhu8zAhMgZhvs1sYxHDnGlBF_6SiPMONJu_P-aoxjfZTqIL-DkIZDRsnPMOjstW-cDV4rbEYuH2kf8IEkPdl9rfmJDh82kQQp39cCAqx6_98Fb97DwzzClkX55UFfAJg4Bav9jG7O4b6B0HkknsxwOxkybuQF0hgGJAGkjJrttyl73fkGYrCrZbU5M0_vuO-0jo8MqUEuvXi3NzjMLWTG7HplBSwgh7AZHsphIeyyfGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
اسپانیول، اولین قربانیِ رئالِ مورینیو.
🥶
☠️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/104444" target="_blank">📅 14:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104443">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a456af91c.mp4?token=CVobrvKm4MGN0rG8YuWFo3Ea3SknFlJmOT7e7He3ag_hCwaCHGCLgQdp83GxMkbBjZe-HqoACFs3MwcE7AfRE9S_LZtUlHSG8EbzHFdA6vJQx_NTxqhhUOgYNu38NhroE82p2dMsMRbTgc64cMPKSU1hzJue5zyvcJkTk-voHDF5s53GLfqmxs-mFLQhjGq32jNPU8v2xKEHtSyuArTv3ZL7bmMMiUDaPKt3g1Mo_1N6sA2xE2fJbvTsLWZuXXs3kbJQZ3ig1PbVs9y-DwxFE2aMJbznxciu9v8HPT5i0NqMqT8NjBQG2okGqJtkqrulVjc_8YfPV7HhklaCiWUY7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a456af91c.mp4?token=CVobrvKm4MGN0rG8YuWFo3Ea3SknFlJmOT7e7He3ag_hCwaCHGCLgQdp83GxMkbBjZe-HqoACFs3MwcE7AfRE9S_LZtUlHSG8EbzHFdA6vJQx_NTxqhhUOgYNu38NhroE82p2dMsMRbTgc64cMPKSU1hzJue5zyvcJkTk-voHDF5s53GLfqmxs-mFLQhjGq32jNPU8v2xKEHtSyuArTv3ZL7bmMMiUDaPKt3g1Mo_1N6sA2xE2fJbvTsLWZuXXs3kbJQZ3ig1PbVs9y-DwxFE2aMJbznxciu9v8HPT5i0NqMqT8NjBQG2okGqJtkqrulVjc_8YfPV7HhklaCiWUY7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
جلوه‌هایی از مسابقه دیشب لیگ‌عربستان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104443" target="_blank">📅 13:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104441">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrF3qRuxtLlV_JXrUXjzEz4sRtTrifTPmhh95UJw-NvYs8RTu6MZ20HENUQZoaCN47lJrGMCO5oU09haLe2y9PLQqqQHKQ5jkmqGVwbTsq6bEt5J-rODw1WpJc-Mbwwc8In9N9MzZz2Xs1DZizuckq75KA-T1HDuTyusps9ydNPIOt6Nf1WD133XjdhXmYAuN4v2KkQYbw9WNPfczPDRl5qDe91uZhr3wX8WljaUUC0jHKRkt_Vb5CAUHc9QY87DuU1sNEyH6JwN-3LbZgDWL33cwAyL6nURqLUvptpBTH_PW_XPMtyxDtXpoTT8d_sdDlXNCgO-hbLiCVrW-p2lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfxXKFoqlhqAHjPZeM1g0sLBI1Qd3X39-28W63L2zqENDt6RVQO_o3SBDoZWdugJPgaMep-G0K785TPmzLpGCMDEomy_FpiU1YMXxp9W0BDsmLpdgoKDQ9iXQmNQsnrUiD8FcPl7IjACP0zkLqdiS2g2-lRxJI6qq6Bj6eTtrXHZ7WT-9u-5qFlcIBrO0x8daSX3YiV2lNYQ05iBqT0TcxzdaIgYsV9BOQCwp7bhQWMzYb8S34Kws0L_Dxc_dXaCqx62oDl5xcWpKYb6WeRqyb7WyXfL73fc5ifGYGDyTaYFJnwe7TmFd0fXMRAEXHwd3mAU1qGM1P-IMoGl_tuKFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیوفیس جدید ارلینگ‌هالند
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104441" target="_blank">📅 13:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104440">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5669817976.mp4?token=ThiDaQuJUVJXWMt9auOR13jpe6E_1xVG4wx6-LcHFKr6Sufpy4uxQl8JL0s-LwcNfeNHuA5pkbu8alvOIBjliMBCUmDJKYydDdxVo9DOTc4HzN-SrTEqK4p3rzBlSe_h7OgT8dC-sPYXhORWce7mX4-XeS6og6TcpS2ttIEx6RFzr2KZRalMC7VpEsfE3v60fvzxS6QS6X9q47DIyVkLpEt1ijiuTe6hh-DP810SJ9j8tOsjLfLeaGvtEhjPbHQdCJcmoqLcNf3wYT9lGbFd4QJVm3IAwOQPyKGdcuIab_Iyvdx72akRYJQUYg7QhQETR7PuHYEvtwzQPgElVHxnMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5669817976.mp4?token=ThiDaQuJUVJXWMt9auOR13jpe6E_1xVG4wx6-LcHFKr6Sufpy4uxQl8JL0s-LwcNfeNHuA5pkbu8alvOIBjliMBCUmDJKYydDdxVo9DOTc4HzN-SrTEqK4p3rzBlSe_h7OgT8dC-sPYXhORWce7mX4-XeS6og6TcpS2ttIEx6RFzr2KZRalMC7VpEsfE3v60fvzxS6QS6X9q47DIyVkLpEt1ijiuTe6hh-DP810SJ9j8tOsjLfLeaGvtEhjPbHQdCJcmoqLcNf3wYT9lGbFd4QJVm3IAwOQPyKGdcuIab_Iyvdx72akRYJQUYg7QhQETR7PuHYEvtwzQPgElVHxnMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
ادعای عجیب و قابل تامل هواداران استقلال که مدعى هستند كه كيفيت پخش بازى هاى استقلال پايين تر از پرسپوليس هست و اين موضوع درحالى مطرح مى شود كه بازى هر دو تيم در يك ساعت مشخص و در يك ورزشگاه بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104440" target="_blank">📅 12:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104439">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcwhlQ5kqGu9sNo2pm-cofQ-rm7sZ0Efs3RUXpDFrzasf6Z5EBhrX51_BvtWyxuy1zC2viRHIaH8h-LKI7dsADR9vRvPRYdFRbanH2Mph70VT_QNBSVbDN5-oLnxS4P6w8dYrCQiXes1PnYVEkeai4J-0P0ZdFI8sf66lnEd3Eb03K-Jixm7On72zIdzWgoNwm-hU0AbmHMQ63e640ffJzlo4nq_mAgFtzigC6_pf8rYEvQD2JHVcz1t-z8gjIYgpmOgABvvXeLzgRE1puBh0_MeIzN7Ml4ZbXd8wDhpT9Y4_caLU3xGqEl0osFuCkhwWLX1RzU86-zKFB3EKi2xuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست بازیکنان بارسلونا برای دیدار امشب با الچه بدون حضور بالده و رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104439" target="_blank">📅 12:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104438">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03e1a23b0e.mp4?token=ZmwSjfgjWWL6yofMpfeJAMsCM5zR1PCUTk5f0EsRed3bVrMCwn6Jy8mXRZGrTCJfxQlEisluXSxX6Tyfed505QJQFKuQ1qxKjN66b1M1pJhCEM59FxBvTihotPoVgNHI51y7TJ0JfaFv2jw7S3xrK1-GsI65CUAJo4AWetjEKqYBigJ0VNsgAYeWK2cibwRaqGpmoTiaus23NsZmwaqfHCWs5FU3HvOtY2MlJN0NQFqncRABnAMZQ3By1yQa__8beMr4cJGc1IlGhqMWOXPCDT7vTv9Xp23ngV3P2XDL1S4HHWenOiE1XYcMVdYbb6moTW68x18ahKLgi2IKe-9DJXJyvU5wq2wLqEuxky20KrywHcLCWVI9C1gADH3DUdg49Qh1RjpdQJYm7IeekzqUx30P1K9xS0ta1W4RvyhfvNHhzJoh6E3AIlCTFM3J_kLXAjbYL3ppzsHcOAEeI8duLkQb_3zbIy50LFngKZNrYPISflRQPKWV8j5BIo8BOJLAcK0ywZ2d72z3MQRvacD2Gm-JM0V4A0sTPULNLBa9xwyMmhzyDPFbtYKvdQPfcx_mx79zTL9S7AUDuYjKKNpObsMxIrKabknYC0g0EV10O4DOuA9qSTBx-xE5XddQxFfDNuge1MXahPARDKfHQzyjDHpLLaxdu_oiCQ64HH7D2Bo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03e1a23b0e.mp4?token=ZmwSjfgjWWL6yofMpfeJAMsCM5zR1PCUTk5f0EsRed3bVrMCwn6Jy8mXRZGrTCJfxQlEisluXSxX6Tyfed505QJQFKuQ1qxKjN66b1M1pJhCEM59FxBvTihotPoVgNHI51y7TJ0JfaFv2jw7S3xrK1-GsI65CUAJo4AWetjEKqYBigJ0VNsgAYeWK2cibwRaqGpmoTiaus23NsZmwaqfHCWs5FU3HvOtY2MlJN0NQFqncRABnAMZQ3By1yQa__8beMr4cJGc1IlGhqMWOXPCDT7vTv9Xp23ngV3P2XDL1S4HHWenOiE1XYcMVdYbb6moTW68x18ahKLgi2IKe-9DJXJyvU5wq2wLqEuxky20KrywHcLCWVI9C1gADH3DUdg49Qh1RjpdQJYm7IeekzqUx30P1K9xS0ta1W4RvyhfvNHhzJoh6E3AIlCTFM3J_kLXAjbYL3ppzsHcOAEeI8duLkQb_3zbIy50LFngKZNrYPISflRQPKWV8j5BIo8BOJLAcK0ywZ2d72z3MQRvacD2Gm-JM0V4A0sTPULNLBa9xwyMmhzyDPFbtYKvdQPfcx_mx79zTL9S7AUDuYjKKNpObsMxIrKabknYC0g0EV10O4DOuA9qSTBx-xE5XddQxFfDNuge1MXahPARDKfHQzyjDHpLLaxdu_oiCQ64HH7D2Bo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
🇮🇷
صحبت‌های زیبا و حرفه‌ای بانوی هوادار ملوان درخصوص شرایط این‌فصل تیمش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104438" target="_blank">📅 12:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104437">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWFRwhgg5j6Vk3GpSyufZn2eSobc7SD8hOX6klcU36ynr8O23m5PMDC7gTJoM4EGmsrhWKIjtoOUut3-r2KtFyY3WKN7xPV_y4w20pgT8nZBUTMzVhmorNnWQPIcOZdxVpi-Zp_w-zxcXL9Sf_aa2FxO0PaBDk2VcGMnCHZfGsfXaiyKTNnmSjjtmj8UJGb-519oFFweYgizN3fqjOOOHDjLRXdATzv7Z4_4vNrHVl3KEvt5gfYOCXmUyCnEFD7UGqxC1Q3dylUiKf9ILXHA275OCoDBgrlGjrEGKMsm8RjkqFiluWFJYYkRTgCSnaX0a40MFu3Lz7m-kJ_hhI7aMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
مدیرعامل فجرسپاسی: به سازمان نظام وظیفه برای جذب علیرضا بیرانوند نامه‌زده‌ایم و اگر‌ مورد موافقت قرار بگیرد، از ابتدای مهر در خدمت سنگربان تیم‌ملی خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104437" target="_blank">📅 12:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104436">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1928a613f1.mp4?token=FKSOfVCWO5b256h_Xst6JfIQYZalrLXAgBXLsCjnim9kAnfz1fraR_sAZw6nLlMwITGgJXw-cLoFaa1CWlzj5sQBtxxZ3insXjzbfduD_BaoY0DgY_nuMq-V8c_nQPgkP6pI0mbghMMQ_5bedUNtzCwZz5jZsixctFKoG0HdPoLMOZhN8bA9Lq03a723sgRfp4Ox9Nkk8eKON0czqD2EZit6xiytnL0RoBmXqSiD1B-kk3rEQxki-1WT85Ma3jPi64Jk23BzfwnoiVucE5OLEAbF9hKoXLeIh22IG3OpO_jknVOZwvDH-rEtFQ699IP9K5ipgEC6dr-7S6CIU8F8Fayuu7wHRFteASUrmcMJJCUx4D6i5odZ7bQEoC-tLXuIJiZlnY0oM54oXud3lmXyKjRvBK5tOxmBASCLzwopnHMQkEdX0lvDFTlDADBL-KRAwcan-bYiuWZVTCgBElZlVjFUKMm8iqHECO8fSv4WsSZzikzqjpqM78xO-tyDI_YuZ7XZ3SYSe2uPkFYbw1yMKyy-QZoWMgjo_C_XwolwPqi89hdTJQQiehLHIfOBUEi9MvLVBbitC_8Ap0_CgUgkQ4Rn58pphfnn7rHO2hyCGVqjesKMpaT2tdEerVJ_dhwuNNbj52TZ2EEElLx6t2Js51Tizz8YGLhQFUmMN8SIOKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1928a613f1.mp4?token=FKSOfVCWO5b256h_Xst6JfIQYZalrLXAgBXLsCjnim9kAnfz1fraR_sAZw6nLlMwITGgJXw-cLoFaa1CWlzj5sQBtxxZ3insXjzbfduD_BaoY0DgY_nuMq-V8c_nQPgkP6pI0mbghMMQ_5bedUNtzCwZz5jZsixctFKoG0HdPoLMOZhN8bA9Lq03a723sgRfp4Ox9Nkk8eKON0czqD2EZit6xiytnL0RoBmXqSiD1B-kk3rEQxki-1WT85Ma3jPi64Jk23BzfwnoiVucE5OLEAbF9hKoXLeIh22IG3OpO_jknVOZwvDH-rEtFQ699IP9K5ipgEC6dr-7S6CIU8F8Fayuu7wHRFteASUrmcMJJCUx4D6i5odZ7bQEoC-tLXuIJiZlnY0oM54oXud3lmXyKjRvBK5tOxmBASCLzwopnHMQkEdX0lvDFTlDADBL-KRAwcan-bYiuWZVTCgBElZlVjFUKMm8iqHECO8fSv4WsSZzikzqjpqM78xO-tyDI_YuZ7XZ3SYSe2uPkFYbw1yMKyy-QZoWMgjo_C_XwolwPqi89hdTJQQiehLHIfOBUEi9MvLVBbitC_8Ap0_CgUgkQ4Rn58pphfnn7rHO2hyCGVqjesKMpaT2tdEerVJ_dhwuNNbj52TZ2EEElLx6t2Js51Tizz8YGLhQFUmMN8SIOKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
خاطره شنیدنی حسن‌روشن پیشکسوت استقلال از دربی معروف شش‌تایی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104436" target="_blank">📅 11:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104435">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d84a4cfcf4.mp4?token=TZBlYY-gn0N8rTuhiBJ-jyfFGdE2PBR0g_kK7CF1OXSV0r9f9rPvllt_iIVt7M7eLVZe9uunrXpDpQAUcVJ3OSBJr20ZMk2DIZTbgDzthsA_fFJ8gK_Ow862aIJzvUCadYhssmy97l3686ygOqbqjMyZTLzc-DDjVxh7qqdLt1Qs6EKn6--_a_wLSeQGdMfufDsQHP5PCayZmWilEKq9-aFDytq39pzvtQJtZm2aiJF8-gNFkUZU804SjmhWgoVm9JH5wWx6ZDcVvs-aiGlTxvQhn87L29JieGj7n9B2uT_w_M_RGVmmgzftRi3KY2VwOjCYtAeZq5pwSpbjRsOPvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d84a4cfcf4.mp4?token=TZBlYY-gn0N8rTuhiBJ-jyfFGdE2PBR0g_kK7CF1OXSV0r9f9rPvllt_iIVt7M7eLVZe9uunrXpDpQAUcVJ3OSBJr20ZMk2DIZTbgDzthsA_fFJ8gK_Ow862aIJzvUCadYhssmy97l3686ygOqbqjMyZTLzc-DDjVxh7qqdLt1Qs6EKn6--_a_wLSeQGdMfufDsQHP5PCayZmWilEKq9-aFDytq39pzvtQJtZm2aiJF8-gNFkUZU804SjmhWgoVm9JH5wWx6ZDcVvs-aiGlTxvQhn87L29JieGj7n9B2uT_w_M_RGVmmgzftRi3KY2VwOjCYtAeZq5pwSpbjRsOPvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
کافه‌های مردم پلمب، بساط لاکچری بابک زنجانی پهن؛ عدالت یعنی
پشم!
در حالی که کافه‌های ساعدی‌نیا به‌طور کامل بسته شده‌اند، بابک زنجانی، مفسد اقتصادی حکومتی، شب گذشته یکی از لاکچری‌ترین کافه‌های تهران را با عنوان «VIP» افتتاح کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104435" target="_blank">📅 11:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104434">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ff1QydhtxWKsrEWo8XN3J0l0nfROwQiY6lBaVr_Ubm8s55PQ_EHuI9w-qKDY1ZRYRUtv4is36HrZhRti08Bzk7aHo7XZp2ijYqBivPZLilFqn93unC-qWg3mBh96YiltZfn7kgL81xtwm4XtSYKrDK0J96eFdgKpVvAKRN0b1dEAB2CCp1V6HWe_B0x3ONT187U0Dg3aBb5eAKvFgEzdiCAtjhs9RuWB6eFei2Xny9IdYLcyBjT298EEhxDeg-n-7rvxVthm2MeJ0x1CKHx7ATuQSBK2JmRwIiaAoPrJouVJM7ngNQWsVWvYByrHDErPS9SQnrWkTbbm42XsyuY1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚽️
مصدومیت وحشتناک چادی‌ریاد بازیکن کریستال‌پالاس در بازی دیروز که فصل براش تموم شد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104434" target="_blank">📅 11:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104433">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if3pLbPNZHfrS77APPTGE0auNu_K7B1ZLVqgSV_ND9zJ4pmw1nJoJBgHO40LA2I8Up4u19fSLCn_O8LCpyqakboRyml5ML6IjaS4iWP8M9YDCnzbWHJPHZmk7aaDRIHYCmhO4kH3Ncfesea2-Irlyp_IZeH7YtilOoUQQbiJDIUsErhX8CF9chtKIaFRQ28sVAVpFvI6x-Ytpntgdor4dHwWer9zJ1M-wo4aXYsmVDqrnN_8PAfvy9EL-_ug0gF6a7IfZAYnZJHsYhcSQXIIukogcCOJr77Gs0w6yZyD8RSe37GHp1hUa1BImPXKZ46i8-d4Ptv7GBjchvh4hPIIAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
باشگاه استقلال با انتشار پوستری برای بازی با سپاهان نوشت: نبردی از جنس اصالت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104433" target="_blank">📅 11:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104432">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7773a1e510.mp4?token=odzuFcyF_eZ5A1N0k6NNnuefz83LaMOGJElwP3SOsR1hCBYkmcAeaDNKGzvM5eTnWDVMinrM8yS_4QFPCQh9H7ULb-0sN0fmK-GSKkMTPjbJzxFL_k1eH09va1F-1JCzWEvy26M1hOMeYrbLTZwpqVijmDR17WWiBVS3iOQe03JE83j_O0qHYWtQE8fo8rjBOifkLP6frQCv8gwO3Vv1oAhIcTW8HzaX7iVnhDfPwiEzWXoZxxI1dKmIKDJDEMO1sjdhCe1vYfWhhbkOC3QmU9XWC_KO1indMS70qmW4OkL5f7PerOdb09LdawdRQk-TMEmrhb0heVqmiDu8_y25yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7773a1e510.mp4?token=odzuFcyF_eZ5A1N0k6NNnuefz83LaMOGJElwP3SOsR1hCBYkmcAeaDNKGzvM5eTnWDVMinrM8yS_4QFPCQh9H7ULb-0sN0fmK-GSKkMTPjbJzxFL_k1eH09va1F-1JCzWEvy26M1hOMeYrbLTZwpqVijmDR17WWiBVS3iOQe03JE83j_O0qHYWtQE8fo8rjBOifkLP6frQCv8gwO3Vv1oAhIcTW8HzaX7iVnhDfPwiEzWXoZxxI1dKmIKDJDEMO1sjdhCe1vYfWhhbkOC3QmU9XWC_KO1indMS70qmW4OkL5f7PerOdb09LdawdRQk-TMEmrhb0heVqmiDu8_y25yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کریک بعد از شکست 2-0 مقابل هال سیتی:
این فقط یک بازیه، می‌دونید، فقط یک بازیه. اولین بازی فصله. خب به اندازه کافی ناامیدکننده هست و دردناکه، معلومه که هست. ولی فقط یک بازیه، پس یهو مسیر همه‌چی رو عوض نمی‌کنه، کل مسیرِ حرکت تیم یا باشگاه رو تغییر نمیده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104432" target="_blank">📅 11:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104431">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/104431" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/104431" target="_blank">📅 11:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104430">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HptiEVJ3nRS-2-6FZBrab_3sq91lZem1h7zYGVv73L_TA8mDaLEwocG-U1hODfrGnLQd6ltSV2zQ_9QHXJTux6SZH4USheTQOISotIeWZgaVVWPEdaFiU1CSnO5D2iY7arB4jISmxx-dy2TBoKuxGtfyDDIAwFeuQfUgrgdYDHFb6FwL8S5xrs0uC27PMd8XjenZlMao56B4EJmj_7ueHt2E9xT3j8gCU5loDrGprYXoaGqHM2sLLXKXMXo7EXHlSD7zDM75bDBqNQ1uH5nawz6I9snQ7XO5ZRcuP6jkSQKZiyWgudOGo4Xmvl9EW2MH3ePuUhfn_dmP-LLtIGqJ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r1
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104430" target="_blank">📅 11:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104428">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c490b878e2.mp4?token=hxyncpddpCIXFBNLXzQq37rMN2B7668QtXs0jz18U8pzS69FN-Zc6WZwbDKANtuMcR2P2R4QfVcMP5sC296rFL850ojZdCtfk9DVMxmMW8pUEH9AMi-TCFWlysiddgYgMO035dqiCR0On5--AcoybI0wum337dRMCtJkpwd1dYP8k8yWT5ZaDDNu272aeHFhAcuQx2eI04_b-e3Pl4-1zfYQABjOLC-qRLc__TtNc-kHJbg5YKuvDYpe6xJrrRVzDh3Ma-H56WaS08uewcLrDs0P52XGjg8jZju2h7cYnmmcOuAvE5rqN88S5kUIyidOA28AjMgWtbSxAFlzL4-Htg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c490b878e2.mp4?token=hxyncpddpCIXFBNLXzQq37rMN2B7668QtXs0jz18U8pzS69FN-Zc6WZwbDKANtuMcR2P2R4QfVcMP5sC296rFL850ojZdCtfk9DVMxmMW8pUEH9AMi-TCFWlysiddgYgMO035dqiCR0On5--AcoybI0wum337dRMCtJkpwd1dYP8k8yWT5ZaDDNu272aeHFhAcuQx2eI04_b-e3Pl4-1zfYQABjOLC-qRLc__TtNc-kHJbg5YKuvDYpe6xJrrRVzDh3Ma-H56WaS08uewcLrDs0P52XGjg8jZju2h7cYnmmcOuAvE5rqN88S5kUIyidOA28AjMgWtbSxAFlzL4-Htg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
خبرنگار: رئال مادرید ژوزه مورینیو رو چطور ارزیابی میکنید؟⁣
🇪🇸
هانسی فلیک: امروز با رئال مادرید بازی داریم؟! در مورد الچه سوال کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104428" target="_blank">📅 10:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104427">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c2144e6b.mp4?token=e8icDRuEAKm2TicwqHcsOfpP38ZY6jBP2MKvZbmJrX0uATth2z8h539XWd3jIg8TvszxF9MYLM3UJrjfZ9Q8WlK-31QqaUaf2CXqEhZM2KiNadGfM2pqsxTpab5N2dNHzfKtRRenLCWwJK4wCgbvIm2JHA6JK5IBwOFNbue2AZ_DfpsdTV0k-Q-ik4mRd4-7OUxI0A7Dp1z30zw9uMZh2iWvHki8ZKPKA58xinNYNU9Hfr60t3N9MZwDTIyysHOQ5kKVtfuWX93jIr_x1IicL0armFSz6NmwNAsjBfB8n8ri1M0LHgKNz-KErhSpUpxo0LONH-w8PGZoasVTqrRkqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c2144e6b.mp4?token=e8icDRuEAKm2TicwqHcsOfpP38ZY6jBP2MKvZbmJrX0uATth2z8h539XWd3jIg8TvszxF9MYLM3UJrjfZ9Q8WlK-31QqaUaf2CXqEhZM2KiNadGfM2pqsxTpab5N2dNHzfKtRRenLCWwJK4wCgbvIm2JHA6JK5IBwOFNbue2AZ_DfpsdTV0k-Q-ik4mRd4-7OUxI0A7Dp1z30zw9uMZh2iWvHki8ZKPKA58xinNYNU9Hfr60t3N9MZwDTIyysHOQ5kKVtfuWX93jIr_x1IicL0armFSz6NmwNAsjBfB8n8ri1M0LHgKNz-KErhSpUpxo0LONH-w8PGZoasVTqrRkqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برونو فرناندز بعد از شکست 2-0 مقابل هال سیتی: "همون اشتباهاتی که فصل قبل تو هر بازی بیرون از خانه انجام می‌دادیم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104427" target="_blank">📅 10:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104426">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👀
💥
پسر رونالدو هم راه پدر رو خوب ادامه میده و در زدن ضربه‌پنالتی استاد شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104426" target="_blank">📅 09:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104425">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f6325ec27.mp4?token=vrJvFBUwb3YXbC0qUlSgfuEWINSNJ-jtAdZDxDfAmWkMfPbN6iDeNfXgPXEY-a9ANAqjTysoCJZdzmsqJnd37tRudc290eY1Urw9iHM6wHOaebroPu7DuKXYcnxRNYJ6V0DtLu3JD5qbd1ulE2MOVbp2czjITPM0weJDOlqiQm6uN-d4XLzIh5rfqzzfdkET2Ykfdb5bXbizP9-ev18CY7F_M51NvBzpaML8nBnrN4ErTOwxe2OKU5MJ6mfRUZqlRhpVArBeAQ9YwU2hYmsPqD3Q6cH0kBfZOLWcpxAWVJwjYX7Rd1Ll-0O6oa4-mcT1DpVUFOQrexdGauapeVi-1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f6325ec27.mp4?token=vrJvFBUwb3YXbC0qUlSgfuEWINSNJ-jtAdZDxDfAmWkMfPbN6iDeNfXgPXEY-a9ANAqjTysoCJZdzmsqJnd37tRudc290eY1Urw9iHM6wHOaebroPu7DuKXYcnxRNYJ6V0DtLu3JD5qbd1ulE2MOVbp2czjITPM0weJDOlqiQm6uN-d4XLzIh5rfqzzfdkET2Ykfdb5bXbizP9-ev18CY7F_M51NvBzpaML8nBnrN4ErTOwxe2OKU5MJ6mfRUZqlRhpVArBeAQ9YwU2hYmsPqD3Q6cH0kBfZOLWcpxAWVJwjYX7Rd1Ll-0O6oa4-mcT1DpVUFOQrexdGauapeVi-1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی‌ساعاتی‌پیش لیونل‌مسی در شب باخت‌ مجدد تیمش اینترمیامی مقابل تورنتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104425" target="_blank">📅 09:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104424">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/995ef211fc.mp4?token=BMFWZjObKZ4u0FzSgFxnThgae7_G2lwNMLepqCVvp9PAAyg9eB8QeCaI3MRmj9UD8z13e9ou8I--mWIsWDTPNf2jJCpTw7efZavn3btoHWGd0-HPPcXI2qME4qJ50iouX22kLKCswNkCFJlywOwGX4AUCKm7ZD0fCXtayuvZhcj4tT9zRE17I7R_MSisMSP7qFG43aEQQ_PlXC7jo9xIid_1LNZm4rh1qfvNSQbFsn_O_wauVeJ_DkFVY2bIkuUaL3cLshhdsVHRGdyGZNZvvFa0Q3hMGBfCCqIdu0_HT6BDN1QTEiZZqoSXeysDHNaG9eNKXbKELm6NuQ1oPocUlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/995ef211fc.mp4?token=BMFWZjObKZ4u0FzSgFxnThgae7_G2lwNMLepqCVvp9PAAyg9eB8QeCaI3MRmj9UD8z13e9ou8I--mWIsWDTPNf2jJCpTw7efZavn3btoHWGd0-HPPcXI2qME4qJ50iouX22kLKCswNkCFJlywOwGX4AUCKm7ZD0fCXtayuvZhcj4tT9zRE17I7R_MSisMSP7qFG43aEQQ_PlXC7jo9xIid_1LNZm4rh1qfvNSQbFsn_O_wauVeJ_DkFVY2bIkuUaL3cLshhdsVHRGdyGZNZvvFa0Q3hMGBfCCqIdu0_HT6BDN1QTEiZZqoSXeysDHNaG9eNKXbKELm6NuQ1oPocUlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
جنجال‌علیرضا کوشکی مقابل نساجی که باعث نیمکت‌نشین شدنش جلو سپاهان شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104424" target="_blank">📅 09:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104423">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
‼️
⚠️
رئیس مجلس عراق: قالیباف توی جلسه گفت خلیج فارس منم حرفشو قطع کردم گفتم خلیج عربی درسته، دوباره این کارو تکرار کرد و منم دوباره گفتم خلیج عربی درسته. قالیباف در واکنش بهم گفت مشکلی نیست شما اسم خودتونو دارید ماهم اسم خودمونو!
رئیس جمهور عراق هم گفت چطوره بگیم خلیج اسلامی که مشکلی بینمون پیش نیاد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/104423" target="_blank">📅 02:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104422">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qj8LtqIlxWHTPo4X178LPktTRNEUujg-4QkQmTmWgM4YBKle9wpVtWViuIGHN2chWIFn9tCg4Z_RazwQhxxjs8x4GdSGLPlcmZbaUuPLigTo8i1gbsjALnOy8qQds0mRuPeANCz2lxUzDGCnK0bTr9fg4dD1O67VcGW40d9q-onMCO3e8DiraQC1VxgqjJnEOCCzPuNTF1iIoED8Z0G5_qfQZvnV6ypC7Z62XW9MViu6TRywp8lh9WsJ_1hEJmZ-V0rffB80tViE_pQetW77-rk0fW2xGqbs7_pn3mCPa1pGS0Py-T9PZ-am2rWsazvTpLPFprUwmwwuge_93DyiGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیونل‌مسی در ترکیب اینترمیامی مقابل تورنتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/104422" target="_blank">📅 02:18 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
