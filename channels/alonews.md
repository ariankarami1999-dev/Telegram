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
<img src="https://cdn4.telesco.pe/file/NN4HfmiDHW0sqdnzSg7OUi4qHOzjbIdiVVC_KKl3ycV5uKohRGQ9O2m4FnlHP_x8PWY6wNz1m2xFs3IiwlRVrazdN256QAxqVpP2VhLgLoBZ9YehYMVfNFp8_EYGjNmrSzO0fXN6e7pQUr4D_GMvoAtrpNQ_jNhKr3T7oBlDA3QHzGqLgoRU9zwH45RKTlopK5AlbRE_trmUvGH-zD39t1eHNTjKGBLhUTH3KyFCjCVm8yIwJNQZ0TAY6P2TLVc7qZ0ZtZvQk1lnMeaGXod6v7XfOIruruDk3REBXePd5iSLyRAzWqXSJLDwB_L0zz3XrEHbn3iK2OQK3TxYG5RIxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 979K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 20:25:31</div>
<hr>

<div class="tg-post" id="msg-138227">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a223d8da6.mp4?token=hbDzqagQJtkdSt9Ec0spbeuRZgfFP7FkJEeRQdhSvzgvGat_YQKsjXRPUWIRc6TmyFXNhIjkNw1fXotNIqhAWi95xgN-aSuMh1QmjxIfCKcgwmF9Y35v8wdTkXjF_k93HxgfAbVN_1bUVaJhhwxQwrFXpKpPzV3gnLyBWedERgwVMKASNMQEYCs-eBfvMW0KTPRS4TkvokIIGJ8DbfC9dfSY5VDswOE2-MnhFYFttq-dpZE-ERnWwUqkwiJnV6JhVSbHb9xNpxTUUwOaIYsu2tbpygtd-dLpWH4_LqNAHBccxvFziFERLjPAeCuOweQzNW48MvtO0pW0HV1ym-3Xx1kFz_nGjobmLFFBipg8uBuFALq5XqHJxtxLBSMEm3gzDHkV85FMrA25wI0lLyWTyudAv6lYYLcmQxtkYL4rTBjOml-ECuW7QY_sPoHST6N2tOpkU9Z_MqFqT3lQ1dicSaSnaYN_oEEpnu-XGv4LHS7k3kKD783wuKNd6MeSYRhWAVpQLcPoBYLWu15HeLyEZQT4U3JXyqyK7Nre1eZ9SSYoOxAnBG5R0YB0Vor9DeZr06yv5OgoCnRcnDN-uyuKC8R0oVfCJZ1ByclL0er6KcuglfsBPOuRZele9OkHSN7wVDJpdKtepz3mPpj1JdyvgwMPCvMQ4VD_dBAmO1sv0WE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a223d8da6.mp4?token=hbDzqagQJtkdSt9Ec0spbeuRZgfFP7FkJEeRQdhSvzgvGat_YQKsjXRPUWIRc6TmyFXNhIjkNw1fXotNIqhAWi95xgN-aSuMh1QmjxIfCKcgwmF9Y35v8wdTkXjF_k93HxgfAbVN_1bUVaJhhwxQwrFXpKpPzV3gnLyBWedERgwVMKASNMQEYCs-eBfvMW0KTPRS4TkvokIIGJ8DbfC9dfSY5VDswOE2-MnhFYFttq-dpZE-ERnWwUqkwiJnV6JhVSbHb9xNpxTUUwOaIYsu2tbpygtd-dLpWH4_LqNAHBccxvFziFERLjPAeCuOweQzNW48MvtO0pW0HV1ym-3Xx1kFz_nGjobmLFFBipg8uBuFALq5XqHJxtxLBSMEm3gzDHkV85FMrA25wI0lLyWTyudAv6lYYLcmQxtkYL4rTBjOml-ECuW7QY_sPoHST6N2tOpkU9Z_MqFqT3lQ1dicSaSnaYN_oEEpnu-XGv4LHS7k3kKD783wuKNd6MeSYRhWAVpQLcPoBYLWu15HeLyEZQT4U3JXyqyK7Nre1eZ9SSYoOxAnBG5R0YB0Vor9DeZr06yv5OgoCnRcnDN-uyuKC8R0oVfCJZ1ByclL0er6KcuglfsBPOuRZele9OkHSN7wVDJpdKtepz3mPpj1JdyvgwMPCvMQ4VD_dBAmO1sv0WE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رهبر اپوزیسیون اسرائیل، یر لاپید، درباره جمهوري اسلامي ایران:
من از آوریل ۲۰۲۴ می‌گویم که کاری که اسرائیل باید انجام دهد، یا ائتلاف باید انجام دهد، بمباران تمام تأسیسات انرژی است... تا مطمئن شویم که اقتصاد ایران ویران می‌شود.
این تنها چیزی است که رژیم را سرنگون خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/138227" target="_blank">📅 20:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138226">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRYk3KLw8JnV5yS0bCOsgalG7ZGbVcy7e5UR7eY55i5Y7MNzmMSi6cKz4kGhe9__MYxg02A3lkVqmeCxbDCieRYSzUQ98g2zs5nMA1Le7yXgnnaJDD2hU6aeNayOM-EZ86KP_bmsRXb5LHuIGO0Yg_3IxcfsGiIolqi4RFP7PzRPujIs4dq6TGV9X80r521NAsoysKcrCfduWL40-jzreHH5LoDU3nucFN5gee-_Wpbt2O6CWr9UYN8jmv1LuhamN81oOjeAmBjLxeFw-5uuMaTz0tJeGzNDhdsKyp0FsR6yG3JMbinIgZpYNbvf37MzLDaP15bTPgr_SmA3lz6h7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
✨
رضائی موتورز
✨
🚘
خرید و فروش خودرو | ترخیص سریع و مطمئن
🔹
خودرو: ملی | گذر موقت | مناطق آزاد
🛳
ژنراتور: ارسال و ترخیص
🌍
صادرات و واردات قطعات و تجهیزات
⛴
ترخیص کالا از ایران و امارات
📌
بهترین قیمت، سریع‌ترین خدمات
📲
موجودی و قیمت روز وارد کانال شوید
👇
👇
https://t.me/rezaei_motors
https://t.me/rezaei_motors
https://t.me/rezaei_motors</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/alonews/138226" target="_blank">📅 20:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138225">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سهمیه بنزین سه هزار تومنی که ۱۰۰ لیتر بود به ۵۰ لیتر کاهش یافت
🔴
اینم بزودی کامل حذف میشه و دارن نم نم جا میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/138225" target="_blank">📅 20:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138224">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
کاخ سفید:
دیدار نتانیاهو و ترامپ به پایان رسید، جلسه مثبت و سازنده بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/138224" target="_blank">📅 20:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138223">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نیویورک‌تایمز:حمله اوکراین به یک کشتی ایرانی می‌تواند دو جنگ را به هم نزدیک‌تر کند. این حمله در دریای خزر، یک رویارویی مستقیم غیرمعمول بین دو کشوری بود که سال‌ها در دو جبهه مخالف بوده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/138223" target="_blank">📅 19:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138222">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57cf711cfd.mp4?token=VtjVHJgq5je3oVemam7RN6xpd7etZ2pzrwrxpNXTm7dYOMxR4LQr6Gc4FtHqLsB1w4o91PGSt3AnLn3qTFE00qZu5eeBiAaB3CbifBJTjwYRgMQ9ReWM74REt2hLFn3jflmwgBkfr0H34U6LYq9JeVAxZh8wLaKCpRrX1UQhaebpfJ01IBbDzy9_CDBhVCDcFzM3L0DIW3AvS88N9JmbF9ks8akuOQ-rXc75jvBAP4p2g4M4T_40HdKhr1Zf_bZBz2D7WXMZiQzmn5SH3yo9ZVNvIgLLgRjbU5FLw79zA932kjQPXzKHtQxfdAak7iuLCSvjHPI9-8q_e8pfEF4skA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57cf711cfd.mp4?token=VtjVHJgq5je3oVemam7RN6xpd7etZ2pzrwrxpNXTm7dYOMxR4LQr6Gc4FtHqLsB1w4o91PGSt3AnLn3qTFE00qZu5eeBiAaB3CbifBJTjwYRgMQ9ReWM74REt2hLFn3jflmwgBkfr0H34U6LYq9JeVAxZh8wLaKCpRrX1UQhaebpfJ01IBbDzy9_CDBhVCDcFzM3L0DIW3AvS88N9JmbF9ks8akuOQ-rXc75jvBAP4p2g4M4T_40HdKhr1Zf_bZBz2D7WXMZiQzmn5SH3yo9ZVNvIgLLgRjbU5FLw79zA932kjQPXzKHtQxfdAak7iuLCSvjHPI9-8q_e8pfEF4skA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون حقوقی وزارت خارجه: سیاست جمهوی اسلامی این است که تنگه هرمز هیچ‌گاه به حالت قبل از جنگ برنگردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/138222" target="_blank">📅 19:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138220">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jEg-Osw-Y0P6ktaDcNO9vUGc5WZQaYoVs871YfcbhqSYay5dj1cGhSzEQZDHOX0Aj1A0ftb2h-u8qJlL4mdsv3erYfhI9HYEdPri8RXzu5H1l5Nc4cVSuy4VQ262DypvQn8_NkL8_CG9jm9p4zpEWCEd1HpojG4Wg26DwqAJxoGw3_zFi8tXLeHR3W-xlPAiujIdAKQAxAjGzFexloBxXEDqhLstJPgV4J6EYzzmywBVMM9tqtDdhuFcicb4JBBIXY0MYmVqBNinZxuYlR2Vo-UY6Ec21WJ3vznEpwUS7ZXLqrjV30ufrwVY0AqIPmL1HKSneaK3rPvhZeoXBXM0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BnKWdc7ZYO5MX02sx7oyBseRaCzsgUEXsPRFTp6Y03EmNW3NSpscseGz69_yVIH34Fi43oxuoFqRHHuYxLz9TWsS-mfUOtu6661OUJMxh_PBiUytAp1Jb_66a7aLrNNB8LvtreyBGpqsb1tHChIrCHQO5_41w0AaoNL1zuW8A8VN7oqOtO20hjb6TztsQUe4kqF1VNbdEbN-SP7V49dGtYPC60V6DcPpFgu_xFlH4rqImGAa2DqJPAiAQVMAVXZ1esEc2odTuqdpUKuKjdzkVAeOfmZXoO5fxAqZCmGU9uN7ZOOagEtsbI0_Q8QspyejGHl0UPfHdVghklh3gg9o5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از فرودگاه بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138220" target="_blank">📅 19:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138219">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
زلنسکی: امروز دیدار خوبی با ترامپ داشتم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/138219" target="_blank">📅 19:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138218">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
اولین تصویر از دیدار نتانیاهو و ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/138218" target="_blank">📅 19:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138214">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riy9-3JPiNmq9kAdXw3CTdvKISGD3o2xAUtN3zQZ--Fpa-Hf_BIYLqfRanvFzK_CoB6Rg9JIfJEhm4h-ojpEyXW_JQJk45GP7QTwdKfvns-2Ia9fAXeRe2DJg_iWKqWIvQso-mPnYM3rwnm9yYLTKg_HxHIR1I6jsO2SrdwXg99Kcsu9l8_zmZyO-HQOJWL_Y8v_LYMZhO17Rt1USZ9-XE_YUxO8g1m_0DEf4KaSXvjqdaxBx9XMC4wNRDisBxph__aO9DMonwlnwxP0ad25iEsuKbMVJ1hmsXhnh7OS87ay3QCkRxLxC0copQwhMHcVzizjpJjvC2L9bKIMfJ2FyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKmSCttkujnfiV4GCH3taw7n-pP1cNJxC-LnJ-3TSixwKHkMtX2tDQXwt_wFGSbT9schHjCrsQt7SoPNyVo9cltWzIuqyz8a-cVDj1rJ1vHMOX4WzSXk4Mblyh54oBA6V7VvQf0hWWI1YRBo2O8EGmqIXfbch5keNWx8-BTpSLD7fcnroVBQb825uYGnD8i4WUpzQ7W3CDzpLihpcIjsa9ScKRWuZ2NGocLO0HNTKK23FstUhT0wUACxWIoG8xWwoJD2jNmhAMWbm_XnOrh_C1Ham3hdI3A4jkALG7OoWYNVdiVZN-c8dc2NsRG20zlCUpJdYcSiMKNm7OptZnIZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CwLA-UeYxwaoGYXQavVr5MV4UxRnqFu-9_0wZ-3SuAzJNswnDmLRlsbtzPEXMS6Z8iuxHGC-7A-q_op81s6dXCuJp_mMA8jJv7Kk1YcJnOCpxqdt5p5sNYp8k_N4MszVp2CN7HJypkk8hE6wNAR-4AKywqj1Xte06EVLK5S7h62Lvya7fMcJugw6e0WZJxXA7Q2Wqo70rTHQCAdZqC6bXiRUS4cep65BUKcWNBQJ7xvDtGy4qMPupuCKxBpdfmAVKQxETKAf_DuzQtsnn5Hjc1yxnWEPc_kLYr5HgEQeaeqqmtPO4-C62aGmazLyEiZ7HhkqZjVFllvGQQAbckruIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTchlRurzGGEzdyAMH6rMRSwaDeOrJpRI1w6H_BNSe839CpvEAeDp3cghetLaPu-8E6tLBcWnH6dC_W_eWFDyxnaEBnEycwTFoiOdoZIjtNgh4ppPjsgrG07l5ujfzXnjnB7ztF6Zcd7U_KBNtgRGas6kMIAJXxJBNqHGCbT8T7jx0iuDeUw-DriPiIDFoam6fkaXz7YQxZWlqHCLkmxICVxVRr_AzwP7A0r_wxai7SGVJouiSyVkdJ-wOSyIs4hh0dnoog7tvgVqBdy8w2JhXbBjO3K1NLQUw3RDlFGksPf9ibmPVE0BYQJqorZELBMK1e7PtT7DPhkvUThqXzIPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هم اکنون دیدار ترامپ نتانیاهو و هگست و روبیو/کاخ سفید
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/138214" target="_blank">📅 19:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138213">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pvf2d5mCOSnRE3cZUzftB7HIOmlekZ2QkcGw1de1ZvBlsAd_zUGSbA78Aq4uF4mgHK_dsKZ6QKgG8SvRNsLrjPjulsCrgmdhP9Rm7nwW2r8a1sicDdgouBeEsbZ8pkw7bZTJjxd4FkfKRAFCUs0GY_fcY6W6iSlatvDSKT_jgQidVm3cgtQCRex2Zw6FjBlDRRHB7FCikQ7AnjdgA9_yecMM0EHAIaZ3OVNyCD5t-Uco_aI7dx73__ayR6ErvFRhA-DM_g7pl676x7ooJxxyVP005yqKIXCmgS9y-t7ozIh6dEefG31qJpsphy8Da2MRx9SDumJ3HajQ3awW_Nsb9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اولین تصویر از دیدار نتانیاهو و ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/138213" target="_blank">📅 19:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138212">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
لایحه جدید سنای آمریکا برای تحریم ایران
🔴
به گزارش بلومبرگ، گروهی از سناتورهای آمریکایی از هر دو حزب این کشور روز سه‌شنبه از توافق بر سرِ لایحه‌ای خبر دادند که به واشنگتن اجازه می‌دهد محدودیت‌های بیشتری را بر خریداران عمدهٔ انرژی روسیه و ایران اعمال کند.
🔴
این لایحه تحریم‌ها علیه ایران را تمدید کرده و صادرات گاز و نفت روسیه را هدف قرار می‌دهد.
🔴
این قانون، قانون تحریم‌های ایران مصوب سال ۱۹۹۶ را تا سال ۲۰۳۱ تمدید می‌کند. طرح مذکور، تحریم‌های اقتصادی ثانویه را بر شرکت‌های غیرآمریکایی که با ایران تجارت می‌کنند اعمال می‌کند، تحریم‌هایی که قرار بود امسال منقضی شود.
🔴
رأی‌گیری مقدماتی لایحه برای صبح روز چهارشنبه برنامه‌ریزی شده است.
🔴
آمریکا در چارچوب یادداشت تفاهم متعهد شده بود که در طول دو ماه مذاکرات با ایران تحریم‌های جدیدی علیه تهران اعمال نکند، اما تاکنون چندین تحریم دیگر را علیه افراد و نهاد‌های مرتبط با ایران اعلام کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/138212" target="_blank">📅 19:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138211">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
زلنسکی: من با رئیس جمهور ترامپ در مورد روند دیپلماتیک، احیای آن و مجوزهای تولید موشک‌های پاتریوت صحبت کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/138211" target="_blank">📅 19:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138210">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lopBt_1p2I4m1oapPAAaCqQX0OBykoGUhrPzFLhdyPVF0uokj-tZ301dq92lr24Qmtb1hDj40C_XbvRwnfeTevJzPmctQaPl9cdqvRG6MtX81CuTN1VxSY_JGl-L4Bw8McBHSugDBrZ5QdsPRBtdK7ozbKRFqG3XfXOrA4oVFkApa4ZY6pIqEoeHJIPEYJVz2BaK8kp37AJU8cOoIYtr263JmXR8Mal77KWwDpYVa7_ZHAZranjHyNWYcyy0KFsMWkKus-yJT5ESRcWSwRV8nUdKupNldfsC9cBX6KmDFOLVsdIIO4eNVGafS--LThyd0WxqERLeUuIy0-Zu63XMRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قطر به تنهایی ۲۰ درصد LNG جهان را تامین می‌کرد و دومین صادرکننده جهان است جنگ ایران به توقف صادرات قطر منجر شده و بازار LNG را بشدت تحت فشار قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/138210" target="_blank">📅 19:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138209">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N81OHPR9XuDHCkkUD0SuCiJxlBL40ybYA53QwCK4R6mO43NzKovvRUxjQ-P8qACceiQnHvNtwpuuzZFY1oLCR9tNPBVYP3uqumeta9ogRQsisJnotUq8uycnlFIz7yI6-yttZKhmk9OLX-FkcLbcV_CZjC-lMMmE3Meb3hDTu36ASopLgLKkhrB3wKzg5OORGhu_irFPVcoBVmBPkMkjwazQ6lhhBkf4alQcIgmq8UnSSoIiife-NcdoW8Yqe4blSZiBdUf7UKNqb8GRejyraD56oZqIcH1Y8kbUO1EkTlnLOp9138EHeDcDXyArSc7jEPBh_3KXijJGj8-qcTvYow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین در ماه ژوئن ۱۷۳ تن طلا وارد کرده که بیشترین میزان از مارس ۲۰۲۴ است.
🔴
در نیمه نخست سال هم در مجموع واردات طلا چین به  ۸۲۰ تن رسیده که دومین واردات بزرگ در نیمه نخست سال و پس از ۶ ماه نخست ۲۰۲۴ است.
🔴
چینی‌ها در حال خرید طلا در کف هستند و تقاضا خرد برای طلا در چین همچنان قوی است ETFهای طلا در چین هم با ورود پول معادل ۲۸ تن از شروع سال مواجه بوده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/138209" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138208">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، برای گفتگو با پرزیدنت ترامپ به کاخ سفید رسید.
🔴
این هفتمین دیدار نتانیاهو با ترامپ از زمان به‌کارگیری او است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/138208" target="_blank">📅 18:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138207">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
باراک راوید، خبرنگار اکسیوس: یک مقام ارشد کاخ سفید گفت «ترامپ در مصاحبه با شبکه فاکس‌نیوز قصد داشت پیش از دیدار با بنیامین نتانیاهو، پیامی قاطع و سخت‌گیرانه به او منتقل کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/138207" target="_blank">📅 18:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138206">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
زلنسکی بدون برگزاری هرگونه کنفرانس خبری، کاخ سفید را ترک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/138206" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138205">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Agy-j8m-k8xLjmB0PBKjlArFFXQKcQUm1vqKcfloLjX_DgRYxsTnS1C3uAX-rGgEZmteN8TavJPhvEzv6BeL4OlOnEhi8UefaXlo7BDRJ-csZszrgJZAXbOUHIrMgoE1EV6e2YpKGNgA8gWqnOUKP1dN1Qef0gAPMXkGGz-Oafv-0EnD1D6aqsAuy05jmp3QaOWDlq2LGzHL8OQURhvYVv2KmOs52z96YVXRkZAU9KYMr4UIiQB1o_vWb-inFuLnT6sOCajWcs54UqzQcdS_oipqsqG87VGE2JyaBQxZkNBniTSMByr4D4rWGZ_vx8t6b6rrMB-DCzfRqL8hXhqtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندار کاشان: ادارات یک هفته وقت دارند تا نیروهای مجردشان رو شناسایی و کمک کنند تا زودتر ازدواج کنند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/138205" target="_blank">📅 18:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138204">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YV8yIQxKkIA0pn0xYogP_SsKsq4OpNfe158I_7nQXHE65_wYAJzIMnXY_YNamUloo9a6ESSg5l9X0iKeRGbyQvNdwcoqebv8pPpy070fRg0hGyyBXTBzo-iSVyXVT3HaLIgY51yp94HNboOB5yYySnOb15vR4CQ3d85A1EqG1V9iZxvwbXHFI-nhKLDPkV6w_t9yra7ZhMNQzhTl7trwy6XYT963nc7HZpFv0h4wGKg8t1eiTsdJaurX68DClqDPxU_RXI2j03uRAs9KkKx_TLXhkOpbXO_3TtpDcaR7s1lsJ677H-rn9mE0oX-cC6kM5tSRF8lQd1WFfi2tA_Qh_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده نیروی قدس سپاه: دولت عربستان از تجربه رفتارهای غیرعاقلانه و پرهزینه آمریکا عبرت بگیرد و محاصره یمن را پایان دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/138204" target="_blank">📅 18:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138203">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xb-pBVwXqmtah1VoU95ROKFC1PrzbQTRiIoqPHaEbTtH4cQixBA8KosgBRyHxIcNduPixUqoJ3GWHIeziURuAhlk8sJe3EqOVcUbwjrMzVOp6VUwIcj73KYumKt5uK-D0lHNZMgvPwTjgxj1aw4Fy82Vwt6GuRBf-Qn7cbZAhv0TZUIAFceUSqPgGBamTQ9qUdIAS00NukknAIE_zksbEFANsqFqiSbfqL4lLGh4esL3WWntKuSXDazPxZrp-Pp27x4GCHn4Z39ID1zyv_SUmPcA_mK9kBEzCoM5TDgWnsT3WKVMUkXonPMp8gVI2wFwIHafmHit7rexMbZzFUoA-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ورود نتانیاهو به کاخ سفید برای دیدار با ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/138203" target="_blank">📅 18:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138202">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f588936643.mp4?token=EYJoMzNwejB6dI0sFNZTcnb3cBVt8Wa0cLlliDkE9UY-mbNaijZ_RB4t_tkIfCB1TS8nMakV_O81gBTQbs8xBHqnO_lFZV7sHgZ_4t6lNQ-nt3NdaDaPjEJDTQFlfFqeG8R-wc-Oe_UQg0luievitfUAm6rzLPrBW64SWLj2vIHb0ImivJ661IwXAijQcjKGh1M9tRaESHQZlf4UDIDNZuoR_Q7B3DmfTaOFJSlZWnMzt8SGoBGiSiF-6sTjwRmyZfAaEe5QOrnigqcHdwqmb3scnuSusYyFFlsLBjxWUo3aktXlfLWpRj6PFxh6Yn_yf2zz7gHFsff_D1L70VT5PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f588936643.mp4?token=EYJoMzNwejB6dI0sFNZTcnb3cBVt8Wa0cLlliDkE9UY-mbNaijZ_RB4t_tkIfCB1TS8nMakV_O81gBTQbs8xBHqnO_lFZV7sHgZ_4t6lNQ-nt3NdaDaPjEJDTQFlfFqeG8R-wc-Oe_UQg0luievitfUAm6rzLPrBW64SWLj2vIHb0ImivJ661IwXAijQcjKGh1M9tRaESHQZlf4UDIDNZuoR_Q7B3DmfTaOFJSlZWnMzt8SGoBGiSiF-6sTjwRmyZfAaEe5QOrnigqcHdwqmb3scnuSusYyFFlsLBjxWUo3aktXlfLWpRj6PFxh6Yn_yf2zz7gHFsff_D1L70VT5PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رهبر اپوزیسیون اسرائیل، یاایر لاپید:
اعتماد دو حزبی اسرائیل را در ایالات متحده بازگردانید. چگونه؟ اولین قدم کاملاً واضح است.
🔴
بنجامین نتانیاهو و گروه او از افراط‌گرایانی را که ما را در داخل و خارج از کشور از هم می‌پاشند، به دوران بازنشستگی بفرستید.
🔴
به دنیا بگویید که این یک دوره دیوانه‌وار بود. یک دوره دیوانه‌وار. و اینکه این دوره به پایان رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/138202" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138201">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
مشاور امنیت ملی عراق: مقامات ما چند فرد که متهم به همکاری با اوکراین و انجام حملاتی در داخل عراق هستند را بازداشت کرده‌اند
🔴
مظنونان اعتراف کرده‌اند که برای اوکراین کار می‌کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/138201" target="_blank">📅 18:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138200">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
نتانیاهو برای دیدار با ترامپ وارد کاخ سفید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/138200" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138199">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8bef0b40e.mp4?token=gyNzqspK_-2HHPbx2eBtg8L5203h5nUR5MfNChoeahwuQkT_M5TSpwiXCPM69IKzMayXehtPqdkjrZep2z3OCJZ5PkkS6fu6nhbianjLq1i-C64Jm5AqzzRAkFPkd4iCE-p81iXaW83hpI1tzQr3AuHXpZDt0DaBbRrjK842H5mUahixvsbYRbpYevl4SWmqGIKVvOCJ963d0B_fgSQOY1195i2aJJgY0LWqyqaUw6b5fWcC4BxjN-vB-j58L-Xh09rDdJEMBr6iO1uX3Aw2CSOxMWG9QXZ9vvBzE3i9VYGCGHBQoVIMKBSBEV1NLaxrMNbBP1HINz0FX1PzR1PbNKJKEj_23POy1Y7xURDjdceKwPrEd8nvq8NMf3BDNyTUUl8QNL6rq2J_w3P18-OTh6UbZC2Ua6iHvROWq8d1K3UtvR49eJziJkw56zA5l13AWEf_zawRaimrr60enbxP5-OwAFkPywKDcrA7XL4FtUgTOuqpHnLXSZ-CO9yPPWtGJp32uJXScbyzUiblDemz9YWQRMOEbCSa9p4Pz0MTd79J8A-QA4V7eTltdQC8XpDfWYfPQPbosb_1GEBpCb8_crXZE8us99EI7TIh_AnkQFJbPJLV2eJCUnYrT35vezLhcdcaBg7rorfiKwp-k7XrKzLvch2P7jj-0OGHEpggJFc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8bef0b40e.mp4?token=gyNzqspK_-2HHPbx2eBtg8L5203h5nUR5MfNChoeahwuQkT_M5TSpwiXCPM69IKzMayXehtPqdkjrZep2z3OCJZ5PkkS6fu6nhbianjLq1i-C64Jm5AqzzRAkFPkd4iCE-p81iXaW83hpI1tzQr3AuHXpZDt0DaBbRrjK842H5mUahixvsbYRbpYevl4SWmqGIKVvOCJ963d0B_fgSQOY1195i2aJJgY0LWqyqaUw6b5fWcC4BxjN-vB-j58L-Xh09rDdJEMBr6iO1uX3Aw2CSOxMWG9QXZ9vvBzE3i9VYGCGHBQoVIMKBSBEV1NLaxrMNbBP1HINz0FX1PzR1PbNKJKEj_23POy1Y7xURDjdceKwPrEd8nvq8NMf3BDNyTUUl8QNL6rq2J_w3P18-OTh6UbZC2Ua6iHvROWq8d1K3UtvR49eJziJkw56zA5l13AWEf_zawRaimrr60enbxP5-OwAFkPywKDcrA7XL4FtUgTOuqpHnLXSZ-CO9yPPWtGJp32uJXScbyzUiblDemz9YWQRMOEbCSa9p4Pz0MTd79J8A-QA4V7eTltdQC8XpDfWYfPQPbosb_1GEBpCb8_crXZE8us99EI7TIh_AnkQFJbPJLV2eJCUnYrT35vezLhcdcaBg7rorfiKwp-k7XrKzLvch2P7jj-0OGHEpggJFc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور: ما تازه از یک رویداد خارج شده بودیم و در عقب ماشین سوار بودیم تا به رویداد بعدی برویم.
🔴
لیندزی گراهام داستانی درباره دوران حضورش در مجلس نمایندگان برایم تعریف کرد. و اگر دقیقاً همان چیزی را که به من گفت تکرار کنم، پایان همیشگی زندگی سیاسی من خواهد بود.
🔴
اما آنچه می‌توانم بگویم این است که آن‌قدر خندیدم که وقتی به رویداد بعدی رسیدیم، دچار گرفتگی شکمی شده بودم و به سختی می‌توانستم صحبت کنم، زیرا لیندزی گراهام می‌توانست هر کسی را بخنداند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/138199" target="_blank">📅 18:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138198">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6531958cfb.mp4?token=eRjf3gKV-q6aH8_zIPlU_Nw6rC6Zw4BUl6WXq6_j3-DKP1QiaFwkhiRJIfm8sXvUdZKKcUyHtQAjx4jo0ZAV6TTYcH2ZxUM1htOrgQCom5JmQYqZu0QEAmZ_X3MX4axbx_4bUceMuSXmacvJu8YYTJtLKvUFiqMQ6b-Y2iqc0FAUeTMBSbT5Sz1_7ixZ27yk7KH8SHPbhsV1Hd1X_3Ji_Lf0KOHZX9-ZL6ZMXzhtND0lcQI6tLRa6o_d7RIKT-X_tYYaAVjpido-3dsFKJ4JFSzojCmzekNx9jXFMHCLLJmNPoZXfzDsDS_SMcmb7FFD5948MUiWaSZ7rDmCM6m6iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6531958cfb.mp4?token=eRjf3gKV-q6aH8_zIPlU_Nw6rC6Zw4BUl6WXq6_j3-DKP1QiaFwkhiRJIfm8sXvUdZKKcUyHtQAjx4jo0ZAV6TTYcH2ZxUM1htOrgQCom5JmQYqZu0QEAmZ_X3MX4axbx_4bUceMuSXmacvJu8YYTJtLKvUFiqMQ6b-Y2iqc0FAUeTMBSbT5Sz1_7ixZ27yk7KH8SHPbhsV1Hd1X_3Ji_Lf0KOHZX9-ZL6ZMXzhtND0lcQI6tLRa6o_d7RIKT-X_tYYaAVjpido-3dsFKJ4JFSzojCmzekNx9jXFMHCLLJmNPoZXfzDsDS_SMcmb7FFD5948MUiWaSZ7rDmCM6m6iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس‌جمهور جی‌دی ونس:
لیندزی گراهام به عنوان یک انسان غیرقابل نفی بود و البته به عنوان یک سناتور ایالات متحده نیز همین‌طور.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/138198" target="_blank">📅 18:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138197">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه اردوغان نخست‌وزیر عراقی الزیدی را در مراسمی در مجموعه ریاست‌جمهوری آنکارا به گرمی پذیرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/138197" target="_blank">📅 18:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138196">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMQBYD1HdTCg-AswJR_QI_M6kJxuEEYOBFYAUPN8YJFIKxRQgnX3TO-bE986gQMNroneyLI_4Xn0OCStFg21QYi0KNrEIMvvQ6-OTzfzRNd027VHCHRwIDgBNXwaRbvcbNUQbmBtdBaMTcv8lrsGYehdPeyzDfrVcDepuf_B6OAZ59CprdkNgENO7Og-lmvPOHzMj4pLqCOmdPkXCN0KBrQBnWLV3v4ZExbDa4RDYPTdSXisxxIIO2yaOcCSVjEmiKTQujoGsBSIPH6RiuGBi7sOCUMix9i4amEhYTzXMLoSgHYNQrotjk4ibcsJSQPmW-7oZK6BO5ivh5sfzUh0Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جی دی ونس با ۴۳ درصد در پلی مارکت و با اختلاف نسبت به نفر دوم یعنی مارکو روبیو، شانس اول نامزدی جمهوری خواهان در انتخابات ۲۰۲۸ آمریکاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/138196" target="_blank">📅 18:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138195">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpgfGRubHjEky9bN7yo8q0V_AGSfy6H_0zykj4zeqOYRsueDmxCnoM2uuVLfK_6JNxfCBZFtl2B7TH401lZk2AEWwgrnjMpM-hUbxWjTo_mPaIg-Lslc_MECkT6XU_W8zwxAVe1nhb-ghK9eUUM5uTViIuX5qEmn5d8nzne_nQysJwIL0cdI1pQKNZ9G-yM7kIHu0WH6Scz_sFZRQmYqS90AbfsqAEqGpL-oSfp9u_S4Ctz75WLPC-0FrykjyBopAaaPdbGVfKnBqx8VvE6rcZMGUe3Ut3HgoFfCMNInxrZpmv24OnCkODLLThwzfFdrvRRTgDpyaOVcdm5cemiAtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پژمان بازیگر عشق ابدی رو دعوت کردن شبکه سه...
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138195" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138194">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
العربی الجدید» به نقل از منبع آگاه ایرانی: تحرکات دیپلماتیک برای کاهش تنش در  منطقه و دستیابی به راه‌حل دیپلماتیک در روزهای اخیر شتاب بیشتری گرفته است.
🔴
در دو هفته گذشته، پیشنهادهایی از سوی میانجی‌ها بین دو طرف مبادله شده، اما هنوز به پیشرفت چشمگیری منجر نشده است.
🔴
تبادل پیام‌ها بین تهران و واشنگتن به طور مستمر و بدون وقفه و از طریق بیش از یک کانال ادامه دارد.
🔴
تهران به واشنگتن ابلاغ کرده است که پیش از پایان محاصره دریایی آمریکا و بازگشت این کشور به اجرای تعهداتش، اقدامی برای بازگشایی تنگه هرمز انجام نخواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138194" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138193">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e2bb8d9b8.mp4?token=KPr2KOE5B07LJyo3MiyyQ_A4trYwqfNztOOjD93tcFWSpS9lfdnsZfYl-6iTpSJpyVLB1nxn_irmnZqF5Ew1ioMIE_4VXmGr7E0rDnBxzRnk8JVbVMqxs_wf8RqQr6eDIYzsihIv-xvLYm5b7quQ3S1Exjw60YKml3mgNjI6tET2yfrJRIwxcsxJYQIDQ5NijCzwgmc3iGtEh1MZqW5Iz9tnwk94wo407WJbQ5X-VrUmvsXxp5g2382fQfSg245q2McmE6RcuM6RANgeN--s_oAmMzKYQQQ8ginmTR9a7PkF29X5PRDUf_STPLAsyEtSOfVBQ8965R8S7KxK1etVxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e2bb8d9b8.mp4?token=KPr2KOE5B07LJyo3MiyyQ_A4trYwqfNztOOjD93tcFWSpS9lfdnsZfYl-6iTpSJpyVLB1nxn_irmnZqF5Ew1ioMIE_4VXmGr7E0rDnBxzRnk8JVbVMqxs_wf8RqQr6eDIYzsihIv-xvLYm5b7quQ3S1Exjw60YKml3mgNjI6tET2yfrJRIwxcsxJYQIDQ5NijCzwgmc3iGtEh1MZqW5Iz9tnwk94wo407WJbQ5X-VrUmvsXxp5g2382fQfSg245q2McmE6RcuM6RANgeN--s_oAmMzKYQQQ8ginmTR9a7PkF29X5PRDUf_STPLAsyEtSOfVBQ8965R8S7KxK1etVxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی وارد کاخ سفید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138193" target="_blank">📅 17:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138192">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
یمن: نقض حریم هوایی یمن توسط عربستان با پاسخ قانونی مواجه می‌شود
🔴
وزارت امور خارجه دولت قانونی یمن اعلام کرد که نقض حریم هوایی یمن از سوی عربستان سعودی اقدامی مردود است و با پاسخی که عرف‌ها، قوانین و پیمان‌های بین‌المللی آن را تضمین می‌کنند مواجه خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138192" target="_blank">📅 17:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138191">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e13ebc21.mp4?token=d5r-vRJIy_AKNjtzWzBPkqupTSHSvqw9DAma_7oOiOw9VUMXYkPr6Q7d73nGaAqFs774sGXphrnhfdjOzRkLXeVf2Kxsv4q2O5x8yHbL1oxd6jCajZNu3QbrR4rs6XLAIPi6fu9a1ar0LsOMXZ6nRkTyyEL0OvcKT1nikp6_V7rIrqgYIQvCBIvtNqdgElihRjeMmZ7E3Imy9wH_6Cqg5eQJo2nRCQkblOxVDiCv3Jq_mHViVc0MqsOc4uVPFit5TLJpOViQjSUmhOIOmIf4TvLf2ddptxluSjtECj36exDJNXzeLosACCaNq1fHPwMCwcIWc56IcsSF4rTeg2GKeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e13ebc21.mp4?token=d5r-vRJIy_AKNjtzWzBPkqupTSHSvqw9DAma_7oOiOw9VUMXYkPr6Q7d73nGaAqFs774sGXphrnhfdjOzRkLXeVf2Kxsv4q2O5x8yHbL1oxd6jCajZNu3QbrR4rs6XLAIPi6fu9a1ar0LsOMXZ6nRkTyyEL0OvcKT1nikp6_V7rIrqgYIQvCBIvtNqdgElihRjeMmZ7E3Imy9wH_6Cqg5eQJo2nRCQkblOxVDiCv3Jq_mHViVc0MqsOc4uVPFit5TLJpOViQjSUmhOIOmIf4TvLf2ddptxluSjtECj36exDJNXzeLosACCaNq1fHPwMCwcIWc56IcsSF4rTeg2GKeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای که دیروز گرفته شده‌اند، پیامدهای حملاتی را نشان می‌دهند که زیرساخت‌های نفتی عربستان سعودی در ینبع، در امتداد دریای سرخ را هدف قرار داده‌اند. این تصاویر همچنین آثار سوختگی واضحی را در اطراف یک مخزن کروی شکل متعلق به شرکت آرامکو نشان می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/138191" target="_blank">📅 17:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138190">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ: مذاکرات خوبی با ایران داشتیم
🔴
بهتر است با ایران به توافق برسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/138190" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138189">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
کیفیت هوای تهران برای همه ناسالم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/138189" target="_blank">📅 17:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138188">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ: بعد اینکه ما محاصره دریایی رو برداشتیم، ایران توافق را نقض کرد. ما دوباره آن را برقرار کردیم.
🔴
ما نمی تونیم اجازه بدیم ایران توافق ها رو بشکونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138188" target="_blank">📅 17:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138187">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
آکسیوس: مقامات ارشد آمریکایی معتقدند که فشار اقتصادی ممکن است آسیب بیشتری نسبت به بمباران به تهران وارد کند.
🔴
گزارش‌ها حاکی از آن است که ایران برای پرداخت حقوق جنگجویان خود با مشکل مواجه است و با خطر ورشکستگی بانکی و کمبود بنزین روبروست. یکی از مقامات: «آنها از وزارت خزانه‌داری بیشتر از وزارت جنگ می‌ترسند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138187" target="_blank">📅 17:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138186">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPACGc7tdM5CjRr10triUjKHVSAtTUlSmvYjNpFZc30sCMDe73FXWMnkSNyN6vxcFFvLmNBL9h0xdhplWRtLK6kgQVtlnYPzdE-8XO4RbRc2W4rRk4Te2ubryJ0TzoZgmBX0ri1VxhzUQtyGyvI1Anqoml53v5JAKyYg5QoTqUF8rqexh_UkLSGC5BUuquDzwKk4A--R4csAPxo5a60Fd7c5XqaMGcs2RzUQSsxRwi18L2wSxpQK2GseOCtd4I4EGkaTMX_7Cy-d7oRDqga2OsZXFMcCVcxQsXIbVJXRWcpYy1iFMmCOMKrC18sQtMB4klkn314diqPEoH8ZSf_6Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت اپل برای اولین بار از مرز ۵ تریلیون دلار ارزش بازار فراتر رفت.
🔴
این شرکت، دومین شرکتی است که پس از انویدیا، به این دستاورد دست می‌یابد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/138186" target="_blank">📅 17:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138185">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ: لیندزی گراهام خیلی با ایران مشکل داشت، اما این اواخر یک توافق خوب را ترجیح میداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/138185" target="_blank">📅 17:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138184">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
مراسم یادبودی به مناسبت درگذشت سناتور لیندسی گراهام، دوشنبه شب در هتل فور سیزنز در واشنگتن دی.سی. برگزار شد. این مراسم توسط آنتون سهناوی، تاجر و بانکدار لبنانی، و مورگان اورتگاس، سفیر سابق آمریکا، برگزار گردید.
🔴
در این مراسم، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، و همسرش، سارا نتانیاهو؛ اعضای خانواده گراهام؛ چندین سناتور جمهوری‌خواه؛ و همچنین سناتورهای دموکرات حضور داشتند.
🔴
همچنین، استیون میلر، معاون رئیس ستاد کاخ سفید، به همراه همسرش، کتی میلر؛ مارکوین مولین، وزیر امنیت داخلی؛ و یهچیئل لایتر، سفیر اسرائیل، نیز در این مراسم حضور داشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138184" target="_blank">📅 17:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138183">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ: ما ایران را نابود کردیم. آنها نیروی دریایی و هوایی ندارند، ارتششان تا حد زیادی نابود شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/138183" target="_blank">📅 17:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138182">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
یک منبع ایرانی به رویترز گفت:
عمان ایده‌های دیگری را برای مدیریت تنگه هرمز پیشنهاد کرده است، اما ما هنوز پاسخی نداده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/138182" target="_blank">📅 16:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138181">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری / یدیعوت آحرونوت: نتانیاهو پرونده کوه کلنگ‌گزلا رو روی میز ترامپ میذاره
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138181" target="_blank">📅 16:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138180">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THwHnG5RSBucTG409NclsxCpW6ibLUMzXQ2a4ZF-qlv5j5GdHhfCR0e_2R9DJQEvL0urzoQX6ci0QvhdQL7FMkK4thJBjaO5fQHPb3yTWlnzXP-SoPDyvCJ1ORc_5nTdfGMJym-d0lP0yGLfGEhiDBMn1DprcPLodkO7F_JpSFXP7LczFB7qucdnA0dGjlFo6mBDim-DM4VbBvYJeaEibfDbHY5oCokgujYljC0CQ0dH9dlNnKA36yxDRHQ9YTd4A9EfA8ALlNiCcD6OUgVS4T-doAmr_5VdI4z_59UlJ_BhC54cxTkKRacye-gfF_FlTwqGjCl-d85YEzqquR4bVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آکسیوس:  سه ساعت قبل از دیدارشان، پرزیدنت ترامپ در فاکس نیوز پیام ترسناکی به نتانیاهو فرستاد و ادعا کرد که بی‌بی در مورد کوه کلنگ در ایران صحبت می‌کند تا او را متقاعد کند که در جنگ باقی بماند.
🔴
او تأکید کرد که بی‌بی باید در این مورد خصوصی با او صحبت می‌کرد و به دنیا نمی‌گفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/138180" target="_blank">📅 16:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138179">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
مقامات ترکیه در مجامع مختلف بین المللی بارها آنچه نقض حقوق اقلیت ترک در یونان می خوانند را مطرح و برجسته می کنند. اقلیت تراکیه همچنان به عنوان یکی از موضوعات مورد اختلاف دو کشور به قوت خود باقی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/138179" target="_blank">📅 16:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138178">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ : تنگه تحت کنترل ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/138178" target="_blank">📅 16:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138177">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f7a42bd6.mp4?token=AomNCqL-rDeixVaSB1jwqheU6VNOPJfgKllNjyE6ZO-lsvhLZU0nTtfJka7dQcniU8vqYhj8wusAIdu5iJ4BAokQH3JncP38b-eVYjTpfMk1y8TZdnmdpinTtsezG7oSHaxymU7XCl8AGhpESn92YZViK4gio0mGnIZooO3wGrstmz9-KpcMVY286IlYCYwJb-sZdLt5PwWkyVbUs1TiGkK2RzL8uuMECPhFkg3ib1SRgUrBQ1ME7U1QYnaZAaktQ9GV9T3D2Cj7wMXbRfeeGZrV20nqNe5qZgm_pqWBWzDT0sWc2lWF5jwKc1pNbPKD9WvuASP2t1xggXWGYMkeGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f7a42bd6.mp4?token=AomNCqL-rDeixVaSB1jwqheU6VNOPJfgKllNjyE6ZO-lsvhLZU0nTtfJka7dQcniU8vqYhj8wusAIdu5iJ4BAokQH3JncP38b-eVYjTpfMk1y8TZdnmdpinTtsezG7oSHaxymU7XCl8AGhpESn92YZViK4gio0mGnIZooO3wGrstmz9-KpcMVY286IlYCYwJb-sZdLt5PwWkyVbUs1TiGkK2RzL8uuMECPhFkg3ib1SRgUrBQ1ME7U1QYnaZAaktQ9GV9T3D2Cj7wMXbRfeeGZrV20nqNe5qZgm_pqWBWzDT0sWc2lWF5jwKc1pNbPKD9WvuASP2t1xggXWGYMkeGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران گفت: ما محاصره را برداشتیم، اما بعد آن‌ها توافق را نقض کردند، بنابراین دوباره محاصره را برقرار کردیم.
🔴
آن‌ها توافق را می‌شکنند.
🔴
دیگر نمی‌توانیم اجازه دهیم که توافق‌ها را نقض کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138177" target="_blank">📅 16:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138176">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/741fab9a3b.mp4?token=oFWmWW3vQJ4w6rMBT1Fl67bgk8KSw8XRoK8pWtlcaOujawj0RKxHjJYoActGOKt48fzO2QhilSZfh1odU9f48jSanOhImuRdxokyNQHOQRAGtfE9sGely3BYzzrGqO3uBPGSu9ziewA9ExRF60PnAxsvKlNbCUDBLZbPrzmmEKWzAezUCkYph3bs75n3W0griJrN_A3qWsEp8YhfyYHIRQO67QqfaRby-F8r76No5xnIj5EJ2UCOrv0x0GajXGgJWQeHfGQOl46Pp3P96f6Djb38M6q_akWOwDKC6NxARMBXgdbi5GmNTNRKTEtqzGPQ2ECu56UdMYz7sXzK-NsxCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/741fab9a3b.mp4?token=oFWmWW3vQJ4w6rMBT1Fl67bgk8KSw8XRoK8pWtlcaOujawj0RKxHjJYoActGOKt48fzO2QhilSZfh1odU9f48jSanOhImuRdxokyNQHOQRAGtfE9sGely3BYzzrGqO3uBPGSu9ziewA9ExRF60PnAxsvKlNbCUDBLZbPrzmmEKWzAezUCkYph3bs75n3W0griJrN_A3qWsEp8YhfyYHIRQO67QqfaRby-F8r76No5xnIj5EJ2UCOrv0x0GajXGgJWQeHfGQOl46Pp3P96f6Djb38M6q_akWOwDKC6NxARMBXgdbi5GmNTNRKTEtqzGPQ2ECu56UdMYz7sXzK-NsxCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران گفت: اگر من قاسم سلیمانی را نکشته بودم، شاید او به سلاح هسته‌ای دست پیدا می‌کرد.
🔴
آن‌ها در آن صورت به شکل دیگری فکر می‌کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138176" target="_blank">📅 16:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138175">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده و امارات متحده عربی توافق کرده‌اند تا اولین گروه مشترک دو جانبه را برای تسریع در توسعه کاربردهای هوش مصنوعی نظامی ایجاد کنند.
🔴
این طرح، که با نام "گروه ویژه سیناپس تالون" شناخته می‌شود، انتظار می‌رود در هفته‌های آینده به طور رسمی آغاز به کار کند. این گروه ویژه که در ابوظبی مستقر خواهد بود، شامل حدود 20 نفر از متخصصان آمریکایی و اماراتی در زمینه‌های هوش مصنوعی، داده و امنیت سایبری خواهد بود.
🔴
این گروه ویژه بر ادغام هوش مصنوعی در حوزه‌های پشتیبانی اطلاعاتی، حفاظت از زیرساخت‌های حیاتی و پایش امنیت منطقه‌ای تمرکز خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138175" target="_blank">📅 16:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138174">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e377889b.mp4?token=n9VUT-CEny-S501kLp-728VPqiMuzSM5hthJVSh-9Td0MQdf3aAhqoVfnVysPNHYojudHMvBPzY1Th1A_sEuOkcJaQVrvotRrI56BwxTghKn6bH19AUoHGDTiWd3CHsvKdUuLICtXUMfQg8yQakWC45wxw9vJKV_v35WgEkfQwGLfyG-bKHt7V-GK0AkoffxI6-p2XNe5_6uEv545_rtnrDsKUiMwWSKbGA7Aor4wDpULvYVsisJEx7qJE7QUg8EnOjvKJZpm7Bl58xapIzCKKrdGz_RMoaK2BK_NfX9oo3xbuoJIcX0eCetOvVWuQ1A6TpdumiV-HQe3rYnK1Doyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e377889b.mp4?token=n9VUT-CEny-S501kLp-728VPqiMuzSM5hthJVSh-9Td0MQdf3aAhqoVfnVysPNHYojudHMvBPzY1Th1A_sEuOkcJaQVrvotRrI56BwxTghKn6bH19AUoHGDTiWd3CHsvKdUuLICtXUMfQg8yQakWC45wxw9vJKV_v35WgEkfQwGLfyG-bKHt7V-GK0AkoffxI6-p2XNe5_6uEv545_rtnrDsKUiMwWSKbGA7Aor4wDpULvYVsisJEx7qJE7QUg8EnOjvKJZpm7Bl58xapIzCKKrdGz_RMoaK2BK_NfX9oo3xbuoJIcX0eCetOvVWuQ1A6TpdumiV-HQe3rYnK1Doyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی قرارگاه مرکزی خانم الانبیا: هر شرکت و کشوری که از محل دارایی های ایران مبلغی دریافت کند اجازه عبور از تنگه را نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138174" target="_blank">📅 16:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138173">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87d4b7705a.mp4?token=lGcNGk4nGN8wc9pZFEn9FUu1ir7khgFlz3TLZuKsHzxzxwBxvH3w-i5iMM2DVmbin1Lkm1eEUoopGpl3rJ30z-LLoGlQNLJQZIA3v-sF6q9r5-h0D4athGhHTpKvHj5rY5kyc6ezneKvt4GyylHZq5AwaA2DvXo-fkd4X5B6zLtwFKU_svih9jqUDS8UhK-4g2AFgmG925hLpN2M3ri1TdPG5kDMSwPnEAq3G8uIhvrUzt4A2dva2qOEgze8J-MwcsFmhcx0klkTJc4O0aYhp8y3ebRXPG55r3-AQBbwwoTtS6fugZD9uN7TkVU8FAfbfMlLtJPARqT0I6qKsJqkkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87d4b7705a.mp4?token=lGcNGk4nGN8wc9pZFEn9FUu1ir7khgFlz3TLZuKsHzxzxwBxvH3w-i5iMM2DVmbin1Lkm1eEUoopGpl3rJ30z-LLoGlQNLJQZIA3v-sF6q9r5-h0D4athGhHTpKvHj5rY5kyc6ezneKvt4GyylHZq5AwaA2DvXo-fkd4X5B6zLtwFKU_svih9jqUDS8UhK-4g2AFgmG925hLpN2M3ri1TdPG5kDMSwPnEAq3G8uIhvrUzt4A2dva2qOEgze8J-MwcsFmhcx0klkTJc4O0aYhp8y3ebRXPG55r3-AQBbwwoTtS6fugZD9uN7TkVU8FAfbfMlLtJPARqT0I6qKsJqkkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
همچین موجودی با این سطح از درک سیاسی و روابط بین الملل، نماینده مجلس این کشوره!
🔴
شما به چهره مجری که اقلا دو دوتا چهارتای روابط بین‌الملل رو میفهمه و همچنین به چهره قشقاوی دقت کنید!
🔴
در حیرت هستند و جالبه که اعتماد بنفس بالایی داره چون تصور میکنه حرف خیلی مهمی زده!
🤔
یه مشت گوسفند افسار گسیخته تو مجلس جمع شدن و برای این مملکت تصمیم میگیرن چطوری جیب ملت رو خالی کنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/138173" target="_blank">📅 16:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138172">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73971fb109.mp4?token=dYWhd9x6puCcOjAgmW1WAYD40Cx75bD0xMx2LqzgxNQrynPCOGZHWGZTaFfXjlpcsFheKyVFxwhTd6CC9q_QA7dzrSsA8sZDD9bPsA1yFKKY2shFtdE29nnk6SwNGtWUS_DcCUh90xtSyMLlwE11ghqyMajBiDJI9WtNWwvhvGRM6xx5P8Zxf4840wBeJ6udnr9TuA9oPmvkm36BGItF5MaGWVKYpzxdRnM7xpcBpA3uwsktMuTeKsT9JTr3ICqvgI5pwij9hykMLO_pAQc7ITtBMo6PybDg0qwPySE5TGCK57AV-LslEGaPYm-7uMpGu-UwTt_dFunSa4WRlWqSgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73971fb109.mp4?token=dYWhd9x6puCcOjAgmW1WAYD40Cx75bD0xMx2LqzgxNQrynPCOGZHWGZTaFfXjlpcsFheKyVFxwhTd6CC9q_QA7dzrSsA8sZDD9bPsA1yFKKY2shFtdE29nnk6SwNGtWUS_DcCUh90xtSyMLlwE11ghqyMajBiDJI9WtNWwvhvGRM6xx5P8Zxf4840wBeJ6udnr9TuA9oPmvkm36BGItF5MaGWVKYpzxdRnM7xpcBpA3uwsktMuTeKsT9JTr3ICqvgI5pwij9hykMLO_pAQc7ITtBMo6PybDg0qwPySE5TGCK57AV-LslEGaPYm-7uMpGu-UwTt_dFunSa4WRlWqSgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ برای بار هزارم: اگر من رئیس‌جمهور ایالات متحده نبودم، اسرائیل امروز وجود نداشت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138172" target="_blank">📅 16:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138171">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ در مورد ایران: اوباما فکر می‌کرد می‌تواند با رشوه دادن راه خود را به دوستی با ایران باز کند.
🔴
سپس آن‌ها بیرون رفتند و سعی کردند موشک‌های هسته‌ای توسعه دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138171" target="_blank">📅 16:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138170">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d1d64e4a2.mp4?token=ZtrmodI6cJVtE0UYoP_PbxSbc9TNQa_-w5-d7apfDoABBZ1eRTQ_bq8fdwPRvlMsrHDaAet5Dv--qsC0izIdr-cIfLzfef5mRse5ryczm3uatboLxTLqa9_Am3vT38mRT4Abh6TEb71hxjCj0nlgKSk2epirfpFsIhppovlTHf9tsKGEvrH0xdUd-j7HaUC-gFJQ6hRNeGgDyswlj6mTn05LssiXAevzxpTxxqX9M4kfL8Sz0J2IaWp3mfkfILBmtHNGRWWyExy13ycnSGHy1gtMM1EQqNn0IXvMsrKr2zdvw7IBPyKmp7JIQoEMVdCI_GAmP5zLnRBeDnDmVblCaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d1d64e4a2.mp4?token=ZtrmodI6cJVtE0UYoP_PbxSbc9TNQa_-w5-d7apfDoABBZ1eRTQ_bq8fdwPRvlMsrHDaAet5Dv--qsC0izIdr-cIfLzfef5mRse5ryczm3uatboLxTLqa9_Am3vT38mRT4Abh6TEb71hxjCj0nlgKSk2epirfpFsIhppovlTHf9tsKGEvrH0xdUd-j7HaUC-gFJQ6hRNeGgDyswlj6mTn05LssiXAevzxpTxxqX9M4kfL8Sz0J2IaWp3mfkfILBmtHNGRWWyExy13ycnSGHy1gtMM1EQqNn0IXvMsrKr2zdvw7IBPyKmp7JIQoEMVdCI_GAmP5zLnRBeDnDmVblCaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / ترامپ:«آن‌ها با نداشتن سلاح هسته‌ای موافقت کرده‌اند. در اصل، فقط باید این موضوع را به‌صورت رسمی نهایی و مکتوب کنیم، اما آن‌ها موافقت خود را اعلام کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138170" target="_blank">📅 16:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138169">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec79b34881.mp4?token=O1OzJbH8sZnOjgnN7FbhnfkWeLdLCb2Cd2GfXPTroLZHZ2A6G5etd7hh5czG_hPcWR9M2iaFFLPtSBjqcOM55PrHuq7yL4jj0qlxcfYzGPCyPoMs9ZTysf7z5AyQ6X_Rvc2lqDHlLldbcxdMNAZYgUfMY4Q8N5vMIC_SMM-nCWIjhxEgfJYkgQQWh0M6vUDfzcRS9-tIBDoQBcUuKqQbVWoAhTkXhGnHGIj3386F4FzIqPUQQ4DSZsypiJFLEHcREZxbBbEzDs8YLEhVhVZq1EJFOZCnhV_ByN40osLimMrrMGp344MGhofeTBQFhCZ33gO-mUo3-jHMaaqY9jk4l7jEG-GRkPY2N_1c5Z4Q7vi7uEXGA9nkUrmSJje4YYzEkEbSG9Pb0q0kfeI7eXNPmTYPb86hDCTjAEz4z389erE2hSGe341EAdYSgElbEihxqPxLt35rrLpGsYmQUxLLVz12PFWsInwewxr21vEYUYTPvBXzNbfK_S6HuhMIe45ZOKTHd08WmsrzeIWF-dCRlyu65PEfnuJBXcENRaHCEEDg9PlVMjJ8md8a0_rgW6LLiwvTT04qbhH_Zh27k3dZOAAD_eorPrwyfJPP-AWknpUHFzfXHorbnXUUVI_Fac8muoKD_blIhJogTN0_0CjF3FI3kOGR2fBs_Gb2pD6ukJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec79b34881.mp4?token=O1OzJbH8sZnOjgnN7FbhnfkWeLdLCb2Cd2GfXPTroLZHZ2A6G5etd7hh5czG_hPcWR9M2iaFFLPtSBjqcOM55PrHuq7yL4jj0qlxcfYzGPCyPoMs9ZTysf7z5AyQ6X_Rvc2lqDHlLldbcxdMNAZYgUfMY4Q8N5vMIC_SMM-nCWIjhxEgfJYkgQQWh0M6vUDfzcRS9-tIBDoQBcUuKqQbVWoAhTkXhGnHGIj3386F4FzIqPUQQ4DSZsypiJFLEHcREZxbBbEzDs8YLEhVhVZq1EJFOZCnhV_ByN40osLimMrrMGp344MGhofeTBQFhCZ33gO-mUo3-jHMaaqY9jk4l7jEG-GRkPY2N_1c5Z4Q7vi7uEXGA9nkUrmSJje4YYzEkEbSG9Pb0q0kfeI7eXNPmTYPb86hDCTjAEz4z389erE2hSGe341EAdYSgElbEihxqPxLt35rrLpGsYmQUxLLVz12PFWsInwewxr21vEYUYTPvBXzNbfK_S6HuhMIe45ZOKTHd08WmsrzeIWF-dCRlyu65PEfnuJBXcENRaHCEEDg9PlVMjJ8md8a0_rgW6LLiwvTT04qbhH_Zh27k3dZOAAD_eorPrwyfJPP-AWknpUHFzfXHorbnXUUVI_Fac8muoKD_blIhJogTN0_0CjF3FI3kOGR2fBs_Gb2pD6ukJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: «اگر به عقب برگردم و کار را تمام کنم، همانطور که برخی افراد دوست دارند، با پل‌ها — بسیار به راحتی می‌توانم اکثر پل‌های آن‌ها را در کمتر از یک ساعت از بین ببرم.
🔴
اما می‌دانید، ساخت یک پل ۱۰ سال طول می‌کشد. پل‌ها طولانی‌ترین زمان را می‌برند و نیروگاه‌ها دوم هستند.
🔴
می‌توانم نیروگاه‌ها را در عرض یک روز از کار بیندازم. تمام نیروگاه‌های آن‌ها از بین خواهند رفت.
🔴
حدود ۹۱ میلیون نفر بدون برق، بدون پل‌ها، مجبور به زندگی خواهند بود. و این یک تعادل بسیار، بسیار ظریف است.
🔴
آن‌ها می‌دانند که اگر معامله‌ای انجام ندهند، من آن کار را انجام خواهم داد.
🔴
پل‌ها از بین خواهند رفت — به معنای واقعی. در کمتر از... می‌گویم در دو ساعت، اکثر پل‌ها، پل‌های اصلی، همه از بین خواهند رفت.
🔴
و نیروگاه‌ها در یک روز.
🔴
اگر بتوانم از انجام آن کار اجتناب کنم، دوست دارم از آن اجتناب کنم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138169" target="_blank">📅 16:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138168">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef09b94dd5.mp4?token=ZBCl-IR-Ici9d1lYqnzV7wrWCT6qb94lK8dCrCYCvota_wmbwbvjUdEFiXc0J9i1QhadYCgMmMJKQKxpbZFXZh83VuPOYyD99962iGP2ZvRlcrgCQZVk1tUZ_ByHit9p3O1WrQxwoOIOM1WvlEt1BvfmOGYi6bJZRBwHIwZQYyip-aNvwevagMLlB3E5YLGdvQJBPQY_bON5mWRjXrVrm1hjBnhWA75iiM8qJK66NBxsRlw4wCRmnJOIQYgvY_M02oPhpgSs5glerGKCyiz0gAdZT4iUma0oZfHRDfgkLCFyMeBQM9gJXwTpE7NfbeODXqWAqoIJEVGuNqCtjBexuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef09b94dd5.mp4?token=ZBCl-IR-Ici9d1lYqnzV7wrWCT6qb94lK8dCrCYCvota_wmbwbvjUdEFiXc0J9i1QhadYCgMmMJKQKxpbZFXZh83VuPOYyD99962iGP2ZvRlcrgCQZVk1tUZ_ByHit9p3O1WrQxwoOIOM1WvlEt1BvfmOGYi6bJZRBwHIwZQYyip-aNvwevagMLlB3E5YLGdvQJBPQY_bON5mWRjXrVrm1hjBnhWA75iiM8qJK66NBxsRlw4wCRmnJOIQYgvY_M02oPhpgSs5glerGKCyiz0gAdZT4iUma0oZfHRDfgkLCFyMeBQM9gJXwTpE7NfbeODXqWAqoIJEVGuNqCtjBexuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
لیندسی گراهام در مورد اوکراین بسیار نظامی‌گرا بود.
🔴
لیندسی صادقانه بگویم جنگ را دوست داشت.
🔴
او هرگز جنگی ندیده که دوست نداشته باشد. او بسیار درگیر آن بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138168" target="_blank">📅 16:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138167">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: ایران می‌تواند چند مین دریایی کار بگذارد و هرج و مرج ایجاد کند، اما ما تنگه هرمز را کنترل می‌کنیم.
🔴
محاصره دریایی که ما در حال حاضر بر ایران اعمال کرده‌ایم، چنان قدرتمند است که هیچ‌کس نمی‌تواند در آن نفوذ کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138167" target="_blank">📅 16:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138166">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: ما پدافند هوایی ایران را نابود کردیم، همانطور که بخش زیادی از تسلیحات آنها را نابود کردیم.
🔴
ما در موضع بسیار قوی در برابر ایران هستیم و من می‌توانم اکثر پل‌های ایران را در کمتر از یک ساعت خراب کنم.
🔴
اگر ایران با ما معامله نکند، برمی‌گردم و کار را تمام می‌کنم.
🔴
جمهوری‌خواهان زیادی هستند که می‌خواهند من به اقدام نظامی علیه ایران ادامه دهم و آن را پیش ببرم.
🔴
دیگر نمی‌توانیم به ایران اجازه دهیم توافقات را نقض کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/138166" target="_blank">📅 16:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138165">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ : «نیازی ندارم که بیبی (بنیامین نتانیاهو) درباره این موضوع چیزی به من بگوید. بیبی این حرف‌ها را می‌زند چون می‌خواهد همچنان در این موضوع دخیل بماند. به او گفتم: چرا باید این را به من بگویی؟ اگر توافقی صورت نگیرد، آن سایت را به‌راحتی نابود خواهیم کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/138165" target="_blank">📅 16:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138164">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ: اکنون زمان آن رسیده است که ایران به توافق برسد. ما نمی‌خواهیم به پل‌ها و نیروگاه‌ها حمله کنیم.
🔴
ترامپ به فاکس نیوز: دستیابی به توافق با ایران بهتر از ویران کردن باقی‌مانده‌ این کشور است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138164" target="_blank">📅 16:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138163">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ونس پس از چندروز غیبت، در دیدار نتانیاهو و ترامپ در واشنگتن شرکت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138163" target="_blank">📅 16:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138162">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcNf5BlndsXQmCNG7eX5nuHn4_W02FygxgfZ4PBj0kDBGWQuqqMqGMDU3DGmQOAyzeVNPtPeWrNzrkvwOAH52NF0JlKuTmQEqGYtUo_UEO6ELHhk6ERYkCRScHByBQOw1YYH7wx_vqzdnYFyF90aMNYRPKC6H-ShjPn7ZHq-RzHMnlhqNbgnLQ6j1yXg7UynmO9Khd4PlPLcugPnAeLTYIjq0I4AaUxr6voyFNuXxkXZmhc-ygh_t3Q67C7BFHayBARHcSI9L4HxV9iF05uIEYO7b15nW16HAYJj3aJybV_hYSRatEa4H5qkvvxMjZN1v3EeURy8nP3guTr-vOlUvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از یک دیپلمات ایرانی
:
تهران می‌خواهد پیش از انتخابات میان دوره.ای کنگره در نوامبر آینده به یک توافق جامع با آمریکا دست یابد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138162" target="_blank">📅 16:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138161">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ به دنبال توانایی‌های اخیر اوکراین در زمینه پهپاد‌ها و مقاومت این کشور در برابر روسیه، دیدگاه مثبت‌تری نسبت به زلنسکی پیدا کرده
🔴
در عین حال، رئیس‌جمهور آمریکا نسبت به پوتین بدبین‌تر شده
🔴
ترامپ به فناوری‌های دفاعی کی‌یف نیز علاقه نشان داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138161" target="_blank">📅 16:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138160">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ایموجی خنده تا اطلاع ثانوی برای غم‌ ملت غیرفعال شد</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/138160" target="_blank">📅 16:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138159">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N0rH2srbHYD_btDzZ1sbD0gWA6C6VOh3Emn0rqUpxrIjNQLiOscGkAFP4AGnAsgqZ2QQmU_pscaZHhlJ3YJSLlbJjx0vGlA6q6HDlFoyVNvwldo9BXPmZeg2k5B68fjRlNzLD1rAutgCrMZwBgCoIEnYCfy-opQAG8zFk3ncSqZ1w4uf9T_K-lDaYmN_sslK8hryY3wp7M1qSbHgsEx64Qgs7TEkh5UIRGSP9fxUWDUxdkSkVyCFCXae3y2KxDB42ozKKDnlogZG-4q_FPr3vJ5VFKNkkMxgCiV3EhhWaTaNZ6nLBDqDMCw0-wkZgao8qz4j1Iy_TNzVhneR2aKSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری شهرزاد همتی خبرنگار روزنامه های شرق و هم میهن برای اعدام دو جوان کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/138159" target="_blank">📅 15:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138158">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4fb160c7.mp4?token=g3iWvyTjZhZ_FOCPgjimN9iDKIgOxqv2upRETEzwEcglJqenOxnUa2wQBei1Y-DSmi8TV2vm8yd8az-DCRSQHo0CrKiLNcS8uFtlr63_lzs_wk-rMSvBOLnXAzMN1uuPHitIPf-AMNSgfdWrOgPOfC9EJsjXGLxqFTVE__bTtRhiAtuodSZBggHXn0kvuE1lMJd8QGycAn6xlPX_iKB0kAvMq3IdlomL8Acclab63Vzi1JWnyVb_UpKY34uBHpdhoN9jfzWOkfFXhuaROeXNcM7XS2DANXrxB9S2DrzlaSlkoc1SW_UAJp1nMAhYTvCM241hmXUSnhByV9_fceKQpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4fb160c7.mp4?token=g3iWvyTjZhZ_FOCPgjimN9iDKIgOxqv2upRETEzwEcglJqenOxnUa2wQBei1Y-DSmi8TV2vm8yd8az-DCRSQHo0CrKiLNcS8uFtlr63_lzs_wk-rMSvBOLnXAzMN1uuPHitIPf-AMNSgfdWrOgPOfC9EJsjXGLxqFTVE__bTtRhiAtuodSZBggHXn0kvuE1lMJd8QGycAn6xlPX_iKB0kAvMq3IdlomL8Acclab63Vzi1JWnyVb_UpKY34uBHpdhoN9jfzWOkfFXhuaROeXNcM7XS2DANXrxB9S2DrzlaSlkoc1SW_UAJp1nMAhYTvCM241hmXUSnhByV9_fceKQpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبر کشته شدن آناهیتا آذر که از دیشب تو رسانه ها در حال دست به دست شدن بود، توسط خود ایشون تکذیب شد.
ایشون گفت از کسانی که اولین بار این خبر رو پخش کردن شکایت کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/138158" target="_blank">📅 15:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138157">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
نخست‌وزیر عراق وارد ترکیه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138157" target="_blank">📅 15:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138156">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
طبق گزارشات متعدد اوپراتور های تلفن همراه به اینترنت بین الملل ضریب ۲.۷ دادن یعنی مردم اگه ۱ گیگ اینترنت مصرف کنن اونا ۲.۷ گیگ ازشون کم میکنن و اینطوری بسته های اینترنت با سرعت چند برابر تموم میشه تا مجبور بشید زود به زود بسته بگیرید...
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138156" target="_blank">📅 15:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138155">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
کاش سگ توله‌های فاسد مسئولین هم اعدام‌ میشدن، هر گوهی بخوان میخورن و صدای امت معکوس هم درنمیاد</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138155" target="_blank">📅 15:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138153">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nqci7KeZl6lkCE0rpcKTtS5zOn2o-DHq6thRyqHS2UdnsZlgLDl1MKgy2z4Cvb2pkIbEm7vQPGA6EHOvJ6_GidCA-Oz4IWfnOmEuYt7JknVr9M_etkfgtSOMNGCC3BlGMsKUaSMXZNTKQvcwTkXfenSwxuZcrmm949y5nTG2KbmahlHSX70oFlCi0ui-c-iQ_CXNMEwDIpVIlouJcWnI_4t9VbLq_jSghlVjHgwOTgZQJky4zj_o77zWMa6FSX2FatZOb8nTWH6AR25SQfdjrXHSKoL4d2V-vpeVtnkgEgJ65l9fBQPxRG3TiH-i7VtpaKcSF2YV0HmHM2h3zYhA2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aWv3PUdxCYxgbKfkL3qxeUI0Mn4hTXlPMVI8THGumFLAELF_NrkUVyyGbsFpU2c0guRxYb7HUam1asTKaO4fR-W_SPDsmTl2srAjSl-Ql8R-83fhDpDaWn1jOEdK-KZrU35vKvAFEBuZPShBYZCdebPHrlt_GIIVlzNt7p710VJ0cNy9jq7hyGJ8Rko3Sth7rfGoLBUPpcvjSVxab78uHUNNi7VMrheDUb6fbZ0mTxy5lBMJ2z2DHWJFSdv_6s-hB3tthy5hTrFc2bYRIgixy1WzcN12zLs_uzN4-75XAUb9vZZaM73qlR8pUiyXq-0X0DRegunLsg0qRXOax8jKUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعدام سه جوان دیگر
‼️
🔴
علی دشتی، قائم حسینی و امیرحسین ملکی هم در پرونده میدان علیخانی به اعدام محکوم شدن و از خانواده هاشون برای آخرین ملاقات خواستن راهی زندان بشن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/138153" target="_blank">📅 15:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138152">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سی‌ان‌ان‌ به نقل از مقام کاخ سفید: ترامپ در کاخ سفید با زلنسکی و نتانیاهو به طور جداگانه و پشت سر هم دیدار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/138152" target="_blank">📅 15:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138151">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رویترز: کشورهای خلیج فارس با دریافت داوطلبانه عوارض عبور ایران از تنگه هرمز موافقت کردند
🔴
کشورهای خلیج فارس از طرح ایران برای دریافت داوطلبانه عوارض از کشتی‌های عبوری از تنگه هرمز حمایت کرده‌اند.
🔴
خبرگزاری رویترز به نقل از یک منبع در یکی از کشورهای خلیج فارس این خبر را گزارش می دهد.
🔴
این طرح توسط عمان پیشنهاد شده و هدف آن جبران اختلالات ایجاد شده در تجارت نفت پس از عملیات نظامی آمریکا و اسرائیل علیه ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138151" target="_blank">📅 15:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138150">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
معاون برق و انرژی وزارت نیرو:
محدودیت برقی ۴۸ شهرک صنعتی بزرگ کشور از دو روز به یک روز در هفته کاهش یافت و برای حفظ زنجیره ارزش صنایع، محدودیت‌های تامین برق واحدهای فولادی تولیدکننده اسلب نیز کاهش چشمگیری پیدا کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/138150" target="_blank">📅 15:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138149">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3870346ca.mp4?token=oozE14epcpD310bFkc-mBgTzcgidwMZpttbnLXI2z0WnF1hWhEqxKGER2orUyefbnNwcH60NwhhF493Vq3kE6k0FP_yjiSjfLjzLL9LElWA2fflKWf32TtdHyGVyeBJW1IBC2alad0h7y49-1BvjfwAGgk2Jlj417uvcnHd5N4DkNwDmSfRCIgAp56tFqFkDZzmjMP1Ot5V_0UNbHigxQc1BynCtch0g6mMCmEpa-Q8MgL5SRJwvp-gxrzDW8sWmUJCNkrTDVTY7tlzgCIF2RLoRwOQFM_i63kAlmCkCIDlwncznK630VPHIBxzvpDQo0WyTbzOY5RsfwRhtScTJVb3_faq4CAc3zqAaQwNbcsOGTXhpPX-3HHQghEjL6GwLzb6mTL3WO7_VlCwJF0ebZHujCG3G-x1Ru81hChbkIxoVTY455mDT-bHzhM4mzTBEHgNDWkfq6Y2F5G3CUYM34Wt1l0fbdaGqn4gOUb8ue2TAKFHjoPcro9juj3Ee2mYCSvGlRthU0K6TgBcXmaqFQYL-A7qf3JwhLN2xH83_HMZJeWaLKRtj_F9eb0y6PbFoF-626P_t7YhINXZdlRl0Acr32a0OpqheM7dTPJhNPy5JRwhLoENWQEcWwxDCNJnxiOgPnfg47QuQRnHJs3yUceOj-aphCZXyvdUDYZmM0Rc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3870346ca.mp4?token=oozE14epcpD310bFkc-mBgTzcgidwMZpttbnLXI2z0WnF1hWhEqxKGER2orUyefbnNwcH60NwhhF493Vq3kE6k0FP_yjiSjfLjzLL9LElWA2fflKWf32TtdHyGVyeBJW1IBC2alad0h7y49-1BvjfwAGgk2Jlj417uvcnHd5N4DkNwDmSfRCIgAp56tFqFkDZzmjMP1Ot5V_0UNbHigxQc1BynCtch0g6mMCmEpa-Q8MgL5SRJwvp-gxrzDW8sWmUJCNkrTDVTY7tlzgCIF2RLoRwOQFM_i63kAlmCkCIDlwncznK630VPHIBxzvpDQo0WyTbzOY5RsfwRhtScTJVb3_faq4CAc3zqAaQwNbcsOGTXhpPX-3HHQghEjL6GwLzb6mTL3WO7_VlCwJF0ebZHujCG3G-x1Ru81hChbkIxoVTY455mDT-bHzhM4mzTBEHgNDWkfq6Y2F5G3CUYM34Wt1l0fbdaGqn4gOUb8ue2TAKFHjoPcro9juj3Ee2mYCSvGlRthU0K6TgBcXmaqFQYL-A7qf3JwhLN2xH83_HMZJeWaLKRtj_F9eb0y6PbFoF-626P_t7YhINXZdlRl0Acr32a0OpqheM7dTPJhNPy5JRwhLoENWQEcWwxDCNJnxiOgPnfg47QuQRnHJs3yUceOj-aphCZXyvdUDYZmM0Rc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌زمان با ورود بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به واشنگتن برای گفت‌وگو با دونالد ترامپ، رئیس‌جمهور آمریکا، گروهی از معترضان با تجمع در مسیر حرکت کاروان موتوری وی، علیه او شعار سر دادند.
🔴
معترضان با در دست داشتن پرچم‌های فلسطین، شعارهایی از جمله «لعنت به تو، بی‌بی» و «جنایتکار جنگی» سر دادند و خواستار بازداشت نخست‌وزیر اسرائیل شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/138149" target="_blank">📅 15:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138148">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHwMA5KJO-cbwAyh4zPQWLMeQxSu2p2pbO0s9Z_NU2foADZlsDo2av_5UwvQaNn2oqYu3B_1jPgR3T4HUap2ZNmnbjLYHHUiVdIZd5x8FmBwyMx8UUmfiCEl6zUan__shzqE7iftAB7D6A9eb6ut8iNFt4xvrJ8NFSVuDXec4LGAx5AVRKj7OZ1gBnVczy8x4LuH63uOF3L2KcjppKpEptxHjYgFZcF_ISTVP6yFEzekQUYKiQRgzlY6APrf_pFyuLCi9owcMlljaDabrY4VD9tAz6PS5nIuXGomtisFIMmEyGfkHmzF0A6zcFWBwSvhPwWR1y6jkY4KcE4PrfaMTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی الزیدی، نخست وزیر عراق، همچنان به سفرهایش ادامه می دهد.
🔴
او پس از سفر به آمریکا، ایران و عربستان حالا به زودی به ترکیه سفر می کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/138148" target="_blank">📅 15:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138147">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
بانک مرکزی از ثبت تورم ۵۷.۷ درصدی در دوازده‌ماهه منتهی به خرداد ۱۴۰۵ خبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/138147" target="_blank">📅 15:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138146">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
نکبت 57 بوجود اومد چون چپ نفهم فقط میخواست با فلاکت زندگی کنه ولی بعد از آوردن خمینی آفتابه بدست به ایران، خودشون از کشور فرار کردن رفتن تا مردم ایران سالها در رنج و بدبختی با یک مشت بی عقل دینی زندگی کنن و هر صبح با صدای اذانشون کسی رو در این خاک اعدام کنن.
🤔
تخم انتقامی که در دل این مردم کاشتید، تا تک تکون رو اخته نکنن، ایران رنگ آرامش رو نمیبینه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/138146" target="_blank">📅 15:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138145">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/229e970aee.mp4?token=UX7x12zY6DWwbDt8SGPsqMvn3QCudPx10nMsLDvWjN60KQZwzoFhK4pCrPfRgTqq0AKo9PZUyohlSuEuo4wzZDb7Iwza1qzWXWOXTMADJtB4UCu0IzCiBmPLNFHFAvxOsLdgmewq7OTDYv5v8aHAQW_OA_H6jjb682rnfRZrBLz__pibqe7n46gpzzeNtr0D5G-YgJIgm1wUj6fD5GFMYRJ2ryCNR6I77qH9-Xol6ma85TsLsC00sjJfMA4gJsnt_Cmaa9G5Xsy_yTvw9771ShQQzps7LuGH3P71ndI_MRVVn99i0RH3fiNb0Z31FeX6ft0ykjzt-aDLqKrDPT9YVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/229e970aee.mp4?token=UX7x12zY6DWwbDt8SGPsqMvn3QCudPx10nMsLDvWjN60KQZwzoFhK4pCrPfRgTqq0AKo9PZUyohlSuEuo4wzZDb7Iwza1qzWXWOXTMADJtB4UCu0IzCiBmPLNFHFAvxOsLdgmewq7OTDYv5v8aHAQW_OA_H6jjb682rnfRZrBLz__pibqe7n46gpzzeNtr0D5G-YgJIgm1wUj6fD5GFMYRJ2ryCNR6I77qH9-Xol6ma85TsLsC00sjJfMA4gJsnt_Cmaa9G5Xsy_yTvw9771ShQQzps7LuGH3P71ndI_MRVVn99i0RH3fiNb0Z31FeX6ft0ykjzt-aDLqKrDPT9YVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امت معکوس جدول‌های مقابل کافه‌های خیابان سنایی تهران رو تخریب کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/138145" target="_blank">📅 15:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138144">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ffba1ed79.mp4?token=NEnE1KwgS2dJi4x6uYYJsJLYuh4_TTyCLiw2TnknD9sLM8xRsoXRluMX5E_JX5vZzeHlwi_cMLu78TUlSwOjsZ7TYHxRLRfAqNZrGlmqmK4J1eq0L4CbuKXv_WnSyGnuugpqKAua2DBKRJI8Igrr9O00g1jEEDI9HdcL2FgdbL7BFlZcdC9TMslK30k8NQiCL0HXQywOimNNwrJIMhTIzqYn77zeexJYATuqXz84NXieHyZSTw30DMpxOynZVkQ3kYTPjC7GrcE0es0umyOYdy259UqTBKZlrHvTxlyBmS5HE4NGGDqcpgZva63mKIHFnfzq1YOmpXe0cZk91OjLwK8FqS-G_4OrsYzpoh45BQF7T05wfiQorB0kZ1ayfVHU8m31IkmRaBhcHVnAJEefll4AyQtu8g6aNco9MjZ7jGfaa7AxNwu5xrRV6Jrlr3X83Bf_KqRoQmz9O0-pmDypmOodU1U3ePq4o1VR6vEh3hZgjKwdt-ADJcyjltns1ViHWK5b7rE8ZKUkrlR-1yhkAnxyjwquLZ16RPdK6f1k42u_4y7XIr7pg0c_ftctjZi7xNRbRzdzRS6qBU-QQ-FjQbYcikPKsZCdNLXffPGasaFp55JdOUSLEKSW2TgyLqnIF-p0Ha2l-cDLh9O5tjqlBnX5-oyeMu1CVnd0dJf9gDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ffba1ed79.mp4?token=NEnE1KwgS2dJi4x6uYYJsJLYuh4_TTyCLiw2TnknD9sLM8xRsoXRluMX5E_JX5vZzeHlwi_cMLu78TUlSwOjsZ7TYHxRLRfAqNZrGlmqmK4J1eq0L4CbuKXv_WnSyGnuugpqKAua2DBKRJI8Igrr9O00g1jEEDI9HdcL2FgdbL7BFlZcdC9TMslK30k8NQiCL0HXQywOimNNwrJIMhTIzqYn77zeexJYATuqXz84NXieHyZSTw30DMpxOynZVkQ3kYTPjC7GrcE0es0umyOYdy259UqTBKZlrHvTxlyBmS5HE4NGGDqcpgZva63mKIHFnfzq1YOmpXe0cZk91OjLwK8FqS-G_4OrsYzpoh45BQF7T05wfiQorB0kZ1ayfVHU8m31IkmRaBhcHVnAJEefll4AyQtu8g6aNco9MjZ7jGfaa7AxNwu5xrRV6Jrlr3X83Bf_KqRoQmz9O0-pmDypmOodU1U3ePq4o1VR6vEh3hZgjKwdt-ADJcyjltns1ViHWK5b7rE8ZKUkrlR-1yhkAnxyjwquLZ16RPdK6f1k42u_4y7XIr7pg0c_ftctjZi7xNRbRzdzRS6qBU-QQ-FjQbYcikPKsZCdNLXffPGasaFp55JdOUSLEKSW2TgyLqnIF-p0Ha2l-cDLh9O5tjqlBnX5-oyeMu1CVnd0dJf9gDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
فروریختن یک مرکز خرید بزرگ در ژاپن در پی وقوع زلزله
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138144" target="_blank">📅 15:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138143">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
روزنامه هیل:  عربستان سعودی هیچ نشانه‌ای از پذیرش شرط تازه دونالد ترامپ مبنی بر عادی‌سازی روابط با اسرائیل در ازای اجرای توافق هسته‌ای با آمریکا بروز نداده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138143" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138142">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1cQdip1xkgLVyDyCrdFLwu4ZnHP6M1YjsjAL8ATO7uLkdHxvljATPo7mSbtF-11ht3Vrvfu8xGVbXCpr1DnGwzo1WXvlFhYPzalSfFPMCO_hSv8htmR7ER-hkJBbWmtz-P-m0CegAIQVxS6WbHB87mr7zrky2_Cd8Z4DaDXLVIBI5cf5HBLii9Qo7hIqlsnyQfzCsj21xqeYyRrxwLsGqTya-_oO_svMmQ2pUPS1SZcL-jqdk1IYN1G2TnECruVbQaL0s1Ps7Dl15sOTFujOqM0MI4jdZxLDaOmSHpV9AvhHFH0lhFyZW9A05-S-Xp-mV3mI3qvUtp_z9tS4uL14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عضو شورای شهر تهران مدعی شد: شنیده‌ام ۴ گزینه در حال تحریر و تدوین برنامه‌ای تحولی برای سازمان صداوسیما هستند.
🔴
تاریخ هفتم مهرماه، مدیریت پرچالشی به پایان می‌رسد که دولت، مجلس، جریان‌های مختلف، حتی بخش جدی سازمان و مردم منتظر پایان آن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138142" target="_blank">📅 15:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138141">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نیویورک‌تایمز: وارث اسرارآمیز ثروت جفری اپستین کیست؟
🔴
کارینا شولیاک، دندانپزشکی که به عنوان آخرین نفر، پیش از خودکشی اپستین با او صحبت کرد
🔴
اپستین اندکی پیش از مرگ، سهم بزرگی از ثروت خود را به این زن واگذار کرد، از جمله اینکه یک انگشتر الماس به وزن ۳۳ قیراط را «به عنوان مقدمه‌ای برای ازدواج»، به او اختصاص داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138141" target="_blank">📅 15:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138140">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LA1iqpyZz15aJ-Yi6AMlv3rdsG2CdUQRLS7I572jjl1uLPvI7iH_doxd9CS6bNDYiJV2aevAJTvTNAnzsveqjAuPXM0zswMHqQ1oK9Zu_5uZxp3ARXqs2KDokGsIPPt4PzD_A55aqVyJVLNm9pGmAimFkPJVCVEr9SMhHXHhIuGvvXKQ2BJjjKuQPhbnPOi0oFw7ywKu6Ccrp1XFLPle_B54WIxPEGUk3NNyg6Bz_jTb2SQECnH0Tx1XOOdGubnRXaHmQlNNVyjWGR_aa7O1aRNBEk77h9eBvIN50fwAgJ5_xvRZCZjA9CPvke06rdPfkSerRqZWH72-QpuF9xtapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در آپدیت جدید اینستاگرام می‌توانید یک نفر را به‌عنوان «یادبود» یا همان وارث انتخاب کنید تا بعد از فوت شما، بعضی کارهای پیج را انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138140" target="_blank">📅 15:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138139">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIKXCKkvx4dbJ6aeqO4IqU7dZoUyjruinq6FyXEH_t8kIqD801r19FjwhRFsGriZ0mj3-2u7jjrXVMNBqghAiZih8zoLvoyuPSBL8JxdnrdFj5qCZwxn_72sqg5MTRyGGIDs5lL9McLS9gzUFCVM5bJPew-JunRuKiaj6tcvskm6FR03Rn-VuyMctc4dmYF62YUw5airCqS4WeF0LiiP19mmyPM003vKjv48LpxsxxE7utPSHert8fhOWqXyCCiaNEeL3C4bNHKCF5sQpL4_7MoWdh4uA2EJYR91uedRc0AbAE9cwYnpckxWdtvPXMZf4kzMJoFfwvfraun2IC0LAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۸۷ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/138139" target="_blank">📅 15:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138138">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزیر ارتباطات: اپراتور های ایرانی در عراق را برای رومینگ تقویت کردیم و اینترنت برای زائران کاملا رایگان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/138138" target="_blank">📅 15:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138137">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سی‌ان‌ان‌ به نقل از مقام کاخ سفید: ترامپ در کاخ سفید با زلنسکی و نتانیاهو به طور جداگانه و پشت سر هم دیدار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138137" target="_blank">📅 14:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138136">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ادار‌های استان کردستان فردا تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138136" target="_blank">📅 14:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138135">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رویترز: آرامکو پالایشگاه جیزان را با ظرفیت ۴۰۰٬۰۰۰ بشکه در روز، پس از حمله انصارالله که به تأسیسات این پالایشگاه از جمله مجتمع گازی‌سازی و مخازن ذخیره‌سازی آسیب رساند، به طور موقت تعطیل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138135" target="_blank">📅 14:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138134">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
قالیباف: تمرکز مجلس و دولت بر امور مهم و فوری باشد
🔴
تأمین معیشت مردم در دستورکار حاکمیت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/138134" target="_blank">📅 14:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138133">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
الجزیره: ایران در قبال وضعیت در تنگه هرمز «انعطاف‌پذیری» نشان داده‌ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138133" target="_blank">📅 14:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138132">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4jucXYy0KE3Oas9f7TPObOoludXzCG9c6U3ccnLjbhyrrgzAs1o8H_lGWOhGD7Hzd4mC-PEt4MxV0wClpGe9pudDy1mi33f4Dpl187pqzHggQ3TQK5nMFOzcCGG9nV-n85S90Ert2TMMQwN6aNhhjMGrkenip466S3rIes6yZjtCR7Dg-ykCnLpibfXLoAMcoG9GqBBUTvOcZNnqbkOE7fpsp9iq7Bgn4QTSESw01fkIfML2OGW6Ghb0WzMh_FaesBR40fAEoJjZHRB6l46eC-wNeuffGBYISjUU_Ls_Sb6fkulfk0fpOkb6EQsL1AvYr6-GH9V2l8hnKRlfwuW5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: سپردن کار به مردم و اعتماد به نسل جوان باید دستور کار روابط‌عمومی‌ها باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138132" target="_blank">📅 14:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138131">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AElMRRdk1oMEIIG6L8HJwz1gt6nDlqMU3Q8MbyLMgfQtkbcCREW4yFsDKBHd3sLyQblLugLWpforGCFpJGoUY_31LgxweA5ymH43j_PXcpYGNGHEmqVWpYaHn2zzSMZ6df7e56SlzB-Ir12eJfXrHmrIwmqW9ZjJW4lsMfYPfd4OVpBGrtjtSCupCA6S-6jW5cZ-4-Ed36D464o9oacnnR0jLe-4Vaxgeb1scNFQEm0-hK1U2IkuD87pnbxG9Gfv_BPb04FqGc_7Xmx6O6EFbMFmssKv4CXwetRLhr81Y0kcwkDnYTpSATrztbFmt5bIAAJd-BwGKR-l0dGZNsD1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال‌های پایش اوکراینی ادعاهایی را منتشر کرده‌اند مبنی بر اینکه ایران ممکن است در روزهای آینده تا سه موشک بالستیک به سمت اوکراین شلیک کند.
🔴
وزیر امور خارجه ایران گفته است که این حمله "نمی‌تواند بدون پاسخ بماند" و نمایندگان مجلس هشدار داده‌اند که کی‌یف "درک خواهد کرد" که ایران چنین اقداماتی را نادیده نمی‌گیرد.
🔴
موشک‌های بالستیک میان‌برد ایران، مانند غدر، امید، سجيل و خرمشهر، از لحاظ فنی می‌توانند از شمال ایران به خاک اوکراین دسترسی پیدا کنند و سامانه‌های پدافندی پاتریوت اوکراین در برابر آنها با مشکل مواجه خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138131" target="_blank">📅 14:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138130">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
تایوان در طول تمرینات نظامی سالانه خود به نام "هان کوانگ" که از تاریخ ۵ تا ۱۴ آگوست برگزار می‌شود، انتقال تولیدات نظامی و تبدیل کارخانه‌های غیرنظامی به کاربری نظامی را آزمایش خواهد کرد. این اقدام در راستای آمادگی برای احتمال حملات احتمالی چین به مراکز دفاعی و لجستیکی انجام می‌شود، طبق گزارش رویترز.
🔴
این تمرینات، سناریویی را شبیه‌سازی می‌کنند که در آن چین از تمرینات نظامی روتین برای پنهان کردن آمادگی برای یک حمله استفاده می‌کند، که این امر باعث می‌شود تایوان به سرعت سطح آمادگی رزمی خود را افزایش دهد.
🔴
این تمرینات همچنین توانایی ارتش را در توزیع تولیدات صنعتی، انتقال کارخانه شماره 202 سازمان تسلیحات در تایپه، بسیج تولیدکنندگان غیرنظامی و حفظ مسیرهای دریایی حیاتی از طریق عملیات مشترک نیروی دریایی و گارد ساحلی، مورد آزمایش قرار خواهد داد.
🔴
سرعت اینترنت سیار نیز کاهش خواهد یافت تا میزان مقاومت در شرایط جنگی و در صورت اختلال در ارتباطات، ارزیابی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138130" target="_blank">📅 14:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138129">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزارت ایمنی کره جنوبی : روز سه‌شنبه نشت فسفر سفید در داخل یک پایگاه هوایی بزرگ نظامی آمریکا در پیونگتائک، استان گیونگی در کره جنوبی رخ داده و برای ساکنان نزدیک آن توصیه تخلیه صادر شده است.
🔴
طبق گزارش سازمان بهداشت جهانی، این ماده بسیار سمی اغلب در سلاح‌ها استفاده می‌شود و می‌تواند در تماس با اکسیژن مشتعل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138129" target="_blank">📅 14:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138128">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
معاون اداره‌کل حفاظت محیط زیست خوزستان: آتش‌سوزی امروز ۶ مرداد در نیزارها و پوشش گیاهی خشک حاشیه کانال زهکش المهدی رخ داده و خارج از محدوده تالاب هورالعظیم است.
🔴
تاکنون هیچ آتش‌سوزی در محدوده تالاب هورالعظیم گزارش یا مشاهده نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/138128" target="_blank">📅 14:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138127">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
حماس: هیئت مذاکره‌ کننده ما عازم قاهره شد
🔴
انتقال به مرحله دوم طرح «ترامپ» از محورهای مذاکرات در مصر است
🔴
هر گونه توافق جدید باید محدودیت‌ها از زندگی روزمره فلسطینیان را کاملاً رفع کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138127" target="_blank">📅 14:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138126">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
معاون توسعه مدیریت و منابع استانداری مرکزی: ساعت کاری تمامی دستگاه‌های اجرایی استان مرکزی در روز چهارشنبه هفتم مرداد از ساعت ۷ تا ۱۱ صبح تعیین شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138126" target="_blank">📅 14:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138125">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:
نتانیاهو به دستاوردی رسید که چِرچیل نتوانست.
🔴
او ترامپ را با ما متحد کرد تا علیه ایران اقدام کنیم، به طوری که آمریکا را متقاعد کرد قبل از وقوع یک حادثه مشابه پرل هاربر، وارد عمل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/138125" target="_blank">📅 13:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138124">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mS_lsi9jEZidHAEKgGQ3Y8_58xV1uRyqby9bQ0DNhGI_LowQno0lQxnqS4Yt3R46eQFwrBXmT40iREykOXGF_op7QBpFEz0ZSlcbFyZx0pX-kUbTcdBp0_Dj4RklXYMixCPi26mT06dHxJ7oxwlLzR25x46qp06jRLwGII6usW_m2Rx7FSP4E9G9FZk5sjLl3UgNs6fkODI-lCr5twlfmpWkutAoaW_ZyrkJNOe7NeimXlvej0Zfr9d3-kA3yCXexwpv-emRF9rM0WTYBXkbjczCwZ-ALimxisi5RbS-gQwiOy7QbS0XZwMgPIyJaGlgwurQgLhFaMkCMdzq1Gor_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام آمریکایی : تصمیم به عدم تشدید تنش پس از جلسه کاخ سفید در روز جمعه گرفته شد. دو منبع اعلام کردند ژنرال دن کین (رئیس ستاد مشترک ارتش) و جی‌دی ونس (معاون رئیس‌جمهور) نگرانی خود را از تشدید جنگ ابراز کردند.
🔴
کین به ترامپ هشدار داد که اگرچه ارتش قادر به اجرای گزینه‌هاست، اما پیامدهای منفی از جمله کاهش ذخایر مهمات وجود دارد.
🔴
کمبود مهمات یکی از عوامل کلیدی در تصمیم‌گیری ترامپ و تیم امنیت ملی بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138124" target="_blank">📅 13:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138123">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f005de3ae2.mp4?token=L1M-FQyBkLU8NPoomED_DJo8UQt3ZIqyYLzmPm1f37Zc_L4ncA3w5x9a6bsRymH_t3ZST_f1gvaumsUZoWcJ8-hwlqZFwX3exjWyp3rRy6XVQe4vsOg6Kk5_IxkIDIR2jO82LVobadZHLzB1kosZKW9yOLCXnF67KINjSnNN9FnZQEEPbNFHkPHm19dizWahW6bB5srEhGBzISqAuHdj2NvDNJ6_f_EMuA-g-VJahRV_wwtIXn5wz9YBTjiBn55Z2ilwY1ICJ9zg8MszkBT3_bnXbqzGFSp4MRRd9rz0m2VlhtKM912oYHCQLXwJ0LKvmmbWb8VKLr3for81S6Mbig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f005de3ae2.mp4?token=L1M-FQyBkLU8NPoomED_DJo8UQt3ZIqyYLzmPm1f37Zc_L4ncA3w5x9a6bsRymH_t3ZST_f1gvaumsUZoWcJ8-hwlqZFwX3exjWyp3rRy6XVQe4vsOg6Kk5_IxkIDIR2jO82LVobadZHLzB1kosZKW9yOLCXnF67KINjSnNN9FnZQEEPbNFHkPHm19dizWahW6bB5srEhGBzISqAuHdj2NvDNJ6_f_EMuA-g-VJahRV_wwtIXn5wz9YBTjiBn55Z2ilwY1ICJ9zg8MszkBT3_bnXbqzGFSp4MRRd9rz0m2VlhtKM912oYHCQLXwJ0LKvmmbWb8VKLr3for81S6Mbig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش ها از وقوع انفجار های مهیب در مسکو پس از حملات پهپادی صبح امروز اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138123" target="_blank">📅 13:44 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
