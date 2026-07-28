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
<img src="https://cdn4.telesco.pe/file/li5gdq7LJk4jqDFPBT3Xwog_LsHcchQDUGaupdzRu8keTQpOiNn6bKqeQmU7T6VdJ65Eb5_0Lal_ui3bvOEl49Si1Z0uZF4zb83bp97uanxfdi0y3LEqtny7Fztkqhag17BXBjaPjYlMT7iw6h9i2bufAqo3YQQAx2MqimkbCYrFPDlTjIxh-X_vBmi8pSScrC9iGVCcgSg1EB2D5d7CCdeSTcgRZWoFoTjzSbLMC3pLhqCiFYLhJY-2TgWg-ZsAVhXiz1Wgf0zk-nENA4AXuR_ZbBI-iDAn7vy8uKyzMil9ccufvRCL727NkR28u8DdGHovNLQh0usWDyeP5Vtapg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.22M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 03:26:08</div>
<hr>

<div class="tg-post" id="msg-675933">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
بزرگ‌ترین تأسیسات پالایشی عربستان از کار افتاد
🔹
شرکت آرامکوی عربستان پس از حملات پهپادی یمن، فعالیت بزرگ‌ترین مجتمع فرآوری نفت خود در بقیق را متوقف کرد.
🔹
ساعاتی پیش یمن اعلام کرد که با پهپاد خط لولۀ انتقال نفت از شرق عربستان یعنی همان خط لو‌له‌ای نفت را بدون تنگۀ هرمز به بندر ینبع در دریای سرخ می‌رساند، هدف قرار داده است.
🔹
حالا شرکت آرامکوی تمامی فعالیت خود در این تاسیسات را متوقف و در چندین سایت تولید نفت، عملیات مشعل‌سوزی اضطراری را آغاز کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/akhbarefori/675933" target="_blank">📅 02:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675932">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7j7Gj3ZO124eubdh0utRnBAUKL1mf6vB3-oUM1BClUYI7tnKip1YR7OYa43T_EyBIOrG8LLVvNEVtPIAtrGJjO67B3UJznvpcdQ-WSVeow9hxeTh39pkz4ftuF0S-VVnlin0sIclFgCMMdNAVD3MNPJHQD5O9raxwnKjnIBLc4GVeFWqHPILxKN_j25j7lp8UtAgJfddUwlrKYIhLQof6hhpJfgCVrZBoc5Ah85rd--GJMB69fmcMIOQ21WaY65LUiUlWjC7mlIr7KjlpePS13SL3y20u4-xOGiE1KPdLapavwa24BOG9_Hjy3cBQba6tg5l4_1eITIwb_HFWN7HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز حساس واشنگتن؛ از موجودی موشک‌های آمریکا چقدر باقی مانده است؟
🔹
وال‌استریت ژورنال در گزارشی به بررسی وضعیت حساس موجودی موشک‌های آمریکا پس از حدود پنج ماه درگیری در جنگ با ایران پرداخته است. این گزارش که روز گذشته منتشر شده، بر نگرانی‌های داخلی دولت آمریکا در مورد کاهش شدید ذخایر مهمات دقیق، به‌ویژه موشک‌های تهاجمی و پدافندی تمرکز دارد.
🔹
طبق تحلیل‌های مرکز مطالعات استراتژیک و بین‌المللی (CSIS)، ذخایر برخی از این موشک‌ها به شدت کاهش یافته: مثلاً حدود ۳۰٪ تاماهاوک‌ها، نزدیک به نیمی از Patriot و THAAD، و بخش قابل توجهی از JASSM کاهش یافته است. بازسازی کامل این ذخایر ممکن است ۳ تا ۶ سال طول بکشد، حتی با افزایش تولید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/akhbarefori/675932" target="_blank">📅 02:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ابراز بی‌اطلاعی گروسی از زمان بازگشت بازرسان به ایران
🔹
مدیرکل آژانس اتمی در مصاحبه با شبکه «بی‌بی‌سی» با بیان اینکه ایران هنوز عضو معاهده «ان‌پی‌تی» است، گفت که تهران باید اجازه ورود بازرسان را بدهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/akhbarefori/675931" target="_blank">📅 02:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675930">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
نتانیاهو نخست وزیر رژيم صهیونیستی وارد واشنگتن شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/675930" target="_blank">📅 01:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675929">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شنیده شدن صدای آژير خطر در کنسولگری آمریکا در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/675929" target="_blank">📅 01:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675925">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05b88909c6.mp4?token=p3BWW9Dov5L33xEIrPgj-lJtqpiakpLlKhIchFzxj7Mt6-qC5vIyuaS9oN_ciMPV3v25qi4YUI3UbPOB-uQWYjraaIO5Mt-0GsFkwJXnvsUWA7ytzDmeFzN67hEWHrKX2tItM2GXgHHSxVg9V3l9M2Sdr30j6CEKE4Ke2nHqokkOl3isc8uSfLdKi8CWF-sCyhRmASDqIH7niZ3FmXPBtAh4WSN9ovi0AUDHI-_Ruzl60oz0y9xfkzu-CJ3MFppZsk_l-d9D84DgdyF6caMllEzc_0aM1GZMSDLpgff6fCyc9qBBIYTamnPkYUGfleRVDIEmacecoPZ4aT24H8a2_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05b88909c6.mp4?token=p3BWW9Dov5L33xEIrPgj-lJtqpiakpLlKhIchFzxj7Mt6-qC5vIyuaS9oN_ciMPV3v25qi4YUI3UbPOB-uQWYjraaIO5Mt-0GsFkwJXnvsUWA7ytzDmeFzN67hEWHrKX2tItM2GXgHHSxVg9V3l9M2Sdr30j6CEKE4Ke2nHqokkOl3isc8uSfLdKi8CWF-sCyhRmASDqIH7niZ3FmXPBtAh4WSN9ovi0AUDHI-_Ruzl60oz0y9xfkzu-CJ3MFppZsk_l-d9D84DgdyF6caMllEzc_0aM1GZMSDLpgff6fCyc9qBBIYTamnPkYUGfleRVDIEmacecoPZ4aT24H8a2_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از انفجار و آتش‌سوزی در مخفیگاه‌های جدایی‌طلبان تروریست ضدایرانی در أربیل عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/675925" target="_blank">📅 01:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675924">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
گزارش‌ها حاکی از آن است که کنسولگری آمریکا در أربیل
هدف قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/675924" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675923">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
منابع عراقی: بیش از ۷ انفجار در حومۀ اربیل، مقر احزاب خرابکار و تروریستی را لرزاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/675923" target="_blank">📅 00:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675921">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a40bf5ed3.mp4?token=mU3CPxXyx93B2Vgu0AXkdCtgR1eUY7n8f0jqSOPGg3wOMDW6ALyr1dhAm1RhgWOef2YmXlS7CKVdHBYQ5H3b65Ub0n0PqpGyLM0NwuEeYy32hXMAuIjXTTTJmbbVK6vSVslszj_jFEUQcQNxyUF1-7--b1WOaPrFdoxKSa_d_BVKqVIHubRCOvzWGjtn0eWU5H9m-uHlOvul0Cl0hndfmLJTiwSXhxmtK1_UH4kYvyEs6ZGnJ2AixGSgbYCreGw5X2HWFoUOXyABT3ZhFa-svPevHFJYHRlL8ygCi_ZcgJCgdbAlUgSGA_BCJckB8_kfPUNlyyPd49i7pLiVZGfAbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a40bf5ed3.mp4?token=mU3CPxXyx93B2Vgu0AXkdCtgR1eUY7n8f0jqSOPGg3wOMDW6ALyr1dhAm1RhgWOef2YmXlS7CKVdHBYQ5H3b65Ub0n0PqpGyLM0NwuEeYy32hXMAuIjXTTTJmbbVK6vSVslszj_jFEUQcQNxyUF1-7--b1WOaPrFdoxKSa_d_BVKqVIHubRCOvzWGjtn0eWU5H9m-uHlOvul0Cl0hndfmLJTiwSXhxmtK1_UH4kYvyEs6ZGnJ2AixGSgbYCreGw5X2HWFoUOXyABT3ZhFa-svPevHFJYHRlL8ygCi_ZcgJCgdbAlUgSGA_BCJckB8_kfPUNlyyPd49i7pLiVZGfAbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات به تجزیه‌طلب‌های ضدایرانی در أربیل
رسانه عراقی:
🔹
تاسیسات راداری و مقرهای تروریستی در مناطق خلیفان و سوران در استان اربیل هدف قرار گرفتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/675921" target="_blank">📅 00:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675920">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اربیل در شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/675920" target="_blank">📅 00:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675919">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اربیل در شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/675919" target="_blank">📅 00:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675918">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
گزارش‌هایی از حمله به یک میدان گازی در شمال عراق
🔹
منابع محلی بامداد سه‌شنبه از حمله به میدان گازی «خورمور» در استان سلیمانیه واقع در منطقه کردستان عراق خبر دادند.
🔹
همزمان پهپادهای تهاجمی خارجی نیز در آسمان «اربیل»، مرکز منطقه کردستان عراق، به سمت اهداف خود پرواز می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/675918" target="_blank">📅 00:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675917">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e4fd2715.mp4?token=gYW0WXLXVZ5A8buYUtn-kFvQP_peULaQT5f-NadHXUezLqnDEZzH6ITmzDkBwjudzFPpbNb23j-IPHXWHosVejqnRM6jKDDesiY6ybRNJtlVd3F2bSPdWgaOrS3SR0VCBXoi6lANNt3E8a20W9NV4j9RA4ht4TwOAOI03qxBlncVmic0SLwTEmGhlkjZSy9hFmnywKINOW-TA2wJ4qlBa2vsc3ATJaFuxWpuSbdGABiBFPnPZBgICXtRTt8PifNKcMAfocwAtBjx0tv9U9GMUTrNwpIS6ALsztq3Uxr6Xo2xFDK9AwehT25u5vGmLUo-MXBVL5L6dGOfoCnh07iRrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e4fd2715.mp4?token=gYW0WXLXVZ5A8buYUtn-kFvQP_peULaQT5f-NadHXUezLqnDEZzH6ITmzDkBwjudzFPpbNb23j-IPHXWHosVejqnRM6jKDDesiY6ybRNJtlVd3F2bSPdWgaOrS3SR0VCBXoi6lANNt3E8a20W9NV4j9RA4ht4TwOAOI03qxBlncVmic0SLwTEmGhlkjZSy9hFmnywKINOW-TA2wJ4qlBa2vsc3ATJaFuxWpuSbdGABiBFPnPZBgICXtRTt8PifNKcMAfocwAtBjx0tv9U9GMUTrNwpIS6ALsztq3Uxr6Xo2xFDK9AwehT25u5vGmLUo-MXBVL5L6dGOfoCnh07iRrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاجی بابایی: نباید در مورد NPT کاری کنیم که بهانه دست دنیا بدهیم
🔹
اگر حفظ نظام جمهوری اسلامی نیازمند حرکت جدیدی باشد مطمئن باشید مجوزش را خواهیم داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/675917" target="_blank">📅 00:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675916">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/587a803682.mp4?token=ipLE_i9SpGjzlX9pQ_IMJVoGTnfQu2y2XkxfuZSQSku0RhYnbBfyRvfcpbJq2DKMYPnjFa8QGGg13jzT1tYa5mnzXNdvlYtzcqIFF00brjTuK3tgPBkimJQolzEc0vPN9q0Jn63qx9FRcu59mtx3gG3GawbvKrEJMKdCBYg9jYGCEd17ma3YlOH4L9sxJRskdO8NzpL3pe5Ct78IOq8PpXeqnSohdzTiiecMIaP-O576L1Kjgqi4oT7HtDllHgiyI2ZduyGhu2os1JMgCJtTiOrL0QX7TnQEUwcsb-v-h07TZgCOl5g8Lk3Z3KIGPl0RSs40OBH0scS5Mmz-T_1ZTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/587a803682.mp4?token=ipLE_i9SpGjzlX9pQ_IMJVoGTnfQu2y2XkxfuZSQSku0RhYnbBfyRvfcpbJq2DKMYPnjFa8QGGg13jzT1tYa5mnzXNdvlYtzcqIFF00brjTuK3tgPBkimJQolzEc0vPN9q0Jn63qx9FRcu59mtx3gG3GawbvKrEJMKdCBYg9jYGCEd17ma3YlOH4L9sxJRskdO8NzpL3pe5Ct78IOq8PpXeqnSohdzTiiecMIaP-O576L1Kjgqi4oT7HtDllHgiyI2ZduyGhu2os1JMgCJtTiOrL0QX7TnQEUwcsb-v-h07TZgCOl5g8Lk3Z3KIGPl0RSs40OBH0scS5Mmz-T_1ZTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیباترین گل جام‌جهانی به انتخاب فیفا
🔹
گل سیدنی لوپز کابرال، بازیکن کیپ‌ورد به آرژانتین در مرحله ۱/۱۶ نهایی، عنوان زیباترین گل جام جهانی ۲۰۲۶ را به خودش اختصاص داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/675916" target="_blank">📅 00:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675915">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4dR7K84yk4kezEYOuIMtrXK-bdlKPf3jJy1rJbnXh6TbNAmeHvI_Cv53pNVuzdagoKB2f3s1ixdrkMsYk4-QF46h5Trk2FFQjyH-NXglyMTOraFZi6wMfNceiFecaGcS-IRrqgynPatRxuhzyR8bcQjR-Azmers6chLqt1dEJm2GRuy5UGZ_E8c6rBepCZ5zFVtqfBrmPgl2PGAIyvehw-XDlKJLSA801ZKJzmnGrZi1JqohCw5_nz0zRMq52qTgNK9pmzjBBaGyEN3UIL5yrwu5svIAVkdBafsZFgPxY_EWlxgqYLti69phSS72f157iCX9OV-Ur5gcSX244kSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/675915" target="_blank">📅 00:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675914">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0144687c28.mp4?token=ZTzRMsmrSV5kvME-Od5_vnmy0F86P6cbYIybm4dxV7e6OXJ7WETyFC0iPZ0k9s8Mfbp3SV6deP7gpB-djGYDQ4oY-hTXnOhAeYp_cOuh70oTvFnCU_SG9a-IH4mLTP8YR7w4AqJAz_k1j7tTD2IjHzS-MsgQVFiy-XaS9KbUHDT117DR8CQkijCsODRNJ6m0LH7umqacTGwbvaYWGndc4L_3AXf42KhMfNztQKcgitU3QctDOoKNZ-1DhG-JyHqoeiVLlslvoo_3_0-sFrtc2F4WVtO8WesVIzcS2IMq36bPfFx975B0mEkie_fFMiqau3g5Th0tx32lzjlWhp_ICA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0144687c28.mp4?token=ZTzRMsmrSV5kvME-Od5_vnmy0F86P6cbYIybm4dxV7e6OXJ7WETyFC0iPZ0k9s8Mfbp3SV6deP7gpB-djGYDQ4oY-hTXnOhAeYp_cOuh70oTvFnCU_SG9a-IH4mLTP8YR7w4AqJAz_k1j7tTD2IjHzS-MsgQVFiy-XaS9KbUHDT117DR8CQkijCsODRNJ6m0LH7umqacTGwbvaYWGndc4L_3AXf42KhMfNztQKcgitU3QctDOoKNZ-1DhG-JyHqoeiVLlslvoo_3_0-sFrtc2F4WVtO8WesVIzcS2IMq36bPfFx975B0mEkie_fFMiqau3g5Th0tx32lzjlWhp_ICA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عراقی تصاویری از سقوط پهپاد آمریکایی در نزدیکی سد حدیثه در استان الانبار منتشر کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/675914" target="_blank">📅 23:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675913">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مقاومت عراق، اتهام عربستان مبنی بر نقش داشتن عراق در حمله به تأسیسات نفتی این کشور را رد کرد
🔹
ترامپ سه‌شنبه میزبان زلنسکی و نتانیاهو در کاخ سفید؛ ایران و اوکراین محور گفت‌وگوها
🔹
مقاومت عراق: هرگونه اقدام «احمقانه» از سوی عربستان با پاسخی سخت روبه‌رو خواهد شد
🔹
واشنگتن پست: طرح آمریکا در حمله به قایق‌های مظنون به حمل موادمخدر شکست خورده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/675913" target="_blank">📅 23:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675911">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c19b8a98.mp4?token=H_wXjxao2VnGO9u9jGWsR_Z1qF49wNtGjcJvNXeHg9Q8GHkKCZvBBK_HiOCUF6pN6zCo84qhgMZHrg4AwPePw48m3iKROSxmCtA13q0QM2-C1v6laJDWMkh54elxfUKEgHkWw2nJSjiyZySafMFgy1j02ggykmyhAfY25DZMKWYLTZprRsHeVczGkkrvgKxa-SJ1qNY42uEJhHiOULSp2X5mXcvh7dTXsKSKvOpWqOL9ayDP4RK8rxB4cEEiW9iYFG7Ox7ehdA3buG7g3ueQdl6WwdoFDVeQe2zDBnODF1B10q53DYNymWwYwzgGst785s3NVFl262ZEczjyCRGO7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c19b8a98.mp4?token=H_wXjxao2VnGO9u9jGWsR_Z1qF49wNtGjcJvNXeHg9Q8GHkKCZvBBK_HiOCUF6pN6zCo84qhgMZHrg4AwPePw48m3iKROSxmCtA13q0QM2-C1v6laJDWMkh54elxfUKEgHkWw2nJSjiyZySafMFgy1j02ggykmyhAfY25DZMKWYLTZprRsHeVczGkkrvgKxa-SJ1qNY42uEJhHiOULSp2X5mXcvh7dTXsKSKvOpWqOL9ayDP4RK8rxB4cEEiW9iYFG7Ox7ehdA3buG7g3ueQdl6WwdoFDVeQe2zDBnODF1B10q53DYNymWwYwzgGst785s3NVFl262ZEczjyCRGO7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپادهای پلیس چینی «کلاه ایمنی» را زیر نظر می‌گیرند؛ تخلف کنی، هم هشدار می‌گیری هم امتیاز منفی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/675911" target="_blank">📅 23:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675910">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQsPF2bN2ogJtjMGYbqCvtwiUsZpzuxpJQoWGmYCBdfLORsWitfGbsNNUnhgHkqXmcCGPxWkJxn3WZGB0HmXbAMG1QdxhV_TCJHKOJC46zni_xEaBMdnJYc69AJ_1-RhcUFs6mGwbOaA_RiVxrlTfWjbxDy9XRsZoDLnweqGoaAoYZk7lxpsn4VREwd4W8N7G6nj5mSFafst4C2h4QyNNSNWH3meEZ5hbeQuU-J35a9sWR-kkaFk45KIlbW_OJIll_fkrITK0Qy7B6KjpbiBc7LvXf5C4CMzfusALOMMCyESBUgP2kS4gROz_59QfL9vN3HXcIWyEZKOQf_TTq7z5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقاله ظریف در الجزیره: پنج دهه استراتژی پنهان اسرائیل برای سوق دادن آمریکا و ایران به سمت رویارویی دولت‌های متوالی اسرائیل تلاش‌های دیپلماتیک را تضعیف کرده و تنش‌ها بین واشنگتن و تهران را تشدید کرده‌اند
🔹
در حالی که بنیامین نتانیاهو، نخست وزیر اسرائیل، برای دیدار با دونالد ترامپ، رئیس جمهور آمریکا آماده می‌شود، دلیل خوبی وجود دارد که انتظار داشته باشیم او از این دیدار برای منصرف کردن هر اقدامی در جهت پایان دادن به خصومت‌ها در خلیج فارس استفاده کند. این انتظار ریشه در یک سابقه تاریخی دارد که بیش از پنج دهه را در بر می‌گیرد.
🔹
اطلاعات از طبقه‌بندی خارج شده، خاطرات مقامات ارشد آمریکایی، گزارش‌های تحقیقاتی و تحقیقات دانشگاهی، این ارزیابی را بیشتر تقویت می‌کنند. در مجموع، این منابع به یک الگوی تکرارشونده اشاره می‌کنند: دولت‌های متوالی اسرائیل، اغلب با حمایت عناصری در درون تشکیلات امنیتی این کشور، بارها تلاش کرده‌اند تا مانع تلاش‌ها برای پایان دادن به درگیری‌های منطقه‌ای یا تلاش‌ها برای مدیریت تنش بین ایالات متحده و ایران شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/675910" target="_blank">📅 23:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675909">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
ترامپ: در حال انجام مذاکرات عمیق با ایران هستیم
👇
khabarfoori.com/fa/tiny/news-3233599
🔹
۴ سناریو پیش روی جنگ ریاض و صنعا/ مهم ترین سلاح های یمن در جنگ با عربستان
👇
khabarfoori.com/fa/tiny/news-3233622
🔹
دوئل‌های توییتری قالیباف و ترامپ و الگوی جدید گفتمان دیپلماتیک - نظامی ایران
👇
khabarfoori.com/fa/tiny/news-3233428
🔹
نیما تکیدو؛ ستاره‌ای که رسانه‌های رسمی نمی‌شناسند اما میلیون‌ها دنبال‌کننده دارند
👇
khabarfoori.com/fa/tiny/news-3233431
🔹
پایان ۵۰ سال فرار؛ قاتل خواننده انقلابی به دام افتاد
👇
khabarfoori.com/fa/tiny/news-3233468
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/675909" target="_blank">📅 23:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675908">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d817e971db.mp4?token=rdLIFUFYTLushI6SWQ9JXHEzWcADYrKydTSMC8uDqZaPMB7YUnROiFeT83I7yiVoO3U7krLF4O7265WIjG9J12W2jSaRG1HbWyDnxNXMjSAc_Wf0ZvHfmar7sCtFnjwZJ6F7wHKoqRfFrXL3INYON5cSGJeEGTsRUsJGd2LuA9UpPN8t8oq7tCyl81E-J_6ZlVQCmk8zA5KK4_KXeVqnwaKgal5anmcd3IQj4VUCmyKq0quGHKU_zhKKSotEEjfaYd0yfhGR7qtuBro19sfcMvvI7Jy9y5S8fNwYCL_yieSi0raDk6w-sOr4h-piNROK8VfqfS4rY_DpJUkd9ByEjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d817e971db.mp4?token=rdLIFUFYTLushI6SWQ9JXHEzWcADYrKydTSMC8uDqZaPMB7YUnROiFeT83I7yiVoO3U7krLF4O7265WIjG9J12W2jSaRG1HbWyDnxNXMjSAc_Wf0ZvHfmar7sCtFnjwZJ6F7wHKoqRfFrXL3INYON5cSGJeEGTsRUsJGd2LuA9UpPN8t8oq7tCyl81E-J_6ZlVQCmk8zA5KK4_KXeVqnwaKgal5anmcd3IQj4VUCmyKq0quGHKU_zhKKSotEEjfaYd0yfhGR7qtuBro19sfcMvvI7Jy9y5S8fNwYCL_yieSi0raDk6w-sOr4h-piNROK8VfqfS4rY_DpJUkd9ByEjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی‌های سگ زرد درباره ایران: در حال حاضر، مذاکرات سازنده‌ای در جریان است. ایران می‌گوید: "لطفاً، لطفاً، هیچگونه محاصره‌ای اعمال نکنید."
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/675908" target="_blank">📅 23:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675900">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwxJYvu-p2G5C8w0Oc4ZD_OUsgPKkYdiJK-bHXWKwzU1HOKu2h8MFxZY7YllCzaYldvHjLweQH6ZO32VfWnKoL9uoGB7Og5_pGc9CHYk76vomOI50vLt37zNFqW31WdV7eYFMtoG6nwHOaD17haLx0uPflDxuTO5qAWLY86Zxynl4Y6sT0x4KvjIEhzddjyliZTA1BI4t8-11rxyWjon9XjnLZyN6gSESjhhpi9yXoeKwZGjXHDkgF1tNWa7rE8UkJDHD5G_jjORbFstz0UIQOPFOkXJTTNoQeCIxMbpu-o3ycYNNbjaX1CNR3MLvA2HPAuCBSHZwd4yaLneo0Z8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XrJn_3ExNKnYwnLbiKU5F3for4upt1sNb3G_HWUmnz7l0PjNDQeQVP1qAr2tRPAjB9FH18aIMJ_cUTNTmaV36hwqZv8zu91MgPtRSWGvWKrSO2xo5CHN1v6Uw8KL1nuZsV6HwJ_u3pfz7yyg3svH7nzBHr1C1-9YuGrq-VeB-uZa4rtvSCtTfjAFNF617cuYjuPTMG8X2pHV94Q5RKAnN7IKqOz7Wno53rCgsByM_sptCi78k4Lwt23bQ4euncQEN_DXiCNwjAbIcvD0FZToFtQibbKh9PXo-b7pAssqarfnKBv1d-O4XDMXm-tLBxYNRNLm_vRj46w92h4tku66ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-4sYnb9mvT5Fcs8nJX9_1-aPtquVOM-AMuOzXdPYk7geJnlD_lNKXwjLCygbaIKjzuJtBet3KXS92rTQOHLz2EN11R9_Gp-n-vlbiGbz7HEcwPkbTRv9y_2odi0g0Sh9s7mcuVHgc1z6myF1-TFCS3fv_ZWk67jmfxLCI61oGIxgcz_fAm3aI-ObXhEE5tswYv1cwbyf7tmh-dD8v1G-gCY9aGpMVxS5Uh5IfjFxBuBp9DMYDSNQQtfd79KrIFXFabRBfI7eLK9x2jv1uK7RTF5-tbxcS7WHKiPJ1Tth_I8xvGp4d3GsuN2xrc62vUMsCxuX5n3Fg_d4sdNhPStIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SKecR7AtOcy32c9-VhPdbMBaCrj5gT65yakjXLFdbof8_7-knvSUvvISfphfMNmo3PEBypCJzTGPQRrqygG9CLuzySXu3gxE9d5sYYHybdPACq1_Q0EXvUSr6R8ta6r5W7QE4_gO77g9uk7oSlkaJ6wOvFL7YkTkscA9OKW4ek9FgF0w-WavyuhxhD7pGO6qqiBdzXokTJhmwFTFjda1kSpywX95V9ik3I07-qE1z9i8GBSl0IZ861S3BnEpnus-gBbgcBMIalA5A5SejkMPLLXA2c1z6beRQZoVMsMVCS9g98mR2B7fOfpBs6Sk4cI-N944sguJjsYSEETJ7cu3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujv_ZrxAU9d-yS-TIMqRw-faGaQaHIFdtQerQNkXGrLBS_jg1h0AuNyoYxLKGVPhbGt80J9Tu-wTvcnA_mqpJ-0k1G42TMYqx_ikeCPqeGt67pUr37-tbiPwf9GW4yVJ9UUr0ybYSYjQux_cddqi6UlMSlIbIazUQv9s4YX2M2GOs3Ilv_cUG9P1-IUARMrl6QBhw05ggGD5qNHZQTFa1v8XLDs7r9p8VmjIJJIvSekGOXxfkpkwGNvPdCDgh_aBj-G3d5LdE-ycd_zcjXetn5zFvG202a2IDZXGCYIeCZtv6kKh93AfBDrMUASdrV1yXTCkvPkOAYDOqJfeRzZCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fs_bjuNLz2oGfgi7uMrJk2dY6Y9DyTLtVi1BTQMDD1u3Bk9ZSBz8wLZybMP6Hdq-SPKURgARLZ19Q4Yf-55EKUlTOHpfwESD98dMDMWMPMFEZBFLg5RSDo-rcpjNbhG0E9guI4yoAYedud2e285tqaMy64-p65wTkc5mtW-jFmSYGKWV5KVYFNDAeuVyfT4qqb4gjl4rTULp26MJKPtbX8iTZofFSwk1dnWqdkwob5hMXTg3krb-BeSWAM-cTutpTN9tkHk0usZr9dCGqPVYm4tlPV92HasJyMAbB8s278B-IIk7bdSwUhFlbmyxVcYdHe611XTACOA_Hk1yYnXETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TvnUlNzabJd3jK7CQ4_facXdnf7zZIAN0NqLP9o3GNuwKI7I-z3zx8bmfyT_Nk1ICPizgNxICsRKCQL1YcxngXIUkqBhqIAbpT_FOSqGmzxoxw6uV6iBLPJDgVrFk3up6qTgXRMYb4wpmH_1oPbA26dkyuWWmG87H4itmNVQywc3DXxHCBLHKRjKa9b_sv7kcMM8fu0zgpYzYZIY8CtbFIfvpg_kVHk717nwwV4FSC0XWgDA-z6uWkJkQzyvhCD7Dun2atyZqyZglahcZ2RwHI7pgm83eQ8t-Iyy6aC904eue-eja7aIZtyn_z3S2OPjOgY_42HMeL_igrANSP3Gtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vRkRYovyK3PSC6dRq9P68SHlggLsECK0W1L5SosMoviKG5WjQQzpH2qavx1Lj_-Ip_QiuGJRlgl-GJ7jWqnfVk_MGF_eAuAyq8YfAE3d8iF6Emwd9Ubu2FKtAZsg3wGvN9HBj95bVWyAcrJhu7b3AabKfTVAnNOT1-wa7kdWFjtwN1db8wGl0PgI4bWhJ4IVOwOlEEmIPrcDosGuivgDJP2z5qUsAzfsjkeh_XywDu4K2SgP7wOWjMv5-dISNhHDYPZvd-h3Z3mCz2JlFxE-iO3FEj6-aUbnBSQ001xzlGh-QYjGUwLWz7_mFn0Xq8zJBtRbNvBXV3gy9vw9l5LgNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۸
عادت طلایی برای بالا بردن انرژی و تبدیل شدن به بهترین نسخه خودت
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/675900" target="_blank">📅 23:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675899">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ساقط شدن پهپاد آمریکایی در الانبار عراق
🔹
منابع عراقی از ساقط شدن یک پهپاد وابسته به آمریکا در استان الانبار عراق خبر دادند؛ پهپادی که گفته می‌شود پس از هدف قرار گرفتن با آتش مستقیم در منطقه «الفیافی» سقوط کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/675899" target="_blank">📅 23:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675898">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
حاجی بابایی، نائب رئیس مجلس: ما هیچگاه با آمریکا به تفاهم نمی‌رسیم
🔹
ما نباید هیچگاه با آمریکا در آتش‌بس باشیم، اصلا آتش‌بس با آمریکا معنا ندارد و این به معنای آن نیست که مذاکره نکنیم، و نباید دوگانه جنگ و آتش‌بس را بپذیریم.
🔹
نباید اجازه دهیم آمریکا هرموقع…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/675898" target="_blank">📅 23:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675897">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5c64910dd.mp4?token=Krw8_6346LvPHayxKRXpS0trLoE9zss_sNWuqZ4K33xu5Rv9N_jOM0I1t-p5g6BCrFVmgZlshX92i_ooUjmuJ4jccaeH4Q90saTmKC2wwWHoB1xZLGmiEK5jpjn1vM3ZPrxMcQIWGbL0kxvwiOT3Lgw6Lnu4q01REIGoIhGW-WozUHWGxMPdfdw6O-2oZ8ao2749uDe9U90muUBBGhstHXsavp_33HAnNmksQPiwE92RZn4Ib7O4VTs26hnR6qWaJEwusFD8UnQVGM3YxVMcXkMvzLPVAOVKMO_jmYF5-QEwuGeMwT4HuaOxJehpWK9p91G7R6QiAR3wuGp7waWsPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5c64910dd.mp4?token=Krw8_6346LvPHayxKRXpS0trLoE9zss_sNWuqZ4K33xu5Rv9N_jOM0I1t-p5g6BCrFVmgZlshX92i_ooUjmuJ4jccaeH4Q90saTmKC2wwWHoB1xZLGmiEK5jpjn1vM3ZPrxMcQIWGbL0kxvwiOT3Lgw6Lnu4q01REIGoIhGW-WozUHWGxMPdfdw6O-2oZ8ao2749uDe9U90muUBBGhstHXsavp_33HAnNmksQPiwE92RZn4Ib7O4VTs26hnR6qWaJEwusFD8UnQVGM3YxVMcXkMvzLPVAOVKMO_jmYF5-QEwuGeMwT4HuaOxJehpWK9p91G7R6QiAR3wuGp7waWsPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سگ زرد: نمی‌شود ایرانی‌ها را خرید باید شکستشان داد
ترامپ:
🔹
نمی‌شود آن‌ها را با رشوه خرید. باید آن‌ها را شکست داد و ما داریم حسابی آن‌ها را شکست می‌دهیم. خواهیم دید که نتیجه چه خواهد شد
🔹
همان اتفاقی که در ونزوئلا افتاد، در ایران هم دارد رخ می‌دهد فقط مردم متوجّهش نمی‌شوند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/675897" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675896">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZnEchUP1VwfLHlRgMiBXma-6C7Vu9QKv_wDJk4aTv3tQLhB3Ntz5y-2HxMP6mSodQ5Mbhb2S2II6Y8CY2P4iyvEntBArEg1zBacaWC9o48gB53NS_fgtY6jdE7NyDcXw_Iq5OQrxSZpETfaGv3l4b8N6-YU82NVNN2fs9Jz-_vIvejF2vum1v_0uQ36IuWOF7gvLNhoAj_iqf3wUU1rkDmT1zmdJrjRN-URMVbo4ezo2l4s3xqkGRXIPnKhl6SLaaMIGHUlpv-GKuUryhbGlofR1mmd2R3aLv9AcdQfOuuxOEQvfXFNOYkxBV7SxkZiW2ZDtsdhhY5Oei3vXzz8NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دینار تو بازار کمه؟
🤯
هرجایی دینار نباشه، توی دینارز هست!
خرید راحت و بی‌دردسر دینار از دینارز برای سفر اربعین.
🏴
@dinarz_app
🔹
نرخ و ثبت سفارش:
https://dinrz.ir/9v6
🔹
تلفن پشتیبانی
۰۲۱۲۸۴۲۸۴۱۲
🔹
پشتیبانی در بله
@dinarz_support</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/675896" target="_blank">📅 23:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675895">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای خوک نجس دربارهٔ ایران: مذاکرات دوستانه‌ای در جریان است
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/675895" target="_blank">📅 23:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675894">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66ac763ce4.mp4?token=Bgyn60I5_ug5F9BBP46HC5pggGkR2uwBS6IwUQUK5bcxr4kgXEWFVCWqLcqGSBqcZwVj4snSdkOquBLHsMvU2C5L5IjZyF67bP1M8VP0-sY-zfxPOspVApigjCBGqJSTzQOX-nmzvJaL0ppgoUjuXYJbxoU5_LLBGApX7il6nsVfuZC50HvYio6rlnYQKRLKxb9zbzjinU3tpiEHgwps9wTFBamjMNd3Y1_A70kMcTD_U7ZPhz8py6sfdomZk7AiVLByTpzlfJ8JwTBHoiUxOFsW6rxgEOtD7FILQWmIyNzSL2Cp2SMIyc3L1eAxoO5EHRNwyQNZuAMDgNZLRlKvmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66ac763ce4.mp4?token=Bgyn60I5_ug5F9BBP46HC5pggGkR2uwBS6IwUQUK5bcxr4kgXEWFVCWqLcqGSBqcZwVj4snSdkOquBLHsMvU2C5L5IjZyF67bP1M8VP0-sY-zfxPOspVApigjCBGqJSTzQOX-nmzvJaL0ppgoUjuXYJbxoU5_LLBGApX7il6nsVfuZC50HvYio6rlnYQKRLKxb9zbzjinU3tpiEHgwps9wTFBamjMNd3Y1_A70kMcTD_U7ZPhz8py6sfdomZk7AiVLByTpzlfJ8JwTBHoiUxOFsW6rxgEOtD7FILQWmIyNzSL2Cp2SMIyc3L1eAxoO5EHRNwyQNZuAMDgNZLRlKvmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنرانی سگ زرد با شعارهای تند معترضان علیه او مختل شد
🔹
معترضان او را با عبارت «حامی آزارگران کودکان(پدوفیل‌ها)» خطاب کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/675894" target="_blank">📅 23:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675893">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
حاجی بابایی: تنگه هرمز؛ نمود اقتدار ایران در برابر آمریکای مستاصل  نایب رئیس مجلس:
🔹
این آبراهه به بازدارنده‌ای قدرتمند تبدیل شده؛ هر کشور تحریم‌کننده، با واکنش قاطع ایران مواجه می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/675893" target="_blank">📅 23:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675892">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7Zqz2flf1VLx9VTkWmDa1Q_2QsiKFhwhn1ShqGyGq7synaaCA_tlaVjWtDFOgcrr5bz04xIAcUEG7RFDZY4z5nsOYrhBppjmV8oOlRG6-AvotNFeYceh04xS-nJdvQCwJ6xRIprHyjlnksql4b-08wofyOLsJ9oqqVQGLzd8mXcyH5wI5EdXoj3XejHDFbezQ-w7fFsUkx5nRYo9KW3CIvhCDH2VkP3JkkiUuIUy-BnZGpYa72eOrxIK-2iGvZix9APtZyH0fFiV81rh4v9DQHtQ7BSvRWSswDirbfyGf6J6DFHanmLGvukqYjclTJLjr3ZSMPgq5BhggvzudIc6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ سناریو پیش روی جنگ ریاض و صنعا/ مهم ترین سلاح های یمن در جنگ با عربستان را بشناسید
🔹
یک سناریو در رابطه با جنگ عربستان و یمن، از سرگیری جنگ زمینی است. دو احتمال در این رابطه وجود دارد. یا عربستان مانند جنگ قبلی مستقیم وارد جنگ زمینی با یمن می شود و یا شروع به تحریک شورشی های داخل یمن کرده و آنها را به سمت جنگ با صنعا سوق می دهد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3233622</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/675892" target="_blank">📅 23:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675891">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/684fac0bac.mp4?token=bY9ibzux0bj-TwCWrTtW8tPUoWCbASuXidwEwr3TvybWuZ4_Fqr5ApvAVlf0MI9MXDprdCRPtEYNy7oGFkom43b9--CStYjBDdKU0li435eqBWnylSMxPRz7sB7qtErZaFTpGquBznpbJFeCVEV1i43LA0nqrTwLt29HS90o437OP0hr16nxvHZzlFRKWzBq_nfDaEb7Q9dbFi2CR_GD_BRX0Qk5LQdY3-3xXnuhm308nxKausEyxZBZf4puyfsFTx_EVKvk6hKr7hfRWzCMIlnNIIvwSdG6sXSt5mdSxyQNG7r-8kX93xKgF_EDuhOs0bSCYukN0PqZbDeMmOPuWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/684fac0bac.mp4?token=bY9ibzux0bj-TwCWrTtW8tPUoWCbASuXidwEwr3TvybWuZ4_Fqr5ApvAVlf0MI9MXDprdCRPtEYNy7oGFkom43b9--CStYjBDdKU0li435eqBWnylSMxPRz7sB7qtErZaFTpGquBznpbJFeCVEV1i43LA0nqrTwLt29HS90o437OP0hr16nxvHZzlFRKWzBq_nfDaEb7Q9dbFi2CR_GD_BRX0Qk5LQdY3-3xXnuhm308nxKausEyxZBZf4puyfsFTx_EVKvk6hKr7hfRWzCMIlnNIIvwSdG6sXSt5mdSxyQNG7r-8kX93xKgF_EDuhOs0bSCYukN0PqZbDeMmOPuWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاجی بابایی: تنگه هرمز؛ نمود اقتدار ایران در برابر آمریکای مستاصل
نایب رئیس مجلس:
🔹
این آبراهه به بازدارنده‌ای قدرتمند تبدیل شده؛ هر کشور تحریم‌کننده، با واکنش قاطع ایران مواجه می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/675891" target="_blank">📅 23:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675890">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ef574baa.mp4?token=o0I4hCpDASgdMvcotmR9cQ5sar4L__hQTBix1Adwvi4KA8djE5D1VzGa5KljuN6P1WWh5YWuvAhUG9WA_EK6a71skuDW5239CUUis-lZ8vl8P-5X0goioEl8qbvz9k-jk7LDXE4oJAgoMk5EXXYCwsuGPt2Tk-nxUC9lNbQJkEQwsOdu_SXK-OBIf7PgP1X6MWurdBLAzJ_-SqMj99GA4pdhZw7x_NdYsQJ2lQS_eVcHOnvuWxT5K9CHXhRQLwBeiAGcDm4GS59UmphS5fBdlZjBPfOsJD4E4z9Kyz8fhVDelIy_Ez5DwT_mDqqzQbPj6_DwMOrSqjJWgMbFS4popQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ef574baa.mp4?token=o0I4hCpDASgdMvcotmR9cQ5sar4L__hQTBix1Adwvi4KA8djE5D1VzGa5KljuN6P1WWh5YWuvAhUG9WA_EK6a71skuDW5239CUUis-lZ8vl8P-5X0goioEl8qbvz9k-jk7LDXE4oJAgoMk5EXXYCwsuGPt2Tk-nxUC9lNbQJkEQwsOdu_SXK-OBIf7PgP1X6MWurdBLAzJ_-SqMj99GA4pdhZw7x_NdYsQJ2lQS_eVcHOnvuWxT5K9CHXhRQLwBeiAGcDm4GS59UmphS5fBdlZjBPfOsJD4E4z9Kyz8fhVDelIy_Ez5DwT_mDqqzQbPj6_DwMOrSqjJWgMbFS4popQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک هار: از پدر و مادرتان بهتر هستم
خوک هار:
🔹
من بیشتر از پدر و مادرتان برای شما کار کرده‌ام، قبول؟ قصد ندارم از پدر و مادرتان انتقاد کنم، اما من نسبت به شما از آن‌ها بهتر بوده‌ام.
🔹
کمی ناراحتم زیرا ممکن است در دو سال و نیم آینده، رئیس‌جمهور متفاوتی داشته باشید؛ شاید
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/675890" target="_blank">📅 23:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675889">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرزند ارشد شهید سیدحسن نصرالله: شهادت امام خامنه‌ای مردم کشورهای عربی را بیدار کرد
🔹
ساعت کاری ادارات کردستان روز سه‌شنبه از ۷ تا ۱۱ تعیین شد
🔹
وزیر بهداشت: در تجاوز اخیر آمریکا ۶۰ نفر از هموطنان شهید شدند
🔹
یمن: پهپادهای ما با موفقیت به اهداف خود در عربستان اصابت کردند
🔹
وزیر علوم: آموزش در کشور هنوز مهارتی نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/675889" target="_blank">📅 22:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675888">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67b6a03b0.mp4?token=eh0_0gBELJgCE9kc5K36zOO6Bm4dKiV8RoJIkoVvnW50uYpHZoQeyIFkHyDdPqzOHrlD5-whiJhXUAVUkt1ZQ4wzjttnX6C3xOfFmevf0dvD6Zxzyd92ocMZE5jSJz9TfBftAYJXP3avWhLAeOhvZukja0wiSVaULg2dyZS6kxU3slaCF4K4XEmz_aR-qMK4QcdcAAoRwuJ7UgwBqxHXiWYWzOZek8MrhZcIF_598Jb16IOFAuSGt6r9HNxIM6dezAqxa59VFQg-RBQGkrrzDv44lT01b9_JHZN7rxPDBUD29MBcSyvg75HY3-ptOKu0vU57M0InSSH6jFdi1yG9OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67b6a03b0.mp4?token=eh0_0gBELJgCE9kc5K36zOO6Bm4dKiV8RoJIkoVvnW50uYpHZoQeyIFkHyDdPqzOHrlD5-whiJhXUAVUkt1ZQ4wzjttnX6C3xOfFmevf0dvD6Zxzyd92ocMZE5jSJz9TfBftAYJXP3avWhLAeOhvZukja0wiSVaULg2dyZS6kxU3slaCF4K4XEmz_aR-qMK4QcdcAAoRwuJ7UgwBqxHXiWYWzOZek8MrhZcIF_598Jb16IOFAuSGt6r9HNxIM6dezAqxa59VFQg-RBQGkrrzDv44lT01b9_JHZN7rxPDBUD29MBcSyvg75HY3-ptOKu0vU57M0InSSH6jFdi1yG9OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک نجس: ممکن است بقیهٔ دنیا مرا دوست نداشته باشند، اما مهم نیست
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/675888" target="_blank">📅 22:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675887">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0841c94803.mp4?token=uL3tX_SVb_G4wha5bn3O7Y-k-7JE3zJKfCqXhgjXtA5zeLJ6rYtzbH3AyAcVpV30qP5DsZpzi6gm1iFYkkEwc3_5kW3JVT9QTS2GjnWmV55HxX7SuREM16tmKaluj3SvroIEowzbl6HSKcUXD5F-X0DV-zvPo-FJOTeoWORP_3ro7aaO3rG3GBZ2H4hJDxLNv94UXo_-2nkK2JRfMCHqYqdaU8kaVmHgb9I8FcAk91gqPJUc-z8E6b3K4n8H531bEY2Vviv6ETHrULJ3kwF1xiE0oPsXX2Kz-CpDjH2XoE9RTHGb3MBgg1CTKUBUo9lvXG32npxcZ4LoLQFaCGYW0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0841c94803.mp4?token=uL3tX_SVb_G4wha5bn3O7Y-k-7JE3zJKfCqXhgjXtA5zeLJ6rYtzbH3AyAcVpV30qP5DsZpzi6gm1iFYkkEwc3_5kW3JVT9QTS2GjnWmV55HxX7SuREM16tmKaluj3SvroIEowzbl6HSKcUXD5F-X0DV-zvPo-FJOTeoWORP_3ro7aaO3rG3GBZ2H4hJDxLNv94UXo_-2nkK2JRfMCHqYqdaU8kaVmHgb9I8FcAk91gqPJUc-z8E6b3K4n8H531bEY2Vviv6ETHrULJ3kwF1xiE0oPsXX2Kz-CpDjH2XoE9RTHGb3MBgg1CTKUBUo9lvXG32npxcZ4LoLQFaCGYW0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوشیدنی آلبالوییِ خنک؛ طعم ناب تابستون در یک لیوان
🍒
😍
مواد لازم:
🔹
۷۰۰ گرم آلبالو
🔹
۲ لیتر آب داغ
🔹
نصف فنجان شکر دانه‌ریز
🔹
۲ برش لیموترش
🔹
کمی کمتر از نصف آب لیموترش
🔹
۴ عدد میخک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/675887" target="_blank">📅 22:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675886">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95b575b358.mp4?token=YmCPE5hzTZPoPD01btVAbcIiI5tfMec2b3itOSBAX9w3mnLPkHNvw79cxZ2OuV_EvGl6S7Ez9V2t_pgIeVbcIwoNIQvDbu_hT7T37o-x4NbixF3niqfsapRBOhNSUhHl-rgCgpGAGlMaQYdvEt4Vp75gvBbAqKi4hYBHrQTLUfchqeKY9z2ouiCWEclmM6tbxm34gJb_IbyDlFDDgDevjItLlN6XFVP0dyZozVyrs0q96Uj_Y9JCAr6dtGkvy2Mhz_nWZDXENUM4Me7R_xj0gLfp5O25xRdGoniUZb_ZEV_c7tPAafwLMsznjbpMnFOKj8tpzDFhxPDPnQRTBUznNorc-yXBq1Jb7tzx6FjrhsE4SEinwqXfJStvGRjTkRceeqeXND28BpEryGux2_y4x3_W1owob3sTVIhicRPuC0TRw2T6L3l7ShAdCPVHKl_eM1W5WvAlZzXMJ5fHa_DR2asp6CxRmwnTay0cevbZPlcinMp8gDRgmFvPL5xHSfTQUK4f_UEdRj5T1iifhmXdFtBRrDksVlgurcU-wwma4kuq17Y2ejNH9OkWyCzjzDzUplI6LSSwMi9hS7sfeGz2nx0LBfpKnIn8fEYemG-ONTh-KxXEG-IVuMeiDsd6yOMJVm-eTO7Xkm4nMIGYxogaMkpjK1apSPaBCT100x25Tqc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95b575b358.mp4?token=YmCPE5hzTZPoPD01btVAbcIiI5tfMec2b3itOSBAX9w3mnLPkHNvw79cxZ2OuV_EvGl6S7Ez9V2t_pgIeVbcIwoNIQvDbu_hT7T37o-x4NbixF3niqfsapRBOhNSUhHl-rgCgpGAGlMaQYdvEt4Vp75gvBbAqKi4hYBHrQTLUfchqeKY9z2ouiCWEclmM6tbxm34gJb_IbyDlFDDgDevjItLlN6XFVP0dyZozVyrs0q96Uj_Y9JCAr6dtGkvy2Mhz_nWZDXENUM4Me7R_xj0gLfp5O25xRdGoniUZb_ZEV_c7tPAafwLMsznjbpMnFOKj8tpzDFhxPDPnQRTBUznNorc-yXBq1Jb7tzx6FjrhsE4SEinwqXfJStvGRjTkRceeqeXND28BpEryGux2_y4x3_W1owob3sTVIhicRPuC0TRw2T6L3l7ShAdCPVHKl_eM1W5WvAlZzXMJ5fHa_DR2asp6CxRmwnTay0cevbZPlcinMp8gDRgmFvPL5xHSfTQUK4f_UEdRj5T1iifhmXdFtBRrDksVlgurcU-wwma4kuq17Y2ejNH9OkWyCzjzDzUplI6LSSwMi9hS7sfeGz2nx0LBfpKnIn8fEYemG-ONTh-KxXEG-IVuMeiDsd6yOMJVm-eTO7Xkm4nMIGYxogaMkpjK1apSPaBCT100x25Tqc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک نجس: از پوتین می‌پرسم آیا ماهواره‌های روسیه به ایران کمک می‌کنند
؟
🔹
ترامپ، دوشنبه ۲۷ ژوئیه در پاسخ به سوال خبرنگاران درباره ادعای کمک روسیه به ایران، گفت که شخصاً این موضوع را با پوتین، مطرح خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/675886" target="_blank">📅 22:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675885">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b898eeb1cf.mp4?token=ME_G3IfYA7wa6W4qtrXW4RVdGS3_TSvj9_UIhLApGbIvOJskvc70pj6Y74uKMl8eCD2i9x3ShVudNjjDxlS9IBnppKwDEq7Hy4U6yvmXWWFf9qYFeXgoCGZgtlmOzA4hg51DTSAQEQ7J1k6tEvaMCyorX_bDO2UKU22eCDg7LSv_jDvnSKMhmH2GrNJ_dwW-q0Ps-7BSrp4fwWcWxzecVnE5vCmO0xxZRzNa1nRqmfEigbXI_Gjw78og-UzrCIi-hkpL32lpZN2X3HwVuetF9FvDM7eHRygkwdN-627-kFEKrxcmeTBltxKjvd0qkkiax13yWTE1E2meKIEgj_RFmQ_wf8bM6wKJf2-TrmgSkvmoCy0evFBwZr0nzCm1x3-yGjbv4kbf8wmzRJoHjVL9zb2kMt72XdsiA5491NEMSSJY0Ws2BlUtCn6SG5PVJP2n-HG_JFpws4yZP3ZSVpq53XckfiUoHrE4AVAX5E_c_-T-hz1uLWuqeJn8a3q72prZM78pJPc7EEUVeGc9eX_rKiw9jEXPJfzSWusb94vUyRaFQdUpD4-64sWhJQXo1mnhy_3pjNNyub7L1UPwVqjNVwhICDoPQpDqy-4TCqH7VhHDpcy98YdXG4uNeX1mWLqSzuzcotF2-hYNkuWwyleBY-wvv3dPUTXCQnm9d4ms5AE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b898eeb1cf.mp4?token=ME_G3IfYA7wa6W4qtrXW4RVdGS3_TSvj9_UIhLApGbIvOJskvc70pj6Y74uKMl8eCD2i9x3ShVudNjjDxlS9IBnppKwDEq7Hy4U6yvmXWWFf9qYFeXgoCGZgtlmOzA4hg51DTSAQEQ7J1k6tEvaMCyorX_bDO2UKU22eCDg7LSv_jDvnSKMhmH2GrNJ_dwW-q0Ps-7BSrp4fwWcWxzecVnE5vCmO0xxZRzNa1nRqmfEigbXI_Gjw78og-UzrCIi-hkpL32lpZN2X3HwVuetF9FvDM7eHRygkwdN-627-kFEKrxcmeTBltxKjvd0qkkiax13yWTE1E2meKIEgj_RFmQ_wf8bM6wKJf2-TrmgSkvmoCy0evFBwZr0nzCm1x3-yGjbv4kbf8wmzRJoHjVL9zb2kMt72XdsiA5491NEMSSJY0Ws2BlUtCn6SG5PVJP2n-HG_JFpws4yZP3ZSVpq53XckfiUoHrE4AVAX5E_c_-T-hz1uLWuqeJn8a3q72prZM78pJPc7EEUVeGc9eX_rKiw9jEXPJfzSWusb94vUyRaFQdUpD4-64sWhJQXo1mnhy_3pjNNyub7L1UPwVqjNVwhICDoPQpDqy-4TCqH7VhHDpcy98YdXG4uNeX1mWLqSzuzcotF2-hYNkuWwyleBY-wvv3dPUTXCQnm9d4ms5AE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنجره متفاوتی به حضور رهبر شهید ایران در چادر عشایر اردبیل؛ مردادماه سال ۱۳۷۹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/675885" target="_blank">📅 22:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675884">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
اقدام به محاصره به منزله توسعه جنگ است
هشدار قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی‌های تجاری و نفتکش ایران در آب‌های ساحلی و سرزمینی کشور ما نموده است.
🔹
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می‌گردد و همان‌طور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی‌گذارند و با آن برخورد خواهند نمود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/675884" target="_blank">📅 22:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675883">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10282ab1b3.mp4?token=aVLanIHBDUSNCsG7vzwoxyzdmQUWGvlKnC3QorXpg5MiaNzRYyMY4fK2F9u_5zV9kwqWiM3hQoElK2h_vQ-G7dUigLJhO64kaHgyxKPrqbuaiEHiBcBFuDPBePmqLnnTox7yzpLqikxgeJhes7Tqsvz2iMK0Dx3kWChrGKWNo9uvb09u9iRcCl_g620sRraqIQuBH7VpG2fx40L8fPcT85MDh7wg33Q6MyjwTuSzi3ZQORF_4XdTjBfeNCdjJd1-WNQJ9AksrFqGQxgkTtzPOqZXmBmtTAngWo4SQPQuTG9yY7T2og88gtUzldtMGwvjZXdTuvcVE54ezBk-ZHjzMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10282ab1b3.mp4?token=aVLanIHBDUSNCsG7vzwoxyzdmQUWGvlKnC3QorXpg5MiaNzRYyMY4fK2F9u_5zV9kwqWiM3hQoElK2h_vQ-G7dUigLJhO64kaHgyxKPrqbuaiEHiBcBFuDPBePmqLnnTox7yzpLqikxgeJhes7Tqsvz2iMK0Dx3kWChrGKWNo9uvb09u9iRcCl_g620sRraqIQuBH7VpG2fx40L8fPcT85MDh7wg33Q6MyjwTuSzi3ZQORF_4XdTjBfeNCdjJd1-WNQJ9AksrFqGQxgkTtzPOqZXmBmtTAngWo4SQPQuTG9yY7T2og88gtUzldtMGwvjZXdTuvcVE54ezBk-ZHjzMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: نتانیاهو با فروش F-35 به ترکیه مخالف است
🔹
خوک هار: «هیچ‌کس به من نمی‌گوید چه چیزی باید بفروشیم یا نه.»
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/675883" target="_blank">📅 22:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675882">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c645f1ae8b.mp4?token=mhAL7BHbxWEeHTLVTQRiTiYLWommJrqXO8ojD4Zaxoso8xgJmvso1dM6M0TLWZ9LFWzg8srF4-6qPpwmhDPSXbtF6-_zosSKIirRGoq67e998C5PoabREgrr5c4SzXtPPVpRCkPS0msJ9elAxDL0UgwNZ-VyGCyedt1J_ZUtgOEIc88GJD_BN1-sZWz05rrZjdJj1L81NwLjkevHVcO4PHkLzpakhp24gw2zVbW8J4O15JYEPO-mY70HY5NHVNx3qx07WprHkYN9no8zKX4r7IR1MuhIv8_RS31aBgshgFBelFxmIIRQjoBbdhnMJs-a11EaZ1Febve6EiBfVja1YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c645f1ae8b.mp4?token=mhAL7BHbxWEeHTLVTQRiTiYLWommJrqXO8ojD4Zaxoso8xgJmvso1dM6M0TLWZ9LFWzg8srF4-6qPpwmhDPSXbtF6-_zosSKIirRGoq67e998C5PoabREgrr5c4SzXtPPVpRCkPS0msJ9elAxDL0UgwNZ-VyGCyedt1J_ZUtgOEIc88GJD_BN1-sZWz05rrZjdJj1L81NwLjkevHVcO4PHkLzpakhp24gw2zVbW8J4O15JYEPO-mY70HY5NHVNx3qx07WprHkYN9no8zKX4r7IR1MuhIv8_RS31aBgshgFBelFxmIIRQjoBbdhnMJs-a11EaZ1Febve6EiBfVja1YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عادات اشتباه رانندگی بیش از قطعات بی‌کیفیت، عامل کاهش عمر موتور و خرابی‌های سنگین خودرو هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/675882" target="_blank">📅 22:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675881">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آتش‌سوزی در کلانتری ورامین تکذیب شد.
🔹
نخست‌وزیر عراق: اجازه حمله از عراق به کشورهای همسایه را نمی‌دهیم.
🔹
رهبر اپوزیسیون رژیم صهیونیست: عربستان با اسرائیل سازش هم بکند، نباید هسته‌ای شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/675881" target="_blank">📅 22:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675880">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1365c9a34.mp4?token=iOUoYNIR4RwO7FeSD8_K7Zf2lfpLLTPlVAI4dEwn0mii0Tpp1ULJ-817laYesLo-LAXpLOMdVFdDJfxZOV6DKngxe6hmia0pOJVBZZfiqbs9e7wGX9GHLHjzYumRTwyXHZr4Ebn9KVRrs3Qm9Kkcrnh8fuG3gkPQnX1wbGTtAYmQk9OUuJBRNaQMDYWZEhuJaLeWeqN-v0zZGlbOLYqOtMEDuKsrt8yPB1Ko1dULmncRxH93DH9s2_a4xoJiSfXv1GKvka6DMPYpes-Mn5z-_34FPPjGd3N7nsZc0xu8eidUDQWf4tAp-ZT7TbwRJhTNdsseh1j1s9rjfvyqKRzsG4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1365c9a34.mp4?token=iOUoYNIR4RwO7FeSD8_K7Zf2lfpLLTPlVAI4dEwn0mii0Tpp1ULJ-817laYesLo-LAXpLOMdVFdDJfxZOV6DKngxe6hmia0pOJVBZZfiqbs9e7wGX9GHLHjzYumRTwyXHZr4Ebn9KVRrs3Qm9Kkcrnh8fuG3gkPQnX1wbGTtAYmQk9OUuJBRNaQMDYWZEhuJaLeWeqN-v0zZGlbOLYqOtMEDuKsrt8yPB1Ko1dULmncRxH93DH9s2_a4xoJiSfXv1GKvka6DMPYpes-Mn5z-_34FPPjGd3N7nsZc0xu8eidUDQWf4tAp-ZT7TbwRJhTNdsseh1j1s9rjfvyqKRzsG4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت‌الله جوادی آملی: رفاقت ۷۰ ساله را از دست داده‌ام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/675880" target="_blank">📅 22:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675879">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
هشدار هوانوردی آمریکا در منطقه بحرین
🔹
اداره هوانوردی آمریکا (FAA) به دلیل افزایش تنش‌های نظامی، به خلبانان هشدار داد هنگام پرواز در حریم هوایی بحرین و آب‌های بین‌المللی تا ۲۷ اکتبر با احتیاط کامل عمل کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/675879" target="_blank">📅 22:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675878">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nvns6WiPZf5RONSYbxdo3l_ecFA31z-W5LTV1O7UKP0tDk-neoefNcAjwr14J0fG2hySW242ExU5_g-oi4o3iTD1vxUrqeVtKfdGxHfY_0Ufdn4Dq-pAOfjeY_ryFiJ72BTzA92pxZhposyWcOjVSuOH6BCnX6avB1F_zwbSghyspXyy74BhlayqrkHOBNdX870Gv2WvOIiVRzXeDopJvZxat8XiXSqxry2XpK9966rPPRJq-i_D3YgjcsqiT3xmVlxSqa2CIe_jFmGkm-rmJVJrFGZEJQjA_lMgUe0wJE9Ci7yUjvlXvFCMV3xdJxhNkh1bMGsyPHQmEI4tPr-R1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر کمتر دیده شده از رهبر معظم انقلاب اسلامی آیت‌الله سیدمجتبی خامنه‌ای در نماز جمعه نصر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/675878" target="_blank">📅 22:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675877">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c4ea3de2.mp4?token=QtMrvaDauECrzwlGrfnNpg0hnnkd0xm2F3o3HedJHCAgC10kf4LZMThzqQ_pIPQHBUwvnweZxq4qIfbIEKqvUm-qrHENGgsfprsfwCJ-XB-rAwZUV1K5dP763-v3dP7q5C35UyFAi-BCAQnWLStpWTnQGUdjd2YZ42hZ7NfIaJcdzQ3V03vxVr8iQM5hwjjfMPZsg-AbCera_Xd91abL8nQbsAdeu7tKrmPBi4swNmeNp15517SvkbUdo_Vwo8MkhgBmwsfZmboDfV0kqbEzzgFvVGX5bRYRnYBduXJRhCxxezWXczfXEsUFzlbPrfl1HLM6TzdSdzD2ujwPe2Bm6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c4ea3de2.mp4?token=QtMrvaDauECrzwlGrfnNpg0hnnkd0xm2F3o3HedJHCAgC10kf4LZMThzqQ_pIPQHBUwvnweZxq4qIfbIEKqvUm-qrHENGgsfprsfwCJ-XB-rAwZUV1K5dP763-v3dP7q5C35UyFAi-BCAQnWLStpWTnQGUdjd2YZ42hZ7NfIaJcdzQ3V03vxVr8iQM5hwjjfMPZsg-AbCera_Xd91abL8nQbsAdeu7tKrmPBi4swNmeNp15517SvkbUdo_Vwo8MkhgBmwsfZmboDfV0kqbEzzgFvVGX5bRYRnYBduXJRhCxxezWXczfXEsUFzlbPrfl1HLM6TzdSdzD2ujwPe2Bm6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گلچینی از هوشمندانه‌ترین ضربات ایستگاهی دنیای فوتبال
⚽️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/675877" target="_blank">📅 22:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675876">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک پنجم مصرف روزانه سوخت کشور قاچاق می‌شود/ عضو کمیسیون انرژی: روزانه ۲۰ میلیون لیتر سوخت از کشور قاچاق می‌شود
غلامرضا دهقان ناصرآبادی، عضو کمیسیون انرژی مجلس در
#گفتگو
با خبرفوری:
🔹
روزانه ۲۰ میلیون لیتر سوخت از کشور قاچاق می‌شود که معادل یک پنجم مصرف روزانه سوخت کشور است و بخش عمده این قاچاق مربوط به بنزین می‌باشد.
🔹
اگر قرار باشد سوخت به‌ صورت دو یا سه نرخی عرضه شود، دولت باید زیرساخت انتقال سهمیه سوخت به کارت بانکی افراد را فراهم کند.
🔹
در غیر این صورت دولت باید سوخت را با قیمت فوب خلیج‌فارس در اختیار مصرف‌کنندگان قرار دهد تا از قاچاق گسترده سوخت جلوگیری شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/675876" target="_blank">📅 21:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675875">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cr9NKv8DgUtZggHVoLTTmfTc65uZ-he34-JtjdemBrMn--EI-re5OulwXwrQISj0qKJ6m2umRunLawRWkhgWdO9yb_jQ7Tx1SNzDPK_ou7jvN5pm1sc9WTIwBfqxYfDvW6sJlb0D8yaj1K75CJ4PadEOesL2zwhCB36oHWqWRc36GNBAFM3SHFT9-jiveSq_rAZXOIh-hefE9eMb81Ev5fu7IpyGuT6P4sKTSw6GS9e3GcrZwfAqai1FTXB-bFQMlLWuQ2lEBjhi4ZnOW5kjQ5zEsEwvASh6qaFK9u3dZNtS1nk5qHgHKgnH1AYjy8IER0tzopIAlHsUhm_fURb5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت پس اخبار منتشر شده درباره مذاکرات مجددا کاهش یافت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/675875" target="_blank">📅 21:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675874">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
آشفتگی در آسمان اروپا
🔹
نقص فنی گسترده در سازمان مدیریت ترافیک هوایی اروپا (Eurocontrol) موجب تأخیرهای طولانی‌مدت و به‌هم‌ریختگی پروازها در سراسر حریم هوایی اروپا شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/675874" target="_blank">📅 21:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675873">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ddc468dc0.mp4?token=SB7kc_A7ulChzvqINa194SPizY0ywUoDW8St2gHt61XjMYSqfH6Zyub5Uxf7LRAELhM5AnfhlDUNVM6xNHnDc6y1vXX1vy4xNbgZNNiKaVwqPb_gcvrwIdY65H-b1pPipxZA3GAnW-ebpa4YR91_94WXhvcjHe2l3E5VuxDHt5KW7qHnPJDekPtFBvSsz3YeKq6O7q2JX5D9pqerXGfLdQM2DqlKf7YE9X9MmSTndfa5vQijKIHUV-mCJRbuwZs9Zt92m7lQ4Qal8n0TdjaOsZb3zyF3AqMwP_Tf0chNZWEUa2rjUE0OGUB-uXCTCvuPxCW_IYgtCxfAMrQWxlusX4nDUI-L5UGiIIqJaeSQNbU7Tqw5mnO_8kja3xCPV1k-_sEC9MDNpEZgygkVgRaYKrl72hN68Vl168tE9w69Cyp-hxh5FJEqLMgqoSsGxpvugwbMg3zMW7KqMv48hfSDyTJuzhXcmZPRct4Jhv-K1aEcaqGTa5sktZehEnpMClCDJh8210RbjdZm-p1RkrMe1qBjetj8q0jGLyJ_0RuSOLih4IV5fw3jZnXkgXIS6C_rY4X5_80zvlTgHZiF51jUxE-ml6OpxYiuoPXQsr_eKXWTAWUiTFL5l-Z7GyGt5CqlWiz4cRDjDVRc88YVaWmmXhrwc6rO-Yccr6dTvpQ0aZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ddc468dc0.mp4?token=SB7kc_A7ulChzvqINa194SPizY0ywUoDW8St2gHt61XjMYSqfH6Zyub5Uxf7LRAELhM5AnfhlDUNVM6xNHnDc6y1vXX1vy4xNbgZNNiKaVwqPb_gcvrwIdY65H-b1pPipxZA3GAnW-ebpa4YR91_94WXhvcjHe2l3E5VuxDHt5KW7qHnPJDekPtFBvSsz3YeKq6O7q2JX5D9pqerXGfLdQM2DqlKf7YE9X9MmSTndfa5vQijKIHUV-mCJRbuwZs9Zt92m7lQ4Qal8n0TdjaOsZb3zyF3AqMwP_Tf0chNZWEUa2rjUE0OGUB-uXCTCvuPxCW_IYgtCxfAMrQWxlusX4nDUI-L5UGiIIqJaeSQNbU7Tqw5mnO_8kja3xCPV1k-_sEC9MDNpEZgygkVgRaYKrl72hN68Vl168tE9w69Cyp-hxh5FJEqLMgqoSsGxpvugwbMg3zMW7KqMv48hfSDyTJuzhXcmZPRct4Jhv-K1aEcaqGTa5sktZehEnpMClCDJh8210RbjdZm-p1RkrMe1qBjetj8q0jGLyJ_0RuSOLih4IV5fw3jZnXkgXIS6C_rY4X5_80zvlTgHZiF51jUxE-ml6OpxYiuoPXQsr_eKXWTAWUiTFL5l-Z7GyGt5CqlWiz4cRDjDVRc88YVaWmmXhrwc6rO-Yccr6dTvpQ0aZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه جنگی یمن فیلمی مرتبط با پهپاد مسلح «بیرقدار آکنجی» ترکیه‌ای متعلق به عربستان و لحظه انهدام آن را منتشر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/675873" target="_blank">📅 21:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675872">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عراقچی: سکوت و بی‌تفاوتی جهانی، جنایت را به الگویی برای تکرار تبدیل می‌کند.
🔹
یمن: اقتصاد عربستان به دلیل تجاوزگری‌ها دچار فرسایش شده است.
🔹
مسکو: اقدامات تروریستی کی‌یف ابعاد بین‌المللی گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/675872" target="_blank">📅 21:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675870">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S924HKW5lhBIlHuaBtjnPx49YAoK0HcmBpnOlZh4xk08TUXOcVQq3YYHkdkN1CkRp9O9iIaPUDLpCgOShjmIacaWjCnFl_AwCHlvmzGSEwDWFL7IQ_Q15KA0DX12-lQ7WdzfvsokL1nnSOxW0Mze5P863siCLR8CNxXYRJb1wzvoCaW8ucyREC-RAzf2uCEUcEkE6dybc3JxPYaxxd93wHRPn4NpKHMBUzEEAjbzLVdOo2F3kmGW7ZXRFHxO0EC9Gw9kJt3dCyKKs19GPF62QH_h38AVOlO0RhIMVa0jPYDGNAqixCEgITeQEY43gSCnjx2qmmsV_uCCTwnLcvPXQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NoR1kNVdqliy0Wcw8XxCVgz5TYQ9KVtV3yd_0Gs1K7pbUOFq55yV0YbciXA-fJ3FSRLNCIq_EgLw5KSWMZx6OQpNcYCYElKpHrRLI0abF8ckEqc2vOQnLj576XTOj-jThIqrerMX07YrlOugEXnAizp35UVIwTA6U9c1WWiJpYt98YwOCYF06jvrkhv34nGmnZNHSXXyoBFBCpaysoVHx5xjNsTPqiRwvcz3zRVcjLkiq10R3w33jTg6fW3ndFXjZvIy5H_0lir6H7SC3MvMcK6xedXwIoVROlA5ir5XWRo74i1zNcT9c_dy1PPM4cAc8BxZCaulkZUSFJe6tJeofw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران؛ دهمین کشور قدرتمند در حوزه سایبری!
🔸
در این شاخص، ۸ مولفه اصلی از جمله نظارت و پایش گروه‌های داخلی، کنترل محیط اطلاعاتی، توسعه رقابت‌پذیری تجاری و ... سنجیده می‌شود که در بعضی از آن‌ها، ایران رتبه‌های بالاتری را کسب کرده است.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/675870" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675868">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82e84c6426.mp4?token=aAfnCNTvZXkg-aM1jCPh3kVNYomxtjQ8b9GnyT3TYV75Zy4dQ3KhSHRqKaQLogLieZ2tbro70NgjBCA5KzsfK3VpEjRqxd_w5V55DilJ2_ZQHFKxhVm9H5bjVQTw837X4APokN9xw1I63uVHgfgEKOuRPuUW7HiKTYYvNiCedQS6E1ieixu0SAcRbz5akIcZJOMHxylj-6I3o_6ipEvEIXe0OqVBbsHwEpuNkcTCqTXDPoFh9pU0M8GcLNrKc3XszVtw2eIywGXBJePcspk0XDmfge2-GtIjlDrTpTRCpq544atx9-1Y87_tZvBj2DE9Yrd9Br8kyZDm9J_CminTwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82e84c6426.mp4?token=aAfnCNTvZXkg-aM1jCPh3kVNYomxtjQ8b9GnyT3TYV75Zy4dQ3KhSHRqKaQLogLieZ2tbro70NgjBCA5KzsfK3VpEjRqxd_w5V55DilJ2_ZQHFKxhVm9H5bjVQTw837X4APokN9xw1I63uVHgfgEKOuRPuUW7HiKTYYvNiCedQS6E1ieixu0SAcRbz5akIcZJOMHxylj-6I3o_6ipEvEIXe0OqVBbsHwEpuNkcTCqTXDPoFh9pU0M8GcLNrKc3XszVtw2eIywGXBJePcspk0XDmfge2-GtIjlDrTpTRCpq544atx9-1Y87_tZvBj2DE9Yrd9Br8kyZDm9J_CminTwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقر تروریست‌های تجزیه‌طلب در اربیل همچنان در آتش می‌سوزد
🔹
ظهر امروز پایگاه‌ تجزیه‌طلبان مستقر در کردستان عراق مورد هدف پهپادهای انتحاری قرار گرفته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/675868" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675867">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
شلیک دوباره به کنسولگری آمریکا در تورنتو
🔹
کنسولگری آمریکا در مرکز تورنتو بامداد دوشنبه برای دومین بار در سال جاری هدف تیراندازی قرار گرفت.
🔹
پلیس اعلام کرد مأمور مستقر در محل حوالی ساعت ۴:۴۵ صبح صدای چند گلوله را شنیده و سپس یک خودروی سفیدرنگِ بدون پلاک را دیده که با سرعت از صحنه گریخته است؛ تعقیب این خودرو ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/675867" target="_blank">📅 21:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675866">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سخنگوی کمیسیون انرژی مجلس: در سیستم ما مماشات با مسئولین خطاکار خیلی بالاست و بیشتر رفاقت‌پروری وجود دارد/ گاهی بعضی افراد خاطی در سیستم ارتقا هم پیدا می‌کنند و جایگاه بالاتری می‌گیرند
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/675866" target="_blank">📅 21:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675865">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
دیدار با ۱۴ معصوم در تجربه‌ای باورنکردنی؛ ۳ روز فرصت برای پرسیدن هر سؤال
🔹
00:16:50 خونریزی در مغز با تزریق آمپول اشتباه
🔹
00:29:40 آرامشی تکرار نشدنی با حضور سیزده مرد و یک بانو
🔹
00:33:10 فرصت ۳ روزه برای پاسخ گرفتن از هر پرسشی
🔹
00:38:30 ریزش لجن از قلب نزدیک‌ترین دوست به خاطر حسادت و توهین به اهل بیت
🔹
00:42:20 نگاه آزاردهنده به نامحرم، لذت بهشت را از بین برد
🔹
01:00:00 چرخ ستارگانی به تعداد فرزندان، روی سر هر انسان
🔹
01:07:10 روییدن میوه در گلخانه پسر با دعای پدر در برزخ
🔹
قسمت چهاردهم (پرسش)، فصل پنجم
🔹
#تجربه‌گر
: حسین صاحبی بزاز
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/675865" target="_blank">📅 21:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675864">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9kRFyMV10WnLdtBmwcGbEhZmHOMcOr4TIWtDliw1nh60lvqC0JrTNBPGxJMz8K_hSBbwhu6RNiG9DiEowSPvnYQI1ooTVsmyxUu_BAWpxngJE0ysDskFgwxrjX19ltlcmGyc8OADDoTbqnX-5qHlOaTxTpZ9EdKzm4ZcDDTcwcLdSM9Z3eAbKO0WhrFijqem8HyLVQMEiMReLEqPB5N7YaLZIQzyV9VaNS-VAeKob16XqrbhkzKvPcEncwAaFyGgcrobyR39oVSzj8S6IOnudqh2jBSHY_LsuiBbnBAJsQ9Bb3ltrBjJdk2-cOI3ujuxPHNZO2AoDS-twxHRhbN8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بیمه شخص ثالث چه خسارت‌هایی رو پوشش می‌ده؟
خسارت‌های
بیمه شخص ثالث
به دو دسته تقسیم می‌شن:
🔸
خسارت مالی
: آسیب به اموال دیگران، مثل خودرو یا موتور
🔸
خسارت جانی
: هزینه‌های درمان، نقص عضو یا فوت
✅
بیمه‌بازار در دونستن تفاوت این دو به شما کمک می‌کنه تا موقع خرید، فقط به
قیمت توجه نکنید
و
پوشش مناسب‌تری
انتخاب کنید.
👈
مقایسه و خرید بیمه شخص ثالث
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/675864" target="_blank">📅 21:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675862">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ادعای باکو: ایران تلویزیون دولتی آذربایجان را به فهرست «رسانه‌های متخاصم» اضافه کرد
آناتولی:
🔹
آژانس توسعه رسانه‌های آذربایجان روز دوشنبه اعلام کرد که ایران، کانال تلویزیونی دولتی AzTV این کشور را در فهرست «سازمان‌های رسانه‌ای متخاصم» خود قرار داده است.
🔹
این آژانس نگرانی خود را از این اقدام ادعایی ابراز می‌کند و می‌گوید فعالیت‌های برخی از رسانه‌های ایرانی در آذربایجان طبق «اصل عمل متقابل» «غیرقانونی» تلقی می‌شود.
🔹
تهران هنوز قرار گرفتن AzTV در این فهرست را تأیید نکرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/675862" target="_blank">📅 20:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675860">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR6R1zBbsUSOF1ptUBMNfXBHzHgkRZZ0jZ1gsAhkNpMGNih-crb-lLFnDsqNWoQ2hUcpTsmIXtRiL2qDConqYCN2eUV1uWYPuMegsA59n0JU84-oKE-6-V_mKwSshv29SlAEWHC_JhGmQOlwyMi0yxsOKtUyURGijY0b45w4FLR0PLVEWrtiRTy5QA_9HfO4pIRiPzzYeVoGtOWj38Bkb732jPqoO7RLpZ9z8iQqNz_5yz7zLfwMhFEWqfQ7zA3ccASFwrDeCFCeUyJWSbMAOSpAG2xlRe5x1gsVaWN3ELYWb2hrdPYmPPkOr6HZfdirLGVAFRJeWe0rVv9qckjh2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این علامت‌های روی لباس رو ندونی، ممکنه با یک شست‌وشو لباست رو خراب کنی
👕
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/675860" target="_blank">📅 20:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675858">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک معضل جدید در موضوع کالابرگ
رسول بخشی دستجردی، عضو کمیسیون اقتصادی مجلس در
#گفتگو
با خبرفوری:
🔹
به دلیل اینکه برخی از فروشگاه‌های کوچک توان مالی کافی ندارند و دولت بدهی خود را به آنان به‌ موقع پرداخت نمی‌کند، نمی‌توانند با کالابرگ به مردم کالا بدهند، بنابراین از گردونه خارج می‌شوند.
🔹
برای حل این مشکل دولت باید در فواصل زمانی خیلی کوتاه پول را به حساب فروشگاه‌ها واریز کند تا بتوانند به کار خود ادامه دهند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/675858" target="_blank">📅 20:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675853">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
سگ‌زرد: ما با خیلی از کشورهایی که بدون ما دوام نمی‌آورند، بسیار مهربان بوده‌ایم
🔹
می‌دانید بدون ما چه کسی دوام نمی‌آورد؟ اسرائیل. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/675853" target="_blank">📅 20:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675852">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
سگ‌زرد: ما با خیلی از کشورهایی که بدون ما دوام نمی‌آورند، بسیار مهربان بوده‌ایم
🔹
می‌دانید بدون ما چه کسی دوام نمی‌آورد؟ اسرائیل.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/675852" target="_blank">📅 20:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675850">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427876ae4e.mp4?token=vFvJLvIAUSPG90rImux3VxEZkPXJYFYPS0tRiOg4RpUleVlY-dWc2Q50owTiIgCwH0yxEAUeYRiaWS5UH2Qu176HnySnMY2rvh7HFX1V36Fxi6u5qTcj3Om9C3PLoi420IzlYSCz3530qyd-mgBvpRXbc9_sH8v9vl2A9y05-uosuHxMJNQj2zjh99qfCm1Uf2lUYJ6XVnvXostBj_GgdGFVfEA0YDxCkrIsDf3gXxLWmMS66MpoKl77YlPhb4tqJxo6OC16EdUo2BC_cHC2Eo0CYQyGNaHKUBWAv7kZQjxH7wri_6L2vqL2OhT0xhV_zId3Cwd2e8H99ZdwikGT0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427876ae4e.mp4?token=vFvJLvIAUSPG90rImux3VxEZkPXJYFYPS0tRiOg4RpUleVlY-dWc2Q50owTiIgCwH0yxEAUeYRiaWS5UH2Qu176HnySnMY2rvh7HFX1V36Fxi6u5qTcj3Om9C3PLoi420IzlYSCz3530qyd-mgBvpRXbc9_sH8v9vl2A9y05-uosuHxMJNQj2zjh99qfCm1Uf2lUYJ6XVnvXostBj_GgdGFVfEA0YDxCkrIsDf3gXxLWmMS66MpoKl77YlPhb4tqJxo6OC16EdUo2BC_cHC2Eo0CYQyGNaHKUBWAv7kZQjxH7wri_6L2vqL2OhT0xhV_zId3Cwd2e8H99ZdwikGT0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به جهنم
🔹
لیندسی گراهام، سناتور جمهوری‌خواه و جنگ طلب واشنگتن که همواره مواضع بسیار تندی علیه کشورمان اتخاذ می‌کرد و خواستار اقدام نظامی علیه ایران شد، در شامگاه شنبه، بر اثر یک بیماری مرد. گراهام سال‌های زیادی علیه ایران و در حمایت بی‌قیدوشرط از اسرائیل…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/675850" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675849">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
محاصره دریایی یمن علیه عربستان؛ صنعا معادله «محاصره در برابر محاصره» را اجرایی کرد
🔹
نیروهای مسلح یمن با صدور بیانیه‌ای رسمی در پاسخ به محاصره ۱۲ ساله این کشور، از آغاز تحریم و محاصره کامل ناوبری دریایی علیه عربستان سعودی خبر دادند.
🔹
صنعا با تأکید بر آمادگی…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/675849" target="_blank">📅 20:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675848">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a086966c85.mp4?token=Rt5V9rlXqmq4vZwcDnRePgM0tQM4kVv0QGIzzNwq6dTMySaYy0otfMAZm6u56TmaYjSUxLQZaccaFUtqBA0jG1aJzP5W-eEyMXUaKwUL4biZHymGw4Tg6VbpATcn20nxneyKE5-qKAZhhiw5EhvhMTwvS-uE4ppn9diL8I6BMsu-VoHKKx0Juh1QOMqbD6SERTHNQ5IhqJN9FUCFCinYQyDJU1sxev9VSlKot1Cs0znYGMs_4hFr4HF9wHlxdzVWeiBsbNlSbNAPsrAVS63qWQqvPsdvsV59ATG9_faZMr24p-ucYcuDpwFSuqvvyOzOzEjnU4vyY0WZ5I9df2IdvI8O1_R6GoQpxRfFpZxhC-BYA_zq2E8VmKEnMWeBwuVedteDrKQACiIcyp_C88kDnnV_B6Nc2xei-HqAqmtnwjituWRcoxJmT9G3uBgFGU3aTK_wAKLtd4rpADg_RuYNdusYMeY8COvZOYyPfc2NJSb82H7KrZKxK_tjvl4kHdC6YPnIIoeEdSidO_O9Y0hA0uckLW7tApuAy1qyFKXDM_kbMqVpLFYectYfJPz4TYymeJgu8IE_B7kOe7aj2Q863lN2EgV0y2MTxO5swFFSgouvotWDMd3EuyP3FSfWNqPpBKZEQOssHhZL2yvF4GAxpVUBLlAJxkd7o8hp4kVwW6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a086966c85.mp4?token=Rt5V9rlXqmq4vZwcDnRePgM0tQM4kVv0QGIzzNwq6dTMySaYy0otfMAZm6u56TmaYjSUxLQZaccaFUtqBA0jG1aJzP5W-eEyMXUaKwUL4biZHymGw4Tg6VbpATcn20nxneyKE5-qKAZhhiw5EhvhMTwvS-uE4ppn9diL8I6BMsu-VoHKKx0Juh1QOMqbD6SERTHNQ5IhqJN9FUCFCinYQyDJU1sxev9VSlKot1Cs0znYGMs_4hFr4HF9wHlxdzVWeiBsbNlSbNAPsrAVS63qWQqvPsdvsV59ATG9_faZMr24p-ucYcuDpwFSuqvvyOzOzEjnU4vyY0WZ5I9df2IdvI8O1_R6GoQpxRfFpZxhC-BYA_zq2E8VmKEnMWeBwuVedteDrKQACiIcyp_C88kDnnV_B6Nc2xei-HqAqmtnwjituWRcoxJmT9G3uBgFGU3aTK_wAKLtd4rpADg_RuYNdusYMeY8COvZOYyPfc2NJSb82H7KrZKxK_tjvl4kHdC6YPnIIoeEdSidO_O9Y0hA0uckLW7tApuAy1qyFKXDM_kbMqVpLFYectYfJPz4TYymeJgu8IE_B7kOe7aj2Q863lN2EgV0y2MTxO5swFFSgouvotWDMd3EuyP3FSfWNqPpBKZEQOssHhZL2yvF4GAxpVUBLlAJxkd7o8hp4kVwW6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور بعضی از وام‌ها به صورت نامحسوس بیشتر از سود، ضرر دارن؟
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/675848" target="_blank">📅 20:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675847">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wjtqp5rX4xNebKvzxkPainx3hjGocIP2gOYaRcSMSVHsgSH5qvUBrEfdYq--T9DVxLwxa6nQb0Xlnhoy5KkouaqMEXGmxfEVFcYAB-q-EBhTQkXYVyhEHANHISwFOaCc8pCuVaBnjp_7IVhuk84j-257GzQchkdaevBDU4m4NEnui-yZkV5CkjzwVXHiMd4MnptVePLLg8s7q59SC5ZHuSyZhE0GQ0E8Rbwdc_ARk8-56x3IddHL-2q462_21oOU8786xYzzpolPq121iRSff9QMPXFrRBkYU9WpjFJSCU9LNWK1bQpSdGC7FgElbNeBlfr9HVYNkfMZr9BtaRg_2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/675847" target="_blank">📅 20:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675846">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ezf7-o6XZe2s30ar8_lDEnuYwFaVk3r3phzK1YNvcRiA-A-IkvEcorUOmbOEIzd7EzS8DZ0RVfcPBBEO1z4hvjjudLNmGa8ZWRFClPUS-KZZNLm5lY9cz1SMypvjOImekS1y4IGZbAz--ZLtp0Lt3UbeMEsvjkH-A6G5G2BAsoBP2DbTKGv2Kub5FhB6c7kHqzKYOtc4v16HdAxobE6pBc1uFZDD6jjmS2QiUDrNCfhAqdWtIuAgVVR8VVr4WtN3ATOOs-hMuLmjdQ_OvZ4Ts4-hY1KeEMGj4hFTJE2ZuZHL9BCTB0mt2V2wtdvSEEtkdjP2QqPL_7dxsMXSNbxfEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
بزرگ‌ترین جشنواره فروش عمده بازرگانی رنجبر آغاز شد!
✨
🎉
از ۵ تا ۱۵ مرداد، انواع روتختی، شال مبل، روفرشی و پتوهای برند شادیلون را با قیمت همکاری  و اقساط ۱۰۰ روزه تهیه کنید.
🚚
ارسال به سراسر کشور | ویژه فروشگاه‌ها، عمده‌فروشان و همکاران حوزه کالای خواب.
📩
برای دریافت لیست قیمت، موجودی روز و شرایط همکاری، فقط کلمه «جشنواره» را در دایرکت ارسال کنید.
🌐
RanjbarTrading.com
📥
دایرکت تلگرام:
@ranjbartrading_com
📢
کانال تلگرام:
https://t.me/ranjbartrading_general
📞
راه‌های ارتباطی:
☎️
۰۵۱-۳۳۶۶۶۵۰۰
📱
۰۹۱۵۲۵۰۳۲۰۶
📱
۰۹۱۵۰۴۴۴۵۹۱
🌿
بازرگانی رنجبر؛ همراه همیشگی همکاران در سراسر کشور.</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/675846" target="_blank">📅 20:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675845">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
نگرانی از تامین و کمبود دارو کاهش یافت
🔹
با وجود نگرانی‌ها درباره محدودیت‌های حمل‌ونقل، آمارها نشان می‌دهد حدود ۳۵ درصد واردات دارو و مواد اولیه از مسیر زمینی و ۵ درصد از مسیر هوایی انجام می‌شود. از سوی دیگر، دارو و مواد اولیه دارویی تنها ۰.۲۳ تا ۰.۴ درصد از وزن کل واردات کشور را تشکیل می‌دهند.
🔹
موضوعی که بنا به گفته مسئولان، به دلیل وزن کم، افزایش واردات هوایی و زمینی را امکان‌پذیر کرده و می‌تواند مسیر واردات دریایی را تا حد زیادی پوشش دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/675845" target="_blank">📅 20:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675844">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ادعای
ترامپ قمارباز: ممکن است اتفاقات خوبی در مورد ایران رخ دهد
🔹
آنها می‌خواهند ملاقات کنند و ما در حال ملاقات هستیم ؛احتمال دارد که بتوانیم به توافق برسیم.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/675844" target="_blank">📅 20:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675842">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4-zgl-06fStRjFnvmGTv7I4jtpMuUDJ-RTo-tPFGjZelOpXHt6K-sDEipXJHoP94s4VuIlLyFJ9I6-Vf7MdAoES-FNFW8EJyMBfUGlFIXFqLs5lHgIqp_9tlgQyKfNOPanR3lBY3CBLLd2gerCiTewatKiXQZLpwCe-OmSastfVbqRLZTZvT-ug1jzQwVysnULbkAcpR1FXlPa57Ef9aP2FE-UA0XbO8JkmSqqnIyfR_SI7nyXKlpo7Nm-JqkZfMPXOU2yss_IqDarWdTga-Rx3_66QeWmnabCZhTK0elIb3yDtdmEMyLBkQ6UDbp9Q7Nq4BL6WeCviXsE8vNYYjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نبرد روی میز
🔹
در شرایطی که معادلات منطقه‌ای همچنان پرتنش است، میز مذاکره به صحنه‌ای دیگر از نبرد تبدیل شده؛ جایی که هر واژه، امتیاز و موضع، بخشی از موازنه قدرت را رقم می‌زند. اکنون دیپلماسی نه در برابر جنگ، بلکه در امتداد آن تعریف می‌شود و گفت‌وگو، ابزاری برای پیشبرد اهدافی است که پیش‌تر در میدان دنبال می‌شد. اعلام آمادگی ایران برای ادامه مذاکرات در ژنو، دوحه یا اسلام‌آباد، از تغییر میدان تقابل حکایت دارد، نه پایان آن.
🔹
هشتصدوبیست‌ویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/675842" target="_blank">📅 19:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675840">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سخنگوی کمیسیون انرژی مجلس: کشور در وضعیتی نیست که بتوان قیمت بنزین را افزایش داد اما به دولت این اجازه داده شده است
رضا سپهوند، سخنگوی کمیسیون انرژی مجلس، در
#گفتگو
با خبرفوری:
🔹
دولت می‌تواند هرسال و هرفصل قیمت حامل‌های انرژی را افزایش بدهد. در قانون بودجه ۱۴۰۵ هم ممانعتی برای افزایش قیمت حامل‌های انرژی از جمله بنزین وجود ندارد.
🔹
در مورد برق و گاز افزایش قیمت اتفاق افتاده است. پیش‌بینی می‌شود اگر قیمت نرخ سومبه ۱۰ هزار تومان برسد حدود ۴ تا ۵ میلیون لیتر مصرف بنزین کاهش پیدا کند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/675840" target="_blank">📅 19:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675839">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqotd4EOwpTm_7TAkJ1lFXxfGf6FAxDbBQKz9WJDloK9qH4fomGDiEX4QmNYqjtU1ggN2qFf7fJ6fvkrwIG3NrZ23drVnAG7DQiYKJivVxtVll1X8EE1nnQf8QPTi-rwATfGkebWx0GKEcjTurnVPeXNGox0sjJMyEILDvppMPJJLvfRVedCem3M1gMtlf-ELoffI01n78XtvQtJDLG_I42WBiJVYwayKx9qI-sgaiKcJs6Hvpl1V89Q-T3VhZEe_kR7tJXNsaBxgOlS6kP4r871BfeSoeYyjYe91akE60iOuSo7jkSCRw_Sk4HHY3c92CgtoBDdbTS-EAl8E-zc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای شفق‌نیوز: آمریکا با تسویه غیرنقدی ۱۱ میلیارد دلار بدهی عراق به ایران موافقت کرد
یکی از اعضای کمیته برق و انرژی پارلمان عراق:
🔹
واشنگتن به بغداد اجازه می‌دهد بدهی‌های معوقه ایران برای واردات گاز را از طریق تأمین کالا، از جمله غذا و دارو، به جای انتقال پول نقد، تسویه کند.
🔹
ریاض عدی به شفق نیوز گفت که ایران حدود ۱۱ میلیارد دلار طلب پرداخت نشده از عراق دارد که بخشی از این مبلغ در حال حاضر در بانک تجارت عراق (TBI) نگهداری می‌شود، اما به دلیل تحریم‌های آمریکا علیه ایران، قابل انتقال نیست./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/675839" target="_blank">📅 19:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675838">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167fec05e0.mp4?token=IXv5JDayXuihtbls3t3RhDWd586Xcqn2iv6M9GAIhFXSPHn5DF2TL5eHasfWsvp51bBVt4p24towOGZpyCN5RnKl8ne1QwE5ssKJ-UpaCEwaZvfYW88QXHzhfhoOHDzCVVDAc8NXNOyPxhvLhn8grEP4sCeV3YO0GP4H_dewbxmwyAICBro-TRSE-LNwbzC3y-riJayTMBJ1UuNIjb8lxUDA9JCanqMiMhaiozhsHVq6ewWDgdWWPiYk32F3Bj_Ln3cHTjFgby8rqch6Aes5DbBmt90LaZqA8zhBcbmBe0qv8zVI8-LkG8NLi9X42jSx96ml276ag2bu9ZlYk4qFbJTKpUlxILTXwc5h8adb1K2nJDu6omfd7qsNj9h7I2xmqiGQ32FyKD5OLsgH-uwLOiy0TKsLiYgSDuCQ1L-_gy2Pmkbh_D66LzgGrSHLAkZsYv4YmsMPL2Kcp5OCI3U-ZbqGEdc02O8tTSEiN75JJPDxXEjnMUP4sbkiTOmmVJR7gNR4oPv3X0p-s8_meZs6NEU24D6pxtyCQixlSFrJ9oo2nu_IIK1p71kk-e-HT4i96nqZNF7JZal7HG8AWohyltLXiQQvUHVSHODGtGOlwC7NfaYslsjUZJ27uez7ib0y0QLIrgqsZ6eliDbZnpTJi0PB1Qz4oD0xrfKHKzXiQPo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167fec05e0.mp4?token=IXv5JDayXuihtbls3t3RhDWd586Xcqn2iv6M9GAIhFXSPHn5DF2TL5eHasfWsvp51bBVt4p24towOGZpyCN5RnKl8ne1QwE5ssKJ-UpaCEwaZvfYW88QXHzhfhoOHDzCVVDAc8NXNOyPxhvLhn8grEP4sCeV3YO0GP4H_dewbxmwyAICBro-TRSE-LNwbzC3y-riJayTMBJ1UuNIjb8lxUDA9JCanqMiMhaiozhsHVq6ewWDgdWWPiYk32F3Bj_Ln3cHTjFgby8rqch6Aes5DbBmt90LaZqA8zhBcbmBe0qv8zVI8-LkG8NLi9X42jSx96ml276ag2bu9ZlYk4qFbJTKpUlxILTXwc5h8adb1K2nJDu6omfd7qsNj9h7I2xmqiGQ32FyKD5OLsgH-uwLOiy0TKsLiYgSDuCQ1L-_gy2Pmkbh_D66LzgGrSHLAkZsYv4YmsMPL2Kcp5OCI3U-ZbqGEdc02O8tTSEiN75JJPDxXEjnMUP4sbkiTOmmVJR7gNR4oPv3X0p-s8_meZs6NEU24D6pxtyCQixlSFrJ9oo2nu_IIK1p71kk-e-HT4i96nqZNF7JZal7HG8AWohyltLXiQQvUHVSHODGtGOlwC7NfaYslsjUZJ27uez7ib0y0QLIrgqsZ6eliDbZnpTJi0PB1Qz4oD0xrfKHKzXiQPo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بررسی تصاویری که ابعاد واقعی انهدام پایگاه های آمریکا را فاش می‌کند
کارشناس کانادایی:
🔹
انهدام رادارهای راهبردی و دوربرد توسط ایران، شکاف‌های عظیمی در پدافند موشکی آمریکا و اسرائیل ایجاد کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/675838" target="_blank">📅 19:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675833">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nobxFH51m6xNqaXPfECYrcKfS0NH5zft4pt62Tt7MJPSzb572QL1fIhHUiMqcq3Lp8tD-Czgcrvj6_F_FSrSJI4k_ZjuaBYO54-2fvdjyw7oq0gmc4NBnGXVhlZgbfQkFMFBQGhP2Z3l48X3sLZVEQj0xhdCIqMGpt67LLPAkpECRxam58NGyt53wwQ6wFk0-A4Pdvp1z2-N7GsLrTkk0NCFkaqjnHiiskCEhCvvcNHSAn_yvzUsfawarX9WF8H8dyblKsMZKlGGNsTMUOAB00Qz901eoKHSLeZYPx3oH9_xCmE_qC1KQw75wQIFyMBfuce_c5R56L_nRoVawlxptg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JphjDYkCvUoekIlZGHJhlOeBdAR0euFRG_8AJHPgwLpFfVo4zrBtHDzd8l1HrzyobZV29a6hV7FZIPvyphOuKtj9_1e-BPY_X2gHHCfHB_452x8bxdx6LwuahZGvhb1Sinj-Wvpp0UwhMB9Uz9aCIICvz3IMlrtb9KA2P6lyv15LwX3jsI7MJPN3tvYToJpXF-Y79_BOStDiJVptbic4mDuMKnUt1fRd68KgEfaPhP-2a6PhKzPzX9SRgEWqJe0Iz-2G_H7DD5kJJmyT0pK66VPWIEWYE8nhnhJ9saWK6ftkRxtheVAyC29Y1LPANG9l09UibnETmx0Y0faPDlJ0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JC5kTDL4nWKBAyYPMtmXn2h9b83YXslU2Z5l44vHefK1a4nUZHOxS2gRRg5wE9-EfcT_qPuvNMu7KRIXz2cbiZbMfytlRBLLhBRogDIyz-Hfy4apKjb8pmX2QZcuRaaNcxXWJZ3jJlw7Yymi4GK3Yx51NEDUVCDQRhrvIgk-QrQ6k-ftlZv9kEUA0ydhRFMSXXWFeC0oCS0-IzABTBLc7dIOep3kBr5qAr9Sy5mCGBvgK5HX73eY8MsJ6aZo6QC25QffYVMBxK1i4Htgeq8zwJYVQtX04AOuEdSD7B90cdD7xvIyqhXrMPTPmp5u3TdG4g3ZK9ura6UVFPB1Wtu5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0QJAFEOZnPHukmEHlP-ycPA3qr5DlM_kOn2Qxr8UaLHbvnvNEPzSxaAGMsdxTxKimoLhj3wP4bwEifSLjxslhEdSc5NeISR7jOBX9xQIrEpi46I8CgkG0ZRWyFDij6q5NyLOEG_xj70SaqXafWic1Pvs9yCzipS89OIhC6t_ZhENoytZuJutNx2A5W7sPsA7RUJ6rDXUb44Si1wMmWi3ddEYZUITRbbdiAna7RNIrVTuWHZFiyngBJvZtujHUQt_TBywu6iz7_eUVNtkeoQuKkfK_xa93Casx1q455RhqC8kaMzS36xmUUIWVgOfDBmF5uDJ8ibuvngDlhuUoArTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پرفروش‌ترین فیلم‌های سینمایی ایران در سالی که گذشت؛ مرد عینکی ۲ میلیون و ۳۵۰ هزار بلیط فروخت
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/675833" target="_blank">📅 19:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675832">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 بزرگ‌ترین خطر آینده جهان از نظر شما چیست؟</h4>
<ul>
<li>✓ آلودگی و مشکلات زیست‌محیطی</li>
<li>✓ نابرابری‌های اجتماعی</li>
<li>✓ جنگ‌های فراگیر و گسترده</li>
<li>✓ بیماری‌های عفونی و همه‌گیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/675832" target="_blank">📅 19:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675829">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ضریب نفوذ بیمه در ایران فقط ۲.۲۸ درصد
🔹
با وجود رشد ضریب نفوذ بیمه در ایران به ۲.۲۸ درصد، این شاخص همچنان فاصله قابل‌توجهی با میانگین جهانی ۷.۱ درصد دارد. این رقم در کشورهای توسعه‌یافته به ۹.۵ درصد و در چین به ۳.۹ درصد می‌رسد. ضریب نفوذ بیمه از تقسیم حق بیمه تولیدی بر تولید ناخالص داخلی به دست می‌آید./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/675829" target="_blank">📅 19:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675828">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c298eb37e.mp4?token=aKOLSrglp1eIOPJK55ZOrQphvGXvNPHoqHHKuWvh64dT1k8EyBVVenVMVt1pquiNCUpeI8-bYA9ZfQ3gE_f0m3aw7EP7ec9NHuO4qdKKv4WkawQkXczwFjbgc8PlkEpV9U05pMmApKjlXEAB7FtaNAckH00Clt38vmeYRr2cyzhyWntnY6eR_RrHp4TKk2_CwTMn-P5Quk2g1H5eHDS_7XC0WEjeASEYIxEUVo7aiFXo4DS9fLJsNjN7-MKq4vSWo8xv7KwJ_xAm_ztSadO3xvqRyhk8LhihFvUID3xG9DtTd0pep9x8M1bBQmMzT9MguQMZcI3SeX6aL8AW4VhxgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c298eb37e.mp4?token=aKOLSrglp1eIOPJK55ZOrQphvGXvNPHoqHHKuWvh64dT1k8EyBVVenVMVt1pquiNCUpeI8-bYA9ZfQ3gE_f0m3aw7EP7ec9NHuO4qdKKv4WkawQkXczwFjbgc8PlkEpV9U05pMmApKjlXEAB7FtaNAckH00Clt38vmeYRr2cyzhyWntnY6eR_RrHp4TKk2_CwTMn-P5Quk2g1H5eHDS_7XC0WEjeASEYIxEUVo7aiFXo4DS9fLJsNjN7-MKq4vSWo8xv7KwJ_xAm_ztSadO3xvqRyhk8LhihFvUID3xG9DtTd0pep9x8M1bBQmMzT9MguQMZcI3SeX6aL8AW4VhxgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فضائلی: آیت الله سید مجتبی خامنه‌ای هم مانند رهبر شهید، مذاکره را حرام نمی‌داند
عضو دفتر حفظ و نشر آثار رهبر انقلاب:
🔹
در سیاست جمهوری اسلامی، اصل بر تأمین منافع و امنیت ملی است و بر همین اساس، مذاکره نیز حرام دانسته نمی‌شود و می‌تواند همزمان با پیگیری تقابل و انتقام در چارچوب منافع کشور دنبال شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/675828" target="_blank">📅 19:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675826">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ابوالفتح: دوران پذیرش تلفات در آمریکا تمام شده است
امیرعلی ابوالفتح، کارشناس سیاسی در
#گفتگو
با خبرفوری:
🔹
اکنون که جنگ زمینی شروع نشده، آمریکا ۱۷ کشته داده است. دوران اینکه آمریکایی‌ها ۵۰۰۰ یا ۲۰۰۰۰ کشته بدهند و مردم بپذیرند گذشته است؛ الان برای ۱۰ کشته هم اعتراض می‌کنند.
🔹
اگرچه روی کاغذ احتمال حمله وجود دارد، اما به لحاظ عملیاتی، هزینه و فایده آن فعلاً باعث تردید آمریکایی‌ها شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/675826" target="_blank">📅 19:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675824">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSI4ZhDSg1iEkV-iatmdY_4R8GJTVWAo01ddUu8edjEeIDrfvfMRCbt2WNhTZa4GBJMlAPa0o5s9jgVSvhoL_GIjOtoI7NcOykSeJ0r4Zw5sK6kd3Khuwfkt13JGWRtEL61s8qDB1RtFmIlSyBC85W91it6s0pvoGDP1jocfwJZ553tqJOlQIpTo1SsQp_EbymbCqTJXeHWSi5R1lBZ9FeqrRpXvPbJSVDSYZqx27Nde8XAtW_Z19RkCfk0i3hNIgmYLwmgW3kOLg6KfQdTWmaZNcboBpo_abvVzbQrOc9jkudvKGhxwOX6mUAB1Gx2OARJfohNX_XIzrzsy2WBtBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توت‌عنخ‌آمون؛ فرعونی که پس از ۳ هزار سال با «نفرین مقبره» دوباره جهان را تسخیر کرد
🔹
توت‌عنخ‌آمون، فرعون نوجوان مصر باستان، حدود ۳۳۰۰ سال پیش در ۱۸ یا ۱۹ سالگی درگذشت و برای قرن‌ها در دل «دره پادشاهان» فراموش شد. او در زمان حیاتش چندان مشهور نبود و تنها…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/675824" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675823">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1afccbdfd.mp4?token=PdE1P8APPvpwgdiAA-B9hSIhgCWYQck47otqSZ98gL8VcjXdPhPg80wGAMgf6dE4uGsDoJRut0yzcxm3kj-qWJIwnKi6KzFrMdt_3q-ITZiZJU-ZMa9plWSe5qp7LQFAMSpf2b6MLeGEz-F8fqT60EPsh8W_i_7t2UTRDW7LEuIVna0xuYoAHRjVPNS6cw9BbKwMDZ3a8bIRKE7K0Tm3k6AwJgy0kjosYYf2n970HGU16xRL3p_jOfAYNds58-Wo4vpw6jas_XSPhc32lAqp9-2C2HRcrqaIhwQo8TuTzyuD1E3iOZIN-1FsdscpOj6cvaLpwnUqH_41ItOd8mgVdrrPMQYBZzE7WSeEG-jh_AB8ig5sZZboN0HHSGH4hk0Qk722XBYGzENjMt3gHAfiKsly7R43QOvyLDf6cBjwqxRrmPxoNC9OK_u25Z1MReTSMxB5Jo4zrl5hY9qRSIgfL1KuDN54CR9nlrpEg_dZpP4SbA_o-_IaupQPt60pBh47383UmwMRYG32tH7uQShigwppVUAmf9W-Gd636J2ucORL86m_EgARfGmL7gTedUBp1gkJa5cL5EuokDYgUKpAnV0XCk9DJMmO1ecnEo4rLYnqTCEnMyWsDf27z33IAiPoGNxgDGM4qre94GM8R3xNGD66qyjSlYosR_yXTx8fAxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1afccbdfd.mp4?token=PdE1P8APPvpwgdiAA-B9hSIhgCWYQck47otqSZ98gL8VcjXdPhPg80wGAMgf6dE4uGsDoJRut0yzcxm3kj-qWJIwnKi6KzFrMdt_3q-ITZiZJU-ZMa9plWSe5qp7LQFAMSpf2b6MLeGEz-F8fqT60EPsh8W_i_7t2UTRDW7LEuIVna0xuYoAHRjVPNS6cw9BbKwMDZ3a8bIRKE7K0Tm3k6AwJgy0kjosYYf2n970HGU16xRL3p_jOfAYNds58-Wo4vpw6jas_XSPhc32lAqp9-2C2HRcrqaIhwQo8TuTzyuD1E3iOZIN-1FsdscpOj6cvaLpwnUqH_41ItOd8mgVdrrPMQYBZzE7WSeEG-jh_AB8ig5sZZboN0HHSGH4hk0Qk722XBYGzENjMt3gHAfiKsly7R43QOvyLDf6cBjwqxRrmPxoNC9OK_u25Z1MReTSMxB5Jo4zrl5hY9qRSIgfL1KuDN54CR9nlrpEg_dZpP4SbA_o-_IaupQPt60pBh47383UmwMRYG32tH7uQShigwppVUAmf9W-Gd636J2ucORL86m_EgARfGmL7gTedUBp1gkJa5cL5EuokDYgUKpAnV0XCk9DJMmO1ecnEo4rLYnqTCEnMyWsDf27z33IAiPoGNxgDGM4qre94GM8R3xNGD66qyjSlYosR_yXTx8fAxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😣
گردنت درد می‌کنه؟ شونه‌هات افتاده؟ موقع راه رفتن احساس می‌کنی قوز کردی؟
فرقی نمی‌کنه خانه‌دار باشی، کارمند، دانشجو، راننده یا حتی ساعت‌های زیادی با موبایل کار کنی؛ نشستن و ایستادن نادرست به مرور باعث قوز، افتادگی شانه، گردن‌درد و درد قسمت بالای کمر می‌شود.
✅
قوزبند طبی با طراحی ارگونومیک به قرار گرفتن صحیح شانه‌ها کمک می‌کند
⭐️
مناسب برای:
✔️
افرادی که شانه و گردن درد دارند.
✔️
خانم‌های خانه‌دار که ساعت‌ها مشغول کار هستند.
✔️
کارمندان و دانشجویان.
✔️
راننده‌ها.
✔️
کسانی که زیاد از موبایل یا لپ‌تاپ استفاده می‌کنند.
✔️
افرادی که احساس می‌کنند هنگام راه رفتن یا نشستن قوز می‌کنند.
💰
قیمت قبل: 1,598,000 تومان
🔥
قیمت ویژه: 1,098,000 تومان
🚚
ارسال به سراسر کشور
💳
پرداخت در محل (در شهرهای دارای این امکان)
⏳
موجودی محدود؛ همین حالا سفارش بده.
👇
https://memarket24.ir/product/brief/38083/180124/</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/675823" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675820">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
یورونیوز: سومین هشدار ایران به بلغارستان صادر شد
ادعای یورونیوز:
🔹
ایران پس از آنکه بلغارستان اجازه استفاده از پایگاه‌های نظامی خود را به آمریکا داد، هشدار تازه‌ای به این کشور صادر کرد. اقدامی که تنش‌های دیپلماتیک میان تهران و صوفیه را تشدید کرده است.
🔹
سومین هشدار تهران به بلغارستان پس از آن صادر شد که ترامپ، به‌طور علنی از رومن رادف، نخست‌وزیر بلغارستان، به‌دلیل فراهم کردن امکان استفاده از پایگاه‌های هوایی این کشور قدردانی کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/675820" target="_blank">📅 18:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675819">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1554001316.mp4?token=lompJUCoGNuQVuokniQHRQIZK1lRVtFaypPknX8AwFGEY6j5KN42HTDLaSP4_oXUde7q4mZ6S8NPwjjaNWBlHW_IUJ_5R4P3zpljem7ggQf371GFQanF8URzSkynZ8NQCFrtu-_7mUf3eFzeY4hJPwABuNc2pJM3lJqVxcLnmQdZ9kDOUk0903oEn1YnBkWtTWxC1V2m1xUQtLJdXuHuCrlbJUvFCrzW88AJne0MHeTT5SPj-KTlJV2iDr6mN2ULYg9dK9p2kp5pzIoA_D8clDO9LHvbsgNwvih8_qtwqYdYmk_exCLv0dDsxGIZTEKs3aaloN9Ey1RG3LAYA0rTiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1554001316.mp4?token=lompJUCoGNuQVuokniQHRQIZK1lRVtFaypPknX8AwFGEY6j5KN42HTDLaSP4_oXUde7q4mZ6S8NPwjjaNWBlHW_IUJ_5R4P3zpljem7ggQf371GFQanF8URzSkynZ8NQCFrtu-_7mUf3eFzeY4hJPwABuNc2pJM3lJqVxcLnmQdZ9kDOUk0903oEn1YnBkWtTWxC1V2m1xUQtLJdXuHuCrlbJUvFCrzW88AJne0MHeTT5SPj-KTlJV2iDr6mN2ULYg9dK9p2kp5pzIoA_D8clDO9LHvbsgNwvih8_qtwqYdYmk_exCLv0dDsxGIZTEKs3aaloN9Ey1RG3LAYA0rTiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های دردناک حامد عسگری در حاشیۀ محرم شهر دربارۀ مادر یکی از شهدای مدرسۀ میناب که هر روز ماکارونی درست می‌کند تا شاید فرزندش بازگردد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/675819" target="_blank">📅 18:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675818">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سخنگوی کمیسیون انرژی مجلس: حدود ۴ هزار مگاوات برق به دلیل جنگ از مدار تولید خارج شد/ قطعی‌های برق جنوب به همین خاطر است
رضا سپهوند، سخنگوی کمیسیون انرژی مجلس، در
#گفتگو
با خبرفوری:
🔹
ما گزارشی از قطعی برق به صورت گزینشی و تبعیض‌آمیز نداریم. گاز را همچنان بر اساس قرارداد به ترکیه صادر می‌کنیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/675818" target="_blank">📅 18:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675815">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVIfVYm_Y9RLXajSgktQUkD3NLyxNouKZvWpwj0Zy-isipv6kijtVdKGgkjtinhGwSvblw2wDPWsbFczrKCxqvG0GtJiBXjMnW7H_AlZKhhCxenT0-x2L4b8cvob0OzaFRzxuDW8TKfttV91uNkAlJ5AEBs2_cZSJ_oXLnIrC1SPz8A49oljgsPA7yI1KWqw1T1oQJjtDUBtdCnP0LUGV2BuXAMPXjsuVXR7eqPWxeYy6dF0Yhg_kg7q0CnUPuV0TMYcyY0U1fe2BwCeP0J-4rJZb6sqgYGiX2fYipq5RbEPivj0M1S1O38YX04qv7XT0ZSSNP3ldtnolTMN3YhdnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای آسوشیتدپرس: میانجی‌ها می‌گویند به پیشرفت‌هایی در مذاکره با آمریکا و ایران رسیده‌اند
ادعای آسوشیتدپرس:
🔹
مقامات منطقه‌ای اعلام کردند که میانجی‌ها در بازگرداندن آمریکا و ایران به مذاکرات، پس از توقف حملات هر دو طرف پس از یک دوره تنش‌های به سرعت رو به افزایش، به پیشرفت‌هایی دست یافته‌اند.
🔹
دو مقام منطقه‌ای که به شرط ناشناس ماندن برای بحث در مورد مذاکرات پشت درهای بسته صحبت کردند، گفتند میانجی‌ها به رهبری قطر و پاکستان در تلاشند تا شکاف بین واشنگتن و تهران را پر کنند تا به توافق آتش‌بس موقت که پس از تبادل آتش از بین رفته بود، بازگردند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/675815" target="_blank">📅 18:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675809">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OL6j58PIcCX8dP1T9aBHB_MfxP8t9rL4Tga5Ef0ROLV_HajqrRcfs2zlHF43ZkC-PcORU_vz2uGf9jDDKphkB3hPLxeqMGl0TPAO8pCzVGzc0bx4lIdqdGwprd4OyOnLXvXwqFn27JGEaiXlV1FIih2co97mk_yZBFLv4X0AlYHEil587fBeAPa9NvQ9hkh7xU7b0WA3ZIloMQYxQMsEA2VzrekpdLmxF6oGzALYFHpWTKwNFWoRqucBhbKWERndVATxywDfFD_xYfvWEQeAIiSJ4bAaIFNQGDvd3wdu4QdN1QwOfa5O73lD1R1BQ5KclPJTafVKVgr2bTaV4O2Ahg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnUCkqrpUtc2BeZb_fJQetZcFDJQ2SruxBK6j-CIr-EPXrGh7sFKUmRyrRxAaGCErWYNfthzBPZMItPbEGWNKCNlVmrlIsNYq-MSXt8MTpUzyaQY43ZHhsWYE5kHgJw7U1b9m9WILkcuoLjDjVQMH6S3BdBFElVj2dt4O2gJSSd2YlzjQszquB83D0ZBpo3I96FN5XLNiu-3LgGUVRzTKb4EG5647Vwsln4QLKQgFqbZv0dyJqQQbol_AHxy8BlQwj-MLhBZVHsk7LIoyKXym8gjxISEx8TzaStVzoBs2xqCkgfjJdDiURBc-7fvLqmb3pofbY9Ei91dr2ve1SXvvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nEZRPY2EyHnYPIDsruxBBuDsOKoxj7KOhUFByzY8itZZNLYRn_xMHb9Y3r4kPrzaWuoDGp4ObXa3rHkHmO-SgI3NiBIMeTH-5JTvlwChxFzpmXWAvnTyGwHCm-2dfw8wFv9Bt8ryfQcU5wZYnmpC1kxw6oMAftig5T3JRglEh5kC2FYWAXNxkvDYmNsncJgQed6A8m7S3z8Iq-tTxGen4j1bN7yhJw7xdyKZRwempNSIDjgPuyRc3CTwVcUOlcw8pWQBCV0vUUeLIx2Odprln5VKumnyB50o8g8D37nme8o_h8FUU0sd6iiQCU3j83WjjnZx_x9x26aJPM9I7M5soA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLtUyTCotoCNzQPZJu6BigAQZpIIlQP8XvWUjj1GxnBm8AFlRNdPFLiO-9ZLuUy660AdNiqXGpOXcFTWJptATYxKOuodA1HUW4LKtFFuh0-0vKTZkxoK9Q4458fLvvjiS8YBeJt3vAaceKhTn4u4lJWZOlU3zG1jaobG8qbhUP9YXIaVj8d5mu-ICDA3lc0Ran6_BzV2mNOmxob6ibc8VKDMMDJCbuRj75YATxxORBwSOpmD97e0qyYx70IoOEswC8te2rSFba_6HvMkAeGQs_f9BWgSU1ra2aDOn4NvU_G4V-mpvoZ18GQ8ijgEOB2ZqLb0S58sO_DdCwdE_UGQ5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
مدیریت هوشمندانه مصرف با تغییر عادات کوچک، سهمی بزرگ در پایداری شبکه برق کشور داشته باشیم
🔸
تنظیم دمای کولر روی ۲۵ درجه
🔸
استفاده از حالت Sleep برای وسایل
🔸
جداسازی شارژرها از پریز پس از مصرف
🔸
استفاده از ظرفیت کامل ماشین لباسشویی
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/675809" target="_blank">📅 18:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675807">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f2710a8ea.mp4?token=SOXEygH30h9oQKNLeBuNmNRTXNdv4D8ZjwMrZAd8DaGYjA40d1TK--REkARHp5s_cwR5XKu6IT-4s4h1SceLee0coRCd4fGtE9hmK39KMMLHWCcF8GPZPSFwGKjWlQPVtKQ39J1XNc68IxRXolZfl9zxSWFDhA1Cri8q2NhmVv7jUj3Gs0WPCK90ybQZ7-gqeGW4oiIh_ZU2chl-_fWXOyuLeJYj_CSdUHPsZxCz4g3EKtbukmluH3VFuDz9KgwTP8pSYGUo_yxMzwoKD4-HeOv2YE--wK365ZoRTBsUxlB3V2KFUfl5n1XnRq4rCxN60OkygQsDPpcS7edB4N-MDjSl09Gee4U-rNWjoIr9pTmY6q3jkjdaZjNdvQrF2vFA1HZDWWJXb4s9MWToE_wd5PlOz9q7I_8kbDXGWW5JCgvlf_4Tum-oiy2lUDDYiuItq65KvhnjF2lhERfsNiguc843evHvKqAIFC95dPv_gmjaBREX4VJ_KZ_v4oZEvsl2QCStG6xiN7MzRoWPCxO5RZ2OA5dpCu_x_f8FH9hKMZmE--O7AKvAyxFiwdBnze3_unfec4TvzCTpBu4MzVb4vnu3wuoDbNtXVln6pVTwQhkrociLUjSo_ZeH8s_DW5fC77soOtyY7Ml0EvgJ9MLBDPOlipqr1CKOXB9e9zw-Zyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f2710a8ea.mp4?token=SOXEygH30h9oQKNLeBuNmNRTXNdv4D8ZjwMrZAd8DaGYjA40d1TK--REkARHp5s_cwR5XKu6IT-4s4h1SceLee0coRCd4fGtE9hmK39KMMLHWCcF8GPZPSFwGKjWlQPVtKQ39J1XNc68IxRXolZfl9zxSWFDhA1Cri8q2NhmVv7jUj3Gs0WPCK90ybQZ7-gqeGW4oiIh_ZU2chl-_fWXOyuLeJYj_CSdUHPsZxCz4g3EKtbukmluH3VFuDz9KgwTP8pSYGUo_yxMzwoKD4-HeOv2YE--wK365ZoRTBsUxlB3V2KFUfl5n1XnRq4rCxN60OkygQsDPpcS7edB4N-MDjSl09Gee4U-rNWjoIr9pTmY6q3jkjdaZjNdvQrF2vFA1HZDWWJXb4s9MWToE_wd5PlOz9q7I_8kbDXGWW5JCgvlf_4Tum-oiy2lUDDYiuItq65KvhnjF2lhERfsNiguc843evHvKqAIFC95dPv_gmjaBREX4VJ_KZ_v4oZEvsl2QCStG6xiN7MzRoWPCxO5RZ2OA5dpCu_x_f8FH9hKMZmE--O7AKvAyxFiwdBnze3_unfec4TvzCTpBu4MzVb4vnu3wuoDbNtXVln6pVTwQhkrociLUjSo_ZeH8s_DW5fC77soOtyY7Ml0EvgJ9MLBDPOlipqr1CKOXB9e9zw-Zyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکی بخون، بدون کنکور
🔹
رشته پزشکی ۹ میلیارد تومان قیمت خورد!
🔹
این شهریه دانشگاه نیست، هزینه ادعایی قبولی در رشته پزشکی است! ماجرا رو ببینید، احتمالا شگفت‌زده می‌شوید...
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/675807" target="_blank">📅 18:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675806">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d677525559.mp4?token=Tqq2ldq5kOhzxlnq-cJ-ZxRDH5wtNlfOtjPN9UybdjCn5je90-R-jmQ99pFH1VqjdwpgRKH1dbvf3mY_RMEaQK866MfZ2VYAEZFBRJ_k9ZkQXqIXtbhlE27upWZSw0iORm8FI9pxJ41toEBFDr9YDvJGokSKPexMvcs1Zes2F0kgRWFU2KyPVS_8Q4UQMymK6huNKIpYe27Mtl7ARXgIMa6AW3KPSjDNrA8UEXZ063GFQ6OX4Q1zYs_dYwWx8-5YZyEhJwHZ0hyVECtpJZfD_kU2FscHVeoIO6-q9jGPi2jU0XOlv2ecxHFHguRzkCWVSwWTw6nFJgefBh-apB0HvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d677525559.mp4?token=Tqq2ldq5kOhzxlnq-cJ-ZxRDH5wtNlfOtjPN9UybdjCn5je90-R-jmQ99pFH1VqjdwpgRKH1dbvf3mY_RMEaQK866MfZ2VYAEZFBRJ_k9ZkQXqIXtbhlE27upWZSw0iORm8FI9pxJ41toEBFDr9YDvJGokSKPexMvcs1Zes2F0kgRWFU2KyPVS_8Q4UQMymK6huNKIpYe27Mtl7ARXgIMa6AW3KPSjDNrA8UEXZ063GFQ6OX4Q1zYs_dYwWx8-5YZyEhJwHZ0hyVECtpJZfD_kU2FscHVeoIO6-q9jGPi2jU0XOlv2ecxHFHguRzkCWVSwWTw6nFJgefBh-apB0HvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا وطنمونه، خاکمونه، محل زندگیمونه؛ ما با این خاک تعریف می‌شیم #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/675806" target="_blank">📅 18:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675804">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ایده‌ای نو که از دل پسماندها بیرون می‌آید
کارخانه‌ای که ضایعات از آن جان می‌گیرند و به محصولات مبلمان شهری تبدیل می‌شود
🔹
محسن قضاتلو مدیرعامل سازمان مدیریت پسماند شهرداری تهران: نیوجرسی، دیوارهای بتنی و فلاور باکس‌هایی که در این کارخانه تولید می‌شود بسیار مقرون به‌صرفه‌ار از بازار است
▪️
عبدالمطهر محمدخانی سخنگوی شهرداری تهران:
در مسیر اصلی خیابان‌های آزادی و انقلاب و در ادامه بزرگراه‌هایی مانند شهید همت از این محصولات استفاده خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/675804" target="_blank">📅 18:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675803">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1Bk4vlUaZCuR57bE4Rgnttz0weFsuL4bRed7Ma8kA-Piocd6NeErwX1mcGvfzzz2TTVhC92be8r60EuStTSDHtF9o3_PJzw61D7Hd3YQ1A5NccPubiKQHDvSoAbtumyS9d_1-f_0PkdAVA0fWwBMAgafxatyHQztB0F22lkz91P1_knTZMyRiuHNknC-o5sl1DBf92Nlo5wiglUz-OulY9xFI9K2mGU8jLpXWbYQ0pIvnBS7dr_mZq6mPkdp89hkAnBS2ApCLJd8uj6ONH3BSvJPQCl_AIMaGkoWLu6vMkkBO8zCoDqRGa6PAnveKfEn3mW0cVH75jig1z0_KEvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داروسازی دکتر عبیدی هشتادمین سال فعالیت خود را گرامی می‌دارد
🔹
هشت دهه نقش‌آفرینی در سلامت ایران که از سال ۱۳۲۵ و با پایه‌گذاری نخستین لابراتوار داروسازی کشور توسط دکتر غلامعلی عبیدی آغاز شد و امروز با تمرکز بر کیفیت، نوآوری و ارتقای سلامت انسان‌ها ادامه دارد.
🔹
داروسازی دکتر عبیدی در آغاز دهه نهم فعالیت خود، با تکیه بر دانش، نوآوری و تجربه، همچنان برای افزایش دسترسی جامعه به راهکارهای درمانی اثربخش گام برمی‌دارد.
برای مطالعه متن کامل خبر روی لینک زیر کلیک کنید:
https://abidipharma.com/abidi-80-years?utm_source=messenger&utm_medium=post</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/675803" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675802">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCtt6zJf9moQFbyRvWuiazE2FW3f5PC7MyySN7veFkAU5zdz6NIWgZooQ3LfE-NqzTZBUG5EEJnMCl_W-ArgdG3mqVuS08OedKYuVVmC-0x_umHVmhCaWo-l_t-ADlNHRcejFPPiLFp9Uld_jv1p6o14zr6A4kcKAG3W_SizntGBU2xZjMdjVfW2ZFxwsGkSOP3WVvUcivLDLqCyhCXcDTLPsIf8kA7_54VN_ImosFSgfIqDVswysFv4imhP3K_zXzP7s4IKCeYEW2THJCbUUCUdJ3zYiLdewl3Gs3lOGR1J3Qg-I_rmSWYJzUTKgkUupCZHh1Zl_OEo1QsUaMppdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ژاپن برای مقابله با گرما، یخچال انسانی ساخته که در چند دقیقه کل بدن را خنک می‌کند
🥶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/675802" target="_blank">📅 17:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675800">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سخنگوی کمیسیون انرژی مجلس: جنگ بلندمدت و فرسایشی باعث تخریب زیرساخت‌های ایران می‌شود/ ما نمی‌توانیم در مقابل زورگویی آمریکا کوتاه بیاییم
رضا سپهوند، سخنگوی کمیسیون انرژی مجلس، در
#گفتگو
با خبرفوری:
🔹
در دوگانه جنگ و مذاکره هستیم؛ باید درست بجنگیم و درست مذاکره کنیم. ایراد وارده وجود چند صدایی در کشور هست که پیام خوبی را به دشمنان نمی‌فرستد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/675800" target="_blank">📅 17:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675798">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPDy570FCL0O8_IlP62KsCPb8WhOmjDL6l5SOpiPJYXeHu4WMEXqHgnbdNZwvKoVzegb4eeBMq80iefxK7nZsrMQiMfB2xE3kUj1L1y4t3-7gKTr-UQNPRDjRUyGI83KHIfNnd1xVxPIGDN-VxycE7F6MiYOwviPhc_agv6ySBVwa_lw0bphvZO_J1uP2-PvmmpLoDIZqpGjs8-VNwTy5SPnTj0cQz1d_V22j2LW_FRilj-XJCOgqtU8bWk6Kn4TVZB-BeIFfWNZSBgKM6VfuqJTuQEwr9uYFSdCShH812TFYAmWGlcTHNBkXsJOU72L3dgSRSDEMSnVIBWBcpFqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر کمتر دیده‌شده از حضور رهبر معظم انقلاب در نماز جمعه نصر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/675798" target="_blank">📅 17:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675795">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e77e1528be.mp4?token=ZkDXzrKtgKjjRBV8psUGneGbNrzI8_7b67cbG5qxqAL7Y6NMK9IPFq_gxMCCkJKfpe5DUrfWAMHMC2wbPduMcaHaAGEogR93c_nVmCjUADIS8VKKwoojQzEdexdABqRcMzxPWYHL65xtWrYT7R1p_39plephpbyv7lWMMvU3I6Z6q6yoEAshErJJ2FVMRbnkUyrMfE_sK79L0SC2Amy8nr7bNUExyNf-AMOF95Ea7FoDowPO_druB78BFaDVMTnv48XpnBrjcEPYBFOpKGrkuc3vNzP4CD6WkRV5Ea_lQyw1Eg_UJPUPZHOv2EU3IXqez3ehaAqD_3FT1D_Qul1LZ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e77e1528be.mp4?token=ZkDXzrKtgKjjRBV8psUGneGbNrzI8_7b67cbG5qxqAL7Y6NMK9IPFq_gxMCCkJKfpe5DUrfWAMHMC2wbPduMcaHaAGEogR93c_nVmCjUADIS8VKKwoojQzEdexdABqRcMzxPWYHL65xtWrYT7R1p_39plephpbyv7lWMMvU3I6Z6q6yoEAshErJJ2FVMRbnkUyrMfE_sK79L0SC2Amy8nr7bNUExyNf-AMOF95Ea7FoDowPO_druB78BFaDVMTnv48XpnBrjcEPYBFOpKGrkuc3vNzP4CD6WkRV5Ea_lQyw1Eg_UJPUPZHOv2EU3IXqez3ehaAqD_3FT1D_Qul1LZ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی رؤیای غرب به درخواست کمک مالی ختم می‌شود، اشکان خطیبی به جمع‌آوری کمک مالی روی آورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/675795" target="_blank">📅 17:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675794">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
تیزر قسمت چهاردهم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای حسین صاحبی بزاز یکی از بهترین مخترعان کشور که به دلیل بیماری سرطان خون، تحت درمان قرار گرفته و در یکی از مراحل درمان با اشتباه یک پرستار خونریزی مغزی کرده و روح از جسم جدا شده و در دشتی زیبا با ۱۴ معصوم دیدار کرده و حضرت زهرا (س) اجازه پرسیدن هر سوالی و شنیدن پاسخ آن را در مدت ۳ روز به ایشان می‌دهد و آقای صاحبی با بهوش آمدن از خانواده خود درخواست پرسیدن سوالات را داده تا واسطه شود و پاسخ آن را به آنها بدهد؛ نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: حسین صاحبی بزاز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/675794" target="_blank">📅 17:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675793">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXqB5ddePxPzZ2_77bWU6PsTwRiYtDKV8znefE2Si4j68D4YPV8FDWvSjgII-WeZE2GyEnPYjQL5Dotk2WdEwUD4QoC4oW-d6oesXCtq9-4jergxfcjPDmkrIko71HSRTY8b0kU-uTr3EGBM7TLDDPqEb7nZt5PR6Rc0Bg7hUTtLyGIQ36x89WZjNGf956PUPD0u9vLhMfndfwg85elUmbAjpXb53UClvVesHqxZtmQ1wqgcGTa-lizu4TuYcu0fKWZDXUExbJvHem7deWmdaDDdokviG7IFnJN_0yLSI5cWCbDiNJluSm7Xi6PLZnYnduSAUUv90QSrmeMd0stjrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاف دمای ایران به ۴۰ درجه رسید!
🔸
هزارکانیان در استان کردستان با دمای ۸ درجه، خنک‌ترین نقطه کشور بود.
🔸
دهلران (ایلام)، آب‌پخش (بوشهر) و شوش (خوزستان) با ثبت دمای ۴۸ درجه سلسیوس، گرم‌ترین نقاط ایران اعلام شدند.
🔸
همچنین در۴۷ ایستگاه هواشناسی دمای بالاتر از ۴۵ درجه به ثبت رسید.
@amarfact</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/675793" target="_blank">📅 17:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675792">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حسینی: تلویزیون ۹۵ درصد نمایندگان مجلس را دعوت نمی‌کند
سید نجیب حسینی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
صداوسیما به عنوان رسانه ملی باید منعکس‌ کننده نظرات مدیران ارشد کشور به‌ویژه سران سه قوه باشد. سانسور صحبت‌های آنان نه به صلاح مملکت است و نه به صلاح رسانه ملی، این اقدام اعتماد مردم را کاهش می‌دهد.
🔹
در صورت عمدی بودن، سازمان باید عذرخواهی کند و اگر سهوی بوده جبران کند. با وجود ۲۹۰ نماینده مجلس تنها تعداد محدودی در رسانه ملی حضور دارند و ۹۵ درصد نمایندگان هیچگاه در این رسانه دیده نمی‌شوند که این یک ضعف آشکار است و باید رویکرد صداوسیما تغییر کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/675792" target="_blank">📅 17:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675791">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa2999e06.mp4?token=pQpPjyRqJOTEtull92Ko_3LbdmDWmKlSvFTkWjdrjRTUjwed32mupqC8Lgg_tWsDzJVmY57XhRgSjnAGAD4xPFyTvEN289My9EnDQ7boKMQdZMdfVEFa95sJIfmcrq_sw1NtTb6xxgU6mxjBdp-CpM5ItJYmfkNjPDDhcnG3ARgwcVQH1syHRVNtlNQWvVVPaL7COSIGJvDPMg0LJD_R9uj2DBOYS1vefnvKyhIfCTYB4Z5hDfDnCL1MCSHmVo-0SxeZm4p-nArJ4eTD9yT112bRtRqB1NiL5KEiu-JtNMDzKnd_lr5RRTx4WgVTzO1nNOZynPzxlsbpCknhMdEfWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa2999e06.mp4?token=pQpPjyRqJOTEtull92Ko_3LbdmDWmKlSvFTkWjdrjRTUjwed32mupqC8Lgg_tWsDzJVmY57XhRgSjnAGAD4xPFyTvEN289My9EnDQ7boKMQdZMdfVEFa95sJIfmcrq_sw1NtTb6xxgU6mxjBdp-CpM5ItJYmfkNjPDDhcnG3ARgwcVQH1syHRVNtlNQWvVVPaL7COSIGJvDPMg0LJD_R9uj2DBOYS1vefnvKyhIfCTYB4Z5hDfDnCL1MCSHmVo-0SxeZm4p-nArJ4eTD9yT112bRtRqB1NiL5KEiu-JtNMDzKnd_lr5RRTx4WgVTzO1nNOZynPzxlsbpCknhMdEfWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب‌آبادی: در مذاکرات عمان طرف مقابل اصرار داشت که مسیر جنوبی تنگۀ هرمز فعال باشد و ما نپذیرفتیم
🔹
ما به آن‌ها گفتیم نتیجۀ این اقدام هرچه می‌خواهد باشد ما طرح‌های شما را نمی‌پذیریم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/675791" target="_blank">📅 17:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675785">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">گلیرم حسین</div>
  <div class="tg-doc-extra">حاج مهدی رسولی  قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/675785" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🥀
