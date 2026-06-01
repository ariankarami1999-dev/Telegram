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
<img src="https://cdn4.telesco.pe/file/ODlY8868Vc1bENeazxxYpXjdBdUGsMLwuS0XrzyVImHYtcj4yEkilP5ymy3ES7TdD9EHKzXC5N90Nx558M445Iu5uylHm4eI6QEFbyQWGnbtZhenF36IvwGZSKy08as9_sBKxlfCQjbdKY0zpb-EOQRnHFGPUAlJywFMwRZifCmewZ1IZYcmvWV6NYBiGTNoGCl07zgIZkY8UV72bEQY_0Za1STc8PX8n9Y4uL-_YuqfM-gk_q7yp-w8HGzWLyQrOkNXQ_ZVBSkwWFeFNij3xk6uC8xornvXh3zBlmNDL0Ite2CEfIqAlvj54hCtSveClKznu7LCOgb8drJVereXkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 917K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 19:19:40</div>
<hr>

<div class="tg-post" id="msg-124242">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری / هشدار قرارگاه مرکزی خاتم‌الانبیا به ساکنان اسرائیل
🔴
سرلشکر خلبان علی عبداللهی: نتانیاهو در ادامه شرارت های خود در منطقه، ضاحیه و بیروت را تهدید به بمباران نموده و برای ساکنان آن هشدار تخلیه اعلام کرده است.
🔴
با توجه به نقض مکرر آتش بس توسط رژیم، در…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/124242" target="_blank">📅 19:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124241">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogfwvVLnvILj6lBI-8I__uFYrIY1LyUn7YXP5pqcly0a46LwtO5yIAO48MeD2lU8cc2yPaOO9b7BVaUVEntGK8huCsjBdkWLHmfW8Sa2wJj3nl6-uCFhXHpvKY_fBHUYaqLAIzXlJjizUAMaMOuJlfZDm1qPlYsN_FTeNzwdE0eNqZ0jV2M80nPQAEeLKC8LuOqFWLrlvgiFnA788e_PRCJQGg3bm1Ttwp1c39aUCmuxZ4YYLnhIEK7qGVOvnsr2NxnN23zPBfBfhIeEKvq1gT2O5dXU70N5rvRPb4pl906OVa5ldGc62LP6f_vMkWugiJ3M4-WP13OUCJi8OrpH0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حساب سازمان اطلاعات سپاه: هرکه باد بکارد،طوفان درو می‌کند
🔴
ایران عبور از خط قرمزها در لبنان و غزه را به معنای جنگ مستقیم و تحمیل هزینه بر امنیت ملی خود ومقاومت اسلامی فرض کرده و متقابلا عزم خود را برای عملیات دفاعی با انجام اقدامات معناشکن و گشودن جبهه های جدید به علاوه حفظ معادله تنگه هرمز قرار می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/alonews/124241" target="_blank">📅 19:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124238">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2FsS0PC_am1gDcCuHevgal6L8H0qNh36dmBhXhqHj_MUFZAyG4PJQdnQlBnVO7nH5kxQ5di6UYtoBL7uPdwS6TdAvbe1Ty4UiUjukncdzuN2_nMYngBLnKPkjAQMvr_KEFLxb_Z0ruH2wTbLR5UAyBcE-bWCmzsleWuU2gg-lCfoviK8slp5Z7jO7rIULXzoEgERAHyl1aqiHFnZqU1s0DEclIZyQQ_B-vN5JfZb-0Hb1JQGuTiDzK1Lc9p25opLI5wJ5AdBS7KZ-mhIQ-VfvjgRAoKz0-sF0dmQBQ8hMxGWXt9XcJfsJufNRAPdP2dqiDzQFg7bWwga7Lhoe63LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZJpddt_RARqZ961NBwte8m9gyNORoskN_HglGuS-ydSolP87KVzu0IvOxE58EqbmxiHnngAFNfAYY7vwFBlj0lFHeMNZ70mAqKKpEA1-g6_uVG7Sly8Sym8TuNIEqY4XqmtmVmnngrcPUwhtAeqPC6BJN0jLpewAt3yQZrlAsGNRsXoTuBEJyIO4ILICtqZmi0sSLz0FlTV480B1g6O4bPmhmR6koFMLUJcwlo4FPG97do6mvZwxxbgrhgH8HPaDoiXeEklrja3DgEdpnBzpyzpd3RAwoqGxIs0joHEgKPO8agJdiunRspPdiwUwBiQvQgApvdUZlQGxurRvGrqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NrMhmouiV2_C4DN4yCkijT32l7t1R_9uTPJ73lIjJqT4o-1qMStwTkBoCJKxPymp_bRei3E-mpgOmoYCQlykiCJLtUYwOPQgcJMkbzO1A_ZfHBuZ1iJjOgPPSOl9W17rD4ehKxErtWSj7dZPNATtu3OYlP1ZQBvWVnq210ot2rinqIU5q09HWhgZLeUMMN1YOp9FhpnxGzHZ2vVF94elMlTjppSxo_P0Cmo67I_xYgiRkG4d9224x8n35hRyRTjm-L7pBWjMlOItjQaeBhxZCu5UFiEbPzmKy7dezAM_iw0-WJh0xnDHvEhmkBkvMpc82muyhkue_rExMHC8RrHUjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
صحنه‌های ای دیگر از حمله‌ی سهمگین اسرائیل به صور، جنوب لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/124238" target="_blank">📅 19:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124237">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوری / هشدار قرارگاه مرکزی خاتم‌الانبیا به ساکنان اسرائیل
🔴
سرلشکر خلبان علی عبداللهی: نتانیاهو در ادامه شرارت های خود در منطقه، ضاحیه و بیروت را تهدید به بمباران نموده و برای ساکنان آن هشدار تخلیه اعلام کرده است.
🔴
با توجه به نقض مکرر آتش بس توسط رژیم، در صورت عملی شدن این تهدید به ساکنان بخش های شمالی و شهرک های نظامی در سرزمین های اشغالی هشدار می‌دهیم اگر نمی‌خواهند آسیب ببینند منطقه را ترک نمایند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/124237" target="_blank">📅 19:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124236">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhNzcww8VbScBjySyq9zFPGwciHJntRiA3uEAK2U6yuhTf7l1BgNaYYnzk9NyRQvzY2h1Tzf0vaqdxSNai-1SC5tTXSstiEohDStRdudZbVS66gw9oyWQd1vs4BZ9M5IMk9PniaeXy_KSkD7HsfQ4QHmZ7MXHMIAw3P3qvb8tIdQPevFaCoX-w9JJLvPr_TACbieEOPqkzg_qyr3bNnGiLOJkDSYexseqnOmEpGmuBLvyq2dU1NwgFX-FpwNAK_OsiCW349gKHMbuMgKZJZnqC_IY4AXfBEGklgRLoX0pk76GIZQ5AZ_80yg4idSIBPQp_2dXnzSZnFYRdRJYfagfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی و کیفیت بالا
❤️
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
از رباتمونم میتونید تهیه کنید
💞
👇
✅
➡️
@Napsternetiran_bot
☑️
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
چنل کانالمون
👇
📣
➡️
@Napsternetvirani
☑️</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/124236" target="_blank">📅 19:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124235">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6269863c82.mp4?token=iYp5XBWzKk-AagXB4N6zLOEULhjmFwLGsrknTg-mudsn3kFyVn8QljkevksUhn0hej3JAtA0Vf3ttWsyjr1KBMHSimav04zfbXF40S11uBemQh2bxMuA9JuwprSlQjla0zrTuNsQVHnD4qyOjYNHHsfe3eEDEa5gzsC7JLX05Oj1I-NLIenRdO1sJ43YJiWPql7nYFmXDfQYxVkJ53QPMFOlw2KucNEaowniHsxaKlCZwzb45PL3CHsndgQk0aCjgyDTy0il5M8k8-t_xIkrAXMQunmbR-NnJfFA0w1O-MFpxTSiVCGacMhog1Vok0gA4YIMjT8lH5pnNg47ibL3rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6269863c82.mp4?token=iYp5XBWzKk-AagXB4N6zLOEULhjmFwLGsrknTg-mudsn3kFyVn8QljkevksUhn0hej3JAtA0Vf3ttWsyjr1KBMHSimav04zfbXF40S11uBemQh2bxMuA9JuwprSlQjla0zrTuNsQVHnD4qyOjYNHHsfe3eEDEa5gzsC7JLX05Oj1I-NLIenRdO1sJ43YJiWPql7nYFmXDfQYxVkJ53QPMFOlw2KucNEaowniHsxaKlCZwzb45PL3CHsndgQk0aCjgyDTy0il5M8k8-t_xIkrAXMQunmbR-NnJfFA0w1O-MFpxTSiVCGacMhog1Vok0gA4YIMjT8lH5pnNg47ibL3rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک حمله هوایی سهمگین اسرائیلی چند لحظه پیش در صور، جنوب لبنان، انجام شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/124235" target="_blank">📅 18:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124234">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZdiaHEbzoaHqT5Whr_BdjYRpHFccHEBQkVq9eM1s_PmZYF8w05Czxpx0I0bOqREaYU-koX4JcULEry9XiT2hGTaWihZ2NH4682NK-OOsttFv-4prsjjx46GFhyxFvb5JxlJK5P-DIIv1jj7Zg9jvSQ67cHujv6mxX6kDh6K4KKa0MwAiRfxlSdS3JJwldDclczWeT_OUyy2Zr8FzUUtkGeTA5lXyXt-TvS1-NvFmn9oexicKXI6uiTb8mfkncKc9csQrHGNcz9LximpU_kCjhXIT75w4J23FAxlADtB2hJaDrSBFzC7UAkOaNmuvhKEb-uzWWVR_5wEOkVKqoLsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از حملات در روز های میانی جنگ به پایگاه چهارم شکاری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/124234" target="_blank">📅 18:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124233">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای امور خارجه ایران و فرانسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/124233" target="_blank">📅 18:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124232">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی در بیانیه‌ای اعلام کرد که شورای حکام این آژانس به درخواست مصر، اردن، مراکش و عربستان سعودی در پی حمله به نیروگاه هسته‌ای براکه در امارات متحده عربی، در تاریخ ۵ ژوئن جلسه فوری و اضطراری برگزار خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/124232" target="_blank">📅 18:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124231">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWxByMJbzStwxcfzbL7VNDV2xDwq33ZZq3QnPPvbo0UbYFpor3qtbG95eknSaChOc4h5bUQ67a-LQ6J0dqGwnssCaitR-rhyb0UlXWGBhijnPiFFo5jGZD4JgjIOsV5e8Dbl4F8Ykm8qWC_-rGE-efGmA5-CPgrVA8mi-dKK725NSEUJkh3t13aSzOykNYTeejXE8BCl7hwhad8CnOvgmdSoPCgqQ-AXreDd1znamf6o--dMi05CUs8kVRxZKsRt2me40VN_l9ekejT6r-fNkxU5EWeAONOvu26Yaoffq2-En_hDv9b0ANfx7rxHwccLGkS8CoUKfu-b7RlSYF34LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایزدخواه، نماینده مجلس: راه قدس از ابوظبی می‌گذرد به امارات حمله زمینی کنیم
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/124231" target="_blank">📅 18:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124230">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzmk1v2QP_O9rRa596kiR2P8QvWQelPCkHUDT1XbgBPmqn7JHa8RTSg9xBKxatiK2dYTLI7sNVXIN7ZbA4W2weC3cuyMlRZPXm3nS4wKOj_MMV5g_6xE7wFoAntCfFEjHdOCG2G5A8HGijH3E_Fb4jDKGMGTDoKonR855vjBP7N2NY8PWOQsuU8pyc-w9JOwAdj5Sx8nvthJRpj3ZjnKDsq0h1bNSyZHI2HNH_FraxMl_b05XodtjMiUIiUCOlJPhHhtVrxvaXNaBVDZJLX3IXYol9sKg7h9XUznt_YRafcRFhVlqmjbIGcraj1UZbproWNDqbR_lo3SEE-4_DRcvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در بنگاه شرط‌بندی مشهور آمریکا (Kalshi)، شانس بازگشت ترافیک دریایی تنگه هرمز به وضعیت نرمال تا 1 آگوست (11 مرداد)، به کمتر از 40% رسیده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/124230" target="_blank">📅 18:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124229">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEROR0_RoTkcwRzD4rz5dUljanzLlAvJQgt1IVM-REH2o2Anl0gU5ZMVKutV3at8doXd_QcVPQfL7lAf668ul0nSSb5RfE_YixaajKjwv38ui0Jt8Y3pKUBeOEp2zEbbf1j3zkTpddotN0w6irKR1yepkOoEOtiacOVPoJlBuLrT0wE4CEoiI6ZW-Kiht4FsBMoCSoDFAJV8ypuPGt9Gp-J--LMQ-gWne6nQXsY1rNn96a7jhuGXLw3-rzwcfvt5OROnzYMl_NEykGDn42TXUSqNXb8-hMg8CcvPfN84Z0GuYYgBDiY5ElpSnG5FROMmcZ4NvXGPvXtuQCK4xNVYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت 97 دلار ، نفت آمریکا 94 دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124229" target="_blank">📅 18:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124228">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63c6a5299.mp4?token=oNTwIfnT3XNcSFD8ixkW4FMcLRcfz7ZouJy3alHGrwdaPHzULiEkv85Td3Xb99ON4XpwYy-ATEbcv8Y1zzF9nxG60vKanFISA2g2_mkkWHuLhb17BK9-o6tx6X-qe6a1HTytJNuWNm3MSJe-TGJlI-vsUEKIxtSgpjnnhpBUk74gEgdCDhOOCIyTrZmvNLXZNlxtU7bxV6ZahDyqAwZjNuiyP9i_WtQ8CrLWVr11Eil4imJRinuFxwwUxMSzIV_5V_X_jk1uaMRGOtNPnrRHJXVtOooMisXzfGzXqekBY6Vq1krK4IXcXiMCz_oFMYB3AkDviAonlPBZclA1qGptbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63c6a5299.mp4?token=oNTwIfnT3XNcSFD8ixkW4FMcLRcfz7ZouJy3alHGrwdaPHzULiEkv85Td3Xb99ON4XpwYy-ATEbcv8Y1zzF9nxG60vKanFISA2g2_mkkWHuLhb17BK9-o6tx6X-qe6a1HTytJNuWNm3MSJe-TGJlI-vsUEKIxtSgpjnnhpBUk74gEgdCDhOOCIyTrZmvNLXZNlxtU7bxV6ZahDyqAwZjNuiyP9i_WtQ8CrLWVr11Eil4imJRinuFxwwUxMSzIV_5V_X_jk1uaMRGOtNPnrRHJXVtOooMisXzfGzXqekBY6Vq1krK4IXcXiMCz_oFMYB3AkDviAonlPBZclA1qGptbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دارایی اسرائیل، بزالل سموتریچ در نیویورک: دولت اسرائیل خانه تمام مردم یهود است.
🔴
امنیت یهودیان در اینجا نیز به قدرت و امنیت دولت اسرائیل بستگی دارد. اما بدون شک، هیچ جای بهتری برای زندگی وجود ندارد.
🔴
یادآوری می‌کنم که ما اکنون به مهاجران جدیدی که امسال به اسرائیل می‌آیند، پنج سال معافیت کامل مالیاتی می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/124228" target="_blank">📅 18:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124227">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204ea63704.mp4?token=iVG8I4_oNlX5_eaSBA0ZQsVfBcF1OeB7GtLIgRrYNzf87sNr1aDfDhbN5UMGijtCQJK5L5MjwFZ9Mjb5gYDTFFsc1ZfTfs69BKYZn-6aCE3YswTCA5QpFzOOGpkby6eGZKfYBW9J7ck9T7SnP6xbX8U21y1zLLlZ6qEsZFGaW7gmqY_RFcOcDgOXzN2tvuPyB7NvszQA1f6gc-QcYVwupqN2Ndddr3PzdyrPKc2bZRIB8HWok4BGlKMOnBv6FxK0Vjsmn66bDIQXR6PnQx33romluELTQOEW2MKyZoTSKYxLg43c6JLy59dCFXOtFCC2FKXR8NbuywYUupSJZ8zWgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204ea63704.mp4?token=iVG8I4_oNlX5_eaSBA0ZQsVfBcF1OeB7GtLIgRrYNzf87sNr1aDfDhbN5UMGijtCQJK5L5MjwFZ9Mjb5gYDTFFsc1ZfTfs69BKYZn-6aCE3YswTCA5QpFzOOGpkby6eGZKfYBW9J7ck9T7SnP6xbX8U21y1zLLlZ6qEsZFGaW7gmqY_RFcOcDgOXzN2tvuPyB7NvszQA1f6gc-QcYVwupqN2Ndddr3PzdyrPKc2bZRIB8HWok4BGlKMOnBv6FxK0Vjsmn66bDIQXR6PnQx33romluELTQOEW2MKyZoTSKYxLg43c6JLy59dCFXOtFCC2FKXR8NbuywYUupSJZ8zWgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دارایی اسرائیل بزالل سموتریچ در نیویورک: مردم ما پیش از این بسیاری از مامدانی‌ها را پشت سر گذاشته‌اند و اکنون نیز از پس آن‌ها برخواهند آمد.
🔴
در نهایت، انتخاب مامدانی، مانند هر کس دیگری، این است که در کدام سوی تاریخ می‌خواهد باشد.
🔴
اما تاریخ یک سوی درست و یک سوی نادرست دارد و این موضوع در طول سال‌ها آشکار بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/124227" target="_blank">📅 18:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124226">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b099e3a6a7.mp4?token=hGTiMrYVYhFx--pBPEytVn1V74wMNyIdEMcUJMLRA2IBNdnCo9kYdMufM5rLDp-ca9OKQXaIXAgP0iX8jNz5Gmon0W0JMTf5h30WKoVSaPMEs54Vj1Q4tLh57fcdQ_FrgXEuobArCST367Bw-tbykFfDSDrzqvCsGDxl_9YkeZS2G1GuHWjPyvKZuUhU4JCdqfUAeKfNi-h6cSzA44f6vwOU6LBgCgR2so1ARaBuXHfQZz99KUBYugZNXRuv_2r72riqnV_5dcD9zTXsPJqS3KS8v3C-UZPrSMyS_pTf20uCSxJMvgJceLLu55HULbf-BJ-uLIb4Q4bQ4fhIw9NXmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b099e3a6a7.mp4?token=hGTiMrYVYhFx--pBPEytVn1V74wMNyIdEMcUJMLRA2IBNdnCo9kYdMufM5rLDp-ca9OKQXaIXAgP0iX8jNz5Gmon0W0JMTf5h30WKoVSaPMEs54Vj1Q4tLh57fcdQ_FrgXEuobArCST367Bw-tbykFfDSDrzqvCsGDxl_9YkeZS2G1GuHWjPyvKZuUhU4JCdqfUAeKfNi-h6cSzA44f6vwOU6LBgCgR2so1ARaBuXHfQZz99KUBYugZNXRuv_2r72riqnV_5dcD9zTXsPJqS3KS8v3C-UZPrSMyS_pTf20uCSxJMvgJceLLu55HULbf-BJ-uLIb4Q4bQ4fhIw9NXmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ملخ‌ها به مشهد حمله کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/124226" target="_blank">📅 18:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124225">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRS6CxW3nEpBK4KxBejW-i-lj9kjlE17HwFRsWkn5ZZqErMLuxbiDSja_gkHGmhijjYP945oLvmLgXWuuSVvVIjTPv8fVIVzfEpDNSUurJVAObVThLI7SvpQjnUExQCItEt0uAFGkOBk2yemkFH-nZkWjXXvn_0Td3eM3v8UM-mk43c3KUcbtYl_fe3wI_CwmMk9n1TPwAZDIHzpIJzmtERKJ04pRuOPjzuPwVLROtjl3DpqEtvyLKAXO724o2GiQlKqxkgJxwPe3kTarIXYhy5mx0zgRGLJQBnK25Ykw7L-eFgJCAj8Xe2DhE-7kqqzWEjg8u-CsUgnFDLyrZelsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت دفاع بریتانیا می‌گوید یک پرسنل ارتش بریتانیا دیروز در یک حادثه آموزشی در شمال عراق کشته شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/124225" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124224">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزارت کشور کویت: به ساکنان خود هشدار می‌دهیم که در انتظار حمله قریب‌الوقوع ایران در مکان‌های امن بمانند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/124224" target="_blank">📅 18:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124223">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKFO4-xeWI5KKOS7AkCkRd69FEaofB115xu3Bun6Q08aWNlipRT69bY1M3oJHffDwkX6rnHNY6rZQ_VtZaJnZIhTtjhF64Tu2wkDnpAS2-qEm9fS5sCznf2kxy49mgx2cO5REEH6iYO-TKbO5NYcfEh0la2-1uqh3moNe-Slhs0HTGWul1okHBkQMrNyQzf7UCXkVnbaWTq0ERq-7SPVItDZITyhO5DRfYbqXff-8pNwVXwBcVWsNtqqU-_Sn_wcljNw77yRDdbWJ0Lzl1TM8lEbcWCyG6r1VfUL2wryb-5lfXOWqImYWKlz2f1yYtZPDjoCdD_xwzwDhU4GAc79Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارش می‌دهد که یک کشتی باری که در خلیج فارس در حال عبور بوده، در ۴۰ مایل دریایی جنوب شرقی ام قصر عراق مورد حمله قرار گرفته است.
🔴
«یک انفجار بزرگ» پس از اصابت یک پرتابه ناشناخته به سمت راست کشتی رخ داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/124223" target="_blank">📅 18:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124222">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
بقایی: آتش بس در لبنان بخش لاینفک هرگونه توافق و خاتمه جنگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/124222" target="_blank">📅 17:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124221">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
اتحادیه اروپا از اسرائیل می‌خواهد «تشدید نظامی در لبنان را متوقف کند»
🔴
اتحادیه اروپا به کشورهایی پیوسته است که از اسرائیل خواسته‌اند حملات گسترده‌اش در لبنان را متوقف کند، پس از آنکه نتانیاهو گفت دستور حملات بیشتری را در حومه جنوبی بیروت صادر کرده است.
🔴
سخنگوی اتحادیه اروپا، انور العانونی، گفت: «ما از اسرائیل می‌خواهیم تشدید نظامی در لبنان را متوقف کند و به حاکمیت و تمامیت ارضی لبنان احترام بگذارد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124221" target="_blank">📅 17:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124220">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
قطر و سوئیس در مورد حمایت از میانجیگری پاکستان رایزنی کردند
🔴
وزارت امور خارجه قطر اعلام کرد که شیخ محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر امور خارجه، تماسی تلفنی از ایگناسیو کاسیس، وزیر خارجه سوئیس دریافت کرد و در مورد میانجیگری پاکستان بین ایالات متحده و ایران رایزنی کردند.
🔴
به گفته وزارت خارجه قطر، این تماس به هماهنگی تلاش‌ها در حمایت از میانجیگری اختصاص داشت که به تقویت امنیت و ثبات در منطقه کمک می‌کند.
🔴
وزیر خارجه قطر در این تماس بر ضرورت همکاری همه طرف‌ها با تلاش‌های میانجیگری جاری تأکید کرد که زمینه را برای رسیدگی به ریشه‌های بحران از طریق گفتگو و روش‌های مسالمت‌آمیز باز کرده و منجر به توافقی پایدار می‌شود که از تجدید تنش جلوگیری کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124220" target="_blank">📅 17:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124219">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ارتش اسرائیل(IDF): گزارش اولیه - صدای آژیر در مناطق مارجالیوت و کريات شمونا شنیده شد. جزئیات در حال بررسی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/124219" target="_blank">📅 17:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124218">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ارتش اسرائیل(IDF) هشدارهای تخلیه برای حومه‌های جنوبی بیروت (دیهیه) صادر کرده‌اند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/124218" target="_blank">📅 17:48 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124217">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سرگئی ریابکوف، معاون وزیر خارجه روسیه: روسیه در حال مذاکره با ایالات متحده در مورد مسائل مربوط به کوبا است.
🔴
امیدواریم که توافق احتمالی بین ایالات متحده و ایران قابل اجرا و کارآمد باشد.
🔴
روسیه آمادگی کامل خود را برای ارائه کمک‌های عملی به توافق‌های احتمالی بین آمریکا و ایران حفظ کرده است.
🔴
آمریکا و ایران باید از تشدید اوضاع و ورود مجدد به چرخه رویارویی نظامی جلوگیری کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/124217" target="_blank">📅 17:48 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124216">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
افزایش شدید نفت برنت ادامه دارد: عبور از ۹۷ دلار!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/124216" target="_blank">📅 17:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124215">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
تجمع فعلی هواپیماهای آمریکایی در فرودگاه بن گوریون در تل‌آویو، اسرائیل.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/124215" target="_blank">📅 17:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124214">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ce339cc1.mp4?token=gj_dWBqEvsxcKLEVfhD21wqUBJzB7tuhW3-7ManOKDoW7fCXVaogBDJjkiZhrZBjtHYosIHZ4D4HhcZCVh5TBGh9B1UmIICm_AoqZmG3CrfKBy9cd_Jji-Swu39gWTtl0FVXo4Lkqqwtjid2ygmojoXBBm8SxrDNHlq8hFkZXRp5q_IzfoX8-Wa-_Oev82yRzq3Z4d16klV-vJgP1GzcwHjcaVxMDimk1AgycpV099lxA1FD6a4TG4CZs9vwBNXNSTNfW-9dJOEf5k__-HeyR_vG9m2yoD2DO8QL73HOBOXN6nhMCwa34f2skWWvvBpNFrfY95Q66ReY6hqENt9IiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ce339cc1.mp4?token=gj_dWBqEvsxcKLEVfhD21wqUBJzB7tuhW3-7ManOKDoW7fCXVaogBDJjkiZhrZBjtHYosIHZ4D4HhcZCVh5TBGh9B1UmIICm_AoqZmG3CrfKBy9cd_Jji-Swu39gWTtl0FVXo4Lkqqwtjid2ygmojoXBBm8SxrDNHlq8hFkZXRp5q_IzfoX8-Wa-_Oev82yRzq3Z4d16klV-vJgP1GzcwHjcaVxMDimk1AgycpV099lxA1FD6a4TG4CZs9vwBNXNSTNfW-9dJOEf5k__-HeyR_vG9m2yoD2DO8QL73HOBOXN6nhMCwa34f2skWWvvBpNFrfY95Q66ReY6hqENt9IiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله فیلمی منتشر کرد که نشان می‌دهد یک پهپاد FPV دیروز یک سرباز ارتش اسرائیل را در حوالی قلعه بوفورت در جنوب لبنان هدف قرار داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/124214" target="_blank">📅 17:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124213">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DY6otX117OOl9Wx7pA2JSXMP1muhJkSG2Uq5gfz8NZv_4MAC3qZNvH6Sy4foXhdZwRGLSpPWpvFeuhClWlAVqCx8eqdGq2SnL_gsmkG4JAHvTknBk8sOw4z_8sTu9hwYU2qDRBCHm3K77ivoRnvq7rX6J26Ookv6WG2LbIha9qDlo_ipox7v6OvbmkrJGW77bhabuTL7UOScUYeGvBUdxT2ftqB3pWuPHyP_S8DwihD9Yt-7oORwyJsgokPPQ87hOravTMc2gKhFFewetSXnku0G23xhFjV62VXojBpbjmAu602_R3_JbxS2GNfvUudfR1paP7lZ11sh25-hlVtCnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت آمریکا بیش از ۸٪ افزایش یافت و به ۹۴ دلار در هر بشکه رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/124213" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124212">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kqmv3vdb4r-jY4i3GmXzzeZG7yc2lSXFVojjddKEFcYZ052U_CUH_jNZLhsZ-dn4OmmkkEmV7pr_U49VDYSpwATZ8P7Hlf2D21Ghg0BdTIBpgJT02faMQO4Q_Z6n_c6ToOpT6yiIhqW164EQzyr8sbvyUt7l54zUX1-_u_tqe2HnEM9DkYF5kvfNgNvp2eSldp_vG6G43kFqyslqgR4D4t9Wfb6j0h_ewI8G5P69ED6Xtjptfu-KQlAYXismM00x7jOBxhCTJdg_IqmVoKpWw2T41ct2S2fst1-g2cgpbxWYqdAwCCrkqTC_SlvoLlKWclst4HouJeTlQ-xD6xsKnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق تحقیقات جدید، سینگل بودن خطر مرگ رو ۲ برابر افزایش میده!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/124212" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124211">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/053fd72894.mp4?token=n856jbPubwQB2JENtwrt_7v39yQyFq50H15_D5GNUU8jNFk6dFbmIzhEXSd_R5qEEQM1SCGCBBNvpzvCw0BKB09nOSmgmD9PN8BJ32fErZQ9vbuJk67a0W95eqnzHEdRQ-tqWCCzK7PjGCl-7dHlCKvcZJkdriw4uo4SpLu12osvDnpNlJ8T72_KljLQn8bX-bYkexLvumMqyGZOZpVnQmGqtp8WvShtPEyHB1F0GdFiuB3URaxIk6-w9ekHf8vsf4_nQdBBj2DI3rbEccPEdOSKwCDDGi7X5F0a7SABvnMICNbQrszQvXTZymk3soXyBIovgZ4IPTUz1nrBOarrAI8JNf1aR2SwuEEyvJWK6RqxAX0SAvVYB9atFeZ4sjltxuwBT5NSxPP7415DZc7TVlYKgR3EELT9VODTiS_7O9a9L1fetdZQHpMxucG9dJnX8LroKHG4XIrLPlVPgKn_PdaVR1HBB6hsabMhselWCNtpih8zIQcBg8KnsLDsXklOhmd595027WVlP8x0dOsCIBkTT-XMzv4stAmnyk1sZkIY0JoXEP_VFs237w9v4sXg4fQmHfzyC69IVGVnsPMvzVxGJyWWgEDpReAjNIkcb1_N3POg0QTrdezMSt7Tcybr4hDNnUBz2bwvoCUyc1Bp7w1pOQoWS3ZjqJi8bcwfISQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/053fd72894.mp4?token=n856jbPubwQB2JENtwrt_7v39yQyFq50H15_D5GNUU8jNFk6dFbmIzhEXSd_R5qEEQM1SCGCBBNvpzvCw0BKB09nOSmgmD9PN8BJ32fErZQ9vbuJk67a0W95eqnzHEdRQ-tqWCCzK7PjGCl-7dHlCKvcZJkdriw4uo4SpLu12osvDnpNlJ8T72_KljLQn8bX-bYkexLvumMqyGZOZpVnQmGqtp8WvShtPEyHB1F0GdFiuB3URaxIk6-w9ekHf8vsf4_nQdBBj2DI3rbEccPEdOSKwCDDGi7X5F0a7SABvnMICNbQrszQvXTZymk3soXyBIovgZ4IPTUz1nrBOarrAI8JNf1aR2SwuEEyvJWK6RqxAX0SAvVYB9atFeZ4sjltxuwBT5NSxPP7415DZc7TVlYKgR3EELT9VODTiS_7O9a9L1fetdZQHpMxucG9dJnX8LroKHG4XIrLPlVPgKn_PdaVR1HBB6hsabMhselWCNtpih8zIQcBg8KnsLDsXklOhmd595027WVlP8x0dOsCIBkTT-XMzv4stAmnyk1sZkIY0JoXEP_VFs237w9v4sXg4fQmHfzyC69IVGVnsPMvzVxGJyWWgEDpReAjNIkcb1_N3POg0QTrdezMSt7Tcybr4hDNnUBz2bwvoCUyc1Bp7w1pOQoWS3ZjqJi8bcwfISQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام ۱۴ ساله امیرمحمد شاه کرمی
🤔
عرزشی های حرام زاده شیطان پیش شما باید درس پس بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/124211" target="_blank">📅 17:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124210">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
آجرلو، عضو تیم مذاکره‌کننده: ایران هنوز پاسخی به پیشنهاد جدید آمریکا نداده است / در کمیته ۶ نفره و شورای عالی امنیت ملی در حال بررسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/124210" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124209">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ارتش اسرائیل(IDF) هشدارهای تخلیه برای حومه‌های جنوبی بیروت (دیهیه) صادر کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/124209" target="_blank">📅 17:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124208">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سه موشک که حزب‌الله به منطقه کارمیل در شمال اسرائیل شلیک کرده بود، کمی پیش توسط ارتش اسرائیل رهگیری شدند و طبق گزارش‌ها هیچ آسیبی وارد نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/124208" target="_blank">📅 17:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124207">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WABKTyf8CVe6jBDz9kn7E7xY91RIKW7ctcS18Xu8_rOEQ3_VULQMsADWuMkB_4xHMPUnYyycpO3VjtzKNwoWtuQUz-azPMG0rXjBdRgKt0doHGAv3NASfPXOUFyvujhrVYOiQaE56bvJFPhOI2XMdpIl4v5kq8h0J-Z2ErNXPF-YnUvG-gRStU4UiNko8yQjqVrEonn3tRbFPwuJBw53V44_nkvFNK3tlOBporp4tOLrJIZw5n2EqVNmLIXLi24OcvHLvEzZlXHkGHTcO6kZyM6udBaExF8BJpwpnUFyy-a0QECcX53VJUNLhZlsfjfLq7Pr43GkjHEGDL2NiaX_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت همینجوری داره میبره بالا !
🔴
نفت از ۹۲ دلار رسید به ۹۵ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124207" target="_blank">📅 17:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124206">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQrbScdulN48l0LNMO7IeiJ-s4J_C0regL2_oCDFnB2DC0SMfUH6bhYClP0GGpzad46iMsyTDTf4eORP16nVPpFXhPuNqA6K46x6M4ZYZh_t0COiRc1IVTnxbchPtuHRagaoJE-ggCLnb56aUoTJk5lKzBFckVk34Rm607Jk3py_X5m0IhyNay675rtW3xPBBSattzqQMw6SgGOxyyfyzGC_xVtFdwFOx7dOjNBwkO4K0G4LINclFoXDh8h0mrtcO2K0jAy2rHsGgyKZ2A_N96_CQ_FUDT2WEunVo_ehfrS8PgumqWojI5koxCDkV-L9c0UlDq6lTU0aSQn_A9m6gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ادعای  ایران اینتل واچ : ظرف چند ساعت آینده، حمله گسترده ای علیه اسرائیل بخاطر نقض آتش بس توسط جمهوری اسلامی ایران انجام میشه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124206" target="_blank">📅 17:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124205">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ادعای اکسیوس: یک مقام آمریکایی گفت که مارکو روبیو، وزیر امور خارجه آمریکا، در ۴۸ ساعت گذشته با جوزف عون، رئیس‌جمهور لبنان، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرده تا ابتکار عمل جدیدی برای آتش‌بس پیش ببرد
🔴
این مقام آمریکایی گفت که ابتکار عمل جدید در چارچوب مذاکرات جاری بین اسرائیل و لبنان مطرح شده است
🔴
به گفته این مقام آمریکایی، برای پیشبرد این مذاکرات، ایالات متحده پیشنهاد داده که به عنوان گام نخست، حزب‌الله به تمام حملات خود علیه اسرائیل پایان دهد. در مقابل، اسرائیل از تشدید تنش در بیروت خودداری کند.
🔴
به گفته این مقام آمریکایی، این کار «فضایی برای کاهش تدریجی تنش و برقراری مؤثر آتش‌بس ایجاد می‌کند.»
🔴
این مقام آمریکایی گفت که رئیس‌جمهور عون تلاش کرد این پیشنهاد را پیش ببرد و توافق را تضمین کند. اما مدعی شد که پاسخ نبیه بری، رئیس پارلمان لبنان، طفره‌آمیز و ناامیدکننده بود.
🔴
این مقام آمریکایی گفت: بری گفت که تعهد حزب‌الله به آتش‌بس را تضمین می‌کند، اما اسراییل اول آتش‌بس را برقرار کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/124205" target="_blank">📅 17:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124204">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
طبق منابع العربیه، یک نفتکش بزرگ با پرچم پاناما در حین فعالیت در آب‌های سرزمینی عراق در معرض انفجار قرار گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/124204" target="_blank">📅 17:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124203">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
شبکه ۱۵ اسرائیل :  ایران موضوع غزه رو هم وارد مذاکرات و هر توافق احتمالی با آمریکا کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124203" target="_blank">📅 17:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124202">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gtpKHJV3bJaYZ634aa22SREpPQM5FHecqKa7VTOKF6oyKNSOWHHBO8s-3cItKec9ltR5YxCln-EMqSukKxjLzMKbxGWj1HFR7WOWC2EEF6CCbVxuvLmGf2MxflYBn78Sj-m3vCM_vENzCxr-miVh6N9LktE8r90QmQHN1OkpdYRlm2MXOcLRPKCgne7aGYy96bPnLAoyrD9b38OCmnyp16x6WnyG3vNei4ZDn-VDi2INpvM7Ck3pQmVlAZu8IZwqJmTOR48Y1fStuv0yWpR3_8D2Jwd2sPtYw9TyZKxehAJv-aTMCHV9UqzRJXrIuseNLKfCdli42i2xIbKF-DTbWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا و سیما نزدیک نیم ساعته داره در مورد اینکه حملات اسرائیل به لبنان غیرقابل تحمله و باعث نقض آتش بس شده زیرنویس می‌کنه!
🔴
خبری در راهه؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/124202" target="_blank">📅 17:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124201">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
مقام ارشد ایرانی به خبرگزاری فارس : خون یه فلسطینی برای ما هم‌ارزش خون یه ایرانیه!
🔴
همون‌طور که خون یه لبنانی هم با خون یه ایرانی فرقی نداره، ما همه جزو یه امت هستیم و تو این نبرد کنار هم ایستادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124201" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124200">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
جمهوری اسلامی در واکنش به بسته بودن تنگه هرمز گفت: برای لغو انسداد تنگه هرمز لطفا عدد ۱۱ را کامنت کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124200" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124199">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ارتش اسرائیل : داریم توانایی‌های حزب‌الله رو یکی‌یکی از بین می‌بریم و این روند ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124199" target="_blank">📅 17:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124198">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
هم اکنون ، نفت برنت: ۹۳.۸ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124198" target="_blank">📅 17:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124197">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqZliIT6SJY8-flK53dwVCT094UoOCCFoWmvaliTq-kJU4wqvc2Ta4WRRN_kXNpWmKi6GVFUUA6VN1WwhwDRGZxb2cvPF-MzeNUcaqNKOcF1wbr8_wgq3FXjeBpcKhxCzhfioQdXA84G8DeLOPED79Eke1MV0S9MwNR2hC4y62V6VgIPNfC8ZEhcn1XEyBiBhgOcjY5kOIC4iinc9zDjN37Izbulc_PzE14l6czlnRj0SDQ6qVSB9EOeGvAqY5aG30te3df_10KjCRa02jcZUlYtkckGBY5-yBGtgbeUJVzkR2rpvO72wu7beRt9yXFz9vWGDoSyHULLvmy7wcE2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت ترمینال‌های نفتی خلیج فارس
🔴
عربستان داره با دریای سرخ، تنگه هرمز را دور می‌زند و امارات با بندر فجیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124197" target="_blank">📅 16:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124196">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
یه تن ماهی خریدم ۵۴۰/۰۰۰ تومن فک کنم توش پری دریایی باشه، منتظرم برم خونه درشو باز کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124196" target="_blank">📅 16:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124195">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
کانال ۱۲ عبری: دادگاه عالی اسرائیل به اختلافات پایان داد و به‌طور نهایی انتصاب "رومان گوفمن" را به عنوان رئیس آینده سازمان موساد تصویب کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124195" target="_blank">📅 16:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124194">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
تسنیم: ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند/ عزم نیروهای مسلح ایران و تمام محورهای جبهه مقاومت برای واکنش به جنایات صهیونیستها و گشودن جبهه‌های جدید
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/124194" target="_blank">📅 16:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124193">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
تسنیم: ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند/ عزم نیروهای مسلح ایران و تمام محورهای جبهه مقاومت برای واکنش به جنایات صهیونیستها و گشودن جبهه‌های جدید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124193" target="_blank">📅 16:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124191">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHIKf9tAuVhX5toLcL0MhqHO-N863466NxuNtWNOrNPfLlZTatE_s79x699OjhBfX_xO2BiAV7R9rBtr8leMHsHYpCpbppd8HlgD8-7K-q5Beo7SOYwppU7ICa0dPkud4FtIEyf2Dj5GIYzGa_OFN5s8ufDDsSJlvFSIVRIYaau0DAcz80DvcC8H7DOAc2iTJkOr-70ZbiABJW5gy7O5K6ZTQmeeLoYiLRVA3meW7mcAoC2023YguAUGeIzdHQVbDyNKx0q1Bzv49E-PpdC2RllwJysmb6LuKIXkeXraT0S2jwizl0YsyS4UunVWuhkhsreJdQetT6HtZxVCZfPr4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش فاکس‌نیوز از آخرین مطالبات ترامپ از ایران
🔴
ایران باید بپذیرد که هرگز سلاح هسته‌ای یا بمب نخواهد داشت.
🔴
اورانیوم‌های غنی شده توسط ایالات متحده شناسایی و نابود خواهد شد.
🔴
تنگه هرمز باید فوراً و بدون دریافت عوارض باز شود.
🔴
ایران باید همه مین‌های دریایی را جمع‌آوری یا منفجر کند.
🔴
محاصره دریایی ایالات متحده برداشته خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124191" target="_blank">📅 16:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124190">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⭕️
لازم دیدم یک مسئله مهم را برای همه توضیح بدهم.
🔴
دقت کنید؛ در ۱۸ و ۱۹ دی، مردم معترض که به دنبال آزادی، رفاه و زندگی با عزت بودند، توسط حکومت قاتل به کمک حرام زاده ها عرزشی قتل عام شدند، نه توسط یک کشور خارجی.
🔴
تا زمانی که این مسئله برای همگان کاملاً روشن نشود و تکلیف با حکومت ظالم مشخص نگردد، انتظار نداشته باشید که وارد بحث شویم که در جنگ چه اتفاقی افتاده است.
🔴
در جنگ، وظیفه حکومت است که از مردم دفاع کند. سال‌ها پول نفت، مالیات و منابع این کشور را دریافت کرده‌اند تا از مردم حمایت کنند؛ نه اینکه مردم را سپر دفاع و بلا خود کنند. اگر آسمان کشور را نمی‌توانند مدیریت کنند از بی عرضگی آنهاست.
🤔
تفاوت این دو موضوع را باید درست فهمید. سپس از جنگ و وطن سخن بگید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124190" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124189">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bj7yI0DztgSRdF-bGrqsmot8n4fVDIePw3InE7UKEU3NN6NaoKv6ON1_N0B2Bsxaps0yFuUveSmoB2-kTxtP6dS1KNP4Q4vlwhSfBqMymbEU4piMflV5m5ZPxA0tLS5Xhf0IgkHNxSb7uL06t4Q4KtS8PA6aQZgTvyN4WaAnyu2gahVxK1RSFPQQGqOLwZxigYXAZA-mxjuRknkxXX75wA4H8wHInNMUo4YEcYHigtt0h_IixF9tHXN0HDYhmm9BjubgvREu0nMibHbMF9bvM_RnOLKEZYWFGSc_CZLu48W2vtKgr1FV4vNN-DvNSLZAj53Yu1E6qW5uzeSdhZH8PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات سنگین به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124189" target="_blank">📅 16:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124188">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران:
وضعیت در لبنان ممکن است مسئلهٔ برقراری آتش‌بس بین تهران و واشنگتن را به نقطهٔ اول خود بازگرداند.
🔴
نشانه‌ها حاکی از آن است که واسطه‌ها به سختی تلاش می‌کنند تا واشنگتن را به توقف عملیات‌های اسرائیل در لبنان ترغیب کنند، و زمان زیادی هم در اختیار ندارند.
🔴
پروندهٔ لبنان اکنون مسیری است یا به سوی توافق، یا شاید به سوی جنگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124188" target="_blank">📅 16:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124187">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نیکزاد، نایب رئیس مجلس:
رهبری اگر مصلحت بدانند، می‌توانیم جلسه علنی را با تعدادی از نمایندگان در صحن و سایرین به صورت مجازی برگزار کنیم
🔴
بنا بر مصوبه شورای عالی امنیت ملی، تجمع یک جای مجلس پذیرفتنی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124187" target="_blank">📅 16:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124186">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b35NEDgZ7A7ZodEtE65c9CwgXx15fdU1znPOGCIeWgRyVI7LlgNl6T_FW5x-1EIV0LkUla0Z332yQjHQXa7LK8VaVhjSQZbzjZhv3IETTl1WJHlzhGEYm2Qa9CzcLFHqymDLRVt4Pun3w6fvVA23DXZgo_g8tm8gMTrN7C5RXUcHl16GAcKvXazDL7MgYKdCoTxSFSguV7A9JFliaaKbwLG1b4GFwL24PDugeFxIBuP47bqyuRgEs1myW6GMLsZ671YtVF0HxMEwr8lhC3EYCrx8pQ2C3KGlvOVrhNdePrlY2sm9Gkc42GMJ36tr0YADouauogwIdlwNiuxIDZ0vOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازیکنایی که قلعه نویی نبرد جام جهانی اگه میدادن به غلامحسین پیروانی راحت میتونست از گروه صعود کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124186" target="_blank">📅 16:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124185">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
مراد ویسی تحلیلگر ارشد اینترنشنال: به زودی پزشکیان، روحانی و احمدی نژاد ترور می شوند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124185" target="_blank">📅 16:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124184">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
مراد ویسی تحلیلگر ارشد اینترنشنال: به زودی پزشکیان، روحانی و احمدی نژاد ترور می شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124184" target="_blank">📅 16:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124183">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aj-PZlE9b5t86vOcn4ZoHQ6IjAyli7XYKeCs9Y3A1bxwzXpU6yufaxrQEAOVUmwSBAnqsPwJ9Q1ynBiMpkkPQ42NfFQmjGzwGNikP_kwWd27z9mBWgk2Lj-3qeewkbGlG9kWKnWw8qkB7gyTAXdb868rbiw-v2D_jqtgsfW0pcCAvcrHEU0gIEEKDuE7gmeJ4cYJsNIMwlHqBJcn3iW59qcayWr5rxMkFpmQw54bGrZSTlXBZWaThLOnsc_J5rWZyvThz1S-ZfUna1lVfAZQowG8lCUUIvQwnkx8KMd61hg3UtckFxbVMNG4Wd9RYugNcW16vQBYmyW8WgIvAm23Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فهرست تیم فوتبال ایرانی برای حضور در جام جهانی
@AloSport</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124183" target="_blank">📅 16:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124182">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
عربستان سعودی حمله ایران به کویت را محکوم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/124182" target="_blank">📅 16:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124181">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCl-962be5s2PudFHpBqMF7L0tJidpNofPpJbNtdAX40Z5v7dNuCYzTOy2cTa7lyvpt-MC7f1j3ycwLlrv8noBIO22co5OcXoNsBibW9_e5kA27PArMyMLerfdIQugoNwHP7r1s8oV6_B7BFapAj1gHpizHQHh9SeTVojlIEAtdoXgZi0GQJfuyDaersIhQkByOwZHnHvLdZYkMjt_MOrdAkCHcPLsiZIRZweX_dsy7TL1yStGpVFVuHsf6IiowpvQeUVbF-mqLCWBMx0QUJCclDQvNvyXKsp9n_sd9QoOsz2Zg7Ty1fKiHS715B0u_Q41GSo3Ep3x1mZjjoC8KrOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: دیشب،نیروهای آمریکایی موفق شدن دو موشک بالستیک ایران رو که هدفش نیروهای آمریکا تو کویت بود،رهگیری و منهدم کنن
- این موشک‌ها همون لحظه خنثی شدن و هیچ آسیبی به نیروهای آمریکایی نرسید
- فرماندهی مرکزی آمریکا (سنتکام) همچنان در حالت آماده‌باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/124181" target="_blank">📅 15:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124180">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ارتش اسرائیل  دستور تخلیه بخش‌هایی از بیروت را با هماهنگی ایالات متحده صادر خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/124180" target="_blank">📅 15:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124178">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
بانک مرکزی:
نرخ تورم اردیبهشت ماه ۵۳.۹ درصد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/124178" target="_blank">📅 15:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124177">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نتانیاهو: ارتش اسرائیل فعالیت‌های خودش در جنوب لبنان رو گسترش خواهد داد؛ حزب‌الله در حال فراره و ما مصممیم امنیت رو به ساکنان شمال بازگردانیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/124177" target="_blank">📅 15:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124176">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/124176" target="_blank">📅 15:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124175">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinternet | فیلترشکن هوشمند</strong></div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/124175" target="_blank">📅 15:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124174">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6483eb70f5.mp4?token=EeeXU1KyrNgnI0QAJrMZ4JkvBMscyOfwR5924WSkw7rxJwTX-1sbDDu9TMbnlDYh_yLI8t4KfBnQniMndlTSrExsRjYhAtW24P8NYHQTXXN2K9nXu_JfkJTPzyvRfSqIiMLvSdwZHt3KtxLJ_wOde1QDIqpC1ubq0Dsg2KGTkj2bHIhr0JhFYWrF0r-3RTkTSddXYpZuibfW8cJ4u4SbQ9rwbYVcnEnGjhjyQCa2QpWOQU-2O3UBj2_Yzwr5QwnjGOGdc9p3d6i0gTU2jFBe3SUuOPMoOHhXcuONN2JqlerePNTQl-PG89rxE1YwA4hqHQvtulwHt7TfDJwnQB70WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6483eb70f5.mp4?token=EeeXU1KyrNgnI0QAJrMZ4JkvBMscyOfwR5924WSkw7rxJwTX-1sbDDu9TMbnlDYh_yLI8t4KfBnQniMndlTSrExsRjYhAtW24P8NYHQTXXN2K9nXu_JfkJTPzyvRfSqIiMLvSdwZHt3KtxLJ_wOde1QDIqpC1ubq0Dsg2KGTkj2bHIhr0JhFYWrF0r-3RTkTSddXYpZuibfW8cJ4u4SbQ9rwbYVcnEnGjhjyQCa2QpWOQU-2O3UBj2_Yzwr5QwnjGOGdc9p3d6i0gTU2jFBe3SUuOPMoOHhXcuONN2JqlerePNTQl-PG89rxE1YwA4hqHQvtulwHt7TfDJwnQB70WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در روزهای پایانی جنگ، آشیانه‌های هوایی پایگاه هوایی الصفران امارات حداقل دو بار مورد اصابت موشک‌ها و پهپادهای ایرانی قرار گرفت: یک بار در اواخر مارس و بار دیگر پیش از ۵ آوریل.
🔴
این پایگاه میزبان جنگنده‌های میراژ ۲۰۰۰ و پهپادهای تهاجمی وینگ لونگ متعلق به نیروی هوایی امارات است که گفته می‌شود هر دو در عملیات‌های تهاجمی امارات علیه ایران نقش داشته‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124174" target="_blank">📅 15:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124173">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpjOphcvaITEqMdoCfenlqXgmgJkMKA4jPb1e9RG4o6rrTxTHNTY3Z8T-Dk9WTHC6L1JUdeRrTQcugGrdB_dBRNFfRu5N5vhvpePp-7eZSPrgciNiB-rSyAXlGMrUfjKbplHfXaD6YpPt-HJNmJ7CdMdiKMeMDqqM8T1BSAlzBZ3qgXJ_GNUEf7AGbdgQIdueLjCgB2bD_N5VZqflTHvMFd_7rpS9MC2WUkNCppLFnwOSNLfhktEeNOzhWl5XdJ0EBnjIEfv8AKd56DrSGB5AAltCfy5uA7RYmcMt6mnz0Z_ytnG3Jmp_UXJhRjm0lmXZ8UAEyZ7O7ZYRysXYZIDaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسن خمینی امسال به مناسبت سالگرد روح الله خمینی سخنرانی نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124173" target="_blank">📅 15:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124172">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8W0L2fHNLu8yHfzavvF0oA408jH7J965npdt3E7i-tMtwwqBOie_dxL2mczDarhoEk7ir2dXslzCyFezVw20e0DTIv4Xw1f_7GrMnKl79YomeD0bzBr3OKl0a93u1QiVh09o9yDXIX5Ec4j5FSa7RtW4PVSyAAvo6KwIKF2FeQxSNOLceMtZXDqaXV3sAJ2GSURO2G4DiZt2hMLelwa1QmQ-0u9vQk2_LkNDf1mSk6GF2WzCx_8RO3McwMJJ373cQyPc52Pv_LAoQLe8UM_DgiE2BVZjDkKQ0new0abcTWjjboNH23absxVuL9WjaE7e13YZP1z7W2UP0_P9QYWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی:
عملیاتِ نظامیِ سنگینی که اسرائیل در جنوبِ لبنان انجام می‌دهد، آخرین تحرکاتِ پیش از «تفاهم» نیست، بلکه پیش‌زمینه‌ی اقدام نظامی دیگری‌ست!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124172" target="_blank">📅 15:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124171">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⭕️
الونیوز فقط در تلگرام و توییتر (X) فعال هستش
🔴
سایر شبکه های اجتماعی چه داخلی چه خارجی که با نام الونیوز فعالیت می‌کنند مرتبط به ما نیست و پیشنهاد میکنم که لفت بدید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124171" target="_blank">📅 15:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124170">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075d4fa2e7.mp4?token=gtqviluQNmK5zxST6ywPP12WGrut0AJ8Oy34lNV-lsUHcqZg3A45miOBLreGZ0L8A1kavp6MWwKZRtlVYqSI3ThGYVkL7hMuwecLYTE3CJiHD5IAbwZisGnmZiKwlp8yz0La29eXLchBYu4of7lMJvWg0pdMqacXKnWRIrhevT-dlUMmqv2jMPth-0CCqqk3xriu6a14i7uU6AoNJR1x1SfuYn1HN24NSJNDuWcSAvam-nItNcVuh5wsUxn5TrmDuTxfL8MwIQaxWqapwRDzbiQweCGileM4vtPgEPPlvy47Dk8yKBvrPsxNHdDpr_nNMU7jW6A13rfaapyecEiFGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075d4fa2e7.mp4?token=gtqviluQNmK5zxST6ywPP12WGrut0AJ8Oy34lNV-lsUHcqZg3A45miOBLreGZ0L8A1kavp6MWwKZRtlVYqSI3ThGYVkL7hMuwecLYTE3CJiHD5IAbwZisGnmZiKwlp8yz0La29eXLchBYu4of7lMJvWg0pdMqacXKnWRIrhevT-dlUMmqv2jMPth-0CCqqk3xriu6a14i7uU6AoNJR1x1SfuYn1HN24NSJNDuWcSAvam-nItNcVuh5wsUxn5TrmDuTxfL8MwIQaxWqapwRDzbiQweCGileM4vtPgEPPlvy47Dk8yKBvrPsxNHdDpr_nNMU7jW6A13rfaapyecEiFGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله فیلمی منتشر کرده که نشان می‌دهد یک پهپاد FPV به یک باتری گنبد آهنین در سایت جال العال اسرائیل در شمال این کشور در تاریخ ۲۷ مه حمله کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124170" target="_blank">📅 15:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124169">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a0296238.mp4?token=C7GKLwNQ2yOSC0nQUsHO1LMXRwMGQhlsYoIuybJ-0mjQdPMTAiBHInW2MWUvT2o1zIBi7sYbQ9aG9jVGwXUEXDtlZidJ6OHw66AxOgv4DoKuim4O2fd9cLi-IRHRgw4SD6adLNasdDTz_uZkO1ruNJb9Gx7UsjFZxtzGVLRdUXxwLajQYtWdqHLsaB2iNN0D2gMwhSZfp7c7ToDwuV6ZJu57-YXovZG6_VCxHfEeh_I08u9PxkbrDaKscSmgafgfejSQvb3344I1N3luH1drVo_OKlcvSHCN_LVETEGC9JgTY86HLnSgPH9lco056eZn-AHG7N87eqRLXvxnFxLFZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a0296238.mp4?token=C7GKLwNQ2yOSC0nQUsHO1LMXRwMGQhlsYoIuybJ-0mjQdPMTAiBHInW2MWUvT2o1zIBi7sYbQ9aG9jVGwXUEXDtlZidJ6OHw66AxOgv4DoKuim4O2fd9cLi-IRHRgw4SD6adLNasdDTz_uZkO1ruNJb9Gx7UsjFZxtzGVLRdUXxwLajQYtWdqHLsaB2iNN0D2gMwhSZfp7c7ToDwuV6ZJu57-YXovZG6_VCxHfEeh_I08u9PxkbrDaKscSmgafgfejSQvb3344I1N3luH1drVo_OKlcvSHCN_LVETEGC9JgTY86HLnSgPH9lco056eZn-AHG7N87eqRLXvxnFxLFZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پنج کارگر در انفجاری در یک تأسیسات سوخت موشک که توسط شرکت هانوها ایرواسپیس در دائه‌جون، کره جنوبی اداره می‌شود، کشته شدند و دو نفر دیگر زخمی شدند.
🔴
این انفجار در خط تولید سوخت موشک جامد رخ داد، در حالی که مقامات معتقدند این حادثه در حین کارهای نظافت یا تعمیر و نگهداری اتفاق افتاده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124169" target="_blank">📅 14:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124168">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiayflpsZtn-tEYscMjUjR9AXUJQTjRgxfe1bk1MlCZ4b5MR1ZeDm9jgJsgNx_DAvk1TFT2eXoYbmyzw2SB2OL-mcNgaMqd84ohqqSXmy6CqXnkfxnSEQRa3-XZWNbLt8oOYvGwY5HcgNbXQy97BaXHvpGp5NlSUbJV1miZSKEkexQ1qNmFsxzdI73ayA8ddlUts7kWk18wqZQh3-_Fp7JpGrFvWipCqVM36seKNw16ufDah-rEbBPxdxuqlSkuTR1tIREHz0_nXCK63-ngaT0sniVCgL-Vzl7LgWq0qWfSfU9dnUgi_H18sKfldHcyD2f5X7G9jLRgHlfoKBcPh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی، عضو تیم مذاکره کننده: خیلی مهم. صبر ایران دارد تمام می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124168" target="_blank">📅 14:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124167">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
احتمال شکست آتش بس در ساعات آتی بالاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124167" target="_blank">📅 14:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124164">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmxGBXzb6wMWUMr4UlIc9EJlqifGhmXj-FWJ1uA_GIly7dh3dgu26HOnZJvV0vIxWoMYiirrj4j4kvZ3B17hviEuqtQ4-RSvAORsmfNK5MSZEM9vRaYlmAHRDCMyKzcLThLRNmwEdyWVCeR08qMjhMYvmNrnvt4OSkrxWgyAXPnB9-DIYGSNF9iUQXusom5UnxXBN6ZW2aRTMNuV40ipqoVG0i1YF4gFccNnrjCJBg2GU8uQ-DSCpUghRMBXek-zg7Ttu8WHcNO-ZN38pUFEhvVb7-XH8k8nrNoRXRY1x8v1-0T3jrf8djNg6PMEeEXUUSPjwW2TR7Adu6Arb3sGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TcO4EiaLng8YLVAOr4qvvihL6_1YSv34shc8F_6_8giYuyDSNsp5qqnKM43FZv3z1UfTESgb-C3dv4aYzif9ybyEcRzVxQj69smgTDLqytkQgiJCxrmGesXjXKrCZJW_mKQiftZnaOGxo3QJi-IGxwUKOttcobrna_9F0FIggswgKBCyd8j0V95t2w79uy6OFDMC3tX8pkTNGYVKOVgnozNLVDZBjHUq33L9uehrMwMwLvrUn2f8za28jF9P3XWSrgurYoomTwfesmQ26ABI3e5F_TzlSYYQ0IdIgws8-_Bc0S2lFezzpNlggqsDCXTBtul6-y2pjHelDrbyitCycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ue3ED1qGtDtplSvjIwa1yNDB-L7SeW21FfqNWGYCBOffmEPyCn0vmGzB-sBt_PPNz3_MiWBE8tgLQPBTLl79AtR9y2NRftwEKciSi5nysi_s1QBQRzgxnMPbGmnAV5f_0s9VmcOxUgjg01fyP9W_WT3h6d5ouZ9YnhSScm7clOHCkUi_9oZZOnRETOnVGcGAxwO9pdmG2oT7upte9Ufg426JjtftH-7kuduiKg3JscphdJvkXlFghufbNHWpJQoUKShOchcEa3LTozv38g3k8vgl7MPW3CFTcDmEkqrnp41zXIvZYbCuuA5s0FIcaZYBDIaJtkSxbxtwvapGonMDBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی به تول، ملیخ و شوکین در جنوب لبنان انجام داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/124164" target="_blank">📅 14:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124161">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hlbMfqhMbJYtxb2FvTMFLgch4yTqZEQtIZKX7JNK6BBviQExBHfPVw17DvmsEI7OHgijUboXewYDbpMnqME0bLLIKXuZ1DaG9LpGYQXacS5liiHvpkO83imQH26MGu3e6khTOkT7pvR6FTp2VP1hr-eoBo1oRCtYswdQin2EN_iG8b13FJgRFHjZBWqRxPZmXxZfw76wG5-3SkWMroRjsF8_7HjjejMX2ybfi0vNrvChsCa60KKfxUf7_kiViEdS8kKL1sT_UlmYkjhubaWklgUBlyQJL1rd0mpNl7TbGI_pdbJYWdICB6NOmmaT97J_7BwpF0V3dwveCsC-97AqYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ic3J2TcMqjPfR1TU5H6fuGTYJgG1wxjp27AgguMaWIWeoyS7-tE5CXIzGXPu1r3bHPu7a2Nqlgk4PtJQQQQiP0xXCKpn90l2HUrwHiOeRnRF4bJWDZuUaCrYpg4qv3Jbboc7bEmL4L0RDRGzLztvLp4QTdk0yciFqt2gbOi3ultjmchgrU5NDCC6KqitQ4-1e1DpSe4l12Si9Xlnfhr-C7wKe0zpLqmUji2K3qlhTgu0yEzuypedm-NbrfXI0jnJeTBFhZFwCn0oLTTZ4jF_8tEnOzvvEdUMVZBCjX8DI0v6UEfb6N8E4-tylEKKJxHNCvi1Qnc6I8UH-ELoCf1yew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qu7TnIZvCUiEcsvufLbUJdlBVLXmpMXgVITr9fEVDf0hJgcXbO2A2JCZg43FHaV7JGiJIT3n2UIil_u4qA2bC4Ipwm8WaCV2DW5ZoUN6FBAydP2ZqN_uTmdMPpC91iPXGJVUywXaFAw9oPqQt81IM3-yuIxqQR__ymhaQWjX5nYhKIDZhemX_e7ZmgYT0nAO_EOa2V3UKu6LPI_a5X3HvxQEBAYSKUb1hQs_fsHN9gwdmmIFMygSTY8yJgx8Xg9x2RsHWOTqSlatbavKSKloNB2EovUv4UYC-PgpUvgn1GAsVAehL-YtSGo6s4b_l_CAzUK_RbPH6sL_KcMYnMhFXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
صحنه‌هایی از الحوش، منطقه صور، جنوب لبنان، پس از حملات هوایی شدید اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124161" target="_blank">📅 14:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124160">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYLfr9OKj-un9iGsoWFbdqoiXJkcFFtBc4ydzq9xkbsbyXDVWJMiUbqVCCEn5fpBfXovv8_vReFvqbiEt17TzbAHiW8xyqWZbJfgs4OmCH-KMQXTk8dr2ps31ns9IM9W6wW8ePqdVgZZMk5Uml_m0wI026vg2qTSe3PIqybpRAfR0Uv-c4jOtWTCmQLO35pLnLvNOMKbtsh5gMShw38QqumJK4jQLxT0rBawUn9BaCp_vjHwH5K6Lf10gCx4MwM_g0CbFHfqqeL91NPKr1ejdE-G_jXz9VucZzvqQnXu1bAwaTqMiRN1WftrHlkYwt03rfjVrcQAZfvoTd-7MzcHnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124160" target="_blank">📅 14:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124159">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⭕️
⭕️
اپلیکیشن‌ها را فقط از Google Play یا App Store نصب کنید.
🔴
فایل‌هایی که در تلگرام، کانال‌ها، گروه‌ها یا از طریق لینک مستقیم دانلود منتشر می‌شوند، اگر از منبع معتبر نباشند می‌توانند خطرناک باشند.
🔴
نصب این فایل‌ها ممکن است باعث شود اطلاعات شخصی شما، رمزها، حساب‌ها یا حتی دارایی‌های کریپتویی‌تان در خطر قرار بگیرد.
🔴
قبل از نصب هر برنامه یا باز کردن هر فایل، حتماً مطمئن شوید که منبع آن قابل اعتماد است.
🔴
امنیت را ساده نگیرید؛ یک کلیک اشتباه می‌تواند خسارت زیادی ایجاد کند.
⭕️
تحریم ها ارتباطی به موجودی کریپتو شما در تراست والت یا سایر کیف پول ها ندارند.
🔴
درصورتی که کلید والت خودتان را در برنامه غیر مطمئن وارد کرده اید حتما نسبت به تغییر کلید و انتقال موجودی به والت امن اقدام کنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124159" target="_blank">📅 14:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124158">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⭕️
الونیوز فقط در تلگرام و توییتر (X) فعال هستش
🔴
سایر شبکه های اجتماعی چه داخلی چه خارجی که با نام الونیوز فعالیت می‌کنند مرتبط به ما نیست و پیشنهاد میکنم که لفت بدید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124158" target="_blank">📅 14:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124157">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
یوآو کیش، وزیر آموزش اسراییل، مدعی شد که اسرائیل حتی بدون حمایت ایالات متحده، دور دیگری از جنگ علیه ایران را آغاز خواهد کرد. کیش در ادامه ادعا کرد: «حتی اگر آمریکایی‌ها برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای اقدامی نکنند، ما متعهد به جلوگیری از دستیابی ایران به این سلاح‌ها هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124157" target="_blank">📅 14:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124156">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kE-JiTH5YNWFsYGOa0_ULIE-QeHeAh09M2cMADy2JliDP8_lvsmG4zZ69ydls_eMhIS6KibDnzthZ4AyvrBPXsUaorY9jMR4BY3WKCcrwyNi3nGDm6Zh3X6SRjppiODUjXOejwL-MzR-2sqUeOf93zNoIUP1yd2U4dPWlF59YqWq3l44zsSN-jZiJpHwbzA3LEuzhY4XrdrMyPmVfV3DFeOAoGvkAjzX7oE9bEpUothFnxbGjoVSnCgJGuB9pvsz3uTD8gfkptRo3jvGlrqoNR3EubxoRBV96Hxsgic0xgnbZzu0199Hts1Qh2LfMJl059qtVxSbhASdJUVm-09-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: نقض آتش بس در یک جبهه، نقض آتش بس در تمام جبهه هاست
برای توجه فوری:
🔴
آتش‌بس میان ایران و ایالات متحده، بدون هیچ ابهامی، آتش‌بسی در تمامی جبهه‌ها، از جمله لبنان، محسوب می‌شود.
🔴
نقض این آتش‌بس در هر یک از جبهه‌ها، به منزله نقض آن در تمامی جبهه‌ها است.
🔴
ایالات متحده و اسرائیل مسئول پیامدهای هرگونه نقض این آتش‌بس خواهند بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124156" target="_blank">📅 14:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124155">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/b8c69052ae.mp4?token=KXvW--ptTQtkMpOg3hTZZEfnnh6plGN-wCLfElTVu3j1qZuzsNEkwI3U09eIXN5kglQPY4PyGOqTL0zYtaiooR_mWhYZEJIqrAj5VRe3JFD8F4TNubAyhMY9t-vWC8nj0km_nLi87MgcmIj1xusE6czKD71Zxzr3MLboG630S3LotyjW0PbXICIJ8OZsAdYeon4zQBae13fCvxuUFVjFX5m6pO7WX2j3wqhcIOW0bkHuYp1No_fu8tSLQM1GRoAi0d1XVo36z1lq79h9o3zenoUhsvhHhkgknJkJco5C4ghM-XsV26us5SvFx3-8xhVkrPld7aCEfWpnX4gSzdabcoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/b8c69052ae.mp4?token=KXvW--ptTQtkMpOg3hTZZEfnnh6plGN-wCLfElTVu3j1qZuzsNEkwI3U09eIXN5kglQPY4PyGOqTL0zYtaiooR_mWhYZEJIqrAj5VRe3JFD8F4TNubAyhMY9t-vWC8nj0km_nLi87MgcmIj1xusE6czKD71Zxzr3MLboG630S3LotyjW0PbXICIJ8OZsAdYeon4zQBae13fCvxuUFVjFX5m6pO7WX2j3wqhcIOW0bkHuYp1No_fu8tSLQM1GRoAi0d1XVo36z1lq79h9o3zenoUhsvhHhkgknJkJco5C4ghM-XsV26us5SvFx3-8xhVkrPld7aCEfWpnX4gSzdabcoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع فعلی هواپیماهای آمریکایی در فرودگاه بن گوریون در تل‌آویو، اسرائیل.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124155" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124154">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a24488805.mp4?token=W9227u-LQ5dk0aHPTgE54DIKJjCvTPrjZuvhT0cziJ16gLTtLc3nFHQAC__2iL33EzToxEW6VjIY1lOHgoCSWjyNUeooqJ5CPtWLBw1aP5wlA0NYOLskU5T7dUt7U8wzw6DA220Y2jDMSMtBthcWHResH4kejuL7-xbxrmRT17iO41w792BrvvQ-OtC1vOdgS1Di-2hVl3KKOReGkV7rWyoChnRfcOHQEvujbEHihtstZql1lzVUBzgFgjNbGisCwZQxYJXpWfNJLqDIXlVs_Q0NXXcnCgz_HVOmzPD9GS_uZcWUKMbE3tyhXZV-AaN_yEkrD0G1_zY3gh5vZvjosThTYrxOt9k0HhWfYENp6WIHJCJGa9MaAEwN7tEPOx0uyMXaKf-TOO-0aw1_dO6FaXRUWDDgLFa473lEstxknXFHqiZCrGHMdKL6SgZHrx-42lVyay-yIkAPGiaIENiwlf5LT-pCG9tC7xJyBvvxkfolo6pMFHTw-aPepdk1V7EbkABpucEAku1xu9veAQrJR3-qAudaoDTV46lv1TNkIspZj7tHOE_qx0SKpXnK8FaroDML1Vba2e2UQ8aIksTIW4h40j7P5X7FrbfVgLNe-GwDdXyFsHf0wQEeHUJU9yyF-uIpc1bCd5hSzO1ex1INlVm1LiPxS0qJhYt3IUg1Cqk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a24488805.mp4?token=W9227u-LQ5dk0aHPTgE54DIKJjCvTPrjZuvhT0cziJ16gLTtLc3nFHQAC__2iL33EzToxEW6VjIY1lOHgoCSWjyNUeooqJ5CPtWLBw1aP5wlA0NYOLskU5T7dUt7U8wzw6DA220Y2jDMSMtBthcWHResH4kejuL7-xbxrmRT17iO41w792BrvvQ-OtC1vOdgS1Di-2hVl3KKOReGkV7rWyoChnRfcOHQEvujbEHihtstZql1lzVUBzgFgjNbGisCwZQxYJXpWfNJLqDIXlVs_Q0NXXcnCgz_HVOmzPD9GS_uZcWUKMbE3tyhXZV-AaN_yEkrD0G1_zY3gh5vZvjosThTYrxOt9k0HhWfYENp6WIHJCJGa9MaAEwN7tEPOx0uyMXaKf-TOO-0aw1_dO6FaXRUWDDgLFa473lEstxknXFHqiZCrGHMdKL6SgZHrx-42lVyay-yIkAPGiaIENiwlf5LT-pCG9tC7xJyBvvxkfolo6pMFHTw-aPepdk1V7EbkABpucEAku1xu9veAQrJR3-qAudaoDTV46lv1TNkIspZj7tHOE_qx0SKpXnK8FaroDML1Vba2e2UQ8aIksTIW4h40j7P5X7FrbfVgLNe-GwDdXyFsHf0wQEeHUJU9yyF-uIpc1bCd5hSzO1ex1INlVm1LiPxS0qJhYt3IUg1Cqk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اوج استراتژی و تاکتیک جمهوری اسلامی همینه که میبینین. هنوز نبسته ان میگن حالا بقامون رو تثبیت کنیم، بعدا واسه زدن زیر میز وقت هست.
🔴
منتظرن 2سال باقیمانده پرزيدنت ترامپ تموم شه.
🤔
تفکر حرام زاده ها حکومتی همینه، فقط دروغ
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124154" target="_blank">📅 14:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124153">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نخست وزیر ژاپن: با رئیس جمهور ایران تماس تلفنی برقرار کردم و از وی خواستم آزادی و امنیت کشتیرانی در تنگه هرمز را تضمین کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124153" target="_blank">📅 14:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124152">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
امروز صبح تو دانشکده‌ دندونپزشکی قزوین، یه مرده با کلت کمری وارد دانشگاه شد و همونجا زنش رو کشت و بعدشم به خودش شلیک و خودکشی کرد...
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124152" target="_blank">📅 14:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124150">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Cuh5cuSmrIBmXZp8DguVdZxCVL5z5Wv_pFab-_UI8p_Cvl2m7poQWTLMY6Y2ARcxxdmSAQdrbbava9Zl7JiKBiSr0Y02VsFukMNxj6akwC8sCp3yvL2ZKs8D48nweX9avnwWaK6FeMg1W54pWeO6CYJSD_eeimSh_Py0jam3FZHgGOgxqLssutTdlRuSGcarOyyxKx1P9Coiku27i9OPCGDdhc_tcNg0YNuOHc6zmSHrS54_eswXRU1JGIXIWc1SnUhzfs700JVjq8BTknZe-VB2AJDtQdtcOzZ0-mFhWHVnMQqgUPtMlkf6oV1QaAEa8MXzcChFvN7AB1cUyIklIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/naPWJs5K9W5lFm7Ie2v5zW72zhxVTloE1BRl-295PzkuKyoszIXGPMoKk_pkYKYStVW9uK-4VUGYqkze8ShVE9_jgaDc1ThCIVorD2WJ9mjbcRqrmASj91xgvr4x_0T6YGQk2ZmgP7Ejbso8y4buZ6DaUV6nWlAFh_0u3wA5eELTlHg9KdeuLSWpgCvl-iQ5JA50IdA685onwlkfcjelRNiAY0g_cCJouDGrqpLphYhFYYaguGbNiDf0i7s--c4Gng86sN4y8AXKNMzq7DXH-HUWdi53eZN07m8_0DSV5rIBhLHm2P7-KnXz8Yde7G9ht3lEleRTPj2Kyr2eN8sVMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گزارش WSJ: هکرهای ایرانی به حساب اینستاگرام جان اف. بنتیوگنا، فرمانده ارشد نیروی فضایی ایالات متحده، دسترسی پیدا کردن و تصویری از امام علی پست کردن،هم‌چنین حساب رسمی اینستاگرام کاخ سفید دولت اوباما رو هک کردن و اونجا تصویری از امام علی را در کنار این پیام منتشر کردن : اینجا کاخ سفید نیست، فقط خانه شیعه است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124150" target="_blank">📅 14:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124149">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUpIgqIEHxyZEZfSPRZvmrskgWxypZVkiosNvFXVpr_pfEqkGmQYgDrI_Pz7McIJ_dhhPnD6mZWmxdCD-6-GzGRXtbEbH2Ro6jRZbqhix1ZlTo9pzOFuE0j4qV9eTxQn2ySrHSASSC7glRkNaqhs9b8sZVat7pLRLT7pJmfPGg_zMjADzON1nW4xFwcU5QxnO28eEeRDVdL5J1vaB9t8b7vEp6SjX9HFbA_-1kWbaNRA8gIB0dUSZSBPmJ902eRfyZAc7zmmAFYonA6yCy8tnscS0rBOqLXM30ZVX42gWryS-nCMgrInE92SmghB9rp9Behfn9CKCry0bPG1ttqGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان توسط رژیم صهیونیستی نسل‌کش، شاهدی روشن بر عدم پایبندی آمریکا به آتش‌بس است.
🔴
هر انتخابی هزینه‌ای دارد و صورتحساب آن پرداخت خواهد شد. همه چیز به جای خود خواهد افتاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124149" target="_blank">📅 14:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124148">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X53PfkYJPp_zFDbysA5Dq076sLBSONi8wUWfqR7SMYmrxqeVhQ7Cp9aINHsYdsMTxKZMpKWvDPXEggHFTTo1wPhMghUOswHbpZn4jU8u5hv_S-pnlUPZ9JfYwxXDbfVKaEsl0F6YZR2_I3TqrL_Ym6xcStBMuWzZfWAwOJEc2nzeTfp9pCz--_a-VNXY6VWpL8vEyM3DQNhFewy3qzGbID8qzefy8YLJq5STQcBMo5bldzqs6xi-6tmA3aRIy4ZTSZ1dqZYOw0WzAcsCsFBmsseeWXRgOBcTUO7TRd09rXKusxr7mE0AuBuxsAiZshwY9nipC2bEp_2eiB69iJzkDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دن اسکاوینو، مشاور ترامپ و معاون رئیس‌دفتر کاخ سفید: هر داستانی پایانی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124148" target="_blank">📅 14:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124147">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1gqzJRXrI1boSTDZA2JYJEPBETqb5sgdR1RW2dLIcmS3C6d1WMYfLuWww8QHKyk1WyJU7l1m2Z27I-YuI6l2y-BAD7Xcyeb5WP9Dx1dH3A-9LiuEltJy_a0G-rmtE4Wj0kalGQBxsRYMqJigkMvvNkzlBgK0ezxSo6-xmVvY8VMfM8fg5QTKDxPgvz2Z2XITU2DnBbIBZBXaikyHaX0hOSJQcnF0x3OWwLlfbxFQmzKJak2NsZIvA9xiezkG1iP-U_IY4UkfOrSqLQwlMrOMsKhrYmAYWX6Tg5uGQEzF4b2-UijPGyTtyTPA0gumL6UYg1sPM19JTIeBZ4fgGtoeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
آیا تا به حال کسی یک دموکرات خوشحال دیده است؟؟؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124147" target="_blank">📅 14:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124146">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMGZF6TiNPXIJShx6Xy4rLTJ0LhgRhfETCzR52YiFOFKFwJJM8V7ktmcxZjfGwskszZriwVB-tHrPNgxK2dLW4Cq2K60lyEwgFjYvMGvC-G6viqQ8hAMYvY6Dnv2ZhJ1A3ml8OVQToh2rQ3tgT-qDyzsk4PUK3oMZjd0uTGxGZo9Lg2OkcrND3HmeQvmNBAsD_LpeZjVxwWfrS4vS6nuberNJJGQ6HXTl601uPdtVEl2zY2VCIrwOaYy_3TtPpK_w25e373F9PZfvMMofLFoNjGxPqLPNF2f_Rr4Mk7v39g4bj2wp-y5Ul64_H-znk2eX-EsWVo_0gjQjoV-0Uf73w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۶۴ هزار واحدی به ۴ میلیون و ۳۰۰ هزار واحد رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124146" target="_blank">📅 14:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124145">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/188c520708.mp4?token=SY-B3pcqNRndNwwX5tvCfeEmnmISrEGOs-ojyIso1eWXvq_Cv1TZeRAXNDdaq68P61lhDbBr1-joY6NRoLFC-xPKXhAEj1N88EroakwK8ERE1mZRsIl6COe0Di3CZBvCmoFWer2ocmVvB7EpyH7HLzoTyF1dAqb0-n9oUZvbaZ5SM114p6ZOTNyRUg3VPYCwrBZhjs1lJVD3aM_pGEqJzSLZaPH7rxGeVm7N7wbx6z5wdUcBW3DMOxDpFHT1COUPzpd_nIHPkVLgMWcMN5nBYizPPXWd78edE6SCBJDg77o_6ev7Mto4lpJF-IZQK7KEtdTJW-k8WuamMw6kJulLyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/188c520708.mp4?token=SY-B3pcqNRndNwwX5tvCfeEmnmISrEGOs-ojyIso1eWXvq_Cv1TZeRAXNDdaq68P61lhDbBr1-joY6NRoLFC-xPKXhAEj1N88EroakwK8ERE1mZRsIl6COe0Di3CZBvCmoFWer2ocmVvB7EpyH7HLzoTyF1dAqb0-n9oUZvbaZ5SM114p6ZOTNyRUg3VPYCwrBZhjs1lJVD3aM_pGEqJzSLZaPH7rxGeVm7N7wbx6z5wdUcBW3DMOxDpFHT1COUPzpd_nIHPkVLgMWcMN5nBYizPPXWd78edE6SCBJDg77o_6ev7Mto4lpJF-IZQK7KEtdTJW-k8WuamMw6kJulLyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : با دستور من و وزیر جنگ، ارتش اهداف حزب‌الله رو تو بیروت زد
🔴
قرار نیست حزب‌الله شهرها و مردم ما رو هدف بگیره و مقرهاش تو بیروت دست‌نخورده بمونه
🔴
عملیات علیه حزب‌الله تو جنوب لبنان ادامه داره، اونا عقب‌نشینی کردن و ما هم مصممیم امنیت شمال رو مثل جنوب برقرار کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124145" target="_blank">📅 14:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124144">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
تیراندازی در دانشکده دندانپزشکی قزوین/ دو دانشجو کشته شدند!
🔴
امروز حوالی ساعت ۱۰صبح یک دانشجوی مرد در ابتدا همسر دانشجوی خود را به ضرب گلوله به قتل رسانده و سپس با تفنگ، به زندگی خود پایان داد.
🔴
دانشکده دندانپزشکی قزوین پس از این اتفاق هولناک، تعطیل شده است.
🔴
هم اکنون پلیس در دانشکده حضور دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124144" target="_blank">📅 13:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124143">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJNMQIXsAstlHSMCV0f_PFWLS_XrD2gG7BtFYaDxg5Xpdbr-cis6SXuLMUnLzuf0_s5HGwiaeKZ2iRyxCO_EBToMAS9z3b0Zv-6nFbja0EFkYYtU9WJxz854r_gawnmCPHmoZRBVpII0uBjTPiqGd1SSTQ-acS6pwx2iTYloo5lBPP9f2YhcGunJpFNcV2Qe4yEaS5DhbLj7O4g0DxNGfYnTcbZhlX5XRbl8FClFXZtqihI7fSpIOd52W2unLVSppxMeHvca2ZWBqcu7EKQgf9OFbHMH3yw0yFhKQpXthOceNuxfXGemB5rxsB6P7ovhuBT307zaogGnkdJo8Qmbsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاتس، وزیر دفاع: «اگر در شمال اسرائیل صلحی برقرار نباشد، در بیروت هم صلحی نخواهد بود. اسرائیل از ۷ اکتبر تاکنون در دوره‌ای امنیتیِ بی‌سابقه به سر می‌برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/124143" target="_blank">📅 13:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124142">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tB4ShaL8infgLpUklajI6AIXaLr8IkQEVT74BMsr1drnAvvZOnRkIw4h2bq0H0WYN-MXtrpZ1IrR2uoyhg11GnPcbjbCchhkmnX5NUHcore3EIxEyir8ecwna-JUHun3MvgiCuPKzHuJ8JTqP3s9JLiled9xFQPp3k04L1te-X-hpO4L1QtvyxFzZcVER9Gn2ng8vv2sQ-FycdQVK_tjTLt8Vd18tPbGRlI5o2QUur68dWfCbQDcIsF0eLt8PtVf8SqUJQHRjCCP5nSz83QlQ7lo65c2WPcckBIxXKOUPLsZ3yIc5OnZW1iD9veFNuEsMtFE8kc_DIRtvgvWgjF29Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گفته مدیر شرکت کشتیرانی DHT Holdings، شرکت‌های نفتی با شتاب در پیِ اجاره نفتکش‌های غول‌پیکر هستند تا مطمئن شوند می‌توانند محموله‌های نفت را جابه‌جا کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124142" target="_blank">📅 13:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124139">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YF0-LF7EtF2nOC7k2Odv-402P0VOtN3oJv7xpXtl3uM_aH-MDh15Mv7FdCjGhwdg46qrkudDW6v60b98FU1qFbT6cbJ9DJCi7fv-gmSKOUXTSkAR5335pT1xx--oVKi8KQdMWvKgs3Ao5V5vYC9XzdzPP2TIrq3bbFFoN7bnj68ME9ymlVOtXjfqetoZ1WgmNnalucwML-iafmz9zV1qWj8yDbPsZK53l1GpXXSoiSPtofTnJHUGDtR3vMWqDjfq2JkFftih5vebW_BRevjRnEE-LylrUu7yoFmt4fc2Sg0ABw7Xq2Ucx82sHSq4Zz8ZQUBDKMiRO61__zvQU972nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HyN-e8mDg-0m5o9Hu1WJPvJALWVjNrGC8c_JS6hcugN0W9djfIp5FVl4dFrttmf1W-MI-e6vlueuTlAfw05EaWYHsivgAXR6ppf_xmbbT1xic35lUK-tdhBWPspF8Sb0SM2Dlzy-CILDwimJWy74sRsHugtU1kyG8bPRITkRb_VDZ08YW3vqcpNaj08sUIpVJYpRa0tk27O0ZFpq1x1KrOR99deikgx_HjOGwmAffzpoklIJ8_B7zpRjGALjagQgPFwIf2ktTLA5HuvTTe0KTc2gQyiU6krYZbAuyK5PJlvlrZz2otpy1ayELwxhm8rui_fW99sKR8mnNds2sZZ99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mrjte3sQ-VwlONMM9fiXGWKHR2NwnmRYCvmLft0yazr6q10h8OlSIAz0hs-Vjxt5p0SE_ALWE6fmRdy5r95eToFvz8XQyh5QLHjgUViEHKOWi6Ht_bhaqU6TE0F_YAPz_76Fui11OoEwaA3mSK-QjLi-HWKtzvP5PD4QfjCZ-taX08H7L2JZ3ms2lKFG0ytsHha8wkeGE_uLI5cAeL3VZjkjKiqzy4dooPosYkzwwzxjxMOCIR4chGerZN0b_LvlAdMLCsyE5ywCoFiGvdxtGiHPVtWukVogJxre8MLvD7I_2FtUHKmaXVuV6rhXtjuc0kPNdg-bzNLSIrPM5RLU8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124139" target="_blank">📅 13:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124138">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdjCG929CfjIlWbi8lXKpsyiYkC7UZKiLFueUN3Li_j4I2usOrHRzFmHpgKlEhr5rnsaRH9VL02i1VVEWPxU5r9-Og_IGYjk8or8H1OiXvhTLluhVrCK0XPlTwtnyx2gQM8tq-TBGuR3OVxMtmy6mAsO4P027ii9IOEnIF3TW4qyxgxG0iHZIZ6mhZDB_OWoeE2ZsTL81x1cdtKK3TjNG8v3CzHdabQs64oKNLgS3WBToBe8KszxdXhcEN74abMNpUKpBUx39ZzxDSbTXbgGBXWQQsP3yugUTsIQuXmggTCSqEQAGpzZoE6nvpCh3CpL4Lp9OMzeU754NL9THzOfkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قرارداد‌های اجاره تا دو ماه به‌صورت خودکار تمدید شد
🔴
رئیس اتحادیه املاک استان البرز از تمدید خودکار تمام قرارداد‌های اجاره تا دو ماه با شرایط گذشته خبر داد و گفت: در کنار نظارت بر عملکرد مشاوران املاک، فرهنگ‌سازی برای رعایت سقف قانونی افزایش اجاره‌بها و تدوین بسته‌های حمایتی برای مالکان و مستأجران در دستور کار قرار دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124138" target="_blank">📅 13:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124137">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJz_sZl49Wgt_ZaQZLYHFRckEjywfPG0FDMkHeZbEQhnOkwQJi2JlNfArTeNYkDKZyrts9EC9bAQp3yUEDJHVv6XA5ePPVKyKB0IhHXoUZLfyWNtfPtYxywoN1eHNha-JX9CFSZ01PBuZOIyYO39icn-XHBMX7i0cQrpzp1rRHWZk7ZkD5Acg-Oa4chgH5R3pMVWp7nO-rn39RxsIFqgBha3RcYEQX4iQHDZBaoqrL7RRQp5Tv5Y42T9rctKZpVzP9eZ2BtfJXZW0PzkY6QJmlryWS5ES7SbyvxChtpZdQZM3eaOyRWv-vLUYnuD4TISjslqbjO5QxaFa0HdY4oF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۶۴ هزار واحدی به ۴ میلیون و ۳۰۰ هزار واحد رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124137" target="_blank">📅 13:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124136">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCk18VQiiUBkEYV5uL2wisAZDo82VXcZV9BB4cNDamECdqtraXtir1Q3FCtaMPeBTe1KJ_pOi9zrKtU5CyuwKxxHoHPks1iEDv0aIozm7yxDrTcpRc5EOBA4d5K3Ut3z0yI7qzKm7ngFPnUcfht_FIGcQDwzwghkv71Ixl-hXhHDVaHoxrEBot__UeFzExkiRZwC_Cl4JoH9LDVST_ngG06sUQD5rJaOlJd_a089956sSsjBvNRE5PwzaDZxVk6bdAXXm7J5CljLQeHxNsxM_4XobrJbGO_LcRD8Nv3Z9plld42nzwCNleVz9wKP-J1vtBrW4OG5Czx7MYUBhA7tnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علیرضا فغانی امسال به اولین داور تاریخ فوتبال تبدیل میشه که توی چهار جام جهانی داره سوت میزنه.
🔥
@AloSport</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124136" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124135">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/413f7d8180.mp4?token=EL29JMW9ih6QtnAvf4BtEw9rx24slMpyvacDULepPpn2yMEv-i_bsskW50Amic8KH-beN-0QJKBAbxyXuw7D4I3OmfkIdhGCQysQlUYlwx6X_vYLhiZfJowYtpL7M6ceEXZNGjwWnCBIC3PX8MawaCb8QgMDrOOVdr7byYZTNaOi9qosfZM0Vzh0hwifvtjH6xDJojI1Z1cGcp0zBct66RRlBMn9pmyycObeXi4rWY9OIjEwpv4FjbiD1ca1sKnp0KQCLiiMk5grmaB9CFX5BYZxxqSg8ItM2aHDEGCvSjbFaHOn8HMofJp8491RvUnzEKjrwZddxufy64oHSg1pKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/413f7d8180.mp4?token=EL29JMW9ih6QtnAvf4BtEw9rx24slMpyvacDULepPpn2yMEv-i_bsskW50Amic8KH-beN-0QJKBAbxyXuw7D4I3OmfkIdhGCQysQlUYlwx6X_vYLhiZfJowYtpL7M6ceEXZNGjwWnCBIC3PX8MawaCb8QgMDrOOVdr7byYZTNaOi9qosfZM0Vzh0hwifvtjH6xDJojI1Z1cGcp0zBct66RRlBMn9pmyycObeXi4rWY9OIjEwpv4FjbiD1ca1sKnp0KQCLiiMk5grmaB9CFX5BYZxxqSg8ItM2aHDEGCvSjbFaHOn8HMofJp8491RvUnzEKjrwZddxufy64oHSg1pKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بخشی از مصاحبه مهرداد فرهمند خبرنگار بازنشسته شبکه آیت الله BBC با محمد دلاوری خبرنگار بازنشسته صدا و سیما میلی!
🔴
فرهمند در همین چند ثانیه ظاهرا به چند «خبرنگار» که جلوی دوربین بغض کردند هم حمله می‌کنه که از قضا از همکاران سابق خودش هستند!‌
🔴
فرهمند خودش را ایرانی نمیداند و بقول خودش هرکس فارسی صحبت کند که ایرانی نیست ایشان صاحب همان تفکری هست که دمشق را از خوزستان پراهمیت تر میداند وهیچ وقت آنگونه که برای سپاه احترام قائل هست برای ارتش ایران نداشته.
🤔
پول نفت ایران تو جیب همین حرام زاده ها میره تا از قتل سیستماتیک جمهوری اسلامی نگن ولی از تنها اپوزیسیون مردمی بد بگن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124135" target="_blank">📅 13:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124134">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54174c75ad.mp4?token=RbmSm9Vqs9MKPN2rNhgJ1CI-X6PXd56LpQaNGUJ6buTVUgFXreZWPutcFCC0qA1kfwT56E3XjFwNC97eDD8kCiILMeRsZDqkByJD2ekwBV-WoIsn_JBKOmO3jF2kmv6Et3EbJGcLvxnqVGkUZGBK9t_57WBdqPmR3EqpS_2FYzynSPyiU_uYSksOnEPurxm7kFGDlK_QhDk-q61vEmvQxzPBADfz80fr5DG1sx3rqpxnPp5YuiHzPEle1OZ8p7f3hT4RN-K_MgQiBVa4mRZ7pdj1sUeYD6JHiwPtLWuC0NAsjWMSPmoE97SwHc86QYnmNgr99JtJf9tSmiEc7af4Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54174c75ad.mp4?token=RbmSm9Vqs9MKPN2rNhgJ1CI-X6PXd56LpQaNGUJ6buTVUgFXreZWPutcFCC0qA1kfwT56E3XjFwNC97eDD8kCiILMeRsZDqkByJD2ekwBV-WoIsn_JBKOmO3jF2kmv6Et3EbJGcLvxnqVGkUZGBK9t_57WBdqPmR3EqpS_2FYzynSPyiU_uYSksOnEPurxm7kFGDlK_QhDk-q61vEmvQxzPBADfz80fr5DG1sx3rqpxnPp5YuiHzPEle1OZ8p7f3hT4RN-K_MgQiBVa4mRZ7pdj1sUeYD6JHiwPtLWuC0NAsjWMSPmoE97SwHc86QYnmNgr99JtJf9tSmiEc7af4Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرگزاری معتبر تسنیم، ویدیوئی از گشت زنی قایق‌های تندرو تو تنگه هرمز منتشر کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124134" target="_blank">📅 13:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124133">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
طی شبانه‌روز گذشته ۱۵ فروند کشتی که ۴ فروند از آن نفتکش بود پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگۀ هرمز عبور کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124133" target="_blank">📅 13:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124132">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjRJ1v-9zjUe8SMFyHtp7O5Mk7TO6vJMxkvb8wD_mIkNIxjLm5q9PEmBDgfmqo0obwchv3DjVLGKA5-5chsh3bMdPbLaZqaETpPVFujcqFYNGnmg7-Mjrq61jjEaXaZjp42lhvBNCQl1FFRyQfRdKe4yPfprlrHKb6_oyC9bBPVj3fZ7eWzd_Ut5ScWrIM_hmMrZD8SP8BaqltFNfH5crpFCkxKG6SB0-gzo9bb2IQeUjYR1fLL6iJwmFxAKJi-Rcju3ogg-PnPcdUZy3WvAymCkB0prkbN5161KN2VVkWylRoBy3wcQgfV7Z-YTvsvIuMiyXoOxXMUZvU6c4c9WWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز صبح تو دانشکده‌ دندونپزشکی قزوین، یه مرده با کلت کمری وارد دانشگاه شد و همونجا زنش رو کشت و بعدشم به خودش شلیک و خودکشی کرد...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124132" target="_blank">📅 13:41 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
