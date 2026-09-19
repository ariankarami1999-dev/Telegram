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
<img src="https://cdn5.telesco.pe/file/AtBtclqpxnk9Jj6d9e8QzZgQw-PQJlCREz1-OwRiiOvCDHa-2LUGGqXei-vdfZex3Vh2cS0-OMDW-zmZUSU50UwFKw7QH4Z3gbmU_Vcd4HlIbRaGgUWUd-LBCBaEb5vws9F0Xb1kaQ5HRM5eTukJI-hXaJLlrsjij6Pting6lTd36gPLQxqjZqVPJgdDSif7LGZFzUKm_-pXZxU9jiVqE4KygDK1Wtz6ObfPk6W5oZOf1HR-eCF-o8Z__gT0aow8t8S1BgSYS40BPh-oc1trTDip2_5-nypjiWjUnPHwlgMEEXytjGkxA6Zh-gOCdzAoKxrZrF0T1Q1vX-kkePxw_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 408K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 15:29:19</div>
<hr>

<div class="tg-post" id="msg-106865">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHPHGaeWRNgUSWAyTgWVILn1osuqoC-0keDsvFa3sqnecLluOi28vva9TXw2DP1UZr_DuPgZq-PftdrHy5YUPJKoLZ4bm0BRX6gy1CJK5UL2P2mtFfvfW6-88x0r_WWshMsqmsqEtIzMr8OcmNgd_jsU5JGfsR5o_PdcIi0JFy8SoGlEzlascIiq41MRfOxRvARJSErv9_AvhWJLsMMA_YZWlJOnr5r21hhpSUypcPvLo5XUaOpznTDqISS4ktKoago5NB2i51uWg1FsYDjs-TYgpitAazUnL0vz465mYeAqkT8aUZbD5t-bDWgfRKAk67POqanS64gSh2bCre-0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
لیست‌تیم‌ملی آلبانی برای فیفادی بدون حضور یاسر‌آسانی ستاره تیم‌فوتبال استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/Futball180TV/106865" target="_blank">📅 15:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106864">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed8ff21de.mp4?token=JsqZs4QJv01FUklwntDXsQqqP6Pi8djllh7ikCsSnmVR987aum5KBDKiMosX57-UnCYBzua1Ykj3oLwVBzjj0CxUefPVRLhyPdmSrfDWKnh-vqE7-0onscymQP43cCN0-pqLgt40zeFwwh5mGgr4I_bgaog-L99qM4jVSFQftD_t5mz5ulyChZ6yzDXJQLRbjm252B8lBeGF7eL_jn92stgNXsZUt2lK8zTa5QZEzuvGhYr6LDdh4GVNDYv8hMdUXYNXbqipgN8tijhLv66JEbFQfguEbkGMEx-UFYbD_k1ZEl2l0An10DBfuc1bnthHgxxnruLtwyp4fpZgGbPDrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed8ff21de.mp4?token=JsqZs4QJv01FUklwntDXsQqqP6Pi8djllh7ikCsSnmVR987aum5KBDKiMosX57-UnCYBzua1Ykj3oLwVBzjj0CxUefPVRLhyPdmSrfDWKnh-vqE7-0onscymQP43cCN0-pqLgt40zeFwwh5mGgr4I_bgaog-L99qM4jVSFQftD_t5mz5ulyChZ6yzDXJQLRbjm252B8lBeGF7eL_jn92stgNXsZUt2lK8zTa5QZEzuvGhYr6LDdh4GVNDYv8hMdUXYNXbqipgN8tijhLv66JEbFQfguEbkGMEx-UFYbD_k1ZEl2l0An10DBfuc1bnthHgxxnruLtwyp4fpZgGbPDrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
سوال مهم از هانی رامبد؛ برای رشد پایین تنه حتما باید اسکات بزنیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/106864" target="_blank">📅 14:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106863">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87cfdef19.mp4?token=eVzVOGdLIDcD2EhrIkm1uzLfB-gEPKWnNN2BMmb89QdqkiREMCh0xgdf9vmHlQDaFkHhriGOhIIgIbZsWL-Te9yUnKpY9tGQEvDam9G4ccd93LgrNCPePZle5WraVRsRQQaLACgWd834l3Oxo6PRscYbGy98WqmC6TMWti1rXAr4tH-m-quiDg_ccKcmx8bmh34OG12R7RHcxqCMUfVYdkjCXBZSWZbNutj5iS5vo2Am__lfk4QaWeVJpxFoN5wki_5LQOcyPqA-vGEeWsCwtAao3TaeOsHNOnGgflQmTEQ0-G8OzfLinz2cUA4Cn4iD8OoEgsML2SpRoGREkxteZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87cfdef19.mp4?token=eVzVOGdLIDcD2EhrIkm1uzLfB-gEPKWnNN2BMmb89QdqkiREMCh0xgdf9vmHlQDaFkHhriGOhIIgIbZsWL-Te9yUnKpY9tGQEvDam9G4ccd93LgrNCPePZle5WraVRsRQQaLACgWd834l3Oxo6PRscYbGy98WqmC6TMWti1rXAr4tH-m-quiDg_ccKcmx8bmh34OG12R7RHcxqCMUfVYdkjCXBZSWZbNutj5iS5vo2Am__lfk4QaWeVJpxFoN5wki_5LQOcyPqA-vGEeWsCwtAao3TaeOsHNOnGgflQmTEQ0-G8OzfLinz2cUA4Cn4iD8OoEgsML2SpRoGREkxteZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚑
صحنه دلخراش مصدومیت یک‌بازیکن در هندوراس که پای بازیکن در آستانه قطع شدن رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/Futball180TV/106863" target="_blank">📅 14:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106862">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔥
👍
🇩🇪
شب فوق‌العاده اولیسه در برابر یونیون برلین با سه گل و یک پاس گل و هدیه‌ای از طرف نیمار؛ بایرن مونیخ ۷ - ۰ یونیون برلین⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/Futball180TV/106862" target="_blank">📅 14:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106861">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jb98IiMhRhEYO9w8XD0zMfAYSoeaetukRDV5rNotYM2T3pEjh9zuWtn1ppwrq5_rRvBqejdBQ8owTnQJhUi9s_0t6NMPaq5ISEtQ3F5gqo8zLiJC7QkfX6qtrBFoUgcr0QP-BBOss9oFv7oQsEzBV8wr8Hll78Op8N-gX_Yy7IZIQSqDoH9Cejd9QbeMaXHn5EdxwYNMBBbgeKcwtJEcMBvPEVAJ_W6IuPZ5akaKpNQrIRtEkOVxePZrOwhSJxNcUDShArcGwgtiLFTyh7mAr41y2x6i94l76c-TZt-rfMQMZDb1v9dmv0aSRpULl4BRANLJgcoITI6Cwx2Xw67TSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌پنجم پریمیرلیگ انگلیس: ترکیب تاتنهام مقابل استون‌ویلا؛ ساعت ۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/106861" target="_blank">📅 13:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106860">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3121f63a1.mp4?token=HGp_Pp1fibdfGCgPmz1yGYUzBUhA7_1LshtrB2tTvx3s9k3WKHqrkqbc20Cn2DKwtB1pm_vfeIVWe6C6qZVtsW_b9BLQL9EIlTb22bYuJrVOkwobJHPxY40nbh2BUk8oaeaGEy_Tt0rDhS4PcNzvAPrEwrF54orLkpV_ouQkRv4JhOqy0yxI6-oZtgY-td-3lBhkwUlWS9-TaURwqfD3XcALcG-ebOWyfb9OToGBegLVBQkH1pqoZhGJrQ9noBI6zV8k_2E6dmmDlUjxqDd5l4500WIrDDWqFuutrhlGHOlacEuCsg2C0gpolqcVhGvQgqoA9JaDoTSG8JIMqcAWWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3121f63a1.mp4?token=HGp_Pp1fibdfGCgPmz1yGYUzBUhA7_1LshtrB2tTvx3s9k3WKHqrkqbc20Cn2DKwtB1pm_vfeIVWe6C6qZVtsW_b9BLQL9EIlTb22bYuJrVOkwobJHPxY40nbh2BUk8oaeaGEy_Tt0rDhS4PcNzvAPrEwrF54orLkpV_ouQkRv4JhOqy0yxI6-oZtgY-td-3lBhkwUlWS9-TaURwqfD3XcALcG-ebOWyfb9OToGBegLVBQkH1pqoZhGJrQ9noBI6zV8k_2E6dmmDlUjxqDd5l4500WIrDDWqFuutrhlGHOlacEuCsg2C0gpolqcVhGvQgqoA9JaDoTSG8JIMqcAWWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
▶️
ابوطالب حسینی با این ویدیو اعلام کرد که دیگه تو کار ساخت برنامه فان 360 عادل فردوسی‌پور نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/Futball180TV/106860" target="_blank">📅 13:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106859">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKvwa8ivpPXpVbY88AJvkcbj47Y7QJ5b7brX4gtvqvGGeMFk-XJmC_xzTQQKlCMEJIz-qAN1B7s8LtJJUq3YS9iDDVoq8InkDf8PuXh0eFeq4IoEpD0IuB0hKwPTeIaZiA7Wg_UtnavqZb_QtSQm_6B-WRayjVhSAUs8h0pWJt4ibBkbi2PDpeYE9v0HtQ6oO72-6Abbtson-TtEFQKoCasbSlmxVemKccv6DyaIS8ACLFSYPxRBnsvDzn62W9E08DKc5hiPOYJDNJqqifgO5yz_33f8zNVD6cpeli94dEkKowzxqLJiFYlp_Hizp7rxmlSeB1ZV8U5Ka48Y48Ixqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🏆
رافینیا: بدون‌شک برنده توپ‌طلا باید یامال باشد. او آمار فوق‌العاده‌ای داشته و قهرمان جهان شده. مردم حاضرند برای تماشای فوتبال او هر رقمی را بپردازند و من یکی از آن مردم هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/Futball180TV/106859" target="_blank">📅 13:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106858">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgDR8xNkWVzGegZIJGC1xSiOZ8_5OyVgrEL9qO8taintep_9Sw-9HooujlZFx6Tby7npWJn2fIG14eHFxB1vA35HsxOz9uVSbkYoUbRI1sHSpufUUtLNFRT8PD_VLofcivJtD8jO0keqXzj4Kddhr2BmfZzaDJ8Y5a7iwuMoW9_vKZgpR6h2NeEjJl3L3vFQG6ZGv95ND7H0sRbOWvgfXJd-XuQPyN7-jD1qsvcM-4G2_0Jb19qXZF3XPxybl4H797504UCz3X0Ja8KXB8A4CYTwuAamxGwxTv42OV9SCdyMWihgm9yDkPQKFhIiMyseSRv_I3NKvjb43shbhlcEUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇪🇸
رافینیا
: در ابتدای فصل یک‌پیشنهاد بزرگ از نظر مالی به دستم رسید که مقصد عربستان بود. این پیشنهاد می‌توانست آینده من و نسل‌های آینده خانواده‌ام را به کلی دگرگون کند اما بخاطر عشق و علاقه خودم به بارسلونا به سرعت با پیشنهاد مخالفت کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/106858" target="_blank">📅 13:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106857">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da53ddde15.mp4?token=OplahypIfoXDqiyjHnldgPQ2K282c4FDyi79njPE_en8fOC-aMWk7s7xg0wbZno0ulhlc-SEe27Q1jLGkT3oRuHXZmxUoNz-0zSKGMt2XC-D2fFYKlyViX-6YF51EVMsj38dP8mquevLva6LKGmE24EO2w4iJmH5rJHX4FcyxUbhs9Vwcu30aHOZxUcm9mEJ-CnDcYdDQ_-zeMBJ0oYMVvFxUVyDHwQow02pGnubLKAcStdzKPA7KVEqtmdIxf6vmmf0il7gZp2s_ocNQ-tv7SqB4w1XfgSNL09U64IJgbo8_Uwqk6IsuzL4zS92XZ66NN5pWe3EOmVztUvAIOz7kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da53ddde15.mp4?token=OplahypIfoXDqiyjHnldgPQ2K282c4FDyi79njPE_en8fOC-aMWk7s7xg0wbZno0ulhlc-SEe27Q1jLGkT3oRuHXZmxUoNz-0zSKGMt2XC-D2fFYKlyViX-6YF51EVMsj38dP8mquevLva6LKGmE24EO2w4iJmH5rJHX4FcyxUbhs9Vwcu30aHOZxUcm9mEJ-CnDcYdDQ_-zeMBJ0oYMVvFxUVyDHwQow02pGnubLKAcStdzKPA7KVEqtmdIxf6vmmf0il7gZp2s_ocNQ-tv7SqB4w1XfgSNL09U64IJgbo8_Uwqk6IsuzL4zS92XZ66NN5pWe3EOmVztUvAIOz7kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
رژه کاروان ایران در مراسم افتتاحیه بازی‌های آسیایی ناگویا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/Futball180TV/106857" target="_blank">📅 13:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106856">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVKgWbkMakd6CReFpNjDbgjrJoWrvDeavosu1pC-2qRixd0afg1OgSPJPBDRjEoUMR4oHVeC-Cr_dQ96ES_Txl0kxlva69oWl9weaHfeUvkbcHWCgOLfes0F_5dwUmbPKQ23MpEaN8WHDzNv8lOd9d4tyM4mZyT6LuzJTkC6AsySmWzpJjQDIQB2ySznwcvmPXussUrA9Canlr8seNPrvnJ-2DWFFEHYqJu7WSKSRHWcBPf0x4JxNYkE3eztSnFW2ltn2ZnVwr--a6esu1AEBMttCX-YDIfV8Jw7QxsZBi_YyG2ZKI56rTiXcAfuMSWBkYRUivkbinqoZo-4Hv7dOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
🇪🇸
نتایج مانوئل پلگرینی در تیم رئال بتیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/106856" target="_blank">📅 12:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106855">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAs69U695Gns_B3cg2Q_7AtTty5f7ebIDx9turlQkpdwQ_xEFGQ_AWRA7yWWn8o-s5hl1M05qcPBgKZezzLsjr2ASDqe_-E0b-8th0Bp0kQQGZxYfYTrvQv6nCTPm1M0OhEyeAa4vFlNExxj3yIZA-Hq7f0CkhRoW867dpqgzUXbaAmvaKmhX5eDECXwF_0dzDIncFj3iHoUCCM_h5VvQOJpsr22JmYkhQ4Hepgrr9h9f--v0G4UCy-4qHYhwypFeIvNGbprSZf0pyIdBZN3fc4JwyTEjNBNCqs89yTd6BSXcsPb2MUZ7EzOQX4sZKrpNy5KSu56vzSnVdf7mTZYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
🏆
با برد استقلال مقابل السد جایگاه 5 ام ایران حفظ شد و سه سهمیه مستقیم باقی موند؛ نتایج مسابقات استقلال و تراکتور مقابل تیم های قطری تاثیر زیادی روی حفظ این جایگاه داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/106855" target="_blank">📅 12:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106854">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-sKHmHCUD-mHwY9WeIpcTB6Lovn0Aa-OfI4xSwcgPPrGi5UUwaOY5PoGcN_nZQllioJ6cu-51d8g6G4uVU6qpTbr0jZsTWyyfnaYwZfY0ObXMTFOzI1Ms0SsrLF2vdOsNqjyBVes_82aMKvtxMMwSyPy9uZ_guVZ7hKE8_wEYwS4GxtUW4RWqRnGw3OQ6VaYosR3SQ8j-iZqzo0xa9q46qrkyHkjlvYXOQFbkC2bGSxTsSWpe3s_CtyW85U6xHscf67M8tla012XSgNC3Zy2DvBAnsTZ5PsB0HBWmNIzUtMC4aPkVA-sL6DWPcKjoDbTgcqY8soDR_oWBwNN1pcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇪🇸
لیست‌بارسلونا برای دیدار امشب با سویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/106854" target="_blank">📅 12:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106853">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltOb71cbpBgfgRZcKklx5LSb2jmXDbMc6DvW2l7RkdFwcYKWwDh0n6B7dO-X3wPSRmzaCtuPcZWE5nX3I4J6ddd_0pAQsd2m7LVZ9TEwzH3P_l0JKetsGzwSUzHh5tbSsY0sNN5XAHJsTa03Rwwls0QQGZi1KjeE861RIFv-_TmAcioMJ0XZhfcRzjxrFtgQWl3MLxsEBUtYAkUpn-PV0kAPUr4sjk27GDpDzPffuQAFNZf27Om_nEFQ9OEkA9yiaW_WlKInj2K8oaAtTG1xUIxOnkBD6EgZAYIn1aqlLTstuKe4Jtj6Jt-7Tq-s643bUwz3qMe4-lyRUCasmeaq5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
▶️
مسابقه دوی نیمه ماراتن بانوان که امروز در بوستان ولایت تهران برگزار شد که حجاب شرکت کنندگان بدون محدودیت خاصی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/106853" target="_blank">📅 12:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106852">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106852" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/106852" target="_blank">📅 12:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106851">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOeoGwwEeFcC9lqDf9tBT5zFXoBj3C6IeYdKZt4uDnp83PrQCo5HzQHYrFRt7FBaHmisV208Frp_8DdR595I3QJWifYn5lJUyJJWmK-2JxzA7Jm0LguDW18pfPlCcMZfboGVobjFqaREHvMzz01vf0ydwHjzQkX1hV5ppoHqSWadl0bDcNL1d6tCTcmznCl3TyT3ScMCC0VRB6KYrjisg9q28CJ5cMCNaIz2bSXzGWpwhFZTI_9to9PAwojs36pSjf9LJuBmxqC28P6NwNqzIpcFu8Ci7nbZkafriZ_a2mB18GON9RYNROHCyfGxqE0fWChwXyxDxkW6ij1XID769Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
استون ویلا
🆚
تاتنهام
آرسنال
🆚
برایتون
بارسلونا
🆚
سویا
دورتموند
🆚
اشتوتگارت
اینتر
🆚
رم
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
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/106851" target="_blank">📅 12:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106850">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👍
▶️
🇪🇸
🇪🇸
در دیدار خونگی رئال بتیس برابر ختافه، ۱۱ نفر از مسن‌ترین و باسابقه‌ترین هوادارای رسمی باشگاه، بازیکنا رو موقع ورود به زمین همراهی کردن. این مراسم بخشی از برنامه‌های هفته افراد سالمند بنیاد رئال بتیس بود که با هدف قدردانی از هواداران سالخورده و یادآوری نقش اونها در خانواده بتیس برگزار شد.⁣
از اونجایی که بتیس توی بازه اصلی هفته افراد سالمند، یعنی ۷ تا ۱۳ مهر، بازی خونگی نداشت، باشگاه این مراسم رو زودتر و در دیدار برابر ختافه برگزار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/106850" target="_blank">📅 11:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106849">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPm3iEzbEdMZWYdf7K8lCma1BzYT2CciPzZjcn4u9YqKtk40IpfJBEdS8gANS9yb89_ROA5PeS-5N7QmM1ZbMA_3iFV0fFpZ1wwHBfvhVd8ioiVVDeQWNXRNupVaEWImlZTNnCJPgWszwa4hvvkP08WSn2IUe9lBTJyBjPTL1Qw1PPJpPlE12_qCfpJiGl2SdOsNHxN3Gu0Dvjy1SSlW8unQZIKO4iRjF2YEngo-1r8svi2pNjBFE4gb7umthA6da6JaKlnNkmLnNGnp5Sgeb3K4aMXUffrrmCT4euqjRal-Ll9WWQkduViPI8ztrrgRIJjI4NdJmc8eVzKbsJiSGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
😆
وضعیت سه‌فصل اخیر اندریک در رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/106849" target="_blank">📅 11:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106848">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32f6de555a.mp4?token=IFZCKpgcMA-qHVIKV9UFuyW5DNdIMErKs-dvCUzc9JdojrgtaKsgBsqm9NrgOxPYHeqtmqpFIZP5ylzF6GenPIMD4hkzjCmafzJu_bCdxTmfxQPh8nVlbi8NwIGRdB8tRC4g4kQKERhj2qNuLRzceyx0TVam5XXgdocs1tkPiiijgNtieljTctQSqNFQONLzRIf8qmQxUV3o5MQJ_pSKOfTuq0g7rS2oIosVtDFxwyPAJccKsVRFfl9y_ve1SzOn_cdMICWftgGPpUc5gXzxjGflILCi39N6TB7FnIEFU4qZJs5A_cJFZidcK3HuW8Q_dsF03uzkUNMwgBs_TBemZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32f6de555a.mp4?token=IFZCKpgcMA-qHVIKV9UFuyW5DNdIMErKs-dvCUzc9JdojrgtaKsgBsqm9NrgOxPYHeqtmqpFIZP5ylzF6GenPIMD4hkzjCmafzJu_bCdxTmfxQPh8nVlbi8NwIGRdB8tRC4g4kQKERhj2qNuLRzceyx0TVam5XXgdocs1tkPiiijgNtieljTctQSqNFQONLzRIf8qmQxUV3o5MQJ_pSKOfTuq0g7rS2oIosVtDFxwyPAJccKsVRFfl9y_ve1SzOn_cdMICWftgGPpUc5gXzxjGflILCi39N6TB7FnIEFU4qZJs5A_cJFZidcK3HuW8Q_dsF03uzkUNMwgBs_TBemZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت رئال‌بتیس که خیلی شیک‌ و بی سر و‌صدا خودش رو در جمع تیم‌های برتر لالیگا رسونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/106848" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106847">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7feae8a28.mp4?token=QlA2oM9CZqOdzM_n_-UoOY5_mAlTqeQEMxnpnYKKoY5ZebiLfz44enNKZiJTqywOKNFlhGqoXtZaS8Ng2oRZlclGRpzpIxMs3hKCcQYHNmcKHua0ceIp0jbh7O26lCOrObhihayGsqOrqTEo6MA8w97izdaUGb4JDk6drPC-k36psd2NwK_633Y0l4aNRznZtWCo3yBnd3-e8mLNfPFor4UwXjvK9TfXWnwjdr-EL0hWXUNWSNSZShG3PBdZp7Yflmg1KNlKVFtVl4qhUA5va0iDnZ5sVRn9Jy62vZRA-yb0KHC0VG6J1eXt7ESrrii7kPtyeL_C_W9-yKUxvVxsRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7feae8a28.mp4?token=QlA2oM9CZqOdzM_n_-UoOY5_mAlTqeQEMxnpnYKKoY5ZebiLfz44enNKZiJTqywOKNFlhGqoXtZaS8Ng2oRZlclGRpzpIxMs3hKCcQYHNmcKHua0ceIp0jbh7O26lCOrObhihayGsqOrqTEo6MA8w97izdaUGb4JDk6drPC-k36psd2NwK_633Y0l4aNRznZtWCo3yBnd3-e8mLNfPFor4UwXjvK9TfXWnwjdr-EL0hWXUNWSNSZShG3PBdZp7Yflmg1KNlKVFtVl4qhUA5va0iDnZ5sVRn9Jy62vZRA-yb0KHC0VG6J1eXt7ESrrii7kPtyeL_C_W9-yKUxvVxsRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇸🇦
استادیوم آرامکو عربستان که 2 سال پیش یه زمین بایر بود حالا تبدیل به ورزشگاه لوکسی شده و در مراحل پایانی واسه افتتاح هست...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/106847" target="_blank">📅 10:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106846">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ca24d608.mp4?token=fNhSscCi4MyKNfMFDZtTsnc4LBTAtBqe5G-2vh-d5i9zwKIrLwoFOIvWMFsTZPRjLhYkTulMHEdTlAxc7kCcrqAyN3XvyaaXScRAMYJ3K6OLfMOVsRRW5oBwPJgPut9YLMtQummQKkKb-dE-Nd2y3U0j8eqqq6mQTdGk9CaD85bnj6ZISYJsTciMVDjHfWGEGtuEGdHOghIVdYF_9bEVLq0qc_BAQAWyQg_I_DCi93kA2HC51sXm2n04jmQ4qxmPy-dlLz6GFjOtxlbjI4Z3hYf7DLZ6nCZpg3-kuMA1qzLhus5Ty08w-583FAj507OlBUFHYJRBMNjkAa1SjpJ6sTU2Fz6sZfGRG38X_ZFuOjFASOUDhEpRDFo-4sOHlJ0spTN0K91RemDSh9DUFxvAglG7bpnhzbEI7ZsYeCxsLK-h9rQHcIMnAFIZeRtwIKDqXIqJMb_rCEHEjsFDR0K60_sAdr0asUUnajEMiCC_dwnNwbUsRJIz_HlgzAnsXUdB-BRNVL_x1m3ebJ6uSxz7YooNIS-trGse5jwuZcj8pDc5cr4rJOUOoVDNm-Y1AciIHpRkbS1q9ASdxZqTvJjF_xmCchwmvoBm7UeII92Ky0L98rEK1nJW09ypaTiHJjgBFJUxv7YWAn3NfPie4FQcXlZbry1SpIT2A3I4FLsME9I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ca24d608.mp4?token=fNhSscCi4MyKNfMFDZtTsnc4LBTAtBqe5G-2vh-d5i9zwKIrLwoFOIvWMFsTZPRjLhYkTulMHEdTlAxc7kCcrqAyN3XvyaaXScRAMYJ3K6OLfMOVsRRW5oBwPJgPut9YLMtQummQKkKb-dE-Nd2y3U0j8eqqq6mQTdGk9CaD85bnj6ZISYJsTciMVDjHfWGEGtuEGdHOghIVdYF_9bEVLq0qc_BAQAWyQg_I_DCi93kA2HC51sXm2n04jmQ4qxmPy-dlLz6GFjOtxlbjI4Z3hYf7DLZ6nCZpg3-kuMA1qzLhus5Ty08w-583FAj507OlBUFHYJRBMNjkAa1SjpJ6sTU2Fz6sZfGRG38X_ZFuOjFASOUDhEpRDFo-4sOHlJ0spTN0K91RemDSh9DUFxvAglG7bpnhzbEI7ZsYeCxsLK-h9rQHcIMnAFIZeRtwIKDqXIqJMb_rCEHEjsFDR0K60_sAdr0asUUnajEMiCC_dwnNwbUsRJIz_HlgzAnsXUdB-BRNVL_x1m3ebJ6uSxz7YooNIS-trGse5jwuZcj8pDc5cr4rJOUOoVDNm-Y1AciIHpRkbS1q9ASdxZqTvJjF_xmCchwmvoBm7UeII92Ky0L98rEK1nJW09ypaTiHJjgBFJUxv7YWAn3NfPie4FQcXlZbry1SpIT2A3I4FLsME9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
🇮🇷
آنالیز فنی جالب تراکتور در بازی مقابل شباب الاهلی امارات که باعث شکست نکونام شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/106846" target="_blank">📅 10:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106845">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec418d62cc.mp4?token=RMZgKx47_ifRSgJ5yAmzk_H3Z-kDgPQQw8SRNiq7_BVkCgL_7Wcw6i7irzSR_8uE6ywckm0kKiGltLMT70LR5ArkYakgdPvpfP_jOjQzqEkWdpli009VNoBtHgs7z7adden7CwwyfPsu9llJDnxhPayoZGJ6lZQ_X6mLnXzmVdnAaQmKSY-H96cUosgcUobaxZ3x-m242UtjJfj62Nhp4zkuQe4qBwImhoHfhW8az21iwxT9YlHNo4X8YhrbCnstPQ6LgQr3SWsrECY5fy0gOFK-J7fiblQYFAwGjm75Pl_BBnH5PGiERSA3rXOWVB91_gn4ZYbG5W9XnmaJhWM9Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec418d62cc.mp4?token=RMZgKx47_ifRSgJ5yAmzk_H3Z-kDgPQQw8SRNiq7_BVkCgL_7Wcw6i7irzSR_8uE6ywckm0kKiGltLMT70LR5ArkYakgdPvpfP_jOjQzqEkWdpli009VNoBtHgs7z7adden7CwwyfPsu9llJDnxhPayoZGJ6lZQ_X6mLnXzmVdnAaQmKSY-H96cUosgcUobaxZ3x-m242UtjJfj62Nhp4zkuQe4qBwImhoHfhW8az21iwxT9YlHNo4X8YhrbCnstPQ6LgQr3SWsrECY5fy0gOFK-J7fiblQYFAwGjm75Pl_BBnH5PGiERSA3rXOWVB91_gn4ZYbG5W9XnmaJhWM9Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇪🇸
امباپه: "اگر میتونستم، کریستیانو، زیدان و رونالدو رو به رئال مادرید میاوردم. من فکر می‌کنم آدم کیفیت و مهارتش رو هیچوقت از دست نمیده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106845" target="_blank">📅 09:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106844">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSeg6JXpZiFUvncOx6Twn86k8NO-UuoVk9Xommj8SXqfajr7FjpJ6l2cMsSXhJRbhpireLAgixAOJ9Vq_KDwezAZwqojxX00k3GHqyaB1ZYpU6WdvX0wpNXiKB3RJyrDUkfF1EQHcad8yCO_TrFg5x3AbqmYLLhyktWSnabTRl85cL-OQ3Z-9B_z-qvwSv9y3yWlXhSfYTf-2Zjq3AspXNrBcwU2i-yuWa6-HUthg5pbvTvu49E7ft8RS9BRsFyEHE6U7YtmlXcL0KT2giyYU9SN4vvagaIcceLDvmGcuj24PCrqBwbI2Ynt8U79w3J6frUSFkviA-aykZ1RVSZnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
👀
از عجایب مملکت؛ یک‌نیسان آبی با ۹۵۲ میلیون تومان خلافی بالاخره توقیف شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106844" target="_blank">📅 09:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106843">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32c2ecca4f.mp4?token=HsJv1nXhjlIos5fzeA2crMFH7QOYHtOSd8aZYCeo51ZgjE0q17aXKHrF3AhNGeWsQEA3HM_20LIOee9VMbvZCkWblU6EDNUjzMuOKjn7oUM0nw7XPfUwccT81mBgZgKnBM6HmNHqJI697JvDiRZlSy0ZvEWx4I1n6FQKlwKvhMNcUCLlfvRmpHznxQNxm8UKs3KxllAyVhmU1_aJqiOgv5tGgBlAvh9ete-dB6vkMMEUi2_NP5lTEFcQfbRMgx7xiM3wYwioD0XfCyeoVTEvp8UgHp72AVd7iv9gDbHm3RTMvLZW8dvSbhGSVEG95gbLcm1lvZmoPyaJ6CXtsMwlhrOEo0MRGo69pBdGxPvx729_Vjla3sf3C5KCticxrB5J_t3ivaWA82kt1t3sUhVtL3iZhWojvJ1n9-8KWrMmwtXn79eeV-k7ZRuEErsYgUGhkznkHD_TKO3yWeNqtYelpRiF38HaAiiLlX-YV0ZhesAuph8okXth4i2JgNocud-bEsmzh8K5_yz4Ma9P1PgypC1wuDo_rimwPRM6kJB5oyzpBHG5dg8KNdj1cCo0Jxx0RhBXQNL99ILYBm0YGcjXkCQEYSy0reg87DS9NelSozGJHUy4LvcPGPhBjOT8KWzf2AaJKw91wtQi0JqYNAskYEGpKftSl2yBOi-GilGt_xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32c2ecca4f.mp4?token=HsJv1nXhjlIos5fzeA2crMFH7QOYHtOSd8aZYCeo51ZgjE0q17aXKHrF3AhNGeWsQEA3HM_20LIOee9VMbvZCkWblU6EDNUjzMuOKjn7oUM0nw7XPfUwccT81mBgZgKnBM6HmNHqJI697JvDiRZlSy0ZvEWx4I1n6FQKlwKvhMNcUCLlfvRmpHznxQNxm8UKs3KxllAyVhmU1_aJqiOgv5tGgBlAvh9ete-dB6vkMMEUi2_NP5lTEFcQfbRMgx7xiM3wYwioD0XfCyeoVTEvp8UgHp72AVd7iv9gDbHm3RTMvLZW8dvSbhGSVEG95gbLcm1lvZmoPyaJ6CXtsMwlhrOEo0MRGo69pBdGxPvx729_Vjla3sf3C5KCticxrB5J_t3ivaWA82kt1t3sUhVtL3iZhWojvJ1n9-8KWrMmwtXn79eeV-k7ZRuEErsYgUGhkznkHD_TKO3yWeNqtYelpRiF38HaAiiLlX-YV0ZhesAuph8okXth4i2JgNocud-bEsmzh8K5_yz4Ma9P1PgypC1wuDo_rimwPRM6kJB5oyzpBHG5dg8KNdj1cCo0Jxx0RhBXQNL99ILYBm0YGcjXkCQEYSy0reg87DS9NelSozGJHUy4LvcPGPhBjOT8KWzf2AaJKw91wtQi0JqYNAskYEGpKftSl2yBOi-GilGt_xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
پورن‌استار ایرانی که در ایام‌جنگ اخیر با دختران خوشکل و زیبای اسرائیلی رابطه خشن جنسی برقرار می‌کرد، دست به توبه به درگاه خدا زد
😳
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106843" target="_blank">📅 09:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106842">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s5fGN2inmCjsg6fKLaRLXZFbxWjhtqDs2PeWBfCZk5dVXF-b1P5nbzL_Yon_1TgxZzPLAzvkjo-x6c2x1zIJyH29p0-1H15FMWFfjDDtje5EY12pqIMLso1I91gI25vPmmmGz3wlwmjEgZ5Jibn5PjJtAfFdoTqwxr35NyrLCchtfS04T9rnJeB2_zqUQB30vGYJ0jM20fTaXvFtWYc441KsSQ5IEBS4YZfBF1aYWgZ04WbbmrTqpHKabxLgvVB5_dFQLvq6oYNAxiauXz2uh_dfgR4szEVrrtsKi56rFHubAXyYKel5PBBsO8dBmdgVmIuGUAzp-jr3UtXm5vFvmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔥
فیتیله بعد از ۱۱ سال پخشش رو دوباره از شبکه ماهواره‌ای Fx2، شروع کرد.
هر جمعه ساعت ۱۰ صبح.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106842" target="_blank">📅 08:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106841">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583a7cae1d.mp4?token=G6RzpKdkoB3ui7DPvDTz_RmcqSTQJjGVwtG-VJ1iartmHuqIBsgxF2qTh8oOxDCWk20FkcDfMOqWnnZppUP0tzO1JWV3Stl5q_kJdanvsRsyqKYzxilJyvACeLJ3gqz2r7C0lcNky9WbWhaMEhHjPOHPe5f4KvG8JcozK_X01NyMN4rYIhh4oj5xcHKY0ghl0oavxvuLw3BlK3bIfEZYMrmp2wp4a0l9HVox2iE5d5Y8BAAOYl51O28mP7qFDoSQtfm89pYFLgxDZCosxYRbfv7WNb5u858zH8hgtuXcINzsn4wnJiSpkQitDIuK4UAbsJzyAqmujM8LTBgBEJbqyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583a7cae1d.mp4?token=G6RzpKdkoB3ui7DPvDTz_RmcqSTQJjGVwtG-VJ1iartmHuqIBsgxF2qTh8oOxDCWk20FkcDfMOqWnnZppUP0tzO1JWV3Stl5q_kJdanvsRsyqKYzxilJyvACeLJ3gqz2r7C0lcNky9WbWhaMEhHjPOHPe5f4KvG8JcozK_X01NyMN4rYIhh4oj5xcHKY0ghl0oavxvuLw3BlK3bIfEZYMrmp2wp4a0l9HVox2iE5d5Y8BAAOYl51O28mP7qFDoSQtfm89pYFLgxDZCosxYRbfv7WNb5u858zH8hgtuXcINzsn4wnJiSpkQitDIuK4UAbsJzyAqmujM8LTBgBEJbqyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پاس گل جالب دنیس درگاهی با ضربه سر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106841" target="_blank">📅 08:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106840">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106840" target="_blank">📅 00:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106839">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/106839" target="_blank">📅 00:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106838">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106838" target="_blank">📅 00:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106837">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRbEAC5kXoCvqpWB1qCoes0J2rN4e_HuRoDuajVwvbkUDG9AZzMdWyXuj9ond0bUnklITa_9Fyne-Ia61voi5mLDJTpo1obLwfvmXTwTfE9zvLPJRm-_Ruk0OL4bh_-eqiDJiDO1qoLH-aeHbWL5juWmlXybxuiFKnbxZ5ccaNInes5KuqyRPYe6JS4fAvS-uUhl8m2bnnGF2lb-Pj-P4lYSdtTgnfGLkc-Eoyi8sWlFS_7EOuRcYchgwUH-hjgYFRi1qUYOiusQA2vWAqu3lGx5HSnZksdJF5pYgfvI0yRFm65JkSO0Bp9_8_jn1CEddEImjgsp11YSj-PiELW7NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لامین یامال درباره علاقه‌اش به نیمار:
🔻
همیشه سعی کردم بازیکنی باشم که با خوشحالی بازی می‌کند، و نیمار تجسم واقعی شادی در یک فوتبالیست بود.
🔻
نیمار از آن بازیکن‌هایی بود که فقط با دیدن بازی‌اش لذت می‌بردی. نوع بازی‌اش باعث می‌شد تماشایش سرگرم‌کننده باشد.
🔻
تقریباً تمام دوران کودکی‌ام، صبح که بیدار می‌شدم یک کلیپ از دریبل‌های نیمار می‌دیدم، بعد یک کلیپ از گل‌هایش... او واقعاً بازیکن خاصی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106837" target="_blank">📅 00:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106836">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofRZ52L_Vq8RJe2opxgdFiUmIhkTQRArZr641rPx58miCQzv8sEoNc5hENwYdI8ITf1H3Zll3FTKxz-dA1J6uEUAPNsNUej7cwaAxrwB7Ce2ZpDILrhfOHVfck6gB_dUOKrPYNYcwtSt0SvGADDpaN6_JiL-QXINA6xlFGd9fySaFgLkejonjkW7w19EyyTXrh_1vFYhwbW2un_n4x-6zWiwtaXLRO8P1RuGirBeCKALmEDde-nxoBqboJftlIySbyBZJ-xEPNNaclYyBiVnHc6Rl5e_1Wt-sz9zMpQ7G_Ty7CTr1SiO1rvDibxl3-ez_d4ljhdNfOrUba9jsEYzXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
يحیی‌گل‌محمدی و تیمش دهوک در هفته هشتم لیگ‌عراق مقابل حریفشان به تساوی رسیدند. این ششمین تساوی یحیی و تیمش در لیگ‌عراق بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106836" target="_blank">📅 00:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106835">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gl9jAfSQUaWJ_lOthIyZat1gnTqg0W-5ajlbcmHtD-fopakMPrUWaQAo6i16o2BYjs9dlIVEPCTKdAv8o7BKCNab7D15QRWeo8eGNGc2AkG5ANIpNHwzCxXKojzC_F41sebKiPQhSt4zZz1r_c7EYofQ03UOO34D1LWOsYltWWIdjpFNZ2whbLs38EJypP7X0H9cKrDcULdYqP2wDMbBmvKpdk9OrcODzWXdf2FtnUj9SuJHfKb1iBDa7ewY_vbW6x0MDbR2Jr54MnA7Mllw8K5RVJf8pt5xMiw2PRXJKSqqEhtA9HlKLU6nkq8hem7VPWSZMi19rehOYzjIf08W7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
‼️
لامین‌یامال: تا پارسال پاس گل و دریبل زدن را بیشتر دوست داشتم ، اما الان گل زدن از نظرم بهتره ، گل میزنی و تمام، کارت را انجام دادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106835" target="_blank">📅 00:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106834">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1135acc96f.mp4?token=hficH2fe1yynsgjLOhfIiFVT83g9ObvFTy7Cy5lrt0w-bYcdB_q9oyzpTGcCzvn7EERZ3fo8PhDpIm63WtoCj8ShJXPa7RMPNdSEaYtR2X6ksaTzwEBdwjWmMuBhMmqDlhHrpG8SdIorXEZajCa64qrKM1v_2K3A9ikQLHnpPFCVY8RuKg5RWH3uDcd5ujLKuG-K-I-3RF_gJydwxB1IOVx9GDm8-Bg9br0NpuWYGXU_J8khwHQGcV5gPtp0R33_lmW0LKambHvFls_rqyFe3w5dfyBeDQddO6NkrZZ5DjdCTHviG-MpkviR2lVHe9MMbaGvpvyZiksFJqM7KrVs3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1135acc96f.mp4?token=hficH2fe1yynsgjLOhfIiFVT83g9ObvFTy7Cy5lrt0w-bYcdB_q9oyzpTGcCzvn7EERZ3fo8PhDpIm63WtoCj8ShJXPa7RMPNdSEaYtR2X6ksaTzwEBdwjWmMuBhMmqDlhHrpG8SdIorXEZajCa64qrKM1v_2K3A9ikQLHnpPFCVY8RuKg5RWH3uDcd5ujLKuG-K-I-3RF_gJydwxB1IOVx9GDm8-Bg9br0NpuWYGXU_J8khwHQGcV5gPtp0R33_lmW0LKambHvFls_rqyFe3w5dfyBeDQddO6NkrZZ5DjdCTHviG-MpkviR2lVHe9MMbaGvpvyZiksFJqM7KrVs3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
محمد تقوی، در برنامه هت‌تریک درباره پیروزی استقلال در برابر السد در لیگ نخبگان آسیا گفت: «استقلال نمی‌تواند در لیگ برتر مثل لیگ نخبگان بازی کند، چون نوع بازی تیم‌های ایرانی متفاوت است. دفاع منسجم استقلال اجازه نمی‌داد بازیکنان السد، به راحتی بازی کنند.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106834" target="_blank">📅 00:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106833">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/914fe9902d.mp4?token=k9grUfUNanTxQ60QWbN4xQxkTORrftG57mje8nBjWhGYY1R1oz1G1Lh4ryfuETl-L4sVHuLlKNs3NxH1aiPcXVZsp_bCDPpf0QY0bn8BTDmGDLh2Ug9nca1MYlxH5rfomF0_S7zvP4fac_FhqFE6_Lmv79pc1OBZwGQUiG62D-09RQ9XXkSyHl-IOLKzCMRYghnEnuUPZEO8JT_prEk9QnEqfGZzNHHgarFs5C63wJVwhOI_xZ5tcyHqNDVrzlTOQ81bTsjqKRirxV_Us40grO5fDJ6OLW-Mfhr4o3HnFOa0E5mYpXeaRaQTQE7uWDbQonvVA48EyIiha4uXPqgxog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/914fe9902d.mp4?token=k9grUfUNanTxQ60QWbN4xQxkTORrftG57mje8nBjWhGYY1R1oz1G1Lh4ryfuETl-L4sVHuLlKNs3NxH1aiPcXVZsp_bCDPpf0QY0bn8BTDmGDLh2Ug9nca1MYlxH5rfomF0_S7zvP4fac_FhqFE6_Lmv79pc1OBZwGQUiG62D-09RQ9XXkSyHl-IOLKzCMRYghnEnuUPZEO8JT_prEk9QnEqfGZzNHHgarFs5C63wJVwhOI_xZ5tcyHqNDVrzlTOQ81bTsjqKRirxV_Us40grO5fDJ6OLW-Mfhr4o3HnFOa0E5mYpXeaRaQTQE7uWDbQonvVA48EyIiha4uXPqgxog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
⚽️
گل‌های دیدار بایرن مونیخ - بوینیون برلین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106833" target="_blank">📅 00:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106832">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e28dd692.mp4?token=jk-c50J4DRyQ7M6sNDk6R7fpknoDP-h4ROGJedOSyqNl75EidTIevDAIhXiXtlfw1kGC7WIGLErkRTueR0YEoFs_9hCXf137U0YZBL_TbGNYc-jNsnGVBnGXvfy6xXqBs7j6hJzTpDezTCW8WHmvv0Ye9v6MhgPCz5gtxGnP2o2dF7H-Yi6qzat3LXekpJaVk25h9Z3JvgPjIggFmDCWEZgerv29qsKsSZweSj1D60OZALlJsmMGcYOKGBW_9MS5WceqxFZ07tsjzltmhFlHzIv-SEPTM5cY4bRGT6eKMg6-LjWDM8ZzAx6V0rgcPpD54XQfQr1un-22FNod_YbECg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e28dd692.mp4?token=jk-c50J4DRyQ7M6sNDk6R7fpknoDP-h4ROGJedOSyqNl75EidTIevDAIhXiXtlfw1kGC7WIGLErkRTueR0YEoFs_9hCXf137U0YZBL_TbGNYc-jNsnGVBnGXvfy6xXqBs7j6hJzTpDezTCW8WHmvv0Ye9v6MhgPCz5gtxGnP2o2dF7H-Yi6qzat3LXekpJaVk25h9Z3JvgPjIggFmDCWEZgerv29qsKsSZweSj1D60OZALlJsmMGcYOKGBW_9MS5WceqxFZ07tsjzltmhFlHzIv-SEPTM5cY4bRGT6eKMg6-LjWDM8ZzAx6V0rgcPpD54XQfQr1un-22FNod_YbECg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇩🇪
سوپرگل دیدنی اولیسه مقابل یونیون برلین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106832" target="_blank">📅 22:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106831">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz0U6vJTtl_PxTpZRlGLnDCxwq9kXkOKFDbEaZd_2MDM3rfU4HYHn4tQUGPRZiXmPzune2l_82aK3amz4uKXoYZ-btqWkOO_DGZ7EVQW4KaL19R2KPnghzOZNaFazgcTHed1QGzzZasinpaARgIVpKsh1SMbPJbjAB120rp8CWCDsrg4fC38Ux_ym7h5QDmwCwzEuD-j4lh5MgzTdy_YyPSmJxfWmZgPuNMv8-WYVjc_jToI3RGE8YaJUwNKUW_SqlSI1xY_cGtPMNrafMdcF2hdqgvEKlDbQJlnWfIZXt9n_JiPXk_qbpe0CcgbdCut-u8nxmeDpLoYtVPIEG3L7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
🇪🇸
پس از دو بازی غیبت بدلیل مصدومیت، آلوارز به دیدار یکشنبه مقابل رئال‌مادرید رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106831" target="_blank">📅 22:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106830">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfXfqBC2VOB4ly3KOyK1tcqboRZUKk_KvUmrf71dpMXVZKNUH3_wVMHGDji_k69_uEtImvKIs77jNCBmR60Pthpb-QSZaK4bk4ZfsDavFJVYCdtdVAmAtUItEfiuYT4MU74gsw4at-eQiynuW732eGPoZnh5SHNZcIxvNKTHddKF8Ih6Pp_34Mk6unUun4HmsfRJz4tVqF1SFdlMQDXLAehQ287VrGm7Ad-gULpYTA3hekBjaWDA6zakkUcCMgThTWrAfMLYIA3NxdTd2BxCN8Gibiegl1zS8nE28M4qnBapZIAKsb-4BuBvTwX5igP_aa36HHPI1ON8FmsUDSq3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
داکنز نازون پس از عدم موفقیت در بازگشت به استقلال، راهی النصر لیبی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106830" target="_blank">📅 22:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106829">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3aa9abbc6.mp4?token=f5Z499pxEHCzIb-VL9PqEW72MFlbCtauo71Gmoe481J7J_6-4C66JxbmDLa27D7QXREtWTzATJw92IbXqjk9iuJDKNTf0yn1A9n9e-YA0YxIT9rVYXc-d5bgQjKpPQodH4asM5AMpz9WfPdwK7lR5E36ZGYjL5ECtPScLICJSN0VuaAPtWtnQ7vlNAsHTru5Z2zYocGWE809dC_9RQng_-1MExxIXhNwLqvKk66r0mnZ2sYUaNbw06EMBh0LGESjgwxiGgCfz0WXkSEacm7rA3-g0_5pGieMcKmOSgCasyW-ZOzj02HY1P9L-GCEuo4U8_YZbG94N_pWlU8d1T85Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3aa9abbc6.mp4?token=f5Z499pxEHCzIb-VL9PqEW72MFlbCtauo71Gmoe481J7J_6-4C66JxbmDLa27D7QXREtWTzATJw92IbXqjk9iuJDKNTf0yn1A9n9e-YA0YxIT9rVYXc-d5bgQjKpPQodH4asM5AMpz9WfPdwK7lR5E36ZGYjL5ECtPScLICJSN0VuaAPtWtnQ7vlNAsHTru5Z2zYocGWE809dC_9RQng_-1MExxIXhNwLqvKk66r0mnZ2sYUaNbw06EMBh0LGESjgwxiGgCfz0WXkSEacm7rA3-g0_5pGieMcKmOSgCasyW-ZOzj02HY1P9L-GCEuo4U8_YZbG94N_pWlU8d1T85Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صف‌فروش آیفون ۱۸ در اولین روز فروش رسمی‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106829" target="_blank">📅 22:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106827">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdZBu29iEzGAe1jVv0VT7c14cOSSvtlZpFFQQw7JDYoFryNovBTyE50NyxLxVQUW6Bcu8rFg99lC-jcHRDhnemBjgqEHlCcgsn5wWr-ZBmI8CEfplZ6FQse6MLQPNFwPKTI0QwLKQ7UOUMW-DhX67M21AnX4kzLY2YZMqctni23nSQiYEXwwqElu5tZYlwYJ1vpOsKgeaimwY2WosNliIrA71Q4A9QtGjy5uFmf3xcM2jgXEeGVlNlaEN2PdMBNgduXTdOtxjeL5boR503qfDNX2Aej6V23O9t80lJ1LPkf43F2W2Dakn6w5OobUpLAvQP0F2qWB3OKfQClGSl8ufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/etq-oAnmSrRsazwCpqD6EjWyCGg3tIcWgXyZYkeNnYguAeNE0AJyrj4Zg4cUEEx4QVPkmOwvlSeXFzK3LvuF6I2FMjoz1DJjN4zNVpPlbOxMgNKIzPZQ9dhjO649GDUco4xxyXttISWteHmGMFUCXRaq_3nygtcqcdPNEFXBNyGDfIIkwwzkBCf_1-bba-G3zgD-hFKQuVKgrIbdXLakW-qx0P-khIMlXNTy6ZqgS6_JIh0XpYc_gj-7cl3ZJpVLpjcx8dDhZK0XdkCubMBONa7oXFp0Ahc1e2HsJd2FBZ6qvPjna0ewiq0njPAmDqnx7QsrDjo51c1otsaG2mWasw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🗓
سه سال پیش در چنین روزی
رونالدو برای اولین و آخرین بار اومد ایران و دوتا بازی بعدی النصر تو ایران رو پیچوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106827" target="_blank">📅 21:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106826">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNpL2an3seBKGgsa8SHASLrvYQcWxtMdqIRrq65DeoVLBsjrnrR05B4lAkkwjFlJyYk-9TuAvhXN2qbit8L8vmR3UUGgdllC3Y3szrVePTd4E8zarmAogGbCx1HrhMKlLrmAFUtCLqrDWDN9fDfSPFOPF91aE6XHT1_8kwIVugOcGc4fxuWqvlpntfPJg4F9ePK3im6fDQWwOrDkGunsL-F9PxJabPMyaTP1wfVsr9UcwQ_EdoTV4BuzQowofhIbXmabjme_zKvM7m2ddaX5zMcpjtNsB93ms72Emn5tWefpjbzdVy8nXJDNxvYryUzvozhIIJfrWQtDGevgH23EDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
ترکیب بایرن‌ مونیخ مقابل یونیون برلین | هفته 4 بوندسلیگا 2026/27
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106826" target="_blank">📅 21:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106825">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9ikpv3GROMz4yfNRH5_MM65NSqIAtwJk4HP2bEE4hgX8Ti0zki8RQrFBAddSyQJntQYJ-E3GcPnuR2Nxnb3hSNB0bJ4zgQDPuNLNQmogGgZwcdugTUeXjOy2bjuATnB1Kio20sXN0HTDKUBm1Ele0L3m1JfIQGlEqs6nKFtELEsSqjDLQJOJOck1PL1O1eVi2JPCsAbhak_75ZJ_2tOwYnQ1m9fQ3i2HgqWXIeObAdbXRBVXGSeUt0Lr2VMLaFT5qozOehtbUPfx5JIwI5blbWEecZBQ6UZ5fgROwhUBvjMknmxC760yAV1cxwkph5V2FRMEWh810sTx543vINY7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇹
لیست تیم‌ملی ایتالیا برای فیفادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106825" target="_blank">📅 20:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106824">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa894a6b5.mp4?token=E6u1l4oRfsomWIKClWkLw2SBDRGoC2W-u0MXLkVFdxTvzbnNdAH3WLVmWReF9ZdoOQYkaQxKT-TBXIswn-SWC8gHYRuHWd0Rzd7enJWgQSJMmK__63N_fVyIz0cVLbXXbpXhms0SL6wwtdxTbYnI3iZW5TK8TipOzj7iDO-hctWiXtPyBqtouhWOfgvKCJFvMuim4zgOX-IvuDoCd9e3L944FWqpBXPWNDmZ9Uryh7pl5xc6qIaeR56zYWMOFXFfzIZ-2Pu7Hsg6V_aeqyU0QGSwZ0nud-0gP_tOO-NzkeehecLlZWxEUCqB4csUcJdRiBY_Lao3V2fCudYp65S67Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa894a6b5.mp4?token=E6u1l4oRfsomWIKClWkLw2SBDRGoC2W-u0MXLkVFdxTvzbnNdAH3WLVmWReF9ZdoOQYkaQxKT-TBXIswn-SWC8gHYRuHWd0Rzd7enJWgQSJMmK__63N_fVyIz0cVLbXXbpXhms0SL6wwtdxTbYnI3iZW5TK8TipOzj7iDO-hctWiXtPyBqtouhWOfgvKCJFvMuim4zgOX-IvuDoCd9e3L944FWqpBXPWNDmZ9Uryh7pl5xc6qIaeR56zYWMOFXFfzIZ-2Pu7Hsg6V_aeqyU0QGSwZ0nud-0gP_tOO-NzkeehecLlZWxEUCqB4csUcJdRiBY_Lao3V2fCudYp65S67Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎬
👍
پدرهای عزیز به این‌دیدگاه عقاید جالب علی فروتن حتما گوش بدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106824" target="_blank">📅 20:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106823">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed690df00.mp4?token=oPd6kRKwUQLPDYrfgX-ETSVffpComYCIzgZaQxYarWMo69f7ACeS2z9x1IqhG23cqpY7wW6dJFZ_7-G8hi-eVnwR3-kdyL5D5XP3L_ZpwN9Fg95tIpplXLvslvrrKVoOIWo-ezw7Ze7uRmfpZqvE7dneqwsNjcUjkJ7t7bxhF_Zuwv_fThelEoUandHsGPCh-eL_4uecJUj2QT0FkqAbiipqU49LG4VGYxHOmF3DhQXekdJ9sdR1_G-05DsaohP5iuN9afWAzDPvAizyY8ekynBNQsP_hAZSXoNv6FNeNiAbDj0JgU90ZAhMiyNNZJ_47PNiqCJefQo7EutIvO1gTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed690df00.mp4?token=oPd6kRKwUQLPDYrfgX-ETSVffpComYCIzgZaQxYarWMo69f7ACeS2z9x1IqhG23cqpY7wW6dJFZ_7-G8hi-eVnwR3-kdyL5D5XP3L_ZpwN9Fg95tIpplXLvslvrrKVoOIWo-ezw7Ze7uRmfpZqvE7dneqwsNjcUjkJ7t7bxhF_Zuwv_fThelEoUandHsGPCh-eL_4uecJUj2QT0FkqAbiipqU49LG4VGYxHOmF3DhQXekdJ9sdR1_G-05DsaohP5iuN9afWAzDPvAizyY8ekynBNQsP_hAZSXoNv6FNeNiAbDj0JgU90ZAhMiyNNZJ_47PNiqCJefQo7EutIvO1gTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
مسابقه دوی نیمه ماراتن بانوان که امروز در بوستان ولایت تهران برگزار شد که حجاب شرکت کنندگان بدون محدودیت خاصی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106823" target="_blank">📅 19:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106822">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC320vUAABf0IEFZa6gvCnXZuZwBvima50IbNvTjyrRRtGYve8QBMUHiYPnn-xGN5D7TuxUqpWVTWNls1HcgWMK3ou3zfxnJ0BPcfMIy-W1ahIADbYji6PWh0pupowyr6H5ZjmzUvy9agAqAH8C_1oIwsHS0psDaBM645HHxU9928Uvz1SiSJ8yCRW1DVY4cU5G_tVSRXIU2_gFo9FAUEZPAgTqqdnrBvDn51o_MK1urof-6h8jpRAwVUfUU_SGgehe_bxlRPmINxwWNFK39Nv871lW49XrQQJclsBHyqDZpIjDtjXxv3m3VUigaRBLlWMAvIqV0QSSS8PwxKryHPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇫🇷
لیست تیم‌ملی فرانسه برای فیفادی در اولین حضور زیدان روی نیمکت سرمربیگری خروس‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106822" target="_blank">📅 19:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106821">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69347998c.mp4?token=imf3oRM2XKfR3cRGJf1x650hldwlpTgjDz8HCfTtOBLKdKlzDogU4uMBMlKpGnhId_dh_2lde310UVR4epoHmm4WrM0u__LkLzJhftv_Gn6xzsBJ1rqahxQ_apMieoq7OXP9jwWJCXhHubaHZap7qhYDtlasZfD-Bnh4vLL8J72JHyWgbXpX9IHDQeo1pULcX4Smp-xh9d3NE5tdX8hueIjcofMXUIFM9cTIRA4bJFB3XV5llFIDYCunTEnyXQ__TaetUIVOcbxaadF9q2j0lrdkxjaWWMpHVubjymTNFn3h1g3ARtRIb6ygIhf-_wtkZ8X-7PCfGof9MjtqjO06rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69347998c.mp4?token=imf3oRM2XKfR3cRGJf1x650hldwlpTgjDz8HCfTtOBLKdKlzDogU4uMBMlKpGnhId_dh_2lde310UVR4epoHmm4WrM0u__LkLzJhftv_Gn6xzsBJ1rqahxQ_apMieoq7OXP9jwWJCXhHubaHZap7qhYDtlasZfD-Bnh4vLL8J72JHyWgbXpX9IHDQeo1pULcX4Smp-xh9d3NE5tdX8hueIjcofMXUIFM9cTIRA4bJFB3XV5llFIDYCunTEnyXQ__TaetUIVOcbxaadF9q2j0lrdkxjaWWMpHVubjymTNFn3h1g3ARtRIb6ygIhf-_wtkZ8X-7PCfGof9MjtqjO06rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اولین واکنش امید عالیشاه به فحاشی ناموسی خداداد عزیزی: دچار شرم نیابتی شدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106821" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106820">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854ffbdefd.mp4?token=pqhnkZ7D3e_w9buO1G5YzU_hKv80oOCOySma-pRoMT4suA4rfnxoiXN9GVR-1raIbc0bv8_XYxRi-cMTSBs_o-o7p88jF8g7LiYSYBHXBvCGbor2mQdbAElVRdZoNzecEUVukPPbUJZAIHO5252cApeqhzgr-TEYfXhh7knLrE4uOaQeyeydZbGreAqmDoxpZyt6rCa5kMgCiAbOx3dglE7AjUQC9dihRDoBq8zIkFN2b-_uQr4WnSwxooLv-OrIPgcBJz7hTa28gW8olsHxrlswNV4K5lXPcTdsBKoYV56X6lObYjdWltHgLMQdMYwymLnk5mSoaByulfzwkEyO5IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854ffbdefd.mp4?token=pqhnkZ7D3e_w9buO1G5YzU_hKv80oOCOySma-pRoMT4suA4rfnxoiXN9GVR-1raIbc0bv8_XYxRi-cMTSBs_o-o7p88jF8g7LiYSYBHXBvCGbor2mQdbAElVRdZoNzecEUVukPPbUJZAIHO5252cApeqhzgr-TEYfXhh7knLrE4uOaQeyeydZbGreAqmDoxpZyt6rCa5kMgCiAbOx3dglE7AjUQC9dihRDoBq8zIkFN2b-_uQr4WnSwxooLv-OrIPgcBJz7hTa28gW8olsHxrlswNV4K5lXPcTdsBKoYV56X6lObYjdWltHgLMQdMYwymLnk5mSoaByulfzwkEyO5IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🐐
دیوید بکام: "من هنوزم باورم نمیشه که اونو اینجا تو میامی داریم و داره واسه تیممون بازی می‌کنه. همه ما دلمون می‌خواد لئو تا ابد بازی کنه. هیچ‌کس تو 39 سالگی همچین کاری رو تو این سطح انجام نمیده. پس حقشه که کاندید توپ طلا باشه. به نظر من که باید ببرتش!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106820" target="_blank">📅 19:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106819">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dccf6f34c.mp4?token=MoCf2SmwBiPeQzh6VmpZ4MjyFbMIwPDqP2RROzIjvCjZFCNmtyxgaDzJfvnR7IAO7soYz9x8LFE9mctAu6NYGkhtS8ssj7fgCbKwuQdbJebtlcss0WGBPv-IT70G6f2NulMA1o-6aS8leO82GJerQUyJemIdYS-pIcRrLq7kKfT7rc4ZVlpJF-cNgh_FvPHDdzEofHFM0UjWIQ3TIyxkYbYpT4l6UksEpezFKe-__cL-znZ_DVKJTDJ2QYaqW31a4rUUs26ygG9yhU6wVDo45nQIRxaJYbsSX81AnEUMhzXqgxJ3bP4446m1gw0QkOvu76QLkfGBBtNRJnexR8b9iYNN419cmMaEvzV8_UcOrSBxDvMQRqZlhQbrz3_RpXhgiqGz5VeAAoquGmKnhwCVKFm2RH95Q1QcZGM46EVqDNQlxg9W9xUeWCnDp27f_OKi1YR6Z8wkUXPjY7B-H4grjb6bOnX5OuV2_tR6SaSrGo_TiTUOG2JYAgqYCrkqsOVn2zsOeQWhlOiHx9lLDZ3i2VyLXX8MQYhDt2lcsjgD0tf9ncirhsfj0h_mhm595GV9gyUAj3unHgFOiQQ5ZxWlKlsG_q_DWMbx8F9EbDZIP06JAmfsNqLOe7ky_3L03-BTU2-aI5FoZfunLSYif5MgAhVH1NbN1-eAobmWYLriZ4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dccf6f34c.mp4?token=MoCf2SmwBiPeQzh6VmpZ4MjyFbMIwPDqP2RROzIjvCjZFCNmtyxgaDzJfvnR7IAO7soYz9x8LFE9mctAu6NYGkhtS8ssj7fgCbKwuQdbJebtlcss0WGBPv-IT70G6f2NulMA1o-6aS8leO82GJerQUyJemIdYS-pIcRrLq7kKfT7rc4ZVlpJF-cNgh_FvPHDdzEofHFM0UjWIQ3TIyxkYbYpT4l6UksEpezFKe-__cL-znZ_DVKJTDJ2QYaqW31a4rUUs26ygG9yhU6wVDo45nQIRxaJYbsSX81AnEUMhzXqgxJ3bP4446m1gw0QkOvu76QLkfGBBtNRJnexR8b9iYNN419cmMaEvzV8_UcOrSBxDvMQRqZlhQbrz3_RpXhgiqGz5VeAAoquGmKnhwCVKFm2RH95Q1QcZGM46EVqDNQlxg9W9xUeWCnDp27f_OKi1YR6Z8wkUXPjY7B-H4grjb6bOnX5OuV2_tR6SaSrGo_TiTUOG2JYAgqYCrkqsOVn2zsOeQWhlOiHx9lLDZ3i2VyLXX8MQYhDt2lcsjgD0tf9ncirhsfj0h_mhm595GV9gyUAj3unHgFOiQQ5ZxWlKlsG_q_DWMbx8F9EbDZIP06JAmfsNqLOe7ky_3L03-BTU2-aI5FoZfunLSYif5MgAhVH1NbN1-eAobmWYLriZ4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انزو مارسکا سرمربی سیتیزن‌ها:
🔺
تردید هوادارا پس از رفتن مربیای اسطوره‌ای طبیعیه. این شک و تردیدها برای هوادارای منچستریونایتد و آرسنال هم بعد از رفتن سر الکس و ونگر وجود داشت. برای هوادارای سیتی هم همین مسئله صادقه، چون پپ هم یه مربی معمولی نبود. اونم مثل سر الکس و ونگر، یه اسطوره بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106819" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106818">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106818" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106818" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106817">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPXR_Nme2ou5s9vM2nrxXrngCS_5xqHYozUzOOrM8XlDhUfnepNSMb2mAX2QFoTanEpmWGbuRNfDuiL1PQ73s0ZPo7MSTGsHYV4668Clstj1-DToM_7Rbq0-VMtjJsbFHDuHe-aGWlDHFFOo3RPybETFNsR-cIvAcNfLBc5ggOpNGYGqfRbkGADEuMeaXzrK-V1f8gkrP4Bp3bDQJaXmnVEo_aNM6yvbmOCQHFARwPHhKB8-NXcMITl9U_eNVARakNPtl5i8Tod5fW1n2TX5JPYNu7jvWWliOXjbxLkQM4rYHLFTGChk8Uvr0xwpEge2S394IqH0saPpO8WKjQ3ffA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106817" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106816">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabf7dd06b.mp4?token=QfWpANYdI-S8H8s_lznq9NNy6OCK9BFWm1CMN2_TQZffl9Kt35bypgsjuBGgwXhf8xZ86zw0iaJI-0nKIfJflRpKlkqfLYtedfo5jHurXPgj6fYZgc4t8VKinO90yoXZPOr8voujXJHkrWQ-0JTuouPQ9Cb9UsPEmpUyV-M335oLQB1B9PpHEx88T6ZsQcbg_Mg-e58kr8TXsyR0Vc_QGsge28FL1QGW6yCuBJITkBHPx_FfmgTXw4RwkU7ujdMsS3lUbDpauTUUX8nDCNyLPoSjiNTvk4OKBhP9KDoHSC-smO7UykMt7miL-QAUG2Zxn0rifHt0VhzSbbWoPWXbyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabf7dd06b.mp4?token=QfWpANYdI-S8H8s_lznq9NNy6OCK9BFWm1CMN2_TQZffl9Kt35bypgsjuBGgwXhf8xZ86zw0iaJI-0nKIfJflRpKlkqfLYtedfo5jHurXPgj6fYZgc4t8VKinO90yoXZPOr8voujXJHkrWQ-0JTuouPQ9Cb9UsPEmpUyV-M335oLQB1B9PpHEx88T6ZsQcbg_Mg-e58kr8TXsyR0Vc_QGsge28FL1QGW6yCuBJITkBHPx_FfmgTXw4RwkU7ujdMsS3lUbDpauTUUX8nDCNyLPoSjiNTvk4OKBhP9KDoHSC-smO7UykMt7miL-QAUG2Zxn0rifHt0VhzSbbWoPWXbyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
فرشید اسماعیلی: دلم میخواهد دوباره به استقلال برگردم و دلتنگی شدیدی دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106816" target="_blank">📅 18:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106815">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oO78jWhcTNKGNWc3X0DrZdKEBpY6CJOVYY35gZTXk0Nu_C3KZVTF8zoxlUHL730lbepEJTvObQD8IGW-6B6D55FOfFECB-PVyqRu2kyN24CIydDZkdHRISH6nOu-XuL4vfQda_v0BBTYX3AVZebY5poL5yx91XjNEVtKCRqA5z2Djnmcv3_5ZWSzOGfFZO4JhBM9ApibHSo6q8sAVNwCpcpPcQ5LcB6SGYi8OF2udka31p-dMdVNClAV7vo7GlWxU4oHEtA-IMhy6w7fWZyi4FwlW1Y0Wlj4E6OA1HYH-UwD6PihC57ZT_zzNCgSMpZZJ8CuAYilgazYnLg6CHzYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
لامین یامال: من در تمام افتخاراتم از امباپه پیشی گرفته‌ام. به عنوان بهترین بازیکن جهان، شاید فقط دو نفر باشیم. من فکر می‌کنم که امسال شایسته توپ طلا هستم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106815" target="_blank">📅 17:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106814">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd6e64a79.mp4?token=N_cTgY_dg04aY-hXHY702Yuw0otXwIJXffSL-JhTe3sryauUQuVjDFwOC47pxs7z9njMbw8jtsCE07ds1XUx45wQYkZy7Ke1o6m5-25n2qas7oXdaqJSXTV7-eE7GW1cFsSwKecLK4Xf_gEmK4W-APUsJoS_OvKqQ9vXYlraMDHWqb9qv3787IZJAuAtpSppjknrbthhzg-AzAGNCG1_6cMhgdSkylYlzU5NczAuJSavVqNnKTQxaqBH1jWZY-FyiUCTuc__28IXzKiFFrPUV-fEiPhLNaZU1_zXgV3y9IQPkWUHZ2l7-5RywTAB4F0GWhU4Faqu5ynoBCW7ArDWxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd6e64a79.mp4?token=N_cTgY_dg04aY-hXHY702Yuw0otXwIJXffSL-JhTe3sryauUQuVjDFwOC47pxs7z9njMbw8jtsCE07ds1XUx45wQYkZy7Ke1o6m5-25n2qas7oXdaqJSXTV7-eE7GW1cFsSwKecLK4Xf_gEmK4W-APUsJoS_OvKqQ9vXYlraMDHWqb9qv3787IZJAuAtpSppjknrbthhzg-AzAGNCG1_6cMhgdSkylYlzU5NczAuJSavVqNnKTQxaqBH1jWZY-FyiUCTuc__28IXzKiFFrPUV-fEiPhLNaZU1_zXgV3y9IQPkWUHZ2l7-5RywTAB4F0GWhU4Faqu5ynoBCW7ArDWxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
نظر ژابی‌آلونسو درباره مالکیت جدید چلسی که به یک فرد ایرانی واگذار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106814" target="_blank">📅 17:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106813">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-SCdtcTB8tjQlZM0-xeL8Abr0_FaVeWsIc7M20h7kgGdvikTRG9FwT10NBHu8upzOt6mQuY07eQEs6CwIqiAjNAhcd_TqfM_NkAOUXBvUb8_HskDXmkkMoFg5lJhwnxckJL0GBP9bJiBN8LB37jhrb1WtW5jvvq3CqsG_jxlIYtpz6T3vIUm5txDYEh85m2DcgNK8W6gDutvnvAKJ1I7iCI1YiRF3kit0puVec88T09RDfSy-pKJrsuCM3rygJ6hK3NpyhtzojbPQxMruG2bM6aEA9Zi8NxSGDN8lWafUctM_vraY_El94-6sciITwuAD_mx_3hiZdOKppAEb8jBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رافینیا: می‌خواهم قراردادم را تمدید کنم و دوران حرفه‌ای‌ام را در بارسلونا به پایان برسانم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106813" target="_blank">📅 17:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106812">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac9522ee8.mp4?token=N3nSMtb_59dfBgkJy4nBmAu0aWNL2-QdHojq-eOwA9qeVe4HEuCmuQGNdBwwdEFug6LEDHm_nnJDz5zlX-lAjIv4MHqeNa94vFJowl6UTAqQlyY49PxheaALYisNf6BE2JpzEKntX0B_tIWRoOhhYN6ZEzYooXWS5V0hiqUQBZGQ6Rook2C1x8iggt5N_ZrWP1DhGysmUCkbQ5IiFh9r7Jih5DGDmP01XIl8iUVCH5pzUzhjlqswTIrYaJ6g6tuFfCjeRLuIgmq-rNxXZ-Q8VqFTiU3TtkvAAt_gQOH3aEE3DgO7fkqhEYdXUVOZWzNEt0ck6pmCUEqBEJ4D0vXlNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac9522ee8.mp4?token=N3nSMtb_59dfBgkJy4nBmAu0aWNL2-QdHojq-eOwA9qeVe4HEuCmuQGNdBwwdEFug6LEDHm_nnJDz5zlX-lAjIv4MHqeNa94vFJowl6UTAqQlyY49PxheaALYisNf6BE2JpzEKntX0B_tIWRoOhhYN6ZEzYooXWS5V0hiqUQBZGQ6Rook2C1x8iggt5N_ZrWP1DhGysmUCkbQ5IiFh9r7Jih5DGDmP01XIl8iUVCH5pzUzhjlqswTIrYaJ6g6tuFfCjeRLuIgmq-rNxXZ-Q8VqFTiU3TtkvAAt_gQOH3aEE3DgO7fkqhEYdXUVOZWzNEt0ck6pmCUEqBEJ4D0vXlNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
بابک مرادی بازیکن اسبق آبی‌ها: یک کیلو و ۸۰۰ گرم طلا بخشیدم به استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106812" target="_blank">📅 17:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106811">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45512a16b8.mp4?token=ZV5FotvpgSRx_gkr3IEAewFLeIXcvp4Zi1etkpCiU0BxJU-kR8QxJxjs-UAdhI7lIvZROn4gk7ex_OJQ5Nc3HW4s_7E_GXMLlPMt9JLVW3G2gPLhrIXspyXqt-hdlHJamj7GGUTbjiOVxiArL4zZQ47gNd4gEZEMLhh-QbSMEcuCq_QEiWP0T8WGDAuDY_i3Em0UnIu_8v2u1uzrpysvr7Ewp93rK6LgpBQ7_umiqfo7GpYAG8F2Q83oU28GYtVyKiw6HTtJSlZ6gsHb4TA8yAgIp1-XCLW8S7tPk2W0zGbi9GhSsgHNoJ_qZftqE5-yFma0XvxTMqExLZS_AC9UHIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45512a16b8.mp4?token=ZV5FotvpgSRx_gkr3IEAewFLeIXcvp4Zi1etkpCiU0BxJU-kR8QxJxjs-UAdhI7lIvZROn4gk7ex_OJQ5Nc3HW4s_7E_GXMLlPMt9JLVW3G2gPLhrIXspyXqt-hdlHJamj7GGUTbjiOVxiArL4zZQ47gNd4gEZEMLhh-QbSMEcuCq_QEiWP0T8WGDAuDY_i3Em0UnIu_8v2u1uzrpysvr7Ewp93rK6LgpBQ7_umiqfo7GpYAG8F2Q83oU28GYtVyKiw6HTtJSlZ6gsHb4TA8yAgIp1-XCLW8S7tPk2W0zGbi9GhSsgHNoJ_qZftqE5-yFma0XvxTMqExLZS_AC9UHIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
چرا فیتیله‌ای‌ها دیگه پخش نشد؟! افشاگری عجیب علی فروتن از سکانسی که باعث توقیف برنامه فیتیله‌ای‌ها شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106811" target="_blank">📅 16:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106810">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3_uxCwasajqVzYv3Tw-97AJ-cdO1uaSubLLdqOVui7YXuZcCqnJ4YsJPtFN4Uvd4wVaslVMAmojjqNFaZYiCmmVfDuNPhlWb25AtodCKBbcu7KyQPWnsRY9At-Xfr1kvcBpdluKclodW3VrKn8CbuAjw6CYACr0a9gFMN0v41pIMuGZIbjmCUR0pJVrdQC0L1rRHehKUNc1DlpNMQBYgywx6-2CQY3kHYo-sr6vEdSVWYa01lU4-r4uKLl6vxwK1wNf6VQw1lYTyyXJiKXLy-o_eSl5B2XD2d55gnlG7FlHwOsCaTeEDBVnvKCt_1Api0mq_-aYhSUAeiT7id9BKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
۵ قهرمانی لیونل‌مسی در ۱۱۵ بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106810" target="_blank">📅 16:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106809">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171fd833db.mp4?token=BHEfQ8BzrxX-jCtlVMHhAubzWHT9Xo0rdYKLp2PK8XGGmzyW0T8o85egTKGGgcZ_nNQf8_4PS4Arv4jFLelPvBOVTyBrqGrIgUNSOZ2cLBASRUSFIgQZUdGtvHE19XjS43LsvOJewwCkBUV7eyFdcdX4_dgIuWBwf-ONfrGQqM7f0N6QZZFWztS4oHPOhYOn3zE6EXfFWb7iU31cLv65Su5n2gl64_YeY5_r99T6XT5XbOBa0xl1K1iUetODi6bSpUBmllTJUiVT1hsMZaYvuRmI822Q8eXOxly9P9Sfxk6nvdvA2cFberlYYlMDweoZbnXhteKBPSXoX7RNJZ4zBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171fd833db.mp4?token=BHEfQ8BzrxX-jCtlVMHhAubzWHT9Xo0rdYKLp2PK8XGGmzyW0T8o85egTKGGgcZ_nNQf8_4PS4Arv4jFLelPvBOVTyBrqGrIgUNSOZ2cLBASRUSFIgQZUdGtvHE19XjS43LsvOJewwCkBUV7eyFdcdX4_dgIuWBwf-ONfrGQqM7f0N6QZZFWztS4oHPOhYOn3zE6EXfFWb7iU31cLv65Su5n2gl64_YeY5_r99T6XT5XbOBa0xl1K1iUetODi6bSpUBmllTJUiVT1hsMZaYvuRmI822Q8eXOxly9P9Sfxk6nvdvA2cFberlYYlMDweoZbnXhteKBPSXoX7RNJZ4zBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی نشون داد پَرش و ضربه سر هم خوب بلده.
😮
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106809" target="_blank">📅 15:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106808">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb5c6a4f7.mp4?token=md4DLqpXQvoPGLRXCLscLcIC02o3E9WuygO-eqhCTlW_hInvsVAbiAMuTeeOpbG5f59D--beJYRLV4dOllcXoE4tPuFoKzeTgDnvtyf9cIUDS2kW30SOdF3OHju7YEJeVXmk6TB7iWWC3J9O_ZVNyssYQ1dETiCIQbwNFy7TOtfsBIIaVCjx_NWdZwQ7w1lkq-jBY_b9JdqWWe0Tz1pDaBKzKt4CA4r5laST0BEFbur34LiLmGGDqPprjWi1lTftCNMERKvu0BmGBTYoVAfHd7EIr-5jZduIeUuWR6GGTmOb_7l_hTSPYfu2bgyxLVp2dSJVDEDxgFortAhQkT97aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb5c6a4f7.mp4?token=md4DLqpXQvoPGLRXCLscLcIC02o3E9WuygO-eqhCTlW_hInvsVAbiAMuTeeOpbG5f59D--beJYRLV4dOllcXoE4tPuFoKzeTgDnvtyf9cIUDS2kW30SOdF3OHju7YEJeVXmk6TB7iWWC3J9O_ZVNyssYQ1dETiCIQbwNFy7TOtfsBIIaVCjx_NWdZwQ7w1lkq-jBY_b9JdqWWe0Tz1pDaBKzKt4CA4r5laST0BEFbur34LiLmGGDqPprjWi1lTftCNMERKvu0BmGBTYoVAfHd7EIr-5jZduIeUuWR6GGTmOb_7l_hTSPYfu2bgyxLVp2dSJVDEDxgFortAhQkT97aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
اعتراض تند رسول خطیبی به حمید مطهری و تیمش بعد از باخت لحظه‌آخری فجرسپاسی به فولاد در اهواز
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106808" target="_blank">📅 15:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106807">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSEbyUYukTrdxfaGPGWx-uIO1lwk2o0dzAsSZiJBNrPjPIvKE61uexwBaMr2tbAQUaIjHvFujyrB3SCxtTT5EMgNHgma7GElsLEmtM2kSJM5hq6YyeK6YQ-QfNUP4LmVML4kFUYMj2BUnPylX9y6KvVT2DFzE8ScL8N_s_V-TPPyr7SU-Sbe46f34OADZhjKI-ZzpOHnFFP-f9jQhGK93KzjED2j8Q7EMXkG5YzGkFYoTsyASfipNb1IAtGSw1lMs2uHMtQUTXU5TDswJWANG5V3e_7EtPicG8o3dJnXnWb__Ifl6of6-TL0VLUZvPedhbgarD-cq_lXXmT9asrwSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌐
گزارش هیئت مستقل حقیقت‌یاب سازمان ملل درباره مدرسه میناب: مدرسه یک مکان غیرنظامی بوده و در عین حال این مدرسه در مجاورت یک مجموعه دریایی وابسته به سپاه پاسداران قرار داشت. اطلاعات مربوط به مدرسه در سامانه‌های هدف‌گیری و بانک اهداف آمریکا آپدیت نشده بود. هیئت این حمله را یک حمله کور/تفکیک‌ناپذیر اعلام کرده که موجب مرگ غیرنظامیان شده. بر همین اساس، هیئت آن را جنایت جنگی تحت حقوق بین‌الملل ارزیابی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106807" target="_blank">📅 15:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106806">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40dc07061.mp4?token=ZgUhe16OAdnDf1N4JL39E3YtEw6LJu24jW-DZwiI78ZCjy8nnCE1Ldu8-RNxV5My9lYQBe-CLN5KfeFuNBR-_bQTW0wXfI381AE3M1cV_eiGizymNSnbo9ID_WWpQwaIdPjaFfd_BbaQ8zgxkuaf2s_U37lD5fR-o4_WkXGt6mKFbgRfTeOb2ZKbaIsXxOStvSdcfb1gC7v8ezxkS1Kwbj18bEMUm7EsTS8CihUukeLQBrqZxQtayGC3cWFXGojfP2vM8YPFDvD_fUj_q5VCr6cFnylMA-E3zZih8yiMw6ZzWmlTuU8TScYwMnT3TRGXnf2JaHLSMwJMLyaWd-rulQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40dc07061.mp4?token=ZgUhe16OAdnDf1N4JL39E3YtEw6LJu24jW-DZwiI78ZCjy8nnCE1Ldu8-RNxV5My9lYQBe-CLN5KfeFuNBR-_bQTW0wXfI381AE3M1cV_eiGizymNSnbo9ID_WWpQwaIdPjaFfd_BbaQ8zgxkuaf2s_U37lD5fR-o4_WkXGt6mKFbgRfTeOb2ZKbaIsXxOStvSdcfb1gC7v8ezxkS1Kwbj18bEMUm7EsTS8CihUukeLQBrqZxQtayGC3cWFXGojfP2vM8YPFDvD_fUj_q5VCr6cFnylMA-E3zZih8yiMw6ZzWmlTuU8TScYwMnT3TRGXnf2JaHLSMwJMLyaWd-rulQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
▶️
مهمترین اشتباه در محبوب ترین حرکت بالاسینه؛ به توصیه استاد هانی‌رامبد عزیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106806" target="_blank">📅 14:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106805">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUBVOZyaRGWrClmyJ5SJiCejQUFBT1p3PIScotr22PMwpY8_AvJlRiviSnHphThjmMeaL35Csz7orVR0PNxa5YZ34rir3qeughZLkLUtq6B-c50UmSppjMyLqWMhnHCbAS0Pss-3n5hI1scggsxW7qN-qy6ElMM_ZXSR8dorXfEcjuasoyEINStYMQByzzr2kJgJKMTV574LgBH6ozoouzkZSybxOCjncIJeLA1cKiwCjUYM5noESqhxGm8VXtLsgs19MenPGp2V-UQIVyZX6nqmy6GGxojs62TxFEG6Zs5z_fBdJfP9ZKYm2dCI2SjEOC-akkOimUj8ge6uVMLqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیبو کورتوا درباره برنامه‌هاش برای آینده:
کار من بعد از خداحافظی از فوتبال؟ شاید کار توی بخش مربیگری دروازه‌بانان رئال مادرید و ساخت یک آکادمی درجه‌یک تا به جای خریدن یه تیبو کورتوای دیگه، خودمون یکیو پرورش بدیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106805" target="_blank">📅 14:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106804">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vmwlbk7D4hYKIOh-0D0UnaCRHj2Ecq3cC5wx5LOMp1RLLHjmIjcbczRGNBHkSeAOux3xxn-BVfmpiO-fGx8cFCyg-ZMZI_xuwSxeuMlCOM9epmlpwP5KA2kWGgqMvo_DVKaAldHSv68kWwDrISWP5_yV8JnJUwH_sx9YZmqNdDopCbqEmiajeXhBIEAXKZE1ni2ZT3LXAxprNq0V6GAMjF7OAmOOP1mXqWRbHKBJjGT7lHEN2E-yAsDcAJX6wZS7D49vUGWl8hfOzdIN6HzVcbQUe3YMxsMSL7ZGB-ERlIRZGEcZUwmPkKvRlHg6Uvpdsbi6xhvKeROtn_XCQfLJJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هری کین درباره توپ طلایی:
"من دوست ندارم درباره خودم صحبت کنم... 73 گل، خودشون حرف‌های زیادی برای گفتن دارند."
"این بهترین فصل زندگی من بود، و این تفاوت بزرگی ایجاد می‌کند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106804" target="_blank">📅 14:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106803">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325a2dc7b7.mp4?token=Dg5YcMmcuPI5Veo1pSVI73p021XVUUdjnuP-5wfPWumxmlYTNoMqHmwVtp85mN0B_jT9WATSh1y5VMKE60ikbIL6KX9OcoHUKVK7YEvL97BSV7Ztc5LV6HIKeBNRnasev_DkzXmlmDL5yEimT3821P45Z6bQpDtCA2VXnxw30qNCDbR087zUFD5CmgNYVmpFtt8IJE2gRXrTonqF0CtkVZHK2gxD2ifEk2-JUZaHCuUw_muvz8uy9VK467qNdr21jwc8F7eKia8nArI_Z-CZL0FsyCx2nkyfmo9h7CmgINT764Jp0iROH0e712PdzUM50QWh1WVg5ej85aFsNKS-0ma-wGFVvlZ7gtf3EPoapw6iO5atWsOsOrO9XZq9FbNMpHijkD7Y2b41bD9vqauPp_IQh9eI7SJGw5rP4ZAM2SCCm7TqAs-rBgMjZWZwglwTGkMEC1XiHHQObLrQAsap3Lb1reziz1fbSFQDcgFGxbANvO_HrkQ_H2nuwCdKa8T0Se73votG3PmjtfAYaDNsR23FKHvmj6FVj7H3FpQ7vAeh0KHsNapOXKRkX5USuTyFrbrfvneXfKhnoNByOFC5Yisy4P6PooOkp4rooDhNZMpL-D5BMm8l075hVwBLh9CKt7s6yQ46lfkKJjOQ742--Rw5l4YlkHyTcPuko9AlKnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325a2dc7b7.mp4?token=Dg5YcMmcuPI5Veo1pSVI73p021XVUUdjnuP-5wfPWumxmlYTNoMqHmwVtp85mN0B_jT9WATSh1y5VMKE60ikbIL6KX9OcoHUKVK7YEvL97BSV7Ztc5LV6HIKeBNRnasev_DkzXmlmDL5yEimT3821P45Z6bQpDtCA2VXnxw30qNCDbR087zUFD5CmgNYVmpFtt8IJE2gRXrTonqF0CtkVZHK2gxD2ifEk2-JUZaHCuUw_muvz8uy9VK467qNdr21jwc8F7eKia8nArI_Z-CZL0FsyCx2nkyfmo9h7CmgINT764Jp0iROH0e712PdzUM50QWh1WVg5ej85aFsNKS-0ma-wGFVvlZ7gtf3EPoapw6iO5atWsOsOrO9XZq9FbNMpHijkD7Y2b41bD9vqauPp_IQh9eI7SJGw5rP4ZAM2SCCm7TqAs-rBgMjZWZwglwTGkMEC1XiHHQObLrQAsap3Lb1reziz1fbSFQDcgFGxbANvO_HrkQ_H2nuwCdKa8T0Se73votG3PmjtfAYaDNsR23FKHvmj6FVj7H3FpQ7vAeh0KHsNapOXKRkX5USuTyFrbrfvneXfKhnoNByOFC5Yisy4P6PooOkp4rooDhNZMpL-D5BMm8l075hVwBLh9CKt7s6yQ46lfkKJjOQ742--Rw5l4YlkHyTcPuko9AlKnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تأثیر غیرمستقیم تحصیلات بر فوتبال، از زبان بهترین بازیکن جام جهانی ۲۰۲۶ و برنده توپ طلای ۲۰۲۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106803" target="_blank">📅 14:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106802">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2929cbe0df.mp4?token=jwvsgFMwRX42DsoEGLmb2QSMch1ofqpoFvLKUozsKdBd3uWP91EdTwBWJ9oJ5diss4IL8ncN7nnbFUBBvPyuIEjBFnuhkf5G3a6F_3YHvy4rfD4dluV1nkjfYH0hccHf4L_MAd1iDTTrp7nQ8hRl7AEoy8gfuNRJej6gRdToHLKT6cpjcKNZTY2AuAEgyNOBTqlaxqkcQqPHs5KkJUKnKy98Zzl8Gmg5uecLjG2xDQo0uuvHGK44gDSh8SQg2OHpxWNvA_SuQz_OGZL8l_HZMMHv5BtQT9QemAO8xS2aGpXlUz6aCVZYD2P_OwiWdsPZnn1iglC8ADDRloZfLviG4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2929cbe0df.mp4?token=jwvsgFMwRX42DsoEGLmb2QSMch1ofqpoFvLKUozsKdBd3uWP91EdTwBWJ9oJ5diss4IL8ncN7nnbFUBBvPyuIEjBFnuhkf5G3a6F_3YHvy4rfD4dluV1nkjfYH0hccHf4L_MAd1iDTTrp7nQ8hRl7AEoy8gfuNRJej6gRdToHLKT6cpjcKNZTY2AuAEgyNOBTqlaxqkcQqPHs5KkJUKnKy98Zzl8Gmg5uecLjG2xDQo0uuvHGK44gDSh8SQg2OHpxWNvA_SuQz_OGZL8l_HZMMHv5BtQT9QemAO8xS2aGpXlUz6aCVZYD2P_OwiWdsPZnn1iglC8ADDRloZfLviG4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
زیباترین گل‌های کاندید پوشکاش سال ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106802" target="_blank">📅 13:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106801">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37652c08b0.mp4?token=p7ADfpBd60l-s2wgwwK4XD0iDm8x-pkWG4fHM3w4qCd6j90kqQ_Q3u6O-28gBo8f7H_cAQA44RWQt-gPOZGGJfyqRaPpGhTeezxchl5Jk5OXFLoUPJmwDMFM4tO7iYkA3GUFzlrmpz_4lWHh21Dph08jmHBKH0MgtY25f9AdKhwcNWQWVwrF50UJl5n19ChqE-dD9FUhkUF1z-LYhmUZrXhy8G-ZdNA1-1259puLc1O7BxdIu-jejSsyQ5aq-1IJqFaZjTkdMzvmiu3XX5CoKyzZyamWff-b5Ivj6tiUaVamZ0YBC8hXtaiO5nDzfY7Sg6svWNKrUJTwyInwJnJAN4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37652c08b0.mp4?token=p7ADfpBd60l-s2wgwwK4XD0iDm8x-pkWG4fHM3w4qCd6j90kqQ_Q3u6O-28gBo8f7H_cAQA44RWQt-gPOZGGJfyqRaPpGhTeezxchl5Jk5OXFLoUPJmwDMFM4tO7iYkA3GUFzlrmpz_4lWHh21Dph08jmHBKH0MgtY25f9AdKhwcNWQWVwrF50UJl5n19ChqE-dD9FUhkUF1z-LYhmUZrXhy8G-ZdNA1-1259puLc1O7BxdIu-jejSsyQ5aq-1IJqFaZjTkdMzvmiu3XX5CoKyzZyamWff-b5Ivj6tiUaVamZ0YBC8hXtaiO5nDzfY7Sg6svWNKrUJTwyInwJnJAN4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✔️
توضیحات مجتبی‌پوربخش مجری اسبق تلویزیون درباره افتخارآفرینی کیمیا علیزاده در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106801" target="_blank">📅 13:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106800">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ch-IGWc88r9WKkvWAMUmYRDqtbkKINwTk8g5erkKh6zkdsQspQCaoaDVAjGWrsYt2ZZJQ2mZWMKu3mw3RoSNaEbu2vrJCH016Lkn0t3obUg5aSYI0B88e7bUmCFSmznXkeELVOsrKhaZuuoKZpAqd0xPgl5dXmPHpgBR_HWfruuiqgO8yoBie4kScVLplUR5Q_e7qihNFQ5ByMveB5wFRGhTwSRINDh9hcCjgRHS2UrojdgSh3rNbNjd375zauTxUHqV-_VFeqOM0OOSHUN4LWrxA5dmGTYOxRdK25cR_wXGQrgN9bBOHPD9R6-luym-vqcJQq8AOzzUvuOhOWHSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
لیست تیم‌ملی انگلیس برای فیفادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106800" target="_blank">📅 13:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106799">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‼️
🎙
صحبت‌های عجیب و‌ دردناک مهدوی‌کیا از دخالت خانواده‌ها در مسیر رشد استعدادها!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106799" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106798">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106798" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106798" target="_blank">📅 12:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106797">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-Xj00uC_PQklYVDxTw-B-3pnLpktKAUKVJtnykIn3j23ld123EvvbzKivIQXP4FTYJvso4cnN-ib5-Bx2WdLnHIkrF1wwPlDPOBm4o_HJ0odGXtBMSj4S5cbyU4oztAoW8UMru8Pissf0ZKq93FRvzgdnN95-F0GkhqcX3BLHb_B6nehz5XG6kXTfExIrNk3pzMh8JfVN2Uqd12miff3L0MEIuvHEF_07d7l-r68Tc75e3ujRBXuI_qsL2i00yg0h9RqmWtGUEwJzQmmk88V3jlaFXX78hofviSK-3lwEaPSFglJGPLpw9tpyfhsRzSrw9ZnTVt5Wb5hmPZuSsDDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
چلسی
🆚
برنتفورد
انیون برلین
🆚
بایرن مونیخ
لنس
🆚
موناکو
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106797" target="_blank">📅 12:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106796">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKqoi0b09SM0ynp7URB1IWdKlvpPc3hS0-RxtuRmMoEk3pRyeSdeTa0an2cDUG021kp9zIT9ASpBM5AfqADTJR-g03gwJDYWAQ4Un8K-sU3Swhwf9uJZgRpvpmFGwFOB59TxCKDXmFF10dGLZK_qDqaIm12Cu67AsVO1sBCo1ljVS0t_8lvJ6kEY23-sVIYda7QnkmldIJ0schDBVyOPwo3i9RNwtq6bsjRbDUkT5lRk3M5gLm3AD6-fQuHYc6cY8UFBhCnBwlOfM--Ops9MMbqwXetCmNg4fhh8IELgQHNjDLoeeTQJ7QkyK1rVUSViA-E0m7hYmCx0k5lygfHaVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
رافینیا، با هت‌تریک خود مقابل راسینگ، در 7 بازی اول فصل 2026/27، به 14 گل و پاس گل رسید و رکورد بهترین شروع فصل لیونل مسی در باشگاه بارسلونا را شکست. مسی در 11 بازی مشابه، 11 گل و پاس گل به ثمر رسانده بود (فصل 2012/13).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106796" target="_blank">📅 12:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106795">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f364f9a06a.mp4?token=Pz4gLOCRDfOnyDK1mAjAUVcOPt0VUCxyQRhvx0obDbPjvDkwMGLaUUpyhU2KGLZoq9Zt0e2EXuG0gV_i58TN3CrF7PR-dj2sqUzfJMwkVWgzu1dDozX5w29xpAEx5GfHwXayHzzV0O9DbX0q_z6IjiSGh7wJxSceNhSDvO5wqDc_zyNO6kVImChwZw62nR3J7IKxzaRWyv6hqUFv1OqrUzFAZ3g0pa1SkZeezc2YASTAlCpo3VBuu_HzyTzGGZNPTjBiuDAdWM6UMPUphCygn5Wi7H18eRQZMTktgLapK0DJI1gMoxWbBr1MzI1HzbmYU-Afuf-IKHi16tpBjWLGoidnz9kUfop4c6k-RwCEYcOQ1NdqJnbHX0NV0HF9SHLj2uQ0wEpbkdjVkEH-qQEugCWTwGeiJQtcv-ss2IPvob5Xtf6DBtN924Kp5Bzd4Y-utapxh0cs2JS0TD5Tqmdy_sS78osWHrejFEHRygZugTM15QBSgUz2b6ZtA0eRnma7ofqvKDJVFz6JadIfe8FnAPtuAgenOdDz6MDkekNp71fFnzp7JHXDtH1MjrNctGuSIjbM-Kp0bCuDF5YKKR2Y0cJEbL2IipVWerg8Web05k993wKPhCHFFk17QbN5tFCDHK2bHm7E40PGLk1w3TFdn9EGgG_o2uhYknQE_a3rkMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f364f9a06a.mp4?token=Pz4gLOCRDfOnyDK1mAjAUVcOPt0VUCxyQRhvx0obDbPjvDkwMGLaUUpyhU2KGLZoq9Zt0e2EXuG0gV_i58TN3CrF7PR-dj2sqUzfJMwkVWgzu1dDozX5w29xpAEx5GfHwXayHzzV0O9DbX0q_z6IjiSGh7wJxSceNhSDvO5wqDc_zyNO6kVImChwZw62nR3J7IKxzaRWyv6hqUFv1OqrUzFAZ3g0pa1SkZeezc2YASTAlCpo3VBuu_HzyTzGGZNPTjBiuDAdWM6UMPUphCygn5Wi7H18eRQZMTktgLapK0DJI1gMoxWbBr1MzI1HzbmYU-Afuf-IKHi16tpBjWLGoidnz9kUfop4c6k-RwCEYcOQ1NdqJnbHX0NV0HF9SHLj2uQ0wEpbkdjVkEH-qQEugCWTwGeiJQtcv-ss2IPvob5Xtf6DBtN924Kp5Bzd4Y-utapxh0cs2JS0TD5Tqmdy_sS78osWHrejFEHRygZugTM15QBSgUz2b6ZtA0eRnma7ofqvKDJVFz6JadIfe8FnAPtuAgenOdDz6MDkekNp71fFnzp7JHXDtH1MjrNctGuSIjbM-Kp0bCuDF5YKKR2Y0cJEbL2IipVWerg8Web05k993wKPhCHFFk17QbN5tFCDHK2bHm7E40PGLk1w3TFdn9EGgG_o2uhYknQE_a3rkMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
فرزانه جمامی، سرمربی پیشین بسکتبال زنان استقلال: تمام اعضای خانواده‌ام بجز من طرفدار تیم پرسپولیس بودند و هنگام دربی اذیت میشدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106795" target="_blank">📅 11:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106794">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuH1G7NhzT-Lu68RrkJZlbTps-FjVb30g-iRrwz6OLWpoy25jcyvlP7BRxKiBkKtPODxCi6mQcMdvyyHpT9AIu8AXx_VaykaW_8REktuJ7rpCYOjYmsEU5UWgCoCv6Dvt-ak8AFYklPtq-prVNwrXrsGZ5sxjCwL0tAoLx6OjxbPT7I7Wy9iFNRRGOI84hOgOCqYx1ZevxZjyRDRbCo1EbDUkSkfCVzelTAiYPYxLQkMTnxzpeCH6rIlbEXelC7UvyzJ7vP6tuUkMHUPtcQv7uEU68EG4AoQklFCjMaGNfV404kwNYYG2vKzx0cjetbMtVE1fNBxcuazRGf6ZqyH6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه شروع آموریم و کریک در پریمیرلیگ با منچستریونایتد؛ اخراج بعدی در راهه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106794" target="_blank">📅 11:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106793">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd63d44791.mp4?token=XgDJUpYNUnDKP6knhI4Lr5z59tahmDFeppbYugyys2Rt2h6vicDQ1AdtaRatOL-oAGU3vVhRjRyUjpkBHr1SFIeTk7Z308eWrjOw7rGIbLN8htKm5I8MCLVThwIk4LVKmrKIU0CRX8jlRFzRNGVEh3rs8WfYzz-OqTXnBfi0ZZLxiEklcAHKp2QA99A169Lx0yi7QF0oH9_GaOL1ELqi6Ev40Q44I5wSSRN8YBV6fMesa_tDW6kHxoY4QSmhEDd5PaS4lH-7OWM9HLViRFJZe5VOFoZ5fFHxQNt6aE2jjoe-ZhhG_2nbT3JDqTy9WjN3XMuVafnnUcqyGR4E-cdtxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd63d44791.mp4?token=XgDJUpYNUnDKP6knhI4Lr5z59tahmDFeppbYugyys2Rt2h6vicDQ1AdtaRatOL-oAGU3vVhRjRyUjpkBHr1SFIeTk7Z308eWrjOw7rGIbLN8htKm5I8MCLVThwIk4LVKmrKIU0CRX8jlRFzRNGVEh3rs8WfYzz-OqTXnBfi0ZZLxiEklcAHKp2QA99A169Lx0yi7QF0oH9_GaOL1ELqi6Ev40Q44I5wSSRN8YBV6fMesa_tDW6kHxoY4QSmhEDd5PaS4lH-7OWM9HLViRFJZe5VOFoZ5fFHxQNt6aE2jjoe-ZhhG_2nbT3JDqTy9WjN3XMuVafnnUcqyGR4E-cdtxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
پاسخ بامزه علی دایی به یک سوال عجیب
طرف انتظار داشت علی دایی چی جواب بده؟ بگه نظرم در مورد خبرنگارهای مثبت، منفیه؟
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106793" target="_blank">📅 11:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106792">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e2af4be6.mp4?token=WnreNFs2yfRV6rEkoshyl6bCM2zk1DyW4aKore62qZTBtI4-CHwewvSXA8dISWktPd2t_lLPSR_65uoJ8backrMAMSWyXU2si8tT5Kj9Ajz8gJIpzsVXWT32hsQHbrlmkja8irTojp9L8sTUPYK7T6cNMhyDOre7QzW9rqB7nvehMxLU5ljCc1BnQIJBofTTR_gpjI_ok_SnNrEUXIeAU6NmIDpsCNZrO9h329ONUDBGgQV74M1r_NTQfxAySprjUAy1hYRvF4tP3zzgzEDU8m0lIQLrYFHqXMOrIMEs5CTtEGTA2lSxFMbEq5BfrNXQAu2Yny0uEMpv7h-3xvYCyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e2af4be6.mp4?token=WnreNFs2yfRV6rEkoshyl6bCM2zk1DyW4aKore62qZTBtI4-CHwewvSXA8dISWktPd2t_lLPSR_65uoJ8backrMAMSWyXU2si8tT5Kj9Ajz8gJIpzsVXWT32hsQHbrlmkja8irTojp9L8sTUPYK7T6cNMhyDOre7QzW9rqB7nvehMxLU5ljCc1BnQIJBofTTR_gpjI_ok_SnNrEUXIeAU6NmIDpsCNZrO9h329ONUDBGgQV74M1r_NTQfxAySprjUAy1hYRvF4tP3zzgzEDU8m0lIQLrYFHqXMOrIMEs5CTtEGTA2lSxFMbEq5BfrNXQAu2Yny0uEMpv7h-3xvYCyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
دلایل جدایی اسکوچیچ از تراکتور
زنوزی: اسکوچیچ شخصیت ماجراجویی دارد شاید می خواست با تیم دیگری قهرمان لیگ شود اما...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106792" target="_blank">📅 10:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106791">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebaab7dd8.mp4?token=dvfub_yLfbvj_gLUa1lh4viZieY72o4ypV6_dm_SL-l1kYa2E5lh7OeonBjf4bWb351iIXS0FJpHg0asXvb8OsKB6gR_Ji1HZKK9SoOPd8TNG7eb4lm4UhEcjHUgnXdFkNNwJar_l1QH2IJpibHb0fHtW_Dx2ktzFwKBwrJqPkY7FZU266Om9POM6_5Soi1rSd9X_hjagCFlGoEmOiPCSYZoBPj5y5_zl1mE86MjdrrFMPh_YXZivdWb97yQ7q_g1ezVWnGYykwCSpXv-UEk3EXGiwgMe07o8cF7Ib713tjPSGCJ1sqifQ2fkDO-9GZDzH6aniKoECFHYPZ_n_RkkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebaab7dd8.mp4?token=dvfub_yLfbvj_gLUa1lh4viZieY72o4ypV6_dm_SL-l1kYa2E5lh7OeonBjf4bWb351iIXS0FJpHg0asXvb8OsKB6gR_Ji1HZKK9SoOPd8TNG7eb4lm4UhEcjHUgnXdFkNNwJar_l1QH2IJpibHb0fHtW_Dx2ktzFwKBwrJqPkY7FZU266Om9POM6_5Soi1rSd9X_hjagCFlGoEmOiPCSYZoBPj5y5_zl1mE86MjdrrFMPh_YXZivdWb97yQ7q_g1ezVWnGYykwCSpXv-UEk3EXGiwgMe07o8cF7Ib713tjPSGCJ1sqifQ2fkDO-9GZDzH6aniKoECFHYPZ_n_RkkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
روزی‌که استقلال تحت هدایت جواد نکونام قهرمانی و اورونوف رو تقدیم پرسپولیس کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106791" target="_blank">📅 10:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106790">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c341c5cc5.mp4?token=pNXBPTnGwrUiwd5aUgaEvwXjiP48wwH1X6WW-ruv1oRUYPpRao-aihWuPZO9YhP9LM-WbpvwM6F5o_AHCt3VwfGGvYjRfp3O-1ypaYyzRbzKrOfLDKXXgzAgepzi6Urz8yzyx2QlAQgHxHjBuoyDJ96rHg4-kNdZUaUMuPYGpwzHrgVEL32xA8Vj6KLqGmazxRNYY0lYnwpPexPBHGVlJTLtsIzb-GXOXmIwEyxCYBwdk9P8uwBkuQNgtwYi_cl-1oB51BL6X-xudegRCyYizOzqKBolEYvWC9kKPO16xgcqLY7Lj0mg1D_7fW4bRiB9DAsdvRT2Iyqn8hMf-s69ELn-twcB6qMJWPLo7F9kFGkcH-kKXtRdWWJT_5PgznYn59cRzwcji1iF2vBdlChgriKd9ACtLcnFvqrTH7nCX8_k4J1ypOml7LMujdJKQg3z_ynFQrqXFZF2PXvUpgHnp3Qre29etSPGiERyZx6NBz2UW-1igR84P1qZBfPEG4Aog7FUDxkra8-1d1plYCGJnU27TdyFMZ2qROyRHP5PA4MDw_qTAp3ZH6KVeiE69doScGdYJJGdRz2S3wKyRNZYX8INhRlkFQ-t8bSGBlbDN-RR1HB89adHLqoRlXgKzAcB9QRzsQ8oK7RJusm_dN9FahzTuvD0izIL_-eB2MWlA6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c341c5cc5.mp4?token=pNXBPTnGwrUiwd5aUgaEvwXjiP48wwH1X6WW-ruv1oRUYPpRao-aihWuPZO9YhP9LM-WbpvwM6F5o_AHCt3VwfGGvYjRfp3O-1ypaYyzRbzKrOfLDKXXgzAgepzi6Urz8yzyx2QlAQgHxHjBuoyDJ96rHg4-kNdZUaUMuPYGpwzHrgVEL32xA8Vj6KLqGmazxRNYY0lYnwpPexPBHGVlJTLtsIzb-GXOXmIwEyxCYBwdk9P8uwBkuQNgtwYi_cl-1oB51BL6X-xudegRCyYizOzqKBolEYvWC9kKPO16xgcqLY7Lj0mg1D_7fW4bRiB9DAsdvRT2Iyqn8hMf-s69ELn-twcB6qMJWPLo7F9kFGkcH-kKXtRdWWJT_5PgznYn59cRzwcji1iF2vBdlChgriKd9ACtLcnFvqrTH7nCX8_k4J1ypOml7LMujdJKQg3z_ynFQrqXFZF2PXvUpgHnp3Qre29etSPGiERyZx6NBz2UW-1igR84P1qZBfPEG4Aog7FUDxkra8-1d1plYCGJnU27TdyFMZ2qROyRHP5PA4MDw_qTAp3ZH6KVeiE69doScGdYJJGdRz2S3wKyRNZYX8INhRlkFQ-t8bSGBlbDN-RR1HB89adHLqoRlXgKzAcB9QRzsQ8oK7RJusm_dN9FahzTuvD0izIL_-eB2MWlA6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
خداحافظی خامس رودریگز از تیم ملی کلمبیا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106790" target="_blank">📅 10:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106789">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0579123b95.mp4?token=dciN_SyR63LH3rHdR1DdB4wmrV0PT0FHEh0YjCggyF83K121GgvrPniVfoqa7tw8JEAZ3PMBLy1FZdL4RNrDRVsyVcZreDl8qPH-V1GpIrrDDvmReRq1ZvhESNa7ZVJSOQKzHqm5sYB2Bmc6IBfEhT1wsoyfqyRKT4fl5CKG3qy82e5Ze9vKRLRA0IonjTJFZKio1vMojmoxVJZMAn1aR1Ffao257RlAEYoxHxqyZyeLxGwMNPYzlQ8RbXnXYvevh5FZy7Nx-oBDiFHsRDetKs_zOCmtU01O1RQNXJJmKZmISNgfTZHUcscaOWRzu2pwJF-diWWPgA5j4sN7Rqs-8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0579123b95.mp4?token=dciN_SyR63LH3rHdR1DdB4wmrV0PT0FHEh0YjCggyF83K121GgvrPniVfoqa7tw8JEAZ3PMBLy1FZdL4RNrDRVsyVcZreDl8qPH-V1GpIrrDDvmReRq1ZvhESNa7ZVJSOQKzHqm5sYB2Bmc6IBfEhT1wsoyfqyRKT4fl5CKG3qy82e5Ze9vKRLRA0IonjTJFZKio1vMojmoxVJZMAn1aR1Ffao257RlAEYoxHxqyZyeLxGwMNPYzlQ8RbXnXYvevh5FZy7Nx-oBDiFHsRDetKs_zOCmtU01O1RQNXJJmKZmISNgfTZHUcscaOWRzu2pwJF-diWWPgA5j4sN7Rqs-8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
حمله تند فرشید اسماعیلی به شفر: قبل از فینال جام حذفی گفت یا قراردادم زیاد می‌شود یا روی نیمکت نمی‌نشینم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106789" target="_blank">📅 09:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106788">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1063b33e5d.mp4?token=S_lp01pwinFIWuwAhY3-v2cDc4Vz7uvP2mu3k1WNBtl0LeSWgcp5FqCVn9Y81NaiI5anl15YqzEx02QC2kRa1N8GdrtcZgVuRvL_SmS5jpCSElAApMnlhB9JtWaZqi-M__vax90ALug75SRz4umJBhk44LO-ICInaRPYo-BkLocAZ7YGENBMFumKSOPhsX0CFcigEoagrOM12VZfEZMSfeIwcCheQQeVA5f7TWRaaa56YEuBxWSfdk__77y0Gxkux3ZZ5PJlnX9njjqD9x8iVLO344Elxm2rHg5rNQvR5QkcxTerA3GDo-9mPZMizo7784hsYFe-N1j0wQ_O0TzbeomtzIViBdRBYmAObSW2C8A_0iAWvoyCFBQbnXhk7Db8CBBybX6lE9VOXhDq3eYT6O6SJbzUu1aVg_-ggogHf_eHQb2WPZOtzmxtk4oEz7OZSe9H1a27SaWgMnEZXA6YIYAPUyIaQKTbUP6pm6-K-tD5zdnbp_0C-nTy2ptkH4qKxWylTD4rfFXsyffBTAd6vJnMh4P5iK6AmcOSOORRZ5orewYj4XeusZj2RAkGxSvrXCnNnE-kfiAUMw506S9Xte2FdqTGW62DB3iri4KGXp5qs2Wq6aA9Iu7tY9Bnv_9njBO9qFHdDB1b84f4mDxBgOb1VPn3CflDA28MkxWV_9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1063b33e5d.mp4?token=S_lp01pwinFIWuwAhY3-v2cDc4Vz7uvP2mu3k1WNBtl0LeSWgcp5FqCVn9Y81NaiI5anl15YqzEx02QC2kRa1N8GdrtcZgVuRvL_SmS5jpCSElAApMnlhB9JtWaZqi-M__vax90ALug75SRz4umJBhk44LO-ICInaRPYo-BkLocAZ7YGENBMFumKSOPhsX0CFcigEoagrOM12VZfEZMSfeIwcCheQQeVA5f7TWRaaa56YEuBxWSfdk__77y0Gxkux3ZZ5PJlnX9njjqD9x8iVLO344Elxm2rHg5rNQvR5QkcxTerA3GDo-9mPZMizo7784hsYFe-N1j0wQ_O0TzbeomtzIViBdRBYmAObSW2C8A_0iAWvoyCFBQbnXhk7Db8CBBybX6lE9VOXhDq3eYT6O6SJbzUu1aVg_-ggogHf_eHQb2WPZOtzmxtk4oEz7OZSe9H1a27SaWgMnEZXA6YIYAPUyIaQKTbUP6pm6-K-tD5zdnbp_0C-nTy2ptkH4qKxWylTD4rfFXsyffBTAd6vJnMh4P5iK6AmcOSOORRZ5orewYj4XeusZj2RAkGxSvrXCnNnE-kfiAUMw506S9Xte2FdqTGW62DB3iri4KGXp5qs2Wq6aA9Iu7tY9Bnv_9njBO9qFHdDB1b84f4mDxBgOb1VPn3CflDA28MkxWV_9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👑
🇮🇷
ینی بهتر از این خانم بنظرم کسی نمیتونست تمدن کهن ایران رو بیان کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106788" target="_blank">📅 09:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106787">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7912d30312.mp4?token=BD9zroIANAlQfGEmTA2PK24xeHh5WmI64aWZ8DPTks7ohdOpLREpHYeXf-GtY0ws7i81Zl3KfEUgkFNqPXfIPbkIxQCRaU-TiUHudjBkwhd9eHQpY4aWxfm4iRfoJc83dXMP44qYJY15vretcFNOSfilNqBDjPQhfMb0VyXADVbWVQTO6DRDXvop9ymGk12OsV2VDyNS5Ncwzcvd5Gg7cqbkoYs1zSbDySRkAxj5sHXNDKnfXeccA33KswFT2rip-hRONUYQgS9nu5jMfbE8XrPW89s3qhGQMI-S987uEZ1PQ7FxzLoGlo-MTKW4m_rjrEXqKSuWItbMo61UrxzAWRmTbJXq3gU_DLOsmtUcbSI2WJY1_Zjkz7HvVeKlKIYSCW9KbT-sL2-VZlOf7BOqxIs7L3PQT__qj-etXcuYXpp302BDt3bexDEN12OXJ-WeQ6X9ANqu93o7ASL3vjKfHkFJOQXAwEhSoUrm9H3YqyN812lz2hMIktjptcz_0YNtpFdy61opV7NkQYSVn-zeaR7BzCm48fGnyW2nzp72hosD4bA0VhgMRlhH3EoJuhF1j3nyNdUXVpklXSybYuBPTeDUFPcBb4Y3wjdSEn7hCittWBqnTNt5Gd_RbZ-E8SMRp6WvG8o9JyJ8lYMoK3e8dq5AuAudoc7VVENRYdOYjVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7912d30312.mp4?token=BD9zroIANAlQfGEmTA2PK24xeHh5WmI64aWZ8DPTks7ohdOpLREpHYeXf-GtY0ws7i81Zl3KfEUgkFNqPXfIPbkIxQCRaU-TiUHudjBkwhd9eHQpY4aWxfm4iRfoJc83dXMP44qYJY15vretcFNOSfilNqBDjPQhfMb0VyXADVbWVQTO6DRDXvop9ymGk12OsV2VDyNS5Ncwzcvd5Gg7cqbkoYs1zSbDySRkAxj5sHXNDKnfXeccA33KswFT2rip-hRONUYQgS9nu5jMfbE8XrPW89s3qhGQMI-S987uEZ1PQ7FxzLoGlo-MTKW4m_rjrEXqKSuWItbMo61UrxzAWRmTbJXq3gU_DLOsmtUcbSI2WJY1_Zjkz7HvVeKlKIYSCW9KbT-sL2-VZlOf7BOqxIs7L3PQT__qj-etXcuYXpp302BDt3bexDEN12OXJ-WeQ6X9ANqu93o7ASL3vjKfHkFJOQXAwEhSoUrm9H3YqyN812lz2hMIktjptcz_0YNtpFdy61opV7NkQYSVn-zeaR7BzCm48fGnyW2nzp72hosD4bA0VhgMRlhH3EoJuhF1j3nyNdUXVpklXSybYuBPTeDUFPcBb4Y3wjdSEn7hCittWBqnTNt5Gd_RbZ-E8SMRp6WvG8o9JyJ8lYMoK3e8dq5AuAudoc7VVENRYdOYjVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
صحبت جالب رسول‌مجیدی درباره تواضع رودری ستاره بارسا در دلجویی از والنسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106787" target="_blank">📅 09:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106784">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-JysuT6hElUQnB-u1g1kB_IbGCboKjUblXvTMZLlUxGulCo1vDyc_NzgT7ipq3fBNVbB1sha8K6uPZ9z1LWGNnTRTyNWrkN9pGgBkncyy7KrsarfOo30-kRdxddRw8JvwlhqPYIZ00EDyoJ0gxRZDiCACQf_SGm9rsmIKsbtjYzWZHprZOSC07T2H8nQ3Z5hldZnUjm8gkC4QhwMbKbe6NAxecEdTZSR6zxw1GhC_DyT1644P0uhqJcd3Hnr5o6Lmpm8VvTnb4OUtyZ2XGV5eNkUyY7UTRsmzd9DQaeCkxWVms6VCWmSy7B7okVKntqrAaKpZT357DXdnK8-LA_AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
📊
🇪🇺
نتایج هفته اول لیگ اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106784" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106783">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea7884a87d.mp4?token=nzrAeic7Fb7aTtjALSMoE54s2utIOzReZe-6DjWbwxUPMTvq5E84RFcJ78G6PONr7UPK-uOsw4aA_a8lJ1pzcRyzZmTEOmuBwNUt11n3NyYCYB2V4kQnFSmp22ygXECWjIo90Kk3wv3rHlZ_zmLAhJQED14ulwAAsTqhKmHQrRs9mw-s1a76ujcTO4gdnaLgcLIpTdIzX1od2VPEG-NXpKC9s9WGFyOPYpmvG6ff4jr8L3EC6UKmQirUXTFgKkICCAP8Y4u8NxalFpdBEjAyWjvT7MJuHD3akISqCwZ3b5Sxoh3FkgAYhO1-VATtNugUrluNw-SZQooNvrwDJyFh0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea7884a87d.mp4?token=nzrAeic7Fb7aTtjALSMoE54s2utIOzReZe-6DjWbwxUPMTvq5E84RFcJ78G6PONr7UPK-uOsw4aA_a8lJ1pzcRyzZmTEOmuBwNUt11n3NyYCYB2V4kQnFSmp22ygXECWjIo90Kk3wv3rHlZ_zmLAhJQED14ulwAAsTqhKmHQrRs9mw-s1a76ujcTO4gdnaLgcLIpTdIzX1od2VPEG-NXpKC9s9WGFyOPYpmvG6ff4jr8L3EC6UKmQirUXTFgKkICCAP8Y4u8NxalFpdBEjAyWjvT7MJuHD3akISqCwZ3b5Sxoh3FkgAYhO1-VATtNugUrluNw-SZQooNvrwDJyFh0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
ادعای هومن افاضلی: ایران در آمریکا از ورزشگاه آزادی هم محبوب تر بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106783" target="_blank">📅 00:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106782">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBBa3RVLPVSFbbuanPxDxbuVY_kr5q07vnlberdU2xh08TB44kMSPcElTTJ50HbAzBWr3MX5EPQ6iajQ3IC75vJ1pLHvPhS0NzWKudGp1U6Y62CyUXcVP8kSZUTpFPXh6ra0qWugmMzkYnVA8EsyDsqYwA1d-Kz_AIJrSQVQWg9GSgxTRecsBq3uDK_OcaBG0vrMexau7h3wnA2fQ_mbtC4AYN_gIdzzj1ZD3Y0rsgGt9tAK2lBFrPW4Gq_baHQPmEN9xJqFP3L3w987WDJzKqNYsNLRFbvKVzb63oVuRZbykIuITTaS7VdZhQHuRrf0SdK2rkR7oGOFZm4AaOOGRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جام‌اتحادیه انگلیس؛ سیتیزن‌ها در یک بازی درخشان و با گل‌های بازیکنان ذخیره خود مقابل نوریچ پیروز شدند
منچسترسیتی
😄
-
😏
نوریچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106782" target="_blank">📅 23:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106781">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ2PJe7aDx-T6kUkoKMQGrycQva7O3Ap69ZhTtU0N4bwXddkrt4bwRb1Ag46AkBvPovBHwslah9r1VpvivIZL9WD0fBDHuPE2lNVFVNIjNHLeEk3u8s5GbuY_x7Z9-u04HmBPPzGEhBCBXIGubloXeVoTJK62QTx-7ifSTxyoaZkRMRvHFEgumbhpEYrzhpizNKXLqV7UMGqBklT0pzlQlwscmlZ5WCy1Hfog8IbQ7PDD4qopIYWgo7wSrkHpfr8Pvdju4CSF-l1jfs_E9u8z58hLZKnZEju_6S3ZI3CEoN8x0rbnLuVvKbNpdGcwyOl9RLTNNP7VBUU1m-EN8tf-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وقتی لیونل مسی در سال ۲۰۲۳ به اینتر میامی پیوست، این تیم در قعر کنفرانس شرق MLS قرار داشت و تا اون لحظه هیچ جام رسمی‌ای در تاریخش نگرفته بود.
✅
مسی پس از ۱۱۵ بازی، به ۱۰۰ گل با پیراهن اینتر میامی رسید و این تیم را به چهارمین جام تاریخش از زمان حضور خودش رساند.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106781" target="_blank">📅 23:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106780">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af53c1869.mp4?token=oqymuHSXEJ6iaXsb04LAX9TP_0C1ECmFSYwgQnh6Xs-83AJBw3kc7wavNpGnwUo-8tkzfaWesoFBXZmVG4EdPT8srIv5zUDDDxFHUZqvNlkVzFBKZJ-_3tGSdsjg2G2_igHFALPhIH5-I8Agwl0n7HBMCaxHpR3G7pkfpgGYz4MLPSTgS5Oxzn2D3CvI2Lr33uVJOJq3QsfMof7SrWWqqVv4Gwu5JG-6xz6WrIb3g7wALTo_qfTrxYMD3jjVC9fA_tmBktYCZodbJdFZubSNT32JhDzMUtgx14jDu1MWxOd_6bK7m9ED_YIBx1RQQHAWd8ER48uj_x3BVOPXwvPTAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af53c1869.mp4?token=oqymuHSXEJ6iaXsb04LAX9TP_0C1ECmFSYwgQnh6Xs-83AJBw3kc7wavNpGnwUo-8tkzfaWesoFBXZmVG4EdPT8srIv5zUDDDxFHUZqvNlkVzFBKZJ-_3tGSdsjg2G2_igHFALPhIH5-I8Agwl0n7HBMCaxHpR3G7pkfpgGYz4MLPSTgS5Oxzn2D3CvI2Lr33uVJOJq3QsfMof7SrWWqqVv4Gwu5JG-6xz6WrIb3g7wALTo_qfTrxYMD3jjVC9fA_tmBktYCZodbJdFZubSNT32JhDzMUtgx14jDu1MWxOd_6bK7m9ED_YIBx1RQQHAWd8ER48uj_x3BVOPXwvPTAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🟡
دفاع قاطعانه بیگ‌آنز پوستکوگلو از رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106780" target="_blank">📅 22:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106779">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njJDSCl_RCujRWufJcBUFlzPNKMG3Puxe33TDqyUsix8jQLqZjIaswb1ZxlSSv4FLwX1Jef1fekJN_4rKwg4slEG2qYq_v_T1U203jX89aXbPPYGZnnNs1vL-fr7Oi4w9CO92km8mtW3-YEsI4H0xjMNJqIKgXURTqqgVYIohR4pYZuxVrZjUW_eqlx-eX7S7dItfQAh6WGqRdOSb2zdicHvCibolbI2TXO8yJSt0w1qQSKNmeD1B16tOznRsn5MZp6lv3vypskIWdsRqLvkBQgHpxowUQwwvz5ivOZod5VCVzA3deYqqBzSBanqMaXGZbb_noWayMzHvkIpEa_XvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه اسطوره مسی و رونالدو در سال ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106779" target="_blank">📅 22:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106778">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U297exZ6jd5r3EpiUEndvngxyaZDNnFMPTRgl_IG4CdXcGkKo-nTarYeWiswxGFDGoaI4_PvobcrJvDUUE8H2UNRheeVYwNqpDgCYTmajfiDNUw0SZ2rHFmJAfpe6qUlesF8HLiongyspEsuWJkS6YZDAp8Pkxn004K5kVqFBALDL2CAhhZfrHu5bfRex_re9T3RMVkPAJnC0npdgt5805KHU9bYYAKTavXfHk5rrxQ9ZlxORsiy_yDZ9ua5ta0nd8jsnVjV_xKJAPw5R0xwHwzvq6rZ2xgwCvlvFCo8UxXj3YB-bbBUvduAG25p0n3m3xOfhdPkHUdULYr20wQttg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
✅
⚽️
هفته اول لیگ اروپا؛ ترکیب لخ‌پوزنان مقابل کریستال پالاس با حضور الهیار صیادمنش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106778" target="_blank">📅 21:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106777">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✔️
🇮🇷
🎙
صحبت‌های جالب نوید استادرحیمی درباره عملکرد درخشان یاسر‌آسانی در استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106777" target="_blank">📅 21:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106776">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yw4egvvdOwEKQRSY1FI6qno1JAe8aTjCoOfJIpnbUbV2OaG9ct-sU4WYuSEXk5ovEK9h3cl7YHWQ_MmZ-QtVrcAIvDFbhetbReWN_aRymeTGgBRhhPOHnWU5RfA4NHCLlxYTL-RrLwZwxAYsJQrbNSWTxecjxElUTPdquBLhezU7YDw5AeJ1oTPayoLvh7BOme1rtG7B_1CBxtCtmLqwen3VVIT1uGLDIBWI5ibT3s68dTyyUIjbInAKpuDc5cgy2eJUqd97JmkM5ZhuqYYb4OzxPePF5V1Kgzfi96SLt2vBCCKR23U2StGmC086ayA3shUC92TGnRhd7FOvz4wFdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جام اتحادیه انگلیس؛ ترکیب منچسترسیتی برابر نوریچ؛ ساعت 22:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106776" target="_blank">📅 20:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106775">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8c416616.mp4?token=Wnt6jY1GLSKPMmtVtqhTbPucnLH5gSK1WVP_dlaBT4ts6ZjfjCQxOE84SNKnBv7E_r5hEse_6Zt9d-sxb28L-FEnOY9atHGhOlgQP9l4-c5aPZdv7bHf7ghWubwOeXzAiXVkY7pc6p6xLA0WvYUpq7zStx7a3ZVATkNAZsh04a3foDudzxSu71whMbjbtS1DxhoaJ5uWdLwFqyTAV9bcmps5hfQ9pRQSkp2WHNjKyDGZ2hFxrmB9lYQ0HPa68uaQanMnsdz0UuBsXDUNSMuWaCCS2uYjuf_KXy-4iIVCEe6vYA4DuoLxYtqnQxJ_D_xUe253LVSEl1_ph1tBsF0seJUHnD0YV7BBttnbQlI1sWbKUr7WGTrM7G_kXGr2R4aYX2DJ0nAZHazJkXH6AVNlj3IhMmHYn28Ouk-TlF7VCnRcZtF-ylraUrNBS07eQwlfDCXZMqo0HXtRiUlX6ZFNvzdeKzqeUcxkIKEENWrJ-ts13xsxGvejsVM6emwiX7msnaCtj276ecgacU5FuryTF1uBTRF9cld_0TyuUdgYbXoGsOlqTEEI7pHLmyliqCR43cO92nL2ebRHAodC9BSykULiE-O6c1CoVc4tP5dKoUUW_kXTBuV18sAc6v0UKU6uzqF7SJLEWN_y3sW8B3bRsWKMsSiEPmR4aM-PTGATyR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8c416616.mp4?token=Wnt6jY1GLSKPMmtVtqhTbPucnLH5gSK1WVP_dlaBT4ts6ZjfjCQxOE84SNKnBv7E_r5hEse_6Zt9d-sxb28L-FEnOY9atHGhOlgQP9l4-c5aPZdv7bHf7ghWubwOeXzAiXVkY7pc6p6xLA0WvYUpq7zStx7a3ZVATkNAZsh04a3foDudzxSu71whMbjbtS1DxhoaJ5uWdLwFqyTAV9bcmps5hfQ9pRQSkp2WHNjKyDGZ2hFxrmB9lYQ0HPa68uaQanMnsdz0UuBsXDUNSMuWaCCS2uYjuf_KXy-4iIVCEe6vYA4DuoLxYtqnQxJ_D_xUe253LVSEl1_ph1tBsF0seJUHnD0YV7BBttnbQlI1sWbKUr7WGTrM7G_kXGr2R4aYX2DJ0nAZHazJkXH6AVNlj3IhMmHYn28Ouk-TlF7VCnRcZtF-ylraUrNBS07eQwlfDCXZMqo0HXtRiUlX6ZFNvzdeKzqeUcxkIKEENWrJ-ts13xsxGvejsVM6emwiX7msnaCtj276ecgacU5FuryTF1uBTRF9cld_0TyuUdgYbXoGsOlqTEEI7pHLmyliqCR43cO92nL2ebRHAodC9BSykULiE-O6c1CoVc4tP5dKoUUW_kXTBuV18sAc6v0UKU6uzqF7SJLEWN_y3sW8B3bRsWKMsSiEPmR4aM-PTGATyR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
توضیحات فرشید اسماعیلی درباره چیپ معروف در دربی تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106775" target="_blank">📅 20:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106774">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d822ce6be.mp4?token=HAF7qodeyF6cfmgxmfhTz8YOwVho1M0sEZXYneKE0_XuwC7cf_IJgEQtyF0WxpFn3emD6aGBcOWqkmZKaehz92ZRlJBntMmODs2afbZTofTwyUTGz5zIVBsptZOq_aKXZHt6mU1NgUjede08r0H4sCljaMHonEgyq7S8vYxZoygDxw1aDPWAKQc-fEeu-s7XmKDrRyMNrSNravEsFsnYCA-oFcUInDwv7kGmqMxxk_jRiVomtHYXBFM5KUyirzAc0alLitgaV-gS5y4JJ5u69D1H34x2-pJe0lZyNb1Ge_1E6u01OpAL4X45QOd2QSfdSQpW8-fUix_5WI3qdXytXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d822ce6be.mp4?token=HAF7qodeyF6cfmgxmfhTz8YOwVho1M0sEZXYneKE0_XuwC7cf_IJgEQtyF0WxpFn3emD6aGBcOWqkmZKaehz92ZRlJBntMmODs2afbZTofTwyUTGz5zIVBsptZOq_aKXZHt6mU1NgUjede08r0H4sCljaMHonEgyq7S8vYxZoygDxw1aDPWAKQc-fEeu-s7XmKDrRyMNrSNravEsFsnYCA-oFcUInDwv7kGmqMxxk_jRiVomtHYXBFM5KUyirzAc0alLitgaV-gS5y4JJ5u69D1H34x2-pJe0lZyNb1Ge_1E6u01OpAL4X45QOd2QSfdSQpW8-fUix_5WI3qdXytXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز خوبه قبل گفتن یه ببخشید گفت
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106774" target="_blank">📅 20:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106772">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae6b91a252.mp4?token=pevxRj5g7Mtw3RFlpfRs8HDa2XMynv-e9-k28GEy_y_5GNFzs9WFtB2SX2vQpMSBo-34-wmIUf8R7_LLFfZQVYw1Ax1weL3zXlhlLgGcQgRjazcwNLVrnWB2N3UilUCNz5jN8dDun8WxKy-5SQorUOsJtqYAIdP1Y4TF3rhPVC4YHWTjKQkSud_4iVKI_-QEJiaS6O-aE3by6kgqBNVI3IvwQOKc3OMZAgEJEUtoxyNIWofwhBBv0Z3XMGclz81lLKYiYO0FHGoFoJDzbsKOUYqJv7oPzFylKQ5Q93-O1QVUMd3zOOTrekoRuL5b688glriKMCbjRfLywwtgkiLIYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae6b91a252.mp4?token=pevxRj5g7Mtw3RFlpfRs8HDa2XMynv-e9-k28GEy_y_5GNFzs9WFtB2SX2vQpMSBo-34-wmIUf8R7_LLFfZQVYw1Ax1weL3zXlhlLgGcQgRjazcwNLVrnWB2N3UilUCNz5jN8dDun8WxKy-5SQorUOsJtqYAIdP1Y4TF3rhPVC4YHWTjKQkSud_4iVKI_-QEJiaS6O-aE3by6kgqBNVI3IvwQOKc3OMZAgEJEUtoxyNIWofwhBBv0Z3XMGclz81lLKYiYO0FHGoFoJDzbsKOUYqJv7oPzFylKQ5Q93-O1QVUMd3zOOTrekoRuL5b688glriKMCbjRfLywwtgkiLIYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
یه خونواده ایرانی عروسی گرفتن، بعد اسنوپ داگ رو به عنوان خواننده آوردن
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106772" target="_blank">📅 19:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106771">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd7aec7c83.mp4?token=HqFPARvlnMNrugE_yNCo2VGCBr67i_z-rDx94EoGM06QIBiDFBkS_K4nsGmx-ulOFW9Pbmte6yOTVWt__gXTz5JwYKUFjowXZ9Sw0PIrMb_jTTERdiFpcaHVu3uBFL0A0aE4GgM2NVKN-esEeqXxPkFwhyvt5vXYjxrvASGbDo4-Ok6_t8PY-ASsw9CesrHV_sbkKOq2wRrtxECgM748vGWjaWLxNX7HgnfRsbO_xfplS3nYPbtIg9fen5Fdk4t5586TE-d_MSRYAPHU7KWsmJG6uhrL4mx_VXY_gyBevjOJy_y7IhmPEOEpyld2CweQaGIg5CrUYvB9L0klKMyrg5g_6OwSS6RHcm5_4sMVjK7PLgUu2Of_w4Ea7tsYBEpxWRW42UdIXRgO5RrJksrBK5-QAErB-Ssn178ZBDhvi5sIHR_1Sdm3G372eSXjl9Gut4NFEJRgBIwLM1xp2ZV6ZlGbMGCm2Mn1yliIbiHQOCQX7dhfXjLhIepfijl2exDL2KGWIQexu8jUm7J9Jj1qJcxbIS6AitZHgHBy-NQNMJ23OsFDQtEmyeTEA5f30AvqvXxPuPfM95OnyY3JkzAIZxrds_aQQ3cLtjs8pl6N7I1wSHaW5YOWSwg4FLV9S1wibhbJFUPz22Mup5hoNdbFetvMr-Natl-uvPKOAQotBhk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd7aec7c83.mp4?token=HqFPARvlnMNrugE_yNCo2VGCBr67i_z-rDx94EoGM06QIBiDFBkS_K4nsGmx-ulOFW9Pbmte6yOTVWt__gXTz5JwYKUFjowXZ9Sw0PIrMb_jTTERdiFpcaHVu3uBFL0A0aE4GgM2NVKN-esEeqXxPkFwhyvt5vXYjxrvASGbDo4-Ok6_t8PY-ASsw9CesrHV_sbkKOq2wRrtxECgM748vGWjaWLxNX7HgnfRsbO_xfplS3nYPbtIg9fen5Fdk4t5586TE-d_MSRYAPHU7KWsmJG6uhrL4mx_VXY_gyBevjOJy_y7IhmPEOEpyld2CweQaGIg5CrUYvB9L0klKMyrg5g_6OwSS6RHcm5_4sMVjK7PLgUu2Of_w4Ea7tsYBEpxWRW42UdIXRgO5RrJksrBK5-QAErB-Ssn178ZBDhvi5sIHR_1Sdm3G372eSXjl9Gut4NFEJRgBIwLM1xp2ZV6ZlGbMGCm2Mn1yliIbiHQOCQX7dhfXjLhIepfijl2exDL2KGWIQexu8jUm7J9Jj1qJcxbIS6AitZHgHBy-NQNMJ23OsFDQtEmyeTEA5f30AvqvXxPuPfM95OnyY3JkzAIZxrds_aQQ3cLtjs8pl6N7I1wSHaW5YOWSwg4FLV9S1wibhbJFUPz22Mup5hoNdbFetvMr-Natl-uvPKOAQotBhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇮🇷
۸ سال پیش در چنین روزی، کامبک پرسپولیس مقابل الدحیل. اون دوران الدحیل تو ۵۱ بازی فقط یک باخت داشت که اونم جلو پرسپولیس برانکو بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106771" target="_blank">📅 19:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106770">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5345b9e16.mp4?token=PKc0uGleKGqKhEKsxgoE5NCfi5qoDJ89Irdkm_FCWoptj1EQgWst4-E7lNbNAg8ewN3VfdbmalnBX5T_f7g8cVjJJWWCBCvwBOlE45KNvW5GY8wq0d20vBP0ktkIvYv2iM9uNPVtjeXFf3GZzuVFDQJP32Bd0rgZsFtpRAd-fUXzAP1CCNTaSe3CxFeCjlIuJFqtwHLSIDI98OcbCmHgYhIfGV2JUzCGCQ7np-CpSOuVjvKcLUqPJBk92Ot9QdVL19eVgv0g6sGEguHyTt33LWr3ow7Di1MMEyTrl5ZrT4K-NyWQxgkHiKYPXgAyPEvM0D2BGOn0gVOWJ7ykJqlrIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5345b9e16.mp4?token=PKc0uGleKGqKhEKsxgoE5NCfi5qoDJ89Irdkm_FCWoptj1EQgWst4-E7lNbNAg8ewN3VfdbmalnBX5T_f7g8cVjJJWWCBCvwBOlE45KNvW5GY8wq0d20vBP0ktkIvYv2iM9uNPVtjeXFf3GZzuVFDQJP32Bd0rgZsFtpRAd-fUXzAP1CCNTaSe3CxFeCjlIuJFqtwHLSIDI98OcbCmHgYhIfGV2JUzCGCQ7np-CpSOuVjvKcLUqPJBk92Ot9QdVL19eVgv0g6sGEguHyTt33LWr3ow7Di1MMEyTrl5ZrT4K-NyWQxgkHiKYPXgAyPEvM0D2BGOn0gVOWJ7ykJqlrIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایانِ عصر خامس رودریگز در تیم‌ملی کلمبیا.
💔
🇨🇴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106770" target="_blank">📅 18:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106769">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9692b0808.mp4?token=Wv4aU49jMkPRQMnS3HXsbOCZgEnxBoKrdN-dJYGPD8DXRGaan7W9_oyYmgdJ6ahaLLkLUve1Ti4nBdZnVZAcirnkzRKJC6dlWVPOYrPqo00VqNhjlxvx9Ex3gwnkciQ5JRqptsE5LjxhOpXICc7JPfaiIIy66lb43VydYngw9bYHsDlalgW3Y7Dk_gxeG8kg-nCJhGO3WYXb_wnv9gve48bmk2hkjNbOxVNCePTPGCJbaVsePmvqBTFe6zFlwtZRR1XhzGS4NMI8k4bfINSay1RFXVw5mTwUJTCq1TUqc5HNiMI35R0y2qj2E7NvylPwAnpVQTJo12C_wo-_QtWOLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9692b0808.mp4?token=Wv4aU49jMkPRQMnS3HXsbOCZgEnxBoKrdN-dJYGPD8DXRGaan7W9_oyYmgdJ6ahaLLkLUve1Ti4nBdZnVZAcirnkzRKJC6dlWVPOYrPqo00VqNhjlxvx9Ex3gwnkciQ5JRqptsE5LjxhOpXICc7JPfaiIIy66lb43VydYngw9bYHsDlalgW3Y7Dk_gxeG8kg-nCJhGO3WYXb_wnv9gve48bmk2hkjNbOxVNCePTPGCJbaVsePmvqBTFe6zFlwtZRR1XhzGS4NMI8k4bfINSay1RFXVw5mTwUJTCq1TUqc5HNiMI35R0y2qj2E7NvylPwAnpVQTJo12C_wo-_QtWOLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
بابک‌مرادی بازیکن سابق استقلال: ذهن فرهاد مجیدی را خراب کردند؛ خیلی آدم خوبیه اما یه دستیار مرموز و بی‌شرف در استقلال داشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106769" target="_blank">📅 18:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106768">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYN4QsB-ioxc9CisuCGwPn53bjg6PnLnWFqzCNib5fkFsnBcS3w1cNROiIfPJpTKx7eN-LicZ5YYVHG6FhUghcLcAhgLMO_NoOumE7WRHFJQ3Bu6eBQDAnPPVJzncdY7nnz-4aejwIX2QPKn0caUWHlj5pg91EIfz8122xgEu4jlffWDH2joFsQVXMNKn6Gvx_tdAxpcZ-wV6-YnY3mlEUhAIJYo2wh7eNzfkKGy5FkSIxvr6cNkKLgvyMlgtitb5K1XIyE7YTNdW6q2iJ3MwIzd4uYglopD4_MRRurFcPD9-CtklsuFBAjWG8OBYtkgTmcwVobjP7FSJSx-eSsSkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
برنامه سوپرجام اسپانیا 2027 اعلام شد
نیمه‌نهایی اول
🇪🇸
بارسلونا_ اتلتیکومادرید
🇪🇸
⚽️
13 بهمن 1405
⏰
ساعت 23:30 به وقت ایران
نیمه‌نهایی دوم
🇪🇸
رئال سوسیداد _ رئال مادرید
🇪🇸
⚽️
14 بهمن 1405
⏰
ساعت 23:30 به وقت ایران
🇪🇸
فینال سوپرجام اسپانیا
⚽️
17 بهمن 1405
⏰
ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106768" target="_blank">📅 17:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106767">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d8b49aaa0.mp4?token=EK_7fK693VzjHv6OeO8w5zq5SSnykvxus_VI4hnkcof_EFwq65xi0naJ6tUAmf51dXxj7SNZ5b5Hp9VxUuRA8I5FmnYb_8zRJAnLpLmtuL3wQdQrg36XjqyvHchYMxJmTpc4mkoaKRHiH0qqIxdXYrEqRVoYsachN1wJhEIrCuV7hD1FNRzdMZUlxRvZRRA5hQUfSqdVw2LWqQoP_u2NMCfqhG-FLq2QqMaEnIl9n4jN_FgN1uK-agITbZTRBa9jtBGJF5Enaizzau3Heyd2-tHPIn1eKfV9g4hqrPJhKg0KP-ytUpyqQFqDgx3IIqmUQwE39r2vSVdathAJ6-P90Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d8b49aaa0.mp4?token=EK_7fK693VzjHv6OeO8w5zq5SSnykvxus_VI4hnkcof_EFwq65xi0naJ6tUAmf51dXxj7SNZ5b5Hp9VxUuRA8I5FmnYb_8zRJAnLpLmtuL3wQdQrg36XjqyvHchYMxJmTpc4mkoaKRHiH0qqIxdXYrEqRVoYsachN1wJhEIrCuV7hD1FNRzdMZUlxRvZRRA5hQUfSqdVw2LWqQoP_u2NMCfqhG-FLq2QqMaEnIl9n4jN_FgN1uK-agITbZTRBa9jtBGJF5Enaizzau3Heyd2-tHPIn1eKfV9g4hqrPJhKg0KP-ytUpyqQFqDgx3IIqmUQwE39r2vSVdathAJ6-P90Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
انتقاد جالب میثاقی به زمان‌بندی ارائه‌شده از سوی سازمان‌لیگ‌برای هفته‌های آتی لیگ‌برتر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106767" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106764">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acdc40365b.mp4?token=joPLf4vu6nGOfl1khzBwEZXtZUR6HxQGKjcG7RXayvMMyKVSnhrFd_uVyJO7x6rWzuq7zsg1B_UybmfdXP_aQFtWL-diOMb0YwsqptpWIF_ZyT1I0nHq6DdVddVhU1UNtYSU9xoPAkvmyQC0rz6nk1ouew-xNEBDE0xhkP6jukMREDKeFuCvYIzhBwzAUzMmXgz-xtHX2K0S_xBZO-oU-ACyfI3RU0zgwUSlLuTpKSwVsjlM1TaJBmiZde34Sb5i5-h2msxh25th2akIPEsCuz1mvLBNEtvqjISpsIeK_3dqs05mPcTJRfnB7ECsyaBVjldODvPyusIpLcw3-3_4-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acdc40365b.mp4?token=joPLf4vu6nGOfl1khzBwEZXtZUR6HxQGKjcG7RXayvMMyKVSnhrFd_uVyJO7x6rWzuq7zsg1B_UybmfdXP_aQFtWL-diOMb0YwsqptpWIF_ZyT1I0nHq6DdVddVhU1UNtYSU9xoPAkvmyQC0rz6nk1ouew-xNEBDE0xhkP6jukMREDKeFuCvYIzhBwzAUzMmXgz-xtHX2K0S_xBZO-oU-ACyfI3RU0zgwUSlLuTpKSwVsjlM1TaJBmiZde34Sb5i5-h2msxh25th2akIPEsCuz1mvLBNEtvqjISpsIeK_3dqs05mPcTJRfnB7ECsyaBVjldODvPyusIpLcw3-3_4-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
واقعا چیشد که به اینجا رسیدیم که یه بازیکن فوتبال برای خودش آرزوی مرگ میکنه!
صحبت‌های تلخ بابک‌مرادی بازیکن سابق استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106764" target="_blank">📅 17:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106763">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbZpEoUixZyTjpr2wLyLDH-9Ku-EbC__j3EGWwwEFPDAPHSl2I4C02YLNVFBon79iguqvY46IuCBaZhz5b4n_qD4FTIj7vkPcHKHvobon5FwaFf6TYtagMlOlmeoCXM838GLt8r5n7Sak5SZAiqRxZdT6M6Cyil0nuTgmGV8QN_3Lmj_24lr4siAM-z7g7MFdUZSLsPpCfzJKQLf8qWxCSgaD8kzgW0FMWR0Tg39EVnFkkVUkRZTLl61KQqAlWU2h0sruLfKjg-U_BYwHjAXu6Ti8uZAD5hcfJnq90rka0r1iZxRlkeP6jGigaumHoqLedmMvn0c9OfOzSgx1sPB9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📊
🥶
کیلیان‌امباپه از زمان حضور در لالیگا به تمامی تیم‌های حاضر در این لیگ گلزنی کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106763" target="_blank">📅 16:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106762">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db11bb42ef.mp4?token=M7tTO5D5Gid7w5u8vuTRdqzvNcrhCx7aRB5LmeTb2LM7BFXer6VCcHmpLcF7issRrECk6egULxEjbo9Ymssh380tKdCoNtnKAxYvp_otMdQC_Txx_ykZrhTWnnD3WWWd8CdBF2KW35Wcz10o4FnvQL6u3tbd-wSsT1y20mnt8H6FYy468kqyc31rM6t87zJb96e4mRxzmOcdQi2hvq1SyGr4xwvcNCyDphTyyFAfXCHvmmxfZPinropMLHoyzeXkZ4hPOQCzJ6CHELBqi-iM-Wt7Hm5Bk1EQxjnkbZY60W6nqV87pI7sTSy78Cdf_T3H2kOZmpc0E9VB9VwxwPs9Notz1niq4FXrv-8QJB39DyI83jU74GBRcbmEyIhUTHOuML_D_aSiAaz7gkVU-v98JpKW0svK-uQtFzCw7BQ3-Zec7G6dHZw2BZbk_71TOqE6m6hYUHxfoLx4fT5k4XvmV5nNl96zE0QRmA5FEfM-0pkEw-TJJBuxoyQ_IERiK_Oi5qHdfhdGQT36dmlI0_KFWKlsNXH7QRWkYf-u63KOaoqnn448y1A1LVKjgGv7uiwm0vW81vXjl-XalEh1tgwI5OR70LdMbxHap4Of7WX2_pZmiQxZrFN99J-z83O1khApipTRWkNOoo61W4l7Ef5QGXzSOETORYHe_GFUBR_X7Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db11bb42ef.mp4?token=M7tTO5D5Gid7w5u8vuTRdqzvNcrhCx7aRB5LmeTb2LM7BFXer6VCcHmpLcF7issRrECk6egULxEjbo9Ymssh380tKdCoNtnKAxYvp_otMdQC_Txx_ykZrhTWnnD3WWWd8CdBF2KW35Wcz10o4FnvQL6u3tbd-wSsT1y20mnt8H6FYy468kqyc31rM6t87zJb96e4mRxzmOcdQi2hvq1SyGr4xwvcNCyDphTyyFAfXCHvmmxfZPinropMLHoyzeXkZ4hPOQCzJ6CHELBqi-iM-Wt7Hm5Bk1EQxjnkbZY60W6nqV87pI7sTSy78Cdf_T3H2kOZmpc0E9VB9VwxwPs9Notz1niq4FXrv-8QJB39DyI83jU74GBRcbmEyIhUTHOuML_D_aSiAaz7gkVU-v98JpKW0svK-uQtFzCw7BQ3-Zec7G6dHZw2BZbk_71TOqE6m6hYUHxfoLx4fT5k4XvmV5nNl96zE0QRmA5FEfM-0pkEw-TJJBuxoyQ_IERiK_Oi5qHdfhdGQT36dmlI0_KFWKlsNXH7QRWkYf-u63KOaoqnn448y1A1LVKjgGv7uiwm0vW81vXjl-XalEh1tgwI5OR70LdMbxHap4Of7WX2_pZmiQxZrFN99J-z83O1khApipTRWkNOoo61W4l7Ef5QGXzSOETORYHe_GFUBR_X7Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎙
رست‌دیفنس در فوتبال از زبان رسول‌ مجیدی از معدود مجریان باسواد صداوسیما؛ خیلی جالب و شنیدنی برای عاشقان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106762" target="_blank">📅 16:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106761">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106761" target="_blank">📅 16:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106760">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915324d20d.mp4?token=J9HikILXa3qw4XR43l3PpcpdZ2i99bxffnJHXZ5NIWsRhrPpmTPAoIC7RfRU2r_Png1iC2fUbS82C7VQPqtTHKV9-K-d2CLy6SRrmrBlPL28jwscvA0YqB22xPKy53oxlK8YkJcQXKt4nrsoxodcjGpZwKbso2f1butNHiyG_buq0uoOGyRTIqDRa3x2Vwq8cAH0hzFsU6F8kRaFe4JR8BCWcCuFprxlibCJ6Tda07kxtxevNul4f5jLwugmv55XQOgZfKnyLq4Vz4EX1xlDLeFOvslpMLIpJcb1j-aBQi9VhbC6RVlsD5LQMBKuabPJJOt0JXk3fx670YrhKEG9hbKYj700fPTptbg5PcGoAgnKec7xr3cN47yg8sVB7vWKZZtcRUx9-hNeBy0sxi1hGCtKkJXH0u7OzW-zoENniyQXOmn68TTHCz_s5NksY01e5HsNDIbMTmeW6uX7MpVNze2DQrds2-zJi9sxhbYJWUNDpPQeuj77Q6lbUGTQM_UxXltf-3MGIj-sA-rK-aNKFsw6lU-jpvieL6Sq32y1S-8rQaJITdXgx4p2OhJ6K_7LznS8K6PnLY2a0x_UDL3ipv0cay3qmCX10KhbPR4elhFBP19OZhn7tGvQoV2L9I5LP0Z-Luo3x4LLw_t4EMcO7LINvfsPfDthnjqsreGnoec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915324d20d.mp4?token=J9HikILXa3qw4XR43l3PpcpdZ2i99bxffnJHXZ5NIWsRhrPpmTPAoIC7RfRU2r_Png1iC2fUbS82C7VQPqtTHKV9-K-d2CLy6SRrmrBlPL28jwscvA0YqB22xPKy53oxlK8YkJcQXKt4nrsoxodcjGpZwKbso2f1butNHiyG_buq0uoOGyRTIqDRa3x2Vwq8cAH0hzFsU6F8kRaFe4JR8BCWcCuFprxlibCJ6Tda07kxtxevNul4f5jLwugmv55XQOgZfKnyLq4Vz4EX1xlDLeFOvslpMLIpJcb1j-aBQi9VhbC6RVlsD5LQMBKuabPJJOt0JXk3fx670YrhKEG9hbKYj700fPTptbg5PcGoAgnKec7xr3cN47yg8sVB7vWKZZtcRUx9-hNeBy0sxi1hGCtKkJXH0u7OzW-zoENniyQXOmn68TTHCz_s5NksY01e5HsNDIbMTmeW6uX7MpVNze2DQrds2-zJi9sxhbYJWUNDpPQeuj77Q6lbUGTQM_UxXltf-3MGIj-sA-rK-aNKFsw6lU-jpvieL6Sq32y1S-8rQaJITdXgx4p2OhJ6K_7LznS8K6PnLY2a0x_UDL3ipv0cay3qmCX10KhbPR4elhFBP19OZhn7tGvQoV2L9I5LP0Z-Luo3x4LLw_t4EMcO7LINvfsPfDthnjqsreGnoec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برخی از راکت‌های تماشایی سوبوسلای در لیورپول؛ واقعا عجب گل‌هایی زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106760" target="_blank">📅 16:05 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
