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
<img src="https://cdn4.telesco.pe/file/jIHNrJjaDHSiMTTl-U7W8-YEkEgFSA0KHHR7_Md-IYUEAU7VNqpgHWsraJSfe6bXEwP8hjlILrktoDLeaU-PmRnZEofvhzy-nT1aXMkKSjFKqFgl9Zig-p5lHOUhT-MASen0ndIEO6_ZN3LTSXNiYmwbwWcaDuh-GQU6LIz7a5CEelUowM9PzPBr4X3Y2N64WMa5O1270KC0WRcgTnNYvfqIUxUtdz5BVgw4LVP2YDW88CSsWgDL497xZ8HT_TqXr5ntq1c7ym5GuPnyaAThBzFjnL_caXqU0VfFHZpucCnuOoehJmjYoXPd-outwHQHueOwCmEVbBC_GItKo-N7sw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 202K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 08:37:57</div>
<hr>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=mmPcCkPdnC_pMKeeDK-192HrGpp7N-JOTd37W-Afd8TIg-xYoOiv6lEUnvjZJ2rbhKqdHgJpPErlQuC6Z82YolVI-pW-Z-rDVM5azV6nWk9QYR9X3KwP50qZmzsO0OYZCi-rf-HVXmidb-vG9ogW66DZwHmbQJVpOo7PnSLfZaFpDBOSCcDo6tG4nfcjv5MZ86wAXXrHvxJ4TwNSSWdMcUZqehdvTm0p2aCw8fq1MhNsJqYifsS1qLAD8NzcbswFRUpelpHYABgy8pT_t9j4r3-tpw8N16cy9H1jdPkKEIAqPF9JT5r1sSPrTOITZB0R_Pd21PcmJJmmtKEreXTkCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=mmPcCkPdnC_pMKeeDK-192HrGpp7N-JOTd37W-Afd8TIg-xYoOiv6lEUnvjZJ2rbhKqdHgJpPErlQuC6Z82YolVI-pW-Z-rDVM5azV6nWk9QYR9X3KwP50qZmzsO0OYZCi-rf-HVXmidb-vG9ogW66DZwHmbQJVpOo7PnSLfZaFpDBOSCcDo6tG4nfcjv5MZ86wAXXrHvxJ4TwNSSWdMcUZqehdvTm0p2aCw8fq1MhNsJqYifsS1qLAD8NzcbswFRUpelpHYABgy8pT_t9j4r3-tpw8N16cy9H1jdPkKEIAqPF9JT5r1sSPrTOITZB0R_Pd21PcmJJmmtKEreXTkCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=veCPnEUV4cpojdLmHvthy0yUr-FpRbXGB6OeqaOszyHrzUmZxDAE3C4kpxw3DLayAl1sPsJXVgGhrceulvf1BH5s4CRvf6C3xIUyUhC-hCBZTwyhEQg4NEaNXLV1nK6MLOMffnyPZZNTdqyiIyqsVMXqbfIAr58Au1dOzhWHNYInNLTD9whICKZcBlKxT8XFn4VoWNzjN1AHa-xFtT-5otEsovDHtgbONSoLYfe2wCNzIv96HJP6chz9ql5igLCtCc8QKbgrl87fRdnDwDYSxOzKiorkt89QVxbaOYq8HJoLAYF4CpV1679bSd5EHCycMd-33J2aN9J-NAWBus8AUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=veCPnEUV4cpojdLmHvthy0yUr-FpRbXGB6OeqaOszyHrzUmZxDAE3C4kpxw3DLayAl1sPsJXVgGhrceulvf1BH5s4CRvf6C3xIUyUhC-hCBZTwyhEQg4NEaNXLV1nK6MLOMffnyPZZNTdqyiIyqsVMXqbfIAr58Au1dOzhWHNYInNLTD9whICKZcBlKxT8XFn4VoWNzjN1AHa-xFtT-5otEsovDHtgbONSoLYfe2wCNzIv96HJP6chz9ql5igLCtCc8QKbgrl87fRdnDwDYSxOzKiorkt89QVxbaOYq8HJoLAYF4CpV1679bSd5EHCycMd-33J2aN9J-NAWBus8AUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65223">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔹
اگر میخوای قبل جام جهانی با بازی های دوستانه مثل رضا کینگ کونگ پول دربیاری همین الان وارد کانال شو
👇
👇
https://t.me/+YF28GUBRSZkwYTlk https://t.me/+YF28GUBRSZkwYTlk
‼️
با درآمد دلاری پیشبینی های این کانال شرایط بهتر میشه  g11
🔥</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65223" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65222">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmOiLfrMHNaJbYdD_uOby8ODQygRMaSA1-3l2zzjNPuo8EBeVP4LaXlYodHvv1UzLBCuxvvFNdK3HDmZZbfrlpn_QAGAh7tma1UhshoT0Z02voc4c0n5l4o5Q3gea32ILHHxnQUjql-QuSvDj_Ke_3gEvb6IJa3_gOjn0U8C2V_khsVHj9KrR5N5pDDSrdGBUAbjcEyzwqyTPLAS1-FwEtdJ5RfACGy0emtds4PLEx4hCHyfqUFZPcfRLjTn8-BNjxFUBX7WXu-g_C5aUgDlWsniJBizNEsgz_dEzD_jHUwMuxA82kdVjmgw-RIckNKjdHLU3uBzeYTUYYofsFFizw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اگر میخوای قبل جام جهانی با بازی های دوستانه مثل رضا کینگ کونگ پول دربیاری همین الان وارد کانال شو
👇
👇
https://t.me/+YF28GUBRSZkwYTlk
https://t.me/+YF28GUBRSZkwYTlk
‼️
با درآمد دلاری پیشبینی های این کانال شرایط بهتر میشه  g11
🔥</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65222" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r889RVM95CtCiSE635dIcEPW-AGz7nAGtjH9PUgyGLXhPMRw9vXVp3y8ihKWLW7HygpH4pTpNcYUXqFte35Pgj6rUXbOFV9_Gkst34FUZZdk_oGHtFsxop2vejX-k-TOig84FXEbGsvulEgdf4k3Q51JXtEw6PewM-jBbF2UAdP8C1My_yOTs4QXnq9LsHI0P_w3gatL1wG41bNehIjOHRLqmZOXbYBM-5JmqEDZXWC_3784Gtlc89h7Pfq8BXvbpk4nE1fZWXRH1C4udQoJqnJMvlIzpVdjTH2pnZDm4Wa-HNU7MeU_XWsZ4hLWQN8KCf1LOUMBr7PON9ye5dFApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mfd7Ayg99IpKPzw0hSnokEOInmZtlSLYjNJvY3wXSULg487aMpOhg7cmnv-ZJSVq3a4KYHA_KXKwnpKEiJOLaZ6unQP4EM9LzEU-st0UVdoU7xt9ua8Pp_TNGsSDHPzf7t_CBPlPaEbhNjf7Luf6gcZNcJOu6HRWfr_qYhBU3MigLbKdxV8C98FeGIDduBQz6ciTJe8GAJY642Jfuls6tscbSQ-AJ-1QE5r5FpTpY-qx4oY5nVF3ndbeRSPr_wtxMbfRGnvHArtq5Wtc28ruTMuLMho5GxR8dhdbaB3KOwg-P3vLk7wfb-0d3TZs8jFE7jJ48trkkn2lWA4SqmeI7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCRfN4yL7UMSfQKN_xBXzfg6n4phYcHswP_ZgeZeCdfP55P-84_CTU0B-53nXLZXHmQ6Ff39eSbAydVJZqTIJeMLGxyqy91Nq0aFJNpjJ_K2iEYL_mnxy0P6XleOuzvVBbSAIRCeNN4Otsq5wlmhe9gHKZQJgwC-bcDCGtOtj3ibYDmI2Y6t0OdKQP3sCQh88a1rMOn-TiBOEDP-XJS9qzgLG_gPixkJeOejZ1ArdEHgHOgW_zTadH3q1htse1UmVvsUUSmgLgwL2rPqfDuumcLqCjQ-_-MnhyOfNoIHkTiFCSLT_Pn5Eh1HdnyruQ2DArgakS16O6OFpRXrWO1u-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HKguuF7--CRyLFvjw1K7oqpBt84N7hqM66sbRZCysg_D4s2Uo4KKIsF3x_69HMws5_JkiiMC9kwYY_VCyryFQ0THKupl6xO6sfH1F2rvHDmE5REt2geXvB9O7_QBmBEHwqp5gul6K3DqUCzCC-dZ-J2igknP4uN7fj8T_KiMi4E8amJ-EK2xJ8LEdRip3fY2NXvefczn1O0QYmVNlGddI-69oKwBz66q349Kafxxl2hvSPOXEP2rN9fsVQ1lnkTKqXnfNBoSsq85DyHUJz-4E005VueO329f2ZZZPlJZl62EUTHNzSHplacrcOC_YRaqlpxiLPBzOuozFxyfmb9elA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyKnq7Y2aJsZyj0nPJpNAbod-nKoLUTcazkLmPIcgtN20Mp56KmcOsNk6XCxcN3YYhIYJ24MvccZYyPp5K7cS9BfWi-njxYTsDEIAEKbTla3rP8oqk48qlEENwnuh8KnnI15QFb1ZDuPMmfltuoG24bBTDL2zD1FUvE63cUQlLc2PfYa1h5cEIxPmLhr3IhCy_ogObcAABzdFJiI_a8CAt2IbmRCBWyZtORWFHYck19ixMFMDTS9ba_XzB5oVeySiSkq77IO7i8fcX1wIhcQbl1HsWvbXN5nnB1spZHGgKYRWtMmDlkx7a4R9OAb0b9iityfmsHfBxcBMSi_-JDBqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3xSzT0lg8HzWxemYwG0oihUTwpo_PlUxwXafOij8XXaGkJqpsdyjoUtoStEKJwezEQ_GS2dvy_mCmncau0vpwQK6lnxyQ6tXWXNjmwwkg1UV7xFqwvrCgftujfO0k5y85M-GMr4fbt8IXHwHdblPWT2wPWcjiuyBX_cHiooxNLMDAFGp4E497X1s5GVPBAg_Afgiszp-K7HMJTPHB-4fzqCgl_P2hih-F5M4cy4D7Kh24M3TV-qcmW377OVS5-Clh1gi3pT17tTJzDCwPOV35b8ocpGI-jbvXsreKfuNbecQVMn2CLyoByPHL7WkLKEW3C1opt3DHOCAuO0WU6VDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhxllV6SEUFYM-NeBUqKJxZE4c8pwmEp92fFJllfEIyn8GV6xrfRvkcFPeBYP5pcdNQtYSjfWXuV3-Ha3_rwcBPNBOap3glSkh6Aei0tzn1ZTc8JlmlcAF1Qq4uOfqulb6KseZL_3Js6Pr0msudJtnttNsmAEpEXBqlnIMfFamg4ppXVt37KNqY-tDho0SOWhUdTkNEjGGLk-vSUMVAVnhtdyjbj0LuQ4z_zWD7mwMmL9L1F76noq-YqNPmbYBG3BZ1dZSRXOaq4ntFtnJs_HjPieuddtm-mmhPqWjKYtifTSlaH3sA1HH8K5jchKlYPzk_EA21_KU3mdWLmtgz47g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65208" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjUigbcdUKAFwsqR_BPh-PC6aQZW4kLxhAmCBTDvmo8_s70iiA-Q-JrFbWwK258bLV2HHDYbUK7ZEufPBnq2vAvlALFIE9y6L1m3kR8IBVR_jwSL_koj9OpOkBOB2HOO1k_WasDDAT4x4KgUCdIuW20B5U8FVu5-ZE9gfNP-ARtqytN4xCE1wMAjAgk18569fIfUaPcn8Yx81a7fF906kaWQaDhbpO8pDKtyRetRwVDSFE4J01x0fGk6PEy63B-fKusYwkQ971FSTzYJw_RDpKnbMDbF-TT93Dqx7CfyMtGOBHZ3RGvYdNboYHN3zQCbhmmuzI3rTk26SWtJSnzCmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CITB5Dq0KRKYet24iiZcPuzjFXN4G8oGkn2Qd1CgZvc0-YrUB9Ee0dEyAZ87SnqTEQEz2Qq66P4MvieFh18C9HOe4Ngr_64fARxRlNHLXlOzp88y_FhuhPnA3YFKXecYcHZdMeJQCbEtf60XsT7_8qtXikqGwoMryXoJKooynDVTLUAnJjbvrpWoiWIqGV919edsbpLG6rCnpIC4hzYWu2xM0hPp51s8G5HT99ABuK9I9BlxYCEJN4G53-w9xvx7hfcZVxMYm8EnFPMlEJ1txeg4eeeg67mDbeO4pw95NmBsHPXyEXdvsb9ulLmG9E9QJDeJhuPtc0R1rLvBQibuVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=e5dJbSl1KkjR7ir3WAJGc0Gk7VfFI-MMzF2gcU6wH1RULCYF_qA4Kj2CkPY-xSIjlkJiHFlmKj43NTDcZLhoeXGw0VhRsYjtOr8xQF_Eaf1yHpk_R6WzB2k7Gs_mfUkfh02H0ts_cjCOs1iR7kBziwDe89TL_jkLfJrL4oeqwcTdTJtO4rN-CUOdYHssldfWy6OaH4kcm69VCvLA_BnuVHXqQgu6e_k5wKWo0u3JFB_w-jcWsRZwxLPjWhDZmgXvOyRLm6mdSqoFRsVdFh8Uz9rSdHIcCA0D42pSZf5-x7wPgINSSYHNZvvI8x9EaAwryWsxtESbZInBCf57YmO2kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=e5dJbSl1KkjR7ir3WAJGc0Gk7VfFI-MMzF2gcU6wH1RULCYF_qA4Kj2CkPY-xSIjlkJiHFlmKj43NTDcZLhoeXGw0VhRsYjtOr8xQF_Eaf1yHpk_R6WzB2k7Gs_mfUkfh02H0ts_cjCOs1iR7kBziwDe89TL_jkLfJrL4oeqwcTdTJtO4rN-CUOdYHssldfWy6OaH4kcm69VCvLA_BnuVHXqQgu6e_k5wKWo0u3JFB_w-jcWsRZwxLPjWhDZmgXvOyRLm6mdSqoFRsVdFh8Uz9rSdHIcCA0D42pSZf5-x7wPgINSSYHNZvvI8x9EaAwryWsxtESbZInBCf57YmO2kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIRaRqIzWL-dPGSTzojJCjm_vrRv0noaxW3OYjaJX2AIBF7UC6ePVfaWiSZEg2GF74ElAUAKyRuUGQN4hEtr27nDmON5GS2bzFQAoxQceqN4wS7U73Geuxa5fJbqsjlnb1VEQj8fjFtEk3J8K7Ux0_ur--EIYO6wfLERp2Ysi78GYisOkTa3fVAw-uIQqyDTBo6OLr5GjhL4fLnWZUe3CmPMKTeHNDs8wc0aw3zVLPbXF8yQ4pxQRoHzZcUfyZz_HrDf-Qty-AYwDI18niOvUhUUtZI-GUfqS6FPFwLnS8Ps4b9hsqC68YV7Harr_jCAjZa9Aj2NTWskeO0SNZ2JjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9ch0TXlmBlAxD550Hoy6JtCJiwaoUbaZnJCsZh9zxcmEzDxslRBCtmTB6GZzgMOEHw4qxgTuUimz13flzWbeyQZ2jREWkQ1y-9abyOAZ2sOSXcqhkcBoAfeGuXlmbvi2Od_MOWxBwTQXM6TvRhLw7ZNe4fce-278YFdVkKXl9P9KKeYCtVLz6mCh7FQOSfVfqyT2yDwltMd3NFETMtWr5dKYoX6EOvLGe5EyiM9habXdl-JnyAdBp1huCCTcDODlfRmx90KnAW234tu5DTkbPsM0xpZd96QO0HwCH-2oHPUxz7a529l7bZSjAfZNmJXqpju5njF3VVc4m29GvWxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HaYhVCjtcFWj46Lt-VDElFHVewPaXwXwjLsDs1vXOfCw11Iqch-phFjT7g51uorJ4bKtMYjfDnMSt3WHZbHMYaCmhi562uqhd-QrH_g0arZSDuN2kMKK3hDbXB6EKTSuWTK0wyEBAdIRSXqDMQ_Fu7-kF-0lCpUcdvi1p1xifTBQYsIP3KXdpZlQLw5fv9jE8ctHpEXYsX6gR9my6v0ELUpsbrUUKsVGSkIFNMgpe7z1FTCWR9metQySq2CiMiT3ZMrVzHNSRgrkkOuGU3Jl2CanuCY6l3YdQidDqODXpBCq6efHKWCEGY_LD4cHXEjuBjKhn8QHwxFfrxly6YSP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-fRhUhXmtDv2qlu2ZzKP-rEQGzCXZLxrdhqo1saxD5ySN_E5DakLgUTQMMIMhkhVVDOJOv54raPoNmKsKuZ3ZtBXSlet1WT2DdRWeHqlprKqvhc8Y65SJRfE582hk6ntcMZf3N2gtpcfx-59Bletn6KEVt0jbMmMeLaiYiV0V7EIBZYLLKjBBIXS8ZrIHCnwlwRNVmO6eVhUJRCoJ_gVcgEc7vKZMiE_UYGsNKgnY_ROGSo6q6nHmn7P0XQn0XKHcSgKTakadlHVyw3RZV8enbWx_2kjSkGCdIYecvWiCHUFk7BIJaKFNqTKXP6yGYPw_0KGYVxYrvx9lO8syFp3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=rsqITjzt4T3MkDtDZIGnX9ruFkWdl7bEIWNzkB52QDYns-NtLeoic0dDT3O75SnpI0pQUnsrchlnREObbfg99E8HM2HRTi7pirG74zBogt3xdwHd-d4sR5uCiWN04CbhSsBbzlzjRTe3IfiL3XBiUNFkA-a-tUus96Yh7iP8sC4vt-cn0sNQdoAC2mSSq1GsYE6mVWJZn8qHL7gs55M-fZsOk5FZnGgHkhdbrhfekq42tHtEQiW_4knXphTUeoeanvnnzWUj5OgmoQXytGVEMZ8GTeCRQw88QN3Xj4PjlzJtc2P52OLuelt5h4zrhBA-ruSQp14bIIS8YHG-Dn2mWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=rsqITjzt4T3MkDtDZIGnX9ruFkWdl7bEIWNzkB52QDYns-NtLeoic0dDT3O75SnpI0pQUnsrchlnREObbfg99E8HM2HRTi7pirG74zBogt3xdwHd-d4sR5uCiWN04CbhSsBbzlzjRTe3IfiL3XBiUNFkA-a-tUus96Yh7iP8sC4vt-cn0sNQdoAC2mSSq1GsYE6mVWJZn8qHL7gs55M-fZsOk5FZnGgHkhdbrhfekq42tHtEQiW_4knXphTUeoeanvnnzWUj5OgmoQXytGVEMZ8GTeCRQw88QN3Xj4PjlzJtc2P52OLuelt5h4zrhBA-ruSQp14bIIS8YHG-Dn2mWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPbvVvSS5-pd6XMphfRhOlkDFLaAK-PDehdvSitZJjiD8l6sSDyqxUry0y4j-78kQObuavcCjH9PJH85WvJNDWChWqXJNutisZAU_jeX29LbUbBBdRm3C5J4NuuMBdvPkxl3TSRlK_CaYD4zU5L2TssbEDl3BeEZhLx2eTi2cRfoaWXIPZmg5Fa09l3C2kab3eOvDpPEjYstjO_AczaMHVL1ntn5qm3yN4t2e4mgXQ9jeSyVb9uEGotNDtacB4caiV2jBnsQ-b1sFpis1K7dM3cjVxAzPT0IpxNoUzMyoFoouvVLMlFCKL-hiWKTiQlm-w5lvpT3RBHw497Kj3K7wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=XMO0tZr1_EO8qfLtWmx09KLFgUggxTUYfmfuDjtTj6TuP3T2irIUDk5XTJ8_Xu7roTthe3koDGBc1TIN2kZZVdddVBfSnpz7oAtXFZs7TCYeGodSTg5Z8x0xsGOQQmBoi3Jq6Tk-aLWHxUwmY9Kg2lSudGtgbonirPg5TDqGEbR5sBrKyFQY8sHFw4z7aCOGHS04kt2qNi6qdmai9kw3rRdUIpjj-v3E2M87BXnaTuSQu7gruWbO0oEoqT77lVoJugErSnlpiEX9vdFQVAJ7vfTr267u6ZnPoxaZkOphSdOv0PhWm7Hy6XxkX-jzyEuegQ_oHYq_BcBUep8xX18erQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=XMO0tZr1_EO8qfLtWmx09KLFgUggxTUYfmfuDjtTj6TuP3T2irIUDk5XTJ8_Xu7roTthe3koDGBc1TIN2kZZVdddVBfSnpz7oAtXFZs7TCYeGodSTg5Z8x0xsGOQQmBoi3Jq6Tk-aLWHxUwmY9Kg2lSudGtgbonirPg5TDqGEbR5sBrKyFQY8sHFw4z7aCOGHS04kt2qNi6qdmai9kw3rRdUIpjj-v3E2M87BXnaTuSQu7gruWbO0oEoqT77lVoJugErSnlpiEX9vdFQVAJ7vfTr267u6ZnPoxaZkOphSdOv0PhWm7Hy6XxkX-jzyEuegQ_oHYq_BcBUep8xX18erQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
ولی اونا میگن شکست خوردید! این واقعاً چیز بدیه برای کشور ما
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqJq885jv-f5hz2DEtKEi-XwWIN_SD4nGio4YFjWEMlo3cenqDCrrxp0jNwAiPgNPoaswOpl7jHlsChBbC57eiWMl1LnQIHa-6rrlYLNlxq38N7A_aMjUQYcvzTZ7zGdSPYx-aUfhvD-O03U6xbwQldh2-4vGNRV0HiRi1IsuxW-b7FExXIfN9EQCI-_wtBTyY6Fw1_3GiRx1wY-bX92cdNyIVfI_3G3QGvLJK_eEw_ncpUrON_QBO5_Ru9jAgZKNIqozuCkvptSNFGvoKQiv47q2P6XrrG1115cbU0lpprXDNhnS9K-U2yXOd2XC-3CR0jg2DxvrY3jRnoWcNTnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=eS2u0WCDvDz77zTDWOfxkI-nDlZyX8fXodXkSisaR67ByhqqrQOCsjZk8_Mnxwv7y5Am7E8ibay_m8kR5MAc-2Rr0gpkEj1TQ4FPmlP-YX9mfmqK10XaJKY2UrOfTtjCU8YUPUHDfHwrt-zSWCHgGDbnpfNBbxjDXpaE2qMcT5E0B4MpZ4owThLoN-S52AINuHrX49RRFaGj8FYNXdf40YlBp82EUxlUk5r8_AFf2jUIaEUfuZmN68_kqns1SlRmmweWR5jN-SplWs8iAauBJZJbnbyOxLGr5LBZGc30VoWz5qWbhq44IoY3ejvCkCXRsRwlx10cfxcn9nyc2WyOGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=eS2u0WCDvDz77zTDWOfxkI-nDlZyX8fXodXkSisaR67ByhqqrQOCsjZk8_Mnxwv7y5Am7E8ibay_m8kR5MAc-2Rr0gpkEj1TQ4FPmlP-YX9mfmqK10XaJKY2UrOfTtjCU8YUPUHDfHwrt-zSWCHgGDbnpfNBbxjDXpaE2qMcT5E0B4MpZ4owThLoN-S52AINuHrX49RRFaGj8FYNXdf40YlBp82EUxlUk5r8_AFf2jUIaEUfuZmN68_kqns1SlRmmweWR5jN-SplWs8iAauBJZJbnbyOxLGr5LBZGc30VoWz5qWbhq44IoY3ejvCkCXRsRwlx10cfxcn9nyc2WyOGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=nyR4d239nDMZ21zs4WG-VtPduAml-pOfoq26BY42ydPqXqL5MQJ4cEz3UaHKtDeehsZkeQMmLDxRwGFJi24hri2gkhw3P7VRK9PN3QO_1Kr6Ag6pjAc1jsfbQgZihni3BpzQLZVOiyMFunw7O4SVlXVgiuohcvGCor4-5TF_Fd35IcMBXt-Q0Klkno-3B5QV-SDZfFaPWCU25E2Spwbc0_5c7sTuV1XoTyd_WGMXtIrmaJXiyVuCWmwa93vNY1eh7Cyx8m6jwzJe1kTi_MF9O8EZGEAfgFJinJqZE9eGHM8a3WGBD9XFZ1w_VuIsR4aGyqX0WHulFNg4ZZPh7yMy5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=nyR4d239nDMZ21zs4WG-VtPduAml-pOfoq26BY42ydPqXqL5MQJ4cEz3UaHKtDeehsZkeQMmLDxRwGFJi24hri2gkhw3P7VRK9PN3QO_1Kr6Ag6pjAc1jsfbQgZihni3BpzQLZVOiyMFunw7O4SVlXVgiuohcvGCor4-5TF_Fd35IcMBXt-Q0Klkno-3B5QV-SDZfFaPWCU25E2Spwbc0_5c7sTuV1XoTyd_WGMXtIrmaJXiyVuCWmwa93vNY1eh7Cyx8m6jwzJe1kTi_MF9O8EZGEAfgFJinJqZE9eGHM8a3WGBD9XFZ1w_VuIsR4aGyqX0WHulFNg4ZZPh7yMy5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=n9RZyw2xmzsxGIsqPL4AXO8NGZBNhJIfzOAZ4O7dQIgR92di6U85F9M5LXkJHJweO6YhAUZjb4XDmXcM8I1lDL3KzLvKBPnLkorXnoxS9d5N0rO8vAnbiAxayEsjJ8W6R7_zB0p-s_LkQsofIV-Wmv69aDtRtgmh3xOu3JUYjchdn4CeFZU_sl6tuw02Y9wLybkW0ZnMufnbkYcr43M-3RsfwHJtsF2aAlX9qbF1ATE0LRfM4bcxjWnvLNvTtS7tEKfS5Dqhj_tVunL1_xlGDqGpO_S07hWkcrxyShfE6ywAg7VKCg4UabCBjQXk2o6uST2cg3sU0y4Gvw9jewX7bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=n9RZyw2xmzsxGIsqPL4AXO8NGZBNhJIfzOAZ4O7dQIgR92di6U85F9M5LXkJHJweO6YhAUZjb4XDmXcM8I1lDL3KzLvKBPnLkorXnoxS9d5N0rO8vAnbiAxayEsjJ8W6R7_zB0p-s_LkQsofIV-Wmv69aDtRtgmh3xOu3JUYjchdn4CeFZU_sl6tuw02Y9wLybkW0ZnMufnbkYcr43M-3RsfwHJtsF2aAlX9qbF1ATE0LRfM4bcxjWnvLNvTtS7tEKfS5Dqhj_tVunL1_xlGDqGpO_S07hWkcrxyShfE6ywAg7VKCg4UabCBjQXk2o6uST2cg3sU0y4Gvw9jewX7bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TgbQ0Tss6gylG6wXH5LEaIpghgT5N6NbcLaMSlvuGB_vlFNkcFwVW3I11tREzPNuwP199TKBQWj23owA4l_zQDNNy9Ha0SIupj5SOgxdz3jZAArCt1nwUexlMMF0apV3GVdUGbvV62M_rrIoUAtMJKeygCuooZNimijV1F_dRKqLBz07Qxuoj6-ZgmHKrWZOdQAJJGlxSdB7msJwt6b4CiNBoBjKzbEucJM4APXePW5Wc7dPDZDeOcZ3XLd6RORp0dGfa4yv6et6Bmy0WTOxuvu9fOpLHppLgKxd1mqx5mx1Y__Wn26naLF8cR1H4BsOQHz8wtsDBOBeKvZB8oRnqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LRPseH_P8vXnvQvDLIlUlxHlJvnB1BXmmLyjWVuZt7R-Ow-2ob7xeWo6raAg8f6jbyVf3Ylia8CROY1UWv7LmYzmPdl6dNmJrluHAqu_2gK8N-HG2MKbOZMrpLaFdfD48QIs628HJ3SftUqU5iRizLY8eBGR8EkbFWgD89S1Dc1ON4Xqqk1DGfdae3Vgv1vzIEJ-avB8ylSwzGL0Lo0EhubaJBm9zcuVJRZLjyuSgeOkYmtpO0e9jtT40h-lyIi7kBznhs3QM7OXTqZz4exd_qYd4GaKF_Xefbafrrt1NHtfr2WYOoryqBRO7mZj4EYGAFbt4HK6fEad-c2X00rDjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=oifK8TT7aftqmXq0_v8b7iDTDtQn8_Ql1j9TRNAgGvCutD2YHOmGo-IlqVfL-R8koV5mmYK0D81An4O-BNqYovKYn8uMOjMOYiOP0Je6iBaT50nFkF89X0qFHS_ywYFgpn9s5kMuejQy90ZXheDrQlkWK6b4u2WI5bU-kpwXaiB3xgdyQv7k3jDeM_i0tCSEiqYmFDveWDXkeirzzKtNU8QfSIfCxalnqRBrEBK8t3Sna2i-HmHmK1yapRHzW9IwZIfdYpE28bfIuu9Jv-WP6MSyOs3sm8vGCj2D1sUr6LhcBI95Ih9AcGiFEYmLevziuRbHeYx8uU2bZjdcnEwqbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=oifK8TT7aftqmXq0_v8b7iDTDtQn8_Ql1j9TRNAgGvCutD2YHOmGo-IlqVfL-R8koV5mmYK0D81An4O-BNqYovKYn8uMOjMOYiOP0Je6iBaT50nFkF89X0qFHS_ywYFgpn9s5kMuejQy90ZXheDrQlkWK6b4u2WI5bU-kpwXaiB3xgdyQv7k3jDeM_i0tCSEiqYmFDveWDXkeirzzKtNU8QfSIfCxalnqRBrEBK8t3Sna2i-HmHmK1yapRHzW9IwZIfdYpE28bfIuu9Jv-WP6MSyOs3sm8vGCj2D1sUr6LhcBI95Ih9AcGiFEYmLevziuRbHeYx8uU2bZjdcnEwqbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=tkMJpR4Gy1WntosAw-HW3QdfpUEIXBwTykfnCUHbJXJ8A3lAMHIvgxQ7unHZ07Cg8jHxU0u-R0Kbv4irDbMM7gb6kb7zsLEZjxRpvfYgHCtTzhCsaLJBq0YEi09SQYDfmbHE6bV868Wqhb81aYI9X62OLUd44emh2vuX6ot_GUGmvd1nfRjZv1L61qVAckSHMNjRr_P23oNlgeS0FiEerlNt8MLajWvOMVX4nJWDr1vUJNfHaDf4w4rZcrYpzfKBY3_YbASH5z1PAwWhuopCigtLD-ewxbJUATeVfHC_Zkmw2sFG0PmhRYm4Jz1es17iYQsslp4uLeWF6eZ6bBe5lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=tkMJpR4Gy1WntosAw-HW3QdfpUEIXBwTykfnCUHbJXJ8A3lAMHIvgxQ7unHZ07Cg8jHxU0u-R0Kbv4irDbMM7gb6kb7zsLEZjxRpvfYgHCtTzhCsaLJBq0YEi09SQYDfmbHE6bV868Wqhb81aYI9X62OLUd44emh2vuX6ot_GUGmvd1nfRjZv1L61qVAckSHMNjRr_P23oNlgeS0FiEerlNt8MLajWvOMVX4nJWDr1vUJNfHaDf4w4rZcrYpzfKBY3_YbASH5z1PAwWhuopCigtLD-ewxbJUATeVfHC_Zkmw2sFG0PmhRYm4Jz1es17iYQsslp4uLeWF6eZ6bBe5lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYUFsECQ2znPfsbo0Sl7meVOn16IMTZximwjh3FMktwBmaKRXO87VNK_HRorDj94bvnOErvcI6lm7Zn0bvE7Nc4PSRHFp6lR4e4X9x9laxCuYYy3dV228dtCxcuA2qCma0U5lnHaVnJ1V6BBhuXuT0N-ItLPO40IIPoHUEX5PcMn15US7BbT_6YOuCk79HX4au-aRuSOH5ydOXEYN8TjJdB_xFbrhY6tVIAaKl8utokKMGIFSXZd6-mpbEF0RsWGALwGAhzoTkcyYdhZX02qp6I8r2ilptLYzxnETM-4XZrKgt9FciCtBbihQf_f1tpn__l47Ehe3ZREpP5UKhrGUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qqs1FpHzIYf9zWGIugg80xzRotIkOT877hrnnLR5LXW32I5TtFAoIz2PTkA_orF85hR8WD-z4cMM8nAPTvj8Yc_jPA-CSZudIn2FZuPdXe6dJfLzhuABRiYH98pVsqYDD_p9DNwydsvulJqM8Z-jbsHHzOPkPDaQ2lb3dM4gzMU-CNoC6YmEx19fEwAJ8a_5JZFxDnMiXAwnlKe-d8olON1YfnnWC6NGmkfNVRA-xxUHueLB1PcczAdiRNXBxi-FKfOAEjHQVGQA2nKw8FrNcdY2_pxw3uOMM75CcgsBSz1F1a4nG8MC24IvxJtGd7dr6yvtBc08qsQfzhaQjwnpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WsXFcz8CQ1SaM8OF9-xGYgZFNwO-SuqqKT1ObdZP3BGQETpLWIso1bRyIviuQPNokI0Acn_V2i6N0qSjA2M-HQSmFijR45o8qwlxLRqk5ph8eWXwZmhKXHDi9Z8U2LJ94ktSuaAJ58Rq5LNmhVVguXkL745k6Jo3TWgGvu9yfb7obwzP83Uw-zSKXVg7-4IQs19l5GVUke-taqcHQ6g7wUEHJgQjDJKUGJCzxnyw_ei6kXuoQqLYPx0br3lp5CmuA9a-AF6YFJpuD4G1_U0bjykiNE0TJoQtZel3ycmtnYg0_9EoOAEVxoH36YnbA_6MxFxJcaluNTl6qsuUy4LXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ChnKsql3LCamRwvGXc7ycUlKhh3jKlxz1NRrBNT7Za15t25odVZl3oFlvSk4Sfc_EiCdXiWHeGq4I-68Ku9FUSSn3-9davSXpgi9Zmq8n_yld-KgsXhIx6dE6pjpv1vGB43DdkPCK5f72xLkghGxDpjO0TVqTMWhy_NV-f9yKp3hlaDlchXlKYrFQbpIbkKZhPWA6iqYGPYzxCCBiLFckhLCGV9DZntiEro71azOyN9Qf6g2YrS4-l7rAkWMquTPUIu6YRqYREDlQxT4k7Ni2tYP-TQ5LsK5o4Vza8eccR3F8zIPxlxMivZQNmqBo9p8rV8S4lXERdUetZyTxcRHug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FNx5lT_8K3NVyeHtbTXNIZyEyxRpRf1v0aB2L66QTtvLpGHmJIk_Cn3OlEJU8H0pjnuT4zevX1lo3Cqi2k-gZLefUvfgJm7sfE6fl3x1_8YknpmkSyaUYdoYIif2rmmJke6BvlWC4G59CD_3Vp4GMw6rNbXOMWIXEw0bP9opvtlJ6uoIW40F_MSlmDH01DnSQOs0ZFdFBqzq4UGqXiYPU4C6jgjtaHz6QHlyyOfRhuq5GQNuaHizp0tQRwiFPk6_uks57wuwuGDJrJxqDiYb8LpzN2ToRhRp-D3sCWCKKlD4ReZ6j2BEoBhahVcuLr2-LDYipRMwjKoN-OSOAS-fyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mtwIqesOxerxiKa4YaSwN7Z9r4eKpm0FaxqJRH_9VjFQsoW4POIUbnO41Uki8Jp-6XrUho-3Hdy5UA9HMizhVcJjKCp-_ckSeIs1VZBYaXtILY_mr_MjwEr1fFOucOhFLXRYOz_RsAzIosf64mlwP-Rs6NEUkodcGhn3gXr3Y0mudn4_eQsnrTLR5c-ZyoOsJ2Xv0xj0RphnzPlYuyjQJ5I9bIHfEQXLWdizAUNJuVGsx43EM5vEKOLVwe3jWvC3bMhPjUdVLVsgWJ77THr9Hxfrh55uCn5JpudKQC_r-mBTpc4LFDJYSmSQFi4UdrEvcxCJ4dtUUTCALFaFGDfKsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65151">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=XEpLP6CL87SmshijKm6HreM0RXjiltrB6tGdvxXH1Amq7mT-YVQNLbOLV4z9Dcb4XVdh61EtFH-4NkhV4yZJUFpLEs5tccR2JBfvk1wNsi_28dH6XMUUzJstXB1EM4LccClFQsEXFf8FCWTcg2dSOTBV7i35kK2yAPCILq81VTFeotFRUyidVJgH3RaHxKaPVb6t0utks14vigR56DqvIlxl3r3tb68WnCMpxfYiBSG1mO3YEgsQRmFwZcVsT0S2Qs7eaYjKZ24LelRws993mZ7nFz5bQNeEW7sluCCJGIvEIN_9KuKHrHKgA-YGWRMwHzQ9YsC2w17oH2yYR_sMyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=XEpLP6CL87SmshijKm6HreM0RXjiltrB6tGdvxXH1Amq7mT-YVQNLbOLV4z9Dcb4XVdh61EtFH-4NkhV4yZJUFpLEs5tccR2JBfvk1wNsi_28dH6XMUUzJstXB1EM4LccClFQsEXFf8FCWTcg2dSOTBV7i35kK2yAPCILq81VTFeotFRUyidVJgH3RaHxKaPVb6t0utks14vigR56DqvIlxl3r3tb68WnCMpxfYiBSG1mO3YEgsQRmFwZcVsT0S2Qs7eaYjKZ24LelRws993mZ7nFz5bQNeEW7sluCCJGIvEIN_9KuKHrHKgA-YGWRMwHzQ9YsC2w17oH2yYR_sMyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اسکات بسنت، وزیر خزانه‌داری امریکا:
ما حدود ۱ میلیارد دلار از ارزهای دیجیتال ایران را توقیف کرده‌ایم — کیف‌پول‌ها را به‌طور کامل گرفته‌ایم.
برخی از دارندگان ممکن است همین الان در حال تایپ باشند و ندانند که کیف‌پول‌شان گرفته شده است.
این پولی است که از مردم ایران دزدیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65151" target="_blank">📅 00:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65150">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKYAznlroO0xoMQVMKZiVra9qOUbDSa6T8VbaWlScKVLKo0NBMPZxWL4jc8_XHA4ArkuaksM1SgUzRAnQodELxPZ_Ahjf7tff2rhdODylShdR71UdYmRPf9pyZW5Q94YNNzItXLpN2MRWk-3r1MpMGof5LzkjT7HsUOAdzZZHuhMZZoxcpFnS2KvDm0JFjTlOniPLbsbZCwZ5Gy6H07zpblSkLyGdJEBYB9XgJ6zRMjAZzi0zvArrFbj_JKaDHiDVS5e75wAsmBeE1WOvHdsqT4zD8LxQKF4CiWHpF1PCYm_IEocfcCoqHyKSvDJzgYatVUqiFFfywis-UtHVOaNKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویل بگیر آقای املاکی!!
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ترامپ باید بدونه که ایران به عنوان پیروز میدون شرایطو تعیین می‌کنه
نقد مقابل نقد، نسیه مقابل نسیه، هیچ مقابل هیچ
البته برای موضوعاتی که مورد مذاکرست نه آرزوهاش.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65150" target="_blank">📅 23:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65149">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_woaKQcqVuJKU6C74lRZrrvSxcJWZGwwRAg0UuIzVWhnhqSLR4l1H0toArd-YvWF3nu31CqL0Lb2_QJRPGqaSutuAuxQwqdo3hSHmcEMMDOHxp_mz-iRmZ4HNCmGacSAVNixGMoowzA9_sBp109XfLFCWhwQ_pr-p2P4yEoa-moKdr06RuVVAe0nAZz4cdG1UEjQWtypgknzvF1lnzK_LbLMRr5mVW7cGexXgG-zAazuxVwCMcvCf41BLgavLg2ijOaBrvcOJX542G-rdU04fpXfOw4L0hFph4HHYBn5rrgBAGffaU9EF5Z2DArszJ-bhieeVYo5vzlnnG_dyD8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمودی، رییس شورای هماهنگی تبلیغات اسلامی تهران: ستاد آماده‌ی تشییع جنازه‌ی علی خامنه‌ای هست و میخوایم با جمعیت میلیونی برگزارش کنیم ولی زمان‌ش هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65149" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65147">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
گزارش فعالیت پدافند قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65147" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65146">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
بقائی، سخنگوی وزارت خارجه: در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم؛ مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65146" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65145">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خبرگزاری فارس به تازگی اعلام کرده ترامپ مفاد توافق ایران را تحریف می‌کند.
او ادعا کرد که ایران موافقت کرده تنگه هرمز را به صورت رایگان باز کند و مواد هسته‌ای خود را از بین ببرد هیچ‌کدام در متن اصلی وجود ندارد.
ایالات متحده باید فوراً ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران را قبل از ادامه مذاکرات آزاد کند و آتش‌بس کامل در لبنان (طبق شرایط حزب‌الله) نیز الزامی است.
این توافق هنوز در انتظار تأیید نهایی در ایران است. منابع آگاه اظهارات ترامپ را ترکیبی از حقیقت و دروغ توصیف می‌کنند تلاشی برای ادعای پیروزی زودهنگام.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65145" target="_blank">📅 20:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65142">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T05_-5nIHscmm1Pxq9f_fI6J8yNwZzHMwaAjukzhBdqcDkmgudgYvXcCs51cBNXVcYCb4mPOgD2WPQ4vsF1K9YwTSmdeQkGy1q88cbGRcVFOv_Hp_HzLRxbhZcL86kgXa_tl7q1NK0FtuzJtlJqMnVac2w9-g2hOP5tn8w6ouihnEtpeMKZQ1JRk4bZNNIgDMBYPrU9r985QiZb_Ulr2uRLbxv-l6z70MDgFfwYg_DGo14r3Akl86YBLd-j_xnC-gZFf-HSs8T_i9jnGwPUMnknQ1otDDll1WWsELf4PQMhxUjF5J-LyHYBPR1yEKqurgqJx4sHOb2PpwzfBL7rLMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65142" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65141">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⭕️
🇺🇸
🚨
🚨
ترامپ در تروث : «ایران باید موافقت کند که هرگز صاحب سلاح یا بمب هسته‌ای نخواهد شد. تنگه هرمز باید فوراً باز شود؛ بدون هیچ عوارض یا هزینه‌ای، برای عبور آزادانه کشتی‌ها در هر دو جهت.
تمام مین‌های دریایی (بمب‌ها)، اگر وجود داشته باشند، باید از بین بروند. ما با مین‌روب‌های قدرتمند زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز فوراً مین‌های باقی‌مانده را پاکسازی یا منفجر خواهد کرد؛ که تعدادشان زیاد نخواهد بود.
کشتی‌هایی که به‌دلیل محاصره دریایی فوق‌العاده و بی‌سابقه ما در تنگه گرفتار شده بودند محاصره‌ای که اکنون برداشته خواهد شد می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین، زیر کوه‌هایی که عملاً در اثر حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند، دفن شده است، توسط ایالات متحده بیرون کشیده خواهد شد کشوری که طبق توافق، همراه با چین تنها کشوری است که توانایی فنی و مکانیکی انجام چنین کاری را دارد و این کار در هماهنگی کامل با جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام شده و سپس آن مواد نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی رد و بدل نخواهد شد. درباره موضوعات دیگری که اهمیت بسیار کمتری دارند نیز توافق حاصل شده است.
اکنون به اتاق وضعیت می‌روم تا تصمیم نهایی را اتخاذ کنم.
از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65141" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65140">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5e51deyx4gOKxas_DXhKOos5wCzTMFlyVyxUbNGm1UtRZd_dSaWwLMs8XpfOas6tN0q2vWBadwPD0tRmAzlr0PPLLM_XoYxeKqYkUlNKY4qZsHhaQBXMdxib620m8UOyEMSZSKNOL3APAOAIQQkfqv_6zOyoUobecSXp7Zm8Ooc3Z_uN6JaAggB7O95SnXL9wBxGmm-lCKarNGIacaWnlZhEyeQjYPjyt-FTUFEhCSU-BmcJmPxuZ5EC1xFfA-owZgE7c_4J0onvIn65Zjyq6KixtqizdA-ffkLb_ovXr29CiGEWQQ8sDw9lneP5BlXwU_ALwzlS9-Uw1VHXdQ4kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی مشاورین املاکه
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65140" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65137">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WvbLl44Vv6A_syXTuoIu8ZJxzK1WffOhxRseC-CLMPb3JEGNf1ejPvHWXFHT-lA4rDJmHUmUvJNbVVqgLz3QM4ihjZpxbFT2yb7PNbfpJWp6-lJ36kSZWJ7RzFGTPz8eFf739rVC9niLgcDe4QTbNLF_O6fcKIy4f6uNoRBxRKeXp-Eytc2v822wlsme4YZezcBI6yJrgsxH2I8zNqSVNSWPHpiMGoglGJHui33HFUIo-EOg7VzgB1ljyXeUznpWeELzWnDw3PHFO1ua0xzDHm2R8utiRQ-hu618QmNy9Xv2_8T182GqseVEE8EnArgywD4kR1povuZ36NG4PIPEyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نت نداشتین این دوتا شده بودن سمبل شرافت و نجابت حکومتی‌ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65137" target="_blank">📅 14:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65136">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMwM1jONvKG4v7usQ86ARLl5ScdvgBECI-TbZnpP-UtusA71vdFhFVEqAb6CdEbPcXHcA_zYnmxl4zliX-Rt3ZgL5ztzn53jcRVbFrIt_xz-RtuZutjlhNA0H12MX56JrULozznP3v2fm7VToUOIwmG9MGsWcBSuMr3GBdp7xc0uL5mkgtygS6L8Kgag_I9un54eAzgF9ovQ4lu3wpDsjIAeaRKHNConFgW5UAYbS9lx5MA8mt8QehXZoI6AKpDT2aSo2v1nCZ0ov0ZGt13z0NMwltsrFxjhIx3dXDuH1jwTklFW-qOZIB5PQIKJbmiohjArSOE5u4-RXLWx6Q5rjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های حمید رسایی تو کانالش درباره چه کسی شایسته جایگاه رهبری است با آیه‌یی از نوح و پسرش که حتی صدای خود طرفداران حکومت رو هم درآورده
خیلی‌ها میگن مجتبی رو به پسر نوح تشبیه کرده
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65136" target="_blank">📅 13:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65135">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=Mj_7kd4az1koK0iFWwf9lmS6xtclIEMlSz97spaye_FsgzXgMb7gHD6n9rSYGxgP8oEl7YortmqhebjJU396l_V39nZhxdpuKBt3V9u8HNqk0457DB7Ct6qN2S2ZYBHNtYQuSHotHNG1GxjUWkpHYTRik55QoVp-m-Hy0w8vBysUaVQdRHVex363BBQfQV5WEMKw0UKkGWIX08Beu2OfLKX6Vr1DGhEN8rHi2I0Zo_IlQPzI4tTCOO8DDhqXhkNQ02dQnBCl_z8IdPIKxkAP97mAAQfMydpC7seEuTbI9cTSeDXmktmw7Vl52c1aZgx8VV3jSjanbT8ZP_EQhBuYdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=Mj_7kd4az1koK0iFWwf9lmS6xtclIEMlSz97spaye_FsgzXgMb7gHD6n9rSYGxgP8oEl7YortmqhebjJU396l_V39nZhxdpuKBt3V9u8HNqk0457DB7Ct6qN2S2ZYBHNtYQuSHotHNG1GxjUWkpHYTRik55QoVp-m-Hy0w8vBysUaVQdRHVex363BBQfQV5WEMKw0UKkGWIX08Beu2OfLKX6Vr1DGhEN8rHi2I0Zo_IlQPzI4tTCOO8DDhqXhkNQ02dQnBCl_z8IdPIKxkAP97mAAQfMydpC7seEuTbI9cTSeDXmktmw7Vl52c1aZgx8VV3jSjanbT8ZP_EQhBuYdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماهواره فضایی شرکت آمازون دیشب حین پرتاب به این شکل پشم‌ریزون منفجر شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65135" target="_blank">📅 12:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65132">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiD4g9mj5biuPouRVhKazUc8Yu0xkA6QoDmcNw88_W0xuXcKzVFi7G8i-BZMtzBIFDn3w4HUzhAQFcknAWbC_CkImscpgRSvTXFNrTITd0JRob6Ov4D8lHU1XaWSAIDhMuwwmrLKcjsIEBbro9CQWeth6OaWFHDH72pXZjoc5wIu_HI2VS_s0q66ivVO3upi3QSvKjUT3Bp_1ENn7LB_5hxzSNrLP1JZOPDIABjG_3FggGk_A3T36wzk4_awp02IupeHQDM6AugNpLc8kJSDQm4LqYp743ymiz8YLVW0xhJgdJE2e5Qi4KOXTezKtCsAnjQzKdrdbXVrWDwTjszsgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
واشنگتن پست: دولت ترامپ داره به اداره چاپ اسکناس فشار میاره تا ۲۵۰ دلاری با عکس ترامپ چاپ کنه
قبلا ترامپ ۱۰۰ دلاری های با امضا خودش تونست به چاپ برسونه و اولین فرد درحال درحال خدمتی بود که این اتفاق براش افتاد
همچنین طبق قوانین امریکا عکس افراد مرده میتونه فقط رو اسکناس چاپ بشه و از سال ۱۸۶۶ که این اتفاق بی سابقه‌ست
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65132" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65131">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=qzziMPbcWGMOeh7p-MgsSzPQl93R9i0JNkb9-qMKFBIu7BApxy5jHBrrUY0E0ni1HV23DU4gZyKvzU2uJeNomJG6IcGZ8rp6WomAuBJGrpxnNyVATKKGfOQTC6C-lMa4Er0wUJ_HeOqzoyYMzwXaABHUWiVViZgrJaSUk0NCFU16xSpuOVhmg_0RYbv23uDusT9_LFHk4dT0Tl3y1EWl9qbHMfG-cvanYoR4ytFfMfapFqG_E3tUgOeYX2D0jf17ytJMNYHDgH0BDpERLtRLUNbIjOQmdHn8t0hpkzfMsaRTieQ0Tml4M7LNc3E_r3CMda5Yg3yzHgfbcdWXZqXrGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=qzziMPbcWGMOeh7p-MgsSzPQl93R9i0JNkb9-qMKFBIu7BApxy5jHBrrUY0E0ni1HV23DU4gZyKvzU2uJeNomJG6IcGZ8rp6WomAuBJGrpxnNyVATKKGfOQTC6C-lMa4Er0wUJ_HeOqzoyYMzwXaABHUWiVViZgrJaSUk0NCFU16xSpuOVhmg_0RYbv23uDusT9_LFHk4dT0Tl3y1EWl9qbHMfG-cvanYoR4ytFfMfapFqG_E3tUgOeYX2D0jf17ytJMNYHDgH0BDpERLtRLUNbIjOQmdHn8t0hpkzfMsaRTieQ0Tml4M7LNc3E_r3CMda5Yg3yzHgfbcdWXZqXrGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: کشور‌های عربی مثل امارات و بحرین و مراکش برای تاسیس دولت فلسطین به پیمان ابراهیم نپیوستن بلکه چون اسرائیل رو یک متحد قدرتمند علیه ایران می‌دیدن به این توافق روی آوردن
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65131" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65130">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJTEpfwxirBVprKKmPSPg2LHzRh8YhJRNMoMIL7Z12bH7eTjN0eK3FPk3-iGVRziUEb8MucZnz0lgJlcOL5CAT39vqsohdUmmgX7r7iq51ax9l3wr-mQiS9TNk2vEQO87Z_7cL67d0n7HFqCEmauUBB9XXxsHTE29p94NN1d4NY8Y7p0lMXAVrZQ4n0TH-k9rS8fatrMx5cPRoQrWJGFdrafwmx55giKz-umKaKX2rDWID-Au15HknJbkYRcHu3O4RDY90BdtRqyq2NMSOHIhu-2lQeM-JQ70gyiVHcAEQX0bAb6yr7sinF2oGgNp-aLbpOfXKhc369k1ZdR7XVp5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش دفاعی اسرائیل: از زمان عملیات غرش شیران تقریبا ۲۵۰۰ عضو و فرمانده حزب الله و ۸۰۰ نفر از اعضا رو از زمان شروع آتش‌بس حذف کردیم‌.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65130" target="_blank">📅 08:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65127">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
گزارش صدای انفجار و همچنین پرتاب موشک از شهر جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65127" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65126">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011753724a.mp4?token=qEUBQ5AFLuVQ6SuDb5Y8A01AeDsgLLbY0rLOFx2un7rZ7Ktrzu1eynf3bOZn3yseab46GyJycGo5A2XOznnc04wSmZ_18aUeOdMczw2b9AkqbO-ctf3KpqXzBz9D20hwjz6JgL9OEY_wx24vsf2NIC4ZObRR1Rr7FDGeigcOtl4S0Y-4IcgMmYUE6PoCWAhqvv22WsjNkMgSF5UB9ssBh4P96XKzTRa2eJhfhoECPy-W7rh5nmddPU3EXRqBeliFXz4IVd4R0gfiKC0L-WKYTU8hM3MWg4UEuA4NC-A2mSOBeIRExDUatQbomGJb2qnV1aBdZNjB0AollMMdRbaQ1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011753724a.mp4?token=qEUBQ5AFLuVQ6SuDb5Y8A01AeDsgLLbY0rLOFx2un7rZ7Ktrzu1eynf3bOZn3yseab46GyJycGo5A2XOznnc04wSmZ_18aUeOdMczw2b9AkqbO-ctf3KpqXzBz9D20hwjz6JgL9OEY_wx24vsf2NIC4ZObRR1Rr7FDGeigcOtl4S0Y-4IcgMmYUE6PoCWAhqvv22WsjNkMgSF5UB9ssBh4P96XKzTRa2eJhfhoECPy-W7rh5nmddPU3EXRqBeliFXz4IVd4R0gfiKC0L-WKYTU8hM3MWg4UEuA4NC-A2mSOBeIRExDUatQbomGJb2qnV1aBdZNjB0AollMMdRbaQ1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا کاهش تحریم‌ها برای ایران روی میز است؟
اسکات بسنت: هیچ گزینه‌ای روی میز نخواهد بود تا زمانی که تنگه هرمز باز شود و ایرانی‌ها موافقت کنند که باید اورانیوم غنی‌شده با درصد بالا را تحویل دهند و نمی‌توانند برنامه هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65126" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65124">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇺🇸
#رسمی
؛ توافق موقت ۶۰ روزه‌ی ایران و آمریکا نهایی شد و متن توافق، فقط منتظر تایید ترامپ است، هرلحظه ممکن است خبر اعلام شود
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65124" target="_blank">📅 22:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65121">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=cFo_gkOZlk4Zy_hhmLxjLT_UrLFvxmLQB0uB3tpOOAEv6DnG4WRyeNKnyN93jYMf-zF45Y4eyC0w5zt1qwu8yTFXmuF2l_RDpNvHayOvAf6St-vl1sAKTM_2r6Q9tYF04FwR2RzOdSH4WakhBedBdFUohQWmbjaTm4lHK5GQo8vfwoBpJhsQvc2nWnOM5Ka07hSoaf9mE1kXqD3WPZe4EMrTdu6qYMmz86bd3qTYzEIeeE2PnT-27ICXFYe_C0LL_x6o-WuOBWFVi9DGVBg8lSHOehgmkabEbKv6Uexn3dT_BfKsBQ_edZJFkGLeF9EO5dhXKSq9S2R5s2rPJZAIMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=cFo_gkOZlk4Zy_hhmLxjLT_UrLFvxmLQB0uB3tpOOAEv6DnG4WRyeNKnyN93jYMf-zF45Y4eyC0w5zt1qwu8yTFXmuF2l_RDpNvHayOvAf6St-vl1sAKTM_2r6Q9tYF04FwR2RzOdSH4WakhBedBdFUohQWmbjaTm4lHK5GQo8vfwoBpJhsQvc2nWnOM5Ka07hSoaf9mE1kXqD3WPZe4EMrTdu6qYMmz86bd3qTYzEIeeE2PnT-27ICXFYe_C0LL_x6o-WuOBWFVi9DGVBg8lSHOehgmkabEbKv6Uexn3dT_BfKsBQ_edZJFkGLeF9EO5dhXKSq9S2R5s2rPJZAIMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالی که جمهوری اسلامی اصرار داره یکی از بندهای توافق آتش‌بس تو لبنان باشه  نتانیاهو و اسرائیل در روزهای اخیر بشدت حملات رو علیه حزب‌الله افزایش دادن
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65121" target="_blank">📅 22:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65120">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌ها به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65120" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65119">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⭕️
توییت جدید اسکات بسنت وزیر خزانه داری ایالات متحده.
دولت ایالات متحده هیچ تلاشی برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
به ویژه عمان باید بداند که وزارت خزانه‌داری ایالات متحده به شدت هر بازیگری را که مستقیم یا غیرمستقیم در تسهیل عوارض تنگه دخیل باشد، هدف قرار خواهد داد و هر شریک مایل به این کار مجازات خواهد شد.
همه ملت‌ها باید هرگونه تلاش ایران برای ایجاد اختلال در جریان آزاد تجارت را به طور کامل رد کنند. روزهای ارعاب تهران در منطقه و جهان به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65119" target="_blank">📅 19:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65116">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSrXJpwrU-xm5QOtQ8vRdskF8UoAHSmKlWxAdOIyz6knuBCzU7Vn_c5F1neBHpblh_9aq-YtHr_qmRtAqT0XrFdNMcIgU-gEodg4CfnYMe_bNpXcKRs1lpk3N422f8PMT489PwKBcLPlJG04GkBBXJQhNLZGSCC2AHH7jx3j3SGHhKsCA7NGECVttUH2NdMbds8tLhryxjPUqslvmeF2pQXWAKyTw8omig_OmtjiAZCSZjPvo7xWLd3DYX5cEugF3clvjHUdy41kyeYdGieXKQmSpLFbVhMLvb7wDOKsTRzuety-h2gGaRplriBW8m0h2R8LuvLdRuUgD70Mnnhpcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
آکسیوس: اکثر شرایط تا سه‌شنبه نهایی شده بود و مذاکره‌کنندگان ایرانی بعداً اعلام کردند که تأییدیه‌های لازم برای امضا را دریافت کرده‌اند. ترامپ در جریان توافق قرار گرفت اما به میانجی‌ها گفت که «چند روز» برای بررسی آن می‌خواهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65116" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65115">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pezAZupYsQSF3BzphVrhTTZyeOz6i16WnSoO203C1o_ULGjMQJsGEmTD4FEyIfLnWXyXRsWl-JhmzY06z-yS1SwoL2KR92BHeboQv-TKnnPtBcdf-Hb7k-r37NZk2FVy6QsrtRsKu37lPmrxifv1IRN_40PJeBWhyr7OuNMxIE0h3XGD0-9zn8Nnv6H1Wao2OZiaWm-k9TuSJXkkMmYLY6FzMLhM8wxDI2V57rvJUAQCCEKX0vndMxyST8id8tDqDU5kF9lYD_VRliY5AICtXbFjCKhHjaKYb2Je8x4OkrFb35p1lmiLxWiNCwl7uyqsz39WF42Yfvn4gKAUn3qn6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوارنگاره جدید میدام فلسطین از حرف جدید مجتبی خامنه‌ای درباره اسرائیل؛
" رژیم صهیونیستی 15 سال آینده را نخواهد دید"
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65115" target="_blank">📅 16:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65113">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYvOHKrE32vK0U4AOOSBidBWWtTZAXW5kXhFSUl-cir6GNRNwq00_-No-GDJ5sdvGNOQS8Fdc3gkPATGge6nYN0Y0Y8QxtKrZBRF32Vc_lEtw5ioyDKeiN7bwdy88-sJtvARC8kLCKtqFGEYV3uD-XJj12gWFoIbkvUhheSLShYTxOd-UJ9MTod8FJ229-7z8xq5J59nWKgNgRCGrm1aS_AJbU-rfoVNaL4o4D8507SpbY6EvKHqxZnSEWSBuqtNcZdIx3tUbGarSlHMsbast3WEMvtZsYs0Mgh9LRIUf4ZvxRgwatUUVvnD9oJgXMZe6VfzJI_WpUkeQ8ea9FrfAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
نت بلاکس
: سه ماه پیش در چنین روزی Iran دسترسی به
اینترنت جهانی
را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با
فیلترینگ
شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65113" target="_blank">📅 16:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65112">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حملات تازه اسرائیل به جنوب لبنان؛ تل‌آویو از هدف قرار دادن زیرساخت‌های حزب‌الله خبر داد
ارتش اسرائیل اعلام کرد حملاتی را در جنوب لبنان انجام داده و زیرساخت‌های متعلق به حزب‌الله را در منطقه صور هدف قرار داده است.
ارتش اسرائیل در بیانیه‌ای کوتاه گفت این عملیات علیه «زیرساخت‌های حزب‌الله» صورت گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65112" target="_blank">📅 13:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65109">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس: ایران ۴ پهپاد یک‌طرفه به یک کشتی تجاری آمریکایی شلیک کرد. ارتش آمریکا این پهپادها را سرنگون کرد و پیش از پرتاب، یک واحد پرتاب پهپاد ایرانی دیگر را در زمین هدف قرار داد.  @News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/65109" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65108">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/news_hut/65108" target="_blank">📅 03:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65107">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/news_hut/65107" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65106">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">چرا نت من قبل از وصلی ها بهتر بود، چه وضعشششه آخه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/news_hut/65106" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65105">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">عمو Pishgiri بهم sms زده و گفته خشخاش نکارم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/news_hut/65105" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65104">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/news_hut/65104" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65103">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65103" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65102">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:  @News_Hut</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/news_hut/65102" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65101">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZYEq58_9thTZ89MZOGPzcM1Ub-CvhE2jDNj5xEagyvvFBE6fJZh6fStDtRKIMrd2EIKDMLNDxSLtcGj1iPcl2u2ptz1Rja_YzW8QvreRUp42m2xo5d3rA6zrOeZT1cxLLTwTWYSJuoyCM6U5L-xZgInUdqVJngeFEoqiXCRjJ3RtjTKbveze9_hjTC-NT_fuzp3jV_MMsv8e0UB83MHY5x1B1lBVZaWDQe7z6kuozo7GW-GfAHq08mcXZ7vVlGZhulRhFlwVnXno1osNOPYja_0KExyNWD-FL3kjSpgE7J4ma4wa9V5hBO6xmmcjysExcsg238PZ1FKnHonjOBj2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@News_Hut</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/news_hut/65101" target="_blank">📅 08:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65100">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">امروز ۶ خرداد عید قربونه
@News_Hut</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/news_hut/65100" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65099">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmzMq9ZPw6Jnj3pBUGYqO9T6-J_2L3TX3orehmz6i3rskclQrmrc8EzaSX_MZpy0sYghUWzIKXYtjBT9wFzF1qDzAR0anEHfRNVKKAmKtYBuXmQmKKKU5vFb6WaX3wcnyVyV_nZwcTB2_1JakYGng2MkbIVB_zSxfR0limOXu_TtpLmRvFlVxyNt6dy1RIAsxCzvu9U72310H8p0Wp_jF0oB9CX7A1d4hok4wQeaY9x7842wuQCSTYn4BtC25orb21N0A4hVKW3uesg2XPqidqvL2QJ1VuVGDUgs4iQBvjVjdhRgvGA0e0IxY8g6PDQaBlGved6dan_9HN81bfLt3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها پارمیدا دیگه بعدش آنلاین نشده
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/news_hut/65099" target="_blank">📅 08:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65098">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اولین صبحِ اتصال اینترنت بخیر جوون ایرانی
🫂
#hjAly</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/65098" target="_blank">📅 08:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65097">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">جالبه یه یارو مثلا نورالدین الدغیر خبرنگار الجزیره تو تهران میاد توئیت میزنه همچی تموم شده و فقط امضا بین دوطرف مونده
خبرگزاری داخلی و وابسته به حکومت همینو بعنوان خبر میزنه ینی شما بیصاب شده‌ها به منبع ندارین خودتون؟
@News_Hut</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/news_hut/65097" target="_blank">📅 03:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65096">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ganq18iV9IQVq2L2whwYDS6mymOitR8fLklMhw-5bQXwdmdw6p3siYeaT0V3c4GOO_IiJDMtX5edYnTxhY4EU683rSyK4uKP-1zOZDQc1vxt4XiAHsZ8bp3trGcLskS3y77_RtYfrADyt41zzxZxjWfMWmfPIm7L9gNE9kK8pQFnhE4ARjYNknidZ_DWIzO10i1pLnKq2WW-tHjTolNPw5tIbOuok7qTkwJnkKeIH7EYeh9g0Xv_LCWLEDLI0OGM8WD3QccMCsiQ0z6-DP2oA-bUSfoie-rJK9w0mJarfbfveHpfgQdX0n20r6-UXRszEzQnF_FZFqWzrSWABgku-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  «اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/news_hut/65096" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65095">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اتاق اصناف: از این به بعد فروش سیگار نخی ممنوعه
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65095" target="_blank">📅 22:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65094">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgXb0Yi9vY7IJ8h3esUmPXy2tYPiVQ5FTy9TZPjyEY7v9vm0Qcw5l00CmaiKtZDiUH7I3HwWRK6mnBiKgIRwnql_dOOAhpV7DiPaz1-HkACL4N7XLsksVRJnQES2FKQ82GBvDI5PXxt09CwTjrmh7gjU8XKf-BPCd2Nq9Km8SsBmooe9Naus5s019d8gdhUtpOFGuKyGcGJJirj2deUjb_9CLTKT422cHIrAwU4Bd_ikMiVmNqp1kBdmfuA8qWXKKKBcELYv-JgbpVneSLz_ILBn1LCN52oG4MpWC3uMDuZSq9PEole7E304jQJP9qOXFHww7u0yz6yxe2AvbKWKXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: همین الان معاینه 6 ماهه‌ام تموم شد، همه‌چیز کاملا عالی بود از دکترها و کادر فوق‌العاده مرکز پزشکی نظامی والتر رید تشکر می‌کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65094" target="_blank">📅 22:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65089">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نت خونگی.npvt</div>
  <div class="tg-doc-extra">9.3 KB</div>
