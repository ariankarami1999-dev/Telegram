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
<img src="https://cdn4.telesco.pe/file/Dkmr1q0qIDesOoir0qVyT3LhdqKNetpIr3uPxft_lPMqsw83MPrKlMuA_7FYtWoIsWCm69LuNjIjeMdWa2qQMQ_jDg1iWkJxkM74ZyhT_TOXdXWflbDsExTNrdBnmC_WfVhSi32zzTNK4Xu0zfC_gVwn8RoaGNxuTwuQ8IhgxSLYWry4ceO2v8hNZ7uuKszCecpQyOlvQEnIR2rWiNg5lzbpjHobunc4dAivlZD4x9TlmaB-aO1Kn2GgKcKjxqS0EixK6qcD3r5kZEXx80w_aWI1sG74IvUXzqKZbrzxI9R_AnGGP1r0ctYfZg9x1sYk0m1KoF6h2jSsVX0nyHFCYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 181K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 23:32:33</div>
<hr>

<div class="tg-post" id="msg-76128">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سخنگوی ارتش اسرائیل:
ارتش اسرائیل دقایقی پیش دو تروریست ارشد سازمان حماس را در شمال نوار غزه هدف قرار داد، جزئیات بیشتر بعداً اعلام خواهد شد.
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/funhiphop/76128" target="_blank">📅 23:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76127">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسرائیل هیوم:
ترامپ پیش‌نویس یادداشت تفاهم با ایران را به نتانیاهو و رهبران منطقه تحویل داد تا نظرات خود را اعلام کنند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/funhiphop/76127" target="_blank">📅 22:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76126">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaXfbO9qSuqlguXu-qYE0JioD96hkM5cB7ysZt9tK7EpaG6A5F_CblgFFgtu7suVFVqXktprS-zjbRaiQq0OG3rxA2FPyo195WaKWPCigvqwTFdhXtUV13vqolo9osBkeoLRjjD71cCmP2pr-7wYszLBoyaOls8F7U1_eYPGDX0RcqBhu4UqinH76o36f9tq1K94PGbbDwKt2ahcD1woMljo7RfuJzHIJy9QwQrmUAh2wtewmBYUqIv1Q-SoXxVxA_ssJqSSH0WouyRTDPbVWvUj8VVkMJOiNwalOn-SqbcSZjvVEYFVZGvnnWLrAsX1ViSTRj4ccZSQpx60RhDlwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکنه رئیس باند فروش کانفیگ ایران لاپورتا بوده</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/funhiphop/76126" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76125">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اسرائیل همچنان داره لبنانو میکوبه
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/funhiphop/76125" target="_blank">📅 21:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76124">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نکنه رئیس باند فروش کانفیگ ایران لاپورتا بوده</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/funhiphop/76124" target="_blank">📅 21:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76123">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ:
عربستان و سایر کشورهای عربی به ما بدهکارند، اگر آنها به پیمان ابراهیم (عادی سازی روابط با اسرائیل) نپیوندند، من فکر نمی‌کنم اصلا مذاکره و توافق صلحی با ایران انجام بدهم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/funhiphop/76123" target="_blank">📅 21:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76122">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">با تایید رومانو آنتونی گوردون به بارسلونا پیوست تا درصد اوب بازیکناش از میانگین ۹۰ درصد به ۹۵ درصد برسه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/funhiphop/76122" target="_blank">📅 20:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76121">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامفض:
این کاملا رژیم چنج است. ما یک رژیم را از بین بردیم، سپس رژیم دیگری را هم از بین بردیم، و ما الان درحال مذاکره با رژیم سوم هستیم و خواهیم دید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/funhiphop/76121" target="_blank">📅 20:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76120">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ:
به خدا من می‌خواستم بزنم ولی فقط به خاطر روی گل عاصم منیر که خیلی دوستش دارم و درخواستی که کرد به ایران یه فرصت دیگه دادم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/funhiphop/76120" target="_blank">📅 20:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76119">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6012f650.mp4?token=YmDOCYoGmWN-1zq62Vk6bbNjjAVpKaV2U_VMN6IHslHdO4kloHltw8zAsdxi7x5P9MSnfFvskuFX0ygXQrPkSsyXSrIadg9gxdZcYhq87e5DAy7P6RN2FyFF_l4SYN8HQcTszKk-yy-5LoukN448jiqB486u4DTLrz7ZdUglZqrqmpGyqN2Dzus2ZXXik1SJbyh3UkAeMtcK00mDb5b7eqLlfV8q9jyHTXRkdZSOi-sJbXE1KbC9KLUdWETXEhMFvKVE7Aj-afYHKI2mti-7PQMZKbGwROFczQY5lF3-aEBUMzcyt7hYS_YVklj9i-frPue71c-PB3L7ZwWVHN5PUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6012f650.mp4?token=YmDOCYoGmWN-1zq62Vk6bbNjjAVpKaV2U_VMN6IHslHdO4kloHltw8zAsdxi7x5P9MSnfFvskuFX0ygXQrPkSsyXSrIadg9gxdZcYhq87e5DAy7P6RN2FyFF_l4SYN8HQcTszKk-yy-5LoukN448jiqB486u4DTLrz7ZdUglZqrqmpGyqN2Dzus2ZXXik1SJbyh3UkAeMtcK00mDb5b7eqLlfV8q9jyHTXRkdZSOi-sJbXE1KbC9KLUdWETXEhMFvKVE7Aj-afYHKI2mti-7PQMZKbGwROFczQY5lF3-aEBUMzcyt7hYS_YVklj9i-frPue71c-PB3L7ZwWVHN5PUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
ما اکنون درباره هیچ گونه کاهش تحریم‌ها یا پرداخت پولی صحبت نمی‌کنیم.
ما کنترل پولی را که آنها ادعا می‌کنند مال خودشان است، در دست داریم. ما کنترل آن پول را حفظ خواهیم کرد.
وقتی آنها به درستی رفتار کنند و کار درست را انجام دهند، اجازه خواهیم داد پولشان را داشته باشند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/funhiphop/76119" target="_blank">📅 20:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76118">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ درباره ایران:
آنها شروع به دادن چیزهایی که باید به ما بدهند کرده‌اند. اگر این کار را بکنند، عالی است.
اگر ایکار را نکنند، هگست (وزیر جنگ) ادامه مذاکرات با آنها را برعهده خواهد گرفت و کار را تمام خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/funhiphop/76118" target="_blank">📅 20:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76117">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6a042bbf.mp4?token=Md_TmMSK6kfEB5wa4Ag-hbL9lNyxBSqymTOLnJK5wuZH5UEo1Tjt-djTJEtdo2pX8BbOhAr9xQH1IGDp7hkIwnfltT3UqwvqvQttYkb6vdBwj6YmFmCPn1PBfDBGGPrnIAVDl3wZsVZYEhOQpkcYwIouDASlRqbFONH0RtBvC7DSPlEqfytJk0_1GIkO3zXzpb9ZiWo1qMSfHVbPh1XKXxqky8lvFex1ZKjke8E_OjRWuFxWrP9mFDWbX3giPahQ4POhpSRql4SNPgcd91Mx9KfREalr_REcwPapEdAYbPiXc-mJJMsOmTopSH15fkk15XOPs4iCxKMdrMYVf7hdpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6a042bbf.mp4?token=Md_TmMSK6kfEB5wa4Ag-hbL9lNyxBSqymTOLnJK5wuZH5UEo1Tjt-djTJEtdo2pX8BbOhAr9xQH1IGDp7hkIwnfltT3UqwvqvQttYkb6vdBwj6YmFmCPn1PBfDBGGPrnIAVDl3wZsVZYEhOQpkcYwIouDASlRqbFONH0RtBvC7DSPlEqfytJk0_1GIkO3zXzpb9ZiWo1qMSfHVbPh1XKXxqky8lvFex1ZKjke8E_OjRWuFxWrP9mFDWbX3giPahQ4POhpSRql4SNPgcd91Mx9KfREalr_REcwPapEdAYbPiXc-mJJMsOmTopSH15fkk15XOPs4iCxKMdrMYVf7hdpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا از این موضوع راضی خواهید بود که روسیه یا چین اورانیوم غنی‌شده ایران را بگیرند؟
ترامپ:
نه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/funhiphop/76117" target="_blank">📅 20:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76116">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ درمورد خبر صدا سیما مبنی بر اینکه تو پیش‌نویس توافق گفته شده تنگه توسط ایران و عمان کنترل خواهد شد:
تنگه‌ برای همه باز خواهد بود و
تحت کنترل هیچ‌کس نخواهند بود صرف نظر اینکه ایران چه می‌گوید؛ ما مراقب آن‌ها خواهیم بود.
عمان هم باید مثل همه رفتار کند و اینکار را نکند، وگرنه مجبوریم آن‌ها را منفجر کنیم.
🙏
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/funhiphop/76116" target="_blank">📅 20:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76115">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFBkXEotl0YH6hptQP21GK8AcqsTS_TcTi6t3-GADX4Vsl_LTAU36Erf0bq1QWhrhKRFlAuPR6PZ9MmU0TDrSgx1w0FJ2O0aoSQn9TINl3-OhQc3iRJIQDhsrdaR-_mHui0PFIusyd5GMDHJm2EVfa3kTX80W9AHqZhyPnzzIG40_r_kiI58xbnaGAEQZv1mihxH8WE8lTFyUPvRqDSSq4vPGXMXsRxIV6OyD6NnTAsH7UPwHBnDZjEGmlPm6qUeUxQebBWAkcSZOffwgyNCu-FNbYPluBt5YXeCBycyLCSngspV6y26hthA_lozmxGf9wFGKyJ-hxRpYqKQV2t8GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/funhiphop/76115" target="_blank">📅 20:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76114">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4635a829.mp4?token=ZfsYBnH84RFzusGgKFN1bkV71zuCep9Wjk7ul6y2oAAcPBVpwENg8o5t3zX8c2dxnC27UzdyJ3ESrbuTFzqGfJ1bZJWvXZx476UNkzyobV0B0u8UWe5PRCm0v_Uk3BTjbBRXYCjWVVf9sBwhU0K4w44fGqvfqAeJGpfr-LoWMrcXZ-vSsqgZ16GHcj8OnYUTOkN-Y3r8XY_7l9Y9B6-hvO9qkV3USsqUu5iWyMmGsYOaEhJJ046IND9RPgRNuBfAlE2pY2BMrREAe_C0rjqw0c3hc6653lIb4Nr3KUtbQLaEiC7-Q81UZkjjqu7GspmV8h5lVudo2Ywa7uLbWGQZ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4635a829.mp4?token=ZfsYBnH84RFzusGgKFN1bkV71zuCep9Wjk7ul6y2oAAcPBVpwENg8o5t3zX8c2dxnC27UzdyJ3ESrbuTFzqGfJ1bZJWvXZx476UNkzyobV0B0u8UWe5PRCm0v_Uk3BTjbBRXYCjWVVf9sBwhU0K4w44fGqvfqAeJGpfr-LoWMrcXZ-vSsqgZ16GHcj8OnYUTOkN-Y3r8XY_7l9Y9B6-hvO9qkV3USsqUu5iWyMmGsYOaEhJJ046IND9RPgRNuBfAlE2pY2BMrREAe_C0rjqw0c3hc6653lIb4Nr3KUtbQLaEiC7-Q81UZkjjqu7GspmV8h5lVudo2Ywa7uLbWGQZ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا جی جی مصاحبه کرده گفته پشمام ریخته که جوونا هنوز ابی و داریوش گوش میکنن چون ریتم آهنگاشون خیلی چرته   @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/funhiphop/76114" target="_blank">📅 20:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76113">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرگزاری مهر:
آتش‌سوزی در یک ساختمان اداری در فرودگاه بین‌المللی امام خمینی در نزدیکی تهران، پایتخت ایران، رخ داده است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/funhiphop/76113" target="_blank">📅 20:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76112">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مارکو روبیو:
دیپلماسی گزینه اول ماست اما گزینه‌های دیگری هم درمورد ایران وجود دارد.
ما معتقدیم که پیشرفتی در جهت رسیدن به توافق با ایران حاصل شده و در روزهای آینده خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/funhiphop/76112" target="_blank">📅 19:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76111">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afe37ba190.mp4?token=NG4QNn0nYlAcW_jU8Aqsi7nqOGAmOWXrk4hMWof3lj7NPjIo4UJddD0YsBXy6xHCdurC0v2dZes5nExMoqQuhfDkKlkslUmGlFYCfRXL50vavUT7QwsCDoXv7nuM5YDw8okw68U74cA5spBDEivCySUQU_7rv0V3UcagcPky-zRy_IoJ5Lm7pSD8_f5-pHjt9wFK03d7B3QrOdcFpBjyUMyJxHC-z_ojqdOn8vmPZExjAt4zn0sdq8sGpxpFV-NMat8kayJ4fFZBe8NtCbz9940-D9wro8g-K3An_i7MbXZYSVcfsJ0mEQqLFbgpfP5pdFycEg12xUsaEaI29soD0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afe37ba190.mp4?token=NG4QNn0nYlAcW_jU8Aqsi7nqOGAmOWXrk4hMWof3lj7NPjIo4UJddD0YsBXy6xHCdurC0v2dZes5nExMoqQuhfDkKlkslUmGlFYCfRXL50vavUT7QwsCDoXv7nuM5YDw8okw68U74cA5spBDEivCySUQU_7rv0V3UcagcPky-zRy_IoJ5Lm7pSD8_f5-pHjt9wFK03d7B3QrOdcFpBjyUMyJxHC-z_ojqdOn8vmPZExjAt4zn0sdq8sGpxpFV-NMat8kayJ4fFZBe8NtCbz9940-D9wro8g-K3An_i7MbXZYSVcfsJ0mEQqLFbgpfP5pdFycEg12xUsaEaI29soD0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نه داداش ببین طرف خیلی باهوشه حواسش جمعه به خدا داره شطرنج ۱۶ بعدی بازی می‌کنه:
با وجود درگیری با
ونزوئلا
، کشوری که دیگر نیروی دریایی ندارد، دیگر نیروی هوایی ندارد، دیگر افراد زیادی که کشور را به سمت مکان‌های بسیار بد هدایت می‌کردند را ندارد و رهبری آن از بین رفته است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/funhiphop/76111" target="_blank">📅 19:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76110">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4df9e7ea0.mp4?token=rwkurkAe5uDC4mdEHgZdVNN7XNTAxEnmb7oW5wIR64t2VlEns3cluYwHx9--LHnFLP3KQQtbtzkIJUyP3DyIOyH2bfOaLeL-gKTNbekrxblQRVJyxr8wSW545aLNnRoOEztsfX-N2Mk2kFJzFS23qz6nOX9KxTbwjc-LRYcAuz1zEzpZt0JisgEx_z7BVh0Rymt0Ycawy0iRtrOzaK87jA1TU6jCeWqjI82t1NYC0_is8yHxPk0UZrVnZQzLxrlIRTMWI4KZHxkKepgT5qiwrh2RYnNQPFvGXFvGn6s_6MemC5K3IUujv_6FdnD7e1b8k9Ua34y1ldtsuR0bvEkBHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4df9e7ea0.mp4?token=rwkurkAe5uDC4mdEHgZdVNN7XNTAxEnmb7oW5wIR64t2VlEns3cluYwHx9--LHnFLP3KQQtbtzkIJUyP3DyIOyH2bfOaLeL-gKTNbekrxblQRVJyxr8wSW545aLNnRoOEztsfX-N2Mk2kFJzFS23qz6nOX9KxTbwjc-LRYcAuz1zEzpZt0JisgEx_z7BVh0Rymt0Ycawy0iRtrOzaK87jA1TU6jCeWqjI82t1NYC0_is8yHxPk0UZrVnZQzLxrlIRTMWI4KZHxkKepgT5qiwrh2RYnNQPFvGXFvGn6s_6MemC5K3IUujv_6FdnD7e1b8k9Ua34y1ldtsuR0bvEkBHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
ایران بسیار مصمم است. آنها بسیار مایل به انجام یک توافق هستند.
تا کنون به آن نرسیده‌اند. ما از این موضوع راضی نیستیم، اما یا راضی خواهیم شد، یا اینکه باید کار را تمام کنیم.
آنها در حال مذاکره با توان کم هستند. شاید مجبور شویم برگردیم و کار را تمام کنیم؛ شاید هم نه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/funhiphop/76110" target="_blank">📅 19:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76108">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⚠️
پیشنهاد استثنایی به مناسبت باز شدن اینترنت ، زیر قیمت کل ایران
🛍
🚀
100 گیگ پر سرعت +ساب
1,000,000
🚀
80 گیگ پرسرعت + ساب
800,000
🚀
50 گیگ پر سرعت + ساب
550,000
بدون محدودیت تایم و محدودیت کاربر
⏰
🔴
بدون قطعی و افت سرعت
🟡
بدون ضریب
🥇
پشتیبانی واقعی ۲۴ ساعته
💸
ضمانت عودت وجه
❗️
این قیمت تکرار نمیشه، از
دستش نده
ثبت سفارش
👇
:
🎙
@Mohammad_vpn2</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/funhiphop/76108" target="_blank">📅 19:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76107">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یکی از منابع فان هیپ هاپ تو نظام امریکا
‏آمریکا به هواپیماهای مستقر در اسرائیل دستور داد ظرف ۷۲ ساعت به پایگاه‌های خود در اروپا بازگردند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/funhiphop/76107" target="_blank">📅 19:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ کاملا از حیطه منطق و عقل خارج شد و به PBS گفت:
ایران در ازای خارج کردم اورانیوم غنی شده خود هم رفع تحریمی دریافت نخواهد کرد و به طور مستقیم اظهار داشت: «آنها اورانیوم غنی شده‌ی خود را کنار خواهند گذاشت اما نه، نه، اصلاً. هیچ تسهیلات تحریمی‌ای درکار نخواهد بود، نه.»
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/funhiphop/76106" target="_blank">📅 19:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بمببببب فارس:
ا
حتمال اعلام یک‌طرفه نهایی‌شدن توافق توسط ترامپ برای فشار به ایران
منابع آگاه می‌گویند دونالد ترامپ، رئیس‌جمهور آمریکا، احتمال دارد طی ساعات آینده به صورت یک‌طرفه اعلام کند که توافق ایران و آمریکا نهایی شده است.
این اقدام از سوی ترامپ با هدف اعمال فشار و القای توافق به افکار عمومی، پیش از رفع کامل اختلافات، ارزیابی می‌شود.
بااین حال، یک عضو تیم مذاکره‌کننده ایرانی در گفت‌وگو با فارس تأکید کرده که هنوز برخی موارد حل نشده باقی مانده و تا زمانی که همه موضوعات مدنظر ایران حل نشود، هیچ توافقی در کار نخواهد بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/funhiphop/76105" target="_blank">📅 19:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76104">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">علیرضا جی جی مصاحبه کرده گفته پشمام ریخته که جوونا هنوز ابی و داریوش گوش میکنن چون ریتم آهنگاشون خیلی چرته
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/funhiphop/76104" target="_blank">📅 19:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76103">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بارسا تو ۲۴ ساعت گوردونو خرید، بعد میگن پول نداره</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/76103" target="_blank">📅 18:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76102">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI4azrH5FbLMWNGWitY4LEuj-wCwubM2Mn-jJN70iAa9g1hiMxF_qQfJcZ5TuiEeHHGg9Fe0XvnEsy3qoOYkaOVfQQMnPFcGflYsy_cPHcDHcVdaRAvJXKGdRKzbZIWs_lCBH2TjaawiJr9oS8denxehF8IuLUHrnoxVTBYABAc1wkh6LCNh8fV2kYt0SJ38VZMkObrzBlMhWT59Y1tRMa32dyjsn3M4eYE6T68kqS2FTipcEvSeGluUDcCkUH_-DNv2I3QcJUG7MocAZwewFidj59GvQ7P316QrY2Ibe17Tijaao7qYAo7xMn4VyLspkNJnGWLY1WsbP9vlU9-pNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید درمورد گزارش صدا و سیما از پیش نویس توافق ایران و آمریکا گفت کاملا ساختگیه و در ادامه هم تاکید کرد: «هیچ‌کس نباید آنچه را که رسانه‌های دولتی ایران منتشر می‌کنند باور کند.»
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/76102" target="_blank">📅 18:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76101">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MichkVGbAdoJZDMeBvvLQ0z-5gmy1VEyyKB4tK05O3Tc6chUuA8kp73R3G_CuVwRygWXoXuwLuhpL1GP13ysPVc8oUmW9x3W4mMPJe1xDFHMTOz4WdWxI-t5GbgGsEuSvA_CyLc7XkxrLQRu5xbY113O6MaICetnHRw5n7fzFUojbt8-B_OAfEoBzPKOWhWskygafMKxyLQ41a75Lljc4IoU0mmQbIVfNiRw3xyexWX5ustNw161uahQPneJDezYO9G0wZEJqhNSeDY4CpeAB26Nd89E6bDZcT62l2oXC1ntXZlN9iFbGjOMR4OX995i5c8d0baqClxOWexIum5gkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها ترامپ فکر می‌کنه خیلی بامزه‌ست، لطفا بهش بخندید کیر نشه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76101" target="_blank">📅 18:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76100">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLQSc198xbLnBCzZDakOsJfeov0wGbXm__buTMlaGUELPv7gxw2vKnXjD_CdEtnqyYPo9asYbo12_HzQgEazWv7nkhEXu46NRCiKxT9B-Qo3eZVgbafkl8kYD4EmIRTrmGeWXZWqVlWvqs7wAhbm0mzBdsIEuYUcQKWoLAhtxD4ty_fIgddQ0O4l9WePh-oszAjTidjdfsom_P0ekfpk4Bn0s6k7yqp2TvcS7JO1fDbHQmZzNGv16vF5WThEZpwjyb_2u4yAk9fmgfNw8i8GWjOjgVZ6aUxOzoRwEU2eX8olgTl2OaBGxhhwOaD86UmYumjiZpmLvbej-8FFQjtJLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g6
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/funhiphop/76100" target="_blank">📅 18:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76098">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ظاهرا به تیم ملی جمهوری اسلامی اعلام شده که اجازه اقامت تو آمریکا رو نداره و بعد هر بازی باید بره مکزیک  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76098" target="_blank">📅 17:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76097">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اکبرزاده: دیگه فکر نکنم دشمن جرات داشته باشه حمله کنه.
پ.ن: یادش بخیر دو سال پیش جلیلی و ثابتی هم میگفتن اگه اورانیوم ۶۰درصدو بدیم به آمریکا بهمون حمله میکنه، چون الان اورانیوما بازدارندس جرات نمیکنن حمله کنن، اونا هم عمه های من بودن تو ۹ ماه دو بار به ایران حمله کردن و تو عمق ایران همه رو ترور کردن کسی کیرشونم نتونست بخوره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76097" target="_blank">📅 17:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76095">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کانال 12 اسرائیل:
انتظار می‌رود هواپیماهای نظامی آمریکایی در صورت امضای توافق با ایران، ظرف ۷۲ ساعت  اسرائیل را ترک کنند و به پایگاه‌های اروپایی منتقل شوند.
هواپیماهای سوخت‌رسان نیروی هوایی آمریکا در صورت از سرگیری درگیری با ایران به فرودگاه بن گوریون بازخواهند گشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76095" target="_blank">📅 17:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76094">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ظاهرا به تیم ملی جمهوری اسلامی اعلام شده که اجازه اقامت تو آمریکا رو نداره و بعد هر بازی باید بره مکزیک
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76094" target="_blank">📅 17:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76089">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZByOJCruOb72Wod-Uj75gJCdY9QQSQ_bldajg5Mh3tdN9JaRVMfRQyzzyu7heKyf5uwX3D2-KUmZ58YtoKuk0CB66iNQLIQQabV7bxhKaiPPnwEQmQ6-qFXbhhU3CDOTTgaRoPPfv9td_2tasvQUlpo-o58XRGKWVw5_P7XFQ45MDDzsxmjUe6XJXN0PMJ29MZgvhCWI766NyHhHFMdKb8sBI-n6Z9ZGLy869pX9N86N9cioNBP2-CTxqcjqsXRpVaH2tUwk-4FYmkRGgmAW0x1RQeDHS1_Q_juZuJjgWsfgw5-HzBVyXX_Hj9US0LNjCISYwfHGxD3R_rbZD1a4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در جواب آنفالوی رسایی رضا پهلوی رو فالو کرد.   @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76089" target="_blank">📅 16:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76085">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❮⬥مــنطقـه آزاد⬥
🍒
💋
❯ ویسکال ۲۴ ساعت بزرگ ترین گروه تلگرام
😈
https://t.me/+Q4LrN9EBJM0wZmJk</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76085" target="_blank">📅 16:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76084">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❮⬥مــنطقـه آزاد⬥
🍒
💋
❯
ویسکال ۲۴ ساعت بزرگ ترین گروه تلگرام
😈
https://t.me/+Q4LrN9EBJM0wZmJk</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76084" target="_blank">📅 16:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76082">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پزشکیان در جواب آنفالوی رسایی رضا پهلوی رو فالو کرد.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76082" target="_blank">📅 16:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76081">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromReza</strong></div>
<div class="tg-text">خداروشکر
همین کم مونده بود اینو به عنوان چهره مخالف جمهوری اسلامی بکنن تو پاچمون</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76081" target="_blank">📅 16:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76080">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انگار خایمالیا سردار جواب داده و میخوان برش گردونن تیم ملی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76080" target="_blank">📅 16:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76079">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ایران تو صدا و سیما هنوز با توافق مخالفه، تو تنگه هرمز چپو راست داره کشتی رد میشه</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76079" target="_blank">📅 16:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76078">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cznG5jBTNL4SzywcbITq9k1UEr_AL1oZYD_PBrUVlc71r4-NNacL9S4Uo-WMSviRWt8N3CMkYSX3chYPIUvFBYd5jFhcKMQaVwY5lskqRjHZ7T4Numm-TObf1oywaoKSCa-41yKCqSrF2Tnl8txaTJN5IzxMiPGe4j-6oOiVzzWRinlyleVCfImuiAa1l56Esoq0I-JKjlXl95VivARmI9W8XseazNPFC52fS-maJPIBRINTci4BffrOTH_dElWW4hxoaRl0Gq6jQPVtVZkY5WkVF0ZcHXpml7uLiW9BMaZkcrXiGDRBnQA9P1WDEy5VYkQ_q_DIEJxcoM61F7YR6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت برنت به پیش‌نویس تفاهم غیررسمی تهران و واشنگتن ریکشن نشون داده.
@funhiphop</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76078" target="_blank">📅 16:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76077">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رسایی: قلبم به درد آمد وقتی دیدم پزشکیان اینترنت بین الملل را غیرقانونی وصل کرده است
پ.ن: کیرم تو قلبت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76077" target="_blank">📅 15:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76076">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ارتش دفاعی اسرائیل حملات خودشو افزایش داده و کاری که چند سال پیش با کرانه باختری و نوار غزه کرد و داره سر لبنان و حزب الله میاره.
نمیخوام کل حملات و پوشش بدم ولی داره تو لبنان پیشروی میکنه و برای چند تا از شهر های لبنان هم دستور تخلیه فوری برای تخریب ارسال کرده.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76076" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76075">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromꜰᴀʀᴀᴢ</strong></div>
<div class="tg-text">اینا اینترنت رو وصل کردن تا حواس ما رو از عروسی دختر شمخانی پرت کنن</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76075" target="_blank">📅 15:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76074">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آخرشم پزشکیان میوفته تو استخر نیم متری و غرق میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76074" target="_blank">📅 15:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76072">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjP1wydOuujVMh-k4VRlmKLDkReRjoJ3k1jFDJRe_X2RQ__EpIviYtQ5kaPN12RtHBEswm2YlXvwhQdG7KapQKpffLFBqNn2XWVUlTzlLugipTyudugQ8YHDwLZ9fy4Ny7QCaoNYooNj29bZxI2NyltZfSBjESjE74T9GfpZuplIjb6_EWMWh7d7QYA2JuwOr92x-y5osyN3d2RhFxfA3qyZvuU2FX02uKi7Zo0eXAFJ3gJSjGQFIk8z9ZWbnhhWGvGlk_U2fkSE1CU1pqH9d2zJ59Dk7ZFwOYgTM4p7pUAv3dvBxRinT4_esZ3bhwlFKoBrgnMpiP_Q69z__ldkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJmj0TZx6Y9Az4wQQyOosOCo54psJirkmxVSvG_dXaMgL_gRLiVZMR4BEkfAWzY2HRUJJlNde-LnECWvu5UE1lIMd9Ar-wlg5ESiE--LbPNPEgCeFl9Vdw1NBQMKWYkuHauEX21WCtsF5kw6BJG39_yM8R2P1dl_1YDDTal99DvuL1mTJdJNmE23gQYE97indk_s5Mx7x7VYMGUgq2UVrSSLXh-1gMat_hAx934fIif0wv4rOT5rZg7K1iPRk2lZUQaUwZ08UnuU8PeDM6aEuiA7RP6vSa_LM0wQ7jfxgfMw8tXoW6JpwkaqbqqyyXRMPfVUtP-eY_OYI5tmDYh_Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همون همیشگی  @funhiphop | reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76072" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76071">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انقد پیام ندید، گیگی ۵ هزار تومن وی پی ان نخریدم پیام بخونم باز، فقط ویدیو های بالای ۲۰۰ مگ
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76071" target="_blank">📅 14:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76070">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رافینیا ده برزیلو داد نیمار</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76070" target="_blank">📅 14:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76069">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فوری: طبق گزارش Jerusalem Post، ارتش اسرائیل و سنتکام در حالت آماده باش قرار دارند. به این خاطر که احتمال شکست مذاکرات هسته ای/آتش بس با ایران و اقدام نظامی توسط ترامپ است.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76069" target="_blank">📅 13:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76068">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی ایران: بعد از اینکه دشمن توی جنگ نظامی موفق نشده، حالا بیشتر رفته سمت جنگ رسانه‌ای و روانی. به گفته این وزارتخانه:
الان تمرکز دشمن روی ایناست.
* فشار اقتصادی روی مردم
* ایجاد اختلاف قومی و مذهبی
* تحریک اعتراضات و ناآرامی
* ترور و خرابکاری
* قاچاق سلاح و استفاده از استارلینک
* حملات سایبری
* فعالیت رسانه‌ای علیه کشور
همچنین هشدار داده هر کسی در جاسوسی، همکاری با رسانه‌های دشمن، یا اقدامات تجزیه‌طلبانه نقش داشته باشه، با برخورد قانونی شدید روبه‌رو میشه.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76068" target="_blank">📅 13:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76067">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ebe6aef1.mp4?token=farsbsZFzHSqJsLkukLg4TNICEN6cdK07tBpTeC8ylNHYo1JUHXOfvHpbiEjl3To92ukm3UteWzu5ftvEWG5Fwz3ICMyqqC3VjL1alpuKUI2BnXd03cmP_j0dkbTBLIFSDO81T1Cwc137C7kMobfPBvisrmLEfHw8BaiERMBPqnq2UKL2rNqbdOiYLRXON3N6EV4EsYEko9X47XzMkB_DT85a_xHGEtFyBq2-M1VEK-rrpqDzynohiohfVe7yTjPZryaDGXLkB-IcsD4k6ANvQ8x2lntvCoFpMoEaNnRZSCmKLn7g2guKJP9z1Ek4ICD3h1KTMyWJTbuXxPw4jGZmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ebe6aef1.mp4?token=farsbsZFzHSqJsLkukLg4TNICEN6cdK07tBpTeC8ylNHYo1JUHXOfvHpbiEjl3To92ukm3UteWzu5ftvEWG5Fwz3ICMyqqC3VjL1alpuKUI2BnXd03cmP_j0dkbTBLIFSDO81T1Cwc137C7kMobfPBvisrmLEfHw8BaiERMBPqnq2UKL2rNqbdOiYLRXON3N6EV4EsYEko9X47XzMkB_DT85a_xHGEtFyBq2-M1VEK-rrpqDzynohiohfVe7yTjPZryaDGXLkB-IcsD4k6ANvQ8x2lntvCoFpMoEaNnRZSCmKLn7g2guKJP9z1Ek4ICD3h1KTMyWJTbuXxPw4jGZmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش های تایید نشده: فرمانده جدید شاخه نظامی حماس، محمد عودا، در محله ریمل توسط ارتش دفاعی اسرائیل ترور شد.  @funhiphop | reza</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76067" target="_blank">📅 13:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76066">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آقای پزشکیان نمیشه اینترنت رپرا رو قطع کنی؟ تا عمر دارم مدیونت میشم بخدا
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76066" target="_blank">📅 13:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76064">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">میخوام
🇮🇱
🎒
همزمان بزارم کنار اسمم تو توییتر  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76064" target="_blank">📅 13:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76063">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">میخوام
🇮🇱
🎒
همزمان بزارم کنار اسمم تو توییتر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76063" target="_blank">📅 13:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76062">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XV1hFrXkkgTfI6z6uT94FdyiJkZkVyf0UToS85Nnx41EDTVbDh2AuK7syn3MR4rUti62Gjdx19xEN3IO95H4hv-Nres5863ukcadZnXsyXmb7XjQD8KstP3bGu1SbexvCF9tJWRWY38ZaUeEUmpxv5ORhPMmkDd3xR5ZhlEycIwJ0FUMqcEyAsr4sLdPN69gdlfBPrPuqmgtVxXZkLBL7MhlJF-so_Oi1XKPumN4710gjrTeTXbRHHrhclgsWrJjQz15y4ZppsN6GYsnqCcywur63vBNORAxS_mS06CyX4u3x4svHkvnpG67-QEj56euA5MO9_VIm1EDK39BPD6zWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادمه ی سریتون کصشر می‌گفتید که رهبر سالم نیست
چیشد؟!
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76062" target="_blank">📅 13:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76061">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کاپ رنک یک وسط بازی هم تعلق میگیره به قیاسی
کار بلد بود ناموسا ی جاهایی داشت باورم میشد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76061" target="_blank">📅 12:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76060">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خداحافظ وحید جان</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76060" target="_blank">📅 12:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76059">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">زنگ بزنید منوتو به امید بگید کانفیگ فروشم
براتون اشک بریزه یکم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76059" target="_blank">📅 12:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76058">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گذر پوست به دباغ خونه میوفته
Make Vpn Sellers Great Again
#MVSGA
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76058" target="_blank">📅 12:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76056">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdi</strong></div>
<div class="tg-text">یه ترا کانفیگ میخوام بودجم هم حداکثر سی هزار تومنه
زیاد نیاید پی وی حوصله ندارم باهاتون سر کله بزنم</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76056" target="_blank">📅 12:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76055">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کریر کانفیگ فروشا با گیگی ۱.۵ میلیون شروع شد و با گیگی ۵۰ هزار تموم شد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76055" target="_blank">📅 12:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76054">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وال استریت ژورنال:
حکومت ایران قصد داره قبل از اینکه بحران اقتصادی دوباره منجر به اعتراضات خیابونی بشه، با یه توافق اقتصادی با آمریکا جلوی این اتفاق رو بگیره.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76054" target="_blank">📅 12:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76053">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اینترنت هنوز به وضعیت کامل استیبل نرسیده و خیلی اختلال داره.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76053" target="_blank">📅 11:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76052">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">معاون فرمانده نیروی دریایی سپاه:
با اینکه احتمال شروع مجدد جنگ خیلی پایینه ولی ما به هر حال دستمون رو ماشه‌ست و آماده‌ایم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76052" target="_blank">📅 11:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76051">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctE9VIxWVTz8t0c-UPUo7Gmg0C3cAW7jETdqjv8WShH3a1Qbvppu4HGzETr948P6MOSoSMg8CMwwpxPlKQ7kAGsrEtluymhObs3LJU_wQnkVPGdurCjHA-qLokl4yCWe4F2f3CRWQKySwukRVxNUPhLFpGIedaz6Nbj8p38z-a2cQhFhkRmdFVJ3WMnHzJIsN4Qgykej4dCn9zgML5hb1w167cXAUkStBzCNf11ReyvMNc3H4MZV19C_QNK2fRKoMGXVkJAQhyQ_HKShOHqC3_-WbXXXVnzVW6fAp3zyH7ALJj6lCEFypImc20ZWzBM08Et-pYccAExjH3OBYsVcTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرام خانوم برگشتتون به فضای مجازی رو خیر مقدم گفت.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76051" target="_blank">📅 11:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76050">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76050" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76050" target="_blank">📅 11:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76049">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sK8nwCdFCkioJsxUyUCHJTukZzRM5zU46A9iSQLKGL5SIs_PofDxAcg2NURu6cNc7Y1PCxpypvfMRquUeYWdBVR8TwjB1nefxDZNkaBF9wXttBiN4rCcunpmQSqM4kF3aUp5G_vnzS_piK2Zp9JAVIolIAGrGNghsPtbWN_F1HbKCEE8MXM17Dh4P-tJ_fFjqwYxTfp1vWgu--ArA-ajSfHKO7zcVDe5MopBS18yPOandpP_GjHKLpDwqYgMnqW-zW9ENUIY42FVxpa04PIYVZ1rFjf6EGJjiELIWxZo63kDxHsLmD5_kiQyUIKOLn5BxTAXPrsNLa5e9JxccSuNCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r6
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76049" target="_blank">📅 11:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76047">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وال‌استریت ژورنال: ایران در مذاکرات با آمریکا، خواهان آزادسازی کنترل بخشی از ۱۰۰ میلیارد دلار دارایی‌های مسدودشده و دسترسی به بازار نفت جهانی است.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76047" target="_blank">📅 09:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76046">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/247eb1347b.mp4?token=oDi9UyuoqdmLGF3LahX2YedZDgxBUhcoAzcRnYsVbH1zeqw9oRwBBtE1ZSRrCzjsomtALAZDCmB-ORGBLvCcVe32gwYVpF7llPgzBPSDDTWDzjMFgay2xBzqeA9C8orrK30CnNtOyyZ44Acvz4mDPRhAfELj15Q3ArnXvgWg56ZjbMnOsmGTczWWn7Y2o2lSZuBzrqFuJf1Gfo87kPn_9jdPQ4d1RtbdQdePXLkqyu6060_clV2ITdGLHOpVsPi7rHzxGmiwhv-kAqN7zhJp6iiIQTkPfd8-sqSzSLIUF4LQeNPTsra1M9VGzqPaSsVwIv_4UdR5mcTWFFI3wAEB7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/247eb1347b.mp4?token=oDi9UyuoqdmLGF3LahX2YedZDgxBUhcoAzcRnYsVbH1zeqw9oRwBBtE1ZSRrCzjsomtALAZDCmB-ORGBLvCcVe32gwYVpF7llPgzBPSDDTWDzjMFgay2xBzqeA9C8orrK30CnNtOyyZ44Acvz4mDPRhAfELj15Q3ArnXvgWg56ZjbMnOsmGTczWWn7Y2o2lSZuBzrqFuJf1Gfo87kPn_9jdPQ4d1RtbdQdePXLkqyu6060_clV2ITdGLHOpVsPi7rHzxGmiwhv-kAqN7zhJp6iiIQTkPfd8-sqSzSLIUF4LQeNPTsra1M9VGzqPaSsVwIv_4UdR5mcTWFFI3wAEB7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شببخیر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76046" target="_blank">📅 03:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76044">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ممنون از آرتیستا و سلبریتی های اونور آب که در تمام این مدت قطعی حداقل با بخشی از پول هایی که از همین مردم به دست اوردن یه پنل خریدن و کانفیگ رایگان دادن به ملت و نزاشتن این حکومت خونخوارِ دیکتاتور اینترنتو رو همه ی مردم ببنده، کمال تشکر رو دارم ازتون عالی بودید، دمتون گرم و کصمادرتون اگه فردا روزی باز از همین مردم طلبکار شید
ما که کیر در بساط نداشتیم ۵ گیگ کانفیگ دستمون میومد سه چهار گیگشو حداقل به چهارتا دورو بریا از همین ممبرا میرسوندیم کارشون لنگ نمونه، عرضه همین یه کارم نداشتید جنگجو های وطن، بشینید اونور همونجوری بزنید تو سر کله هم تا پیر شید</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76044" target="_blank">📅 03:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76043">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تا کانفیگا مفته بخرید که خیر نیست
صداوسیما: بازکردن اینترنت تو این شرایط خیلی کار خطرناک و غیرقانونی بوده و سریع باید راجبش یه کاری انجام بدیم. حرف پزشکیان مهم نیست و بزودی اینترنت قطع میشه چون حرف دیوان عالی انجام نشده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76043" target="_blank">📅 02:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76042">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رپرای محترم اگه میخواید کار بدید الان گلدن تایم کره گیریه، از من گفتن بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76042" target="_blank">📅 02:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76041">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219c3c116e.mp4?token=MBsb2n-7ateEypygsqKs1NXOnfkMkV4C2Wz0tjGs2va2SwluMVRbPqE4MXyvpzaPKM-HK_EEgr-IL85bFoUdlk4wsStXE8bQMbVydcNIY43XWoWjNUjFEnuUCcuqwpqGYoU6MAzxW5lkJDeEKiXdHNMOq2f2xQJNwOsQmsvtpa0AKAZa4m99bDCeZXxEFLfVsCzl4g1mLY1x0Ed-iiAwFjmGszMZrdQSlF2Hgu-xT4fmDuGOo0-NwoFJIBrBY05sr2_5awUDiJ3ZTP6SPUqCJy8aFhpjuJg4e-Ex6tqV444sDcZx6OERk0RML3wTUVtfDDYDIrtjNhxPF5Aaz2tKjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219c3c116e.mp4?token=MBsb2n-7ateEypygsqKs1NXOnfkMkV4C2Wz0tjGs2va2SwluMVRbPqE4MXyvpzaPKM-HK_EEgr-IL85bFoUdlk4wsStXE8bQMbVydcNIY43XWoWjNUjFEnuUCcuqwpqGYoU6MAzxW5lkJDeEKiXdHNMOq2f2xQJNwOsQmsvtpa0AKAZa4m99bDCeZXxEFLfVsCzl4g1mLY1x0Ed-iiAwFjmGszMZrdQSlF2Hgu-xT4fmDuGOo0-NwoFJIBrBY05sr2_5awUDiJ3ZTP6SPUqCJy8aFhpjuJg4e-Ex6tqV444sDcZx6OERk0RML3wTUVtfDDYDIrtjNhxPF5Aaz2tKjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون همیشگی  @funhiphop | reza</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/76041" target="_blank">📅 02:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76039">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">@Ali_nor30
یکی از هزاران نفری که هرچقد هم منتظر بمونیم قرار نیست آن بشه، اونارو فراموش نکنید.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76039" target="_blank">📅 01:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76038">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تو جواب سوال چرا نت پرو میخری؟ طرف میگفت چرا میری فیلترشکن گرون میخری؟ یه ناموسی هم میکشید بعد بحث تموم میشد.  @funhiphop | reza</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76038" target="_blank">📅 01:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76037">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WE8htaeYUsvwISv2Ty41hZB9xs2vTWBIIiEVD2ip0Vm3nhN9TsNIULZ8L0_yk1z4X3JVs2Boevn7XO3wP6tgPtCkJziYiWF7bemFt8NAAa996kgZar3XpmzY69it1qMUdKnWSp9oixl3XpcAECRZlJ6nXLDwymtgO3Vc1fFn4AaAbmkmkoR2CCOLrskGC02mdz6QNuewpnPnhrUV4pTuhHoqxIq9GviHpBwePOdNlVVMX1UU4xlwKnaPpsy9b30zPrSPkR_ILhOf_Hpw7-gjvY0Kb7tU1IWUQZoWsmNp3frVSpGjqgodCnqp79tn7WAWJeiyMIjzy0kJTSx7X3o4BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@Funhiphop | MEHI</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76037" target="_blank">📅 01:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76036">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fl8-lzdV7FQHJc66j6OEbahyphM0zOkjAaEcs4y-UXANPYPwQ9mftwVMpO2MxPbGXABIUzVd7jgpvB6RNT5xAIrOZJjXQ1n1RD98GF6Fc4Ql6lbiKbRqlGpZhukjfwjnbuvrxAHnZW2tifSctNWYMEpoDk8QTYRMyZ6-TuMqUHWj8BzLn_y_xpjvoJE4vGlccKa4tnfWjT9UcI1Z8ZxyacK2hgU5UIv9gpPFRANQ8UGUcDl6sXEwvx2cK7a_c9QptoukNRRZP4Q6x6iXMtUvGrS-nw_qETWXDFhiLxasJqGINnIHRjsT4ypsr7ZYc0c7kLF2Ux4ZnbsUZgnJ61sOBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@Funhiphop
| MEHI</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76036" target="_blank">📅 01:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76035">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پروکسی های جدید مخصوص دانلود سوپر از تلگرام:
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@Funhiphop
| Siavash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76035" target="_blank">📅 01:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76033">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OU6LW2woNZlgJ_282wSK5TmCaksEJMM0RiKNYoEBgEJELp1UaAwniLmImIK3KHvrXajXnyhJY-T4JhwZ8RfzirzaVWn4IlCGFILHpG6t1zIVJMbahJACAiPGlnfu_uuMnVQUXT9oRFxG88S0A2neZYWGgLB2FxnxZsald_uq2ipJT8jkdZTQJZrfJwiFH_zUgnfzi3r4YSpiJ17L58QZLi7AR6EwPLxpivamnvMvF3mLSbmmxED1BsoXrbMqz9dGNBHafiyBjz6BpIlZQ65EhLyBKbdxwoyid7M_WhwqEEUU8OiHuk2SbzFmdf9C9JHyNm3w-ZtRsv8aPb4qbT-phw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😠
ترامپ: با توجه به وضع بد آب و هوایی فردا، جلسه کابینه را در کاخ سفید برگزار خواهیم کرد و سفر کابینه به کمپ دیوید را به تعویق میندازیم.
موضوعات کمپ دیوید: ایران، دستاوردهای اخیر دولت در زمینه اقتصاد، کسب‌وکارهای کوچک، تلاش‌های ضد تقلب و تحولات سیاست خارجی
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76033" target="_blank">📅 00:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76031">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مقامات آمریکایی به CNN:
وضعیت گروه‌های نیابتی و حقوق مردم ایران نیز بخشی از مذاکرات است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76031" target="_blank">📅 00:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76029">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9wDcyD5eaiW8ONABdczDVsURE9_86tRpGKIpVEZ9k9leLCHRldM_AEesySdKAaD9gXqpRwJ_v20DqQmVIXvQjQ9OKXqNAGBMitQ9c92shzp6EjrABzC8GVXe_zJRrdRRWi7ytRATzGXDzUR2cHTTeeVbiRQ4ETDDo54OBZhoBkvae38Nc1jbRE8fqEoYf_VWgeryuF-RHLA9k2VoXYBwlrWqoGXM07RLVOuGxkyfp-VyOq9J4haLFjUAskKMm8N3HC8eijnmUijH36eCimRyxfI1HyVjjgS431Kq_juVGbGqKXA7zSXFwlyspduifKICTSUga6GoE7pLVac77WjNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76029" target="_blank">📅 23:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76028">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aqbo_A5FKhXACvLQUjJFn4N62rfI9EjQqa7aiH0CtTMwUdZkA_FNvvYKN7cUvdj6trldipPxFSPo3ElcPp0-xlVs4khl2b1NSOHOoiuDdQuYaCfU6B1axSluE8vICH-5cjR_b1Aoh57rePdU94CjzSewaSZ7C_QZR4a0OezEPBmQKDEs4FLRGHiyxD_tnRTV9E7EMHCHBDsehl-QeNRvF--swGDV-j-13tGmX0JHPuuvb89C2CpcGIKYVNvqDv3qCAmN5UCOKZ8nvnewLBwIHA38sXsE8RnqTXRy3Go5ScGaj86aw6YgU-mc5qsjm2Apws1KgvueS620T89SIgciDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست فارس هم جاودانه شد
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76028" target="_blank">📅 23:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76025">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5uu8g-YMXWMJpakFDRTGSvxfMuy3YziMrfpTJIQozesq6EQi6FnPlu_E08M2uUSu2ivo_W3tX2d9gcmMML8GNZsmLURQXxCwjzD6i55hVvUCVuD5sFD8anWjb6Dhj45LskMFZSm0iI9qQiJ1dnM1I7yV3ib32zpWr0iLpxiGKryLd2rifDis2zAjT9m1jgbDw5dM93XJQ0HVKVtZZoYVXmNRy6wUCfS9qeGCXWVPwDwLRn0b0RWWBT9ireXD3LKmFZikkr454ACLvgN4ijFU9AVmMXqbegeAk1eURhZMYt9HOTOqQk5ygZtgp0kCNSfE-j316okbna-jFO746X2-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌شان از بین رفته و در ته دریا است، و نیروی هوایی‌شان دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76025" target="_blank">📅 23:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76024">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کانفیگ فروش اوپن وی پی ان نامحدود ۱۴۰ هزار تومنیم هنوز نیومده، دارم نگران میشم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76024" target="_blank">📅 22:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76023">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نتم که وصل شد
بریم تایم لاین رو بگیریم دستمون با هشتگامون
✌️
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76023" target="_blank">📅 22:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76019">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نمیدونید چه حس بدیه از کسی که به کانفیگ میگه کانفینگ، کانفیگ گیگی یتومنی بخری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76019" target="_blank">📅 22:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76018">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کانفیگ فروشا انقدری تو این مددت در اوردن که الان میتونن پول بدن از آمریکا F35 بخرن به ایران حمله کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76018" target="_blank">📅 22:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76017">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارش های تایید نشده: فرمانده جدید شاخه نظامی حماس، محمد عودا، در محله ریمل توسط ارتش دفاعی اسرائیل ترور شد.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76017" target="_blank">📅 21:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76016">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حاجی دوتا2 چرا برگشته به عصر حجر شبیه دوتا 1 شده</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76016" target="_blank">📅 21:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76014">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تا دو سه روز سعی کنید با کسی تو تلگرام ارتباط نداشته باشید لهجه اپ داخلیتون از بین بره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76014" target="_blank">📅 21:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76013">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVZmkTXfRxksqjRTlTvZGt3GRPnjN-CAzF8qZYksUlyew_aGE54jKGgGr72cVVpQGi9ZzrbYFdZzC4ziwhL5iu4BBSrMPaWbZ-9DOkvdnPXCbv92bpALJFx3vXEoiQ0lyTjNTXCkhF6oLmxcz6TnSgFIkFdxOUjmxxtqqg8iJy6DrnnXN1ucoKJLzB0ByZ5-tBKZXykzq9a9yfztnfMPVL8eFxJ0Dv7Onz-MUaAMxUR5g3qAq1e1Z8fvBHGsHtAR3T-V697dtLlALaXOxo4SLvpYETwFLWlwGSrG5X4kMZqJyI0Z4QV6M512OrehOiJOiPjXPmfW4pfHAs0tPdQCOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">NetBlocks:
🫶
Welcome back Iran!
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76013" target="_blank">📅 21:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76012">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کانال 14 اسرائیل به نقل از منابع:
حمله به ایران پس از دریافت «پیام مشخصی» از آمریکا، در این مرحله از دستور کار خارج شده.
این منیع گفت که جام جهانی پیش رو و جشن‌های ۲۵۰ سالگی استقلال آمریکا عوامل مهمی در این تصمیم بوده‌اند، هرچند اشاره کرد که وضعیت ممکن است در آینده تغییر کند.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76012" target="_blank">📅 21:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76009">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اومدم بالا پشت بوم ساعت ۹ شب
هوا چقدر خنکه واقعاً
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76009" target="_blank">📅 21:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76005">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">جدی جدی مثل ماست وصل کردن، چقد عجیبه اوضاع</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76005" target="_blank">📅 20:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76003">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کصکشا درسته رو دستتون مونده ولی چرا باید کانفیگی که فردا قراره ۵ هزار بخره رو الان با تخفیف ۵۰ درصدی ازتون ۱۰۰ بخره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76003" target="_blank">📅 20:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76002">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">چی میشه که درست بعد وصل شدنتون اولین کار تصمیم میگیرید از فان هیپ هاپ لفت بدید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76002" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76001">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نت خط هم برگشت</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76001" target="_blank">📅 20:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76000">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اونایی که کل این هشتاد و چند روز و آفلاین بودن بزرگترین کابوس vpn فروشا هستن.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76000" target="_blank">📅 20:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75998">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اگه تازه وصل شدید و موزیکایی که چند وقت اخیر اومده رو گوش ندادید بیایید برید تو پلی لیست شیپ همشو گذاشتم
https://t.me/+7joX3IWJYepjNzFk</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/75998" target="_blank">📅 19:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75996">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حمید رسایی، ستار هاشمی وزیر ارتباطات رو آنفالو کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/75996" target="_blank">📅 19:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75995">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وزارت ارتباطات: اینترنت خط های همراه هم تا ساعاتی دیگه وصل میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/75995" target="_blank">📅 19:35 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
