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
<img src="https://cdn4.telesco.pe/file/uQhk-sN4BYEX2u-XZQCdiJTOwlohhS5TRWvkaDwWKKRR49SEu-Gj0BKi_kM2efxvizIdexUN2xtbsgIJAjSbZ3eBq8TtPqNizxI10tTxJhHB8ihTP1QcJWQ_4WuzQ4LCSGS8CB1SC9ZI993XWs-7i5SYI0GeyfZMV6Ac380EhaEeJdWbgtr1WZYKOuzyUwkafw6z_Bi1hILqGJZRfZKvI1FmG6T62hfdF_YrWaRLlD5QigJg57owXM6Ta1ZvCpmry3O4c1IWMwxO0XmcOvZMy9pWwjGaMeE5_q1_ojZZ2mFS-if6vlpg7DazDDyTWhHujA3NNCPAVx0mpxEUM1EyOQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 356K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 18:41:02</div>
<hr>

<div class="tg-post" id="msg-24686">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=S9fhAAM-J75y0qxEQKf1CYkpYA54zSx7Gi76-KpF1TGX7HKkRrXD0VqiX6QMMrGbpcP0_Lq0CU4Cg0dwyWRRz4cq2jl6Od7ZDx7yjHVdWlryNFvaCCLxoVCENzJ97R5rsyzoMJNTyecBrso4ifGi8DyHzHMrxncKfjKs9P2QCyQYWrNcKJY7EfLQPPyANTN8CjZgSa_CLMF6sjVlybIEEk741w5BoHgMZOfqjhZoREhFlv7CdxLS7p0BLLb_tDHnJJZvYN2OvpmXTqov8Ik4WEK_PuyAWBOvI6OwsKAQG2rP6WhsqqETOiGn31Srpw3aEY8_UvrFl0JYxI6j4m9d1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=S9fhAAM-J75y0qxEQKf1CYkpYA54zSx7Gi76-KpF1TGX7HKkRrXD0VqiX6QMMrGbpcP0_Lq0CU4Cg0dwyWRRz4cq2jl6Od7ZDx7yjHVdWlryNFvaCCLxoVCENzJ97R5rsyzoMJNTyecBrso4ifGi8DyHzHMrxncKfjKs9P2QCyQYWrNcKJY7EfLQPPyANTN8CjZgSa_CLMF6sjVlybIEEk741w5BoHgMZOfqjhZoREhFlv7CdxLS7p0BLLb_tDHnJJZvYN2OvpmXTqov8Ik4WEK_PuyAWBOvI6OwsKAQG2rP6WhsqqETOiGn31Srpw3aEY8_UvrFl0JYxI6j4m9d1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سبک خاص و جذاب پنالتی گرفتن یاسین بونو که قبلا هم دیده بودیمش؛ پنالتی امروز صبح هلند رو به صورت عادی شیرجه میبست عمرا میگرفتش ولی اینطوری راحت سیوش کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/persiana_Soccer/24686" target="_blank">📅 18:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24685">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=DayV63JvBtYo7iVk59NReyoqS1R3eIxpI5fv8GAm-IB87_POCHLmw5UDQqbO_ECzOEyV_Q8GBmOGMOXiTK7BdZE8tHPteeLq9A3A-Geq5rdECJXx1I1i4DVDrwERCIKKkWsgADyvYeKNyBo_81haL8cxkxvnylYj-M071bZSS9AjylqzUtbk-QIswIxDZZzUNj91nlXVdSDrswfGMhOuyWmlksUW1_bseAW4tywYKvBfOw4I30uEKBVqzwycInNSzS01BO5hiutPgKWv4SGO2pYbrSVeEoNPBNRQbB0aGoEXRbWv_11AgsQgj255iLMW9UgUbuSkKe2mI_r5K19VWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=DayV63JvBtYo7iVk59NReyoqS1R3eIxpI5fv8GAm-IB87_POCHLmw5UDQqbO_ECzOEyV_Q8GBmOGMOXiTK7BdZE8tHPteeLq9A3A-Geq5rdECJXx1I1i4DVDrwERCIKKkWsgADyvYeKNyBo_81haL8cxkxvnylYj-M071bZSS9AjylqzUtbk-QIswIxDZZzUNj91nlXVdSDrswfGMhOuyWmlksUW1_bseAW4tywYKvBfOw4I30uEKBVqzwycInNSzS01BO5hiutPgKWv4SGO2pYbrSVeEoNPBNRQbB0aGoEXRbWv_11AgsQgj255iLMW9UgUbuSkKe2mI_r5K19VWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
تیم‌ملی‌آلمان همینجا حذف شد، نه مقابل تیم ملی پاراگوئه؛ اصلا بعداین‌دیگه نتونستن درست بازی کنند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/24685" target="_blank">📅 18:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24684">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLJgzDWZcG9AxvwON9lYhceyYnLF4GH8BZcYKnzbPYSbC5bVAr_MLEhNQqtRrpi4RcioAANtBgldc4svRg4U2bl97siRHtheVrIPzke7RvdbGvLhH6rCu7XYZt7-Lk8Pf08ZKG7iAILCiD5oq8GM3TEThaR4p5y3f3_5RuLWosk1jxNDX9NoDor5mtgmmY3U8DvxD8_il47lgLiYUiAWOX_tS8OHD2hCAQ7MmODCsIkwqRTwBQLtNrZcYW_C-ihTu81fm0c3rLw7VX7gLaK4v0-J5CpNf7hTIZf8vvqDXL1fC6aM9ALqs0RRSs8nBjiwwxGSIsRBC4P4HMbWQXpJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
جادوگر تیم ملی غنا: در طالع و سرنوشت کریستیانو رونالدو نوشته‌شده‌که امسال قهرمان جام جهانی 2026 خواهد شد. سخت و دراماتیک است اماپرتعال بشکل باور نکردنی قهرمان خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/24684" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24683">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaCUPqxv32UYRku8h8qkKVQdWEAK8MtSQSZgjbsopbpTzAaponwwGxuokY5DqVCsnJQVLZpjT0jAZuANXM_nQvuBLPdjc7-IKXmp0NpnkvNi2LnmPGR0GEEWdHc8vzQD4EQvMk2wKbgGN7NuoZL8yoL3eF-pMlhW_JEbCnMJZ_X1kGBsVCH9eTc_BRTq-8WnpedUqejDJYhIUmIc5Mu5k6FVpRir2hOrsxT8-3ZHYfKNym5yEY4d8EelsQGlhyiAt9P4KD6YmAPR942htpcoW3bExbmJvk0y9iQirN9flb6Q1XaGHTqgF3W-Y-iwIG7h7T0cfinnefaydKflRMfCvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: باتوجه به علاقه اینترمیلان به نیکو پاز؛ فلورنتینو پرز میخواد او رو با الساندرو باستونی مدافع 27 ساله این باشگاه معاوضه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/24683" target="_blank">📅 17:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24682">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsIXrE17XfkzWW8239RTeGd8uXxt-lz3UBWK42K4uF5GFgeowu3kJOdxtINLIWjFMQ2QxqPgQ71YgAWsnBXCBrO7yxOuK5_inqNfR9S9plfXdlP2tvA6WNcjVozwORoh3FvFBBEwaqbLEYDPL0YavgEOxWLF0yo3QEngIx8j0uZccz0qnqgJtKkGDi9syWYabscwXqfD8LcXHzgCQSznHL3bjZSPoP_EJvK-7WXMlwOdC2Cbw1EVUIl5heJYF80cq5qV0DAN9hndZO2K46pazLC7pXGZlELbyzOBlzNUJxmI9f-sOtGwkIAV-GNtj9_JVBkRgdDWukeenfCaJEaQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/24682" target="_blank">📅 17:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24681">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=QC0CcCVNr8lkSet0WcVm-rubgZTv-st0xs56uYPnF_IHywM2eFjsGS_hZqZsPORGr4Qi3djSndpFm1ux2Wc1SFE6Mipj8hACInQ3fjTQJGp63GFv5pvY1sSUFhdcWc2O7WBdBaSZlsXn1lfhZk4lv7ZXXL_Af1xoWdYrSMmF_npjpWTJZvCg8LM9fPbivwqPJQzrzKquwQP67DqJCRcKtM1E7W_GqBdu4ux5XrnVcczQsOa9Pjys3GAXXhW-PdCJNPL_mqQkTSiBWqPhDV-sYabjDGDtdAvaV4DLpaz13M0cqQ8BzAuOi7W_6nOd-IX9GlDtVQpiowQc4Yrswikgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=QC0CcCVNr8lkSet0WcVm-rubgZTv-st0xs56uYPnF_IHywM2eFjsGS_hZqZsPORGr4Qi3djSndpFm1ux2Wc1SFE6Mipj8hACInQ3fjTQJGp63GFv5pvY1sSUFhdcWc2O7WBdBaSZlsXn1lfhZk4lv7ZXXL_Af1xoWdYrSMmF_npjpWTJZvCg8LM9fPbivwqPJQzrzKquwQP67DqJCRcKtM1E7W_GqBdu4ux5XrnVcczQsOa9Pjys3GAXXhW-PdCJNPL_mqQkTSiBWqPhDV-sYabjDGDtdAvaV4DLpaz13M0cqQ8BzAuOi7W_6nOd-IX9GlDtVQpiowQc4Yrswikgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
#تکمیلی؛ بعد از حذف آلمان از جام جهانی؛ مانوئل نویر گلر 40 ساله ژرمن‌ها رسما اعلام کرد که از بازی های ملی خداحافظی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/24681" target="_blank">📅 17:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24680">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESibDmisJKlZ2zyEycqGMW2K333jb-N7lpBKQhkLy5trmW6yFGSF32GgvOjVDYvVJeNwnhzs_Tg3ILjg3fmdlQDAawTZ51pzeSao1mg3oZLGK7_Eui5uZA4xmCmFSBqXp-pa2DYZY_y5SXH-X4Zs3SqxPbAbS_CeN9CkcFkwG4hRbadD2-XIPxeOhbqId05TcolPrWXD6Yi4QeJ9GC3toobkkmIQF6g3n01L3S9N_662qBqLPfhSZwLlxNAB2J_oOrblY9kxZJMcsPLWszT_TuhC30BZfhSSzOk3M3vU9ATgIoybrGzmjXylZyYj5fLgzv3MJV65xOhpxedoHRO-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مسیر به‌ظاهرآسون تیم‌ملی آرژانتین و لیونل مسی برای رسیدن به فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/24680" target="_blank">📅 17:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24679">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9VqGRQQwqWCw7DRSm5IRDFfkVW_AChBdyXlUaxdoVe3uUicRVMB09csv2FibYrSmeQpu63gol2w4fU0bVSY2Yzwbii54G_IibMx6VCsZdEQ6-TDHL8LQ6P7NvLDWsNOG53PzBaGnK-qlJOsmVIITlo4p9gUjDiO0QJDjm9YAD0nfaTX-57-fnNunrK9zuw8SAeNHb8XUEEr35R7xDXt1Rs9AgB5ezni1k-NuCTnlymdvB7f1qGPq00lW4Xr9iK_aWfTzlx4bh9zCksjT7A-HcfeYXeczT7hP2ZEMYn_OE1rd9aqxcR6CcTY_rWyvxlovltOJsDVz1u0eOTEN0-iaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/24679" target="_blank">📅 16:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24678">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5a1o-ts5-egllzUBeHk_zg0YUrqQ_f51B-vXYjBNF-WZJwREc7u112BhGxTxqvFmwosPrYZe4o_a-APzoVlSWDolwBhviZsmVCp6XoAsP5YkNGpfaZe_S8ob0Gf_C2L9Fuuh1W3vb9tmdzi22DmWioitKt6p_yV4B-cO1KFn1V0HeUuLNRyTNUJYjyY6izFoYVdZMyshzeAsQX6PLRbv1q5st9pE8pULl-Mv3yTas5-FOyMLVZvSJNfQf3BcNaPvRUVrxQYK0vZGSpwGAWpEoejubFCNsOW5QmyFB76msG2eWPsBISiaXUzb1B532VO2ytf2xT1ZhWPSuDClWYIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/24678" target="_blank">📅 16:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24677">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmayYgkO170ckdvm_x-3h8bxi9DgB30vAeRIVswYJftkvIJhQPQx9LQwIlNnB9wA7vww5TI80KHHMwoqhGWD8zwKgXw70BaN-g60z9c9sWJEjIggq-KmPUzY90U-h-IAgIaS6NS_9YgGhzhOggDj-bS1BQTAHEXiFRfrTBziTipv0eq1dWuo3_hjUyoB0utt9BQuJ8N93_FKT0YWz7k54RV4OZWWEEI1eNErHzrdGA3vYVLaTlzO4v__NxXKm6v-uXLmTyxr9W9GeOfJcKNmUHY5L9YulHlEtoTTtngPQkDx0bND-CGmnoD9e7F6cN_M7v9NGL_REUBVBtNfY1ai3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
شش بازی بین آمریکای جنوبی و اروپا در جام جهانی 2026: 5 برد یا صعود تیمهای آمریکای جنوبی. 1برد تیمهای اروپایی. فوتبال اروپا این دوره بد ریده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/24677" target="_blank">📅 15:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24676">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUDTzOf3jhg5g3q8R3rxF-ssYHIx9VOswn3pIVdAIuxz2jxqBOi3LDIVulByD7ocmayMR_91oXhLwPp6XEzQiFEiuepZMnFkRu3cO164q7CP1PHxL9i6S3xWmGEjURVXXpWS6V5TOg_4Du85qkdP5-27OJjHl3MvdXs_i-ve11ZWeKg4m8-SVmNENFHBC93jHxmLzXSHys__Fj1jqnbOUbt1CpWURItMWKJRlCHn7kgJwlk58AUJkuZCV9lIi1E-Z6N8w9eph3bCouFedim-rJmEEI6OdF3v7oyY8XtiW8bWQX_L6zQXKyPXnKqhMWhxE4AAq5OM6jpc5LIhUVxwtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/24676" target="_blank">📅 15:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24675">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxWW7h8eV4XQlQ-eixZhR3PMUr_D7KXswAcNTpZ0jp6XXHgWPI6eFgPIIjahPnGE8RzrqlFn65B9GFaEdQT5jxPo5ImkY3bPUsmBvuG7yTyCcz7mTAL9UmbumIezRsjnaTvY1yFazRRznZY5lCz_RzxM12AaC352Y-dA1hvsUeglPn8u99crJ1Bnw8cD-lOwQ0lkI_kjAc--klLfheVDLErisGw-2uuCkCmftwg6IGNWWPMtaDuW1HHrbf-uqo7QAwsVEit_SaHZz4tjbvyocYxxW5Rlm2EV3c0c8A6LH3clJ2z0QT1lICSjKuj_fCc2GEMmt8F-NLPXXNAAOiNEow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/24675" target="_blank">📅 14:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24674">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpbf0olxWIMaw7ui_PDKuMvAkw1D27ez2innIK6SmjaV55_Kd0xBBgLrZBfPnQVNLzkU3JN6v2mJb2SjAhWv7BenPGeoZQDlPj0w0qfplR342tcDj1x2H2aDH1Cb4EPcyZKZMxWBa4kOD6nPSXMKU7dYL_AI8wB6rqqZwifaUp9pl3ow49Dffna4AGKwJYaUreB16AdDlNXGb2Wq7FR-iXGpRxULd0Z1WqywqMwNVaeq1e5h--TtYiD2YSEQvd3yjFAihhUClvAF6qupbrtK4NUDpPbQwWTy-y_11nDZzR4qYxCey0U18HXHQx8TAzKOdWeqDFlUfcOS9uK2PKjmhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/24674" target="_blank">📅 14:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24673">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuNRysP2pXbhx6dBhmffs9qYEuRh-HNanUZZ6G_ol8Us_W4L2YlFUo1Ii3V41w2dDoA5CuOG7UPBAeSEo0X_QworDVFcD41aCaWOwRJK7GyKYTBDx5xpMveBlbl0KVtp2tSHxvO6KyfFm2fhv9ca6z1zOKGmDuWyo_NEKQJP8hKguMvvBLstuDNsfLbMUDLNBENT8d5XySyHX2_oGOz2lldSuOhRoUpxe_eQa5ZJSaycP7MoMiAyASA7lmEqvccpy56F_sId-sA_09obaOpvdBKT0LMyxaCTLWTSXvQLIx7OcG1Q6baZrjADF4xlxp2eYxngwHGG5W3qKo0GL-aqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌استقلال باید مبلغ 150 هزار دلار نیز به حساب جوئل کوجو بابت فسخ قراردادش واریز کنه تا پرونده این بازیکن به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/24673" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24672">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82624c7740.mp4?token=oG_dbmZ5BCtpFRP9Zgd4BHDxNVxJU65qszGm_d2DUczZMb5hE4Pr1hcEu5W0dSiX_9pmJGIQs4_jnA6sMpiS_bJVxfeilEnkqk42EbE38NWzuSULIn_aDcGEx3Oet2-YR2dqTit3jWDmmvWg_oNMeCKU1MV1inVwlk8LMgmAPIZpe_ZhWOSGYm5U0ooXEbTkO0tzzcOcxxsoryQ6vDk6MiIm1-T9Row_8Q23yC5Hqa-nwnE8UzfI1Wy10r8J_Pf6vfsQx5KqsUiZhl2K68OvzAkEQyMu776fYm5f75oGcvk28EvoUas4-3SGmEbeC72Iik7B0c3oeqLsLlNXAIOnRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82624c7740.mp4?token=oG_dbmZ5BCtpFRP9Zgd4BHDxNVxJU65qszGm_d2DUczZMb5hE4Pr1hcEu5W0dSiX_9pmJGIQs4_jnA6sMpiS_bJVxfeilEnkqk42EbE38NWzuSULIn_aDcGEx3Oet2-YR2dqTit3jWDmmvWg_oNMeCKU1MV1inVwlk8LMgmAPIZpe_ZhWOSGYm5U0ooXEbTkO0tzzcOcxxsoryQ6vDk6MiIm1-T9Row_8Q23yC5Hqa-nwnE8UzfI1Wy10r8J_Pf6vfsQx5KqsUiZhl2K68OvzAkEQyMu776fYm5f75oGcvk28EvoUas4-3SGmEbeC72Iik7B0c3oeqLsLlNXAIOnRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
میثاقی ژاپنی که بعنوان بهترین تیم اسیا اونم نه مقابل هرتیمی مثل‌نیوزیلند و مصر، بلکه مقابل برزیل پرافتخار ترین تیم جام‌ جهانی حذف شد رو مسخره میکنه؛ جوری میگه منتظر 2050 باشین اینا میخوان قهرمان‌جهان‌بشن انگارخودمون‌خیلی‌وضعمون خوبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/24672" target="_blank">📅 13:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24671">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVwwkQAdIgZvGFTFueIHDL5OVof0RW8FqVwHTcNK28OKlENjfcSzGQckxGAGG_TXJ_tpGTq2dh8Vhj5UgOMByOURa1iOq0EWl2EpR3uBY7xloHe5cU4ikBZJJ-KtJ-pdLul9S5LaFltEcjFp1au3vrg8OGB1P-tqY_jER0ovGWhhQuIQntYyHs0kkEs4WefZjARveT0W28LHrqT9I8dEvUWy06QhpfDiq9T9fRHw8KJKnEj-oXjNuSqlohTDJAO2xoh-ERjA4xSIwcg3gaYwAUI6N2sIl2-Dc2_5M8YZPE-DcsQoCyqaO0KgymKDqMWrv4j7eGAstUqVu2iG2JmeZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛ گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24671" target="_blank">📅 13:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24670">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLctmbZcPXgOMPwZwCOu936wO_a1I-jLcq2_W6Oa8GMH9IiYEsP3nd2cJpAip9GWWAhLBP3DQENHVpH8-ANWBPzX4ayj8Gknc6yaYrqzrJHqo9sy_ZsoOinp-P1PI5atj6dj9gU1BljZtPIHpkxlSrGSBsKZdyxbcVp8MCWb4qXZQVKcxZKdGBZcXp50O0prTiz8HoYD7iLJ8ooAKl0UujUWHY2gj7-PUO3WWEelaiS-53sLI07yqR6U9_T2qY1CWsR8Ifs2CBpmbILf4nBKl8c5ow8haz3sfKpElbuD-spT9B3lAeRPaL1paf0GiI6cU-JVmzj9tg752gkiCuuTRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24670" target="_blank">📅 12:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24669">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e8477068.mp4?token=aWsOaYbZHnOfiEp5gQ5uhzEc7uGQ2Z7ai9XQfdw6-Ml_bSliaOWvSgMcyqc4pF6prkW14Blr0IdbpxaDWcRZBgqPxKcvV4GuP2Ltl2NOt-5SZ5CNKz1-srWtd3KM179k2YBs3LAkxR68j_8XUHAwKO6ETRhuhQUrxIEWHyH8w8LppiT32blFndxTRl5GbyYMs6A14_Z29h-DFf1Eer-9T3mevM4v-igsbfTjCthHusZ6M3e1Lm6EUcYkYyWHvS8fLuIAaCCkbWKOYhzMoZ47HM5A1HfR_6r3X59JzdkiunF3nLyW0aG-3tbvGWWAGmGBanPHM44z9C6Z_h38cJBykQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e8477068.mp4?token=aWsOaYbZHnOfiEp5gQ5uhzEc7uGQ2Z7ai9XQfdw6-Ml_bSliaOWvSgMcyqc4pF6prkW14Blr0IdbpxaDWcRZBgqPxKcvV4GuP2Ltl2NOt-5SZ5CNKz1-srWtd3KM179k2YBs3LAkxR68j_8XUHAwKO6ETRhuhQUrxIEWHyH8w8LppiT32blFndxTRl5GbyYMs6A14_Z29h-DFf1Eer-9T3mevM4v-igsbfTjCthHusZ6M3e1Lm6EUcYkYyWHvS8fLuIAaCCkbWKOYhzMoZ47HM5A1HfR_6r3X59JzdkiunF3nLyW0aG-3tbvGWWAGmGBanPHM44z9C6Z_h38cJBykQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
یان سومر دروازه‌بان37ساله سوئیسی‌ تیم اینتر میلان بعد از چند فصل حضور در این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24669" target="_blank">📅 12:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24668">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=TcQckrfInqfYtUnbegfOOD_3C227n5vbpVGvHtDdlU81yxzDTZTcoF95laMfw-iRFG9GSWkmVPziskbQcVfbA9NOpjDmEpcBl97uRUKeQ5YF8jAoCOGUEKVv7P_z6oSi6E5DuyYy0MGkpdg_RuHv-vyXD-jL89pqQ7EO3kRtZOPJCavbh6yqTOcRT3T9HmTHl0HftbSGI5Jy8QDo518yAFP7AwusJ27-YoA2iywMuRJTT-3fBXXhzm7ze1h6gwk68s3gVFJVvkC9LnWYI9Bia0KKsEtrmVeqPixHwtYxpK9STJNDxLiTJKc9E-c0Gh8CIeJkDDkgao1ZOvso7AuNKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=TcQckrfInqfYtUnbegfOOD_3C227n5vbpVGvHtDdlU81yxzDTZTcoF95laMfw-iRFG9GSWkmVPziskbQcVfbA9NOpjDmEpcBl97uRUKeQ5YF8jAoCOGUEKVv7P_z6oSi6E5DuyYy0MGkpdg_RuHv-vyXD-jL89pqQ7EO3kRtZOPJCavbh6yqTOcRT3T9HmTHl0HftbSGI5Jy8QDo518yAFP7AwusJ27-YoA2iywMuRJTT-3fBXXhzm7ze1h6gwk68s3gVFJVvkC9LnWYI9Bia0KKsEtrmVeqPixHwtYxpK9STJNDxLiTJKc9E-c0Gh8CIeJkDDkgao1ZOvso7AuNKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24668" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24667">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=ScSRxj_14JOIYweuppOrbj5bTxnIDKqXA4aKo2b3dvLPOWc_sTGdBppkbedEWXjVp3Bw6pNyuObsUqnz4Wn1y5ocQuTIQkXLFG2cLJ62Aw1gffRwhQ7ntvLypPOouWP_ic8rWyTDSltVFb1ag5iRoobGHcvylq57pmgaxTnhDdoaCWb502RUJRzjGBEvqUlyii6OxdV9Lgq3aMv-Wj7Ef6rEMsJ0YdmZU6Pq1J2GPikhKDRm9wOpcMm0Fm7sSguC61hGCvy7GhNs6TSL0kKmXgM60_KEu-Ybwa7ETVE5oKtdrU3A5_JsTpDF-wiUdgcvzUdjM7n9hUZ0r6MI89MMzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=ScSRxj_14JOIYweuppOrbj5bTxnIDKqXA4aKo2b3dvLPOWc_sTGdBppkbedEWXjVp3Bw6pNyuObsUqnz4Wn1y5ocQuTIQkXLFG2cLJ62Aw1gffRwhQ7ntvLypPOouWP_ic8rWyTDSltVFb1ag5iRoobGHcvylq57pmgaxTnhDdoaCWb502RUJRzjGBEvqUlyii6OxdV9Lgq3aMv-Wj7Ef6rEMsJ0YdmZU6Pq1J2GPikhKDRm9wOpcMm0Fm7sSguC61hGCvy7GhNs6TSL0kKmXgM60_KEu-Ybwa7ETVE5oKtdrU3A5_JsTpDF-wiUdgcvzUdjM7n9hUZ0r6MI89MMzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداگذاری‌باورنکردنی جوادخیابانی مجری ویژه برنامه جام جهانی روی آرناتوویچ و خداداد عزیزی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24667" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24666">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol8lWTqogkqLu0r2VanN-ORu4E_L_NMxlLFR_Tj9U5UeZqM89VoWi-K-eiuI8I_Fpvp_bQOIRX2TOzjmOGSpzDbjD_mVeFbHuIKaM8a4bXEuEtmM-O5JeGdwjtmXD3SE1Z_ioU4Fi3Cx08Wf5B0uxf9LpuclOBqKEAz7rVm_1FHK4c4Vgt3QB6TxMs23a2_VdAFGnw0XeFqnK7ovtdOdNwDGlffyK9ui-tZprkAYP-t1zqRMZRqOMdLlRi9xC_tmsbrI_7BNdhQP44MGLuj4NBycU-0vP1DynmmYXLaKBA5EvaQi9vwyOApbyGqsP64seDgi2XuXwi46S-z4hJupYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛
به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24666" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24665">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2r1B3qBMTFPK8dLqAs9j_Cv2BqT2tQFrIklw6YWI3qg5yUOudW83tykOCl0b9AMcUB-pxrHZUnN_I-TKh-zY4LhF0wAGY4qvgEsXieDkj4eVXNK7yoeeunJEW1LZJFOrsvTkH_yJd04UxiSZCPezRCACjzzewZJmyUkVgxkT3Kkys6W-u4sv_NV4VlCJu6Et9zqluFtQ4_bcWph02PUbI-UQ89V8BgL7r6BwB1xbXKBPyVpICugUpazUEcpeeEdZ25ndlu1AZjciygKKWoh7w773cLYuXaV1UR_pu-j7GNt8TPlw6LZ-Ng70xpPx_c9GjW5R2UJb90IgIJ1x8wYrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی 2026؛ صعود ارزشمند و شیرین کانادا به یک‌هشتم نهایی رقابت‌ها باپیروزی دیر هنگام و سخت مقابل آفریقای جنوبی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24665" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24664">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkNtH2MxzhjXL7ZeJy_1GRbA1R0vBb2kwWzzTUyiBDuMmMBgcKYsXhlzsbifbHTOj7c4pYN-K533MQQXkM05IxIrmlWRXGNAGghHGMzwF-BZJmf_7ufRgY2mv2IdskSuLH2e6a3-ADwlH90o5eWMG5ODl7Jci37qiojSPxAvLgrtRQFPjNfsfVlIMS2x8SUhgzenNezKUy8VkK9ihAmTdaS74HcWGQ2Q786GmdWtmX1Gf7efBxkB_dNyg0Amr6LbFNstZTP2OrNCgKHORxkZOl9HQPsWV2-bS_vfo6sB5yzdJPKOZq2-x-0dOzC8MNhY85h_25nBSIZrbQAHKsNzVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از هر واریز
🤩
🤩
درصد شارژ اضافه خالص هدیه بگیر بدون قیدو شرط!
😮
تنها سایتی که
به ازای هر 1,000,000 تومان واریزبهتون1,200,000تومان شارژ میده
اینجاس
👈
این یک هدیه کاملا نقدی است!
✔️
هرچی شارژ کنی
0️⃣
2️⃣
🔤
موجودی خالص میگیری
👇
🔴
اگر هم باخت بدی همون لحظه
🤩
🤩
درصد  مبلغ باخت به حسابت برمیگرده.
⌛
پشتیبانی 24 ساعته
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان r9
@betinjabet</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24664" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24663">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/airvqIQVxoBDLrSni_lVCpp6_19ZKs_p2ztXcLauzY0j3uSyABn49_-mGESU99RmpzQJP8iBDd87-Oho62NiKj7MfXjAm8VG6d8ancgH4cVY6AhkNgd7qp47vk5r5bn6USbTVHTaKoPHQzMkN4XHkGYqIVHfg14rFI2XEkeoFtvxzBhA2FtRwaMsk17CotnoPxnvHEYztx0dnTGFvQW80-p1B8Fy_SZ2-AL-77yciRryB1yi1GCouYH4alJHgqJFDp5UCf4HfcWRQ-zDDB2TYjwNq4oDvFbHs2o4G66Nhrf7AKbGuMxQj8xRNVFCB-iNGgGmaQri9fHs8bE6BGnfHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24663" target="_blank">📅 10:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24661">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572d6647db.mp4?token=mtNYIyZt4ZgeLcpXYsvJ0oFnLyRFbeuaYVy8wM-CWSMIxQSEf9feXOEBBFkhuEafEldZXJXcnxwyuoFMXyOCB4fKkr7swc0FgpYrWioi7Qg_h0yiEQDQispOmbIsow_oUPEErpwdGULaG5XP5pa2wdemIu_dQUq8lKNIoIGoIcyuOEhQMibDSMRLxsoND2yqWs8RwAaihFCXviPSeiFfKa0x5NdYf26xd_IGGJBE1jKPixFV_UD0ZtKvSz7UjZ855dQ6vUdLhmCZ0twIKClk96-UJM87u4SJ18ibH3wqf5vdLWb7iHUPLHJL2oy4jm7D9YgjjwsAB-aibPg9I5LGHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572d6647db.mp4?token=mtNYIyZt4ZgeLcpXYsvJ0oFnLyRFbeuaYVy8wM-CWSMIxQSEf9feXOEBBFkhuEafEldZXJXcnxwyuoFMXyOCB4fKkr7swc0FgpYrWioi7Qg_h0yiEQDQispOmbIsow_oUPEErpwdGULaG5XP5pa2wdemIu_dQUq8lKNIoIGoIcyuOEhQMibDSMRLxsoND2yqWs8RwAaihFCXviPSeiFfKa0x5NdYf26xd_IGGJBE1jKPixFV_UD0ZtKvSz7UjZ855dQ6vUdLhmCZ0twIKClk96-UJM87u4SJ18ibH3wqf5vdLWb7iHUPLHJL2oy4jm7D9YgjjwsAB-aibPg9I5LGHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
صحبت‌ها و عذرخواهی هاجیمه موریاسو پس از حذف ژاپن مقابل برزیل بدون بهونه اوردن و گیر دادن به زمین و زمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24661" target="_blank">📅 09:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24660">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gG2QVJddcLa1WnzzHtP8mWyl72oGn_iBmJ1G4B74zfmVSsx5xR77UKXmyFrPU7Xr_q65X9k4oqrtPgc3JRxpU5KYE1JDQ2GsBtORBSXTuTG4xN0X3NuwOG3edih7KPMc_9K00ENhbSu8Q9uzt60Yxjhmt9Ox5SA3MA2m5qHe6rFf0OvgkxoaUlXIx8VP0BJId2WUXnoeLEY-Rc0pFbWMhLVP1lCbQMTHJlMG7ztShXns_VHFCVBzZcI7hDIfz-O6_s5FeDTtdsEz_nWBU15Yt5PJlk_ooz6DWzewNaG5qtggKFHuxhoJ0XEBH2-UvZfyJbEllDJBJ7q1HTOUmtn91Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سه‌فینال‌آینده‌جام‌جهانی فوتبال در این ورزشگاه ها برگزار خواهد شد؛ کدام ورزشگاه باشکوه‌تره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24660" target="_blank">📅 09:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24659">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24659" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24658">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG047tohR6nVRh6ODsHaaDvDB1HWWjREdAEqMWZfE88mcbPt_3OmjvZtY0zzT_YkIF4-BRrvUrfldc3K9VBBPxdaAFhgu-UNP2RCikV-pgaQ6K5UmGC4aQhFgVRuAJtbzowFZ4Gv729-MKf_1dfLqXMtWb4ym_g89PTlbuB8AJK1KdH2xzeYwgt5W0L7H4_fEvwSg8vJToE5oLWKm3x-qa5ua2IgALi2UyrWgnix4f8zW4wwzdiAC4kvG6KACzjOnABAAlm12xLRUkCZasfL9mTbH-0nFdxrht4RuOMbNEaeTPhyTZQDc3GZJFaJSL4gsiif0T6-Z4-5NuiC8dEaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24658" target="_blank">📅 08:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24657">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IACMWnr7aqLYxQmiebKTQdtfoIAhRh_FiN4BJpWu4iX3TbtumPpiS-HekhYNt8aWcyjE9kAn00T1EAyZZMdYbT0LItWKqe5FdNbyF2QfJ703EZx2tzW4FIdfVze1FuHZwBqXCguKCIokySgWqvJy7bSRSTN2s88Iva6OEyyPOf608yFtLCQNwUmujuZrK6itgXylNaEZPhBANSG2Qv-dkk0SZSyB-xE5QOay3xOvWeILwGhySYglUCCfCEkzbKpfg4U_HvCciUcbbZM1l9jJ-u-bFD2xujrT4NDU5E_4lZmebwaKpBeSvoWw-nI6cVG5uHIqe3aqhZDbvaUgMdv-6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی بعد از صعود برزیل و پاراگوئه به مرحله یک هشتم نهایی جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24657" target="_blank">📅 08:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24656">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V80xyrLhHTqqg9Styz5ZBk-j0nMYVpzhm6qKqhGH64uXTkjpuVQaCnN6hgIREfu2EnyAUiTYpB-T2yLdlauY44VL_V6ZE6fpH4g0xFAdthkO9y8Uw7gRV8jE5wJji2jxP8npbHJode2vdeAFD9c7yyPvHUIcnbLiEnlmBYwV9c6W6n_JgXFezbjYchXXxNkHZEOxr1dSI_nIn6B0yFjbW5aGcNOgQ24QnxyWvD1R5sESLv1RCq_WyERz3D9QUaDFk8i06MSxS3KCN8Hx4dnG6KAsfzRp2pVypuP0wxJ0Y8kntzyVPbTa8ULr9XsIA6tMVrpLDXq2OM5F61zFLy_fPeJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V80xyrLhHTqqg9Styz5ZBk-j0nMYVpzhm6qKqhGH64uXTkjpuVQaCnN6hgIREfu2EnyAUiTYpB-T2yLdlauY44VL_V6ZE6fpH4g0xFAdthkO9y8Uw7gRV8jE5wJji2jxP8npbHJode2vdeAFD9c7yyPvHUIcnbLiEnlmBYwV9c6W6n_JgXFezbjYchXXxNkHZEOxr1dSI_nIn6B0yFjbW5aGcNOgQ24QnxyWvD1R5sESLv1RCq_WyERz3D9QUaDFk8i06MSxS3KCN8Hx4dnG6KAsfzRp2pVypuP0wxJ0Y8kntzyVPbTa8ULr9XsIA6tMVrpLDXq2OM5F61zFLy_fPeJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24656" target="_blank">📅 03:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24655">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=BAXOseDmauPVvxE5-swEcW88nNLKYkq7P1a2OwDkbtbfq1jutFL4hk0i_D9WLuKtoacikial5_WRb7OlkhAdagQqJasvgVp0X3V-tfAmeRfPkVLxWYXdRjIskz3BoooB6n2Ym1pl4msf03X2vB71qxtrCPsaLEEuUuqGa85bCbLgcAyVziDorU32OSyk-rO-OVWfs23z34IqpNr6-h-xDgSu7cSppBrh83ic9VQ9NPfTGWwz5gsZGwsgDAPPf4Tz6FcunTmEe_w1IBsDKqWZBF0AfRl8yjcbORMDb0ZMagSIthuG2JSek3RwrhvbGdncJYKqfYp5B9eK3nZJ6PKDJD1683mFkcjU4Gld7zZNRIXU2JSKv0uMnWKCps9R3g1PaBsACAB6vpZmHbkp-9iC7As90tpPR9vHfG4F9QiDFnW993QUoEMtTDJsjzrRPKZqA9twhR_X7PRDRhUSjmuAeznxjUHCJ_8oVoRk1s2Bu65x0B0oJRoJXv80ILgyYVmjLVA42MD602MmzeeIytNj5HAhErNRIfsePO0zUChGEDsm8WFoGzGSpxwIwwOvySBvA5yL7pdg1jb9AmM5xgdn55sKGjBD0JKyYcSpJjdU8vucBCYhA1ju5p_mGEBlc3ZAPkM7ekkyyoKaOSNhh01J1fHllxUuIFeAGsCohiWeb-8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=BAXOseDmauPVvxE5-swEcW88nNLKYkq7P1a2OwDkbtbfq1jutFL4hk0i_D9WLuKtoacikial5_WRb7OlkhAdagQqJasvgVp0X3V-tfAmeRfPkVLxWYXdRjIskz3BoooB6n2Ym1pl4msf03X2vB71qxtrCPsaLEEuUuqGa85bCbLgcAyVziDorU32OSyk-rO-OVWfs23z34IqpNr6-h-xDgSu7cSppBrh83ic9VQ9NPfTGWwz5gsZGwsgDAPPf4Tz6FcunTmEe_w1IBsDKqWZBF0AfRl8yjcbORMDb0ZMagSIthuG2JSek3RwrhvbGdncJYKqfYp5B9eK3nZJ6PKDJD1683mFkcjU4Gld7zZNRIXU2JSKv0uMnWKCps9R3g1PaBsACAB6vpZmHbkp-9iC7As90tpPR9vHfG4F9QiDFnW993QUoEMtTDJsjzrRPKZqA9twhR_X7PRDRhUSjmuAeznxjUHCJ_8oVoRk1s2Bu65x0B0oJRoJXv80ILgyYVmjLVA42MD602MmzeeIytNj5HAhErNRIfsePO0zUChGEDsm8WFoGzGSpxwIwwOvySBvA5yL7pdg1jb9AmM5xgdn55sKGjBD0JKyYcSpJjdU8vucBCYhA1ju5p_mGEBlc3ZAPkM7ekkyyoKaOSNhh01J1fHllxUuIFeAGsCohiWeb-8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24655" target="_blank">📅 03:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24654">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwwOZOKJKr_TWQxgLyevF0hS3-ax50wtjhItWgKl_uZLtdxSX0HCfwxdZJopj6XSwKaECbRalPRLg6X7cAm522udFMNzCQpxxqWIsYKu4u7d5gRBGkUcKkXndCEwxYVSRRlsSZ8pS9FS5w5TH9WfjC1bzEans6y01EBi9eL48xSfyGDVStom1_5YkwWzJp3m0j9RktWeUzFtvpwdvDjsUCxxYN0PVy98Jnz8JTQuM62P4WwkxLlRW29BsAaYJsTc12nr_7g-HNrQ-Byvgy8-srVBotCgMGT6gD3ke1UCdYPR3J7XS77KFS8XHGxyrQI6FdgLKyG3S3HE8Ww-kVRg6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24654" target="_blank">📅 03:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24653">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=Kp2qSx-ey0cFQJ-Xz270wz-LxxaAwebtvafQ8PbEQjF6QecY5Xn0cbjm_0YgQzqMoEd9scwToreWvDmQXQAp9z8PSBjnJAX28FiQYeKvLBiUPC7uC2RLXPAVPS6cINGgTfryt8ysW3GjyZInjm1PakkUAHRXkqzt43KxzaxUguCastC3bpZHmZ3rXi73sKq9Nup8JQpsKhFGIlRKqB0ufakb7PyGaL9ZBNQkRlQVoKgFglOO84mtrTb52b9PrmgE-hnuz_d-XDdVrweKiqCGniWe4NH6s9OOVb07dEGinrgP6vkOSkXU6rtDEs5hlSg1sYMlnvifsF8aRiKCANIM8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=Kp2qSx-ey0cFQJ-Xz270wz-LxxaAwebtvafQ8PbEQjF6QecY5Xn0cbjm_0YgQzqMoEd9scwToreWvDmQXQAp9z8PSBjnJAX28FiQYeKvLBiUPC7uC2RLXPAVPS6cINGgTfryt8ysW3GjyZInjm1PakkUAHRXkqzt43KxzaxUguCastC3bpZHmZ3rXi73sKq9Nup8JQpsKhFGIlRKqB0ufakb7PyGaL9ZBNQkRlQVoKgFglOO84mtrTb52b9PrmgE-hnuz_d-XDdVrweKiqCGniWe4NH6s9OOVb07dEGinrgP6vkOSkXU6rtDEs5hlSg1sYMlnvifsF8aRiKCANIM8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هالک‌ایرانی‌درگفتگوباابوطالب‌حسینی:
شمشیر خوردم و مانع کشته شدن یه بنده خدایی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24653" target="_blank">📅 03:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24652">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1TDzu7WOY7OPEsg8wvwLTKP_dsotx1hmaPZjcm2SvdZQURq2ukefYTqE3H05ufMt-rCjsL8lD62nNLkly93MY8tdjqDlSnDcmEtJxdHA9qtt4GtkNei5t6eD9bI18VPOxxm4RkCxINVBiJbdN8GPvT3wyGyvdyq0B1Ic5mLp4MehjeKjSfky_T1z6w1iaf3YWP403Q4V5f1U-wHk2vR828fyJTN1GYthlkd1FORssBbcWVzFGyTq3OcWg8gffsDzp9aJmCMX0oqN6PyMlicz9obiNxC7o5oZeClOhPSICuMVubTHuNTePUn4TChKUJWvNRvQDWGtvi1UCS5RUoCmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24652" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24651">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5qx64r1Co57N2gdNZD7ArOdRrA22eaVLVupCBf84ZWNHyN3TnBUaNB6M_oFbtU5nvFVvI08QrQCfPEbn47uovKFxzWqU64YDFKfi405ekrw1w7RKYNQy-AcnmL0HUqwNRQ3hHoZtdrMavfW1sYBxN5lr84zpyU6uGks34Md_R6dA6bWwIII6NFkp4TjfgAMKDvlrZVEVM4skO9H_uGfzV9mOmt7RJPwWTgkbmE0gynq_gClPpn9yf6Y7Oe3iLhYeSaTQ3Jw6wD1GG8eeMQRgSYEcIbga2rX78EJh0u0dTkkBlYYFmoxzxvqV-yAFSNQ9qBYl9AU4lf7gEUC-UKVsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلمان‌امشب‌از پاراگوئه‌گل‌خورد؛ آخرین کلین‌شیت نویر و آلمان توجام‌جهانی‌برمیگرده به فینال 2014:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24651" target="_blank">📅 02:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24650">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=aaYgCrihG_mRW0cIJxAG3xdWZANSPNCLaOV4ZhVIqD2-Yah8by-J1QcsGR3Z4t-e2ZLeEjpLB8V_WpQJ2eiTjNXxzHT_UW_-0F1m7cbwcIPr2gPKn-JY-JWYLmndKpK5bIINTeV_PncsJ3jtFzYjWLOdPp59ic3nAVVwQU8HfcZGtwsCNf1vSTYpgLgOKB5K5RruqoytwE2fjp7lnn0qTaItDngdury5MRSQ6zjd1luxz5h6nXcs4u4BVnGYuXFfcNRlEatWYQuaCZYIp4vv0zFWhB-5ENn0nHBAriSyDkgqOLnAZy6tNfwBL7d747dbMV24UuGM6kk7LzlLinLxhgX0uyr8WvtTlvgbkyAY9ExuRPTGtTAFVG5Qc5hiLuwhh6oJAOc0m6xd_K6A4eH3rLHrARRsD66i-mrWjUelQmmPLgQOypcJ4CYg525THtnHzp8FNmlo1UeeRLOXFdOg5LdbSC3W6ciILKic3iS5_tzKJLnsC9iW3whIhTvC0kHlMlPHFQEziw0BcMxboej57cB4hWlfkoVDWeKKBDTerdcQpNx-HVMf9sCXMDsLibHybbpHW-hkrgR5w8BKHSkUyteZcfdJccVd2QB5rppoHj2CS3AuHFzDCGNotHowo_4bRXFgiDCw0PEhCpOLew3EUOFC6LDQrkh3j9DCGX7Cnmo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=aaYgCrihG_mRW0cIJxAG3xdWZANSPNCLaOV4ZhVIqD2-Yah8by-J1QcsGR3Z4t-e2ZLeEjpLB8V_WpQJ2eiTjNXxzHT_UW_-0F1m7cbwcIPr2gPKn-JY-JWYLmndKpK5bIINTeV_PncsJ3jtFzYjWLOdPp59ic3nAVVwQU8HfcZGtwsCNf1vSTYpgLgOKB5K5RruqoytwE2fjp7lnn0qTaItDngdury5MRSQ6zjd1luxz5h6nXcs4u4BVnGYuXFfcNRlEatWYQuaCZYIp4vv0zFWhB-5ENn0nHBAriSyDkgqOLnAZy6tNfwBL7d747dbMV24UuGM6kk7LzlLinLxhgX0uyr8WvtTlvgbkyAY9ExuRPTGtTAFVG5Qc5hiLuwhh6oJAOc0m6xd_K6A4eH3rLHrARRsD66i-mrWjUelQmmPLgQOypcJ4CYg525THtnHzp8FNmlo1UeeRLOXFdOg5LdbSC3W6ciILKic3iS5_tzKJLnsC9iW3whIhTvC0kHlMlPHFQEziw0BcMxboej57cB4hWlfkoVDWeKKBDTerdcQpNx-HVMf9sCXMDsLibHybbpHW-hkrgR5w8BKHSkUyteZcfdJccVd2QB5rppoHj2CS3AuHFzDCGNotHowo_4bRXFgiDCw0PEhCpOLew3EUOFC6LDQrkh3j9DCGX7Cnmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
صحبت های عادل فردوسی پور در تعریف و تمجیداز رامین‌رضاییان‌ ستاره36ساله فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24650" target="_blank">📅 02:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24648">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=jR7wiU39W58yOugLKIWNCnSxlD1sxgFaE8A_Mgrd3Wv7oCZDyDBaXKvnegj11yyFvwFcS1NmJ1ZdY2218j2R2rBhdYmkZMLSof9JpKGVQ6640_iGibec6Wd3Ono4CgsJIxwyu4neUZY8jh4LZ-SlpKHDft1nPOcPIeyoybTYnarA1GHuS2WQuE_FnyjEhhQsspt1_ifoam7Xp2ADmSyT5qOMh1saiKVq1byXGMUorCqil8LbY2nNUKykgjq7uMWCck6aOPnYsJZerbx7jPCxLIrOwIHRCr4XOGSkz6lX9-sGhf6hXzFBpOc5SxRdZ5Pbv8VgtT2X5qfYnq2ubeGNpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=jR7wiU39W58yOugLKIWNCnSxlD1sxgFaE8A_Mgrd3Wv7oCZDyDBaXKvnegj11yyFvwFcS1NmJ1ZdY2218j2R2rBhdYmkZMLSof9JpKGVQ6640_iGibec6Wd3Ono4CgsJIxwyu4neUZY8jh4LZ-SlpKHDft1nPOcPIeyoybTYnarA1GHuS2WQuE_FnyjEhhQsspt1_ifoam7Xp2ADmSyT5qOMh1saiKVq1byXGMUorCqil8LbY2nNUKykgjq7uMWCck6aOPnYsJZerbx7jPCxLIrOwIHRCr4XOGSkz6lX9-sGhf6hXzFBpOc5SxRdZ5Pbv8VgtT2X5qfYnq2ubeGNpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24648" target="_blank">📅 02:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24647">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eG9tTVBGsg7Sj6FGHt14FyM_p70ScSNIOtp-gDeXMP15xuXK0bi_MUgEjT_4S_jgpTZfhSWNKjNBeLRAQiCgUyT2RgNxnwladLHkn48w0dDSuGkCMSN0mFz97ciZ9otH_EEMowIFKcCb5uEMQi99XLmGTairwQmAyhyywUdjx5ad4_M8ai9qgbUbHByLQSNXmDaDxXdo2wCqejo27PRJXpmWhGMqSRaqSEAiO2yfS8Hp1bEy5O2DzXFCumGNO6m20B165b4CMYGlkE7qvvXrnljXDgNiHa7UnYrYwP6k1sXYyAlCRRoNZgK6b0DEnJO1k1B2LeEYnTvvOj_Xe48hAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جواد آقایی‌پور مهاجم‌سپاهان:مردم عزیز اگه تو رشت هستید و نیاز به کمک ضروری دارید به من پیام بدید، کاری از دستم بر بیاد براتون انجام میدم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24647" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24646">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24646" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24644">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P09t_oZAYs3-VeDxKtUTIVrc583lMPAFrKKz_s8O0nka2kpOFYRd38Y7UHD_Z-KwvCnzGjQvVqexw_t1h20i2juzoam2eWEjVH0YyKeLICUdDHJF6l4mjKZ93mJr2VkP0z2wHn838-LPkddsr-PLI3ZkGk-CZXWFZhJBp3LkYMgaHa2vzLD5FvWqLk2cLcYzIjqPOzmXpvmIgnYsMvECHDUEgtyR1r_ElaSFauc-jpjXzfPX-sLaLaUT8uLVno9BvdP-CTr9-k66WBUOUaeBeXR_iWjxfUgQlz9zxDEppwIEEBZFa1HExLAbt-7uOSkGFr38RNGL_Xf6HJySk5jRLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ علیرضا بیرانوند تو جام جهانی 2026 :1 کلین شیت نویر تو جام جهانی 2026 :‌ 0 کلین شیت
‼️
تعداد کلین‌شیت درسه‌جام‌جهانی اخیر: بیرانوند دو کلین شیت داشته. مانویل نویر - 0 کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24644" target="_blank">📅 01:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24643">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmWLR6PY1ZPQ02W2ewdVOIh6IBWStwHF1xkQsgOxGqODSAHEQJXlyLwJkO6SzuXPUeW2aKB862CT8DZEcsIgv0exjxtOeQQRWycfYWHSxCcDsSclzwRun6mex8M6Ar_oXmuJ7G65u_2hJ88X4BU1qVN-lsMf3H5I3gse263uApqMZND4uXzlFpFLLqjRAp6k0zdcbLbfJayVRWeYqNOlH-QBg5RY5oYMwkLJvDDh1ZCgUPChEkq1CEriOwpNwyqwU-ec9hq090NspDt0daCLA9IDKYFrjflHTM7BgaztHQBGyeCbNtbIAJ5F6TggbpdA6ket-so_Rkfv2OjWqrSB-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24643" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24642">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBR2NKVJ1w8Mh7fwALcJvwCo8oU_CnSUNyPDO4-LIWv-vCpchcO2lATL3_-wW5QQkDUuLrmpa-M6x05eHherN-GhoZneqeuehkKZH3EPLUqlUUkqBrbdywVwFSVE4k5Kmz6lXUQgLN_7KHC5zr533xBeQ2KlO8iRNgphHWePuUAiaHhpjbkd1rkJgfnK9C5odky1BSTGCI1w_z-4IR3TGQhSx8H9ZQw6_Z5rQVAZPNRrHNs_ecREupvdKxLyKezwBYojX4gB-f6puaK8-hAeLuDjvW46j9RB6ngDsKCDaaNEmwQRWg5KDrjBGGRuHSIEHkQg9UnlE1AvcDIjVfNssA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
جادوگرغنایی: تیم ملی آرژانتین با تمام ستاره هایش مقابل کیپ‌ورد غافل گیر خواهد شد و باشکست در این مسابقه از جام جهانی کنار میرود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24642" target="_blank">📅 00:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24641">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm3vs9v09pAnit44_m2LmE2DJrIwj-OXRHOM3ZS_2bcWrsgFoR2faiQYThsDIws9Mz7WsD5qJvmAf_VeVElFkdM02rVcYHvb0JWYOqaGqyphz10CXb-6ap4rbOmALqZ9s7GlA0U5bhngGH_9Q5l_w8JuW4WN6NhsVNhY2TKHZQ6CeZl2AX0a4otQDxUZ71C_1XX7Otrg6O8GBbrCZ77usDge8ucye6NKZq31jUt8DTkeMbKLzwTRpOE52tZllhhRiSVwa_7yAjwzZ0B_Tm1dhlUPMwRRttRGEJVjsrjksX9s9qLeS6JO8jQNd8cQfg1loFL3JoRDsqvChTwOg_uZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق پیگیری‌های رسانه پرشیانا؛ بخش رسانه‌ای باشگاه پرسپولیس پوستر خداحافظی از اوسمار ویرا روآماده کرده و بعد از تسویه با او منتشر خواهد شد.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24641" target="_blank">📅 23:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24640">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=heXfO4_xOLzJJNJMnynysIsAPrS7k77DkGX6Di9vD3UoaHlIT9YV04ELgokNNXGb9umZZW3Z61XnIx3-ZGQvxVG44yVFb7brPzKCxkwgob7Dw4b2AxHO_ezwyz8aE2lfnQ0PKV5_H4ldqNs07G5GqVPKL7mrtGOBA7oJM-umY844li5_0rv7L3NQAq3y28vopkmVoVOT2P2mbIW--ZwzwN7RWJ_ELjiaktVKz9qahyA3221GFOcYzCPony-d7aEQtfQKPRNPV2UtJ2Awh2kR-IPsTpdT4MGQ5UAIoTSi72FGzkMXH6QyhtH7HhfTQXnX5OD9fcbfYxf1S6S3jHEuZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=heXfO4_xOLzJJNJMnynysIsAPrS7k77DkGX6Di9vD3UoaHlIT9YV04ELgokNNXGb9umZZW3Z61XnIx3-ZGQvxVG44yVFb7brPzKCxkwgob7Dw4b2AxHO_ezwyz8aE2lfnQ0PKV5_H4ldqNs07G5GqVPKL7mrtGOBA7oJM-umY844li5_0rv7L3NQAq3y28vopkmVoVOT2P2mbIW--ZwzwN7RWJ_ELjiaktVKz9qahyA3221GFOcYzCPony-d7aEQtfQKPRNPV2UtJ2Awh2kR-IPsTpdT4MGQ5UAIoTSi72FGzkMXH6QyhtH7HhfTQXnX5OD9fcbfYxf1S6S3jHEuZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24640" target="_blank">📅 23:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24639">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0usCYQ2hc8_7SvjoaM1eiaD-cQHiTmVazGNH8kNhpQHxrMLw4T-zDM5jSpfj25taPNQ5P3yk8vjNCRIuDdBsAIfkDYmewk3K4SQ_AgQ92CokbYN9V5ql1VUOiEaWYEHatBxt7V5Dc9uLWFlcMwrQVNnpn3TOerBvrdc5qkjSY9MsXXC652TBmjfTSMD5okhEcnui5mV1_Vt6VcWj_j-htt2J2A7IBxHjO-DhRvACqkrCrS58Zsn3nHdR9qyYkvfMtU9UX8rTweC2uf_Gyul_VNTdSePaWdTm_MeEv-nnosGdoULREeuEui-QWNBjwXQmsKMixcjyp8Ez50Zos634g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24639" target="_blank">📅 23:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24638">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cr8elVos-aRXSr38ifvABfjSz-BcygOiyxfIgkzf-pEyM7sBvPBtqorDr7rpw5med9gooN9R_7QLjlubAuexPKpdNJaB0wfJ_DSaaxcabqz0QtBeHF21ehsP0Ioo6cmk246U9Z81SLw581xCjIfS_1fwiVWkeOfPJX4rRlA8K_afNMTjsx-Pn3RhWnWk6Sum-1xJa3tntWAL-lWIkPQVx9LtpioP9Pk9p01d6o-mCMEjJ4xa7xZk-6G_muDgmn_Avxtmc-TfXkLjRcpmlIsmeDFnEtL8ZSL3o06OBaPOXl6fV6GKme3NmNwQjdkYxVkUYDJ10UR-8ewVKPL4g7ZB7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛صعود دراماتیک و نفس‌گیر شاگردان کارلتو با برتری مقابل تیم شایسته ژاپن؛ سلسائو بالاخره سامورائی‌ها رو شکست داد و منتظر نتیجه دیدار ساحل عاج و نروژ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24638" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24636">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt_YVfXwbhPTu6Gpqv3OC7CyJdhVdxkS6s1YHHcwtBDuvTjLYt0VSMyHaYQd_tt-GQRwlar2ehFHXI1fXd5Y7ptNjJaK1k5rPED179kBKg3hIxbRElxa6RNaod2fdMwXdWmKQfKsQfgHzFUzM-PMEzV0bQnmUZeNnD40jWFzvCKiAW0MMXMMwb0FhFv17Zea9JMjuZgzcGzIQ0KMaBFebZZyKYUk_xkUQ0xNk2MiG_icxwtZ9jqUJdjUiGigX9nKsNUSmBL0Ib87-Bx6QYOEQH_-NNNCNmesnyXhVhS0YbIQvFubER488zxEzAJ_BkuKqA-WBZU4-5SUALmdm4Peng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛
از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24636" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24635">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCgp4NMCE8oDK98qGUrSxSS6kPuCXMTTmFbIlZzEy7zo37hLUEakRT3k2eOflsOUYA6ug_qO0ZLMoMcyD2DnpMvQtEnWPcxm9m56nRbZzJzJl6PsM_yUP0XqXuP881tis15_nG8NRV5TQBeLpzh2nzANbhOrN6I7d4RW571drb5O4a_vZ949QOp4t3zfDQM6IhXGgMmEjaGHaQ4mo6ymJUKB-YduWcCEZf9hc_1FmsO2sFF8kik_bIY7A1cfSCniRBuar_n31xVSUpVp0dbSZ9kJjrAnOfSUW925kxzOoo8HU2rx9xPh9jx0jGUmGg0L7OxfIwtiP2VcDf97P2G2Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛
گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24635" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24634">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BktUkHioqU4O33FGneAy2ziLSmi5942W7uC39uTBfdM-wdkrLmUxoEV8XDn-y5GjoRWfGoJtfpYVwEBpsAeZJA3g1JRc13j0GHqEOnrcFZJItI8OlQlAd8yxQGGxw9cCsqgCvpfiBV69dqinI9pdzZw3Dic9YMOKQN3SX7BCJ-YO1-AgW_Wjrctj0RPvn-6Y8NZuM7RI5yPsgoqWfOXM4QiOiWUuQc7ZP3mt13YVhG__rUFk2J512HlCvD9pCft1HH7t3olQ-LIqOJPtJ78AOzF1N5X8eHCoDos9CsZ-DiBqNudJ2Rsvg92azytBMy7eMPmmSRYXKG3sX4Nr5ONqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🆚
🇲🇦
🗓️
۹ تیر
⏰
۰۴:۳۰
هلند
🆚
مراکش
📌
هلند یا شگفتی دوباره مراکش؟
⚽
🔥
هلندِ که به عنوان صدرنشین صعود کرده برای ادامه مسیر قهرمانی به میدان می‌آید، اما مراکش با انگیزه تکرار شگفتی‌هایش، حذف یکی دیگر از مدعیان را هدف گرفته است.
👀
⚡️
لاله‌های نارنجی صعود می‌کنند یا مراکش همه را غافلگیر خواهد کرد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24634" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24633">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thpw2QlkRzeZj-iWlYlldqzCdkHv9Ll30d1m_V9W2Gz616EHcNkN-1j_nk7iJth1XVn5scXEwSLVvkLvY8Nbmq6wyc32W_E3UlMvDKKf9SsEEbsG-Q-1PlmoFO5nEFX-PSqMZfgPN9V6d0bQyEuvIQxgRF4brHMUvdUPRF-m7pSJd8zL6gBlAdViJ2d8oA3Fer9qAYhM4X_LbbmL9vKBOxJaL4fGZgSVWtD253P4e3yC0bvlmfCtoWnABd2uSJ9vWyl-oBYkPEXU9RpV0DCn5hn6PJAZ6ICJ67ODjjI-tzUgl8Q98jNBGr5PbWzg0zz46nUPJBYN1stGmPMSnOP79Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24633" target="_blank">📅 22:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24632">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnkNrHj27La6Kf7K_q_nYRehV2qjAzUSyTiJUIpqie2ig_bLN-QM7tJn623jT7_igGPgM0gArAMw3dYmkfqONull5JboWN5r-8sy1QaSgrrgmPP-p6ytGrDsZVOMUeCk7B3BwLadth2hSJn94UWr2ABV5Y6dd9cpoYY-ikvKbyqer6Msv09iu7FPZeVYON_kuVGFQDdc4KUDe16Y5PBLrpufMnEkhuq-kVmpt2iXOSR6Em6gyJGmZ3M3cX21Fi-kEYEcSjJlSQ42iEv5cvRNALetUoG3JWVZG10m3l3g7RkZ8xU_FfcUUpaMp4_6gqoKAkvgSHCWN8TjloqG2WSfVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاسمیرو ستاره سابق رئال مادرید به این شکل گل مساوی رو وارد دروازه سامورایی‌ها کرد. سانتر دیدنی گابریل رو ببینید. قشنگ گذاشت رو سر کاسمیرو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24632" target="_blank">📅 22:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24631">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=LnkHFrcStXo8yIL6R9vEIC8FsJACghwRtVK273eIKpEop2_WJViPBfornsp_Wk8p5YzkpM1c1ZP2dIFieoaiJrsNTcG914A5JpxB6ysayAfwBQeZgSFmgEbX4LvhEqnWatmWMUgXczbIRYKxeCNpANwdr13GtRF_Ng9d-a-1hcWX8mlslvOW11FKbykIz5XgJpZSqcHWn7mDG1DgO05rpLTIX_mPwV8ZaIaT6_Q-frCUixlyUfMCTA6KK7x5wzuZBNyCwuqAR94S93zHrTVC0yci5HueZQN-XLNP6gd4mnQvAhh7bQcZLXtxWMz0pXbCaKCs_T0Ht8oNb4GSZojxn6hOXkEng7RwWfhka_qpQ-eM58ocysxQBl3yuckM-Z42EN17umSoo7TN3PDlPrTNTc_OASSYU_tAW4wL_lZ-lZ0kaYVnStow5PYwpeTKIjRUs-OhStZ9IjEgE8T8RvjG3clF56hNrmewVBUiHwRb9vtZQM_ycYGj2ZyES1A-txKaB37CklslDF76JAYxHgSPglbj9ilzVo2Zt529gowVVph4Vt4Nhdb_MBxRIiKTY-M5wZilMlCFaDgiegeh6xZjKVtcfUd3c23Nk8kWwX8VGfLYgZlihObtCsKBo-vnhI_cPeDD6Om3SugGs7Z7TSF2DCN_Vous-Ca9CBaxiXRzcLk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=LnkHFrcStXo8yIL6R9vEIC8FsJACghwRtVK273eIKpEop2_WJViPBfornsp_Wk8p5YzkpM1c1ZP2dIFieoaiJrsNTcG914A5JpxB6ysayAfwBQeZgSFmgEbX4LvhEqnWatmWMUgXczbIRYKxeCNpANwdr13GtRF_Ng9d-a-1hcWX8mlslvOW11FKbykIz5XgJpZSqcHWn7mDG1DgO05rpLTIX_mPwV8ZaIaT6_Q-frCUixlyUfMCTA6KK7x5wzuZBNyCwuqAR94S93zHrTVC0yci5HueZQN-XLNP6gd4mnQvAhh7bQcZLXtxWMz0pXbCaKCs_T0Ht8oNb4GSZojxn6hOXkEng7RwWfhka_qpQ-eM58ocysxQBl3yuckM-Z42EN17umSoo7TN3PDlPrTNTc_OASSYU_tAW4wL_lZ-lZ0kaYVnStow5PYwpeTKIjRUs-OhStZ9IjEgE8T8RvjG3clF56hNrmewVBUiHwRb9vtZQM_ycYGj2ZyES1A-txKaB37CklslDF76JAYxHgSPglbj9ilzVo2Zt529gowVVph4Vt4Nhdb_MBxRIiKTY-M5wZilMlCFaDgiegeh6xZjKVtcfUd3c23Nk8kWwX8VGfLYgZlihObtCsKBo-vnhI_cPeDD6Om3SugGs7Z7TSF2DCN_Vous-Ca9CBaxiXRzcLk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
جالبه بدونید که؛ گل حساس کایشو سانو مقابل برزیل اولین گل دوران حرفه‌ای او برای ژاپن بود. تو ایران هم‌بازیکن‌داریم تو بازی دوستانه هتریک میکنه تویه بازی خیلی مهم مثل مصر پنالتی خراب میکنه. فوتبال ژاپن 100 سال از کل آسیا جلو تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24631" target="_blank">📅 22:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24630">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔵
تیم چادرملو بعدتساوی بدون‌گل دروقت‌های عادی و اضافه توانست بعداز زدن ۲۲ پنالتی در مجموع ۷ بر ۶ گل‌گهر را شکست دهد و به سطح دوم آسیا برسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24630" target="_blank">📅 22:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24629">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGYj8wzJgRlKOQzlQyozKE1enr7SvSIp0v6wFJ-QASzG52LUh4QfBbWOFgnoCnd0n65N8F4ecBD6Xxcs8U_L7AGS6HoWHpx0lzKzL2RJt0_Cs2FgKclQBJZBjk6Mby70VFyRstDr74eNyHthdElCcavX0o7Btu9YBJppHViLuA0uajN-U2NxkbGprOFxE7aGecO85V3A1dL0zcQZ-z8ignf2CkA_xIkrFltPFuAqLG3MTEZeCrxm1HB-BfRgv_TAtyJObTWUivawok6As8xEQ0tPK6p1j4AfAjnG3SCLtg7xpndC4nKpwpyQraBQ90TzpWFOlJhqAxFIRF3PJPTF4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
باشگاه گل‌گهر سیرجان: مدیران باشگاه پرسپولیس مدعی‌شده‌بودند که این تیم یک ماه کامل برای تورنمنت آسیایی‌تمرین کرده و این تورنمنت باید حتما برگزارشود امادیدید که تیم چادرملو در تنها دو جلسه تمرین این‌تیم رو تهران باتمام ستاره هاش برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24629" target="_blank">📅 22:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24628">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=UU9wW6Rc2LCIsy1suS80SKKBbFdE9F_92_H-ghr2pR9cGePjtJjtVm5QnRm5O7_opPku_q6MUVw7T_4kIN71uN2kJkuKPEe5uTlakaGZx_KkbQ76NBaI5S4Pq60AQBmOZLjCnMVhw6fu1TyeyTl8m6iR263UTxf13nJaxOLxMTzOvFAgEnyKO5RpiG6m2QOJ9ez2jlKBkTNekZ2VEkE5zGxekojxDWEFETbvx7AXJi0gQ-LMJhJpJzSG3OzV1hbXMqkAvbSTehCjPoCAgER-z0ocolZKC5fVTr6joYugRq9Bj_usSvJXjoQBnQct9DTJR977lX4eTBxEizSZMMZI6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=UU9wW6Rc2LCIsy1suS80SKKBbFdE9F_92_H-ghr2pR9cGePjtJjtVm5QnRm5O7_opPku_q6MUVw7T_4kIN71uN2kJkuKPEe5uTlakaGZx_KkbQ76NBaI5S4Pq60AQBmOZLjCnMVhw6fu1TyeyTl8m6iR263UTxf13nJaxOLxMTzOvFAgEnyKO5RpiG6m2QOJ9ez2jlKBkTNekZ2VEkE5zGxekojxDWEFETbvx7AXJi0gQ-LMJhJpJzSG3OzV1hbXMqkAvbSTehCjPoCAgER-z0ocolZKC5fVTr6joYugRq9Bj_usSvJXjoQBnQct9DTJR977lX4eTBxEizSZMMZI6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های ابوطالب حسینی درباره خوشحالی بعد از گل شجاع خلیل زاده در بازی برابر مصر‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24628" target="_blank">📅 22:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24626">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863d336b56.mp4?token=LJBAiC3xwUUA7wdVSB2wEeGolvxsfHe3iAj4Hh2t41AK3OtE5Kg7E7ZnGlcAd0i84t_8HfGnrJgOL6sOHyFypJQQ06MMu2gcE7snE1euobi3Nn8YurK66glpTNJO6QpNeC6gX7PRAUiV0OcPy8PKh0KEgVG4cXr_w38Ml-tIFWTMm7HiG1YABuJdkUv1c7h6YA2SKCHghmqBXSwV_nVTVwvd-nRhH9zOVrAjyQLDVj5SixNGiuI8KIkdm0_VxG9Bm70iP_UPd0sSCNOIFMKx34gnoh7snQuvQ72czRfn8rGg7iLmNx-vJY3hNEmSt4KZooSMjEHyyS2U-6jilGCQaV5ubcL4_cDDmzP_bCdu-xLc8t0tRiEkem10sittDqpKYbZRacmT5wWsM9qpxRX4CfC19vpc2aFMny6oNEBbbHQRET-KFJpdghdb_Xi80zH13a8o-VuAmBM0eCn5XYrciDuZnUcJrYyuUJT4XjoC7H9Ouk0HWbqiE0-ME4v0ByXrYJ3GydAhoV8TJoMhyiKmdnIWm62ghRh-vSp90mQe9P47xTf4W8aIY_jcrT3EODYon0HeT3Id3_l3omA9MhZDfV9I269q_P8Lx0W9O8dXXFIl--aGUNMzOnwHG8qBHKur44VR9IlcRWhmhYK48oHWsZdvwY5PeQ_U0qCwBxveQR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863d336b56.mp4?token=LJBAiC3xwUUA7wdVSB2wEeGolvxsfHe3iAj4Hh2t41AK3OtE5Kg7E7ZnGlcAd0i84t_8HfGnrJgOL6sOHyFypJQQ06MMu2gcE7snE1euobi3Nn8YurK66glpTNJO6QpNeC6gX7PRAUiV0OcPy8PKh0KEgVG4cXr_w38Ml-tIFWTMm7HiG1YABuJdkUv1c7h6YA2SKCHghmqBXSwV_nVTVwvd-nRhH9zOVrAjyQLDVj5SixNGiuI8KIkdm0_VxG9Bm70iP_UPd0sSCNOIFMKx34gnoh7snQuvQ72czRfn8rGg7iLmNx-vJY3hNEmSt4KZooSMjEHyyS2U-6jilGCQaV5ubcL4_cDDmzP_bCdu-xLc8t0tRiEkem10sittDqpKYbZRacmT5wWsM9qpxRX4CfC19vpc2aFMny6oNEBbbHQRET-KFJpdghdb_Xi80zH13a8o-VuAmBM0eCn5XYrciDuZnUcJrYyuUJT4XjoC7H9Ouk0HWbqiE0-ME4v0ByXrYJ3GydAhoV8TJoMhyiKmdnIWm62ghRh-vSp90mQe9P47xTf4W8aIY_jcrT3EODYon0HeT3Id3_l3omA9MhZDfV9I269q_P8Lx0W9O8dXXFIl--aGUNMzOnwHG8qBHKur44VR9IlcRWhmhYK48oHWsZdvwY5PeQ_U0qCwBxveQR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خطای شدید روی وینیسیوس در بازی امشب با ژاپن؛کارت‌قرمزنداشت؟ داور به کارت زرد اکتفا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24626" target="_blank">📅 21:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24625">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHoVsK8kCZTpxUQwTbcvbh60rcHMu231b8k1Vh6fmNfMb7uI7XeZ4SjoGQ0BZQpNZhxY_DKrIEOkEOo5yxAsJhyFFlpriM9P1wKg8k7c7zYff37OfDrMAOGwgWRgl0f-r90gAHvQM_NlAcgvN71fQu_wQcowte3NmHm30-MWuhZWEkLQVT4gUkrMQGoxAjvDczOLTsvnMjX6B0dDuaH0gDFOdgHpWqkEqc4pk-p_wWCMoR1aTqi8AZiHQc_KuHVY49WiInyfomw_jaE9BM5N_aeGtmB7UgLcvoPgenIE2b5McefIn4sn1UmRZe5xEsuGid9_1pI87zToX_PWeMmXxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک شانزدهم نهایی جام جهانی؛ شماتیک ترکیب دو تیم برزیل
🆚
ژاپن؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24625" target="_blank">📅 21:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24624">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7056183539.mp4?token=b9wai5HWJR93NhsqGnVYEsYUpy81vytdf1pOwwMxeRGrEt4_MkmaJyi1onyOxBiheG4iLn56-VXVgFKtw0gozjopqw-kwnWb--kyE3LsnqsEjaiP-EARaPFXepr7vH5JBvaO2lwwXwUfKgTvlhBdB5AQMR9MgrSg46sHQha3wgtLpWSoLgZVXmFMBOdPO1eK16EF7OAY6Ut_lk3yTlck0KO3-ipNVSCOBotWDe_gtXp_yBFk9WeRftPvlqxbw-o6gBTOHMgGvcMUC8GLCxDOrfA8aMmYT5U8mzirH3fUR_8SjOfSsY-_Yb_9GIJjsvI4Dm5_J2SoqL8cbnopJFA-BihwCOZ6a3Vso8zML_PM4FmK9DTAAXBlEKPiu6RloS51__d1QniPUfrwLBs3hAs_ZRpLne5Fju9_Dx4WWQ_Ih0kJQmojYB7wOFP2jnJjumunD4LQA8C8zggvk1SfC0pVtKVAsADdzAfyRmlcMoAp5rXzk0pjWIFOBKeP63owLdIQdJYNIHPS6FDa_ra7WzrnYHTQp3Ker8WQ-SA8qKwwLtrHZMHH3ZW-_LxDz8nYpjpkNcjvDVfqm81_waRTXnBKdjeL6fnw5na-9cMw45T5RWpeJtY30YInLQkefJ126ekezrtC1bKV6ox4lbWPV2w_hB2Kd15XSY-khO4qH7HlwUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7056183539.mp4?token=b9wai5HWJR93NhsqGnVYEsYUpy81vytdf1pOwwMxeRGrEt4_MkmaJyi1onyOxBiheG4iLn56-VXVgFKtw0gozjopqw-kwnWb--kyE3LsnqsEjaiP-EARaPFXepr7vH5JBvaO2lwwXwUfKgTvlhBdB5AQMR9MgrSg46sHQha3wgtLpWSoLgZVXmFMBOdPO1eK16EF7OAY6Ut_lk3yTlck0KO3-ipNVSCOBotWDe_gtXp_yBFk9WeRftPvlqxbw-o6gBTOHMgGvcMUC8GLCxDOrfA8aMmYT5U8mzirH3fUR_8SjOfSsY-_Yb_9GIJjsvI4Dm5_J2SoqL8cbnopJFA-BihwCOZ6a3Vso8zML_PM4FmK9DTAAXBlEKPiu6RloS51__d1QniPUfrwLBs3hAs_ZRpLne5Fju9_Dx4WWQ_Ih0kJQmojYB7wOFP2jnJjumunD4LQA8C8zggvk1SfC0pVtKVAsADdzAfyRmlcMoAp5rXzk0pjWIFOBKeP63owLdIQdJYNIHPS6FDa_ra7WzrnYHTQp3Ker8WQ-SA8qKwwLtrHZMHH3ZW-_LxDz8nYpjpkNcjvDVfqm81_waRTXnBKdjeL6fnw5na-9cMw45T5RWpeJtY30YInLQkefJ126ekezrtC1bKV6ox4lbWPV2w_hB2Kd15XSY-khO4qH7HlwUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب حمیدمحمدی درباره شبه علم، خرافه و فوتبال در ویژه برنامه جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24624" target="_blank">📅 20:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24623">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGX4hXqRii6Xw-1UJNV3ji-BfqkrF1UiOm54JmA6xoAuvc0hRAWEPIczgprgJpk_9NMJfMn1uaUDP3P11Ows63RnXy2hjLMnpwPeNeWsptsY1iZ7FcUarpzb8kQ2WA7KKR-4RENmbPNoq6DKYxgNlQp36B664_232ehcb0_M64DELDlXnb4j1Aj3Yq1HZ9fgzB4N0Yv5FB5b7Wx14GpgGsJPzFfGUVxHM2fxjMpOXQBOCXgVTLKmyyswb2YGgfpw-N3AXaFYLny-n2XJfYU-vddMLtCtuP_O-1T2BWKVpyA1dZJ_lJjK3Du1ZIEWYtDuEhj7cRKDEMecOIXnrOJwNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
طبق‌شنیده‌های‌پرشیانا؛
جواد نکونام در جلسه با مدیران‌ایرانخودرو برای‌پذیرفتن‌سکان هدایت باشگاه پیکان برای یک فصل حضور در این تیم خواستار 55 میلیارد تومان شده. درصورتی که پیکانی‌ ها موافقت کنند نکونام قرارداد خود را با این تیم امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24623" target="_blank">📅 20:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24622">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stOkSyhJ2CWcR23dSjdbgOnmrQCx9z-lhxoOaecuEz_iwnvyf6Gd1aAcoZAlfk0wPVe1mFwFc0fkYrlCCKfvTJN2x94dt4rtkYPjbmJ-VeuAKqD1_ggU_coQ1TZpvmCiFx3XqWEoQqJTzEMTOp972VfR0S6JSryaUNWXltwXA6SxkMVbHywG6BuQbLuu1SchgJsyxSPnMbMfFQ5ArBkBes-wXlAvgDbQ4xeZea0533Ex7tIpUYwF-ULfJyzCA_b3ti1aZZwzOtmEHlEd26foINZeEEJW7_w3ePAkmiFOPDqKvqKNXG8mXj_DzXyR7bULNvUMXi-BTufgNCXbm_ckcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سیدمهدی رحمتی بعد از عدم توافق با مدیران ذوب آهن؛ با صنعت نفت آبادان مذاکرات مثبتی داشته و احتمال اینکه به‌زودی هدایت این‌باشگاه رو برعهده بگیره زیاده. تیم صنعت نفت در آستانه بازگشت به لیگ برتر ایران قرار داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24622" target="_blank">📅 19:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24620">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z3WzHIax-WXhufZuPwu3_lmTxNXxmf_iUCC9zV3hJhpncU_BHndyexo7Qw5deFpeeRQ6TFtltZRLl19AuYKD465h_LUiL_AyEFPXAie_Kda4yPgVGwcvXx4llYu8mjM8oXxIdicmFjz6M3fS6tAFWPGwD5xh8YhXmV4JyohgmS4VUIh3sTnArTw7MZBE6Op0bkSyDI-5A9awq5iVI2-i7rapLiyO5lx1aypdzIYiTEjoO4kn1KTm19uclDiqUmg0AZX2ijTtumAUDoGAzE2CF7FWPSYwlHDcSpt_Wv4mmKV4ut_K9oaqZfo6QajH8RmMuqtlJzbaqN1paIZlv3dC8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n1Gqv_DiKEx4y2vxNvxPKgvJELC-NryH_-cSzvFwiPoHkZm2uxh9lQlobL5ro7VNcuzUF3UsR7VABXYbCY3z8wdk0Rem_Uj_JQbPHOhfJ2Zta-Q8R4HRwCuVrnGh-LNgKwaMOhSGKA_Ng6YO5j3W3mey_YaipSkS0BcgDoREUpJDRNTKS0qoyHYzUEB-u86aid2vYwvYqx-r6Yjj-n2OgW8O0fw7UVCCwW5CThRAjNdYYT5jpCviZT_JKdXKtwfdte6Ny04qjix3_52AbnPsrn6PGOD_X062KCe-fcycjTi2S8O6r6tuGvDCBxEqDPyodLQL-gU8HZwZGnhGjSzstg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
از تلویزیون تا زمین فوتبال؛ بالاخره اتفاق افتاد؛ تقابل جذاب ژاپن
🆚
برزیل؛ امشب ساعت 20:30
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24620" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24619">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMK1yJ0yte4ol_t-KOAHmhX7UMjiyaqbuUJpWU1h5pe7oJeWbUvbOHUQUr0Uc4JYPBFc5CI4533xlO3f22XCkuV5T3Tm15VUptB1W048QMgFwCgQ4ZJb3PzGVx0Z-jjLU26OIuzV9bshOlwVGsKwzLV5-soDU8oP831On_PvnEhrF5I6v8TLk5MMpJVijvBlH58ktpFZjaUgDAIcX_OPWROtMXNbOHdRAew_P-1hMer-jkb_IIertIEDURGk_d_GowiqVxTdabKGlOLOUEh5nHXpXfq-y7-fgFmG1RL5-VCNR5Ke2UvAiTsp4bIAs7ftWtYPzG6Wl4IzfkBSdWaLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شانس قهرمانی تیم‌ها درجام جهانی ۲۰۲۶ از نگاه بازار پیش‌بینی؛ فرانسه با شانس ۲۳ درصدی در صدر قرار دارد. پس از آن آرژانتین با ۲۰ درصد و اسپانیا با ۱۱ درصد در رتبه‌های بعدی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24619" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24617">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJDRkQ6HCZkRGp3G6Jll1Uw__DqOL_q0xs84AmcuCE75X-2DTXpojto_t2QC9RGOwaMlIocztReR2QROw-qwq4PkzbxKkNNpxP8AnrtihUoFYK-m7kYJhP1wY3kiaQgS_uptNq8Y2lW7XIGneTWiygN1oqqt217ArrcDnlFEuuLxmzApvx6sX8r16SiV-eInXFRXm5AY351a998a15Z4IzBD3LPrerfrYfLB9uAV7I4AvdyKWwbhP_-FbPDdTMOHupIdyWXtlB1QUNXURTJ0J234lOpPXOxjdnyFtDDWRzv7TiN1Sw2D_ndo0yiteyP67eudSGYtyRmMOjm450dPgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24617" target="_blank">📅 19:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24616">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXl3p1R58NxtYepJzKdFLTUcBYPmXvGYSt0N2Ga2QT6wP6CnGZzl6GPPctHEk9LHeYRwRt54TzAIq4nGMtJUhZtyaDZRoW8LCryo1TfqXn7ARauCuQmFNRiV5HX86wEVINpoLDa7dHHZtsWIsDE3-m1EhzQlBdAzCga5Bs4Flaiz4nFA4_v8MJtQe2FWS94ifvI91AswsazDz502UMQAvQpCK8tUVDS1NSdLxWeRgcFsrBx0fq0ZjOEttm-lJrxbPsbunhKVbSUxSMgL6kqPcNnlhUgnPcTPHAaqLMiBl25QLv3rZJ14V3V0AXj9YTfKYyJAgFt1hti139-1l_SVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24616" target="_blank">📅 18:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24615">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BI8YWx_dCoTNUmBxMdHOMh1af3Yjw66mfeRO67vzQ3GtcuLG1JXoOl5rvhVn9MbaxK-5iFsK9-FEHmStZaTryoMjzgnZIsdoYDrUtO18iI80xTyTccMI0pNy8au3jNriSq0RWj2iNxutBZOIguiba1Bw2KDjRzim6JFbHsTybhSkapkIezFpCsyMKNPhgwhCReysZlo79TE8eY6btZrUklNcel2XgdUH1i9sHRYbWDsoZ4CLsAH861XXEyIUsR3ZEDSTY1lnLC0klf85ucapZ9rh5mOrCSnFBiU5uXzHewuXJBWmfUm3owsYZqayA0qnVOR1b91NyjtoN-1BavM4lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24615" target="_blank">📅 18:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24614">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hd7YwUEZg0Xq1RcJh_1PylkZp8vhFLf7WF1ZeFYLKdkBEHEvd7LYEgkneYl1Rw97dya7S-bbWpACwQXN0nQ0WgJqYBSSZNnqxems1_R1b6YABO18I0h1wxAhlyhqhSjTBg9mzDhjFQl7xFahuEHFVRA13VYvNvRNTwZkGXz5ukgQmlqoGymvR0by2VLUaPEp89uDvh1SJeaxGBKjp3KC1loD7_ADwQVKHKz3m9MLx-Ze3jQBI2H36zMUFivsXdl65MUqrnDHn5nSANbbsXG5lbUHtMxyttYHFDjrl3jOl9w5g2E7Yd4-JV52MMJxCM7z1Zit0gI8mB9WWVYL8J5A6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه مارکا: مایکل اولیسه بله ضمنی رو برای پیوستن به رئال مادرید به مدیران این باشگاه گفته و اعلام‌کرده‌درصورت کردن رضایت سران بایرن مونیخ اماده عقد قرارداد با کهکشانی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24614" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24612">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-Dec9rIQe49RCYJ0hDpTePp1X72qxHnP38WBTxPsTDYrnkZ3KmfITt3sUM7yf7K7ecBkzYKlRAzfy5V8-uHiwGtAuxRxJ5UJvIbc_bXjcFduAMgbw0TWxlyk9iTTfMdMES50_eOeyfa_XmrP-IlRbRA9wd4C7gvDTccLuAeoN7wbaay5d5L6WmjBZ4NwzabBLBxkBh1_3M5U-F_UUlvDIAFq1vJCB3CjYAvsalEPyT25NK0O5-HFTb8NYeP_Ftc4CAGA5jRlJo11Mjq-nGGxkvjDxHEZYDevBDaL7RKhVpyCPEgEaH7iqzMjGX3luAvQVWTatNpy1yiHmlQlVsbTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
محمدمحبی امروز به‌ایجنت‌ خود گفته تا دو هفته‌آینده‌افری دریافت نکرده به استقلال برمیگرده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24612" target="_blank">📅 16:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24611">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5Ez2CS-gIVxoQv_fLPlPh9soi1OZieWaOBwuTHbmgcodEnsNrUccXA1ujFkqAgTIxUvyfPYMeogGO3feLD7Hyc9_iHiUZ2pe72MsPfnrGTHOA12Z0pTqVW6FGFrlqGHBEPxLpDzBTkHgFwDm8JhMaB2SN45lEXxGK0fsajk7RkhdNrEZWmT-zu449u9jNpTT7jylTeOv_-hFcBrPqpgG1A0leyvFWMcdy4K9iNX_b6bpos0NkTQ50hNGF8fjXv7zuElrjeqzqo2nloU2ZUHYAPJUWBlgyYLXhIRnuMfsR7G2FbIvdNhYRl6hTXeDdWAU4Ru7cjKQIuRetbf3oCsVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریتزیو رومانو: انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی جدید منچستر سیتی انتخاب شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24611" target="_blank">📅 16:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24610">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nONMVeoKQsHIOjiRHJLuthvSDXfPj9eC0HGFQJPSxVZ64sinFDRbp4rnJAiQ14ZjjHrQmTxlri9RxsQQYnwJD14hvxuM5pVHLalz-VICxABj-U8KjkG6jttsaurxan0A5oBCNPkFxURYxttd7nFdQAcDtsd545YkKLtZt6vN1h2CauBkUwA1JMEvZDXZw6RSCduaf1-cIqxyCvabg3InKKwNlHS4KbxqIg_5-BFJ0pgn0XhXmEa2_ByIemcza4z1TbpIrnnx5rXQL0FPLiTxPFyP-Fre4genZH5b2vPstwmb7C6jy-6-0CKEdOe4mEAFB5naKYc8RajDjsE_pC_0vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
باشگاه رئال مادرید رقم فروش ادر کاماوینگا هافبک فرانسوی خود را اعلام کرد: 60 میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24610" target="_blank">📅 16:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24609">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=MISUiV2uOdgij6ifU3RrDc1SNO5eS074EApzJyvmpxhaYqxoLRj6nSfRI75nuDz6LrYnpIB1hKuTJpn4TLXHTzp-ooHZS-0vtEOTEfFNBS84B9Npe8lAZyjkKCvw3KCAuCUcOjsORNKQGyhTQCCQiruUo5EBES_b-dkKvxGNzqma8-8ErfAkRiNJmJXQminSwHrm1zDV6BZIANhuwI5Vjzzv5fH85uKv_3yJTKUTt64wyPfj1irE3LOOkOy-qD35c1nxhApNuAhn_8REK3iNPyg1IX4hzxGn2lqUxl5bQ2AyTeYnhIy8g_kZPfVCVAlq_5nr3WvX3Vz9TBTtBwEVPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=MISUiV2uOdgij6ifU3RrDc1SNO5eS074EApzJyvmpxhaYqxoLRj6nSfRI75nuDz6LrYnpIB1hKuTJpn4TLXHTzp-ooHZS-0vtEOTEfFNBS84B9Npe8lAZyjkKCvw3KCAuCUcOjsORNKQGyhTQCCQiruUo5EBES_b-dkKvxGNzqma8-8ErfAkRiNJmJXQminSwHrm1zDV6BZIANhuwI5Vjzzv5fH85uKv_3yJTKUTt64wyPfj1irE3LOOkOy-qD35c1nxhApNuAhn_8REK3iNPyg1IX4hzxGn2lqUxl5bQ2AyTeYnhIy8g_kZPfVCVAlq_5nr3WvX3Vz9TBTtBwEVPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آهنگی‌که وقتی شاگردان قلعه نویی بعد حذف از جام‌جهانی به ایران برگشتن باید براشون بخونند:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24609" target="_blank">📅 15:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24608">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsgE-wNXvrqdrrGglP5HJGDsGnQjRP_JSvxLBt-vsbZ0tQAc_vKKth86js9p77Zd382cLL-qOOgq-AL4-fcUTnWoCXoLTm1CC83UMNrOsAMV-xvuSZInCjcQSXdZKeh6wc1fJQsUj75PX7YnQS1Eviu4RwODvXT7iuaugW-hGMO5WaFRQndwaS8nQmzbf47ALzywjYEIKqM3hPrtuE6eufFTOlx_KJPDKcZUCij7YTa5CgIma31hwCwSdTgtH_5_rZvDCOq9v2ge7DENFPMF729JyY_sns5lQThMqlRRreqwotoTFA7lwL2I2JHkB-WbaGBR-VdPUqHtspwpz8hJEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24608" target="_blank">📅 15:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24606">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MddsNh2sEOH0vdKzbmSSMaZx80vHbOgbEUHXUDNW11xsdWyXXEhwflYwEpQKGNVJH9430el7vmPWHjfot-ZwdQqsFk5ojR6Z51i3VTbR08CLC1_ovsxAFVbLNkhKaOkTS0AxysPOQS3zYLViVG9o7n73gnJm-jCqpS8A6IozrjPvbPOTRi8dby8wvt3WkjQs6YmviHxMArEq-OjDaLC4auvlBkzN7Or8nmgIuoxBQhkDvn1HfbCoX_F8qmEE9KYcwXh_FocKRC0i23SRHuPbagUQhLcvJrgdk-5t4V0LGpjj8j4nvgOvYRkAMhzbW-yud_3Ca7uVoG3ZRZxOYFFYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jq0VTFoECNXEbis7TY3bJOCtCivRQJ5ruoiknDTWzSPqly1U7b4c5KKeZB-pf0SvvAHmm6kO4O94vOG4UdWKPBcMI47f2ExXO6k0AW0xbCD1_j3BAwiIGwF-jtnBalaai1DT9Ug0B3rndsDPFQjPVWO3IoqCO8Be3NmNkr9keaCParpOEHCyK8oKMjfd_pDIbxhH49SJ3BRtMMGuOru0C95lNEj_DRuq94PCeTHZaVod_diJ5w-d1JC1UVCX0BjkapVBBvLk9DLEV4lpGKLI7pl2T11hbDPTFMm6gf4Ea4d75033Vzf-0wTak7hJS714FB9WQka7BO3pDHCR9DY1jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور کاپیتان دوم تیم ملی برزیل: وینیسیوس فوق‌ستاره جام جهانیه و مطمئن هستم که میتونه ما رو به قهرمانی این رقابت‌ها برسونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24606" target="_blank">📅 14:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24605">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuL-kODfQbarcQZlF1IZ4_uUSKkT_mlRJU--q3DsOyMWtMfDnZG0Y3pAZqhZ9lEAYpioEKvdb0G2MBJng0JlPTFw6uRx3H94IQgo2HuWmdj2vXJGe538sSbOEwmaqwIHLUR9gslh8hq9gegccfYwj6hSMBcmq2hf8ngzjgDKcER0lLWLzkxvXjzYzRrqP1b6BGy6XBTlk5Ek-oRcyL29utU4ALC73Xlyk0HDGyRPzGzRNo2_X4CSF0GWLCW2APPaXL37rR_-If0RJS59dW_jLKHzhrkeJemx9vzP3vmEkt4ZF1MPBx5rgaPdYdhURnO7BY0ryzW9bvS1C4IiyfzN3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این بلاگر و هوادار تیم ملی اردن در پیجش افشا کرده یکی از بازیکنان متاهل تیم ملی آرژانتین بهش پیشنهاد دوستی و رابطه داده که او رو بلاک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24605" target="_blank">📅 14:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24604">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aosazWtbtfoTm0Wm6XPBYBhzlsl8Lw0C95zHZtifQbfrl7G_29jmgcRv83tmE1UDr-5t-RL7AL4uYQYWyIHjrWizmlhEKIPqQMhtUXUuPHCVIlldfG1jCNoSYkwjq2CufR9iXzodd-anUsAoXZxzSmGzwnxdsAR7t5BDgklfOpL9Vsy4xNMT0byNO9F7c0dgd5CUUzXEv4X7SSW_JPNzeU9y43Mubr94dpDq2Sg87h9PK3PsC1nPIS1zWKzKWzDoyMg9E0nBsNl3X1QgbLTnm-UbcJ--lTMskVRgLxzI4C0HwbUKQB24quHtGzAwrr-uXmNY6U_-bemcZFxnREg3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
مسی باگلش‌‌به اردن حالا ۷۲ گل با کاشته به ثبت رسونده، همون‌تعدادی‌که جونینیو افسانه‌ای داره. لئو به۷ کاشته دیگه نیاز داره تا این رکورد رو هم بشکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24604" target="_blank">📅 14:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24603">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKm0YpSEsO2WVhRmI5pGNZGM7VsrIVTUK0mmwvXWO3-ppoM5ABKPRqSCTiBvFScrkOxLfKriqofDtnoDcUwxCNhKkAp1KbrN1cny2Qr76Ny5BfZLAkEiv9mu4tcxeFCDztpRWIUzTY5L_TGozPDUzojdwuWtmLX64TnSi-VR3ATe557mMiIC4YVGBU1H_kzdiWlbiENtel5Kajr5DU7IUo7WmDZtZKSRVDdBHdAqk7pqCYq3pOMZSBiuHaYqOfKyTkpGVLg8Dn3O0BhZvvd3o2mbe-bRRxtnCjyRBWdwp72Z3pBJQYCEDuFg29qHf4gO7nDqMmzDtlg9HqjBog2ymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24603" target="_blank">📅 13:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24602">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=XShMi59Fd6KILFmAIpAMqc4RSpAd7kd3CbXe_PNQGEUdgeX9pZ6OFLTBQTNLvTz0C4m0Q_LzOZ_lhy0mDu3tpzXhLhhA4ADO0MiRQh9s3I2ImVjdNPPu_7J_1YvmQA6A_7YvRs2Vba7cgsSOZmbrQ8QjFrwdrtmRm6MutHBgbp1w9_0pH5tUH8qkmt3WQsxaynwS5vRQSvAyAYzPSfOyauPTvn9eit2r70zJsbTsqtCNImJNzEkFk5TnaITELbVMVpMfY8do-5PVBQiLhQfKWb1_REobumIvXRpgCSSGtKYlerZso-2jilGyMcp7jvUFBWpPaGKQshJ3eZ6FUTGtZ7WiHghXZLHguYMSCv84LVbl7oi-1GrBfSXcL09eF8YPzIJmcHe-Aevx76tstV5fTBfiu_A3feJFr9wXKHNVjIxSmFkrUVRMSTDGyXVt8nKfq3RJN9uI80GCt5zw-x61Y2ScOS4qbnDre-AfClwUpjV4Ldz_j-ajYYNFBraD93TWaOxVt5OHneF1at3GZtmcTMEvdcuU4p8NhscENfW8FkASNhA8ipGysKSL94Yln-L2s-hDO26UIFu3jJN_iK4Tc_IRAuG2goLoPhhej-5T51uVLv8fA-_WoA541-giIZ280AQ-CQgg4ci9FXN_D4emhLc1qW73ceZ-oh17u6I_Ijw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=XShMi59Fd6KILFmAIpAMqc4RSpAd7kd3CbXe_PNQGEUdgeX9pZ6OFLTBQTNLvTz0C4m0Q_LzOZ_lhy0mDu3tpzXhLhhA4ADO0MiRQh9s3I2ImVjdNPPu_7J_1YvmQA6A_7YvRs2Vba7cgsSOZmbrQ8QjFrwdrtmRm6MutHBgbp1w9_0pH5tUH8qkmt3WQsxaynwS5vRQSvAyAYzPSfOyauPTvn9eit2r70zJsbTsqtCNImJNzEkFk5TnaITELbVMVpMfY8do-5PVBQiLhQfKWb1_REobumIvXRpgCSSGtKYlerZso-2jilGyMcp7jvUFBWpPaGKQshJ3eZ6FUTGtZ7WiHghXZLHguYMSCv84LVbl7oi-1GrBfSXcL09eF8YPzIJmcHe-Aevx76tstV5fTBfiu_A3feJFr9wXKHNVjIxSmFkrUVRMSTDGyXVt8nKfq3RJN9uI80GCt5zw-x61Y2ScOS4qbnDre-AfClwUpjV4Ldz_j-ajYYNFBraD93TWaOxVt5OHneF1at3GZtmcTMEvdcuU4p8NhscENfW8FkASNhA8ipGysKSL94Yln-L2s-hDO26UIFu3jJN_iK4Tc_IRAuG2goLoPhhej-5T51uVLv8fA-_WoA541-giIZ280AQ-CQgg4ci9FXN_D4emhLc1qW73ceZ-oh17u6I_Ijw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24602" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24601">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY0P7RFQlA992qRsOLF1rTRIRxF4G7EgrqtZSVg5RDIFOyPWW5pZ60kMHlZgGzKztpbYPkn-ZA2CDmMNexaEsWHfOWOK1_VCzHwwYl6LcayKP_tp-l_5l64LwP15OwRUL2RMvkI5OQDDm6tdF_gLXJQTIksGhmnXdB0g_b_NAnhuL4DYMXEOaPlNAh2qWthBYDmhIilQPZlwUimnK82G_UKojnEczS-F9fC-h2eTuTZx2xHepQHSDEY69XHkqygDX-09eK2N5HwGxun7lMM0opx7jmUHkVhdUkpb8FYdfWMAzlvZ2c3kdzrMuX8EYknKeDYHmGcygBB195niklttzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24601" target="_blank">📅 13:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24600">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=QNeQ9yhXBzXYWmQa9nSsi2GUOSXku8G-yiuzltvApAYbolArufWzPoB3vSHEamLyOUeEa0V_67Oqwnhwm-M2NZmsNWvYMlMrIpHzMVlC_xyqnBQlKjXB0OgX38yyQgHosncwg4IruiW6oGckXvYP4gmW0ZVVSu0gHzDx88XFB_CsccWNEq5dA-_sgiQvkJCLFWdrHSJi8XGQ_96ye_zlZyuXH095lSIRlLnHg3YEBmSLBYNjy66pgMYnMVrh7AGl_xlFBkrbfeL_aTjw-j1U2RttUZBnRNxfWFU6zS-FUFLTzPzwIpbR17g08z_sd5-zgFpnFwwP5Ucd0pqkZAs39Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=QNeQ9yhXBzXYWmQa9nSsi2GUOSXku8G-yiuzltvApAYbolArufWzPoB3vSHEamLyOUeEa0V_67Oqwnhwm-M2NZmsNWvYMlMrIpHzMVlC_xyqnBQlKjXB0OgX38yyQgHosncwg4IruiW6oGckXvYP4gmW0ZVVSu0gHzDx88XFB_CsccWNEq5dA-_sgiQvkJCLFWdrHSJi8XGQ_96ye_zlZyuXH095lSIRlLnHg3YEBmSLBYNjy66pgMYnMVrh7AGl_xlFBkrbfeL_aTjw-j1U2RttUZBnRNxfWFU6zS-FUFLTzPzwIpbR17g08z_sd5-zgFpnFwwP5Ucd0pqkZAs39Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌مناسبت‌دیدارحساس امشب؛
24 سال پیش، فوتبالیست‌ها رؤیایی را به‌تصویرکشید که میلیون‌ها نفر باآن‌بزرگ‌شدند؛ نبرد دو تیم ژاپن و برزیل، جایی که هیچ چیزی غیرممکن نبود. «رویای ژاپنی» فقط یک مسابقه نبود؛ یادآوری این بود که با باور، حتی بزرگ‌ترین غول‌های فوتبال هم شکست‌دادنی‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24600" target="_blank">📅 12:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24599">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-vOQLfa2NV_57VLOE6zjrl-mOA410LbgqHXrEnT-OnVvngAKU1KtTmzeE9gAhKvvhDmCYL7qAS-nXLWculiMXQvfqDh52DDhVJfBp0sY3m3w4r7t_qP3D34aAZnLzUEY41Z6IPTlTP2upcn30Hko9p1zSLD7QjFbgfxKY6nlIkPFfrNrhSZ7GOPYI3AYa_L37cuIBv_iW2kWh3onp03IrtErvFwiXMkOBqkPOiAqyciSDTHSrG8N3xQLafD35UhK6Bb-0qluVbWoqPPdw7y9k-QM5pyOpARic9IProjTnt2QlYJwQa25XPNt334H_ffvx5W3fEbfIyd03_IpyceGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه‌فلیکس‌دیاز:فلورنتینو پرز رئیس باشگاه رئال مادرید بعداز فروش نیکو پاز به کومو با رقم 60 میلیون یورو به‌اوقول‌داده در تابستان‌سال‌بعداو رو به رئال مادرید برگردونه تا برای کهکشانی ها بازی کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24599" target="_blank">📅 12:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24598">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiK7KvnkO9h8JvnG_9WlCDnhjlPNThvaS259UBkc6ijDxEtzSNL_69ryBwmmLVKPL4YpZtusSat0ZBTP47-Ms0bPopOU-oNdQculO_qI3OKkkKe2eqiDZs6JzKnFrwKFki9cXXtq5WYasAlN0Kzt0k_NBa_TLRZjGkD2q92EtCVZlUjGZbKCGBaIBf2P0Q-ahLZXbhBwNBoWL86FjwVUDxf1a-pu8H5e_Uvo-5OPFvOX6gNpWxltuyHOdIDAiMCDbaZkoLJlZ9Ep0U67oPdf5C86Tga-PWpi0LqWb6z_WcirvMGWu4SsBOULyQfQOtTg-QE9DpqaGBFFIFWPRKnt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جالبه‌بدونید؛
پدرو همچنان‌تنهابازیکن تاریخه که لیگ قهرمانان اروپا، لیگ اروپا، سوپرجام اروپا، جام باشگاه‌های جهان، یورو و جام جهانی را فتح کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24598" target="_blank">📅 12:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24597">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJmgk6OcI-xWzVfyeL-cP43PlyvTiRhcn-JbMNAL5Cq1ohoVJ20ko3LQa5N1QGgBpx_ybLVI-Z3iX6OSh7mx5F9s0ny07oFoHaJZHSCOH7ZZknHbozGkPPQeaHQicacVs2fKCH9aRRvdmo0ZpwKM885RiI9Eja0c5oMqHMYdtsel_InTHIblNyabnHgACgMBUMUKf2CzBkFJ_h5OkPqI0mtJxc14LW9cyR-I2HcunSgnM1fqIUERK1LRKiAvtaTuYuC1UPWlFzwKkeo-h8niI5zbgfwI0ZNlQQWfMZHWc1Ks-oJtOWJavwjK__ITdjsHnR2Bkkajqi1w_aIM4J_OGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا
#فوری
؛
طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24597" target="_blank">📅 11:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24595">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feV_9VrPjp7ZfZe4N3wi8nUzuud6kYkUw1bbsgEivndunwNgZ6ZL_d86dosKVZYkYifdi-ppAE_vTT5bDYtVkwhb7T4cNm3R0kweWyMgpCdO5sMzo4iecXlDD3-x8a4LceK0uGvJ_mYQICI0vfqnflxZrXfdHJxtDg1NXaUOxjzQGjDVcU2h27WWwOR2Q0QrLqpI6ZKgvN8GViPixElHNfhHPyLTh8SdNQx9HQITzRHZNDhvAbBOiQV87KvNp4L-GcwOfm3WN30t_9HWyKumiF5X9lCba6YFtPg8l9dp8S3LIiSHmIrlFm28GhOzL1UcAvHJQcYvp_YsLg95ePqvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛ تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24595" target="_blank">📅 11:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24594">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYqkxGX_T8Y00gKpPzVnPvLCw6WbXEJepnN4xjm5SeAH1WV_Qlu9tQ5X781gucXpAWWKyQTV4irs5ydN7w8gDQaQZXuU6kR39SYvLfXWfyZq3fDUPErZr5HWDBLhnfqVhQYskzvNs5wjIi6KlP5Q97PBGnYddYGaftzbMc2SC1C6mlJ0HoNT7E957acma7aEotRK6INXXpPuuAN9ShtKpgm85PEvUUoli1LbfmHh7N1SLbQ0thGUjLjGA4L7iBkznK1WCD1-OG7-xqxC10aBUFUuy31peoXt0xPHBvnZZBI-4GdOVZDcf0g7TQnfMmXhrC4-Eg1xbQ2oNMGEYTSfsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24594" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24593">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TunJFUXE57t6LCY82acsuPtUEnYwA691qlAUCeXymLUU9F1DXKhHVSm9oqi5dS8di7QHBTF99Z6yrjvB8br21pZx6sFOImHlLLfeOOT-A8QE_HEpeiDDKo2m8EnYW8jlgOinH4c38yddW0EHzQg8IdXdAZnJBoHUs-9BSe2m5zHGtb-rYKX3tpCqsKPhoqvdV1SPNEYtn9bb0VzBhLwY-ObQBFjMdJm4mphogo-YgrXYp_o5g6Wx_aEXY5aFGxG3UAcgqRvBVlt8YzbTPUWWVcCvenDXfXfrwEAz_zPg6jkgdzL168KADqPvDuyLeprgTtfhIO-QIn15LEbVuckG4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال در تماس با مدیریت فولاد خوزستان آمادگی‌ خود را برای‌پرداخت‌رضایت نامه یوسف مزرعه وینگر چپ تکنیکی‌این‌تیم اعلام کرده و این بازیکن بزودی با عقد قراردادی چهار ساله به استقلال خواهد پیوست.
🔵
باشگاه‌استقلال پیش‌تر باخود…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24593" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24592">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=NfAZuOJ8B6RppO0-NPjjmtlptH_e9FHohGUKFLKE7iscZw0Vk8QAx8bsq9ZCdXOMBDefQMItfIYIZjYNt_NnLSj6SWP77WX8NYvnOoZdit8lzc9z-zANnAlDgOC4ocd0vUfjzWBH3PDSIaoysgPsi5yuNlzHmlWCt2oyDiqzhH9Qor1r-v9oi5IhOqzs-C3Clmk-Iw__dz630Q0c_bmZlFiuzEvUTJaWv_IeX6WXj3-nV7y9NZLoEVkpBnVIpgXK614MpapBFM_rvNfs9VPgJB-x9aDSPYSEwaeQ91GMESR2UKDEzNsVvJ9CpN53P3AFtkTxlFSkHaP80adtkfHr5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=NfAZuOJ8B6RppO0-NPjjmtlptH_e9FHohGUKFLKE7iscZw0Vk8QAx8bsq9ZCdXOMBDefQMItfIYIZjYNt_NnLSj6SWP77WX8NYvnOoZdit8lzc9z-zANnAlDgOC4ocd0vUfjzWBH3PDSIaoysgPsi5yuNlzHmlWCt2oyDiqzhH9Qor1r-v9oi5IhOqzs-C3Clmk-Iw__dz630Q0c_bmZlFiuzEvUTJaWv_IeX6WXj3-nV7y9NZLoEVkpBnVIpgXK614MpapBFM_rvNfs9VPgJB-x9aDSPYSEwaeQ91GMESR2UKDEzNsVvJ9CpN53P3AFtkTxlFSkHaP80adtkfHr5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24592" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24590">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiL67F9gPNlR5UN7EOtGSG5_vSdYsWmH94nCSP_OZZfH2VRoZ6AYXj1T7NMVEqC5JDosJezwOacN3HwA3ZphmwgQ-zPiv_apj_56PTWK4cXoDKDrDw5UtDDgTcl9ctPtnKsanZ7BxuvNjPMIkt787kKUBl0Zh_KMIKrZgjibttgl3RhQm5rffQVKbaPNLahtQNmFL_0-Fx0bNypNMh2Pjo9FwGcSFdATc6t94CeKGAmnKhFIPtBbB7jxt8tGgtGlPDq_42FgCfK0R-LnTME4cRgwsDA3mfzxCbSRvSx9u0WHVQ76LhZlMVPrpL7qIjdHXwwNUxtfiSPkqq6VTA3d9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24590" target="_blank">📅 10:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24589">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtG8NaRxeSa0Fu9qmzYn6i5jxXdN1HPAVdniQDwwBDQirZjDXZVZs9EaWcjUn_Fer8e91EptuinZY_UNjmgs7PkVOlRPyI1cxhlbEM3R_CrWJJiGkXTYk3RV6VMLRuoYZ040KTeFp4btu4Tj5Z_VFhyI-WOt3zB9jXjO9b5zYY_wMBMeRNiRDFsbneYiAVuyxVHE2DjQ3bgIKVfgxy6uEZjy9eIVEOMtRtoNJ9hGrkRbg1dG26cZLxBdJMECywLLJ4glet0VcS8Lq0pzbOLCod3bWivOccq7fNBPcYGEwM709-wtEs7EsoWKEduSyXi1rUpb0cQKdj8T_zhJxGliUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24589" target="_blank">📅 10:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24588">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=Pa3r_2BKWgc6dEv9Ikz7Q0u3_kZa-spQxgzfo2UQXe8NCza69BJnML3UREoFe4PatpY7moze4nWbt3LPGc-BX2RIu_pEbTYBEw3qdv36zwmqVO7V4EqHrLmEqOtfrARor1g78WCEI4JeBoYDzizLOfdsw05b3DYvS8LyiEnEznmuME2QrT3QrBxCvC8LlMGHcDdVk7yCt-IyLRglSK2_qpA16ee8-10YRlJ3AQdNDwrfwsYedTGXwGa_vSFjp_Zr-gbNELXnspZMxNzSyiZILsXNkVCZg32SsMjOkAxImdHhiUP6-IJhqkFUZmZOOPxSpK7zA_3cvnxEcT0SVBI81g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=Pa3r_2BKWgc6dEv9Ikz7Q0u3_kZa-spQxgzfo2UQXe8NCza69BJnML3UREoFe4PatpY7moze4nWbt3LPGc-BX2RIu_pEbTYBEw3qdv36zwmqVO7V4EqHrLmEqOtfrARor1g78WCEI4JeBoYDzizLOfdsw05b3DYvS8LyiEnEznmuME2QrT3QrBxCvC8LlMGHcDdVk7yCt-IyLRglSK2_qpA16ee8-10YRlJ3AQdNDwrfwsYedTGXwGa_vSFjp_Zr-gbNELXnspZMxNzSyiZILsXNkVCZg32SsMjOkAxImdHhiUP6-IJhqkFUZmZOOPxSpK7zA_3cvnxEcT0SVBI81g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
صحبت‌های‌رامین‌رضاییان ستاره استقلال در دوره از رقابت‌های جام ملت‌های آسیا و جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24588" target="_blank">📅 10:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24587">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=k3KFa8gfg_jh2yH6yo2q7TWOpOQPOdh6BFUOI8qBAH_ly1iTYac6Tb1HQ7cgSuiP_KRcYwvCkeL6TYyoh7hINVggfrhuQwTvQOgoXeHv8Tybi2lJ0w3xowHMBrMoWgLrZUoFbg3Er3PfAVPrDg0u4dXeN4JEpVt2F6h7zu2OlfKsR34H_tTzMOFGfIOyszqSKZ4WVAYr1GBYHsBH-hg4MgwphuTIUIso2i_VZhysBFhJtv_vpTmDC-UocElzGxQ1NGQlmLp29Ix6prKKnmDV17pnps2-JbvjEF9HN8eFdHqpufR2ejBqSlIHsxIshiz6AHr0w22PyRW-i9AOUl8SBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=k3KFa8gfg_jh2yH6yo2q7TWOpOQPOdh6BFUOI8qBAH_ly1iTYac6Tb1HQ7cgSuiP_KRcYwvCkeL6TYyoh7hINVggfrhuQwTvQOgoXeHv8Tybi2lJ0w3xowHMBrMoWgLrZUoFbg3Er3PfAVPrDg0u4dXeN4JEpVt2F6h7zu2OlfKsR34H_tTzMOFGfIOyszqSKZ4WVAYr1GBYHsBH-hg4MgwphuTIUIso2i_VZhysBFhJtv_vpTmDC-UocElzGxQ1NGQlmLp29Ix6prKKnmDV17pnps2-JbvjEF9HN8eFdHqpufR2ejBqSlIHsxIshiz6AHr0w22PyRW-i9AOUl8SBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ابوطالب‌حسینی درباره بیانیه اخیر جواد خیابانی با زبان عربی برای الجرایری  ها؛ که گفته‌بود تلاس کنید که اتریش رو شکست بدید‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24587" target="_blank">📅 09:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24586">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=kBUfOOABaCQnyTXP6ITTDI_ZomgshFek76Lol5m5uVGb7eRk88rrIWfNwLDA93uEwFX7HAHQpM7cVSWN-2e_liQdFT7gZzRY60nw1-VOcwo3wfjuIG8C3bU5nLEneqeSQSBbagN4SMZecLguVs_Jgt40RtZgkLnjXoOazBbbpRlJ6VQ6Arnd_GIF94l8C94ATYAokBWHyPYjvWcdrvsssEFCymU25dsAcnIovdndtegdQy9sCuRU3ewoZoWGYSiu3W-C61dh3AYfUry1liesMv8Y__OhciQEqyfTw4ny3rr7EzakEIyr61TJ6YhyV5bq1uHgjPekp2SDKli9L2LZ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=kBUfOOABaCQnyTXP6ITTDI_ZomgshFek76Lol5m5uVGb7eRk88rrIWfNwLDA93uEwFX7HAHQpM7cVSWN-2e_liQdFT7gZzRY60nw1-VOcwo3wfjuIG8C3bU5nLEneqeSQSBbagN4SMZecLguVs_Jgt40RtZgkLnjXoOazBbbpRlJ6VQ6Arnd_GIF94l8C94ATYAokBWHyPYjvWcdrvsssEFCymU25dsAcnIovdndtegdQy9sCuRU3ewoZoWGYSiu3W-C61dh3AYfUry1liesMv8Y__OhciQEqyfTw4ny3rr7EzakEIyr61TJ6YhyV5bq1uHgjPekp2SDKli9L2LZ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
فوت پسرتازه متولدشده کودی گاگپو ستاره تیم هلند و باشگاه‌لیورپول درکوران‌مسابقات جام جهانی میتونه بدترین‌خبرممکن‌برای این ستاره هلندی باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24586" target="_blank">📅 09:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24585">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👤
واکنش عادل در ویژه برنامه امشب جام جهانی به حذف شاگردان امیر قلعه نویی از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24585" target="_blank">📅 09:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24584">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MU5RyrwEjgdc84yj5KyJuL3T0fqAx0KxeoJMuCC1rLncMmsSmL-GP5F36xK-BHht9AHGRYCY8Z2620wmh4u88KVCTv7sB9Ddk6bj3ksjnbkYYF8M5D31a4aF0Z7FWEGmSVABYdjMA-Yc44tlVHq5OSGwwQxP-0AVoTh6xaQd7u70JogSOasLFbfXPySAln4ZMkR39sUGgMVJVV7C5s5enkkdR-vvCcmjuEzX8fcDKX4oa5nTPLRYsklnlrgfYe8WQ0Z-Zv28ddZXwYQCDljCXLsZLOh7eE4cEj-UVkERoj7Jn7mV1iTkCUNsHWdG4dBLBxJYqHWwnX3a9sKCdI3Dyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24584" target="_blank">📅 02:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24583">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anUwOuQE8fJ7Y63T-wW5UdycwoFQRWTaR4jwEZ0kQd8CE-XOJcOR1Uo-DLNl15-8nIDYQN-l8TbcNQUEKKbzA_yg2yI0dJGIG8gs2ziYmuxjRYDFpaxfKO68F95pQ_1oF_B4SwkQpERgVONiZaPR18eW-uwgUyoIAAQKdiSOmSnbIe5ad4_dPp4O1u5NeGV20r9p-4NDlbM0VRlcrsXei0xD4yLXmJ7AvY63ZYoBI3Q6vbpfMsvQ34rnRg0pB8p1uDzHv3Ww9V8YIlZ5urtydJtKrj2-XydwgWyi-IKqviDHOHKyH53VgMnBxx2y5eCHNmBlJ5u4HvNFu5vK3to1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان با گلزنی در دیدار امروز با مصر، شمار گل‌های خود درجام‌جهانی را به عدد ۳ رساند و درکنار اسطوره‌فوتبال‌برزیل کافو، به صورت مشترک درصدر گلزن‌ترین مدافعان راست تاریخ جام جهانی قرار گرفت. رامین رضاییان: ۳ گل؛ کافو: ۳ گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24583" target="_blank">📅 02:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24580">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7yTRTV8qMd0DTN48hnmnl9tO9tNvVXPdO6dStyTbt-KMovBqYwhmJHBzNXagofz_T-UWq7yyRMaCA1HMfvuMheFSQkhX3_yWGxVc0kCnm63aRr22ppHx0j7lNZPTaFqRbuCZ7WpaLucHy3861i4ug8Fs6Ewzm4Fldo5puzp5dE0QpnQ-xdmRcrML9zaKxPqcNeH7a8Gc0fjw1KeU41Nyt-_av1UtHx4B_j6cw1rAxi-hx43Mu7iPzPImGn8NvOyPqZTz4Rqp_rw5q9Qohk7_WV2gwOKfr2RqLum6Voy7E2yOkL0juvaxRmpf2Ma1jbw42dpjWvhnwnZH-P38dZLCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دو بازی، 36 سال فاصله، یک اتفاق مشترک!
‼️
سال ۱۹۹۰ دیدار برزیل و اسکاتلند درجام جهانی باوقوع زلزله رودبار و منجیل در همان شب هم‌زمان شد. و حالا، تکرار همان تقابل در دیشب، هم‌زمان با زلزله‌ای بالای ۷ ریشتر در ونزوئلا.  اتفاقی که بیشتر از آن‌که نتیجه‌گیری…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24580" target="_blank">📅 02:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24579">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/td09a3dPT8m4kLgEtAbm66uEIuaXF_Um_jQ21_r1JkI9PZu-TlDnYCrriJF-NPBJQMdrbwBNkp7662pPDkG2yjuzohBpyhu-GWCSi5u4rFpOc8s6eihtBnAidvMai34DbDmE8PhcUIupmfEbW1VdGLg6n3BfZNFfAWq1pzfehe9iC1bvuYkv-CD3q_qdFBgI87WL4V3KIpigo8_ppn08-1GwjzHRq5QphalztOq3OXMpR9ap9n1Xn9OwNPH2O1OYRjd4hra_ZEbKDIasLqIjidmsqhj14a75TZh501MNCZ7UjdeGv4HUKxZLPFc9cnKROBAQViEbjaKwbzTgd5cafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24579" target="_blank">📅 01:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24578">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlyIle1tiwsy8jawE13N8GOettIYYY6uXEu4ZS1tqv4PbVwJvqnM7TkY5AAguqnVOIkdgofZEa_T0_hkW6O9w2i359481jOZcQ0L2s6RjlnWkux5tQL-BCp-xTAYop7PGMhXY3pw0WzIMuvf9TovnstEQTCJ-_dEXxIUxvtPtroVJCR2dV2GfXvVn4E24SBoYDQrZ6P8k8SqWvmbOIPzgaAeZxgg-D1qHLolZ7C3tnmewj--MxLtf2TfzlgXfbc_z2h7I4vcQiLGa5E2RgL660tF_xu0xOsNxDxb5uSPte5v8c3GGL1LxA5kDZG8AAofzaYJ8wEg2Jguu4u1MXUqKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛
تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24578" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24577">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jsytpd_-Igcedj64846J0deVglsUAgO4Yidb3dCjiGmPri0CL8Yv0KNpELV2z8BEIZ_Y4OIuS0n245ayvNWgO1lgjmuvc6RSPOQA5H1oQPjcLHB5bij-W7I5LzU4kk_TEm4zdJP-uNIxGTe2Wgt2Ri53-mQ6zOOMEdNfqfHN-aXvQWPfbjanf9_yRBfSGv5BGzOrs9m7Pu0V6BVME0Ft3lYrtc-GKCgumU4Dja7mqiLnkLoMkFOIc9ayAnQN6dofeaiqRQ6WvWjc-6KWqKYt4RTe2nqmi4S4DWacHvPf-rVXTJG5dP8WzFk7dpqKZu9dPS1BzQdPrYrP58glUrmW3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف بدون گل در جدال کلمبیا - پرتغال تابردآرژانتینی‌ها درشب گلزنی مسی و راهیابی کانادای میزبان بجمع 16 تیم برتر جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24577" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24575">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUovjx2zHf4on-v_yd6E-GqWjxJM0pYuxM2tjrXlROIvCBWYmG8VIhjiYO8wKIQBJCR8xinAtGcFFPb_i2o17Dvv56rWDeBT1-hmVKKeg0BZfsz0zixc5vQWry7P0VjviFlSZwfmuRstlRMKUpbCBfcVk255G9437EEkQu0vh0wmW2hQsuvUJ2eYW1gp-K4EC214Kq1tDbCVuVtUJj4HpEfoOh9Fuj8TqAXPVuDANygCpc7ACp8Oe6nQZHTgBzbXs6DqCNpkHXTSvvM4o1uzGLtemAZmndgwDfVrySOKN2tkQebeQ65dvNaYMp5_R50RdCc8tW3v5Rk0OowMDq6_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24575" target="_blank">📅 00:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24574">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=pZPh7YK6M-KKDUH7S1rGlfJDjHx1CJmn9MwZxtowiAxQLX4LvVV0YTodK1mRaCPGcPQuN4DLlvGk22r3vUuDpj-cKUsERDi447CgS2_R9Xh9VUrp6KQVOBOmeWQwNdjF5jLttWaSj8Mud3cG8T8i2v3oIlQf9hENGK3L3ES1epLsvLU7ZZDeiheHHCoz_omaasg7D3v9wfeh137mtZuNUbxNF57i0pyuA4L6qnSMAxN1oFHLW7E_aXnG3kLk1iCiN3ud83T277DT44Tagb17ZTlEmZld4TjfGSC-2BCMRh1_TtLY2HcQuOMtDNGFZy9EIyiP9cQoUleJo1mYTFXPzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=pZPh7YK6M-KKDUH7S1rGlfJDjHx1CJmn9MwZxtowiAxQLX4LvVV0YTodK1mRaCPGcPQuN4DLlvGk22r3vUuDpj-cKUsERDi447CgS2_R9Xh9VUrp6KQVOBOmeWQwNdjF5jLttWaSj8Mud3cG8T8i2v3oIlQf9hENGK3L3ES1epLsvLU7ZZDeiheHHCoz_omaasg7D3v9wfeh137mtZuNUbxNF57i0pyuA4L6qnSMAxN1oFHLW7E_aXnG3kLk1iCiN3ud83T277DT44Tagb17ZTlEmZld4TjfGSC-2BCMRh1_TtLY2HcQuOMtDNGFZy9EIyiP9cQoUleJo1mYTFXPzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیابانی‌این‌بارگیرداد به تتو روی‌دست امید نورافکن میگه حالا که‌اسم بابات‌علی اسم مامانت چیه
🗿
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24574" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24573">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iza2FTZryLSQTlkymtCh1mJMhDoBXmDfZoa2Ejx4b7guEp2d2Klu5cB5BhdKVXkEFbfozq6GgR_DkSPDV5zzSN0fez-Rbi24FgR29jE6hu1EgqsoOyJMj5Wi_vP3aH_5PhxGbZcd9L3x6Lc0qikA1_-177BnOdmqAxc5NtVK_xisN2u0pzqnUX1feOOd3_AxZ-z-UiwrDe0HRov_BK418mHXmwpR2cCn07GH89gaCHrMmuNTxy7IvYXSSau_j3jmtSmPRIQXSDU3tRY0eH4T-tw0bamTQJPgGTrG7j3p0LSxtA_eeKBf0fbjzbrhS1WYKVqYGCWKvDDR4cgrtYew1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
👤
#اختصاصی_پرشیانا #فوری؛ مشاور محمدرضا زنوزی مالک باشگاه تراکتور که در نقل و انتقالات اختیار تام گرفته با باشگاه اتحاد کلبا وارد مذاکره شده تابرای‌گرفتن رضایت نامه محمد مهدی محبی ستاره ملی‌پوش‌کلبایی‌هابه‌توافق برسد و این وینگر 26 ساله‌باقراردادی 3 ساله…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24573" target="_blank">📅 00:13 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
