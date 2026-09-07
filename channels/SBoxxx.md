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
<img src="https://cdn4.telesco.pe/file/bUJURo5gBC1twpAc9F_97-Fcp3rp0VPJ2x4BB2eGjJzIy7bx3_nVcFm0Gtmx9pjnwky8nDltWzaD1onUX9TrOgkb55Y6EfsRV3fnHGa8rHkPrG5_siFOfxxv-lwIdRpcF64HnHerzVa6Fc7l_bryLfthmaT7N10W0HyMH2CGvyvkk6kJxt82vkOo_XkQHiaJWXkgohuJ0kFo3xm-AlE7DtLHkBoX_S1BIHm31eqVq7iGHVKJ-aNgJtKZsR7pdPBCF4JvCynrrjFR8MpFRwjMqfnwgllIfjidTyVy97n7PnHXyUgbdI4dSfHliFKX1ltj8URg-WealP9sxrezgn1bJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.7K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 23:33:12</div>
<hr>

<div class="tg-post" id="msg-20638">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سمیر الصبری، معاون وزیر دفاع دولت رسمی یمن:
«تصمیم برای آزادسازی صنعا و حل مسئله گرفته شده است».</div>
<div class="tg-footer">👁️ 976 · <a href="https://t.me/SBoxxx/20638" target="_blank">📅 23:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20637">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یک آزمونی هست برای تعیین قطب نمای سیاسی شما
این
گزارش نتیجه آزمون
برای من است</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SBoxxx/20637" target="_blank">📅 22:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20636">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ارتش ایالات متحده در حال حرکت برای استقرار راکتورهای هسته‌ای کوچک است، در حالی که برای مقابله با تهدیدات فزاینده علیه شبکه برق و افزایش تقاضای انرژی در پایگاه‌های نظامی آماده می‌شود.</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/20636" target="_blank">📅 20:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20635">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPRZVEvqO1i2GnQlqDcNO1dhe-mmwfErDOnXfXwgvM4gYd3iC3ieNl5LDOpn0EAoZFvhC1WX4zbR7OFgj3_EhgVUwwSt6cieyLTdR5FVfDv181rzkIa4mRa7OsdrJkNsoMOq4hIS-X8OEj9uRjwc6u6ZZgkpqhIhCUfWNaFI-R7-4TrHnr5aWBijzLRYETf2bnWR-Fulk0IoySjGNE_efr3GTngicUXuv4F5C0osTVutDJWfm3pC5CPeEK1B0PVnsX_qBZip9psE8ZS7otPFGscIhbBHL2-iKGFnGncuOC8YtPVHI5yb7vARpygZKMOfFAvexcv6ihT3g3hfQGLH9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سارا خلیفه مجری مشهور مصری به دلیل قاچاق مواد مخدر به اعدام محکوم شد!</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SBoxxx/20635" target="_blank">📅 20:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20634">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">علی‌آبادی، وزیر نیرو :   تمام نیروگاه های کشور برای تامین برق در آماده باش کامل هستند</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/20634" target="_blank">📅 16:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20633">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">علی‌آبادی، وزیر نیرو :
تمام نیروگاه های کشور برای تامین برق در آماده باش کامل هستند</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/20633" target="_blank">📅 16:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20632">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ki5ir91n0WZ_Wf_L19dDF4hnCOiuAyJFz7rWkWpDz9Hic6dSEcPJoJ9KKZ508Uc2sevM4WCojVeTARMAE8tRuY9ZVGYly1H9d-iNl34v5fPr4c8GIUK9JkszzCcz6MYFmCWmIpMb-7jHyqwGk1Nvxg-zNxScnG3E-SNBXO18TOL7PwwzeiyCv7CoiM3bt-4iUl8uC_nwVM94Yy2G62ea9uEtEAP_hkRJc1dTLmhTuJqnsq56-Aj2_V_zLJJF8_-DGDZCq0-0kQib5BZWyiNgbV6fi_pp3yeY6C5cutOAJje0HM_zkdhZGeQMuETtO29y1P3QEcC09S2bO9AfEQFmMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/20632" target="_blank">📅 16:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20631">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این ژاپن بزودی بدجور موی دماغ چین خواهدشد.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/20631" target="_blank">📅 16:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20630">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بوی یک حمله همه جانبه به نیروهای موسوم به محور مقاومت می آید:  — حمله پلیس عراق به منازل عناصر سیاسی نزدیک به ایران — ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی — توافق دولت لبنان و اسرائیل برای پایان حیات نظامی حزب الله — آماده شدن نیروهای مخالف حوثی ها…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/20630" target="_blank">📅 16:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20629">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">همزمان بیت روحانی فعال شده اند....</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/20629" target="_blank">📅 14:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20628">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حملات به تاسیسات شرکت سعودی آرامکو</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20628" target="_blank">📅 14:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20627">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 24</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20627" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 24
دو شنبه 7سپتامبر  2026</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20627" target="_blank">📅 14:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20626">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بقایی:   مذاکرات خوبی با هیئت قطری داشتیم</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20626" target="_blank">📅 13:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20625">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بقایی:
مذاکرات خوبی با هیئت قطری داشتیم</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20625" target="_blank">📅 13:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20624">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بعد از کتک خوردن عراقی ها در رشت، این بار مردم غیرتمند سمنان هم این وحوش را به دلیل دست درازی به نوامیس خود گوشمالی دادند.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20624" target="_blank">📅 12:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20623">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33e75cd83.mp4?token=Avnq3B2CfWWiDjpNv4_lQv-9CSouO2RNeHLMWHHzHhmi2rXkZTd8CEWVrSno6lS6hjyQ-EYyE_hJf5ahZaDIgIOHaOb2A478K1uxkxA30U26TA79x7eAn-NOmMYLbCCwBCFPSB7EZEym_B70z3_RJNRafXX-U7ZWF6SRr3KcozPKBLsiQFiGooB1clh78HO5TXEfac_jGZ4Zowr-KSsnSBKgLanMTX51BUPgwORUA44wYeTHLkRwYgMa27PqN0U4yRN7Nx5qPMAdvyZVD2Mu1bXu7WgaASmYfKFFwvC64zjh_EhDFwPLlTsYEKzDmLEthbN3gfkjFgx-QvntWfB5dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33e75cd83.mp4?token=Avnq3B2CfWWiDjpNv4_lQv-9CSouO2RNeHLMWHHzHhmi2rXkZTd8CEWVrSno6lS6hjyQ-EYyE_hJf5ahZaDIgIOHaOb2A478K1uxkxA30U26TA79x7eAn-NOmMYLbCCwBCFPSB7EZEym_B70z3_RJNRafXX-U7ZWF6SRr3KcozPKBLsiQFiGooB1clh78HO5TXEfac_jGZ4Zowr-KSsnSBKgLanMTX51BUPgwORUA44wYeTHLkRwYgMa27PqN0U4yRN7Nx5qPMAdvyZVD2Mu1bXu7WgaASmYfKFFwvC64zjh_EhDFwPLlTsYEKzDmLEthbN3gfkjFgx-QvntWfB5dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از کتک خوردن عراقی ها در رشت، این بار مردم غیرتمند سمنان هم این وحوش را به دلیل دست درازی به نوامیس خود گوشمالی دادند.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20623" target="_blank">📅 12:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20622">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در استرالیا استفاده از مواد روانگردان برای مصارف خاص درمانی قانونی اعلام شد.  پس از قانونی شدن ماریجوانا در بسیاری ایالت های آمریکا، قانونی شدن استفاده از مواد روانگردان طبیعی در موارد خاص در استرالیا پیشرفت مهم دیگری محسوب می شود.  شخصا باور دارم که بزودی…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20622" target="_blank">📅 12:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20621">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطوح میانه بالا قرار دارد و با توجه به ریزش بامدادی طلا، پایین هایش خرید موقت دارد با تارگت های 4418 و 4441</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20621" target="_blank">📅 11:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20620">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFv2Ciz28CyHCzt84EHWxFz4HGEac5iG1Vz_tJDAmUlUwa-xCR28yyEXod_eMIYvvnfsDk8B9LwQokpuCuWdRaaY_9wG1q15W-kFadskFVU1K7iXuPVu91XXHcjGIEXAWkfRQDfzYmHCNuLWAlgdn8W83R1039phMIRY8Cu1UGF2piO_eb0fhDBmCiPg4vINeaV1JDApEthJQ63Q-8PZ9jW-B7ALmTjTswmG_4qqFHkhFk9zy04owhqqyiumvab9ZtvFrLyvStg4fNbyI3oWHwuUrbYSBnRdmDwrjBiEJ6uxPWiyNgiG1RLvVRikgCpGFe9T4umBcJSHCzZb_HnRzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطوح میانه بالا قرار دارد و با توجه به ریزش بامدادی طلا، پایین هایش خرید موقت دارد با تارگت های 4418 و 4441</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20620" target="_blank">📅 11:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20619">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze2_2AbHS2eg_zzTeAScPbU3la3gDtW9ppzHRubOsI9ytJkRZOA-YvJxv0s88Mx9Lnzwn6FNd9Gtm2TEWrL4IoZiZmpZqwDeGpiD1LUUBKrCfhTmP5Z1rncrOupb3dS9RqJAl_YVf7gknLWJ_qZUoV6xlJtshvwnIVvUPpae__cC9-qRTQmlb469ioP8wU-haU0ZK5WFN6Xpcfjqp37SWTrydYh-ZODbOkwg3LunrFT6cyrvFukVI3t0fjcwqt5PzDBN-fV3dPx4QoyCOeab5Zki1dnlbQrZJG5G4Q5AtDB9sPMz9SUBSzu6ze2gDefYRj92v46DLi47VsVgcZ7QNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای لعنت به پدر مارک بوسنیچ که گذاشت آن گل را بزنی و بعد ۳۰ سال مجبور بشویم چهره و رفتار انیرانی ات را تحمل کنیم!</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20619" target="_blank">📅 11:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20618">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حزب‌‌ راست‌گرای افراطی AfD آلمان برای اولین بار در تاریخ خود در یک انتخابات ایالتی پیروز شده است.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20618" target="_blank">📅 09:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20617">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">— به گزارش رويترز، پس از حملات اخیر ایالات متحده و ایران به تانکرها، حجم حمل‌ونقل از تنگه هرمز به‌شدت کاهش یافته است.  داده‌های شرکت کپلر نشان می‌دهد که میانگین روزانه کشتی‌های کالایی در ۱۰ روز گذشته ۱۰ کشتی بوده است که کمترین سطح از ماه مه به این طرف است.…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20617" target="_blank">📅 08:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20616">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjIhHfOVlNpuOHrb2CRgQmc7kowTt6VfjYCeP4EDzOrYu-XcDcfZLyF7Arg9aOPmmopOW0p7oyPcoF-H9GCVwVuFnCdm4CuWwKrGbc2XE7cy7Fbmta8Ryhl9Xf0w3xXgswWTendR2Vl5Uqg8IA345TY4ixI_XWLYczkKLf---SdUoDVVue4wdvO65X-3f0-9WnKY1tSn6eNGjm1iejPQgqliQ7KvsdCo-i5NFaEGenG5SBK4gy-LbEh22aSlnlhcQN3gNg0HurNOIsYbpohJzEZqV3B_2WKb8yYmhMyzz7tzBx31Hstk41B53Y7TqY6JfOCPtdqoHiq_r5GyGAsEsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار این پست مدعی شده که بخش عمده نفت عبوری از هرمز به سطوح پیش از جنگ برگشته است!  به نظرم دروغ می‌گوید چون قیمت نفت خیلی بالاتر است</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20616" target="_blank">📅 08:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20615">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حزب‌‌ راست‌گرای افراطی AfD آلمان برای اولین بار در تاریخ خود در یک انتخابات ایالتی پیروز شده است.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20615" target="_blank">📅 02:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20614">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce5OqUxKT8TZaZ_XQ-TBiZcoqzwd5FXa0ypiwU52EndKD3c82m0kRDDVyIQv8OtMvGPd-8s-1itwbZgk3FrMbclb9D8IDxZwFG610GtOG_XvMxI6Rqr-inDq2NMwvSN40MGPLZYxS1G_gjxs7lenRH9cEiLzrIGkYSkJGdU_Dyqli5lpthbeVZeT85bqjQDz3jVBFeKOgd4n0lqV0-45MDwfFtvLW5RC59v11eVlMGzNSRS9mcxPcKm1x_d0n9ivwfuHbANhxmYiPCLCsG5hOzpOaF7Rvjq2HwHRrzE6hLhjpQyRP_8AcLcb6w9R2aJHTvQGI5zAzYQGn9tWe3amog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه میان‌مدت ترکیه برای سال‌های 2027 تا 2029، افزایش 229 درصدی در هزینه‌های دفاعی را پیش‌بینی می‌کند، که از بین تمام دسته‌های سرمایه‌گذاری استراتژیک، بیشترین میزان افزایش را داراست.
این رقم، هدف کلی برای سه سال است، نه افزایش در یک سال معین.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20614" target="_blank">📅 01:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20613">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آیا ارمنستان در حال تبدیل شدن به هاب هوش مصنوعی آمریکا در قفقاز است؟
ارمنستان در حال ورود به مرحله‌ای جدید از توسعه اقتصادی و ژئوپلیتیکی خود است؛ مرحله‌ای که در آن زیرساخت محاسباتی هوش مصنوعی می‌تواند به اندازه فناوری نرم‌افزاری و استارتاپ‌ها اهمیت پیدا کند. راه‌اندازی کارخانه هوش مصنوعی شرکت آمریکایی Firebird در نزدیکی هرازدان در اوت ۲۰۲۶، این پرسش را مطرح کرده است که آیا ارمنستان در حال تبدیل‌شدن به یک پایگاه راهبردی آمریکا برای زیرساخت هوش مصنوعی در قفقاز جنوبی است.
پاسخ کوتاه این است که هنوز برای نامیدن ارمنستان به‌عنوان «هاب هوش مصنوعی آمریکا» زود است، اما شواهد موجود نشان می‌دهد که این کشور در حال ایجاد زیرساختی است که از نظر مالکیت فناوری، تأمین تراشه، نرم‌افزار، سرمایه و مجوزهای صادراتی، به‌شدت به اکوسیستم آمریکایی وابسته است.
ورود
Firebird؛ نقطه آغاز یک تحول بزرگ
مرکز ثقل این تحول،
پروژه Firebird
در هرازدان است. این شرکت آمریکایی در ۸ اوت کارخانه هوش مصنوعی خود را به‌طور رسمی افتتاح کرد و اعلام کرد که برنامه دارد تا پایان ۲۰۲۷ بیش از ۷۰ هزار GPU شرکت NVIDIA از نسل‌های Blackwell و Vera Rubin را در ارمنستان مستقر کند و ظرفیت زیرساختی آن را به حدود ۳۰۰ مگاوات برساند.
این ارقام در مقیاس اقتصاد ارمنستان بسیار بزرگ هستند. پروژه فقط یک دیتاسنتر معمولی نیست؛ بلکه بخشی از مدل جدید AI Factory  است که در آن برق، سرمایش، شبکه، سرورهای پرقدرت، GPU و دسترسی به مدل‌های هوش مصنوعی در قالب یک زیرساخت یکپارچه ارائه می‌شوند.
دولت ارمنستان حتی ارقام بلندپروازانه‌تری را مطرح کرده است. بر اساس اعلام دفتر نخست‌وزیری، در مرحله دوم سرمایه‌گذاری کل پروژه به بیش از ۴ میلیارد دلار خواهد رسید و حدود ۵۰ هزار GPU جدید NVIDIA Vera Rubin به زیرساخت اضافه خواهد شد. مرحله سوم نیز قرار است ظرفیت کلی را به بیش از ۱۰۰ هزار GPU و بیش از ۴۰۰ مگاوات برساند.
البته باید میان ظرفیت فعلی و اهداف اعلام‌شده تفاوت گذاشت. تحلیل‌های مستقل تأکید می‌کنند که رقم ۷۰ هزار GPU و ظرفیت ۳۰۰ مگاوات عمدتاً یک نقشه راه توسعه تا ۲۰۲۷ است و تحقق آن به تأمین برق، سرمایه‌گذاری، تحویل تراشه‌ها و وجود مشتری کافی بستگی دارد.
نقش تعیین‌کننده آمریکا
وجه مهم‌تر پروژه، صرفاً اندازه آن نیست؛ بلکه منشأ فناوری و نحوه دسترسی ارمنستان به آن است.
شرکت Firebirdیک شرکت آمریکایی است و پروژه هرازدان بر پایه فناوری NVIDIA و زیرساخت Dell شکل گرفته است. علاوه بر این، توسعه مرحله دوم پس از دریافت مجوز صادراتی آمریکا برای انتقال هزاران تراشه پیشرفته NVIDIA به ارمنستان امکان‌پذیر شد. دولت ارمنستان می‌گوید مجوز اضافی برای ۴۱ هزار تراشه NVIDIA GB300 صادر شده است .
این نکته از نظر ژئوپلیتیکی بسیار مهم است. در عصر هوش مصنوعی، کنترل دسترسی به GPUهای پیشرفته عملاً بخشی از قدرت ژئوپلیتیکی محسوب می‌شود. واشنگتن نه‌تنها بر تولید بخش بزرگی از تراشه‌ها و طراحی آنها از طریق شرکت‌هایی مانند NVIDIA تسلط دارد، بلکه می‌تواند تعیین کند چه کشوری به پیشرفته‌ترین نسل‌های محاسباتی دسترسی پیدا کند. از این منظر، ارمنستان صرفاً یک مصرف‌کننده فناوری آمریکایی نیست؛ بلکه در حال تبدیل‌شدن به محل استقرار بخشی از زیرساخت محاسباتی وابسته به اکوسیستم آمریکا است.
«دیپلماسی تراشه» و قفقاز جنوبی
اهمیت این موضوع پس از گزارش اخیر
Wall Street Journal
حتی بیشتر شده است. این روزنامه گزارش داده که دولت آمریکا در مذاکرات مربوط به توافق صلح ارمنستان و آذربایجان، از دسترسی ارمنستان به تراشه‌های پیشرفته NVIDIA و پروژه Firebird به‌عنوان بخشی از بسته اقتصادی و تکنولوژیک استفاده کرده است. WSJ این رویکرد را نمونه‌ای از Chip Diplomacy توصیف می‌کند.
اگر این گزارش را در کنار پروژه Firebird قرار دهیم، تصویر بزرگ‌تری شکل می‌گیرد: آمریکا در قفقاز جنوبی فقط به دنبال روابط دیپلماتیک سنتی نیست؛ بلکه می‌تواند از فناوری پیشرفته، سرمایه و زیرساخت محاسباتی برای ایجاد پیوندهای بلندمدت اقتصادی استفاده کند. این تحول از نظر ژئوپلیتیکی قابل توجه است، زیرا ارمنستان در نقطه‌ای قرار گرفته که میان روسیه، ایران، ترکیه و آذربایجان واقع شده است. ایجاد یک مرکز بزرگ AI وابسته به فناوری آمریکایی در چنین موقعیتی، می‌تواند حضور اقتصادی و تکنولوژیک واشنگتن را در منطقه افزایش دهد.
چرا ارمنستان؟
مزیت ارمنستان فقط موقعیت جغرافیایی نیست. دولت این کشور طی سال‌های اخیر تلاش کرده است خود را به‌عنوان یک اقتصاد فناوری‌محور معرفی کند و از سرمایه و نیروی انسانی دیاسپورای ارمنی نیز استفاده کند.
اما مهم‌تر از آن، دولت در حال ایجاد تقاضای داخلی برای Compute نیز هست. در آوریل ۲۰۲۶، وزارت صنعت فناوری‌های پیشرفته ارمنستان قراردادی پنج‌ساله به ارزش ۲۵ میلیون دلار با Firebird امضا کرد تا منابع High-Performance Computing را برای استارتاپ‌ها، پژوهشگران، دانشگاه‌ها و فعالان حوزه AI خریداری کند.
این اقدام بسیار مهم است، زیرا مدل توسعه صرفاً بر صادرات خدمات دیتاسنتری متکی نیست. دولت می‌خواهد یک اکوسیستم کامل ایجاد کند. همکاری دولت با شرکت‌هایی مانند AWS و Mistral AI و ایجاد «Artificial Intelligence Virtual Institute» نیز بخشی از همین تلاش برای ساختن اکوسیستم داخلی است.
اما آیا ارمنستان واقعاً «هاب آمریکا» خواهد شد؟
در اینجا باید محتاط بود. یک دیتاسنتر بزرگ الزاماً به معنای تبدیل‌شدن یک کشور به مرکز نوآوری AI نیست. برای ایجاد یک هاب واقعی، ارمنستان به نیروی انسانی متخصص، دانشگاه‌های قدرتمند، شرکت‌های نرم‌افزاری، سرمایه خطرپذیر، مشتریان بین‌المللی و مهم‌تر از همه برق ارزان و پایدار نیاز دارد.
مصرف انرژی نیز یک چالش اساسی است. صدها مگاوات ظرفیت AI برای کشوری با اندازه اقتصادی ارمنستان عدد بسیار بزرگی محسوب می‌شود. بنابراین توسعه Firebird به همان اندازه که پروژه‌ای تکنولوژیک است، یک پروژه انرژی و زیرساختی نیز محسوب می‌شود.
از سوی دیگر، رقابت منطقه‌ای نیز در حال شکل‌گیری است. Firebird همزمان در حال توسعه پروژه‌های زیرساختی در قزاقستان است و برنامه جهانی آن تا پایان ۲۰۲۸ به حدود ۲ گیگاوات ظرفیت می‌رسد. بنابراین ارمنستان لزوماً تنها مرکز منطقه‌ای این شرکت نخواهد بود.
نتیجه‌گیری
با این حال، اهمیت پروژه را نباید دست‌کم گرفت. ارمنستان در حال حرکت از مدل سنتی «کشور کوچک با صنعت نرم‌افزار و استارتاپ» به سمت مدل جدید «کشور کوچک با زیرساخت محاسباتی استراتژیک» است.
اگر برنامه Firebird طبق نقشه راه پیش برود، ارمنستان می‌تواند در چند سال آینده به یکی از مهم‌ترین مراکز GPU Compute در اوراسیا تبدیل شود. نکته ژئوپلیتیکی مهم این است که این ظرفیت بر ستون‌های فناوری آمریکایی بنا شده است: NVIDIA برای تراشه، Dell برای زیرساخت، Firebird برای پلتفرم و سرمایه‌گذاری آمریکایی و مجوزهای صادراتی واشنگتن برای دسترسی به سخت‌افزار پیشرفته.
از این منظر، شاید عبارت دقیق‌تر این نباشد که «ارمنستان در حال تبدیل‌شدن به هاب هوش مصنوعی آمریکا است»، بلکه این است که ارمنستان در حال تبدیل‌شدن به یکی از شرکای زیرساختی آمریکا در جغرافیای جدید هوش مصنوعی است. و این تحول می‌تواند پیامدهایی فراتر از اقتصاد دیجیتال داشته باشد. همان‌طور که خطوط لوله نفت و گاز، بنادر، راه‌آهن و کریدورهای تجاری در قرن بیستم ابزارهای قدرت ژئوپلیتیکی بودند، در قرن بیست‌ویکم GPU، برق، دیتاسنتر و Compute نیز می‌توانند به بخشی از معماری قدرت جهانی تبدیل شوند.
اگر پروژه هرازدان به ظرفیت‌های اعلام‌شده برسد، ارمنستان دیگر صرفاً در حاشیه اقتصاد دیجیتال قفقاز نخواهد بود؛ بلکه می‌تواند به یکی از گره‌های محاسباتی شبکه AI تحت رهبری آمریکا در منطقه تبدیل شود—درست در نقطه‌ای میان روسیه، ایران، ترکیه و آسیای مرکزی.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20613" target="_blank">📅 00:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20612">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20612" target="_blank">📅 00:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20611">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebedA9YfYP2aKurHF0UNIvDeF7qUvlD8EVBwbC0MEA7EX0KTQeP7WFy38MuAGBKQkVzOs-jC4Cbola-ELDpRndw6RHNgnS8ihG2XcgLLVDCPOovRyzkcIA62BONTKkmBcF1xY6Zg1ip5OBdUqMLw26U93qQ63H_WdXA-eGpmwoZecpdNUkZhK-fBMbD4HY1OPOCTYo9ym4IzJWwOtJ-WwNNYXYmZHQYg1O1_3liiuTage0oXgjo3IwrBbWgey8nAPJtvHHlba4fANE4XiMhOWdXvDaORQ7TE6JzNH7IfTGX7vDgtYedSvfbyVAb4bkuCGjPRmBg04JnOQvSkGgmqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!
ولی همین که نام Persian Gulf را می نویسد باز خوب است</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20611" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20610">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIl1tcRIO8A0KAEo7JVf7w7PqzrOQOEWxH0vI6JXmSxpdij_EsV33d_H0Kx8GSmGQ4Ljztvq2rPG5NrCDMbYwQpKJ0rBnmlU61uVMUUJtWCWr4HheilKUkoTbb3Inm9aVrXz2kkMN3wcp45RrWiQgjyM5EGDIi25AMOSfrsZWVrKloENCh2iRvS5Hqzpf0w_JlnLtLkaR8yby7kcttroWWSTlkD1TjYCI3xtB1qysjVYHVYQM6R0FBNEzudl7KTDXVF64RpAoz83M2SeNx25iD_8NmsCiaXLpY9KYfTurv68uh_qrZglrfnuKuZSYWl0sz2moj5oco4jw2qQJWh0xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیره انشالله!</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20610" target="_blank">📅 00:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20608">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سرلشکر رضایی:
برای داشتن وحدت باید به رهبری نگاه کرد</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20608" target="_blank">📅 00:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20607">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWbUgJb41-OLbX-YzcAOKcTWKARsQj_P_5-lHh2V0FRzSSD_t6ZeG_VkbC_7cxNBmijcsnz7kR0Q5JSM0RhQijMeDRENE76ZIAvc5POl8IBp0gqbLUHa-jOBhHLGs8e69IE_RDrCNuZc9R9-TfrR0sj8Cvxrv7I2R8We3lPy8aBwoKNBZzOfdPoSG9IE6vJo0QoBh_sU3f8Z1uz_UM2mGRtZGrbk9WC4zRNIcOl5MsDXt_gEeduXvUpy2ZARbOF38KYnCpHuS_T326CXOPbrXFWSe-CxB0JEj-RlWZv74F66EqViQOptRpCgwHqcV45_hgUy7ckHNrlyPBg0aEMW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:  در روزهای آینده منطقه‌ی ممنوعه خارج از تنگه‌ی هرمز را اعلام خواهیم کرد.  این منطقه‌ی ممنوعه از خط محاصره‌ی دریایی آمریکا شروع شده و تا مناطقی در خلیج فارس امتداد خواهد یافت.  هر کشتی که وارد این منطقه‌ی ممنوعه‌ی جدید شود، به فهرست هدف‌ها اضافه…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20607" target="_blank">📅 23:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20606">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWp-y0A3szAdzlm6K2V77trz000vWc7Pm5A50grCGum_y-0r9ay7rdX8IW6Ick7pA3-j0gvzpN8bCuCpPj8hnWYu21HQ00l8qI-UVA4owSEtxVh5gQfF_OgGu-1zK7aSi6qUxUEDtzAOk2iiaw7SxRAC2rjg-lI-tA1sppwIydfZTIj_36SDch14h8o25s3ulTqPCWlCoCdgBFNqA_LpI71z4rvCwrAQTOeQglSD1qdILBgKouMCYrY5A6g7GuJjIfxz9SzvrAnBN5g2D2YqQ1yAyI72l3_lVVyxml3V_HN3YQXb8C-z5K6NMujmxXqIDwM8iVLO1SY2PkiYzK4D8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه ما خیلی سلاح های دیگرمان را تست نکرده ایم   مثلا شاید طبق مورد ۷ بخواهیم کوههای البرز را ببریم تنگه هرمز تا این‌‌ تنگه برای همیشه بسته بشود و اسمش هم بگذاریم تنگه ترمز!</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20606" target="_blank">📅 23:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20605">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سردار رضایی:   ایران عمدا تصمیم به غرق کردن کشتی‌های آمریکایی عبوری از تنگه هرمز نگرفته است، زیرا آنها حامل نفت هستند که می‌تواند به محیط زیست آسیب برساند.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20605" target="_blank">📅 23:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20604">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سردار رضایی:
ایران عمدا تصمیم به غرق کردن کشتی‌های آمریکایی عبوری از تنگه هرمز نگرفته است، زیرا آنها حامل نفت هستند که می‌تواند به محیط زیست آسیب برساند.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20604" target="_blank">📅 23:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20603">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enLIyJSBNZ7-uyaFYHwlQkXMaQN34L09ytL33KQGHGRKpQE1C0hvz9IUrsDVXyBZw5KEbqamIJZzLAlfe0csapRfwneblexea82X9w4HrRoJlbMxm2LbzlVNzzGY6GrnIkvey_JvehLyj9TuGOwJGik4tIPosFYnvyq3Uk9EC9hW2PWrNXQZMCG7eQzXdXvzL8VPzXDsi1ZGYSMMkaBMAJDtGrZuLAFPKb8zpOae4DbrrhxClwkvAeZfx0IbaJzDt-MMN-NkmV_FdRoNUfHmoMhWOOqCkpS_ynRQQMsKONr1Zv6mcJeiK3NQkTvO9QD6ZFvcS55g5uJ75ylpAq6gjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:   برای اولین بار موشک خاص و ضدناوشکن ایرانی آزمایش شد  ۴۸ ساعت پیش برای اولین بار موشک ضدناوشکن ایرانی را بالای سر یک ناو آمریکایی آزمایش کردیم.  این موشک خاص، جهنمی برای آمریکایی‌ها به وجود آورد و فرار کردند.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20603" target="_blank">📅 22:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20602">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qONR-Z2r8JpsHaWd-0Og6oOM5cWowykWKbgBePlHvN0JJ87mfVvnk0eaq3hAkZuNPW8ZFQGID3JQqh2kZFN_Y9RBaJiX3Ra_1e5Mu2DWebh94fh7Z0bP0AThesDvnhm_pGYBa3Xwc9iPztTIZTCTKUOYCybZlLIdT7SFf5gI-tQ0AEtmXPhmvGh-1aghUkAdI0nd8wwQ9xlgxzGN0zyq4RmN0uSwJOK_eBzYRaJ-whxKH-jaQ-Hct7_ZwamEDVzIpiFrdZD7aiFyLV1xCYIllCwuAJpZKJgb0RO97s6Nhb9-qpPH9AsNso3Bu3zOwfFJLa2Us9o-9Bs2WJZ03NHJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار این پست مدعی شده که بخش عمده نفت عبوری از هرمز به سطوح پیش از جنگ برگشته است!
به نظرم دروغ می‌گوید چون قیمت نفت خیلی بالاتر است</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20602" target="_blank">📅 22:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20601">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">محسن رضایی:  در روزهای آینده منطقه‌ی ممنوعه خارج از تنگه‌ی هرمز را اعلام خواهیم کرد.  این منطقه‌ی ممنوعه از خط محاصره‌ی دریایی آمریکا شروع شده و تا مناطقی در خلیج فارس امتداد خواهد یافت.  هر کشتی که وارد این منطقه‌ی ممنوعه‌ی جدید شود، به فهرست هدف‌ها اضافه…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20601" target="_blank">📅 22:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20600">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26516f3c08.mp4?token=KLMNyYQeEnnI4Ik5gNKiJN5YCrmr373JT9kXgs_gPXv1L8DHWbZHFiZev2KIUvh3UBiCuzE2atlcWiRr1sqEHomDpaS0W_zCB6itEwZMO4d1zBQjmUegbWBi7g7qHlRTZ4-pfjFRIl168KgLJX0LWdXzSyshrenzYiIOcKqU9uQVHZEnhLUMi4-rRi_VM-73RVs3d7x5mYeUwOqtRg9UtpDb7GEFFOH9bhR3hhPSWfCONmVcZlfqVL1nGlzZGXkbGyL4fIZew_ed7wIAEs78IptZJSFRhF4AktzGxaTHylZaEzknlZATqCUwiQvLwSCEsKylMKc9EafKD-OhBUZTZ7HRa7ZH_oRiWC48BXpFuC1EiNUuqYKFf8Cz5tCjTOFBX099XiXcq27BiqRg382iu2aDGuceB8xH3VvNV1vojdJ8qu5Pk4ORfJY3_mRBd9mDcTAYrFwskesJRVrd7flRsV2bO2OPqdsKfx4gqLw3Ty1S4-eBafZFKNzP2CKKHJTYkyHu3HULwIX9ezO2xAb8gWxog08V3gyeB1TMNxoIFylET74O2gD0rQ1Xmt3wbwiBnKnV04vrYr1qBLqVsSa1C2a-oTq3b66I0gXDiYo9h101kLrtYql6KhyMImGEsuy1IPbnDjUYs95K14iDafIM70E3OoE8nzmfbFPD3RpNPrs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26516f3c08.mp4?token=KLMNyYQeEnnI4Ik5gNKiJN5YCrmr373JT9kXgs_gPXv1L8DHWbZHFiZev2KIUvh3UBiCuzE2atlcWiRr1sqEHomDpaS0W_zCB6itEwZMO4d1zBQjmUegbWBi7g7qHlRTZ4-pfjFRIl168KgLJX0LWdXzSyshrenzYiIOcKqU9uQVHZEnhLUMi4-rRi_VM-73RVs3d7x5mYeUwOqtRg9UtpDb7GEFFOH9bhR3hhPSWfCONmVcZlfqVL1nGlzZGXkbGyL4fIZew_ed7wIAEs78IptZJSFRhF4AktzGxaTHylZaEzknlZATqCUwiQvLwSCEsKylMKc9EafKD-OhBUZTZ7HRa7ZH_oRiWC48BXpFuC1EiNUuqYKFf8Cz5tCjTOFBX099XiXcq27BiqRg382iu2aDGuceB8xH3VvNV1vojdJ8qu5Pk4ORfJY3_mRBd9mDcTAYrFwskesJRVrd7flRsV2bO2OPqdsKfx4gqLw3Ty1S4-eBafZFKNzP2CKKHJTYkyHu3HULwIX9ezO2xAb8gWxog08V3gyeB1TMNxoIFylET74O2gD0rQ1Xmt3wbwiBnKnV04vrYr1qBLqVsSa1C2a-oTq3b66I0gXDiYo9h101kLrtYql6KhyMImGEsuy1IPbnDjUYs95K14iDafIM70E3OoE8nzmfbFPD3RpNPrs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:  در روزهای آینده منطقه‌ی ممنوعه خارج از تنگه‌ی هرمز را اعلام خواهیم کرد.  این منطقه‌ی ممنوعه از خط محاصره‌ی دریایی آمریکا شروع شده و تا مناطقی در خلیج فارس امتداد خواهد یافت.  هر کشتی که وارد این منطقه‌ی ممنوعه‌ی جدید شود، به فهرست هدف‌ها اضافه…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20600" target="_blank">📅 22:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20599">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">محسن رضایی:  ما موشک ناوشکن‌مان را بالای سر یک ناو تست کردیم و آمریکایی‌ها وحشت‌زده فرار کردند.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20599" target="_blank">📅 22:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20598">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">محسن رضایی:
ما موشک ناوشکن‌مان را بالای سر یک ناو تست کردیم و آمریکایی‌ها وحشت‌زده فرار کردند.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20598" target="_blank">📅 22:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20597">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ: ایران از خط قرمز ما عبور کرد.
در یک حمله غافلگیرانه، آنها پنج موشک با سرعت ۸۵۰۰ مایل در ساعت به سمت نیروهای آمریکایی شلیک کردند که هیچ اصابتی نداشت و هر پنج موشک سرنگون شدند.
اوضاع درست می‌شود!
در همین حال، ما واقعاً به آنها ضربه خواهیم زد؛
اکنون نوبت ماست که حمله کنیم.</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/20597" target="_blank">📅 21:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20596">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfz5mB5byI98-Ve3f7ceDQnng4RyXyOvBzavXrdDlDpgwy3e7Ze6hqGfSK2yC-G1gf_H_hDYWTQ3ePM4zFGOk0_7ZBU0SAhPGSkZeo5cyKboz-6z7v-CzyoZ5qrx_IuI7V5spEPr4hM3knc52-adV79tTaLw7mcgMGhMJxlWNL4kJnQjQcSUCbnJ5Ar6SbQIJvnE-6J-AB9789C9KGoRlj0inxGPqDMWC2e__OV9cHYtIVkVkdNtcNq0-Pq15lF4Qn65IVT-aU_dIX5g_YjXp8ZFf4sC1KXM4k0l4qb7gf2Ox1vsZaJBONQMfwsTQgMXVQqdikMtXPuvFI1knBTaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هیئت قطری به سمت تهران حرکت کرد</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/20596" target="_blank">📅 18:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20595">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یک هیئت قطری به سمت تهران حرکت کرد</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SBoxxx/20595" target="_blank">📅 18:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20594">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سنتکام:
نیروهای ما تا دیروز ۹۲ شناور تجاری تغییر مسیر داده، ۳ شناور از کار انداخته و ۲ شناور نیز توسط نیروهای آمریکایی مورد بازرسی و توقیف قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20594" target="_blank">📅 18:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20592">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qATgBA_ZUka7evEmiLE6fbIaBXU41gWatJlhkAzX5CERJEXci4wwyTBih2NDxiGKnQM-XGZCWrPtMWkHIVx2qxI_t2vtyyeEucNnxBW0kIcT77RNT_qwMHrV3unDSGsLLFgidCWNmJoPyQFCtaLBrn5lQ2gzGeSb2zuMK1d1x2Bad65o3bpatpF6GSwzscElYb5505GDVoOHy4M1xsKqT5QPSbohb7RP0JNA_ne7nla-uPDOPaIO9PcyLh_9oKlGrY1cfHfphu4-voQqL7-EOd2bvZl9zYz191y9QUMPKH4W1Ozg7tiXNoFORG7fVY6tDGETHDqMcQ8amdk5_I2p0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار سوخت گازوییل در آمریکا وارد تنش‌آورین دوره سال شده است. موجودی جهانی گازوییل در یک سال گذشته ۲۸.۵ میلیون بشکه کاهش یافته و به ۵۴۲ میلیون بشکه رسیده است. در ایالات متحده، موجودی‌ها از میانگین ۵ ‌ساله نیز پایین‌تر آمده است.
دلیل اصلی، کاهش عرضه از روسیه و خاورمیانه است. ممنوعیت صادرات روسیه تا ۳۰ سپتامبر تمدید شده است.
وضعیت در خاورمیانه به دلیل اختلالات در تنگه هرمز پیچیده‌تر شده است. محدودیت‌ها بر ۳ تا ۴ میلیون بشکه فرآورده‌های نفتی در روز تأثیر گذاشته است. در نتیجه، نرخ بهره‌برداری پالایشگاه‌های ایالات متحده به ۹۸ درصد رسیده است که بالاترین سطح در ۸ سال گذشته است.
بازار از قبل با کمبود مواجه است: بر اساس تخمین‌های CERA، کسری ۲ تا ۳ میلیون بشکه فرآورده‌های نفتی در روز وجود دارد. در ۱ سپتامبر، گازوییل در نیویورک تقریباً ۲۰۰ دلار در هر بشکه، یا حدود ۱۴۸۰ دلار در هر تن قیمت داشت.
اکنون، خود ایالات متحده در معرض خطر مواجهه با کمبود سوخت قرار دارد. تا ۲۸ اوت، موجودی ULSD (گازوییل با گوگرد بسیار پایین) در ایالات متحده ۹۴.۱۸ میلیون بشکه، یا تقریباً ۱۲.۷ میلیون تن بود. در یک سال گذشته، این میزان ۱۲.۲ میلیون بشکه (۱.۶ میلیون تن) کاهش یافته و ۷.۴ میلیون بشکه کمتر از کمترین سطح پنج‌ساله قبلی (۱۰۱.۶۲ میلیون بشکه) است.
تا ماه اکتبر، موجودی‌ها ممکن است به ۱۰۰ میلیون بشکه، یا ۱۳.۵ میلیون تن برسد. این اتفاق در بستر اوج تقاضای فصلی رخ خواهد داد.
اکتبر و نوامبر احتمالاً ماه‌های دشوارتری خواهند بود، زمانی که تقاضا برای سوخت برداشت و نیادز به گرمایش همزمان افزایش می‌یابد و برخی پالایشگاه‌ها برای تعمیرات برنامه‌ریزی‌شده تعطیل می‌شوند.
در آمریکای جنوبی، موجودی گازوییل در پایین‌ترین سطح فصلی خود قرار دارد یعنی حدود ۲۱,۵۰۰ تا ۲۲,۸۰۰ هزار بشکه، یا ۲.۹ تا ۳.۱ میلیون تن.</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/20592" target="_blank">📅 13:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20591">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یک جوری‌ مینویسند دلار را رنج منفی کشیدند ….
به قول امام خمینی (ره) انشالله خداوند همه ما را آدم کند!</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SBoxxx/20591" target="_blank">📅 12:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20590">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خشم روسیه از تغییر الفبای قزاقستان به لاتین!
این دقیقاً در راستای تحقق رویای توران بزرگ ترکیه می باشد که من آن را به عنوان حوزه بعدی تنش میان غرب و روسیه (و احتمالاً چین با توجه به جدایی خواهی اویغورها) تخمین می زنم.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20590" target="_blank">📅 11:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20589">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:   سه فروند شناور آمریکایی را در مناطق دیگر هدف قرار دادیم</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SBoxxx/20589" target="_blank">📅 01:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20588">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf9VC6e6SXFHRQOMgpKTHBV4M2wVKyl1_dhmJQVhEf_XLKlUDjY0aOkxCZAsxzJ5ZBmjVQnOEv9ujWCItkQwDR7ZGTqSxxhG7_jyFU35QxVi5FWvo7XCUapH3gvuetRrkpr4zOLYiQ8BWUKkYjEobTc04XEWJADoIgdEMvrPPYnkRvmUXpSuaOeK1AWxQV3g41iVb9F5edSXzbGZ5XN6E6XwDhgLVXr5jZmkFaqQYA6QYRnb_9ahFoz_Pl8F1d2siDxeeHQjHerhedE6zxrbm55bLELdoSzhInTwzeI7_FDy0cgdnFFTVdyQyXBn8HHnQckzcV7JJ5JbBaVHDsaaHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر فروش تسلیحات آمریکایی به متحدین نظامی اش از سرگرفته بشود واقعا؛ یعنی گزارشها درباره فرسایش ذخایر تسلیحاتی ارتش این کشور تا حد زیادی اغراق آمیز بوده است.  نتیجه بعدی هم این است که روابط ترامپ با روسیه و چین دارد تنش آلوده تر می شود</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SBoxxx/20588" target="_blank">📅 00:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20587">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:
سه فروند شناور آمریکایی را در مناطق دیگر هدف قرار دادیم</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/20587" target="_blank">📅 23:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20586">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/20586" target="_blank">📅 20:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20585">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خبرگزاری ریانووستی (RIA):
پوتین وضعیت پیش‌آمده در مذاکرات کرملین با ویتوف (Withoff) و کوشنر (Kushner) را دشوار خواند</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/20585" target="_blank">📅 20:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20584">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Secret Box
pinned an audio file</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/20584" target="_blank">📅 19:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20583">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دو ایستگاه برق دیگر در آلمان هدف قرار گرفتند و مواد منفجره کشف شد</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/20583" target="_blank">📅 19:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20582">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ادامه انفجارها در تنگه هرمز</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/20582" target="_blank">📅 19:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20581">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ گفت پس از آنکه بایدن ذخایر راهبردی نفتی آمریکا را خالی کرد و از پر کردن مجدد آن خودداری کرد با نفت ونزوئلا دوباره پر خواهد شد!  این توافق مهم شامل بیش از ۶۵ میلیارد بشکه نفت است. این امر آمریکا را در مسیر سریع بازسازی ذخایر خود قرار می‌دهد.</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SBoxxx/20581" target="_blank">📅 18:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20580">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نقشه جدید کشورهای جهان بر اساس ابعاد واقعی شان!  طبق این نقشه که ابعاد کشورها را مطابق با اندازه دقیق شان نشان می‌دهد، سایز کشورهای غیرغربی افزایش قابل ملاحظه ای داشته است.  رنگ آبی: نقشه کنونی رنگ صورتی: نقشه جدید</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20580" target="_blank">📅 18:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20578">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromExciton Computer Missile Program</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EH3bNRf1gefZWlNgKTlHxptXmi5t0mxtfuBjItaEf81ADqdNZaAAv6ps3hH0qQGEzakEZZZZsn4uBZENxzSvs0nTe75r7orN6OuxlvnF91F_8FCK6xPJ2o8Swf9m2GsYbjQ8nf9jLj8pwtp4b3A_kcA8GVB3DrzBHM_wmFKyYhiKJ9diysWH3QWb5f4hWikpfOrHZKwBMCPIi2gtin1fUNPP8NLz3cPk3b1FoYk03kkI6Arcyz6a39isg58TUnNtJkBqzv8TsaxrsEwFudos07IUGf0E5iOK4tef2BmK0MsEerhy-l5jxbw5wFMESCw8g6Tkbr0hym06WXZ6U3SNVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iH56dNCwPlGQwj4Ij-0HVuWUpB6-C2po4TQ5JX5Lj_Qakrq1f6dbDD5Bi_VLH6LeHxLWM3xCdUpjGXd6eh1U_MDLicaEesFBbg6kNcPVzK7hPMHF_5cmNLRuFPCVhGq3b3Jf87OT_ak2M2UNPRV7z_icF9puBLmm14NRqTNqGkI3SR6oGg6F4bKZN4pjN_1-HDfPtOihsOPf6g2OVseNRZm3676fKh4qV6AAxaIyw00pMZ0f0VXHzA9F_T3IbiM2JNsAEpq4j9S2Bl0y801_-bivOLAd2hJrNJbDX2s8rd6pRWH2irLf8jvVphst11vpsjIAws0h6t1PG6jCqnCbfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپاه دیروز حداقل 3-5 بالستیک ضدکشتی به سمت دریای عمان یا تنگه پرتاب کرد تا شناورهای آمریکایی را برای پر هزینه کردن محاصره برای آمریکا بزند که به نظر اصابتی رخ نداده است. شناورهای غیرنظامی بزرگ در فاصله کوتاه عموما حرکت ممتد در خط مستقیم و قابل پیش بینی دارند، مگر مسیر خاص باشد. اما شناور نظامی میتواند پرتاب موشک را متوجه شود و مانور خاص انجام دهد. شاید یکی از عللی که حوثیها در هدف قرار دادن شناروهای تجاری حتی در فواصل دور موفقیت نسبی داشته اند همین مورد است (اما حتی هدف قرار دادن چنین هدفی هم با بالستیک بسی پیچیده و مشکل است).
اما مانور شناور شناورهای نظامی کارایی مطلق در برابر هر موشکی ندارد. یک موشک پیشرفته میتواند بخشی از این مانورها را ناکارآمد کند. در هر صورت موفقیت یک موشک بالستیک ضد کشتی بسیار وابسته به اطلاعات دقیق از انواع سنسورها میدانی است. وگرنه شانس اصابت جدا از طراحی موشک کاهش خواهد یافت.
🚀
🚢
(
بحث آماری پیشین در رابطه با بالستیکهای ضد کشتی حوثیها
)
@Exciton_missile_program
🚀</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20578" target="_blank">📅 17:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20577">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سنتکام:
پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند.
دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر در دریای عمان منهدم شد.
سنتکام اعلام کرد این نفتکش‌ها بخشی از شبکه تأمین مالی سپاه و نیروهای نیابتی آن بوده‌اند.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/20577" target="_blank">📅 17:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20576">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnIN2e_lPMIri6CVarj7BMq9FVtROmxF1IWhmDunV6nyvRD2a0wGfIxZOY8174OfPszmGjFKIwnv0TytsXngM-1PONVKYzJk4KFAZWtIt1SiphboHQBE9mfzGTGSMxcBIz8z_g7OYhnxcWmO97yY6aApmGMF-mBfI2JKj82t4p86Ibg9_E1pDaJPBsNcKZ7AcPwfpFCQX-5hHqFMJFL_ClKtgOGJjYlowijTkvr2-8fbduMKMIJUehAk_hI4xR6NrhlSwrb_YxoBJ9E6xe66l751Q5tMuRgek3CWhy2hvtIN9O0dmq5UAxrhHiCameVu_Oo7tnWMTb3x_2IFXz_hCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین کشورهای هر قاره جهان  بر حسب مایل مربع</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20576" target="_blank">📅 17:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20575">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">انتخابات اسرائیل</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20575" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تمایل شدید نفتالی بنت به سرنگون کردن حکومت ایران را باید دقیقاً در راستای صحبت آخرش — از دست دادن آمریکا و حمایت جهانی — ارزیابی کرد.   یعنی اسرائیلی ها چون فهمیده اند حمایت جهانی را از دست داده اند میخواهند خاورمیانه را بازمهندسی کنند تا دیگر تهدیدی برایشان…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20575" target="_blank">📅 14:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20573">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">راه آهن کشور اعلام کرد ترکمنستان و قزاقستان با تبعیت از تحریمهای جدید آمریکا مانع انتقال ریلی کالا از چین و روسیه به ایران شده اند.</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/20573" target="_blank">📅 14:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20572">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجنگاوران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNZlmNYppqTda4PrLAUnmHIJMF8KJPwFUOSJC_z_0NhhSjeJuDM6LaEZXUqe8V1pxgaHNsluAtFSp2aAOBgOJ4PCiHPGevAMlk5hvokxVzVi95WnzRhPMyX0k71Srm3l2hf1j_oCUE7t23Ws9jTcO51UXxoQVbCkGojUeBUbAcDdDiUrMc11awJRE5dR_qzvbCQ26oKZ8MdDeEGLAmpFQkP3zBm-CnX8CedfZNuWA3O9CdVI9xCqgD9zNX4yK0SLfN7DPVw8c7SUkAdXjgE6i4eKhYbdREwdPcsIZEoJCZnAJHpPkAtlIIi-coXc2xLlNJrjc7jqSNVj4e78VTeUuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهپاد تهاجمی جدید ژاپن؛ به اندازه یک چراغ‌قوه!
ژاپن برای نخستین‌بار تصاویری از یک پهپاد رزمی بسیار کوچک را منتشر کرده که ابعادی تقریباً در حد یک چراغ‌قوه دارد.
تصاویر منتشرشده توسط NHK WORLD-JAPAN، پهپاد را درون یک محفظه لوله‌ای و با آرایش چندروتوره نشان می‌دهد.
با وجود ابعاد بسیار کوچک، این پهپاد برای انجام مأموریت‌های شناسایی و حمله در برد نزدیک طراحی شده است و می‌تواند به دوربین‌های شناسایی یا مهمات مجهز شود.
از جمله اهداف احتمالی آن، خودروها و تجهیزات زمینی عنوان شده است.
ابعاد بسیار کوچک
قابلیت حمل در محفظه لوله‌ای
آرایش چندروتوره
امکان استفاده برای شناسایی و حمله
مناسب برای عملیات نزدیک نیروهای زمینی
این پروژه نشان می‌دهد ژاپن نیز مانند بسیاری از ارتش‌های جهان به سمت پهپادهای بسیار کوچک، ارزان و قابل‌حمل برای مأموریت‌های تاکتیکی حرکت می‌کند.
#ژاپن
#پهپاد
#پهپاد_رزمی
#پهپاد_تهاجمی
#نیروی_هوایی
#فناوری_نظامی
#دفاعی
#Drone
#Japan</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20572" target="_blank">📅 14:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20571">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">زاکانی:   به دنبال برق اتمی برای شهرها هستیم</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20571" target="_blank">📅 13:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20570">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">زاکانی
:
به دنبال برق اتمی برای شهرها هستیم</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20570" target="_blank">📅 13:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20569">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اسکات بسنت:  چنگال مرگ اقتصادی را ضد نظام ایران فعال کرده ایم:  ارز آنها در حال سقوط است و صادرات  نفت شان به 0 رسیده !</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SBoxxx/20569" target="_blank">📅 12:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20568">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ایران دارای یکی از بزرگترین ناوگان های نفتکش دنیا بود اما با این وضعیتی که پیش می رود باید از شوتی های زحمتکش مرزهای شرقی و جنوب شرقی کشور برای انتقال نفت بهره ببریم!</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/20568" target="_blank">📅 10:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20567">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEdf9mX3jQYNl5GibSIVwaavRhAoRn0kxhFTXMRIrcjKmgW8TKV_q0vbdBX9MraQrfw_Gxqy2PxHg-6w-vcxRjwsuEbRRWeKLvBeaJBd3IefmGfGI7ioTVErPG966SNMXM0YxJX9tcmlN7V2Of3_s7ZlMbYla5X2WCWiKDj8d07DQI-yJJi2bMsfqtL_akut-CjDagZYxvkgpLW2gg1m4mdmFP-L0_pQdytrpmWfAnRdNeC9uGiSw20t8WySy1VpojF10fWKcJOw2yJcWnhbxl2Mzs5jUXyOXZLh9baKa5J2LqdFZohnHSZyflbDa9DxYcCU1WE1xviiJcHchbEW-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SBoxxx/20567" target="_blank">📅 09:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20566">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUE7H6ncfEp3KZ3W8bs7rxuxzBeQ0qAmdqvmUqOvVTm583bT_difdFhAX3N91Koai9zYH5ZoM3r0ys2zrjY730ufsbfpWmF1GQcjzGLxY40z_Fmk2XeY_3BjIWlXv19UJMpIDC-rZGiNVtwXHC4vZ_P-NmkV--W0sP8KVZ6lRfniK-RZUaSXPE2t2lHXp_CBcw15XL3CVuRi3fEGqyO95-CTS7cqR6n_uXw38EcPNDEENY4QlFOeAd6LOdm87tFsxX5SZKRHOPVz-2YThMTOI068jqB8F6Tfq54PS9tgHs44dTV_rsJ0LoCG3GvRsC0Zq70_kZzr9uINoMf4FqddSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دوباره هما خان سعادت در آسمان کشور مشاهده شده....</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SBoxxx/20566" target="_blank">📅 00:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20565">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">— شلیک موشک‌های کروز ضدکشتی از سیریک به سمت تنگه هرمز.</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SBoxxx/20565" target="_blank">📅 23:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20564">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEW832TftN5wYSTFvyC5WO69Pe7PeaMuUjkitekkpiGoWXQp2lIbT8EN-gRTl0m1Ix4aRR0qiGNVLt1QvSkE1UcVSeqVR6SOiMHBZ_hotKCvV5zF1nQDUxtxArhMKUlY31K46puRCPgVcJeCuIj-I-F4MK1-HRfI3ua_qhZI_3dJEWrvy-eVi4tXVMeoG3PE4po3Mrm-ydAF5qyCYUOJxU9Xua3wm2ZNpC7G16DLehmBn9Le4La6XkWcyCD8PafONThyLDzi6l98QaGObvhM-V0PQ8UrvxUjsSTM2_8lAGkFvDHTKYMg3o6BnNstrNjfmQmHTcOyBc7WDTfU395hAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما تکذیب کرد!</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/20564" target="_blank">📅 23:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20563">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">قرارگاه خاتم الانبیا:  حملات پیش دستانه علیه پایگاه آمریکا در اردن که در حال آماده سازی برای حملاتی علیه کشور بودند را انجام دادیم.   |</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/20563" target="_blank">📅 22:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20562">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ
:
ممکن است خیلی زود کوه کلنگ را هدف قرار بدهیم ، چون حس می‌کنیم آنجا اتفاقی در حال رخ دادن است</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/20562" target="_blank">📅 22:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20561">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJJNyJw1Nx2kskNyuVwM-xisR_s3gAlsjjhLTn1lNef7iJesg85LlGfEZsrbsAGcNZUStT6PeOHJ-TKH2hVMFPvfZJJ2MJWzhZkH0oMxJ7ULOWfOMESlSE2d9y2diTnet_LP7QNpxk4wOih6hnUPMFdw4qOT-8Nt4TpXxmogFAzJFZfyAS3lPykxrq177Qd4_BYkNTA-KxzDHSX_sdBOTyqd-m5bh7AUkl90Asxyc5rg7LvFSWznIMlH8W8G2nr0T-Mn8-KxXY1UIaZy2q5W8mTb2_TyHOS2ELUOebT8HrpGdn7ccS2ZfclsDfYNBZKoinSMTot5lry0COU09x2Yug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش حسین پاک از تپه های علی الطاهر!  به گفته او، تپه های راهبردی یادشده از دید نظامی سقوط کرده اند</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SBoxxx/20561" target="_blank">📅 21:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20560">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">برخی سایتها و منابع خبری از حمله موشکی ایران به پایگاه‌های آمریکا در اردن خبر می‌دهند</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SBoxxx/20560" target="_blank">📅 21:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20559">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اسکات بسنت:
چنگال مرگ اقتصادی را ضد نظام ایران فعال کرده ایم:
ارز آنها در حال سقوط است و صادرات  نفت شان به 0 رسیده !</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/20559" target="_blank">📅 20:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20558">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">از نبطیه چه خبر
نتانیاهو راست گفت که مسئولیت نخست دولتش‌، تامین امنیت کشور و ملتش است و در این باره منتظر کسی نخواهد ماند(به خصوص امریکا). شاهد، رخدادی است که از ۱۰ شهریور تا امروز همه خاورمیانه عربی بدان چشم دوخته اند. خبری وایرال شده.
ارتش اسرائیل کنترل عملیاتی ارتفاعات علی‌الطاهر نزدیک نبطیه را به دست گرفته و زیرساخت‌های زیرزمینی گسترده حزب‌الله را پاکسازی و در حال خنثی‌سازی است. این مجموعه که طی دو دهه با هزینه مالی کلان ساخته شده بود، شامل اتاق‌های فرماندهی، انبار سلاح، ژنراتور و امکانات ماندگاری چندین ماهه می‌شد و به عنوان مرکز عصبی واحد بدر عمل می‌کرد. در واقع هتل-قرارگاهی چند ستاره.
موقعیت مرتفع آن امکان پرتاب موشک‌های کوتاه‌برد و پهپاد به شمال اسرائیل را فراهم می‌آورد؛ و مساحت و تیپ ساختش ماندگاری طولانی را برای نظامیان فراهم می ساخت. ولی از مدت ها پیش، با شناسایی دقیق ماهواره ای، هوایی و تجسس زمینی‌، بستر برای تصرفش مهیا شد.
این عملیات ترکیبی از محاصره طولانی، شناسایی دقیق با پهپادهای حرارتی و ورود مهندسی بود. برخی نیروهای حزب‌الله کشته یا مجبور به عقب‌نشینی شدند و تجهیزات مهمی به دست اسرائیل افتاد. از دست رفتن این گره راهبردی، توان فرماندهی محلی، ذخیره‌سازی امن و پرتاب محافظت‌شده در محور شرقی جنوب لبنان را به طور محسوسی کاهش داده است.
البته این  ضربه به معنای فلج کامل یا جمود نظامی حزب‌الله نیست، ولی موجبات شگفتی کارشناسان خبره نطامی را فراهم اورده است.
حزب‌الله سازمانی غیرمتمرکز با ذخایر پراکنده موشکی و پهپادی در عمق خاک لبنان، تجربه جنگ نامتقارن و پشتوانه ایران است. نابودی یک مجتمع، هرچند بزرگ و مستحکم، توانایی بازدارندگی کلی، عملیات چریکی یا بازسازی تدریجی را از بین نمی‌برد. نمونه‌های جنگ ۲۰۰۶ و درگیری‌های اخیر نشان می‌دهد این گروه پس از ضربات سنگین زیرساختی همچنان توان پاسخ‌گویی نسبی خود را حفظ کرده است.
اثر واقعی این عملیات در تضعیف الگوی «جنگ پایدار از زیرزمین» در جنوب لبنان، افزایش هزینه بازسازی و تقویت فشار سیاسی برای خلع سلاح یا عقب‌نشینی بیشتر نهفته است. اسرائیل خود اذعان کرده شبکه‌های مشابه دیگری هنوز باقی مانده‌اند. بنابراین، آنچه رخ داده پیشرفتی واقعی در خنثی‌سازی نقاط کلیدی است، هرچند حزب‌الله همچنان بازیگر نظامی فعالی باقی می‌ماند و سرنوشت نهایی به واکنش‌های آتی، وضعیت آتش‌بس و توانایی بازسازی بستگی دارد. ولی حزب الله دیر یا زود ناگزیر به مذاکره و توافق است. دقیقا شبیه حماس.
#یدالله_کریمی_پور
#Karimipour_K</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20558" target="_blank">📅 20:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20557">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارشات تایید نشده    از شلیک موشک از اصفهان</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20557" target="_blank">📅 20:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20556">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ve5kJdripak_5jrLoQX4tgof1aCFr4XgSJld4NCPANLl5mI0lqOhAeO7iI3YaY4pzp_BffOi4-jgNVBngNhIwUjz3SphWFixj4ptDy7q0djLcEcf_NriDWLCIyYvHox-nvdNhDC8X5nVFeByIWWL4Q_Z0Hpsj6QGtdWWBWnafIZyejxRzbJoUM8iiYZRgcw1vi4hxj2rI31GPC3AMrNVqFyd07jdSn8H_2zHK3m8M88KqdnQiAHCAIJEDvG7GCHRec1mNknif_7mgwFmocFHkBryiwBtjLw5DXnWgd_lElSMvqFq9vZLyKVO9BZ4Mk-3eQUGBbBm8lFaxiKxrP4GOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی اکنون به 48 افت کرده و می توان در این محدوده ها دست به خرید طلا زد</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20556" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20555">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2MHNXkbFs3g9Eug6_M7LZHuLS4oVFEbwPWCPT6XtPN-j3bzg0mC6ybVcrK1sl4W80cibBgbU9YQPKuofiA_fBjcHMlqaMCloDgZl5dhp-L61ik6ssO28LiqK4Hbp9eO46f9yssXnfFzQS1xO7mnFBvA74RpN4_jK6c8vaU3bDFuJeFGmTtSOf5YvOg67C0dDKakxBTtdNMNk_ce3viKqvhBoQdKSn_kRGuLSRkTFzIAQwYabGCCaHX4aFp44aEUC8Z_E26Z_vrSEZDH2SXUO4gL4AimavGhuIFQrtPvWaqRDi5V5gv1nemJ0DkN_NXXFz0kRzo72SSizTe2uxGVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد و پیش بینی می شود دستکم تا 4385 شاهد افت قیمت باشیم.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20555" target="_blank">📅 20:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20554">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گزارشات تایید نشده
از شلیک موشک از اصفهان</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20554" target="_blank">📅 19:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20553">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">از اپوزیسیون هم شانس نیاوردیم !
این قاضی زاده تا دیروز فعال سیاسی بود از امروز شده فعال بازار شت کوین !</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20553" target="_blank">📅 19:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20552">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ایالات متحده تحریم‌های جدید مرتبط با ایران را علیه بانک ترکیه‌ای گلدن گلوبال (Golden Global Bank) اعمال کرد</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20552" target="_blank">📅 18:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20551">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مثل این است که یک مرد مدتها با یک زن غرغروی منفی باف گوشت تلخ زندگی کند و با کلی بدبختی و پس از سالها صبر از او جدا بشود و بعد در ازدواج دومش هم با دختری با دقیقا همین مشخصات ازدواج کند و همان فحشهایی را که به اولی میداد به دومی هم بدهد!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20551" target="_blank">📅 18:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20550">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مثل این است که یک مرد مدتها با یک زن غرغروی منفی باف گوشت تلخ زندگی کند و با کلی بدبختی و پس از سالها صبر از او جدا بشود و بعد در ازدواج دومش هم با دختری با دقیقا همین مشخصات ازدواج کند و همان فحشهایی را که به اولی میداد به دومی هم بدهد!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20550" target="_blank">📅 18:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20549">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این ترامپ رسما دیوانه است!
رفته خودش این کوین وارش را به جای جرومی پاول آورده بعد امروز وارش را تهدید کرده که یا نرخ بهره را پایین می آوری یا تجارت با کشورهای دارای مازاد تراز تجاری با آمریکا را متوقف می کنم!
همین هفته پیش وارش گفته بود تورم بالاست و تمرکز ما روی مبارزه با تورم است و شاید نرخ بهره را بالا ببریم!
جالب اینکه همان پاول فلک زده را هم خود ترامپ در دوره اولش آورده بود و بعد هر روز به او فحش میداد که چرا نرخ بهره را پایین‌ نمی آوری!</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20549" target="_blank">📅 18:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20548">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارش مشابه</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20548" target="_blank">📅 18:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20547">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گزارش حسین پاک از تپه های علی الطاهر!  به گفته او، تپه های راهبردی یادشده از دید نظامی سقوط کرده اند</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20547" target="_blank">📅 18:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20546">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حالا اینقدر بچه ها نگران این تپه نباشند؛
ماشالله اینقدر تپه هست برای فتح کردن !
مثلا یک تپه ای هست به نام امین الطاهر که کنار علی الطاهر است و هر کس به آن نگاه می‌کند طلسم می‌شود و فیلم «تپه ها چشم دارند» بر اساس داستان این تپه ساخته شده.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20546" target="_blank">📅 17:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20545">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d58b19c9.mp4?token=ALpls-M5pVf-LU4BkW7cbJ-v7WoPkbQ6FNDBDskISi2OgKGR-5gtu8SmoMZWuY5as5LqRQW99Vo6V0sNvFHuWtn98un73e1hYRaE12UsXSWzFVvjvlH6H2WD50x8Q5eSngUIkhDVH01c0apOyVt46zTglDCeB_Pp25gbfcBZAdW5dJuFMiJN8FoU7AyEEcPDgHMLMBdUeDag7zgauF1GRG5btjczA-PheCJJ7I4Nyc8STH9kEqqU868UX7ohuh6bExo37tjT0iLP9HP_EVRWKNf8k8qt357OzUSvObIKIEJiGUGtTwdlcJTP7ADNDFAvBKdK1DqkAQ7tq-sgaMTKAoOgSK14SXz_B1M3_mf50gkM-JM_Q5QYWUD5CyREHNRf-YFgjBySb9V661CLUvNAWHhLISe0P-J6ChAwGGXXzsUqjCSgGnwsZtKp1lGj0eD8WVNT4v63OuYbz6PHiPgrJk6Ofdjja_TJ3reQy1dSmkb0tFy877OJh50hx9Id4GGHszE42lmBi4S9YOnVdTOxNxMEul3nJQhtPwufeBB6i7NDrkGZzURSFhlkPaA89g-rASO4WkLAyLn0TIb3mCmZLHZU3ATY0e-DiNE-ORwcFP0DBoGmd3mjRDkDXW6x36PrQcRbLF8TaYkzpWToPy2y0yEwP5BrRNagYTNB4Cgdew4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d58b19c9.mp4?token=ALpls-M5pVf-LU4BkW7cbJ-v7WoPkbQ6FNDBDskISi2OgKGR-5gtu8SmoMZWuY5as5LqRQW99Vo6V0sNvFHuWtn98un73e1hYRaE12UsXSWzFVvjvlH6H2WD50x8Q5eSngUIkhDVH01c0apOyVt46zTglDCeB_Pp25gbfcBZAdW5dJuFMiJN8FoU7AyEEcPDgHMLMBdUeDag7zgauF1GRG5btjczA-PheCJJ7I4Nyc8STH9kEqqU868UX7ohuh6bExo37tjT0iLP9HP_EVRWKNf8k8qt357OzUSvObIKIEJiGUGtTwdlcJTP7ADNDFAvBKdK1DqkAQ7tq-sgaMTKAoOgSK14SXz_B1M3_mf50gkM-JM_Q5QYWUD5CyREHNRf-YFgjBySb9V661CLUvNAWHhLISe0P-J6ChAwGGXXzsUqjCSgGnwsZtKp1lGj0eD8WVNT4v63OuYbz6PHiPgrJk6Ofdjja_TJ3reQy1dSmkb0tFy877OJh50hx9Id4GGHszE42lmBi4S9YOnVdTOxNxMEul3nJQhtPwufeBB6i7NDrkGZzURSFhlkPaA89g-rASO4WkLAyLn0TIb3mCmZLHZU3ATY0e-DiNE-ORwcFP0DBoGmd3mjRDkDXW6x36PrQcRbLF8TaYkzpWToPy2y0yEwP5BrRNagYTNB4Cgdew4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری صداوسیما:   ادعای نتانیاهو مبنی بر تصرف تپه‌های علی‌الطاهر هنوز به تایید شورای نگهبان نرسیده است</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20545" target="_blank">📅 17:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20544">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی اکنون به 48 افت کرده و می توان در این محدوده ها دست به خرید طلا زد</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20544" target="_blank">📅 17:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20543">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdNR2vqcgVeybmDgPdpSfDTjH_jk11UGCYjxYEMOyMDRQMkUWUIauEwmxIJUg11g7R4k5pzrvbam7e2LRl91n67dw3TzBqP4nhpxpED5fswoMKT2nZBqgqmxk0XsQkDG7EMGvBM4gtdvBFIzaN71CQ3eAEA7fcj3aNVB_DM8xNvP2PF1COUYu1gfiyOgmsHEGSZ7Zp3RGV98h4RLohDsKbg64TVGNlg9Twd9SrT3egIbHw1J8fbNKVbRkNtNVSXaeuMfCFQ2e5YZx4H0S0S0yUSujI7WJfdJwSqbWkJmRomS5eiFQom_0_3gzvhgSIP3YtLN62JqgQCyefFrxBIMhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی اکنون به 48 افت کرده و می توان در این محدوده ها دست به خرید طلا زد</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20543" target="_blank">📅 16:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20542">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">در‌ روزهای اخیر باز اسم عاصم منیر مطرح شده بود!  سبحان الله !</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20542" target="_blank">📅 15:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20541">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/20541" target="_blank">📅 09:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20540">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ظاهرا آرژانتین با حمایت ضمنی ترامپ به دنبال حمله دوباره به جزایر مالویناس (فالکلند) است.  جالب است که به محض انتشار این شایعه، استارمر بحث تروریستی اعلام کردن سپاه پاسداران را به جریان انداخت تا شاید از امتداد شعله خشم ترامپ جلوگیری کند.  اخیرا بریتانیا تصمیم…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20540" target="_blank">📅 09:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20539">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRm5HqxCY6Mm1pbEb5_wRSsiY3-sO4S6z7mK4E6YgEMS4bQtwk1pnzuXZiBCzDwak1c_0vYe_nwi1p5l55MMFPCgjPjSS8veh3hs-Lmw9jtGXdj5-f1uym0M0fNnZpFrN9mKmaWBN11jkxo1u7ONdbHCdLwXgRNEM5Rl5hwvkHgnEcfsc-FVJxuiAEmTnz2esLY0RHyBgBnDWsUTC7_K1Arg4Iigvd5pHEwErn3w1HDUE7hl1sMdn6R97RCrgFoI5JgKzDnCyBGVcfH9hcZmHkDGyIeQ803GkfA7QwlyeWeLwFZk8c9iMKt3X7dSEtnsKMP9LOMsofylM2qXXJQFdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش خنثی سازی مین ها از راه دور
این روش عمدتا توسط نیروی دریایی بریتانیا به کار می رود که تخصص ویژه ای در مین روبی دارد</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20539" target="_blank">📅 01:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20538">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_KKFm5_mfEEwBTSYhOKu021rirU7J4xVBjW8TGSro_1bgLqyKSc1WhT_GOR6FG55ZKjd-0XdO9gVyId8c5lL4e552oJHY_yaSaHBD4hP15gQ8xVWDRTnUfdiqRtzCTATFBhlzM4GSOD8o97hpmQWKdBWCECuRGDo_9OlN5vWc3WyU1iBuTkf-1Elims5LgLGokml5jpjzIwKdiK5R4v7IvOvoIMMYGNENCtoUZk9-vDykziDTNTicxYMmva3i0YZvBbtDiSBhok92hiwGaIMr7FRjFXFU17CYQAJGu0K28uIDHUwkcbPosWJoLP5znPI5HruUI5ezH8tmmqC_nWYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این گزارش های آژانس هسته ای و اظهارات تند ترامپ + نتانیاهو شرایط را به صورت قطعی به سمت جنگ می برد.  مراقب موج‌۳ باشید.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20538" target="_blank">📅 01:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20537">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20537" target="_blank">📅 01:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20536">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5fc46a9c.mp4?token=WspauPW2CQnp4kPv1vPA5VzSz9Kaf16DEFwRw-PJTZgbn4Osi1Hs0mtjZtURqy8Z42OqCnOkKurxGdgolBGgAkrLA1k7VO4cMG21ENM8HCGXBg4CepsUR9VBn18khbqB8Y4M1Tg90NB3eenxmQlUmytbejBzP9WCTf3RMjin6uUKbfHI1R34t-MXzG048Wp7lIyMQkEB7cVZaKOukIYNecvu6_Q8jKGgZK0RgpvWMJmNMxapWjOwLHSg8yI4eFEMkTQlnH06iyu113-hZnZc9yodCYqI_3yhtKKctUqNa4O1XKu5t6n50FExAVvwrstFYulyzstZdLuvRW8HHUcJoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5fc46a9c.mp4?token=WspauPW2CQnp4kPv1vPA5VzSz9Kaf16DEFwRw-PJTZgbn4Osi1Hs0mtjZtURqy8Z42OqCnOkKurxGdgolBGgAkrLA1k7VO4cMG21ENM8HCGXBg4CepsUR9VBn18khbqB8Y4M1Tg90NB3eenxmQlUmytbejBzP9WCTf3RMjin6uUKbfHI1R34t-MXzG048Wp7lIyMQkEB7cVZaKOukIYNecvu6_Q8jKGgZK0RgpvWMJmNMxapWjOwLHSg8yI4eFEMkTQlnH06iyu113-hZnZc9yodCYqI_3yhtKKctUqNa4O1XKu5t6n50FExAVvwrstFYulyzstZdLuvRW8HHUcJoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسراییل برای دومین بار اعلام کرد بر تپه های راهبردی علی الطاهر مسلط شده است.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20536" target="_blank">📅 01:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20535">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار سوریه به فارسی 𓂆</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f5a76c78.mp4?token=qZ9qwWYs2i_7FRpU9q4CTNDUaJZ2uZumC4BUfjqpr5XUxeSijBauYMMEsIfWtrFBzWrS3jRSCB0KW1Nmr7xAJdEoYcoV3hYN48Pc7SPu1TxmTmgIOEIQu7YXeXDjf5QZvdxq8VzZKsRQhMj7vYYHfoV7CS_18bj6cicpn1lvXj6lVXwDd8g7_aihJv4XgGBMfpyu5gQ9b5FajJjGE2zH4oBnHXwScPqECIxFfHYuA0R_XNjQVxR88t5SsYVViNlijtT16sH3M3WrJkSzaMXWnpbcsoBGZY7wFyiesZHJ0pWFjVJfUpmUQlnJOE1FjuAz1P5CMozNWxnw8mku2PuYuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f5a76c78.mp4?token=qZ9qwWYs2i_7FRpU9q4CTNDUaJZ2uZumC4BUfjqpr5XUxeSijBauYMMEsIfWtrFBzWrS3jRSCB0KW1Nmr7xAJdEoYcoV3hYN48Pc7SPu1TxmTmgIOEIQu7YXeXDjf5QZvdxq8VzZKsRQhMj7vYYHfoV7CS_18bj6cicpn1lvXj6lVXwDd8g7_aihJv4XgGBMfpyu5gQ9b5FajJjGE2zH4oBnHXwScPqECIxFfHYuA0R_XNjQVxR88t5SsYVViNlijtT16sH3M3WrJkSzaMXWnpbcsoBGZY7wFyiesZHJ0pWFjVJfUpmUQlnJOE1FjuAz1P5CMozNWxnw8mku2PuYuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حالا درسته اسرائیل علی طاهر رو اشغال کرده ولی اینکه ترامپ پای یه کاغذ پاره رو امضا کرده به شما حس خوبی نمیده؟
@SyrianToPersian</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20535" target="_blank">📅 01:22 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
