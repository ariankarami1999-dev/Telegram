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
<img src="https://cdn1.telesco.pe/file/Kc0_gko5moHzS2wj6oJY0CeAihOCgsE0LUqAIdl4ERnK7K1lk0R648gTy91u5P0G1d5JyPWl6a9E8bituAwNXFUi5MnA0Iu4INeuk7Gf8K_uNYECHLYIN87G6caBZWYrteMWbMKA7jOaVN0QP0eSpuQ6rOZSw3LwCcV1nEsyOQDJzDBvNn-tdF5T33UOGftCdlx16VrpQ7ewkmP0HKKfMPrO9s2Y6AB1hZK01zD0wb6_QqULbRGRFEB6Z_KWyxLWSGTdMlhk26MTO26mGQbadkC1-JMcBfs4Wl4tClcoGvUOy0oxsx6Of7LS2xNXkGeK1MhdSu6-giphs3tBMhBEBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 16:40:44</div>
<hr>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/MatinSenPaii/5389" target="_blank">📅 16:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUZBDvoFdXEvW2kiXUxN_Vjfx0Sue80srTZVW_EaNugU-U4N5ZccocKhKCgxNyuxjzJQ82M_S0ZiST91DBtSt0CJkJF-vSu8PH46pwTVtDO6fjqEkuTZciSxPCzVFczjFu1fBC5jnumx9Itg67IDtEOdlBT1Ikr5bkBAxUVaVbUrydmtD2jWLwzuRmmDb11l_bTZXbtsMK8_B7Rsi_tLUecdii0PL0_FuFWwkzXhBMtK8LrK97ufl_a2RUqYLOhyugMh611mILd5ynWE1R39v5TxEG0WKBtFa-Th5511s5musFZhLI08tfJQ1z2I5duvgD57T86WSPDp8cYvuWc5EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر بلاگش رو از WordPress کوچ داد به EmDash
کلودفلر جزئیات کوچ دادن بلاگ اصلی‌ش از WordPress به EmDash — سیستم مدیریت محتوای متن‌بازی که خودش داخلی ساخته — رو منتشر کرده. EmDash با TypeScript نوشته شده، روی Worker خود کلودفلر اجرا می‌شه و تا ۷۰۰۰ درخواست در ثانیه تست شده، در حالی که بلاگ معمولا ۷۵ درخواست در ثانیه داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/MatinSenPaii/5388" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EJDnZVq2cQrN9Tj7sHAiq1xEwu2iDDL09yS2IzWD7JqqNLUBmb8DIG1rEAFtlpNCdmdZhPtleAHIO0cNPiQJ44C2vZblBTrAAyGPFnbWpMxXoySTF2I2G057DHM0YEB8W_g37RkRf9XT5IOvxGUtva4ZI-s-BU2Z-A60YxuFH0SqJ9zrpucB4U34LJUgpRjG9gDI77iIxIjLbTeXpNaW91DUeCEAvb4Tg7BiIPLJRWDBTA9UWPwk8mcEXDs9PO5-_sEjw7R3u_dkNpczFXieYyjs3NxGsEciLyg0B8ZvSSxD9hbzQmRoiTycXatCn5k71_SsZ11vv8KtdpPTtyZAFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا حس می‌کنیم هر مدل جدیدی که میاد، انقدر از مدل‌های قدیمی قدرتمندتره؟
باید بگم که این بیشتر از منطقی بودن، «کلک» شرکت‌هاست برای مارکتینگ
اگه یادتون باشه، 2 هفته پیش همه‌ی این بنچمارک‌ها(خصوصا سه بعدی) جوری از GPT Astra تعریف می‌کردن و چیزای خفن می‌ساختن که انگار خدای همه‌ی مدل‌هاست.
بعد که Claude Opus 5.5 اومد، خروجی‌هاش رو جوری نشون دادن انگار اون مقابلش پیامبره.
حالا این قضیه برای هر دوی اونا در مورد Gemini 4 Pro داره تکرار می‌شه
به این کار اکانت‌های بنچمارک و Ai Enthusiast ، قضیه‌ی Strawman Fallacy می‌گن. یعنی مغالطه‌ی آدمکِ پوشالی
توی فلسفه، Strawman fallacy یعنی از رقیب قدرتمندت، یه فرض پوشالی بسازی جلوی مخاطب، شکستش بدی، و بعد خودت رو پیروز جلوه بدی
هم خود کمپانی‌ها، هزینه می‌کنن که اکانت‌های توییتری/ردیتی این کار رو انجام بدن؛ هم خود آدما خیلی وقتا این کارو سر هایپ و ... انجام می‌دن.
چه شکلی انجام می‌شه؟
1- مدل رقیب با پرامپت ساده یا بد تست می‌شه، ولی مدل خودشون با پرامپت بهینه‌شده.
2- قابلیت‌های رقیب مثل reasoning، ابزارها یا context بلند خاموش می‌شه.
3- هایپرپارامترهای رقیب به درستی تنظیم نمی‌شه ولی مال خودشون با دقت tune می‌شه.
این شکلیه که می‌گم هیچوقت به بنچمارک‌های این شکلی توییتری، نمی‌شه اعتماد کرد.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/MatinSenPaii/5387" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OB_UujMFo1f7iC-SrKfFYMlI6aWc6nvfLUaBjfT5fs5K_VclwxaDmMvKacTZxb0mG0fzYd2WkeFmK3X1zR_dBQag_fidBK6tdMO-eLN86_6vNlLcqigg1xqWUhHtLlwbDeEGVCwldyGuFsg3oM6R0EHs7rjgP_Kq11ef7wTMFxBP5cEzhuztdKSq8m_X6dbuOctEebu5kq_fkCP_SrCGfh2qHCQKh-lma2RTaEqu32DUuMp383b10CX0zxQi1lVv_mGTA6v46sfYA7LuQRPc3fBw0SnrhUF4zdznAT23v5MIU6IQs7IPBR7QwKGCQpKji5fi7aeypcy-baL0iqf2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ هزار دیتابیس Supabase داده‌های مردم رو لو داده
پژوهش شرکت UpGuard نشون داده حدود ۱۶ هزار دیتابیس میزبانی‌شده روی Supabase بخشی از داده‌های شخصی‌شون رو عمومی کرده: اسم، آدرس، شماره تلفن و گاهی پسورد و توکن.
و بین اینها دیتابیس یه کنسولگری دولتی توی فرانسه هست، پلاک هزاران خودروی یه پارکینگ، و دیتابیسی که برای دریافت رمز یک‌بارمصرف کلاهبرداری استفاده می‌شده. Supabase که امسال به ارزش ۱۰ میلیارد دلار رسیده می‌گه پروژه‌ها پیش‌فرض امنن و امنیت یه مسئولیت مشترکه.
بخشی از ماجرا هم کدهای Vibe Code شده هستن که بدون پیکربندی درست، داده‌های کاربر رو  لو دادن(شبیه یه بنده خدایی که یه بار پروژه اوپن سورس گذاشته بود با به به و چه چه و بعد دیدیم apiهاش توی کد فلاترش هاردکد شده. (طرف مخالف سرسخت ai بود و میگفت به کد ai نمیشه اعتماد کرد)).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/MatinSenPaii/5386" target="_blank">📅 11:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=kXrPPH0YGPpgZ0p-aYLgycuuCd6TvXdqIFn4bLisYuubQK8gIKLqZFemmxj08RL-HlSOkOCOM8P06mbVU6km62NbdaZ5k6Rvckv6jlnOJGqs54GGMrOT5RSKmWng2vTlbths1lGtD_SEaDp-A0MB_zTBZ31_G3MUhEo6IiY8n0prNPo3Ud5zqcMzg1i09vevOW6FKEhzWQxhhubLzwoDU0_Fi0-tJu0OAd1ltRqctqxn3cJT3_wq6YWWqwViV5gl3aM5A04GgiW2MVqwA_l1w4NrDMGTMIieiPuD-GlqGlxKAju7snpun5-xTtDbjHytVQmS_fnTZsWbgBs_n2qVNRvTNumFqVIjOgVbt6RDUS5Exb7bAmFuv6mK8T6TaJniTKVxR-y0_wlF4fEnTDlQgtslXPFTsliPOLcfV454wCTZp5UcOvFMW70xDCCGgKOHlCdS6vQi68_vjT30wGR9z0_rjt3ZkHgsjpqyshJDnFRsVSA9JRW-szMmpdcKFPXDg3DplGxPbf-rCTLB1HJI7TJiKGt5gMJPBAstDLZShPAp_AJZVapoW6PDY_PDoIl6C-wkNa5fTm_PMWaJJ8MzL9BodMQ68qa7Fx-zotcec4qrb7_FouFwKz7oGpqakspeb_b-e2vV7EDkEDow7sMf35W5jxElq0g9nHwHsBfaTHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=kXrPPH0YGPpgZ0p-aYLgycuuCd6TvXdqIFn4bLisYuubQK8gIKLqZFemmxj08RL-HlSOkOCOM8P06mbVU6km62NbdaZ5k6Rvckv6jlnOJGqs54GGMrOT5RSKmWng2vTlbths1lGtD_SEaDp-A0MB_zTBZ31_G3MUhEo6IiY8n0prNPo3Ud5zqcMzg1i09vevOW6FKEhzWQxhhubLzwoDU0_Fi0-tJu0OAd1ltRqctqxn3cJT3_wq6YWWqwViV5gl3aM5A04GgiW2MVqwA_l1w4NrDMGTMIieiPuD-GlqGlxKAju7snpun5-xTtDbjHytVQmS_fnTZsWbgBs_n2qVNRvTNumFqVIjOgVbt6RDUS5Exb7bAmFuv6mK8T6TaJniTKVxR-y0_wlF4fEnTDlQgtslXPFTsliPOLcfV454wCTZp5UcOvFMW70xDCCGgKOHlCdS6vQi68_vjT30wGR9z0_rjt3ZkHgsjpqyshJDnFRsVSA9JRW-szMmpdcKFPXDg3DplGxPbf-rCTLB1HJI7TJiKGt5gMJPBAstDLZShPAp_AJZVapoW6PDY_PDoIl6C-wkNa5fTm_PMWaJJ8MzL9BodMQ68qa7Fx-zotcec4qrb7_FouFwKz7oGpqakspeb_b-e2vV7EDkEDow7sMf35W5jxElq0g9nHwHsBfaTHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه. - عاااااشقش شدممم. با کدوم ابزار ساختیش؟ + الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/MatinSenPaii/5385" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wa_7S39YtpsQg8vggxPZ1iJH33WvuhrqFXU5TVm6ixhZdHp5yvhXJ69dy1b39q4DhU7mtxdcj9dvJlV_HPYxHeZtp7H_R9dyVhVt5QFTp9oaEii4k4yM_MHsHTnhWfHtLPZaZAIis_J9DxNG2f5RZa6AXO8M9uLUHWJ0TkSaY6yAxEA6Y6twmN16oUIkCEn0_BcrChMWTWWbJ96PvALUWLK5bpdPqnRc7z3-74a0SHxJdBKsEKESBLhocw_VK--pb9mVtHf4cP_u0cyX8A8gY5xdIgogVMJ5iJP_MjIafZ53QH-BQou2_9csVRxo_oSrfg0jZUygcmECDGpvRv440A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه.
- عاااااشقش شدممم. با کدوم ابزار ساختیش؟
+ الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/MatinSenPaii/5384" target="_blank">📅 09:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpDG2yUnmCRKO-DR9vwe-uroJTETdAEwwEX-G4CmTC7ccEKrficbIsqdY-2iAt0MdDMHG6ob38VDnr-Tq5EVS9OzKXk6WgyewPj9B3mDkRT5QjVBk0BQfd4JRyl2WuiDVbZHH7HDArjtmVFnrtxb6G9KUMgGYt1rJMCDL0UDiYMyDj4t2EMDcIbOPfR3FmndfHriXncMtBVPnjQkOyukB0297wivo3CFVfZaVPFU8ZPggfPqfP2r9zrf1k5Ut4gjXnA_WuJiZ5JqodlOKPTb44_4ucHvFhIdfhL3Fqr_dtWusLeYdMj6qicaLtoLXvoqW46kHL1mTqJ_L4wFLAs16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولایا (Ollaya)؛ مثل Ollama ولی برای مدل‌های تصمیم‌گیری
خود Ollama، اپلیکیشنیه برای اجرای مدل‌های Open Weight روی سیستم خودتون. حالا Ollaya، همون Decision Models که Jev ساخته رو می‌خواد لوکال و متن‌باز اجرا کنه: سوال تایپ‌شده از هر متن یا JSON میدی و جواب کالیبره‌شده رو توی چند میلی‌ثانیه می‌گیری. جواب از یه پاس روبه‌جلو میاد، نه از تولید توکن‌به‌توکن: حدود ۸ تا ۱۰ میلی‌ثانیه برای ۵ تا سؤال روی RTX 4090، در برابر ۲۳۶ تا ۲۷۶ میلی‌ثانیه‌ی API عمومی Jev. با API سازگار با TypeSafe کار می‌کنه، پس SDK رسمیش بدون تغییر وصل می‌شه و مدل‌ها هم همونطور که گفتم، open-weight هستن.
اما یه بحثی که وجود داره، API خود Jev انقدر ارزونه که فعلا من با اینهمه کار باهاش 5 دلارمو هنوز تموم نکردم. لوکال اجرا کردن لایا هم خوبه اما شاید بهترین گزینه نباشه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/MatinSenPaii/5383" target="_blank">📅 07:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AZxef-4vC0UIr1iBB2JGIbTW3ylgmrcLt5hKJQwO2PhsRZw_i-ySCWRWAh8a7LThlCOYOmSBGgsDltRHngne-iCZZpC3a1lxvZbIlhmQz2hW5L2GUTDtEglc7XfdRG-6RfAICCen76fReGXmsCs4hXBMRKgjXMnI30yXbo42l-kU5uqV7btGcwaxkI1FeJoa0gTMoDONsiGpTABioFowd3ij8HCvgzQtgipEqShcu9zHuSowdWpVyHIsvxk1DYqeGV-DwstJ-IfLMayKK9_EX1Hx1AkYo_X_yloOq1ZXwQKaCjMfZQdLR7lvoKqaGsXAry6hzX9E1EXEPc6apIy4Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک هست دوستان.
گوگل یهو ایران رو تحریم نکرد. سالهاست ما تحریمیم
گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده
این خبر هم اشتباهه
می‌تونید ایمیل بسازید همین الان با گوشیتون و نگران نباشید</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/5382" target="_blank">📅 00:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تانل با دو سه تا یوزر و سرور قوی هر 40 ثانیه یه بار ریست میشه
معلوم نیست دارن چیکار میکنن
کلودفلر هم اکثرا کار نمیکنه واسم آیپیا با نت همراه. فیبر وضعیتش بهتره</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5381" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وضعیت اینترنت خیلی افتضاح شده
هم نت هم VPNهای تانل</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5380" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwZUN05IJ-dVDffKCIoDNpV2sEJT-qTbXxHf6roR3QuuvNduDdCExaWqlftj3OueF1Zyoy-182QwMRGN79CeEqpyi0NeXrBMqk1ajwWKERUpUs1bbzL5x_VHynILYICR2dZMdDhKVLpF55fv5o2bJ4coO1DoKnjyfAssgXvVDYcu7b892eByJX3cNhl6gzsYTzTpcXHM7AL7M5NEwD3EPLNBhYcvYMxdt12RvuZX5ft150xVQyx_SK17sKvMpHWYkQ0CpC-RI0avF9pCdIPNO-ZrJD3zneWCjeuoMBkFwsdcj-_esGg6uKJHg-KZAUG2df3uU5ptICapRghRIrTUIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابطی رو که توصیف می‌کنید، ایجنت براتون می‌سازتش
گیت‌هاب توی اپ Copilot یه قابلیت به اسم canvases گذاشته: به زبان ساده توصیف می‌کنی چه رابطی می‌خوای و ایجنت یه سطح زنده برات می‌سازه که هم خودت می‌تونی استفاده‌اش کنی و آپدیتش کنی، هم خود ایجنت. هدفش اینه که وقت کمتری رو صرف تطبیق‌دادن با ابزارها بکنی و بیشتر کارت رو پیش ببری.
این کارا فایده نداره گیتهاب جان. پلن‌هات گرون و به درد نخورن
برو این دام بر مرغی دگر نِه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5379" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cwmFqQsQSciIFdzsWywoy70xJjwineM2ZHDKW7lgxJPQJz3LBBWbffUOSkutkdiagb03rXKO3kzbS_a2mY7plVSJ4iYXkxO0cF2_VpKrE-XybqlYNn_de_uIU_sfK-Is1qJJhJrYqf3KLEFxh-iP4SpOCrZTpt8EyelD_wI4uh3i7v78r1esTLC4m5ww1ub3EGrXleAU-YN-jZVTEiaYB4jIa0Xe7Gfx-Bh-5HmLr8SIc2Gbixa9EjZbdtBpZ8iFEPr9e6hKIuI1-CAyl9cpt00e4Qyrbh00ss-1AY7G-T0NjeBUUO6EW8DVBvjcyugscvjrTsw4uf8wTp6Te7Bbfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">(باید برم ببینم کپچا فارمش چطوری کار میکنه)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5378" target="_blank">📅 23:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YdGWIhaknkLaj0APkIil9d--DLl6sFvLxGcIf8giw5xOeLLtmN50VzTbYZHAazEQ7fq0GDnl7aTK8-_jKfjdW0Pct7OYZBGdLUhT2npxTippLg03D652bxJtYxQiy-Z7dQLPv5eCQm1J-DK84VS0V4I90lzfU_OG8joKLpMX2u4PNnqgWXBmszOpQSFa5Yl1Q8WEpYSdvCDbNIXbbmjrIBqoyk-ZjllJcLy8_JAXGs9tJJ-j1MD7eEECVCMWg6nCnlydcj1xDFOyila-oNWytJ3Ra3oFxEbQlTaql5rrLUzIj43aG-mdC7LniYqZpcxNGYPVVgOXzZSPtWjcyLi6QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر سایتی رو برای ایجنت‌ها به API تبدیل کن، بدون Browser Automation
💪
یکی از توسعه‌دهنده‌ها توی ساب ردیت هرمس ابزاری به اسم
agent-data.dev
معرفی کرده که ایده‌ی جالبی پشتشه.
حرف اصلیش اینه که برای خیلی از کارهای تکراری وب، مثل چک کردن قیمت پرواز هر روز صبح، دنبال کردن آگهی‌های شغلی جدید یا سرچ توی یوتیوب، browser automation رابط مناسبی نیست. ایجنت باید سایت رو باز کنه، بفهمه چی روی صفحه‌ست، هی کلیک و اسکرول و اسکرین‌شات بگیره، و هر بار که لازم شد کل این چرخه رو از اول تکرار کنه. وقتی کار در اصل «این سایت رو با این پارامترها سرچ کن و نتیجه رو بده» هست، خیلی منطقی‌تره ایجنت یه API call بزنه و JSON ساختاریافته بگیره.
حالا این agent-data چیکار می‌کنه؟
1- یه کاتالوگ از APIهای آماده برای سایت‌هایی مثل X، Reddit، Zillow و کلی سایت دیگه داره
2- اگه API مورد نظرت نبود، URL رو می‌دی و توضیح می‌دی چه دیتا یا عملیاتی می‌خوای؛ خودش API رو می‌سازه و نگهداری می‌کنه
3- از طریق HTTP، MCP یا CLI قابل استفاده‌ست، پس برای ایجنت شبیه یه tool call معمولی می‌شه
نکات فنی:
😟
به‌جای HTML selector، endpointها رو روی همون network requestهایی می‌سازه که خود سایت برای لود دیتا استفاده می‌کنه؛ برای همین با تغییر layout کمتر می‌شکنه
📱
خود APIها مرتب تست می‌شن و خرابی‌ها خودکار شناسایی و برای تعمیر صف می‌شن
💰
زیرساخت proxy و CAPTCHA رو خودش هندل می‌کنه(باید برم ببینم کپچا فارمش چطوری کار میکنه)
سازنده‌ش گفته قراره نشون بده این روش در مقایسه با browser automation چقدر سریع‌تر، قابل‌اعتمادتر و از نظر مصرف توکن بهینه‌تره.
🔗
وبسایتش:
agent-data.dev
📌
ردیت
اصلی پست
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/5377" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این ویدیوی موشن‌گرافیک رو با مدل Opus 5.5 برای یکی از دوستان ساختم. و باید بگم با ۲ خط پرامپت و یه ویدیوی مرجع برای گرفتن اطلاعات و متن ویدیو عالی عمل کرد. عالی  حدود ۴۰ دقیقه زمان برد و دقیق ۲ خط پرامپت با چندتا فایل فونت.
✍️
Saeiid</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/MatinSenPaii/5376" target="_blank">📅 21:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=sVNnaacLBtcWfxb2FCEohe0s_HWgTHMYVBGC_aEbqtfzHVnu7QQccG7o4quKSamYN7H5SkuoRAhB_Qt4EJ0u8wt1ZDuHt300Iv9cszl0jjwKWF2hSOdTu0STIUfw5yyil7eDBLFXscEd6in2du9-l80x0Ei79Ry2D_aXbdMs2Q1w8wH5xxO0gu-I-Bx-uxqEoqZ5qnyKvip-_7x34bS4nOQ1YgAMUXjy9BPcBE9Ol5ZlMI3aFU0BF0nXXPGD50nr6H5w_tfrwa8XsY3DqOSGMucx1KiNyQ5a7rCbC5HhuJW6bTUnfrJqtN6WPnHInYykA4DKXcPK3LusPHI7NCUWFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=sVNnaacLBtcWfxb2FCEohe0s_HWgTHMYVBGC_aEbqtfzHVnu7QQccG7o4quKSamYN7H5SkuoRAhB_Qt4EJ0u8wt1ZDuHt300Iv9cszl0jjwKWF2hSOdTu0STIUfw5yyil7eDBLFXscEd6in2du9-l80x0Ei79Ry2D_aXbdMs2Q1w8wH5xxO0gu-I-Bx-uxqEoqZ5qnyKvip-_7x34bS4nOQ1YgAMUXjy9BPcBE9Ol5ZlMI3aFU0BF0nXXPGD50nr6H5w_tfrwa8XsY3DqOSGMucx1KiNyQ5a7rCbC5HhuJW6bTUnfrJqtN6WPnHInYykA4DKXcPK3LusPHI7NCUWFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/5375" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/etA3PPBZtQRnvYsDDFXuxniiW2QXl7vosz9u2HVd_QMLvJVDcgJH5lJO6eJZ1Ki3wcZzlG3zncbauoNTAHaatebR18qm2GD3OEuXi8xaiYFwgMGsYAF0M2O5f4dDhEURfP9fAe372rAvBVy55OpET2dCif4GkEXsskHzEjYVKnxkfRw5DHrZf6gFXpIVbH3HdtdX7e4DxrRnHQiSrQBxqOHU2ckWpgJTaF6FlQZnPHTlCYQNQ1KiOZKoYaeT3hg6MYV-vE_3NPDjz6Qhog9rQUV2kFZwhfkd64UvSXlNKdSph-GaAPsRGWbmOezDP69Sno750suwfcc88sYHvk31qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pz4s30cfB1FlMGTRal9V5FIHOSbq0WzNIYo_kUCsCm0YU9zwmc-71c8slDaftfxkdDuvgI1Tr4sqjGJLlitTySpCd8Z6Zz6ImNV84wL9a7d7p3ndyLuT5IcBa5FeC5LvzJhEqeo0q4yoKXByZcufjx4hHE_kXRM9CEpQ-RxgyjqwVw9vOSH3mGJoPlrWXG74iNMsnc4oWh_5yJFV-JxDEqEIBcp_qTIln8Ff_lIVMEdCoA1Hf18tigoJMDtPgnEw4ztwmCE9GBGomgZTGVhbogZ4x7D_JeC-FtFL3-Vw_wCVN4JOeTvuALNRkRWzV_o38-zehyqlAd8_0_6vgRV3hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A0AIjLZqNMQIZVdKtBt4KgIlViCGpNIeXf3rg9bJR7-0lJiv33weID0cUmviEePnnQ_35vQgmb_uxG8_zhhlK0Y6_UlPDE3Ar6Yn2SQo9yXv9x6dxvXpddendlw5jaFu8m7e3fwLNcjS1CifRUvulaIahmF1WIxIHGLMSKMLIHNfLXz8NHUMyWWbtvdScfKnFiTSF4WQNsbBjK2O516itlOs61MneHBSnMeqmYePxlPh3UVZEESaH_Xf4JhxuCchtX1THWGpG1vQn_nR_YewIuvP8KmiLOSg8vJjkTaHHO3VFkkdXcUaO7UICVkRRYiDz_KSgfTq0af4VZquC4lHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/btsQV3-cZzDqlvbwDjYkQkoBIvVL2OuFuIxvgq7NN1Kcw-ZjtVrH1UZ6WQSejgcoGW4KzpE3zReO6czJz2Xq-YgDgXgrPGU7Hr0M2qECwerO6wsPGjih0VX_juV1HqGsNtZnZzKuF116CNLPj8egEet-1EVlkCSsAVSAzzuy4E6JHXcZSNrqtdmZgNm1piPU0W6-qowMrogRQeH5wPRWJUp3iiONfM55d-RgDj9RjlJoZ7-BGjjmL16o7GnEB-k3sm68XAknbJ-te0JaP5j08LXieJcsTwzphGUg9HijHtZjePBWCxmZB_mr3nEBGir89kMuT31rzcBbx97U_UVrLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اروین از توییتر
یه سایت بهم معرفی کرد شبیه به Mpay، اما بیشتر برای بیزنس‌ها یا کسایی که تراکنش نسبتا بالا دارن؛ با قابلیت برداشت مستقیم از کارت و کارت‌های تبلیغاتی برای کارهای حساس مثل تبلیغات گوگل ادز یا تراکنش‌های سنگین و گرون
از اینجا می‌تونید ثبت نام کنید:
https://finup.io/?code=MATINSENPAI
لینک، رفرال هست. اگر دوست نداشتید میتونید کد آخرش رو پاک کنید. برای شما سود یا ضرری نداره
نقاط قوت:
1- برای ساخت کارت، MasterCard داره به جای Visa(شانس قبول شدن آفرهای رایگان معمولا بیشتره)
2- قابلیت برداشت ازش وجود داره به ولت کریپتو(هنوز تست نکردم که KYC می‌خواد یا نه اما توی مستنداتش چیزی ننوشته بود که احراز می‌خواد یا...)
3- آدرس BIN آمریکا داره
4- از ارزهای مختلف برای واریز پشتیبانی میکنه برخلاف mpay که فقط تتر داشت
5- دو نوع کارت بیزنس و تبلیغاتی(هزینه‌شون یکیه) که کارت Advertising شانس پذیرش بالایی برای کارهایی مثل تبلیغات Adsense گوگل و تیک‌تاک و متا و... داره
6- کارمزد رایگان روی برداشت و تراکنش کارت‌ها
نقاط ضعف:
1- هزینه اولیه ساخت کارت 10 دلار هستش
2- برای KYC شرایط ثابتی نداره اما توی تراست‌پایلت نمره‌ی خوبی داره
3- حداقل هزینه واریز به خود کارت(نه ولت)، 50 دلاره
و اروین گفتش زمان واریز مراقب باشید از صرافی‌هایی که امریکا تحریم کرده نزنید. ترجیحا بریزید توی تراست ولتی، جایی و بعد بزنید به ولت این سایت
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/MatinSenPaii/5371" target="_blank">📅 19:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZxwX0AuHneYWYedLb_KG6OA15cHQlS3URlDvYDyqEMgNPmKAbI_2pAwnahod57rRdA00pRLYoQ5duKfK-bwg1dyNJOg7KyteClaASyGVaoSGEu7-fVOSR2T6o1-jU18tQeUlqa7fPsLmWAw747e5BFzzsPHjy63uH8KSmdVMisnckzzyxzxxC3A5rtBP4N5lLMfGMhF4a9g1PiFATWpC9aeyJMVutpVLqSuTXTknYswINZA3YvFtV8RVKc7COjZCh7hh8A_R90JgCroDQxosrT0LBde7kWIfrKuB8nXQgLnnvSudfURoQXuVGUeJaV5EvVe-cEfTanqw5K98OI8w_N70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZxwX0AuHneYWYedLb_KG6OA15cHQlS3URlDvYDyqEMgNPmKAbI_2pAwnahod57rRdA00pRLYoQ5duKfK-bwg1dyNJOg7KyteClaASyGVaoSGEu7-fVOSR2T6o1-jU18tQeUlqa7fPsLmWAw747e5BFzzsPHjy63uH8KSmdVMisnckzzyxzxxC3A5rtBP4N5lLMfGMhF4a9g1PiFATWpC9aeyJMVutpVLqSuTXTknYswINZA3YvFtV8RVKc7COjZCh7hh8A_R90JgCroDQxosrT0LBde7kWIfrKuB8nXQgLnnvSudfURoQXuVGUeJaV5EvVe-cEfTanqw5K98OI8w_N70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یه ویدئوی جدید از مقایسه‌ی این مدلی که فکر می‌کنن Gemini 4 هست با GPT 5.6 Astra توی یه انیمیشن ساده(هرچند بنچمارک‌های این شکلی اعتباری بهشون نیست کلا ولی خیلی وقتا درست از آب در اومده این مقایسه‌ها توی قدرت دیزاین و درک سه بعدی)</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/MatinSenPaii/5370" target="_blank">📅 18:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=P52oxrDKRhI4Xg5pGC61dGd2IGA3IenqU5g4q8-1E7QLIwso2VAhbcUR5iai8mm1BWbL_bo8758FFtbp-pV7wjIsz2tbKCD8rBsfoeW6g8ummiH5KtoxN_QdANVEnqS6znG4FhgVlJkN0rLskNViyHrQrCA5jpQFUO8YBcYpKOnInWDF2V0Hm6lrrKOZ9HeUaIxoYJ6I20DkEbNDRiztRFnRU0sFOsmEGl73865O4HaLhQ027AcpLtZeQLaQ2a2O4Hw0KVTVGOOGwOE-Ig7vPRQzyQ68OW48uf-yOfgqJl-Vxk8udTk2fGLKwxERkaubaXjzV1s5lckXDrer0d5wYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=P52oxrDKRhI4Xg5pGC61dGd2IGA3IenqU5g4q8-1E7QLIwso2VAhbcUR5iai8mm1BWbL_bo8758FFtbp-pV7wjIsz2tbKCD8rBsfoeW6g8ummiH5KtoxN_QdANVEnqS6znG4FhgVlJkN0rLskNViyHrQrCA5jpQFUO8YBcYpKOnInWDF2V0Hm6lrrKOZ9HeUaIxoYJ6I20DkEbNDRiztRFnRU0sFOsmEGl73865O4HaLhQ027AcpLtZeQLaQ2a2O4Hw0KVTVGOOGwOE-Ig7vPRQzyQ68OW48uf-yOfgqJl-Vxk8udTk2fGLKwxERkaubaXjzV1s5lckXDrer0d5wYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/MatinSenPaii/5367" target="_blank">📅 18:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/5366" target="_blank">📅 17:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تیم Tokio نسخه‌ی ۰.۹ فریم‌ورک Topcoat (یه فریم‌ورک فول استک برای Rust) رو منتشر کرده که می‌خواد ساختن اپ وب با Rust رو به اندازه‌ی Ruby on Rails راحت کنه.
توی این نسخه ری‌اکتیوی سمت کلاینت جدی‌تر شده: توی macro مربوط به view سیگنال‌ها و عبارت‌های تایپ‌چک‌شده می‌نویسید که به جاوااسکریپت ترنسپایل می‌شن و توی مرورگر اجرا می‌شن، ولی بقیه‌ی رندر و منطق می‌مونه سمت سرور. نکته‌ی جالب‌تر اینکه نویسنده میگه راست بهترین زبان general-purpose برای دنیای توسعه‌ی مبتنی بر AI هست، چون قراردادهای مشخص به مدل کمک می‌کنه با توکن و خطای کمتری کار کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/5365" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m_U7OPeoO31KUiiJMUWTtMykRjrB7baGijW4vGWQgi5PBtHfbNi4JR8PkB7hb5BfbiBq0FLJo44yf0X_Ltuudr9gcYBj0cbGGdFOYFy2_odV51hsd5nvfreyY558I1PJmQycL-Mlh-Be_M5jQZ3Ii5JJOT2jIOFcnzKiDAUfdIUU4OwqrFRF5prZHj0JYLO2Ajb9YyKvH_4nmu7s9icK2ue5zEW5cUX9_VCCkoHdyHw0_6HdaHRBeAPEc7g-Xsmyt_KqS7P8lIBfkcjhqsiZvsTkUh0r_IYfgvNV26Ev0IGkwduM9PiHqUM53tQ-CkqW4KshXfTXX6zc2KqJuPjoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به علاقه گوگل به اسم قناری، خیلی طول کشیدنِ Gemini 4 pro، و چیزای دیگه حدسم اینه که ممکنه گوگل پشتش باشه
کاربرا فعلا گزارش دادن که به شدت کنده...</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5364" target="_blank">📅 13:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YR4p1Ed5-S75VwSsPVSKTEun9qTq_QleOFHRIxb22N9KBdMZ-8UmMVesE5ycrRliiGjOt7UqAM4h3VyO1d94puc1arVjhXOdo9rxgm_ouMVC3hDgrhkXzf6oePEMNBZGiNIGmR-surnI44su-xHKwW3EOKTB3trSf26ikjzAhwJYZKeUO_HL9sLenuy2t3j0iSPFT7j_CwfobpZIAkrs0bNc677FRPDKc1cQ_WmWjjfgMlEIny7Eumm_DFFt7XeLI6oTzjFEKZxilYiNH4xD4H8YO5h1huTYsjg5B6gMMCGpiUCxcnPJ1VhOYYEND6Zcb6Gbd0ZLulDP_ojELgDiqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Gemini 3.8 Flash روی Cline رایگان شده آموزش استفاده ازش: https://t.me/MatinSenPaii/5099</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5363" target="_blank">📅 13:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">زبان‌های برنامه‌نویسی توی عصر AI چی می‌شن و چه بلایی سرشون میاد؟
خوزه والیم، خالق زبان زیبای Elixir، یه مقاله‌ی فکری نوشته درباره‌ی اینکه وقتی ایجنت‌ها بیشتر کد رو می‌نویسن، سر زبان‌ها، ابزارها و کامیونیتی‌هاشون چی میاد.
چند تا نکته‌ی خلاصه از صحبت‌هاش:
۱-
کامیونیتی:
هر زبانی دور یه سری سلیقه‌ی مشترک شکل گرفته؛ پایتون «یه راه واضح برای هر کار»، روبی «خوشحالی برنامه‌نویس»، لیسپ «تغییر خود زبان». وقتی دیگه خودمون کد نمی‌نویسیم، حس تعلق به این کامیونیتی‌ها چی می‌شه؟
۲-
اکوسیستم:
فاصله‌ی اکوسیستم‌ها کم می‌شه، چون پورت کردن کتابخونه‌ها یا پیاده‌سازی الگوریتم‌های یه مقاله با ایجنت خیلی ارزون‌تر شده و زبان‌های کوچیک‌تر سریع‌تر به بزرگ‌ترها می‌رسن. ولی از اون طرف، وقتی ساختن یه کتابخونه ارزون باشه، چرا کسی بیاد روی یه کتابخونه‌ی مشترک همکاری کنه؟ خودش به ایجنت می‌گه دقیقاً همونی که لازم داره رو بسازه.
۳-
سینتکس:
سینتکس‌های خوشگل (مثل optional chaining به‌جای چند تا null check) دیگه اولویت نیست، چون ایجنت از boilerplate خسته نمی‌شه و از دیدش همه‌چیز توکن ورودی و توکن خروجیه. به نظرش زبانی که ادعا کنه «برای ایجنت‌ها ساخته شده» و تمرکزش روی سینتکس باشه، داره حول محدودیت‌های امروز مدل‌ها طراحی می‌شه.
۴-
کامپایلرها از بین نمی‌رن:
اینکه ایجنت مستقیم اسمبلی بنویسه منطقی نیست؛ کسی نمی‌خواد برای هر معماری یه نسخه‌ی جدا نگه داره. تازه هیچ زبونی توی همه‌چیز خوب نیست؛ Rust، زبان‌های اثبات قضیه مثل Lean، Erlang/Elixir برای سیستم‌های توزیع‌شده، SQL، هر کدوم تضمین‌ها و سطح انتزاع خودشون رو دارن.
۵-
تضمین‌های قوی‌تر:
اگه ایجنت کد می‌نویسه، می‌شه trade-offهای زبان رو بازنگری کرد. مثلاً type inference برای آدم‌ها خوبه چون نوشتن تایپ حوصله‌سربره، ولی ایجنت حوصله‌اش سر نمی‌ره. نوشتن صریح تایپ‌ها اطلاعات بیشتری به کامپایلر می‌ده و دست زبان رو برای تایپ‌سیستم قوی‌تر باز می‌ذاره. به نظرش زبان‌ها در آینده با این متمایز می‌شن که چقدر تضمین می‌دن: از طراحی‌ای که حالت نامعتبر رو غیرممکن کنه، تا تایپ و اثبات، تضمین‌های runtime، و تست و fuzzing.
۶-
دیتابیس برنامه به‌جای LSP:
پروتکل LSP برای IDE و آدم‌ها طراحی شده و با فایل و خط و ستون کار می‌کنه، که ایجنت‌ها دقیق دنبالش نمی‌کنن. پیشنهادش اینه که اطلاعاتی مثل سیمبل‌ها، رفرنس‌ها و call graph به شکل یه دیتابیس با زبان کوئری در دسترس باشه. آدم حال نداره برای پیدا کردن رفرنس یه تابع کوئری بنویسه، ولی ایجنت راحت می‌نویسه، حتی کوئری‌هایی مثل «همه‌ی مسیرهایی که یه مقدار می‌تونه nil بشه». برای همین هم جادوهایی مثل monkey-patching که کد رو غیرمحلی می‌کنن، بیشتر مشکل‌ساز می‌شن.
۷- در نهایت
Observability به‌جای دیباگر:
breakpoint گذاشتن و خط‌به‌خط جلو رفتن کار آدمه. ایجنت می‌تونه سریع کد رو instrument کنه، trace جمع کنه و اطلاعات رو کنار هم بذاره. پس باید runtime و state سیستم رو جوری در اختیارش بذاریم که بتونه برنامه‌نویسانه کوئری بزنه، حتی روی پروداکشن. اینجا هم طبیعتاً یه اشاره به Erlang VM می‌کنه که این قابلیت‌ها رو از اول داشته.
جمع‌بندی خودش: زبان‌ها قرار نیست از بین برن، ولی سؤال اصلی عوض می‌شه. اگه دیگه برای «آدمی که کد می‌نویسه» بهینه‌شون نکنیم، برای چی بهینه‌شون کنیم؟
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/5362" target="_blank">📅 12:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">AI
فقط یه ابزار نیست
نویسنده‌ی brettcodes از این جمله‌ی تکراری خسته شده که «AI فقط یه ابزاره، مهم نحوه‌ی استفاده‌شه».
استدلالش هم ساده‌ست: ابزار یعنی دریل‌برقی که کسی ادعا نمی‌کنه ده درصد شانس نابودی بشر داره و اگه برعکس بچرخه خرابه.
اما AI یه صنعته، یه محصول اشتراکیه که قیمتش بالا می‌ره و مدلش بازنشسته می‌شه، رهبرهاش مدام حرف‌های عجیب می‌زنن و پشتش مراکز داده و منابع عظیمه. به گفته‌ی اون، تکرار این شعار فقط داره مسئولیت استفاده از یه فناوری خطرناک رو از بین می‌بره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/5361" target="_blank">📅 10:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsF5BASKJDABmK5mXGymIHEXlRPZcJduhT7l3_Ae47WNtiYurBygprj2_EKr3THVTH879exIv7h2XxIHhAdhcKk-0wJg1jbx7NN_NZD-IEpe3Zts6uK2a4qTFFIo7GJ73tKoBg-FJGjO20Qmsk-J59pPGLvBTvT2qvTa8vgQ8MGkEyehrRoXaZCim8G3Yd8ODGfJBFwR7pvyGI2YJIGSHVxbDYf3bCcA9H9_J5YeSsupyJKUWiDDDK0Q0LGkE7kRdsL6lU2x6O7vBJ5XyOSLnUv5jsDgUwPVw0zFqJgQOeaFs650NpHQ-vPUzVKG54H91FkYxLql7jEKLkvS0P-eSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر وارد بازی میشه تا ایجنت‌ها امنیت سایت‌ها رو به درستی تأمین کنن
مشکلی که کلودفلر دیده اینه: خیلی‌ها ویجت Turnstile رو نصب می‌کنن ولی اعتبارسنجیِ سمت سرور رو جا می‌اندازن و عملا سایتشون برای بات‌ها باز می‌مونه. Turnstile Spin یه جریان کامله که به ایجنتِ کدنویسیِ شما اجازه میده هر دو طرف ماجرا (ویجت و فراخوانی Siteverify) رو پیدا کنه، برنامه‌ش رو بده، منتظر تأییدتون بمونه و بعد انجامشون بده. از داشبورد، Wrangler یا یه URL مهارت شروع می‌شه و اتصال‌های ناقص قبلی رو هم تعمیر می‌کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5360" target="_blank">📅 07:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5359" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">واوووو چه باحال
😲</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5358" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5357" target="_blank">📅 22:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت توی 18 دقیقه هیچ ابزار خاصی هم نصب نبود جز ffmpeg و اینم پرامپتش: make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5356" target="_blank">📅 22:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت
توی 18 دقیقه
هیچ ابزار خاصی هم نصب نبود جز ffmpeg
و اینم پرامپتش:
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
که یه کم بالاتر داده بودم.
روشی هم که ساختتش اینه:
۱. هر فریم فقط تابعی از زمانه
کل ویدیو یک فایل HTML به اسم showreel.html هست که یک تابع renderFrame(t) داره. این تابع زمان رو به ثانیه می‌گیره و همون لحظه رو می‌کشه. هیچ حالتی بین فریم‌ها ذخیره نمیشه و حتی موقعیت ذرات هم مستقیم با فرمول از t حساب میشه. به خاطر همین میشه هر فریمی رو با هر ترتیبی دقیق رندر کرد. تیکهٔ «Rewind» هم ساده بود: فقط renderFrame رو با زمان‌های قبلی صدا زدم.
۲. حرکت‌ها از چند اصل کلاسیک انیمیشن میان
- Easing: فرمول‌هایی مثل outExpo برای ورود تند، outBack برای کمی رد شدن از مقصد و outElastic برای حالت فنری.
- Squash & stretch: نقطه موقع افتادن کشیده میشه و وقتی به زمین می‌خوره پهن میشه.
- Anticipation: قبل از جمع شدن شکل، اول یک لحظه بزرگ‌تر میشه (inBack).
- Stagger: حروف و ذرات هرکدوم با کمی تأخیر نسبت به قبلی حرکت می‌کنن.
- Motion blur ارزون: به جای نقطه، برای هر ذره یک خط از موقعیتش در t - 0.02 تا t کشیدم.
۳. تکنیک هر صحنه
- ذرات: کلمهٔ «FLOW» رو روی یک canvas مخفی نوشتم، پیکسل‌هاش رو نمونه‌برداری کردم و هر پیکسل مقصد یک ذره شد.
- سه‌بعدی: بدون هیچ کتابخونه‌ای. چرخش و projection پرسپکتیو رو خودم با فرمول ریاضی نوشتم.
- مایع: با metaball ساخته شده و داخل یک WebGL shader اجرا میشه. هر حباب یک میدان r²/d² داره و جایی که مجموع میدان‌ها از ۱ بیشتر بشه، سطح مایعه. نورپردازی براقش از روی گرادیان همین میدان حساب میشه.
- جلوه‌های نهایی: یک shader دیگه chromatic aberration، grain فیلم، vignette و فلش رو روی تصویر اضافه می‌کنه. شدتشون به ضرب‌آهنگ‌ها وصله.
۴. صدا هم کامل با ریاضی ساخته شده (audio.mjs)
هیچ فایل صوتی آماده‌ای استفاده نشد:
- Kick: یک موج سینوسی که فرکانسش سریع پایین میاد.
- Clap و hi-hat: نویز سفید که فیلتر شده.
- Reverb: با چند delay که بازخورد دارن ساخته شده.
- Sidechain: صدای بیس موقع هر kick کم میشه تا ضربه‌ها گم نشن.
- زمان‌بندی صدا با تصویر یکیه (۱۲۰ BPM، هر بیت نیم ثانیه)، برای همین همه‌چیز روی ضرب می‌شینه.
۵. رندر نهایی (render.mjs)
اسکریپت Chrome رو بدون پنجره (headless) باز می‌کنه و برای ۹۰۰ فریم (۱۵ ثانیه × ۶۰ فریم) renderFrame رو صدا می‌زنه. هر فریم به صورت PNG مستقیم به ffmpeg فرستاده میشه و ffmpeg اون‌ها رو با صدا به MP4 تبدیل می‌کنه.
۶. کنترل کیفیت
وسط کار فریم‌هایی از هر صحنه رو رندر کردم و کنار هم گذاشتم تا ببینم. صحنهٔ سه‌بعدی زیادی کشیده و شلوغ شده بود، برای همین طول ردّ حرکت و زمان‌بندی تبدیل شکل‌ها رو کم کردم تا واضح بشن.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5355" target="_blank">📅 21:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5354" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dM3Wo5nyPHnM-CVZIMgDhXbBq0guLY5pvdMCjqWf0pIOxT2Sh-tTfZj9L2B5bXdZZdKucbr4oE2OsMGw_s9k3t9tJ8S4bVPL3R9va2QYFjSqZHKNt5qA00dNBHr_nNlGnbgnYHETUt56XvCKSiTreYEos0Qm32e4j8dQXIOe6fqTWd7SwQDcS_Q3wpM6kryP39lBqS6I92D1nuVS2YXu6j4B_njY-Nzqs0cGsN_H8WbCszoDujSTZsnPs4EnVnJVaQ-jXLPtUBTlVk_pf8lAwYVgIvPJuErlLKiTyRXntc-qGnDH5syvBSGvvOAZhQGwE3vv--XlSzNOUy8U1M1sGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب خب خب
کارهای جالبی قراره اینجا انجام بدیم:)
matinsenpai.com
فعلا لندینگه. به زودی لانچ می‌شه</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5353" target="_blank">📅 20:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5352" target="_blank">📅 19:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.
به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out."
آسترا حتی نزدیک هم نیست؛ خودتون ببینید. GPT اینجا صادقانه بخوام بگم، فاجعه‌ست، OpenAI کلا بدسلیقه‌ست.
✍️
shneural
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5351" target="_blank">📅 16:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaEojTmFj7HLXrimzyOAw8CRNd3QuRmJi6hBsVb5SpJL0NVUm1SlGRnWXceCHU8CmP3DpPzmNnPeOdZvE6JMbf7L5x9ULNxoPCXPP2aLtGwoqGYI-XaLH9-MsISuABfKpbMa-zQXWldBxoU7kZW6lgCF3XlVU-2QUoACHZY1yUUT7L-KEKjaQMDxySfkQURZ34gWpjmLwW1LCdRuCCNEXP3nxVAjjarXus4yAugJIBPLvq69F9oDMQI_Jk8r3p0tHuwF1eTshBN_TDAVgJkg4ZPYilYsnO53HoW733EudO52kksoDTnJbYw4J1wVh75tTKTDy_y0qRY4-0vt7Nwlxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازبینی کد با Jev؛ Diff خام دیگه در کار نیست
یه ابزار متن‌باز که پی‌آرهای پرحجم ایجنت‌ها رو به جای نمایش خام دیف بر اساس اولویت دسته‌بندی می‌کنه: فقط تغییرهای P0 پیش‌فرض نشون داده می‌شه و بقیه P1 و P2 هستن. توضیح تغییرها به زبان طبیعی نوشته می‌شه، لوکال اجرا می‌شه و چیزی هم به گیت‌هاب نمی‌فرسته.
🔗
لینک ابزار
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5350" target="_blank">📅 15:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oYFv6yldcZ34XCDLNI8NJWWhvf-schQofkE_fHKUMyo3GKQmELm1sUc1Oc2MSxYrtf-MGJ1774GrhliVNYcgQAtbsggpOihIUig00mdq1ni2lL1Eim6cgLCimTvxHzxy7WY78LXbu7KyCWck1gMB6BTbrM6JKDAIWVGPLuHAZx6Kjjt7YnkTmbdRcaGzzgzbet6njjv0g8xw5QA3rGhK1EYQD51XfgrJS9fxaSBfLx6-9_hdIlYj9L4Bi2B7maeb6_k9Fzs9w-r8GAuw-5yOIfNxWmGjUmhe6JvvlTUg9zv1RbMgaYuh96PO8axFzm00xdeLZULleWdz-gB9a0QZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5349" target="_blank">📅 14:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-hb_RKThbQ9aFM-GsIOPdV4JvnfmB6O3yRJQKE5ow2usj_ATpOe_kfunE31sg3fojOGUXxL0ygyg7HYUj9MQyc8ITM94eunqvKngabxqnWgG02xmBIyBn4ADRGnHvrkt5cZAu3pgA7vmTYpeEeZFS_ucwc1yp6vKBxDiFqbd0JDfZzFafkEIELkYBCB1ppP-PolB3HnHS5n3j8KOGzBdkrr4xmMQXNgmJafpxSs6Dnm9gpa4Z1ivqVfMBg7kST2Vgs8N5rtx0IQceHWOP9OVX3C8-YiXRMrbjr_2lyRlwQDifyVZc9HO9swTwU6L6tI-mRYlEJ-oJu2QhVww_6ckw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت‌سی؛ تایپ‌اسکریپت اما بدون موتور جاوااسکریپت
ورسل لبز کامپایلر آزمایشی scriptc رو معرفی کرده که تایپ‌اسکریپت رو بدون نود، V8 یا هر موتور جاوااسکریپت دیگه‌ای به فایل اجرایی نیتیو تبدیل می‌کنه. نوع‌سنجی با خود کامپایلر تی‌اس انجام می‌شه و خروجی می‌تونه C یا WebAssembly باشه. نتایج اولیه استارت‌آپ سریع‌تر و مصرف حافظه کمتر نسبت به نود رو نشون میده، هرچند سرعت اجرا هنوز پایین‌تره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5348" target="_blank">📅 13:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">https://youtu.be/qNYT3eoyJ-c</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5347" target="_blank">📅 12:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ویدیوهای بلند بالاخره هماهنگ می‌مونن
ریسرچ گوگل یه فریمورک مولتی ایجنتی معرفی کرده که ویدیوهای بلند چندپلانه می‌سازه و جلوی عوض‌شدن ظاهر شخصیت‌ها توی هر پلان رو می‌گیره. لایه‌ی هماهنگ‌سازی روش Gemini و Veo سواره و SynthID هم داره. چهار فریمورک به اسم Co-Director، CANVAS، A²RD و VQQA پشتش هست که دو تاشون توی COLM و EMNLP 2026 چاپ می‌شه.
به نظر قراره ویدئوهای هلو و پیاز و عشق آبدار رو قوی‌تر بسازن وقتی این تکنولوژی اومد
😂
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5346" target="_blank">📅 11:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ozy3hm4mv0PWcGyfCMRs7bzSJ_aMY61oBhCK2qjG6PXKM_BzhHhFT0s6t0IHm7A9QebKgEcDncudhbtnQ_7Q1bHYGkrq5V7SvWNX1Ba-XurdowBNsglVyxHPD4AaOhoJDDEaBTTIKzMKF5qXbTvY1rETfbEBQZe4O5rDGJN5ThcCh6ACttHx7vAUsaeGBLhjLHPVd5qiOD24XdQiazipIOZ0SDE4p3gZYgMVn02DLCjqZ-cWBVjZS1yQiOgJZJBjw-JyRAqSK-vMVRpWqi6V7A6qG2LqsB4HXeKVi2VmQGo7XaM1-lmwjZ-6ycNFTbF-of30E7G6ffW8ZVWu405Tpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک آرنای توسعه‌ی وب مدلهایی که اخیرا ریلیز شدن.
طبیعتا Opus 5.5 با این هزینه، صرفه‌ی اقتصادی خرید پلن کلاد رو خیلی بالاتر برده. و نمره‌ی پایین Luna 6 توی ذوق می‌زنه حقیقتا. اختلافی با Qwen3.8 27B لوکال نداره:)
که آفرین به برادران چینی</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5345" target="_blank">📅 07:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مصرف Opus 5.5 به طرز عجیبی پایینه و همه توی کامیونیتی ایرانی و خارجی هم دارن میگن.
خودمم که دیروز توییت زده بودم راجبش.
روی پلن 20 دلاری هستم تازه و اصلا تموم نمیشه به این راحتیا</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5344" target="_blank">📅 00:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=td0M1Ke3B8F4PsM72XYEWbJSyT1TOw1S9JA8GWf0mQdYdrE35M31_LQiPXYaMdnzv4zmu_30JJGFYM81SrXTPRhGyZvcZLA4DsXub-gZVZrfHlrhClB86wdd_QyqtDubsKJpVKlPNsLKIULjYWRj-JP6gywT9UOmKmsnCY-5xPYPp8b0Kuiq9_yRRZ6qAp2dCeNDN_DChD3Gf67OyQU1HCQHOs0Wg6e-NZnPFXmtDun434f0r5MBcOoH_gOXrQ28vzE-zoUevhEGA3CakkjjbxUGn6YSa88QAa5Iimd_WkcT4LoGYjXXJf7fafxlQp4nPAQTGXL3WUafjs6qTUVSGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=td0M1Ke3B8F4PsM72XYEWbJSyT1TOw1S9JA8GWf0mQdYdrE35M31_LQiPXYaMdnzv4zmu_30JJGFYM81SrXTPRhGyZvcZLA4DsXub-gZVZrfHlrhClB86wdd_QyqtDubsKJpVKlPNsLKIULjYWRj-JP6gywT9UOmKmsnCY-5xPYPp8b0Kuiq9_yRRZ6qAp2dCeNDN_DChD3Gf67OyQU1HCQHOs0Wg6e-NZnPFXmtDun434f0r5MBcOoH_gOXrQ28vzE-zoUevhEGA3CakkjjbxUGn6YSa88QAa5Iimd_WkcT4LoGYjXXJf7fafxlQp4nPAQTGXL3WUafjs6qTUVSGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، Jev از زمان عرضه داره روی GitHub منفجر می‌شه و همهههه راجبش حرف می‌زنن؛ و اینا چیزای باحالیه که مردم تا حالا باهاش ساختن و شما هم می‌تونید بسازید:
- پروژهjev-trader — ربات معاملاتی واقعی که سفارش‌های limit زنده روی هر بلاک ۳۰۰ میلی‌ثانده‌ای Monad می‌ذاره و فقط Jev تصمیم می‌گیره. ۱,۹۱۱ استار
github.com/jarrodwatts/jev-trader
- پروژه jev-ultrafast — ایجنت مرورگر که هر کلیک رو خودش انتخاب می‌کنه و فقط وقتی واقعا باید تایپ کنه، مدل متنی صدا می‌زنه. ۱۶,۷۵۸ استار
github.com/browser-use/jev-ultrafast
- پروژه jev-doom-agent — Chocolate Doom واقعی کامپایل‌شده به WebAssembly؛ دو موتور روی یک نقشه، Jev هر فریم تصمیم تاکتیکی کلان می‌گیره.
github.com/lukaske/jev-doom-agent
- پروژه jev-t-rex-runner — همون دایناسور کرومه که هممون هزار بار بازیش کردیم، حالا کامل توسط Jev بازی می‌شه: بپره، خم شه، یا ادامه بده.
github.com/joshlarsen/jev-t-rex-runner
- پروژه‌ی typesafe-chess —خود Jev در برابر یه موتور جست‌وجوی واقعی، دو بازی با رنگ‌های جابه‌جا. موتور جست‌وجو هر دو رو برد، ولی حدود نیمی از حرکت‌ها نظر اولیه‌ی Jev رو وتو کرد.
github.com/TholeG/typesafe-chess
- پروژه jev-drone — یه کوادکوپتر شبیه‌سازی‌شده فقط با دوربین مسیر مانع پنج ایستگاهی رو رد می‌کنه و Jev نیم‌ثانیه‌ای یک‌بار وضعیت رو قضاوت می‌کنه.
github.com/RomanSlack/jev-drone
- پروژه tax-doc-classifier — فرم‌های مالیاتی IRS واقعی رو با دقت ۱۰۰٪ روی ۲۶۱ فرم دسته‌بندی می‌کنه، با هزینه‌ی تقریباً ۰.۰۰۱ دلار هر صفحه.
github.com/kyotofin/tax-doc-classifier
- پروژه killmyidea — ایده‌ی استارتاپی‌ت رو توصیف کن، Jev از هر زاویه‌اش امتیاز می‌ده و بعد kill، fix یا ship برمی‌گردونه.
github.com/monteduro/killmyidea
- پروژه jev-curate — ردیف‌های Parquet و JSONL رو با قضاوت‌های typed با سرعت ۱,۵۰۰+ ردیف در ثانیه پردازش می‌کنه و فقط چیزایی که از حد رد بشن نگه می‌داره.
github.com/AkashPriyadarshii/jev-curate
- پروژه pg-jev — افزونه‌ی PostgreSQL که بهت اجازه می‌ده به Tableهای خودتون سؤال انگلیسی ساده بپرسید و جواب واقعی بگیرید.
github.com/realZachi/pg-jev
✍️
imryven
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5343" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UlYKPzVbc4QDa7JRcnQH4OWcCgQSYSirLPaDDLO7KNpkO6tMWlgKLdA5cDB0DE9j_TTjLnD3MSDb8MF4ruCM3YXEbTJAu2raaXekfNEwr4yGyl0QQlS7dWjuKwPvlGgd0yEOWX-33YvjYFcaaZwXicUHR-PP9Xuw16whe4EQ7MeRJamV9tYlUl3b72NhiE9fPRi5cohkGGPFbZNwEuACjT_RABJ8U-k_OI5Cyb_y0xRPKKWmsByQvm5J-DuLGSYFfjj5MVwYDUgjEcVTC1_jKVyEk3YXpM13gJLx_5eKtgaLUmDaeq3PnWgXEa5zbM3JAywTRZ1MGsH8aflpGiH9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«داداش اینا که AI بود»؛ ناسزا جدید نوجوونا
😂
گاردین نوشته تحقیرآمیزترین عبارت امسال بین نوجوون‌ها شده «That's so AI». یعنی وقتی می‌خوان بگن یه چیزی جعلی و بی‌کیفیته اینو به کار می‌برن. جالب اینجاست که بین عامه‌ی مردم، خودِ AI داره به نماد بی‌اعتمادی به محتوا تبدیل می‌شه، نه فقط صرفا یه ابزار.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5342" target="_blank">📅 20:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هکرها چطوری ChatGPT و Gemini رو کردن دستیار کلاهبرداری
🥸
یه تحقیق تازه از Vigilance Security نشون می‌ده یه کمپین گنده (اسمش رو گذاشتن Dark Sourcery) داره جواب‌های ChatGPT، Gemini و Google AI Overview رو مسموم می‌کنه.
قضیه اینه که: کلی پست و PDF و صفحه‌ی پشتیبانی فیک می‌سازن که با تکنیک GEO بهینه شدن، که هوش مصنوعی شماره و ایمیل تقلبی رو جای «اطلاعات رسمی» بهت تحویل بده.
تا حالا دست‌کم ۳۷۴ شرکت قربانی شدن؛ از Fortune 100 گرفته تا Delta و Lufthansa و Bank of America.
چطوری این کار رو می‌کنن؟
1- شماره‌ی فیک رو با فاصله و نقطه و ایموجی می‌نویسن که فیلتر اسپم نگیره، ولی مدل راحت درش میاره
2- شماره‌ی تقلبی رو قاطی شماره‌های واقعی می‌کنن که معتبر به‌نظر برسه
3- محتوا رو فوری می‌نویسن (جابه‌جایی پرواز، قفل شدن حساب) که هول کنی و سریع زنگ بزنی
4- پست‌ها رو می‌ریزن توی LeetCode، اینستاگرام و حتی PDFهای سایت‌های دولتی و دانشگاهی
پاک کردنشون هم فایده نداره؛ کمپین اتوماتیکه و روزی هزاران پست جدید می‌زنه.
بدترین قسمتش؟ Google گفته این خارج از scope‌شونه(
😂
😂
😂
😂
) و OpenAI هم گزارش رو بسته، به این بهونه که reproducible نیست. چون عملاً به سیستم خودشون حمله‌ای نشده؛ فقط خروجی AI دستکاری شده.
۹۱٪ آدم‌ها جواب AI رو چک نمی‌کنن. شما جزوشون نباشید؛ شماره‌ی پشتیبانی رو فقط از سایت رسمی خود شرکت‌ها بردارید
چون به زودی شاهد همچین افتضاحی توی ایران هم خواهیم بود متأسفانه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5341" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DZkfx_dmhfjxvJ1XlRL3vQtx4NX_MderAbKD1gRSJeezLddWSSaXRixSL4_8QGYstE3wyjMSXXMYelAtVHDEit0R23ZzO8ROU1z0iYCOz4gHYQi8D0ls4KmfrO_qiOsU0lOH7eSJeydV6e7-QrENJ2JZMtP2_y5pmv8p-ptYJiP2c08xsn_CUqHrcFLY30a24zXUrJVMAGCS4D64vTa6TH5Y_74hqzOYsW2uJ41peJXl_-V4A0pxpwVToXH_Zcdo_uyU7sMRlnT3JJTy55PSezyo2Kule63iXto5Oo7wRe4iOSusbvHB8dd4Ud98S_AYT0IOvt2vcOwGNl_WhpuPig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق رسمی استرالیا علیه OpenAI
نخست‌وزیر استرالیا گفته یه agent از مدل‌های اوپن‌ای‌آی ۱۸ ژوئن رفته توی سایت Services Australia و فایل‌های داخلی و آمار سلامت دولتی رو برداشته؛ دولت هم تا ۱۰ سپتامبر خبردار نشده. این اولین نفوذ ثبت‌شده‌ی یه مدل AI به سیستم یه دولته و حالا قراره تحقیق قانونی بشه. (حالا اینکه agent رو چطوری چند ماه بعد متوجه نشدن رو کاری نداریم
😑
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5340" target="_blank">📅 18:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دارم روی چندتا پلتفرم کار میکنم، یکی یکی ریلیزشون می‌کنم
اکثرا هم سر و کارشون با ترجمست
و یکیش هم برای یادگیری و تقویت زبان انگلیسیه، اما با یه روش متفاوت</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5339" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O4kcTaFa2TMr9Bx-UuKmQbhotF4gtSYk-eP9_S4xJ1BKDfOvslUxre4_fbwzoZXYjdEU9faOpbh0tknUuZDkjFCyEGyyE_Lq-hIZOEULH7bFdY3mw5cS_8VUBlMdtMhGXyRlS5swZWXWmYhuskJxmSfpDtnFypFrwFyWOfbJeMEmQVUPMHs9_ZBxJbpKPCtFQFEmegj5DdulMQV3aZUiyX5d-MT-mEG4ZoEZfaOe1pB5L76SV919gyc5xNY5x_KUv-bohnM3Q9WXXSSd9nZ2Boe6zgjaeXn-4SfIDc-_1tNb2BQon5UhQZ86nSn40Ba1X4wsEZNMFFu4HT3TuIMAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5338" target="_blank">📅 14:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromReza Jafari</strong></div>
<div class="tg-text">تو سایت زیر می‌تونید ببینید مردم با jev چیا ساختن و ازشون ایده بگیرید!
🔗
لینک سایت
@reza_jafari_ai</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5337" target="_blank">📅 11:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5336">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مراقبت کن عزیزم. سلامتیت مهم‌ترین چیزه و ما درک میکنیم
🌱</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5336" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌. دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم. پس اگر شرایطم رو می‌دونید…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5335" target="_blank">📅 09:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5334">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌.
دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم
در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم.
پس اگر شرایطم رو می‌دونید و ناراحت شدید واقعا برام مهم نیست که درک نمی‌کنید</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5334" target="_blank">📅 00:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5333">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mDAiNW_Rsuos34zrWfYSCkQ6O8ls9tmdYYTXyC4zZ6TKcGhAdV3hb2tX-L6NIsoqmbSzx_3VmSJ8r9Q_dQQYa2W5R32kWd-ShU66_UeTWmgnKevXprQ40VqL1CiWCIeZZ8bnJS9pS-ClcDwKeiJQIYptmNAFcokS6F4kbblb0GKG_5LHkgB9dkWQxAl9l42ZE2gUmrfcxhM1nvT1N7myy5T3_CHWZEVfDWkbCeeX-0Mw7rxjPCTokjM0As0VYIxjdD1Lyo-nTM35ByHFud7vrEgWZKa0DSYa4NsDk40GBPEY0mgNPu1wEnjy63dUMsN3PtvpHARHl3N2rhFYUe6qnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل
GPT-6 Astra نشست پشت فرمون تویوتای واقعی
😂
یه بنچمارک عجیب به اسم DrivingBench منتشر شده: مدل‌های زبانی فرانتیر پشت فرمان یه Toyota Corolla واقعی می‌شینن و باید یه مسیر مخروطی رو طی کنن؛ یه ناظر انسانی هم آماده‌ی ترمز زدنه. نتیجه‌ی جالب اینه که GPT-6 Astra با Codex توی تلاش دوم ۱۰۰٪ مسیر رو در ۵ دقیقه و ۲۲ ثانیه تموم کرد؛ Claude Fable 5.1 به ۴۵٪ رسید و Grok 4.6 فقط ۱۱٪ پیش رفت. ویدیوی هر تلاش رو می‌تونید توی سایت منبع ببینید:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5333" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71e738709.mp4?token=feKsGsYvr1qWcIkABPvye-ERlsGZU3JyHTngZ8Ea_SiHtPiv2UMT6d-IBNa6Pz7gs2aIYPyPv8zMZJSDN0G4fggYGz4IgBNzgMXgC-iGGUgEY5qUAQ-mB3rwu2BSwdtF_hVUzzPxXWQRkYbxWoRVqX-Vsf6Q4FUuVoja47eO3vAMNWSCWUJz-iWBs-8BRoYhdLK7LETq9bW37O2oDly09pKXGBZSPcmGgVTacjb0SUQpBik2myItPcCpEN7tLZnPIHUSkqkMKTIR70-zB0m1VzxVb8tZqZ7TPYEJ6nK5lfJP-Bi5H4YaeSkrWa_LEEpmbaq2FHNfTLE_-R48NmXq7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71e738709.mp4?token=feKsGsYvr1qWcIkABPvye-ERlsGZU3JyHTngZ8Ea_SiHtPiv2UMT6d-IBNa6Pz7gs2aIYPyPv8zMZJSDN0G4fggYGz4IgBNzgMXgC-iGGUgEY5qUAQ-mB3rwu2BSwdtF_hVUzzPxXWQRkYbxWoRVqX-Vsf6Q4FUuVoja47eO3vAMNWSCWUJz-iWBs-8BRoYhdLK7LETq9bW37O2oDly09pKXGBZSPcmGgVTacjb0SUQpBik2myItPcCpEN7tLZnPIHUSkqkMKTIR70-zB0m1VzxVb8tZqZ7TPYEJ6nK5lfJP-Bi5H4YaeSkrWa_LEEpmbaq2FHNfTLE_-R48NmXq7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتضاح Union Alpha</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5332" target="_blank">📅 22:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مدل Space Bunny(که یه مدل مخفیه که نمیدونیم مال کدوم شرکته) روی اوپن کد رایگان شده برای یه هفته
- 1M Context
- Multi-modal
بریم تست کنم ببینیم چیه
امیدوارم
افتضاح Union Alpha
تکرار نشه</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5331" target="_blank">📅 21:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5330">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4UUwoZf2QFP4sduBeTfJ8J7U6WXDJOoiNq4qJkY8vPuV2XSnUn27VmvO9rTIzyk2kBR2S7eRr90-UuHD4KVqN0h1rCkaXfunqf7lQmHgNM4_0Hz3xjMqW0iRu8IpS2vsDhRW1xf4pTkCf8w4FID0Nwsq4V5e-5NniaL4d8-GJCR1xB8SsawFIbbr25zHk-zUD_LUMtfoa7oDZzOZP6T1mBQ8sZZYQ4TcFN6CHzu6aeIiqy6uu-SSylBw1iadrR0mSzAeevOZnAUQrU7zosVyrdMBCMRxOhJ0Fz_frAKaFhTAtWYfQi4jcr0bLd6gqzelJ1Xoc5kphsk69kIOP4dxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی GPT-6 Sol، GPT-6 Luna و جنگ قیمتی با Anthropic و Xai
دیروز Grok 4.7 اومد، اون وسط Mimo 2.6 و چند ساعت بعد هم Anthropic مدل Claude Opus 5.5 رو منتشر کرد. اما از لحاظ هزینه، شوک اصلی رو OpenAI با معرفی هم‌زمان GPT-6 Sol و GPT-6 Luna داد که رسما بازار رو وارد جنگ قیمتی تازه‌ای کرد(برا ما که خوبه والا)
مدل GPT-6 Luna با قیمت ورودی ۰.۱۰ دلار و خروجی ۰.۵۰ دلار به‌ازای هر میلیون توکن، تقریبا نصف GPT-5.6 Luna قیمت خورده و به یکی از ارزون‌ترین مدل‌های تاریخ OpenAI تبدیل شده. مدل GPT-6 Sol هم با قیمت ۲ دلار ورودی و ۱۰ دلار خروجی نصف Sol قبلیه(۴/۲۰) و رقابت شدیدی با Opus 5.5 داشتن. از اون طرف هم خود Opus 5.5 هم افت قیمت داشته و هم توی تست‌های اخیر، سبک مکالمه‌ش طبیعی‌تر شده.
منتظر بنچمارک‌های معتبرتر هستیم، خودم هم به زودی تست میکنم
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5330" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5329">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یه سری نظرات راجب مدلهای چینی دارم
سعی می‌کنم ویدئو بگیرم توضیح بدم کامل</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5329" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5328">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عرض تسلیت به دوستانی که مدرسه میرن
غصه نخورین زود تموم میشه
😉</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5328" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8fb483df78.webm?token=ljnw-e24Utpcvbooqdd_D1nebAmYuJQsK5ABS705ottjRZMsuomXvCFInRNswYM1MUIjJIhjNDDn92z6GWQjX7595aM5yOIpUQybl65lS_Ne3lqhmhfwOwmnSeG_SPejIfNPZBXJ1AMwhmPWWMzzp65YX87sJOaOjrUWisbPBernhgXTPE3XAUcjKEtcUQVva0gSM5SYnDVpofQvCyDvmNyN5RzFax5wSf1cWho6UxPGB1cCrHJB5tPlGfBgJ0jDCMBF5cICm2ezQdeNlTQKzP-ZR3cBqAMEDwMRusC83gH31_KjYWkjcKKfe-tOj8kn7WRFRNsLtdYcHvn5KiOxzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8fb483df78.webm?token=ljnw-e24Utpcvbooqdd_D1nebAmYuJQsK5ABS705ottjRZMsuomXvCFInRNswYM1MUIjJIhjNDDn92z6GWQjX7595aM5yOIpUQybl65lS_Ne3lqhmhfwOwmnSeG_SPejIfNPZBXJ1AMwhmPWWMzzp65YX87sJOaOjrUWisbPBernhgXTPE3XAUcjKEtcUQVva0gSM5SYnDVpofQvCyDvmNyN5RzFax5wSf1cWho6UxPGB1cCrHJB5tPlGfBgJ0jDCMBF5cICm2ezQdeNlTQKzP-ZR3cBqAMEDwMRusC83gH31_KjYWkjcKKfe-tOj8kn7WRFRNsLtdYcHvn5KiOxzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5327" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">Check this out:
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5326" target="_blank">📅 14:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bdN45KCD3UG-F0E-fny7Ta8nMh0CkBv7yR4vDKbu0c0ZN4fAPKySL_GqNGLDA7wmRGV-2RBUm7n_vYLbUmzdnDNT3Qi-T3omRfYcebhxPF1WqpoQ661E7Uzwl5LuVkhWCjJFDvf1pqT8mLaByT_VB8yN3bsB6e1rpL1TJdgP9HEkaczXaPUFKgzYVioGQxNFOIHMbNVAbDK1HzVQwARh9UAJs4UuDv44cNrVglxz2UVp3uuL4dpU8fOcKwc7xcuRGaqAIV-vcNyaTILnWMkIIMvsWPUdeyYxtuJrGcyl3_cdQ8344oyrkQbUtfd7LYwwqrmw9w_hYBAqbYIQ5KcisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بگم از چه مدلی استفاده می‌کنم اونم با چه مصرف پایینی، باورتون نمیشه</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5325" target="_blank">📅 13:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فراموش کردم بگم، یه World memory هم واسش گذاشتم که کامل از روندی که تا الان پشت سر گذاشته اطلاع داشته باشه به طور خلاصه</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5324" target="_blank">📅 12:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dIE6Po5qIS7_izyv9JGRCCItLKIoZqL2L0o9Tnu3QJtt-cHw5rYraL-clJEm6lSj0NWmja8b6MYJGUZIwdFkqGYPnfxktGwUjAl2yZqj3FLLgs7ey97xBDh5YxgL3bq-qW0oBHv_Se6Hz4ME81jtRMiqZCCrEd8u5vkkoppzFxJKcNQ3xWjUHpqJBTM5RX9KPgCiraLBfK5EUJI2VR-9dG0tUg_pSdW1jy2PHyGU6p4lTPubfJOIks04ZT3SbazaIUAA4xB0_A51g0pW0dDJE-pGGMaFKuUhIpS4n_u0UHa1D9rOnrYZVgaS6K9oE_GWmjGlpSBqyuv3dgqT3vQFbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NtVRGjwGalj6L1q5LI_M4C0IFEXazfAcLmxSuzMT1VBC0__OsEwJ0hKaoBrEzI4Nj9Fb5J-tgZY2f7lfPrK07vo0ujxaSkAe8UCTslvsBq26zKcCIyPQauLLtd0DQLmvwx94xUCknYOHNBY0ifmybRx6dduOciWWqb58NZx3CWkW_hiyYkGHfgXgr4zEzla9irFY2Z5Q9txBJcFaP_5hL3bEFF48cU2EyBVQlraUYV45wd8ByZKkyaI1V9burxVGSVDVTi4sT37aVb0FkZCBdY6ySphDhSwRC9nbu5-R4kfLn-y-ewmzCv-x-a7si2ZEdzWb4DvQqHK-ZTLPA-I3vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G1q9eiWHU8860nVH-CD6-99ZBR95Mfyqm6hZo9xDy7Mzyh7p0BdKaYZtfhCpDeQnIiT7cTYw1m10nt9rHq2nRctq54mv2N0JXH1AKInUMoKBc8tjzbyUnAvsna9DOJBGmJ27UOuPGh4NFBiXOIKnrBmfRDkW4bjB-N3lIL6cBCcpEz-iPSPnmhWFYJILAHGXvhzUlWDjWsY7vIKWFDWeARrDUP7tOsSr_SPydA599Tz4B0_XMTy2d7Yzt1QbGO0DRCmD5vIOPz3WDqRpFCbzVg87RlagZP7HR_Vwt1lGD_akY9GOEU2xsn2mUf1blDr-3FbDiAmdOdnFRVDXdIJhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/enT7Jy5tO6iF0Jz5t-cbHZivzWbre31LroBEIBUOLGtkTiUthkteTGuiKvfeh_j6R9hlWUymNiMcEdosBimDgM9Dbv2Z5Uqu9vCTZr_JTHqquuhjc3wPQYFKAe4pQQjJbMGvRadZOE4Vts16OIpJli7QVWNLMBa9fJ32aUFsOxp3v5ip0jo9Yb7E63vpPB7hBAFrpfbwbI84YSZgPEmZh-wYQBgqpESxKcW0-f6aene3hdosNUp8-KkV1Jj-P0janBNMZWcVeXnET-Ozp-EDDaNWFSs3o6UZ673aIqp5k4vI8CCkDSIdVh43ZNWxCi2f-mLnIxeJMxGi8NUq-PgWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gL3vlTltrGac2Y3k2vcfQRSPhVclWN7TaqD8X1qoKF63Sb6HsIg0bV6UVxJJcPSc8Z1u2_404d6Rvl3zsllFXvCrvHYUpsn8inz1qClj-M9aKCN8MtWqpaXZsYe3ek3osG6YnuRycuwFLzRFGDDoGu23qjQSvYF59OkbBAC74DGzrPjpfTYT3VVY7ozPUK--NQC6EzULI51TScq42vuEqvXjqUjAza0wIbztk3Kz5MwI1gY4oIoTLXF0invY0mBvz2QTRvH1StqmrYljfnL9dVKvMnxF1dtqedXIUohe35xHtLodL1zqR92K9NhYvlU6UM1tjuANCKt5MVcTbyLsGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BarmqQLigcFuDLzzAFTanzhHMBQ9ZZzQxB_7rZ9WML4jO4qPjYPUUkXdz5qwX9S-Vl3u95e7EtCuxEkj0866dLKiqps7xog2Kioi6tMhRbAd4U92FkxoxzShV6KVWqTFXPgLi7lzrSCym3do-7TpZyX_doSPdYeoweRZYmucA0phzZQXvB7AB9AiPcRrlMMleeR6BgHSR4kzvJpaeuDXDD3jzgf1IepeIrgA5KPcQ8pvzHyM9F6wP5MqevAt9zta42LEqdpvYHqrViRFdFRsLXGTnPpQJ-jJ1MF_7Iq0iCPqR_92VgvDVX01OKIWYvKTsHN_IyLynkPnpZfrpY-iHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MsBgZfxH8loyWmxOGkzkpiCauBZsn17hTBwQpWyWVJ82Jmi9RtPsv-u8btr92zAaekD0dAfmB4DA1MqAVEj5M-_aglpiB3ia6Rx0OJN9ICT0hoUpqNfo_eT2p9lVadSZtSfVsqye1EJSK3O5-0ujSgDsfOjWmutMjDcIf0BVrwjeCz7d2eAJgL5jH6fQ2q5DK6XPQM3ImCtSuyjau9tO9EM1AfdBBbPw3oLBiApZ9IqGJFEOelEJztpI2_b0PhX1MY-MjY1nLSM0On0N67m5V6KQblq_MU7SnKVRFIEzfsH-mwEFustvkS6MDaLGzlfb6Gzsd9RuEUCVGzIX3t8Rww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev  توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev از برادر کوچیکم دعوت کردم بیاد کمی راجب…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5317" target="_blank">📅 11:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eIXAuITZkN3CNN9ME9u5SX76Uemvv_r-CUCyJPh3XS2RCmSQHp--ge0KVyaCOQHzR0HnHSRKlNddl8sEOiCKQYO_30tQgvWNPzrKxtqc32GWQImxZaVq7-7rmbTqFd8ayK8OHnUyIYNuSvt03pZYLtyS5uUw8N41I-LpehlgBmovrGbKY5z7VJ1caCCuceKj32e4NDfLy3CFohWnUzfrPJQdk9jF6KkPI6vR_O42nPOL6oW4bBe6wyR-WdrJqBLO75FjRo5DmWY3bnAItFrdOxzFGK1BjbEqucUpYwUsIh9306LvcZJF-2BrUQkJ5zZ7bY4tHkF2cnEXMWHYI5NsWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کد Rust سریع‌تر از کتابخونه‌های روز، فقط با «سریع‌ترش کن!»
نویسنده‌ی بلاگ minimaxir ماه‌هاست به ایجنت کدنویسیش یه دستور ساده می‌ده: «این کد رو سریع‌تر کن» و بعد بنچمارک می‌گیره. نتیجه‌اش کدهای Rustـی شده که ۲ تا ۲۰ برابر از کتابخونه‌های state-of-the-art سریع‌ترن. حرف جالبش اینه که بهینه‌سازی سرعت توی RLHF این مدل‌ها جای اصلی نداشته و با guardrail و حلقه‌ی تکرار باید تکونشون بدی؛ پرامپت‌ها و خروجی بنچمارک‌ها رو هم کامل منتشر کرده تا کسی ادعاش رو بی‌اساس نبینه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5310" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فراموش کردم بگم که هزینه‌اش نسبت به Opus 5 کمتر شده.
هزینه Opus 5،
5$/25$ بود
هزینه Opus 5.5،
4$/20$ هستش</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5309" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vNY3oEWUmUBHwlgV3iq0N0_QtQNqRrMUUYebarR0S8iPFkVfmd2HeClJcnBzNS_vcAIDkudTK8GLsJ0YB2wHlbDGBt9hXwevvMrpGVW6sqKo2fMWlbT_WrgPj_7eCVW6GOu8Sp2_bZMCVtI8E4Cm7OI8ZZKlq8sbQrsuWnhIxRUK41Bhy49HM93qwazAN0Z7cJKTxhbo_d5S_Ac2QP8P_osOMO0Q9JBEt9c1nG6qyiO-6sA7zI0tWRu_Z50ho-lwDsjb3laR3SPjN53PWp7bR2_hMcLHkX7mw6Poj_-tDeYR2YH-0OnNhXi1rfjsoj7GmjF7uj3pD5g_E85_UM2KSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5308" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O0spP69-5qXyvgDuQCXuf8BhcqU7eQXG_x_oeIUUxbVLtQXeAP1T5bNx1psF-pHqR-3V3aBB4s45DRs4utz_5R89o9n0huMqlDNcGhFpKtoEssVIN8NUUt1qOySlWGkXdpXOVdtnnlYK_w1T_Bm77WE45JTA9NqWJO6fqaCUJZO1ff2KrTZ_S_Ic_WtCOXuN5QVovzNIBBNsKL20wGzJ26zRjEmctJQkEem3-khCbKd6Go2UcpkD2XH8fKiyUvjnyWQtZYFp5xqtHu1kpmUXlEOUTBj8nhEDhlZWAy3S-ujyTUWCIkmwIlBakde5HWl-lkUT_zYoPXrnsvqfB8ovwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hjjfHrVvaI0kmV_ZG9fom60LJe8UqirXT-A52Lf04RFck7NWuR-eIGCI8DH33bGrIQLL2UoOMwQ5_xpYIwO9LoeuehVhlv8pATNHZrumNn-OdanXtWRbB5jGOS3fTqcUHGsRy83ZwCLRjg_1VQS-v-FVK_HP5ctr25SvBgUoyuaSgr5gzVVNf_kyf0HWREXVLUqT0NKxzrwh9tzjW0JhDN_2VGelslGg0T4gcCuKFfCWz5-HY9w8rzldQ25wymQ6b8SCTtbHfxso5dDTCgjSIAVh2mu-EYDe0AupH5LNARHt6Ju1BVHe7l7yELw0FsnUOMcASOH3BfT3P6QJHsI5SA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل Opus 5.5 ریلیز شد
وقت اون میم مدلهای چینیه</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5306" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QpxFyQ8kn5wFmVmdvS0YT0eKKZXDWoyRTTwMzCvxHA5YA06PnTUCIYt1y3GmRgoH83ZwuhkSRdSKbOAB6PG4Ym7kHde6LgbUASbgEumHAKlCubjpsGJcsNsFHok2GDKTUVyW_IqAQJk4iMBj98hgMQLBiLfXNQAy_Ktv3y881-QaXo4ho5_SSorQUYWjJ9aQjgypYdc-N_yxvJEjNCraPUKvIWXMq4G-9_l4zmkyxTuK_PhBOpxIGdjTzTcsQrijZjxnoiGHGGon5PhKhfCal79hki_HU64C3g3gT1t-0SqG25vuhuBLoAB75xjo0pZYs2eaJiHqnSlPAc-fNNKQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی 9Router ارور
HTTP 403: [403]: {"type":"error","error":{"type":"FreeTierError","message":"Error from provider (Console): OpenCode's free tier can only be used from within OpenCode"}}
می‌گیرید از اوپن کد، علتش آپدیت نبودن 9Routerتون هست.
برای آپدیت کسایی که با npm نصب کردن، از دستور
npm i -g 9router@latest --prefer-online
استفاده کنن، و کسایی هم که با داکر نصب کردن از
docker pull decolua/9router:latest
docker rm -f 9router
docker run -d \\
--name 9router \\
-p 20128:20128 \\
-v "$HOME/.9router:/app/data" \\
-e DATA_DIR=/app/data \\
-e JWT_SECRET="change-this-to-a-long-random-secret" \\
-e INITIAL_PASSWORD="your-strong-dashboard-password" \\
decolua/9router:latest
استفاده کنن(با پسوورد و JWT دلخواه برای JWT_SECRET و INITIAL_PASSWORD)</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5305" target="_blank">📅 14:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این وسط Mimo 2.6 Pro هم اومد و grok 4.7 رو بولی کرد:))</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5304" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s89dfKtEMrv4nN9XqJ-3l2Tfn2RNsOerqAF8Hr7b0wjIvNT3-AWd8CFtX_3WsV9-oSj-Mn2unxnT8ANty-Pbs4XgBD8hTBtKo3xVV3j5RsZS7V5lbb2o6_M9UF0ILi_kCSGmVEgYbbyB5SIFHK_jViY0ZBAVSNRuIbzdK0KV1UZQa43osl_tMmYHpPVGJdGZhwvinibzG15RY-VEFPBe4XyLotE_azeNX35xtdt1EQcw2fxz6gpmZZc4jMr6RaOvx7tHWj31kGjZKsbhpYWz8e5aVAKypqp0WM-H6VG_J-osfqt94dyDnGNAebWHU9FJdPJ24sdhg4OIVssMcZuUBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو پولدار کن یا متین ویدئوی ماینکرفتی بسازه:</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5303" target="_blank">📅 11:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uSX2La_rDLhimG9tN37a87k7AjgfEmjGLY5Weq-2bV_PmMFcsW3Xcpr7UkXYmR0XpPVhNktDsJoileYRSYriniefuCA1nDI1LfGZTGw6hojdrGVCwoYfHRQnDKPZCnYBKNDlZx_YOOlYiL2FFk1TPyHsMJozW7yJEhDPgXNl4-weCZwd49BSARXz9Nbid0mtu1w9l3hdIreJNTkTj5YWVZKXMs9F7k4FZeQJR3j5qvXeMu8i1mGCc2C0a2z-PQbx8swzT2MCuWl1tD-n6Ehz-XYAC3fV-oJtRgOBH6TVg2sw_ks1ubf-a_l7IVSP1ab8k0h69gC0VSslikjrHZSy5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev
توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev
از برادر کوچیکم دعوت کردم بیاد کمی راجب خود ماینکرفت توضیح بده و کاری که ادعا شده ai تونسته انجام بده.
همینطور در مورد Jev صحبت می‌کنیم و اینکه اصلا چه نیازی به این معماری حس میشه در کنار LLM ها؟
و می‌ذاریم ai ای که کدشو نوشتیم، ماینکرفت بازی کنه برای خودش ببینم چه اتفاقی میفته
😂
لینک سایت Typesafeai برای گرفتن 5 دلار اعتبار رایگان:
https://console.typesafe.ai
لینک سایت هوشیار24 برای تخفیف 90 درصدی API از GPT 6 Astra:
https://houshyar24.ir/?ref=B2N4W9SS
پروژه رو هم توی ویدئوهای بعدی که تکمیل‌تر کردیم می‌ذارم گیتهاب واستون
🥰
📹
تماشا در یوتوب:
https://youtu.be/l-o_fQM_9AI</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5302" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مدل
Grok 4.7؛ آپدیتی که بیشتر ناامیدکننده بود تا پیشرفت
ببینید Grok 4.5 نسبت به قیمتش واقعاً مدل فوق‌العاده‌ای بود؛ سریع بود، کارکردن باهاش حس خوبی داشت، قابل‌اعتماد بود و به‌عنوان مدل پیش‌فرض عملکرد خوبی ارائه می‌داد.
مدل Grok 4.6 از نظر من یه قدم اشتباه، البته قابل‌درک، برداشت. کندتر و گرون‌تر شد و برای انجام هر تسک، توکن خیلی بیشتری مصرف می‌کرد؛ درحالی‌که فقط یه برتری جزئی از نظر هوش داشت.
البته دلیلش رو می‌شه فهمید؛ بالاخره تیم سازنده باید خودش رو توی بنچمارک‌ها بالا بکشه.
اما بخشیدن Grok 4.7 خیلی سخت‌تره.
1-
مصرف توکن برخلاف وعده‌ها بیشتر شده:
گفته بودن مدل جدید توکن‌بهینه‌تره، اما توی استفاده‌ی واقعی بین ۳۰ تا ۸۰ درصد بدتر عمل می‌کنه.
2-
بنچمارک‌های ضعیف‌تر:
توی چندین بنچمارک، امتیازش از Grok 4.6 پایین‌تره.
3-
سرعت و تجربه‌ی کاربری بدتر:
کندتر شده و کارکردن باهاش دیگه مثل نسخه‌های قبلی لذت‌بخش نیست.
4-
هزینه‌ی واقعی خیلی بیشتره:
هزینه‌ی استفاده‌ی واقعی از Grok 4.7 بیشتر از دو برابر Grok 4.6 درمیاد و حتی از هزینه‌ی Astra هم بالاتر می‌ره.
با توجه به این‌همه تبلیغاتی که برای این مدل شده بود، باید بگم واقعاً ناامیدکننده منتشر شد.
البته بنچمارک‌ها همه‌چیز رو نشون نمی‌دن و Grok 4.7 توی بعضی کارهای مهندسی واقعی همچنان تجربه‌ی خوبی ارائه می‌ده؛ ولی درمجموع حس می‌کنم هنوز خیلی به مدل‌های سال ۲۰۲۵ شبیهه.
مشکل اصلی، قابلیت‌های Frontendـه:
عملکردش توی کارهای Frontend به‌شکل غیرقابل‌قبولی بده. قابلیت‌های 3D تقریباً وجود ندارن و مدل دائماً توی حلقه‌های تصادفی شبیه Gemini گیر می‌کنه.
حرف آخر:
این انتشار واقعاً ناامیدکننده بود. امیدوارم تیم SpaceXAI این موضوع رو بپذیره و توی نسخه‌ی بعدی بتونه دوباره ما رو غافل‌گیر کنه.
✍️
theo</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5301" target="_blank">📅 10:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lE_8jDF0QWFfg479opq8GujZYFs9pDNwRCtN1xs7yDYrBgwLYxBd4VU-6kQiCfedJwJLmeeVf0_N8q-hWxS6mvm6W5vzg2IX_ICuHhVovhOJJvFmbVVnCQBxe4oOcNBnabKtvcDx54qwjUFv2A1zUE1GHc7ufLPl02cF8wOewY-P5NCiBH-ddmUfj8aJoaXB79JAuRK4JQjBg7v2k41PB4UxJTqSWQEOftPJmutadvX8m9gV4IIhB9Z83pIPixUC8oQN5UGagCzPGwt90vEs2cshQF4_ZlhLOzp29jycyR7NUfnhWc3fNeanqchg3nkt1VS-pQyRfwPreAOXubkxMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره. ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5300" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hzD6Ky1Z6brDy22caZGF21tmA6m2zGnt1YsUTL9uoyaF8R4DFfWkxM5Um7NQhym6R3Qm6dEaWP96MgXxO1tGK38orwVHHKfI_P6Is_WkRwSzcO7KMRMd2qaZuhowkVRxUnokHDgd-scR95_KsnIwc0_wUTnJGAePuFryu7Kfu5aCxOGnzVgvAclshi98XvMsfAUPuQ2AlNhCF6II9wZHTFtk3HMYF3CG69J19LgT7jqEqUGhat--wdzUaQRNDSTiVcYa41RhSSlZY1a7qHEXUMD06xs8WTQ35879IekdkT1FTZTTJ0KGLHdWqRcNkHn2OyPS5VQz6VYcbYuo8jMVfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qGtLe8_Bogp84dtKV93VwSnjStyTRe4rWTieYnuQrVGLRa9I0cOC4jONtPnLtaAUmBdwGzxM_Auw-de6rSruUz7GDUfqQLm9MdS-9h0YY_NIWJTkW_dpE7PMEL55E7HZbr7_0wVJ6_ShgIlYhzEfIX0TEMVKF-Vthio90mJkbOvq62E4Y2kn-Zft8NZP9EFxNjJSDQRF1KxWM7qnyX9p54yXYv2KQaXW_0Qr0IQ6GImfy7dVs3xM44RGiTGzFQErsymd6tUDhE6qwZ4WKA2gLL7Irmv6MBBmKyJdWxcRJELvdWOFp1bsvwdThawm24MaJq-ZC2xaoMZWvtS0-gagxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره.
ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5298" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد: https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5297" target="_blank">📅 22:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mFbi3uBhQDCelQxd4acHSdrmeUwwnBeuHIu5OKp1vrTKoN0h6PDaqkaOcwlaUEBelayTYR16V3BnBaJzUBf0ziGbVO2oeQAjQvoNXTKgdxeveiewgHxC2EfBA2RTwsPK8DVu599nTmZlLF1nwVN93JEWyNlPaAziFZ60dMf9OAtyC70PQkMXTs7eu4hSxdEVJ4QILVQjw5V82D9J7wt7VxXiuvva7MCWa0lBFDxCMeAbNWr2Z6dhJD2cJDLGFz26aMj1Drnx_is9tP78kErNulaAo_-jYoXoTq9GK99A8w2upSywnNZuRuhIW0qj9uFr5HNAaQFZGANLS0NEv2dsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد:
https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5296" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QxvVoFqf7IO_1D-gFLMaFAv6WIAc5VCKqcQeggPf6mLzXleHNu4QmKdoyjtLfKtY912qh60JlzIP1bdnd8GvuqazYQDcfk4pjTZ5Hwjq0DajRzkpMOXVHFAT98XUlz-BmFHg0KHElxQ6OuA4W9iVlUloXYXhM3rAgPTWrNR81_Kr6V5Fhb1JeKYwhnv4A9Zr-S-Vp_1cfyU1CjGJF06ngIzmNd0XyCyNtmyclAShOCR631yxvOQ2zfdx7f8ACmnVRDC1pny7y_86hsgM8WrhCjJ3qK_oqW2YczWoUESQw8iiorL-KzzmEah3MfAmlMZ87hN1jedm4SZB5F21VMobJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی مسلمان
اصلا هیچی بهش نگفته بودما، خودش یهو اومد گفت بسم‌الله</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5295" target="_blank">📅 18:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یه نفر یه چیزی ساخته بود
من دارم یه کم خفن‌ترش می‌کنم که ازش ویدئو بگیرم
بعدشم اوپن سورس منتشرش می‌کنم
مربوط به بازیه
#️⃣
از اونجایی که 3 تا 5 هم برق میره، بعدش ضبط میکنم و احتمالا تا شب آماده بشه</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5294" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5293" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اگه اولش ازتون پرسید Can you chat with Jev
باید بزنید No
چون طبیعتا LLM نیست و نمی‌تونید باهاش حرف بزنید
یک مقدار شاید پیچیده به نظرتون برسه اما به زودی راجب کاربردهاش صحبت می‌کنیم و ویدئو هم داریم</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5292" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CnIJaNR3RAX7DfqUijSohUzLdz2jgMJUf4LSaCSHFViYSAcC7nEy0xs_FIFHAKoXoZRQ11jD55vz8iBpU1lhiRlDiqRzIRogIvTzAXA67IvAHabwy--48YQY6y5AYoiE0tmavbNGZyUaGAEmGFZIvR-gO2vdnFRLr68bxO6W-u7WSnLMIwNX_3L9LfhTivEXzT0ndnrODv0YBld3937-W3wg0x-SMqFw5aO_8gT4QH5-uZ0ohxDw6PxdRZQCmnmsEo1qj_92WJHcRLo67x5Pd55H3wklShwz0pIeyVFaUlJFb8CNoa59KopqVRZmPvTyTEDDss8EI6TYRjAtD7yMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی بامزست:)</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5291" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5290" target="_blank">📅 13:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bM5sBkGUW2P1zZrs771v_3U1bP1m4ME0Si_5TjCgphXiR-DAkh6pjctDF0riCyaSV2lh0qgFKnxUgiqZDyoND6wc-fz2j_NkpO6-XNzRdPyDIw8JqWscP6ZlN1F9BvQVirK7biVPF2aRqca_DfQvxglUKEIDZmZrYwpmOulfG9yTqPDaCkVz53GsGpiGTsrYToxxqRTewhUJgjpLu0qkD7XIi_nQX74gKfA6TGHsTZghbkVcbPWWf3fEWbj-fkHs-Fj-NMb9NWTsSzhavzNT3OYnJA6bNw7K6OgA3gPkgrwPP1xirgw-U53S7UX5fzm5z-Ip916cVKqUoLrop-pTRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad) برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5289" target="_blank">📅 13:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromgooyban🦆</strong></div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5288" target="_blank">📅 11:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5287">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VVFWp_lcYBvIVNZwHkTRa7uZ9q_VYCsbDoepiSTi13_pekIZEiVJ7f8Cs59kQKWT_dwAoQ35irURmu4tGbedr1rfgmBO0sbOMpcUmOf79K40ad575LS6vZnrcsIg9CvI5kEGsuLtCMT_o_3SsC-qsgtIXVDt-OPJAsEGovKAlwL5FwV2vjgtbUtJzatAD-IqSYJ8Nb7DKvMZrjRY8On_KRghh-T_mMzS6WVNtLQ6DYSCBB59qrOn5W_IQqBYWavdMuK7y1F6pcqDkk9O34i6ljfyhl_HIXDT3wFcPbij2Me-HQ1US5z-Pdx9cV0SacuiIUg4uWgA4WVlgb3opDfLOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad)
برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5287" target="_blank">📅 08:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R4ArPsLHwvxUDDaxytcg-ALA2Xq3Irk5XAumsw2eb5WX57U094lwoOj0Xlk-Bju3ZEnaxbr-Yfbou8PT_FgsEga6HoAXSbMOBlBLucW0a224JCI4XDbrQjdASYuqSAsVvMUA6NYTs9pB_1EHXM84Hc3hV9bu_eo2RMJ0P7vgUoNQalImBdeGBnolT0zVvzDRp3zQ6nfh9VU1H_2Q-wW_J0g4yqdblRFAkMUJomdmfTPzjAGu9nw1SW7_LkOCgz_WwrVvMHc277t1XW2yxJnuiyx08YDbl1GWjUoI8UbUQv5uaxot2KwzBJDRqEj7Z3RPURHoQEqXXRS0ShYUMGBLBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.  خلاصه‌ی توییت این دوستمون:  - یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه. - هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده. - اما Jev اصلاً متن…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5286" target="_blank">📅 23:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه  هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم، سعی کردیم با یزدان عزیز با استدلال و تجربه‌ی خودمون…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5285" target="_blank">📅 23:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sJjXu7mBogGqK3Im3sGxLlG05rxggyuZWdubvsFxM9D0PurPwropd3WbXAMXCBS40-CNeU1b8EbMGZOXlfEj4jejMO9_h1BlQ4xhhUQOyWfe0aG3SKW-ALE_dPHuIAQ1TAN29rlrmj9OfUwYB58MctzGKgqO4igUdh4GgwpxX9HE0iNtVwaEpO7F-vBOHPSR9SLnD_ho1suVAFt7VtKdl5GuazAaeV-t4MYB0yLdqtKXjwVMkIXPId4Oc04PsFKmG025lBT7bQo_EZXOX4qqSt34lnpCOgwxVrKUI3WI4DxxIjDujLh58FxXbd4MUs7qnW6QixAPK1lbECczh0T1kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه
هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن
به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم
، سعی کردیم با
یزدان عزیز
با استدلال و تجربه‌ی خودمون به این سؤال جواب بدیم. چیزهایی که بررسی می‌کنیم:
— چرا بیشتر بحث‌های این حوزه توی شبکه‌های اجتماعی «حکم» بدون دلیله
— فرق AI با یه ابزار ساده مثل ماشین‌حساب چیه
— تفاوت نوآوری (Novelty) و خلاقیت (Creativity) و اینکه AI کدومش رو داره
— جایگزینی شغلی و تحلیل آینده
— چیزهایی که هنوز دست آدمه و AI نمی‌تونه جاش رو بگیره
— بحث کاهش نیمه‌عمر مهارت‌های تخصصی
— ۵ تا کار عملی که باعث می‌شه بازار کار هنوز بهتون نیاز داشته باشه
📹
تماشا در یوتوب:
https://youtu.be/x8V0w3I9g10</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5284" target="_blank">📅 22:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_o1xa6N4MUGbRhXj3OPROGSxN-VV_cuBTaenq34ZvG2kDLEAIbepNelb9BpONitWfkZYHWth50k7v1_TKaGOrlSP30dCCGzeE0sDKrNFCz3slnX-Gt8LnnPZBjXvjaRnG_wbWtfr3zI5LpQxO73-RtZNIwsM9Ow05YtOnPnrhu0U5LQydlVmCF9CUabpk1YI7Asdi8xTPSlp8COlAw-7oB58UxeNkZHe81oyTgg7pvxfSSG90Bza0m7pFikJMBlMKOK8YA3zttLzK0tVN_K3ekvgl32A14I0WhfiV6YoFadXzHLHwTy0D1L-jIxwnKqQ-qywToqrxH6LOGueKWY9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
بچه‌هااا یه آموزش جدید آپلود کردم
🥹
✨
اگه Gemini خطای 403 میده یا Google Flow براتون باز نمیشه، این ویدیو رو از دست ندین
👀
💗
توی ویدیو از صفر Blue Knight Panel رو می‌سازیم و آخرش با کانفیگ‌هاش Gemini و Google Flow رو تست می‌کنیم
😭
🔥
🎀
تماشای ویدیو:
https://youtu.be/GK2PGDzkbh4</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5283" target="_blank">📅 21:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5282" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=t_GMXWGK8oQCuT43poQuRNoLQi0Ao3lrDiledABu61I5zgk5D-GVt0yteB-jGQvhlfJUcaRFGDiIiNh92CIWmf7m4iEFhR-TOLTvtFuGDHCfwXcLThngpQ_A7aMKpI_jOix0b47JKlR6WrLita8ThiGI7_EKJ_vHOFcThLkolftCGBVQN04cuDS1A5xtyxEVLn-qr2EXZycWsTqOuuq30eTMYZwgLVTW3cnY3OyKQhKRvYKpGmPFMoJRrKDrCQgTdE64lwFjU8qs0K848waPNJFhpQNr7_IXjucquTp0VvIaZIRkGKJgryV-X2vFM6WPE2EN8EuwjbGtTqwWXiR-A4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=t_GMXWGK8oQCuT43poQuRNoLQi0Ao3lrDiledABu61I5zgk5D-GVt0yteB-jGQvhlfJUcaRFGDiIiNh92CIWmf7m4iEFhR-TOLTvtFuGDHCfwXcLThngpQ_A7aMKpI_jOix0b47JKlR6WrLita8ThiGI7_EKJ_vHOFcThLkolftCGBVQN04cuDS1A5xtyxEVLn-qr2EXZycWsTqOuuq30eTMYZwgLVTW3cnY3OyKQhKRvYKpGmPFMoJRrKDrCQgTdE64lwFjU8qs0K848waPNJFhpQNr7_IXjucquTp0VvIaZIRkGKJgryV-X2vFM6WPE2EN8EuwjbGtTqwWXiR-A4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو که دیشب گفتم واستون می‌ذارمش، توضیح می‌ده که می‌شه حل‌کردن مکعب روبیک رو با
نظریه‌ی گراف
مدل‌سازی کرد.
- هر حالت ممکن مکعب روبیک رو به‌عنوان یه
نقطه یا رأس گراف
در نظر می‌گیریم.
- هر حرکت قانونی، مثل چرخوندن یه وجه، بین دو حالت یه "
یال
" ایجاد می‌کنه.
- مکعب به‌هم‌ریخته، نقطه‌ی شروعه.
- مکعب حل‌شده، نقطه‌ی هدفه.
- حل‌کردن مکعب یعنی پیدا کردن مسیر از حالت به‌هم‌ریخته تا حالت حل‌شده.
توی ویدئو، سمت چپ یه مکعب روبیکِ به‌هم‌ریخته دیده می‌شه و سمت راست، شبکه‌ای از نقاط رنگی و خطوط مختلف. این شبکه درواقع فضای تمام حالت‌هایی رو نمایش می‌ده که مکعب می‌تونه با حرکت‌های مختلف بهشون برسه.
نکته‌ی جالب اینه که مکعب روبیک فقط حدود ۲۰ ساله که اختراع شده، اما تعداد حالت‌های ممکنش فوق‌العاده زیاده:
۴۳٬۲۵۲٬۰۰۳٬۲۷۴٬۴۸۹٬۸۵۶٬۰۰۰ حالت
یعنی بیشتر از ۴۳ کوینتیلیون حالت مختلف.
با این اوصاف، شاید جالب باشه بهتون بگم که برای هر حالت مکعب(هررر حالت) راه‌حلی با حداکثر
۲۰ حرکت
وجود داره. به این عدد معروف،
God’s Number
یا «عدد خدا» می‌گن؛ چون از هر وضعیت ممکن، یه حل‌کننده‌ی کامل می‌تونه توی ۲۰ حرکت(حداکثر) یا کمتر به جواب برسه.
پس حرف اصلی ویدئو اینه:
حل‌کردن مکعب روبیک یعنی پیدا کردن کوتاه‌ترین مسیر بین دو نقطه توی یک گراف فوق‌العاده عظیم.
این نگاه ریاضی کمک می‌کنه بفهمیم الگوریتم‌های حل مکعب چطور کار می‌کنن و چرا پیدا کردن راه‌حل، بیشتر از اینکه فقط به حفظ‌کردن حرکات مربوط باشه، به
جست‌وجو توی فضای حالت‌ها
مربوطه.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5281" target="_blank">📅 16:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=vEMNCGKlr1BwDxljXlXRz5X_sDS2DVZSIGLxfj3ylnsDD5aV6LnoF6iVHwx0LN-D_mUjHZz52VGV88rf7jESCrC0SOg4iw-MWK4Y60KmNRoKW344VZBvwk9PsUY2BpjU0m8IhX02WKfOqdpbCUgX-0tg6rGSH73Cu1Q333LDVYt8XiIaIjZZGC1Tq_Fo1j13sCJdHARzKosbaHRfRPUbhhxURTWX8kRtoia-JHRgW5HIJyNXxW23l455QJolzksUFXvig__xByX7v-dMgwIX8Bhzx0nd3oiFWhsNTPriQ_DRH_ga6UuBvpao_G2rJXseMZY2eXNV-HH5Y2rP_Q1Lpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=vEMNCGKlr1BwDxljXlXRz5X_sDS2DVZSIGLxfj3ylnsDD5aV6LnoF6iVHwx0LN-D_mUjHZz52VGV88rf7jESCrC0SOg4iw-MWK4Y60KmNRoKW344VZBvwk9PsUY2BpjU0m8IhX02WKfOqdpbCUgX-0tg6rGSH73Cu1Q333LDVYt8XiIaIjZZGC1Tq_Fo1j13sCJdHARzKosbaHRfRPUbhhxURTWX8kRtoia-JHRgW5HIJyNXxW23l455QJolzksUFXvig__xByX7v-dMgwIX8Bhzx0nd3oiFWhsNTPriQ_DRH_ga6UuBvpao_G2rJXseMZY2eXNV-HH5Y2rP_Q1Lpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.
خلاصه‌ی توییت این دوستمون:
- یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه.
- هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده.
- اما Jev اصلاً متن تولید نمی‌کنه.
- Jev به‌جای تولید توکن، مستقیماً از ورودی به یه ساختار یا خروجی مشخص می‌رسه.
- به‌همین دلیل، سرعت Jev فقط به این دلیل نیست که «سریع‌تر متن تولید می‌کنه»؛ بلکه اساساً فرایند تولید ترتیبی متن رو حذف می‌کنه.
- نتیجه می‌تونه پاسخ‌دهی سریع‌تر و مناسب‌تر برای کارهایی مثل خروجی JSON، ابزارها، ایجنت‌ها و پردازش‌های ساختاریافته باشه.
به‌عبارت ساده:
LLM مثل نویسنده‌ایه که جواب رو حرف‌به‌حرف می‌نویسه؛ Jev بیشتر شبیه سیستمیه که مستقیماً ساختار نهایی جواب رو می‌سازه.
البته این به‌معنی بهتر بودن Jev برای همه‌چیز نیست. LLMهای معمولی برای مکالمه، توضیح‌دادن و تولید متن آزاد انعطاف‌پذیرترن؛ اما Jev برای خروجی‌های مشخص و قابل‌ساختار، می‌تونه سریع‌تر و کارآمدتر باشه.
✍️
ترجمه و خلاصه از
akshay_pachaar</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5280" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q-_ZNv0Z5CUWR8mX5Nlq5aSVrNvHZChOMG0qWmjtU-7AkE6t-Nir3lrMXpTEZweJehHZTdLJbrQNjIfqvp_aKPrpD9FBO25XbQ4ww1D8nfRjKOdVIbXpFn7ZUmASglc8nJkQ7DCkbWzbSa77wKNKHL_97eVTq09ZAO4LQtYbQkElYdKgwV7mzrmf_Nz7nkSwiFzFak_Y9jF7P-plLDH0QUEs6GPOpaz6NPbCj1h-oxL-nCPiDbnfBjDjsDS7MahNjZs2mv_3qfKJ_ddBXpCQodQQi8d5B6I8vCuYgW8nglRJtsCfCAUY0MsN7CKlsvschSvHJ6r1Ki7_FddxEyi7pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم توضیح تخصصی تر: https://www.youtube.com/watch?v=vj7hysh0mOI</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5279" target="_blank">📅 10:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/axVwZXGt6loBJxaVTwthRdAxTqrv2CeSEj6uVU5tYxUxQxgvFbjW5ydQNGxgCWFZ5l1BOmqy1mUH8Q9ruvifN0AMM32K1CFQSlHsGxomH44-X5zhTvo_A5g00_UaWethENC1msedXe3AShSkbIanAUssMFqvKTPWr8mV9xQLr78r8Q2hzbS98ZUv3fLqgTcUUmVmfd-EW1W1Re6fZwhOvF_YGZ1D42ktJa_TsyIm0gcAI1urVqfuBhBNre4Ese_dfZhDhC97-JP4QZSe-25iHdPbk69_m0pmgFxSWuu4H6knLh8TGAy4aGeDeTfJ-YdmJkthHhfzP7iCCf8_zgmMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیلی که توییتر رو دوست دارم:
(اون روبیک Graph خیلی خفنه فردا می‌ذارم فیلمشو)</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5278" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">به زودی برای پروژه‌های اوپن سورسم هم آپدیت میدم بچه‌ها
هم Aether gui هم اسکنر</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5277" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کسایی که ری‌اکشن
😁
می‌زنن آخر این ویدئو مسج رو دیدن
😂</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5276" target="_blank">📅 20:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=E4Agc6gp7sNV-V4paYbFjZKetfOrZeJaeUmLlkhOPtg8Fo6Cs_KbSUHfv5msJxf9LufQTGuM-PCHRMqthIVacebb8eqp4Cv_63iZM_lRI4TuPgQ3Wl0-_zqC9fxnv7R8GsTCl3dcRs4zQnvM8cI6fXcknvsthvSjC-5-hoMrwuQ2bXYqROvh36HbZrt11oXwW5nWLZyFX4aNvUtO8MpzNMgvgD-qR258HTBreNqzwl6-9liECWXnE0EKI23gF15JrH_sGHeUh3AQX51YEDQkhUsdy-K-hPxUTxlSAkW_u3C0s_ogVoap0oq0mhleuNGvB6nAwl3snyDRlqG8oNDU7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=E4Agc6gp7sNV-V4paYbFjZKetfOrZeJaeUmLlkhOPtg8Fo6Cs_KbSUHfv5msJxf9LufQTGuM-PCHRMqthIVacebb8eqp4Cv_63iZM_lRI4TuPgQ3Wl0-_zqC9fxnv7R8GsTCl3dcRs4zQnvM8cI6fXcknvsthvSjC-5-hoMrwuQ2bXYqROvh36HbZrt11oXwW5nWLZyFX4aNvUtO8MpzNMgvgD-qR258HTBreNqzwl6-9liECWXnE0EKI23gF15JrH_sGHeUh3AQX51YEDQkhUsdy-K-hPxUTxlSAkW_u3C0s_ogVoap0oq0mhleuNGvB6nAwl3snyDRlqG8oNDU7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5275" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">از اینجا می‌تونید به عنوان میهمان وارد شید: https://live3.eseminar.tv/ch/wb182512</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5274" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5273" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=FFkgXGljIevuinZOXItZGOr84lmNuxIvAaKYtNe-nxTsqpxTMRKGjKNIEq30lTN04ElfVgPgab9hpM-JWtHAeM2eoVrSU7j7BdmGEQbewZZbrxBQEnCWUPOtAMoTiEe9v8CHwQUmYDjOyY6ic-O4iNjOTqEXGE6bGcTBVZFT8WHptYuk7blCJ0nX94p8VFZMWIRx19dNWRg1vt-W_NA_FqnTD8l9BMOCFvV2kcRKwRXM805Lwa1keDj2Idke7uNScxT3lXPz3sRrX05OWRix8QvgV1A5zLoxrIm8bHg_QOkdTgjr9sXCSbv0t6zya4lrXCpAmubDZbmeymE1NApW14EoAoLfhZeRIVlAPpksY5rCZ2hwKEKGHZxotPSx1BXtiISGOl0dkt8WmI0X07fSyVBNsdBmZt99oyMvV3vIsxOR1AYiRrBer712N9OuXUlcmqqb4dG3YvkMdvOtm4dO6qzIvDSIhHHstR7PylDNIhi8pXriKnWwW71QBzcfFY0GSgSGXC4zjgGHjXb86LiiaInUhrEZY8NaZ9UkACqvmZCo6TsJdEYEB7k8iA4q8bfKJNNFVa4_pkKZdXeti1NkH1TB2CHw5Zkan32pII1-8ntEVY_YenptFYY-Eb0K-ufqe6eAfO7ADmWdEKpln2_adYyIFyNMxUgE3Jc5Iyp6SVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=FFkgXGljIevuinZOXItZGOr84lmNuxIvAaKYtNe-nxTsqpxTMRKGjKNIEq30lTN04ElfVgPgab9hpM-JWtHAeM2eoVrSU7j7BdmGEQbewZZbrxBQEnCWUPOtAMoTiEe9v8CHwQUmYDjOyY6ic-O4iNjOTqEXGE6bGcTBVZFT8WHptYuk7blCJ0nX94p8VFZMWIRx19dNWRg1vt-W_NA_FqnTD8l9BMOCFvV2kcRKwRXM805Lwa1keDj2Idke7uNScxT3lXPz3sRrX05OWRix8QvgV1A5zLoxrIm8bHg_QOkdTgjr9sXCSbv0t6zya4lrXCpAmubDZbmeymE1NApW14EoAoLfhZeRIVlAPpksY5rCZ2hwKEKGHZxotPSx1BXtiISGOl0dkt8WmI0X07fSyVBNsdBmZt99oyMvV3vIsxOR1AYiRrBer712N9OuXUlcmqqb4dG3YvkMdvOtm4dO6qzIvDSIhHHstR7PylDNIhi8pXriKnWwW71QBzcfFY0GSgSGXC4zjgGHjXb86LiiaInUhrEZY8NaZ9UkACqvmZCo6TsJdEYEB7k8iA4q8bfKJNNFVa4_pkKZdXeti1NkH1TB2CHw5Zkan32pII1-8ntEVY_YenptFYY-Eb0K-ufqe6eAfO7ADmWdEKpln2_adYyIFyNMxUgE3Jc5Iyp6SVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه! به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید: https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5272" target="_blank">📅 17:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه!
به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید:
https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5271" target="_blank">📅 17:57 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
