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
<img src="https://cdn4.telesco.pe/file/iAxVfNDfbUhAPEbjiIMNtdLkwvqpQHsCe0S8vEat5uo-iijOSsuWHSiq4GvpfneEbRlmUFO7yGEftEiNAO_iR2XgfkdYB9ZPThUSwqJCEVLY4h0tXkvca3AuUU6J9hzoWvrayX6hDOZeeoilcw31Tw7I_m4h9k0FIJ8nGOZOdZFOjDaRv6QsdaW_ClIl_cBpinRveKR5B09GvVcGSIDljUzHuGwdGOQL-VSkwL5d-ilgxI3FgaAf-yVYQgLmynJySXAk6pAygGxPLEFHUqtJcWoyCCkAmBaKKvxU9CL0RILHTv8vowh2fo-XsHUcEMFF3x2vq84yxCI4ZbJZEdb3KA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 931K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 11:01:25</div>
<hr>

<div class="tg-post" id="msg-137395">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
شرط واشنگتن برای فروش F-۳۵ به آنکارا
🔴
سازمان‌هایی که در ترکیه فعالیت می‌کنند از طریق شبکه‌های مالی و صرافی‌های ثبت‌نشده و فاقد مجوز، برای جنبش حماس پول ارسال می‌کنند.
🔴
این سند همچنین آنکارا را مسئول تداوم این وضعیت می‌داند و تأکید می‌کند که فروش جنگنده‌های اف۳۵ به ترکیه بدون برآورده شدن پیش‌شرط‌های لازم امکان‌پذیر نخواهد بود.
🔴
ترکیه باید تضمین دهد که در آینده سامانه‌های اس۴۰۰ یا تجهیزات مشابه را خریداری نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/137395" target="_blank">📅 10:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137394">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
استانداری اصفهان: احتمال شنیدن صدای انفجار در اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/137394" target="_blank">📅 10:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137393">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
هاآرتص: تل آویو می‌خواهد تهران را به حمله پیش‌دستانه علیه اسرائیل سوق دهند و در نتیجه برای پاسخ اسرائیل، مشروعیت بین‌المللی فراهم شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/137393" target="_blank">📅 10:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137392">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b2e0a325d.mp4?token=DzRzHVzrunNmvvjAUqRFXSoSab_ms3g-03n2rxLSQckpZ7k3LPlKC5Ggx73jo_CcZ4a_ojmfXhngxCnNimA17kaIz0nuXDkeqXNEezH5HZ0TeV6oJO-xIt86IUvYDLuhxM9kTtgstDAqw8t62NhFgdseBGdq7fBIztDj565_Soi_Up8PggsJWp6I2o5PFArqSeKcBGCffMFbl4owabFZdJQUVEDGAP-euLyPELryQJkCjA6zEJEtjpGqBVlvSb-UZ1edcBwjBr_otAWq1EiHT-g-_hidyWsi-y8STfHVm1aaZx8zID4AAc_pPS4LmIxtlAfXfAqBJnj7dsBYSmfpXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b2e0a325d.mp4?token=DzRzHVzrunNmvvjAUqRFXSoSab_ms3g-03n2rxLSQckpZ7k3LPlKC5Ggx73jo_CcZ4a_ojmfXhngxCnNimA17kaIz0nuXDkeqXNEezH5HZ0TeV6oJO-xIt86IUvYDLuhxM9kTtgstDAqw8t62NhFgdseBGdq7fBIztDj565_Soi_Up8PggsJWp6I2o5PFArqSeKcBGCffMFbl4owabFZdJQUVEDGAP-euLyPELryQJkCjA6zEJEtjpGqBVlvSb-UZ1edcBwjBr_otAWq1EiHT-g-_hidyWsi-y8STfHVm1aaZx8zID4AAc_pPS4LmIxtlAfXfAqBJnj7dsBYSmfpXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کتک کاری پسرها بر سر دختر در یک ایونت ورزشی در تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/137392" target="_blank">📅 10:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137390">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزیر امور خارجه: آمریکا می توانست از طریق گفت‌وگو ابهامات بند 5 تفاهمنامه درباره تنگه هرمز را برطرف کند اما راه دیگری را انتخاب کرد
🔴
استفاده از مسیر جنوبی، حدود ۱۰ روز پس از بازگشایی تنگه آغاز شد. از نظر ما این اقدام واقعاً مغرضانه بود.
🔴
آنها می‌توانستند اجازه دهند مفاد بند ۵ روند طبیعی خود را طی کند و سپس در پایان مهلت تعیین‌شده، ارزیابی کنند که آیا شرایط به‌صورت منظم و مطابق توافق پیش رفته است یا خیر.
🔴
اما آنچه برای ما روشن شد، این بود که موضوع فراتر از یک سوءتفاهم است. به نظر می‌رسید آنها اصرار داشتند که در کنار مسیری که ایران برای تأمین عبور و مرور ایمن و آزاد تعیین کرده بود، مسیرهای دیگری نیز ایجاد کنند.
🔴
آمریکایی‌ها کشتی‌ها را از مسیر تعیین‌شده از سوی ایران دور می‌کردند و در عمل آنها را به استفاده از مسیر دیگری هدایت می‌کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/137390" target="_blank">📅 10:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137389">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f61992002.mp4?token=XlEFNcZmwEhTzJfnrnCKUZiNVieNspGYr5gjswzcXyJpxlAFla1jdxreO_1skoaZ-SG8-RHopKgcM5qMprOFAZu5wPJEnMu_3cwtAHe5_hMKsklF5ibp5DPJgGfrmc6h-ed_w2I38h78A5y52vim96yCCr2hvuo2Z31Glt-PHTRIPJ9B2i8sumiv5Na27gzAiE6djLQwxv9JgdxGx0F9KEPg6Has1pLuUEvYRT3-wVdt7fJOuntHbx2Z15PIgQqwkhx_bTRJXh9fcY9cYAAdL1ytKCRgCrSM2_Vhld9j4nJodVO_V4hYaED6ZtX1IeLPfX967CNtK1pjtw4ACAKOyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f61992002.mp4?token=XlEFNcZmwEhTzJfnrnCKUZiNVieNspGYr5gjswzcXyJpxlAFla1jdxreO_1skoaZ-SG8-RHopKgcM5qMprOFAZu5wPJEnMu_3cwtAHe5_hMKsklF5ibp5DPJgGfrmc6h-ed_w2I38h78A5y52vim96yCCr2hvuo2Z31Glt-PHTRIPJ9B2i8sumiv5Na27gzAiE6djLQwxv9JgdxGx0F9KEPg6Has1pLuUEvYRT3-wVdt7fJOuntHbx2Z15PIgQqwkhx_bTRJXh9fcY9cYAAdL1ytKCRgCrSM2_Vhld9j4nJodVO_V4hYaED6ZtX1IeLPfX967CNtK1pjtw4ACAKOyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روی آنتن زنده، مشاور قالیباف و الله کرم، نماینده جبهه پایداری دعواشون شد.
🔴
الله کرم: شما مذاکره کردین که هسته‌ای رو بدین بره، من به عنوان نماینده مردم نمیذارم.
🔴
مشاور قالیباف: تو خر کی باشی نذاری؟
اصلا کی گفته ما قراره هسته‌ای رو بدیم بره؟ شما میخواستین قالیباف رئیس مجلس نشه ولی شد.
🔴
الله کرم: نذار بگم قالیباف چطوری رئیس مجلس شد !
🔴
مشاور قالیباف: سیکتیر بابا
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/137389" target="_blank">📅 10:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137388">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
اوکراین: حداقل ۱۵ نفر در حملات روسیه کشته شدند
🔴
در ادامه جنگ روسیه و اوکراین، رسانه‌ها از کشته شدن حداقل ۱۵ اوکراینی در حملات به کی‌یف و دیگر نقاط این کشور خبر دادند.
🔴
ولودیمیر زلنسکی گفت که در حمله روسیه به یک نمایشگاه دفاعی در کی‌یف حدود ۱۰۰ نفر هم زخمی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/137388" target="_blank">📅 10:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137387">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ایلان ماسک: تا ۱۰ سال دیگر هوش مصنوعی از کنترل انسان خارج می‌شود و کنترل آن دیگر در اختیار بشر نخواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/137387" target="_blank">📅 10:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137386">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
بلومبرگ: کویت با وجود حملات روزانه ایران، یک همکاری زیرساختی ۱۶ میلیارد دلاری با بلک‌استون، بروکفیلد و KKR در زمینه خطوط لوله صادرات نفت خود به امضا رسانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/137386" target="_blank">📅 10:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137385">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsraDnT-tM_QuotEhQzwV8D7vR5rvxL5BWrN4UPMCMs3nUII50ndclHRJcHp-XpvJlPcL8ZYq2d-qyLKOWVThKdrQ9uoxeZn8MY-dtiKUe86tqbAI5C7r8o1kp18ZCzartQjykVYf7vDnr4ID6TSHP_GgB5XHv-4NxOP9F3Ldt589mNMG3g3RxY8T1tArp_uNvUvTOfn1eZPKHo64ZEhSjK2-LFvrPlKi4l2UOhyQaP3FYU2H_krsCvG2BUByUL3U5eKR9SyM4EjJL0QtGH5OATG-UFnr-ygxPdumP_vqycrcauTO2SVY3lqecK2j8ymT2fj6Wb9WH-_8Kau8Ff81w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص بورس کانال ۴.۹ میلیون واحد را پس گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/137385" target="_blank">📅 09:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137384">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
پایگاه‌های ردیابی پرواز از به هم ریختگی در جریان پروازها و عدم امکان فرود تعدادی از هواپیماها در فرودگاه‌های جنوب عربستان خبر می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/137384" target="_blank">📅 09:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137383">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
دختر ۲۰ساله‌ای که تو خراسان اقدام به تهیه فیلم‌های جنسی ارباب و برده میکرد بازداشت شده
🔴
محتوای چنلش هم تو بات گذاشتیم و میتونید ببینید  زیر ۱۸سال
⚠️
⚠️
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/137383" target="_blank">📅 09:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137382">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeLCL-jbpHJ2AlDz7D317fo4nAhOJz20rXQPvlHdORoWiuc3D40g799y0LKPE-y7rf5zvkhjDAJjshH9yIXt8iMktU2mM94PJpdqEmmvg7sMFvA3Z95tRyQY0tNiGYPgtXg4pflPnobNEnVSe6skmCNE2YqNsOvCl4WtdKCCcGh39fP2RCOz0z2irbiizN9Z-1CptI_phzX8QxkzNKg3X96oOMUysgIr9SNcEaPaP076qPHP9rEAyO9Xe0Rl0s0mTtCrNAWXqC4aufwwxNAKfWEvrnjy7dNr892YmzkQKwRQEX2bO9gPPPhWpdZLeEHONbq91585mdmkqGzHmhul8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تأسیسات نفتی در جیزان همچنان در آتش می سوزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/137382" target="_blank">📅 09:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137381">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
گاردین: ایران توانسته توانایی خود در حملات را از طریق پیشرفت فنی در برنامه موشکی و بهره‌گیری از تصاویر ماهواره‌ای، تقویت کند
🔴
شواهد نشان نمی‌دهد که تهران در این مورد از پشتیبانی اطلاعاتی خارجی استفاده کرده باشد
🔴
از برجسته‌ترین روش‌های ایران، استفاده ابتدایی از پهپاد‌ها با هدف خسته کردن پدافند هوایی ، پیش از حمله اصلی است؛ این موضوع شاید نتیجه تبادل تجارب نظامی با روسیه باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/137381" target="_blank">📅 09:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137380">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
برای نخستین بار پس از ۱۳ شب متوالی، ارتش آمریکا دیشب هیچ حمله‌ای به صورت رسمی به ایران انجام نداده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/137380" target="_blank">📅 09:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137379">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ:  کارها در ایران فوق‌العاده پیش می‌رود. اخبار جعلی را باور نکنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/137379" target="_blank">📅 09:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137378">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRvJbcADHT-KXuxLvPnSu-QPWYObq_qa8q1G4Hsc4r6dI58g-7Sq64-LBIdo7PCtya-thu-WXuIS2Ydwot6h1Eyp-I9ILORkbZln5-UycDULoo01z7uFFZZNIlrRuRIHo9AiXAukQV49-iOOGeX8cpYiV8OTLYCn7jn1-vxSyOsYtYowg8UrRapayDjwTTyC09_ou7yUOYRQvZ3q2CVASE4g0uVMI5G-964aH0bc6IuS9sFA_J2fPQ-6OcZmstE8CIBiUch8wgV2P694pTPUwRLLTF1_vqCUhE8Obd75wF_LfYtSoaoXCFlt6GyPF_lud70iXdj_1APEmys1oSjt6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ازدحام بی‌سابقه در جایگاه‌های سوخت عربستان پس از حملات موشکی یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137378" target="_blank">📅 09:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137377">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
دونالد ترامپ: "دوباره این کار را انجام خواهم داد. باید آسان باشد. من واقعاً در نامزد شدن برای ریاست‌جمهوری خیلی خوب شده‌ام. سه بار پیروز شدم. بار دوم انتخابات دستکاری شده بود."
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/137377" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137376">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: کایا کالاس(مسئول سیاست خارجی اتحادیه اروپا) از نگرانی‌های حقوق بشری حرف می‌زند، اما در برابر جنایات و حملات علیه ایران سکوت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137376" target="_blank">📅 09:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137373">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a61b348325.mp4?token=lEm3QnWgx8f6qqj7P_VwGgCtipVOYFojLH5KOqTCAJwC5-nCo5sTXL-IjEV5KxTcv5fFN03phOxQjbwBV3ZnsxPf2KHMjzKswcbVOR2XAbxu1_MHBcmcEfcsNvpWxRlyhsLc3Xsb8oD4YYs2PNChUrQQnnlInen-OQNRSsfyllQMFod2Iac3p0uSl_EjQLFWf79glnG7HUtY8I16Ps1oc5bKFTd9Gc6NAHcraQpeEPZh7iZVMASwuZ-VRE58m0rY34IeY0JHYt1sMssynuZc4fa_OjeLTUV-Ej36eweFejUjnl_eY_rPrRWYF4bs1SxOtv1xfsSVGotxclwvRJQXfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a61b348325.mp4?token=lEm3QnWgx8f6qqj7P_VwGgCtipVOYFojLH5KOqTCAJwC5-nCo5sTXL-IjEV5KxTcv5fFN03phOxQjbwBV3ZnsxPf2KHMjzKswcbVOR2XAbxu1_MHBcmcEfcsNvpWxRlyhsLc3Xsb8oD4YYs2PNChUrQQnnlInen-OQNRSsfyllQMFod2Iac3p0uSl_EjQLFWf79glnG7HUtY8I16Ps1oc5bKFTd9Gc6NAHcraQpeEPZh7iZVMASwuZ-VRE58m0rY34IeY0JHYt1sMssynuZc4fa_OjeLTUV-Ej36eweFejUjnl_eY_rPrRWYF4bs1SxOtv1xfsSVGotxclwvRJQXfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات سنگین شب گذشته پهپادهای اوکراینی به شهر روستوف روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137373" target="_blank">📅 09:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137372">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JO_UdhMgmZpzvgKPtpUx-N6dOyt9qsaodgdI4GK31jT0OgBF_5LpBvxZzIS5Z4IeIIHqzGjCZMWrr4Nj5me36Yh9O4M95MGRqKxbZKe1XSJLhb0gOrp_cPHFm5MkpaU4Ir9ygrGKSTUznrSy2t0pHzWl9BjBss_RIHyjI3r9Dzk1WRtJ4n4nNqRmzcXFKSRiZDcS_6gavpRSK9UC-0Mpp4JmyuhpqdpOPLhCdriuRSONfoY2ZC7XI8o2AfOkNDl3u2IgpH5KNBNzaxosAs-7vUS88DuuVGyB7CoLJ-8oQfaNiVbDFtk9a5WQj7SDUZfyE4LqhYE7YKhvrjD8BDRmeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت و WTI به ترتیب با ثبت اعداد ۹۶.۷ و ۸۹.۳ دلار بر بشکه وارد تعطیلات آخر هفته میلادی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137372" target="_blank">📅 09:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137371">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxB3oOkuaxXvmyfKGrgRHMh3gSsBq4DiLfYZDT4xIHuyu0we2aNn2jg6rar-VqaJjMvWpG7p4owG8oBKHcnSDC3ueeRnuSYWB2ozU1jfvTUUXo_m0Gtc_68v6DY0GkTHlKP75ubgzSJRrv8-c4XBsFp28JEE_zWyLoZVDpJiIiJCsDDeYzMZa4eLqWtjs8aWdJmhmsyKaN9n-Zz7c3imnkk4AWEFwqQtgoLyOO7PIWajbiCjLJhZGX7wJALUWVwK173J2wQhQGTACZdjLzrGfQ5230ySIKGGYSykMv6ICV1R1k_suqC_iLvkOG75Lbl6Re6uomSCyUzW9_579L5Tlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای تایید می‌کنند که آتش‌سوزی در پالایشگاه نفت واقع در جازان، در نتیجه حملات یمن، رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137371" target="_blank">📅 08:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137367">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d2b02766.mp4?token=tyzg0503uEn6_5mY-Kj9BP8ezHBRX5kBtYNN9o52sD9O5Fw-jBprx86cwfzIW1CHuurhD-Uds3-qzI7y3i6UEej0Tz83QP2wqz2hW25TJHae56ng8JncnJDHsiSAF9kYCt2XIE2G-6Ba8GE7CNlcWpIz-b42gXjilikKffLdh5ux2lDQVF9N_I9pQlGIwQVKL6_uXQk87Nm9-IpHbpTbT4deFecPuCHS5moCbqKtzAi8JM0V7DABAW2CpFV-Yrn_DlgrgjaFhE8ZMzp_Z9PPukIHCUO3HZG-_wLeDDFD3eP6aVCnZi8KB1dE3--HXQKMzDQWFeuUlSbssRp4DcHkog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d2b02766.mp4?token=tyzg0503uEn6_5mY-Kj9BP8ezHBRX5kBtYNN9o52sD9O5Fw-jBprx86cwfzIW1CHuurhD-Uds3-qzI7y3i6UEej0Tz83QP2wqz2hW25TJHae56ng8JncnJDHsiSAF9kYCt2XIE2G-6Ba8GE7CNlcWpIz-b42gXjilikKffLdh5ux2lDQVF9N_I9pQlGIwQVKL6_uXQk87Nm9-IpHbpTbT4deFecPuCHS5moCbqKtzAi8JM0V7DABAW2CpFV-Yrn_DlgrgjaFhE8ZMzp_Z9PPukIHCUO3HZG-_wLeDDFD3eP6aVCnZi8KB1dE3--HXQKMzDQWFeuUlSbssRp4DcHkog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله یمن به تاسیسات نفتی عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137367" target="_blank">📅 08:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137366">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTgGkRDBuLyxetuq5laD1XaEL4bTFh7eCI1cB1_0POez7meckMqzeOe_gZg9c6iDNgHxG755DPVfRG5hyuBkjjKaA1mfrHi2e5H5Zqlb1piQSgnAHkwB37Embt7sPMawC7BLqq6xItzt_4LLeSH_hoDDZ1542Z7aCGfhyF883AGQzVVyWiDycV0atZD8UwXo3qW25BV-VzQVTz2qFeFvT6m9pUVQXqMx0c5-asqLRXZaIJpeq7gRZNOeY9Exu-8q87-1Fh4s5Hi_DMBWH0lzCFUqcVCkJy6vmdj_Y4dE7RoD1feooOYJ4syuRWdlLNKBYpdI_MdpEqwS_-VU_4Tf5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا معتقدن مجتبی خامنه‌ای، رهبر جدید ایران، نسبت به علی خامنه‌ای تمایل بیشتری به دنبال کردن برنامه ساخت سلاح هسته‌ای داره.
🔴
با این حال، مقام‌های آمریکایی میگن ایران هنوز برنامه هسته‌ایش رو از سر نگرفته، اما به گفته اون‌ها، رهبری جدید ظاهراً آمادگی و تمایل بیشتری برای توسعه توانمندی‌های پیشرفته هسته‌ای نشون میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/alonews/137366" target="_blank">📅 03:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137365">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66640af45a.mp4?token=kSgNNsm87byclsghNccbgH3T5ZkqF7EIbwb5_H4ICVJ2pvJ-OdcpTeH7z0Ysme6jZ24ocxxke2CY_HIFtaSfLviNF6Ygg0sHTQmWCyEmbBdWxfoUkgRKj0GCYjwuTyMlMS5YEhpnTWzSCesUAKed8J65Qmkd7BdpxjfHCLmt0gGKxDA5xRQjv06cf3D4G4bRVdTrOhb6ehCSYRgIiIe5f6uFRxQZj2UkmYMQ1V4vg-AViYLD-ar5la6LtVXWFGza9dlf5d4BWw-Pb1fxZrRQUT0d69kLWFZmxlPlS4tqYTLEQUzurBaZSkYM17cD3wptFKUJJ9RiuO--zQ-zq7-yqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66640af45a.mp4?token=kSgNNsm87byclsghNccbgH3T5ZkqF7EIbwb5_H4ICVJ2pvJ-OdcpTeH7z0Ysme6jZ24ocxxke2CY_HIFtaSfLviNF6Ygg0sHTQmWCyEmbBdWxfoUkgRKj0GCYjwuTyMlMS5YEhpnTWzSCesUAKed8J65Qmkd7BdpxjfHCLmt0gGKxDA5xRQjv06cf3D4G4bRVdTrOhb6ehCSYRgIiIe5f6uFRxQZj2UkmYMQ1V4vg-AViYLD-ar5la6LtVXWFGza9dlf5d4BWw-Pb1fxZrRQUT0d69kLWFZmxlPlS4tqYTLEQUzurBaZSkYM17cD3wptFKUJJ9RiuO--zQ-zq7-yqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لشکرکشی شبانه در عراق
‼️
🔴
گویا ساعاتی قبل نیروهای وابسته به جمهوری اسلامی به سمت پایگاه آمریکا پهپاد شلیک کردن و ارتش عراق یه ستون زرهی سنگین را راهی پایگاه‌های حشدالشعبی کرده تا پهپادها رو جمع کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/alonews/137365" target="_blank">📅 02:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137364">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
فعالیت شدید جنگنده ها در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/alonews/137364" target="_blank">📅 02:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137363">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
چهار سوخت‌رسان از اسرائیل برخواستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/alonews/137363" target="_blank">📅 02:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137362">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
دختر ۲۰ساله‌ای که تو خراسان اقدام به تهیه فیلم‌های جنسی ارباب و برده میکرد بازداشت شده
🔴
محتوای چنلش هم تو بات گذاشتیم و میتونید ببینید  زیر ۱۸سال
⚠️
⚠️
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/alonews/137362" target="_blank">📅 02:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137361">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری/ هاآرتص:
تل آویو می‌خواهد تهران را به حمله پیش‌دستانه علیه اسرائیل سوق دهند و در نتیجه برای پاسخ اسرائیل، مشروعیت بین‌المللی فراهم شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/alonews/137361" target="_blank">📅 02:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137360">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
شرکت هواپیمایی اتریش، تمام پروازهای خود به تل‌آویو را لغو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/alonews/137360" target="_blank">📅 02:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137359">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
عوستاد: تا فتح قدس یه یاعلی مونده
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/alonews/137359" target="_blank">📅 02:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137358">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEK_1yWkKkGMeTX5WuFiAQ6_iVfuahFw7WJmn3IZ25ckH94VTew2A0lI0llZSeXCbFcndm2GmKsRENeBCpD8uM8hhrZjYbLugWsJuLWvbE3BXOZ6lrDa5vbW1HqXlWetljQcRfOmN6qwBzmQ6lQ0vTgHFO5XzMf2nDr-wvGAlEIvevqGp0a3GZKp3zddgOW8lqRAFFMBpbr3cm1zqHtGcQvwyhbDz1TDPbkec-Vy414VNdaWv8oX-Q9CCl_w4P4AVo5RVlmUaj77JBzwNk6S53hEvf-N9YkqTnSPDY2I0Q_QUbrxPZlfbFJmxRySZk4aPgBC-q46w4ofag5TEfiHxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد: تا فتح قدس یه یاعلی مونده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/alonews/137358" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137357">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
شلیک موشک از خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/137357" target="_blank">📅 01:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137356">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فووووووری/هم اکنون برخی کشور های اروپایی در حال لغو ناگهانی پرواز های خود به اسرائیل برای فردا می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/alonews/137356" target="_blank">📅 01:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137355">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hect9TDCNky-HB2rXYcqOA1TlFhpRZXY_pdL4fUGDiQM8600ZmmJ7S7LmtqNt1BeAOGxuhc0_1SxmXVf8RrlwkQzM-ToBcwRSZ-pNU-mKWBLbW9wUVemBQfFIUCW4IwE-27h3FP3hRZQsoePYe9vr9ZcMEwDCYhZVDlhPrhV8zo3xBXpzQWUoXONZAQ49LxxqGlt-WaN42Exl8p4hPAe82EKgSIVqVTSSDTuwclnnNUjVzDZDItq7glK2J6VyaSy6nyzZ9buXGWLFO_zhYJ3JKSnWMDfOrexOVv3_GWdD-09D3ug_gB1DGWgRTHj33flj3BuzsK1UgCJa0TdcGsoSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای ارتباطی E-11A BACN نیروی هوایی آمریکا در حال آماده شدن برای برخاستن از پایگاه هوایی شاهزاده سلطان در عربستان سعودی است تا ارتباطات را برای تیم‌های حمله آمریکا تجمیع و هماهنگ کند؛ این تیم‌ها در حال آماده‌سازی برای انجام حملات احتمالی گسترده علیه ایران هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/137355" target="_blank">📅 01:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137354">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e29cb2148.mp4?token=eIBTus2mcGQku30IvVl0KunvXKIf3dmecgUVboOx_HY557N9YQgx7FisUfR7n24jkM8BfxHKePQmjKHRr1yPlo0T1StSR0lBdIUNdK4MMR3WrMqmR_W3CwBkfgaZ9paznjSCLSA6U33p7Xru3kV5rreanydGdEx1g5xY-Eik_uTziHxKgb0tEdstlMsZklT2aeV-KvAx_yXqNDyhz5wiUzX-4yUxDajmekYF9b5C4fCJ4sv-O1VvJdIh0DACMsztjx7JwmhHb3gOjhGNXzzCxuis6mfQr4Ml-yfWebHOTdVz67uId5WnFo3f1RJULWCHd3fSNGQm3uzw9reP5ohTnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e29cb2148.mp4?token=eIBTus2mcGQku30IvVl0KunvXKIf3dmecgUVboOx_HY557N9YQgx7FisUfR7n24jkM8BfxHKePQmjKHRr1yPlo0T1StSR0lBdIUNdK4MMR3WrMqmR_W3CwBkfgaZ9paznjSCLSA6U33p7Xru3kV5rreanydGdEx1g5xY-Eik_uTziHxKgb0tEdstlMsZklT2aeV-KvAx_yXqNDyhz5wiUzX-4yUxDajmekYF9b5C4fCJ4sv-O1VvJdIh0DACMsztjx7JwmhHb3gOjhGNXzzCxuis6mfQr4Ml-yfWebHOTdVz67uId5WnFo3f1RJULWCHd3fSNGQm3uzw9reP5ohTnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این شخص ارزشی این ویدیو فرستاده برامون و میگه حرفم به مخالفین حق هست بزار تو کانال تا ببینی
🔴
جوابش با شما:
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/137354" target="_blank">📅 01:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137353">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
خبرنگار کاخ سفید: سنتکام گزارش داده بود بعضی اوقات ما به ایران حمله نمی‌کردیم ولی میدیدیم که کلی موشک در آسمان به طرف ایران میره، بعد می‌فهمیدیم که کویت و امارات و بحرین و عربستان در حال حمله به ایران بودن ولی به طور رسمی اعلام نمی‌کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/alonews/137353" target="_blank">📅 01:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137352">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری/سیریک رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/alonews/137352" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137351">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cd-ANm1gW3vuWm0NHuVjv4JiY-FDqPLelKbNMGCeumXx4g2FX6Sg3qVcWasvo8B9dhZhkIp2tz6rC1LgQ-xu7Q8JveUNX5J6k8re1GdinT48G_cm2YU0ibTmkRK3w2H-Omz0HBjDWdmUO-dJPx6vYz6noc_iO1cvg094lV_F3onYhCuOqGiebr1cz7nU-Hu4Nawl7rm0wVLZbdeC_WQmbyCbBf8KE7MmbMK7couKgO-cSqy_yPKfCDo3xAdaPIT3FuEv_-7l5qQGnrgw0u-GOJ_mnvgnYkwJ_yDyyr-DgjbxgbsaH-DI34gIxmpxOvTsrg9by6vvokGeabrHEJdgqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همراه اول قیمت بسته های شبانه خودشو 3 برابر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/alonews/137351" target="_blank">📅 01:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137350">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
به نظرم یه جنگ سنگین و فشرده و حداکثر ۱۴ روزه در راهه، از لحاظ شدت حدود ۲برابر قبلیه و ترور هم زیاده. خداکنه به زیرساخت نرسه اما احتمالا میرسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/alonews/137350" target="_blank">📅 01:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137349">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: هواپیمایی اتریش و شرکت آی‌تی‌اِی در میان نگرانی‌ها از تشدید تنش‌ها، پروازهای خود به مقصد اسرائیل را لغو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/alonews/137349" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137348">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq7Pit73x2P6yJVTgbJ_VvXLpcTBZ_yXJ1qt9V6vl6mvUz0cFgsov_zANxVxUHy5GK1RXY0vDsB0di_XXzsYTqD_ytDJvsmmF5fPl9G9HQtwClsebDvx0h-A9eOT2dpSuQs2I7kbg_DdZyknTc5yJ_69QwDvgKQ1kWdjWfYKM-vVrjW0fVlAGMaOXzZXJ0I45G3ZOJbW_tIw_Do9sx9wcdXXTuQBgD4FfA_spQAClTrDH7CtWWn-kQuS8x078ghejMiRR2Su83Nnvf7RXastN7EbGATpowu_-7A1NgLmP8FnEaPOgEz_bnbzRnufaZKJT7ELN7WLcBct_SKnSnOtIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرویز پرستویی: لعنت به پهلوی و همه طرفداراش
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/137348" target="_blank">📅 00:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137347">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
دقایقی قبل یک موشک به پایگاه آمریکا در بحرین اصابت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/alonews/137347" target="_blank">📅 00:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137346">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKR0mHZWXvlSZljtq_-yHMWPpVRr26UYttbTSNFlECOPu1ssNNGPVoItSBiusdCt672oDSy9z8m7k1ovjJmHeE1SqlykuPKXt7lz9cnDRg4RvqrkmzNeinr6NdrJ4BsOG6oVa0UBii8kj7QVLk6PbZsOyHWJtBSgAWvrsdu8xjJuHJGwN8rF1WNfUlX4bDOs_IhRwvdgoY8oFmC1Pv-Kl1OG0y1VpTrKYyf08bdpc_Sko_JyD9F0XhDb8CtTjEMuexyeL93IrSilKGsVclBW1HK68EwnB_bmZFnbeMTEEE6CdvtwTN1MDs6t4ooisN5FlnydGP0E7ngxXuA5tIWaqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: یا مرگ یا ارث بابام
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/alonews/137346" target="_blank">📅 00:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137345">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2479a179bf.mp4?token=K0XnH7_0cPdaXCJZsguT8G6OgRY8JtvX1zzDykymvifm9Zp9AfvL51nM3QahQQInWuyNQLV_-1pvD6zIVo-hdzIzrfSDJDBoU_HIxn1BbZkJ1NxIQw-EA4X8CTji_r8nEfyMjkKizTE4rmALDO2MlgK3HAt4ipM0pStzmy83q518CxT20vNWyKl63AJic-SMwoEpMCKdsUuJPeTNQVizeQpFuIBuzL0ugTUz4pfLi8GT3tM_Q4m9G8nhgrxNALLvXODk-H85cU15TE4k2KuPTQxA3MtgmbvsERw1exbpuupjdYtorTS41EvhbDQwTPTociRFD2Il_VioL1ak2AQ6Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2479a179bf.mp4?token=K0XnH7_0cPdaXCJZsguT8G6OgRY8JtvX1zzDykymvifm9Zp9AfvL51nM3QahQQInWuyNQLV_-1pvD6zIVo-hdzIzrfSDJDBoU_HIxn1BbZkJ1NxIQw-EA4X8CTji_r8nEfyMjkKizTE4rmALDO2MlgK3HAt4ipM0pStzmy83q518CxT20vNWyKl63AJic-SMwoEpMCKdsUuJPeTNQVizeQpFuIBuzL0ugTUz4pfLi8GT3tM_Q4m9G8nhgrxNALLvXODk-H85cU15TE4k2KuPTQxA3MtgmbvsERw1exbpuupjdYtorTS41EvhbDQwTPTociRFD2Il_VioL1ak2AQ6Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی قبل یک موشک به پایگاه آمریکا در بحرین اصابت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/137345" target="_blank">📅 00:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137344">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
گویا سفارت خانه هند هم در تهران تخلیه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/137344" target="_blank">📅 00:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137343">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
مراد ویسی؛ تحلیلگر اینترنشنال :
🔴
تا جایی که من آمار دارم تعداد جاویدنام ها ۳۲۲۲ نفر هست. اگه آمار بیشتر هم باشه اسمی ازشون نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/137343" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137342">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4lD6V2jPrwPlpHtAZkYbQBF46HJNv7ehAMpKh_HUZYrearxxQsMbdOUpzQpmF7U42nq4km7bsgmIbKK8Ufind-IAONumJtAcbu-nudDJBgTJDVkifF9vHdb0AxJJKEYa8Ay5_mpDv6JZ0jWh0MgsHDpu4TQlprzVMOvL8lG72Fo2VUShzUgeq1DQ5t4PVbyIxOtUuXQdHcaA_s38gn-VLBNcqKlMC3Z7-9_PYLcR4z7O8HaD86IUN2LLTnucWEBvJBO-hGjorGprO46FoYM2LhcKYzz_XpnqrhHB-068oXc4zwHlLoVZpDi4i0Zq_BV3vQ1Hlxy6rbKmo-vX6hALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرویز پرستویی:
لعنت به پهلوی و همه طرفداراش
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/alonews/137342" target="_blank">📅 00:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137341">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ائتلاف از حمله به مواضع نظامی انصارالله در استان الحدیده خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/alonews/137341" target="_blank">📅 00:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137340">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=u_i3QOy7C41AjOdAx8uubkmLbiXWeVSGnnEhSE9zQ1JnfkHSSswYFcJWPwq69yuEpFlft6JJbwmRpMooAkR7Nlc9FkPmHSPrJVEPEB0hgCuUcyG6vKozLWElAqP8FSRmEA9xEQsxZeOX4RDLI0dGmFETBfT2iIWUT4fS1nNZ-SrrCBldgy450rWk4YxkEZOSMUR6xB_S6YQe0Ycrf05zK4q9KaU5tN-NHO5HjhGFU_c9IIkXwmf4tL9wz-SOUChQcwDoQxz2fqzk2o10YfTPgKS0mXt8_3tkSVmZjUELCRyJHMJzUnWpa5bg3DRw5M7GAC-RiNV0uJG2ivUR9M5dJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=u_i3QOy7C41AjOdAx8uubkmLbiXWeVSGnnEhSE9zQ1JnfkHSSswYFcJWPwq69yuEpFlft6JJbwmRpMooAkR7Nlc9FkPmHSPrJVEPEB0hgCuUcyG6vKozLWElAqP8FSRmEA9xEQsxZeOX4RDLI0dGmFETBfT2iIWUT4fS1nNZ-SrrCBldgy450rWk4YxkEZOSMUR6xB_S6YQe0Ycrf05zK4q9KaU5tN-NHO5HjhGFU_c9IIkXwmf4tL9wz-SOUChQcwDoQxz2fqzk2o10YfTPgKS0mXt8_3tkSVmZjUELCRyJHMJzUnWpa5bg3DRw5M7GAC-RiNV0uJG2ivUR9M5dJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آژیر حمله موشکی در بحرین به صدا دراومد
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/alonews/137340" target="_blank">📅 00:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137339">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8mLzRo_iYaF-17W7AtfyPoNP7BiQso5FhGSEQnWjf1GSCHEw8X38Cw-YVV7TTMb2DBXD-AWQiT6hKQz7zxiyuxCDtH9xkkrEaeYBC-TRZg57HprN1hlWvQazvaByvuLRMfp7KVyqykyLgvtRP1sprUO7yLfiJLzperH9ohjnjn39dcJzcfwM5EWLVlX6pl_Sn0G8d6wp1suif5KvGZI31CE2RBobBTiXjUkm9RoAXc3IfJXc8LuDpxLbgX-sThOpwYKL405Yo2TFL535FDfZhlS7VqeNrLOWv8R1UeX6P2njBpU8WNXoCISw2Vcb4CCzNm092h6LpM5VLwGKm7L4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دختر ۲۰ساله‌ای که تو خراسان اقدام به تهیه فیلم‌های جنسی ارباب و برده میکرد بازداشت شده
🔴
محتوای چنلش هم تو بات گذاشتیم و میتونید ببینید
زیر ۱۸سال
⚠️
⚠️
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/alonews/137339" target="_blank">📅 00:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137338">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499b17bb9a.mp4?token=EqpkphaNHS37P61bMFCCcF9JCq7EbNiQclFHg8FAr29YfGH0JQy_qDrpyeM5w63QFRfKxq8XS_46f54xdc_F-JCAiUUUw0Ciw8xGneSTrAdI7RbO6Jv3NPjUS2_4Ssg2c-DrNzXuYgE_Ly9BzVi5D45zr_e3GZRfLKGPnAVdphhFz_SYTZx-wJ6fG1sXTmFMb6amheEefxjCy2BQxKBKocQ6YzC4MggVyxj9WBkxkOKwXn2KPgXQWhBYmxkUPMDd1_4dopdemukIzQA1k3QGzJVocAAQQqZ8Dv5raTWLKOz1AeHRZtmJdg1W1DyQ0I9y3-eEyw4Oq-QPDmeqTncxvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499b17bb9a.mp4?token=EqpkphaNHS37P61bMFCCcF9JCq7EbNiQclFHg8FAr29YfGH0JQy_qDrpyeM5w63QFRfKxq8XS_46f54xdc_F-JCAiUUUw0Ciw8xGneSTrAdI7RbO6Jv3NPjUS2_4Ssg2c-DrNzXuYgE_Ly9BzVi5D45zr_e3GZRfLKGPnAVdphhFz_SYTZx-wJ6fG1sXTmFMb6amheEefxjCy2BQxKBKocQ6YzC4MggVyxj9WBkxkOKwXn2KPgXQWhBYmxkUPMDd1_4dopdemukIzQA1k3QGzJVocAAQQqZ8Dv5raTWLKOz1AeHRZtmJdg1W1DyQ0I9y3-eEyw4Oq-QPDmeqTncxvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیروزمند، کارشناس صداوسیما: تا کی قراره مجتبی خامنه‌ای بیرون نیاد؟
🔴
مجری: تا نابودی کامل عوامل جنگ.
🔴
پیروزمند: خب اینطوری شاید ۱۰ سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/alonews/137338" target="_blank">📅 00:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137337">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری/هم اکنون وزارت خارجه آمریکا در هشداری جدید اعلام کرد:
تمام شهروندان آمریکایی باید در برنامه‌های خود برای سفر به خاورمیانه تجدیدنظر کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/alonews/137337" target="_blank">📅 00:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137336">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Djcxnx2FT4FeDY3xbWMmecG6DI2zp5R8amD4nxE-IPNx95sA1ekG-DOLqIjP8bY1xkLWEZng_JUrwLOHaATG-yzkUQkGYMssi16d1lMSYt6wO8_7Lhx091odx_0Ll7FzEYIbhgiB49eN4dpkGA-HXERDuvvbIX5FkhvBcUbiQB2o7Ri5aOnrR_e2kAw77pOBTcQgVc6Y2crrKDYzeu74hJsoMQv56KlwyjjPwJlqJRJQ8dzH0xolDGat8gUBSyd942LgIXOc93HmY8gHPZNKo01SXHxpb3chV_-hGwmHPUdS4K1oDlvsGnV9FEZZ2AcB2_Wz354Gk0CB39B6jZx8Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارشات بمب افکن b21 raider که جدیدترین بمب افکن آمریکا است جهت عملیات در تهران به اروپا منتقل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/137336" target="_blank">📅 00:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137334">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
نیویورک تایمز:
مقامات نظامی می‌گویند بمب‌افکن‌های دوربرد B-2 و B-52 در ایالات متحده در حالت آماده‌باش کامل هستند و هواپیماهای سوخت‌رسانی هوایی بیشتری برای پشتیبانی از آنها به خاورمیانه نزدیک‌تر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/alonews/137334" target="_blank">📅 00:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137333">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوری/انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/alonews/137333" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137332">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bd99063.mp4?token=vMXSxnmJ8MriR33WclsGAr0JZmb5Ff1D2lv91ZQJ3BqvPLKqVTkSeb_ZaUXPDYx4hnWVaOX1_aT7UluzOdQU-Mc7E2rTW7lQ-EHVwwfTDNECCxgdwBicrrbMdB-B_rbQvUdqH2aPLe2Me5drXGNfE0F5G6E4RHMQygqUPhZ847ZfgYfKNXeMsnl6sFtR2RAUmNNQViRft6NAAhJ58gAXyxY8_g050TNSzTL3ZRLK_pLv8Wm7cSFt1rrUuhDayMkGu38Q0yq3vwwomSfEmaKEqDViplZC728bbArbBl6ie0EFgeoI3Gh-5-cVT4GGhwEIdXhPSBg4eTm7thgaxadhZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bd99063.mp4?token=vMXSxnmJ8MriR33WclsGAr0JZmb5Ff1D2lv91ZQJ3BqvPLKqVTkSeb_ZaUXPDYx4hnWVaOX1_aT7UluzOdQU-Mc7E2rTW7lQ-EHVwwfTDNECCxgdwBicrrbMdB-B_rbQvUdqH2aPLe2Me5drXGNfE0F5G6E4RHMQygqUPhZ847ZfgYfKNXeMsnl6sFtR2RAUmNNQViRft6NAAhJ58gAXyxY8_g050TNSzTL3ZRLK_pLv8Wm7cSFt1rrUuhDayMkGu38Q0yq3vwwomSfEmaKEqDViplZC728bbArbBl6ie0EFgeoI3Gh-5-cVT4GGhwEIdXhPSBg4eTm7thgaxadhZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی؛ تحلیلگر اینترنشنال :
🔴
تا جایی که من آمار دارم تعداد جاویدنام ها ۳۲۲۲ نفر هست. اگه آمار بیشتر هم باشه اسمی ازشون نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/alonews/137332" target="_blank">📅 00:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137331">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
خبرفوری/جنگنده‌های F22 آمریکا به عربستان رسیدن</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/137331" target="_blank">📅 23:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137328">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34fd806b7.mp4?token=OUSTERarqDk0hG8W4421y9kGdAKnN7aknSyMJYwun82jhn9EaA44hWMhytbmK6qe3ChARjvECEjMPQFjzWp5Ro0SVHcd2IvhYuCYCA2qXNyU3bP8Ew-Lv_nMvnPDOgZ7Bem3unxqjZLo2XSs5qYk_2frX7rrJPXMIhrtzMxdtOVtoXDrdAmlesdKjUX4VG9JOAEx3UCkvv5NFhrTABGtzeUbwH4NVvLJsNHhfgZIa8Cn00Rmhf3XivzxWfDn2EoVCTMA7KO-oz6k5YmCrzJh2PZBH_goiE-2BpWYvRda9n3_yGPar5fOBMWIPAnKj81ILoAxU4zRnGjhTMexJ4bcVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34fd806b7.mp4?token=OUSTERarqDk0hG8W4421y9kGdAKnN7aknSyMJYwun82jhn9EaA44hWMhytbmK6qe3ChARjvECEjMPQFjzWp5Ro0SVHcd2IvhYuCYCA2qXNyU3bP8Ew-Lv_nMvnPDOgZ7Bem3unxqjZLo2XSs5qYk_2frX7rrJPXMIhrtzMxdtOVtoXDrdAmlesdKjUX4VG9JOAEx3UCkvv5NFhrTABGtzeUbwH4NVvLJsNHhfgZIa8Cn00Rmhf3XivzxWfDn2EoVCTMA7KO-oz6k5YmCrzJh2PZBH_goiE-2BpWYvRda9n3_yGPar5fOBMWIPAnKj81ILoAxU4zRnGjhTMexJ4bcVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران گفت: اگر من رئیس‌جمهور نبودم، اسرائیلی وجود نداشت.
🔴
ایران، به شکل شوکه‌کننده‌ای، شروع کرد به شلیک کردن به همه در سراسر خاورمیانه.
اگر آن‌ها یک سلاح هسته‌ای داشتند، از آن استفاده می‌کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/alonews/137328" target="_blank">📅 23:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137327">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ظهر امروز نفتکش عربستانی NCC MASA مورد حمله حوثی‌ها قرار گرفته بود.
🔴
خبرگزاری دولتی عربستان سعودی اعلام کرد اسیب وارده به این نفتکش جزئی بوده و آن به ادامه مسیر خود ادامه داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/alonews/137327" target="_blank">📅 23:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137326">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
خبرنگار: شما می‌گویید که با ایران مذاکره می‌کنید. چه کسانی در این قضیه دخیل هستند؟ ویتکاف؟
🔴
ترامپ: تقریباً همه. جی‌دی، مارکو، خیلی از افراد مشغول گفت‌وگو هستند. این موضوع خیلی مهمی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/137326" target="_blank">📅 23:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137325">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_hDO-vWutDEOx2hCi3HqYIs3sBbBo-JHWI1R4MAqwtyKmuTArLBs3xIqefAJKmrEZ_Im6-P8XHpTkuJgQRRSWLIrIKjDpu4rdUg9HOINLvm8UkdoCw6rKXoIr3zUMIWfn18WPtIFUJlXs4nUTQ1t3CD0CDSnFvjh1g4IhjUhd_zDHbTEVlf27qn9p-7gml6RgWXMxA2w4efsT4TfXu_KOegyKRv3zmmBFUUwmCTny73YbcLD3NPo7he8_4hnRodPOlRxNzIDCgUTg0iCtqNI9NduwJb5ngqepZXvMCjKRP2CJqqKNO8bDiKoORTS86r0XLvJtn1ek6etaFvUiCgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون بندر الحدیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/137325" target="_blank">📅 23:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137324">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ : ایران، باورنکردنیه، شروع کرد به شلیک کردن به همه‌جای خاورمیانه.
🔴
اگه سلاح هسته‌ای داشت، حتما ازش استفاده میکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/alonews/137324" target="_blank">📅 23:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137323">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea64c7c35f.mp4?token=fu9WV0lpyqSuhX7shlmY2TPuMlyjqSJd3ORf5_xQnLhZ5FoATdMWBgv4xkgVg8reuxfqiqT7wJTNHxIaPWsOZ4hRN5ZXPA0xyMznu02vCO8bRMOAUZLJT3qTJdWnzHughN7pXQejM5XIo4PX5XF1gPzsWAZbXYT356U19rj4JOXQgU3p8tJuuPk8I36dQejxCQsGbD-efsihnbRgFVVi57BilrWnrEHHWqLIFrCoWF-HHAlvh35HhIN8oMwUHaZqqk6phY9JcLzCZzo_tI60MPpQncQKlDfmyDCb1Al2crV1XrJYfroVIGaQG0WY1wNr-XsSelr3r9bF9BQVP8XRFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea64c7c35f.mp4?token=fu9WV0lpyqSuhX7shlmY2TPuMlyjqSJd3ORf5_xQnLhZ5FoATdMWBgv4xkgVg8reuxfqiqT7wJTNHxIaPWsOZ4hRN5ZXPA0xyMznu02vCO8bRMOAUZLJT3qTJdWnzHughN7pXQejM5XIo4PX5XF1gPzsWAZbXYT356U19rj4JOXQgU3p8tJuuPk8I36dQejxCQsGbD-efsihnbRgFVVi57BilrWnrEHHWqLIFrCoWF-HHAlvh35HhIN8oMwUHaZqqk6phY9JcLzCZzo_tI60MPpQncQKlDfmyDCb1Al2crV1XrJYfroVIGaQG0WY1wNr-XsSelr3r9bF9BQVP8XRFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : باراک حسین اوباما خبرنگاران را تحت پیگرد قرار داد، اما هیچ‌کس چیزی درباره‌اش نگفت.
🔴
وقتی اوباما این کار را می‌کند، اشکالی ندارد؛ اما وقتی من این کار را می‌کنم، می‌گویند اشکال دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/137323" target="_blank">📅 23:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137322">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
گزارشگر: چه زمانی ایران تسلیم خواهد شد و واقعاً پای میز مذاکره خواهد آمد؟
🔴
ترامپ: شاید آن‌ها تسلیم شوند، یا شاید فقط به یک غار بروند و مخفی شوند.
🔴
آن‌ها غارهای بسیار عمیقی دارند که می‌توانند در آنجا پنهان شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/137322" target="_blank">📅 23:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137321">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رویترز: چندین انفجار در مناطق الحدیده در غرب یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/137321" target="_blank">📅 23:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137320">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری / حملات هوایی نیروی هوایی سلطنتی عربستان سعودی علیه بندر حدیده، در یمن که تحت کنترل جنبش انصارالله قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/137320" target="_blank">📅 23:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137319">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ : وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند.
🔴
اما دو روز بعد، آن‌ها گفتند: "وای، این فوق‌العاده است.
🔴
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند. بازسازی ایران ۲۵ سال طول خواهد کشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/137319" target="_blank">📅 23:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137318">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQPTuQ98b3WpOJMUkFqQVywYtduy8xCFKStgKTKM1LfV4U6v0FlQF337HCbG0VCvyYKtaOCdniR8i9pQeqhv3l3t5kPPVjc0Iwexwr8PPp3FPJhTCBL3AjklFA_YqG-B20arrH3OKR_rD5uJRoutcWIDa76yOWlf8s7Pg85RRI_xtvITmixyFCVE3lhkLXinCrygCc67xTwDs77Qr8vBbfIPPpXMHO2S9E1XyLhHjxLNhBvyt7dNuSpxB57SIgvv9yTJNSc_fu3fLCFhFjjiL7N81UOsTZf_uLiJLXTxxVamIxVVGFYtfHloKlKuR1jObOoggz25QgmB-myRL4-_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون کاهش قیمت تتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/137318" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137317">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ: هنوز درباره اجرای حملات بزرگ آمریکا علیه ایران تصمیمی اتخاذ نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/137317" target="_blank">📅 23:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137316">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ :  من صاحب مسابقات "دختر شایسته جهان" بودم، و همیشه نماینده ونزوئلا در این مسابقات عملکرد بسیار خوبی داشت.
🔴
بنابراین، من اطلاعاتی در مورد این کشور دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/137316" target="_blank">📅 23:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137315">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5decfc4f.mp4?token=hApwYK4TTdDaa5Kz2hcdXQCeCCyNldDePnAkaGmNNJkQv9iuJppzRzzVFQTaCGWfkvo5iX_Gk1JN5TPkK9zZ3-c8-WL-CM8ASw-XnJRBL61O4Cf8Z68kbLo3QTN1H9UvKZrFKWeluKR8NAzkHAkyRhNnpfHb4liTL8Enh25j4tnMFEB7nNWcQ8f8XGYYu6JeY5CvXXtooHzyRDv4KSdnBMjgfP_aFIJrOiK6S49ex_rrHJy2DoU4fy14NgWlxsGydC7RI3hWSQD5JkuqapJyw-fZFJiYtao_qqXEe5OGRuu_raoirvHWKstDlGsEL-nEMGxhStwD-Zy-7q6VfNG37w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5decfc4f.mp4?token=hApwYK4TTdDaa5Kz2hcdXQCeCCyNldDePnAkaGmNNJkQv9iuJppzRzzVFQTaCGWfkvo5iX_Gk1JN5TPkK9zZ3-c8-WL-CM8ASw-XnJRBL61O4Cf8Z68kbLo3QTN1H9UvKZrFKWeluKR8NAzkHAkyRhNnpfHb4liTL8Enh25j4tnMFEB7nNWcQ8f8XGYYu6JeY5CvXXtooHzyRDv4KSdnBMjgfP_aFIJrOiK6S49ex_rrHJy2DoU4fy14NgWlxsGydC7RI3hWSQD5JkuqapJyw-fZFJiYtao_qqXEe5OGRuu_raoirvHWKstDlGsEL-nEMGxhStwD-Zy-7q6VfNG37w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ونزوئلا: ونزوئلا هنوز برای برگزاری انتخابات آماده نیست.
🔴
خانم دلسی کار بسیار خوبی انجام داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/137315" target="_blank">📅 23:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137314">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما در حال حاضر با آنها در گفتگو هستیم. به نظر من، با گذشت روزها، آنها جدی‌تر و جدی‌تر می‌شوند.
🔴
من معتقدم که توافق، راه هوشمندانه‌تری است، اما کاری که ما انجام می‌دهیم، راه آسان‌تری است. ما آماده ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/137314" target="_blank">📅 23:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137313">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
خبرنگار: وزیر جنگ گفت که چین و روسیه از ایران حمایت می‌کنند.
🔴
ترامپ: هم شی و هم پوتین به من گفتند که در این کار مشارکت نخواهند کرد.
🔴
ترامپ: من به آنها اعتماد دارم. فکر نمیکنم که آنها بخواهند من ناامید شوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/137313" target="_blank">📅 23:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137312">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: همین الان که داریم حرف میزنیم داریم با ایرانیا مذاکره هم میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/137312" target="_blank">📅 23:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137311">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ درباره توافق هسته‌ای با عربستان سعودی: در یک مقطعی، عربستان سعودی به پیمان ابراهیم خواهد پیوست و برنامه هسته‌ای غیرنظامی خود را دنبال خواهد کرد. هیچ گونه غنی‌سازی انجام نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/137311" target="_blank">📅 23:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137310">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری / ترامپ: مهمات برای یک حمله بزرگ علیه ایران آماده است. ایرانی‌ها باید این موضوع را جدی‌تر بگیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/137310" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137309">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ درباره ایران: «آنها میخواهند توافق کنند. گاهی می‌گویند نمی‌خواهند توافق کنند
🔴
دو راه وجود دارد: یا می.توانیم به آن‌ها حمله کنیم، یا می‌توانیم با آنها مذاکره کنیم، که همین الان هم داریم انجامش می‌دهیم.
🔴
همین الان که داریم حرف می‌زنیم، داریم با آنها صحبت می‌کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/137309" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137308">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=nvnFM8VX9y-JEvePwAWV_sV_UpcO2gi1tSQC4YOGliHCsz0WjosV3qF3ILIS4JUtGq71l-4UIxnkZeU35BGEV_O8s8rNaJPpMaJR4L-RqwQ6CXXFgHCpo-IWc82JhDHdENr0V8rRkxjL_OfkOfH56p8vyh3h7nw6q7Yu8WEyhL8Q1zN4KIrrxQu1KaO3heuIk5t0bQDEyTRM-_7eCggAPpYJqd8iBri3W5bZA22KX8oVKaqeenUXbbK_LROF6xBWCvUGaYfUQw5UafiCMeTZR6kR2fEMEx6-lsQ3tVx5GzOx2sJXE0gvuTrrfOCO0HzvczU5thYDUFmTbZ7ouRWqmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=nvnFM8VX9y-JEvePwAWV_sV_UpcO2gi1tSQC4YOGliHCsz0WjosV3qF3ILIS4JUtGq71l-4UIxnkZeU35BGEV_O8s8rNaJPpMaJR4L-RqwQ6CXXFgHCpo-IWc82JhDHdENr0V8rRkxjL_OfkOfH56p8vyh3h7nw6q7Yu8WEyhL8Q1zN4KIrrxQu1KaO3heuIk5t0bQDEyTRM-_7eCggAPpYJqd8iBri3W5bZA22KX8oVKaqeenUXbbK_LROF6xBWCvUGaYfUQw5UafiCMeTZR6kR2fEMEx6-lsQ3tVx5GzOx2sJXE0gvuTrrfOCO0HzvczU5thYDUFmTbZ7ouRWqmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: شما دارید درباره‌ی منفجر کردن نیروگاه‌های غیرنظامی و پل‌ها صحبت می‌کنید. بسیاری از جهان متمدن این را یک جنایت جنگی می‌دانند. نظر شما چیست؟
🔴
ترامپ: من به آن سؤال پاسخ نمی‌دهم. شما از کدام رسانه هستید؟
🔴
خبرنگار: نیویورک تایمز.
🔴
ترامپ: حدس زدم. همان نیویورک تایمزِ ورشکست
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/137308" target="_blank">📅 23:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137307">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهوری آمریکا جمعه دوم مرداد به چین و روسیه درباره فروش سلاح به ایران هشدار داد و گفت که او اظهارات شی جین ‌پینگ و ولادیمیر پوتین مبنی بر اینکه تاکنون چنین اقدامی انجام نداده‌اند را باور دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/137307" target="_blank">📅 23:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137306">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ : اگه عربستان توافق هسته‌ای می‌خواد، باید به توافق ابراهیم هم بپیونده
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/137306" target="_blank">📅 23:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137305">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ae6c6862.mp4?token=WwW70Cp4eVGB1CwKenWyrOM5d6td7ajyoIJ5wggTV_rj7ntSRn5xm_36LJ4bPaotxKhfj2vPwqkfGxlWVMS1AWNK8owPLg-spfbNoVAemeAvAM1GSZHDx2vJU7nbB-uFjIy2ymeGPluSzOSJQG8X2ITi8uwucuWwZi-xGK2JUUEQFoWNs_3r9m0pGVEEDnDlo3Y3gftCOIQ-2pSJ_ZTfhH6D9l8vyeSEKCDVmu6CEX9mHO-KQ-K4f3Kl-WhDCX5PQ231qs4khUdPRFm7gT4cjaRdTUj-oj7_I3qo3uhrOHrMb_NKnnPvp2AiXTFD5H4sqEvQELaY11S7SgRE-UMU1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ae6c6862.mp4?token=WwW70Cp4eVGB1CwKenWyrOM5d6td7ajyoIJ5wggTV_rj7ntSRn5xm_36LJ4bPaotxKhfj2vPwqkfGxlWVMS1AWNK8owPLg-spfbNoVAemeAvAM1GSZHDx2vJU7nbB-uFjIy2ymeGPluSzOSJQG8X2ITi8uwucuWwZi-xGK2JUUEQFoWNs_3r9m0pGVEEDnDlo3Y3gftCOIQ-2pSJ_ZTfhH6D9l8vyeSEKCDVmu6CEX9mHO-KQ-K4f3Kl-WhDCX5PQ231qs4khUdPRFm7gT4cjaRdTUj-oj7_I3qo3uhrOHrMb_NKnnPvp2AiXTFD5H4sqEvQELaY11S7SgRE-UMU1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صلاح یکتا که کار آچر کشی و فیزیوتراپی در ایران و دبی انجام میداد رو گرفتن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/137305" target="_blank">📅 22:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137304">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
فارس:  آمریکا با موشک، یه تانکر حامل گاز مایع رو مورد حمله قرار داد، چون به اشتباه تصور میکرد که این تانکر حامل گاز ایرانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/137304" target="_blank">📅 22:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137303">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
روایت «المیادین» از فشار ترامپ به کردستان عراق برای جنگ علیه ایران
🔴
خبرنگار المیادین که در سلیمانیه حضور دارد،‌ خبر داد واشنگتن بر رهبران منطقه کردستان عراق فشار می‌آورد تا مستقیماً وارد جنگ علیه جمهوری اسلامی ایران شوند.
🔴
المیادین همچنین گزارش داد که دولت آمریکا به مسئولان کردستان عراق هشدار داده اگر با ایران وارد جنگ نشوند، نوع حکومت کنونی آنان (خودمختاری) را لغو کرده و تغییر خواهد داد.
🔴
ایران هم به سران کردستان درباره آغاز چنین جنگی هشدار داده و تأکید کرده اربیل باید عواقب حمایت از تجزیه‌طلبان ضد ایرانی را مد نظر قرار دهد.
🔴
خبرنگار المیادین همچنین خبر داد، ایران به سران کردستان هشدار داده هر گونه دست داشتن در جنگ، با پاسخ مستقیم ایران و حتی عملیات زمینی در این منطقه مواجه خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/137303" target="_blank">📅 22:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137302">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
بلومبرگ: ترامپ به طور فزاینده‌ای از روند جنگ ناامید شده و می‌خواهد هزینه آن را برای ایران افزایش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/137302" target="_blank">📅 22:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137301">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
طبق گزارشات سفارت هلند هم در تهران تخلیه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/137301" target="_blank">📅 22:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137300">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
هشدار سفارتخانه‌های آمریکا در عراق، اردن و اسرائیل به شهروندان خود: در سفر به منطقه یا عبور از آن تجدید نظر کنید
🔴
برای لغو پرواز‌ها و بسته شدن حریم هوایی آمادگی داشته باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/137300" target="_blank">📅 22:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137299">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
عراقچی به وزیر خارجه پاکستان:
حملات آمریکا به زیرساخت‌های ایران را محکوم می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/137299" target="_blank">📅 22:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137298">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Djz-TYryP-GjkQ5ulzBM3f_BTEd96ADgBWwyI8b2HcX_jSpBk91prdc9MFzD4MIkbH6mNdNJboE_nGYQIDwaKA1X9eG_VU3kyaG4QPyDUJGCeD3FA5Y0jKgtUjei3MmB82jillNSrEXceMxb_8TQ8kuGPp8q9T2GLpCfxJqiunI-Kb3LqVbH0z9AbE9NlQ4rUEdMapQjWBubNtiKXrx0gfTKCqJ1sMaDvxaqN1OdWdGQpJFL4flQVntNqDPG1JentaZJGAXqsOPLiR4GuKdMGLzcVHRRbkqtlYqIwMpO3nnPKC5snwIQza94yjUPXKOGxgHlqyKPiUp53hGCUg38EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از نتایج اصابت موشک FP-5 به کارخانه "اویتک
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/137298" target="_blank">📅 22:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137297">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
بلومبرگ به نقل از منابع:
ترامپ به طور فزاینده‌ای از روند جنگ ناامید شده و می‌خواهد هزینه آن را برای ایران افزایش دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/137297" target="_blank">📅 22:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137296">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3dORvbZ-UPqHP_hsGc5kk4lDWVW-8vcI9dtECuebvYS3S9HkpifuD8xIPDssaSv_XAe3g7RDTQ_aWOnZOhXDap1CHeuOGrAQeCXpt63TuBH1KlhoHSSK3zAvuGCOmnL42e3gZ8quqU83t5Mfb8kDcryVPNir87TKmvI0JgS1_1zSLJuf9VVX_zPhXdujHh5ZHE73ie2X8ZPGMKz0UlsYay9z6AcvcyVrRjKRhXyceomrgSw1HSI7SS1lxKCLFz9BlirAXAPQDSyR1Pv-e3VZw3Dcxk6-X5mtRjv6o0ZndkwM2umLRLdVa6BCL1dju_6NnfSiLXsW7V8PU-ktjShpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقشه جدید برای قتل ترامپ/ کانال ۱۴ اسرائیل فاش کرد:
🔴
بر اساس یک گزارش جدید، چند تن از مشاوران ارشد رئیس‌جمهور هشدارهای اطلاعاتی مبنی بر تلاش ایران برای هدف قرار دادن آن‌ها دریافت کرده‌اند.
🔴
در نتیجه، به برخی از آن‌ها دستور داده شده که از خدمات تاکسی‌های اینترنتی و خودروهای کرایه‌ای به دلیل نگرانی از یک حمله برنامه‌ریزی‌شده استفاده نکنند.
🔴
هم‌زمان، خود ترامپ نیز گزارش‌های اطلاعاتی از سوی اسرائیل دریافت کرده که نشان می‌دهد تهران در حال بررسی طرح جدیدی برای هدف قرار دادن اوست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/137296" target="_blank">📅 22:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137295">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER_hzgUphm-tXubkRLOK8ZVxmRot4EayGTK0tO6Skkqz8u43fJFG6In1Yp3L8PKYz2mI8zB32pwbDjy2eWJH7PGfiwLzc0heX0AhSVP5NjTg3KvCVAi38Zgace8koC4bUPA7ccJ5ZLypOPu5ZAmKHHf4ueP2MGTM2t7h3Qw7_PwJLqimTXT4y7i8oo5UwMDZkHqglAMoW2SNovo9k190WbRVNiUHOY-7RZp-Bd7uFaeDJdlY1uLkAVsTIvIAlkGPN425IUsJBgsLREAlE4hLp2F3dCNjQ00kKDHMvv18mkkShrSiMkxeLRloszcN3cXIrRuyB3Mv8ORdfs-vo5kogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: مسیر دیپلماتیک بین تهران و واشنگتن ممکن است دشوار و پیچیده باشد، اما علیرغم لفاظی‌ها در مورد تشدید درگیری نظامی، دستیابی به موفقیت در هر لحظه قابل انتظار است و بعید نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/137295" target="_blank">📅 22:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137294">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c80ce599.mp4?token=c7F6_O8_OlMcunwJ0MmDTi_R_VUD8z8pnbLsPYFQ08Ojg5s8d0skQyP9cnUrz2mddmjBUaGqI3UC7TtDCOLl2RL6PAoL5kbsG_Jqu0PUY3vBJ8c-dC72hEFuqkNhF9EtLdbZzXotSouN-9DNOY4g_halosZhPdhsBl3BXySRvRHLQP58-4MEvlQ8JuWwndu7DhCN0cr5RxO6KjcBr77Ugd8KN7GJ0fRvtfKStpqw8DrHGN3-sa15xxf1jd0w2JwKkmBD0FsYvRt01nrpP6UnOmC9xODMsnF5mlPLI-UiKCmjlAnwFxtyBIgUsYSN9LB3xWXD_F7tiEWG6hTTD3IJqGGgpP1g57h5Cpzr7DuW2ynUfuQ1w8ZhZY5C3ud9Ynf1InbxKE0VdCAezE3Mj9FOBe0Qc7q3pvk0VQspqfabdHjVW9JJGrkmH-9eGqlG-enUP5iyoD9ecvd9K4XMcr4DDk8Xa-_SUe9a6pegyoJohurI6IaNHfBDwmQNkQUv5OyeF5MT_7SVKORFnwrQ06lf5i_3qCQm3GEMqQSY4Pzj8YEDgptD-jIIyoXdpr_iAyS8Fz8jBeANNXtT-NCT3Y9vGEzbRsGJ_tULc8Eltkwy6izwvNyi2t0MmA7ynnkRs31pwnoB21Fd8akCiF0mmdrwljse3-C9iLVKEFXR8bmHRRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c80ce599.mp4?token=c7F6_O8_OlMcunwJ0MmDTi_R_VUD8z8pnbLsPYFQ08Ojg5s8d0skQyP9cnUrz2mddmjBUaGqI3UC7TtDCOLl2RL6PAoL5kbsG_Jqu0PUY3vBJ8c-dC72hEFuqkNhF9EtLdbZzXotSouN-9DNOY4g_halosZhPdhsBl3BXySRvRHLQP58-4MEvlQ8JuWwndu7DhCN0cr5RxO6KjcBr77Ugd8KN7GJ0fRvtfKStpqw8DrHGN3-sa15xxf1jd0w2JwKkmBD0FsYvRt01nrpP6UnOmC9xODMsnF5mlPLI-UiKCmjlAnwFxtyBIgUsYSN9LB3xWXD_F7tiEWG6hTTD3IJqGGgpP1g57h5Cpzr7DuW2ynUfuQ1w8ZhZY5C3ud9Ynf1InbxKE0VdCAezE3Mj9FOBe0Qc7q3pvk0VQspqfabdHjVW9JJGrkmH-9eGqlG-enUP5iyoD9ecvd9K4XMcr4DDk8Xa-_SUe9a6pegyoJohurI6IaNHfBDwmQNkQUv5OyeF5MT_7SVKORFnwrQ06lf5i_3qCQm3GEMqQSY4Pzj8YEDgptD-jIIyoXdpr_iAyS8Fz8jBeANNXtT-NCT3Y9vGEzbRsGJ_tULc8Eltkwy6izwvNyi2t0MmA7ynnkRs31pwnoB21Fd8akCiF0mmdrwljse3-C9iLVKEFXR8bmHRRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
درود بر روانشاد
#نوید_افکاری
🔴
#رشید_مظاهری
به سلامت باد
🤔
ننگ ابدی بر عليرضا دبیر و تمامی حرام زاده های طرفدار حکومت جمهوری اسلامی
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/137294" target="_blank">📅 22:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137293">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نیویورک تایمز: نهادهای اطلاعاتی آمریکا معتقدند که رهبر جدید جمهوری اسلامی، نسبت به پدر و رهبر پیشین خود، علاقه و تمایل بسیار بیشتری به دنبال کردن برنامه دستیابی به سلاح هسته‌ای دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/137293" target="_blank">📅 22:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137292">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217970b0cb.mp4?token=iSLhazXaXjPsXnWpEDszd2u_-Sh2_58c5gI5_b0An0oygo_5uRx5RvaApVkk477bw7OuJw7wMAUtC6xoytBAUjACwOrseYwbGieCFfsnFH8r7WWqCFCqcaMFUhx-tQWWy66a_zDIkriFvG-rO8T4X7N0T1YKoX3OiKHU5cJfG0m94qz_2Vc07DEFF5pZ0T_uCMB7VV3Qt7M2Qr9okqxOzFzRAcprzpUSeDCaF3LA9g1EEiD0IZJYihldsAF66pG9aiYZ84dsCZfJ1ha_HWjIcnN-fqRgYECKvSGW08waaC2L_duqkuIujeGJy9CIKSjpKxzeeuqP4_xsIBGZW0JEpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217970b0cb.mp4?token=iSLhazXaXjPsXnWpEDszd2u_-Sh2_58c5gI5_b0An0oygo_5uRx5RvaApVkk477bw7OuJw7wMAUtC6xoytBAUjACwOrseYwbGieCFfsnFH8r7WWqCFCqcaMFUhx-tQWWy66a_zDIkriFvG-rO8T4X7N0T1YKoX3OiKHU5cJfG0m94qz_2Vc07DEFF5pZ0T_uCMB7VV3Qt7M2Qr9okqxOzFzRAcprzpUSeDCaF3LA9g1EEiD0IZJYihldsAF66pG9aiYZ84dsCZfJ1ha_HWjIcnN-fqRgYECKvSGW08waaC2L_duqkuIujeGJy9CIKSjpKxzeeuqP4_xsIBGZW0JEpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک زن عصرحجری معترض به توافقنانه: مردم اگه گرسنه هستن یونجه بخورن، ما انتقام میخوایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/137292" target="_blank">📅 22:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137291">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
المیادین: واشنگتن از رهبران کردستان عراق خواسته در جنگ علیه ایران وارد شوند و ایران هم به اربیل درباره پیامدهای هرگونه همراهی با این جنگ هشدار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/137291" target="_blank">📅 22:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137290">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
پدافند کویت مجدد فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/137290" target="_blank">📅 22:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137289">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ایرنا : آمریکا امروز بعدازظهر دو موشک به سمت یه نفتکش گاز مایع که از خلیج عمان نزدیک منطقه می‌شد، شلیک کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/137289" target="_blank">📅 22:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137288">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409d06d604.mp4?token=u1J4X5z2lkm02BdYZM1YP7MwlpAnIdL1UL23PqJbDQ2x61r7DkSRWoVqasOooOp7kj0cbBYEjjyHciEVoFEbHNMXptnD3vvhkjlJy1EfjVEewZtuOApyQN1AUmiHrtYxdxBv7k_QQba-cjtXiz-uXzOsLuOyUwBAwerk2ku4C-nGwmsFfrvF4SmqhsOEuxg8S37jZTX8xqCaq7n_wR8z6lEzQfGVtlFZQNdk5ginoAgJX3dgYHm2pH6buX0efll-3HRcFlX3aSbuZAob3NjV6dpxYMr77cWuyUXE-Tz8H4bIIakcnSN0BNU3TPFDpdLJUhDrFErRG0jcOPslAYQKxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409d06d604.mp4?token=u1J4X5z2lkm02BdYZM1YP7MwlpAnIdL1UL23PqJbDQ2x61r7DkSRWoVqasOooOp7kj0cbBYEjjyHciEVoFEbHNMXptnD3vvhkjlJy1EfjVEewZtuOApyQN1AUmiHrtYxdxBv7k_QQba-cjtXiz-uXzOsLuOyUwBAwerk2ku4C-nGwmsFfrvF4SmqhsOEuxg8S37jZTX8xqCaq7n_wR8z6lEzQfGVtlFZQNdk5ginoAgJX3dgYHm2pH6buX0efll-3HRcFlX3aSbuZAob3NjV6dpxYMr77cWuyUXE-Tz8H4bIIakcnSN0BNU3TPFDpdLJUhDrFErRG0jcOPslAYQKxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راز شلوغی کافه‌های شمال تهران
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/137288" target="_blank">📅 22:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137287">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
چندین انفجار شمال کویت را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/137287" target="_blank">📅 22:06 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
