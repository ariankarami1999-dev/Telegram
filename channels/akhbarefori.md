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
<img src="https://cdn4.telesco.pe/file/eBh4UXPQ2xY0-9vmDHzCdL7TwRWkS5iQfxG5VoVWK3n2Y7ziC0gol_IP-PB9mXyZ6NbdUuwKVOuVhExU6PcnbkvKXSrnqrrUvWgAFE6LycpjUwSu3lc9JYKswvW4etKcH5my_meNJ6AynkIbJGK5EVxWYZYD0-A2Kz2FurihEgcAKNlbMu_5B-uBELPQshtKVXxdcMDAumEsM58_DZ2bnwxqBgxUfXYOFJr2R5W8QJ70TWKD9YU_p7-OO93x_ifiMa-JeJfTelwMAgX6KwgmJUn2m8ACT4YJMLtoU3pIrzA8de3ocm3BbMulq6BfU5Dk116plUpcit6ajCmCGZp8JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.48M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 08:43:32</div>
<hr>

<div class="tg-post" id="msg-668280">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
تداوم انفجارهای شدید در بحرین
🔹
منابع خبری از شنیده شدن مجدد صداهای انفجارهای شدید در بحرین خبر دادند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/akhbarefori/668280" target="_blank">📅 08:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668279">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
المیادین: استانداری کربلا حضور ۷ میلیون شرکت‌کننده در مراسم تشییع پیکر رهبر شهید انقلاب را ثبت کرد #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/668279" target="_blank">📅 08:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668278">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ae4eb2dfe.mp4?token=gQa8el3GqocQDKGMRyBGTJ3pkVYmw2_HkMClvuUDOaMy8nwBz41eOi6I9cAJDro0oZPfTGQ1gLVvqpfZfrfA6ePngjLT-RN4lOD9e_28qnq4DFQV9mUjsqxhnH0zE9WTljoreYHNIPI1GmEcvgQYiORJsaA3Ykeu_hNUvkOQIWS5basYmdzfT3pFN0OtGPOc2gLt6Fzxy_kkN7PkGven7nz7u18CxRuPwRhvzqfqKgMsYXkEmJWBKiufwaRraa2o-A3WqPStXY8hGQRJHBVwOqV4FeHJfPpjDD-bhj4mboxik3zUfCEFB8hkj25lDmRHUGXBMcLbcAvDbJaMyUI3N57VBjCAI1yubMs73m3epImiWRE670ZQaywzXFbeeO2FKIv2C4r2AFPCQyx1vy3HLbZWXeyc-HN4J0K0FuwizvSBPSDwM35GElzVEL-DxAY1hKdZi4wSD7UB88UJdd6sUmA4Z_Z6Mb7iMcrj8vAL9F9lP1aO35Q9xLuhaFWE0FuFkrwLJVGKALz3MvyKT2xOkwJShIXKHnLs11yFGsmGAEUUwzB1JHGff1WTzN-3-CqPjcBBikTfm786d_F6jBtL3l10qj2YQ1FbbyiBgjLhfjSJ3oP3MIla7zZuSZoTMNAB-B6OHCq4WCEFW8KSA2hnkgzQp4IEArgo66hVkD9r8kE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ae4eb2dfe.mp4?token=gQa8el3GqocQDKGMRyBGTJ3pkVYmw2_HkMClvuUDOaMy8nwBz41eOi6I9cAJDro0oZPfTGQ1gLVvqpfZfrfA6ePngjLT-RN4lOD9e_28qnq4DFQV9mUjsqxhnH0zE9WTljoreYHNIPI1GmEcvgQYiORJsaA3Ykeu_hNUvkOQIWS5basYmdzfT3pFN0OtGPOc2gLt6Fzxy_kkN7PkGven7nz7u18CxRuPwRhvzqfqKgMsYXkEmJWBKiufwaRraa2o-A3WqPStXY8hGQRJHBVwOqV4FeHJfPpjDD-bhj4mboxik3zUfCEFB8hkj25lDmRHUGXBMcLbcAvDbJaMyUI3N57VBjCAI1yubMs73m3epImiWRE670ZQaywzXFbeeO2FKIv2C4r2AFPCQyx1vy3HLbZWXeyc-HN4J0K0FuwizvSBPSDwM35GElzVEL-DxAY1hKdZi4wSD7UB88UJdd6sUmA4Z_Z6Mb7iMcrj8vAL9F9lP1aO35Q9xLuhaFWE0FuFkrwLJVGKALz3MvyKT2xOkwJShIXKHnLs11yFGsmGAEUUwzB1JHGff1WTzN-3-CqPjcBBikTfm786d_F6jBtL3l10qj2YQ1FbbyiBgjLhfjSJ3oP3MIla7zZuSZoTMNAB-B6OHCq4WCEFW8KSA2hnkgzQp4IEArgo66hVkD9r8kE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم اکنون؛ خیابان‌های نجف اشرف مملو از تشییع‌کنندگان است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/akhbarefori/668278" target="_blank">📅 08:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668277">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
سقوط یک هواپیمای باری با ۵ سرنشین در دریای عمان  ادارۀ فرودگاه‌های پاکستان:
🔹
این هواپیما ساعت ۲۱:۱۸ به وقت اقیانوس آرام از شارجه به کراچی در حرکت بود، که مشکل سیستم ناوبری را گزارش کرد و بلافاصله توسط مرکز کنترل ترافیک هوایی کراچی راهنمایی شد.
🔹
در ساعت…</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/akhbarefori/668277" target="_blank">📅 08:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668276">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
رئیس‌جمهور لبنان برای پیشبرد توافق با اسرائیل به واشنگتن می‌رود
🔹
خبرگزاری رویترز به نقل از یک مقام ناشناس کاخ سفید گزارش داد که جوزف عون، رئیس‌جمهور لبنان، برای ۲۱ جولای(۳۰ تیرماه) به کاخ سفید دعوت شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/668276" target="_blank">📅 08:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668275">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
الحدث: آژیرهای هشدار مجدداً در بحرین به صدا درآمدند
🔹
منابع خبری از شنیده‌شدن صدای چند انفجار در بحرین گزارش می‌دهند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/668275" target="_blank">📅 08:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668274">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfcdfebc55.mp4?token=Uk8qbqwfn-K2kZAH7sAZYUZsEQDMVhV6W9wZtqIyWEI_s8k9cAs1ItIdqu3s9DaqYOABVhE6OF10GgOmatmSRPqyLk8i3nkJUgclN-830kXWI8uGvhjXhvCO7DB17QfXlONHeF4n_0PK1g-FXDFrw7rF0wkDOu7LibQOVy2bxOiow-YAVn5D2QYq0HJtrcDSjEkrLbWseWORfGIpfPkPHDs3-Bw3QyIthj9fhcSZ2hWe9OQplh21YCRevQnXV45upVrGNy5dRp-CdAjR70EKLtp2l9Wt8Nb_pHfHeCN3NgVKXzmDUweqtqZDlE54JiGpoEPBftvAn0Q4-M1vvc5INA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfcdfebc55.mp4?token=Uk8qbqwfn-K2kZAH7sAZYUZsEQDMVhV6W9wZtqIyWEI_s8k9cAs1ItIdqu3s9DaqYOABVhE6OF10GgOmatmSRPqyLk8i3nkJUgclN-830kXWI8uGvhjXhvCO7DB17QfXlONHeF4n_0PK1g-FXDFrw7rF0wkDOu7LibQOVy2bxOiow-YAVn5D2QYq0HJtrcDSjEkrLbWseWORfGIpfPkPHDs3-Bw3QyIthj9fhcSZ2hWe9OQplh21YCRevQnXV45upVrGNy5dRp-CdAjR70EKLtp2l9Wt8Nb_pHfHeCN3NgVKXzmDUweqtqZDlE54JiGpoEPBftvAn0Q4-M1vvc5INA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛
انتظار جمعیت عظیم مردم عراق برای استقبال از پیکر مطهر رهبر شهید انقلاب؛ مسیر تشییع، نجف اشرف
. ۱۴۰۵/۰۴/۱۷
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/668274" target="_blank">📅 08:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668273">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سپاه: حمله به ۸۵ هدف نظامی آمریکا در پاسخ به نقض آتش‌بس  سپاه:
🔹
در پی «نقض آتش‌بس» از سوی آمریکا، نیروهای دریایی و هوافضای سپاه در عملیاتی مشترک، ۸۵ هدف نظامی آمریکا در بندر سلمان، بحرین و کویت را هدف قرار دادند.
🔹
همچنین یک پهپاد MQ-9 آمریکا نیز سرنگون…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/668273" target="_blank">📅 08:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668272">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a11aafb0f2.mp4?token=d7N99i6b_D9R16s3PsR4d2JcUTAZSoShWH2oiA1k9na6Lm172LSYhLPDUd7K-4MRLZ3BgByppOMLER9Vk2RO9fkY6-4lfDE7JtWIgVMJJ_AwmmHsRBHW40djYWmwRwOW3zZuosbE6dAFqFX7EruOeIaseu6rSFaJqY0MZjAUAWOlV34OWlP88Lo5aqntBf15oE_HhUtzupNdLXxMuM3oNpzuZ3sPQFaRKB566JBx8a6ETcBu2A8gwZuu889VI2mYwsrqO9KaXaoLz1Eh6Kj25G2hZ_un6IbyJhJNq9uCjszog9FJG66G1F8RCQYZlqkHkFRjgEK3jIPeIYZfFhJYww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a11aafb0f2.mp4?token=d7N99i6b_D9R16s3PsR4d2JcUTAZSoShWH2oiA1k9na6Lm172LSYhLPDUd7K-4MRLZ3BgByppOMLER9Vk2RO9fkY6-4lfDE7JtWIgVMJJ_AwmmHsRBHW40djYWmwRwOW3zZuosbE6dAFqFX7EruOeIaseu6rSFaJqY0MZjAUAWOlV34OWlP88Lo5aqntBf15oE_HhUtzupNdLXxMuM3oNpzuZ3sPQFaRKB566JBx8a6ETcBu2A8gwZuu889VI2mYwsrqO9KaXaoLz1Eh6Kj25G2hZ_un6IbyJhJNq9uCjszog9FJG66G1F8RCQYZlqkHkFRjgEK3jIPeIYZfFhJYww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد «لبیک یا سید مجتبی» در مراسم تشییع پیکر رهبر شهید انقلاب در نجف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/668272" target="_blank">📅 08:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668271">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
المیادین: استانداری کربلا حضور ۷ میلیون شرکت‌کننده در مراسم تشییع پیکر رهبر شهید انقلاب را ثبت کرد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/668271" target="_blank">📅 08:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668266">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7h31jJyVcLteO6-GA8DCszM2w4OW9I8__oiqBVzi0hqwMJjg7M50EboDC5m1tlTNRGw9fyV81MmB6aEVWL4ukOqkQuB0rH4EVYiZdHtU7CSxrJXhlDQwfawBkwC0WbaflDf7hU02sMuDlpWzbBx8-9-ibI6KmAn8iiCcbzOP2VhNUHB--oABtn1HVWkU78a7kfQxezt_AMEqzD5vCWoZbK_gKP7C6aPlUPzLAYmHvFWW5kJn3SrgP9jx-wnRJlBxMfDHeABQ72RC8hDX48dMmnYVo2wLi-x9ccq9jHQ0oFu7y9bK2q42uOcpWnHYoGBEB_Q-HYp4kBpuyruZ2ouYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GbfmjM9SB-6Sli3GplF-y8LfV0_1Rd6PWV_kooa1BTwtSSA5c-irchxW-kbJJSt1DnMV5RDqcTAJRFHV2ZN_8VIhhn9B_tAKrhTAS5bItzJbvJJUT3JGJ5-6jhWpRV7YNppte-HlB-SfpSHSnW8GdQ3A1BZofwD-BV1TcyXk70s3jlPpW0vTe_-gd4d8xtU-Fsxc6edV34oFQW_ntZ2xgmGBD3TvRin79iFBugb2nZoFv11xUfprcQChURIAtskOD36MT1lpiIGLXADG4VMMbjZd-rGG_dO264OuwYE85rtEBe91abjBZm4mqY-T0qBZ0mIGIH5mUWbZqqLb_gqS0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mQx9uleLrVPNCQ8dc0bNCMmIy5fshCAVCTHDX37t2PZ8VdoZUZLgcMQmpHlvH9cZuGIXUIrljh0Rp8GotU_-IE9p8tRhaASX6HCs95qJ4Tts1vokCDHkWuhh_ueV2EfQApO5wZKkLGNl8Wiu-lD9p2u4D2O2bClVIZiSl9Lk0on0N1frJO-TcORhzYp2GhQnPXW0iTHym-TEKXEflUJ907MNVxptM4GNbp-R5RK-TUMSFALUaVXVUDsix_Gz67gxQ27wDmb5d7OFb_5icUP4k7mJYLHZ9sNm2GRJ19XPNldpwTcRxyf1-vWOvzeEaEDyEiKkXnCCvzMAkyApVV7NuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yj__doB1IpOFOWd6ABQZT80rZtfwyQx9sbmK7OW76UvWx2EUlEqhXIDnhUuPblle_qPooudxBJQ_ndztd3qU1opAh7y7Ojav5Jt2x0Lc5lfum4qZI7RdTTEcnDQyTIrNoXuQZ4X_tkm_aWjW87FywQPaZomqwjEx4_71imGgkb1mf46HXwRTmSaQyhf5eY5m9aTbXFhmAa8AySIhqLUqrUfhGnmZH2hWPrwKiRDU0zSyzYQhhFVC-fqv_1oVKg6g9ZCYb5AxzGbAKOwc9u0x0MLPi_1cDYZBeZLGrLRS3UjHypruQC-bivM0CzTEyBksLcjkuZ175FNvnD8ejGAIGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hIDtTg71gSgl0KqB3n42JZ9ytM51BeQbQgIJbm2BKykU0OciZJhPgizsuiCAy7DPlf_fQbUCX77K2fJQLzljBNa5T-TnOfnSrsrIi9wT_LFDXtZCvBjbW1sxP2piLd34aDNocxMcYeqZXJyFkBFlrNPXNhGGpCznj-ef1ixb7UcqMy8fZdmuiHVYIFLHZ1n2pYXb-BRodZ6fKUVFj3UA3NiFxgt8VkekzMW2DbaWENGHxPixl83r6pKuUi5OSspU0Ri7bDvPXM79BDopaIObiiemBpCNZvxc8ye4BLkjsQfbBSpkZps5-oX6NFv9NG9OfElahhpGSMi_nkGaOnylyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سیل جمعیت عراقی‌ها در تشییع پیکر رهبر شهید امت اسلام، در نجف اشرف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/668266" target="_blank">📅 08:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668264">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DhukctfzmuHUDuBZBnXCri1KvUsnweKXg8UiGxz8KIHGNmIoXjXlzZNpYGzUb6EMyZZtZZyvUcZyZl9t-ZT-PXY55DIPqWzQCKDTvjFyzAru9Q3ASooGjw28te7_AqjYsdDTo9ZwnpWcMwymb9dSkFDu3EkHb76V2OANihVe_MDaqwm96los6dvte1mrt65S0SOkwgfzMIYKzkos3hHaGVsL8S0xHLOasZJBZcyHeCR3_iajH9aAtktcGaTKrAYLmrZU95C4LWQpLfI1TmXsBMlfz2Y9NA7hV6ApyBcNbdpgI2JxD2duaKZH5_FF038bIH65Wvo6GsgK4FvvF2-Rrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ow5Oc9IoMYulEBl32Sa2WZtt-p36WNBLgvBo35AuG8X40E5oeqOIE9BMzReydvnitWlxlgWeEZ4uos8B4cjEuDqKZHV8_I-gs7b8Js1wJallggZr9068Eb5Z_DscXyD3hP-jxqJsEwqt0rlSTox06z5LfWHUImRISYxbBy1bP2HyhEByBTFH2BE15MNLR9rtRxp_fDUHSCMN5YmCB0jMVSr0HELGy5A5AoHph7ddk4nXsgdczBjxpQBBPgxxHdAz1hADwSTQ6n-4PsL29oiNeUUtFWOYhddEwgPLnSQT2QnpLNLKvPdWuDxF_W0LQtvFn16mWeqfbBaWlLijfe6Ekg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور سید عمار حکیم، رهبر جریان حکمت ملی عراق در مراسم تشییع آقای شهید ایران در نجف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/668264" target="_blank">📅 08:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668263">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ff16f06b.mp4?token=acCaLaFHfc5mKkVByt2BTFIe4Wtf0HCDi5KyESIJteHHDVw5YGfAU8e5NZmAlC7w_JQoE-TQW3eW22M5lhz2ybd21wk_QXXNmkpd73whRwsGX3gBnS_08N3nIHfwkjYQPzI2tySrS2wydy6vI8fR5dccgiwz45bMSGZHuFiI8gYhZVrAU-FdnldtjQmcKoprhBJhHrlWVVWPrJag7t_cKjEA9yuXEBmrkOZuGGGgo4zI7asQo_XeiZmDc11t2xsnRsMbfTm96_63HJiwQ_QaS7mbOa1KP5HVfLs6vNCDrorTSv5HQUbPRNfMUpNKJDd-68iZqp_Z8d6VxeNx3pKOVCXZ4uWkDPWeMDQz2h5ppy3pIg5DpbUvKtZAN4ixNw3YxrCLvEnQFizVWeNdfGOIjm5VW_wcqhACdXpun5NWAe1VRxV3l2kqTCjY3FEGBL3Ywg0-SLyNDt9k6whfCsybRye6e-oTJyh6iWbfvUXQ4t1NeYoA6QAnYhuCKQb6rSep2vx_CAvcTQtpCSE7H6ZR_EWtGzUfMlpLeTelNScj-f_yvhdeRUaKaT2L87g07_fhIfMxXURUCnkHz30MB-lre2Kv3Cvt9d9ifaz3TweRPKBtjO1_TJgKgUc06K_3ZRMvQ8eMeeMZjkhC1DOjiU3PZWzdhh_1fkIDkP0LijjhdGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ff16f06b.mp4?token=acCaLaFHfc5mKkVByt2BTFIe4Wtf0HCDi5KyESIJteHHDVw5YGfAU8e5NZmAlC7w_JQoE-TQW3eW22M5lhz2ybd21wk_QXXNmkpd73whRwsGX3gBnS_08N3nIHfwkjYQPzI2tySrS2wydy6vI8fR5dccgiwz45bMSGZHuFiI8gYhZVrAU-FdnldtjQmcKoprhBJhHrlWVVWPrJag7t_cKjEA9yuXEBmrkOZuGGGgo4zI7asQo_XeiZmDc11t2xsnRsMbfTm96_63HJiwQ_QaS7mbOa1KP5HVfLs6vNCDrorTSv5HQUbPRNfMUpNKJDd-68iZqp_Z8d6VxeNx3pKOVCXZ4uWkDPWeMDQz2h5ppy3pIg5DpbUvKtZAN4ixNw3YxrCLvEnQFizVWeNdfGOIjm5VW_wcqhACdXpun5NWAe1VRxV3l2kqTCjY3FEGBL3Ywg0-SLyNDt9k6whfCsybRye6e-oTJyh6iWbfvUXQ4t1NeYoA6QAnYhuCKQb6rSep2vx_CAvcTQtpCSE7H6ZR_EWtGzUfMlpLeTelNScj-f_yvhdeRUaKaT2L87g07_fhIfMxXURUCnkHz30MB-lre2Kv3Cvt9d9ifaz3TweRPKBtjO1_TJgKgUc06K_3ZRMvQ8eMeeMZjkhC1DOjiU3PZWzdhh_1fkIDkP0LijjhdGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شب گذشته؛
تصویر هوایی از پیکر مطهر «آقای شهید ایران» در آغوش مردم عزادار عراق در فرودگاه نجف اشرف
. ۱۴۰۵/۰۴/۱۶
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/668263" target="_blank">📅 07:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668262">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2b9692df.mp4?token=R9qiZsoeX2Zosq-vvqqtUZtJWfw3Lg6ClPjfLWHwlVJ--glX_9s0mEMEk9zvVybesQ191FZnSIW8LkjKdYbhcuGynuZMqXkw0K55l0-9jcd0RgOfHWGcGMaNi8Vp3wnhdbNUw6aJ4KjVVXBR6ePVrVyFN-AfsB-G5up7MHqksRM7zsO8uEZw5aKfzPbvnepzUPvwR94gfzVj59bAZrS6wJHDe0uxiZNvwmMjHvsnBK-DRg7uVv6fi1eN_a1gteqjsvgYgIr5orDx4dflvWkPAIaZ0WbeejKSvrNLtX50WeJrYWUzrmGbyoFf9M6czCrelly_jDQ6kW0wmP8rkjfAmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2b9692df.mp4?token=R9qiZsoeX2Zosq-vvqqtUZtJWfw3Lg6ClPjfLWHwlVJ--glX_9s0mEMEk9zvVybesQ191FZnSIW8LkjKdYbhcuGynuZMqXkw0K55l0-9jcd0RgOfHWGcGMaNi8Vp3wnhdbNUw6aJ4KjVVXBR6ePVrVyFN-AfsB-G5up7MHqksRM7zsO8uEZw5aKfzPbvnepzUPvwR94gfzVj59bAZrS6wJHDe0uxiZNvwmMjHvsnBK-DRg7uVv6fi1eN_a1gteqjsvgYgIr5orDx4dflvWkPAIaZ0WbeejKSvrNLtX50WeJrYWUzrmGbyoFf9M6czCrelly_jDQ6kW0wmP8rkjfAmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراق، میزبان وداعی که تاریخ فراموش نخواهد کرد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/668262" target="_blank">📅 07:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668261">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/801ccce70b.mp4?token=AeYXVwMj5QGcTHaNTGxTKah3lr6ScVR8A_-bidtmB4aNPwyiO0YCx3DfWhDEZdtD8277AQWfNRXAI3lcosckj9Y3_knzF3QAA41_Ya4AFuuuVrrMuLnIzsuiZqU-iFjmVWo1XRI-l4mONOcqpDsth_vRg_608H560FjjNaUDgOV9FPToKAFNKyKz0FAz_8thG7be2CBm8yujjT2mMqeMBSWWFr8szHtgNlYazbhfqYBq2RzXz7KPl9kVjgfJxfKHsg2TFrA04L4fBGkwdfag8hy6y_c2QnJQWUpDqaQU9x1bak8vbSfDvltSekrKnnToVgJn-oUSfGwhOgjtpKijpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/801ccce70b.mp4?token=AeYXVwMj5QGcTHaNTGxTKah3lr6ScVR8A_-bidtmB4aNPwyiO0YCx3DfWhDEZdtD8277AQWfNRXAI3lcosckj9Y3_knzF3QAA41_Ya4AFuuuVrrMuLnIzsuiZqU-iFjmVWo1XRI-l4mONOcqpDsth_vRg_608H560FjjNaUDgOV9FPToKAFNKyKz0FAz_8thG7be2CBm8yujjT2mMqeMBSWWFr8szHtgNlYazbhfqYBq2RzXz7KPl9kVjgfJxfKHsg2TFrA04L4fBGkwdfag8hy6y_c2QnJQWUpDqaQU9x1bak8vbSfDvltSekrKnnToVgJn-oUSfGwhOgjtpKijpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور مقتدی صدر در بین عزاداران رهبر شهید انقلاب در نجف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/668261" target="_blank">📅 07:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668260">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6ecd8e54.mp4?token=ndmY-e9t9jUijg2mzWxtPFNnZDmn3KhPfX_37y9GYWJMTiJaftogOKgRTXSKKSDnpT2z7UmSsyJstZcBAAkvonsA2e_UzxTk9cF8MvWdde1wZvLfudCoZjUJONXFoELuXP1URMmEkyeVOpzzJggc4KYMzHuEpMOSa9lextn7y8tHaup_qEfFIRwgn4E7K76ScESTozI8hWenzu7S0lkF0IQDQHTf_dH-MNdvi3jvueoz1kA6fGho4b2qqFQ2sMOZnVBHOyf7IyLbNcrrNWQpH7n5yJ4Lxy0jQR1uFDWgDB21vfjNho2y4xnkJhkuscIinDDdFkKV7qFvpGBtR9SDwZupepMSxseltQO_W7OHXGFU7HzYYEz9LEAaYDS_LZOimtayUNpiUgrbbmblIKRLZjUZa1qm9cOb0bLfLvL95DNWuMUNnqFbG_-jYyzuVEFpWDLRulr56kCeGjKDD7FnBqEGySUZlwusEsfQlPTOdC1A9viQDqairUQbaqz4K7BXzn-_mGLJ9szckJR6kX5jOfdUbOj8D9iQ0KYyd-9gbeWmaHe74m6dnMS_9KJoqTrxw3R-4GClWsOnm1vohqWzW3lodJGfMaWc7fjIGdMWZ-cCvCubFEms0A83d_UEgC51Blt5G90kSj5G3CqC1Xi7v3v7q0LC0T83SYnpRRpQkVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6ecd8e54.mp4?token=ndmY-e9t9jUijg2mzWxtPFNnZDmn3KhPfX_37y9GYWJMTiJaftogOKgRTXSKKSDnpT2z7UmSsyJstZcBAAkvonsA2e_UzxTk9cF8MvWdde1wZvLfudCoZjUJONXFoELuXP1URMmEkyeVOpzzJggc4KYMzHuEpMOSa9lextn7y8tHaup_qEfFIRwgn4E7K76ScESTozI8hWenzu7S0lkF0IQDQHTf_dH-MNdvi3jvueoz1kA6fGho4b2qqFQ2sMOZnVBHOyf7IyLbNcrrNWQpH7n5yJ4Lxy0jQR1uFDWgDB21vfjNho2y4xnkJhkuscIinDDdFkKV7qFvpGBtR9SDwZupepMSxseltQO_W7OHXGFU7HzYYEz9LEAaYDS_LZOimtayUNpiUgrbbmblIKRLZjUZa1qm9cOb0bLfLvL95DNWuMUNnqFbG_-jYyzuVEFpWDLRulr56kCeGjKDD7FnBqEGySUZlwusEsfQlPTOdC1A9viQDqairUQbaqz4K7BXzn-_mGLJ9szckJR6kX5jOfdUbOj8D9iQ0KYyd-9gbeWmaHe74m6dnMS_9KJoqTrxw3R-4GClWsOnm1vohqWzW3lodJGfMaWc7fjIGdMWZ-cCvCubFEms0A83d_UEgC51Blt5G90kSj5G3CqC1Xi7v3v7q0LC0T83SYnpRRpQkVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نزدیکترین تصوير از ماشين حامل پيكر آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/668260" target="_blank">📅 07:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668259">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxrYEJUfoRV0osf3UKkq5wD9lutrFsAwsLGNpkyOsngx-tibAsWFEYPMv5oTsovJikpHnkY5FFaja_-e9kNnjU36dUM6Rwwyr5o5_iH2sk37LPqtHqvtTExsg4GafRmPFayZhQ2sMw2bWX8EUdFoqnnN0wzvmHsJdKEA0CvIkQM6vez_OTx0DHDnkBgAb9OLHPyvyzslUqPkEJ4udzTsTzYZ1dESDP_i8wb6s4YRHKB98SeNw9wDzRdmOOXQvBvkm0rifwWfzRip7DKmKFXP5I5W-dwY8JNlLtmAxiJQvF-1DBwcBv7UET3auso7IrwSFLrLdcCkNXws_Apch0zyOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: افسران ارتش آمریکا هشدارهای اطلاعاتی را پیش از حمله به میناب نادیده گرفتند
رسانه آمریکایی مدعی شد:
🔹
افسران ارشد ارتش ایالات متحده هشدارهای درج‌شده در پایگاه‌های داده حیاتی را مبنی بر سال‌ها به‌روزرسانی نشدن اطلاعات مربوط به اهداف نظامی در ایران را نادیده گرفته و حمله‌هایی را تایید کرده‌اند که یکی از آنها حمله جنایتکارانه به مدرسه شجره طیبه در شهر میناب بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/668259" target="_blank">📅 07:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668258">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nggxUlrGjgi8yV6KK9E_ZSyI7Gw_LvMAhY8CPxyE4KXgzKIRqFSmiRCeN27GuCWRi9Te71bGDXUleb_2ury3Bw2o3TuTyAYN1MY2k3kONcpvNN4_EWM1jvPIAfjPkVLJd6dXUyVcLaNi6oSAc_h6Wmu08OeEHvFvcDj56__fovnxPKaL1sNLGDB0l4LkDqxkvLweNf8wA0dLPFnNhWm-3XUdwnDnxhQexr-6ivRRGitacvQySPs_gfVITQTH5lQR-j-e23Ng16r3SCoimsXIGsP39mas1o-zlOP5MX1NS4a6rZQ_A6N2nPS7lM5j8XPvrxqs2Oj2oX7bXoBR5N8Mqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از خودروی حامل پیکر مطهر رهبر شهید انقلاب اسلامی در میان جمعیت مردم عزادار عراق در نجف اشرف
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/668258" target="_blank">📅 07:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668257">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f4c3f506.mp4?token=EiofF6_9XSeL9EUXT2hwE6ocWU_sFKq2az7-9vNl9ZD4EBss5Q1BmxXWjxfWeIsoUdZvNAFtl6czaPaeKP1HdAHGZLUZlZM8kOGJcRqZRtlMWH7oENrVNr1CEFXwBaYmmOH5QQppqMx5qNRQoZkTFsOZ5FmHIWoY-cGiOXYMnlYmZQPWSv3jnB13PoOKvJvShhRRariZ5u36GBeaZMR9MTXO67NXDEfv0PIHx56S4-nO3bnImIBygeGovrCgAaYgM9bZjCUlF5KI-Z__doXTV2W4EbHL5Ng2PbCsEqKvfsBeWd1VGwLhPJWKEyKju59mrsno_ZamlDZgL2JXM43WTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f4c3f506.mp4?token=EiofF6_9XSeL9EUXT2hwE6ocWU_sFKq2az7-9vNl9ZD4EBss5Q1BmxXWjxfWeIsoUdZvNAFtl6czaPaeKP1HdAHGZLUZlZM8kOGJcRqZRtlMWH7oENrVNr1CEFXwBaYmmOH5QQppqMx5qNRQoZkTFsOZ5FmHIWoY-cGiOXYMnlYmZQPWSv3jnB13PoOKvJvShhRRariZ5u36GBeaZMR9MTXO67NXDEfv0PIHx56S4-nO3bnImIBygeGovrCgAaYgM9bZjCUlF5KI-Z__doXTV2W4EbHL5Ng2PbCsEqKvfsBeWd1VGwLhPJWKEyKju59mrsno_ZamlDZgL2JXM43WTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار هیهات من الذلة عراقی‌ها هنگام تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/668257" target="_blank">📅 07:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668256">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سنتکام مدعی پایان حملات به ایران شد  سنتکام:
🔹
ما دور دیگری از حملات تلافی‌جویانه علیه ایران را تکمیل کرده‌ایم.
🔹
ما بیش از ۶۰ قایق کوچک و بیش از ۸۰ سایت را با مهمات دقیق هدف قرار دادیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/668256" target="_blank">📅 07:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668255">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff90c9a8d.mp4?token=gyZkL-ny-nDt0WCLDaUxzstyhDWrmHQMu9dt2QN-C1HaX0VTuDK7oL0o4SJm9i_qKywHvg5qWblDF4As7cWLXSoKts_jbrfLaQ5Wdj0kI1h5WGXGzM5YciQg4q8x0grJwR_UdsVG_iPhqs8SoeQsFiLvgjygM0T2Dpf7I_H65-b9pJRXSYu2h6nX_LXEXoFau4h34D_2ygwYg-k7ISxyamz4ziL0s0C9jyI9D488bo1eGWAxIpLewVwmsIY63FjuGbCDKfLJFI0U7LX14ys6WdGRCrsnlpOtF-8-qUA7VrCKM5JvDHPTJNzQo4e_8QFGrNBCw0RpCiy5fKrRRs1uiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff90c9a8d.mp4?token=gyZkL-ny-nDt0WCLDaUxzstyhDWrmHQMu9dt2QN-C1HaX0VTuDK7oL0o4SJm9i_qKywHvg5qWblDF4As7cWLXSoKts_jbrfLaQ5Wdj0kI1h5WGXGzM5YciQg4q8x0grJwR_UdsVG_iPhqs8SoeQsFiLvgjygM0T2Dpf7I_H65-b9pJRXSYu2h6nX_LXEXoFau4h34D_2ygwYg-k7ISxyamz4ziL0s0C9jyI9D488bo1eGWAxIpLewVwmsIY63FjuGbCDKfLJFI0U7LX14ys6WdGRCrsnlpOtF-8-qUA7VrCKM5JvDHPTJNzQo4e_8QFGrNBCw0RpCiy5fKrRRs1uiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکرهای مطهر شهدای خانوادۀ رهبر شهید انقلاب، در جوار ضریح امام حسین(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/668255" target="_blank">📅 07:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668254">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
پیکرهای شهدای خانواده رهبر ایران در حرم امام حسین(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/668254" target="_blank">📅 07:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668253">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJ-pevN0Md-KgxCiwNLa5uQGeETG2Ub3WmsMloKmoO_8MYhjuZZW0tSzCKsByMka8InxxoxwT96jaqlM9Y9feItQacqQjGZs8wYcC0tFxYTT5LRbTQ2jGAdG1Mqr4oIIj_-llvDLqImv_dFJESaOe1pjc4OFopaDWBBDZ06Vj-8Uo07eJkGXqPIhYQ8pR11wSaZTn62rKqtbGqz4nY81lNlhda-7Rr9L23TKPWwflxNUVZX-ZmhXgZLvuNd1J0tu1Qwzo3kABYvWXrxyxMCwCyl4z006_5GlK7PANplmnOdlfSWLFdoy-qEbMZaB11chkHAuxBuCWsL7hzhqtB5K8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور شیخ ابراهیم زکزاکی رهبر شیعیان نیجریه در بین عزاداران رهبر شهید انقلاب در نجف اشرف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/668253" target="_blank">📅 07:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668252">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
سپاه: حمله به ۸۵ هدف نظامی آمریکا در پاسخ به نقض آتش‌بس
سپاه:
🔹
در پی «نقض آتش‌بس» از سوی آمریکا، نیروهای دریایی و هوافضای سپاه در عملیاتی مشترک، ۸۵ هدف نظامی آمریکا در بندر سلمان، بحرین و کویت را هدف قرار دادند.
🔹
همچنین یک پهپاد MQ-9 آمریکا نیز سرنگون کرده‌ایم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/668252" target="_blank">📅 07:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668251">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10a07000e.mp4?token=gHzB6RcWgY083baCtOzV7iETKEIthXG9_-rqyY1_9ev4QG4PaqyDDsidJhHiTth50vQ0qoqLpV0zq1YwI7EbobI-7nm8lF1fG98VgabFNJRboENLJxfOgem40TTU7l6WZF_3m5t8JbhtGhqTlBtOUFpCdymvUEXCgYaH7F5lP0Y4zqPzBcyDF8QywrelNGlVBX-2DB_8rFh_zSIP4vnYrktki8QzzMFoGQthC4TQ82E-yRldbXjfuMn4iZw42_RaDSNUAFE2FJq9mpYPagSgLavbuU9A2Fkml7EN4hzDS5R7ICEWx9xWJ7DPTPqSCE_HW-KFJ1v4MdO18rEK9kwQMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10a07000e.mp4?token=gHzB6RcWgY083baCtOzV7iETKEIthXG9_-rqyY1_9ev4QG4PaqyDDsidJhHiTth50vQ0qoqLpV0zq1YwI7EbobI-7nm8lF1fG98VgabFNJRboENLJxfOgem40TTU7l6WZF_3m5t8JbhtGhqTlBtOUFpCdymvUEXCgYaH7F5lP0Y4zqPzBcyDF8QywrelNGlVBX-2DB_8rFh_zSIP4vnYrktki8QzzMFoGQthC4TQ82E-yRldbXjfuMn4iZw42_RaDSNUAFE2FJq9mpYPagSgLavbuU9A2Fkml7EN4hzDS5R7ICEWx9xWJ7DPTPqSCE_HW-KFJ1v4MdO18rEK9kwQMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عکس نوه خردسال آقای شهید ایران در دست دختران عراقی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/668251" target="_blank">📅 07:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668250">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ed0bdd1e.mp4?token=ocLQ-T7alBoDJwsAUO-xShp0BaWfqc2_w9lNes2R80LstWI2zzlmBpXsAiPsup6uhciZ7zLeP20TvRVZRu9HLY-jM4yKjn7fSTzdFiDFb5KbeWQsgKkYWWNFftm1r7IgWO8rc3zvDsWgWgYijlsVevZfJ1yWr5VttMB61XODwJSIVX5yMmPyVydVrDwy4O95tMDz6avT9CVQUSc9PvDPjNzelj00gNsabQEnSvr5YLtM4C3wutVIKJ1OA56DtDwGGDC0qHwBUZ22Y69oZAz2DWC6EbthXkc8vyF7Gz7vaNSSruh2giCTtUJgAGqEhgin_6ECh66QudleSRERx94Xjp_5qJy7r15PBKh0soPCk_SnmjxaAeqyPnGQrJPoT30XzG58KVEz7XrUtJwjDAqe4T3orBSoWMC4aSRdZF6zAwIpwsosmP1BMydCZb0aLD92TrnkHrR8vd0QfCdOuJSOHyJ6NcvRP_BysTleaUqwcEIFrDD8IIC9wLTABk2WI4LVXCnjddb5YKuB1H-2x7VNNzA4ZcpTzv8Ngwd0Rx3h-_EgFd-vEYR6DXtYdl2LICV3GeHfSQn29BK2hljQFbIsaGqE4iYJnAzS1cm5ivnYArV3SX7WUMeGT3ANYg1vDAhivOR3x6FG_P2357xlH9nZF5ihO6NzdwEl2QjATMK6NXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ed0bdd1e.mp4?token=ocLQ-T7alBoDJwsAUO-xShp0BaWfqc2_w9lNes2R80LstWI2zzlmBpXsAiPsup6uhciZ7zLeP20TvRVZRu9HLY-jM4yKjn7fSTzdFiDFb5KbeWQsgKkYWWNFftm1r7IgWO8rc3zvDsWgWgYijlsVevZfJ1yWr5VttMB61XODwJSIVX5yMmPyVydVrDwy4O95tMDz6avT9CVQUSc9PvDPjNzelj00gNsabQEnSvr5YLtM4C3wutVIKJ1OA56DtDwGGDC0qHwBUZ22Y69oZAz2DWC6EbthXkc8vyF7Gz7vaNSSruh2giCTtUJgAGqEhgin_6ECh66QudleSRERx94Xjp_5qJy7r15PBKh0soPCk_SnmjxaAeqyPnGQrJPoT30XzG58KVEz7XrUtJwjDAqe4T3orBSoWMC4aSRdZF6zAwIpwsosmP1BMydCZb0aLD92TrnkHrR8vd0QfCdOuJSOHyJ6NcvRP_BysTleaUqwcEIFrDD8IIC9wLTABk2WI4LVXCnjddb5YKuB1H-2x7VNNzA4ZcpTzv8Ngwd0Rx3h-_EgFd-vEYR6DXtYdl2LICV3GeHfSQn29BK2hljQFbIsaGqE4iYJnAzS1cm5ivnYArV3SX7WUMeGT3ANYg1vDAhivOR3x6FG_P2357xlH9nZF5ihO6NzdwEl2QjATMK6NXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ پیکر مطهر رهبر شهید انقلاب اسلامی در جمع خیل عظیم عزاداران عراقی در مسیر تشییع نجف اشرف.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/668250" target="_blank">📅 07:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668249">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipropej7eW7pX8vkDwDhNPksbusK6doCQhQD02ajWtHaqCnfKwnQiIzVzLNmr4BFPV4m0uTJkiiSwW0LO9ky5uMOZFwS7Qk4lN-rXR5vDNE2vixw1W6kxuDwybgeNEVeNMESTuRKA7t80fKRylBPH1q7Z607VrLYILWrFNVOMomdbAYCD7B5vxHoEYbM7V43A_U6GxVzfSfxD-onLZr4WYOX3nvc7SsqK7gN2o4A-S5VfnhGoEUL2BIdQ2raTa7t7jNPTXf5Tp3Gx2Qe_Q8rpzQtftmGxCIr4OVvViO8a5ggx0m3N3H-R1iWNEUWizx8j3farmyclb5S0nt5E04ENA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۱۷ تیر ماه
۲۳ محرم ۱۴۴۸
۸ جولای ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/668249" target="_blank">📅 07:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668247">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d75a445d83.mp4?token=HJkCsDP-WYuRaZVynbI-6YxcYYE_Ndcn2XIvn-sjFUBskPgUsgt6yOgV-TjVUMxXn0ATSCPs73jCrXKalpTM0kGlEO1iZbzP_w7BVKbhLUkyPpUTJnIMC8YNnx5ei26fLpcsy_uDArjwd9dImxhTCZfTBL-AcYUS_Q_Y58Hmg6IXRkgI_gO7i_ZoNrDSSXiV1px8vT92vJU0Cxm5S7PeeFLA3xf6M1EqimybFVhjZuEYZCOV6cm3mnJ4p9-LYNaLDfANBG-BxDLxNUl4BfUHSej2gybmRhIhC1NgRnguRzROC_alSC9-s_JY_7iJlquumCrl8vQDetv_STWmrDdB0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d75a445d83.mp4?token=HJkCsDP-WYuRaZVynbI-6YxcYYE_Ndcn2XIvn-sjFUBskPgUsgt6yOgV-TjVUMxXn0ATSCPs73jCrXKalpTM0kGlEO1iZbzP_w7BVKbhLUkyPpUTJnIMC8YNnx5ei26fLpcsy_uDArjwd9dImxhTCZfTBL-AcYUS_Q_Y58Hmg6IXRkgI_gO7i_ZoNrDSSXiV1px8vT92vJU0Cxm5S7PeeFLA3xf6M1EqimybFVhjZuEYZCOV6cm3mnJ4p9-LYNaLDfANBG-BxDLxNUl4BfUHSej2gybmRhIhC1NgRnguRzROC_alSC9-s_JY_7iJlquumCrl8vQDetv_STWmrDdB0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
السلام علی قائد المقاومه الاسلامیه
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/668247" target="_blank">📅 06:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668245">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USkJH4LYCafjxivXgzhd8PUjxfOYGgrYLa2Q62a9Nj0E2iCT1Bkw5AN7lSbsSPilSV5E2Wbx7XB9vlipI7R444L9pxiXlHWzR1FsQcUz4OM5hPgd2vEBUKuw7xNItq_DISNjXEGvZaeehR0-aL1drn9ZKyjpseN8bG03echTMo9xLxhAZa-KgnqxVI32AnlvJI5VEMlNid6GMqI4c7BecM3WvbFYiGn04NZpsNf5xtLGMyVchvO1wNl9dupHk6-1eebKxx4ZrxIBC3z9PW4B5WmKrD5u58UY-vMI5MyLwpmZptBzPboAu_xHtN1_MB_Tx4A4Vnykftspu6obP7T32g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xxcm5dtLzQLSfwhDWX2K2ESmjC6rQTPcdKlw77MJ6tlb3-GF5iYx9C9qPOq-QxZLFXNplKURLufan07xuu-lz7ngtuiyilX3KyShFEMl3s_SGApfPsWDqui0f9n0RNZW8yPgxw_p53tovB-0a2b8ff2tqxzb9A_ME_-YFZC6IyUvSra8bfnXMw6vrYaqNRUgyclsEtPl5XTHYzun-R9i_zce7DHy1jG2zihP4PG8q3RdjrU3piuprEJ3rreQgZtJ92TKXWR7Af_iPxMHu2ToOCW781TKit-TGwnKNC9WK4n_K6ZehhuM7_yvOjjK6VcGyuJYMHzptxSNauj9aSNcbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از پیکرهای خانواده رهبر شهید امت در حرم امیرالمؤمنین(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/668245" target="_blank">📅 06:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668244">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2c3a8b7ce.mp4?token=RCES7q2PidPHGP-5hmJSP16GtvL3yVx7nJ5UrOC1ZqMXX2RRGHmod3nWM0lby-vMPxygVgDjmPWmJUW6plbhEyJ15PPkd7aftjR6-xHrUTZOS4pCmtjFvpdsnigX-OPmCX5SFW4xbSEqn04LHzc8-9TjTuaZCe4YF6Fhiv3lcoANXBidv2ey9c7FDeweUs-YQjkPEelz5sBcwqsElgalT5dBzMAf4CE8Ht1V2DAfmwvICi278ORPdFRoShkT8QlSi-QumD6FGid5cKrDZUkBqzEx9-y8niW4zuF6gsqdRA9OtWnEgvMV8pbphm7_ZVMHYZzsNpho8CzBAkpSieDtNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2c3a8b7ce.mp4?token=RCES7q2PidPHGP-5hmJSP16GtvL3yVx7nJ5UrOC1ZqMXX2RRGHmod3nWM0lby-vMPxygVgDjmPWmJUW6plbhEyJ15PPkd7aftjR6-xHrUTZOS4pCmtjFvpdsnigX-OPmCX5SFW4xbSEqn04LHzc8-9TjTuaZCe4YF6Fhiv3lcoANXBidv2ey9c7FDeweUs-YQjkPEelz5sBcwqsElgalT5dBzMAf4CE8Ht1V2DAfmwvICi278ORPdFRoShkT8QlSi-QumD6FGid5cKrDZUkBqzEx9-y8niW4zuF6gsqdRA9OtWnEgvMV8pbphm7_ZVMHYZzsNpho8CzBAkpSieDtNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور حماسی و پرشور مردم در مراسم تشییع رهبر شهید ایران در نجف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/668244" target="_blank">📅 06:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668243">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0085a62f98.mp4?token=hExML-oA1BxOj3oGb-U8yY2ljSa400VVZWCfzuXkRmH7cLPdKBrbmFYGX20_86n-ri7B6j29WDWMIykzsdfDThMbxrUdUi2Rxc6ezvGiUUg-4JCHVgXpxLh4JipRYPXqx2JZjt8IiWPvXC1FeQu06GKJvoXx6cYs_bvDnRzRQ5O-IMXfHs8tH_wgnnZHgRDtNJjoFw1klQRiwBB0wiNnN1SQwFE4oYyjMhjJZgRygY-OGYyVnKg_SldaLekuPKq0HvReSewhcKu8Rj6qEPx0M3tdnBOq53uyuW0zd0I46y3MX0QuJKOQreGk1LvHdFKkK4wonPr9hB33zmHOk6A2wx5PZyJnkY32MWxuDCcnqJeWYDILRemxjJIagMX8bldq6akYVgBTV80eKCmPn57vlOWUxls-e2nGnBWyXHdLDSv63m9rjfblkNPbFbF9NqogGS5J99HiDuLPPPkRdp75zz5D1-lYFWc7d0PpYFDST84AW3hFJfaD0P-CPXk-UA7NUZm3c42UrZGWir84KY0VKQaQA-SdStk3kyJrLfxvIrBRSf2zdrE2zgQtfoigDk_-NOFc-dcM36y_k0tFFUb468JTC5cL-i3ty77KQcm7kDxXAKcFZmPDql5dkGnqW-o7RoPjvbOGlgyS3yhEw0eqUVZRGEQdpcO3x_a9wK3NV5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0085a62f98.mp4?token=hExML-oA1BxOj3oGb-U8yY2ljSa400VVZWCfzuXkRmH7cLPdKBrbmFYGX20_86n-ri7B6j29WDWMIykzsdfDThMbxrUdUi2Rxc6ezvGiUUg-4JCHVgXpxLh4JipRYPXqx2JZjt8IiWPvXC1FeQu06GKJvoXx6cYs_bvDnRzRQ5O-IMXfHs8tH_wgnnZHgRDtNJjoFw1klQRiwBB0wiNnN1SQwFE4oYyjMhjJZgRygY-OGYyVnKg_SldaLekuPKq0HvReSewhcKu8Rj6qEPx0M3tdnBOq53uyuW0zd0I46y3MX0QuJKOQreGk1LvHdFKkK4wonPr9hB33zmHOk6A2wx5PZyJnkY32MWxuDCcnqJeWYDILRemxjJIagMX8bldq6akYVgBTV80eKCmPn57vlOWUxls-e2nGnBWyXHdLDSv63m9rjfblkNPbFbF9NqogGS5J99HiDuLPPPkRdp75zz5D1-lYFWc7d0PpYFDST84AW3hFJfaD0P-CPXk-UA7NUZm3c42UrZGWir84KY0VKQaQA-SdStk3kyJrLfxvIrBRSf2zdrE2zgQtfoigDk_-NOFc-dcM36y_k0tFFUb468JTC5cL-i3ty77KQcm7kDxXAKcFZmPDql5dkGnqW-o7RoPjvbOGlgyS3yhEw0eqUVZRGEQdpcO3x_a9wK3NV5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سحرگاه امروز؛ لحظه ورود پیکرهای مطهر شهدای خانواده رهبر شهید انقلاب به مضجع مطهر امیرالمومنین علیه‌السلام در میان شعار «لبیک یا علی علیه‌السلام» عزاداران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/668243" target="_blank">📅 06:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668242">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
منابع عربی: انفجارهای شدیدی پایگاه هوایی السالم در کشور کویت را لرزاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/668242" target="_blank">📅 06:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668241">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
خبرگزاری کویت از فعال شدن آژير خطر در این کشور خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/668241" target="_blank">📅 06:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668239">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
خبرگزاری کویت از فعال شدن آژير خطر در این کشور خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/668239" target="_blank">📅 06:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668238">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
سردار محبی: یک فروند پهپاد MQ9 در آسمان خورموج ساقط شد
سخنگوی سپاه پاسداران انقلاب اسلامی:
🔹
در پی تجاوز هوایی ارتش تروریستی آمریکا در سحرگاه امروز، یک فروند پهپاد MQ9 توسط آتش سامانه پدافند هوایی سپاه پاسداران انقلاب اسلامی در آسمان خورموج استان بوشهر، مورد اصابت قرار گرفته و ساقط شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/668238" target="_blank">📅 06:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668237">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/36ad33cf7a.mp4?token=enXs3L-gTagLdQSHbFywsnmsPlEUCSSA8rPMYQhiNIJXaaK4Xw9sMvAK7w3VDsl2UZ5UWJs45Z1h0uIRD8kWHgK2anNz970Uq2t96_-BNCh4401xBe_HXIV_pxM61rNYHXsBQytTHjYDWitF22eH0g80b8oyhFgbqNqLtBeiWqhvHtEvbJyyNN7gyxDWVJp2TcOeZ-seB5LDu7xCJLL-pboN5OcSXepPezGXKXVEkci7YFf1QTwDpv60weWDLna8JamjBAxNObvzVm9l31Wa3XZX86QWdLibjEw5iH5qfPYBlk4J36MAG4Z9TCsHt3GOD_giEyvlj8AeYUqar5R7rA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/36ad33cf7a.mp4?token=enXs3L-gTagLdQSHbFywsnmsPlEUCSSA8rPMYQhiNIJXaaK4Xw9sMvAK7w3VDsl2UZ5UWJs45Z1h0uIRD8kWHgK2anNz970Uq2t96_-BNCh4401xBe_HXIV_pxM61rNYHXsBQytTHjYDWitF22eH0g80b8oyhFgbqNqLtBeiWqhvHtEvbJyyNN7gyxDWVJp2TcOeZ-seB5LDu7xCJLL-pboN5OcSXepPezGXKXVEkci7YFf1QTwDpv60weWDLna8JamjBAxNObvzVm9l31Wa3XZX86QWdLibjEw5iH5qfPYBlk4J36MAG4Z9TCsHt3GOD_giEyvlj8AeYUqar5R7rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل خروشان جمعیت در مسیر تشییع/ عبور میلیونی سوگواران از پل کوفه
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/668237" target="_blank">📅 06:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668236">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال درباره تمایل آمریکا به ادامه مذاکرات با ایران به رغم نقض آتش‌بس
🔹
ساعاتی پس از حملات متجاوزانه نظامی جدید آمریکا علیه مواضعی در خاک ایران، روزنامه آمریکایی مدعی شد منابعی در واشنگتن از تمایل این کشور برای ادامه مذاکرات با تهران به منظور دستیابی به توافق نهایی خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/668236" target="_blank">📅 06:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668228">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJCPdOLa7qrOmgt3ISHeVvtPN4x5uYIx5ydWbZyO-ZPc0mXEccJsXnZ9o8XuJzWU9tvfSjnXWYdCDVjuVyikWHV2o3MtOdbpX7ktbbbXIUpkwV6gLEkfOjm4BlLDM8cCPamJirLpDxs3yUCW_kNHvUykxWQRbauXZlqub6yOgOJUCPD_tP0O7fcdH3_QjbC8oi7lekWKWfqK9-W1mu_nRze9Ctgqy7wf1DH7igqm4AQ3s8hREuQIrTMfpfOiLHihqNUqDt73K6ldovBgha2GK1tv5HcsRMmyT2eHYNJ-rMGSK8G24gx5AWGmkNUbFI92PO2kydjl3XNIay5wCKZZ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O57kxoggj17CoqqQb-Tvlx_9DZHwNS4HfHCrUbHPkNyhSDcnzUCCwVGqyKt686wur0tUPvn91GTLQX4E7uVU6yPtfkWFQw3hOxxIhritrEj3dwwmZ4RPu8O4IDoPXlJNAAl6J4TvZwHRQbmhEajyw43Lr81mBRyzwEoczNMg61LCV6o6JNSoSltZy-Q74J_PWnJSlCrLJ9EL5GL7aYOlfwZ68Xt-TLmTs0AWx72r-eo6uZi6bvZ5CAKugZJgo3rIUdtCz0NHiTVu0p8I_asC6WmeyzkfbXo93xBX9zR9Bk4zOyNBy37Lc2ZJO7mYKtKIVxJbNT5d1kuDP27YnXnnoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-hB_Iy_cl_Z8eTXZXzpUMocTopCmbcUJns19kcSdl0iTwMWSnhEqNnpC0jMAD3vFogA9bjER2uvAYizXiSWL_FaXrXXQu3MA6g7xhfmmNMWObnihj7_liNXh723uJ40AzdMpWew3HqLKBOr0HgFw0Ubt7MY1tDSn-4506hD1LjggrMf1Nq_Y_M3wyslZtjAnkpSQ-5RaBZ-ye4sRjsaVSVViqoSOt8hP7f7Cm4j9CHgBVAm9vcveu2Ydsgkt449Oy9wKd-WNubNNtehqgpy9PgRiFZ_SnYU5Wrh3lsp8OfrsfkUVV9lvuR7OP1SgL2wRLeThOmVs7wMjWCSpXDgaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdBUiyzyslwzwtjMh1Tpx8VKa-qstbf9ESfp33H-CnmW55moIrGQ-wS_b0HMhoek1H5MLdgBXiKsYWmM5TzBFZNAzAYDoS1DiD9gtVqtuFA4EhDFT7_rExuMURvE2fFW4PT4z8QfOvGnY5u1WE1CeADdnkPJAvb09tDbT5bq8d2NGEt0k----JBYSdDRBhMxMNx3f3E5LMYczbNrmLg2HnSnB-dM_ywG7ja0pZJmK_EyitTK5aRHZ8Y1n2CsGEVFxa2G8f12LytElAeNDq-22OoOcV5JyIywD2ForoLO522kFuKMh1uL2M-Hcp-WzrMwTFh5unqDqtohIzOWEp2I9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QObkLqJ5t2DYdQvGXA2Mrns2_C0RgrIHJ8h5tIttla_3G0Z67qqGnXY6prqBzissY0lzloYudXBVaeZXEMrmd8rNL7FPRkHfBjMB_rtISdYpKFGUGUhuX89UEtLE2BRpEiDi0vLl_1weC-CLwTnMsu1QpThaeQib3NvUCgsNwsF0xzRafEvzIFwwkmBGAxVDIFGac9lCoIZcVYBe21A1DKESiZtcTgwD9NlCDzRbM0BPjW6Sfic1ruqDoV9Gq0KXZMzRTZ1cE7aYgTkRiHluEUYEUyTCAlpMUgsECLe5InrzhybAuHCtxkmhstHu_HITT5xTe5FOznklblviUJt_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/blzkrYXdwMEYvyUehMOEZ-MOWz_AbmhfKLVTuNcmR_Wh4ofAtwY8Jdh1fSOIlveLxkn1rr2dp6y8JYHoRJWyUZ68hjgYlRj3F-nOefY3JRmCx1VrYuvL8WVKnAt1RjMocL5Nojmj6rI9wBUspgU24sVS7KfQ9qVIzrtDyYzd_DWyb-kDNBjAliQFvI70YfcSSm_90VbK9M38l1ymPKNlnyXuYuWO9E6AFk0Q4ny2O2nl6_HKsCW7dggtpe3eijw-2VttZKMw3AkK70nAeY-850aGQz1GauPge4UnYz7o-BV3TYN-Ce53RU1d8uqRKeT99scDdXlL1JtHuRCIr5cZIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JiNIsHKfhDUNF98DwZluP_043z6W3HOewJIVXc2-rDemtiFuNbaWLZTELSJrHcSxQaCdqURg-z5LYmL4dMeAp_Ph7xnW-xVzggzhqW6dEqC3BwtqaISbXb8X3pdhOXi5qfLulCZbhK_oxjLerNPBRXgwOmvAG5a079L-f6cg1G-qKAVx8FWQZ8q6chuE_8Dzc-7WcdohWwtAad50Q9823quSpLfrda6cd2mKeXFIe0NCweXloF5cIH0i0wPig-Yp7sp74mKnfCwB3m2nrC9B5qcvAM2ffPI40ARQdFdUnE9EIiuoJorZwAaFx60ej6B8CfZupWp1Cw_6v56_2N6qzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DiHHXPapwq1JMJpvWewmvreG8xioBiQeB60Zko6GyNCx2q_lCOQUpddLEZpgqIMvTPzvEhZSjM5oVabK2sXQNrOa0RgDLzb-664dcEcEr0qoIrnfh-LtmGM0gdXjjIziffMEiHtv4QTMuylmCFroS_YptVrPD0yLk830KU8TE_Qhmso4igMyoz8nTK_U55AFJvfdARc4F8x9jCxgPzw5TsnTvTVqvPJ8-bUnDCMfNTtpj1LoTO9qV77fNhNDAWzex82Cke-Jp8vlhlSQkGxVVj71HwKDQaTQBydRir4A1ytBHm4hlXTWnXnNi7wANnbyEsHW3731vup4wGMeNDFJoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
غوغای عراقی‌ها، دقایقی پیش از آغاز مراسم تشییع پیکر رهبر شهید انقلاب در نجف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/668228" target="_blank">📅 06:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668227">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
صدای آژیر در بحرین دوباره فعال شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/668227" target="_blank">📅 06:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668226">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58742557ec.mp4?token=vJjLhDLIPW1l9o7M56m-O5fbLYNfyyaahElaAPcAf_NYUqV_1eSDM9L_lZfPIrconPYAjAFnY5FwFlAVzR5B5r70rzK6kug6YuziviWPkH7Je47q8ngefw4GlXwE7hegcautOpsYIIjVGOM9jwfXe1KcyqTY3guyIjlBscwhy7HkKG669nTpb5YtzNVBIxOuzAHsgMJCtds45ZChmdd8ZqXht5xXsHvNB1RQdKKDOhidL8iwUOFhxOcHx7a8CAIS9wzbuMcLycE4fQdDEv-Os0aJ4EulmrGhL5PVWguWoVbOqLvW6INJHAQ3Bj4keYrEbGa9-2NRHh133LamrG9Wmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58742557ec.mp4?token=vJjLhDLIPW1l9o7M56m-O5fbLYNfyyaahElaAPcAf_NYUqV_1eSDM9L_lZfPIrconPYAjAFnY5FwFlAVzR5B5r70rzK6kug6YuziviWPkH7Je47q8ngefw4GlXwE7hegcautOpsYIIjVGOM9jwfXe1KcyqTY3guyIjlBscwhy7HkKG669nTpb5YtzNVBIxOuzAHsgMJCtds45ZChmdd8ZqXht5xXsHvNB1RQdKKDOhidL8iwUOFhxOcHx7a8CAIS9wzbuMcLycE4fQdDEv-Os0aJ4EulmrGhL5PVWguWoVbOqLvW6INJHAQ3Bj4keYrEbGa9-2NRHh133LamrG9Wmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودروی تشییع پیکر رهبر شهید انقلاب و خانوادۀ شهیدشان در شهر نجف عراق
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/668226" target="_blank">📅 06:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668225">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68ddcf397b.mp4?token=QFDUgzV2Lm_gEfvaYB_wDMq1RT5V3WgyEZjjVoVIhGzUm2GweWlJm8WJAUtd4w8AIkF90Ofz7EQhH7Jyd86Y7u07hzkHlVD-SN-FgryUr7U_IHsWjHiq3N_wbSs6s0So5j7yB_x5NYtbdLFajYO-KiQeSvAismhsTEbQkc1Ylr8lGfSwZpaloM5t1pBwjvpzTLefsEXubFPvgNVUNDdgsOc_wUxVue3BZWiirpmkVhMPWXm2Ek2j_WcTf6VWhfw6Iy2TH4lmpDniAFSllL1vjUt_Af_KAch_pIK1LmKy6p66MCCtcd7Tz2n-qM4wVepdjQwjF3X0cAPVoceRBctm9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68ddcf397b.mp4?token=QFDUgzV2Lm_gEfvaYB_wDMq1RT5V3WgyEZjjVoVIhGzUm2GweWlJm8WJAUtd4w8AIkF90Ofz7EQhH7Jyd86Y7u07hzkHlVD-SN-FgryUr7U_IHsWjHiq3N_wbSs6s0So5j7yB_x5NYtbdLFajYO-KiQeSvAismhsTEbQkc1Ylr8lGfSwZpaloM5t1pBwjvpzTLefsEXubFPvgNVUNDdgsOc_wUxVue3BZWiirpmkVhMPWXm2Ek2j_WcTf6VWhfw6Iy2TH4lmpDniAFSllL1vjUt_Af_KAch_pIK1LmKy6p66MCCtcd7Tz2n-qM4wVepdjQwjF3X0cAPVoceRBctm9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نخست‌وزیر عراق و رئیس‌جمهور ایران به پیکر مطهر رهبر شهید انقلاب اسلامی در فرودگاه نجف اشرف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/668225" target="_blank">📅 06:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668223">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
صدای آژیر در بحرین دوباره فعال شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/668223" target="_blank">📅 06:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668222">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp2s1B2GcRnYiyWsm-68brtFz7emZbDu6g1fS0b2nhWSryR8HHw9-NbN0Qs46kVAiUnrDaqVFb26Gm3iia1XbQXdxfItZT7NrFY0C3E7mFImgnkm78BrEuj4BLvSq6QR0HcXE4-49sRos001jkwfQp2MvyoGYRI_zyOrfZ5j7rHshIQWqOOyQSAXw2W2AuYrEiyrERtGe-A9Qu79NTbCDKdPLHxs8X7Zs_Fe4gSfkzFjYhcckF4PW4beI2VermXdeX7K9hAB_Y5Nh4mqRbX8mnG8jfJtu2N4d7FEISTOGNoXu7By92v3R7niwA5OclITL7j2Px4dfveCzyDjqn-teA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف با برشمردن موارد نقض تفاهم‌نامه توسط آمریکا نوشت: دوره قلدری و باج‌گیری تمام شده است، راه به جایی نمی‌برید | ما اهل کوتاه آمدن و عقب کشیدن نیستیم
رئیس مجلس:
🔹
کلیدی‌ترین موارد نقض تفاهم‌نامهٔ ۱۴ بندی توسط آمریکا:
۱ - نقض ترتیبات ایرانی در تنگهٔ هرمز
۲- تهدیدهای مداوم به حملات نظامی بیشتر
۳- حمله به مناطق جنوبی ایران
۴- بازگرداندن تحریم‌های نفتی
۵- استمرار تجاوزات رژیم صهیونیستی به لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/668222" target="_blank">📅 05:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668220">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf867b1801.mp4?token=Ml3lUDaeOONkpmPRWrSSKXk3A4sATqD9DRvXxVT7YRa2Wj6See8MXM84HOc6wq_0taWOfB_Vz-Bupub229BGqCmfyp6JOCMjLfeptSVuraPQmrjKF2CZfWj2K3ztZxFrCOFLb07U3sQKgFZk2czrfgD6p_cwNr-u9MskWwrKr2EA5btga0wIUCSoWSYWkyOiyytFaY72x7mD-0E0whjEYd9VfuVrRwZAcsURSnPcMnmzJzUKDzjvaRPnyj_OenEHxRiVdjTAhFmnJeNUn0e6-aRmudSCzKvaV7cLiTQjkTskaPQtXa7UqGZsstTUsH1uqbubSQWZm9lexdMvCMfVhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf867b1801.mp4?token=Ml3lUDaeOONkpmPRWrSSKXk3A4sATqD9DRvXxVT7YRa2Wj6See8MXM84HOc6wq_0taWOfB_Vz-Bupub229BGqCmfyp6JOCMjLfeptSVuraPQmrjKF2CZfWj2K3ztZxFrCOFLb07U3sQKgFZk2czrfgD6p_cwNr-u9MskWwrKr2EA5btga0wIUCSoWSYWkyOiyytFaY72x7mD-0E0whjEYd9VfuVrRwZAcsURSnPcMnmzJzUKDzjvaRPnyj_OenEHxRiVdjTAhFmnJeNUn0e6-aRmudSCzKvaV7cLiTQjkTskaPQtXa7UqGZsstTUsH1uqbubSQWZm9lexdMvCMfVhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیل عظیم مردم عراق، دقایقی پیش از آغاز مراسم تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/668220" target="_blank">📅 05:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668219">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
شرکت شهر فرودگاهی امام خمینی: عملیات پروازی شهر فرودگاهی امام خمینی از ساعت ۰۵:۰۰ صبح روز چهارشنبه(۱۷ تیرماه ۱۴۰۵) به روال عادی بازگشته و همه پروازها طبق زمان‌بندی تعیین‌شده انجام خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/668219" target="_blank">📅 05:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668218">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93dd221766.mp4?token=Awgldq1IeM34JT1utbGM2WD0VEb_8V62ZlMhQgLWGV7AJ2udiZkdmJ7ynxxacZyo4tYRWSpPLI33l2fY1F3g1lFoxZD2eFdN84wC-uMqswe7jnOpI9gN3R7Agkdry3SEhVNusXYvhUprrhnNNaskM6wr-cKd1fL04p_TT_CY1oqlr_Ep2sLB_1WH1-aCcFljEdq5PpSDrp2pwq9QoDPDPgruLAQyeRJ_2WnmrdmzmN0b7LVDUYYmlMehjDDZtx_nm4qUrIr7m0R9Xagpl4WOt1ju2MSCLoG4JY_t4ITtwcmypo631kAKNqygLNk5WKzAmwmhDTI0fTZH_q34z79Y14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93dd221766.mp4?token=Awgldq1IeM34JT1utbGM2WD0VEb_8V62ZlMhQgLWGV7AJ2udiZkdmJ7ynxxacZyo4tYRWSpPLI33l2fY1F3g1lFoxZD2eFdN84wC-uMqswe7jnOpI9gN3R7Agkdry3SEhVNusXYvhUprrhnNNaskM6wr-cKd1fL04p_TT_CY1oqlr_Ep2sLB_1WH1-aCcFljEdq5PpSDrp2pwq9QoDPDPgruLAQyeRJ_2WnmrdmzmN0b7LVDUYYmlMehjDDZtx_nm4qUrIr7m0R9Xagpl4WOt1ju2MSCLoG4JY_t4ITtwcmypo631kAKNqygLNk5WKzAmwmhDTI0fTZH_q34z79Y14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر خوزستانی که از مراسم تشییع تهران جا ماند و خود را برای تشییع به نجف رساند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/668218" target="_blank">📅 05:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668217">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0HGiKGvlRkNMI1XyEenVkvVVeif9uxxjQaLCDcnAEw1UmTJQ5bpNKWpR-SJB2Q76XkR5_GhbWVqwjy52cn0xoFRpxe1OMu363rJbORS2tjOzaWMW2jrMxAPhvBAJEuz9sJrjn4btcDaTonCt2OcA8tY-bbq-7dZv0S8X9t25Iwu6KkBAvraJwcIeEtk5x6Cq3xLba1vjntvu4gxHQcRu5dZx5IoNB6cKySeDQNAWTYsEHhpZ2u7I-euFtpE92EPq6gLjDaoev7jRsX9NJ_E4RbKY-SFRgipe2tAN8yZEg9w6qLWj38XSdiuieONL81KhlleTuDlyGDnhR-Shns57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
خیل عظیم مردم عراق، ساعتی پیش از آغاز مراسم تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/668217" target="_blank">📅 05:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668216">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1v-bBbKQbbDQnmZz2zVV0DPS93QCwlYqAGwjjevaTibRHnea8C_3IasvFYZBeW08v5pfSlRLn3dGMOVXbT6k19mY6JhnPWgAyENx30BE_KrYlOKyqjdlikY3dka32WvQ2YorHCNzj8dY7ueMXDGbz8Y98UX5jxVEYv2hBMTFnrqWuEtghsBEA2ig5AHREiFfvDScATqt0BmKG2XPnCpdlf52w3fh9T1a19UR4fJaVUbkr7kCicI0fgbJ-_LlaqeS0CfeIL63C4PtnFkabzBFGsieCR4sSMvIsxmyBODUkf73l_woNHRokBjWX9SBPrjXihCVZr4ibGqOX1vTOpFuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر آقای شهید ایران و رهبر معظم انقلاب در دستان عراقی‌ها
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/668216" target="_blank">📅 05:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668215">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0978d5ec24.mp4?token=QBYysuW0i-2gIKPwepWJGkq1LtWIAgUBG71fzItMuRJI_hTnOA0q7Wn208c81WMsfoUzDkYZXHy39ytEaJokvYdZ2FJjiAXGkFBBzyl_5eAtN1cSPW7oJlBdh8hGKAz4HbeAK7ThHvj4YkGQ9z-vGC_JefH_pundUt3vWUaJgb_n-NkAWB9z_dotBPj4CzgI9jYEdTpI9tEuUofZ6_z_uoGRJb1dAdRBZsklOqqcZMzrP1eTDVft7VMpd2cjfI-_xtJjCN5GbKr37V58r9i_8tuqiIbKmbq68A-R1FwEqtDEw1HpX7uECLD9V142i58Rxg77i86vnDagN6C2hruiCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0978d5ec24.mp4?token=QBYysuW0i-2gIKPwepWJGkq1LtWIAgUBG71fzItMuRJI_hTnOA0q7Wn208c81WMsfoUzDkYZXHy39ytEaJokvYdZ2FJjiAXGkFBBzyl_5eAtN1cSPW7oJlBdh8hGKAz4HbeAK7ThHvj4YkGQ9z-vGC_JefH_pundUt3vWUaJgb_n-NkAWB9z_dotBPj4CzgI9jYEdTpI9tEuUofZ6_z_uoGRJb1dAdRBZsklOqqcZMzrP1eTDVft7VMpd2cjfI-_xtJjCN5GbKr37V58r9i_8tuqiIbKmbq68A-R1FwEqtDEw1HpX7uECLD9V142i58Rxg77i86vnDagN6C2hruiCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ازدحام جمعیت و حرکت مردم عراق به سمت پل الثورة العشرين برای آغاز تشییع پیکر رهبرانقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/668215" target="_blank">📅 05:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668211">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HWKudp8Og6OASEDegQna3BXmsMs8vqeZvgqV8H2ma96mQmCyDuy5JZ5KGJbtZrMB7zMUc28ZxNruw0GTIfOYg6419prhktorGH-R60UjwgwvhFiCtqNwjcCtjVxpNhmaJM8iIWZSpw9f5DMA7p99JOlwzVPZ5BNnh3wtWFWyh-86KsizgbWHO5ChrmG2SZHLfPLiM-qFVOE4gtuUmbG0zzGhfauMOfPw-qV4ln9uOigkPN_pdYaO_9m6UFRwVlTdrOF0Mc0hLqO6hcKpvZin3i4lUy8rNX6hQS05DqOvrFaD1pSD9TSLXlnAi5p_DhQmhQrRquRMfFkiID6rWnlNJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LakJPcVFJY-iuUl4y2m8q7-YTwAWrzL_X4oKgStJ0OOoCN2wWHSSdMrc4FmXp182zp582ujBeXgqe4Nai8tMC2SgplpSHTPv2rm5zpZW5pyfBxwzzqD8PJSvj_a0i4-eaBm-vjyIS50UPON_OykrmR_cxPknPYMtIqv60SJvJzV6rqpbDaJKyIIGUsteZbJ2kl45ac_KIDSzzDS7Xle00vxft7WNgbNXKI-8_YcFXVnlBglHSIhU_xPSM_07cgkdDcCKjnUc4u1T76vfWtgTrj8Z9ZSsFo8d4M3qg9P7MPZEWRp-7zj4ffc5_0YPW0vCE5xa6OLgROlGC1PeXUR00Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtZjLKNJwZHPBDtsCInHGycS6omlBH29b_2zWBLWfGun04hGB0pHTB6FcsT5X16ffxJfOkc9SdtisbhR1oTmxNFhdUCRs5YtyW1SGimZCy__iUVkV1NjrnVsPRdvvA0lQAGNon0XnfyptoddzP4v8w_uxN6_wbExWZn_fRT8JanNBAi0Y__dzLlLSj72BR1xQ0dg7hcMvXq8lrZV_jxcAC68UjCDKqBbZeFnItIAOiLcwHAVNWkdlH5vWhcO_i5NblYAvnkzwomWxgP-cKOu9sUvSvH5LWQuNBa4t9TTQV6EM08R26D18WEAOuEkJ81H6gTGFdpwiWSqEEt92lCiXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIQPF6MZ-KwaU9m4ls8DWtfR_dU7r6bfXKPOpkvXlnuqwVutvW9TnEBbKu5seBZy9mX1z0ieLf7eo83167MBD0Q9Z6WIguro1Z9cwA3bBonNh8IF1f79B_nhV_RsCBbrzqQlYs3WWARrl6B9t4hMckvCb9Yv4lUSQsTVIpzDe0Hlt9KaajiRPAmSC_UTGCXsRjNwXa2CIJo7y1gGSVENus1ID53-1mjng7YQkoRSzdAUuducLLEHU8SBecwLwenm4vJNvD2O0BLJD1EiigJ3bZswaiMp972Ls6Espqzu3I5xhgCf2TAo3IntB9VjHahP6M0_fMny-Jv98o97liE4Kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌ وهوای نجف، ساعتی قبل از آغاز مراسم تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/668211" target="_blank">📅 05:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668210">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13d536d20.mp4?token=pBfMVvIMjc68cGey4ytlUQ32s44koboFAKYUyfAj00XtDzOrejCYUDnbZx1MzaQV5b46xItdCoubZxNcUGMW_w-JWx051alkpw4GeqeOPQnULqzagdqF-NbswoLyaDgBphxKmxWL-c0EXHRld41WQQNp2SUzYjjUpXKSIWyrO03v5kSE4YQMmiHIyhp1TqO2UWFt6p4qgDqQlkC_lrolOEIzOE5SkzfoNqpRDUark3VdDh3BVaXTszPpd41BldyZWpNBtsns8xjev3HXatBg84bkXcFVcMhqn1-E05nOx0ireZcdv7F6EFAO80s5GqMDdyMA0xAZWVpjctocM5pDZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13d536d20.mp4?token=pBfMVvIMjc68cGey4ytlUQ32s44koboFAKYUyfAj00XtDzOrejCYUDnbZx1MzaQV5b46xItdCoubZxNcUGMW_w-JWx051alkpw4GeqeOPQnULqzagdqF-NbswoLyaDgBphxKmxWL-c0EXHRld41WQQNp2SUzYjjUpXKSIWyrO03v5kSE4YQMmiHIyhp1TqO2UWFt6p4qgDqQlkC_lrolOEIzOE5SkzfoNqpRDUark3VdDh3BVaXTszPpd41BldyZWpNBtsns8xjev3HXatBg84bkXcFVcMhqn1-E05nOx0ireZcdv7F6EFAO80s5GqMDdyMA0xAZWVpjctocM5pDZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موج حضور مردم برای شرکت در مراسم تشییع در نجف اشرف همچنان ادامه دارد و جمعیت از مناطق مختلف در حال پیوستن به این مراسم هستند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/668210" target="_blank">📅 05:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668209">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
قرارگاه خاتم‌الانبیا: تنها مسیر امن عبور کشتی‌ها در تنگه هرمز را ما تعیین می‌کنیم
قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
بی سابقه ترین رویداد و حضور مردمی در تشییع و بدرقه قائد شهید امت اسلامی، شکست خفت باری را بر استکبار جهانی و آمریکای جنایتکار وارد نمود.
🔹
ارتش تروریست آمریکا بدون هیچ گونه پایبندی بر تعهدات خود و در شرایطی که پیکر مطهر رهبر شهید مسلمانان و آزادگان جهان میهمان مسئولان و مردم سلحشور عراق می باشد در تجاوزی آشکار برخی از نقاط جنوب کشور عزیزمان ایران را مورد هدف قرار داد.
🔹
نیروهای مسلح جمهوری اسلامی ایران به تجاوز و اقدام تروریستی آمریکا پاسخ کوبنده‌ای می‌دهند و تحت هیچ شرایطی اجازه دخالت در امور تنگه هرمز و مدیریت آن را به آنها نخواهند داد.
🔹
مجددا اعلام می گردد تنها معبر ایمن برای عبور و مرور کشتی‌های تجاری و نفتکش در تنگه هرمز، مسیری است که جمهوری اسلامی ایران آن را تعیین کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/668209" target="_blank">📅 05:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668208">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
سنتکام مدعی پایان حملات به ایران شد
سنتکام:
🔹
ما دور دیگری از حملات تلافی‌جویانه علیه ایران را تکمیل کرده‌ایم.
🔹
ما بیش از ۶۰ قایق کوچک و بیش از ۸۰ سایت را با مهمات دقیق هدف قرار دادیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/668208" target="_blank">📅 05:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668207">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b85abc28.mp4?token=jleDeYC6BkZlNdn3cIRZpbkGyj9vr8ZsIGrIOkLcx2J4o9Olejcswi0xUo7Esar-dVWTuUoX8oaerf0OKRZjKZCEtcY88ALfsUZW_lIfaOevAQwWk9y6qDOFt66ea0nnA5MTvGD4g2m5dUIzkXhyAzsSkHb07XpT3nmVujEEdS1Af0iwuuJGpfLkHiF6s2Qd5mzsGpOH0VBCSLLUdqtxxRY64mhpEAZiMN8pLnQ_fjJo51-AXFFNkHLGOl02q8JxezpA5zVGDu_7PWfBdVkddxTB_KAtiqnMIgoZ9OtCHHI0JN7qIg7pYcfRQK2_h2xO9pmipq-hrVXRDGL-y4awTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b85abc28.mp4?token=jleDeYC6BkZlNdn3cIRZpbkGyj9vr8ZsIGrIOkLcx2J4o9Olejcswi0xUo7Esar-dVWTuUoX8oaerf0OKRZjKZCEtcY88ALfsUZW_lIfaOevAQwWk9y6qDOFt66ea0nnA5MTvGD4g2m5dUIzkXhyAzsSkHb07XpT3nmVujEEdS1Af0iwuuJGpfLkHiF6s2Qd5mzsGpOH0VBCSLLUdqtxxRY64mhpEAZiMN8pLnQ_fjJo51-AXFFNkHLGOl02q8JxezpA5zVGDu_7PWfBdVkddxTB_KAtiqnMIgoZ9OtCHHI0JN7qIg7pYcfRQK2_h2xO9pmipq-hrVXRDGL-y4awTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر نوه ۱۴ ماهه رهبر شهید در جوار حرم حضرت امیرالمومنین (ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/668207" target="_blank">📅 05:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668206">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجار در بحرین خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/668206" target="_blank">📅 05:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668205">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجار در بحرین خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668205" target="_blank">📅 05:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668197">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KwwYa9jZZV3ZOqBjtOecq97NqG7xCxwNkPgwAmEqqCI-I0UeiUvZC_9qmeJv0QQ_S3yWPVc351x7e1zp6J9xfTpMG-N1qL4IkJ2HglhCmGGl41DTGnOYB7KZBUWnJu6B7KrEbkVppxDHBcxsseI_qF_hq65lRj7cN3L5TtUtGwq1oDQqH4eyh58-CJPWlKt07DsgSxhQEWqzgFBzR8iD6eQZiGWvJ1r_qfikddM7vWYzw2lzaiXUPfnkUgnW73Quff10kqNiKLCu77Jf0dZ5xZqI6IDqyOE86zjNhpAVJo3UdTebEs-i4KjammCDs7rQ2vSVTL8pVz0EBDWNQ96KRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pem-k4Vp72bpCUTSXCMon9-rCeql-APXeKVxO40Ffr347cMjgTFmk1UtoY28KZv97a0rU-k99l0NdL81jw66ZQS0FbuQFrdePZX5NpMMSTsVP5-yKbpsY7LsWrlqgMVXC29yNtaDdlw87xJoV1VwGzgGh6RlC1IWzh8oVFKl7QJD21s5PMSXufKU7DwT0OAnHbRuAqx6O270R9BNsF4bfPYwTaXj6Ulj5wNtcl68izh5NYOdBKAgtMTMWWpq7EKbDcR2NGltCHLDKSTX6JCWC7If0FSI-qHit9hpa4z8fKcFdbU6iQB-NhvNKT9GXo65ERB8_k-0ELP2TtVKnnyZXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tBfdvkdpQHLixpdXsMd7mDpHM50wemhg5G71cKa7CXSTsf0z8lqZqEF0Sf1VOibusN29taCrIfjmIfGoKrDqOyed85DwkJbJxXZRBVR5RBx4TURDe7vPcz7BQAOp2cFUdS8486rWyoDr3HB1uPyq2ab_BlgE_jS1RMXjVSfTAxh0J7AcxGesx90ryAeWlHZF_rxlw86PjYV5SppVh8WmcPU9JIi5Rk-Ws-_zz4UUMocRaecDlqyuFcdIU9VNxXescXIwIlo7-gzTKQeZ1DbPmnJL80spg21MHm4i1kaX44EPMwYydUsxiJ8c1SrbxxqPXlWwWcy_5LTCMmMtnmzs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FgGnZyNJRtSrxUCUlABUJrz5fQTu0e5ymVSlT5p7uS7SmhR0CHm_bQBeW4wOMJtmgHSTQZa8x2VX7MPb2piUBFpxWVCr3UhOD8Bs-JpRvb1oAVHAZYpB0wcDFsHiKjEiNX1_BmNtGEQff8E_yfkZRYyUDi29KV3bYyNomGx_jm4doN9CQP__gJ_ayvZTEXXPyfRie34uvcaX4SFsyZGehccPh1cU2lnhMNd5Xspev5b0ZLc2AV69RLpJAG-dSDDBweCzO81_vs_qR0oYHiRS5rmI43-TFx-FagimOsL3cHKjUQkCOSmiNSxDgUmlDDYUIOyf1r1bRjFMuVIvPVA36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WP9Tn9qjBiVNQ1cy1JkvS5cBCME-mQkNspwpg4J3V8oFkbu3uOaBSrl10KUAQJcyXL4o1yNJQHpWGq7Ra8LQOysPfR-1JDf1S51iWusC7LI-BhYYvO-9rBrDiUOlopQBstBvVftnGmeuU2q_gLB7z3hk2ZIbPVPseue9lLd6mRKIHpvj0RLypHTJZPwUCnCsIzUvMvlyjYxYssvF-kkCkiXA32HkisJg9u_Cp_ZhfhjYchH1VPY-2_mowbQYtqSVdJNGcTEK3XFlm2s-InkKYRODEmO5mw-RFAUO9ypOdA9-Q9DkocAAZPK1V_4aruumggf2_K7iPIGR3F3lSKhQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d2OcCKGBFQZwjbzJyO7W7n5tSPP1UacpYPn1iKzJFElEkgjCe6xpEYXXEIc8Ihl0qu4NXKHIv3lKxK1N3svSqFVQeLwB_Hrw4jTilsuJ5Ybc8RjPtg-05-RXyPxodlZe4TmjZS8tTn1ByX94Yr2V7488T91rsYThPXWKiugrrPmGusO-iNSwAn1bDQP_ULnX3blQYAm-z7zM7mvDq189apuyl3mVnhV1-PXE5-Qeop6vazgW6zpTNWbfN_W7F9zYFidE_K9hEj6oEgT1YRgSbISoIBnCzwiawpDiPiJqmy23pplQ4ptGTbxulAnbTQy_Mzm2kklYrL-8DeT4RYM7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbasVtMeTchH8TwIYD1vUokvuKtx8qopj-iZitew68CotDP1j4dR750R60whngeM1XKb7weAC-oDFaigJddbSA0Qvf_GY-CEQRcscGUUgDFW5cdAIs5xyx8dHkLX7Lr6XMvJu-wgdcDxTIxhUj0gdh4Om81W2fhnylHF2RmSySzyWejogEjEZHIoUvtjulVeF1mmzUoUMR_kA87q7jGabXUp0ASZcKwxaB40rfHFc3yVnlJGGEgHl9prLGjYLS__YxGAHlL4mnxVR8fz4lEFA80hX6mvne4lUVn9fTF3gneg6BOEqK-Jf7jtyWfJzBR0oaVk8oi6Rpy6YkNpXtC5uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXuX0RwdBcBFGqWbKvC4i3wp_raomCHcX0sXJ_r1OT_hUsV3Gn-V9QD2u9lPEOgnrsrevfm5m6Z8VEw3owlvm4LrXCmI_STJOVzMzqCFeSO1wm3l1KmxaVcFHrO-4Q8YZi7EUiqzzH9kL6OdS9l9TN860yaQwcks_A8iEghw3NA1whHJJh5F3MDKfKoZdlrMaCqQUOIja30q8BbmBjDR8nZhwiSJVjCJ7tupB4ab-T7mIzJA5UyUQTDc9ptDwNTI1Yt8efv6R9lVAIKSUOlTU-VasefoQlf5O8OtcxAf4tEyT9CMgrYdbt47w1kmePeEA1Slva7fegtqcBy_YZgprQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از حال و شور مردم عراق در حرم امیرالمؤمنین
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/668197" target="_blank">📅 04:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668196">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac39b4df86.mp4?token=HAsE12gv4zZS9biAA3NhqoVaTfau30OQS53tNu9ZSztoj1XQgJ1_kc1Ios4KpxOck8nPpLxo1nldJ1Pl5vrQuVtxdzL3fdOP6LRzpwgPDttNRiySDiFnvmoy8yj7wJggnypMEBdeUPcyYU9QRgtzB2Ns2yswuuHtXIXqrUiTK9JyDg8VdMWXfnP8WclVbZ1VpMFZaCi4VovhjsU6Ks-boyy48OBQcIYT1IP4ji-xFhL2YpkggDXRrRQ8lIFsdcwR1nWY_wqQggM-IpyBr2dC_y8A2CxakOW7sZMlPQjYiVnJAqHp036RrywO-ONLHarXLDd1UjTkwR1fOlXPHH85JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac39b4df86.mp4?token=HAsE12gv4zZS9biAA3NhqoVaTfau30OQS53tNu9ZSztoj1XQgJ1_kc1Ios4KpxOck8nPpLxo1nldJ1Pl5vrQuVtxdzL3fdOP6LRzpwgPDttNRiySDiFnvmoy8yj7wJggnypMEBdeUPcyYU9QRgtzB2Ns2yswuuHtXIXqrUiTK9JyDg8VdMWXfnP8WclVbZ1VpMFZaCi4VovhjsU6Ks-boyy48OBQcIYT1IP4ji-xFhL2YpkggDXRrRQ8lIFsdcwR1nWY_wqQggM-IpyBr2dC_y8A2CxakOW7sZMlPQjYiVnJAqHp036RrywO-ONLHarXLDd1UjTkwR1fOlXPHH85JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای اربعینی مسیر ورود عراقی‌ها به شهر نجف برای تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/668196" target="_blank">📅 04:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668195">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6519ae9688.mp4?token=CBjyj47QfIQdI6Q7Ia1g4oC6mzCgn3WTE6batEsnYk7MY2ArmXYnqDznV7xCPaTBfwZ_y64z-eySzIeTkJDI6qnWAgXCxRfy_-ydYgg5_HRnVw9S7-PbZ4i3zkDgVqembDssELpvGgzV94Rj3aKK2I95Xai6r_htDGncyjmIL6FcsKPibuGSqmzBJ_4WUDOkM2ax8BWHG5xfkM3zbnqbtH2pTUcuR3nIuWav_vGEVm9aHfrmg7rB8nI4kpRF50KMbRGOaNFzEcIqLdmBRRMK5db-SC0TwWSYZsOvGZTeq_pNze7jwQXnobrPNbu2Acf2tG3W_h6Fek5T5EAOUUUNLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6519ae9688.mp4?token=CBjyj47QfIQdI6Q7Ia1g4oC6mzCgn3WTE6batEsnYk7MY2ArmXYnqDznV7xCPaTBfwZ_y64z-eySzIeTkJDI6qnWAgXCxRfy_-ydYgg5_HRnVw9S7-PbZ4i3zkDgVqembDssELpvGgzV94Rj3aKK2I95Xai6r_htDGncyjmIL6FcsKPibuGSqmzBJ_4WUDOkM2ax8BWHG5xfkM3zbnqbtH2pTUcuR3nIuWav_vGEVm9aHfrmg7rB8nI4kpRF50KMbRGOaNFzEcIqLdmBRRMK5db-SC0TwWSYZsOvGZTeq_pNze7jwQXnobrPNbu2Acf2tG3W_h6Fek5T5EAOUUUNLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وداع عراقی‌ها با پیکر مطهر رهبر شهید انقلاب در حرم امیرالمومنین(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/668195" target="_blank">📅 04:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668194">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/283cfe7718.mp4?token=rbINENQ0Wg4TWbODqNa9RuPMw24Z1A4CKqFdr1rlA4WZRwgaHxmRN_WMVKyUVebi0pAV5OShUOcjzRZJJT9oqHNSDk2Xg2n6uVH-1HkTZZqVvDjP2892dzovB1B_GxNmxb7ZZM16Ziyj8iTT8g4YV8cMjgAD7oLUU8LuA4TaaMfA0hg9v1yUW8y8QUdCSlkp3gLWokpSlFzLrc6qNA49UbzFElbQ6Ne8JKKU4XAONrTo2X4cf4Uk-hm8QBbor8knXTgmGmsnNcSHd4lr5dlPsaJBS3iFirZAh5_f81GItf5XhWKLNpky6s3ggIg7zklkJ1gyotHVIS6YWYubuIZ2iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/283cfe7718.mp4?token=rbINENQ0Wg4TWbODqNa9RuPMw24Z1A4CKqFdr1rlA4WZRwgaHxmRN_WMVKyUVebi0pAV5OShUOcjzRZJJT9oqHNSDk2Xg2n6uVH-1HkTZZqVvDjP2892dzovB1B_GxNmxb7ZZM16Ziyj8iTT8g4YV8cMjgAD7oLUU8LuA4TaaMfA0hg9v1yUW8y8QUdCSlkp3gLWokpSlFzLrc6qNA49UbzFElbQ6Ne8JKKU4XAONrTo2X4cf4Uk-hm8QBbor8knXTgmGmsnNcSHd4lr5dlPsaJBS3iFirZAh5_f81GItf5XhWKLNpky6s3ggIg7zklkJ1gyotHVIS6YWYubuIZ2iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقامه
نماز بر پیکر آقای شهید ایران در حرم مطهر حضرت علی علیه السلام
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/668194" target="_blank">📅 04:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668193">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4164e246.mp4?token=HtPSohcRTxL8ferwTyHDta5ILhv7aLikmnjiqW8Be_hFHeJrGrOw67TGyFUmfMUfYbHfKMuchnoSrFVPTSEr4qpjwaOXS3k5RR21AEF8FKUKyDuwEmc3e74qeiqoVaunBIvtvnHQMGurn1mNuyPx-PhmB7BEZJSJY6eWnLCIdDw8oPMDg9kD32AcQiYRNd0KSHlaSpmvAj2Nu_COZA_T9PKna8GGu2h5iRu8Vd7RNVeNKZKgAsJEOzs8f-6jQxUEhZIdtgfde0PBdup0FC_DQGMNdaNyoHd08BcuD8EQfBj8SUz71VJqGxBwOfb4fHpY8qSzJMZ7_M4gxTgZiMoLGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4164e246.mp4?token=HtPSohcRTxL8ferwTyHDta5ILhv7aLikmnjiqW8Be_hFHeJrGrOw67TGyFUmfMUfYbHfKMuchnoSrFVPTSEr4qpjwaOXS3k5RR21AEF8FKUKyDuwEmc3e74qeiqoVaunBIvtvnHQMGurn1mNuyPx-PhmB7BEZJSJY6eWnLCIdDw8oPMDg9kD32AcQiYRNd0KSHlaSpmvAj2Nu_COZA_T9PKna8GGu2h5iRu8Vd7RNVeNKZKgAsJEOzs8f-6jQxUEhZIdtgfde0PBdup0FC_DQGMNdaNyoHd08BcuD8EQfBj8SUz71VJqGxBwOfb4fHpY8qSzJMZ7_M4gxTgZiMoLGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طواف پیکر مطهر رهبر شهید انقلاب بر ضریح امیرالمومنین(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/668193" target="_blank">📅 04:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668192">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfbc9752c8.mp4?token=RvB0x6oM7Ml6QEIDr30-tHUTjk3iKggry92ha_D-dwf5sPdydyqml6vILZEs4_dKGwel79ks7K28IoF5f6jgL6dIA4nvpQ-rKWu3hibVjmXH8723C6goaXAM27j-eoEqS27zI5BDrMlfZJCGdFD5aaNphCwplO1VOjnJiZYLX6_txOAcZ1Dxp-1GIfUHcXydVDK1vySCrA701Df1ZTZyyXudlKJGJvRbZRoHjpiJv8gUzgSMwNzKB3nop9A-ON6gBu0EsTR0SC2YHhSGFxTDLMMDYsuZz-NHiSeKCR_FMItVBdGH65UV_21M1ffSjAp-M-TzkMMZJigtRe_PEvhWYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfbc9752c8.mp4?token=RvB0x6oM7Ml6QEIDr30-tHUTjk3iKggry92ha_D-dwf5sPdydyqml6vILZEs4_dKGwel79ks7K28IoF5f6jgL6dIA4nvpQ-rKWu3hibVjmXH8723C6goaXAM27j-eoEqS27zI5BDrMlfZJCGdFD5aaNphCwplO1VOjnJiZYLX6_txOAcZ1Dxp-1GIfUHcXydVDK1vySCrA701Df1ZTZyyXudlKJGJvRbZRoHjpiJv8gUzgSMwNzKB3nop9A-ON6gBu0EsTR0SC2YHhSGFxTDLMMDYsuZz-NHiSeKCR_FMItVBdGH65UV_21M1ffSjAp-M-TzkMMZJigtRe_PEvhWYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر امام شهید در صحن حیدری شریف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/668192" target="_blank">📅 04:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668191">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
شلیک موشک از ایران به سمت ناوهای آمریکایی
🔹
رسانه «میدل ایست اسپکتیتور» بامداد چهارشنبه مدعی شد که ایران چندین موشک ضدکشتی به سمت شناورهای جنگی نیروی دریایی آمریکا در خلیج فارس شلیک کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/668191" target="_blank">📅 04:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668190">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293c50bc2a.mp4?token=tVJDpHqBo_hMlrZhyjQsYLTTEXnGlTV_IymlMEHa08Q27NspZZn8kuY96GXVdDECkxRFIEOuG_G1OjaH4i_a4z-aADTxElhRHnuQggvZgJ1tNrVt_Qzdf7JATYGuzjA-zbMm7WwmODDlN9T51aTfwuL6sMfajVgfrTf71xNgmdH2dD9sEC-G5mXm4myWBdu8w7QxrAGm6jTF88bxwAr71Y6gPa3KuFNRaGBBDEe3dZX2GExWjSHKixMz6E5Nn6khN2WU-X1CozyUfHfK09YI2tLMcURM2f-GyL6ufnMP0DxYj8GK12CXWOcGve74gw2_ercwnRRddTxwCoK22HG2VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293c50bc2a.mp4?token=tVJDpHqBo_hMlrZhyjQsYLTTEXnGlTV_IymlMEHa08Q27NspZZn8kuY96GXVdDECkxRFIEOuG_G1OjaH4i_a4z-aADTxElhRHnuQggvZgJ1tNrVt_Qzdf7JATYGuzjA-zbMm7WwmODDlN9T51aTfwuL6sMfajVgfrTf71xNgmdH2dD9sEC-G5mXm4myWBdu8w7QxrAGm6jTF88bxwAr71Y6gPa3KuFNRaGBBDEe3dZX2GExWjSHKixMz6E5Nn6khN2WU-X1CozyUfHfK09YI2tLMcURM2f-GyL6ufnMP0DxYj8GK12CXWOcGve74gw2_ercwnRRddTxwCoK22HG2VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیت انبوه در حرم امام علی علیه السلام در انتظار تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/668190" target="_blank">📅 04:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668189">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkcXN3Kzsqc-_6cvIoqpacId8cn2MhBYmVgeDrcrRik2MHXaXXKnno-2wDMeZd2ZxKq4uZww2LarrxEt0b6dbEHp675G39zWx-jFMKrvJEGRduKxDSIKtIp82Bwpv71iLKh5usJHErwTSesnWoRevVdDPD-K_4zGuH3j5GE7ZDCA1dXcE1Gxy_1_KT0_phP6iofIHJ8GNsz-kXjnez-kExZqIrSXGqo0eUeqGvzQU0cejxQJHh2zxv5kvwJJjFYWoh0Nl4H1mgnQ8wW6qvXaudyrDA3zO_7VkkFmGQzdINLvmc0qPqsQcaxAtFascAIkGfGOPWgWCS4Tsuar2TSsAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرژانتین و فرانسه در صدر تیم‌های با بیشترین گل زده تا به اینجای مسابقات جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/668189" target="_blank">📅 04:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668188">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
پزشکیان عراق را به مقصد ایران ترک کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668188" target="_blank">📅 03:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668187">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b564605731.mp4?token=DsjU6aP2Xzz_7MA14x6Bs6tcNaUQGYIWgP76tSRimrY8oeFUVee7KNTfsS8vZmpgyEBa80qgzyS0A-v_Vv9-ovMPPxOIGu311PUPnOcNQwdUn5z7xs6v6x-iqCu_YQB5wuNs6z6QG0Ul5GzvtHT9Wzq6O9Et0NkJRTbEdmm9A9dv0hCAWIHsWakmP6AyIjIbRjOYEuHax04htz5qiXweMbkjrjlBqvFlgtS25MYpyA5kpyZusgFBB2CfioHwztOAeuC2DFPze4xQhNlT9XQlKYeNcCpsXVxBZB5N2pU2r3ZZzNzKMQa7dLQb4jt_8pBrqcjhSTHdB0wXMZ8HqCqjGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b564605731.mp4?token=DsjU6aP2Xzz_7MA14x6Bs6tcNaUQGYIWgP76tSRimrY8oeFUVee7KNTfsS8vZmpgyEBa80qgzyS0A-v_Vv9-ovMPPxOIGu311PUPnOcNQwdUn5z7xs6v6x-iqCu_YQB5wuNs6z6QG0Ul5GzvtHT9Wzq6O9Et0NkJRTbEdmm9A9dv0hCAWIHsWakmP6AyIjIbRjOYEuHax04htz5qiXweMbkjrjlBqvFlgtS25MYpyA5kpyZusgFBB2CfioHwztOAeuC2DFPze4xQhNlT9XQlKYeNcCpsXVxBZB5N2pU2r3ZZzNzKMQa7dLQb4jt_8pBrqcjhSTHdB0wXMZ8HqCqjGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور اقشار مختلف جامعه عراق در مراسم تشییع پیکر رهبر شهید امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668187" target="_blank">📅 03:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668186">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2567d64ec2.mp4?token=XGaLwORlVOsujhgGO04qQinr93YV30ZcydiOl6cqnTfhw36SO_dtKBb308vSy95nEHdyH92mCpCjcjR4HdMK6aXZg3WEGWp_sipmyO_SpaohsD7d95aYmQl8J6jn5QHI9DQCAIpQklu1qRjE3Qpzvpl4CZXL_PTvQI7krDkC84uSaDQaXYFusM4oLGVkDT6lGwDw5WUlrsHki4egx-vXVMMelhFdhW2Ytc1snC7hWO1XvOb_1d0kS9-pt88qFlB8MV9UtN69NPscFJ3LVKxXFtXPbXWTQ8RsRFYCH1PPvjTFl-wnNQzj5-ye5881nr7XlV0bggcjiKCS57HtzJ8wEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2567d64ec2.mp4?token=XGaLwORlVOsujhgGO04qQinr93YV30ZcydiOl6cqnTfhw36SO_dtKBb308vSy95nEHdyH92mCpCjcjR4HdMK6aXZg3WEGWp_sipmyO_SpaohsD7d95aYmQl8J6jn5QHI9DQCAIpQklu1qRjE3Qpzvpl4CZXL_PTvQI7krDkC84uSaDQaXYFusM4oLGVkDT6lGwDw5WUlrsHki4egx-vXVMMelhFdhW2Ytc1snC7hWO1XvOb_1d0kS9-pt88qFlB8MV9UtN69NPscFJ3LVKxXFtXPbXWTQ8RsRFYCH1PPvjTFl-wnNQzj5-ye5881nr7XlV0bggcjiKCS57HtzJ8wEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهیدان سید محمدباقر صدر و سید محمدباقر حکیم، حالا میزبان آقای شهید ما هستند...
🔹
تصویر نصب شده در نجف اشرف به مناسبت ورود پیکر مطهر رهبر شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/668186" target="_blank">📅 03:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668185">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bce9bc8fdb.mp4?token=UWm1VlE9_1_MipI3pyH-AAoibxk6bfsK5MnYhGNY5hef31xnCaUtdV1Pl-hKj-F_dkcn6W1XANg2SArbOxsv6l6RlD7LAL2pxix_yIYSlU2xPwAm07wX1_vKeby7ZZnr23fCND8UJzpNes3eJHEreF2uTB4pmZUXeLb0VjEtGJSMP8c93GMnd2OXdFHmO6jmUeszBbcw_4WtyRiMaEweNgGJTytP8hEi5yi97N7UAaRoptupLwuzPQSECnbePy43hk7dujhNDrFOv8qXGZfzNeZvFZtEV12LP_DDMVdF0Knr60LaJLFltZcIX6m3-gT_NLb67uKlxkJ9CcfGj3w0vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bce9bc8fdb.mp4?token=UWm1VlE9_1_MipI3pyH-AAoibxk6bfsK5MnYhGNY5hef31xnCaUtdV1Pl-hKj-F_dkcn6W1XANg2SArbOxsv6l6RlD7LAL2pxix_yIYSlU2xPwAm07wX1_vKeby7ZZnr23fCND8UJzpNes3eJHEreF2uTB4pmZUXeLb0VjEtGJSMP8c93GMnd2OXdFHmO6jmUeszBbcw_4WtyRiMaEweNgGJTytP8hEi5yi97N7UAaRoptupLwuzPQSECnbePy43hk7dujhNDrFOv8qXGZfzNeZvFZtEV12LP_DDMVdF0Knr60LaJLFltZcIX6m3-gT_NLb67uKlxkJ9CcfGj3w0vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری عراقی‌ها در کربلا و دعا بر آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/668185" target="_blank">📅 03:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668184">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52d30bf222.mp4?token=KIlyXA6LiJYCsl0odDa6PkhNsA0a91edkol3m3T9TdWz_qlx1C10XkdQWo4UPwsdtnV_dIdGXZS72GmxdlO8yqS0HOyqIafxvUiruQBnq1urwUkeQ07U0t9wfSmBHDndWuosN7Cgo_WDYPmD0W_84Qp-jg7rxZqcdm4qJL7L6U5kmAZSKLs3Yu0FMFlb6GiFG87vRd3L65AvlBQHSBwzsUaLmDm-cMW7VoVGAZuoVSsie11gcU7IAk55nD6av8LMsSvZb1ttUTCofioLPs72nzOnkOEIFjsJNtu98Mrp2WwlZ_TxJz4EIJgstm9CEBATdv-sBKaJiIKjfXm7iSqbDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52d30bf222.mp4?token=KIlyXA6LiJYCsl0odDa6PkhNsA0a91edkol3m3T9TdWz_qlx1C10XkdQWo4UPwsdtnV_dIdGXZS72GmxdlO8yqS0HOyqIafxvUiruQBnq1urwUkeQ07U0t9wfSmBHDndWuosN7Cgo_WDYPmD0W_84Qp-jg7rxZqcdm4qJL7L6U5kmAZSKLs3Yu0FMFlb6GiFG87vRd3L65AvlBQHSBwzsUaLmDm-cMW7VoVGAZuoVSsie11gcU7IAk55nD6av8LMsSvZb1ttUTCofioLPs72nzOnkOEIFjsJNtu98Mrp2WwlZ_TxJz4EIJgstm9CEBATdv-sBKaJiIKjfXm7iSqbDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار هیهات مناالذله عراقی‌ها در حرم حضرت امیرالمومنین(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/668184" target="_blank">📅 03:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668182">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe2e701a0.mp4?token=S52PmKkU07mEPqBjXqwsCelmB7k9-orMnqU7po8bDRetftRxBhob5j5K-JDknHH9sEwgpirV7_8NxII3rBPB2Suk-66_kKeaDURKVtPqWG7Qb1U-rMsFJjjV-vnpLwsvSCghxmG9nHo4CYdPxDABbojnnEM2CuTOtcomAkV_a3uU1jiqI2CVIzSvarRGg3l-2sk0LbOJ9V8tGdJFLW115Ftv90soTUHhYvg5LY9jaKjmQlnZmc8GLWnV4uQ25huEGFfTWx6fWRreloBgXfT0HBpp0XkMCh3hFRWJhCHoZzusLVoyEJzvlBccaSb21d8WFRVkVHkts74Ylvg_7wPBAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe2e701a0.mp4?token=S52PmKkU07mEPqBjXqwsCelmB7k9-orMnqU7po8bDRetftRxBhob5j5K-JDknHH9sEwgpirV7_8NxII3rBPB2Suk-66_kKeaDURKVtPqWG7Qb1U-rMsFJjjV-vnpLwsvSCghxmG9nHo4CYdPxDABbojnnEM2CuTOtcomAkV_a3uU1jiqI2CVIzSvarRGg3l-2sk0LbOJ9V8tGdJFLW115Ftv90soTUHhYvg5LY9jaKjmQlnZmc8GLWnV4uQ25huEGFfTWx6fWRreloBgXfT0HBpp0XkMCh3hFRWJhCHoZzusLVoyEJzvlBccaSb21d8WFRVkVHkts74Ylvg_7wPBAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودروی حامل پیکر مطهر رهبر شهید انقلاب به صحن حضرت زهرا(س) در حرم امیرالمومنین(ع) رسید.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/668182" target="_blank">📅 03:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668181">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای اکسیوس: یک مقام آمریکایی گفت ترامپ طرح حمله به ایران را تأیید کرده و
امروز، در حالی که برای نشست ناتو در ترکیه حضور داشت، دستور اجرای آن را صادر کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/668181" target="_blank">📅 03:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668180">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
جدیدترین جزئیات مناطق مورد حمله در جنوب ایرا
ن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668180" target="_blank">📅 03:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668179">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6976fab17.mp4?token=F4Dfj3Q0DxD-LkgoGtaK_K99jYgbaVEtQ20SrW8dVHdmv2DHflj_Qz9tnDLk3TX79xM6Ncon7o5Bfyd7gbHphkV5k1Ns1mB1TISlgraPM1szYFuJzQ6TDqYnchXvFLKVHl0KMSPVzhnOGRu-9sovGX9NLi7YEnDGC-FcveZYs3BfHlRgU-nrmmb8Pdf0Egma48-HDNDMj2uaVRZaJz9OYPnDeWBCjToSuWnP2scj1GhjJvYSu4GTc_INVu_LLcOjmlHipiXDj8qw8Mv7gfRapDUjMjIb3nnYsJvRUH2CYXRKBknRQl3puA-ppVdZKkWZXeFnogw6FIERnJtQfWKVcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6976fab17.mp4?token=F4Dfj3Q0DxD-LkgoGtaK_K99jYgbaVEtQ20SrW8dVHdmv2DHflj_Qz9tnDLk3TX79xM6Ncon7o5Bfyd7gbHphkV5k1Ns1mB1TISlgraPM1szYFuJzQ6TDqYnchXvFLKVHl0KMSPVzhnOGRu-9sovGX9NLi7YEnDGC-FcveZYs3BfHlRgU-nrmmb8Pdf0Egma48-HDNDMj2uaVRZaJz9OYPnDeWBCjToSuWnP2scj1GhjJvYSu4GTc_INVu_LLcOjmlHipiXDj8qw8Mv7gfRapDUjMjIb3nnYsJvRUH2CYXRKBknRQl3puA-ppVdZKkWZXeFnogw6FIERnJtQfWKVcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی حیدرکرار انتقام انتقام
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/668179" target="_blank">📅 03:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668178">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62c1a1ba88.mp4?token=i8O3uk6UR5nJ21gskMFb-WVVKGzDZ9bTa_s7Ts1UyI9y11UgJb3i_SsWd-AX4pTJLMDfe60hkW3S4iARFOWPFD1bdBddHSxOiDPqjaIUmelI0Uez0U6DpvozwVvWW5OzaLWeEq0-WpXLnDPPTro4PzyoZti4Sr-txGQOXZInTnBt5glg-afG5CawbdKyAWJShT7NnAclagwjUcPtCYYB-v_Lap7dEstXXUMVjet0pGSiuk5cgx_Rze0sULUvtoiTXfXUhYGtQepUlQ3tPsVBQI52PpuuQN8Qp9n0E2K5Enm6ybsLJWy_Fqf9qaYvFJFe3fCpZCto671a5CYZnXgoOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62c1a1ba88.mp4?token=i8O3uk6UR5nJ21gskMFb-WVVKGzDZ9bTa_s7Ts1UyI9y11UgJb3i_SsWd-AX4pTJLMDfe60hkW3S4iARFOWPFD1bdBddHSxOiDPqjaIUmelI0Uez0U6DpvozwVvWW5OzaLWeEq0-WpXLnDPPTro4PzyoZti4Sr-txGQOXZInTnBt5glg-afG5CawbdKyAWJShT7NnAclagwjUcPtCYYB-v_Lap7dEstXXUMVjet0pGSiuk5cgx_Rze0sULUvtoiTXfXUhYGtQepUlQ3tPsVBQI52PpuuQN8Qp9n0E2K5Enm6ybsLJWy_Fqf9qaYvFJFe3fCpZCto671a5CYZnXgoOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابان‌های نجف اشرف قبل از وداع با رهبر شهید امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/668178" target="_blank">📅 03:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668177">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4d8e44b3.mp4?token=t4W84x7yWNpSK_OEnpyLq8dDAqcBTQil1wXnnvWxZXY_TXTp5n9lazrSrxiGzM09yaO26og3YTTQruEkEAGT3214wYSSfezFpZpxYgktWT09fWYaHPGy12yU1sZxLiw_xjqnHCjVgm9wK36txDYYHgKm8GXl6Mq9afduMVJsEdFadKPD9rCiZ-PjZIUlua5NYZgzBokh_RBBgoUDOyE5yMqxxzHidj0SWGSYcuOv2p9NGgdQS_BQTbQCkLBMgVIHeod9M6FOWAHdUyV_I4JcQugkAIvu3X3jKoEc6FrPZLE84Km4lp4BHpdd910DKKJq_EJJhLwBiHOUVCOmMUMoXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4d8e44b3.mp4?token=t4W84x7yWNpSK_OEnpyLq8dDAqcBTQil1wXnnvWxZXY_TXTp5n9lazrSrxiGzM09yaO26og3YTTQruEkEAGT3214wYSSfezFpZpxYgktWT09fWYaHPGy12yU1sZxLiw_xjqnHCjVgm9wK36txDYYHgKm8GXl6Mq9afduMVJsEdFadKPD9rCiZ-PjZIUlua5NYZgzBokh_RBBgoUDOyE5yMqxxzHidj0SWGSYcuOv2p9NGgdQS_BQTbQCkLBMgVIHeod9M6FOWAHdUyV_I4JcQugkAIvu3X3jKoEc6FrPZLE84Km4lp4BHpdd910DKKJq_EJJhLwBiHOUVCOmMUMoXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درهای حرم مطهر امیرالمومنین(ع) به‌منظور آماده‌سازی برای استقبال از امام شهید بسته شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668177" target="_blank">📅 03:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668176">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffdade163.mp4?token=l0XagTPd4p2KO2NelmH_UWMcjzGERP7BZd-NCDIO-0bHOg2D-4_iaKj3Knz2-A050jhqzLDEZo_2fbE_JG6wLTnAGgIfE_-4DAJYKsmlIkieRCZ2fTBAYvO9RFropwpFIhadF6drTdP0G59ymuRgplMujarz8EFtVU2GCMhkD_YgWIET8q2BSMXOjRHMqBM6inlg6MdTvfyKSnhQ2jlTu6D4Uc-ddB-IorM3fweQLUJDZ46jZFaqi-Z8IdlyLuAdJZ46lI_pwt2g3EapNHgJtRfYRgK106GITkHEnRiz5XfsFnCyxc3qO2LoqvXeML7bRDu99YxTVEawqWraNvB7iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffdade163.mp4?token=l0XagTPd4p2KO2NelmH_UWMcjzGERP7BZd-NCDIO-0bHOg2D-4_iaKj3Knz2-A050jhqzLDEZo_2fbE_JG6wLTnAGgIfE_-4DAJYKsmlIkieRCZ2fTBAYvO9RFropwpFIhadF6drTdP0G59ymuRgplMujarz8EFtVU2GCMhkD_YgWIET8q2BSMXOjRHMqBM6inlg6MdTvfyKSnhQ2jlTu6D4Uc-ddB-IorM3fweQLUJDZ46jZFaqi-Z8IdlyLuAdJZ46lI_pwt2g3EapNHgJtRfYRgK106GITkHEnRiz5XfsFnCyxc3qO2LoqvXeML7bRDu99YxTVEawqWraNvB7iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یزلۀ جوانان عراقی در سوگ رهبر شهید انقلاب در بین‌الحرمین
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/668176" target="_blank">📅 03:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668175">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c0b2f180.mp4?token=syZarHVUVsoWtcw9ikMyLtqUVEqowwQJYAE_kjYeQk-GF4p6o49biogbqZDe3Qu755H56k1aVNV6pTmxlAAgdoD5zXljnixhaTbO7jV7ywmGtMHbGcr8fLeYhi2kYswsaYml4N2wLU1FnwK6aNL_OUdbrJ20y9uxiKmhNtpyq5d0k4XgOGUOy7GojLF88iklPRXkL8as3Tjm_BvUPlJtrVDzMJX3kfUOPGlkST8x2Uoo4fUZN0ooAwxxDn5WT5QWE0GHNltcIf8aLTI1lXsF_2cgOyMJWeBQYj9X_RETnvJ2WRKOlJ2Pk1_iJ_Qn3nT6PXZaZpOdZXupL9_Z4Bdtuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c0b2f180.mp4?token=syZarHVUVsoWtcw9ikMyLtqUVEqowwQJYAE_kjYeQk-GF4p6o49biogbqZDe3Qu755H56k1aVNV6pTmxlAAgdoD5zXljnixhaTbO7jV7ywmGtMHbGcr8fLeYhi2kYswsaYml4N2wLU1FnwK6aNL_OUdbrJ20y9uxiKmhNtpyq5d0k4XgOGUOy7GojLF88iklPRXkL8as3Tjm_BvUPlJtrVDzMJX3kfUOPGlkST8x2Uoo4fUZN0ooAwxxDn5WT5QWE0GHNltcIf8aLTI1lXsF_2cgOyMJWeBQYj9X_RETnvJ2WRKOlJ2Pk1_iJ_Qn3nT6PXZaZpOdZXupL9_Z4Bdtuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای خیابان‌های منتهی به حرم امیرالمومنین(ع)، ساعاتی پیش از آغاز مراسم تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/668175" target="_blank">📅 02:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668174">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
سی‌ان‌ان: وزیر جنگ آمریکا روز چهارشنبه به اسرائیل سفر می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/668174" target="_blank">📅 02:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668173">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
صابرین‌نیوز: هزاران نفر از عزاداران عراقی در پارکینگ‌ها منتظر هستند تا وسایل نقلیه برای انتقال آن‌ها به کربلا فراهم شود تا در مراسم تشییع پیکر امام شهید شرکت کنند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/668173" target="_blank">📅 02:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668172">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cc907b68.mp4?token=LsES1L1pX0KUKOowCmHrqy_dWnkKpGThTZrIwMbs3m3g7HQxgtm931FUqHiTJI3yEfOjRxRJCwJDG-WhImeyCHzQAD54t2gj3J88n4kybxJ6GTxD1jXTkaMW6jpTz9A-n1e_D2Zmt-_iiOaDvZhnP7UWAMGERMMTDyhjKSvQhV03mpNAIVwHv_4BLYiHteU1Hgx_XBdCIzuFfR1RJ-k5xcNVjQXEvxqT8CvdB2SSSjXjUVfyQPfjE7TFsUh_3fERYX81KOdyvSNfYyHW2a7vZVpz7FLjHwyrz8DtQFo73G38ciyiEF0KLnqAuisHIMKRb2qX1x9sAw2RsAAMFhEgGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cc907b68.mp4?token=LsES1L1pX0KUKOowCmHrqy_dWnkKpGThTZrIwMbs3m3g7HQxgtm931FUqHiTJI3yEfOjRxRJCwJDG-WhImeyCHzQAD54t2gj3J88n4kybxJ6GTxD1jXTkaMW6jpTz9A-n1e_D2Zmt-_iiOaDvZhnP7UWAMGERMMTDyhjKSvQhV03mpNAIVwHv_4BLYiHteU1Hgx_XBdCIzuFfR1RJ-k5xcNVjQXEvxqT8CvdB2SSSjXjUVfyQPfjE7TFsUh_3fERYX81KOdyvSNfYyHW2a7vZVpz7FLjHwyrz8DtQFo73G38ciyiEF0KLnqAuisHIMKRb2qX1x9sAw2RsAAMFhEgGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم اکنون «میدان الصدرین» نجف اشرف با شعار: یا سید فراموشت نمی‌کنیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/668172" target="_blank">📅 02:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668171">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3Tj3eKVcohBoRKZ-u3Zb0kKl3Wv9D4Up-DGwyyF6H1-t6Ysmj29nokJA6OHunZDDruGcBxg_82eCC_aswTkV27ZSeaTQMoX5pcE666jPkkaXQaJQ76QDB8-dXzjKt7s49R6VZ88RIXhlsnxtu-Zy4-QYAwIKX8uYgKq3yZkv5UB4aujvgA67PCSPBflBle7vQUULhsnJwTzvbQVtUHVtmYFFFejKrNDyF6v-3EF1EAFCW8x3oMdDIujr1L-4HdXrvjWu4GnXH4H_yBs1w_kMC3nHszeBTNayfWAlATNYSUw4xOHiOWtxapU4L0k91m1dkbKptv_M_Rn8gbLhjYvRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
خوشامدگویی متفاوت عراق به قائد شهید: «خوارکننده آمریکا خوش‌آمدی»
🔹
«هلا بجیتك، مذل امریکا و التطبیع: خوش آمدی ای خوارکننده آمریکا و سازش.»
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668171" target="_blank">📅 02:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668170">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80c67bdf1.mp4?token=Z7cecCQ84c_SGB1uY-wSLfXXRF_w7BekbDl-3EN5supAdF_rU97BrvoqRZf1C8c5KgmH_36dJm32onuiQMODCQi2MAH6B1lvOgTTcoi6ANYRrf_fAj-NgwbD6InoiNgQEvUZ9no4JNlTg-D78IImEIkM_zq5ARkSr1WBO5OZ7yHuZ2n6zw3b2s_VYUXwkEV9MXb4I41OLiPfyqEYSOo7Zqb6Nn3pJzmYV-OqXxQtoicwXFFop3RwagNvV6LJccihHhN5vvyRAyJ18D7XC51es1RUnBhX35N7r94kaj-REGGTWMiAvJ-YVW1hAUYBQx-9_oP1upfE62hvcDlPguebyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80c67bdf1.mp4?token=Z7cecCQ84c_SGB1uY-wSLfXXRF_w7BekbDl-3EN5supAdF_rU97BrvoqRZf1C8c5KgmH_36dJm32onuiQMODCQi2MAH6B1lvOgTTcoi6ANYRrf_fAj-NgwbD6InoiNgQEvUZ9no4JNlTg-D78IImEIkM_zq5ARkSr1WBO5OZ7yHuZ2n6zw3b2s_VYUXwkEV9MXb4I41OLiPfyqEYSOo7Zqb6Nn3pJzmYV-OqXxQtoicwXFFop3RwagNvV6LJccihHhN5vvyRAyJ18D7XC51es1RUnBhX35N7r94kaj-REGGTWMiAvJ-YVW1hAUYBQx-9_oP1upfE62hvcDlPguebyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از رهبر شهید انقلاب در خیابان‌های عراق
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/668170" target="_blank">📅 02:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668168">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCGz2_-Lu3xF5iE5GpWqObpLnihmT8x0UXEPdLKVtU3hhh2u33sfCzZYlsbvhRv584_vtHPjSZoQajilOWo04yz8dDfScY_SbOfthIX8WifgKuZszREZUb4IgrXYoFdtsVk5YPtrJRQ3C6XpDu73vMD_lXxuMuXfQ-c42DSC5r3snf8_pGIoNgdoC9C1wYfy4TKuf7qEIM7YHELSQE3I_wp1sX79O7GqTuawlAUWo6dhWQi0Zu_jn72yNwNDFmCnQUbGOYO_ajKkD1G3U1_r28KiP-eta5LaqOIX53dzJW9XoXUIOiOq7UT6u7Wz1dKjVNBz6ccJnJ0X-SA2VeXXuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xr_8qt1j8vaPIlrygMfP-EeyvrLJQ6upQ_OZ0WdIlp_0xOS9Gnv6yIS_YUaQL8pXi5IZt_65lcnaJraVdBuTDWd8X8y358nB02RNtASTa_zXiUhVdmT0UYnUUI2yGMWWB5P6_qmxrzMmr8lDQA0gdnvD3Ih3u3rqZkT64Hl1XthbsVBSVBcxcCZ7rKUpw7FWIprBvbMAb9CwZMf4Z93LHGBgItEvP16rm-0p0tALD35z8O1k3ZnnkyzV2zswPUjq5Dp8bxfed9aYdzypFlO0i7u0w5HFtaoq7BHDOmqN1QobChV9j1igtW3GVb7SGXYAAMQ0ftlfPjocnrKHD9OjbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر منتسب به آثار حمله جنایتکارانه دشمن آمریکایی به جنوب کشور
🔹
اصابت بمب رژیم تروریستی آمریکا به یک خودروی حمل و نقل عمومی در بندرعباس
🔹
ستون دود بندرعباس ناشی از حملۀ دشمن به شناورهای صیادی مردم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/668168" target="_blank">📅 02:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668166">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDQpbhGXQFP_oNJJU0GMFkS5HEq-LJuyCRO7Tds93eM8lrBTeK6sl_EIz6zOZzWjsLlfPDFy8OpO2T7nEIU2n1gYr3_-1h-O7jzKPyqb3kAarO3s4cfEzEt_cI8lcttCWCBTfCrgJzV9vfGXAw1-9rnH51N1nXQGU-YyUNqCr4WuGl6la2QJDNF2lSrDGYplgnwVwViAb_rdW6eG95nUQSkQlY0kFotajjZ2wsp1QBp72cI9jhJAIvNdri7pEEsbFWkYP81cSh7rrUS_f-uMpkA2kecW5qmVIj4rTUtNlfZbkFsRdUsbiXmFQtif0Fj_jB9MD7KeBNL-adKN_YGYvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0sstLduzFHLiefsrSaVcV-R6qyrdGP7QbnZgdrEk9jlBkFwRl1muKvmxAsfrlvBz93CjR7in-DRrB7mejcETx-BAcgVPHp1VNcFRhqBZA8am6ThbHAXP0EW3uylZSr70UKNnCYlw7D0Vc_310nGkh3a9SWvhZ6QYHhiACjmfDxKMlcCZYGz5OiTSM7NJfopFAItQJPtJmkI1ZDVgp_5utOFArGLjIwelvEQuDSRkTAAtXmXkAyArGLD6SF3ZprVMxyL-YbaJ1mHd28EaPRJWgvuN8zQwZ3R24L3_P8s0cu1H3UhRZF3JmI6SnIT6nZEtnSydE5s8LE5N6mbTLSgRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
استوری محمدرضا شریفی‌نیا و هادی چوپان به مناسبت تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668166" target="_blank">📅 02:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668165">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f11883d2.mp4?token=BUGfFhNsQLlWqI0RTcmw6NfXw91yaC0IC62YVhXe93C8KtnrKljC2jFZn-QShdx6nttzo9KyBUPFBu7e7LAt3aLStEnKZbyPT61VOvW45k6xlwfVtvvn8554Jmac_ssDUCU2veTj2v7XDQ-TrwXlI4uyc7SN7RiE-1-DMsh1A0phViGlwJBqtkvTMWcebk837PPATpLXcRdYoseTNaIkiGB3cB6ny7eUqJEgE0MtVKi4G7Ofv0qm3V5j6KIdUmuSSfnYsgIYgZ9klfEbgsukDf5TjrUTUG1xXF7UFkMXpbwFMHaSGJUJxkxDFpfVAv2R3GRI-lU6M3QVN_7Qa-7e4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f11883d2.mp4?token=BUGfFhNsQLlWqI0RTcmw6NfXw91yaC0IC62YVhXe93C8KtnrKljC2jFZn-QShdx6nttzo9KyBUPFBu7e7LAt3aLStEnKZbyPT61VOvW45k6xlwfVtvvn8554Jmac_ssDUCU2veTj2v7XDQ-TrwXlI4uyc7SN7RiE-1-DMsh1A0phViGlwJBqtkvTMWcebk837PPATpLXcRdYoseTNaIkiGB3cB6ny7eUqJEgE0MtVKi4G7Ofv0qm3V5j6KIdUmuSSfnYsgIYgZ9klfEbgsukDf5TjrUTUG1xXF7UFkMXpbwFMHaSGJUJxkxDFpfVAv2R3GRI-lU6M3QVN_7Qa-7e4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزارت برق کویت از قطعی ناگهانی برق در نقاط مختلف این کشور خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/668165" target="_blank">📅 02:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668164">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOLGEJhK8-ImQA1tUOnNhimNtfffSqXbJEF305WlsJ1-8TcE0Lj5HAoAbKdSuDWD_KirjefGvwQvPGXuQ_SgmjBNrPjoNlN2N32DgDHJAvTk3Bu-yb-637hyQXG2-sYQkWXsog3UONbrVLY4EAzVylOtm2cKJRW6CsWEvFjUweE3ONzEBnvefatxLxuSQBDk9Xe1mCJa9d0hKUGRUFebhekEzYdhrM2w99p5MB2ATO-y83Muc2jYbFfLobwZ21in8zFG2R2dPcZcEiZmdUa7Yocakm3fvlr5c_aJ5pNPQ0eS1Nhj9PS7m1yS1CnWJGj7bpHlYwqA2TR7k-sp8TLgaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار مرحله حذفی و یک‌چهارم نهایی جام
جهانی ۲۰۲۶
🔹
شش تیم از اروپا، یک تیم از آفریقا و یک تیم از آمریکای جنوبی
🔹
بازی‌های مرحله بعدی، پس از یک روز استراحت آغاز می‌شود.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668164" target="_blank">📅 02:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668163">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
چند نفر  بر اثر اصابت ترکش پرتابه دشمن در اسکله تجاری شهرستان سیریک مصدوم و به بیمارستان میناب منتقل شدند
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/668163" target="_blank">📅 02:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668162">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a1db4c83.mp4?token=eeXrSyuYdwFoF8pZ_G9OyXBNvYUnAyB1m_pvrXYRIvAnM_PdB08Cs5KQwH0_bVZUEFZIXP-jtymQzS4v3gL1CSTBEu7t9Do4s-1vVls5WOE7pri3EE0fwxoyjoDfz6-XPXLy7obc048LbEYVwmZFiYnPTzDlN1z0tw-K1D05k8LrBNADTFUMTP25xi908JEOCWt-GDYGwIZg7Hp03xHU3iZU7bkZQdyNmsKrj0pDbvmuhz9nZI-PR1wJ7Qqq7-uxLLL16y3rpy3DQmwtvlGuL4Sw2WeJIwXZPWWxLhedarbqu4QGowjlHbS-JwQ3QCZg7UJWYUY3HDXQy8G0-cncIQ3ZthjRX3Va6yIOv4jtXew9Ny87Tyyr1u4zJZb2bQDGiHLCZasaokn4-9t_6LrJT2yu6WmUJU8HhlqvLPEtR4J0QfccGXRaoQcVFkteBwBpKDCITZzMHrZj02uaSh6XzYPRH67O-z1Fclnr1mbnKACYLeDQyETRSY50OJ4dMn2mybnPud6eC_f5Ml53ubfG6WAh4bo8On01b5OsSy0-dCf037T_uWKNvIlx92UOHNoN4GlQ2QTo2MffL381EIzl_-cTXCb0V_6FuydUQhnNDX7WbXYEaSWCOwKk8k3LWogrZRsX7i20YFc66PZbw3yVITBtDj_GxLFz5M4ioMhjyXo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a1db4c83.mp4?token=eeXrSyuYdwFoF8pZ_G9OyXBNvYUnAyB1m_pvrXYRIvAnM_PdB08Cs5KQwH0_bVZUEFZIXP-jtymQzS4v3gL1CSTBEu7t9Do4s-1vVls5WOE7pri3EE0fwxoyjoDfz6-XPXLy7obc048LbEYVwmZFiYnPTzDlN1z0tw-K1D05k8LrBNADTFUMTP25xi908JEOCWt-GDYGwIZg7Hp03xHU3iZU7bkZQdyNmsKrj0pDbvmuhz9nZI-PR1wJ7Qqq7-uxLLL16y3rpy3DQmwtvlGuL4Sw2WeJIwXZPWWxLhedarbqu4QGowjlHbS-JwQ3QCZg7UJWYUY3HDXQy8G0-cncIQ3ZthjRX3Va6yIOv4jtXew9Ny87Tyyr1u4zJZb2bQDGiHLCZasaokn4-9t_6LrJT2yu6WmUJU8HhlqvLPEtR4J0QfccGXRaoQcVFkteBwBpKDCITZzMHrZj02uaSh6XzYPRH67O-z1Fclnr1mbnKACYLeDQyETRSY50OJ4dMn2mybnPud6eC_f5Ml53ubfG6WAh4bo8On01b5OsSy0-dCf037T_uWKNvIlx92UOHNoN4GlQ2QTo2MffL381EIzl_-cTXCb0V_6FuydUQhnNDX7WbXYEaSWCOwKk8k3LWogrZRsX7i20YFc66PZbw3yVITBtDj_GxLFz5M4ioMhjyXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین جزئیات حملات به جنوب ایران؛ وضعیت در شهرهای بندرعباس، سیریک و قشم عادی است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/668162" target="_blank">📅 02:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668161">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
پزشکیان عراق را به مقصد ایران ترک کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/668161" target="_blank">📅 02:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668160">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ1z7ostftUERTJZH46gVdaUSYCzV9NIpo_jN2fnkBg_Wxv70COmwrtn8QogDyQ418W8S1TcYBVc7AbXLfjfqPrnprzKYDqfbMN8kVxccijddQd7vUwALrrEUn9MdAqkK2qgIkpK0xn3LoMEcKxwZoXTgmeGxksMUPN-2mzX7Y_k74-OMzT25TSfd-akYYQTtN9sXkrX3WacDbAWwtwD9qa-h42PZbkXf-xj9oK3mrSonjtoK4_w4vDKB_tZiLJsKyq7rjZ06xOEgQx_VXnvHn6jVD8kdQ31vQMJ7qw25q49RLmhYN2j9EDDUzBESsr8ra1CG3chgDZxgIb4T-SLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جام ۲۰۲۶/سوئیس در پنالتی‌ها بلیتِ دوئل با آرژانتین را گرفت
🔹
سوئیس ۰ (۴) - (۳) ۰ کلمبیا
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/668160" target="_blank">📅 02:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668159">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec577fb73.mp4?token=Nz19eEfCTnQ3jUFcXfSFC22v6kY_95_oaP-XAx-adCnnXTlw6ZPi1zb1YwW8XHHBjGcA-0Z-6bRhBlDsK9p6Td8gKQEcfssBkLpCrjZCuyN-X4hBCHVRuRkI8Zkh1iOKYbXTB8MOHsDGuz7sXNLX1Gw_VQjmOCxbngwX8gQWcNX5qduFm8x24b8ell29_VKJVVNlSATOsDN8TzWeVip8FxYfOsxgYMmGpYwfpU6ZmYSWSRlHCqLg8-PSgUB8713_QAvcRwRrynsTOO5oGLFclCL0cJ5oBF4XE7CNe0qvfbACFodn6SmtNE5lAMDK8jKP01f9W8qkVuAjaRqU15Aw5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec577fb73.mp4?token=Nz19eEfCTnQ3jUFcXfSFC22v6kY_95_oaP-XAx-adCnnXTlw6ZPi1zb1YwW8XHHBjGcA-0Z-6bRhBlDsK9p6Td8gKQEcfssBkLpCrjZCuyN-X4hBCHVRuRkI8Zkh1iOKYbXTB8MOHsDGuz7sXNLX1Gw_VQjmOCxbngwX8gQWcNX5qduFm8x24b8ell29_VKJVVNlSATOsDN8TzWeVip8FxYfOsxgYMmGpYwfpU6ZmYSWSRlHCqLg8-PSgUB8713_QAvcRwRrynsTOO5oGLFclCL0cJ5oBF4XE7CNe0qvfbACFodn6SmtNE5lAMDK8jKP01f9W8qkVuAjaRqU15Aw5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برق برخی مناطق در کویت و بحرین قطع شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/668159" target="_blank">📅 02:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668158">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
بر اساس گزارش‌‌های اولیه، حمله امشب رژیم تروریستی آمریکا در استان هرمزگان عمدتاً تأسیسات و موقعیت‌ هایی را هدف قرار داده که غیرنظامی‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/668158" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668157">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca00dc6e4.mp4?token=d6fMQoHIl-am9nS5Aw9QWfvU80LOlvlaY4MMIgEEqEwg5D8__yohrYOebOEfRAXSG1ps7-AKfBDH98POElGSPT7bKLl4tEbYtS6gbo4sDgr3yhVpLoUp2q2GLz1KFXCI0nG87BUchS7It0CLrtGrP2xNjzo02rONlnj59KjfZ4PFs4TTPChDYC7cKRL3CzVOsaEcZRXgz9U5fNfLIJUajcqFsraffG0bmCxHt7jfTXDXVPrI-FfceecUroCrzZRZIn0DB8i32pSy28LZ2RCRLQs_H2kaL0gwwLKSPOYrxVHKGR3lrGjY0--daeNl3zJPKg_ANAEMk8iw6mLypCKoSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca00dc6e4.mp4?token=d6fMQoHIl-am9nS5Aw9QWfvU80LOlvlaY4MMIgEEqEwg5D8__yohrYOebOEfRAXSG1ps7-AKfBDH98POElGSPT7bKLl4tEbYtS6gbo4sDgr3yhVpLoUp2q2GLz1KFXCI0nG87BUchS7It0CLrtGrP2xNjzo02rONlnj59KjfZ4PFs4TTPChDYC7cKRL3CzVOsaEcZRXgz9U5fNfLIJUajcqFsraffG0bmCxHt7jfTXDXVPrI-FfceecUroCrzZRZIn0DB8i32pSy28LZ2RCRLQs_H2kaL0gwwLKSPOYrxVHKGR3lrGjY0--daeNl3zJPKg_ANAEMk8iw6mLypCKoSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرتاب منور توسط ارتش رژیم صهیونیستی بر فراز ارتفاعات «علی الطاهر» در جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/668157" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668156">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
المیادین: توپخانه مستمر اسرائیل حومه نبطیه الفوقه و مفدون در جنوب لبنان را هدف قرار می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/668156" target="_blank">📅 02:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668155">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ستون دود بندرعباس ناشی از حملۀ دشمن به شناورهای صیادی مردم است
مدیر بنادر و دریانوردی شهید باهنر و شرق هرمزگان:
🔹
دود سیاه در پشت بازار ماهی فروشان بندرعباس ناشی از اصابت پرتابه های دشمن به اسکله صیادی بندرعباس و آتش گرفتن تعدادی از قایق های صیادی مردمی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/668155" target="_blank">📅 02:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668154">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce85279956.mp4?token=NUsd_auz03zc2OoEfUyaZrz6hE8QbRxQ8omQyz74RFgAKbVB8UauZkj9byW5l0fFwMLQyaSxIahyqNA5U0mV9MyLFlDVI0drTM1yQFBn0crXwBZa_7BiIbF59Dxub2NzJ96osM8M5XcXRZhQtdTYz2vGl7fEAHwAa_1uAuSMkHB-17n50H662ceRtZ4ebWe86Sf6nfcpKKCcXMDR11BnWw5FitoQ-yTr5IGxoEVc8lZy6_dYhgWYbkcofHmmJ4aUSIHw16r0P6yVsvatmb8TrZ-FBxRUPrx_avyYXJuL1uquaBLSdNLjEdeJzGVAIAdW4fJBT0Iv6GMfZB-FojbIFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce85279956.mp4?token=NUsd_auz03zc2OoEfUyaZrz6hE8QbRxQ8omQyz74RFgAKbVB8UauZkj9byW5l0fFwMLQyaSxIahyqNA5U0mV9MyLFlDVI0drTM1yQFBn0crXwBZa_7BiIbF59Dxub2NzJ96osM8M5XcXRZhQtdTYz2vGl7fEAHwAa_1uAuSMkHB-17n50H662ceRtZ4ebWe86Sf6nfcpKKCcXMDR11BnWw5FitoQ-yTr5IGxoEVc8lZy6_dYhgWYbkcofHmmJ4aUSIHw16r0P6yVsvatmb8TrZ-FBxRUPrx_avyYXJuL1uquaBLSdNLjEdeJzGVAIAdW4fJBT0Iv6GMfZB-FojbIFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای اطراف حرم مطهر امیرالمومنین(ع) ساعاتی پیش از آغاز تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/668154" target="_blank">📅 02:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668153">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
روزنامه صهیونیستی اسرائیل هیوم:
ایالات متحده به کشورهای خلیج فارس اطلاع داده است که باید برای پاسخ احتمالی ایران در ساعات آینده آماده باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/668153" target="_blank">📅 02:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668151">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
خبرنگار صداو سیما در سیریک: دقایقی پیش، شنیده شدن دو انفجار دیگر در اسکله روستای زیارت شهرستان سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/668151" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668150">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99baa6d07b.mp4?token=hnctG77R-th4bJU00Bvu4y16IIagFOOvEjE4Lkj98lRnVECwV5mKPIwaSe1D2olvrbVF7T5A-9i0VGQRxi0bhFglyB8YksN-XgyRpcqwBYoXPtxem3JAF-T_61CUrAP0d2CILJ5f2SV1ajJLkWKbuxC_cucIoKmil_qc6fDtYWWi0hjvzFBU2r4RnvTT8PXLhOMWPzq7TfIh9ZFzmHlds9doGc8HpFMqBoSINVBycBla5wj0p0vRLiaQeta48vhBPdoSG_76z32QeCjVCoyeNcAINV1WgWMVwOjJ0HX3rPX_JsAD8aTruhYQHnybD-Gv1Dkt_qp6Ve3yELRkwYkn_2Qb2n2wtTgLeIvDTSHW38VgEymquLdWUmOWLzpbKlrBxpu04UBIWwU6Hk2SPphKmw4_Hb1s0s8GYoA505IJ_QfqtSAjcM7nk54EmhR7RUUy3BlB6S8T7HWu0AWFoaDVC8Yn0sWIXq-EHTZInk0ooyOOOHJaJjvFrbAQkc3l1BSTbaPa0e-WKzvrCfzoGiynmTmxVMNxWhLnAHrQr_6Kknqa8QdHjcEGykNvz52u5J3naZnelbeHYZNAM1uk3_X5kOk0WTtXfM4LXIRgP7HRhamV6Do-w2DKOONAAEq_dDiEG1JEOaLt1gQ3OvlS3XghqN5Lg8ARkKhi1JN4iH7srZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99baa6d07b.mp4?token=hnctG77R-th4bJU00Bvu4y16IIagFOOvEjE4Lkj98lRnVECwV5mKPIwaSe1D2olvrbVF7T5A-9i0VGQRxi0bhFglyB8YksN-XgyRpcqwBYoXPtxem3JAF-T_61CUrAP0d2CILJ5f2SV1ajJLkWKbuxC_cucIoKmil_qc6fDtYWWi0hjvzFBU2r4RnvTT8PXLhOMWPzq7TfIh9ZFzmHlds9doGc8HpFMqBoSINVBycBla5wj0p0vRLiaQeta48vhBPdoSG_76z32QeCjVCoyeNcAINV1WgWMVwOjJ0HX3rPX_JsAD8aTruhYQHnybD-Gv1Dkt_qp6Ve3yELRkwYkn_2Qb2n2wtTgLeIvDTSHW38VgEymquLdWUmOWLzpbKlrBxpu04UBIWwU6Hk2SPphKmw4_Hb1s0s8GYoA505IJ_QfqtSAjcM7nk54EmhR7RUUy3BlB6S8T7HWu0AWFoaDVC8Yn0sWIXq-EHTZInk0ooyOOOHJaJjvFrbAQkc3l1BSTbaPa0e-WKzvrCfzoGiynmTmxVMNxWhLnAHrQr_6Kknqa8QdHjcEGykNvz52u5J3naZnelbeHYZNAM1uk3_X5kOk0WTtXfM4LXIRgP7HRhamV6Do-w2DKOONAAEq_dDiEG1JEOaLt1gQ3OvlS3XghqN5Lg8ARkKhi1JN4iH7srZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت عراقی‌ها به سمت حرم‌ امیرالمومنین چندساعت مانده به اقامه نماز بر پیکر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/668150" target="_blank">📅 01:55 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