بسته‌ی
#مداحی
#هیئت_قرار
ویژه
#اربعین
شماره ۱
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi
@gharar_madahi</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/675785" target="_blank">📅 17:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675784">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a679707f.mp4?token=lTB2Yk8DLYpwRtR2UZVT1IJ5AG0Xroh6Rq7L7CZ3986yBLjSC_KbhzrXv2o6qrsM5glDHZd5NMZQ2B_Rf5PQ_C0PLO4dDIiEjec7u298G_rgq1nkmrKgoQ2s6CP8jEE-b_aXelFpu2VVqGHUcZA6fibVDb1kyH7W86maEACiJe9NokKAlmz1gK_7bSYI_mMsZ8zhdKjwr8XEE-L-J4y5fSp5Fovvl4YrWDf9zcWTCKYJZXtG5hOXR2agunmN0nmZOqBFdSZPDQ9W6hn4f90tLQ0o7EG66YGe3xIO2J1Np8vqDVjE9-o7g90iem0VIKBiG9riAtlVqcMKFBFuAlTj8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a679707f.mp4?token=lTB2Yk8DLYpwRtR2UZVT1IJ5AG0Xroh6Rq7L7CZ3986yBLjSC_KbhzrXv2o6qrsM5glDHZd5NMZQ2B_Rf5PQ_C0PLO4dDIiEjec7u298G_rgq1nkmrKgoQ2s6CP8jEE-b_aXelFpu2VVqGHUcZA6fibVDb1kyH7W86maEACiJe9NokKAlmz1gK_7bSYI_mMsZ8zhdKjwr8XEE-L-J4y5fSp5Fovvl4YrWDf9zcWTCKYJZXtG5hOXR2agunmN0nmZOqBFdSZPDQ9W6hn4f90tLQ0o7EG66YGe3xIO2J1Np8vqDVjE9-o7g90iem0VIKBiG9riAtlVqcMKFBFuAlTj8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوگل رمز عبور را کنار می‌گذارد؛ ورود با یک ویدئوی سلفی
🔹
گوگل قابلیت جدید Selfie Video را معرفی کرده که به کاربران اجازه می‌دهد در صورت فراموشی رمز عبور یا از دست دادن گوشی، تنها با ثبت یک ویدیوی سلفی هویت خود را تأیید کرده و دوباره وارد حسابشان شوند.
🔹
گوگل می‌گوید این ویدیو فقط برای احراز هویت استفاده می‌شود، مگر اینکه کاربر اجازه دیگری صادر کند، همچنین برای مقابله با دیپ‌فیک و جعل هویت، چندین لایه امنیتی پیشرفته در این سیستم به کار گرفته شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/675784" target="_blank">📅 17:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675783">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c998f012.mp4?token=prto6ipaNjioLdCYzRZ1IyCkQkv449BjAf4kcpP_u_fV_EsX41F5S1Aeu2tJqwYJE4gSRlQrQYoiRviCH1ELQJhEp1rLlhtvLrJi9KH7_T8C4VGMFLtpNbCWOdNjyekY3wqDcD-EE8K1F8ryXvsV7w9FlsZJIFSYiQcwMtZDS9N-4DwQEtFSDlWe5F_so2GPGkGHBjWRX_Hq6KHhateBB1Jufk1Hx6YaFVTSbxm0XeDDI-ab4456vXM-g6dY1M2eaPgDwoMpWAWA9zIlbB7a4sbD5-bpt5zFaA7is8huu7jk4Wp0G6u-7cla-5id6pwZjb3_yQFRzsTaoOCzXu0V7iRmBa7d9mCZQR4qzSEPIruuYemndGQ0sPEKtmBXN2DO9ALaspS8xrTXcZQ0j7o38kRkjYFLpRuakjLHyOmR9dm2Wc9GNXtIXfIhbIq8888XoxsibGIIoFPgGAtrserHUzhGa9BkYNMrY6fxspzpJHeDUa1PI-tU09btdpYpIdlEPAs2Jn8GjYR4oDkeJq-hVFUna4H1jCWrFKUYMTkdBrQWXZYo2VAsBY8XTt-QdPtWjO6TKWXPhAIGXhd9hOhAKckOwzqs-XtQN5EJ1V2_PA37xjPCeroOEfigeIrE1jl-DJBEMZgeLOZtIdgjAi20255IhesxKLKJCnbCdpDe3I8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c998f012.mp4?token=prto6ipaNjioLdCYzRZ1IyCkQkv449BjAf4kcpP_u_fV_EsX41F5S1Aeu2tJqwYJE4gSRlQrQYoiRviCH1ELQJhEp1rLlhtvLrJi9KH7_T8C4VGMFLtpNbCWOdNjyekY3wqDcD-EE8K1F8ryXvsV7w9FlsZJIFSYiQcwMtZDS9N-4DwQEtFSDlWe5F_so2GPGkGHBjWRX_Hq6KHhateBB1Jufk1Hx6YaFVTSbxm0XeDDI-ab4456vXM-g6dY1M2eaPgDwoMpWAWA9zIlbB7a4sbD5-bpt5zFaA7is8huu7jk4Wp0G6u-7cla-5id6pwZjb3_yQFRzsTaoOCzXu0V7iRmBa7d9mCZQR4qzSEPIruuYemndGQ0sPEKtmBXN2DO9ALaspS8xrTXcZQ0j7o38kRkjYFLpRuakjLHyOmR9dm2Wc9GNXtIXfIhbIq8888XoxsibGIIoFPgGAtrserHUzhGa9BkYNMrY6fxspzpJHeDUa1PI-tU09btdpYpIdlEPAs2Jn8GjYR4oDkeJq-hVFUna4H1jCWrFKUYMTkdBrQWXZYo2VAsBY8XTt-QdPtWjO6TKWXPhAIGXhd9hOhAKckOwzqs-XtQN5EJ1V2_PA37xjPCeroOEfigeIrE1jl-DJBEMZgeLOZtIdgjAi20255IhesxKLKJCnbCdpDe3I8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعبیر جالب دیپلمات ارشد ژاپنی در مورد ایران و امریکا...
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/675783" target="_blank">📅 17:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675782">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnapp | اسنپ</strong></div>
<div class="tg-text">📊
مسیر همراهی؛
روایت گروه اسنپ در ۱۴۰۴
💚
🗓
سالی که با همراهی
بیش از ۸٬۵۰۰ همکار
، فعالیت میلیون‌ها کاربر و ثبت رکوردهای تازه در بخش‌های مختلف اسنپ سپری شد؛ از توسعه‌ی سفرهای اشتراکی تا بیشتر از ۱.۵ میلیارد سفر شهری و از رشد بی‌سابقه‌ی اشتراک اسنپ‌پرو تا تلاش شبانه‌روزی تیم پشتیبانی.
📌
توی این ویدیو، مروری داریم بر
مهم‌ترین آمارها، دستاوردها و اتفاق‌های اسنپ در ۱۴۰۴.
🤩
ویدیو رو تماشا کن و مثل همیشه در این مسیر همراه ما باش.
🔗
مطالعه کامل گزارش سال ۱۴۰۴ اسنپ
@Snappofficial
✅</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/675782" target="_blank">📅 17:00 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
