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
<img src="https://cdn4.telesco.pe/file/ad4OW40mzBfN37dinLMjTyB_D0R6LvjlixdMdaiCfztol1tsIaZjFcLFaxAz8ikuhn54UIpuqgepmuskjsOP3JSf4e7jMHyi_BVh0xAxP-b-URO4tTOIHrbuLqLtqOu034Ei3JHbBX0vpS8DvQX4nVJTj8wIsfp5HF2ZX5bhoaM9zJL2vOZqGY02WcjZ4--VXIeFWa9pyGYx8WcpfIaop5jqhRzvPYAXbQDC9RiAiSpW3eo64Dtx9lNQQmfKozPjcENBdPkZHTjIxsTip5yF0UsMYCBYDrJkaUCfCjZ0i-T2Eztu0BTUcwL59vUm2lvN18hBBWvWYJScmudT3jPGzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 18:04:58</div>
<hr>

<div class="tg-post" id="msg-133416">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
فرشید حقیری : بانک شهر تمام سهام سایپا رو خرید، از کارخونه بگیر تا تیم فوتبالش
✅
احتمالا با توجه به این موضوع پرسپولیس ب که سال بعد قراره تو لیگ یک شرکت کنه، جایگزین سایپا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 880 · <a href="https://t.me/SorkhTimes/133416" target="_blank">📅 17:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133415">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
❗️
اوسمار ساعت یازده و نیم صبح امروز به ترکیه می رسد و با پرواز ساعت ۹ شب از استانبول راهی تهران خواهد شد.
🔺
تمرین فردا ساعت ۱۷ برگزار خواهد شد و ویرا در تمرین حضور خواهد یافت.اوسمار فردا نشستی هم با حدادی خواهد داشت.
✍️
قرمز آنلاین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 939 · <a href="https://t.me/SorkhTimes/133415" target="_blank">📅 17:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133414">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
🔻
🔻
علیرضا فغانی : گل سوم پرسپولیس به شمس‌آذر آفساید نبود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/133414" target="_blank">📅 16:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133413">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❗️
❗️
شهناز شریف :
🔴
«ما بیش از هر زمان دیگری به توافق صلح نزدیک هستیم. با توجه به اینکه احتمالاً نهایی شدن آن در ۲۴ ساعت آینده پیش‌بینی می‌شود، پاکستان در حال آماده‌سازی برای امضای الکترونیکی توافق‌نامه صلح بلافاصله پس از آن است و پس از آن مذاکرات فنی در هفته…</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/SorkhTimes/133413" target="_blank">📅 16:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133410">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❤️
🤩
پیگیری حدادی فدراسیون را مجبور به ارسال نامه به AFC کرد
🔴
پس از اینکه کنفدراسیون فوتبال آسیا نام گل گهر را به عنوان نماینده ایران در لیگ قهرمانان 2 معرفی کرد، پیمان حدادی مدیرعامل باشگاه پرسپولیس پیگیر ماجرا شد و تماس های متعددی با مسئولان مربوطه گرفت.
🔴
همین تماس های حدادی و پیگیری خستگی ناپذیر او هم باعث شد تا فدراسیون فوتبال ناچار به ارسال نامه توضیحی به AFC شود و در این نامه تاکید شده که گل گهر نماینده قطعی ایران برای فصل بعد لیگ قهرمانان 2 نیست و فدراسیون ایران تا 10 تیرماه برای این انتخاب وقت دارد.
🔴
در این نامه فرآیند انتخاب نماینده ایران در لیگ قهرمانان 2 به اطلاع AFC رسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/SorkhTimes/133410" target="_blank">📅 16:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133409">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ruvahwm2L2Qllc0ToDIV7qfprzZ5oATnLbVkFP6a5YJPh1LGy96GvqnPjR0jv2QjqswqW7z07P33G1eqUMp6qJeKwhtcSaneZNHwAQuzL_zsWa-vP1mh5KECYPvGBcH038InbGgtJqcEgYjX4QlwdfcGGFB_K21s1HcUP8C78ifagdqQVTQuu06dFgQPN1T6eA1AC0WnFDkICttiO4bgwpxze0suFmQBJ66AmKjZSUUvLpS9aS89Lzd6IJ49m41yIKLsOlMmaGxqhB0LR7VLTgqziFsI4Le_fOmS9gXRyfZhPLAzmKhY8exPcUXTzIGGDUQC90aYqi7io8vRrHRJeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسمی
🔴
آقا یحیی گل‌محمدی سرمربی دهوک شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/SorkhTimes/133409" target="_blank">📅 16:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133408">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87af10648a.mp4?token=PYdk8azYejdglIgvER2tryouhHzxu2I9nd_RbnbBweD2NgeEWDpZQApoaYDDq0vSC1EJRjm6IWAYQpjctYhDK7DY8MDfCpiwTBZfViEGNMJviUS7TflqyFDMAUo8Fz_tN6UlAmG6IqDhtUYUXHL8TWoA0gY8nq-Wd_qeCJaq7YO9fFJxuFlfQO2oDK7Wx34hqXe5jTj9BZ8HsKqPPvvoWULD5KoXBtv_yiMMCKGnF-0HvPu2yVet4O2duY90bvK70aMObxXZMyE8hVO4pqOgtY3AfP9xSRLzX494lEIkMYFrQ8f9b1w_Uuc2nliaizEKXaolwM5U8DOY-KN6kvNqlRDUF2VXxUbpZ0ekZ5hrirHKRz1TptO1R2iwDqcJworRZzME0f23YQp7rggQtXahnD7bs-E51kZjNAcqpFIzJ_3UWfUN-ZnqXARcJPEUJENp46lWNHgPfcOSyE5SrHI9SE9PIYU15dE0xKe_kIxxFyrrOtt1Q4i3VEtA32IL-OvKSH_XNORsMzahm39gi5r1X4mWW3rb7kR5PhYZj24-K_NlK1fG5t05D_fH48Gd41qeg5azYX2t36uPj1cVPH5Vy-rc00PgBmNtYaGktOEsKzs5f5EeDBcwPGUUL7xAy0ajrpGNhntKgB66a9XXrWIh0NRFOyBXm3rFsKEwrGXrlLo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87af10648a.mp4?token=PYdk8azYejdglIgvER2tryouhHzxu2I9nd_RbnbBweD2NgeEWDpZQApoaYDDq0vSC1EJRjm6IWAYQpjctYhDK7DY8MDfCpiwTBZfViEGNMJviUS7TflqyFDMAUo8Fz_tN6UlAmG6IqDhtUYUXHL8TWoA0gY8nq-Wd_qeCJaq7YO9fFJxuFlfQO2oDK7Wx34hqXe5jTj9BZ8HsKqPPvvoWULD5KoXBtv_yiMMCKGnF-0HvPu2yVet4O2duY90bvK70aMObxXZMyE8hVO4pqOgtY3AfP9xSRLzX494lEIkMYFrQ8f9b1w_Uuc2nliaizEKXaolwM5U8DOY-KN6kvNqlRDUF2VXxUbpZ0ekZ5hrirHKRz1TptO1R2iwDqcJworRZzME0f23YQp7rggQtXahnD7bs-E51kZjNAcqpFIzJ_3UWfUN-ZnqXARcJPEUJENp46lWNHgPfcOSyE5SrHI9SE9PIYU15dE0xKe_kIxxFyrrOtt1Q4i3VEtA32IL-OvKSH_XNORsMzahm39gi5r1X4mWW3rb7kR5PhYZj24-K_NlK1fG5t05D_fH48Gd41qeg5azYX2t36uPj1cVPH5Vy-rc00PgBmNtYaGktOEsKzs5f5EeDBcwPGUUL7xAy0ajrpGNhntKgB66a9XXrWIh0NRFOyBXm3rFsKEwrGXrlLo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
فیروز کریمی: عدم حضور پرسپولیس در بازی های آسیایی از اعتبار فوتبال آسیا کم میکند عدالت اینه که پرسپولیس به آسیا بره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/SorkhTimes/133408" target="_blank">📅 16:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133407">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
پرسپولیس دیوان افتخارات و اسطوره فوتباله ایران بوده ؛ تمام این چندین سال ثابت شده
🔴
🔴
مقایسه کردن امثال خداداد عزیزی با این عزیزان و بزرگان گناه کبیره محسوب میشه درست
✅
✅
ولی واقعا انقدر باشگاه ما کوچیک شده تا یکی عین خداداد بیاد داخلش پست بگیره؟
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SorkhTimes/133407" target="_blank">📅 16:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133406">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPorAMEy1u4KCh5ykl-PGWet370zdK30-yyXZtHyRKFIWWJ6V8JyVGpF5YhpkYkOQdskZnN5T9rGZ6Qm05ozLLjcsfQi9AQ7tVeVBnYwdW9fBvhdMnvZvQxK90smdjCC4pTNM1Mc8aAnWDaWYBm5oOIx4tjdv6zDVBohN_OEJgXmsZ3x6IBCwfnjAoFkvN9uMUM-K5qaCZx6mNEr-9ERJWI555TK-B4uRKCN9Z2QsU1Fm_PRuy5ER-ymFIr3EjhuvWtXonlf4j6dJ8iv_NKyOlAQf9eum46W2lVxDAK3ySaIfiLsmFBQYcmv-bPyRRE0gmWpGy1nhCK5eSrMbfu7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
شبکه آلمانی eSports One مسابقات جام جهانی رو به این شکل پشم ریزون به سبک بازی FC پخش میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/SorkhTimes/133406" target="_blank">📅 16:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133404">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
❗️
فوری/ نخست‌وزیر پاکستان: متن نهایی توافقنامه صلح بین ایران و آمریکا به دست آمد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SorkhTimes/133404" target="_blank">📅 14:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133403">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🏆
ادامه ابهام در سهمیه‌های آسیایی؛ سازمان لیگ با فدراسیون هماهنگ
🔴
فدراسیون فوتبال همچنان درباره سهمیه سوم ایران در رقابت‌های آسیایی به جمع‌بندی نهایی نرسیده و برای تصمیم‌گیری، کارگروهی تشکیل داده تا با بررسی سناریوهای مختلف، مسیر نهایی انتخاب نماینده مشخص شود.
🔴
طبق جمع‌بندی فعلی، اگر اعتراض باشگاه
گل‌گهر سیرجان
در کمیته استیناف تأیید شود، این تیم به‌طور مستقیم سهمیه آسیایی می‌گیرد؛ اما در صورت رد این اعتراض، تعیین تیم سوم از طریق برگزاری پلی‌آف انجام خواهد شد.
🔴
در سناریوی پلی‌آف، ابتدا دیدار
پرسپولیس
و چادرملو برگزار می‌شود و برنده این بازی مقابل گل‌گهر قرار می‌گیرد تا نماینده نهایی ایران در آسیا مشخص شود؛ با این حال، هنوز ابلاغ رسمی از سوی سازمان لیگ صادر نشده و همین موضوع باعث ادامه بلاتکلیفی شده است/مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SorkhTimes/133403" target="_blank">📅 14:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133402">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
پرسپولیس همچنان دنبال تیم «ب» از لیگ یکه، ولی باشگاه‌ها قیمت نجومی دادن و فعلاً معامله قفل شده؛ با این حال سرخ‌ها هنوز بی‌خیال پروژه نشدن.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SorkhTimes/133402" target="_blank">📅 14:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133401">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
یک مقام ارشد آمریکایی به نیویورک تایمز گفت: «میانجی‌گران و مقامات نظامی ایرانی تأیید کردند که رهبر ایران از توافق راضی است».
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/133401" target="_blank">📅 14:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133400">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❤️
واکنش بازگشا به شایعات برکناری حدادی :
✅
آقای حدادی هستند و برای گرفتن حق خانواده بزرگ پرسپولیس میجنگند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SorkhTimes/133400" target="_blank">📅 14:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133399">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_auPkTYcfaKOimIkyQfcjQ1lWWypqV0vPMuUnzb98wG_6SFIXHNjX132ZmPhIj9hoCx8CK3y9vACDKThkUIXvjQFQVPO5eay2ESm2cUD3DJWfADz54hzHBXIc0seQbab5Cz7H6wJXyehT9bLlOj5BpZazplas4oHLje0A7D-b28HtStzKHGmjdgx78WcqeZpTEQdjtTdnnTsaXfmJplsh_Wqjybu1cB9wJd2zwVsZplRUv00rUbzrV-rPX0wfAM5L3e9HOEkF9DSA-vse9v3IIIc_8AeXyfoKSnxQOusIdZWiSh_DybBXQ2o2PdmfhcSiGw3GV2bqBbE2QEzbAePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
واکنش بازگشا به شایعات برکناری حدادی :
✅
آقای حدادی هستند و برای گرفتن حق خانواده بزرگ پرسپولیس میجنگند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/133399" target="_blank">📅 14:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133398">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
قدوسی، قرمزآنلاین:
❌
اوسمار قبول کرده که مبلغ قراردادش رو کم کنه، باشگاه هم قبول کرده که درصورت بروز جنگ و ناامنی، اوسمار می‌تونه فسخ کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SorkhTimes/133398" target="_blank">📅 14:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133397">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbOziHWYHylcssV00fiIFB5t46KR7Tl4dU6O0PPfbEV0Om2-D6CPyuYZd1gHU7Fuh1MvsdQuFuXBntt8xkOQWn6MmOzDl-4eq3sakR5nKVtBPfqDo-gMdBOgGUvQKFabI1Xy-uvWgxh_uqmEfMuws5s1ElREcJIMqn0A6_rcf92oglFtqhnk48Wegndhl_BrN6uGxw6VvT0sf07ODbCLM5ToDq0X-BUl3d_GhFh21oh0oTnsPP3C1D9D2sdVrPRsW3F9jvNnllQo2JM2R_qBmaxsc9e_BuaG2SF73Uy0htvya8LRjiXpdTB1Y_GCsFKRZ0h5mVrX5mzNloXXY-6flA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
گروه B جام‌جهانی ۲۰۲۶
[
قطر
🇶🇦
🆚
🇨🇭
سوئیس
]
⏰
امشب ساعت ۲۲:۳۰
🏟
استادیوم لیوایز
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/133397" target="_blank">📅 14:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133396">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
امیلیو آلوارز به تهران آمد
🔴
امیلیو آلوارز، مربی اسپانیایی دروازه‌بان‌های پرسپولیس هم جمعه شب به تهران رسید تا در تمرینات حضور پیدا کند. او از میان شاگردان خود پیام نیازمند را به دلیل حضور در جام جهانی ندارد.
🔴
تمرینات آغاز شده است و جمع اعضای تیم هر روز…</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/133396" target="_blank">📅 13:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133395">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
❗️
اوسمار ساعت یازده و نیم صبح امروز به ترکیه می رسد و با پرواز ساعت ۹ شب از استانبول راهی تهران خواهد شد.
🔺
تمرین فردا ساعت ۱۷ برگزار خواهد شد و ویرا در تمرین حضور خواهد یافت.اوسمار فردا نشستی هم با حدادی خواهد داشت.
✍️
قرمز آنلاین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/133395" target="_blank">📅 13:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133394">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
عراقچی: اگر در ۶۰ روز به توافق نهایی نرسیم اما دو طرف از روند راضی باشند ممکن است تمدید شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SorkhTimes/133394" target="_blank">📅 13:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133393">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYAuxuuMFZPcv-rmIndxdArrcPFX8ZGCD-UfThaqTdhP2plTOvhaCzSZ4UnhrW2bN-eGZfoh7Z7-4orbFdLMTAXrEF5UohbU3Y40x5jMxkjNgy3vOVeih4tqdl0NLY6jby0aDDdDQRYS3dqchp6A3TS01Bunmrae1QDK7-kMjIjHIJjIc238eP2UDfsu4PB9u49BO7LX4RyJpgx8Ks3lRH6MS9eNxswN0NbQRhmxcMm-1RhLG3qSUFSNNooeVv_ybHpjeslYAmTGSE-Yl-0YgYLsPDeHqGpHNjPssde0TbnkqdNzRIS3ZYcYhnGPd2mwtfpca1Mpaoipa8TU4mok0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇮🇷
فیفا هتل شیک و زیبای وست دریفت (Westdrift) را برای اسکان تیم ملی در لس آنجلس معرفی کرده؛ فاصله هتل محل اقامت فعلی تیم ملی ایران در تیخوانا با هتل Westdrift در لس آنجلس 265 کیلومتر و با ورزشگاه محل بازی ایران و نیوزیلند حدود 10 کیلومتر و کمتر از 15 دقیقه است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SorkhTimes/133393" target="_blank">📅 12:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133392">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
عراقچی: اگر در ۶۰ روز به توافق نهایی نرسیم اما دو طرف از روند راضی باشند ممکن است تمدید شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/133392" target="_blank">📅 12:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133391">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
قدوسی، قرمزآنلاین:
❌
اوسمار قبول کرده که مبلغ قراردادش رو کم کنه، باشگاه هم قبول کرده که درصورت بروز جنگ و ناامنی، اوسمار می‌تونه فسخ کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/133391" target="_blank">📅 11:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133390">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
طبق اعلام سایت فوتبالی اوسمار ویرا در راه ترکیه است و روز یکشنبه یا دوشنبه سر تمرین پرسپولیس حاضر خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/133390" target="_blank">📅 11:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133389">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISBf4dQ9df52UzbOXG2Zr8O6bF5iFniasVvYRF6KMpVibhvhPIV9BOS6oM0eRBdGlcbpQQv_ER1NFpzE2jy_eI4CBSlWGHmzbegZ4Du-qsyr8zJ3K_OVks46oioDiWGMrZoahg8YRlnYx1wOPfzFYA9pVgOBqruY4jO6M8kJWC3jzv49g3w6xrUhGNs3rddow8CRt0DV_spGCshVBsT41Y0mhW2K6WFIn0oPqQ09WpkQ7coFhuAF83N2WxliFL85YW1IrDvu1DOPQYaSDOSQ9dQP6ty4W27hXEUHh6rySUhs0eK6yr6GE-N9xAXVJ5CgP3ZDMvEuhDomryEt2a5diQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
پرسپولیس دیوان افتخارات و اسطوره فوتباله ایران بوده ؛ تمام این چندین سال ثابت شده
🔴
🔴
مقایسه کردن امثال خداداد عزیزی با این عزیزان و بزرگان گناه کبیره محسوب میشه درست
✅
✅
ولی واقعا انقدر باشگاه ما کوچیک شده تا یکی عین خداداد بیاد داخلش پست بگیره؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/133389" target="_blank">📅 10:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133388">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❗️
محسن خلیلی : سروش رفیعی جواب تلفن نمیده.
✅
اوسمار فردا میاد ، واسه بیفوما هم بلیت جدید میگیریم بیاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/133388" target="_blank">📅 09:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133387">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⭕️
⭕️
شبکه خبر: سردار حسین سلامی فرمانده کل س.پ.اه به شهادت رسید
⭕️
سردار غلامعلی رشید، دکتر تهرانچی، فریدون عباسی به شهادت رسیدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/133387" target="_blank">📅 09:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133386">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
دیدار چهارم جام و سومین و آخرین افتتاحیه رو آمریکا با پاراگوئه از ساعت 4.30 صبح برگزار خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/133386" target="_blank">📅 09:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133385">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCvx4acm1kOGJmZKgzIcvCUYTycq1PDoWCYltRpyKdjic0zx6CaDduqw_aA-i-PfAjNFPKL2CCclRwP5mqlJfRFgBrSx84lbngumJUPdwwhwpzqHzVnQ6z_gzNxqYrjp26B73x-h8aq6trm5njJpBk2DqpXheeDs1iA28naovyKplct0qUOYz2HDdyPVNccciR4zT8OejRwH5oNQ8ZplSobczHt9qkJ9Rep1l9sp9zGDZwEr_TvXqgzFYgVSiGBw8kfr9V1lIO1qpAv6jvzRo0q9iUsbWP9aDLZSXWTweRHIM2Elpi4WzvYXt-hAoQZVyx1U56qcqInLpXU_5tVRHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پایان بازی | هفته اول لیگ ملت های والیبال روز سوم
🇮🇷
ایران
3️⃣
×
0️⃣
آرژانتین
🇦🇷
🇮🇷
25 | 25 | 25
🇦🇷
23 | 19 | 23
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/133385" target="_blank">📅 09:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133384">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v91e7o-77MwaCB9aMeGgvbMlECS2eQfL3ZEZt_Uwi72CsUH83DKlVaKM3XjnbZDj1FfSr6AC0mF-RzM1Tq5mr6E45mkSmM0QHTpjjjJXwHcK3knxaAyoKurPQ0od5q2GlWrjtq_TWbWAoALaBP2aEbBhdx2mlLBnWWYESsL7L--4UPKwfASCjYaWV9GeI9flCF8eIMRh921Y0rComtVMoVeYmDAWi1mz_dNIjLcpWZRVP5hDBho0uhkszOjjEhK7285Cr5PretW5KbR688nU9ZFHlaKt9v4DWvhCvu-dJk0WweLqC_2cawZAPG_Qd-VMoHjFeLoNgebUB7lRvBYNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
طبق اعلام سایت فوتبالی اوسمار ویرا در راه ترکیه است و روز یکشنبه یا دوشنبه سر تمرین پرسپولیس حاضر خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/133384" target="_blank">📅 09:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133383">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇦🇷
در نزدیکی کمپ تمرینی ارژانتین تیراندازی رخ داده و تا الان یه کشته و دو زخمی داشته!!!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/133383" target="_blank">📅 09:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133382">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❤️
🚨
چند گزینه درتلاش برای لابی و جانشینی حدادی/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/133382" target="_blank">📅 09:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133381">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
این هم یادمون می‌مونه، در روزهایی که حدادی در حال دوندگی برای درست کردن سهمیه آسیایی پرسپولیس ششم جدولی بود، خیلیا داشتن زیرآبش رو می‌زدن تا جاش بشینن!
🔴
عاشقان قدرت
خائنین به پرسپولیس/شاهین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/133381" target="_blank">📅 09:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133380">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkxzrPdSu23JQRs3he09VRK9qzztFPsmxp0bcHkC__cLRAzUSmuyJDGhphwmQaVZBs3swlX5m5nsX7n54MZ7jfW0RnUbv-gI4fsj6pFj2XaKQbNlJ_Yag1DsIeKQKe-e3uRbvejyoVpFXrvfor59DTTlxr43WQa_yshYp2VHhzNCr8a6iUut6KzkaHsPjBoKoakJXL7gdljKb0Iehf8HEbMobyiyVxYP_ASPdza9pIJI_A0zgGX-6bB5QjcDgIrrUbXRhKgd97jN46tf0XW5nz3XcZtLpTXUBnFfE3YInOw7nD8_2i3KP8XDqi2VOF1hnIuU0QtosK-3y-hdUE1Vuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
دیدار اول گروه C جام‌جهانی ۲۰۲۶
[
آمریکا
🇺🇸
🆚
🇵🇾
پاراگوئه
]
⏰
بامداد شنبه ساعت ۰۴:۳۰
🏟
استادیوم سوفای
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133380" target="_blank">📅 01:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133379">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cje3My5plPQY_Mfi24JsQfA410xmMnaxbCmvxr20yUVG8gSj3fgO6OuB6KB8JkLLZ06_eAfQ6W715mrlTeBVskIdc8q4ifyEZUldSGBdw2ellVRvXPJTYEJ6pxxF4Wn6fTzRen_owpgf-rtvENcaSdHodQX3f0IF6QX4L6U2rL-DYJevvcSdAdJaV9OG_PdOHeAnkLPXXZ6XNaRxwg3i8SrrME1EHHqe53cmkcKHWZstUyCabsDQGrOjxxvG644SIPVhM3kihgLFYVfD3BzeXc5A-xddztztAyAG3Q0ijeR5wrJ-6mEtCQRwBXck7IPInks-mTz0gtoEDoT6eELczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
دیدار چهارم جام و سومین و آخرین افتتاحیه رو آمریکا با پاراگوئه از ساعت 4.30 صبح برگزار خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/133379" target="_blank">📅 00:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133378">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇨🇦
گل‌تساوی کانادا به بوسنی دقیقه ۷۸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/133378" target="_blank">📅 00:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133377">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhinUA2r1mx5xyfXUYz2Z6W3ipuYbt6xlmSaYBDR-MtMhDx-UOevoPMs-qe7Ia-300fLKUJD4bgkPncEE4hhx9ucE1WTmqd7eay9SIM-Vo0zHybNqL87j6S4svTSQ0--2y0F3W0PakPHnBu_I4H52EEcXfmX1hDtI2d4x6t7gWqzA5zbJZpTPJuqrf7avUUUetE-g9zdH4tdDHf7t_FDoiyt8FgNmvRmUapgpIMYzbeKfSdNWEb7K2gUjQMoKI4w3YwuyWt-IE-yVcVH4oU17yzGLjSF6iq4O1dM7hmb_YFOOEHVdG5mGlP-aHngvwqAKdAeidpJN-wyea4nRwQ1Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
برگاتووووووون بریزه
😳
🚩
🚩
بازسازی ورزشگاه آزادی بالاخره داره تموم میشه و این ورزشگاه بالاخره شکل قشنگی به خودش گرفته
👌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/133377" target="_blank">📅 00:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133376">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇨🇦
گل‌تساوی کانادا به بوسنی دقیقه ۷۸
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/133376" target="_blank">📅 00:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133375">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=G9uw2A98Gb3_OAFX1TZ4xdlpTtJNIJQp9lPw8VvOURDvpTkE8cT0T4L4-tgOHhOgcPeAyVQ0UkoLt4LkZeMIlNGHrk7YkA9CwXrZknE3Kb9LB9vQuw_SaaKWBxN1g6OcfDd4H8Zi6FJRWngyvhEGft2IWblKZvVsaT3OlsbMvls8NCJUWdcDm73i1mjzel4zFzsEf3Z5HvxaseXxm8kkThqQ_lJxMF9IzYwM4jb_FBZFtFlpf5atq8eXh_eLiiLKm6h9MQEyct-lxoX4-tN2VA5jpdSuzosl1vwK1AFD4P2oxEJf8R4eGf_H75g3gL5Ql4FiJZQ5J3JhISNxEryOAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=G9uw2A98Gb3_OAFX1TZ4xdlpTtJNIJQp9lPw8VvOURDvpTkE8cT0T4L4-tgOHhOgcPeAyVQ0UkoLt4LkZeMIlNGHrk7YkA9CwXrZknE3Kb9LB9vQuw_SaaKWBxN1g6OcfDd4H8Zi6FJRWngyvhEGft2IWblKZvVsaT3OlsbMvls8NCJUWdcDm73i1mjzel4zFzsEf3Z5HvxaseXxm8kkThqQ_lJxMF9IzYwM4jb_FBZFtFlpf5atq8eXh_eLiiLKm6h9MQEyct-lxoX4-tN2VA5jpdSuzosl1vwK1AFD4P2oxEJf8R4eGf_H75g3gL5Ql4FiJZQ5J3JhISNxEryOAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
حمله تند محمدحسین میثاقی به منتقدان تیم ملی روی آنتن زنده تلویزیون: آدم مفت بر از خاله،
کصکش
تره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133375" target="_blank">📅 00:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133374">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
🔴
اوسمار راهی ترکیه شد/ویرا شنبه شب در تهران
🔴
اوسمار شنبه ظهر وارد استانبول  خواهد شد و بعد از چند ساعت توقف در فرودگاه این شهر سوار پرواز استانبول_تهران شده و  شنبه شب به به تهران می رسد و ضمن حضور در تمرین نشستی هم با حدادی خواهد داشت.اوسمار احتمالا در…</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/133374" target="_blank">📅 23:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133373">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
همسر اوسمار تو یک استوری از اوسمار خداحافظی کرد و اوسمار راهی ایران شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/133373" target="_blank">📅 23:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133372">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5318d7b2c2.mp4?token=txC88KUYDitcSm3rIrjl8EWN0z_e8xancu_iVfYWjCOfDWDdkWHIipKZs5H20cIjNhpVegWQWI6tBZOwQHBDfNHperHvTPjh_d0Mj7oUUmbaul_Evg3BVRFK24oNZOdMEwQXhRtiMYO-SCTNkGoaHVdbcZ3tenN6zxGG9DSXDk6KLuJNngBKKZ6znpN3Ij3rQ-qP63ikon3DGeccHc4fmgJO7Mhtn5JVQF1rLHEDURhFIU_dcMb-GNb8acDg0zJyACvIo9Wrhd9L9x0oQaR2VPH4svYMkAuy6cUVBTuU9wJp5UpLpGjg7IArsAjNDd4gsmiOTYgJYXdB9cg5OW-VnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5318d7b2c2.mp4?token=txC88KUYDitcSm3rIrjl8EWN0z_e8xancu_iVfYWjCOfDWDdkWHIipKZs5H20cIjNhpVegWQWI6tBZOwQHBDfNHperHvTPjh_d0Mj7oUUmbaul_Evg3BVRFK24oNZOdMEwQXhRtiMYO-SCTNkGoaHVdbcZ3tenN6zxGG9DSXDk6KLuJNngBKKZ6znpN3Ij3rQ-qP63ikon3DGeccHc4fmgJO7Mhtn5JVQF1rLHEDURhFIU_dcMb-GNb8acDg0zJyACvIo9Wrhd9L9x0oQaR2VPH4svYMkAuy6cUVBTuU9wJp5UpLpGjg7IArsAjNDd4gsmiOTYgJYXdB9cg5OW-VnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افشاگری جنجالی عادل فردوسی‌پور: فدراسیون فوتبال بعد از اتفاقاتی که افتاد تصمیم گرفت سردار آزمون رو به جام‌ جهانی ببره اما فهمیدند گاف دادند و اسم او را در لیست ۵۵ نفره نداده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/133372" target="_blank">📅 23:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133371">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
عراقچی: اگر در ۶۰ روز به توافق نهایی نرسیم اما دو طرف از روند راضی باشند ممکن است تمدید شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133371" target="_blank">📅 23:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133370">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
🔴
اوسمار راهی ترکیه شد/ویرا شنبه شب در تهران
🔴
اوسمار شنبه ظهر وارد استانبول  خواهد شد و بعد از چند ساعت توقف در فرودگاه این شهر سوار پرواز استانبول_تهران شده و  شنبه شب به به تهران می رسد و ضمن حضور در تمرین نشستی هم با حدادی خواهد داشت.اوسمار احتمالا در…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/133370" target="_blank">📅 23:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133369">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⏱
پایان نیمه اول
🇨🇦
کانادا ۰ - ۱ بوسنی
🇧🇦
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/133369" target="_blank">📅 23:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133368">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
🔴
قدوسی: اوسمار راهی ترکیه شده و به زودی میاد ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133368" target="_blank">📅 23:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133367">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
عادل فردوسی‌پور باز هم ثابت کرد که برای ساختن یک برنامه حرفه‌ای، بیشتر از امکانات گسترده، اعتبار و درک درست از مخاطب اهمیت دارد.
✅
در شرایطی که صداوسیما سال‌هاست از بسیاری فرصت‌های مهم رسانه‌ای عقب مانده، عادل فردوسی‌پور در برنامه ویژه افتتاحیه جام جهانی…</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/133367" target="_blank">📅 23:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133366">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
عراقچی: اولین چیزی که در توافق اشاره شده این است که محاصره دریایی رفع شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/133366" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133365">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
عراقچی: اولین چیزی که در توافق اشاره شده این است که محاصره دریایی رفع شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/133365" target="_blank">📅 23:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133364">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
عراقچی: اگر موارد یادداشت تفاهم رعایت نشود توافق نهایی امضا نخواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/133364" target="_blank">📅 23:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133363">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
عراقچی: موضوع هسته‌ای، رفع تحریم‌ها، بازسازی و پول‌های بلوکه شده در یادداشت تفاهم آمده
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/133363" target="_blank">📅 23:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133362">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
عراقچی: دشمن تعهد خواهد داد که دیگر آغازگر جنگ نباشد و از تهدید و زور استفاده نکند و دوطرف به حاکمیت یکدیگر احترام بگذارند و در امور داخلی یک‌دیگر دخالت نکنند
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/133362" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133361">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
عراقچی: وقتی توافق نهایی شد بندها را تشریح می‌کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/133361" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133360">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
⭕️
فوتبال ۳۶۰ مدعی شد که اگه اوسمار تا ۲۴ ساعت دیگه نیاد،باشگاه سراغ گزینه های دیگه میره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133360" target="_blank">📅 22:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133359">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd1dc6dde.mp4?token=bCZdFdSjRdpIOLXNyUa9jCUOv9YmG1pMLN7EJsL5omJ0v5aa15zJiqQhWqiEd0qUMv7EfqCwJ8-xwIIdZBTvvmvt93EMYxBX_kMWxUy-KCyzRt6UiM63sOr7iT9m-GrxqB0aGFA6Y3p_SQctoa4GfgXwGxV89UHoP_uMH1tE8i1YuAUzvyIuqzwTPbTIM9_b_L8XbPjbOpXkbU5qjPM3An-y_davPwl5P9VAdmuVB2_4hfpBap9uTFHQ7j-ef5FBs3vfIbUe09clHPfR99GnVIn5WplLXHn8ibqqdG27-LqDpJ75uexZXUP50__8oNuNeHMfW6_vEV5E7C_HVD_Qng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd1dc6dde.mp4?token=bCZdFdSjRdpIOLXNyUa9jCUOv9YmG1pMLN7EJsL5omJ0v5aa15zJiqQhWqiEd0qUMv7EfqCwJ8-xwIIdZBTvvmvt93EMYxBX_kMWxUy-KCyzRt6UiM63sOr7iT9m-GrxqB0aGFA6Y3p_SQctoa4GfgXwGxV89UHoP_uMH1tE8i1YuAUzvyIuqzwTPbTIM9_b_L8XbPjbOpXkbU5qjPM3An-y_davPwl5P9VAdmuVB2_4hfpBap9uTFHQ7j-ef5FBs3vfIbUe09clHPfR99GnVIn5WplLXHn8ibqqdG27-LqDpJ75uexZXUP50__8oNuNeHMfW6_vEV5E7C_HVD_Qng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
لحظاتی از مراسم افتتاحیه جام جهانی در کانادا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133359" target="_blank">📅 22:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133358">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
رویترز: امارات با آزادسازی مجموعاً ۱۰ میلیارد دلار از دارایی‌های ایران موافقت کرده بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/133358" target="_blank">📅 22:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133357">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
🔴
آکسیوس : ترامپ در  تماس تلفنی با نتانیاهو گفته:
❗️
«این همون توافقیه که دنبالش بودیم؛ یک توافق عالیه و وقتشه جنگ با ایران به پایان برسه .»
🔴
طبق این گزارش، نتانیاهو در این گفت‌وگو زیاد حرفی نزده و ظاهراً متوجه شده که توافق در آستانه نهایی شدنه و توانایی…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/133357" target="_blank">📅 22:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133356">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
⭕️
آکسیوس و کانال دوازده اسرائیل تایید کردن  توافق بین جمهوری اسلامی و آمریکا نهایی شد
✅
کانال 12 اسرائیل : سرانجام توافق شد ؛ این توافق قطعیه و به نتانیاهو اعلام شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/133356" target="_blank">📅 21:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133355">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
#فوری | ادعای ای‌بی‌سی به نقل از منابع:
🔴
پیش‌نویس توافق از سوی مقامات عالی‌رتبه در نظام ایران تأیید شده است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/133355" target="_blank">📅 21:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133354">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
حالا دیگر ارتش سرخ هست تا جلوی هتاکی شما و تخلف غیرحرفه‌ای را در راستای حرفه‌ای‌سازی و معرفی نماینده آسیایی بگیرد. حرفه ای گری کسب و کار پرسپولیس است.
🔴
با مراجعه به صفحه AFC در اینستاگرام با هشتگ #FairACL2ForIran به اقدامات غیرموجه فدراسیون و سازمان لیگ…</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/133354" target="_blank">📅 21:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133353">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-Wr9wAvjQUJ6GUGgGIXU4szmlstNAHFVyhF5kdPVlHCLn9qlV32YnVPTtADsDWh1hOtox5xtxfPv_RU8NkcpUtGEgqFMZaE4CMiRBzFacQayLI2lxxs31ESoqEoROaj5hxrTKjOsm56LiRePK6n-jYbc9TSZ9jbkL_uUPZr4b8a87iDcQvmJI-CZsIx_tVQX-8dCs_wGhLX6KNymd7jvieog3joyB2FMb5CKcSyxEH8T_JnI1dpDY3S5ihXHsx_lPZjFTUOMF0-SNrOaAKSVB_nMWDE1w5GDPnxokPTfAhQvebAjFHN-EbpC_G6W8dM_eZ957ly96174EVrbRQwOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حالا دیگر ارتش سرخ هست تا جلوی هتاکی شما و تخلف غیرحرفه‌ای را در راستای حرفه‌ای‌سازی و معرفی نماینده آسیایی بگیرد. حرفه ای گری کسب و کار پرسپولیس است.
🔴
با مراجعه به صفحه AFC در اینستاگرام با هشتگ
#FairACL2ForIran
به اقدامات غیرموجه فدراسیون و سازمان لیگ اعتراض کنیم
https://www.instagram.com/p/DXkUpt7k5yN/?igsh=MWU5dzJvYnd3anpoMA==</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/133353" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133350">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAxbBD4jZ7btNCv0Uf3Yfk79nW_hYSV1epsJ37rEVQYiBtyhzUl5qjfn7oU79iqGLQ7dMfvZtoGTBGUXqtGEu23aRkg-BxoPyZITlhV8435lVm1V09WqxtJLx5PkZrK29h99SFQNoCk9vzKjDS_XYWJ7a3cwZ6fuedOVqjYp9JkewTClRBgZIgjscYt3iAhEJTABytGuautFzwr9i442E9kpqwsiEdq4pqPv0ql9nzHforK9Xo-ZzWqrROFBJ6Tvz-6hkVv90EdJFoLlT3qHl8m_IpIXi9x8KoulBsRMH0Mv1g2017wQ-HUa13Y88zonjib1HV0OJWIHD3voN2CmTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بازی‌های امشب جام‌جهانی رو با ۱۰ درصد بونوس اولین واریز پیش‌بینی کنید!
📌
جام جهانی ۲۰۲۶ رو با وینکوبت پیش‌بینی کن و ۱۰ درصد بونوس اولین واریز بگیر.
📌
چرخش رایگان گردونه، شانس روزانه تا سقف ۱ میلیون تومان.
🔗
برای پیش‌بینی بازی‌های جام‌جهانی با بیشترین آپشن ممکن همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔗
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/133350" target="_blank">📅 20:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133349">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
⭕️
فوتبال ۳۶۰ مدعی شد که اگه اوسمار تا ۲۴ ساعت دیگه نیاد،باشگاه سراغ گزینه های دیگه میره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/133349" target="_blank">📅 20:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133348">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
محسن خلیلی : سروش رفیعی جواب تلفن نمیده.
✅
اوسمار فردا میاد ، واسه بیفوما هم بلیت جدید میگیریم بیاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133348" target="_blank">📅 20:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133347">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
پرسپولیس که مجوز حرفه ای خود را بدون مشکل در فصل جاری کسب کرده، به دریافت مجوز حرفه ای از سوی برخی باشگاه ها معترض و معتقد است کمیته صدور مجوز حرفه‌ای در این زمینه دچار تخلف شده است.
🔴
یکی از مدیران باشگاه پرسپولیس در این زمینه گفت: باشگاه پرسپولیس قرار…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/133347" target="_blank">📅 20:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133346">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
مهدی سالاری مدیر گل‌گهر: رای قطعاً به نفع ما خواهد بود و توصیه میکنم تمرینات پرسپولیس رو تعطیل کنید تا بازیکناش برای فصل بعد آسیب نبینن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/133346" target="_blank">📅 19:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133345">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
خبر فوری رویترز:
🚨
توافق توسط جی‌دی ونس و قالیباف امضا می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/133345" target="_blank">📅 19:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133344">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
پرسپولیس همچنان دنبال تیم «ب» از لیگ یکه، ولی باشگاه‌ها قیمت نجومی دادن و فعلاً معامله قفل شده؛ با این حال سرخ‌ها هنوز بی‌خیال پروژه نشدن.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/133344" target="_blank">📅 18:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133343">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🔴
پرسپولیس در مشهد کپی می‌شود
🔺
مدیران پرسپولیس در ماه‌های اخیر طرح‌های مختلفی را برای تشکیل تیم دوم مورد بررسی قرار داده‌اند تا از این طریق زمینه رشد بازیکنان جوان و مستعد را فراهم کرده و مسیر حضور آنها در تیم اصلی را هموار کنند.
🔺
گفته می‌شود یکی از گزینه‌های…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/133343" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133342">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
ایرنا:
❗️
متن توافقنامه با دقت بالایی نوشته شده و دیگه هیچکدوم از طرفین قرار نیست بدعهدی کنن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/133342" target="_blank">📅 16:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133341">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLZwUF08Gi4_-Z2FZloXeiY7D5wlgXJZNAPgaZdwbnWjx7QwZM5fap5ZhwLEWDt_O_KhojkyGk6NMqnVv1tZNSjf8bGTWimKsFuspCXBR7gPAwE0vS5tc408JBgO1aJ8jK5r0-3HVPxg6a5N2zj3uTxZtW8Eb5wObBTaddpDJdQJXUnEybQT1R9GAOGorCZSN7BVyn1xdRppLsdSR98vOhu72oRd7fNA9h-Wqx1XdzsczmC9LSxtKzr_zMRfhctZ40OdGzCoS6LrU0d_V3RgvSU8cXtzeEi4WFlssZ0xOav0zkDPvjiR7uCDcE3PUtWJk4iFU1b3eoy4UXjfIIqOuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
در نزدیکی کمپ تمرینی ارژانتین تیراندازی رخ داده و تا الان یه کشته و دو زخمی داشته!!!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/133341" target="_blank">📅 16:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133339">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
پرسپولیس معتقده مجوز حرفه‌ای استقلال غیرقانونیه و داره در AFC پیگیری میکنه/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/133339" target="_blank">📅 15:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133338">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📌
📌
خبرگزاری دولت:تمامی خطوط قرمز تعیین شده از سوی رهبر انقلاب، آیت‌الله سید مجتبی خامنه‌ای، در چارچوب نظارت مستمر شورای عالی امنیت ملی در متن مورد توجه قرار گرفته‌است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/133338" target="_blank">📅 15:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133337">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚡️
⚡️
خبرگزاری دولت:تهران در طول دوران تبادل پیام‌ها، برای اطمینان از اجرای برخی مفاد تفاهم‌نامه تضمین‌های معتبری از برخی طرف‌های ثالث برای اجرای تعهدات پیش‌بینی شده دریافت کرده‌است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/133337" target="_blank">📅 14:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133336">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⚡️
⚡️
خبرگزاری دولت:تهران در طول دوران تبادل پیام‌ها، برای اطمینان از اجرای برخی مفاد تفاهم‌نامه تضمین‌های معتبری از برخی طرف‌های ثالث برای اجرای تعهدات پیش‌بینی شده دریافت کرده‌است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/133336" target="_blank">📅 14:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133335">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
#فوری | سخنگوی وزارت خارجه:
🔴
متن توافق پایان درگیری ایران و آمریکا تقریباً نهایی شده و منتظر تأیید نهایی نهادهای تصمیم‌گیر ایران است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/133335" target="_blank">📅 14:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133334">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuNrTMMlu0PYwZJaLt7t8sc3C1zcsc474pVlbZLuFPTBhrYlwGep_l7rD7lmT1ZQdUSKSzQ5j3sOKLzsqQJ9B2J5_u2aQK6txl-UiZph3p97GZfLSzuoeZ0pVuon7uzaB3D9ljFwVhDPNswQnsMA0dxJQDaxh32rITgEnqwsJeU6sOOSapz_A5c00gsGlYVRu-gXKaZPH5X3D9Zj_J9VW4nqeRmVuV4TxG8EHZLQNvuLlZOlRBFiX2O2kG-RdCgJZDqJCiogHddPfLrivzORoUpGbd-O6cNNNWUVHC2dxBbWcaXiHZ0_qXNnmNKsu8ZiOzwQ5wi8TOWwVRmd1Sya-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای تورنمنت 3 جانبه
پ.ن نظرتون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/133334" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133333">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRof-654oThvssA6uwMz08FcWAda_1Pzd8aqP1a5meO0kiz2OTkN2dDfFp5RSxsWBdoDfbGhueUiOybr20gV7MUF5F5kqImpYZaR7w17x5u_mlyAqaqi2KL0XitgUwWSGwqsm_zTmV682LrNfW5OU2yJYzRWTVeHN5mI_xaM1qE-lRS4MquIIfXOsORroAGjHn8sbC3JKwrTOi58HZoINxnUe9L7YajNSr46NYcA0fK-M-fxSWAjnUkOgAdmJvIAnqV0PACIEA3PO8-XYlIumbOQH_7Q8I7_rp7WlJZ_p-SgAdzrkL1HDiZwkla7FiyiMUqEJMkCUWKBvstWZ7m2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سینا اسدبیگی در لیست‌ اولیه‌ بازیکنان‌ مدنظر اوسمار ویرا قرار ندارد اما مدیریت باشگاه قصد دارد درصورتیکه با احمدنوراللهی یا محمدقربانی قرارداد امضا نکند سینا اسد بیگی رو بار دیگر به جمع سرخپوشان بازگرداند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/133333" target="_blank">📅 14:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133332">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
ادعای العربیه: یک تیم حقوقی پاکستانی برای حضور در مراسم امضای توافق میان ایران و آمریکا در یک کشور اروپایی شرکت خواهد کرد.
❌
ایران درخواست کرده است که توافق با آمریکا در یک کشور اروپایی امضا شود تا به آن جنبه و اعتبار بین‌المللی داده شود.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133332" target="_blank">📅 13:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133331">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XmDUDQcSwa7D8QAD2ITloDmcILwE1zEAT-xcgNrF8IxVYnfvWsR3O4uWo7L97N5IJXEOl1Rmnwb6J39yRSnhYLlZY8hYjCfzo2ln8V4crTQK7a22_aT6H0B69w5FWJX9ZqQDUbA1QNKo20XredZ_InSI1nvdl0Rj83SgapzBTS6FTn0k--00YDXQ1u4Lu7yLs4zD6Kf4jI-rAaVwn6mgnSTDANp-f3eB5eVNd3d9Ui2eKxTFtak4lQu1tEH0_ihamVFsTZAqfORSB0wwdAfHlQZBnPuQWKPZFQkwgCXoFycAKVb3UL3nka1FETL7TAJyecJjklgaWvmcEyAzCmLSkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
بونوس ویژه جام‌جهانی برای تمامی کاربران به مدت محدود
🎁
به مناسبت شروع جام جهانی، برای مدت محدود
۱۰٪ بونوس ویژه واریز
برای تمامی کاربران در نظر گرفته شده است، تا با قدرت بیشتری وارد پیش‌بینی مسابقات و رقابت‌های این تورنمنت بزرگ شوید.
🎁
این بونوس ویژه به‌صورت محدود و تا ساعت ۲۰:۳۰ امشب می‌باشد، که قابل استفاده برای تمامی کاربران سایت به‌همراه یک گردش پیش‌بینی با ضریب ۱.۸ ‌می‌باشد.
📌
برای ورود به وینکوبت از طریق ربات رسمی سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/133331" target="_blank">📅 13:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133330">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
✅
مقامات گروه ۷: تفاهم‌نامه آمریکا و ایران ممکن است همین یکشنبه در ژنو امضا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/133330" target="_blank">📅 13:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133329">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
✅
مقامات گروه ۷: تفاهم‌نامه آمریکا و ایران ممکن است همین یکشنبه در ژنو امضا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/133329" target="_blank">📅 13:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133328">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
#فوری |دونالد ترامپ، رئیس‌جمهور آمریکا: ما امروز به جنگ با ایران پایان دادیم و این کشور توافق کرده است که هرگز سلاح هسته‌ای در اختیار نداشته باشد، چیزی که ما بر آن اصرار داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/133328" target="_blank">📅 13:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133327">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
فوری/ مدیران باشگاه پرسپولیس با ارائه مدارک مستند به afc خواهان رسیدگی به روند صدور مجوز حرفه ای باشگاه استقلال شدند. مدیران باشگاه پرسپولیس معتقدند فدراسیون در روند صدور مجوز حرفه ای دچار تخلف شده و خواهان حذف این تیم از آسیا شد/فارس
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/133327" target="_blank">📅 12:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133326">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
حمله علیرضا نیکبخت به افشین قطبی: ذات خوبی نداشت؛ در قهرمانی پرسپولیس هیچ کاره بود! آن تیم را حمید استیلی و مرزبان قهرمان کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/133326" target="_blank">📅 12:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133325">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_lW5-583dbEpJlqpSwpSAcgAro2jE17nhtmwzfj8DBW_iX9NXauE7P9DJVJZb4ticOzqCKEcG3aJp-E4df5mZ1KgS-Sbvd5ElwJtUPvCoF1EeCbhYpn-KYygrfIf-JZj6vgRTqFOSVNAWwVr7mhi2MmmigAO2iLy9IiKZuBsxbdBEKyVN_rGi9Q3JSjJXqTaWMWQV51XI6JQPAaEby_Xn38FRD0uyxeY_Enoag7IqF86pWxppZsxc6c28LKI17lwTWx4PhD9Y0isJrlS9-HdNfL2pRQVHA_icrfpkc9e4SDY5dyziD6B63l_jeTJrFOO0uh00HKFHrUsXzWkv-GnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
محبی چرا با پرسپولیسی‌ها میپره
🧐
✅
پ.ن خبریه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/133325" target="_blank">📅 12:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133324">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
فوری/ مدیران باشگاه پرسپولیس با ارائه مدارک مستند به afc خواهان رسیدگی به روند صدور مجوز حرفه ای باشگاه استقلال شدند. مدیران باشگاه پرسپولیس معتقدند فدراسیون در روند صدور مجوز حرفه ای دچار تخلف شده و خواهان حذف این تیم از آسیا شد/فارس
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/133324" target="_blank">📅 12:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133323">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
کریس رونالدو کاپیتان 41 ساله پرتغال : من میتوانم چهار سال‌ دیگر بازی کنم و در جام جهانی 2030 نیز حضور داشته‌ باشم. حالا حالا ها برنامه ای برای خداحافظی از دنیای فوتبال ندارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/133323" target="_blank">📅 12:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133321">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
دیبالا مهمون عادل تو ۳۶۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/133321" target="_blank">📅 11:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133320">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
🎥
لحظاتی از یک روز پرکار در زمین تمرین؛ جایی که پرسپولیسی‌ها با انگیزه و تمرکز، برنامه‌های آماده‌سازی خود را دنبال کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/133320" target="_blank">📅 11:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133319">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
محسن خلیلی : سروش رفیعی جواب تلفن نمیده.
✅
اوسمار فردا میاد ، واسه بیفوما هم بلیت جدید میگیریم بیاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/133319" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133318">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
ترامپ: به یک تفاهم‌نامه بسیار قوی با ایران رسیدیم و بالاخره این جنگ تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/133318" target="_blank">📅 10:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133317">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
خلاصه دیدار
🇰🇷
کره‌جنوبی
2️⃣
🆚
1️⃣
جمهوری چک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/133317" target="_blank">📅 10:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133316">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇲🇽
🇰🇷
مکزیک و کره نصف راه صعود را طی کردند/ جدول گروه A جام جهانی پس از پایان شب اول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133316" target="_blank">📅 10:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133315">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
‼️
باشگاه استقلال صورت مالی شش ماهه (۳۰ دی ۱۴۰۴) رو روی سایت کدال آپلود نکرده است. به این دلیل که مدارک مالی و شفافیت در بخش‌های مختلف باشگاه در راستای حرفه‌ای‌سازی از سال گذشته آماده نیست.
🚫
یکی از الزامات اصلی مجوز حرفه‌ای‌سازی است که حالا استقلال فاقد این…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/133315" target="_blank">📅 09:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133314">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZx_i71MAD1AhspGDjJzv-1rGYtEaCkvVahfxC1RDA9G0d7OGPc-JYviZBOZ2scMsrpYcS1lbq1ITUGM_mftQt75TdBSFO2lYhBZTTCJDxkw3U6hVxeLtOjvzIgn3WfMfUMYqiZIqNqUisY6U78M_fGyCpQiLM2gWW9ytLoMYBu7rirJ6ctplZ1iwLPUyI3g30M-B5yRLSzZeNZ_j2Nd0krVmGGvul8JmM7OrJ4S2lpL6O3FmEhvovWIcDbRg6UcPrTziXTWVFyX3J1deCQUZ1u5aBZeM9zw7Qdfqt7FfJOlVouSjjU__JF6Ah-t9wy_z0DMt8IZVcO1SXk3sBJw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
🇰🇷
مکزیک و کره نصف راه صعود را طی کردند/ جدول گروه A جام جهانی پس از پایان شب اول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/133314" target="_blank">📅 09:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133313">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SqJ8HcJ2r9eDbtTZ6Cel4NR4AuvjlnkngTXwEXCOBQ5jpgJU98lUcF8XyW1cVAHtYcosHWhk9-94H15nToLD9knTgZhsR8n6qRoXAHNZGqT9BkuSVn4lB7s7zxy40tlhgBZldjoop1KzbbIdqTR96xGFg-yn0xc8L_zBO2oHQclNxbcN5ylVhyMu5Ctp6X4Lpz0BtpsdAmY-AxT_JgaY35s1SpncrPJQlDPTBEfmIF7vISHZcQGMNsM8JTKs8jmViAggM5PGYUvIYb9_RgQvLqMpCpc_BniVoIthWnvyn8fjYHaxVIMFg24_jUPi0RgNiPBAm4ZccT4XR_EIBnRFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
بونوس ویژه جام‌جهانی برای تمامی کاربران به مدت محدود
🎁
به مناسبت شروع جام جهانی، برای مدت محدود
۱۰٪ بونوس ویژه واریز
برای تمامی کاربران در نظر گرفته شده است، تا با قدرت بیشتری وارد پیش‌بینی مسابقات و رقابت‌های این تورنمنت بزرگ شوید.
🎁
از همین حالا تا ۲۴ ساعت آینده ۱۰٪ بونوس ویژه روی تمامی واریزها به مناسبت آغاز جام‌جهانی که قابل استفاده برای تمامی کاربران می‌باشد به همراه یک گردش پیش‌بینی با ضریب ۱.۸
📌
برای ورود به وینکوبت از طریق ربات رسمی سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/133313" target="_blank">📅 01:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133312">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
✅
والیبال هم که زاییدیم و ست دوم هم باختیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/133312" target="_blank">📅 00:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133311">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
ادعای واشنگتن پست: رهبران عالی رتبه ایران و ایالات متحده این توافق را پس از دیدار با یکدیگر در مقابل رسانه‌ها امضا خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/133311" target="_blank">📅 00:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133310">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
ترامپ: به یک تفاهم‌نامه بسیار قوی با ایران رسیدیم و بالاخره این جنگ تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/133310" target="_blank">📅 00:24 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
