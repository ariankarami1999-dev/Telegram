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
<img src="https://cdn4.telesco.pe/file/M1FT8c7QyAppcfNGFAocN76S4whyyv0zNJNkUqbnCB8EDfv_lTkjnybNV7U87FsLeEHzMLqev9P7gd3mUxL-NXox7mHQNvZbv6_4uKcSv5BWeRYoRmeB-ZdUmqgBBS50bOfj1Nldj_RMu-dn61AgwFqGXJVIKnjiLXjXfoYvZQtkHVsBIMuH8PX8Uko8slLtqa-kvhrhcvZ9o9OYBwY6gV2j1W9zDQdIKQ_a3e_MmB_kZmCPnMdZS-qZZssxXIavVBHUM5RgCQJfLUgS0pYOMIYtmZZ7F6OY578STl-l_-o-M7prEerRbXq5bL7xTkd_UXZuMWYW-WUD7QLUzVDVBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.47M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 08:59:38</div>
<hr>

<div class="tg-post" id="msg-668834">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdqmp8hO7Y0xV6Gt2JT-fGkNqfd7a3hv2lr5mQ8JfuiDD0Vv41w2UQZw2d6xPn3eE64NQu859N-phL3x7ZiQEMU08BGNxMn69osy9Qeuw7_xfxkKJ-GobEaJKIP9hLlKnGQxS4mzSIJxoQPiYUOo-WvD63K0qdrCdwE3pz1tzpjLzODEZ0OPXw0tZ8IoGpOMCeAgc6nlOli4GXTg9R2Hjzl9anmSQ-G1stsG2_sqo8df1KYVAoJ-4PcGdRo8v3C-FQk2bKyRigxZguncNVl-UkVRILBrxtbbwvOQWlxFCqC--VgKLHUBsbq3LctwjEelL7Dp7xumHlJYkRZrKMGylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیر آمریکا به سنگ خواهد خورد/حماسه مشهد تا ساعاتی دیگر
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/668834" target="_blank">📅 08:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668830">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db584baa4f.mp4?token=ohkfLyVdpQsdIWXH7ywX17TWf8KiNRDeNDzCHi_D1KLg-aly8iuKb11j_XDnJq-CfJaMCN-1j1rU1zq6vfWLV9ays3fUUhIcHYTpCyfXikcX1M7KJI6RoQPdGipIDmXqg8ZAmyrp9pd1oCNHR8-CxyYdvFJBa4bYo9NWY-jkEP4dqcgTj1EG5AfDhTM0y2_6AoXvR4JHydNQWb9yh7r7LOwkZ-FwwhLrGeDbuluWnxjlgy39YuW3t3NJ1c3Icj1fR0fAht8Bfm-U2zIpMno2Z4R9hLw6Vcfh4d025470-hXi0qM0YobwKusOXa6kJ0lNuJ6jYgOTsuLVTrViB9_oXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db584baa4f.mp4?token=ohkfLyVdpQsdIWXH7ywX17TWf8KiNRDeNDzCHi_D1KLg-aly8iuKb11j_XDnJq-CfJaMCN-1j1rU1zq6vfWLV9ays3fUUhIcHYTpCyfXikcX1M7KJI6RoQPdGipIDmXqg8ZAmyrp9pd1oCNHR8-CxyYdvFJBa4bYo9NWY-jkEP4dqcgTj1EG5AfDhTM0y2_6AoXvR4JHydNQWb9yh7r7LOwkZ-FwwhLrGeDbuluWnxjlgy39YuW3t3NJ1c3Icj1fR0fAht8Bfm-U2zIpMno2Z4R9hLw6Vcfh4d025470-hXi0qM0YobwKusOXa6kJ0lNuJ6jYgOTsuLVTrViB9_oXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شور ولایی مردم عراق در بین‌الحرمین برای تشییع امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/668830" target="_blank">📅 08:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668829">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeXzsWSk7k55vVKtdhHS08A9QHuYbOsvic1L0HlI54rhiO_HpY9s27VxzJBUjlLs_o5Thy2HSsyMxl8T3M3p2guXwIZDM6PScstuy6BJtWDHyIhV35DTdaQSxRYuyDWrmZNM3fgX8kxzM7gcPqQpkQ1mVJwwLPckcNcIJ3wg_sDwLKFKveVFR12W8_-7gLyPlJDlRz-dsK0q-0jJ8lY1uQRDqOevb6tQKVZAsNbpJCB3Pl7tNotuJgxOw32ncuIUJaslPBP0ryK8JLmPNJXhjcK-vCU9caWrO5B4IcrD7xSoALvKtrwa4oCsL6YSjDtEWcwsG2UfoBb3y8VPC2iC9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران، دیشب چندین پایگاه از جمله الأزرق در اردن را هدف قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/668829" target="_blank">📅 08:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668828">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5r5LUTBuryxImSBwEjgKh0nfG1VhnHFQ6dp-fkgENWJ3TmubodMCHD_yOVkutIcLlXN18DXye2ydcd9C3BV2lD4WbkOY4rF1vIEQgrFry-4IvWd4nPPn9cv5svlZiJlBZYd9S7y5APLf8hWM_v1IneT-6Q6D7V2v2dKFL6LPiRqAzcLKmpqrssTb7L1AWKzoOXRYmLwKnZjVUegsz9PTU77ePlIMnh44JC-NmAygtSez8k-5UPlrhNmBQD4A4T43c9I8sODgvqgCyHllQkfz08hWPA5dP2hx68Xa7csUDB1twieoNSXgZd3KvSDOoWMGoIJbWWnWnlZiDvYu2y1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در پناه ابی‌عبدالله
🔹
٦٩ سال انتظار به پایان رسید. پیکر رهبر شهید انقلاب، پس از عمری دلدادگی به مکتب عاشورا به بین الحرمین و صحن و سرای حضرت اباعبدالله الحسین (ع) و علمدار کربلا، حضرت ابوالفضل العباس (ع)، رسید؛ جایی که سال‌ها آرزوی حضور در آن را در دل داشت کربلا امروز شاهد وداعی تاریخی بود؛ وداعی که با حضور میلیونی مردم عراق زائران و دوستداران مقاومت به حماسه‌ای کم نظیر از عشق وفاداری و قدرشناسی بدل شد. اشک‌ها نوحه‌ها و گام‌های استوار بدرقه کنندگان روایتگر پیوندی عمیق میان خون شهیدان و راه عاشورا بود؛ پیوندی که در سایه گنبدهای نورانی کربلا جاودانه تر از همیشه به تصویر کشیده شد.
🔹
ویژه‌نامه جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/668828" target="_blank">📅 08:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668827">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd51f7725a.mp4?token=UxdL_cudyEpx_OuhZKo-NoNUlsNx0dbZSyO9vXRkpQTXvJAvRdr3d9mOdYSCckeKZoW3sE7QIpSCmQ0lhet3Q9yW8Kws_PXx6BEAGZOgfZ9gKllrhtmy41XdMFu7mFKhhimHxIxTr37LjuVJtrf8oykf6E6cKbpQ0iBRAu32I4r4VPv4AH_sUHkMZd1xTGHbAtHzoOqzrBe2JjDlujGMzlw7ud1xjr0DrXZtYdlMcC7kDBg_9grFqLDtR-aZaSTcR4Ly-yp_vA8b_QrVq_Zs3r5V8jGnb-bS3f_V2YaUVB8zTZ74FDpMD8Aadn4Ar4b7E8FSbbxewxhN5-KnS6nIvCy630s1MP_9bNikqma0GJ5Do7Px1kwexiEXIe6Gfg0HXiCW0ZQB6Fg_aWKjG2zeziwEXRaI3Vz6lrk2B6k9JFIVH5yTRJKBSUaiQcNAIfLzSPljLHkhzfeezkkmlX9ZBGl26cvDt06hLkVDxDJTmj2CJLz0EVSa6KU_4NltQrb0Ny0poyPRXNZ4eM9AuatmlGE8IdEzUzlp82QG526BAI1_1AArqDCP-PBh5rVCSam8dFHYJZrtiq3qkm6tksz8MF-K0JSkWRApIc8AbfxNpEv8zwvfvpYKCuQfqiLmH_iCqKAltpAUFZnC43jh_87NkAGqi3qMdyH_QdszhbKcXDc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd51f7725a.mp4?token=UxdL_cudyEpx_OuhZKo-NoNUlsNx0dbZSyO9vXRkpQTXvJAvRdr3d9mOdYSCckeKZoW3sE7QIpSCmQ0lhet3Q9yW8Kws_PXx6BEAGZOgfZ9gKllrhtmy41XdMFu7mFKhhimHxIxTr37LjuVJtrf8oykf6E6cKbpQ0iBRAu32I4r4VPv4AH_sUHkMZd1xTGHbAtHzoOqzrBe2JjDlujGMzlw7ud1xjr0DrXZtYdlMcC7kDBg_9grFqLDtR-aZaSTcR4Ly-yp_vA8b_QrVq_Zs3r5V8jGnb-bS3f_V2YaUVB8zTZ74FDpMD8Aadn4Ar4b7E8FSbbxewxhN5-KnS6nIvCy630s1MP_9bNikqma0GJ5Do7Px1kwexiEXIe6Gfg0HXiCW0ZQB6Fg_aWKjG2zeziwEXRaI3Vz6lrk2B6k9JFIVH5yTRJKBSUaiQcNAIfLzSPljLHkhzfeezkkmlX9ZBGl26cvDt06hLkVDxDJTmj2CJLz0EVSa6KU_4NltQrb0Ny0poyPRXNZ4eM9AuatmlGE8IdEzUzlp82QG526BAI1_1AArqDCP-PBh5rVCSam8dFHYJZrtiq3qkm6tksz8MF-K0JSkWRApIc8AbfxNpEv8zwvfvpYKCuQfqiLmH_iCqKAltpAUFZnC43jh_87NkAGqi3qMdyH_QdszhbKcXDc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گرچه دوریم... به یاد تو سخن می‌گوییم
🔹
زیارتت قبول آقاجان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/668827" target="_blank">📅 08:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668826">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
به صدا درآمدن آژیرهای هشدار در بحرین و قطر
🔹
منابع خبری تاکید کردند که انفجارهایی پایگاه‌های تحت مدیریت نیروهای آمریکایی را در بحرین لرزانده است.
🔹
همچنین گزارش‌هایی از پرتاب موشک‌های بالستیک به سمت اهداف نظامی در قطر و بحرین منتشر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/668826" target="_blank">📅 08:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668825">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
تردد قطارهای مسیر تهران-مشهد متوقف شد
راه‌آهن جمهوری اسلامی ایران:
🔹
به دنبال حمله جنایتکارانه دشمن صهیونیستی آمریکایی بامداد امروز به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.
🔹
تیم‌های فنی و عملیاتی راه‌آهن بلافاصله به محل اعزام شده و عملیات بازسازی محل آسیب‌دیده در دست اقدام است و تلاش می‌شود در کمترین زمان ممکن این مسیر ترمیم شود.
🔹
برنامه ریزی لازم برای جابجایی مسافران محترم قطارهای متوقف شده در این مسیر، از طریق ناوگان مسافری جاده ای به مشهد مقدس انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/668825" target="_blank">📅 08:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668824">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
چند توصیه برای پیشگیری از مسمومیت‌های غذایی در گرما
🔹
نگهداری برنج پخته‌ شده در خارج از یخچال می‌تواند سبب آلودگی میکروبی شود و مسمومیت غذایی همراه داشته‌ باشد.
🔹
کنار هم قرار دادن غذاهای گرم و سرد می‌تواند سبب آلودگی غذاها شود.
🔹
برخی بیماری‌های منتقله با آب و غذا ممکن است خود را به سرعت نشان دهند.
🔹
دوره کمون برخی بیماری‌های منتقله از آب و غذا در حد چند ساعت و حداکثر ۲۴ ساعت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/668824" target="_blank">📅 08:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668823">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
صدور مجوز استفاده از هوش مصنوعی و کتاب در جلسه امتحان تحصیلات تکمیلی دانشگاه آزاد
🔹
حضور میهمانانی از ۲۷ کشور جهان در مشهد برای شرکت در مراسم تشییع رهبر
🔹
روسیه: نشست ناتو در کاهش اختلافات میان اعضای آن ناکام ماند
🔹
دبیرکل سازمان ملل: ایران و آمریکا خویشتنداری کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/668823" target="_blank">📅 08:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668821">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
آبشار گدازه آتشفشان اتنا؛ فوران سه‌روزه پایان یافت
🔹
جریانی قدرتمند از گدازه داغ از دهانه مرکزی کوه آتشفشان اتنا در ایتالیا فوران کرد و یک آبشار گدازه دیدنی ایجاد کرد که به ویژه در شب چشمگیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/668821" target="_blank">📅 07:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668820">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMRe1vMGjA5RDKEiKU8bNwYsWBmsPfw_0SqzB1b2nC_Oax0y4LxiqGGd9tHCXOaQHvNwh6qNo-nCEGtuf97BOzTfkdn3fVlgWOSZUSt7UA_af6QHgWU6bzURX2prwravG0fQqSK6j-PJW2Zr0NYv7ilmjLNKmCX74T9ED05h6z0mlkOIOGrT_YLXv7-rmMrL4gGmRtxmn3GaW_KieL_HI5N9L65xinsNdksja015zW-sVdYugAbOxw_gLu9rwc5XjHQCuKx9XVm7Vggo9uXKRObjWDHHhZemaSHPyazy-sNL30IwX0HAF67uGnU8kNxjnYZaLyKaJG4AcEfJjmRKOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابی متفاوت از تشییع پیکر رهبر مسلمانان جهان در بین‌الحرمین المقدسه
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/668820" target="_blank">📅 07:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668819">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00d057128a.mp4?token=u4gdeV-v-sVtI53lGZHkkT1wJWIr82QTQ0jdZgoaPgV4wx50ORgOIJ7-r5ck5MVg8yjefhoGehjPE_HKXKb6SPAK6VCKDHYjh5rdHHgXl3dXjnm8tNO4O3j-srBc3ldOGjHmV2O16Gvbh6kIPhTU4i19SLEiWS5oy2Q9rY8ceM3UKWbVht-bS9egxFU8MmT4uxIzzk1snsQJxWdDxdN90N7p0hXqs6UrxgdEbKeTNnawZgHMt9omNjYc0FFmxkWHP1GjzNzavAE5JIploe8XB_Tt9SNrX5pkgSHM_NCWS753SXxAOpFfghLnapVdNEyERYAF1kgDmCvlrIn9VdCDhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00d057128a.mp4?token=u4gdeV-v-sVtI53lGZHkkT1wJWIr82QTQ0jdZgoaPgV4wx50ORgOIJ7-r5ck5MVg8yjefhoGehjPE_HKXKb6SPAK6VCKDHYjh5rdHHgXl3dXjnm8tNO4O3j-srBc3ldOGjHmV2O16Gvbh6kIPhTU4i19SLEiWS5oy2Q9rY8ceM3UKWbVht-bS9egxFU8MmT4uxIzzk1snsQJxWdDxdN90N7p0hXqs6UrxgdEbKeTNnawZgHMt9omNjYc0FFmxkWHP1GjzNzavAE5JIploe8XB_Tt9SNrX5pkgSHM_NCWS753SXxAOpFfghLnapVdNEyERYAF1kgDmCvlrIn9VdCDhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون، فرودگاه نجف؛ پیکر رهبر آزادی‌خواهان جهان در حال انتقال به ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/668819" target="_blank">📅 07:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668818">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
بلومبرگ: کشتیرانی از طریق تنگه هرمز تقریباً متوقف شد
🔹
تحرکات قابل توجه در تنگه هرمز به یک مسیر تأیید شده توسط ایران واقع در نزدیکی ضلع شمالی محدود شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/668818" target="_blank">📅 07:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668817">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
سه شهید و چند مجروح در حمله رژیم صهیونیستی-آمریکایی به اطراف اهواز
معاون امنیتی و انتظامی استاندار خوزستان:
🔹
آمریکا صبح امروز در جریان حمله به مناطقی از استان خوزستان یک نقطه را در اطراف اهواز هدف قرار داد. متأسفانه در جریان این اصابت، تعدادی مجروح شده‌اند که اقدامات درمانی و امدادی برای آن‌ها آغاز شده است.
🔹
در پی این حمله، سه نفر به شهادت رسیدند و تعدادی نیز مجروح شدند که اقدامات امدادی و درمانی برای آنان در حال انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668817" target="_blank">📅 07:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668816">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
صدای چند انفجار در ایرانشهر شنیده شد
🔹
دقایقی قبل، صدای چند انفجار در شمال شرق شهر ایرانشهر شنیده شد. هنوز ماهیت این صداها مشخص نیست./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/668816" target="_blank">📅 06:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668815">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ادعای اکسیوس به نقل از مقامات آمریکایی: مدت و شدت کارزار جدید کاملاً به گام‌های بعدی تهران بستگی دارد
🔹
ادامه تشدید تنش به این بستگی دارد که آیا ایران به حملات خود علیه کشتی‌های تجاری در تنگه هرمز ادامه خواهد داد یا خیر.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/668815" target="_blank">📅 06:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668813">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8734f9cfbc.mp4?token=qsEL_E7bsvvXjWmoYzODuPNg8iWopFcXoHf1JzoGcTB7l-y7vOt3WfWLLikmJRXpSXeZz2QYdmiyyr0JSowcmn-pZQ8H23-9k9-1sUpd9uIBuJFBrJ7eaitsRoCt_e00c267ncfMHn8QXAnFBffert7zie-bxwmTaV8ub-9BhFcMhYkRvZt1fPVIhkYYZnOw9t1w8aVH4b3uOicvaBeCLGwL192EU0qMk4D4sf-uLScjMAM_Rk6XXlsL8VCM4uEtDBYIsy_-9jCi4tNDfh_IJahj5L6cfYynaZMTw6wu04A7szDeATa8v2N7uQ6FmxiMhg8YoIlO49srzSOYrK1dTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8734f9cfbc.mp4?token=qsEL_E7bsvvXjWmoYzODuPNg8iWopFcXoHf1JzoGcTB7l-y7vOt3WfWLLikmJRXpSXeZz2QYdmiyyr0JSowcmn-pZQ8H23-9k9-1sUpd9uIBuJFBrJ7eaitsRoCt_e00c267ncfMHn8QXAnFBffert7zie-bxwmTaV8ub-9BhFcMhYkRvZt1fPVIhkYYZnOw9t1w8aVH4b3uOicvaBeCLGwL192EU0qMk4D4sf-uLScjMAM_Rk6XXlsL8VCM4uEtDBYIsy_-9jCi4tNDfh_IJahj5L6cfYynaZMTw6wu04A7szDeATa8v2N7uQ6FmxiMhg8YoIlO49srzSOYrK1dTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنتکام: نیروهای آمریکایی دور دیگری از حملات علیه ایران را به پایان رسانده‌اند
🔹
ادعای سنتکام؛ حدود ۹۰ هدف نظامی‌ایران، شامل سامانه‌های پدافند هوایی و تجهیزات نظارت ساحلی، دارایی‌های دیده‌بانی ساحلی، سایت‌های ذخیره‌سازی موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران حمله کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/668813" target="_blank">📅 06:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668812">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ادعای اکسیوس: با «پایان» آتش‌بس ایران، ترامپ به نبرد بر سر هرمز روی می‌آورد
🔹
کاخ سفید خود را برای چیزی آماده می‌کند که می‌تواند به تبادل آتش چندروزه یا حتی چند‌هفته‌ای با ایران بر سر تنگه هرمز تبدیل شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/668812" target="_blank">📅 06:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668811">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
پایان مراسم تشییع پیکر مطهر رهبر آزادی‌خواهان جهان در کربلای معلی
🔹
مراسم تشییع پیکر مطهر رهبر شهید انقلاب اسلامی ایران در شهر کربلای معلی، پس از انتقال پیکر ایشان به حرم‌های مطهر امام حسین (ع) و برادر بزرگوارشان حضرت ابوالفضل العباس (ع)، خاتمه یافت.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/668811" target="_blank">📅 06:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668808">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lY8X6tdRsjmlx-1l4_64By4kjPBJ3Hjb0tc-tGowEZ2b9ljPhbjwvswh9t6ojgunVpKUtr8donqrUY2AxG819zdCUInoo4wl8X19vIP8eIH38NcCH3n19mMsKd-htKU1ssJ5mLy6SSjQru1r5kFZJNCiWgrZmLa_Y-wSiEnjax_pJO3WIsQioPldvuo4aiLnXiuvk005JqeLK3oM7N787CGa2cWMOsEqpSuf-1upSjVHwWq_FzQqPDKC3pfnY1l216udyLQO2mlqvLZVMPNmWEQZ9xFsptqeOB34yGn3tmHuJJHXodrQ2ObJZI1zivxXmyKvL_iaevx2Mfjzf7ZN3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xfo1E0M-HhQiahDj87deGoV_a7qkLiF0lBq7sJpsVLBaV1UB8Jz7FFqX6Pl3VmK5an4g3f5GHqTpxPh9erWdbEx-UNb4KgUzKD_w5rgNtvDMzRk5U6M8lOeYg5Pqv4wpkc8MZH_BjWqCZNxlPFEjQFzQ92pIKPkS1kNCBxi_UAOmQ2X-pepFp9j804NB7nsdDXvXub12SRGZUOZ5RjGSSqP7Zl19ZO-fJy5KjQvTNC4SZd8djs6l0o1E1o6DN3CISOv3iShbrRc6_KYgkKPlOzKJEmHcR7rSYro4CxyZdB3cnQ3ZgbQ8Thbd27KJXnznTXOXyO_HzM5WEQx7gYpBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YxayOhY2B5VZ243AT9kJHVU7fFKoWAeT4lLhwa86nOOOiz6yJpJf5Nl52i-dNrrEOXzdOlyuZKKA9tLn0qMCUeBagBEZH5mX0W8ylPoQEJDrbpahwcfjY7ZZ5WsV3WpZHYXw0GssqhgrYBf5BbZr2rYdG3mRqROwqOylubOkOUy7Ox1Ik_o-y3w1ebtP4Ov9K060FVXWXtUbx1Bk2QKytSv-KEJxsmi5KuUhZf-fOz6CKZtd6BTgdtt2I7gllW5LbOxTgrfjWUldWDGuGFMJK_7gvUQpgRnSmdz0sA7LbJfreoZoF8I5ALnHZKZt2gYHAIvCLR2oc-wzfK7b0iO1qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از بدرقه حماسی و تاریخی امام مجاهد شهید، حضرت آیت‌الله العظمی حسینی خامنه‌ای در حرم مطهر اباعبدالله الحسین علیه‌السلام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/668808" target="_blank">📅 06:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668807">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
سپاه: زیرساخت‌ها و تاسیسات مهم پایگاه‌های آمریکایی در کویت و بحرین مورد اصابت قرار گرفتند
بیانیه سپاه پاسداران انقلاب اسلامی در پیخداد عهدشکنی و تجاوز ارتش کودک‌کش آمریکا به شرح زیر است:
بسم الله قاصم الجبارین
قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ
🔹
ملت شریف ایران، ملت کریم و مجاهد عراق؛ آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع‌شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی و عشق عمیق متقابل مردم و والی اسلامی با مرام امیرالمومنین (ع) را به رخ جهان کشاندید و با شعارهایتان یادآور شدید که هزینه تعدی به مرجعیت و ولایت فقیه مسلمانان بسیار سنگین خواهد بود.
🔹
در اولین مرحله از پاسخ تنبیهی علیه پیمان شکنان آمریکایی، رزمندگان نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی، ساعتی پس از حملات دشمن و نقاط مختلف کشور، زیرساخت‌ها و تاسیسات مهم دو پایگاه‌های استعماری اشغالگران آمریکایی در عریفجان و علی السالم کویت و جفیر و شیخ عیسی در بحرین را در هم کوبیدند.
🔹
سپاه پاسداران انقلاب اسلامی به ارتش کودک‌کش آمریکا اخطار می‌کند که در صورت تکرار تجاوز پاسخ‌های کوبنده ما به سایر پایگاه‌های آمریکایی در منطقه توسعه خواهد یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/668807" target="_blank">📅 06:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668806">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvVZeRa51uamXv2F3YavCrbE-AGOMQxFqyVztF_8hdh7w3dUp54-HQ8oh-eyUo6i-L7bqQ0SQfI_Cwjbae52rD1Blc3WWZcCdwUVcHa1d2uFtZjYdnXo3-cbUU8L9YhYgHtcQ4f0sIQncsoOoGIEdujxo1GzbN66DXifhOqNZ1HiWVbmaW9d_44LpHyo-2tPQAZAejhyAtKkhMkyqkUsxRbHlPpuaq-VZdIIR2Nb6vvp-LerZPk58ESODB0cYuVh3TrjGwqbRFH2f7fbMyj1qP9iRW8MNUsCrgD_m4AMiVEY8EPFNQZaDfDixp7XbGQnTi-BhMRISEuDR7J1iPLLog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: اعتراف‌های مکرر دبیر کل ناتو تأیید می‌کند که اروپا در این جنگ تجاوزکارانه بی‌طرف نبوده است
سخنگوی وزارت امور خارجه:
🔹
اعتراف‌های مکرر مارک روته به مشارکت کشورهای اروپایی در تجاوز نظامی علیه ایران بار دیگر تأیید می‌کند که اروپا در این جنگ تجاوزکارانه بی‌طرف نبوده است. طرف‌هایی که قلمرو، پایگاه‌ها و زیرساخت‌های خود در اروپا را برای تجاوز نظامی آمریکا-اسرائیل در اختیار گذاشتند، نمی‌توانند از مسئولیت همدستی خود و نیز پیامدهای ناشی از آن شانه خالی کنند.
🔹
اما این خودستایی بی‌وقفه مبنی بر خدمت به قلدری آمریکا و جنگ تجاوزکارانه آن، بیش از آنکه نشانه قدرت و اعتماد به نفس باشد، ذهنیت یک درباریِ چاپلوس را به نمایش می‌گذارد که می‌پندارد با تملق می‌توان نگاه تحقیرآمیز پادشاه را تغییر داد. مشکل اینجاست که چرب‌زبانی نه می‌تواند سازمانی که در نظر واشنگتن ناکارآمد است را کارآمد جلوه دهد و نه می‌تواند فقدان عزت نفس تملق‌‌گو را جبران کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/668806" target="_blank">📅 06:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668805">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26234f34a7.mp4?token=hz80NLOShJcrcbmFQPrOkTAEPNUVH58EzRlp3MURlFXtaXYXjCMX8Su0uvtKWgB1ZbPvAFG2q0o1_GpL8MOUNruhyILUsT-SFyjdR_rHvASdR0NOqql6FOHM_Qe_m0gd_YyIcREIcX0Y9N5AnMS-wRZoV4N8zuTuvzGvR27-q7mIKCRxVFyjoZ2Lr7gtowdJjxaEJy9chKroesifkH6iZw0Lzi-iBb0cvbZEz6LQ1DcjZdSu2EHTj5W33kzfGgeNkSvQFujMQhiLfwWqQVsIUsRZeZLt6yeKIzT_bgxiS3LTZEgkHr_IUL_e1uolDBxacF__TtI1Wg32XDEAlQO28Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26234f34a7.mp4?token=hz80NLOShJcrcbmFQPrOkTAEPNUVH58EzRlp3MURlFXtaXYXjCMX8Su0uvtKWgB1ZbPvAFG2q0o1_GpL8MOUNruhyILUsT-SFyjdR_rHvASdR0NOqql6FOHM_Qe_m0gd_YyIcREIcX0Y9N5AnMS-wRZoV4N8zuTuvzGvR27-q7mIKCRxVFyjoZ2Lr7gtowdJjxaEJy9chKroesifkH6iZw0Lzi-iBb0cvbZEz6LQ1DcjZdSu2EHTj5W33kzfGgeNkSvQFujMQhiLfwWqQVsIUsRZeZLt6yeKIzT_bgxiS3LTZEgkHr_IUL_e1uolDBxacF__TtI1Wg32XDEAlQO28Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای خصمانه جی دی ونس؛ تهدید آمریکا به تداوم حملات در صورت بازنشدن تنگه هرمز
🔹
معاون رئیس جمهور آمریکا شامگاه چهارشنبه مدعی شد که اگر ایران سعی کند تنگه هرمز را ببندد، با واکنش نظامی ایالات متحده روبه‌رو خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/668805" target="_blank">📅 05:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668801">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZLmV-SO9A989Od7SSoAEFBpMWJu4TqgUhrOYw3yv4NK15STdvNSIASPE7c9t1TTcn0yt8kn9FwOwQRR34RlEzJ9LxeEiZfVWidi3ymgwi8khgHqJ828Saz1BiiZeW8IFWanRuYsZQc07K4YHFGVDhEAyMOPDeX31Paw2P6j2CIMVCAp7git-S9maK4TIa69tA2R9s7_CdcWDOeixQ-6wA_e3pkkGCXwmB_GMBa_ZbnycalzsMbRsQqxBxJfG6FfOcK5sWEaqtBxU_HNB57nplfR208SqJLdcmjCgfSCkZQQf3XQO8vsOO1imVhTjRBrDnKpQUpzJsYGbjo4UYbfsEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJbzqITKRsDnM1Uv6krv6LMPVeBx1nBOZKBiZmnLTJ1xNbzSxjtCIZcwOanSHabYrMPIOuasN6v6AvPx6IU2GCZTKdtXw_ieXLQo4mF1mMLGRbgIAk0au_eCCftMGSk4FhPHZ4ojtollsnNANTaQtycX9NO61gmSIeecfJSf45rGNPkKk6S0lYqdLUzkHIPGU5ILvUEp2f6NscS1bt1cGq3f0EzQOk9r_WdQes44b9MyLXV4iUt8tyi_IKYkm0vdHLYuUkuxSEQsV_tomaVxaYJgwSWsGaKZTuv-WO_qe16RmtquEtVvV_RgDBcrkTrmXoTEgHp1jFc688qwDHUndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqgpX7KT_kLnUMMDZXMwFIbuwkj5eBLk2gA2yI-jjpL6uU-dSZGJuCzzufRCYe1ZTkggU3laxKnMBgDh9BcqoEJUMD3a5oNt2Lr9NOc4EBCst0PCnd3sfXgNPF7nF7onM-y-zbtIRJPRhHy9BYggVfklX1Zqb1T5ExqOA9bMq2npkeQZpleapC_aH48psE5lGZ9CYjdjp4_nqLZpnHwDARhLxlGNCuZpyeMsz1fFbzCVsk6O3tCVOiK5zJKCCCdQrdWCI0IMJIZHNtiB1lZXEB2NPYWfaEQzkRniLP139DrmbskS6vON-WinmjO9VdGWkWXdF3WBiuGbC24qfesvkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b347b90d6d.mp4?token=pfj-J2mRE4BltGkJAgWjMWeaJcPs5OaecAtQkm-QHYC-LL_5mMuwCTENDsjdvdB0UTYAiy6PY6yvp4DpyFThAZYwJ2B6wshEBBdLHJ-KaxukDfze3qVV6FGGFztHTbDtVySnOy2As2UKMXLdEqEVgHOUPDdnsQNc-XqhG7Z3ehn_27O_b4WfwinzkU-RSbZmk4Ra8hHr3eQMwcOG8eM78uRjhVZJ5zH7lM3aq4uZnE484PswHsTVNYqfdhqg_boYTnbr500nU6pazbY2o7BuT_FYT4_qLYJvWV66_ivEHosKvTtl0CU8WRnRf2l3ggVb4a0CACgJtr8vhaY6WbhfbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b347b90d6d.mp4?token=pfj-J2mRE4BltGkJAgWjMWeaJcPs5OaecAtQkm-QHYC-LL_5mMuwCTENDsjdvdB0UTYAiy6PY6yvp4DpyFThAZYwJ2B6wshEBBdLHJ-KaxukDfze3qVV6FGGFztHTbDtVySnOy2As2UKMXLdEqEVgHOUPDdnsQNc-XqhG7Z3ehn_27O_b4WfwinzkU-RSbZmk4Ra8hHr3eQMwcOG8eM78uRjhVZJ5zH7lM3aq4uZnE484PswHsTVNYqfdhqg_boYTnbr500nU6pazbY2o7BuT_FYT4_qLYJvWV66_ivEHosKvTtl0CU8WRnRf2l3ggVb4a0CACgJtr8vhaY6WbhfbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در شهر آق قلا استان گلستان
🔹
دشمن تروریست آمریکایی به یک پل راه آهن خارج از شهر آق قلا حمله کرد.
🔹
هنوز هیچ منبع رسمی اعلام نظر نکرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/668801" target="_blank">📅 05:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668800">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cbc7b457.mp4?token=DNW5aNVMpZFJ-5R67f2ZJchsUc95kGFqxK4jOSrjrB6_b8CqMI_GVh1qdDgFmtzQN8ie2wYLgFR_-DwNkygb1askdA2nX2seTkNEEGmbEs63Z5h_yNRx1Z_RWyt1xwW_Ml15LHkF5-XuNB9hedzdGLLwRLwMIfyw_iE9QkZ2PDYnDvh8agArxz3m1xBXnmU67CxOZWpskEx0mIWFmAJO9G1_kPUodWOTSp9PHJrdiZXdWZPG7kvzIYTsCt_eCmwF4L5GiZR_ueScH6n7MYKha40A3MjwX3ZvcLCpb0nWl7o9p4rP_qRbqQnQCOCC7jKn8U6KsECslYEMy_hEuX5OfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cbc7b457.mp4?token=DNW5aNVMpZFJ-5R67f2ZJchsUc95kGFqxK4jOSrjrB6_b8CqMI_GVh1qdDgFmtzQN8ie2wYLgFR_-DwNkygb1askdA2nX2seTkNEEGmbEs63Z5h_yNRx1Z_RWyt1xwW_Ml15LHkF5-XuNB9hedzdGLLwRLwMIfyw_iE9QkZ2PDYnDvh8agArxz3m1xBXnmU67CxOZWpskEx0mIWFmAJO9G1_kPUodWOTSp9PHJrdiZXdWZPG7kvzIYTsCt_eCmwF4L5GiZR_ueScH6n7MYKha40A3MjwX3ZvcLCpb0nWl7o9p4rP_qRbqQnQCOCC7jKn8U6KsECslYEMy_hEuX5OfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت های تکراری شیطان زرد: آن‌ها همین چند لحظه پیش تماس گرفتند، آن‌ها به‌شدت می‌خواهند توافق کنند
🔹
اما من فقط نمی‌دانم آیا شایسته انجام یک توافق هستند یا نه. نمی‌دانم که به توافق پایبند خواهند ماند یا نه. مشکل همین است
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/668800" target="_blank">📅 05:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668799">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3042427b41.mp4?token=Bqqau9JQC37kcgL00Pgfi1i59JozRPVaiDS7vfKihPixhWxhkFqLbfqVTv2r7hGmDQsEk84LxyaaomRZHivqdOgWp0uZSfr2QxS5ePQ6beRefN2UC9-3VNRG0wT3Pxkne_Fofi4kLkGniylbrQIzRNEtbi74jVx5kcTu7CpwXRkC9KTmP4xftHeR6EVGWsn6cl5Q7pJvKUbomj1iPrA0zK0hDYg4keb4O6A6vgv7uRaBSTLb1yuP7lVUbuAcJ21W0odlfzgKfuBoNSha3134iNIQe0W6NYaePRon1afauag14E03sY5DehQ5ClRunCgayzlyp2Iu77SE3NVKG_t2jjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3042427b41.mp4?token=Bqqau9JQC37kcgL00Pgfi1i59JozRPVaiDS7vfKihPixhWxhkFqLbfqVTv2r7hGmDQsEk84LxyaaomRZHivqdOgWp0uZSfr2QxS5ePQ6beRefN2UC9-3VNRG0wT3Pxkne_Fofi4kLkGniylbrQIzRNEtbi74jVx5kcTu7CpwXRkC9KTmP4xftHeR6EVGWsn6cl5Q7pJvKUbomj1iPrA0zK0hDYg4keb4O6A6vgv7uRaBSTLb1yuP7lVUbuAcJ21W0odlfzgKfuBoNSha3134iNIQe0W6NYaePRon1afauag14E03sY5DehQ5ClRunCgayzlyp2Iu77SE3NVKG_t2jjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دمام‌زنی مشهدی‌ها در آستانه مراسم تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/668799" target="_blank">📅 05:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668798">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ba6f815f.mp4?token=AThK1MFKfEy2Pm5VZLniMEiC8_E8MxI2x-35T1EJJTolXpfNN_6Fmap0m_5os0DIYYWOIWLNE9JmWn3tectDo-nXyOmAfDUow_t5UVbMRSLzY8lsKD1JGxUhBtEcGiJMndPE7Snid3Ux6f5yQDlbIB1AKTaadSDG0sKnxuDd4Xb1TsOU9ke_ynpan8nIIWfrFy1Z8oxW9rs7TiTUtDQu9JX14BMZWaXSdz5fwdK-xtXJ8K4U1JlMBcq19LV7XA0gQybXwYYiBdlocESrJf4r5lMIoC_Cmuv2y1ES_jr-Eqfvo64TLzenfW-Rb1eITdr4IDvmBoKFaGbO5sst-xwDvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ba6f815f.mp4?token=AThK1MFKfEy2Pm5VZLniMEiC8_E8MxI2x-35T1EJJTolXpfNN_6Fmap0m_5os0DIYYWOIWLNE9JmWn3tectDo-nXyOmAfDUow_t5UVbMRSLzY8lsKD1JGxUhBtEcGiJMndPE7Snid3Ux6f5yQDlbIB1AKTaadSDG0sKnxuDd4Xb1TsOU9ke_ynpan8nIIWfrFy1Z8oxW9rs7TiTUtDQu9JX14BMZWaXSdz5fwdK-xtXJ8K4U1JlMBcq19LV7XA0gQybXwYYiBdlocESrJf4r5lMIoC_Cmuv2y1ES_jr-Eqfvo64TLzenfW-Rb1eITdr4IDvmBoKFaGbO5sst-xwDvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تو کیستی کز غم از دست دادنت
مردان ما شبیه زنان گریه میکنند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/668798" target="_blank">📅 05:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668797">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7569abb000.mp4?token=vTJkvv7ukMzwltUoXVtp1_nqyjM5YmmrPXwN8QFYedY-H0Pzzhihu4LVpU-wQaUyVG9ShhSBTce9lIh84d_T_MVczIO33xISMVe6gXEjNFdUVtERCvCUg7IttKCtcqoRzp12Q0khBRg1fEFY8CXiz9etJUjFYwqXUTCC5EjwT67aqcEcqGuWk8GUkwCheeUJxDXpdlpPg_UMOIJjYIfrvFz5V6LTN8Yb9nCDDguIM_9xDFov64DTm0wKzqnK9zacaaLJkQnwvyIQnOHlqn63bUIDK9ht9cIKYXvDJ0UuAcDIDNqm6fQS7OLgfOOaOcf3sUPveW3XO88uGaVBdazqfQnA9UL1IW7z0m1UXNboO9d4s6HAu3hYqql_4EbIxe-tOlIXVg-suQa5e7Z-C5vecGq1_TkO06ZIg7hYIL-DvsYp8Xns6QFnddl4O2qHjmDeeDHi7n0kaMPhmHu2KEsNn1ksc9QHjxU3_TdGylQ1zHe-janKNk6LzAh-aadZCf3HsndS_Gky5cmLlz3IUAvSMecTsB_odkaISytWP1QbuCcpKcc0bIYjz08Cjle9zy8nHb7m6b8e3MborOfxtcTEg-mXCjboGpi3tmYeZran-Y87jaDQHGTwfDLMuheZgnWZ0htrbBJndIksc-gc8MBM8arQn3z0TDSVV2OQWw1gRAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7569abb000.mp4?token=vTJkvv7ukMzwltUoXVtp1_nqyjM5YmmrPXwN8QFYedY-H0Pzzhihu4LVpU-wQaUyVG9ShhSBTce9lIh84d_T_MVczIO33xISMVe6gXEjNFdUVtERCvCUg7IttKCtcqoRzp12Q0khBRg1fEFY8CXiz9etJUjFYwqXUTCC5EjwT67aqcEcqGuWk8GUkwCheeUJxDXpdlpPg_UMOIJjYIfrvFz5V6LTN8Yb9nCDDguIM_9xDFov64DTm0wKzqnK9zacaaLJkQnwvyIQnOHlqn63bUIDK9ht9cIKYXvDJ0UuAcDIDNqm6fQS7OLgfOOaOcf3sUPveW3XO88uGaVBdazqfQnA9UL1IW7z0m1UXNboO9d4s6HAu3hYqql_4EbIxe-tOlIXVg-suQa5e7Z-C5vecGq1_TkO06ZIg7hYIL-DvsYp8Xns6QFnddl4O2qHjmDeeDHi7n0kaMPhmHu2KEsNn1ksc9QHjxU3_TdGylQ1zHe-janKNk6LzAh-aadZCf3HsndS_Gky5cmLlz3IUAvSMecTsB_odkaISytWP1QbuCcpKcc0bIYjz08Cjle9zy8nHb7m6b8e3MborOfxtcTEg-mXCjboGpi3tmYeZran-Y87jaDQHGTwfDLMuheZgnWZ0htrbBJndIksc-gc8MBM8arQn3z0TDSVV2OQWw1gRAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر رهبر آزادی خواهان جهان از حرم حضرت عباس(ع) خارج شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/668797" target="_blank">📅 05:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668796">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ed255f4df.mp4?token=h1t3aUPR_h91RhEjbp-rjHZdFIy5jLAba6oUJXAq3PQgAmBpksUXkhMp2paPxfP-hoI6VJAl_sMO9YQ27KjeXRdEkG7yeYDC_yfPqdyK061TtiktgAiZdIynDGotAtUEDgd_48aObo5-S929M5xtgMiRoK01rM7XhHf1PMOtOPyNU9DSAHPYxx_MnXl7k8I2MkxRPrOPlsnpVMSCKeIA07OKHuOS4qBCpZ6ezbHxGfyUwqkJOfGKLEuHPuUUkoj6M7tyK6kRQRloFzFhHjQWxwQLseDakHNMh0kNMtw-RFAGMePH61XgaSBw79DfOF61g6oGBynZ7VOBu7NWOkVn96H6FnZW663Yb69qXEHDQ-WAQQf-fSgumXmOdYESvzBuPvR7YIcBhz9RbwroSeTw4PS61AJpvKX6QmIFeF6tNLaiKTe_V5eiJILDW21V9acoIxG_FDJaTigQzW8bceOPfUt_JTHjgl5o5DKXPWdZxGzZJDH-n_0VGba-kU6uTNs5Qm9saRMa0CT_5QBBV9YqX7ku3Uyh7hzc380qDF4kZx7JPVNtRIuxTpeYj-drAHfwfQZtjOcfwuaVmHy-cHsz2C7Guc9sYkzCQR_Rni1kBXyyD6KwYiTTPshVcD8Xj5DjnZ0MKNxb8ZuH2q-wDLpI5xHDrcaqtJvp5BaMlDDdmiU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ed255f4df.mp4?token=h1t3aUPR_h91RhEjbp-rjHZdFIy5jLAba6oUJXAq3PQgAmBpksUXkhMp2paPxfP-hoI6VJAl_sMO9YQ27KjeXRdEkG7yeYDC_yfPqdyK061TtiktgAiZdIynDGotAtUEDgd_48aObo5-S929M5xtgMiRoK01rM7XhHf1PMOtOPyNU9DSAHPYxx_MnXl7k8I2MkxRPrOPlsnpVMSCKeIA07OKHuOS4qBCpZ6ezbHxGfyUwqkJOfGKLEuHPuUUkoj6M7tyK6kRQRloFzFhHjQWxwQLseDakHNMh0kNMtw-RFAGMePH61XgaSBw79DfOF61g6oGBynZ7VOBu7NWOkVn96H6FnZW663Yb69qXEHDQ-WAQQf-fSgumXmOdYESvzBuPvR7YIcBhz9RbwroSeTw4PS61AJpvKX6QmIFeF6tNLaiKTe_V5eiJILDW21V9acoIxG_FDJaTigQzW8bceOPfUt_JTHjgl5o5DKXPWdZxGzZJDH-n_0VGba-kU6uTNs5Qm9saRMa0CT_5QBBV9YqX7ku3Uyh7hzc380qDF4kZx7JPVNtRIuxTpeYj-drAHfwfQZtjOcfwuaVmHy-cHsz2C7Guc9sYkzCQR_Rni1kBXyyD6KwYiTTPshVcD8Xj5DjnZ0MKNxb8ZuH2q-wDLpI5xHDrcaqtJvp5BaMlDDdmiU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در بحرین
🔹
منابع محلی می‌گویند که انفجارهای جدیدی در بحرین رخ داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/668796" target="_blank">📅 05:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668795">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d07ecff9c1.mp4?token=lfdpxaFOT8ktEUhLfB7TyGrpViupM416OlxLns_0Bt2rdgVZDZLs3cw0liE2gXLDmEYJ1NC5fnXQtNcBmyoA1ZxDNLKbvCBNrwvkYMrfYCVdPhR9lNNJkhT6g6T_TrrBFNVKIFww4zHlry_g9jlFK6R5Em4GdqEYinkXi0DIlBtVZbXigZQxojnnpEZP-rYF0LbKxST4OdCDwY8-yZpsQpvPHqmqCid2ISpkV_b-_otBKQbNJdZtoV0K9vYtwatCSLNA519Xwy8nS2zNP-DyZt5DtmTBLfwE9J1dMmn0uaDbdRg64p9AjJ3SmhpUz7g91ps1oO8wy-GE_f5LqVGnYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d07ecff9c1.mp4?token=lfdpxaFOT8ktEUhLfB7TyGrpViupM416OlxLns_0Bt2rdgVZDZLs3cw0liE2gXLDmEYJ1NC5fnXQtNcBmyoA1ZxDNLKbvCBNrwvkYMrfYCVdPhR9lNNJkhT6g6T_TrrBFNVKIFww4zHlry_g9jlFK6R5Em4GdqEYinkXi0DIlBtVZbXigZQxojnnpEZP-rYF0LbKxST4OdCDwY8-yZpsQpvPHqmqCid2ISpkV_b-_otBKQbNJdZtoV0K9vYtwatCSLNA519Xwy8nS2zNP-DyZt5DtmTBLfwE9J1dMmn0uaDbdRg64p9AjJ3SmhpUz7g91ps1oO8wy-GE_f5LqVGnYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روضه‌خوانی در کنار پیکر مطهر امام شهید در جوار ضریح حضرت اباالفضل (ع) در فضایی از اندوه و ضجه‌های عراقی‌ها
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/668795" target="_blank">📅 05:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668794">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
روزنامه وال‌استریت ژورنال به نقل از یک دیپلمات ایرانی: ایالات متحده با ایجاد یک گذرگاه کشتیرانی بدون هماهنگی با تهران، توافق صلح را نقض کرده است؛ نقض این توافق از سوی آمریکا، تصمیم ایران برای تیراندازی به سمت این گذرگاه را توجیه می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/668794" target="_blank">📅 05:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668793">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWMlibncuYDtnAK4zxAQmgrySIiPFuLPYBrPq-ABQRvmOlOTZl-hXEVO1RJAfo56TGHY-Y3aLr5R2N2arZ5MiWZTMkw_XqqKV5iioIl_VEFe38XKoJEyXNBUuf_aSVjiRZ3wxxbpwFc_EuyBD2yCx_V--2-80r7Vl8zf5aGVjTR92XWF_c5yGCwTT_TKdHS4vLkl6RtGKoQTU_t0_Xfvtc_Afs16YuMPz22yTTVr1_etZp_KaPElUdG4ibVyNJGHk30rai8Si72l4bBU-66ve7IV65vT4tISUIhodm0YNh_j03-7iwCHqBrkxsFKKafsTlS9JOpmeJaYqpPfLK3_dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایمان عطارزاده، سخنگوی ستاد تشییع رهبر شهید انقلاب:
زیارت کربلا رهبر آزادی خواهان جهان بعد از ۶۹ سال
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/668793" target="_blank">📅 05:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668792">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcF4PMjwX67mkHcfEC1vp3wnuJDPQJew6NsDeMB8nrlfZwJlkkwnox-hwFesijWMN7yh2vqIfqH9c9LAZUPzUleIAOYxtAtMYKywTbysIjEGjl-rY4QuSHiOFX5PZjFhFMzDiZ_ax6okuwD-Tx1sbTS9AoiePvdWXiJ8WY_SEJj4Kgeh2ZVqdCoON9R1NA6C_2ZiQNtkOc5Gc0ilafxUDa93-DNA9-DlsTse2YjUVvD_8hgPRJXQvjJX040xEXQmFTgy0R6T4rqn4xVx1YoSlAsVd-961sZhiwDywCF3zgsZSO4YnZ1-uYkVMLPTT5IKLmsllCQrHgtowNeRSsgHKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: آمریکا هنوز یاد نگرفته است که زورگویی و بدعهدی دیگر بی‌هزینه نیست. شفاف بگویم: بزنید، می‌خورید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/668792" target="_blank">📅 05:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668791">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
انفجار در بحرین
🔹
منابع محلی می‌گویند که انفجارهای جدیدی در بحرین رخ داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/668791" target="_blank">📅 05:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668790">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10cf4ac29c.mp4?token=Ql-hX3lnTxwR1itoW4etWHd7wvqVwkZdh3Oe5hPnpsajNf5LaG0xHLAb6_D6t7uCuU1Qq6AmFKM7dzSzv5gHZ2wZzAGoCBu35cM93N8nZ9XP7UCCRL69-AAwklc7zTRkOjHvwlsH_cOxTYt7FKi1wBPQ8rY9LlR_RFSfxUu3KLsJNiCWrmAG7sDQD0w3PrfSswS5DeBdQOrO-9Mghvc7VUIdv8YbQPg1qk7Y_7n5Us2egV_EfUvPLyJ2MT-auz8VLW9kxRPs_FPSycnxy22sjU22h3M8xlNNeFXV91Z8o8miM6IefMGBmNGzP5GK6LgCeId5QqaWJ_ZESX3ZM-XcZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10cf4ac29c.mp4?token=Ql-hX3lnTxwR1itoW4etWHd7wvqVwkZdh3Oe5hPnpsajNf5LaG0xHLAb6_D6t7uCuU1Qq6AmFKM7dzSzv5gHZ2wZzAGoCBu35cM93N8nZ9XP7UCCRL69-AAwklc7zTRkOjHvwlsH_cOxTYt7FKi1wBPQ8rY9LlR_RFSfxUu3KLsJNiCWrmAG7sDQD0w3PrfSswS5DeBdQOrO-9Mghvc7VUIdv8YbQPg1qk7Y_7n5Us2egV_EfUvPLyJ2MT-auz8VLW9kxRPs_FPSycnxy22sjU22h3M8xlNNeFXV91Z8o8miM6IefMGBmNGzP5GK6LgCeId5QqaWJ_ZESX3ZM-XcZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طواف پیکر پاک رهبر آزادی خواهان جهان به دور ضریح حضرت عباس
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/668790" target="_blank">📅 05:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668789">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
اعلام وضعیت سفید در کویت، بحرین،‌ قطر و اردن
🔹
با پایان این دور از عملیات ایران در واکنش به تجاوزات آمریکایی‌ها، در کویت، بحرین، قطر و اردن وضعیت عادی اعلام شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/668789" target="_blank">📅 05:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668788">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyaFQtyKJOn693RVZ7iGcVt_oDpg_LoSW_AYwUdBorJM4rDgoEgtKsukwPYPaQMid54mFMBZz9GKKG33zEe2DYSufQtfEWJxj_twTF0GZuT_9mbXkXz_TEehRn4NKo_QfEXYypPRboN8v5rRBUIiEfjwzZBhEwByjc6v_OhKhqquHwhNWYiUxcfMBWjeMNykiRfBStq2O9mqOf4Lq4yutuuAYwqT591U3zS0kmGmCzpcP8Cx-c7f0SXNdu1pE1TvlLB5LJs_Jrv9cWTyV9YoZ1RdZubTUdRIQkBvmcmrOFm3jGASa3K58ua1KSY6z2XxlQH9WBx0Bue5ICBX8LObtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۱۸ تیر ماه
۲۴ محرم ۱۴۴۸
۹ جولای ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/668788" target="_blank">📅 05:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668787">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
خبرگزاری رسمی عراق: مراسم تشییع پیکر شهید آیت‌الله العظمی سید علی خامنه‌ای در کربلا پایان یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/668787" target="_blank">📅 05:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668786">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/586ba974b9.mp4?token=L2T1V1qR2FVXqrrA9YsZ8UjjQ8IH1YBDy5ltK3SIFMUeKqWmNaSo9c2mAKmCAq5-5rvhmbQoyOmX50IrYxrt-ZYJcddXNLowLh3M0cAQufLtn-ztHTEM5oIKqBgGuQ_K1_167KI6v7lypm7HiSV9kG7H33lRAjoc_w259Q8e8RxhmoBL9mhSAKjwnhfLYMtyfyCLbruvHSzqwpvzvGO6n6GDmADLDY_V2IK1UdNg7dqYkDfJA_CV-gV8Gx4o7ob252hZLqbEJc1Qrtv7IeSCbY4mBTOjfJSJMvEWtfKLbsRF9KOM39_yJ2OwO_C1S-nmeDWANKHgyjFvrtSrQIxlfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/586ba974b9.mp4?token=L2T1V1qR2FVXqrrA9YsZ8UjjQ8IH1YBDy5ltK3SIFMUeKqWmNaSo9c2mAKmCAq5-5rvhmbQoyOmX50IrYxrt-ZYJcddXNLowLh3M0cAQufLtn-ztHTEM5oIKqBgGuQ_K1_167KI6v7lypm7HiSV9kG7H33lRAjoc_w259Q8e8RxhmoBL9mhSAKjwnhfLYMtyfyCLbruvHSzqwpvzvGO6n6GDmADLDY_V2IK1UdNg7dqYkDfJA_CV-gV8Gx4o7ob252hZLqbEJc1Qrtv7IeSCbY4mBTOjfJSJMvEWtfKLbsRF9KOM39_yJ2OwO_C1S-nmeDWANKHgyjFvrtSrQIxlfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
السلام‌ علیک یا اباعبدالله علیه‌السلام
🔹
پخش صدای سلام قائد شهید امت به حضرت سیدالشهدا(ع) در بین الحرمین
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/668786" target="_blank">📅 04:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668785">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4a500869b.mp4?token=Y0S-YK4efo-U9u2lt-mQHfV-d8zSY8jbhqNXR3D2Pz-d_Kvpr2h4XtZcSDnT9dakt3Y_gcSAJe96Fl2j0ZWc2FWrZ1Z2pu6KrhHqBOMHzIfkbSYVaeZvE9f0TzTiB9GYiJ2mTLZRb-It-gehWLPIfgLfc-A3bAxOT1BbbpAFjTD1pKxsdcQLXfL3741dEPtfX9h4HdbtR7iiRLpAkrAvD3VMNOchNF8jHbpcbcI_EaTu9Z1EJjODllGuw_unCW3XIOIdq_zAl94kC0qY9RxnLLrCxCqRXcf7o57f4WmOMSgp2mYnpdPRo52e1rQFTKhqjsELj0HEnh3dzq54WILWGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4a500869b.mp4?token=Y0S-YK4efo-U9u2lt-mQHfV-d8zSY8jbhqNXR3D2Pz-d_Kvpr2h4XtZcSDnT9dakt3Y_gcSAJe96Fl2j0ZWc2FWrZ1Z2pu6KrhHqBOMHzIfkbSYVaeZvE9f0TzTiB9GYiJ2mTLZRb-It-gehWLPIfgLfc-A3bAxOT1BbbpAFjTD1pKxsdcQLXfL3741dEPtfX9h4HdbtR7iiRLpAkrAvD3VMNOchNF8jHbpcbcI_EaTu9Z1EJjODllGuw_unCW3XIOIdq_zAl94kC0qY9RxnLLrCxCqRXcf7o57f4WmOMSgp2mYnpdPRo52e1rQFTKhqjsELj0HEnh3dzq54WILWGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر منتسب به اصابت مستقیم موشک ایرانی به مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/668785" target="_blank">📅 04:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668784">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63d0380aa.mp4?token=otaWZ3AAcZEhoIqaOL5PcWAhiGBTm_zbVwIoJMR2azDgCQEtuAKAkZyIDXAV9LswjwZfYv8eqZueSYJaNqoWgXcnwDpIT_tPKHDr5Z5mMiBjIN1fPqhWzIi2i1FcAKUpOLzkktNNWNK-ZUzlc6SoRTjP5ueGDoxKyjqXAL-NKCbvt4YoiKzxQv8Udb2CFi6tCDidwsheGdLUtuNvooz3Ff6qLc21wPyd3pcLl2nm1x_8301snugQ5RMIEZ_ZUHrzsSc0yqpEC7xR-nmDbZ7-5aKLeyV4mmRctbrvSBsoXQE0j-TNDWBfwKIT3wy0eIWnPqpFTl5aAzClnIx4Z2yaZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63d0380aa.mp4?token=otaWZ3AAcZEhoIqaOL5PcWAhiGBTm_zbVwIoJMR2azDgCQEtuAKAkZyIDXAV9LswjwZfYv8eqZueSYJaNqoWgXcnwDpIT_tPKHDr5Z5mMiBjIN1fPqhWzIi2i1FcAKUpOLzkktNNWNK-ZUzlc6SoRTjP5ueGDoxKyjqXAL-NKCbvt4YoiKzxQv8Udb2CFi6tCDidwsheGdLUtuNvooz3Ff6qLc21wPyd3pcLl2nm1x_8301snugQ5RMIEZ_ZUHrzsSc0yqpEC7xR-nmDbZ7-5aKLeyV4mmRctbrvSBsoXQE0j-TNDWBfwKIT3wy0eIWnPqpFTl5aAzClnIx4Z2yaZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وداع با پیکر رهبر شهید در حرم حضرت ابوالفضل (ع)
🔹
پیکر مطهر آیت‌الله سید علی خامنه‌ای در ادامه مراسم تشییع در کربلای معلی، برای آخرین وداع به حرم مطهر حضرت ابوالفضل العباس (ع) انتقال یافت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/668784" target="_blank">📅 04:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668783">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24415cedbf.mp4?token=R-YHWwAGis0MNL_L_8dv3G-YHaPad_G0kScQNKxqBdMayYkITv3wiQgM4yE-4nPPmX_GClLNCQz31YVwAyYgOA8zS_lvuCvm44e_aXVxX-fsP3z88Bensg57B1HoftSle3pzvKIBk-vgtSmD4LE89thQUiC8unlK37CZL5wt8uneaKUShAZ7mawCpgbo6Blk9gv5N0NwesrA1fFIOUhgcTc5rB7pamFror8GEyrTNOp1jr7vzXT3BeU4QXrNIde283X7tGXFrufyRm0XJliThjy91382JWxOF9wmNd3dyjF5ptQau_P0N15o7S5QECMcQ8_SGVE7KIgtFyOfOk6E4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24415cedbf.mp4?token=R-YHWwAGis0MNL_L_8dv3G-YHaPad_G0kScQNKxqBdMayYkITv3wiQgM4yE-4nPPmX_GClLNCQz31YVwAyYgOA8zS_lvuCvm44e_aXVxX-fsP3z88Bensg57B1HoftSle3pzvKIBk-vgtSmD4LE89thQUiC8unlK37CZL5wt8uneaKUShAZ7mawCpgbo6Blk9gv5N0NwesrA1fFIOUhgcTc5rB7pamFror8GEyrTNOp1jr7vzXT3BeU4QXrNIde283X7tGXFrufyRm0XJliThjy91382JWxOF9wmNd3dyjF5ptQau_P0N15o7S5QECMcQ8_SGVE7KIgtFyOfOk6E4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت کویت پس از رسیدن موشک های ایرانی از دوربین های مدار بسته
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/668783" target="_blank">📅 04:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668782">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
موشک‌های ایرانی، پایگاه الأزرق در شرق اردن را هدف قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/668782" target="_blank">📅 04:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668781">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
منابع خبری عربی از اصابت موشک‌های ایرانی به یک پایگاه آمریکایی را در کویت، و ناتوانی سامانه‌های پدافند هوایی این کشور خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/668781" target="_blank">📅 04:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668780">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c0e9b164c.mp4?token=Jvy7cMO5pJLKGSU1KHPdJvOTo-RhsltsmAhTuhmw9hYcjHFvKbvIxhbsqlCvj1qMf8_vL85iVL7wGoXfcuY2OJIG6bNph6iSssTV5as3p_F4ww6e6FvXM2A3Uu5lIY1twWe__ff3nOEpkn4S-vgjWKGpxQbaTIWmeXpomkNmCjjcq4JM8LtN8I3JB-c8vyadSuAR75oDb6yF26fQRghmNidMwLWs8D-u2HPiVD0vnfoS76R2HhX6jQR-bFEY2FF2ATbZ6Td7t9uPVGulksYrGpREp1fpa568YFYU4vhVF9rTYZluD6ydwHfRBPlDzTYEcJtxkB-wSiqYwHo499M6ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c0e9b164c.mp4?token=Jvy7cMO5pJLKGSU1KHPdJvOTo-RhsltsmAhTuhmw9hYcjHFvKbvIxhbsqlCvj1qMf8_vL85iVL7wGoXfcuY2OJIG6bNph6iSssTV5as3p_F4ww6e6FvXM2A3Uu5lIY1twWe__ff3nOEpkn4S-vgjWKGpxQbaTIWmeXpomkNmCjjcq4JM8LtN8I3JB-c8vyadSuAR75oDb6yF26fQRghmNidMwLWs8D-u2HPiVD0vnfoS76R2HhX6jQR-bFEY2FF2ATbZ6Td7t9uPVGulksYrGpREp1fpa568YFYU4vhVF9rTYZluD6ydwHfRBPlDzTYEcJtxkB-wSiqYwHo499M6ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز اقامه نماز بر پیکر رهبر شهید ایران در حرم حضرت عباس (ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/668780" target="_blank">📅 04:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668778">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671c38ae1d.mp4?token=atgQ6pdiKWtQi363OQL-Idpq_hfVYnDuUPWxLyPwfnEkwn0Iw-80A0dlVHblITMWEtUUR3nOIIbql_R3cu3DDLnHRtL5P6ZsQ93Agh5SmhtaGE8Tc7-lH1ci0tPvXj6diBKfwFd691ASt5rj-BuhvSQTSSfoouBYa0Fx9QJT8I7DdSNta5ki4IRIgClxaasNBvDByD38Mc3LSfKRCMIX6sUVxFC7p9-GI8-6B3yqsIlFGyRW01lju6CTi7iH9RddXvgOuRjDKEK25IAh3X504UZGl_GDkczttTPFPPI1ngGp-MHuITMb21emVmbwWijKA4nrpQWHduFmxMWz5cLAaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671c38ae1d.mp4?token=atgQ6pdiKWtQi363OQL-Idpq_hfVYnDuUPWxLyPwfnEkwn0Iw-80A0dlVHblITMWEtUUR3nOIIbql_R3cu3DDLnHRtL5P6ZsQ93Agh5SmhtaGE8Tc7-lH1ci0tPvXj6diBKfwFd691ASt5rj-BuhvSQTSSfoouBYa0Fx9QJT8I7DdSNta5ki4IRIgClxaasNBvDByD38Mc3LSfKRCMIX6sUVxFC7p9-GI8-6B3yqsIlFGyRW01lju6CTi7iH9RddXvgOuRjDKEK25IAh3X504UZGl_GDkczttTPFPPI1ngGp-MHuITMb21emVmbwWijKA4nrpQWHduFmxMWz5cLAaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاش سید احمد الصافی، تولیت آستان حضرت عباس برای رسیدن به نزدیکی پیکر رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/668778" target="_blank">📅 04:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668777">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ارتش کویت اعلام کرد که سامانه‌های پدافندی در این کشور، هم‌اکنون در حال مقابله با موشک‌ها و پهپادهای مهاجم است
🔹
همزمان منابع عراقی می‌گویند که صدای انفجارها در کویت به حدی شدید است که در برخی مناطق این کشور به گوش می‌رسد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/668777" target="_blank">📅 04:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668776">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10964947d5.mp4?token=ArbWe4UW6AXsCUqJqOCBA8fidBnoeu6FONVOcAyiMZtgvFhmiOZQVittpxX3J4rQ7f4fv34BXndSVSb7lxZV25NaeUCn1isNGhv3vPxYzfgcrOBuCUw0-l35UblFzRpDG8vYlPLtE-VZLYPXG0PJFCHT7EFI6s-n33swNcivgGLQCdkc4Aai2E7rFAe-VQOf-f6oip6EBPnifhMxBWCMDPfkQQv3ZrXuBis8PQZJdM6pFsp_c1dz1PMqgIAtOuRQNbReaSy8eYBdzRBq7C2MmpVRQTZaSMo9oVTwP_A2vb1V1swoKxL3VGw5oFW-bN2GD9uhPHkNGWA0oXZRtJtFfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10964947d5.mp4?token=ArbWe4UW6AXsCUqJqOCBA8fidBnoeu6FONVOcAyiMZtgvFhmiOZQVittpxX3J4rQ7f4fv34BXndSVSb7lxZV25NaeUCn1isNGhv3vPxYzfgcrOBuCUw0-l35UblFzRpDG8vYlPLtE-VZLYPXG0PJFCHT7EFI6s-n33swNcivgGLQCdkc4Aai2E7rFAe-VQOf-f6oip6EBPnifhMxBWCMDPfkQQv3ZrXuBis8PQZJdM6pFsp_c1dz1PMqgIAtOuRQNbReaSy8eYBdzRBq7C2MmpVRQTZaSMo9oVTwP_A2vb1V1swoKxL3VGw5oFW-bN2GD9uhPHkNGWA0oXZRtJtFfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجارهای بسیار شدید ناوگان پنجم ارتش تروریست آمریکا را در بحرین لرزاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/668776" target="_blank">📅 04:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668775">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8GHL6IR3OTmgIH8YXHE9VEsNeBQe2AJM5jVrHSNlHYZ0lwsQMQcO62bNImj_MYb0OA3c0q8MY_2qv8ythyUEVQFFpqGbNMR5wCD2URhbmMKaSik6JIQs2UqIsPm-HeROyrm36fsdKVMbD-D0qVNUImi3tWTkF2mS3eLPdJKp2mytEevgfJGBRWmE7gBVW99joxJo7bW8_qIgzSgZqY4923XnIWWQGQsX54QTtC1kRP3VkWEPE2GLHUVkwS_R3iVtiw70MKcKqGrGZPQuTXZDLWYs_Cq3oxdCUsLrD3UnAyUdeNamS8SzY99VbLHOvBpgJPtdyG9a7ipDLyfG3yLmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: منتظر سیلی سخت ایرانی‌ها باشید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/668775" target="_blank">📅 04:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668774">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
وزارت کشور قطر: سطح تهدید امنیتی افزایش یافته است و همه باید به باقی ماندن در منازل و اماکن امن پایبند باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/668774" target="_blank">📅 04:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668773">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693ba173db.mp4?token=GR7VaMwpMEKn4-TU7iPFJzZSGMwJlCcZxVfNzNjI-Kvj84P7WwQ_x8_S7WN8C8KHqMC1srJtgidiwOznrg0v3vLK2bm1l0RSiKh3Z-RhYyudGMBNXwBymCxFeimTQa02aU4MjTZSBl3MVJ0FkgkW12OqX7SyYwL2vd3zc6ilbz2V3IU2rqCQOEIcAq13pGXwwWhFa0gxL-PCsptf8oGsLMZkJqWfskP4AJ2lc-sCHn7rlZI0q--0wzLzf4rjtnn9Yaoh4t3kBxx-nxwX4G4T6pTvIU3T3-MT2LhtApaBCX72AIIAibk8gp93veag-vaaxM-Ju5ETTrU0kG_RzTYs-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693ba173db.mp4?token=GR7VaMwpMEKn4-TU7iPFJzZSGMwJlCcZxVfNzNjI-Kvj84P7WwQ_x8_S7WN8C8KHqMC1srJtgidiwOznrg0v3vLK2bm1l0RSiKh3Z-RhYyudGMBNXwBymCxFeimTQa02aU4MjTZSBl3MVJ0FkgkW12OqX7SyYwL2vd3zc6ilbz2V3IU2rqCQOEIcAq13pGXwwWhFa0gxL-PCsptf8oGsLMZkJqWfskP4AJ2lc-sCHn7rlZI0q--0wzLzf4rjtnn9Yaoh4t3kBxx-nxwX4G4T6pTvIU3T3-MT2LhtApaBCX72AIIAibk8gp93veag-vaaxM-Ju5ETTrU0kG_RzTYs-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقبال عزاداران عراقی در حرم حضرت عباس(ع) از پیکر رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/668773" target="_blank">📅 04:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668772">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
وقوع انفجارهای مهیب در کویت
🔹
علاوه بر بحرین و قطر، پایگاه‌های نظامیان تروریست آمریکایی در کویت نیز هدف حملات هوایی ایران قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/668772" target="_blank">📅 04:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668771">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe0a68bb73.mp4?token=XaNZ4BzUN3C_lMgXnlb8jwgfNgzto8tfmr5P50MqYdcZzyWhknxoOJakzDEJRJEAQIaSqlKE-EGvoVulkyyrDLiiGAWfW3i66bWS8zChJq6nGNZ72WPzLedXhA38PYA7p6QcvJzeR8-euHhapEngEPeyUWicqNX5B4iazMIUrlTuBL0prYq1mIob7E_8GlJWjbQfkaindHvpep__Dnl5XUi8ibQG4iEjOXCE3onv9cjhBwikvexRTzEdn0VyGQnUNH-jg-LrWW2MbA9CJsimkmllJHVhsUSrtm4d8rfOXNlZP3a8MBLrqO39_JwvUoardy23KZmaPE26HxF2ErhQ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe0a68bb73.mp4?token=XaNZ4BzUN3C_lMgXnlb8jwgfNgzto8tfmr5P50MqYdcZzyWhknxoOJakzDEJRJEAQIaSqlKE-EGvoVulkyyrDLiiGAWfW3i66bWS8zChJq6nGNZ72WPzLedXhA38PYA7p6QcvJzeR8-euHhapEngEPeyUWicqNX5B4iazMIUrlTuBL0prYq1mIob7E_8GlJWjbQfkaindHvpep__Dnl5XUi8ibQG4iEjOXCE3onv9cjhBwikvexRTzEdn0VyGQnUNH-jg-LrWW2MbA9CJsimkmllJHVhsUSrtm4d8rfOXNlZP3a8MBLrqO39_JwvUoardy23KZmaPE26HxF2ErhQ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعالیت سامانه‌های پدافندی در بحرین
🔹
برخی منابع تصاویری از شلیک سامانه‌های پدافندی در بحرین برای رهگیری موشک‌های ایرانی منتشر کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668771" target="_blank">📅 04:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668770">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در شهر آق قلا استان گلستان
🔹
دشمن تروریست آمریکایی به یک پل راه آهن خارج از شهر آق قلا حمله کرد.
🔹
هنوز هیچ منبع رسمی اعلام نظر نکرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/668770" target="_blank">📅 03:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668769">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3udZO0nbTUkrR-DGf7-f7wFfhC1QDL-aoG2-y0uOyYvkXXwTKdVXMVYd3QdrD7c7-cHr-O-bE6DII2rmKxGvV-jLUulr4wDIyyvA8hMiKo-e7C2BsoBTzo4VrvryuZWvykcvLHeBJjwWwpnICNLnqVq4Oi5UwfRw3LeqkJa-G9GKBvfCAX3g2msU1bKTSWjTim0l6eaCXHfTwBSNzEHVR2mRyYnEtxuxuGVZqFZ1MX4vYFeyk-zjWcQ8SN2CqiqkYvFsuMvEkbEYJyz5ElXGp6IFE7WBMh7kDBDNbUWD3CQK9AUZh8ADer4_-iJNo451Xtw1-2tu9J8TdNsCgAe8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیکر رهبر شهید از حرم امام حسین علیه‌السلام خارج و وارد بین‌الحرمین شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/668769" target="_blank">📅 03:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668768">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de25f04d4.mp4?token=sXVfBGxxRS71d6lL5t-g428Lx1CdVlkkZjeZNtT-8BMNodc_dLlnCwvNCkgIqqagOviKk_629Y9L3Bs58mGV1eIsfRyTa4hk3WmxFhwjv0NAJWU95v5MGwPPYe2RYsCRLmWyn4g9mDz7UoXJFMawLj4kg4eQrr0HdFHyLkRTzCNewdMUWguLG1weqk-igHtMN_hjjWsMFdXleD0EAFCtJY1erF5l8AW5fZV9ICLT0i2gEbi9RSkGIdnAwfS3xSnOJkLwH6cD20_6DqtqSiAikFvIJta9n5_q-66fTNXHAIgmlTW6uAYZyrK4y5nlWanyQsUn_DQtNIQcRp4TFyU4ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de25f04d4.mp4?token=sXVfBGxxRS71d6lL5t-g428Lx1CdVlkkZjeZNtT-8BMNodc_dLlnCwvNCkgIqqagOviKk_629Y9L3Bs58mGV1eIsfRyTa4hk3WmxFhwjv0NAJWU95v5MGwPPYe2RYsCRLmWyn4g9mDz7UoXJFMawLj4kg4eQrr0HdFHyLkRTzCNewdMUWguLG1weqk-igHtMN_hjjWsMFdXleD0EAFCtJY1erF5l8AW5fZV9ICLT0i2gEbi9RSkGIdnAwfS3xSnOJkLwH6cD20_6DqtqSiAikFvIJta9n5_q-66fTNXHAIgmlTW6uAYZyrK4y5nlWanyQsUn_DQtNIQcRp4TFyU4ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتمام نماز بر پیکر رهبر شهید انقلاب به امامت شیخ عبدالمهدی الکربلائی، نماینده آیت‌الله سیستانی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/668768" target="_blank">📅 03:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668767">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d0174baf8.mp4?token=RWtSJ1GcaMpXwoTpJsqjrX89ZTH2FBwryY4VtTjcD6FIYrt1s3sYoAVEYMytPW5jqQF8sRYWz74S6l4iCbtoksHUxLZ8PcTRQxhxFvzRkyHb9CDDEhyasanMZ_XIRtaI0EA0NFEOJyG8Lg5WdB1ty98T0BQW-j-NaTkDSfuq73iS3rjWxQqOUt9kt3CzwCHphERci9PGToUUuSyJNWfMM5_NV24v24flf5XNvsVmGPrizTnl5mTqvYf-44_nKO2RibZSIinK8vqVCkz8J3Esrkler3q0baxKkhZhSkgLCQGy54rPnHf4EPVdRBhxArpxS10ON_CeDfWHg6ce1IEK5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d0174baf8.mp4?token=RWtSJ1GcaMpXwoTpJsqjrX89ZTH2FBwryY4VtTjcD6FIYrt1s3sYoAVEYMytPW5jqQF8sRYWz74S6l4iCbtoksHUxLZ8PcTRQxhxFvzRkyHb9CDDEhyasanMZ_XIRtaI0EA0NFEOJyG8Lg5WdB1ty98T0BQW-j-NaTkDSfuq73iS3rjWxQqOUt9kt3CzwCHphERci9PGToUUuSyJNWfMM5_NV24v24flf5XNvsVmGPrizTnl5mTqvYf-44_nKO2RibZSIinK8vqVCkz8J3Esrkler3q0baxKkhZhSkgLCQGy54rPnHf4EPVdRBhxArpxS10ON_CeDfWHg6ce1IEK5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حضور شیخ قیس الخزعلی دبیرکل جنبش عصائب اهل الحق در مراسم تشییع قائد شهید در کربلای معلی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/668767" target="_blank">📅 03:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668765">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UqG2uFGrjS9ZxpLYoVuqZKSJsa3dPC8w-CiI387n7s23nFtVmDPtPdnxrxLjtFDlRNowuKLmwdVRybBULGEh3V3hI6Tagijwt0ZJorbCG3IcviHnQ4CixBg8BxiDes7LS7LMkXbzkhBXJ5hi3NfIDUF6cIFshMsXHy9mrmV_Tjiz2tZCF71uthFM8K4y99hbDQydnj1BwJ4rLzAp3LgdjOfw0Ikln6SCCF7u5j_Er_rAa5sHqoQA9CppUYzEzTm5IwsVQxHazTQEeplCxUb15EYvujJc8URYEnanj3bxDrG965DaGQLg_W7n1ac6HBxDjSTU6c98gXgilaQucISSGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6OT4WEckcVBkvxz66mDiatYocdqusXPFjVzdBno3ISmmF8ur_ElTLQ0wXJbNCW8ptS5mCQHzhJMFjtDcVODKjhcxIYiGkkIqrO0aiJOpPHwmyHcFyySLs0ebD5g5GwttwrFVYQNeoZ2-SPGB6vg_1AKSsZv4hqxksSEOgZ8onJafh3w6b-WFr6wQ8tfVJKk-bk7uuGQZEPvNRB3_r_NC77BwKNgs7IXO5I44QbwQB5hqVUK4X56CdH1Pb4k_psc5zu5FWtN0qpnU_Am6e43pSPxMjqSr01GqMRvLEWqcLb4dV-tx72oxpDAcjsD_GKwPt7WsFoCuq3Onwq5oXrRwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از لحظۀ ورود پیکر رهبر شهید انقلاب بر دستان مردم عزادار به حرم مطهر سیدالشهدا(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/668765" target="_blank">📅 03:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668764">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در شهر آق قلا استان گلستان
🔹
دشمن تروریست آمریکایی به یک پل راه آهن خارج از شهر آق قلا حمله کرد.
🔹
هنوز هیچ منبع رسمی اعلام نظر نکرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/668764" target="_blank">📅 03:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668763">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550128c2f0.mp4?token=nQJ9Cmm4iNqw308HkVVl0LFDXZ6hOncDmYjjfKdf00yHinhwkjZAf-M3RCi7IID7AEd70lDQVXh_13WUDWBiYQRUNLZ8DXsg1R8z-G9SUM4rHGLLAdccbTOhSQaeHg4UPU09Rr6IUh_aum3XVcfc_3kM4Asko8_5XOCOqVRrekjyksdzcjQdrNu6JEQ3BP8TbHcwfueX4QDAPIl2D9p56-CJ_bdeOT2b1TlTQ2HiCEaav_IQKSH6UBlLuwMqnUKNdbkuudZYNsmMpVBBaWr_9rFOJ2ehnj6tlDnoEWJ5Y4FY0NSXmYiV_YVLDmYdKmv0Zt4Jswo9l9nC4jt0zj0hk7mnLqhFTa2cjDNQ-wnGDX5n6S86cpGC3SGz-uewEdoCXp61NygwQ853_l6KBi65iQ41bf2PBux60QKwuqxad0rgTKsovCrtSWEMirbkEVO5xTtFAWd6swGM_mvO4Kf00KSR3XmngKjM9WkP6leniA0aMWLLXaktgypafOgykF4gt_biIOiu_W0vZxfrzfi8M5iQW3DndIzPvb0pICtOaPDX-C52LaTMH-U-nC4l8P9OZnuY9D0fKHT9TettTSsTUiY2dYQeRHYxjCj8s07djy48n_I4yEqq6nZYvCLHKqfL4NtOmC06jy3zISUra4fVPhaoTuNaJ21mChsveTCwyyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550128c2f0.mp4?token=nQJ9Cmm4iNqw308HkVVl0LFDXZ6hOncDmYjjfKdf00yHinhwkjZAf-M3RCi7IID7AEd70lDQVXh_13WUDWBiYQRUNLZ8DXsg1R8z-G9SUM4rHGLLAdccbTOhSQaeHg4UPU09Rr6IUh_aum3XVcfc_3kM4Asko8_5XOCOqVRrekjyksdzcjQdrNu6JEQ3BP8TbHcwfueX4QDAPIl2D9p56-CJ_bdeOT2b1TlTQ2HiCEaav_IQKSH6UBlLuwMqnUKNdbkuudZYNsmMpVBBaWr_9rFOJ2ehnj6tlDnoEWJ5Y4FY0NSXmYiV_YVLDmYdKmv0Zt4Jswo9l9nC4jt0zj0hk7mnLqhFTa2cjDNQ-wnGDX5n6S86cpGC3SGz-uewEdoCXp61NygwQ853_l6KBi65iQ41bf2PBux60QKwuqxad0rgTKsovCrtSWEMirbkEVO5xTtFAWd6swGM_mvO4Kf00KSR3XmngKjM9WkP6leniA0aMWLLXaktgypafOgykF4gt_biIOiu_W0vZxfrzfi8M5iQW3DndIzPvb0pICtOaPDX-C52LaTMH-U-nC4l8P9OZnuY9D0fKHT9TettTSsTUiY2dYQeRHYxjCj8s07djy48n_I4yEqq6nZYvCLHKqfL4NtOmC06jy3zISUra4fVPhaoTuNaJ21mChsveTCwyyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی دیگر از ورود پیکر رهبر شهید انقلاب به حرم مطهر امام حسین علیه‌السلام
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/668763" target="_blank">📅 03:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668762">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
فوری/ نامه رسمی ایران به شورای امنیت درباره تجاوزات آمریکا
🔹
ایران درباره تجاوزات رژیم تروریست آمریکا برای رئیس شورای امنیت و دبیرکل سازمان ملل نامه‌های جداگانه ارسال کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/668762" target="_blank">📅 02:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668761">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7o6dLSqbK5V9V_ypx1s0l1lt6Z42_uKNLKC_0d071OjP0Hcq9zZNF1aXZnm0t2VQEdDsN1VbkWTQf7fbbE5zdNf9s7C2bvMFK9XgNfNDvmDozBzgy05iLV3tXZT5XNX0oxbAJU6H2dwK3Ni225JYLspWGi7UC07ufF0NfCzgRlGC3aps302zMxT00VECOOJ8Ms6XHmrObCxZKI8vLC3usp7zv5sk7dp0KJ7mrD95h8FEsKVdo4JMMzTlEdhA89T88eYKH3viIQP2V7QB82771po9ipEYiU0VPzH5DR57PcmHDGmxITkcoqqFskq5ZYYSBRUfYw1YFfg7NeZi6g5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری هوایی از جمعیت عزاداران در مراسم تشییع پیکر آقای شهید ایران در کربلا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/668761" target="_blank">📅 02:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668759">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTrW8xgGJZXmlZ-M_DbFLVsrD02OkwH0DMgnxq4P8yplnHoivxkUH5aOAtzWRgghiWZ9y0xSaU6kqjrnQq93nha8O8WxFN5nUCr2228MmJ2J7OFcBjcr8iV3OlZG-bs1houqZd5VwaNhYrASxnEdF_ykz1tfuQ_KTZtTb6hX92f1gQbD8XcxLpK577NWnK114UQlizWVNXMFMNhLTd65gFuaeuEDqGfbcHkSvL3Q_jEXGhAU9XrAhI-rIo5ZUZPXGiCgbLLBsEz2EwHnHGGpCSmrKu94x8UxP44yCt4d6yohK-Da_tb6cQF0uOnSOGgRLTthc2GDAI7Nx5dXQUtWoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ما ترامپ را خواهیم کشت
...
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/668759" target="_blank">📅 02:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668758">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb3e36225.mp4?token=csFQTuZ01eheCxaCunDoHl4VQflNjwVs5E1kKMaUsw_RsT84iUimXfMly_hUF-OAy_36J7GsH17F6RGWKXIsD8k7H8DNEuPqJV3ZnW1odaWxMtICJq6j8ESf3f3-E1f5yyx1pZ6gFWS__2KrU-MVNssj53l6CyZeJhXphO8_eeymv4kq7s9NGX2QP_fJMWfrDdlL0450WNI9xqJwSu5x4ID8XqZSXaWXXEUE7ufY2YpZwvn2LTHWBZTKXnsC0nTh3fJfkFy-W3Xt_tdpjxWr_BUDH922w1KeoDXnsRT5Q2zPpt0GXQXFMX1z0X1kKAongWVBTcdaesWYxg96M0yo-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb3e36225.mp4?token=csFQTuZ01eheCxaCunDoHl4VQflNjwVs5E1kKMaUsw_RsT84iUimXfMly_hUF-OAy_36J7GsH17F6RGWKXIsD8k7H8DNEuPqJV3ZnW1odaWxMtICJq6j8ESf3f3-E1f5yyx1pZ6gFWS__2KrU-MVNssj53l6CyZeJhXphO8_eeymv4kq7s9NGX2QP_fJMWfrDdlL0450WNI9xqJwSu5x4ID8XqZSXaWXXEUE7ufY2YpZwvn2LTHWBZTKXnsC0nTh3fJfkFy-W3Xt_tdpjxWr_BUDH922w1KeoDXnsRT5Q2zPpt0GXQXFMX1z0X1kKAongWVBTcdaesWYxg96M0yo-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای مردم عزادار در جوار پیکر مطهر رهبر شهید انقلاب در نزدیکی بین‌الحرمین
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/668758" target="_blank">📅 02:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668756">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادعای شیطان زرد درباره ایران: ما همین الان ضربه بسیار سختی به آن‌ها زدیم
🔹
می‌گویم که نسبت ضربه ما ۲۰ به ۱ بود.
هر بار که آن‌ها به ما ضربه بزنند، ما ۲۰ برابر به آن‌ها ضربه خواهیم زد
🔹
وقتی آن‌ها حمله کنند، ما با شدت بسیار بیشتری پاسخ خواهیم داد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/668756" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668753">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ubfk4hFIQCpjjvD7kPg60BP6qV2_8lL2TNXnnIPNShAIxrk4XBJmVec1-MEV-BoehGZ0RbcmiKt5GJDOmPalhHMpq2HiTYm3EpE-NQy34gxmr4bp90gq_PUGrXXFl6LAMIIz43hGLWY3Vee7K_u0yBEpy3EpMxaBk59NTRFnaR6CVD2pcqVysVrDrphyNPQcShd4XW3fEDCfZeTwByw3YY5oetyclQtI7yT8aFsFCL4N2QsK1T5tnxXvXl2Z6C7gSKJMXW6TtuVLRhnKzeWkowrw1nR3Hj7ym07iWmTNT_zCQZzS4DdYpdTMDSpkQvyi9Ux9nHkF-_F1UuVitB4oVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uW7RUFgaphgSDyUwly8NO4pX4lSksDMuk6Yve-rrDWSkOVII-_ova2V27ZYz6jd4I1NCRXkhdEn20CGWyQI0NDlUbb8Kn2sXW0KNXVNhqljW0avpiTJ9HlfhuskLZYTA6JToicctxmR8ktRocClv-qx8mawEzKAtCT2Fu7MwRSvAQUMKp4WXuL4zhR0_yjPfMOIaRBFAIlYp8Xe9UP6k3ytf6QGnUwzFHGfK4z3p_SE5xpCuWTbVGPF22IKPJkZfqoUy3svDHjTGxiZieW0_PkVz5VcYEHpfiMupDs7wmL5h8LG1xa8dCuz35k38rKvOEG14wdPfwof8piXI9crCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4QzUsHS6yCI2SSxQyWy_3jPhG6iDLrGzRmhSUILCeXofGDIwkSUtcsHhiVLArLBNZPVphz54u5CHhGlwc5s_MeBOZPIH47lbujizcev8YEHym41a_4WjEwQ-2GGGqJtW0lPnORCOhIBof2XLhknbmHKm5Vxl9yAvSJ3JUGoOM_e4LMCEntjg7xlLP--vdLY0OoGHoPJZyjkZUOPPEOeFKtW7Z3H2P3Ck1tCt7o-J92zWZgq8OgT18xZmVc1Bk-FPX-g2pmGM1w9y4NkukhACjMyrJLL16vaN0T0H5jjsXuphSZylwD-a2stid7rzISWq5JCE0XFtAcVQfNJrosNKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انبوه زائران در بین‌الحرمین در انتظار رسیدن پیکر
رهبر
آزادی خواهان جهان
انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/668753" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668752">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
نگرانی اسرائیل از انتقام‌گیری ایران از تجاوز آمریکا
🔹
رسانه‌های صهیونیستی هشدار دادند که احتمال دارد ایران و حزب‌الله در عملیاتی مشترک، به سمت فلسطین اشغالی موشک پرتاب کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/668752" target="_blank">📅 02:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668751">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65366aac01.mp4?token=CP1TnVO5xvOugxH5Ph71gCphMDPyBxF6Yy087ApeuQ8exxXH0k1nrrMB0avo6zKZqR-p1-f62zRsQt3BNIfwPSPwfozu3lpQYFM_SHtF62Oui9DalY4WTsKEYlkjIq3g2vB6E1JiP3gViGL9MW6XXVMsVQ21nT3WtMn05KHaCBWhEBly7FDOMkn6SUt-QjmBUFiJvbuZ76c3_aK8L0U6BzmM7HBI34BHoZveeXb_nBfBgnyFHq1oxPcyM2dzUisOUFAQqd7OGj2y4IFhjEt2P67VIdXGoXgdevg3FaP-RwAiQ7W831K5ipSI59IGLBJ6RcdU2ugQ3KjnFG5-XK9yQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65366aac01.mp4?token=CP1TnVO5xvOugxH5Ph71gCphMDPyBxF6Yy087ApeuQ8exxXH0k1nrrMB0avo6zKZqR-p1-f62zRsQt3BNIfwPSPwfozu3lpQYFM_SHtF62Oui9DalY4WTsKEYlkjIq3g2vB6E1JiP3gViGL9MW6XXVMsVQ21nT3WtMn05KHaCBWhEBly7FDOMkn6SUt-QjmBUFiJvbuZ76c3_aK8L0U6BzmM7HBI34BHoZveeXb_nBfBgnyFHq1oxPcyM2dzUisOUFAQqd7OGj2y4IFhjEt2P67VIdXGoXgdevg3FaP-RwAiQ7W831K5ipSI59IGLBJ6RcdU2ugQ3KjnFG5-XK9yQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
فرزند شما فقط برای امتحان آماده می‌شود یا برای آینده؟
🌟
دبیرستان دخترانه هوشمند مدبّران (بارسا)
🏫
✨
در مدبّران، دانش‌آموزان علاوه بر موفقیت تحصیلی، مهارت‌های زندگی، اعتمادبه‌نفس ، تفکر خلاق و آمادگی برای دنیای آینده را نیز می‌آموزند.
🚨
ثبت‌نام آزمون ورودی آغاز شد
🚀
📩
برای دریافت اطلاعات و ثبت‌نام:
🆔
@modaberanschools_bot
📩
یا عدد
۴۴
را به سامانه پیامکی
09982003159
ارسال کنید.
📲
❗️
آشنایی با روش‌های نوین آموزش و موفقیت تحصیلی
👇
🆔
@barsaschools
📍
تهران</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/668751" target="_blank">📅 02:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668750">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d2bcb646e.mp4?token=WZsQwwbRP3VrtIbuJd9_4j6ciSgBH8GGwwQlMcgg44kPcgGZpW6T3cpaXaTJKmDhMD1xIjMOqGLorYk62wuRtsX5PwRGth2cNpsCwoZxAZqc9aJa_ABLihB6271xOLsik72v0R0VKJVfsWZ8XgYFNzOjd-6ZFXelaUoOtYjEJPL9q9ihMFnZkZaqpqpnR_4lMCAylAmUZaE7Dhx7vtEKAESMK74N-_euY0cBWK9Fb450IRDLp2gwMr5w1v2ERTh30DCdThperC8pQGrCArhQY34_fmHIv_QTUC5128zXebCbCFQJ90o-lwx963ahFahSXIW2Q7bQlZottIG61D8xAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d2bcb646e.mp4?token=WZsQwwbRP3VrtIbuJd9_4j6ciSgBH8GGwwQlMcgg44kPcgGZpW6T3cpaXaTJKmDhMD1xIjMOqGLorYk62wuRtsX5PwRGth2cNpsCwoZxAZqc9aJa_ABLihB6271xOLsik72v0R0VKJVfsWZ8XgYFNzOjd-6ZFXelaUoOtYjEJPL9q9ihMFnZkZaqpqpnR_4lMCAylAmUZaE7Dhx7vtEKAESMK74N-_euY0cBWK9Fb450IRDLp2gwMr5w1v2ERTh30DCdThperC8pQGrCArhQY34_fmHIv_QTUC5128zXebCbCFQJ90o-lwx963ahFahSXIW2Q7bQlZottIG61D8xAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابان امام‌رضا(ع) مشهد، ساعت‌ها پیش از آغاز مراسم تشییع پیکر رهبر آزادی خواهان جهان
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/668750" target="_blank">📅 01:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668749">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
حمله آمریکا به برج مراقبت کنترل ترافیک دریایی منطقه آزاد چابهار  مدیرعامل سازمان منطقه آزاد چابهار:
🔹
در جریان حمله ساعتی پیش آمریکا به چابهار، برج مراقبت کنترل ترافیک دریایی منطقه آزاد چابهار هدف قرار گرفت و آسیب دید. در این حملات یکی از انبارهای منطقه…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/668749" target="_blank">📅 01:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668748">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d748eb74f9.mp4?token=rpQVNegCCFpV9C6oC7ZLlF_uRnE5LYfhQfB7YJf7UkHNbftVzTr-g6OfKwJt-aYrwrpW_UqV-yXmbALXwoGIBQfZ78Mocz1AAmyX_LJlWkV74A74HqzgWni7mKWHHUdCLxgEvw-AGLH6CrgTTAmzXrnhxjXa5PSiq5cyzb5ERj1BYHrKz-3PDk2_fgegIEAOxt6VCoorcov_BgBRfm4u9e-pdYUSCc6_eA_cZOfC8lFoiiS3glo-v_QRJX9Re5oECfqU7DsoAjdTtTBEwzAdMpAawqABNwz2LMXeTSNIveu-vp7D-QAM61TDl_Or0bVy7auI5PxNzCAkuCZEx4nobw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d748eb74f9.mp4?token=rpQVNegCCFpV9C6oC7ZLlF_uRnE5LYfhQfB7YJf7UkHNbftVzTr-g6OfKwJt-aYrwrpW_UqV-yXmbALXwoGIBQfZ78Mocz1AAmyX_LJlWkV74A74HqzgWni7mKWHHUdCLxgEvw-AGLH6CrgTTAmzXrnhxjXa5PSiq5cyzb5ERj1BYHrKz-3PDk2_fgegIEAOxt6VCoorcov_BgBRfm4u9e-pdYUSCc6_eA_cZOfC8lFoiiS3glo-v_QRJX9Re5oECfqU7DsoAjdTtTBEwzAdMpAawqABNwz2LMXeTSNIveu-vp7D-QAM61TDl_Or0bVy7auI5PxNzCAkuCZEx4nobw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع نمادین آقای شهید ایران در بحرین
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/668748" target="_blank">📅 01:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668747">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4481c2c676.mp4?token=vXtUo_fAilhvTs-1OCeR18cNsQGAj5jrOG4qTqc9IHA_l_QajJVqIOSyNC8cU-QEeS3-8xfaNsU6on0aTvb1cFcNAGJ-pizj8xn5Jf9ZlcEw5AGtjfDUVHLklRb7JNKhws93DH2GfqU2SZaXQyqTcFi67UfzuZqO1flquh1z8Mm9mZTngkp0EkF33ztK1NVVschEbn8uAJGCTc46kLqVPGfe7-a4y857PLH4HaiLUI8hKM1fGwnuPCvmJClBKW2ogCoStkKodkZEs30mGVP0M8LrOyeo3AwvJYS8itQd-ZTotjH39P7BFppYH4yXEL1V_nJFMCdTognbN4Hbmmxb_kxak-TEivY6r1GH7CLNdDfg1Os0gux9DFwVH7Q9_iXCa1fntcCEeUPbZIkMmn8AXVvGzFNZOStBBSSxImhhb8TtrT2IaFSn4aQt2WPd8SQ1sLos1ctpbvbq0DLCgBHXX1W8fF0C7rurZsoJHII33ODBPLA0HntNst1g5nSf7LEudal_mZeEGg3Z8AX4_-CKjw5oe1L9T3OpNLdvhsAC2RCOQr2sClPfx5Sx_Rh7lIIJJfh1W3c_VsLu2Ljn0LDO55QRFrENoH8veQ4cKkwoxX2hAkNY3ceB-xROhHxSaBZzLVN2eTlM2uA-L1hp16UtNIygb_khEycyjVZhSi1GFvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4481c2c676.mp4?token=vXtUo_fAilhvTs-1OCeR18cNsQGAj5jrOG4qTqc9IHA_l_QajJVqIOSyNC8cU-QEeS3-8xfaNsU6on0aTvb1cFcNAGJ-pizj8xn5Jf9ZlcEw5AGtjfDUVHLklRb7JNKhws93DH2GfqU2SZaXQyqTcFi67UfzuZqO1flquh1z8Mm9mZTngkp0EkF33ztK1NVVschEbn8uAJGCTc46kLqVPGfe7-a4y857PLH4HaiLUI8hKM1fGwnuPCvmJClBKW2ogCoStkKodkZEs30mGVP0M8LrOyeo3AwvJYS8itQd-ZTotjH39P7BFppYH4yXEL1V_nJFMCdTognbN4Hbmmxb_kxak-TEivY6r1GH7CLNdDfg1Os0gux9DFwVH7Q9_iXCa1fntcCEeUPbZIkMmn8AXVvGzFNZOStBBSSxImhhb8TtrT2IaFSn4aQt2WPd8SQ1sLos1ctpbvbq0DLCgBHXX1W8fF0C7rurZsoJHII33ODBPLA0HntNst1g5nSf7LEudal_mZeEGg3Z8AX4_-CKjw5oe1L9T3OpNLdvhsAC2RCOQr2sClPfx5Sx_Rh7lIIJJfh1W3c_VsLu2Ljn0LDO55QRFrENoH8veQ4cKkwoxX2hAkNY3ceB-xROhHxSaBZzLVN2eTlM2uA-L1hp16UtNIygb_khEycyjVZhSi1GFvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین قاب مشترک از پیکر رهبر آزادی خواهان جهان با گنبد حرم مطهر حضرت ابالفضل العباس علیه‌السلام در کربلا هم اکنون
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/668747" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668746">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOXh2Rb4kZE7q5RiFhfGkG3bYA_95SNYPZzf4uj_AFPL6RVv7YV3GZRED2MX8C-QKdjZxFR4H_-roX1EPiwbYPY8TuHfgrgYwHSG5ikgfWLBjH0V22qTT5nY4qf32F3p0i6rOTwjjSj3rv0jBWzKHHnNamKuf6SQkEUQuN3jCqWsHu-w3cr4NlEksfLcYMAbSj_hp5c9ZOHLHE1fw0Pl3pxfK5hE2nnyvJd0oVOJjFBW_MZyzIZ_X7gPNAxVleLWLENPeV0OfX8N0K15qfMIT_8lMF5kfAJmMglHM0LQkEA3GyWlwyFjlMoSAZLqF2N0q-toKJ-WvJVYQbvQ-joICw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماره مزايده در سامانه ستاد:5005095004000004
موضوع مزايده: بهره برداري تعدادي از بازارهاي ميوه و تره بار سطح شهر مشهد مقدس مطابق ليست هاي مندرج در اسناد مزايده به اشخاص حقيقي و حقوقي واجد شرايط به صورت اجاره .
مدت و مبلغ بهره برداري: به شرح اسناد مزايده
جهت اطلاعات تكميلي به سامانه تداركات الكترونيكي دولت ( ستاد ) به نشاني
www.setadiran.ir
و همچنين جهت اطلاع در روزنامه رسمي به نشاني
www.rrk.ir
مراجعه نمائيد.
#مزایده
#مزایده_عمومی
#مزایده_شهرداری
#سامانه_ستاد
#سرمایه_گذاری_مشهد
#فروشگاه_شهرما
#شهرداری_مشهد
#بازار_میوه_و_تره_بار
#سازمان_ساماندهی_مشاغل_شهری
#واگذاری_فروشگاه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/668746" target="_blank">📅 01:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668745">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSAZop9eBdFBbgMiB9ntW0_UzI3y8eV6Elu2MU4czPbBIWTAhxRikFuFIsEEhhgcGRs-WWtKSo8g_kf3dxyoxBLCZkYfmyFPxg2R1xOAp8VIMDwyNuKqq7bXIqy37rpLHrSqO45_DaoRO37queaSqbmfCVDTkAavp2jfri47UmQhCgSU3Gc1v4074HbnQ8DEYeOK_VbQ0MK4kukQuaJgXQFjU3TKZSGZmixIrdKfeeJ_Slv7bI75rffmVp2mWU-Tf5LLA0cKfTXS2x8_GHXHd4L2FpC8nTW7My9k-xWnYNbTf5u5yY8h5YBkW3VB9zedSd-LN9sbd7_Oa7nOR84ZYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود بر ملت و دولت نجیب عراق؛ شما معنای واقعی برادری را به جهان نشان دادید. صمیمانه از شما تشکر می‌کنیم.
تحيةً للشعب العراقي الأصيل وحكومته الكريمة؛ لقد أثبتم للعالم المعنى الحقيقي للأخوّة. نتقدّم إليكم بخالص الشكر والامتنان
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/668745" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668744">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
پایداری برق در اکثر نقاط شهر چابهار
روابط عمومی شرکت برق چابهار در اطلاعیه ای:
🔹
سه خط برق در شهر چابهار که براثر موج انفجار قطع شده بود، دقایقی قبل دو مورد از این سه خط برق دار شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/668744" target="_blank">📅 01:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668743">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d112d822.mp4?token=qwkkvxyuOk3IWEvJsgEhJb7oy2gghowbXNMijVbGZvoen-HySxGq3NM-v4EwbWgBZPDMhYvnCLszWEHo_COl8t09JvNjydcefmbKYCCylG8KiVY7LNbXPSzoXqmcJ1ke3pIQm4S0KnhAHx0oZDrjQk1ShdFnoNfH39va-3JjLxGR9e4-jIbump8w-CR6IRcT94km4fvNcblIEhqlQrpPNElI6QG5CeitoF6lQT8--9USy2pxwrEACWhoQlLfsIwvOgANvc2pnbCl7VqBxvyE3Wn9u6FHgD7CBxeXfZk2BJSukcNo2mlBBF391wpJyAVn9xJxK4uLPd-4Ihi2AJ7celA9DmqwAbkqww5kIb95jnMG9Vscpchg74CzgKdRgPUdE9EYOI4O7rNTliid5qq17ThTPQpGtO8UnWrdZZs9a5hh54fUo5hQjBGkekv2sLPjGdD2JYFI9DSrB6RK4yOMR_kb0Yb1KFzRY9At0YLlzh_Auh8CbzYKQzygH-pQAshd3GhNpCezY6_QRrFVOR3igc-7ZJ1buMbjHIBur4EoIumrrcF7FycmTlzhroNLK6DwPqnwkVEnfCjUZuITrk12TPY384PzWYUBkm0cf1M97FvQ214mDmIMB8Xv59s3NVNiAVb62yXVcV2m7jsyPOdiZBAlA4xSuttSURySRJ8CftY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d112d822.mp4?token=qwkkvxyuOk3IWEvJsgEhJb7oy2gghowbXNMijVbGZvoen-HySxGq3NM-v4EwbWgBZPDMhYvnCLszWEHo_COl8t09JvNjydcefmbKYCCylG8KiVY7LNbXPSzoXqmcJ1ke3pIQm4S0KnhAHx0oZDrjQk1ShdFnoNfH39va-3JjLxGR9e4-jIbump8w-CR6IRcT94km4fvNcblIEhqlQrpPNElI6QG5CeitoF6lQT8--9USy2pxwrEACWhoQlLfsIwvOgANvc2pnbCl7VqBxvyE3Wn9u6FHgD7CBxeXfZk2BJSukcNo2mlBBF391wpJyAVn9xJxK4uLPd-4Ihi2AJ7celA9DmqwAbkqww5kIb95jnMG9Vscpchg74CzgKdRgPUdE9EYOI4O7rNTliid5qq17ThTPQpGtO8UnWrdZZs9a5hh54fUo5hQjBGkekv2sLPjGdD2JYFI9DSrB6RK4yOMR_kb0Yb1KFzRY9At0YLlzh_Auh8CbzYKQzygH-pQAshd3GhNpCezY6_QRrFVOR3igc-7ZJ1buMbjHIBur4EoIumrrcF7FycmTlzhroNLK6DwPqnwkVEnfCjUZuITrk12TPY384PzWYUBkm0cf1M97FvQ214mDmIMB8Xv59s3NVNiAVb62yXVcV2m7jsyPOdiZBAlA4xSuttSURySRJ8CftY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری بی‌نظیر از مهمان نوازی مردم عراق از پیکر رهبر آزادی‌خواهان جهان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/668743" target="_blank">📅 01:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668742">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
حمله آمریکا به برج مراقبت کنترل ترافیک دریایی منطقه آزاد چابهار
مدیرعامل سازمان منطقه آزاد چابهار:
🔹
در جریان حمله ساعتی پیش آمریکا به چابهار، برج مراقبت کنترل ترافیک دریایی منطقه آزاد چابهار هدف قرار گرفت و آسیب دید. در این حملات یکی از انبارهای منطقه آزاد چابهار نیز هدف قرار گرفته است. در حال حاضر خدمات‌رسانی و اجرای عملیات تخلیه خودروهای موجود در انبارها تداوم دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/668742" target="_blank">📅 01:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668741">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
صدای چند انفجار در ایرانشهر شنیده شد
🔹
دقایقی قبل، صدای چند انفجار در شمال شرق شهر ایرانشهر شنیده شد. هنوز ماهیت این صداها مشخص نیست./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/668741" target="_blank">📅 01:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668740">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
یک مقام آمریکایی به سی‌ان‌ان گفته است که آتش‌بس با ایران «دست‌کم به‌طور موقت متوقف شده» است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/668740" target="_blank">📅 01:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668737">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDWj6FpsiyNdOUi6Y_ultSwudZzBlSpmQqLxbmXFXUE-RGK56NBhc2Qzh-T-o9YCK-jllVviKxdL0PGzT2E73_3nlyBJIeLpM9B518Q9xuFOJU0OUgBsBd8nboY61LiYxEaa89a0MZiZ2mqCeOEV9u9F9Rg_nZ8GZ5v7bFTKZWZ_J8xbktVP32cHxg2Ymfzozg6QYpCx2KiqY2B32kiGRURoZ2l1ZC-DT63gKpuRaW_0fcEDTqNA6bbEy-OggwWwc2-Hmv0ZjxPKq2bs_14pzZkI7BmQ28yb09WefNYd-dv2d2MyNtt4tDkeYzNawP0Pk3Rir6ioMZw7kwdlxwo6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQNIK4WFB7uQMnZ0uEYbqImpFOS--X1vA22HJ4by0G2TpUHYKxO2wgT677t7n7jiItLOz_hdcTxqPGD3CYK14p3orqpN20NU560WleKZGGaoRfCHIsYEcYjPLzGn-UgHnYVKjGdnKjp5F18U1YRuwvXyIlxiDlBNDoqs3qkrfxlF9PYvXDnQ-7x-YGqZNdTV5AlubcWa-npyDbixmB0vZBvhAaSrzFn26OkbapLEMftquOuyU6hyNiQS9bqMxY2rsPKOhXTxjOeqsvFV4hbCewz_kz0pRW6oLWGLvchkBSaSE7n4chQWFle5nhDqcai5LIP7A9uzmL3J38icFcbbJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDbqa06x_0-RBuYmJ84JIha0sVKOvg3-8sDilkZdnCtEAxxMFisCJxEVxDXAgr-qwPxo47J34DbrdhJp4g2Xr7R_ml8um2xKzv6YpckoqyIrSJGjL43cR1n4sGtiAYG5o5oJ4xjf1Fa-8awqilwpXQ0udtbHlka_lYSMjVwIY7AXwWvgpN3WSHuXpvuLE104WUPa5n9m0NOpLHtAJ42IcFgB0nKwimIqizzGn5XWLaWhxjCpZ-eITso2_WnLkEnvWW9kTJMsP7pNMg0zY2J7t8wUpAJt0FOtaA20iP7zAq-LvPNRJS6j70e6lZobRDl0OsWYwubZKa52xsOBvZtk-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از پیکر رهبر آزادی‌خواهان جهان در شارع العباس کربلا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/668737" target="_blank">📅 01:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668736">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
شبکه العربیه، در گزارشی ادعا کرد بحرین امشب در حملات به ایران شرکت داشته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/668736" target="_blank">📅 01:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668735">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxVWVJR3BfvU4EgWTuk-EL-chgn6_lDgDzqjH2LLFVZDEoXrfYE24juUu0Uw6dIgjl3igpMuHxnz1Q1LtyDb5WGCGNAzQKqWj9ZX9hwRTW4SGhZaMeduIPVZHNX9c0ey0tyPIAmZetnBv99mNPzfeDs0L27dsANww6-AqxfRnKu7eVTfHTdWJhE2EPw8Iac5bjFk0kluyAAiz1XoNxmCGvM5TMP868b8yKmDUcKx2_Fc3MUFE1u0G25sd4pMHyTs9sOzbzMjr_lVDyM2UD1E-S1S1S1C1TNkORmnjFx1yxEw-mf40aR69BGiM_53fEABG2dDDzrKm_TLA1YUrSPdPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید خوک هار: این به تلافی بمباران دیروز کشتی‌ها توسط ایران است. اگر دوباره اتفاق بیفتد، حملات خیلی بدتر خواهد شد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/668735" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668734">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای العربیه به نقل از یک مقام آمریکایی: ممکن است به سمت حملات تهاجمی علیه ایران حرکت کنیم
🔹
نیروی دریایی ما در حملات امشب علیه ایران مشارکت داشته است. ممکن است در زمان دیگری حملات بیشتری علیه ایران انجام دهیم./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/668734" target="_blank">📅 01:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668733">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ایرنا: بنا بر شواهد میدانی هیچ اصابتی در زاهدان وجود نداشته و اخبار منتشره در فضای مجازی کذب می‌باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/668733" target="_blank">📅 01:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668732">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/afdd27149d.mp4?token=mIDHXbgVEzJXgWWGYuEOEQuq9alBajg2BjsT_4Z8aSLRMXKDL5HJ6iByupsKBgaJ3050Y_yNaKhXpf5054ATuO49Imdhjstpr8GwDmB7YccSFUfMdMSjTTmQnnyQVHGZupBVIX62mBMJlhNCLqt3Gyl1YBGlnmfxqvMJuRcWG7nmkuN-Z6Nf9EECbCYIxBeV7RDSbJ4dn0NU2je6WRvIZOyfPNnAiSxbG9yKMhEMq6RKyHIPjuwiRqx-UVDGK9VMoj3LToeGLWHDyYPipci0fAzHynSpp-ym4at4JkqRFNGhuZRqbZ-kytbGO87EZ3PGoXwkW_qqR_w0EZShLXCbbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/afdd27149d.mp4?token=mIDHXbgVEzJXgWWGYuEOEQuq9alBajg2BjsT_4Z8aSLRMXKDL5HJ6iByupsKBgaJ3050Y_yNaKhXpf5054ATuO49Imdhjstpr8GwDmB7YccSFUfMdMSjTTmQnnyQVHGZupBVIX62mBMJlhNCLqt3Gyl1YBGlnmfxqvMJuRcWG7nmkuN-Z6Nf9EECbCYIxBeV7RDSbJ4dn0NU2je6WRvIZOyfPNnAiSxbG9yKMhEMq6RKyHIPjuwiRqx-UVDGK9VMoj3LToeGLWHDyYPipci0fAzHynSpp-ym4at4JkqRFNGhuZRqbZ-kytbGO87EZ3PGoXwkW_qqR_w0EZShLXCbbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«شارع العباس» غرق در استقبال از پیکر امام شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/668732" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668731">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
شبکه سی‌ان‌ان در گزارشی درباره نیروی دریایی آمریکا نوشت: ما حداقل ۱۹ کشتی جنگی در نزدیکی ایران داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/668731" target="_blank">📅 01:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668727">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
مهر: اصابت ۴ پرتابه به بوموسی و سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/668727" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668726">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlNDKIx2Lzv_XHIv--S9ysuFqTKKQB2ivjgFYDLDJMyAjPv8w0V0nkqF8XpPzy9LB9Cyk5ta6uWFuBT3rkSmKxPPZA95SzAAuiMi_0I_0dTerPnK7yTl8FrcwaRMH-u5xtKFBE6UthdJOcGRENqy3GyywyF9KBHhaPb2e2KjEu-FCTejKAqPoFwyfsVtBaBQiAqNiHFDgLI4oQVLD9Wc3SZ-tCDXy2y5l_hrt2zS9Zavl2FPUszol_vUeMrrcSQMqHchrUpTboT9pwDJ07X956P7b0YVGydYGYkWIiEd_YVdDAXn_RN5JYf2yiaUH8HlORXJSKA2uOwB3V3GjS64KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماره مزايده در سامانه ستاد:5005095004000006
موضوع مزايده: بهره برداري از پنج دستگاه كيوسك هوشمند شهري در سطح شهر مشهد مقدس مطابق نشاني هاي مندرج در اسناد مزايده به اشخاص حقيقي و حقوقي واجد شرايط به صورت اجاره .
مدت و مبلغ بهره برداري: به شرح اسناد مزايده
جهت اطلاعات تكميلي به سامانه تداركات الكترونيكي دولت ( ستاد ) به نشاني
www.setadiran.ir
و همچنين جهت اطلاع در روزنامه رسمي به نشاني
www.rrk.ir
مراجعه نمائيد.
#مزایده
#مزایده_عمومی
#کیوسک_شهری_هوشمند
#سامانه_ستاد
#سرمایه_گذاری_مشهد
#شهرداری_مشهد
#سازمان_ساماندهی_مشاغل_شهری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/668726" target="_blank">📅 00:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668725">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9793440cc1.mp4?token=aBTSi5MgFHUbL0oC-lM6FeLTWDlQuff6DDulsQHue3NNiFDIZvODxCjAEWVrS5vAXcAWk9gm5ITbWkVBb03CsNv4090JsK3k3THdmmU-aBmLdpvP8g8tlJn1R4JYZzoo8ZjzEi9rqudfinnTFnIhz416nK--NM9k_N02FrIOoj6LKwUUeJRYqsyY3wQLwLy_H7VDiwQy7faodRla85G34sF1wF9_voNqnIFm6MIM0SCzyG0I__hyvaxDGLJjJ1f-zkH1hNEc_fyD3lfHDbOmbF4-5qbCnmkKwTotp-bNBzRspIR_7hHi08EnP6c7R6pqF61Wr1qxegoQaa1fqGzaPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9793440cc1.mp4?token=aBTSi5MgFHUbL0oC-lM6FeLTWDlQuff6DDulsQHue3NNiFDIZvODxCjAEWVrS5vAXcAWk9gm5ITbWkVBb03CsNv4090JsK3k3THdmmU-aBmLdpvP8g8tlJn1R4JYZzoo8ZjzEi9rqudfinnTFnIhz416nK--NM9k_N02FrIOoj6LKwUUeJRYqsyY3wQLwLy_H7VDiwQy7faodRla85G34sF1wF9_voNqnIFm6MIM0SCzyG0I__hyvaxDGLJjJ1f-zkH1hNEc_fyD3lfHDbOmbF4-5qbCnmkKwTotp-bNBzRspIR_7hHi08EnP6c7R6pqF61Wr1qxegoQaa1fqGzaPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل جمعیت عراقی‌ها در تشییع رهبر شهید انقلاب در شهر کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/668725" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668724">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuAxPJlWSWderWx1r9ECFFPoIjXVq7uH685R7lRTsp13juiSYCJz_Bxr24197fY8rVIN-A8fagAes4TXrInFo_ZvvN2qC0ixea0V2yq_zhI868gtK7Ar8xpO5SuPsv4B856bjmWfkMsMJlPUHu17QFqfLLO9NjsXX2XOBpru7aFDAolrAvxlHJ9nW5O2TL50-Qs_3QYyMwivteUGIqoU539rUKLYjIG-189bzS7XPLATTgPDG1cQ1ssddn5OyqwYReLJeQTGc_Uo0fjXOZZUAv2z1IFKQJ-usGfxvDbrkn9S5ZHxazbTXnxTO5AyafMgynK_T5SvnY8n0OYcCwNI7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: دشمن به شدت تنبیه خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/668724" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668723">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
اصابت ۲ پرتابه به پایگاهی نظامی در جنوب شهر بوشهر
معاون سیاسی و امنیتی استاندار بوشهر:
🔹
دقایقی پیش پایگاهی نظامی در جنوب شهر بوشهر مورد اصابت ۲ پرتابه دشمن آمریکایی قرار گرفت. تاکنون گزارشی از تلفات انسانی ناشی از اصابت این ۲ پرتابه دریافت نشده است‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/668723" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668722">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
مهر: اصابت ۴ پرتابه به بوموسی و سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/668722" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668721">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
مهر: یک پهپاد متخاصم دشمن در جنوب کشور توسط سامانه پدافندی کشور رهگیری و منهدم شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/668721" target="_blank">📅 00:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668720">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند
🔹
هنوز محل دقیق این انفجارها مشخص نیست.
🔹
چغادک در حملات روز گذشته ارتش تروریست رژیم آمریکا نیز هدف قرار گرفته بود./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/668720" target="_blank">📅 00:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668719">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
منبع آگاه نظامی: لحظاتی قبل؛ اصابت دو پرتابه دشمن آمریکایی-صهیونی در شهر بوشهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/668719" target="_blank">📅 00:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668718">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e90accfc73.mp4?token=N68nQnK2bRKygF5RV1-SptWRM0qikagqhKJVeHJCIoTt6QdeeHkLowXY5eTqV2yy_fjVM8DQI5qGZU6KZJKIukAsommMQSE8QWyN8gj2r5Ik1PjCLjZigysa9AbGSxFR6wQfUBFBibzStsVlQmb0xje0eBiu5YvnRW-H3QoXorY1QbkCowzdPEuNz2cmMCXhgZn5Mg7VX-mpNUJQzxm-ld8ksmH-FasuFO8tiZclXOQPxPrdq7ZgFzRuXcH7gMY93MdbBpxxs_Cq7NsFfQUWu1YlP66R3T1_NEpZ7-oREBpB6ZP9C3-3ngf7RydJ5Ln9_9nlYIkkErErT2A2N9lWWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e90accfc73.mp4?token=N68nQnK2bRKygF5RV1-SptWRM0qikagqhKJVeHJCIoTt6QdeeHkLowXY5eTqV2yy_fjVM8DQI5qGZU6KZJKIukAsommMQSE8QWyN8gj2r5Ik1PjCLjZigysa9AbGSxFR6wQfUBFBibzStsVlQmb0xje0eBiu5YvnRW-H3QoXorY1QbkCowzdPEuNz2cmMCXhgZn5Mg7VX-mpNUJQzxm-ld8ksmH-FasuFO8tiZclXOQPxPrdq7ZgFzRuXcH7gMY93MdbBpxxs_Cq7NsFfQUWu1YlP66R3T1_NEpZ7-oREBpB6ZP9C3-3ngf7RydJ5Ln9_9nlYIkkErErT2A2N9lWWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر رهبر شهید انقلاب، با استقبال مردم عراق وارد شارع‌العباس(ع) شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/668718" target="_blank">📅 00:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668717">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXzHz2Wlme8KohniVOHQDhXLlTaIU4RzgbHz46DFSfL2faSuaOfC66KxSis8Evdg8XczfJkveObL2Ejzuk4qAHxGuFHu0Eqe_3Dkq6LS6V-VKlU8EgmF9YODreTXjIFvjLsgKLaUG9Sl4C9zv0q4aYPvm77PCwlcBfF2THTo2M0BtJN5a4N9wcjx33AdBgTM7YGx1AzomJ1SkcmpQWCkAObR--G6XNFWPkj3VEu2PyOJkh94tOMkUqWayAqt-dULrQZhX7cpO-ZEexuQgOGXNABHFQtW0i2E8bHkBOZL2vwcTTqzHuTT7HJDiP6lpqHJ-SOUIprhjRkFktL7KWjbHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شنبه حداکثر دمای تهران و کرج به ۴۲ درجه میرسد، بالاترین دمای امسال تا الان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/668717" target="_blank">📅 00:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668716">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
یک مقام آمریکایی به رسانه‌های آمریکا ادعا کرده است که حملات جاری ایالات متحده علیه ایران، احتمالاً از حملاتی که روز سه‌شنبه انجام شد، گسترده‌تر خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/668716" target="_blank">📅 00:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668715">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
تجاوز مجدد جنگنده‌های ارتش تروریستی آمریکا به مناطقی در بوشهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/668715" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668714">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
تکذیب شایعه حمله به جزیره لاوان/ تأسیسات نفتی در وضعیت عادی هستند
/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/668714" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
