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
<img src="https://cdn4.telesco.pe/file/Q5bQerLrruWcGnfcM4v_BY8UMdOi70z9JWx__wsBi80nM3yiHVvOT3lgG9jgki6p7RCn5vznReU25PHUM_lvD-rMvj4Y7EaiLb1afDicLOc0dD3RYE6hKA4GsJqP8hC1Sm1UeScdswNAhsHFsPtp-S-x6R15YiMKz-CVnBna9QqwnLxySnb_0KHxDWjNUHmk4MRx14HMylMIxH36qE7S7sXQIfMknenwz5qMTAYuUPmaFMOfOobYb7uuD3aG3HafYwibTiG5p26N9KZrhrX0olPQiNwqG-iPC50-vESL9zm6ep3CrxDtrDgXnveMhtr5hELgfawoNxeiw7h0_KvVIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 23:52:11</div>
<hr>

<div class="tg-post" id="msg-18298">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آن 2 بند اول هم که از هنوز از تنبان توافق گشوده نشده صرفاً در برابر بازگشایی تنگه هرمز بوده.   به زبان ساده تر، یعنی ایران تنگه هرمز را بست که از کله زرد امتیاز بگیرد، اما او یک محاصره دریایی در پاسخ اجرا کرد. حالا ایران امتیازاتی را که می خواست نگرفته اما…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/SBoxxx/18298" target="_blank">📅 23:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18297">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دکتر محسن رضایی:   کاملا مشخص است که آمریکا مذاکرات را با شکست مواجه خواهد کرد</div>
<div class="tg-footer">👁️ 659 · <a href="https://t.me/SBoxxx/18297" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18296">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دکتر محسن رضایی:
کاملا مشخص است که آمریکا مذاکرات را با شکست مواجه خواهد کرد</div>
<div class="tg-footer">👁️ 713 · <a href="https://t.me/SBoxxx/18296" target="_blank">📅 23:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18295">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزیر خارجه ایران:   کشتی‌های تجاری که مسیرهای هماهنگ‌نشده‌ای با ایران دارند یا دستکاری ردیابی کشتی را انجام می‌دهند، با خطرات مواجه شده و تلاش‌های ایران برای تسهیل عبور ایمن از تنگه هرمز را مختل می‌کنند.</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SBoxxx/18295" target="_blank">📅 23:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18294">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یکی از این تعهدات  این است که کشتی هایی را که از مسیر عمان میگذرند میزنیم تا بفهمند مسیر جنوبی ناامن است و از سمت ما رد شوند</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/SBoxxx/18294" target="_blank">📅 23:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18293">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر خارجه ایران: ایران در حال انجام تعهدات خود بر اساس تفاهم‌نامه در مورد اقدامات لازم برای مدیریت تنگه هرمز است.</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/SBoxxx/18293" target="_blank">📅 22:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18292">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سپاه کشتی بعدی را هم در هرمز زد و نفت صعودی شد</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SBoxxx/18292" target="_blank">📅 22:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18291">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سپاه کشتی بعدی را هم در هرمز زد و نفت صعودی شد</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/18291" target="_blank">📅 22:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18290">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ایالات متحده مجوز فروش نفت ایران را لغو کرد</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/18290" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18289">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRed Lion Corps(M)</strong></div>
<div class="tg-text">بازی فوتبال تیم مصر و آرژانتین، چیزی تو مایه های جنگ یوم کیپور برای مصری ها شد. کمی اولش داشت خوش می‌گذشت بهشان که زمین و زمان بهم ریخت</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/18289" target="_blank">📅 21:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18288">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بح بح!
موشهای نیل به دامان طبیعت برگشتند</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/18288" target="_blank">📅 21:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18287">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خبرنگار سی‌ان‌ان:
«ترامپ در حال بررسی دادن اف-۳۵ به ترکیه است».
نتانیاهو
:
«این تعادل قدرت در خاورمیانه را نابود می‌کند. من این کار را نمی‌کردم».</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/18287" target="_blank">📅 21:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18286">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/18286" target="_blank">📅 20:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18285">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">امروز پوتین با لباس نظامی با رسانه ها گفتگو کرده و عملاً می خواهد از اعتبار و جایگاه خود دفاع کند.  حس خوبی ندارم....</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/18285" target="_blank">📅 20:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18284">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdb88acd05.mp4?token=v8SpveuXOWBFYyojGZoWdoGyd0OS_6ZxRjBAQcTnV7rxrPOQaBeCB2SfH06L9z-He3vcs7mkpNO_S0g3KtKS8bvcMfmdkK7rxW1vwWbOG7-OjlBh6r6bafgsSz2trA2CG7btUb7VGGJKQJzkq7CTA6KP-9elJ3qDlaK5dVcDPWqLFJqkKIhT1QNd5EPEDvEHYWnN_YupDLTjQhpAu62_Vnu2Oh9s7DMUA0svhZNa0SjIYNsGFAo7uW7hTCLyiNTNJgShl9HQiK9F5UBzgHxBe8g3zWI8zWqDxiY1VFS20oxouRiph8DShQjrPVdlDMmkbvtX676n0W407ytzySrWKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdb88acd05.mp4?token=v8SpveuXOWBFYyojGZoWdoGyd0OS_6ZxRjBAQcTnV7rxrPOQaBeCB2SfH06L9z-He3vcs7mkpNO_S0g3KtKS8bvcMfmdkK7rxW1vwWbOG7-OjlBh6r6bafgsSz2trA2CG7btUb7VGGJKQJzkq7CTA6KP-9elJ3qDlaK5dVcDPWqLFJqkKIhT1QNd5EPEDvEHYWnN_YupDLTjQhpAu62_Vnu2Oh9s7DMUA0svhZNa0SjIYNsGFAo7uW7hTCLyiNTNJgShl9HQiK9F5UBzgHxBe8g3zWI8zWqDxiY1VFS20oxouRiph8DShQjrPVdlDMmkbvtX676n0W407ytzySrWKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک تروریست و یک شیفته تروریست در حال امردبازی</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/18284" target="_blank">📅 20:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18283">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دبیرکل ناتو در مورد ترامپ:  من از این مرد خوشم می‌آید.  به نظرم کاری که او برای ناتو انجام می‌دهد خبری عالی است زیرا، بله، یک تهدید روسی وجود دارد، اوکراین وجود دارد، بنابراین ما در هر صورت مجبور بودیم در اروپا گامی برداریم.  اما او چیزی بود که برای ایجاد…</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/18283" target="_blank">📅 18:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18282">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">روته، نماینده ناتو در آنکارا:  ما روز سه‌شنبه در مجمع صنایع دفاعی، ده‌ها میلیارد دلار قرارداد جدید را اعلام خواهیم کرد.</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SBoxxx/18282" target="_blank">📅 18:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18281">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFJZUuA5-HPoYEnAQpUEzb2LdJYeQSg7rY4-g9-MPmvcWV7apzMoe_uhP4SQz_-Oz4XcJEsBdE1jTDyQYRyv8AcPB4z9F8l8tq4sA6abofnB8tXZzGYg71FheDC96xeHuqY9JMbrAzqASo1Mrt6o5MrPUCt9vpintB3ls982t87rgCAzTV2WQJ9fov_9wo3Y1ql_8EoSqlCB36ElAv8VgvTNv40F-_NknkElNXVBqnVgZ9bxPDQG85Cb9KgaOhQ1IrWCKWoC0qs6SYs3pi4ttq0nnxhm16HA2yB570Est3I6vJ7e84u0lSiAAWkR-6fY7gq0UGqlchxZ8YjaBKjNqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه کشتی بعدی را هم در هرمز زد و نفت صعودی شد</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/18281" target="_blank">📅 18:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18280">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6EkR859cERWqDK3cbblxpK4kJgmLtpTiusSb7vtEANf4Zi57JuXTqUGP1DG0hNQcY7NhsTB4Wv2E0DGCA622fbaH4rYhz0aLdmI_xz3fjtxz9Ga0aJpAYUW9hceMpvdflpBCrGSiOnz-9_SMtGVPfjcgyf57zB_8fWJpVbeQt5nO_ONca7OhgTb-NpqHUgu87PF1lcpdbsBJ25lCrJvR_7nynIDyHAKgR63oPzEmP1yaVIN0PxdrIt3cRKyyD-srkZ5p10QAv3a8H0VUnZXzi7ogxVC_Ecxe76Z4m0rA_3MA-PLoqoVg5r1H2Hu_xg1hnAIMUS0AGuYXAcDMXwmpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">90 درصد این دولت ها را زردپوست هایی تشکیل دادند که از دید چهره و ریختار هیچ شباهتی به این دلقک های اردوغان نداشته اند.</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/18280" target="_blank">📅 18:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18279">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سیرک جدید اردوغان!  لباس‌های تشریفاتی که نمادی از ۱۶ دولت بزرگ ترک در طول تاریخ هستند، در محوطه ریاست جمهوری مشاهده شدند و در صف ایستاده بودند تا از رئیس‌جمهور ایالات متحده، ترامپ، استقبال کنند.</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/18279" target="_blank">📅 15:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18277">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSjLhTZFyaOcRnwNv1cTJeHmzLGpoVCjFbLiE4NPAT2I3rDnnCTnD_vtSVi6tSh6G_Evt7BEKRbv0lzJs2CSRoQ_jF7VsvKbkrH-tHZ1xlObLQdofhtl6-zAQ-JzMysj3ZOALNS4U7BXicBkojNhIRnczeIRbQINGIEmcOE9losK5_MaiQabsCVJWmVYAs_cuQnFQ1yU9_K2tsYrj79bkDYvBLpUBduDI1ac1WSGyjxH7uCVZm95SXDs49NAjTMD9FFpot8X0Vev-f9OU7SDIfmzpQg6QFi36n_7qS-HL9S_U62WF_PqdL4MO2GNWrSy5W3QdGYFVPlLiBQXPfNAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NC-KvMl2FwgA-TL7Atz2_77WlYiQCvP25OQtMjpnyaDuav_LVRHZSs2gO1lriRWIrCYjkvk6EBgnlBUn93tedAbHxCU8IPYLYz4gYB1MaP9Ie3Y7X1T7pzEFRwD1Xfed4KiiMBbrnsdK0FjS2dqmcVLfU6QXlz3xHhw0rnl5Log7Ht9jepuv3XGe9G8wNW345bABk9MIjHO_mHS5g2oWmAZ5DEku-bztTAGDAsrSfxchKdPC-qOA0KakWjUEF4K7oNQ-kTg164XZQOJQxlJmhugE6t5F4di6A1c1rUxizqCS-KfMziasfvL2n7zchEEuqjOqz5gA0mNbKYDfFBshLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سیرک جدید اردوغان!
لباس‌های تشریفاتی که نمادی از ۱۶ دولت بزرگ ترک در طول تاریخ هستند، در محوطه ریاست جمهوری مشاهده شدند و در صف ایستاده بودند تا از رئیس‌جمهور ایالات متحده، ترامپ، استقبال کنند.</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/18277" target="_blank">📅 15:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18276">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حماس رسما انحلال دولت خود را اعلام کرد.</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/18276" target="_blank">📅 14:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18275">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حماس رسما انحلال دولت خود را اعلام کرد.</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/18275" target="_blank">📅 14:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18274">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حماس رسما انحلال دولت خود را اعلام کرد.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/18274" target="_blank">📅 14:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18273">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoC51aRkhxWlQjZ4gRv3fg4K2auD4NMrTXxFSOHFuzjUjoSl7BsgNdl37i3wk27vlyYoN2iriT48sK9ZrTUWsKWI9vSBHWBwCn-ofON11eU_1qPbDBDkmWtKmQ_U6QEEFZ-KiIicMl-Hk374bMGqZLScTCkCraglmYIv2fLWgL_dFEasBe6H6o3d0i7_uXm0OVpfNdMMF0Q5BQKaSIn_swO65OZy3WDSmS9MSO7IzfoacUjgQ4UCUf8I1jkfIBvcJOI7_COcsr7tXBnnRL1VEKstqjROH1FK1r9M7JSLqlZOvhM8GbnZHfQ7dFFKJAlTiDF0wSYz8e-u95GCCG-Eew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایه کشتارهای قومی بر اتحادهای ضدروسی
تنش‌های اخیر میان لهستان و اوکراین نشان می‌دهد که حتی نزدیک‌ترین متحدان نیز نمی‌توانند از سایه تاریخ بگریزند. در حالی که دو کشور از زمان آغاز تهاجم گسترده روسیه به اوکراین در سال ۲۰۲۲ همکاری‌های نظامی، امنیتی و سیاسی بی‌سابقه‌ای را تجربه کرده‌اند، اختلافات مربوط به حافظه تاریخی بار دیگر به سطح روابط دوجانبه بازگشته است. مصاحبه اخیر کیریلو بودانوف، رئیس اطلاعات نظامی اوکراین، با شبکه RBC-Ukraine نیز بازتاب همین واقعیت بود. بودانوف در واکنش به آنچه «اقدامات نابالغانه» لهستان خواند، تأکید کرد که کی‌یف نباید با واکنش‌های شتاب‌زده تنش را تشدید کند و امیدوار است پس از دوره‌ای از افزایش تنش، دو کشور به سمت کاهش تنش حرکت کنند.
زمینه این اظهارات به مجموعه‌ای از تحولات اخیر بازمی‌گردد. در آستانه یازدهم ژوئیه، سالگرد
کشتار ولین
، فضای سیاسی لهستان بار دیگر تحت تأثیر مطالبات مربوط به بازخوانی گذشته قرار گرفته است. هم‌زمان، اقدام اوکراین در نام‌گذاری یکی از یگان‌های نظامی خود به نام ارتش شورشی اوکراین (UPA)  واکنش‌های تندی را در ورشو برانگیخت. برای بخش بزرگی از جامعه لهستان، UPA  نه نماد استقلال‌خواهی، بلکه مسئول یکی از خونبارترین فجایع تاریخ معاصر این کشور است. در مقابل، بخش قابل توجهی از جامعه اوکراین این سازمان را نماد مبارزه برای استقلال در برابر سلطه شوروی می‌داند. همین تفاوت بنیادین در برداشت از تاریخ، بار دیگر شکافی عمیق میان دو متحد ایجاد کرده است.
ریشه این اختلاف به سال‌های جنگ جهانی دوم بازمی‌گردد. ارتش شورشی اوکراین (UPA) در سال ۱۹۴۲ به عنوان شاخه نظامی سازمان ملی‌گرایان اوکراین شکل گرفت. هدف اصلی این نیرو ایجاد یک دولت مستقل اوکراینی بود؛ دولتی که نه تحت سلطه آلمان نازی باشد و نه اتحاد جماهیر شوروی. اما در کنار مبارزه با این قدرت‌ها، UPA  وارد درگیری خونینی با جمعیت لهستانی ساکن مناطق ولین و گالیسیا نیز شد.
در سال‌های ۱۹۴۳ و ۱۹۴۴، نیروهای UPA مجموعه‌ای از حملات گسترده را علیه روستاهای لهستانی آغاز کردند. بسیاری از مورخان معتقدند هدف این عملیات‌ها حذف جمعیت لهستانی از مناطقی بود که ملی‌گرایان اوکراینی آن‌ها را بخشی از سرزمین آینده اوکراین می‌دانستند. اوج این خشونت‌ها در ۱۱ ژوئیه ۱۹۴۳، موسوم به «یکشنبه خونین»، رخ داد؛ روزی که ده‌ها روستای لهستانی به طور هم‌زمان هدف حمله قرار گرفتند. برآوردها نشان می‌دهد بین ۵۰ تا ۶۰ هزار لهستانی در منطقه ولین و در مجموع تا حدود ۱۰۰ هزار نفر در ولین و گالیسیا شرقی جان خود را از دست دادند. در مقابل، عملیات‌های تلافی‌جویانه نیروهای لهستانی نیز به کشته شدن چند هزار غیرنظامی اوکراینی انجامید، هرچند از نظر ابعاد و سازمان‌یافتگی، بیشتر پژوهشگران معتقدند خشونت علیه غیرنظامیان لهستانی بسیار گسترده‌تر بوده است.
همین گذشته، امروز نیز منشأ اختلاف است. پارلمان لهستان این کشتار را رسماً «نسل‌کشی» توصیف کرده و خواهان پذیرش کامل مسئولیت تاریخی از سوی اوکراین است. اما در اوکراین، اگرچه بسیاری از پژوهشگران وقوع جنایات گسترده علیه غیرنظامیان را می‌پذیرند، بخش مهمی از جامعه سیاسی همچنان UPA را نماد مقاومت ملی در برابر سلطه خارجی می‌داند و با اطلاق عنوان «نسل‌کشی» به این رویداد موافق نیست. این دو روایت متفاوت از گذشته، امکان دستیابی به یک حافظه تاریخی مشترک را بسیار دشوار کرده است.
با وجود این اختلافات، بعید است تنش‌های کنونی به فروپاشی همکاری راهبردی دو کشور منجر شود. لهستان همچنان یکی از مهم‌ترین مسیرهای انتقال کمک‌های نظامی غرب به اوکراین است و امنیت دو کشور به طور مستقیم با نتیجه جنگ روسیه و اوکراین گره خورده است. از سوی دیگر، ورشو نیز به خوبی می‌داند که تضعیف اوکراین، فشار امنیتی روسیه بر جناح شرقی ناتو را افزایش خواهد داد.
با این حال، تداوم این اختلافات می‌تواند پیامدهای ژئوپولیتیکی قابل توجهی داشته باشد. نخست، شکاف‌های تاریخی میان دو کشور می‌تواند انسجام سیاسی جبهه حامی اوکراین را تضعیف کند و روند تصمیم‌گیری در اتحادیه اروپا و ناتو را پیچیده‌تر سازد. دوم، روسیه همواره تلاش کرده است از اختلافات تاریخی میان کشورهای اروپای شرقی برای ایجاد بی‌اعتمادی و کاهش هماهنگی میان آن‌ها بهره‌برداری کند و چنین تنش‌هایی فرصت مناسبی برای عملیات اطلاعاتی و تبلیغاتی مسکو فراهم می‌آورد. در نهایت، اگر ورشو و کی‌یف نتوانند میان ضرورت‌های امنیتی امروز و اختلافات تاریخی دیروز تعادل برقرار کنند، یکی از مهم‌ترین شراکت‌های راهبردی اروپا ممکن است با چالش‌های فزاینده‌ای روبه‌رو شود؛ شراکتی که حفظ آن نه تنها برای دو کشور، بلکه برای معماری امنیتی کل قاره اروپا اهمیت اساسی دارد.</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/18273" target="_blank">📅 13:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18272">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انقلاب هوش مصنوعی و گلوگاه جدید آن؛ آیا آینده رایانش به مغز انسان وابسته خواهد شد؟   هوش مصنوعی در سال‌های اخیر، رایانش را از یک فناوری پشتیبان به یکی از مهم‌ترین منابع راهبردی جهان تبدیل کرده است. هر نسل جدید از مدل‌های هوش مصنوعی به توان پردازشی بیشتری نیاز…</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/18272" target="_blank">📅 12:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18271">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انقلاب هوش مصنوعی و گلوگاه جدید آن؛ آیا آینده رایانش به مغز انسان وابسته خواهد شد؟   هوش مصنوعی در سال‌های اخیر، رایانش را از یک فناوری پشتیبان به یکی از مهم‌ترین منابع راهبردی جهان تبدیل کرده است. هر نسل جدید از مدل‌های هوش مصنوعی به توان پردازشی بیشتری نیاز…</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SBoxxx/18271" target="_blank">📅 12:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18270">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Okm4u0sbByaeCd0VUIJOaZsfpcr7NNaqATVWCOn7GiE_QurTyOq9ocMT7inOXZULT6Jn8bYLhV3wH8zEWFAYbiZu6bERqRYISe4FR7V6Vgjw4I2Cv32aAwP7JI6kUH5yEAfNHVecRd_f105jFse-Ai_53XYoCuReInDC5MmXmiNZ0syR6i27IrCnrhAguyKbpVBACMx5Kn0lY-I7mWow95J4ZnQ8U_0NkTXHEZo2YxKOOIANKM5ojrKPZy0bJXx2wiyLDL0aV4d3nxBRA6aOEgWhzkRf_1boW7luoktiaLbi82I2ZJcjEMIjVby_4VAJS1Gu98XMGnD-B2iXGKFoRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقلاب هوش مصنوعی و گلوگاه جدید آن؛ آیا آینده رایانش به مغز انسان وابسته خواهد شد؟
هوش مصنوعی در سال‌های اخیر، رایانش را از یک فناوری پشتیبان به یکی از مهم‌ترین منابع راهبردی جهان تبدیل کرده است. هر نسل جدید از مدل‌های هوش مصنوعی به توان پردازشی بیشتری نیاز دارد و میلیون‌ها درخواست روزانه کاربران، فشار بی‌سابقه‌ای بر مراکز داده وارد می‌کند. نتیجه این روند، رشد سریع مراکز داده و افزایش چشمگیر مصرف برق آن‌ها در سراسر جهان است.
این تحول باعث شده است که انرژی از یک عامل جانبی به یکی از مهم‌ترین چالش‌های توسعه هوش مصنوعی تبدیل شود. در بسیاری از کشورها، شبکه‌های برق برای تأمین نیاز مراکز داده جدید با محدودیت مواجه هستند و شرکت‌های بزرگ فناوری سرمایه‌گذاری‌های گسترده‌ای در نیروگاه‌های هسته‌ای، انرژی‌های تجدیدپذیر، سامانه‌های خنک‌سازی پیشرفته و طراحی پردازنده‌های کم‌مصرف انجام داده‌اند. امروزه دیگر تنها پرسش این نیست که چگونه پردازنده‌های سریع‌تر ساخته شوند، بلکه این است که چگونه می‌توان انرژی لازم برای به‌کارگیری آن‌ها را فراهم کرد.
در چنین شرایطی، توان محاسباتی به یکی از مهم‌ترین منابع راهبردی جهان تبدیل شده است؛ منبعی که می‌تواند بر رشد اقتصادی، پیشرفت علمی، توان نظامی و رقابت میان قدرت‌های بزرگ تأثیر تعیین‌کننده‌ای داشته باشد. از این منظر، رقابت آینده تنها بر سر منابع انرژی نخواهد بود، بلکه بر سر تولید توان پردازشی نیز خواهد بود.
همین مسئله موجب شده است که پژوهشگران به دنبال الگوهای کاملاً جدیدی برای رایانش باشند؛ الگوهایی که بتوانند با مصرف انرژی بسیار کمتر، توان پردازشی بالایی ارائه دهند. یکی از جذاب‌ترین این مسیرها، رایانش زیستی یا Biological Computing است.
مغز انسان نمونه‌ای شگفت‌انگیز از یک سامانه پردازشی بسیار کارآمد محسوب می‌شود. این اندام تنها با مصرف حدود ۲۰ وات انرژی، وظایفی بسیار پیچیده مانند یادگیری، تشخیص الگو، تصمیم‌گیری و پردازش هم‌زمان حجم عظیمی از اطلاعات را انجام می‌دهد. در مقابل، آموزش یک مدل پیشرفته هوش مصنوعی ممکن است به هزاران پردازنده گرافیکی نیاز داشته باشد که هفته‌ها یا حتی ماه‌ها به‌صورت مداوم کار می‌کنند و انرژی بسیار زیادی مصرف می‌کنند.
همین تفاوت چشمگیر باعث شده است که برخی مراکز تحقیقاتی، امکان استفاده از نورون‌های زنده، بافت‌های عصبی و اندام‌واره‌های مغزی را برای انجام برخی وظایف محاسباتی بررسی کنند. هدف این تحقیقات، ساخت سامانه‌هایی است که بتوانند از ویژگی‌هایی مانند پردازش موازی، یادگیری تطبیقی و بهره‌وری فوق‌العاده انرژی در سامانه‌های زیستی بهره ببرند.
البته این فناوری هنوز در مراحل ابتدایی قرار دارد و فاصله زیادی تا کاربرد عملی و جایگزینی رایانه‌های مبتنی بر سیلیکون دارد. افزون بر این، مسیرهای دیگری مانند رایانش فوتونی، تراشه‌های نورومورفیک، شتاب‌دهنده‌های اختصاصی هوش مصنوعی و رایانش کوانتومی نیز با سرعت در حال توسعه هستند و هر یک می‌توانند بخشی از نیازهای آینده را برطرف کنند.
با این حال، یک واقعیت بیش از پیش آشکار می‌شود: در عصر هوش مصنوعی، توان محاسباتی در حال تبدیل شدن به یکی از ارزشمندترین منابع راهبردی جهان است؛ همان‌گونه که نفت در قرن بیستم نقشی تعیین‌کننده در اقتصاد و سیاست جهانی داشت، ظرفیت پردازش اطلاعات نیز می‌تواند به یکی از عوامل اصلی قدرت در قرن بیست‌ویکم تبدیل شود.
اگر روند رشد هوش مصنوعی با همین شتاب ادامه یابد و محدودیت‌های انرژی به یکی از موانع اصلی توسعه تبدیل شود، احتمال دارد پژوهش درباره معماری‌های نوین، از جمله رایانش زیستی، از یک حوزه صرفاً دانشگاهی به یکی از مهم‌ترین عرصه‌های رقابت فناوری تبدیل شود. هنوز مشخص نیست که آینده رایانش بر پایه سیلیکون، فوتون، سامانه‌های کوانتومی، نورون‌های زنده یا ترکیبی از آن‌ها خواهد بود؛ اما آنچه روشن به نظر می‌رسد، این است که رقابت برای دستیابی به توان پردازشی بیشتر با مصرف انرژی کمتر، یکی از مهم‌ترین رقابت‌های علمی و فناورانه دهه‌های آینده خواهد بود.</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/18270" target="_blank">📅 12:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18269">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFNM0kxOwBoYEQ04HiC34gG6oI2sgI2HAQBio-K0bCb6Q7w4fvq8V7Elr5SH3DptcWYAW-YKh0_chP2HtHATVbhggH2vy9AFmOSZZqSAB4OBGE20_FUhQ59kGKIXceOH12hQOBNynJjPk4Gr8h3bMuXT39LUiT7w0t0ELgTw2vT5zLSaBLXsP3585VATokPeoxz6icl-mmc50xHfgmikukQPitJpubLZUO7ruonLJtPo0NyfYVjtjoKMGaU_DUQUg3wpdhjF7cHGF_NuyTJq2UAz7zgx-uNRBPbA4iu2MJYWdKI5I6uC2EXEzU_BrsSAQL1t34C1i_fdzKzbyQt4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارهای پرشمار در دمشق نزدیک محل اقامت شیفته صبیه رفیق بهزاد.</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/18269" target="_blank">📅 12:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18268">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR8QdU0fTXbiKX-upS1uItK85x0EpPWKlRwdZvj1WSTLJ1CBAhFALuRxbWj04LFnouKy5tiLh4CRGNE-1rtWT41UQ8ChDLsTjWMCUa8043r3OLAL5NbcWqOqW4MnLEp6pfVlNBzFWej5dGNCM25o6WkV0mBRqE5WssMYFs5y3p3cRgDYoKnWaRRKAMvsbVVX0gpr8In4eqhUrcEW4_K6kjgQmCd9xnqUieJ2WDlgYzj5Two0AKU57jwvB0p-fYcpHYiQC0dbA6m2pr2Gv8UH3dyfooabQ8Z31GLbL0eSg7iTWIdyLObpioCbFhZxpNEdjVSb41tA3ySl3p3ZLptc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهید لاریجانی اصرار داشت با مال دیگران داماد نشوید ولی خب.</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/18268" target="_blank">📅 11:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18267">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">راه‌حل شاید ملانیا باشد!   تهدیدهای تکراری ترامپ در مورد تخریب ساختارهای اقتصادی و زیربنایی ایران در صورت شکست مذاکرات، تنها کارکردش این است که جمعیت اصطلاحاً خاموش کشور را به حمایت از جمهوری‌اسلامی و بیزاری و نگرانی از آمریکا و اپوزیسیون وابسته به آن، ترغیب…</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SBoxxx/18267" target="_blank">📅 11:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18266">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این زیدآبادی دستکم ۲ تخته اش کم است!</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/18266" target="_blank">📅 11:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18265">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">در سوریه، ایران و اسراییل مشترکا از گروه های ضدجولانی حمایت کرده و او را یک قاتل داعشی کت شلواری میدانند!</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/18265" target="_blank">📅 11:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18264">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7BiuuPmFaEB4cUVoT4uu0LaYQNwtb7BzgCt9r3Z4dsMWY7FlrEhOZ977XaFClLVS1MPNYmF_6r4bwGwW1_rSEVG2U82aRzc062CbPYadKn73XLtJenVuxpH4QSOYG9lC2X4zWE_k3jUi56tDxOmnOGrGgal1RMMxbwXabkoZGyFO0KdsWwA_DpiI9RSA7MdEb4J-V_6ycrinbr9ptj-Y4V6NUJkfkON2TC7ZS3NKYny3g3teD6zQCO0oMFJihZKd0ksHOeGfecXJ4ND_-fR3lcxJULln-i2idvwvC6aIThrT3u0zQVhgj0sI1vDWbUG1hxI8I1-uAXaUW3jWY6HWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه پایین قرار دارد و ادامه شرایط نرمال پیش بینی می شود.</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/18264" target="_blank">📅 11:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18263">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18263" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 2  دوشنبه 6 جولای 2026</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/18263" target="_blank">📅 10:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18262">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">◆ روزگاری وقتی اف 14 فول تراتل روی دریاچه ارومیه پرواز میکرد ،نعره موتور تی اف 30 تا اتاق خواب مادر الهام علی‌ اف میرفت . اما امروز تاندر تحویل گرفتند و با وضعیت فعلی آسمان ایران،می‌توانند تا تهران بیایند سلفی در کابین بگیرند برگردند . این حجم از اختلافی که…</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/18262" target="_blank">📅 10:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18261">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParvaz dar oj</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4of2MOXlZ4GRfPb0j5ZV4_s4hJD16DMvPbcWI4WBi5EnG9xtZm7VbmZWansSEub5Lgyn_cMqbPqM5xa4JRbqM4YKtWgTnrdw1sZH_1RBxtP6RzFbexeWf0DifQDNmVndOQpGc_lhmpRL_PXPLYURgPOnr5z-a60xK9KpdxcC2D-gzuLGagB8GYqBw1TU7YUuGdRFCkcrYddgqr5qRst499ldAOx2WyUJikr0dUT4gyaYgA2kmZBb-TUfFy5DzfBIqYOBdOY-FtZgspg-MlcMAjki2PlOPvmQK6MGLxkM8PTpY3KYYBLuM_NWbyy7HfI76mFNY_Ky4Oh11kSGl1C5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◆ روزگاری وقتی اف 14 فول تراتل روی دریاچه ارومیه پرواز میکرد ،نعره موتور تی اف 30 تا اتاق خواب مادر الهام علی‌ اف میرفت .
اما امروز تاندر تحویل گرفتند و با وضعیت فعلی آسمان ایران،می‌توانند تا تهران بیایند سلفی در کابین بگیرند برگردند .
این حجم از اختلافی که افتاد واقعا خرابکاری نیست،شاهکار است!!!
@PARVAZDAROJ
| 𝐀.𝐑.𝐀</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/18261" target="_blank">📅 10:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18260">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جمهوری باکو به برنامه اوکراین در زمینه پهپادها پیوست     معاون دبیر شورای امنیت ملی و دفاعی اوکراین، دیوید آلوویان، در مصاحبه با گاردین اعلام کرد که در ماه‌های اخیر، کی‌اف توافق‌نامه‌هایی در چارچوب برنامه Drone Deal با شش کشور امضا کرده است و به گفته او جمهوری…</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/18260" target="_blank">📅 10:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18259">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جمهوری باکو به برنامه اوکراین در زمینه پهپادها پیوست
معاون دبیر شورای امنیت ملی و دفاعی اوکراین، دیوید آلوویان، در مصاحبه با گاردین اعلام کرد که در ماه‌های اخیر، کی‌اف توافق‌نامه‌هایی در چارچوب برنامه Drone Deal با شش کشور امضا کرده است و به گفته او جمهوری باکو نیز در میان این کشورها قرار دارد.  این برنامه شامل توسعه مشترک، تولید و صادرات پهپادهای اوکراینی و همچنین تبادل تجربه جنگی بین کشورهای شرکت‌کننده است.</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/18259" target="_blank">📅 10:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18258">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پاسخ دبیر شورای عالی امنیت ملی به ترامپ</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/18258" target="_blank">📅 09:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18257">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cu8OGt1j19q9NFqucPYbLx8QEDvts5nvO_WeAPagM3DwLP5D4ZpJJDN_jBeiIlUFsLoQNYbUbWXjvTJ6Mn_J9MhAbYV1oqeB-ai3gBigoCq8M8LT-HKVC0SoHfEaiOl5n0woGM8niges1RZtzpPhbHBMgVwOthZhAslAYyTa-xmrqQNCDvLbIcK9OvTDxdimzlfbJyhwP2DjmGUPT56CoCPUnAqpuLybiw9XQBgI0MD-duDASozFw3mPxpJNzoW6c9_-GYINIcRIfU1xwR4sMvsnouJDir-abNtCq0XxvW-ooFhL1sFFbHMMtqYLR9uMsekNyJA5iNt46kTT14hjGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ دبیر شورای عالی امنیت ملی به ترامپ</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/18257" target="_blank">📅 09:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18256">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یک نفتکش در تنگه هرمز هدف حمله قرار گرفته است
مرکز عملیات تجاری دریایی بریتانیا: یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/18256" target="_blank">📅 09:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18255">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مسئول آمریکایی به اکسیوس:
بیبی وعده‌های زیادی درباره جنگ با ایران داد که محقق نشدند.
اما چه کاری از دستمان برمی‌آید؟ او خواهد آمد. او وعده‌هایش را می‌دهد و سپس ما مجبور خواهیم شد همه چیز را بررسی کنیم.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18255" target="_blank">📅 00:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18254">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خیلی جالب است؛  از 6 کشوری که شدیدترین بحران های انرژی را تجربه می کنند، 4 کشور در منطقه ددخیز خواهرمیانه هستند و 3 تایشان (سودان، سوریه و یمن) در ژنده پارچه ای که به عنوان پرچم رسمی معرفی کرده اند، رنگ های نجس و نحس پان عربیسم (سیاه، سفید و سرخ) دارند</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18254" target="_blank">📅 20:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18253">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqbmieuBBVElx07xnMGVYFo3O_1tgwSPZjLXRAhMpNqBEF6BLOd83INa9Vu77JRPZBvfRDHRAWCL8ZbvcbPrH_SSyj28UTSsHnyu8pTP-K9V7zdix7kjELzh8ARIWWeIyxe418DreKIrve0JQbI6qQ0cT1n9WpNbphD_K90HrmhA5wW4aj66zZTi2LRjb3dqVMcgarQ359TViZbQ1fZNj_5aPAE1RCqKSNSXSf7oUT9sP1UOY-MnFjl503RbnUj_xyfQ6xDTjHWkpRf67s3U3sTwghzskRDThcZR2NDwGP96pStk91jbBncseX1ATRaMWnurX3vQ8EPJ0UL64GoVvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما در کل این سیاره خاکی بگردید هر جا کمبود برق و انرژی باشد احتمالاً یا کمونیست هستند یا دوست دارند شبیه کمونیست ها باشند و با شکم گرسنه و خشتکی پاره مرگ بر آمریکا و مرگ بر سرمایه داری سر بدهند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18253" target="_blank">📅 20:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18252">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شبکه ملی برق کوبا روز دوشنبه دچار قطعی شد و حدود 10 میلیون نفر را بدون برق گذاشت.  مقامات اعلام کردند که علت این قطعی همچنان در حال بررسی است.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18252" target="_blank">📅 20:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18251">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گویا آمریکا می خواهد در این مدت آتش بس موقت با ایران، تکلیف کوبا را یکسره کند.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18251" target="_blank">📅 20:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18250">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نشست ناتو و 3 پویه اقتصاد دفاعی روز  افزایش هزینه‌های دفاعی در کشورهای عضو ناتو در حال تبدیل شدن به یک روند ساختاری و نه صرفاً واکنشی به تنش‌های مقطعی است. هرچند در ظاهر، این افزایش می‌تواند به‌عنوان یک محرک کوتاه‌مدت برای رشد اقتصادی تعبیر شود، اما واقعیت…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18250" target="_blank">📅 19:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18249">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ در مورد جنگ اوکراین:
به نظرم ما بسیار نزدیک‌تر از آنچه مردم تصور می‌کنند (به آتش بس) نزدیک هستیم.
پوتین می‌خواهد که این جنگ پایان یابد. من این را به شما به شدت می‌گویم. ما یک تماس خوب داشتیم.
زلنسکی در واقع می‌خواهد که این جنگ همین حالا پایان یابد.
ما می‌خواهیم به ناتو برویم و می‌خواهیم در مورد آن صحبت کنیم. و من فکر می‌کنیم که می‌خواهیم آن را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18249" target="_blank">📅 18:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18247">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
بمب خبری ... اولین حضور رهبر معظم انقلاب آقای مجتبی خامنه‌ای در تشییع و نماز برای پدرشان در مصلای تهران  https://t.me/+SV6YYFA0zX1kOGZk</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18247" target="_blank">📅 15:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18246">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEhsan Movahedian Channel</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a018aa532.mp4?token=A-d-2aOvamTI1T8O-a4XneRqnC_nIZuGxrLwiJAN2HhP_y97bPf52ObV9_UM1PB5RUCD-2KZgFqNUpa2s9lFplL5sGTpulGGpkLfmOtDt6Jx1P32QsH1BN5FhTcz82uUPd32HHzg9wD3Oy6Eo5bMLEFHWZPDOCmrKixaFJ84hl1jxi8vInanyvMkiAyIr6Nx54o9QBHnqRmwWXH9OjwPODzi64fVfun6DojmRxkwBTz-S5ypkJPUqhZRHpXXruBtyFWeYXYvNd12NJPmsjKODGNgJJcH7LLL9xMysOVg-igoPYF1p7dIsKx0Bf8vxzbQkILmGNIYU4xk9XrnkJW7Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a018aa532.mp4?token=A-d-2aOvamTI1T8O-a4XneRqnC_nIZuGxrLwiJAN2HhP_y97bPf52ObV9_UM1PB5RUCD-2KZgFqNUpa2s9lFplL5sGTpulGGpkLfmOtDt6Jx1P32QsH1BN5FhTcz82uUPd32HHzg9wD3Oy6Eo5bMLEFHWZPDOCmrKixaFJ84hl1jxi8vInanyvMkiAyIr6Nx54o9QBHnqRmwWXH9OjwPODzi64fVfun6DojmRxkwBTz-S5ypkJPUqhZRHpXXruBtyFWeYXYvNd12NJPmsjKODGNgJJcH7LLL9xMysOVg-igoPYF1p7dIsKx0Bf8vxzbQkILmGNIYU4xk9XrnkJW7Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بمب خبری ...
اولین حضور رهبر معظم انقلاب آقای مجتبی خامنه‌ای در تشییع و نماز برای پدرشان در مصلای تهران
https://t.me/+SV6YYFA0zX1kOGZk</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18246" target="_blank">📅 15:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18245">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ونس: ظرفیت تهاجمی روسیه نزدیک به صفر رسیده است   در مصاحبه‌ای با تایمز بریتانیا، جی‌دی ونس، معاون رئیس‌جمهور ایالات متحده، وضعیت نظامی روسیه را ناپایدار ارزیابی کرد.   ارزیابی او: توانایی روسیه برای عملیات‌های تهاجمی بیشتر «ناچیز و تقریباً صفر» است. این می‌تواند…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18245" target="_blank">📅 15:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18244">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 2  دوشنبه 6 جولای 2026</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18244" target="_blank">📅 15:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18243">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEHWKz20PizlHLuhsiH-dJz3MV-YBKMZxRvTHB0UpEPFNSLfN99VgPlir_QM_h-b8DH59_UceNp7nYzRUuKKE5r1mxZWT7RkYT9CMwPvvDBSgwtlfrFY_k3RDskMAYSZ5hCYer0Np4ePpJmOE6YGxf0pg-q4FaKxXPuWnijwgsRMbtT-YA1wCQJ2qNpdhqHD1Zv_vLt_Ug7gmiKO1MaDc_mFd5iXGr2WyupblVtQdAPqg54RyFrAJh4N2pCauuW3iT9FMluiOms78I_Ft14mfA-OTpklbjGh82ZGuqHBmj6iPGn55pRXmiOfYRomBpYvKY3t3AQDzifvr63iQVunGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرانجام کتابی که وعده دادم درباره پیوند ژئوپولیتیک و بازارهای مالی ترجمه کنم، به چاپ رسید.  به نظرم در این شرایط که چندین جنگ همزمان در منطقه و جهان در جریان است و تنشهایی که میتواند بزودی تبدیل به جنگ های دیگری بشود، فقدان وجود یک دیدگاه تحلیلی چهارچوب بندی…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18243" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18242">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/18242" target="_blank">📅 12:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نشست ناتو و 3 پویه اقتصاد دفاعی روز
افزایش هزینه‌های دفاعی در کشورهای عضو ناتو در حال تبدیل شدن به یک روند ساختاری و نه صرفاً واکنشی به تنش‌های مقطعی است. هرچند در ظاهر، این افزایش می‌تواند به‌عنوان یک محرک کوتاه‌مدت برای رشد اقتصادی تعبیر شود، اما واقعیت اقتصادی پیچیده‌تر از این برداشت خطی است. هزینه‌های دفاعی معمولاً با تأخیر وارد چرخه تولید و تقاضا می‌شوند و اثر آن‌ها به‌صورت تدریجی در اقتصاد پخش می‌شود. تجربه‌های تاریخی، مانند بازسازی ذخایر تسلیحاتی آمریکا پس از جنگ خلیج فارس که چندین سال به طول انجامید، نشان می‌دهد که این نوع هزینه‌ها به‌جای ایجاد شوک‌های فوری، بیشتر اثرات میان‌مدت و بلندمدت دارند.
در سطح ساختاری، ماهیت خریدهای نظامی نیز در حال تغییر است. جنگ اوکراین و استفاده گسترده از پهپادها در عملیات علیه روسیه و کریمه، نشان داده که فناوری‌های کم‌هزینه‌تر و غیرمتقارن در حال بازتعریف اولویت‌های نظامی هستند. این تحول به‌طور مستقیم بر زنجیره تأمین دفاعی اثر می‌گذارد و تقاضا را از سامانه‌های سنگین سنتی به سمت فناوری‌های سبک‌تر، هوشمندتر و مبتنی بر داده سوق می‌دهد.
از منظر ژئو‌اقتصادی، یکی از روندهای مهم، بازتنظیم روابط تأمین‌کنندگان تسلیحات است. اروپا به‌تدریج در حال کاهش وابستگی به تجهیزات نظامی آمریکاست و به سمت توسعه ظرفیت‌های داخلی یا تنوع‌بخشی به شرکای خود حرکت می‌کند. این تغییر می‌تواند در بلندمدت ساختار صنعت دفاعی غرب را دگرگون کند.
در این میان، خاورمیانه نیز به‌عنوان یکی از بزرگ‌ترین واردکنندگان تسلیحات، نقش تعیین‌کننده‌ای در جهت‌دهی به جریان سرمایه و فناوری نظامی دارد. این که بودجه‌های دفاعی کشورهای منطقه به چه نوع فناوری و از چه کشورهایی تخصیص یابد، می‌تواند بر رقابت جهانی صنایع دفاعی اثر قابل توجهی بگذارد. در مجموع، آنچه امروز مشاهده می‌شود نه صرفاً افزایش هزینه، بلکه بازآرایی عمیق در معماری اقتصاد دفاعی جهانی است.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18241" target="_blank">📅 11:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcEV3FYh8KXd9uGr_XT2wXMg12wgqvML6bgjsZrUjV-Ur3hMKMa5piJ2MCjNn-Cu5SDPXzwHrt3LHX2XO3Ut0OzSgz_GPWZXdihMJcGx9J_OB3oDlaZlcew8ZvsMomxMgZRNyQnvkt68G5BgxHRmszSqJY72WGICo_CXMaLHtW7RUJb1_HigaeljBs0tWvaZ5kasGC0jvE-8vnSjytmaO0sLWluKBAn7er_AvJph6b50EJYU6L5JqGOtolq3GptLPONXqpooNL5mx5FeWDHNCVBXXwsuFTGWxM5_FybeK-jSUXqc-IVORX54GCkO7O6FgjSX3X3EwSCIoNJrIpuj2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتک برای امروز در سطح میانه پایین قرار دارد و ریسک پذیری بسیار ملایم پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/18240" target="_blank">📅 11:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18239">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18239" target="_blank">📅 10:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18238">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شبکه ۱۴ اسرائیل:
سپاه قدس واحد جدیدی به نام « یگان مختار » تشکیل داده است که با شهروندان مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18238" target="_blank">📅 10:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18237">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18237" target="_blank">📅 10:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18236">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePs39fMqD3NO9d9RkFQGChAjUZwVmdOsIHzx6QPUHH208IVQJh6dB1ABfYwBe11NfA-4xSO901PM0rSmnGN2mXMot29S8ksqcJzIRRaot5UHgtm8EAqBcIC96tyETAWv2yaaMAHfvhsJj9FRuIcMNW6Iec1L9PruHH7jPQhrIWZAx4Yt2eTf49Hw8il9GTnKtu0t3ChkvFskxcmsAw24dRtQ1VPI2SenmgaPzApWi9kr-B2ZvIT7c6sWOlqDOHTO_VnXK1RxM3tUj9JZGEV59jHfpbH5bKrbguvfCURQy7DL5MwJtTV4Rwwy9S9XBTdSopwXnEz_LhomARVHJdyLDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ گویا واقعاً زنگ زده اینفانتینیو و گفته یا بازیکن اخراجی ما را می بخشید یا بازی خراب!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18236" target="_blank">📅 09:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18235">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18235" target="_blank">📅 22:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18234">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iY9EkUq5EQQ_gLUVTJA4MoymuKvuPxYxi4ZJ7Wt2zqCJIWn5ZFm-zBIxjAVulr-CLWWIDh53l_8Rg__XTiChbsS9BHMxUE9Ik1tYK_inXrim9RNp4tmM1ITTnB3vuQaMEroaLjGgaQ_T05xw4Is_kRu0pIIlCzn7BEhBKG7NfQSnA4hYUDFksOsqgSLXtoNc6RYbmRP189Pn9VdJlDNaaqxLKSeWyWcuA2GyEzdZMb83iCVKWQl6zr8-zjH_rraZ6gfVXSjzIHT5p1mKORJjX6HNbqixrFUmTn1fZDxmP08ynI-gDE2OK_mvS-0J3LM1fnfFW0GTAOLokeJXmp3BGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
استقرار بالن نظارتی (الکترواپتیکی)  در آسمان تهران</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18234" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18233">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتانیاهو:
«برخی روستاهای مسیحی‌نشین لبنان در واقع درخواست الحاق به اسرائیل را داده‌اند، زیرا ما از آنها در برابر حزب‌الله محافظت می‌کنیم.»</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18233" target="_blank">📅 21:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18232">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ایران می‌گوید از آتش‌بس با ایالات متحده برای تقویت آمادگی رزمی خود استفاده می‌کند.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18232" target="_blank">📅 20:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18231">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دو نکته:  — از این میان ما سومی (J-20) را داریم. (البته ماکت ش)  — آخری (جنگنده کان یا خان ترکیه) فقط یک مشکل کوچک دارد و آن اینکه موتورش هنوز پیدا نشده که انشالله این هم حل می شود.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18231" target="_blank">📅 17:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18230">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
چرا نتوانستیم از صدام حسین غرامت بگیریم؟  حمزه رحیم صفوی.  @MonazeratChannel</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18230" target="_blank">📅 16:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18229">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمناظره‌ها</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f11f469c.mp4?token=oTwrMuJS1yGrrB8uvRHZt0zUCe0V67xd4jFUTXR9nrLtgcFFb2prUeznsxfSMabFPeIrdPcQe989ZlMx9eaWobBw0GNMndGQO-1BAdElUe2IrtpYayxK1GriE9CsPa6HROc82zHuXu5qjoy8Y0FXQOMASRhyPjBPPO19cgJc_EHtN2VbCr9O6xLCMfmI66iRR6koKxlGeo31DClpt_Mbr26ausqUOSyZhmLeIZKBqVL8XO2e7fkbtViVBOl4ZarWX0-xi9FN3wydtG4vYoJS4MneHGsEKnTOd3I6ptnumTyjKZAceEQfp04rXeWcFDNE0I-KiSXUmSHuafaaawk0Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f11f469c.mp4?token=oTwrMuJS1yGrrB8uvRHZt0zUCe0V67xd4jFUTXR9nrLtgcFFb2prUeznsxfSMabFPeIrdPcQe989ZlMx9eaWobBw0GNMndGQO-1BAdElUe2IrtpYayxK1GriE9CsPa6HROc82zHuXu5qjoy8Y0FXQOMASRhyPjBPPO19cgJc_EHtN2VbCr9O6xLCMfmI66iRR6koKxlGeo31DClpt_Mbr26ausqUOSyZhmLeIZKBqVL8XO2e7fkbtViVBOl4ZarWX0-xi9FN3wydtG4vYoJS4MneHGsEKnTOd3I6ptnumTyjKZAceEQfp04rXeWcFDNE0I-KiSXUmSHuafaaawk0Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چرا نتوانستیم از صدام حسین غرامت بگیریم؟  حمزه رحیم صفوی.
@MonazeratChannel</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18229" target="_blank">📅 16:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18228">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18228" target="_blank">📅 15:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18227">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مسؤولان آمریکایی نگران بودند که اسرائیل ممکن است در طول مذاکرات صلح حساس در بهار امسال، از جمله وزیر امور خارجه عباس عراقچی و رئیس مجلس محمدباقر قالیباف، رهبران مذاکره‌کننده ایران را ترور کند.  با نگرانی از اینکه چنین حمله‌ای مذاکرات را متوقف کرده و جنگ را…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18227" target="_blank">📅 15:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18226">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">📌
وخیم تر شدن وضعیت صنعت آلمان در اثر جنگ خاورمیانه  صنعت آلمان که پیش‌تر هم تحت فشار بود، با آغاز جنگ خاورمیانه، افت تولید صنعتی، کاهش رشد صادرات و افت محسوس مازاد تجاری در مارس، وارد وضعیت ضعیف‌تری شده و احتمال بازبینی نزولی رشد اقتصادی سه‌ماهه اول را بالا…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18226" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18225">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">قالیباف، در مراسم تشییع رهبر سابق ایران:  «ثمره خون خامنه‌ای آزادی بیت المقدس خواهد بود».</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18225" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18224">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18224" target="_blank">📅 12:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18223">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کلا خاطره خوبی از محاسبه خسارات و جمع آوری شواهد نداریم.
بار پیش
هم که جناب عراقچی داشتند خسارات اشتباه محاسباتی اسراییل در جنگ ۱۲-روزه را محاسبه می‌کردند که اشتباه محاسباتی بعدی روی داد و اصلا محاسبات ما به هم ریخت.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18223" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18222">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18222" target="_blank">📅 12:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18221">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:
"ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18221" target="_blank">📅 12:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18220">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">Trump Accounts
سرمایه‌گذاری بر نسل آینده یا
پروژه‌ای سیاسی؟
دولت دونالد ترامپ با معرفی طرح «Trump Accounts» تلاش کرده است ایده‌ای را به اجرا بگذارد که در ظاهر، حمایت از آینده مالی کودکان آمریکایی را هدف قرار داده است. بر اساس این برنامه، برای هر کودک واجد شرایط، حسابی سرمایه‌گذاری ایجاد می‌شود و دولت برای نوزادان متولدشده در بازه زمانی تعیین‌شده، مبلغ اولیه‌ای را به این حساب واریز می‌کند. دارایی این حساب‌ها نیز در صندوق‌های شاخص کم‌هزینه سرمایه‌گذاری می‌شود تا در بلندمدت از رشد بازار سهام بهره‌مند شود.
طرفداران این طرح معتقدند که ایجاد سرمایه از ابتدای زندگی می‌تواند فرهنگ پس‌انداز و سرمایه‌گذاری را در جامعه آمریکا تقویت کند. از نگاه آنان، حتی یک سرمایه اولیه نسبتاً کوچک نیز در صورت رشد مستمر بازار، می‌تواند هنگام ورود فرد به بزرگسالی به منبعی برای تأمین هزینه تحصیل، خرید نخستین مسکن یا آغاز یک کسب‌وکار تبدیل شود. این رویکرد همچنین می‌تواند وابستگی شهروندان به کمک‌های مستقیم دولت را کاهش داده و مشارکت آنان در اقتصاد و بازار سرمایه را افزایش دهد.
در مقابل، منتقدان بر این باورند که اثر واقعی این برنامه به توانایی خانواده‌ها برای واریز مبالغ بیشتر به حساب فرزندانشان بستگی دارد. از این منظر، خانواده‌های پردرآمد بیش از دیگران از مزایای رشد سرمایه برخوردار خواهند شد و در نتیجه، شکاف ثروت میان طبقات مختلف جامعه ممکن است کاهش نیابد و حتی در بلندمدت افزایش پیدا کند. همچنین برخی ناظران، انتخاب نام «Trump Accounts» را اقدامی با رنگ‌وبوی سیاسی می‌دانند که می‌تواند این برنامه را به بخشی از میراث سیاسی رئیس‌جمهور تبدیل کند.
در مجموع، موفقیت یا شکست «Trump Accounts» به عملکرد بازارهای مالی، میزان مشارکت خانواده‌ها و نحوه اجرای مقررات آن وابسته خواهد بود. اگرچه این طرح می‌تواند گامی در جهت گسترش سرمایه‌گذاری عمومی باشد، اما قضاوت نهایی درباره آثار اقتصادی و اجتماعی آن تنها پس از گذشت چند سال و مشاهده نتایج عملی امکان‌پذیر خواهد بود.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18220" target="_blank">📅 11:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18219">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رئیس‌جمهور فرانسه ماکرون:
فرانسه دارایی‌های ضد مین را به خاورمیانه اعزام کرده است، از جمله به‌ویژه دو کشتی  ویژه جستجوگر مین
همراه با دو ناوچه و یک هواپیمای گشت دریایی، این دارایی‌ها آماده هستند تا در کنار شرکای ما، به از سرگیری کامل کشتیرانی و تضمین ایمنی ترافیک در تنگه هرمز کمک کنند</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18219" target="_blank">📅 08:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18218">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔻
پناهیان ؛ مشاوره ریاست نهاد نمایندگی رهبر در دانشگاه‌ها :
حاضریم تمامی منافع ملی را فدای خونخواهی رهبر شهیدمان کنیم</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/18218" target="_blank">📅 23:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18217">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔻
بابک زنجانی
:
به زودی خونخواهی رهبر شهید شروع خواهد شد و آن خون خواهی اقتصادی است</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/18217" target="_blank">📅 23:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18216">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ایران قصد دارد به چین تعرفه‌های ترجیحی برای تنگه هرمز ارائه دهد
تهران قصد دارد به چین و سایر کشورهای دوستانه تعرفه‌های ترجیحی برای هزینه‌های عبور و مرور ورودی تنگه هرمز اعطا کند.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18216" target="_blank">📅 22:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18215">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">به گزارش کانال 15 اسرائیل، دونالد ترامپ از اسرائیل خواسته است که فعالیت‌های نظامی خود را در لبنان افزایش ندهد، زیرا نمی‌خواهد این امر در مذاکرات جاری او با ایران دخالت کند.
به همین دلیل،  نتانیاهو یک عملیات نظامی که پیش از این برای منطقه علی‌الطاهر برنامه‌ریزی شده بود، را به تعویق انداخته است.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18215" target="_blank">📅 22:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18214">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رئیس‌جمهور عراق:   عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18214" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18213">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رئیس‌جمهور عراق:
عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18213" target="_blank">📅 21:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18212">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، گفت که آمریکا می‌توانست رهبران ایران را که برای مراسم تشییع آیت‌الله علی خامنه‌ای، رهبر پیشین، جمع شده بودند، هدف قرار دهد، اما این کار را انجام نمی‌دهد زیرا می‌خواهد مذاکرات هسته‌ای را حفظ کند.  «همه آن‌ها آنجا هستند. با یک…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18212" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18211">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، گفت که آمریکا می‌توانست رهبران ایران را که برای مراسم تشییع آیت‌الله علی خامنه‌ای، رهبر پیشین، جمع شده بودند، هدف قرار دهد، اما این کار را انجام نمی‌دهد زیرا می‌خواهد مذاکرات هسته‌ای را حفظ کند.
«همه آن‌ها آنجا هستند. با یک شلیک [می‌توانیم همه آن‌ها را از بین ببریم]، اما این کار را نخواهیم کرد زیرا در آن صورت کسی برای مذاکره باقی نخواهد ماند»</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/18211" target="_blank">📅 20:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18210">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اردوغان به اسرائیل هشدار داد: "نباید اجازه داد اسرائیل منطقه را در خون غرق کند."
رئیس‌جمهور ترکیه، اردوغان، در سخنانی مشترک با نخست‌وزیر پاکستان، لحن تندی علیه اسرائیل اتخاذ کرد.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18210" target="_blank">📅 20:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18209">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">باز این پفیوزها می خواهند تندروهای داخلی را تحریک کنند تا تنگه را ببندند و قیمت نفت بالا برود و غرب از کمک بیشتر به اوکراین که خشتک روسها را بر کله شان کشیده منصرف بشود.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18209" target="_blank">📅 18:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18208">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترکیه با موفقیت موشک بالستیک TAYFUN Block-3 را علیه هدف کشتی متحرک با سرعت هایپرسونیک آزمایش کرد.
شرکت ROKETSAN یک آزمایش آتش‌زنده از موشک بالستیک TAYFUN Block-3 انجام داد و با موفقیت یک کشتی سطحی بدون سرنشین آزاد در حرکت را در دریا با یک سر جنگی زنده با سرعت هایپرسونیک هدف قرار داد.
هدف حدوداً ۷ متری — که یک قایق ماهیگیری کوچک بود — با آنچه شرکت آن را «دقت جراحی‌گونه» توصیف کرد، نابود شد.
این آزمایش نخستین مورد از این دست است که در آن یک موشک بالستیک که با استفاده از سر جستجوگر برای هدایت در مرحله پایانی، یک کشتی سطحی متحرک را در دریا درگیر و هدف قرار می‌دهد.
ترکیه می‌گوید این نخستین یکپارچه‌سازی چنین سر جستجوگری بر روی یک موشک بالستیک در داخل کشور است و یکی از تنها چند نمونه در سراسر جهان — قابلیتی که به طور موثر یک موشک بالستیک را به یک سلاح ضد کشتی تبدیل می‌کند.
سرعت پایانی هایپرسونیک TAYFUN آن را تا حد زیادی در برابر پدافند‌های متعارف دفاع هوایی مصون می‌سازد.
نسخه Block-3 پیشرفته‌ترین نسخه از برنامه موشک بالستیک توسعه‌یافته داخلی ترکیه را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18208" target="_blank">📅 18:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18207">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یک کارشناس:
به نظر می‌رسد که ایران در مراسم تشییع جنازه رهبر خود هر هیئت خارجی را با یک آیه قرآن مرتبط کرده است که هدف سیاسی خاصی را دنبال می‌کند.
عربستان سعودی: آیه ای درباره دو ارتش که در جنگ با یکدیگر روبرو می‌شوند، یکی مومن و دیگری غیرمومن.
ترکیه: آیه ای که کسانی را که در راه خدا می‌جنگند، بر کسانی که "نشسته"اند، برتری می‌بخشد.
دولت لبنان: آیه ای درباره افرادی که در صورت درخواست، از انجام فداکاری خودداری می‌کنند.
حزب الله: به آنها گفته شد "ضعیف نشوید یا غمگین نشوید، شما برتر هستید."
حماس: آیه ای که مردانی را که عهد خود را با خدا وفا کردند، مورد تقدیر قرار می‌دهد، "برخی از دنیا رفته‌اند، و برخی دیگر در انتظارند."
حوثی‌های یمن: آیه ای که به مومنانی که بدون سستی جنگیدند، ستایش می‌کند.
قطر: آیه ای درباره بخشش و لطف الهی، که به عنوان اشاره‌ای به نقش میانجی‌گری این کشور خوانده شد.</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SBoxxx/18207" target="_blank">📅 13:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18206">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اظهارات مدودف، نخست‌وزیر روسیه:  ایران به جای سلاح‌های هسته‌ای، سلاح دیگری را کشف کرده است که از نظر قدرت، نه ضعیف‌تر از سلاح‌های هسته‌ای است و آن، تنگه هرمز است.  بحث‌ها حول این موضوع است که چگونه باید به توافقی دست یافت تا این تنگه در آینده به چه صورت عمل…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18206" target="_blank">📅 13:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18205">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جناب الکساندر سرگین هستند از گه خورهای اعظم که بیرون گود نشسته و به ما میگویند لنگش کن!</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/18205" target="_blank">📅 13:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18204">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I97z51HZq_rGp51FVGl5v7Vh0yGOIavIz9q8zUgFdoQuVx0IMKrygcRvCGQ74kGe_J2rRPNy3hw4_5QGgyWFhpVV73zqh-DL_qMkPfL6-Sf8__pv69Hj9TAoujW-VnuZnF8Um2i-aIx1kTWewFa8fL8HTtKJcmW792WFKxjKLf8Mw4xe6X9M_lw7JBvXHKcc9A9O-PRSsOaGn-t_wDEyTsROJ-vX4VIsxqrYUv6wU_RlQ-6RVaRF2QlVqsU-ml3yMmU2ARxPNnIek7jTHbLL98n19RmqJ7Q7oCdF62pbAfmw84GYguGKaeVmfPSHST761yoBKQoef3dmUnQ9xNKSYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس ترنس هست اما نجس هم هست؟!</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18204" target="_blank">📅 12:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18203">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رسانه‌های غربی:
عمان قصد دارد پای کشورهای‌اروپایی را به تنگه‌ی هرمز باز کند و از آنجا که ایران قرارداد تقسیم تنگه را با عمان به امضا رسانده دیگر حق قانونی برای جلوگیری از این موضود ندارد.
در اولین قدم نیروی دریایی فرانسه قصد دارد در تنگه هرمز مستقر شود</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/18203" target="_blank">📅 10:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18202">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">امروز پوتین با لباس نظامی با رسانه ها گفتگو کرده و عملاً می خواهد از اعتبار و جایگاه خود دفاع کند.  حس خوبی ندارم....</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/18202" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18201">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ
:
ما مناقشه با ونزوئلا را در یک روز حل و فصل کردیم و ضربات بسیار سختی به ایران وارد کردیم.
طرف ایرانی بسیار مشتاق است و به هر طریقی به دنبال دستیابی به یک توافق سیاسی با ما است.
ما از روی حسن نیت به ایران یک هفته فرصت دادیم تا عملیات را متوقف کند تا مراسم تشییع جنازه برگزار شود.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/18201" target="_blank">📅 09:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18200">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-A7Qahpb2R54iLCRwGhiGod9rCOkxeF0mhuVAyC2mpi8Ptdjg3i-6pEU_v9DIPpkbj_KsGPbcV9cGW0crphDF1XLVJv9otDkZoYGEAPeeZ4GCOG3D_k9flHa5tXlMDLMXJQcibd21wyQdXfSLqs91qOb1NgHqr59Kq5egaqNar8rGHLf2fEXamQh_Lfp-71KyXnFaajZyKuQRyjTrdHKdpyxtL4uoxRb1_4EyM0H3fe6AUCFavaoy7FSntm0yMstoB1bu8xLKY6yRgmJYmhztDGLyVGmVFfaxJS0eTWn8Xrta45M69zhhQbw2rghXITpz0VOvPBj8wyFPAZ8q6zzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر جنگ هسته ای؟!
ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. د
ر ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی»
عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که نزدیک‌ترین فاصله به نقطه نمادین فاجعه جهانی در تاریخ است. این سازمان، تضعیف امنیت بین‌المللی، ضعف چارچوب‌های کنترل تسلیحات و رفتارهای فزاینده پرخاشگرانه قدرت‌های بزرگ را به عنوان دلایل اصلی این تصمیم ذکر کرد.
یکی از واضح‌ترین نشانه‌های این تضعیف، افزایش بکارگیری اصطلاحات هسته‌ای در گفتمان سیاسی و پوشش رسانه‌ای است. عباراتی مانند «حمله هسته‌ای»، «ضربه هسته‌ای»، «تهدید اتمی» و «تشدید هسته‌ای» بسیار بیشتر از چند سال پیش به کار می‌روند. در حالی که عبارت «حمله اتمی» بیشتر با اوایل جنگ سرد مرتبط است، گزارش‌های مدرن ترجیح می‌دهند از اصطلاحاتی مانند «حمله هسته‌ای» و «تهدید هسته‌ای» استفاده کنند. این تغییر نه تنها نشان‌دهنده تغییر زبان، بلکه نگرانی مجددی است که سلاح‌های هسته‌ای دوباره در محاسبات استراتژیک نقش مرکزی پیدا کرده‌اند.
جنگ در اوکراین نقش عمده‌ای در این روند داشته است. از آغاز این درگیری، مقامات روسی بارها امکان استفاده از سلاح‌های هسته‌ای را مطرح کرده‌اند، در حالی که دولت‌های غربی و تحلیلگران درباره اعتبار این تهدیدات بحث کرده‌اند. بولتن به طور خاص اشاره کرده است که جنگ روسیه و اوکراین با تحولات نظامی بی‌ثبات‌کننده و ارجاعات مکرر روسیه به سلاح‌های هسته‌ای همراه بوده است، که خطر محاسبه نادرست بین کشورهای دارای سلاح هسته‌ای را افزایش داده است. شکست‌های نظامی اخیر و فشارهای اقتصادی رو به رشد، بحث‌ها درباره گزینه‌های استراتژیک روسیه را تشدید کرده‌اند. گزارش‌ها و تحلیل‌ها بر فشارهایی که یک درگیری طولانی‌مدت بر تولید صنعتی، تحریم‌ها و زیرساخت‌های انرژی تحمیل کرده است، تأکید داشته‌اند. این فشارها باعث شده است که برخی تحلیلگران گمانه‌زنی کنند که مسکو ممکن است برای بازدارندگی از مداخله بیشتر غرب، بیشتر به سیگنال‌های هسته‌ای متکی شود. با این حال، فعلاً و در شرایط کنونی گمانه‌زنی درباره تصمیمات آینده روسیه نباید با شواهدی مبنی بر استفاده قریب‌الوقوع از سلاح‌های هسته‌ای اشتباه گرفته شود. کارشناسان نظامی و سیاسی عموماً چنین گفتمانی را بیشتر ابزاری برای اجبار و بازدارندگی می‌دانند تا نشانه‌ای قابل اعتماد از استفاده نزدیک از سلاح‌های هسته‌ای. با این حال کمبود گسترده بنزین و گازوئیل یا صف‌های طولانی سوخت در سراسر روسیه  بشدت روی روحیه و غرور ملی روسها تاثیر منفی گذاشته اند و برای نخستین بار از سال 2006 به این سو، مردم روسیه تصور می کنند استانداردهای کیفیت زندگی شان رو به نزول نهاده است. این مسئله روی پوتین و هیات حاکمه روسیه فشار می آورد تا دست به اقدامات تهاجمی تری برای تسلیم کردن اوکراین و ناتو بزنند که یکی از آنها می تواند بهره گیری از سلاحهای کشتار جمعی باشد.
از سوی دیگر، ناکامی نسبی آمریکا در دستیابی به همه اهداف نظامی اش در ایران نیز می تواند از دیگر حوزه هایی باشد که نهایتاً ترامپ را به استفاده از سلاح های هسته ای وادار کند. در این حوزه می توان به اشاره ترامپ به راهبرد «شرمن» استناد کرد که استعاره ای از یک استراتژی ویرانگر مخرب با تلفات بالا برای به تسلیم کشاندن دشمن می باشد. (
لینک
)</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/18200" target="_blank">📅 02:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18199">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cH32JTmJ_Ois7in_b6LoIpQCMfEFSwqcmTerHB8XLxgzvVWGMjBpVluWyNp_AD-NiBOi5fZGGn69ya0D1hS-ytP9T5xySkS4invbYDp_YunS85SM5_MP3OH93OJPaLpWE_nPGx1yokbuXPOxs0qK7H0lPtcFxgAaU5vbvJDPC2VR52vAmoYqYfK0XqUYaOS6BLwMzzf7wT5vc0060d1uhBR1EzXNEhGsDObSBICupXrKJXiPk6UdOoOcHQNDTfchM639CUzPVOsMgBVqFG5HLp7VtITzrOMqg3BmMER-anPFJfnBDObfn_5jyFLLet5w76u64fa_Q6F_momyx5LWBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در اینجا گفته شد که پوتین مانند گربه ای در گوشه اتاقی بسته گیر افتاده و این خطرناک است</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/18199" target="_blank">📅 01:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18198">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laKoEznywAFRdrExyBdd3JxeD5pxGOGhcB2xoV0qWqD12j775L--Q1WIXpQuASFCDK_ZMiFVrJcw3mMeD09PufMKJwyeYsGIIFm0S_uL72hXE3WBqsqQF9eVwpejP9j448fE1pZu9vxJoCnxbMjBETkAFrCQ9Syb_wtdO6f1VxM_lR_JkHIzR5gcCTfYG5_KirxWa78-0Percp_6NnYff3HVs-vI6zWzwYUU7tnsI-RADsydE2SAZLzbzv5kpr1UYML6Y7YbWttLXE20IzwXcZ0pf0CjhEzW1pw-9JtpZv2iFqmewQ0B_gD-xTqCMe0R6e_C-zApgXu7iZ5HoJgjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/18198" target="_blank">📅 01:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18197">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دونالد ترامپ در آخرین افشای مالی سالانه خود گزارش داد که در سال ۲۰۲۵ حداقل ۱.۴ میلیارد دلار از کسب‌وکارهای مربوط به ارزهای دیجیتال و میم‌کوین‌ها درآمد داشته است. ارزهای دیجیتال به‌وضوح بزرگ‌ترین منبع درآمد او بوده‌اند.   این گزارش همچنین نشان داد که او ۲۶…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/18197" target="_blank">📅 22:06 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
