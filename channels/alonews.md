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
<img src="https://cdn4.telesco.pe/file/sZZAGKBaJzlxPKr0fnU3J23KFB1IrS8R13vYCz_108Mczwl_x2KuLxErtJU_eMza9l6VsTBbHnEhq_6u2L2N54xtGdJmmKk3NJOCX5DxWLzrawDpH7IkmUAIH-fVe9GaWTSO0xy-J17JhBwgmY5RDMufr9gmc0jhzXyZIrJpxBd9siTBn2AMZzqXaS9f7RTPC6XXJ9d-yKbbuXWj16Ea1Msa6cjNb75u3fwZGwknN6fJOBHQ1CrQ4FTp7FofLAaR9ImVRM3w6Ucm1U1q9urIbPz17AOaOPFrNAyn-zKL16LCuBZXwkSWv6IhUBi6DVSciG9ymF7TbJIG_z4GS8xu2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 980K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 10:11:15</div>
<hr>

<div class="tg-post" id="msg-140326">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: ترامپ به سمت توافق با ایران می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/alonews/140326" target="_blank">📅 10:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140325">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
خبرنگار الجزیره: سفر نخست‌وزیر پاکستان به عربستان در مقطعی حساس برای کل منطقه انجام می‌شود
🔴
امنیت منطقه‌ای نه‌تنها برای عربستان، بلکه برای ترکیه و پاکستان نیز اهمیت حیاتی دارد؛ دو کشوری که هر دو با ایران مرز مشترک دارند
🔴
قدرت‌های اصلی منطقه که توان نظامی، فناوری، انرژی و سرمایه مالی عربستان را با یکدیگر ترکیب می‌کنند، اکنون در حال همگرایی هستند؛ اقدامی مهم، به‌ویژه پس از تحولات ناشی از جنگ ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/140325" target="_blank">📅 09:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140324">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHEQVfADmVCr-HNC4pNdr8OSa3gutaEh7goySjiaW0lsFdmQiRFZADcvZxszn2c6d832-hlcQPziXa255_B2ZNQXr_LBpO_pyrXQjUjAA6epWbGG1CtvFzzDV9JrvXYLms_pWS97m2usYx3ayQHRb5AixMZcpA7ClmbeiqysLnSSfIDcWHkSqjbym_Y8AFwSRlpMCW3kHPlMH0cep8Rw41MrfejmhsCN4yo3JfyQ6SdhkLBbiqzo6n81UM7FsGCRlwhN9CRgnprpOeF0GhuBcdeoqESxjUQNnmgjywBAL1_IbNtSLBS5TLKC4isTmZGIikYPek3Ve1BvAPH3TLVGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ عکس خودش کنار جان‌اف کندی را در کمپ دیوید منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/140324" target="_blank">📅 09:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140323">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZucdB_OXdW0MQcG4Ypw7LXxmNt9jR4l-_ps4c_QojovysbeYNfxCmklM5gE2RYpsInmgXknloUlnSnF7CyR4YjK1jF5EGr3QdmwiQwz-DMp6pwQg1271hmkhmEigBzArXq8Yca-FmKTcdYv8ND3teC80-N0oAC5zQjDUYVJQl2RhEemTkWnWUHzAvlYc1j5CSWOxL_qS1MAZYyEu0zlN5k2HHg4klbPGmXFeeR1_1LhbkDWtXKqIbecHCpFJ1JiYc4LSVrcwocJzGV6lZ7a__EM8jtNSI3aGOhxrrEqxKg-XG9BUUE-3WxTQHlV6Z1EJu-3cQ30c0eBfqAPnvxDj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجله تایم: وزارت دفاع آمریکا(پنتاگون) حدود ۴۰ میلیارد دلار برای جنگ با ایران هزینه کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/alonews/140323" target="_blank">📅 09:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140321">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0d2b7aa1.mp4?token=oLjBv2yqzLy9W98GctQ8rao5UqFYH2BBfAy_uvnkwmfilTtVblPL5lODOFJ2h9P4NcOYUxHePq3sMTjcEIW6sQ5LyXYu7vKCWiKSIdmQn0iUZVH57iCtIwvXkGAfr4KJ6gY-Y3DnSxmKj6lPf6UOqFMBzvgG3avOBO-p4r8kZ0VwkHL1aNi2HC2pEdCTwA-dyOuV-mK7Ja4l8QH2SzJLs2fOYOFGPc0RZe0LuBb93rMUdOMh2YW3k16W7Gn-SRdcXgzqkGvRlF8sL4y84YKZItMKHrF0wnjhxb68ggiy8eJ3LhkiNWP6R5XqhJfWtWA4B4MwZnN6iUMVvikv81lCdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0d2b7aa1.mp4?token=oLjBv2yqzLy9W98GctQ8rao5UqFYH2BBfAy_uvnkwmfilTtVblPL5lODOFJ2h9P4NcOYUxHePq3sMTjcEIW6sQ5LyXYu7vKCWiKSIdmQn0iUZVH57iCtIwvXkGAfr4KJ6gY-Y3DnSxmKj6lPf6UOqFMBzvgG3avOBO-p4r8kZ0VwkHL1aNi2HC2pEdCTwA-dyOuV-mK7Ja4l8QH2SzJLs2fOYOFGPc0RZe0LuBb93rMUdOMh2YW3k16W7Gn-SRdcXgzqkGvRlF8sL4y84YKZItMKHrF0wnjhxb68ggiy8eJ3LhkiNWP6R5XqhJfWtWA4B4MwZnN6iUMVvikv81lCdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز بالگردها بر فراز آسمان بغداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/alonews/140321" target="_blank">📅 09:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140320">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجارهای کنترل‌شده در استان بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/140320" target="_blank">📅 09:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140319">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGJPomGX0hXieQgVMjxbsnc_Fd6yiYI1AtP-JoC3fCaH__38hLu656iDbIzxmses_X9TylabpqwrjZbY86Xx2ybJ9ao3zkVTbEotcRZE-SPaesHTcniubgT-YfXngTkpnKLj-6AZlAycabUbKVXXWPYzAX_SEcUYap-9ZXowFX6KRFm-2YwZ11hkaZjyvh6qj0lJoFCftvOWGGgmcdPQFlsoLEPIQNgeU_cLA6R4ar3ca3zssZ3rzBo1C5BQ0LKSlDY3CcwDV5frkKChvJ9OUEuc7zC72A2F-h_pt8Zy-Vit3QPDyVjvoL5uy2pC9RumPnyzRYv6cUlZ2zNYCjvF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخستین دفاتر ۶ شرکت با مجموع ارزش ۲۲ تریلیون دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/140319" target="_blank">📅 09:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140318">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
دنبال تیراندازی در مدرسه‌ای در منطقه بانگ کروای استان نونتابوری، در شمال بانکوک، چندین نفر کشته و دست‌کم ۲۰ نفر زخمی شدند.
🔴
پلیس تایلند اعلام کرد که عامل این تیراندازی یک دانش‌آموز بوده، اما تاکنون جزئیات بیشتری درباره هویت مهاجم، انگیزه او یا شمار دقیق قربانیان منتشر نکرده است.
🔴
مقام‌های پلیس ضمن تأیید وقوع تلفات در این حادثه، اعلام کردند تحقیقات درباره ابعاد این تیراندازی ادامه دارد و اطلاعات تکمیلی متعاقباً منتشر خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/140318" target="_blank">📅 09:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140317">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سی‌بی‌اس نیوز:توافق پیشنهادی بین ایران و عمان می‌تواند به تهران کنترل بیشتری بر ورود افراد به تنگه هرمز بدهد و دسترسی به این آبراه حیاتی را پیچیده‌تر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/140317" target="_blank">📅 08:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140316">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrSKjIT6q5_IJYrM320FVrwBfS40IevlOLe3dLaXDxlUOmpA4zG0pQhz-y9pQT3gWbxskrMAFKtSl8ePkCPYHIM8McNzTQ1CDoyPIwM1OI67XMPYnUJZFgM_vD0nXXdDmQ0Jl_VvHpd66GOZ0v5byi6PRkeZ1ohEFTamq6YUnTtG60GeB6fXuyco93o4kUChpaPIik2pnIfSHisvwAjB5mzZ9wOUGnd10D--rS06G5zNp84Ibqpfh9iz5L1OfeIB8cSBd33Ry5M39q-cILru5gVnyd8DMUBeJM_fbjO4tKQ5olM3qRDsbE-hoMVe1N3pdSv08R1fyYuENC5yTSkGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ منتشر کرد:"دونالد ترامپ در جنگ با ایران پیروز شد."
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/alonews/140316" target="_blank">📅 08:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140315">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:  آمریکا انتقال بخشی از سوخت‌رسان‌های خود را که در فرودگاه بن‌گوریون مستقر بودند، آغاز کرد
🔴
کانال ۱۲ اسرائیل مدعی شد: نیروی هوایی آمریکا انتقال بخشی از هواپیماهای سوخت‌رسان هوایی خود را که طی هفته‌های اخیر در فرودگاه بن‌گوریون مستقر بودند، آغاز کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/140315" target="_blank">📅 08:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140313">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/615b2fdbae.mp4?token=AKGJaIuf_QulS8nk_c5wgOfOJcVpN5KH8kgdzN4krt8RgLf5Ry-C-u5xGD0FBQxzllQD4oO8hRWSmZ5DbJbHYEaIcX3Lx9eY53qC-QCNmOQIu6hcosu5inerhQOxIV8nh4gaXawBG20vApeU-qluEFKqzIjwooviW75COU_rdAl1BHsrzt3Pes94653F1w42RueWOIHzdIDbjwHhjtnkHkgIMYHVdGrsod3XIi-6fv3Mz-HLzolBdvUYe-OWtUCGMrRidUGIZfrUtF-gXfEVDP_Q4ZoX12D6sQ6vNIcF4R41fgFSfzg-jlTv8hPxwqDmFxLtskolrHvytyXUSme_9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/615b2fdbae.mp4?token=AKGJaIuf_QulS8nk_c5wgOfOJcVpN5KH8kgdzN4krt8RgLf5Ry-C-u5xGD0FBQxzllQD4oO8hRWSmZ5DbJbHYEaIcX3Lx9eY53qC-QCNmOQIu6hcosu5inerhQOxIV8nh4gaXawBG20vApeU-qluEFKqzIjwooviW75COU_rdAl1BHsrzt3Pes94653F1w42RueWOIHzdIDbjwHhjtnkHkgIMYHVdGrsod3XIi-6fv3Mz-HLzolBdvUYe-OWtUCGMrRidUGIZfrUtF-gXfEVDP_Q4ZoX12D6sQ6vNIcF4R41fgFSfzg-jlTv8hPxwqDmFxLtskolrHvytyXUSme_9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
: آیا خبر جدیدی در مورد تنگه هرمز وجود دارد؟
🔴
ترامپ
: اوضاع به خوبی پیش می‌رود.
⠀
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/140313" target="_blank">📅 03:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140312">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc90d74a3.mp4?token=Fp2mSvl2Po3Kg2yWFWEntNjkw9kfnI8YheAGBRbysaV86LeH-VAAPdsMdN2QJo7hBYUyhcD0e2kXuk1DbTxZb-CuvvARluaO6I1M7HO9fItt9xEb8zNB70-xXIIKN0EkiQmXfthlR0t2q0KY53VXk4bMkCFl9FUMHqrrG_TrI0vRyIpktCxoeRrLoTrGuyMKJi-qdSzn8ZOenOvPRp6v_JIZqhsOGwwMNhyjTf9BTbOvBtB2syfa4fb7zJ2_6dsfyhl_i7CgALrtUW2Jx359uvsd4oj2HHuQZsKm8gFcTO83WLZ1SKdrVq_LbuyCQcMSOk8AAcUYeoQFLOQIiDxMbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc90d74a3.mp4?token=Fp2mSvl2Po3Kg2yWFWEntNjkw9kfnI8YheAGBRbysaV86LeH-VAAPdsMdN2QJo7hBYUyhcD0e2kXuk1DbTxZb-CuvvARluaO6I1M7HO9fItt9xEb8zNB70-xXIIKN0EkiQmXfthlR0t2q0KY53VXk4bMkCFl9FUMHqrrG_TrI0vRyIpktCxoeRrLoTrGuyMKJi-qdSzn8ZOenOvPRp6v_JIZqhsOGwwMNhyjTf9BTbOvBtB2syfa4fb7zJ2_6dsfyhl_i7CgALrtUW2Jx359uvsd4oj2HHuQZsKm8gFcTO83WLZ1SKdrVq_LbuyCQcMSOk8AAcUYeoQFLOQIiDxMbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای امنیتی عراقی در بغداد مستقر شدند تا جلوی اقدامات احتمالی گروهک مقاومت علیه عربستان رو بگیرند
🔴
نخست وزیر نیز دستور اماده باش داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/140312" target="_blank">📅 02:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140311">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4300472.mp4?token=J-3mqBIQkJim6cudi04aP4taTtzqagOJbVcY9SZpqPdXfrONiYJucz9TM25t17V0wldMfSCPgUKG5SUy0twTh32bVrqwQls3Kd76hrcm-hm7yIunUdnMaIHZ77g2x7JN7UNpvxT2VDh5JMLGFM1n5U_QgWUWgBHquL1uwAcPQUhNjhRGPUUHvAlZeYlIZJpVf6fUicLxYJwjLMerNZBb5fKLE5gPIhoKIOhBluMfd_EPbTyRwpG1CdM9VaMBtcfyk7qH_4z2iWfK1fE1g_npzZgEbK7FxdCYg4_SQsi01gqJc_Lx8JXoYDN0JMM6ShC9h-OoewA5t1KUXpePD4dOGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4300472.mp4?token=J-3mqBIQkJim6cudi04aP4taTtzqagOJbVcY9SZpqPdXfrONiYJucz9TM25t17V0wldMfSCPgUKG5SUy0twTh32bVrqwQls3Kd76hrcm-hm7yIunUdnMaIHZ77g2x7JN7UNpvxT2VDh5JMLGFM1n5U_QgWUWgBHquL1uwAcPQUhNjhRGPUUHvAlZeYlIZJpVf6fUicLxYJwjLMerNZBb5fKLE5gPIhoKIOhBluMfd_EPbTyRwpG1CdM9VaMBtcfyk7qH_4z2iWfK1fE1g_npzZgEbK7FxdCYg4_SQsi01gqJc_Lx8JXoYDN0JMM6ShC9h-OoewA5t1KUXpePD4dOGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خرازی: فتوا میدم بی حجابارو بکشید، لشکر کشی کنید و برهنه هارو به قتل برسونید اگه دولت اومد اونارم بزنید، این دولت شیطانیه و زیر دست آمریکاست، اسلام همینه، باید ضربه بزنیم و ضربه بخوریم
به گفته خود خرازی، وی با مجتبی خامنه‌ای ارتباط فامیلی و ۴۰ سال رفاقت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/140311" target="_blank">📅 02:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140310">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رويترز به نقل از منابع: ترکیه، عربستان سعودی و پاکستان امروز جمعه در عربستان سعودی توافق‌نامه دفاعی مشترکی را امضا خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/140310" target="_blank">📅 01:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140309">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljqWXRpmR9isENZtNFuOB9Yq6XRyvHuS-oMq6_N6223sgiprN1RrvvkE35tbvGzlY3wBw4oG1X6otNF-BYz9Jlt4ywCa9zY88MVh_trl52-svxDpm6bud-Pjfo8vGd0rz3l2qf7tQolV7g9n_e7G_U9vyhJJufgVAM-HMHYwsCH9CC-4Metwt_S3wrqRkjSv0PTZLHn-sMl_-Xb_QCK96Hm1Jynd9HMh_1K2vRAsS5zOM9NfmlBkT9knfpso5HJqS_CBoq-jTjJyDuGurFM1jMP0HQhtKmkq14bWn6YE2FtgRxU6nnAzbLRxKTopceDkQ8QfOADWblQ1xc34jRNwgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش کانال ۱۲ اسرائیل، نیروی هوایی ایالات متحده در هفته‌های اخیر، با توجه به تحولات امنیتی جاری، شروع به انتقال تعدادی از هواپیماهای تانکردار خود کرده است که پیش از این در فرودگاه بن گوریون مستقر بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/140309" target="_blank">📅 01:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140308">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVARVplJboUsWs1v-_vV5edypM_wy3S0jI40fbPvBjnmZzYSQgkllL6GBronUdi2otZl7FTTf2NgNdcODMRFAnkVbm2dAOiCwFK6RuiE7RpCBUTOZH3HMSvjw-pgGBk0Kr-XaNawuB3wdhXqTRTmH1ZLCzdYoW9aBnDbEz1YKyAfH0-cCfxs0LOv_AZqEiJkoAEjk9nsQzDT5pIA1HMG2VbiOR9olklSxd1TuJmLcsGmtQCRU3MH7lLM1pL1vabOXQ0_7mOnB95Tp2-zuOsRR3cMDulc46h-LiTw8Ckpif32TBh0VS2z2cmauyFti0MdIHxcdXL6BgR7l74xQJanBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باقر خرازی:
حزب اللهی‌ها تو مملک
حمّال
قدرت دیگران شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/140308" target="_blank">📅 01:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140307">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8df7fc98fb.mp4?token=KMpqnDfmveofiiFsASXxDybjyN7T3-hf1buV_TXNJibRmZTgiA7CP95DtAIfsrpJM9CphMf8nR1o_Q3uMKmIu7HBV9c3nQQgFXeBDlQ8slkx77E-5b0GRIn8bFUvw9v8ALcetl8rUC3sLORX5xDDXT8g3jjtM1shIrGp0VTTOvCnBTKs5mVGec-4x5e0ZT6VugkL2Bz5V5ufgSCXh8tpjyDiWFf1uLhrhxom602I5uIdv9CcUJ0lKVaLq74gm3OjAhQOf9ytss2ZZYThMfFXZXlJLNFc2gfDuug7vpJPGZ4pG6uYMjB_ujk1mbfUcPFqXGhR99dO_pPatEsKlkp74A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8df7fc98fb.mp4?token=KMpqnDfmveofiiFsASXxDybjyN7T3-hf1buV_TXNJibRmZTgiA7CP95DtAIfsrpJM9CphMf8nR1o_Q3uMKmIu7HBV9c3nQQgFXeBDlQ8slkx77E-5b0GRIn8bFUvw9v8ALcetl8rUC3sLORX5xDDXT8g3jjtM1shIrGp0VTTOvCnBTKs5mVGec-4x5e0ZT6VugkL2Bz5V5ufgSCXh8tpjyDiWFf1uLhrhxom602I5uIdv9CcUJ0lKVaLq74gm3OjAhQOf9ytss2ZZYThMfFXZXlJLNFc2gfDuug7vpJPGZ4pG6uYMjB_ujk1mbfUcPFqXGhR99dO_pPatEsKlkp74A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
🔴
سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود
🔴
وزیر دفاع با معاونینش در جلسه حاضر شد؛
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/140307" target="_blank">📅 00:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140306">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIZaMrxC5w0TYSRQzCdoSgWDvNAJUQQoglmKK-kuQe7Hte--HeFfaUpxHCTEn5HD-3H-AvDlKR1btoUiqwDICt_ngAMwrXaRV6DpqEIQHY8k7dHLmfI-p2CRMEdnPM6tKncMH_jzDm3a6lE9W7xqJO4shNk_04oZQUJareYWKsUsK7UZDbzDBav-dRtngHju1Crq4oqOBpoSyvw5YffvV4eW3A-VJ2X_G3e9uRGILLfLwG5OchkKEmV-rD-uJnX_y5AObt1IngvdSuNQVLnhBQF-SiyFcqERwXEDz0qjYA9yG_-5G9XbFxLQVKH5rZNCsIZ18-DYzhIR7ZovoYbKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش آمریکا شروع به عقب‌نشینی هواپیماهای تانکر از فرودگاه بن گوریون کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/140306" target="_blank">📅 00:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140305">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pD09vQMyOHIK4cEshYzJ99e2lThhE5y6kK2mFiAfttOfFifoRRdNgFnGgPCha1GNpF4AAIL6LRZXIfVBwW1viNwwd7LWmjhPzyQXH8O2hNkjLetrS2_SpfBLUcYR4wL7molg-lJ9ttbHYwpZqekSEjSgkSXJ2neQ_oaVIhMSGdPrDvC8PeePn2bncVDqqV4XvoJezttEYeZtWSirOKhUmgDr4ALFro0-O1O-KBt-sZotAVB5FlzVwrtQ9FhxrVglF4nmwpvaTgpVSvq-SWogE1izWNvWLlMpAwRshY2y2h-NbQ5hMvs8w585bYyr71HfiB0B8AU0Z7TdMReijCX6tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام‌جمعه رشت : دستور دادم عکس هیچ زنی رو نزنن سنگ قبر، نا سلامتی مسلمونیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/140305" target="_blank">📅 00:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140304">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ: ما اجازه نمی‌دهیم جمهوری اسلامی به سلاح هسته‌ای دست پیدا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/140304" target="_blank">📅 00:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140303">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
رسانه آمریکایی MS NOW: عمان با چارچوب یک توافق موقت با ایران برای بازگشایی تنگه هرمز موافقت کرده است.
🔴
هدف از این توافق، فراهم کردن زمینه برای برقراری آتش‌بس جدید و ازسرگیری مذاکرات هسته‌ای میان آمریکا و ایران عنوان شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/140303" target="_blank">📅 00:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140302">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها علی‌رغم محاصرۀ دریایی آمریکا قادر به کاشت مین در تنگۀ هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/140302" target="_blank">📅 00:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140301">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ: تنگه کمی بازه
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/140301" target="_blank">📅 00:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140300">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ درباره مهمات: «از نظر ذخایر و تأمین مهمات، در وضعیت بسیار خوبی قرار داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/140300" target="_blank">📅 00:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140299">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4VDT5OOkk6UNlKd-DXusqfr_A2cPh0Ou0Sj4t9-jKqDef8Bd1Mz5k6rLKz5JL9olvPbxDRJ8EilIuXeLGBIcGoxfxEAn40nA9FFb_yO3EyAdt2Hl5GPXSoOsuE47qQevGmPwvKj2F8mxnIfI-gffweYp3QienQ0M91juOKe_fPeAWQszp17q4kiegYJl8D9YccDykDRK5_XW6dNerHQFkimLmJyAzKDCttxs8JWzazHupyD1kOckpb4EOyTodllH9J76Ua4v7dWz18uvvZa_GQrrpuVAd2582gysoJfEILj9nCNH6KHswF1DdTPy5SiFhSTmb8r4ikfPs2qC6br3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت ۸۳ دلاری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/140299" target="_blank">📅 00:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140298">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ : - فکر می‌کنم جنگ به‌زودی تموم می‌شه؛ بعیده بتونن این وضعیت رو مدت زیادی ادامه بدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/140298" target="_blank">📅 00:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140297">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815c703151.mp4?token=Vnv54sAAWq8kl-wmguUS-x6qZ06urKFzzNvEyB9uSByZ02Z46S61VfNejaHlZP2-NzdGXW87KyKBiCuFfltNHJrjA5I1k1R6KDHLsFqYcvuzlTFDWI_plFo_P_mkDJmlJOSeBbE7P83VmCAmc0VEphqL2ocU27_FItwa2qi-UkUNrNPwyXyCa3B3PkIBNZywcUD9UaloEbdrA_oMK8tq-03MLIMWDRuarkNNKxzITTo8KKkTckXV96UG6bw-m9N4kKB0m6_HPt7XwES3c0yK3-sEutl7qnu7Bn4hMvUUL1qyPR1vZl1gdpNkF9ib0oimKvUoR9Wgiur4UOEKw-MwYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815c703151.mp4?token=Vnv54sAAWq8kl-wmguUS-x6qZ06urKFzzNvEyB9uSByZ02Z46S61VfNejaHlZP2-NzdGXW87KyKBiCuFfltNHJrjA5I1k1R6KDHLsFqYcvuzlTFDWI_plFo_P_mkDJmlJOSeBbE7P83VmCAmc0VEphqL2ocU27_FItwa2qi-UkUNrNPwyXyCa3B3PkIBNZywcUD9UaloEbdrA_oMK8tq-03MLIMWDRuarkNNKxzITTo8KKkTckXV96UG6bw-m9N4kKB0m6_HPt7XwES3c0yK3-sEutl7qnu7Bn4hMvUUL1qyPR1vZl1gdpNkF9ib0oimKvUoR9Wgiur4UOEKw-MwYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :
- فکر می‌کنم جنگ به‌زودی تموم می‌شه؛ بعیده بتونن این وضعیت رو مدت زیادی ادامه بدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/140297" target="_blank">📅 00:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140296">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkzlkjgKrv-GUTfpayZvgy0D5xv8uE-cXEodcLg1bvW-Nh11Xv5RYFohXStBliE1plsYy82qizabvus9rDSVkGyAbxK0Bc8mzZpj6herjWjuBfl2NfEIylfHsg4cMxHl7sfnpwMgrGmeiOPgiElYue6bniEgyISEq5SvQIBSmNQQfnKCvQOVur38WiCrV4QUhXj0vcSSoAuh2n4EyTJTIO54t9U2LYdC1ygbTCwcq8dPcKIaZR25btgxZOwt9KIKmB4J4Pn6oW3U9ndzafLlL4WGIEBfehObw70oO6BofMaP9msWX1z7bzSmwBe1LMF9iKR-JEFu6oZNOF-nV91BOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن رضایی: اجازه باز شدن مسیر دوم در تنگه هرمز را نخواهیم داد
🔴
‏اگر محاصره ادامه یابد، کشتی‌ها و نیروهای آمریکایی با خطرات و تلفات جدی روبرو خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/140296" target="_blank">📅 23:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140295">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
سی‌ان‌ان‌ به نقل از منابع: ترامپ ماه‌ها است از مشکلات احتمالی مربوط به کمبود مهمات آگاهی داشته و گزارش‌ها برای او غافلگیر کننده نبوده
🔴
ترامپ از این که این اطلاعات در نقطه عطفی از درگیری با ایران افشا شده که او می‌خواهد موضع قدرت را به نمایش بگذارد، خشمگین است
🔴
افشای اطلاعات مربوط به ذخایر، از سوی مقامات ضد جنگ درون دولت صورت می‌گیرد که مصمم هستند ترامپ را به خارج کردن از درگیری با تهران سوق دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/140295" target="_blank">📅 23:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140294">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8ZJWGquu2CE8tWJGepJRj-X7KqE3Oyq_Bw2n2BuN9KgUPvTNEpwqZaY9wC6j_dn_ZDXAaX7FlLdEiz2y3f6QBOBPIblCKhKnJIDg3hNbzsddaGoNHHPbCuiWttWgE4Sf-nzrrvi1yWq-H8vMRw8hikQIDUAjgfpHNNzTISQrp7duxGWvbdhha3iYaCSvXVjAxXtvSwZ9VbG0p8WSY82LndF9N_-2TUYiNmE8Gt3eUkJo2LlrphqS0PKS2tEvigZo-ePcsYTAVZG6K2LrlDd_yQ58wnJ5xW0ge4CIjEDN-AEl9N4a8Tp3JtyLMFmVlL0sNbAEN2Fb_3km3xyZCk37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال: برای سناتورهای بزرگ جمهوری‌خواه، دوستان من «همه»، لطفاً توجه داشته باشید که نامزد کمونیست دموکرات مجلس سنای ایالت میشیگان، عبدالرحمن محمد السید، به عنوان شاید مهم‌ترین نقطه خود، بر لغو قانون فیل‌بستر تأکید دارد.
🔴
دیروز تماشا کردم و او در مورد لغو آن دیوانه شده است.
🔴
اگر موفق شود، دموکرات‌ها ۴ سناتور، ۸ نماینده کنگره، بسیاری از رای‌های انتخاباتی و مردمی، و یک دیوان عالی با ۲۳ قاضی را به دست خواهند آورد و من، متأسفانه، با وجود کار بزرگ که انجام می‌دهیم، آخرین رئیس‌جمهور جمهوری‌خواه خواهم بود! پرزیدنت دونالد جی. ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/140294" target="_blank">📅 23:49 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140293">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏
👈
کانال کان اسرائیل:  رئیس موساد، رومان گوفمان، رئیس اداره اطلاعات و مسئول پرونده ایران در این سازمان را برکنار کرده و آن‌ها را مسئول ناکامی طرح میدانی برای سرنگونی حکومت ایران دانسته است؛ طرحی که پیش‌تر به دونالد ترامپ ارائه شده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/140293" target="_blank">📅 23:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140292">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372d7e9f3e.mp4?token=ZVKcDE7bSj-DyL9KyT0564V8fB7rk30-r2DTJ0MkU3UAoGnIMj_u1p3YKXnL5sx6u-G8exUPHb5Z6fK_I_UzPde_ax3WXbqaKClDKBr4vICLaB4Hr9B4p6ZPZIhWEjiVHqqA_MpVFS_BDAYCTIBv7rZSFM9bsWl8eA6cY-7a3PbX8vuTCJLukRP8vE2PmQ0RfgXI2Jylbgm2Z-nRAdKuWMjrISi9GuYqPSvQneQ6KvahTdbidHlyWUk7jws8O5u4nQIiBNVW_glWiKXV7nSxRqFHufSv2Owo7KwzzUimb_2CiCFnUfJ4KgKmVrrTEU0_t1GQazV09XFD1UElZc5fSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372d7e9f3e.mp4?token=ZVKcDE7bSj-DyL9KyT0564V8fB7rk30-r2DTJ0MkU3UAoGnIMj_u1p3YKXnL5sx6u-G8exUPHb5Z6fK_I_UzPde_ax3WXbqaKClDKBr4vICLaB4Hr9B4p6ZPZIhWEjiVHqqA_MpVFS_BDAYCTIBv7rZSFM9bsWl8eA6cY-7a3PbX8vuTCJLukRP8vE2PmQ0RfgXI2Jylbgm2Z-nRAdKuWMjrISi9GuYqPSvQneQ6KvahTdbidHlyWUk7jws8O5u4nQIiBNVW_glWiKXV7nSxRqFHufSv2Owo7KwzzUimb_2CiCFnUfJ4KgKmVrrTEU0_t1GQazV09XFD1UElZc5fSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ارژنگ امیرفضلی: «بالا برید پایین بیاید، برید چپ برید راست، مذاکره کنید جنگ کنید نکنید...
🤔
هیچ چیزی به قبل از 18 و 19 دی برنمیگرده.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/140292" target="_blank">📅 23:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140291">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
مقام آمریکایی به روزنامه الجروزالم پست:
هر مسیر موقتی بدون هیچ مانعی خواهد بود — به این معنی که هیچ تاییدیه یا مجوزی و هیچ عوارض یا هزینه‌ای وجود نخواهد داشت. تنگه هرمز یک آبراه بین‌المللی است و هیچ طرفی کنترل مسیرها یا توانایی عبور از آن‌ها را در دست ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/140291" target="_blank">📅 23:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140290">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
خبرنگار حوادث:
توی شاهرود، یه پسر 25 ساله بخاطر اینکه یه مدت از باباش موتور می‌خواسته؛ باباش با سنگ میزنه تو سرش و به قتل میرسونتش و بعدش جنازه‌شو میندازه تو یه چاه 40 متری!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/140290" target="_blank">📅 23:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140289">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMJDEPY3hEmtNmxTTFxcUaoGvTJVGk2Nu_c0ulm60Ez_ecufzrEFtejH_5uGEHgOqYhJwSvPGC4qd_SvOqfDshOiC2sDLvCokm40KGa9rptONhSSnsxCkoMIF51DTdERUbIJCTciz9mHfiSmD-nCh68ZiXVedvvY3fOQ9uyHqNWTVXbua4ROaMDsuXVoJUjk0VAIsXUbIx1eXW_xH5ynx3DzNk17iCgajzzlSHD03o1a8hZAS0dUWBFVq3hkY3bwpUj9Y1O1YLFSFsQ0C9LREClHgsg9wF6FD8XDNVqmFHXCuKxWJX4M8ab0ftoPLlM6aiNhBLPIQ5QYNdSUDQ1ndA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از دبیر شورای عالی امنیت ملی که از ۳۰سال قبل لباس و شلوار و حتی مدل کمربندش یکی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/140289" target="_blank">📅 23:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140288">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
خبرنگار حوادث:
یه مرد ۳۸ ساله میره کمپ ترک اعتیاد تا مواد مخدر رو ترک کنه. بعد از دو ماه ترک میکنه و برمیگرده خونه. وقتی میرسه خونه میفهمه وقتی نبوده زنش ماشین و تمام طلاهاشو فروخته. همونجا بنزین میریزه رو زن ۳۲ سالش و آتشش میزنه. بعد پشیمون میشه و سعی میکنه با پتو خاموشش کنه ولی نمیتونه و زنش فوت میکنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/140288" target="_blank">📅 23:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140287">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUj8aR5WvCC4u60QHo3Ef_15T2ggg4k8kJIsmiz9IDFnSOCcULgLF5XJDAng1cxOjATFQSU1c9_f6KJOCnJij8mkl8rf3325aOye8ahwfqqSkAvIQVlTTUYRsS0I3lgFMtdm7jIzw8oYkFd5HgdfeFwVapkKLkjBqIMgs1YKejh_3b8rxIE_LXG3EbD5WODL0X8l2vl1vcu5xaO3SCcFoSYYE39MQS-9ZuvxM1XxaRruac8wpO0V5g6On1j_DUaZfKqD7pk0QS8iilFmzeaMcenwNo4hGjlP9G9aaR3dTEmKyVzRa02bF2MEjNvGUDWyRJOOe11l44IcH2tcQ6MYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جادوگر معروف غنایی:
ایران در نهایت آمریکا را شکست خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/140287" target="_blank">📅 23:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140286">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ امروز با بن سلمان در مورد موضوع ایران گفت و گو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/140286" target="_blank">📅 23:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140285">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9vudsCZrGc5ib_T8Y6mSxztCWhYVLg5H0fjWc8EvBzJ5lE-ZWhiVwFCVL0i0ug-Bsbc5fokKBEB1SDHFKq922EOWpwaJRCPaLBVhrFfR1DW-n3EhDfaWSjdVa9a1WVzkGsp6mRdTvWtm2phP54ULGyEbVLPhun1j4kIm2mzoiAvgnTiXAQ6ezWHSWNtSIO1_n45oQfs8kXcAP7Ividv2LoE3285cpTyaX8CxtA2F2G-JnRY-MceuOfP7CscJlgmPh2MFJL81DWq8M1AB2Np7RyXGLBcvgl4E_5JNsWrKCGC8vTOi4DTYsj4p2gkCW9tiO2DizJNUxHaD2VgWJ1t8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پروژه ۱۵۰ میلیاردی به واشقانی بدون یک روز سابقه کارگردانی!
🔴
مجید واشقانی ملقب به خایه مال بدون تجربه ساخت تله فیلم، سریال و حتی فیلم کوتاه، قرار است برای اولین بار با این پروژه پشت دوربین قرار بگیرد. تهیه کنندگی «بریجتون» را جمال گلی برعهده دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/140285" target="_blank">📅 22:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140284">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏
👈
المیادین: عربستان دستور پنهان‌کاری درباره تلفات نیروهای خود را صادر کرد
‏
🔴
یک منبع نظامی به المیادین اعلام کرد «عربستان سعودی» دستورهای سختگیرانه‌ای برای مخفی نگه‌داشتن اسامی و شمار کشته‌ها در حملات نیروهای مسلح یمن را صادر کرده تا روحیه نیروهایش را حفظ کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/140284" target="_blank">📅 22:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140283">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c59229eed.mp4?token=a7SFTar3mDUW65bMEndLaWCaPrVmymcCDrUiV9F1wE1D6qDrqFQtVE2C0Dic_IoSH_npVQAI883bB8uznjCDq00cBOiEuM8ldY3xc876HTIdWX4Z5Ip2WpPN_5iTkJBc25fLffsUf-AFsNOQZ7ONQqLoUV3viDh2Z3HTF0Ydlxp-uGlRl4iItPmqXAUA0j9JPEN6KaYAvwGBg5F8KdRkKKtiZ6iu42Y1PQkMS8SIRyUTxseP1N2BmPRvqw2JKKAeQiomA_AWNSDLABtI6oRB1R8P9GAqvTE_6s9auCpNoZrgi_rb6JA4wKqPMsfe6cLZ83m5KZelOZBcfjzPSP5PDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c59229eed.mp4?token=a7SFTar3mDUW65bMEndLaWCaPrVmymcCDrUiV9F1wE1D6qDrqFQtVE2C0Dic_IoSH_npVQAI883bB8uznjCDq00cBOiEuM8ldY3xc876HTIdWX4Z5Ip2WpPN_5iTkJBc25fLffsUf-AFsNOQZ7ONQqLoUV3viDh2Z3HTF0Ydlxp-uGlRl4iItPmqXAUA0j9JPEN6KaYAvwGBg5F8KdRkKKtiZ6iu42Y1PQkMS8SIRyUTxseP1N2BmPRvqw2JKKAeQiomA_AWNSDLABtI6oRB1R8P9GAqvTE_6s9auCpNoZrgi_rb6JA4wKqPMsfe6cLZ83m5KZelOZBcfjzPSP5PDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیگه فیلم ایرانی هم خواستید با خانواده ببینید باید سانسور شده بگیرید:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/140283" target="_blank">📅 22:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140282">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79cb41dc94.mp4?token=n_roZlqQohkjRloudeo1gSomaUdKdd9kjpIdWhvsjBR3k9_52WvHcPMeQQe-IQ4NdHyqS7dDXtaBoPDkRM2f2u8gvARdOYv6KEhUR1hA6Cxnwlvc23ZLVuhADeRhyHJ_qsfJGhWAFcrXWu78DwHMWhhXGX8V1FbreC6cmPR3c3ROT25EK5lb0lI3tu_v1kV-MGrLaINQ7opic93UmLojfNLEfxVDoIgXHZX5TuAPP52DC1UlrktzhdR-SX9z6cUtD0Qf7AailvVLU5qRja8-4Ebe2sKYy-k0_aEYM935XVDtzX9OvXC6kxQVZReR1UcAXP41eGy1v9e7pBMBea5NSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79cb41dc94.mp4?token=n_roZlqQohkjRloudeo1gSomaUdKdd9kjpIdWhvsjBR3k9_52WvHcPMeQQe-IQ4NdHyqS7dDXtaBoPDkRM2f2u8gvARdOYv6KEhUR1hA6Cxnwlvc23ZLVuhADeRhyHJ_qsfJGhWAFcrXWu78DwHMWhhXGX8V1FbreC6cmPR3c3ROT25EK5lb0lI3tu_v1kV-MGrLaINQ7opic93UmLojfNLEfxVDoIgXHZX5TuAPP52DC1UlrktzhdR-SX9z6cUtD0Qf7AailvVLU5qRja8-4Ebe2sKYy-k0_aEYM935XVDtzX9OvXC6kxQVZReR1UcAXP41eGy1v9e7pBMBea5NSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تندروها با انتشار این فیلم مدعین که بعد از جنگ ۱۲ روزه؛ پزشکیان گرای زدن خامنه ای رو به آمریکا و اسرائیل داده.
پزشکیان بعد از جنگ ۱۲ روزه:
من همش نگران رهبر بودم؛ چون رهبر ستون خیمه ست. اگه بزننش ما خودمون به جون هم میفتیم و از هم میپاشیم دیگه نیازی به اسرائیل هم نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/140282" target="_blank">📅 22:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140281">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cdcc1be4b.mp4?token=SWmNaqcXtY2s2cPpYjMfvwQQ9TehM7pUxQZcatwmenbCityj5Mgx_fSuxnHXU7eIFoVi-qL9urYgsaojNREZWFebJwWVSRtXYr8jRGnfhHIyR0JGVmQo-S0Zd1uggZaEnPu5h-yB9p7OIGj2y1PSYLFK4RLY4TdSy5eJFF8GUWlmBZMxV-hbEfwpPNS8yp_WoKtptVb7Si6YlweMmfnUA_lHHXaP_49zASC3IBCYm7AW8UYHJelH8TecG82o29lemwEcd7TMqNeEcybS8rOM_KNkO7s-GGOBlCxT3YZYQOTzhtcAsEbvr6ITVFl9SGHfpX7DTs-xe5yVnyxMdnzg_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cdcc1be4b.mp4?token=SWmNaqcXtY2s2cPpYjMfvwQQ9TehM7pUxQZcatwmenbCityj5Mgx_fSuxnHXU7eIFoVi-qL9urYgsaojNREZWFebJwWVSRtXYr8jRGnfhHIyR0JGVmQo-S0Zd1uggZaEnPu5h-yB9p7OIGj2y1PSYLFK4RLY4TdSy5eJFF8GUWlmBZMxV-hbEfwpPNS8yp_WoKtptVb7Si6YlweMmfnUA_lHHXaP_49zASC3IBCYm7AW8UYHJelH8TecG82o29lemwEcd7TMqNeEcybS8rOM_KNkO7s-GGOBlCxT3YZYQOTzhtcAsEbvr6ITVFl9SGHfpX7DTs-xe5yVnyxMdnzg_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: سایپا و چند شرکت دیگر هم مثل ایران‌خودرو واگذار خواهند شد
🔴
رئیس‌جمهور: کارخانه ایران‌خودرو را که واگذار کردیم، وزیر اقتصاد دولت استیضاح شد.
🔴
وقتی اعلام می‌کنم که ما هر کاری می‌کنیم، یک مقاومتی بر علیه آن وجود دارد دقیقاً همین موضوع است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/140281" target="_blank">📅 22:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140280">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkYNmx2YL28RdrncYYHlMN5MWYuSuDgWzUzB4JGSvvW0jGY0FfuC-9mwTYbfgxJ0YljQA9Nw-ULOl21BzW1Wc8KuG5LAKXHfCNY_xYBmZnfECBrxhOKHHh15vaF5XoAT9lzFFB_qnrmuuSEB0EDPw6xPDgvKwcWfQX7hvFh_Jyh5ErzXizY3pEdwEPXSuUCJTboHfJpILwM_bzh1W-bGSMvEBurQlzUZQ2nyuXdh0z018PQfflMZ8tI9-h8sJkFXC_yGjY_eCYu3FUX049rM8jwxN-6e_0Ak4WOsP1jxR7nk704Vo0MH9za1pqf2OzmLIzFm6btNeiWJHLG38UmLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خرازی قبلا هم گفته بود میخوام تیم منچستر رو بخرم اسمشو بذارم خیبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/140280" target="_blank">📅 22:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140279">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
پزشکیان: باید افراد توانمندتر، داناتر و کارآمدتر را به کار گرفت، نه افراد سیاسی‌تر یا ظاهراً حزب‌اللهی‌تر را.
🔴
قبلاً می‌گفتند تعهد مهم‌تر است یا تخصص و پاسخ می‌دادند تعهد؛ اما کدام تعهد؟ تعهد واقعی این است که اگر کسی تخصص ندارد، زیر بار آن مسئولیت نرود و بی‌دلیل نگوید من متعهدم، سپس کاری را که بلد نیست بپذیرد.
🔴
اکنون ظاهری از تعهد به خود می‌گیریم، اما کاری را که بلد نیستیم بر عهده می‌گیریم، ضرر می‌دهیم و صدایی هم از کسی درنمی‌آید
🔴
مردم اصلاً جنگ را احساس نکردند؛ فقط زمانی که جایی را می‌زدند یا تصاویر را از تلویزیون می‌دیدند، متوجه می‌شدند اتفاقی افتاده است.
🔴
این وضعیت به برکت مدیران، استانداران، فرمانداران و هماهنگی وزیران ما شکل گرفت. چرا مردم قطعی برق را احساس نکردند؟ بسیاری از نقاط مربوط به نیروگاه‌های ما را زدند، اما مردم احساس نکردند مشکلی وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/140279" target="_blank">📅 22:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140278">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری / بر اساس گزارشات حوالی ۲۱:۴۰ صدای ۴ انفجار در قشم شنیده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/140278" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140277">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پزشکیان: سازمان تأمین اجتماعی این همه کارخانه و شرکت دارد، اما اکنون قادر نیست هزینه درمان بیمار را پرداخت کند.
🔴
مگر می‌شود کسی این همه سرمایه و کارخانه داشته باشد و در نهایت فقط سربه‌سر کار کند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/140277" target="_blank">📅 22:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140276">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
پزشکیان: از قِبَل هر کدام کارهایی که می‌کنیم یک عده منفعت می‌برند و پول نصیبشان می‌شود.
🔴
طبیعی است که برخورد با این افراد صدا ایجاد می‌کند.
🔴
هیچ‌وقت هم نمی‌آیند بگویند شما جلوی کسی را گرفته‌اید که در حال سوءاستفاده بوده است؛ می‌گویند فلانی را که مثلاً حزب‌اللهی بود کنار گذاشتید، فلانی را که متعلق به فلان جناح بود آوردید یا فلانی را که رانت‌خوار بود، به کار گرفتید.
🔴
یعنی به شکلی با شما صحبت می‌کنند که نگذارند کاری را که باید انجام دهید، انجام دهید.
🔴
اصل ماجرا این است که آن کار انجام نشود؛ بقیه این حرف‌ها حاشیه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/140276" target="_blank">📅 22:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140275">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
پزشکیان: اگر این اقدام [اصلاحات اقتصادی] انجام نمی‌شد و جنگ آغاز می‌شد، قحطی در بازار قطعی بود؛ چون دیگر ارز ۲۸ تومانی نداشتیم که پرداخت کنیم و با ارز آزاد هم کسی کالا وارد نمی‌کرد تا در بازار بفروشد.
🔴
اکنون همه کالاهایی که مردم می‌خواهند در بازار وجود دارد، اما گران شده است.
🔴
باید این گرانی را از طریق کالابرگ جبران کنیم و ان‌شاءالله باز هم آن را جبران خواهیم کرد؛ زیرا زمینه این فسادها را از بین برده‌ایم.
🔴
۴۷ سال است که می‌خواهیم درست عمل کنیم، اما هر بار می‌گویند اکنون وقتش نیست.
🔴
هر زمان می‌خواهیم کاری انجام دهیم،
می‌گویند فعلاً دست نگه دارید و هر بار هم بهانه‌ای مطرح می‌شود.
🔴
نتیجه این شده است که روزبه‌روز بیشتر در باتلاق فرو می‌رویم
🔴
ما مجبوریم اصلاحات را انجام دهیم.
🔴
اگر در حوزه آب، برق، گاز، بنزین و گازوئیل درست عمل نکنیم، مشکلات بیشتر می‌شود.
🔴
هر بار که می‌خواهیم به این مسائل ورود کنیم، می‌گویند الان دست نزنید، چون اگر دست بزنید صدا بلند می‌شود.
🔴
خب چه زمانی باید دست بزنیم؟ زمانی که خودمان غرق شدیم، کشور نابود شد و همه ضرر کردند؟
🔴
بعضی از مجموعه‌ها را واگذار کردیم، اما دوباره آن‌ها را بازگرداندند؛ در حالی که نباید بازگردانده می‌شدند.
🔴
همان بخش‌هایی هم که بازگردانده شدند، اکنون کارآمد عمل نمی‌کنند.
🔴
این مشکلی است که در نظام تصمیم‌گیری کشور وجود دارد و در برابر هر تصمیمی که در جهت آزادسازی گرفته می‌شود، مقاومت‌هایی شکل می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140275" target="_blank">📅 22:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140274">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca136c1de.mp4?token=kfGH1G05Md_q0lVoHZlTjQdLbzbl6vDxakODzRuQgqNPSbP4PJh2oPk7dMQ4wyGUnXZW9yS3oNqPt1psH1U8eh4BpYhWgD97N4gnuwYEmN3YhelwCxvINyGwgL3m6lISkLVLVEKS8Xgb2V_6AXAHajEQ3FbovdEZmjZivINVTY6l53RE5UWPUO1pXJBCnIeFa-4D_Qi5KwTKJJGibMS1UCyWXxEvMTdGskr2iz6W2VB89jqfEO3kDVyawfFVfFeUy01WLR2jX4kUFoJtXLRkCLlSGTZvBEG8JEkcK4y5LeohBmEYN9KKgGcGzC_fQhnrqVmId8UZHpIYBDqQ_SVwLrAZICg4qBDWb72M1F-b03yE_L54pHJJCY1oiiwDIQE7dld1yHJGPY4bRF13aLu-QZzMrPTbJe9IDaQAk2Oo_CbHYf5x2Yd5GniNXDwLEp1Hsq-K0BhGogWRfIKFbRsCOrpjZrLPJYqab_Ve8i4y_awh_3BtvGGmQnqVyuCFBA18I6ZwO0nO_piGHCEDVs-2LvJtPmWUY3zrveVvd8cL52yJ0oTd3M3p2V9JPk3PreYMfvsJVb3q89mzEwXNMvbCXvJ7dka14U1oUdJa-Yi4DDy-G5kVwmTpruhBFP-GGXCqir1vzRTvjpbJR-m3iDErXiV5jdJBo46oi7x6aqHa-2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca136c1de.mp4?token=kfGH1G05Md_q0lVoHZlTjQdLbzbl6vDxakODzRuQgqNPSbP4PJh2oPk7dMQ4wyGUnXZW9yS3oNqPt1psH1U8eh4BpYhWgD97N4gnuwYEmN3YhelwCxvINyGwgL3m6lISkLVLVEKS8Xgb2V_6AXAHajEQ3FbovdEZmjZivINVTY6l53RE5UWPUO1pXJBCnIeFa-4D_Qi5KwTKJJGibMS1UCyWXxEvMTdGskr2iz6W2VB89jqfEO3kDVyawfFVfFeUy01WLR2jX4kUFoJtXLRkCLlSGTZvBEG8JEkcK4y5LeohBmEYN9KKgGcGzC_fQhnrqVmId8UZHpIYBDqQ_SVwLrAZICg4qBDWb72M1F-b03yE_L54pHJJCY1oiiwDIQE7dld1yHJGPY4bRF13aLu-QZzMrPTbJe9IDaQAk2Oo_CbHYf5x2Yd5GniNXDwLEp1Hsq-K0BhGogWRfIKFbRsCOrpjZrLPJYqab_Ve8i4y_awh_3BtvGGmQnqVyuCFBA18I6ZwO0nO_piGHCEDVs-2LvJtPmWUY3zrveVvd8cL52yJ0oTd3M3p2V9JPk3PreYMfvsJVb3q89mzEwXNMvbCXvJ7dka14U1oUdJa-Yi4DDy-G5kVwmTpruhBFP-GGXCqir1vzRTvjpbJR-m3iDErXiV5jdJBo46oi7x6aqHa-2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توضیح پزشکیان درباره چرایی حذف ارز ترجیحی
🔴
مبلغ کالابرگ افزایش می‌یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/140274" target="_blank">📅 22:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140273">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
پزشکیان: ۴۸ سال است که ناظر گذاشته‌ایم؛ چرا نتوانسته‌ایم مشکل را حل کنیم؟ تا زمانی که زمینه فساد وجود دارد، نمی‌توان جلوی فساد را گرفت.
🔴
وقتی این زمینه‌ها از بین برود، دیگر به‌راحتی فسادی شکل نمی‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/140273" target="_blank">📅 22:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140272">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
پزشکیان: آن زمانی که نماینده و نایب‌رئیس مجلس بودم، یک صندوق در مشهد دچار مشکل شده بود. هر روز در خیابان‌ها تظاهرات می‌شد، چون نمی‌توانستند پول مردم را پرداخت کنند.
🔴
نه جمعیت آن‌قدر زیاد بود و نه حجم پول به این اندازه؛ اما در سراسر کشور هر روز اعتراضاتی شکل می‌گرفت. آن زمان، به روشی توانستیم آن مشکل را حل کنیم.
🔴
بانک آینده که شاید ۱۰ برابر آن، یا حتی بیشتر، حجم و گستردگی داشت، بسته شد؛ بدون اینکه اعتراضی شکل بگیرد یا نگرانی خاصی در جامعه ایجاد شود. این موضوع نیز با تدبیر و مدیریتی انجام شد که شکل گرفت و البته با هماهنگی قوه قضاییه و مجلس محترم پیش رفت.
🔴
برادرمان آقای دکتر قالیباف و برادرمان آقای اژه‌ای نیز در این مسیر همراهی کردند و مجموع این هماهنگی‌ها باعث شد بدون تنش از این مرحله عبور کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140272" target="_blank">📅 22:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140271">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
پزشکیان: دشمن انتظار داشت کشور، به‌دلیل  فشارهایی که وارد کرده‌، سقوط کند
🔴
آن‌ها همواره این فشارها را وارد کرده‌اند و اقتصاد ما را روزبه‌روز در محاق قرار داده‌اند و با مشکل مواجه کرده‌اند. اکنون در دولت ما، این فشارها به حداکثر رسیده است
🔴
خودشان هم در تحلیل‌هایشان تعجب می‌کنند که چرا ما سقوط نکرده‌ایم.
🔴
تحریم یک واقعیت است.
🔴
وقتی نتوانیم نفت خود را بفروشیم، یعنی ارز کمتری خواهیم داشت؛ نه اینکه اصلاً ارز نداشته باشیم، اما کمتر خواهیم داشت.
🔴
وقتی ارز کمتری داشته باشیم، طبیعتاً با مشکلاتی روبه‌رو می‌شویم.
🔴
باید راهی پیدا کنیم که تا جایی که از دستمان برمی‌آید، این مشکلات را کمتر و کمتر کنیم
🔴
همسایگان ما اجازه ندادند عده‌ای وارد کشور شوند و باعث اغتشاش شوند.
🔴
نه‌تنها اجازه چنین کاری را ندادند، بلکه به ما کمک هم کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/140271" target="_blank">📅 22:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140270">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
پزشکیان: از همان اول که دولت را تحویل گرفتیم، با مشکل کمبود آب و برق و گاز طرف بودیم.
🔴
به ما گفتند تا آبان ذخایر انرژی بیشتر دوام نمی آورند اما با مدیریت این مشکل را برطرف کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/140270" target="_blank">📅 22:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140269">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud7iXnXgpyGoCPQIxhALQosfazdzXIBovCsrpXJ7HikBX4B2Mq3zVEplVpEgCjIgk_kAr81aLdF8myAW8aGieB74glakFEkssuprq7BmxH4YbxPyHocyv69CgeW5SK9j4TCysoxh8Kj7wy-pYZXnvV6nlVn1TTX7S2F5VZH-cPj3trsXUemi-Izrm2Ywl4xxPIdv8TJHbsWswBGn71PYZ_Ekdag4ELDNEQHHNNyKXuNyd4ENSfzDhr5PrSyBiwskzzAuP94XUwvDV9QquEfvGQFJro_B3KuanJiHFPOloLDc6bUIjxgFMDayAJecaq-_ELJ66mptD7wwyy37vBC6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف :  یه بار می‌گن حمله بزرگ در راهه، بعد می‌گن نه، می‌خوان مذاکره کنن؛ این فقط نمایش تکراریه
🔴
قلدری، وعده‌های شکسته و خبرهای جعلی ابزار فشار نیست و شکست خورده
🔴
واقعیت‌ها رو بپذیرید و به تعهداتتون عمل کنید؛ دنیا به نمایش بیشتر نیازی نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/140269" target="_blank">📅 22:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140268">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری / بر اساس گزارشات حوالی ۲۱:۴۰ صدای ۴ انفجار در قشم شنیده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/140268" target="_blank">📅 21:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140267">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgD6Ebu5FY1_SUw3sifAVYeIZb0Sg2hK2XloKBs5eRyQBjWQr4nZgDJeV7MXT6QScLk8ISgsCu-2GNaipT33rd8imlGE81cw_4mZJ8i9r-ccIko9dYEL2gVGYIniJ7MNT_0eqm2bafI45-zuObiOrbFjI2v2X0IDYuRsh3Qy-TKOkAnpGXwwKoUI9U4ZO2nUTOQuKuQ7QkEGuaL3cyQSCyFGj9mKvj6gLQ-By7N1XY4Z-8ch8MuG5aE4vcMx7uZrVT4D3lPDkHND3-DgY0-Ta1LAT53Q2lIbwGurGgrk_i6b3XtEi5S7Z02J3qv_x7itT9Uupr6rCEV35oi6LOILJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرد ۲۶ ساله‌ای که در ولز با پوشیدن لباسی شبیه به عزرائیل و در دست داشتن یک تیغه بلند، به بیماران و مراجعه کنندگان به بیمارستان خیره میشد، دستگیر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/140267" target="_blank">📅 21:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140266">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رویترز مدعی شده ایران از کشورهای خلیج فارس خواسته ترامپ را برای توقف حملات آمریکا تحت فشار قرار دهند.
🔴
بر اساس این گزارش، تهران هشدار داده در صورت ادامه حملات، تأسیسات نفتی، پالایشگاه‌ها، نیروگاه‌ها و زیرساخت‌های آب، برق و حمل‌ونقل این کشورها ممکن است هدف قرار گیرد.
🔴
پیام روشن است: ادامه جنگ می‌تواند هزینه آن را از میدان نظامی به قلب زیرساخت‌های منطقه بکشاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/140266" target="_blank">📅 21:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140265">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزیر انرژی اسرائیل: حتی اگر آمریکا و ایران به توافق برسند، اگر ایران برای احیای برنامه هسته‌ای یا توسعه برنامه موشکی خود اقدام کند، ما پاسخ خواهیم داد.
🔴
ما به هیچ توافقی که امنیت اسرائیل را کاملاً تضمین نکند، متعهد نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/140265" target="_blank">📅 21:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140264">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3dfaf311.mp4?token=sMkf_0ick0LRE38YqF-kdp1V00aR4p5Rv40yZ5dmNHdDYosB5A7u6eaCGfwZ2qnMYQqIIIaGkFcnjD_ZdxJXpHIMBMu-085nR7xdkLvX0P8ZkPKM6aWc2OGI2Ig1yuhiNmW0pNB3xyh-AVwbGNmLbwpUT6XAm0xKHf2rbA3Ln7XHOMfjplIltBAXDvVbADKGgtmfUIUkrF2Qz8eMoOYK_hLHukoFN1jPAE8mwTzzG85i4VM0a_xqLv_-pTQQMaufh833aSSE_g1WzVPFxqTEWPzpfgiTU6w5Wj_n3g8wbIpgb_xgIKQ4DhHGXkqi9Kr9fw6dDoR5K5QE88f0rLSN3jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3dfaf311.mp4?token=sMkf_0ick0LRE38YqF-kdp1V00aR4p5Rv40yZ5dmNHdDYosB5A7u6eaCGfwZ2qnMYQqIIIaGkFcnjD_ZdxJXpHIMBMu-085nR7xdkLvX0P8ZkPKM6aWc2OGI2Ig1yuhiNmW0pNB3xyh-AVwbGNmLbwpUT6XAm0xKHf2rbA3Ln7XHOMfjplIltBAXDvVbADKGgtmfUIUkrF2Qz8eMoOYK_hLHukoFN1jPAE8mwTzzG85i4VM0a_xqLv_-pTQQMaufh833aSSE_g1WzVPFxqTEWPzpfgiTU6w5Wj_n3g8wbIpgb_xgIKQ4DhHGXkqi9Kr9fw6dDoR5K5QE88f0rLSN3jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به گزارش خبرنگار العربیه پنج‌شنبه 15 مرداد، بر اثر انفجار بمب در خودروی مسافربری ون در منطقه «جرمانا» در حومه دمشق، چند نفر کشته و زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/140264" target="_blank">📅 21:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140263">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
گزارش از شنیده شدن صدای انفجار در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/140263" target="_blank">📅 21:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140262">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سنتکام اعلام کرد: از زمان تقویت محاصره بنادر ایران، ۴۹ کشتی تجاری تغییر مسیر داده، ۲ فروند از کار افتاده و ۲ فروند بازرسی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/140262" target="_blank">📅 21:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140261">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزیر امور خارجه آمریکا: من پنج نهاد کوبایی و هشت فرد را که در تامین تجهیزات نظامی از خارج برای وزارت نیروهای مسلح انقلابی کوبا و نیروهای امنیتی این رژیم مشارکت داشته‌اند، تحریم می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/140261" target="_blank">📅 21:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140260">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
رویترز به نقل از مقام آمریکایی مسیر تنگه فعلاً بازه و هیچ کشوری هم کنترلش رو دست نگرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/140260" target="_blank">📅 21:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140259">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رسانه دولتی سوریه سانا می‌گوید یک وسیله انفجاری در داخل یک اتوبوس در شهر جرمنا، حومه دمشق منفجر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/140259" target="_blank">📅 21:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140258">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: رئیس سازمان اطلاعات اسرائیل (موساد) دو رئیس بخش را به دلیل شکست در تلاش برای تغییر رژیم در ایران، برکنار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/140258" target="_blank">📅 20:49 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140257">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgqjJd0KQ45UF8OwUr_UpZMqoPTqdvkPcO9b5HTVPE-qVZ8NVguCOWcCTtCe8O6AhISovhgN2TEqO8Il1hK0FNJZ561kBCpZzVIvr_czgw43YeqOkiR2-2oH40feI8uzzzYl3zNCuoQNCmFdCXDu216kSDx426nMRskSBuyRii9MiuSa77JigSEzIock7MREFqN8FFIbyewxAmtbpNujfcYE8OHF0WfSUPZYnOp2Xcz5TcNOnQTdtlEEwlZ8iflzdaLcv4pJasXaLlmpip3ZNHNFAri9LrzPG9bdGNdoP-_EmX1cyLHcgL3Nswu8GgnVM-LSZfGd7XH7ZxNLWwKTtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عراقی از انفجار خودروی بمب‌گذاری‌شده در شهر جرمانا در حومه دمشق سوریه خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/140257" target="_blank">📅 20:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140256">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8THoF0zQ-WpC7qHgRNtG2Ui65omkLOVFipigxKlEy7qAhCr5CvJ37QH4XIlcn4YpcWvjxCiQaZENXcu7z2VRkk1fQZGR6B5u4LwjvaV9cfiGECduZgkbXGV3MnJZQ2sojlnDj9Fp_bt0iykBaehtNcbNI0SSYgDjIlMJkArtc6m3PbIF-Qyi5MyN6n01onq9bnlclWkJSvsa58txhuw-_eM0Hi8p75Wt2MsceU0NUf3AChixZL7o8jCuy8JmsDut0vMaszzhKtwumsw32-uwUsWoM7c6O41qDPX_ALS2zuMn_QsK2XZoBbvUjLYGUcuk55oFJmer6ci_k2zxG43Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: اخبار جعلی، همان‌طور که همیشه، شایعات کذب و کاملاً بی‌اساس را پخش می‌کنند. من از کاری که پیت هگستث انجام می‌دهد، بسیار خوشحالم.
🔴
همه چیز فوق‌العاده بوده است، از جمله حمله ما به ونزوئلا، که نتیجه آن در کمتر از یک روز به دست آمد و به ما اجازه داد یکی از بدترین مجرمان در جهان، نیکلاس مادورو، را به عدالت برسانیم!
🔴
همچنین، ایران، که کشور برای جلوگیری از داشتن هرگونه سلاح هسته‌ای ویران شده است، بسیار خوب پیش می‌رود! پیتر در ارتش بسیار مورد احترام است و بهبودهای عظیمی ایجاد کرده است، از جمله حذف DEI و افزایش استخدام به سطوح تاریخی.
🔴
این شایعه توسط واشنگتن کام‌پست، یکی از بدترین رسانه‌های این کسب‌وکار، آغاز شد، با وجود اینکه به آن‌ها گفته‌ایم داستان آن‌ها کاملاً کذب است.
🔴
در واقعیت، من واقعاً معتقدم گزارش‌های جعلی آن‌ها خیانت‌آمیز است!
🔴
پرزیدنت دونالد جی. ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/140256" target="_blank">📅 20:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140255">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ربیعی، دستیار پزشکیان: نظرسنجیا میگن مردم از پزشکیان راضی‌ان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/140255" target="_blank">📅 20:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140254">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kug9sLbxTfvsiO8XnIRKINVGCZmncevmqNBGeX4bBIIM6FCWO4G-e-WONc8gcpK5SGwRHpBwsuVI-Dz47KZ_CcPE9lSRqlkRRKwh9nKBfYvLkgVPL2wPk5BmJrSnDUKspQWzv5LZRzpIYcB99dt-oJQWosr5-Gz_5IkcRQ8nxyXFmhKZQj8vpEUHLtbkdsOaaVk0EUZn8tNOtSbU0aZIE_KgGq2ZxomkNtzB_EZmUYdekJEbrETfnDiGjaeMbPPYwoRx_G8Hq2QT5bVbX8q2uY1FbP0LHJDnzXOySc4qcq3PpVEPNzbuaJmt4KH2lxp2mkuWFGVrKi-HuHJti1dDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره : تنگه هرمز: به نظر می‌رسد توپ از زمین ایران و عمان خارج شده و به زمین آمریکا افتاده است و اکنون چشم‌ها به رئیس‌جمهور ترامپ است تا در مورد جزئیات باقی‌مانده و تعهدات آمریکا تصمیم بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/140254" target="_blank">📅 20:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140253">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6aab95f4d.mp4?token=DLpB2Hhx6kYIRwIY8iwRE1991_IddiDCicCBMnqsj8DhpfVVkuyvso45n2SGmWFWPOyO7XCKry3__JHhcyJ3y-cpMKyODmTeMH_vLBtxRoitFoZFvyuEtjgnIk2Cq0-9qy0YxdoFVCI__X6TNF6VhrvjE1HkUYYxa94DxXD0AbLljvTjYu79pZ9UWJ2BMxDAIPub5lR3Ycad5s8FTAAGWrvOGbPcr9NChYf9p-tn7thGMSJUgKjFivz73j4wvKTUqGQwH39hCNngcd2GR0giR1-AhW-oQ27FXoSyiC9iudi_7pdzUy4hxRSfLg0odiWpDmdKZwoVVHtg6KrVPENr2DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6aab95f4d.mp4?token=DLpB2Hhx6kYIRwIY8iwRE1991_IddiDCicCBMnqsj8DhpfVVkuyvso45n2SGmWFWPOyO7XCKry3__JHhcyJ3y-cpMKyODmTeMH_vLBtxRoitFoZFvyuEtjgnIk2Cq0-9qy0YxdoFVCI__X6TNF6VhrvjE1HkUYYxa94DxXD0AbLljvTjYu79pZ9UWJ2BMxDAIPub5lR3Ycad5s8FTAAGWrvOGbPcr9NChYf9p-tn7thGMSJUgKjFivz73j4wvKTUqGQwH39hCNngcd2GR0giR1-AhW-oQ27FXoSyiC9iudi_7pdzUy4hxRSfLg0odiWpDmdKZwoVVHtg6KrVPENr2DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بر اثر فرود سخت یک هواپیمای متعلق به شرکت «ایبریا ایرلاین» در کرواسی، لاستیک جلویی آن ترکید. این حادثه که مصدوم نداشته به بسته شدن فرودگاه به مدت دو ساعت منجر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/140253" target="_blank">📅 20:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140252">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۴.۰ ریشتر، ساعت ۱۷:۵۱:۵۹ امروز، ۱۵ مرداد ۱۴۰۵، خلیج فارس در حوالی بندر لنگه استان هرمزگان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/140252" target="_blank">📅 20:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140251">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
هم اکنون دو سوخت‌رسان KC-135 در منطقه حضور دارند ، یکی در آسمان خلیج فارس و دیگری در آسمان امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/140251" target="_blank">📅 20:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140250">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
فارس به نقل از منبع آگاه: کریدورهای شمالی و جنوبی تنگۀ هرمز حذف می‌شوند
🔴
یک منبع مطلع در وزارت خارجه گفت: طبق چهارچوب مذاکرات مطرح شده میان ایران و عمان، بناست در یک مدت مشخص ورودی به تنگۀ هرمز از طریق کریدور شمالی تنگه در نزدیکی ساحل ایران انجام شود و خروجی…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/140250" target="_blank">📅 20:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140249">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBXJRzHGmgllBFa6wm0M6BIQ_1jeY6pK9Ol6GsJQ2YKS37TeD-GX3sJwFj77rXqd_i8Z_T3eXbvFNQDNl2ks_iNKRXKGuOM3b3nnv0OJXT5UJLip2BUj9Sx2qpiurQY6lgbt5ljTtB9CQkxhYCWGSO9zHv0sNGSQi5VdlDtyfWRWJTS_xt5WCHc0yiPH6TjSKgFg1W1lIf1Lee1U_cOLvKtoE9wcixfZRypXUM8mP5uWxSTOGf7W-8R5xzR0PeLQ_FNbDXZug8ague4ar6lj-itFfdo9sypQFnokmbeSzCSVNF6b04scTPGvTtUchKRjfklVR2wDwihoDv-2vOfXuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت برنت در دقایق اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/140249" target="_blank">📅 19:49 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140248">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79bc39b72d.mp4?token=Z34K8ci5wFiBzTA4cWNSwXCI3wMUW3s98yzBpkLHrq7xebKept290RGCVmK1tlDPgsFHIFEshbg31Fvcc6axmz0LA7NV93ZUXH6410YoonY3n8njGzaOO6HItgFuJ9yf_dbz8wAUJENMQpixvsIdF0yM0RCsrX4kmZiNmTD0flHWLyAy_V9ZdaEl4JW-TeWGnZj2mVorCLQy-4UQAMlfY81aGwVW5MkBYSaUalyoqz8Dmpd8NENoAyRq7S1AGhKyxoeIoezI8DlKBuEk24Nu-fdAO-emwnrB_xyeNNwHkemTzAv0sCcUnAWHZ4dmsw-NCfuXjZsoMz5S5Ayg4X8x8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79bc39b72d.mp4?token=Z34K8ci5wFiBzTA4cWNSwXCI3wMUW3s98yzBpkLHrq7xebKept290RGCVmK1tlDPgsFHIFEshbg31Fvcc6axmz0LA7NV93ZUXH6410YoonY3n8njGzaOO6HItgFuJ9yf_dbz8wAUJENMQpixvsIdF0yM0RCsrX4kmZiNmTD0flHWLyAy_V9ZdaEl4JW-TeWGnZj2mVorCLQy-4UQAMlfY81aGwVW5MkBYSaUalyoqz8Dmpd8NENoAyRq7S1AGhKyxoeIoezI8DlKBuEk24Nu-fdAO-emwnrB_xyeNNwHkemTzAv0sCcUnAWHZ4dmsw-NCfuXjZsoMz5S5Ayg4X8x8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر کانادا، کارنی، در پاسخ به ترامپ که رهبری کانادا را «بدجنس» خواند: هر صفتی به کار رود، بله، ما مانند همیشه از همان ابتدا در حال ایستادگی برای کارگران کانادایی و کسب‌وکارهای کانادایی هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/140248" target="_blank">📅 19:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140247">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
فارس به نقل از منبع آگاه: کریدورهای شمالی و جنوبی تنگۀ هرمز حذف می‌شوند
🔴
یک منبع مطلع در وزارت خارجه گفت: طبق چهارچوب مذاکرات مطرح شده میان ایران و عمان، بناست در یک مدت مشخص ورودی به تنگۀ هرمز از طریق کریدور شمالی تنگه در نزدیکی ساحل ایران انجام شود و خروجی کشتی‌ها از کریدور جنوبی نزدیک به ساحل عمان باشد.
🔴
پس از پایان مهلت مشخص، عبور کشتی‌ها از هر دو کریدور شمالی و جنوبی متوقف و کلیۀ ترددها از کریدور میانی اتفاق خواهد افتاد با این تفاوت که ورودی کشتی‌ها با مدیریت ایران و خروجی با مدیریت مشترک ایران و عمان خواهد بود.
🔴
عوارض تعیین‌شدۀ کشتی‌ها برای گذر از تنگه در قالب بهای خدمات مختلف تعیین خواهد شد.
🔴
خبر مبنی‌بر اختلاف ایران و عمان بر سر درصد ارزش بار کشتی‌ها [تعرفۀ ۷ یا ۳ درصدی ارزش محموله] به‌عنوان پرداختی صحت ندارد و دریافتی از کشتی‌ها تابعی از متغیرهای زیاد از جمله میزان خدماتی است که توان تامین آن را داریم.
🔴
بیمه، سوخت‌گیری، بهای محیط‌زیستی و موارد از این دست جزء خدماتی است که کشتی‌ها باید بهای آن را بپردازند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/140247" target="_blank">📅 19:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140246">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
العربیه: تماس‌های غیرمستقیم میان واشنگتن و تهران که از طریق میانجی‌ها در جریان است، وارد مرحله نهایی شده و در حال حاضر، میانجیگران در حال تدوین سند نهایی مرتبط با بازگشایی تنگه هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/140246" target="_blank">📅 19:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140245">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
به گزارش کلش ریپورت، دونالد ترامپ در دیدارهای خصوصی از حامیان مالی حزب جمهوری‌خواه خواسته است از جی‌دی ونس، معاون رئیس‌جمهور آمریکا، برای انتخابات ریاست‌جمهوری ۲۰۲۸ حمایت کنند.
🔴
این گزارش می‌گوید ترامپ با وجود این درخواست‌های خصوصی، تاکنون به‌صورت علنی از نامزدی ونس برای انتخابات ۲۰۲۸ حمایت نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/140245" target="_blank">📅 19:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140244">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی دبیر شورای عالی امنیت ملی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/140244" target="_blank">📅 18:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140243">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
شریعتمداری: باز شدن تنگه هرمز یعنی باز کردن راه فرار دشمن و از دست دادن یکی از مهم‌ترین اهرم‌های فشار جمهوری اسلامی
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/140243" target="_blank">📅 18:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140242">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
یک منبع در ارتش یمن: ۱۶ نفر در حمله موشکی گروه حوثی به اردوگاهی بین استان‌های حضرموت و مارب کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/140242" target="_blank">📅 18:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140241">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
گزارش ها وقوع انفجار های مهیب در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/140241" target="_blank">📅 18:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140240">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خبرگزاری آسوشیتدپرس: تاکنون نزدیک به ۷۰۰ نظامی آمریکایی در حملات پهپادی و موشکی به پایگاه‌های آمریکا در غرب آسیا و دیگر درگیری‌ها زخمی شده‌اند.
🔴
بیشتر سربازان آمریکایی دچار آسیب مغزی ناشی از ضربه یا موج انفجار شده‌اند
🔴
آسیبی که حتی در مواردی که در ابتدا خفیف به نظر می‌رسد، ممکن است سال‌ها بعد با اختلالات حافظه، سردردهای مزمن، سرگیجه و مشکلات شناختی بروز کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/140240" target="_blank">📅 18:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140239">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7f9fa5d85.mp4?token=ZNS819poAcPtwD8uiZNeRYzTDoiRZK9JX1_ACOqHCW1EI6I4ShqdSKTN-6QjopqpqtjxMsxvMuTuu6faQeGNIt9JX_OvlD2iYcPV8yB-HJ-3uZT7grPIKZR3_L7UmlnPTCJ7RQYR0mXgaY-r38tLqv-ecjds1XuQmK4rHggonITaOxCGGlaWote8FsvbGU35RfRxAXeLP7huFbJYKq2NkiuDlu55AUkK1mzyOmIMQVvxmSY8rkPmPTekJ2oUQGCT17SiP0r-34v-Q15eY578bbYaSMXs1m4uN9o0xTsdhjNkpSeljfmkuQRHk3e-aoaY8wBGwQh4BeCTxBuSvKhoNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7f9fa5d85.mp4?token=ZNS819poAcPtwD8uiZNeRYzTDoiRZK9JX1_ACOqHCW1EI6I4ShqdSKTN-6QjopqpqtjxMsxvMuTuu6faQeGNIt9JX_OvlD2iYcPV8yB-HJ-3uZT7grPIKZR3_L7UmlnPTCJ7RQYR0mXgaY-r38tLqv-ecjds1XuQmK4rHggonITaOxCGGlaWote8FsvbGU35RfRxAXeLP7huFbJYKq2NkiuDlu55AUkK1mzyOmIMQVvxmSY8rkPmPTekJ2oUQGCT17SiP0r-34v-Q15eY578bbYaSMXs1m4uN9o0xTsdhjNkpSeljfmkuQRHk3e-aoaY8wBGwQh4BeCTxBuSvKhoNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی جدید از لحظه زلزله ۷.۱ ریشتری "کوماموتو" ژاپن (۹ روز پیش) در یک اتاق عمل جراحی
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/140239" target="_blank">📅 18:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140238">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnSyShWcbdkKzXCtni_TyEMUSNTrjAl2jlc9jz8dQTYZBZH6Bl6OEYm6FU-ynhzpoQWfMZ1T2AJgIEGo4RgoUmtAb8GqLVPSCBFuA69UASx45vvwaomnOZ4Z0feeZ1Z9iNQ2T7lBJqZFouvnFpBN0qpuwr_95ePrRzmLZthycly4vUAw2GoI4-SFlZCWnP64yjq-8G1Zv1RYoHbJdUkaHu5i66Ndl1qTiLsSqBNqesa1fT2CT4uxcyuD-aSSJ6O2WDZr_y03e_SyAjr4dsRUBKMBiu-CdkFia4zSD4eWKvoWziug7qRIDjdf0nDoJNRIsowu_rNVpvK-kVbPHXsI_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پهپاد اسرائیلی به شهر مائفادون در جنوب لبنان، منطقه جنوب لبنان، حمله کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/140238" target="_blank">📅 18:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140237">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNPlbMUkEqLEctsBI0SzXSMYo-6IHwoBUknDlTmQXCYUPQznL4D8Al0_zJlu_jPnzlSTNdKOaFwD4iI6SLZEChwQ8ZDUcb5FlK3Ys7rfCE1jQIXA2Si2a6YtdiNwd8fp--1RJl91dYwnzkW36cJhe1FhotrwawGCG70e2m7TzKVWA6LWzvoCLHb6Jn3eIO-H-Esfxrh7T5Onv6lwqzt7cVJ82UsyKrKG_Pvh_jz2hxqpve1BoLAgqI7ttTDK8FZnp9Kb4ctxbCKosP18d5rRXrJLqATl8P-Vhrus_wTKPdB2-Vh-lA2cnwzP9_JUXw6-A6TGsXxvCqRDW-ySh2CRmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
اکونومیست: پرداخت عوارض به ایران بهتر از ادامه تنش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/140237" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140235">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رویترز: اختلاف ایران و عمان بر سر هزینه عبور از تنگه هرمز
🔴
ایران در مذاکرات با عمان خواهان دریافت ۵ تا ۷ درصد ارزش محموله‌های عبوری به‌عنوان هزینه ترانزیت است، در حالی که عمان بر ۳ درصد تأکید دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/140235" target="_blank">📅 18:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140234">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnPgnFbkFg-bVdXCLqpB1taeTTbs68G78FovTHOLltC810zSciVcEQAAsMGR3W63po1fsj8D756ZKVLcxMPemSf1BZcSGGNpEaDS_vZjyGftNjOdPrD1qKr257JcIVYycAHqMdAbG4Ve-mRDd4AKjNj22h0jR5YQS8_7T2iDXC54BBnALghn3i0-09Q5jjQ3KXX8ME7UNaIRUwxW2HGUpGJIIImCYMIZbs8lunmGyMVIH5AZdBx1dtFLVivz-ub37bCgfQC8xptdkRfnw9NyNNsZACP0ZCWn2daAwYpaovIb4PFTyKoAnoKvVp6JMg8Gtvl6obv1XdqYV8DhkPNm9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسن روحانی:
در سال ۱۳۸۳ میخواستن برای سخنرانی امام زمان در تهران جایگاه درست کنن و سیستم های صوتی پیشرفته هم‌‌ بزارن تا وقتی ظهور کرد و اومد سخنرانی کنه؛ صداش در کل تهران پخش بشه. رهبر موضوع رو فهمید و گفت اومدیمو امام زمان ۳۰۰ سال دیگه ظهور کرد از الان جایگاه درست میکنید؟! جمعش کنید سریع.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/140234" target="_blank">📅 18:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140233">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
هواشناسی: به نظر نمی‌رسد تهران دیگر رنگ دمای ۴۰ درجه را به خودش ببیند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/140233" target="_blank">📅 17:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140232">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueAOVORmOeSnixPqu5R1UI9cW0IviyWM8f1ldAGMqEwu8_sxTeDrKPibhVu5TLt0lWATbEtDhfePRJiG1GqNmuOnY5EZvgTFuWGZylkbso1gbSP-xAmkTHER_2V2XgEpN254TV85wNgd_UBtHLE_I7EzY24KoOZn4B-XZWttQe-9kigfMknDkpyhdluWZEooquQNfWnDzEylYfWndIos9brp1xS0yWVkXhQQcp0E1Nx-pimre8ZoUw2kVfTbVXxhmNIIkZXElzs_BnAPpUqR_YvG6RR3qupe9SuEbMlj6IrrZ89WDE9MMa1bbf7fqsNwXPB5WMr2dxEVHURHhbj03Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور:
بعد اینکه آقا رو زدن باید دنیا رو به آتیش میکشیدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/140232" target="_blank">📅 17:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140231">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e9af9adf.mp4?token=Gg3VLzeY8klfwWlWO3ovpn-N83tL5kCwd5YjvDW-BMP7x2dmUd-0awcmMj1UQLQaBtRYfK-JKUwConFi6jFGAidQZDBNCPs_24VcltCgPLOIKMIIl8isZcyIilMCRF1aNHKGa9abtMLp3t_gXf9KGFYsHoP-nCL5SobhTI3JR-vMbJn5T7PW5qIha-ZVVZ1_1kIVgmcmqx_brR6uPn2e8bsOGkN_StpfVJlqIETAdBsZBRluCJiBWfVbgHIkviNi2x6nBVAxdPtdnZ06Mts_Gwwq3fzGquDg203zJwlwYjvPjNRJ92swu2fkA-bFu6wQCUY2SBruV2KTyPVgLuTR-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e9af9adf.mp4?token=Gg3VLzeY8klfwWlWO3ovpn-N83tL5kCwd5YjvDW-BMP7x2dmUd-0awcmMj1UQLQaBtRYfK-JKUwConFi6jFGAidQZDBNCPs_24VcltCgPLOIKMIIl8isZcyIilMCRF1aNHKGa9abtMLp3t_gXf9KGFYsHoP-nCL5SobhTI3JR-vMbJn5T7PW5qIha-ZVVZ1_1kIVgmcmqx_brR6uPn2e8bsOGkN_StpfVJlqIETAdBsZBRluCJiBWfVbgHIkviNi2x6nBVAxdPtdnZ06Mts_Gwwq3fzGquDg203zJwlwYjvPjNRJ92swu2fkA-bFu6wQCUY2SBruV2KTyPVgLuTR-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک فعال فعال مذهبی:
آمریکایی ها دنبال DNA امام زمان میگردن تا از روی اون پیداش کنن. برای همین به حرم امام حسن عسکری حمله کرده بودن تا DNAیشو بردارن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/140231" target="_blank">📅 17:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140230">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4xJDPL5gU1FQJrjzsgCPHr75EoscB9w14kUhKdJCD4rTHa3oytrQkBfQhupgV6714KQA_HOOzGhQU1axlyuw6q4dZcHOd1N7I9yG_6NqZCRrrQYn_-bbfZ3PbZSK9a004wa5fGcFdy3zubL2Ah_nQ-dsRT4irhmu1xIKPdo_t9KRVN9hTdoGqBM7oHZpjpPdsq9i8GdrtIf7OSFd9NrDEdOE-uuDzxfNZplXtWWSH6yiBh1zfGq1epSX46e1vrNxax3AcKw05Q027D4hrSngauPHoBpLwYupoqhx3hQxU7zv0P_hTxqjBKAMATFxXRqcRGW19BostGiobJ13TfZbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جی‌دی ونس: مذاکره با ایران مانند قدم به جلو و عقب است؛ ایرانی‌ها بسیار سرسخت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/140230" target="_blank">📅 17:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140229">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
حسین شریعتمداری: باز شدن تنگه هرمز یعنی باز کردن راه فرار دشمن و از دست دادن یکی از مهم‌ترین اهرم‌های فشار جمهوری اسلامی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/140229" target="_blank">📅 17:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140228">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
مجری تلویزیون: مردم از افزایش قیمت ماشین خیلی ناراحت نمی‌شوند ولی اینکه کیفیت افزایش پیدا نکنه بهشون فشار میاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/140228" target="_blank">📅 17:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140226">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
هم صدایی سایت‌های اسرائیلی با جبهه منحوس پایداری
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/140226" target="_blank">📅 16:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140225">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4mX4qZ_bqgMoJSQJcWmFmBFTLLc8k5hpXskI2RyuCqV5bOiriEBciMXzOm6trgCA_-qPWd9bVNLe6iD_MXmsnWXX-jMg3Y6y6USrcg2DEKjiwf7GJuISEZ3iCri9sojdmsTYbsAWMJ_4Bv4xTZ2bjVodXkAIx-mCEK1sdV8LdSsdPhpb-qXWbV4n4aGjjGrGNIKD8slf-F8_HPNRngVNVeoaXNbdK_-lGi5IEgEqkyF7LCTaCdaG0VSJyXDUt_n4vjxatYdWn9iBcIJ7V6jiwNKh6bBdqXkOBKl-I3NirOg6U79Yn6AXcnQaNaZ_mXHR4JElMZqnYV8QxX32sBXgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کنایه عضو هیئت رئیسه مجلس به بقایی: شما سخنگو هستید، نه سخن‌نگو!!
‏
🔴
علیرضا سلیمی، نماینده تهران و عضو هیئت رئیسه مجلس، در شبکه ایکس نوشت: «حضرت آقای دکتر بقائی سخنگوی محترم وزارت خارجه وتیم مذاکره کننده! جنابعالی سخنگو هستید نه سخن‌نگو!! برخی خبرگزاری‌های عالم از چیزی بنام توافق جدید خبر میدهند لطفا ملت مبعوث‌شده را نیز محرم بدانید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/140225" target="_blank">📅 16:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140224">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6580b7d6.mp4?token=Cmq0VSIPoXKAvALB7G6nVFyriZXamegF_JcLjaZoe-8-diFyLgtDL-MpAiUNKP_m0wcsSLqdn6-SP4GFOs3iqeZNVCSSfr_zRNqMvBTU0uxnenW50n2tdhc4YHcq4mkdB3pBYS0CMziSYuKuKZNn63hZAIzl3W1stbmMI9WP4kYJRuTwaEdUlkVoKu6GbjB9nZ8yWRrpyMg2Mk4pnJCZVP4XiGrHQrbMV2UxYUpyrL6qt6iF4YPm9ennwi2HUyuwHqElGEG9k_Kd6YQFUS_wvDsmK7c0rSYNiaunkIApYArm4u4yLIgom8BFDa4LwIguzaA1b52CCAhHxg97kJxpMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6580b7d6.mp4?token=Cmq0VSIPoXKAvALB7G6nVFyriZXamegF_JcLjaZoe-8-diFyLgtDL-MpAiUNKP_m0wcsSLqdn6-SP4GFOs3iqeZNVCSSfr_zRNqMvBTU0uxnenW50n2tdhc4YHcq4mkdB3pBYS0CMziSYuKuKZNn63hZAIzl3W1stbmMI9WP4kYJRuTwaEdUlkVoKu6GbjB9nZ8yWRrpyMg2Mk4pnJCZVP4XiGrHQrbMV2UxYUpyrL6qt6iF4YPm9ennwi2HUyuwHqElGEG9k_Kd6YQFUS_wvDsmK7c0rSYNiaunkIApYArm4u4yLIgom8BFDa4LwIguzaA1b52CCAhHxg97kJxpMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا سیما: در تفاهم جدید آمریکا پذیرفته که نظارت بر تنگه هرمز با ایران باشد
‏
🔴
هنوز ساز و کار نحوه رفت و آمد کشتی‌ها مشخص نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/140224" target="_blank">📅 16:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140223">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b89f92fb.mp4?token=WSk1IMDw7Gte7wSvJfLCAtVrmr6WU9eMA4JRS2f4ZXO4_IzWWgr2SW-xjxmGM0bY7X7kmGAYqxpFmNeeUc75w6YLuI-6GCCYwo79JffzD40eFzNcyjirtQLsoW3OadE_Ct7uZ_Ti-_qwgeFpNvHZuxvFV7a9Ad3fQxeK8e6Gn58BFhbON6ZhqqGhi5ygwkqXaYQcUNqTHRRRQOesyJg1BE-e66J8BXuI2d5fDj3gT31dvqyARb1WjeOq1y3IHHSCu-I8XZYJ-EiqKvPr4tiSuoc_LybnO2wJJUoAUsPjKeZHVXBv_bcGXxkOHFk6dSs7UziQPEgg6c6f01BzvgUL2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b89f92fb.mp4?token=WSk1IMDw7Gte7wSvJfLCAtVrmr6WU9eMA4JRS2f4ZXO4_IzWWgr2SW-xjxmGM0bY7X7kmGAYqxpFmNeeUc75w6YLuI-6GCCYwo79JffzD40eFzNcyjirtQLsoW3OadE_Ct7uZ_Ti-_qwgeFpNvHZuxvFV7a9Ad3fQxeK8e6Gn58BFhbON6ZhqqGhi5ygwkqXaYQcUNqTHRRRQOesyJg1BE-e66J8BXuI2d5fDj3gT31dvqyARb1WjeOq1y3IHHSCu-I8XZYJ-EiqKvPr4tiSuoc_LybnO2wJJUoAUsPjKeZHVXBv_bcGXxkOHFk6dSs7UziQPEgg6c6f01BzvgUL2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه اصابت موشک‌های نیروهای یمنی به اردوگاه‌های نیروهای تحت حمایت عربستان در حضرموت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/140223" target="_blank">📅 16:27 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
