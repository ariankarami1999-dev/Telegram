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
<img src="https://cdn4.telesco.pe/file/ByJo-9dl89Khdp4gk2KH5hMFuiT452PcrZi90zHfIs75IwHbZB6rYJgkT6DzNhuVUQoDv832gkclwpTzaX_cysIlIBR8AIPACTNcGXlJybR-IsGuR3Xe3ti0whTYux6uUjSzM_lIfb5wacgCk1lC7CbfBBSBG1aIXU4iPCbFZg9mwI3QifZAYkNM20cAViU1OOjuFS_VXvdHPPtJ0leyyzOWpPPBNcDr3DCxXfqRpYqcgJPFWZBhRBgnVBgF3RyNVTuOt9jCPuheSRZJeM3isMkzZeklhwwGCjVg5NVQfu2iuTiS-3XFjc08PfKdr-V7Cpv8labVVcMU1yaJz1p-Xg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 245K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 19:46:32</div>
<hr>

<div class="tg-post" id="msg-23450">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGlXIDj9e2ls1zwsFITN_AJ0JF4ywLtEDemxFakQ3V7pJle6R0D7ZvhU1nJWIl94TBiI9GOFOtY2VbOXTdhWN12_clzlsgc91o87NcSyI4b3BwJ7TkAkigQHWkHcd-veLXTc7Wn-muTM5XDV98ZX2WAlYBu_OF4oyHQFatLDzudtwiZFeNDXfPO-7btCYPRUVZo_XkjdaNcxdxRohACwoQhKK8v-0ta0GIcV1nAdDMiKi_ymSnUlFTGuu0zpCTqaKQlfwaQoSj5fCFAJv7U3MvKo_TWFNNkX_vwlGOmZI0Z4OLcFkxmU1iH97vOCTLcajRVZCxlzzA3o-XRHLaBbag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/persiana_Soccer/23450" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23448">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=g_rV7nU8NVUImbhZPrisGP_3mv9Yh2SI-31bBRjK5j5h0NLMzqb1nU7XxsjqPJahhquLWbzDFxG6wjJKqp0NnH7mSs3mhla0O0R04ZfknoupMCky5edbw522E967VFBG6KHtxXL3khdlKliFFFqpJgeK7JhUrLe1MF-Cbi7mN6QTW72FdUIJWQA6kGvZweO239rOy1pbejNjXI_0qjnR-K45xOZKlpzqNX3PtlqFt1ZT13fXCJfCQ8jluT8cTEKQyHezPM5GC88zhObxMPCkhYnTjdPJLR5ErHNGXeF1Ony4OHC5Y2e-aEbUxrQrV8SMSNMS-0Ktkrl2lxfQCQ_vTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=g_rV7nU8NVUImbhZPrisGP_3mv9Yh2SI-31bBRjK5j5h0NLMzqb1nU7XxsjqPJahhquLWbzDFxG6wjJKqp0NnH7mSs3mhla0O0R04ZfknoupMCky5edbw522E967VFBG6KHtxXL3khdlKliFFFqpJgeK7JhUrLe1MF-Cbi7mN6QTW72FdUIJWQA6kGvZweO239rOy1pbejNjXI_0qjnR-K45xOZKlpzqNX3PtlqFt1ZT13fXCJfCQ8jluT8cTEKQyHezPM5GC88zhObxMPCkhYnTjdPJLR5ErHNGXeF1Ony4OHC5Y2e-aEbUxrQrV8SMSNMS-0Ktkrl2lxfQCQ_vTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/23448" target="_blank">📅 18:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23447">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntHa3ebWQVu7GrGUbZJqjto5ZQW6X0I-bcMozzb7dyn6RsN4bT8qy0QywiiIdLnpte7HRJpjrK79LcdQiKydwTWhKnKCmXvHHxFu_VSKgd_ii4A9AKFVcTovIR1kvgkiEpmMdji6PQgZVmowuHWE4q9uu8OtRb3yWcMtWQ_BxNUJKF1r7sASMLAWFjnDhk2iq9sLgpSc7WurgnsFvSs6m8Jt2YE7DOOwyJkCjv6ztVezLVwEi-m5AcP6XgLE8YM_SlfSAMRSe4w4z7PP6zfxufDG3VY5uqn6dRUb4g4_x9jZgFt-Nukz_Fci-4SDN7dIv7GSMo1magP33RzJU8UUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/23447" target="_blank">📅 18:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23446">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔵
👤
هایلایتی‌کامل‌از عملکرد درخشان محمد جواد حسین نژاد درفصل‌گذشته‌رقابت‌های‌لیگ برتر روسیه؛ قطعا‌بازگشت محمدجواد حسین نژاد به لیگ‌برتر یکی از بزرگ‌‌ترین بمب‌های تاریخ فوتبال ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/23446" target="_blank">📅 18:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23445">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOpuwLucMeGfM7UnAebsBeWSs5w-fDOxkC0e8hVGCCXvfQCrshlLiuUWTXwoqCnJm2Kx5dL_DjjmbEp85Pxs_qKDtAcd3IyxWfjqf0m3QzBS6OJ9COZ3ESPFDFkv4HNXVKoZZYfCSICKcMOh5RgEf-Y6h_6J2LGSyqKU2b2X5s8Ag0S325CbenrbkJA7IsfQK9b7WbqMKxh3ZfQVKkoxjNWSPK353kGUu4jYzhJvHKSetBOCqXYTaU6F4Eu06ViVU0XGXXX9Btq1uRbwy1SONJYOh2ZfiHTDWtZyLzKy6Qb8W2qnwDqphS53paPlE9or16vKgwWMJ__hymbTuvmySg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ ایران میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/23445" target="_blank">📅 18:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23444">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFTV14vMzcjpl2tfzV54lzj8oNLV-KxGWGJvErTdorhdGssfxraDZifcPmlonJ24vzYcGqSXN671YqcjQUCpzU-6E53HVd-U9VN6RPY4mMgDLpwUpMOzfP13vL_JsXIiSrLz6icqUZfehUAZHkE91KwLB_wHjnZ7SYiOznkBPuQWM3VdgAR8Ydzhavfm-G1mGqDnoja9AQ7NBl_lvbkHZUxjmqzYB4ODkqrFeGnJPWblrmZ78fvEtlt_bLAejAAIvZ_8csl9wHBlvIEHHgDaIVJe6jvRpzPDm-ruMjQ4vpHYFjvOYwlfp6hqC3vTktsCYNP7tZHIkT2w5S0zQsrEFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت اوپتا پیش‌از دیدار ایران و نیوزیلند، شانس پیروزی‌شاگردان‌قلعه‌نویی را ۵۳.۸ درصد اعلام‌کرد. در این آنالیز احتمال برد نیوزیلند ۲۰.۴ درصد اعلام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/23444" target="_blank">📅 17:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23443">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=CHC-jvhmpGfhImjviKe9LSgh7jX8aYORPLFwzEpf_88OZD5w9Rg6bKoapQi0KE1jXXXqja_vP-3jKH8-rXAsUxkOxd1sLqv5IM7XJZROMwwQusB-Y2cHBZVexMMbqweSZtz85qoG1zdjwnivDobPpr-VTUEZuNVZmqURHYZ-bRxNQSP-HMXJlQ7FLupDQN4Jr993Jz6F_aaBhd4Y-IxjyZtCzQFS3KB2YcFsMbsVy30sheRN-y4z2skQ3s3fc27np7D8LgtbgN-zfzNSiz7QL3deHfFcTv1bRL3PTy7FG7lXHRid7VvdwXuaXkjFJvYfpvSqbjciFoHdJoDqqkJMjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=CHC-jvhmpGfhImjviKe9LSgh7jX8aYORPLFwzEpf_88OZD5w9Rg6bKoapQi0KE1jXXXqja_vP-3jKH8-rXAsUxkOxd1sLqv5IM7XJZROMwwQusB-Y2cHBZVexMMbqweSZtz85qoG1zdjwnivDobPpr-VTUEZuNVZmqURHYZ-bRxNQSP-HMXJlQ7FLupDQN4Jr993Jz6F_aaBhd4Y-IxjyZtCzQFS3KB2YcFsMbsVy30sheRN-y4z2skQ3s3fc27np7D8LgtbgN-zfzNSiz7QL3deHfFcTv1bRL3PTy7FG7lXHRid7VvdwXuaXkjFJvYfpvSqbjciFoHdJoDqqkJMjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برخی از حواشی مثبت هیجده و جنجالی رقابت های جام جهانی 2026 آمریکا از زبان ابوطالب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/23443" target="_blank">📅 17:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23442">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1q5_tkr583yZlcmGNxW5hMW-71q1vvHhWsMjZf6RHv6Co9Hv8RSO0NlUUjUJ3_cogtu5vl-hhK6wCuJJEMV5JCOlTOUw3omxFEgZCCssiq8Y9S8VdW83S0cXfoxndHc9snljmeC_kjwCj4mWv0OSxVPi_FG80CS2BffoyBHH6DIN6pTltFlGmZi2LIIKKLsy8TA37bM463_R9juhASGriqAPepzWqNbV57As0H1KIKKftgqzyGoxwrU7TiLGxbSBOoBjC__irxFPv0XNDRottOZrWfErnvXLOJ-BoFEC_YfNvH-vP54E8A0JLKLRIMmVnhn2OLkk7KvIcIklEQjnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
صندوق‌سرمایه‌گذاری قطر اعلام‌کرده که بوعلام خوخی پس‌از گلزنی‌مقابل سوئیس در جام جهانی 3 میلیون‌دلار و جدیدترین‌رولز رویس فانتوم به ارزش 550.000 هزار دلار رو دریافت خواهد کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/23442" target="_blank">📅 16:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23441">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHcHKWeys1V4YFOenaLFIOe5PFhKWBJMXlbAJN34TlzQvbgmUQiWjBGcq7A1zYvD6iePEV1hpyvq9bQ4d66o3yfpbHT6C6Hy82bWIjIdGV7cZ6MKtQhnbgAqHfD7elEETE1fxj1i-WrobG8jzInr-_uE1UNiPE2apP4UqTsXHkLtCxVGYnbWjTJ7HInXfqR-_5Be7zof8kTocceOWkzqr9cwXneliOgfce8TMq30wQy5_m4K0csYaYZXN85WFxQ801YYlzAWqRO9UWlpyhQ8xK5hk1mRjh5oWlPn05g4nLfWr8W5gbP5pEMCReDW95v0Wrhdw7_iRxwiTU_xVUuDEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی قطر
🆚
سوئیس در هفته نخست رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/23441" target="_blank">📅 16:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23440">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ6VTCl2qm61B9Pt6lkcg7Xjq85KGLOAArL6hVwicLhdI90jgJT03f88h8CuHqazQLWXY-7qWH_ZdW98zifQbyDFqVSZzevFehErfCXfMp36TDCnDKsdJTF4rFDEdYvObkSYiLhyTTx6QO23s6hqhpiw2cpigj1pVDfRTHk3xt-hbtDp6MtEIig1os28HB2ftpRY7SFaE8C7PAfRK-CtzqWR4wbgdUAqFgZJiGdKB-vqPuuVjCnjcN9IjmWRaG7Mp9lGfFIJ_QG4h_gmx0HldI6-w-RtPk7Iyu7BeIv2tJeCjtV9OV5gTJTgZn6xcXRMZrTH72lSDmsTX7Z_0epqew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شبکه‌های‌رایگان‌که‌مسابقات لیگ ملت‌های والیبال رو باکیفیت‌بسیار بالا پخش میکنند. امروز حدود یک ساعت دیگ تیم ایران مقابل بلژیک بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/23440" target="_blank">📅 16:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23439">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOBrNbH-sTkwz6UDrgr7cBaJWiAs1gF-o20xt_Y9I9ha9uo0KFC03iDQFwmiUwgPGjwzpu7eE-qnGQOl8rrflw8ONYm55oRl9QrEFoees-xVA0QMh76NlMBmVr8aCZnHm397Ht8QypZiusfwXwVbuEVA26o76HPOHgrKDqgqMVGSmCgCxAtIuG1CCCFyeiB1-d6qsDXgO3O4IaF2OGrpLkSUwMhMev6TRZsiYrZvNCgTvqIXp4JOyHM3lK0y7Cxk6LSPFJvv4HthBayv6SWvLfAuxqD3up_C_99ocjr0jtNkyF-ld0zLRFohnKJDEGqqoeTM44XWnk1CPYpZ2iiloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/23439" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23438">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuxwslTgB-n7HFkFnf90Gf-Isc4LPl45EppHHcMlYO5H80l0XDve0kysmem_pw0eubyXUT3CWuEScx9H0_s3SgzRCWIl3G-NdPZ4sy2NrtwPtbaHZDIpdZDyShaOPhTqG8C_su61MbxsPXXVPHQRsXT9z90fkSwQbpWg04ILF0burALy6z9f8BM7yGLKRAnqY080cxvREV5xzWVqIsrEAcALaT3plvmzwiejqPH6gibrUaHkYIC3iyC5EL_LYGNxDOtycaDXnk4wRQlJbyN_rk1gum_3_PWXcNQAo9SNHpUZ4-sW01qlp31UKg5v-P73FqUCYLthPiCxxx2aXjJ4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/23438" target="_blank">📅 15:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23437">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">▶️
قسمت‌‌‌سوم‌ویژه‌برنامه‌‌فان‌ جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید. شیت و محمد نصرتی مهمونای این قسمت بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23437" target="_blank">📅 14:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23436">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=c20C6Jxr-RSf0TLnzEI0rN3nX2vTHfbdnaYM47gHo4xLq-D5ERUdj_Z5ftLjNUnnfctSStzklYAAccaLjOvJiOK0Ck_BYDOmloYmv-mvyImMwJwmusEdyEzTNLgzQP4xjFpWvpHTEJtI3UDiVgfDbBzCjtQJRxMWngnlaBD62M7UEHhAOrWyCIP6MwYxc8eh95riKCKDp9GqOj8fgRy5MZsAt1RS8X6PCKIX1nzISAnPZbHhm9VpgNIuICEPBYy8quYXIuJQI4VUgNzUsWSKq22SHO7XJaNqzglpuo88wAGCTNj9v6Ekn1W_Yh1KyTyX8Whu0yMSEDs6Pd2U7VRwmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=c20C6Jxr-RSf0TLnzEI0rN3nX2vTHfbdnaYM47gHo4xLq-D5ERUdj_Z5ftLjNUnnfctSStzklYAAccaLjOvJiOK0Ck_BYDOmloYmv-mvyImMwJwmusEdyEzTNLgzQP4xjFpWvpHTEJtI3UDiVgfDbBzCjtQJRxMWngnlaBD62M7UEHhAOrWyCIP6MwYxc8eh95riKCKDp9GqOj8fgRy5MZsAt1RS8X6PCKIX1nzISAnPZbHhm9VpgNIuICEPBYy8quYXIuJQI4VUgNzUsWSKq22SHO7XJaNqzglpuo88wAGCTNj9v6Ekn1W_Yh1KyTyX8Whu0yMSEDs6Pd2U7VRwmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
وکیل تتلو گفته‌تتلو واسه‌ماه‌محرم درخواست مرخصی کرده که بیاد داخل هیئت‌ها نوحه بخونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23436" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23435">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=Gde4QN2ciQhgqruk2pDDu6xCIV3QjiIqzjaU52qb-wgdvea0vutjaTYzBkPX4V9TZoaKcaIEUC91ZwfBtycQEHuCew1ziNUA2gIgOy-3zRsCWu0Fy8VT8YkUBZlzZV5QpVIN5wD-a0qiIEFhIOh-GqRL1EK92bbeyW-UrnsaYAWYceAsqlTsSSkHJlFnjxeG5BPOChCn7bpmZWfaFHbq9aFCnWm8gfMIRng6zdAnb1QpKmrsIC8w01yC0rY34VClsR3blkxYK2xaSUJ1z9cULQs-RForVxJRuPZByo-LMAn2OpoL6rwDA_psWTZ_Y_3Up9NMrps76y6MHg6rCqalqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=Gde4QN2ciQhgqruk2pDDu6xCIV3QjiIqzjaU52qb-wgdvea0vutjaTYzBkPX4V9TZoaKcaIEUC91ZwfBtycQEHuCew1ziNUA2gIgOy-3zRsCWu0Fy8VT8YkUBZlzZV5QpVIN5wD-a0qiIEFhIOh-GqRL1EK92bbeyW-UrnsaYAWYceAsqlTsSSkHJlFnjxeG5BPOChCn7bpmZWfaFHbq9aFCnWm8gfMIRng6zdAnb1QpKmrsIC8w01yC0rY34VClsR3blkxYK2xaSUJ1z9cULQs-RForVxJRuPZByo-LMAn2OpoL6rwDA_psWTZ_Y_3Up9NMrps76y6MHg6rCqalqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/23435" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23434">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNS7skMYVSCUtIDYjhvBMVHJoKESltv0XKr-gP42OzUNNlSeJg1y-1z1_S1nreCGJDrv4-D0VxarCpqAPFY5tiawI4amVhvep0XXAvx17xWkTGFRq_3aipbHDaV_aKlXi2Bey64I6fW9xcUZqGcmt5b12jyJ_3vn2OPcNrSv134LT5Y5B2x5AGH9VjX-Kh3z3lR7M1WFCHKin9Vh5mjzkPNLKAGYeZwehSnKKCmxwMLoCPp5DFqBZCTS0kcBGM1ZoScH9VPWvEW83ZiYVxBVaWHh8zVhZq14jYCWoswqg87cd_KWx_Ym0rwmBLRDUUX6AgMkZs_Y9FTclIH3r_LH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
با اعلام فابریزیو رومانو؛ سران باشگاه آث میلان مذاکرات‌رسمی‌خود را با روبن‌آموریم سرمربی پرتغالی سابق منچستریونایتد آغاز کرده تا درصورت توافق نهایی بااین‌سرمربی جوان قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/23434" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23433">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=IcbMK3ogAUvHkVPV8SMrk6h8CQC9F2CLOe0FVRLgEiY6Yb8MGJ5qp10qUQ_fDOnP5yapOASKMjJGdAIPRXZL0U0grF5kCVpqoMdHyiLDMwlT8O071vsLTXoAhiF3DEe4paiLcXfvhRbKqXHKEO230WHRO9chlDChjTZaBkIikuBvR2fVx5B69FtMq1tZ_cpuNcipnEu34ajH6TRGbADQFmjw__oaUqCz9y2YDkcq0_GemjY2OgsZDfxgzZUdIlnLzFNYsxnOqZZ-Fj24qOIRHnm_X6b-wCwwNPEG_8Ox5G4JcM-UTGUW5lqVB2hj3A5cMCLRsdRQFKMBzwNObitbqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=IcbMK3ogAUvHkVPV8SMrk6h8CQC9F2CLOe0FVRLgEiY6Yb8MGJ5qp10qUQ_fDOnP5yapOASKMjJGdAIPRXZL0U0grF5kCVpqoMdHyiLDMwlT8O071vsLTXoAhiF3DEe4paiLcXfvhRbKqXHKEO230WHRO9chlDChjTZaBkIikuBvR2fVx5B69FtMq1tZ_cpuNcipnEu34ajH6TRGbADQFmjw__oaUqCz9y2YDkcq0_GemjY2OgsZDfxgzZUdIlnLzFNYsxnOqZZ-Fj24qOIRHnm_X6b-wCwwNPEG_8Ox5G4JcM-UTGUW5lqVB2hj3A5cMCLRsdRQFKMBzwNObitbqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/23433" target="_blank">📅 13:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23432">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=iMz2r2UbAJymHHwCo7i2h-rCGPFNYbPPpL6Lb3plPAE21WfLIStXJmDpburF4nEP6E2VmLewWulXgrQrvFPyhTcSFAAweOcFSvsAat-QMlksItU7mRQl6xeppl09bCRlOXzqcaxpcNdpZbYSBcBgDec_R_OXWmE7E6yVE3lhVOQ6UBdd8p_tLt7awtMN3kB2fbvjRuh3hwRl07VWJrFhvlhfyKs7cg2gnrvtKBGiDgrp8iqXiJVU4owGkbS1f5zxt84h97RclknZU3TO5RXFJAjpGZnff-MLSWsPLezxoi01EbFFTiFDqGYefvQ41xWFdM0F-F-Hbrz3DgpfR9CNCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=iMz2r2UbAJymHHwCo7i2h-rCGPFNYbPPpL6Lb3plPAE21WfLIStXJmDpburF4nEP6E2VmLewWulXgrQrvFPyhTcSFAAweOcFSvsAat-QMlksItU7mRQl6xeppl09bCRlOXzqcaxpcNdpZbYSBcBgDec_R_OXWmE7E6yVE3lhVOQ6UBdd8p_tLt7awtMN3kB2fbvjRuh3hwRl07VWJrFhvlhfyKs7cg2gnrvtKBGiDgrp8iqXiJVU4owGkbS1f5zxt84h97RclknZU3TO5RXFJAjpGZnff-MLSWsPLezxoi01EbFFTiFDqGYefvQ41xWFdM0F-F-Hbrz3DgpfR9CNCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شهردار شهر سیاتل اعلام کرد که ورود پرچم‌های شیر و خورشید ایران برای بازی تیم ملی برابر مصر مجاز است و از ممنوعیت‌فیفا پیروی نخواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/23432" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23431">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXyzXSFLLh9SfcpT6OnEsKWLoMf4KNaZgs8EWmNFfyXSD5xlcQ1I3RMliTyBD_AWGmDO-a6hyERp-aT7i4_KErBqhKiC1FqrA45iji_SGI7Mnu8EMV_IjJWl_Deb7vxRR4r9QVj_yUjJY5xCjKfpnKchNaTqfHJu4Odn7tR5Nx_V2A-GJTAA91J2ZakGG4ukT-bePyHBhgep5RpjbCf-wzxBHGUDN2Hom2LMvqXOfBColtUBPfb4LTR6HhwP4m8ulap9xR5zT4chLsmdWkvNlM44FrddReGMvbzF246vEwYwAO4yMDnftrT2jwjeROg97pEuCURYIZI7_Ut1lfDpJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
حرکت‌ جالب‌ و زیبای فیفا برای جام جهانی؛
تیم‌هاییکه‌سابقه قهرمانی در جام جهانی دارن، لوگوی طلایی روی لباسشون‌دارن و تیم‌هایی‌که هنوز قهرمان نشدن با لوگوی ساده وارد زمین مسابقه میشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23431" target="_blank">📅 13:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23430">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKWcPK6UeeUUeAWm6WIVzVArEJsJMI6pbEfrYIjj02fv5s1qyWaiEftTF_0sGjckB0xAWvTcIjetk_GC2l7kJkk6JmM9gN1WSdyY_3Bx1rhZw-Lrdo73NBIOsHWbopLo6Vo9ca5XPWUTUoKb-8jPgLNbOP-v8ZGfzTuhqgYy7ekdXPGXpzt2bYAOOdXdBbiobHt0vd0S5YWFonQi4YWCS_mPNk7dvs70eCsmMxI9qieIRrLNe71bsOpVD-BaUi8Z2rrt6Q2lnSmnXE1sQh7q-xPVNUxK2Y3NIEt3nbLlOBg0s9Ru2tTrGyLFQvWkIYwQEsMPvLmNR4yfA72zhIDd3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23430" target="_blank">📅 12:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23429">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=Spyl_BaHjAvsf8bpPeSQxBFS9JWL0Sx9OFzwDFMJnW3RfBFfCMqsK46tiwtexnT4EALhSwDVI8u9gg3DeMup6jOMO925Ipt4wxmNLPqMxKfKBBlN1WC-kQVSMFRDKVyFjnbkducDQpk1Ks3DpLWW6mmjBEjRghXM6iYBjR5T9oLUOPBl6tpB0g8YEkr5RWpoNeNKce_kLtXTqpk5NIgYh-iMu1gR_QoBCPLySQ2o6O6_h6q5Up184xyEM4rFJ__05IFphb_vaNkP0JljzQuaYoZinb6da8FbT3fEhzF7zOHUEveL7CoS_Rxxd3zixCcJcExtxCq7a4wb-XyXViKTKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=Spyl_BaHjAvsf8bpPeSQxBFS9JWL0Sx9OFzwDFMJnW3RfBFfCMqsK46tiwtexnT4EALhSwDVI8u9gg3DeMup6jOMO925Ipt4wxmNLPqMxKfKBBlN1WC-kQVSMFRDKVyFjnbkducDQpk1Ks3DpLWW6mmjBEjRghXM6iYBjR5T9oLUOPBl6tpB0g8YEkr5RWpoNeNKce_kLtXTqpk5NIgYh-iMu1gR_QoBCPLySQ2o6O6_h6q5Up184xyEM4rFJ__05IFphb_vaNkP0JljzQuaYoZinb6da8FbT3fEhzF7zOHUEveL7CoS_Rxxd3zixCcJcExtxCq7a4wb-XyXViKTKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های‌ابوطالب‌و‌قیاسی؛یک رولکس که قلعه نوعی بهش وصل‌شده؛ عروس‌دامادها میتونن با پول این شجاع خلیل زاده رو یک فصل داشته باشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/23429" target="_blank">📅 12:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23428">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT3peM-1W2hi5-1aSCF9h11YHou68S3b3KS-DoguSwS3HPaMIyEfw7D10Kh8PJ3jZZJxCaF6KHgC0D8hCvTEP8JHhXPBERxj4j5r_qHWGFkX4JmjD9YVSJLb1LOzHLAGyuxzvACy_hb6dFswBdjvftpYjDhO4ZkcUELkcg5u2xdXL1CFX9RkfxpDsS6aFm5Qxrmo4okMhMdyBITEERvcAnlvLJvMEjF1jzQvbN-YdmLSrYmwzsjyWJSLkH1zh7XgFnbYJlO_gtvL9QvXlWONZYxyMGGRhYUmf2XN2XO8TVse2T97GKYlivD2IpV7u-zUgG4BAzh1EEWCEW4D7JX3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23428" target="_blank">📅 12:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23427">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pv20H-6EAZS8ERW0IBVHkTeb98KxckWPTeFkfR-ZOFnGj30XmJ6ScCddIJP119UIZSeeiV5UemlWrRDZgFlz6nVvqsuJrnFgouSmYcoDNvi3fpUp5pC677y-siAm1GdZNa2TJ416sxdcKH1nqHGBmrpur7yj6nJIn0HUvyMYSbQZgUAihV7YNXEBNu9G2nl87zSElX0_NGzpf7lyqeGsmTs1ms_XkTk4TN1czoKp9XlfhhkQkNVK9IsPFw2vBh9kz-SezngjRYE_e5xHBFALPEWWLE6lUK1mj3xUbFsBFDBqblHaTbNSYu1VPivagqLk_NqFxvPq3bRp7XWQOkmPug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇺
سرمربی‌تیم‌ملی‌استرالیا در حالی تو ترکیب تیمش مقابل‌ترکیه ۶ بازیکن با ۲۳ سال سن یا کمتر به زمین فرستاده‌که‌سرمربی‌ایران در لیست ۲۶ نفره‌اش فقط به ۲ بازیکن از این رنج سنی اعتماد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23427" target="_blank">📅 11:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23426">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oqj8kQzqvTNNDIeCFkb4r130tPreLQ5YjP0047rM0vgrUSgW1v0a1DDQpDN20Gcvk7rtrZquQq_GNYwEG9oSn_wB0GK5TU009ykDqRjJfBpVLBZIJjRWvUbeM019v-udWfHYLtylSe8yt9BnuZEAaQQTeWilMl6Rwa1IQkD6VSA1WQbtwMPeKQeCMACZq9bQ2qFaO5r3db0YmZR7VMzRqS_vv49wab-3CVSUcDAHMtTaCpRh_zW6TuWgIS6pqCMTJiYGLK6or7AgzP2d8RAaA2xJ0CExsT7uvFVXjUZyCIumFvUJi5SAL60TUURKttbEityUapuz4PYjzNKcWFm8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/23426" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23425">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJpBsZ-T4Q1KT1L0p4-9zh_aI56PxDkVH6gj-CBLI1PQSd-nKXG2y4lTG8ONRrOhxiCr3wJWTvy5vmjxW2912Wqsn1799xHfU3wIYPOWkiTdU_K5ZpXfr1OFKL2RlEeF-8NFe7LmwztN6kuk5OpV-UxpnPCd7HLoW_vzBubQG4DnEz200Ap2LihD9tLxMB4GoTssx9En8v0jIbUenuTjpWiAZozpC07_xQAKIKfki5nNyaye_c_teQUuiYeeX_wMh4IvejsiqzMtvs__masClhRB8lSBe9zwkDE81bSB0WkCfXhiAMIC6vj_aq0cjT6IuSpwe02WFs05rNIjKVgn_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
⚫️
#تکمیلی؛ روبرتو مانچینی طلب 15 میلیون یورویی‌اش از السد قطر روبخشید و رسما قراردادش رو با این باشگاه فسخ کرد تا ایتالیا رو در یورو آینده به جایگاه‌اصلی‌اش برسونه. مانچینی در یورو 2020 ایتالیا به قهرمانی تاریخی این رقابت ها رسونده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23425" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23424">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUSa16lCEOk1qCaa6ykryCBH8ZEoaAe8PxybzJhX-wOIKZDBSsBPCHrHagh9IEO_Upbu2FZhvUv9PLMS1tlrNWUk-wSZw31A0h3vOhbgOj6txnKllolbuOe9XWGme8cDeXhcYv6Lc_-vMLg4uWCxu62O6GK5gwaUoovSJBtUn1Yxsdu_UFaHN2hQD62kkHbBOJmvbUmqm5C_85hhl2xY6UEppU6zvk7VsIKg0uGB7PWKMdGVYdiYsgCrwh1B5D5z-QJtzJ8ogS0ToKaxM3Pbp8JeLfK6VTxAxPzmcOZ63NUOuX5xUyP5r-NXfDxR1obrMv5q5ozUpd1zGw6wbTOb_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23424" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23423">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fJnkcegsQ0iI1QMK3_bSfr57ZgDU1I0Wz7UPe8w5JlNUSAWx0qXbVhJP2xShViwTRaoUFa66kW5gIZcbEEH7bmXWdBn-TGMOV_Qn4HBVkj2qvqec3Z-rFahYi6jOV9k9f6hJmrar9HxiaKRaz5Ji4wYFnLyedJSxdlBDtGWJIVQCJc12iJccQkzU2mKEKnYTQRHAN9sQrzn2_96SdMeEW2uWP6fSlqetISADaFcCBwLXrhMF64YoYXEExLYq0sOiyfLxxI-UYFV9bVRUXItHJR7kOuv8Tpz4RJcZ4me7XDijerwAkdV3i6KMiA4tGmoH-fG0lWPw6byj7YN85GghnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">MelBet | جایی برای پیش‌بینی‌های هوشمندانه
درجام‌جهانی 2026 هوشمندانه قدم بردارید و روی پلتفرمی با اعتبار جهانی پیش‌بینی کنید!
🔥
امکان شارژ کارت به کارت و هات ووچر
اسپانسر رسمی جام جهانی
پشتیبانی از زبان فارسی و کامل‌ترین برنامه موبایل
قرعه‌کشی و آفرهای ویژه جام جهانی
✅
حرفه‌ای،مطمئن و درکلاس جهانی پیشبینی کنید!
📌
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌ Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23423" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23422">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk_CtsXgLDRSWqoA_KZqbf61wL_UEJ1B0Npf3n9WPrAyTRC4B0JwFbtGtf_BPRrky4jvYbxtwD-ndIoI642BXTnCHantqVST9vnIqJqvxipwM26nf-X6_8THMD6jc5Qu9dGVMgsxglvZH-xnOAo281ZL5HgR8bPY7Qo7-151LooGAsT0Vs2VnK-AFw076-8Y-vhRZWCaUolf-3LEzCrq5qE-0HGhRNoL2Sq04jnXPJ4sN2FTZWvGKUd8W7I1uqewQrF9lYOpclXM85teJ8NqK8Cp7nNZOZiACvpSFqSSnTWTnT7cXJGhwCl-ToZsSDSFprgTbw5ZBlvwO6BA2hZCEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23422" target="_blank">📅 11:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23421">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZPF-FXz6Q_OgEXLmnwgD9fHzlvfeilPFEJ3QDrQgTM5L4ZiIFTkg6EvP_QCloTIoIllg969BOKhTCcgTjN6s9h2lPT5KeATMTZqkyKcGgqof3zYGTIF_id99-9c7YsnnEyAQRjXsquRfbGsBhnRVhDxJL9CF-_-Z0YSu0q108Al07rGBlQrCwT8DsIl4Bxm8hvDYHYm_lQGUS2tJwyEmJ4KGdxSxDzzEgNo2yx-3Zk0WR4nIqvLjPVo99Aa5FrzY-zrHdTPv-nb49R7D4-R-z-w4O5pGdaqiqth2QVGPqFitoZW5gapCI1_1Q-qLSfZf1cK7jPEAf5IausYJJXKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C و D رقابت های جام جهانی در پایان هفته نخست؛ استرالیا قاطع و دو هیچ ترکیه رو شکست داد. اسکاتلند هائیتی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23421" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23419">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qssFyysYyN25LumCaTdn3aub9iF3luyORMMhZoiSGR1BozCDaWg28bz9ogJON4opJok2HzgqvtZU0-VJuXwLo7YjISCR06E5AmhBjy9XW1PazFAGQ3BAv1wlCgdkzQG94jrUqLf2fPIpUmWDFJNOnovGRGEWbjmG11vpYav6ty-OcAg2bHTpkGsQi3HH3HRefq-qyfxWC5A0Td3B6cxl2laAy9GhOwVm6991ZMmCwsp6URtATXzUNIAxFo6P62_zknn-RiwJIyh4YZhFNgS1AkfjmX65HGDoSHdaf_C9FvWtvbsfzRREelPDWFNjNls00X4YZofH2zCtr8SWdc6JSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vLTY0rKNHYcQoQ4xwwhnRkIAVf2rpUHf0ZICAFlhs8TU_jjg47TV1qKI5EQKEJTpzzinQwFEH2eRRjNrxGMVEaahg16YuZt-c8ZlCJ9qnK7HxffR2L0dw08lLX_26yhyTyCZkOlFSgLPPrn_sWHEnZO9tgBCvfQS9IJapnZKBwfxdYF22Ks8Houcalz1gfD0ZsbqD2ufA6E8hDBCl4StXKf6-J1xU7hHawNPE1bGqXKK0YYdvAK_rVxslAHMRSjzBI2udUVzjwC5bwqSu2fAJ4Z_vg9qDTe_QhXYEYvUTrIvd4kCTudw17jnZz_min1-WgW_BsL8tqM78jbq5uSwsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی کاپیتان مراکش: اعتراف میکنم که در نیمه‌اول روی اون‌صحنه باید اخراج میشدم که شانس بامن‌یاربود و داور ندید. لیاقت‌پیروزی در این بازی رو داشتیم. هیچ موقعیتی به حریف ندادیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23419" target="_blank">📅 10:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23417">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaOYij-SM4BVWqZIh9Li34bnee_yBr-OOR02hVPE4yMLpk63ABSbKgJbXnQ0BG2yP_iN_BDfirm9geMOlSqPginrTEX9fgWuJrt0ab8OwfZ3Wy8gC36NfJsaZjP9CJZaFoBp7P8IWuVhpY-0YSnGW1Xlmrn_8aYz9DtZKa6Zu8iJaZQ5DIRtIRXBPm8apEBT31ldB-ABY8h0tO0nA8kf0mgqPIeIpKqxPfemV1b36mnx3xmA5v3qK68myExN8iT54AEXAtXUPglFQfg6UFRZNvLgZonajGUVbrqInu5gTQu0ofcvU0s0rpwcQW8WSRyqmsa1y6t-MHk7JxYis8YtEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=l_4CJ_0p3UWKyavZNF7UtWz2yDPQiBsfStWHOVpb3jRJk1o_g4buYXwRHS90H9sKULqVZnHdFTcsEPsE1aEyo3yiq4n0JcYhetBUL0P8HOdKCoFU7pw4hKLDTvmnCPU6lS9vV57A7R8PGhdavC241KVZ_WImrG8fS_49Q8hlKCCGqqZ63TOwO9CnglHYKKn3ts1doTCPicIVMJzI2zHSyJ6_3Rb3xQyiGQHBId6YuZlEm5L3qv28_ePUU4cIABAAMmf2uilSlMDbbX39zsZpieIQ0XML3Fx6c09HQVd2uE-tLrkFbdnTPuoxs9IORUI0VhBAvnCbpNvnysuYy2ZL_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=l_4CJ_0p3UWKyavZNF7UtWz2yDPQiBsfStWHOVpb3jRJk1o_g4buYXwRHS90H9sKULqVZnHdFTcsEPsE1aEyo3yiq4n0JcYhetBUL0P8HOdKCoFU7pw4hKLDTvmnCPU6lS9vV57A7R8PGhdavC241KVZ_WImrG8fS_49Q8hlKCCGqqZ63TOwO9CnglHYKKn3ts1doTCPicIVMJzI2zHSyJ6_3Rb3xQyiGQHBId6YuZlEm5L3qv28_ePUU4cIABAAMmf2uilSlMDbbX39zsZpieIQ0XML3Fx6c09HQVd2uE-tLrkFbdnTPuoxs9IORUI0VhBAvnCbpNvnysuYy2ZL_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
برونا بیانکاردی پارتنر فعلی نیمار جونیور و کارولین لیما اکس میلیتائو در ورزشگاه بازی دیشب برزیل
🆚
مراکش درهفته‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23417" target="_blank">📅 10:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23416">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wltyf0wqV1aV0g1fcT6PP7AAybAEEpC5zE8wt2pyS8FY8G90_ga6eNEQbZyAEXrTRJNsJpFSxYt9kY4VNW3qxgKsW7haqEKd93BkG5TulOeCO1C9Tr27Jp4JxQMgsC289KpvvNQuRcnfwDbh2QXrtfPtfrON8uiYG7xeiw3tBPOoEttk_IMOJtLLtP5L3xACREULpF_oRHr-iPTtkP-we7MiTALk_KPwijVP3KW7VR8flgg7ukyp3DN2tzTqC6D2IInCYY72BJL8zcKvZJsJ-M2RgDdw6jna6tAPIcBHnnr_KM-7tU2-aDsfTksPw8fdIyZlKwbUYE-mryyk14nQmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ازکهکشان‌اومد زمین بی‌بال پرواز؛ مثل شهاب از اسمون اومد با یه راز؛ خرید اونو قصه‌مون شد آغاز، امیر10؛ ابر قهرمان جدید ایران و جهان
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23416" target="_blank">📅 09:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23415">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=mPyb2_cAC0nbLWUq07v3aZKv5OIQkYas99qD8haeFfzkZsX_AhhieesJYeAvjNfDzvHWOEgpghlE75BmEdc0CeUb_WXgo-EdwZVt950R3ST9zr-ROX_8f-PQLcccifxFtpxZaW19Hi00553Oxld7BZ8BdPWp5OFU1iSmPUm1mpTwwQprdKiLSf_CIQHkfLHOGEwDv7EGz_yC3TMejT8Ls5vDi47eBvH_GZ59r8ohXeGfyEte4kg5aLLgbSpNcycOhu_CKf08yjBGWido2E0UNAUB8798wy1SMJroLwNMy_7JZ61MXss59d8kp4bu7NBQv8n1DEpLdX2nFQAuvVfWpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=mPyb2_cAC0nbLWUq07v3aZKv5OIQkYas99qD8haeFfzkZsX_AhhieesJYeAvjNfDzvHWOEgpghlE75BmEdc0CeUb_WXgo-EdwZVt950R3ST9zr-ROX_8f-PQLcccifxFtpxZaW19Hi00553Oxld7BZ8BdPWp5OFU1iSmPUm1mpTwwQprdKiLSf_CIQHkfLHOGEwDv7EGz_yC3TMejT8Ls5vDi47eBvH_GZ59r8ohXeGfyEte4kg5aLLgbSpNcycOhu_CKf08yjBGWido2E0UNAUB8798wy1SMJroLwNMy_7JZ61MXss59d8kp4bu7NBQv8n1DEpLdX2nFQAuvVfWpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نگاه عجیب ویکتوریا همسر دیوید بکهام به تام کروز و حرکت عجیب‌ ترشون؛ درسته ما فرهنگمون خیلی متفاوته ولی‌همچین‌چیزایی دیگه مورد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23415" target="_blank">📅 09:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23414">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZhGYOHkfIlE73gEC4bt-2nmnb0sMvRbKqNbnxO1LKEhuf2hnDJhbaCgOVw-Alfotn7uI9oFTWRE55ewP6nUuf141ACTGVvaKcFD37tjjWvqySgzMxOxpeT9V22NRtfc7QPXvJEM53kvsitcE_TN59RrlIuWCDJMhUHRaUZpsc6pVCAKd5t2LhDN1qUNpd4sQ2rL_eLWIBSB6c4JldXYwaFVXTZoyaishEZnFu68EEwtUatMnCWG5jUmmvFXls9BriXvAZyk6PIIB3DHAlFsL5C4eLTb6dO_jcYGGpv9TQhuS9RUeK8xoce7xKjPW7gADV7QnX4I4pgnsiywl-No8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
درحاشیه‌تمرینات‌دیروز؛ بازیکن‌کره‌جنوبی داشت وسط تمرین یواشکی از گوشیش استفاده می‌کرد که یه‌نفر از کادرفنی این‌تیم اومد گوشیشو ازش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23414" target="_blank">📅 09:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23413">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da531b194d.mp4?token=a0diFKnu4wwuCYO0eWjL2UOBIvAMhK8RGwpn211PauGQoWP00Ymc_YZ52FSCvQGuSI7HXS4cPnNe_N-gsT0FPp3GUbDMQ0PiPmynO8_-AKHROnstP7zcy-1QUgjg3NEzbiP9ts6NLd9hrvkEn4DcXNNZoWtNV6QgmlXDKqLg8b-T-GbFBAY_quCQTy0NHddypAdEHsjqrXeYbSoMS7mRoWw4JJjx2LrqRkrGwnwd2eVcea57v94o8Im4ESN45O6U6NffEp9-p61G7K-u9K4o4uO_IwOYtfF9F30oaI2apBI7mG-MTI_IcsybtbfOT_s-Ny13RXDqKc_W3EXhtKMgpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da531b194d.mp4?token=a0diFKnu4wwuCYO0eWjL2UOBIvAMhK8RGwpn211PauGQoWP00Ymc_YZ52FSCvQGuSI7HXS4cPnNe_N-gsT0FPp3GUbDMQ0PiPmynO8_-AKHROnstP7zcy-1QUgjg3NEzbiP9ts6NLd9hrvkEn4DcXNNZoWtNV6QgmlXDKqLg8b-T-GbFBAY_quCQTy0NHddypAdEHsjqrXeYbSoMS7mRoWw4JJjx2LrqRkrGwnwd2eVcea57v94o8Im4ESN45O6U6NffEp9-p61G7K-u9K4o4uO_IwOYtfF9F30oaI2apBI7mG-MTI_IcsybtbfOT_s-Ny13RXDqKc_W3EXhtKMgpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23413" target="_blank">📅 04:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23412">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxML-Rr6LTUHxmafTq_UkqfoVbzqZTS0Tjm_QFFHIhU5jvrkOWF4Dt_plel8O32A2mYJUShK21_d0diCs2XodNOXxm8qIvjmKi_XT9Y2nGGXdw1uSR0gDQx7y3cXNh6uQ_nRRbXNxdP4g_etvnDkfBrzlT8hJ5poGlcCCtw1IFYJEfDyWMONOXW6rNSmkfQQbfcUAIKUtHqzktp_FGpJ6IH239jFPuQKWO-fkKdf8NCB2XB9gdhptOWyx9nf4GuCiuyroR1gSXIOvt2BrIb6ELnAQr8l38Uet6jX6-mjBC1mp5eIOYqkiZY2AROqwQ3lMLft5eMq4-frLfiKX2O0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23412" target="_blank">📅 03:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23411">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی برزیل - مراکش در هفته اول رقابت‌های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23411" target="_blank">📅 03:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23410">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23410" target="_blank">📅 03:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23409">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi0793k1ssFSmpgp8Q_u1DGi9K5lIGII2jDif3z7RxwmTbI2on-0uLSRA0Ay1LgfCG1a-ig0mFaAJ76HefiaOdw0fmOeO1GXAS75zKJ9bjoBIQ_VSFtYLDgXjavSPaLexyDPYHMl_f3ilCof0wnkosCWawvoKMRjgXq9A2qHgwGPlbAtXRV37hNMRVRazzwdxfhxtzNmDT1TmPXOv5pWoZ1nGkgCXHnNNNrxlYU0xk-SW7PS0ihBo1lklNHIgSAjbkbFu8eEQhqo1XWFebCb_cl5ezzYl3q3xEHZZYa3J0Q450T8WmJl4QZ4ap5YRVC_5I4yKN13vwLMgCWWHWvM4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23409" target="_blank">📅 03:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23408">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858efb6719.mp4?token=ZpDpYT4rJrmaa1XZcYqMCG5T1jBmx_5n3c6a1ReFAJfq-0mKY3jYo4Noh1GMlX0TPqE46tsmwT5A5vy-E2gGZ0Kssw8avENM8w5hjYAP7qTu_GPtYF6x6ggo5IVAW0a8yK-sZBfsA36uOL9RM1sd1pDRsNo7RXrRw4sKcUnhnulm_yAvsxBLGBUjDGsZhnV8-jieV5FHSiwcNDcLukYSAjTnjY58NgCEDMY8eq_njtOsXcc57Xanp5dSi_o2wnvsEXtf5LDD45exrULSGZJXgEPRb7DWGdmWBSmOYFiaztX3RvqRO6XsS87_5CuqyUo5tCh4ie-NbSQfSBz9umc00g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858efb6719.mp4?token=ZpDpYT4rJrmaa1XZcYqMCG5T1jBmx_5n3c6a1ReFAJfq-0mKY3jYo4Noh1GMlX0TPqE46tsmwT5A5vy-E2gGZ0Kssw8avENM8w5hjYAP7qTu_GPtYF6x6ggo5IVAW0a8yK-sZBfsA36uOL9RM1sd1pDRsNo7RXrRw4sKcUnhnulm_yAvsxBLGBUjDGsZhnV8-jieV5FHSiwcNDcLukYSAjTnjY58NgCEDMY8eq_njtOsXcc57Xanp5dSi_o2wnvsEXtf5LDD45exrULSGZJXgEPRb7DWGdmWBSmOYFiaztX3RvqRO6XsS87_5CuqyUo5tCh4ie-NbSQfSBz9umc00g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23408" target="_blank">📅 01:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23406">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5o5b70hUeVcbVkboaMbJOTO-Ww7c4Opp2BTAlhra2pxChu3-jkAZR4nVsTbEyr4dv9kYSnA9UFROV7aDUozKh4YBISy9n-CveCAR-tDmXkaA_NL8cup04l0a519S5gagc3xYCzljde8lmUvDpSGEV0imQNhH1NGAxKpqRMDdAIrG7aQOmJKaiFyLJthQfc5n00To3SdqyROM52l1x-NfZTAb2fAkq0l1wSya3EgFvBxVYajanMBTYSbfC0-N3E8Zn0QDrGqgheaXbDumQjCWWe2dzh84thim_nLXwuqQbU-_Qnc58wQ_Zd1Uh4tSZtN4hge477ugLpC_VO_kE_cig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23406" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23405">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lte3F0qMI_IYeRFiu9TCFaQ9kW8-IAen6oZabfBZq8HAazQlmixUtJsKsTE1MFtuRDCQ7BxGbmz8Cx8QMDXc2Sy6N8wI3jwW_UMFGNYrDsGE5_zSPPkoO4av9dse0XdgGpn5acnOSlSvAlozHEnpry7-0igKFEACB8AWGVK-xbeAG5-T-UTiiEbwOqGgY8c8Ue0XcmpUycNChO9YTH_SY4T0fZQPqMMv8MWB4p7k5uFw9QA8E6fZTkZG-lMa2HxWxANDSZ54--FdgKG4wusjD-SC_S0rbjkx4xCpfAjYq76M8ef5OW_4LU82kydkrFcg6gzSxRQ4TcCtw5F06V58-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
از برد آمریکا با درخشش بالوگان تا اولین امتیاز قطری‌ها در تاریخ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23405" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23401">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOnuKuARD8epYu8oXrvhLFHBC_DyJIcsEJD8uV8GOp3zMte7v3zYSIG9s3IkXAjf-gueMQ-sS_wNbT7LOzP41nU0pePHTshpQcJ1CIUummkMFrDXNJSuyS5uVMKumDoqJ9vLMClUlpef0Kz0XCfmVLbd5ImYNedGTtrzFWtjmDz80MZdChj3_NhQNtOKnuVQcr49Nj6uBYE7a_5jw-AvkltDe4QMUC2ltSCIOWsp910zVm9xeRaqUoBJraPZMrgxFdpUS7spPnD9BnH7B498S4fd9AQx1WmIuyyFj5zEE-cHmTgxoMFFskC8cO2XYC8zD7zItolku-Oe1B87Vs5oRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه اسپورت ترکیه: کادر فنی کایسری اسپور نام پنج بازیکن رو در لیست مازاد و فروش کایسری اسپور قرارداده‌اند که نام سیدمجید حسینی مدافع 29 ساله این باشگاه نیز در این لیست دیده میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23401" target="_blank">📅 01:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23400">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=teSjd_TIS7Vb5Ln8r9Wk5ICkHPAAtW_osVQrVvxpMgWUP8uaXC8kKLtiyg9vlwAtxg59y-_V0u-8a4vwfzl7kPciLbjmllzmk6I3dsWKZtuXZPAqb-yg810IwMaqb0fD78AapF6_N_WIxEJgQ5D8UIuXao6RjBkk4TvuvaPx0IxhXi2OfYoFzC0Mvq3oIND-VrPj-D1p37UvaeAPwLyLsYxw-qkzfNqmLMKfxyNEcQo2_dXvFJbNVaY1AVyy0PV5Q9AsLuXgtYDM3c-UCiMUn_ryOzD6ykihecpOroXDjYFxjkcbR3OqsifPmZ9xYGMfNVbItJJp1DUyflIqsxmWqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=teSjd_TIS7Vb5Ln8r9Wk5ICkHPAAtW_osVQrVvxpMgWUP8uaXC8kKLtiyg9vlwAtxg59y-_V0u-8a4vwfzl7kPciLbjmllzmk6I3dsWKZtuXZPAqb-yg810IwMaqb0fD78AapF6_N_WIxEJgQ5D8UIuXao6RjBkk4TvuvaPx0IxhXi2OfYoFzC0Mvq3oIND-VrPj-D1p37UvaeAPwLyLsYxw-qkzfNqmLMKfxyNEcQo2_dXvFJbNVaY1AVyy0PV5Q9AsLuXgtYDM3c-UCiMUn_ryOzD6ykihecpOroXDjYFxjkcbR3OqsifPmZ9xYGMfNVbItJJp1DUyflIqsxmWqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23400" target="_blank">📅 01:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23399">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
رتبه‌بندی‌کشورهایی که دارای زیبا ترین زنان دنیا هستن؛ ترکیه با اختلاف در صدر جدول قرار گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23399" target="_blank">📅 01:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23398">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q16lWBihUVdaKifQNg4i3CNXAE7AOnoe_veSIF8USGhoWx23YCc78NpTt8s64rPtVSXfF9HGzRvDowRAWjbZ8N2_bc7wNUGma_gBhNERICmlc7BA3pdJ_eIyi5fY4kSW6ed-H4lzeZBr-g9ny017YCdMwiz6etZfpfubPRAU_F4vIPjzlz5EIXuEKaQoOxXYZJqz79azBgg8gTrbxe45IxSoTKD63QCYm6K4ZGC7Xs9K56RlLufBRo1ns-92Rw3lcOKelVRsFY0bEMt8nxoh3iNPPnAuyNTqHlattprv4b6Z_nJpuZ3IFX5excVcS7FZ413o2jqaKBVUDq7gmX3Www.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌رسانه‌پرشیانا از زبان کسری طاهری مهاجم‌روبین‌کازان:مدیربرنامه‌هام با دو باشگاه استقلال و پرسپولیس جلساتی برگزار کرده‌اند. بزودی تکلیف نهایی ام برای فصل بعد  مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23398" target="_blank">📅 00:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23397">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=qK0FcKZuWNrvQlGtdiHkHaDyk9xN9RAjwKLu2Flb0P8sMZgFkcyzmBCxlMlXF-BS0pBv14gpDKGyuM2xz1CUXNPckg0BSrh9WxJkNkzRj75WeOusXj5vuFgZFfTmgMCECzECd6ue18gQpP1uqGghsBXqo-Cz4S3kd-LMY6nVLoRpmergxDgWMJonWeIBG_GntknMv3TdHxo4nV-l6zZzRur0QmXJhenFGmOFVFcdr0yomc0rnUf9xa9hJyjPN6ZbqLo3vE_l1kVJChCDsb6La7HthkxYn_IKoBR4tl3gumcaf4UcLj5akFIXKJ3lVrh8IzVPeb9KwfX5RAu7o1CEp7n0Qf_07H_SvqYB-HYZPMZq8sYmKplFFTgEAIl8cUeBNrSQpNBU4lcLLiHsaySEUsmpV-43cpTKV0wGyZsktQfDzE2PNakbEcstoj1me5ETZRbsokKIm6jShaVlKJKe_heRyvYf37DY1bpPnlPN48dxIvzDfpuPZV8ZfisK4iLb15UkrgvnvaIP2prvNUgvIWPE78OvYsPUokwfTP7GT1D-NogEcF1h6o0feXelUPTYtZAXC0_jW-O2uYF0sNdDLwIhKYw1KMkddYPQ2zSkJ2wdYZ_o6td_pKnB8vP3UsHkIBeQrpkx-MKahzrK_klhKbsH5CEf9AlkDmYYZ59rKWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=qK0FcKZuWNrvQlGtdiHkHaDyk9xN9RAjwKLu2Flb0P8sMZgFkcyzmBCxlMlXF-BS0pBv14gpDKGyuM2xz1CUXNPckg0BSrh9WxJkNkzRj75WeOusXj5vuFgZFfTmgMCECzECd6ue18gQpP1uqGghsBXqo-Cz4S3kd-LMY6nVLoRpmergxDgWMJonWeIBG_GntknMv3TdHxo4nV-l6zZzRur0QmXJhenFGmOFVFcdr0yomc0rnUf9xa9hJyjPN6ZbqLo3vE_l1kVJChCDsb6La7HthkxYn_IKoBR4tl3gumcaf4UcLj5akFIXKJ3lVrh8IzVPeb9KwfX5RAu7o1CEp7n0Qf_07H_SvqYB-HYZPMZq8sYmKplFFTgEAIl8cUeBNrSQpNBU4lcLLiHsaySEUsmpV-43cpTKV0wGyZsktQfDzE2PNakbEcstoj1me5ETZRbsokKIm6jShaVlKJKe_heRyvYf37DY1bpPnlPN48dxIvzDfpuPZV8ZfisK4iLb15UkrgvnvaIP2prvNUgvIWPE78OvYsPUokwfTP7GT1D-NogEcF1h6o0feXelUPTYtZAXC0_jW-O2uYF0sNdDLwIhKYw1KMkddYPQ2zSkJ2wdYZ_o6td_pKnB8vP3UsHkIBeQrpkx-MKahzrK_klhKbsH5CEf9AlkDmYYZ59rKWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛دشت‌یک‌امتیازی و ارزشمند نماینده آسیا مقابل تیم پرقدرت سوئیس در واپسین دقایق بازی؛ لوپتگی نماینده اروپا رو متوقف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23397" target="_blank">📅 00:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23396">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=ULPCDmyT8pfApgB6hNvhbtv30Bof062o98-JCHaL0pXG_HBzlPqraz-NDs_LRxIGPxFv7joq_yOhHxbTc2I1eKPYcnO-_i5mqwvOQyZ_X5MVkUQalXqZjCyN_VOrf-QFLaENh9ZYoWiIN_3avfrvFVaZ_PwlQUw9DpVWwjSALYX01Cgs48STEScWh84QEtKapSPEbVGDkwHFfzuvdDoWIiT0SvU_D7mvqJpIOekC7AekZfrHwANHC0THXv7p60tuKhYxR12tHl_wcb2w1Y4z0rZjMIxqFUf4iqQZBE8aXYiZlXqwI1U-GGQXU7tyvn5zTONpclq_brZGQpD3UmlLZSDgMHGVBeVKkLQpcWtAuYLf0SoU2BBPpZ0JPkQ-aWkNfv7Jjg-E-N05N_pwlNTX9fFI48n8z82FZyUwdzdb-YJpmmYfb52RoIVB7XtWcMJpYaVDft7FsVi6-QrATeQWXYz2_rgBUnSYc7n_b8uAjUgAVIvbhnxtttAOe2y2Guzk4hZMKdR0SVZ6AMFJjaNTKT4M_jc96VkiArQR0yDOZ3-4jPztbwFQ9Bq5tn3B04w3lwGBdM0VyuKPpSzceDn39yIfRRfMPe8JyaNlR8lj9lrctvuBzUVwIgh3sa4h47bX353uKG-xunMwQBauyBUfwlgldbciZnEQL7fWSqtilXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=ULPCDmyT8pfApgB6hNvhbtv30Bof062o98-JCHaL0pXG_HBzlPqraz-NDs_LRxIGPxFv7joq_yOhHxbTc2I1eKPYcnO-_i5mqwvOQyZ_X5MVkUQalXqZjCyN_VOrf-QFLaENh9ZYoWiIN_3avfrvFVaZ_PwlQUw9DpVWwjSALYX01Cgs48STEScWh84QEtKapSPEbVGDkwHFfzuvdDoWIiT0SvU_D7mvqJpIOekC7AekZfrHwANHC0THXv7p60tuKhYxR12tHl_wcb2w1Y4z0rZjMIxqFUf4iqQZBE8aXYiZlXqwI1U-GGQXU7tyvn5zTONpclq_brZGQpD3UmlLZSDgMHGVBeVKkLQpcWtAuYLf0SoU2BBPpZ0JPkQ-aWkNfv7Jjg-E-N05N_pwlNTX9fFI48n8z82FZyUwdzdb-YJpmmYfb52RoIVB7XtWcMJpYaVDft7FsVi6-QrATeQWXYz2_rgBUnSYc7n_b8uAjUgAVIvbhnxtttAOe2y2Guzk4hZMKdR0SVZ6AMFJjaNTKT4M_jc96VkiArQR0yDOZ3-4jPztbwFQ9Bq5tn3B04w3lwGBdM0VyuKPpSzceDn39yIfRRfMPe8JyaNlR8lj9lrctvuBzUVwIgh3sa4h47bX353uKG-xunMwQBauyBUfwlgldbciZnEQL7fWSqtilXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23396" target="_blank">📅 00:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23395">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daZZZbdJYZJRqLAcw220eA7Vp0ppELvfMlskM7ec6Eos4hl1MdqUoaLnkNDJQeuaf7n_K8_Ynv41X55kPWyIjSY2qNVB05EPLm-yxTtcYFGmy6qaxGv5Zn2H-GWSQR_2QK8_Pwkat_VhiGZfhLrYdzVwR6TO8UlCthzWrQTf-M8mIqJCi4FUVAEiApgzO2-vZfBETncq0v9ejnD0c_juK6LvTsNXB-9R7kWrQJFrFeLvvnWEqsI4yJisHYAVAaAGS5QKZxdKMZ84kaI_74RrvMxeb5Bx_SwqMk97KgYAESyhr_d3igpF11ZqOqsbjV2vwT6cxcy3mNOjd6HhFMUX2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23395" target="_blank">📅 00:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23394">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncE0qoml4jRvqnjboDqBxvbesFJs4fb8gzDylGPjKvFfth-uCkqLjhazLyhmhvJw-OCEgzSIzgFbJ6xzdT6CcSQIAx06qumqascCfHt0EwH00pqDbYDeYoCleMwAoaDY_T6rlLcYm8oh3R0Yu4HInNdHYaGWW0-GIEOk4spZb-UySMHVFSZ8fZTHwK7VaDEna1zAdJfJa5wdq8Ynhu8C65CBhSJTLU9puUy5uLQdYvJ2-rm5FyALf3pw-vu-Ra6h0kHIzx4ZGBYGou_IIR5PS1AiYzmk_JfSpiruOXbQ5PLi2SuzXJvDKAbWqjHFTuzAZh0-g8guuOG-vS_7TosXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خداداد عزیزی ساعتی‌قبل با حضور در دفتر مدیرعامل بانک‌شهر مالک باشگاه پرسپولیس قرارداد یک ساله خود را با سرخپوشان امضا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23394" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23392">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CKD2MeaXG9K94h441qPdESvefqwPO6WBktjKjy0xfrGkrc4hVsCeDkMy_DYHDq6D6Trgrdt1eX_ijZa2PogbxVA__g2H7RbjORKjD1fAFhqb036vxHe1DqTBiKFeAb219RK65L0_E_MJvI7iwE1nz1dezhbFAROFrMkGKi629WeCMt9BM_DrmoPwVAptYDwtCHNzBkJ8DoIskU4SG2hDTFeN7qFdaGRO4R1TBQWY3LGsjAC2bpK6sMkrN3QU9GKYei4pGK8Keb4UWPKkB4GF3RWHNTiCwIUcbJpZdPwftAG9-4WAPthGSw8XQa7tKvB28hd7tuYVP7_zU3Txy2U5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UVgpFuTG7nTaj7hYQqMxSHig4BqZENsd89wU0D94cxIPWFEBCPDnrvVbGaOGUB9HJPCH1_Egt6kX-AjpXTd_9k4J2eJ6W73YMnCLr1ghBCWuxJ4kClp9LSMMveoTo8wly1dyZtxmBxNAJBR6gw8v-i-hrfSnPHnorkPjEGZ5I7oeGEot5Cq6IpwcAgo0ceCSqf5rSZ6czbsB4NRdR6bUfapn3d5BMSfHaU3xqoJrs5JNZZ3gImpDRQ8XOI2zY5NLblwCLHri7u6ilRjaQ7PNDSTzcipcH4TJk0Vy0O7snghpgUANEs6KcRP4znXEksGLF5HduMdRE4Za6tND14VKBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی
؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23392" target="_blank">📅 00:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23391">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=OH97HCCUPK6dr6ahfw_HWeEs-Fq-imi_NBHuGEJEVwRALsgxd_zBJ8Hhd9bgGIze2-qsc8Hmkty6YOiMYkuK3cX0mbdDWm-2ReEAUOWFUmxLBzcDotBb7tkTFPp3Tds1fSPKkRo8r9Rh8qfMfKHHEdz7R16k8ocFAh2hm7-hZMOEpJ6utT8M82cdMgLPkhlW5rnpzD7KsYHE9vbDJmuqlQfJonpHA_sYzJIeo-2THJ4s0K-zfJMVUBgDuv9AnutZu2KR_3TLiC11OM3v3ko0afaNVodkU9atexLLluuEAcCymVVMxgzeFhB147ds5FHc1WfZtH3OEvGSnE2LspEzQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=OH97HCCUPK6dr6ahfw_HWeEs-Fq-imi_NBHuGEJEVwRALsgxd_zBJ8Hhd9bgGIze2-qsc8Hmkty6YOiMYkuK3cX0mbdDWm-2ReEAUOWFUmxLBzcDotBb7tkTFPp3Tds1fSPKkRo8r9Rh8qfMfKHHEdz7R16k8ocFAh2hm7-hZMOEpJ6utT8M82cdMgLPkhlW5rnpzD7KsYHE9vbDJmuqlQfJonpHA_sYzJIeo-2THJ4s0K-zfJMVUBgDuv9AnutZu2KR_3TLiC11OM3v3ko0afaNVodkU9atexLLluuEAcCymVVMxgzeFhB147ds5FHc1WfZtH3OEvGSnE2LspEzQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23391" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23390">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5-7xJg_Gc2vM0_5tnyPvR1Pne3iaopcm32x54WeETRFoAouLpjY2GIYtz7MiXW7QkzjZJzR_0KXK-PddaypboV-vt2Oz1PYYt7ujxaDIlD5l_Fnar3nfcQYUHzur3i5yWaUNpyVaGxO3JYExblwI86fdfHMscL-vcyzxLmgYSXBhyKJSXtPIsro74lihRANsF4LssOXoSBzm5MrDFf75Yw9kDDAaGIhU1uRRXKBDKaQuFE35HTe3ADM8RWkVdtjyO32xNf7hNxUHCUcmwJN4ulCxT3EhB0mUpsraUwaZsg6xyWHV3965dvjNQ24cpt23oSB05-DSdgd9qypB3SzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
فابریتزیو رومانو:روبرتومانچینی سرمربی السد گزینه اصلی سرمربیگری‌آتزوری است و منتظر تأیید برنامه‌هایش از سوی فدراسیون فوتبال ایتالیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23390" target="_blank">📅 23:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23389">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRzBOgNwHsqrUlWNDrOf17lglhjqcdB10ziNpXAGD7sxlYfC_UVGQ90Ea3sW4ZQeWODhfxYzgjnXOHYTfzmmLdkDtYQIpPVjXVx1z3ywQW_12ICvgmVGqlP9APAl9TaVban7t4xTMPTmiVq9nsGu1JXtulJFPgHk0WGq5-6j1DARaYJxWyAq4nNFGKMtTI6fOEUWxVVGGEsedoAgaLavEtqscLmpxi5jC_OfgNVD39pNsWK4SVPhRSMAsz3uMpLLMGZLpPnyioHGVUzPShWs5QyUQWYNo-NZgx6qgPb84o_NXu2AShIPfW6IeZg8SPZf48ZAqxlB05moDwy9PBScVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌نخبگان|پیروزی ارزشمند و شیرین شاگردان روبرتو مانچینی مقابل شباب الاهلی با طعم کامبک تاریخی؛نماینده‌امارات‌تا دقیقه 75 دو بر صفر از حریفش جلو بود اما یاران مانچینی در واپسین دقایق بازی کامبک برگ ریزونی زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23389" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23388">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeVcBmoHZjzJ2LReH6T9DBdJHsXIbW6oXU2nBVqIv8IjWJpALYdMbbjdqmYhs5gKc6inzz8kIk5jCglDoMc77im1YKxRt5zhryf8300unveyZw_Gv4uh-OcpSORf1RKwgXcqbzfLF0uoqv7dqidn8HFaJxQfvul2Ry-g5noF5OraXUW1xEXZTuYJpD374v6ywLAa1rIicExxLUgFdpTvgnebE3hzoFDZSkIuhTNi-Pc2Jtwm7nZNUJ3XkEWsxNsBlCSDJG5b7mEZ4gMuAYVOlspilvh80VAzGjePlAcATA_8lBSGySpqgrBDdIpEZV5p4h3bhOJIqzicDTCZY2W7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23388" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23387">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=I_mh8bS3jp13eJXc_40PT8aOIzcfgflFFkqGKObYQXYi_IijZm2R5IUHF-MbUVtfuvn6ui-IZytsb2wBGewrpbyl6M1XVML2_u0i15s3odK15eO5qSTYtKK-GJ-WcXcHjtIPvAx9EBYYZZElhJh7ra0kKKj_KDVQAH37Us9EDJUiQkgBfIlTwF_L6TzYi1vOJTU_ZV1asv7yS2vn4vGWcI9QEHf_PYwlGTkSjmjxYse0ikYtmciJ1cFATBxc-rfXQivOqPo7W7xaEiGBbgM-q-CLFB6uUpEFANqbfDmpDUfrfKNjTt2KQZgUpVkSuaGscMPCWQzvSgaWhNUycgHgQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=I_mh8bS3jp13eJXc_40PT8aOIzcfgflFFkqGKObYQXYi_IijZm2R5IUHF-MbUVtfuvn6ui-IZytsb2wBGewrpbyl6M1XVML2_u0i15s3odK15eO5qSTYtKK-GJ-WcXcHjtIPvAx9EBYYZZElhJh7ra0kKKj_KDVQAH37Us9EDJUiQkgBfIlTwF_L6TzYi1vOJTU_ZV1asv7yS2vn4vGWcI9QEHf_PYwlGTkSjmjxYse0ikYtmciJ1cFATBxc-rfXQivOqPo7W7xaEiGBbgM-q-CLFB6uUpEFANqbfDmpDUfrfKNjTt2KQZgUpVkSuaGscMPCWQzvSgaWhNUycgHgQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23387" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23386">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTKZUzWnJc28_a2L8tnUctXChSQV7UV7NAB2jErBBp-q3feR-WMpTAHzqJ0rTERIbbpm4On7K4F2PCWKrzrf7VVw5KdJsjG_pP9Mo_U1T9SEBgjLMuVV-0pqHiLfnJCFBBqywpBayJGYlwpU4K9ld0knXDWS-CAgsy2qutNut3VcI5i1JYjUtKgmhXBs7t7ZWjSeLLu-p6Ixm9893ZW7dLa7uQK4n5fg-hWvrVUHs8IT2_mHY1HRnGcFG-hnIlkc-p2RQE8iToREATzeF36KOLIbR6yNvMwtDzdVNxzdtoKgkyqrWrf_P4_KfdGP7M_wiIBJGiejjAMZTLljAFzTsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏کل رقابت‌های جام جهانی ۲۰۲۲: ۴ کارت قرمز
‼️
تنها مسابقه افتتاحیه ۲۰۲۶: ۳ کارت قرمز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23386" target="_blank">📅 21:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23385">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=OTTuT6_XIwaI0PQsudy3gWy0aLKHipWD7sz1Mmff2N-He--zDCQHMH52LheF-c3-BI1KLuEM0fmhi5U1HS-Jl5xV8HsGLMWofeT8moT5xwo5h03FisLgI54QVoaTPZ3cY0tVT10L1OfGPaQywroLiACK5SMUdRb2V-L3h3snVXJnJo1G27buddYrramUctD15rYB0M2t_Zt7KGNNL5umqwbPSaaPRsFVmv9u2TV2vNK1bml6AuSUGmYa9YocSj7cfMzXXsVyTNfw62kmgRZdV-nW5itUtkoFzXKHNbAG5Q5UwrokDAuE1odjYP8FwcBgxDT0Z3ulM9gJkSQ9dBmS8YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=OTTuT6_XIwaI0PQsudy3gWy0aLKHipWD7sz1Mmff2N-He--zDCQHMH52LheF-c3-BI1KLuEM0fmhi5U1HS-Jl5xV8HsGLMWofeT8moT5xwo5h03FisLgI54QVoaTPZ3cY0tVT10L1OfGPaQywroLiACK5SMUdRb2V-L3h3snVXJnJo1G27buddYrramUctD15rYB0M2t_Zt7KGNNL5umqwbPSaaPRsFVmv9u2TV2vNK1bml6AuSUGmYa9YocSj7cfMzXXsVyTNfw62kmgRZdV-nW5itUtkoFzXKHNbAG5Q5UwrokDAuE1odjYP8FwcBgxDT0Z3ulM9gJkSQ9dBmS8YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
شبکه فوق العاده MagentaTV شبکه اصلی و رسمی پخش‌کننده کامل جام‌جهانی ۲۰۲۶ در آلمان که با گرافیک‌‌های تاکتیکی مثل هیت‌ مپ، آمار بازیکنان، موقعیت‌ ها و لایه‌ های داده روی تصویر زنده، دقیقاً شبیه‌بازی‌های ویدیویی این بازی‌هارو پخش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23385" target="_blank">📅 21:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23383">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB1VE4VOhwnWZhqObOfmu-1_eWZUG2G21zKPTAfaOIUP5WM5LIIvRxiCgTr1_Pe0xTbm6dWolZrsPFR9TRxqxpByE403WeFR_IRVtPhw9XlZ8gqYKflS6Ukm7701sgn_BLgenWykRLexwpegjtVCR68bWdmVBc0z1Jr0qZ5zW2n7b2E80b4WPthJIFQEMIfSI9Rdv3kcgvbxlw-VwY8XGItRVZvwBHlz7H_VQtfq0xztsjK-ZqKDArl-MypvMP7s3Lt-yBQIqNIWv78Pwd7qEE5ZGpH3kyA99nPsFcgqflIL4MdMGp9CULiOzRVELyfmhwmc9pQFMsprP4cE5KNbfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجید جلالی که یه‌زمانی‌میگفت امیر قلعه نویی از ژوزه مورینیو بهتره اومده رو آنتن زنده میگه تازه بدبختیهای فوتبال ما بعداز جام جهانی شروع میشه. مثل سال 2011 و قبل از اومدن کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23383" target="_blank">📅 21:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23382">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIPuBQB0YE030NuGg_HWdSbpIZ3L8GNq_dUCiE7TuBbCjN4diQVWXMbLMyaJnN334uqK25qS-A5o47F_F9SYVh1JNBTkPD8s0OSI24PIyd99reakKWHxvG6bMYluXV62WyvQoSzY7FM90BjWsEII0EhxnIMf4A-dloamgd4mOAVYs_Iko7i1drXJDOD60NcpNjoNDmxwdrmdjMCtJl4-PiXpKW39GHm9X5uyynbzFeHzzhRDnTlg2TzQdI3qPkNAM813ZGNL7e0wcBHjqFaXVDXRGAQe2zcUoIH62guzOwwOfjWXwc2SAru1bhjz5VlSspPGA9KgjYu9fh_gANaA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
دیمارتزیو: اگه بردلی بارکولا قراردادش رو با پاری سن ژرمن تمدید نکنه اونوقت سران PSG دنبال جذب فران تورس ستاره اسپانیایی بارسا میروند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23382" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23381">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c77121522.mp4?token=TMcgKlYZjxqe0vHmhVyQfAgs4Jsb7is0YVKb1UAZUmy5YlgiCQBYmdz8qYcbjxwd7p-udcaHypxJqm1RJjl6_YZLRIt6Q0b-9mXJCOWDZuOIL3rw0Y9Em2v2WM93N3wBeh3Pjgn89J76KBlycxzhv_QNBwCWOGpterdWYliReBnZFsptz54RZ7k4-7diPh_XOvrJRIb1nR1QdPRzKWV4Bcwy4r3gcegfhy7iuV5BzH6S_NeqPexR9uBU-IUD89SjOgDH75tEKMjfWDz_zeUEKIo3UHmT_iUPUjbnNm6dKoNbgcFMU61MA_r0bhmHQKBygpqPxXHW7S6sXxCQtvZfBEcKW39bf04ADZiHe2gpbMwdGPp_IsTXOWMn-FQBOIVjOairvbQXhCI3z37Eh3omHpBnuo_Nd8o0lBbuMIy5WwPTpKmr4XoHT-TErKlJI6yZMC5CHhGmPVZ2FEAwKfkGDKyQtjOHJb1P20TEhOoLru4DIdFvhWOuumuCwCo8Q5mv8gtZxz-C3n2gyxAHG_cM70VNW8OCqvP3298IBeaHmSiUjVac67UO7dxugLsNMOSAxnRJQmvLhWWa6ikdvS1wuAMmDsVICFEPVpz-W45Cjwhx6OBbzj-pD6RGJVBJaqITRrjrTvDPS2KPwcKE5dOdHVsmtdtmVgC8Zeyt-QNnx3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c77121522.mp4?token=TMcgKlYZjxqe0vHmhVyQfAgs4Jsb7is0YVKb1UAZUmy5YlgiCQBYmdz8qYcbjxwd7p-udcaHypxJqm1RJjl6_YZLRIt6Q0b-9mXJCOWDZuOIL3rw0Y9Em2v2WM93N3wBeh3Pjgn89J76KBlycxzhv_QNBwCWOGpterdWYliReBnZFsptz54RZ7k4-7diPh_XOvrJRIb1nR1QdPRzKWV4Bcwy4r3gcegfhy7iuV5BzH6S_NeqPexR9uBU-IUD89SjOgDH75tEKMjfWDz_zeUEKIo3UHmT_iUPUjbnNm6dKoNbgcFMU61MA_r0bhmHQKBygpqPxXHW7S6sXxCQtvZfBEcKW39bf04ADZiHe2gpbMwdGPp_IsTXOWMn-FQBOIVjOairvbQXhCI3z37Eh3omHpBnuo_Nd8o0lBbuMIy5WwPTpKmr4XoHT-TErKlJI6yZMC5CHhGmPVZ2FEAwKfkGDKyQtjOHJb1P20TEhOoLru4DIdFvhWOuumuCwCo8Q5mv8gtZxz-C3n2gyxAHG_cM70VNW8OCqvP3298IBeaHmSiUjVac67UO7dxugLsNMOSAxnRJQmvLhWWa6ikdvS1wuAMmDsVICFEPVpz-W45Cjwhx6OBbzj-pD6RGJVBJaqITRrjrTvDPS2KPwcKE5dOdHVsmtdtmVgC8Zeyt-QNnx3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نوستالژی
؛ بدرقه‌تیم‌ملی به جام جهانی آرژانتین درسال 1978 قبل‌از انقلاب هر کشوریو بگردی از اون موقع انواع و اقسام پیشرفت رو داشته بجز کشور ما که گذشتمون از وضعیت الان‌مون‌به‌مراتب بهتر بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23381" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23378">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1IpeygRdGWy4LSROW6Lhhhq1Ne_cQYMviEsajNURCljfKqcZoRzYLin3zyEa_Bg4UWQbLAq58yuHpnjmzMoF-wCk9cWfjdEXqSF823uhzyBbPoC3ig33heVdy8GDfuJMDAxDQthOIbQ4wCgTm6zjPKXkn5n82qf9fze8gjpkLR0xIHdfmvj_pF3TTWr5UdCG5QaPf-YiCyBYAw25dSVJQ4K7V_Qb9j_fLQ6DvRmwklwGem1jPUUWE9UfPtMIUwIjxIMqCEfXpjGS5Sd_3cM0doikrsy6AJWF5RoWHwFdcZ4bVzg81u1ASCvFzpkFpvRFW7Vyb-r3l-KWmR4K4w85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcXthuvL-q3KU1tMUWYy2Fk-KPizQTOlI4QYEz6Jd_pOK_hdi_nNRtUBmwHmknnfO9M-IpeWmLSwovLBaIGOX7QRQOhuj2Fe99H5RNPHLk0YuhcvYCwi98wtPGDF41JIuJIYDpFqSjwUZTIbGcKzGcIP5oMFOWVltzB38-DhJlPVTz8MO2oDO_pK9PxKGHjSyStrguQ0GpA65MSU6xzGjvTH7hg5Xydkqu8M9-zBRPxu7tttkK-OGQtvNyCEOMq6Jj3yIBpVqdSdRrf-scReXvWbD39BkB1fXRsMhUMZhZDh87vjJCy7cT1NL9gpYhPktzI-6qTBlza8SkYRgAyL4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23378" target="_blank">📅 21:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23377">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=tIKQoECjxqXDD9hJpFUTY2NWbgT1GEAiWbs2_cYJ-EwZuxFRYqHF30E5g5AAc173x_3Lqgb6VJqdNeJQotA_FjvFgUl3mOR4mJj7UmQz_CJ_w8Gal3Y9BYecvPNEgVwEmnjZHTPcPm9qPzveWiZw3N13tR7doAijrAxsTyHQOAxBlknKKzp8iC4rFweKtNq1WGqrau0TahRC8bHzps7S7gcPL2WdbmDjpAzoCo4-PIPwRPb9ggxGThWNbHRmQXG8flBqKvIOSpSQvcHhmaFgOfUepOhVP7GiMbWDTwA5n965IdKzH_JGL2Es02MKSIOZJq0mxXnBf6KlquOUardNXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=tIKQoECjxqXDD9hJpFUTY2NWbgT1GEAiWbs2_cYJ-EwZuxFRYqHF30E5g5AAc173x_3Lqgb6VJqdNeJQotA_FjvFgUl3mOR4mJj7UmQz_CJ_w8Gal3Y9BYecvPNEgVwEmnjZHTPcPm9qPzveWiZw3N13tR7doAijrAxsTyHQOAxBlknKKzp8iC4rFweKtNq1WGqrau0TahRC8bHzps7S7gcPL2WdbmDjpAzoCo4-PIPwRPb9ggxGThWNbHRmQXG8flBqKvIOSpSQvcHhmaFgOfUepOhVP7GiMbWDTwA5n965IdKzH_JGL2Es02MKSIOZJq0mxXnBf6KlquOUardNXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌ شنیدنی‌ و با حال جواد نکونام از پنالتی تاریخی و چیپ گلمحمدی مدافع سابق تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23377" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23375">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=vjozSV6DUoXXCCt2R2IqgV-BJ9gIp3U_25enJOqMQbNqiFEoS7bDbA6RIkPr31UzscZinxs_o-agfwv8NDyD44C2-VTzj1ICamZxCXBJDNjueDfqoyiFBhmPWu7h2TkCvgtVPW8QrHvrTdx6GNLf48sm47T9IQDwkbZt2WhLET50JvI0WkHHF26I1AGkugwxLeqTNMBjMWCLeEOBl5c_S5Bauy1QmJlvl8Y8dfsnIVKTAjAvwiaPwoeQV4-vNdCXA533_etUUx0KwkjaPSJ0m1q7MYnil-DQu1omfcDKW9l-FW-5Jg1AGQ0koicBGceSh8ejQdHxwSDNwLe2jbKG6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=vjozSV6DUoXXCCt2R2IqgV-BJ9gIp3U_25enJOqMQbNqiFEoS7bDbA6RIkPr31UzscZinxs_o-agfwv8NDyD44C2-VTzj1ICamZxCXBJDNjueDfqoyiFBhmPWu7h2TkCvgtVPW8QrHvrTdx6GNLf48sm47T9IQDwkbZt2WhLET50JvI0WkHHF26I1AGkugwxLeqTNMBjMWCLeEOBl5c_S5Bauy1QmJlvl8Y8dfsnIVKTAjAvwiaPwoeQV4-vNdCXA533_etUUx0KwkjaPSJ0m1q7MYnil-DQu1omfcDKW9l-FW-5Jg1AGQ0koicBGceSh8ejQdHxwSDNwLe2jbKG6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
هوادار تیم قطر آماده دیدار حساس امشب این تیم مقابل سوییس درهفته‌اول جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23375" target="_blank">📅 20:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23374">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=DpXW32-MdYmey0486cH9S0a7-b8HlgXlYVeyvmuj3Xh4GsGP2-geXg4txzkRcTDsZCRG67RcZ1kaIlLvfScQmWWvu3mTs8lPdYekRNSf1iWyzO2SKt2hAZAzAx2PDSncpg0QNghAirNqgMYyHJJoIxQjYIJ2d27NmJ_DYi64pftT7Q9crJqRTQmgFwY-XodLD_yascdDXl4wp4b7M4xDK5kYJfzM4qxuZlXOjuAl0bsamIqjJQXNIjOM6P6uIjLRwiRdW5dPV7c_LLtIKyZNb4Rv9svZ_0Hj45mze8BgoHbjWGYVc_F2WBPpT23uBETlqHs_DU96XqYWlxnmfYmudA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=DpXW32-MdYmey0486cH9S0a7-b8HlgXlYVeyvmuj3Xh4GsGP2-geXg4txzkRcTDsZCRG67RcZ1kaIlLvfScQmWWvu3mTs8lPdYekRNSf1iWyzO2SKt2hAZAzAx2PDSncpg0QNghAirNqgMYyHJJoIxQjYIJ2d27NmJ_DYi64pftT7Q9crJqRTQmgFwY-XodLD_yascdDXl4wp4b7M4xDK5kYJfzM4qxuZlXOjuAl0bsamIqjJQXNIjOM6P6uIjLRwiRdW5dPV7c_LLtIKyZNb4Rv9svZ_0Hj45mze8BgoHbjWGYVc_F2WBPpT23uBETlqHs_DU96XqYWlxnmfYmudA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مهمونای قسمت اول برنامه های جام جهانی
🔴
امیرحسین قیاسی: رامبد جوان
🔴
سایت ورزش سه: خیابانی و خداداد
🔴
عادل‌فردوسی‌پور: نکونام و کاوه رضایی و دیبالا
🔴
ابوطالب‌حسینی: علی‌پروین مادرقحبه برو دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23374" target="_blank">📅 20:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23373">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=dNO6gDeQy_kdvhye_U-ntm1A0L5UXIeKhf0FTeH3Fp91P7TtoIAf5VOChK2Ut4-ZmRoqlKELkv7iert3cJJsBD4TjO3Zp8GfZW0yfMlowWhIjmgiMexeYQA3a4DtHZPF-nOGW7f9UHvDaRw3xRpA2b_TNf-6MllkjKb3OvdJ-H0AUMHxJNcFZkoOdbFjUkBoZJptGJlYX2_NwMUFulaiL9rhBOoBNjut3BluNKOo7dqqkK5mr0Jw7uC8huse7h2yne5uOfjQvutv0b_J5CpGQgd9ZnU1GZypO69b3TSvn4LB968F9iYk0Jgi6ZpjqWGixxN0plU0NNPE0Deh1erImQkDSWNocfv-aOH95IIm011grGhm3f7ISPtKx8g-bmivij8fLM5cYP8HZeo4a39CSjk0rO3bPESi_hEJr_Bu3olB6NAY1INMTylJtzr13aRNSgOaLC70lQHXxI05eJuiCiKQlKshXU9HCTWYGcuyyiAm8i-k9oCGd_dYF3ERajypCChhSOmdlcZPfyrBd3YTjcszYSQh1UKQvs5Twg4o6fwErfeZ2RTrsd9O9JMz726bzrheDhSu_oL6AshlhHca7Sz7_aaFtQsyvufUB8ZG7Jjli1MxSi04WuRaQlmEuZn3D02FoeyAp9sCLDH1lrJC7Re0OnKRRFrd2V1wPCls_Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=dNO6gDeQy_kdvhye_U-ntm1A0L5UXIeKhf0FTeH3Fp91P7TtoIAf5VOChK2Ut4-ZmRoqlKELkv7iert3cJJsBD4TjO3Zp8GfZW0yfMlowWhIjmgiMexeYQA3a4DtHZPF-nOGW7f9UHvDaRw3xRpA2b_TNf-6MllkjKb3OvdJ-H0AUMHxJNcFZkoOdbFjUkBoZJptGJlYX2_NwMUFulaiL9rhBOoBNjut3BluNKOo7dqqkK5mr0Jw7uC8huse7h2yne5uOfjQvutv0b_J5CpGQgd9ZnU1GZypO69b3TSvn4LB968F9iYk0Jgi6ZpjqWGixxN0plU0NNPE0Deh1erImQkDSWNocfv-aOH95IIm011grGhm3f7ISPtKx8g-bmivij8fLM5cYP8HZeo4a39CSjk0rO3bPESi_hEJr_Bu3olB6NAY1INMTylJtzr13aRNSgOaLC70lQHXxI05eJuiCiKQlKshXU9HCTWYGcuyyiAm8i-k9oCGd_dYF3ERajypCChhSOmdlcZPfyrBd3YTjcszYSQh1UKQvs5Twg4o6fwErfeZ2RTrsd9O9JMz726bzrheDhSu_oL6AshlhHca7Sz7_aaFtQsyvufUB8ZG7Jjli1MxSi04WuRaQlmEuZn3D02FoeyAp9sCLDH1lrJC7Re0OnKRRFrd2V1wPCls_Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل‌ فردوسی‌ پور درباره یک اتفاق جذاب و متفاوت برای‌عاشقان به فوتبال و موسیقی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23373" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23371">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/svlEClZuQjFuDFD8OCshJtvY874fGGReIz4eRHjN5021FMsTm_XiqiKeyqDPWo1dl0PrPmNsrW8H8847ygUYBmLr5qXetBmDcZ-ARYBZF7zTJnRPcYwI2t65Z3Mj7AsDXHDS4uWxKV11eQ_3y6i1D3kv4IRK6QD0u-SBcgkC5dP1oao3g5OAHWjrNkwUnFs18MI4JxymyQrc5kGbBoPFXUCvJCsq5JZGy6dM_e8MOSpll4Ey5XPY-NbXeK6V1CQ_6rVufvOsNxN9UID_3y0Q7gAUTmVKlMmrpA0BuDFcwlxmR1epJQTFu7s3E6y-c_PbfTcH1pvmXfT38T4GzT-Bww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qnaQi0bJLsUwiCxta-oFk6N9bWujOsCV-bLVe0A3-8Rqu3qb5ZGnrgWxH6xumrtLPzDbkB4Db8v-j16lHEpQ7tuJF3bH3Nnp9u7jDBP1Pz07wf_gYctzvmpKMqOr_9xvLTRJVdzmZlA-cWTFcSf2d7_dcyhW-sRxr1WhyCN52ZKgqqP1O2TVSMAIwg-Nx1b2Vr6jyANBf11p72yjIVUgahkEEFv2BxXg8DV0lbDUdJQ3Dh0O2xsDN1ZCTIRE9HD8bl6CEqMbvhKgnt0jsXnpbt5eCiiCeGkYz0GtV9bWWLxz1JeRCs3fNg9in8O__GG-zZmtKGNG5loxxzq4R8uiiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23371" target="_blank">📅 19:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23370">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYEp7tBdJEmpB2Y6gxLu0uLGZhwz4F1NRLkR8m3iNfwUywmoabTtaofdFJLjk2xJPqAlKG7QzudzCxYzCJZEg0Ml6womTZ8moCDwIqzq7KWjzqon_XrC7Mo0JBxd4l9z6f2vsx-wgLCf6eI7Im6AqG7RoQm-Nxn6C9MDU_yzlvh4tkHF6T-2Ebtxqitk2evInkG5ioIvhTC4eV4bJ5H2Wcdn_xyxMgQgraMbZyqMWrJ6XnxxFIzJUELztQ7QPCkzN82fXdWRzJnmrA8ZfrcZzWfsIBCoQybdIhYWszI3t6ifcidjxOL4jE6T6rlL5iYXvG8bOxaj6MhJZ2ZOdcBNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23370" target="_blank">📅 19:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23369">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcV2V0-tsb9iezAyG0SHwbKTIhqnySMPjbkmg5Zayqj3wnBx3YE5nCqTqZGPSHQBUab0i-aQwdWWT9yKfetA_ohPGB-C47d_6zhbFpL0tmoKwZkwL4qu6Kjrs8Tfq8IpOtqUKb5Men3lSCbQoymdQzIhMZ-vx1jZ_alsZ9gNej7Pyxq3IZsltvBGf4_a2MZUKF2z3BeQJGgxBSZIUIPGlhoHiOpxkNYWN7RhnFl3yd_VN0EdYX4nzrr4dwFxOdQM9zh9TpbbBoKuHVXINFB2zkrQ5_qMUH9ZLfwGgMaXbtIqbFHO3d25weilqyOj07i1zX4b8hDIAxK1VI9EyPhWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23369" target="_blank">📅 18:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23367">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p5qppO4R6h8ZjAcqPj5-z1S_6RLCl1dMmcJtXCYVnFwSJa4l5aXRebbkOb7O6BKhNhHtxazSasFFXrei_bY5WUZWbD7Ub_QEES5t5TE2q0bRCs_nnvwUQcQtrl8WusGw7T1moS6oKkRm-7bvps4edlwEPTbxmzT57g38tgkv4Aq4K-q6NybHBppfYLyDWLT5Z67NvOxw5QQqqzYRft7jqX1CNyiwWw-xSdVOjfZrUWZyqOH6HaRRGvaKCTCW9CP4toQMafSvW_rpZBp2rLS6ToKY-n2QMjFzRt79v4CrgFLSQMEm99O6iUZ8XlXFp0sh1eBVgX_4FzIi2KSB20NUtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGCBNqN9rMO3gTJJxYWM49oyWZvn7FKkBIoMCo0Uu_cY2JJFY12E5YV1Ifx3v6jqoYEmwmmNccJowwOtOFf2V6yKxEr0lixf-kQP0prMsDB5Zy2kSNHe66E1uo8WcGSAVs5Kfmu9pS-yb0vJ41uJozWXoDHuNhuC0W48E091gh-_3nANOTF23zr3KOeZRxT_gA6m5VYWmZxPnXEKIm-0iDV5yEysFYM4sVhv6yo9AJDEU4yBoKzeJzg_CsII-bLbFyTfBYBeSShlW5-6slBNfyaIULL25RgFZ4iDrscY1AazdYxXonXyRFleBGRjhx2PBsOGeXH6yIASL2I991LTfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23367" target="_blank">📅 18:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23366">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFaXMj4muTAKZk-b9Gfsi0KlT5Eipmv_HE471s0xLPZSL2d66mHp03TiaH9p5KlUjt72mZMtVexzZEDkWYLkwLjrwdrhJSNdESX9oHCkxPcOtTSNG1R-2MvPAgf0SKtYbUzqBIcT6TJWSQwhB-Xg97tb-DIzBEEUjbTjN9dYRausmYcXUiUrtFrjK_Nv_cmrVZ4u9z6JMzFntvy0wlsEritBw3r9cl8SIvwNSOOebXozEKEbH1kRM4MJgY9fFAVVjbttg9LbzKuK-_lXvT_PKkevKysro2V35xmoy06gMRg_HaZmywPSDlbBJ_9WREgMG6QMmSF0ii5oclvfuTwqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23366" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23365">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=qf4X06uy5Xp-f-AWug11-gUBBBzs3rXRTYXc8VylTkwmziBPSqN7QlEmcNfBLJYlBmnKvRe8PdSEB02v5WKyedfDIO7vHrAHvYjAB7z6EF2zjyyYgYRL512IS_nd-siGNIMKhRWu4S5BlLTYl7dmboccwbBgaYgNU8SmBYciOhCircupN7ZcYjxXQ7sr8tge6ptv1_bN_6wXAGfVYQOHD8hcE9QKirlsXlFRtcDS9qYCog5DzdPB9zQrl1hJr1plmHJ3wvNfinhmUF59GNe2d9yHVxFSnMlk7HVcaNT5uaPIGhbtrs45sJCtAA4rEKyL4DCIOnrnEYZPhnHTpZu0ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=qf4X06uy5Xp-f-AWug11-gUBBBzs3rXRTYXc8VylTkwmziBPSqN7QlEmcNfBLJYlBmnKvRe8PdSEB02v5WKyedfDIO7vHrAHvYjAB7z6EF2zjyyYgYRL512IS_nd-siGNIMKhRWu4S5BlLTYl7dmboccwbBgaYgNU8SmBYciOhCircupN7ZcYjxXQ7sr8tge6ptv1_bN_6wXAGfVYQOHD8hcE9QKirlsXlFRtcDS9qYCog5DzdPB9zQrl1hJr1plmHJ3wvNfinhmUF59GNe2d9yHVxFSnMlk7HVcaNT5uaPIGhbtrs45sJCtAA4rEKyL4DCIOnrnEYZPhnHTpZu0ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23365" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23364">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZmb-3PNIdb5vFUsV3R56YDNLg1EkSsSAeDmPsX91bdfm4Nn3bIoJJ0_V3av94GhVcgYsrLKrN4t3dM8Um96LWYa24UNSEmLwIzdjtalMgOEXEtICs7Hi2AibHrv-cDPryRTAVOPl_h72fwJc2oCEVT7QjKtxhGcSfaGTjXdj9s36oArBdmlXcAjHJxVNVp421tJ_tCW8cImql1ppqT7epvosmDGxfehPPBC-NtDSfdQ6b2hMRF7ZPTgvhHV84zMmWN8rTMSDiTanUlRs0xWiyJTc82sfFfFYaILXRYsE6ZjPO358RGLjUKkzkUTa36ZdD_5kyD-J4Y4zqpQgsPQ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط یک پیش‌بینی تا رسیدن به جوایزی که همه چشمشون دنبالشه...
🚗
پژو ۲۰۷
📱
آیفون ۱۷
🎮
پلی‌استیشن ۵
این فقط تماشای جام جهانی نیست؛ این شانس توئه که از هیجان مسابقه‌ها، جایزه واقعی ببری.
⚽
پیش‌بینی کن.
⭐
امتیاز جمع کن.
🏆
برای جوایز طلایی رقابت کن.
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23364" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23363">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_z7LQlwuSy-OdQU98jTbcJYifL6r36M-4JSovxSyrqqhRQR6HP9adhzS3lSNVcl4l0MLks8VaRmUksRMptlLhAquHMJr4FhX470xCq1T3kpulkzHEIZhEvcXKYfeVItH2BWixK0RBVkw7Ov5Vuu7J225jAzU4l3-Ur2JL1pRBFwco9RcrYlxC3eDd-9uLTJxRjBlndDwwM46xPMtKcf7vKuySPbv6r1R7JwA2y0ReeNrUJze7YMWLqMs_rGkUkHy8lBzBwX0FXEI1L_puj2m1GgkXT1jDV_G37VzV2HDWh51nz3SsTRZwdjH53XRKumhu0ohSos-eLNLAMtoQP4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23363" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23361">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jo1czyngaksbiYH9dY4cBWT4MANs2UAkx7xhz-lUGEUmwpqTAuy3j6CTIraAsUBzTZ8jrQK_I1xMwKRFJ4Coo7l8ETrWQP4H71UYREJghlqxRJtirllZnVBVwFuQwLYxzL26-YcAEsWxt4JloOq1ukoZOgWiaRQI5AOWP8CpfYalp2NQB38RTQPgpwb3C6I0GxbL7iE3Ct4o8IdOEIDVGWqvoZ4fZc60taG7rhZekysyidIqDUxh78HWsP3hVrkunL6E7XJcfk2AFjscR7Muoj1Jd_lwdJ4uH9PaoAHetFLMuiimUB5_M09Nxhg05ZwxvcBMJBfl5JYOdSR6xg5l2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23361" target="_blank">📅 17:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23360">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6GID6us1Vk84Qhfx1xCe0qK4mEzT-fjhZaj1R8OvFXyleCLzIZh0_sLkNJ2tgyUvL8Q4aizyMa_tTSREtgUHEINP3V4YHg1pHyj4aARpUGmjcpSSmXhvE2oaWyvXLuLR240hmmLmWgiJyAx3MJrt8aRU92Tj9Aebw_hIiyL3si1vUFu9i6Z5GKoifcnTaKA-awjK6b-oduEBxug6VlWwpCP7QgEGBVBuEcpKO_aA5G5QA5gTBIfT2GQBHDn5f4gYEEreYEZAKE5j-kTuRm-AB2vsUsx0ZpS0STs067DdZfygv7BiHsMdDP3qKrILQ6qVQU-6el_46MOyQpxJFvctg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23360" target="_blank">📅 16:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23358">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UE-hFuSwsCax1QzRI7tNMkox3nG0a3b6iGxDntUpoei12u_k11Qpbf-KzmThWTx6mqYeAKD4JLHd_wVG3uTrVELbW0JMxSoKzHOGeJCVfC0uVBgDc18l3bBU_MR5lgYEnhU6l40ohdmcUTIQP2PoaITlrC-uQ5IaQzVdM66oF0qHy8uB0gHCemD2zLq8CNEsKNTmDKYF5gnrtRmbFP9HwoPG2vxoeQ6YqOyYqvemGG4_YjXuDJk_t7vaythDApXoDCFz8JQUx8G9ZmDzg06Q5YhfxeLYIjWntRrEPaK3ia9rXlaZw4iA3vYHqWAD3BKnHlCe0fFmxl1kMPtjnkR7lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WxT5p-OUzf7nd5XlUDhZj2hDpw0ENysmtTRI4-0wpwf5ntY1aM_4kkVYdjNC3_7Suq2-luN16WW5PBqyusmitCDzAleGaCwncjgTsfnddVx5bleVQ8NVrEO3XUcfLg9Z-Fj7YG186KK5alUBQQVDGu-Y7iPUurDV3MwacADAqJOeZmlGCMKPMO895TWst89zZQWFDzqPxWTIEQXTfZlicJ6oa5vY4XsQVGDsqt71veK0EBfm37HOGe8O3VqS9OxUm2aZ5tYdyZSHFYE7MXoEGbwEYbWEfjfbUu-AR1W17rj92eYahNuBsq0lM6FPF40KP2Bz9paEI1r309y_-1BneQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دوست دختر پسر 15 ساله کریس رونالدو: من رابطه‌ ام با کریستیانو جونیور عالی است و شایعاتی که منتشر شده کذب محض است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23358" target="_blank">📅 16:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23357">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaEtJr6mGhMwUncMfFhcYehYT6qb2i2BGgEkmuIYBOZToVsaccbT_PAiPhMOoUZDly5wGMIw4EPLai4NcT1IytFvXPBk5zIoQzZLFus_DPwYp8QGYdk5hXgoF4g90R1guBellweYj5USigJetN78dNZGpD118qB9DUpEXWEkVFPPcGUouXvOGNLHp4u96p0OycCgs7EzJrzNW6GR6KJ4beqOAazQ0C89Txqsos2nFDXuqRojzj5s4nwoLRFHLF1Q2bye4zV643Ubc2Z6FCNgELzEiUXgqdOjPTGfdccdlh7b37gH6OSOqbFotCkdqLHI50goYoeZAVOrSa6bvAnPiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23357" target="_blank">📅 15:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23356">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFwE9NjJREBiwDvD6iXvF2Q-OImDWVd4M6BtfmOcLW25WR81IFjKOLau0DxBH8eaSarSOZHo6Y5vgC_pKGZ5BQ3zRbWUZt5DE48PsOgGprZHrIXiXLzA81zUUc-ZqWMJADRtNLgIKFcfxzMABMXPTQ3_Q9dRSC5OVn6d1Ydkv3Nm5ERB23ZWpBAML094H6rYT7HXHblGorxDdFFXTZqC1hnAwEBMriLeRAqDNk2Mx87Wu_G96ht2HOvpB329_jWzNL4XUQBkRqdLstYLoidVId_Vw_blvnuAVBQAbhm2jsQcruWS2g6FPJgorUY341z0f6oPSnLpTL7G5T-D7pGFYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23356" target="_blank">📅 15:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23355">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtX6QOpjOZdLxmpv9ttbQKvxAMLtmIo10R1sbAOosSapmx2EQAqLXqChLBw0boZebGRh-Ah1aFN87nHzYf07LG4Tq62SbFAtM6ejGGPWmzzDzhoIiIqSq-Ugse17UXDt4--VeTFgraH2uUgL3XCEl7j4KFSWRJNUgMIDxiKOkpDakTVZ93kvFtxWBWKHgGp5MTY_xJ9KbQyA6EU9KKbYvyrX7Lr7SID-EuGNDp3-5fRcdGM0cbFFC408DvZwhcvJKyrRnsrxGqJBeP-foAZweQqd28tQWtdTf5tbVpWuD_4Q9eKzUYa4PUUtnzkWu4Fy4yBpBkT_7CgRThqSOVKUfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23355" target="_blank">📅 15:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23353">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FWKBZoaicxsmwAsjubHOib8CH0mK95tA9iOfY-LVO9TpuWWJMQ12AE8Rkz4T6V7h1UKWY0pQtBl7hgvSIMnMhk_umnv1qrt7H40IJ7HdVxeeqAqiJixwQ0uvXlbBmZqDvPl1YqdyRA9jOCALioX5SRRGyFE1OJLmYjpzmxkentavW1i39jOL1xtjSImsnLn1HBv9u8yD4BGoqpaoE9pmz0aGvVzmH1o5zrouN2R5ngA2nfkBYiaarhB9cMG1_evwmWaZkFt81gWEUy2nNkvW5dLYmIadQs6CaTDchmuOXql-CwjYV6MY-gwkNyYt43UWslK2z1FHepS1yyq-oncxew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKTMLj0pcc0x0tlnC4etdnEcyDV2pP9fZPcNQX77SosCyWmW21dAmAx9ND7VCBqEiFmDakFRNpCMtx-ocfkRzZBi6USRvhkwyoY4E3eC3mqsea0r-On34kLDIHgyRhT9QxFsCH7FYSG1f3h_tl_0kmJ5dAtq9RTeoJaGmPj-Vor0f_mH9h7BDr71aoKHi2aE6K_UqWmsD5ynMBw8rxkiALkoVmPlY_IZ5OBxQMvplaoVwwndriBTbknFa6fUpYplMsBofCjZNrLidQhZ_yWk9AJXJj05k_OoeaVM7QTiEn6mz_JXpsmtYOI8GBLeTzAynBJofXd7SQYcycRGJYW6MA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نگاهی به کارنامه کریستیانو رونالدو و لیونل مسی در ادوار مختلف رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23353" target="_blank">📅 15:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23352">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fho6nasuMVmq2RO52J9BK4SEt4bT9p4Rl8Z-Vh92TE0LNKGYVIX8N9CX6rEJUqpIY8sbCqn3ErhW3E2-uzEpV2WlkxbE4d3pLB_ct983Eyjt0kaWgJ8EzzwrnzAN9tSMR-Udlw0jqqwgEvUKNrnrqsEW-tdLg-eEmCJoS78yIfdizQ-1WiZ2pt_bEyn_lpqSvMG6fWuNPCvxVaeqa5mD559m0eFYKUmgnBFqQ72zbA90DSr-6zwX75-HOIpk1lDhxak4p4ZApW_l9fJvF51DB9t1MTp3qXzONri9nZ3Mul0z_sS3uKyie6NVyvwuvU5lwkOiBJA4T5XUYCyt2xkl7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ‌ملت‌های‌والیبال؛ جلسه‌‌مهم پیاتزا با بازیکنان جواب داد؛ اولین پیروزی سروقامتان مقتدرانه بود.
🏐
ایران
3️⃣
-
0️⃣
آرژانتین
🇮🇷
25|25|25
🇦🇷
23|19|23  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23352" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23350">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSi8tp3i8Jj9G6uGJYApTJYL23dBop4VwhQs86fjzdcSkFQ3uG8pYu6P-ngLV2_VceyLw18sVskYZPiTD-1RDA0IzCBYysXpfs4UNPc8JKUUklsaR7oLXivvCMnTR1faMSQ-AZrRIu4bWu3a7wu0FsWvbI2idfz05J-7RiMnEIbeMOl5iFZ8KbUekSRmMyu2KwKytKnJu3U63LpWovuEwkbQerpP03K3HYSeQcwCvraM0gfLv_pLrCeIk0YaddmFRxi7TxEMu9W4TWPwoyCnZE2twpvmUacR-C5-2KqmfIky_6QpuTzCzOGqAmMOj2194dm71sw-qOYlwAGiltwoDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_CbEVCorRlbFtwzEKV_qK0bAAMgd1wK3tUbtRac9EbvA-udwiJSSTVlJs7lLNRtHjU9-h56CUdt_-ISPfCnZH4indPvG6iJjAWXqcGTAjlD_irnKKILQ1z3wnfDpqEktiV9VC5F0ED5xQ6IN0hPCptyLvJfG0lGdvwR7HCbv5XXKKRWp8MpLcPwIs8Gv_fDTw2xExmWc8D5eulnZFcM4UYGEek5aR1ttVZJbD2uO3bwGgHJhfSk5fMOgoiPHcHW5Vwrov9x-lMG36bG2bNjtZ6NbHA5ciZTsO-nsDYVqbJYYymfPsgkDuijHDfWKfVr8NAcAL9K9bbWeSd-SCMbNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇬
گزارشگر اختصاصی بازی‌های تیم ملی مصر در رقابت های‌جام‌جهانی 2026 ایشون هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23350" target="_blank">📅 14:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23349">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az_Jt1V3h_pqaQZBJ65XlzNVSvIzBzZDOPsSLnhO_cyy3ieksQk-c7T_Qmg0uYt0rokrksJf2sh0AThmQRmt6eMDoNOiEVSgqc8OjSVSrO4lMy7RqWwZpkI13kdn4XwSW8K7gQA-1TIfSceSdZLaYm_6-AXJx8uLbUUR_nYcZAUiwPEQBKZON1LFo10GUMc59CpQ5xPRYwXs_pUKMJHq3fK2JiKDrBZAEC2tlthPqEZhJao9BqaWwFuOnnH-V4n77qIEles4TzWnx8dC6XUkkm8le6CjFeWSHhZnn10vtf0mP9vBKjWTBH_7ODlDR0mMBW9XlCh-VD-y0tk7kZOlOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23349" target="_blank">📅 14:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23348">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=tyz_SSDTSXTL0haQuBpMD66GGdkL10WtkWSQvqHXL3l2sQgVqQQGiatLsihUW6IjDCnolu-SE4SyCtG1tZ5FshRRtMfplCshKKbHOQI4cPkFgOUYsWizSMx02OWn_s3BFfsGIvs1d8BJ_-4WjFF1qF89STpVlIsXpu-MmDWYbLaiib4LiVauQIl57DUAQi6pf0-CrH7bbQ7OsP_stZk9Mp_UPTigL7zFTVCjvyAuy2byWtFk6MlRF8YnTIuCX949NvMikfwyV1aucSMTwzROzfV1CuuQqA0QvfyILwjd_Ln3LjoY_lQflnEXzE0X0OqIN3Bl6jja8jn1m1t2o8VACw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=tyz_SSDTSXTL0haQuBpMD66GGdkL10WtkWSQvqHXL3l2sQgVqQQGiatLsihUW6IjDCnolu-SE4SyCtG1tZ5FshRRtMfplCshKKbHOQI4cPkFgOUYsWizSMx02OWn_s3BFfsGIvs1d8BJ_-4WjFF1qF89STpVlIsXpu-MmDWYbLaiib4LiVauQIl57DUAQi6pf0-CrH7bbQ7OsP_stZk9Mp_UPTigL7zFTVCjvyAuy2byWtFk6MlRF8YnTIuCX949NvMikfwyV1aucSMTwzROzfV1CuuQqA0QvfyILwjd_Ln3LjoY_lQflnEXzE0X0OqIN3Bl6jja8jn1m1t2o8VACw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
اسپید یوتیوبر معروف در حاشیه بازی بامداد امروز آمریکا میگه‌ رونالدووپرتغال قهرمان‌جام جهانی میشن؛ زلاتان هم این‌مدلی بدون هیچ‌حرفی بلافاصله میکروفون رو از دستش‌میگیره‌ومیگه برو بیرون بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23348" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23347">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j__AGpJXQZ86rGBOkUt96tjwHSqRu3-G09mWhL7bEntQnQ-ni3TQX7V1A0MfX51F5yqyBl2mHSlScM73NA25wPr7ss4YTCUP8J1fqk8BItfUg0N27oth4sSN45OntC_x_fLweyPbP3ygS423xaxX9wS7BVs-tX81xDXD3kbfid97_2c952N30Q50krhokN0luoNm9YxPjWRq3E8ILNGKvqEybqcXIlvpWWFhSIEIO_PqmXGITDDyYrSAd67m0ml2TwZkzoKs-2_8IFnd7SBx2cfpl-L5Y3Wf3A-LDfYcn8xxcHg0WNe2yWwrtljquihvkel9pvkaCkt5wcYGEWP00g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23347" target="_blank">📅 13:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23345">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SwtXwPVTezh6F6kRA62ctMvmL7f1uR6CaJzE3HXYltO6EmvscLG6zw739ynb4yfEALmqxKFecRBlGXYgIUsiWR9K6XA73YP85wmpdnVOmCJKzCuTLx89EJv0XNeJgI8Bt60pVgHNhxuJxN5eahnuob75N0NiBAdfVhmgut5YruE5mnNTA59kJyTnCHgUAxPbr6_2HcsGq7bTYaQR_guEO-_ScUHRJdhZE66mzCfq2CFDuR0gZmNONxCwa6v-WUhinWfesfbD1KTcNXYLflNFTizpfPwd-nqKsOCpej-_exAaq6vNNBoJ2Zki1fxbU6fiSX3pO17-TGv13mjb1JmlAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHF9hVH-JHNwgIS2qGp_TDYspPnNJ6RxmhKn2_aJApfR7-xKbyWy7tHKN7kaBNpFGk7xU9i5GbvMIr4wRcLV9EkIXPSjqUuPJXVxbLLea8T4YH_080bJLeTu2BcqwDEsohbqi4BT8Daub4fSDHr0DMSu0ovvPJviMEPoHAZRdc0HBUspxvTtDoXNEW2_hiiHQ7IRibFbb82P-HWMRgBoXxfs15kF4tP0dVFMqX9H5q0jTuZw8n25Ke0gCIY7mMM0hIpbdDGKEMZmhwBI9hy85XCLjeTLJVnD0p4CsGfxwKyP8mF-NKF22E1co0VM-Cpc8qoHmU9yZFfPfUXMQ6VPFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرنگار معروف باشگاه شاختار: بازی دیشب بارسا و پاری‌سن ژرمن فوق العاده بود. انریکه یکی از بهترین سرمربیان حال حاضر دنیاست. همچنان معتقدم که باشگاه‌رئال‌مادرید قهرمان این فصل لیگ قهرمانان اروپا خواهد شد...!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23345" target="_blank">📅 13:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23343">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMkO3SkRDhB-OCHKP6wS-Y-0BTemRPT0U3oZi_rLTJHeqKVP43QaRIOPn8YOUF_-H2G_nNeEwjO0ToKqDThsR93W5cKd_KNB-UWd_AhsIhm6HfFSnRVpLWQahAIRPNVr-zt748xmiCyMxP4aNaODMtXpKoAWAbenHlyqmRjDj-Yb97BnA5e6wCxEiC5LYwLwXoCyPFyqeyEXQnZmtzLcgBqK_GgraxiTBO7xsVhNu8I64xFLdJIGe_38JAZ-6avI2a--X1JUOaJEmWENosl6qqF9vq8MHWp_LaApJamLpuxSCzI7Vls9G0STtwTh7Ahj0ZOyJfc6msFNuNaxxAa2bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23343" target="_blank">📅 12:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23342">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5uLcIu_yDE-gi6gllem9E14TThkn0WZohem3MioJr5g1x6uC7ng60l2cXDT0YjO5ROdFQXn-RcU4xxkQNlowHww9yGXgaa7TbKEr5XqW-NEel8KqkdEaoa9lPW_Mp2377AB5MZ4INCprBbnmQi_IY3k2uttzC0QVvtLAwsid2DQUoNq0IYyxAGOm-vYwQPkW-n6S4_tT-nPXmY0cC09nzdbneLA3o5qnJMVZzSq9Mh82Jt9eGJBpfoBcsfarwhzjom2m37zsJIQaW0Zrhn6k-vyx6cO_SPEXwNfpaCUQOk76WBT903X0QWUlU50GGWvSvnDDjLo--7R6eqlQX6djQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیف‌وتجهیزات تمرینی تیم ملی انگلیس در حین انتقال از فلوریدا به کانزاس سیتی دزدیده شد. بنظر میرسه که هری کین یکی از قربانیان این اتفاقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23342" target="_blank">📅 12:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23341">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlyo_ELM96jGuEFqBhrKJoYOwXlMLbB5x0Rg1FDaslB2cUvdqknVRs4-sjllYChAdjAaqSon39Ejztotws1qzb11_tnxGgIDXPD0icWkgGkb0N_gO_fKo3wzG4to9a-WvAd7kV7FpbjwuUNGgtoYsIYRvuOr983EaHn6IlMb6E6TC39DtfoZIR0RnQ_UVnIp2l-LZn8sem5ighQsLIaRwB5AXoDvSlQloxQrtMdbbYoxeFAxi6t-_CRgjZdQSeS3U-uy3vw2NECWs5boFQytJw_PtqCIYCjRMGwiclHDvVtTqaEsQQ8a-ftM_mZgLaFWp3FmgWOPFRdQ-VJ4SEQ2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه سپاهان برای فروش محمد امین حزباوی، آریا یوسفی و مهدی لیموچی روی هم مبلغ 220 میلیارد تومان میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23341" target="_blank">📅 11:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23340">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti-Boz0NPL7wePgGtGmSZz-VQfcZvdXJ58YKy79lRfrLhOp5C18W4lM8j7pyG7ntoPqkw7nDUMoAqIBPB7Ll-NPuuCoSun9xqQRqNmYHlNseWhhJRQiIlQ75I5WJQIgF4K2pg9ZEg6Nv5IBUZKu6H7zlp_eBsA8scsa8GcE18i4E9QLWZrHr8IScFDPTu62qLlm0Fp2yjEsR7Vekq_MbwW5pXFFf4IJ4oqok7GxsEJRxiwmXeDGYR5R7xGHLqs1vSXwmueE2MlkQQKHKW5uWoaoPh_PljEkd-IEcJ3WLYEIjczR3_EFAXRG129zSxKyEx7mmgQRXqujZ7tNvdKCG9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23340" target="_blank">📅 11:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23339">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEit5braE5lIbPIHE7l3WEjaveBFi3UrT5I5V4hGqPwe4tRNVhXcJc2U9uOfEtRuz9KwQ6BJcR_bf_M7kGkAx2jq-lRhFz8wPmKGPyESYnYAq3AK37eIWENInXmwsLxXGgjGDuVX-Qn9NLZ5Q36Boox5daAa9lIBw1pVlGIyS9KMUGn0dhLuOT0Q28oR5Tqit4tqQDsKfMUayOrUaOxpXOuokmq_6EVviO7FQCVKzCOtIGWrD9q4kgyz0gAS6dlUbxJEPdM82vfZZlwyoR5VdNOsmvelUi4LV8r7-4-w9EkS1jdKamhPJjFX6QgmmKFbY2qmOKkbpAyPwbUe1cbibQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
10 صفحه برتر در اینستاگرام با بیشترین تعداد فالور؛ کریس رونالدو بعد از اینستا در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23339" target="_blank">📅 11:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23338">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lsm1OZef5ouSoHIuI_adsf9PmT-TRydiLkRLqDEmyx2FFnxbBHX3WpnJZN62ek2xp6wtv77waitwvQEcQ3AcER4xWt1dDbUQe_9hLiJZGkaCsYyIgWVMhb3igSgyqWF7R3nDupI90U4bthjmI4xlxQs7NThpKxIJq9DFU9TAYWUL7gKq_sr7XeOsWrAbyTNsuBlJvx6RdmwEieTrTI8lbDIc-gO-Jgb9mbYbea8GViemWP3N3Nk_nQI-KGSP6lgrWSS5e85hjQXnzJNwewy2_1Li_8rS2PNAnY-DzLDIzBhikeNylYZrBrq5uJ4dM_EzZ354c425NBrS3VrsAuce0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23338" target="_blank">📅 10:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23337">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAAOjZNiSU9vjq6DEg69AVzcOM8bZo0NFrObV_xLHAoBl4P_e-NFF1B6KKgZ7XNer3XE7azJCqfun2GSrzgbHLSmFxO-sV1cBtGEwDzY7f0_E103NjU2_Oj8iqwF5t06NBfa9b9otzJLi-4Xln5QQHCHRyJB0Aqzy733SpNvcU3cPsc9zCcbB09ZHQ04SfMJdZubdDErrzu5z8PvykcVoeRbKvCNz6Aq_OVToM-6YlkY6qJWx4_s2g4X2SHrWfzR3AwVwNEqTKpo8d_7msFqBTEcNRTI-C4kws5F3Ojs210Zahc_nzY46DjtUbTbfC-swnzkJJbjSHYBxarkChXzkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23337" target="_blank">📅 10:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23335">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29987e4127.mp4?token=FAFzfJhejljQp6dxcG-4ErmNopz4KxY56_DCBx_P1j_mHMxMKDnYkbqBVY8oxYrqHr8n9E9T9L_ZQuao2gEdy3muLW9tE5JA-U3sxQRxybQgU__rPfA6-VYcRg4G_Y_9kDDd9v8UaspAonAdmtDI2ds-T9F1rYtirSOQz_iKV7wVAwlePzicwI1h7U-7bYFRT1E3i8ou7QqplwWQvW_fio5usuO1hQ3-tMIJWk4G1yhVOlnsBCwLEMjcSJw6qJEP3vS0M4vlrAHmlZ5HsT5bGy3S8WVVTXoW1nXRfQfUv4wsB7UUjK2LFFXudASYsB-9CRpx9uyGdU1gcVzYd6OFXK3g2RBg2osFfqo4VPXvGGeqXAvPTIH8xXQIGghQSG-RGLH8Fyfw-RzHLHevDf8tbW8IDl1tZQ-5jNOICSFUiWFW-aZIQ7EodnDHdSetxvVNKxddjaEJpsfPcL60L8TiVIGwXi-6kw7o2egsh95lRYHjN_u8le6o3CObm6xoRsOUn4KOAM40uEyarF1uPlLCMnrJ9v4jdP6irTtKLhjLHeUBpqBLy06eov0gc7-WfGxhP0bPkFc5GmK8S8cE81cP1Wck6QWXPuz4go19Wyrbh2qpCvDxbJDYKSaRg90cbF75awRMTSxxB73s52KrCshMdywHU9c2DcLD8k6zMV6U4Oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29987e4127.mp4?token=FAFzfJhejljQp6dxcG-4ErmNopz4KxY56_DCBx_P1j_mHMxMKDnYkbqBVY8oxYrqHr8n9E9T9L_ZQuao2gEdy3muLW9tE5JA-U3sxQRxybQgU__rPfA6-VYcRg4G_Y_9kDDd9v8UaspAonAdmtDI2ds-T9F1rYtirSOQz_iKV7wVAwlePzicwI1h7U-7bYFRT1E3i8ou7QqplwWQvW_fio5usuO1hQ3-tMIJWk4G1yhVOlnsBCwLEMjcSJw6qJEP3vS0M4vlrAHmlZ5HsT5bGy3S8WVVTXoW1nXRfQfUv4wsB7UUjK2LFFXudASYsB-9CRpx9uyGdU1gcVzYd6OFXK3g2RBg2osFfqo4VPXvGGeqXAvPTIH8xXQIGghQSG-RGLH8Fyfw-RzHLHevDf8tbW8IDl1tZQ-5jNOICSFUiWFW-aZIQ7EodnDHdSetxvVNKxddjaEJpsfPcL60L8TiVIGwXi-6kw7o2egsh95lRYHjN_u8le6o3CObm6xoRsOUn4KOAM40uEyarF1uPlLCMnrJ9v4jdP6irTtKLhjLHeUBpqBLy06eov0gc7-WfGxhP0bPkFc5GmK8S8cE81cP1Wck6QWXPuz4go19Wyrbh2qpCvDxbJDYKSaRg90cbF75awRMTSxxB73s52KrCshMdywHU9c2DcLD8k6zMV6U4Oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چالش جذاب هوادار ایرانی با کیت های تیم های حاضر در رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23335" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23334">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c684a93218.mp4?token=TRDMelbpk_bzVZ5C4Ij4I92HFcmnOb2x1Y_Rlq487B8Lgsp3J-uhUZV8lR4u42-nBgNSSMS4ov4YxvnvA25FdlSMOJJ1I3nQNADOsEoBJh90HXi9WXXBagyxTHEcyye5TGLGs20--5Fs3mndBaE51zQP4IyItogqNKwoejFUGkskEkeUYuFbBss0yL4-64WuLhQUpnXtMC4omGRsQFzaYJ2teD0L6qtyhYZCeHsaPZam-WSHqvOiH6fHTinK4kpyEhufka5Tpcs8EPKleJmDY1sw4GBV5ZDEuPwfbqV_mRhNLPmEDtyOVbQT5IbHHlFkdHef7jHso6DmYgw4b-UO_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c684a93218.mp4?token=TRDMelbpk_bzVZ5C4Ij4I92HFcmnOb2x1Y_Rlq487B8Lgsp3J-uhUZV8lR4u42-nBgNSSMS4ov4YxvnvA25FdlSMOJJ1I3nQNADOsEoBJh90HXi9WXXBagyxTHEcyye5TGLGs20--5Fs3mndBaE51zQP4IyItogqNKwoejFUGkskEkeUYuFbBss0yL4-64WuLhQUpnXtMC4omGRsQFzaYJ2teD0L6qtyhYZCeHsaPZam-WSHqvOiH6fHTinK4kpyEhufka5Tpcs8EPKleJmDY1sw4GBV5ZDEuPwfbqV_mRhNLPmEDtyOVbQT5IbHHlFkdHef7jHso6DmYgw4b-UO_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
بازیکنان‌بایرن‌مونیخ چندسالشون بود وقتی نویر اولین بازی‌شو انجام داد؛ منتظر کارل بمونید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23334" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23332">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLgBRwA4ji0vr075NguyVk1-UcNt6UOxkJKfdmMNQVEVGji43g8q31dB2ZioRl89MoTvtzkpW5V7pEbPd2C5zPd88EgU3Y_CeaaQBvUmJ1L7gg9vRPrTtNu-UWT0Z79Dh_GLs2xAX_XA4mDI3js7QSQChu10cSHZLqN6SVmr5dWc5k25wQKMEpD3NELCf7YU1aNdqfZE1Ri7LknEqXjPiXhfdE7aoPmBH_nBqnlIjzcQFjnOp9zdM_32gfjtERlqf9eWQiEQNa7iad49uiPcqxioDSWxnOA5FFViGoy3VIsW1ReDjFszUgzOh_vdFeSNTNsTQozGH3iLeGow4L50dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ باشگاه استقلال طی‌ساعات‌آینده مطالبات یاسر اسانی ستاره آلبانیایی آبی‌پوشان پایتخت رو پرداخت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23332" target="_blank">📅 10:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23331">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|آتش بازی یاران پوچتینو در گام نخست‌ رقابت‌ها مقابل پاراگوئه
🇺🇸
آمریکا
4️⃣
-
1️⃣
پاراگوئه
🇵🇾
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23331" target="_blank">📅 10:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23330">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4oKfdOt3Lik_a7EGjXyHT0sXjoXhdcTHbm9nExq6jnjNbJSaQ1lcVP1tcRAkqvbjahN7SV41phuCEiq4Mym5nOBLTRc6xWr9la28ImJLODgu-dHdishmvpYHGrEqMsokaSf37_-ZdMAC8PRlcGd2o99kDYLZFcr8tyu7z7XnXAOcuIUXA31zsScFwOW9YtGpMxLJoX3dRM0pLrapZ6z05wngg-lg0pigqSIoFjfWpZn7wDKJJvxHlDHS_tM3VDSzrizWobFANtp07ekk60XYV7Tbd98uWbE9XVYG2b_R08oVL13GNkliLp02MmMe2i6jeca4jOTk0iwuQS7kBPG6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف یاران ادین ژکو مقابل یکی از سه میزبان جام در ایستگاه اول.
🇨🇦
کانادا
1️⃣
-
1️⃣
بوسنی و هرزگوین
🇧🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23330" target="_blank">📅 09:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23329">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=vondXvFagkyil4CfbPy3bYFLxcpMVkF66guNd7FJ09rSnLOc12cnccDXwB09oBGaWaP2tr1vet45SC7zI8IOWRxunWIQKOaZfq-Nr2xtNYHJpEqlEJhNTMuZQ-Ydl_1gqxvf7snUIlgg6v6tuoGq_yauixKxqO4_nsoCrXUSs6K3SF-fRqsrEKg9IaNV5C2JkgBRNsCJJWPDbEZUCTuudoldCyUkdXsm441GVTIzQpbIJ1jr24YxqwNE6Qp2RL8Y6f6W2Qus43fcWmkao_RbsRR-gkVBwLnZMUagYXc8cPeT8jIj3mZ1UMVX4pgqP2RuU4_MyAewhKooySimZS3RZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=vondXvFagkyil4CfbPy3bYFLxcpMVkF66guNd7FJ09rSnLOc12cnccDXwB09oBGaWaP2tr1vet45SC7zI8IOWRxunWIQKOaZfq-Nr2xtNYHJpEqlEJhNTMuZQ-Ydl_1gqxvf7snUIlgg6v6tuoGq_yauixKxqO4_nsoCrXUSs6K3SF-fRqsrEKg9IaNV5C2JkgBRNsCJJWPDbEZUCTuudoldCyUkdXsm441GVTIzQpbIJ1jr24YxqwNE6Qp2RL8Y6f6W2Qus43fcWmkao_RbsRR-gkVBwLnZMUagYXc8cPeT8jIj3mZ1UMVX4pgqP2RuU4_MyAewhKooySimZS3RZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تیکه‌سنگین عادل‌فردوسی‌پور به امیر قلعه نویی بابت ساعت دستش در مراسم پیش از شروع جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23329" target="_blank">📅 09:40 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
