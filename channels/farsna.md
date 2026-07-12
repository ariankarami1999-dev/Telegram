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
<img src="https://cdn4.telesco.pe/file/O_5R1VxoJwHHpPyHiBZWQwDdYeiB6LkgetkJemPDZNoPmJ06JefkeicR0BqDiBOHhPeOIXeeUSTA24k4FzPM5nd7i7UBuvh3b_G1U59QTl0HVMpXQ2_P5QCVM-7O-d9q4miWJ9qTMH0aYMbnXYuF5HkXOQIFqX0N_-_0M68x04WiC9ufbxnZXDk5GPUePC5sDbUyB2RlcNraWOvvIcG3h2wDdkBU41Ph0u6Ymj2UUAS5tONxBTUlojpJhrrda84V1JhKycXBnAQFkwG5gu9521uNOv2t02rycHZS0ARoV0IIoPcSXqBb6bxhPDxDMldsgbehpn0XbAhTizpj7avnnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 13:13:50</div>
<hr>

<div class="tg-post" id="msg-449377">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رایگان بودن مترو همچنان در هاله‌ای از ابهام
🔹
در حالی که قرار بود از امروز طرح رایگان بودن مترو و اتوبوس‌های بی‌آرتی به پایان برسد، مشاهدات میدانی از برخی ایستگاه‌های مترو نشان می‌دهد که همچنان هزینه‌ای از مسافران دریافت نمی‌شود.
🔹
درنتیجه به‌نظر می‌رسد وضعیت…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/449377" target="_blank">📅 12:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449376">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/im1eTW6ZymUtCA-Csg6kKNkqIGg0gz3SMmjJWZgiFx0QY0WBTavJM5UiRPBJ6eMuecjqObHPNrgb8Q5fhg254jlQI13r8a_Vo9RAJ5wPvNpHj0lyvhDVVknlyApl_Nj1FzepgBk1AUfp9U50_7BseTyfZE86T-xfA-Ksnf0AAyJTAo0FmwWH3cRGxq8_WQYbQFphFfffWHUSUGmb_dUUW6eBMw7ViBPTubu7opwFv9gJQKjktZKGuxQfHyemoywI6Vy4z2vRKfZpm-uENoWvBFu6Ceep2w6mICwaxshBpi1cFKX56dK-Sl24NF2PfwcX4AdnE7s_Ujy3BGJzgX8rIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با ریزش ۱۲۷ هزار واحدی به ۵ میلیون و ۵۶ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/449376" target="_blank">📅 12:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449375">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اولویت ثبت‌نام حج با چه کسانی است؟  براساس اعلام سازمان حج، از فردا دارندگان قبض‌های ودیعه‌گذاری به‌ترتیب اولویت‌های تعیین‌شده می‌توانند برای ثبت‌نام اقدام کنند.
🔹
کسانی که در کاروان‌های حج سال ۱۴۰۵ نام‌نویسی کردند اما موفق به تشرف نشده‌اند از ساعت ۱۰ صبح…</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/449375" target="_blank">📅 12:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449374">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtiyhBvcKqvD4RfuyiYmeG67NlqxwYkSXuD_1JanemqYZVJ5qF9As_SH1peaMYY26HCrFkrGmeh4LIy1nyMcuX4dmYVfZzJjRhUzTHv6BYK3TspBZbSpam36AedcMrJmU2T7hK3IOZvF9jqBu1Ij6oOVdSzrV3GZPDSQNYTIpraB7pcRTI6pgEb199WzRtxhZdAGGc9UJZ71CE_TNRPZdvkvP2E_ZJBwMb9zEyQ_m7xwVN3X8PnEEMGDsS6fmHrOzZhiFNy2VibkbVQMb9vZdTCUDcvqg_S6vPeZ2YZ5yf3S0TELtGlLku9jO2PNVcHrRsvQ4wtBmkcjDbJPmVQSjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا پهلوی برای مرگ سناتور ضدایرانی هم عزادار شد!
🔹
فرزند شاه مخلوع از مرگ سناتور آمریکایی که یکی از حامیان اصلی تجاوز نظامی به ایران بود ابراز تأسف کرد.
🔸
رضا پهلوی پیش‌تر هم پس‌از حملهٔ آمریکا به میناب و لامرد و شهادت صدها کودک و نوجوان ایرانی، مرگ چند سرباز آمریکایی در حملات ایران را تسلیت گفته بود!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/449374" target="_blank">📅 12:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449373">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a676d04f3.mp4?token=v-UBVlXklRB14sYbHwADza2GXr1lAJow8-ItqwgppdtRceSvvhML0PXaglKNTxM-YLQiD9373XLXuUdNCzVdPDWtOhnfnFlVIY8hHOsvw1zClBtjs5xqXd6uC5BoJScdZzVFPSIftzvYh9ctgzng6Frcw5Ry0wK0tOuz6WjYzO8CqBNZyaJCYOoBH3z6B0ZkvjS1qk2bmZt0hJ_M5Nw3_1XjnD3WBk2eniea_ND7lkyC6MqS32gN4XXwEw6az93e59X7yUotz4pawgR6r0kQFmcbeDhASUPbpnottuJ5h55LJpz5_9rksdOOOVp7Y72bB1awfbcO7AZ2OaHEeSQaMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a676d04f3.mp4?token=v-UBVlXklRB14sYbHwADza2GXr1lAJow8-ItqwgppdtRceSvvhML0PXaglKNTxM-YLQiD9373XLXuUdNCzVdPDWtOhnfnFlVIY8hHOsvw1zClBtjs5xqXd6uC5BoJScdZzVFPSIftzvYh9ctgzng6Frcw5Ry0wK0tOuz6WjYzO8CqBNZyaJCYOoBH3z6B0ZkvjS1qk2bmZt0hJ_M5Nw3_1XjnD3WBk2eniea_ND7lkyC6MqS32gN4XXwEw6az93e59X7yUotz4pawgR6r0kQFmcbeDhASUPbpnottuJ5h55LJpz5_9rksdOOOVp7Y72bB1awfbcO7AZ2OaHEeSQaMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصاحبهٔ لیندسی گراهام در روز آغاز حملهٔ تجاوزکارانهٔ آمریکا و رژیم صهیونیستی به ایران: «رژیم ایران» ۲ هفته دیگر به زانو درخواهد آمد و سقوط خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449373" target="_blank">📅 11:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449372">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XubkKTv-VNG6gcEJMm3SVe_ZbRjgPuzoeqbM9CACmdTYsjekrrY9rykRKWmsAPtK0i9mgS2rvXovKTPc_m3Y1nX0Vns_hwkz5cJqEftTIKyi--uG-wdCS_t9gvq0wFrVFgCD_rfEQb5uME3-QQM2ZTc7XELQ6GXUgB8z6Sst-LFw187zzF94q74CBMtf1hzxEgsx_H2LSf6puVmQs__NQQaoeHJWzxckdKU1iT5mZx7DaXlkT2t4PsxQkHi3_0vJV9el4jR86RYakO71skanvEVuDQcxmK4Fn2RGd3rT0yDoWF50Ru2yH2amW05zPKIfZ3TJ-QmLN2a8W5y07sCf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش کنایه‌آمیز مرندی به مرگ گراهام: حیف شد؛ کاش قبل‌از رفتن به جهنم قیمت فردای نفت را می‌دید!
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/449372" target="_blank">📅 11:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449371">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4FRwHFJhf5uMRUWOQsLmybjF0EvrIltgqHvS8NOrESiq-TsoyFk_M5ofZFcJK17abHP2vI-pZVai6WdZ2zqY8eNE6YLOxCTBc-AgKzEbhSBQ2ZIuyScISUPV8JLgD19_fgovZbgQzYPx3vl5NsDhFm9BtmPz2b19kTmEtFOxM9j6HydCryg27R-g4VEexpxByHfMSEsdMbeSPsIt33o9VcUYTXBeh8_7ZZ83KqQufR830SOF93fFIBQAHUzYaLz6OIDwjKhHIauKf97ky9Vy6R2_-aNwW4h38b0DvBO4sY_1mBdAMIv1uO9aRd4xX1qdYKk-m45jLjHxOus8BZTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: فقدان لیندسی خیلی غم‌انگیز است
🔹
سناتور لیندسی گراهام، یکی از بزرگترین افراد و سناتورهایی که تا به حال شناخته‌ام، درگذشت! او همیشه پرکار و یک میهن‌پرست واقعی آمریکایی بود.
🔹
جای خالی لیندسی بسیار احساس خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/449371" target="_blank">📅 11:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449370">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIEzsydbf-4TNd5C6BxLQ5nuTbD1uy--6glVpU6LiS8qBtJk5PC7vXjsxQ-0tCDRyT_1X41fUDom1YkuwsIhfp6hOYVU_HRoJpbkKCtvVHMaW3-U24TxbKPjkcC-MOtPO3fpeHf7fUdSl_IHUySKNUDmzbEYKcs3pH3dlmyTpK1Aurtfs1FY7SYosCnCJHxXeAsFwy6Jo4cyvk9aICyQ3pVBoit07sGzCk3aJ-8JwjP4FpDKNzzYJAMwwYzLtJdMEmpezkdNZCmIr5taDlIHoaRWRmr5SItYKC9K-Zw-OZwR0962YlG7g-nT6HqEXZ2Ej7L5DBGszZnUP2j48X7S-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: فقدان لیندسی خیلی غم‌انگیز است
🔹
سناتور لیندسی گراهام، یکی از بزرگترین افراد و سناتورهایی که تا به حال شناخته‌ام، درگذشت! او همیشه پرکار و یک میهن‌پرست واقعی آمریکایی بود.
🔹
جای خالی لیندسی بسیار احساس خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/449370" target="_blank">📅 11:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449367">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
سپاه: مراکز پشتیبانی لجستیکی ناوها و سکوهای سوخت‌گیری ناوهای هواپیمابر آمریکا در بندر دُقم عمان، با یک حملۀ سنگین و غافلگیرانه درهم کوبیده شد. @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/449367" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449366">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🔴
وزارت کشور بحرین از فعال‌شدن مجدد آژیرهای هشدار خبر داد.
🔹
برخی منابع هم شنیده‌شدن صدای چند انفجار در بحرین را گزارش کردند. @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/449366" target="_blank">📅 10:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449365">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o83mtPLzoJ_LHo8TIBHULAldPZYNfvIEH6BTxOkDeJaVU5G5m6zYo8b909L4wEXHITM8Agg9yqDp0oxkflLCA_SWEZZJx3Bo61FWlMLRt3qYglZRq-GY3kokfuG7Rviiz1xjCdx-2dt8M23di0NeNgsXXZ6aCgfBDT6U-TjWKu0NC-eoCl9K_3prj83hHRihP-sEktm9dH3kV6-hwMcGb29knxcueUTjgn1FAIvbdNNZ0ddzdAE17H1uiz05vnX2Tv00RvxEdE-MOZ2wLFc77v9b2HtR40nlSXkEkI7gSRzpquxz1ffCduq9HqEbSNdSVbGKYj3nCQZp0ofdOsEj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات ان‌بی‌سی نیوز از مرگ لیندسی گراهام
🔹
شبکه ان بی سی نیوز با انتشار جزئیاتی از مرگ سناتور لیندسی گراهام گزارش داد، نیروهای امدادی شامگاه شنبه پس از دریافت گزارشی مبنی بر «ایست قلبی» به منزل وی در منطقه کاپیتول‌هیل واشنگتن اعزام شدند. تصاویر منتشرشده نیز انتقال او با برانکارد به آمبولانس را در حالی نشان می‌دهد که خودروهای پلیس و آتش‌نشانی در محل حضور داشتند.
🔹
در همین حال، این خبر در شرایطی منتشر می‌شود که میچ مک‌کانل، دیگر سناتور جمهوری‌خواه و رهبر پیشین اکثریت سنا، همچنان پس از انتقال به بیمارستان به دلیل ایست قلبی تحت درمان قرار دارد. سخنگوی مک‌کانل اعلام کرده است که روند بهبودی وی ادامه دارد، اما جزئیات بیشتری از وضعیت جسمانی او ارائه نشده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/449365" target="_blank">📅 10:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449364">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1408d2321a.mp4?token=KiGK8o5OXs5aWnxkhWXVKyQW-_ao87QbT4K2T6fCNxbVB3WS0r6T778e1Qgqqbhtzy8TWlnAPF85FewMCNGT_xkpl7N8oTxallFyCs5EtwIkmH5asx4qQLEke8mpnDIcqlbeC9kxDkC7Gjk68jC9ErTJWK9stzWhrtHhQ8Ls0G8jCc_QUhv8HrusIRYGPkaNyyF9FwDMWJATYjewU89BU9CRt1Awodp51ZInwf0UugJLgiVyKGknXc4OigOI3qKPYxoyir9tPPNnBPpxc8OdR9pVVEo3bx5yf39Iyuch-WwfLkrkVBxOOYehOyHURo17KpFujCJui8aw-zUIHSlGew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1408d2321a.mp4?token=KiGK8o5OXs5aWnxkhWXVKyQW-_ao87QbT4K2T6fCNxbVB3WS0r6T778e1Qgqqbhtzy8TWlnAPF85FewMCNGT_xkpl7N8oTxallFyCs5EtwIkmH5asx4qQLEke8mpnDIcqlbeC9kxDkC7Gjk68jC9ErTJWK9stzWhrtHhQ8Ls0G8jCc_QUhv8HrusIRYGPkaNyyF9FwDMWJATYjewU89BU9CRt1Awodp51ZInwf0UugJLgiVyKGknXc4OigOI3qKPYxoyir9tPPNnBPpxc8OdR9pVVEo3bx5yf39Iyuch-WwfLkrkVBxOOYehOyHURo17KpFujCJui8aw-zUIHSlGew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: مراکز پشتیبانی لجستیکی ناوها و سکوهای سوخت‌گیری ناوهای هواپیمابر آمریکا در بندر دُقم عمان، با یک حملۀ سنگین و غافلگیرانه درهم کوبیده شد. @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/449364" target="_blank">📅 10:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449363">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyJnFlbitho-rYZUIIrjHra5ynG8PCr57F5H9vkS75sLszQYTOVgYuaGz_V8D-4z2_exD5Ez5TrIG7MEsZPn1CWxpQhNUjxOHhEqzfdRGYZjm8eUZi-jlspycBZoyNTl6ox09D3HXdxuYZM93PYNB3q4CHfc0qjDpunSaaJt47BC7aBo3Zj0CGLoV2EM7mU2sJr4e7j8OXVaOKEWPBFmwr1uX9gc0bjr4R8OJgUsKw1c5NLopI2l1KU-GsHJdEvV1sgPiFJuVljK2pE57Hr-m2EyLoQjTeAv-Bd85vGpfjwSWqxWAAqPtNrb65kUG0s9lwA7Mdx_Qn035m9ruVPgGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوهن، وزیر صهیونیست: سناتور گراهام یکی از بزرگترین دوستان اسرائیل در واشنگتن بود. او مواضع قاطعی علیه محور ایران و نقش مهمی در تقویت پیوند اسرائیل و آمریکا داشت.  @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/449363" target="_blank">📅 10:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449362">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJ9a_Y_lSMEitz1XAswqveqzPOGwQab0s7-GSQ3KP-zduyZjM8rZlRrt4EhZ4ta3G9FZSI9v6z6lxteWkHWlKkZktP3MzgRccbwlKQQNwP0VeDQkZqb1M16x7UrXesnHJvrzVTSV3OWc-UdpUsHU4mbj1iCTfeUemBOuwXNMNMShQwjcdHP9zqCniZIrK8XP_uJo3R3hsiAhkC_pEkgk9p47JJKTqaLGNZDNoNxapSdhd1WE3M7NmaTprcfdnsYEEExq77jbLzPxyLY9GU9QxD2_pi7oAfEiGWryc8yp-bivjQx1OhH_lAP4pjDNhPdldYmgzxbfCp4M8gPs6Ik_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ رژیم صهیونیستی: دوست صمیمی اسرائیل و یکی از قوی‌ترین و پایدارترین حامیان آن را از دست دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/449362" target="_blank">📅 10:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449361">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzXvogkkdFqfZoQ-C9dHnP1kmHf6b5j21fyWEyY8fcEuFnsoYVlfZBxgK7_7VvHfFbMhWGGpcngb-hEcapgPesFN76wjU8qVSLB1DKp1WKvQEA59-OiK1-t-oEG8DSCLxsWLnL-nVMtDuMQvY3paNQ5fNfCg3pF5-4B3bMdB9zpBbXp1tTuTtXg46UGKVVeqo03HDkdklUjUR8Tok5VYpQLGGaVmhvr1HdT_tADWME5bnRrex-eOWoris8WO4Eh3k4H5koTKWybG3AgRTqIv584Gsm8yOncpVnpe9cZ7kylnLd_LfD2KoXD5ScKShMjKmpXottsSjy0cLo6v5-2iVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بنت، نخست‌وزیر اسبق رژیم صهیونیستی: قلبم از شنیدن خبر مرگ دوستم شکست؛ اسرائیل یکی از بزرگترین دوستانش را از دست داده است.  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449361" target="_blank">📅 10:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449360">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TK3SSpv8Z9d0JMKK50x-PRoMAEwUBeUFy9KnQKxABUE83_BUS2lUa3Z-AE9MHLSrldhoQHV68o6Hh4hvJQ1DQE2sY9E0eqAfLS_ipcV7pS_9QnpN6rQb8DTLjix6_dcJy_RJ1x--Nc3iEun4GNMGLwYOqhMwXO-mcmzxPhopLsPdOdLFwpq2Y29Oi9ZjWXsuQ2pqSaTrHegkzEkXpKH0OHqo5zuaKo6wHu15Qsfr45rWc2_0NotzWDTxbNwyRox0hJ5if3tH2DjGiZ8CCc3zFulGP_db5Vy5urhSgOnP95wAExr5N65Vs-XESg4SrhYlRSKJg5MaVtUJhQJuS-ojTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بن‌گویر، وزیر تندروی صهیونیست: اسرائیل یکی از بزرگترین دوستانش را از دست داد.  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/449360" target="_blank">📅 10:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449359">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">احتمال شنیدن صدای انفجارهای کنترل‌شده در تبریز
🔹
استانداری آذربایجان‌شرقی: امروز تا ساعت ۱۲ به‌دلیل پاکسازی منطقه از مواد منفجرهٔ باقی‌مانده از تهاجم دشمن، احتمال شنیدن صدای انفجار ناشی از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/449359" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449358">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCXsWuHLK9_pnKYQs8bG5oaRJ7xx3neJKRsAGIcGWJk_-8uf-AjZhcCTR2MzYO2aygzXZXJNQT1EaiSygH4XEJF3Nq9dJr3e7vBb0RbrgLXkpixaXPN1-soWMuySNzaqt7Hve5JThgp4eBU-PLxPgzKE7WgagMGBVfr0fMcOhP1qGM_gC1cQgUmeoff6OGHU7Rc4d_-PStfa7xlDqQtR35wLayZ1OLWpMQ7K38wlwo2DOadDKL7aWryA_HhR0WrdYkskum2Q-D8N3svcIwNzMQl_HE8sCgl3SnGHEXPV7lVxxagQcwDZwMFc5lfjh6i-Q6aE52_n54EHdX_eD6lBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
ارائه ارز اربعین از سوی شعب منتخب بانک شهر
🔹
فروش ارز اربعین در شعب منتخب بانک شهر آغاز شد و تا هفته اول مردادماه ادامه خواهد داشت.
🔹
به گزارش روابط عمومی بانک شهر، فروش ارز اربعین امسال نیز همانند سال گذشته به صورت دینار عراق انجام می‌شود و نرخ آن بر اساس نرخ اعلامی از سوی بانک شهر خواهد بود. بر این اساس، به هر زائر واجد شرایط، تا سقف۲۰۰ هزار دینار اختصاص می‌یابد.
🔹
در راستای ارائه خدمات هرچه مطلوب‌تر به زائران اربعین حسینی(ع)، بیش از ۱۱۰ شعبه منتخب بانک شهر در سراسر کشور مسئولیت عرضه ارز اربعین را بر عهده دارند.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/449358" target="_blank">📅 10:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449357">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmEBAXSyCkhDUZWLbtCd0tcUznWrdwowuUPBfaw8ybrT8YdU5_F1qPGQLwuJ5dGIp4ZrM5v2Gv_jEOdLI38nD3cP6kTeEmKbF4wEymF7a2NTYbMe3Fu-FIP8OzzICXT5XKoJy9-gtR6buM_kB1OA0TvVZMLGKppqac8abfFliKT5Q9V03B-cUd7DkIbxr29pjC9KDdAgt25Rfo80e_eA-aW4-riapR_BExVI3dfMV-RmBTGDsVOoR8qIpIwNgZxswRQPhnMpplZOGLF07sg4umfOSULGMkOabKFvFC_4Jm5Pz4A41kINJ4eJ9h1Ty0S_SWtsPa1sOOuL3OyuUf_0pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/449357" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449356">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/449356" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449353">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QaEq5BUeqBbPmsEFm6CZiNIpMjfUsGjKrzXdJEvS7OtR_xarMIuOYb5tsJGam1n-1G1yB5_ro79ZJGL_MMdsgrNNWPSW4034c6NpnxJgjwt_Y2SlHy_6OoSiTKijglRZEZRNex1_7GvjN5O2lMgxBIGF7K6JVN-_zkpzl2qu3NP2ni0rW-kF9zQ1YSCUrNhev46kUfsu86Z8Qiaaz63LB3NG7hcvGu_XfGledqvoQj0PPuqVv5kTgj3EttG_JXUNNZ4u1OHz3l7O1Xm9cZQ2Ir6rEjkA_8wGoD-IomM4_WiTeLvFG09iEPxDgI7og1TeSOc8n3IUJwpNtMr0dAmz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JE5rUd4qBd8w2YfCWjVo00ATU8Er_7wi3V9N-HcTWv2CfM9pEgyPOA8iYcZ_7M9nH5kAY-Cz7TNgQNapPCnYpRa8mcy51BuYPIxpXWvP8t3xAonfKJlwXJvdudarcYRfHeznBlP2mf71Rtg5WVxUxswUELBLufRQ8UHf274CifgLVncu5bRS7U5d1Pe0ZIGM02tXN66w_F4rOiA-I7CvwBU_OqXacPFC7Kn_3Lk-WL9PaR-VclJOb-0BE4srSHnk6gmDbpRimffUxvYMSimrivwvlxxgfXrwdPheeFCcUqo9dai07FvCpvWxv-pGIU2ANldqQzB0zTau9ImaRJniqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjtvofmuxNvqYE1wo08MRuetgWznp8jzeTfhUpIU9Uf2gCWuwYrOThjASGgcnL13MbPrEmiY49GBsCxOt-dFVyfcN32qFxqwoVZTuB2oIA6qUUJ25mS___qH2_C_jtuH_3Jpi9cdzIsmwCutzCOZ5-IsompFJdvOepj5tLeYjF4QV1pB-JlKy-KjN3GOqQwoosEVp4YmJAblcLgdx8ClrNumLfnloCDVf9_QzWNapEDxzbiC_axL99neh2pO5-Xe6jczGsc9fs2PNwhFvLdhODx-tdwL2wYBEa2mVOdzRgr9rHlcHq3K_BRwNnDInR2UOct_P__x57zx8eMYx5CmvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آخرین اقدامات علنی گراهام قبل از مرگ: دیدار روز جمعه با ولودیمیر زلنسکی و بازدید از تاسیسات پهپادی اوکراین
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/449353" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449352">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iehb-917iqEgb6WBajOTh4MFErQTdeLq2-MMToTxKaDruS_Z2TR93irWcMLjPrjPgHC_8z3lxuvo2gdJY1FNzi_Vx5Ns0Tc8qC9eNzGOtVRut0UROJgoa4JnsjGSwMmwfgO6MqX031qGoLanvLYufyEPLfwq-DGHk9rHTlKtn-UNPPx5bgLYPgsm4qtc-TLGPOyXIbqXEl87U5Z_6aR5sF7nxVvVlKrLIaNDsr-fq1nkmIeWgEt0p310G4IyXEe1jmFomhxihzOBwH4bx_cdP9zjv6LC9hXqqD_jZKij06S7In7r-vsuLqVNgEiR_t6YCZPoUnVcbCBDThOIdpcJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرگ ناگهانی سناتور ایران‌ستیز و اسرائیل‌دوست آمریکایی
🔹
دفتر لیندسی گراهام، سناتور جمهوری‌خواه و جنگ‌طلب آمریکایی اعلام کرد که او بر اثر یک «بیماری ناگهانی» مُرده. @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/449352" target="_blank">📅 10:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449351">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌
🔴
منابع خبری از شنیده‌شدن انفجارهای شدید در کویت و بحرین خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/449351" target="_blank">📅 10:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449350">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5KL7727YVFxVVXSgVNeWIuQ69fpTrs5v24bMdbeXaQH4smICMpiQ75M8m3W5HtzhWQMxcvS31IOHj0HyLOUvkT8_N4rLVuqEzsvZh_SY4QnvCC30z3v7ErSP6hYaVoXI0US2GQezPjKUF8fCeKU9bMJ5Igfn5XJPY15v26Nt61eL1CkpAeYESOVxagQB1vuf0tfLl29aiimcY7AR8ZwN896Fq-DDXovQEyx2FHdAeyVmmTCRoAsa-_Hzml0xyOVBpUjg6n06LcLLsWF2HRduk3GpdWw69Py6UxyEzAbkSXc0tHmadi5dEYLiuusi0hOQQ_RZQmAGAgBpVEiWiG42A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شلیک‌ِ اخطار نیروی دریایی سپاه به کشتی متخلف
🔹
نیروی دریایی سپاه: در اطلاعیۀ قبلی گفته بودیم مداخلات بیگانگان و تعیین مسیر غیرقانونی حرکت کشتی‌ها در تنگۀ هرمز، برخورد قاطع ما را به‌دنبال خواهد داشت و روند افزایش ترددها در تنگه را با اخلال مواجه خواهد کرد.…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/449350" target="_blank">📅 09:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449348">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2DYP48onq11QaN8ClRVmkuCXZ9ZLhwOeSXnkN9_9QlY2QpkPFFdm09cTDUgwAkpbijBIu48OM8JA8S236gpHVjbNTgvR8c0_8f53PCzqLCWjRjDnC9yPFBOUFEqbr7RimylnZS5NGr5Pe1d_V4Jyh6juR9f8PcVHDbnzdntX9XrzwQH5f7G1NzTYOF5qWYFEiJ3zHY6fmNqZINhW1fR_i_EK43rcaLdwJTcfkj3zngMV3cLQ98xb86m5YE6nm2c4p0e6qJPp0f08Ks0yv7tAEJqGeCpFyp-BArzkHNJ7OEsmxJOtlw2CfcmllINM09rr8E3B7G3PM-YBEJDZmZbMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرگ ناگهانی سناتور ایران‌ستیز و اسرائیل‌دوست آمریکایی
🔹
دفتر لیندسی گراهام، سناتور جمهوری‌خواه و جنگ‌طلب آمریکایی اعلام کرد که او بر اثر یک «بیماری ناگهانی» مُرده.
@Farsna</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farsna/449348" target="_blank">📅 09:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449347">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyRM3BxGk0gp4b0XE_RwdWu6fTiGS-n2-jvqmPL6zvX2cJIY54ZXZoukBuhOEepUrl-T9ev7lmbiab3IHVChCFtUDQQttSf949ubGxfc_OFuVAsUCgHseRureUS40-HcbF4wCJ0d-EHff9p8biTpDUoSoeevlUfD3uqdWihB1-von-r7SK7J8MQ55ED8-mgA_DbxDAQXvjy3xx-dTjDaO5banbLSPpxrRv7Naic4gRJLHEQ6DBipRbKTaWyvdEk_xZ37KJbaM5JTfyKfCrNg0SDyOzE609iS3j3bVqdi-y8Zuf1YzVcEVl_r09GEmGRcVO41a75dITIMIloxMXNVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی با استقبال مقامات عمانی وارد مسقط شد.  @Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/449347" target="_blank">📅 09:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449346">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک نقطه در خنداب هدف حملهٔ دشمن قرار گرفت
🔹
معاون امنیتی استانداری مرکزی: صبح امروز یک منطقه در خنداب، مورد اصابت پرتابه‌های دشمن قرار گرفته است.
🔹
برآورد دقیق خسارت‌های جانی و مالی در دست بررسی کارشناسان مربوطه است؛ جزئیات تکمیلی متعاقباً اطلاع‌رسانی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/449346" target="_blank">📅 09:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449345">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مراسم بزرگداشت امام مجاهد شهید در مصلای تهران از سوی رهبر معظم انقلاب سه‌شنبه برگزار می‌شود
🔹
دفتر مقام معظم رهبری در اطلاعیه‌ای اعلام کرد: به‌مناسبت شهادت قائد عظیم‌الشأن انقلاب اسلامی و اعضای خانوادهٔ عزیز ایشان و همچنین با خضوع و خشوع در برابر عظمت و شکوه تاریخی ملت مبعوث‌شده در بدرقهٔ آقای شهید ایران، مراسم بزرگداشتی از جانب رهبر معظم انقلاب اسلامی، حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای(مُدَّ ظلُّهُ العالی) سه‌شنبه ۲۳ تیر ۱۴۰۵ از ساعت ۱۷ تا ۱۹ در شبستان مصلای امام خمینی(ره) تهران برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/449345" target="_blank">📅 09:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449344">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCnYBQtlkaFw1G11qV4J5E-qBKLZF_UxqwSsNRLQ5vilce5pTT5TaeiaX-NS0oNcMQJZtqmUKQQhZVvNBCFRPACn6ZRYj8enjBEAYcXHi12DcfwFqli-_0AmMChzcqMdfH9Gm8rCFIn_I6qhnmCbfHI9lN8lTB8opBJ37niYsX9I_6Zt3kDckQuO5wuy4ep8ud1Z14w0XZOXMEsHGXrM044Vt4ghsApNZAQwTbRoKCXQaHJ8WF98mTN_llniyYubwopu7-SX5M8jvMs4qep29gTTDTnYVOSJa9q0LN-yXGUwbAYr0PeNyTh_T7hWwnFIFTpwZi72PXEj9B8OMAJOJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوت امیر سابق قطر
🔹
دیوان امیری قطر، نهاد عالی دولتی این کشور، روز یکشنبه اعلام کرد که امیر سابق این کشور شیخ حمد بن خلیفه آل ثانی،  در سن ۷۴ سالگی درگذشت.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/449344" target="_blank">📅 09:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449343">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c425861fa.mp4?token=BQl_6BWGc7ynaMBXRhB_lgRIaMgi4pHJXnAHQzChyXldXhnA3jqxCG76SS5Rr2PmXb_UikIe-2lRPiEaCIVVEFS-KQN5I6SRb6EqEeyZQjoUfv1O5dsdXvV6VhnFvNvJuQykjSE4rYPzTo2rISmd5dzXYaULIQH3jJc76nagbowIR1P9hH-_HphqlBlq2_rbjo_1DQXz6edXFFtlMZ8UjU5Bp5yQjsVbEQStk7brLbq7DKhGCgiv2IPOlsJ0BQNmr0sHe-oisr2Qcg8zBiYFNc5p6BscZ4Y6FnWj7lLwBIMamG-LXIR4M8o8xegbdBeLuy8YTyx4Rm07FiGsb54lyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c425861fa.mp4?token=BQl_6BWGc7ynaMBXRhB_lgRIaMgi4pHJXnAHQzChyXldXhnA3jqxCG76SS5Rr2PmXb_UikIe-2lRPiEaCIVVEFS-KQN5I6SRb6EqEeyZQjoUfv1O5dsdXvV6VhnFvNvJuQykjSE4rYPzTo2rISmd5dzXYaULIQH3jJc76nagbowIR1P9hH-_HphqlBlq2_rbjo_1DQXz6edXFFtlMZ8UjU5Bp5yQjsVbEQStk7brLbq7DKhGCgiv2IPOlsJ0BQNmr0sHe-oisr2Qcg8zBiYFNc5p6BscZ4Y6FnWj7lLwBIMamG-LXIR4M8o8xegbdBeLuy8YTyx4Rm07FiGsb54lyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: مرکز فرماندهی و کنترل و آشیانه‌های پهپادهای MQ9 در پایگاه آمریکایی پرنس‌حسن اردن منهدم شد
🔹
اطلاعیۀ سپاه: رژیم جنایتکار آمریکا با تحمیل ارادۀ خود به حکومت پادشاهی عمان، شب گذشته تلاش کرد بار دیگر آزموده را بی‌آزماید و با تحریک چند شناور، مسیر غیرقانونی…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/449343" target="_blank">📅 09:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449342">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌
🔴
وزارت کشور بحرین: آژیرهای خطر به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/449342" target="_blank">📅 08:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449341">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اصابت پرتابهٔ دشمن به ویسیان در لرستان
🔹
استانداری لرستان از حملهٔ هوایی صبح امروز دشمن آمریکایی-صهیونی به ویسیان، از توابع شهرستان چگنی خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/449341" target="_blank">📅 08:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449340">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20121c07f8.mp4?token=uim--37sPE1aV-C_Gbhm2C810RX4YY8jvyBX8eb1V5J7JgeusBmXGaDC4C5gNIgjcrHf78vmm6sS-iArMHMXz49y-d1A_-A74Be-T80p-HjETx4RRXbZkXEfULXrpLZExAQbUvTk2iSh50_8KGjkjb6FcvmrfHHwl3vgaN5rFTSVOnz8CChpWIzoxTCMi8Y1afzp0WUt3n6Y3ncm1fBtWND8I5-DVg7chN7MAgjDlI-5yyYFTzk5TFJ64X78N9uhBsOPRv62YMvyasEKZewx-3JhskkCc-LNVflUZMZ5De3a25QV3goOCw1n1Qj8coTdfiFvgGFG6u2zY3XSB6QIbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20121c07f8.mp4?token=uim--37sPE1aV-C_Gbhm2C810RX4YY8jvyBX8eb1V5J7JgeusBmXGaDC4C5gNIgjcrHf78vmm6sS-iArMHMXz49y-d1A_-A74Be-T80p-HjETx4RRXbZkXEfULXrpLZExAQbUvTk2iSh50_8KGjkjb6FcvmrfHHwl3vgaN5rFTSVOnz8CChpWIzoxTCMi8Y1afzp0WUt3n6Y3ncm1fBtWND8I5-DVg7chN7MAgjDlI-5yyYFTzk5TFJ64X78N9uhBsOPRv62YMvyasEKZewx-3JhskkCc-LNVflUZMZ5De3a25QV3goOCw1n1Qj8coTdfiFvgGFG6u2zY3XSB6QIbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
وزارت کشور بحرین: آژیرهای خطر به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/449340" target="_blank">📅 08:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449339">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
منابع خبری از حملات جدید علیه بحرین گزارش می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/449339" target="_blank">📅 08:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449337">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
سخنگوی ارتش: آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
🔹
امیر سرتیپ اکرمی‌نیا: مداخلات آمریکا برای ایجاد مسیر غیرقانونی در جنوب تنگۀ هرمز باعث ناامنی شده است.
🔹
ما موظفیم برای تأمین امنیت منطقه و تأمین امنیت عبورومرور کشتی‌ها تلاش کنیم.
🔹
نیروهای مسلح مقتدرانه از حقوق مردم ایران در تنگۀ هرمز دفاع می‌کنند.
🔹
بانک اهداف نیروهای مسلح دائما درحال بروزرسانی است.
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/449337" target="_blank">📅 08:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449336">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
منابع خبری از حملات جدید علیه بحرین گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/449336" target="_blank">📅 08:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449335">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8QN1oWo8S8mmXso3uYRXbE6GZHKVucuabI04t7-0sByKpVca9ctTUm8jWscLMtrQA2p7mABn0TYa70NPx4dBRGLLE1RXUh2g_xZ2LQhn6fRK4rxW72hn33SiD2HzO26VgfPdi8RxZuFa2lSH3p3QXxW8Ljd3b1ewtA93qJ3dCoIsiY-Y-pFYt54iuUJeoyOSNPcmHu5TAMfOKlR27ATVaiwPi8y6Sv14GWbtINintHDjlkhgIX2sKR-BkIY6iSxF67UmgcFrnuPUefHMrSCiAz375Kwmy90WHn2x8uK3dd4tfWxe_gulItJOo0p7cjxZs2fVK9dLvD-P35UMM_UZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بلند شدن دود از پایگاه دریایی آمریکا در بحرین، در پی حملات ایران  @Farsna - Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/449335" target="_blank">📅 08:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449334">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌
🔴
وزارت کشور قطر از ادامه‌دار بودن حملات موشکی خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/449334" target="_blank">📅 08:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449333">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار مجدد در بحرین
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/449333" target="_blank">📅 08:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449332">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE-BCY_y11UCut-v53QS1keBV8rBj5-oGNqijT65OPYT1yGLU_x20J4El5BqmC-gU8oAfCTc2XZhFK7HnZGPvclMiyr4OIQighxW2Bv2QIjkGjTCa5PwR34UzUCfJ1ZNU2byjU5p3wjhXwDUhNj97hCNRJezcYqHXKEth8vUNK4cHrDI6BLFuJmeBli7AH5PDbGFulnbtATPSe_dHDFy-OEJEML5lcBc2Y91M5y1FfAlgFtU5EcoOWa_MR0qW3VNEi_pwq3_Ral_PjFG0ZbSWLS82jIF_qaCFRMzmYmHdBaBW1HLIw5kuiUVs7nCYwMnumGwW0EutqcnX1xKEj8nGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم به قول و تعهداتتان عمل کنید وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبه‌رو شوید
.
🔸
همچنین او بخشی از بند پنجم تفاهمنامۀ ۱۴ بندی را که در آن بر بازگشایی تنگهٔ هرمز با رعایت «ترتیبات ایرانی» تاکید شده است، در ضمیمۀ توییت خود منتشر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/449332" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449331">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
منابع عربی: صدای انفجار در قطر و بحرین هم‌چنان شنیده می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/449331" target="_blank">📅 07:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449330">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
منابع عربی: صدای انفجار در قطر و بحرین هم‌چنان شنیده می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/449330" target="_blank">📅 07:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449329">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
آژیرهای هشدار در کویت به صدا درآمدند.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/449329" target="_blank">📅 07:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449328">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
سپاه: مراکز پشتیبانی لجستیکی ناوها و سکوهای سوخت‌گیری ناوهای هواپیمابر آمریکا در بندر دُقم عمان، با یک حملۀ سنگین و غافلگیرانه درهم کوبیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/449328" target="_blank">📅 07:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449327">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چندین انفجار پی‌درپی در قطر
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/449327" target="_blank">📅 07:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449326">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
منابع خبری از شلیک موشک به سمت ناوهای آمریکایی در دریای عمان خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/449326" target="_blank">📅 07:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449325">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
منابع خبری از شنیده‌شدن صدای انفجار در قطر خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/449325" target="_blank">📅 07:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449324">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWhYM8yzYYBfJgDtQGw68dAng0nXmwxAcOiv0ayyNqabVETlyL2jLrWjp2SEFIoZTI7UgBmGaan9yIMLrSzvFEFfPteqKpe2rTk0cVK62qndpUjQKMMaidnw-4JPMnNBTKbtT2I3yPqW7lvdp1WdDrkP1oTQEJo2XSHHQsiSyFES5BxiRtNXAW_Zzvb6shnDVE62z8ltVCb4vhW1ysWCSy9-CojZRch0LR_z6AALIeHBZ65nAIg3dZqVxCbgesi-aubWbUBGHyags7mCcsIwHV67mseptIfXVf1OtccQ9MLQ8MS7HCoUu-FBcU50ulRjKf5-vTZFYRWgkHKRSQlSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرژانتین با عبور از سوئیس به نیمه‌نهایی رسید
⚽️
آرژانتین ۳ - ۱ سوئیس
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/449324" target="_blank">📅 07:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449323">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
سپاه: دومین شناور متخلف در تنگه هرمز مورد اصابت قرارگرفت/ مرکز فرماندهی نگهداری جنگنده‌ها در هم کوبیده شد
🔹
در پاسخ به ادامۀ تجاوزات ارتش کودک‌کش آمریکا به پایگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی ایران، علاوه بر اصابت و متوقف‌سازی دومین شناور متخلف در تنگۀ هرمز، پایگاه هوایی راهبردی آمریکا در العدید قطر در مرحلۀ دوم عملیات مقابله به‌مثل هدف موشک‌های بالستیک قرار گرفت و مرکز تعمیرات و نگهداری جنگنده‌های مرکز فرماندهی این پادگان درهم کوبیده شد.
🔹
دشمن آمریکایی-صهیونی بداند، استمرار تجاوزات او پاسخ‌های کوبنده‌تر را در بر خواهد داشت. بجنگ تا بجنگیم.
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/449323" target="_blank">📅 07:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449322">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be502e4e4.mp4?token=VtvejXhfypa5djMZX_aruq76Etw_DtVi7UtdtegdjtzuPXoPHHIJin1AN_wirJTlQr807i7Oyo4D8Ldwr498Hc5YSs90C8OVdMvRGKza_jzY3sqsmlqivboLbmtW9O_5RVWtjI7OPKkuz8rEOQIpJr4g6BFPHQRkZQOu4rBB1g2XrvUqCaAw0X4mWr7ypc-KwS9bmIBUySfEjbjsve5OvRg1P7qPIs1XTJsXnmdlbQT2HuyKeUduV61UTm_-CkpQShWK9bua7E4JF5OLxRd4M7ydErEY_P0a412lZ0wda_U9n2G1eTR2sC8quLAFxjVRajKFc7eUPFkvi970tttkmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be502e4e4.mp4?token=VtvejXhfypa5djMZX_aruq76Etw_DtVi7UtdtegdjtzuPXoPHHIJin1AN_wirJTlQr807i7Oyo4D8Ldwr498Hc5YSs90C8OVdMvRGKza_jzY3sqsmlqivboLbmtW9O_5RVWtjI7OPKkuz8rEOQIpJr4g6BFPHQRkZQOu4rBB1g2XrvUqCaAw0X4mWr7ypc-KwS9bmIBUySfEjbjsve5OvRg1P7qPIs1XTJsXnmdlbQT2HuyKeUduV61UTm_-CkpQShWK9bua7E4JF5OLxRd4M7ydErEY_P0a412lZ0wda_U9n2G1eTR2sC8quLAFxjVRajKFc7eUPFkvi970tttkmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: مرکز فرماندهی و کنترل و آشیانه‌های پهپادهای MQ9 در پایگاه آمریکایی پرنس‌حسن اردن منهدم شد
🔹
اطلاعیۀ سپاه: رژیم جنایتکار آمریکا با تحمیل ارادۀ خود به حکومت پادشاهی عمان، شب گذشته تلاش کرد بار دیگر آزموده را بی‌آزماید و با تحریک چند شناور، مسیر غیرقانونی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/449322" target="_blank">📅 07:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449321">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f88fbf80.mp4?token=IYILEE8fiy1Im972YQCQFVwDZibVB2fLtnk3jQ7LfUWdyZOeOJkzduVjGwiIZyjsHIZNZpWjrb6DVg46H5jsyERBEOyPX67LwlnLxHhKU_7vkcw-q0tJXA1VQKHqyW5X4acM1cDFJtCooVXhGMj5epVJ1WHs55CnsMNzmjVdOhfBC4P9Anzf7sDK3xxghu47zCovN9y1n97uE0OXu-JlhVRyIsE1Fahl3PjIK7eoPGnHzJh9PXHwomLO5LPk3qnKPXwX-VG82W93ihyVZhfooo0sbZrZubmqZN_j1e8hhggod1mMhxxNG71OqjoQLS2QpmRGmoXO_HnbaKrjgbTEyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f88fbf80.mp4?token=IYILEE8fiy1Im972YQCQFVwDZibVB2fLtnk3jQ7LfUWdyZOeOJkzduVjGwiIZyjsHIZNZpWjrb6DVg46H5jsyERBEOyPX67LwlnLxHhKU_7vkcw-q0tJXA1VQKHqyW5X4acM1cDFJtCooVXhGMj5epVJ1WHs55CnsMNzmjVdOhfBC4P9Anzf7sDK3xxghu47zCovN9y1n97uE0OXu-JlhVRyIsE1Fahl3PjIK7eoPGnHzJh9PXHwomLO5LPk3qnKPXwX-VG82W93ihyVZhfooo0sbZrZubmqZN_j1e8hhggod1mMhxxNG71OqjoQLS2QpmRGmoXO_HnbaKrjgbTEyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
وقوع انفجارهای دوباره در بحرین
🔹
منابع خبری گزارش دادند که مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین هدف اصابت موفق حملۀ هوایی ایران قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/449321" target="_blank">📅 06:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449320">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
وقوع انفجارهای دوباره در بحرین
🔹
منابع خبری گزارش دادند که مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین هدف اصابت موفق حملۀ هوایی ایران قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/449320" target="_blank">📅 06:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449319">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d674470e9c.mp4?token=mzItUD4qsvcr6Zw5NUYYOaR6tzZ5aReiBrnW1qpcw1nyDSffVYY8yJz7ktg6SghyIcqoZ2v2JiMZZIISyFrGAZtMaqdjOfYKKnsEcseZOFQtWLjp7FVZHZGeeqM07HbEJ7O_LGB107su_MyZTL5mEOgS2MwLBTLyuftvv45UljfUABL2jyUjN6OaJOW52M4QLT4_91EGobquLwrOqOLwa3vEst7NSqY9VlARleubphZQbDV1nw2wqo3z1gLEr0q9AE6QvjUTro3MPy2ynyiEbnumswQ_27C1MKiq2k5pJO1gCRg6YK-xoIcw3gqfC9FADW7PRmW68lp9oK5ZQFhCtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d674470e9c.mp4?token=mzItUD4qsvcr6Zw5NUYYOaR6tzZ5aReiBrnW1qpcw1nyDSffVYY8yJz7ktg6SghyIcqoZ2v2JiMZZIISyFrGAZtMaqdjOfYKKnsEcseZOFQtWLjp7FVZHZGeeqM07HbEJ7O_LGB107su_MyZTL5mEOgS2MwLBTLyuftvv45UljfUABL2jyUjN6OaJOW52M4QLT4_91EGobquLwrOqOLwa3vEst7NSqY9VlARleubphZQbDV1nw2wqo3z1gLEr0q9AE6QvjUTro3MPy2ynyiEbnumswQ_27C1MKiq2k5pJO1gCRg6YK-xoIcw3gqfC9FADW7PRmW68lp9oK5ZQFhCtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه شلیک موشک‌های آمریکایی هیمارس از خاک بحرین
🔹
کاربران بحرینی با انتشار این ویدئو نوشته‌اند که دولت بحرین به طور آشکارا خاک خود را برای حمله به ایران در اختیار آمریکا قرار داده و نباید نسبت به حملات ایران معترض باشد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/449319" target="_blank">📅 06:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449318">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
سپاه: مرکز فرماندهی و کنترل و آشیانه‌های پهپادهای MQ9 در پایگاه آمریکایی پرنس‌حسن اردن منهدم شد
🔹
اطلاعیۀ سپاه: رژیم جنایتکار آمریکا با تحمیل ارادۀ خود به حکومت پادشاهی عمان، شب گذشته تلاش کرد بار دیگر آزموده را بی‌آزماید و با تحریک چند شناور، مسیر غیرقانونی در جنوب تنگۀ هرمز ایجاد کند، که با پاسخ قاطع نیروی دریایی متوقف شد.
🔹
ارتش کودک‌کش آمریکا برای جبران این شکست دست به حملۀ هوایی علیه تعدادی از پایگاه‌های ساحلی و دکل‌های مخابراتی در سواحل جنوبی زد. همانطور که وعده داده بودیم بلافاصله پاسخ کوبنده تجاوز خود را دریافت کرد.
🔹
رزمندگان غیور هوافضای سپاه پایگاه‌های نظامی آمریکا را هدف قرار دادند. در مرحلۀ اول این پاسخ زیرساخت‌ها و تاسیسات مهم نظامی در پایگاه هوایی پرنس حسن اردن را هدف قرار دادند و مرکز فرماندهی و کنترل این پایگاه و آشیانه‌های پهپادهای MQ9 را با چند فروند موشک بالستیک در هم کوبیدند.
🔹
ادامۀ تجاوز آمریکای عهدشکن پاسخ های شدیدتر را به دنبال خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/449318" target="_blank">📅 06:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449317">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
صدای انفجار در بحرین
🔹
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های آمریکایی در بحرین خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/449317" target="_blank">📅 06:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449316">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">قطر هشدار امنیتی صادر کرد
🔹
وزارت کشور قطر اعلام کرد: سطح تهدید امنیتی هم اکنون بالا است و همه شهروندان باید در خانه‌ها و مناطق امن باقی بمانند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/449316" target="_blank">📅 06:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449315">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
منابع عربی: انفجارهای متعدد در پایگاه‌های نظامی آمریکایی امارات و قطر همچنان ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/449315" target="_blank">📅 06:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449314">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
صدای انفجار در قطر
🔹
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های نظامی آمریکایی در قطر خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/449314" target="_blank">📅 06:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449312">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
صدای انفجار در کویت
🔹
منابع عربی از شنیده‌شدن صدای دو انفجار در کویت خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/449312" target="_blank">📅 06:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449311">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌ وزارت کشور امارات: پدافند هوایی در حال مقابله با تهدیدات موشکی است.  @Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/449311" target="_blank">📅 06:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449310">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
گزارش‌های از وقوع انفجار در امارات   منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های نظامی آمریکایی در امارات خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/449310" target="_blank">📅 06:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449309">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
صدای انفجار در قطر
🔹
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های نظامی آمریکایی در قطر خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/449309" target="_blank">📅 06:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449308">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
گزارش‌های از وقوع انفجار در امارات
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های نظامی آمریکایی در امارات خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/449308" target="_blank">📅 06:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449307">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
صدای انفجار در بحرین
🔹
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های آمریکایی در بحرین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/449307" target="_blank">📅 06:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449306">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
صدای انفجار در کویت
🔹
منابع عربی از شنیده‌شدن صدای دو انفجار در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/449306" target="_blank">📅 05:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449305">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
شلیک‌ِ اخطار نیروی دریایی سپاه به کشتی متخلف
🔹
نیروی دریایی سپاه: در اطلاعیۀ قبلی گفته بودیم مداخلات بیگانگان و تعیین مسیر غیرقانونی حرکت کشتی‌ها در تنگۀ هرمز، برخورد قاطع ما را به‌دنبال خواهد داشت و روند افزایش ترددها در تنگه را با اخلال مواجه خواهد کرد.…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/449305" target="_blank">📅 05:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449304">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
برخی منابع از فعال شدن سامانه‌های پدافند هوایی در اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/449304" target="_blank">📅 05:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449303">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
معاون استانداری خوزستان از اصابت پرتابه‌های دشمن به مناطقی از استان خبر داد
🔹
تا این لحظه شهرستان‌های هندیجان، ماهشهر و آبادان مورد اصابت پرتابه‌های دشمن قرار گرفته‌اند.
🔹
تیم‌های امدادی و کارشناسی در حال ارزیابی ابعاد حادثه هستند و اخبار تکمیلی پیرامون جزئیات این حملات، میزان خسارت‌های مادی و آمار مجروحین احتمالی، متعاقباً و پس از جمع‌بندی دقیق به اطلاع عموم خواهد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/449303" target="_blank">📅 05:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449302">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/355a926ad4.mp4?token=BZn-f_pPgDoHDLBcFAbRswxzKI4AWDsIEydwevq8Kkuyo5L1UmjD4gnj7wXO-ASvCYTFHg9os0q5Q2UZLT5HPecJaqKcdASFXs7g9hGzaqzj6UFzDwii2j9DkdSqDIH9d0HbBiZ4dGBwv69aYoRmpV0HT9dIxEbmPrLTrC1Rm8wczAiHk2AmooqR4ia9jcQ08QeoZT-ZKsgl6znRxASRJYKAqYv2msaba8Kvu83VTEYtqsE7h1WeMfB4UB4_Rnp-Noe8alboB6z1sPo5zFQRqYYQa9qi7a3QH34oQmMDz7V4bGbPtlh58SpuFIpAvZ2RWWKg5t1Y3Y3TMyBdjV_obQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/355a926ad4.mp4?token=BZn-f_pPgDoHDLBcFAbRswxzKI4AWDsIEydwevq8Kkuyo5L1UmjD4gnj7wXO-ASvCYTFHg9os0q5Q2UZLT5HPecJaqKcdASFXs7g9hGzaqzj6UFzDwii2j9DkdSqDIH9d0HbBiZ4dGBwv69aYoRmpV0HT9dIxEbmPrLTrC1Rm8wczAiHk2AmooqR4ia9jcQ08QeoZT-ZKsgl6znRxASRJYKAqYv2msaba8Kvu83VTEYtqsE7h1WeMfB4UB4_Rnp-Noe8alboB6z1sPo5zFQRqYYQa9qi7a3QH34oQmMDz7V4bGbPtlh58SpuFIpAvZ2RWWKg5t1Y3Y3TMyBdjV_obQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پول و مقام لایق هدف‌شدن برای زندگی نیستند
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/449302" target="_blank">📅 04:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449301">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در جاسک
🔹
دقایقی پیش مردم جاسک صدای چند انفجار شنیدند، که منشأ آن هنوز مشخص نیست.
📝
اخبار تکمیلی متعاقبا منتشر می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/449301" target="_blank">📅 04:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449300">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
معاون سیاسی امنیتی استاندار بوشهر: در حملات دشمن تروریستی امریکایی-صهیونی به شهرهای استان بوشهر شامل شهرهای بوشهر، عسلویه و دیر تاکنون گزارشی مبنی بر مجروحیت و شهادت مخابره نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/449300" target="_blank">📅 04:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449299">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126027adfd.mp4?token=b_D8QsT95QgNgAFFBeCFvy1O7jXU71tBF2T7ijmiTbtQPbNVHZFeQSlvWLwLHZFQuV0l01d74HMfgw9k_YyLrsBArL84SZpKpDBwBZsmFRcy8nkI0V1jvR9JuuwYdVWXGEnZBTrdAGNu-6CJNEWgxwhqsu2PhD1NcqOw4XfZeqN2wQB7r8w890qm_4veDAyuNf2xEJPi4weNObdEuPKwdFUqPcoV8nIa8Atef675F8JzJIs2GXQNgXNyeYve-j2KZdjrWs0MLWAsTQM-OYih1oHva8EvWzuf5ntIv7OCodwCGulhJRWlID7ObV9e3P3jIxYuYFV411Wu4shnKJkk7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126027adfd.mp4?token=b_D8QsT95QgNgAFFBeCFvy1O7jXU71tBF2T7ijmiTbtQPbNVHZFeQSlvWLwLHZFQuV0l01d74HMfgw9k_YyLrsBArL84SZpKpDBwBZsmFRcy8nkI0V1jvR9JuuwYdVWXGEnZBTrdAGNu-6CJNEWgxwhqsu2PhD1NcqOw4XfZeqN2wQB7r8w890qm_4veDAyuNf2xEJPi4weNObdEuPKwdFUqPcoV8nIa8Atef675F8JzJIs2GXQNgXNyeYve-j2KZdjrWs0MLWAsTQM-OYih1oHva8EvWzuf5ntIv7OCodwCGulhJRWlID7ObV9e3P3jIxYuYFV411Wu4shnKJkk7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندۀ خبرنگار صدا‌وسیما از جزئیات و تعداد حملات به شهرهای بوشهر، کنگان، دیر و عسلویه   @Farsna</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farsna/449299" target="_blank">📅 03:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449298">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a42113266c.mp4?token=LwGgEGg21zbAQh1-OyZezT5iuCTRVAFN2khcZGpG8cIbFDTOXubmJZdDzFczVpg2F8UDdSBAeclE_8onW4w1WUDS8fttFhGOJRfsm6eWhNgnnTjxQT0aVeLTMKcueyFumUiSfap-cPfv8L6DfzDLxqyJQw1jxAjrDbwF0i3GAUDxUcmoFg7cbSZByx4hBPqKsRPFE3HAoz7aTOCCdWbxRNcTIiuNaFb1bs85eF3NYh2eA524XEFxLqk_oH67zpB6-fFZLx5fvFCdTLV_DSs5cO7cJPyH4j4xtO3o_qRG4TAjhq8qRSXMcYfEcqEqi8X7N0OxT9PEyiA9h7GvYZ1uB3mDJtMxoUpdEGLcoOEZoC145v4V4bsWDuHB2GqhyN_mKTpm52JEYIDAd_yt1CNxEq3vPsk2S6pSsMAsjW5kIc7gr3ivfTS_TDQl0KiQ55Pte7IyKFpPhNwmIFTn7VFJqrUeRFQQAewVMR63XQGTf2ry_k_qbJy-j2qkuRBwNpnW2GirpyyKVbW50BOv3F8u7UnbDKawcgOyhB4gcArq-knEdMG3B3P1M8Alskqzh9sSyDfkopn9aTuQM2fOWdg6vXHJag0v4eiaWWFyF9ey35CNCRJE_A7SXTfvSoRG5aiBXTe31wnpQ7kAW-5B94pqXo9UuuvIZ3JfsFjBpzMzs4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a42113266c.mp4?token=LwGgEGg21zbAQh1-OyZezT5iuCTRVAFN2khcZGpG8cIbFDTOXubmJZdDzFczVpg2F8UDdSBAeclE_8onW4w1WUDS8fttFhGOJRfsm6eWhNgnnTjxQT0aVeLTMKcueyFumUiSfap-cPfv8L6DfzDLxqyJQw1jxAjrDbwF0i3GAUDxUcmoFg7cbSZByx4hBPqKsRPFE3HAoz7aTOCCdWbxRNcTIiuNaFb1bs85eF3NYh2eA524XEFxLqk_oH67zpB6-fFZLx5fvFCdTLV_DSs5cO7cJPyH4j4xtO3o_qRG4TAjhq8qRSXMcYfEcqEqi8X7N0OxT9PEyiA9h7GvYZ1uB3mDJtMxoUpdEGLcoOEZoC145v4V4bsWDuHB2GqhyN_mKTpm52JEYIDAd_yt1CNxEq3vPsk2S6pSsMAsjW5kIc7gr3ivfTS_TDQl0KiQ55Pte7IyKFpPhNwmIFTn7VFJqrUeRFQQAewVMR63XQGTf2ry_k_qbJy-j2qkuRBwNpnW2GirpyyKVbW50BOv3F8u7UnbDKawcgOyhB4gcArq-knEdMG3B3P1M8Alskqzh9sSyDfkopn9aTuQM2fOWdg6vXHJag0v4eiaWWFyF9ey35CNCRJE_A7SXTfvSoRG5aiBXTe31wnpQ7kAW-5B94pqXo9UuuvIZ3JfsFjBpzMzs4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
🔹
تا این لحظه سه انفجار در بندرعباس، و سه انفجار در سیریک تأیید شده است.  @Farsna</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farsna/449298" target="_blank">📅 03:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449297">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚽️
انگلیس با برتری ۲ بر ۱ برابر نروژ، به نیمه‌نهایی جام‌جهانی صعود کرد.
@Farsna</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farsna/449297" target="_blank">📅 03:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449296">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
تکذیب شایعه حمله به اهواز و آبادان
🔹
معاون امنیتی استانداری خوزستان اخبار منتشر شده مبنی بر وقوع انفجار در شهرهای اهواز و آبادان را به شدت تکذیب کرد و آن را شایعه‌ای بی‌اساس و ناشی از عملیات روانی رسانه‌های معاند دانست.
🔹
وی با تأکید بر پایداری کامل امنیت در استان، اظهار داشت: نیروهای امنیتی و نظامی در آماده‌باش کامل هستند و هیچ رخداد خاصی در استان تا این لحظه گزارش نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farsna/449296" target="_blank">📅 03:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449295">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
شنیده شدن صدای انفجار از سواحل هرمزگان
🔹
دقایقی پیش مردم از سمت نوار ساحلی سیریک و میناب و بندرعباس صدای چند انفجار شنیدند.
🔹
هنوز منشا انفجارها مشخص نیست و اخبار تکمیلی متعاقبا منتشر می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farsna/449295" target="_blank">📅 03:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449294">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=jmPgz4lvtosWUNWnrH12dW6qt07UT9keu2Px3eCdjwEC3hJBklBU2tBm4_SZ-PAhVBFx85x3gUkT4KSSUlDOUbRc4Izb2OjmT-rSM8pZUtvqkIFm_8RHucWoUY5AP8__lHcyQd8X3A9INN7RGg3yqHP-6tz7St50GeWDGFGylEvyCM9WXDllvq_EkGu-A9691lrSxF7zzpe1P5BqhS1XMePvlAyCajI3-jnwuiwjViDCZWWFprJS9_czo_JW6N_MQCU50kRLr8-Sd_UWgx0cTErShcElL0f4zQQ74gwyRjcNG-hcAbr9NiNMdNGKuIuWTb0bvOu3RBusmLbLm8T47Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=jmPgz4lvtosWUNWnrH12dW6qt07UT9keu2Px3eCdjwEC3hJBklBU2tBm4_SZ-PAhVBFx85x3gUkT4KSSUlDOUbRc4Izb2OjmT-rSM8pZUtvqkIFm_8RHucWoUY5AP8__lHcyQd8X3A9INN7RGg3yqHP-6tz7St50GeWDGFGylEvyCM9WXDllvq_EkGu-A9691lrSxF7zzpe1P5BqhS1XMePvlAyCajI3-jnwuiwjViDCZWWFprJS9_czo_JW6N_MQCU50kRLr8-Sd_UWgx0cTErShcElL0f4zQQ74gwyRjcNG-hcAbr9NiNMdNGKuIuWTb0bvOu3RBusmLbLm8T47Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
🔹
تا این لحظه سه انفجار در بندرعباس، و سه انفجار در سیریک تأیید شده است.
@Farsna</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farsna/449294" target="_blank">📅 03:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449293">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLl9WjHs4HTwnELA6Vd1qx6xv56LT6munC26z7T1ZmfQ86ErwY6ijPoDVn2KdE6zAyIOugOSTmapidrMGUaM0ZcS_mR61UXy6xg_9nLwcuRVmXToH2ydrkyCWS3vB5ev6RS30IDG5358AyUuH_MKa7rMANDD-79mVHFSQXQN-_OLl1XL5lNsWmw9cucuvbnzs_No_mwk2GCDawEQXHjaIAPkXFWqY9ZYnyltAyHYDZxw5tG8QJQHLa02fu6FK70idq2knv4548m-OUHr47C49waNaqei3q2cLYOGq-zr-scrYz9XnGqbsjDn77ZoTyMGzpkxS8XsU3-TOuMRa4WEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شنیده شدن صدای چند انفجار در عسلویه و بندر دیر
🔹
دقایقی پیش مردم در عسلویه و بندر دیر صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق انفجارها مشخص نیست.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farsna/449293" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449292">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
شنیده شدن صدای چند انفجار در عسلویه و بندر دیر
🔹
دقایقی پیش مردم در عسلویه و بندر دیر صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق انفجارها مشخص نیست.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/449292" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449291">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
برخی منابع محلی عراقی از وقوع انفجارهایی در اطراف اربیل در کردستان عراق خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/449291" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449285">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PFTb94rJAPQWFQIkq-LFMiML1_nmc4a7_An3bJ_v5-UykKGnH-NrgzQhcIFRbvMh6jMMX_Ynh4PqWi_Nvikn1A344iyf-hVX5L8ZJFaZwSjj4uWboOu00H1JIdUTsj2LVA0CqpSeWKKebmw9LDSwraJ5HKPbEnBI6o98iKGM_7GdYIARfJCumr7VlUgdmlI_rFYo9DYO3U3bnqKspVUFS8FT64e7CY1rLAsu91eJ_eT5h_cnR8uqSFqBM6K9U2hz9GEKkstcGF5a1k5TEhxgK-BTs4cWkAMTbvzM9fK0q5YzCij-Z5iP8kVA1M9vVATojNYxsDegFTdjjDG_T47nRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bA43NFfK7H6A8o62RNPvPJcCTg_9uj6rKUojzHVV75AtXdn5IfTJUKSindSpXm-_-CjdybctadK_NywRr5Ky7lIlWR3zduqaNUxnOP68JgDYZt7t8aE-qHsjOVoie5dyOYXwVWtsAgISt7FOiyDkOOmRVTZmIA6QW8px36SYEGaJkse440LqEKhLMkRExGwngy0EatxU-7_XLt4aPTXzbl3x0ZjKV0dSVF9ByXGxh45nip07UuofID4ZOfY8GHxw1n5RNXF8IL46j6VLoZKuJWzsk8sz0-mlyTHetJHCpqws5GV2gsr3j1jeHF0QjPDSf4YmjtwmpevdaZhIvNArRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4Tli7xBj3OmSI0Os3ov2E5TxhLfWsKfscce7TIgPyh2Bin-uedY7p-QCMhgLllZXfB5wkkoidSI_I6FMiq9282ZROD3rsCnWix3dlRZRMtBo0CwO572QaKrEJGSZPA5HlEuPiqRdpIEXjFYLPWEsQjrRaN1LaJvgj-NOz82hjVLs_SJtUNdUi5B2nM1KMWPYtaP4jJwbQDWe4gP2XNvmqcICfS821mbyQs_syVQrh-a7amOydOkDcrbJUfeHOGMMczJnbo0dDVBM7POa8j4XJlp6DjkUx29fSzA7gRi1IlT5KRJAAJ2StkyvzA6Cp4QU1HR9NyBesLslctVBIS01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGAo22yr7eDOOU0Jiov3lxsfy9j8pmh3a2wV1VGiJ-LIlmO-kiK5TJ-qEuJZs_7iUOgxkv1wRE-vkxAvyTUxmFCwuMT0UdMM5D3h5sqe7xaWYpFCfiZA7hx1OMkgSaBBQTUq1P3DlDCdEnQb8XtsUoGQOWn2eufUcpezYMiK6C5yPvhS_lyTwIndxkkqJvcshEJEaXGrA0hpWb_M6Wsq2_1Y61LH9T_kJfOMMF_cjmaC4196BZQsH8lZhEZroUIcFkAS8XJfott4cDBF5UwiwqwGusly-Ve3uorD1g7sSzTYsyCoAV-xQCY2WzGrHy2lHDIXSgDwnvnzBkxX6KpBtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3om-7f_wOyFlMy71R3o7y71TlUk-qRBy6DRUL9Qk8E6rRdcGQl5A2I8Kq507cTbRNu5NqrsXTn5VDdgq1_P6Ykamfupg3wwDrtwBH0_01iGPbhzmrb4oX2aPJzDI0zY2Ft4iJZBEs6OYfAjrTdIURWBzrn9MEBXz2ZpWdXJWdpFp3ISzmRC2MkEKOyYHa--kPPhxhy4h7ai7rdgAYn4OSChfo0fj9qKvo7dkQOpJYlrrZ_P9YPpjA8huVJnAYXdGP5XGEVuX70ohjouLkyuHnMR5YpkkHuuXxjx-Lh9tcuctUoxsmhLuq4Wk25mPeGvYN3LY23uucasdxx-KYIVLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNKlKeQG6oo0Jp8YuY6DCoJAZoy23lQoh1bgUChbLsV84k_0T6sJpVejh0W9ymvDF9_dN0FjFuyNdb629oUaRHl2zruRVsDOYVAVA8Qorr6XBJ08-59x9ay0pnyUu6cnFqBXo0VVIkXmr7fRNNWJJd1fXP9jYyuIp7osR9FwMPDFl3Gsa8l6RZmJHf5VEFsWl0yoxOxPgIvDvfTTFuWaGACLRwzcdZi7x_D0QBcm6zG9gUPGP7KvMeVADg8iaY5tmMJXrUUIJ3BivOWIaaOY88Edg_CE-ZvN403V1wH321uWWUvZhAppPtC0k5MdTzKNFDj5n-30sNKY9_YllqdrTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم بزرگداشت آقای شهید ایران از سوی آیت‌الله سید مجتبی خامنه‌ای، رهبر معظم انقلاب در حرم امام‌رضا(ع) برگزار شد.
عکس:
صادق نیک گستر
@Farsna</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farsna/449285" target="_blank">📅 02:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449278">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qr1QV6spBhHn9gKlK3NtL9jSBaca6NvexCTy8Vif5UgjizDQo2zy1RAFuNmxSM9UVzAIZbmMeHQqF_l6c1PS9tfXVLn_PQ78MpMSNklZc9zjbIuFda2CftlTjsYNeeWLPitd5_u5OcIaMbG3E90mw0YGaVq0NyhrNsnz8kpB8ZkbxOg7denIgTHndLYMh-JTWf9ToAPYk29WBO1u66G_kBQhRfMsi3H8Bt8WPzBdMj1eCOimKzzD7cWAxRkRdpNvHUBK6_sIUSwb_vkG9dHzfla6C_DHLKN1dh0C0w6I50crlNKMgL3FUQbsDXSv2X6JTGEiPb4nBm1OSr_XCupxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3D0XY1ZOKZrPg4sUzfsLuM1AAhjvySPZj3fvPYEB89b7N0u5x8IIONtGjZglNTBXBgT9wGH5Pa4xCqqPJXWABrcbkBnHxiX4MKjmcx44ftVN_emTNOuVVTnHl5LXujNPfOJm3r3V0CnirDBoJgG0eQROjtfa_V3y_gUTaT75D20hoeAWWFanrBHV5ZPcTMmbyWgVopoXjtJlEroIiw6dOUml30tlymQrUboDhEMjtHDLj4nfdUHTvzd8a76bFmRXbeaTOL3bcCLta6oLwRfAKYmBVsnx61HeAUpQdiGhDoncYQpREyiZdos8PDEoEEFPrV90Qijco3BCWD9Z2ladg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMUKBYeOCTTqH3G2ltlp8CElww_l2ROlBpli7wZrFBxIBnZV9-dx9BUmgUeVrDxpT2hTO5GcMF5_TVyXY7yO1Rr8Lnek3g9DhtdfPVu53_Ee61yt-UtEFyrN8orYsCoatmq0KRs2C_pHlBZK8oucPeAcEomwR9pMH3lPJ1jQkM4etHYu8W44Fmo-dNHgQKwTDn5sUyklAsF1W78-pdMOb1XLr5lTXiQau9oPCrZHaV2rCltuNjM0oF73LXUj5svGh8wx_c-cKxAqBQZEWpHFl3nsxRz7qPgKy24VAupUmDExIU-ApFwJkW65FjKCE9zPi1ZYzwmUbXOZrt0rBz8B0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jphdolqmlgsbZeKiZiNrhUFcG28UMqnXfWhh67-kZSzGp2oF9qR9BYmiVr6pzOpAshK95RS_mCF1a2uM-Tq-6kDWzKQ15fDCldIx264LdCdqf5Lr5qCUvxxsv9kLAQKlZeqbyWlLqmPabatweLWXLaHY4Dg_73Yd9QrkI0mumBiNaTm4tt6yCcPt-8XrJbU9wJNAZhpD-oWSi7KN4dBBVi63XXSIjadXwOv6gtsAzC6v0RFJVjCoJnA0rv_NRYlYhl9aYC0-H_osg81M91R3wpH1Dq-11WCWAdjgNRy8LnMks1CXp1ewYu6cZTxrajDJE7qoHG-_u08XPJv8DagjsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bp8LqjoDFkc5H4EnO98LIQ3l5Fn06hEadeIjdo0SfBVfbCy2trKdLpcVd2B4fVgSxRrLBJUjoXbCodHqYm3rJaT4mgd5agGY_Shp13j2WYaispZW-ataNc5ugMJcIkAQBLS0GOtVr2wFK0WiXcEF2d1rEx6zuZb-YaVibapxYcUTwTixRyLy3EGbbEIl8JVt5DzA87voU7FpvDOpdUBQ0Dp3gz4oq0uZuf7K83VJlMP4z0PeEWQZuXLLGc_ZHYHOLA4XwtPKA_iTjLK-D0RVC2-R9e3qwBN99r-DLVs41t6KZWiSnC64YsGaYTviJL60Pt-2e-01HCKzTAml3k4AUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qf-J-IoEMEFOOmY2qnkoZuIkxReoWSs4qRm4ppAEUZ9L9bRpJdKMMuoSTyLt_t004-Gn9REPEJPoG2rdL5VoZC7_3ZMvVaSFP1KgmdGK-HC_LtMnm6kJP6X47M0h4mNX3z9_dMxV238XKVdeB6KDZ31xtBLXF2jstlKfSYstBdkru-JU-3A8rSufdqrRsNgdO3-ERzIMdG057HSukvt6XvXpVcJmC6lwOQyB0-f6VTTMMKFGKL8UjXz26JMcKtutpicUTl0fBs_VIwuhP0nPLasyExhpylebbxPakj6HHtXBQviN3qSib4X-q8GBWYEq0DdiZd8otifVKJWOir9cfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_CRtujcnlSflTLEJR_toFBJRLM9Q1OyPJRFPKYJGZSxIw5Jw6zVj5ykkueMk2SInE1eyTy0JpMVzN36yvsYo24FY0n0fLpCXHAlbmeNtO0yDRhhOqq4iPCjk7u-nEKEFBtLNopwfNg_X4VY0MA5hOYCD-s6Ms8ovG3HcBpHfCs-CLgtB3Xiq-PaI1OojxE0myW5ZYDh9E0WIMQtuAg5AyjeKT1arBrsKdf4oQYe_WGyVUWjaM84Gr24AEI-r_N9kkuuWRDiZdvUUsL1EZyZHQ48P2UInj-pYeMO1x7B9WyCjHGwcMienspaOqrub24e2YEIV_vOiH_fumM7g2_pBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
#گزارش_تصویری
| قاب‌هایی متفاوت از رواق دارالذکر و حضور مردم عزادار برای زیارت مزار مطهر رهبر شهید انقلاب در حرم مطهر رضوی
#باید_برخاست
@rahbari_plus</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/449278" target="_blank">📅 02:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449277">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
شلیک‌ِ اخطار نیروی دریایی سپاه به کشتی متخلف
🔹
نیروی دریایی سپاه: در اطلاعیۀ قبلی گفته بودیم مداخلات بیگانگان و تعیین مسیر غیرقانونی حرکت کشتی‌ها در تنگۀ هرمز، برخورد قاطع ما را به‌دنبال خواهد داشت و روند افزایش ترددها در تنگه را با اخلال مواجه خواهد کرد.…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/449277" target="_blank">📅 02:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449276">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
شلیک‌ِ اخطار نیروی دریایی سپاه به کشتی متخلف
🔹
نیروی دریایی سپاه: در اطلاعیۀ قبلی گفته بودیم مداخلات بیگانگان و تعیین مسیر غیرقانونی حرکت کشتی‌ها در تنگۀ هرمز، برخورد قاطع ما را به‌دنبال خواهد داشت و روند افزایش ترددها در تنگه را با اخلال مواجه خواهد کرد.…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farsna/449276" target="_blank">📅 01:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449275">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
شلیک‌ِ اخطار نیروی دریایی سپاه به کشتی متخلف
🔹
نیروی دریایی سپاه: در اطلاعیۀ قبلی گفته بودیم مداخلات بیگانگان و تعیین مسیر غیرقانونی حرکت کشتی‌ها در تنگۀ هرمز، برخورد قاطع ما را به‌دنبال خواهد داشت و روند افزایش ترددها در تنگه را با اخلال مواجه خواهد کرد.
🔹
ساعاتی قبل، این تذکرات نادیده گرفته شد و با تحریک بیگانگان چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی‌اعتنایی کردند.
🔹
به ناچار یک فروند از کشتی‌ها که با خاموش کردن سامانه‌های خود امنیت دریایی را به مخاطره افکنده بود؛ مورد اصابت شلیک‌ِاخطار واقع و متوقف شد.
@Farsna</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/449275" target="_blank">📅 01:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449273">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9fcade4ba.mp4?token=E0TsVVm9yEKlTeL4O9U6fVxfYaS-hgjdd5NfRK1gpJcmhbeC4SknKOVZMONJCabnWcxEuFpOlzA1HmyEdEOJL7TFgrg7SsYzy4cg5OvJll_ntirho0Z0haKuZ8OVCTeAqJTgxDVFBvFsY0lNeUDE_CRW83bLYIbtL2cyAVUkhUfSyJhgQZakioPtxzEmkTUwryv3wjrY0D1wRywd2yWLA7IY4V7yyPW0dgAnmdjNqwCi7bNXjabzJEb2p2_zPaaXM_k5IOlNOjEjaDs9pSJLYfF8PSBSPQJTzLF7M8hxhaF4aHZl71yhDYiGG5Aqys0gRxpE4vZlfRLweM4BW8NF7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9fcade4ba.mp4?token=E0TsVVm9yEKlTeL4O9U6fVxfYaS-hgjdd5NfRK1gpJcmhbeC4SknKOVZMONJCabnWcxEuFpOlzA1HmyEdEOJL7TFgrg7SsYzy4cg5OvJll_ntirho0Z0haKuZ8OVCTeAqJTgxDVFBvFsY0lNeUDE_CRW83bLYIbtL2cyAVUkhUfSyJhgQZakioPtxzEmkTUwryv3wjrY0D1wRywd2yWLA7IY4V7yyPW0dgAnmdjNqwCi7bNXjabzJEb2p2_zPaaXM_k5IOlNOjEjaDs9pSJLYfF8PSBSPQJTzLF7M8hxhaF4aHZl71yhDYiGG5Aqys0gRxpE4vZlfRLweM4BW8NF7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم بحرین برای دومین شب متوالی، با وجود تهدیدهای رژیم، در سوگ رهبر شهید انقلاب به عزاداری پرداختند
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/449273" target="_blank">📅 01:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449272">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jS5hP77a_19Gkq7FGCBnR6USueBK5OPSNH_QGOiWHIgMbRux_jByG2G-uha2oUZGifg1h2pRLNBrw9SaSWC5ClbhKJyvXQUz4JtDFBc2nKSId2K1T4AyAwiMMFCWqratOgVLyxBxW4eULKVom-eJ0pLdtOLI0QN0IG1IUYYstZFin86q9xxGfDaE09MdslmA42bgm0Vw8v8qF3eDrEsL-v7aVzWzWXLjrxb3DImx1JsUMf1NsOaTmOrI3eCdG7bhFs9jQ-VgqZu8IIUuZxoUZ5zjIWFrYQvucMYoIpFc5Qi34ryX6Luzj8OgOWDEwFR7HyZ6uLhn4dMZWsLZ9-TLGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تساوی انگلیس و نروژ در نیمۀ اول
انگلیس ۱ - ۱ نروژ
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/449272" target="_blank">📅 01:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449271">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBOaDBzNXEYdiPSZBYNOnJ8YpDjsK11PnuvSmnBVyncAI27HbAgVYdwiPBfzn351aIHuy37wIa5Gyv8zHpApTevDOQMq0uBDHXkaiP5MzGjZyjMNk3oKJh4GPDym5bt-vtRApskvAbUFMKZc84rDk_J-LCS64M36gH4fQfrGT6bdqowUQbxbwRu5Ma4lk_QWLtKr3upgkbNU9eR6-V6M6tOdu-E7_Qo6VgHISj-NmWGX8sfrhGaUa8aYD7XYez9Sy8z2UF_meEZnBNVKte2ypwgzVAIZPErM5ATpFqg_F3c3_yeKMsAMQ3x5x2eJzi9s3lHFfv-bq0gEXC6QnyirbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنگ بزرگ نساجی پیش پای پرسپولیس
🔹
باشگاه پرسپولیس در روزهای گذشته دانیال ایری، مدافع ملی‌پوش تیم نساجی را به‌عنوان یکی از گزینه‌های تقویت خط دفاعی خود زیر نظر داشت و مذاکراتی نیز برای جذب این بازیکن انجام شده بود.
🔹
شنیده‌ها حاکی است که نساجی برای صدور رضایت‌نامۀ ایری رقمی حدود ۱۵۰ میلیارد تومان درخواست کرده، و پرسپولیس حاضر بوده تا حدود ۱۰۰ میلیارد تومان هزینه کند؛ اما این اختلاف قابل‌توجه باعث شده مذاکرات به نتیجه نرسد.
🔹
از سوی دیگر، شنیده می‌شود مدیران نساجی در نهایت تصمیم گرفته‌اند این مدافع ملی‌پوش را در فهرست فصل آیندۀ خود حفظ کنند و اعلام کرده‌اند قصدی برای فروش وی ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/449271" target="_blank">📅 01:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449270">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0da88cf4c0.mp4?token=PKF2JyaaadKd3xlDW_XcJU0SUyVslvIp15-_FwV5ucVyzO_29bvd42cjDZYy8rqydmQDeG9TlQjlQ-T16ZB07TZ5T4fz1vRS2-cH6cPXaOB-r8yHS-Sn-YGpAYtKsmjbSdwz-Hji5BQN5NiGj-LJUaW17HTpM3b7RabD6ODp-eF87GVq3iTst6uzEakwDhmp53W8UkgWnBZTZWXrugDHw1ykXOirQT01tNt9pWrabSSTMw7fQjhDBylMThP9sGAjGKZztyHH8kKWErT4pqIwYpgurWKwCIlzIu5_Q6okiZwWaiD05ufbBBpBnlauYZLhYlyPUSNVHjHb6c_JvYcfLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0da88cf4c0.mp4?token=PKF2JyaaadKd3xlDW_XcJU0SUyVslvIp15-_FwV5ucVyzO_29bvd42cjDZYy8rqydmQDeG9TlQjlQ-T16ZB07TZ5T4fz1vRS2-cH6cPXaOB-r8yHS-Sn-YGpAYtKsmjbSdwz-Hji5BQN5NiGj-LJUaW17HTpM3b7RabD6ODp-eF87GVq3iTst6uzEakwDhmp53W8UkgWnBZTZWXrugDHw1ykXOirQT01tNt9pWrabSSTMw7fQjhDBylMThP9sGAjGKZztyHH8kKWErT4pqIwYpgurWKwCIlzIu5_Q6okiZwWaiD05ufbBBpBnlauYZLhYlyPUSNVHjHb6c_JvYcfLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار انتقام‌خواهی مردم دامغان، در شب ۱۳۳ حضور در میدان خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/449270" target="_blank">📅 01:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449269">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجار چند ساختمان در جنوب لبنان به‌دست ارتش رژیم صهیونیستی
🔹
اشغالگران اسرائیلی در ادامۀ نابودی منازل و زیرساخت‌های جنوب لبنان، چند ساختمان را در شهرک «حداثا» واقع در منطقۀ بنت‌جبیل با بمب‌گذاری درون آن‌ها با خاک یکسان کردند.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/449269" target="_blank">📅 01:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449263">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0mwyZ1UrP6r3ypWBQgNzrUCB3Knpcw1FI592YtIhioIu5asu7ZFzgXw8p3pxOk_asfX3Q7Uz94uJ_MOzjfJhrS84-O5NnlO4FyTD6hUwwJFZzl3SjQV-18HIWwyFc6EEii9CEynJ53dxYhn2U80-Rcb802JSsXBPeG3AXkHP_emtEgYGvnMwUl90q5dze2dqjwW7AKohSab2eqHjtGLw5St7MBtaJ70QohMFHUtv-9xWbzrvf3b92K1_4nvJfScM7JMi4x7QGEgp-g7XZmQyhmUTwj94drlV9UCJom2h-6uUZYQEX7XzAsZgiv6HoxbVDQShI_aauNdqlBlgmeysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W8lLq-VW9468kvTl1ZT18hifS2K1yBvhsYlAwZtB4Ranv5u8ourLa8evnaAGGY7SN57f3xG7er248u9YlxCtyw4sDiXzWBjXFXvFRb2_73eCpmrsDL2LGOqRNmtevNXzRlVNdbSTzgau5XNEGhecKvwglEywlu27Xu38-0mPNACDTfD3G75baKFWAEezRO6UU_vETvjA8kC2U167w3W5EBhhJfDbkVV2S_aTj2l1eNFrlJkPGwo6X3u1VNlEssL_jVut8asrJND1q_zLWNyIsHtK7cPWVtgYPrg6_ZWP5SKQOTmnJD82a8EroAEHAc2Wj1b93W2ByLnfKucl7I8NaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QLiTh8pbKl_ERhvr2z62VrVXo5hqtnU_XpBo0xjT-4hf9i_rox1UbkZ-mS-CnIPMaMwYB1C0G-BtSsirgdcX72pIgunEfcLAk5ZFRIRrhXtdhkBLqv_AefFCRlK4mJJAIVJ5-vnGDQdS11xLl-KScNNhhPwMgoguZUhtizqD7QNVxK-rXwBqrjH40K73ALma2LdMytXcZJqzHhAS9nmKP0pitNfVyh1_9YulfuQlbHxswQpYwqHG7VfkFnQnOZLk_EQMynom_nFdQPgNTAQjkNZPU5SYXnAieHDpLsNlw847iPds6-9XX6zbcxnnmsYyKYQTDX5CYmdc-pcegjy9pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-aqBe1rgULii5CIVVDw5Y4LL9cTnfPheZiGHDbVSb4Nptk56CZpAMzLu_03Tblv2gp1UnDURZND2Vn-0iTfOwjMwBTwURgjaLujX8O0l5yITAF-AErWLg4PhgLdlO0h-NKokCEDVCucat3uBSU9RCuLXJuqcjx0ss7sgm72tgm6ikUNJciMBWVm2USPXUz5k8sdqPJjQPIc42J0IF1N3AHFpAKVhr_wVr6zU7RpdkPUCcYE384C4xkESHQn8yYMwqRm4jRmipRhFo1lraU5tHbpSPUeaiAinmm0g9KTaz62h12tk5sc2p6ASSzihcZRcVRF-lsa6qMQlSyhViP4cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OW7arzMsVO5iA5ReUdYG8LFOCcgOygeIq2toDpC4KRHycNrJ4wrTeV7KnIwxN3cXYF-QTtQnN6ZUPCi5NSQGrYTkXpwebZrg-N5Tm-rhZ__9DRx3BvK_G6oqyCpp9h3r0C7oNvfrZDTrfRGCiq8GitjreeyxwgZzTsH2R8n_uQIDe0Uch1hSjngd1rCnW4vjqj-dO22Yja7IJ3sRkMWTdxgajt9PU9k3zICTYAQj9-neHOEUtQc9G52EqoEkhBTQfKP5R2mTYiHSmNsWR02G2r9b8OHik1MUN0sXrpVZ6aF0-qY7HTPUWjQdNqtiSUiTNdQ3RYoS62AaZWaQtMpU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMAyLBr9o1qXLArqPciozH2O7Rk73niff_EIpZRS7V4VVx4n0t7hCqMqWB9StKtPd45s-L6xgQKfmoDiDDV8r107z89gwOZiWL-OlPR3paOWB4cyQych2hR_ZSbAcgvNhaGsfzDdGflMxjG3nA0Veja4gfkRG4hyhu2NNDmpPBgQGs9cVJy0OauJ43KaAfbx19d-qvV4qpsYC4RLmXw5P2f2zVw5dFNqo3TDrnUK1iMgS58qsa1vxSsDvbuDAsaAl1X-2GqkjVsJEipY4YdXkZXdg6TSnWY0DSZ5fkP6tHWghKw1UZ41cGjmoX6MeyeeuRV0MPEqigFrKjKgBqN5qA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۲۱ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/449263" target="_blank">📅 01:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449253">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-XNWwEjsSS5iP2ldpXAxjUODoRc1Nqe2pWR5bYu2H2ZM1PQfKELx1roD-tHOY35oGNZ0CNMAnWYacvwyjamwCupAYyyZej4OxOF1M8hNQDMzISXtM44JjGpwKRWG_zijwPXj_1H0_cTd3IpYl4G2U2E1OWOApnoNKm8RXrl6GzfyicoPC2jldSbdPMm7j2cULbGRLptTjSq-gjTKkqZu3gjCoJlaSsECSLWKhSkdPY2Tn3Z0liynAHBoJz_Ry9E-6aQ3GQsQivFMuQOcJNYuQqgiy9EmDp2aBK4QMGC02kq3Jc2L9sryPs_qMlE57jB4OGyoBDI3HX43-kujvmq6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ByQa4QXhXQrFjJHuJQk4BMe7_km7fYni7oAQMZGeouEN0EZI9gpf0t_frEKsoOSCq0En8lkJXlYidDKSoO5OewSaziv6uzHS-VcEtM5pneptrTnSjbM2UFkhSpDTG23i2oh8HBqkoFc7G9pQ8RisP417UwJSFE-kR6R_HIm5eUomd5eiRgNfBpLft97HX5m1-KIWKzYbg4M1uZskK70fSVthVpYj5HdSO8wMrHVvfxUKqUJdmqEyGbED4o87vtfYZKwUpRt9A3iEexrWKbGHlGSKuceX3QLKNLf9hrlSJnhTUMu6x7moLqaQVv-krzfn-U7qgMASBs44kX8Ao_Fuqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NrbCy145ap1V9i2DpB0648iJnfl8oq2ffZCeP4aVe_87u5DE8WjCObcOaK9Yp36V9akPhz8NeZSN4HugK7Qb6kJNU35r0mt_o8M0mmAj0yyBEUfzRN6n_s1shVelIAvX3upVCFUzNN841L2i2q3qDAPUin8wOYdS-2cjO9hWPvLjWZo3OWGtnxalvZBswugaj-7h9cA9U5AH931DsIeMeGmCr8iqkVmsu_vi6MrvPJnhOV7hwN0hRZFp3IQgPIyT3JmBhvD0Ma8Kf5xOlLFz1QjL7SNjgrn9l8cVAJZ8xcwDABfS5yg-nf_XE3E7239u9i5EAfyKgilsqOlBouJ-rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KnoOkp3SZ9_CFddSkuqfg_THgtkXAFbb4rtVZgnf8LjFfYPLLkuoeX97-5KWGxUqltFUj9ZgcuwhAOepM6a5Dz_7jzqJsBfO5pbpfUdFMSKZD7qJSSQLmKJTHLUdbDpDfvIj7j3ZneP_aNYWWYQJ_P6kbDDgsT5HYNVtXxU3ydIT1mPJA2YS00kxq3AC95BG8QGzHZ13CM1oA0wR0kKP-LUQ7qhGgivF1_UuVFVVuiBHdweJJQi1m7N_GB4QrGQt-Uvgb71mXTfX2vieKNXggX4e3J2pIskipweyrP7FqQfJYouJI7fgRXWQEufs2Az8YIsOhloZ7KvI-g6EHraNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnE31rto323xBslJ6rubyZa8hyjJYQK_-tfm7yx8LQEntgO_CpViAvs00gkEaPqHtp_zYf4MmlqEuM6PIbub4w_E0TjjBiTpc1UXc4MGpqB4iovDkUyuJHZTXEyK1RPiGQMwm4PHuhX3HWt_oo1Q5AxfQLGukE4xXCxrfT76EVES5TQSaJr2nrv2xRhIG2eXjPEwsYhaf8Jrog_skbxCDM6KEsRqxuzoGhq-lBywtplRL-MbIUnwuOsPZHJCq-obpGexOxjEOCEqBHE5MlDTG75iPNSA0fRXupnI7FDf4z5OfCeQefZSWXAqbS59mngo-k3zDS0qs3D7pcQEU-zpaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T56bsCjd-9ztS4OQto0TYQSruucluDYPToT9mlT7VADOAcQH6s7fOe279NDKpqQ_U0qDbUd4qqcIlsIM_83jVcmuK_4-M6asMRXnnWDbNK1RtPF15SSivzmr-P-7nbAj22vtVV0A8vm_9nwrF69EytIP5GnjEKNc5oDfdl7PADipmtFOZ9SoHJZhgBDVL2pByKTH_lc-DUQp_rfTSFqRZcozgADuXNdd865iLTOHcp9FHgk3IIOIECBIjLlWETGtlVthjg4okJoha0In0a3_44XVLgQffaIHAarTYADj8V0tNUTDdJU0ofu206fR9QyU-TLyUlgsqLTaGUSZyRuV1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dkLnMe43lSTNkP_73dA8rtMvdO8gHIzg1pa_X4fSBmKKOaO1GK_LoH0w_C9cPet8STYCdmZEQiNpFbRQ4UGJ7vDyCbjLbSrgtP2FB458D4kT3d8Y3tWudjUomxjNQiQsIyasOoVdEWJtAZ-VkR4En83mZ2X4fxHOwIigCH2rZWYy-L7EsA6u0EVrNNeNV-Bxcmugd_H9EhIbqRIZQe5gYEHJzaVWBdlSxuB8QPpjU5wte6kgTdQwc22Y9p9srOyj0x2tRyPZl_z_jUVGmwQPFF_Um5wT4COGc7RtXBOXsgZ6GHDbsGoRsMnlyk9W7xI8M0MOVMpWGIXFgxg0IAGvdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njNaRKu4qGCWYo9m8L7aerEhjQYK0w1B-UPF9nAVTJB15WpUmcWoiGoYMws-ejr3aZSji4-uYghVchXbv613-63ldt1GsLTVdr9fMT6fjG3zSKYQHuJhf0gQL9Dl9CTiV5jIctACIs24Chma_6p7JkM0GwNr6l90eEXe5yh9N16jFga9kO28ogxllpo5dcM8VKadS8qxkj2-_eZag6wcIKfw8-BDPdZhUz7z9sWOr7lMzL7DGm6uewz8IwLzT1cLu9ttQcPzGp40z3Hntpv0n6OPN9IW72FAYEIHMgUSN3H-P6rClYIf-nS193GqpvCkpDpfqb_eX59iaf8kDc43fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zgug-IqPaVv7npwwRWeo_juDiTzmZaZH8FQDavY1fyLAg1Y64gk1YgLMUNAJUls0w8vLzPK3bgWGD5IX6L_FjR8pKQ7eYCe3h3ZLAD4YjwswcHqfrfhZQfs1Kg7HqHCKOuBuAvPri7wHTpBUcK-VS6COMYV24QUhp7R_RZjjYluQa2vNcl56WbL5Mux_WWlDBNmHGHzU5DEUkgH8w0rR0mfncI-hAL25ScuGstL4gmqJMBcRNs47JiVlEyo-gKId0lNLJcr0iAoj5RYmmp_F8d0Ln-UaiRN3loZ2xF-3nruEgCiU4lvLLW0F2a0XH6BK4_-KJGGsmE9kID-KOsO7cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ep_wPTFX6fnEzbUhd0RO0pX2ndvbM4BEKcuAfROLYD2qYAcx5bDxcbJEkALAWt6ZZuaHiUCTYZrUFyo3fq5bWXXLsc2EeExjyqH9DNHzhLSsaEE0cyPiVQBakhrc5zkdjkdWErJV3ERHTsjcF4zmENGIY7rVG8rgLQOVAXd8VRIEhMQkvQusZsp2u89qL2IIzwiBnfFSxkioMTtYfnjdfw8rBEu2vPtwIb8BHAL7Cx5mxCKKO4_GtFlsYRPcHIABwK6HmoikEtm0gRGjfbfDW1rUwZhbqXodNAMTP6Qrxh7jrqdUofdHDYJmI_3YHcHSN0im_OHSGUiRSY7B9SwS6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/449253" target="_blank">📅 01:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449252">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRa83Rq_yWCGFQDgBAayUi5ht8ghka2actDVSikU7KXwfaR1jx2-1_CBXS2mFklbX9G3B9ODcrWdAe9To-xgssZe24-OufM5JSvapBRAZIbo8oz4qY4XM3HWfg4dzX1gan0ZWnZX6XvJbgHfgN55dkfmrmVsMrmPqQH5ODnRV0RKUAq7UiBJg09zzDtopJM_ISIrmIrnqYzL0ScBMlw2-GCjjw1RR7WRLE71CpgxjokTGtSkHtQxHFI1afAnoZvs6DIe_4E5NuB5vOrHV99mJrMeF_HyEQa96bTew5QMf0vaKqPElZecuLZqvJMiRfSdVteJEUf2KsvF4IXP9M3-7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از ۶۹ سال؛ وداع آخر در کربلا
🔹
پیکر صدپاره و مطهرش در بین‌الحرمین طواف داده می‌شود؛ گویی ارباب بی‌کفن، خود به استقبالِ این سرباز کهنه‌کار خویش آمده است و ۶۹ سال فراق در چند لحظه طواف ذوب می‌شود و تاریخ به احترام این عروج، کلاه از سر برمی‌دارد.
📎
خاطرات شنیدنی سفر رهبر انقلاب به کربلا در ۶۹ سال پیش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/449252" target="_blank">📅 00:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449251">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvHUbjTm3KYlCVl2AEOQcecJ23q30yv6s6445OXxaBEvm1O2GQOhaju-XdSN0JYf9trpCwAkRbk5ToF7gho5OnOIu2xYX6R0PsIQJhzLiIWKSkgO3UqE2RwpTCJFM3CAl_OfJgdrjBDv5pLXcRsiEkmSqNXz3fzY0ubHauqJBxLJNjee6RZxSF71MgdnJeyMRvWqrUnh_dU_R36rp398NWztxIUl5JmRKajLFNa67VXQfpq6PjMltPbf5N0CJJAPPPU2pvR43s5VTYY8WQtZ4o4Onl34wz4k-FoYaX4jsQ1dvJEizoAejWRXlfjpJJcu8CdfD0XLG2Ene4V86X0Mug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برآورد حضور حدود ۸ میلیون نفر در مراسم تشییع رهبر شهید انقلاب در مشهد
🔹
معاون استانداری خراسان رضوی: تخمین زده می‌شود بین ۷ الی ۸ میلیون نفر در مراسم تشییع پیکر رهبر شهید انقلاب در مشهد شرکت کرده باشند.
🔹
برای تأمین امنیت این مراسم، حدود ۶۰ هزار نفر از ارکان امنیتی و نیروهای مسلح در کشور مستقر شدند که از این میان، ۱۰ هزار نفر مستقیماً در مسیر تشییع و مابقی در گلوگاه‌ها، مسیرهای ورودی و مرزها حضور داشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/449251" target="_blank">📅 00:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449250">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6576fa0761.mp4?token=V0dVe-SPteNxdvzZJ3Om6tpwkfFr7Tlo81pG-g241VmEynmAxkACXlpHV5XOzyY5gMGWdKqq5AjXrmWPjd9EE2poZhkfk8Vt5R0Yy4ZLGSJHVAVdhoeM3F0Ki-7d_zyEtvwTB-B0FkjZBRZl57rTwfrbjeSxsf5e38X24hthEjxVWdbQbjX4Q3KRf6gvkn1x6p5WBmUwo_an26Aai7sDglt1XPkhZUl4ngab1Jyt6lfkSe5zBfAWez0pFtca5_TXxcq4JLx3vTiehP3riWkSnWf_fANEiTF7BY5CrwHkVSRKhfYI1dyIjatSBgaGNGDFxJ-TQFoqxwNcsCDf-oXU4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6576fa0761.mp4?token=V0dVe-SPteNxdvzZJ3Om6tpwkfFr7Tlo81pG-g241VmEynmAxkACXlpHV5XOzyY5gMGWdKqq5AjXrmWPjd9EE2poZhkfk8Vt5R0Yy4ZLGSJHVAVdhoeM3F0Ki-7d_zyEtvwTB-B0FkjZBRZl57rTwfrbjeSxsf5e38X24hthEjxVWdbQbjX4Q3KRf6gvkn1x6p5WBmUwo_an26Aai7sDglt1XPkhZUl4ngab1Jyt6lfkSe5zBfAWez0pFtca5_TXxcq4JLx3vTiehP3riWkSnWf_fANEiTF7BY5CrwHkVSRKhfYI1dyIjatSBgaGNGDFxJ-TQFoqxwNcsCDf-oXU4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توله‌یوزهای هلیا پیش‌از موعد مستقل شده‌اند
🔹
براساس اطلاعات رسیده به فارس، ۲ یوزپلنگ گمشدهٔ «هلیا» همان دو توله‌ای هستند که خرداد امسال در ۲ نوبت توسط دوربین‌های پایش ثبت شده‌اند. ۲ توله‌یوز خانوادهٔ «هلیا» که چندین روز از مادر خود دور مانده بودند، «پیش‌از…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/449250" target="_blank">📅 00:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449249">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66a3439079.mp4?token=qYmuXfDu88_E8ldQkr5zkPFN50BIY4tqtiuXlz3okbAhju3pmynmACkiEGAMuZ5TV7M9huIRmNUq0YbPwJY_sVxncOhtJAD-_Mmxxbc3LLdOP8d8LiLPlORLRFnOoP1BNLziuZo0t8q0h8O1KLQDVPWHm3lz4CKkOyOUiU1X2L4eOpOvHsWPW55WGk_hv-6AFyiwkaaCmOOt0boND4rTppn-j0KlfVh7mBV1KIk3hUJ0YaLKgvPdeiP1Q-rsymFivIqY_jJd8RNzPIi6K_c119ZZ5jvR9_gSd_nIGtivwX-HPXQ_XyRolFq2z_fnTdPrpaqKbUiRdzNlSqf_0LiJUpHvUFF8CgEU0A9DAU5hJyCyKgZaae4oT95O6x6aIcrpb9Xs6Nwt7mlllf5U7X7lYcdac6YFvPSuErWGdt7EpS0Qd4WdmshVkcNRE4qjlHS5KVDBjVjAxUL-GgDnU4VxhXuxqsAZOQvkDk0nxssA5jcGDql31HCvmS6JLSaHD8XBqowA1VekJMemi5nLrzrZPc4ua1K1Sd_X9vaYNnPigqvbt7_zN_1B2K-JO1J0RV5uL6UF-443oR04-GA2kVgVeQ3AX6zxJ8oTtjFtONQ6zglUJI-7czYEcCil7fGax1f3GKMA9_H2SJynhMw5E1qG2wpt7TSiYVkUv_Ah0Evc_II" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66a3439079.mp4?token=qYmuXfDu88_E8ldQkr5zkPFN50BIY4tqtiuXlz3okbAhju3pmynmACkiEGAMuZ5TV7M9huIRmNUq0YbPwJY_sVxncOhtJAD-_Mmxxbc3LLdOP8d8LiLPlORLRFnOoP1BNLziuZo0t8q0h8O1KLQDVPWHm3lz4CKkOyOUiU1X2L4eOpOvHsWPW55WGk_hv-6AFyiwkaaCmOOt0boND4rTppn-j0KlfVh7mBV1KIk3hUJ0YaLKgvPdeiP1Q-rsymFivIqY_jJd8RNzPIi6K_c119ZZ5jvR9_gSd_nIGtivwX-HPXQ_XyRolFq2z_fnTdPrpaqKbUiRdzNlSqf_0LiJUpHvUFF8CgEU0A9DAU5hJyCyKgZaae4oT95O6x6aIcrpb9Xs6Nwt7mlllf5U7X7lYcdac6YFvPSuErWGdt7EpS0Qd4WdmshVkcNRE4qjlHS5KVDBjVjAxUL-GgDnU4VxhXuxqsAZOQvkDk0nxssA5jcGDql31HCvmS6JLSaHD8XBqowA1VekJMemi5nLrzrZPc4ua1K1Sd_X9vaYNnPigqvbt7_zN_1B2K-JO1J0RV5uL6UF-443oR04-GA2kVgVeQ3AX6zxJ8oTtjFtONQ6zglUJI-7czYEcCil7fGax1f3GKMA9_H2SJynhMw5E1qG2wpt7TSiYVkUv_Ah0Evc_II" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثم مطیعی به یاد حسینیه امام خمینی خواند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/449249" target="_blank">📅 23:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449248">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZ23wlw9A6csmftqxHl_NVJ0H8N-e4oNmGrwYidak-qTxvxGnTyXrQBVZEPQczOBll0135CyfQ2fXm-sKUdKF_khEwcBaaNk2IFBROxysYfSCtETSaX0FCh4dFKOuNNgw3gkAX03mSuMWT8YJmvP9Ln1Ka3d_LYAT6sSqesxU_NNXv9tIWaCa9Sb8PY20wUSeqrw_nj_zo0hHwOCuJovM1SPLfygN5ekybC-9LRRfTsIVXgUZrRuE-z6J078oo08kHtXLK8o_n-mmZWZzAmvnRlJWmsMbj135eLmS7ynudpc1LEJER7o5OM3zYlhq5m7p9xHsrF3p2Kx07trS5YLNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ کشوری رهبری به این لطافت نداشته
🔹
اگر امروز مقام مادری را برتر از هر شغل و منصبی می‌داند، به این دلیل است که رهبر انقلاب تعریف جامع و لطیفی از نقش‌زن در کانون خانواده داشتند؛ به مقوله زن همچون «هوای خانه» نگاه می‌کردند.
🔹
«نمونه ادبیات لطیف و نگاه جامع رهبر شهید نسبت به زن و خانواده را در هیچ کجای دنیا و هیچ رهبری پیدا نمی‌کنیم. ایشان فرمودند زن باید «عفیف، محجبه و درعین‌حال در متن فعالیت‌های اجتماعی» باشد.»
📎
نمونه‌ای از تاثیرات رهبر شهید در زندگی زنان ایرانی را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/449248" target="_blank">📅 23:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449247">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تروریست عامل شهادت یک پلیس در کرمانشاه دستگیر شد
🔹
رئیس دادگستری آذربایجان غربی: تروریست مسلحی که عامل شهادت سرهنگ محسن چهری از کارکنان فراجا در کرمانشاه بود در سردشت دستگیر شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/449247" target="_blank">📅 23:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449246">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a29d9d41b.mp4?token=TBID7dFHiZyAnRq4ZdDD_dnj_-6iLovCnNh1D-8d9hTZ35GIt6G37ntGPrZ4RMk6ta15Jsw-62-uQeg2q6yKlZ7qOuFafpkd9zN4LI2JT8pQ6x8Np4zcMJv6vRVQ2Y3sMjY5VE_eyP-XeM7QBliDcauN43wi91tmE06VUnZbzzfIrtBOkqniM4f9EOY8rdAsAklkww38BiTVendUrAJBkUw-XgISWTp31jhJx2og44wqHxfVQvHd3BCb1dj5zz_bN7OBwLe8NdJLF-rYMg_NDNqzaTqkZyOfEX0Vj3Y-ugO3A3nA3ImxqxPHCneeOnjb66oH0rTC5zgVa1Bfab8h3xsy02B7hi-CREbHVWBNMfq48jrA25qrqGybAXT3LUA2aBlVpZHCtvUuxGQPLYDEnU821kcwQW44l1xz0ZEsN5Nq7cIIQxCZ7sh4BLboOwdRSXC0E9B9Cn9GGiYnK6C0AEfc2cMilqUhVzCJCCEEgfPzHWnzWMn2FlXl3zs7f5uQ93ghkFQh5ffUmFqTOeh-QhjCabndywBwRn9pe0IhStt0nq0iTtggGSTg-pXU8-dooarP4hRod58xqYQgCJpz5F36dIYzMC4wkW-L9cOk4urK7krj2IJ_suzktjALbahdYHRdCDUOnldCNawu4PBRsx_LBBeMVFfqS9pgVYXhYcY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a29d9d41b.mp4?token=TBID7dFHiZyAnRq4ZdDD_dnj_-6iLovCnNh1D-8d9hTZ35GIt6G37ntGPrZ4RMk6ta15Jsw-62-uQeg2q6yKlZ7qOuFafpkd9zN4LI2JT8pQ6x8Np4zcMJv6vRVQ2Y3sMjY5VE_eyP-XeM7QBliDcauN43wi91tmE06VUnZbzzfIrtBOkqniM4f9EOY8rdAsAklkww38BiTVendUrAJBkUw-XgISWTp31jhJx2og44wqHxfVQvHd3BCb1dj5zz_bN7OBwLe8NdJLF-rYMg_NDNqzaTqkZyOfEX0Vj3Y-ugO3A3nA3ImxqxPHCneeOnjb66oH0rTC5zgVa1Bfab8h3xsy02B7hi-CREbHVWBNMfq48jrA25qrqGybAXT3LUA2aBlVpZHCtvUuxGQPLYDEnU821kcwQW44l1xz0ZEsN5Nq7cIIQxCZ7sh4BLboOwdRSXC0E9B9Cn9GGiYnK6C0AEfc2cMilqUhVzCJCCEEgfPzHWnzWMn2FlXl3zs7f5uQ93ghkFQh5ffUmFqTOeh-QhjCabndywBwRn9pe0IhStt0nq0iTtggGSTg-pXU8-dooarP4hRod58xqYQgCJpz5F36dIYzMC4wkW-L9cOk4urK7krj2IJ_suzktjALbahdYHRdCDUOnldCNawu4PBRsx_LBBeMVFfqS9pgVYXhYcY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون‌خواهی رهبر شهید در موج ۱۳۳ بروجردی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/449246" target="_blank">📅 23:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449245">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqq06_v2RPaQcdUt89uL9UTOfpKAkfGszSWwDno58DeM2-SpHeLebpVs87QilgFaALl2T_dgA38yH3P2T82CzK4p-ZmJT_MvhfQTAvDg-MZXY4JaRWAtzowvvdj0Iuovt7B-oxfaEj88-fdCA18WAT0YKNKfHb7bHp9WRFx0herWXtpK73wodv-mLwCLMaT1JQc0HAPqJK-wLHv8A7ztTUwXIRDzarhWv9JMZ2gZpbIFihNMOcNqq28_vwnbq4o0e4sMLvttg1qvY3EIexmKE-YKzrt9s__yvt-Jv4VZIuRkbT8HPigBZ4OSCunjc0ynlUAPVomneLY_YL6O2zX_kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
این نقطه شروع کار خون توست...
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/449245" target="_blank">📅 23:18 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
