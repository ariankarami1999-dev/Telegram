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
<img src="https://cdn4.telesco.pe/file/O72a9-HH3H6esaWGx2BmphN1DtYpem78EhNeQvD8STwVQM8jm5P_OgdODy7Ag3W7V8EZzPV9uqpAg9rlG7lxLoighKSQUK5CKIT_uJBjYdY-RoUIlTns8RFOSDdBhgdoP3Q0on2axtdN-qCTFI-buWQvvUuSLZcf4sMEvLDRNyr1ojYLIOvdkNDBwLU20doKFjKGzWkJoW-fcdSR9oxmfdwxUxfo3X2tcQ_SOAVQuOmmJ9OsL_u-5eS15zvaJ80PYwJmXjdi8uQ17Xx3OTYWfkY22pgsmq9KiF7WChAnM3qqaKq9RuJmVji9AMrF8YDLQ78tBbko_aPBwtNYdQ4GQw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 14:30:57</div>
<hr>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رویترز: کشورهای بریکس بر سر بیانیه مشترک به توافق رسیدند.
منابع می‌گویند اعضای بریکس در نشست دهلی‌نو بر سر بیانیه‌ای توافق کرده‌اند که
اقدام نظامی یک‌جانبه هر کشوری را محکوم می‌کند
، اما برای جلوگیری از اختلاف، نام هیچ کشوری در آن ذکر نخواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/withyashar/22949" target="_blank">📅 14:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f69baa1d9.mp4?token=gC72AcUwyqEjcV-iT_2pBLSAppWHWCYDE8s31s5mfVHq2UdR1LKhcmIJiQ8ud6BvAN7UaNTi31txuOli0ZfYYVryb1WzO0lVo5HhAQsquC_Cw6UrBewAsl5NJIiQwY7syPpvkG3sT5zBpoKwLIuYCYG06L1BfC1dvhFcOPUi4PfxgI13EQZBZMrytiTwN9XrnCnoVPRqGD9H7VY-UwFU7fOpiP4eWgMwoft7wi7WW7j0paYoID8nACwVWGzOIpV3hsVwXZ_AKUZeg77CkUdhubNTZR5p_a9wGUM02GfX4v3eT_uuXFgk-JnLLbsveJrj4MkVTysvmF9_xzKQ1ZhDVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f69baa1d9.mp4?token=gC72AcUwyqEjcV-iT_2pBLSAppWHWCYDE8s31s5mfVHq2UdR1LKhcmIJiQ8ud6BvAN7UaNTi31txuOli0ZfYYVryb1WzO0lVo5HhAQsquC_Cw6UrBewAsl5NJIiQwY7syPpvkG3sT5zBpoKwLIuYCYG06L1BfC1dvhFcOPUi4PfxgI13EQZBZMrytiTwN9XrnCnoVPRqGD9H7VY-UwFU7fOpiP4eWgMwoft7wi7WW7j0paYoID8nACwVWGzOIpV3hsVwXZ_AKUZeg77CkUdhubNTZR5p_a9wGUM02GfX4v3eT_uuXFgk-JnLLbsveJrj4MkVTysvmF9_xzKQ1ZhDVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تهران (ونک) ی غذاخوری افتتاح شده که عرزشی سوز ترین رستوان شده به اسم بی بی که تخصصش  کتلت درست کردنه، حالا ی عده عرزشی فشاری شدن و بهش گیر دادن، میگن تو عمدا اسم غذاخوریتو گذاشتی بی بی و فقط کتلت درست میکنی.
@WarRoom
😂
✌🏼</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/withyashar/22948" target="_blank">📅 14:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22947">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ: فکر می‌کنم ایران موشک‌هایی دارد که می‌تواند شهرهای اروپایی را هدف قرار دهد
@WarRoom</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/withyashar/22947" target="_blank">📅 14:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22946">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دیدبان اتاق جنگ پشت سنگر : یاشار سلام محاصره رو شکستن افراد مسلح همه رو تارو مار کردن نظامیهای رژیم رو @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/withyashar/22946" target="_blank">📅 13:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22945">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/063b6ca407.mp4?token=a7WOGdGKBgTNKGeXPYNdE6TKleM7NjDLQaFoFvZMdBhdI5_NtvCYp_Z18i5EsvgzRTuOsxf2UCBWvG5ERG-a8PtaCA6w2X5YBi_Ss4NS2PVdwrO-uVpp73U76QkjOLhHZMgo1PcW-jT-ffQa_pCReBce-fQi3euKUQ-r5qVL0QOGsv7CUCdrRMppoGIDKbpcRbyUFq2Zfao002oYLA2FE5-nxUilFATTzkaN4vy-zzTmPgRmh9GqKaOjP43HxChSrsdEtn73z7pS0uK_axo8BKvO7kZlYi8LJ94cBjNCu6UxTRoZl_o69rQgmdhurc7ZSTgFdvIqSHxCxFCcEkHgqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/063b6ca407.mp4?token=a7WOGdGKBgTNKGeXPYNdE6TKleM7NjDLQaFoFvZMdBhdI5_NtvCYp_Z18i5EsvgzRTuOsxf2UCBWvG5ERG-a8PtaCA6w2X5YBi_Ss4NS2PVdwrO-uVpp73U76QkjOLhHZMgo1PcW-jT-ffQa_pCReBce-fQi3euKUQ-r5qVL0QOGsv7CUCdrRMppoGIDKbpcRbyUFq2Zfao002oYLA2FE5-nxUilFATTzkaN4vy-zzTmPgRmh9GqKaOjP43HxChSrsdEtn73z7pS0uK_axo8BKvO7kZlYi8LJ94cBjNCu6UxTRoZl_o69rQgmdhurc7ZSTgFdvIqSHxCxFCcEkHgqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره ایران: ما با قدرت بسیار زیادی تنگه هرمز را کنترل می‌کنیم. هیچ‌کس انتظار نداشت چنین اتفاقی بیفتد.
ما به‌طور متوسط روزانه ۲۵ قایق را از بین می‌بریم
@WarRoom</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/withyashar/22945" target="_blank">📅 13:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22944">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd5f25930.mp4?token=uiZo3UPDU5vfnqwM2RelRZcRYGxnxm6Sc-jST9oCSlKDaQH_9eTGeLNPzKA7oHaNWVEwNCke0r3Si6tGqcuSZg7SJuAX8plyVPgoW2eagczJ6qU_8Kp2_Mz3-BHQx_-jpJgBmRxi5jV3401EqCGJQLM8SXRZqxj3EaRuUt5-4_VZoRVsds10VCmcr9eYMLy_JTgEhf848MC35wHrOxHjCgWSQB__ZcfwVE1tV-tbTOSQk9kLwOiEiiVNpEPtn6XnSESH-Wa2t1b1Gclyjmj9IBkfjvIeyoCQpnJOr6CWm_5XfEisS6c4tC4PSq2e94XDRLEXHnZIAMLSTm0Bd2iwtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd5f25930.mp4?token=uiZo3UPDU5vfnqwM2RelRZcRYGxnxm6Sc-jST9oCSlKDaQH_9eTGeLNPzKA7oHaNWVEwNCke0r3Si6tGqcuSZg7SJuAX8plyVPgoW2eagczJ6qU_8Kp2_Mz3-BHQx_-jpJgBmRxi5jV3401EqCGJQLM8SXRZqxj3EaRuUt5-4_VZoRVsds10VCmcr9eYMLy_JTgEhf848MC35wHrOxHjCgWSQB__ZcfwVE1tV-tbTOSQk9kLwOiEiiVNpEPtn6XnSESH-Wa2t1b1Gclyjmj9IBkfjvIeyoCQpnJOr6CWm_5XfEisS6c4tC4PSq2e94XDRLEXHnZIAMLSTm0Bd2iwtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: جنگ در ایران چه زمانی پایان می‌یابد؟
ترامپ: فکر می‌کنم خیلی زود؛ احتمالاً درست پس از انتخابات میان‌دوره‌ای.
آن‌ها سعی دارند تا جای ممکن مقاومت کنند تا انتخابات را پیچیده کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/22944" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a5eefe77.mp4?token=NJcGTV8zCc4JRC5Ma-7WAzCXypceVv-m9fUiWvnFUtzL3RTLY4aScq2WsMo1lYqjMvRmEg8mQpqzgwl-rrvs05ZvxLt-swaekw6kdfgCNOoNUzgEEKjO78z6efrz5BgvhLc4Up9DS8SEafJC6vuAVUTS6n8XXoCjHhHkNR9TgtXuNcuC20UhImkosYROxzuuRdd5q755HEyoRH7FmHaG-Ze3ZXU-W4yoMN4grlIO2a5hb6Bjf-mvwk0GJDBmcgmilaiKnDkwsSvfw6GtFMWFT0cBQ4nIax-xw2YXNPtiFN-tsDOQUizMHQa02tARaL7b-OXUFduVfp-4GqFU1-E4VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a5eefe77.mp4?token=NJcGTV8zCc4JRC5Ma-7WAzCXypceVv-m9fUiWvnFUtzL3RTLY4aScq2WsMo1lYqjMvRmEg8mQpqzgwl-rrvs05ZvxLt-swaekw6kdfgCNOoNUzgEEKjO78z6efrz5BgvhLc4Up9DS8SEafJC6vuAVUTS6n8XXoCjHhHkNR9TgtXuNcuC20UhImkosYROxzuuRdd5q755HEyoRH7FmHaG-Ze3ZXU-W4yoMN4grlIO2a5hb6Bjf-mvwk0GJDBmcgmilaiKnDkwsSvfw6GtFMWFT0cBQ4nIax-xw2YXNPtiFN-tsDOQUizMHQa02tARaL7b-OXUFduVfp-4GqFU1-E4VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا
ایران
مسئول حمله به خط لوله نفتی شرق-غرب عربستان است؟
ترامپ: فکر می‌کنم آنها هستند، احتمالاً آنها هستند
@WarRoom</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/22943" target="_blank">📅 13:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ در مورد حمله به خط لوله نفت سعودی: حوثی‌ها نمی‌خواهند با ما وارد جنگ شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/withyashar/22942" target="_blank">📅 13:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ: ما آتش را در غزه خاموش کردیم و روند صلح را در آنجا تسهیل خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/22941" target="_blank">📅 13:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دونالد ترامپ در مورد حمله به خط لوله انتقال نفت در عربستان سعودی: به احتمال زیاد، ایران مسئول این حمله است.
@WarRoom</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/withyashar/22940" target="_blank">📅 13:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">.:
سلام یاشار جان من ساعت ۱۲ فردوسی بودم
دلار ۲۴۲ معامله میشد
اقتصاد مملکت داره منفجر میشه
خدا به مردم رحم کنه با این گرونی ها</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/withyashar/22939" target="_blank">📅 13:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22938">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ : اوضاع در ایران برایمان بسیار خوب است
همه چیز  به آرامی حل خواهد شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/withyashar/22938" target="_blank">📅 13:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22937">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ae38d90fc.mp4?token=C6AGv7XFvPuae2Njcp6L6CHf83utrfcI9wDxkatmORr99_6IplI7br9Px-RSGBduRTKCfDaVEIsfg43zeJjy66tBhDm7Ro0N1fRgsvT_wdtgKWOALmp7WNReIfuEhrOJDg4oUv0JZEDXBqbqWqarZAsv312Qefb35mhzNnYnm0Zo6nBIJt72vYEOm72agjIA11HkFjzBhqF4R13GaNyyEjgL7v95OIWvYevdvqOJtGhpCYTs3EgfQ5hiLnVypDyKalXsyagbncQceTO-GzB8PzZ8WTxVRqc9wNumOwlJVaHEmauGyns1eXs2rxrkKIls2wh3EvgXjA53FF3vILLPSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ae38d90fc.mp4?token=C6AGv7XFvPuae2Njcp6L6CHf83utrfcI9wDxkatmORr99_6IplI7br9Px-RSGBduRTKCfDaVEIsfg43zeJjy66tBhDm7Ro0N1fRgsvT_wdtgKWOALmp7WNReIfuEhrOJDg4oUv0JZEDXBqbqWqarZAsv312Qefb35mhzNnYnm0Zo6nBIJt72vYEOm72agjIA11HkFjzBhqF4R13GaNyyEjgL7v95OIWvYevdvqOJtGhpCYTs3EgfQ5hiLnVypDyKalXsyagbncQceTO-GzB8PzZ8WTxVRqc9wNumOwlJVaHEmauGyns1eXs2rxrkKIls2wh3EvgXjA53FF3vILLPSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ پشت سنگر : یاشار سلام محاصره رو شکستن افراد مسلح همه رو تارو مار کردن نظامیهای رژیم رو
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/withyashar/22937" target="_blank">📅 13:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22935">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ejNcS31lIEngKUCjlSk77MALX1npa1OQYo-9p6TaooOkcZT1hJWec9_gyHKbipNu8ZEux0FsDOHEAGn5FQ-gxSdGNwpHLH-2m9jnZ8iJQW9rJQ87OtWKZHs8ro69Ymxl0uNr50W3cFZODob6pImsuErTWGGGqgWGkBhpCTBOXz4lI4s4lRD61UWbLpT5iv1_sU1JJfiqeuazAEwD0YtN5Mn662J7db5-CJGSyefbP-4gHVOGqneMVDFK1i2eXz7VnWqwnF_cdL_nlj1ASO7kG-hJSr9nVVDMEQGKx0neZKXc7vA69WhxARbAUNGBRiMGO7Nr4UOqr8CMN7TLOutDVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O6ylzDMy0rYxeE0RpobyUmMOkH-MkvWqrN5qMLLrtPkC3Nd8ggmhT08JcsnrjcHhTiOO-cQRFBtNpQWQDAwhJLr--ChD-5Etj5g9kdy_t3qEPMwkO4mCdrPdAWxP95OOPhMd2tl1iGgU4S-R_i7xiUIddcqyo9Yz8o70ydAp0hifXSKhA4dcI8twsP5_IZJoi2tZ3ZaHpornBs1v-MOIw1dODWhebMVNVUQs4ceZOWWuhlR7lqON3toRCWqGWSkLyqXl0YAnzVgajSwhnGxuLV0UMV-JWF0b22NTnzJ8D0FLGdXesxHvciIsgLeLBa0sGsxRs9E0Xgh_Lum_c6Q5Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک تانکر نفتی متعلق به چین با نام لیزا که در دریای مکران حضور داشت، تلاش کرد تا از تنگه هرمز توسط کریدور ایران وارد شود، اما سپس مسیر خود را تغییر داد و به عقب بازگشت. مشخصا آمریکا اجازه نداد
@WarRoom</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/22935" target="_blank">📅 12:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22934">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نرخ دلار ۲۳۵،۰۰۰ تومان
دلار کف بازار ۲۴۰،۰۰۰ هزار تومان
تتر ۲۳۴،۶۰۰ تومان
بیتکوین ۷۷،۳۰۹ $
انس جهانی طلا ۴،۳۴۷ $(آخرین قیمت)
نفت برنت  ۱۰۴،۶۱$(آخرین قیمت)
@WarRoom
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/22934" target="_blank">📅 12:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22933">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d069691bb.mp4?token=TGktAHJddIJhkYbK0ZCuz624UjnbyDBz0m13AcIfHwf09pikaiJPN41uGiE9iZ4o4xc_NY8GzaOFuw5Ne_6-PFjVxmaI1qm7j5ismTh1Eri4AFsPXIHfMY3GZ9DaOd1PtwVzLH-XI_6VoXnaQMmZujryUGMeEwM8aCNemkKAVdY8jxb2v-x1izseZ6QkVhEK3gAKQWwHg-UOnZ9Ep5zXFr2NyTCqblqFsaBC81IUwMqf1hioHGllJF85ETBJEAZ_idWm7AR49168VkgLpXrlPBwNM45lNbJxrNLNKf7aa5SOspft6aRgaM8E1IJ30teTNVOmugPiXYyblUvuuvU52A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d069691bb.mp4?token=TGktAHJddIJhkYbK0ZCuz624UjnbyDBz0m13AcIfHwf09pikaiJPN41uGiE9iZ4o4xc_NY8GzaOFuw5Ne_6-PFjVxmaI1qm7j5ismTh1Eri4AFsPXIHfMY3GZ9DaOd1PtwVzLH-XI_6VoXnaQMmZujryUGMeEwM8aCNemkKAVdY8jxb2v-x1izseZ6QkVhEK3gAKQWwHg-UOnZ9Ep5zXFr2NyTCqblqFsaBC81IUwMqf1hioHGllJF85ETBJEAZ_idWm7AR49168VkgLpXrlPBwNM45lNbJxrNLNKf7aa5SOspft6aRgaM8E1IJ30teTNVOmugPiXYyblUvuuvU52A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بتسالل اسموتریچ، وزیر دارایی اسرائیل:
«اگر جنگ در همان خطوطی به پایان برسد که از آنجا آغاز شده بود،
دشمن چه هزینه‌ای پرداخته است؟
چه چیزی مانع از آن خواهد شد که دوباره وارد جنگ شود؟
کشته‌شدگان برای آنها اهمیتی ندارند. می‌توانید بگویید: «ما
۵۰ هزار تروریست را در غزه کشتیم
»؛ این برای آنها اهمیتی ندارد. آنها مثل ما نیستند که
حرمت و ارزش جان انسان
برایشان اهمیت داشته باشد. از نظر من، اصل اساسی این است:
اگر علیه من جنگی را آغاز کنی، اگر پیروز شوی، دستاوردی به دست می‌آوری؛ اما اگر شکست بخوری، سرزمین از دست می‌دهی.
»
@WarRoom</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/22933" target="_blank">📅 11:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22932">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الجزیره: حوثی‌ها مدعی کنترل کامل ساحل دریای سرخ یمن شدند.
گزارش جدید می‌گوید نیروهای حوثی پس از پیشروی سریع در امتداد ساحل و تصرف شهر المخا و جزیره میون، اکنون مدعی
کنترل کامل ساحل دریای سرخ یمن
هستند؛ اقدامی که موقعیت آنها در اطراف باب‌المندب را به شکل قابل‌توجهی تقویت می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/22932" target="_blank">📅 11:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22931">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اتاق جنگ با یاشار : مرزهای بسته شده تا این لحظه، ۱- مرز چذابه ۲- شلمچه ۳- سومار ۴-بازرگان(گزارش تایید نشده) همچنین فرودگاه بین‌المللی بصره تمام پروازهای خروجی به ایران و ورودی از ایران را تا اطلاع ثانوی تعلیق کرد. @WarRoom</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/22931" target="_blank">📅 11:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22930">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مسعود پزشکیان در گفتگو با یک رسانه هندی خبر داد که روز دوشنبه توافق عمان و ایران درباره مسیر مشترک تنگه هرمز در حضور وزرای کشورهای عربی حاشیه خلیج‌فارس امضا و به سازمان دریانوردی بین‌المللی اعلام می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/22930" target="_blank">📅 11:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22929">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خبرگزرای AFP گزارش داده مذاکرات بعدی میان
اسرائیل و لبنان در رم به ماه اکتبر موکول شده است
. این مذاکرات قرار بود درباره ترتیبات امنیتی و وضعیت نیروهای اسرائیلی در جنوب لبنان انجام شود.
@WarRoom</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/22929" target="_blank">📅 11:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22928">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اتاق جنگ با یاشار : مرزهای بسته شده تا این لحظه، ۱- مرز چذابه
۲- شلمچه ۳- سومار ۴-بازرگان(گزارش تایید نشده)
همچنین
فرودگاه بین‌المللی بصره تمام پروازهای خروجی به ایران و ورودی از ایران را تا اطلاع ثانوی تعلیق کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/22928" target="_blank">📅 10:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22927">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اخطار
⚠️
⚠️</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/22927" target="_blank">📅 10:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22925">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5080718a1f.mp4?token=HGw6vlOK-X36IiRSwii2_8oW_3xGf06sbZgj0psE4_E5syBypTaOYNTFc40oXAD7_s1vhFX2FUsadPE_7Dpd3cpWzMNsBjpOLwkllGB5gk985XVQ5v1_-Xnk2gWRGDvrQiJDQEhTuETtv-AsTHttrrc9OcrAX7dlmwxdFuQBnGGrbBG5eVn0-rhB4O1-Ifys46EP7m2d8o1yFYfWP3CaO4WQBRcAqEwb61PqqjXq1T-he17gFCU0hEbk0Z9Bbm5gAmkcPlTAfFeu5fI-RCXenrQZHPRsZzKFxZzqkSuukGh7a01fUgh_STBUqpyR8bhLZz_xTU6u94UWKrxzihEIVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5080718a1f.mp4?token=HGw6vlOK-X36IiRSwii2_8oW_3xGf06sbZgj0psE4_E5syBypTaOYNTFc40oXAD7_s1vhFX2FUsadPE_7Dpd3cpWzMNsBjpOLwkllGB5gk985XVQ5v1_-Xnk2gWRGDvrQiJDQEhTuETtv-AsTHttrrc9OcrAX7dlmwxdFuQBnGGrbBG5eVn0-rhB4O1-Ifys46EP7m2d8o1yFYfWP3CaO4WQBRcAqEwb61PqqjXq1T-he17gFCU0hEbk0Z9Bbm5gAmkcPlTAfFeu5fI-RCXenrQZHPRsZzKFxZzqkSuukGh7a01fUgh_STBUqpyR8bhLZz_xTU6u94UWKrxzihEIVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون درگیری میان
نیروهای نظامی و امنیتی و افراد مسلح ناشناس
در منطقه بخشان سراوان، پس از حدود ۶-۷ ساعت همچنان ادامه دارد. صدای
انفجارهای شدید و تیراندازی سنگین
از محل شنیده می‌شود و نیروهای امنیتی حضور گسترده‌ای در منطقه دارند و مسیرهای منتهی به محل درگیری را کنترل می‌کنند. گزارش‌ها از
انتقال مجروحان و کشته‌شدگان نیروهای نظامی و امنیتی
و استقرار چندین دستگاه آمبولانس در اطراف محل حکایت دارد، اما هنوز آمار دقیق تلفات مشخص نیست. به دلیل ادامه درگیری و محدودیت دسترسی، وضعیت غیرنظامیان و میزان خسارات نیز مشخص نشده و تاکنون مقام‌های نظامی و امنیتی
توضیح رسمی درباره درگیری و تلفات احتمالی
ارائه نکرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/22925" target="_blank">📅 10:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22921">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffa0dc375e.mp4?token=KhBV_kyDgR8KN3chAkcc4wPJSFxFwltGBTSCO9SvwsXD_6-RDuV_hvd2bZujQYtw5258WB1uBwZdJ5iWjwNbJTVaQOCTZLzYZk5yLRfACCvocLAKHKf67ok1A8lD-Ehd_r8A6-5p0dQZR5S3cy68daBstkT6EUXozpQ566b1lWnmg_3BT5XP3RpVkRKNl7UKbko-zBRGOCYhQQkJNwoqCtnTxH3ATOdskOFjKaPfNwurF1ay84qZ5ygRUe2VHopMavNeiiqluPmlZDfrmRf9GhtMw-TlqZuMVDSb7zB40ExUN-T_YbHrg5Mi4e7RQnE92mcM22CcHCbbrUJtG4nlAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffa0dc375e.mp4?token=KhBV_kyDgR8KN3chAkcc4wPJSFxFwltGBTSCO9SvwsXD_6-RDuV_hvd2bZujQYtw5258WB1uBwZdJ5iWjwNbJTVaQOCTZLzYZk5yLRfACCvocLAKHKf67ok1A8lD-Ehd_r8A6-5p0dQZR5S3cy68daBstkT6EUXozpQ566b1lWnmg_3BT5XP3RpVkRKNl7UKbko-zBRGOCYhQQkJNwoqCtnTxH3ATOdskOFjKaPfNwurF1ay84qZ5ygRUe2VHopMavNeiiqluPmlZDfrmRf9GhtMw-TlqZuMVDSb7zB40ExUN-T_YbHrg5Mi4e7RQnE92mcM22CcHCbbrUJtG4nlAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری‌هایی در شهر سراوان در استان
سیستان و بلوچستان ایران
میان نیروهای امنیتی ایران و اعضای جبهه مبارزان خلق (PFF)، که پیش‌تر با نام جیش‌العدل شناخته می‌شد، رخ داد.
این درگیری‌ها پس از آن آغاز شد که نیروهای ایرانی به یکی از
مخفیگاه‌های این گروه
یورش بردند.
@WarRoom</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/22921" target="_blank">📅 10:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22920">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فایننشال‌تایمز: آمریکا حفاظت هوایی از نفتکش‌ها در تنگه هرمز را محدود کرده است.
سنتکام با به دستگرفتن کنترل غالب اکنون به نفتکش‌ها اعلام کرده پوشش پدافند هوایی آمریکا در هرمز دیگر به‌صورت شبانه‌روزی ارائه نمی‌شود و کشتی‌ها باید در بازه‌های زمانی مشخص، از جمله حوالی ساعت ۹ صبح، عبور کنند. این تصمیم پس از افزایش حملات شبانه ایران و برای کاهش هزینه و فشار عملیاتی نیروهای آمریکایی گرفته شده است
@WarRoom</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/22920" target="_blank">📅 10:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22919">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab9a6cb30.mp4?token=o2l3QQ4EB6n837QmXOoChnIOCnyxzK6U9KMD2VzYzFvPHBhbU4RvRIOjnsTBxzwZz6DT4fLYo7g02vU5oSyC6szRmi1qtP3Srpj_60eCU0iLvrx4t3dwNWbiDsmRi8bc1c4v3DvhN1Y3kZAlfkM4TyW6XUBsndvOe8gQAFTcpKfFOYQ79lluhx1zlMrFQttjAl4P7IUpUo4oi4yEK9veQtO4xxmfpM6ZXYOutiaRcnI5QIlSIZTF8vycyz0t9U4mlcChX0OMkxZ3KalzQJ5FFe6F2wLaJu5GRTHK-DaS_NyX5g8jh6wGeDHjV6-h9BoECOyqejyQHtpkCjExfQcgGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab9a6cb30.mp4?token=o2l3QQ4EB6n837QmXOoChnIOCnyxzK6U9KMD2VzYzFvPHBhbU4RvRIOjnsTBxzwZz6DT4fLYo7g02vU5oSyC6szRmi1qtP3Srpj_60eCU0iLvrx4t3dwNWbiDsmRi8bc1c4v3DvhN1Y3kZAlfkM4TyW6XUBsndvOe8gQAFTcpKfFOYQ79lluhx1zlMrFQttjAl4P7IUpUo4oi4yEK9veQtO4xxmfpM6ZXYOutiaRcnI5QIlSIZTF8vycyz0t9U4mlcChX0OMkxZ3KalzQJ5FFe6F2wLaJu5GRTHK-DaS_NyX5g8jh6wGeDHjV6-h9BoECOyqejyQHtpkCjExfQcgGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ ، درباره انتخابات میان‌دوره‌ای: «اگر از نظر آماری نگاه کنید، وقتی رئیس‌جمهور هستید، چه جمهوری‌خواه باشید و چه دموکرات، به دلایلی اتفاقات عجیبی در انتخابات میان‌دوره‌ای رخ می‌دهد.
فکر می‌کنم در انتخابات میان‌دوره‌ای پیروزی بزرگی به دست خواهیم آورد.»
@WarRoom</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/22919" target="_blank">📅 10:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22918">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d9f9d1ac1.mp4?token=SEwBr45V--qiVDwtYzLU6fHmEc93SOfIaR9OQH4uRKWqUgVNG5Lw8a9c-0ErfNHGEf-Qa39VE78XWls5rCMlL-qng9-1juNtyPRBitlfeWBnIIPVipz6yOzXFgEphmsTFCMCbKiRcnLXe74shGUKq5A10Vzj1VPCxmMlCSrlwNaIchwgA9r3glhZHW8gG4IXgfFbTKteppK7dcloUzVfrdrqVomZqrHfgU9wmQrnryPvvgKPUVC8FGtNQ7vZx4qAU87feWABoNpC29m9NUk5UG_XCY5cgThsuB6dpn12Hg7iegzewPBS_Ur47_P3KgOyIvjHhCDBml0K1Pguuz2yBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d9f9d1ac1.mp4?token=SEwBr45V--qiVDwtYzLU6fHmEc93SOfIaR9OQH4uRKWqUgVNG5Lw8a9c-0ErfNHGEf-Qa39VE78XWls5rCMlL-qng9-1juNtyPRBitlfeWBnIIPVipz6yOzXFgEphmsTFCMCbKiRcnLXe74shGUKq5A10Vzj1VPCxmMlCSrlwNaIchwgA9r3glhZHW8gG4IXgfFbTKteppK7dcloUzVfrdrqVomZqrHfgU9wmQrnryPvvgKPUVC8FGtNQ7vZx4qAU87feWABoNpC29m9NUk5UG_XCY5cgThsuB6dpn12Hg7iegzewPBS_Ur47_P3KgOyIvjHhCDBml0K1Pguuz2yBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : من عاشق سیاست هستم.
به دوستانم که در حوزه املاک یا ساخت‌وساز فعالیت می‌کنند می‌گویم؛ چون واقعاً در ساخت‌وساز و ساختن چیزها خیلی خوب بودم: «آیا در سیاست بهترم یا در ساخت‌وساز؟»
@WarRoom</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/22918" target="_blank">📅 10:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22917">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d38f899a.mp4?token=igz0dtxzWN9K1K8SadC5v-UHEn2YJwudQibUE1IiWQjetkOmhxGh-iMoZLB0g2ovAtE544Ekok151396D5o68NYVqlZxUyIXg9nHjhJFWnmFzHMaMk-qEp925esVRJMA5y64B-dKvJtMxwhKrPC135J19u2zhgLw5G6RWrVVEwJy3VnHH6eg_jFQS1dyu-wZZZBg6LvyRK-KSZb_p7B7rNau9fN7hXFCaYNvSDk3pmFFOV9mhPYflk9r86NWGzHsyQGyaN4nktYVmB3L8l365E3IesZDM33kdFRlJrrUJ5GezP_RYHUVBgQW9o4fhxXQMXoaxgzGPIzasJu_ZMqpKreb9ceR_EHinSR5vcZigiXdsHQ43n0bUFA7vyMhe9G0xT3zOtZRo1o3wZTzQhHz7DElhSxdpPL2MDvaCJ2fOxPCQ2e540RygqBNcPXNqCvHeJJ-G3Iy7waOf6R1hBtBsnwaOXTzLOFinTpDl9eIPEcadMUk7dThcDUZueEPYuxIoBffsZI5b7TSE-Xyi8uaoQgN3-abdb6ro8yEWPpR4jSKcwAkSix3_t_w-sHxn_r7P_sVXeyBWu2NVUmRAKoVquuy9iEmQTKy5qHVAUQXv3DKEz50vlFvzj7Qowh1UhBh2tU4R5G7pC7RWtM1qn8wL_4q7Yd7EteI1W8MTM1GU8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d38f899a.mp4?token=igz0dtxzWN9K1K8SadC5v-UHEn2YJwudQibUE1IiWQjetkOmhxGh-iMoZLB0g2ovAtE544Ekok151396D5o68NYVqlZxUyIXg9nHjhJFWnmFzHMaMk-qEp925esVRJMA5y64B-dKvJtMxwhKrPC135J19u2zhgLw5G6RWrVVEwJy3VnHH6eg_jFQS1dyu-wZZZBg6LvyRK-KSZb_p7B7rNau9fN7hXFCaYNvSDk3pmFFOV9mhPYflk9r86NWGzHsyQGyaN4nktYVmB3L8l365E3IesZDM33kdFRlJrrUJ5GezP_RYHUVBgQW9o4fhxXQMXoaxgzGPIzasJu_ZMqpKreb9ceR_EHinSR5vcZigiXdsHQ43n0bUFA7vyMhe9G0xT3zOtZRo1o3wZTzQhHz7DElhSxdpPL2MDvaCJ2fOxPCQ2e540RygqBNcPXNqCvHeJJ-G3Iy7waOf6R1hBtBsnwaOXTzLOFinTpDl9eIPEcadMUk7dThcDUZueEPYuxIoBffsZI5b7TSE-Xyi8uaoQgN3-abdb6ro8yEWPpR4jSKcwAkSix3_t_w-sHxn_r7P_sVXeyBWu2NVUmRAKoVquuy9iEmQTKy5qHVAUQXv3DKEz50vlFvzj7Qowh1UhBh2tU4R5G7pC7RWtM1qn8wL_4q7Yd7EteI1W8MTM1GU8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره
آنتروپیک (شرکت سازنده هوش مصنوعی Claude؛ ترامپ مدعی است از فناوری آن برای برخی فعالیت‌های مخالف و سوءاستفاده‌های احتمالی استفاده شده است)
: «بیایید درباره آنتروپیک صحبت کنیم. آنها کاری انجام دادند که بسیار بد بود و ما آنها را متوقف کردیم. خیلی سریع متوقفشان کردیم. ما گاردریل‌هایی داریم. بزرگ‌ترین گاردریل این است که افرادی را داشته باشیم که به همان اندازه باهوش باشند؛ چون هیچ‌کس این موضوع را درک نمی‌کند، مگر اینکه ضریب هوشی بسیار بالایی داشته باشد — نه جو بایدن.»
@WarRoom</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/22917" target="_blank">📅 10:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22916">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf8a770bd6.mp4?token=YEg1vYgELtlZ4kJ2zZJ1O2hA3bIZyYkuvIWyCEvKY9OOCbDObX1u3TFwGyqJ33ZKSgl7NH9g-tYd5NK9DhiWKPDNCGEiSMl191G-iZax0Rsxf4nqvrB32TuoxirElJxSzXgCD9YXfnTbjPvFES8xgckH_mfCose4tT7oEv2s1DluFgSxkUuBtgMZ8bTxiLgucTSrX8WlrSeXmdrQ1wen62f0mNF1SjdZ2vxGdC4-vB5PUoVAFbAMlu3b6Kj_ZmiOZmPgfK_WD_BgNluYgKLtY9p79bMZpdiwLFrZrEjKkEksVepkPcen0FWUykJ4IB5lvcbTVRU2CY6oDXmTf9F0fx8QqrOIJhq0BVxcEIAkg5JNmkBNBQQtDknpwG7SR_T5Og8tog_jSC5laEpbI1VsUkaK7pWy6P022JBHdP8aSx_ZMkr3mN3TJnE28pvzM5aNhgWInWltoM-TgftCI671mMxhvDlngXCC-gU13l0gPGkdKTZoSnutahRleSdbFFMeu3-e98ztIvOscw43wyEk0TMaR2wyZuJhoLn6F_dAdkfMaWteBbzMaDcndi0HuKn_RLtGxZd6s511Nhr2KMVTryQxMeojfa0pXk0fyrr6SnO-rQzswjJn-pg_iSb319bneQCBAW7Y2_3bbsj98OZFmCZbInJE1Xzbl8eTVgYEYnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf8a770bd6.mp4?token=YEg1vYgELtlZ4kJ2zZJ1O2hA3bIZyYkuvIWyCEvKY9OOCbDObX1u3TFwGyqJ33ZKSgl7NH9g-tYd5NK9DhiWKPDNCGEiSMl191G-iZax0Rsxf4nqvrB32TuoxirElJxSzXgCD9YXfnTbjPvFES8xgckH_mfCose4tT7oEv2s1DluFgSxkUuBtgMZ8bTxiLgucTSrX8WlrSeXmdrQ1wen62f0mNF1SjdZ2vxGdC4-vB5PUoVAFbAMlu3b6Kj_ZmiOZmPgfK_WD_BgNluYgKLtY9p79bMZpdiwLFrZrEjKkEksVepkPcen0FWUykJ4IB5lvcbTVRU2CY6oDXmTf9F0fx8QqrOIJhq0BVxcEIAkg5JNmkBNBQQtDknpwG7SR_T5Og8tog_jSC5laEpbI1VsUkaK7pWy6P022JBHdP8aSx_ZMkr3mN3TJnE28pvzM5aNhgWInWltoM-TgftCI671mMxhvDlngXCC-gU13l0gPGkdKTZoSnutahRleSdbFFMeu3-e98ztIvOscw43wyEk0TMaR2wyZuJhoLn6F_dAdkfMaWteBbzMaDcndi0HuKn_RLtGxZd6s511Nhr2KMVTryQxMeojfa0pXk0fyrr6SnO-rQzswjJn-pg_iSb319bneQCBAW7Y2_3bbsj98OZFmCZbInJE1Xzbl8eTVgYEYnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ :
«رئیس‌جمهور شی جین‌پینگ قرار است
دو هفته دیگر برای یک شام رسمی خوب
به اینجا بیاید. ما با هم کنار می‌آییم. می‌دانید، من و او
رابطه بسیار خوبی
با هم داریم. مردم می‌گویند: «اوه، او از ما جاسوسی می‌کند.» خب،
ما هم از او جاسوسی می‌کنیم.
می‌دانید، ما هم در این کار خیلی خوب هستیم. ما اکنون
روابط بسیار خوبی با چین
داریم. قبلاً روابط بسیار بدی با چین داشتیم، اما حالا با چین خوب پیش می‌رویم.»
@WarRoom</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/22916" target="_blank">📅 09:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22915">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65695ba78c.mp4?token=dWWv4-pseekZ2oS0mXJmJqtAcfQv9Zw1D8-ZxlSPpDVv5OstVdBt5UtigbkscPlGmPAEWnGAah8ueGI8nBUPf71DWdPFBObzj2UGWNroUoG2iZ2ehbvJ9M1jIu1xnDd9otYMAuLwtmygmCJukO47Li9RzLUpJZ1agfNP7AVgOtzVAvwIF-AA3oA3KsFqIJsC8oO7M2UydALvKuhmRzWJ6ZMMdg6j4O8dpYjH1z85yH5HPRxpoyxkyWtOzPdJw-QM0EWfXchC8ICV_VPMCCLYJeDQIw8ai-032-t523849T20F-zfPv5VR2MQiS5B1aCYz8phHyJXpMVfm83EFb4MYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65695ba78c.mp4?token=dWWv4-pseekZ2oS0mXJmJqtAcfQv9Zw1D8-ZxlSPpDVv5OstVdBt5UtigbkscPlGmPAEWnGAah8ueGI8nBUPf71DWdPFBObzj2UGWNroUoG2iZ2ehbvJ9M1jIu1xnDd9otYMAuLwtmygmCJukO47Li9RzLUpJZ1agfNP7AVgOtzVAvwIF-AA3oA3KsFqIJsC8oO7M2UydALvKuhmRzWJ6ZMMdg6j4O8dpYjH1z85yH5HPRxpoyxkyWtOzPdJw-QM0EWfXchC8ICV_VPMCCLYJeDQIw8ai-032-t523849T20F-zfPv5VR2MQiS5B1aCYz8phHyJXpMVfm83EFb4MYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
جنگ ایران بعد از انتخابات میان‌دوره‌ای به پایان خواهد رسید.
سؤال:
اگر جمهوری‌خواهان شکست بخورند، چرا جنگ تمام خواهد شد؟
ترامپ:
خیلی‌ها فکر می‌کنند اگر ما شکست بخوریم، من فقط عصبانی‌تر می‌شوم و خودم کار را یکسره می‌کنم، می‌دانید؟
در هر صورت، آنها بازنده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/22915" target="_blank">📅 09:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22914">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وال‌استریت ژورنال: مقام‌های آمریکایی می‌گویند
ایران پیش از حمله موشکی ۱۷ ژوئیه به پایگاه موفق‌السلطی اردن، که به کشته‌شدن سه نظامی آمریکایی منجر شد، به تصاویر ماهواره‌ای چینی با وضوح بالا از این پایگاه دسترسی داشته است.
این تصاویر پیش و پس از حمله در اختیار ایران قرار گرفته و به تهران برای شناسایی دقیق اهداف کمک کرده‌اند. مقام‌های آمریکایی نام شرکت‌های چینی را اعلام نکرده‌اند و
دولت چین را مستقیماً به مشارکت در این حمله متهم نکرده‌اند
؛ پکن نیز خواستار ارائه شواهد شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/22914" target="_blank">📅 09:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22913">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تعطیلی مرز مهران تکذیب شد
‌فرماندار مهران: مرز مهران باز است و فعالیت‌های مسافری و گمرکی در این مرز برقرار است و هیچ‌گونه تعطیلی یا توقفی در روند فعالیت مرز با کشور عراق وجود ندارد. طی شبانه‌روز گذشته ۱۷ هزار نفر از این مرز تردد داشته‌اند که نشان‌دهنده استمرار فعالیت بخش مسافری مرز مهران است.
@WarRoom</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/22913" target="_blank">📅 09:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22912">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">العربیه : نخست وزیر عراق پس از حمله شبه‌نظامیان هوادار ایران به عربستان سعودی، گذرگاه‌های مرزی شلمچه، شیب و مندلی را با ایران بستند. احتمال می‌رود تسلیحاتی که برای هدف قرار دادن عربستان به کار رفته‌اند، از طریق یکی از این گذرگاه‌ها از ایران به عراق منتقل شده باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22912" target="_blank">📅 03:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22911">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فاکس نیوز از عرشه ناو هواپیمابر:  «یو‌اس‌اس جرج واشینگتن» روز جمعه ۱۱ سپتامبر در جریان استقرارش برای نبرد با جمهوری اسلامی آماده می‌شود.
این ناو هواپیمابر که حدود ۵۰۰۰ ملوان را در خود جای داده و توسط ناوشکن‌ها اسکورت می‌شود، آخر هفته گذشته هدف حمله موشک‌های بالستیک ایران قرار گرفت؛ این در حالی است که در طول هفته جاری نیز چندین مورد تبادل آتش میان طرفین رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22911" target="_blank">📅 02:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22910">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رویترز: نفت در پایان هفته بالای ۱۰۰ دلار ماند.
برنت در پایان معاملات جمعه روی
۱۰۴٫۶۱ دلار
بسته شد و نفت آمریکا به
۱۰۰٫۰۵ دلار
رسید؛ نفت برای این هفته بیش از
۸ درصد
رشد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22910" target="_blank">📅 01:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22909">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به مناسبت بیست و پنجمین سالگرد حملات ۱۱ سپتامبر، سازمان اطلاعات مرکزی آمریکا (سیا) ۶۹ سند اطلاعاتی محرمانه را منتشر کرد؛ اسنادی که در سال‌های منتهی به این حمله تروریستی در اختیار بیل کلینتون و جورج دبلیو بوش، رؤسای جمهور وقت، قرار گرفته بود. در میان این اسناد، هشداری مورخ ۱۰ سپتامبر ۱۹۹۸ به چشم می‌خورد که بیان می‌داشت القاعده «ممکن است هواپیمایی مملو از مواد منفجره را به یکی از شهرهای آمریکا بکوبد.» این اسناد یافته‌های کمیسیون تحقیق سال ۲۰۰۴ را تأیید می‌کنند و نشان می‌دهند که نهادهای اطلاعاتی به‌طور مداوم درباره نیات القاعده هشدار داده بودند. با این حال، مقامات اطلاعاتی اذعان کردند که این هشدارها نتوانسته بود ابعاد کامل فاجعه برنامه‌ریزی‌شده را به‌درستی منعکس کند. جان رتکلیف، رئیس سیا، اظهار داشت: «بیست و پنج سال پیش، حملات ۱۱ سپتامبر ضربه‌ای به ملت ما وارد کرد، اما نتوانست ما را درهم بشکند.»
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22909" target="_blank">📅 01:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22908">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سخنگوی وزارت خارجه:
منشا حمله آمریکا به لامرد، خاک یکی از کشورهای جنوبی حاشیه خلیج فارس بوده است.
عربستان، ژاپن و اردن تبعات رای‌ مثبت خود به قطعنامهٔ ضدایرانی آژانس را خواهند دید و ما آن‌ها را پاسخگو خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22908" target="_blank">📅 00:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22907">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سنتکام : در اعمال محاصره ایالات متحده علیه ایران تا امروز ، نیروهای آمریکایی
مسیر ۹۹ کشتی تجاری را تغییر داده‌اند(۳ کشتی جدید فقط امروز)
تا از رعایت کامل مقررات اطمینان حاصل کنند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22907" target="_blank">📅 23:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22906">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مقام اسرائیلی در گفتگو با کانال ۱۲  : تسلط حوثی‌ها بر تنگه باب‌المندب به دلیل عرض بسیار کم مسیر کشتیرانی و امکان هدف قرار دادن مستقیم کشتی‌ها با موشک‌های ضدزره بدون نیاز به سامانه‌های پیچیده راداری، تهدیدی خطرناک‌تر از وضعیت کنونی در تنگه هرمز محسوب می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22906" target="_blank">📅 23:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22905">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ تلفنی ، درباره ایران: اگر نمی‌خواهید کاری را که من انجام می‌دهم انجام دهید،
آن‌ها به سلاح هسته‌ای دست پیدا خواهند کرد.
اگر من یک سال و نیم پیش با بمب‌افکن‌های بی-۲ آن‌ها را به‌شدت بمباران نکرده بودم،
آن‌ها همین حالا سلاح هسته‌ای داشتند و از آن استفاده می‌کردند.
اسرائیل از بین می‌رفت و خاورمیانه نابود می‌شد. شما این را از این واقعیت می‌بینید که ایران آن همه موشک شلیک کرد. مردم، از جمله عربستان سعودی، واقعاً شوکه شده بودند که ایران به‌جای آن موشک‌ها، ممکن بود از یک سلاح هسته‌ای استفاده کند
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22905" target="_blank">📅 23:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22904">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">لایو جنگ یمن در گوگل مپ
https://goo.gl/maps/LkwoDWLT38cUL1mVA?withYashar
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22904" target="_blank">📅 23:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22903">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-5fPapUsdy-g2lAc4uzQ9oXkoxZML_r8iapVQZPFoH9NXuV09KFkHqUra2HZXXGfa_Is8iCOzAyUPRoh4n9qT-8AoCUOUBQQvCaYrsii9ojF0b985Ptm7mjn29Ob_bCT2lgoSVP-lIdEHUWAAZ8V3quXZAroSEjUh54p3_Oyov48C1jac9aIwSep5Mt1OMZcOnEGMGb4FPerzGPzRVPiovSM6GaZPgsq7kuh1BJsVU7t4vylxVns5Oz23m2SYQgOmUOpUDUhdyaqZJ8qxe9HXxVZjLmsvVOzypuFan1QOlpNCFzYD5iSNbQEMLyaqhPsz30AnNCzY8m68gxDjE3sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «سود سهام عدالت
۵۰۰۰ دلاری ترامپ
» که قرار است به همه بزرگسالان در آمریکا پرداخت شود، به‌دلیل اینکه کشور ما در حال جذب
تریلیون‌ها دلار توسعه اقتصادی، سرمایه‌گذاری و موفقیت واقعی
است، از سوی «دموکرات‌ها» مورد انتقاد قرار گرفته؛ آنها امیدوارند این طرح هیچ‌وقت اجرا نشود، اما
اجرا خواهد شد!
برای مثال، دموکرات‌ها می‌گفتند تصویب
«لایحه بزرگ و زیبای بزرگ»
که یکی از بزرگ‌ترین لوایح تاریخ کنگره بود و توسط رئیس‌جمهور امضا شد، غیرممکن است؛ اما تصویب شد. یا
پرداخت ۱۷۷۶ دلاری
که سال گذشته به نیروهای ارتش آمریکا اختصاص دادم؛ تقریباً همه می‌گفتند امکان انجام آن وجود ندارد، اما انجام شد، نیروهای نظامی میهن‌پرست ما پول را دریافت کردند و از آن استقبال کردند.
وقتی من چیزی می‌گویم، منظورم واقعاً همان چیزی است که می‌گویم! سود سهام ۵۰۰۰ دلاری اجرا خواهد شد، زیرا مردم کشور ما شایسته آن هستند.
به جمهوری‌خواهان رأی دهید، آمریکا را دوباره بزرگ کنیم!
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22903" target="_blank">📅 22:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22902">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">روزنامه معاریو: نتانیاهو پیشنهاد حمله نظامی مشترک با کشورهای عربی به انصارالله یمن را داده است
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22902" target="_blank">📅 22:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22901">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ: ما انتخاب دیگری نداریم،
باید سخت با ایران برای پیروزی بجنگیم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22901" target="_blank">📅 21:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22900">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏رضا نجفی، نماینده جمهوری اسلامی در آژانس بین‌المللی انرژی اتمی، به شبکه سی‌جی‌تی‌ان گفت: آمریکا ممکن است از قطعنامه اخیر شورای حکام به‌عنوان زمینه‌ای برای تشدید درگیری یا اقدام نظامی جدید علیه جمهوری اسلامی استفاده کند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22900" target="_blank">📅 21:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22899">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏نیروهای مسلح دولت یمن اعلام کردند در جبهه شرقی و منطقه نظامی سوم، با استفاده از توپخانه و تک‌تیراندازان، نیروها، مواضع و انبارهای حوثی‌ها را هدف قرار دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22899" target="_blank">📅 21:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22898">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏تانکرترکرز گزارش داد برای نخستین بار در دو ماه گذشته، مجموع صادرات نفت خام عراق، کویت، عربستان سعودی، قطر، امارات متحده عربی و عمان از خط محاصره آمریکا به‌طور میانگین از ۱۰ میلیون بشکه در روز عبور کرده است.
‏بر اساس این گزارش، صادرات نفت خام ایران همچنان صفر است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22898" target="_blank">📅 21:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22897">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏ارسالی : ساواکیهای اخموی جذاب اگه توهماتتون  با ای آی تموم شد یه فکری بحال انداختن رژیم بفرمایید
‏مملکت به معلم و نانوا و تراشکار و مشاغل دیگه هم نیاز داره!!!!!
‏یادتون نره ساواک یه
**
مثل پدر مهران غفوریان هم داشت
‏یادتون نره هسته وزارت اطلاعات رژیم رو همون ساواکیهای خائن به شاه پی ریزی کردن
یاشار جان فروارد نشه
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22897" target="_blank">📅 21:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22896">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22896" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22895">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وال‌استریت ژورنال: یک گروه مرتبط با ایران از مدل هوش مصنوعی آمریکایی «کلود» برای ردیابی و هدف‌گیری ناوهای جنگی آمریکا استفاده کرد. بر اساس گزارش شرکت آنتروپیک، این گروه با کمک کلود اطلاعات مربوط به ترانسپوندر کشتی‌ها و هواپیماها، تصاویر نظامی و تصاویر ماهواره‌ای تجاری را جمع‌آوری و تحلیل کرده و برای شناسایی موقعیت و نقاط آسیب‌پذیر ناوهای آمریکایی در خاورمیانه به کار گرفته است. آنتروپیک اعلام کرد این عملیات را شناسایی و متوقف کرده و حساب‌های مرتبط را مسدود کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22895" target="_blank">📅 21:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22894">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سخنگوی نیروهای دولت یمن: نیروی هوایی، عملیات بمباران منطقه "صندوق مرگ" را که پیش از این اعلام شده بود، آغاز کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22894" target="_blank">📅 20:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22893">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارش پرتاب از سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22893" target="_blank">📅 20:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22891">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سی‌ان‌ان گزارش داده که در پی مشاهده دود و آثار انفجار در نزدیکی خط لوله راهبردی شرق–غرب عربستان در جنوب‌شرقی مدینه، احتمال می‌رود این خط لوله هدف حمله قرار گرفته باشد. این خط لوله نفت خام را از مناطق نفت‌خیز شرق عربستان به بندر ینبع در ساحل دریای سرخ منتقل می‌کند و با توجه به اختلال در تردد نفتکش‌ها از تنگه هرمز، اهمیت آن برای صادرات نفت عربستان افزایش یافته است. منابعی در گزارش‌ها احتمال نقش
حوثی‌های یمن
در این حمله را مطرح کرده‌اند، اما عربستان تاکنون وقوع حمله به خط لوله را به‌طور رسمی تأیید نکرده است. تصاویر ماهواره‌ای نیز وجود دود در نزدیکی مسیر خط لوله را نشان می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22891" target="_blank">📅 20:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22890">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">احساس همدردی مردم ایران بعد از شنیدن خبر حمله تروریستی به برج های تجارت جهانی نیویورک در ۱۱ سپتامبر … که امروز سالروزش است ، خودم هیچوقت اون روز رو یادم نمیره @WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22890" target="_blank">📅 20:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22889">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">روزنامه عبری معاریو: حزب‌الله تلاش دارد از نبرد علی‌الطاهر، روایتی از قهرمانی شبیه نبرد کربلا بسازد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22889" target="_blank">📅 20:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22888">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حتما تا آخر گوش کنید موتورم روشن شد</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22888" target="_blank">📅 19:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22887">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22887" target="_blank">📅 19:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22886">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSemoyami SMYM</strong></div>
<div class="tg-text">ولی یاشار اگه بهت بگن با یه بمب اتم تو یه شهر کار این نظام تمومه تو حاضری این اتفاق بیفته</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22886" target="_blank">📅 19:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22885">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ستاد کل نیروهای مسلح اوکراین⁠ گزارش داده نیروهای اوکراینی بندر تجاری مخاچ‌قلعه در داغستان را هدف قرار دادند؛ در این حمله در محدوده بندر آتش‌سوزی ثبت شد و میزان خسارت در حال بررسی اعلام شد. این بندر تنها بندر عمیق‌آب و بدون یخ روسیه در دریای خزر و
یکی از مراکز مهم کریدور لجستیکی روسیه و ایران است که بنا بر اعلام اوکراین، در آن مسیر قطعات و پهپادهای شاهد از ایران به روسیه و مهمات، مواد منفجره و قطعات پهپاد در مسیر معکوس جابه‌جا می‌شوند.
همزمان، اوکراین اعلام کرد در حمله به نووروسیسک، سه شناور روسی شامل ناوچه
آدمیرال اسن، کشتی آبی‌خاکی پیوتر مورگونوف و مین‌روب ژلزنیَکوف
آسیب دیده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22885" target="_blank">📅 19:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22884">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فرانس‌پرس: حوثی‌ها با کمک هوش مصنوعی برای ساخت موشک‌های هدایت‌شونده تلاش کرده‌اند.
شرکت آنتروپیک اعلام کرده یک گروه مستقر در شمال یمن از هوش مصنوعی «کلود» برای طراحی سامانه هدایت، ناوبری و کنترل یک راکت هدایت‌شونده، یک موشک بالستیک چندمرحله‌ای با برد هدف بیش از
۲ هزار کیلومتر
و یک موشک با طرح سرجنگی گلاید هایپرسونیک استفاده کرده است. این شرکت می‌گوید شواهدی از عملیاتی‌شدن این تسلیحات ندارد، اما یک راکت هدایت‌شونده آزمایش شده است. با توجه به محل فعالیت و ارتباط این گروه با حوثی‌ها، احتمال می‌رود این افراد وابسته به حوثی‌ها بوده باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22884" target="_blank">📅 19:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22883">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f58f12cf8.mp4?token=jIoeWWV-U9RNMwePxqC8l0EF_5iY0Z9LVhq_tgc4z8t-V0zuPW7EDpxhh3TPyddxv3B-A0z6j1P-CRdX8CD53jddEiC2PkW4AnhkDZSsfElhxcQYkSbRpN1U8L0NgsScFUsSANWjUWrvh0Jb3yi7sFcGY-Z_SC2T3fgSVtqYG-Q0c3tvOQQifpwtJ0FqSqv3f2MTH8OmhSoKLCLM2URiNVOXtb5FGCJafsOQEvTkjCt9hhoKmu6eK7JQtqO_zv4L8xpRv2UKwN-yFhIZQyETOOFpuLFIPQRocU7ZuddLEIhWsawpDYvRDUwmAkQCXYfFKJrExDJQtPwlb318OuEFrTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f58f12cf8.mp4?token=jIoeWWV-U9RNMwePxqC8l0EF_5iY0Z9LVhq_tgc4z8t-V0zuPW7EDpxhh3TPyddxv3B-A0z6j1P-CRdX8CD53jddEiC2PkW4AnhkDZSsfElhxcQYkSbRpN1U8L0NgsScFUsSANWjUWrvh0Jb3yi7sFcGY-Z_SC2T3fgSVtqYG-Q0c3tvOQQifpwtJ0FqSqv3f2MTH8OmhSoKLCLM2URiNVOXtb5FGCJafsOQEvTkjCt9hhoKmu6eK7JQtqO_zv4L8xpRv2UKwN-yFhIZQyETOOFpuLFIPQRocU7ZuddLEIhWsawpDYvRDUwmAkQCXYfFKJrExDJQtPwlb318OuEFrTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما به نیروهای نظامی‌ای که همین الان مشغول خدمت هستن و تلاش می‌کنن مطمئن بشن بزرگ‌ترین حامی تروریسم در جهان، یعنی جمهوری اسلامی ایران، هرگز و تحت هیچ شرایطی به سلاح هسته‌ای دست پیدا نکنه، ادای احترام می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22883" target="_blank">📅 18:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22882">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e269d57611.mp4?token=MXkVjE7LQbEAeB_fL4F7HGStkCijKTMiU1_jbVrUj2aPZ5-3yBvILB3zmHamHll-Qcp2XwXZ1q1Dd8n8ymcPFOy_AvOEkZXJeTi4H_SkT32eo7kqVydY1mf396IcETW8SjIVIeid07_Yxq1UxZPjNf2bgAY64DmpB_LDg80LU18-6Wlx4XzWOT09qofqoGVdHwMbUwqhrpx0prLh8SzkevukBaYFCN4o9L4Km4C241Jl-XnZP6jWbVIXHmoume8wa6ULen06LGZUN8xvjOFQpebGD8zVTe06EOu0YxBNph1s2HB8lobwPr5zF0J4hBsEyxCieG8SRfpd-7n60Z2B0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e269d57611.mp4?token=MXkVjE7LQbEAeB_fL4F7HGStkCijKTMiU1_jbVrUj2aPZ5-3yBvILB3zmHamHll-Qcp2XwXZ1q1Dd8n8ymcPFOy_AvOEkZXJeTi4H_SkT32eo7kqVydY1mf396IcETW8SjIVIeid07_Yxq1UxZPjNf2bgAY64DmpB_LDg80LU18-6Wlx4XzWOT09qofqoGVdHwMbUwqhrpx0prLh8SzkevukBaYFCN4o9L4Km4C241Jl-XnZP6jWbVIXHmoume8wa6ULen06LGZUN8xvjOFQpebGD8zVTe06EOu0YxBNph1s2HB8lobwPr5zF0J4hBsEyxCieG8SRfpd-7n60Z2B0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر هگست وزیر جنگ:
تنگه را ما کنترل می‌کنیم و این نبرد را نیز تمام خواهیم کرد!
تاریخ به پایان نرسیده بود؛ هیچ‌وقت هم به پایان نمی‌رسه. مبارزه با شر ادامه داشت و الان هم ادامه داره.
و این مبارزه تا روز قیامت ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22882" target="_blank">📅 18:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22881">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cc98c2628.mp4?token=l05APLxxYksROIRy0lgxFcyVpTQn4uiCNcz5V4g6HvEQlagbqvt2CTvm8LTntgupDUzgJGnkZqulHpAnPcYFfh6I7muHrGXsFmpCKuSHCpo23teEZqMCRzzXQ1a1kmqsmZeufRckWY_EoWebCj0yrSCBLV-S1JMn-3bKKSXDYoYcEBazve4JcmQHsH2RYKWZr7Q7ajksxW5bYkxMgwPeakMdhQ2uYGerWyRMPPrMgsFDwRJwzLKWFxYmAHgB8laPp9dMh4it9e4Wh5lPOeC9uiYf7Rex1gzJSpoJP5R5_F4bHS-qGkj65UiDPMAEcqinxcrYy8lqeyYp_gttEPKkTDhR9SK8pgt4fcc0XjkSukHlT7R3xPPKZc3aDfGVxzw3dM9BaARQdYNnyzYguwLjIy4TH1kqzljyd_zKI1BIe0UfMf0FmYpHm4fB4xEfASihO4BTBMtCW2ey46uXaP64u-1Q7vtCkHx2TFjQ1xSFTBvOPlI5bypK2NX3ZGCZkZQxFpQLrT_9g_8C_xhKeSdyzg0PT-5uL4TECt_NczQPxz_LWzonHVcpkWA8Vd-f6m9SFj6CwJYkO0PPxLU5izeSgtr_-iwwbtX3AydYylIA5jjKtGoCRMbkDfbF92Fu7-ilI2p2aETUa1gX8b_QF4MwcJ1VFqXFcJkrT_DCgUQ5agw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cc98c2628.mp4?token=l05APLxxYksROIRy0lgxFcyVpTQn4uiCNcz5V4g6HvEQlagbqvt2CTvm8LTntgupDUzgJGnkZqulHpAnPcYFfh6I7muHrGXsFmpCKuSHCpo23teEZqMCRzzXQ1a1kmqsmZeufRckWY_EoWebCj0yrSCBLV-S1JMn-3bKKSXDYoYcEBazve4JcmQHsH2RYKWZr7Q7ajksxW5bYkxMgwPeakMdhQ2uYGerWyRMPPrMgsFDwRJwzLKWFxYmAHgB8laPp9dMh4it9e4Wh5lPOeC9uiYf7Rex1gzJSpoJP5R5_F4bHS-qGkj65UiDPMAEcqinxcrYy8lqeyYp_gttEPKkTDhR9SK8pgt4fcc0XjkSukHlT7R3xPPKZc3aDfGVxzw3dM9BaARQdYNnyzYguwLjIy4TH1kqzljyd_zKI1BIe0UfMf0FmYpHm4fB4xEfASihO4BTBMtCW2ey46uXaP64u-1Q7vtCkHx2TFjQ1xSFTBvOPlI5bypK2NX3ZGCZkZQxFpQLrT_9g_8C_xhKeSdyzg0PT-5uL4TECt_NczQPxz_LWzonHVcpkWA8Vd-f6m9SFj6CwJYkO0PPxLU5izeSgtr_-iwwbtX3AydYylIA5jjKtGoCRMbkDfbF92Fu7-ilI2p2aETUa1gX8b_QF4MwcJ1VFqXFcJkrT_DCgUQ5agw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احساس همدردی مردم ایران بعد از شنیدن خبر حمله تروریستی به برج های تجارت جهانی نیویورک در ۱۱ سپتامبر … که امروز سالروزش است ، خودم هیچوقت اون روز رو یادم نمیره
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22881" target="_blank">📅 18:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22880">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f47e9c912.mp4?token=GkDkqlxnMdoGYoX7hHF_icAhaO6QHxat2ZlSsqHC2IyYYVpHbaAbs5i3MDNLyxdlQ0LCR9bw_de32w_lilSuoAngt5l1ghuyQLM-yKoLhbqBkQK4pwXfSSDvYklEzzTIYXcIK8M-eeF6rSWObVfRW44P7Cc5G8IH36DuUgXM4agx1roppnVX-OZUGI82nWfb_Niyc6yzvKU9LLg3OckT1X2X_RyjTuQGfdEmNBDh8A86CsCT8BatCtLUjaK0jxw-7H2J26rJHgf4G20uqJTNUKEowJqyup7uieGGulS3EzlZC2E9lEJ30wiTtc8sMFQT8XjklmWnDvDymAf6JF8eqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f47e9c912.mp4?token=GkDkqlxnMdoGYoX7hHF_icAhaO6QHxat2ZlSsqHC2IyYYVpHbaAbs5i3MDNLyxdlQ0LCR9bw_de32w_lilSuoAngt5l1ghuyQLM-yKoLhbqBkQK4pwXfSSDvYklEzzTIYXcIK8M-eeF6rSWObVfRW44P7Cc5G8IH36DuUgXM4agx1roppnVX-OZUGI82nWfb_Niyc6yzvKU9LLg3OckT1X2X_RyjTuQGfdEmNBDh8A86CsCT8BatCtLUjaK0jxw-7H2J26rJHgf4G20uqJTNUKEowJqyup7uieGGulS3EzlZC2E9lEJ30wiTtc8sMFQT8XjklmWnDvDymAf6JF8eqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، حملات 11 سپتامبر را با جنگ خود علیه ایران مرتبط دانست: ما هرگز این واقعه را فراموش نخواهیم کرد. به همین دلیل است که امروز می‌جنگیم.
ما هیچ انتخابی نداریم. تنها نتیجه ممکن، پیروزی است
ایران بزرگترین حامی دولتی تروریسم در جهان است و هرگز به سلاح هسته‌ای نخواهد رسید
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22880" target="_blank">📅 18:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22879">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52171a753f.mp4?token=ox2Xxi_3ja2awpJgw880f_tVWaNf56WojoQ2D3cGNNIpbGGQi9dUf7srbWCWx4Y5kdj52d1wTfpwr9EBW5utLTfffSvpeEAnly6G_niqM3M0217UEkRWY3WJLPsBRFCsRdbAjb0LUkgDjWLeoMaNk5m03PFMG5LiwEAJJs7r0qI5a0InvH9wDrqRgmFcUUrvDbDf_dPTI5fgdl8hCdebyvGTQuQ2GcuBn3EnREcPTqKC__5gTdY8FgTBNKXZTxd4ogTU-RcYplGYA6OhUGOKrru64b488nR79S4RNYFxYbAsQrVI6XlaOv3rRuD13B6PzCx_dT2Is8hcZ-fhyAxTZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52171a753f.mp4?token=ox2Xxi_3ja2awpJgw880f_tVWaNf56WojoQ2D3cGNNIpbGGQi9dUf7srbWCWx4Y5kdj52d1wTfpwr9EBW5utLTfffSvpeEAnly6G_niqM3M0217UEkRWY3WJLPsBRFCsRdbAjb0LUkgDjWLeoMaNk5m03PFMG5LiwEAJJs7r0qI5a0InvH9wDrqRgmFcUUrvDbDf_dPTI5fgdl8hCdebyvGTQuQ2GcuBn3EnREcPTqKC__5gTdY8FgTBNKXZTxd4ogTU-RcYplGYA6OhUGOKrru64b488nR79S4RNYFxYbAsQrVI6XlaOv3rRuD13B6PzCx_dT2Is8hcZ-fhyAxTZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود ۳۰ ربات انسان‌نما و چهارپایه در اعتراض به عملکرد وزارت فناوری اطلاعات لهستان در ورشو، در مقابل این وزارتخانه تجمع کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22879" target="_blank">📅 17:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22878">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hX4q_l_yTLm79y_AwBgBiVsZjOP0GsEAelF7ttqV1UFMr95ovjNaI1vVF_waR-Mvk2E9VZ-JErbRRhga9FMOqRhuR4cHIchNaPyMfnP8Ta6lZLoyyKGRzGIq1_fUNcTSs0HyUfNJPyfPkCCCWjQzqY5jcX_EADRWE5sYlnhdem_jJqv50skADyj0mBRvns-f-zV1kUvLIHZTtq09rSdlHywz7qM5jHGhbjhFTYwIMomTos_Pwtq9Ga2kagaSwF-lfxUSFiMaa3fh2AE_Q0XGfjwKmrYXeSozBlWm-80HmzHh4PAQZsp4q_3U1jA_UNyb0efCQ1RfTJ6uSIBDx6IT3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوکراین در شمال‌شرق استان خارکیف طی دو هفته اخیر مجموعه‌ای از ضدحملات را برای جلوگیری از محاصره نیروهایش در شرق ووچانسک آغاز کرده است.
روسیه از اواخر ژوئیه با حمله‌ای دو‌محوره تلاش کرد حدود
۴۳۰ کیلومتر مربع
از مناطق تحت کنترل اوکراین را قطع کند و به سمت مرکز لجستیکی
پریکولوتنه
پیشروی کرد. اگرچه روسیه چند روستا را در این محور تصرف کرد، نیروهای اوکراینی با اعزام نیروهای کمکی توانستند پیشروی روسیه را متوقف و وضعیت را تثبیت کنند. سپس اوکراین با ضدحملات خود چند منطقه و روستا از جمله
آنی‌شچینه و ایواشچینه
را در اوایل سپتامبر بازپس گرفت و اکنون درگیری بر سر
اوستینیوکا
ادامه دارد. روسیه برای متوقف کردن این ضدحملات، از توپخانه، راکت‌اندازهای چندگانه و
ده‌ها بمب هدایت‌شونده KAB
استفاده کرده است. در جنوب نیز روسیه حملات خود را در نزدیکی
خاتنه
از سر گرفته و به سمت زاروبینکا پیشروی کرده است. طبق نقشه مورد استناد گزارش، تغییرات ارضی اخیر حدود
۴۴ کیلومتر مربع به نفع اوکراین
در برابر
۲٫۱۶ کیلومتر مربع به نفع روسیه
بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22878" target="_blank">📅 16:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22877">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پزشکیان: ایران به گروه بریکس پیشنهاد می‌کند که یک صندوق بیمه ۱۰ میلیارد دلاری برای پروژه‌های بزرگ زیرساختی و انرژی تأسیس کند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22877" target="_blank">📅 16:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22876">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا درباره ایران:
«ما داریم
آنها را به‌شدت تحت فشار و در تنگنا قرار می‌دهیم
. فقط به آمار نگاه کنید: هر روز به‌طور میانگین حدود
۱۰ میلیون بشکه نفت از بخش جنوبی تنگه هرمز خارج می‌شود
، اما ایرانی‌ها
هیچ نفتی خارج نمی‌کنند
. در یک دوره دو هفته‌ای، نتیجه
۱۴۰ میلیارد در برابر صفر
است. آنها فقط یک مشت
بازنده
هستند که نشسته‌اند و می‌گویند: «بله، این کار را می‌کنیم، آن کار را می‌کنیم.» واقعاً برای من
مسخره و خنده‌دار
هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22876" target="_blank">📅 16:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22875">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0273c7f90c.mp4?token=YG0Ttwx_bNBdTk0GjJWXycniJslp8evtHY4uylie8EMqvBm95TCf58TmDG9GnI1pcZvefX-OCHybfB7xiSqTlbh5KdBP8AduSLebfY-w3TJRUk849mqXdPgWPZCZn4jlWuV1tyV4Q1joU7_CEKHXbr-l574lf0WS0VKIoRJzveeRf_ZMEWIt5zXlxi4YGgSCCvFYTI67v54ImbkXc-wodplOG-O3Ve24xOZoe8u2xEzxDnHNygs5yZzrz-9H3Z9E_-yRxgJi9xg1erURbDBoiDwpxOkbMsxsJxGsWfaTn_s8FsdPEqWUG7InlaubhvzDyqC0_s_BMQ2KAknynz1xFDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0273c7f90c.mp4?token=YG0Ttwx_bNBdTk0GjJWXycniJslp8evtHY4uylie8EMqvBm95TCf58TmDG9GnI1pcZvefX-OCHybfB7xiSqTlbh5KdBP8AduSLebfY-w3TJRUk849mqXdPgWPZCZn4jlWuV1tyV4Q1joU7_CEKHXbr-l574lf0WS0VKIoRJzveeRf_ZMEWIt5zXlxi4YGgSCCvFYTI67v54ImbkXc-wodplOG-O3Ve24xOZoe8u2xEzxDnHNygs5yZzrz-9H3Z9E_-yRxgJi9xg1erURbDBoiDwpxOkbMsxsJxGsWfaTn_s8FsdPEqWUG7InlaubhvzDyqC0_s_BMQ2KAknynz1xFDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا درباره ایران:
«هر چیزی که ایرانی‌ها می‌گویند، بخش عمده آن بر پایه
خیال‌پردازی
است. بسیاری از این ادعاها صرفاً
آرزو و هدف‌گذاری
هستند. وال‌استریت ژورنال گفته ایرانی‌ها در حال بازسازی ذخایر موشکی خود هستند. شاید این‌طور باشد، اما
مقیاس آن چقدر است؟
اندازه و ابعاد این بازسازی کجاست؟ ما
۸۵ درصد کارخانه‌های آنها را منهدم کرده‌ایم
. حالا آیا آنها هر هفته یک کارخانه جدید می‌سازند؟ آیا دو کارخانه می‌سازند؟ می‌دانید، اینها فقط
تیترهای خبری
هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22875" target="_blank">📅 16:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22874">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا درباره ایران:
«اگر به حساب‌های ایرانی‌ها در شبکه اجتماعی ایکس نگاه کنید، آنها تلاش می‌کنند در آمریکا
مشکلات اقتصادی ایجاد کنند
؛ چه از طریق
بازده اوراق قرضه
و چه از طریق
قیمت نفت
. و می‌دانید، صرف‌نظر از اینکه استفانی،
بلومبرگ، فایننشال تایمز یا حتی وال‌استریت ژورنال
باشد، آنها آن‌قدر به دلیل
سندرم نفرت و جنون علیه ترامپ
از تعادل خارج شده‌اند که می‌خواهند به ایرانی‌ها
فضایی برای فعالیت و اثرگذاری
بدهند.»
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22874" target="_blank">📅 16:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22873">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkEj-Xy4Lgg6KawlKkeobi2S9IL00K56fNxWp-YqhUMoa05UrgLKYEbcU_mYPRU5tV75gJ5SsuL-6t79KKC3cRncUu1l__PO7dKAvVtUaQeewLgXyWbgRtuke3WtffoYkgtRC30Cs2wGnruj8OBnRFt6SR1VA2W2UxVmAMeIJKEEZF6jzQcpbhQ2UiHfOZyEwFlFe6jETZ7cFKoSStn1ZaInD1F9DC8AgRb7FYwvaEJ4bDMvZBJ6I44e8prgU4JxTYuu0ie5Y5_8zB03Eflarp4KxZ7L2TL-HFodT_JgiFS4_UDnAkJu41JZqh9IFtE6ehHe1RsZfPt5SAk0Of5GTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان‌ملل با ۱۶۴ رأی موافق در برابر ۱ رأی مخالف تصویب کرد که نقشه مرکاتور کنار گذاشته شود و از نقشه "Equal Earth" استفاده شود که سایز واقعی کشورها را نشان می دهد
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22873" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22872">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل: حزب‌الله به دستور ایران، لبنان را ویران می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22872" target="_blank">📅 16:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22871">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">امروز گزارش تورم مصرف‌کننده آمریکا (CPI) برای ماه اوت منتشر می‌شود؛ آماری که می‌تواند بر تصمیم بعدی فدرال رزرو درباره نرخ بهره و بازار کریپتو اثر بگذارد. زمان انتشار: ساعت ۱۶:۰۰ امروز به‌وقت تهران. تورم بالاتر از انتظار معمولاً برای بیت‌کوین و بازار رمزارزها منفی و تورم پایین‌تر از انتظار، مثبت تلقی می‌شود.</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22871" target="_blank">📅 15:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22870">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">قیمت شورت بله شورت معمولی در ‌ایران به حدود ۱ میلیون تومان رسیده !
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22870" target="_blank">📅 14:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22869">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza</strong></div>
<div class="tg-text">داداش یاشار سلام خواستم از وضع مملکت بهت بگم والا مملکت جوری شده که یه شلوار خواستم برا بچم بگیرم پول ندارم ناهار و شام رو تو یه وعده میخوریم اونم نون و پنیر که پنیر هم به زور تونستم بخرم بخدا دیگه نمیتونم شرمنده زن و بچم باشم به خدا دیگه نمیکشم</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22869" target="_blank">📅 14:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22868">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22868" target="_blank">📅 14:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22867">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22867" target="_blank">📅 14:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22866">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2d53e8de.mp4?token=iSSFS8rz0uRvWmJJ3G--UIDZBV0SH33SAzut3O-zJ90y_q28SEpJj4LqjJ4oKPeJaG5EIJZiynEtLZ_az24FZ7P-W4c0c-rHakFx1dTENlmzGiWkoC0F3fATDerf6ynOjBAO7hl6Xc0ld8zWPb6OhMOg3gS1gNNA09PkWewcXsHyyaFxKKSfg5ireFWvvPt23ZoBWKWxM8VAQPxEg6SEKYP9qKGr4nbgeaUOYMVltz57g37BppjRPNd0oqEy7wQ0_B5k21eUweV1yddxOVFMJCMy5a7Mnwa8pokUrLPyGAxs8_qzIlOGLzR37opd2w4Fwpkwvd3Fc5BoX-YVHqLbU1PURn6MaacLn-QZEE3VxtWbtigjFOL-mN8GvHMWdp_zz3cIUwUkyZe4ij-JU-pEdY8Bmfm1OWTrmuCfAz1glJwo8UTm2x-UWMQ4zHYvliD65qRgh1ZfihhFyoh4Mx2PmOqv29d4yvlsYw-5brwmhKgwMauuMAeVgiZjznYui7Tf7KmNn5sFsruaNJLcQyIeGdMVxRtehdhDphm-m-JpBtLsGvjccR-b4wcSzUN3UR8d5I_xGmjAWaixvhekY1CgZvtenEaieb3GJkHUjASQIWGEzOSbkj-bhKrsJa43EodZNz0SO0Vjl86QEJdGgt_xZyU5l277cj5M_3u8JdKV4v0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2d53e8de.mp4?token=iSSFS8rz0uRvWmJJ3G--UIDZBV0SH33SAzut3O-zJ90y_q28SEpJj4LqjJ4oKPeJaG5EIJZiynEtLZ_az24FZ7P-W4c0c-rHakFx1dTENlmzGiWkoC0F3fATDerf6ynOjBAO7hl6Xc0ld8zWPb6OhMOg3gS1gNNA09PkWewcXsHyyaFxKKSfg5ireFWvvPt23ZoBWKWxM8VAQPxEg6SEKYP9qKGr4nbgeaUOYMVltz57g37BppjRPNd0oqEy7wQ0_B5k21eUweV1yddxOVFMJCMy5a7Mnwa8pokUrLPyGAxs8_qzIlOGLzR37opd2w4Fwpkwvd3Fc5BoX-YVHqLbU1PURn6MaacLn-QZEE3VxtWbtigjFOL-mN8GvHMWdp_zz3cIUwUkyZe4ij-JU-pEdY8Bmfm1OWTrmuCfAz1glJwo8UTm2x-UWMQ4zHYvliD65qRgh1ZfihhFyoh4Mx2PmOqv29d4yvlsYw-5brwmhKgwMauuMAeVgiZjznYui7Tf7KmNn5sFsruaNJLcQyIeGdMVxRtehdhDphm-m-JpBtLsGvjccR-b4wcSzUN3UR8d5I_xGmjAWaixvhekY1CgZvtenEaieb3GJkHUjASQIWGEzOSbkj-bhKrsJa43EodZNz0SO0Vjl86QEJdGgt_xZyU5l277cj5M_3u8JdKV4v0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی
پ
ِت‌پِتی :
من هانی رامبد رو بزرگ کردم ولی بهم خنجر زد. بهم گفت نباید پشت جمهوری اسلامی باشی ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22866" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22865">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تلگراف : اسرائیل تیم بریتانیایی مستقر در کرانه باختری را که خشونت شهرک‌نشینان علیه فلسطینی‌ها را رصد می‌کرد و قرار بود مأموریتش را گسترش دهد، از این منطقه اخراج کرده است. این اقدام در پی تحریم‌های اخیر بریتانیا علیه شهرک‌های اسرائیلی انجام شده است. اسرائیل پیش‌تر نیز در واکنش به این تحریم‌ها، تعطیلی کنسولگری بریتانیا در قدس شرقی، توقف برخی برنامه‌های آموزشی بریتانیا برای نیروهای تشکیلات خودگردان و اخراج نمایندگان بریتانیا از یک مرکز هماهنگی مرتبط با غزه را اعلام کرده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22865" target="_blank">📅 14:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22864">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رویترز:
جهش نفت فقط ناشی از ایران نیست؛ همزمان
حوثی‌ها بندر مخا را تصرف کرده‌اند و به باب‌المندب نزدیک‌تر شده‌اند
. بنابراین دو مسیر حیاتی نفت و تجارت، هرمز و باب‌المندب، همزمان تحت فشار قرار گرفته‌اند. رویترز می‌گوید نفت این هفته بیش از
۷٪
رشد کرده و در مقطعی رشد هفتگی به حدود
۱۳٪
رسیده بود.
اما بعد از انتشار خبر تلاش کشورهای منطقه برای رسیدن به یک توافق موقت درباره عبور کشتی‌ها از تنگه هرمز، بازار برگشت و آخرین رقم
برنت ۱۰۳.۸۸ دلار و WTI حدود ۹۹.۱۵ دلار
بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22864" target="_blank">📅 14:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22863">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آکسیوس: دریاسالار برد کوپر، فرمانده فرماندهی مرکزی آمریکا، روز پنجشنبه به عربستان سعودی سفر کرد تا در بحبوحه پیشروی سریع حوثی‌ها در یمن، درباره تشدید وضعیت و گزینه‌های مقابله با این گروه با مقام‌های سعودی گفت‌وگو کند. این سفر همزمان با درخواست محمد بن سلمان از ترامپ برای انجام حملات مستقیم آمریکا علیه حوثی‌ها انجام شد؛ درخواستی که ترامپ فعلاً نپذیرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22863" target="_blank">📅 14:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22862">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">علم‌الهدی، امام جمعۀ مشهد به نقل از مجتبی ای آی : ۴ کشته شده در‌ تصادف راننده مست در مشهد با نظر رهبر عنقلاب، شهید شناخته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22862" target="_blank">📅 13:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22860">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رویترز: پاکستان تحت فشار قرار گرفته تا در جنگ عربستان و حوثی‌ها موضع بگیرد.
افزایش حملات حوثی‌ها به عربستان، پاکستان را که هم‌زمان متحد دفاعی ریاض و میانجی میان تهران و ریاض است، در موقعیت دشواری قرار داده است. توافق دفاعی جدید پاکستان، عربستان و ترکیه نیز می‌تواند در صورت گسترش حملات به خاک عربستان اهمیت پیدا کند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22860" target="_blank">📅 13:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22859">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آسوشیتدپرس: عربستان فرودگاه المخا را بمباران کرد.
یک روز پس از تصرف المخا توسط حوثی‌ها، جنگنده‌های سعودی فرودگاه تحت کنترل حوثی‌ها در این شهر را هدف قرار دادند. این نخستین اقدام نظامی مستقیم سعودی در منطقه پس از پیشروی گسترده حوثی‌ها در ساحل دریای سرخ است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22859" target="_blank">📅 13:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22858">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fae9ec34.mp4?token=V8yhe7bF8Ai-E13ifOKt7yfkNHpTeM6ZiwMnbsvbK-0wxp8dtszqs3GD-pR5OgY_IUdSkq7caAw2wOQfZQsCCBwyEnsmlU9KZqt5MKzslVnui0bpfNjPxVjzRyPGlNBOFNFHN2lqVxA9bCbmx78Q8CJuRPKVkeoFUJGCmT8gQNL9aljnLQC1XTVJq_pjHQqgsvNNVvjFsRm0bPhIu3hXYHk-BULag-HdxrK6j9iLImOHCH4cyBb2sSLxqOWv18m2Ej7g0MaH_FUjQyyhMyk4Ny4LXgD03KcGppyKnBnsXsfhs6CTb-KwUvkYoxRp50OZRvBXaAgcK_JL1vFmc8Pj7AffKWkSGoOgq8edk82mjLk8c8JCBivorYFsECmrj7Ka7gdIfPOrNsJRbfs0a6UMZeevxSxCz6m-tCGVW1sqaKgw3ljMXFYZBQC4ZcUCtqfnwNkn6CgmN2uaaBl5kpIG6JBS5mQYnSqjymSsRNv5OMDR_ML1hxw15VhIHJUNApGLfnebcaUNbvKyZzR_7Jo-8GimPRwZWhww4H5W0ZLMf_cUc3ktHwLten2qa4Z82Uxg4SYYoJDTOvkvcrvOFIPV246zXMG6Y0ZLPnI-AhiwIKtITOVDdJzZvbVXMGaEQlDj5Kb4qfb-chG2HSfUY6YKYBkAVNitHgzQIsD_wsDD4DM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fae9ec34.mp4?token=V8yhe7bF8Ai-E13ifOKt7yfkNHpTeM6ZiwMnbsvbK-0wxp8dtszqs3GD-pR5OgY_IUdSkq7caAw2wOQfZQsCCBwyEnsmlU9KZqt5MKzslVnui0bpfNjPxVjzRyPGlNBOFNFHN2lqVxA9bCbmx78Q8CJuRPKVkeoFUJGCmT8gQNL9aljnLQC1XTVJq_pjHQqgsvNNVvjFsRm0bPhIu3hXYHk-BULag-HdxrK6j9iLImOHCH4cyBb2sSLxqOWv18m2Ej7g0MaH_FUjQyyhMyk4Ny4LXgD03KcGppyKnBnsXsfhs6CTb-KwUvkYoxRp50OZRvBXaAgcK_JL1vFmc8Pj7AffKWkSGoOgq8edk82mjLk8c8JCBivorYFsECmrj7Ka7gdIfPOrNsJRbfs0a6UMZeevxSxCz6m-tCGVW1sqaKgw3ljMXFYZBQC4ZcUCtqfnwNkn6CgmN2uaaBl5kpIG6JBS5mQYnSqjymSsRNv5OMDR_ML1hxw15VhIHJUNApGLfnebcaUNbvKyZzR_7Jo-8GimPRwZWhww4H5W0ZLMf_cUc3ktHwLten2qa4Z82Uxg4SYYoJDTOvkvcrvOFIPV246zXMG6Y0ZLPnI-AhiwIKtITOVDdJzZvbVXMGaEQlDj5Kb4qfb-chG2HSfUY6YKYBkAVNitHgzQIsD_wsDD4DM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو چندین تُن سلاح حزب‌الله را که سربازان اسرائیل از رشته‌کوه علی طاهر بازیابی کرده و بیرون کشیدند را بررسی کرد.
پیروزی استراتژیک در مرز شمالی. دهه‌ها زیرساخت‌های تروریستی تحت حمایت ایران به طور کامل توسط ارتش اسرائیل نابود شد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22858" target="_blank">📅 13:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22857">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏شبکه ۱۳ اسرائیل به نقل از مقام ارشد آمریکایی : محاصره اقتصادی و دریایی آمریکا می‌تواند ایران را به سمت اجرای یک عملیات نظامی بزرگ پیش از انتخابات میان‌دوره‌ای آمریکا سوق بدهد. جمهوری اسلامی درحال بررسی یک جنگ بزرگ است که فقط به حمله به کشورهای حوزه خلیج فارس محدود نخواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22857" target="_blank">📅 13:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22854">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOrM5kxH9ycUNWhOQAUJN12iWxpxkPg9FCqg-KUS25cXYFMcIq2ztYcYDBvw-MyPPFXZ0pCTLZ7FKY5LDIeq28eTRTh3-ASIDQL693ALq4vtLSeP_MfQK_LegLYGzqNtVlClS3OeMoLjwrDMbVvBlXUXLgczJ7uVWOG5Ll4AR24CJqtrDjBK2RgIxlHI1YA5qLumNLb4PGlysSKsqm6iYG8uJLVg6GNXThp7pbGm2o45TA7deoTAu5wn2kRsowI3jZmA6qS_lSylvooM8UtCvos-UiS2Vv3IFCGw6DgtbwX7xdgXcVESOlOderhyV72wNnjzsopmnhMfvGtw1Ec-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2iSxykDTGk_x42Xd6y0D-lzk-Iw4RvU0B6WEZYk4nPbJh-JtFIO8HMd9MZkEHwuHPUMrVk4NT9WCFiMx5yE9Sf2w_xXEkgT2FNa8aMLbhkLj8_6frIGmRMYz8NI1uhOE5Cfe0PKTYual52qZfhGUGIOSNlwT0yn8WKcx2suB0JDrwqpb6GQ4F8f3S2o0L-iSwR1k6FX4CpHqc8-VtvGh_49B8r65E_hEupsS1azbGH-_oohYW-g_bXq4jChNRevVrJKpwTsv4l3oIQf2_AtWjIRbkOz9IqV59a8ZR3n2TiyN5fq_Mr4mm_VvhSf0p5oaJ6EIXTkMMqMUBTYqYHJmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZ6ZjKuroHvYl7TFhca3vfRrx4QoKgPKbyZRR24X2xOTXnKC98y0WzUIcnwDVegbosZMnRt_BvTv7N1wE4iYRtbGZp6vzUgTMKtGnecbuPcP_wOKFHInmqYKEBXjr3ueZ3gisSMcEXA04sbQKtrQM7p87BVA-nWbipG7F9te4eSRMqy0Lv73nh_mYG-GLXh_agJsvot_7KSq4K0PBs54vBOJYrsbH-WUVritpfZiBVrS4GHcerbThTp3mCAAq5zvPf7z83VJT1m_V9JpLvZmAqpW8gshQ7JpEhg7uB54Bo4ndIeIjAPNEC19W1iJdeVoAzP945YnJcGKNjfwBSo60g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش های بسیار از ستون دود در شیراز , دیدبان های اتاق جنگ : دقیقا زاغه شیراز هست که همیشه مورد حمله قرار میگرفت
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22854" target="_blank">📅 12:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22853">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">منابع فلسطینی به شبکه الجزیره: محمد الیازوری، فرمانده گردان خان یونس در شاخه نظامی حماس، در یک عملیات ترور اسرائیل کشته شد
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22853" target="_blank">📅 12:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22852">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سی‌اان‌ان: آمریکا طی هفته‌های اخیر
حضور اطلاعاتی و مستشاری خود در عربستان را افزایش داده
و بیش از ۱۰۰ مشاور نظامی آمریکایی، که ممکن است شمارشان به حدود
۲۰۰ نفر
برسد، به نیروهای سعودی در عملیات علیه حوثی‌ها کمک می‌کنند. مأموریت این نیروها ارائه
اطلاعات، پشتیبانی هدف‌گیری و ارزیابی لحظه‌ای میدان نبرد
است و نیروهای آمریکایی مستقیماً در حملات مشارکت ندارند. سی‌ان‌ان همچنین گزارش داده
صدها نیروی سپاه پاسداران در یمن حضور دارند
و در کنار حوثی‌ها فعالیت می‌کنند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22852" target="_blank">📅 12:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22851">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اقتصاد رو با کارتونهای انیمیشن ۳ دقیقه‌ای به رئیسی یاد میدادند !
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22851" target="_blank">📅 11:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22850">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رویترز: قیمت نفت برنت این هفته حدود
۱۳ درصد افزایش یافته
و در مسیر ثبت قوی‌ترین رشد هفتگی از ژوئیه قرار دارد. نگرانی از اختلال طولانی‌مدت در هرمز و پیشروی حوثی‌ها در دریای سرخ، برنت را همچنان بالای ۱۰۰ دلار نگه داشته است.
@WarRoom
فایننشال‌تایمز: نفت برنت به حدود
۱۰۶ دلار
رسیده و ادامه بحران هرمز فشار تورمی شدیدی ایجاد کرده است؛ افزایش قیمت انرژی باعث شده بانک‌های مرکزی از جمله فدرال رزرو آمریکا با فشار بیشتری برای افزایش نرخ بهره مواجه شوند</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22850" target="_blank">📅 11:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22849">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رویترز: منابع نظامی اعلام کردند
حوثی‌ها پس از تصرف بندر المخا در امتداد ساحل دریای سرخ پیشروی کرده و به جزایر راهبردی نزدیک باب‌المندب رسیده‌اند.
این تحولات تهدید علیه مسیر صادرات نفت عربستان و کشتیرانی جهانی را افزایش داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22849" target="_blank">📅 11:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22848">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آسوشیتدپرس: آمریکا توانسته تا حدی
کنترل ایران بر تنگه هرمز را کاهش دهد
و صادرات نفت ایران را تقریباً متوقف کند، اما جنگ همچنان ادامه دارد. جریان نفت از هرمز به حدود دو سوم سطح پیش از جنگ رسیده، در حالی که صادرات نفت ایران از حدود ۱.۸۵ میلیون بشکه در روز به حدود
۲۵۵ هزار بشکه
کاهش یافته است. هم‌زمان حوثی‌ها حملات خود به عربستان را افزایش داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22848" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22847">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce588839b.mp4?token=VOkwT_qh5xbHCQnKSn2MQOCyhELAbr0yfd5h19Eu97dMysdNxFWsSlSV5fppYN_K9Y69EvXubPh6xVPQssjZi9d80GB2bAc_NKdTuErAhePRaF3bmWz2lM4f9kTKNZX7LopoVboswB3ut9ghN6yuT-_QmBm9t2JQeE6xdGU0rJ96RcTCsY-SIloUiDzhZi0OqI_3-sQCXJ1AOqrLGjqllOhGrp4CyAkAGSW-09s4OMf-RCcz4NYJtohTTCNIYehs8Rp1sJYLatennPuZIkmZx1OC3DF7cvMXrhypdRST4k9iI7lkvueItW3yGI01XG-wwVPUdTh5FUEU-gruYnja7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce588839b.mp4?token=VOkwT_qh5xbHCQnKSn2MQOCyhELAbr0yfd5h19Eu97dMysdNxFWsSlSV5fppYN_K9Y69EvXubPh6xVPQssjZi9d80GB2bAc_NKdTuErAhePRaF3bmWz2lM4f9kTKNZX7LopoVboswB3ut9ghN6yuT-_QmBm9t2JQeE6xdGU0rJ96RcTCsY-SIloUiDzhZi0OqI_3-sQCXJ1AOqrLGjqllOhGrp4CyAkAGSW-09s4OMf-RCcz4NYJtohTTCNIYehs8Rp1sJYLatennPuZIkmZx1OC3DF7cvMXrhypdRST4k9iI7lkvueItW3yGI01XG-wwVPUdTh5FUEU-gruYnja7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار
:
آیا ممکن است جنگ با ایران تا پایان دوره ریاست‌جمهوری شما ادامه داشته باشد؟
ترامپ
:
نه. حتی یک احتمال هم وجود ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22847" target="_blank">📅 11:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22846">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اکسیوس: محمد بن‌سلمان، ولیعهد عربستان، روز پنجشنبه در دو تماس تلفنی از ترامپ خواست
فوراً مواضع حوثی‌ها در یمن را هدف قرار دهد
. این درخواست پس از پیشروی حوثی‌ها و تصرف شهر بندری راهبردی
المخا
مطرح شد. مقام‌های آمریکایی می‌گویند واشنگتن ضمن افزایش حمایت از عربستان، فعلاً از
ورود مستقیم به جنگ یمن
خودداری می‌کند و تمرکز اصلی آمریکا بر باز نگه داشتن دریای سرخ است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22846" target="_blank">📅 10:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22845">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فایننشال تایمز:
ایران و کشورهای شورای همکاری خلیج فارس روز دوشنبه در شهر صلاله عمان درباره سازوکار مدیریت موقت تردد کشتی‌ها در تنگه هرمز مذاکره می‌کنند.
این نشست به ابتکار عمان و ایران برگزار می‌شود و نخستین دیدار سطح بالای دیپلماتیک میان ایران و وزیران خارجه شش کشور شورای همکاری خلیج فارس از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران در فوریه است. هدف مذاکرات، رسیدن به توافقی موقت برای تسهیل کشتیرانی در هرمز و کاهش تنش‌هاست.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22845" target="_blank">📅 10:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22844">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کانال ۱۴ : سخنگوی IDF، جنرال بریگارد ایفی دافارین، به عمق شبکه تونل حزب‌الله در تپه علی طار در جنوب لبنان وارد شد، پس از اینکه نیروهای ما کنترل عملیاتی تپه و تخریب زیرزمینی زیرساخت‌ها در منطقه را به پایان رساندند.“این شبکه تونلی طی دو دهه ساخته شد، با بودجه و هدایت توسط رژیم تروریستی جمهوری اسلامی”، دافارین از تپه‌ها گفت. به گفته او، زیرساخت‌ها به عنوان یک مجموعه مدیریتی مرکزی و به عنوان “مرکز مغز” واحد بد حزب‌الله در منطقه فعالیت می‌کردند، از جایی که در عملیات شمالی کراس، عملیات عقاب، و همچنین در جریان نبردهای فعلی انجام شد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22844" target="_blank">📅 07:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22843">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/935a8bd7c0.mp4?token=ukKTBq8MbiUdNWGWJbKcD-aeVjRTRD46vz3RoCwXFl-QupmzPy8S-ummeOsBzwWn_SKwBExaGm96fNrV5gwa5Q1MPCutZyUg7zPf9_L3Y1wuIzSJN6RcUpLzpWNanVck1FtSQuCG9bRm3ckLqKXXHK6c98_feqYVldP3LOKETUQgHTTHXhQItK6KOihtBXa7j1uyjmaXsfS5F_3YGrj5426FB50crbClYenoohlGGFBw-59GFv4DAMmvMS8LFQYfzqA2qSDGwWOlpVYCXm-IZO3WcuHIvGEUmbY9heHytkcOmDntDXLQeFPdixdtBeqDtoMcB6aoMQTmGvxeOHz1tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/935a8bd7c0.mp4?token=ukKTBq8MbiUdNWGWJbKcD-aeVjRTRD46vz3RoCwXFl-QupmzPy8S-ummeOsBzwWn_SKwBExaGm96fNrV5gwa5Q1MPCutZyUg7zPf9_L3Y1wuIzSJN6RcUpLzpWNanVck1FtSQuCG9bRm3ckLqKXXHK6c98_feqYVldP3LOKETUQgHTTHXhQItK6KOihtBXa7j1uyjmaXsfS5F_3YGrj5426FB50crbClYenoohlGGFBw-59GFv4DAMmvMS8LFQYfzqA2qSDGwWOlpVYCXm-IZO3WcuHIvGEUmbY9heHytkcOmDntDXLQeFPdixdtBeqDtoMcB6aoMQTmGvxeOHz1tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ شامگاه (صبح جمعه به وقت ایران)، در سخنرانی خود در شب دوم و پایانی مجمع ملی جمهوری‌خواهان در شهر دالاس ایالت تگزاس، به اقدام نظامی برای جلوگیری از هسته‌ای شدن جمهوری اسلامی و تنگه هرمز اشاره کرد. (دوبله)
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22843" target="_blank">📅 06:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22842">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac2ec14c.mp4?token=ayq6zGhYnXpRkmHAYmJttt8_Z2S7BYPbysJs0bgdyHWP0zYF2NnCvbWFwfr80-JvdBYWxm4gIOSAGyLjBfecKLeQSjnczNoUS3rjPl5qcCBFEdIEBtjdcGxeDESCgBowKu7cARzBBYsGZnq8HYfmWa1dR0Wfo1hrsoaaEb1PwjdNST0ezikYBrZFJQujaoyTySSaOyxFDZHPyiqnt-cnaBSgFxDlD5Ke_DCdF1c-doYNRyF7_J68oH6bM1hB7VmkC9MT1b_FvOOyv2iqJ_wO7jGxqNQYJftwroKRvyQRjFkeMrc0wQoPvES7sYgFGPfjBeW8au0kkypiDzhemxz4Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac2ec14c.mp4?token=ayq6zGhYnXpRkmHAYmJttt8_Z2S7BYPbysJs0bgdyHWP0zYF2NnCvbWFwfr80-JvdBYWxm4gIOSAGyLjBfecKLeQSjnczNoUS3rjPl5qcCBFEdIEBtjdcGxeDESCgBowKu7cARzBBYsGZnq8HYfmWa1dR0Wfo1hrsoaaEb1PwjdNST0ezikYBrZFJQujaoyTySSaOyxFDZHPyiqnt-cnaBSgFxDlD5Ke_DCdF1c-doYNRyF7_J68oH6bM1hB7VmkC9MT1b_FvOOyv2iqJ_wO7jGxqNQYJftwroKRvyQRjFkeMrc0wQoPvES7sYgFGPfjBeW8au0kkypiDzhemxz4Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوکی
.
خدایا کمکم کند.
جمعیت :
خدایا کمکم کند
اوه! حالا می‌دانم. حالا، می‌گویم که تقریباً همه… می‌دانید اگر رأی ندهید چه اتفاقی می‌افتد؟
به جهنم می‌روید.
این را می‌دانید، نه؟ باشه؟ به جهنم می‌روید. و من نمی‌خواهم چنین اتفاقی برای شما بیفتد، پس لطفاً بروید و رأی بدهید. چون باهمدیگر…
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22842" target="_blank">📅 06:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22841">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbe1f11f1d.mp4?token=I2RIrPLFEaS1n0-NWsanh9mHtnEWCoV3Tz_cupBfN7JZL1HyryT_MabscWe_hSV4n_MXhvlKBfDWENsD2neiARAAAasXHp_XCjSikTSmtzs4Bd6RtZrK7n1UCTRVcfXONjUo3uzC6xo8dlS6n_Fdln2VSSQIVQE-gM1cEkUTrzR2LQIctKxr6td3Wxy-sFcOJKF8UF-Fzdq4_7AfBKGz1roz-OJ4rqpx0WNJkg1Lp4y67MJplEqYC4hm9SPrxZhjhMBQH1DpqvEUTmAvAZqG0BGSiUkBbl5rQPvH-p5UQltMde2tuAc-Ft4JDXPPxE13GV57ej_-QOOFd_rOMQf-9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbe1f11f1d.mp4?token=I2RIrPLFEaS1n0-NWsanh9mHtnEWCoV3Tz_cupBfN7JZL1HyryT_MabscWe_hSV4n_MXhvlKBfDWENsD2neiARAAAasXHp_XCjSikTSmtzs4Bd6RtZrK7n1UCTRVcfXONjUo3uzC6xo8dlS6n_Fdln2VSSQIVQE-gM1cEkUTrzR2LQIctKxr6td3Wxy-sFcOJKF8UF-Fzdq4_7AfBKGz1roz-OJ4rqpx0WNJkg1Lp4y67MJplEqYC4hm9SPrxZhjhMBQH1DpqvEUTmAvAZqG0BGSiUkBbl5rQPvH-p5UQltMde2tuAc-Ft4JDXPPxE13GV57ej_-QOOFd_rOMQf-9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس:
اگر ما وارد ماجرای ایران نشده بودیم، شما الان می‌توانستید با خیال راحت به سمت پیروزی در انتخابات میان‌دوره‌ای حرکت کنید؛ با ۲۲۵ کرسی.
ترامپ:
بله، خب، شما این را نمی‌دانید.
مجری فاکس:
آیا پشیمانی‌ای دارید؟
ترامپ:
نه. من اصلاً به کلمه «پشیمانی» اعتقاد ندارم. البته آدم همیشه می‌تواند کمی خودش را مورد سؤال قرار بدهد و درباره تصمیماتش فکر کند، و مردم هم از من این سؤال را پرسیده‌اند. اگر قرار بود دوباره همان تصمیم را بگیرم،
دقیقاً همان کاری را می‌کردم که انجام دادم. توانایی هسته‌ای آنها را از بین بردم.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22841" target="_blank">📅 06:37 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
