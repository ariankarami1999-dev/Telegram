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
<img src="https://cdn4.telesco.pe/file/OFccW3G-snRbKETu5yKM5h5vMcBMJddttnggzN0iDkRZWXkia1e8M9ryjSiKtyiPPL0wpBDuvfNX7aZisTjebp7_Wr8i8UFlU4HOmDF3rIeO2qc9MGnGATebPiaXpEUp7nxKxY1vXmeM3x5O9Tg6cWEg_QhDSvAKxPc56XMCJEh0aE-t8ovrcAfzssHZZa8JiElx5Xcc0jmadslMS7ylePVrKmrk1z1DcAG6H009cAPCaVZHUX11Qyk015Tzw-JDnMfeevsU637mvI0MY-t00L23LGOxuA2IV5Yq1QfHbdqvxA_wl5MG0pdwGaRIMTRyxEkSER7EJb5-XXskRHeFbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.04M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 08:27:30</div>
<hr>

<div class="tg-post" id="msg-678823">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a1c1e934f.mp4?token=L-TeP0U6VeY9WYbOsmv9FCVM_AfMzO2z84vcG69eYgmOXSRW36fkOC63jU51IC1iziud8EziPD9FKHLpKUpLSoD1YtAI-0Pc9t2Nt1p9TR5j9PdelxVz9FjKuDHmzs-0thvbRxJG-57vsVJhpCc8kAD9awyevJCWu28QGV4YldAyJh6UHETKE4xhGepWe3ZAagXKBZOI9d4-BQvQPXGODTEmLEaU2eQMBGhCYsNf0Ou37qu0AP_K5eesK_hg7DUyHB9bnzZoWL45XB_YKIXgbzjT0OyS164frSpGstwnZdZucP4hGtAfObkqoqxDdjBp3E39C28VoXF_Wi3flMlr1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a1c1e934f.mp4?token=L-TeP0U6VeY9WYbOsmv9FCVM_AfMzO2z84vcG69eYgmOXSRW36fkOC63jU51IC1iziud8EziPD9FKHLpKUpLSoD1YtAI-0Pc9t2Nt1p9TR5j9PdelxVz9FjKuDHmzs-0thvbRxJG-57vsVJhpCc8kAD9awyevJCWu28QGV4YldAyJh6UHETKE4xhGepWe3ZAagXKBZOI9d4-BQvQPXGODTEmLEaU2eQMBGhCYsNf0Ou37qu0AP_K5eesK_hg7DUyHB9bnzZoWL45XB_YKIXgbzjT0OyS164frSpGstwnZdZucP4hGtAfObkqoqxDdjBp3E39C28VoXF_Wi3flMlr1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این حرکات بازوهای سفت و خوش فرم، سرشانه‌های صاف و ایده‌ال، پشت بدون چربی و زیبا در خونه بساز! #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 311 · <a href="https://t.me/akhbarefori/678823" target="_blank">📅 08:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678822">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df107556f6.mp4?token=AfPTI2IMHFpjQz-beEbycR_W4SAipgmSQTt8jXbBxqVyLug7mWokHpxuPzHNJsuYbzb3-mazAjY93DgzusQqCXn8LL-sNtPvOxQCErsX6_5rA4Ru0b0rYPYX5o5jo0d1tQaCUuwRGoOmN7M42ZIITgKodgs2Ce90Ah92UKT35ofSM7CNOfhI87k2wVTWnAy-ZLzL_gtLFoNOvAVLrRq3B3K38kbw2lzA567TVFvZ6ugMR09r4PvRghDLIk69aMrsQaK3iOfeiMJq-YKvbFMeWa3eafQLm_7LchJhYibTbE7G9U03Cc92L8N3QVqKfCqQK9NlmvwxNe-uf8SX-Ltb1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df107556f6.mp4?token=AfPTI2IMHFpjQz-beEbycR_W4SAipgmSQTt8jXbBxqVyLug7mWokHpxuPzHNJsuYbzb3-mazAjY93DgzusQqCXn8LL-sNtPvOxQCErsX6_5rA4Ru0b0rYPYX5o5jo0d1tQaCUuwRGoOmN7M42ZIITgKodgs2Ce90Ah92UKT35ofSM7CNOfhI87k2wVTWnAy-ZLzL_gtLFoNOvAVLrRq3B3K38kbw2lzA567TVFvZ6ugMR09r4PvRghDLIk69aMrsQaK3iOfeiMJq-YKvbFMeWa3eafQLm_7LchJhYibTbE7G9U03Cc92L8N3QVqKfCqQK9NlmvwxNe-uf8SX-Ltb1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزی که یک انفحار مشکوک رخ داد
🔹
۶ سال پیش، "انفجار بیروت" که یکی از قدرتمندترین انفجارهای غیرهسته‌ای مصنوعی در تاریخ محسوب می‌شود، اتفاق افتاد. این انفجار معادل حدود ۱.۱ کیلوتن تی‌ان‌تی بود و زلزله‌ای با قدرت ۳.۳ ریشتر ایجاد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/akhbarefori/678822" target="_blank">📅 08:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678821">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
رویترز به نقل از منابع: ایران به کشورهای حاشیه خلیج فارس هشدار داده که هرگونه حمله جدید آمریکا با پاسخ متقابل علیه زیرساخت‌های حیاتی انرژی در سراسر منطقه روبه‌رو خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/akhbarefori/678821" target="_blank">📅 08:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678820">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
بازار ارز به کدام سو می‌رود؟
🔹
دلار پس از نوسانات، از کانال ۱۹۰ هزار تومانی عقب نشسته اما این آرامش موقتی و ناشی از کاهش تقاضای هیجانی است، نه بهبود بنیادها. مقاومت کلیدی ۱۹۰ و حمایت ۱۷۵-۱۷۸ هزار تومان است.
🔹
کارشناسان آرامش را شکننده می‌دانند و بازار در انتظار سیگنال‌های سیاسی و اقتصادی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/akhbarefori/678820" target="_blank">📅 08:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678819">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
صبح ها خرما بخورید!
🔹
کسی که با معده خالی خرما می خورد، کمتر دچار کم‌خونی می شود و بدنی مقاوم در برابر بیماری‌ها خواهد داشت، خرما با افزایش سوخت و ساز بدن باعث لاغری نیز می شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/678819" target="_blank">📅 07:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678818">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad59116b2d.mp4?token=rNIXrdrJWf5FIs4aTfk5CgB5R4Civ6Wo8T-Hob24-ZHFVvoakYVcF9UFY7wO5LTDbYdv857WUtQ9ebWYbt-mbwOYgC8eL9osY-S5AQ-UzIbAzSve5GKDbof4Il_hAf1M76DDE6sSKSD2_Whze_GW4pYbHr-fP4U4OaBxJsUqfeu-0fK_84B9J6r0nypIisLC5XnBwouvm8x_vfS3s1F-67uLEmlPjUh9xcgJJfxXrS8q00Nd4TCGx0HhtAuGUXPEh28K4hZQ1k5-mn-nBX7H7NKrOwKDcbKCoKnewl5FblSO0arL_n9RjjKqbSmNre8xGNiCHXGzaxqlyb3ETHAiVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad59116b2d.mp4?token=rNIXrdrJWf5FIs4aTfk5CgB5R4Civ6Wo8T-Hob24-ZHFVvoakYVcF9UFY7wO5LTDbYdv857WUtQ9ebWYbt-mbwOYgC8eL9osY-S5AQ-UzIbAzSve5GKDbof4Il_hAf1M76DDE6sSKSD2_Whze_GW4pYbHr-fP4U4OaBxJsUqfeu-0fK_84B9J6r0nypIisLC5XnBwouvm8x_vfS3s1F-67uLEmlPjUh9xcgJJfxXrS8q00Nd4TCGx0HhtAuGUXPEh28K4hZQ1k5-mn-nBX7H7NKrOwKDcbKCoKnewl5FblSO0arL_n9RjjKqbSmNre8xGNiCHXGzaxqlyb3ETHAiVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: تنگه هرمز قبل از جنگ باز بود؛ ترامپ حالا ادعای قهرمانی برای بازگشایی آن را دارد!
🔹
ترامپ می‌خواهد خرابی‌هایی را بر‌طرف کند که خودش به بار آورده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/678818" target="_blank">📅 07:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678817">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuoGwDIzuLJjwy432l0GxNIt0r06MUzZSZygsCVJtiq4DWV3MZZtECtR7UMj3x2dzVWyEpBOtg1HnGNMj_en69BJMM8CcdEiP5kqpngfv0--FrwKAcyv9aKd4fq5TSmpPwbcbsujRq41XaQmvM1VxCpEzfQFk4rzguI5OmFinUKdc8P0J9EBg-S6rTPnSORHkwkrfbFhcDqQUyhTjQCw1_59wIk7YTmFzw39qJceBBdRauWa9Ha5GIeJ2H1kO_Gqq05PZCcK_w5-pfPc4f8Fwo7XaHUdoxMPgkjf3XBGMQgjdL580VXAwkqkp5DzuAIwwatbufwbS-bis1QlYfbbNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۱۵ مرداد ماه
۲۲ صفر ۱۴۴۸
۶ آگوست ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/678817" target="_blank">📅 07:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678816">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کالابرگ سرپرستان خانوار با رقم پایانی کد ملی ۰، ۱ و ۲ شارژ شد
🔹
دریای مازندران فعلا تا ۱۶ مرداد مواج و تعطیل است.
🔹
ارتش اسرائیل: دو نظامی دیگر در درگیری‌های جنوب لبنان کشته شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/678816" target="_blank">📅 06:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678815">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ترامپ جنایتکار درباره ایران: وقتی این موضوع را تمام کنیم، قیمت نفت و بنزین به شدت کاهش می یابد و در مدت کوتاهی به چیزی شبیه به معجزه دست خواهیم یافت #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/678815" target="_blank">📅 05:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678814">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A71rfUUVB4_xqcxQw5LSu3bfZBfcze9SoJxsdxvjeKa_4VTovDt0wzjDQ0bQXyhVcPfT3IKvBafX5fA4YSsGmolqGaN8bp2QzVe1fXrpW8k9Cm6kGiX6hWR2d8TC5LQGLx0a4ceqkgla1OdWvBqIkkfCs59VpleaE9ffSQ8yGsRuXCZEus9nl5i_S7bc6wMSnZyU2KUVf48QvbODJTHXsUGCFnKFfm_PPFiB78qWs1Y-8FyftS4r_FlzFC6n_EmRJSV6t6fq-Y8l7xEYsxJLrG55tsXOYLCAiP840I7oPXYXUvnYp9uzdQxTIANRsDGPT-Pq8XuMFePVuQLyCJpVSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام رفقا، برای اعتباربخشی به یک کار پژوهشی نیاز به تعدادی پاسخنامه داریم
🙏
🗳
تو این نظرسنجی میخوایم درباره تجربه شما از برنامه‌ها، تبلیغات و فعالیت‌های
مرتبط با جام جهانی
بدونیم و بیشتر از چند دقیقه وقتتون رو نمی‌گیریم.
پاسخ
صحیح یا غلطی
وجود نداره و منظور ما فقط
نظر و تجربه شخصی
شماست و
هیچ اطلاعات شخصی از شما گرفته نمی‌شه.
لینک پرسشنامه
لینک پرسشنامه
ممنون از کمک بزرگی که به ما می‌کنید
🌸</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/678814" target="_blank">📅 04:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678812">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
واشینگتن پست به نقل از مقام‌های آگاه: نارضایتی ترامپ از وزیر جنگ خود شدت یافته /چرا که هگست از حامیان اصلی اقدام نظامی علیه ایران به شمار می‌رفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/678812" target="_blank">📅 03:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678807">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ادعای‏ معاون ترامپ: در درون نظام ایران، افرادی خواهان پایان دادن به جنگ هستند و در مقابل، تندروهایی نیز بر تداوم درگیری‌ها اصرار دارند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/678807" target="_blank">📅 03:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678806">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای‏ معاون ترامپ: در درون نظام ایران، افرادی خواهان پایان دادن به جنگ هستند و در مقابل، تندروهایی نیز بر تداوم درگیری‌ها اصرار دارند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/678806" target="_blank">📅 03:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678800">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bddc34601.mp4?token=Txx7OK8gGdyN84tQmOcQdJdoJa6i0lteB9WYx6UiFFTmI0ZOqiFtH-i4r3dVbp171Fyk6gJw3wbLr5-MOzgrjW-NUtt6PBXqXnUOHzM7figYrsIqs-sZ23jqH9hOeqxRVJncReehD4gDPimj5nnfa57wQU6lDk6IcNaPnFNtykElywcVzMpwEScjjhe13e_K9fMNHGfcdbhjYpwixnZ66MF0mFZcGUU8uWnlf7bWkovhMwv0ZoFWYz4P4AK-yf8su1ieIduxj6FSlc7IHnmC78lGaMkuIbXiPypDkgiNPgugAd9kiufgh3jwrvFvYvp0X_nLQKkRiN4RSuxIVg3kzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bddc34601.mp4?token=Txx7OK8gGdyN84tQmOcQdJdoJa6i0lteB9WYx6UiFFTmI0ZOqiFtH-i4r3dVbp171Fyk6gJw3wbLr5-MOzgrjW-NUtt6PBXqXnUOHzM7figYrsIqs-sZ23jqH9hOeqxRVJncReehD4gDPimj5nnfa57wQU6lDk6IcNaPnFNtykElywcVzMpwEScjjhe13e_K9fMNHGfcdbhjYpwixnZ66MF0mFZcGUU8uWnlf7bWkovhMwv0ZoFWYz4P4AK-yf8su1ieIduxj6FSlc7IHnmC78lGaMkuIbXiPypDkgiNPgugAd9kiufgh3jwrvFvYvp0X_nLQKkRiN4RSuxIVg3kzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم درباره قیمت نفت: ممکن است مجبور شویم دوباره آن را آپلود کنیم؛ می دانید وقتی آن را زیاد می کنیم چه اتفاقی می افتد، اما امیدواریم مجبور نباشیم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/678800" target="_blank">📅 02:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678799">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6568e534e6.mp4?token=WkJXott98fiwHAoDgz8XIPUP1K8MX_XPBJzCNv2LN0qjIQTi6PrF3FDgETEVCc3YW7zSshJL8x-dp_9_MH0IdEdFGNFIJg3YZGshUsEABRlotNEe-qrVV_g4ThHr5NXznMLfmm9x6YCcPJLy1z_jphpQ7ITbic5iIu9TGaCr6uNK9piLfsD4iFu1XnwFlStu_kiuXk_-bS4wpyN2tP6Oh1TEXI7QAYT6y7s-iObBzSALCThSLzd3aesgbq5ka_4ET8Wvd0qthtuZuuIfnaN5mC4HEfd82-4aaxUU4VtRd_wmxnMPWKhur1fdQjKnoPR4dyRQ-0kEul5R0qWwveb1Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6568e534e6.mp4?token=WkJXott98fiwHAoDgz8XIPUP1K8MX_XPBJzCNv2LN0qjIQTi6PrF3FDgETEVCc3YW7zSshJL8x-dp_9_MH0IdEdFGNFIJg3YZGshUsEABRlotNEe-qrVV_g4ThHr5NXznMLfmm9x6YCcPJLy1z_jphpQ7ITbic5iIu9TGaCr6uNK9piLfsD4iFu1XnwFlStu_kiuXk_-bS4wpyN2tP6Oh1TEXI7QAYT6y7s-iObBzSALCThSLzd3aesgbq5ka_4ET8Wvd0qthtuZuuIfnaN5mC4HEfd82-4aaxUU4VtRd_wmxnMPWKhur1fdQjKnoPR4dyRQ-0kEul5R0qWwveb1Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: ما در حال آماده شدن برای بزرگترین حمله از زمان جنگ جهانی دوم بودیم، اما ایرانی‌ها از من خواستند که مذاکره کند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/678799" target="_blank">📅 01:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678797">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da3608a66.mp4?token=cYxB2CLrhNq93fEGQw36Lu3hLUhifE9bFpp7avDrKmW_pStrRAcoYdJqhR8ggzZBm5e971Vqg56uYZkEnCtPM0oe7b5g65pD96kr4MS1EjCTX47QcVPp3AAaxMKxOuhVvk_t6Nzvz-uBGtPoy7FyvL789xLUaQg8k5rgE8gizgxg7YG6kUoqqSDk106uq5rWMdxnNaOBsBUBSYTBFtFPyyuRPG_rAMo2PC0x9GG9i0M2A7WXMaFC5qP-ncOTgnGyLsjuSMIXmOKXdC5CGXvFZe1ZLW_EfvBS4A05ouUd6CBvlK-vKNU935uV80nuVybLEDvWBIakCRZjA4g_crwsMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da3608a66.mp4?token=cYxB2CLrhNq93fEGQw36Lu3hLUhifE9bFpp7avDrKmW_pStrRAcoYdJqhR8ggzZBm5e971Vqg56uYZkEnCtPM0oe7b5g65pD96kr4MS1EjCTX47QcVPp3AAaxMKxOuhVvk_t6Nzvz-uBGtPoy7FyvL789xLUaQg8k5rgE8gizgxg7YG6kUoqqSDk106uq5rWMdxnNaOBsBUBSYTBFtFPyyuRPG_rAMo2PC0x9GG9i0M2A7WXMaFC5qP-ncOTgnGyLsjuSMIXmOKXdC5CGXvFZe1ZLW_EfvBS4A05ouUd6CBvlK-vKNU935uV80nuVybLEDvWBIakCRZjA4g_crwsMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار درباره ایران: ترجیح می‌دهم به یک توافق برسیم، چون نمی‌خواهم آدم‌ها کشته شوند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/678797" target="_blank">📅 01:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678796">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdtEwxcs_MTAAr6fUYcTw675IV2p-pK6gHFw6HZS3KkbWEuSaFFdxTE8miKK2UhNVEMzu1HZ6W32wyV0wK0lQhqdnKrBZtxSYsB7gIOZeD9SeJy4ErvwRCGTja6mbH0y1LEbs65T4SPhBqgKp_9vOJwogAbH5CIUe9YEwK19FdRIoM-k6587mvuRJh2ksRP_96HFV-sB1vX5FYJiwst6H7tJl3n0zUqNItplHWpfBwj2q66F9Ud6wmDo4kAnHbSQI543gVrls8EJsHwr6IwBYniSdqIbyZIi3QgGPx4NKcR7UweMYm0d0vIeDkCH8jZ-KQlpVq33_yvXBaG3J32p-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام رفقا، برای اعتباربخشی به یک کار پژوهشی نیاز به تعدادی پاسخنامه داریم
🙏
🗳
تو این نظرسنجی میخوایم درباره تجربه شما از برنامه‌ها، تبلیغات و فعالیت‌های
مرتبط با جام جهانی
بدونیم و بیشتر از چند دقیقه وقتتون رو نمی‌گیریم.
پاسخ
صحیح یا غلطی
وجود نداره و منظور ما فقط
نظر و تجربه شخصی
شماست و
هیچ اطلاعات شخصی از شما گرفته نمی‌شه.
لینک پرسشنامه
لینک پرسشنامه
ممنون از کمک بزرگی که به ما می‌کنید
🌸</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/678796" target="_blank">📅 01:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678795">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c7b20d47d.mp4?token=ELk4g1dwgyApomGftdBbfaJ4yzHLDO6z9K_MfcTschYdbOvqCEtqU4MOQ4qdUPgRCfRU4Gyf9kwrXGM19S8Ln4nXir0Int31PpW2c1-nEo46r5ZGjV2euGyaiWDluecXEmy4jdBuB1xxV-GU9ZURQSIhX9SoVC27drXoCAYEwkQHKafsoyGmrfv1NBb-rFw9hOZTomQytZVdwjDGeuFopazqJr-m9xSXD9MllTfzqh4Jud2RKwivXOj1_RB8hWe-OAm6AFLNy74H9Zv_FRNp2HUXbtzYKjIfcx0yWVcgHsoBxfO0O3QOUjnI6UUUsD60brGVdD4A73Z9KGCK7qOKaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c7b20d47d.mp4?token=ELk4g1dwgyApomGftdBbfaJ4yzHLDO6z9K_MfcTschYdbOvqCEtqU4MOQ4qdUPgRCfRU4Gyf9kwrXGM19S8Ln4nXir0Int31PpW2c1-nEo46r5ZGjV2euGyaiWDluecXEmy4jdBuB1xxV-GU9ZURQSIhX9SoVC27drXoCAYEwkQHKafsoyGmrfv1NBb-rFw9hOZTomQytZVdwjDGeuFopazqJr-m9xSXD9MllTfzqh4Jud2RKwivXOj1_RB8hWe-OAm6AFLNy74H9Zv_FRNp2HUXbtzYKjIfcx0yWVcgHsoBxfO0O3QOUjnI6UUUsD60brGVdD4A73Z9KGCK7qOKaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای‏ ترامپ متوهم: ما ضربات سنگینی به ایران وارد کردیم؛ با این حال، من دستیابی به یک توافق را ترجیح می‌دهم، چرا که ایران نباید به سلاح هسته‌ای دست یابد #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/678795" target="_blank">📅 01:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678794">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ادعای‏ ترامپ متوهم: ما ضربات سنگینی به ایران وارد کردیم؛ با این حال، من دستیابی به یک توافق را ترجیح می‌دهم، چرا که ایران نباید به سلاح هسته‌ای دست یابد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/678794" target="_blank">📅 01:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678793">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKvBkjWpl9knKloyQjQkd_XuG9PRb5403snUTHfjgvBb_AWsDaif4haf6J3zuPfH8XbhvJzQ6deYJJgEkSh-i2mL5v24T0NfYa189ufT3ozt6D8BhCn9Nh0igk0-HOEfRntTAGZ1eWwb_p384JiFNcQPwyrV4MFFJDX863_Y5RWBye89QQoxTYGiOlO8uTy8nO6DQ7dSDZV24evJixC-qEJPtMUAaNv37X1x_HM5cVKv8iaeZ9rRJo5o6DA6G0EnT8cnPdjhzjjYa8U4-Lsz_kIeSBn3ZWkbR_HvIqvUEczIMBe25o2OfRlBkxTFtijDMCiBImGMaXNrg1YDKvN5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرار غول‌های فناوری از خاورمیانه
سی‌ان‌ان:
🔹
جنگ علیه ایران برخلاف انتظار، فقط بازار انرژی را تحت تأثیر قرار نداده، بلکه امنیت سرمایه‌گذاری در مهم‌ترین صنعت آینده جهان یعنی هوش مصنوعی را نیز متزلزل کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/678793" target="_blank">📅 01:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678791">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ویتامینی که کمبود آن خطر ابتلا به زوال عقل را افزایش می‌دهد
🔹
براساس نتابج یک مطالعه تازه، کمبود ویتامین D در میانسالی با ابتلا به بیماری آلزایمر مرتبط است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/678791" target="_blank">📅 01:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678790">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee83dfda5.mp4?token=vsfK3mDWEFYMFV2S7yD0FgNQYV0DYZgFSsQPRClCHPnBkDqLgAVohC8WiEa0g3vpBS5lWOmW8u0TCx4VBy_WeiP2acvF5JCdozSwq-BMQqFPPX7wnMU740-WjtX5FigqIvD2zPew3tX6a8fDHI2KxQZySmixVO_8T7jbW-D0WT5TrWD9bdvDY36SwHHqca2l4E3O8b7gaJvSJ-6RmvNj0CiiIiU1lhZDqDYXDWtvJ9_oqnyNXEezm_1KzN_SpSuoJ_tqGg2qPMKfubngMlzRlDhvCeXbIq-z45LAGKDEkA_t4zlJrkaOWGQokmE7GhHwvmIQlxvpB4qgejBVz2q4JBJy4KxaxKUwdZkixnayrLsraH9T-_kVY7f4ktSr5_8EcDY00oCouxAuSPjERUjx_NgekUktwm9u6aESoEDAn4McO44Lo3wv5LawvgUzctYmLFcTmrIe_iXP8coL31qE-_-7TUcAV7YNmPZrL9_YPWuRxNzpeKW82QqHqZpk288GnJESxVKtQ_YBAMMJnMmfYd64DNSImu2r2qeOr6W0V1h8T70qJErdwSPHB8vXPuvJJdE4jJKCYFQ7HHUTZgwzPlRorC9QBwP9ybQ5lXlC7MaT_B80xklSNEovwz3NXwuVKupBwnwMDmSi4sr5x4PjtxriRcVB6MKy2UyGd2SNtAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee83dfda5.mp4?token=vsfK3mDWEFYMFV2S7yD0FgNQYV0DYZgFSsQPRClCHPnBkDqLgAVohC8WiEa0g3vpBS5lWOmW8u0TCx4VBy_WeiP2acvF5JCdozSwq-BMQqFPPX7wnMU740-WjtX5FigqIvD2zPew3tX6a8fDHI2KxQZySmixVO_8T7jbW-D0WT5TrWD9bdvDY36SwHHqca2l4E3O8b7gaJvSJ-6RmvNj0CiiIiU1lhZDqDYXDWtvJ9_oqnyNXEezm_1KzN_SpSuoJ_tqGg2qPMKfubngMlzRlDhvCeXbIq-z45LAGKDEkA_t4zlJrkaOWGQokmE7GhHwvmIQlxvpB4qgejBVz2q4JBJy4KxaxKUwdZkixnayrLsraH9T-_kVY7f4ktSr5_8EcDY00oCouxAuSPjERUjx_NgekUktwm9u6aESoEDAn4McO44Lo3wv5LawvgUzctYmLFcTmrIe_iXP8coL31qE-_-7TUcAV7YNmPZrL9_YPWuRxNzpeKW82QqHqZpk288GnJESxVKtQ_YBAMMJnMmfYd64DNSImu2r2qeOr6W0V1h8T70qJErdwSPHB8vXPuvJJdE4jJKCYFQ7HHUTZgwzPlRorC9QBwP9ybQ5lXlC7MaT_B80xklSNEovwz3NXwuVKupBwnwMDmSi4sr5x4PjtxriRcVB6MKy2UyGd2SNtAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار رسانه صهیونیستی اینترنشنال از درماندگی صهیونیست‌ها در برابر استراتژی و قدرت ایران می‌گوید: دیوانه شدیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/678790" target="_blank">📅 01:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678789">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6957964a42.mp4?token=TtohpKSV9wN3QgTzTdhyaBXlDRxniCioNZMbF1BwvfG-yA4LmA1KielAuSS1dX2LnKa1iXy6w9rlr3szxsCel5rYqnFYYB0UCX6-5R04vy9g_eGmWdZ8AESf3r4oHo4TBl3w8nwEop2IKVsvQl5o-kIPa9zHBaDPhfoeHIm5gOzY0xR2PE4q_GyKJVZIwALN8YmnnD-7oL0WMev68mmxL5LQr4OZbtxxEitpD48lUXEQ2HEKn8qWiSDCZBqUMHBGJK0cDb_sAD6hPT6cuuBMGbL3Vt2d39PbBak46gDoYnwSB9NgLf9X-pw_Jf8SvIJTINhpHwRCOuOctqNEBk0Yxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6957964a42.mp4?token=TtohpKSV9wN3QgTzTdhyaBXlDRxniCioNZMbF1BwvfG-yA4LmA1KielAuSS1dX2LnKa1iXy6w9rlr3szxsCel5rYqnFYYB0UCX6-5R04vy9g_eGmWdZ8AESf3r4oHo4TBl3w8nwEop2IKVsvQl5o-kIPa9zHBaDPhfoeHIm5gOzY0xR2PE4q_GyKJVZIwALN8YmnnD-7oL0WMev68mmxL5LQr4OZbtxxEitpD48lUXEQ2HEKn8qWiSDCZBqUMHBGJK0cDb_sAD6hPT6cuuBMGbL3Vt2d39PbBak46gDoYnwSB9NgLf9X-pw_Jf8SvIJTINhpHwRCOuOctqNEBk0Yxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: کانادا رفتار خصمانه‌ای دارد. آن‌ها همین‌طور هستند؛ واقعاً برخوردی خصمانه دارند
ترامپ پلید در مورد کانادا:
🔹
کانادا بدجنس است؛ آنها بدجنس هستند. من مردم کانادا را دوست دارم، اما رهبری آنها بدجنس است.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/678789" target="_blank">📅 01:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678786">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
حمایت تسلیحاتی اسرائیل از امارات، این بار با ارسال پهپاد
🔹
بر اساس اطلاعات افشا شده، در سال ۲۰۲۱ جلسه‌ای بین مدیرعامل شرکت «البیت سیستمز» بزرگترین تولیدکنندهٔ تسلیحات اسرائیل، و رئیس دفتر سیاسی-امنیتی وزارت جنگ اسرائیل برگزار شده و در آن فروش احتمالی سامانه‌های تسلیحاتی مختلف به چندین کشور از جمله قطر، عربستان سعودی، اتیوپی، رواندا و ترکیه مورد گفت‌وگو قرار گرفته است.
🔹
بر اساس این سند، به البیت مجوز فروش پهپاد هرمس ۹۰۰ و همچنین مهمات سرگردان «اسکای‌استرایکر» با بُرد محدود ۶۰ کیلومتری به امارات داده شده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/678786" target="_blank">📅 00:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678785">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمان آماده‌باش در یمن؛ صنعا از مرحله جدید تقابل با عربستان خبر داد
🔹
نخست‌وزیر سابق رژیم‌صهیونیستی بار دیگر قطر را دشمنی خطرناک توصیف کرد
🔹
روسیه: ۲۰۰ پهپاد اوکراینی را در طول یک روز سرنگون کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/678785" target="_blank">📅 00:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678783">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xeu4tGLYttwBZ9R7FIHYpJ2vY1vxSDAluUFawWaaViGZ0uqI_UFXjWB-ZeVXGizhHi5ZFkxc5bI5pCg8T4tgDJLxlXty6RJg8VLIjNaBcwLTyRdyxJOhVdtw2TeU8GvGviK5W38Ntb3NEx4C8sH4l2aWrVXdpRHjZAsP7onqqNQMejh8kK7UiLHl8bJuZNvZAjmO29tTyJa6ytVgIcWnyzL3vySINAZkddM-zbkTlJkAmqDNGXZ1aymWIapKJ71FBlcY7_BPOEaSR45UNW3qBnvKsoujl3g46Z4UH3JKh2STa10EIrB08Tg8hic-wrV32V2dso_eySt4KfmsZxLP_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایرانِ همه
بخش اول گفت‌وگوی صریح و تفصیلی رئیس جمهور امشب پخش شد، پزشکیان در بخشی از این گفت‌و‌گو به نقش مردم اشاره کرد:
🔹
اگر تا امروز مانده‌ایم، به‌خاطر مردم نجیب ایران بوده است که ما را نگه داشته‌اند، نه‌‌فقط آن‌هایی که در خیابان بودند، بلکه آن‌هایی که در دلشان عقده‌ها و گلایه‌هایی داشتند، اما به‌خاطر ایران به خیابان نیامدند و مشکلی ایجاد نکردند؛ نه‌تنها مشکل ایجاد نکردند، بلکه همراهی، همدلی و هم‌صدایی کردند.
🔹
هشتصدوبیست‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/678783" target="_blank">📅 00:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678782">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54cb9690d6.mp4?token=SKY8xidIJ_bLErScuG2WZCYdRNmMAD1L7VZ7OIP0-39GtuORpAjI8L7abLI4r5yTBbTwyjDnxgkv8D8aAG5_wrnS0CMiEMX-rfmrmUDtqOf8dRyUspeXSuBfOUVlP6QwxeTxOptIgRis9qMS_dG5dq24aMyqjkXco9ZM7MlafMaf-ZrJKaWi7heedSSRrxV9T87RuqkE3JgHKuSMQAJJRDmv0CC2LtAyqToeu8mWUu8754P1kfwgF-AIboFnfmcHsV_gPJw_ZnszKGEB8FK2MJjVk-kPM84LIZY7uVRkfXrIhf272fydaLRqlNsAHgS_FiKN3y_cf3AC6hWb3mozVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54cb9690d6.mp4?token=SKY8xidIJ_bLErScuG2WZCYdRNmMAD1L7VZ7OIP0-39GtuORpAjI8L7abLI4r5yTBbTwyjDnxgkv8D8aAG5_wrnS0CMiEMX-rfmrmUDtqOf8dRyUspeXSuBfOUVlP6QwxeTxOptIgRis9qMS_dG5dq24aMyqjkXco9ZM7MlafMaf-ZrJKaWi7heedSSRrxV9T87RuqkE3JgHKuSMQAJJRDmv0CC2LtAyqToeu8mWUu8754P1kfwgF-AIboFnfmcHsV_gPJw_ZnszKGEB8FK2MJjVk-kPM84LIZY7uVRkfXrIhf272fydaLRqlNsAHgS_FiKN3y_cf3AC6hWb3mozVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شروع عملیات گسترده موشکی روسیه علیه مواضع اوکراین
🔹
در این موج حملات بیش از ۴۰ موشک شلیک شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/678782" target="_blank">📅 00:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678780">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: بر اساس پیش‌نویس توافق، نظارت بر تردد کشتی‌ها به خلیج فارس در اختیار تهران قرار می‌گیرد، اما عوارض یا هزینه‌های خدماتی دریافت نمی‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/678780" target="_blank">📅 00:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678778">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c7abd15f.mp4?token=L98KXsewAxQCdMqkEY5vYEC_6XGMywTvzFdHkOPuONcwpAgMne2GRrU_u9Zz1XeMMUui4oRDOucLFjqDD7oQPjyoxT-Sw5wstREAkZ8UUVRGEDDDkG2B-yWdlah2RZQVqev0cmJmpgna-mfcleMj2b1HQ3DbKSgZct4_b0P5CSPZtDXriWV6YSCiABwwd5nTMqTJxoQskcihDYbr-Vv1Sjc28a7r24tZ3uX9ik9SbUKsjTVSftKZ6yXztVpeNRLQxXTYaJYaAYFOXaOU7rBSTZHVJx_JjL10HaMj1tzk65onmdbR7ZxEMl-i91irglf-F7cStrMQocWVViZOyPgyqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c7abd15f.mp4?token=L98KXsewAxQCdMqkEY5vYEC_6XGMywTvzFdHkOPuONcwpAgMne2GRrU_u9Zz1XeMMUui4oRDOucLFjqDD7oQPjyoxT-Sw5wstREAkZ8UUVRGEDDDkG2B-yWdlah2RZQVqev0cmJmpgna-mfcleMj2b1HQ3DbKSgZct4_b0P5CSPZtDXriWV6YSCiABwwd5nTMqTJxoQskcihDYbr-Vv1Sjc28a7r24tZ3uX9ik9SbUKsjTVSftKZ6yXztVpeNRLQxXTYaJYaAYFOXaOU7rBSTZHVJx_JjL10HaMj1tzk65onmdbR7ZxEMl-i91irglf-F7cStrMQocWVViZOyPgyqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شروع عملیات گسترده موشکی روسیه علیه مواضع اوکراین
🔹
در این موج حملات بیش از ۴۰ موشک شلیک شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/678778" target="_blank">📅 00:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678777">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1O5Er7UhcQYILnF29_xT-2w-SwZdXarZAW7A9NFFye_ITk9kUn2tlp-Egv_mU6iqRxXORNfX2w9yl1M0HddnU2R1lJoEXnfbUFO0w91FO4xZzKXU3Xs42tJznyBSRtGFJB9c6jgazANQ6vdOeMbuiBql6HX25uldZ_3y9XpnVuquW9nqfKCoGyExrDQIkS7L6aVXdx4s41SwSHuylWt5yGVTCgSaO-yKFlb6jb08mv1_-y2JNeAL4iUz-6pPZL0yFVTqgGMr5lo3IOHzRYxrhaxSKFZDnWaIaBtWIWK909fPNyOn3QYUSn7mDyYc1NskxUIZ0YZv7HuIB5HowoPBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/678777" target="_blank">📅 00:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678776">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIssSYb_0jsfT-1jaAQiE6Qqu4nLi6mMRzsdaoaJvI5kQX5wQTxFCYqbNIR12CZV-ESg9v3RAEG3Hrc_1RmtNkM4RZcbXVBwljD4iaMysWPbouSs3ma2TGjEl49dOfW8Acqokr7_mNgQbZGMopBpRiEz7H9PYLEe-xci_IrgIGW1oujgZ8wT0BxSQkjckjwtpJAmdWgXlmT_6ZWZFkCdrqJLI9WyYsQugzzkrw2Feq-tgJ1PsxnbMz7f0MH4gdql8kl418ZgIOWwZiwvD-rC5QJBydWwkOgpPC4JE_F_If8M7S6Y7clW_QxQCvRhzqAS7lHNZ14atDKMNLUffrFp5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حاشیه‌ای تلخ در مراسم ختم اکبر عبدی، انتقاد کاربران فضای مجازی از رفتار عجیب برخی افراد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/678776" target="_blank">📅 23:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678775">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6C44MW_0cfBQ5p2wPXnc3O7O8Gaom3rs4p1BkVyDN_cpHZ4JEqD1ZC8rSnHQnYjdfU-MB5Fvu_4lh57qsT0x6kicPBjmE4Eo_kIL8LlEWVfGeNdgi5GFPTA9I3x7CSUs09Nbb2Ivqga7mit9AaMyS84AsiQA5eDAUkKOZeJYQqDCK8UmGyV-wCkSyHpzDPajxysR4M3dZRgz5_pB3jA0jwUuKg78sb4vpAWVhq7QVP1siNTJ4Y8iQxVO4PnM2a8ZQ8kZAUh5omndteODAsBHZAYA2ARvFvsCK85y6R5DYkBIQ3ymr6oB3dxcQf09PtEWqnMnB-kqHBTbWomelllng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف صدها قرص نان از خانه‌ای در اراک
فرمانداری اراک:
🔹
فرد متخلف با در اختیار داشتن چندین کارت بانکی، به‌صورت روزانه از نانوایی‌های مختلف اقدام به خرید مقادیر قابل توجهی نان کرده و پس از انتقال به منزل، نان‌ها را برای خشک شدن روی پشت‌بام پهن می‌کرد تا به نان خشک تبدیل کند.
#اخبار_مرکزی
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/678775" target="_blank">📅 23:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678774">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔹
خبرهای متفاوت هر روز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
پزشکیان توضيح داد که چرا وقتی رهبری «علی الاصول موافق نبودند»، یادداشت تفاهم ایران و آمریکا را پذیرفتند
👇
khabarfoori.com/fa/tiny/news-3235815
🔹
جزئیات مورد بحث جدید از موشک خیبرشکن ایران
👇
khabarfoori.com/fa/tiny/news-3235764
🔹
لفاظی جدید نتانیاهو علیه ایران
👇
khabarfoori.com/fa/tiny/news-3235795
🔹
طوفان حاشیه برای همسر بیژن مرتضوی | نرگس فرخی کیست؟
👇
khabarfoori.com/fa/tiny/news-3235690
🔹
واکنش عجیب آیت الله خرازی به اطلاعیه روابط عمومی دفتر رهبر انقلاب
👇
khabarfoori.com/fa/tiny/news-3235548
🔹
با نصب اپلیکیشن خبرفوری، از خبرها جانمانید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/678774" target="_blank">📅 23:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678773">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcnZ3jzVaPVM2heqV3gRlT91qKgbg3zzA6NwCgEWT6sMc_Dd9Yvw4vMIKovPtLsQPC5N0iaFWRZdiaMWutFtytCAEM60x0Tq2z50EVdsx1NH4BSSTtmy6FnjLRF5AQosVQNKsCInUfFIETdjK77-JUgXXxcDs7x_f_u2gqYwvOYBUVf7uXZi_XFsgGqDgjaVWXYkaIcCrc2MRbgFppQGDxQCmUUp9GdI4mtxygJtieZ9sO-CC3OE_fx6_Gl03mlb2zO9EdXe7nEzNnGVDQ1EEYDlo-bg1T4R7jCoJz1xwlACcX7ggsXDCkWEIwF0XeevmFyuLzRUqeRjulmMTD_CNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حداقل سن دریافت هر نوع گواهینامه چقدر است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/678773" target="_blank">📅 23:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678772">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
رویترز به نقل از منابع: ایران به کشورهای حاشیه خلیج فارس هشدار داده که هرگونه حمله جدید آمریکا با پاسخ متقابل علیه زیرساخت‌های حیاتی انرژی در سراسر منطقه روبه‌رو خواهد شد
🔹
این هشدار در جریان مجموعه‌ای از تماس‌های دیپلماتیک سطح بالا منتقل شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/678772" target="_blank">📅 23:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678771">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTs3fHTXzmZTYBHSzAeJVyt_wt5LZMaFnGSULak3o95PaGY7KjH2IaSaJc6W8ttYJMWrBkVLjxCE6Th96axKYPng1EhmrKRnRH214_rqwrk0zarvSFt0qYWXQCNbqOUz7p8_1k1F1tfn8wpVSs9LvjtmD41ML6jMBAwti1GlxnnsBQzUsbx4BwLPpFNOfRZ1Vxv811mu7ExXrQAht6oVlFcT1Qc6uM8VuQQTOwflsENXWgKFN2vugSXGl15CV_UIlIxFDFeYGcEa0QeP5y715zOZH5cxST9fzeEOzTFr8Viz4fRUwwMvtUa-GSdwBHxHaRMoNpVWvAZenF5yhwtNmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اندیشکده هادسن: چین می‌تواند از آب‌های سرزمینی خود با موشک اتمی به آمریکا حمله کند
🔹
چین به سرعت در حال نزدیک شدن به یک سه‌گانه اتمی است.
🔹
در ۶ ژوئیه، چین یک موشک بالستیک را به مسافت بیش از ۷۰۰۰ کیلومتر در اقیانوس آرام جنوبی آزمایش شلیک کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/678771" target="_blank">📅 23:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678769">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QTTudjMxLd1cFfyeDViwBPM98eYgIquYdVWlsmoG5IEmrQJiK-DNIPg6e3EkYQ9MEA_MHgOscb5O0eCQTY0OxO41PChKPJZ3SB2kmXdoZzLlFGoWTFtgVy-CM-TEtigURwXa3Gu6hfB8W46YDkR42HC5_5seCvI5VX5JiP_MeBKSazf_YI3mI7k5PfMhLnJrkCC_avlOibdrMXcOWOFZFcntXkWei2_k88Omsy_29ByuXVYxVpEOCwzug6Yzp9KPAutTTQFiuyFUiyRLk7DdYal4_ywinRcLikHEO9G3We6bm8WOsRNscZTr4tLJIbUP8gER_09JAf9Kc5ZXD4Z3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SuzyFRo0YqB-PksP_eEoFoUgaKdvU99jSvu4sA3cWfGqxMLkwAcfOntW-Scncv6A7mIJXSqrERhH2fSNDUxtY8mEAJuZ2eXLptg6F4zavuJ2U-FNf4yWNB24eEpHmVORQu77eu_YUpp0XC1xfbb71nGp1XOR8hJv7Rk9cDteUia0orAvLEgWXyCDSomj_YL3v-D2XvM8DortHDCeaOT5GCPO4x4NFWIZ3Rd7J0KrC-zKRYcQSNFpK2WgXT888ZuFUeVItMe3osBPAFtAjO15jeAor3WrPEqQv7-2gK4D_ZPbi6uVcYHH-vlja3EH4Iin8fMD_YBx-rVu2BsDF7haPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جوجه بلدرچین یک روزه که اندازه یک بند انگشت
است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/678769" target="_blank">📅 23:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678768">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMIiyvtDs97QZ12gbRMkcke7_DZe3u3XzE-7PYVkbWb_0SYJ9UNsubmCzD6TMxwk8y9N9oMML55tioQS3zoOZkqYWJ6SsKg2ohyNN88NJYJl2JTcc2oSZ1vFvD61VICSnwWWAprH_7aISxPvXEk9v39rgzCjhE_LNDAqo35dzIqtZ-eHOqyOfBVG5L25yrSkZ2UgcsbUjUaBrQ6qRaIRhpxggdZ483puZpfQ1VUwVtm06MLk5trAdwACE7NZJvHGslosW8GlKbKdaKCaU3qhICoTXS5EBRx0quyegGLb1DZ6KrIRdD_dvn2zxp9m_yJ5S5xTw2kyHxbgwS_MN7Lrjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اختلال در دسترسی کاربران ایرانی به چت جی پی تی
🔹
از ساعاتی پیش، شماری از کاربران ایرانی از اختلال در دسترسی به سرویس ChatGPT خبر می‌دهند. بر اساس گزارش‌های کاربران، این سرویس بدون استفاده از فیلترشکن برای بسیاری از کاربران داخل ایران باز نمی‌شود، اما با استفاده از ابزارهای تغییر IP امکان دسترسی به آن وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/678768" target="_blank">📅 23:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678767">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb6e894ba1.mp4?token=Izx11BLF-li7GeIMbRXis4VasVk3o9ONzIwVWMU9P4Po9Gfnlh3F4NBeDvzUKB_0LmaES6LyAaEdWlhx_4HJd-Lmw1wfvdG5iREIUZ0Dbu4NbIaxdyNcoAUBkf9uEo4m6ZMetJOIVV6Pw7-eNpGJfkWlDU9rcYn6vT8FGXW74_wvg0AVGmB49pBXFMHUbnqPMbM5Epvp06wKZ5oAAZfWOMc61osYZezusRCmUxX2kcATTqjqVnRn58Z-a52TbjL9iBD_aeSek3tcSswKQjbROT4DSeoagalXuvKsa0-FKkawGR7AmiVTfWw8m9Fm475gicWqHe22Q7XvEpA_LZCGTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb6e894ba1.mp4?token=Izx11BLF-li7GeIMbRXis4VasVk3o9ONzIwVWMU9P4Po9Gfnlh3F4NBeDvzUKB_0LmaES6LyAaEdWlhx_4HJd-Lmw1wfvdG5iREIUZ0Dbu4NbIaxdyNcoAUBkf9uEo4m6ZMetJOIVV6Pw7-eNpGJfkWlDU9rcYn6vT8FGXW74_wvg0AVGmB49pBXFMHUbnqPMbM5Epvp06wKZ5oAAZfWOMc61osYZezusRCmUxX2kcATTqjqVnRn58Z-a52TbjL9iBD_aeSek3tcSswKQjbROT4DSeoagalXuvKsa0-FKkawGR7AmiVTfWw8m9Fm475gicWqHe22Q7XvEpA_LZCGTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای اولین بار در تاریخ المپیاد فیزیک، کیان ضرابیان موفق شد به نمایندگی از ایران در المپیاد جهانی فیزیک ۲۰۲۶ برنده مدال طلا شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/678767" target="_blank">📅 23:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678764">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7iiwjgfBUxu_UHxP2aEE4f0xo7wpFQ89fsRU7N0mAML_Wum7iAadIUMSQHAbMkxxuybCJ9ArntCKc3mhxMYf_upZkwe0jNe8YHUIJ9JpQynVj665ApnCpLdcGbJpZL76jkwwRxnHGvruYIofpu6nuh6tDH3tZxbl-wsi7muISWgV_VygO2h94qmrhYC0Ujb6xP5NXgXCKabUommqJtW9UaDp58WRgKuVOmhGZjHrDd5jdNZ-HKH-T3UZcELSibK5Fu_YQWaJu92DuafUGKq88_Ite3yOYczM5bUAj5M-SQBMeJNt8yX617-UMMc7T4ej1IeU-8Ph5Xr3fRPt3MX2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله کم‌سابقه روسیه به اوکراین/ موشک مرموز روسی که کی‌یف را به آتش کشید/ پاشنه آشیل زلنسکی چیست؟
🔹
آنچه در حملات بامدادی روسیه اهمیت داشت و می توان آن را رویدادی کم‌نظیر دانست، دقت به شدت بالای حملات، ضریب موفقیت بالای حملات و عدم رهگیری موشک ها توسط شبکه پدافندی اوکراین بود.
گزارش تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3235814</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/678764" target="_blank">📅 23:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678760">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
کاربرد هر کدام از مُسکِن ها چیست و برای کدام درد مناسب است
🔹
پیروکسیکام: ضد التهاب، ضددرد، تب بر
🔹
مفناميک اسيد: دردهای قاعدگی، دندان درد
🔹
ناپروکسن: ضددرد، ضدالتهاب با عوارض کمتر
🔹
نوافن: دندان درد، سردرد، دردهای عضلانی و مفصلی
🔹
ژلوفن: ضد التهاب، ضددرد و سردردهای میگرنی
🔹
ایبوپروفن: آرتریت، درد پس از کشیدن دندان، ضدتب
🔹
استامینوفن: ضددرد، ضد تب
🔹
استامینوفن کدئین: ضد سرفه، مسکن برای دردهای متوسط
🔹
آسپیرین ( آ. اس. آ): ضددرد غیرمخدر، تببر، ضدالتهاب، ضد لخته خون
🔹
آکسار (آ.ث.آ): ضددرد، ضدتب، ضدمیگرن
🔹
بدون تجویز پزشک هیچکدام نباید مصرف شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/678760" target="_blank">📅 23:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678759">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a98862a57f.mp4?token=NPKLS_Cs40l_TQN9sGf_7uMtaFQQKdvLlRYqcWg6Nexwb9VwnlxM8kScKQ9bQ5FJtF0gEkFDxSU3Cz-08lHxKjBauAadE220iw9-ZRaAf2Zy251MRhW2r18HvSsNUzEU4J3Tnse4p4HuZY8JLsuRzbw2Pwqwp-noaMdMVwOFiwLtf-eiyX9n7MW0qrLCUWDrrS9LL35Uu1TvyAs2UJFQth4cTV6C7J-vReek3q9eE6XumJMhpzqcf8zXzHy02h5jJV42zEK-l9OrkqVNLX-QrHYCynnerJippE81GRVi6UgCnAn7jKtV6tocVVkHd5oCOdZAar0UOd0M3qMUlgyDr6nBcxMTePogeAwZsQcoL0I7CeJHGvz-4uO8UNDB2DFC9ifteumqYtiFZ0X9ZGZ0P200AvuZKk0TxThtEp3MWPbDv7LCsD7vrq73Jjm9_PEzXnupfk5yTynhlnI-FnBxlefqVuGMNMry78mopYUus1CbOpa2DiFCxFvBUCg7hHUECZa9iFwwZ8ylPW_TkexgTULRIsF2Lt3U6bTKDj0u3hGTUfEhYDZcNHYxC0DIR_CG2tEbzmyBn2aBKTXi3wzV-9Q2QFjKOUEjLzapo8aGqb9X_gw5o-ghxyIclAKDyoX9yMnuEXGlCnge-F_aSoHbgBgzhXeFmso3JBYjQrtzZEk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a98862a57f.mp4?token=NPKLS_Cs40l_TQN9sGf_7uMtaFQQKdvLlRYqcWg6Nexwb9VwnlxM8kScKQ9bQ5FJtF0gEkFDxSU3Cz-08lHxKjBauAadE220iw9-ZRaAf2Zy251MRhW2r18HvSsNUzEU4J3Tnse4p4HuZY8JLsuRzbw2Pwqwp-noaMdMVwOFiwLtf-eiyX9n7MW0qrLCUWDrrS9LL35Uu1TvyAs2UJFQth4cTV6C7J-vReek3q9eE6XumJMhpzqcf8zXzHy02h5jJV42zEK-l9OrkqVNLX-QrHYCynnerJippE81GRVi6UgCnAn7jKtV6tocVVkHd5oCOdZAar0UOd0M3qMUlgyDr6nBcxMTePogeAwZsQcoL0I7CeJHGvz-4uO8UNDB2DFC9ifteumqYtiFZ0X9ZGZ0P200AvuZKk0TxThtEp3MWPbDv7LCsD7vrq73Jjm9_PEzXnupfk5yTynhlnI-FnBxlefqVuGMNMry78mopYUus1CbOpa2DiFCxFvBUCg7hHUECZa9iFwwZ8ylPW_TkexgTULRIsF2Lt3U6bTKDj0u3hGTUfEhYDZcNHYxC0DIR_CG2tEbzmyBn2aBKTXi3wzV-9Q2QFjKOUEjLzapo8aGqb9X_gw5o-ghxyIclAKDyoX9yMnuEXGlCnge-F_aSoHbgBgzhXeFmso3JBYjQrtzZEk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر گره، قصه‌ای را پنهان کرده است؛
قصه‌ی دست‌هایی که هنر را به میراث سپردند...
🔹
روز تبریز مبارک
#اصالتلی_تبریز
#تبریزگونی
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/678759" target="_blank">📅 23:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678758">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعایی جدید از وال‌استریت‌ژورنال درباره توافق بر سر هرمز
🔹
در ادامه گمانه‌زنی رسانه‌های غربی درباره توافق بر سر تنگه هرمز روزنامه وال‌استریت‌ژورنال مدعی شده که ایران و عمان در حال نهایی‌سازی پیش‌نویس توافقی برای بازگشایی تنگه هرمز هستند که بر اساس آن، نظارت بر تردد کشتی‌ها به خلیج فارس در اختیار تهران قرار می‌گیرد، اما ایران عوارض یا هزینه‌های خدماتی دریافت نمی‌کند.
🔹
به ادعای این منابع طرفین بر سر نکات اصلی این پیش‌نویس که شامل ایجاد خط ورودی در نزدیکی ایران و خط خروجی در نزدیکی عمان است، به توافق رسیده و آن را با آمریکا، کشورهای منطقه و مقامات ارشد ایران که هنوز باید آن را تأیید کنند، به اشتراک گذاشته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/678758" target="_blank">📅 23:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678757">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f04aac33.mp4?token=G9HyOUPs6405JTAdGWHdnGg9Myd5-3OEziB2QE_oi25Y263cXJtbBmJ6dnogvrpZyiqbblSNZ38egsaLDgbmlmbtznQYuK6hwPOd2W1Apw7l1J4-e9XzQhPr16yJMCwOPxPS4kw1Bwz3PusBx_c8YVYiE9YobadRLovt49GWUflyWM-RbR74hmbikQf-crxwfBfd5rDFAF5s54uTeG4hE9M2OtqlGYGsvoeA1YtkudfeJrP-xt8jqpvNEziZJ7G_wB-oy0NRfiTupVBdvm0oLTvaf5WVFze-HgiWKk5CbvhQPtCRtwwR47nxGNBTDQTSwSxlHyaOd_ZrCVWO5SJRXIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f04aac33.mp4?token=G9HyOUPs6405JTAdGWHdnGg9Myd5-3OEziB2QE_oi25Y263cXJtbBmJ6dnogvrpZyiqbblSNZ38egsaLDgbmlmbtznQYuK6hwPOd2W1Apw7l1J4-e9XzQhPr16yJMCwOPxPS4kw1Bwz3PusBx_c8YVYiE9YobadRLovt49GWUflyWM-RbR74hmbikQf-crxwfBfd5rDFAF5s54uTeG4hE9M2OtqlGYGsvoeA1YtkudfeJrP-xt8jqpvNEziZJ7G_wB-oy0NRfiTupVBdvm0oLTvaf5WVFze-HgiWKk5CbvhQPtCRtwwR47nxGNBTDQTSwSxlHyaOd_ZrCVWO5SJRXIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهدات بلاگر روس از مهمان نوازی و صحنه‌های متفاوت اربعین امسال
🔹
جمعیت کثیری امسال با پرچم قرمز آمده‌اند فقط برای آنکه نشان بدهند مصمم هستند تا انتقام خون مرجع دینی و رهبر عالیقدرشان را بگیرند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/678757" target="_blank">📅 23:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678755">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2937305fdb.mp4?token=iBrfp-hiEzK9jveMd5eNXF0HZd2SrqfJsEmeAJsrA6UcmSvXJjc5sBkgvgs1GCrxyzm1nDiiF6eP7N3_XzeEx02NFSYR4j-fiyRffnnREUYOSCXl4-lDujfMbbCCEeyKmv6r8xkf0PK284dpVzV8LqW3Lqqizpw53RwY3NMlKyPPCQeDml8juDs0kgxdRkIxt5sBAX3ZEvQxdKVuLyzlaZ-z1EkbQcUc-k4qSLHyQMxi5_V9uWEZ7yMMP3-arn0JnOab1-cPGXnch_Crj7rJubhMuPeocPD0IbcAKDfv_UQowtSXBI-4JcBjkXPQMvVe-NmP7BXb81tNDOeO0vRUPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2937305fdb.mp4?token=iBrfp-hiEzK9jveMd5eNXF0HZd2SrqfJsEmeAJsrA6UcmSvXJjc5sBkgvgs1GCrxyzm1nDiiF6eP7N3_XzeEx02NFSYR4j-fiyRffnnREUYOSCXl4-lDujfMbbCCEeyKmv6r8xkf0PK284dpVzV8LqW3Lqqizpw53RwY3NMlKyPPCQeDml8juDs0kgxdRkIxt5sBAX3ZEvQxdKVuLyzlaZ-z1EkbQcUc-k4qSLHyQMxi5_V9uWEZ7yMMP3-arn0JnOab1-cPGXnch_Crj7rJubhMuPeocPD0IbcAKDfv_UQowtSXBI-4JcBjkXPQMvVe-NmP7BXb81tNDOeO0vRUPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: باید پُست‌ها را به افراد شایسته بدهیم نه به هم‌جناحی‌های خودمان
🔹
نباید این طور باشد که چون من وابسته به فلان دسته و گروه هستم، برتری دارم. کسی توانمندتر است که بی‌خطاتر باشد، حتی اگر در باور و ذهنیتش ما را قبول نداشته باشد.
🔹
اگر به همین قاعده…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/678755" target="_blank">📅 23:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678754">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11cd401fe.mp4?token=IDUQj4RxhHJMw1l5WuHjqmdltLD4qQQPi8_syubtVeIe0I7bGuEeve1ZkfX46ymfAiKNqeUwKq4QBREtYLKv5Q6mQv0Zz69xhky7QyHVpb0wxiS4zuznuRi3mUNer80s7PJjiFeZXNLPIoQ4SmHxkYR2bs4Z-52w054z50_Th2emeaVHk-lfkDh5uGoDDE8gcKTF3lghLNAXxrhKtKiEC5u4U2UBN404jUX4ZAoUe36ssaT8awlQxM5h1E-mhGN1oL20ZETjH2m-2_EKiIePoz4wLz2-B9nxTFnwwIVsE9mas6UM19Ngn2bc3h4gkhPTnjMOexDrF7Cx8itXePOQPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11cd401fe.mp4?token=IDUQj4RxhHJMw1l5WuHjqmdltLD4qQQPi8_syubtVeIe0I7bGuEeve1ZkfX46ymfAiKNqeUwKq4QBREtYLKv5Q6mQv0Zz69xhky7QyHVpb0wxiS4zuznuRi3mUNer80s7PJjiFeZXNLPIoQ4SmHxkYR2bs4Z-52w054z50_Th2emeaVHk-lfkDh5uGoDDE8gcKTF3lghLNAXxrhKtKiEC5u4U2UBN404jUX4ZAoUe36ssaT8awlQxM5h1E-mhGN1oL20ZETjH2m-2_EKiIePoz4wLz2-B9nxTFnwwIVsE9mas6UM19Ngn2bc3h4gkhPTnjMOexDrF7Cx8itXePOQPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد ۴ تن آهن آمریکایی به ماه
🔹
یک قطعه ۴ تنی از موشک اسپیس ایکس به طور غیر عمد به ماه برخورد کرد. به ادعای کارشناسان این اتفاق هیچ خطری برای زمین نداشته اما انتظار می‌رود یک دهانه آتشفشانی در ماه به جا بگذارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/678754" target="_blank">📅 22:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678753">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
در نخستین جلسه‌ای که درباره آسیب‌دیدگان حوادث دی برگزار شد، چه موضوعاتی با مقام معظم رهبری شهید مطرح شد؟  رئیس‌جمهور:
🔹
ایشان بسیار ناراحت بودند و ما هم به‌شدت ناراحت بودیم؛ چون اقداماتی که صورت گرفته بود واقعاً بسیار وحشیانه بود. از طرفی، به‌دلیل نبود آمادگی…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/678753" target="_blank">📅 22:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678752">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
رئیس‌جمهور: حوادث دی‌ پارسال قابل فراموشی نیست
🔹
کسانی که کشته‌شدگان را ۳۰-۴۰ هزار نفر اعلام می‌کنند، نامرد و وطن‌فروش هستند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/678752" target="_blank">📅 22:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678751">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmJXiCMlCXZdxoifRbevvoVdrlPlu9sVLAsCDDBHqSS5xW8e8AEzHZ5VsmimaYiO4KVEC8F9Td_7pMDeOIji6k5YABUZphmLN5Tsf-yWoXq2hc5l27ElFXUhyW-lP52p6JOQ4cWwhWb27iLuQ-DtuhW0JSbtpww55FEVd2LHwWBiuBkCyDVEwU1q8yvtawkSKYBOgPs2e_kKj86nuYGpvmFFL6qgsz2vHCiuqFFD825IY2ujNA2NJzlydEbiMySEzOZBW4be1nuZeSrj4IxdoOa4iKVD92TqVfnD_dQsaQq8kd2D0MXcVyZGimF-yVr_t_hAxHZhIP95MIiq5WlWdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وحدت مکرّراً و مؤکّداً تذکر داده شد
🔹
همانگونه که پیش از این مکرّراً و مؤکّداً تذکر داده شد، صیانت از وحدت و پرهیز از تفرقه و تنازع، اختلافات سیاسی و برجسته کردن تفاوتهای اجتماعی وظیفه‌ی همگانی است و البته نقش مسئولان و عناصر دلسوز و دلباخته‌ی انقلاب و امام و رهبر شهید در انسجام و یکپارچگی کشور، مهم‌تر و حسّاس‌تر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/678751" target="_blank">📅 22:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678750">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef0c240dea.mp4?token=Xh0qWX67z27AOvZx99ZGG5vGYe7YB_2keMcajbq2NW9LYt4rouYCO2YR2uJFo8cCTSBxCIs3nkjkkR7G_06ZpN7IUgUDm9Omyd3K5NLHMGPv9OJft6nGXQSmRYzpAxVGcNAGltfV4Vy_GFOl3F-QFv2Jtv0ow1TlhBmx3Hk2sqcRzAqoIGBG10WyHyv1hBCC7MuPvdMe7MhHhy6Fj73Vpi1zbZiwPey7MC9WPUPrIzrc_WLklAwiGgMc7QevZ9Qhb4k_3FEGdrAjGURGBnRkErNv1uPuk_gC-wwH84Iy7mlkt2GpbDdr7DerEheB2pTYM-FXuZ9ZcrfSfo6sqV6XGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef0c240dea.mp4?token=Xh0qWX67z27AOvZx99ZGG5vGYe7YB_2keMcajbq2NW9LYt4rouYCO2YR2uJFo8cCTSBxCIs3nkjkkR7G_06ZpN7IUgUDm9Omyd3K5NLHMGPv9OJft6nGXQSmRYzpAxVGcNAGltfV4Vy_GFOl3F-QFv2Jtv0ow1TlhBmx3Hk2sqcRzAqoIGBG10WyHyv1hBCC7MuPvdMe7MhHhy6Fj73Vpi1zbZiwPey7MC9WPUPrIzrc_WLklAwiGgMc7QevZ9Qhb4k_3FEGdrAjGURGBnRkErNv1uPuk_gC-wwH84Iy7mlkt2GpbDdr7DerEheB2pTYM-FXuZ9ZcrfSfo6sqV6XGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: شخصیت آیت‌الله سیدمجتبی خامنه‌ای رهبر معظم انقلاب استثنایی است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/678750" target="_blank">📅 22:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678749">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcfb35d1bf.mp4?token=vXJYL3Xw1Z1BjD7rwpH60TGF_A4tNZMX42azy4Vg62Hx5FddgrtP3dQkuG3T9dfqj7UHvMpvJadicLxFUp2Fedt--R2qSHW4VaHsdDneepWAgDQ99hxmdS9agSZqkdajIyG65eMhpYJaXPluVZbJhSUX5yFBhtgfGltVCVkgol2kwdaYamg0kph88cTLCuf-waiKssBz3MEopcHmU-6NEnNcq9epfJ4wzkfZcIUBY3Rr-qcjEhQS7LrX_GID_q6TnMxpYHdTKTxwJZmf9GWy9hnw-scGy7PoFvQi_PWhJWxeaIh-pG7wya65fStQDUv9Y_S9pXgEd2xc8PPn2dMBViwJ47J8PzerpSeelZ4OxZNxhUzX6i4hGEkaZ1NABvSmSpl4NXA3NUhBB8J6vNs4YloSRDbAWG8NvBCwwAKv_Ilsbdd7Py_Sdg9LmONpubZubtNZsyYBFHZU6G7OaeuNaoYhQAtbZGuEH5opoUCfE1-ko90xWI2vDnl0Y6-eCGRPXv40bG41DuClJpxKoi9yWKlFxOHY3LhoXdwrxsXpg28dQz0X5smD3sjeREnQCT2JnGpzqucMz4m5PEANFCq0IMDf7XZMBzbI3fxKBJ9ril3bgl1D79-sz46_I-1dfXG87Y2Aa6iY-YmLtBm6rqjIFMy6KXcahlNf0Ngk0-Y9xa4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcfb35d1bf.mp4?token=vXJYL3Xw1Z1BjD7rwpH60TGF_A4tNZMX42azy4Vg62Hx5FddgrtP3dQkuG3T9dfqj7UHvMpvJadicLxFUp2Fedt--R2qSHW4VaHsdDneepWAgDQ99hxmdS9agSZqkdajIyG65eMhpYJaXPluVZbJhSUX5yFBhtgfGltVCVkgol2kwdaYamg0kph88cTLCuf-waiKssBz3MEopcHmU-6NEnNcq9epfJ4wzkfZcIUBY3Rr-qcjEhQS7LrX_GID_q6TnMxpYHdTKTxwJZmf9GWy9hnw-scGy7PoFvQi_PWhJWxeaIh-pG7wya65fStQDUv9Y_S9pXgEd2xc8PPn2dMBViwJ47J8PzerpSeelZ4OxZNxhUzX6i4hGEkaZ1NABvSmSpl4NXA3NUhBB8J6vNs4YloSRDbAWG8NvBCwwAKv_Ilsbdd7Py_Sdg9LmONpubZubtNZsyYBFHZU6G7OaeuNaoYhQAtbZGuEH5opoUCfE1-ko90xWI2vDnl0Y6-eCGRPXv40bG41DuClJpxKoi9yWKlFxOHY3LhoXdwrxsXpg28dQz0X5smD3sjeREnQCT2JnGpzqucMz4m5PEANFCq0IMDf7XZMBzbI3fxKBJ9ril3bgl1D79-sz46_I-1dfXG87Y2Aa6iY-YmLtBm6rqjIFMy6KXcahlNf0Ngk0-Y9xa4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: حوادث دی‌ پارسال قابل فراموشی نیست
🔹
کسانی که کشته‌شدگان را ۳۰-۴۰ هزار نفر اعلام می‌کنند، نامرد و وطن‌فروش هستند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/678749" target="_blank">📅 22:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678748">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d663cf9cdf.mp4?token=Y-zLaSFHW1MggUstZKqGTJsrgMVe2GWbr69fkYDjfpjOFe7BtZZNUCCkFEeNKMGKpqyi7agRwc-GPSB4wIKoEivmaDCtNZUrwOP4Dzhc_Z1UdGIF8jPKROnr-f_5twQaS9OzCeqBUY602F5-JTVCZvjgIEC5F-DuOqwR28h1ObGNJviLCf8URaug8cVRF2xzUCmAZc1bO2jnJMFWIBQx4XNLH1guAMAzejv42c7zJmKUg4UC11cy14J1yIa_BeZUfkW_y-LZSom1SXdSBcuU9WIS2dCpKmneB-Yli52hjQ6bPFb2rMnH0IJiu9z1sbPnSDdkZvyaF4z3lVz4-baUNYpSNaRHQ9j2FLjcHV5vT-Yqt14Li0ueCP__mN8v9vudOQOxzA3eaIKvvN46EaB4cLmGa6i377u3SxkrNNIcnBWSUGSBWxyaGAYTBncJRDdG1duf51uFPnlTYh_lkMv71BqdD67OY9QCx36sM_aQCvbU11ENxiIXxlqAI1jWAyKIhiO5VLaAIiFD5IS3vZNiuzN2GzgqMg6O232KK46MBDeCmv-sfJ_Id1ApQMXHiYYFrNA5pab4JscIjmLnT9lKq08zXCBwaL-MM4oJ2jtBGIpI5APj8lAStIv8RCvOMUu-69OEQ4g2NXz4y-8_y1QpBwjTv1MD-pcazTL4CPH-A64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d663cf9cdf.mp4?token=Y-zLaSFHW1MggUstZKqGTJsrgMVe2GWbr69fkYDjfpjOFe7BtZZNUCCkFEeNKMGKpqyi7agRwc-GPSB4wIKoEivmaDCtNZUrwOP4Dzhc_Z1UdGIF8jPKROnr-f_5twQaS9OzCeqBUY602F5-JTVCZvjgIEC5F-DuOqwR28h1ObGNJviLCf8URaug8cVRF2xzUCmAZc1bO2jnJMFWIBQx4XNLH1guAMAzejv42c7zJmKUg4UC11cy14J1yIa_BeZUfkW_y-LZSom1SXdSBcuU9WIS2dCpKmneB-Yli52hjQ6bPFb2rMnH0IJiu9z1sbPnSDdkZvyaF4z3lVz4-baUNYpSNaRHQ9j2FLjcHV5vT-Yqt14Li0ueCP__mN8v9vudOQOxzA3eaIKvvN46EaB4cLmGa6i377u3SxkrNNIcnBWSUGSBWxyaGAYTBncJRDdG1duf51uFPnlTYh_lkMv71BqdD67OY9QCx36sM_aQCvbU11ENxiIXxlqAI1jWAyKIhiO5VLaAIiFD5IS3vZNiuzN2GzgqMg6O232KK46MBDeCmv-sfJ_Id1ApQMXHiYYFrNA5pab4JscIjmLnT9lKq08zXCBwaL-MM4oJ2jtBGIpI5APj8lAStIv8RCvOMUu-69OEQ4g2NXz4y-8_y1QpBwjTv1MD-pcazTL4CPH-A64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: در جنگ ۱۲ روزه پس از بمباران جلسه شورای‌عالی امنیت ملی درحالی‌که پایم زخم برداشته بود، خدمت رهبر شهید انقلاب رسیدیم و آقا در آن دیدار دستوراتی دادند و دعایی برای ما کردند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/678748" target="_blank">📅 22:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/744aacf05b.mp4?token=ss4ODVE2yqoo_eUiLzk4mut_Hcu28uYZ1esYB3v4d-IOCXKv7NpYZlm-6Mks2pWMjyBS8Pc8HZsfmvGEOd-ito39uSqtuFnGjJsQVbDU8HwV6DwMQDeE58rLD-x4IqrWGtwY6cNBuHjTcKS6xBE2_7A6czZQzX-AFVwAYq99RdFW5J91vygFz2zy3fDsm2AxHuyf5u_2OTYubkJEC8eiB7Vj55XDhvCS2kqOlZ7fz9T6STpURHNKh2kxEuFC8w7LE5MrC_zGwJTabigMSYrTT03PQWC9l2Bsbekq_CZcT0pVzRe-KHICG24QcF11y9CTh4HIFDHRqa-ANZNEBk9UXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/744aacf05b.mp4?token=ss4ODVE2yqoo_eUiLzk4mut_Hcu28uYZ1esYB3v4d-IOCXKv7NpYZlm-6Mks2pWMjyBS8Pc8HZsfmvGEOd-ito39uSqtuFnGjJsQVbDU8HwV6DwMQDeE58rLD-x4IqrWGtwY6cNBuHjTcKS6xBE2_7A6czZQzX-AFVwAYq99RdFW5J91vygFz2zy3fDsm2AxHuyf5u_2OTYubkJEC8eiB7Vj55XDhvCS2kqOlZ7fz9T6STpURHNKh2kxEuFC8w7LE5MrC_zGwJTabigMSYrTT03PQWC9l2Bsbekq_CZcT0pVzRe-KHICG24QcF11y9CTh4HIFDHRqa-ANZNEBk9UXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: ایران برای هر ایرانی خانه محسوب می‌شود و بنا بود سازوکاری چیده شود تا هر ایرانی آزادانه بتواند به کشور رفت و آمد کند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/678747" target="_blank">📅 22:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbef359f.mp4?token=Qp40I5qlx6MvNfzZYLi09aXuoku4u1uYL2F7NFrPvp7kBfQVOi7_02wJhYiWzQg0RbBowQQ4IKWHSmPS8ctak_bfjR-8VXLc1Tz2_tuo7qeq-ZTkDE26JM5RqxvVF5Mb5bQrEF16dvY8Q_LnsqFLj916XOUBumTnPyQxasg0wi4R7OekJm0L5Fbr6h1lg3AEJoXOFN7k6cGiUv9eo3f3t9vayGhX6pXmegokZ4z8xhJh0NHF1cT5J3qnD8pDNhY18PM97QoScEQR9DMQfZxSLKjgaCbLw0yv7n5suaapwnxRhjBLEIcHL_7yxEOkZj1RQKofvwE7mWqm6NVOVBfEwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbef359f.mp4?token=Qp40I5qlx6MvNfzZYLi09aXuoku4u1uYL2F7NFrPvp7kBfQVOi7_02wJhYiWzQg0RbBowQQ4IKWHSmPS8ctak_bfjR-8VXLc1Tz2_tuo7qeq-ZTkDE26JM5RqxvVF5Mb5bQrEF16dvY8Q_LnsqFLj916XOUBumTnPyQxasg0wi4R7OekJm0L5Fbr6h1lg3AEJoXOFN7k6cGiUv9eo3f3t9vayGhX6pXmegokZ4z8xhJh0NHF1cT5J3qnD8pDNhY18PM97QoScEQR9DMQfZxSLKjgaCbLw0yv7n5suaapwnxRhjBLEIcHL_7yxEOkZj1RQKofvwE7mWqm6NVOVBfEwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: همۀ ذهنیت من دربارۀ حقوق بشر و نهادهای بین‌المللی فروریخته است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/678746" target="_blank">📅 22:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
پزشکیان: وجود رهبری برای ما نقطه قوت است
🔹
پس از پیام رهبر انقلاب درباره مذاکرات، برخی از افرادی که دنبال تفرقه و اهداف جریانات سیاسی خودشان بودند، از این موضوع سواستفاده کردند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/678745" target="_blank">📅 22:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678744">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84823c6925.mp4?token=SMHIxBJtXtPqH_xxYz_kJACRfQsLZrFJfe5WzTPRtGA8jiupfieRV-b9hHXiX_hN3s6TqvXeQXqeD2mnRsCPHHWvA2Vdn975CinoTSWt7jyysh8EcCTrICbF14y5TCtDueuSH8cEOP4wmmUAElybWCQqykqMN3Eod0t6ScQZyUauUgmDIGYscFZxs0rc4cAE_Srv_pFYnIAzIr76QByDojIowAobvo4xbs64uCC6uleIAoHXLUi9RgmL5cmDY9vWLfTf97uQVu2MTtZy2MGuUTGvqdCPUNXSJB3RmHow9gnCz9WDifMmR5DXwwav4ute9l54_xH7zxNBAonlElUE_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84823c6925.mp4?token=SMHIxBJtXtPqH_xxYz_kJACRfQsLZrFJfe5WzTPRtGA8jiupfieRV-b9hHXiX_hN3s6TqvXeQXqeD2mnRsCPHHWvA2Vdn975CinoTSWt7jyysh8EcCTrICbF14y5TCtDueuSH8cEOP4wmmUAElybWCQqykqMN3Eod0t6ScQZyUauUgmDIGYscFZxs0rc4cAE_Srv_pFYnIAzIr76QByDojIowAobvo4xbs64uCC6uleIAoHXLUi9RgmL5cmDY9vWLfTf97uQVu2MTtZy2MGuUTGvqdCPUNXSJB3RmHow9gnCz9WDifMmR5DXwwav4ute9l54_xH7zxNBAonlElUE_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: رهبر شهید مثل کوه پشت ما ایستاده بود و از دولت حمایت می‌کرد
🔹
اگر کمک‌ها و پشتیبانی‌های ایشان نبود؛ ما نمی‌توانستیم تا اینجا پیش برویم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/678744" target="_blank">📅 22:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5abf48a216.mp4?token=jeMBPaLbRjRRuNfciez3tMgpJWALMVhOw6iCjuIn3U7UuEF-1-pue-8ncJtrp9PsmtEv2nsVynj6brbNLKDxMRvobXo3YHBORABRSBTr1NZdTpQyOYYwjhyIwUwqQ9CMxTjTvMwLJ_ouICRx5jbPk17npp27wwEOxw7PXX3rnkqxz2rTyesJ1ldTfNO9mmfC4h_ueVEVWz7HsovowTNShsN3VJMvgDMxwXJ5utDDYPRGpxO70min_nTLtzcJXeWLcvdo4MUapJalepIu8gLq7bYFWlXjMq4gNQSPmZM9F_Op7jmRJGLu1zr_iH4qCVPHN6GU4bajLdet-ST5bbJIDoOCys2fjqg4suhRKmUWfDtRt-WanaxNHlj97EpTkYAA2R-3dP3_f9wBOQOWjgjm6BHcwvoH47nKFoipvEUmGzP8DXR5cogokPAaziu9vScVybMWCWaz4SjS1eTATCRRDBOesKEANsayNRfVv_VLhrlmUnANTpG-3xRZZLvztcMD4rzIgo3_GxfJ3rGDrKJUIJc1LgYuWMM6HkLV_4qROox5ZZIqhg9Yn_SyXtF4SH5_h9YMhuhHOwZrpqdhGm2YOmDgiEbvG4A6eLrpAn-pm03RtSmzaTZqKzuQLImYUWw7eI6VvexRM6k-aBcLhaqGeQcYps4ZuZXYagZN0dngtiY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5abf48a216.mp4?token=jeMBPaLbRjRRuNfciez3tMgpJWALMVhOw6iCjuIn3U7UuEF-1-pue-8ncJtrp9PsmtEv2nsVynj6brbNLKDxMRvobXo3YHBORABRSBTr1NZdTpQyOYYwjhyIwUwqQ9CMxTjTvMwLJ_ouICRx5jbPk17npp27wwEOxw7PXX3rnkqxz2rTyesJ1ldTfNO9mmfC4h_ueVEVWz7HsovowTNShsN3VJMvgDMxwXJ5utDDYPRGpxO70min_nTLtzcJXeWLcvdo4MUapJalepIu8gLq7bYFWlXjMq4gNQSPmZM9F_Op7jmRJGLu1zr_iH4qCVPHN6GU4bajLdet-ST5bbJIDoOCys2fjqg4suhRKmUWfDtRt-WanaxNHlj97EpTkYAA2R-3dP3_f9wBOQOWjgjm6BHcwvoH47nKFoipvEUmGzP8DXR5cogokPAaziu9vScVybMWCWaz4SjS1eTATCRRDBOesKEANsayNRfVv_VLhrlmUnANTpG-3xRZZLvztcMD4rzIgo3_GxfJ3rGDrKJUIJc1LgYuWMM6HkLV_4qROox5ZZIqhg9Yn_SyXtF4SH5_h9YMhuhHOwZrpqdhGm2YOmDgiEbvG4A6eLrpAn-pm03RtSmzaTZqKzuQLImYUWw7eI6VvexRM6k-aBcLhaqGeQcYps4ZuZXYagZN0dngtiY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: هرچقدر فکر می‌کنم هیچ منطقی پیدا نمی‌کنم که چرا رهبر، فرماندهان و دانشمندان ما را شهید کردند
🔹
آنها با هر نمادی که برای توانمندی و ابتکار و خلاقیت ماست مشکل دارند؛ خیلی از فرماندهان و دانشمندان ما که شهید شدند خانه نداشتند.
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/678743" target="_blank">📅 22:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e7041a742.mp4?token=YkZRNOr1HI1in1FphPTvua31n3Yu-wL5aWSidKYXNuDxxmkRtGZd2Kx-OhDLzrtD-jYPiGf-JZDcD2LlDtiS1bjwXfRft-RBVZWJmrTuMg2-F5lS5PIgvNPOjbvwLuAOqSR3b0sF23iVPKfbtUF87bEUQxGYNXdqkgwMAFojW6hKPSYxExgpSpBbbwDPAnO6Ao_kO32sJfPgeJ_RIPtlCCcfL_F1Xc4WUYw1GfH6wBtKv5sx85ywcmQ3BxNtmoi3aDf10u2L5-aFhcRe0NvTPPIzqvClwMpQnJI7hBJyocxRtsiHQec-DyMtOkqc1OCamLVCD4Z5eV3ZlFkqCmQVBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e7041a742.mp4?token=YkZRNOr1HI1in1FphPTvua31n3Yu-wL5aWSidKYXNuDxxmkRtGZd2Kx-OhDLzrtD-jYPiGf-JZDcD2LlDtiS1bjwXfRft-RBVZWJmrTuMg2-F5lS5PIgvNPOjbvwLuAOqSR3b0sF23iVPKfbtUF87bEUQxGYNXdqkgwMAFojW6hKPSYxExgpSpBbbwDPAnO6Ao_kO32sJfPgeJ_RIPtlCCcfL_F1Xc4WUYw1GfH6wBtKv5sx85ywcmQ3BxNtmoi3aDf10u2L5-aFhcRe0NvTPPIzqvClwMpQnJI7hBJyocxRtsiHQec-DyMtOkqc1OCamLVCD4Z5eV3ZlFkqCmQVBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: می‌خواهند ما را زمین‌گیر کنند ولی وقتی با مردم باشیم هیچ قدرتی نمی‌تواند
🔹
تحریم‌ها شدیدتر شد، بانک‌های ما را هم تحریم کردند، جنگ راه انداختند و ما را محاصره کردند؛ به مردم قول می‌دهیم تا جان در بدن داریم و نفس می‌کشیم با تمام وجود خدمت کنیم.
🇮🇷
…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/678742" target="_blank">📅 22:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2f58dcf3.mp4?token=sowYZwMPOO3TweR-4M_urL_4A4cjsUS0re7A0q67f-c-8Vc82qnwL3oohNX2stKsxc7dEgy_-aJoeKkrwHDvsBwwBxKAkj2fR0aUoNbBDXHnc9WKMXoh70fRsGn5O34sxZijYHbNzO4qjlaAGF0Q0-ALyDIVCLgwX2S9o-cw4LZBMHLL1I_ENcqkGRftOGARBqMxZwDv9CGHAPV7WNHXRNaJQSX-sX324GpURzAkeMR3U8p8vgOzAUg1N5e0VoPRnFLPbdPG5U9tUhdMNzf9bTNhcKFYv3nUcv5ulo6KknLjzrZmDfkx71CvUTCw2Z5ivIBQYUOxImUne18IN0sxaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2f58dcf3.mp4?token=sowYZwMPOO3TweR-4M_urL_4A4cjsUS0re7A0q67f-c-8Vc82qnwL3oohNX2stKsxc7dEgy_-aJoeKkrwHDvsBwwBxKAkj2fR0aUoNbBDXHnc9WKMXoh70fRsGn5O34sxZijYHbNzO4qjlaAGF0Q0-ALyDIVCLgwX2S9o-cw4LZBMHLL1I_ENcqkGRftOGARBqMxZwDv9CGHAPV7WNHXRNaJQSX-sX324GpURzAkeMR3U8p8vgOzAUg1N5e0VoPRnFLPbdPG5U9tUhdMNzf9bTNhcKFYv3nUcv5ulo6KknLjzrZmDfkx71CvUTCw2Z5ivIBQYUOxImUne18IN0sxaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: نقشه داشتند جامعه ما را به‌هم بزنند که اتفاق نیفتاد و وضعیت با قدرت اداره شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/678741" target="_blank">📅 22:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37956f160b.mp4?token=aYDOyHfeNWQmfp9tZwXoA3-z5EkcZTEox4MMHLp9XMjeVCNdF4B-YD2GBWGYW6TvaBYBZ26jSxu77YDsXl1ZHc_aoy2DrhOGE56F6-dNZHx_7anYWE6Or-0vU6KbqDoz_kIqOd7OL0kV7G5jkguD_z417bQOOHh8PUJHqdURdMGH4OOhFUAJH5xgQFXISKNqKN6465QmCLJxuv_xEAoTghXNUIVkVyvJnNNpcoRXPmSZrid3RLAk2VAo7ih6RV8s7m4ilcETvqkPxWHaNtpk-IqTtqeZ_MSZXS7t3dbYnTNoM9WzkOSoj0lrkHwjV1fjl1R9DXfjUMYfs4VDv88NHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37956f160b.mp4?token=aYDOyHfeNWQmfp9tZwXoA3-z5EkcZTEox4MMHLp9XMjeVCNdF4B-YD2GBWGYW6TvaBYBZ26jSxu77YDsXl1ZHc_aoy2DrhOGE56F6-dNZHx_7anYWE6Or-0vU6KbqDoz_kIqOd7OL0kV7G5jkguD_z417bQOOHh8PUJHqdURdMGH4OOhFUAJH5xgQFXISKNqKN6465QmCLJxuv_xEAoTghXNUIVkVyvJnNNpcoRXPmSZrid3RLAk2VAo7ih6RV8s7m4ilcETvqkPxWHaNtpk-IqTtqeZ_MSZXS7t3dbYnTNoM9WzkOSoj0lrkHwjV1fjl1R9DXfjUMYfs4VDv88NHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: نقشه کشیده بودند ایران را ۴۸ ساعته مثل سوریه بگیرند
🔹
شهادت بزرگان ما در جنگ رمضان دردناک بود؛ با همه سختی‌ها و مشکلات امروز از ایران به عنوان یک کشور قدرتمند و با عزت بالا نام برده می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/678740" target="_blank">📅 22:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9009174817.mp4?token=LluvX6RvhntlSCAkutPOYFH4qUESRnrLNYwWoljv6mCcnDoU2L3sUfKaTVX_omzRoVfLF8zBACuNDIJnuB9y8U52yNmNy7xgoULG0Bc7Y6uqG-2s0YKcjBgem86V0Dhn064Fn6gKINs_aoZgXxtowSvuI88TGrxgfCirhl3XBsvDFKkkHCaMecGLMLTC3gj7L9HLONsrEPjo8mlZQ98EbbNKCqW2S6aqEZPv9KWY5AuH-FaVfZvC6XRgRwYbSBI1__W_1575GSY-uNt0PW2LEHr-qDl6qMZE-1tLHZ2Tqut5gZ-qhLHw2cW44e27kUZROYc1LJY6t4IzdG_2QxvMHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9009174817.mp4?token=LluvX6RvhntlSCAkutPOYFH4qUESRnrLNYwWoljv6mCcnDoU2L3sUfKaTVX_omzRoVfLF8zBACuNDIJnuB9y8U52yNmNy7xgoULG0Bc7Y6uqG-2s0YKcjBgem86V0Dhn064Fn6gKINs_aoZgXxtowSvuI88TGrxgfCirhl3XBsvDFKkkHCaMecGLMLTC3gj7L9HLONsrEPjo8mlZQ98EbbNKCqW2S6aqEZPv9KWY5AuH-FaVfZvC6XRgRwYbSBI1__W_1575GSY-uNt0PW2LEHr-qDl6qMZE-1tLHZ2Tqut5gZ-qhLHw2cW44e27kUZROYc1LJY6t4IzdG_2QxvMHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: کشور با وجود نقشه دشمنان، با قدرت اداره شد  رئیس‌جمهور با اشاره به جنگ ۱۲روزه، خشکسالی، ناترازی انرژی و فشارهای خارجی:
🔹
با وجود این مشکلات، دولت، مردم و نیروهای مسلح مانع از فروپاشی اجتماعی شدند و کشور همچنان قدرتمند و با عزت اداره شده است.
🇮🇷
…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/678739" target="_blank">📅 22:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
پزشکیان: دو سالی که گذشت؟ چیزی که عیان است چه حاجت به بیان است
🔹
از روز اول با شهادت اسماعیل هنیه شروع شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/678738" target="_blank">📅 22:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7901af0162.mp4?token=l51IpUbnQ0lT7mmmpyLHx4XNsisUQ6gXJPfILZ-K_mVossELkszsf8Ie8vILIpynQbse9gxCWPrFlQzO_i4KoF4cCixdJH2xZBlB0jGyv2142FSrrOQCYuZY2QU2ppGQdKYJmmoDpj_ftRqFleaXIvVbkTAXRsDer-3j2EjA0Adwh1CB1RLdml1CAwKGVrnQl3BfNSQIdD4v41yxgqLscwrhPVJgH3uMlPhcCmJSpY4LQ8DeKPQFy_YBOomZ1iB1Se8cFJKFWO5ww3i6c3sxVfmLteK52JnBfN76hGrcTzLncTQDCAmqjoxWRm35Pk_mt0lzbM_t9wRQbgqhahu3-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7901af0162.mp4?token=l51IpUbnQ0lT7mmmpyLHx4XNsisUQ6gXJPfILZ-K_mVossELkszsf8Ie8vILIpynQbse9gxCWPrFlQzO_i4KoF4cCixdJH2xZBlB0jGyv2142FSrrOQCYuZY2QU2ppGQdKYJmmoDpj_ftRqFleaXIvVbkTAXRsDer-3j2EjA0Adwh1CB1RLdml1CAwKGVrnQl3BfNSQIdD4v41yxgqLscwrhPVJgH3uMlPhcCmJSpY4LQ8DeKPQFy_YBOomZ1iB1Se8cFJKFWO5ww3i6c3sxVfmLteK52JnBfN76hGrcTzLncTQDCAmqjoxWRm35Pk_mt0lzbM_t9wRQbgqhahu3-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: دو سالی که گذشت؟ چیزی که عیان است چه حاجت به بیان است
🔹
از روز اول با شهادت اسماعیل هنیه شروع شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/678737" target="_blank">📅 22:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
یمن از حمله به نفتکش سعودی در خلیج عدن خبر داد
سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن:
🔹
صنعاء نفتکش سعودی « Daisy» را در خلیج عدن با موشک بالستیک مورد هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/678736" target="_blank">📅 21:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678735">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون وزیرخارجه: خبر دعوت پاکستان از وزیر خارجه و رئیس مجلس درست است اما برنامه‌ریزی نهایی نشده است.
🔹
دادستان یزد: عامل ارسال تصاویر پرتاب موشک به رسانه‌های معاند در یزد بازداشت شد.
🔹
انهدام باند قاچاق سوخت در بندرعباس؛ ۵ میلیون لیتر سوخت قاچاق کشف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/678735" target="_blank">📅 21:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678734">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
اعلام ضرب الاجل ۱ روزه برای مشمولان کالابرگ الکترونیکی/ این فرصت را از دست ندهید
مهلت استفاده از اعتبار کالابرگ تیرماه:
🔹
بر اساس اعلام وزارت تعاون، کار و رفاه اجتماعی، اعتبار مرحله تیرماه کالابرگ الکترونیکی تنها تا پایان روز چهارشنبه ۱۴ مرداد ۱۴۰۵ قابل استفاده خواهد بود و پس از پایان این مهلت، اعتبار مصرف‌نشده از دسترس خارج می‌شود.
🔹
به همین دلیل، خانوارهای مشمول باید پیش از پایان مهلت اعلام‌شده نسبت به خرید کالاهای مشمول طرح از فروشگاه‌های طرف قرارداد اقدام کنند. در غیر این صورت، امکان استفاده از اعتبار مرحله تیرماه پس از پایان زمان تعیین‌شده وجود نخواهد داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/678734" target="_blank">📅 21:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd24f9884.mp4?token=Mv6eVZ8D2IPUgd52sGZ-rHAdHLiM_B4hEo78LrUTmrrhEZ2XRxTd7oZefT36-jbwNlJ8EPZUPTu5za-nYFErxT3WJ-H6ukFfOu0NDvFkqFeGx5c41C3dYdf40VVqzeIu7zKcxVU6hoHuxYxCvUvaoDUG_M3npoKxWEuWUrusJvGyEfyQ7hq1wAYuqjiNKkvYNwsX2BpONjYAZrTdk4haXe4JtxlIxn8It2SekPZ1rEg_p6_xUCV_UXwv_-83TkKuAAnkoecuzaU-p1SA-DqAfaNbunyozXAdeF9Yvx_7L2kJ-aBl59MZ4j0hWBABWnIpU83lmiXbyvoOQF8WhRvFeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd24f9884.mp4?token=Mv6eVZ8D2IPUgd52sGZ-rHAdHLiM_B4hEo78LrUTmrrhEZ2XRxTd7oZefT36-jbwNlJ8EPZUPTu5za-nYFErxT3WJ-H6ukFfOu0NDvFkqFeGx5c41C3dYdf40VVqzeIu7zKcxVU6hoHuxYxCvUvaoDUG_M3npoKxWEuWUrusJvGyEfyQ7hq1wAYuqjiNKkvYNwsX2BpONjYAZrTdk4haXe4JtxlIxn8It2SekPZ1rEg_p6_xUCV_UXwv_-83TkKuAAnkoecuzaU-p1SA-DqAfaNbunyozXAdeF9Yvx_7L2kJ-aBl59MZ4j0hWBABWnIpU83lmiXbyvoOQF8WhRvFeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخلیه اجباری شهروندان به دليل اتش سوزی گسترده در ايالت واشنگتن
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/678731" target="_blank">📅 21:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678730">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f20da8e96d.mp4?token=ilKfUiTdZoCR0uZF3TKxBISBgWRiAzg-qyjDPAj9yjF7-lQBKFe4Uvw8WE5DRUJFPCq5aQPr49ezF6t9Cn3vOUtZcMsN4uoN9MYFm5gc8RxcHIWCrgz2jGSsD8Zew8NgTDVz-CoAR9HJqciM95qKj0MGz7SfDajZDfokxiU5wxoCHq9wOZrXNiThxy_07VmXScdW6Rb2MkNWnak8VKtXAGfxuK1jWFuftQjyuusZOMYxRDEtas16ZxUjZ5b83NtqApqjt3YNj8STex6XY09Rrped7IdXfVBmavPp4w41ia9djpG4bqt2G4v24KRFFa6vCnX2MVNZSXNtqWOzVYZT-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f20da8e96d.mp4?token=ilKfUiTdZoCR0uZF3TKxBISBgWRiAzg-qyjDPAj9yjF7-lQBKFe4Uvw8WE5DRUJFPCq5aQPr49ezF6t9Cn3vOUtZcMsN4uoN9MYFm5gc8RxcHIWCrgz2jGSsD8Zew8NgTDVz-CoAR9HJqciM95qKj0MGz7SfDajZDfokxiU5wxoCHq9wOZrXNiThxy_07VmXScdW6Rb2MkNWnak8VKtXAGfxuK1jWFuftQjyuusZOMYxRDEtas16ZxUjZ5b83NtqApqjt3YNj8STex6XY09Rrped7IdXfVBmavPp4w41ia9djpG4bqt2G4v24KRFFa6vCnX2MVNZSXNtqWOzVYZT-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین دو ماهواره هوشمند به فضا پرتاب کرد
🔹
چین دو ماهواره ابرطیفی مجهز به هوش مصنوعی را برای پایش زمین، کشاورزی و محیط‌زیست به فضا فرستاد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/678730" target="_blank">📅 21:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای سازمان تروریستی سنتکام: ما به اعمال محاصره علیه ایران ادامه می‌دهیم
🔹
تا به امروز، ما ۴۸ کشتی تجاری را منحرف، دو کشتی را از کار انداخته و دو کشتی دیگر را توقیف کرده‌ایم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/678729" target="_blank">📅 21:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9WiPJR4y2fUy6NUfFvcq3Bun9BrUYs3Wm4LoOAF7Ny2rt0fYdBQK_RdYbu4uJY9V97cWj6AZA-q2IGcGFEAFTVBx-BRGUyNY78jeFUL9ww2vkKle4AyQZPvB6DPnzUjzOCBKrlpaSpQPMPQiRHh6SSui3YNcutBk9MaXqKQ-yysx8cRd-j-npZpdDGLY4wmtkX6NEeOxnWeB0Se6akINUxjG5ObmbXUM_UCKU16p06EweQIhHCgOv2C2Vp8QRzHQ4HdG94gwh29KYP9KPx8Svu9_uVXyrS7hxqvypbNFrPJ8DC0GGQWFq-TvVKOdHUtcBZvknSc2OIN80bPzRNY4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهدیدهای تکراری ترامپ از لحاظ رسانه‌ای و سیاسی چه تاثیری دارد؟
🔹
این الگو نه یک بازی روانی بلکه به یک سردرگمی راهبردی تبدیل شده است. هر بار این چرخه تهدید و عقب‌نشینی تکرار می‌شود، ارزش تهدید آمریکا را در محافل سیاسی و رسانه‌ای کاهش می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/678728" target="_blank">📅 21:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678727">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
غریب‌آبادی: آمریکا پیام آمادگی برای بازگشت به تعهدات فرستاده است  معاون وزیر خارجه:
🔹
ایران در روزهای اخیر مذاکره‌ای با آمریکا نداشته، اما پیام‌هایی از واشنگتن دریافت کرده که در آن آمادگی برای بازگشت به تعهدات اعلام شده است؛ تصمیم ایران برای ورود به مرحله…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/678727" target="_blank">📅 21:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLr3AxCfB3VyC_ypv7l7sEk8qNkjMd6ZT0xKsII58GY8w_X_xWKsbBc4hD8LyDdFJuRgVvdLakXs584afg-IXXI9jKI8MFEXz_KC1VdLmGLsYJPQW5G4zOZEUusQrrzTHJB9Obm_EiUJmpxtbJs9hLJEpsDgY9pR-ZQ_Npis6oFNDZw9GhOHmksPh0k1MQyyfm1UM-MzgOFbJwnyLrbCOjJB2kyqmvc1XJ-pjjhwwYqjBB1ZxOdk-dFFuy8E53Hqo8vi551HHO38aBwol-pQzYa0KPXsr5CoxLxolzkUjblHNRvNCEBt6ay6V6bQly5OnrOq7d3m6sucNjzhYuwWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
با بیمه‌بازار، سلامتی شما بیمه است
رسیدگی به سلامت دندان‌ها مهمه و داشتن
بیمه تکمیلی مناسب
خیالتون رو راحت می‌کنه.
✅
در بیمه‌بازار
می‌تونید پلن‌های مختلف را یکجا ببینید و پوشش‌ها و سقف تعهدات را با هم مقایسه کنید تا انتخاب مناسب‌تری داشته باشید.
🦷
پوشش دندان‌پزشکی تا سقف ۴۰ میلیون تومان
👈🏻
دریافت مشاوره رایگان و استعلام قیمت
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/678726" target="_blank">📅 21:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678722">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
غریب‌آبادی: آمریکا پیام آمادگی برای بازگشت به تعهدات فرستاده است
معاون وزیر خارجه:
🔹
ایران در روزهای اخیر مذاکره‌ای با آمریکا نداشته، اما پیام‌هایی از واشنگتن دریافت کرده که در آن آمادگی برای بازگشت به تعهدات اعلام شده است؛ تصمیم ایران برای ورود به مرحله دوم مذاکرات همچنان در دست بررسی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/678722" target="_blank">📅 20:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678721">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcsP_aepIL1fAj16akmt67GWcPGOkaQc0YyT3C9Qh4wq__bP-Au1W-xnyNTMHvgupLhhnRsGT61FMyaQOBvGMJzpMgrWM5kGyBWgpcCy7l8XcOn2zXU81ptnH96Kh4JfE99D4ZVQF_kvgkcKoribUua0Pvxkkss180KgBXDdzEuFb8jQJlBVteQ5snosjimcR8Cwxlk1m8C4vA95hFDdadNH9eTwSqRton7raphIPb3JgRtTZL6NimTuKSNjOUmMmx_isqXnpLeCUmNdEjmzADNBNOZrSkIAbQAuI_nOofmKqHjuYIoQawvwFZS_rRCiZQVpj1kCfzQm-mVDfsAswA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پدیده‌ای کم‌نظیر در آسمان ایران؛ رژه ۶ سیاره
🔹
سحرگاه چهارشنبه ۲۱ مرداد، شش سیاره مشتری، عطارد، مریخ، اورانوس، زحل و نپتون در آرایشی دیدنی در آسمان ایران قرار می‌گیرند.
🔹
بهترین زمان رصد در تهران: ۴:۲۰ تا ۴:۵۰ صبح.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/678721" target="_blank">📅 20:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678718">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
غریب‌آبادی: تفاهم با عمان به معنای بازگشایی هرمز نیست  معاون وزیر خارجه:
🔹
تفاهم ایران و عمان درباره تنگه هرمز به‌معنای باز شدن فوری تنگه یا اجرای بند ۵ یادداشت تفاهم اسلام‌آباد نیست؛ بلکه مدل جدیدی برای مدیریت تنگه است که بدون دخالت کشورهای خارجی و متفاوت…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/678718" target="_blank">📅 20:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678717">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
غریب‌آبادی: تفاهم با عمان به معنای بازگشایی هرمز نیست
معاون وزیر خارجه:
🔹
تفاهم ایران و عمان درباره تنگه هرمز به‌معنای باز شدن فوری تنگه یا اجرای بند ۵ یادداشت تفاهم اسلام‌آباد نیست؛ بلکه مدل جدیدی برای مدیریت تنگه است که بدون دخالت کشورهای خارجی و متفاوت با ترتیبات ۶۰ سال گذشته دنبال می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/678717" target="_blank">📅 20:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678714">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
بازگشایی تنگه هرمز با چه شروطی؟
یک منبع نزدیک به تیم مذاکره‌کننده:
🔹
بازگشایی تنگه هرمز تنها با اجرای ترتیبات موردنظر ایران و پایبندی عملی آمریکا به تعهداتش امکان‌پذیر است.
🔹
به گفته این منبع، توافق احتمالی ایران و عمان به‌تنهایی به معنای بازگشایی تنگه نیست و باید تدابیر جدید ایران در هرمز و رفع موانع ایجادشده از سوی آمریکا نیز اجرایی شود./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/678714" target="_blank">📅 20:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678713">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQC3Xgo95W0yxX9hPMFKS9Ifq9W11naGA1mQEyCsu5VmtQ_ActEBzstX4jDtyUnNxj66vtCKsU-s7JfcY8fhJBFgLAbZjBvrHoCqejbp0ZHDCtOYqKQeJP1dS_L3_D2c5qbMbwWOSFdBLaq6MdVKOrBhWRNIq4q-nDogTP24cMdl9CZ95NSp1or6305UZiSjHow4RWS-Xo-GiizW3RmUcotDCnvaMBla0G2B969d_CgJCAbK-5anVElQK5BrcfCJyyvL3qozyBxwQcmNpAr9OJCFEP64rcrzkIyFdhSmAaal7x478wmUicXFewGudMaDTZdMB45wbqGxDkqbOfvOlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/678713" target="_blank">📅 20:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678710">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/678710" target="_blank">📅 19:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678709">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پشت پرده‌ مسدودی حساب شرکت ملی نفت / از ضمانت صندوق بازنشستگی تا صف ۳ بانک طلبکار
یک مقام آگاه با افشای جزئیات تازه از پرونده‌ی مسدودی حساب شرکت ملی نفت، توسط بانک صنعت و معدن تأکید کرد که این اقدام نه یک تصمیم سلیقه‌ای، بلکه نقطه‌ی پایانی بر ماه‌ها تعامل بی‌نتیجه و وعده‌های عملی‌نشده است.
🔹
منشأ بدهی چیست؟
خط اعتباری از محل منابع صندوق توسعه ملی که توسط بانک صنعت و معدن در اختیار صندوق بازنشستگی صنعت نفت قرار گرفته بود. شرکت ملی نفت نیز به عنوان ضامن پای این قرارداد را امضا کرده است.
🔹
تخلف صریح و وعده‌های پوچ
با وجود سررسید تعهدات، صندوق بازنشستگی نه تنها اقدامی برای تسویه نکرد، بلکه پس از دریافت مهلت‌های متعدد و حتی رفع بخشی از محدودیت‌ها، باز هم به تعهد خود عمل نکرد و بدهی به قوت خود باقی ماند.
🔹
صف طلبکاران طولانی‌تر است
برخلاف جوّسازی‌های رسانه‌ای، این پرونده فقط به بانک صنعت و معدن محدود نمی‌شود. بانک‌های تجارت، خاورمیانه و پاسارگاد نیز به عنوان طلبکار، اقدامات حقوقی خود را برای وصول مطالبات آغاز کرده‌اند و در حال پیگیری قراردادی هستند.
🔹
بدهی‌های پنهان صندوق بازنشستگی
این مقام آگاه با افشای ابعاد دیگر پرونده گفت: «مطالبات از صندوق بازنشستگی صنعت نفت فقط به شبکه بانکی ختم نمی‌شود؛ این صندوق به سازمان امور مالیاتی و برخی دستگاه‌های دیگر نیز بدهی‌های معوق دارد که همگی از مجاری قانونی در حال پیگیری است.»
این مقام آگاه در پایان هشدار داد: «بانک صنعت و معدن تمام مسیرهای تعامل را طی کرد و ناچار شد برای صیانت از حقوق سپرده‌گذاران و منابع عمومی، وارد فاز جدید اقدامات قانونی شود. اگر روایت‌های ناقص کنار گذاشته نشود، مراحل بعدی قراردادی با قاطعیت بیشتری اجرا خواهد شد.»/چندثانیه
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/678709" target="_blank">📅 19:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678707">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
منابع عربی از حملۀ موشکی به بحرین خبر می‌دهند
/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/678707" target="_blank">📅 19:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678706">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
حسن روحانی: برخی‌ها سال ۸۳ می‌خواستند برای سخنرانی امام زمان در تهران جایگاه درست کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/678706" target="_blank">📅 19:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678704">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHDBaIN2OBpbutOlbKWR_UWkOPnufJPUSHu65qYAnpZLphJ8F-upSg04oFTWGQ5qFZKuxBKi2MynnxV8hsNLefDApWKu6kkoQY60r3pfLMIJgdi4dfPfjzkK84wxkDxNX2SUzds4uDSqWBHhQ__83qdZOE19E22n5TlTS1V0ngYKdprsYshkJ8h5zNFaRDG1SeLZdvrzmLlw2u1RMRBx0ogT2IOn_uKGDfhNmwUgqeCwZ0d-mwEHZgDwe3nm1zSGZYMkDfq482OEM2REp0qSge2Cssp90NrcDXXugs5Ixg9YbS88LN923HXs6r1lZxZNqhNTy7hHOL3mW30Aev_hkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقویم برگزاری کنکور سراسری ۱۴۰۵-۱۴۰۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/678704" target="_blank">📅 19:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678703">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
بالگرد ترامپ در آسمان واشنگتن دچار حادثه ایمنی شد
🔹
رسانه‌های عبری گزارش دادند بالگرد دونالد ترامپ، رئیس دولت تروریستی آمریکا، روز گذشته هنگام حضور او در بالگرد، در آسمان واشنگتن درگیر یک حادثه ایمنی شد.
🔹
گفته شده در این حادثه هیچ‌کس آسیب ندید. سازمان هوانوردی آمریکا در حال بررسی ابعاد این رویداد است.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/678703" target="_blank">📅 19:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678701">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94095c883e.mp4?token=WYL8VtEL2V1EdI_g3z5-xCP3hDTrBTDtHMide8SmsTsZoSw8la1yJAgIkp5EHrdWMWvXb2YxRgcHdOmJfORiWat9hfpJpkfcsUpPtSb1yjXO2HXllflI_mvOzigYn79AT1Ac5JjluosCOd-nPgyw55wG56oekAGtK1EU232WExbzS1WOvQYrmQFQKDqOj1NKpkjia7o6F2yIR0n-E_ACLBn1P8w_gR4BzJREFyBQnd9cs0BqdIVfmYCfcDIePhchzBxs0w5XZUslqaJPmok6MMssOcgAEbpA5mdgEB79dCuniGhuhEBz0BJkUqp3FTA9EihtnP4FnRlOFENCrmYcpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94095c883e.mp4?token=WYL8VtEL2V1EdI_g3z5-xCP3hDTrBTDtHMide8SmsTsZoSw8la1yJAgIkp5EHrdWMWvXb2YxRgcHdOmJfORiWat9hfpJpkfcsUpPtSb1yjXO2HXllflI_mvOzigYn79AT1Ac5JjluosCOd-nPgyw55wG56oekAGtK1EU232WExbzS1WOvQYrmQFQKDqOj1NKpkjia7o6F2yIR0n-E_ACLBn1P8w_gR4BzJREFyBQnd9cs0BqdIVfmYCfcDIePhchzBxs0w5XZUslqaJPmok6MMssOcgAEbpA5mdgEB79dCuniGhuhEBz0BJkUqp3FTA9EihtnP4FnRlOFENCrmYcpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دریاسالار بازنشسته آمریکایی: کمبود موشک‌های پدافندی «خطرناک» است
جیمز استاوریدیس:
🔹
اگر ۸۰٪ ذخایر مصرف شده باشد، آمریکا نمی‌تواند از متحدانش در خلیج‌فارس، کشورهای عربی، اسرائیل و اوکراین دفاع کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/678701" target="_blank">📅 18:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678700">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMFyAnay0VN9KtXVi_bc7ZRiH02w-4AC2PSWNdjV3l5pbCYR_4sNdyDPWtzj3AHj-io3KSvbJGx1zuh_uh7ymWhcr_gu_NMOYtdKbkjjDAGnblwt4Zqacy_VZ_pWwG7Qxl_Qocb6mfz-QtJpXJ963CbjHszeTUKugQ-eVluaQfeDOArLfyCOnYYsmGzjCPcgDZneXaJu2czaWY3XCPksTTuAzNbdwx20GDy7wyMNIyCCUAu_nto4ptUdig4Bq3zYZNGm7jQtNw8_K4vRhOE5KtDJS_myjdWOdErRJqFN_229RzYhfV-iWA8IWTrs-yV0IlgXo12U1KBlpOGk05BDjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/678700" target="_blank">📅 18:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678697">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOXl_JlMdJ-EHsVv2tCt6-j2XLWHA0Zs5XVo2EuA6kI0RdH1c0C6M1R6Eb6kgdcbwxKDNzVHCyZNS_9t76mAa8-_f4xCvO-Bf8tGolwsHCWobmij-6SBSnM7pC5ZtKtUEPj9TGQuAOEkM__D-v_gjhOLFITz9OBKfjGJqW0z0KOcmC21g4MweUOxvGIFqYJ4wGZNqXlddY0hUEBF8VwLwkuBP7aKHPmuIPKUtUZ17Z_k7dyXNgTmd_ltFavHuEHeu-EIqTGi13sqqwkH2TfQ14uL6hJL_tIuB4AL5g15xNCJDdqRLDDARBIz-vMViKtuTgH8e1oZ7cHsq0mIaJYP-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیشرفته‌ترین روش‌ درمان چاقی به کلینیک ایرانیان رسید!
مجهزترین کلینیک زیبایی و لاغری ایران و خاورمیانه با ۲۶سال تجربه
✨
کاهش وزن با زیکورپا
، در کلینیک ایرانیان. زیکورپا، تولید
داروسازی دکتر عبیدی
، منجر به کاهش وزن ماهانه ۸ تا ۱۰ کیلوگرم می‌شود.
🔻
بدون رژیم و ورزش
✅
قبل از شروع درمان، توسط پزشک/متخصص تغذیه آنالیز شده و دوز مناسب برای شما تعیین می‌شود.
👈
همین حالا
«مشاوره پزشکی رایگان»
دریافت کنید
کلینیک ایرانیان(زعفرانیه|سعادت‌آباد|دولت|تهرانپارس)</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/678697" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678696">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYdZA4-8FUxYzAwva_xtrG6onqw0z9L_Iysu9q0hYg6jwHxVUPtO_mJsNin0sFXX7C04S52OWnOT89d_yLEIoYH4Qo_1whyI3VSbUX0UPNKFpJY-fVwlSHUtxMMQZ2J-9qU1RcbXcxYwhopijjQqcBlr43fR9K7mYjcxjGCM_Va8znRBnuNM8AEO_BY0NpA7r3ePQiB_tIvWMNk7f1_PChdaRcljgJQ8KJ_y8PgjAfzid3uxP67YuXhGxFuct8VlhPGfnMVJcpFfOgCBF6-xDABGzZZUBs6UQsYIZ3Mlqxjt5t-5evRhlla5o4ltgGcHgLKljiiDi6f8ugWxjtPbaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکی که قرن‌ها پیش، رازهای بدن و درمان را می‌جست؛ ابن‌سینا
🔹
ابن‌سینا فقط یک پزشک نبود؛ او دانشمندی بود که پزشکی را با فلسفه، تجربه و مشاهده پیوند زد. آثارش قرن‌ها در دانشگاه‌های جهان تدریس می‌شود و اندیشه‌هایش مسیر پزشکی و شناخت انسان را تغییر داد. آثار…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/678696" target="_blank">📅 18:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678694">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqac-utY_7OgQENiXD_CmSgYs3AFcGWVvT8iBtWlhEbZS7_J8UtIscK5XneZEFh0DL_4m_EzKU3mlw019i7u1CURE_jNFWfOPcGHY6saepBnDeRmIZo23bgbdZK3_1wYYErp2RNZh8CZNT-sw5-uwF2GAQlIa2e-4iLVKNLAWi0I2mPfCMLhbNVyZl6nMSnjlbaQNlNjyIVpfrKZuY4KHPZpN5_znSp-ZAY1GIvDCnc2NmGWjGFhPkg3eVJyMF5eoRnj8Uo-CdfnR1mDm2vESexe7SNIEhu77o7YmPYEiBk7tiGham05OIXenAB_nbXFTxEneflfBoHjg3E3F27Z_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سود ۶۰۰ درصدی صنعت سیمان
🔹
با وجود کاهش تعداد پروانه‌های ساختمانی، صنعت سیمان همچنان سود خودش را دارد.
🔹
بررسی‌ها نشان می‌دهد سود صنعت سیمان در  ۵ سال اخیر بالای ۶۰۰ درصد بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/678694" target="_blank">📅 18:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678693">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
قیمت جدید بنزین سوپر در بورس انرژی ۸۴,۶۰۰ تومان تعیین شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/678693" target="_blank">📅 18:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678692">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEa0q6FAQMfAcVVu9HglV_ydGI4Kex6hJVK1RekjBEarxfi7bvPzHf060B_Mpy_K8whSGxcdvhvLUFiBHNOVuGzZ37ksc_N7bEGqK_ZMmRKDwRRKzncnwwKZqc1q_jU_DxSp_5-yEELNkUxIobOX1frSAZ1esbLIdgHSj4bMKRoVtL4t1H_3CRbjKEM-y9T0YZ9uVxcynMP_PXAXbeGJLz6lhqZZqpo871BSJF_KUWCEW5-WyD0rJl-2divE53G6XrB99dxq1HqZspXtaY_4NRq9YeBVhWliXQkqfIG41nebnSmsMmB679c9vyrgGLs4DufcIRfSjPSQ19vU0THGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهمترین مانع جوانان برای ورود به بازار کار چیست؟
🔸
در این نظرسنجی بیش از ۲۷ هزار نفر شرکت کردند که سهم روبیکا ۵۶٪، بله ۲۵٪ و تلگرام حدود ۱۹٪ بوده است.
🔸
حدود ۳۶٪ شرکت‌کنندگان کمبود فرصت شغلی و نزدیک به ۲۱٪ هم عدم تناسب آموزش با بازار را به عنوان بزرگترین مانع جوانان برای ورود به بازار کار معرفی کرده‌اند.
🔸
به نظر می‌رسد حل چالش اشتغال جوانان، در گرو افزایش فرصت‌های شغلی و نزدیک‌تر شدن مسیر آموزش به نیازهای واقعی بازار کار است.
@amarfact</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/678692" target="_blank">📅 18:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678691">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
لغو تحریم ۳ شرکت هواپیمایی مرتبط با ایران از سوی وزارت خزانه داری دولت تروریستی آمریکا  سی‌جی‌تی‌ان:
🔹
طبق جزئیاتی که روز چهارشنبه در وبگاه وزارت خزانه‌داری دولت تروریستی آمریکا منتشر شده است، تحریم‌های اعمال شده بر ۲ فروند هواپیما و ۳ شرکت هواپیمایی مرتبط…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/678691" target="_blank">📅 18:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678690">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/041ad29cb9.mp4?token=ElWN2RPPQjXYGtJ2d1j6pNKxembh-4POQWiffJ61vXz0ZqKH4OXQrk2BRomdsmM0BUxetsir1ChbOHAIJSn8TAXtXb7VTBz7WEu5Kyb6HI-1noikfudtTGp2ZPvfTKxRi8i--B3vSHhOGritOexY1YTNbfkfu0Al_POyx0KYdxLFEpYsUrPgJlTDKvV2oEUvz3IeNOZSI-ePAVQpRv2DmmXkLtbXqHXJUGTtm8oP0PJfjJ9hf8EXcQZScG4PUqrgDXCN5Wug-vgSAaXABIhOq_XYcC9aU4zhwp6AC_BtYGL0Z2TZ2TDv3of5LoASvqMKTZLsGrtBADCDLO0VDSWcLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/041ad29cb9.mp4?token=ElWN2RPPQjXYGtJ2d1j6pNKxembh-4POQWiffJ61vXz0ZqKH4OXQrk2BRomdsmM0BUxetsir1ChbOHAIJSn8TAXtXb7VTBz7WEu5Kyb6HI-1noikfudtTGp2ZPvfTKxRi8i--B3vSHhOGritOexY1YTNbfkfu0Al_POyx0KYdxLFEpYsUrPgJlTDKvV2oEUvz3IeNOZSI-ePAVQpRv2DmmXkLtbXqHXJUGTtm8oP0PJfjJ9hf8EXcQZScG4PUqrgDXCN5Wug-vgSAaXABIhOq_XYcC9aU4zhwp6AC_BtYGL0Z2TZ2TDv3of5LoASvqMKTZLsGrtBADCDLO0VDSWcLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید انقلاب: حرف من را از "خودِ من" بشنوید/ گزیده بیانات رهبر شهید انقلاب ۱۳۹۴/۰۴/۲۰
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/678690" target="_blank">📅 17:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678689">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ادعای رویترز: وزارت خزانه‌داری آمریکا اعلام کرد برخی تحریم‌های مرتبط با ایران را لغو می‌کند./ تسنیم
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/678689" target="_blank">📅 17:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678688">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای رویترز: وزارت خزانه‌داری آمریکا اعلام کرد برخی تحریم‌های مرتبط با ایران را لغو می‌کند
./ تسنیم
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/678688" target="_blank">📅 17:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678687">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromامـیـن‌الـلّـه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/883ac1089e.mp4?token=qz_ssD3Kvd3-4V7fwQ-ImyPpz6hoi-yCprmlT9MVYQb_Xv1Svy7MuAvzSRe1325TwsA9xen17n4UNduRt72HOPlsjEorOcWUjASypJszivOo9NKDpSOv8Src80KoExF8RT3a1O25J26MY2XdEQExM_qt-SWiFHBHT3_Xiri7UdffyvnDPQn_K0ez6uPt_9K0UgTfx4mFA7NQPbdwQ5FZZ_hf0c316wPaBu_9bgc3N8r8ybRPsgOYh2UmO5PhWGzk-0bQZ0H6VlW8hSudaxthSkGXBOw_wUNqoefGBxePAIZajJw2K1za5pzf4xc2GRTPWt2XkXR4SYFPgZ7sXZP2HKJAj6zdjgtZA__m7DoAtRtmel2TJnYR4AyKlzr9JBdhUkyKRg8vsC8kDU5pN2ZpznVJktBNRQpj9n3X_vAXFBWQUBUu3xj3OHw2_eawWvudzCD3q-ic0Fhf-Q35ryt3ljL--dOzbYjEmUCoQfkZpJki22ulT1SHclH_WVvq3GkGHzu6qceF8H1WvMSTElj1_KywsE3HNJ4ln6t9ZK6pGRtfdsdC_6pqk5Uw6_6UhekKWM4rgnGAMgz_PJt5ZKHcfspL-q_zcmC0PH77brDPBBUTr58SS3ym0d78bjgJmAC3kQyjT7lfJyxB5M2LgNRGDFPAelkktu83uPJ-8oWmCHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/883ac1089e.mp4?token=qz_ssD3Kvd3-4V7fwQ-ImyPpz6hoi-yCprmlT9MVYQb_Xv1Svy7MuAvzSRe1325TwsA9xen17n4UNduRt72HOPlsjEorOcWUjASypJszivOo9NKDpSOv8Src80KoExF8RT3a1O25J26MY2XdEQExM_qt-SWiFHBHT3_Xiri7UdffyvnDPQn_K0ez6uPt_9K0UgTfx4mFA7NQPbdwQ5FZZ_hf0c316wPaBu_9bgc3N8r8ybRPsgOYh2UmO5PhWGzk-0bQZ0H6VlW8hSudaxthSkGXBOw_wUNqoefGBxePAIZajJw2K1za5pzf4xc2GRTPWt2XkXR4SYFPgZ7sXZP2HKJAj6zdjgtZA__m7DoAtRtmel2TJnYR4AyKlzr9JBdhUkyKRg8vsC8kDU5pN2ZpznVJktBNRQpj9n3X_vAXFBWQUBUu3xj3OHw2_eawWvudzCD3q-ic0Fhf-Q35ryt3ljL--dOzbYjEmUCoQfkZpJki22ulT1SHclH_WVvq3GkGHzu6qceF8H1WvMSTElj1_KywsE3HNJ4ln6t9ZK6pGRtfdsdC_6pqk5Uw6_6UhekKWM4rgnGAMgz_PJt5ZKHcfspL-q_zcmC0PH77brDPBBUTr58SS3ym0d78bjgJmAC3kQyjT7lfJyxB5M2LgNRGDFPAelkktu83uPJ-8oWmCHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">؛
تمام عالم رو هم بگردید، باز هیچ‌جای دنیا عفت و حیا و ادب زن شیعه‌ی ایرانی رو پیدا نمی‌کنید..
زر و زیور دنیا ارزانی کسانی که هنری جز نمایش تن و خریدن توجه ندارند..</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/678687" target="_blank">📅 17:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678686">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ادعای آسوشیتدپرس: پیش‌نویس توافق میان ایران و عمان نهایی شد
خبرگزاری آسوشیتدپرس، به نقل از دو مقام منطقه‌ای:
🔹
مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/678686" target="_blank">📅 17:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678685">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jo0N1r8uXVQCl5QzhdMp9oqo_-1kBTp26G8PzmLyV3OW_nOTiBNq4u73v_a3gGN6l5LELeGQjkSBOVZcpNnA_3Ml4IfaDLeuUQDyY3Il6BGmToYZJ-qHjjqHMAfe2mT9yXSn7fPwEmMn5o4GX1V6RPJ0BEJE1u9gyoOZjltLXxo-t19g3bgi5pYeH8Bpsc68C3RiYwD837o7pCla0zQoavjAwNilqYakcZ31bXsXWCt7iNOrqk03SquRETf4LD_usUQWTMqFLxuvjoqN_TJEgKhAZ0snnZSkeK10_If3PDtOSNUZg0kcfSVGhUNwdDHc1EXR8w5wsvI7SD1fobJcgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط در بلوف و عقب‌نشینی | چرا تهران دیگر تهدیدهای واشنگتن را جدی نمی‌گیرد؟
🔹
هفته گذشته راهروهای قدرت در واشنگتن بار دیگر صحنه گمانه‌زنی‌های داغ درباره احتمال وقوع یک برخورد نظامی گسترده میان ایالات متحده و جمهوری اسلامی ایران بود. اما حالا همه‌چیز بوی یک توافق تاره را می‌دهد. کاخ سفید دچار یک سرگیجه سیاسی است که صدای همه را درآورده است.
ترجمه گزارش آمریکن کانسرتیو را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3235490</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/678685" target="_blank">📅 17:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678684">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7471eda44.mp4?token=DVIUWVlJ4ZnMm8oJ2O_AxA3h-pVx0_w4DOHAHaVI3J2Wb9jrFhvszfqiU1q93HiKKidszoIvGeFoYcb5Fuv2xmSA-1qkoaKF9t_wloIGj0i0usB2wE3TUkL2FvsmjpCNbgmc2iHRI7Wa7NT3W1Xob74ISXkrwOdUAkiOfreYO_D16XhBCajKbXVvm1efdzN2gBOhsH6eliP_tbwoBJs_iUDwVpxUKvcsNtE3Aoi7MjAO5IQGQwN_CoM0aE-bnecOt14xnhEKpiYuEu_veWbd6d5DGabRiuu7uCAHUrPBDuHQtTg9SofHovSkNPy06RTHFPWLZCXqv4fCHnKUiWChIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7471eda44.mp4?token=DVIUWVlJ4ZnMm8oJ2O_AxA3h-pVx0_w4DOHAHaVI3J2Wb9jrFhvszfqiU1q93HiKKidszoIvGeFoYcb5Fuv2xmSA-1qkoaKF9t_wloIGj0i0usB2wE3TUkL2FvsmjpCNbgmc2iHRI7Wa7NT3W1Xob74ISXkrwOdUAkiOfreYO_D16XhBCajKbXVvm1efdzN2gBOhsH6eliP_tbwoBJs_iUDwVpxUKvcsNtE3Aoi7MjAO5IQGQwN_CoM0aE-bnecOt14xnhEKpiYuEu_veWbd6d5DGabRiuu7uCAHUrPBDuHQtTg9SofHovSkNPy06RTHFPWLZCXqv4fCHnKUiWChIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعریف خنده‌دار کاخ سفید از جنگ
سناتور آمریکایی:
🔹
ما جنگ راه می‌اندازیم و اسمش را می‌گذاریم عملیات غیرجنگی!
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/678684" target="_blank">📅 17:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678683">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b19afaf3d.mp4?token=hgGzQsxuMnV-Co1RjEcp0lEfc1WCyYfdijc5MloCcV4DpRb5sk35Rkk_w57xbvmfCr523R536Jck9XGYdcyYUIPP5q4xn0VrSzHlkrlnWwBO38TJYP4BOAlgV5zEGvpmYtx72EqpykRMwQomKYlYRyVUA4M0MyM4Ww4fRbact6P5L13u4dePg_9pI7YVbRNUXPtM3QSeoSign5CWH2eMm_XQDCv8LBVDWeNL0DCoxFwZ3BU6dhGPB4H5aY6WBmMd84h-8xRgItf_7yQ-JXDkLuqxx7IEOWeYfzaIlD44sgia8rQhqotg90e8oclgU9FQGFsLfYOlGRKXAKYT7AUEIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b19afaf3d.mp4?token=hgGzQsxuMnV-Co1RjEcp0lEfc1WCyYfdijc5MloCcV4DpRb5sk35Rkk_w57xbvmfCr523R536Jck9XGYdcyYUIPP5q4xn0VrSzHlkrlnWwBO38TJYP4BOAlgV5zEGvpmYtx72EqpykRMwQomKYlYRyVUA4M0MyM4Ww4fRbact6P5L13u4dePg_9pI7YVbRNUXPtM3QSeoSign5CWH2eMm_XQDCv8LBVDWeNL0DCoxFwZ3BU6dhGPB4H5aY6WBmMd84h-8xRgItf_7yQ-JXDkLuqxx7IEOWeYfzaIlD44sgia8rQhqotg90e8oclgU9FQGFsLfYOlGRKXAKYT7AUEIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاله جای مادره؛ آخه سینا مادر نداره
🔹
سینا ۲ ساله شهید شده، مادرش هم شهید شده؛ پدرش هم شهید شده؛ مادر نداره که در فراقش بی قراری کنه؛ خاله جای مادرش بیتاب فراق سیناست.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/678683" target="_blank">📅 17:03 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
