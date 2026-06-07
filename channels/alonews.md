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
<img src="https://cdn4.telesco.pe/file/Y_jSktuvsFhV0Kx2gy3l4stVQEtXuc8U1nJmK_n39L0iiCM6OkECDfhbjd8duQfzEutHONwagdvlGRaIVy6Kyb7PZcARhiQuPTUoIgc8ntH3_Sc9xA6f_zhlkZk0ginDi8HgcccLT595iRDylLUbQpuhUh9GNHF_hpNmRK6JOkpryD91GH6-OdgvxXh2iAcg5gSrPOfe-7zoG1Ku70mapjApS84Z6VmjI49rgtvVClX_AUvAYTiVL0GNPwKDI5JZ-8A9lRIgvpJWuigcuOlgZOmL4Hh1JnT9Ue9N-oM0aUq60uH5d6XLlXh8tTYxVa8x0vcnlV1jNutsYPOkaEk6vQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 970K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 12:03:12</div>
<hr>

<div class="tg-post" id="msg-125702">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893be9ef42.mp4?token=VtSKKbMzF52DkOZowy9gfpXZ16zY4hwAkOzq7Gwk5sboXZhYIXResquxU_6INJ7WaE0r3F6n3TEGTOchcGDsEdVpN5r2jOrzsMkj-aMoaJI8HOVpJMoRHeHmbc0kl-TOiEeKwcQsoEON2sM5w906Orb9xYXJF_BF5bqDFD87iBXWXp_lvEmKADD3ZwJ97W4cDHCLvHLwuxQfhMUcYOouS3aHjRys5ny1K-Vwa_eX8PQPboHrDbypBI6jYSq5pSRq-kbuWyVpMredvjxhQlqTN41XwY2McM5jRchDP1DAC4YldnaRlfIZznfoJ8RR0KpOkVRSlEA7eoWCTjUuhpGacQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893be9ef42.mp4?token=VtSKKbMzF52DkOZowy9gfpXZ16zY4hwAkOzq7Gwk5sboXZhYIXResquxU_6INJ7WaE0r3F6n3TEGTOchcGDsEdVpN5r2jOrzsMkj-aMoaJI8HOVpJMoRHeHmbc0kl-TOiEeKwcQsoEON2sM5w906Orb9xYXJF_BF5bqDFD87iBXWXp_lvEmKADD3ZwJ97W4cDHCLvHLwuxQfhMUcYOouS3aHjRys5ny1K-Vwa_eX8PQPboHrDbypBI6jYSq5pSRq-kbuWyVpMredvjxhQlqTN41XwY2McM5jRchDP1DAC4YldnaRlfIZznfoJ8RR0KpOkVRSlEA7eoWCTjUuhpGacQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار تجمعات شبانه : ترام ترام حیا کن برو خونتون لالا کن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/alonews/125702" target="_blank">📅 12:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125701">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
طرح رایگان‌شدن مترو برای ۵ دهک درآمدی در شورای شهر تهران رأی نیاورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/alonews/125701" target="_blank">📅 11:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125700">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزیر کشور پاکستان با عراقچی دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/125700" target="_blank">📅 11:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125699">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
الجزیره: ارتش اسرائیل در لبنان در وضعیت واقعی فرسایش و خستگی به سر می‌برد
🔴
معادله کاهش تنش و محدود کردن درگیری به منطقه جغرافیایی جنوب لبنان، همراه با محدود کردن عملیات تخریب اسرائیل، در عمل با هزینه بسیار بالایی اجرا می‌شود.
🔴
اعلام کشته شدن یک افسر و یک سرباز اسرائیلی در درگیری‌های اخیر، موجی از خشم شدید و گسترده را در محافل داخلی اسرائیل برانگیخته است و تأکید کرد که ارتش اسرائیل در جنوب لبنان در وضعیت واقعی فرسایش و خستگی به سر می‌برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/125699" target="_blank">📅 11:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125698">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🌐
با ما همراه شو و در زمان قطعی   وصل بمون
😎
بقیه هنوز VPN حجمی میفروشن اونم با قیمتای نجومی
🚀
✅
از ما با کمترین قیمت ، بهترین سرویس رو بگیر
👀
😍
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot @NetAazaadBot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/125698" target="_blank">📅 11:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125697">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SXbhPWO3Vl1vzQoMz6seMAxt_yxtr1oZY2CFUrmkObrZy06-cViXb9LmwiBXl30pvhos1xfMn6y7H0UOjGPA51EV3-1ReJJAa6_tOmE_eVh6oKVhXGJORtI1SAzig8uXtfOKevYnJp04S8PfF-OA8gS9udyZ96uLU_YE86Tuzpvd07XzitBCpyG32tThNwLGO2ixh7a4-TJGjT4dKiy-BIGRy-mxR7bbFVUlL82i6vDjGVEhipNfVZxcuGWgCZ4mV7cazuEehNg3tDzsuKItinen6MBjuha4C844iCc_IOUuiTKkyRHa8OsQzMTNZ-0U-qkyUeyKymK7pqdnA20inw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🌐
با ما همراه شو و در زمان قطعی
وصل بمون
😎
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
✅
از ما با کمترین قیمت ، بهترین سرویس رو بگیر
👀
😍
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/alonews/125697" target="_blank">📅 11:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125696">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
تتلو واسه ماه محرم درخواست مرخصی کرد که بیاد مداحی‌ کنه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/125696" target="_blank">📅 11:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125695">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: در ۹ اسفند ۱۴۰۴، امریکا موشکی خوشه‌ای که با انفجار به ۱۸۰ هزار ترکش مرگ‌آور تبدیل می‌شد، به لامرد فارس شلیک کرد
🔴
این، صحنه‌ی آزمایش جدیدترین سلاح مرگ‌بار ایالات متحده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/125695" target="_blank">📅 11:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125694">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3FdiGnvhIpJkJiQMZUymQx-81W2YaU7KdpkHy-_mNQh77TN6QfQPeQcu5QFgb8uMuF1LaEsbcPoxjGVf4l9nfO_Yoxj5Ix0v61o1uwFavttq7TBPiasVdNBLixCn4a28T9Yi7fUZx9Tmj2x0D6mp95SnafRSqbOJOcZNCoyHOq_xmb1AYSrwCjdhcV-wwPSOqy4tJwoyS4UoBQP_USgKGDGQ4GqIF__P6g_y09Z1FPnGQN7hD3WqRwiHYgXzIcDvFJRHpRCjj71j25J7QJ_veSg43LFZhJa3Vq1DIYv-Gu-nSnAMulSH4mfqRQdWZKoQXm2wmw7qIKomUyTVmAH8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص بورس تهران در یک ساعت از آغاز معاملات امروز، ۸۶هزار واحد مثبت شد و به ۴میلیون و ۴۷۸هزار واحد صعود کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/125694" target="_blank">📅 11:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125693">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار کنترل شده در یزد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125693" target="_blank">📅 10:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125692">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">‏از وقتی اینترنت پاکستان قطع شده  کانفیگ‌فروش‌های ایرانی خیلی جدی رفتن تو گروه‌های تلگرامی پاکستانی و دارن وی‌پی‌ان می‌فروشن.
‏توسعۀ صادرات و ارز آوری برای مملکت به معنای واقعی کلمه و آتش به‌اختیار.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125692" target="_blank">📅 10:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125691">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
واشنگتن دارایی‌های مسدود شده ایران را برای حمایت از بازسازی و تعمیر خسارات در اختیار متحدان خود قرار خواهد داد.
🔴
رویترز خبر داد که وزیر خزانه‌داری آمریکا به تیم خود دستور داده خسارات واردشده به کشورهای خلیج‌فارس در حملات جمهوری اسلامی را بررسی کنند
✅
@AloNews…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125691" target="_blank">📅 10:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125690">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
معاون وزیر نیرو: هیچ برنامه‌ای تا امروز برای اعمال خاموشی‌ها نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125690" target="_blank">📅 10:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125689">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
واشنگتن دارایی‌های مسدود شده ایران را برای حمایت از بازسازی و تعمیر خسارات در اختیار متحدان خود قرار خواهد داد.
🔴
رویترز خبر داد که وزیر خزانه‌داری آمریکا به تیم خود دستور داده خسارات واردشده به کشورهای خلیج‌فارس در حملات جمهوری اسلامی را بررسی کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/125689" target="_blank">📅 10:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125688">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5faa7d2315.mp4?token=MDzqsBtWSZxi0eFKyJcgZrsoLFr72WaiOW1qZoeTdSQ2TPuBNFDh7H_MhlqaShIE5f8K-MSDCyDnBYvaTZ0FI2FzMBbYCFjoqiAsZzVVs5qXkxVI9TxWi7fS0qvr5IUt7sXHvbNYoJjoOCyFlxy_yERSrV11we9SGE1OaksuieG5hTVfMWTs8yiR5y4DOpeqgnHSWAS2XYVIoca6U2hvYP7OQGkY9yhbjwFNHhwIDUcHRw5ICWQ9ybF1cHmzFP9MByNOXgvg65VWaso1rQyoJiMjLbsxTeOkXFbLNEwgDHpiyvma86nltLeIrRGOMG5LXeYOL9sXeWoPWB2272GdzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5faa7d2315.mp4?token=MDzqsBtWSZxi0eFKyJcgZrsoLFr72WaiOW1qZoeTdSQ2TPuBNFDh7H_MhlqaShIE5f8K-MSDCyDnBYvaTZ0FI2FzMBbYCFjoqiAsZzVVs5qXkxVI9TxWi7fS0qvr5IUt7sXHvbNYoJjoOCyFlxy_yERSrV11we9SGE1OaksuieG5hTVfMWTs8yiR5y4DOpeqgnHSWAS2XYVIoca6U2hvYP7OQGkY9yhbjwFNHhwIDUcHRw5ICWQ9ybF1cHmzFP9MByNOXgvg65VWaso1rQyoJiMjLbsxTeOkXFbLNEwgDHpiyvma86nltLeIrRGOMG5LXeYOL9sXeWoPWB2272GdzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در طول شب، پهپادهای اوکراینی به انبار نفت سیمیکولودیانسک در لنینه، کریمه حمله کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/125688" target="_blank">📅 10:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125687">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkahdQEOBbWbbrAOlT9vWMRsyjyszeF-R7bf4M91UySVgw6Dj2VY_FdK36ud4Z-iHeCmPGRmnpn4zxPkGqSn91cCedHYqHC-rJKzNs2n_tmdKgprRAHgknKvKJCEw1Y_dvIkZxcuuI5pHRAlnz2UUHqW7rjHFvFHuEI_sZqRae0AjST87NNjF4YDiNQxVBJSWiR_bglIjvdw98KLcW3Mc59cKXJfxPvJToHAp5CQm37PzxcQwf_gyhhsykK3sG_0-y50Tqc7K1CpiBXKvyzc1jBImB756GtvUaNNDLLgPa6sP0A0Ad0tvspdudrWjhQwMWDcvgWHGu05WuAQCbzjmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه:مذاکرات متوقف شده بین ایالات متحده و ایران... و یک "پیام بسیار مهم" از پاکستان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/125687" target="_blank">📅 10:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125686">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
روزنامه اسرائیلی «یدیعوت آحارونوت» مدعی شد: خانواده بشار اسد رئیس جمهور مخلوع سوریه خواستار خروج از روسیه و سفر به امارات و بطور خاص امارت نشین ابوظبی شده بودند، اما مقامات اماراتی این درخواست را رد کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/125686" target="_blank">📅 10:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125685">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f9YLplwjE6VqFzk_PeyuX8MpCEXPZD3S5M1YyC0p_CZWX4d3eUTFFJjRSPdKDWOiSgPST-OAg10d897zOL0gZHzTAA-bo3R6BHWlOla9BPUUec3jQXpanLBSEsDyUpMflsk477i5DabvvP4nI28b3uTifT2Nok45Avn8UIJmuRT82LZMDfXT9ZZHZKKX-eQ3GnN1qJDFma-cYIkAk12auvNawCXaZhWV95NJ5iCm6iQ5R7kseNJKREEeA5bVKspORt9hHyMm9xUKkQt5bDBdaWrYlYT4LGqoJJE5_uoup6iKMw03aMtVB1qkYWbEGppbduJeIl00yClrnH2lhIYe4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذخایر سوخت تقطیری آمریکا به پایین‌ترین سطح از سال ۲۰۰۳ رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/125685" target="_blank">📅 10:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125684">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
الجزیره: در پی جنگ علیه ایران، ۱۴۶ کشور قیمت بنزین را افزایش دادند
🔴
نرخ مواد غذایی نیز همگام با قیمت انرژی تغییر کرده؛ این موضوع بر هر مرحله از زنجیره تأمین، از کود‌ مزارع تا کامیون‌هایی که مواد را از مزارع به قفسه‌های سوپرمارکت‌ها حمل می‌کنند، تأثیر گذاشته
🔴
اگر قیمت‌ها همچنان بالا بمانند، خطر سقوط اقتصاد وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/125684" target="_blank">📅 09:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125683">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
فرار هالیوودی با خودروی پلیس؛ متهم دستبندش را باز کرد و پشت فرمان نشست!
🔴
یک متهم بازداشت‌شده در آمریکا موفق شد دستبند خود را باز کند، از صندلی عقب به جلوی خودروی پلیس برود و کنترل خودرو را به دست بگیرد.
🔴
در نهایت واکنش سریع مأموران، این فرار جنجالی را ناکام گذاشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125683" target="_blank">📅 09:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125682">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
یدیعوت آحارونوت: هنوز برای اعلام پایان توافق آتش‌بس در لبنان زود است
🔴
با وجود اعلام حزب‌الله مبنی بر رد توافق آتش‌بس، اما حملات به شهرهای ما متوقف شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125682" target="_blank">📅 09:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125681">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej_PiE0_CDEMqiJHn3rl_sFk0M4J9GphhWXKikoBe8vylgNu1XYtWFZuHI2YdTs1iIEsn8J2A1ngnZec2H0dkS4SD7hxx3ZuR3wbE9eX-CgO-UwLsdTurXyct2Jc_Hi6eQvU2ONlXsLLn-uDfTm5ihaJEjGccjH0zTR3ObZ_5IHcCOzROg6HldAZtEDBrfq04XsgC64_D_aGKmTQDVvxqWdLlxPyMEElmtaKCRsbKJYJpvOXV9HH7cy1YSySRtyq0tyuQfzJADc6jun-gBC78QQJIv-wCEv2VISBCeIvWMBVwBTOE3Y3GxtvIQnVFzTsW2Dh1lkwzLyOSg4hR3o9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۳.۰۹ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125681" target="_blank">📅 09:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125680">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDvutrp5ml9SGGOnRftK8lPHvDsSr1g9rJ-MMHOcELfxhJRMO1Gu2Ns0we2dZx97PKc3CFbNfa6ck-y0Meyi8jkJoRqFynJ4cBTl6ug6NVtHypbSi6VJxLI74v0sN7yimsmu67P0FuFuoWFTojluuMnR69hFePnhglBC2ZFo3KTbKfVMuc4ZwMNo8M_Msd_p0ysEEUMsc_DNVosmG6iWMDCwS1Gv3jNay0UjukuVNvZu5qfHbyr3KpniOHAClyE4-5tFlFrdywGX2J2awCvxo9ODNPsj2PZHpsS1p8662QrBpBOf7OA5RfVFGYJVP5eXUxdcf8ugqjRLz87LZMJFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ با انتشار تصویری با عنوان بندر پهپاد نوشت:این روزی واشنگتن را نجات خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125680" target="_blank">📅 09:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125679">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWKq8eVg5xpxr_hlnJ8SqYl3wlmGHos3iJq-E3RzDZvSDpLf3R9OowdIg1g7MoZ9oA2-2J-qiqPpjIIKF5mj1ZqDJB-Qya84eV3BGbIkmom4ntO2BWYJjo_0lDYToXkS-bXC0W1mhnAMOhF-P-jgno_jn3f3erzalk5Oa_5cVKCl8pPL-J3Agr1anKQnfA2NxTF7v7_rcYhpPXS7KdqKIzRaa3lSgq6fUyEs8V-bT_UnOVmSA-9ZMEILDquvoABWg-tCAXnzBm87xzBtkzkMbn55gl4BDOqTCED6fckZui7sg5crQbTtVEkb7AUpT_4Tev9iPs8T1k49Op1h_p0jsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیم یو جونگ، خواهر کیم جونگ اون، اعلام کرد که کره شمالی هرگز از جایگاه خود به‌عنوان یک قدرت هسته‌ای دست نخواهد کشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/125679" target="_blank">📅 09:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125678">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
یک تیراندازی جمعی در یک جشنواره در تولدو، اوهایو رخ داده است که در آن چندین نفر مورد اصابت گلوله قرار گرفته‌اند.
🔴
قربانیان به بیمارستان منتقل شده‌اند، همراه با تیرانداز که در بازداشت نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/125678" target="_blank">📅 09:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125677">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سفیر ایران در مکزیک: تیم ملی فوتبال ایران اطلاع یافته‌ که باید در همان روز مسابقه وارد خاک آمریکا شده و پس از پایان بازی، از خاک آمریکا خارج شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125677" target="_blank">📅 09:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125676">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در اربیل منابع خبری عراق از شنیده شدن صدای انفجار در استان اربیل در شمال عراق خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125676" target="_blank">📅 09:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125675">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
امتحانات دانشگاه جامع علمی کاربردی غیرحضوری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/125675" target="_blank">📅 09:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125674">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
کره شمالی: سلاح هسته‌ای، حق حاکمیتی غیر قابل مذاکره است
🔴
«حتی به اندازه یک سر انگشت» در این موضوع عقب‌نشینی نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/125674" target="_blank">📅 09:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125673">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGKTRr66lUC9wibSB7yvOuJHBNr_kyu4lSClu_Z7onvjuoS8RM7BAPUB4yGf6lqHIH9ssm9VPelyd1WV-rNEciDOHs-jqQ8-RQHCeMidKbIMTyPnjckOxeo0NLJ1SVTpiSXxL8-qXpvQUdIaPxeJ2axsOk0Locfq6_WE78jytRpV4PqBC5pLk8YTehPCSgs5ykbwokJgvDTNwI0qHUeXmi7SDhW_8iUoFBPrmvWmlpUyV8dsfJJEqFM61DsiJINuEF2jyPabJS3TZF_g11tfPfQ6Ja7j7sD8_0VvIwjSAZLf1vn94PGIaYkasMWhkHdHDIUxiVMdq0PelGCpO2TsFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام مدعی شد امروز دو پهپاد ایرانی را بر فراز تنگه هرمز رهگیری و منهدم کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/125673" target="_blank">📅 08:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125672">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
پولیتیکو: راه‌هایی وجود دارد که ترامپ می‌تواند توافق آینده با ایران را به نفع خودش تبلیغ و توجیه کند
🔴
اگر ایران موافقت کند که برای دسترسی به دارایی‌های مالی خود از یک خط اعتباری استفاده کند، ترامپ می‌تواند ادعا کند که بر خلاف اوباما، هیچ پول نقدی مبادله نشده است.
🔴
اگر ترامپ اجازه دهد ایران به نحوی از تردد کشتی‌ها در تنگه درآمد کسب کند بدون اینکه به طور رسمی عوارضی دریافت کند، می‌تواند آن را به عنوان یک مصالحه قابل قبول معرفی کند.
🔴
اگر ایران به عنوان بخشی از یک یادداشت تفاهم درباره چگونگی پیشبرد مذاکرات، تکرار کند که هرگز به دنبال سلاح هسته‌ای نخواهد بود، ترامپ می‌تواند آن را یک امتیاز اولیه بنامد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/125672" target="_blank">📅 08:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125671">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tohEHrfBbFVef42P7I8FtnxrSTEQxj6M3qnAEx1ZNHEtUbO4AQ0llDRqpZQDVIdmP3WMSUMP4nCbkpJ6tT1aoPsfK-ulhiaG-2beO8U9KlC16phPflbmG5qOozxmaTnPwPhf1euLXdcjvrHf3KuPOpLFz9fDWNqq4IIGwJIZwV1wsMs_jH3WMTZcQSbye6oJswn20jGoB9unr4CSymgUGFVb_nHl7V6TGZFTsQYMw8punh5r2r7wok4c8VipQ7uNn8jK2F9MqZBoDIuAksaEzA1b4fQXCt-7pKUAFmVFRgv4Uj_vU8a58iduvI1lMCqKJIrTK5Hy013mv0XE-7Nypg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایجپت اینتل ابزرور: تصاویر ماهواره‌ای تأیید می‌کند که از آوریل ۲۰۲۶، عملیات توسعه قابل‌توجهی در «منطقه پشتیبانی لجستیک ارتش ایالات متحده» در ینبع عربستان سعودی، معروف به LSA Jenkins، آغاز شده است.
🔴
به نظر می‌رسد که نیروها و تجهیزات نظامی بیشتری از آمریکا به این مکان اعزام شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125671" target="_blank">📅 08:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125670">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزیر خارجه عراق: یک فاجعه اقتصادی ممکن است رخ دهد؛ اگر جنگ علیه ایران تا پایان سال ادامه یابد، با مشکل پرداخت حقوق مواجه می‌شویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125670" target="_blank">📅 08:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125669">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTVGwXSBDGiaUCRjyV_1fP7CX0o9Gzrmm4S4uZKX5jVuEvocJKFr11OONUblO8HOILrBy0iy70V4o39WFz5uG8HxaFlG0bWObEQS3eipPpf8-WzSRWwlTyJOMvZ47umzoB5UhXMeB0uFY9u8MLe8cSQ9pho5x3O5mNElGq8G-xMh7Uki46ED9G6-Q2CNCS7qjzbZH5e0-UkRkdCEz9mZMveYsNnW-nS26caMAyww_x3yrja0qxBVzPPhkYV3iXCGPWUqml-PwBfXn4u6DIUKop53XjfnWNmn9FFsQeG30weoRGipm6ure6lyXPMCHr7uwdPRSlLPc6ApNTjDbGpndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش CNN: دولت کوبا شروع به توزیع سلاح به شهروندان عادی کرده و رسماً از آنها خواسته است برای یک تهاجم نظامی آمریکایی قریب‌الوقوع آماده شوند،
حکومت نظامی در پایتخت کوبا اعمال شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/alonews/125669" target="_blank">📅 08:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125668">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_DLYbS3EppG54ErI9OFfGe0iDV9kUORGjMfURN3bKLl0QCizCJ2m_9rG4ZlwBcOGgnsi67JFRMQA_dE1lmANdPlDC1Uw1pg_7JmRxsK64JEMUJBtKn_fZPqWSeM5gopme6MEoJR_h6qMvw3ha8lqKVvqe2EK1frYRa5thZoOkH9tzl6eJsO3TS03pvJVbowAtI6timdu-3GI9JvbzRQ4T_EmVYAUpuR1NA_X01rgP45W6FRKrywzIaexSb0bPe4bh7jBZ2cAFmJz5v832Nr0iqaNHa4ylylc1jL-8ydmFulNASyo3__flbikTOQGnYslRUWtCmXubP_DMDHl6BG8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرچ گوگل یک سرباز کشته شده اوکراینی: مذاکرات اوکراین و روسیه
🔴
مذاکرات زلنسکی
🔴
جنگ در تابستان به پایان می‌رسد؟
🔴
چه زمانی جنگ به پایان می‌رسد؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/alonews/125668" target="_blank">📅 08:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125667">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
کیهان: چرا از NPT خارج نمی‌شویم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/125667" target="_blank">📅 08:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125666">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxzqtlRJkFkL6ymhR7UJsh8Kcw-b54mOLkMtChrC4v--uRGr36ZWICNdKRtMMarrqOiOsINuoIXDF25OPPO7iNKSALsTL5qwx8W7WeWPMIxq9ZhWQdR9tGVnTwtusfQsWTV1Z0HOD-64knVFaZ51ITU7TqwuBmUAqxrxaAu1kgyKifWlE9SGICEv_caEGzWUMntghaedmZ7_s0dIOqoO43ZW8TxBcOp-Asz_UEDDMTrJv-CcMqO9SHrMRReZ0Yz4yuTBwGVaw7bAd4820kDz4pEAHY03PDC_lFsWJ0jVCv0OJf5Fg8MP4YqJp_z_WMmpzQw459EsqQ8jcCzHcMFs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارزش یک میلیون تومن وجه رایج مملکت از سال 97 تا کنون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/125666" target="_blank">📅 07:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125665">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0rorRzdaghndyAbecL3S0VKYkbri2SHsqIjFEFwYpO0axg6GGrmCHrgQnEVJyxyGVsROrPCaD6409l3tG4YkPzkuamlomCZ1TXXOF4gw2uMT1aQ07z5A0ucU1QB6HOWhzon1QXj6QbBPZyWskz7o-hwcBlHy0w8LiRCeNqsdXIHEbvyG6O8zAvv4KsnhS3KR_DtE6TO8Bt1w5qM7ZlfQEZQQ1pm-ajUlGuxHPZbznFv5zA-1MAg8lMccicgpoNaZwa-K-3zWIz96pLi_B726j-UBCWL-3-R4gilX4sv2vXvupIggaT4lAazmNalmFnmi8syttxjRB_n9B5W47skiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای جدید نشان می‌دهد که انبار متعلق به شرکت فناوری انرژی آمریکایی بیکر هیوز در اربیل، کردستان عراق، کاملاً تخریب شده است.
🔴
این تأسیسات در جریان حمله پهپاد کامی‌کازه در اول آوریل هدف قرار گرفت و تصاویر نشان می‌دهد که ساختار آن به طور کامل نابود شده و هیچ اثری از انبار باقی نمانده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/alonews/125665" target="_blank">📅 07:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125664">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/voOe_XjOX6w_jkg-dNGADUzSG2dwSwknBT1fObzu20v5yCH3h1iPmX8ogY5bwWAmXGk8a1HYW9wcCqEXYX-FPskQFx5B6m_F2bhvcycn6hPo5CTsqs3lNc6m6Cr4ViHByx7fpf5t-TQPW_5ElMDeOrxDvtPGrmot-Krk2O5bBpPSFPait9f7QPCptDtpWzCkybkLECUZ7r78I2a_MChvobKb4RFmT8-Zr4HimwKuL3ZA1dkQ1b08JQM92Z7XAcB3i9SC9fGNYZ69XuFE8wiQEXfzj_JT-cQnEi1faowZKtwlDikV9_c6PKiDxTSAJv2C4NcvDETRtx34K8AwrvRk8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
نامحدود فقط 90 تومن
😍
فقط ۵۰ نفر اول
❤️
✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 90 تومن
🏷️
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/125664" target="_blank">📅 01:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125663">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران:
پیش‌نویس یادداشت تفاهم ایران و آمریکا در اختیار نهادی در تهران قرار دارد تا در آن بررسی شود.
🔴
این پیش‌نویس برای اینکه بدون مشکل به سمت اعلام توافق پیش برود، به آرای اکثریت مطلق نیاز دارد.
🔴
ممکن است در اواسط هفته شاهد تحولاتی استثنایی باشیم؛ البته به شرطی که دولت آمریکا مانند دو هفته پیش که تشریفات اعلام توافق آماده بود، در لحظه آخر نظرش را تغییر ندهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/125663" target="_blank">📅 01:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125662">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip-D8AFEPrL9zHKbH8yoW39f8DO9ZqsOBzfBqWh93__x3F5SoyVfRP7rV6vUyyCZwuQ9BGi9P722aRzugGaQsGuu4-AsGyVbq-9OfuxziO3GFxo6GmCZPoX0vqx6O_sN75PkWMSDNCrJVWxS6ExDCdvvPAtC8eTaNQ6_5LB2ZZgp6wb2P6iOMqJ1FnVTL7xMZstZzK6I2Cuun1i_LINDYQCohva0ZclQZV1xdJnn0ZE1dsNW4S-tXaAQoh44G-cw2GMsTfrhEKxsl0FJsRe4OTXLbiPatuDLLfAio-CdyIjHhCEoscNpHB7_tbvUKHliLwHVGhrcl2ZHPWrJVKT2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کنعانی: حاضریم تو زمین بمیریم اما پرچم جمهوری اسلامی بالا باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/125662" target="_blank">📅 01:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125661">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2ca304ca.mp4?token=hZEOnOB8zz5iJjfeuwizFn35DOHrRcX9xaQJ7-S2fP1DKAMeHRBvxKLJJNSkuBxK_qCS93K6j0Bzu48hhD-lnyHeN5nt5lBXTp46UbWdhh-0CsmFFs2Hum1uEZUmjVDKic4S01Hg6NTP-l9jljIXZv0kIHbsM21-1AC-nJxx19o8MsIZr-w6kEgtUnPlYV30rYrbmLM3tYemgPv3pyNmfjBjk6MF_B7voZXTVCLDGF0IBNb5rmCeha-1ODxknZgMO0dt9U9rrwRyPurCIbtINRaL_GGvu2nK9-OV7qMlLusS54W4zlgFDoDOhv-ZLXMCzVpaWgp2WbFDb681DONA8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2ca304ca.mp4?token=hZEOnOB8zz5iJjfeuwizFn35DOHrRcX9xaQJ7-S2fP1DKAMeHRBvxKLJJNSkuBxK_qCS93K6j0Bzu48hhD-lnyHeN5nt5lBXTp46UbWdhh-0CsmFFs2Hum1uEZUmjVDKic4S01Hg6NTP-l9jljIXZv0kIHbsM21-1AC-nJxx19o8MsIZr-w6kEgtUnPlYV30rYrbmLM3tYemgPv3pyNmfjBjk6MF_B7voZXTVCLDGF0IBNb5rmCeha-1ODxknZgMO0dt9U9rrwRyPurCIbtINRaL_GGvu2nK9-OV7qMlLusS54W4zlgFDoDOhv-ZLXMCzVpaWgp2WbFDb681DONA8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخوند، اسماعیل رمضانی : بالاخره یه جایی باید مشخص بشه تا کِی می‌خوایم مذاکره کنیم
و باید چه اتفاقی بیفتهِ که بعد بگیم دیگه مذاکره فایده‌ای نداره و ادامه نمی‌دیم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/125661" target="_blank">📅 00:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125660">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Akg-yauBMAHgUJ3z74z4OZQ8Ely-DtPYxMviUWAM08eFVLo9JA9FMU5WPBYC3Mbx827_UrtUwUHcXsAL031-pgjVXD87iZhXcFK3s4IH_Qd6emypHJd8nHCwhSrFKQtTrSj5o8MAWT1BSRwZgVE1EdDkmkiQi9_DCfQKJcNmh3-rEO-9eC8HIVuz8HX2plCvZfKtCwbnOlGxw7jr_GDNza-ZUgl_YRI8gFI0iDr1DqZzMusjIb-fj30Gs8wBVdd3tZwue7rE5tcUoVvgnLSSYdCJuIqfeKlCXe8d-9M508XMjFxU_Ir7fOtY5AJu-Vdfkm8UdnYAyfJaDnESeUj5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
درپی درگیری میان پنج دوست صمیمی در ورامین بخاطر یک دختر، چهار نفر از آنها به قتل رسیدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/125660" target="_blank">📅 00:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125659">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zo1ErrpJ-WcCHoqqnCMb9_R_TJ0kyA2vgWn7Di7AOHXXlx5-kfenVf-gfvWJjZ8KTg9L2Fc3O0EPLc407Om-VCdCu-FKcSGofHc3w0JcsoLERqas3HXvXefPQfjoXwSiVmVX1bx_-ft08Qpf6d-t9WqYuzkez-SSo-txUbm98dFYsiOPpyVt3U-651ZroCVW88wLuVKgr4iX1qYjDTBXdzJvyI19uosRfiMmcnUf2sWCbNLstRRjSFJmf_cpjlui2bM1mR-sk-2EOuHJJolwMk0c5e2n6P_E-RGHKygNAbzzwdV6PIfrt-I_awk8tVIhPklkJIAULQ-hprp19Q7kXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به انتشار پست های عجیب با هوش مصنوعی ادامه میدهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/125659" target="_blank">📅 00:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125658">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ثبت ۵۰۰ مورد ابتلا به ابولا در آفریقا!
🔴
سازمان بهداشت جهانی در بحبوحه نگرانی‌های فزاینده در مورد گسترش بیماری همه‌گیر گزارش داد که تاکنون نزدیک به ۵۰۰ مورد ابتلا به ابولا در منطقه مرکزی آفریقا تأیید شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/125658" target="_blank">📅 00:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125657">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mot-dFe2KWdHxYunV5NUleKOM-rukw0W3yT5g1ObCPJmxXFZh1omVyDcBiTadLIAn0MXd5AJGA84WaxdKafUvCuICT21gbg8glhlnf9LaAVctEiqHsHoNzInrmcfmxf4qAgBB3WSv9RKp29eJn-hjIOZRuUc0TujAklOul7a-dMwwC2FQt-hUdWIh363Dqe37mPFFuG9ciq_4mRl_AIhvWzgdS2wsISJZ4kkKjDa1KTVqmsnaCjvvBWpxoIPQ8KSnq37aO_peg1Ah2T2OpTH4EP_HGYlzLOOmaK3xB5r5xgBPvETZQf5enraFxTK2oUs9PFGXvHMAZo-S_gbi87hVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/125657" target="_blank">📅 00:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125655">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FYjxMBcV97SQiXPj0xR8kKm4Vcz-l-UMoWC5NNlKft3UCHP2B_2qQncSF_CZjeakQ2rpeA1Fq1EDVvphcEz3MnnFwHnIhsrJ2o6dQ81jGi_m-AVL3dJv97xhqPLmgpcB-GbySDMvb0hKUHEfA19rg_iWxFUuEDlJd8wjA_l_pfvAP-JHuGm7NxdH6CjlDJQCW0zRY5O4jBV0dWVx_wzQMW92uFeII7hdwm_m8ylm774F4L0bFQwSgvz9eZsDJz7Lnsm73X8y1rsb8tJl5b4fJzT3Nyb-ImikkoNUrmEqZRFa70Gnw3xgTf-rP5HUPDWrZ4Qa17Le9PQK30drjP6QAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fmPbwDL1MrX7O3bLXZvD21mv6Bp705IBjhCPy5jonWsfCi-wpLTZ1dY86W2PwtVqhcDk9e66xZWTJ-I5OMcw-7Ti7LUyuA5p56R99tMfcFE6hw3xqo8GbVQVvTGwnK7xWmBn3ABVSnsB1c7QQjHRofrVjN5VqSA-wj4sD7H_MWq4VpSr-1HalpTx8YrqMfDnL15SSFzQ_Zsi58BYbp4DoF6qRbUZncWHfQdpvHs_8CT6DxHBKbEd1DH2No3ZEIa06D7MNJrb7UHnsrpGsPAxOkrATFLFv6YJnEUqlysMg6n7xkr8LTrKK_y5b9_hdkIBLAbHrV7PEFh6aVNvxqgj9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اسرائیل اعلام کرد امروز دو سرباز دیگرش در جنوب لبنان توسط حزب الله کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/125655" target="_blank">📅 00:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125654">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lny0Ed1yrSek4kPj1PcdYAMdrrV0hpsTHA-FWA0732WEqBldOL2433uMQMxtuqWtFtjn7OmY1BlZNar2ceqBNp1p8aM80yBk_AAoGpqoFrATFj5MxooIg9L8p7OiZve1s9Apj1QGMMXNRELa8OUBQZd3zyBdgtJT6cBGcy1wgDZMRWunc7JsqGNNc_rKtxnth2eIM8-J-HJ74WbgZFNonZ9ITpDORIa5GMttcWd715WELa6HGl-OzEiC98JAwyBaH6YnyQemhNgZmQGlo19FOpHqj_NxVcuoauAtVHN1xUOFcxjkBEBzytBu9qj_tEUlEK9bW00dqWP57O8WRElDkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره‌ای پایگاه دریایی شهید محلاتی بوشهر قبل و بعد از حمله
🔴
تصویر توسط پهپاد Q4 تریتون امریکایی از فاصله ۶۰ کیلومتری گرفته شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/125654" target="_blank">📅 23:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125653">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
لاریجانی، کارشناس سیاسی صدا سیما: مردم خیالشان جمع باشد که ایران برنامه هسته‌ای خودش را به هیچ وجه از دست نمی‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/125653" target="_blank">📅 23:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125652">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a83f7f667.mp4?token=cdJvg5Kq9sIfTzr5WLX3rvLWDDgexY0YFGjZ1byTHsbRv8aEGldG6i1wjhmKakjMMNM48bmp7555y497a2rnqDiE8RdNYbPB1fha8qwItleJ7mstT7VAfpLjhncsLakHtclhBODSflGDnFYkc75FBPLyNCfQ6eDJySjRATyVdy3eP7B9Mhqm4C3vY0S5DVnwFcwewRo4T57ovXkTo2FLDGeIlVDl_xbQWIwGfDNv2Pk6oGdrGolhmkAN3MiCU-U4vt-FoyTVC3Xzvbhihbo0cEEwVnPJl8xYPhasFjSC8swDtTyLtOSuhMj2EUm9z1UUcey8pqOkgHMPr3HN_EFZF4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a83f7f667.mp4?token=cdJvg5Kq9sIfTzr5WLX3rvLWDDgexY0YFGjZ1byTHsbRv8aEGldG6i1wjhmKakjMMNM48bmp7555y497a2rnqDiE8RdNYbPB1fha8qwItleJ7mstT7VAfpLjhncsLakHtclhBODSflGDnFYkc75FBPLyNCfQ6eDJySjRATyVdy3eP7B9Mhqm4C3vY0S5DVnwFcwewRo4T57ovXkTo2FLDGeIlVDl_xbQWIwGfDNv2Pk6oGdrGolhmkAN3MiCU-U4vt-FoyTVC3Xzvbhihbo0cEEwVnPJl8xYPhasFjSC8swDtTyLtOSuhMj2EUm9z1UUcey8pqOkgHMPr3HN_EFZF4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آلبانیایی‌ها به یک اقامتگاه مجلل 5 میلیارد دلاری توسط شرکای کوشنر در جزیره سازان و تالاب‌های Vjosa-Narta اعتراض می‌کنند.
🔴
ششمین روز از تجمعات تحت عنوان "آلبانی فروشی نیست"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/125652" target="_blank">📅 23:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125651">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
باراک راوید خبرنگار اکسیوس: دو منبع آگاه به جزئیات به من گفتند که معاون برکنار شده‌ی رئیس موساد، یک سال پیش بودجه‌ای به مبلغ یک میلیارد شِکل (حدود ۳۵۰ میلیون دلار) و تیمی متشکل از صدها نفر برای پروژه‌ی سرنگونی حکومت ایران دریافت کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/125651" target="_blank">📅 23:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125650">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c6bed627.mp4?token=Tr6Tt2rFak15EjcY5PPasTb-Ooga1mIkhtmiYM1-F8cxT07B4_Dve6xsIvEy50Ji1tLyvNoa3yMWMOavroS6s6wTe-OTKhcgPMn1Zo7eVCj697PYLttdFHO2PJoMJ-jSZxRdBa0lWFRg34a8f-6RCcMd4VK8HaGqReMGm3eM8knV9vLNU0PgTUVlQPr5FLge-cgBrda0lFLL-l9n8Q-BoWUszugieoyvaNNCELbqH4Ft0ALH7kHiFt2UY_B9KKY1xzXzsQICh_-rInGFRJsGhYP11CNzwcZgFri_fwalSRHtdR3D0ZIUPxIOFYuMzLldmHf9tykkvrkBMIcY8qyAfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c6bed627.mp4?token=Tr6Tt2rFak15EjcY5PPasTb-Ooga1mIkhtmiYM1-F8cxT07B4_Dve6xsIvEy50Ji1tLyvNoa3yMWMOavroS6s6wTe-OTKhcgPMn1Zo7eVCj697PYLttdFHO2PJoMJ-jSZxRdBa0lWFRg34a8f-6RCcMd4VK8HaGqReMGm3eM8knV9vLNU0PgTUVlQPr5FLge-cgBrda0lFLL-l9n8Q-BoWUszugieoyvaNNCELbqH4Ft0ALH7kHiFt2UY_B9KKY1xzXzsQICh_-rInGFRJsGhYP11CNzwcZgFri_fwalSRHtdR3D0ZIUPxIOFYuMzLldmHf9tykkvrkBMIcY8qyAfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجیب اما واقعی
‼️
اندی هم مجوز کنسرت گرفت
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/125650" target="_blank">📅 23:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125649">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
جهت رزرو تبلیغات فوتبالی ویژه جام جهانی و vpn در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/125649" target="_blank">📅 23:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125648">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
تابستانی گرم‌تر از حد معمول در راه کشور / هشدار آبی برای ۴ استان
🔴
رئیس سازمان هواشناسی: با وجود کاهش ۲ درجه‌ای دمای بهار امسال نسبت به سال گذشته، پیش‌بینی‌ها حاکی از تابستانی گرم‌تر از میانگین بلندمدت و عبور امواج گرمایی از مناطق مختلف کشور است. استان‌های تهران، مرکزی، همدان، مشهد و بخش‌هایی از دامنه جنوبی البرز با محدودیت منابع آب و شرایط نامناسب بارشی مواجه هستند و مدیریت مصرف آب باید با جدیت ادامه یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/125648" target="_blank">📅 23:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125647">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YwJikTgkXQhz78VJk3zguuGd-8-wBVNYTL-XzSJwfD7eblso7b1NG6-nx4IBYG62_ufT2fVPafyGnH6yLCUzepNFbMDj4TevSkQLyypcLpBN855_rFJuAHwspMH3RI0Sovt5mRwUNyL1Sfw88KyCYJlqkXYaSszMAZnt8wwCbf5ZzfeI8Z4eTlqPpiiRBGKCj6KYwqB0LQYYdG2FDnXWeqvufya3Y80suaZyi8H9ET8TQUVDU_PVSPoLUC-lCLTGnmophQ7Ims47ETFxlRNRx3dlDEH3PZa2xI3QRDVbNEzmGOjjB5npXL6spZ1eoVwsHa0Cub8CscwBuemluhiJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز تعدادی قایق تندرو نیروی دریایی سپاه در مناطق مختلف تنگه هرمز درحال گشت زنی بوده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/125647" target="_blank">📅 23:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125646">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزیر کشور پاکستان: پیام‌ مهمی از سوی ژنرال عاصم منیر به تهران آورده‌ام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/125646" target="_blank">📅 23:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125645">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTYWyG_86LF-9elYA4wWjjk2WQeuEjNSBazQrUeuaOuyr9CuMhA8GJca8K2MLtPwYZwoJGB2d17RZlj37n836yF4YN48l4GKGwcBk4p-OOkDujSWVdChQPYG34Vi-f4zHya5KBP0otmrfRbSZA-vv0NVIHdTRDcs5QSAhmAh1gDj-mfzXO7vcaVJyFeUNDoKrROfPfSSOiGFVc0RmZRdBm_aZsfAQJCOe7g0aXl6EKsTKhecajIwHrGZILc7D9HAI0yZTiBhJE2Zr0fkNbfcbtjmtUmTmGPlRrHr7-2t63Z3jO12hyYMYLXyD2ZsVmyP3hD3Au1-ZGvfWoTGfRBcsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدف طاهریان مدعی شد بهمن ۱۴۰۳ به ایران بازگشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/125645" target="_blank">📅 23:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125644">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل کاتس: سربازان ارتش اسرائیل همچنان با شجاعت در لبنان علیه سازمان تروریستی حزب‌الله برای حذف تهدیدها، محافظت از جوامع شمالی و تضمین امنیت شهروندان اسرائیلی عمل می‌کنند.
🔴
هزینه سنگین و دردناک است، اما در کنار این، عزم و شجاعت سربازان ما برای تکمیل مأموریت قوی‌تر از هر چیزی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/125644" target="_blank">📅 23:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125643">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رئیس شورای شهر تهران: رایگان شدن حمل‌ونقل عمومی بدون تأمین منابع مالی به توسعه آن آسیب می‌زند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/125643" target="_blank">📅 23:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125642">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🔥
آتیش زدم به مالم به خاطر عیالم  بقیه هنوز VPN حجمی میفروشن اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 190 تومن
🏷️
💥
بدون محدودیت حجم  @NetAazaadBot @NetAazaadBot</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/125642" target="_blank">📅 23:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125641">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NesGfoXKaPtEHTaIaUM__lQEdZ9aTZ6nc3k9LUTXJp4mjcgflCn50kOLDeNKQXJaSTk4tD4X2pmHNV8eUpVh23s8rIhhf2PBh8f18TU8HzceXn1sctv32nKcCPuUTx74UwjJGTFfs7StXPBURWO97hl1tWEULN6IhRHL10XiJ5QgqwhZzhvq8k-3n3FnV5i7HX6qhLUWW5iatRn29TChaEZLCS-P-QfoW6QD6Kj_Ft6YxSphZNl3rDHxz2UXDPw0QuVEAhZFLD46tIxe6lMcrsFlWxzK-6JBwLUxJkddTiKEXHrceNoL4Nati5A0tuIcMZYOd3fxGctwCB_VvIsapg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
🔥
آتیش زدم به مالم به خاطر عیالم
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 190 تومن
🏷️
💥
بدون محدودیت حجم
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/125641" target="_blank">📅 23:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125640">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ماجرا و محتوای این پست بسیار دردناک و ناراحت کننده‌اس، اگه بیماری قلبی دارین به هیچ وجه نخونین.  توی سنندج یه زن و شوهر از هم طلاق میگیرن، بعدش مَرده حضانت بچه هارو به عهده میگیره و میره یه زن دیگه میگیره. دیشب همسایه‌ها بعد از شنیدن صدای جیغ وارد این خونه…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/125640" target="_blank">📅 23:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125639">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ از اینکه حزب الله و اسرائیل حاظر به قبول آتش بس ترامپ نیست و به نبرد با همدیگر ادامه میدهند ناراحت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/125639" target="_blank">📅 23:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125638">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQ_O4w707sAaOtCzKwnTR9CfENsnoaAaAJre_YqrbTpk7V4MyiApArRE_Gk5JH8ZDIwfUoUkQhUZxoQA55jrgGyyU3hPhwUphL2kOGL7meCKMq7mZpM-JZWlqdEHqp4_H1-fnhOUBpWVFxh_l3TQzFEP5Y1np2Bz-1KSUZhyOAGwGgqnml8jO9xqo8J8p2sKihNJQekyZyNYPHowL1O73jLWFOEJ8haQ_BbUx0TJsL9YKLUvgFDp7aXOb_innlxH6pHTcTJ8qOLu9jDXMWZ3n5fRHGB8AedkNk9wNeugqkJEiOvRhMEVsJh6RHu_6iqC5pbGOadqAuuf8AlcErm_lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مونا آذر، بازیگر ایرانی و مشهور هالیوود اعلام کرد که بزودی وارد ایران میشود تا از خاک ایران حمایت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/125638" target="_blank">📅 22:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125637">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
کانال ۱۲ عبری:  افزایش تعداد سربازان و افسران اسرائیلی کشته شده از زمان آتش‌بس در لبنان به ۱۶ نفر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/125637" target="_blank">📅 22:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125636">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LL7iwEMLbl2HMCkIcFfp0xp5N73pYtDj1MOB2Pl_lz7KXghYXNSU5nfPVPPsHkbKUlDCXifGzvhGOL_-F93KbYHccd-LGbAS8dSVuSfrsFHWMi95Ku4bRPyizTubrWY1cClrfxlKDYPl4bfifVGf59r0S5Gjrbr-1RJcfe-XPP3aSe5aE5w0sESh5Bg1nQuZssYYDyrivzg-WSa0gM8GgaW66wmEG3Hh7Yt7EcEwA6EomfRc6Oz4UhAAzFXsDlxXIUkwywMu7sT91YvtJ78cr7pxBJsF9SPvEZ0YacbJYuXMIw3tjVJd4PIPispHrzOoVhB_03_WwbpBBeLVdFLh2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش صدا و سیمای جمهوری اسلامی، معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان اعلام کرد که عملیات خنثی‌سازی و انفجار کنترل‌شده مهمات منفجر نشده باقی‌مانده از جنگ اخیر امروز، ششم ژوئن، در بندرعباس آغاز شد.
🔴
عملیات پاکسازی تا سه‌شنبه، دهم ژوئن ادامه خواهد داشت و در این مدت صدای انفجار در سراسر شهر شنیده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/125636" target="_blank">📅 22:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125635">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
شاه چارلز سوم به همراه جمعی از اعضای ارشد خانواده سلطنتی بریتانیا، روز شنبه ۱۶ خردادماه در مراسم ازدواج شاهزاده پیتر فیلیپس، نوه ارشد ملکه الیزابت دوم، در جنوب غربی انگلستان شرکت کردند.
این مراسم خصوصی در کلیسای «All Saints» در منطقه کمبل برگزار شد و در آن، شاهدخت آن، مادر داماد، به همراه همسرش تیموتی لارنس حضور داشتند. همچنین  ویلیام وهسرش کیت شاهزاده و شاهزاده خانم ولز، ملکه کامیلا و دیگر اعضای خانواده سلطنتی از جمله شاهدان این مراسم بودند.
شاهزاده پیتر فیلیپس، که در حال حاضر در رتبه نوزدهم خط جانشینی تاج‌وتخت بریتانیا قرار دارد، در حوزه مدیریت ورزشی فعالیت می‌کند و نقشی رسمی در ساختار سلطنتی ندارد. همسر او، هریت اسپرلینگ، پرستار کودکان است. این ازدواج پس از پایان ازدواج قبلی فیلیپس در سال ۲۰۲۱ صورت گرفته است.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/125635" target="_blank">📅 22:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125634">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
نیویورک‌تایمز: اسرائیل مکالمات مربوط به مذاکرات آمریکا با جمهوری اسلامی رو شنود کرده.
🔴
اسرائیل تلاش‌های خود برای شنود مقام‌های ارشد آمریکایی از جمله استیو ویتکاف و البریج کولبی، معاون وزیر جنگ آمریکا، رو افزایش داده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/125634" target="_blank">📅 22:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125633">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2f81d5cd9.mp4?token=U3LPG0UHcv_T5bZZC4XHRJRUz-VXBDwrZ_N9v12RywYPjU5VAOALaqclGvF3L78UZutxgIZj33uKVizfj2XPGNPYmoUUz-grOBzA-QXdkJn9o6b18XRIVqtj7qcsPNKNhQ6RU_GI82Fq0Y3x4ftW1uFq-Obb61M9ATg-eUim91bbHGVfMkedx9j_FoE96TY0uYH8qB5aRmNmGkGc2JkDrdeNy2m7giiBwB_bbIpPSxoZGmroomEI6qgVwvEnQJPoymqhcykgiTow9r4dmpG_GQucges-78dea1G6MqW4gd7UgynA0jETLtnhN4oaY8Vs3VDiDFFlJwg8f_bBtLtLKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2f81d5cd9.mp4?token=U3LPG0UHcv_T5bZZC4XHRJRUz-VXBDwrZ_N9v12RywYPjU5VAOALaqclGvF3L78UZutxgIZj33uKVizfj2XPGNPYmoUUz-grOBzA-QXdkJn9o6b18XRIVqtj7qcsPNKNhQ6RU_GI82Fq0Y3x4ftW1uFq-Obb61M9ATg-eUim91bbHGVfMkedx9j_FoE96TY0uYH8qB5aRmNmGkGc2JkDrdeNy2m7giiBwB_bbIpPSxoZGmroomEI6qgVwvEnQJPoymqhcykgiTow9r4dmpG_GQucges-78dea1G6MqW4gd7UgynA0jETLtnhN4oaY8Vs3VDiDFFlJwg8f_bBtLtLKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پویان مختاری شروع کرد به قرآن خوندن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/125633" target="_blank">📅 22:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125632">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Co30uDJsCLKncsakHPX0crNa5hszDE9l-8sj_wSLPmEvA2W-haSaP8K4s6mqcV4GOLIkGvF03ACFbeuFHkAjAZEW75hZ4XUIscU-vboJNH-lzmc8O1mkpg6xnykL8TzLa3mh4ufPNTO1ApEKutzIrI6gpE0-3p5u0-PZD9tF_CoRKFLjm0hWAGawcz0FYi2DDjJBJh69f-1MKXgX6EBgfWVVCuV_P_drekGb_-NOcjEmftEGdY0KrFCSu5cYeiErxe3uszhX6WLqS_tNXQ_OyIm-tlUpZ4gV-816O3R3snfPSTKs4ZmAhwl4PBL0OaONk8OXoeLGP6NkxU0fBzKNZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه زوج اندونزیایی اسم بچه تازه متولد شده‌شون رو "علی خامنه‌ای" گذاشتن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/125632" target="_blank">📅 22:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125631">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFa9rcKiWbO48ML0pgkMvdOhimh81UT65FTiTHgpwB9hGsn4u-LUIwoPl9L7CxxZJV6L9ODMUXLx2c0gHqkm5H3B8jSHFTqc4ty9ZADNHP4M13psOST9m9uiJxZBNOkTekOmi2DhsD0A9wZ9L4kzxlCn7xrgiGVV8KMM_djIli2lpXmqUkkBIq1kfsu-8EZWctSrj2OB8zKeuB-eNBHGYdemKcb0JS6RzSDzQi5La0iH-p0pTuQiRCp4h4zhRU4vq6rhZhnOr_NpPgyt4iqYdrmH8ktTDPDNjSYFLotWiOsojErqYhPvF2md1Di9Wcxf6U4Hby3wHomZe0ErdyuCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇱
تو بازی دوستانه پرتغال و شیلی لیائو اینطوری بازیکن شیلی رو زد و اخراج شد
😂
😂
@AloSport</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/125631" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125630">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjkJ0kVPhS8-NZ8A7VGALAUxDYUBAkco3d3qM8T8QnN4EQMKubR5VZrhO4unWyX8qUtmHyiN44ZAnZSJ6KJrm0ylCxqqbL2cLsRa_wVeEx_MotNTZdb2Yziu2q2aCCFFZg1HI18ziWa6VLxleB_OEcHKRjG1pX3GfqNzsi47Q_uFw5D0m6NMZAnE_EVgk4LmiE-wFd0MNnfdBZXlviqGUEXNLOrKgQUFIsIACT6anIL7jLVMGjXY39rz4v_PPMEUJLTfUyey5OGhTrwYbUIMYOysedWrABoX-BD5lU1NEBB0IGLqJo4DHpz9EGRjjXCM-RgmwNh1hh1NuhfvdyUn1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خان‌یونس ، لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/125630" target="_blank">📅 22:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125629">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199e947d8b.mp4?token=K19jg-N3zJmHtiuhkHHHw59Ck-jX-0a8hVB4yVr1vMMqG0R2MySTYSKZbYDhqNITMWJb0PuXogip051DXCh5gHuKU-tQQ-r1AhaxJIFUb1HpxwgH5Bm_24FSZFqdOXqKCdJrLoZByuyvEpgNIH-CWTAhtSGKmEB-ePhgiMCPbWe9sv9NhuSMqFEuKqTmOVVZxNfOoZ7Yo_MLrUhvbbOCC8g1ucyrwgWECr0n-RaxWFRBqXJM_Jvh40ibpXY6Ocsu5fwUzsHDU7_CSyHdnZSuZWg4lMRgEDFmWhO6iWZX11nUcFu75wD0aHRZ_NSx9YrY8GvEn6jVN3In2YBGD0AEUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199e947d8b.mp4?token=K19jg-N3zJmHtiuhkHHHw59Ck-jX-0a8hVB4yVr1vMMqG0R2MySTYSKZbYDhqNITMWJb0PuXogip051DXCh5gHuKU-tQQ-r1AhaxJIFUb1HpxwgH5Bm_24FSZFqdOXqKCdJrLoZByuyvEpgNIH-CWTAhtSGKmEB-ePhgiMCPbWe9sv9NhuSMqFEuKqTmOVVZxNfOoZ7Yo_MLrUhvbbOCC8g1ucyrwgWECr0n-RaxWFRBqXJM_Jvh40ibpXY6Ocsu5fwUzsHDU7_CSyHdnZSuZWg4lMRgEDFmWhO6iWZX11nUcFu75wD0aHRZ_NSx9YrY8GvEn6jVN3In2YBGD0AEUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام مجیدرضا رهنورد ، وقتی جلوی دوربین ازش پرسيدند وصیتی داری ، گفت سر مزارم قرآن نخونید ، شادی کنید و آهنگ شاد پخش‌ کنید ؛ او یک آدم عادی نبود ، یک قهرمان و اسطوره بود...
🤔
عرزشی حرام زاده بعد تو سمت مردمت اسلحه گرفتی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/125629" target="_blank">📅 22:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125628">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbvD10uf2MoPIEDT1pabJoHVTwDdw1a5oz6sbUefYgmY8FkSnyTcBdeN6A54Ggz2oeyqWtMWdbBV8WKuPuGi1PRhE1TAmX-Fc6pc8TUIo16JoEhGk1sF9EEu7u9g4lV0BClMSta7JJNufu5oIGeesCjjF-FCzhDFgVPz__cIyy_Cle8lge7xVBO63mrq9trVLs06N-SD_9kJxb81sgBKVNstFl8V1JPEsrfYsxpeiIJIShe5E07B_eEQRgJBXPQIfjyjF_u3bGst01dNxgdqKnKRbHjRa0Be093Rrd_yHwUmIxmtXdLJVMau2wSq0UpDP4OcfSSAeUsUiVxsvftnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/125628" target="_blank">📅 22:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125627">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ادعای ایسنا: وزیر کشور پاکستان در جریان سفر به تهران حامل پیام ویژه‌ای از فیلد مارشال ژنرال عاصم منیر به سید مجتبی خامنه‌ای است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/125627" target="_blank">📅 22:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125626">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
روابط عمومی نیروی دریایی سپاه: صدای انفجار شنیده شده از اطراف جزیره خارک مربوط به خنثی‌سازی مهمات باقی‌مانده از جنگ تحمیلی سوم در منطقه بهرگان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/125626" target="_blank">📅 22:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125625">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
محمد جمالیان، عضو کمیسیون بهداشت و درمان:
🔴
بعد از اون پیامکی که برای مردم فرستاده شد کشت خشخاش تو کشور زیادتر شده!
🔴
کشت خشخاش تو یه سال 246 درصد افزایش پیدا کرده و مردم فهمیدن فروش تریاک سود آورتره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/125625" target="_blank">📅 22:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125624">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=UdL4oPL-79AhOx3MzreaoFN5jGcE3I7UOA0WDPyvtqiw1f9ZBqZsxTmO6GU9AysRE6HIc83RLCeUdJz03MaV9_vVpFcg-VvVwINh6dpmDVQE3NLoygpmuJlA2dAYLHg2CZJluMky116YEkOpAtd1SCUZcFWiBUISLQRnUpsCfM9_6YUZH7ABmi_ctRoH89LXk8fDhzX5aN7utrxP8tSGdNitG-aq1bG7fmGbV-s-Yk0xR4dbHhv35JbieAlog4ykF2zm7UlRJMBr5r4P4AJt_8FeOp8atH_2sVielCPPxOPFNIhn6FsW9XLLup0sCTUGY3-B3MBUNZYb1yC7EKewBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf1fba69e.mp4?token=UdL4oPL-79AhOx3MzreaoFN5jGcE3I7UOA0WDPyvtqiw1f9ZBqZsxTmO6GU9AysRE6HIc83RLCeUdJz03MaV9_vVpFcg-VvVwINh6dpmDVQE3NLoygpmuJlA2dAYLHg2CZJluMky116YEkOpAtd1SCUZcFWiBUISLQRnUpsCfM9_6YUZH7ABmi_ctRoH89LXk8fDhzX5aN7utrxP8tSGdNitG-aq1bG7fmGbV-s-Yk0xR4dbHhv35JbieAlog4ykF2zm7UlRJMBr5r4P4AJt_8FeOp8atH_2sVielCPPxOPFNIhn6FsW9XLLup0sCTUGY3-B3MBUNZYb1yC7EKewBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیکزاد، نایب رییس مجلس: تنگه هرمز طبق قانون مجلس به حالت قبل برنخواهد گشت/ تنگه هرمز برای ما از بمب اتم مهم‌تر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/125624" target="_blank">📅 22:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125623">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
یک سرباز اسرائیلی، بر اثر جراحات وارده در نبرد در لبنان کشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/125623" target="_blank">📅 22:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125622">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
احتمال شنیده شدن صداهای شدید انفجار به مدت ۵ روز در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/125622" target="_blank">📅 21:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125621">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
تسنیم: لحظاتی پیش صدای انفجار در جزیره خارگ شنیده شد. این صداها مربوط به خنثی سازی مهمات در منطقه نفتی بهرگان است که در جزیره شنیده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/125621" target="_blank">📅 21:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125620">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
کرملین: نتیجه عملیات نظامی در اوکراین برای واشنگتن روشن شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/125620" target="_blank">📅 21:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125619">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxLjK2iZQ4h_pax3YP2k33xeTc-zz21gskzRosbDZ3kAKUzbytZ4NFKCYomvGD5gtYOvwNzezoJl-Au32PPXpzj0mWhQTm0Wb10HtjrmUZMXRVCdpPKJWgmd9ZdFJhixWkAMZfo6ed3yEaPk48IAplf3pDL3gc9JyG03w-zUs77JohyjicyF7wJkpaTzQEpNbr-Zda4Vznyo3Ozhrvj_7AJAJOtywFof6nLGRjxBfqHSQmOPppTBtNsgglTd8WKnLvDySy5fE51zeiYBTnfO-9vt0DcM7SgSGn4M27nv_ERO7Lipik1z8OEuWJWtTjfy16LhkuZbCBD7RNvYkPhT0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال: کتابخانه باراک حسین اوباما، در ۱۰ سال، وقتی کاملاً به بلوغ رسید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/125619" target="_blank">📅 21:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125618">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cto9ya7jpHHamWl_fYDv3cK1aup7AFp7al3fvjzM_EqRhLCY4dRrnwIs0G-l9-9Y1lq9zw3zQFIiWpkWvkdQmKIYhfTzPfB9dC4x7EYnqZNXANf2uoY_kikScgNKgQg4h2beFt-X6gE0uLit7WcysnFANBJAxafm8hpRVdTlTLeMqeRFP3X6PLt1u_q-8hQkTxjYUrtsysbDe6X52did19bcEaXXpnQRR8gbDc2KzYBb0zlneRLysIQYcqmNvetOph3V75ymN_XWkBDN5hHeCadc1uoZtm2WMUhPuNKQV0WJ55T3wsB2hAGNDiyh-0AAJbK_Oda9-gIHIfq9X1rxRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حکم بازی کردن دانش آموزان معترض به مصوبه کنکور در محل تجمع
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/125618" target="_blank">📅 21:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125617">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_LAZOJM2SZqw3On8U0GOgKrloibxEAZZaBFMVamo5djQxFm05Sizwj1EsrLIRatVSw8BsNLEudbKEDxy0XkdyTNP1CIQLQCvvvfI0_sBEzCBmeCYKiqcMzCwVfVF9GyNpXd2f0UWEOFf8VN4ozuiT29_FL9ILjDBI4aBbuRpHupqehH8YUqkGq7jCmPalq-P-VJB6etN7UqKUyrl1dOZcNHNUOw1YpBPlJn2NDAYJxjJSS-tg3vd20GDxvKvT1ZEnw1t1MsACT4-0TJJhprspOw6g1EGtx0vXgiUzc78tzqZXyZBjq90tu-OFZA_tOfaNRKjDx3nXQox0gdxiHLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارزیابی‌های اخیر اطلاعاتی ایالات متحده نگرانی‌هایی را برانگیخته است که سازمان‌های اطلاعاتی اسرائیل تلاش‌های خود را برای نظارت بر مقامات آمریکایی دخیل در مذاکرات با ایران افزایش داده‌اند، که این موضوع باعث شده مقامات آمریکایی درجه تهدید ضدجاسوسی اسرائیل را از «بالا» به «بحرانی» ارتقا دهند، گزارش نیویورک تایمز.
🔴
اطلاعات اسرائیل به دنبال درک استراتژی مذاکره دولت ترامپ است، از جمله مواضع مقامات ارشد مانند استیو ویتکاف، البریج کولبی و مایکل پی. دی‌مینو چهارم.
🔴
مقامات سطح اخیر جمع‌آوری اطلاعات اسرائیل را به‌طور غیرمعمولی تهاجمی توصیف کردند.
🔴
پرسنل نظامی و اطلاعاتی آمریکایی همچنان هنگام فعالیت در یا در کنار اسرائیل از تدابیر امنیتی تقویت‌شده برای کاهش خطرات جاسوسی استفاده می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/125617" target="_blank">📅 21:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125616">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
مهر: صدای انفجار در خارگ مربوط به خنثی سازی مهمات است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/alonews/125616" target="_blank">📅 21:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125615">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
مقامات ارمنستان امروز شش نامزد از حزب مخالف ارمنستان قوی را یک روز قبل از انتخابات پارلمانی دستگیر کردند.
🔴
رسانه‌های دولتی دلیلی برای دستگیری این شش نامزد ارائه نکردند.
🔴
این حزب توسط سامول کاراپتیان، میلیاردر ارمنی-روسی رهبری می‌شود که در حال حاضر به اتهام دعوت به سرنگونی دولت تحت بازداشت خانگی قرار دارد. کاراپتیان این اتهامات را رد کرده و آن‌ها را با انگیزه‌های سیاسی توصیف می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/125615" target="_blank">📅 21:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125614">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fa8198822.mp4?token=D2FQmn9HfU86370W-HJ8bEMpW1M1dVcszTb0B0CNAg282U1pMwJerjMV3gfJ8M310PXh5vxl_hMThQqSqr5nrT_UCxSz2F957gD0Vfly2hGqBr9FJTD4w9PBfGPcAhILPiTowH8VB32_aPasO0zztCVn_24E5a0zcAxKYEda-yejgP7wBloJfjZ7Sw8H5chNYLDqe72h2Abu8390mUT2MAO9y1z2MaMPfRfd0oI-onBTXIck9R2SARBM4tyRgyjdBesMhAljdE9hld6UM1ONHb68dMsRllI9BMicWsduoK9uu8hoBbY0SXsG7gFLLynLS0Uq3nN4JL5dYekI2gO3HDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fa8198822.mp4?token=D2FQmn9HfU86370W-HJ8bEMpW1M1dVcszTb0B0CNAg282U1pMwJerjMV3gfJ8M310PXh5vxl_hMThQqSqr5nrT_UCxSz2F957gD0Vfly2hGqBr9FJTD4w9PBfGPcAhILPiTowH8VB32_aPasO0zztCVn_24E5a0zcAxKYEda-yejgP7wBloJfjZ7Sw8H5chNYLDqe72h2Abu8390mUT2MAO9y1z2MaMPfRfd0oI-onBTXIck9R2SARBM4tyRgyjdBesMhAljdE9hld6UM1ONHb68dMsRllI9BMicWsduoK9uu8hoBbY0SXsG7gFLLynLS0Uq3nN4JL5dYekI2gO3HDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مردم فیروزآباد قرآن هایشان را در آب ریختند!
🤔
عرزشی حرام زاده وقتی دین رو بازیچه قرار میدید و دروغ تحویل مردم میدید نتیجش میشه همین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/125614" target="_blank">📅 21:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125613">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJuSwTK7kvhGi7N9PgICW0jkvdnxBsEkmCI_CSq47wlQ8KqCfwepOES97xAh6AffkVC1LxRt69aDZBAXdpQ-hEfARI1g6tRQ9tdKQleioxHjdxkQThF9DVQ8DNRTXvccI1dsxzichmo7Kniceu5KOWKD9LiYR5CXhLiBrsl0TDz2DvB5Bs9XGpQPDDHfpwfD2lnXP06omwxzkOuyMp9_ahhVR13U3j8caJXo2pmAF2GKPpEJiNt3kVTFg7hIMa2aLDJlIsLath23CfHBxYVaNIBIwtNOwFVLP7O6CfV4XPsK5nznL4sqa3pe-lQDKhSDu5QgCQgCyDByELpRN5uUKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن پست: سریرام کریشنان به مقامات دولت ایالات متحده اطلاع داده که قصد دارد سمت خود را به عنوان مشاور ارشد سیاست‌گذاری هوش مصنوعی کاخ سفید ترک کند تا یک نهاد خارجی که بر سیاست‌های فناوری تاثیر خواهد گذاشت، تأسیس کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/125613" target="_blank">📅 21:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125612">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oibXd9pyB-d8fFNFwbPA1fjN935qMDO26VlGc1UHSjy6Hl1NAZ0Hg1VsQJZ5Rl9autNbOlrHvjqToru7HCcHMBPwmq0IstdRJ7nefaveQUuHHKkj_D1li-pHq8LjHMG09xEq7EarCkQ3XoOWUlU4NMAAEW2pnuNb9qAeMfgZL2wtky9kjD803ute_oyYhuhxY5BkK2KPvBuv-YO_PqUuu7NNj0z-vACrQQ4As1xSLUBhWumii1zXshUwvOraqSFYZVAupwYRB5pK_QFzW9jWptbZfWm-J-_1Tws4BLnbFYULOdeuYaWs23lFrS1J9sm6850CC1zRtr745ly2iiKZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار وزرای کشور ایران و پاکستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/125612" target="_blank">📅 21:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125611">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e82f3909.mp4?token=iwCzCDPCWmh-L-l8tYk8I4iO_F8rRExIeYqFX6rEMwe7nv2jlL0gOtnKpXttOzR9gxMTY4RStWdoGk6-wmmaewCwjHcmGKqVBucqLgOd4nQ_PyAAK8I3ZsjIXN4U2SPVsmAY5E45rkipnP_rfYGuAKRzkuxSByQeW2a_Gj7ppotUtM9CEXWGz5xWd3WVr2I_5JMiqwy-wTOxO5F-gR6fRMP-veljwkQZwF8u23__Vvd85BD33vwlX6jc-OSUqVIQ4KjzhToNM9xihitjh513LcPAbipLIMdJsUDJmbDFipUTevfhvk-yH7fTmwRW12fCc5ur7z0dbD8gCqortMISiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e82f3909.mp4?token=iwCzCDPCWmh-L-l8tYk8I4iO_F8rRExIeYqFX6rEMwe7nv2jlL0gOtnKpXttOzR9gxMTY4RStWdoGk6-wmmaewCwjHcmGKqVBucqLgOd4nQ_PyAAK8I3ZsjIXN4U2SPVsmAY5E45rkipnP_rfYGuAKRzkuxSByQeW2a_Gj7ppotUtM9CEXWGz5xWd3WVr2I_5JMiqwy-wTOxO5F-gR6fRMP-veljwkQZwF8u23__Vvd85BD33vwlX6jc-OSUqVIQ4KjzhToNM9xihitjh513LcPAbipLIMdJsUDJmbDFipUTevfhvk-yH7fTmwRW12fCc5ur7z0dbD8gCqortMISiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران سنگین منطقه وادی برغاز در جنوب لبنان توسط جنگنده‌های اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/125611" target="_blank">📅 21:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125610">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نیویورک‌تایمز: نگرانی آمریکا از جاسوسی اسرائیل از مذاکرات تهران و واشنگتن
🔴
گزارش‌های اخیر اطلاعاتی آمریکا نگرانی‌هایی را درباره جاسوسی سازمان‌های جاسوسی اسرائیل از مذاکره‌کنندگان آمریکایی که روی توافق صلح با ایران کار می‌کنند، ایجاد کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/125610" target="_blank">📅 21:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125609">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
نیکزاد؛ نایب رئیس مجلس: همه آرزو داریم هرچه زودتر دست مجتبی خامنه ای رو ببوسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/125609" target="_blank">📅 20:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125608">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نیویورک‌تایمز: نگرانی آمریکا از جاسوسی اسرائیل از مذاکرات تهران و واشنگتن
🔴
گزارش‌های اخیر اطلاعاتی آمریکا نگرانی‌هایی را درباره جاسوسی سازمان‌های جاسوسی اسرائیل از مذاکره‌کنندگان آمریکایی که روی توافق صلح با ایران کار می‌کنند، ایجاد کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/125608" target="_blank">📅 20:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125607">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRI-ID9_O7clmjBDmmQUa2DhmEOeduDBxfvFjxTcjYuTI3eGCjNbgdf__x4Bk7vgSAtLP406TRbB6ss3tSahlxhvvBvP06GtqGeTCD5S-5lCmTmSNAT9WuzFobPReaUC0MXv_X0sUqzUMaVvmDpRhixo8bmZniNdEf4lPjhosp1jfjrdYTepa4YmbrSgS7LmaLavazeoH4p9yefmCF2A5p9JacF4IrJogGqVaK1wveypll8DoF0ZYwiwAfUcEKr7oWCmBsm1q9xQUlKtmfXWLFtvi-aYFHovAh5pkT47Nl1eYoEsmmR7T_7kew6kzxjtNsxUipkF09maZDRcBUTIBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اختلال شدید GPS روی قطر
🇶🇦
، بحرین
🇧🇭
و عمان
🇴🇲
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/125607" target="_blank">📅 20:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125606">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW3D6YnKe9smVgW_POgn9fvvZFzhmgoTf4PIZ6RyROfJ54UfCejEw7Wi3kU-zI1_P0rtxn2cHQSL7AmmG3sDGxRezKkUDVOpeSFFjUT6YoEzozYhnaYnF9E61v7LRsuARdOyrF34vRorDBixtK_lJD3G3zxsXh7IEIoQUSMar9Uxw1-d82RfcqQfhE9eZw7yDdXqJcobsGqwpvsw1pdLwn7WKoB9UbHq1Kz4n9Q-XuNqz0QaNXRcb84yj12lzIXCag6bhCHi_1epkkYuZ2cwvUuR0s2-CezWEtPW2Fz-oDMSNCy5eBYDHw1iV1UyUwu1Cjct0m26Y7u2C7rlWy3YBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / یه مقام کاخ سفید/پنتاگون، از تل‌آویوِ اسرائیل رفت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/125606" target="_blank">📅 20:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125605">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
هم اکنون ایجاد اختلال شدید GPS در سراسر خلیج فارس‌ و تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/125605" target="_blank">📅 20:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125604">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
هاآرتص: یک منبع در نیروهای یونیفیل گفت که ارتش اسرائیل پس از اعلام آتش‌بس دو روز پیش، عملیات تخریب روستاها در جنوب لبنان را متوقف کرده است.
🔴
به گفته این منبع، آخرین باری که نیروهای اسرائیلی در حال تخریب روستاها در جنوب لبنان مشاهده شدند، روز چهارشنبه و پیش از بیانیه مشترک ایالات متحده، اسرائیل و لبنان بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/125604" target="_blank">📅 20:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125603">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6ab06f5a.mp4?token=T5AoG0jYCE7M1aXwjsIDNBdglzGSqlN7TjSJdNXkoN1IIj7D6nhFaFHbwFnz2mxAAoeNe3hc6D_tK5l4nRMWXWWjE3T9nS_HLg1tKJGloOR0rXSTazRJtd-_yr7cP_ULdS3ZkdD0fwTyXF0mevo85LLu6O490vvcKXnsC4YXFu0oNzvLU0yGAxBZTWUgqQHGqboasAkI2VD4IwJoy9qWeY5CNGl667VCvAEYyYIvpSsTJB6L8cWY6lAQDXQFqGptamQlc_IsSV_vFw8FLE5y2NRSjbnEMsmW4soMQRiWUqgm90E3uyhA9-LPQyde40440zHIsHjylV4NKBGgziSJlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6ab06f5a.mp4?token=T5AoG0jYCE7M1aXwjsIDNBdglzGSqlN7TjSJdNXkoN1IIj7D6nhFaFHbwFnz2mxAAoeNe3hc6D_tK5l4nRMWXWWjE3T9nS_HLg1tKJGloOR0rXSTazRJtd-_yr7cP_ULdS3ZkdD0fwTyXF0mevo85LLu6O490vvcKXnsC4YXFu0oNzvLU0yGAxBZTWUgqQHGqboasAkI2VD4IwJoy9qWeY5CNGl667VCvAEYyYIvpSsTJB6L8cWY6lAQDXQFqGptamQlc_IsSV_vFw8FLE5y2NRSjbnEMsmW4soMQRiWUqgm90E3uyhA9-LPQyde40440zHIsHjylV4NKBGgziSJlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی به اطراف القطرانی، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/125603" target="_blank">📅 20:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125602">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزیر کشور پاکستان لحظاتی قبل وارد تهران شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/125602" target="_blank">📅 20:18 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
