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
<img src="https://cdn4.telesco.pe/file/lHjXCm15g_ZmsLKrDgTkaWYaGBNyXs7AkZgnlAReowFgaE8j5-_foP-Zb5nOI2M8kn4_jQT1y_AkoFHK9SSf2l64Sa7T3oa-4V6GjjKJjJ4VcWzteSxTYNwIPvHpJC7iDtf2d951up25tbnbxihuU4uMRS1w-Uhpx4GplZyCUnWuCqUeJ7tFHr21JtF4xh-hhkK6eTWSnJHhXrAJjO-L--4x_13_fsKz2-jRtqZfS6fQ_1DmF9fDEupHC229Ox7Qa3ZX_Z42Xvy_emzrjg-Ihgf3UbbJI9bDy-AmeqL0akYb9dV9hM3-CzNYlBhbSXqO5zTFlrIcNhMJt2NbZL5Rjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 225K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 11:49:06</div>
<hr>

<div class="tg-post" id="msg-65986">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a45e16c46.mp4?token=JvZuBpucNs58jEtSg0oUCKZEhmiqrvdgWmn_i2X1FE2E_Q75mjLFB3KA6pbEjw9wsq32LrdGutMTipqpubXu_LYRHSFzPL3TmtFqsMk6PgumACGlGnUH7jl4fGl-x9kGlxKbVjuknbgCkjEOyYrwQUU6w3e7Y2kFWMn0zL_h0vCwIFxoQDtnHtndmgRu-Wi8qmrLUYKrW5RbF1uVglxjXuismYXNOTsrKIKXR3MGv5o-LiDTZ77Kc1bACuKGaTaL8hLdCayv2SnwX2V08srWZDIua3-zpsYS7DBgX5_YLUm3mLvkHynetY7h83u5qoRSNQmlAlqvuj2P--acoC0oEiNWEvWv1mcG1aaghHZCJWSO_PUgDWacZOxr3bfQO2JacMymgePufhulFdo7yZ4qFhtJ-ZBfwx0qzmNl3Ghb3IIKKK5wED9Ayk3x4Vj3jZQBiQfDX8UfrB7ZghDb8rqOE3dpEjcpaxVT0DTeuIwZrJ1Iami6jy5D64nN3e5xO08b995VHYVADddUwCmhp2xpS8AOGdIcykn6fr9sd34RcjOZWRj5R0u0-0Dg9jmFVB65ArXSj5Oi4G6yn-pgrVhLikWnFr0-BF7chw4nnNcGKn_w-S706hUnBq_rJ6WjhOewoDR3qBoLDIvhxk5lM800QZV2lk6aIeuzgKVjWO_IgUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a45e16c46.mp4?token=JvZuBpucNs58jEtSg0oUCKZEhmiqrvdgWmn_i2X1FE2E_Q75mjLFB3KA6pbEjw9wsq32LrdGutMTipqpubXu_LYRHSFzPL3TmtFqsMk6PgumACGlGnUH7jl4fGl-x9kGlxKbVjuknbgCkjEOyYrwQUU6w3e7Y2kFWMn0zL_h0vCwIFxoQDtnHtndmgRu-Wi8qmrLUYKrW5RbF1uVglxjXuismYXNOTsrKIKXR3MGv5o-LiDTZ77Kc1bACuKGaTaL8hLdCayv2SnwX2V08srWZDIua3-zpsYS7DBgX5_YLUm3mLvkHynetY7h83u5qoRSNQmlAlqvuj2P--acoC0oEiNWEvWv1mcG1aaghHZCJWSO_PUgDWacZOxr3bfQO2JacMymgePufhulFdo7yZ4qFhtJ-ZBfwx0qzmNl3Ghb3IIKKK5wED9Ayk3x4Vj3jZQBiQfDX8UfrB7ZghDb8rqOE3dpEjcpaxVT0DTeuIwZrJ1Iami6jy5D64nN3e5xO08b995VHYVADddUwCmhp2xpS8AOGdIcykn6fr9sd34RcjOZWRj5R0u0-0Dg9jmFVB65ArXSj5Oi4G6yn-pgrVhLikWnFr0-BF7chw4nnNcGKn_w-S706hUnBq_rJ6WjhOewoDR3qBoLDIvhxk5lM800QZV2lk6aIeuzgKVjWO_IgUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
خبرگزاری فرانسه:
روز جمعه، از کشف یک جسد در صندوق‌عقب خودرویی در مجاورت محل تمرینات تیم ملی فوتبال ایران در جریان مسابقات جام جهانی ۲۰۲۶ خبر داد. بر اساس این گزارش، بازرسان و کارشناسان پزشکی قانونی مکزیک در حال بررسی جسدی هستند که در یک خودروی متوقف‌شده در پارکینگ بیرونی استادیوم «کالینته» در شهر تیخوانا پیدا شده است؛ استادیومی که به عنوان اردوی تمرینی تیم ملی فوتبال ایران در این دوره از رقابت‌ها استفاده می‌شود. این حادثه تکان‌دهنده تنها یک روز پس از افتتاحیه و آغاز رسمی مسابقات جام جهانی ۲۰۲۶ رخ داده و پلیس محلی هنوز جزئیات بیشتری درباره هویت مقتول یا انگیزه احتمالی این جنایت منتشر نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/news_hut/65986" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65985">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ac66f6c0.mp4?token=IIV2IFU4s_o_OLy4ZMPOZwBZM9DKuL0L6N0AZRQivwE7guQN75K6eQCDmQ9kar0oUeZYl5VslWCUGfU3K1JY4VIUt_CAwMToCtMRiX2GocrR9WvN8xnLYov2pS6PVH2GMlEajHh9_Jfn4eFIurJxjYlp43HwnWI_4_PAOSkruoHytxKT4O3QKF0QY3z2tJarxmTSzaQKboUAx_GYXdfFtgoR8c0KNJ8CnNrCoWWV2LqvldmROxuZt72MVUA4C5Gejm8t0Y-f5gLELnEK0Pwiaw8c_gKRVn0auv0nUAcJ4iCdASTCkLq1FULQEiGrlzeszbNCypEqcoTQe8lvcIi_9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ac66f6c0.mp4?token=IIV2IFU4s_o_OLy4ZMPOZwBZM9DKuL0L6N0AZRQivwE7guQN75K6eQCDmQ9kar0oUeZYl5VslWCUGfU3K1JY4VIUt_CAwMToCtMRiX2GocrR9WvN8xnLYov2pS6PVH2GMlEajHh9_Jfn4eFIurJxjYlp43HwnWI_4_PAOSkruoHytxKT4O3QKF0QY3z2tJarxmTSzaQKboUAx_GYXdfFtgoR8c0KNJ8CnNrCoWWV2LqvldmROxuZt72MVUA4C5Gejm8t0Y-f5gLELnEK0Pwiaw8c_gKRVn0auv0nUAcJ4iCdASTCkLq1FULQEiGrlzeszbNCypEqcoTQe8lvcIi_9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند تا پسر اهوازی وسط جنگ وقتی رفیقشون خواب بود این شاهکار رو خلق کردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/news_hut/65985" target="_blank">📅 11:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65984">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11109e09bd.mp4?token=nK8CCkhzTaFQpk_kDGLHwHUEIWrsvIFunDMI_bIe-yZi_rG8exVGoqCSzgH-GsrQqz7b-H8eSidXwIiUjzxSGkd1cNLyJHUSn7BsiFngTrSkDFPOBcLFWcUU9-gEy8_89Z72zyz8DLKF1HlML671dfkqxiJ19jMXMsVVnxQ_dE9GGa9aKKs7kxmxKl4uUO26lBPahtcbRgTNNqbyoofTLfDK30VA_YZMdbfh3gvdx1VBqZ-1c2Gx7M2MlpBDKlaXOZCCo4pbiHgDGUbnKgrpyiFMmRTbafbL8Z5fguPs9va3nETApcXKVSlwCG5AEZVOdFChGNENlsdfHZ8DuqmGNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11109e09bd.mp4?token=nK8CCkhzTaFQpk_kDGLHwHUEIWrsvIFunDMI_bIe-yZi_rG8exVGoqCSzgH-GsrQqz7b-H8eSidXwIiUjzxSGkd1cNLyJHUSn7BsiFngTrSkDFPOBcLFWcUU9-gEy8_89Z72zyz8DLKF1HlML671dfkqxiJ19jMXMsVVnxQ_dE9GGa9aKKs7kxmxKl4uUO26lBPahtcbRgTNNqbyoofTLfDK30VA_YZMdbfh3gvdx1VBqZ-1c2Gx7M2MlpBDKlaXOZCCo4pbiHgDGUbnKgrpyiFMmRTbafbL8Z5fguPs9va3nETApcXKVSlwCG5AEZVOdFChGNENlsdfHZ8DuqmGNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ربات گدا در چین دیده شد
یک ربات انسان‌نما که از چندین روز بدون شارژ ماندن شکایت می‌کرد تا همدردی رهگذران را جلب کند، در شبکه‌های اجتماعی چین مشهور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/news_hut/65984" target="_blank">📅 10:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65983">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77f6aacbc.mp4?token=KjKHT19-RG27dFmTKr7ByYIyW-mtBSjX_W-y_2mzfLDOLoQ7AahKmtUG_FfMPugFCeeu1gw6lIcgo_jVDj9hTFMzBbv29rQkrtJmugwPTOMwzERrG3fqIplDI4YwIN6WjJi-kkEC6eagPUn9m3leeyyBy637pA0q41YXCGsEneeBKjeL-rByxxL4ym9p4S_wjro23MmCVXRr8tAM2C7tAWcL3FNbQL48deMeCsNXOK6zH-kTSoCdynulbe77TwDWWYgFHljJnSAY4cdbYseAwOSAYf44cqpMvU3CalobbJ-w3ZlvZsZOvQSo9b7D4JZlynD-E0-TCD56z9R6nxE4TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77f6aacbc.mp4?token=KjKHT19-RG27dFmTKr7ByYIyW-mtBSjX_W-y_2mzfLDOLoQ7AahKmtUG_FfMPugFCeeu1gw6lIcgo_jVDj9hTFMzBbv29rQkrtJmugwPTOMwzERrG3fqIplDI4YwIN6WjJi-kkEC6eagPUn9m3leeyyBy637pA0q41YXCGsEneeBKjeL-rByxxL4ym9p4S_wjro23MmCVXRr8tAM2C7tAWcL3FNbQL48deMeCsNXOK6zH-kTSoCdynulbe77TwDWWYgFHljJnSAY4cdbYseAwOSAYf44cqpMvU3CalobbJ-w3ZlvZsZOvQSo9b7D4JZlynD-E0-TCD56z9R6nxE4TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد دیدن این ویدیو از مسعود فهمید جز توافق راهی نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/65983" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65982">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKdP5IkNGCern6J5ZWxtzacNYJs2ERoK5KXSYWu4VvEW9Mv5P1shdtD0OPImfQ-yIrBcL8pemp-TaZl4qtxvhIaIVURX0QaHgc0KizdOBwbzLP4hLHKc0CW2-A6K-Xh7ku0zIASDVgLdFeib1UF54Imyf0xaf9Kc7uUyh_rRVaKWbO0t2YKZ2lb-k6xoHP2FlxmCPRVDJIeSOqpKGbf-8KrHd_aKe6ve_8SU4XcYwu7jyBvCcBRqFoeryp88LcbDjejTurdKV1tEC0bffQ7JBYBig6MP6KxhHDX4_myCNq1U9sjYNHwTHHuFrtqdB1d9QYISdprMwn-Vs7xXf28unA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام:
ایران چندین پهپاد تهاجمی یک‌طرفه را در تلاش برای حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز به پرواز درآورد. نیروهای آمریکایی در ساعات اخیر همه آنها را سرنگون کرده‌اند، در حالی که جریان ترافیک از طریق تنگه بدون مانع ادامه دارد. این کریدور تجاری بین‌المللی همچنان برای ترانزیت باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/65982" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65981">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65981" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/news_hut/65981" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65980">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=iebmhxfhh9Gm3yjmvLHjjBNwKFv2u4ugCJxdqj9EC-5L_P0TNpTaTRp4Hoz_-NYW9bsb4MkqSqvp3T0TO1zDY7aSt6Xw5jnEUwIp3Z22fgW6pZy2iDXOQZfep0GM2G-AHnbJgA69y0sq2G7-We20KrB9Jnbp1I9fhOJm5RqBtdwgs5riVSP1ShT9IcmCASGOba0294cuVP58gihmm9j1TW0zr3U2oTHL1rFqluxeJAAtbav4khFmg_rgnLZviHPYqR3Yr11C94GSJ0tP7h7K074vEVoDGpo6rImD2NKetzLPj-xwXV1uBKA1kOlH88CApSRGCeR0W-gLc2gStrOQu5O-GzaB7AVMOU8STWuEqjjUTU2G5gG5SQpquFpzjPi3HFFO5Zbqx42v7mcq8ZIM-xjm5h0M4nJ6SYZu1t-HkLjZU3tHXJ1tBcR8-UaTtQdaykuDJzumVhqGCa8wHuUIRMIAFU14z89oLlK7zLLzNyQZIRxL7StxbSCZiQ44_VOwVjPJkuCJBhxaECkgL7QFDgg_JwhpXqPETGqGFtNVXQvjTWjQDdA6WPbX3L_8ovVEMzePvGav7R4LICNdKes6zMe7iEf2hp5g7cNSpRC_Bltodc2UqTHHHn8RiGSFGSBYL1EiRfjToIFNvtdwLg1rEa0K9wd68ldkeXJotR6rU9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=iebmhxfhh9Gm3yjmvLHjjBNwKFv2u4ugCJxdqj9EC-5L_P0TNpTaTRp4Hoz_-NYW9bsb4MkqSqvp3T0TO1zDY7aSt6Xw5jnEUwIp3Z22fgW6pZy2iDXOQZfep0GM2G-AHnbJgA69y0sq2G7-We20KrB9Jnbp1I9fhOJm5RqBtdwgs5riVSP1ShT9IcmCASGOba0294cuVP58gihmm9j1TW0zr3U2oTHL1rFqluxeJAAtbav4khFmg_rgnLZviHPYqR3Yr11C94GSJ0tP7h7K074vEVoDGpo6rImD2NKetzLPj-xwXV1uBKA1kOlH88CApSRGCeR0W-gLc2gStrOQu5O-GzaB7AVMOU8STWuEqjjUTU2G5gG5SQpquFpzjPi3HFFO5Zbqx42v7mcq8ZIM-xjm5h0M4nJ6SYZu1t-HkLjZU3tHXJ1tBcR8-UaTtQdaykuDJzumVhqGCa8wHuUIRMIAFU14z89oLlK7zLLzNyQZIRxL7StxbSCZiQ44_VOwVjPJkuCJBhxaECkgL7QFDgg_JwhpXqPETGqGFtNVXQvjTWjQDdA6WPbX3L_8ovVEMzePvGav7R4LICNdKes6zMe7iEf2hp5g7cNSpRC_Bltodc2UqTHHHn8RiGSFGSBYL1EiRfjToIFNvtdwLg1rEa0K9wd68ldkeXJotR6rU9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/news_hut/65980" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65979">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEKuz6c-w2VYiBC_W9cV9SXWimKsVg7Rb0iouA-6UnU77OaAZaLASI2dGex73HM9mhrtEq2YnngBq4jDgPtN7Pn-ht1xAWd1hsBfQzhszOl7NBzm_yZf_dY5tSjsxD8FRQlYYb3RzS3mXGT3hzhTvl5xviF6ASbhSoRBJu-RgG52Qzs__vyIa3FF-3-IfLZa1-0R9dBZaLFoqRdw8OwBSfCCadtoasStiyrzbT-al9X0V4jlYXBhnL9PKKJPCBsNMz-fINHd3BMUH8IiGC9GDxU4A_Qz2t3_I7nhOhYAisnb812YzoasZzPOKp2GoRzCblHpveFe_3ohSSe_14CpDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روح الله خمینی:
اگر آمریکا و اسرائیل «لا اله الا الله»بگویند ما قبول نداریم چون که آنها میخواهند سر ما کلاه بگذارند
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/65979" target="_blank">📅 09:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65978">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92693abb1.mp4?token=IiUaZgHqoZ1V8kYlyajdk5cDr6yxzomW7q5k91Z1hCx_nbKOqNkjT8cE7IE8PXSL3xb3tPe29RNQ61ZvsLtUltPqFCK7S_D1WsaOivTVL2SOAWRdAxx86Iwp3NYtfkkKZ9MkKraRERB5WrIioiZm4cTDcbzy5Ftw40QNn7e-cjT_lcjIwxL7_Mo3SJm3_KEEKKPoAv_nx6IQ55FeAGkCFAcKlTLWOezO_GxWCRfQvKvN2Js_3rml-ib9ueqKdXtaYJyzk2azynYnI3K7jQK998EijKJAslTWMWz1leiCZivYqLv81hPnDfgJFCLm28H1kl5IyUsQJUh7GRNyYqMC4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92693abb1.mp4?token=IiUaZgHqoZ1V8kYlyajdk5cDr6yxzomW7q5k91Z1hCx_nbKOqNkjT8cE7IE8PXSL3xb3tPe29RNQ61ZvsLtUltPqFCK7S_D1WsaOivTVL2SOAWRdAxx86Iwp3NYtfkkKZ9MkKraRERB5WrIioiZm4cTDcbzy5Ftw40QNn7e-cjT_lcjIwxL7_Mo3SJm3_KEEKKPoAv_nx6IQ55FeAGkCFAcKlTLWOezO_GxWCRfQvKvN2Js_3rml-ib9ueqKdXtaYJyzk2azynYnI3K7jQK998EijKJAslTWMWz1leiCZivYqLv81hPnDfgJFCLm28H1kl5IyUsQJUh7GRNyYqMC4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی خامنه ایش رو میکشن، مقاماتشو میکشن وتحقیرش میکنن بعد میزنن تو سرش میگن بیا بشین سر میز امضا کن.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/65978" target="_blank">📅 09:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65977">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65977" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65977" target="_blank">📅 01:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65976">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v40moqvDum03zP1sf_FbmkGfu5JVDQ9ccbXCthljkUPkD10MyY7ejKA9Dgkazxh8Th0_hHrgaHk-PGR4iq5GtwAJlbA24Ih3AZokPbGa_H1dkcCBM_HiRgDYrSCM37ioAZKannMGaDebb30jZ8Hng8hx2p9bUaBFyt9CaKPQbwvAuWBVkH0r6ecewES99vz93XVf6fTHg3_Be1vnNRHTD4nB3vP9vAYXE8gDNc7FGtsKfcjQUCTfvgoqnX0tXSJr3BcmJNvQEl7f8XdkSqPy0H5eB4NQTw4aA3CzwgUu1IQLkJdWEmkB62FKXpCMnYAzLSR4wwpiTzSrcQixXK-35Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65976" target="_blank">📅 01:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65975">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0jP8KhJBZRBxIWgiJCitIPGFLP1A9AO8jynkDDCSVgV8j6QEfrybIKGBqn1MBCRLyrKS8_WqulIOKYADns8JVNTcS4TP56dBz0MgEMYnVQdo6fWrPpqdwJ9oCLmryC-rNaaAYk4qS579jr6LDGo3YecILyhoWeytbj2FvLavakmXv4ESif9FVP2RUqMV5KvwIYSRbpD2o4ATfuxGEMS7KNHI3HHinu8423YBwMbd7CeAt9OkgMFpTb8apXKn1arYacMYYcBMLsCeyla6a4LvFmJ8vFlrHJywmygeI6hOMAJ6OmQbzW4-rf7Zy84HCtclyDSNtWEZK6fJnobXyTDvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تندروها گرفتن رو قالیباف
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65975" target="_blank">📅 01:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65974">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
سپاه:
کشتی هایی سعی کردند بدون مجوز از تنگه هرمز عبور کنند و مورد هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65974" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65973">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/penif8J2yA6SXYhV4CY5yipu0kA7lOuwbi9NjBgJrKojASl_myC7K3q1GVVsK8yOHJQ8VQVIo6ChSDx6c696ouyI33heVB4LXJe07nKf-qdNN3W7Cr2c8f90ZRFjvnOi_KkqNz13rFq3T5F4hYhaX6__IE6A2AGcl9LaOFUb8y-YdxBwp4T2wvtvQZCGVIt9x6lcmpE3JBaEpsZ91EzxgelwyzDE4MBcwyiUoL9gD5mqCUxBkiDbIVh_7ahQZ2Lp2pMFyL0AcW8a4HDyc8Pk3SB2bk8XjtJzMJOIMNg1v43FU3J8PUOysZ7ve41G5mofcFPgyQ0vn4luNfj8lSyjOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل
🇧🇷
-
🇲🇦
مراکش
🏆
جام جهانی ۲۰۲۶ - گروه C
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه متلایف
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
- برزیل پرافتخارترین تیم جام جهانی با
۵
قهرمانی است و در همه ادوار جام حضور داشته است.
- برزیل در جام جهانی ۲۰۲۲ از گروه خود صعود کرد و در مرحله
یک‌چهارم‌نهایی
در مقابل کرواسی شکست خورد.
- مراکش در شش دوره جام جهانی حضور داشته و بهترین عملکرد این تیم کسب مقام
چهارمی
در ۲۰۲۲ می‌باشد.
- مراکش در جام جهانی ۲۰۲۲ با حذف اسپانیا و پرتغال به
نیمه‌نهایی
رسید و یک شگفتی بزرگ خلق کرد.
🧠
اگر دنبال جبرانید، یعنی از مسیر تحلیل خارج شده‌اید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65973" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65972">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65972" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65971">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65971" target="_blank">📅 00:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65970">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=o4FQ1pMI9-jYmkkBniyqYi7oBdy3CTom-Dzv5OKi6YF_07CR2U8KczPiN7uGSuLJIvbzorZmbxbPrbnF058DiH0f0V5sL_gZZQOXVivvJ-A_0SsYjruGKBvwHfsWNbdbmbnGbkYor7j4HUkWl5VCjI2wv_RE_Et1IGzCZL1fVxRZ1_nIYeniXN7CR1HlKr72N2iEuPbLtg_m8odNHs4hSs0XrH2xCx9JMDzn2GTaL02a4y7rMu-SutG17DsU9LxH0txJLUafhsuRhIpaSZ4SBY4ch17Ltf4FVXrLChBiAYhMTkpadR2UadSFhWLBudoP7oz0aEhO_yhWsZqnVYmYJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=o4FQ1pMI9-jYmkkBniyqYi7oBdy3CTom-Dzv5OKi6YF_07CR2U8KczPiN7uGSuLJIvbzorZmbxbPrbnF058DiH0f0V5sL_gZZQOXVivvJ-A_0SsYjruGKBvwHfsWNbdbmbnGbkYor7j4HUkWl5VCjI2wv_RE_Et1IGzCZL1fVxRZ1_nIYeniXN7CR1HlKr72N2iEuPbLtg_m8odNHs4hSs0XrH2xCx9JMDzn2GTaL02a4y7rMu-SutG17DsU9LxH0txJLUafhsuRhIpaSZ4SBY4ch17Ltf4FVXrLChBiAYhMTkpadR2UadSFhWLBudoP7oz0aEhO_yhWsZqnVYmYJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صدا سیما: هک تصویر انفجار اتمی در تلویزیون، سیگنال آمریکا بود
!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65970" target="_blank">📅 00:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65969">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060800d75a.mp4?token=MPwswvn0dhBAkEIELp3SRecbcsXPd-uUHI5yGKCjzrYYhpYdONyikpB8paa-clDz3iYfM0pEzazrb-BDcXEzmD8k919lc2MYX4ZJk-1Dv0V3wuWm4pj4vnvxxpWaWiqGBj2I2g9H9cnCqXxrUGJM-VFFb3kq2nrkOftg1jaFYOGUAh7T7OoEz0abUfPmLn6tFbfFjXyI7KrLI9qorAueeGV95TFaDzzEUUJMjIaHxsKJZ2R1YmFT0XKqMgGyiRajm62RuDnfV5b0FGRH7NXynrfPNGwtvQPA5eFauDs9BY9pNm1Ev6N-JWif4ZU_i39jVq4OmgGRiDHHuD9UeUMu9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060800d75a.mp4?token=MPwswvn0dhBAkEIELp3SRecbcsXPd-uUHI5yGKCjzrYYhpYdONyikpB8paa-clDz3iYfM0pEzazrb-BDcXEzmD8k919lc2MYX4ZJk-1Dv0V3wuWm4pj4vnvxxpWaWiqGBj2I2g9H9cnCqXxrUGJM-VFFb3kq2nrkOftg1jaFYOGUAh7T7OoEz0abUfPmLn6tFbfFjXyI7KrLI9qorAueeGV95TFaDzzEUUJMjIaHxsKJZ2R1YmFT0XKqMgGyiRajm62RuDnfV5b0FGRH7NXynrfPNGwtvQPA5eFauDs9BY9pNm1Ev6N-JWif4ZU_i39jVq4OmgGRiDHHuD9UeUMu9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
گفتگوی عراقچی هم اکنون شروع شد.  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65969" target="_blank">📅 23:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65968">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
عراقچی:
محاصره دریایی آمریکا اولین چیزی است که در این توافق به آن اشاره و تاکید شده است که باید رفع شود
دارایی‌های مسدود شده طبق یادداشت تفاهم اگر امضا شود، آزاد خواهد شد
هیچ‌یک از دارایی‌های ما نمی‌تواند مجددا مسدود بماند
برای جبران خسارت ایران طرح بازسازی در نظر گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65968" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65967">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
عراقچی:
به زودی ایران و عمان بیانیه ای مشترک در رابطه با تنگه هرمز منتشر خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65967" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65966">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
عراقچی:
به طور قطع تنگه هرمز به شرایط قبل از جنگ باز نخواهد گشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65966" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65965">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
عراقچی:
پایان جنگ در توافق همچنین به معنای خروج اسرائیل از مناطق اشغالی در جنوب لبنان است و ما این موضوع را صراحتاً به طرف مقابل اعلام کرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65965" target="_blank">📅 23:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65964">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGZdKDaT-ltefppuFbtEyqR6a5d-ynRu5qZO8vDQ3v_MrG1inqkpIfiQ_tKYDVbuQ8ZMmPqldDdilNOpfdKaCbI_s810fogvdyvl218ExSU45L6mZDsvDsQ-BV3u2q00FslK4nbxsc7akf3DNhdOR4z5h9qCxqIg_SIedxJ3PeWqHZC4IHBs_QObpTzSSNKCDJRl4qti1gg6BPdZMWDtx1JUpZ0QyyIXSGxEhYJvoXbNswiIvIarZOJCYN-eTvON_O9NP6A7-I6S6n9v0d2Z96sercP1Rf7IxBJs8hCzPFfkUNwDRSoQYRmbIsd972hmrRbGaJ5duPlwjWm1r-rFsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
تعهداتی که داده شده باید حفظ شود. نه اگر و نه اما و نه بهانه‌ای. برای معامله نزدیک پیش رو، راه دیگری وجود ندارد.
هر چه بکاری، همان را درو می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65964" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65963">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
نتیجهٔ تفاهم یک یادداشت ۱۴ ماده‌ای است و وقتی نهایی شد تک‌تک آن را به مردم می‌گوییم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65963" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65962">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
عراقچی:
ما پیروز میدان هستیم؛ مقامات خارجی به من می‌گویند که ایران را این‌گونه نشناخته بودند و ایرانی‌ها شگفتی آفریدند و با قدرت بیشتری از جنگ بیرون آمدند
من می‌توانم اسم ببرم که کدام مقامات این حرف‌ها را زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65962" target="_blank">📅 22:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65961">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
هیچ دوگانگی بین میدان و دیپلماسی وجود ندارد و هردو در یک‌راستا حرکت می‌کنند
به این ۲ رکن، رسانه و خیابان‌ هم این‌بار اضافه شد و ۴ رکن باهم در یک‌سو حرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65961" target="_blank">📅 22:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65960">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
همهٔ ما مدیون تک‌تک نیروهای مسلح هستیم.
همین‌طور ما مدیون مردمی هستیم که ما را تنها نگذاشتند و هرشب در خیابان‌ها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65960" target="_blank">📅 22:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65959">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
عراقچی:
دشمن تصور می‌کرد که بعد از جنگ ۱۲ روزه، در جنگ ۴۰ روزه می‌تواند ایران را تسلیم کند اما با مقاومت جانانهٔ مردم و نیروهای مسلح ایران مواجه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65959" target="_blank">📅 22:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65958">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
#فوری: طبق اعلام زیرنویس شبکه خبر ، عراقچی تا دقایقی دیگر مهمان این شبکه خواهد بود  @News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65958" target="_blank">📅 22:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65957">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
خبرگزاری تسنیم وابسته به سپاه؛
حزب‌الله: لبنان نیز شامل آتش بس میان ایران و آمریکا است
«حسین الحاج حسن» نماینده فراکسیون حزب‌الله:
بر اساس آنچه از سوی مقامات ایرانی به روشنی به ما ابلاغ شده، لبنان نیز شامل آتش بس است.
بر اساس آنچه مقامات ایرانی به ما ابلاغ کرده اند، اسرائیل از خاک لبنان بر اساس این توافق عقب نشینی خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65957" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65956">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 450 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری عالی
✅
مناسب برای گیم و استفاده روزمره
✅
تحویل فوری
✅
تست رایگان قبل از خرید
❗️
پشتیبانی 24 ساعته
📣
کانال رضایت مشتری @kavianivpn  جهت خرید اشتراک پیام بدید
⬇️
…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65956" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65955">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOMbxg6-WPlb02pBvEVU9j_ZSnhcd12LQnAQnO0xVaa5D1jAbZYtLY2yjPKKnCKFg0x92slxCfu71BsT4L-Wh72P7mXVykXd85KDhVYJDLPKmCou0XK_02tsiiEP2pxpUm6wSSh2Ow0VlKRqlfrEN8oEX-1K6ih6I1HCHZYnkJLVcn3UoFmrK8vI9PFkNzXistgNrLdIa6c-tDQiNjJbcoWb36wJGUruM9Ryp5ZwlRrGdyDXK5Mo8zUtElhZd7dQv_CfBnNZhEgKOw4aa4xq1vYQBhc8FIeu1gdhA8I5lCZI5ahyN9ao4Vj6ag7uXGXChCmfw4lOUT9lQkMKGNQ3Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 450 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری عالی
✅
مناسب برای گیم و استفاده روزمره
✅
تحویل فوری
✅
تست رایگان قبل از خرید
❗️
پشتیبانی 24 ساعته
📣
کانال رضایت مشتری
@kavianivpn
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65955" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65954">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
کانال 12 اسرائیل :
توافق قطعی است و این به نتانیاهو اعلام شده.
ترامپ از ایران خواسته به صورت علنی درباره توافق شفاف سازی کنه و هشدار داده انجام ندادن این کار پیامد هایی رو به همراه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65954" target="_blank">📅 22:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65953">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
رویترز: امارات ۳ میلیارد دلار از دارایی های ایران را آزاد و به آنها تحویل داده، این اقدام تضمینی بوده در ازای اینکه دیگر به این کشور حمله نشود
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65953" target="_blank">📅 22:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65952">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bM8KeDXO-oWVrbP9t3hYhBatW_UN_PWH3Ey5pa_4kigNTEsCXiXXqVj2ohoPtEbe37FsSA17NPoIbdd2Ws7IYjZfAmgE0K7Rhh15O6kpR9_1mdsvxOSzzcWyBJ0bfhBvs86k_tLct2I0BeOaU7vDwl1lK6_0OVHFYTxP7lpKVoio-2E4LUJ1xTsn-lt1v1Rb7aJCSHah-drrV6bTkmuDLuF57HceFP46LzM8XYtgTXKhbfhp-tQKpoQRwbhYc1JSn-lObFVHVb4AAafj1D9ioLgwtMZDPySfjtFqTeHcw8l1OZzwhZj1ZglWAqXO8oCEhserwerA3SkmLTX9gmcyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#
فوری
: طبق اعلام زیرنویس شبکه خبر ، عراقچی تا دقایقی دیگر مهمان این شبکه خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65952" target="_blank">📅 22:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65951">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzJPov0phEMR8GWO9-KpaPKtf16meUYc4r4WZcs55yM0CU3elv3LDTuSwpUfVQD1JrjHI9jAuSFOgrss9PapLLh7jFiFvngYxzOWag3mbwQjE8xbiar9GJRo6gqu-oujRcXKV_seB8g5hj9fNkWvksDRvlX0AF4SxJSM7MeLIG34WIIl7ZusvJy9yrcagaSB3DNAWNcqMhdfJ3VQgNCd8-ikuEQ8HLKSnWbZ4oZeXZjSQKrSZ7e5G8IwDJKTuWDizDViinGLjmTHk1LfCJzUexPBn7i_uhD7B9mpYv3weKFNyfQjtsdpr6OFXj8WnrsEVPCEsB7CoOfcdgDhGrE83Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا به شیرمردان سپاه اسلام و حضرت آیت‌الله العظمی سید شیرمردان حاج آقا مجتبی حسینی خامنه‌ای، خوب دارین کیر می‌کنید ترامپ زن کصه‌رو #hjAly‌</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65951" target="_blank">📅 21:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65950">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHlwQxF_Vqsl0YtcxnHNAFcKxJqJFawv5PT_fnMEMp3LkL8wCzMboNBay97cb-6yBWMdyUbgEpiu5MkS9Nee3c5iqQkmcWiMYCbBIMqrS3BNn57rG_R7rxDXeJiPoJjA4VZy2RYw10kTg6OoB29Rd-BsUq_k8V7OsIB0k8cnAyHqsjF2lbU5i-n4w92_-qcZJg6i2Swb__SIp3X2H8gt-6sHLFEGJZ7saapwTsSdprPzizuP4Yqvmp5dak1NW7-jg4PeZlwGmU3EA6Esgx2kxM9dS-sbHWiivBqGglpyLSPxTXcWC-BJEnQDO9p3ZBqKFvAgQAbjL4FF3gacP0e_zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:
طبق اطلاعاتی که به دستم رسیده توافق احتمالی بدتر از برجام است.
نه احتمال جنگ را از بین میبرد و نه گشایش اقتصادی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65950" target="_blank">📅 21:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65949">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
الحدث:
وزیر خارجه پاکستان امشب عازم ژنو میشود
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65949" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65948">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز هفتگی پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65948" target="_blank">📅 21:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65946">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSamrztZq_mj-FZ_MU_zNxBc9zXCHiva-AW2_eLBHdT7se77BQVOefgry1Rqcn6VyJhQpdwBqBFlZyqDomq3wErJHCf2SZRQqAjQjOxoynnBG3UalcaNq3YTI2MXqJDMeHsZ9VYIu_2alw_S_yjf7Dnez282tNlcDbpZqUGrd3N3mx1XunCvov9NbafCS79CnBGNQd0oVV7kNcMLCPBIPmCVoswcco-meSeqOSjxi0E_eGwtGC-DhBbXwiY5mHyBIUrIgW438vcIauAahLaQAlyz_7hAteDKMTrttLZ2KEN4q6j4MgGjjVVky5h1XVRi19uks48BEB2vNM2ZqS-0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز
هفتگی
پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
نفر چهارم تا هشتم ۲ میلیون میلیون
📈
۵ نفر از اعضا به قید قرعه ۲ میلیون
🏆
فقط پیش‌بینی کن و برنده شو
👇
➡️
@PishWin_Bot
➡️
@PishWin_Bot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65946" target="_blank">📅 21:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65945">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e7da6863b.mp4?token=LugVfm9f68xW-sk6JBqXWZurFI_0U5g9fYxGywduaS7b8EKwy_TJS_QAuZDfBVNq-lkPQLZTTMPntd_yApWIw7xdj4WNa8-SUmbSJUGywxu5snWB9ce7gdNH-Y2CHFs1ylj4dc9AMExzwGlDOrpT2ev341O99bi-gUDXxWh1S1nJXsa4EXs8KohibstNvMmJNN-ePvxjZcj9BOKSmrBoyVDRgMdJkpvWxWZ9N4Y9UapPewkQmPk7pNwfEYeNPnFQhWgXeDYsQYHejTXTkLLCEWD0PH9rTsTpvtD635NhjpgyPMeT6b7VwNjNKd-JKp1ZF0_OkMC4k0e7Cbr9juK62w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e7da6863b.mp4?token=LugVfm9f68xW-sk6JBqXWZurFI_0U5g9fYxGywduaS7b8EKwy_TJS_QAuZDfBVNq-lkPQLZTTMPntd_yApWIw7xdj4WNa8-SUmbSJUGywxu5snWB9ce7gdNH-Y2CHFs1ylj4dc9AMExzwGlDOrpT2ev341O99bi-gUDXxWh1S1nJXsa4EXs8KohibstNvMmJNN-ePvxjZcj9BOKSmrBoyVDRgMdJkpvWxWZ9N4Y9UapPewkQmPk7pNwfEYeNPnFQhWgXeDYsQYHejTXTkLLCEWD0PH9rTsTpvtD635NhjpgyPMeT6b7VwNjNKd-JKp1ZF0_OkMC4k0e7Cbr9juK62w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهباز شریف:   در بحبوحه تلاش‌های میانجیگری فشرده پاکستان، ما کاملاً از کمپین بی‌وقفه اطلاعات نادرست که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، به راه افتاده است، آگاه هستیم. گذشته از این سر و صداها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65945" target="_blank">📅 20:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65944">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tziqcvMKDryedfgxr-PyqKK_GXWtb0VggwQ__u4ozHYEfz3BOu4hSczhAGypFAUU8jJjZ57D3t6NZ1h2PXFGHfqP9tsADWv3ds75vmCH_vFnL_r1I4xI7xfs4DoGfFtZeU71Tz7uQWmbMStjnnBE39q-umNQ0s3qVB0bEvFjeTCj0a8nDzmiQ1Qff3y_L_2Ziq725I4lbU6QIDUSQ_pagGtZrMyvG8o_whNGm8nmYphom7kg6u9OGu-flhz2vX3Wtw_fPXmP9jc8LUTDZzfm9A1Xc6ThpTmH2mMlEWbUT4SwqkZcdqTOJprSR8_DtsWPAVn2FI1G7WFk-FpJnuI7Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهباز شریف:
در بحبوحه تلاش‌های میانجیگری فشرده پاکستان، ما کاملاً از کمپین بی‌وقفه اطلاعات نادرست که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، به راه افتاده است، آگاه هستیم. گذشته از این سر و صداها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق توافق صلح حاصل شده است و پاکستان اکنون از نزدیک با هر دو طرف برای نهایی کردن مراحل بعدی همکاری می‌کند. صلح هرگز تا این حد نزدیک نبوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65944" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65943">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b6a7c560.mp4?token=nbG0Oymmfzulz_6Q4mboysczj1ZPQmXBuw9pTAZRPfbVcBcGzwkW-Nfblulw6JnnNR2O5l9E9lJ6z4EolBHA5g9FdR-90DJ6OrMtlVsNIF32ivWqRRcXyjmBuRGf6xcxvvTFnUuRDazsLniK_BlKM98QGKbESpXNbQcUVOk-Iiy_sr8YBH6UF8Zj_e746jhm_HzNwaJGuK8XzGDrFRZ0keWR14XnGcb-_JFARpFOG78aN4wpYEUGsFNVr_E1XIF-pTsDByP9jwk9Sifmhnc3UNYJTnH5IThKbSXrNAKOS9R3C2ypRAqRdvHx8ak_PkcdrfZday3oxOhq9nUdKG1JNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b6a7c560.mp4?token=nbG0Oymmfzulz_6Q4mboysczj1ZPQmXBuw9pTAZRPfbVcBcGzwkW-Nfblulw6JnnNR2O5l9E9lJ6z4EolBHA5g9FdR-90DJ6OrMtlVsNIF32ivWqRRcXyjmBuRGf6xcxvvTFnUuRDazsLniK_BlKM98QGKbESpXNbQcUVOk-Iiy_sr8YBH6UF8Zj_e746jhm_HzNwaJGuK8XzGDrFRZ0keWR14XnGcb-_JFARpFOG78aN4wpYEUGsFNVr_E1XIF-pTsDByP9jwk9Sifmhnc3UNYJTnH5IThKbSXrNAKOS9R3C2ypRAqRdvHx8ak_PkcdrfZday3oxOhq9nUdKG1JNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از مراسم دیشب افتتاحیه جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65943" target="_blank">📅 20:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65942">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8WvTYqz_xiuvx3VkWjkualJ7r6t3QZ6xKzhNqo6DZACLK9RfnVlcY4txQTeJye_foxiVR-BhQ-z249K7N9rZZ6DUMMqx5SyleP0GcJHiqGeRcSYtGNyXgHwIXXz7iVBpV4rAZGFiBAHisNKwWtGOBCeySN8Kf5c-Kd9ghE_emLjxAPBj9fOn2beHtfbA-gx-Bi5duWFrhMowhpElkapqYDrzy2zcLFBTZca9PK96b44HRZqhATOKcYwGB2Juxk0iKa5YjKOPFoll4Tch2l9JLjcjiEqxDdWKC3jc-S1IMWMkQLa3IkIAcS_YhnjnZN4Ngi18mj8wlmotvmYjI6bmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندزی گراهام:
ایده یک صندوق بازسازی ۳۰۰ میلیارد دلاری، با توجه به اینکه چه کسی مسئول ایران است، به نظر می‌رسد بی‌معنی باشد. این شبیه طرح مارشال برای آلمان با وجود نازی‌ها در قدرت خواهد بود. آن زمان این ایده خوبی نبود و هر صندوق بازسازی که به نفع این رژیم تروریستی باشد، اکنون ایده خوبی نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65942" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65941">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65941" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65941" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65940">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfPguW-_gxrbMwofX6_lVADh9gOdkGr8asjeN0ZB3YKeB2G3RVuKymyWuD_hnQV9perteZ7GcLCJeKC0aHTkhlm3zBJMekSeCq46vp476m8sRcT7oa4lmQ5tXZyDdV8H8LW-1gIXyVO3iGwLgivauh6RUS_ryh6iCyflAsvCRMm-bZ9rHg2Z251ZOWl2hDwB15wiGcVwKIIXHTaCY_Rate02q6dZ8fBdxqC5WMoNTX0X-_id3w4hEGhEG8W8hu1ckAkWeX0cmUu0pBfWxDGNNLtNDUMYiip3hENkAIzy7R5D72k65ZBpzIf3oUV6zdr84dxrbPXYdNarS7S5vzD5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65940" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65939">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjH9XMW_FHwPpvk9lK84Ali5SWeWwSWncioXyaFXm5NJx49ptT-D7-6t1mWNzJRAjIFRpeg93Q6OqzNSF8mTe0Mre0AjG7y9SZMILtxCT3r3zMdczi-r-G9qOXTB3UazndOGbStm70G93Sqn9Gk7BsGf_GTdNM7is3ANriD_x9TQbT3I6qLZHilv08g1nUDxr76_NygQiKxo6uCQVe22Nndp63mln9slhZHdBzVeWn0HB36TF2IaO7_wktoyMi_B67asuxssCKeRXMM1vVPBd2WIeI8ZV3Jrj5WUqsRniBFclelMxQqDBz1s7f7wRSK_BHo5FJP_p9uH7jAfBJd3Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام:
ناوهای جنگی و دارایی های هوایی نیروی دریایی ایالات متحده همچنان به گشت زنی در آب های منطقه ای ادامه میدهند و محاصره علیه ایران را اجرا میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65939" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65937">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=Z2WiX17cYT1Kqenfi2Xlauxot2v4i3bS39R0-pTK4G8m47DW_3zpG5JXc3U1F7sC1lX24jaTWTQeDxwjxRSibeX_U6HouvVO8p0pvU4OkV_gEpYPWrbwvUhWxaScDL-j657sTvgXSg92fbojC1Am7Z9pTY3l8_nZj-r2ooEz35a3YpRawa7zZaAdmBoeJebDIQVg2OVpR_ZewVVDce6i6txOZaJgRL0v1xe_aEkmEcC9Ecj1C5OV_arZEZXgV3aUkagpNnTjKzdkk7d8DndKBM1lWvOWKPW_Wc4DIwn8pdQ9oy6Lf5mLT2XycgrFkr8s-ldyy5aLxVckzr3idH_lOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=Z2WiX17cYT1Kqenfi2Xlauxot2v4i3bS39R0-pTK4G8m47DW_3zpG5JXc3U1F7sC1lX24jaTWTQeDxwjxRSibeX_U6HouvVO8p0pvU4OkV_gEpYPWrbwvUhWxaScDL-j657sTvgXSg92fbojC1Am7Z9pTY3l8_nZj-r2ooEz35a3YpRawa7zZaAdmBoeJebDIQVg2OVpR_ZewVVDce6i6txOZaJgRL0v1xe_aEkmEcC9Ecj1C5OV_arZEZXgV3aUkagpNnTjKzdkk7d8DndKBM1lWvOWKPW_Wc4DIwn8pdQ9oy6Lf5mLT2XycgrFkr8s-ldyy5aLxVckzr3idH_lOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی قبل از جنگ ۱۲ روزه و ۴۰ روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65937" target="_blank">📅 19:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65936">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmlIdaQQyEhOcsjaYw1a1mzHpk2mcrGZzsaZwjYp34qZ3yRpRVhBqommCRbPU5SGQ5KocLgCxMsnBLOaIFTOu2Vsem-jIS8ifIzFZ78N2qjpy5wRGaj0WMX5HJv269MkGZ9oAMd4LCmgaSH8gryHo1tyK-8vHr2v_Wa4lI1aaUVEB-cwTd56GJ9cxmpWkp0NVFv8hDoIjO8mD8owqU7Og6dEIFavHokgOpDdqe3hrySAuwzA0dIS116YyZf7k9gm0UH-ohKukhhKLMeGLDRotxsbl-TCeJULD8sn-NJigRZLoagAMf0LHNSUjol2c3dPCR53yBHPklDPNREYlhh_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: تفاهم‌نامه اسلام‌آباد هرگز تا این حد نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از گمانه‌زنی در مورد محتوای آن خودداری کنند  @News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65936" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65935">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
جی‌دی ونس:
اولاً، ایرانیان هیچ وجه نقدی دریافت نمی‌کنند و هیچ وجهی صرفاً برای امضای یک توافق یا حضور در یک جلسه آزاد نمی‌شود. این توافق به گونه‌ای طراحی شده است که نگرانی‌های ایالات متحده و متحدانش اولویت داشته باشد، و اگر جمهوری اسلامی ایران تعهدات خود را انجام دهد، فواید اقتصادی به آن‌ها و کل منطقه سرازیر خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65935" target="_blank">📅 18:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65934">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تا دیدن اعصاب ترامپ تخمی شده عراقچی یه توییت زد گفت رسانه ها چیزی در مورد جزئیات توافق نگید :)))) #hjAly‌</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65934" target="_blank">📅 18:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65933">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ:   شرایطی که ایران به رسانه‌های دروغگو فاش کرده است هیچ ارتباطی با شرایط توافق شده کتبی ندارد. آنچه گفتند، از جمله بیانیه ضعیف و تأسف‌بارشان درباره وجود توافق، هیچ ربطی به حقیقت ندارد. افرادی بسیار ناصادق در برخورد با آنها هستند. هیچ چیزی به نام…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65933" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65931">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKXsjFW5HXwyUV09OMLUUn-6lmH5UPUQKSy5eN7SInREcqt8ZGsxCRO8YfNhFXeUBJTNS1i7pui-__CDZo10mhpgMpX8pVNUb8yDiMghunwrA5ME77cbngve-jf44mdXJ6nC0bhYe-wHBLvVM62B22SkhutCaV1winEaY75dct0vKepHeaENwuBocTqhwOUj0hFTeITdT6WuJfakuhbcaL_BGoBKKVszru4jda-BCbRQ3yKoz2fxiBtCLNXjaohiTgaFWxvKwdHqpTgrYiHb5h0FORBt8bnriDRlMrHrFY40JGPvQtEwfpQvy4i3ZfUQE8r1OwZPDR1FBImYheVNSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tPYrpqWfkTigu3V4PNk8SkYo6-MdDoYyfVCzUOf0P6EQMDFZgC2i9T6OBU9cq-q49AromJDpGt0ZuH3LHQ5_g-ot3nNsmKvs0QfsWfebiAIlvGyil5pYjKZ_82GpfWViZm9CXK4Fpel-5ZD5rqdkf3Etne72OihlYtqy3gmULyL5paI_bxTn5sCYUZAmBoICm1HCgtpb_nopcYrPsDScbnErMBcDlrEIO5etswxLftTFPhexLGf8t6MAv5oiiDg_jTdiMoR_rMEXD8RcrQK9qjPk1P_nkFPBrZYLYYDb_AqfR1TRTNhsMbCJ1Bfh_kotYZ79OSOR10kxleD20WRoDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
برنامه امتحانات نهایی پایه های یازدهم و دوازدهم منتشر شد.
شروع امتحانات از ۱۳و۱۴تیر
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65931" target="_blank">📅 17:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65930">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c65a1f96.mp4?token=bAPc3K2GT-YUrJSLe7jLZOg4jQU2yXGe5qM7xb-hEhZRSBPaB5KRWj2WEeYmEy32GMlGt4UCPx2Kmzl4BEqdPXyMJnFwjunH8Beg_z2u1NRlTs5P6rqCLRyC5G4dMWj7LMnYQ7_nUyAFNp6MC4hTQYr9dbUM3y1qasVPhYj8X0HRJyXzQx0i0DmGaO6VUABIJetzssUaEuZiih780NXZdT-T8Q5c5gApaTNBhvDMjRs-XarGO0uHxUkMEQ4qaeL7u6Az20POdJzz-ha7uRi8javpN_KFPhU7X32PMGFxOMk0msMmiclSgY_u1OEJpyY1Z9_AEUeMjw5VEMcKDPWQig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c65a1f96.mp4?token=bAPc3K2GT-YUrJSLe7jLZOg4jQU2yXGe5qM7xb-hEhZRSBPaB5KRWj2WEeYmEy32GMlGt4UCPx2Kmzl4BEqdPXyMJnFwjunH8Beg_z2u1NRlTs5P6rqCLRyC5G4dMWj7LMnYQ7_nUyAFNp6MC4hTQYr9dbUM3y1qasVPhYj8X0HRJyXzQx0i0DmGaO6VUABIJetzssUaEuZiih780NXZdT-T8Q5c5gApaTNBhvDMjRs-XarGO0uHxUkMEQ4qaeL7u6Az20POdJzz-ha7uRi8javpN_KFPhU7X32PMGFxOMk0msMmiclSgY_u1OEJpyY1Z9_AEUeMjw5VEMcKDPWQig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین طهلیل ویدیویی بنده از شرایط خاص منطقه برای عزیزایی که تو دایرکت درخواست داشتن
🙏
🙏
🙏
#hjAly‌</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65930" target="_blank">📅 17:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65929">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6007e01a82.mp4?token=HXE-NizyTyV7XHzfanVmZUhQjYvxbcJZe5hxooHEc9W-HwK3WAMHcF7UW7ZxOJq9GdlWysEev27m9uZ7wF5iRsdr8lbwem5NmL62JUkP5ogStWLyFaPCI52PGUfzHz_DHoWO9LxnpA9qRDeD78XtWNJA672zANKBheqo-SjlZtCnEL3xHuVQWs7wypsZU9s7oEksx6qd_tcFoXY8_MHPzYRwqvB1WoznoKWEsxALT6mVNXs14J_P5AotfIvr3jm7ZYhd9uQoHlGgW-BcYBHZlHPUQBLOHgOAr712x1rBI6CdRnEET7bIlxYYm3VL0BIRHXVWAm8LFkDXbBYpghuDOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6007e01a82.mp4?token=HXE-NizyTyV7XHzfanVmZUhQjYvxbcJZe5hxooHEc9W-HwK3WAMHcF7UW7ZxOJq9GdlWysEev27m9uZ7wF5iRsdr8lbwem5NmL62JUkP5ogStWLyFaPCI52PGUfzHz_DHoWO9LxnpA9qRDeD78XtWNJA672zANKBheqo-SjlZtCnEL3xHuVQWs7wypsZU9s7oEksx6qd_tcFoXY8_MHPzYRwqvB1WoznoKWEsxALT6mVNXs14J_P5AotfIvr3jm7ZYhd9uQoHlGgW-BcYBHZlHPUQBLOHgOAr712x1rBI6CdRnEET7bIlxYYm3VL0BIRHXVWAm8LFkDXbBYpghuDOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه ای ۶سال قبل:
هیچ پیام مستقیمی برای ترامپ ندارم چون اون رو شایسته مبادله پیام هم نمیدونم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65929" target="_blank">📅 17:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65928">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ:   شرایطی که ایران به رسانه‌های دروغگو فاش کرده است هیچ ارتباطی با شرایط توافق شده کتبی ندارد. آنچه گفتند، از جمله بیانیه ضعیف و تأسف‌بارشان درباره وجود توافق، هیچ ربطی به حقیقت ندارد. افرادی بسیار ناصادق در برخورد با آنها هستند. هیچ چیزی به نام…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65928" target="_blank">📅 17:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65927">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
ایرنامتنی رو منتشر کرده و گفته تفاهم نامه پایان جنگ دربرگیرنده این مسائل و موضوعات است:  ۱. موضوع هسته‌ای دست‌نخورده باقی می‌ماند هیچ توافقی در مورد پرونده هسته‌ای در تفاهم‌نامه فعلی انجام نمی‌شود و ایران هیچ تعهد جدیدی نمی‌دهد. گفت‌وگوهای هسته‌ای در مهلت…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65927" target="_blank">📅 17:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65926">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQN8zsa1-9qC0jc0UJtVzMaiRJ6Ai6JV4FA-vy3M3ObG0TEkHgCJgdtloAl3YZEB__PY92qOU5n36GNPmSJWATm9y-HKBzSXRmK6lgBb77PLTOX1qs-Zgo3RDMW9u1A8ewrxA0DV4XVVGoT7ez1PNo7oynk10rjz8I5eoKuLI5dZkHaZTUCBKymBFMqFvjM-hB9b5hXzop4o3YVDG4xGpI8OJW1vRSQHLVn7TPME_Gar6MvHLfBPL_W1pG880D89qFxlsOn3neYqzpE1SLagC-zWhixrzFU7QxikR4DdnQ9SHezbIG7CMntzRRPBqN2Y0GbGPykP4ZwV8KKZv1twQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلاکاردی عجیب در تجمعات شبانه
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65926" target="_blank">📅 17:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65925">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKQU6hjofNEs0GYtO-aJYcM9NSlA-l7508_VWn3HFFfkk75YBA4-x35AVOEq2pMJqJHQp6SK_w5lMwMZKW2KDJqWlogHq43xYyIOieM2YeNjHNzyp0hJCK6C-6aIBvB-qm1brlHbVtE1jBpwFvkT2fW9_9x4WqG-4TtL99x0cVYLttpwWm_BurtQpcvDS-XYFRriv2W6i7gfiKr1EQ5jMhwF76hlvmt6IRUEJ8GyztA8mFtPRqf-AnkMmxzJT-4IbNiPoPK_wGkemyFQ7ryafDVs4pOqorsbXrNFsw1hC53brewE8yzLhYJIW5XllpWGP09q6CET3SswtcZ9gtWQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
ترامپ در سال 2049:
ایرانی‌ها هر لحظه ممکن است توافقی را امضا کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65925" target="_blank">📅 17:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65924">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAAsgFfHRrW5tlU4Sc5hkYxVWPiUh0y_BKPYxOaRa4S6uQL07dZ3MceEznlWbVxIKPZ5ukFzOmn55KMA0fnPPCMs_At20KdyO6VuEfoL6uNpXFIlTfbGhK9tYJkN8R34kzq9DyS6_wI8msR_m7ccMTbzpOlTgUjWYYVI9MpXzKIDxP-KqRP14ZR3R3iivbnxdtk54aP0AxRHIOPq570-xj0suNwvSUOq2k7LrtZHekVC2P8BPkoTqDRwo6RtDkLEKkdK24R1TG7CHobOt_eyyZU8npP-JT7JOtgxUOx8a8fovwwfIcqVbeFRRnENCFQlEiCuslzCU1UAO8M1x5GOoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
مرندی، عضو تیم مذاکره‌کننده: یکشنبه در ژنو اتفاقی نمی‌افتد
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65924" target="_blank">📅 16:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65923">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f5e54d8d.mp4?token=CCAnPwsrg9KutM31-TrjAsyeGKZltyapVPOXIJp3SQWYI6jClnPFHS6VmfQXmElsDroEnROEne_4GlWOp3ibSXa2Ppjn20ryOIs7JwJR6_mdlmF4Xp1tE11CjZEYpPDW4glCdp4JFNe4H8UxQ2R6U96G0nPkJe2jvk3YhnckPVFHCCOecHKc4fPFdliBAaQrXHGM_6H9Nl98OJ6Ykwu3GwMgEZjHV9PzDWoTOpjxWCFTbKKd3pUzN03zOky4oA_LGoRt_eA_p9i7QklRVgxKQzzli3ZbybhxKsSBzs3zO_0S8hqWCeAK4Zm6vSPg9CYjf2okZEoNEt_1QoOBFshxKHfQUVcPhnxNzgAVjyMsTeAjp4PwJ8aXHahFJClxK_zE8I1uTflX40BtdflGE9nhzCcFVylmXo8T0yyeGWsTpzXKw4p_REImkcXYflVDNKWl0lSpQxbqVpKnaAM4tpA_7lDPIxh2qFQl22fH2tEg-gAlZ6a28dFE5KUnPz0-bMgCIs8VDmU6lfQKaqdFfUToaE3yYRf4QkcVlN7GspJRPxX90YjJpFLdqBS-RIrv3A6oTg3PMGGAjKTV3bu1GOvOIAXJGvJacCIMwkfd-vgmYAJWxetN31YlP94P6f-h2AIMTXbGThAT5CxXoTF5b1nlreGr1g1H03jxHtaFltKdTDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f5e54d8d.mp4?token=CCAnPwsrg9KutM31-TrjAsyeGKZltyapVPOXIJp3SQWYI6jClnPFHS6VmfQXmElsDroEnROEne_4GlWOp3ibSXa2Ppjn20ryOIs7JwJR6_mdlmF4Xp1tE11CjZEYpPDW4glCdp4JFNe4H8UxQ2R6U96G0nPkJe2jvk3YhnckPVFHCCOecHKc4fPFdliBAaQrXHGM_6H9Nl98OJ6Ykwu3GwMgEZjHV9PzDWoTOpjxWCFTbKKd3pUzN03zOky4oA_LGoRt_eA_p9i7QklRVgxKQzzli3ZbybhxKsSBzs3zO_0S8hqWCeAK4Zm6vSPg9CYjf2okZEoNEt_1QoOBFshxKHfQUVcPhnxNzgAVjyMsTeAjp4PwJ8aXHahFJClxK_zE8I1uTflX40BtdflGE9nhzCcFVylmXo8T0yyeGWsTpzXKw4p_REImkcXYflVDNKWl0lSpQxbqVpKnaAM4tpA_7lDPIxh2qFQl22fH2tEg-gAlZ6a28dFE5KUnPz0-bMgCIs8VDmU6lfQKaqdFfUToaE3yYRf4QkcVlN7GspJRPxX90YjJpFLdqBS-RIrv3A6oTg3PMGGAjKTV3bu1GOvOIAXJGvJacCIMwkfd-vgmYAJWxetN31YlP94P6f-h2AIMTXbGThAT5CxXoTF5b1nlreGr1g1H03jxHtaFltKdTDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هگست وزیر جنگ آمریکا امروز ۴۴تا پرس سینه زد
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65923" target="_blank">📅 15:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65922">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
خاورمیانه در این مدت
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65922" target="_blank">📅 15:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65921">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
ایرنامتنی رو منتشر کرده و گفته تفاهم نامه پایان جنگ دربرگیرنده این مسائل و موضوعات است:
۱. موضوع هسته‌ای دست‌نخورده باقی می‌ماند
هیچ توافقی در مورد پرونده هسته‌ای در تفاهم‌نامه فعلی انجام نمی‌شود و ایران هیچ تعهد جدیدی نمی‌دهد. گفت‌وگوهای هسته‌ای در مهلت ۶۰ روزه پس از امضا انجام خواهد شد.
۲. تنگه هرمز؛ نه واگذاری، نه نقش آمریکا
ایران هیچ تعهدی در مورد واگذاری مدیریت تنگه هرمز نمی‌دهد. آینده اداره تنگه در چارچوب یک امر منطقه‌ای و از طریق گفت‌وگو و تصمیم گیری مشترک تهران با عمان حل و فصل می‌شود.
۳. پایان قاطع جنگ در تمام جبهه‌ها، از جمله لبنان
هدف اصلی تفاهم‌نامه، پایان جنگ در تمامی جبهه‌های منطقه است. آمریکا تعهد می‌دهد که اسرائیل را وادار به پایان جنگ در لبنان کند و عبارت «تمدید آتش‌بس» در متن جایی ندارد.
۴. آزادی دارایی‌های مسدودشده با ساز و کار مشخص
بخشی از دارایی‌های مسدودشده بلافاصله پس از امضا و بقیه به تدریج در طول مذاکرات آزاد خواهند شد. تهران تضمین‌های روشنی بر اساس ساز و کارهای مورد نظر خود دریافت کرده است.
۵. غرامت جنگ در دستور کار
خسارات وارده به ایران در تجاوز آمریکا و اسرائیل از جمله موارد مورد اشاره در تفاهم‌نامه است. ساز و کار اجرایی دریافت غرامت در مذاکرات ۶۰ روزه پس از امضا مورد توافق قرار خواهد گرفت.
۶. جزییات رفع تحریم‌های اولیه و ثانویه؛
موضوع مورد بحث در توافق نهایی
رفع تمامی تحریم‌های آمریکا و قطعنامه‌های بین‌المللی در مهلت ۶۰ روزه مذاکرات هسته‌ای بررسی می‌شود.
۷. سه موضوع و ۶۰ روز برای توافق نهایی
در مذاکرات ۶۰ روزه تنها سه موضوع بررسی می‌شود: استمرار برنامه صلح‌آمیز هسته‌ای، رفع تحریم‌های یکجانبه آمریکا، و ساز و کار جبران خسارات. هیچ موضوع دیگری در از جمله توانمندی موشکی ایران، دستور کار نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65921" target="_blank">📅 14:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65920">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
متن توافق پایان درگیری میان ایران و آمریکا تقریبا نهایی شده و منتظر تایید نهادهای مربوطه هستیم.
متن نهایی تا زمان پذیرش قطعی آن توسط دو طرف منتشر نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65920" target="_blank">📅 14:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65918">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jv53ib9lwLBOIobv1etRZPxeoAIRIWs2P4jsGNln2t-5xmOQqN2dyvOR9iZVczR7LJlC7FBcxWpu9QiOmx6m3RZXMOuoQmJAaTHuNS4ByV5CcQWRhOyhee3aSOFpNYZgwjojJ9ObKVcZSu915XEGnE12x4uFjVC_7NTHLMY8XlYRdrnvuBTXLrrRbp349qm4q-8hH8ffCzWFp2-sGpWkA_4t1mdvHtW3J9Zx21io3pIwB0JkYGVkhRdPtu-uEiGCdfpSGgfGHXDjlJzPOWkYh7mwSzAmG9f3iikGlLOiqNqpNvwSxHPKosWKOaMheqr5LWDiXJGHCZfDNh-EzlhJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQdylPiTz3wjgxtRf909izf3Ni_-Pqc7ExKg3Fk4GIWw39BRRmCtsvJgHgpt9zb7IfVblSZfTlOgDUKZAPcLbBhrk2Acrzrm7p48s_87HWXtOptxvpuCwCYvp8rR4pm4PyjRpmOSfiymVr9KZR2RlH-N4m7EXVZmGuWFZawVa_FA_M_ih_Z5c_amGYOEAFGvcicQGL61ONDs3t7uEn0TYVRQwV4syltTdkC2QMVtYSFlmRvUjOXzCY99E8TCQz3GONo09pJp75yAq5vAoPMvLp_03zwcF_Fs1XRb_zwKT_6Za-gLhwYAvL0Sf5vASmDVAYqKmZt1SMaRyGB69sP3gA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصویری که یک پرستوی نظام در تجمعات شبانه از خودش منتشر کرده درحالی که چاک سینش پیداست.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65918" target="_blank">📅 14:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65917">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aed65f61d.mp4?token=cYQvKuu2kiK2zypuBX9wy-tipjodjRIdPI8KsyXMBFBtPXalIQ27l1ljlPcsffIupWQR5CSz1Fu7TCiPf_nUa6OAy2ZlL2acyD9tODugrfVL5zO1JpLpLtTuMCvIYkrKeyhK1ZMNEhwJIvTtX_PtHpxIB-X1sw_AfowUbY524BzMkOLFUgnwMmIJu7Mcj8so5ga1yh8evpchrdOXZKjuv-LkcVjaZffQsyWNhZXSr4eKXXFJ0_CkNb7GVZ2e60Jh4iKol_hnI_YfFsjRgBVglxF-ODRMZFylEWDGDRVvHci-0P9WEbvCUcqiZ3Av2Yv4kUo3GbB9Zr3PyrOK-sfA1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aed65f61d.mp4?token=cYQvKuu2kiK2zypuBX9wy-tipjodjRIdPI8KsyXMBFBtPXalIQ27l1ljlPcsffIupWQR5CSz1Fu7TCiPf_nUa6OAy2ZlL2acyD9tODugrfVL5zO1JpLpLtTuMCvIYkrKeyhK1ZMNEhwJIvTtX_PtHpxIB-X1sw_AfowUbY524BzMkOLFUgnwMmIJu7Mcj8so5ga1yh8evpchrdOXZKjuv-LkcVjaZffQsyWNhZXSr4eKXXFJ0_CkNb7GVZ2e60Jh4iKol_hnI_YfFsjRgBVglxF-ODRMZFylEWDGDRVvHci-0P9WEbvCUcqiZ3Av2Yv4kUo3GbB9Zr3PyrOK-sfA1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وزیر ارتباطات: بستن اینترنت امنیت نمی‌آورد. وقتی اینترنت قطع بود، وزیر اطلاعات، لاریجانی، رییس اطلاعات سپاه و بقیه ترور شدند. با بستن اینترنت، جوانان نخبه مهاجرت می‌کنند و این ضد امنیتی است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65917" target="_blank">📅 13:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65916">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‼️
ترامپ از زمان شروع جنگ ۳۹بار گفته با جمهوری اسلامی به توافق میرسه
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65916" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65915">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30551bbbff.mp4?token=fSIJnDIgKLiXBjEpAhPoKc1j2BjHiEMGa1bG0G1zvXCgvWki1rYT8Qyan_Q6UMRPEHtNvhXw51Meo_e9sMeQaU5lMdzwFmGErdAxGQLpzc-bxrOt4WKHPsdPg6SliE8934poGK92Mqxrs8rEpCGCybKit0_O7oTTvDBZKeoae8tTvHNtf3srNU9mGi3ry-eCnmbaBmVdYY1gGCm9bMKQSgoZHpikah4CacXLJnMfw0lzfCPPIhC-Vm34kfXqihMpUr6UPWsd3WDR9mZGm6izqe5X2KMiQ8c2jireqYOT-0wvjR9sH7BuZTpaE17i35kLjeMzenSa5-us4t8fxCx-NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30551bbbff.mp4?token=fSIJnDIgKLiXBjEpAhPoKc1j2BjHiEMGa1bG0G1zvXCgvWki1rYT8Qyan_Q6UMRPEHtNvhXw51Meo_e9sMeQaU5lMdzwFmGErdAxGQLpzc-bxrOt4WKHPsdPg6SliE8934poGK92Mqxrs8rEpCGCybKit0_O7oTTvDBZKeoae8tTvHNtf3srNU9mGi3ry-eCnmbaBmVdYY1gGCm9bMKQSgoZHpikah4CacXLJnMfw0lzfCPPIhC-Vm34kfXqihMpUr6UPWsd3WDR9mZGm6izqe5X2KMiQ8c2jireqYOT-0wvjR9sH7BuZTpaE17i35kLjeMzenSa5-us4t8fxCx-NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آتش بس در خاورمیانه:
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65915" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65914">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65914" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65914" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65913">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=ThEktdwtoQL0F-8wJlZW2s-Wug2tU-7KDFHXvCW2dFyM1ApEMDGoWNaadNwBapqORYhFBpvOAWzupmkJmJWG5TM2dfrwdV57ss94z7TxLwEmUwUSaZEmHpnL1u3HpBs6Nn68ppmsAVfOMO9kRBbJb9mNygQdoWKP5Myos4sqNqKD0ySIitDhzo7RrN7dZZG_uSa871YKDXaZjD5S3MPiNmq0hOC9AWrT2VzGbreLKnLxxQfm7nzZFErlPZY86S0HBUWNQ5xTSJ1xcHSNN-Hf3WlYNmkbcJq3CbegjCtmCbLyu8gUyH2JBIYGoAhPzMIJ6eNP2fSU_EiClzZmy173Hkop8V8wPYdiNCIv7zC846brv6H0wrDCUAKtAWxpHSYtk8HiexEUiUU6jhm8kHgJwa64k5VhkhbAH74gutbIW0jaP9h-LGnt8VNyXiWOSXp5KYLKjwMh1MG7nu3CY-CLfur_Gc1sPYXPkYMtYEPdNuk88FSC_M8Lvv3u9Hmwt7GhvHL18tgxcnwp_OiNtFQfYV47RT18jVZxcnVfgafOIBV7FbmtshqGZ0EZhJ6WMbX67DwIY42LgqBIUtJ7iig3UidyMhi-zw_1BTqK9DX0lxp9psSz06QwYQOzkiP-XwdPfW8rhNbNgkPAE8bESJm-KVUFFFfQlte6cNdJ4eGGfs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=ThEktdwtoQL0F-8wJlZW2s-Wug2tU-7KDFHXvCW2dFyM1ApEMDGoWNaadNwBapqORYhFBpvOAWzupmkJmJWG5TM2dfrwdV57ss94z7TxLwEmUwUSaZEmHpnL1u3HpBs6Nn68ppmsAVfOMO9kRBbJb9mNygQdoWKP5Myos4sqNqKD0ySIitDhzo7RrN7dZZG_uSa871YKDXaZjD5S3MPiNmq0hOC9AWrT2VzGbreLKnLxxQfm7nzZFErlPZY86S0HBUWNQ5xTSJ1xcHSNN-Hf3WlYNmkbcJq3CbegjCtmCbLyu8gUyH2JBIYGoAhPzMIJ6eNP2fSU_EiClzZmy173Hkop8V8wPYdiNCIv7zC846brv6H0wrDCUAKtAWxpHSYtk8HiexEUiUU6jhm8kHgJwa64k5VhkhbAH74gutbIW0jaP9h-LGnt8VNyXiWOSXp5KYLKjwMh1MG7nu3CY-CLfur_Gc1sPYXPkYMtYEPdNuk88FSC_M8Lvv3u9Hmwt7GhvHL18tgxcnwp_OiNtFQfYV47RT18jVZxcnVfgafOIBV7FbmtshqGZ0EZhJ6WMbX67DwIY42LgqBIUtJ7iig3UidyMhi-zw_1BTqK9DX0lxp9psSz06QwYQOzkiP-XwdPfW8rhNbNgkPAE8bESJm-KVUFFFfQlte6cNdJ4eGGfs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65913" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65912">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
کانال۱۲اسرائیل:
مذاکرات نهایی آمریکا و جمهوری اسلامی در مورد برنامه هسته ای و مسائل اقتصادی است و برنامه موشکی در آن جایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65912" target="_blank">📅 12:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65911">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
یه‌یارو بیکاری بلند شده تمام اسکناس‌های کشورای مختلف دنیا رو جمع کرده و باهاش ویدیو ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65911" target="_blank">📅 12:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65910">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
رهبران قطر،امارات و پاکستان کسانی بودند که مانع حمله دیروز ترامپ به ایران شدند.
سران این کشور ها به ترامپ وعده دادند که توافقی اولیه با جمهوری اسلامی دردسترس است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65910" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65909">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9247426e69.mp4?token=qCtm6N1IpGCCTUiElA-DCrLv8mTO1q7cUYRcOuhlWx3uqYMX2qOznzJ5R_yRd-OdcbXxYGRXj_XRUIRrDApuUn-myLg0W1xYrMASqODaTAwuuuaXp58exzp_S__8HvnZ69aVfPbfkMdiFyhkLMtkDHeyRr1MxNt1o3eoloZl7ML1WPUgCuCHNJ0MFZEqUddqun4CfTLUjEeb4CmjItamBRQ6HzL1NFowc5yCMhfTqQ7P8682M0pGmGRST3fk56wDs5JWgswHyX4jGcy4lriLyQ2kD7boSXc0A9h5vdtEWfVrkmeh8XgXOoqK_cg5vbS4hiiqwXPCYbLKTL83m-wXfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9247426e69.mp4?token=qCtm6N1IpGCCTUiElA-DCrLv8mTO1q7cUYRcOuhlWx3uqYMX2qOznzJ5R_yRd-OdcbXxYGRXj_XRUIRrDApuUn-myLg0W1xYrMASqODaTAwuuuaXp58exzp_S__8HvnZ69aVfPbfkMdiFyhkLMtkDHeyRr1MxNt1o3eoloZl7ML1WPUgCuCHNJ0MFZEqUddqun4CfTLUjEeb4CmjItamBRQ6HzL1NFowc5yCMhfTqQ7P8682M0pGmGRST3fk56wDs5JWgswHyX4jGcy4lriLyQ2kD7boSXc0A9h5vdtEWfVrkmeh8XgXOoqK_cg5vbS4hiiqwXPCYbLKTL83m-wXfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یکی از کشورهای آمریکایی پلیس به یه زن مشکوک میشه که ازش اسلحه بگیره. تهش طی تحقیقات زیاد متوجه میشن اسلحه رو تو واژن خودش مخفی کرده و با تهدید پلیس مجبور‌ به تحویل میشه
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65909" target="_blank">📅 11:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65908">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
خبرگزاری حکومتی مهر:
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا منتشر شد. این تفاهم شامل تعهد آمریکا به رفع تحریم ها، خروج نیروهایش از اطراف ایران، رفع محاصره دریایی، بازگشایی تنگه هرمز، لغو تحریم های نفتی، و پول های بلوکه شده ایران است.  آمریکا موظف است طرح بازسازی اقتصاد ایران را ارائه دهد و در حالی مذاکره نهایی میان دو کشور باید در مسایل هسته ای و اقتصادی انجام شود، بدون بحث درباره برنامه موشکی ایران. این پیش‌نویس نیازمند نهایی شدن در نهادهای مربوطه است
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65908" target="_blank">📅 11:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65907">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک دیپلمات از یکی از کشورهای میانجی که بندهای متن فعلی را با من بررسی کرد، گفت که «ایالات متحده و ایران در مورد متن توافق به توافق رسیده‌اند»، اما اذعان کرد که هنوز تأیید نهایی لازم است. با این حال، هواپیماهای نیروی هوایی ایالات متحده دیشب با تجهیزاتی به مقصد اروپا به پرواز درآمدند تا برای احتمال سفر معاون رئیس جمهور ونس به مراسم امضای توافق در ژنو در روزهای آینده آماده شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65907" target="_blank">📅 10:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65906">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
⭕️
توافق قریب‌الوقوع جمهوری اسلامی و آمریکا بزودی در ژنو امضا خواهد شد و به‌نام توافق "اسلام‌آباد" نامگذاری می‌شود. طی این توافق یک آتش‌بس ۶۰ روزه که لبنان هم شامل شود، شکل گرفته و ایران می‌تواند با پول‌های بلوکه‌شده خود کالاهای بشردوستانه تهیه کند
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65906" target="_blank">📅 10:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65905">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=sLaeRhV-AJm6gdBNhzdzy8-oHlrzPUsvY5DhOBCMDxSB3NBeHGgNK7E7matDm19i8oaBIQ1-6wxWQvAowYffuGdEINboYm1XHN8zW02QErwmpwXsLtVNyC6oK8Ft84TxVYORTyKx37QGOFVmz6JwhQ0SUIfA0CfoU5-uZBzMJ8kkX-ji6XerP4CE01x7y8kycIne3hLrKLjJlAmCm4d1NtqYF5i9_3AZpX905ZQ1MIq0DPFrKwfcroOxPZTOiRsRzryqe3Me-YnetJVH1sAzWFSt6Z5xHyCwUauOMpOL-rwRor0ZkgHOGlWvOJnhsYyY3-9gZvPVvhcmvIHKAoNvqhu5M7Q0rhNMkInum48jZ0YNPQeBfssxVGPEIqe0CzruhXh01wAM4xplQpD9tsCmhGUScNBhVPXPCxzOfYVPSsh889RqNf8WMjTGJKMwwDXXax5xorlNzS_Mk4Qpy8zHvhivgp4T2Jg4sIrq2n3S1LtihOV6gMaloD72vYmTk_nqHtwQtNlGsR2ar7R802NLI9fM4igW_72hyCZcxUUh8GY4KEBgbQ4y9yLkZHD6gNjnuDxY3S1w3G14KBheEHbL8dJuswcMEg4kLGJgmjjbaeru2XjZVrq8-meU_uTvc7Q_7ecNQ7kwR2QYqqsEPWL1tKSUjYXirHuDw8rY4U_XdXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=sLaeRhV-AJm6gdBNhzdzy8-oHlrzPUsvY5DhOBCMDxSB3NBeHGgNK7E7matDm19i8oaBIQ1-6wxWQvAowYffuGdEINboYm1XHN8zW02QErwmpwXsLtVNyC6oK8Ft84TxVYORTyKx37QGOFVmz6JwhQ0SUIfA0CfoU5-uZBzMJ8kkX-ji6XerP4CE01x7y8kycIne3hLrKLjJlAmCm4d1NtqYF5i9_3AZpX905ZQ1MIq0DPFrKwfcroOxPZTOiRsRzryqe3Me-YnetJVH1sAzWFSt6Z5xHyCwUauOMpOL-rwRor0ZkgHOGlWvOJnhsYyY3-9gZvPVvhcmvIHKAoNvqhu5M7Q0rhNMkInum48jZ0YNPQeBfssxVGPEIqe0CzruhXh01wAM4xplQpD9tsCmhGUScNBhVPXPCxzOfYVPSsh889RqNf8WMjTGJKMwwDXXax5xorlNzS_Mk4Qpy8zHvhivgp4T2Jg4sIrq2n3S1LtihOV6gMaloD72vYmTk_nqHtwQtNlGsR2ar7R802NLI9fM4igW_72hyCZcxUUh8GY4KEBgbQ4y9yLkZHD6gNjnuDxY3S1w3G14KBheEHbL8dJuswcMEg4kLGJgmjjbaeru2XjZVrq8-meU_uTvc7Q_7ecNQ7kwR2QYqqsEPWL1tKSUjYXirHuDw8rY4U_XdXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه خبر:
با صراحت میگویم بخش عمده ای از شروط ده‌گانه در توافق وجود ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65905" target="_blank">📅 09:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65904">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=okRXe3IuZVCUDSkdaKzsVa5NYC306vfZje_bKkpvdnq4nkBVUh-vcL5sn84T7s3tB2IvTLTGtl0nJthaxntZD4P7zz5W4RrDZe-6fNx8onDlwu6eQmPbqIMwb917iPaOasrgJN1sF1w2yTx4sgbHDpk2ImlKVT9q8ZdhcIoxRKAvGs4DAdEKiTBCZur4kaT_0ZGM4rgSYgrnHnyGhklqsEuGvRLq6IM6DUsr6DHp8dNfMT1u1BEwxoT4UBu_LaNMtOBnT27UHCy9pDrM1Nr9880r9gQxxtMlp7Z8RUe_tGhigdl4ZOC82EIuaof3I4u0KC2rECE2uWWwiS5Vdrs4bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=okRXe3IuZVCUDSkdaKzsVa5NYC306vfZje_bKkpvdnq4nkBVUh-vcL5sn84T7s3tB2IvTLTGtl0nJthaxntZD4P7zz5W4RrDZe-6fNx8onDlwu6eQmPbqIMwb917iPaOasrgJN1sF1w2yTx4sgbHDpk2ImlKVT9q8ZdhcIoxRKAvGs4DAdEKiTBCZur4kaT_0ZGM4rgSYgrnHnyGhklqsEuGvRLq6IM6DUsr6DHp8dNfMT1u1BEwxoT4UBu_LaNMtOBnT27UHCy9pDrM1Nr9880r9gQxxtMlp7Z8RUe_tGhigdl4ZOC82EIuaof3I4u0KC2rECE2uWWwiS5Vdrs4bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته شده ترامپ بعد دیدن این ویدیو تصمیم گرفته که توافق کنه
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65904" target="_blank">📅 09:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65903">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vr68w4g_IxAJ0YJC5JUT6txg9hVehY9UBcWJzn3LTrRseBu7XQ2-FiDKAsqBSoWwIutq82mPoS2QXPEpQfQurNj3vZYSjEd8ZymjG0myPw3DXH-ZPMqVQQs45gLaDbTdYyx6h8xEy0b5PBFnrWbgCWE6MlW_c-pleVWFPB1c5ZhXQijiO2EE1MSuh-xlsjwqjdy-UemtjSNjkkxtNE-KHJ8C37c8UmrX2Fh39gzCCEeD3P3cf5vVu2KQoYTNPnnTjmiEF41sxxvGTNN12n5eehwHHTiJ-ipWGVMYfHPlsEHEYSBawum_LNAoxiLJVqDq9UgX9Cfc_We-Hopn9hWdVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین:
اگر همه این دولت‌ها با این توافق موافقت کرده‌اند، شگفت‌انگیز است که چگونه همه این دولت‌ها به این سرعت امضا کردند در حالی که ما اعلام می‌کردیم که در اسرع وقت بمباران خواهیم کرد.از آنجایی که این توافق انجام شده است، آیا می‌توانیم آن را ببینیم؟
در این توافق چه چیزی هست؟میتوانیم آن را ببینیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65903" target="_blank">📅 04:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65902">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVrDIjW7uk5bsxEfxJEZ42n-Zur06BK0KUXH7W-fUPyh3rwHh5QnjkVVsbuMu8s4VdIcftTHj1ecNWGXjtEskBZLuJDBXP2XLbABeuqTH3rh6d0kwdmhqlOKSGD6V0uFFP6f7VmZiQTwQNX-02eXua6Sn4-O8Mcl-fs4XHDa27vEhyahaS_p67WPJ4ZbF_ThZe6SJptijJ9N-7y2iqPO0uEkj9WspLQ978uZQRh0CrGqwPO5EafI8SfLtpSRwzqdVhW1waKnd2JTPkXZlWPEnqC6dsvB0UQ1h2wS6eDKDCZTkNZnjx1ffdgWDXRe_Z9GvnawAhBOlkW5G-blyZ225Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دقایقی پیش زلزله ۳/۱ ریشتر در پردیس تهران به‌ وقوع پیوست
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65902" target="_blank">📅 04:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65901">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
رئیس‌جمهور ترامپ درباره ایران:
ما با ایران توافق کردیم. معامله بزرگی انجام دادیم. هیچ سلاح هسته‌ای وجود نخواهد داشت.
مردم خیلی زود به خانه‌هایشان بازخواهند گشت. تقریباً همه چیز تکمیل شده است. ما هر آنچه می‌خواستیم را به دست آوردیم.
نکته مهم این است که هیچ سلاح هسته‌ای در ایران وجود نخواهد داشت. یعنی نه توسعه یافته و نه خریداری شده.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65901" target="_blank">📅 03:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65899">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78687e07ef.mp4?token=NjJc0KqBORJVDjEvHp7i6MGCxrxnE-k3vfzHzv1Z8vvsWhfXFq71_SF0hM-Ln8rx7Cbi4_QHGJjprlf6FQRZ3nrcTkpkh7PTSQf96J71v5aWBrxUnT_02Nour6gK-7-49OIsnzrR71PdP_a-zNaAByE01O7JqV5yvxqaCH8ESd6qLcqosETWDVoXibafLpMR85TwhuAXzXkf3HJdkWELGou7zXoyHp3FkQB1CRSXxiXgYvTh4UjgUK_vBP86-CfCvUZjcxU9lZEuCMdJsHUROhuwOkqktbYn3mXiflz2QfeUPSAKJDmq35EZNZ3f8iROjN0ree_mJkbI5mo4ueYmqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78687e07ef.mp4?token=NjJc0KqBORJVDjEvHp7i6MGCxrxnE-k3vfzHzv1Z8vvsWhfXFq71_SF0hM-Ln8rx7Cbi4_QHGJjprlf6FQRZ3nrcTkpkh7PTSQf96J71v5aWBrxUnT_02Nour6gK-7-49OIsnzrR71PdP_a-zNaAByE01O7JqV5yvxqaCH8ESd6qLcqosETWDVoXibafLpMR85TwhuAXzXkf3HJdkWELGou7zXoyHp3FkQB1CRSXxiXgYvTh4UjgUK_vBP86-CfCvUZjcxU9lZEuCMdJsHUROhuwOkqktbYn3mXiflz2QfeUPSAKJDmq35EZNZ3f8iROjN0ree_mJkbI5mo4ueYmqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ درباره ایران:
امروز جنگ با ایران را به پایان رساندیم و آنها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن تأکید داشتیم. این هدف اصلی بود. این ۹۵٪ از موضوع بود و آنها این کار را به قدرتمندترین شکل ممکن انجام دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65899" target="_blank">📅 03:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65898">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65898" target="_blank">📅 01:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65897">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ikHTQQkSfvcVbNL0PUZVuW-7L4hREYZl6MWdWcIdlG-h48TR7_hSGAJoSRJ-8kOalOBLHDRJoqSRK1YB2n8ssG5-Y2-kJHGVJlTvu5WKujSijiQefgUtWTTqII4uFvFduVMK13uHwzOnrZeCD_6GekLjFwc2y4wBt7J0T8IMqqdId_g3uLVkGyn6ZmQfJmED4M3Wr0UwkIMi7gvVugSwk-Z48saMSj-ZfORQ9pa-Us8_dUi2Ji5zu0-_L1v4QvxIsgVIfrPnkxgWYZ-6pGzQ8X_4uP0UfHdNW48MjnWrvTrl76H2jFEJsFVlQHiNkh-FXeNAmn7-UOrnPYQDKStcng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65897" target="_blank">📅 01:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65896">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
صداوسیما:
شنیده شدن صدای دو انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65896" target="_blank">📅 01:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65895">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxGPa802LHXHiZ6u5ONuS8R55s9ZkZCvKNYoYpFhYEeuxRdnvwtDKEm_Lo9YoC1bAxDQFo1dTIQmXutmnmEO6iRy5yd32Yu0cj3p6YxP-5690eZUlhdsd0VeICmukZymz0KF8pnMHo-wJ-rLqfnVNPYMSNl-PlSD7Dcka0Y2MfLMCNuKCcohItep0GmPPy0M5xN4fSPoyrSIWSjfV86zfzzjS-B0o3--pj8mfcbemk1nZM7eaWruGOotkyWuudwZOV-yxJS2v1ripNxaM9Ft-1T4BWP4mzfsTS0V16xGJZ_8U6fQLu7TThUJ1OUcL0RW5v9xL4sePS7WwRxOea2x0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اعلام کد اضطراری یک F35 در آسمان امارات
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65895" target="_blank">📅 01:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65894">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دیگه نمی‌زنن
😭
#hjAly‌</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65894" target="_blank">📅 01:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65893">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
فعالیت سوخت رسان های آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65893" target="_blank">📅 01:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65892">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
مهر:
هنوز از ماهیت و علت این انفجار اطلاعات دقیقی در دست نیست، اما با توجه به دستورالعمل‌های مربوط به بسته بودن تنگه هرمز، این وضعیت احتمالی می‌تواند در همین راستا باشد
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65892" target="_blank">📅 01:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65891">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
گزارش هایی تایید نشده از انفجار در گناوه
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65891" target="_blank">📅 01:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65890">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
منابع محلی در سیریک صدای انفجار شنیده اند اما هنوز علت این انفجار ها مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65890" target="_blank">📅 00:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65889">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pke6Ma6L1SCjqk37cAqeFAEh82VYeACUTem1FmtiObovKG6ToDJKO7M40e0D1Gc8lyxm9awTsFYGNppnj85s4Rne9VsdhAwctNV0XzSH_X-46gX-YlMEehafalnUScM_Z4Q895T3V31wXiw_fy7q9DookldafLKa-MMr9X1lQS2Exdbsa9XZM2P0kykpQFcH8OLAuLGz4KHWTjlviszDx4Owb8fMDZId1jxqQZVJFBw2zj1z5Q4KNY3Vmd1aSpqMkXZ0C4ePASR4NfOoS3B6xuSgNNUOHb2S2ZlMGjqZ1jPZE5LnImGr6LGRE4iurSDM9aiKaH37cvO8CnF7ygag5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💥
تنها یک پست از ترامپ امروز 1.3 تریلیون دلار به ارزش بازار سهام ایالات متحده اضافه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65889" target="_blank">📅 00:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65888">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐀𝐌𝐈𝐑 𝐌𝐀𝐒𝐎𝐔𝐃</strong></div>
<div class="tg-text">الان یعنی با قاتل
حضرت سید علی خامنه‌ای
💔
، قاتل خانواده‌ی رهبر جدیدمون
💔
قاتل سردار سلیمانی
💔
، قاتل سید مقاومت حسن نصرالله
💔
، قاتل شهید فقید اسماعیل هنیه
💔
، قاتل دانشمندمون محسن فخری‌زاده
💔
، قاتل سردار حسین سلامی
💔
، قاتل سردار محمد باقری غلامعلی رشید
💔
، قاتل سردار موشکیمون امیرعلی حاجی‌زاده
💔
، قاتل شهید فریدون عباسی
💔
، قاتل شهیپ محمدمهدی طهرانچی
💔
، قاتل سرلشکر شهید احمدرضا ذوالفقاری
💔
، قاتل سید امیرحسین فقهی
💔
، قاتل شهید اکبر مطلبی‌زاده
💔
، قاتل سردار سرافراز عزیزمون علی شمخانی
💔
، قاتل فرمانده بی‌بدیلمون محمد پاکپور
💔
، قاتل سرلشکر عبدالرحیم موسوی
💔
، قاتل سرتیپ عزیز نصیری‌زاده
💔
، قاتل عزیز اطلاعاتیمون اسماعیل خطیب
💔
، قاتل شهیدان غلامرضا سلیمانی
💔
و مجید خادمی
💔
، قاتل سردار سرافرازی که بر بستن تنگه اصرار داشت یعنی شهید علیرضا تنگسیری
💔
، قاتل رئیس جمهور آینده شهید بزرگوار علی لاریجانی
💔
، و قاتل شهیدان دیگر مانند محمد کاظمی
💔
، حسن محقق
💔
، داوود شیخیان
💔
، محمدباقر طاهرپور
💔
، بهنام رضایی
💔
، اسماعیل احمدی
💔
، علی‌محمد نائینی
💔
، مهدی رستمی شمستان
💔
، سعید برجی
💔
و منصور صفارپور
💔
توافق کردن؟</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65888" target="_blank">📅 00:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65887">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما به نقل از سخنگوی وزارت خارجه:
قطر و پاکستان به‌عنوان میانجی‌ها فعال هستند
وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمده متن نهایی شده بود اما آمریکایی ها مواضع خود را تغییر می دادند.
ایران ثابت کرده است که در آنچه را به عنوان خط قرمز معین کرده است مماشاتی ندارد.
مواردی که درباره توافق مطرح می‌شود گمانه‌زنی است و موضوعی نهایی نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65887" target="_blank">📅 23:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65886">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2pyPmL2nFr7kwE4M9YwNSn7ive-IsGSv1BQmKbaT5vpWIMSWel4wSaOaeG0sLG6uLhD8EYEnrr0T8ca2rH-Tg7T8r1ccefGXgNm6DhXTPu0MOYeL8ESko6RA-9C7fewQnHT52nQk09ZMwJipj0ZA4EgBvr40FFo7l8VutzxtkLuXZzpx0pozZvZt1vfrbX_jfNvWqW66WHi4CMRxniyXWcs9PDbNSX5EHpqL5ZuzaIjKRpHxdmKlvJhLgP8QTSR5YWKc-OHGLdGvnKkdXSVFUbQzrVRL3NLlZQhPpflQBa9NI08esWowpEjvE2r7hijhHkynqTMuHMsP9UQXswX3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
دفتر نتانیاهو:   رئیس جمهور ترامپ با نخست وزیر نتانیاهو در مورد نهایی شدن یادداشت تفاهم با ایران برای ورود به مذاکرات صحبت کرد. اگرچه اسرائیل طرف این یادداشت تفاهم نیست،نخست وزیر از تعهد رئیس جمهور ترامپ برای اطمینان از اینکه توافق نهایی که در پایان مذاکرات…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65886" target="_blank">📅 23:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65885">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:  رهبر جمهوری اسلامی با امضای یک توافق موافقت کرده.  @News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65885" target="_blank">📅 23:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65884">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
دفتر نتانیاهو:
رئیس جمهور ترامپ با نخست وزیر نتانیاهو در مورد نهایی شدن یادداشت تفاهم با ایران برای ورود به مذاکرات صحبت کرد.
اگرچه اسرائیل طرف این یادداشت تفاهم نیست،نخست وزیر از تعهد رئیس جمهور ترامپ برای اطمینان از اینکه توافق نهایی که در پایان مذاکرات شامل حذف مواد غنی شده،برچیدن زیرساخت‌های غنی سازی،محدودیت تولید و برد موشک و توقف حمایت ایران از گروه‌های تروریستی وابسته به آن در منطقه باشد، ابراز قدردانی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65884" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65883">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: بعد از توافق سریع محاصره رو بر می‌دارم
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65883" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65882">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
رهبر جمهوری اسلامی با امضای یک توافق موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65882" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
