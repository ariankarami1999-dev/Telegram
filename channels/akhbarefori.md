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
<img src="https://cdn4.telesco.pe/file/F64n2Ox_ZfqP2x1r_7p9hd8wQjQYsxt7wwfqWgfEKEW5LQ_9bOc9J_WSfkKEtALS1bVcw-FZiJ1OzDmxPUc_4tW9AkXnfBKvVP7t5a1-r0BGlxDicnhVelQ995_EnBdtJboAc8LvJ5IssDxtUdC7ZKMscsWht0h1XWMUuiUCIaPG2PwliKYJrRURSiA7tjn5vUTo_96iMrzWz02dEmsJIBRLL_J8ddYIYaVpjJ1R3-Arhkr4wiwb9dfJaHsitLucyWhvdDuVWY8NXr3EYhoXr9FIeKG6X0hB78Td-29VUw-Y3v9usvgOBdYwUUP352teABDs1ksUTbyq-WFLYi0myg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.44M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 19:42:19</div>
<hr>

<div class="tg-post" id="msg-661497">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ادعای سنتکام: تردد کشتی‌ها در تنگه هرمز امروز افزایش یافته است
🔹
ترافیک کشتی‌ها در تنگه هرمز امروز افزایش یافت، زیرا ما همچنان به حمایت از آزادی دریانوردی ادامه می‌دهیم.
🔹
۵۵ کشتی حامل بیش از ۱۷ میلیون بشکه نفت از تنگه هرمز به سوی بازارهای جهانی عبور کردند.…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/akhbarefori/661497" target="_blank">📅 19:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661496">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e355b9bc7a.mp4?token=XBDeQIFjJNTn_qP8bTDR1ctl6uQc5IZkFEvRB6FvipuIRKvFzgRlBg2cOyQY4_Le49q-jbaMC5Owbxrve1DE1NnuaDWxN-tpPJ-RSnUYM4iDru6usXCSlCYuNB9wUca5zLtKc1iFzCmU7orlAROB-PKvs33mOCFdtWezAsenQsjMwrBvV5xCV-75UYbPnsdsDD1GglnVvacW2bSgStl6m79ec8NmIhX3ezP5EuDj3NTEKGY0fEx_iwM7iikzdDe3sc-yq_dQ6LZTO8ERAftundi-oqQYunJ8TAtL65JJ7tzF2eP3RUoGOCT6_QPw1oBNNlZu1OPvlR00lVDiQ_e0IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e355b9bc7a.mp4?token=XBDeQIFjJNTn_qP8bTDR1ctl6uQc5IZkFEvRB6FvipuIRKvFzgRlBg2cOyQY4_Le49q-jbaMC5Owbxrve1DE1NnuaDWxN-tpPJ-RSnUYM4iDru6usXCSlCYuNB9wUca5zLtKc1iFzCmU7orlAROB-PKvs33mOCFdtWezAsenQsjMwrBvV5xCV-75UYbPnsdsDD1GglnVvacW2bSgStl6m79ec8NmIhX3ezP5EuDj3NTEKGY0fEx_iwM7iikzdDe3sc-yq_dQ6LZTO8ERAftundi-oqQYunJ8TAtL65JJ7tzF2eP3RUoGOCT6_QPw1oBNNlZu1OPvlR00lVDiQ_e0IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حدود ۱۵ سال پیش بازی‌های موبایل به این شکل بودند
#نوستالژی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/661496" target="_blank">📅 19:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661495">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5cm7OGR1hKKtEmc-PjRRS4rtSYnphWqqdKZFWj2k5yRBgg8ZsB-Khw3xQ7wVoOMLxsbJCD8KXtVNsgCNcZswpsxKZ9vVE0w7_EbMT0qUNmyhhTOCxGp9FKG1siEw2lpCGz5F3aoZy4EV63ixK9eoqYNOMvWf-DGrcfSwxY0zsoa_RI4m9R49cChuZZsL6xVkUCr-3MiJQdIdYYckAcl8lV7ZblLFj3YOavwhg4TzlbUJbU7sXIJu7npfDNECuD6fwLKQIRzxmUYtGDO4Ap9VRqgMNjwVxzGK8zFyhsARmjPSXM2C09iiFLk2y7PHCBKRE4Fa4v340U5MW2kU1etEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/661495" target="_blank">📅 19:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661494">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81e10405c7.mp4?token=T0fA8ietYOVyptWct3nlS4VQYfk5EIThyPsC-pggzmeCnhgVV09UoHP_1HXuxoDbsSjh0586kITdkuxIYiSHlBEBnxSIzW35nHWV3t0sV_El9P6PsyhgnxODVWU37sR595sj9zQIBoRp9EnC0dvrRDlqVRFNU1BxSeu6-x_TsuriLIoXTmVxD3k8Oxn4FHBwy8aWj1ybu0AbNDdWL1hp7kE-Afy-ZLhZP7jPp5K6kbluOFcBf_-0E6ZOYl7QY8p6uLvxvsf2oN6nVsSUiRung1q_RqyiXaTheTSiwLhUVALv4CKQogd4UJc3Ye85BbhQPtdq8e2lCM_ZB5JeWFAivQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81e10405c7.mp4?token=T0fA8ietYOVyptWct3nlS4VQYfk5EIThyPsC-pggzmeCnhgVV09UoHP_1HXuxoDbsSjh0586kITdkuxIYiSHlBEBnxSIzW35nHWV3t0sV_El9P6PsyhgnxODVWU37sR595sj9zQIBoRp9EnC0dvrRDlqVRFNU1BxSeu6-x_TsuriLIoXTmVxD3k8Oxn4FHBwy8aWj1ybu0AbNDdWL1hp7kE-Afy-ZLhZP7jPp5K6kbluOFcBf_-0E6ZOYl7QY8p6uLvxvsf2oN6nVsSUiRung1q_RqyiXaTheTSiwLhUVALv4CKQogd4UJc3Ye85BbhQPtdq8e2lCM_ZB5JeWFAivQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما: بمباران در اطراف شهر نبطیه همچنان ادامه داد
🔹
رژیم صهیونسیتی در تلاش است ارتفاعات اطراف این شهر را تصرف کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/akhbarefori/661494" target="_blank">📅 19:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661493">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRocslNlumfLtrNBeJXjwqdqS6OOj5WPkAM7G10yqFNKC3N5oqyeGc9drZT9kbI1jlZZGiPCa_ZPVu1KcRrHLoLSXAna6KCiNYXh0Ec4vrRHHnd8XjvQAv6gIwDaigsDtZJcFYMgS24tBOhpgEbtE9uTK8-FIMXiFRkFHoDf7CheljXKbwmXek6gYKcqJk2Ka7acoLA4ONEEwF--EsrdypfQ8khcvVsYBrJSoiI5S1NGqokHnZbrD0Ws2CYqCn1sHYHbrIhtpzMq1FZ0BXkwBCFGH3w9VbVndURF4oGi2ytItInM8AaAzPj1lTvfxG14F2nU5Lrf0JpeBuNWUV1ruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: وقتی توافق روی کاغذ بماند، جریان انرژی خاورمیانه هم متوقف می‌ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/akhbarefori/661493" target="_blank">📅 19:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661492">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6Ldhgza2cE5lsPOkLcrQ0dZ2U5WJLqgczCTDcNpokILJH0WIr8lwOEA_pVEY8-DCQ4Oci6DMK7KV8cBOTMt58tPUOxGimm357Jgq2TywTPqJ19qXI1Y8UmknAPS4hPj2onAMsKCIYIHz2L-z1Ee4HznpJBo7Pykelzturm8e--7rqGIQzQmzLuxvCvOeQuAxoi37dinG_vmFx88Ff2ffKxHOY5Mg9oUwe25_LCRH_6bLMIA3xY_yoN8PIbjB4dbGbNjlw35QbyCMrDoNc6htF544sKoDgKzG8jGiGcdSRGuACFB1zSVsmhGF4DhNaGbzt-kdOe--7ac6fVoJgWciQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار الجزیره در تهران: تاکنون، خط اعتباری که به تهران اجازه دسترسی به دارایی‌های مسدود شده‌اش را می‌دهد، فعال نشده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/661492" target="_blank">📅 19:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661491">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65eed99daa.mp4?token=tvr-Tz9J5ka5ZTWiRHoKG7C-Rn8uBPt9Ys92-c9d5OTnrE-8y_6GBwW1RWKSuQ-X-liuaWwU8x1KcTPaEnGVfSmrwxLPzTnTmpP4gQDXdq6nRalLK5kwIOdOE_Fz184zM9qetX2sAl-vselEn9wA6Kqq_3Ssz05ndS1CyM15GbOwynsKbT50_e6zkngaQgpoqAEQIb6UvoxuLBDX7OaqB6fqm1IBfq8zpEQ-0rVFw_omlFQ7ZJrPaJDCiumW-Hz1HSA8RnQsbIlgQed9N2U0kXmYm_NMLuy6FWeGtnOb2x1MjlwJ0SBhrxpa9BWJ5fpZWuSqKs3P63ETGd5rsGhKXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65eed99daa.mp4?token=tvr-Tz9J5ka5ZTWiRHoKG7C-Rn8uBPt9Ys92-c9d5OTnrE-8y_6GBwW1RWKSuQ-X-liuaWwU8x1KcTPaEnGVfSmrwxLPzTnTmpP4gQDXdq6nRalLK5kwIOdOE_Fz184zM9qetX2sAl-vselEn9wA6Kqq_3Ssz05ndS1CyM15GbOwynsKbT50_e6zkngaQgpoqAEQIb6UvoxuLBDX7OaqB6fqm1IBfq8zpEQ-0rVFw_omlFQ7ZJrPaJDCiumW-Hz1HSA8RnQsbIlgQed9N2U0kXmYm_NMLuy6FWeGtnOb2x1MjlwJ0SBhrxpa9BWJ5fpZWuSqKs3P63ETGd5rsGhKXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردی اهل ایالات متحده یک Wall-E لِگوییِ واقعی و کارآمد ساخته است
🔹
این ربات می‌تواند حرکت کند، چشم‌هایش را تکان دهد، به کنترل‌های دسته‌ پلی‌استیشن ۴ واکنش نشان دهد و صداهای انیمیشن را پخش کند.
🔹
درون آن موتور، سنسور، بلوتوث و چراغ‌های ال‌ای‌دی کار گذاشته شده. او همچنین دستگاهی اضافه کرده که قادر به ایجاد تخلیه‌ الکتریکی و شعله‌ور کردن اشیای کوچک است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/akhbarefori/661491" target="_blank">📅 19:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661490">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlPkqcUUeZLpUXri1pFA9PlXHGGjZ7WP371zW9Bv0luQWFF3BE4jO4LeXp2BkzgH6yWpsS8ndPsxTcDUIi6WvenFm6VK6slp8ziQ73RfW79E9Awlph_iUhvSt0BNyFS_Cpj2wDs1AYymajcrVvX4kR5_9Wx3-NT-92rl5ibAXzKFqNbWcoP1RV9ao4Z4kxHTZFD0uPKgLrHb6L6CyIAW5S_MpA9j-ZIFB92-za5Sry8syq_M6lIuKlK2qbtI0CCy0JYsjeh0utm1tejr_05qlT7mcMUY8kjCanjKhdizkiv0RD_UeQZ5GnGua7O-2nfpnUJX8lBd-s0UlKXpU249DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کلیدهای میانبر در Word را بشناسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/akhbarefori/661490" target="_blank">📅 19:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661489">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFXojKgCtZNPpPg80tyyKw_ARefCQikYM6q44zv5d-OXySIz2Z4lS65LUb_MUxrIXN2ToHGOVqLxqNRdRVSTZnQWtPsCnd-C3SVZjtZ-tkMKErgfKn2mCibbQE4gM2KBOOopBknF8elnpsyCHuOyxCvnMuY86OUIUUju4mCbavv12B4ppuXJgNHPPjhqT5vrH1ZVp4LW7BWVbWwZS76aHWoeSlzXXegEojtGC3WaZuGJYgMcXWyp33aQfxJBDsZwlJg0vRghnwfgoI5mrhIkR9xVMS-98Pl9EWB_4p6nzQiPASWFNVglBN7AHg0-PJ9qjqFe2F72lkQ4zDC8yLBZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
«سقای شهر»؛ پیوند خدمات بانکی با خدمت‌رسانی به زائران اربعین
🟢
بانک شهر همزمان با آغاز ماه محرم از اجرای طرحی با عنوان «سقای شهر» خبر داد؛ طرحی با محوریت مسئولیت اجتماعی که با هدف حمایت از زائران اربعین حسینی و تأمین آب آشامیدنی برای عزاداران در مسیر پیاده‌روی اربعین اجرا می‌شود.
🟢
بر اساس این طرح که از ابتدای ماه محرم تا روز اربعین ادامه خواهد داشت، مشارکت‌کنندگان با افتتاح حساب ویژه «سقای شهر» و یا نگهداری موجودی در حساب خود، امتیاز دریافت می‌کنند. این امتیازها در نهایت به بطری‌های آب آشامیدنی تبدیل شده و توسط موکب بانک شهر در مسیر پیاده‌روی اربعین میان زائران توزیع خواهد شد.
مشروح خبر را
اینجا
بخوانید.</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/akhbarefori/661489" target="_blank">📅 19:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661488">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyIO1iJeANLJFkCtBS4TG3-9IO-MDIBH7Fb9C_UoTtIHbM3akzDjbzBBPiN8pK1pNOOHCuncnWjGlaR8vON9HCGfidw6toQ5NsHJGB30X6reNHnTAgOM56LtC3kpKuBkUAU9tVd_9Lg8ogN8hBjRoDtDf89Rh_wamnrkZkOAYHMpnEj27XHDg8PTeFJgEl9LAHBrDAZTl7Yf0WVywvUZLMBt8t7vS7MRM16QhFIQMhQA2esRhSiJJU6ncx_prfXtJ7siROvleZoGzAJu-ec64ww9nZTudp9Y1uoeiVkaoBpoxulm-H1aALZCuKpn7QMjojJQgGWjUc725BiyI_yGVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران‌خودرو: دوباره گران می‌کنیم
🔹
ایران‌خودرو که ۲۷ خرداد قیمت ۲۵ محصول خود را افزایش داده بود، پس از اعلام وزارت صمت مبنی بر لزوم اصلاح قیمت‌ها، قیمت ۳ محصول را برای مرحلۀ سیزدهم فروش کاهش داد.
🔹
با این حال، این شرکت امروز اعلام کرد این اصلاح فقط مربوط به همان مرحلۀ فروش بوده و پس از پایان آن، قیمت‌های افزایش‌یافته در ۲۷ خرداد همچنان معتبر و قابل اجرا خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/661488" target="_blank">📅 19:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661487">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7H366pqXg7iFEWd4kYqtn0DPuC9G6Dni1SjK-4P7IIJZRoRD4hvqpfdN9U61wUMW3NnlWwcUyuE8MWT4R9YHMW32kH5UgU6dzISxlV3f4Gt4QzvghobBhq1KRZ7jmnS1OlbpcXfvFvE2ALX_M5s3uzUIWGQewmR3XrEOpqmxS2ilPv67ebZ0lJqVtA2QCBea5DSIQvdQeAeFe9zuoj2uasOL7bfBZh1_LHb8FjcS3Mc6nWsbd6VyPrlk3mLF1WRH9jKAJADFVEFHU627xgG63oA7eTpomXXDdK6ma-jaao6Mhzl0D4dQ4ksLBn5lTyQC0WhvfR_gtHthMNF8XOCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/661487" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661486">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ادعای سنتکام: تردد کشتی‌ها در تنگه هرمز امروز افزایش یافته است
🔹
ترافیک کشتی‌ها در تنگه هرمز امروز افزایش یافت، زیرا ما همچنان به حمایت از آزادی دریانوردی ادامه می‌دهیم.
🔹
۵۵ کشتی حامل بیش از ۱۷ میلیون بشکه نفت از تنگه هرمز به سوی بازارهای جهانی عبور کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/661486" target="_blank">📅 19:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661485">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
نتانیاهو دستور توقف تجاوزات نظامی در لبنان را صادر کرد
🔹
نخست‌وزیر و وزیر جنگ رژیم صهیونیستی دستور توقف عملیات نظامی در لبنان را صادر کردند اما بر تداوم تجاوز نظامی در مناطق تحت اشغال تأکید ورزیدند #Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/661485" target="_blank">📅 18:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661484">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
مهم‌ترین حواشی و اتفاقات جنجالی ۴۸ ساعت گذشته جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/661484" target="_blank">📅 18:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661483">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
نشست سران قوا به میزبانی پزشکیان برگزار شد
🔹
نشست سران قوا به میزبانی رئیس‌جمهور و با حضور دکتر محمدباقر قالیباف رئیس مجلس شورای اسلامی و حجت‌الاسلام والمسلمین غلامحسین محسنی اژه‌ای رئیس قوه قضاییه برگزار شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/661483" target="_blank">📅 18:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661482">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d26a976aaf.mp4?token=NDvPxDemwyNuWf5d4Z44ua2mQFFXJ2zvMVmjsp7S9MOs9m2vtHO1YE05KrtU-OWQbb7lA3Jtj5jrtiRkJij_HXgYRwdaxFtErRfqsVi3ZRXHK6MJxLN_aiwqcWbVIeufc44QnFjcJRtWFgZ9Gj5TS7BOrlXUtRqZw8vhDCZeiO-LbZFZRfShHIlpy6aJqP97bsECNk1vI8RV4l7eWmWGrwlvB17BTrjEpElD_MMEs0-7ZKhqBjTq-R8tnc3rwfR0B3mzHiKhz7xsRv-z9WHbe-2JDTJuwBwFd4Kzzg0ivYoWB_pqFwMzykByvh-CQVCZxdmoK3IHVr6mFcrabpbX7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d26a976aaf.mp4?token=NDvPxDemwyNuWf5d4Z44ua2mQFFXJ2zvMVmjsp7S9MOs9m2vtHO1YE05KrtU-OWQbb7lA3Jtj5jrtiRkJij_HXgYRwdaxFtErRfqsVi3ZRXHK6MJxLN_aiwqcWbVIeufc44QnFjcJRtWFgZ9Gj5TS7BOrlXUtRqZw8vhDCZeiO-LbZFZRfShHIlpy6aJqP97bsECNk1vI8RV4l7eWmWGrwlvB17BTrjEpElD_MMEs0-7ZKhqBjTq-R8tnc3rwfR0B3mzHiKhz7xsRv-z9WHbe-2JDTJuwBwFd4Kzzg0ivYoWB_pqFwMzykByvh-CQVCZxdmoK3IHVr6mFcrabpbX7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویداد داستان جنگ در برج آزادی برگزار شد
🔹
دورهمی صمیمی اهالی رسانه و کسب و کار با نگاهی به آمار رسانه‌ها در جنگ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/661482" target="_blank">📅 18:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661481">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
اعتراف رسانه‌های صهیونیستی: اسرائیل باز هم تسلیم شروط ایران شد
🔹
تحلیلگران نظامی و رسانه‌های رژیم صهیونیستی با انتقاد از عملکرد رهبران سیاسی خود، اذعان کردند که ارتش این رژیم بار دیگر تحت فشار ایران به حاشیه رانده شده و مجبور به پذیرش شروط تهران شده است.
🔹
تحلیلگر نظامی سایت «والا» با تأکید بر تغییر موازنه قوا اعتراف کرد که ارتش رژیم صهیونیستی به دلیل فشارهای ایران محدود شده و این یک معادله جدید در منطقه است
🔹
رسانه‌های عبری گزارش دادند که رهبران سیاسی رژیم صهیونیستی بار دیگر ناچار شده‌اند در برابر خواسته‌ها و شروط ایران کوتاه بیایند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/661481" target="_blank">📅 18:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661480">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbWCq3Dz7MuNZua5f0kJXs5zPuMYEdqHRrQbrovHyhsxZYVOhcqHl2m6NzfOtIRqYnAEEXuqTbkIgcQcQLNYD9QxqEHAetGLsCTYJCKpTbnTRgjsDdATOvP1v9XCHw9aRbVkGzMciBTbKprccQGxAB5xcQSeEuExhh0qkAu1BzDlaLJjHj-CbEy7ILykJm-6RWK5pCV_OtNUPhiLHZFcDHHm8P9ce_Vxn_7riV13T3LTbpcpKn1VUHardizQoDDdV0qlA6IomysQxclMlkL581ea52HZg7AVkvnoq5NoYRCQ0h-vfIZ90rr0uN6DkvbAmODaj0aNtfTR6ep5I0QpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حاج حسین آقا ملک؛ پاسدارِ ابدیِ شناسنامه فرهنگی ایران
🔹
حاج حسین آقا ملک؛ بزرگ‌ترین واقف تاریخ معاصر ایران و نبض تپنده‌ فرهنگ ملّی. او با وقفِ نفیس‌ترین کتابخانه و موزه در قلب تهران، ثروت افسانه‌ای‌اش را به دانایی پیوند زد. مردی که فراتر از زمان زیست و با…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661480" target="_blank">📅 18:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661479">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
هشدار جدی مقام ارشد ایرانی به آمریکا؛ مهلت زمانی برای توافق محدود است
🔹
یک منبع عالی‌رتبه امنیتی و سیاسی ایران در گفت‌وگو با شبکه المیادین اعلام کرد که میدان نبرد و دیپلماسی در هماهنگی کامل با یکدیگر پیش می‌روند.
🔹
واشنگتن به تعهدات خود در قبال لبنان پایبند نبوده و این خلف وعده از نظر تهران کاملاً غیرقابل قبول است
🔹
جمهوری اسلامی ایران هرگز دوستان خود در لبنان را تنها نمی‌گذارد و از حمایت آن‌ها دست برنمی‌دارد
🔹
ایران نسبت به محدود بودن فرصت‌های موجود برای پیشبرد تفاهمات هشدار داد و تأکید کرد که زمان برای طرف مقابل بسیار محدود است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661479" target="_blank">📅 18:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661478">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb9b554cbc.mp4?token=h8UhyfE_iOcRwdomTVTfxwd6t-1qqpfWyWnluSQeht1v4LPwwqLstiiihoZQO4MI8esV5X7oG7RHrKueD2XyHwcofBvQskQWsL1H8piJQy57kc5yLP4bOsQCMDZhGBBwBwnU1dNn4dKSh8QPgoP-f_oKyst__lA4fLX__82WDilsJ_oJvrU7lSNsU1rCnabiXukwkgOVRPzWoWynH59Yzxr7kLBjACNMeRHoXigs0Mt_Z9jr0_03yqiJ_UGg5Kz8M_Ktj-5mpeyukm5QuWFPMfiHAak1B9gThk62Dv1hZnpXDeapdl2Ww3Shksr0bIQp-YL9tP_dH0RRkKDZxaSh0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb9b554cbc.mp4?token=h8UhyfE_iOcRwdomTVTfxwd6t-1qqpfWyWnluSQeht1v4LPwwqLstiiihoZQO4MI8esV5X7oG7RHrKueD2XyHwcofBvQskQWsL1H8piJQy57kc5yLP4bOsQCMDZhGBBwBwnU1dNn4dKSh8QPgoP-f_oKyst__lA4fLX__82WDilsJ_oJvrU7lSNsU1rCnabiXukwkgOVRPzWoWynH59Yzxr7kLBjACNMeRHoXigs0Mt_Z9jr0_03yqiJ_UGg5Kz8M_Ktj-5mpeyukm5QuWFPMfiHAak1B9gThk62Dv1hZnpXDeapdl2Ww3Shksr0bIQp-YL9tP_dH0RRkKDZxaSh0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت تنگه هرمز پس از بسته شدن مجدد آن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661478" target="_blank">📅 18:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661477">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
تعویق یک هفته‌ای امتحانات دانشگاه تهران
🔹
تمامی امتحانات پایانی نیمسال جاری دانشجویان دانشگاه تهران با یک هفته تأخیر و از شنبه ۲۰ تیر، در همان ساعت، روز و محل تعیین‌شده قبلی برگزار خواهند شد.
🔹
آزمون‌های برنامه‌ریزی‌شده برای روز ۱۱ تیرماه، به تاریخ ۵ مردادماه ۱۴۰۵ منتقل شد. امتحانات دانشجویان مقطع کارشناسی در تمامی واحدهای دانشگاه تهران به صورت مجازی برگزار خواهد شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661477" target="_blank">📅 18:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661476">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ممانعت رژیم بحرین از عزاداری حسینی
🔹
همزمان با ایام سوگواری حضرت اباعبدالله الحسین(ع)، منابع بحرینی از ممانعت رژیم بحرین از برگزاری مراسم عزاداری حسینی خبر دادند.
🔹
برخی رسانه‌ها نیز گزارش دادند که عزاداری حسینی برای چهارمین روز متوالی ممنوع شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/661476" target="_blank">📅 18:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661475">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rF7ntaKtKpKEmn31JXFaY_yzY30oK5atE3JFyPCyAwyIOe3UcMhde8mblaUxdLEXLU4NScbnLifLNrV8qikNqpIXmNE0ukwI4rZU8NmRaGmod0is4U-U0wXZHVxzZ0M_CYPb1LzKzBO5pknot5qc6OgDv5HoFiDk_VduXozIkeM2eG2qU4gdSNrhBbUBxLQKJz1PYIKb8V6E8f1V9v2NUEayg_rFQkJxhf75_MQ7MI2g47FPiJXelAig_KzU6DaHeSFZcwkgL3CwoKKDDakFKRiLNqT8aNru3IT6e91kvqBA4Bl8UYNvPjfESSNKxGzYYyrbzj_rQoTDhxRhVRKAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین خبر از وضعیت میرحسین موسوی و زهرا رهنورد
🔹
میرحسین موسوی و خانم رهنورد، از بیمارستان مرخص و به خانه‌ای که ماموران امنیتی تعیین کرده‌اند منتقل شده‌اند.
🔹
وضعیت حصر کماکان پابرجاست.
🔹
طبق خبرهای رسیده، روند درمان میرحسین موسوی همچنان ادامه دارد./جماران…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661475" target="_blank">📅 18:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661472">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
آکسیوس: ویتکاف عازم سوئیس است؛ کوشنر هم‌اکنون در سوئیس است
🔹
انتظار می‌رود دور نخست مذاکرات آمریکا با ایران در آنجا برگزار شود.
🔹
هنوز مشخص نیست زمان جدیدی برای مذاکرات تعیین شده یا نه.
🔹
معلوم نیست ونس هم به سوئیس سفر کند یا نه.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/661472" target="_blank">📅 18:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661471">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
نتانیاهو دستور توقف تجاوزات نظامی در لبنان را صادر کرد
🔹
نخست‌وزیر و وزیر جنگ رژیم صهیونیستی دستور توقف عملیات نظامی در لبنان را صادر کردند اما بر تداوم تجاوز نظامی در مناطق تحت اشغال تأکید ورزیدند
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661471" target="_blank">📅 18:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661470">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
هیات مذاکره کننده ایران تا دقایقی دیگر عازم سوئیس می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661470" target="_blank">📅 18:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661469">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e56de999.mp4?token=GA4EZlfa1uqOxOhZU-Qzw7HXCdMaEPvktvBTSaD8rF-3rL2zcJ7ALfjhsRfygZcttgxNNQx6lJ2Sf9jWKQRwTGzwUfhgmuWHQKaQQYFGM5dyWMhDg1wFQMms9l486EnLOYV6QJ0OBaitMmN4McXt9ZFXQKMOIu35nhQyEJsHqStpkC-n2TJqTinJVh2T4I71_oGqiW1tSRpTOkg-onPJdYVDcQhVQ1p023oSS6hJKZSQcpuZNZG2nf3RyRm9pgNgfDwgsiX8HjrZ14Jk3s0DT9TkB7AfwJLrhCKAZq0QbaGDOG8SE7oFKJOa0V7T_rpQx4GscCmg1OL1AMq0xfQjMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e56de999.mp4?token=GA4EZlfa1uqOxOhZU-Qzw7HXCdMaEPvktvBTSaD8rF-3rL2zcJ7ALfjhsRfygZcttgxNNQx6lJ2Sf9jWKQRwTGzwUfhgmuWHQKaQQYFGM5dyWMhDg1wFQMms9l486EnLOYV6QJ0OBaitMmN4McXt9ZFXQKMOIu35nhQyEJsHqStpkC-n2TJqTinJVh2T4I71_oGqiW1tSRpTOkg-onPJdYVDcQhVQ1p023oSS6hJKZSQcpuZNZG2nf3RyRm9pgNgfDwgsiX8HjrZ14Jk3s0DT9TkB7AfwJLrhCKAZq0QbaGDOG8SE7oFKJOa0V7T_rpQx4GscCmg1OL1AMq0xfQjMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتفاقی عجیب جاخالی دادن کامیون سوخت روسی از پهپاد اوکراینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661469" target="_blank">📅 18:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661468">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMG8Gy_iXwNB6xmUCWCMIB-kJcmzYDnnYRWWzgBMF1zwDXQsURIirGYLDsLE3muolcxb5vC2A2IFKsvoTFpMcYOtvIvHHglwwblq4OeyvEI6xB0318BNZSkp_6fREdSevp783Kq2xXPk9aVcLYIXumMK4VStf13pIxEdG8ltcCzJbGk7CTPBuEXq5nAVIk2Mud-vhxRwkn47V6ON91J0EDVsSBw_u2Xya-FuSkymq3BMOe4lIO_-927e4pUS1uyPD0_onGA2FE3ZhbV3uj-nn_SAb3Fi2S_jFWVSu3pIa3105P5xIJCad-Tn3VC9CI0Y7SLr2sjxqcMYrNv2F6Mxog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج بی‌سابقه حذف حساب‌های اینستاگرام؛ باگ یا سیاست امنیتی جدید متا؟
متأسفانه در روز‌ها و هفته‌های اخیر، گزارش‌های متعددی از غیرفعال شدن و از دسترس خارج شدن حساب‌های اینستاگرام  در نقاط مختلف جهان منتشر شده است؛ موضوعی که صرفاً به کاربران ایرانی محدود نمی‌شود و بسیاری از کاربران در کشورهای مختلف نیز با آن مواجه شده‌اند.
امید مهربان، پژوهشگر حوزه هک و امنیت، در گفت‌وگو با ما می‌گوید: «از زمانی که متا سیاست‌های خود را در زمینه مقابله با حساب‌های جعلی، مجهول‌الهویه، ربات‌گونه و شبکه‌های فعالیت غیرواقعی تشدید کرده، حساسیت سیستم‌های نظارتی این شرکت نیز افزایش یافته است. این روند را پیش‌تر در جریان پاکسازی گسترده حساب‌های غیرواقعی و کاهش میلیون‌ها دنبال‌کننده از صفحات برخی چهره‌های شناخته‌شده مشاهده کردیم.»
به گفته وی، در بسیاری از موارد زمانی که یک حساب به‌عنوان حساب جعلی یا مشکوک شناسایی و غیرفعال می‌شود، ایجاد حساب‌های جدید با مشخصات مشابه می‌تواند ریسک شناسایی مجدد را افزایش دهد. استفاده از نام کاربری مشابه، اطلاعات هویتی یکسان، تصاویر پروفایل تکراری یا الگوهای رفتاری مشابه، ممکن است باعث شود سیستم‌های امنیتی ارتباط میان حساب‌ها را تشخیص دهند و محدودیت‌های بیشتری اعمال شود.
مهربان معتقد است: «بسیاری از کاربران پس از غیرفعال شدن حساب خود، از روی نگرانی و استرس اقدام به ساخت چندین حساب جدید می‌کنند؛ در حالی که این تصمیم در برخی موارد نه‌تنها کمکی به حل مشکل نمی‌کند، بلکه می‌تواند روند بررسی و بازگردانی حساب اصلی را پیچیده‌تر و زمان‌برتر کند.»
او تأکید می‌کند که بهترین راهکار، بررسی دقیق علت غیرفعال شدن حساب و پیگیری اصولی موضوع از مسیرهای رسمی است؛ زیرا تلاش برای دور زدن محدودیت‌ها یا ایجاد حساب‌های متعدد، ممکن است دامنه مشکل را گسترش دهد و ریسک از دست رفتن حساب‌های بیشتری را افزایش دهد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661468" target="_blank">📅 18:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661467">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ابلاغ دستورالعمل فروش ارز اربعین؛ سهم هر زائر ۲۰۰ هزار دینار
🔹
بانک مرکزی دستورالعمل تأمین و فروش ارز زیارتی اربعین سال ۱۴۰۵ را ابلاغ کرد که بر اساس آن هر متقاضی بالای پنج سال می‌تواند تا سقف ۲۰۰ هزار دینار عراق دریافت کند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661467" target="_blank">📅 17:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661466">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سفر ترامپ به کمپ دیوید در شرایط توقف مذاکرات با ایران
🔹
در شرایطی که مذاکرات بین تهران و واشنگتن تحت تاثیر تهاجم رژیم صهیونیستی به بیروت متوقف شده است، رئیس جمهوری آمریکا آخر این هفته عازم اقامتگاه کمپ دیوید می‌شود.
🔹
دومین حضور او در این مجموعه در شرایطی انجام می‌شود که ترامپ در تلاش برای دستیابی به توافقی نهایی جهت پایان دادن به جنگ علیه ایران است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661466" target="_blank">📅 17:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661465">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbHzUdSYnbA4DRv-P_bgIlZRT6hB7zKW5ODSZslqPi2LekroOQrmUpQFqQdHGmxr-yEhkOd-_0uMzVIdBa0GU3Lwpcf37tH_kjGj0_2h_-GxNRnezVkT_o2utIIVCgRKOKFxwg9NkDu5LuarQcL3-xBacYuChStionTY2X5ufd16UKZvP4_pX9B7rKXmT_P3sDAMZ0ENc4StelcIJE47XI7z9RAPR39_L8VZPpxqj3md7v6nc1joXcwxiVpqZc8jA3gGLAfvYHJaVV488oIkpLQouXvg8qlnZLvn1uHd6x9MEIMGywEvIEbXi5ay78j4StTI1mRsmdTtLwUgaqk4cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام گروه خونی در جهان رایج‌تر است؟
🔹
O+ رایج‌ترین گروه خونی جهان است، اما در اروپا A+ بیشترین سهم را دارد.
🔹
O- می‌تواند به همه خون بدهد، در حالی که AB+ تقریباً از همه دریافت می‌کند.
🔹
توزیع گروه‌های خونی در جهان یکنواخت نیست و هر منطقه الگوی خاص خودش را دارد.
@amarfact</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661465" target="_blank">📅 17:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661464">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
خبرگزاری رویترز به نقل از وزارت امور خارجه سوئیس: ما همچنان یک محیط محرمانه و قابل اعتماد را برای تسهیل گفت‌وگوها فراهم می‌کنیم
🔹
دیپلمات‌های کشورهای مختلف که هم‌اکنون در این روند حضور دارند، به تلاش‌های خود برای برقراری گفت‌وگو ادامه می‌دهند.
🔹
به دلایل…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/661464" target="_blank">📅 17:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661463">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIP9d58TzwDeKv-PW1Q3ERuKf2eLvH0m9HVF0aMjAZSsqVqTSOB33LPcy2u8j5OqHIa1mi_KAZfionL2vhAnWuksob63bXoFXNpkK-o8OUT8dqowtY6PKk2wdHrocfWLGVUeBoff9xENcUPHV26eRaRUWmZp-69iKkYeEdFrPamWU52bBX6PTd_HH_DXquXOIX1P4Y3EnBEXM2ml7RE4ISpWxCjpdUJ7DutGRbxa9qCZHPOoyTWgrGbjNtbUxdsIeCroTApCE_l7jyXh5V4S-8IX3CAvJxyaJrelW27FDUa-0tvOTx-05uPpGGbD5JLJOgl5fwnXhdOXaCjWl1JjXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازی صعود؛ رویای ایران و نیاز بلژیک | نتیجه بازی چه خواهد شد؟
🔹
تیم ملی فوتبال ایران شامگاه یکشنبه در یکی از حساس‌ترین مسابقات مرحله گروهی جام جهانی ۲۰۲۶ به مصاف بلژیک خواهد رفت؛ دیداری که می‌تواند مسیر صعود هر دو تیم به مرحله حذفی را تا حد زیادی مشخص کند.
نظر شما چیست؟ کامنت بگذارید
👇
khabarfoori.com/fa/tiny/news-3224518</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/661463" target="_blank">📅 17:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661462">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e98b351dd.mp4?token=uUjjiJvNOijdryuXqdW7iWU3YWu7EfwiUTJtHwgfDeHLytrSdqC7pOQYkoumsXt6nI31BcTiCihDIFCII9goO6X_iRSPqNLo4vG-QBOvcxipEcPM9OouFBwP_T8SPtiMcnmtlBjGiDpM8BiQtKPjC2_obhSFdAyGmFhipzXUDtsxmxTBTQkV7X7SJX__BlHQ4Uf3QaN4zNVV3erCh-y_uSMlyj6_FaK4NYlOs9kfIuFNTDlhmyjfyT1brqtl1sZ8xlqsGbgGBp4bvTQFzhU5yZJMGSaMGePKdjuvnEkP1uGmzY3XbOxU9C3QaNpp3EJst2SBMHsGcmL6LXBULQrpcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e98b351dd.mp4?token=uUjjiJvNOijdryuXqdW7iWU3YWu7EfwiUTJtHwgfDeHLytrSdqC7pOQYkoumsXt6nI31BcTiCihDIFCII9goO6X_iRSPqNLo4vG-QBOvcxipEcPM9OouFBwP_T8SPtiMcnmtlBjGiDpM8BiQtKPjC2_obhSFdAyGmFhipzXUDtsxmxTBTQkV7X7SJX__BlHQ4Uf3QaN4zNVV3erCh-y_uSMlyj6_FaK4NYlOs9kfIuFNTDlhmyjfyT1brqtl1sZ8xlqsGbgGBp4bvTQFzhU5yZJMGSaMGePKdjuvnEkP1uGmzY3XbOxU9C3QaNpp3EJst2SBMHsGcmL6LXBULQrpcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمایت از ایران در خیابان‌های نیوزیلند
🔹
شهر اوکلند در نیوزیلند شاهد برگزاری تجمعی اعتراضی بود که در آن شرکت‌کنندگان با برافراشتن پرچم‌های ایران، فلسطین و لبنان، ضمن تأکید بر لزوم برقراری صلح، مخالفت صریح خود را با سیاست‌های جنگ‌طلبانه ترامپ اعلام کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/661462" target="_blank">📅 17:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661461">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
تنگه هرمز مجددا بسته شد  قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
وَإِنْ نَكَثُوا أَیْمَانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِی دِینِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَیْمَانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ(۱۲ توبه)
🔹
نظر به بدعهدی‌ و پیمان‌شکنی…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661461" target="_blank">📅 17:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661460">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سفارت ایتالیا در تهران روز جمعه بازگشایی می‌شود
🔹
وزیر امور خارجه ایتالیا اعلام کرد که بعد از چندین ماه تنش در پی تجاوز آمریکا و اسراییل به ایران، سفارت این کشور در تهران  روز جمعه بازگشایی خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661460" target="_blank">📅 17:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661458">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
جی‌دی ونس به فاکس نیوز: دیروز واقعاً ۱۶ میلیون بشکه نفت از تنگه هرمز خارج کردیم
🔹
ترامپ به ما گفت تنگه‌ها را باز کنیم، و حالا این اتفاق افتاده است.
🔹
این یک رکورد است، حتی از قبل از شروع درگیری‌ها نیز بی‌سابقه بوده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/661458" target="_blank">📅 17:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661457">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
تنگه هرمز مجددا بسته شد  قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
وَإِنْ نَكَثُوا أَیْمَانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِی دِینِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَیْمَانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ(۱۲ توبه)
🔹
نظر به بدعهدی‌ و پیمان‌شکنی…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/661457" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661456">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌
♦️
سخنگوی وزارت خارجه: ما تعهد را امضا نکردیم که اجرا نشود؛ رویکرد ما تعهد در برابر تعهد است
🔹
اگر طرف مقابل ار اجرای تعهداتش سرباز بزند ایران هم با تدابیر لازم پاسخ خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/661456" target="_blank">📅 17:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661455">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
خبرگزاری رویترز به نقل از وزارت امور خارجه سوئیس: ما همچنان یک محیط محرمانه و قابل اعتماد را برای تسهیل گفت‌وگوها فراهم می‌کنیم
🔹
دیپلمات‌های کشورهای مختلف که هم‌اکنون در این روند حضور دارند، به تلاش‌های خود برای برقراری گفت‌وگو ادامه می‌دهند.
🔹
به دلایل مربوط به محرمانگی، امکان ارائه اطلاعات بیشتری درباره حاضران یا محتوای مذاکرات وجود ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/661455" target="_blank">📅 17:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661454">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
درخواست‌ برای افزایش ۱۴۰ درصدی قیمت نان!
امیرکرملو، سخنگوی اتحادیه نانوایان تهران در
#گفتگو
با خبرفوری:
🔹
در حالی که نرخ جدید نان هنوز توسط وزارت کشور ابلاغ نشده، مسئولان صنفی اعلام کردند گرانی نان صرفاً به خاطر آرد نیست (آرد حدود ۱۲ درصد تاثیرگذار است)؛ بلکه هزینه دستمزد، انرژی و اجاره‌بها افزایش چشمگیری داشته است
🔹
با وجود ابلاغ نرخ‌ها در اکثر استان‌ها، تهران هنوز در انتظار ابلاغ رسمی است و نانوایان خواستار افزایش ۱۳۰ تا ۱۴۰ درصدی قیمت‌ها هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/661454" target="_blank">📅 17:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661453">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38565964d.mp4?token=czdvgxsqXWSe6_tAaE34iO4aHN_g49kM3GgtYqmNbujDXVHrY3-Z-1LjMndQ6WOWYSTvJi8VeMo0-dqfjEnkGPUxsIQpA5rDHfGBJQVi4BHv4QlzaUcTlCWEmQ3XqO2ZLBR6R5Ed0TPeyqoKmdFgco0hytOi0aGJXxUUkpCLAJpwLj7wuUeA-E66qgvRejwq0H7vL6r-6szpkBOP83lAooK14W5KXi5BFTEKvVJ7qmVKfUN8knRIYzsbiqG_KQ-zn7_DxZVS78lOifCNEoNULIdh-k8TTPN4oTICcMoEM916CJiGK_Q938Xt4IeM6QXkqlCLTdT2eSZdSTs7U_hvlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38565964d.mp4?token=czdvgxsqXWSe6_tAaE34iO4aHN_g49kM3GgtYqmNbujDXVHrY3-Z-1LjMndQ6WOWYSTvJi8VeMo0-dqfjEnkGPUxsIQpA5rDHfGBJQVi4BHv4QlzaUcTlCWEmQ3XqO2ZLBR6R5Ed0TPeyqoKmdFgco0hytOi0aGJXxUUkpCLAJpwLj7wuUeA-E66qgvRejwq0H7vL6r-6szpkBOP83lAooK14W5KXi5BFTEKvVJ7qmVKfUN8knRIYzsbiqG_KQ-zn7_DxZVS78lOifCNEoNULIdh-k8TTPN4oTICcMoEM916CJiGK_Q938Xt4IeM6QXkqlCLTdT2eSZdSTs7U_hvlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس به فاکس نیوز: دیروز واقعاً ۱۶ میلیون بشکه نفت از تنگه هرمز خارج کردیم
🔹
ترامپ به ما گفت تنگه‌ها را باز کنیم، و حالا این اتفاق افتاده است
.
🔹
این یک رکورد است، حتی از قبل از شروع درگیری‌ها نیز بی‌سابقه بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/661453" target="_blank">📅 17:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661452">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a838204259.mp4?token=EZTXXUOG_DsjUtAw-Zt91ompJ2CUl0S2A4bY6KewADHl9O8RNaHBAKvQ_iD5TMq0Gs2pDQ0pRNYAEYr505JzbY7sP4H9wX9mLFRjF99qoTgxv3HOVobzHsEYry7hbZG7xAWvKTOp3wOZbC8wgM8bSYPrGTzEu4srrQAkGF5Sr6jlEs_pKeYExTrDvmIilH_M6bvMQUTMSSpBPjqEEYt02lhFNcLylqAVn8afdE0NSWjh4wKGI3EcO9KArNleftfiQ2Wa4WJMezuDms-bBIxQa-Gqi_EiWdC4nmfBuW9A-dOaNfeoQlMTNxKtGElb2n1yH6WGkcE0CziKn5pabqNzMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a838204259.mp4?token=EZTXXUOG_DsjUtAw-Zt91ompJ2CUl0S2A4bY6KewADHl9O8RNaHBAKvQ_iD5TMq0Gs2pDQ0pRNYAEYr505JzbY7sP4H9wX9mLFRjF99qoTgxv3HOVobzHsEYry7hbZG7xAWvKTOp3wOZbC8wgM8bSYPrGTzEu4srrQAkGF5Sr6jlEs_pKeYExTrDvmIilH_M6bvMQUTMSSpBPjqEEYt02lhFNcLylqAVn8afdE0NSWjh4wKGI3EcO9KArNleftfiQ2Wa4WJMezuDms-bBIxQa-Gqi_EiWdC4nmfBuW9A-dOaNfeoQlMTNxKtGElb2n1yH6WGkcE0CziKn5pabqNzMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس، معاون ترامپ: من بسیار مطمئنم که می‌توانیم این آتش‌بس را حفظ کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661452" target="_blank">📅 17:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661451">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌
♦️
سخنگوی وزارت خارجه: اگر بخشی از تعهدات طرف مقابل اجرا نشود کلیت تفاهم دچار مشکل می‌شود
🔹
طرف مقابل باید هرچه سریع‌تر تدابیر لازم را به کار بگیرد وگرنه کلیت تفاهم دچار مشکل خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661451" target="_blank">📅 17:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661450">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mho1zYX_tewnTeKAFeIDBZBrigqBj2McKurzwC87E6P-fjia3O4PQ0fPyYZJejPezjFjRr4kH2cYTsht6NZV1ITWS8Jzj-f6jsLiBRU2YgFmywbPgUWnQhBrRqd8PR0GAbn-pibKmmLZrC8nYhWtjJH7w-y_VTxmykwpzLwYupUWerxs96x9vmn6naeJmUYw6WanfriXGRQcHCVUOV5WnMVyUQfYIZliTELOwE7yXhcyQ7xCW4O7gVu9D6bWzL_WIbRNB2S8qX2i8FFmm4iz7epf9PAeRyCQ4ejVS1FSKqu4rWxiqVDkogS9eftc5HUssxb0VtZrWwUr8AM5WMBlXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهترین پاسخ ایران به حمله بزرگ اسرائیل به لبنان/ این اقدام تهران ترامپ را به وحشت می اندازد
🔹
شکی نیست که اسرائیل از تفاهم اسلام آباد راضی نیست و شکی هم نیست که تمام تلاش خود را می کند که تفاهم اسلام آباد را نقض کرده یا نابود کند. بهترین روش هم برای نابود کردن این تفاهم، حمله شدید به لبنان، نقض آتش بس و مجبور کردن ایران به حمله موشکی به اراضی اشغالی است. بدین ترتیب، جنگ، مجددا از سر گرفته شده و تفاهم از بین می رود.
گزارش تحلیلی خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3224502</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661450" target="_blank">📅 17:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661449">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ritPiNDMhzL2AgZSZ2CCA0KMbL8XbjqrDFGUiCBPIonXYvnQ8cnEy07SF4g4OkwgQO_swZhHJ6Tn-Ae1lVPJxkxHmiE3cXH1L6HucRb3MIUxKUl5dmKYQJiJApPlNQe0zc8soFl5TBtc934rXV-mlC4Fj9vt4FSbehzi67kG5ZGz3tw5iYwJ0jWTkLQQ73H3U7SVEn3_7gW9apVSvumR-XRx944S0sViODORHwqeYMhZ5cf5ZUPC8naHq1PuDeUXzb3Gh7GE8jRftzKzBdNonNAkRksM9cNJkqnYsETTe40mFfrVTwUVAwkD6BSvbEz7PP_M4PSrSnyVGLcti5wuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روضه حسینی
🔹
همراهان عزیز خبرفوری اگر در این ایام محرم در خانه‌های خود روضه برپا کرده‌اید، عکس‌ها و ویدئوهای کوتاه آن را برای ما ارسال کنید.
🔹
منتخبی از این تصاویر در کانال خبرفوری منتشر خواهد شد.
🔸
عکس ها و ویدئو های خودتان را با ما به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/661449" target="_blank">📅 17:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661448">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ما به تعهداتمان پایبند بودیم و طرف مقابل موظف است رژیم صهیونیستی را به توقف حمله به لبنان وادار کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/661448" target="_blank">📅 17:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661447">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ما به تعهداتمان پایبند بودیم و طرف مقابل موظف است رژیم صهیونیستی را به توقف حمله به لبنان وادار کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661447" target="_blank">📅 17:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661446">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: هیئت ایرانی برای پیگیری و مطالبۀ اجرای تعهدات طرف مقابل به سوئیس سفر خواهد کرد  ‌
🔹
در سوئیس قرار است دربارۀ اجرای تعهدات طرف مقابل مطالبه‌گری داشته باشیم و مشخص شود آن‌ها چطور می‌خواهند به تعهداتشان عمل کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661446" target="_blank">📅 16:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661444">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
تنگه هرمز مجددا بسته شد  قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
وَإِنْ نَكَثُوا أَیْمَانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِی دِینِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَیْمَانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ(۱۲ توبه)
🔹
نظر به بدعهدی‌ و پیمان‌شکنی…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661444" target="_blank">📅 16:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661443">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
حادثه در فرودگاه مهرآباد | پرواز شیراز به تهران از باند خارج شد
🔹
هواپیمای پرواز شیراز به تهران، هنگام فرود در فرودگاه مهرآباد، از باند خارج و در حاشیه باند متوقف شد.
🔹
در این حادثه به هواپیما و تاسیسات فرودگاه آسیب وارد شد اما خوشبختانه تلفات جانی و مصدوم نداشت.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/661443" target="_blank">📅 16:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661442">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWYt_ZoP99a80Mc4CK6UQmB4NSqDgtvuW_rlBRg9oGI_3H9N1MAeXwJpkDpXMQQXo8QfGJuWd4ACEuJC_SJTmysW1Zp0F9lYWDidzNC8XKiUn2MJgLaWrhLNraLerXHMwNUEL_ePRc5wuJ9mtIBaqfCxWhVPEHTlMOU-1Zmadq-LeUm6PRJiZdBoQ5ebwonCD19jz01swXp1sGOoSSb37MIpdLzyGWhOytHt1B52eMgDn6FOeLuBa3sv-2qtBo9T5gKt75rhUDT-l33NZW5MaV-DmUzjLJbmjza4Fe3xnC9RRbZR1PwJMUJBK0JW8OtoajSVNog86wlP3ArYTDYqvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بار دیگر ملونی، نخست وزیر ایتالیا را تحقیر کرد
ترامپ با انتقاد از موضع ایتالیا در قبال جنگ آمریکا علیه ایران نوشته:
🔹
او زمانی که بحث جلوگیری از دستیابی ایران به سلاح هسته‌ای مطرح بود، از آمریکا حمایت نکرد. حتی اجازه استفاده از باندها و فرودگاه‌های ایتالیا را هم به ما نداد که یک دردسر لجستیکی بزرگ ایجاد کرد. با وجود اینکه آمریکا سالانه صدها میلیارد دلار برای حفاظت از ایتالیا و دیگر متحدان ناتو هزینه می‌کند، آنها از ما حمایت نکردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661442" target="_blank">📅 16:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661441">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ونس: به مذاکره با ایران فرصتی خواهیم داد
معاون رئیس جمهور آمریکا:
🔹
مذاکرات با ایران فردا امکان‌پذیر است و وایومینگ و کوشنر برای انجام این مذاکرات آنجا هستند.
🔹
اوضاع در مذاکرات ایران خوب پیش می‌رود و انتظار دارم به سوئیس بروم
🔹
ما به توانایی خود برای حفظ آتش بس اطمینان داریم.
🔹
به مذاکره با ایران فرصتی خواهیم داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661441" target="_blank">📅 16:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661440">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
حمله مجدد اسرائیل به جنوب لبنان
🔹
رژیم صهیونیستی بار دیگر جنوب لبنان را هدف حملات هوایی خود قرار داد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/661440" target="_blank">📅 16:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661438">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
تنگه هرمز مجددا بسته شد
قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
وَإِنْ نَكَثُوا أَیْمَانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَطَعَنُوا فِی دِینِكُمْ فَقَاتِلُوا أَئِمَّةَ الْكُفْرِ ۙ إِنَّهُمْ لَا أَیْمَانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ(۱۲ توبه)
🔹
نظر به بدعهدی‌ و پیمان‌شکنی آشکار آمریکا نسبت به عدم اجرای بند اول تفاهم‌نامه‌ پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس توسط رژیم صهیونیستی در جنوب لبنان و کشتار بی‌رحمانه و آوارگی صدها هزار نفر از مردم مظلوم این سرزمین و همچنین با توجه به عدم عقب‌نشینی نیروهای اشغالگر صهیونی از اراضی جنوب لبنان، اعلام می‌دارد تنگه هرمز به روی تردد شناورها بسته خواهد شد.
🔹
متذکر می‌گردد این گام اول پاسخ به عهدشکنی دشمن است و در صورت ادامه تجاوز گام‌های بعدی برای پایبند کردن دشمن به اجرای تعهدات برنامه ریزی و اقدام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/661438" target="_blank">📅 16:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661437">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
شکستن طلسم ۳۰ ساله بوکس ایران در جام جهانی
🔹
مهدی حبیبی‌نژاد با شکست نماینده انگلیس مدال برنز خود را قطعی کرد و طلسم ۳۰ ساله بوکس ایران در این مسابقات را شکست.
🔹
او فردا در مرحله نیمه‌ نهایی به مصاف نماینده آمریکا می‌رود. #ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/661437" target="_blank">📅 16:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661436">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9975898851.mp4?token=UBkFiFDGl75p08zfB0xecXyiT89_owOEvx4iPwLSC9cAfDK4W5nN4YDoV2UMgQjjpPH5w4ayjc2VSWfizwQZkoodWAbSZUI1UtvWYSSsaFcYwj8wUWr9TlE3B4GcYHuYqL0SwMaDnzTBCCqvdAy_5RobBGPWvbI_EaMho-RtkoBSXZ5D5jM4edxwT1wszldO4iqbDsbkX4blM2SJloLBUDTBWNNIeUtcFg-NCcJANFYEW4RrtjzGfh8YjLcn0t-8Z715K4GeYZzzMAZ68JHN1e8n7e2iCG1hfmyETddQ8BLROSnSHnsYuuYGjEAm7XlHqR4ddtaXhwgE5AHco07oxBox7ioy6aNvkcvhKCaW_KwKvD1XISrUDIDGo9Lt3h_OqTA0qcQGlfJ_xPD31eQMHiZWsvRVcPdFNQfit-FytAOx7heVnuS-iHUZYSWGyLRGeGAQ3rCCrjxfqoP_cID9Qi-blsmq7q_6fcf4e8_NcSWTMjeb5OgB42L_R8YnJqp5PMsv2ZXBT4uJ3oEzfN6m8vsxmd-gC8pR2REAcJeJgE4l0RhuFrYzINwNoG8f11tf0yzYX2zyasKMRxrc2KL30EFMNwtaF1SJjmzy-eCERaYSV4dM7dNOowMw6XoTvdyBkIIMXaYEeGARMunlNDv5VDGZaUv3KGJ3i33Oeio93dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9975898851.mp4?token=UBkFiFDGl75p08zfB0xecXyiT89_owOEvx4iPwLSC9cAfDK4W5nN4YDoV2UMgQjjpPH5w4ayjc2VSWfizwQZkoodWAbSZUI1UtvWYSSsaFcYwj8wUWr9TlE3B4GcYHuYqL0SwMaDnzTBCCqvdAy_5RobBGPWvbI_EaMho-RtkoBSXZ5D5jM4edxwT1wszldO4iqbDsbkX4blM2SJloLBUDTBWNNIeUtcFg-NCcJANFYEW4RrtjzGfh8YjLcn0t-8Z715K4GeYZzzMAZ68JHN1e8n7e2iCG1hfmyETddQ8BLROSnSHnsYuuYGjEAm7XlHqR4ddtaXhwgE5AHco07oxBox7ioy6aNvkcvhKCaW_KwKvD1XISrUDIDGo9Lt3h_OqTA0qcQGlfJ_xPD31eQMHiZWsvRVcPdFNQfit-FytAOx7heVnuS-iHUZYSWGyLRGeGAQ3rCCrjxfqoP_cID9Qi-blsmq7q_6fcf4e8_NcSWTMjeb5OgB42L_R8YnJqp5PMsv2ZXBT4uJ3oEzfN6m8vsxmd-gC8pR2REAcJeJgE4l0RhuFrYzINwNoG8f11tf0yzYX2zyasKMRxrc2KL30EFMNwtaF1SJjmzy-eCERaYSV4dM7dNOowMw6XoTvdyBkIIMXaYEeGARMunlNDv5VDGZaUv3KGJ3i33Oeio93dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جایگاه VIP استادیوم سوفی آمریکا
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/661436" target="_blank">📅 16:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661435">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPp43CSYqI8vWSR9U29XdCq1ckln3ybHntI0LXIlHsmk_5rJi_nmdL_jFpqnK_9OjV2XUml0uLYlvW21cRP11EgKbaWsd26F2kJXxZBvHJR22c5j8X_cMJZcPGaytnEwqnmpby9aajxIFdJsequp-K3Lpdff2I9O3tAPLRxv4HgsG_1lVHDfdY4WThH5GVUtfTszZail4-cFU4B_Cc3K7U54txqHSYCuLELTHoN1TpSap3E9BbrlEpK4XeieNU3SiGUfvWEYSiRZh9lH1myHuRka2OEG6ENTusO1WKkLaBTDIzbzcxj5UZredeqy9Go_ZJ1C0qKLCo2LhKEnhKYOyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وام بانکی: طنابِ دار یا سکوی پرتاب؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/661435" target="_blank">📅 16:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661434">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dc19b6b7d.mp4?token=cdhUT0QwXqHOr4p1YxJoabz5Jen4pSE4tPfKmewCKPEBDfOUod0Y5WzzDztW6oAxGtFA4MO2_Wfb9nA1IJAHjLYscidVvmWl6R_HZmxbEILe6u5wiMIWH0WbRUaIx4F51sK-zectE4YAzEpAVaeEIXuzRUZDrefGDAWijCHJUpGjpkYtsRyKTfk_fBdYbPBMZPvWMvVnGABsYZ1LaeV0XJBBNeDyfIoTLpaA-vaw5rnpzovq3wfn97f8Lz-HKXPOqks99Oc-NNAESONzUSfcbbJYauFGtDszsAagPi3gjOJh8LI3NEJlcX9WWyRA-VFIvGLYeMe0yRByVZwVSDlZAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dc19b6b7d.mp4?token=cdhUT0QwXqHOr4p1YxJoabz5Jen4pSE4tPfKmewCKPEBDfOUod0Y5WzzDztW6oAxGtFA4MO2_Wfb9nA1IJAHjLYscidVvmWl6R_HZmxbEILe6u5wiMIWH0WbRUaIx4F51sK-zectE4YAzEpAVaeEIXuzRUZDrefGDAWijCHJUpGjpkYtsRyKTfk_fBdYbPBMZPvWMvVnGABsYZ1LaeV0XJBBNeDyfIoTLpaA-vaw5rnpzovq3wfn97f8Lz-HKXPOqks99Oc-NNAESONzUSfcbbJYauFGtDszsAagPi3gjOJh8LI3NEJlcX9WWyRA-VFIvGLYeMe0yRByVZwVSDlZAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر کشور پاکستان با عراقچی دیدار و گفتگو کرد
🔹
سید محسن نقوی، وزیر کشور پاکستان با سید عباس عراقچی وزیر امور خارجه کشورمان دیدار و گفت‌وگو کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/661434" target="_blank">📅 16:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661433">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrsxKRNpD7RCDotIQLKniLfmBdB8930lEJQ7lDPs8UrdahT7FPBmIfd7yHXKdVQ2Sf2r4ljRgRvEDmlAZGSpuhL_6w7qtLANfkmw7x3kPT2lup0vSMJIlca665gVcTtTqBXyyLNSb8aE2LTRhzzM0u1MIdn-7ZfoT3UmEj0Nm057NC01ItD6Vm-_lyyLke7UodfAMI463MKV-nh95YohgL8lGCDXm586smP9OZaeEhPTyvcIKfcxdEvPZO5ys5WmVQny20K6EFv1cWjcwgeW5frsMXd2L8vqqABvyU-HeAwzuGNwSYAAjPSvAEyy8ubLQwKyIQAJ3H0w5i7B_piasw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ پستی درباره تاثیر خود بر آینده سیاسی نتانیاهو را بازنشر کرد
🔹
در تیتر مقاله آمده است: «ترامپ برگ‌های برنده را در سرنوشت انتخاباتی متزلزل نتانیاهو در اختیار دارد.»
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/661433" target="_blank">📅 16:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661429">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIl-rlD3WOzbshc6louxZhdFXW88l25twSb2_4SHZ6EI-j13CCa9bOzGC-01LjEfrE-FcP3ApGjP3rwNP0zw-NKeHRDVSXAl6q2CYGFfGxnKbN2uWQFvbGBqoAE_VSeV9vFPL2U3LzEId213s-AGwvoMweDz6bAivAL7wx9TPTvUkA0ia0JjugKQpFIWnmG33L6wQOIRQevGL2kqyKvycFCgPW1GZFVPwbcYNc7kY1-qfiYiHLE6euBPtflgXzRgdEOFkQcQjvt5zvpYm9SPepb3kJl4w1ZWYVHnjnc4E77-4rNRWjrMADgeE5bfB18uSSuyRImIrUurvwsO68NXkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iebQHqmdWBJck4LJ3OBJfXs0UoX9Yhj9e3gmkafj1uSY1TFurUsSQQTDkT6jyQEA5xnhWgFHboZdtpSLxfrcrO082UqRB38LwSLvfkqohZnN_XWhZ7eEp3GXKS5BZ95m1eJ1Z81xL6JP19NHCOmFsDY-xgWKmNadUGuyY2uRiNiJafWInAzFowtcwrE_1J2kxcmpwaIxvBFIB_-v6lfDTJOTvn8A6koHEqtMyXtX2J2isorQci0BaF-UqJzF35ZepRgJsA6hAFnnmtrcfTtCt__nbjY5U7mFP8Lxs6YbyecbSeVwfDG5_6toVfEqHvqeT8S0oB7johIFKHE7gHs5Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkCN4uamW_QtSoi5N0qLeVxPt1huXnjObgx_-1fv5mMZyzqgqZQbAatEo39c6JdYU7JJg-epetbK17mjEgh6U8wEylb_UT3HY7x34EG2bqB2sx4Ji8MJ2qLQcQESfB1kqNyZneldmyS4ivmBSZrnxFN46_xZNdEkoxgxFEvFK0ukI5aPFx3dkknwSDkYbmciNGl08EpCO8I6GHIy2UQf4LYjx2WMj0LtE2OUSaGcA3W7QTKfYkIFWo7LIFEIBoO8xRUOg-_vtc8QzX65CIHC9kVRZ_JapLOgjIwBBjB90ooWBB4J9Va5O-ozYCQgwPfXyZ3SJq563BQ2RMvnRVXFaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HX_1E8Ymuk84uDRptqcIogAjoJRVBbCvhYBlEyIbzVZUDgxijs-MYAclyzWbC3myyf9enFLHzyv-0tFReBoD5pwpV7C0nbW5M7k0W0PIzWKJJ5M2JdwYVRmdoVAS5GolSZVTpN5b-l_rAWkil2ZSdl8ZxvDwxtQA7vbQ7x5gtp6Is5NKw_iVns_iKknT-OGI08jpwVEW3Bbn_m3eYIoMkrsPVLFePfloCfgdS2czEKKdua1G6B8oeAOsEdMWAY_GXQcA8yGLRzG7rGDnJrvfGO0esn2XNNMqSvwRVOjZR0BPn9MKQwOJo391oFjqj4EOevGGzLWBvd7c8GGuEQH4Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگه دنبال یک کیک خونگی خوش‌طعم هستید، این دستور رو از دست ندید!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/661429" target="_blank">📅 16:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661428">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2_EaXHyQXFZS8aoSNRzskWFOIJPRTHrXkv3UE3MCQHKuuE7XiqU3HCozVdkJJJKdskrOFxVeg1OoANuNdNdfhgRIRscR9Nv-A6Yt-04uY5OFX1GSnBv_PI7yzXd7xBj2J0l7UnT_yaA9O47bvtarl50UoSeZBxN-Ei2FZZo3Ge5WsVW27AlcdGRvuYt4xMtKR5gNNgfqAyz7F6zyPdBym9cg6KQlAFlcTJQ0rZF6opY-Oyl76dCcOsvrjpFFXsSJNobrT-CoUDsMzI1EguZt2FJ1-Rz3GqKMVtihOjfwtHqNA4POAkpcMkoTYC0vij9fIeKU0KmqYwlXAZmcYlVOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
کشف یک شگفتانه شورانگیز در «سیاره صورتی»!
🔹
تلسکوپ فضایی «جیمز وب» شگفتی شورانگیزی را در «سیاره صورتی» معروف کشف کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/661428" target="_blank">📅 16:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661425">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNx4LsxPa9tBJEvp3rMLXE7TrSi7ei7dZXc0eeph9JVAJljwY6b3gooWNuHPV99CyqjKTBK79hauoHsG9_8sOz7a_DF39Q71vyBlbeV489D4zlhDAYuQR_vLkwUSMwY4P8cxpkslg6Ta4mp0obFzuf5l8wIDhCZJE7a0ZeGPjWgTfrB406OMhYMOBHUysHi-exiDWDQAY9LsIwB0j6okYT8CF9Ug8uck7UCMdSWpPEkAvyFLfX6CmrI1GuXBGkOyIQLCaeqYB5TGsZODtLkL_H4BPj03VOCeMICFph5qrE5icP4nYI9FnEdGKbQIl9vhIRrxs-lP_B6YWg8rTEmOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pq7JR9Wc5VF1nlm6hc50OKFZcmayMgM1y8STRON5PVdGkzQKlZJJYgTM7gSkq4V5ye975GLOpOu9EFwo1GSpWqT0FyLR81PvYFUBDCU7DUlWg9phPEIYx9OoLcUjWbSZrPqWp6JXnlZtyPq0-J37qwN65xitsKnM_riE578CHMI_R8COjs95_fEP-llzemelL7mw2nf-ApD8T9yv-isaYA4pM_oG9VQu5FayLwszonYNoQoDAQr_b3Y-TPvbMA0QVn-vnQ3t5U-y3_RIXqsNoiHRN9S3OIs49J0CnvkdzlZ_vo96vn71hhkWfzc10OkbZy4Oag4N0efkkoRABRhTBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ah4JoLD4TNv_kHDD9ow_RC7JsGFVhESSldJz8z6hgN5MyA2ZvXQovCaj6fizb9KuypPu35lhvqQAAMFeGSmjBqBdBvsCfNipdl4aQT38hPRttSt_0DOq8ENTEmXvAusCE18c1m5mzM-B-heMohN4Rj0MwLSIf9uSDTSA7bbgN2V6E4hDcJMi2L-xvzejrHAd3Zq9KuRdAEuf2spQBITBfFsICBSKpq6jkQcotZ-8zIslUMOcSf_QLh2TdZDqW0wj2zaccQ6upLoUXnuvcuJ4VPTzCyXNth_i1slqK6B59QEPXIlqo18OwN4idaAnDOZwjgAMbAQb5XNWfLImA98U2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حمله مجدد اسرائیل به جنوب لبنان
🔹
رژیم صهیونیستی بار دیگر جنوب لبنان را هدف حملات هوایی خود قرار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/661425" target="_blank">📅 15:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661424">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c0899f051.mp4?token=qeWUJgESQA9Aq_m1cs6exvr2OueCmRBkNqUGcE7mlj7AM5OhbXaNyJPDXfMU19GTysYXCJ0BWXSxcQLNGw0L-AaTkLSxeigokeg8NjIfn89ZoasBTCLgnbklT6TuM4dl8pSqtASNckZYKc125TY8ip6QWkPrFslL8F0ocFfCtWtSufL-6-Oywq5cRsL9xRW01oDoRjpDnR7NUphib7LKEES5MFTRDnbbCoWotTaia3J-nLzWxy53Bl7pNlMo8vXK4AUDRPKPU3Dyty7ehIeuEWglMNFvynkAPxbJe3ZwqmC3gS2z3oCjlvbjTj4P6WTKUhbeCg-v-xE2LJuudW7QrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c0899f051.mp4?token=qeWUJgESQA9Aq_m1cs6exvr2OueCmRBkNqUGcE7mlj7AM5OhbXaNyJPDXfMU19GTysYXCJ0BWXSxcQLNGw0L-AaTkLSxeigokeg8NjIfn89ZoasBTCLgnbklT6TuM4dl8pSqtASNckZYKc125TY8ip6QWkPrFslL8F0ocFfCtWtSufL-6-Oywq5cRsL9xRW01oDoRjpDnR7NUphib7LKEES5MFTRDnbbCoWotTaia3J-nLzWxy53Bl7pNlMo8vXK4AUDRPKPU3Dyty7ehIeuEWglMNFvynkAPxbJe3ZwqmC3gS2z3oCjlvbjTj4P6WTKUhbeCg-v-xE2LJuudW7QrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر یک از نقوش اصیل ایرانی، نماد چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/661424" target="_blank">📅 15:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661423">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKpFPDxjI1McbSb8rRWXp-sMD3rKCf1_qfAMH9AzR6NcHjXOYh8Zd85pxMZu6sKInwDulNyUhc9mjhA85gVTdeORZgJWcls33enVNXDye62UaRrFA88eVEfXvdUA48KtL9Mp0HRHrNhHuRpqbndH9IahjXw_TYLhbhtVVfhJQXd6j8dXSzLSXE61m2wijDjLM61i4BxuMp03yeTZFzkF3yYgD3Q-gwcQ_0A-DzX7wrltyWnafoUvAMBhYMHq2DWMPqg60P2QKU4lpfo606ExsvejB9MsrgULhvi25gQSkEumxwZhC8eLj3ILbW58tJd0b-kN5wT0NFgQMPX0eV4j9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
«سِروال»، سوپر مدل دنیای حیوانات
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/661423" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661422">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
یارانه خردادماه ۱۴۰۵ به حساب سرپرستان خانوار دهک‌های چهارم تا نهم واریز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/661422" target="_blank">📅 15:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661421">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/972310ae87.mp4?token=Cm443kqXA9kOJZkzfwiYFYjVE86xlkkaChLXVDxz12u-X4z_XXaNInq7KUSfJNfMQ11F5vOBh-7WZ0wqML9SoqdIVXBEJGDTZCWOQcFoSZEpxTuFs-6gwzVuDnUYyAjykkSVNjuQcbeCOVEr6o6F0B0ml_SNbPO4j6-wSdjofP_n8Xj36PgeXJMXzNNY8RDQEOVRoRqaGQh9JhXBTjhnKRBt4uqSfHk-xRHd0GlZRRFd7E_fCu35QaamDtRVFV3CbjW3GAnrxmzFz6TF5isdmzZ-BRHnjmiQN_oRB3pxPmLsYoNIE9fIV9N16xwl1HeWRnNdmILckzcFA71seGvUkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/972310ae87.mp4?token=Cm443kqXA9kOJZkzfwiYFYjVE86xlkkaChLXVDxz12u-X4z_XXaNInq7KUSfJNfMQ11F5vOBh-7WZ0wqML9SoqdIVXBEJGDTZCWOQcFoSZEpxTuFs-6gwzVuDnUYyAjykkSVNjuQcbeCOVEr6o6F0B0ml_SNbPO4j6-wSdjofP_n8Xj36PgeXJMXzNNY8RDQEOVRoRqaGQh9JhXBTjhnKRBt4uqSfHk-xRHd0GlZRRFd7E_fCu35QaamDtRVFV3CbjW3GAnrxmzFz6TF5isdmzZ-BRHnjmiQN_oRB3pxPmLsYoNIE9fIV9N16xwl1HeWRnNdmILckzcFA71seGvUkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ونزوئلایی‌ها تصاویر ترامپ و روبیو را به نشانه اعتراض سوزاندند
🔹
تصاویر سیاستمداران آمریکایی که بیشترین ارتباط را با تجاوز آمریکا به ونزوئلا دارند، توسط معترضان مخالف موضع واشنگتن نسبت به این کشور در خیابان‌های کاراکاس لگدمال و به آتش کشیده شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/661421" target="_blank">📅 15:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661420">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/254877efcb.mp4?token=MfBeQGJA8DfdHqSM8ZVgFHTuJW3IpJOcOQlvzH8tohfFfkpJA00fhVTwuuIb6apjXfO7HlKZ1UC_XslJqnGi3Nj82_UBV2ncf1hJzrRK3iQqHt4AN7tJnVzFkalA5y-TIAtYROOCnJ9B225WiwZTXzkNnVZGVavPPqqo9d7AT9D89hcLxpfN2W7IGhMo5jstrqyLtrKHSJhyfs7V1sDxmBaq1ct2ELDC-q2P8SvdJG_XeGJCJQED1NKj98kDeXqaNC0YqOBKrNHtw9FBh70giRJDJTJsOCTvhJhm5D_4TQzRn9kfNx0CwGnw3WXQtsrAPLqgyBhfeeb4n76wYS3IzRZPX9DEIsW6AfdSjv1V59N31xiPIPmaaD_aUC_5FU5VNg8fFkwWZHxvdEV3B6oxLdgBtWNB5f0rK02rY-XzQlBiRUx6FC6sO_zc28hCzKxZUhNL1hBbTVGKirrW1Ve-J4wSX_oJTRLyrmrs5NUEvZ6eBYdzt6csuGMdukhHYjElY2E8vA95mxA50gRJRHkfzwikVWcbFANAA4uJM1H0eQUBKNSb_SaO3puExmPTYLKZhh8H5K-zSCSqCnq54mXHdy9FeMS302Lutk-Ep_tW5iZ3fTbqwAve_3Eq57dw6LFPEf2nmhgj-jV9jRfI_r5dEqvHPDTCdEsa2L-lcp2Mnvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/254877efcb.mp4?token=MfBeQGJA8DfdHqSM8ZVgFHTuJW3IpJOcOQlvzH8tohfFfkpJA00fhVTwuuIb6apjXfO7HlKZ1UC_XslJqnGi3Nj82_UBV2ncf1hJzrRK3iQqHt4AN7tJnVzFkalA5y-TIAtYROOCnJ9B225WiwZTXzkNnVZGVavPPqqo9d7AT9D89hcLxpfN2W7IGhMo5jstrqyLtrKHSJhyfs7V1sDxmBaq1ct2ELDC-q2P8SvdJG_XeGJCJQED1NKj98kDeXqaNC0YqOBKrNHtw9FBh70giRJDJTJsOCTvhJhm5D_4TQzRn9kfNx0CwGnw3WXQtsrAPLqgyBhfeeb4n76wYS3IzRZPX9DEIsW6AfdSjv1V59N31xiPIPmaaD_aUC_5FU5VNg8fFkwWZHxvdEV3B6oxLdgBtWNB5f0rK02rY-XzQlBiRUx6FC6sO_zc28hCzKxZUhNL1hBbTVGKirrW1Ve-J4wSX_oJTRLyrmrs5NUEvZ6eBYdzt6csuGMdukhHYjElY2E8vA95mxA50gRJRHkfzwikVWcbFANAA4uJM1H0eQUBKNSb_SaO3puExmPTYLKZhh8H5K-zSCSqCnq54mXHdy9FeMS302Lutk-Ep_tW5iZ3fTbqwAve_3Eq57dw6LFPEf2nmhgj-jV9jRfI_r5dEqvHPDTCdEsa2L-lcp2Mnvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشه‌ای از تمرینات پرفشار کره‌جنوبی در راه آماده سازی برای جام جهانی آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/661420" target="_blank">📅 15:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661419">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
دادخواست رسمی خانواده شهدای مدرسه میناب علیه آمریکا ثبت شد
🔹
رئیس مرکز وکلا، کارشناسان رسمی و مشاوران خانوادهٔ قوه‌قضاییه از ثبت دادخواست به وکالت از خانواده شهدای مدرسهٔ «شجرهٔ طیبه» میناب علیه دولت آمریکا خبر داد و اعلام کرد این اقدام پس‌از دریافت وکالت از خانوادهٔ شهدا انجام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/661419" target="_blank">📅 15:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661418">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1960e5024c.mp4?token=pQoA7r_Tf69VvnASZtrBk2bbFHTQOlMF4NcHcrzEbviYGaIsoSD3mUdJZ-5nined7cTeXnqrbFUTZO3ASZFk4JqECr4z-_NCkQWDuWSXcgzqSBg1vMEBnt6mnGUG4Bu7-K5zyrVCJAr8MnP4SPdhYPvJCGWFyILBebbJzeFJw68-AtTL_c5tTIVmyMWGS82aWybBRkK3y3AabJhdw6momc34b5qZ6pYI7HIrND51DjrbmbeCwf-HiOwbTBVdImfSGkvBQZiobDXevzuzUsqqCk7W4yEW4urrPQNB6TqCnrqoCKX2u6sWMPrhF_dzM3hMXMZOY30Wv0ToQ-e5GjhSLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1960e5024c.mp4?token=pQoA7r_Tf69VvnASZtrBk2bbFHTQOlMF4NcHcrzEbviYGaIsoSD3mUdJZ-5nined7cTeXnqrbFUTZO3ASZFk4JqECr4z-_NCkQWDuWSXcgzqSBg1vMEBnt6mnGUG4Bu7-K5zyrVCJAr8MnP4SPdhYPvJCGWFyILBebbJzeFJw68-AtTL_c5tTIVmyMWGS82aWybBRkK3y3AabJhdw6momc34b5qZ6pYI7HIrND51DjrbmbeCwf-HiOwbTBVdImfSGkvBQZiobDXevzuzUsqqCk7W4yEW4urrPQNB6TqCnrqoCKX2u6sWMPrhF_dzM3hMXMZOY30Wv0ToQ-e5GjhSLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لاپید: تنگه هرمز قلب معادله جنگ ایران است
🔹
رهبر اپوزیسیون اسرائیل می‌گوید هر تصمیم نظامی علیه ایران، بدون در نظر گرفتن اثرش بر بازار انرژی جهانی و تنگه هرمز، عملاً نادیده گرفتن واقعیت‌های اقتصادی آمریکا و سیاست داخلی آن است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/661418" target="_blank">📅 15:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661417">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd6d14fba.mp4?token=Dp1Xk_p6sph2iWcsSWYwkYJ6i4J1x6vpijXEPoGsAOWqCjzjOe_GwfT6VFyKHJKtb5tVlvaeLDYra2RPsWUfOgh5tircD79uzlT7M4HB-Hq9aFWTmctlNKoc1yxW1UXFKBCI5w84l2WB53Nuc_0wdv9irVNW5Wts8G0kA8WY3bgAIASb9JXOJEYseHRCgAlTzfLFNLePnufm77dAxhfc4-wSPZQv70tgjqUeca6HR6tTXxNsnhU_BkGmAzOXok2ynXAxu26WvRWXLsnCnJc4QNsUvo1RtlQDZtoN8rzELqeQQsTdS9OvJ4aaWWqjwi-LwIfWKW6rg0mMW9q6TQWutYPEOUDxc8n-3HK3-P-oasSMRrVNFPhB-tyDEIaUXP4rnBGgqRPtmXR0AqdDxJ391uXNPV3b2OxO2uG8mt1GMmsWVQ6nskPBLU_jRbL4gVAJYHNldYmaEFy_4XiRgkzTbpx-jzvycmCj3FBu2ahGFfg3OB-EVia5_fkSGMR9Z_P0ugXsuJofoX9N9jDuovAn1peHgI4g18M7DUY9_TGKBtPHkgtAUv5hXqyOow_nTWLkXqZ8zrzLYMpuMxtQB9h4PvWIjdH6YtkQ_BtEElFGhHH3GrBPw0LGCHyrxLDLAE_YO2qfL4cCHdIv5_J3nwxzcXBhkn7vOoSj1clIpOgyuj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd6d14fba.mp4?token=Dp1Xk_p6sph2iWcsSWYwkYJ6i4J1x6vpijXEPoGsAOWqCjzjOe_GwfT6VFyKHJKtb5tVlvaeLDYra2RPsWUfOgh5tircD79uzlT7M4HB-Hq9aFWTmctlNKoc1yxW1UXFKBCI5w84l2WB53Nuc_0wdv9irVNW5Wts8G0kA8WY3bgAIASb9JXOJEYseHRCgAlTzfLFNLePnufm77dAxhfc4-wSPZQv70tgjqUeca6HR6tTXxNsnhU_BkGmAzOXok2ynXAxu26WvRWXLsnCnJc4QNsUvo1RtlQDZtoN8rzELqeQQsTdS9OvJ4aaWWqjwi-LwIfWKW6rg0mMW9q6TQWutYPEOUDxc8n-3HK3-P-oasSMRrVNFPhB-tyDEIaUXP4rnBGgqRPtmXR0AqdDxJ391uXNPV3b2OxO2uG8mt1GMmsWVQ6nskPBLU_jRbL4gVAJYHNldYmaEFy_4XiRgkzTbpx-jzvycmCj3FBu2ahGFfg3OB-EVia5_fkSGMR9Z_P0ugXsuJofoX9N9jDuovAn1peHgI4g18M7DUY9_TGKBtPHkgtAUv5hXqyOow_nTWLkXqZ8zrzLYMpuMxtQB9h4PvWIjdH6YtkQ_BtEElFGhHH3GrBPw0LGCHyrxLDLAE_YO2qfL4cCHdIv5_J3nwxzcXBhkn7vOoSj1clIpOgyuj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحریم و اغتشاش دستپخت ما برای نابودی ایران بود
نفتالی بنت:
🔹
در زمان نخست‌وزیریم، با همکاری موساد و سایر گروه‌ها رویکردی ۱۳گانه در قبال ایران اتخاذ کرده بودم.
🔹
این رویکرد شامل فشارهای اقتصادی، سیاسی، امنیتی و غیره بود.
🔹
یکی از کارهایی که کردیم این بود که هزاران ماهواره استارلینک را داخل این کشور قاچاق کردیم تا در اغتشاشات، اتصال اینترنت برقرار بماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/661417" target="_blank">📅 15:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661416">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33afe1d58.mp4?token=c3Af2IF6w8syDgKRVTTVAq6SKdcF4fEzWR8A--SUaIix7ycdNun-Bs_2J5CVVAdqLBQP8rYWR0zHOMgP2uoLFme_KSH2ZoCup6RMH_g4cZeitRDUEBa8TNpVBhO2TeUjBKblec8JbRaxNv42LZHNUxmy94qau2lrIlu7GP64v1-XVlMfsQeXyG1Ga4ypXujTwx1Ye8JQoCw732Iw0eus6TtcN9C1Y2dZyFtOV7VbTj8JaAie9H4aBEnxQ9yl89YaTjySJEw-WFCpa2fjyI5-rZytbsw4zr9LoQa8gc4FrPLrI8BdKFxQPoxm0pNJV1bKQlNHiboqdIteR0hU1_rVyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33afe1d58.mp4?token=c3Af2IF6w8syDgKRVTTVAq6SKdcF4fEzWR8A--SUaIix7ycdNun-Bs_2J5CVVAdqLBQP8rYWR0zHOMgP2uoLFme_KSH2ZoCup6RMH_g4cZeitRDUEBa8TNpVBhO2TeUjBKblec8JbRaxNv42LZHNUxmy94qau2lrIlu7GP64v1-XVlMfsQeXyG1Ga4ypXujTwx1Ye8JQoCw732Iw0eus6TtcN9C1Y2dZyFtOV7VbTj8JaAie9H4aBEnxQ9yl89YaTjySJEw-WFCpa2fjyI5-rZytbsw4zr9LoQa8gc4FrPLrI8BdKFxQPoxm0pNJV1bKQlNHiboqdIteR0hU1_rVyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پروفسور جیانگ تحلیلگر سیاسی: از نظر راهبردی ایران نباید آتش بس را می‌پذیرفت
🔹
اگر ۶ ماه دیگر جنگ ادامه پیدا می‌کرد کار آمریکا و اسرائیل تمام بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/661416" target="_blank">📅 15:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661415">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738e76890c.mp4?token=EDuuwfFyPM3trE05UDr1cuwlfMHCmQhyxYafEDZvG9-mHZFk9rq0yYHSDCyeAp65AMHuaTXb9O-oI_1MBpuNdGVoiOMHLgMs31zvolEq2bSQzXbDZWB4-9ajadRtlXo5DJ2333JgUKWUQTk8xbGCH0wPA3fT98J_I3xPf73H9PNfKL9W05zF8eCSBlDcUcgW3fg8oZveHgYv5qUM5Cg-ZbioCQ-Jt0Plm7BnIVp7OH-uUWcbL8Vt1q1LubJWTNjNmA4dBxbjwps15Cp3MwQO89ybTPF72eUXH1Mk9oT3u3AyXGha3JvoMyHg8ke-spJ45ZUCvLp7JWJX-BXO4aXVgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738e76890c.mp4?token=EDuuwfFyPM3trE05UDr1cuwlfMHCmQhyxYafEDZvG9-mHZFk9rq0yYHSDCyeAp65AMHuaTXb9O-oI_1MBpuNdGVoiOMHLgMs31zvolEq2bSQzXbDZWB4-9ajadRtlXo5DJ2333JgUKWUQTk8xbGCH0wPA3fT98J_I3xPf73H9PNfKL9W05zF8eCSBlDcUcgW3fg8oZveHgYv5qUM5Cg-ZbioCQ-Jt0Plm7BnIVp7OH-uUWcbL8Vt1q1LubJWTNjNmA4dBxbjwps15Cp3MwQO89ybTPF72eUXH1Mk9oT3u3AyXGha3JvoMyHg8ke-spJ45ZUCvLp7JWJX-BXO4aXVgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لاپید: تنگه هرمز قلب معادله جنگ ایران است
🔹
رهبر اپوزیسیون اسرائیل می‌گوید هر تصمیم نظامی علیه ایران، بدون در نظر گرفتن اثرش بر بازار انرژی جهانی و تنگه هرمز، عملاً نادیده گرفتن واقعیت‌های اقتصادی آمریکا و سیاست داخلی آن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/661415" target="_blank">📅 15:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661414">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
وزارت امور خارجه سوئیس: ما به فراهم کردن محیطی محرمانه و قابل اعتماد جهت تسهیل گفتگوها در بورگونشتوک پیرامون اجرای یادداشت تفاهم ادامه می‌دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/661414" target="_blank">📅 15:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661413">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee9dcec1c.mp4?token=mRvbiFdfNt5QuO39NzDA_jhluCbXj9rdAo0p1-bkkvQlWy_y7HOF0lQ7XFSIDA2XdEzZo8oH23MYqgkYpMmGHInv14Ol7EvTTTx3DTazc9MRBaGGWG44Op_brZ1KU_etMuAVk0nY8pVzKoKmz-BTozZ-ZuTcjP-OVMMS7l6QfmgrS_KShdAD-J9riNFOvOMArzsceiXu-zup7OCqncZ_U74sOWmPFsmoCUBynueCGSR2_KN_I8A_DgklzM-GdGvkeNPXaP7LE6KYFNcS9vySDBcdU9HhKnrkbkxQiMCmgvJnSeBiyUzqcbLk9-nLM9eIkgJGK153wCnoZc_5frZzWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee9dcec1c.mp4?token=mRvbiFdfNt5QuO39NzDA_jhluCbXj9rdAo0p1-bkkvQlWy_y7HOF0lQ7XFSIDA2XdEzZo8oH23MYqgkYpMmGHInv14Ol7EvTTTx3DTazc9MRBaGGWG44Op_brZ1KU_etMuAVk0nY8pVzKoKmz-BTozZ-ZuTcjP-OVMMS7l6QfmgrS_KShdAD-J9riNFOvOMArzsceiXu-zup7OCqncZ_U74sOWmPFsmoCUBynueCGSR2_KN_I8A_DgklzM-GdGvkeNPXaP7LE6KYFNcS9vySDBcdU9HhKnrkbkxQiMCmgvJnSeBiyUzqcbLk9-nLM9eIkgJGK153wCnoZc_5frZzWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اندیشمند برجسته آمریکایی؛ این واقعا شگفت‌انگیز است، این یک تسلیم بی‌قیدوشرط بود/ایران به هر آنچه می‌خواست رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/661413" target="_blank">📅 14:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661412">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139b8a8525.mp4?token=TaecoO_u4-Q4vEqOOl-zXj7ZJtfKjbLahhUHj6_C-7QsZK1WfQxvSJFYTrPMpUaJv-DwjTDLQBC--K4UnC7YPxOSVHwBBBsVKje_TzeJO3URydee2d7JGW8WTnv3gUXZtxLwi_xxKAUEo_ZP7Jff3n5ngPy_EKZ8Dw1AaUSYkSl3uY2jArCis6_bpzjhr52sA_LYnxGf5dmt43bvOCm4YkB0njIknSvm0IBsTWJl42sV4NUumL5dbh2a3YZb_RF9qabWe_7p4ttlNRmcvOpoAYs-Qiw2Lkc2gU6JjzM9NTaCQGyQQdGtmf3920A6zaYDTDmqaGqg3BA8BjUQdRxU1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139b8a8525.mp4?token=TaecoO_u4-Q4vEqOOl-zXj7ZJtfKjbLahhUHj6_C-7QsZK1WfQxvSJFYTrPMpUaJv-DwjTDLQBC--K4UnC7YPxOSVHwBBBsVKje_TzeJO3URydee2d7JGW8WTnv3gUXZtxLwi_xxKAUEo_ZP7Jff3n5ngPy_EKZ8Dw1AaUSYkSl3uY2jArCis6_bpzjhr52sA_LYnxGf5dmt43bvOCm4YkB0njIknSvm0IBsTWJl42sV4NUumL5dbh2a3YZb_RF9qabWe_7p4ttlNRmcvOpoAYs-Qiw2Lkc2gU6JjzM9NTaCQGyQQdGtmf3920A6zaYDTDmqaGqg3BA8BjUQdRxU1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر معظم انقلاب: رئیس‌جمهور ایالات متحده بود که برای این یادداشت تفاهم التماس می‌کرد
🔹
ترامپ: بدون توافق ذخایر نفت تنها ۴ هفته دوام می‌آورد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/661412" target="_blank">📅 14:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661411">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wtm30eyedmAFUIYyaN8ZT_gKuZUnfplu3mzqnZxQUPG-aNnfEDbswKdklxAh57YWvo_gxEiu7EJo7ewyfyF4Pn6rmzAPT0gOV1yYiKSTdU30f1x1GZigehEhPOZIKkYx240PMuk-mUr8A5kXNiwJtDzpJ-I4HJiAbc0ilvIYqr3nIKbwF-m7zz2HwxjhYmUzWuzkUiSiDdpBgy3OgthAbr75TLk9B3xwUZk6sYp_SXHuwhxVVro8hpNH2XqVvyKp3XckdkehJbQmUg5mNYuUx8lmxzJwA5NpaAYxc07goGdGG_i8uVAnEHUa5j7aPnXD7k19Ycyf-SslMysIgMCB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: ما در جنگ خود علیه ایران چقدر خوب عمل کردیم، کشوری که از نظر نظامی کاملاً شکست خورد
🔹
دولت‌های اوباما و بایدن در قبال ایران ضعیف عمل کرده‌اند. با روی کار آمدن من، سیاست آمریکا در قبال ایران تغییر کرد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/661411" target="_blank">📅 14:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661410">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
حزب الله: در مقابل تلاش دشمن برای تصرف اراضی لبنان کوتاه نمی‌آییم
🔹
اتاق عملیات حزب الله لبنان با صدور بیانیه‌ای اعلام کرد که همزمان با پایبندی مقاومت اسلامی به آتش‌بس، در مقابله با هرگونه تلاش دشمن برای تصرف اراضی و گسترش اشغالگری کوتاهی نخواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/661410" target="_blank">📅 14:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661409">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
نیروی دریایی سپاه: اگر شناورها مسیر دریایی جنوب جزیرۀ لارک را رعایت نکنند، مسئولیت هر اتفاقی با خودشان است
🔹
از برخورد احتمالی با مین تا تصادف‌های دریایی و حتی هدف قرار گرفتن.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/661409" target="_blank">📅 14:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661408">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b36f5f37d.mp4?token=TeDqvbkmkdjVfD5g2jgj4EIaWEkk2gF0LG1VqLWXQTJykTaKG6WRTEQKDyNY1tYjvEFsS_y-PjMa_Ql4kbgNOqHtqJkWvotPKWzQIOi6yQ0NvmcUbjCSUNZ_6eYBZKISRviRD42A9yiqi9x8k5SpxQtC5PPdd-C87sPWiV4WqfU0kHo4RwPuGtdEkCFFJL-BD5Yz2cIwLS7m6lc1-R3ea3vYCVz4IB-xU1msEZ-G1f0pdmnNmRm2KKnGnJst-bRuZ8TngdvwXG6sDAVtCYQNBgQJLS8NlS6Z9aeRXEONSlXMN7BCAZ9FojMez3GE66Weev1Y2DHzo4v8O_DJFHFyJiJphBk4P1sxfydcY-qqMqw2EOFn0ep46ZgeU5qwoBB0tzbwfHMCr-idmhfn_tEZL96Vls4Aj-XvlJf2W2I2b_dg5CnDQynMZb89mtx9S1bfXWwWMSMEqv-kscI6nrLE8bd0CGH7044a0Lh6Q40tsfcsfzI3tjIwH1tXZkBFCSOp5rxTnaoEs8hKT3ZqLp7yhKr1w8fRP2Bn6mtmi3bnGWrSVK2XWzhJqr3DO-U52cPPAE-xM9X9EvNWV4Yc8sXSb8JlbmlkzxNaKRMu-T5D6zIYoTv6wd0JHkbYsPKWwek8M9jaqKiKC-hsG9QeQ9BLnLIuoZAIG5pfk3sI4AEfecA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b36f5f37d.mp4?token=TeDqvbkmkdjVfD5g2jgj4EIaWEkk2gF0LG1VqLWXQTJykTaKG6WRTEQKDyNY1tYjvEFsS_y-PjMa_Ql4kbgNOqHtqJkWvotPKWzQIOi6yQ0NvmcUbjCSUNZ_6eYBZKISRviRD42A9yiqi9x8k5SpxQtC5PPdd-C87sPWiV4WqfU0kHo4RwPuGtdEkCFFJL-BD5Yz2cIwLS7m6lc1-R3ea3vYCVz4IB-xU1msEZ-G1f0pdmnNmRm2KKnGnJst-bRuZ8TngdvwXG6sDAVtCYQNBgQJLS8NlS6Z9aeRXEONSlXMN7BCAZ9FojMez3GE66Weev1Y2DHzo4v8O_DJFHFyJiJphBk4P1sxfydcY-qqMqw2EOFn0ep46ZgeU5qwoBB0tzbwfHMCr-idmhfn_tEZL96Vls4Aj-XvlJf2W2I2b_dg5CnDQynMZb89mtx9S1bfXWwWMSMEqv-kscI6nrLE8bd0CGH7044a0Lh6Q40tsfcsfzI3tjIwH1tXZkBFCSOp5rxTnaoEs8hKT3ZqLp7yhKr1w8fRP2Bn6mtmi3bnGWrSVK2XWzhJqr3DO-U52cPPAE-xM9X9EvNWV4Yc8sXSb8JlbmlkzxNaKRMu-T5D6zIYoTv6wd0JHkbYsPKWwek8M9jaqKiKC-hsG9QeQ9BLnLIuoZAIG5pfk3sI4AEfecA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چیزی به نام آتش‌بس در لبنان وجود ندارد!
🔹
خبرنگار: شاهد یکی از شدیدترین حملات به منطقه نبطیه هستیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/661408" target="_blank">📅 14:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661405">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2029917f7.mp4?token=YBvVjryGQSuWxs8OScW5hZvaiV-etnpXqqQNd2a5qct0SbQqwB5JFNr_-_gWXW1l6e0IEj9HApD2e2YRfKEgEOPQWZsKYO-3eqCE9xu-u8SHwHsiplroD2rGKWOdXoRHmQ1R2QFK_wxEZ-pks-ZvvpGjIrwsF1odgKS0SbXfxDVt7jEAp_E3-wiFuF8AzWm4fIwlv7_bsU1wCGmQyVLSQFaNR81lJknJ5DSxUQuf5IEp7wDDh6GcrF8FczOP_KOQMGXqsq1zCaHFkluUzF71oHJ1C9k67ZU53yk6OylhDjYsYdrS9CBFxc8ZP7YQrG6s9nw8hS-F-l34T255EQ2y_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2029917f7.mp4?token=YBvVjryGQSuWxs8OScW5hZvaiV-etnpXqqQNd2a5qct0SbQqwB5JFNr_-_gWXW1l6e0IEj9HApD2e2YRfKEgEOPQWZsKYO-3eqCE9xu-u8SHwHsiplroD2rGKWOdXoRHmQ1R2QFK_wxEZ-pks-ZvvpGjIrwsF1odgKS0SbXfxDVt7jEAp_E3-wiFuF8AzWm4fIwlv7_bsU1wCGmQyVLSQFaNR81lJknJ5DSxUQuf5IEp7wDDh6GcrF8FczOP_KOQMGXqsq1zCaHFkluUzF71oHJ1C9k67ZU53yk6OylhDjYsYdrS9CBFxc8ZP7YQrG6s9nw8hS-F-l34T255EQ2y_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنایت در شهرک قناریت در جنوب لبنان
🔹
منابع لبنانی از حملات شدید و پیوسته به شهرک قناریت در جنوب این کشور خبر دادند که تا این لحظه به شهادت دست‌کم ۷ نفر و مجروح‌شدن ۱۷ تن دیگر منجر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/661405" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661404">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ابلاغ دستورالعمل فروش ارز اربعین؛ سهم هر زائر ۲۰۰ هزار دینار
🔹
بانک مرکزی دستورالعمل تأمین و فروش ارز زیارتی اربعین سال ۱۴۰۵ را ابلاغ کرد که بر اساس آن هر متقاضی بالای پنج سال می‌تواند تا سقف ۲۰۰ هزار دینار عراق دریافت کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/661404" target="_blank">📅 14:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661403">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a971dbe16.mp4?token=piBImmlDU4umo-YqcHAQjZYd6vKo-ZB9ucnr9VfZzkhwX-YWN39_LWWtX0B3p9bxDt8vRPD4BGjsjF1lwQw40Cp23lM9e5pkJnQwi1vOZYpNMpJdne2z_84RlbOISZ5KFaoFMGvM37getmMN9rTrGrtvzWxfMipoeSGMvh-GcO7MfI_cbjgkIT25DeNso6aVFzOGEtwkdgIKLIZItyvH5QGnGHQ1ZyTqR5xCnW1insOS5uWM0gaPBZJNiRZXZI2xzQ2Qd-XIKI8MBZibluUsdOJQZ5Llk8rg5AdKQmIf5oVPTorFTB3yiT1AFE0NGxEqEZwqXk3shZadrht7BqXckQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a971dbe16.mp4?token=piBImmlDU4umo-YqcHAQjZYd6vKo-ZB9ucnr9VfZzkhwX-YWN39_LWWtX0B3p9bxDt8vRPD4BGjsjF1lwQw40Cp23lM9e5pkJnQwi1vOZYpNMpJdne2z_84RlbOISZ5KFaoFMGvM37getmMN9rTrGrtvzWxfMipoeSGMvh-GcO7MfI_cbjgkIT25DeNso6aVFzOGEtwkdgIKLIZItyvH5QGnGHQ1ZyTqR5xCnW1insOS5uWM0gaPBZJNiRZXZI2xzQ2Qd-XIKI8MBZibluUsdOJQZ5Llk8rg5AdKQmIf5oVPTorFTB3yiT1AFE0NGxEqEZwqXk3shZadrht7BqXckQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت پرده لباس‌های یک‌شکل مدیرعامل انویدیا؛ سادگی به سبک میلیاردرها: هر روز مشکی می‌پوشم تا یک تصمیم کمتر بگیرم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/661403" target="_blank">📅 14:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661401">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U942zxZWRxOHHOtWHvJ7jGcd-cBWddVwNWA2Ktq3jtwVREvHHQhdXNGKSWey5_88tz8HaDn4phfiqGKDPyaA3-4D6fWtSZMbjVzabreUqE_vs9a4X5f8TlxcBn7nxpmyNFgNnjvyn66oQdO8IdZA-nbUzNJbjp9YfOboiRZh3aZ093tK01n8_T9LqUMfvqZk56G0oFeJ6F_-0QLbm-CHNluoBN82W2h2MAPwhQQZtoJmsfkHtXTEm3PbO3r144jzwheTvtXNLLCaF7LwzlVt-QZdEx3bUP-oImLrd9-v00uP9ZLAieGWyzYCsuDfMlxqfaMV4qtPJAgox49FP_5fdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰ درصد بازار پوشاک در اختیار کالای قاچاق
🔸
سالانه حدود ۲.۵ تا ۳ میلیارد دلار از بازار پوشاک کشور به کالای قاچاق اختصاص دارد.
🔸
برآوردها نشان می‌دهد سهم قاچاق در این بازار تا حدود ۳۰٪ کل مصرف است.
@amarfact</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/661401" target="_blank">📅 14:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661400">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d08bb1e1.mp4?token=I9XgkGQh-qXqV43q-b9apft94wX7ntGUBGtewtyKw5FNy49Vd2-6B00ArMpv3-OXfdpsGIlCypZfrGGPvYjr6JKqn4OEss1i-gPW-7yIN-edkJ5ImXU1jgyRJeOaR0QQruUJ30kQG31VjgYgDSRWma_YxvYEpMtcu7xxA0exH2OWtOlMhqXp5zBCDDCFEtV-kqjpMqkTLUIuh6pYLgx78KE_Ygkv2bLCHJKzVXYBnAPLqbpp9nZq2d4a5kkHtmoezxoCXTRqk5NkVNqdYszL5CdVt4SlZ_sUQ5oR5LUeiitvWlihe63pZza3v13Y9LA8OokLe0084Hg2GEySewWxIpgmL_R9JQpiTcO2qScN_GkIzj_V0fnhYInMB0LU-CX3jls95RpwPxY4P50jHsmE1b1dOEgrkT0DmSf8jkWXrc9TraxVDheFI3wAZ1jQYKktCZxzYFiKRJ5zdHUaLF1AJyXferv8rBOM9VwFIJity0BM0WPDTx8AGsKiMT085SAauA_2ztrOvXiYJwtJlbJO8NgOk4zniAJJEvuA5VqJGaZHqiNfn84aq8NaMx_8B8sZ_BOFklTdVq9uNlRTSywkCk1B8xA9Z311WmXNFh-NXI0M5ErCu0uGqjjv8KWiXMY2287gpud1FL2aMiThTeZMIaWyia1b5o4y8pKsU4_5pWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d08bb1e1.mp4?token=I9XgkGQh-qXqV43q-b9apft94wX7ntGUBGtewtyKw5FNy49Vd2-6B00ArMpv3-OXfdpsGIlCypZfrGGPvYjr6JKqn4OEss1i-gPW-7yIN-edkJ5ImXU1jgyRJeOaR0QQruUJ30kQG31VjgYgDSRWma_YxvYEpMtcu7xxA0exH2OWtOlMhqXp5zBCDDCFEtV-kqjpMqkTLUIuh6pYLgx78KE_Ygkv2bLCHJKzVXYBnAPLqbpp9nZq2d4a5kkHtmoezxoCXTRqk5NkVNqdYszL5CdVt4SlZ_sUQ5oR5LUeiitvWlihe63pZza3v13Y9LA8OokLe0084Hg2GEySewWxIpgmL_R9JQpiTcO2qScN_GkIzj_V0fnhYInMB0LU-CX3jls95RpwPxY4P50jHsmE1b1dOEgrkT0DmSf8jkWXrc9TraxVDheFI3wAZ1jQYKktCZxzYFiKRJ5zdHUaLF1AJyXferv8rBOM9VwFIJity0BM0WPDTx8AGsKiMT085SAauA_2ztrOvXiYJwtJlbJO8NgOk4zniAJJEvuA5VqJGaZHqiNfn84aq8NaMx_8B8sZ_BOFklTdVq9uNlRTSywkCk1B8xA9Z311WmXNFh-NXI0M5ErCu0uGqjjv8KWiXMY2287gpud1FL2aMiThTeZMIaWyia1b5o4y8pKsU4_5pWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت نوزدهم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم اعظم فکریان که در قالی‌بافی مشغول به کار بودند و یک روز به دلیل بی احترامی فرزندشان دلشکسته شده و اقدام به خودکشی می‌کنند و روح از بدن جدا و به عالم برزخ سفر کرده و تشنگی مفرط و عذاب‌آوری را درک می‌کنند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: اعظم فکریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/661400" target="_blank">📅 14:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661398">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71bb3ee9dd.mp4?token=mLt8Xazrjd_iS8sRu5vevcEkMXKZECHp1BqoAbkXtfOgS5M0Kj82VN_3nalzciJMPo6Lz3NmTCUJvgGlsVscNvEwkVI8G0MzVZB8rTJx_OqFU6I8sCB0SpXn4OKpZ2PxPNNYeVlwOKRtx7GDwzPX5caVTHiLx0018oWBXHvD7039vqilfWbFTpSPXL9N4ASRHZqqMm0ej0T3rXD6VN2YPZ4kCx5yQxlQcE3et2BgpVbwSlhkSb9fcxMT6XSjwCH8yd4ib0HEvNZktAj9DAIZyRo5eUlSYjV4D8l1gk2S3pyW4ZMWQuMXXT2jLGwWoITv1_AIRGfo4T3zRKzYCd1umg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71bb3ee9dd.mp4?token=mLt8Xazrjd_iS8sRu5vevcEkMXKZECHp1BqoAbkXtfOgS5M0Kj82VN_3nalzciJMPo6Lz3NmTCUJvgGlsVscNvEwkVI8G0MzVZB8rTJx_OqFU6I8sCB0SpXn4OKpZ2PxPNNYeVlwOKRtx7GDwzPX5caVTHiLx0018oWBXHvD7039vqilfWbFTpSPXL9N4ASRHZqqMm0ej0T3rXD6VN2YPZ4kCx5yQxlQcE3et2BgpVbwSlhkSb9fcxMT6XSjwCH8yd4ib0HEvNZktAj9DAIZyRo5eUlSYjV4D8l1gk2S3pyW4ZMWQuMXXT2jLGwWoITv1_AIRGfo4T3zRKzYCd1umg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تماشای بازی ترکیه در آمفی‌تئاتر باستانی کاش
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/661398" target="_blank">📅 14:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661397">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJIThEQ4EU0-ZD5LXZfbWrq8vRu5eGnoWb2VQCW6cdEoBqzduPDsR47XrVhLDDvzfga1n4codpeX9d8-UbFBHmnYyHinu9E0lTBW4sHKH7zeAmS-CpLov_Uryr1hLFmJCZgJaPO5h7E-qyaYCMLzUeMOxMUmRoxspuAP49kaA2Iu9dgqBAvuNkboV_mVgcVJfsCXrDetYu6Wn8DfpW9zOVGKcH94f8T1MUDdpRtNi8Ai_mjIr_pGcHJDoSSpYiXdIl5pH5WtBm07VvCcPjSXBFQqiwL_UMzZ3Krcxrg-LPcfAyogWJmWGQs_MfLNLD4AEHd5271R6iKH5_P_rDxY3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«قرار بازداشت» رو زیاد شنیدیم، ولی دقیقاً یعنی چی؟ #واژه_کاوی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/661397" target="_blank">📅 14:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661396">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291962135c.mp4?token=Jzm22rC9fHZkzFF6oh3_3-J3cqQMflnxsBuwqMtWsBqDBVvQ1T2ax8WdHJ3OAhYvU6md2OcaW4V4sZfWBRwlZI0X4XxGbjXXLUZgwy1aEAP9RiEXTj2mmP4wBRlpt8KWCXoPdxaNbSBnj112_C-9AdYbTbnI-XN62RHztPT-MemG7BH7vuyEDaxWyFhKM2RYiNLBX9pSS0qEFdI2hw64eSZb0n39WN-Ss9Jpr9Ah4JjpIfNm3PCAPESj8ztoi4YBPjVgAQ5Pc59LAyi-H4cHmL2X2sirOug4DBLVvexVFyxIulF_4lfsmKAM02DHQa9SEIBkNjF_zY32NIdYkuQcfR40BUve2o3YiAxXptcvvibqbAVhwwiRSA3Rog_XiYXgySxz5PTbTbqRRW-WT6S5p8Wz3wtmRWUq7BFH4m_pCAN86BexL5-tVetT6XjHs2rPxyuVGjS9hMFgxUiLRE58HMu8qCo4O-pLJI6ZI_luf-CfP0JplRBeehqLr3PmunUScDvfEufqslK4q5e84WNVBGC9yL5D5glGeElsibYQskVtlQffBYE6ey1nv65c0O-k2RVnR4BK8zRbH8vPj6rD83i5He1eiDwJMtM6Pw-bw8dK5C86RJXwvnRIrURppyAc2A_48Hz_-71zizLlDoN88cxmizF37J_J_0OJW_fP8ac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291962135c.mp4?token=Jzm22rC9fHZkzFF6oh3_3-J3cqQMflnxsBuwqMtWsBqDBVvQ1T2ax8WdHJ3OAhYvU6md2OcaW4V4sZfWBRwlZI0X4XxGbjXXLUZgwy1aEAP9RiEXTj2mmP4wBRlpt8KWCXoPdxaNbSBnj112_C-9AdYbTbnI-XN62RHztPT-MemG7BH7vuyEDaxWyFhKM2RYiNLBX9pSS0qEFdI2hw64eSZb0n39WN-Ss9Jpr9Ah4JjpIfNm3PCAPESj8ztoi4YBPjVgAQ5Pc59LAyi-H4cHmL2X2sirOug4DBLVvexVFyxIulF_4lfsmKAM02DHQa9SEIBkNjF_zY32NIdYkuQcfR40BUve2o3YiAxXptcvvibqbAVhwwiRSA3Rog_XiYXgySxz5PTbTbqRRW-WT6S5p8Wz3wtmRWUq7BFH4m_pCAN86BexL5-tVetT6XjHs2rPxyuVGjS9hMFgxUiLRE58HMu8qCo4O-pLJI6ZI_luf-CfP0JplRBeehqLr3PmunUScDvfEufqslK4q5e84WNVBGC9yL5D5glGeElsibYQskVtlQffBYE6ey1nv65c0O-k2RVnR4BK8zRbH8vPj6rD83i5He1eiDwJMtM6Pw-bw8dK5C86RJXwvnRIrURppyAc2A_48Hz_-71zizLlDoN88cxmizF37J_J_0OJW_fP8ac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نبویان جزئیات جدید درباره نامه‌های رهبری ارائه کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/661396" target="_blank">📅 13:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661395">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
وزیر کشور پاکستان وارد مشهد شد
🔹
پیش از ظهر شنبه هواپیمای حامل وزیر کشور پاکستان که به منظور دیدار با مقامات جمهوری اسلامی به کشورمان سفر کرده است، در مشهد به زمین نشست.  #اخبار_مشهد در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/661395" target="_blank">📅 13:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661394">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab51b559a8.mp4?token=bzpy39wPkhuKOKAKoO5S1TYV__tf2MVYY-uizJNec-YpluGNtTW-gDwbYES0yI2qFvWvAgHrGaGLSzynW-hvoFHOWtDrj86sGXRE2MWPRlhoJbazs3RUWY8man8oJTgbXKOWvz4PYQQ1XfqBXpJxtQp0l2leNg0sJ7-ZXPZktYW1A6vl9wwONVMMthQq4JdMHOKq3dzY2QkAIU0l0ChX4AmgJXA7wThWD8ANsg7c8q_0b6xFZSOi_qzk3gFfX7_dWAscV0LOz95LA9-5rYospxpXMjDPuLzDGv4fw_Bt-xFtspi4696J3mic03EKjutTWLYXSqgdHF69BSj5Opm1LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab51b559a8.mp4?token=bzpy39wPkhuKOKAKoO5S1TYV__tf2MVYY-uizJNec-YpluGNtTW-gDwbYES0yI2qFvWvAgHrGaGLSzynW-hvoFHOWtDrj86sGXRE2MWPRlhoJbazs3RUWY8man8oJTgbXKOWvz4PYQQ1XfqBXpJxtQp0l2leNg0sJ7-ZXPZktYW1A6vl9wwONVMMthQq4JdMHOKq3dzY2QkAIU0l0ChX4AmgJXA7wThWD8ANsg7c8q_0b6xFZSOi_qzk3gFfX7_dWAscV0LOz95LA9-5rYospxpXMjDPuLzDGv4fw_Bt-xFtspi4696J3mic03EKjutTWLYXSqgdHF69BSj5Opm1LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزارت اطلاعات از شناسایی و دستگیری سه تن از لیدرهای میدانی و ۱۴ نفر از مزدوران شبکه خرابکاری خیابانی دشمن آمریکایی-صهیونیستی در استان ایلام
خبر داد
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/661394" target="_blank">📅 13:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661392">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e1db5f80.mp4?token=PtsIvCv3ooSIHfx2Zwln1RbnCl8sHkHSEVTh4YHhNAg76QoLqqOZ0AW9q691neSjm7L68pL2zX2NH8Ak8panolVrIPSmqPkTz3eSdQUWh0ouS-ebp__uX32E5JkQab7ejrmDIDeaXIMUXTJE4dGrjnXNxq-dxrZmyMg0c-wbbN9UHnT_RBvzouuEEloXyVcJauFM71PGl936PKg-vmU_xjSnawcQofNLe7xZY_O3WcEIQry0ZaQjm0V0jW5lNtcxiXUkI1-sNy3jT7Jw9WYOh5_bG4JTwkI-vDzYktLGoMG6BEAdgCdWoV6CFTl2zdK2lpzIspML4T3MgUuiqC1fYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e1db5f80.mp4?token=PtsIvCv3ooSIHfx2Zwln1RbnCl8sHkHSEVTh4YHhNAg76QoLqqOZ0AW9q691neSjm7L68pL2zX2NH8Ak8panolVrIPSmqPkTz3eSdQUWh0ouS-ebp__uX32E5JkQab7ejrmDIDeaXIMUXTJE4dGrjnXNxq-dxrZmyMg0c-wbbN9UHnT_RBvzouuEEloXyVcJauFM71PGl936PKg-vmU_xjSnawcQofNLe7xZY_O3WcEIQry0ZaQjm0V0jW5lNtcxiXUkI1-sNy3jT7Jw9WYOh5_bG4JTwkI-vDzYktLGoMG6BEAdgCdWoV6CFTl2zdK2lpzIspML4T3MgUuiqC1fYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل در ووهان چین
🔹
به دنبال جاری شدن سیل در ووهان چین، حمل و نقل در شهر مختل شده و خودروها در خیابان‌های آبگرفته، شناور شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/661392" target="_blank">📅 13:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661391">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مشمولان اعزامی تیرماه ۱۴۰۵ برای دریافت برگ محل مراجعه و معرفی‌نامه به دفاتر پلیس+۱۰ مراجعه کنند.
🔹
هلاکت یک نظامی دیگر رژیم صهیونیستی در جنوب لبنان
🔹
یک شهید و ۸ زخمی در حمله هوایی اسرائیل به منطقه صیدا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/661391" target="_blank">📅 13:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661390">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpcMQ28Lo5ETFKaZKzNCAkzQ-Fx1DezVcpm5h0bI8r1K8W8J3FBVHy1rX72Cb6VQDhZet7jOBbGg1pAgBmQS8BbQCZb46VHV009wodKjEqRLuaLILXoTNCmRgWRJnOh9bHnM9K2hkUDqRwtHHYZ3bq7_79QiCKbc1c2emSvOriilALAZD_HPJKqymNxxuX9MMsXTQrqjHwHDwc6NUSTus0vde-NWDcAtUNo8IkYs2hgzMsJxn5u2AT7hcY74hfhR84VhfvHbpaEIMdpI2Udlqr8Gj5XUl4CaXh8qCWX2A9KMsEW0_LjCKlwiTWLxk1fZQ5lXwjmhcoAu4TZKlyF6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت کاربر آمریکایی درباره مادورو و نتانیاهو: یکی این تناقض رو برام توضیح بده
کاربر آمریکایی:
🔹
ما مادورو را براساس یک حکمِ بازداشت دستگیر کردیم، اما نتانیاهو که در ۱۲۴ کشور تحت تعقیبه، شش بار به کاخ سفید دعوت شده؟ یکی این تناقض رو برام توضیح بده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/661390" target="_blank">📅 13:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661389">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
حمایت خواننده لس‌آنجلسی از ایران و تیم ملی
🔹
گورگن زرگریان خواننده لس آنجلسی که در حمایت از تیم ملی فوتبال تا تیخوانا آمده، برای ایران و تیم ملی کشورمان آرزوی موفقیت کرد.
🔹
گفتنی است، او خواننده‌ای است که پیش از این از مواضع قیصر انتقاد می‌کرد!
خبرهای لحظه به لحظه جام جهانی را اینجل کلیک کنید
👇
https://www.khabarfoori.com/worldcup</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/661389" target="_blank">📅 13:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661388">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENMIvHaRTIjf6YjcjLkRhHIbBczE5TvlBh3dOXcmvV1ukkBYRDs4pgrkQ2pmggux1SzlXr9dChHdqtrNIBxIfEEZE7bf34xZFfsaJ6sFi8g04bB_XZHIu22SvwOdTKaLJrcREVOBFmdXVECevs13luT4BsacX4kPVQDuOGjNaLaQex7qke8qmLc-YJBrmCNdMLjjjGaehN0NPgQVJF2eZrq6liBAq5w0egSQPLkBcPs4_eMI3DvtIuzMS05JofEGCt2v-o_ptkdaYTmz1NxIFEGY94793IBOS0C8AdnTwHy4bdGdWZRRyQoq1GJJjFRO1CcO50_ppYBEafIzqO254Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب هولناک جنایت میناب، برندۀ جایزۀ بهترین عکس سال جهان شد
🔹
مرتضی آخوندی، عکاس ایرانی، به خاطر تصویر هوایی تحسین‌شده‌اش از مراسم تشییع جنازه باشکوه ۱۶۸ دانش‌آموز شهید در میناب، مقام اول جوایز معتبر گلدن شات ۲۰۲۶ را از آن خود کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/661388" target="_blank">📅 13:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661387">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
واشنگتن پست به نقل از یک مقام پاکستانی: اسلام آباد با تهران و واشنگتن در تماس است و با جدیت برای رفع موانع تلاش می کند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/661387" target="_blank">📅 13:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661384">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
واشنگتن پست به نقل از یک مقام پاکستانی: اسلام آباد با تهران و واشنگتن در تماس است و با جدیت برای رفع موانع تلاش می کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/661384" target="_blank">📅 13:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661383">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای ارتش اسرائیل در حال بمباران جنوب لبنان
:
اگر حزب الله از نقض توافقات و انجام عملیات خصمانه دست بردارد، ثبات برای هر دو طرف ممکن خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/661383" target="_blank">📅 13:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661382">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from️لوازم خانگی بهشت بانه️(admin)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qh7HqxNQGOn5QY7xDQlervCdcAGLMx4lsBBwVF-3GZMzrkw26Pw1iihKUjI5vlNHQ6pT8UNyd0yAS6Or-J3qx0Qh6GqlzEIPeUC29HjK2Yj8zzi-IQUw74kiWGM117slF8aNrB_x4qiT6DBnG07GnPsHK-RV8YSLFct8TcwiFMn5diw7gRn6d-wskwfaYGuAN1-9flJoLtDREdcOvhTbYELKNdAgI0pouc23B2W-N9RZZynhckV6giQ0yJaqNXIWG44Oz4zdymD70JmwyYqF8tP6C2sj1lEJSX2CQs8OFMWvtQLJcOTMHm_4pCJMSX-fgpkfVMH81Vx3CfN6I2efVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش اجناس با نرخ دلار150.000
💵
✅
فروشگاه  بهشت بانه سلیمانیه عراق
✅
لوازم خانگی عمده برندهای معتبر
✅
الجی کره
✅
بوش المان
✅
سامسونگ
✅
تحویل درب منزل باگارانتی شرکتی
✅
تسویه درب منزل
✅
لینک ورود به کانال تلگرامی فروشگاه
👇
📱
https://t.me/beheshtbaneh2021
📱
https://t.me/beheshtbaneh2021
✅
مشاوره کامل خرید تلفنی خانم ها فلاحی
👇
😮
😬
09188806440
🥳
😬
09182643758
✅
مشاوره حرفه ای در پی وی
👇
👇
✅
@banehonline2025
✅
@ORGINAL3758</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/661382" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661381">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiliHeGd1JZMG4e95eBA_Kz3Ont4Fahq-BfmKHYKSqGV7IVoNBmc4fgXBbXXRRsaWVes9QCTWb5F3s9D1rRfR2CpSk8UBmDLYLY31r571f0m8MZT_v96vcywg8tQaX86DbIEWLyLAdllczgu89F9mbPGjhBbUI8wrV_bZ2HbZOWUXqQ2QcjMkEPPl8EV8KhYWkQcIrZa16qtB3GVb88qDRmwqrCbKkEUbSbmCvdE8CXZZJPBzhpFZu787UjOF0m9jWkOtwGOeGQ_fn-mmxO-aXdv_cDzglfezspdCnoGf1fvthD_7bVvZHYFpE64ObLtjEApIwa4Zj4pKa4KePGXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس روز ناسا
🔹
ناسا در بخش «عکس روز نجومی» خود تصویری خیره‌کننده از پدیده اختفای سیاره زهره توسط ماه منتشر کرده است؛ رویدادی آسمانی که در آن زهره برای مدتی پشت قرص ماه پنهان شد و سپس از لبه روشن آن دوباره ظاهر شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/661381" target="_blank">📅 12:57 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
