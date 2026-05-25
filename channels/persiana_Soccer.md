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
<img src="https://cdn4.telesco.pe/file/tjs8j3mUWFgV3TwVn8pogu7I3yRJHM6csRK_1c-o5-BcEq6SQMSd7Ag_xYgni2kWHkJ6s7T0sM8uubL_zhd_FkAy-_N1f5GeXW-d4XG00M4XmI1U9ulXntyhQgFpTBcbCSPNLWqjVDXsdLr0t9YnZFw6RKp_HPul_srnY4EhwDgfTkd-LAm3bNrax8gRxzMsVyzGLPE3I9YOTlf5pZpPQ_Q4hdrVC_uNmuWBak-wahLIrEIoHe65HEl2SWncWJBcllyDGGWdTFgaCGmGmmglyEhIJWrJxMEvtJmwfwXhPMqhiTQBjMdNQXN8IYclpBmyeWyYlm18PePF5G0IpqtwPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 192K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 20:30:38</div>
<hr>

<div class="tg-post" id="msg-22309">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgaSg90UL9xNVM7BfLhlqUV2Hzqi9KRyukY49qeVhUjX_goq55Zt_WE2jAAg5j7uI4UbHqqwR9gjgJFG2crgzxUkHwWC2xr9BB1tSuf4Wp8BCZLL_PClDZ57rGev9hadn8SdcEQzsUkHJlqSQyIn9yklX2_38yj0ntVOOfbIauZpdyJ0bs45Ss4hprKNJZhcX-OFeFMHeS7l3fB6rFvMqDjKfKp-FN6PgNCuieT3Sdiy9MBP1gvskI6BiZHh2hepJhtN1J-JoWpLa3qtme_Hn4kYxCGR0n9VIPgLajCrcBsY5r0yECunPGeLp5mr9Y0ePsPX9JuZ7n65i0JaojTqFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/persiana_Soccer/22309" target="_blank">📅 20:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22308">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFDlYgfWzyxw8W4JtohS1QmbRMiab5q9fO6H-ii4qEDvhatLDBDvEsU8q0RA-rZpu4PrkPOKnkmHTfpQei33TfxCpX25abNuo7urRsJ6ZkS_9jEAFSYKqUKfpFHtwFB_Ol4hZ_atDZj6LcmDOhz4G5Ch5bt28HhbeVWZSo-jRkLST2l2LsnTP6rGw_PJmockLQnKHq5Phs0lDjAGDXas5EfVpCr4sxSwnIvZvd4s5nffymwLyChs8XulLTGPAwphhtYIhznwxkDTci-0zwqNefFzgzjOMr8OecEs666ogQk-vyBADQH3SS8raf15o3OF8tdgBkoy2xChKPEvPiK-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...ایوان سانچز ستاره‌اسپانیایی سپاهان توافقی از جمع شاگردان محرم نوید کیا جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/persiana_Soccer/22308" target="_blank">📅 17:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22306">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K1IpdWoWvP99oxRELwuqmDaHTaCqoKXjoOZZcuvyjb6gaeWbjVXC2RLA_PRWXxS2kCgDbTCUxo7x6YdFZXFZ_cVa2YvjaNl-t8nzyhcfW8Ib7042ifJlR5h0x0Ybu6inLoVQ37sPDztnL7_uFba7YQ7TOEwJcr54qMCF1GHk5CmZb0BdJaz0BFhf0kTICFvMMKoWHQ_VGlzVWgKvrUK7tDtinhSd-hWy2xy2y1-RqG0acodam3tA_rR2wDBiWTxWWqzOMSc86194gYhoB9k5A3JjWhkLnezkIDuiTK_hJW7xTECLeKWMyZMJjhwDka5AjaDw7Fe2kJ8w4NlqIopDEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SY7Iam_IEY3NXkK1OWOMMXpB5ZfvBMLAKgpQ61khcr6Qqdx8YzhPjm8bCulJP6Q4x8cNkBcJ83hGgd8yJFZA3b7TpQRw8wXN8QMNit2PqSWEe3PTUJ28WZQPu3dyXw_IzwvooYF488VabPhFGu2lqCVL9u_VmeGtPivobfUrMXpdVRB4HVe0FEoMHP9HYe3o8GCgm7__6C_4C7HVajQohfmBK-VUUDkgFqjwL4pu1Yu8eH_198MPLLC0EN7v49WknEPUHptSL8lDs73I-T35RQwIl6SAk4sndA4evoNSqIL6ZZnPRUohOBzBTzdMqU1pAJ_kHeK_z8EuQhOzClE4hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مائوریتسیو ساری سرمربی‌فصل‌قبل‌ لاتزیو راهی آتالانتا شد. جنارو گتوزو سرمربی‌ سابق تیم‌ ملی ایتالیا با عقد قراردادی سرمربی تیم لاتزیو شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/persiana_Soccer/22306" target="_blank">📅 17:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22305">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcgWM0Ikj3YCnKSqcfbVDn-yD6CRHDyso8S2WMjaQYzuKvrmRJrx2C1O_qGkMWE5wBuLDfrGTvGo-8gJykgeiX65BhXKwV9PnXvzqinqmASjKeGL2bIb1fQXtKnxTdVAS9WTUn42YCiNp74wJh9oAQ3DepGZ06i2KwofNastNV11PvOXzsnBLxCSVzoqEmTeNF2XHk5Xq2eJEaVN6Uu-N6IsvCX0JW5VIl7vp8G80QJ-kYygWYAVARNUwGRno1zLRmunxVKi5d9m-PAkohgF43zmRdy7cwaVMcF10neR-w1aN6RlOWlDbQZjR_ImNMtdq7HVgEi2rsqefUHOUYi-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سردار آزمون ستاره سابق تیم ملی شب گذشته بین دوستان نزدیک خود: تا زمانی حکومت جمهوری اسلامی پا برجاباشد نه‌ برای این تیم بمیدان خواهم رفت و نه پام رو تو اون کشور خواهم گذاشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/persiana_Soccer/22305" target="_blank">📅 17:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22304">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahCwkqXX8-GJWs5uy9CCgdcwB3-OOq42Yg5hOJa07Sj4pkM2yd1qoK_M9kI8yw1BezJ7_Lh85188ezWFMzSd_ouhym9ItQe2HJ3sF_T_XwlQ3uV-OqU-u8dCqgtH3fHoJ3EzWSyPVt0QOAa1IH4BybWsMW0IIIjxpnO9N5KY3FBNixLoDHqgtwKpGW70I81RUGOjXGaABPS7Men7kS_Je0LSRnyBEld2-nBztyw3gi2DpZX_nQStGi0utmGZOc1Mnv8jAbPsCTKB5EVFQACL7W0QS30VCiCOYy1kFlNRm1Tywp1U6roAVdBMwgqEZk0VhcUf3mVXneKTFjDJ_OsYuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... اوزجان بیزاتی مربی جدید استقلال و دستیار اول سهراب بختیاری‌زاده وارد ایران شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/persiana_Soccer/22304" target="_blank">📅 16:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22303">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxoxQN48bqJejR4ZK21QKiSvcjAJ2nN8Jk8z7luV6S40htk0TYcQEvrnGUusHhP3wfoiGt27H0cnIZnnzKDGtDqcjclbE4XQAGBHCUGmntcGezIC28qmZa6mP5fR2fuxzlaofJKSPQNedZYz-37P8vk3q_ToF5017Me4xcaoHQmF1yKiPVPPq1svYsaNVMHCm_z-AbyxTGWar1FFqwVRPv9CHB4n5jtb8gENU-r-0E3L4Sv9AwkbDuXyvWqLuD54Wh3YYtAByG77J_2il_QXhzm3bIYHIBfGquWoIbRq3HXHGZdJOqjNOgvOA2trJrMkTC9o2aVrJgceCu6mn9lPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/persiana_Soccer/22303" target="_blank">📅 16:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22302">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKrP8UNRRFAWvgYss6jSMzRfaWWYdNta9C5z237IZZ7SIy4UAhIjM2JY-9z1YjFpE2z3vXXEIGMO1EyFVseWmBc1q3ulcH2aaJ3n4pEwl46qEJoAKD4tP8UGtNOgOCVZxfeZhdBu9qBaNq67Qwh6imSQSGOYHYtptTmT2Eff57LaWqbfQ-jym7Grf_KY-KFwEN_nUuoMBUhF8KDw6-k2JIZUVvAh-EpO5PU4DX7xGHiGkzkniXtCLs_YruE4MiiOpHLrPklNuD6ooiALzzFWJaShj2Ko_XBC51tNMNEpzDWtJv3W6fMxy32IbCYkdZbOQPW73MOH79DjQU5VjI2IbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/persiana_Soccer/22302" target="_blank">📅 15:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fA-LOKhRMdBHUP1ozvCzKr2i1eWAJ9NWIf88MEwaSM1se-XB7u8NYurhIRFh350oSughxSpR6dNZ7fDy3MCeyay9tPraXOuxl4RIxgObtCf60VmKCJodBGcCYhhAitGO2NlVXf10U-NCrR_nZV4KW7NSI0ebuJ4jtm6gIZyVQiVPl_L4Exg_2fUwf7wS_CTnB_zo3ygxkPCsW0N6A9jTyrExyp0Vn8qiJnYAoFjjGofxQhaDxZ3H40nMw3lJVjoPOBhgkumEHaBUHRmu6XKBgBz56brqvLlxXUjpcjbYa6CKNScnaKF3zbq5YsnpbKPxjbqs4cxFWtUa0ru9Zk6uDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/persiana_Soccer/22301" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_w4_onSSrxRLuHOqx_Dn2vL90lJe0ESN6TCu809s69L9B-18ptTDFfOzz6G-z2hzyORhKxL16HIZoq0DXhFSKbWmy56U2tj9Jlal7n0e4nB1T-qPIHCVve6t1K4RX94gd7ZcSIq1xqHM-7WU1uRXuGrRyVgh8JOxWH1M-C19h_Zrj5fvNUyoq-_B1kaXXmW5CzEmKBMX_s-PYu2vV3eqg4cjUc9ONrjWc6yU_xpVwYGxlIkbSpVmi3qnvWzYlqX0U2RoIgtGTJs7j9aTrDzAoSSv8_7ATueh_M2ZCdOrW82ZcxZAJCDfiCMqyvTD0AfbjJ6FVBqgBAlV7F9hwGpwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/persiana_Soccer/22300" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22299">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlwtrIBqlbUlaNxlitqMEaZh8yij9kEQpdbTtrKIA0J61EcMlh42QE2oCDXcGcSrywpN2bdk399G0B7sC9jiEC7Bd4SmPU5ZiPjB2Ro5X7HSyTh46AVosusGhpBG92cyuI4spLjs_4Ku24Yh5orHaTcy3RcK0utSpFbccBkv9yHHub2Qwwg5AktlzWM_hqo0vdFb_kVIZVuYTaIl0Bm18pHPBxMILq1VzXZy1IVe3M2Mmbohm83MBhdmdwEMsqTe_XmW77xkI9GJ3z_ARB2NcRz5o2ebB-ZOFNXbP1Vd1FtxEsJIL-iBy2U1l0z_Fb2yTu1KbwDU7ZtUz_hstQ9jVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/persiana_Soccer/22299" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22298">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze0a1YK1y9rqTqCyfk_ARnmDfA858p9eylcoxdu1987jiiolKxhH4fXrEjrh386tOswOpF09hdGucQtJh4eiBr-ETAOBBDu29JH5l3WB5Y0ilLKnH4mMYRLiACx5YrkU7T_M9Sv__Gun_Mf2ccMuRHu-_3GPXrUJtBIOCwaiO4sPmOgIpheIap4B5aAfyCtHfoFrb5r_AEebr3hpjXaYiCvZPaOcjD7vNkNvmG8rk1P9-4MKFckoykDhRcBnTyshvsPvOSz4UgWnJpNAaImIiVWVYrY0GBRpZOjFieIc7V7SfdvsxI42qs4EgWJ45nerVwfBufwADrAjw7-L4Xy0Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
دیگه
#فریب
بونوس‌های الکی سایت‌های سود جو رو نخورید
❌
💲
بیا توی سایت مورد تایید ما یعنی
#وینرو
و با عضویت500هزارتومان اعتبار بی قیدو شرط بگیر
👏
🤩
با عضویت
🤩
🤩
🤩
هزار تومان اعتبار رایگان بگیر!
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگانr4
📱
@winro_io</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/persiana_Soccer/22298" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22297">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQmLHudhcuUUBY48l7gAoKZEDsyu-GoPtNtEdAS2BjSd2I1C5ym3IgUva93tm5tsdLm6SLE6fpguvwCg82b9H3lSY2X3ibbU2HT-_vAQgCzlEiyUIb6MQuO_6VcSw_0giejW7iOyeftfghAkem9fhoW1wIFi_lI0sU_f3Iu3ew0qsIDjOqysErG-oT_eVVmZenRxYYHRLWPkwt6Uuc534KCebIuALxI0PKrk6q2WAJyq8TpQ4bqaPUuH476q89h5q6wQASdpCqweXKma5uTbLvApFpyrbaZCL-tuj1CgkSLdGbuFG1tLIvK9GjEepSVXq10q7yfqRgPiQ3OFPcUbxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/persiana_Soccer/22297" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22295">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGAzZiI0tUf5x4QvigXvROoE7iQXjyvUmat6cWC77DpwnmkZoX3GYB9TvrjRd_RK_LhDNjMauf68JSbTDeXrsb3KA-NlXYklDLvJS5iDmWOXM-gcZyZT8FOsfXm7JpQEYVaJIIfmhuSVVF1Ca-RFBKN28g2_gQ7xKqkgi0SUF5a3tHOphbgfNAju2BsxZ1JLfZ_XCxoLeAH-REFSex3owocuJqYiIsKUtxdmSS2bE7L9MRKvPsFzl07jFVnLC38m_5GJljvU43-QF6JRMTtt6QfH2faMnRSIkK1NSo681LrO2KcG1d7Q5Bbye96f4cr-ITy6c-M1xRyWOZ3_YpaFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رشیدی کوچی نماینده‌سابق‌مجلس نیز تایید کرد: اینترنت بین‌الملل‌مردم‌ایران این هفته به حالت قبل بر می‌گردد، یا ظرف 48 ساعت آینده یا تا پایان هفته!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22295" target="_blank">📅 13:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22294">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK-I_BQw3lI9Ob61iS5lm37uXpJSYDv-hkEdew-QerucM4XWh7wVnW0FOM62yXUIsBrtndatAIfLuxOBFmQEfVkNvULAKOUjQXKgcOoYdecOnfGro5NRXjOgHSKx0pJB9dSEHskjIEvDzUHEC2tIdQ0aJnOYNshoUNenA-LEDGxyJ_MFho21FXwIB_-DUPri8wBxDDzYy6vnICcH0Vs52X5uD8K4EcyEpke8OucUQqjEzFD6cbW--LeP-KnUVsoUM2ic2TzErHsZOOM18z10jBhffHZJX8s0EDSbiX4vlr2zn9mz0IK4LqEGt6A6_P2I99b1nMv0osVsCuwBK_edLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22294" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22293">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCWDtZ-6TY1HYeNKjl4b6IFveCzoC5nbsDsZlfJyAG_0GHuY__mXUp0gCL5n8wEL44CB6VI7MXfPDR3FUqJGfMgX5xD4BhNDuGsnf1Id8Nrqd7gUQc9xVvkdZK1jxk2Gv26vELbBRaZPP8dx36b3LLbT8rMeIxQ1T_zyP3NOxqgqus4ATD3508E2bo4KxA9Ux22_mclgqvowQqzXAZ0Jqfm5tlwa21CS0RCcJMfI_ONXLZQeN9k_R1BMtwCulZ0sFg44hJQz_5nCZZoysrl5Mt8CjBFIxk_zwzcvUjqeXFm39OCXZmGLR4iFg9zdqBzGp2e4osBzZIWSo0JIObCD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛ روسیه با اختلاف در صدر، ایران در رتبه هفدهم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22293" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22292">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hM8owcGlDXyl8yEhK-sL741NPdag1bm14dqwy-8JtuV-Mn5UwXfLx8-_rWSgiEskCQCR-vwdCwaGQ_M8qiQZmoCIXBIJKvMmtwuxtnEnHDhnwQMXv9DDP9XoKI4n-RhR1DiiD6xTiumbVpNrOgykrVlrPMhV1d1fZUz-ZnpBI8w8FHw7SdKr20Pswlyhjfjz3zwu8_XI5VpFHS6FLpR3ABAbmlAc-a3Lpi668qnO_h_5yqe2FLE2lVSu5f4zYTA2locBroexjnA03yi0OiY2o2jls3IGvT40K7WK7tmbkfBZ-_PpaQU20fptp4q6qTqgGGVLEDN1ta3RzL0tVO8tuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22292" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22291">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpUWKzSb-S6pjEX-HwafBmPXBybjP6Wjy_QTyjYo82JkO1xiwdgnzq3_V5I1dLoKdBlPZC6UL4Aa6KNtU1elqa10LyiRZUVc_GHeikOwA64o1ZQjy87t1gB73A4DriW8c4kJWSOeeCzHtx3LD4T6u8nLgk1JCPwTqY5wQv04xoH4g802og3Rx4Fzoxl7hI2cYDqMOrF2p-L_EffyE3lCVwdKzIQN8Yieej3RSDv0i2h2USwJ2eNWsoKQp4YRPYnG6sLLQXgY2oNmkogoaRQjuYFPLByeisa2Js8IYCyQ6b3PYuGV9WOdLwnm3_f_Imc-PyDpemn0pxa1krrU5t-f1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22291" target="_blank">📅 00:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22290">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbyP5rCImQuIV1L7R6YiEzQucAcQgHOt6vIgaVIDGDhzbWlBR8NYwlG8I_Kjzi7sDnPkwQj3c8yftP8erOGM6JP3VfJ2zPlB88IQkciTzjqAYu-jXmCaU9tezmGUUC1NgM5hTDd52VCTMdFlfrrswvyQl4nl15jq50vbPy0slcR1tqUJfAc7cl6YvkmytCuuPO-K_qBRWWlAHf9P0hOopZXoZnEV2wgVlnJmhzcmMARMe8mTEh0vKxvUuhdQ1GYMswIbpdNpHkk32ByW1ACptkqq7YgcgcWbw9tQld3lHhGOJkLp7teLbrlpvYqWANJKjH4G-29dV9rstARqFJHciw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22290" target="_blank">📅 21:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22289">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fgp9flRndDHijEnefALIxtHFzqeIq7xi-WASXHBiFHUvLbdzdkUeuAKSF0E2pkLlPwAgdd5HnTB8ael0pWCOSSvVddeWwI4qHfrfF3nH0t5K0fLjEadLnRIRYVLPYl6QKmk8_ZvDy_hQ8qrQp_OPKEarvXM_VDzT8VdV2O2Kepc3SCarI2iDcoWx-N3NKIIL3ei960kqa8pdShIjMbpPSgRXOySAwhNsTYD90Ul1ah_xMkBMSC2IHb9DFvnI-RrgUtBYd_Igv9qOn0kw9TsDQFjQ3rEAhsQ8yr_jwrkTagiWlXbfLX03zvRFyd7P4NRK0UXueD9NQTEuTQl7Tkj3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
باتوجه‌به‌توافق‌‌مدیران استقلال با ایجنت آنتونیو آدان برای‌فسخ‌قراردادش‌درنیم فصل؛ برای پر شدن 60 درصد بازی‌کردن او و سوخته نشدن سهمیه خارجی‌آبی‌ها به‌احتمال زیاد او درون‌دروازه استقلال مقابل فولاد قرارخواهدگرفت.البته‌اگه بازی لغو نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22289" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22288">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rfq2x-w7zxyhoqJGIOz3zuaNq1m8CJLu_Z31mtxRx0pBzmwJUHKnZx5GjbvOLbxMFVAOrpg5GDqZIh5pj8u0tpUPdzFCJWJnxjH0otyZKrLkkDI3-L-Q57EekQTC1gIcuzhBmzW_pVwSrn1qyELg5FwJH6OrRVloca-ecfUAJ9da3E3KMak3h2WMT5Va-K6PY9VcYYi2CyvCNJ-yx2FaKBeTR0Qm2TVNBPUJy-WZReq_TaNNwmK2vfZqc-SmZ91TYM19VIV77jDD_hy_XQ6Me6KEQj96XHTZeF0DIziQYh_yWrlaV3-kgGNV4opMnWIiKBrRGgZD0UMPrt2lixjYoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22288" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22286">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSIXqnIHO9Uqm5XUuvViv5CfI_bEJ0JmQOHWsXPc3r0-jArkFk7EAGWDjsm6idFuzPNu47Awf3Q02rT6ngNVBDpbLWKwysHZlhRuU7pETIpurai5_bQT1as8nw4v8CA8ppZmmHpNNq8HbktnwFSE1tNPugGRh_tOMyV3RxrY3tjPaQmoEWGuOJbMMc_7kvn8BCUABiadU3EAS0FxDRe-jimZyW2Png44KEF1N_pgITyI1I5Qk3Kqe01lg5uVz8Zi9U7CKdirsVCOjKXs6ckL2fyTQwsfZQK8rihOuZHrbtAKNHQVOZazjUWIwFWetG9teME9pZupdfSDOlqFE2VNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22286" target="_blank">📅 21:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22284">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AmDYPcF6QUVsPsgUPd85HbHQeYmK-CcZYjNpYgjIcR6oz9Ju8k1DpOiBpE7ZhSV6k7AW1ImMkgx7rweVVGSm9_A-qsKRcQVj4pA8SQyNKnUAjCCg6VD0LiRhGjyo3rWhjq_5j9RZykmgUXg3D_GOJ3H_QJ_2rbpxjB9moYfyjsM7bNGJNAJ51wJ7H5RhlE9wruSIk7wNqGnlvwmLOq0r11VlEJU2x0pXk-YrlfCdJVkUW_3LDP86eivqneFd0_3uoraUC6-Fmx7Uk-K2xljpv_PD5lMt6JPHrVAhPdS1XxR2cH6wwLpVEpoWLorsGTMDxymb30w3C7ll_QhBZzyb_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZK65iP8s61-s8_kB3PX_7zjs6UL8fLq5x_kwYhI_YxZGjCmWpuHSyoaiu4AF1uT77IiXgKTAfiQzRKGmi9LrTQybP-W6l_J9MKE90cWd7iOeJ8WWPdvIFJTPiWyZnx47Ba2b403_9TOIbEwONe30q9bg3gslAjNYghzTX6MLtpSp19MntkSe670IzbSn3YjrvhqYgvFSQ1IIJ3Q4E1790sS5toNyRx5aY7kNFNbz1Qh6Gz9YxMC1OrfqWAV7mg6XyeWO7HuBV6sRs2OvBo1VJkS8xPzHXte0lCkPFx2lCQGAKUhP82i9kkOFaJ1aMCQQvIxVYrm51WexMfDo7bTHEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22284" target="_blank">📅 21:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22282">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5hsW6XPz2f0RXevfiejkdnhUm36gZTaaqE-IWBX7gjPwI_IQyquKKi8T9ZSs0ke1d0ARVcoOVZNWMleM9Hv_rv-ViN6fHwh5kCdd8d7A_YGR5VVCmZRojv5_MPqeoi5mCBRVxTuiG2Am13Ar0HKAAzauY-mazBhxSVIfDdJqxljlt3OigQ4H0iIM68u-uxRWyDRUeOCI5zJdzK0LePng0SNdBq1NxjzsXuNR5IgYBs7b-AyrBwxXVnky4yxUlUC8fC4_81nq7mg9GwN2dCXgs-WZv--UxNkA4vw0nQ0lOQDZuWeGLAmKk0NmdaRC2lkgc8PqUt8rVgNjtvNdfnJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lY0g5bsQP_hxcLZtvxxwBmfqjCMJZJehPD8SOwpAzbzGyVYUOYkBWEr20WfUi8xuEzST9yuqtiJ41WhWltW7lqtF4Wuj2MUavQ_f7QJFyH0k-YLygICx1lyD1F4lyKWqgZSS7gHUD2i5VZcbpNeVfLUjn3Yx9x9IgcEOg9fEfHK0yF5xERxSXLDyeehC8pBotMcIYUD2dpZyZc0XXrbBcx6gmUU5ZP3N_iSBg9dSEGWG3K9-RMH7BZdJ7PJYc5leJnJCZbl_BFgaDmhRkG5A8z4ICP6y3g34xsOvfdSHMROYZXRyG1rj2bY1ChYgyymp9Wkd422uUfxfOrplmgdEnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22282" target="_blank">📅 20:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22281">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-jPI--Fy5fEVySHSD6OI6opylUk-mIWcIuq9O9an0pa-V1uZVNrssiecbMWo-XpS7LjY4odq9F1SgX1GtulCNLiaG0QcYZoppLEB6JOay2f9mgbatHMGgokS5o7unBw6MYNAT9joc_C07TII0iUpyLSrdr0IHhYVeN2jTslYJ1AcOxYN-qmb6SbuZ21uZ7TYqMM_WDbv5L2W4PoAG_BB0wl8l2zlNhCI760zNt0ag6l1tlS8XJw9s8pUAZFwRShcXUnvcPqKmadI6YgPs8bxZuSM1tX6cJaoxZScqtSm_-f02pwV8cu0HbGUvyY_0Bt6V_T2Tqh63CSR4uaRcuI9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌لالیگا درپایان رقابت‌های این فصل؛ خیرونا که همین‌چندفصل‌پیش‌سهمیه اروپایی گرفته بود به لالیگا دو سقوط‌کرد. بارسلونا هم‌که چند هفته پیش قهرمانی‌اش قطعی شده‌بود نتونست به رکورد تاریخی 100 امتیاز در یک فصل لالیگا برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22281" target="_blank">📅 20:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22280">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9syQkKgAf7GDRuAQohJqFUhx4TWgYyHNHHiL9Pekqp1lazUxgKN8Px7TgquTHXUSn3Sp9LWG_POopxMN3_HCWzUCv6n6LTPHfJo6yamOyeOLy1OJ1R1iqEAHO-ZqX6KoBprh_cg-fXwqy637Z5kwWE6l05kjBOZ_Dez0kSmhvjFe8PWpmo6B3vq-2DN_6I3ofNFlhmWlvxnzZdrT8Kajz_3_i0vjhjks9kQrHWYDXWYHlkFxAzGMrvIaKyA9Akg588OnjDfv72GfDUoo2EKhXoWNCFmT5acSAw1byFoAwSnL9MiwBY3WBzrtN7KYcP8GaAFEsmFP3gG0dPwzZSwtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ محمد امین حزباوی مدافع میانی 23 ساله باشگاه سپاهان قصد داره از این‌تیم جدا شه. حزباوی از باشگاه پرسپولیس آفر رسمی دریافت کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22280" target="_blank">📅 19:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22279">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQj3YXu1qMxTulsUbvRwRbLY5lWaZjydkTpjXDB8cGpewGYgzolonlgRArnyZezUJnDOqAC9bletlV3I0LLuRHe-fsKQxkud21f0UQ_Mfawj7riQEjU7KXDC29hxxEQEQy135sBzAJjRi-b8Mlb3anNKFmU1EprYia95ouoz7U6gwAyayeZmN3hwCJvUj5ZzYCES8ljZfvDL3CuDJEFMnb4a2t9vy8jeBDv6cNoydVFgYzEawVALpZbfTZ-4pDdDp476O0TJh9guownSrjmUDPTvYbTBHuSLNptvibzvsiFRGt8JE1knbusm4ntCwOzYYWZumBON0bm-wZcmru7lfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیتنا پایگاه‌تخصصی اخبار اینترنت: به احتمال زیاد تا هفته آینده اینترنت بین الملل متصل خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22279" target="_blank">📅 16:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22278">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZhRwYnjv87AHlJ3B4R30JIszJKgsGjkBS-di_YclgjE4t2KsN99hVWrWJgzoEKyPjbSz624pYJZKsOjtmfmLGZtEPDlWEsHLvZTfh0AEqVWw8p3EWnXqsHSAT6CFdl74TL6zpYEY8RRXZ-VdiXYleFOqXBKSITa_K-cDI_uxhYJdrLjGfoIDj2GRjHkAwMK1Tegk2EzcT3HoSceLHWmSgb47mgd-uvdlP_9hhsew6hhjzWf2swo85Czmm1y2Jc6j11WR5qlGpy0CXl4i6ZAcJVYqSqFhPhjYKWdxXATQEMJZUkuaRii18A3etg5R9hbhxzAXAfp6jE-DJaEsjJp-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات
|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22278" target="_blank">📅 16:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22277">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UY9bwBGrrXbPJzZPXaQ2fW-oBhm2EnABplWJn3zos8FVw_LPpZZ9aA-kENMoqSE_rUx1QGtpmbu-Snp5muXY9LTPbSqhPqyBuyLueWx7HPpoIJ3d-HAOPtN--oDkJzBciDmhuOBP82JUH43W9AWn5GNlc_08FicePAu16jHsUdIeOO_yWzVKhPCO99sKdGFVbW9dYhU50o5Trs9mA61WLNkxbt0S-hNXE2wzQZzct0Emc-y35uK_U33jk1bxlRbu9BvG10pRa8JDDzi8halwJj4S1kwN1MpK_mWqm8v8stIDmATj_4bWNmlsfbRFo7qRY859F_xCzXOvVy4K5vIv5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هری کین بازیکنی فراتر از یک مهاجم؛ توپ‌گیری، حمل توپ و دریبل، پاس به موقع به هم‌تیمی و گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22277" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22276">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCAw56jEbG3TudDJB9NbEfUtQZQTWLAJUSOpTK8bCq5oASZh0n7bebemejgH9UsvBzPhUTZTBbn-7Df2fHvk7Kl0yVHBH7WkpYSJpUx7MZYTUbAZW-4TLik8Q5LwlIq5TVnC94w0o33hEivleGGn9ImWBQAHbGL0-waxXFsGPUbq4dl5B8G2hMiZZi0kYS1CRQiEBlnq-64n-n8vRHGmMuNizOBkvCiExkjEIisbrbYQn5NPcOOo7uoyRiS-WFOr0yz7UoT8qM0UufitBN7qPoAMEoktZypZKMGGaBtKlXOURMhryoFgo8xeBM9gItd521xVhDIfHNteu8KjMHYHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22276" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22274">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pI7akCO72Wg4gGhlJgXWFP2YG8_tD1Cj_Ca3g01l-0QBgLmlIz8lZoZ16GpUvQi2b69jnpqgwoJ3PqHP_7p3Zsk6GHFsreq8UPo2ICzVdZlzLikYtmghkMFuomgdOX6pWaRO-sRi_CnmzfwnjGyxz5Fq8Xh9F3TQBjV5Y9TcV5IZnmCw98R2YXo9bOMhy_6riTwkgVh6YyvxnJWe8qKUMdm8bu2GPvg8vGdEnCzLW4FZXORVtFggAwLemLySSbLwIhqRpGMLXsvRQZ9SHFF8deZcnXLKn68vECNp5dtfi0cRgdM59RJHA2Ms9Y4RwP6O9_8s9h2ZJWYeaPmBpW0hmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌گفته‌‌روزنامه‌های‌ حکومتی: اینترنت بین الملل مردم ایران تااواسط خردادماه حدود 15 خرداد وصل میشه‌. حدود 2 هزار ساعته که اینترنت مردم قطعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22274" target="_blank">📅 15:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22273">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j24cmZvBzT9Ct4I8EWErk8gXgqUemCiajw9ZWrzNdkcdbCcWd1OENfx3ScMOizYRhJ-_d85a80derhef1c_4jkcitg6KzhbLb1l_0c1GYF0pDsb2F_9I22BaLK7G5_jkqc1NKS8rfJHOq684z6iLUIV8F4yCo35PVrPgGisnb1jWb2jazX8YK4eT3U07ipSDMDxSIKL3kfSxmVL0WO3Q4u9Y0oSUFsi-aldRem13z52dlkXEPuCqFymKA6Pf9eDj8JEX2btMPQjukan27pKuYpoh8oiQN4k8mRj4OSVkFfaa7NwVmx9RBmpishxx9KZ0_WXZ-exdAhCJGc821k4SRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22273" target="_blank">📅 15:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22272">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5Q9gXGeziE5rCIQn-qV2h1jXXfc0b7rOowHIT2Ju02RK0DfhSBE5g3f5HktcTDAlvcjLItCIyyGayQ7aoBUl4hh6YwO3zcfDvsGWW5Ki96WKwWyijMm0r13aO2kqwpQ3mQ3ipaNG434y4ONNpH_8ZuJEpm0uiQ68x6RaBWpcCasbFbk504paBfNoXIbdOE9bQh2RlztpF-ZlcHQGQNcjvMlvuAKv9oHWgEFZmD_3VXRjOJuO6hcVeXNSonBL1vYH1FI4wv7R9-YE3VTTjFw4mZtd-b7So--xdp4oA5839C3mRmI9BiXcQ-_QpjsUdYpsTcN2CKzR293IoJzaEhQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
درحالیکه وب سایت ویکی پدیا از تیم های حاضر در لیگ نخبگان درفصل آینده رونمایی کرده و در بالای جدول هم اعلام‌کرده این جدول غیر رسمیه اما برخی به اشتباه اعلام کرده اند که AFC اسامی باشگاه‌ها را منتشر کرده و برمبنای آن اعلام کرده اند که نمایندگان ایران از سوی فدراسیون استقلال و تراکتور هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22272" target="_blank">📅 14:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22271">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=IeDpfBF9TXDTwbXA38vLXPonJf8K9GB2VF2MBvGdn7RLlnuCHxgJ5n9ed9iNMXmSoBW0VfTLrmr9hJ1XD87VXMgOdFyVbmvuMVEV5IUNlMZ3et01Axd9KvHKYCDzJ7WKEXtIGHPopxWY3KNk5Iyt6UTd4Qu1HIF_6TSDqAOJS0FawzDebEiy-YCHrY8KJ5OLMtF_BG9eGFFGBaQPBEEjl1yy7NhWDjP3l_EZZWRp77duIKmIr0IwLZih_sEaUzuF665kmCBSXl25jCEsh07eJpzVWEKS7fE1JwpPyPp8RVhrH5UQhXWDK3mBkw2_cHsTOwqeIlSk1ee4SYpGvhOqWoRUQmJIlN8y8Gz7Svu36rTeU_M6Rf-2YNv_nT2Xp18lFjo9yrjIvQEsuQjhCCKl_eBsxhTey-5nfCTmLf4S0KXVALxsVw2MtoD6iB7o4gSprrjysWGXyx_SjdAYxOyxX7DkpRJcHME738d6rczBvipAXvDlOMjGDtgWeeMT1IeEYKKaSNZ8nF12ndwHwc8PKqclgcfBXk-MfVmfX0PcZ5Bvz9t-od1A5pdx4lyzCbbPVdF-j-eQF5biw0CF6b0rPPypgWmOVv8ChRSEmKX1uqCbPyCthBAo3EjRQlbOJB3qsxnirH2OD4fCisUR2kDofODDtnHUMrUK4cZrhGW132Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=IeDpfBF9TXDTwbXA38vLXPonJf8K9GB2VF2MBvGdn7RLlnuCHxgJ5n9ed9iNMXmSoBW0VfTLrmr9hJ1XD87VXMgOdFyVbmvuMVEV5IUNlMZ3et01Axd9KvHKYCDzJ7WKEXtIGHPopxWY3KNk5Iyt6UTd4Qu1HIF_6TSDqAOJS0FawzDebEiy-YCHrY8KJ5OLMtF_BG9eGFFGBaQPBEEjl1yy7NhWDjP3l_EZZWRp77duIKmIr0IwLZih_sEaUzuF665kmCBSXl25jCEsh07eJpzVWEKS7fE1JwpPyPp8RVhrH5UQhXWDK3mBkw2_cHsTOwqeIlSk1ee4SYpGvhOqWoRUQmJIlN8y8Gz7Svu36rTeU_M6Rf-2YNv_nT2Xp18lFjo9yrjIvQEsuQjhCCKl_eBsxhTey-5nfCTmLf4S0KXVALxsVw2MtoD6iB7o4gSprrjysWGXyx_SjdAYxOyxX7DkpRJcHME738d6rczBvipAXvDlOMjGDtgWeeMT1IeEYKKaSNZ8nF12ndwHwc8PKqclgcfBXk-MfVmfX0PcZ5Bvz9t-od1A5pdx4lyzCbbPVdF-j-eQF5biw0CF6b0rPPypgWmOVv8ChRSEmKX1uqCbPyCthBAo3EjRQlbOJB3qsxnirH2OD4fCisUR2kDofODDtnHUMrUK4cZrhGW132Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22271" target="_blank">📅 12:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22270">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfTQinDaTFnk7QW_0DaF_GyKuBQHxecnMDhc_Jq9IXNNmQiwlUEDbg2V8CF5Xu3ulFEnBT7bkY4MzeJZ4AdRMT7DKAVBrDra4T2Kt3_bGWJbimFoDkvZW85fWzess60jimd4OtogoCZAMNeW97Px7SADDSwpLxGinCxT7nmV8cgKcF51DVZQSK2YQu_q7vfmlbh-H_wMOVadOJqeDqY_OPCU440TZjNyMRyhX0wF8j_kIhh6bbrTj1dBJNuOcg5HDUqwHODR5abJWFLqGfOMMaqbpkj2oQwFmzZJAB4TI8oJJc-QHy7fc9ZCij-vSreMuNVO5GZ9yAVW0uRl4fc_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دنی کارواخال کاپیتان 34 ساله تیم رئال مادرید امشب آخرین بازی خود را برای کهکشانی‌ها انجام خواهد داد و رسما از این تیم جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22270" target="_blank">📅 12:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22269">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=ai73lw0gFsw82qJrie3Q3bVNRernAawi6a-pPDdBAi16ZAW81Sl4U3iROVF4XN6QwZJjaZQ3-NgQ8bLUG7VyeDVqivUNb0fWA6N02t6IxXBIondZHxFUrakfSVld8MWdR1dirDaV6QOk4ZY6BzrpCYL2Ss5QePWa162zXuYWzQhw-qn-Sjw1eHbszx0H5a1FcR7pRFZbWRQFxIY0fpqDv38LC2XuotQ1AB5uOtYWS4WhvAKEHIG291tT-UEUd32bZQAJzE-K6OECDhZ0DxDpyUy42qn8_iBnZ7hb10AlyuF4AuzwHDOPuo6CGP1yjJeMud9EAhyYgxbC-LzJLRmk3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=ai73lw0gFsw82qJrie3Q3bVNRernAawi6a-pPDdBAi16ZAW81Sl4U3iROVF4XN6QwZJjaZQ3-NgQ8bLUG7VyeDVqivUNb0fWA6N02t6IxXBIondZHxFUrakfSVld8MWdR1dirDaV6QOk4ZY6BzrpCYL2Ss5QePWa162zXuYWzQhw-qn-Sjw1eHbszx0H5a1FcR7pRFZbWRQFxIY0fpqDv38LC2XuotQ1AB5uOtYWS4WhvAKEHIG291tT-UEUd32bZQAJzE-K6OECDhZ0DxDpyUy42qn8_iBnZ7hb10AlyuF4AuzwHDOPuo6CGP1yjJeMud9EAhyYgxbC-LzJLRmk3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
روایت همسر ناصر حجازی از پادرمیانی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال بدلیل تاخیر در حضور در تمرین بخاطر تفریح با دوست‌دخترش
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22269" target="_blank">📅 11:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22268">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=ora3lZoJLjGfVkT-nHS8g2IDBTe4WzSc1Pzrwgq1fpXqlk0INNVS9w7iF-A7IS-IYoqPAOelvE5Sx9P9QxAmvsEeYm_aWjHY-JKmGzvwjz_GfEEorfrXiC_AGEGR0T5ATWZotTzlxyMExzH72j2mhPpymAAAP-sU6L4gBfTt1nmysleZiFNjy2Jn5OElLou8_iOdzX4pUT8-Voma5TgOy6ecIk4mhN1ImbEP5wYCzp3pUB5YcUaTgNKt0cVg2eU2BdjFdkKyADxqK32TmNcmAw01APqt2LQnxM6qU1d79TbYDNsIRsz5x_MxbmdpkI91Y39ok0KvjWAvsIumCa0V_yPP4-oq_IaKtcHL7jaZSTfUB73aAniaFAw53SBLNK5B1LZ2-ocdzBBsnq4Q8mz6Ovjn_fkfIpFOyqGrBWU9B8yqdSq8BAoD0QgHIvBulLvX0L8pe7gArhl6siFzPT3gLRG01kMfgsrcgQtWs1PmG5MxtcuhCeZGcNLKJWB4zq_EqkiPTzThRnc00AEh3yUHZ9IWrQ8j7KRChr5pLNpoD5SgR_K_HAvIPRTSf7QY9o4bWzFmBIxRo8MKXxAcxsXYncISRGrD1g5wEkhofo4JInfjQizBUgPoJ4lWsUhqLEr_zcS2pkYi0AdI0xqXxI89DEQlCEiJv-tR29qZI73JvZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=ora3lZoJLjGfVkT-nHS8g2IDBTe4WzSc1Pzrwgq1fpXqlk0INNVS9w7iF-A7IS-IYoqPAOelvE5Sx9P9QxAmvsEeYm_aWjHY-JKmGzvwjz_GfEEorfrXiC_AGEGR0T5ATWZotTzlxyMExzH72j2mhPpymAAAP-sU6L4gBfTt1nmysleZiFNjy2Jn5OElLou8_iOdzX4pUT8-Voma5TgOy6ecIk4mhN1ImbEP5wYCzp3pUB5YcUaTgNKt0cVg2eU2BdjFdkKyADxqK32TmNcmAw01APqt2LQnxM6qU1d79TbYDNsIRsz5x_MxbmdpkI91Y39ok0KvjWAvsIumCa0V_yPP4-oq_IaKtcHL7jaZSTfUB73aAniaFAw53SBLNK5B1LZ2-ocdzBBsnq4Q8mz6Ovjn_fkfIpFOyqGrBWU9B8yqdSq8BAoD0QgHIvBulLvX0L8pe7gArhl6siFzPT3gLRG01kMfgsrcgQtWs1PmG5MxtcuhCeZGcNLKJWB4zq_EqkiPTzThRnc00AEh3yUHZ9IWrQ8j7KRChr5pLNpoD5SgR_K_HAvIPRTSf7QY9o4bWzFmBIxRo8MKXxAcxsXYncISRGrD1g5wEkhofo4JInfjQizBUgPoJ4lWsUhqLEr_zcS2pkYi0AdI0xqXxI89DEQlCEiJv-tR29qZI73JvZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از تکنیک‌ ناب‌ودیدنی نیمار جونیور فوق ستاره برزیلی‌تاریخ‌فوتبال در دوران حضور در PSG
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22268" target="_blank">📅 19:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22267">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJwiV_S-Zh86JfKecbb3AoCUsnuv_SMsssK9o0iKlhC20qDK-dAu6LD4UsVKbdWnjgp7k2gBMsw2st4djJcALQ1P0nEvVA_jL82PhtLIelaMWTM4DfH3qNVCYwWOR1M_6lHwSuu_3r2LTiKRukGRQQX3bdSCTCMkLUgvQMi7HEOraVAD94I4XKXV6UcORP6f_HfOb3GcnFpj9mOwG1bZf8Ti0zFGSZnvhlqf5U4s2QH5FdCQD_mWVkgP_C3ijwcFX3BzEJOTF1Si_br49mH9pSHRYyKS2b16Dh_BUosPFJUF6Rnqr3thezN26ZWmM6uAaBchagrfZJkNLcey2NOJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22267" target="_blank">📅 19:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22266">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFYk4AgTrLjRyWkl2btTtoNX_9SRj8M0moo_RiOzQEkleSJH2Yvn5TTgNJKABc39f7IUHeZIEdIqez4ahzPA8pCuthLk_-zB7NTaOwJ4Xaoj_P6AbGxVxXfw3u--hzOUBaBRr4qCM4Lg6GA-q33ktydhULsQXm1tBLVn7oinbSLs9ViwMsiD-3pgNNAZ72z9GJ8GmMknIvAKIhaAFt9aLHuuhYPEXQkSd2iS81Dktl8h8CMC0hwYyZLKREXuYgrFQrxs377YBAUnc0L3mglDmSPduV9XT60KBi4Gs5GMBuCg2gOPk5ab9adtDPa5Hrp0s8NOKoB5fLwlEZqEmWZHqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22266" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22265">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDWFOolOI15wufL9lh5fzzZlMCdo_ku93kL_wbzz1BMBSiuL1wCCnstQ7GHiAP8k54MBPPF8QfRXynu30pxF3xmYfGTWA6ESoIhuvHMyu77Dq7HIKFkuE9Xu1u1eMoc6dCj4II31db9WC6SUQKU2kFOhnke256-HZcBZQ_llENADyCLEA0JbAAJksKTvb-4MnUzCkM0UqbIWuI6kmIBuqbMIbBI808UjUDp9zc5SKhYTJacLm-hy3eo_2k1RYYLQw13x0Jo4LlGsEbQY_UaKbHEaIQMN0Huv8eaZHExAgMq9EJaVanTEjILR6bUvovlfJ9DNK2PvduiJbE_euxVWjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسمی: پایان راه آلابا در مادرید؛ با اعلام رئال مادرید، داوید آلابا، پس‌از پنج فصل، مادرید را ترک خواهد کرد و در تابستان، بازیکن آزاد خواهد بود.
‼️
داوید آلابای ۳۳ ساله، ۱۳۱ بار برای رئال به میدان رفت، ۵ گل و ۹ پاس‌گل ثبت کرد و ۲ بار فاتح لالیگا، لیگ قهرمانان…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22265" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22263">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRkgmKF6C2B3YwOCtDLfM5EI1nesCA8BT7O1LkFxcC_XBUPf0c36tsZ5E0vVdKXqIpD35qNDs3Pwetq_YPV8Dh3DDYKQJdrnaTIq2HjJqwJod0Nq83TUAU6-CYIGIKt2zk5mSCVVV48xfCvrV0jbkxQtL6QF9sNeUje5HOG9OAYrZNG-4mLYpRbpa-w2ZdTvQA93cZmnHw4CmM8Qa5iDckgp2KDWObjkTUcLQ8uV6Tj82yQ8g4F1VFtqCbO1xLxp8or1FiDe9h8BXqg_UW_10vTqBlxqY5RyETa7ThlifawMNyiUgnv7xzR9aF-zzxOdm18nXxNdnnJW3rvuDNSpxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22263" target="_blank">📅 19:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22262">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRi33X-8OqzybTftlJwT0otLe-lWzBWOoPVcuXT3SGHsvxD4uuh5fDFDrVDGDK_50kUc3uF_HTjhrWylnvTGqA_FDd1RV5FOTuoiLmXPnekBOLVOIM8UaqD3mU1UVGRj85R84LXb-VtA37Xp6l2GPXCpIMPkrZAoMEvwuf1DsrQPtKnRm9FYRWh42OvKiS6dqKxrY3w_bQNvBM2Fv8Sq1Uy1CRy6ZrI1K7AOeM471vM_Su7_1rS4NU19InQh85fNI686PQPLfSIoD68yxuVCPq6AsW6M6OJN7AqIU5KAdJaeYaNoAeXeIa5K_1Y7A04bOeu9_45heYgy-z5RuarAxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22262" target="_blank">📅 18:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22261">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zrt_hyMRM5SJItNqWQrCgTd39wLRvw_Hs6YyHwQXjeeW5HBWdxTNj5AYkiS6v-2IIdhkC6mnhbzd9m0A4gdzbG_uSHlvGpiD8mOsxKH-9_cLu5qR3M3ivMfYpoxv5egeCEjw41YsBIKJ5DDAPKlVfdIsZc4kNtUK2SCVO3burdj_YzhKuZELcp4TkYRSVcIDhgV1_z5OD5N-0teJLrnvhYnLT03F2_88SNcV0iZYEzCo-fTD6oSIzt9ERCLUaCTlj3-OK6DH6IyshFmgdmwBkdWssIHKklNliU4pr9iJauzAXobWff8mbYQK6Bk4ULc8QO82OrbhEGItPbx5EWjUOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22261" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22260">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRhfLqmGxbtZYRdDMpyrmn4GTnDn2gxFEHRCxgg-yDd9kTHDzRk0n8mJO3VRGdnjuLS1JHnViiDjXVaoL1mSAsuweIu6P7aC3uPXX8vy_y9Pu32uVAEI4SlLd0vcNy3aHHTMGKJWQWc7MGPSPHLlBPF-Y4M9QRsOhQti3bpLtPByWTPI53dXu_rt0ncsDV3nwo-pDNgbxI9F4x2k4HcHE8AgPuUQhgX9x4j-xKuzTuv5JRTqDJ6oZMx6_YoVXTUFhi_hT35CGcUR-p8uu9NGMrjHmyCDoxQYH_eBDY_RX9a8mN4SBjLcZoMtParoAOfkwVfkz3PZ9TDQUrzhobMpSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛
باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22260" target="_blank">📅 15:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22259">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r43YlmSDwvPf2ndV58pVTqXkFgxL3EkX5LwOdRMDtJIkw45BjJJCbEtz_Vl98KnPRSFINFb3oRTaDZJSLBI6rQjVLw74h5WAuE0S7mg4r20W06h2xPcHcD0F74kAsRvFUc4uxLY4oHuJEbkg_jeyKYFTEnD4i9B1tAPi4zLf0LGyaVsNBryKdmfpcYl72QWOpLn9FxGDTZmTrO6HclQWo6Vf8wScslbX1LEFTrcjagd3HZIrp2_Wuy9TZCw9ILlzPylzXDRIxD2GjGt3Lqya4mcOombzQvxhBfxF20_qolEvgDsKA4UXgZ7xtbeAe6xrD0UOfReyI5EpJr0q95SJww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22259" target="_blank">📅 15:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22258">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZpltP73a5nFP8uww-dRomhj58HsOJxBXNl_pVGk1Gjs2z7DRrYQxeq_lrYxwgVZJ6VMrruZhWc6zSaMfecaiaHKVEnl9lWCgSbhJGL77enT_P17oppX2Je9L4JQQ_EqSwP_lThxfTrjAxPX1YbK-3g1qQHjD9jtWhroLYl6mYSKkiQfEFymY13tCHsmuQC2UTWNC2_a9Sfv8eqkyQRBdECK0-ZEqZOWVCJSp0Ld1kuLZColW80j6_kNbMkXXUoIjR8ZjOgeeNxSPv9V7yJ6iZ90sQvf8-wwJ4wjFg-aPg72zFDVIHcV_k2OSUUAQVoMxlMwx91w3z1BFpQOGDXRYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برونو فرناندز ستاره تیم منچستر یونایتد به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22258" target="_blank">📅 13:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22257">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXafzWpRVK63CSNiTNqvX0OMpgH3DX8V90huJojTSe9m_T9Tp3n_Oz-pF5P18yqn3joi8sT6nrn4UqsL-mF5xahw4oBgSYOAXovVEr5Tozls_xlq83isFFgSe8PVJF9-LEw8tKN_ZDxv7pUUpOHJGwqS-DZLrDXgcQKQ3SuHlHAxM1JtnKqGBPY9lQvEf67KU3P4fh5TAMaUlqT7dKQEn0opUVBySNESMWAHZQybDwEMyz58s2OocekClIRjcE5xOv6vwOPDrp4U5d_GUZk24n6-e5qP1stnPKdZ4o8yO3IBR65_bLpzT-bKH3R49IqN6PGPy1kmLr40EfwawBKD_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22257" target="_blank">📅 13:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22256">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUGExLNNA5k4QJWS6x-68yIHyWCnCdFJNJMKB0YclvZe4Bcar7E-ILVho8WZJGD1HSeePSJ5Qg8jkxgYueEh2QUjWOIcXp0tE3oAPiSUBZHWkiarbcUSPyTQ2E4f9h-gkTModzE4Mynkw2h0v0xp5fN2ZCESMyn339zLAHUpsDZ8Ic4_-xGfUvNfSiyIl6gNlTs8VVsbCBYRFj1nGb8xF391Ogp503yrDum32itcYYpCtE7FNZp1XQY7ymgMqXMMyaJgh6mdtLUWPj3F0yJxozYQzXOpVxu3lWzmLJp7g4wxt222-jkE7JGKNvOOkCtR5bnEKTCrRTso_4Y5fuJ9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسعودپزشکیان‌رئیس‌جمهور: اینترنت بخش جدا نشدنی زندگی مردم شده. دستور دادم با نظر رهبری و در جهت رفاه مردم ایران بین المللی وصل شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22256" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22255">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bizr_9Tk_4om1yjd0pDj0LvPL0EvAagTYKdSv-sA9tw_-H_iJJgMKU_Ub2pxqb9ZG0_d_sJ1uLv-5a82h9S8gD4gI2PUI0I-zrC5k2KbBfrlde9lAW0ss_7sRuRRR4VFhy3qwIByCZ1KHos4UYfaKiPB65HbRpSG5abhg8SX464XeQuUNLDpgCYF2RXVnlPgaagrJoNUCNUDfUo1xUdEZpXwU9gEgAz-Kv0OIdTvzaAfGFgvMH_CbCPPlTcJm5YVq4BbnAt_WRCxhPCtJIUrOmPTjoLpElPviJceN3SuyrOkGA3KwNiMh3D442Hv7thw5wHcFs0eX9mOjxosNIEMYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22255" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22253">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJeBleObrVT-SZJqUgfcvCePMovJCQTgnZzq_elE2A94ivx_ZApTynoSp2DpvQKLFD2Ks6gTPF01MNcysR17Qio5SQLv00x6JzRT9JC8MD_Lbt_c5YkVhhsCxgY-mQUeHXE0mktkpK-U2GnDvAsMvVTyViaP0FTlsg9JU5MCbPV6P6XCWvp7k-df34ZNQuTtWMJJpepxMOH-2TxZZ5uj0le1bhjYMLK_n-86V8Mw9IxLgJPG_5ZnjrjYQ4fRTlEikCXLk2KvB_rJFUbgbQ-TZU8TsNxsDMRHnDmnB9lq1imPRhRjpqceLb0Dfv88E1Boip5QoiXWMqrwiGB0tP1IwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فکت؛ کریس‌رونالدو به‌اولین‌بازیکن تاریخ فوتبال تبدیل شد که در چهار لیگ مختلف قهرمان شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22253" target="_blank">📅 13:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22252">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTuti_QEG9_vF_MyXI-Mz0XfdoQqgvfUHzp68OUzSdGzoWKO0iIWHAcgpexyO4_rVUPyexCAfVcfu2xFLhOoHjm11bLDdX30GzOjX8y7u6VEVGaduyiTVnbKPdfIe4XOudGQOk85rv6s4WYV5cAQw_sNl7FLiAzwhzIcqcUTu4Lj7GSGL2HEW2c1FPG62h-I9i42zTSzsuPvCCJVe0MuGirCaLHjy7H-3UhyawA4WGfv2aHOrzykWQJjT2sAToPOxNC9nEMgOYcAm_9w-dQ5ahzzYCJaCfrdPFGUBB1m-1sX2oCV8QhpSNVGENIrqvhXqhZNmDtynnm00kMqbczzHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب فوق ستاره‌های توماس توخل برای جام جهانی به تیم‌ملی‌انگلیس دعوت نکرد؛ توخل در مقدماتی جام‌جهانی‌نتایج خیریه‌کننده ای با سه شیر ها گرفته بود اما درصورت عدم نتیجه گیری در جام جهانی قطعا مقصر اصلی این اتفاق خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22252" target="_blank">📅 00:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22251">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raEwb1T6XXdI7xAVt-SbGixA21ln7yBOWqDHJwWPdlqocCcpIw-U-mF6JLq9j6KaN3TQPND8s0WhH63VEly2n0Mo9rHy8D6Z3DIcY6ZPpu-6q38sw1GeWQuV3MnLOOFoZ56vDMSRa2bHp0QPyGwjRuxoEAJ6utvvtuJalCFAtOJqZs0IwmG5st6ab0k6P3NqWL8iArwEidgPIlq-fssKmblLiS-QRwnWMDsMAjVKVgIBwfCxQCmLT9pVJmzqCVwE_2WM7n61Z7XX8p_kc06XZA6MMigQwLZcWIJunQ_YPYwewTDFUjcEoZKduWeCHa6dc0rkXZajuL7CWMeJganw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22251" target="_blank">📅 00:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22250">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ek5tnUnaTjOu1LvTswtwTd4Cf88iN0qe2-WDYs69uBFHESJWKmhqmvsAlnFnyj93tbT39CvSbXGk-fpbHfQ97AYnU-nd04SUP2kHs1G1g4CCSAc8rwdBIWlvw0Vr730vVkdpEXtqpfTE7Q-UWC8q_56Og5P4Hwvsp3BFQdGLnaTE-SRUdzdRrOq9FBB9HiczXSFn7RPbtgo-nwdRKahxGAxmoyXwoF4-RLZiu0kzKTTVjHtIkk7-vKaFytl5CNtuvoIQIQw9hHSDOEvlAi6n62K8qsctym__wJ1CN2rElYnYRrTONYCG9oYL1lb8IoFl3gVqjN-Nm4wDF7RQsWcFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22250" target="_blank">📅 21:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22249">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4uiOjJ0AAOp5xP3Mgfvh5L2GcmSDuf_t0mkT6sgFhnWXx-lkIw-n6bNg6e9fViTtt2hVeB2XCcaWrAWmOsP6pCbQmvIz66Lq4Ulc4dxqWPnXd9wfWYOyHjLSUfVjZgYKESJ5n8P4Mxfj9VSc7SyDa88mgB5dQ3u4vzFHTTuDtg_VYqoT71Mxjv1zDysUpvvUOPqnALfbV8MsTJY44uT-wmPY6DwpL3_FbCSNXTrfHLmtjJA8YtatI_Pn-xcHwN0OS5ZbVm-wQsCFfH-Z7UhrTkYj9KhVmF0iJR8NQKjOvXOgTX-cqfpvzjyXbN1Zq7mXpLvOSOTNHpr4a2UVcCTcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه اتلتیک: باشگاه رئال مادرید به داوید آلابا اعلام کرده که درپایان‌فصل‌قراردادش تمدید نمیشود و رسما در لیست مازاد کهکشانی ها قرار میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22249" target="_blank">📅 21:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22248">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GF99Fn7a-xwswCm4qjJWFYPbT-pobPJuuuyubzRbvTF3fSbJ14Yac0bN-o0KofCTf-aUV0hn3llBn5KFi76JCEmvVL07ptdc_MZwC_ULCobswKdTt83kv4vmAuP8WVjoAzNFtEoszB68NdDMiejig5AbkxWsDq8cYzLaTZlQpe6yXKcuPI6vlY5F01gTkV04jr7ZwxpnXPA9TPOS5oN79vpprcGJVNVCq8jvp899Jrhul7x0QjWE8ux2MuC5HapADURNRW3K31n2uV12tRvVd4FICdDcpcyqlZ7wLBTPOEMzHc2l2y22CzVbglniFd_rmvf1jZtHGXlXRtONJKp2Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22248" target="_blank">📅 20:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22247">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkyfSGHdbiSH_6fGqwLRA-ejuyAajSze1GgHsT0gLA5nX1yA6W0sf6Hk2Q-lLAxO9PoBekYaRKLJ7bOtMNzKXfmiUiZDx2CTeTTjhLWw2BcUfGFSWbnW5wTfgrfSySCCWrLFZ7kvoDYeiYtNci5031Mx6LQvzCzk8EeO9J043CrIlRtJOVoKGcFK-hhq0IfMqhIyDqkGgknm792-ev6cHzs97RTlo0UlB-mA4ABXhXzEB9LiRZ5iUUVj5DM_pU3cZCr_Dy1LWdgNZa4XWW146y4WY8sB6jnDBw2MPXB2F8PjJGxT4nAHoAx7uAaEkWc3wnydiOCr55s8XJXPqbh2Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22247" target="_blank">📅 20:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22246">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCM68L84JMZ2VePFcLPe5Xcm2TieUmG79aD_DDeK6vIYoskzvBSqY4AsrGjIhqUy7CVmHzDlyexMhVuicv-C7baZPjo-GCyWJiGpQ_6nBfEF5Dc2jCg22tEuEx_JMn5X7KHUTRKtyeYPIdq6EjowpuCISWE3tnGVY-1H1rFIolARWxKDrT3yVymum6trnJ82_YyMXGzJQFimQKILc6jTr6q_b6I644d-OE9nfqOKSVI2RAn_G20d71HVmujwnw6FQt3p-ws45AgNdzNEnUUYB_WUsZetIWo1zaVwM9pJuE7jX85sCusVhynIq79CDgsIsPQxB5-tIdiTptJCjPDmOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایوان سانچز وینگر اسپانیایی سپاهان بعد از دیدار آسیایی این‌تیم به‌احتمال‌فراوان از جمع طلایی پوشان زاینده رود جداخواهدشد. سانچز از شرایطش در ایران بعد از کشتار مردم بی گناه راضی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22246" target="_blank">📅 17:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22245">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=Tvec9fI5hYl8wOHKshWPuYSntDH19MDI2V5FHbPR6ir9CCXMGlUx1lukXosa9G9ZOG2Brv727BP_WRHO3XOwqPEceK5EmpPwaj9rXyQUdf1zpyq6lffFqvNpCvIznvRwoSDOO4mvR23vWE9vSZJot6oYnAvDqyQl3wivFtapvVOxFhiYsT6xBl0oxcQBvl42thEdrzd9LEt2eafhPN_AfLm9VVcDkYsKnvcxQML18uIvT5N_UCT_RWaDQ4tqQrjdOrD8yarPwTMIijVfcU06sPdv97CtEYPnYQLYknihoJ7485b3PZFjOBLy96Kpvo4lD7FiTDPwNkGj2zAg1Nk3Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=Tvec9fI5hYl8wOHKshWPuYSntDH19MDI2V5FHbPR6ir9CCXMGlUx1lukXosa9G9ZOG2Brv727BP_WRHO3XOwqPEceK5EmpPwaj9rXyQUdf1zpyq6lffFqvNpCvIznvRwoSDOO4mvR23vWE9vSZJot6oYnAvDqyQl3wivFtapvVOxFhiYsT6xBl0oxcQBvl42thEdrzd9LEt2eafhPN_AfLm9VVcDkYsKnvcxQML18uIvT5N_UCT_RWaDQ4tqQrjdOrD8yarPwTMIijVfcU06sPdv97CtEYPnYQLYknihoJ7485b3PZFjOBLy96Kpvo4lD7FiTDPwNkGj2zAg1Nk3Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌بینی‌جذاب و جالب از فینال لیگ قهرمانان اروپا امسال؛سال‌رویایی و تاریخی آرسنال تکمیل میشود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22245" target="_blank">📅 16:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22244">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nly2QVPg5rZ4yVfHm1bVX3kMddsM68-iiqSVrcKQzLk7vct5KUHx-RRYPH-7BJPo5IPajquoxQqL8LzljGgDM2PH388NJ7XJPRzQIgP0l3xJI2Z3NEdPOA5v_AZxy2eWmGnG9pkdoUCxHypAE6idi61qQ_drNdIGiY0I6xzkygHCIPpHpiv3J9MJqHD-hFwclqSBmmtgSWrEtG3eSmVq6Au4iZY5X_qBqf-vIgSnpBap1_HBvrXrXuKpDZumThi-00B3DUoEp_U6Vf4cXkGv73L2lSkuDxq7or9JIXjmRiZjHK92UM2vs2OlLk94YNVbcO8w6kGpTYclT_RKQN5CNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شانس قهرمانی تمام تیم‌های ملی در رقابت های جام‌جهانی2026همه‌تیم‌هاباصدر؛
اسپانیا در صدر.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22244" target="_blank">📅 15:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22243">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQh69KejAjvNokCSOxflfxzPscQexcvGlZH0_5xX5Pn9_QQ_MgkKMMAoEk0icdVoqeuqsRvWEHSU3A696rlukBYNwBwdZapX7sEccdpSn_63DEqp7eOdkDoEHO0c1waTW2Llmo7bE6WJwKxZYkZOTbk0wknc5q6-HyyCfkhxBU3YuBk824id8euIylLgDXnFiefDnePFd764XEKBqaE2--adTNlb_pcr4g9hDKMBmpTbBVe6cxPEE4E86e1FH4GPWEEt4VlqH_c9LbKlMdV_3BuGa68uF2PqpacE5znrbIaNYPlYIhd0ygbR-S11wBY_wmwxy_HbvqOKtjoK02g8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22243" target="_blank">📅 15:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22242">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6LGzWyUGmUsct1I8wx1qeoQ2x1eOO70Co7rLkxH7uUyYQ0Fa8IjU1P6hRk4Wjqo5Bvylq6YjEwp3-VXo-uRU3WymKH09n3_rSHfkFWYpcRAGp3rmoX78QGZLrcdUfiMU6qzkDgSTTf3TGDDXtkTGHHbyGY9490ltV0poSkOyCUT06k5viHC4xvYyS-sEnzpVnUE3PUNjbBMj2OSWP6DsoU6xLCFozo3T6STonmG_2_jXDnWMFZodnzh6imJR_Ru26L296Own5NtqP3EQvJMrZAiuwWxksgNgD4bnX5lLGBPOiNzHVUL2xZFO8IoAYR1Oq-jtHzPpI804PvYhdAC4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22242" target="_blank">📅 14:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22241">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUtyB_ydXggSeEXlWHzDl1dWmK-f9mvgvFxDe3FANhl4qq5tDC2dPIWhk_jn5A448UcIjXqlr4yB4a1Nr9PbCSfGiL75c9O0i7FW4u6esyvgAR9uOzV8iZSuc6VCIdIU6nmH3dtiI79PsO_zDpwcMKT-HQU_UniVSo49ovp0jdLI5IdCwq6chSHKAisaChj7DlquV7IXvxmkRqCgtKzeKwPm_Iuu4VxPtgUAt7SJDPGz799oGrIrNfrAGsJm4_yOs8P-xl6X0IeNDsbVFVEYL7WGPSVUJL9qTIn3bUqPznHN-3Cdz2D46jkPMJze4RgwQH41oksVJtTs74HdqJQPHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22241" target="_blank">📅 14:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22240">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArUxInd7u_xe96ZhEt92U6FEnAh6NfXYHv0z3CqB_3iXZPDw4yMjd9WS9y8gR54icdVl6SBuTLVYADCsKr6l0607E7X3LwbaAcNqAPVELefvnlQlrzCVQwVZrf26tt8l29cjbmzD97gCi1pW3VDhu61vsp7AJ2UmAkteJIhrQGhbjPAn4LD_I9uuzu75J5wFSzAejmurH2D7iOvw9DjEi54ZzthqtSa6DIiEGnNHK-WVTRdvtDPjNk0LFsb_-_BcnV6LssKv11oZmagqADRWoOlbwHdR3pYNjr_5BqZ0x3Ejt-ES0QJN2sha-0Dwzx9dsWbMJuTeza7VZHwinMhdpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی تا سال 2028 رسما به عنوان سرمربی دائم منچستریونایتد منصوب شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22240" target="_blank">📅 14:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22239">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hu1bpJQfmojDmkMF7DRJs0z0e7UelJknZjeOci00HwkMkZHc2ysZ-OzdaHlexwYpkC3KqdFsxl5mCuJvssGtkXt67g-yi8Im4LVCtdoHXDqqrgaj_wCMjRzqq4LosnOXTXkYqnPG8T61gERQyjzQGYWq0JztItGqIivDy5sxkg4A0-PRnrJ-DwTWTjiJ5Caa_-dHNiNkPZro7EoiNxpQq5f2wrlO6wz0_rq_T8sCDC_WKoNlI8t54ZNXHT8KBO59UcZ3659CKP7oBOdqEu9gr2QMbrvPyomUgXeY18OjeoDPL2wykSJD0yrY6AVP6-Org63DrMwnjqSMPyIesTPIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22239" target="_blank">📅 14:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22238">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAtscrM-5U0Kq1BCVpzoaGvNkxdc2qcL9U6Eb08lP2urMcDKEfjh3UMhP6c8HpuupSTpCkqgRueGrVfA0yQVrrnkkKALtpsTOMsPYQWpvTx7IeY2PHw5urirVTLKVjdwFQ5jhk5YaWDqC9SNfGDSFqEAn4Dgvik4xxpROmG1QqTTEqJPYgaw0w_cR-9X1ZUdbD9_5WlRYyplmR24uALMqggY3cUlGDtm82P_ylm5amePaeFvofJJ4mhwH0OtqMhbZpJdEu29kssMV78TRU2K1Muh30MMvWJh7xgz32cHrrrhXwkr81PKiYIWSlYU8WBuTtNMJLpx-mryRPie5qZu3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22238" target="_blank">📅 12:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22237">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OS7jT3dBw8ne-ViovrwEuf5-VUrSkkqMJeOY135XjsfucUBXmux8irL0_xlLam88pKJnTfuR2CNozz1pZPJ1-sz2au0Bxz1j1fWxBkgxE2hrTm6HL2Ezsf52eAcA3TBMlWtceIFvjM1NiXlJhmUUzeRJAFxTOqr-1Ui6uzQslDy35reCOYTMyb4IxCVd5TNH-O_Io1Oogm8fmdCTI6PqE_vRCKPS8R0VK7DqMO4pChQ8TY1_t2WtA5CAK3J_K3QoiqVyS8ZIlb_14zq9nZY3IbXk8kTOW5ZzC0G2zxtP3_5iSwhQIgx8Pbc27ygfn4nwoOlbdh1XEL9nvf-rc1ByYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22237" target="_blank">📅 11:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22236">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SohyrP2Q7LLYGhkwgoHETyTm3kvA3-4XcY_U7IJSQAXDnj16ryOQM_xPoIxWFIZCeHg5tWSpcSjz4G5P18ig85TLpSTFGByUwutw_GYAkFNqzNH9NFHQRitVzphBnW8-vlS8Vl2pGhyi0po04vI7uAuTB1026XG4WsGgmxNRLmBYNQw7E85rdESB7ECYtGiv4Hx1rJP7hyVvjyroc8Sohk8GuxIr1JPouuSSHz02dLIiMyQ04z-N4Bhoq9Pupv41sskJXutMz8YLg6BRk2vHvt2WURS8IgcMS0w9UE36C314UfGP9I4Px-OCT8IS-QGbDd7yqMXCg_ECr1IpAeAAoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22236" target="_blank">📅 10:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22235">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjXFAzfWG-Wb8EczzyOpqbxOzQkpUKGze2V5Vhl6eHfpgwwoeH48XNHl_smxea_crhQZVqNCDGZeMbpuyiulinR0J86sDbYKAhM0q65WbTNHHBHog4yVNEuZi58HLmWXYIw4UjVb9v4EMWXtviNtwg9rgSXTnlLupZkksPBq3NOvNkDo6TI7u9Jx1gi1tR1CgrWLlK5-zfKeRWszprxcNQEPSReY7ly3yakiIfpsSfvyXkk9p0P-KcjRkRRs1e7IN6pV8JwfE9BTUQHuk3opYhUb99KOIGL2KHS9MHMLQ80_sBUeQjhhYuXvDWcQAsd43mO63RUKioc3FfQTsaENNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22235" target="_blank">📅 10:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pcvyl_GS2t5ghEHkpiYqUfnVD3-7UFFaoAI4svRMvnPA585sjntbWXy98IOms3c0erpdu66qiBpKtQtaySVs4GUjb7Kd_KMxohnvHGcOMQYgLQIcOZ4cSg1pYlUkf69XwOEDwkkM3GXdXs3XaThex4omCZTSg0FLetE_7gAj4O4gCqBclymTcC3U6op-WgbKBoKjlI4jKPbPvimJ8jo8gVzGtIEJj2QGrzZ8c-zkQmt58kyCyBTB-L1lBj1EZWuTxrLA9LvHGLmrM1VKo8CXdDkJjQSMP-lWvmIcUVPsRFdXNBslbR60cG-fPOn0_j3k1p9xhaNCUyYfMwtnjL_ppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_ybCw0LLrt9fkkU9rh-Pu3pGXjKKz1aJi_KCgY4c-HH3aH6QF5uxcw7TaQ6zrUdyKRubW4ds4DTMzjSLgo8m8btSPBuD92sj_EVUrWLLK7RJn7dNMO5mYP1Kx60SoF0M5GDHq_wGxoRZzkQeiDSOd8sw7nOa5Y95pGWCQD7GE0tc5WQpwtFQnp1-DkXalWaRYBZOKrumg5NKmudLW9HX02DGmE5odt06uECaY1bwUvphbU237rxPK6RcQ0wK8xmQC6q-xPP8bolIMaPBwRkDt3UjZphr8BTu2X7UH7CT1v6i78fTMFcMwu07zSuVj01EJE_te3xZSLLz0k36ccvow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22233" target="_blank">📅 00:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22232" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22230">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G31L60lnz5N_HnVDIgIUH8NyDDvYTh5mPUZiRuvqm0aAT7pM8mKeYGOVyRYTZdkmfHGlT8xOOeQrASBU29GE6s2SYJ83NIMsOQ_HBdrDT6mg3YXyBOPM7b462KzNj8xd1ZI29KW5dv-NcSgSY-KFIlW9ZlDQ0jPn_fSfi0AJ_erPTk-OYxJ4QwjhHtcEbXJ2LB8m0G039deGsj5xs7N8mg89SxinJUMtM-R_wfe5dRcEZDpoqYJx-yzkiY8UaezG82vpFoGQUA6s1-bVMifxOd7ZjweARpU_YzS9eV2_GIDJqoQcIcomqRGZY03haycoQF6T2NF_ykxpEEdiyM7pfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ifdpaNXJi-8eUTe18wYBI0lp3Gsr6FkrxBtrqqxK8JVzvqlES-jbVG3AKFt93Jt9WOerzjDcKkGB-5Vz6Hast7ESi4Ry2WzJIe25Mwyqm87y68wMoZXf1wYlieVioa7AUy6DeZpuVdQZaXSOEGnf4xsYeTiSBtA1x2PulhQGYfXK53_eCknHBug75CRhyIW4sPxO2silmbBgvzKgHvIgW3X3AJWYtj5dKfYWCe13-TYnGc5vLlqUbcRW-qKf0uBO6XIAsyR9f57H3mgh72a9Fo3gAypG_V3KUDLj63x8p5NBC9yYwcavc-L0d3VS-aYv0zV-J7dkXJqmrKLTgwlCbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
هواداران پرسپولیس امشب پیش از دیدار با ملوان انزلی به این شکل ازدواج امیررضا رفیعی دروازه بان جوان این تیم رو تبریک گفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22230" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22229">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDVX0Y3bfR6G2zMvJmZOLnKrZJ1GwqQEQa6huKGye88i6MP_jcBGcP1fXu3pwI8vIyDZgXyrk5AnbYSVomrfAybIvwm_aoMdsQzt-YmrjYupLa6P1dFA_iZ-zjK2guW2ajvztP1MDuN3yvXZVfyWFLGzyRqJ2JRBXdGJcp5GWF3dSXxHKTNXr-0JiyZcZLYAmYuE2iv1XrnHT4wHWJjXXDD2NCh-P80g-uD-UbnkF3q3zMOgeBDO1L3oPIQmetP21bY14BqaUDt6z0kZ07ShRY6zQkL3xCIaj7fc7lPn7PZQJj9dV6U_BzY8gTJqIhffua_Byx6U67n8znOznc4WOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22229" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22228">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iiq1n9zdzSbEX91df4_iMkRJnT1wR9MuUAnacXVhz9YmLpA7M-hXq3ND7gP3rMAqO_F1Oy-o4xLyD_CtU4guFkCOped3aaMnoyF8XujepJeOalUdCJ9dQ8Ru_CkyJ08zPqm21Fm9XIJBpJo4Tr48GwrR-zcdYE-pd4ba9e1Cc0bEOvR2yW83DDzYUtK0Rv0gGIi91Ni7a_kYZsGP-82FmR0o8KyBTbqhskvvhdKSMAW_sR7nSbg1Z9YlUtKQMXFzH3XfJqinb8pk5h0eguRAn7Y-J4DPbtHG6pnM0c5sLR8oxaw9cJOYfzpSPvxFJzP5YxwfpGGxR34TDpK7fy5-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
والتر ماتزاری سرمربی سابق اینتر و ناپولی که در دو بازه زمانی تا آستانه عقد قرارداد با دو باشگاه ایرانی پرسپولیس و استقلال پیش با عقدقراردادی دوساله رسما به باشگاه یونانی تسالونیکی پیوست‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22228" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22226">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQrLyULo0bxJAiCHjdqBhdSuI2R27oAO7GMhoR-9Tk1KZOMZ5UbluUDZoKlFo4OWBwWlF_lOk_KuVPdGK4fx0PNbp1eUcsrY6MfOdV4tk80zmI_TVuHXkV2T9NAl6xfvBDtnkVJ6zE0-aw-L2tlnmKZB7JijgTEE46Xz9AV121XN6rhFxAXYXWUriaZQUdhOKC_3dAEOyOsfq3oj6ggkVUZ3aJrbyeI2-wNslEBBjJeUnl2AmvvBYsE1wc6GEomsQxzp2-l3uRaMFz22_U9gqIee0qTUGR1Ibse0zVZL_kTqpuZezIlsXFDnyFX6fT2xExTdHFMqlrSVfTUf5LNSfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ النصر عربستان بعد از هفت سال با کریس رونالدو قهرمان رقابت‌ های لیگ برتر عربستان شد. قهرمانی که با درخشش کریس رونالدو رقم خورد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22226" target="_blank">📅 23:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22225">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjO5ChD3G_CoX4P7TxN8SMB3kEgOkNNVwf6Ua0ZUd-SYcnNatPnu6hsswHtyK2E8avZFq5ZDqzU4xmJX57CULauS5Ov495JDKnWZ1RBuzHPkOBQxJFtjnIRDLob-YEOXTmFsNiOaj1K7GPMeun8edf33B8u8RmpThWTQLSe3gLRvD1al5szzf2GX4NRnBeZEuGRqIpJV1EL__FPqaKZyCBzP_aQzRqx0m_dwAUezKOzZp4CQm3GPfrg0MtmhsbPnXwxjb5eIzrwsjgAxeNrz4hBcVIGIvnsTqKxHjVy1jVwfwq1sNmi9z9WEwTcwoDWNJZ_RuiIYmBHVoL0skNzOSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خط و نشان CR7 برای رقبا برای جام جهانی؛ دبل دیدنی کریس رونالدو 41 ساله در بازی قهرمانی ارزشمند النصر در لیگ عربستان؛ این 973 امین گل تاریخ دوران حرفه‌ای فوق ستاره پرتغالی بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22225" target="_blank">📅 23:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22224">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d569523e34.mp4?token=vjdab1w6BBXysSxbFS5BjPK3z3JcHw2c8-9Xn1dJ2F1WvGi7a5kOrDt_rJP_IVLpxYVoJojak0MsBgMVGpAQWzjMb4c6N80KA8QOgsmvOAz3O1PQnYz3HUUHHR8bLKXqt8Fx0nej5DvzNQvyLD_7UI-eElvkExbup21zNEJqWeDwuJgc8pmFEccI529Smj38wXmHrmzjGVCirjsC_9w79G7XtJMJfb-zCKYgUP1gogWlYAKESESkDyT9mTcqeTM27YKeVU3X5y_PXfTDgJa6y4DFdDV3NmSNjMbG3m0IQK4nahotB9ZLwY5vxZ1v61wDyV6hwjkEl4sw2rAbC9bvPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d569523e34.mp4?token=vjdab1w6BBXysSxbFS5BjPK3z3JcHw2c8-9Xn1dJ2F1WvGi7a5kOrDt_rJP_IVLpxYVoJojak0MsBgMVGpAQWzjMb4c6N80KA8QOgsmvOAz3O1PQnYz3HUUHHR8bLKXqt8Fx0nej5DvzNQvyLD_7UI-eElvkExbup21zNEJqWeDwuJgc8pmFEccI529Smj38wXmHrmzjGVCirjsC_9w79G7XtJMJfb-zCKYgUP1gogWlYAKESESkDyT9mTcqeTM27YKeVU3X5y_PXfTDgJa6y4DFdDV3NmSNjMbG3m0IQK4nahotB9ZLwY5vxZ1v61wDyV6hwjkEl4sw2rAbC9bvPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22224" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22223">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=dBQn7YmRABc5xMWE5WwoFHeN76uFifnfk8Ao6k1QR56ISsHMfNFoSM31zmt1t4TWTf4xWbVOdZMchQWOJ3dDyetAaBcxgm9AeH3FTCmQKx0uaTzl7ktitaFORfbndHG9G6cOzqAc9WoBA4o7sndsCLOYQ4JFTw7CZoJhqO6xpnok6aG84rc8jRy9WyyoKdGFJT8BdW2E-tptWm4DwBKyoi3RCB0ccttGRmis2vh6-qx_frWLVzN3Q-Ok3PQ1ohs-p5o5o4yJ7OW7KTV5WMfcPqERV53KljZFAgswbgZacIRhyhUJg_adBeM39_0Pvd_SB4WGysH38Cs7-4dHtTV0ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=dBQn7YmRABc5xMWE5WwoFHeN76uFifnfk8Ao6k1QR56ISsHMfNFoSM31zmt1t4TWTf4xWbVOdZMchQWOJ3dDyetAaBcxgm9AeH3FTCmQKx0uaTzl7ktitaFORfbndHG9G6cOzqAc9WoBA4o7sndsCLOYQ4JFTw7CZoJhqO6xpnok6aG84rc8jRy9WyyoKdGFJT8BdW2E-tptWm4DwBKyoi3RCB0ccttGRmis2vh6-qx_frWLVzN3Q-Ok3PQ1ohs-p5o5o4yJ7OW7KTV5WMfcPqERV53KljZFAgswbgZacIRhyhUJg_adBeM39_0Pvd_SB4WGysH38Cs7-4dHtTV0ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درصورت پیروزی النصر در بازی امشب مقابل ضمک؛ این تیم با کریس رونالدو قهرمان لیگ خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22223" target="_blank">📅 23:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZJkep8btndqLlhR7kR5PGjbz0MToSh1trlgRFFRpuy9YEA-qxO21u6d6Csb_uZaoBCuVWx6ST7XvCr89JM94UvI5fLJwHCVE6MZPdMrxR2Snf0SCMev6h_eVP_oVYNcwmyEq5O7v4jG2p2rH7btQfuqOtvkMqLoaeUh0Q4GQFpIOnFCi48nZW-HSngQW3bGMvS3eloRwKlZYHiHX9YL2eHQ8wIiY2x10JVwJDkbhY3d7Y0pVai1f_-y9twWvJEWfK6PRM6Tvf2Dx6OiUbucPW-n2QHweRXPp3pfCwyzZqbCpu0iz9glpHIXMXLZrHHiUji5XU66Hklv-ZJAzGujwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22222" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7-Nxtavbd5Ki11eY9n-i8jIVzcTwwTU_F6HkOHLfr942_14wT-J_uSViO_QOD6XyvxNd0tLS2tWy8wg8je92Chltks5B2Nifkyr3MJ_6HeVjD5jSjk4U_Ua3A9Usr_hnAF0nQm34CmVvPL8OrArjN-0YpFjnUJ_3TZ9WETxjesXpPT0KAHEh-qaLtqFdMu61elVFZ1PasesKgQzLqGqpA-08DxbKtgG3Id5IL7_zBRoS7a7nOZn7ETSJ-mWe2tHvxstk_g5lV2hl5ow9RLmp9BqvgEwNi-rrFU3odH-5FO9CuQ2fn6bUuveGORylJFpQgZVembYZ-0ibktS8RFw2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام فدراسیون فوتبال؛ باشگاه استقلال مجوز حرفه‌ای خود را از AFC گرفت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22220" target="_blank">📅 19:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPhUKGmMKUWirShCQOPOj1JxtaPggNAMv5XRPg5Y5qG14eAYRqrUOGd5wbJ49huD9VAZ9g1saasKgjUNkcQpjFQNZzSLxn_lXBohdKCv0i-VenTQ7MghTSqd-Pl08h3VDuYJkq1sozf8B-yExfLEpgHDUDyFDjyCWI6tT7QEieMJI5g5oQ_d1SZiTbLRZAFYYUNTahnAzp5r51O4I0PV6nG7RRTBEuegwUV-bswoRviSJ3ScjS2GPgVKNTz38_FPflmOWsx52H6mgZbvS0V3X4ZTIJ73hrWKqOlOBq1u7D1DM7DRPIQQ6ldXQRxbhUqkVQWsfkeKUC4W9Da-v6NsbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpXW9dyKqkY0f2Tfp3qI0ys5QeCsQHMFY9MTxc86g8gb5xjLXsYPH-Jo44wQsC5_aoO-S1ZRHdFj9smbgAV8f3_6qzUsWfMFBaucwJVAzeHOx890X04XlzsK38t4OZo-1IeNH9KCGHGAwRYjMQ6rfhYkLTf3BCy5uTPxpEo9tgGnMiWRVYAKZLMiMWO1j3G0oe_YlWWtpkZ3IS17qbjh6brVDt7Lh7VGh-K5uO4gU9XEX0vv8otX_HYLfOccXvbLS04UAYthgkoA7VyrzULa0UAUrNOBIE1NtX-5hX71L_nL4g9FhfjA8PozprmGDWnxByDxsicpPHH70_yOEpUFuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gvv-DjiMrPOOl7c_b9PPVOwN7HSUZTgZHJdcLxZuVDs8ZPIWkaIGeDU9jQ87dgT-mLNfvhDp64rUeHXMMJdJignAD5NxSHYQeYVZ-xVDNQBz2i9f5pD-OurAAc6EX8cWW4Y7FzTfB2RrR_YCA1jiQiI3VQXx-JUi8BN6hxFnVddF3B6MmspEsaUfV9P8QelLpSgisxoYmYb3538dXxghu9vFLQwJCN9JuatLhZWD2HJk0gtnEZCSnXiZpZyg_p8pe7-0xXiNhZm484bfcYc3tTTB-n8USTVCxVrdxlISwIVmSbovdNb_Nenhua72O-6xgsUaAiiIhuM7krJsHAjVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ4Aiwat1BOyM4OMVznOrnDNLt3EgWFr7R7crNaMHrw8n0klQ2-zPmNyfg5nfQSPvBxui2coA9x1-bENgKuLlDsxyXIxAWfizkHbrTRwI6rBu0buBJV05T_8hLxATClqr_4MgxNOzPTjZGmI1zBz-hiJ6m8kmUCNDmFvwSO2IU29mnHelgicZ6XKPsvEwtWAksCoVPFkixXUAGf5l8dP2pLhBHT8aAQHhb9Pp3ihVeVG6xTdJJEr7Qb8LG9shn8B-nY9w9ImZtV4q3GeYiiabVgeHrnFT1xBoRP-l9JIUXKvpSpQfhzJeJSS-VBk1OHuCC4aiQ7zztM_ZiKuLpWdpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHUOStZojRcbnoBczMS3pfo4QYeHH51fmzFu8CKZIkGZIFn6q3stwSRURTNNp00FVfL8lObVLZ4vcdGd34JgS9pbM37oxae8DSamwZ1VwEGn29iHb3wKTl7LHHdsdV3iLXhNTH3TI3dmatVcgBcQK0VZ3lBxdNEwlDQczjijxzs__-sd17Gh6z4yKde3pQIjPAztUh9YNvzeAxBhS3ZkC-mbslKD9V2_083a9V8zJtBzg00xVrCl1-UtWnajmhRHl6l18pxay3TYgRWNIKKLiLBnI-CUy5itO2v6EdhrfbXh17Duhp95AUm9LXuxhSJDdnTSKHNSQ117j5V3LqkhrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVf-9x9JtdNQxtoBh-Rwvw260Cuh79ztNsvVuYMuHaek2AcJT3yw60pvu5qjgMA3vqQJWwFNRMcw8dpUsdDB97j4XGJAupmziiFBXnYT_XKejIYJJCGrUaJ6KrmDYcNd6jnVVSR10pSzkTejX5OI47TQOM2rqtWrdeFWhlhtbvzXZB5cdiO18oafNKtSPj6G9YdDcyFsm3xzx9rjQ3uHvaQX4EUTjt7c019ceSzFFdAwGq4BI4YG-vG6ZvbNzl8Rw-PHIItgXv9QtiANJ9hidlhRs2n0MaBAiT6Ebkd2bQyr_wSPXRZ-vQgLWwuQrJw_nKvn-bt-nQVCWC_i8wG3wA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇧🇷
همسر مارتینلی ستاره‌برزیلی‌آرسنال: رویایم قهرمانی آرسنال در UCL امسال با گل مارتینلی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXgj7TRhxCJaa7A-QqFsEZPHH40Rnzo4pHw3M3gynS9iGiJHCA9SAJz4AFPhbSdg6X8FxB5jM-n5zJ3sipfXd39lq3YSNAGFK0QjDGfUaqzojrrhXhUK7XZGv4lkCkAe8aVwP4f04UpH5qXNu1gqppfmdnaic06i22ZJkvAZctgPFwetlqt64BPWZKPopPK3-zu7AZXHFyTwkB9kG9r_RvBb3tKVPhHt3-82ajPY-n6Y8dJhz6uEgaZTUfZbV19WXSUCgoUKJKoM6SGP2LUEEgceoSaNv97KQYCkwnn-r-PJF0M-tjsAKPS1hPgRXaUV6VJZX_iKWv4N9SCypfq_ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfhTOMuzgrJ_IPj4pSJDM_-evC8UL4D-iWruOQF0wUItmRxbo492rVVInBio_z0cUbUTbXkVn7XAGl2GDpQJfjSVdX31dNcr15aEWZzFPTztX5_kfnHS7Ouj4D2jGMWhGOkNs55RUBh00SLGMS73IG4O_gEDAfmfwvMeHfQ8TT6F8l0fTvSIjvwq5JOHAKSBGE4wkHBjOEQJ-amwgOIg14Fbd6xA8OXdLGV4Q34XW6pzoWN_xtVtP8cxLssXSLOOT9e_NRK9VDgWRWSpLdcob6tuAUttZ3f1DBZpfA4GE1jaWJNP4MMnBaJjvgx_hJYmCimfZerYEnZ-XLRckVYWYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IidYt_HQ6THs2JfDGuWYCuYzNk9e9UTzKZSTvlLNTFPdOovDA2DTSn0RgWaQJkk5V49YoWDs4XTELOfgKMtLNkjmcGxkiCnI7zszUx1KczDcerMD7X7kwV3eqKnIdSDtWOaIe8k1qOZWHZRywNhyuRKqpUyGmMcncClO3Pld2BTWwBfnc_jOiUh32HscGQnxuJYz2OnmSyZrekTNvLh0PuZxIH2nWm5DmA0DqEVeQ2v1YqfbKJtPMYl8dBZO6Anv3cCYqjy2dP7HAmzDQtTdYM-u6ksPhv66XPW5RHSpNEFYTbus952SQ01vthsw7vk5n_GDAZaHah5TAksJQmH4DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6t-Y-gTPE3A7iXroIoF44b8fEwC5w-Q8nR-ptVRWUAmFWBq_zl7ys02JMTKmwNUv4g5A18KdtaHxySTt_SHOZwtsCKZHCmZabheXHSsHLtqojpWkUEGHnP_mKvmfjDhICUYxYdrXVk6cHp2W3wEaHwfM-PeY3TJ1PsJPwUlsxidCinYkq8poWNQLr4x1CZS5XCSz3P2IxEUhY15z5jC-tGgRLRQuqhNwzAgadk9m0dAmgGUvBpr9fRuSjZV3szYC1QYi5r_exMZ8tGq2F5ANNMRAOMftGavjzgNnaqA6p-DaNvOGeLyzLU2-oaMN5zMEMRVOOYjAivHqEKRN8LHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEK52OlSRiuFRUKqOeHZP7sKN_ar4z2gVzdyGlpGMTKdatXzj4rJnaHsoy2SKol7RDOvkz9tZvz9tZeo6F-t55v2zqH8CeGvrtmn_KuTIVtVv70FZFTChZxf_CEYu7H2C_j5E6UQh5XhqftpaRbUTyGI9UHyf5-YICXjEfmshk6xAHMZm1h9D0aGxRwHjjwDc6lqxAVjzy1tcWi7d_2v9Um12TsetdOfWSEj6rNcZ4Nhs9iOLgV1VOODoMuwf8UzsU-go3arg9vrwiJmwoVlfduH5Ws6VtdFRJ8FCYFm8X5ZbBOLEVLx0PbKpF6lWMv6c3KsMWyvGuEH0vqftjNYZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZ2pbq-AJOtxfA8Wyv5MyOojfMfhVFCpgVSuYPeusnFkQjmdiFM_Lkjbp-_cFhgT1l5ULRm7EKPWUsZBvbTRWuVatlHB9-HxGCvGmGr2ZXyLpkIsudiyRjpB-9cAidTvIwsM_J3zOwVUmj_6zRfbdmwxwvkSLkaZzZ9yKkqDnNm6at8ZGW7vEzfk8VYb6cIj7Bq2RItsvq6vQuDgyj0gI87FA-8-ozMYlULyIiJyyjBb4TNpx7mgx_XM5xohnT_GI4QEYhvl-ANq5_JgITHFidwF3cxWJJ-fl1Yxlm7jn4Z0td1KKOrqS8bIJw14vCkrbDPGg7tbXRWQlU51QQO1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tH-l4GeW6VG3b45R1ZCcPSpYa61dKd0O6hkuQeOjZjaQduq0QsThGSveSoVN0iADFGSBEc41ilZpobMb0t88qWnG3hsTbb_k6YQAzx6iyYmOSF7G-scqwmONW8YMoxt2pcdbwHyW4bgzEbeflhiJcvvhsJP0rymvFLS0v1SpFnzXBlfBWRALvMx5nrO-GUplHxZuwl-g0rrWjfLbrSwREslpQTBt3WToIW6w0j-2EoUWVwE8zfiVnzNMCk7EZh80tYL4nJtqAQjQ-qZrtsZ3i3i2Zkc-nDsNVFonnt5cdPjgO3TRxbNW6-MuRgWlniIwwPWl1q1kaO0_WXNJwrUSTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijVPHywZ6LocVXW_2TpZgMYVQASPMj54EaMX7TKAl47G2kMYFumKWQM4UTsKK4WZ9u4XH8hZsb0li8tfVimlSxzqSM5tlRKpECYVhpBJ-r5b5iExh0Xx37pIvl9R9qN9llJZCbHex_YCyc_fUK7enlzDRkAMl2_oijRfYJ4VGuw8oOHCeYxA_-Vzp_bA9x-8HE-bIns4GGgRo6aJNow6GL1KjqO0c_mVwVpgrrwxOImlZQA83x-fQ3YL7Q47AfYDg3G1QLm_4GJ-0uHVV-SaE0ISz4SxhqD3qGCv9t17-QdmdpXTqX6uIQ2b_kn4sPFHsKSJSPnF7lbBO3X5mOiF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEg5-l8V9qBldOMJzJl7petNwJYBpqSSb1LBI3j_JOSFYiLUdoqwFopksGU0UU0O5iMN_e2bYM7-Jvx33T25L0Pw4PURGus1IPvfIRhnEcXRkzyaSRLfcaDSB_yyxGBSqUIaY17Gl6PfJc4uf0jVF7uw2XSY11qyEDx0P_sRCpfGzfOWye0jDFd1vW3OivRHXy3JvISIlkjK-8gOHvi9G8SvqqH2Q-yHs6Bdn6r7guGnar6RQongp9dxcPGamJussrt5wITO1azB825O4kNXYlimyYfDbowf_QawrcXPyt-fOk0Vcm6y1E2qGa_rXsowTJ3Ht-JEGSePdXryfoGLqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lp3H5mMPi-vQUAbWHqT08Ss-t3dXyvVQqvfrlrEq769mChOQ0KGvHHreInB8VWNMe-o3ux8VpcVlFXX4QVq3RNUhWJ062PJodHhUx2R363KuU3yGP2gjVapm7Zd4HlhjUV1-gAyQKWpPdjmuW5ktr1qR6LJYt2jFCyyR-zBMm-mZS7qBWaMKIVrXhp7PmkcVh3g5s4SSYWOCp3C1tqks6NwSjs-VltAq7AyHAqFuIINdGdXreOHt1U5HROirsuI0ncC9W0HsUZVCJiKjwIAYM1kGuM_1qPRLUevxMb9-TknwMfGpGnQCtfst378uGgS2bzBbBm-Cm18rO9vayJXigQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ksveOhVFJFxRFoy8wVqDcPJ31H11rDUxBK_h_j6WcOBlAKe0vNeJTAvWxgtDLAFPyUJtx8TPB5Ee5aT_Qzy_ujJJlL92UMqbDqShMTovelsUuZqjq3OZ5IOBwKiHJ6vYSik5dfumz38VmOe6f_Gekh1y47hR9oRs6q0HMISO64TmyOS68d3bLVqIITO8xq9U9yAnnArWLt8p2YlLGhcRE2-Oof0aSP5fc5TGoC4ks8Ic1tv8JVPcXPMeoYjz9ypuTpNB7manDZzM6iEhbWSK-c32pXummMWPJCzuYUcTnL9XeNJTN7V23pLk-RfuMkd0cNXYulNgAkNwbYQFgqq1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXDMlY1iAabCwGaOuO5ZdwzteDg5GS8fi9cgyKouCG5e1O8nCffvgtoBdkBmuRBaVUNP0XG0sK5r0doltfUx-VlzRHytJH-94r4GZba3tXB7DD4v9e5Wc28wgk3T8s_x2PsTWD-rOtd1mj_6aVsGSHEy1t5t6w5mg-7pVaGv0uNOWrF7ssZJuD8SwINi-nYi-OADlyoysN0exsoVZ_zjkYY-JBqbqqQVcAdX_Licb3xLw5Lxeas5nfCOuoOyR1eG7yXYg5QwFmGQWyclL5NTd_OJmMXzYT0BIHqrG9Rqv_OfL6HzX8HMKzev717s7C5WLGX9bBsxFLLT6RWwj0vibA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=B_P014VV5lDkWuAk2OtDwVtq1lcvU24TPuGdhw9_SGOA-ttYgNRe2_gB21ZGP0X8kLzvS6s2VaiHY-qP1oxpIs4d69-TTGxzfwPbMlpil4h5DjhCB9OsVPVqsb95jjrROF2TNX_5QHvRaHZ4lfzuidwuaTNZLxFTGkUr9p1ynl6NIkN1E7Xkpp7YZpg_mzkov1n1Y1bgXFzkClIcN73mAx1SyeOgZzOSO06ybgNHxOSboPJdH5oNehB6vxlUTAJrBJfpU9h9_Z2Yr7pIXurdjcbrsGRqFTFp6ztDi4Y1bWbQsm6pnQVryR4Wy4euOaICk75gndqzbFyucQ0ZRnfM4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=B_P014VV5lDkWuAk2OtDwVtq1lcvU24TPuGdhw9_SGOA-ttYgNRe2_gB21ZGP0X8kLzvS6s2VaiHY-qP1oxpIs4d69-TTGxzfwPbMlpil4h5DjhCB9OsVPVqsb95jjrROF2TNX_5QHvRaHZ4lfzuidwuaTNZLxFTGkUr9p1ynl6NIkN1E7Xkpp7YZpg_mzkov1n1Y1bgXFzkClIcN73mAx1SyeOgZzOSO06ybgNHxOSboPJdH5oNehB6vxlUTAJrBJfpU9h9_Z2Yr7pIXurdjcbrsGRqFTFp6ztDi4Y1bWbQsm6pnQVryR4Wy4euOaICk75gndqzbFyucQ0ZRnfM4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJu6LEJev_ISx4pKUF0LbozdsTJI8K_PIsvWMz9pzf1dpjzbY7iN5z_1LddigELXbinht993d1xxyaPSs8miysHG-WO4OJRAndI2sSRP6RmUZg8Ca_L0xH60GFO43KpiG9eeNs5-vcxsenhAGdcuBIKA6dsSv9BGXGeH3TvDLIlEgE48DWXOXcckN_VrxKMSTC5sPC2_RWlxfiiMilPqy5p_QYC6D0D2pinzco30u9mAOLiBxvgYMqmWaZuoep8JfeVaNEV-StTTBc4zZN1zGJgvre_fYuYq6KHpjMlWKQWMh0Z5lYu1p-9QF7sz-LlUfnHLGFIn0oXSAr79EAwvvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKR1iwW1B5on1NSCJxCOs9ZyuT-MWDJ-8vyG52TvoMc8JmpFeuVpsotjOtuBXz93fBxI3wrvVYEjcfdy1oStBG0kv1iiU7qOphnt5oNK-rzrBgVx1dx16OmxmUk7OUEz2btGliOkQ1Crn41QHS_Gsu2H_aumLzqb5BjMI5kjakOZswGvAb6c5uQOeIf157gvm2mdxktxeF_W6P5kKT6Q_5uBKmV_kMTujRDNzuHKdd0WpTz7nvLFA7TiVvsX0I2k423hewuhyJSVsH8jag-NsW74QHDOIBXT_-5kyoSI5tcjCEE_K-tsyTGEu1E0kWR95vTJNyanc3CqYM4L2FahXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8p-6wlkBnXyhwZLPod-R1W6dCm9KJXycE_mdOCYOt8Z5PD3H7IW01R3XwCzrdZY6tv7F5fFXVNRQexJVslMaK_sMcgdxv357pwafwyhExkDGHMaTDBs4R-rhTNx59L2uG1jZwcVJUNf-X70vHhyRuCeXqItkc4JxHyxVAmz-I67AWLoClraI21PCqTrJ3S9U6hPTONhIwLdPh06V9bFrvTnwgcJpbBW14DlyNVm8XZ1qtGqzguBH5P_B6r6LYWvO75UmtJC_s8jHBrYsSqsATtD9VCMJuelf1Fd_wMJgFmVkcL5nXy7HEI-AsammAZQs8Z7_Y7gRO_OYQPOEQHZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
