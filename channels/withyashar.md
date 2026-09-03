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
<img src="https://cdn4.telesco.pe/file/Py7d37P_lWbJdXDeHznNzZFpF_wXoohNAQu7m-lCcR20Sk25vvC8efamAj8lvFrbIdqW8E9MVsL6unOZ4j4dCIYvShqUOtlasIux7pA6oV85Ryobzwh2Pp-IUHLNmL7LBnsLys9fAleYS1UqzjNwIQW-lUgDO5bnK0jPYUjwbjCn0_B4UGvu32yyrnxivkmbzJ3HqxKS2IJTuzHqwtwLN6Y6VVSdj_FBqP6rGnO7huJAUXx_xd94yCSzeQW_Ac_bebDQgVJLPruFJ8304ZxuglUpBokFEWaPX6ezTXq4JkQa0nuYP7k8hF678IkammBBIY_zZnC-rPm5alJLz3ZH7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 447K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 20:53:28</div>
<hr>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5m8E040Tx4DNHqLcpRJEQHmquMeRt1CXR0wyhanoAkAc-t-tTSwbh3mSsbdLEcKxZkyujMiHK9JILu5zZDi9LiXU_cafmc8JA4VbsF8cB4yigGWYSluSz1bYX-MoxgUbLSnu0VcQ0iDcgby2mbrAhokP896lr0exaHqhzpu4TF-nAZ2l25rOTgFdYjhv8BHqM4WZuf-lTFM9l-YhwkZaMQK7oGgnBgKx2MvcmoX_cTI31YatvP3QKEfV0whaWMqMIkcUGQZChOQHX_8YBbfHYnnT0b9oe3G7jwh0q-TTo2VgWunzpRMqjOZGKv3ir4VqXzljL1m7aMDSEIIpCQ7Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا : امیر یاریاب، فرمانده عملیات سایبری فرماندهی سایبری-الکترونیکی سپاه پاسداران (IRGC-CEC) است. او در این سمت، گروه‌های سایبری مخرب وابسته به سپاه، از جمله «شهید همت» و «شهید شوشتری» را برای هدف قرار دادن زیرساخت‌های حیاتی آمریکا هدایت می‌کند. ما برای اطلاعاتی که به شناسایی یا یافتن یاریاب و افراد یا گروه‌های مرتبط با این عملیات‌های سایبری منجر شود، تا
۱۰ میلیون دلار پاداش
تعیین کرده این.
@WarRoom</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/withyashar/22207" target="_blank">📅 20:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کانال 14 عبری: افزایش قابل توجهی در سطح آمادگی و هوشیاری در داخل اسرائیل، با توجه به احتمال از سرگیری درگیری‌های نظامی مستقیم با ایران، مشاهده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/withyashar/22206" target="_blank">📅 20:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/090e602491.mp4?token=XTN-86W5S7RLYX1MTMUhtm5LXNAwk7wefJISgEEet2oL5IbfeuaDo7o8bv_d1pXIWK17ob0xalS_oO8yqZGpwLI2hND5-69hDIAHz5s_AIrW_uJdhTl41ZUJjVT0OK19z5EG9xJkXD1Id1hNihNHH6Ld7BhCCBIus05w0QyyO88BcGwH9voYflifoK9FVQyPjvXxsPTVe9x6_JtQki5AbzxKeWtO_flpPtLxkJZP5PWtNl6_pRvD-NsPwoft7QVfTme1ZlppZMz8mcH8lUtJHkpHtVJB2skXb02EyND8THP1N4RZZPchiGqFIveuuj5mP4ZnIkZtsTZwiY4-DtWEQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/090e602491.mp4?token=XTN-86W5S7RLYX1MTMUhtm5LXNAwk7wefJISgEEet2oL5IbfeuaDo7o8bv_d1pXIWK17ob0xalS_oO8yqZGpwLI2hND5-69hDIAHz5s_AIrW_uJdhTl41ZUJjVT0OK19z5EG9xJkXD1Id1hNihNHH6Ld7BhCCBIus05w0QyyO88BcGwH9voYflifoK9FVQyPjvXxsPTVe9x6_JtQki5AbzxKeWtO_flpPtLxkJZP5PWtNl6_pRvD-NsPwoft7QVfTme1ZlppZMz8mcH8lUtJHkpHtVJB2skXb02EyND8THP1N4RZZPchiGqFIveuuj5mP4ZnIkZtsTZwiY4-DtWEQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره بریتانیا : کشور شما خوب پیش نمی‌رود.
فراموش نکنید که درصد بالایی از نفت خود را از تنگه هرمز دریافت می‌کنید.
و شما برای کمک به من آنجا نبودید. کشور شما برای کمک به من آنجا نبود!
@WarRoom</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/withyashar/22205" target="_blank">📅 20:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22203">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نیویورک‌پست: عمان به‌طور محرمانه پیشنهاد ایران برای دریافت هزینه از کشتی‌های عبوری از تنگه هرمز را رد کرده است. به گفته یک مقام ارشد منطقه‌ای، مسقط حتی با دریافت هزینه‌های داوطلبانه برای خدمات زیست‌محیطی و امنیتی نیز موافقت نکرده و این پیشنهاد برخلاف ادعای پیشین سپاه پاسداران، هنوز به توافق نهایی تبدیل نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/withyashar/22203" target="_blank">📅 20:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اتاق جنگ با یاشار : نتانیاهو داره هر روز رژیم رو انگول می‌کنه و صحبت از تغییر رژیم می‌کنه بعدم جنوب لبنان رو میکوبه سفت
💥
😂
خواهیم دید چه خواهد شد @WarRoom</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/withyashar/22202" target="_blank">📅 19:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22201">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اتاق جنگ با یاشار : نتانیاهو داره هر روز رژیم رو انگول می‌کنه و صحبت از تغییر رژیم می‌کنه بعدم جنوب لبنان رو میکوبه سفت
💥
😂
خواهیم دید چه خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/22201" target="_blank">📅 19:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نتانیاهو: "ما اطمینان داریم که قادر به سرنگونی نظام ایرانی هستیم. این وظیفه اصلی است و به زودی به انجام خواهد رسید."
@WarRoom</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/22200" target="_blank">📅 19:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/22199" target="_blank">📅 19:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">@WarRoom
جنگ خاموش ؟</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/22198" target="_blank">📅 19:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/22197" target="_blank">📅 19:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4N3WiLGrf5zugdQ5bTvImWqbR8Gb0qd_tXUovdseELyNou1PZvGo-hAgUGk6KQiByZgCGxjMPkfMT7eLoufhNC7tllCQAEfCyghAwg9AkZr-BS1dobzofutoPDhUb6rH6Pwo7lV1nziAbEIzJpqQb744aBf9au7n36pwXBe2rt6uO1EBsaSSlFQRcgl6h1Oi1sA8ePnrpdRZHlsFogkQHYQSmNL3hZF-GXgaRaBb8UBjCU5226JfxlVWp5kZKNxoE5VPzGL63AcDhazvjmZGJ-PlWRzDgRMkq1-nqdjujzqOHq4AAjUPhAO9if7DcVe6h71KngqXZ6vAce2BDBfyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش پرتاب موشک/پهپاد از سیریک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/22196" target="_blank">📅 19:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گزارش تایید نشده : یاشار پدرم تو نیروگاه برق همدان کار میکنه ,میگه نیروگاه برق ۴۰۰ کیلو ولت رو زدن ,حدود یک ساعت پیش تا دو ساعت , میخواستم باهاش تماس بگیرم ولی نمیشد الان زنگ زد گفت
@WarRoom</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/22195" target="_blank">📅 19:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMlVMEx5kSGJ8doV1LzCs-P3cBblOXGp6z0ZRGIDfmUQkG-Ur08hr0iuRvQ9VXGfOY8MQDcMmbYNfZ9h_a3RRh0QvxGrZhaZyKgvL89pAsYC5-lFDk_A_qXDTaw6MErzW2bU8gZam04qVUCQioRtkmTGOahDzajOejGOGJa3AHZqOaazngbSQnU6KMG4Zp2kNraZN5h__EHhQZKFg8YzHw5uzTsgi13oWFdo8hqF0fjQ-KG2CYr5BuzbUBHwtVj4oEa_FlRf1Dst-4kmVqnZekPD9rJFZ8F7asXkXgTt53-3Ytgw_vwMANpwRt1UvcJbA-1d3u0zhVgSIuCKaSdxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تبلیغ از طرف من نیست ! پولی ندید  بهش !</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/22194" target="_blank">📅 19:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkC-01WwPM5QbEJdG7ufRT2hf6uL258R5Lj0Sa_jR0t8waRK4hZm3kaku6B0AbwiTsqbBDVDRjRJVZdI6-GlG0nr-Mq-DYJwnH1zr8AZiay1g6KGWwxkSjlTdyoA3pKkKbF7G1QRv2PSvm8lXN_yaHlfXFBVPhhLlsqmxb-UyfUoXcGojwGZxNrt6TlLdDMVmpOxG_JdS1ZyN4Ai92A1zNjgEFwNgdSmiMSapmhlGsYrcNWxLMSPtkH8TKCbUMEchfvFzF20CyicyzhgdpORiKblg-fev5UVwtcwVfvddiwjdm363EZsCZkKNQ3RE2aOXDPtfa4QFHWLBHp99thu6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای رسانه‌های خائن و پلیدی که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کنند، باید گفت ما عملاً مقادیر نامحدودی مهمات درجه متوسط تا بالا در اختیار داریم؛ بسیار بیشتر از آنکه بتوانیم در این عملیات یا هر جنگ دیگری (که بسیار بعید است!) که به‌طور غیرمحتمل رخ دهد، مصرف کنیم. علاوه بر این، ما مهمات را در سطحی بی‌سابقه تولید می‌کنیم. ما در حال انباشته‌سازی و آمادگی برای هرگونه سناریوی احتمالی هستیم. ما این مهمات را برای خودمان، یعنی ایالات متحده آمریکا، نگه می‌داریم نه برای فروش به دیگران؛ اما فروش به متحدان به‌زودی از سر گرفته خواهد شد. همچنین، لطفاً اعلام شود که دولت بایدن بسیار بیشتر از آنچه ما در ایران مصرف کرده‌ایم، مهمات را بدون هیچ هزینه‌ای به اوکراین اهدا کرد. صدها میلیارد دلار به اوکراین و ناتو به‌صورت رایگان داده شد؛ هزینه‌ای که اروپا می‌توانست پرداخت کند اگر تنها از آن‌ها درخواست می‌شد، اما ما آن مبلغ را مطالبه خواهیم کرد، اگرچه با تأخیر!
@WarRoom</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/22193" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22192">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6V0_Y7h5eLLCJEsRsAdoEHaW8IFEqTynuIREl2DPeGJ0ZwX2DXbdu4JqvJkTS1bm9vayEnllJ7c2i7OEcgt_lqxaW1PJRB68NnOxOemsYLwqicoIc0c1x2E3E8fF5fC5zp1ay3pN2T7zSYSVivtjXH2yKK2WwiKnM8Y8uqrxGlrdXxFPQYroRC_VEyZGZoDeQKxbPhX3iJjXQuONPV83bNquIbfTHC0nssBNZ_Ypk46kA3KXkyrh8-SwmtREy3OueEHijA-gxHwzSPLEiKlLYBsPn-KoSZ5xByLQMDDuKzyhz8PCPqrbUy7IBAyDA69i2O66SdrSGr8wg7qre69zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : مردم و رسانه‌هایی که مدام بر این موضوع تأکید می‌کنند که ما مهمات نداریم (و صددرصد اشتباه می‌کنند!) در واقع خائن هستند. آن‌ها این کار را می‌کنند زیرا ترجیح می‌دهند ایالات متحده در جنگی که به‌راحتی در حال پیروزی در آن هستیم شکست بخورد، تا اینکه ببینند من پیروز می‌شوم!
@WarRoom</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/22192" target="_blank">📅 18:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/22191" target="_blank">📅 18:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اسرائیل نشنال نیوز : کانال ۷ عبری مدعی شد موشک‌های ایران به هتلی در اردن که افسران نظامی آمریکایی در آن اقامت داشتند اصابت کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/22190" target="_blank">📅 18:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f75591b88.mp4?token=rzBeYKivz_Z5FL_bKh6xM7qm0kCZJXIU4oHLODlWLX1s0RMK1YDH7LWIVRJb2iBQ5QebhxRoQy_zEA8yPO46MArvGID0YEAJWiut2KXd_50Ypr4DyP5hdBHN1HmGQYb70qGNn3Ii8tMK5oA2kK7FK4dCK7_55kh6Bq72WMkjMWK3tjPmfPCYKq-5d9CVa6B24oDVXxWkvoGAfQhqSD6tEt0cqdYzRIZ2iQmwE9o2kpIJ3iGpg4ud8TACplj-1O0QqC_h9elzl1YKDnLBNVw_lACR2fuGLx3bFU13cCpbBhu1Nb8S50OhjxsIb28ycUg8ozMjHfwQXOwYj0AG4t8Q1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f75591b88.mp4?token=rzBeYKivz_Z5FL_bKh6xM7qm0kCZJXIU4oHLODlWLX1s0RMK1YDH7LWIVRJb2iBQ5QebhxRoQy_zEA8yPO46MArvGID0YEAJWiut2KXd_50Ypr4DyP5hdBHN1HmGQYb70qGNn3Ii8tMK5oA2kK7FK4dCK7_55kh6Bq72WMkjMWK3tjPmfPCYKq-5d9CVa6B24oDVXxWkvoGAfQhqSD6tEt0cqdYzRIZ2iQmwE9o2kpIJ3iGpg4ud8TACplj-1O0QqC_h9elzl1YKDnLBNVw_lACR2fuGLx3bFU13cCpbBhu1Nb8S50OhjxsIb28ycUg8ozMjHfwQXOwYj0AG4t8Q1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اسرائیلی، با پشتیبانی تانک‌های مرکاوا، در حال پیشروی در جنوب لبنان هستند
@WarRoom</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/22189" target="_blank">📅 17:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مقام آمریکایی به خبرگزاری الجزیره گفت پایگاه‌های نظامی آمریکا در منطقه، از جمله پایگاه‌های این کشور در کویت، در جریان حملات تلافی‌جویانه شب گذشته ایران
هیچ‌گونه آسیبی ندیده و هدف حمله قرار نگرفته‌اند
. الجزیره پیش‌تر گزارش داده بود که ایران در واکنش به حملات آمریکا، موشک‌ها و پهپادهایی را به سمت اهدافی در کویت، بحرین، اردن و عراق شلیک کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/22188" target="_blank">📅 17:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22187">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در صورت ازسرگیری جنگ، ایران ۳ گزینه برای تشدید حملات در اختیار دارد
۱.
گسترش حملات به کشورهای عربی خلیج فارس
، از جمله هدف قرار دادن تأسیسات نفت و گاز، نیروگاه‌ها و تأسیسات آب‌شیرین‌کن؛ اقدامی که می‌تواند به افزایش شدید قیمت انرژی و آسیب به اقتصاد کشورهای منطقه منجر شود.
۲.
جلوگیری از خروج بیشتر نفت از منطقه
با تشدید فشار بر کشتیرانی و تنگه هرمز و تلاش برای متوقف کردن صادرات نفت از خلیج فارس.
۳.
گسترش حملات به منافع آمریکا و کشورهای غربی در خارج از منطقه
، از جمله حملات مستقیم یا غیرمستقیم به اهداف غربی.
@WarRoom</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/22187" target="_blank">📅 17:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بلومبرگ: درگیری آمریکا و ایران به بن‌بست رسیده و هیچ نشانه‌ای از حل‌وفصل قریب‌الوقوع آن دیده نمی‌شود. در حالی که حملات متقابل ادامه دارد، تلاش‌های دیپلماتیک برای پایان دادن به درگیری پیشرفت قابل‌توجهی نداشته است. تهران همچنان از عقب‌نشینی از مواضع خود خودداری می‌کند و واشنگتن نیز فشار اقتصادی و نظامی را ادامه می‌دهد. هم‌زمان، دولت ترامپ در حال بررسی راه‌هایی برای مهار درگیری است، اما احتمال طولانی‌شدن جنگ همچنان جدی است. گزارش‌های امروز نیز نشان می‌دهد درگیری وارد مرحله‌ای فرسایشی شده و آمریکا حتی استقرار نیروهای خود در منطقه را تا سال ۲۰۲۷ تمدید کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/22186" target="_blank">📅 17:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سخنگوی قرارگاه خاتم‌ الانبیا:
عملیات های تهاجمی علیه آمریکا ادامه خواهد داشت.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/22185" target="_blank">📅 17:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOhyF6nPjZGQlPw1SZtkxJ-hMqe6GPujl4emvmLn7HSt2BYDDYVZRm4jhJn_9RBwgNGApLgWLBbX68Db6GablZVFJ8Dr86kCoGIzP6Jzw75tEtVGsRNqKEhuOiaCNU1WEyGTdBLmpiY6PxOOK1VAaJSRZosmpfUfwFPRoPplctqj2-ajzE38Up1EdG-V7ATS9ENAaKDt-mH3mdb85-TXh26XS1VngqcTda-BWvkXP30VzcRt_yE5Kg4Pk9VU_6LIHlCwFyxVx-TdQ-mM-mASCXxJUmMhSw2N5ZcX5phZCAmghG1tq19KMmZMpszTOLw8VJfyfkHjrSD0xQXUUElMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش اولیه تاییدنشده
از حمله به یک سایت در استان فارس
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/22184" target="_blank">📅 17:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c459a770c1.mp4?token=QTOoObTK53TPKydQkq_mrpuMoVGjSjB8Tn4lof_epjs9xHvNO-V6fyvDHK9st2POevdBzZ04lxkd72UTwao5ZxHGJTBQIlanV0bUyrap_82vC8p2tcy9MfVSfDwxAratjsXsZERPEmWawOtt1kJAPXUiJRVjBMDQhIYYiNKRMw9TA4fG_Od3vlpOCE-FSSXb7jAxzjA50wEOLps7TpQeBVtZxyboe452FxJPdO00ZDjvGia8jA1oNGUfb-12_VGGprE4HZFak_6Gek-_DyWATzpNkxjuG2gTTLV862Yjb74gztvz0qx1OIaj3kkbclbzHhBKVwpVi1dCj-gmYWpIXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c459a770c1.mp4?token=QTOoObTK53TPKydQkq_mrpuMoVGjSjB8Tn4lof_epjs9xHvNO-V6fyvDHK9st2POevdBzZ04lxkd72UTwao5ZxHGJTBQIlanV0bUyrap_82vC8p2tcy9MfVSfDwxAratjsXsZERPEmWawOtt1kJAPXUiJRVjBMDQhIYYiNKRMw9TA4fG_Od3vlpOCE-FSSXb7jAxzjA50wEOLps7TpQeBVtZxyboe452FxJPdO00ZDjvGia8jA1oNGUfb-12_VGGprE4HZFak_6Gek-_DyWATzpNkxjuG2gTTLV862Yjb74gztvz0qx1OIaj3kkbclbzHhBKVwpVi1dCj-gmYWpIXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدمه‌ ناو هواپیمابر آبراهام لینکلن ، به تایلند رسیدن و رفتن تا پس از یکسال در دریا بودن در خشکی عشقو حال کنن
@WarRoom</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/22183" target="_blank">📅 16:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">احمد وحیدی فرمانده سپاه: انتقام جان باختگان نبرد هرمز را می‌گیریم
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/22182" target="_blank">📅 16:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLom_u9Xzr6OOZEa4recykpJlR-isQOXs2taEZn9ZJ2fvFTyW0Ldz7IZw5wlT5WlUmVsx49OVyxb4tZEYfKvZyKjMSQbI6TvZiwrimQRFfJYB-vi4vW3fSLZmrySxmu6UKfbwa-nOMKJPHvNm4cxwn7uMmiAw75TPEoJxN2szXbkKMi6qLQNvL08YUAAbWGGj5fawVdsvhnZHOdYtHiXFcmZG_M6DgZd_DVNfAqDlZ1hPxhWup7GTiLNl6jg0QyaY3wBlaz97As6B45EMnB5eOAauyOkeXqT1OT7xKtrQ6YvOmPAYLPeBKJURm_gyf-ZDJyiMqwW7scY5tOjC9asqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر ۴ کشته شده هوا فضای سه پا ۱۱ شهریور ماه در کرمانشاه
@WarRoom</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/22181" target="_blank">📅 16:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بیانیه ارتش:در حملات اخیر آمریکا به ایران، که دو شب گذشته انجام شد،
3 خلبان نیروی هوایی ارتش و
6 نفر از پرسنل نیروی دریایی ارتش کشته شدند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/22180" target="_blank">📅 16:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ویدیو از دیدبان اتاق جنگ از خمین
🚨
🚨
عراقی ها مردین بدزدین
😂
😂
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/22179" target="_blank">📅 15:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22178">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from....</strong></div>
<div class="tg-text">چند بار دیگه بگی زارتان زورتان کارشون تمومه</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/22178" target="_blank">📅 15:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22177">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-cPxal1WdOSqYmzHRXdhvAzQBCUARHlwVJGuG3LvZUTxOwTEl95uzNiZzP9M0ZIj-5I8v-AYnCj26QVc0iEe00rWSVx71G5uTd_x5z_HHl7S4r2fihxuyBiMa9TJFlz0XBO6npT_Y46G8CEDG87LqCKgNIYuzEKzC7jb94_3O0VNte5f-dgsMb2uu8e_0Ijyw9iNlSnBDiJ5LxCRpVdLnY0rz6AiW4Bkhlkln5zz6CYXUfjMouNzQDc5Kk7o8P0Y9yKL60A1ve8vWWF_Mi796iAHZ3dq2h6we9pYPCOy_kKDSd0CuPqZooV3ZaTg9pRD61Ge_8NQpalwSoCv5Dn6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث: حجم نفت هرمز برگشته است!
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22177" target="_blank">📅 15:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22176">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWUnioeTLNuypsrxDifyLE3jkvHC0hcKEhU2OO5PYLbA38kJl7lnbpoMCMRlXYEp_HuzLOB7E4DfXBnd_qMfZtiXgMyHV29vLjZIrCOm3edoUtVLWcIfE7xkuQYrxyXKVXzntczaIIXUN0D1sGQSDF7ku5PJ-rJHqPdqbTufnu7WJQUQWYqsy4F0BLbLG9E37WfP3nUtlfiUnqvFLKYREVtSabj8JnywOokIlWI4LKYDoZab8-ne3-n0jpzpiO5UrFDGgs7KoUVyNElPep6NH9Vee7cyfVivrKg3D9oyXdL-2gvm7zn4ofCorDcN9NdAFcw0x1-7RZgXBE4y1p6bfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در واکنش به این گزارش نوشت:این عالی است!
واشنگتن‌پست: سوریه در حال تلاش برای تبدیل‌شدن به یک مسیر جایگزین برای انتقال نفت و کالا، در صورت ادامه اختلال در تنگه هرمز است. دمشق با تکیه بر موقعیت جغرافیایی خود و مسیرهای زمینی و بنادر مدیترانه، می‌خواهد از نیاز منطقه به مسیرهای جایگزین هرمز استفاده کند و به یک مرکز ترانزیتی مهم در خاورمیانه تبدیل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22176" target="_blank">📅 15:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22175" target="_blank">📅 14:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22174" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🫶</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22173" target="_blank">📅 13:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22172">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMo ya</strong></div>
<div class="tg-text">داش همین طوری الکی ویس بده فقط صداتو بشنویم</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22172" target="_blank">📅 13:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ارتش ایران اعلام کرد که امروز صبح، امارات و کویت را هدف قرار داده است:
ما "سیستم‌های ارتباطی هوایی"، "انبار تجهیزات" و "پناهگاه‌های هواپیماهای جنگی" متعلق به ارتش تروریستی آمریکا را در پایگاه احمد الجابر در کویت، با موشک و پهپاد هدف قرار دادیم.علاوه بر این، پایگاه‌های استقرار نیروها و "سیستم‌های رادار" متعلق به ارتش آمریکا در امارات نیز مورد هدف قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22171" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نرخ دلار ۲۲۴،۰۰۰ تومان(سقف تاریخی)
دلار کف بازار :نامعلوم ! تونستی بخر!
تتر ۲۲۲،۰۰۰ تومان (سقف تاریخی)
بیتکوین ۷۷،۹۵۹ $
انس جهانی طلا ۴،۴۳۴ $
نفت برنت  ۹۵،۲۹$
@WarRoom
🚨
🚨
🚨
🚨
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22170" target="_blank">📅 12:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f620a5c792.mp4?token=NV1_Q8pcqWw5rrIDx-bx9amBkBtf6hQN1sPo0aMozLXsuSNW_vvR_Xhem_Pfoay-urxCocTaCufJXKGSS-bY-ZSJyBvWVYa4QXLicJmsSWT0WoCYYewpiZnd88o_UQF8A759FIbb2ynO9GJrQoltnKf41oWPPuBXHRoEuMWWxz8r4FUTqND8T12pE_kBLHnJ2MXRgGk-weOMcszL-OnB_OiA9Z7MltDzLqOFVvyMrMcAKHalBhNPTLaCJcYI2J6NEkMYMg0tO5CfaWyX2pkLwtyN7Yuy6VFqR9mR05QeI7MWyNnJ0PlPHtS2yh-TZck2UPqOTQ5Yr_YjhjEzm24MfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f620a5c792.mp4?token=NV1_Q8pcqWw5rrIDx-bx9amBkBtf6hQN1sPo0aMozLXsuSNW_vvR_Xhem_Pfoay-urxCocTaCufJXKGSS-bY-ZSJyBvWVYa4QXLicJmsSWT0WoCYYewpiZnd88o_UQF8A759FIbb2ynO9GJrQoltnKf41oWPPuBXHRoEuMWWxz8r4FUTqND8T12pE_kBLHnJ2MXRgGk-weOMcszL-OnB_OiA9Z7MltDzLqOFVvyMrMcAKHalBhNPTLaCJcYI2J6NEkMYMg0tO5CfaWyX2pkLwtyN7Yuy6VFqR9mR05QeI7MWyNnJ0PlPHtS2yh-TZck2UPqOTQ5Yr_YjhjEzm24MfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ خطاب به هگ‌ست در مورد ایران: شما شب گذشته کار بسیار خوبی در مورد ایران انجام دادید. شما آن‌ها را به شدت شکست دادید. بسیار عالی.
ما در این زمینه، به هر حال، پیروز می‌شویم. ما باید این را بگوییم، زیرا رسانه‌ها از گفتن آن خودداری می‌کنند.
با این حال، حتی روزنامه نیویورک تایمز هم گفت که ایران اخیراً وضعیت خوبی ندارد. این یک خبر تکان‌دهنده بود وقتی آن‌ها این را گفتند.
آن‌ها هیچ هواپیمایی، هیچ چیز مربوط به هواپیما یا کشتی ندارند. همه آن‌ها در اعماق دریا یا در انتهای باند فرودگاه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22169" target="_blank">📅 11:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رویترز به نقل از منابع: ایران به آمریکا هشدار داده است در صورت حمله اسرائیل به ارتفاعات «علی‌الطاهر» در جنوب لبنان، تهران با قدرت پاسخ خواهد داد. بر اساس این گزارش، نیروهایی از سپاه پاسداران در کنار نیروهای حزب‌الله در این منطقه و شبکه تونل‌های زیرزمینی آن حضور دارند. ایران هشدار داده هرگونه عملیات همه‌جانبه اسرائیل برای تصرف این ارتفاعات می‌تواند با پاسخ مستقیم و گسترده تهران روبه‌رو شود.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22168" target="_blank">📅 11:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گزارش پرتاب ۴ پهپاد از سیریک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22167" target="_blank">📅 11:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22166">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVGDfPmafGiWzhJXh8UMfIhULb2A7vNcgh9VhncQk6bjsLsqLfFrvdUt9F58ECCtGmtOOILRV4Hxt69BWf5Zow5H8D857SglIp4frMXj_xAQDNrL-o-UYA6LbsbWJ0bzIr11rsGQjDLlxYqGwc7F6oAUR1AU-07ZE_ieiwuok7crEadj_B7dxYzWyF-aoXTRFI_pig5dyPa_UQeHHfj8QoxwTjq1nsPOwumANOdwElUWr4jqgVaPzomqUvorqxyP6hh8hPZ9VD71PY5goixWHm3BV6vng93WiQlTB5wxowJeZ4HfgIlJyt3EJSX_wbLrOESf6JQ7HmxInSNTKZf51Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوون دهه هشتادی ۲۳ ساله کرمانی
زمین خودش به ارزش ۹ میلیارد رو وقف مسجد جمکران کرد تا اونجا رو بسازن و معارف اهل بیت رو گسترش بدن.
@WarRoom
دیگه کرمان هم جنس خوب نیست و همش صنعتیه</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22166" target="_blank">📅 11:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وال‌استریت ژورنال: پیت هگست، وزیر دفاع آمریکا، مأموریت و استقرار شماری از نیروهای آمریکایی در منطقه را تا سال آینده (۲۰۲۷) تمدید کرده است؛ اقدامی که نشان می‌دهد واشنگتن خود را برای ادامه درگیری با ایران و حفظ گزینه‌های نظامی بیشتر آماده می‌کند. در حال حاضر…</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22165" target="_blank">📅 11:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بر اساس گزارش رویترز، شماری از مقام‌های ارشد کاخ سفید در حال بررسی این احتمال هستند که پس از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر، در صورت ادامه درگیری و شکست تلاش‌های دیپلماتیک، اقدام نظامی علیه ایران را تشدید کنند. با این حال، دولت ترامپ در حال حاضر…</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22164" target="_blank">📅 11:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رویترز هک شد
مالک خبرگزاری رویترز در بیانیه‌ای مطبوعاتی اعلام کرد یکی از واحدهایش با حادثه امنیت سایبری مواجه شده است.cاین حادثه امنیت سایبری در پلتفرم مدیریت پرونده‌های قضایی C-Track که برای مدیریت دیجیتالی پرونده‌ها و اسناد دادگاهی استفاده می‌شود، رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22163" target="_blank">📅 10:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c5b61e6d4.mp4?token=oVQMHv0Iuev6QcpDRirpkXj-fK-efn3qtQR1Kcpa99Yy3_WM0477bWlpChcnXFHnuAGAMiOuMib6lMhQTpT7fsGKoAilwW-JRd4ILkZUqXczps69rxhPyuwA8V0biiZEUXkfLuCYGgmuYI3dsEeTwZpITXVpTZxXvCeLADTci3Q69BfAxrLvh96oFVvHoRbh_EhD9rAsDFT_CR9b1EYbfw9E9lWMcyvVeKMm5N7_V1CJcQeMv02lnM3FM9lIZPemBhxsca4OyjoRZRE7ueRCaa-eybtZ2ILsPrikQe54jX4-jL-s8hPM783aGUE62qM39pDpx4MviA7z2oNXJOL8FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c5b61e6d4.mp4?token=oVQMHv0Iuev6QcpDRirpkXj-fK-efn3qtQR1Kcpa99Yy3_WM0477bWlpChcnXFHnuAGAMiOuMib6lMhQTpT7fsGKoAilwW-JRd4ILkZUqXczps69rxhPyuwA8V0biiZEUXkfLuCYGgmuYI3dsEeTwZpITXVpTZxXvCeLADTci3Q69BfAxrLvh96oFVvHoRbh_EhD9rAsDFT_CR9b1EYbfw9E9lWMcyvVeKMm5N7_V1CJcQeMv02lnM3FM9lIZPemBhxsca4OyjoRZRE7ueRCaa-eybtZ2ILsPrikQe54jX4-jL-s8hPM783aGUE62qM39pDpx4MviA7z2oNXJOL8FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد ممباقر : در زمان حمله هوایی چه باید کرد
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22162" target="_blank">📅 10:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22161">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a7c97f4e9.mp4?token=Cajkv8Qj915rwErVy3OOfj26h_9yWGUmhwQM-R3fVLgQbDcRD8fKeM5KJwkKZTPR0Wj8AqAQD3y__HHVQILwpqBDNSrpOWZYi8KkIKOZF8ceJEYMDkVMCAp8y1VgUhs-6Jy-PJC97fWYcJo7cb5L7gqkJ7mtuuyA-31P_iBP8aV9tHPAOwKVkIxHl7ASovzzu-DVrnBKaOTuS_Vr5br3SOYXiPeViJegVxnxF_IeAjf-u9IEpcVy6PtjxtmdT_pahcXroM3P21ygYEhnqTzj_MiceUbEnkd1ul2PPqOf-Xvfp_xeyTz_Xz_Efcws5CfE0KpN_kFEt6FYPLk8D1ZQPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a7c97f4e9.mp4?token=Cajkv8Qj915rwErVy3OOfj26h_9yWGUmhwQM-R3fVLgQbDcRD8fKeM5KJwkKZTPR0Wj8AqAQD3y__HHVQILwpqBDNSrpOWZYi8KkIKOZF8ceJEYMDkVMCAp8y1VgUhs-6Jy-PJC97fWYcJo7cb5L7gqkJ7mtuuyA-31P_iBP8aV9tHPAOwKVkIxHl7ASovzzu-DVrnBKaOTuS_Vr5br3SOYXiPeViJegVxnxF_IeAjf-u9IEpcVy6PtjxtmdT_pahcXroM3P21ygYEhnqTzj_MiceUbEnkd1ul2PPqOf-Xvfp_xeyTz_Xz_Efcws5CfE0KpN_kFEt6FYPLk8D1ZQPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چادری جلوی یه دختر موتورسوار رو گرفته، وببین چی میگه…
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22161" target="_blank">📅 10:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رویترز: تشدید جنگ ایران و آمریکا نگرانی‌ها درباره تلفات غیرنظامیان را افزایش داده است.
رویترز گزارش داده شدت گرفتن دوباره درگیری‌ها توجه‌ها را به شمار قربانیان غیرنظامی در ایران جلب کرده است.
تازه‌ترین حملات آمریکا، ۱۸ نفر کشته و ۱۰۸ نفر زخمی شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22160" target="_blank">📅 10:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1eb4d6be4.mp4?token=qPLBxkZzDbD0rMMUBb5cKnmWtIRDWpG2nyxnNyjopUbsfgEYh5jthrU8j8RZPLXuDdu43qjuPkNsGWNuNgQdA3nBHOqXWxMlA5OJu7buBSW4T_HOiCNLGqkZ05Nwc45EFx8GIvatZ0-i0B7mJGZrUoiVkz4svhIyD45slhziZjFFDF1uGGiwflkuQaMJGqPiNIIYTVkxRkTFBQec161iAqIbz9tztQ6TVPtgSenpG1K-zEJ4Vlwullwx3e3QmcX3NwFNTlphbOCCBqPhD0xkj3q4IXgGoW1YwX-AMjxfXlJf97MxR8oRGXsgaYSJRmrClpPwYlFKNJXAGC5qt1eIjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1eb4d6be4.mp4?token=qPLBxkZzDbD0rMMUBb5cKnmWtIRDWpG2nyxnNyjopUbsfgEYh5jthrU8j8RZPLXuDdu43qjuPkNsGWNuNgQdA3nBHOqXWxMlA5OJu7buBSW4T_HOiCNLGqkZ05Nwc45EFx8GIvatZ0-i0B7mJGZrUoiVkz4svhIyD45slhziZjFFDF1uGGiwflkuQaMJGqPiNIIYTVkxRkTFBQec161iAqIbz9tztQ6TVPtgSenpG1K-zEJ4Vlwullwx3e3QmcX3NwFNTlphbOCCBqPhD0xkj3q4IXgGoW1YwX-AMjxfXlJf97MxR8oRGXsgaYSJRmrClpPwYlFKNJXAGC5qt1eIjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: اقتصاد آن‌ها بدترین اقتصاد در کل جهان است و پولشان بی‌ارزش است. بنابراین، فقط مسئله زمان است؛ فقط مسئله زمان
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22159" target="_blank">📅 09:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a756d7f2d.mp4?token=sYkTuTHpCrK1nvid3nyYytn8KWtTs2CPii4fJoUvsZhGJcV2zP1cab1sh_OfGQfkgqbqS605CuB0P-fkUZaUvLGifQ_4Eo5a-ZJNvnZ9yxVfPI3dnX4soMYWLJWvVM3mj-3SPb495wlMBrnFMFjpw8b_seoqdnra3cpM5X9KcH1_RlWK72zyYaibiD-mwgvHIbFXICrN5SZHrZhCqvhGJekQfP8Nyh5P4qv-z8KBRAzvMgdnOEawyokqZqkuu7mgPUmWbTUxSP7V2kZvovPhaHw2RImzQ1E75gBRsEx-9-vsdmBCI0lO2a7QQ42kS9QTr-Hi7WPfyx0HEAj84DmELw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a756d7f2d.mp4?token=sYkTuTHpCrK1nvid3nyYytn8KWtTs2CPii4fJoUvsZhGJcV2zP1cab1sh_OfGQfkgqbqS605CuB0P-fkUZaUvLGifQ_4Eo5a-ZJNvnZ9yxVfPI3dnX4soMYWLJWvVM3mj-3SPb495wlMBrnFMFjpw8b_seoqdnra3cpM5X9KcH1_RlWK72zyYaibiD-mwgvHIbFXICrN5SZHrZhCqvhGJekQfP8Nyh5P4qv-z8KBRAzvMgdnOEawyokqZqkuu7mgPUmWbTUxSP7V2kZvovPhaHw2RImzQ1E75gBRsEx-9-vsdmBCI0lO2a7QQ42kS9QTr-Hi7WPfyx0HEAj84DmELw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریس رایت، وزیر انرژی آمریکا: مسیرهای جایگزین برای انتقال نفت و گاز ایجاد خواهد شد و نمی‌توان همه تخم‌مرغ‌ها را در یک سبد گذاشت. شاید جهان پیش‌تر به تنگه هرمز وابسته بوده، اما ترامپ در حال تغییر این وضعیت است. خطوط لوله جدید ساخته و خطوط موجود گسترش داده خواهند شد تا وابستگی به تنگه هرمز و اهرم ایران برای استفاده از آن کاهش یابد. رایت همچنین گفت نیروی دریایی آمریکا در حال خنثی کردن تهدیدهای ایران است و انتقال نفت و گاز به بازارهای جهانی ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22158" target="_blank">📅 09:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حکم صادق ساعدی‌نیا در دیوان عالی کشور تأیید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس و مصادره کلیه اموال
بر اساس اعلام مرکز رسانه قوه قضائیه، حکم پرونده صادق ساعدی‌نیا در دیوان عالی کشور تأیید شده است. او به اتهام «فعالیت رسانه‌ای و تبلیغی علیه امنیت کشور به نفع گروه‌های معاند» به
۱۲ سال و ۶ ماه و یک روز حبس تعزیری
و
مصادره کلیه اموال منقول و غیرمنقول به نفع دولت
محکوم شده است. همچنین به‌منظور جبران خسارت واردشده به اماکن و اموال عمومی در استان قم، ساعدی‌نیا به
دو سال منع اشتغال در شغل کافه‌داری پس از پایان حبس
محکوم شده است
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22157" target="_blank">📅 09:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وال‌استریت ژورنال:
پیت هگست، وزیر دفاع آمریکا، مأموریت و استقرار شماری از نیروهای آمریکایی در منطقه را تا سال آینده (۲۰۲۷) تمدید کرده است؛ اقدامی که نشان می‌دهد واشنگتن خود را برای
ادامه درگیری با ایران و حفظ گزینه‌های نظامی بیشتر
آماده می‌کند. در حال حاضر حدود
۵۰ هزار نیروی آمریکایی و ۱۹ ناو جنگی
در منطقه حضور دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/22156" target="_blank">📅 09:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22155">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رویترز به نقل از منابع: دست‌کم سه پالایشگاه نفت هند و یک شرکت بزرگ بین‌المللی انرژی قصد دارند به‌دلیل نگرانی‌های امنیتی، استفاده از کشتی‌های قرارگرفته در فهرست سیاه جدید ایران را متوقف کنند.
این تصمیم پس از آن گرفته شده که ایران فهرستی اولیه شامل
۴۵ کشتی
را به‌دلیل نقض مقررات دریانوردی در تنگه هرمز ممنوع کرد؛ پالایشگاه‌ها همچنین قصد دارند از این کشتی‌ها در عملیات انتقال نفت از کشتی به کشتی (STS) استفاده نکنند
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/22155" target="_blank">📅 09:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ در گفت‌وگویی تلفنی با شبکه «کان» اسرائیل، در واکنش به تشدید تنش‌ها با ایران گفت
اسرائیل نباید نگران باشد؛ چون من
رئیس‌جمهور هستم
و تأکید کرد که آمریکا از اسرائیل حمایت خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22154" target="_blank">📅 09:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اکسیوس به نقل از منابع: ویتکاف آخر هفته گذشته با طحنون بن زاید، مشاور امنیت ملی امارات، در ساردینیا دیدار کرد و درباره گام‌های بعدی در قبال ایران رایزنی کردند.
این دیدار در حالی انجام شد که دولت ترامپ فشار اقتصادی بر ایران را افزایش داده و کارزار «عملیات طرد اقتصادی» را دنبال می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22153" target="_blank">📅 09:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آکسیوس: مارکو روبیو از سفارتخانه‌های آمریکا خواسته دولت‌های میزبان را برای قطع فوری و نظام‌مند تجارت با ایران تحت فشار قرار دهند.
در این دستور، از سفارتخانه‌ها خواسته شده فعالیت‌های تجاری غیرقانونی مرتبط با ایران را شناسایی و از دولت‌های میزبان بخواهند
شعب بانک‌های ملی ایران و صادرات ایران
را که واشنگتن آنها را مرتبط با سپاه پاسداران می‌داند، تعطیل کنند. سفارتخانه‌های آمریکا در
ابوظبی، مسقط، هنگ‌کنگ، دوحه، لندن، برلین و چند پایتخت آسیای مرکزی
نیز در این روند مأمور شده‌اند. واشنگتن هشدار داده کشورها و شرکت‌هایی که به تجارت با ایران ادامه دهند، ممکن است با تحریم و محدودیت دسترسی به نظام مالی و دلار آمریکا روبه‌رو شوند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22152" target="_blank">📅 09:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بر اساس گزارش رویترز، شماری از مقام‌های ارشد کاخ سفید در حال بررسی این احتمال هستند که پس از انتخابات میان‌دوره‌ای آمریکا در
۳ نوامبر
، در صورت ادامه درگیری و شکست تلاش‌های دیپلماتیک، اقدام نظامی علیه ایران را تشدید کنند. با این حال، دولت ترامپ در حال حاضر تلاش دارد پیش از انتخابات از گسترش بیشتر جنگ جلوگیری کند؛ چراکه ادامه درگیری، افزایش قیمت سوخت و تلفات احتمالی می‌تواند به جمهوری‌خواهان در انتخابات آسیب بزند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22151" target="_blank">📅 09:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22150">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش پرتاب موشک از‌ تبریز
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/22150" target="_blank">📅 01:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش صدای انفجار از تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/22149" target="_blank">📅 01:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">😍</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/22148" target="_blank">📅 00:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/22147" target="_blank">📅 00:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">واشنگتن پست: پنتاگون دسترسی نظامیان به اطلاعات محرمانه و حساس را کاهش می‌دهد، این در حالی است که نگرانی‌های فزاینده‌ای در داخل ارتش آمریکا در مورد پیامدهای احتمالی جنگ با ایران وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/22146" target="_blank">📅 00:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پدافند شرق تهران فعال شد
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/22145" target="_blank">📅 00:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22144">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">@WarRoom
Branding</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/22144" target="_blank">📅 00:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">السیسی، رئیس جمهور مصر، در جریان سفر شی جین پینگ به مصر، حمایت قاهره از موضع چین در قبال تایوان را مجدداً تأیید کرد و اظهار داشت که تایوان «بخشی جدایی‌ناپذیر» از چین است.
ترامپ : با شی حرف میزنم
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/22143" target="_blank">📅 00:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">@WarRoom
Khate man</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22142" target="_blank">📅 00:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHamid Taheri</strong></div>
<div class="tg-text">یاشار جان مجدد درود دلیل اینکه ایران اینترنشنال این همه بر علیه ترامپ هست و سعی در خراب کردن ترامپ پیش مردم ایرانه چیه؟</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22141" target="_blank">📅 23:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گزارش صدای انفجار یا پرتاب از سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/22140" target="_blank">📅 23:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22139">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">@WarRoom
سپر انسانی ۳</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22139" target="_blank">📅 23:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">@WarRoom
سپر انسانی ۲</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/22138" target="_blank">📅 23:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">@WarRoom
سپر انسانی ۱</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/22137" target="_blank">📅 23:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ناو آبراهام لینکلن رسید پاتایا
🥴
😂
ناو هواپیمابر آبراهام لینکلن CVN72 پس از ۲۸۶ روز متوالی حضور در دریا و جنگ با ایران ، که یک رکورد مدرن برای نیروی دریایی ایالات متحده است، در تاریخ ۲ سپتامبر امروز به بندر لائم چابانگ تایلند رسید.انتظار می‌رود هزاران پرسنل…</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/22136" target="_blank">📅 23:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e37dc0a2d7.mp4?token=NCoGkUwIvrf0Y4UoBkrt9s8U697YNxbrkPmr_SVAfFXkKGCJpcezJm86NvZZKkLaUqQShHAM56Q4dnNpcLtkjR4s3eDhYqMZsQMFlyxn6oSUNPrsTpk3n_cv7Gs9ApCHxBwAu6uDEgfCrwIWjITtWreYJIXgVsMlbFM1fVwOtNVSAXW0kqqXthiW021d2Hov3RG8t28WmQiXiSrPudBeReyXGQAUz8t7tge36R8g5qBTQmJqDsf5oLv4-Z_wxiOvOKNtDr7hnh13x1Z6KNdpNH93h-5-YN1a9UfNifZWk3iewyZOzB3hoxpt5-TfKJiGuJHxPXlRpNBe1pJk124U8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e37dc0a2d7.mp4?token=NCoGkUwIvrf0Y4UoBkrt9s8U697YNxbrkPmr_SVAfFXkKGCJpcezJm86NvZZKkLaUqQShHAM56Q4dnNpcLtkjR4s3eDhYqMZsQMFlyxn6oSUNPrsTpk3n_cv7Gs9ApCHxBwAu6uDEgfCrwIWjITtWreYJIXgVsMlbFM1fVwOtNVSAXW0kqqXthiW021d2Hov3RG8t28WmQiXiSrPudBeReyXGQAUz8t7tge36R8g5qBTQmJqDsf5oLv4-Z_wxiOvOKNtDr7hnh13x1Z6KNdpNH93h-5-YN1a9UfNifZWk3iewyZOzB3hoxpt5-TfKJiGuJHxPXlRpNBe1pJk124U8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام می‌گوید نیروهای آمریکایی از زمان تشدید محاصره بنادر ایران، ۸۶ کشتی تجاری را تغییر مسیر داده‌اند، ۳ کشتی را از کار انداخته‌اند و ۲ کشتی را توقیف کرده‌اند تا از رعایت مقررات اطمینان حاصل کنند.
از زمان به‌روزرسانی دیروز، ۲ کشتی تغییر مسیر داده شده افزایش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/22135" target="_blank">📅 23:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22134">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cee95e57f.mp4?token=VxrWTxGGYKEN69fb_7oT5GaIsovSWs-silvAno0zkb1SpDll6WntuCPcGxnOC9FMk9wbCo1pkx4Ltg39e6uArZq-MzfryzayPjBLm2h-3MNC2_BbylYByoqqkA7ZpMvcVoelbNdJAzYVva9Lb-t0Pm440iOrmbUXEA28p9sh9bhS4PBTst7FCA3u-1sOqAUzmLenXreDmJj_VIbfRenFbTYO36oCAKX_yHUd_VE9ZnYCsVLVc6_llxXFTaodGxKyBFpJIdHSDjT8BLFMjz8Zn7jgnFU8lqOUnD_HOJuHCH5Ux-Q0740t-E5Oy0fG4BMP79hKfAgSjNF-zVqLT4Gozw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cee95e57f.mp4?token=VxrWTxGGYKEN69fb_7oT5GaIsovSWs-silvAno0zkb1SpDll6WntuCPcGxnOC9FMk9wbCo1pkx4Ltg39e6uArZq-MzfryzayPjBLm2h-3MNC2_BbylYByoqqkA7ZpMvcVoelbNdJAzYVva9Lb-t0Pm440iOrmbUXEA28p9sh9bhS4PBTst7FCA3u-1sOqAUzmLenXreDmJj_VIbfRenFbTYO36oCAKX_yHUd_VE9ZnYCsVLVc6_llxXFTaodGxKyBFpJIdHSDjT8BLFMjz8Zn7jgnFU8lqOUnD_HOJuHCH5Ux-Q0740t-E5Oy0fG4BMP79hKfAgSjNF-zVqLT4Gozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:به محض اینکه این [وضعیت] به پایان برسد، که فکر نمی‌کنم خیلی طول بکشد، نمی‌دانم آن‌ها چقدر دیگر می‌توانند مقاومت کنند.
من تحت تاثیر انتخابات قرار نمی‌گیرم. من نامزد نیستم. حزب من در انتخابات شرکت می‌کند و من به حزبم کمک خواهم کرد.به نظر من، حزب من به این واقعیت احترام می‌گذارد که ما اجازه نمی‌دهیم ایران سلاح هسته‌ای داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/22134" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e5dd427da.mp4?token=tQ6YZIfJ2WDV-AYhzzYlg48JCUVAhMlRTChD5FDCiYQTdfWvdlq2Phmsq6v-mqPFNuO3IZVeI2m6EXqUp5HBfeoNLfoD5xN1s8cSCjS6tNgK3tIDdIOdH2tc5zAe75Z7iEtHzdshfFCGwxw_jpqH43qwhY-mrGosjIYjXybL2ae99jFCEI2ZXiyXLS0UiGyIoq37KNpS33hTsjhAx607rK5SNtjcQZcVXH9_kBZt_pTYFfHg7x3FwPRBtJ4z2zsLtqLARBQWifS8i8myNO_PHL-hDLEy2LEgJQIYgqcFiEYD8_3LYOEGepCedW0G_xJ0jGkuQ-vMb36Tv0XM1PTsVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e5dd427da.mp4?token=tQ6YZIfJ2WDV-AYhzzYlg48JCUVAhMlRTChD5FDCiYQTdfWvdlq2Phmsq6v-mqPFNuO3IZVeI2m6EXqUp5HBfeoNLfoD5xN1s8cSCjS6tNgK3tIDdIOdH2tc5zAe75Z7iEtHzdshfFCGwxw_jpqH43qwhY-mrGosjIYjXybL2ae99jFCEI2ZXiyXLS0UiGyIoq37KNpS33hTsjhAx607rK5SNtjcQZcVXH9_kBZt_pTYFfHg7x3FwPRBtJ4z2zsLtqLARBQWifS8i8myNO_PHL-hDLEy2LEgJQIYgqcFiEYD8_3LYOEGepCedW0G_xJ0jGkuQ-vMb36Tv0XM1PTsVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران دیروز شب یک حمله بسیار سنگین بود و ما آماده‌ایم هر زمان که بخواهیم حمله دیگری را انجام دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22132" target="_blank">📅 22:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22131">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خبرنگار: آیا شما سازمان سیا را برای مسلح کردن ایرانیان اعزام خواهید کرد؟
ترامپ: من نمی‌خواهم این را به شما بگویم، مناسب نخواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22131" target="_blank">📅 22:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22130">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22130" target="_blank">📅 22:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ درباره ایران: آماده حمله دیگری به ایران هستیم
ما تمام تجهیزات جدیدی را که آنها سعی در ساخت آنها در امتداد تنگه هرمز داشتند، برخی دفاعی و برخی تهاجمی، از بین بردیم.
آنها سعی می‌کردند کشتی‌ها را ببینند زیرا نمی‌توانند کشتی‌ها را ببینند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22129" target="_blank">📅 21:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cce539976.mp4?token=hONslcYxYzQxDRfU0XD6Xq2CHskUkA0y-hBnsq0ul5yULO7As06B8QyXihvM_5wxyt8MRkxd3-Qkkjl6r121n6RfyvOPo3WNrE_pgT4D1oEt1QC0D18_ymFyurqJEsHAfNSt7UZhbNpECXSJMZkyXDWCbQAvEJ_JJRniSFCmM5b7goq18ljYRuWXBONnU4YbtdLZ_5kCcx2dte3rpdvvhOxoUsL4Wp0gv7ewmDsfo-VD-q_bVRGvpO6blxKXCwFgmALM44x8UC5LkLqAlkb5VVO5sSwyaHu5mi0zyUo6OZFSCo68mVeKod7vcP6_TbznJjRLQPG5-o9ew_4WPM8NlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cce539976.mp4?token=hONslcYxYzQxDRfU0XD6Xq2CHskUkA0y-hBnsq0ul5yULO7As06B8QyXihvM_5wxyt8MRkxd3-Qkkjl6r121n6RfyvOPo3WNrE_pgT4D1oEt1QC0D18_ymFyurqJEsHAfNSt7UZhbNpECXSJMZkyXDWCbQAvEJ_JJRniSFCmM5b7goq18ljYRuWXBONnU4YbtdLZ_5kCcx2dte3rpdvvhOxoUsL4Wp0gv7ewmDsfo-VD-q_bVRGvpO6blxKXCwFgmALM44x8UC5LkLqAlkb5VVO5sSwyaHu5mi0zyUo6OZFSCo68mVeKod7vcP6_TbznJjRLQPG5-o9ew_4WPM8NlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران: ما هر کاری که آنها انجام می‌دهند را می‌بینیم.
آنها نمی‌توانند بدون اینکه ما ببینیم به دستشویی بروند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22128" target="_blank">📅 21:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fdea0685f.mp4?token=GHi9f_6UTgzMysfYI-eCpK0ifEYJJUFrXPH4Br2v0R_JNY6Z3vFq4paq19O9dsd3YZWiBoG3wNjoqjEcZSsoFzgjUYs0Mm48GSveSLd2bUtTVcPB5_We-KoYRg-J6b2FbtwyoQIMLdDFpSrU2geLC8cW7ToBDSO_t5uEppYz7N5V-TSW7jw9WofpNAxXnsUK6Z6yzvyFIxqM_qAnmDDhsKPdfeu4SOUnG7hFLbD-8SFSNtuhoJ-V-QoXl3pHx66-bzbcpMYvIvmM5Xm7M1yOkC25D80TMvc3qap2MzAUFp4Zyg7LFzVhcwwBaOyl6tho66Z8QsvJnzmVaglCAVcFkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fdea0685f.mp4?token=GHi9f_6UTgzMysfYI-eCpK0ifEYJJUFrXPH4Br2v0R_JNY6Z3vFq4paq19O9dsd3YZWiBoG3wNjoqjEcZSsoFzgjUYs0Mm48GSveSLd2bUtTVcPB5_We-KoYRg-J6b2FbtwyoQIMLdDFpSrU2geLC8cW7ToBDSO_t5uEppYz7N5V-TSW7jw9WofpNAxXnsUK6Z6yzvyFIxqM_qAnmDDhsKPdfeu4SOUnG7hFLbD-8SFSNtuhoJ-V-QoXl3pHx66-bzbcpMYvIvmM5Xm7M1yOkC25D80TMvc3qap2MzAUFp4Zyg7LFzVhcwwBaOyl6tho66Z8QsvJnzmVaglCAVcFkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران : آن‌ها وقتی مردم برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند.
آن‌ها دقیقاً از بین چشم‌هایشان به آن‌ها شلیک می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22127" target="_blank">📅 21:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c3fbdc32.mp4?token=pPRzzJUPAOG602JHsQSbusZnNXNqeSAiFDY7YGvZhMjZl9y3Z-6VPINAC_LKGAcP7u2hf2QzdbpUNBN1W_LUL11yUbDO1rzICKORqQxVnqcK6-av5jtAbOhxQgZYWbJeq4SGyTMLrsX0v4ZBHn19-JN867xNLbXTspEhLbLs62nxpU8TOnAGFuOHaQmwSBAoItxos4cFo8mXLeGd_I-MdDpeE2QkQIuaHbo3fp-uWVLGTy96UUdEO13uy3jTqeWwX3t-ybXDK--b9KwD11GZ7NQc5ilEQMEDF3FlhIiQ7P_Vly0uam9D0FC7yj3-MWZ2GKGSyz6g_X9KpKLbrC7dooWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c3fbdc32.mp4?token=pPRzzJUPAOG602JHsQSbusZnNXNqeSAiFDY7YGvZhMjZl9y3Z-6VPINAC_LKGAcP7u2hf2QzdbpUNBN1W_LUL11yUbDO1rzICKORqQxVnqcK6-av5jtAbOhxQgZYWbJeq4SGyTMLrsX0v4ZBHn19-JN867xNLbXTspEhLbLs62nxpU8TOnAGFuOHaQmwSBAoItxos4cFo8mXLeGd_I-MdDpeE2QkQIuaHbo3fp-uWVLGTy96UUdEO13uy3jTqeWwX3t-ybXDK--b9KwD11GZ7NQc5ilEQMEDF3FlhIiQ7P_Vly0uam9D0FC7yj3-MWZ2GKGSyz6g_X9KpKLbrC7dooWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
تا سه ماه پیش، ۵۲,۰۰۰ معترض ایرانی کشته شده بودند. و حالا می‌شنوم که احتمالاً ۲۰ تا ۲۵ هزار نفر دیگر هم به این تعداد اضافه شده است.
تقریباً ۶۵,۰۰۰ معترض کشته شده‌اند. تنها پاسخ این است که به آن‌ها شلیک شده است.
رژیم هر روز ضعیف‌تر می‌شود و در نهایت به جایی خواهند رسید که دیگر نمی‌توانند به‌راحتی شلیک کنند، زیرا فکر می‌کنم مردم دیگر این موضوع را تحمل نخواهند کرد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22126" target="_blank">📅 21:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22125" target="_blank">📅 21:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خبرگزاری i24 : در سایه تشدید تنش‌ها و بحران اقتصادی در ایران، سازمان اطلاعات سپاه پاسداران از احتمال وقوع دوباره اعتراضات هشدار می‌دهد. در همین حال، مقامات حکومت مدعی هستند: "آمریکا در تلاش است تا بی‌ثباتی داخلی ایجاد کند."
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22124" target="_blank">📅 21:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22123" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22122" target="_blank">📅 21:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22121" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22120">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تقابل بختیاری زاده و تارتار برنده نداشت
پرسپولیس
1️⃣
-
1️⃣
استقلال
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22120" target="_blank">📅 21:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22119">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارش آژانس بین‌المللی انرژی اتمی:
از ماه فوریه، هیچ بازرسی از تاسیسات اعلام‌شده در ایران انجام نداده‌ایم، به جز تاسیسات بوشهر.
ما تأیید می‌کنیم که قادر به بررسی این موضوع نیستیم که آیا مواد هسته‌ای ایران به اهداف نظامی تغییر کاربری داده شده‌اند یا خیر.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22119" target="_blank">📅 21:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا: یادداشت تفاهم با ایران منقضی شده است
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22118" target="_blank">📅 21:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گل اول استقلال به پرسپلیس
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22117" target="_blank">📅 20:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نتانیاهو
در گفت و گو با شبکه ۱۵ اسرائیل:
ایران را تسلیم خواهیم کرد و این رژیم سرنگون خواهد شد
و تمامی نهادهای ما برای تحقق این هدف تلاش می‌کنند.
وی اضافه کرد
ما می‌توانیم در هر لحظه به ایران حمله کنیم
و اگر آنها پاسخ دهند آخرین حمله آنها خواهد بود
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22116" target="_blank">📅 20:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رویترز : مقام‌های آمریکایی می‌گن شرکت کشتیرانی دولتی چین، «کس کو»، روی کشتی‌هاش تجهیزات مخفی نصب کرده که می‌تونه ارتباطات نظامی رو رهگیری کنه و کشتی‌ها و هواپیماها رو در نزدیکی سواحل ردیابی کنه.
به گفته آمریکایی‌ها، این اطلاعات به پکن برای شناسایی و رصد نظامی، هشدار زودهنگام و اختلافات ارضی کمک می‌کنه.
چین این ادعاها رو رد کرده و گفته کاملاً بی‌اساسن.
﻿
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22115" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مسئولان در دستگاه‌های امنیتی اسرائیل:
ما هیچ اطلاعاتی در اختیار نداریم که نشان دهد ایران برنامه‌ای برای حمله به ما در تعطیلات یهودی دارد، همانطور که آقای کاتس گفته است
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22114" target="_blank">📅 20:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eabf8dc5a2.mp4?token=CQfEU9YF670krhvKjWuk6wAJKzUD_ZLPOuuxpflzRbk_mX_ZmX49zk0p33zlTJde5uyJGGGAIc-ZkI00f6kxR1u8-HqwkOy4nhOayQewBobqbY17VlkkpPGaE-USSsq1SV1Tbw7eDaqYC-DCC605M1Kt4FbjCF8NB9Ao9MKnIidoYn1m4at2K34X7NRdOGfuB3w0vCpOJvXYykAanFQG2C6oUXEvas8TOD-Eumm3CiUiC60D4NpZyjs_kn4ZjWoYm4v_FtXfV8LbeAZIY0ZvFFYlwFt02Im3E3MsP5i2IkpTNmIkiQ1IpndHyS3yNLQ4zldvJ1BCMOX9keVLNa1pVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eabf8dc5a2.mp4?token=CQfEU9YF670krhvKjWuk6wAJKzUD_ZLPOuuxpflzRbk_mX_ZmX49zk0p33zlTJde5uyJGGGAIc-ZkI00f6kxR1u8-HqwkOy4nhOayQewBobqbY17VlkkpPGaE-USSsq1SV1Tbw7eDaqYC-DCC605M1Kt4FbjCF8NB9Ao9MKnIidoYn1m4at2K34X7NRdOGfuB3w0vCpOJvXYykAanFQG2C6oUXEvas8TOD-Eumm3CiUiC60D4NpZyjs_kn4ZjWoYm4v_FtXfV8LbeAZIY0ZvFFYlwFt02Im3E3MsP5i2IkpTNmIkiQ1IpndHyS3yNLQ4zldvJ1BCMOX9keVLNa1pVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راننده جنسیسی که تجمعات مشهد رو زیر گرفت: خدا شاهده عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و بجای اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22113" target="_blank">📅 19:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مارکو روبیو درباره ایران: هیچ کشوری نباید به ایران در دور زدن تحریم‌ها کمک کند. هیچ کشوری نباید به آنها در ایجاد سازوکارهایی که بتوانند از طریق آنها درآمد کسب کنند و سپس از آنها برای حمایت از تروریسم و ​​تلاش برای ساخت سلاح هسته‌ای استفاده کنند، کمک کند. و…</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22112" target="_blank">📅 19:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b1fd93ee.mp4?token=A9UVucbpT3Rx-PSAX7RcAhfYBM2rUgVxPxgCfmoY32tLhBFHH61M5LyukC9Lg0JJGTCTf_n7OW5-fFdPGmEiWHE_gLEkd_EqCE4BpgyIes_mhVIQ0jwZalIPewvMwzUQex-wEoDZUJs89JPMs5TqHtdQI1C2S3aa0nqK0fZ4hU5ZVY4hYaN4iZeZ2dDEk7oZAxom7i-3kB7Oh0izKESK0tnrVEbeoWCLB2kpk1dzvgAyINVYbQFM2MJQ3E5tKT8aIF1qc3gW7vkT7JR_T5W12NeU6VdFUPbc50Wpn9oz9N5TkNUOjnH2lw9IQCqmG-MdAcSXCaspubYQMfzdRlV4MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b1fd93ee.mp4?token=A9UVucbpT3Rx-PSAX7RcAhfYBM2rUgVxPxgCfmoY32tLhBFHH61M5LyukC9Lg0JJGTCTf_n7OW5-fFdPGmEiWHE_gLEkd_EqCE4BpgyIes_mhVIQ0jwZalIPewvMwzUQex-wEoDZUJs89JPMs5TqHtdQI1C2S3aa0nqK0fZ4hU5ZVY4hYaN4iZeZ2dDEk7oZAxom7i-3kB7Oh0izKESK0tnrVEbeoWCLB2kpk1dzvgAyINVYbQFM2MJQ3E5tKT8aIF1qc3gW7vkT7JR_T5W12NeU6VdFUPbc50Wpn9oz9N5TkNUOjnH2lw9IQCqmG-MdAcSXCaspubYQMfzdRlV4MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران: هیچ کشوری نباید به ایران در دور زدن تحریم‌ها کمک کند. هیچ کشوری نباید به آنها در ایجاد سازوکارهایی که بتوانند از طریق آنها درآمد کسب کنند و سپس از آنها برای حمایت از تروریسم و ​​تلاش برای ساخت سلاح هسته‌ای استفاده کنند، کمک کند.
و اگر کشورها تصمیم به انجام این کار بگیرند، ما نیز باید آنها را تحریم کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22111" target="_blank">📅 19:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مسئول مرکز ایثارگران سپاه فجر فارس اعلام کرد:
حدود ساعت یک بامداد امروز، سه‌شنبه ۱۱ شهریور ، یک راننده بیل مکانیکی از نیروهای قرارگاه خاتم‌ و بسیجیان سه پا ناحیه فسا که در پروژه‌های عمرانی شهرستان جهرم مشغول فعالیت بود، در پی حمله آمریکا به این شهرستان کشته شد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22110" target="_blank">📅 19:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTSKUFRVekyuWCf0KhcpuR7zhiCTVq4L8RKnow2HSjM51uVruI13PFGwxq2LfZLEsG2gq5qp56193H5PlRiQNCjWKHox9hb2hPEg_KjPJeu6K-2FEMy_Pv82KzNysBt67TD8u7J4CeqfTQUhl9fAQgloAmDuXvU14K1rrkElOgRiJr5HFmSbx_R1IS1QelcOX-Bxhzs7hWvxdbDeayxTu3f25pTvMldNBhBHi3lWpBUKvt8U2LzW6TmFk4_tl0J9CZYo8VE191k1qNzLk0JMO-0TQ78RNvfFpGOQhDWYv0Duka9uDBCycSIQhA6Prz53T8xD_8GWV_SpMn3LLuua0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
ترامپ در تروث :
اکنون که این منطقه تحت کنترل ایالات متحده قرار دارد، آیا باید نام تنگه هرمز را به «تنگه ترامپ» تغییر دهیم؟
درست مانند خود آمریکا، این منطقه از همیشه «داغ‌تر» خواهد بود!
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22109" target="_blank">📅 19:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3b32fad2.mp4?token=FWSSGf84nf6XgjJ0hpIp6EUUj-KBzlqjskWk34hKfkuLcJ8W8LZA2TwE1HddJ1oh7xjxXErMOg-B6ya_lyCzZRvvSu1p-Gdb0RI3AfX-QNWn5MQRnAcyFVruMGlnO492qD5UMrIQaqovWf2fxGs9cNCe_6zHZcnujtL1bjZ1Cev_DU5X4E49tEnSKqggoLynb-mcMNgdk4ivEWgJBAU9w2BdTPM8BGXSNkLVPUoQtc5obptCiTFB_GNEHUo3dUV14OXC7QS1BMIptzVkN8yOnyck1r95WQVUm-S0BAAGaZRS--EQCOZgNtJGinPe0un3lFitXu3egzKs9pk-KthVeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3b32fad2.mp4?token=FWSSGf84nf6XgjJ0hpIp6EUUj-KBzlqjskWk34hKfkuLcJ8W8LZA2TwE1HddJ1oh7xjxXErMOg-B6ya_lyCzZRvvSu1p-Gdb0RI3AfX-QNWn5MQRnAcyFVruMGlnO492qD5UMrIQaqovWf2fxGs9cNCe_6zHZcnujtL1bjZ1Cev_DU5X4E49tEnSKqggoLynb-mcMNgdk4ivEWgJBAU9w2BdTPM8BGXSNkLVPUoQtc5obptCiTFB_GNEHUo3dUV14OXC7QS1BMIptzVkN8yOnyck1r95WQVUm-S0BAAGaZRS--EQCOZgNtJGinPe0un3lFitXu3egzKs9pk-KthVeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران: ما الان کنترل تنگه هرمز رو در دست داریم. کنترلش می‌کنیم.
دیشب ۲۸ تا قایق، ۲۸ تا شناور رو از بین بردیم. ما تنگه رو تحت کنترل داریم؛ اونا دیگه چیزی گیرشون نمیاد و ما چندین شناور رو هم زدیم.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22108" target="_blank">📅 19:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3543df88e.mp4?token=kZF-ctGcbpyvCXRH3cO8AcHAy8V7l7OtFByAYGO37R_OPX5XxbFSGNFmPuBv3Bx00VKOogFyFL31aQ_IYw2tpHd9AZHCGMKRv5ZcGIYAplTbvolSk7ZqYPBEsRP819hFdLI_2xnQU2o96tQGtu7J8r7HsNt-oMmJ_S8paVnK_XZjd6Pj3aKQ4OgTxiYwYM9FPMFxGcy7JTexdcZN7-6Ayr4-JnXCPy-1GvF9mmIxPm4vKUzEFnVshI29PwCXTwjjphqrIE4i1_pzoTj6IUh7ex1_AGc9-NMUD7bFniKiC_h1NdiGdbCLh4r745v9ZY7OcoxilS0-FkKlhmmQcZ9VUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3543df88e.mp4?token=kZF-ctGcbpyvCXRH3cO8AcHAy8V7l7OtFByAYGO37R_OPX5XxbFSGNFmPuBv3Bx00VKOogFyFL31aQ_IYw2tpHd9AZHCGMKRv5ZcGIYAplTbvolSk7ZqYPBEsRP819hFdLI_2xnQU2o96tQGtu7J8r7HsNt-oMmJ_S8paVnK_XZjd6Pj3aKQ4OgTxiYwYM9FPMFxGcy7JTexdcZN7-6Ayr4-JnXCPy-1GvF9mmIxPm4vKUzEFnVshI29PwCXTwjjphqrIE4i1_pzoTj6IUh7ex1_AGc9-NMUD7bFniKiC_h1NdiGdbCLh4r745v9ZY7OcoxilS0-FkKlhmmQcZ9VUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
من به مردمم گفتم: "ما باید در جایی به نام ایران، جمهوری اسلامی ایران، متوقف شویم و باید آنها را از داشتن سلاح هسته‌ای بازداریم."
شما می‌خواهید مشکلی ببینید؟ بگذارید آنها سلاح هسته‌ای داشته باشند. شما نیمی از جهان را نابود خواهید کرد. آنها بیمار هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22107" target="_blank">📅 18:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">صدای انفجارهایی در کشور کویت شنیده شد که از استان بصره عراق نیز قابل شنیدن بوده
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22106" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
