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
<img src="https://cdn5.telesco.pe/file/QcDJAgCY8Hj73dMOAKhWYEG4ikGZHtW7sI6SI-zwEbnYlLk3-8p-8RK-SEWM5bU4ZjAJfMiWaQmVB6EMHiGwFgL3w6_KjIalXkXvxE0q66tdAWvO4cjZw7cdAUu-y4wcPvtUYcLBiJKfxcmAquJmaYzRzGoxZkgeGr67P-V3lbckc5HmYmsTQt6YB6mJMPj6OXnumkpFfwOfpYOEJRyvbxZf80cU7AeQa6VRvu_LQjrzpVhDRiZNYYjmmctHAeUUxzZA7hEgMD_vXEjsTwopjgjmq9OV8KLv45Pb3X0ptc3w8RrifMNRe1CtE2RG-748uZMdZVdz7OcpydqtjOYLYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 426K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 17:26:02</div>
<hr>

<div class="tg-post" id="msg-105594">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇨🇳
🏀
ژانگ زییو، ستاره‌ی 19 ساله و قدبلند (2.23 متر) از چین
🥶
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/105594" target="_blank">📅 17:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105593">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🔵
مصطفی‌متدین از مدیران صنعتی هلدینگ پتروشیمی خلیج‌فارس در آستانه مدیرعاملی استقلال قرار دارد. این شخص پیش از این مدیریت سازمان توسعه هلدینگ‌خلیج‌فارس یا به اصطلاح شرکت "پیدمکو" را برعهده داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/Futball180TV/105593" target="_blank">📅 17:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105592">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixv-GINYk7AgClNeAnf2rZCJ4BB6uXqf4wkPFNQkiqH4J-DJ6iBYS-BD2cbeZEBC7OQV_wiNvql6U6mImW-bOrCxqc51T76a6aHbiABn_an-Smg4wFSEwFi80vcqevM52h-K6x_c01G5CtOkQ7ou1tnYMQOhdKiTJXOoROZMZk048TSAZYp1bOjnVSx-1oH3zHDB4PeuzCRFJuqcWT2tLPIL3oA-qhPaVHjTMDJNkNmky5guNccJwlY-dVdKc9cmmS3lZeI-qK4zvgz37e5dY8XPpSJvBEH7KvmCWRKOHGpSeCIThywy5i6fFSi9fcfAElqBiqcEVD-G11gi02AGDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
لیگ برتر ایران؛ ترکیب تراکتور مقابل گل‌گهر
تراکتور- گل‌گهر (١٨:١۵)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/Futball180TV/105592" target="_blank">📅 17:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105591">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3805b0d1.mp4?token=HidpGq7GtQArNxzFeYzE0h88tTw1Cqw2JiS6PAso7yqhHCcUs6hz_v608YIVEpRUCBIegQLpL6B673kig2YkP3_Z0TKP1CV-jHLlwrEvydsEKISCcRqIXzo-ZgwybNkffaIfFrEJwqgQr_bHjmDYaEhP3i78q-FqVPnXJcZkGM1_tB_oYvDlZOlinTiHBLpWBH4c-nt1fa-XC-nb24fAQdDoqY9--igXQEpq6Vp4Yq_dSSEMOs0Rqu7QmFSKhg0ysU-XRlYUcSioaPaw2I_w0FxJYC9OLqsvERfJ5hE1XtFcyzcB654pWoeJmBAURo2gi60tuR7NBlABAFdP8q9cIjDHJpVgrHEVuSBHE8tG0sQfyX9G14GurfDb79e7uBz3BH4deXHm6XgO_ajbYCVC3gh6Xa6K6-uRHIUGBTPftT5S7gl7UYuMpovOBlKwrJ6bWqR73BJr1YCCuEhTRqyYAPzVe1oFoyMg-rKPhrw0jAt7sTELk-0jFbbx4ikpfsHS5332W1spSANJkCzEWxqwiHf8_or8zOb77-Gg169ke-xAKFO-OOKcSsv-IiX75AZ0ZFmH3AHXQZ41Jk0nX1bB2WMIbnjPdNdaj2-yW5MRn4a0GwoXFzIH2sCaDLIgqaF0hDt9MSn2HJecOKogbFdCnTSi81nRNpZcxyyMV0nW_Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3805b0d1.mp4?token=HidpGq7GtQArNxzFeYzE0h88tTw1Cqw2JiS6PAso7yqhHCcUs6hz_v608YIVEpRUCBIegQLpL6B673kig2YkP3_Z0TKP1CV-jHLlwrEvydsEKISCcRqIXzo-ZgwybNkffaIfFrEJwqgQr_bHjmDYaEhP3i78q-FqVPnXJcZkGM1_tB_oYvDlZOlinTiHBLpWBH4c-nt1fa-XC-nb24fAQdDoqY9--igXQEpq6Vp4Yq_dSSEMOs0Rqu7QmFSKhg0ysU-XRlYUcSioaPaw2I_w0FxJYC9OLqsvERfJ5hE1XtFcyzcB654pWoeJmBAURo2gi60tuR7NBlABAFdP8q9cIjDHJpVgrHEVuSBHE8tG0sQfyX9G14GurfDb79e7uBz3BH4deXHm6XgO_ajbYCVC3gh6Xa6K6-uRHIUGBTPftT5S7gl7UYuMpovOBlKwrJ6bWqR73BJr1YCCuEhTRqyYAPzVe1oFoyMg-rKPhrw0jAt7sTELk-0jFbbx4ikpfsHS5332W1spSANJkCzEWxqwiHf8_or8zOb77-Gg169ke-xAKFO-OOKcSsv-IiX75AZ0ZFmH3AHXQZ41Jk0nX1bB2WMIbnjPdNdaj2-yW5MRn4a0GwoXFzIH2sCaDLIgqaF0hDt9MSn2HJecOKogbFdCnTSi81nRNpZcxyyMV0nW_Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
لحظاتی از مسابقه طناب‌کشی تیم ایران در بازی‌های جهانی عشایری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/Futball180TV/105591" target="_blank">📅 16:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105590">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20fca94904.mp4?token=KNORPgSzYphI-BAk7rX7vQ-Y1sLHO90S7NYUkL986WEpIjfYHD79rvSb6XEnS5g1Z2VxERDASB_5eS8Js1fiqh26xnV_n5Yyj0BvKQlZdm3ur0LQOjy2Bwv55gmERLk8co7C7jg6pkuN8yQ23Iqh8J9DrANxBTFPuXvJ95t9zbQ092u4-xzFjF2W0gAEyF9IuoTAsYf_RJGowHuKd2RSrv7GGBOz_Dgo23kH2mOWPYqCemrFTrvB-hnxvAhQFsfLdv9p5xgJeSoz4am8wptkCS8_0libwOWPx6I--ZSMK4HjG5a3HANLKoCqYxN8XrJlYgZqxkUBreiO1QxhJo0fGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20fca94904.mp4?token=KNORPgSzYphI-BAk7rX7vQ-Y1sLHO90S7NYUkL986WEpIjfYHD79rvSb6XEnS5g1Z2VxERDASB_5eS8Js1fiqh26xnV_n5Yyj0BvKQlZdm3ur0LQOjy2Bwv55gmERLk8co7C7jg6pkuN8yQ23Iqh8J9DrANxBTFPuXvJ95t9zbQ092u4-xzFjF2W0gAEyF9IuoTAsYf_RJGowHuKd2RSrv7GGBOz_Dgo23kH2mOWPYqCemrFTrvB-hnxvAhQFsfLdv9p5xgJeSoz4am8wptkCS8_0libwOWPx6I--ZSMK4HjG5a3HANLKoCqYxN8XrJlYgZqxkUBreiO1QxhJo0fGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
هوادارای بارسا جلو کمپ تمرینی این تیم منتظر حضور رافینیا بودن. حالا رافینیایی که جلوشون دراومد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/Futball180TV/105590" target="_blank">📅 16:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105589">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAOYJACzVXaPEDfm6cUJkG0nAZNvKKMsVf6u5UVJGJk8quZnxhH_GRDoS2NtWVoNclTAr6ER44Sihbqt3V96CPfmqJ5Qd79y_Csy1U_tJ63isEY8OkLs9h4yHuP8UImbSbix1PMbNj_7X7Q_qx4XW0CEbe6vaqvKqL4mawX79s4QeBet0_DSrOoWgdgQ1NN5tf7nRUA7umEIVktoniEnJ9t7YO0HHysbsinY9qYxcjWrL9oDSBjrFDdm7QTxQQQRirLqZA34A_jgcel0-POCJ5s2K2pFgvp1Om9UBAt-b8Hb_oA_1vIJ3t_yAmYF9f0_Pb-Uts2-4fXYGJGijF25nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شانس برنده شدن باهاته!
🎁
تا ۲۰ شهریور
با خرید هر بیمه‌ای از اسنپ‌بیمه در
قرعه‌کشی موتور یاماها، آیفون 17 و PS5
شرکت می‌کنی
🤩
چرا با اسنپ‌بیمه بیمه بگیرم؟
✅
با پرداخت قسطی هم می‌تونی تخفیف بگیری
✅
برای هر سوال یا مشکلی، پشتیبانی ۲۴ساعته داری
✅
و در قرعه‌کشی
موتور یاماها، iphone 17 و PS5
شرکت می‌کنی
این فرصت رو از دست نده؛ چون با اسنپ‌بیمه شانس باهاته
💙
وارد لینک زیر شو و جایزه ببر:
👇
👇
👇
https://l.snpy.ir/ixsth
https://l.snpy.ir/ixsth
https://l.snpy.ir/ixsth</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/Futball180TV/105589" target="_blank">📅 16:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105588">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
‼️
🎙
مُچ گیری عادل فردوسی‌پور از محمود فکری: کُل دنیا دیدند دارم به صورتم گِل می‌مالم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/Futball180TV/105588" target="_blank">📅 16:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105587">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29285b8410.mp4?token=t2fJAd4e5G8LjCe0NkTXiX5e96dxMTi4SS32ZfIITQ6Ao6GfYHINVT5lMpfYHzJW4ro3uOYXKEl-8bK2JqGRfcyDpxcXXjJ6Hc1g_joAcoM5laeoFh7P4o8Hax0pvyZ9NCF-bgMkOpjpPxlj31lR9wEq0dQPQX7eknO98r_mGq25r9D0RrVPMakxMrvGxwEmTE1mZVMMhKo0Bxt04GQsWcPHv10xyjIXGkPfK-i4ntMpOx219q33Qk2YmZjDgyLBwv_el6xv_-7Q0hi8CqNOK6y_w1kywp02DcS1kBrqynd7kh49WAv3XR3p3F-YSSnTkjoZh2n3JNWwZ_Pfewh8gSLtlzgRF-TaBf3ouH5MiHO7Tf7a8lQRv3cVztMpU9qGIjcaYtwYsBbj3U6WqPDNsFbgrih3dwcn2P0g3zlA81jGZ720YaXoAMZ8ayx4SbASo0G6bU_gwoGxR2-C1CLmjwD29UlbSmTI1bCQVETWHmaiRy_fyTAq0i5aERkjo65HNf3C0I2s5n6bXw95EpFOQPJIQBum3rN8MMi2YARczUreBy6WL1gab8OBSU_ODyXwmvc5j68tI0LDIru_urR5eqGmz6acLLHj073PTJteM_5ELts_Lk0idiH9T5Zn6JQpoR5rdsOj1W3iiG_axgjkPwifSg2mRqx6xba_4jEGdGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29285b8410.mp4?token=t2fJAd4e5G8LjCe0NkTXiX5e96dxMTi4SS32ZfIITQ6Ao6GfYHINVT5lMpfYHzJW4ro3uOYXKEl-8bK2JqGRfcyDpxcXXjJ6Hc1g_joAcoM5laeoFh7P4o8Hax0pvyZ9NCF-bgMkOpjpPxlj31lR9wEq0dQPQX7eknO98r_mGq25r9D0RrVPMakxMrvGxwEmTE1mZVMMhKo0Bxt04GQsWcPHv10xyjIXGkPfK-i4ntMpOx219q33Qk2YmZjDgyLBwv_el6xv_-7Q0hi8CqNOK6y_w1kywp02DcS1kBrqynd7kh49WAv3XR3p3F-YSSnTkjoZh2n3JNWwZ_Pfewh8gSLtlzgRF-TaBf3ouH5MiHO7Tf7a8lQRv3cVztMpU9qGIjcaYtwYsBbj3U6WqPDNsFbgrih3dwcn2P0g3zlA81jGZ720YaXoAMZ8ayx4SbASo0G6bU_gwoGxR2-C1CLmjwD29UlbSmTI1bCQVETWHmaiRy_fyTAq0i5aERkjo65HNf3C0I2s5n6bXw95EpFOQPJIQBum3rN8MMi2YARczUreBy6WL1gab8OBSU_ODyXwmvc5j68tI0LDIru_urR5eqGmz6acLLHj073PTJteM_5ELts_Lk0idiH9T5Zn6JQpoR5rdsOj1W3iiG_axgjkPwifSg2mRqx6xba_4jEGdGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
خاطرات شنیدنی ستاره سابق آبی‌ها از دربی شش هیچ؛ قراب: همایون بهزادی زبیاترین گلهای تاریخ را به تاج زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/Futball180TV/105587" target="_blank">📅 15:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105586">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59ae44943.mp4?token=QFPTCUM7DDVKAwVB9y_Ipg4C6pdLbslHcRxlbDrt3QgeJCb24sKReUAzNWcQy-1ExiNblFXnoiUjdJXW5jUsDuo4obcLz68g8-XzsbEiN1b8w_k3F2IFx39otR2EdyKvVXv1hGPfkW0xnJjWu8cw7jTYdNlnteZPoGOa-nqVjxQbBW1Ju8qRc37jt5Vgj2wthZBC5jK4LsT_wEm5RLeUpwaSJVVYPAY65TJyrNwg1_69UC9vxBQkMmqbLOLD79YSU9PosWF1H6XBzCm56JWWhUnx5NeH_KzNfK7w-dzvxUP765N_1z6vmws2FeeODZ7HPqXg9IvavcI5CIP6AfNiRDv4YXN48O3ESf_IqgIlGPiwGEiGp84bUJUmz9FJ6XXqxmzHgosBR3lnk-vyT2zxb3IP0fHtB3jG86vvhfx5snmSrFsib9KbWk-jtHe35Z-8oyDgqETi-L4CPVK4vLVuBI4uQbFW7zRAvOnBvkXfjA07Mkbz0ZBDP6jMSpVcr5mp5y4ovAs5Iaae2o9fsJZo6X23Yvu-J4EudZ435pmSnNfM90wroBqZQnT8yx8If75qn9HcD8L3PcaRgWH35Dk7jmcbs90sKhAk7S7INX8XbDbOmuRXPhMD3gqo9Bmcwvsgx2P4zEYAN0qBgH61vptm2yffVcmqVzDcNdacLMa-Woo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59ae44943.mp4?token=QFPTCUM7DDVKAwVB9y_Ipg4C6pdLbslHcRxlbDrt3QgeJCb24sKReUAzNWcQy-1ExiNblFXnoiUjdJXW5jUsDuo4obcLz68g8-XzsbEiN1b8w_k3F2IFx39otR2EdyKvVXv1hGPfkW0xnJjWu8cw7jTYdNlnteZPoGOa-nqVjxQbBW1Ju8qRc37jt5Vgj2wthZBC5jK4LsT_wEm5RLeUpwaSJVVYPAY65TJyrNwg1_69UC9vxBQkMmqbLOLD79YSU9PosWF1H6XBzCm56JWWhUnx5NeH_KzNfK7w-dzvxUP765N_1z6vmws2FeeODZ7HPqXg9IvavcI5CIP6AfNiRDv4YXN48O3ESf_IqgIlGPiwGEiGp84bUJUmz9FJ6XXqxmzHgosBR3lnk-vyT2zxb3IP0fHtB3jG86vvhfx5snmSrFsib9KbWk-jtHe35Z-8oyDgqETi-L4CPVK4vLVuBI4uQbFW7zRAvOnBvkXfjA07Mkbz0ZBDP6jMSpVcr5mp5y4ovAs5Iaae2o9fsJZo6X23Yvu-J4EudZ435pmSnNfM90wroBqZQnT8yx8If75qn9HcD8L3PcaRgWH35Dk7jmcbs90sKhAk7S7INX8XbDbOmuRXPhMD3gqo9Bmcwvsgx2P4zEYAN0qBgH61vptm2yffVcmqVzDcNdacLMa-Woo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
پریمیرلیگ هنوز شروع نشده، جنجال‌های داوریش شروع شده!
⁣
🎙
📹
مایک دین، داور بازنشسته پریمیرلیگ، توی مصاحبه با پادکست جیمی واردی اعتراف کرده که زمان داوریش بعضی وقت‌ها برای خودش چالش می‌ذاشته؛ مثلاً ببینه چقدر می‌تونه بدون سوت زدن بازی رو ادامه بده یا چقدر می‌تونه توی دایره وسط زمین بمونه و ازش خارج نشه!⁣
⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/105586" target="_blank">📅 15:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105585">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b748609641.mp4?token=RzunL_DpN2NHsZfjNwDcmWO40VKtB7nNEzxdG90go2s3bV0kBxlmMV9SXikhNokzXxPuRi23u2flZVL9xkGDem9GGrNm3wtOmIGk5hv5rSBbG_a1la30pCrz67SAZXFjjyRCz8OFBtlSZjbpbV6y3RRXtCd_aj1Zgndg-bpAVYN0gVRjNoHQcIp1OUfCuNLt26yBfBT_-fd9W0z8e3-0YPi_iH3Av9KRbPavIYE3te7mlkm5Pvv1NHGH1fJ21P0Wdo-s9na4uvk1AThoO-MVmakLE1PttiIdswmix_iyFu63nAN7nNXoRFcRn4ZZsIAr5NDuL8x7Yzq3enPR1Cz3rFRSmgIquJ7Sd0W9eaL2SD3mnMzAiswkXvxtROQFe4REmSBmOkQUBnGgjTdwLs3_gJOuVtePXYaANs3wbs06sxbsB-keAV4dYFKBGnAiZEBl0tn2Kbt7y4Gg4_v6As0SZx347sF50HVrn2lDIore5ZDJKW3yAyK4jc2ZjXN2lLeJ7voveMGyRDgHJj1uucfv4BeOOJuy1hTR1LVD3sVOKMjwjNmzRln4CMpMC0zl6lWT9qS4S56EQcrgWDSIH6MG79GVTknrZhh7OR5XkE8i97hlMVi6NHsr0cs4LjwUpju2SAJrEHwCA18Y2kZPoRJx8k8MDhRNAeLnEQ-403NDTr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b748609641.mp4?token=RzunL_DpN2NHsZfjNwDcmWO40VKtB7nNEzxdG90go2s3bV0kBxlmMV9SXikhNokzXxPuRi23u2flZVL9xkGDem9GGrNm3wtOmIGk5hv5rSBbG_a1la30pCrz67SAZXFjjyRCz8OFBtlSZjbpbV6y3RRXtCd_aj1Zgndg-bpAVYN0gVRjNoHQcIp1OUfCuNLt26yBfBT_-fd9W0z8e3-0YPi_iH3Av9KRbPavIYE3te7mlkm5Pvv1NHGH1fJ21P0Wdo-s9na4uvk1AThoO-MVmakLE1PttiIdswmix_iyFu63nAN7nNXoRFcRn4ZZsIAr5NDuL8x7Yzq3enPR1Cz3rFRSmgIquJ7Sd0W9eaL2SD3mnMzAiswkXvxtROQFe4REmSBmOkQUBnGgjTdwLs3_gJOuVtePXYaANs3wbs06sxbsB-keAV4dYFKBGnAiZEBl0tn2Kbt7y4Gg4_v6As0SZx347sF50HVrn2lDIore5ZDJKW3yAyK4jc2ZjXN2lLeJ7voveMGyRDgHJj1uucfv4BeOOJuy1hTR1LVD3sVOKMjwjNmzRln4CMpMC0zl6lWT9qS4S56EQcrgWDSIH6MG79GVTknrZhh7OR5XkE8i97hlMVi6NHsr0cs4LjwUpju2SAJrEHwCA18Y2kZPoRJx8k8MDhRNAeLnEQ-403NDTr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
🇮🇷
🇮🇷
لب‌خوانی صحبت‌ها در صحنه جنجالی داربی؛ کنعانی‌زادگان درخواست احترام گذاشتن داشت
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/105585" target="_blank">📅 14:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105584">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBXr5MzcQ-rMSLaBRWOoLqgDCFJ2023n4sR6QHxYFr0EglPxK382JWOSAXv-5qxHJiI2qLIndV0T-vWaJRoVLSZn0_elzEJc2AScW7jBCNxQqQQTugTNNBscapSXiDzXLI6XN8zxWTmloejzTP208CVeoL5c19Vp-sKheIJRSVWPLSMI7pexXL7Nlp6niJhZ39HfNEmpLsX_NNFWW1prOjZRI7GPM-sHRdMpA8o0WcQlGT1KgIe8Iuwf9r_f87idGFcJMOuTc6nLYuvxoavohdyXzRP99OSEQZKesQ7OujVuo67EtPguleKGhNf3--4dSf_mVOesi2HkVnCSqPbatw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇮🇷
💸
هلدینگ‌خلیج‌فارس مالک باشگاه استقلال اعلام کرد که در ۱۲ ماهه منتهی به ۳۱ خرداد ۱۴۰۵ موفق به کسب سود خالص بیش 187 هزار میلیارد تومانی شده است که در مقایسه با مدت مشابه سال گذشته حدود پنجاه درصد افزایش داشته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/105584" target="_blank">📅 14:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105583">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf4edadd1d.mp4?token=tcj4eQClqwMhleEz-JHKbq2Sbm8juaigR2a8IaM4er8RmsyIwvP3ii_MVYcy5a98PPkCsV8zTwKwJM7jn86uHKih0cPMgd0LeuvUt5Utsi498DaoOvnv8BAiYEOxRespLK0faRtu2gc3mL1OLpZwpogKZ4ALmPPoMhVwJPjACy2aULNML1k4WdmAxbCItZTVsUEUAEArJzkmXVUCww-4aGrjtzmC4RI7GiimsfapCCizltr-lZdbaGLkefKRPyV68X1kLvOf1aLFy6OlBIgU9omIm3qWlLXeDZ0VvtM7fuhdSZUYYfTO4OJDos29KVMSS6MIvlMUKsMmA1Lpp_hEMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf4edadd1d.mp4?token=tcj4eQClqwMhleEz-JHKbq2Sbm8juaigR2a8IaM4er8RmsyIwvP3ii_MVYcy5a98PPkCsV8zTwKwJM7jn86uHKih0cPMgd0LeuvUt5Utsi498DaoOvnv8BAiYEOxRespLK0faRtu2gc3mL1OLpZwpogKZ4ALmPPoMhVwJPjACy2aULNML1k4WdmAxbCItZTVsUEUAEArJzkmXVUCww-4aGrjtzmC4RI7GiimsfapCCizltr-lZdbaGLkefKRPyV68X1kLvOf1aLFy6OlBIgU9omIm3qWlLXeDZ0VvtM7fuhdSZUYYfTO4OJDos29KVMSS6MIvlMUKsMmA1Lpp_hEMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
🇪🇸
آیا پنالتی امباپه باید تکرار میشد؟⁣
📹
تحلیل صحنه پنالتی توسط روزنامه مارکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105583" target="_blank">📅 14:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105582">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71a26a715.mp4?token=PN2LSFoSPtSoGSEfkJLqjiYrHMTPUtzFphcUgFPL-zlEehMSRRanJdOyS84eQ_l5_aIdj95YjG1we07WjB2KNcnrSn_tzzcKikpp4YcrLs-cBcDjQxwJ2L2KlTiZJuB2MQ0J7cwbyBLEHaNf9i7k-c0gYGXKetHRHyyRmbmMNE3tsX-RS6c7H94Pu3S8cZpTgk4jX8BrocsbMiVd5rZWFPzUGwoVqduJVOwIRKLXU1HXz00GthckqwWbadWPYb0MzXPJih4vu91ElmfhB-qYa8CrhSgi0AEq4GIQ6qjLwA8FqGGLMTZrs5EEXW6mrG3m5nBuzEDmJdAUi5H-fTgIcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71a26a715.mp4?token=PN2LSFoSPtSoGSEfkJLqjiYrHMTPUtzFphcUgFPL-zlEehMSRRanJdOyS84eQ_l5_aIdj95YjG1we07WjB2KNcnrSn_tzzcKikpp4YcrLs-cBcDjQxwJ2L2KlTiZJuB2MQ0J7cwbyBLEHaNf9i7k-c0gYGXKetHRHyyRmbmMNE3tsX-RS6c7H94Pu3S8cZpTgk4jX8BrocsbMiVd5rZWFPzUGwoVqduJVOwIRKLXU1HXz00GthckqwWbadWPYb0MzXPJih4vu91ElmfhB-qYa8CrhSgi0AEq4GIQ6qjLwA8FqGGLMTZrs5EEXW6mrG3m5nBuzEDmJdAUi5H-fTgIcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
😁
😁
😁
وضعیت دیشب فوتبالیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105582" target="_blank">📅 13:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105581">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0lp9RZHNx7iigFUHeo-jv6jj_nRfh_GQHINCesrrAcJiJKMWXnQcUX9lLGqZlIKXWGyQ-1h12NgssAANW4BUNSd-Cu7bmxwYhB_WHxV9N81MU9UaUVUqB_LJ5Pyck1q8dqnRFYFkDnSjsw-HdXhyCd1UOm63lFR50HIAByGnrB4UFoxUf0A_fboGX7vvOIwOp1XbUqP8MpKtOAu5mSsJnzAYaByOv17t8J-uEcUR_38aypVCAhEIrc5BggpNp8WiQFYvUj3bmp2iP9jLOoxQcOf41MJSzMCAzrPGtPtLiktIjPjGrtjxKDJOnJOs14OK9Y27OSnty2V4WEIvcryeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
20 تیم برتر جهان، رتبه‌بندی شده بر اساس ارزش‌های بازار، طبق داده‌های سایت ترانسفرمارکت
💸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105581" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105580">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
براساس گزارش برخی منابع خبری، سهراب بختیاری‌زاده به تاجرنیا اعلام کرده که زمینه فسخ قرارداد با صالح‌حردانی را فراهم کند و دیگر قصدی برای استفاده از این بازیکن در تیمش ندارد! به عبارتی از این لحظه استقلالی‌ها باید از بین سهراب و حردانی یکی را انتخاب…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105580" target="_blank">📅 13:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105579">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
براساس گزارش برخی منابع خبری، سهراب بختیاری‌زاده به تاجرنیا اعلام کرده که زمینه فسخ قرارداد با صالح‌حردانی را فراهم کند و دیگر قصدی برای استفاده از این بازیکن در تیمش ندارد! به عبارتی از این لحظه استقلالی‌ها باید از بین سهراب و حردانی یکی را انتخاب…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105579" target="_blank">📅 12:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105578">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
‼️
🇮🇷
سهراب بختیاری‌زاده درخواست برخی از پیشکسوتان و بازیکنان استقلال برای بخشیدن صالح‌حردانی را رد کرد و نام این بازیکن را برای بازی فردا مقابل آلومینیوم اراک خط زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105578" target="_blank">📅 12:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105577">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=iomDK0C62Bied5CjaZXz-6ucYN_cxmVlVkuj_O-t3t4mjL4brCKh2USwQeTMBLYifxKAiycp0mEInDGM4lAExEZA33BNPzkpS6Cfdaaai5mEOcm78lCIrk2EiOBCYOLOR1X84BWfdBnwp5388tmPalbjqJxDKpzw18DEpcC2GzFdSR63rlyXHxzSJTZAGTnrdR87fL3FK0r6kjYB-mePLKoy88HH77vPwtunm1AfLJiNgwXB_T_oS5TOARRN6KLHshLWp6n06ZmF3oWDmsnUCaMIxSGC-pKWYym86G3o289rBFt_u9_ksL0TkqIB65L5kusVdYPSW5xMCU7t21pBEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=iomDK0C62Bied5CjaZXz-6ucYN_cxmVlVkuj_O-t3t4mjL4brCKh2USwQeTMBLYifxKAiycp0mEInDGM4lAExEZA33BNPzkpS6Cfdaaai5mEOcm78lCIrk2EiOBCYOLOR1X84BWfdBnwp5388tmPalbjqJxDKpzw18DEpcC2GzFdSR63rlyXHxzSJTZAGTnrdR87fL3FK0r6kjYB-mePLKoy88HH77vPwtunm1AfLJiNgwXB_T_oS5TOARRN6KLHshLWp6n06ZmF3oWDmsnUCaMIxSGC-pKWYym86G3o289rBFt_u9_ksL0TkqIB65L5kusVdYPSW5xMCU7t21pBEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
وضعیت دخترای حشری تایلندی بعد دیدن پرسنل ناو هواپیمابر آبراهام لینکلن در پاتایا برای تعطیلات!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105577" target="_blank">📅 12:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105576">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇪🇸
لامین‌یامال در آخرین تمرین بارسا پیش از بازی با والنسیا بدلایل نامشخص غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105576" target="_blank">📅 11:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105575">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzGAwe8e5Wj81rEIEBpig6-oBzW90Y2JGiR22z7oDbkDINKI4dZm12_BOSK-3eeQsreTA4hCNo6o2D6icZ3vTEM8m6RwkyML-qbKJNgOhgObzKLGtAFim4ijkNHDXHnr32OF7fcK-R8v6hagDM8okbF9gc3gfWkZ3r7Oy1F8I2wCW6mGc7BMPuNZf030VeQMDg10jXqJL6UCiYRdi9MLDAPnUXrnGPZhX1d_eOpF5HgCcDcUKmkVhqi0gddHY96eJJnqtbLPtw-1mIPROjYatdnIpQFda-ne-JJd3jSrC3zdiXRdb7nnhO3Mbxe2dxnxzJvWwYnhSgkbqffKsWM2Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج رئال‌مادرید در ورزشگاه بتیس از سال ۲۰۲۱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105575" target="_blank">📅 11:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105574">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c140b1799.mp4?token=SfVHXH0YDFrYQul9w6avorAO3PLiW7saWU69LefzDSZWEzgzoaUD7oWeg1vuu7fhB_fHTUSVFO-E-WK2pT4DXQfgS91OU5J3w9JnyQdAOJb11_OlbQ9qWiCxAtD0eYKAF9yo6yVz1a0CIVvSxM1AfZJ---QglyBqIBH_s-qifdVQCJv3SfokK9deN9ixOEGWI3n7NmYAyX2dIv58vIbFMB_57renhHfpCle63s7CGd7gbbh3AlSJ247Gp6TlJ4cO30d1tduBycFkmAWO9Vow371w_V6EpijMv1JmuuloJz9SjWrGJ7ISg6LUXpdI23HQ8kEDOzYri_gMvbI8FwGAWZ4awUdGoDM_9m3-ay-b4uxOAy7v0dNDumt_rCsUJSwyuxTPOd0u1FPKak3b69GZaxtxTxTx0qMdXFhaEEEpShzureR5jo6Ma45rs4nHRoSq1go5bgV-LbOZlXOTi1VUo2sbAZSYWcTlqlQbLNH8oz5Xl3oovL2Y3S3032UKbdobb_qZZUdHzNmqP_2La1X1Y9-_J90D4hLr1DqN7hAoVxrvkwJMkezm5Lu_vV2o2uYetS8YhlR4rn4_bTc4ZMdOGXcAJ_9sJe4aBT9BZsKISlcUe0e4KYNinuB219sHZZAJ1C1GmJ0to5E1ZM7VkD8kjHjpxy7kBI7hqIFYACr-Dm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c140b1799.mp4?token=SfVHXH0YDFrYQul9w6avorAO3PLiW7saWU69LefzDSZWEzgzoaUD7oWeg1vuu7fhB_fHTUSVFO-E-WK2pT4DXQfgS91OU5J3w9JnyQdAOJb11_OlbQ9qWiCxAtD0eYKAF9yo6yVz1a0CIVvSxM1AfZJ---QglyBqIBH_s-qifdVQCJv3SfokK9deN9ixOEGWI3n7NmYAyX2dIv58vIbFMB_57renhHfpCle63s7CGd7gbbh3AlSJ247Gp6TlJ4cO30d1tduBycFkmAWO9Vow371w_V6EpijMv1JmuuloJz9SjWrGJ7ISg6LUXpdI23HQ8kEDOzYri_gMvbI8FwGAWZ4awUdGoDM_9m3-ay-b4uxOAy7v0dNDumt_rCsUJSwyuxTPOd0u1FPKak3b69GZaxtxTxTx0qMdXFhaEEEpShzureR5jo6Ma45rs4nHRoSq1go5bgV-LbOZlXOTi1VUo2sbAZSYWcTlqlQbLNH8oz5Xl3oovL2Y3S3032UKbdobb_qZZUdHzNmqP_2La1X1Y9-_J90D4hLr1DqN7hAoVxrvkwJMkezm5Lu_vV2o2uYetS8YhlR4rn4_bTc4ZMdOGXcAJ_9sJe4aBT9BZsKISlcUe0e4KYNinuB219sHZZAJ1C1GmJ0to5E1ZM7VkD8kjHjpxy7kBI7hqIFYACr-Dm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
زوج فوق‌العاده پشم‌ریزون ازه و اولیسه در تیم کریستال‌پالاس دو سال پیش رو ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105574" target="_blank">📅 11:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105573">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105573" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105572">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv95tEwzBbN7QUBZXQQ87VW7IFRhACc5SumPmGfmwL75Qm6iIhTgCXFU4ReVUrLWZ9Z-Otj4h4XwEjKM3gzDgAU1NcYqTr7Je_Yyac7dDd38CfEXwXGcIFWg2Vlntj2A0_TenrQRjit5UhMHRu22vSTH_s19jyYfNOZacckOa5G4mKQUtogQTeT1I_35czPi-Xb-cdPtX7_ntnQE4-Kd1JPk81HnC8rSQcDWWjPuRoiIUdbbjkkrBV5WNVvvQwgH3ZVJRbrnCqcGkcn9foYP0VB6IsfIdDZgtmH9LMwNzoKXd8JzwqY6GxUxZpdHbnJcwlaz5zIhB95NBqiJT7X2pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
بورنموث
🆚
نیوکاسل
کاونتری
🆚
منچستر سیتی
تاتنهام
🆚
ناتینگهام فارست
اتلتیکو مادرید
🆚
اتلتیکو بیلبائو
ناپولی
🆚
اینتر
آتالانتا
🆚
رم
دورتموند
🆚
هوفنهایم
بایرن مونیخ
🆚
شالکه
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105572" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105571">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c6aac1de.mp4?token=i-NVTaJ36HxGioJzToEn4TpGI2OGjT5RijLJC5_3RL6sc7XppcGI1TGTiH59NRfmLyPtrQk4R2dEDiWAEwQMS1yJg-EZ839xEMpKofJfP1hM-re9TLZrHEFLfKDhhx-pJ1iRac9TrrO9OsLCvBqA2X-hRQhxnJjoVOVYLeJVRJUUOq5GLhOw_Qo04JVm0dAuC8zT-5y-6AzYxmioiNPs1RN67DmGVKEWhd5vGaigSc74oh7vPbiPfsI1lizrajnEqt95ZOlqfJVJEwOEW4IhWH_CX0MRkh02orBAovqq94FcAtWo0KrZ7QSdhVQAMUHE3-LsKeopvAr3jXJHehh3nZdHT1XRw0vgFQJTVLShfVGF5C4r8S_u8Gvvu1rL_1bjtyyEkDWdCjPoUlCgM6-8ccFxUdM7o3J9VZCscS7y6JZ0Jxynec_u3D6wO5PSu4vM70qJXuliwUDmWd4c1UEaNyGdGyQhRIzMiVIZQ-T0PdSboSninubykkkiRoILrw1KSm3PAeIHNo0vkQRfKK8Q141virnObaFQZIRJwddOI-DYqcJtBbh52Sdqzh5muiarMVbWuSIzeIEK0nmXMTu-P1YVZmPrs0wxY5QnPENhVt6O0OvMK2Xybk8woKKeMTaylwgukjKwoDQF2sBcTbRQdpBHTSMdwb9zikSO13PewxI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c6aac1de.mp4?token=i-NVTaJ36HxGioJzToEn4TpGI2OGjT5RijLJC5_3RL6sc7XppcGI1TGTiH59NRfmLyPtrQk4R2dEDiWAEwQMS1yJg-EZ839xEMpKofJfP1hM-re9TLZrHEFLfKDhhx-pJ1iRac9TrrO9OsLCvBqA2X-hRQhxnJjoVOVYLeJVRJUUOq5GLhOw_Qo04JVm0dAuC8zT-5y-6AzYxmioiNPs1RN67DmGVKEWhd5vGaigSc74oh7vPbiPfsI1lizrajnEqt95ZOlqfJVJEwOEW4IhWH_CX0MRkh02orBAovqq94FcAtWo0KrZ7QSdhVQAMUHE3-LsKeopvAr3jXJHehh3nZdHT1XRw0vgFQJTVLShfVGF5C4r8S_u8Gvvu1rL_1bjtyyEkDWdCjPoUlCgM6-8ccFxUdM7o3J9VZCscS7y6JZ0Jxynec_u3D6wO5PSu4vM70qJXuliwUDmWd4c1UEaNyGdGyQhRIzMiVIZQ-T0PdSboSninubykkkiRoILrw1KSm3PAeIHNo0vkQRfKK8Q141virnObaFQZIRJwddOI-DYqcJtBbh52Sdqzh5muiarMVbWuSIzeIEK0nmXMTu-P1YVZmPrs0wxY5QnPENhVt6O0OvMK2Xybk8woKKeMTaylwgukjKwoDQF2sBcTbRQdpBHTSMdwb9zikSO13PewxI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
واکنش مورینیو‌‌ و نیمکت‌نشینان رئال‌مادرید به پنالتی که امباپه از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105571" target="_blank">📅 11:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105570">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
✅
🇮🇷
صالح‌حردانی که دیشب یک استوری در حمایت از سهراب بختیاری‌زاده گذاشته بود، استوری خود را حذف کرده! با این حال سرپرست آبی‌ها به حردانی اطمینان داده که تنها با یک عذرخواهی ساده می‌تواند به تمرینات تیمش برگردد که تا این لحظه این اتفاقی از سوی حردانی رخ نداده…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105570" target="_blank">📅 10:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105569">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf1cf6a70.mp4?token=tbS3PPvlrH2hgzF4va9PJM_ALAKHCH5Doi8lMO6N-I3UM22mosPT4BcW0qlXYfV1GQi5YoH0EK6-knsdpAbsuWa_-IIRPXUKC9RwQxHcfFlqJhMQ8Q1VX6R9TvmFAcWy_x_HDB_1Cm7jAJ9W4cWsQsRb1dG37v-6DYrnq6z8wVHUloHV_lTmUaKe4VoFABEKrznoh0saa-llSJDqcsoEMs0NNZTszMZSz72vCiBEBpiZr84Ih2bTG2vWvMYO3L7Rm9Cu7hQpee3wqXcehFnIM66s57oUB-0fhFNJc1nluqBS-G2wHgcyTN4rZQKWmM2NxtbO3xrayCa9cg5X0Z8R6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf1cf6a70.mp4?token=tbS3PPvlrH2hgzF4va9PJM_ALAKHCH5Doi8lMO6N-I3UM22mosPT4BcW0qlXYfV1GQi5YoH0EK6-knsdpAbsuWa_-IIRPXUKC9RwQxHcfFlqJhMQ8Q1VX6R9TvmFAcWy_x_HDB_1Cm7jAJ9W4cWsQsRb1dG37v-6DYrnq6z8wVHUloHV_lTmUaKe4VoFABEKrznoh0saa-llSJDqcsoEMs0NNZTszMZSz72vCiBEBpiZr84Ih2bTG2vWvMYO3L7Rm9Cu7hQpee3wqXcehFnIM66s57oUB-0fhFNJc1nluqBS-G2wHgcyTN4rZQKWmM2NxtbO3xrayCa9cg5X0Z8R6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
اولین شکست فصل رئال در خانه بتیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105569" target="_blank">📅 10:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105568">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQXZLKOozhID2sbLhADObvbb9RbgrZD2abGubfLPichqQUVvE6jWCKiuTzbIMkEC0EaTxXujMHA5m4NugSEZc8VKFEyF1nwnpLkJNqg0KAnx82Ne_nAUOn5YP-i7daV0InKvbyKlZLO0n-ON7a_H9T4mzrQI3gVtWdSpj2uQOLgnfHGnrNI8nhyKFu564btBDI-kL4YXsXXRf593EntdK_Qqv4ykyg-6QZRzGTMGTQkWL08iSctJKZlokB6A55jYWZ03Na7xKUhvU0PXYckUe_MsiXi1kcYK1z8vihqNcgmiR6ql6-v1_hbfX_HkefRDf0M8B-9nHRMC8vhU5tHYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇫🇷
لوئیز انریکه درباره نتایج ضعیف تیمش: اگر دوست‌داشتید میتونیم روی قهرمان این‌فصل فرانسه شرط‌ ببندیم هرچند که من شرطی که خواهم بست رو لو نمیدم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105568" target="_blank">📅 10:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105567">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0094c6fe9.mp4?token=ugT_ZdSKX7PJVJFQqK1WAkXN5AqSFYiNi4PapeCesbVonwxmdjiZuKZ_qOD22tXF45RE50xFY5Yy0E6v9mKjUd6Umym1UmgfkECABg-DlGESrlyGylTqjckDWyZo-BiGQUHg-tFQRnVnLdBNQQHjTOBoiYMoqqvhZui4K6ZXvf2maJxMjCDBH-0-Tu8mAOTmgxhqn1P2_wajqhTgh2YMpPrUkllGgIgSNz3u9fHseYYLeOeL_S2PYaw4KhHkj7QpPxNCb8Aygc_vfDyNemi0LpFwiU5CwhpBcturTUoH0bxMQv3PifVyHOdbw8WzDELuFwXX4yXyPLibvaU6PwlfLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0094c6fe9.mp4?token=ugT_ZdSKX7PJVJFQqK1WAkXN5AqSFYiNi4PapeCesbVonwxmdjiZuKZ_qOD22tXF45RE50xFY5Yy0E6v9mKjUd6Umym1UmgfkECABg-DlGESrlyGylTqjckDWyZo-BiGQUHg-tFQRnVnLdBNQQHjTOBoiYMoqqvhZui4K6ZXvf2maJxMjCDBH-0-Tu8mAOTmgxhqn1P2_wajqhTgh2YMpPrUkllGgIgSNz3u9fHseYYLeOeL_S2PYaw4KhHkj7QpPxNCb8Aygc_vfDyNemi0LpFwiU5CwhpBcturTUoH0bxMQv3PifVyHOdbw8WzDELuFwXX4yXyPLibvaU6PwlfLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
به‌نظر شما دلیل فحاشی به شجاع خلیل‌زاده در ورزشگاه عادل فردوسی‌پور است یا رفتارهای او در داخل زمین؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105567" target="_blank">📅 10:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105566">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ffae934b6.mp4?token=hZfWXNNeaeofXIO_tZROIi13-iObo-tXe_Hdb1Ej1pPZCsP6zZqCZUjD26S94vI6YAZVRNRh79S0j7WWV5nrUX3vtXAlAB5wzb-iKQADDe_IzREAxI3gboe73WxLH2tQPIaVZBXV4m1nt-5J7L0PChsnNucvfEoRIbEnRKdDRCZwpsLeNfGPPXVbiaLHh9w9blmYsUa4RphE_2D7kPBibcZg3DYTI6NgF1owdEcKTwjHuZXmH2qMtczMEaSI2wz8Idxl1BB_VTmsufHG8h_bZTrBuX38WL-KpmgfCBqV4sS4yhJGM1JUqL74BLuGVJ5X177dxXeYyRT92O1KitYHLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ffae934b6.mp4?token=hZfWXNNeaeofXIO_tZROIi13-iObo-tXe_Hdb1Ej1pPZCsP6zZqCZUjD26S94vI6YAZVRNRh79S0j7WWV5nrUX3vtXAlAB5wzb-iKQADDe_IzREAxI3gboe73WxLH2tQPIaVZBXV4m1nt-5J7L0PChsnNucvfEoRIbEnRKdDRCZwpsLeNfGPPXVbiaLHh9w9blmYsUa4RphE_2D7kPBibcZg3DYTI6NgF1owdEcKTwjHuZXmH2qMtczMEaSI2wz8Idxl1BB_VTmsufHG8h_bZTrBuX38WL-KpmgfCBqV4sS4yhJGM1JUqL74BLuGVJ5X177dxXeYyRT92O1KitYHLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
‌مخ زنی به سبک مهران مدیری در سریال جدید مرد سه‌هزار چهره: فقط اونجاش که میگه برای من منگنه بشید
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105566" target="_blank">📅 09:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105565">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe613df04.mp4?token=VFA_YqFD0A4C84sjJfyFZ801jz149q4d177FABrEgbNTJG4ctKkANLReKlhmn3DwWyMI_CYb84_IklqDFmF229-ApPbwE2cB9r524JJhSI2Bro1QbYddegHTm83fsULu7BqjqQngXatWcKf0itP_qUqsdCi7jm3io_BSzIsnIEIkwq0UAibjaEAjPNBOT5-_DQKHb9kpgA2Cu8GFkQvVN4NKlbByIXWHit1qRVo1ScsiTpEKLcUBSLukemOx37bPj7y8jKEKRbFLETmUzQdeYV-eWty8ZKwu4Apwwn22RSiHy804giY3gGvECpv1UA9nsKTi8sobwHsG2ri0ZflfXJDwFH0Ck7uvER5XbEZz-WziTLQN7pd2lIGEt_9ZMTmlf3h1Inodv70X-0S1AezX0lT35so4D0TKZxp6jUrxu3Nn4AxmP_0vEDkOIr9sXhJ5ZW3cOjJVFPDw0uWnpEW7CEbMjqnV9IrpE6gZsxwE3OKVsm0hR2ScWQ4U1mzTnovppiltiehTd9LX7sjEHINssQDMzlDhLFvqrik6S4aGPa_Pt0nGTfPM6ARKtcyAEcRiUCPzsRTN_r8pjixpjP2n4y3tPNJRwdnTk4YajRTVoIzrdqSd84XGBnWX-fviAlGoNpPqmzxXopcEoJERVxM7y-ypA-mzto3_0Ze57WPrw2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe613df04.mp4?token=VFA_YqFD0A4C84sjJfyFZ801jz149q4d177FABrEgbNTJG4ctKkANLReKlhmn3DwWyMI_CYb84_IklqDFmF229-ApPbwE2cB9r524JJhSI2Bro1QbYddegHTm83fsULu7BqjqQngXatWcKf0itP_qUqsdCi7jm3io_BSzIsnIEIkwq0UAibjaEAjPNBOT5-_DQKHb9kpgA2Cu8GFkQvVN4NKlbByIXWHit1qRVo1ScsiTpEKLcUBSLukemOx37bPj7y8jKEKRbFLETmUzQdeYV-eWty8ZKwu4Apwwn22RSiHy804giY3gGvECpv1UA9nsKTi8sobwHsG2ri0ZflfXJDwFH0Ck7uvER5XbEZz-WziTLQN7pd2lIGEt_9ZMTmlf3h1Inodv70X-0S1AezX0lT35so4D0TKZxp6jUrxu3Nn4AxmP_0vEDkOIr9sXhJ5ZW3cOjJVFPDw0uWnpEW7CEbMjqnV9IrpE6gZsxwE3OKVsm0hR2ScWQ4U1mzTnovppiltiehTd9LX7sjEHINssQDMzlDhLFvqrik6S4aGPa_Pt0nGTfPM6ARKtcyAEcRiUCPzsRTN_r8pjixpjP2n4y3tPNJRwdnTk4YajRTVoIzrdqSd84XGBnWX-fviAlGoNpPqmzxXopcEoJERVxM7y-ypA-mzto3_0Ze57WPrw2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
باشگاه نوریچ سیتی هر سال نشست خبری ویژه‌ای با عنوان "نشست خبری با قناری‌های نوجوان" برای هوادارای نوجوانش برگزار می‌کنه تا بتونن مستقیماً سؤالاتشون رو از سرمربی تیم بپرسن. امسال هم این برنامه برگزار شد و البته با یه اتفاق ویژه همراه بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105565" target="_blank">📅 09:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105564">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01f66133f.mp4?token=RKF0LYhCK0KT65inccAs7QoRN5T96JQnkyh5CLFy6vKo2GMGBVqub4NLON4WH3N6xL3iq1XEFM9ehnEek2RWGnsV0D8XHnOHW4ENU8StJry60AGF3C-gZHVurcRO1NhkmhNk8YLI6uyqfd-A2w_JXwd60ih9SjG8V9sQLWBMbDMWC6C19edxkGmWKvJq21Nac4vlQz4AzIF4qfyQNRN1344px0-qAUI4K1fJzdjFAHMcQ5_8elMTEj_ZPGy7w9VhefqzGlkwyPdT6Z-5jT8h_eCCLA6tqCPAcT0yHRfbapl3-xaroEoKtUR_hEK9pSv7rXLAC-olmcWM5dGLL0hRuwgS1H9bntGFMNalkZLOhkRE7EETbEFQLCv88VnxuhrRJnfiFTVwsoKMfCV0D0UZ_AG86-zQTcaTJI62Yb6naRWpCbMrD_ltqRqVMxHYYbKFcHpLLBdkr6ZmEVqU7elGWmBPzcuu1VF-yP1yA6sD5hV6JTvw63iIl0IX5KSuRZCbZiavTqFCbcgqGLDDminy0DJAMYn8fNCVlVYQ2F-6T4HrZCqNK7Gc2fj071uGQpn045TjdxfuQ8xzhddjONVBjNHhH1YKy17VmSM9sqKcpXBE5mYB7HbyBR9u5nZkkVdF6BH6GnpHAvEniS1kUR2WDd_spL-Z6G_APjLYJWHzBkU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01f66133f.mp4?token=RKF0LYhCK0KT65inccAs7QoRN5T96JQnkyh5CLFy6vKo2GMGBVqub4NLON4WH3N6xL3iq1XEFM9ehnEek2RWGnsV0D8XHnOHW4ENU8StJry60AGF3C-gZHVurcRO1NhkmhNk8YLI6uyqfd-A2w_JXwd60ih9SjG8V9sQLWBMbDMWC6C19edxkGmWKvJq21Nac4vlQz4AzIF4qfyQNRN1344px0-qAUI4K1fJzdjFAHMcQ5_8elMTEj_ZPGy7w9VhefqzGlkwyPdT6Z-5jT8h_eCCLA6tqCPAcT0yHRfbapl3-xaroEoKtUR_hEK9pSv7rXLAC-olmcWM5dGLL0hRuwgS1H9bntGFMNalkZLOhkRE7EETbEFQLCv88VnxuhrRJnfiFTVwsoKMfCV0D0UZ_AG86-zQTcaTJI62Yb6naRWpCbMrD_ltqRqVMxHYYbKFcHpLLBdkr6ZmEVqU7elGWmBPzcuu1VF-yP1yA6sD5hV6JTvw63iIl0IX5KSuRZCbZiavTqFCbcgqGLDDminy0DJAMYn8fNCVlVYQ2F-6T4HrZCqNK7Gc2fj071uGQpn045TjdxfuQ8xzhddjONVBjNHhH1YKy17VmSM9sqKcpXBE5mYB7HbyBR9u5nZkkVdF6BH6GnpHAvEniS1kUR2WDd_spL-Z6G_APjLYJWHzBkU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
بیرانوند: مردم فکر می‌کردند این آخرین جام‌جهانی ما باشد. میخواهیم در جام‌جهانی بعدی هم باشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105564" target="_blank">📅 09:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105563">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf296c20c.mp4?token=vln6TfZvTaksWoYWTyIhW0EaNWuTEhnw-tv2EHgHOuwbd-iKh1UnAydXIBMhJwiDl8GYm9zcoV4eaf0c1IgSJ8A8kF6lyZr0K9UEX69ifFr8jOiNr5RRCwJbOQy4wxUifjVwsNNoAvCHFaL2l0mwRPbnbwsrPaHuRUt0NXUDEx-3XFz7kfNX3xv8Ll0pt04aW1iNX2Vgmp4ryAqSCfe__PBblKMjoMTxkdn-LNsHy2Wk5Fa8u-KVPdO78HIlbCAS9xoCYXSARucF0UID7SwLjTSnKHIy-2QUHQYxrz3KouxZ6vnWqoLZJX1v3UmLkjZWxKwgt3bdHu4fyENoze0OFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf296c20c.mp4?token=vln6TfZvTaksWoYWTyIhW0EaNWuTEhnw-tv2EHgHOuwbd-iKh1UnAydXIBMhJwiDl8GYm9zcoV4eaf0c1IgSJ8A8kF6lyZr0K9UEX69ifFr8jOiNr5RRCwJbOQy4wxUifjVwsNNoAvCHFaL2l0mwRPbnbwsrPaHuRUt0NXUDEx-3XFz7kfNX3xv8Ll0pt04aW1iNX2Vgmp4ryAqSCfe__PBblKMjoMTxkdn-LNsHy2Wk5Fa8u-KVPdO78HIlbCAS9xoCYXSARucF0UID7SwLjTSnKHIy-2QUHQYxrz3KouxZ6vnWqoLZJX1v3UmLkjZWxKwgt3bdHu4fyENoze0OFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🔥
جورجینا همسر CR7 با لباسی از برند گوچی در هشتاد و سومین دوره جشنواره فیلم ونیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105563" target="_blank">📅 08:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105562">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105562" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105562" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105561">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN30SfnMt9z9wd-Xf16D5qP5FIsdcbB7m-cAWZbXfTZsTcnTIxEsTX-eneiJHvN4UMM_OX1Yo0sYkaipdQlrFmvZ5zNxRS2-OLzB--e3sChd19aiqFvDkqLTkD9-1M1OKOFFW1dxoVnRfKs8Y_s2jDVhIQ3f4K2IbLn11qPN8R2TU9BPXEz-LlcVtJB8GPll69v_QIaAt4OIoP1xdtvnDVUlu9V0DZClGjtdzfbeOlZQRVbAfuRBjheq-fbOekA0h5_pRKwxKhfiMP9P3Am4umV5-Dz8cgFKPksF4a9KpjGWDCBDEjHG493ZiYHMc1dyUigJTHfbVlVVRnVeJZcpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105561" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105560">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105560" target="_blank">📅 01:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105559">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b6612a039.mp4?token=u0WLylGMoTwaU6kCHeRWkENMMEU9f90TZOEkbdLPyfXPy21xPOYWW9DQbVp0wpZXWzhbu3Of3ktA2Z--xiGpO7jJAMYh4Meg7cH5WH8sDZ_DR4QUXq0Ks4UN28_CIVCAonLYMwAJ5Xee9S3ju4NxFQELUbgiyIVRvUmqi35hcdjy2R_px23QIGhE40fgvXhwrrUYQxF3YXs9rVE0V6zdLib5xuJPQOaY8wgVy6os57WeN4gIu5fuToXxvFnxpcnOyOfZ3ZDyqaJ0PMpOqbcO7fQMZWsekPZ2ul3TcvXoW61AsnTaQbUh1liT5rMWh87lWK3RjsRLYU30LuTJFdP1LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b6612a039.mp4?token=u0WLylGMoTwaU6kCHeRWkENMMEU9f90TZOEkbdLPyfXPy21xPOYWW9DQbVp0wpZXWzhbu3Of3ktA2Z--xiGpO7jJAMYh4Meg7cH5WH8sDZ_DR4QUXq0Ks4UN28_CIVCAonLYMwAJ5Xee9S3ju4NxFQELUbgiyIVRvUmqi35hcdjy2R_px23QIGhE40fgvXhwrrUYQxF3YXs9rVE0V6zdLib5xuJPQOaY8wgVy6os57WeN4gIu5fuToXxvFnxpcnOyOfZ3ZDyqaJ0PMpOqbcO7fQMZWsekPZ2ul3TcvXoW61AsnTaQbUh1liT5rMWh87lWK3RjsRLYU30LuTJFdP1LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
رفتار سرد مورینیو و وینیسیوس بعد بازی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105559" target="_blank">📅 01:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105558">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPS3tsNPuZMk4KWG_RFpOqaFEL-74eV95b39-zKJXfnHekbd0NPkLDsljYfZ5ElRYkEYd2zWTD8xR6k36ZswSnO1JnZ6uAh_Yty3y691P0ztLlsCOOMeHCkQP8rxrIkRHyI1Ikqlyi--aMnHzhYJRaJaOGjV1XQ3bshiP9vJPnR4S0YqkvdTgY0K-LY5palqvPnoSzienqluffrfeInkTcsxhzLmcHlOeuep7mjyCb8vMU4JAe-9_DjJp-Uq7Qtf1axtFdMGNdiSTnwUczZn0-vcUaky5hk99Z84f1gsPy3VJhzDNpSq0ac2gpmZ3BUx1EMWsauJhXkX2_LLAGnj8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
#فکت
؛ در آخرین‌فصلی که رئال‌مادرید مورینیو مقابل بتیس در خارج از خانه باخت، آخر فصل بارسلونا با کسب ۱۰۰ امتیاز قهرمان لالیگا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105558" target="_blank">📅 01:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105557">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmm-oQGdycOXrIYqG0_BpIRNVR6KgiZr4VXdxQeKt1GbdtihnYVxEGdt0AhHLGF_B4n6yMBterpzs_K76Q7YlK0XxassLYpsSQA8_KWHfgZ3aP6m0NWHvWdW2mp6sxr8FizP7EqpLlZiz1maGnKrfP01bim2shROXuQecbp32C8sMDkIbWugnkTZGFyrmNMzNjKlHMtOlCP0hzynf9wmoM2pBmctTiEMkBUhLZcMgseTlBmVl6UqrwhBZN0mO0IOuqXPmkidr_HMihgPgqKRq03Sax8OJtIkKAUXhH3xJLaTjcvQD0igPZ-MT-tGsCt-NcQ6U3DdXvmPc6sd3KS8lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
ژوزه مورینیو: عملکرد داور بنظرم مشکوک بود هرچند باید برم بررسی کنم. تعجب می‌کنم چرا نیمه‌اول به تیم بتیس حتی یه کارت زرد نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105557" target="_blank">📅 01:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105556">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d903ez6eTC5DYuyDCI8NwotSOJepmJHH88cF4PqffM00OnyPqg8JUDEGEgtrnjPOOl4BHGzsmry-aQYEik4jnrOGEZj3YaGZMmh1uE3PBbtJRlbf7KEBFM7F85ZLmN0l24PvI73bvnvXvrZA-YaNq-v0DmzBhZ-qwo_GrM-gGcQk9_-pDDOciMfSCvGlT-5nVB42K_PX9_XAkDuToemc8QLcEn3e6kyv1qkViPxr3KS0xKlP3qVncs3DZnIOkwcug2WokFuD8VAG2WKKVUTdwLSLXc83um8zH0G2-OTYKNIKMSRHB6Ts9uyg_GRe3j-RdnlOH7SwXW7C-gR24fxHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وسط ریدمان رئال‌مادرید گویا باید از اونور یه فکری به حال پاری‌سن‌ژرمن فلک زده بشه. سه تا بازی کردن دوتاشو مساوی گرفتن امشبم باختن! گویا اثرات جذب فران تورس داره خودش نشون میده
🤣
🤣
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105556" target="_blank">📅 01:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105555">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK4qCPo0fEDiDojnXbe6W6CjRQWMM_zMFov66Pu-k19TV2juFPv2bWkzfXgyjXGYaLR0Je3AZdHgIVPqfPlV2pusuTuI0zE9C285Ly_vjB35HSP68ctcAkg0EJ5u07EU2LHnDjJf-ViZwR5K8uVv6ueqxEuHRroC5bUumB3op2VeTGh5j_Nvy11vNfSQoP2YvRdCW0ASgCEK3tzplgRY0wQuKYv0GH5Af9NxU6q5aYFp19X0IBFsfX6ePo8R9Canbn94M3GOVCJHjiQniTczqKr_I-yUww0cMlEl-dmUx9Vd_g9Wx_d3Bgo8FFeaqVxslBRyMTSVDRjFN0alS_J7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
ژوزه مورینیو: عملکرد داور بنظرم مشکوک بود هرچند باید برم بررسی کنم. تعجب می‌کنم چرا نیمه‌اول به تیم بتیس حتی یه کارت زرد نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105555" target="_blank">📅 01:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105554">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🧕
البته گویا این صحنه هم آفساید شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105554" target="_blank">📅 00:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105553">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoUbWy_2lcFInXNkCM_LOuKq6xp8F-z8ADnGaFmc7ak0tTJGoHIyWaK8uj87XraP4aaMJmXQwOBwDTO7Agz5b6puosyUhpykvAOcXk-h-Z68ifkvtBlg0xr4liuiOb74DFwhUCnQQtYvIEubrwpulvwm6B0u7gyP1YGZU3i-8ms8fRU5e7jAIjQWcHRiN-0Fp-s3TUhVO9PQz82h2YAdYjdMzlQw1mNHoQOJdFNIuinhYbByhr_u9o0lRceGjj7BbkcnHMdaBl25YACBcLGxaUMBr4V1-dnjDU4_QneA5i4cofr5Dj4Y-_AbcSoABTsuVJnm7w1UHLLQcQ7kD9piBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🇪🇸
رئال مادرید در پنج فصل متوالی در لیگ، نتوانسته مقابل بتیس به پیروزی برسد [سه تساوی و دو باخت].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105553" target="_blank">📅 00:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105552">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWnk3ZaFMNxm79v8m55qI0_cvvj_zVJSrnW3J0x7MHPxQSRhN67rUIWBDqm4VYZSdetN9amGkkWD-RIdRWPCFBPcuLmrpNNu0Q_psuupLu993ZyNcypXwBh0U1-84-uX2IQCk_ESTXyHCQiAeZ4FWd0t3oGntVZmB8r7nHNmoIORi1Toz7tYy-dTSPx5IN-52T1U0anSh7Lv5s1iaQ_EDGHPIloCSZNJ93_ExrdeOQh72bFULRxlej02z95V4sdP2ieX2dLONk8ePSQc9fGh_8Pv6anmNTGD_XMh5aILQB5rfLTPrWUPSzu-VNUjBqL__Zi3OpZ1RcGM1euSQhCBbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌چهارم لالیگا؛ نود دقیقه نفس‌گیر در خانه بتیس؛ رئال‌مادرید با زور پنالتی هم به امتیاز نرسید؛ پلگرینی مچ مورینیو را خواباند!
🇪🇸
رئال‌مادرید
😏
-
😃
رئال‌بتیس
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105552" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105551">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdSSoMXBj1HAmK0d_KGXdKtizDqAHXsdwcnoGlhLdny1G4VQeH3_zbpFXrxA4EEDFr0wCjn2zllWug8QC-v7dm6XyvzFflvdekda23cnkwe0hInMRq0Tsk8MvHqV4h2uixba2SPkh2Y48CbewtXkIxe7OXmZRcMD1mXRwQ9I1cKoGQcM1CxOsGKqWhkvPj7Sd5ENPfRQx_Cp5fymwnREgYdzmBLQrCuK3qcTsDAfVs5z0xqqGzU-wF722M0LDtldLTiBq4nNgzox85rljAR9RLQSYbLjVCT-SJD4UDhY1s90NYAChcgi6TKA4QL5YBoLWm0aMad62rMOpPIyd2fHxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌چهارم لالیگا؛ نود دقیقه نفس‌گیر در خانه بتیس؛ رئال‌مادرید با زور پنالتی هم به امتیاز نرسید؛ پلگرینی مچ مورینیو را خواباند!
🇪🇸
رئال‌مادرید
😏
-
😃
رئال‌بتیس
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105551" target="_blank">📅 00:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105550">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
داور میخواد پنالتی رو تکرار بده
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105550" target="_blank">📅 00:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105549">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AE6jfLixIJt-yaneNJOWSXNSiZgDjKiOTCkrN80xcavxW7RjBjdRR8wEVz7YWLatU9DC-nldIFcbMx7ovJzENK153dzNq9ihWgjPsdOFkZC5yJwNshgGnbDwPVXvbegT46DJljEjmWga1vJ_-_fV0IkkRPEmTQxzDDLiaEKoHLP1eN-EEVOCh5s09gVTSa0v3OPkzmkN-EjDuvzmjHC5li5B7FNPjzFP-tNZsdaQCN_Z_m9Llf8hvAy0bUf2FjIGls1spB4DBChlgm8gvEhFWeRpJq7VK9fHUpy8e0s3qpxgi0MxLuR44lyJYwYG2K1gp671RMVUGzwkmKLcskTc3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
داور میخواد پنالتی رو تکرار بده
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105549" target="_blank">📅 00:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105548">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رئال‌مادرید بدشانسسسسسسس
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105548" target="_blank">📅 00:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105547">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وای خداااااااا چه شبی شده
😂
😂
😂
😭
🔥</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105547" target="_blank">📅 00:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105546">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🚨
امباپه ریددددددددد</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105546" target="_blank">📅 00:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105545">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بدلیل خطا روی وینیسیوس
😐
😐
😐
😳
😳
😳</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105545" target="_blank">📅 00:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105544">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">برای رئال
😐
😐
😐
😐
😂
😂
😐
😂
😐
😂
😐
😂
😐</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105544" target="_blank">📅 00:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105543">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پنالتییییییی</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105543" target="_blank">📅 00:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105542">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tV-nDXJnkToX0LF1sP99Tqo7VutR6U-Z0CTDyVPsJpn2yaDgl2s9J1PMWWPcyBgCTeXjIOaxJHJSsTfoe3ng8fxyam5NNf699jxmkNFXn2SHx1AXHAVvMhytB8J3WRJwl4zQSCt26C0jq7CN1bqJFXcoLb7X01u_pfg1t9XD_1xB3piu_1kSkL9V_JYLebhf-PH4Gp155a4USFjTmVoQmjfOn-haJ7p3EnmiFKzvFbai99Duqg246saCHckISl-supO-4TWGUSUXjg0HUrPAxjY2lKackuXJqyZy20Jh5iYhVS3GiBRI7yYm9PumSOqrKo6Vc_et9bSe4OtbS7oMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آفساید ببینید و برینید
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105542" target="_blank">📅 00:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105541">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🚨
۶ دقیقه وقت اضافهههههه</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105541" target="_blank">📅 00:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105540">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7IFkEytNs1wvGrW_mzSPxlfZyhI5B6zJ1Sut1lk8p1Csemy8d9Qg5r-cub85pOkM__Ue7nVl6MkB31OFiBpLfX8qzZ0ZSvuVYsc92CXTeqKG_YbUxjelLQ7JQkxDxUMxJRywbnHE6nDgYAZC583oxGL4jI4KskQSH0rgfoSBGowi6zylOoBIIT1bHpE5Dxl9rb2Kvg3rcFyCFI-E2_RTupq8H5YcGWnO4haKe-Uj0nxlvyLxSZAQWH-bRq3bbXBMxT5vb4ETVQ_H5ScZL-Ud-7IF2qVlkpth-lab9kZarJ6fELkbk7LhW2CAvhYUM0VsmaSSX1MAeD3aju1xb4FfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفساید اسپییییییییی گرفته شددددد ریدم حاجی چه صحنه‌ای
😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105540" target="_blank">📅 00:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105539">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🧕
آفسایییییید رئالللللل گرفته شددددددد</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105539" target="_blank">📅 00:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105538">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🧕
آفسایییییید رئالللللل گرفته شددددددد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105538" target="_blank">📅 00:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105537">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اوه صحنه رفته وار</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105537" target="_blank">📅 00:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105536">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اسپی نگو سوپر بگوووو
😐
😐
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105536" target="_blank">📅 00:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105535">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رئال کامبک میزنههههههه ببینیم یا نهههههههه</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105535" target="_blank">📅 00:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105534">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چه گلییییییی زدددددددد</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105534" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105533">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پشماممممممممممممم</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105533" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105532">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سووووووپرگل اسپییبییبببببب</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105532" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105531">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گلگلگلگگلگلگلگگلگاگا</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105531" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105530">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رئال تیرررررر زددددد</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105530" target="_blank">📅 00:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105529">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105529" target="_blank">📅 00:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105528">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اسپی برای رئال‌مادرید اومد که گل بزنه
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105528" target="_blank">📅 00:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105527">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رئااااااال ریددددددددددددد
😂
😂
😂</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105527" target="_blank">📅 00:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105526">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بتییییییس زددددددددددددد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105526" target="_blank">📅 00:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105525">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گلگگلگلگلگلگلگگلگلگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105525" target="_blank">📅 00:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105523">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e62db78c19.mp4?token=n2zN-6_V7xITAowFc90Hq5WlaEIiGkdzO6p379Y5Ztl83azNZNdvCVPAc6DZvXHUaXfshwlIMRvP3Zr1Faa9fFLRc1XlncquJjXDGfoR6aiVkjoc6uky-JzbPwuiF_uB6yFwIpX5QvO-ja0f_atZwJKl0DBywqrULXgxwjQULkkJomkq6Bh79QlzUKBDYChDTS4ZLwtZizU4fmuDrtLODOlyCqbqXDBsAaSAmiLEh2mlBR7Cix6GtzBYcUuPhTc9KdIY4DNhwvwURlGezfMfidR3vB3Xb6GM4mJbLRI4ad-IlqklA5jdTte5Oj181Ez2xfE5TztyLSY65daCo_01hnkZkvLHBBUqoQ-P2b6nnwns59FS-BV_3VxRZyzf0BE9Bb403nKwpSKzDjtLorSJioAuS2rjH692aZE6UzwS0o4VA12LCjdZ3XLnPayLBU89waOyPWxjJu1So8ctZ3CEAgks4NzUVZq-G1f8aB9oT_n3WSVD3-IO9pumVzvNhrhLsgZX2MUCJFV-bTVhVEsR1_I3kmt_MSICrFq2XNvlZkBBT-C_8pZFbnq4_ZwXijmqI1sbLLE78u1MBCmH3P2dZc6p8X-KzXQ_MoQIhz0M7gtIj-oWs1fM500BuN32vLPST_VeWE49A-AstEh8rxhuGoHBKJzFSOoUjvq2H2mgtKs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e62db78c19.mp4?token=n2zN-6_V7xITAowFc90Hq5WlaEIiGkdzO6p379Y5Ztl83azNZNdvCVPAc6DZvXHUaXfshwlIMRvP3Zr1Faa9fFLRc1XlncquJjXDGfoR6aiVkjoc6uky-JzbPwuiF_uB6yFwIpX5QvO-ja0f_atZwJKl0DBywqrULXgxwjQULkkJomkq6Bh79QlzUKBDYChDTS4ZLwtZizU4fmuDrtLODOlyCqbqXDBsAaSAmiLEh2mlBR7Cix6GtzBYcUuPhTc9KdIY4DNhwvwURlGezfMfidR3vB3Xb6GM4mJbLRI4ad-IlqklA5jdTte5Oj181Ez2xfE5TztyLSY65daCo_01hnkZkvLHBBUqoQ-P2b6nnwns59FS-BV_3VxRZyzf0BE9Bb403nKwpSKzDjtLorSJioAuS2rjH692aZE6UzwS0o4VA12LCjdZ3XLnPayLBU89waOyPWxjJu1So8ctZ3CEAgks4NzUVZq-G1f8aB9oT_n3WSVD3-IO9pumVzvNhrhLsgZX2MUCJFV-bTVhVEsR1_I3kmt_MSICrFq2XNvlZkBBT-C_8pZFbnq4_ZwXijmqI1sbLLE78u1MBCmH3P2dZc6p8X-KzXQ_MoQIhz0M7gtIj-oWs1fM500BuN32vLPST_VeWE49A-AstEh8rxhuGoHBKJzFSOoUjvq2H2mgtKs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
مهدی توتونچی: کاش به جای علیپور، کنعانی به مانیکور می رفت!
🎙
وحید فاضلی مربی پرسپولیس: ناخن های کنعانی را مثبت می‌بینم یعنی او تمرکزش کاملا روی دربی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105523" target="_blank">📅 00:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105522">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d308caf8de.mp4?token=KYWvz3Pwjs6eVG7jrgx4UPLGHPc-DAgZHd9qtyNGdMxqZpUL31Xxywf1lEqiQP9OGTSre1xoMBjA5Zk6xXy30WGW8JWVbXnBRVH7lBEdaZN4qWYUpQRsjj6X3lP4M9wx6YlIp0C2JkthwWFzo-1NC5JNXXHU_PwVuL0sRTxyk_Xmdzsx7qqQi2RJMXeLkXFsRcbIRvPYRAC6r2jDL1VsM3KgG4-HKGlFUTNG8KAIg4FXR4W4S2xJ14mWCA_L7kmAkni2S3d-wqQxT2_AHjhDOPxWyarNdYhEEeZZNXY7ZL7CtUkXPd5FnA4ErbPJPOkatKix6unI4c7iAtLWjryjgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d308caf8de.mp4?token=KYWvz3Pwjs6eVG7jrgx4UPLGHPc-DAgZHd9qtyNGdMxqZpUL31Xxywf1lEqiQP9OGTSre1xoMBjA5Zk6xXy30WGW8JWVbXnBRVH7lBEdaZN4qWYUpQRsjj6X3lP4M9wx6YlIp0C2JkthwWFzo-1NC5JNXXHU_PwVuL0sRTxyk_Xmdzsx7qqQi2RJMXeLkXFsRcbIRvPYRAC6r2jDL1VsM3KgG4-HKGlFUTNG8KAIg4FXR4W4S2xJ14mWCA_L7kmAkni2S3d-wqQxT2_AHjhDOPxWyarNdYhEEeZZNXY7ZL7CtUkXPd5FnA4ErbPJPOkatKix6unI4c7iAtLWjryjgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📰
🚨
📊
آنالیز دربی پایتخت توسط محمد تقوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105522" target="_blank">📅 23:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105520">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwIextjJomOn2YMcQa4Gtqb-4MWb1IPdE7xGCmwegr53c_Rl0q2RkLmBbOhyjHBqP6RNXLpOiVkZBFSZinJlxhSQu4O0QtlQ_nRzvtYenxQBcvloPrZBlX-dBaPVTDHH2S2YfBjDr4lh09gvYhnrpYhKVjuf4uyovalw7rJ3jL1HKZCS12LzrNl58lc2QpmuY3FzBAcV3nwQvJVb5GmbI0upxZ8ibyRobYHjwp1ayGQdUpwPiUgv1PCFi4keAjit7iIIUFgM05fAcd_k9l827n2l_t2lDQB39y1RW8wc9M3TaPG6Gvk-qjbWgPZ5O2ASzRHRwWuOxW2ayOL3U1996g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
برخلاف شایعه ساعات اخیر، عارف‌‌آقاسی مدافع استقلال دچار هیچگونه مصدومیتی نیست و در بازی با آلومینیوم به میدان خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105520" target="_blank">📅 23:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105519">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFlAo_Y3413XBQBP4zQcehyob-L6eXJL0epJ4zir274sCtCNtLqKdh0iKARrKsOfUqFtWIuhKbTAubdDM2ARbT3qupkd6kMO7pbAilZaDMCGgDC-1tkb_rSJBFMuN1etGyMk7uQDyEw02CJd1jLBL75Zc-voUWb-R5IB5XmdFNOy_uDI7ma5wmNfawGxK-62g_qCZLKwSdw_MlOwkkloXhDfPU_CzQiK3yAqbQF6pxsKl043bG0ZX5AlHJp1DjTCrDIgOEOUbc9Q4pzeuE9TO5TtttWK0J_3ZiaK_Ont6oPfkRfs73regWQgwTCqgAlYwGptkRjnq_DA7qvIvd5V_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇮🇷
استوری یاسر‌آسانی برای صالح‌حردانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105519" target="_blank">📅 23:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105518">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1298395760.mp4?token=NwTcAFmBNn4Ncby5POynRUgm1jnjBoGIrsLulU_lalo2-Bz7eFwxrLzKhT9lr8zkJSeFhz0YMGbB-qb5IbFBP1EiHqg-_P9bKrVt1WUT1odrOp66mGjUJbc1Ei5Cpk040mvRv0oMCiO4zNvnSeEN5NQgaVXkqeqWzm3Vbg4_mvP8TJt_ra3HGe5r-47kKYqcI97wHTlNKDnpJFRJ-8lXRB792xYDY6YW47vHHOex8_7-hszTK5cjod9NlzZy8MeR_Kwxh6FldVap6vQgVZMEMvFCaEMeJwz5RaXXfVqG_3vcZetV2aJO-YCB6KkkQq2VH74jdP4q0ZcoqTkDYKyGqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1298395760.mp4?token=NwTcAFmBNn4Ncby5POynRUgm1jnjBoGIrsLulU_lalo2-Bz7eFwxrLzKhT9lr8zkJSeFhz0YMGbB-qb5IbFBP1EiHqg-_P9bKrVt1WUT1odrOp66mGjUJbc1Ei5Cpk040mvRv0oMCiO4zNvnSeEN5NQgaVXkqeqWzm3Vbg4_mvP8TJt_ra3HGe5r-47kKYqcI97wHTlNKDnpJFRJ-8lXRB792xYDY6YW47vHHOex8_7-hszTK5cjod9NlzZy8MeR_Kwxh6FldVap6vQgVZMEMvFCaEMeJwz5RaXXfVqG_3vcZetV2aJO-YCB6KkkQq2VH74jdP4q0ZcoqTkDYKyGqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇷
🇮🇷
آنالیز زوج سمت راست استقلال در دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105518" target="_blank">📅 22:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105517">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-XYkZAHi-USDA4tSOddD44EJRQ9uZ7480X5x5q6bB2LM3z8tRectoGG8JV2SyPKN5ulZrWep8Xby1rj4c7INamUJJ7oplCWCNz1hytxW5bXny46yJVoezAzpumefLjjsa-uCQTXfMFfmM2Hb_SMyA_-553MoGw0D86OO9uHBapqFgqzjW57GZPGVY9yIrFrszR_lYZY-6WlfEszSzePiALPX4lhJuwMcAXvJKyeRJdYq0uY9T5hr_g8gILfp-pjNUkQnF-Sb1xMNK5BN7fIO00ij50pHINyt9hHRe1woJKl3NC4mvefZWDcS5C2ekiA4m9oWytTzqnryc5kxXxBEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پاری‌سن‌ژرمن قرارداد چند نفر از اعضای تیمش از جمله لوئیز انریکه و ژائو‌نوس را تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105517" target="_blank">📅 22:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105516">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d0b4fd3a2.mp4?token=JwogUXpU7XYSqGEDqAjEU-WqwtEdiBcsm2hmz_2312hcQjTYz7Una8wXYvSCVTJscjMJmdJRClv6rKe1q0ixuU21GzkHB5aDQ8Mq-UQRRmSydalYAZYLxyuMd2sM8nQnZdtNgponwHJ3bckLIFt_nhLw7I6VWCXDaDvbyFcWIJjUGom-SE1X0Z4X8Z3BlSdoGlS4WdTzBR1SiQ6YZPhYBVZzyE2ERoEXqzE5LZjJMWu1vmrNcTAHlBCEeyxdNd-LtDsGvhj_ulJ6asFw8wUsYiig1cruN8Zka7SPJqxOb1qAB7Q-CuA63V0T-TdSuZtrBKXCjbxLq8PST97spNDu_CHeYkPP1JSAiEBbb0LP4Rk2tE6olEEFvNOc8ryWUhsaubuwGRE1W4vLchBsg7wr4B0fd9krhBI9IkLcLov8EWgabaC-6W_HJ4dTPb5RE__sTrQNimh5N6ogmXW9F06SgYH6iHNRc2faSbZ_HAyIt8j7XQua_OXOPfIfejW3Z4wYKBsExSNU1_HirLIs9nMnD5gVpHMBu1sty9cyP-vxw0TRMKWqJlphhXwBcYy5fJThRMVK-QEfftYFYkAcFLVnr2rdWBkqh4j8uijQy5LPGsMchQP4gJYdB4w3Cwk4Hsz3Sb_GBl39ft0MI0axH2rGHVWHsBHI1K_BE4rg3_diZsc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d0b4fd3a2.mp4?token=JwogUXpU7XYSqGEDqAjEU-WqwtEdiBcsm2hmz_2312hcQjTYz7Una8wXYvSCVTJscjMJmdJRClv6rKe1q0ixuU21GzkHB5aDQ8Mq-UQRRmSydalYAZYLxyuMd2sM8nQnZdtNgponwHJ3bckLIFt_nhLw7I6VWCXDaDvbyFcWIJjUGom-SE1X0Z4X8Z3BlSdoGlS4WdTzBR1SiQ6YZPhYBVZzyE2ERoEXqzE5LZjJMWu1vmrNcTAHlBCEeyxdNd-LtDsGvhj_ulJ6asFw8wUsYiig1cruN8Zka7SPJqxOb1qAB7Q-CuA63V0T-TdSuZtrBKXCjbxLq8PST97spNDu_CHeYkPP1JSAiEBbb0LP4Rk2tE6olEEFvNOc8ryWUhsaubuwGRE1W4vLchBsg7wr4B0fd9krhBI9IkLcLov8EWgabaC-6W_HJ4dTPb5RE__sTrQNimh5N6ogmXW9F06SgYH6iHNRc2faSbZ_HAyIt8j7XQua_OXOPfIfejW3Z4wYKBsExSNU1_HirLIs9nMnD5gVpHMBu1sty9cyP-vxw0TRMKWqJlphhXwBcYy5fJThRMVK-QEfftYFYkAcFLVnr2rdWBkqh4j8uijQy5LPGsMchQP4gJYdB4w3Cwk4Hsz3Sb_GBl39ft0MI0axH2rGHVWHsBHI1K_BE4rg3_diZsc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هوشنگ نصیرزاده: هیچ‌کس نمی‌تونه از آسانی شکایت کنه؛ افسوس از این اعتراض‌های آماتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105516" target="_blank">📅 22:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105515">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf94f3a1ca.mp4?token=MIyogdMc7WIG1FbDXlSiqQdjTM1vVI7Gqn9xRCteXVFtD0Jglj5QC0QZMDlbNfypMDu-pv6eZnItYUEB7gGJt0Glo0xE4jGLCNj3tqNmfFQaGIW-3eD3YDKfzvLfATbNuWkvvHSn9DT1HzDG4NReRtahsBwiXshtp5R8iv2WZyQ6F6dGrRW1jwaaS42eanhEG5JbenvpR5C4PGgHrZhOhcpgYyvtw6en1lbmP0ugK02C7BzNS7_Y0mJV9Y-qeRFMXNLy1HgUZ6QOIRtwl00Hy2ZPWLGVTedD7k8M_J7RYXuh4Ew7Ul4t6Z8Wl9V5O3n2Whhb1zrx-7PKPvA7s9pxEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf94f3a1ca.mp4?token=MIyogdMc7WIG1FbDXlSiqQdjTM1vVI7Gqn9xRCteXVFtD0Jglj5QC0QZMDlbNfypMDu-pv6eZnItYUEB7gGJt0Glo0xE4jGLCNj3tqNmfFQaGIW-3eD3YDKfzvLfATbNuWkvvHSn9DT1HzDG4NReRtahsBwiXshtp5R8iv2WZyQ6F6dGrRW1jwaaS42eanhEG5JbenvpR5C4PGgHrZhOhcpgYyvtw6en1lbmP0ugK02C7BzNS7_Y0mJV9Y-qeRFMXNLy1HgUZ6QOIRtwl00Hy2ZPWLGVTedD7k8M_J7RYXuh4Ew7Ul4t6Z8Wl9V5O3n2Whhb1zrx-7PKPvA7s9pxEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
ناراحتی محسن خلیلی از حاشیه‌سازی هواداران پرسپولیس درباره اوستون اورونوف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105515" target="_blank">📅 21:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105514">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tANYt4Zad3Q7mNhwaYALrdPGeIBIAHtJ-k2egI4yjubwWzybhDeAgczrBngeUBxOx43mOUDsetzRQksFIqcdpbW2xig8d3EB1Xk4QA8dbk0qaIw5zDGvMuoRf_0w1n9NrXKAagWPMvvsGcQCAgt3sJgN9X68s9-_KFgsZ7qidHJMMMEoWV7Y6dCLEgfGFS1bgY3piXAdd8IBPcMvJCAaJY1KSFwAcnc_FxJKtzqq56-uwdtIJj-2l-wNiQb_Gz2bie7aYObUWwzL-iwtsrdoBwOHWVQYoeTYVSd0XzPd48K9k3S6zHjJLja03Zt_-zkKOdBAXKqE_jZ9HtTqiLiNLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
ترکیب رئال‌مادرید مقابل بتیس؛ ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105514" target="_blank">📅 21:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105513">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b668e9a164.mp4?token=EUtQswJy7sGPtcHZ5Cf7hdYmQSpJhPuGJbYpxmHxocGJyuMWkVyjEvEYJioDhAlFFbNDB8J1H1KWVBzRzBkVvz_w55w9GvgIvVttNoidoxXEPuXrqBJgyR12k2t3ueOur1JQTgshyLzf2fEdGEznjFo1RX3uG2lfa4CI76dhibbeK8euqC-ND2Dh0hGDwlkHKz1lkrp25vauUHjHaNzYoDPkOP90OHDb-D8MwvP3cPfYtPEI5yBLCw5ErmzBP4Tj93iXkMvbDKFViBpuphZdtRz0pfqZ3uMojipe7n3uM7_vamL6bMcUi0TwzF6pl1zHCLXjkx0DurpNPd4CHcc6BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b668e9a164.mp4?token=EUtQswJy7sGPtcHZ5Cf7hdYmQSpJhPuGJbYpxmHxocGJyuMWkVyjEvEYJioDhAlFFbNDB8J1H1KWVBzRzBkVvz_w55w9GvgIvVttNoidoxXEPuXrqBJgyR12k2t3ueOur1JQTgshyLzf2fEdGEznjFo1RX3uG2lfa4CI76dhibbeK8euqC-ND2Dh0hGDwlkHKz1lkrp25vauUHjHaNzYoDPkOP90OHDb-D8MwvP3cPfYtPEI5yBLCw5ErmzBP4Tj93iXkMvbDKFViBpuphZdtRz0pfqZ3uMojipe7n3uM7_vamL6bMcUi0TwzF6pl1zHCLXjkx0DurpNPd4CHcc6BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان چالش
🎀
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105513" target="_blank">📅 21:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105512">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0ab284a6.mp4?token=P2HbJnMpsucN16M2zawIK2UHbVJVjrHuRQWjCQyU-KeT_XwDnD5bMZqFhg7RMjoOpA4qF4xJHPDWZQKRUwJxIBQXN4J_Z5iHuJ_DYnxaLH-TD-qrOwsPPwwDFQZX85jbO01iHXZjij_Tk_zH-JUhALLTMDz5Z9o3FlJgI9OJTSM1CEUFZXPdDn4EFcIxddFNUURbLKQpbyFKUI83SvzBwjKD3DgX2KBYMmVyLuVLAtCklo83MjeavHBQP2_rX9o1tm4UiH-o1IUGGUiExwv2RW42H_rU_KR080NGPgnQw_01eJgHiSYvWtN6vRDRNa2isIFgNeMYu19ro5w8qo8ouDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0ab284a6.mp4?token=P2HbJnMpsucN16M2zawIK2UHbVJVjrHuRQWjCQyU-KeT_XwDnD5bMZqFhg7RMjoOpA4qF4xJHPDWZQKRUwJxIBQXN4J_Z5iHuJ_DYnxaLH-TD-qrOwsPPwwDFQZX85jbO01iHXZjij_Tk_zH-JUhALLTMDz5Z9o3FlJgI9OJTSM1CEUFZXPdDn4EFcIxddFNUURbLKQpbyFKUI83SvzBwjKD3DgX2KBYMmVyLuVLAtCklo83MjeavHBQP2_rX9o1tm4UiH-o1IUGGUiExwv2RW42H_rU_KR080NGPgnQw_01eJgHiSYvWtN6vRDRNa2isIFgNeMYu19ro5w8qo8ouDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
🇮🇷
یاسر همرنگ داور سابق فوتبال:
❌
با یک عکس نمی‌توان راجع به دادن کارت قرمز قضاوت کرد. تنها ایراد وارده به بنیادی‌فر چک نکردن ناخن بازیکن است. داور VAR زمانی داور را می‌تواند صدا کند که یک صحنه‌ای از عمل «وحشیانه» بازیکن موجود باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105512" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105511">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae761380ef.mp4?token=F4yj7gys3S-YoabB6Lpw2YE3gDw-mpnqEJORgUY7x6hJTQkOrG07MehqNyDZzvc4JYNjUgESM0elaPe1L5BMUABWaIRxuDx5H_OsA3qEjGXrR-GdTcLQ2EgEyCL0a8fSrKkgCu9CKtk_qhoITsPJbiYasE1EF6s4y0tSuhiO6TN5KodeX-KKSjKiZfbY6dItIXIefDA17cEj-UJ6uKdqIncZ-RzJmRTB1it6p-I2HUrIP52jmCsx9NwxviUzNJi375xNe_ugVLnEqJhQ56MBsCIQQcPuNESA2y9THAspaylZeDz-cVS3ysSqOlEERy0vo00T982KM1zsbN5f00poLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae761380ef.mp4?token=F4yj7gys3S-YoabB6Lpw2YE3gDw-mpnqEJORgUY7x6hJTQkOrG07MehqNyDZzvc4JYNjUgESM0elaPe1L5BMUABWaIRxuDx5H_OsA3qEjGXrR-GdTcLQ2EgEyCL0a8fSrKkgCu9CKtk_qhoITsPJbiYasE1EF6s4y0tSuhiO6TN5KodeX-KKSjKiZfbY6dItIXIefDA17cEj-UJ6uKdqIncZ-RzJmRTB1it6p-I2HUrIP52jmCsx9NwxviUzNJi375xNe_ugVLnEqJhQ56MBsCIQQcPuNESA2y9THAspaylZeDz-cVS3ysSqOlEERy0vo00T982KM1zsbN5f00poLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
‼️
⚠️
جلالی: هنوز هم سر حرفم هستم؛ قلعه‌نویی در اروپا بود، از مورینیو بهتر می شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105511" target="_blank">📅 20:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105510">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e88a7236c.mp4?token=l8ZHrkz0z8lWXI6LjQBCcPcnlWL4TtaXOhjmNCvcVJAEcCnFcnjdJw-PbhCv4GJvsDU-4Agu12ApANRgb-A-ghJq7ets9pVyLMMFwHhyZ0fyqEolEu0yt3QCB8YjvUC6UWdwivGWVIKo1cAmsD8VbVJIEapPO1JA0WGlyf3L23Ilvp_6FdBhk_JLEgk05GEnDjjQ4Zs6CFHpwZUxXaT4gqK72EmH1D_2mQI2zLwmd7n6CkWSR6pGhUqBBQ5memaRH6DojqwgbADhIXvb0PidjFEJBv0xWFOOtuJ0aqND-0u1IS4Ctxt-bEnk3ntVzOG0NaNrzIWKVXnvYDWaX9XJtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e88a7236c.mp4?token=l8ZHrkz0z8lWXI6LjQBCcPcnlWL4TtaXOhjmNCvcVJAEcCnFcnjdJw-PbhCv4GJvsDU-4Agu12ApANRgb-A-ghJq7ets9pVyLMMFwHhyZ0fyqEolEu0yt3QCB8YjvUC6UWdwivGWVIKo1cAmsD8VbVJIEapPO1JA0WGlyf3L23Ilvp_6FdBhk_JLEgk05GEnDjjQ4Zs6CFHpwZUxXaT4gqK72EmH1D_2mQI2zLwmd7n6CkWSR6pGhUqBBQ5memaRH6DojqwgbADhIXvb0PidjFEJBv0xWFOOtuJ0aqND-0u1IS4Ctxt-bEnk3ntVzOG0NaNrzIWKVXnvYDWaX9XJtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
نصیرزاده مدیرعامل سابق تراکتور: بیرانوند در صورت سربازی باید به لیگ یک برود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105510" target="_blank">📅 19:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105509">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2862cc83d9.mp4?token=GGrQ7gfhI6b3S5nFrAXNqLIUiCQ1zqXhdMYapo00ejSf6JNTz-Msn5T0qbNhw9rPr6afEIo36da5Q7w5MithfdMnazgJluC09RxUzHIxgSpyOUEIKsmWh65fWa0hRdA7OPLUKxoJ00tBvbk_GQT3P0SCdFdGAAJtcheIxFNdmMILqPdu7j8fd8aF6FD-569gKcj9MZkks0yXxw6OqhGsJ26wnb7n2lGsbueqfOan_tKW7a7nEQyQZFTBOn_c2ECUH842ftKQD6eDGpPCN_t7McuthbRPmFrxYdb2zJQep7HJKzB_aij3hOQ-5GbnrOynDCoz52WzohW95LuY4z2V9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2862cc83d9.mp4?token=GGrQ7gfhI6b3S5nFrAXNqLIUiCQ1zqXhdMYapo00ejSf6JNTz-Msn5T0qbNhw9rPr6afEIo36da5Q7w5MithfdMnazgJluC09RxUzHIxgSpyOUEIKsmWh65fWa0hRdA7OPLUKxoJ00tBvbk_GQT3P0SCdFdGAAJtcheIxFNdmMILqPdu7j8fd8aF6FD-569gKcj9MZkks0yXxw6OqhGsJ26wnb7n2lGsbueqfOan_tKW7a7nEQyQZFTBOn_c2ECUH842ftKQD6eDGpPCN_t7McuthbRPmFrxYdb2zJQep7HJKzB_aij3hOQ-5GbnrOynDCoz52WzohW95LuY4z2V9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
🇮🇷
آنالیز گل‌های دربی اخیر پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105509" target="_blank">📅 19:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105508">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
⚠️
رضا قیطاسی تو مسابقات طناب‌کشی بازی‌های جهانی عشایری موفق به کسب مدال نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105508" target="_blank">📅 18:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105507">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33404ffbf8.mp4?token=rdwsgVZ1QYU7ohFfMoGCBeuaMgfhaLai38rwNfOzMrBKevE8ixyw40OqiXRE5-oUTiyqKNbzc24Lw9L6hQ25_RWlpHisdfmCwG4xELUiS6qQSKFatKX94Jat_kh3K_8EOKNHIBmE0le7Nvxf6EG91cre18Nk0fRifriYns6sLrFCRT6CCBSDEvUxDzHwINC4L4z1qdaFp6Jtf48EE_4xslw-u0bB3KYqGh-dX7I5GI4643ZWfwS82JN19Bybp17-1MjQCzxiORaFemn78Cqfqy4MEs2jtaoEwIatGaDSAa7UhICwBkGcK06KZ6APu3sCqqmRsVrqqjrix2wNKCHDb1TVCrEZ7NP5drjdUbZQbu9tsG5bVU9GE2N88mPHZoYA0qW1Ngam8IUXycGGiXM5mxy1wzocP5M_vLl0COKMS_qrnAKvyseQkj2s-MDLi0QES6mfCuP0Mf4NuWQo5QxIhdk110a5QLmUuxx6vNUVVRFa42340xVeDQUk-PTv8zP4LAxPxnRh6DFhwv0CMx1p8tkJhsfgQhptkkMfBciijaNXmDRyVkdu2IDSuBX86F5QWzVoHT5uA-t8X0jr-xOgWM7iF7F9K01-tGOgAGnV0i4M8aeluEEEZ_ljsIAxBulp1VWr5ayTaeQdJtOYz2H90NJxjXv-DFJZi0mHmjESIKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33404ffbf8.mp4?token=rdwsgVZ1QYU7ohFfMoGCBeuaMgfhaLai38rwNfOzMrBKevE8ixyw40OqiXRE5-oUTiyqKNbzc24Lw9L6hQ25_RWlpHisdfmCwG4xELUiS6qQSKFatKX94Jat_kh3K_8EOKNHIBmE0le7Nvxf6EG91cre18Nk0fRifriYns6sLrFCRT6CCBSDEvUxDzHwINC4L4z1qdaFp6Jtf48EE_4xslw-u0bB3KYqGh-dX7I5GI4643ZWfwS82JN19Bybp17-1MjQCzxiORaFemn78Cqfqy4MEs2jtaoEwIatGaDSAa7UhICwBkGcK06KZ6APu3sCqqmRsVrqqjrix2wNKCHDb1TVCrEZ7NP5drjdUbZQbu9tsG5bVU9GE2N88mPHZoYA0qW1Ngam8IUXycGGiXM5mxy1wzocP5M_vLl0COKMS_qrnAKvyseQkj2s-MDLi0QES6mfCuP0Mf4NuWQo5QxIhdk110a5QLmUuxx6vNUVVRFa42340xVeDQUk-PTv8zP4LAxPxnRh6DFhwv0CMx1p8tkJhsfgQhptkkMfBciijaNXmDRyVkdu2IDSuBX86F5QWzVoHT5uA-t8X0jr-xOgWM7iF7F9K01-tGOgAGnV0i4M8aeluEEEZ_ljsIAxBulp1VWr5ayTaeQdJtOYz2H90NJxjXv-DFJZi0mHmjESIKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
تلاش‌جالب یک پدر ایرانی برای گزارش دربی برای پسر روشن‌دلش که حسابی دیدنیه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105507" target="_blank">📅 18:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105506">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b357d488.mp4?token=PTm2LNNpRvTrcrGA6VaJ9A1pMLJ4Ao5zo-pzEiNrp0gUPlzuWrA6K9In4dn4e6VWC7vErh3EVV1mfk7jj7VUIr3EDBQ4XBs0uU-T1bo3zlVfHRUgLsxInoLTQwp4_EmfqNoV7gIH7Gqcwc3Yrke7gWYTkEefCbwADpwuIqJhv4DqGwBq6PUix9nW67ukPApWUNc-TOrkFSCAYjgDppND5kcmqe67dfp98FvpMt6HH5YwnaHMcV2y2aCZwk5I7eUgDBncRp-dNye48lrasJVXeHKzAOCfojN9qgI-fLcCkpnKfCa0mmGzdGGySCzI87oX3Oj0dl5-5FPDQneS-hcbSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b357d488.mp4?token=PTm2LNNpRvTrcrGA6VaJ9A1pMLJ4Ao5zo-pzEiNrp0gUPlzuWrA6K9In4dn4e6VWC7vErh3EVV1mfk7jj7VUIr3EDBQ4XBs0uU-T1bo3zlVfHRUgLsxInoLTQwp4_EmfqNoV7gIH7Gqcwc3Yrke7gWYTkEefCbwADpwuIqJhv4DqGwBq6PUix9nW67ukPApWUNc-TOrkFSCAYjgDppND5kcmqe67dfp98FvpMt6HH5YwnaHMcV2y2aCZwk5I7eUgDBncRp-dNye48lrasJVXeHKzAOCfojN9qgI-fLcCkpnKfCa0mmGzdGGySCzI87oX3Oj0dl5-5FPDQneS-hcbSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
افشاگری محمود فکری: خیلی از دربی‌ها رو از بالا دستور میدادن مساوی بشه و ممکنه هنوز اینکار رو بکنن
❌
نتیجه دربی رو خیلی از پشت پرده کنترل میکنن، خودم هم شاهدش بودم بارها و میدیدم به مربی ها میگفتن بازی رو مساوی تموم کنید یا به داور ها گوشزد میکردن اگه یک تیم گل زد جوری بچینید تیم مقابل هم گل بزنه یا بهش میگفتن اگه مساوی بود ریتم بازی رو بگیر تا با همین نتیجه تموم بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105506" target="_blank">📅 18:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105505">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105505" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105505" target="_blank">📅 18:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105504">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFNL95wNNs_FRa-P1wivxrufGeVPOYdJP9HgJznSllevfXVS04uw4FXLxj_ptUFE2W1Zhtq9awseE2pszBLeEUNDXB_F5MIxis-G89uA4Uedz-GlUa93BasueFQZxfDZCjDq-1hF25SWBLc5mudENNTaA26c-j7BFJ_-Hj9Cc73MxsBGQKrSwfVVXvCIXI_LYeKxs5UxzRuGOryZJu9qVNyuPWWaQig7t6fSIWk1mxS1OZ9abrMyndpN0X2rQnzKA07ypIqPL0A1e4etW22h-xeoAsTgocaEo926Onbl2-mbS2ElFtJL5IdyCjNMTobTak8k69oGHEO8Ii4neXU4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
پاری‌سن‌ژرمن
🆚
موناکو
⚽️
را در سایت بین‌المللی
TrexBet
پیش بینی کنید.
📊
مونامو ۲ برد | ۱ تساوی | ۲ شکست | ۹ گل زده
پاریس ۲ برد | ۱ تساوی | ۲ شکست | ۱۰ گل زده
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105504" target="_blank">📅 18:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105503">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ4E6g_i3Qs6WRWNdFXN0Whnrm-u2cLbPVVguhGVddNEELHRk1jFwEKofkRWJ9WAsR0bxkYlnTZlphx_md-vGAV5Zm3BK3M6XEBbkHSWNLv8MWKT2B0Fdh8tQlLrs4xTItw2Ws_VuGfb25ixKNgc1wJrKRduHXgQtJ2TNs1uWC0SRB2XWtXZXXaAdYddobOVPUB7JzuvPbIgP4ko4bxbBX0gji5Z5wR5aePZdd0HWWGnhm0-nMfQbUT2r2uOqDPmBKa1wm1DaVh1hxEKmm0PvRzBjR5-oJICfbKy9UzHKsc7DYrqJCgSz96cGckf1KSo5kgnuD1Zsacf-gdS8pS3GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🇮🇷
هوادار استقلال در حاشیه بازی دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105503" target="_blank">📅 17:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105502">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea454a991.mp4?token=XFimQiQna_Jc2QqWnCvSzQRIl1i8k0h-HoKcqSx7zwqOm0m8IquCX1zd24uAuQEXpTP78SVpLD9BymXmFStzNwKibsnQtCnhl0CidPDkKxQ8NeFsNeXTb23fgEG1rXh9r0VbKtIY0ZTEk-S7Did2QxrnlBQS5cf5PodxF-QB6hPnsXtPzgm891FFxkwVGhm64EbxQYlC2xuAMM7l5HIlxoBJ3kuN90mhkDIMwlyF_snCq-t50Lh7GrTaVw_imWsN7KJVGl71WS2gP0-XTM4GDGrqyJQVc73I_HMwLvoIGWEbUsJ2_W_kjpZwIPPt2Hgz6rYZ-nNXUt6U6Noksj796g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea454a991.mp4?token=XFimQiQna_Jc2QqWnCvSzQRIl1i8k0h-HoKcqSx7zwqOm0m8IquCX1zd24uAuQEXpTP78SVpLD9BymXmFStzNwKibsnQtCnhl0CidPDkKxQ8NeFsNeXTb23fgEG1rXh9r0VbKtIY0ZTEk-S7Did2QxrnlBQS5cf5PodxF-QB6hPnsXtPzgm891FFxkwVGhm64EbxQYlC2xuAMM7l5HIlxoBJ3kuN90mhkDIMwlyF_snCq-t50Lh7GrTaVw_imWsN7KJVGl71WS2gP0-XTM4GDGrqyJQVc73I_HMwLvoIGWEbUsJ2_W_kjpZwIPPt2Hgz6rYZ-nNXUt6U6Noksj796g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚔️
🇮🇷
🇮🇷
نبرد جالب و دیدنی تیکدری و صالح حردانی در حاشیه دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105502" target="_blank">📅 17:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105501">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10152fc52.mp4?token=qq65pIUXXHZrhG1yV1Pxs-NYTh7-PqfAFeUS3WcUY-EfYvY86F8tMKnHUw1AyOv8CCJ2YZMLpFG3e3eQ1IC_4lfHMxVOy-JlKfxpMhbH2NgtMRU9oLsMcK6PZZ_Tlr33e7E_ay0UQe4p1WQ5LsFTyx6GqlKYar2-oqGdMp2W4zRYck5BeJi28-y9cT8ZMRPmy8HKbiGoDK8NVMio6GwmNMqN9ZlsFVyIUGsi2xs5mQCOFI1k2L7FISx2UoZuXcUbHytURNhzdDC1oqcmHG9JLNgTJQIzB2Bz1PIeayEDuE9Qr3cX0mdh-Urmg1fICLIsruoMScGYvgax-vasyFfC1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10152fc52.mp4?token=qq65pIUXXHZrhG1yV1Pxs-NYTh7-PqfAFeUS3WcUY-EfYvY86F8tMKnHUw1AyOv8CCJ2YZMLpFG3e3eQ1IC_4lfHMxVOy-JlKfxpMhbH2NgtMRU9oLsMcK6PZZ_Tlr33e7E_ay0UQe4p1WQ5LsFTyx6GqlKYar2-oqGdMp2W4zRYck5BeJi28-y9cT8ZMRPmy8HKbiGoDK8NVMio6GwmNMqN9ZlsFVyIUGsi2xs5mQCOFI1k2L7FISx2UoZuXcUbHytURNhzdDC1oqcmHG9JLNgTJQIzB2Bz1PIeayEDuE9Qr3cX0mdh-Urmg1fICLIsruoMScGYvgax-vasyFfC1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
🇮🇷
علی‌تاجرنیا: خودم پیش قدم میشم و‌ مشکل بین صالح و اقا سهراب رو حل میکنم. چیز خاصی نیست. هر تصمیمی سهراب بگیره باید احترام بزاریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105501" target="_blank">📅 17:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105500">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dcbb7663.mp4?token=FWtOLvtTZOPgIeLhmbjAPRqXZeDubzK7JTkKUUhIe_xF7FSBqHCEwWxF4DfmkTVh_y8BQSa6MIWhMGLqahFe2XFvAMYXYdaE1U928hmqqMQjDcv7znySwiyGcHkNzmX0zI_WDNSfKCj8P2tqJNp8V3zhccFFPa3-9p-J0XKowK7BmbwC2myGDTMEVvV2wbgFc-5DUVhyjTr1h7c2GEuKGQg53kb081ZW7qwJDwTeoWJAzdoR24w6zGtM-ac21RaVLFgsMOotpqscB0M55wMYZVDOMcdeS1wv03GzNH2Q_qsi5KMbIU7_1MjEDuxnb3WDyLjTfveLNNcBtNhEtbCZJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dcbb7663.mp4?token=FWtOLvtTZOPgIeLhmbjAPRqXZeDubzK7JTkKUUhIe_xF7FSBqHCEwWxF4DfmkTVh_y8BQSa6MIWhMGLqahFe2XFvAMYXYdaE1U928hmqqMQjDcv7znySwiyGcHkNzmX0zI_WDNSfKCj8P2tqJNp8V3zhccFFPa3-9p-J0XKowK7BmbwC2myGDTMEVvV2wbgFc-5DUVhyjTr1h7c2GEuKGQg53kb081ZW7qwJDwTeoWJAzdoR24w6zGtM-ac21RaVLFgsMOotpqscB0M55wMYZVDOMcdeS1wv03GzNH2Q_qsi5KMbIU7_1MjEDuxnb3WDyLjTfveLNNcBtNhEtbCZJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
💙
بیژن طاهری سرپرست استقلال: بعد از 23 شهریور که بازی آسیایی را برگزار کردیم اگر سرمربی ما صلاح بداند بازیکنانمان را به تیم امید می دهیم/ در اردوی قبل پرسپولیس به تیم امید بازیکن نداد اما محرومش نکردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105500" target="_blank">📅 16:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105499">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇮🇷
❌
صالح‌حردانی بدلیل انجام برخی کارهای بی‌انضباطی خصوصا در بازی دربی، از سوی سهراب بختیاری‌زاده تا اطلاع ثانوی از حضور در تمرینات منع شده و احتمالا بازی روز یکشنبه مقابل آلومینیوم اراک غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/105499" target="_blank">📅 16:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105498">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXqKYdtXC-Qh0yArDedOUaFTMNvPnnDkDVqFd6HRGX1YMPR2mEsJq_y5v01Ea7_Dgn93KAaW_xWsTUuTtY-sVi0Lc0VvGPTlHGPwVUrGiLvkeiOgycKHon7P3uJco8avjlzK9SJySsnJ6TJpuQN2A1sC8fDNiRKi3zsAgWJB2K2DQFcrucr87h9BUja-fZxyaJbd0j-tQE9PNJaKhCxfR7JQTImQ5kvGLvQhS9qiyajiDDDQCCTIOIx9gOlqkqB3lRK0X2Fx9hmaketkzRcg39cvscxHudn7lj_6sOiT4BB7_TFKK1_RcUlq9HdEnxbLjzzkp3-8a5n3YTQGoxW6XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
لحظه‌جنجالی و کمتر توجه شده از ناراحتی صالح‌حردانی از کادرفنی استقلال بابت نزدن ضربات کاشته‌های حساس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105498" target="_blank">📅 16:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105497">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJTBAQ1r2l0PbeFwoNvOt3YyoUGXkvVym6MkxhW92_GIdAElW9TioyFdGxo6T6xMDSJO5cFG0FZm5CGmPpZ9lCB9Z7G_k1h1OF15K_J18DX9sGXfSNY56T3dM6mLEVKSMcPoj-n_p8mqiNzCJcye4EG-iUrepBfMw4S-w8dbPvofJgnJTxXrKxri7Y5e8xgjCplbpF-jYFUeEdDDCs3XCvcZVfp_saJmZkXhI8k4hcP4gctJoZx4MOUTtb_OskVitfxdXKCCCtcg3kDcmgrJdWzromfeviRXJuhjFcxc5EeROa3HYsleeoNjU8VqkwdClZdQ92LkSZ4az8LTC5zCsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
ترکیب منتخب بازیکنان بدون‌تیم؛ چقدر ستاره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/105497" target="_blank">📅 16:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105496">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👀
⁉️
🏆
توپ‌طلا رو باید بدن کوارتسخلیا یا نه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/105496" target="_blank">📅 15:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105495">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c1e785e5.mp4?token=I8eyZqki956-cFPBrNSYA0Ru84QTNb6lTE9HL9iRkkgt8O4m1Y5RGn1TCRkf_ullrf_jOfoH4w8g1UOUO8P1TZ-_5JQTwhRJv1wjrhybV4w_yG7K8XLEDutg-mu4-TC1jRBEx3NREjNf7tqILHxuYqH-l0EfgUXmXBaCodU0rD1Xslt1L47izVg-Zfob_O3IIuZt1wbX6TgwlAPgDw1ZDC8HJlAl9iKtZnUNtIinfMjDHMmW_GCXSwzAIKj2u_NI_jKAgN_zagRxP7rAtReO8c5QmCzjftpaE-VqDdjc709CPjsKEc3A-iRms0XSkv9ZGhT6KIufJap5j48GafXC2TGHGLZMaN-icLLysmyJWISzcaC7KQ2Mh4XZpPi94GnVeOTMlM5Lo5BlvnMqDmFGHRM6mc_EhFIzAB1RzUZbfWqXAZN0dS_ZekyyOpkR7fGWSmsgO_F09TvbWjM6IBMmc3fU0t_eSFFkgfNRVM1zaO6tsbOAdsmiNV9uSiNzgOwgw6yp7HRJ1pCaU8Sr3NTNI_0KWOAzNFm22BM8p3gczRlHApevAPsmnxbQU4kV6F7OBID4oD7KvJiOXtXx9QqH4sJY_t4PddIl-RKr8laiGpcPQhjIljJ7GZcIdy6rum597l0OEQtWauLDjcQ4tER6fkMp7ctMWzq1HGpRmeIcNA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c1e785e5.mp4?token=I8eyZqki956-cFPBrNSYA0Ru84QTNb6lTE9HL9iRkkgt8O4m1Y5RGn1TCRkf_ullrf_jOfoH4w8g1UOUO8P1TZ-_5JQTwhRJv1wjrhybV4w_yG7K8XLEDutg-mu4-TC1jRBEx3NREjNf7tqILHxuYqH-l0EfgUXmXBaCodU0rD1Xslt1L47izVg-Zfob_O3IIuZt1wbX6TgwlAPgDw1ZDC8HJlAl9iKtZnUNtIinfMjDHMmW_GCXSwzAIKj2u_NI_jKAgN_zagRxP7rAtReO8c5QmCzjftpaE-VqDdjc709CPjsKEc3A-iRms0XSkv9ZGhT6KIufJap5j48GafXC2TGHGLZMaN-icLLysmyJWISzcaC7KQ2Mh4XZpPi94GnVeOTMlM5Lo5BlvnMqDmFGHRM6mc_EhFIzAB1RzUZbfWqXAZN0dS_ZekyyOpkR7fGWSmsgO_F09TvbWjM6IBMmc3fU0t_eSFFkgfNRVM1zaO6tsbOAdsmiNV9uSiNzgOwgw6yp7HRJ1pCaU8Sr3NTNI_0KWOAzNFm22BM8p3gczRlHApevAPsmnxbQU4kV6F7OBID4oD7KvJiOXtXx9QqH4sJY_t4PddIl-RKr8laiGpcPQhjIljJ7GZcIdy6rum597l0OEQtWauLDjcQ4tER6fkMp7ctMWzq1HGpRmeIcNA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
👍
همسر رشید مظاهری: شوهرم قبل از انتشار آن استوری خود برای من فرستاد و گفت که اگر حتی روزی به اعدام و زندان محکوم شوم، فدای یک تار موی ملت چون همین افراد من را معروف کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105495" target="_blank">📅 15:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105494">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de11aaaa44.mp4?token=aQQ92gDrmxEYPRs_p9pZ6hwvCPXeOdZdDnE5gGsTe_R3xXB8vgGHNvUqHN3FaK_ikfe5jjwjVIKEzBPRg_a-MQkTpto8kateydURtK18hqG74rNhA2-NdXUpdlWyzwAsY5ljqJ_K5N1NYQhprXT7ByvFXFCITC7DRNFiR35VTiRqBVtiYpvOs1fZjps8FZj0H1hbNSAxiU5XBc680dm1MmmrRqepsXBLm4RqMXpa7DdNXDleE5su-pzpmAh0tPgwQYf0MtSbhE-IvaP0wgeSX6AWLOzb4euUaT5o2xp1WHpdobd8ra4J_yhOayec1Eiry5bpv069FRcZ3ntk1o5zCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de11aaaa44.mp4?token=aQQ92gDrmxEYPRs_p9pZ6hwvCPXeOdZdDnE5gGsTe_R3xXB8vgGHNvUqHN3FaK_ikfe5jjwjVIKEzBPRg_a-MQkTpto8kateydURtK18hqG74rNhA2-NdXUpdlWyzwAsY5ljqJ_K5N1NYQhprXT7ByvFXFCITC7DRNFiR35VTiRqBVtiYpvOs1fZjps8FZj0H1hbNSAxiU5XBc680dm1MmmrRqepsXBLm4RqMXpa7DdNXDleE5su-pzpmAh0tPgwQYf0MtSbhE-IvaP0wgeSX6AWLOzb4euUaT5o2xp1WHpdobd8ra4J_yhOayec1Eiry5bpv069FRcZ3ntk1o5zCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
از یک دربی تا دربی بعدی...
💵
دلار: +۱۰۰,۰۰۰ تومان افزایش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105494" target="_blank">📅 14:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105493">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a3572f3e6.mp4?token=dkNxrmzYu-r_JhRVe934I7kRAZqwBxUj1mbwupzAPS6no3GBnD1wD4ufX5DJESAVxmHUU-9kBg52IspLg_O_uBMtThzHpzyOGPRYzbji-2Tj4RDFGWz764NNVpbSYgWlLV4btpn74-c5FVS_50TLzjsbIWp7StLLKn0DLII9AvSWUF5K6roITXOXTUPrXeRdTsUfRwcjvo22UAb6o0fsBIOLby8O3h_PHchnNmat0vf-LTye5ZGBcm9LjfdMtjnNVooAgcX0nc4nPr6QM_R8YZfJT53vFMK4MCbgoJjZHoGNLNaJ2YluHIy5TLGJaTZ386_ReLNcNXVgnRS3aCduzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a3572f3e6.mp4?token=dkNxrmzYu-r_JhRVe934I7kRAZqwBxUj1mbwupzAPS6no3GBnD1wD4ufX5DJESAVxmHUU-9kBg52IspLg_O_uBMtThzHpzyOGPRYzbji-2Tj4RDFGWz764NNVpbSYgWlLV4btpn74-c5FVS_50TLzjsbIWp7StLLKn0DLII9AvSWUF5K6roITXOXTUPrXeRdTsUfRwcjvo22UAb6o0fsBIOLby8O3h_PHchnNmat0vf-LTye5ZGBcm9LjfdMtjnNVooAgcX0nc4nPr6QM_R8YZfJT53vFMK4MCbgoJjZHoGNLNaJ2YluHIy5TLGJaTZ386_ReLNcNXVgnRS3aCduzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی فوتبال به هیچ‌جای زندگیت نیست
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105493" target="_blank">📅 14:25 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