</div>
<a href="https://t.me/news_hut/65089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚨
🚨
کانفیگ‌ها و سرور هایی که بصورت منطقی براتون وصله
،
در صورت عدم اتصال می‌تونید گوشیتون رو بزارید رو حالت هواپیما و بعدا امتحان کنید
.
🌐
‌ ‌
لینک دانلود NPV با نت ملی
🛒
‌ ‌
لینک دانلود مستقیم برنامه از گوگلپلی
🛒
‌ ‌
لینک دانلود مستقیم برای آیفون - 𝐍𝐩𝐯 𝐓𝐮𝐧𝐧𝐞𝐥
🚨
🚨
🚨
تعدادی از کانفیگ های V2RAY متصل منطقه‌ای؛ یکبار کلیک کنید همه رو کپی کنید.
vless://392c0d0a-157f-4fe0-b528-11586477cbe0@185.213.165.81:38024?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.80.73:2096?path=%2F%3FTelegram%25F0%259F%2587%25A8%25F0%259F%258%D8%B97%25B3%2540WangCai2%3D&security=tls&encryption=none&insecure=1&host=sni.jpmj.dev&type=ws&allowInsecure=1&sni=sni.jpmj.dev#%40HutNewsPlus%20VPN
vless://e0a98968-eb18-417a-87e7-c8933aac5f13@31.59.40.53:52729?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
🚨
🚨
🚨
پروکسی‌های متصل منطقه‌ای با نت مخابرات:
https://t.me/proxy?server=62.3.12.2&port=8444&secret=ee6f7a6f6e2e7275f22c5421fa893965
https://t.me/proxy?server=91.107.169.174&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=176.65.128.238&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=87.248.129.5&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
@HutNewsPlus</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65089" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65088">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuSCOVqei8gxo_arpuLUa3KzGnlFPWSK9agNRTwOMv4A85jE9TzFmGB1oJzPUwlLLtfwPUKjJGM7Mhn2S6_S8kqSRUnH-L9K9i9ciJeXG7IpHCc5_XCq6Qx1gsjFcuBtXes5Qtvy0SC7CmyX24Dq65-XU3hXDnsKjt2bmwfV2Nxob0i7hlwqrAnDxvNqOWQw_DUndK869daP-BT7Q5UZ0cbsBC4dm8bfbaQOCwjAfuBFHELnlRfnEWLdDbNbp-1922GGOxykzrpKcIKRS1pIAWl5vI8UUvUjgaoRrL78ruqWgZOPRGAqAGXe8AKSQCpJcYM6KtM-QmP3Ebq_sGRKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد عوده، فرمانده ارشد حماس، توسط اسرائیل ترور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65088" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65085">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نت بلاکس: دسترسی به نت تو ایران به ۸۶ درصد رسید، اینترنت همچنان فیلتره ولی امکان دور زدنش فراهم شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65085" target="_blank">📅 21:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65084">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=rHMtO9HwY99D-o0cj472lW0kyw0v1VQ84CUuSpkzEBIZMv2df1bgk27W-3BAOo7tB9zZTdayvrUoHE9SeTYrnsbn36mlL8GDf7ggIio9eImPX8xqVXG1SlA96BrAd50OqRhUtUMYAGMVV6HPz-L3-FXRv_xDCo94xDdWBKhMnkOb2UTsgIDwfqIPks3pdgwBn9f-6HDaUb_8H8K4Vr56wfI_0SAqHdJqrrlb7OZFeXY3koolaVeSchdsMNLpkOs7gY_AcPby_ujuYqUume8GgJsmAIex65gHDb1BLaI4tZXLzxC07ZvcJYjptZmRJJozitakrE7YKzS4gN_8vCteYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=rHMtO9HwY99D-o0cj472lW0kyw0v1VQ84CUuSpkzEBIZMv2df1bgk27W-3BAOo7tB9zZTdayvrUoHE9SeTYrnsbn36mlL8GDf7ggIio9eImPX8xqVXG1SlA96BrAd50OqRhUtUMYAGMVV6HPz-L3-FXRv_xDCo94xDdWBKhMnkOb2UTsgIDwfqIPks3pdgwBn9f-6HDaUb_8H8K4Vr56wfI_0SAqHdJqrrlb7OZFeXY3koolaVeSchdsMNLpkOs7gY_AcPby_ujuYqUume8GgJsmAIex65gHDb1BLaI4tZXLzxC07ZvcJYjptZmRJJozitakrE7YKzS4gN_8vCteYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن  @News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65084" target="_blank">📅 17:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65083">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFudo.</strong></div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65083" target="_blank">📅 17:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65082">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65082" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65081">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMKPX</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeH67SA0Jl0oxbT3epB2jyXu2t1Mrvs8U_Y0Z5m_RrfPR2RhcdYfkbsDOIHqM751mfiNzTdVkpZ7OtX3BzGG48q4hDG0KUf_68rjIK0VLjzgP7ra8FZFw4Zh_dlaKi6ZWGGHpoXNIotJZ92FIiJD5sbh0r5nHNM3-PQRYLeEz9wq9SOl7G_l7t6M67m6XGs7xXdMQrxBmPlsl2lmlH9Xhzfn4buI-inICfvAyYeMbxG_GjtA07k8RUbWrgxz7Cawj3desXGOAbrkXOOotoGAHHYOBY5Awgeb96cdvG4cWMxYq_q71J52VYIrCFfq0-rXaPrp1eN42PuzaD3Fgnmwxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65081" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65080">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmdi</strong></div>
<div class="tg-text">درود
کسانی که نت مودم دارن میتونن با jump jump به اینترنت وصل بشن
ما هم بعد از سه ماه قطعی به جهان برگشیتم
بر باعث و بانیش لعنت
به امید آزادی ایران جونمون
❤️</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65080" target="_blank">📅 17:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65079">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65079" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65078">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYBqc5VtfFuWTCm2mkQGJ4sRkwWBatsP9KSGHf6WAKkYcArE8lvcFd3B8JRXLpDM6g3qsqm6we1NFaSY4eqPfCxZbL8mMXq2lQ_u3dYsnbifSwxrPY3Pj13hJWgd38s9C3LtuEgUto4oWONPYdo-qDx2RP0YsJ-zdTic3VvnO1f9gXAfJHJN8HYSYMQnGveLY45iau6XrJDFzVfRss-VT02IEx2FrFSIeyKC4k4N5A_xj_p4FkjBqxI567rCGNWkPiAoIdws9lj0Ajl7Rf6ibfBS7kSnUSkU7sUmggWDEeXIsypW8BXGqFBMOcRYwypu9jDZHGJMJevAoQB_mYDyXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65078" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65077">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.   این چهار حروم‌لقمه عبارتند از: رضا تقی پور، نماینده مجلس کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی رسول جلیلی،…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65077" target="_blank">📅 14:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65076">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLrsuMJrxzVD8yojrb7y5SMmSDj-eok41P44PGTU9lMgZGG9ePNPZX1I6N3hXJiw47vinQYzmmfC5SRmc7l_4A8LkVlBYGEmbtkAZi3CFnjL99aZFpFKR71sQOy15A2q-MChqvzErwb9WTE7YUQRRLc9FacSt16nSw2ZvQ3aUQMP0K5uWEtCu2ZlhIL1L3qyKWrHx4mJOITzaA-25zy5kQcSvE10qYMzDoB4M6rwB42aWWFa1onKfBgRavTec8ih6D5CpLHeyTzFke5uq5btlnMtnv2vhTMKreyYeCYDJhbdx50fxynmI261ATjRmYq_dRHAjlL7kNiV3xRqydSVNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.
این چهار حروم‌لقمه عبارتند از:
رضا تقی پور، نماینده مجلس
کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی
رسول جلیلی، برادر سعید جلیلی و عضو شورای عالی فضای مجازی
محمد حسن انتظاری، عضو شورای عالی فضای مجازی
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65076" target="_blank">📅 14:33 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
