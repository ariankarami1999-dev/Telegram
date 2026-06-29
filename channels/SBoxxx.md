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
<img src="https://cdn4.telesco.pe/file/Ctp2En3OqmEurcq8wiGfz-A1eUJzGFzXVjuLF0Zw2FOzHqBYKlqN4oT2_dznpai22RkQ2hzgImr8kFQywq-TzCiEMjAJLYivYUA2ItBSqIVQ1ecK5V7kQtp2LCRJfrtkuv68Qtnsu4Q0dTzJX-fABvRlkNGcnkiJVA9rCAZklOBVq6lpblTpdc3Z81hqbBciKvx9noHge_slH5tkkobeEZHRF9O5SEuTZRPiHX12bWdA9xskG_ixfqg_aRax-xxGN08F7DEaqclCWVFLlhGqTPGa3hnhbuyUgo1tu8zHCcK1s4-sk8NoOiBVvuSjSytb71gYiugKs67gsJviWOd52g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 22:51:11</div>
<hr>

<div class="tg-post" id="msg-18107">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5YeOBP5HPkAasKtzgXRMe9KqAEixTvbztEeGncHAxtqT9R4UXiTWDmMavUAm0t78ErefC784DXW_cbEG1kAjCF6_rfx_5wnQnZ--8FwSvnO7n2gLIxjw_BbU1ZcfmUGlgWbNAXtrvwVQKcA6mqYlRE54ZpuLmOyGL8vkSLsgIuUfxJe9-pA2O7Lec5u9FHZIGlQSjWgYOmTrf4RD81JexFRz4eO5OlABZCfIFSpTIFSVPdPPijgrr_78hyrmUBpnDWA3HW2rcA1H-ZKlRI-BjFqi6Zb2k6zfbFMfZe7D_gc0DwCfm9G9_kyjZYwidV5Yj7adurCBCTHY6oOxZv3wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم خان امشب اساسی رو بای نفت است</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SBoxxx/18107" target="_blank">📅 21:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18106">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">معاون وزیر خارجه ایران غریب آبادی:
ایران تلاش خواهد کرد تا عبور هرگونه کشتی‌ای که از مسیرهای غیرتعیین‌شده توسط تهران در تنگه هرمز عبور می‌کند، را مختل کند</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/SBoxxx/18106" target="_blank">📅 21:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18105">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مکارم شیرازی در دیدار با پزشکیان:
اگر بدخواهان مانع‌تراشی نکنند، توافقات اخیر می‌تواند آثار مثبتی برای کشور داشته باشد.</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SBoxxx/18105" target="_blank">📅 20:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18104">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLfMpxpb5IrntqsnX33tDbf6G9bZLTVtpGZ9RGHtJIcCIXFfcXQ1dLrvFjJS1kYVJRSZFHlqPVFIganfPeEPEO41_RO7_nJ6Zhu5ogaGUjYhH38tcYJFLxzeRNCRMdvrFfoXtOWqjOoEiyOI0rCHnanB5a-kt9StFOpvGvnEX-1l_EMo_1LlIUhjOSOGzUufbjjD-jT-m-TC3j8fMR8F4ugZRXCBXg5099WKi1XfwpmdIxYO5KctN3hXxI0Sji77Li2hh6vDvKzFjkYUKUBQSo23iMs0X_QnrbXxQOtwMmgE60atF0jy7aQrvMycg3rO5veZFIYaH-XvPJv484MEfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:   «من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/18104" target="_blank">📅 20:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18103">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ایران می‌گوید برنامه‌ای برای گفت‌وگوهای مستقیم با ایالات متحده در این هفته وجود ندارد، با وجود ادعاهای مقامات آمریکایی.</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/18103" target="_blank">📅 19:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18102">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:   «من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/18102" target="_blank">📅 19:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18101">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:   «من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/18101" target="_blank">📅 19:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18100">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:
«من به نیروهای دفاعی اسرائیل دستور دادم برای عملیات «آبی و سفید» در ایران آماده شوند، نیروهای دفاعی اسرائیل فقط منتظر آن هستند.»</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/18100" target="_blank">📅 19:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18099">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بوی یک حمله همه جانبه به نیروهای موسوم به محور مقاومت می آید:  — حمله پلیس عراق به منازل عناصر سیاسی نزدیک به ایران — ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی — توافق دولت لبنان و اسرائیل برای پایان حیات نظامی حزب الله — آماده شدن نیروهای مخالف حوثی ها…</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/18099" target="_blank">📅 19:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18098">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بوی یک حمله همه جانبه به نیروهای موسوم به محور مقاومت می آید:
— حمله پلیس عراق به منازل عناصر سیاسی نزدیک به ایران
— ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی
— توافق دولت لبنان و اسرائیل برای پایان حیات نظامی حزب الله
— آماده شدن نیروهای مخالف حوثی ها در یمن برای حمله به انصارالله</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SBoxxx/18098" target="_blank">📅 19:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18097">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نه بازنگردانید چون غریب‌آبادی، ادعای ترامپ درباره جلسات فنی برنامه‌ریزی‌شده آمریکا در این هفته را رد کرد</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/18097" target="_blank">📅 18:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18096">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ادای تنگ ها را درنیاورید و بگذارید رستم بخسبد</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/18096" target="_blank">📅 18:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18095">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نه بازنگردانید چون غریب‌آبادی، ادعای ترامپ درباره جلسات فنی برنامه‌ریزی‌شده آمریکا در این هفته را رد کرد</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/18095" target="_blank">📅 18:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18094">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نه بازنگردانید چون غریب‌آبادی، ادعای ترامپ درباره جلسات فنی برنامه‌ریزی‌شده آمریکا در این هفته را رد کرد</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/18094" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18093">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رستم را به زابلستان بازگردانید!  ترامپ گفت ایران درخواست دیدار حضوری در دوحه داده است!</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/18093" target="_blank">📅 17:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18092">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUAFKypfFwYJAJ0munQ77G4DZa3iQC9bAfvppAcM1WUlDmlG5v9S1How2CGob4PsYKHX3T_PgP0X78wSjURvvlWOyggTZiM3ucNMIMXG1KWCr6PyPW2NLV828Di50R9zdGcD7Zd4kTNj41qbasSdT5NLdnBEAUClcdH_N-FGZj9gFTt3VyCIu_5-6q8-C_XwG54zld4oyXr0gY5KMfFnj0ViFrOsf_hDyA_6zXEDKY-lgSmBO9oaYQGKVPQKswlIHbAoFMu1iPM6vA-6OySAgcP17vlg_HiIMQFQ52hqq9Id22sOfJNqakYwJTzcNXEdvznIvuH9qsvnGaDHsTgxig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طنز بانکداری ایران  به دلیل حملات سایبری به دیتابیس بانک مرکزی شما به پولتان دسترسی ندارید ،اما بانک بابت اقساط به پول شما دسترسی دارد.</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/18092" target="_blank">📅 15:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18091">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEX8tB0NM0oUs6WSMSAaqbFTkLkvBnyjp2uAO7IFfNf2Zss9TYiOj-eKMJJ6FeEClgBNrv5zT1tAQCiMexwC5DMMRpm-MfORxyqZqAM8ybogMm26gIT4V9eiRG1g6Tdj2v83uFiGBRxjalnXXetJ3MYnrHiRpYjHxXcqG0AY8EJVWOnzvL7W7SaPX7SckBFELKbCRtN0CFXKU3mvAAAK1fq9rzOthjJ9F_ixRDzlKbX0temL31_zJ4Tzt0kVq59nSRo0SZ9tGYcDsS_hZTUbqEHNMCEJABGU9L6FWdE6ChQKlPQBVdN1IxEkmEHkrzekR6hVsCJ_ntZWTVpWM2XvPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینطور که بویش می آید بایستی بزودی رستم تهمتن را دوباره فراخوان کنیم.  فقط فکر کنم عینکی شده باشد که ولی خب.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/18091" target="_blank">📅 15:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18090">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ایران: هیچ گفتگوی فنی با آمریکا برای این هفته برنامه‌ریزی نشده است - تسنیم</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/18090" target="_blank">📅 14:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18089">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXlMlpikNVhFzd9IxQVG0fv8giFb7w-AgOlcfPjTEo6ZVsb6s9-tqhLJAQluPH6KRbj5FvA5I3P6tznS-UVCfZ261J1776kWHm9EpPLzjkt7AXG98bfhMnhO2Qq-TdvLL0NkTnfI-iaRpBKYVadOu5Z491Fg2dejr9vf5IMZ7n0XAjD21xoKxzTOvDbZsV6zaoMSZ0DwRdo_uhSoXS5XVVm7puHD8LYCqxoBNZ6VUX9UdP8ZXonUsSEJodKpeg0WoIE8Io7zU2vhnHR6Bu7IujZjSn4sIiLl5iflQK97riDb0Lkd35aVQNbSgj7I9ZqQtJRIibzaOBaVsFnK8kVyJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت اسرائیل پهپاد به شهرک نشینان در کرانه باختری اشغالی ارائه می‌دهد!
منابع محلی می‌گویند که پهپادها برای پرواز در ارتفاع پایین بر روی چوپانان و کشاورزان فلسطینی استفاده می‌شوند تا دام‌ها را پراکنده کنند، فلسطینی ها را بترسانند و اطلاعات جمع‌آوری کنند.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/18089" target="_blank">📅 14:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18088">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ایران: هیچ گفتگوی فنی با آمریکا برای این هفته برنامه‌ریزی نشده است - تسنیم</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/18088" target="_blank">📅 13:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18087">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الهام فعلا استراتژی مالش را آغاز کرده تا مثلا خود را در دل آمریکایی‌ها جا کند، غافل از اینکه ارمنستان با چرخشی عظیم به سوی غرب، در دلبری از واشنگتن و تل آویو ، گوی سبقت از باکو خواهدربود.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/18087" target="_blank">📅 11:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18086">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هیچ حمله سایبری در کار نیست.  MV = PQ  وقتی M را با چاپ پول برده ای بالا و از آن سو Q هم اگر افتی نکرده باشد دستکم رشدی هم نکرده، قیمت ها یعنی P باید منفجر بشود. پس تنها راهی که داری این است که از سرعت گردش پول یعنی V بکاهی و آن را بندازی گردن اسراییل و نت…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18086" target="_blank">📅 11:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18085">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X42_-1GEbboDxj-j8y0DH15weDBC0D4U1-kUxOukfP-38zh_9YvKnbgHuFyrRx4rRnUcqZkF2wcrJNxQOQE1i1SrR27kPWBgLtBdk2g7zuo79GzxVgIAtxsdNRwrLu_rAhNoyA1jjRMvF07_xPqwRB4GcDtxUOpBjdDxvtSBEv4feL6D9P4S4AxF7RJBlbimyIS_DkhOvEFSzWsEsqTeZEjte3vbBIPZxT2RIHyOo9o7XNR_l7G_whzDCQw3qeMe1J7ZzNWdJ0V6lSyQId8bQeCD0UpvYAqBeTMUPbx9CMZ6imfC5FyePbEA5LxoVvFw6d_HiWE5-huO22tyGCrzwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا رقابت هوش مصنوعی میان آمریکا و چین این‌قدر سروصدا کرده است؟
رقابت هوش مصنوعی آمریکا و چین فقط رقابت فناوری نیست؛ هم‌زمان رقابت بر سر ارزش بازار، سودآوری، امنیت ملی و برتری ژئوپولیتیکی است و هر جهش جدید می‌تواند انتظارات سرمایه‌گذاران و موازنه قدرت جهانی را تغییر دهد.
مدل‌های ارزان و باز چینی در کنار جنگ تراشه و محدودیت‌های صادراتی آمریکا، معادله اقتصادی هوش مصنوعی را تغییر داده‌اند و ابهام درباره فاصله واقعی دو طرف، به مهم‌ترین سوخت این هیاهوی جهانی تبدیل شده است.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/18085" target="_blank">📅 11:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18084">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nu-m_zVRloyKqXSI3iM6hAKTACxeYwiKQsOb_DX__X1qwlrpPFFfxTUWEkREabMXiz82f-yuGcwvoZvSr569atmU1_97pT5K9ozyjHxLQwQZwO5SOGEWAAQfTeGLZMVkZ_kfKWk3QPO1XiOXe9fGExjq7xkfk_G0kRNPbqjKfHX2JX9T88gg2Iyv5ajjjRPB2jxZEwRfI2oIH_Pw6_plsWH5oVug_7ebxWpIxsP4tFgATyT9fQzNWK2VsgbH7IE1W_SaVtfZWPSRRLvcNWbyLkgj8Gv-q_ZkfakadW2UcCRhraEe1zgWhWUzPldsXkyMJt-oo3WURjV_eHiQYq5CYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم عبور کشتی‌ها از تنگه هرمز به طور قابل توجهی با ترافیک سال گذشته متفاوت است.
پورت‌واچ آمار جدیدی درباره ترافیک کشتی‌رانی در تنگه هرمز منتشر کرده است. در ژوئن ۲۰۲۶، ۵۰ نفتکش و ۴۰ کانتینر عبور کردند در حالی که در دسامبر ۲۰۲۵، ۱۱۵۰ نفتکش و ۴۰۰ کانتینر ثبت شده بود.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18084" target="_blank">📅 01:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18083">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حمله سنگین اسرائیل به منطقه "مجدل زون" تو جنوب لبنان</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18083" target="_blank">📅 01:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18082">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آکسیوس با استناد به مقامات آمریکایی  ایالات متحده و ایران توافق کردند حملات را متوقف کنند و گفتگوها را در این هفته برنامه‌ریزی کنند</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18082" target="_blank">📅 00:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18081">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترور یک عنصر ازبک در سوریه  بنا بر گزارش منابع محلی یک عنصر ازبک با نام خالد الجزراوی روز گذشته روبه‌روی منزلش در الفوعه در حومه‌ی ادلب توسط افراد ناشناس ترور شد.  برخی منابع محلی این ترور را به داعش منتسب کردند، این در حالی‌است که داعش هنوز مسئولیت انجام…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18081" target="_blank">📅 00:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18080">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترور یک عنصر ازبک در سوریه
بنا بر گزارش منابع محلی یک عنصر ازبک با نام خالد الجزراوی روز گذشته روبه‌روی منزلش در الفوعه در حومه‌ی ادلب توسط افراد ناشناس ترور شد.
برخی منابع محلی این ترور را به داعش منتسب کردند، این در حالی‌است که داعش هنوز مسئولیت انجام این ترور را بر عهده نگرفته‌است
چندی پیش یک عنصر چچن با نام مصطفی الروسی از اعضای نیروی ویژه تحریر الشام موسوم به العصائب الحمراء نیز ترور شده‌بود.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18080" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18079">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18079" target="_blank">📅 00:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18078">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آکسیوس با استناد به مقامات آمریکایی
ایالات متحده و ایران توافق کردند حملات را متوقف کنند و گفتگوها را در این هفته برنامه‌ریزی کنند</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18078" target="_blank">📅 00:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18077">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وزیر علوم و فناوری  اسراییل، گیلا گملیئل:   وقتی که از رژیم ایران عبور کنیم، نوبت به جاه‌طلبی‌های امپراتوری عثمانی می‌رسد که به دنبال گسترش و نفوذ خود است. شکی نیست که ترکیه با آرزوهای گسترش فراتر از مرزهای خود و رهبری منطقه بر اساس دیدگاه خود، تهدید واقعی…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18077" target="_blank">📅 19:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18076">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVuo3EqEF5NF513J8Dn1r7-IFBw_AUX2u03JmQVp7UvaUd2rANIbjRzoVlcNtExv1CzdJCjJNiytpQt6Wavo_3wSyKpVwkLBTAPWXCO0scL5brHD664Qg3iU0hWA_CwqRVzhgatFAdh2dqoNF2lzt-j13cUVJNASj_Um7SDrHFILVP2LaoH7jf71xMPJXfov-Mtbi-htvjTcLRNf-_87lLAxx7eLrbSCZY8QXlwvdNm5NHJzwzlFIfRCXoQztgthwMGB4NQg2mPCZu5UbAOIBTXGXrLJ--V3DASkluVz293Br0EWGLDT__SL1U4pFT8bLzxtOEbxPB9LP3qHpiJFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا شاخص سهام کره جنوبی در روزهای اخیر ریخت؟
ریزش اخیر کاسپی بیشتر از اینکه نشانه ضعف اقتصاد کره باشد، نتیجه هم‌زمان فشار روی سهام نیمه‌رسانا، نگرانی از تداوم نرخ‌های بالای آمریکا و خروج سرمایه از بازار بود؛ بازاری که وابستگی زیادی به سامسونگ و SK Hynix دارد.
با وجود شدت افت، کاسپی هنوز فاصله زیادی با سناریوی «ترکیدن حباب» دارد و سؤال اصلی بازار این است: آیا چرخه رشد نیمه‌رساناها ادامه پیدا می‌کند یا قیمت‌گذاری این صنعت زودتر از انتظار به سقف رسیده است؟
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18076" target="_blank">📅 16:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18075">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">هندی ها جوری هستند که یکی شان میخواسته از بانک پولی بگیرد به او گفته اند برو گواهی فوت خانمت بیاور و نداشته؛ رفته جنازه زنش را از قبر کشیده بیرون کول کرده برده بانک که پولش را بگیرد!  حالا شما فکر کنید بین شمال تنگه که پولی است با جنوب تنگه که صلواتی است کدام…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18075" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18074">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وزیر انرژی اسرائیل، الی کوهن، می‌گوید دولت جدید اسلوونی به رسمیت شناختن فلسطین را لغو کرده و سفارت خود را به اورشلیم منتقل خواهد کرد.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18074" target="_blank">📅 14:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18073">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بحرین می‌گوید حمله ایران به ساختمان مسکونی آسیب زده است، تلفات جانی نداشته است</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18073" target="_blank">📅 14:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18072">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b2ebb26.mp4?token=aob24XFaLca9GV2AsdVju8sDuRr0cNcaat7qOpeWU0sMiIIkU3cL3n0_9SaltGXfRWEr16mJfv3shy8czzz48L2ZSKTF0IMN3AbETPnrCjCwA438dNKXBLw4h8Jy_wq1el1GeqNjFHOxydQ9gLTRBRm94Jmp3mgmE8HxsBXjPghiDU-cIYPu0-ZQCJN466D2SCtlsQoKUL_vysFSwCLpD1v7WuTSoYRVmB9bsf_hdEMdv03X0Ns5Ws1EtBMoz8GSRr9y1y03GIsJNoxCt3FnPPvQPES4TwVq6FHpQ3KqxME0KnWykRd4o7saLVK_C7YJ0oNAKaWnnjYAy50cC5QKKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b2ebb26.mp4?token=aob24XFaLca9GV2AsdVju8sDuRr0cNcaat7qOpeWU0sMiIIkU3cL3n0_9SaltGXfRWEr16mJfv3shy8czzz48L2ZSKTF0IMN3AbETPnrCjCwA438dNKXBLw4h8Jy_wq1el1GeqNjFHOxydQ9gLTRBRm94Jmp3mgmE8HxsBXjPghiDU-cIYPu0-ZQCJN466D2SCtlsQoKUL_vysFSwCLpD1v7WuTSoYRVmB9bsf_hdEMdv03X0Ns5Ws1EtBMoz8GSRr9y1y03GIsJNoxCt3FnPPvQPES4TwVq6FHpQ3KqxME0KnWykRd4o7saLVK_C7YJ0oNAKaWnnjYAy50cC5QKKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی نجاسات الجزایری پس از خوردن گل تساوی تیمشان از اتریش که باعث شد تا در مرحله حذفی به اسپانیا نخورند!
بعد پروفسور جمشید خیابانی به عربی از این نکبتها درخواست بازی شرافتمندانه داشت!
حق شما همان گیوتین فرانسوی بود و بس!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18072" target="_blank">📅 13:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18071">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">این توافق اساساً نوع مهندسی و طراحی اش به گونه ای است که هیچ وقت به صورت آشکار منجر به حل کامل و قاطع اختلافات نشود. عمداً بخش های زیادی به صورت خاکستری و ابرآلود باقی نگاه داشته شده تا همیشه بهانه ای بر زدن زیر میز وجود داشته باشد.  عین بلایی که سر ما تریدرها…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18071" target="_blank">📅 10:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18070">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خدماتمان اینطوری است که کشتی هندی با ملوانان بنگلادشی متعلق به میلیاردر یونانی دارد راهش را می رود، بچه های ما به کاپیتان آن زنگ می زنند که یا بیا از نزدیکی سواحل ما رد شو یا ما ترتیبت را می دهیم بعد کشتی وارد آب های ما می شود و ما اسکورتش می کنیم تا بچه های…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18070" target="_blank">📅 08:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18069">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5daefe620.mp4?token=JDzSblnu3yOFa_SoKZ7ibj1w5FurAA-kzMZ43hYhCoVc987J-Rhc2LbAvJcw6GzCr7BvHo9VZBfjx0KncI7ujO_UZMWQ1cN9nLo3s20EZzK3X8BGQ1mSVaaFDvqVVGdZtVa9k0PC2bvsWWpdlzJVUtr4Zy08nRB2aNPwNZnrHeDh5CPVrWyDzgMlu1WUqw03qg-ZUanLcB9f5O1IuGq20HJiw7iVxXbAm9RUNDQ9v-nA3sBvUjVAailFN0ycDOv4xPPiDVAXyDQ2yJew9UxnAJ4xnUFYuBXjQYCXrto317X4lLrGXQ0rW474kqHm8nONgmihgKfxOL8OPuFee5woOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5daefe620.mp4?token=JDzSblnu3yOFa_SoKZ7ibj1w5FurAA-kzMZ43hYhCoVc987J-Rhc2LbAvJcw6GzCr7BvHo9VZBfjx0KncI7ujO_UZMWQ1cN9nLo3s20EZzK3X8BGQ1mSVaaFDvqVVGdZtVa9k0PC2bvsWWpdlzJVUtr4Zy08nRB2aNPwNZnrHeDh5CPVrWyDzgMlu1WUqw03qg-ZUanLcB9f5O1IuGq20HJiw7iVxXbAm9RUNDQ9v-nA3sBvUjVAailFN0ycDOv4xPPiDVAXyDQ2yJew9UxnAJ4xnUFYuBXjQYCXrto317X4lLrGXQ0rW474kqHm8nONgmihgKfxOL8OPuFee5woOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در واقع دارند می‌گویند از مسیر عمانی ها نروید چون اینقدر خطرناک است که ممکن است ما بزنیم تان!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18069" target="_blank">📅 08:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18068">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گزارشگر صداوسیما یک دقیقه قبل از حذف ایران از جام جهانی:
یک کشور مسلمان، کاری کرد تا کشور مسلمان دیگری صعود کند!</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18068" target="_blank">📅 08:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18067">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شبکه ۳ بعد فوتبال یک روحانی  را آورده او هم آفتابه را گرفته روی همتی که چرا گفتی از دشمن گندم وارد کنیم مگر گندم تراریخته نشنیدی!</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18067" target="_blank">📅 07:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18066">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وقوع انفجارهای جدید در کویت و بحرین
هم‌زمان با انتشار گزارش‌هایی از وقوع انفجار در بحرین و کویت، وزارت کشور بحرین از فعال شدن آژیرهای هشدار و درخواست از شهروندان و ساکنان برای مراجعه به نزدیک‌ترین مکان امن خبر داد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18066" target="_blank">📅 07:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18065">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عراق عملیات گسترده ای را علیه سیاستمداران عراقی وفادار به ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18065" target="_blank">📅 06:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18064">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تحلیل همین است.   این مواردی که خبرگزاری مهر گفته هنوز تایید نشده.  پاشنه آشیل توافق هم بند مربوط به لبنان است</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18064" target="_blank">📅 06:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18063">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ
:
هواپیما های ایالات متحده بار دیگر ایران را بمباران کردند چرا که بازهم آتش‌بس را نقض کرده بود.
احتمال دارد زمانی برسد که دیگر نتوانیم منطقی باشیم و مجبور باشیم آنچه به صورت بسیار موفق شروع کردیم به صورت نظامی به پایان برسانیم. در این صورت دیگر جمهوری اسلامی ایران وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18063" target="_blank">📅 06:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18062">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏
نیروی دریایی سپاه: آمریکایی‌ها جهنم را در این روزها تجربه خواهند کرد
فرماندهی نیروی دریایی سپاه:
شلیک‌های کور آمریکا به سیریک معمای اشراف ما بر تنگه را حل نمی‌کند. اما شلیک‌های ما به متخلفین، راه روشن عبور را به باقی شناورها یادآوری می‌کند.
حساب پایگاه‌های آمریکایی منطقه جداست. جهنم را در این روزها تجربه خواهند کرد.
‎</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18062" target="_blank">📅 06:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18061">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گویا صدای انفجارهایی در بندر لنگه و قشم نیز شنیده شده</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18061" target="_blank">📅 01:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18060">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بیانیه سنتکام:
«پس از حملات دیروز ایالات متحده در پاسخ به حمله ایران به کشتی M/V Ever Lovely، به ایران فرصتی داده شد تا توافق آتش‌بس را رعایت کند، اما وقتی نیروهای آن در ساعت ۴:۳۰ صبح به وقت شرقی امروز با پرتاب یک پهپاد یک‌طرفه به کشتی M/T Kiku حمله کردند، این فرصت از میان رفت. این نفتکش پرچم پاناما در حال عبور از نزدیکی تنگه هرمز بود و بیش از ۲ میلیون بشکه نفت خام حمل می‌کرد.
نیروهای فرماندهی مرکزی امروز در پاسخ مستقیم به تداوم تهاجم ایران علیه کشتیرانی تجاری، حملاتی را آغاز کردند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی نظامی ایران، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات نگهداری پهپادها و قابلیت‌های مین‌گذاری را هدف قرار دادند».</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18060" target="_blank">📅 01:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18059">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یک منبع نظامی ایرانی به صداوسیما گفت:
«صداهای انفجار شنیده شده مربوط به برخورد چندین پرتابه به برج مخابراتی در سیرک است».</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18059" target="_blank">📅 01:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18058">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18058" target="_blank">📅 01:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18057">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی به سمت کشتی‌های متخلف در تنگه هرمز تیرهای هشداردهنده شلیک کرد. صدای انفجارهای شنیده شده در شهرستان سیریک و جزیره قشم در استان هرمزگان به این علت بوده است.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18057" target="_blank">📅 01:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18056">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارش‌های اولیه از حملات هوایی آمریکا به جنوب ایران.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18056" target="_blank">📅 01:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18055">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مجلس خبرگان رهبری بیانیه داد:  باز کردن تنگه هرمز ممنوع است و هرکسی که به ترامپ و نتانیاهو دسترسی پیدا کند، بر او واجب است که آن‌ها را بکشد. ﻿حاکمیت ایران باید بر تنگه هرمز اعمال شده و از طریق آن عوارض دریافت شود تا خسارات وارده بر کشور بازسازی شوند. ﻿</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18055" target="_blank">📅 23:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18054">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e39aee93e2.mp4?token=l_sV72fgk_x-S-iAeQWW7betkbIjIg741Guyoj67-TOYwI-UNkDge4Q2VTcyxugLFwgKepG1YYw1BFXzu5O8hBrdYWZN4FvYmL9a8co_92UqHid5dQiESMMOxuwg0jUElEetojIj7_sGJFvnmPunVbWPOz7xQTZrmGvY8nYy_p6W_e7dHJkTfVjcn6daB5Icud9724lA6lFN1Je1sRiSlWmRQgcgFyeaUy-ROZ0v6l0mzFyAbGuIh4BUaXulLYf3FBzQAaqK4WyQa5_e8HlGgsB7uexCo7HT8ILy5rSMf5BtzA6F9Y0-GGIuRzOheAQTQeIKrUpJwW-FeJnTwGIImIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e39aee93e2.mp4?token=l_sV72fgk_x-S-iAeQWW7betkbIjIg741Guyoj67-TOYwI-UNkDge4Q2VTcyxugLFwgKepG1YYw1BFXzu5O8hBrdYWZN4FvYmL9a8co_92UqHid5dQiESMMOxuwg0jUElEetojIj7_sGJFvnmPunVbWPOz7xQTZrmGvY8nYy_p6W_e7dHJkTfVjcn6daB5Icud9724lA6lFN1Je1sRiSlWmRQgcgFyeaUy-ROZ0v6l0mzFyAbGuIh4BUaXulLYf3FBzQAaqK4WyQa5_e8HlGgsB7uexCo7HT8ILy5rSMf5BtzA6F9Y0-GGIuRzOheAQTQeIKrUpJwW-FeJnTwGIImIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داشتم به این فکر می کردم که ویدیوی التماس جواد خیابانی به الجزایر برای مساوی نکردن با اتریش را دیدم!  یعنی هر چه شما می خواهید به خودتان بقبولانید که دیگر به نوک قله فلاکت رسیده ایم و دیگر  تپه ای برای ریدن نمانده یک دفعه می بینید یک کصخلی پیدا می شود تا به…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18054" target="_blank">📅 23:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18053">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مدیرعامل شرکت خدمات انفورماتیک:   تلاش می‌کنیم اختلال بانک‌های ملی و صادرات تا پایان وقت امشب برطرف شود</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18053" target="_blank">📅 23:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18052">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الجزیره: اختلاف تهران واشنگتن بر سر تنگه هرمز بالا گرفت   اکنون شاهد آن هستیم که ایران و ایالات متحده در تفسیر مفاد یادداشت تفاهم با یکدیگر اختلاف دارند؛ اختلافی که به‌طور فزاینده تنگه هرمز را به اصلی‌ترین نقطه اختلاف میان دو طرف تبدیل کرده است.   دو بیانیه…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18052" target="_blank">📅 23:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18051">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">به نظرم در شان ابرقدرت چهارم دنیا نیست که اینطور بانک هایش فلج باشند.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18051" target="_blank">📅 23:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18050">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هیچ حمله سایبری در کار نیست.  MV = PQ  وقتی M را با چاپ پول برده ای بالا و از آن سو Q هم اگر افتی نکرده باشد دستکم رشدی هم نکرده، قیمت ها یعنی P باید منفجر بشود. پس تنها راهی که داری این است که از سرعت گردش پول یعنی V بکاهی و آن را بندازی گردن اسراییل و نت…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18050" target="_blank">📅 22:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18049">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این توافق اساساً نوع مهندسی و طراحی اش به گونه ای است که هیچ وقت به صورت آشکار منجر به حل کامل و قاطع اختلافات نشود. عمداً بخش های زیادی به صورت خاکستری و ابرآلود باقی نگاه داشته شده تا همیشه بهانه ای بر زدن زیر میز وجود داشته باشد.
عین بلایی که سر ما تریدرها آورده شد که آخر هم نفهمیدم ترید فارکس قانونی است یا نه! عمداً فضا را خاکستری کردند — نه آزاد نه ممنوع — تا هر وقت بخواهند باج بگیرند و هر وقت خواستند رها کنند و هر وقت خواستند بزنند و ببندند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18049" target="_blank">📅 21:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18048">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الجزیره: اختلاف تهران واشنگتن بر سر تنگه هرمز بالا گرفت
اکنون شاهد آن هستیم که ایران و ایالات متحده در تفسیر مفاد یادداشت تفاهم با یکدیگر اختلاف دارند؛ اختلافی که به‌طور فزاینده تنگه هرمز را به اصلی‌ترین نقطه اختلاف میان دو طرف تبدیل کرده است.
دو بیانیه اخیر ازجمله بیانیه سپاه مبنی بر نقض ماده ۵ یادداشت تفاهم درباره بازگشایی تنگه هرمز و همچنین بیانیه وزارت خارجه مبنی بر نقض ماده ۱ یادداشت تفاهم درباره توقف فوری درگیری‌ها، شواهد این مدعا هستند.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18048" target="_blank">📅 21:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18047">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⛔️
دولت ترامپ ، دسترسی به 2 مدل هوش مصنوعی آنتروپیک را برای کاربران غیرآمریکایی مسدود کرد</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18047" target="_blank">📅 19:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18046">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyGdYmU4vEBuaEjasS2u9wNMH7sORYmAYWJsZtc4re76QfNKr1kBaxEdGXvGa0ZE0cc3pQxHKkfcQ6TleAw22O7Wfr6tHmlvy9QtBMRlDc3Z3A_hiG2tgQPDuNxuV_DL95FGEIjL0ia-BQ5tjy-69E1B-Z9SMGRKo5mowSYs-nsVRSK2Zh28UdzvPXV4IV47QNBBmeosfE4DeQW0rPza_rCB9AMckcaNKJsRYAr0088gFSGnlbflIepUxIfUeFIYC4nI5DhQWeuKfxZx2m0fsTLXzeZB26Wm7veMPskyVONtRiAAT6WF6if2yF8Y891MCi9y_ftj7E-uutC5hvh-kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شادی فلسطینی ها در غزه پس از گل مصر!  مصر برای اینها چه کرده؟!   دیوار کشیده تا از شهر موشها (غزه) به درون مصر سرازیر نشوند. یک بار هم ارتش مصر فاضلاب خود را به تونلهای حماس سرازیر کردند که باعث شد چند ده تن از اعضای حماس به دیدار خالد بن ولید بشتابند.  آن…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18046" target="_blank">📅 18:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18045">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dafd3cf871.mp4?token=QTeggEddq-TPHakzHZHYs142SsKI1cWZ31mKQMS9IFIKjDtqgjXmOF2HKUBE8hpsdDKVsA9DA-hFenNL7Fz4H6cTF-_xYiYsgmCU5Tk9z7LmxbLGvrn00zVv_NsdoV3MmD3EcZckpjirniJLyIefrhPOygQf03Ix58HiXCOG9s3cmB-_gBEJjryX48RBcXH7f_QNPCQSAtRVA4ovYTaIcgIDy25e_AdHyVsDsizmyDAMQAuox6i2YL2uz6LXDdKH8X_0IZapLbI1z3LzNbp4WJXnD7TFMI9jot5ChOMw7rD9DZR7gP-An0s4iN4BTtle1y6KTO98_JH6-a2QKTnC1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dafd3cf871.mp4?token=QTeggEddq-TPHakzHZHYs142SsKI1cWZ31mKQMS9IFIKjDtqgjXmOF2HKUBE8hpsdDKVsA9DA-hFenNL7Fz4H6cTF-_xYiYsgmCU5Tk9z7LmxbLGvrn00zVv_NsdoV3MmD3EcZckpjirniJLyIefrhPOygQf03Ix58HiXCOG9s3cmB-_gBEJjryX48RBcXH7f_QNPCQSAtRVA4ovYTaIcgIDy25e_AdHyVsDsizmyDAMQAuox6i2YL2uz6LXDdKH8X_0IZapLbI1z3LzNbp4WJXnD7TFMI9jot5ChOMw7rD9DZR7gP-An0s4iN4BTtle1y6KTO98_JH6-a2QKTnC1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی فلسطینی ها در غزه پس از گل مصر!
مصر برای اینها چه کرده؟!
دیوار کشیده تا از شهر موشها (غزه) به درون مصر سرازیر نشوند. یک بار هم ارتش مصر فاضلاب خود را به تونلهای حماس سرازیر کردند که باعث شد چند ده تن از اعضای حماس به دیدار خالد بن ولید بشتابند.
آن وقت هواداران جمهوری اسلامی، ژنده پارچه چرکین کشور خیالی فلسطین را با خود به ورزشگاه برده بودند و این هم جوابشان!</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/18045" target="_blank">📅 18:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18044">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">UKMTO:
گزارشی از یک حادثه در تنگه هرمز دریافت شده است.
کاپیتان نفتکش گزارش داده است که توسط یک پرتابه ناشناس مورد اصابت قرار گرفته است. این کشتی به پل فرماندهی خود آسیب دیده است؛ گزارش شده که همه خدمه سالم هستند. در حال حاضر هیچ خسارت زیست‌محیطی گزارش نشده است.
به کشتی‌ها توصیه می‌شود با احتیاط عبور کنند و هر فعالیت مشکوکی را به UKMTO گزارش دهند، مقامات در حال بررسی هستند».</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18044" target="_blank">📅 13:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18043">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رودان هم جز میتوانست جزو گزینه ها باشد که ولی خب.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18043" target="_blank">📅 13:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18042">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سبحان الله! با Secret Box روزنامه فردا صبح را داشته باشید.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18042" target="_blank">📅 13:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18041">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سبحان الله! با Secret Box روزنامه فردا صبح را داشته باشید.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18041" target="_blank">📅 12:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18040">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الان است که اربیل یا بحرین را بزنیم!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18040" target="_blank">📅 12:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18039">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الان است که اربیل یا بحرین را بزنیم!</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18039" target="_blank">📅 12:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18038">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aT_tLYkcd8qbKTy7tWDFG0uGUdO4OGx-y9WEJqyrVcCFGN79oubf4WJR5yoXVedeXiBqOJh6QqDGg5kMvT0W4yX_4Tk6ikjNWIheTMRIVVIGs4Gc8Jo7vX_g7qUxgJuffvib4AlODlELmFbMjJ67uY9zG-a71iRhauqMr3lYSmjroD44YtvanU4PjaiQs8rTfcxufwQ9EMKxlytau2RDYsFc74btAey6WqdFHzwvIumw-UO-x0pDFCnsNwKSndRZbfhHkRzPCdbnSewKkCSAtKnYHyAkx5lqH4Wo3jaQRjMkr2nzzcw_IlgIKXfB3JTAw__JTkXZ6eVCk73LSY_Z1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر نفتی آمریکا و جنگ با ایران
آمریکا از ذخایر راهبردی نفت به‌عنوان ابزاری برای مدیریت شوک‌های بازار و کنترل فشار انرژی استفاده کرده و کاهش اخیر این ذخایر باعث شده بازسازی آن‌ها به یکی از اولویت‌های مهم واشنگتن تبدیل شود.
برخی تحلیلگران معتقدند کاهش تنش در خاورمیانه می‌تواند علاوه بر اهداف سیاسی و امنیتی، فرصتی برای افت قیمت نفت و خرید مجدد نفت در سطوح پایین‌تر جهت تقویت ذخایر راهبردی آمریکا فراهم کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18038" target="_blank">📅 11:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18037">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLS9X-bybK9sHXkuBRK_IS9s6ZVuWNd4-T2xwtC4WC9B_s6DUyOdG1l6WJwl02iX7kvziT-l-F_M7aDoB3LGKCEa9eFeZ6rlnUbi9NhrWd2qMS0EBujrOkz6PT3q1zIcM00YGyUPikvqdXif-P9MkFqVkZiaQKgl9jFWePuUK2uhAGOci8y_bica-KcVnzbXFQES85rFlKNLA_LhAD4eovGaA_GVGaiCc9nbzanauPR_Jms-U1TAcmsyJrU1VoQS6TuVihXFBiO4i-_xKLTTBQPutaH6ynBvUr2vDXwXQ6FP5aOyS1woEZ8KDOJdSeCOp8RhLJWMF6MlWYzk4xuF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه بازی</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18037" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18036">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrRMFrP-JHCiGeFGfv35kK89kMvnNwfC6x5PQ8ehIr3j_sMQfEbxoGRXIsYz1edBd1WFM6g1XfSNJ2CPOeMHsEugxTjH3-Byib9vEg0Irnx6X3LzXeyXE_xX9ondObQY2EaN2952iUCkQuSqdVG2xJrQtoYy8S4vWR72ZQt4qLfqDD2jVIrIknTCDETb5OWdS6llIuW_fppPBEisvWNBgXjHf5r3atKr6lTibOL6KCnYprIG4lCyJjDoNR2iuxqzUGPu14VLHAUkPJSc_UrXw3S7rnSRi3IKu-wjxYAhB0RJp3EVJacA58TeKNWcXIGMlC0LsVDaVHPHp7xD17tL9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18036" target="_blank">📅 08:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18035">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر فارسی</strong></div>
<div class="tg-text">الان تو زمین بگی محمد‌ حداقل بیست نفر تو زمین و ده هزارنفر نفر تو تماشاچی‌ها برمیگردن‌ میگن جانم؟
• میرزا •
@OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18035" target="_blank">📅 07:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18034">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رسانه‌های دولتی ایران: سپاه پاسداران چندین پایگاه ارتش آمریکا در منطقه را هدف قرار دادند</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18034" target="_blank">📅 02:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18033">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رسانه‌های دولتی ایران: سپاه پاسداران چندین پایگاه ارتش آمریکا در منطقه را هدف قرار دادند</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18033" target="_blank">📅 02:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18032">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی مجلس ایران: ترامپ هیچ تعهدی به اصول مذاکره یا آتش‌بس نشان نداده است</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18032" target="_blank">📅 01:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18031">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">متن اعلامیه سنتکام:
حملات ایالات متحده به ایران در پاسخ به حمله به کشتی تجاری
تامپا، فلوریدا — به
عنوان پاسخی قوی به حمله دیروز به یک کشتی تجاری که در تنگه هرمز در حال عبور بود، نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در تاریخ ۲۶ ژوئن حملاتی را علیه ایران انجام دادند.
پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد حمله یک‌طرفه به کشتی M/V Ever Lovely حمله کرد، هواپیماهای آمریکایی به محل‌های ذخیره موشک و پهپادهای ایرانی و سایت‌های رادار ساحلی حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
این تجاوز بی‌دلیل علیه کشتی‌های تجاری توسط نیروهای ایرانی به وضوح آتش‌بس را نقض کرد. علاوه بر این، رفتار خطرناک ایران آزادی ناوبری را تضعیف کرد در حالی که تجارت به طور فزاینده‌ای از این گذرگاه حیاتی تجارت بین‌المللی عبور می‌کند.
نیروهای CENTCOM به ارائه هماهنگی و حمایت برای عبور ایمن کشتی‌های تجاری از تنگه ادامه می‌دهند. نیروهای نظامی ایالات متحده همچنان حضور دارند و هوشیارند تا اطمینان حاصل کنند که همه جنبه‌های توافق با ایران رعایت، اطاعت و به طور کامل اجرا می‌شود.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18031" target="_blank">📅 00:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18030">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حملات تروریستی گروه های تجزیه طلب به ایستگاه های مرزی در بانه</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18030" target="_blank">📅 00:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18029">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سنتکام   به دستور دونالد ترامپ و در جواب شکست آتش بس توسط جمهوری اسلامی عملیات محدود ما در ایران آغاز شد</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18029" target="_blank">📅 00:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18028">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7AIcW-JwH_cGardCnAZlcXD69_eAWNloVEho7ulYMotP1Qj02CqGEWrZfoWiZoXgTfwD3c2mhfCtuY1PHI5OI-CklCJZ7GOtDwhNjrREdKBn_3VWkQWQ7ajXVgfJY9DXb9MnaLsVQgUni2AwIUcN-sbvnQrkr_0OTIoIGKIFxx9j43ZbfLC1Efco_PSl8EFvzPJ7VNiixU4El8MGcFEN2PsO7WDq2vQJw-YDJC-lclS-4OhwAL1cmcbcm8jfZd2ETvtOhEWNDybTIGsmqSqrA6AdVvSPnX-CFMeApbtgzxMuHTUxDvHKqB4ePKEL1FW3XS5kJ6UJ938gZo-dBzHZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مثل ما نفت را خریده.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18028" target="_blank">📅 00:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18027">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الان است که اربیل یا بحرین را بزنیم!</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18027" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18026">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چادرملو! صد تبریک! / مردک نزن تو سیریک!</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18026" target="_blank">📅 00:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18025">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فعال شدن پدافند قم!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18025" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18024">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پزشکیان را آوردند که جنگ نشود؛ هر 36 ساعت یک بار جنگ داریم!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18024" target="_blank">📅 23:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18023">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">به نظرم بهترین پاسخ زدن رودان باشد؛
هم آتش بس نقض نمی شود هم به هر حال پاسخ داده ایم و هم دل جمع بزرگی از مالباختگان خنک خواهدشد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18023" target="_blank">📅 23:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18022">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkGCYeDXV5fgpjzKyRnekVNtDzR2gE8EIKY_jfGVn8kgCaY6DibX-_WVHoVo4pmHlCRD_zIA5ARzTrGZcW4bOfEAu8Dr996LeOHZKcKTcoRSrtmE_8nC8e2orkyl4ifImHrx4bcaoGUG5CHE-sE5uMqrw1wVFE86caY2IPaTk5Y-4psM_AqTyvIeWQebZwp8pLmvObRAmUUJIsKrBBrfKV1rTeRxVO20AyLFLTakYfW0hYyYVbLvLJ3BX4tiw3IWT02uTqX2HHuI2E97Ue7DNQ7_sqfwX2XS47Zlqz1tpOcYoQEi000Tkcu9giU-tedUMFMBaqUUPAHc9pjCDwlWAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایید حمله آمریکایی ها توسط یکی از همراهان باوفای Secret Box در بندرعباس!</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18022" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18021">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این مواضع ضد و نقیض تعریف همان موج کذایی 4 است.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18021" target="_blank">📅 23:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18020">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سنتکام
به دستور دونالد ترامپ و در جواب شکست آتش بس توسط جمهوری اسلامی عملیات محدود ما در ایران آغاز شد</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18020" target="_blank">📅 23:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18019">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ اشاره کرد که ارتش ایالات متحده ممکن است پس از نقض آتش بس توسط ایران با پرتاب پهپادهای تهاجمی به کشتی‌ها، با زور پاسخ دهد.  "خواهید فهمید! آیا من پاسخ خواهم داد؟ خواهید فهمید."</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18019" target="_blank">📅 23:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18018">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ اشاره کرد که ارتش ایالات متحده ممکن است پس از نقض آتش بس توسط ایران با پرتاب پهپادهای تهاجمی به کشتی‌ها، با زور پاسخ دهد.  "خواهید فهمید! آیا من پاسخ خواهم داد؟ خواهید فهمید."</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18018" target="_blank">📅 23:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18017">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ ایران را به نقض آتش بس متهم کرد</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18017" target="_blank">📅 23:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18016">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هیئت مذاکره‌کننده ایرانی قبل از مذاکرات، کتاب ترامپ را مطالعه کردند  طبق یک گزارش، مذاکره‌کنندگان ایرانی قبل از ورود به مذاکرات مستقیم با ایالات متحده، سبک مذاکره‌ای که دونالد ترامپ دنبال می‌کرد را از نزدیک بررسی کردند. این نه تنها شامل روانشناسان بود، بلکه…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18016" target="_blank">📅 22:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18015">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">هیئت مذاکره‌کننده ایرانی قبل از مذاکرات، کتاب ترامپ را مطالعه کردند
طبق یک گزارش، مذاکره‌کنندگان ایرانی قبل از ورود به مذاکرات مستقیم با ایالات متحده، سبک مذاکره‌ای که دونالد ترامپ دنبال می‌کرد را از نزدیک بررسی کردند. این نه تنها شامل روانشناسان بود، بلکه آنها کتاب «هنر معامله» ترامپ را که در سال ۱۹۸۷ منتشر شد نیز مطالعه کردند.
این مرحله نشان می‌دهد که چگونه ارتباطات غیرمنتظره‌ای در مورد فعالیت‌های ترامپ در رسانه‌های اجتماعی در طول درگیری پدیدار شد. بنابراین، طرف ایرانی سعی کرد درک سیستماتیکی از الگوهای مذاکره او ایجاد کند.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18015" target="_blank">📅 22:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18014">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آمریکا، اسرائیل و لبنان یک توافقنامه چارچوبی امضا کردند که بر اساس آن اسرائیل یک منطقه امنیتی در لبنان را حفظ خواهد کرد.
ارتش اسرائیل نیز آزادی عمل خود را در این منطقه امنیتی حفظ خواهد کرد -</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18014" target="_blank">📅 21:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18013">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ:
بنیان‌گذاران ما در اعلامیه استقلال چهار بار به خدا اشاره کردند. چهار بار.
من حتی یک بار هم ذکر نشدم. من بسیار ناراحت هستم. حتی یک بار.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18013" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18012">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0KP3Q7xNgQ2X_BetqdmsPZD2GWQ0A4fF80LdL1E4BofJy7j_k-wwGzp1vytzABTZ2-xIkhJQN4tGjA_1uSjOxEBGTgEhPLITsg9nudQN80idgVtH7jtrdaQiOrSBkrsDca07GUQ50IBKFrFHGaXCSf20pkKjLWDJZ_7aDRocxVAI441L3OL1nCtwksuZyDEda6ej_c7R_sGJ-8HAvklOjp6ZUirfw28Rl5EC9H5zQ_TR-PIFn2aE7XT1GmPfsSjcS7yZP_s562-Jv_6K9DyNVnqpERuirixV8hxHcFydUeMSIC-6uPnQuSzMoAReJPIuKZiZT3IYtHn5z4StWA5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ ایران را به نقض آتش بس متهم کرد</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18012" target="_blank">📅 19:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18011">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ ایران را به نقض آتش بس متهم کرد</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18011" target="_blank">📅 19:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18010">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انتشار اخباری تاییدنشده از پیشروی نیروهای زرهی اسراییل در جنوب لبنان</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18010" target="_blank">📅 19:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18009">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APN8_YQoB7a5yoo2ree_rUf7y1n_rDrCtuvlgwdgWGoWdWFXK3DnuWDOIKCLPrpRrtWRsxgCRU9FqaSkm1v22mmhCCkzprMn7Ag1iZzfsdhJKGbakxVqp17285vhZow9BZ4qNHFbuHxvXEx-YYaqjaSk5lhN6sRN5NNoK2NKM9Nkdgf0cO0zAGQ8UkzU_z_2yYKuDVpovXbPxQGPEpwoas72roBVswdVUh59vzIoo9K0hOkvPVyhuPC69vKZuOESvQrQIcn0ztnbvc2vSzfJCBU94Jxmy-smUGmQdQfvsKh7TxIvfQVWGLhJ_JHwtNqO09y6neP-Pd5l5s12O__Mkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق کنید.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18009" target="_blank">📅 18:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18008">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بانک ملی ایران در اطلاعیه ای از اخلال مجدد در خدمات کارتی این بانک خبر داد</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SBoxxx/18008" target="_blank">📅 18:16 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
