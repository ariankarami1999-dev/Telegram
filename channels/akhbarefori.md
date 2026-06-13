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
<img src="https://cdn4.telesco.pe/file/b1MYv6YLwpoFWyMIZLBnPD24CLM0L6ugBUnV5nML0E86Oj-FgEFl9ymInWdlKKR_-Ycew9KbdKaPahTliDaGpJIe6LLmmefVconyty7BS-0pH7yPzcanNNue2J0Q3J0TV26bho4OdromKBv4oOyT37Wub6YqrwuQ2p3YngvXGKzr6MmZJAyTzKvpXL7oA8d2Yc858W67ZA5slhWZyAADBLbz0zQPapc9RQgdiFmsFTHgT_J99AVYN9XIGk2-SQdtXEzfcpoijZ25y2pE4OqQyH48kPg9hHorqA6YjJnpQHHg7zS2KlVK4tsxMYNVXYoNC28JVXyCUk7YirZzJF5wnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.57M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 01:26:55</div>
<hr>

<div class="tg-post" id="msg-659146">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
قطر با تساوی مقابل سوئیس، اولین امتیاز خود را در ادوار حضور در جام‌های جهانی کسب کرد
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/akhbarefori/659146" target="_blank">📅 01:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659145">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsJ2fNPim-fvTXPrhGc-N_fhpCOvD29bSIFAnSeGN2znBk3rU42t3vTEZ5sriSTxyECw_UL7o7dnf-hV8cgL6Bgj2aph22XMt_4-wbk01IBOqGBCF61hz37eUkV-YH6aH3WWmFyRRk0IVaHd9LoYrsYl6FO8Zeuwtyx8k1vLrDU383QF5kDgobYK0s2HKZMNWL-QB1M-HBNEBSztMThm3VEUdJ9GyPl3UTPylnpj4-EhoAIb20XIP4vcQvPsTj7J0HJYi9efBrBF85o78D6P9iGoOOPk2J7WfGfIsJmi5qYe_cW4v9ejK0-ok5iR4F-_-FifEA6ZR4IBUEL01vrplw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله میرباقری: ‏
🔹
مطمئن باشید مذاکرات جاری، ضعیف پیش نخواهد رفت / رهبری صحنه را کنترل می‌کنند
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/akhbarefori/659145" target="_blank">📅 01:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659144">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
آخرین اخبار از توافق و جنگ ایران و آمریکا؛ احتمال امضای توافق طی ۲۴ ساعت آینده
👇
khabarfoori.com/fa/tiny/news-3222545
🔹
ادعای ترامپ درباره نابودی تاسیسات هسته‌ای در اعماق زمین با بمب‌افکن‌های B-2 پس از توافق با ایران
👇
khabarfoori.com/fa/tiny/news-3222777
🔹
شوکه کننده: کشف جسد کنار کمپ تیم ملی!/عکس
👇
khabarfoori.com/fa/tiny/news-3222565
🔹
فراخوان برادر داماد رئیسی برای لشکرکشی خیابانی علیه توافق ایران و آمریکا
👇
khabarfoori.com/fa/tiny/news-3222722
🔹
زمان و مکان برگزاری مراسم وداع، تشییع و تدفین رهبر شهید انقلاب اسلامی اعلام شد
👇
khabarfoori.com/fa/tiny/news-3222672
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/659144" target="_blank">📅 00:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659142">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/No-8wHHKFSoV5dBXJ1FpYpMprB2_7zUxUcbloeOUj60vbXxyhK3oNgOgny_YCpkj2BbgasHuJwGifxVN2QUzRGM1vs0BLIf1BRBDl5JNtDHXu3iG2__p4qwDwXU0FrcLVXpB1NZOQxWlMd9V9WqowrlhgJrVcwiX7GFGl7V7MpMB-6MwrcymFqKw_rInOk3PPg1VcU7HnMCqsDy4NJs_QwRg34sQPm1jmlUxy_bFPwAMRh8eEtj_C4JzH1hRdNOe-aDAExQkYPD0iF4e6jgCvbBSlm598_YuVWDYU9-E_VUUJ0u0ll2Sh5Rszw96JP4zZt2wd2ehXVr4j5yOZeLnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VSXnc_i5LxjCnzBq5M_yvCnEVJDY30-cCXFop4gvGdXER6bC6UR_Xzf42yC0RV0maQr-Q8D6CrxD1uBVqPTf1nWTto0HypX2_BIPOf_DQCU8ZrKdLyMtl_fTjEoYR-jNRzNrzlGkq3cdC7h_GuN1lwjYHnk_3x2XaxAOmb95jZ-kXevtTOkk0zy2uR7khbhiystm1C0EviFrt0c3aemTqjjcTwqFuiog9V5mNYWoz7HPw3chtTT1oWlzVXUb5ExWx1NlB6Ru0SKDtMXq-Ru76jw044--ePnaheiP5iJuljVSI5OazYQx7qiJQd0lpJo4cNJaGBdur5ZBvB8Z9WR2ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صرفا جهت حال خوب، ماه - جزیره قشم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/659142" target="_blank">📅 00:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659141">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSLVy8IDwLsK8ZhKp8-lHPJrZcjmgXaodRNPwJWYm5wqFMuUMkRUTzc7pVTkzgEJB5G10UGE7JErqfnxi5WQh-dpPZsNe7-Jl-g2Foq8dZCNANJpmhVT-RmjqhzY9kSLG3Ez291b6KNz8ESEdDmu9wjxQlcEz2sphBbSVENx21vKV3OqGt_GKyeDMs0CuxSv-pVaQCwh-46J1M9U69d3BmICGCRQSWQP_dR27q6iSMhiQynucRigAmbRxp4Ls8HvS8yRAknc_Kj7q_uXDyN_O-SCBVSv-4TSwj7GITXSCDNgj9z16hboH1W2_3HxOrk1Uk24ARgx700c9ke7MyAIuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آژیر هشدار در شهرک صهیونیست‌نشین مطله در پی رصد شلیک موشک از سمت لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659141" target="_blank">📅 00:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659140">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
هشدارهای اولیه در متولا، شمال اسرائیل، به دلیل احتمال پرتاب موشک فعال شده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/659140" target="_blank">📅 00:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659139">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cP8hdHkYoflJZ_Mgb_4zeDHKzjsSBRSEwe2OURlrqnB_7FCC2tYzsZ--Maq2PMCElNj7-flFjiZ_mzJtLJRrA1_duzO0JC8skkhuAGtKtBGIDQKLdjmZ3ovdGJhOEjTHh-u-kpVo7zR4_3XOx-tRKw1wD9cVlhnUzfarhcqGqtpWyA9v81grrawuVKhaTF7fp78b2nGlVsucHvChRotWujOo3s0lgWTQZfdh6Hd8wlhks-b_ZsLLrrVyPUn1WdqciynZI1_JmrcGASm7jCFaVKz5EMthKe18hJ3q361YCSb_aAgUehW3NUVHA-Q-sEv-65E4Njc5SvWzuqpq9sWTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/659139" target="_blank">📅 00:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659138">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roizOAh9xoSayTclEA5C6i4a88bBbYEMEPPvjQhU5B6yoD29SR8MzKDfH0Ift83PMcv8ASaQ1fDXm9DRI_kR2YFVsuzxUkGgBxchdTkyk2QHpMTptZvI3rPsJy62xKLQM1Ifn5jHcXAH34_bwyFbAOlTzP7qM1F4PMq5cK-LxNHY-ps_B2zaqtQ9lGoYQwcsykKDdL4rIFnmvtJ4mPBCGfEIc-yUWT6dxRlMMPm4iBlyfq9zc4TNdDIrM2tLv16LGLdUm4Zk-USCrYDbd0F7MY-7dFwzAlVoaYOM3D_qRSAtGTg0gfGJyfNbv1W9GtqX4tUIzwthJr31DMFHQZpqnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید ترامپ متوهم: فقط ترامپ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/659138" target="_blank">📅 23:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659137">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/659137" target="_blank">📅 23:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659136">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
خروج تعدادی از هواپیماهای سوخت‌رسان آمریکایی از فرودگاه بن‌گوریون
🔹
بنا به گفته شاهدان عینی، تنها تعداد اندکی از هواپیماهای سوخت‌رسان آمریکایی در محوطه فرودگاه باقی مانده‌اند هواپیماهایی که پیش‌تر نیمی از فضای محل پارک هواپیماها در فرودگاه را اشغال کرده بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/659136" target="_blank">📅 23:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659135">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
مطالبه ملی از نهاد مرجعیت: صدور فتوای مهدورالدمی برای عاملان و آمران ترور رهبر شهید انقلاب
🔹
امروز مطالبه خیابان‌ها نسبت به ترور رهبر شهید انقلاب در ۱۰ اسفند سال گذشته، فارغ از جایگاه ایشان به عنوان یک رهبر سیاسی به جایگاه ایشان به عنوان یک مرجع دینی اثرگذار در حوزه بین المللی نیز معطوف است و این ترور تعرضی آشکار به مقام مرجعیت در جهان اسلام تلقی می‌شود.
علاوه بر این، تداوم مطالبه‌ی خونخواهی مردم در بیش از ۱۰۰ شب گذشته در خیابان‌های کشور، به وضوح نشان می‌دهد که جامعه، این ترور را مصداق بارز هتک حریمی می‌داند که امنیت ملی و دینی ایران و جهان اسلام را خدشه‌دار ساخته است.
در این میان، نقش مراجع محترم تقلید در هدایت این مطالبه‌گری، نقشی کلیدی و راهبردی دارد.
🔹
امروز خیابان فریاد می‌زند و از نهاد مرجعیت انتظار دارد تا با بررسی دقیق این ترور ددمنشانه، فتوای «مهدورالدم» برای عوامل و آمران این جنایت و در راس آنها ترامپ و نتانیاهو صادر شود.
🔹
صیانت از حریم مرجعیت و اقتدار نظام سیاسی، ایجاب می‌کند که این مطالبه‌ی ملی، در قالب احکام قاطع دینی بازتاب پیدا کند تا راه را بر روی هرگونه تعدی به ارکان دینی و سیاسی کشور برای همیشه بسته بماند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/659135" target="_blank">📅 23:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659134">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcDM7fV0WLO6Ig850Ab4KZhRGjUvwQV8HDV3AqtaU0AxQMbHJuvVtRno8EryKQ8bQnDrD271AxfuROhkiUy6xyLWyL7H1KH2_rg645Tp0u1ctriulOIWoakhJHpKhF-1Fzu8BmlCAFj_UnpbXvDi8ESswl3TgJxMoGp5mWfvc0r33N_OJt37ali0f5jhYdBPwHELNInXpBpnAqF2kcNJHSXUOgot7-yaw1mJqaZZm0A88lALy9UASH_nE1C1wdYPjepahlt28If7f5ru-2CydBW2uDKDB2xYoLgRWv1xBtOXezkoMnVAN_-6smC_QSkxffoTMMHkpGbsowr6HFqFCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
تجربه یک جام جهانی مهیج در نئوبانک فرارفاه
🔹️
اگر در "فرارفاه" (
https://www.refah-bank.ir/fararefah
) دارای حساب هستید و یا با افتتاح حساب در این نئوبانک، ضمن شرکت در طرح "فرالیگ" بانک رفاه کارگران همزمان با برگزاری مسابقات فوتبال جام جهانی ٢٠٢٦، از جوایز ارزنده بهره‌مند شوید.
🔹️
مشتریان با مراجعه به نئوبانک فرا رفاه و انتخاب بخش فرا لیگ با اعلام نتیجه بازی پیش از شروع آن مشمول امتیاز می‌گردند.
🔹️
در پایان هر روز از برگزاری مسابقات به مناسبت شصت‌وششمین سال تاسیس بانک رفاه کارگران، ۶۶ نفر براساس فرایند قرعه‌کشی و با لحاظ مجموع امتیازات کسب شده، مشمول جوایزی تا سقف ۲۰۰ میلیون ریال می‌شوند.
🔹️
پس از اتمام تمامی مسابقات جام جهانی، ۳ نفر دارای بالاترین امتیاز مشمول جوایز به ترتیب ۲۰۰، ۱۰۰ و ۵۰ میلیون تومانی می‌شوند.
🔹️
مجموع کل امتیازات هر فرد و همچنین میزان امتیاز سه نفر اول در جدول امتیازات بخش فرالیگ از نئوبانک فرارفاه قابل مشاهده است.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/659134" target="_blank">📅 23:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659133">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0MqvBhSN_2yMy5Uu_pAZA7ui6wKC7hijqp7FAmU-ADrzPTFhypWBHBGEBOVx33WEBL-S5Ox7xxRSFNuEfS4qqduJOn386D4smv1EnWddgAr4aRcT-w-UYXFjMeC_dQcRZ9GqwLQsENNrV0bjxUJgkXqDWbMFIXjxLNfWRBCuLljFFcpIpvwM7dnfm329hyfQrL6vMkScJHcKUNQ6igpbwMOHVG5vat8B9tZEOR2JfVFeFqq_lzL1PBskGdhNLO6FoRRbBZfkuuVMMWUrQeiNObzfnL-Me3y0bR15eAUC2CutLEH2FjprpcYhlro2hP7WlY2rDtH1QWQvXw95I1zNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تتر ۱۶۹ هزار تومان شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/659133" target="_blank">📅 23:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659132">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEX8gqIs8zj1AR1qSYDBDiHrbcxAOs1ljdqnshnt_wTWvqVOfT2gki5uLr1oPGMfZyHSpCq8HcZd1lxUyDXdETILqQ2cHHdq5cftUlM4u4KOW2FFOdEtvzzrmLPfvuyLrzg7KaDd4IIOfgaHbh7XF1hAsXTuVjcf5bS7KHXYPxDrl8hQ9HmG04hrUgzB8dp3SaKOQSoDrN23U0-eP6q9gfj0wfg84cTB5o8axrCPVnA4Gth3rasDJCvjXDqVnZTtDWCBy6UkBWYBePuEz3qwjd9oG9u6iNTd3XU-_KFqhV1TTCxkhJKhrVJhgdjpRz2uY-nwk_7lbuacMgROQRJHDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حکم آنچه تو فرمایی
🔹
گمانه‌زنی‌های رسانه‌ای و برخی نشانه‌های دیپلماتیک از نزدیک شدن ایران و آمریکا به یک تفاهم مشترک حکایت دارد؛ تفاهمی که گفته می‌شود در صورت نهایی شدن، به‌زودی به صورت رسمی اعلام خواهد شد. طبیعی است که چنین موضوع مهمی موافقان و مخالفان خود را داشته باشد و دیدگاه‌های متفاوتی درباره ابعاد و پیامدهای آن مطرح شود. با این حال، آنچه در نهایت اهمیت دارد، حرکت در چارچوب منافع ملی و سیاست‌های کلان نظام است. هرگونه توافق یا تفاهمی، اگر محقق شود، باید در مسیر و چارچوب مورد تأیید مقام معظم رهبری باشد و همه جریان‌های سیاسی و رسانه‌ای نیز به این چارچوب احترام بگذارند. در چنین شرایطی، وحدت نظر و پرهیز از دوقطبی‌سازی بیش از هر زمان دیگری ضرورت دارد.
🔹
هفتصدوهفتادوسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659132" target="_blank">📅 23:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659131">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/959dce732b.mp4?token=CRKZ3BbInN_wOp3ugX4XB2B-alPJog8ll10HpxVp3Tdr-2lEg3T8QahMYKsqARXHM2NjpltcI1NwYs2I0HhGnMBJ4h1fkab8rJ-RiNhOdmrBlffPZn1ecXk3O8uAPKeod3cnPtMAw6bVRPU0uBdEF-5CCweje_yipojyfC3p51xXA3VLs1Fq__Gv6qJlolCPcCR8Qc2RIMxaYSYnCZya-V614vtJ2STLvQ_1AaWYpGOgZT927rvgdcFxyMlCdYgBVyzU-unMnL5McqvFQGYHDs7Z-8oQUC9CyyGXgJRqB7fKuAxlBc11U5trDD6A5lhWC-CqbN6zf5W4qffKGKYI2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/959dce732b.mp4?token=CRKZ3BbInN_wOp3ugX4XB2B-alPJog8ll10HpxVp3Tdr-2lEg3T8QahMYKsqARXHM2NjpltcI1NwYs2I0HhGnMBJ4h1fkab8rJ-RiNhOdmrBlffPZn1ecXk3O8uAPKeod3cnPtMAw6bVRPU0uBdEF-5CCweje_yipojyfC3p51xXA3VLs1Fq__Gv6qJlolCPcCR8Qc2RIMxaYSYnCZya-V614vtJ2STLvQ_1AaWYpGOgZT927rvgdcFxyMlCdYgBVyzU-unMnL5McqvFQGYHDs7Z-8oQUC9CyyGXgJRqB7fKuAxlBc11U5trDD6A5lhWC-CqbN6zf5W4qffKGKYI2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهتزاز پرچم فلسطین در بزرگ‌ترین میدان نیویورک
‌
🔹
هواداران مراکشی جام جهانی پرچم فلسطین را در میدان تایمز نیویورک به اهتزاز درآوردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/659131" target="_blank">📅 23:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659130">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/859711ac57.mp4?token=UezXZnKoPonc78Zxjd4xaHXZi2X7ylgSWjYTjkLvpFwRczhlVyTFGDRDIPKxluMx0MccB-dn9bQ8gMDgQ8sjj0UYsTiEDDeWevXAE97qMIJLxEfrN020vf6bTPNSNL_8BhFI9rjbnhvbEMrYXA-5EKiPnNF4gc2KZoWOG8uurKc8CMeS3kR7nJrFNxLGfy9r9WQIJFMm0CJ7eN3Bk6QBryoKzWuYuiZI3b7htcf1mhTDs6teC6n3JjMr4rUyisdZJdkziTo7O0VACwvOG8xeQuTS4yawdRx-hBv8g8d_duDnTwTOznFxYSyFV2IvxcClSInmY1FTwuZmQ9eUBXjqKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/859711ac57.mp4?token=UezXZnKoPonc78Zxjd4xaHXZi2X7ylgSWjYTjkLvpFwRczhlVyTFGDRDIPKxluMx0MccB-dn9bQ8gMDgQ8sjj0UYsTiEDDeWevXAE97qMIJLxEfrN020vf6bTPNSNL_8BhFI9rjbnhvbEMrYXA-5EKiPnNF4gc2KZoWOG8uurKc8CMeS3kR7nJrFNxLGfy9r9WQIJFMm0CJ7eN3Bk6QBryoKzWuYuiZI3b7htcf1mhTDs6teC6n3JjMr4rUyisdZJdkziTo7O0VACwvOG8xeQuTS4yawdRx-hBv8g8d_duDnTwTOznFxYSyFV2IvxcClSInmY1FTwuZmQ9eUBXjqKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویداد تخصصی «نقطه تصمیم»
آینده از آن کسانی است که در «نقطه تصمیم» درست می‌اندیشند.
جمعی از مدیران و کارآفرینان برجسته حوزه فناوری و اقتصاد دیجیتال، از تجربه‌های واقعی خود درباره بحران، بقا، رشد و آینده کسب‌وکارها سخن خواهند گفت.
یکشنبه ۲۴ خرداد ۱۴۰۵
ساعت ۱۶:۰۰
مشهد | هتل نوین پلاس
https://evand.com/events/نقطه-تصمیم-015774
#نقطه_تصمیم
#DecisionPoint</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/659130" target="_blank">📅 23:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659129">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCri3s1SJ5qbTd9dXPXqm-BYEU0OMpoR_Zc4XK4HP00MMRu-4yKLWjiYoqApAfN7P0fSGZY2z6OOnmCqcxIeWUQEGof0zZTpi1GKM9KzO5GIYGVar-nIUW0dV0i5g2tYs41baX5UiZk42jb6NmFLVJikYjxyp7axjUAa-avG0KpT7EOGDRe6h1SIT6ic388PvWGQt1jH0FEixdB4qnyBp_hZCf2RIcrJCP_clQciiUvq9x5hreIdbJO1QfMyvGsd9F4E_mBbZuvWBVHxXg0dP5E7FNxy8LuihWOAeZRbD6QuEYTCsjtUNkZcHBs_RCf3zKZsT040kqvS1aul8rrgZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
The cries and sorrow of Minab’s children will never leave you.
آه و افسوس کودکان میناب رهایت نخواهد کرد
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/659129" target="_blank">📅 23:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659128">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5WuJBCNqzYRR14l5EfcIwHRiHU-6J7PiwfTVMGA5rwSXb-niYDNa4gfAfPezDKdywTk2SRrkRftDN0iVEldBHong1sJqUukxgerawXm8hN3EQm_Z31fzOByeeXYsX6Bi9PZn4zh4uDh6fLJR7wjHOvkx7dc568r9_g6uQH84HD5ilhr-5tvG-Azrsp4w93XsitQ9102x_FSForgmDbBYmiAG_Z1z6Vd6KSDBmi8iOlgLRHDI9LnrdT0xqgHUAFW4ni-ayEHm2OUIVMmW0EebTt4-tVuIIVU9AzLyytn9U2GO2uWTl2__jBkTZZJbtqHV3_I1aYzp4Cx9N5wu0V5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار وال استریت ژورنال: ترامپ گفت فردا امضا می‌کنیم. ایران می‌گوید که این توافق نشده است
🔹
اصلاً تعجب نمی‌کنم اگر دوشنبه صبح به وقت تهران/یکشنبه عصر به وقت آمریکا باشد. ۸ ساعت و نیم اختلاف زمانی.
🔹
فقط برای اینکه ایران بتواند بگوید ما در روز تولد ترامپ امضا نکردیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659128" target="_blank">📅 23:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659127">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
رهبر انقلاب: وحدت ملی از مهم‌ترین عوامل پیروزی در برابر شیطان بزرگ است
‌
🔹
از جمله مصادیق تقوا، رعایت نعمت عظیم وحدت ملّی و انسجام بی‌بدیلی است که حول پرچم ایران اسلامی به ملّت بعثت یافته ارزانی شده و در زمره‌ی مهمترین عوامل ظفر در مقابل شیطان بزرگ می‌باشد.
🔹
شکر این موهبت، اهتمام آحاد ملّت خصوصاً نخبگان فکری و سیاسی از جمله نمایندگان مجلس به صیانت از این وحدت و پرهیز از اختلافات پوچ سیاسی و برجسته کردن تفاوت‌های اجتماعی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/659127" target="_blank">📅 23:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659126">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPGRGuz9PiebSL4Q4To-wHdWhAJf2e3wmKyoKbDp35cwUGbQwE91izto3WUIXfDhgTMgh1sclHtRFx9c8doVcVhMwuLZBLvMsVfJC1t-MYtkfiWb6Ka3tegUnQ0ktTBF31sufdcazoTDGIGUJI1TbGEUanpZCY8px28QrnsAaM5r3WU_jvK5rrx2rcehx6CGCIPPkHq-VxlE0k0LsFCmqTxDzGYCiJElFVoDeWfrgBV6os1Qyea-brK2lsxBhogZkvxlm7QGeHhPIDbX99YYoNdgjlz8xCYrcJieIoCKg9GDQ6uYXsK0dInJac7efHqP-JgSXb9_Dq639ggbaHH_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سایه‌ات را به کابوس همیشگی‌ات تبدیل می‌کنیم
We will turn your shadow into your eternal nightmare.
#WillPayThePrice
#تقاص_خواهید_داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/659126" target="_blank">📅 23:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659125">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: مقامات ارشد اسرائیلی می‌گویند ایرانی‌ها بی‌دلیل با این توافق موافقت نکرده‌اند، طرف آمریکایی شرایط اصلی آن‌ها را پذیرفته است
🔹
به گفته آنان، این توافق بلافاصله منجر به رفع محاصره دریایی و نجات ایران خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659125" target="_blank">📅 23:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659124">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
رهگیری جت‌های سوخوی روسیه از سوی جنگنده‌های گریپن سوئد
🔹
وزارت دفاع سوئد اعلام کرد جنگنده‌های جی‌ای‌اس ۳۹ گریپن سوئد روز شنبه، ۲ بار هواپیماهای روسی سوخو۲۴ و سوخو۳۴ را رهگیری کردند.
🔹
وزارت دفاع سوئد اعلام کرد حریم هوایی این کشور نقض نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/659124" target="_blank">📅 23:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659123">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO7_H1prvA2rXUKODv85Ux8MHVGCzFJmyU85ioogU7Xs6UHGEUK375io9DLUDFom-TA_4tSs6SsOhi1SNhsSH3AL_C-eZ9wUWEA1JRsfP0nigemGcvF_xVb1Ps_uH5R3F26l0c2Rj-U0_SFDHraxuzkUbJgiWpvoedzE9PTGEaj7et7ohDfnPUd6pwjMYhXGTuL-waazyM68r7Wr2E5W1PnwKnpi3DpSbutZvqmV87U6f_xTGAFQqgzl1f6VTMTryIhsqKyd6bf-P_Qw3mLFuHn1x_7czvuN71rZqGla1SfYNFiGaSqj0wojD7u5KTopE7QfRLB-3m30gRLtr4F2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موافقت بیمه مرکزی با تمدید یک‌ساله مجوز قبولی اتکایی
#بیمه_البرز
بیمه مرکزی جمهوری اسلامی ایران با تمدید یک‌ساله مجوز قبولی اتکایی از داخل شرکت بیمه البرز موافقت کرد. این تمدید بر اساس ضوابط و آیین‌نامه‌های مصوب نهاد ناظر صنعت بیمه صورت گرفته است.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5046</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/659123" target="_blank">📅 23:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659122">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
اختلال گسترده در سرویس‌های متا؛ اینستاگرام و فیس‌بوک از دسترس هزاران کاربر خارج شد
‌
🔹
هزاران کاربر در نقاط مختلف جهان از اختلال در سرویس‌های شرکت متا از جمله اینستاگرام، فیس‌بوک و مسنجر خبر دادند؛ مشکلی که باعث خروج ناگهانی برخی کاربران از حساب‌هایشان و اختلال در ورود مجدد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659122" target="_blank">📅 23:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659121">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H55yZ201K7S7iYFAo2o5oc9KFCHYLrLWPefrmqmbDnEuMU6hopYVcVClRmJd_vBPmvQJlCI_9NxIMIfY7jxuopN_yfm09i2iGoU2b4GHaZMz0DVXq3hT15sTUmUI2v2FmeJSgz9iETFgKDcT85NOx844sbyRIH_65PpvlgH9Bd8L3oEnw9Ol-o7XUf4vZ8eo1gS7lcmbxXjix-yjLMIcqJ6jpZi2EgW_uHhJv1RoXg3XMe5TUIWLh4rVn_V3mzGOkIQ7cGkIWgm18--rlnF2mUHsVhth6KFp1mT6jraglVElGwOq5P_lS2-f38afCOb8TMlF7AaM1Q1sZupOiucyfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا تولد ترامپه!
زیر این پست یه تبریک ویژه بنویسید!
برای هدیه تولدش، هرچی فحش پاستوریزه، کنایه آبدار و طعنه خلاقانه بلدین، زیر این پست براش بنویسید
پیام‌های شما در رسانه‌های خبرفوری منتشر می‌شود
در ویراستی خبرفوری را دنبال کنید
👇🏻
https://virasty.com/r/BWcv</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/659121" target="_blank">📅 23:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659120">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a715e5146f.mp4?token=H-5caifMr6R4s8JKCcFBjRYg3VCILPeezZ8mAXYcqnVDPXrcDl5dy3it8bfSp18u0FTOl5y8yT2UBC2tka5lc6mBWXC14qoloO7xoEITFAOhZpLrIiPc4tfO0Iq3plhOtwq982YzpIObI9VsnIeVTvqN5uoxHCLqgcuhQfx1BFWGpkNMDC6Ny0MlNXH_cVxgoAcdGqZIcl4ywUIrLm7wgEc2Gf6F2B9ylXHaO9LHXPfMfhuPoaeyGkLL2D3qlQ7vL58-eOiXBCaOM14DheWxP4l5MD5roVaJtgOYHBI1NPkphCmt0siaf_jVGj6d2brufcinNqO_qAsX2vafxstElA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a715e5146f.mp4?token=H-5caifMr6R4s8JKCcFBjRYg3VCILPeezZ8mAXYcqnVDPXrcDl5dy3it8bfSp18u0FTOl5y8yT2UBC2tka5lc6mBWXC14qoloO7xoEITFAOhZpLrIiPc4tfO0Iq3plhOtwq982YzpIObI9VsnIeVTvqN5uoxHCLqgcuhQfx1BFWGpkNMDC6Ny0MlNXH_cVxgoAcdGqZIcl4ywUIrLm7wgEc2Gf6F2B9ylXHaO9LHXPfMfhuPoaeyGkLL2D3qlQ7vL58-eOiXBCaOM14DheWxP4l5MD5roVaJtgOYHBI1NPkphCmt0siaf_jVGj6d2brufcinNqO_qAsX2vafxstElA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم هند تصاویر ترامپ را پاره کردند
🔹
در پی کشته شدن سه ملوان هندی در حمله نیروهای تروریستی سنتکام، مردم خشمگین هند با پاره کردن پوسترهای تبلیغاتی دونالد ترامپ از روی موتورهای سه‌چرخ خود، اعتراض خود را به سیاست‌های آمریکا نشان دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/659120" target="_blank">📅 22:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659119">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جزئیات تعرفه‌گذاری جدید قبوض برق
عبدالامیر یاقوتی، مدیرکل دفتر مدیریت انرژی و امور مشتریان شرکت توانیر در
#گفتگو
با خبرفوری:
🔹
تعرفه جدید برق از ۱ اردیبهشت اعمال شده است.
🔹
قبوض بر اساس الگوی مصرف محاسبه می‌شوند؛ هرچه مصرف از الگو بیشتر باشد، هزینه برق به‌صورت پلکانی افزایش می‌یابد.
🔹
برای کنتورهای هوشمند، مصرف در ساعات مختلف به‌صورت جداگانه نمایش داده می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/659119" target="_blank">📅 22:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659118">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
عصبانیت مارک دوبوویتز رئیس موسسه ضدایرانی FDD و حامی دوآتشه اسرائیل
🔹
ترامپ می‌گوید هیچ پول نقدی به ایران داده نخواهد شد اما معافیت‌های نفتی و آزادسازی دارایی‌های مسدودشده به ارزش میلیاردها دلار برای تهران را نادیده می‌گیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/659118" target="_blank">📅 22:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659116">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای اکسیوس: مقامات آمریکایی و منابعی در کشورهای میانجیگر تأیید کرده‌اند که امضای توافق به صورت مجازی انجام خواهد شد و گفته‌اند که این اتفاق عمدتاً به دلایل لجستیکی است
🔹
به گفته این منابع، یکی از دلایل اصلی این است که جی.دی. ونس، که رهبری تیم مذاکره‌کننده آمریکا را بر عهده دارد، نمی‌توانسته پیش از آنکه ترامپ صبح دوشنبه برای شرکت در نشست گروه ۷ به فرانسه سفر کند، به ایالات متحده بازگردد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/659116" target="_blank">📅 22:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659115">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
شبکه صهیونیستی کان به نقل از منابع آگاه: ارتش برای توقف عملیات زمینی در لبنان به عنوان بخشی از توافقی که در حال شکل‌گیری میان واشنگتن و تهران است آماده می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/659115" target="_blank">📅 22:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659113">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nkm8yxlSqKuMeILKzM8Bd3_O3wYIDwGDR6FfPMTElXJH71GENiEKXVBbABhhOxI_LocjqisUa4k7-QEKPQtzUoPQw72P9gTgasY2OWvNhOTxsvpN6ilYNQXCOCT6xbRBLPBD2H0g1WDv2E5GlEgtCK57dSlmzP5MDrDx5FYElw9yoBls4WDautp3F6HBdKvh6cxq27OAMe4yInWT8WxdUAsgkPr90vIdtX8uireNNrlKiOqxtREf52WrNJ14CvPKrY4_NgOmrNh3yqeC4NsLKXeXm0WlF_lU3Sgc0xxeQqhxP8PHSbI00UOP_doEpp1cieE9QqL1pgh7y5fbXds9ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت غریب‌آبادی از پیروزی‌های ایران در طول یک سال گذشته در برابر متجاوزان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/659113" target="_blank">📅 22:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659112">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rk_4DWjyXDtWsFm26Qj3ez0EHNkFZhVbGTMtjJogpCYlNW2EM6p55pyqj07G3wZqUuDG2Tzt8wgD8shNkq3uPDgLgtKF9UcQp6rfCHXxRJBNMcDIdTs_x0AesIGjIJshqIxA-wZG7OzLb4S7ULvNiKLsefFp948CQbrG3840zxRrLk2NnaXtzp8_3IT0z-uglQycXAkCkDWITecGmr5-M44EnlC7_dykbvd0W6BE4qpQ9wZjWB8ShicE9LzWCJ38kTguYYfnvL4hF6E8MoFFaZJU_5qn72o3NLSdKXoVSBpNzkXUrjvfK7VUHzomQN43S1CB-vEpFiZj7P86h8Brxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/659112" target="_blank">📅 22:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659110">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCnoLOpjuBYJonxn8Vjq_5kg9Lqj2HRXyBwgtPauDiwJv30Qp2ouxxTfkRay__cJH58wjFAjf5E9FPhFPXpwvegFSMUIiPxTjBkL702ZRiDmbegPulYUT3nxMS4a7A1aHoFfbxyZ8ufnbO-_pNKwtTbg-CDpUBtjW7UcjsUQSYZWa0fvrZVx55g-Bkp4f_fikjyBtw6mNQ9kBNqEvEIozgBlRGFqK_9GrFUnjXXPoG-0vgo-pgp0ruyQbaOkE6rYq6iOLVGkdZUDrFXBUfysYeiFL2X-AaBhUicOYLtMyMEFb8nSxAtQnCNGwFHGu3Mig8x07qIy-wbfDL-ilCz5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4p-5rDbEQjQonojdbkF6rBZTrvnB_7jToB5MxbTZlHoOXVK7H9HRSGAeM4XiTn7Q8kkL0I1DurZk2Nze9vPcz5p4ypRgkJ-0hj1-VcwYRqshOPlt_oij7qP3YvNBaPBLtqbXOctAlQoV_URFFfaIsqyKAY5PbyE1tlP7MLrPfsfFX25g6Sp0xaADMX7-m9UnwsgEoMxM2imDdjH1EeNAFndHaLqUBj9m7HigUJH1kaztPj8R-CjxWOnu8NomBNmN837mZ_5AXAxnWeJM5AQ28UueUnTMDDpf2rtbC_flNWs41HhWbfvUmZmIdXY41aXU83W8pGN0qz17mPML64qgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترکیب منتخب و بازیکنان برتر گروه G جام جهانی از دید Score ۹۰
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/659110" target="_blank">📅 22:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659103">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOSGM3Dp_QZ3zTzUCao1PKDDQdcy6on6FpAd1ywRercnk1CAdOKSxvraDnzLldnRq8kvkIDm1UJQgUCyyzMAZNngELv9iAahkdiu_iHHiGFBvbA2BxqeDyvINwSos2gLxfullbj1Mkz0-27r8mo2Ko3UzPDJG39zg6QJYBkYhlF6iVnW0tKcqWNNkYGxRf3vtLmxY3V4vst8begSSCJWCz8xJBVfdQElmXSOOCWDk49kDv_9T79GSnewccAJ7rB-ph5gXE5RQlU_4xawaYhgk1fpi1pg6BZZto_PgLjc_CGmp9ATtVPjpeBUgIhOBCLQ7D0sfk5gMXS9om7-HK4UIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EO5K7pgJcVRWX7ES9dTRcFGAxUalP0WBnNcMnvkmiQsipoUvB18fD8A_1uMwISl0vCUp7jVKWB_BIwEgsf5aPWYe6A239-KgfCVHtP6-ia9LBSoCa5BLZWdXviNdwvTjVZgxWAzTTuQu1unoNWBX9z3gBktP6d90KX94nkKLMOt4b-v5FtdSHQmtRHEY3ftv4sYm94z4WQYIeGLS4hegTKEd1E-louLAY9i0LAR-jgPV3955ItZa73hwDKHBmA_qfxRdy3qfzjm5RDKGuFMhjP0WgwnQOlYymrwhHpwlstxF7zruA3ijXAZDOdo1lqJNIv5pR46tt6LgJm5N2n7BMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0UxhT7wvXdC8JzVaIYInKb0rzWIBrGJE60An5CUbwi9TQSsDMULJ377MXSVl4e1qnvyx0a2Z00UbmmbO19tRRuW6X4PgNTCclJXaIvHsiDG5mvTHB9crZ2ea9GnEk28LupL3uNqKi5PoN3Gm_SbHRiiSnuR5ZxQKBhVTCjOY4vfG8Y7vGU1BVAbJ6WO0xVZAWIop1Eiqa-PM_5rcNljOWzcZY2JHidmFSzkYootlxQtaLVNuhRIU0ilPWlfJQqunyeNxAoFbp_KfeSVH5Ve07OPhpjRM_UhemHgxurllH5Kc2DoNrO068KP8Y-KDGvoYLvia5dYKHDoI7uygOsEtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GADuqW03xG8878b40X_c3gNWPKVRwIN5l7eWI9wawAEgzxD5_9QEl_wRY63daTeHWv6Db4eBcH123TRqp-g2_bs1JXvNEBpw-2Fqlwsf_WfZ0zvxDEOyjXfy369lF4ojLMZ4EUhXjgd0dsiUjnzZ333zkuoYGDYP8g5b07PJRM0UbslL-ZYofiPwWoQ0zFyJaIxn8sT__DUG3KgLSQdN3lzeEAcLA1KlUWOzHhASov_gTj-DnTpFSWdhIYpSwVmynl3iN7oVnNPNmSs23wFTCK_kgOU5n9Mf7gmqi2ph9IYdPDgLmpRinYGXPmleYUjiOuXKgmE0cFOY171FmO1lnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAnhcYmFighIqCOGMDkaqg1Tze4mnmkHhiVIRnAonU5j-XXuYud5gxchriBF-fHXA0MVBdeWopluP7lcnQwYKW0r7rw48n1VDtj5yA6LtIJfvaTJm71Ed35CQisQWe3x_XHkKExCGVprmNVCQtCfSVUbogiX1ExelAfpwOtnObUd10nidb612xrPu5kn-AH1sp5EVSHb0fy7HuPXzsHiXrALHoTn3MAqFAxdvzIEmHWkIz5zHGpoz0_tokEnhZaEmmZ10mkBmSx1pU9DpUdt03_2a4Pe7LunSnOR0eHWGf_PiFPTzR-QZHLJVI71KJVP5ThpuZqrrof7zW5vw6tkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T01WEIclVOwKYmdIrUds2AxpU6m8R3ru_-4b1MMtpc4Odh1ZJGfIVONY29jeeQlDmfI4w2A9Cwsv0Xsx9pcYtLZsZP0C5u8p9DLFXV3tFUKtP4P-DbH7vaP_ddyHQGv9LYfCDLLkr8d4CbSfNLELyz5lXcftarbr61lsbQArt13LVXHTiaBDLdY2T8en-YUn1LL-QhVPR5Ae2It1fA0SzH5qQvAWu9NhhOLoJUP0Rvhnqdnz6YK6CpDybR_q_i8kWe0-ZScETcT3bCzE8DSFjkFA6IdH-I3-b2B1-51QB3o-JlqAEiH2W8fZf63Z_pmiRYmsggYst_64W5wu0AgdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dGMh-phJeNsak-RZMXs8dlQZm8A8eCPeswlkSkjQCo1AfWjAkz3DOE9Tp_zQRolESUryzaRvwI_KDXKYscda_AXf0iFUOjAcHJhFlLQLPS1Z2tN6igtn_giko6U5SAfP-agXhOrwtzDejs-vN3LMRaLmp0Vqz-MjS5zAW3PmkFsNPj0oLtJtwtOauj30wAxFSJv0Izzrs2OYOsK4SvXV9J7fpNqmJzi2NamIcYxMte-ljo-1ZY0qXsUY6FGabTb3mZZoAWprWecsTBtftzGFyxafDcDhsIOHcdcnXdZmLkCi7iM4-gKpSGn4mGzVa9wmuQEjcbYUUZXCL_aZsxVZjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند آزمایش ضروری برای افراد بالای ۳۰ سال
🔹
این آزمایش‌ها را لطفا جدی بگیرید!
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/659103" target="_blank">📅 21:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659102">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
برگزاری جلسه اضطراری کابینه امنیتی اسرائیل در سایه مذاکرات تهران واشنگتن
🔹
روزنامه «معاریو» گزارش داد که کابینه امنیتی و سیاسی رژیم صهیونیستی به دلیل تحولات اخیر و روند مذاکرات میان ایران و آمریکا، فردا یکشنبه جلسه ویژه‌ای تشکیل می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/659102" target="_blank">📅 21:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659101">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Taghiram Bede</div>
  <div class="tg-doc-extra">Majid Razavi</div>
