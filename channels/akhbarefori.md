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
<img src="https://cdn4.telesco.pe/file/Zeyo_gw63NrJL-D2cnB-jjsLj0E_jYIiqwWYjV1n2lYABGDW4rHIMGYl9qsKaEcqQ_25sGlbMBvx0oVl5lpN70s3vg4bJrW2XNS4vk5wOYYo28qhH9mPx8JqkKchdvmZiF82rL1QzTpnDB-ISjmLBWEklv-DTHowhV-boUEo9VoDV6gq9n_ONI15HgudInbpRALQT3Aa9W8RV0hu3cUx8alCePVOphzIcPCMVK42ppU4Rss0V-MD5MCCFRu-lg2fYiOTbHnbTZS5MZAxHs6yuL2NFk-Ab7mysuOHa7dejp0NFyWjJxC2CzsEgzmljgxNGLN35Q0R1VYiWyORMqNVEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 21:14:03</div>
<hr>

<div class="tg-post" id="msg-671852">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22723d50a1.mp4?token=ody20qtGnSGBMbwr6DbgW7K_J5J5ShLNnDED0pMlauBx9CnOymu4aZwD_wyJnuYVT0o7m201k5sCceC8Wt1v0HkUgThdsXQp9LZG75mjSTVNqG9XyH1EiTyc71ChEiYZ-Yt4oCgaWgI4m7Isc3Cmyo-wV1_H2bB6Xo9uHK_qudwwGjGFP8uHHKY3MT3u7iFx3rMIC2GYOaKnFqa-yQVa2VH4kW7E4kMEnqISWX5b-JpDMkoQNNTMvIXUT_xrEuR5FGrKvtuxEaNHrXcAvu15CWbvCGN8ViBpGUNI-5ieqxvytaWoMBS5pb_kSw_f4bai5mig6jRyp1XsUbeAr-tRsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22723d50a1.mp4?token=ody20qtGnSGBMbwr6DbgW7K_J5J5ShLNnDED0pMlauBx9CnOymu4aZwD_wyJnuYVT0o7m201k5sCceC8Wt1v0HkUgThdsXQp9LZG75mjSTVNqG9XyH1EiTyc71ChEiYZ-Yt4oCgaWgI4m7Isc3Cmyo-wV1_H2bB6Xo9uHK_qudwwGjGFP8uHHKY3MT3u7iFx3rMIC2GYOaKnFqa-yQVa2VH4kW7E4kMEnqISWX5b-JpDMkoQNNTMvIXUT_xrEuR5FGrKvtuxEaNHrXcAvu15CWbvCGN8ViBpGUNI-5ieqxvytaWoMBS5pb_kSw_f4bai5mig6jRyp1XsUbeAr-tRsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای نشان می‌دهند که ایران به هتل کراون پلازا در شهر دقم عمان حمله کرده است
🔹
این هتل به طور انحصاری محل اقامت نیروهای آمریکایی است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/akhbarefori/671852" target="_blank">📅 21:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671851">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU_yYlPPIKxbLiTFCBnBfrHRYuCoPZzo3BoOm1oP1LntamvnaaS8vCfvCFv3ILHy-gX_w_JGNwc-FTirWEgsTAjdYlYQan3qVAsD4GMEPjg_4u9nj3J0jPS3dvIfv_uzlQzotjJoyBy_6L6FDLdenvZ1g0Wq18Blfr0ppyEjwG1PSXlJzJjMrEHmUfTqvNZ2T3bhl4MXar4L7QW_wsg-D52ieXm9WXmtYN1k2JPeq3tOaLjuYkM8L3t_kzVOHrVzOQUCAhi_7qbDMdfXlXpDQ49KKCzXQ0_si2T0yOVFWHB9eIIkImtP0yRzNdCHRutL43WAyu7Vj8tEzI3X0lKKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی فیلم: علفزار (۱۴۰۰)
🔹
ژانر: درام اجتماعی، جنایی، معمایی
🔹
خلاصه: اگر به فیلم‌های اجتماعیِ پرتعلیق علاقه دارید، «علفزار» را از دست ندهید. این فیلم به کارگردانی کاظم دانشی، داستان بازپرسی را روایت می‌کند که در جریان رسیدگی به پرونده‌ای پیچیده، میان…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/671851" target="_blank">📅 21:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671850">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
حضور یک تروریست در فینال جام‌جهانی
🔹
کاخ سفید دقایقی پیش با انتشار اطلاعیه‌ای اعلام کرد ترامپ، رئیس دولت تروریستی آمریکا در فینال جام جهانی فوتبال شرکت خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/671850" target="_blank">📅 21:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671849">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGkJOWD3zPOxNnzBHzG9YdxmV1nLEjO-nH7skel9ZPIt3_yXISl9L-n2HTadzay6VWbXekFUyda48OHT17Y6FaMMrjSVG5QdPi4ny7x_gyRL9wu2iFZZVRurPjovkGjDypb3L2K4lonC24OTgIvZmgZ8_xlmNp9SlndgEmvzkXNicXnEM1Q4LpWkyCxAxJgBP-U2clDsgC17rcxbO2htDTJ-kUwgceTxJRw58G-RTkDpiK506ajsW9YppegCUlY76ENU-5TKkviswuc4vyoYvXtM9YABmT3mMUaDuM0SJpu8s3wbVAqTu6Af6cAq-ztS_zGL9H-LMRGEMyXnAa55WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
متن زیبایی که بالای سر یک کودک سرطانی در بیمارستان بقایی اهواز نصب شده
🔹
علی معرف
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/671849" target="_blank">📅 21:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671847">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f0f88d2e.mp4?token=XXge4Jk6wzQBaTV2AUJ8PGYy-lh8CqokkvtxPlJFGLX0TrpiClDZg3OGSMvhbRtLop6oFH0bwPDdxajJ2qyE9DkISTCPeLBvAcziuQCiLUTxxz2nmdh3jt4UlVjaTTNgVgWG18Cx2eRqrzeUPFGsCB-JA1ZDlusCJRlpQbq79V7xZ--Gteg6r5YHn_3twnTVG6nS4j7uXIYaLCOXCAb56l7hTxH0VDDKkzRlCkHC7FfEf95B3cCA9k0eouq-C1MZX9YAy80dVi2tPRMWTQqKPXu18Lpm7S7Kjwag_nkRyTGVtaCbRa8EWE7g842SOfYGjRxjn7xjNUwFj6Te7TjmLZcxqU60HoDmBzNsoNA-fnGCE05yZKkkQ9YJG4Ggh9F4SSdTlkZUGmJtZbLaQckZ-MboWrJBGaiYYS3hr4J2hAIIN2G4vELUukYw8AQxk_gDRMfPA0ADjFw5zFsogdj-QSIfJq8gN0wEB5M-nin-oYpZR2V2Q4V42gmnDk9iN1Eg2vLXKlXOz44-t4Y8e9CC5g6CF73wnebJaQxLbkjWPvCtC_XPHCa6uzVK-iaULKtDwp-ytOOHPmT90Aq54SIV6b8JSB20k9UT2jR2YNkmxANoeEiIuAIh7ni6C4eyorSH9YF4ssM6eDQTL-ISjjj_ofrBER_GVMmypxtaa0qRUig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f0f88d2e.mp4?token=XXge4Jk6wzQBaTV2AUJ8PGYy-lh8CqokkvtxPlJFGLX0TrpiClDZg3OGSMvhbRtLop6oFH0bwPDdxajJ2qyE9DkISTCPeLBvAcziuQCiLUTxxz2nmdh3jt4UlVjaTTNgVgWG18Cx2eRqrzeUPFGsCB-JA1ZDlusCJRlpQbq79V7xZ--Gteg6r5YHn_3twnTVG6nS4j7uXIYaLCOXCAb56l7hTxH0VDDKkzRlCkHC7FfEf95B3cCA9k0eouq-C1MZX9YAy80dVi2tPRMWTQqKPXu18Lpm7S7Kjwag_nkRyTGVtaCbRa8EWE7g842SOfYGjRxjn7xjNUwFj6Te7TjmLZcxqU60HoDmBzNsoNA-fnGCE05yZKkkQ9YJG4Ggh9F4SSdTlkZUGmJtZbLaQckZ-MboWrJBGaiYYS3hr4J2hAIIN2G4vELUukYw8AQxk_gDRMfPA0ADjFw5zFsogdj-QSIfJq8gN0wEB5M-nin-oYpZR2V2Q4V42gmnDk9iN1Eg2vLXKlXOz44-t4Y8e9CC5g6CF73wnebJaQxLbkjWPvCtC_XPHCa6uzVK-iaULKtDwp-ytOOHPmT90Aq54SIV6b8JSB20k9UT2jR2YNkmxANoeEiIuAIh7ni6C4eyorSH9YF4ssM6eDQTL-ISjjj_ofrBER_GVMmypxtaa0qRUig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حاوی تصاویر تقریبا دلخراش
‼️
♦️
امروز ظهر در خیابان ولیعصر تهران، یک اتوبوس تندرو BRT بدون راننده و مسافر به دلایل نامعلومی شروع به حرکت کرد
🔹
این اتوبوس در مسیر سرپایینی قرار میگیره و با ۶ موتور سیکلت و ۲ ماشین سواری تصادف میکنه که نهایتا ۶ نفر مصدوم میشن...
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/671847" target="_blank">📅 20:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671846">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
حمله به بهبهان تکذیب شد
فرماندار بهبهان:
🔹
ستون دود سیاه مشاهده شده در آسمان  بهبهان مربوط به سوزاندن ضایعات لاستیک و زباله در اطراف شهر است. مورد امنیتی یا اصابت صورت نگرفته است. شهروندان اخبار را تنها از مراجع رسمی دنبال کنند و به شایعات توجهی نداشته باشند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/671846" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671845">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون آموزش: اگر تهدیدی صورت گیرد، امتحانات نهایی آن استان یا کل کشور لغو می‌شود
وحید کنعانی‌کلور، عضو کمیسیون آموزش، تحقیقات و فناوری مجلس در
#گفتگو
با خبرفوری:
🔹
تا الان هیچ تصمیمی برای لغو امتحانات نهایی سایر استان‌ها گرفته نشده و امکان آن خیلی کم است، مگر اینکه تهدیدی صورت بگیرد که امتحانات آن استان یا کل کشور لغو شود. برای جایگزینی امتحانات لغو شده استان‌های جنوبی بعد از بحران حملات، تصمیم‌گیری می‌شود.
🔹
بخش زیادی از بحث مثبت شدن معدل یازدهم در کنکور ۱۴۰۶ حل شده و مورد خاصی وجود ندارد و اجرا می‌شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/671845" target="_blank">📅 20:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671844">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سفارت آمریکا در عراق هشدار آماده باش صادر کرد
🔹
سفارت آمریکا در عراق در پی حملات پهپادی در اربیل، به شهروندان آمریکایی مقیم عراق توصیه شده است که در وضعیت آماده‌باش کامل و هوشیاری بالا قرار داشته باشند.
🔹
در این بیانیه هشدار داده شده است که احتمال ایجاد اختلال ناگهانی در سفرهای هوایی و بسته‌شدن موقت حریم هوایی منطقه وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/671844" target="_blank">📅 20:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671843">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGySAFH5IWc8xNfaHwbmJrqUzjhSunA-uiQYChwV_bDF4Zz09ltHpA2i1kzldk321bAGRJsxUZFnCnH5jWq2iWMP14oLkTzkvheCmRS21Y7k7q1ClWK7fJqxq4Xvrm5IbOWH1M22sDYnSqsHljHfF3JN4zvevxpaueyRiHJcCWfcoLJlJ_EzfLPsUM0zHIyZZYwbVYHPZS27KaPRv6Z9C8DhVtadfsRRl0VteJC596ndB1ipezF1MXxGI5oTViknEUIwndwRUIZaDtI7pUQoFWR4uWt_0up1x4Y3k6XSOJRjtSDmVURfaOskcsRkcV5LHH2pfJaZ3T2_aKdsZvZY9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سایپا محصولاتش را گران کرد!
🔹
شرکت سایپا امروز به صورت رسمی قیمت محصولاتش را ۲۱ درصد گران کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/671843" target="_blank">📅 20:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671842">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96a114eacf.mp4?token=c-cre-P_msnD4V1MhYXrBT_jHICQGy0n2d2L7frRGi23Q-VTz_DymxTBLv7tvqi0FsppqEK2Qd2-b8uY1DRMxpI3Rrw1w9B1uSZi94yahzuc8WAYltECuRaXa2KN1Y91FFXJDzf6w-wVoS6JqATCoYAvUhel0SDu-clQdwdH64TBg_l1AfDvgSXDiu3BheRyia8XCktTNS6MGvyvUalAY_-eOG4usBJypxMSa-K8kySc4oj6fQZGhIN2XYsmzl7N3a0Kos9Yl6S4lTtbXhHWrSRN542hTZKGHioRkubA8HvyX8CyDHN4HSBP7S-qhoRL2wTOC0wvm3d-QvMMfiO8aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96a114eacf.mp4?token=c-cre-P_msnD4V1MhYXrBT_jHICQGy0n2d2L7frRGi23Q-VTz_DymxTBLv7tvqi0FsppqEK2Qd2-b8uY1DRMxpI3Rrw1w9B1uSZi94yahzuc8WAYltECuRaXa2KN1Y91FFXJDzf6w-wVoS6JqATCoYAvUhel0SDu-clQdwdH64TBg_l1AfDvgSXDiu3BheRyia8XCktTNS6MGvyvUalAY_-eOG4usBJypxMSa-K8kySc4oj6fQZGhIN2XYsmzl7N3a0Kos9Yl6S4lTtbXhHWrSRN542hTZKGHioRkubA8HvyX8CyDHN4HSBP7S-qhoRL2wTOC0wvm3d-QvMMfiO8aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شواهد جدید از کمک امارات و کویت در حملات به ایران
🔹
انتشار ویدئویی از یک حملهٔ پهپادی در بندرعباس، بار دیگر نقش امارات در تجاوز نظامی علیه ایران را آشکار کرد.
🔹
در این تصاویر، یک فروند پهپاد از خانوادهٔ Yabhon ساخت امارات در حال پرواز بر فراز منطقه دیده می‌شود که نیروهای مستقر در محل با سلاح‌های سبک به سمت آن تیراندازی می‌کنند.
🔹
این تصاویر در حالی منتشر شده که بررسی‌ها، هویت پهپاد را تأیید کرده و نشان می‌دهد ابوظبی، برخلاف ادعاهای بی‌طرفی، در حملات علیه ایران نقش عملیاتی داشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/671842" target="_blank">📅 20:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671841">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
قطر: ما گزارش‌های رسانه‌ای اسرائیلی را که ادعا می‌کنند ما با مشارکت در یک عملیات نظامی علیه ایران موافقت کرده‌ایم، رد می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/671841" target="_blank">📅 20:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671840">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DslhzoPQQw36zUGnNwFoP8S3DgsPO_iVMISuLL9xrUaC6sNResiNvr_UQNIOxwbrtRzWJXO3J65HawBSisDM1jOueMtzZquasQAeLngKrC1ciEmp-5z-GzAiobrFzJ8vDe4ohYQ3pbDRT4mtXm-gMPEeXLuWypIu98zsRvYsbdG9uzX7hI4O0DglKJevHuPKTcneL8R3k4FQzZckPQspiT4neRq0IDoJK7MtsDsUezvaeo9HFHITsHIdlPpoF2CmjEQ3f7Bnj5GntMKL9SSYQ-h2doJwHZIqoKpAKjfXkvme-fzsSDbBNwxWWlqwDcgaidUSuGgIEuMfFYhuGr92MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشاور محسن رضایی: تصمیم مهمی در تهران اتخاذ شده است؛ اگر حکومت جولانی بنا به درخواست ترامپ و فشار آمریکا دست به اقدام علیه حزب‌الله بزند، با حملات موشکی و پهپادی مستقیم ایران مواجه خواهد شد. این هشدار به جولانی داده شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/671840" target="_blank">📅 20:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671839">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
وال استریت ژورنال: آمریکا در پیامی رادیویی برای کشتی‌ها اعلام کرد «مسیر جنوبی تنگه باز است»؛ یک ملوان از طریق بی‌سیم گفت «گمشو»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/671839" target="_blank">📅 20:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671838">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddQykGpyjBJoLiAo7lrGZHLpLg0qLfvIPzzCzPUWtFt8dzvjNw9ybbWmPh6q--flut0Usc7s01RSuGC2CR38HmVi5ooqNyB75ygLyICwZhPz9uEb42H6q4tv44byEhyNHlCPL4ha7xANEyKZLU7AU2ATBVnBNc4s3ZRHdGVSewvz9l0voDibvC50N2BXdJWSvsjEBRL6ea9SDXTuR4N9ycvaxvxGsQ6RxLaoIlEckoS3sv_3mLPApQnFF9w40eWhRA6OXHehBbN-n2ep9pMhI_r4kQh3hcqjJ6R1qWBfvB-e04telAf7yS28kWLOVdN4mxLZoeSKTq7IryZtMPU09A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای نشان می‌دهند که ایران به هتل کراون پلازا در شهر دقم عمان حمله کرده است
🔹
این هتل به طور انحصاری محل اقامت نیروهای آمریکایی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/671838" target="_blank">📅 20:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671837">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO8dpAI9yHEDuLBCoXkYVqJr9IyfwacrKMfQJkYm4FB3rMugnhXpbn7TzH2YwwOKKN8cMFYlz6nMmdhn-j2JpWSuc_1r2d9kT4eOGMEs3gvb_lXE2ZkFAmtJRfQUmZWjgPtSIbZXPspRrQmS-UqdJrVJjzj5uGlOvUi071JbYqL_6IrIHMRT_fw3JDcAW6LWNihr2oha_30KuemzF-r-b0z7du7SprTHewUIA0SSgOCTJDgOOCORjtdl3muqJyEJa7WhT5XkWMgN2jVkwnggvxYiVBB84NCfvVcB2hczw7tStsozmfx5X1f63G_ePqndYW6IS42MAHaQhpNofYwvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان ست چهارم
🔹
ایران ۲ - ۲  آلمان
🇮🇷
۲۵ | ۲۶ | ۱۸ | ۲۵
🇩🇪
۲۲ | ۲۸ | ۲۵ | ۲۰
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/671837" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671836">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
روایت تکان‌دهنده مردی که پس از مرگ، فرصت دوباره از خدا خواست
🔹
00:09:00 توانایی ادراک همه‌ جانبه افراد پیش رو و پشت سر در صف انتظار
🔹
00:15:50 سفر به سه فصل مهم از تاریخ بشریت
🔹
00:28:20 خواندن خداوند با چهار اسم اعظم، برای طلبِ نجات
🔹
00:37:35 بازگشت به دنیای زمینی با حالت سجده اجباری
🔹
00:50:30 تغییرات رفتاری تجربه‌گر بعد از تجربه
🔹
00:56:20 علت تبدیل خیاط‌خانه‌ کوچک به قصری باشکوه و عبادتگاهی والا
🔹
00:59:20 به میزان دوری از نفسانیت به روحانیت نزدیک می‌شویم
🔹
01:05:10 کوچکی دنیا نسبت به عظمت آسمان اول
🔹
قسمت سوم (صبح غیرت)، فصل پنجم
🔹
#تجربه‌گر
: فرهاد یزدان‌ستا
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/671836" target="_blank">📅 20:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671835">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae6595c4c.mp4?token=BGKCL5Xipg3bj5aXmBrpyZ70JuiTdrdYI1a43QuoL6B-1Mebbtbiy8L9XJPfVycDdWHy6ZOlhGmeLY1VB1zx6vxWzkPlGw-TrYZM8XXVHZ9EuYZhh8uFq0-y7AZOT9-XXunuU4_5AmO7KSHGgP3NxjbQr-wqCXRhb-KhwsFqQ3FCh4VxMRdaaefap6ZGNlnvEZBJEw2aK7LPx7QrMKe2Os5JtGrR-T6NCnM_3sNSOR7w-ciceNbRDkq0-d1b0ORr4ov4_xtfjlSF_HW1DbJ-GNnoxsoK8S2BKhEjnE3Oi1Y7AV5wEklWiscYgM09Np40Xf-eVs5kvNFW5V0PzGEing" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae6595c4c.mp4?token=BGKCL5Xipg3bj5aXmBrpyZ70JuiTdrdYI1a43QuoL6B-1Mebbtbiy8L9XJPfVycDdWHy6ZOlhGmeLY1VB1zx6vxWzkPlGw-TrYZM8XXVHZ9EuYZhh8uFq0-y7AZOT9-XXunuU4_5AmO7KSHGgP3NxjbQr-wqCXRhb-KhwsFqQ3FCh4VxMRdaaefap6ZGNlnvEZBJEw2aK7LPx7QrMKe2Os5JtGrR-T6NCnM_3sNSOR7w-ciceNbRDkq0-d1b0ORr4ov4_xtfjlSF_HW1DbJ-GNnoxsoK8S2BKhEjnE3Oi1Y7AV5wEklWiscYgM09Np40Xf-eVs5kvNFW5V0PzGEing" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جام‌جهانی زیر چتری از دود
🔹
در فاصلهٔ چند روز تا فینال جام جهانی، آلودگی هوای ناشی از دود آتش‌سوزی‌های کانادا نگرانی‌هایی ایجاد کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/671835" target="_blank">📅 20:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671834">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hx0gloHCQsrcIaCVoPIMxNsy0Bbdl2OZWKMkCYVtNzp5PEZ9XUkL5-bFq-Xt4aifEJVzcxiPQE51PnEu0dMoqQQSvn1Z82pPnlQXckFhCiKGUvPOEh9Y10oF1BP7x8cFy2sWza6E9QifhIPvZJUr5FfebbV9RFmzzAmlrm7j15UC6uEb3W150yfcy1xHFpYQSOW_4Qv2iD_ohLeZn2-Cb5zxzGpwLyZeTNI3cY5z1UlcNCI-5doDsd8d7uETgHGhSyCkmooLejtb8NQrRlIsFhSuurBrqNXInaH170s0id8HFWa0oDfzpAu4bDzkwGiwRt6VLJYe5-gjTlv-LNmMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای دولت دبی: گزارش رویترز درباره وقوع انفجار صحت ندارد  دفتر رسانه‌ای دولت دبی:
🔹
هیچ‌گونه انفجاری در مرکز این شهر رخ نداده و اوضاع کاملاً عادی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/671834" target="_blank">📅 20:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671833">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
رویترز: صدای انفجارهایی قوی در مرکز شهر دبی شنیده شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/671833" target="_blank">📅 20:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671831">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ma8vsR_9Fv1LHjPNM5muTuwAqI8l4fXJqzjEJIVL81S6gWbeQC8pfMZlU66YMGFgDQFzMmT2lW-LVsXp9-KRsN0N2Iz2YKsx6fDWtCuc7IFw5tx0u1vW8mGxn_lZ0c5H1wNoBxHo3G1gd-T0D2zt7hCPvss2oBIGGPw0oBMapK_u0EuYsJRynxuJ8H51l7rJGMGxJ6mmXlaRQx6RjXQeUhf_DGlOLDXrAAyyUIivUHJ9xJqlESCRHk97IQuoOKndii4JTKjB9AfFziBoGXkSiCscrwy754YsShYQboJVaFeEIGhg5fgenQaMIZ9tvvor-LZ355oOysInyyM-QCHWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه‌های اجتماعی در حفاظت از کودکان و نوجوانان شکست خوردند
🔹
شبکه‌های اجتماعی برای محافظت از کودکان و نوجوانان، ابزارهایی مانند محدودیت پیام، کنترل محتوا و تنظیمات ایمنی ارائه کرده‌اند؛ اما بررسی‌ها نشان می‌دهد بیش از نیمی از این قابلیت‌ها در عمل مطابق وعده‌ها عمل نمی‌کنند.
🔹
از ۸۶ قابلیت ایمنی بررسی‌شده در تیک‌تاک، اینستاگرام، یوتیوب و اسنپ‌چت، فقط ۳۵ قابلیت موفق بوده‌اند.
🔹
اسنپ‌چت با نرخ شکست ۷۳٪ ضعیف‌ترین عملکرد را داشته و پس از آن اینستاگرام (۶۶٪)، یوتیوب (۵۵٪) و تیک‌تاک (۵۰٪) قرار گرفته‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/671831" target="_blank">📅 20:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671830">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مقام نظامی یمن: اسرائیل برای رهگیری حملات تلافی‌جویانه یمن به کمک عربستان آمد
🔹
نیروگاه تبریز هفته آینده به مدار بازمی‌گردد
🔹
آیت‌الله جوادی آملی: وظیفه همگان، حفظ وحدت، حمایت از رهبری و صیانت از نظام اسلامی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/671830" target="_blank">📅 20:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671829">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
رویترز: صدای انفجارهایی قوی در مرکز شهر دبی شنیده شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/671829" target="_blank">📅 20:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671827">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ER_OJjx50U9ORXO3bDb9FXBmwIeG8UmJlFRduHso635pPbaJmDI9uZU3GWvGekMFy052qOpT9un8y0VoxZ6oZgHifcn1JW9xbHgH_lvFm4SgjMAG0nPG_FMTgYyYDSDgBZRQl79j75NNdxOkzEAS29Q9EQPK4joOGg2TXvrs-KGhsSDSu5RPVhbiBB66x6sdF-zb9iSQvDPqaUfMA14IUUsEL6s1pX8HZH6_80MylBkhYcV7zEZu2SNMKjs_QlCUhliOVipjRZtuLjqmId97B_dgQeCnJ2wXl3kEjFb6SM6j38gYPJu_lSuP5i-iVmiYhF-H_s7LIOkXPZ9vx92qsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MUXQ601AT8mkixGj0DXkBIAyudy_nx2KSpbSdUHJABt4AB2kDbYZC0TI-luEsWlPXXJwq_HUwq_x6tc-BgSWan95sCYLnrqwP53qzIzXMTswPn-q-GeKugBfxQnrnEAGR10nMCaCpnh_jqZIZULaK0UV10Aw-YF3XdFzZSSByLiBhCNTHDkFgigSGUp5FE6A07Lh9YmYpKw6AD92uKQX0RZ1E9itZEsnX_bqoQKLg35zeHFnYjprtVC6aI8OW78V2lYwjiKDyTz6udRtarKSYXQXjDVHEXnI-WhCfNXszQCHkEJYph5H9MI8uWB_FI5FcOJmn8E0Pq2D8oUEi2Pfww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
از تلاش کردن و نرسیدن خسته‌ای؟ «موش‌ها و آدم‌ها» رو بخون!
🔹
«موش‌ها و آدم‌ها» شاهکار جان اشتاین‌بک، داستان دوستی عمیق دو کارگر فقیر است که با رؤیای داشتن خانه‌ای کوچک در دل زندگی سخت آمریکا پیش می‌روند. روایتی کوتاه؛ اما تکان‌دهنده از امید، تنهایی، انسانیت و سرنوشتی که نشان می‌دهد گاهی زیباترین آرزوها، تلخ‌ترین پایان‌ها را دارند.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/671827" target="_blank">📅 20:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671826">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌
♦️
پایان ست سوم | لیگ ملت‌های والیبال
🔹
ایران ۱ - ۲ آلمان
🇮🇷
۲۵ | ۲۶ | ۱۸
🇩🇪
۲۲ | ۲۸ | ۲۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/671826" target="_blank">📅 20:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671825">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO2jYEpBhT0KgzWf4jNelZqtEUygBb__ICappL3nK1P9ydBK-oXBHnY6HTbxN52QoVmEjIL-Nb6v8ff3nGJr7xDR5Pt2ao-LKeWKWpPUlzigEvx6wYgM-W7fjadBqAv4Jx18-hGi06lRgUSV5zmQqa2WLzcWOUOGHktUPG2rDk9zYHt5OwegbaiLR56pOHCSNxYK6anMhp40GI6WEh2paT8frDQs1kGZJJGQI7GzVimYH22YF-DvIOP0jZU234YfFZCngRuQq2zP3tvLPX7N56ow0yKqjAcI25KytirUZ9wfQZG8d9LM55PhWbNx3WfZXpibk0BrdqYepaI7YLA_TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/akhbarefori/671825" target="_blank">📅 20:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671816">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uv8kDUg0bgzvlZEyH6pfipYmFSI3xM0chFpX0uxG8oykpdqV4TS9utFzwqgo5V-keZv4E-pyEyq-8Pa2MrMl0tuFLTLwgMT860c5nbO0TmiHDWAeaTsvj1BDjhaE_FSzkFq3geCG5-lgJhRAgNPXV2N374kasMjFDASafBPpaE1BUoo1vCEBniUEgTD0_K7q2zOOi_iW78hfQ93037CkhFVQStVI3n2Q318CPt3Lk0IYxBxRZfCwVIq6d0xT5ztIUW7ErPAOYHe6cWHPD7D3U9RR7QQ4xcThpbRMJ7kN8XXbNv0mwDq6E4nJSqZ-Vmrs35m7mEdfgcP2xtM16x1sSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKoPNjO5JWQ-R7g4wAQSv9yyTboMISYwVkD_iXZkcOdndf4aWjRrTViyTaWtB0so3aZX2p26T7pBqJMgKk7WJkBB7LG00kVp0PTOSgJrAnq87zAwrAWsMVM8nYRDSPhWrueOC3nvvjm2dlo2n9AEf8_uVCl_pFMv9nrouw0S46_vDwV46koS65sw5Gm35NIKFWLfXi3vF41cLr5T3SlFTkiqOGJoK3kxkHFhPJ_a2AVJ2enPUTW2KgWfhK2Vc_BxPA5axpLuq0YvMsqPN4nRnuDi3T-FqYv9M-BBpag7TO4PJe5stk4SIXoNIvlBMqVFA0i1Zb0hdy01ol7DbULYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DflpwvQc9ijOpLNLPa9sjfDuF_tq2kuZD_czgahhFZjtUiJ4LueFVVtjIIcp0Wx20fsDSWCUZVwoT6SJPSlmzhIfDtVxmRAWEpWyFVh3YfVKB18i-jfvWzFeHXwdbHNCe-ORSbzkaeRvkPs87j2A_7fGhWIolKsfLBb38oyvLlRNwPzxXWkloRUztRK9dOUJu7xn6QUR9tUxNX_5t7HYVkXjjan6W-Mmolpq2znQPvlyHLreFbDGbSiRV0Iata6E6z3Qpo71aqkUo9P1R_hv9L8qQeezo7u36hmmw3c88hfiFtSlp8M6JuezNEG-guB-hJjiLj3TRHJULVRGIZ4aNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/neCza6yIZ2vDoJ7mIoi7o_o7LPFFuaeMB-VI7ypuf-PQFLCW45e1zm5-MM5vXGs6NpYe4GsApAmNSlvsJn-SOpwStQ7XoN1mxL6YWr7nBXKUd06pA4-zG4tEYD2JI0zcl7v_fMSaeMe1OfOspF6EqC2XMydBH2Uopiu07mq29W6oH3Pur3-oNWFoF9fs_18V44gJaEXKwAO2W9UBguFpZ6Ek64FcXCmzDxotefusNVAtzCUxkZP4I-7lmXz9dcPyBSl94EiO35bhgu_Bc44AJ4xAdj_074KVjD-sAY7thnDveLIkywq0ui4ikS6PByurLduqGG-5eUs83jX_FFaB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgPhnPCHKkLdx0-dQx5dgtyFW7zAsdhx8yqlB3U8Q15Oo-gODHxK5xYWFSGCfgLeqi1VhLC6NCXZbm44u-zApx2_fSJATJiP67Xj42ar9lq0slkRFkKHo9lNmnarG_9Jacwmg384TJLsZGWhTRLt_tb6mWNF_rtzCL2To51n34w118Stge7xIrpChJoHMGHZpTuZqjAbvzNpqft1R-xmiepbZSTHXb9ckN3F3HxbQ2hHZWVvb8afJkmIK-9h8NKSTkpnl4s-pWUDhGMtg-PrMadNie8RuTVW3Mh_gYsqcEvcrwZvtJlRR5MTtsnTXPBXWDGloAdKPGe-R3vPvFkdzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrJouMYseQF1XcLHk9Nv21GNsUvCG-n5DED6721XN8IiYG4Ym_LvF55Zq_LPEdabQo5MckEph4Z9ZjkIB19wjFQpyaF6AenWs5_eLhOx7LlB1XHZoqVXDvhSDRhaWsYcfW2Ef9ALh_6w1XnI1jY3d9rXGV5h6R2e05Qw_aB7SpIZQxdVgu-4NVsIHg0dfQei_lzsde0GFhgQdz8h7-RyAxKVbg2rnOszn3Mc_4pK-FTBVdnbt66lOH_7utWOokp-kHkjXPaThTic8K9bEDrOlS0gABmVuNpvvIFveSP5O8y5Hioi0Y1oAgFpwqficpK4WwHmhNV5pEDXuxwF1I6AIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-paU13PjKfNOUhvrpzy1tY0v-V2HaTum3n1xOm9Z6LKnEouIq56tNb5p3hN-JS-tLf3X7_f0ATMj9FbKGZIowGr81u5RX0cyiXJu7XeojT-r67tV2pPp_hZreMHeoRE7P7QLVu-AQcWaH2vFPEkzeujuNFzzL0FCFK13qWMl1uIxYlo2qxby57HhWDa8Cd2W9WKelgTgNDa92tVZtEhwrfJEYHN1zunJcjkwhWW0nIMPx-5M0ItBpHDWlz5oP8f7r_mBPU7UXSbVrJmHzPakaqBaqI4ot40cOEovANh_aYaYuMxjhcGsiigb_4U_bL0M8Vu37HMsBKQjX9xZKoJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkWOgng8n-nPPYmIVA9GH0ofV5yZqSra86HtecwmuEzfWF783w-ATPmXca000gZ7GwDHtNRuNzXl4cNLnMe35oNlx1GgDhSl2AZXoZj4cX-Nr5bDAu5yGXSjf-dXEfjsCdGtv7HfDHjw1W3HXgcQaSd1RJVOAfJcXwSIE2wfoaIyHlxB9MnL7SEY-v1fVWkXynhnO-4S5iY_Utb_Y9aXUiJHL6U-PZSNw0QGuc21iHxHHJTJd6Hgq3QfZP51HbCkrgnrVoNLPwWYlGxviKUAvtTfr6N0REUppDnu1M1Vvz8v_8bvnieKumwDIZikRF1LVBsHQJzFkWiI2m2Y16VOmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7PGKpj8cmdM7oOtWAuwZnQoCI-pQTGgB1FQyp2G9TMl7JK2y7mq86fjnFHTHzgjIxcwF_J3kBKdscF8lNPASyzuNK147QWi0t0mt8veX_I0moYfx6zdfHap2uKmMol6LPJ9jtIOr5Qw9MdbExz4cdiFNAGEsKAtmDRK3-EqjDFeLn4rjAE8mhWXZxjoHwTWS982sewMptluhEELM0jQqlXNTwXCdYIQwgrz6rPfANWNq4Qi2-d7RQTdqtOuYj7W0mqnoXteQ0M20HOiz3JCFpo-gnK5uRuiOmKaIoFFPRj2UD9XJcDeqVjWJVsa_u5jBPVK-I0b1jcYlVJJW8RC4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گزارش‌های ارسالی مخاطبان خبرفوری در خصوص قطعی برق خارج از زمان مقرر
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/671816" target="_blank">📅 20:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671815">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToXI24VLPIcqW5wuuWj-FX4kmdpaez0Qw1H8l4EEqxbrB_5Y56pxdI8gGFnFDt4-3wC7BTDsocjOwhwzqiRjpiU5cSuSiILHTmyoJ1thqVPhETJosWTdgZ1jRwEFVpOvBsdxViHkiMozq-MCBwEMa7kpuS5ImYlge4hBd1P-kdmO1isEF1-X15Qi2Nw4CnnAZRMOn3d2JaSaeOYBOLkhF-VApHEIphVai2LZVIONwg7zyFmO6zjG_Jr-NA0_xf52lJy7yQcjbS84cuNKsahYzonliyYixw1dXZrU1dBnOgnU9q940T4rxJZDoY9TDVvZ-u3T7WacQASgwZE0OX9p3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: دوست دارید کل زنجیره تامین انرژی منطقه را نابود کنید؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/671815" target="_blank">📅 20:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671814">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mStYD4vhp7XL2VeHEVFUxtKK1-DRcWKb3pN0r8XbklJxKjaa5dD2jWLCu5J2BR3sbGW5H6m72m6irWn8bnVu3FNn8SS7qd2rHFNvS2A4JCayUucYN52Oyos6F6u_TCpJgTH0ruCGaSSDYrPv_pBd-vudHGa_a72GmAXodN7jYszYG8z-RHkQJRLSFBrmzzjNXfgbpfGPanmm0Vt5WXK9kZYhPGnwvKxbFDLzPidFk-uG2DenS63GpUXxL8ihwlehVJM1ULkEnfjYNJmUwZFXRvQf9bWkW5tbBwmDNOUzXmjYlmKO9xNzUiSQTFnSlYtXqb_twRHoMx9B24j-_LkBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور سردار قاآنی در مراسم بزرگداشت شهادت رهبر آزادگان جهان در چیذر
🔹
این چندمین حضور عمومی سردار قاآنی پس از آغاز جنگ تحمیلی آمریکا با ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/671814" target="_blank">📅 20:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671813">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogb6uzat6oeowi1462T8f1qlVyBvgG_BEST0n9170-YTmi961YGyQQFgvludGIN2l5RgwI0QD8YzFN3G077X5FE7-0pqOFqk9UBb-mFOPkHGW5N_7M7wuE27FeU9SzPs7v_3vpO-BTqGJoxX9sPfTGvcstDyvPS5Glekk0pa6oPNhwy8ZVL2_xGUv2kmc4p8oAtTH5IrBcIix3-uNkeP9UwH1FIGyKVe5KK4wevIo5SPvHQEb_7jp4TiiBTx2TaezlxOeuJteT8hOdcOP187tsD7LfUADvhLqj4cZfJJBHnXnUkQy1y_XWvL_Q_DdPhE3bDCU8R3pL5vWmrtxnETyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز خیلی‌ها فقط یک جمله گفتن...
«کاش زودتر اقدام کرده بودم»
💎
اجرت از ۳٪
🏦
خرید مرحله‌ای طلا از ۵ میلیون تومان
🔄
طرح تعویض با عیار ۷۵۰
👰
سرویس عروس از ۱۰ تا ۶۰ گرم
📲
مشاهده مدل‌ها
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/671813" target="_blank">📅 20:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671812">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
رویترز: صدای انفجارهایی قوی در مرکز شهر دبی شنیده شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/671812" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671811">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
اعتراف ونس به ارتباط اپستین با نهادهای اطلاعاتی آمریکا و اسرائیل
معاون رئیس جمهور آمریکا:
🔹
او به‌وضوح با بالاترین سطوح اطلاعاتی آمریکا ارتباط داشت. دولت ترامپ «کاملاً» در برخورد با اطلاع‌رسانی‌های مربوط به پرونده‌های اپستین اشتباه کرده است.
#جاسوس_موساد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/671811" target="_blank">📅 19:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671810">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
اصابت پرتابه‌های دشمن در حوالی بندرعباس
🔹
حوالی ساعت های ۱۹ و ۱۹:۲۰ نقاطی در حوالی بندر عباس مورد اصابت پرتابه‌های دشمن قرار گرفت.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/671810" target="_blank">📅 19:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671809">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti1s7tGFYaYXOAxVWgEcjliGxGx8fP70BC0us50Wyk7CQDNDColLqhHKxqEPz_rbQmZMNQ5WmouE6o4jVDxYaCKZKRr94ShZdBryX6WCbhGXSWLovF2ddGzosmlBlWa_U4GrdDVHhxPyvWdcoD03LnBW3YJftEwdY_YjHJcnPBM_BkTq3PtW94RIjIMiAMy8D7vMEqEZeeqP6i9hnd3nbvrgIkE7PjtNu-kU2rgAGPCk38ElJybnfqIhK7O9C8DuCR8iqH-V68zdLBsg0zlJInzR31EVQp1OJb8ZWILXtjyyLiodx6gGRmxFp5FzCzVpJDpSyXmBnvB4jyJma7B9aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردِ آرام در مهم‌ترین شب فوتبال | علیرضا فغانی؛ روایت صعود به قله داوری جهان | از قضاوت فینال المپیک تا سوت بزرگ‌ترین بازی فوتبال
🔹
علیرضا فغانی، داور پرافتخار ایرانی که حالا با پرچم استرالیا در رقابت‌های فیفا قضاوت می‌کند، با انتخاب به عنوان داور فینال جام جهانی ۲۰۲۶، به یکی از معدود داوران تاریخ فوتبال تبدیل شد که مهم‌ترین مسابقه جهان را قضاوت می‌کنند.
اینجا بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3230845</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/671809" target="_blank">📅 19:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671808">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
پایان ست دوم/لیگ ملت‌های والیبال
🔹
ایران ۱ - ۱ آلمان
🇮🇷
۲۵ | ۲۶
🇩🇪
۲۲ | ۲۸
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/671808" target="_blank">📅 19:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671807">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
صدا‌های احتمالی امشب در نوشهر مربوط به تست شبکه گاز خواهد بود
روابط عمومی شرکت ملی گاز مازندران:
🔹
صدای مهیب احتمالی امشب در نوشهر، مربوط به تست و هواگیری گاز خواهد بود.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/671807" target="_blank">📅 19:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671806">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVK6r2TiX1EIeoMkIIPqHfqK3IC7BWj2gRKF37_xZ5H2ALZIi9Hm1j0xYANiP67A6vYiBSSwKDbu-d8YywPGBvbA7sdpueZ1Xb1zu93lxP11N6wjeWBAS-V2e-t2I-UV22sDn2OAs_RFx5F_Bx6IJA2ShQVi_XWTOsSijLwlTxHkD4IOePPig6Nquu7dLyeW7vYC4XGArZQulyL1h4AkHgvVIr_o-82nCZtlDTgtncVSPEDy-b42_rMqRgSeJKs5o-_v88ZuctOeE-BlYT-GGFW4Dm6oWEAZLaAKQStlG1YgPmZMtH1A5XR_5WonkT-uHnQ9JEL5zmuzLvm-0b99Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فهرست جدیدی از ترور مسئولین آمریکایی اسرائیلی در رسانه‌ها منتشر شد
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/671806" target="_blank">📅 19:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671805">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
اعلام منع تردد دریایی در آب‌های سرزمینی بحرین
🔹
گارد ساحلی بحرین با صدور اطلاعیه‌ای رسمی، محدودیت‌های جدیدی را برای تردد شناورها در آب‌های سرزمینی این کشور وضع کرد.
🔹
بر اساس این دستورالعمل، تردد تمامی شناورها در ساعات مشخصی از شبانه‌روز ممنوع اعلام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/671805" target="_blank">📅 19:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671804">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
اصابت  پرتابه‌های دشمن آمریکایی در حوالی قشم
🔹
در ساعت ۱۸:۱۰ نقاطی در حوالی قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.
🔹
گزارش تکمیل پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد./مهر  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/671804" target="_blank">📅 19:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671803">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
آمریکا از مسدود شدن بیش از ۱۳۰ میلیون دلار دارایی دیجیتال مرتبط با ایران خبر داد
/اقتصاد آنلاین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/671803" target="_blank">📅 19:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671802">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
وزیر علوم: کنکور سراسری در زمان مقرر برگزار می‌شود
🔹
برای برگزاری آزمون، هماهنگی‌های لازم از تأمین برق حوزه‌های امتحانی تا هماهنگی‌های امنیتی، با دستگاه‌های مختلف انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/671802" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671801">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f50a9527e.mp4?token=Y2BuZLtjcD59eDR8zoGNNAu3FaZKwPBeC87Oqt8WDd1pbimHQAMBzq2IZWDYWBtuHwVFqNylCOIdjtvN25O-ezfh1InweKliwM7pdqp6-24X6XJYqlPQVGLsQ3w2YP9oBP-vvHGs4ySqr053cuoROD4UYop87GqmGSI-TucMSwAgs4iFRTxZvBAt92GqtSyKzyFMCntkQbs7gt9Ei5yKzBr95s93hbs8E6Q-fjhj9wUoitKUjHLcO1GJDSyvA_rEJ5H1fKJ9fGsVv5WJLeDUaVxxeFoOgVW2eAam_gtmzSHX37H-qpDVyGIUcvbdpGEzBHaXIzRHWlrdw3o7E3JyRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f50a9527e.mp4?token=Y2BuZLtjcD59eDR8zoGNNAu3FaZKwPBeC87Oqt8WDd1pbimHQAMBzq2IZWDYWBtuHwVFqNylCOIdjtvN25O-ezfh1InweKliwM7pdqp6-24X6XJYqlPQVGLsQ3w2YP9oBP-vvHGs4ySqr053cuoROD4UYop87GqmGSI-TucMSwAgs4iFRTxZvBAt92GqtSyKzyFMCntkQbs7gt9Ei5yKzBr95s93hbs8E6Q-fjhj9wUoitKUjHLcO1GJDSyvA_rEJ5H1fKJ9fGsVv5WJLeDUaVxxeFoOgVW2eAam_gtmzSHX37H-qpDVyGIUcvbdpGEzBHaXIzRHWlrdw3o7E3JyRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بر اساس تصاویر ماهواره تجاری سنتینل طی حمله پهپادی شب گذشته ایران به فرودگاه اربیل، آتش سوزی و رد دود در محل استقرار سامانه پاتریوت امریکایی دیده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/671801" target="_blank">📅 19:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671800">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
‌ پایان ست اول | لیگ ملت‌های والیبال
🔹
ایران ۱ - ۰ آلمان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/671800" target="_blank">📅 19:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671799">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3G_Cotjoqrg1Ckbpn3UN7beakybEmqnZ0bJuivOP2aGgQRBWmjYFd0AmUJbYQeYFSSEoYxmsVagh5hnXSn89u-Zt6_yZ9JE5pG6FsRnGPAV_b798LYH8erOBQnTQ7n-qaMaoUA-7orFJ2HwI5l5KXi6U_SmLz6EO2O-6L-ANbaQJRVBhzHNuJ1Aa6GwuazRqHhogvau0G42fSf8L9_aT0w6cnIrgAIyPxv5_Frc07b6WCzEpSWP3toPdxcpifc6cptfuK_Rf05r3c7LqFwfsvPhkngBFFp3tZ_mDJhvwWbaws3qj2rOaDLsBTPf800j1qsd43Yhg7HOnH2GIHwrXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین عکس از آلوین در سری جدید "آلوین و سنجاب‌ها" که ساختش شروع شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/671799" target="_blank">📅 19:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671798">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qca3mpXB2bFP5imyH3NEFxCP1q0cCLpElNHp9d_O_T1307s9nsD5T_0oro6f3uh8zap2xC9OldxfDzWVumvfUhJJ1d8Eydl27FETEOC_RtCdwAncsxShId8R1NrasJ0hbciIe3lfvTA3TE2xvWMla10SoWwlrDfUze1JuPU79jXiQ4JuHYq-Sllu9v0Yw6IlLFPCNHIPTDyxuc5D9ZxWJ8AMp4HBCAviu0_8Djh5S2ueH5hV_eWWqO8ASI0KoZUm6OIrRTQbFp3mRKSH3WbNa9cX6JxW3BYS3gjtYC1D2Vb_mkv2XYuepzauWFFP-jnTIfGPRrKTAWVm1-rX6WttXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/671798" target="_blank">📅 19:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671797">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqHbKHV7aCyW9RxuX-VQcvvDuy3Pjsx1BIjjeHopHVWy2OsA1B6sIsR0Jfp1MH-2182wR256GfBE7T_GJWpikx7ano1uwNdqhqIDLy_QJWXXKSzTck4q9DLKKUjcMD3KRpykayMHosq1K8qQulOyoGfGz7LaGERw6lBbXUfchygPfcFUTXp3AAYnpyQRk--MQakXjbDecXex2ypn6zsrgYexcSLug-ykgngpD22B5OshlEZNRfkhZW5G5mrtWEDijYoMV6Ee09k4bZaCIHJJyXHGYsTjqUTL71GNI-_4UrTObcBsMKoYIdU8B82_2l72HOWhzZxmghvYeg3sK_B1zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری هادی چوپان در رثای سربازان مظلوم که در حمله ارتش رژیم تروریستی آمریکا به شهادت رسیدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/671797" target="_blank">📅 19:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671796">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUv8dUV2mw5Re2SG9Qr202l3ZXxJyGWkT3ckT9NthxvqvkzAUEzKvSAyMOyGSX9KIms73RPnCqmIsjvY7JDsB4GjLS60JAgJW9x00s6kFVWP4EEYTv1Ddm9QTn8YF3Xp5aaJQJx1Nfcfe37AdpjsFNAQsdSNmDAodMLA6ocgK5Y7bEgclB7h7NqH4gzSfrDXZrMnGynuBzEO0GP_93ufJ08ZdjgCnio8-iHS5LJUMese37p75RFUFZ__Sywbbk3bWyntkWWimEiJ016tUB4xVQIHCrbBkFcfAIV0xE75FAanR6HQHLGLFob_8RI1HF72bu5l0Ja27Ah_c8bDsdV5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدهکاران بزرگ پای ثابت بانک‌ها را بشناسید
🔹
بررسی آمارهای بانک مرکزی نشان می‌دهد نام برخی شرکت‌ها و گروه‌های اقتصادی طی ۵ سال گذشته به‌طور مداوم در فهرست بزرگ‌ترین بدهکاران کلان بانک‌ها تکرار شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/671796" target="_blank">📅 18:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671795">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqS4vj-qhXfrgKo8_LPNqnJDUk-aVHWBxhBN2R3_F3jnantVqqqGKrRUpYud7-QdXCXZAIdaaUERdw14RsAcpWUoPfqIW34uATM5YBhbQntaU34I9hZEIpxvPYIaxo6GcuE-C6GjzduIN4N2B6EwSxOnyIxd3KkVFBjSwznkqI4NdVc1waiqZCiRM-mvJ02jRzaEbITf4CdBI8PN5_R_6mtCUkasUEaZ5RVBNmOrP39IeQqzUqMPa4rkKUSBoli5EpDc2q40ioq_YP4PfQ3d49K1JDeFI_peP41RU7lI_GRivBdogkE2FNGCQzo7kG0QEi06exAKcqg6vwwO1Pbvew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه: آمریکا با نقض تفاهم‌نامه اسلام‌آباد، آتش جنگ را دوباره شعله‌ور کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671795" target="_blank">📅 18:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671794">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
اصابت  پرتابه‌های دشمن آمریکایی در حوالی قشم
🔹
در ساعت ۱۸:۱۰ نقاطی در حوالی قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.
🔹
گزارش تکمیل پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد./مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/671794" target="_blank">📅 18:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671793">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
‌
پایان ست اول | لیگ ملت‌های والیبال
🔹
ایران ۱ - ۰ آلمان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/671793" target="_blank">📅 18:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671792">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
آمریکا برای خبرچینی علیه انصارالله یمن جایزه تعیین می‌کند
🔹
وزارت خزانه‌داری آمریکا در یک اقدام مذبوحانه که نشان از تحقیر اطلاعاتی در برابر قدرت رزمندگان یمنی دارد، اعلام کرد در ازای دریافت اطلاعات جاسوسی درباره فعالیت‌های جنبش انصارالله یمن، پاداش مالی پرداخت خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/671792" target="_blank">📅 18:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671791">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/251b490de0.mp4?token=o3hikr4WKuTtofPDTx2TGLsfIicgMiid61Q7WQ0uvgorS4gVSOdQ8GV9QofiIj1U7E3rzftXTH8hdWfFZtTItim9_Tv5EH5OPplMYuqbJkxyjHQdlcUeFo38N8AS44Ea6gLbjb2PihiZcg3yC6Jl_GMn0pngMJimULWXYljtEK6NFyp5K0gsW9_oPqNsK2kfmlKqkrDBN1ybu-Xgtf0igMJUfeykV2ze1kqHRL8-C7tMkBEGAHCHpT_2CIDkqKvASkXNnAbb_si8gDc7OzcfseWjtnuzYPkRrQX14mVeLAA_Bu6rG2pX75gUn-8bxbrvVF8VDVH-gdUPaeAhE1lllQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/251b490de0.mp4?token=o3hikr4WKuTtofPDTx2TGLsfIicgMiid61Q7WQ0uvgorS4gVSOdQ8GV9QofiIj1U7E3rzftXTH8hdWfFZtTItim9_Tv5EH5OPplMYuqbJkxyjHQdlcUeFo38N8AS44Ea6gLbjb2PihiZcg3yC6Jl_GMn0pngMJimULWXYljtEK6NFyp5K0gsW9_oPqNsK2kfmlKqkrDBN1ybu-Xgtf0igMJUfeykV2ze1kqHRL8-C7tMkBEGAHCHpT_2CIDkqKvASkXNnAbb_si8gDc7OzcfseWjtnuzYPkRrQX14mVeLAA_Bu6rG2pX75gUn-8bxbrvVF8VDVH-gdUPaeAhE1lllQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسپانیا فقط با فرانسه و پرتغال هم‌مرز نیست؛ از جزیره‌ای با مالکیت شش‌ماهه تا کوتاه‌ترین مرز زمینی دنیا، مرزهای این کشور پر از شگفتیه!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/671791" target="_blank">📅 18:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671790">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افزایش ۲۵ درصدی مشترکین خوش‌مصرف آب/ سخنگوی آبفا تهران: آب مشترکان پرمصرف قطع موقت خواهد شد
بهنام بخشی، سخنگوی آب و فاضلاب استان تهران در
#گفتگو
با خبرفوری:
🔹
وضعیت منابع آب سدهای تهران نسبت به سال گذشته بهتر شده، اما هنوز با شرایط ایده‌آل فاصله دارد. مصرف آب در تهران بهبود یافته؛ سهم مشترکان خوش‌مصرف ۲۵ درصد افزایش یافته و سهم پرمصرف‌ها از ۸ درصد به ۲ درصد کاهش پیدا کرده است.
🔹
مشترکان پرمصرف در صورت اصلاح نکردن مصرف، پس از اخطار با قطع موقت ۱۲ تا ۲۴ ساعته آب مواجه خواهند شد. سرانه مصرف آب در تهران ۱۹۵ لیتر است؛ ۶۵ لیتر بیشتر از الگوی استاندارد و نسبت به سال گذشته، ۲۵ لیتر کاهش یافته‌است.
@TV_Fori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/671790" target="_blank">📅 18:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671789">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
رکورد تازه یوز آسیایی در خراسان شمالی؛ ثبت ۱۲ مشاهده مستند در سه ماه
مدیر محیط زیست جاجرم خراسان شمالی:
🔹
۱۲ نوبت مشاهده و تصویربرداری مستند از یوز آسیایی در این پناهگاه حیات وحش میاندشت در سه ماهه نخست سالجاری ثبت شده که از نظر تعداد دفعات مشاهده، رکوردی کم سابقه در این زیستگاه به شمار می رود./ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/671789" target="_blank">📅 18:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671788">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVjguHimMcARc9pOs3mNt0LxBcTgI3hb1M2cW__HkAo7wF9iDd3o9U4KJ4yXSiYFdteR8nHCgB5dYcESkLxrqtAQue0y2QUdzBkszHfrERZ16vHnhlTIZjs7pYBso7uvBNUWS27FxpWhT7am8LmFaVOBfy9uOXyXF58Yb7UtBlV2e4aq9k4KfR-kISHvE7BIpBCZEKo9P63pkAl5st5azoDjMzWqZj4NWDmAAxCPagmapOeb0HkymrRuIm9JWVgjVe41PRyIyZSTZgPfjHODzeUZ7Co5V4-5csg6PCE6nHpNhFxyiMmQqH-kuqS8iZ_iO-08lF7uOnkQnMSZIQn0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مه‌لقا ملاح؛ مادر محیط زیست ایران
🔹
مه‌لقا ملاح، ۱۰۴ سال زندگی کرد و بیش از ۶۰ سال برای نجات طبیعت ایران جنگید. او آن‌قدر به باورهایش پایبند بود که گفته می‌شود در شش دهه فعالیتش حتی یک گرم زباله از خانه‌اش بیرون نگذاشت و از بطری‌های پلاستیکی یک‌بارمصرف…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/671788" target="_blank">📅 18:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671787">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a5942b565.mp4?token=eTP1geWcFpPZ0Tdo4uM3772TvUc_tzUx_9cg9BWI3vO7LlqU2olWF3R2Ic8V4TKNf8m-uWSko6dXMFYX_LT7G-b4yYSGSmmY7kE8s5sqGORExTeNzcohMGuUA97QzFgU0RueKZEe37JHmx8ISqEjcuOir_WlHEaMCIvvpVuD0M5RFiKqr9KP6gd_zKJqDbh7JKcYmLNVxkrTvyxehHVnpKiWq6xGmIsyDWrAqUBocJSbDyOMNs4hXPDeftoEd8WLq06tfpp5lmISacYZV0wMkDdsFE3NJeey4ABpC5M-xWcjc-TIZhLTogNfnVqilIAJMblQuldHmbmeifUXCzEcqwfQi1203z5fIuQ1Z4G0bW3dr1jtKt6RqEGpw3YNyXluytedYlWuRPdQOi3SM_loeeFKlWN0OXWXyf7huDO_yezAttrL9EstJtSqiw9RiRhkn8Gi1SxNYEG_L5hTz8zkz3ZGI5X849UmYZmovuf8wd1WG6SXywqhlX5grK4IW7IWzFZqKdjT0Sda6pmj_MXLzSdvDRhm6bUu4gPZtkECiB38GCw2WkAEbtaEw9njaEG7YRfaz_7KpKx3_NOkHdLUrIVEOk_tu4lJRRjKzievtFZL5AwL-tG3-lOY-3-bDlKzbE590fxAw1qzBKxkVRc11G7OF5vtjXuylhdZ4nVgPTE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a5942b565.mp4?token=eTP1geWcFpPZ0Tdo4uM3772TvUc_tzUx_9cg9BWI3vO7LlqU2olWF3R2Ic8V4TKNf8m-uWSko6dXMFYX_LT7G-b4yYSGSmmY7kE8s5sqGORExTeNzcohMGuUA97QzFgU0RueKZEe37JHmx8ISqEjcuOir_WlHEaMCIvvpVuD0M5RFiKqr9KP6gd_zKJqDbh7JKcYmLNVxkrTvyxehHVnpKiWq6xGmIsyDWrAqUBocJSbDyOMNs4hXPDeftoEd8WLq06tfpp5lmISacYZV0wMkDdsFE3NJeey4ABpC5M-xWcjc-TIZhLTogNfnVqilIAJMblQuldHmbmeifUXCzEcqwfQi1203z5fIuQ1Z4G0bW3dr1jtKt6RqEGpw3YNyXluytedYlWuRPdQOi3SM_loeeFKlWN0OXWXyf7huDO_yezAttrL9EstJtSqiw9RiRhkn8Gi1SxNYEG_L5hTz8zkz3ZGI5X849UmYZmovuf8wd1WG6SXywqhlX5grK4IW7IWzFZqKdjT0Sda6pmj_MXLzSdvDRhm6bUu4gPZtkECiB38GCw2WkAEbtaEw9njaEG7YRfaz_7KpKx3_NOkHdLUrIVEOk_tu4lJRRjKzievtFZL5AwL-tG3-lOY-3-bDlKzbE590fxAw1qzBKxkVRc11G7OF5vtjXuylhdZ4nVgPTE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
این روزها با قطعی‌های برق، داشتن یک چراغ‌قوه معمولی کافی نیست!
🔦
چراغ قوه دستی ۸ کاره LED Torch
هم چراغ‌قوه است، هم پاوربانک، هم ابزار نجات!
✅
نور LED پرقدرت
🔋
قابلیت شارژ با USB + استفاده به‌عنوان پاوربانک
🧲
مگنت قوی برای اتصال به سطوح فلزی
🔨
چکش شیشه‌شکن اضطراری
🔪
تیغ برش کمربند ایمنی
🚨
چراغ هشدار برای مواقع اضطراری
🏕
مناسب قطعی برق، خودرو، سفر، کمپینگ و نگهداری در منزل
❌
قیمت قبل: ۱,۴۹۸,۰۰۰ تومان
🔥
قیمت ویژه: فقط ۹۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
💳
پرداخت درب منزل
👇
قبل از قطعی بعدی برق، این ابزار کاربردی را تهیه کنید.
https://memarket24.ir/product/brief/30291/180124/</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/671787" target="_blank">📅 17:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671786">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a755c6a7f.mp4?token=i6r4hN32hMbw7m6cjItq13CFx8qH5BwHTteMnspliRuO8b3XUr9TDFc7n1kLHN-UmNffNJabaf6ZD4fsf0qX81_SehGfq6T9raqETrNFUCNzdRTjmSGOrzKWp7BvObEAzREesw_hJIMoEovFZVc35IAnrtVvsip8JcRFDp2jmSMF_McDfjKZMyXWacZSKPuiBX6ZHtVX46_0SBe_Z75uBzk7wlUT5JSEjnzmNb2Dqbylf-pTv47rqKrETDWTrSpIAmi6FCzHQnwLad46idvR_gyfaa7P0hE2YeI81BbZiAO_CxmGU87FXh858yZd_eW1boybeoyeMqlqhz23vhtsQFbGSn8ygczf31eBQEdW331_YFX8MAtoN5MLP3t9AiD36we291yFNG4shd7VJpeFt9jKEEku2bvnbwmJnw_EhNRaVkGl615XhScN4Yr3fS6RRuF4pcRwQD8fQBGkLTCc7i98HMpuE2P-OIvltU3pkt5uVamazeKjIvMl6CRHW8BgJ-hH6KWUc1A_e90weTGQP8MQkNguFXUHabJOunKNOPeVUO_UGhh9RErI1P1d0Jr3XCIPF38lE7Qq9mtjrkK49vVFaXjkIpL0Sbt4qX0vBa8o0pRP9YOktnmgniufeuXfnouD62HzeITDcwQLNGft85i9xr2q8g6gJDSp9zzOhYk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a755c6a7f.mp4?token=i6r4hN32hMbw7m6cjItq13CFx8qH5BwHTteMnspliRuO8b3XUr9TDFc7n1kLHN-UmNffNJabaf6ZD4fsf0qX81_SehGfq6T9raqETrNFUCNzdRTjmSGOrzKWp7BvObEAzREesw_hJIMoEovFZVc35IAnrtVvsip8JcRFDp2jmSMF_McDfjKZMyXWacZSKPuiBX6ZHtVX46_0SBe_Z75uBzk7wlUT5JSEjnzmNb2Dqbylf-pTv47rqKrETDWTrSpIAmi6FCzHQnwLad46idvR_gyfaa7P0hE2YeI81BbZiAO_CxmGU87FXh858yZd_eW1boybeoyeMqlqhz23vhtsQFbGSn8ygczf31eBQEdW331_YFX8MAtoN5MLP3t9AiD36we291yFNG4shd7VJpeFt9jKEEku2bvnbwmJnw_EhNRaVkGl615XhScN4Yr3fS6RRuF4pcRwQD8fQBGkLTCc7i98HMpuE2P-OIvltU3pkt5uVamazeKjIvMl6CRHW8BgJ-hH6KWUc1A_e90weTGQP8MQkNguFXUHabJOunKNOPeVUO_UGhh9RErI1P1d0Jr3XCIPF38lE7Qq9mtjrkK49vVFaXjkIpL0Sbt4qX0vBa8o0pRP9YOktnmgniufeuXfnouD62HzeITDcwQLNGft85i9xr2q8g6gJDSp9zzOhYk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ببینید؛ انیمیشن ترامپ و عربستان!
🔹
رویترز: عربستان سعودی به ایالات متحده اجازه داده است از یک پایگاه هوایی در فاصله حدود ۷۰ کیلومتری مکه در جنگ علیه ایران استفاده کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/671786" target="_blank">📅 17:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671785">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
حفاظت امنیتی نتانیاهو به دلیل وحشت از ایران  مادام‌العمر شد!
🔹
کابینه امنیتی رژیم صهیونیستی در پی ارزیابی‌های نهادهای امنیتی، با طرح ویژه‌ای برای تأمین امنیت خانواده نخست‌وزیر این رژیم موافقت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/671785" target="_blank">📅 17:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671784">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دستور اتحادیه اروپا به گوگل: دسترسی به اندروید و سرویس جستجو باید برای رقبا بازشود.
🔹
لاوروف: دلار تقریبا به طور کامل از معاملات روسیه و چین حذف شده است.
🔹
وزیر دفاع سابق ترامپ: بمباران هوایی تغییری در موضع ایران ایجاد نخواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/671784" target="_blank">📅 17:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671783">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
صدور کارت ورود به جلسه برای ۵۶۱ هزار داوطلب کارشناسی‌ارشد
🔹
تاکنون بیش از ۵۶۱ هزار داوطلب آزمون کارشناسی ارشد سال ۱۴۰۵ کارت ورود به جلسه خود را گرفتند.
🔹
از بیش از ۶۵۱ هزار متقاضی شرکت‌کننده در آزمون کارشناسی ارشد سال ۱۴۰۵، ۲۴۹۷ نفر از داوطلبان توان‌خواه هستند که برای آن‌ها تمهیدات ویژه‌ای همچون منشی، وقت اضافی و دفترچه بریل یا درشت‌خط در نظر گرفته شده است.
🔹
طبق تأیید سازمان بهزیستی، برای داوطلبان واجد شرایط استفاده از وقت اضافی، زمان آزمون به میزان ۱.۳ برابر داوطلبان عادی در نظر گرفته می‌شود. این زمان اضافی صرفاً به افرادی اختصاص می‌یابد که وضعیت معلولیت و بهره‌مندی از وقت اضافی آن‌ها به تأیید سازمان بهزیستی رسیده باشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/671783" target="_blank">📅 17:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671782">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5784417b.mp4?token=bk9OmrZlN68QiVQEOCClzEWId6GM2oDKPWFUv1B9W_twPRrV3Zzac_YwTwBQ_KV72CPLrEMtwAVsBuz_XTYdxQQJzO_bH0_pm_FIjKd1N77zk0tocvyvEoQIHUxXCrJzc_BszNtVbpd4ml6ly2U3Sdi6FsG2OusB6FuNl9jLSsC9Rzu4Qf6sGxZ0cuEN3wS3dagbEb0S9EFw3nrvID0XiCiyyglcgLrdYM9oiRH2jPIjZi-osS92DdZ51FLFjHOwsjJDiBbDBvQhfKs13TlAGZYcZNOEoZCkvC7OqmtHug4ok1oTys3mxf0w3MM8zI5rWBTplh981hTDXOsWUXvIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5784417b.mp4?token=bk9OmrZlN68QiVQEOCClzEWId6GM2oDKPWFUv1B9W_twPRrV3Zzac_YwTwBQ_KV72CPLrEMtwAVsBuz_XTYdxQQJzO_bH0_pm_FIjKd1N77zk0tocvyvEoQIHUxXCrJzc_BszNtVbpd4ml6ly2U3Sdi6FsG2OusB6FuNl9jLSsC9Rzu4Qf6sGxZ0cuEN3wS3dagbEb0S9EFw3nrvID0XiCiyyglcgLrdYM9oiRH2jPIjZi-osS92DdZ51FLFjHOwsjJDiBbDBvQhfKs13TlAGZYcZNOEoZCkvC7OqmtHug4ok1oTys3mxf0w3MM8zI5rWBTplh981hTDXOsWUXvIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک خوراکی خنک و دلچسب برای این روزها؛ با طالبی و انبه هم عالیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/671782" target="_blank">📅 17:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671781">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
انتقاد رهبر انصارالله یمن از کشورهای اسلامی: فقط بیانیه‌های زیبا صادر می‌کنند که خدایی نکرده آمریکا و اسرائیل عصبانی نشوند
.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/671781" target="_blank">📅 17:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671780">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4a44f052.mp4?token=ma3BTVJmcxfAMG4aDs1HMCCrtz7ARuqsjdGqnA61kwwrsRqjfRNa_L-EevIMNc8OqXzCVf3WyzgtUlZzQkUInaTRMJ4LAuBuYHRxCKRV7fe4YpCJmtWfMDk_aSX5rm4e-AMcW8VWF7QMueslJA4wcsSPdqkgiDX8O7Mv7cC6STLL-8Y4eOk1jetjKGSMUBkcTQxsQqCMsjjy7F-YAiRHwgoHkmqd-LM2SQDfsSHmcuFQJK6QaFhpTbUPqcjVxEqxpUUM5InL8K-m9s3DUBfxy__PDPVZMtBpLsOe576UMLuvlLkpzWvJ6RlPE6IvnJCFUGWAy4UUnzEHv1UOUI9HrDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4a44f052.mp4?token=ma3BTVJmcxfAMG4aDs1HMCCrtz7ARuqsjdGqnA61kwwrsRqjfRNa_L-EevIMNc8OqXzCVf3WyzgtUlZzQkUInaTRMJ4LAuBuYHRxCKRV7fe4YpCJmtWfMDk_aSX5rm4e-AMcW8VWF7QMueslJA4wcsSPdqkgiDX8O7Mv7cC6STLL-8Y4eOk1jetjKGSMUBkcTQxsQqCMsjjy7F-YAiRHwgoHkmqd-LM2SQDfsSHmcuFQJK6QaFhpTbUPqcjVxEqxpUUM5InL8K-m9s3DUBfxy__PDPVZMtBpLsOe576UMLuvlLkpzWvJ6RlPE6IvnJCFUGWAy4UUnzEHv1UOUI9HrDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: عربستان باید مجازات شود
🔹
عربستان حرمت همسایگی را نگه نداشته است و با نظارت آمریکا، شراکت انگلیس و با همکاری اسرائیل از ابتدا علیه یمن تعرض کرده و همچنان ادامه می‌دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/671780" target="_blank">📅 17:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671779">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
توهین بی شرمانه ونس به ایرانیان : اگر نظام ایران سرنگون شود، ۹۴ میلیون درمانده تروریست به اروپا و آمریکا سرازیر می‌شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/671779" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671778">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_48phjmJfMSIQczm6rdvj0_2AG3Hw6VkahrsUgrHmxsR1y9ehQ1zxQn5C0plgkNKXKF-6SmX2En4R87LkQuQ3Gfw7UCO-XFEElspgOohH6U2QQ7qPy8qNUvinbF8gCTrr2pUZKmPZWvq49DUiFUPnfEv7A0rjIlf_smLJbyS6YkpzIYHNQIthezLZtMrFD8f72iAuRrtuWGXkM-enXNkbyFaZhq6tIpRpv0y1jMC1O0fTpvwFaemumyW-fTKqStk9Fr1rZtbBOypAnE_vj0rXLXgnVUcs69POk7NKQ-bCb7FUOb1Gr-6jETjvszau1CFW5hY29tVMwCjL_0FmRP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت داری؟
پس مدرکش هم باید باشه.
با آزمون تخصصی آریاداناک، مهارتت رو به گواهی معتبر تبدیل کن و برای استخدام و رزومه یک قدم جلوتر باش.
✨
آزمون تخصصی | مدرک معتبر | رزومه درخشان
🎁
کدتخفیف: aria25
🔗
ariadanak.com/ariaacademy
📞
مشاوره و راهنمایی:
۰۲۱۲۸۴۲۴۵۴۳
۰۹۹۲۶۶۶۸۴۲۴</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/671778" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671777">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa86c532c.mp4?token=GLx9hPk4oAK3JAAbnHuyesGWmbuE-h3OvNPPrshDAa3f1s-G95-haWBE2mR1KAZjoPKuiWJmsXgbOPVs_gTtVrZR4F-dki_C5qOjbOMtgLz4pLf4jLTU_Bp1_MxKpf2N0LZEpUFQg2lxYRm96Srp1NltkO7eplN2pO0gHh2q6G_dSfR8_rCRlRlvIf91cEuNOiEVQIDGlR9Pi2ahNYsIjXQlxLqH10XYWQ-Id2VS89Ib-DxFMmAgPf5W2J-3yvhQZf7l3FQ4H30y3GpJfkXHjAmkL7iAaIPS_n85cSYlJi8MNdUuFEkynWFB3KD_VZpkg9s8yE_Tugb8XByxfIh6Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa86c532c.mp4?token=GLx9hPk4oAK3JAAbnHuyesGWmbuE-h3OvNPPrshDAa3f1s-G95-haWBE2mR1KAZjoPKuiWJmsXgbOPVs_gTtVrZR4F-dki_C5qOjbOMtgLz4pLf4jLTU_Bp1_MxKpf2N0LZEpUFQg2lxYRm96Srp1NltkO7eplN2pO0gHh2q6G_dSfR8_rCRlRlvIf91cEuNOiEVQIDGlR9Pi2ahNYsIjXQlxLqH10XYWQ-Id2VS89Ib-DxFMmAgPf5W2J-3yvhQZf7l3FQ4H30y3GpJfkXHjAmkL7iAaIPS_n85cSYlJi8MNdUuFEkynWFB3KD_VZpkg9s8yE_Tugb8XByxfIh6Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فواید لیمو رو از زبون خودش بشنوید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/671777" target="_blank">📅 16:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671776">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دولت هند خواستار توقف اعزام دریانوردان به تنگه هرمز شد.
🔹
حزب‌الله لبنان: هرگز سلاح‌هایمان را تحویل نمی‌دهیم.
🔹
یمن حمله آمریکا به بیمارستان کودکان اهواز را «جنایت جنگی» خواند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/671776" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671775">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
آتش‌نشانی: مشاهده دود در منطقه ۲۲ مربوط به آتش‌ زدن ضایعات بوده است
سخنگوی سازمان آتش‌نشانی تهران:
🔹
منشأ دود مشاهده شده در منطقه ۲۲ مربوط به آتش زدن ضایعات در یکی از کارخانجات تولیدی اطراف تهران بوده است.
🔹
این حادثه هیچ ارتباطی با شرکت مینو نداشته است.
🔹
مشکل خاصی در محل وجود نداشت.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/671775" target="_blank">📅 16:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671774">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
هرگونه شایعه درباره نحوه فعالیت مدارس فاقد اعتبار است
وزیر آموزش و پرورش:
🔹
برنامه‌ریزی این وزارتخانه به‌طور کامل بر مبنای آموزش حضوری است؛ شرایط کشور در تصمیم‌گیری‌ها لحاظ می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/671774" target="_blank">📅 16:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671773">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eec695808.mp4?token=tRPJYbjTRAwPMIQnJElHJpdDLHR8XV1-bCvaBxMzOdtx1h7pPfVZs8kdtud0DBCikH6BFludMe3yjSPDpoqLn2oeIpkwUR9k29G5ecYZLcrE2JL7wNtXN1Q-JTvBrWV4ujULsLcWqye7_YKF5K_jNKleHVGn7QWYypb5cv7i-MGnM6JrYpgKeyVWlmiuaABioQ1k2MBS879XeJudyHUL6hcMVdhsLRPSOcT9Tv3DV9fmIA1S90Rj-48NMu_xW6tcQc6CnruegEDQ5Y2HLk9wQCCoT35fszEW9gYOCL27XXglM9tezAWXUkxEqErDIxT12e1Vbeo9M_vKED9N4o6J2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eec695808.mp4?token=tRPJYbjTRAwPMIQnJElHJpdDLHR8XV1-bCvaBxMzOdtx1h7pPfVZs8kdtud0DBCikH6BFludMe3yjSPDpoqLn2oeIpkwUR9k29G5ecYZLcrE2JL7wNtXN1Q-JTvBrWV4ujULsLcWqye7_YKF5K_jNKleHVGn7QWYypb5cv7i-MGnM6JrYpgKeyVWlmiuaABioQ1k2MBS879XeJudyHUL6hcMVdhsLRPSOcT9Tv3DV9fmIA1S90Rj-48NMu_xW6tcQc6CnruegEDQ5Y2HLk9wQCCoT35fszEW9gYOCL27XXglM9tezAWXUkxEqErDIxT12e1Vbeo9M_vKED9N4o6J2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تقابل تاریخی در فینال؛ مسی و یامال: از قاب سال ۲۰۰۷ تا رویارویی در جام جهانی ۲۰۲۶
🔹
سال ۲۰۰۷، خانواده لامین یامال در یک قرعه‌کشی خیریه یونیسف برنده شدند تا نوزاد ۵ ماهه‌شان برای یک تقویم خیریه با مسیِ ۲۰ ساله عکس بگیرد.
🔹
۱۹ سال بعد، آن نوزاد و مسی، حالا به عنوان رقیب در فینال جام جهانی ۲۰۲۶ به مصاف هم می‌روند.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/671773" target="_blank">📅 16:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671771">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLhiQm0-vkXQYt55g9zC1dt5Ofum9UbeHMf7zr8Fbzh5JC9-2fHo1Rw5SVB215GH4fEqgiw1bOwQp9GY2CZasVA3V3hGHG9N_MrVMatzYL97XlyT18U_6YaF98gVVIv1XulQ-nnYHSmSbAIK-UNebzfQwv492AgXkEmnXluCHkgOHJmDaWdMXUPl7vodK9tlrZtKE0gjWLZnuIMS8wjLRXj1jiLBEhwaP3iogsyRgIHB6q8_LvHEmJhS5ELm6XdNVmCq0LZWY__9eYGXIQgpwbBtzPClT9DjWbjkiDp_eciARXqC8L-DFouLs84Yf2IkOqdDuEGLwoEo8lMwC_-9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سایپا محصولاتش را گران کرد!
🔹
شرکت سایپا امروز به صورت رسمی قیمت محصولاتش را ۲۱ درصد گران کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/671771" target="_blank">📅 16:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671769">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCzUxX3QJ3zlaDBFiT5RxX5LTza-m1HulhyMhxrX4Sib4Tr_5SVyMz9voBrCDVIZRp5p3_nIYDDn1fPEnVWFHv2HT9VYcv5IPGJn4cZQwprETMqDn8X6PX7ZRMDmletovszuPFA0HK2aD0zJZWhYkibLINj0a8RasSg2uXaHmsUkWsCfNdeetJV-njNCd-nDHUUVPpFWhUzYm0hHF4nEh8nmfSCWAU2Oyfp5TGKWUAwkBTigcdrurPLvThjeBjetujyhr_e3ZJzRr8HorEkW7QOC9TVMeWSFsZZqMHzV1E4Pop9g4pKuphWhOFEArukVlnKriL9ZMKbUUPnjOFlEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بر فراز دهانه دماوند؛ طلوع ماه کامل در کنار سایه زمین و کمربند زهره
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/671769" target="_blank">📅 16:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671768">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbc5724b26.mp4?token=hfpIZbI_XMsQuOofBXmB9Uxpc5GxTcGNg0cb1kFi11KCf_APG33VazRyhGXDaWT57c-oAdkiMS0dWN8ygNTAEIq663ADIPJ5F266tLNCXEzS2hxAIRH1Wfv31MD_pZN4o7idDclTvknwcqeIcs7DffzjJAiDskmSRcAOIudLQPpEIc3Zkh9yT-XrZdqNssiHEh539XczC_Uzken7pmm_yZA1eYS9u9trFv8PFbwFHno_WXjhOzoRoKTqqtoR-LvFjTDvGkpWGEfUxBj6CmiMFP3FnW732mBplVr6lSH0PPme2Xryo0HqCqOtCk2TMMla3szY2T3WNvkIa7_zM1_YGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbc5724b26.mp4?token=hfpIZbI_XMsQuOofBXmB9Uxpc5GxTcGNg0cb1kFi11KCf_APG33VazRyhGXDaWT57c-oAdkiMS0dWN8ygNTAEIq663ADIPJ5F266tLNCXEzS2hxAIRH1Wfv31MD_pZN4o7idDclTvknwcqeIcs7DffzjJAiDskmSRcAOIudLQPpEIc3Zkh9yT-XrZdqNssiHEh539XczC_Uzken7pmm_yZA1eYS9u9trFv8PFbwFHno_WXjhOzoRoKTqqtoR-LvFjTDvGkpWGEfUxBj6CmiMFP3FnW732mBplVr6lSH0PPme2Xryo0HqCqOtCk2TMMla3szY2T3WNvkIa7_zM1_YGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشف لاشه پهپاد متجاوز MQ۹ ‌آمریکایی در دهلران‌
🔹
یک فروند پهپاد متجاوز MQ۹ دشمن بامداد امروز توسط سامانه نوین پدافند هوایی نیروی هوافضای سپاه در اندیمشک رهگیری و با موفقیت منهدم شد.
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/671768" target="_blank">📅 16:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671767">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4pOjC8wMxrnHbNm2M5V-JzRqoJw8Jok5gEJ8B2HZcndvJoQffw_E6KPxUZqLjl4NaJFkUBP1nUwnrUj3mILTma0L6cKa8nVV1p8GK6VGTbmGItAvfbguN2z4slnzuLxVIsTZEQSqu1wuH9sDmYZMda_G11n1AEuoB-1wh6bLwklWcfkP7yvTdmC_gyEBrykx8Mih5dHOIPIg1wZGwweWTNkkq9F-ID5a7Q-pLE45kMFnJxlC73k33_4UD89u3X1m4PYeYr_GeSvbMSiv-mk-oy4P7hgmU5emznEHus88u0rwwDaG_Q3z743zwF97hDBybHHWEr9bhbZ-S-Y33EgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام کشورها بیشترین مناطق خودمختار را دارند؟
🔹
روسیه با ۲۶ منطقه خودمختار، بیشترین تعداد مناطق خودمختار را در میان کشورهای منتخب جهان دارد.
🔹
پس از روسیه، بریتانیا و فرانسه (۱۱)، ایتالیا (۸) و چین (۷) قرار گرفته‌اند.
🔹
منطقه خودمختار، بخشی از یک کشور است که با وجود قرار داشتن تحت حاکمیت آن، در اداره امور خود از درجه‌ای از خودگردانی و استقلال برخوردار است.
@amarfact</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/671767" target="_blank">📅 16:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671766">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: هرگونه تعرض به ایران با پاسخ قاطع، مستقیم و بدون تردید مواجه خواهد شد
اسماعیل بقایی با تأکید بر آمادگی کامل نیروهای مسلح برای تمامی سناریوها:
🔹
ایران در دفاع از امنیت ملی دست‌بسته نخواهد بود و همچنان بر اصل «تعهد در برابر تعهد» پایبند است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/671766" target="_blank">📅 16:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671765">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3db11da08b.mp4?token=PDAge_zPFt0NKrqLLgywmCP1Jr1BkAMcg8Il3PXQDaLEDFCVexY6GXQ43tKqpQot9kicHvnQ2nYFp9z4Zq_QIozmX6Mb-e2hFBHPE1EjZN3ziYav5y1-3sPvKVi4AHwliN4cELK3X9jTSTQgud0xK0DSjWuAx6hhkgAXf2LHg7VGSQg-W-hKN3mYIP4pDWomcVVaDW6zi7dKtaDXPCOL1fR_EmQUdzFaxkBYjL2YIAeknHdM7E5suWwO7RuSKgu1KayWbhyPpfWDhQ9LxHDGBDalJ7fSfDIJ6YrINBBnuN--2muFUfzKf5HTgH9rJYMrqphhmzjYpZeoHw2FkVvSow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3db11da08b.mp4?token=PDAge_zPFt0NKrqLLgywmCP1Jr1BkAMcg8Il3PXQDaLEDFCVexY6GXQ43tKqpQot9kicHvnQ2nYFp9z4Zq_QIozmX6Mb-e2hFBHPE1EjZN3ziYav5y1-3sPvKVi4AHwliN4cELK3X9jTSTQgud0xK0DSjWuAx6hhkgAXf2LHg7VGSQg-W-hKN3mYIP4pDWomcVVaDW6zi7dKtaDXPCOL1fR_EmQUdzFaxkBYjL2YIAeknHdM7E5suWwO7RuSKgu1KayWbhyPpfWDhQ9LxHDGBDalJ7fSfDIJ6YrINBBnuN--2muFUfzKf5HTgH9rJYMrqphhmzjYpZeoHw2FkVvSow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیو وایرال شده از میزان احترامی که تیم آرژانتین به مسی میزارن...
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/671765" target="_blank">📅 15:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671764">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZ7axM3vb-O4OJXrnalGRSmISVn-r7tXuhDvYe114pHWidP5gC3eyEHcqZI3yl3J8CLksEapLshi5PI6UXcV4ijoeCs1KlepWMflUgp58DafRc6rtG6jibB5e4qVUA1cMN4XR7gFmuOYDnmbzRNB0f3JHLwJQHs-5zz-xtKRCBn9pxegrP7zAWU5CTmPimLv3Zj-s0x6af_9CdUCGVI7K2E741okWwPv4TTFhNa2_9ookr2asDOQSrcY6wKsCxD5ngWnn_xL4zSnOO5Yldeyl2_ylUpu3ypISW8i5VQ6GpmvRFejm-34DMAD_bQ_dFoZUz-UsYP6caNndw6OvaJrew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
کالکشن ویژه تیشرت‌های اربعین «قرار»
طرح‌های مفهومی و مینیمال، مناسب روزهای اربعین و مسیر عشق و ارادت.
قیمت اصلی: ۱,۴۵۰,۰۰۰ تومان
قیمت با تخفیف: ۹۹۰,۰۰۰ تومان
تعداد محدود؛ برای ثبت سفارش پیام بدهید.
🛍
سفارش:
@gharar_order
👀
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/671764" target="_blank">📅 15:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671763">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU0qTaBBuuShOvv7okeRSJ9jW7h-mFBTlzAfQZk45JFT6Ff9RbjVZ-_Ee3n3ehQQ1CeZ5rLXsbiGH56k5bsNsN46qME5IPMa8jAx9LIlhc7yYFyfyuQal4U4sAbPo8_Es2QJy52MqAr1lW9Npkgqlkq-M0wahvaWF0mrtqKrgbBXEDwWRxB1YPnBEG8YMoD7GMTpUbAh-8EoeP-K7gnha0cEvW1fwNSqD_k9LCXpo7EOdVXkymzMjg-YNBxpmrw1Y243uXs9AHzTPs3cI9u5InJBqAIrcPfa5iW06XyWUy3ZE60hRudA-jy6SFpIUlmPxhpsmBXOWbxEMwKNlA1jTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چطور با خرج‌های روزمره و کوچیک سرمایه طلایی بسازیم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/671763" target="_blank">📅 15:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671762">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8c13c9ef.mp4?token=fZc2_aO4Vc1nrRYRfurZdM4MlLXutwFohP7jf37SZO5tVGaz0nGBWrwHhwHPWESbNfViB63IAUJ3psOH0vU-x6tr-MD9F7EfeaE5hxgrJXWa5nzssNQh3SL6sDSmW7lHSW1tn2zwWyr4AYpyAm2zNEAWTk2zLalqzlV4P3VfzXjNkJg5K1AuPV05QpWV6F9V7JsrbsYt9OxWk0y_DPAUVEd4HUhW3WffQllZ7bsuW4EF9IVmfyg_ZUR51hVTwHfHFf4l-9Upbg8lXalmV_x90svEMYLbJuWUVg0-wKM651bWKh-MBszxfOpCa9J5m9xuV6IWLDRozJd8Y0yV3Jnirw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8c13c9ef.mp4?token=fZc2_aO4Vc1nrRYRfurZdM4MlLXutwFohP7jf37SZO5tVGaz0nGBWrwHhwHPWESbNfViB63IAUJ3psOH0vU-x6tr-MD9F7EfeaE5hxgrJXWa5nzssNQh3SL6sDSmW7lHSW1tn2zwWyr4AYpyAm2zNEAWTk2zLalqzlV4P3VfzXjNkJg5K1AuPV05QpWV6F9V7JsrbsYt9OxWk0y_DPAUVEd4HUhW3WffQllZ7bsuW4EF9IVmfyg_ZUR51hVTwHfHFf4l-9Upbg8lXalmV_x90svEMYLbJuWUVg0-wKM651bWKh-MBszxfOpCa9J5m9xuV6IWLDRozJd8Y0yV3Jnirw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توقیف کامیون در هرمزگان؛ راننده دختر ۱۰ ساله بود
🔹
رئیس پلیس راه هرمزگان از توقیف یک دستگاه کامیون کشنده به دلیل هدایت توسط یک دختر ۱۰ ساله و به خطر انداختن امنیت ترافیکی خبر داد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/671762" target="_blank">📅 15:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671761">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d221f37fe6.mp4?token=gpEi74TTnEjP34XHTCwDcm3DJAjyZlmEPgJUA7R1sBzsCiSHgsx9fd2pUp31ifVtoWl7H48h5TckI9wyaFTsJxw9oUM1A8thK_iftwdHUlRf4iHEiV9ZLWRD1CS_YWcfUuihd9TDqFYFqY3A4CZFB9JmBxyHysN_aITc3u3aL0ubJGSfM8yeTbdk0BPOF02PkbSRumSwyYmaPmRjVw4VF2hd3RFhEOgWhgtWNa95Q0GACSIkcMtl-HAVrwrLzFlmft01EMfgfFzH-8JVTnQ5TqP8t7mEIsJD6i8VhzFlmXNysGi0yMsipZTCDC5OnNgLCeo8BhEq1dp3e583MGXh1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d221f37fe6.mp4?token=gpEi74TTnEjP34XHTCwDcm3DJAjyZlmEPgJUA7R1sBzsCiSHgsx9fd2pUp31ifVtoWl7H48h5TckI9wyaFTsJxw9oUM1A8thK_iftwdHUlRf4iHEiV9ZLWRD1CS_YWcfUuihd9TDqFYFqY3A4CZFB9JmBxyHysN_aITc3u3aL0ubJGSfM8yeTbdk0BPOF02PkbSRumSwyYmaPmRjVw4VF2hd3RFhEOgWhgtWNa95Q0GACSIkcMtl-HAVrwrLzFlmft01EMfgfFzH-8JVTnQ5TqP8t7mEIsJD6i8VhzFlmXNysGi0yMsipZTCDC5OnNgLCeo8BhEq1dp3e583MGXh1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاسمین کراکت، نماینده کنگره: ترامپ احمق مناسبی برای نتانیاهو است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/671761" target="_blank">📅 15:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671760">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3762a04834.mp4?token=JVog2HCA7b3L3Y77WxOY8lr_Go29rgbdcgxy0buv6yP6ECCrkgaWrlZ_dtLUsnf8GjQcvjESKZdn7IBrvyy4y_3LuhBr3GUK792pNknar5-mgLGs5Ab4t1yuqqlfRQCqfltAauuyhMln8sOAq1TCRNx_hkdVnAy7Yu50PgnnxzJWT4TXDWpWDJHqGXIhagmw7-EHbiA_u1cdZWz6XP0vO86N2HZDSh_0YUUbzKpWzkF_KfjwsQtUzZxrhOACjUg1vb0wz3gTEiCA2xTe_gDGlqy7eQTFkh8jRZv4EAy5oe3u93SCXzMnKHlUygEoDbVwo3Yrum-OX52ZjcTC-U2wKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3762a04834.mp4?token=JVog2HCA7b3L3Y77WxOY8lr_Go29rgbdcgxy0buv6yP6ECCrkgaWrlZ_dtLUsnf8GjQcvjESKZdn7IBrvyy4y_3LuhBr3GUK792pNknar5-mgLGs5Ab4t1yuqqlfRQCqfltAauuyhMln8sOAq1TCRNx_hkdVnAy7Yu50PgnnxzJWT4TXDWpWDJHqGXIhagmw7-EHbiA_u1cdZWz6XP0vO86N2HZDSh_0YUUbzKpWzkF_KfjwsQtUzZxrhOACjUg1vb0wz3gTEiCA2xTe_gDGlqy7eQTFkh8jRZv4EAy5oe3u93SCXzMnKHlUygEoDbVwo3Yrum-OX52ZjcTC-U2wKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فینال جام‌جهانی؛ بازگشت اساطیر در راه است؟
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/671760" target="_blank">📅 15:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671759">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ادعای مؤسسه کپلر: طی ۲۴ ساعت گذشته تنها ۱۳ کشتی تجاری از تنگه هرمز عبور کرده‌اند که از این تعداد، فقط یک کشتی از مسیر جنوبی (نزدیک به سواحل عمان) استفاده کرده است/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/671759" target="_blank">📅 15:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671758">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
مدیر بیمارستان شهید بقایی اهواز : پس از حمله تجاوزکارانه آمریکای جنایتکار به اطراف بیمارستان، موظف شدیم ۲۱۱ بیمار بستری را جابه‌جا کنیم
🔹
تمام تخت ها و بیماران بیمارستان شهید بقایی ۲ به علت وقوع شرایط اضطراری تخلیه شدند.  #اخبار_خوزستان در فضای مجازی
👇
@…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/671758" target="_blank">📅 15:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671757">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس فدراسیون فوتبال: نتایج تیم ملی در جام جهانی مطلوب بود!
🔹
مدیر آژانس بین‌المللی انرژی: موجودی جهانی نفت خام در حال کاهش است.
🔹
وزیر جنگ رژیم صهیونیستی: از لبنان، سوریه و غزه خارج نمی‌شویم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/671757" target="_blank">📅 15:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671756">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2569337d78.mp4?token=JYkWCAdTR9Shs1m2QHC-CVm3B1q62nMVxPytBnaTiIUSgiGyiju5JLtf0jQDp62s_5J1pWJmf7w2ERXDfRTsdVXr6TTyuXAtBRueHefKtv6fx_Nn-TKOPRpNRwLHaa2bPRgkgUXIS12lXoTjn7YE7F0dI0hgup3JnrgY3o1fNcq8Px2d52EOHkk4uywajYbROeyJShmXSO3MqAuWjpkc4KsxMc8-tyW4F-COnZ6ZH23yJV48I8fvJRJF79xaaTGOad8p1M2kvBLbGiac2chZupjBtsjxYgSC0RlzKQ39r0JmJS3iY4xotHmh4Eh9g8rw2jOm2sEHmf9FJlF3_BC-7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2569337d78.mp4?token=JYkWCAdTR9Shs1m2QHC-CVm3B1q62nMVxPytBnaTiIUSgiGyiju5JLtf0jQDp62s_5J1pWJmf7w2ERXDfRTsdVXr6TTyuXAtBRueHefKtv6fx_Nn-TKOPRpNRwLHaa2bPRgkgUXIS12lXoTjn7YE7F0dI0hgup3JnrgY3o1fNcq8Px2d52EOHkk4uywajYbROeyJShmXSO3MqAuWjpkc4KsxMc8-tyW4F-COnZ6ZH23yJV48I8fvJRJF79xaaTGOad8p1M2kvBLbGiac2chZupjBtsjxYgSC0RlzKQ39r0JmJS3iY4xotHmh4Eh9g8rw2jOm2sEHmf9FJlF3_BC-7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به شهرک النبطیه الفوقا در جنوب لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/671756" target="_blank">📅 15:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671755">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698b4f5438.mp4?token=FYys03G2WYGnL4fowFpQW1tD43HQiVuDMcwruzww2VLqJVuWo16KZsQSsU1rgzSzIM63MsKsLYR74vyCldMP2GuknwMDNo8Vx_pmV5YvzJe4x6DYH9BwqjKMQaeDywWUrl2xvZIox61f0sIU3a82Zq7aQKYbWFvmTn7NeUx9KxTC9f4ssNAp7s0-8Trcc55bWuBR141uvbirckfhdYY5GGeBqBGU7Hr1ZFj89DwHYvYkLbMiQ-zMH5bXYURqT2uoWYPPT9KYH5NDhpWjP0PHDr-YU0ZF-ZrbLAjYjMPE_c5vqbC4AehKk80cADACmf114ppZFTgr4L-KKQeQNcZVKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698b4f5438.mp4?token=FYys03G2WYGnL4fowFpQW1tD43HQiVuDMcwruzww2VLqJVuWo16KZsQSsU1rgzSzIM63MsKsLYR74vyCldMP2GuknwMDNo8Vx_pmV5YvzJe4x6DYH9BwqjKMQaeDywWUrl2xvZIox61f0sIU3a82Zq7aQKYbWFvmTn7NeUx9KxTC9f4ssNAp7s0-8Trcc55bWuBR141uvbirckfhdYY5GGeBqBGU7Hr1ZFj89DwHYvYkLbMiQ-zMH5bXYURqT2uoWYPPT9KYH5NDhpWjP0PHDr-YU0ZF-ZrbLAjYjMPE_c5vqbC4AehKk80cADACmf114ppZFTgr4L-KKQeQNcZVKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به یاد سربازانی که دیگر بازنگشتند...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/671755" target="_blank">📅 14:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671754">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c19qURHjBBQAvn_WdSHqOkqEsA3WIiF9qmarOoc-qf2tUAJa-jf8X0hXuXZoOism1n4DRDa7NYW32h_dpDp09wVyVe9G1S76YRatdG3YqknxvBRhFXHKHqEGAwejLefkA_SXUWCR3Ub5Dm-mZAS_qXAun5Lipa3u82ia-mAfJjO0ZXHkpJgSdTQYDFls1OrUXc_1TvTfPzaZYMWRNnKS-OBN5nDv8r_sycPx20edhPzIZBco7zw1GzWr_aR_GAj79MThlxvUzbnpFZkCI5xOBbGOwEmu6cztWCA3W38Yzpz3SN5DHK1KkhIKdOQnFUJekF218gvb77T5QxR7zJE2pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران در غنا در پستی، حروف کلمهٔ  HORMUZ را رمزگشایی کرد
Hands
Off!
Recognize
Maritime
Unchallenged
Zone.
🔹
دست (از تنگه هرمز) بردارید؛ منطقه دریایی بلامنازع را به رسمیت بشناسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/671754" target="_blank">📅 14:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671753">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
واکنش خوک زرد به پرسش درباره کشتار دانش‌آموزان میناب
🔹
مجری: آیا متعهد به انتشار یافته‌ها خواهید شد؟
🔹
ترامپ: فکر نمی‌کنم کسی بتواند بگوید آنجا چه اتفاقی افتاده است. در حالی که چنین اتفاقاتی در جنگ رخ می‌دهد، موشک‌ها در همه جا پرواز می‌کردند. و نمی‌دانم چطور…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/671753" target="_blank">📅 14:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671752">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
رسانه‌های عربی از شنیده شدن صدای انفجار در آسمان منطقه «القادسیه» و محدوده بندر در کویت و فعال شدن سامانه‌های پاتریوت آمریکا خبر می‌دهند/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/671752" target="_blank">📅 14:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671751">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7ee4b457d.mp4?token=fnxzsj2-Z7tJICzLWcRZO-UUXQBnTO-zPqmXuyiibPBv13GgFKgA45XObgQf1azdmsQUlcIFM3tJMM5lGaLAFkOC98WZSuvTffgJzJBCIle4onEn37RCid3tGsCjGsguNoJgOVjN241nvUMDnDa-qUDYoFL-eoFl-C-B-8qrsDAxuZ7lPpZ4kYwaGuonrxYmbuGtWIQD6uOQf49r_YQdz8CH_JtASYPnXaalV3gC7LLc7Ff1gUqLMWQu36Awo6XR2ybwUnm6oXKc3ZQHhRTfaSQ0LiKmAC_H2nGg9BcD4GTbrtV9XEAAQoYXIyEqBUvLhIuKQxbBbiDelYvp9beK0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7ee4b457d.mp4?token=fnxzsj2-Z7tJICzLWcRZO-UUXQBnTO-zPqmXuyiibPBv13GgFKgA45XObgQf1azdmsQUlcIFM3tJMM5lGaLAFkOC98WZSuvTffgJzJBCIle4onEn37RCid3tGsCjGsguNoJgOVjN241nvUMDnDa-qUDYoFL-eoFl-C-B-8qrsDAxuZ7lPpZ4kYwaGuonrxYmbuGtWIQD6uOQf49r_YQdz8CH_JtASYPnXaalV3gC7LLc7Ff1gUqLMWQu36Awo6XR2ybwUnm6oXKc3ZQHhRTfaSQ0LiKmAC_H2nGg9BcD4GTbrtV9XEAAQoYXIyEqBUvLhIuKQxbBbiDelYvp9beK0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
انگلیس تا یک‌قدمی فینال رفت، اما آرژانتین رؤیا آن‌ها را دزدید
▪️
قسمت پانزدهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/671751" target="_blank">📅 14:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671750">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4358d8bd7a.mp4?token=huKMcZel0MNhyum_m34MIGSI4EbbaHJR5wOJhWDxyr3KhLd2hamEX372QZwNU-5fn1SghXpsf6QLESms8XFcim_uO_UMEmeDyEvnYNxmhnVdzdnLdbMyRRs9SQWA4E1mySd1eJx-ESOFlDWK3Vmmf7AEN83nDtcTlU3b2X0fEfbkj3gNWdixyluaK9DNk5O24CuHcrbV6qaqkf_KfvZWem4KfgCszc6MIb7v9tBm_QTviAXJXNWnCtLmtWorFN_nV_Tf8vhPQXpKZdnkXcPxl8yZreytm-bqPwpExLPM3V0F2pdsY8nJQns9BvsB0QmbbuM-AlFpyeqQZSImVbhpXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4358d8bd7a.mp4?token=huKMcZel0MNhyum_m34MIGSI4EbbaHJR5wOJhWDxyr3KhLd2hamEX372QZwNU-5fn1SghXpsf6QLESms8XFcim_uO_UMEmeDyEvnYNxmhnVdzdnLdbMyRRs9SQWA4E1mySd1eJx-ESOFlDWK3Vmmf7AEN83nDtcTlU3b2X0fEfbkj3gNWdixyluaK9DNk5O24CuHcrbV6qaqkf_KfvZWem4KfgCszc6MIb7v9tBm_QTviAXJXNWnCtLmtWorFN_nV_Tf8vhPQXpKZdnkXcPxl8yZreytm-bqPwpExLPM3V0F2pdsY8nJQns9BvsB0QmbbuM-AlFpyeqQZSImVbhpXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکورد یک میلیاردی؛ ویدئوی آرامش‌بخش ساخته شده توسط هوش مصنوعی بیش از میلیارد ویو در اینستاگرام گرفت
🤯
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/671750" target="_blank">📅 14:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671749">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVTkzTGI9ib2gvke-WuN3Ntb1iXsOhwgAi2kbiHDG46Xe2TibNlLFm2Hyt_UdcAudMETr1ngjIq7yp5mFw-_qUcwdXcqXkXvTpr8MrIPmUoscUgAXTRAw5gvH9V8ncPlul_CRyMyhwrtzzZL81hj6Pvc09gfpIhVltf2PpQ7dSeL49Unad0S2v6P8IA775SLGTLPfHm9QjuRHUPF97JtRJztRsvNyBOQSkLyRMDPYzoaX4hrC2LkRG3wtFYHbFHlFZYLMBe3HVVXrYDk7AGHG2zwM8MkEQHIc673WESpIhWgpCXyxd0L_AVvbgi2rEXeneMm2U2XCCUlamty4AxD4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک نکته درباره واکنش کاربران شبکه‌های اجتماعی به درگذشت مادر داریوش فرضیایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/671749" target="_blank">📅 14:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671748">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EECpz8-wY470oEbiokAg0tR6rKtT3bP1TYrb-whcFgjgBtQdIpJj6OBRQ0nnrppLflg5zp_GCOdOfJ1DD3PBq55UngAEfzhBsw-Fp5kW1DdlLzBOynBF7dQVRU6_DuHfKip9gyVlGbBJgOXP6E8XoZSZha7h7rWqu2kRmDvMWnipDbNM3-Bb0NDMdl47-QpfBW1wqZ5jKn8iLyTRaJkP9wNlUIRXFHWJsvwujmAQ5woxG3IlOCcXwBGbZUW6j68q_Xh3FOBkPpAYqTL5d3rZeJYo88WV3E_FElL26ulF5l9CCFhN5-O-aihUnN2G-Zpu-AwVNH9FSjG99TRZqiQQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس‌لرزه‌های جنگ بر صنعت بازی‌سازی کشور
🔸
۷۶ درصد اکوسیستم بازی‌سازی همچنان درگیر چالش‌های جنگ است.
🔸
تا خرداد ۱۴۰۵، ۴۸ درصد از استودیوهای بازی‌سازی کشور ناچار به تعدیل نیرو شده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/671748" target="_blank">📅 14:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671744">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0nvbLf0CFyhD7uGOPG_MeStKxU5An9_38dwTUZ2mRZeKuu8YyCT9RtIEIdQxIlLpTy2j012mj0rqnceTwcTAy3uaUKM5WPjZQb4IPpyFGz-uoQnPcuOoy6LFhPMd6hAjjU5Mt5E13C5E4XgM7X2HPv2m85EgjDHlme6bt2uuLWH4Y872mQfq5-IyMDlOmAwEYtTmTiCQQmWPPKJSD9ycILtJcDEt47R2GgOOA7UbQLXS7j9c54Uq-nDYLBfgKQ_HF3Io_UXYE-3Mt4vh3pv9koEGOewv-td3t0cdGaMSH2PBiFGojJTS7kJdc1zxjhAyHjnULpsHNBdyfR8aIymmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZbwxpA28e7qi84BesFpuqh_do-1s5orFkWQgDnYEN5iBeJcKo_SFGgBMjh2tQkCXGTYJEIXMqSA80Dfyyu-eRAtCU4CVtZz0itCaGoNx5nvgzajIJd5qNHJtYAtJgUuI8-29FaYYVcPndwlNpOJf8_tdx3EqyCMWmJP5AhtgcXoK8lTj3Lr7W1sGFeFKPqgTJsiKoqdPcsJA5KCiMTpF9oSmhRTOBb850GNcbcot2AzmEu3GfP_WmPmOKGNXt-X4qzeoEGMSKTWX-l8cZixfpUIX8X0mqtq_5hIE1wGwScuxjKdNAxiSAO3-_6cugDemXJvMNqfc1rsdfUhdX2hnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OqJ_pCwvPMOYaeGtFfV557if6pxBCSspq0usKyKGwIp48W9DvAKNDEbZARDCYi71zriR3tELgJt_GMQaZsi3u8DDhClJL4xYUzAlg6KQXSsMCrpCGFJG0vJ57VLKiU-jyeA1Xfg4ojxiAM6ZPWSAPtE-vO24c7WLDy1NmALm5c2tbXGo9cuJW7oSpls22z_0zrkGoZNy9kw8g6CmhrOyPGMGPDiIEeTLb9WhU8_6ljjbW5kKao08N_JCP_UPiKyGEY75R_Dv1r_OmtucMgb_jWZCyY88f-HcKH9JGAWPgbLO6KtQOHkYjPD-6BO-jCjS8VsjNWYLp_pg4Qi8W0I9Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YzPVryjUID4oCcGsi5quiFO6hSehSeKF5YeC56Kvg09w4yuquJHd1FbKghDcm_qRbNgrFqgt5fv4yk22-7nZb13ianQwR3Rh_njCm7KA-q8bErRrHG9b-9CVBWzuQ8Hn5bWXuuxVbCKqlhnKPeLyfCN8Bzi3QDHcQv-_S3D2Vjyxx7cnfJMRWsBxePghRdRxMNSy4fEB8Z2CMLdEDB8N5bkHGwDjaPk8n9KyuKWb5mj6T8OUY_0H2HiZDoXctBH0BFyFXlUJsS8RdgCi8s7qqSWP0uaQAORJUrg6g7vRxF6xf3WpxIx-m2UIyKy2Oy1AuUGqrNCf-S6lq5KhK3DtVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این راز ساده، استایل شما را چند برابر شیک‌تر نشان می‌دهد
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/671744" target="_blank">📅 14:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671743">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
تیزر قسمت سوم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ فرهاد یزدان ستا که به دلیل ناراحتی قلبی به طور ناگهانی در منزل روح از جسم جدا شده و خود را در صف بسیار طولانی منتظر و مضطرب می‌بیند و در هنگام عبور از درگاهی، اسم اعظم خداوند را بازگو می‌کند و از خدای مهربان آمرزش و دادن فرصت دوباره جهت جبران اعمال و بدرفتاری با خانواده و اطرافیان را طلب می‌کند ؛ نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: فرهاد یزدان ستا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/671743" target="_blank">📅 14:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671742">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
اجرای عملیات آفندی هوافضا سپاه علیه مواضع آمریکایی در موج های هشت، نه و ده عملیات نصر۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/671742" target="_blank">📅 14:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671737">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pMaONJpD7saiWP5FzWx9CCfYboYjOi7bJxlVekdqrr7Bpg7TFvBk5URy2G6_PvUzuSLCkIuZBO7EdKlXUc_Sh9ufuCyOxDsR4NYhnVdAmQNB2IFvNtsgdwfsFwfhLGqyLayufZ-jkmyghkCQIu8w1TXWsNNlBe4vSeLfm-xzR-fT_WGgOzEgzhe6dV3eYqqbbEhA1ivp0a3VY71yxyHiXK6AMQeCURgVqSdMsd3HgmGkWvMAcQq2O0vJ1_as4hz4libCIuU2wKZwBrngNf7YuSYzjXyZ0cYlf_czc3-IPcW8G_DD3SxFXSOT4PeRcJihf23CFqlXmUx9XxneBm7cxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJo_SbLSwO2J4H52TN5a1C9jh_FNSRykKGcuDpxVDAC_5YkT4yh9pNEAUBM4s88RD_xhdmB8_7XmGWFB7pihY3hQLPBi6U5wDG5Y6G04oiXFHfFsAmNHWsbrRMb2gcUlF72qDKaHvF-qLU-XYMI0LkayRWRPBdQX9dNvXU7igeDj31RPB3Ga7cUL2GWh_i6tkqDAd2MqtC7d4NFhCeAjqGHBBMfOxuOLBj_9botuIYEu5fwNFnAo795uh0vvXXm0h14XLG9ouH-dpgJyaTj9-lK9Pl5IF5PA3q3spU-4t-Ay-WZ5c_5n3WbpGfXvC-NAZzJsnZ3fLEVd9vIxHApSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgVOA1PowBUzAtd9rWnYMhGvF3cSEGgBITXlCFQGh1WzeKw--uETYpAB5C7mf5WIFYc6PShMMxQuKuybkDcPlI7YuvuBPsTqQcSqwY7Ju2h-nybXld4oPvzxlg-m1s5PzUpwrhZV_GZxsQ_wtB_aAk2HV96pv_xsE2u4FaEWhFPmbdckVipW0_GKi4Hxq6FgSu7zMVTFLUxRz6olYBbvSqZg3qHntX7F9UDtOm8kJ0zaiu6-gJcXbt2i28hikG1p-77CLm2IczX9XIcI2IU-0e_lMAgaKoPBBbron9_ndHSeLJfIvTQcCICv1ZPiHzQmy-IbP4BfvZrTV7GyO22W0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLqSZ0c8B5wlcnw3p366RlEPSeZpfI8f0aQtioziKqP_FSI_bvF_xf6AUJADG-bbAcX_hEs6_y3oqQ2eMpy7nbaiAveNO6v6-DGaW0VzF5ZoSmPTHSHzPv7WNgyGLJZaFV9xWzrPGqPwves20Xez-1iEtcJNkeSrXWwng4LWb8HdpyD69rWcpPhKO_B6mpyO4QA_lZRDMTeXwLkSgdEdU6uLfVhFsMnY6bUn3sI1aYqWVAIKknYH05gItblg0oSCIoW9aAUk1X0E50ULHGXsQCZxNm8HI_asUUGbdlN67sS10oCU7tUyispy9OKfREYqdi83zN81gKfeVdbrULauHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYcKTVOw8Xx-4JA2YBNhN9_xTBwcvTPUTeHXitOBFCo1CvmZbqX9wzMJPjylrTHESk1OA8-4ADrNSqd0p3YZ1bLlCBs8yIhfHowaQvnk8nzoisfC9YzUnPpl1oMh5dDoB7bSPS-aJUjBaeKlG7U3B0q17wzlEZizidgb3xMoKGUEPWORec5FoMS8oz9OsIObL_nVcp_wfqw6yD7x93FDgWUNiqy09T3Hz66_pKW78S2uzgL29B3-xAfrNBONqi4S1EjgtuOMMhAoygjYlkKMxI4TsrsWRBUL8oTblwzKvo4I9BxSIs6eivCBmLup4wCjn76LnmtlpatDW_BsdI723A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دود آتش‌سوزی جنگل‌های کانادا، هوای تورنتو و نیویورک را آلوده کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/671737" target="_blank">📅 13:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671735">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY6Cfk1h7da1VJn0VRMo1Sn1Wcd6NfEk2BP0XAwLX-ygkaP5JTqIbDasR1auWAt04kv5fZn7t9mCC1SCdWa74-pyr2LISfvrmk7Ri1L2znAFPYP9h8cwmUkrrt0hrV-oxT6QcTY6bVMnakuDkfPJGrTf-EltKMgO0v_97AnWiJ29z3F4UCsS6so_ej_o0nxEwSGnQpkNtymEjwALsHYAXp0QtOoTG51ZJCMcccp27SRvD0KdPGafHR8JnsMdtvOl2WbXPJgG1l_2SqhbA_nJjM7LtqAu4hycZoEZKc6XxsDcqdp-bbrFWSQvq7lpeLFdAOP5k9tFDOkmzpYFsWuA6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیر بیمارستان شهید بقایی اهواز : پس از حمله تجاوزکارانه آمریکای جنایتکار به اطراف بیمارستان، موظف شدیم ۲۱۱ بیمار بستری را جابه‌جا کنیم
🔹
تمام تخت ها و بیماران بیمارستان شهید بقایی ۲ به علت وقوع شرایط اضطراری تخلیه شدند.  #اخبار_خوزستان در فضای مجازی
👇
@…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/671735" target="_blank">📅 13:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671734">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b5af118ad.mp4?token=jNeFHsCxxOdVylX5EvastTisO2JwnlHTLqPsm0PCl0D5USkW261fitaRHn84qVI1oKHszRO6EDgNNMgnj2nH4l4XMWP4fYGIRRDsVYMPUddQvZiyxXbhWMX9cHeqV1Aws4YKMsp4shaINaz-CzSgqgwGnIrSE8FQfaSLTFW8I4GvLRLW6WMQzxuhsActBKGcPuFapu9TZ-74f3Vc1UsNiVCIwHCVXzpPbwlGOA9o3mMtv20FVwHhtvZWID-nYev2McGoNEl1Nz7atS1b1fEu5wIQXnXCf6n-o7o36BPapw1rYBibtN9dVW7Xva_oJNYnh91vC6kiVmXpfi9GaIuwqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b5af118ad.mp4?token=jNeFHsCxxOdVylX5EvastTisO2JwnlHTLqPsm0PCl0D5USkW261fitaRHn84qVI1oKHszRO6EDgNNMgnj2nH4l4XMWP4fYGIRRDsVYMPUddQvZiyxXbhWMX9cHeqV1Aws4YKMsp4shaINaz-CzSgqgwGnIrSE8FQfaSLTFW8I4GvLRLW6WMQzxuhsActBKGcPuFapu9TZ-74f3Vc1UsNiVCIwHCVXzpPbwlGOA9o3mMtv20FVwHhtvZWID-nYev2McGoNEl1Nz7atS1b1fEu5wIQXnXCf6n-o7o36BPapw1rYBibtN9dVW7Xva_oJNYnh91vC6kiVmXpfi9GaIuwqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دریاچه ارواح نوشهر با فضایی مه آلود و ترسناک یکی از خاص‌ترین جاهای دیدنی ایرانه
👌
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/671734" target="_blank">📅 13:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671733">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
رویترز به نقل از منابع امنیتی و نفتی عراق: یک نفتکش در بندر بصره مورد حمله پهپادی قرار گرفت، اما خسارتی به آن وارد نشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/671733" target="_blank">📅 13:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671732">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfWUQjxmcwaZpd-XWI-X9kv2nPQNnZV4BFfEqCUVG_91kXc05zVDXyUu0Ew61Uv-kATILj2HlVNcs7h02Kl3McHeI2aeDqJ4i9oCKv3d3owOwT9vieMV3DJ64xTLLXzB2OaRWLjwJYSs6zcVYtT20ZDjpYWgVIl575_v9XuKHRwiyZ4sRFtfmtBiwDcjbFPZm1n7XH3xhmyuE7v5fdWS4JmWR2U1Cc5NazGpraGr-MHq1BILtHq5Su2iaOHBj5fH6wj3nIdcrPEenyyWGt3NhNUH-DbxbMNGltFW3vt6Iqoxm9RJyDpzhiQgG9GQxi9o5dl9ktTG4Fp1S4C2uSUAvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی قیمت بلیت فینال جام جهانی؛ میانگین ۱۱ هزار دلار
🔹
براساس گزارش فوربس فینال جام جهانی ۲۰۲۶ بین آرژانتین و اسپانیا به گران‌ترین رویداد ورزشی تاریخ آمریکا در بازار فروش مجدد بلیت تبدیل شده است. میانگین قیمت بلیت به
۱۱ هزار و ۳۲۷ دلار
رسیده، ارزان‌ترین بلیت
۶ هزار و ۹۴۳ دلار
قیمت دارد و گران‌ترین بلیت فروخته‌شده تاکنون
۲۸ هزار و ۴۷۹ دلار
بوده است.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/671732" target="_blank">📅 13:05 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
