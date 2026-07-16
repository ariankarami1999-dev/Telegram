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
<img src="https://cdn4.telesco.pe/file/ETp76c6biJqfO4-WKWsg4UcrPlENKBpSujwTBGKHzVoQrvcAYFqozNcLeLmJbkKEnmR60IOEEASsiuCnAc8ZDjCUz8XBbNoY88rNAQi5IQ3HqW_s0sB7BGlMN30ibF5whCieic5sQ8aDmcVeZAi1tmxqb3Jee3199BPGVmFQqpq4YUq8oPU-g7M92ki-cONUWbnE1eZfqIbnXoioNeRH0bVbIlBxglp9RfYoEkx6zVuLD3hWkEIWRw2WLf9FNGhO0kWv0q0arbS6kPyQdOlyrv8RppdGLfCPQLUAvrU7FkHXWzddfodyZl0sR7vHVBHiDilCLabArTzdLU708NqU0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 942K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 18:00:25</div>
<hr>

<div class="tg-post" id="msg-134751">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01eccbfb3c.mp4?token=fLLmzB771qpEThGFNbTQVG3sqrXcsex0J1UD_iO0m41X9kzzAN2CVHd_WwkV_X9hGLOKBjAfK4nh-SZSsfah3x_LYEyLjClPtoSu0FhHHwCOTs1wDFmpmhJcoFvUCnbmCGghEWFJsKVmd4V6A4onbmHMXAsjLwv3Pr7MnaBOXpowu0dufiAVhm3qN7TSYi0VZcNTZ8mIPB1vAycjsOT89Gl6U6ZNxnZ64N31KY7M9LpjJ-5NIH_fwFl7sbmpoLyda7ijDVTAaJCtR-3L-qkx6CUM-LCPr5lRt8tqZR1A1LfPwaxjiUHh6XFhN9XsDYR0qKCELwD_qeJGFyKg4M0qow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01eccbfb3c.mp4?token=fLLmzB771qpEThGFNbTQVG3sqrXcsex0J1UD_iO0m41X9kzzAN2CVHd_WwkV_X9hGLOKBjAfK4nh-SZSsfah3x_LYEyLjClPtoSu0FhHHwCOTs1wDFmpmhJcoFvUCnbmCGghEWFJsKVmd4V6A4onbmHMXAsjLwv3Pr7MnaBOXpowu0dufiAVhm3qN7TSYi0VZcNTZ8mIPB1vAycjsOT89Gl6U6ZNxnZ64N31KY7M9LpjJ-5NIH_fwFl7sbmpoLyda7ijDVTAaJCtR-3L-qkx6CUM-LCPr5lRt8tqZR1A1LfPwaxjiUHh6XFhN9XsDYR0qKCELwD_qeJGFyKg4M0qow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امید محدث؛ کارشناس مسایل سیاسی : مذاکره بخشی از جنگ و ادامه آن است
🔴
دیپلمات فردی عافیت طلب و محافظه کار نیست؛ بلکه سرباز جنگ است؛
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/134751" target="_blank">📅 18:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134750">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری / رویترز: نیروهای پاکستانی در عربستان در حال آماده‌سازی برای اعزام برای جنگ با حوثی‌ها هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/134750" target="_blank">📅 17:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134748">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/916cff4f6a.mp4?token=ORJNuLfLO70pVNLVE8dx9otMOjHG5bOXCl9WgQ7bkXzRnDhynCPpYczbpe8BDOOKBFSUJCYfM6HostjCqrD8UDeylsm3e_-2aXPRkJ2TA0UG5VcLldQlSRttbf0x3SZg8Ie4yWjzE3DoMVd7MOJ0hbT8V7deP8-hHiAGTL6AQFyH1ItlcFAD5h5t9OQOR35frD2nAAMhLpfkLTpoXgi1ig4g_gCgOqu3hJknKQcNwLDJ0am1fv5DXc4oa4Re9NKM1MJ838yMJlth7sGc1iBNE6RCE5zxiZhkSu_D_VWQgkBCOmjMu-bwjsv49CoOWBzug0vfJISr_3xMK_fyqxiwQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/916cff4f6a.mp4?token=ORJNuLfLO70pVNLVE8dx9otMOjHG5bOXCl9WgQ7bkXzRnDhynCPpYczbpe8BDOOKBFSUJCYfM6HostjCqrD8UDeylsm3e_-2aXPRkJ2TA0UG5VcLldQlSRttbf0x3SZg8Ie4yWjzE3DoMVd7MOJ0hbT8V7deP8-hHiAGTL6AQFyH1ItlcFAD5h5t9OQOR35frD2nAAMhLpfkLTpoXgi1ig4g_gCgOqu3hJknKQcNwLDJ0am1fv5DXc4oa4Re9NKM1MJ838yMJlth7sGc1iBNE6RCE5zxiZhkSu_D_VWQgkBCOmjMu-bwjsv49CoOWBzug0vfJISr_3xMK_fyqxiwQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراضات شدید در کیف پایتخت اوکراین
🔴
معترضین خواهان استعفای وزیر جنگ اوکراین هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/134748" target="_blank">📅 17:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134747">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef7072e45c.mp4?token=K-oKyn7jBXA2Qe3l-L-03L6itap7qh8WDnUtgA1_zoHZZ-zWRxM05Gp_E9wesdkARzenHkYUFAZhsfHi-yPxg2isTo-yndHtpeaYAilRaVVP_Ahv-wO5svVJvGIs3ayrhNUL3lSIspfwd1P8Xii88sSMXcTl-rAgKiEnKLs9IHWyL7b7gyw3-XdYv4qEK4PcEBWEbTTknyFuTNFWKqUWJXGRxFQpaTjiM97Ste1EdFr9nF39M6g10engaP3dXRoIbvfSNw6UHH983uyTPioHOwgWBmTEJh-80A3STC_8C7CEQPvWUlWFdzzwERmhHyaabRVhKrmghIIcD8-6y_jliQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef7072e45c.mp4?token=K-oKyn7jBXA2Qe3l-L-03L6itap7qh8WDnUtgA1_zoHZZ-zWRxM05Gp_E9wesdkARzenHkYUFAZhsfHi-yPxg2isTo-yndHtpeaYAilRaVVP_Ahv-wO5svVJvGIs3ayrhNUL3lSIspfwd1P8Xii88sSMXcTl-rAgKiEnKLs9IHWyL7b7gyw3-XdYv4qEK4PcEBWEbTTknyFuTNFWKqUWJXGRxFQpaTjiM97Ste1EdFr9nF39M6g10engaP3dXRoIbvfSNw6UHH983uyTPioHOwgWBmTEJh-80A3STC_8C7CEQPvWUlWFdzzwERmhHyaabRVhKrmghIIcD8-6y_jliQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستار هدایت خواه، نماینده مجلس هستن که توی تجمات شبانه کلاه خودشو در آورده گفته هر کی پول و طلا داره بزاره توی این تا یه نفر رو اجیر کنم بره ترامپ رو بکشه...
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/134747" target="_blank">📅 17:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134746">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyQfwH_82SwTTXhjqceWkzH8V2TxUNUF2FDLC00ajO5r77ykJtsx7AbC2Oulukk1oMBlRC8LX-Mg6-kak-vDG7kiWvI4cocWmP3SbbFfcm0r3YkBQzamc5jOM7qW9WmUW9WZ2fZmQfOun_4vv7rFfqa5hlcN8F5xAef6d5f0NmjJ6fuzK9MMcyfBTStoVWLqRcnmQDh8pqyi7UDrRIBUJ6tPOkt6lVb1UaMvCaMYhv-c4kwB9D7hrYJr3wR72YYbNBEIt13MHClgqNdrwR5NVZGMYVOoA_5EeeP-XgeS0JsdXE5OnVGtcaGo9QvsRWdYZmjnZ9SUfynNNE6fN_kzoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: من جانباز هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/134746" target="_blank">📅 17:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134745">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
رهبر انصارالله یمن: عربستان باید مجازات شود
🔴
نقش عربستان در همکاری با آمریکا، اسرائیل و بریتانیا برای ضربه زدن به هرگونه موضع واحد و یکپارچه امت، اکنون کاملاً آشکار و شناخته‌شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/134745" target="_blank">📅 17:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134744">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e83aff651.mp4?token=n0-TqG4sHHbRYjvyNCkai6mateBy0qTnBYdSDAEP33GEfjHjKLfHETb5AteIHgffDckydI50wDp4ylGxscW_gHjPByiFsObnnAW2ixuR4nwqTlkbVTt98HRKxodV0j_GHOAah2aLsYuy10ZGvPLUYhCMHeGDPXMPwnqrLdZegXr3PmoFpXgr6PXZ_H-KjK9p8SfWiVaIoETjRzD3GNBTwLaC88X4vNuVagYby8DnhqiSrTE76uiB99ry2AoXlDmEbczj1kc2-efstJT2P3VK8DCsU3BOQR-bu6bj2XYKyxxDl5gqAQ9Z_oGJGhTpUQdqXsljjbqcDK0fCM69Veyzqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e83aff651.mp4?token=n0-TqG4sHHbRYjvyNCkai6mateBy0qTnBYdSDAEP33GEfjHjKLfHETb5AteIHgffDckydI50wDp4ylGxscW_gHjPByiFsObnnAW2ixuR4nwqTlkbVTt98HRKxodV0j_GHOAah2aLsYuy10ZGvPLUYhCMHeGDPXMPwnqrLdZegXr3PmoFpXgr6PXZ_H-KjK9p8SfWiVaIoETjRzD3GNBTwLaC88X4vNuVagYby8DnhqiSrTE76uiB99ry2AoXlDmEbczj1kc2-efstJT2P3VK8DCsU3BOQR-bu6bj2XYKyxxDl5gqAQ9Z_oGJGhTpUQdqXsljjbqcDK0fCM69Veyzqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مصاحبه با فاکس نیوز:
اگر ایران به بازدارندگی اتمی برسد ، مجبوریم آنها را با احترام آقا (سِر) خطاب کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/134744" target="_blank">📅 17:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134743">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbc5724b26.mp4?token=h0RGucemy-sZaPBsfakgco4Mf4nOsJLBFm-gnua-YTTv3FLIaOz6CBlbCS5qAsOaeZ8CX106Mu4Mb8kwilKC17h35KafXWmuzdG2wzKHfbLFwGx9jmQn-27MIR7p6968uCHXWdgVUn0Kw6EmM13EwVRgJgGpGOd7ZiFCML8XWzeqXS-53925KA3GndIs8h8SwCFqXu-B3yxdPwjh_tHkNvG_ZsvvYe-knbokko3mpUBR9YITFGXwXLLJXj8pzJTDoa6cY851BWCvfoRpwQcINbCiz19CfOnzi8s87hrGRvV8Dc40cjppybdZmeJTuYUrW-E_NSFWQjd7DQ2Uab2PXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbc5724b26.mp4?token=h0RGucemy-sZaPBsfakgco4Mf4nOsJLBFm-gnua-YTTv3FLIaOz6CBlbCS5qAsOaeZ8CX106Mu4Mb8kwilKC17h35KafXWmuzdG2wzKHfbLFwGx9jmQn-27MIR7p6968uCHXWdgVUn0Kw6EmM13EwVRgJgGpGOd7ZiFCML8XWzeqXS-53925KA3GndIs8h8SwCFqXu-B3yxdPwjh_tHkNvG_ZsvvYe-knbokko3mpUBR9YITFGXwXLLJXj8pzJTDoa6cY851BWCvfoRpwQcINbCiz19CfOnzi8s87hrGRvV8Dc40cjppybdZmeJTuYUrW-E_NSFWQjd7DQ2Uab2PXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لاشه پهپاد MQ۹ ‌آمریکایی در دهلران‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/134743" target="_blank">📅 17:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134742">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cc16d12e.mp4?token=Pi1jA6D6jB68K11HxKIepicDD-SszP4u6H3Nh4mNKEfD9jV4TuDXUANQw2cFAQXzQi4ZeeuSidMiPg1KpStwPMABf-lp9xqwg0NqII5a0Leij3lLGKeeqJgBSvaklijm-poM18GMlojXOkWFi6j5sm7nEwszlTdS4658BJDUP90B6-O3C69XGPSwcW5ocv-UrpN4XbM3U1b705Y8qM7vXFPjpwVzIxQaU1lQmGqrHzvLKoTUMCVoFyW18iG1taXDx7KDlna3H-pDn0eK3sF10cLv5SA_Z9X6a1DQ8SOjPsfA2J_AGxg7AELTmj1PhkJP4GU_PSZRtxVUM_6aMzZ13A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cc16d12e.mp4?token=Pi1jA6D6jB68K11HxKIepicDD-SszP4u6H3Nh4mNKEfD9jV4TuDXUANQw2cFAQXzQi4ZeeuSidMiPg1KpStwPMABf-lp9xqwg0NqII5a0Leij3lLGKeeqJgBSvaklijm-poM18GMlojXOkWFi6j5sm7nEwszlTdS4658BJDUP90B6-O3C69XGPSwcW5ocv-UrpN4XbM3U1b705Y8qM7vXFPjpwVzIxQaU1lQmGqrHzvLKoTUMCVoFyW18iG1taXDx7KDlna3H-pDn0eK3sF10cLv5SA_Z9X6a1DQ8SOjPsfA2J_AGxg7AELTmj1PhkJP4GU_PSZRtxVUM_6aMzZ13A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در میدان مرکزی میوه و تره‌بار کرج و اعتراض کسبه به مدیران
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/134742" target="_blank">📅 17:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134741">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه:
در ایالات متحده، سهم حملات و توطئه‌های تروریستی چپ‌گرا به سطوحی رسیده است که در دهه‌های گذشته مشاهده نشده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/134741" target="_blank">📅 17:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134740">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
مشاهده دود در منطقه ۲۲ تهران مربوط به آتش‌ زدن ضایعات بوده
🔴
سخنگوی سازمان آتش‌نشانی تهران:
منشأ دود مشاهده شده در منطقه ۲۲ مربوط به آتش زدن ضایعات در یکی از کارخانجات تولیدی اطراف تهران بوده است.
🔴
این حادثه هیچ ارتباطی با شرکت مینو نداشته است.
🔴
مشکل خاصی در محل وجود نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/134740" target="_blank">📅 17:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134739">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPwSSHoCsJkzVc485PXXghHq9oy7uvV48OSUifsCGY8OoHOhbXE2-viTXTNQN_4qIrYqHtvBj8ka5fB3Lw7y_Oe8Q_rakr_yuN45R506tvKczJ6MGKfHzQd0_4x9xw-VLlngbUW8tw9ka3-8cwJZFRJYQbOS7yfWUyMe62-uKI0ZcH5_8-BC-h-qm0QYkvSL8eAKIeJGMj3P2vSRSbofHmOaUU6msvFwzN4MvAf8DppQnVDQ8Z_TBOOSl3pzDEWeeR8SyhXHz-6fEfPoGEg6ghJwdS-E7XLZdLFXs__37Z1qSj-QHkPBsAW5F66Q1sEMFXR7M6CYUw5IuqzRiAUPUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که ایران به هتل کراون پلازا در شهر دوقم عمان حمله کرده است
🔴
این هتل محل اقامت نیروهای آمریکایی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/134739" target="_blank">📅 16:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134738">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1XmPBs6DNW8cH4jGLZJL0kQlSWCGg-rA-iTi1xFi0aqzcIeehg5wkvbNflvOUcsbNMhSVZmdd0nhuuro7d5FPb-HBcQJm8LY3BO-5iPy-X6LrXGTDmnJlFE3sShOrXAeQZ4IydAzfSwQjlE-nFAgkoGuUKhHZzldSLK1RIQ0rzSFw6mzB-UaTlUqi1qFgp_rlZg6hDjiqnj6atXM3HiuQ0zkhKI256aMetSklu0PdmPoGvDGuD7wW09Y7Xv8Mp_pVzbHNnh3ldhcoYp9w3CEVMKJDsmsMx2RgKgvz6nfN9JuvDhHeB8h2lvr9iqESQrxwBsQ8U4sfSIOSCigxPt6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: تصمیم مهمی در تهران اتخاذ شده است؛ اگر حکومت جولانی بنا به درخواست ترامپ و فشار آمریکا دست به اقدام علیه حزب‌الله بزند، با حملات موشکی و پهپادی مستقیم ایران مواجه خواهد شد. این هشدار به جولانی داده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/134738" target="_blank">📅 16:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134737">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVpzwx7ZLUGFaNJCscAbm_aM9sK0EeTBa4kxqyi_fntHFph8Fb_DGR7xeLMy32V6E_eRfn4J6_GCj-yomQZi0gQCct8cib3rYBVkQ-LjIgkyCaEa2zPrnbFjbKmj9VDvdzJCJSqCgF0LMohw-xyTvI6LF59zqUj7ZKyT91k8T3JCIZWQdmJ-9I_fvhNUTMcW2gJa8d7LHXwhyl5VQUYo0b4fo1fxOnQJBp-SiFYGS8KNm9q_cQN1FJIgaumUvA7IkcL2kTKqvZqVMxfo6NSfyPGNy2L-404wb8FJAOBjtEP0hLFAC6j1IabLRZJ9jxkeOJVJyWvKS6h1SwYizdNL6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسارت حمله دیشب آمریکا به فرودگاه سمنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/134737" target="_blank">📅 16:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134736">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLj5MV55fCYO8TTIody9DFqzCp-KoQVXg8ixyD6iMHYBuBs5TEhlXe06CLjn-wOzepyrp3y5_IUy_klQWyzJH0Sp4j0Z3DUsaq6B_vvii6w4Z1-zBoobEQbgAsDKxLV8GeZui2JobILp6uZS5LURkox_rTjAKad8nIniK4k1uOdDSbWu7_BRPmVHhEWPl05qqP4g_NZQWpQBC6_-n70NFB93YBxRC2cjo4OiYEw89RQtN70xUsOC_E_bw9u9co3NFjkTX9USsq1ZSkitqvDH8PmLfsfKv5gFk2VSgvRrBlsBSyftn3gn3lEETKY71XYowOPx1noKQsk4wJKxUsm6rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز
:
مذاکره‌کننده ارشد ایران گفت راه دیپلماسی همچنان باز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/134736" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134735">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlBe20rR1iI6ubqWVmlH71WenoFVaiNOEyndyMZlgKKzesu23kgWoSS5bSv5BUYSE2WaxYtPqER0tzM5kzzd-HSu9Su7ciPgYyqzjnPphVTpxY1cthj0aLDDfbR9Ws864OZAQZhEpsM1Q7zl9kGsrJ7B0-gQV9A70tYGP5o3pGBEfEmuKSCUb34_GPNaLq4bsCZnDz5VmmVKLMf1ZMNid2PFdKiF0xq7N9SWMEdOYTjcsJj8H2Qzux9tYEugn5yFnjiBFsvNBJGNU5aI_J-8pvjIhBe2VBYUcjmV6lR-IyfE9i-P_sxw_Kb8bpw0CsAeldLLOtDQYKemq671-NDgnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین وضعیت قیمت نفت
🔴
با از سرگیری درگیری نظامی ایران و آمریکا، قیمت نفت هم به وضعیت صعودی خود بازگشت. شنیده شدن اخباری مبنی بر احتمال بسته شدن تنگه باب‌المندب از سوی حوثی‌های یمن نیز بر نوسانات این بازار تاثیر می‌گذارد.
🔴
در حال حاضر نفت تکزاس ۸۰.۴۱، نفت برنت (معیار قیمت جهانی) ۸۵.۶۹ و نفت امارات ۷۸.۹۹ دلار در هر بشکه قیمت خورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/134735" target="_blank">📅 16:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134734">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
هند خواستار پایان حضور دریانوردان خود در تنگه هرمز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134734" target="_blank">📅 16:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134733">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری / گزارش ها از چند انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/134733" target="_blank">📅 16:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134732">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رویترز: شرکت‌های حمل و نقل دیگر به اسکورت‌های نظامی ایالات متحده در تنگه هرمز اعتماد ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/134732" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134731">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7129ac30e.mp4?token=sdKAd3GFfRuR3ulb-MNgnjWFNZHH29MFAdAkedojY6Go9z03cGgCgOPF3o4_3dyVQq-JSA-IL2vY-mTYe7PmnC1T6kBLHwOnyLbZYIVjbD_bx8PMGxXmR6SUkykzE4mjd0QLAJu_-jcZT0D_ZQTZvt--qFS2m2cCrXbr6vUl_Dpu4iJAojmJme2TOVyX5eE4emSwzgKBJJ1rk82_OoSaaZK_nA8BhH8G_o2CJvvqaq3OYsGZphWJD8kxq-Sgbw5b1T362rPyTDGf7eOfmyoSQGGeMqTWTHZ1-7-ScuM-X_Ck57dBcoHWftNVUDwqVLt3DFnfH17s6x1nmnhBdWByJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7129ac30e.mp4?token=sdKAd3GFfRuR3ulb-MNgnjWFNZHH29MFAdAkedojY6Go9z03cGgCgOPF3o4_3dyVQq-JSA-IL2vY-mTYe7PmnC1T6kBLHwOnyLbZYIVjbD_bx8PMGxXmR6SUkykzE4mjd0QLAJu_-jcZT0D_ZQTZvt--qFS2m2cCrXbr6vUl_Dpu4iJAojmJme2TOVyX5eE4emSwzgKBJJ1rk82_OoSaaZK_nA8BhH8G_o2CJvvqaq3OYsGZphWJD8kxq-Sgbw5b1T362rPyTDGf7eOfmyoSQGGeMqTWTHZ1-7-ScuM-X_Ck57dBcoHWftNVUDwqVLt3DFnfH17s6x1nmnhBdWByJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویس کرمی، مدیرعامل شرکت ملی پخش فرآورده‌های نفتی ایران: نصف ظرفیت پالایشگاه لاوان در حمله دشمن آمریکایی - اسرائیلی از دست رفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/134731" target="_blank">📅 16:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134730">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5MkzPaTR3pA_dLs6BCvEvPms3Ak-RKDaCUQXlsc1jnwvOCcbP3FV5ipDCmfxQIFAv8hVO5Kozb1pxHFWoGTxYprPAh5569J9BHZznjT4lolBsMh8ijvGN8Iy_ZrlujL221QIVJl409-GnRyat7-DAYxctOIsk5mH1uXPeI1Sf78PRVweoZhG8mF6duId32EgyHo1b4CQhfCPVwJ7AAYpfIwqKIdOKldvFQtxRYEZEsSi8lhIxB3KNWLvZQiKSweKCmFggff4o9tPBLBqVsCR3mIPaIP-tZ8mxGbqRRvqsxJGOdIZ9Huws-koKbA1LhmyHJGlANbd4H-GwgLjS5cJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جدید محصولات سایپا اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/134730" target="_blank">📅 16:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134729">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سخنگوی ارتش: آسیب به توان موشکی و پهپادی ما در حدی نبوده که عملیات‌های ارتش رو مختل کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/134729" target="_blank">📅 16:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134728">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری / آژیر خطر در داخل سفارت آمریکا در بغداد شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/134728" target="_blank">📅 16:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134727">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وال‌استریت ژورنال: ترامپ شامگاه سه‌شنبه نشستی برگزار کرد تا درباره احتمال اشغال جزیره خارگ یا بمباران کوه کلنگ گفت‌وگو کند.
🔴
ترامپ در مورد اعزام نیروهای زمینی تردید دارد؛ او بارها از بزرگ‌ترین تهدیدهای خود عقب‌نشینی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134727" target="_blank">📅 15:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134726">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
کانال 12 عبری: دیشب، ایالات متحده و ایران با یکدیگر تبادل آتش کردند. آمریکا به هدف قرار دادن اهداف در منطقه ساحلی ادامه داد، اما برای اولین بار، اهدافی را در مناطق پایتخت یعنی تهران مورد حمله قرار داد. ایران نیز موشک‌هایی را به سمت کویت، بحرین و اردن شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134726" target="_blank">📅 15:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134725">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm4z7NTt7kQ03tQxqgnw_7wEKMmEhSKqbBkHsyhUybKghmnD_vu9JTVk_KmTPFuColomjZvk0VOkHYZYWGhOb2oANgp0ow_Y6f3h5eOUMrPbrIyuRHazEZsbapV-PHWFkqwFZk8-0b9r_D0OCv5hE2S5hSMBDA58aFObfj2RfQ0M-gGEdLVkMZsYkDv9pwds1yLtNBvYmkt3U0kwDfoKjp4nvdkC-HDn1u_UKaC4T2x_lyoKk68exvqNtx0Wr4L_FpXkKnBEbSGb5AMhNuW7-Qsc0ANPXUhQCrEij8B62MjOfFEDYWXx0A7fDtTauW9sXejNYAPy2pwlRtt33Ml8hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گریگوری برو: عرضه فراوان نفت در ایام منتهی شروع درگیری اخیر باعث شده قیمت نفت فعلا بالا نرود
🔴
قیمت فعلی نفت با وجود حملات زیر ۸۵ دلار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134725" target="_blank">📅 15:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134724">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
منابع عبری خبر از گفتگوی تلفنی بین وزیر دفاع آمریکا و وزیر امنیت اسرائیل در مورد جنگ با ایران میدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134724" target="_blank">📅 15:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134723">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رویترز به نقل از منابع: حوثی‌ها اعلام کرده‌اند که در صورت هدف قرار گرفتن شبکه برق ایران، تنگه باب‌المندب را مسدود خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134723" target="_blank">📅 15:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134722">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
کپلر: ۱۳ کشتی روز گذشته از تنگه هرمز عبور کردند و تنها یک مورد از مسیر عمانی استفاده کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134722" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134721">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kM916EH3FkwU1bHIbUvC31AvRnanVfuiTunRQVzCXAgvCmVVuTOhjUwa_jZreJMtHpfts9kmi-t_RyNzOjNTDF3Yh_SSkX4s-XLGmTz_nlCpxbnqhmtoLzm67wdIYA9mxNzH1Ba1zs22Bxj-DCIwVqfzQ0QZF-D4WW7o7BopQFD647yOVO-WFajpDlZ6WFXoIhVpi2WqKtjIDVFuxMfArBa1J9L_4E737_huF4jIfcvZi-RMaQ_XSbCijAcqrqJH1t413wP6TokdkSNKS-haZRI_TNyVQ6CUTJItkJyxwkNCWNyg94r6tE5slEXab7yluuii9MlkEhbeF8vj0g4JyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نگاهی به آرایش ناوگان آمریکا در محاصره دریایی ایران؛ هر چهار ناو لینکلن، بوش، باکسر و تریپولی در منطقه حضور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134721" target="_blank">📅 15:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134720">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: در حالی که اسرائیل در حملات آمریکا به ایران شرکت نمی‌کند و به آتش‌بس در لبنان پایبند است، نوار غزه همچنان مهم‌ترین منطقه برای عملیات‌های ارتش اسرائیل است.
🔴
در غزه، ارتش اسرائیل دامنه عملیات خود را گسترش داده و در ماه‌های اخیر، حملات خود را با شدت بیشتری انجام می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/134720" target="_blank">📅 15:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134719">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ثابتی و رسایی رو باید بست به سرجنگی موشک و زد به پایگاه ناوگان پنجم تو بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134719" target="_blank">📅 15:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134717">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_igszQqJR-US6nhPNImotEyklOemFV2XRx4WsZNyPUkWyo2ndT_1tJmStH7u_g7v9Y8b5xtE8b1nSAYExoAR5eE0WsvNxy8Lthsj847byuU8krPSmKmXLaVsBOt-3Hdvli2lnyIjpTlPJAt7ATN85TXxw_FyAPb6xsRWXukkW1uw_O1ChonV7ATsZMSzyDtTWfUsnFoj_a1CwXtg9q9zVscArnNdrGuVf_lK_Dfra2hBknwGlmG3BD1WWttg9lxol3sLdogynvR0B18hfbWM_73CsCDKjPV8JYO9nRSU6Ak6h5JDxrThMrf6wN2UpZi7VLyVh7U_2HvUrsHb58Tqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی منتقدان خودش رو ولگرد خوند و نوشت ۱۸ماه جبهه رفتم و الانم دوست دارم برم جنوب
🔴
بنده ادمین الونیوز جلوی 950هزار نفر اعلام میکنم، آقای رسایی ....... هستی اگه نری جنوب و زیر بمبارون ۱هفته زندگی نکنی
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134717" target="_blank">📅 15:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134716">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F56Yy5vKRSntxztfhe8V9XZYg-dmNh1nQtopADEMEuH4wto2KE4GVcjteHxIWnJg-9ELWq7iJTXfubVySU-JgHxb9jKu7nfknG5pdG9ei4f6nRl25CmXYfGyptZxoQu-bGLub9SjVMqrZIu-vHP6LMQNdUSBQzpQyho3me-kX5-_aqZ1cErxZzMyO85H9yjt7P-Ls9xL4V7-poNZCp0tZQY7K7imbSyKRyMsC5mpkYoLLLlalpMQRj2dhtnl_7-BtD1XxdA9360lP8r851qUTIpqJE6Trn3KpN-56yZoObCbqjnFE3YjWFSuTqTo0ahyVfqY-fFsJj0WJRl_jDrXig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی اکبر ولایتی: تنگه هرمز متعلق به ایران است و هیچ قدرتی در دنیا نمی‌تواند تنگه هرمز را از مالکیت ایران خارج کند
#بوتاکس
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134716" target="_blank">📅 15:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134715">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f854ed7d0c.mp4?token=Ctc17f_7S2USWITT7cHp4rIE44P7BOJ6BY0YLKlLXl6ekN9OImZBNSFgxbJBZvLzC-bVUKF6VEsUDU8hRUAn1eqmYKMWKfq_oUJQDg0uke8zhwPBt9sYFzSwVhXl5XaECG0i5aaFD-luiNF0goIhwNTFQJFM2-ZlwNISub3NciyQYE199s5Cl70e8SeSmKwrzYM0FhxhMytswKt5OEDLNNO9sKf6E07X10ryXePzkyeoeRSWRuMoONCMAxJkvkGaT5khZMg94NZeO1kilJUHGQKpCSLEPBen9JV0M__3s_IxC1J3f6WwlWUEtyKK7xBObLSyzoUgNDQLWaRk774xIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f854ed7d0c.mp4?token=Ctc17f_7S2USWITT7cHp4rIE44P7BOJ6BY0YLKlLXl6ekN9OImZBNSFgxbJBZvLzC-bVUKF6VEsUDU8hRUAn1eqmYKMWKfq_oUJQDg0uke8zhwPBt9sYFzSwVhXl5XaECG0i5aaFD-luiNF0goIhwNTFQJFM2-ZlwNISub3NciyQYE199s5Cl70e8SeSmKwrzYM0FhxhMytswKt5OEDLNNO9sKf6E07X10ryXePzkyeoeRSWRuMoONCMAxJkvkGaT5khZMg94NZeO1kilJUHGQKpCSLEPBen9JV0M__3s_IxC1J3f6WwlWUEtyKK7xBObLSyzoUgNDQLWaRk774xIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد انتحاری اماراتی در آسمان جنوب
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134715" target="_blank">📅 15:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134713">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJBUT1JDmOHR0dQ-YXGtHBq9-aqb3ojQmV1nkyM1aK7nvgiOMAFLw9uVQosy51tzOJbALTUVlzZaJMrUMOYe206ZMQRKeyxLkKHgTFFIk7AZVbVU4hJf6VJk8pLTfXDe4nK8p0OiMTxa20XWboBQ7M8nl04fGAcofQ8B84M5528yJi1cr884qyu22BwOKNtHJscFEQssu8zxnaqDMMeUPMUWsj3nM8OXLhdNDpbicvZkJ8iw-PRM8avxC_XXCrfN2oLE8qIWqMEAAhYY6TCRsd_fvoF_P5_4GcRqNdrhSoPNA5gklyJn8UNnssAH5k8L04Uf2utUkoiTkt4wAARvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/679fc2d852.mp4?token=X-LMwYx5-Ziuz4sxFefZxCm4au48bHxV4bZxPy3u7Vs0m6zF2lMJ1lBz9cT5Vhrn6XwuJqUZkWRtcbiN1t4b5qm91ToUwFP6iKYphw3P7lteSgxOPvwbZPAL7__opYqzV6-bRf-f9971J-I8x3fmTlSz3sEFZxmI4IA63SBPiLwz4sBPwf4T1ICq-oTqmzFGWqxjNwCDk3jGMUs7ypUb8mxhaVjoRKsZ7y-QqsENr2UdSTak0i_9wsCpmCCStE3nDrWsZEz6i0DD2qcVoUTT-N04JLkrAkZsYqEoLQ6OdgPX5yjvasPZ_PlbXxN6ehp6cop42U8Z4ZPqCUC10Ss3pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/679fc2d852.mp4?token=X-LMwYx5-Ziuz4sxFefZxCm4au48bHxV4bZxPy3u7Vs0m6zF2lMJ1lBz9cT5Vhrn6XwuJqUZkWRtcbiN1t4b5qm91ToUwFP6iKYphw3P7lteSgxOPvwbZPAL7__opYqzV6-bRf-f9971J-I8x3fmTlSz3sEFZxmI4IA63SBPiLwz4sBPwf4T1ICq-oTqmzFGWqxjNwCDk3jGMUs7ypUb8mxhaVjoRKsZ7y-QqsENr2UdSTak0i_9wsCpmCCStE3nDrWsZEz6i0DD2qcVoUTT-N04JLkrAkZsYqEoLQ6OdgPX5yjvasPZ_PlbXxN6ehp6cop42U8Z4ZPqCUC10Ss3pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون حملات جدید به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134713" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134712">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
جلیلی: مردم میگن حاضریم تمام کشور رو فدا کنیم اما انتقام بگیریم  #قرومدنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134712" target="_blank">📅 15:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134710">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFxI9UHkBTmpIaUOKKY3LLabv9zBorUwV7pX8nHC8dqNpUygFbBT0Yd3ctqTj6LBAV73LOou5vFIVEQ_iyAXcY78AfA1G39o6vH3MZIR6Ed3xV978j6XBVvzsk_3pdxqnO8ARP_Miy82LS_Ckyzct0rHodnOIMm7-TAwuaIeTffqHlUPrvexwfPz8VOFFmuWENBYS1wxpuZmLy-KbBHZHMN2WwR75a_Cn_UWgjxSZQcnCCg-KjzsfV3mwjC90ra86tIvUocXUW5E2Q_ATpHTbxrB8GlOBcdhCUOZQm_x_2_bRHwae7jt5KL1V49L-CKgc8uqg9H3wFT-2UesXIpbNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZDh3d7yrz8NA6SCSYIm8CS4s-OFD1N9NJg25FHE_G_v5jOC_1TwZVDOUJk2ekZiRKHu2tAbAm53p7og1XCPYGiab5LVA27QxI1wkW6DXsyZwcBSkd5bZBhoBt1FaLtJEDByw6pjuO37yjF6w-iDLQOSuL2jBZ_vE3MqHZYdhdpJI0_1pHV1FMuB8l4maQc0PiQlAsrHt9cw-1ud6IRCIGLtLPd5wFfqHS92VBY-iERIumv6SuVEMT8TV2eQX6wvhgpvfbq6UMjq-SNK9zvUWEkBeAeZF_dneSC4wGSjpA4Qujk0cPDATt16wwaks5MsxZU_Geie_sid19g9nE71Nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آتش‌سوزی در نزدیکی کارخانه مینو در منطقه ۲۲ تهران!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134710" target="_blank">📅 14:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134709">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ژیلا صادقی،مجری صدا و سیما: همه جای دنیا مشکل اقتصادی و قطعی برق هست،مردم بعضی کشورا تا روزی 6 ساعت برق ندارن، مردم ما ناشکرن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/134709" target="_blank">📅 14:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134708">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
بیت‌کوین امروز در محدوده ۶۴ هزار و ۲۸۵ دلار معامله شد و اتریوم نیز با رشد ۰.۶۸ درصدی به یک هزار و ۸۹۰ دلار رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134708" target="_blank">📅 14:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134707">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb22f7q9UP9f4G_shXzXwnoKHq1ewoAmGSfO8waJG-VLuA5A1MBBL9YWYxDuSUlxbd80DLWfS8psp1zH5Oy1VbabX1WKZ_N3t8NI1cUnAYZt0N_ISQhzMaR-7Q6KS-xJ-OR4O13f6uHZHhpenFqmKVLZCNmRVwxrH0TEp-S27G2ojdORQxepdAyvWZLaE_sbrx0UV1oDXlFza5gj96zJ3lp8NnjKLKc0vrzp92aGY6m-fEIKJXAJ5V2Q9CUBc2M-FKPyvFLzvHTWY1NZCrK4o6ragRkJDP9g_cKL-m6ePfMLjfXXmxKCzwPbTCSB-zphDr5HSNzBTf4lHQRJAfmqJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیلی: مردم میگن حاضریم تمام کشور رو فدا کنیم اما انتقام بگیریم
#قرومدنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134707" target="_blank">📅 14:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134706">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
صدای انفجار در آسمان کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134706" target="_blank">📅 14:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134705">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqbuFWd0_nlF9L3tecbH05Hi84DggT3DyWVdfm_TsJ90tkoJKqG4knKRW0t7Z7kJd3neZxPnD6n4nWihteF-IY4cC-BWzcmCr1dXeKMse-x10vVioRxFQE8hg2VNSzfN2Ds18CudAzYkkIFJQzG7Y9KmezxUVQkDVofxMWhRF-sl6hZP1pqozsZdAr-je5lVsvHMcNj_PXYwEz9PM5LiLtqY6VmwsTb4ZC3VRJNMRA9-iuOTnJESFwKW6Wrnw4IaqqQd_olXJx4c8sqT_YDr9JPeg_eEvSr5hscalRDu19STdFiwtOPP9V7tvRrwkx6Cwv_Ljs34tQZ8ZyObf8ZtlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / هم اکنون حمله پهپادی به کویت
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134705" target="_blank">📅 14:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134704">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزارت دفاع ترکیه اعلام کرد که سفر فرمانده نیروی دریایی این کشور به بندر لاذقیه سوریه در روز دوشنبه گذشته به منظور تقویت همکاری نظامی میان دو کشور و تلاش برای بازسازی ساختار نیروهای مسلح سوریه انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134704" target="_blank">📅 14:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134703">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
الجزیره: تردیدها درباره نقش پاکستان در میانجی‌گری میان ایران و آمریکا افزایش یافت
🔴
شبکه الجزیره در گزارشی به بررسی تشدید دوباره تنش‌ها میان ایران و آمریکا و آینده تلاش‌های دیپلماتیک برای مهار این بحران پرداخته و نوشته است که نقش پاکستان به‌عنوان میانجی میان دو کشور با چالش‌های جدی مواجه شده است.
🔴
بر اساس این گزارش، پاکستان که تنها چند هفته پیش توانسته بود زمینه تمدید آتش‌بس میان تهران و واشنگتن را فراهم کند، اکنون با فروپاشی تدریجی همان توافق روبه‌رو است. درگیری‌های اخیر نیز برای سومین بار آتش‌بسی را که در ۸ آوریل میان دو طرف برقرار شده بود، در معرض شکست قرار داده است.
🔴
الجزیره با اشاره به دیدگاه برخی کارشناسان می‌نویسد که پاکستان اگرچه توان ایجاد کانال‌های ارتباطی میان طرفین را دارد، اما از ابزارهای لازم برای تضمین اجرای توافق‌های حاصل از این میانجی‌گری برخوردار نیست.
🔴
در ادامه این گزارش تأکید شده است که سرنوشت بحران، بیش از آنکه به تلاش میانجی‌ها وابسته باشد، به تصمیم‌های ایران و آمریکا درباره تنگه هرمز گره خورده است؛ آبراهی راهبردی که همچنان در کانون یکی از حساس‌ترین و خطرناک‌ترین منازعات ژئوپلیتیکی سال ۲۰۲۶ قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134703" target="_blank">📅 14:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134702">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoiG2hHi0yh30PrlFJ2aG1BK6M9tNl0NcUzA0kMXIO-csXHnOn0GDiAFM_HY36jkUy6Uo2b4ao27qVgIBuadSB92BhwOgBTKk3vY109s3rsfo1NvGEdJ9UY-DtwtlX6xmF1Xi8acXrckLB7vRpQWfyyAqtDD2uYlNMbYKxdm_6b_hx8lqRM5WKxtu73EH6y8dwf4INKB8rlGHpE7IfT_UK4i-wn1ZmtJCsvk7FfP0htyOX394jLlffoQJ2VfO6WiSCqxH9jUrk9nVtMM2vUbSJWDSw-iS3Fr0NKUMgofBAZFBjOi1LTU8fhEHRUi0ekLG5YClMPlwsMEedCavETEWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار مرکز پژوهش‌های مجلس: نیمی از روستاها زیر خطر فقر می‌روند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134702" target="_blank">📅 14:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134701">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
کاخ کرملین (روسیه): با ایران تو تماس هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134701" target="_blank">📅 14:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134700">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
گزارش ها از اختلال در ایرانسل
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134700" target="_blank">📅 13:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134699">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHrYMRMsFsdXRKy1Wzw-OZ_PEv5Cy9b4cso46NHLXfcyK967VUVvZCZc5XKdXhMgGHnM0An_KJlPPBzuCVsWjGhG318JXUfQutirIvLYPENSwjqCyceJmBKQsatf5TpgWkQDZ8mBiNAlv8cVVM-SwEDrswwlVuiiSYS_VZ5CuHjGdVd37P3q6ATcUywcQjnaRsJtoslzUV8Z9KXR9ZT8Dr72oEk02AOfmJe_gogZdwkxQjGoOVqftC_xd5SaTcPYMqmRZVomjKc1YWq3kvMiIOTscV-WOGq5aZaicrWYePlfSvPNgQrMcXzgekh3T3nR7sL54sXLp0FOpPgiUf-AgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جدیدترین دیوارنگاره میدان ولیعصر با اشاره به مرگ سناتور لیندسی گراهام: نفر بعدی کیه
🔴
حروف D و T در متن بزرگ نوشته شدند که اول اسم و فامیل دونالد ترامپ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134699" target="_blank">📅 13:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134698">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ6Rz-47Fenx6zinbKI5u3L0flnEDlvh5GV4edNaDqpxz5CM4tkWaize0Pn2DzC_55-icf7ThTaYvddWvnr2bMoRDbtt37Fl-oiU9ncGq89J7GHwWXAvs4V7MWKvzQ0VRb0PYILxHHkYt_sxLIB-o2w21qyBM_yEMHnWGsXSVUs699vRUGiu6703eUyc5jtQep0q0-47HBPUYve5qzQragCj195U1hoPj4L4CVvHC1M6WAE3Y0ihraCsDG-EtpET3Uie6zVQ4SoIAE1Dyk3DJiTO3rQTbGKHe001GwXp-2ndAX4eUnrevAgbkuxWZd3hkJ0UqsB5xmiMVELS4nkJWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از احوالات روس ها در جنگ با اوکراین، نقشی سوخویی که برای فریب کشیده شده اما روی همان نقش هلیکوپتر میل گذاشتند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134698" target="_blank">📅 13:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134697">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سفارت ایران در لبنان: تنگه هرمز جز با «شرایط ایران» باز نخواهد شد.
🔴
ایالات متحده باید این واقعیت را درک کند. یا از طریق گفتگو یا با استفاده از قدرت نظامی ایران که آن را مجبور به رعایت «شرایط ایران» کند، راه دیگری وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134697" target="_blank">📅 13:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134696">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
کاظمی، وزیر آموزش و پرورش: برنامه آموزش و پرورش برای سال تحصیلی جدید، برگزاری حضوری و بازگشایی کامل مدارس است. به شایعات فضای مجازی دقت نکنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134696" target="_blank">📅 13:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134695">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu_Uk4SpOzu2xpZSt1oKmmpq_I3Z0X82e2LzpTDYecWRNG1ozP5CXRzzJVdDDJDQdzdpokhgv-ujxzDngeJcSBWJi7pKtORuU-AEgWtf2j8iDBYCzYfyL9S5CGYOasWAlrFSTEVOZU80jrij0cWaDH5VEgibm2P2LfJ35fE1rbhuHOzsYOQL-HKi8G1YVZRPfh1FyPpAbTlVOvbc5DMNIx30Y3QsRb-AOHObRwf4HUmWTdIsCSRb0KBhMKRqDEZZnklZuxb4H3bxON3P1J_bNzd5J0ACBau9FX7fqgJNPqY9yt8SXJNfkAuKAu0qJbj2pIHKKtfCSeeuzFzi0GVtlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: از لبنان، سوریه و غزه خارج نمی‌شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/134695" target="_blank">📅 13:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134694">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
الجزیره: پهپاد به نفتکش در آب‌های عراق اصابت کرد؛ صادرات نفت بصره موقتاً متوقف شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/134694" target="_blank">📅 13:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134693">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
رویترز به نقل از منابع امنیتی و نفتی عراق: یک نفتکش در بندر بصره مورد حمله پهپادی قرار گرفت، اما خسارتی به آن وارد نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134693" target="_blank">📅 13:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134692">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سخنگوی اتحادیه صادرکنندگان فرآورده‌های نفت، گاز و پتروشیمی ایران:  گفته می‌شود حدود ۸۰ میلیون بشکه نفت خام در این بازه زمانی(بعد از امضای تفاهم) به بازارهای جهانی تزریق شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/134692" target="_blank">📅 13:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134691">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIOYIc30wRSFuGomTqES322-LfuUCw5ppWRC5-AcshsLKgTTArDiSDCWTntGYiA70uLYL4vOMhaFYJpZey9n2oFEMFkRxgG9oivBzf4PXc83mjOTmSqL6Xl8xSIXshd14ofV2AjIBf_GG8PPL-tHojFr9fNfBKpsan2i0or6ECr015_crP6_hMuMImhZV5YfbleR4yeZe8xn1JOdfd_vWF00NUdtEKkkgI34Nfd6pRlS4wJBbbPKNHrzwgDyFOKrWxnSI9CrNYBvTYA2aJtyuEEQD3lxhzd3TguQq7jcU66VD7hG33a_OIIB8_UW7zFpuoi73_R6B3-lS9wHtUPBmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افتخار ایرانی‌ها
❤️
انتخابت رو به عنوان داور فینال جام جهانی تبریک میگیم و ایشالا خار بشه بره تو چشم لبنانی‌ها و عراقی‌های مقیم ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134691" target="_blank">📅 13:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134690">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
عربستان تعطیلی سه روزه فرودگاه بین‌المللی ابها را در پی حملات دوشنبه‌شب نیروهای مسلح یمن تمدید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134690" target="_blank">📅 13:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134689">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سازمان آتش‌نشانی مشهد: ظهر امروز در کارگاه قیر یکی از پروژه‌های حرم آتش‌سوزی رخ داد که این آتش‌سوری در مدت کوتاهی مهار شد؛ علت وقوع آتش‌سوزی در دست بررسی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134689" target="_blank">📅 13:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134688">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c1f3ede08.mp4?token=t7Fw0MdTc8P8zur4ULN9Furwe5yAcBDCeBGrkWNi3iMtdhk2g7AwOiPOkI42Gn4wgGHk8VNVouFuLYOeAWBG9s98lN2WIeh-dy9FmhGe_pPuPsXnNuMpHcjCkVAZT-xpDApEmfMz7A526N1-YqmoemB_dtI_hHvll7xoWvOvnHMJ3dyYE1-_9o_I8Pc_aN4h8PtppNd5h2E_bk89T-z-zxbWMbxDJnAs0aWXGSaq0nkVjXIFD8yTSGLouFc4MYwT_qXG8pUK0GhjdST2rYMWK1wXFWFsI4sVo_NSJYdtV73WM9wEQaIbE68n_coct05ycWwEp3CqKek5weTbJRXw8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c1f3ede08.mp4?token=t7Fw0MdTc8P8zur4ULN9Furwe5yAcBDCeBGrkWNi3iMtdhk2g7AwOiPOkI42Gn4wgGHk8VNVouFuLYOeAWBG9s98lN2WIeh-dy9FmhGe_pPuPsXnNuMpHcjCkVAZT-xpDApEmfMz7A526N1-YqmoemB_dtI_hHvll7xoWvOvnHMJ3dyYE1-_9o_I8Pc_aN4h8PtppNd5h2E_bk89T-z-zxbWMbxDJnAs0aWXGSaq0nkVjXIFD8yTSGLouFc4MYwT_qXG8pUK0GhjdST2rYMWK1wXFWFsI4sVo_NSJYdtV73WM9wEQaIbE68n_coct05ycWwEp3CqKek5weTbJRXw8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجلس نمایندگان آمریکا شب گذشته لایحه توقف کمک‌های سالانه ۳.۳ میلیارد دلاری آمریکا به اسرائیل را رد کرد.
🔴
نکته قابل توجه، رای مثبت 103 نماینده دموکرات به توقف کمک‌ها به اسرائیل بود. موضوعی که به هیچ وجه 10 سال قبل قابل تصور نبود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/134688" target="_blank">📅 13:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134687">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cnLHKmPdMiKYL_7H3n684gq0T9wC33pygTko7grbilPn7IL1huZ4CMDt4e3nEy0hYibZ0g0pIzA-xnvxXy2SV4nEm5C_tsKTwD8h7yEbRyP4pZIrHyrZSnJrrANVhqoiuhyNUq7hWQD_6Q6icZTGsPlvCNu8hjVUsUcu5_KyE-O1CPR7te8NqIWCn0fRQqa5FhWjjGlSlqWhX6xgLryDK7QU-4mdwMHD6wldiUGSqW_RNE3xo0kIzY09bBvPZMHtJOHSaIhfwTib5oXJRYCTBq9fHpi8zeyydr6XIZ2fI1CEwgcHfdel4f61W97I-mxYTKJ3WeVjp3kgsfGNbHjddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتشر شده از سنتکام، از حمله دیشب به یک دکل ارتباطی در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134687" target="_blank">📅 12:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134686">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gmf8mxgsDSctZA2RqN_eCDBdxfVoZHjt844UPT1knA2m0u_DAo3qbQVFao-2yj6pyDD1LbMP75ZUo_SRGOgrPoC5aYJsAOxlZFUbzoQPj-yQy711jFHcNJLSeLvLos11P7qC9RrfQ-ZsWhLDoZnDtcralAkiTn0QMBj7nNIIb1j7NUUBYNCF5TpXyHoej2VF9PZ4WOz-HVBch7Q7fQsMOusxODI7HZIugjxkweYPW4HB_jbeJy6gOkDEuKANCHw8f7Cj87FSobHpVQeGxjMEf1dbSbiCjKlxNOw_qMiMBCWYdLtMU_MQFKguqOqXeh9xGsuqume7VeWfgaENR38gmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز گزارش می‌دهد که شرکت‌های کشتیرانی پس از حملات اخیر ایران به کشتی‌های تجاری، به طور فزاینده‌ای از مسیر ترانزیتی تحت هدایت ارتش ایالات متحده از طریق تنگه هرمز اجتناب می‌کنند.
🔴
یک منبع کشتیرانی با اشاره به ایمنی خدمه و بدتر شدن فضای امنیتی گفت: «به نظر نمی‌رسد ایالات متحده هیچ کنترلی بر اوضاع داشته باشد.»
🔴
در حالی که واشنگتن مدعی است که تنگه همچنان باز است و بسیاری از کشتی‌ها با هماهنگی ایالات متحده به عبور خود ادامه می‌دهند، شرکت‌های امنیت دریایی هشدار می‌دهند که هیچ تضمین قابل اعتمادی برای عبور ایمن وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134686" target="_blank">📅 12:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134685">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوری / تلگراف: انصارالله یمن در حال آماده‌سازی برای بستن تنگه باب‌المندب است/حدود ۱۰ تا ۱۲ درصد از تجارت دریایی سالانه جهان از این تنگه عبور می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134685" target="_blank">📅 12:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134684">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری/ گزارشات از آتش سوزی در حرم امام رضا در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134684" target="_blank">📅 12:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134683">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G4EURejxIjzOYaF7cpNK-Rnu1wkyk4qe_-aO7O7-NWoy4zemr2417HDLpi7y9LM0RhjvaB8rY9TDvoMpsnnUZlNLvpB4x91KuOTxFjhyhJpMlPwnzdklILCC8JZ-ILiUuP0-7ab7l1lN3-LFtTjJpvFxJjUqbDiStPaTyhrD1tabQysFhmTjujbgxb2sJ6iWgwMMzpRGgUJY31WGBKUcU7HK8pc7aUj42OqHyy8DtR1ldmbxjgLtzGB2lpIMuODIS_pRY_qJqzCHwewfR2DZBVd0cSE2ENdaEKO_V8wOHRZT_s_Rfxp4u__A_gt4tcEM8TO8Ud5nTFSGp8nh2hcATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رفع ممنوعیت صادرات سوسیس اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134683" target="_blank">📅 12:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134682">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سوریه، با رهبری جدید خود، اعلام کرده است که یک عملیات قاچاق سلاح‌های پیشرفته و موشک‌ها را از طریق مرز سوریه و عراق به سمت مقاومت اسلامی حزب‌الله در لبنان، خنثی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134682" target="_blank">📅 12:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134681">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری/ گزارشات از آتش سوزی در حرم امام رضا در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134681" target="_blank">📅 12:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134678">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cugIunwc7RRVX24lUYlf80ZY5_HmhACJsUcTpzadolKn4Xz9D89fY3ty4M3lcix0YjHuY0iz5PfDEZDw29EY9IoIIZS2wyerSd_MKewmKNFBjSLvbul3YEaWwxGYicLml5XZkbsdnh8I2gGjJcJg3sXVsghR3yZaZdJBqe-qjNeiDfNIOZuiwbn48qT8Rx47VILgY0sX_RBP5zqo5cwP5HHnVe3ygGZffJKaTu94VNH2s5MzagVgb7RzKrYbK8f8LkwGEJdnI_OajImmOmNyPL55QgtpdQgbasAK0peAYhzK80CzvkwESYHzcHUdx3YDkckccKRQ4zleJix5eVKxug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJrfCZf0TTeZHc7zImiwp9t7enf6oOQmFL974S_yfWCFJJvmOG_WhJAk-n5ufrh9xE_GnR40_ZwQezzOer2oZG5RvTzdpI0xr2xhV1ivd0EgZ4uGuv9uoijpUkFg0vELFi9-OYnlfbLgWPIgdRkpvD46SCfHxJZAoxRoWs7EqFX2TRJPl61YclmH-dred35QQMvH0h_mbBOyTNFlIF9k0MYIAMwsdmqQEBazLB8kjAwJ4Gr_IpYL91JaQwzFxwAAezE66y7F4jXwDbqgMxfRNoBCF1FO7BRux3VClsrPmRdCxrjeLYwfGGehFCnRLk1wqmQG-qrsKFgEpgGGwDfJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-sorAwpArksghxLoKzm1hG5ENG1cf4Kaa_U2QyxYm8e-CHrqSiIoC7obBPZ9OQzMoW4qoujZPnTkamM7AsBQl-dNX7eknAQK9865WETrEHEAVjLQqHwm-6sqEhuillzxdDvLduSS9UaZa8iBt9URJM_tf7T3qUbgqnVdGYNrTO-abPwj5jSY6HAy4AGyV1NbCAIC3qyJx-8gbHZdcIZzDxFaL5qm0N6zbkYEhe22CA21JHs7nnpoWvASbt5Nkbr1AMIqHFh-vVaw0VwXVddE2w_uwxFiZaS67TfQSGAGS3Hvfpcx4GBX-Op-Eg03FuPPc2_5IECjKTI7vnx8kxGFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مشهد همین الان
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134678" target="_blank">📅 12:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134677">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsUHlnvCv2m4YSlvpV7J5jWiDma2v6RR4K9TizBYABbu9ONWULPYzeSJxBIE8-zOi5jgmqFRw6l9i30YQz7hSNEDq6P3hskTDqg1xoUrtHgFt8nLjAWseMhniGbII8D-KdSaFTLmcK3tP5n1DtfWh1Z0MVMmcYPkjSnG5-AIShhmxuoGkHhPVKL5l0KaDFL22gNgjBYvb94gbnDZSphH2eOA7gS6inGcCeh8upJhnuwIvLZ4d-Ey-7jNY6CkQGhdrjpebjx4N5J4q-NeoU38nfVnd0pJhQjWAkznFnJ7iXj91WW5DsYGyExUBvZCK4GerviFNHiDV_qStB2NVxnevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ گزارشات از آتش سوزی در حرم امام رضا در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/134677" target="_blank">📅 12:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134676">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
هاآرتص: ترامپ در حال بررسی عملیات زمینی آمریکا در ایران و حمله به سایت‌های انرژی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/134676" target="_blank">📅 12:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134675">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری / سفر نتانیاهو به آمریکا؛ به تعویق اوفتاد | مراسم سناتور گراهام هم به ماه بعد موکول شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134675" target="_blank">📅 12:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134674">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhBQXqPZOQ6iylv3EfSSMqJJD2eTGjWX9Bj3EUHThak7Dy7wQ3htrQuIBlRFC9BnxjZbUOGPoUj-wIBh2aPUlJSwOE8p3EuEwiyuA3CzYCIXLvxXKvPUwRWvbBmNfASuny1_buc6KhJ10npMjvMNygdG1I1S1Leo2yNon-JwPk0kBwYhY-vKe3Dr_8tiYqHk0TRLl_FVebTL5HuOsoC7_1AcCF5JR6VPxyriCVCdyd9OD7XK273ulrTdkV4GS3AxklyoJFxB5xH7Ng6sy0XI4oJG4EcsnUnyTzI8pM1hWgEIZxfz1YTWDWeD95c08bi7xeIvzEMTYZ8vZvnAPm2YlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش شبکه سی‌بی‌اس، انتظار می‌رود که دونالد ترامپ، رئیس‌جمهور آمریکا، در سخنرانی خود که شب پنجشنبه پخش خواهد شد، به اتهامات پیشین و گزارش‌نشده‌ای درباره دخالت چین در انتخابات، اشاره کند.
🔴
این ادعاها شامل این است که چین در طول انتخابات سال ۲۰۲۰، به اطلاعات مربوط به رای‌دهندگان آمریکایی دسترسی پیدا کرده است و اینکه سازمان سیا از این فعالیت‌ها مطلع بوده، اما در طول دوره اول ریاست‌جمهوری ترامپ، او را در جریان این موضوع قرار نداده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/134674" target="_blank">📅 12:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134673">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
الحدث: حملات دیشب آمریکا به مکان هایی نزدیک پایتخت ایران نشون دهنده گسترش عملیات و تغییر عملیات به اهداف جدید در شمال ایرانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134673" target="_blank">📅 11:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134672">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
خبرگزاری فرانسه: پاکستان از آمریکا و ایران خواسته است تا مذاکرات را از سر بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134672" target="_blank">📅 11:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134671">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPIAiXhaxT2JdlDZ_DQjBHzxTCIdHdeeqPPJyLAH7VYj599121e4GhMGWPSa4lPFpj_NaoXsYt9d4c-L1DMSQ81BBU9VHD85euPDQ99ej0yNx15n7RHUDJY_pVWIXVO_5tbKWaDryQ7tHEuCT7qWaC8pDnGf22jje89C8HVzefTTexNgakxI-raMj7xZ29Z94p4CInONaAcVUzxpHH-rldtiTkgth1xOqQibRKwuD1dLveRrraW_dezM-IMLI5XGTgLstjo1dHL_pwPuM2L6L8HPKm-0UgoduvgNSSfeqEy-3kUbEJ2mdh_igDYQ2opekV5xxhGny7pWHHVIQBWUtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد امضا کنندگان کارزار «درخواست حضور اعضای جبهه پایداری در مناطق جنگی در جنوب کشور» ۱۱۲ هزارتایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134671" target="_blank">📅 11:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134670">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de798daa31.mp4?token=tXnwn6_gEz-7Xm4Mp83SM7t_usct1p1VSq1FfzVmFOWNfWSZwoKtWWv3fUuIm48WUhdekdYw9PywWtACGbGIgGK7UmoDf8UFCjzoJs0zcdFwUcKdwQEaJEuOfrGEzVCaKZiQuaSsf4uvprktI833Mvoj9FCriJ3Hm0Okd0_fTUacw9urKF48NB8SJO-8zoL5wzxeKVxTc71Op77A0iRQ6Mk2McNqLNK6GtLANIoDJ1vdqLfmmP-zeTBbr98pGIEETw_8QcIq7h15FG0l91NSvBpPs780dE57jpUiLJUjgz31vaB0L6-EdklKmiZBjbHUgkQoHiMaOWfL3of-den_BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de798daa31.mp4?token=tXnwn6_gEz-7Xm4Mp83SM7t_usct1p1VSq1FfzVmFOWNfWSZwoKtWWv3fUuIm48WUhdekdYw9PywWtACGbGIgGK7UmoDf8UFCjzoJs0zcdFwUcKdwQEaJEuOfrGEzVCaKZiQuaSsf4uvprktI833Mvoj9FCriJ3Hm0Okd0_fTUacw9urKF48NB8SJO-8zoL5wzxeKVxTc71Op77A0iRQ6Mk2McNqLNK6GtLANIoDJ1vdqLfmmP-zeTBbr98pGIEETw_8QcIq7h15FG0l91NSvBpPs780dE57jpUiLJUjgz31vaB0L6-EdklKmiZBjbHUgkQoHiMaOWfL3of-den_BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توقیف کامیون با رانندگیِ دختر ۱۰ ساله در هرمزگان!
🔴
رئیس پلیس راه استان هرمزگان:یک کامیون کشنده که توسط دختری ۱۰ ساله هدایت می‌شد، توقیف شد.
🔴
این اقدام، مصداق آشکار به خطر انداختن امنیت ترافیکی و جان کاربران جاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134670" target="_blank">📅 11:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134669">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/673fc2d1a7.mp4?token=T5VV90kiSdLNvPvja-vQPpmju173mtjNgiaIp4owd07FOFB0C3eUNW_78H4Na9Bmah4RKiDwT5fUB7ADK2RAQoSYlU5Md1LsYaWLqhaKoZvx4aEepT5kMd2glsY8AkkTFiDnXzHfH5a5nUMxgdrtKWtjUTURj3Boi6mpdgaUw2yA8w_s5mtHuWkPIOkWSlzyLNBnB2CJxC6pPr9M4461_Wh8Z1sb-Ytn5ZXixfxpm2sJp6wqTIXo_apWSTvI5cHTgckPcDvbnrobwFBrY5rnUQDx1YQ_GKN425ijAhtn6hmLH7fTgSWxwC3O7SjTDJiIgOrbI1ebscQw0QEybY9Viw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/673fc2d1a7.mp4?token=T5VV90kiSdLNvPvja-vQPpmju173mtjNgiaIp4owd07FOFB0C3eUNW_78H4Na9Bmah4RKiDwT5fUB7ADK2RAQoSYlU5Md1LsYaWLqhaKoZvx4aEepT5kMd2glsY8AkkTFiDnXzHfH5a5nUMxgdrtKWtjUTURj3Boi6mpdgaUw2yA8w_s5mtHuWkPIOkWSlzyLNBnB2CJxC6pPr9M4461_Wh8Z1sb-Ytn5ZXixfxpm2sJp6wqTIXo_apWSTvI5cHTgckPcDvbnrobwFBrY5rnUQDx1YQ_GKN425ijAhtn6hmLH7fTgSWxwC3O7SjTDJiIgOrbI1ebscQw0QEybY9Viw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت‌های مهدی مطهرنیا در مورد احتمال حمله اتمی به ایران
🔴
باراک اوباما هم در آخرین سال ریاست جمهوری گفته بود پایتخت‌های ایران و کره شمالی در مقابل حمله با بمب‌های کنترل‌شده هسته‌ای استثنا هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/134669" target="_blank">📅 11:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134668">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزارت خزانه داری آمریکا؛ ۱۳۰ میلیون تتر دیگه از دارایی های ایران رو مسدود کرد!
🔴
جمع کل تترهای مسدود شده بانک مرکزی هم تو یک سال گذشته از ۱ میلیارد تتر عبور کرده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134668" target="_blank">📅 11:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134667">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfH0MNPDKPGghHm40kl5ABli1_5IYfd0ca7Iwa5o0WbLxUKSyoQ2uGRAxNRXkt5MRQOkE0HhQDztkPUAlUnDzM_z-PfM_oMqQZT1WnUxt26qiI3FlWIAqVu3sn378YxaIA-nxIXUI08ST9xQnL-S-jj0MV5WP-GaJwtzJaBYrTRpmfgzdzck09V5beDCS0WJoNn1Js63vwtwi-xvpCWsSm5cFs2V2KVd3E7PRlZaAe6ggY7fGQt9aGgADmpvtrSFeR2BIc_TnviEU-lT7KaxoC5Uot1p-YhgJ265Z6lN1YvwP3hoPx76gf0qWEACHjIaENC1Er4YzphOrJmPg2KOvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرآنلاین: احضار برخی نمایندگان تندرو در پی ماجرای تحصن مقابل مجلس
🔴
مجید نصیرپور، عضو کمیسیون اجتماعی مجلس، در گفت‌وگو با خبرآنلاین با انتقاد از عملکرد برخی جریان‌های سیاسی و رسانه‌ای در دوران جنگ، گفت بخش زیادی از تریبون‌های رسمی و رسانه‌ای در اختیار یک جریان خاص قرار داشت و انتشار برخی روایت‌ها و اظهارنظرهای هزینه‌ساز، زمینه شکل‌گیری شعارها و برخورد با مسئولان کشور را فراهم کرد.
🔴
وی با بیان اینکه برخی افراد با وجود مسئولیت و جایگاه خود نباید به اختلافات دامن بزنند، مدعی شد بر اساس شنیده‌هایش، تعدادی از چهره‌های مرتبط با تحصن مقابل مجلس از سوی مراجع مسئول احضار و به آنان تذکر جدی داده شده است.
🔴
نصیرپور همچنین تأکید کرد برخی جریان‌های سیاسی، بقای خود را در ایجاد دوقطبی و اختلاف‌افکنی می‌بینند و معتقدند با از بین رفتن این فضا، سرمایه و حیات سیاسی خود را از دست خواهند داد؛ موضوعی که به گفته او، در نهایت هزینه آن بر کشور و مردم تحمیل می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134667" target="_blank">📅 11:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134666">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
روسیه: جایگزینی برای حل‌ دیپلماتیک بحران تنگه هرمز وجود ندارد
🔴
متأسف هستیم که رویارویی‌ها پس از امضای یادداشت تفاهم، بار دیگر از سرگرفته شده
🔴
امیدواریم که مذاکرات ادامه پیدا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134666" target="_blank">📅 11:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134665">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
قیمت دلار آزاد امروز به ۱۸۸/۶۰۰ تومان رسید...
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134665" target="_blank">📅 11:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134664">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
روسیه: شب گذشته سلسله حملاتی را علیه تأسیسات صنایع نظامی در کی‌یف و زیرساخت‌های بندر یوژنی در اودسا انجام دادیم
🔴
وزارت دفاع روسیه سه‌شنبه ۲۳ تیر اعلام کرد نیرو‌های این کشور شب گذشته سلسله حملاتی را علیه تأسیسات صنایع نظامی در کی‌یف و زیرساخت‌های بندر یوژنی در استان اودسا انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134664" target="_blank">📅 11:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134660">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7wc_u2YMnOsa_s3RbRe65S4gr-spP9Uvb1dr0k0B_z3YkEGOOP7x62J0a00U80r_C9tsvSNuBOLsI_hYlx846nQsUntRFhxp5lNKpzYCWuGUpm9iF6A9-OzZ58dtt1wMPWa8JHlGYiMcUJYyurD6rtCIroxlorm-CnUt6mixx5CMJsAcjEHlkPFHj57gGMhkFVUIvqFIcVbsZNd29vw2VsUkoGwNtEa7Atx47XDlvKjqBuBavxgPrCyDaOXXZ6IcPkU_YuX2NqduhBf-3f26utf_j91C6afFcIsWc9gVp07n6o7bUpuenXDBPn_WYjckqHh05Pp5UL9N0M5VLq_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/liV3t6Q5Vpbi18zAxxrlQtjNLM4k2Q1DAzJNX9KMesQBF-0sMp0izNGcnppxZ1xchbdQtH_sVDpx5PcpzNnPau21A_cGGo5J_gIMMAWi_N9irkJLUUiY4rTgGUfhsPaXrApbf2FZXYF75I1z_r67Iu5PNY6zUc53ZwjRX-_HsfuFBO9-BOTiQNqz2nZ5s3Q9JMJUD9cPCMFURr55Feoq8ShYeHNSXfAioONlrf8yIxJm-o4qDMAv5qlPDjdFujrplgOG9eBpttVhRGdfL1HygD7prDLtzaUB_FanQI1rsi3tSbACJP3XTQyn1twcpg3EM1HQr576qaxIS9kpW5aB2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7eMYuMRvVW5CQnbUpDpUIImD9-IhcMVQp1jvQztcfAFPT2VQjO4XzNaycvKDp8iYzD-u2nW6DG1JvAklD-PHR32kvuD9ZzJutPumRCFnHAh7u3FbQY-OxJ9R33D6DMKml2tdOYheV5G7tgY3U-0DSV5nqULxaHLZxeVLeI29k8VUgFZ2GgTACXxa63JJj03l-aPIySYQBLwJNSwyqKy3-nTyToFuo6wo5sE8I4Hd9B2WpAusm6kkiYVdYIsjpL8vQfTCEvcN6-hfl7tgkXEM_x_Q3DT6Z9NXa03rPrPxToEOX-SvjFXC8jI9HyD7TrY3CL8ju2-4JQHn_c3rT1GFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bwiTpwK39mGb8MbTpfWiqpCMQ6syBgPmgoPA7fSnW-iS4hqXU2e1hzPGOX_X1iO43QsM08MeA4g1YUvinMrpviCGSkiNkR_jKtgYE7f6L8n10lZsKgxk1QLwDy-P0ES33ygbCq_PWLMx9AUr5bVnUtTx1rr7thSGNYhUV2MIvPu6F1HN4b3GG4djmIJkwOW23qu536b46Qz-YmCo_-qmoCriwyvj0TXaXwUbVHwFsZoJPCqMsxzZR7ASKJqis4GzFVO95jEOuoak1gWWPK3lVw3udyd1hm3-GyIqXdzAX13oNtORSnW1C2-kXSIvs99mVTFTRmiu9kH3WEcg8RyE3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازیکنان آرژانتین بطری آب جردن پیکفورد پیدا کردند؛ بطری‌ای که روش نوشته شده هر بازیکن پنالتی‌ به کدوم سمت میزنه.
خنده‌های انزو فرناندز که مقابل اسمش نوشته شده بود “وسط بایست” (یعنی پنالتی رو به وسط دروازه می‌زنه)
@AloSport</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134660" target="_blank">📅 11:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134659">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c9b24d606.mp4?token=mz3mzlcpx3vrmv5_oPpZYZHl1Y8ymfvV3HydV0I-EJAQcriuF2Yiqv7HJyQi2AZ6hIgjJm-7aUJpJdQHvo4o3u_RXzsteNIAR5jXA9iUKzA4gYri9kzw7TvNkaAnT_bBfcgePqCVVLeg31W_kg-aKxuyAU-MSqQhPxFfamj566TsaoYgTq9mldCYbPnKtnvUSgVRvQcrnXALeo-UvdCuXNXP2wEI7LU_xLl4caDK6FqOJXMxf6M5pQb1y7YdAJEDClh9kQTnMU3dcGa55jN_S6G1bQ5Fpke0B1Ia9qjsR07hxvvP0FTkqgyO7wUfYRyJzPqKKWl57mIniloc7DiHxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c9b24d606.mp4?token=mz3mzlcpx3vrmv5_oPpZYZHl1Y8ymfvV3HydV0I-EJAQcriuF2Yiqv7HJyQi2AZ6hIgjJm-7aUJpJdQHvo4o3u_RXzsteNIAR5jXA9iUKzA4gYri9kzw7TvNkaAnT_bBfcgePqCVVLeg31W_kg-aKxuyAU-MSqQhPxFfamj566TsaoYgTq9mldCYbPnKtnvUSgVRvQcrnXALeo-UvdCuXNXP2wEI7LU_xLl4caDK6FqOJXMxf6M5pQb1y7YdAJEDClh9kQTnMU3dcGa55jN_S6G1bQ5Fpke0B1Ia9qjsR07hxvvP0FTkqgyO7wUfYRyJzPqKKWl57mIniloc7DiHxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از ماهواره های استارلینک ایلان ماسک در آسمان ایران، دیشب
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/134659" target="_blank">📅 11:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134658">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزارت خارجه آمریکا بامداد پنجشنبه از موافقت با فروش ۲ میلیارد دلار سامانه‌های موشکی نقطه‌زن به عربستان سعودی خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134658" target="_blank">📅 11:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134657">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECAyagvguD6ZUSLkiWvmH-5i3_oO82IdOSK-dKzojgL43bGSwVzW-ySDxIfjJWyIEEfvhL5jWRUrk35to5xSvKjIEtIuyyjzmePlk63n6Hfcs4Znb3AHmndWeborTyE0r_EjZF9FbYO_6RTuTMjb23SD1W15_ds5LguXwwGyYsr4CMRn3WR9yPEhILb30qiGXAy2kO8gP0ptuycv-ESfx1REFrSY_C6EDDSljCwk2GSWNtxOI1ATvavw6GL4Y81ZBUs9vGfaadLo9oN0lE_VnGsLL3nxYnaVLjxn4AGCzO6jzWySHBkB_vdoOmtE5qtO6zfUo5m4bqDUguI4ekrDLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غضنفری، نماینده مجلس: پزشکیان و قالیباف حاضر نیستند اعلام کنند تفاهمنامه با آمریکا عملا نابود شده
🔴
شجاعت و صداقت عذرخواهی از مردم را هم ندارند. اسمش را جنگ بگذارند یا نگذارند "جنگ سوم" عملا شروع شده
🔴
ترامپ، ونس، روبیو، کوشنر، نتانیاهو باید قصاص شوند. نه تنها یک دلار در جریان تفاهم نامه را آزاد نکردند، بلکه آمریکا در حدود یک میلیارد دلار ارز دیجیتال ما را هم توقیف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134657" target="_blank">📅 11:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134656">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزرای جنگ اسرائیل و آمریکا
🔴
هگست، همتای خود را از فعالیت‌های نظامی ایالات متحده در ایران مطلع کرد
🔴
کاتس بر اصرار تل‌آویو برای ماندن در مناطق امنیتی در سوریه، غزه و لبنان تأکید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134656" target="_blank">📅 10:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134655">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
صدای انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134655" target="_blank">📅 10:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134654">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزارت امور خارجه پاکستان: ما به تعامل فعال با طرف‌های اصلی ادامه داده‌ایم تا از تلاش‌ها برای کاهش تنش‌ها و گفت‌وگوها حمایت کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134654" target="_blank">📅 10:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134653">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سخنگوی ارتش: در صورت تداوم حملات آمریکا، جنگ به عرصه‌های جدید کشیده خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134653" target="_blank">📅 10:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134652">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQQA8PiM_MdAlzbj0oya_71wCIH3lxfQueeGufJ-puuLLbcmiElPBijeolnzTqtRz0YDqgulF65PTESEu1mYIFngz3GqgVdtMpEkgMCLh8I3U22nuBLaVjKQMFfKiqwTQuKt0I2Q0o0as_3bYrQ0dBrmz7J9fKuVjyWH6u7-tmukwA0BA4OnixIMeVSXBpRsgUOcDO6yR6t-2nmm_THHJx8N1AbNLnzrNljrbdc4SlXyg8vuTINTk5MaPGDIFIYqRQ9t1K9JEs7j3u2wMv4vchikHYgTcaiuoSIeCaLgZiznPE-CcdDHIVkayCkkrjpp52y42w57ebzcSsfeKzSxkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عقب نشینی نفت برنت به 84 دلار
🔴
قیمت این لحظه برنت: 84,69 دلار.
🔴
نفت آمریکا: 79,42 دلار.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134652" target="_blank">📅 10:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134651">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
شبکه آمریکایی سی‌بی‌اس فاش کرده است که رئیس‌جمهور آمریکا، دور از چشم دوربین‌ها، از رد پیشنهاد ایران برای توافق هسته‌ای ابراز پشیمانی کرده است.
🔴
طبق این گزارش، ترامپ بر این باور است که واشنگتن با رد پیشنهاد تهران برای محدود کردن برنامه هسته‌ای‌اش، فرصت جلوگیری از طولانی شدن درگیری را از دست داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134651" target="_blank">📅 10:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134650">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc1a68ea8.mp4?token=pbdJ4YqgnnwRrTR_hh5CLXBQtkUKZ40fnXEgMRnmImaibwcwy1S6K3Gcytko9yDQ5IozC8_2H_nTu2AkLgt0_OLikPrb4-3tBckDpRofambdNOpjWMk42OM3JspH8A_4JJCVULrdFdOcsKooIVMIQqUGDRryZuhZEw6IJk4mWNFuukrixJJ5wvDR_ICT57hqOYsFAChY5kET_c8PqL7OfY914FoPou6AFrHKw6Rju-byx71Hsnvfyyu-n-z59Ij93nu0L-Q_QOvqw0LPHgWIaCFBeqPLqC6dKe9Q_A8UKmjZm8RKvnFNkvvqKVp8MbNA9POlRcVpcMXEPZ6cvdhH9p-vs7ZwhO5pmb2YUcPBdee6GeUqp_6N2P0hSUbMqNURj8X8g_4KsiPqfutz1sj9LdWOT84s0Fr6kWMd0vTI9z5QhQiPTtj_FzEbfcWWeiZyeR0mVozy8J2KARhwmiTrn1OUXILS00CE0wdq9upJofUEi-EmQLKVJ2soKi-B9v44tHeA6lnUlXSLVQmIEVr-qd_QVyG0lb7tXE1Zc07fjh09YIuHg-XPhs0BR2U-aHDFKe3ug3DR-3oThAVdS6xftq2nN8KHPvp__xHatbW2jakpvhkB7Qs_8c-rWpP_HdSawGVJFCioSUBwN0Dy-6PrYYcEfp5kKpk3E1mnISVBhLM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc1a68ea8.mp4?token=pbdJ4YqgnnwRrTR_hh5CLXBQtkUKZ40fnXEgMRnmImaibwcwy1S6K3Gcytko9yDQ5IozC8_2H_nTu2AkLgt0_OLikPrb4-3tBckDpRofambdNOpjWMk42OM3JspH8A_4JJCVULrdFdOcsKooIVMIQqUGDRryZuhZEw6IJk4mWNFuukrixJJ5wvDR_ICT57hqOYsFAChY5kET_c8PqL7OfY914FoPou6AFrHKw6Rju-byx71Hsnvfyyu-n-z59Ij93nu0L-Q_QOvqw0LPHgWIaCFBeqPLqC6dKe9Q_A8UKmjZm8RKvnFNkvvqKVp8MbNA9POlRcVpcMXEPZ6cvdhH9p-vs7ZwhO5pmb2YUcPBdee6GeUqp_6N2P0hSUbMqNURj8X8g_4KsiPqfutz1sj9LdWOT84s0Fr6kWMd0vTI9z5QhQiPTtj_FzEbfcWWeiZyeR0mVozy8J2KARhwmiTrn1OUXILS00CE0wdq9upJofUEi-EmQLKVJ2soKi-B9v44tHeA6lnUlXSLVQmIEVr-qd_QVyG0lb7tXE1Zc07fjh09YIuHg-XPhs0BR2U-aHDFKe3ug3DR-3oThAVdS6xftq2nN8KHPvp__xHatbW2jakpvhkB7Qs_8c-rWpP_HdSawGVJFCioSUBwN0Dy-6PrYYcEfp5kKpk3E1mnISVBhLM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر از یک کشتی مسافربری که ارتش آمریکا آن را منهدم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134650" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134648">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZGgYp6QqNcHJ296yNBmZIYYnzX518DNxmVZl1zcGawjmjecYy1wkwBYRe2GZeOgfeJj3gf0TKWqKqrmAOxf6zOD127c4z6B8mKZ05nKgyLuzp8E0HRFCCk07k0hQLFbUR4-Ft45YsI6f0naIINsdVu-joeiFqbfpGmMxTU72QWfnBRxlQlinKwF2qr8HDLtsYpbqnR68vWU2R5iB35bS4UXJ3XrixW55B2ImrABlvluoOZa8c5Hvuqj3xJOwxUMr4pYjYNgKTKpd_q6gxnx80a8LWoCFMlKDlKtKFoRU3Euqj9QBEgFfhKpvzcKV8zu5fOvjJu2r4u8Rv_lbDqfRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/koGw-rxy5yM2D_IKUW3yw-CklJJwf3ty3eGSwnYIbNin7nFkk7uDJrE-NY92lUPWyRMEyRgL5ZbLRCP8QCnGO8NzJm8rfz9K7SHEkaw-65dmfg5fJJRVfCVeeQJmzf-2T9EFdU71Arlrr-plRAx3mef0WxF1ypiJZI_caQzXCfuS1Gb_7eAuaoP-gE3lcCMCA_yPl4KsSZQa62o1cyUCgSST7HVVTEDO8epKt99YU9hq_1d-afToYEf0UJfTrLQXkzp5ePjO06j8xSoo9JhfDz40EKCvV-iXpfhnrwRN_pg0g4gyIl_9aORy2Zns4RunUxtRlAWJv8NTHzhFlw3msA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
ولی ما میدونیم چرا!</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/134648" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134647">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه روسیه: بحران تنگه هرمز تنها از مسیر دیپلماسی قابل حل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/134647" target="_blank">📅 10:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134646">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6657e40491.mp4?token=qOOD9FBpnJeAgINI1nwyxWIHshd19cb46AFdYheMXYKr5NhF8e43rOaXGJSPxQ6FcnOya85VnW--FuBpL6MKKttPyFNdgMK_YARowfJzwKmmzMpAvMPz2OkIot5GkiIueQbbTo6ryOcvF3g9wGtdkyeZEbklE5VE8HHP0XYQ50Wa3K2M_pSebO0moejSG5KI21eJLZ3y0ZAK0jJJ6CLqkBGpA9NVXGXH1rvDgRpyjSHPreWhoz7RTn3f8UsdNzwYBBImZd9izkpwbkeJPbTnUamh3b1pQkOk7g_9hqFBYxBJU5UkyTVhRhR036V5ZwbI5uhE_EpGKAE493C7bRnqCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6657e40491.mp4?token=qOOD9FBpnJeAgINI1nwyxWIHshd19cb46AFdYheMXYKr5NhF8e43rOaXGJSPxQ6FcnOya85VnW--FuBpL6MKKttPyFNdgMK_YARowfJzwKmmzMpAvMPz2OkIot5GkiIueQbbTo6ryOcvF3g9wGtdkyeZEbklE5VE8HHP0XYQ50Wa3K2M_pSebO0moejSG5KI21eJLZ3y0ZAK0jJJ6CLqkBGpA9NVXGXH1rvDgRpyjSHPreWhoz7RTn3f8UsdNzwYBBImZd9izkpwbkeJPbTnUamh3b1pQkOk7g_9hqFBYxBJU5UkyTVhRhR036V5ZwbI5uhE_EpGKAE493C7bRnqCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس: اگه رژیم بپاشه، ۹۴ میلیون آدم درمانده به اروپا و ایالات متحده سرازیر میشن! و وقتی تروریست‌ها در همه جای دنیا پخش میشن، زیرساخت تروریستی‌ شکل می‌گیره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/134646" target="_blank">📅 10:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134645">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fS2596qVPBWELgOQwxvm5oj2r-bqnau99O9WZOWzT5I4EDuJCSsj5mMLxMOHTuHQmD1OEsxowQDfQPWzFTqqMKK5v3Y2AD84bByzSeweESH942V3gNDFY4rFULJfYi4l_Cuu1by9XoQPTXOhPt9LBMXn1OAZRR5j_mI0aS1MjSYalwOAnEnwXmfOtR3ugKS7vXyq3K2MTmAOMxUAkco3RwWF3RTNnMmEUSYP_MxDWM7E9u9RCrEX5tfn_X_L-UubQkxNw-b9gg17595V411tR55aYW5K7hgba5Jgtg_pF6U59QJV4jFp0V-4CFMzyvCafoGQ4Rq4wlGrZJk6WHdnog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشف جالب مسی و یارانش از گلر انگلیس
🔴
بازیکنان آرژانتین پس از پایان بازی با انگلیس به‌طور اتفاقی بطری آب جردن پیکفورد را پیدا کردند. او تمام عادات پنالتی زدن بازیکنان آرژانتین را روی این قمقمه یادداشت کرده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/134645" target="_blank">📅 10:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134644">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری /  آمریکا برای حمله به کوبا آماده می‌شود
🔴
شبکه «سی‌بی‌اس» بامداد پنجشنبه به نقل از مقام‌های آمریکایی گزارش داد که پنتاگون در حال آماده‌سازی برای حمله نظامی و تجاوز زمینی به کوبا است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/134644" target="_blank">📅 09:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134643">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سخنگوی قرارگاه خاتم‌ : اگر زیرساخت بزنید، هرچه زیرساخت در منطقه باقی‌مانده را می‌زنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/134643" target="_blank">📅 09:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134642">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
جی‌دی‌ونس در مصاحبه با پادکست «جو روگن اکسپرینس»
🔴
کسانی که از مذاکره با ایران امتناع می‌کنند، هیچ راه حل واقع‌بینانه‌ای ندارند و تنها پیشنهاد آنها بمباران بی‌پایان و بیهوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/134642" target="_blank">📅 09:33 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