</div>
<a href="https://t.me/akhbarefori/659101" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎼
تغییرم بده
🎙
مجید رضوی
#آهنگ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/659101" target="_blank">📅 21:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659100">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
معادل جدید «هدفون» تصویب شد
معاون گروه واژه‌گزینی فرهنگستان زبان و ادب فارسی:
🔹
پیش‌تر در گروه عمومی واژه «گوشینه» را بررسی کرده بودیم یعنی آنچه مربوط به گوش است
🔹
با ترکیب «گوش» با «ـینه»  که پسوند نسبت است (آنچه مربوط به گوش است)، «گوشینه» را  مصوب کرده و انواع آن را بررسی کردیم. البته این واژه، از واژه‌های پیشنهادی مردم نیز بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/659100" target="_blank">📅 21:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659099">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
کانال ۱۲ رژیم صهیونیستی به نقل از مقام‌های اسرائیلی: توافق احتمالی با ایران، منافع و مصالح امنیتی ما را در معرض خطر قرار می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/659099" target="_blank">📅 21:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659098">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
دبیر شورای هماهنگی بانک‌ها: در پی اختلال خدمات در چهار بانک کشور مقرر شد هر پذیرنده و صاحب دستگاه کارتخوان که در این بانکها حساب دارد و حساب پشتیبان معرفی کرده باشد امشب وجوه مربوطه به حساب پشتیبان آنها واریز شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/659098" target="_blank">📅 21:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659097">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
بانک جهانی: جنگ ایران به اقتصاد دو سوم کشورهای جهان ضربه زد
🔹
بانک جهانی در تازه‌ترین گزارش خود، پیش‌بینی رشد اقتصاد جهانی در سال ۲۰۲۶ را از ۲.۶ درصد به ۲.۵ درصد کاهش داد و تورم جهانی را ۴ درصد برآورد کرد.
🔹
این نهاد بین‌المللی هشدار داده است که به‌دلیل تداوم جنگ و بسته ماندن بیش از انتظار تنگه هرمز، رشد اقتصادی حدود دوسوم کشورهای جهان با افت مواجه خواهد شد.
🔹
در میان کشورهای آسیب‌دیده، منطقه خاورمیانه بیشترین ضربه را متحمل می‌شود.
🔹
به‌طوری که عراق با بیش از ۱۵ واحد درصد کاهش رشد اقتصادی، امسال رشد منفی ۸.۹ درصدی را تجربه خواهد کرد. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/659097" target="_blank">📅 21:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659096">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5566cdd092.mp4?token=F8UMJmIE0D9Q6aRLkl8V6xkKN_-Qg2gdpd5pzG25THnnLHc5Mc6ho3HPfmlpYTIRa6Uv5SW3qFFHM-eETznQcc6ogG-kUe21REjkK69_uRXOodHdNPtf75kpVO2yIZTZBQkB8bCtXSA0UgZt4ebZs-VxcAb_OafjglPEYYTUMcfW-sb5CDKuZLN7rJtPNylM9MmOrCtfaT1Q67VKB07ZusumBg-A-6vHjMXGfOMTAmwLT6y0T-Qf_FVEUX0pdzjZxD-3Bydaml6cqGtIFx7185InfMRaaqJGoR04uO0Jn0E_66m90Y5KFZEbXR21FKx75LNuVm7Thi1_9oJCPjSFl37k_txJjV3slaLEPqPJqEBjAI_flqHua82pn_z8eVffcDCQ_RelegYmPg3fwbC_ZIDwAnm4puKCFgHphr0lLkWoQUqhBHKdvSJQtLaR88QvReHehH826oenxw50-rlujODqSPGGIMhQGbx__OcwD9Xtls7eppnV78g0hQ3INDHgdLJPOQHhWb_asJTgLm7iSs9mVY400FgGfc6Rsrq6V3Mp3d9yG2Bn39ByTk4RW-0rnFmWQ3a-dxxbVhWWh-BCu86ouFLTN48YAm-sxUT_DV03x3Qf_f0jZnXvOHvGi3o879GTsSvcKtuizWwtQt73RHSzBF5CYV3khk7XwyR6ZvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5566cdd092.mp4?token=F8UMJmIE0D9Q6aRLkl8V6xkKN_-Qg2gdpd5pzG25THnnLHc5Mc6ho3HPfmlpYTIRa6Uv5SW3qFFHM-eETznQcc6ogG-kUe21REjkK69_uRXOodHdNPtf75kpVO2yIZTZBQkB8bCtXSA0UgZt4ebZs-VxcAb_OafjglPEYYTUMcfW-sb5CDKuZLN7rJtPNylM9MmOrCtfaT1Q67VKB07ZusumBg-A-6vHjMXGfOMTAmwLT6y0T-Qf_FVEUX0pdzjZxD-3Bydaml6cqGtIFx7185InfMRaaqJGoR04uO0Jn0E_66m90Y5KFZEbXR21FKx75LNuVm7Thi1_9oJCPjSFl37k_txJjV3slaLEPqPJqEBjAI_flqHua82pn_z8eVffcDCQ_RelegYmPg3fwbC_ZIDwAnm4puKCFgHphr0lLkWoQUqhBHKdvSJQtLaR88QvReHehH826oenxw50-rlujODqSPGGIMhQGbx__OcwD9Xtls7eppnV78g0hQ3INDHgdLJPOQHhWb_asJTgLm7iSs9mVY400FgGfc6Rsrq6V3Mp3d9yG2Bn39ByTk4RW-0rnFmWQ3a-dxxbVhWWh-BCu86ouFLTN48YAm-sxUT_DV03x3Qf_f0jZnXvOHvGi3o879GTsSvcKtuizWwtQt73RHSzBF5CYV3khk7XwyR6ZvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویداد تخصصی «نقطه تصمیم»
آینده از آن کسانی است که در «نقطه تصمیم» درست می‌اندیشند.
جمعی از مدیران و کارآفرینان برجسته حوزه فناوری و اقتصاد دیجیتال، از تجربه‌های واقعی خود درباره بحران، بقا، رشد و آینده کسب‌وکارها سخن خواهند گفت.
یکشنبه ۲۴ خرداد ۱۴۰۵
ساعت ۱۶:۰۰
مشهد | هتل نوین پلاس
https://evand.com/events/نقطه-تصمیم-015774
#نقطه_تصمیم
#DecisionPoint</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/659096" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659095">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5Flr2OnDG1hDalB6pzCYYe2fheUSnpPZHjVNSyiDDqakqjcN3VaR-Rry3oXB6XihRjcgSGT7SYJ14GByPhCnyyb-Gq6O8oiS3hAUepsf0eDaBERtz7GaXKdG8KJemDz5w3XsCP4heEbTMgivEd1ieLFsFkRp7o2gCE5JxKsxvkzA-VCdI5CYFsGO-TdinL9iWhHCNQj0DEDUYwrsx12YgpPmBRl0WxcNCeHy0SQ3vLtFQ2dZxBjOc1BdNBOhNmp6OmgR7pTr3l7U93lLkEkk4HeByjS_h8fQXWoaohmuWD8LdzjBVktmuMbqoWpxWw3hIJNrLriB4LvjLGyo0Bxug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاریخ از خون بی‌گناهان عبور نمی‌کند؛ روز حساب فرا خواهد رسید
🔹
خون بی‌گناهان فراموش نمی‌شود؛ تاریخ، شاهدی است که هیچ‌گاه نمی‌میرد
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659095" target="_blank">📅 21:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659094">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
شبکه فرانسوی: مقامات ارشد ایران و آمریکا پنج‌شنبه دیدار می‌کنند
🔹
شبکه تلویزیونی فرانسوی BFMTV به نقل از یک منبع نزدیک به مذاکرات ادعا کرد که انتظار می‌رود مقامات ارشد آمریکایی و ایرانی در ادامه مذاکرات جاری، اواخر این هفته در سوئیس دیداری سطح بالا داشته باشند.
🔹
این دیدار می‌تواند پنجشنبه یا جمعه، پس از پایان اجلاس گروه هفت که چهارشنبه به پایان می‌رسد، برگزار شود.
این شبکه تلویزیونی اعلام کرد که مذاکرات احتمالاً در سوئیس، احتمالاً در منطقه آلمانی زبان این کشور و نه در ژنو، برگزار خواهد شد.
🔹
این شبکه افزود که مقدمات دیدار مستقیم بین یک مقام آمریکایی و یک مقام ایرانی در حال انجام است. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/659094" target="_blank">📅 21:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659092">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b1e841ca.mp4?token=C5KhYKU9kpp7yQP27DpfYc31TdY38DU3H4gBLIvCCjHsN6Nx4Ro38jkt31UVdDrYy4N5elopaizvOdlhyJmqiI95UmE7PUGW-hanaa5L3YAfZfG8_LOUexgzEzrulkncmEvjNDFn9PeIfGxA81FBQ2CUYBiIQp2kTpndUoEDNfkqAhoXoWAgAW9JKt2cuDzQuPYe9ELCM1VxyxUJvOFLR6N8v3DCu7gf2l4x6SMrZOnrMx5lyy3CsCWQVWdpVPgqfw8GryZIzZKsecFIvf6vQ-XGIpl31eaA9RQtVEyHaHlqBQM8-mTfj7srn_G9w4X3MS-C_KrkmbjqXyH_AbQBfVLGjMSQHePUg6suvX3QNAiFzeXN6JQx-t02ktD-jQbu_I6FFfkfzA2S44c7_YHFoE9vdJIpdvVfvcvdqHgXeAuiWhvsOHQJ-ockjfNfEbYijWCu_5xJbgdKhmviDEefoUEQR7_BTPJFz-_INdadOcDladtKXoceqSEPEL3BP8xaADmT2IDWUnNnHYi5k5qsoIiSkn8Gcx8qFh99bZj4IWe6cjC1NRNHqMydfvjqda0JkqWPlEinePFwbs43YH4iPYoVPjBTgtB1LhMvxfwbquZ9_3tTgHv9zzSIe5xBcNwSfSdiBiUm3MKhFL0jefbufiL0fy8UzzvVe2mdlsWgOcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b1e841ca.mp4?token=C5KhYKU9kpp7yQP27DpfYc31TdY38DU3H4gBLIvCCjHsN6Nx4Ro38jkt31UVdDrYy4N5elopaizvOdlhyJmqiI95UmE7PUGW-hanaa5L3YAfZfG8_LOUexgzEzrulkncmEvjNDFn9PeIfGxA81FBQ2CUYBiIQp2kTpndUoEDNfkqAhoXoWAgAW9JKt2cuDzQuPYe9ELCM1VxyxUJvOFLR6N8v3DCu7gf2l4x6SMrZOnrMx5lyy3CsCWQVWdpVPgqfw8GryZIzZKsecFIvf6vQ-XGIpl31eaA9RQtVEyHaHlqBQM8-mTfj7srn_G9w4X3MS-C_KrkmbjqXyH_AbQBfVLGjMSQHePUg6suvX3QNAiFzeXN6JQx-t02ktD-jQbu_I6FFfkfzA2S44c7_YHFoE9vdJIpdvVfvcvdqHgXeAuiWhvsOHQJ-ockjfNfEbYijWCu_5xJbgdKhmviDEefoUEQR7_BTPJFz-_INdadOcDladtKXoceqSEPEL3BP8xaADmT2IDWUnNnHYi5k5qsoIiSkn8Gcx8qFh99bZj4IWe6cjC1NRNHqMydfvjqda0JkqWPlEinePFwbs43YH4iPYoVPjBTgtB1LhMvxfwbquZ9_3tTgHv9zzSIe5xBcNwSfSdiBiUm3MKhFL0jefbufiL0fy8UzzvVe2mdlsWgOcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور چشمگیر مردم پاکستان در بزرگداشت رهبر شهید در برج تاریخی پاکستان در شهر لاهور
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659092" target="_blank">📅 21:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659091">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgmLhcuI7mRx1S9I93hQceZvn_clJcxre42xgNxCr0d2dsa37A9Q83KAv4uW9X1fc5MScoQ4ykVN4uqAfzB30dkzAdclBltDwSfkMpCXBXVusbIQR6fckMXb_GwRo49AZiqs88tNeGXk7useGpxcaruVGI107Ffo7SCnJ8eNDAftr9HC-k7Duzhja82G8F54GJ5wnkNkwO27buclFroRaF8y1ipRVHt1hlXZ2qOUXp2KmwLnV-Yi5S64u0KcRJSZM-Rtgvg2A3V0x2vwt2Rwrs5MthKafYrKIxyBOn3Wu-pYHAwTPprqb3XE9h3PVz0TrQ6unUQJT-DdgFKygSYSjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صفحه جعلی منتسب به سرلشکر علی عبداللهی در ایکس
‌
🔹
در روزهای اخیر حسابی جعلی در شبکه اجتماعی ایکس با نام سرلشکر علی عبداللهی فعالیت می‌کند که هیچ‌گونه ارتباطی با ایشان ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/659091" target="_blank">📅 21:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659090">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
جوادی‌حصار، فعال اصلاح‌طلب: مذاکرات نتیجه‌ای بهتر از برجام خواهد داشت
🔹
اگر نظام به این جمع‌بندی برسد که باید صلح شود و خاتمه‌ جنگ اعلام گردد، حتماً به مصلحت کشور است.
🔹
منتقدان مذاکرات باید با استدلال و منطق انتقادهایشان را مطرح کنند و من هم در جواب می‌گویم مذاکرات نتیجه‌ای خیلی بهتر از برجام خواهد داشت./ خبرفردا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/659090" target="_blank">📅 21:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659089">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
حضور چشمگیر مردم پاکستان در بزرگداشت رهبر شهید در برج تاریخی پاکستان در شهر لاهور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/659089" target="_blank">📅 21:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659088">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fbd800e3b.mp4?token=lUStqgBlquqgcYaKIGgAz6FPeno54KoWAKWBn1SkAtpBsf59hQCsSE550QVCa402EefK45JPj3jhpygy0a2jxeLd2nCMk_PIv1odJMskce1VMNaA4zKtW9_1IcdIHZY8i96raArb6VgA95QZ-SDXsgIwCGWzuWAkJKZ0DeugOYohjFHLt8dY81lzp0dKRVzPf0j35xJyvW6YUZNWmo1Sh6Cd34koI2zjASSSYm4GAIsJ0Knuw2P08Y9ak4LE4kn0gZ5T96J2POd-PW5zWrV2lpzTp6EWnIg5hzNccSmkHNgH9dXFnK5YEaKLFu1bO2HVy6UJTliEk19HRr6v9A0pEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fbd800e3b.mp4?token=lUStqgBlquqgcYaKIGgAz6FPeno54KoWAKWBn1SkAtpBsf59hQCsSE550QVCa402EefK45JPj3jhpygy0a2jxeLd2nCMk_PIv1odJMskce1VMNaA4zKtW9_1IcdIHZY8i96raArb6VgA95QZ-SDXsgIwCGWzuWAkJKZ0DeugOYohjFHLt8dY81lzp0dKRVzPf0j35xJyvW6YUZNWmo1Sh6Cd34koI2zjASSSYm4GAIsJ0Knuw2P08Y9ak4LE4kn0gZ5T96J2POd-PW5zWrV2lpzTp6EWnIg5hzNccSmkHNgH9dXFnK5YEaKLFu1bO2HVy6UJTliEk19HRr6v9A0pEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده سازی حرم سیدالشهدا (ع) برای عبور دسته عزاداری طویریج در روز عاشورا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/659088" target="_blank">📅 21:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659087">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17bcb3a45.mp4?token=kWorggxRh3Km8DLFNrrM0Udaxeuy13Rw3KmSPUYlyKER5LPfICoNr_MbnV1eb_XQqXTnlxYm8Ada3fvCT9O4AJdCFo8B6MBFi76qBoa5apjkuop94B5HvaV34I0keqyZA_xl2NfgCK_glpsfRFJtWlu51H_kgg0R0wvZHEfPn6i1G6_htdzdqkZIKvYXe8n_d3YF4gVf4_8g8v_-J5pwpbhOyuN-OJ55oBZRMPGbcdeGXRdAKLEdW_5YWsQc4IhocUlipwE3Cnv7-Z1q79dLEeqaL9B1hvbOmNC3H0lxI6w5mGHnQO8lKN2OxfTVSNCFmJFzxaQFR0Q6hIFB1Sf8Z5kAbYHw58p8MONBnA4w-9S4qPkN0gVi4Rx21i9RgPCHyZYcf14XHBauAK0pUiAtSFPJRWdXdCCwMC5hqNxizYKvS8pSBCZNMJTluZTNkZt6Lchh-5ZkHdouz8pezhzq3IfWgwvUjhnfLabQ3gbmnx0BaSMulo-jHT8MzIwHh6JWb0FllHWDEZzLK7fA3k-3kvWwkZftG6y36n6xmMVRE5EJrOsb9VJrqGDaez09LZ-4s_3yK6-IIKIVj-GXkWLhoKikUa5D2aWSGh0_HJ8yNyztU-hUB5WuQEdQxT9zj4El2JXFWjur2_kMsWKd38FsoiVIiC37l-XCZqhmXyNf0Uk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17bcb3a45.mp4?token=kWorggxRh3Km8DLFNrrM0Udaxeuy13Rw3KmSPUYlyKER5LPfICoNr_MbnV1eb_XQqXTnlxYm8Ada3fvCT9O4AJdCFo8B6MBFi76qBoa5apjkuop94B5HvaV34I0keqyZA_xl2NfgCK_glpsfRFJtWlu51H_kgg0R0wvZHEfPn6i1G6_htdzdqkZIKvYXe8n_d3YF4gVf4_8g8v_-J5pwpbhOyuN-OJ55oBZRMPGbcdeGXRdAKLEdW_5YWsQc4IhocUlipwE3Cnv7-Z1q79dLEeqaL9B1hvbOmNC3H0lxI6w5mGHnQO8lKN2OxfTVSNCFmJFzxaQFR0Q6hIFB1Sf8Z5kAbYHw58p8MONBnA4w-9S4qPkN0gVi4Rx21i9RgPCHyZYcf14XHBauAK0pUiAtSFPJRWdXdCCwMC5hqNxizYKvS8pSBCZNMJTluZTNkZt6Lchh-5ZkHdouz8pezhzq3IfWgwvUjhnfLabQ3gbmnx0BaSMulo-jHT8MzIwHh6JWb0FllHWDEZzLK7fA3k-3kvWwkZftG6y36n6xmMVRE5EJrOsb9VJrqGDaez09LZ-4s_3yK6-IIKIVj-GXkWLhoKikUa5D2aWSGh0_HJ8yNyztU-hUB5WuQEdQxT9zj4El2JXFWjur2_kMsWKd38FsoiVIiC37l-XCZqhmXyNf0Uk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوکس‌ترین کافه رستوران ملل مشهد
کافه رستوران ملل جمان لانژ
راه ارتباطی جهت رزرو
👇
📞
09007102044
کانال بله
🆔
@juman_lounge
اینستاگرام
🔵
instagram.com/juman_lounge
📍
مشهد،خیابان آیت الله شیرازی ۲، مجتمع قدس؛ فاز ۲</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/659087" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659086">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7vHeyVf7hHTwHw5fQcTFp7X3gFGWqpcmHPfg8JeTneeCNWeHolyJHvWzqeDUNsJRL0EpEGAxEKgDK8X40lFFXBiPyybAMAx6GOBJPZRnVKn_ihIJY7OHbXPTGC6k0Y116chk9FUVXsE2AZEQ8qBAkhoYON-OxAxaEzqtU2fCs-E2ViD_TkwWco5XlFyM8IfXeQ9FkeTny0kcbPRdVT76JXITjQpQuVMLRheldqFSZPqTyFIUFzFa7yEnFQY5I9XnaCiNvrKvNdwgIKQBhX50I8u8CkKphtzU3GiICI7aUUXiWLpPF5fJZnQOUQXeD6jZzQ8pV7G2vg7zoMCp8zkkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۲ روز جنگ؛ مقدمه‌ای برای حمله دوم / چه‌کسی ترامپ را در تله نبرد با ایران انداخت؟ / توافق با تهران چطور پیش و پس از جنگ اول ممکن نشد؟
🔹
بعد از جنگ ۱۲ روزه مشخص شد ایران قادر به جنگ در سطح هوایی و کلاسیک با آمریکا و اسرائیل نیست اما در سطح نامتقارن به شدت موفق است. به همین دلیل، روی فاز چریکی، دریایی و موشکی تمرکز بیشتری شد و نتیجه این تغییر شیفت، موفقیت در جنگ ۴۰ روزه بود.
گزارش خبرفوری را بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3222750</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/659086" target="_blank">📅 20:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659085">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKUrfFYXd9_XQVVWhNTl_ZEjrN41tnemhi8d0q4SlGM271wq94uZTBWlDZhPP9cwtbgFkyhwhuq7Pd6EyKA9RsSH2QEEI-r7nStTgYbETzcdmMeBwhpWDDXVYs5_c6kNxRA8DPclIVhEVlQXXCNaiB3iRAaTp6m5UawoLuD_J8ZBpREVTzkujDqMZWgJvbkO7v_VpdmMbH7Wob-xE_baEPEZyGRVtlFFftecz336ieGqkYt2k4ilISHXVhvMmL0XDSaM_3jwnOH3mKiH0_oOKQmlGA-dGokJQyENUqBRb_nWlCkBVLkJLQAZW3yK_qjXEQ8GoGV3wbWUTu-pB6GJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریزش دلار بعد از  انتشار اخبار مثبت مذاکرات
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/659085" target="_blank">📅 20:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659084">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صدور شناسنامه به تبعیت از مادر منع قانونی ندارد
محمدحسین محمدی، عضو کمیسیون قضایی مجلس در
#گفتگو
با خبرفوری:
🔹
از نظر قانونی مانعی برای صدور شناسنامه به تبعیت از مادر وجود ندارد و مجلس این موضوع را تصویب کرده و پرونده آن از نظر قانون‌گذاری تمام شده است.
🔹
اگر ثبت احوال، وزارت کشور یا دستگاه‌های مرتبط در اجرای این قانون اهمال می‌کنند، باید درباره دلیل توقف صدور شناسنامه پاسخگو باشند.
🔹
این موضوع در اولین فرصت در کمیسیون مطرح می‌شود و به عنوان سؤال از وزیر کشور پیگیری خواهد شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/659084" target="_blank">📅 20:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659083">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
وزیر انرژی آمریکا: تحریم‌ها علیه ایران می‌تواند تا حدی برداشته شود؛ اما نه به طور دائمی و نه کاملاً، اگر توافقی حاصل شود و ایران شروط اولیه را اجرا کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/659083" target="_blank">📅 20:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659082">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
اسکادران ۱۵۷ ارتش اسرائیل که در حمله موشکی سپاه منهدم شد
🔹
اسکادران ۱۵۷ نیروی هوایی رژیم اسرائیل ــ که یکی از تأسیسات آن در پایگاه هوایی رامات دیوید شش روز پیش هدف موشک‌های ایرانی قرار گرفت ــ به دلیل اهمیت مأموریت‌های محوله و سامانه‌های مورد استفاده‌اش، یکی از محرمانه‌ترین یگان‌های هوایی اسرائیل به شمار می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/659082" target="_blank">📅 20:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659081">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
ترامپ قمارباز : در واقع، آنها دیگر خواهان سلاح هسته‌ای نیستند و نه از طریق خرید، توسعه یا هر شکل دیگری از تأمین، چنین سلاحی خواهند داشت ‌
🔹
قرار است این توافق فردا امضا شود و بلافاصله پس از امضا، تنگه هرمز برای همه باز خواهد بود. #Devil
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/659081" target="_blank">📅 20:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659079">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QImlEM4dDeGtwS1TIjacJisBnsXQACiBFn7i7byJ10Kc0uO3b-jtxWUdlrZFIZpKj66MC_dVwDpHMkXErW5EsRSQ6mF3zZmeeW1h1LjEI9oMlOcK9NeCaoOw5cbzYePeW4d8_FuSL4NW9yEmlpJWu1terqKELlhoP8Z5R6FcH-RPdy0MfUdUbNK-O57CMoFIQX556qyfZLoJOLZjRaTf3qSRzz8rluttYlu9eV-TWcDnbgzc_KyPHWNvkCIEeDyQHb98o8FMZ792E86E-__Pgs9Ra2rzY50EJAf1ZqWjPg9xkf7KPeLk6M84bDs0vokgCRuhNLGDYVSs6ryDC7868A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdTuFndBwJb4wqVrhROD4mff4TZyWpVi_8nT7bCckhzqHwKV5Gca6EvRiYaUrjkcbev1SPW5H9XlapGcFsmz5R4SKeBtFI4IMD-NLcXtDXevee2DxImnPzI_7hCG6AoDCxhCjyYut7nDyaakU0KMgRBwNljv0EsMEgz5kwkfuL2xNFnQ-F1JsuQ8ue56roOfS5xRV5GJQThMhXw52Zc2gDPsAhxEgX4YgVaZWQ16uDW3CV8rRilwxkAGzyXMwORKNxhjftITXdSr-2qflsC1z3H79EDQeowWC-7KwyFSCPckjL1OYBzbI6vj1hK4MxjyTEFg5RmnQmkiGlK1wW0YIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: بر جاده‌های آبی سرخ
🖋
نویسنده: نادر ابراهیمی
🔹
کتابی تاریخی داستانی که روایتی است شاعرانه از اراده، مقاومت و هویت ایرانی. این کتاب روایتگر زندگی میرمهنا قهرمانی گمنام است که استعمار کوشید او را «دزد دریایی» بنامد؛ اما مدافع شجاع ایران و خلیج فارس بود. قصه مردی که تنگسیری زمان خود بود.
🔹
اگر می‌خواهید کتابی بخوانید که با حال و هوای این روزهای وطن هماهنگ باشد و اگر قلبتان برای خلیج فارس می‌تپد این کتاب برای شماست.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/659079" target="_blank">📅 20:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659078">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ادعای ترامپ: «توافق باراک حسین اوباما با ایران، یعنی برجام، جاده‌ای آسان و زیبا و هموار به سوی سلاح هسته‌ای بود که ایران شش سال پیش به آن می‌رسید و تا الان دیگر مدتها از آن استفاده می‌کرد ‌
🔹
اما توافق من با ایران دقیقاً برعکس است: یک دیوار محکم در برابر…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659078" target="_blank">📅 20:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659077">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKBf4Bo4bk9rulc_wDmvD7_-h9l7vozsUmyyv9A4JmO5_yXFVIUlYSPfEsGkM3g9GCdoiZKHtV6ZA3pFEw93bF1zt4SxTl8I6TcaIdDxE2R699pcrnbsVLgvXuPUaBxSWhtDFsXTJctxWA4d5sjVwEqrIfi_OrGUIjc4FNhZ4vuV2NLBR0bNnyb14BMHwwU3MDjrUVDNgE9DTotPiUN9q1wn72PRHPPXX8TGJJMjar3P9DIHjd9Bh_7WlGA_58UPdMhwPeJrZwNiDutncU1PLUkB2UpjxlDxWtxIoYmPyRJcF414yI3DMest3-6o-68GDKO9-7e6rBrx_7wgTQrwqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ: «توافق باراک حسین اوباما با ایران، یعنی برجام، جاده‌ای آسان و زیبا و هموار به سوی سلاح هسته‌ای بود که ایران شش سال پیش به آن می‌رسید و تا الان دیگر مدتها از آن استفاده می‌کرد
‌
🔹
اما توافق من با ایران دقیقاً برعکس است: یک دیوار محکم در برابر سلاح هسته‌ای!
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/659077" target="_blank">📅 20:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659076">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
عبور یک ابرنفتکش از خط محاصره آمریکا
‌
تنکر ترکرز:
🔹
یک ابرنفتکش دیگر با عبور از محاصره دریایی آمریکا علیه ایران، تحریم‌ها را دور زد.
🔹
این نفتکش بدون اجرای عملیاتی پیچیده و صرفاً با خاموش کردن فرستنده سامانه شناسایی خودکار کشتی، از خط محاصره نیروی دریایی آمریکا عبور کرد.
🔹
با این اقدام دو میلیون بشکه فضای ذخیره‌سازی دیگر در دسترس قرار گرفت، تا در صورت نیاز، ایران بتواند از آن استفاده کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/659076" target="_blank">📅 20:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659075">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
غریب‌آبادی: ترور فرماندهان ایرانی نه تنها اراده ملت را نشکست، بلکه پیروزی‌های درخشانی به همراه داشت
معاون وزیر خارجه:
🔹
یک سال پیش، در بامدادی که دشمن آمریکایی- صهیونی گمان می‌کرد با چند ضربه می‌تواند اراده یک ملت را در هم بشکند، نام‌هایی برای همیشه در تاریخ ایران جاودانه شدند.
🔹
رژیم صهیونیستی که برای ادامه حیات خود به ترور فرماندهان و دانشمندان یک کشور مستقل نیازمند است، قدرت را نه در میدان، بلکه در استیصال، تجاوز و جنایت جست‌وجو می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/659075" target="_blank">📅 20:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659074">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ادعای ستاد فرماندهی مرکزی ایالات متحده: از زمان آغاز محاصره بنادر ایران، ۱۴۱ کشتی تجاری را منحرف و ۹ کشتی را از کار انداخته‌ایم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/659074" target="_blank">📅 20:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659073">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
مسئول تأمین مالی داعش در الأنبار عراق به دام افتاد
🔹
اداره اطلاعات نظامی عراق از دستگیری یکی از عوامل برجسته اداری و مالی گروه تروریستی داعش در استان الأنبار خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/659073" target="_blank">📅 20:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659072">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
آموزش و پرورش: تغییر زمان امتحانات نهایی به‌دلیل تشییع رهبر شهید در دست بررسی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/659072" target="_blank">📅 20:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659071">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBBkR-_Yr62uG6e-_4BPoJ3QgMhJSCksySa6S-1Eg68q8Rpk3eSW1TW1gK9nkZ1yLUvQlEoET6xgUUOZ9CMDNJqsRNh-qf6A8UNwCsgAlfGEKYoCi5pIFJuP0KUMRu9aNhuiCpyRx67EwsiVVzmnpvodw9TOICpiEG9GTNEU66a35XhfzMhbJsNzYfFzw4ABpg6LeCSODJviBvCBDE4X1lmTTm9aiThLgskQqSzfge-84xCtKXCXJt1bEyv7V-5kE7rgreyYQmLyHRddZQSB0fMKZTsQ06Xyh1HknCbYBHVKA5CQnon_tfDQo4nx7EpwGvGRqn6K37t0mcRjikMSFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: جنگ تحمیلی ۱۲ روزه، بار دیگر اثبات کرد که فراتر از هر سلیقه و دیدگاهی، وقتی پای ایران عزیز در میان باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/659071" target="_blank">📅 20:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659070">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/526ce4aa07.mp4?token=XJ9sQbOCsUe9HU1y9V_O3D7iiYEeZOxVzB0VtaRXdJAPKxZB0e1zevllq-l6iUNET_hk_yNlV5xAidqbHQ8I5OKASKFvmb5sJMwUgqawp5RgQFRaKtvdviMCQC-LOiCdLZOXra0G0nW2_qaY5SvmF8YIqTOknfkkvLStIC0SxanC3E-1AXekfjrKflSiQd0ul3mlgcmqaMiBD7L-lPzb7T5RAZd4Jf-URm-FO7EZM_lEGWfe5vjNmiOqxnmArYZdoF5fLF8A7gsUXTNIGafPncyTiV3QWKDI-jgXhyw00YuZiL-4Tggoyd7C_DobFT-KNGaLnywg6JfZf5rYdiYWLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/526ce4aa07.mp4?token=XJ9sQbOCsUe9HU1y9V_O3D7iiYEeZOxVzB0VtaRXdJAPKxZB0e1zevllq-l6iUNET_hk_yNlV5xAidqbHQ8I5OKASKFvmb5sJMwUgqawp5RgQFRaKtvdviMCQC-LOiCdLZOXra0G0nW2_qaY5SvmF8YIqTOknfkkvLStIC0SxanC3E-1AXekfjrKflSiQd0ul3mlgcmqaMiBD7L-lPzb7T5RAZd4Jf-URm-FO7EZM_lEGWfe5vjNmiOqxnmArYZdoF5fLF8A7gsUXTNIGafPncyTiV3QWKDI-jgXhyw00YuZiL-4Tggoyd7C_DobFT-KNGaLnywg6JfZf5rYdiYWLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تماشاگر جنجالی در بازی آمریکا و پاراگوئه زمین‌گیر شد
🔹
در جریان دیدار تیم‌های ملی آمریکا و پاراگوئه، یکی از تماشاگران تلاش کرد خود را به زمین مسابقه برساند، اما نیروهای امنیتی بلافاصله او را متوقف کرده و از ادامه حرکتش جلوگیری کردند.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/659070" target="_blank">📅 20:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659067">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJ7FQO1xMfMGv9_roRbftHjrySlAsoPbZsN_b8XRwXdwYwXNXtZbXmXVdlDY_2d6orR2U0lkg_shg_jFqOcOAWVySg73BTUNGKJlJ7Jtu7e8ohfSvU0o-dbxbnfa7x9Bv1t7qZ63kMbR1vGoV-uJQ1Kqg0KJ-S7wj1vkrS5f6yNiXHuSd-YFqp7M4ui96PKRe5QIxdEmrLBM1A5x1KTgszutQLvmt-J3UNUvRJ_nh8SesP-yKCyNNpjmr9PPnPsUNvDg4q4euUHn7m-D9pEjUFD-vQ4HK79tlfLNjllWCD9tukkBE3l1TJN0o0UwpZdY9MJzKu7kSeYfZitvxzykfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از دیدار امروز معاون وزیر خارجه با سفرای چین و روسیه، با موضوعِ تبادل نظر دربارهٔ آخرین تحولاتِ مربوط به پیش‌نویس یادداشت تفاهم‌ اسلام‌آباد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/659067" target="_blank">📅 19:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659065">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
دارندگان طلا ثروتمندتر از مالکان خانه و خودرو شدند!
🔹
هر مترمربع مسکن در تهران که سال ۱۳۹۰ معادل ۴ سکه ارزش داشت، سال گذشته به کمتر از یک سکه رسید. همچنین قیمت یک پژو ۲۰۶ از معادل ۳۲ سکه در سال ۱۳۹۵ به تنها ۶ سکه در اواخر سال گذشته کاهش یافت.
🔹
کارشناسان معتقدند این عقب‌ماندگی مسکن و خودرو در برابر طلا، یکی از عوامل رشد اخیر این بازارهاست./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/659065" target="_blank">📅 19:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659064">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frP8bYsbdv2rC3994JcUI7oiXbGvtCgvbDN7QRYR1ptOqS5V1iQmEKHyAkgEwrKix3BxX_C8OVpiCjxzOcx6SQ1t4dau0iMlT1pt-k7VkfJdh5rmYo2f1T5894OKSpZZE88nYu4PEGGfi5g3fgEX6Ta_lrSlpSWmEBAg_zf1K9KNEN9hYpdjkEnW7sKvctz_zRtIijU0BkonMrXNRSFwFPYPN6U2wDKHQQJR_Oh_uMTI1Uzn75fPcYIPI8WhtJRFDTg6tmzw3sI7Os7Pa8IWMFNq1LPYqevDj4d_8KUeDUC1Us3ouLQY3rTAOi-gOO5D0pMgAAMs8qIFhHyOB7-mYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا چه بهایی برای حضور نظامی در جنگ با ایران می‌پردازد؟
🔹
آمریکا در ۶ روز نخست، بیش از ۱۲.۷ میلیارد دلار هزینه نظامی متحمل شده است.
🔹
شکست اقتصادی، کسری بودجه و ناترازی سوخت از جمله هزینه‌های جانبی این تقابل عنوان شده‌اند.
🔹
هزینه روزانه فعالیت ناوگان‌های آمریکا نیز به حدود ۱۰۰ میلیون دلار برآورد می‌شود.
@amarfact</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/659064" target="_blank">📅 19:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659063">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d837c54ce.mp4?token=DMuKI0xF7btZ1kVMa6PqCBRwQUqIR6vIGjpz1IYsaoPfZGiTjyVghBPq65FqoBM9C0ADCJAtG8nKb_S4xOhcz9ZvI9u6_A0YhfHD03eem9vhKqistXdb6GFicfD3JEXif9ZsQzdfH94XMx6Qr4tVHWZWTmnZCzDmOx2p4uqcRsHUKG7Qk8tPbPxIJbiTIM-xUR-oE8Ft_gKRiIPcC_c1OkjS7OIfAIr3AZ3qUdP3JgPZKTPs5wJoWR_sJ1cqnOs-aHCwTOjAqZRmPepkguybWkVeCshPYZmp2jjflaSb0GCY_zKHRGCzA--aYEiu5Hws1RJIO95xet_1nyJzDMkn0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d837c54ce.mp4?token=DMuKI0xF7btZ1kVMa6PqCBRwQUqIR6vIGjpz1IYsaoPfZGiTjyVghBPq65FqoBM9C0ADCJAtG8nKb_S4xOhcz9ZvI9u6_A0YhfHD03eem9vhKqistXdb6GFicfD3JEXif9ZsQzdfH94XMx6Qr4tVHWZWTmnZCzDmOx2p4uqcRsHUKG7Qk8tPbPxIJbiTIM-xUR-oE8Ft_gKRiIPcC_c1OkjS7OIfAIr3AZ3qUdP3JgPZKTPs5wJoWR_sJ1cqnOs-aHCwTOjAqZRmPepkguybWkVeCshPYZmp2jjflaSb0GCY_zKHRGCzA--aYEiu5Hws1RJIO95xet_1nyJzDMkn0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار دو اسطوره در حاشیه
#جام‌جهانی۲۰۲۶
🔹
رونالدو و رونالدینیو برای حمایت از برزیل وارد آمریکا شدند
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/659063" target="_blank">📅 19:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659062">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58e1dbb1ac.mp4?token=QnuRWNK8Yg3U4jAE6qcQemEjWzqxlaKlmtHFMSKS0tYCJSs3aKOrEAyRMidSG8T5Jc4D0kpACAsYfYuF6M5Vc7Gw0BNxa8oBh5KBHOnvGUWmh8meq84N9i2Ror9N4YGmxmRtV706E3W0iYkFY5VtnU9MiqeNdHh235HctW3ntzl-e7_6Bc1N_FcP1-yMVyyLoq-f0fGA5ZfTWnUa6LiWDp0uPWF8yptK1inwE09nfHyXoMNWMIDo38HoZ5_lOInA61mkxiSKI6AGvO73nXEHY0W-68xnBJ0XfcVpbViAUWQLOycfysXGAXcB7L0GeAemugWM0kIfNQjbLtoi88ALDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58e1dbb1ac.mp4?token=QnuRWNK8Yg3U4jAE6qcQemEjWzqxlaKlmtHFMSKS0tYCJSs3aKOrEAyRMidSG8T5Jc4D0kpACAsYfYuF6M5Vc7Gw0BNxa8oBh5KBHOnvGUWmh8meq84N9i2Ror9N4YGmxmRtV706E3W0iYkFY5VtnU9MiqeNdHh235HctW3ntzl-e7_6Bc1N_FcP1-yMVyyLoq-f0fGA5ZfTWnUa6LiWDp0uPWF8yptK1inwE09nfHyXoMNWMIDo38HoZ5_lOInA61mkxiSKI6AGvO73nXEHY0W-68xnBJ0XfcVpbViAUWQLOycfysXGAXcB7L0GeAemugWM0kIfNQjbLtoi88ALDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داغ سیاست روی دل جام‌جهانی
🔹
تاریخ جام جهانی تنها به گل‌ها، جام‌ها و قهرمانی‌ها خلاصه نمی‌شود؛ این تورنمنت بارها تحت تأثیر جنگ‌ها، دیکتاتوری‌ها، بحران‌های بین‌المللی و تحولات سیاسی قرار گرفته است.
🔹
در این ویدئو وقایع سیاسی شگفت‌انگیزی را در دل جام جهانی خواهید دید‌.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/659062" target="_blank">📅 19:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659060">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه پاکستان به الجزیره: اسلام‌آباد فردا مراسم امضای آنلاین ویدئویی توافقنامه صلح آمریکا و ایران را برگزار خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/659060" target="_blank">📅 19:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659059">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kc-gccWg4850FkOdlV8hMu2NM5HmqbUgw9EWxl4vDXP7cHfN4eocyFnOJVn_gtvJZJvl3CTztKhvZLbbyovwh5bwq6GK28ksRpeYIJN12CzhQh_26LT_GTHovxiRTpqMv_ciBMIpwc0TyGASzgyaWR29aKZEBqswb8HteHl3VDm2nLpVyRaWqh1faiEkYqm29Q2u_46hEccFNXnKqyowEHKykNhWKoq3PyT-rX1hq9zRUvYavjp7P-KWEZ7DdOWM6VEHuCsmy8u7mGWZcZ7Wx57QNepiZgQOuueUyxIwD14Hg5IicwZu7jVBoSwX60lm3BXoF_0BogfhsGUxdonr7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از حمله به یکی از مهم‌ترین سایت‌های راداری آمریکا
🔹
تصاویر ماهواره‌ای جدید، تخریب سایت رادار هشدار زودهنگام آمریکا در جبل دخان بحرین را پس از حمله پهپادی ۱۱ ژوئن نشان می‌دهد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/659059" target="_blank">📅 19:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659058">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77cef5107e.mp4?token=SyXvwAN8IgdGPbNjfoyNNKz2u3pCHq5Q3LHvCqEaHdJQ_DXqOI0oJlORdwTyiyY_ctx3PekCAb5ll_IQCVWbnjGXQ080cZ2sSVNAW6ivY54eOjt3pKz6ntvm7NHKuz7vn6JYqKITxpsfYZgfnc8_8dgF1sOJolak1xTf7Ms2cfqUy7Drz2WJXWiPXwKLOQJ-urvvKAj1Lif-CshlK7sn_uhMmYArW9PHpkIKvkdQnNxFXO8zU9zFxT0TOIkAP9gnNwBbsbG1evux0NnfKQ6xID-DBm5CD7QCzt3njZC5lzyHd29Mz397z0oTFGsiWC_s0f00Qt7q9bDkwDVfQuoItw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77cef5107e.mp4?token=SyXvwAN8IgdGPbNjfoyNNKz2u3pCHq5Q3LHvCqEaHdJQ_DXqOI0oJlORdwTyiyY_ctx3PekCAb5ll_IQCVWbnjGXQ080cZ2sSVNAW6ivY54eOjt3pKz6ntvm7NHKuz7vn6JYqKITxpsfYZgfnc8_8dgF1sOJolak1xTf7Ms2cfqUy7Drz2WJXWiPXwKLOQJ-urvvKAj1Lif-CshlK7sn_uhMmYArW9PHpkIKvkdQnNxFXO8zU9zFxT0TOIkAP9gnNwBbsbG1evux0NnfKQ6xID-DBm5CD7QCzt3njZC5lzyHd29Mz397z0oTFGsiWC_s0f00Qt7q9bDkwDVfQuoItw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویداد تخصصی «نقطه تصمیم»
آینده از آن کسانی است که در «نقطه تصمیم» درست می‌اندیشند.
جمعی از مدیران و کارآفرینان برجسته حوزه فناوری و اقتصاد دیجیتال، از تجربه‌های واقعی خود درباره بحران، بقا، رشد و آینده کسب‌وکارها سخن خواهند گفت.
یکشنبه ۲۴ خرداد ۱۴۰۵
ساعت ۱۶:۰۰
مشهد | هتل نوین پلاس
https://evand.com/events/نقطه-تصمیم-015774
#نقطه_تصمیم
#DecisionPoint</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/659058" target="_blank">📅 19:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659056">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPrRg5DkYG2csSpFLv4EZKTMWm1aCRvmhb3T4fVZJt_yIWA1IvM3qQoQQFcUssHPdmVNsPWGozbT_yoWKG56P7iW4hJNR60_e0L8yKe_82M3ubT-UcZltuKpYT5mokftBzu12tNl906U9AWhP-jQPSQq4rPY0C7yqIZPZBn3fUo0AyCSSr-r-JqiN6xRxJMupfaAachxQr1i1UYZfXBb2KNTfwQ-qdVrQmCP5zuK_liL9G2_vA9qa_kVgI8snSVusUpGINSWsdloNqDNPb1FuNpqU-wbSVYeZzZBQB6FI0lQB5oSw4Ku5gKLqfztBHLyPcwCWotedO9AwRgMsT63LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef5608be81.mp4?token=UeXElB4QP-IVeuwsu9B3vXl4I8sykFoA6cFmIXlKcKjGZrqzI0AUze_j8JhP8rZ4QO-aXkSfk2cj1nhcgg3w-kfKsiwXfi269-5b8m_UOuvRNafe7MbFQOOK8e5W_MsAVmXsWXWnmVT1erC7Nh_0WyE_XnZX1JMB0SOvc7C6tia4u9-yxGmXXOZin-7or5Ib_t2sha1rUNvmU9HjwBIlYihtlcTnFS5DrC952sF25EAVpwHOKs7dfyOTrz18O2sQbKIDp5zMZVVlCqSY82-5ANJ1pyhP6SE3nOYLqNhNAY9VATRKKKqNvgydq1zbjDTOJpMauwze1TB2BkHv7n9TSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef5608be81.mp4?token=UeXElB4QP-IVeuwsu9B3vXl4I8sykFoA6cFmIXlKcKjGZrqzI0AUze_j8JhP8rZ4QO-aXkSfk2cj1nhcgg3w-kfKsiwXfi269-5b8m_UOuvRNafe7MbFQOOK8e5W_MsAVmXsWXWnmVT1erC7Nh_0WyE_XnZX1JMB0SOvc7C6tia4u9-yxGmXXOZin-7or5Ib_t2sha1rUNvmU9HjwBIlYihtlcTnFS5DrC952sF25EAVpwHOKs7dfyOTrz18O2sQbKIDp5zMZVVlCqSY82-5ANJ1pyhP6SE3nOYLqNhNAY9VATRKKKqNvgydq1zbjDTOJpMauwze1TB2BkHv7n9TSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنجال برای اردوی تیم ملی ترکیه
🔹
ویدئویی منتشر شده که در آن ادعا می‌شود چند بازیکن تیم ملی از جمله چاغلار سویونجو در حال استعمال دخانیات دیده شده‌اند
🔹
این تصاویر واکنش گسترده‌ای میان هواداران ایجاد کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/659056" target="_blank">📅 19:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659055">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ادامه اختلال در شبکه چهار بانک؛ کارت‌خوان‌ها جواب نمی‌دهند / مشتریان در پمپ‌بنزین‌ها و فروشگاه‌ها گرفتار شدند
🔹
اختلال گسترده در شبکه بانکی بانک‌های ملی، تجارت، صادرات و توسعه صادرات از صبح امروز شنبه ۲۳ خردادماه، علاوه بر توقف خدمات بانکی، دردسرهای زیادی…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/659055" target="_blank">📅 19:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659054">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnR6nn7fV8pKRLVIMRjYTQx01Ju_c3yE_yztK6axO3JDuxEe3ZFn3MwCHHAILHwqNTpuE0wIKqvmSsQURAwRaT5Qpv2f0X5YMGK6iSTEExtWCXEAgvgNXEb9NXEZSFfQV5iuzdSB5XIlde5W-S9mc4Re_81-SO2gWW2WFpdyIsk8Yv5_w_9TltdEhQXNB8qnFpWt5KGhYJPZaOx8-JGqBN52tE6LCY9J_LSoXTxcmZKjjPm6lo58xhGf9bbnl_z3bsSKk3C93gcDHy84njttvFYte4_tYrzHy_ZpzldyrKwvGF3mu6dzUs1lBUdETVhj0atX1JbIiJVtwQ0Jr34NsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلگراف: ترامپ به‌دنبال امضای تفاهم با ایران پیش از نشست گروه هفت است
🔹
روزنامه تلگراف در گزارشی مدعی شد دونالد ترامپ رئیس‌جمهوری آمریکا می‌کوشد این سند را پیش از آغاز نشست گروه هفت در فرانسه نهایی کند.
🔹
نشست گروه هفت به میزبانی امانوئل مکرون رئیس‌جمهوری فرانسه در شهر اویان-له-بن در نزدیکی مرز سوئیس برگزار خواهد شد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/659054" target="_blank">📅 19:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659052">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
توضیحات علی باقری کنی درباره حمله به بیت رهبری: به برخی از نقاط از جمله محل حضور رهبر شهید، بیش از یک موشک اصابت کرده بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/659052" target="_blank">📅 18:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659051">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTUrmCbiSZI9iXstZbMmKNSgrQwmTn8F7Zkrdnu4e41Fwi7dDy0JjPgnhPFBTdnCc-ErADWEZWxo3dDBCsdNJAo7Ka4OgTabNejaqZSDhq_-ctJGyu-OTSWqeq34PaYJtCxxfqEV8UByBeSv7qYn1PhTzu5iyhJ74mdv9bed-N91uUBbWlvMUovyfnjIrxDiiXuNUT6P987cucsFlxvwK-IKfexFFktbp2lPULUXyTYfSfqcoIwh1gXNTekj1CtrW_6sQh0n3rlm2DXkxqlb9UYCBJQ8s-hfcxsuhwOon-sEV4No4o-Y75en9FZa8oI4BUtXLQys44XhUGJAPp4UXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/659051" target="_blank">📅 18:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659049">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
صندوق بیمه روستاییان به خطر افتاد!
🔹
با گذشت نزدیک به ۲۰ سال از فعالیت صندوق بیمه اجتماعی کشاورزان، روستاییان و عشایر، این صندوق با سه چالش جدی روبه‌روست: پوشش تنها ۲۲ درصدی جامعه هدف، مستمری‌های ناکافی برای تأمین هزینه‌های خانوارهای روستایی و کاهش پایداری مالی.
🔹
نسبت پشتیبانی صندوق به ۹.۵ بیمه‌پرداز فعال برای هر مستمری‌بگیر در سال ۱۴۰۲ رسیده و پیش‌بینی می‌شود این شاخص طی دو دهه آینده به سطح بحرانی ۴ کاهش یابد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/659049" target="_blank">📅 18:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659048">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWxCl_NkvdAZpOdh_21PnU0fo2NSQofBRsO_ufmou-5vyYoz47lpA8ocJZXjtCgU1Jg_METkZ3EHDbAJBS1admEcbmMEUjUONBNXyMqEMoJK60D1vJuu1ZMP0yvd-pAvOMi9-10xJ2qClM8kG53PFItUejMhxHus0QjpORkZRVhP2pR5lEJpdtbHK-TdjorKGCe1RtnzeDpHGykkOk_w6bklbx4FC7Wq9rEsbrGA9Vjxm1MIvpllQv06gBeyW4iQYICpaEvhgi8VHHgJ7P2j6wvko5ImYWM_NRxU_jZr0rjSuFY5bH7OzuCAkxiz5yZax-upDjY6wkMQVtgm5q0MOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط ۳ دقیقه زمان نیاز دارید!
اگر به فروش و بازاریابی علاقه‌مندید و دوست دارید در یک مجموعه رسانه‌ای قدرتمند و پویا در
#مشهد
فعالیت کنید، فرم ارزیابی اولیه را تکمیل کنید.
✅
۱۰ سوال کوتاه
✅
بدون نیاز به مصاحبه اولیه
✅
بررسی سریع رزومه و پاسخ‌ها
برای شروع روی لینک زیر کلیک کنید:
👇
[
https://survey.porsline.ir/s/UxvsfaZk
]
[
https://survey.porsline.ir/s/UxvsfaZk
]</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/659048" target="_blank">📅 18:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659047">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgin0HkfrK5jYPL36B-tUfTVeZOQKhKw1-ucc6wD-33WRj2gd3rxWWcxyT6VmEkvC2LVDj2RQ51QUD-9dUaPf7anGDIvGtFyobVBcsQg5nyvvMUwApQV5179Yy-XMIbVyIEwyFtWYXnB2kZev3Q_zX2HdGUZdKD_63GT2iA8P9HniRsg5B06nNO2mIwKyJ0jkBQpORpLlZ5zYt7_X7ViOb-yyRVSyIHXEhhjuyy85FrmsZM_wh_qkplz_D3B3TnWWGvDkp5Gou9zzu24zyGF_QKECNvToLKsot3AuM6dNoB0H_wotehr1jFefCDj-I-l_VBTBBxAUP2PDjjVpk5w5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عباس‌میرزا، شاهزاده‌ای که آینده ایران را در سر داشت
🔹
عباس‌میرزا، شاهزاده‌ای بود که شکست را پایان راه ندانست، بلکه آغاز بیداری ایران دید. در میدان جنگ دلیر بود و در اندیشه اصلاح، پیشرو. او آرزو داشت ایرانی نو بسازد؛ ایرانی با ارتش منظم، دانش روز، مدیران…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/659047" target="_blank">📅 18:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659044">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو هیات رئیسه مجلس: پزشکیان باید گردن بزند!
علیرضا سلیمی، عضو هیات رییسه مجلس در
#گفتگو
با خبرفوری:
🔹
دولت دیگر باید مبلغ کالابرگ را اعلام کند؛ مبلغ هم نباید کمتر از افزایش میزان قیمت‌ها باشد. دولت قول داده و رییس‌جمهور تعهد کرده است که اگر قیمت‌ها افزایش یافت، میزان کالابرگ را افزایش بدهد.
🔹
ایشان در انتخابات ریاست‌جمهوری اعلام کرد که روی حرفم گردن می‌زنم و امیدوارم فراموش نکرده باشند و گردن بزند درباره حرفی که زده‌اند. باید رقم کالابرگ افزایش می‌یافت چون شخص رییس جمهور تعهد کرده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/659044" target="_blank">📅 18:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659043">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
اختلال در خدمات چند بانک/ اقدامات فنی برای رفع اختلال آغاز شد
🔹
در پی بروز اختلال در خدمات برخی بانک‌های کشور از جمله بانک‌های ملی، صادرات، تجارت و توسعه صادرات، پیگیری‌ها نشان می‌دهد موضوع از سوی بخش‌های فنی در حال بررسی است.
🔹
از ساعات ابتدایی امروز برخی…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/659043" target="_blank">📅 18:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659041">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/migeADYxysTIBkTPO1ThBU2g2GA3wMF3R9RU9SZMM5_2EtZw8O-VxDUb6kwceGCPkGRBUG9PjCNTZfcUi9dBSk7HDHYEfBv5FnitvJNr846dtnvmGmsOyvrG2itdaef-opFBLYhBw9wnoi3encTe2510jPtINLkI95sRfL11BmcmnneZlEXoPk3Voi8fVlE3EncpOZPuKzlDnMo1zGmHmcIDTQspg_cWGCUYYkFjPoJGQ9Q-G_n9jwbFP_6HmIrmIyLvrde1lR9zCbMSFANNj6ZaTp3PNKfYKSrDlnZgqR2pQVTq5TBz1w_vPW8o--ij-NN4wr81oQn3hS9B9f4BJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکنیکی که کیفیت خروجی ChatGPT را چند برابر می‌کند
🔹
اگر هنوز یک پرامپت بزرگ می‌نویسی، داری بخشی از توان واقعی AI را از دست می‌دهی، یک تغییر ساده می‌تواند کیفیت خروجی را چند برابر کند. #نبض_تکنولوژی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/659041" target="_blank">📅 18:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659040">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUzjuepCtDumYCCEA3bTp4YXibEJQsCtJ5TksVRESoK0GsJiw6NUU6_B4UdfVgFhpEIOwSGHyO2E1bqz29my7onhwso2KGgeclvjsRX_DLWXlXbkiToeqlO-p0NvjRcxSSnUEQXZowdKwO8RZzEVk_RSlcBGM2pLzL1STpQK1OjnDPQDXS5-vvfZXteZ8ernVYRyOJ5bM5M6EyQq3LxuesILdy3THvyY9KJ-zrHKfWFveNyalWHUZAjEOSC-fUo4GDstKoB5OYNKBtddIcWC-Lt0NwSjpjdTgK7koITy7h5J0o1IgThvt62oiqixtkfLh1wxgC_s1A9jmOkXSzrA-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبق پیش‌بینی سایت اوپتا، ایران به‌ عنوان تیم دوم از گروه G صعود می‌کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/659040" target="_blank">📅 18:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659039">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRVbBu9a_9w8lY-HlT-qRVF003gxvBxr-z-CjOoL9PxD0zILaHW2H0mdgaFtzBoKaPP2pQVX0FJq5-GGe5xOD8trsy5IA_QrQDG2C1gyAUO3T3tmjcFlaOS7q5kPt3xeFzhXAaIOCD2swfRaKtaj28jVn8raEIvIschmn7f7upVo2PwW3FI_Woj0_rQ5Ugc4Xl6G8g0EbEZtPRhRHH2aD5dxdMhhgPlCky_ZM9-78p3nsg9uH3aqc9ASKAzzTYWutb7cDZeYMz15_kQM27h_ejKeR_TkZiRgK7phtUySXCJfTpIDH385FchPKYFd8OTymu4WoB6BSKWXF9NrUQ9FgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستگاه‌هایی که بدون اجازه شما دزدی می‌کنند
🔹
سایل برقی در حالت آماده‌به‌کار، شارژرهای متصل به پریز و دستگاه‌هایی که ظاهراً خاموش هستند، ۵ تا ۱۰ درصد هزینه برق خانوار را به خود اختصاص می‌دهند.
🔹
طبق آمار وزارت انرژی آمریکا، این اتلاف سالانه ۶۴ میلیارد کیلووات‌ساعت برق و ۴۴ میلیون تن دی‌اکسیدکربن تولید می‌کند. استفاده از چندراهی‌های کلیددار و جدا کردن دوشاخه وسایل پس از استفاده، راهی ساده برای کاهش این هدررفت است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/659039" target="_blank">📅 17:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659038">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXTSGuy6pxYcpMJu-NPzFO-jvN9H8p9Nc-AmKq7eDI2_sFqtzpzJH4v_hckZPT63cV4jhQAIdDsB_DRsnbA8e-nyTD9SM1QFhhsBo_Jf11CsUKslebCjkTMk91ZoVAwPK4XADeJ_qECO1Ap93QFQw65Zf_j-Au6pJeoDUjvNlzf6bLefMXT2hDIc5cOsKmoFK3pXfaqRM22KGyEpTN33fo8kXJT1MvpipKdRXEo--3P-npFULtkoEQdJJBri7-xe6SUg5kGpgPuxSeeRPVmcU7siSKAgXvAhd5_0opCS4W-L9HCfNDd0tveDIl5HbM8iIm0JJIBuc7z5exxutvV_2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر امور خارجه پاکستان به همتای سعودی خود: مراسم امضای الکترونیکی توافق آمریکا و ایران قرار است فردا برگزار شود
🔹
این با اظهارات قبلی سخنگوی هیأت مذاکره‌کننده، اسماعیل بقایی، که گفته بود یادداشت تفاهم فردا امضا نخواهد شد، در تضاد است، اگرچه او روزهای آینده را رد نکرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/659038" target="_blank">📅 17:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659037">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4I0kmlfRM8Wqrk4pjZt2CvCIVy8G6g8g2vjWT2QyOjMhdxIB3-DFuWwTTdaaYKEL3kpvJBjzElsuYYW-qN9OcrIUjFP9YwK6pSCzoQ_79J8ztv1vr8s-1TmTqElkGL3G1eCxrLxmv-jBleT03FN91WSCAbiMgUeHym6ck6tDTYse4tWL-uxIURqZcKz7uFjNQTin57uoiuTZyOLNzk65uUFLST4KhpZaohrVKE5ncPMT5GAlwgaq8IQegZxB9hK9NonSSLH5iQqVPwjWU2xY5GrTRw4z_d4CXowUgpT4jnfton-ukFkY65JXHmRNqZKpJ-kL8hKzC9qLgbltI6g3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ گیگابایت اینترنت رایگان، بدون قرعه‌کشی!
💥
⚽️
همراه اول به مناسبت بازی‌های جام جهانی، به تمام اونایی که مسابقات رو پیش‌بینی کنن، ۵ گیگ اینترنت کاملاً رایگان هدیه میده!
اصلاً هیچ قرعه‌کشی در کار نیست؛ یعنی پیش‌بینی کنی، قطعی نت رو گرفتی!
🙌
فقط کافیه همین الان:
1. وارد اپلیکیشن «همراه من» بشی.
2. بری توی بخش «زمین بازی».
3. فقط یه نتیجه‌رو پیش‌بینی کنی.
تازه فقط همین نیست، کلی جایزه هیجان‌انگیز میلیاردی دیگه هم در انتظارتونه!
🎁
🎮
⏱️
تا فرصت تموم نشده همین الان دست‌به‌کار شو!
📱
لینک همراه من:
https://www.mci.ir/-4S0XAJB</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/659037" target="_blank">📅 17:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659034">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde5949fcf.mp4?token=kc6xS5ZfOPeZvdc0MJJ3bezS3pl6RSbx_iJD5VjWiHM1fUxCVrj_K7imMpMywCgArDLg7RY-YnVdncPh3SJeRyBUY7KZQVi2Q9stH7jAMFnB_6t_dsfUE9mDSvZB5V_y3uRvYjksmUMvf9LgYwe3EHfCfN2mTKYvkfc7owE7brU5TXHaRUpXjweMRz3O1v0olsajB77ZU6W03o3qPWHMDYFRLoQ9G47aEXgqcxTg9DPwVDW5ZIvzXykqGZAJDkCdtaGvvQeBGhVIPz8n21sKuBiRqOQMp2Hl0c1FMzn2Im2Y5D4r9kxDMH_a2Slpt0t9Fklw8BccUqaI90_X8LY6spziBuVa9F3jCGFsfoPZWWn_VSp60wP5AHjbbhgzi942qJjBG08txGjgJZ4YA9MgfdzwolV5_YFqv9kW-YbFI1HYXhUPXwnZle-fKo5kSIAxcV3Dyf49EhIvy_DgVTMahAkPhsDZ9znm8R7qDpU8L6QDGCXSHPeMYyxf1nT9uPkEW0SUPglmsfOfJ8aDorJ9WNk65QZbGIPciYvQWPZFrWIduxES80nPSjnkIbEec6py1mDcGHh7Lr7DvOJMfOgYXtjzj3Z5yKSesvssx3101i5cOMoXLZkzezEIMQApdNEN2yxGT65AYbJPDq-sArqpDOjJB97CVB3JTN8PZoj97nc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde5949fcf.mp4?token=kc6xS5ZfOPeZvdc0MJJ3bezS3pl6RSbx_iJD5VjWiHM1fUxCVrj_K7imMpMywCgArDLg7RY-YnVdncPh3SJeRyBUY7KZQVi2Q9stH7jAMFnB_6t_dsfUE9mDSvZB5V_y3uRvYjksmUMvf9LgYwe3EHfCfN2mTKYvkfc7owE7brU5TXHaRUpXjweMRz3O1v0olsajB77ZU6W03o3qPWHMDYFRLoQ9G47aEXgqcxTg9DPwVDW5ZIvzXykqGZAJDkCdtaGvvQeBGhVIPz8n21sKuBiRqOQMp2Hl0c1FMzn2Im2Y5D4r9kxDMH_a2Slpt0t9Fklw8BccUqaI90_X8LY6spziBuVa9F3jCGFsfoPZWWn_VSp60wP5AHjbbhgzi942qJjBG08txGjgJZ4YA9MgfdzwolV5_YFqv9kW-YbFI1HYXhUPXwnZle-fKo5kSIAxcV3Dyf49EhIvy_DgVTMahAkPhsDZ9znm8R7qDpU8L6QDGCXSHPeMYyxf1nT9uPkEW0SUPglmsfOfJ8aDorJ9WNk65QZbGIPciYvQWPZFrWIduxES80nPSjnkIbEec6py1mDcGHh7Lr7DvOJMfOgYXtjzj3Z5yKSesvssx3101i5cOMoXLZkzezEIMQApdNEN2yxGT65AYbJPDq-sArqpDOjJB97CVB3JTN8PZoj97nc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از ترامپ آمریکا دست چه کسی می‌افتد؟
🔹
دموکرات‌‌ها و جمهوری‌خواهان از همین حالا خود را برای انتخابات بعدی ریاست جمهوری آماده می‌کنند، انتخاباتی که دیگر خبر از ترامپ نیست.
🔹
اما در اردوگاه جمهور‌خواهان رقابت داغ شده، آن هم بین برخی از اعضای دولت ترامپ! حالا چه کسی می‌تواند جای ترامپ را در اتاق بیضی شکل کاخ سفید بگیرد؟
🔹
در این ویدئو تماشا کنید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/659034" target="_blank">📅 17:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659033">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DS7SiuLsjJIdXMF-aTkWmgkYw0F9WIYxtqUKzBcABmeHZsE9-u4hrtoqK8W8LEkokBzEc565CZh_4xIOW2qeavzr2Gd3LtMUviEIKiMl8pclCeKg2niiY_hoA6R832_WNLDyiDIQmny_jTUXARKsnHBIJEokH4FhxQcDM1zcmS6t__I-Isjy6IL9o3L7aH6jTkQOe7QJcYk9-P1aOwITcCa8zJI9ZKppqmNPyKFkjdSrrK1DtKcsU7YeEyX8RxUBzixnXZMX_7YNOx95Y6b_0lZJ5yzB0NZtSIeuEF8VXj0RdVGQmKmWMgF9HDEiI32L_EL1SycOuGqO-HgqzIemMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخست وزیر پاکستان: ما بیش از هر زمان دیگری به توافق صلح نزدیک شده‌ایم و احتمالاً ظرف ۲۴ ساعت آینده نهایی خواهد شد
🔹
پاکستان در حال آماده‌سازی برای امضای الکترونیکی توافق‌نامه صلح بلافاصله پس از آن است و پس از آن مذاکرات فنی در هفته آینده برگزار خواهد شد.…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/659033" target="_blank">📅 17:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659032">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db235a359.mp4?token=BAGFLeSzJ7HL-2BjQURy8PaWtx3RJpRxtt7JvGlz4BqQNv5f3qsFsP8d1Dbk0cY3J82FwUUhAOo06S3ddTsqo3NtUU91fAeJ_hrdzzNiqzQs2g0rcAylxfn40JQgG6smHCO2s8tPFoWlBSaV94cJXLN3jgsT0bvXuBeIOqqxFqEscLIoqXkyXvPyZzQJlMABYT5jNZskG9E2meYJjwE7aB5FB3SCMWJEsjDvgxmgYOfYmu5zaJw_LJpniBwgBF0mJao3QDAlfUEScf-yMk9e4cf-HI0HLsCaC41Wm5FWNBuvYN8xNusylMHITmuFUmlsJfhBVxg3qQKbxhyolor2dx6i52Q5l3NSrmChiNxy96PNQV22FtOgDNOuawzeO7vpGW4_-5voaGALcRGBTvE_O17g3iccLLlER-XpjdrklPPBPuGP3FcTMPji0aI4Fkw13ogyqcPqogPMzK9_xoc6xMhG1LMd0v60g-7bF_lnU7AHk5WkCvV4VrYJSJUTLhU0JBv_vTJ4PV89GN54Twy3uCAA9dqaRsHHw2aX-QImDrjr_HzAi8HWQJMepTlYn2HQkPejo33CJS7pzLetUB1k26HR4hqUebigRzRycYu-O71QeYRtVJzBFclf7EGIlsYbjvOHwdF5ogzs-wGwuNOD9adkxUBIS7HIaUnu2saKi0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db235a359.mp4?token=BAGFLeSzJ7HL-2BjQURy8PaWtx3RJpRxtt7JvGlz4BqQNv5f3qsFsP8d1Dbk0cY3J82FwUUhAOo06S3ddTsqo3NtUU91fAeJ_hrdzzNiqzQs2g0rcAylxfn40JQgG6smHCO2s8tPFoWlBSaV94cJXLN3jgsT0bvXuBeIOqqxFqEscLIoqXkyXvPyZzQJlMABYT5jNZskG9E2meYJjwE7aB5FB3SCMWJEsjDvgxmgYOfYmu5zaJw_LJpniBwgBF0mJao3QDAlfUEScf-yMk9e4cf-HI0HLsCaC41Wm5FWNBuvYN8xNusylMHITmuFUmlsJfhBVxg3qQKbxhyolor2dx6i52Q5l3NSrmChiNxy96PNQV22FtOgDNOuawzeO7vpGW4_-5voaGALcRGBTvE_O17g3iccLLlER-XpjdrklPPBPuGP3FcTMPji0aI4Fkw13ogyqcPqogPMzK9_xoc6xMhG1LMd0v60g-7bF_lnU7AHk5WkCvV4VrYJSJUTLhU0JBv_vTJ4PV89GN54Twy3uCAA9dqaRsHHw2aX-QImDrjr_HzAi8HWQJMepTlYn2HQkPejo33CJS7pzLetUB1k26HR4hqUebigRzRycYu-O71QeYRtVJzBFclf7EGIlsYbjvOHwdF5ogzs-wGwuNOD9adkxUBIS7HIaUnu2saKi0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیاده روی ۵۶۰۰ کیلومتری برای حضور در جام جهانی
🔹
این هوادار پرشور برای همراهی تیم ملی اسکاتلند رنج سفر پیاده حدود ۵۶۰۰ کیلومتری از لس آنجلس تا بوستون را به جان خرید و خود را به جمع هموطنان هوادار رساند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/659032" target="_blank">📅 17:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659031">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdf641019b.mp4?token=Y3iz9AcSyt07-XjLngQvDYXVVT2puRdyBjZJgYfdOEzX4pmC0h_Iail9cgMz46Nobf7BQ-3rUyhbIlRZ8xvnff08dU5aYTENr0JUv5ZzrHeZ97NRzDT_yAIuHbBGUJyb5BT6KGni1KvHgiy9UhhPCy1Pt78Aq8Vt_9EnuzQkalgdbmbFD3CccAXpTncMMmVLDx3AuYEjnGIGwf7J00IoAYBr2XpBlBOVJf5PT-0Urh38zxvU83Sh3jM-_vHlQFWd-B53wTcebm3tasEAHqIY3N7t2te7-eC7U7ZUK0g32Up529tJSfDl18yjTwfHJx9B4OsNyK9NOc1NL2pM3UxNpla4PNmr7Lyo7y06aFjP7suAidButmdS23OFr2T5f_6I84hSLPCHGr5yTi0URIIiKjDppeSN7FqyYGaLhdwanrIUZYYMxdf5n-2iQMmmcB_2cbMeHpB4Gl_nJ9WCb1ixqW8OgAmsnPS0p4szXGVIZObjbMgSq3awyf8nCXD66fiSiwtDQaGPNAQ8fBWMOqTGC4KH4wDpNf_5fu_ylKXl0cW_cGx0lp7So90RY1v60d8AKLIt6fwedgcAktdOjSvUfxPzxUFkAbxOg92PRu9Qq_lwCdukAoacFyJdOQc4pRw9GsqhSCNIlAIFfW5TcK7cHQiHT1Y7WUqp13AJ3xZFFao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdf641019b.mp4?token=Y3iz9AcSyt07-XjLngQvDYXVVT2puRdyBjZJgYfdOEzX4pmC0h_Iail9cgMz46Nobf7BQ-3rUyhbIlRZ8xvnff08dU5aYTENr0JUv5ZzrHeZ97NRzDT_yAIuHbBGUJyb5BT6KGni1KvHgiy9UhhPCy1Pt78Aq8Vt_9EnuzQkalgdbmbFD3CccAXpTncMMmVLDx3AuYEjnGIGwf7J00IoAYBr2XpBlBOVJf5PT-0Urh38zxvU83Sh3jM-_vHlQFWd-B53wTcebm3tasEAHqIY3N7t2te7-eC7U7ZUK0g32Up529tJSfDl18yjTwfHJx9B4OsNyK9NOc1NL2pM3UxNpla4PNmr7Lyo7y06aFjP7suAidButmdS23OFr2T5f_6I84hSLPCHGr5yTi0URIIiKjDppeSN7FqyYGaLhdwanrIUZYYMxdf5n-2iQMmmcB_2cbMeHpB4Gl_nJ9WCb1ixqW8OgAmsnPS0p4szXGVIZObjbMgSq3awyf8nCXD66fiSiwtDQaGPNAQ8fBWMOqTGC4KH4wDpNf_5fu_ylKXl0cW_cGx0lp7So90RY1v60d8AKLIt6fwedgcAktdOjSvUfxPzxUFkAbxOg92PRu9Qq_lwCdukAoacFyJdOQc4pRw9GsqhSCNIlAIFfW5TcK7cHQiHT1Y7WUqp13AJ3xZFFao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد صداوسیما از عراقچی و تیم مذاکره کننده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/659031" target="_blank">📅 17:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659030">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_1Bd6BQFMWtcKbvR-8iq-9zSdP1RCRxObXnAJKsKpT1DwIvE-4ihCAdNoJauyEbQlweOM9Re-qE9_bYmAUJOLs8BGQ73kd-WIidgugc5d3HDEs47q2KPQ_iv1DfwIRTycX0UFGNspjfha-guNi0WNv-40zage3Z4SxQ-EaSyfZmSxbOy958SaJFWTavp3uHZZF2xCGMHNF4dgvdhAJT2ilO0buNk9VcBxqi1WdG8VsILAnX47shlBiIS_uGlPzIVDgXsannle71Tu2WpZ8qQ2NiO6O020NPhXoqu2cnHQ5sO93EQAWifZtGgKlFz5AKvPrsfbkDn9nM2uZ9B03P_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فاصله ۴۵ درصدی قیمت خودرو از کارخانه تا خیابان!
🔹
به گفته بسیاری از کارشناسان، مهم‌ترین عامل ایجاد این وضعیت، کمتر بودن عرضه نسبت به تقاضای واقعی بازار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/659030" target="_blank">📅 17:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659028">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdo-8W1tmjD9DNbP05u9l7gsWeR0eOWoygZgpnShMIjwM_xT6FqpuMS8R4UiPYQ_m6U77-wgrsFUCzYBbQ0AEuWRH2CCoczqjxBJEIL-6Ixxrye3J15-wRRX8ehCgKJl7hHhM8pQarOWvPgUAb4LMqs1d5XyAEnNTV3kgJNkCi5AJwH2InTzPpmojbrwtPPgBpYBh0XbufJxaAIGf8QYNHxMFP_kMDfFeoJb7PR9Z4mHKLCs4sDyuQGL6f5488jOV1KZpHpMowgtzD-BBYd-a7_aydUohbQC0BpXJ58eIFiFV99z65xAC-rbtqqPSM9JlY2k4POvzauupOoekWng0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علیرضا فغانی به عنوان داور بازی فرانسه - سنگال انتخاب شد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/659028" target="_blank">📅 16:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659025">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۱۱۶۶ خانوار جنگ‌زده هنوز در هتل‌های شهر تهران اقامت دارند
علی نصیری، رییس سازمان پیشگیری و مدیریت بحران شهر تهران در
#گفتگو
با خبرفوری:
🔹
مجموعا ۲هزار و ۹۸۸ خانوار و بیش از ۹ هزار و ۳۸۷ نفر در ۴۶ هتل سکونت اضطراری داده شدند که افراد گروه‌های «ب»، «ج» و «د» مشمول اسکان اضطراری هستند.
🔹
در حال حاضر ۱۱۶۶ خانوار و ۳۷۹۳ نفر همچنان در ۴۶ هتل حضور دارند. تاکنون ۱۴۶۷ خانوار ودیعه مسکن و اجاره دریافت کرده اند.
🔹
ودیعه مسکن با میانگین مبلغ ۲ میلیارد تومان و اجاره ماهانه میانگین ۴۰ میلیون تومان است که بیشتر از این عدد هم اختیارات به شهرداران داده شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/659025" target="_blank">📅 16:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659024">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ادعای اکسیوس: موضوع دارایی‌های بلوکه‌شده ممکن است در قالب یک توافق محرمانه جانبی حل‌وفصل شده باشد
🔹
به گفته یک مقام آمریکایی و یک منبع از کشورهای میانجی، آمریکا، ایران و قطر در روزهای اخیر درباره سازوکاری گفت‌وگو کرده‌اند که بر اساس آن ایران بتواند برای…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/659024" target="_blank">📅 16:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659023">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9805bc1a1e.mp4?token=d6NyCtDZ5-04pF4NDJbVdthbiQaolDmSGn0EI3s8yxihih5VpmP5QqIrB6BDChXy9kkWZnqPhd6dpk95mjwBPB4y3z1GBzjUAYHsdNyDsjBWLfPU1LhzqOrB6xhPmCqJm6UnM5c3TZdTKU9fYwoB5sjFQmvt527m2i2Cn_dy_I4N81-68zUW3WxK8yosIq20S-SFI3B15YIKp1af9zDUJFtjUCeVl25GVL9KyhOH9OpZdberBwp_TR7oHLHwhoZUrzTyvmx0izE1QFHVYAGpkr7sf1mo_-HCuEMIh0RIr3WDma2ip7-upw1VJI_zvAjHwuwdulPUam3V0YgX9N5a2FL0uqz_R8xWpWSxDv9wLowG_f7it4Cn_9QDa0kA4-h-BpT-mvxTlhwf0uhWtUezZlH55nbcnPlHdldlmGQGUR7qeQsMIYe1pUDJWuRoYXYi4lYs0uKf-Y_KpYu94zPfQao4g0CykDoIizdtkG3k1cMhFu7lmqehnuDgkzIOXPbR81uiPHzeJGgdi6kxGvdgxRtAot3uVkZeiBVgfnzKtW548zA9Jt_bEUkCTFKOTvtCg3nQzxlb_2CWazfItH1le6tyXAYDHA8VWAHOcQpL-4i_ynVXc-yEOUV5evtoGImcNYNfeDYn4mkjXvOr4lhUTgeYipfLwIHzL-qZoo8DH-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9805bc1a1e.mp4?token=d6NyCtDZ5-04pF4NDJbVdthbiQaolDmSGn0EI3s8yxihih5VpmP5QqIrB6BDChXy9kkWZnqPhd6dpk95mjwBPB4y3z1GBzjUAYHsdNyDsjBWLfPU1LhzqOrB6xhPmCqJm6UnM5c3TZdTKU9fYwoB5sjFQmvt527m2i2Cn_dy_I4N81-68zUW3WxK8yosIq20S-SFI3B15YIKp1af9zDUJFtjUCeVl25GVL9KyhOH9OpZdberBwp_TR7oHLHwhoZUrzTyvmx0izE1QFHVYAGpkr7sf1mo_-HCuEMIh0RIr3WDma2ip7-upw1VJI_zvAjHwuwdulPUam3V0YgX9N5a2FL0uqz_R8xWpWSxDv9wLowG_f7it4Cn_9QDa0kA4-h-BpT-mvxTlhwf0uhWtUezZlH55nbcnPlHdldlmGQGUR7qeQsMIYe1pUDJWuRoYXYi4lYs0uKf-Y_KpYu94zPfQao4g0CykDoIizdtkG3k1cMhFu7lmqehnuDgkzIOXPbR81uiPHzeJGgdi6kxGvdgxRtAot3uVkZeiBVgfnzKtW548zA9Jt_bEUkCTFKOTvtCg3nQzxlb_2CWazfItH1le6tyXAYDHA8VWAHOcQpL-4i_ynVXc-yEOUV5evtoGImcNYNfeDYn4mkjXvOr4lhUTgeYipfLwIHzL-qZoo8DH-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیدمجید موسوی، فرمانده هوافضای سپاه: شهید محمود باقری زمینه‌ساز عملیات وعده صادق ۳ بود/ سالیان سال بچه‌های موشکی در حال آماده‌باش بودند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/659023" target="_blank">📅 16:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659022">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
بقائی: تفاهم نامه اسلام آباد بر خاتمه جنگ تمرکز دارد
سخنگوی وزارت خارجه:
🔹
تفاهم‌نامه اسلام‌آباد، توافق نهایی بین ایران و آمریکا نیست، بلکه تفاهمی است که رئوس کلی مباحث اختلافی را مطرح کرده و مشخص می‌کند که
جنگ خاتمه خواهد یافت.
🔹
موضوعاتی مانند امنیت کشتیرانی ایران و تنگه هرمز در مذاکرات مطرح است.
🔹
زمان امضای این تفاهم‌نامه هنوز قطعی نیست؛ اگرچه فردا انجام نمی‌شود، اما احتمال امضای آن در روزهای آینده وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/659022" target="_blank">📅 16:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659021">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
فقط ضروری‌ها ویزا گرفتند
🔹
وزارت امور خارجه آمریکا مدعی شد که «برای افراد ضروری» از جمله بازیکنان و کادر پشتیانی تیم ملی فوتبال ایران ویزای این کشور صادر شده است. #جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/659021" target="_blank">📅 16:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659020">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chBCl6lG4yB_hJ6ISgs8O_Lvz-FRf3P9pd0Vm-_H5PbEck1jlYvY4G2NkhK8FPni3yF7d3n-afNsQrbthCA1mo3OGhVC0ppVjF-OsU1Hvz7EM2smsqoiahCLQ4INhzCSr7dsQqEu1JqCQaBLT-k1EKcQUBwAHERynoSAv8YoHCTV7GfUQ5A3Z5N5FGj31tnXO4Foqjwqu48kF-zXEilGwt0lltcDE8DvTteY2ukNOhsSGUbr0LSOVrNfpL_E_6NmUsDwO1TV9qpVmupxMnh4poBLLSPiUO6miEg-QKo_KPnfk6c6Q4_Qv7DxbhPEEQQUCTBfG_uZuLAqMc-6oWalnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بزرگ‌ترین مسجدهای جهان کدام‌اند؟ حرم امام رضا (ع) در رتبه سوم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/659020" target="_blank">📅 16:12 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
