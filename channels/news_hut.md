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
<p>@news_hut • 👥 193K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 23:41:19</div>
<hr>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65223">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔹
اگر میخوای قبل جام جهانی با بازی های دوستانه مثل رضا کینگ کونگ پول دربیاری همین الان وارد کانال شو
👇
👇
https://t.me/+YF28GUBRSZkwYTlk https://t.me/+YF28GUBRSZkwYTlk
‼️
با درآمد دلاری پیشبینی های این کانال شرایط بهتر میشه  g11
🔥</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/news_hut/65223" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65222">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/news_hut/65222" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r889RVM95CtCiSE635dIcEPW-AGz7nAGtjH9PUgyGLXhPMRw9vXVp3y8ihKWLW7HygpH4pTpNcYUXqFte35Pgj6rUXbOFV9_Gkst34FUZZdk_oGHtFsxop2vejX-k-TOig84FXEbGsvulEgdf4k3Q51JXtEw6PewM-jBbF2UAdP8C1My_yOTs4QXnq9LsHI0P_w3gatL1wG41bNehIjOHRLqmZOXbYBM-5JmqEDZXWC_3784Gtlc89h7Pfq8BXvbpk4nE1fZWXRH1C4udQoJqnJMvlIzpVdjTH2pnZDm4Wa-HNU7MeU_XWsZ4hLWQN8KCf1LOUMBr7PON9ye5dFApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mfd7Ayg99IpKPzw0hSnokEOInmZtlSLYjNJvY3wXSULg487aMpOhg7cmnv-ZJSVq3a4KYHA_KXKwnpKEiJOLaZ6unQP4EM9LzEU-st0UVdoU7xt9ua8Pp_TNGsSDHPzf7t_CBPlPaEbhNjf7Luf6gcZNcJOu6HRWfr_qYhBU3MigLbKdxV8C98FeGIDduBQz6ciTJe8GAJY642Jfuls6tscbSQ-AJ-1QE5r5FpTpY-qx4oY5nVF3ndbeRSPr_wtxMbfRGnvHArtq5Wtc28ruTMuLMho5GxR8dhdbaB3KOwg-P3vLk7wfb-0d3TZs8jFE7jJ48trkkn2lWA4SqmeI7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65219">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔹
اگر میخوای قبل جام جهانی با بازی های دوستانه مثل رضا کینگ کونگ پول دربیاری همین الان وارد کانال شو
👇
👇
https://t.me/+YF28GUBRSZkwYTlk https://t.me/+YF28GUBRSZkwYTlk
‼️
با درآمد دلاری پیشبینی های این کانال شرایط بهتر میشه  g11
🔥</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/65219" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65218">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/proB_W1K51ooyQFdv6dpuL1Cox2qQph4-a3QQaI74Z0cBgyWdlU31wo8hmfjVGWPY3L2c9L07J-C9sLW9OCJyb5w9OKQBCqwWMCoudJpgO4QWsVIDQkTF-8_k9zDiZwTxqNxq11ivCXkE9eOMLiDpQ3cEZzLveTx8NLUUas3E8tlgXQc_eXepoSJjjYbzSore0nXD-0S-ljnPKPQeymveJoPxLY0jJbOZOQLgbHYG-UJ5BRncVt5qA8tM-w1MLrxlkzdR-fm8Ay7GoGGV7MoyuupsXwaZD_J2UZ2wljk9i-jwuW0gjNgqh89QChwdocfhN09aLyNGk85JBWrOiZkiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اگر میخوای قبل جام جهانی با بازی های دوستانه مثل رضا کینگ کونگ پول دربیاری همین الان وارد کانال شو
👇
👇
https://t.me/+YF28GUBRSZkwYTlk
https://t.me/+YF28GUBRSZkwYTlk
‼️
با درآمد دلاری پیشبینی های این کانال شرایط بهتر میشه  g11
🔥</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/65218" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCRfN4yL7UMSfQKN_xBXzfg6n4phYcHswP_ZgeZeCdfP55P-84_CTU0B-53nXLZXHmQ6Ff39eSbAydVJZqTIJeMLGxyqy91Nq0aFJNpjJ_K2iEYL_mnxy0P6XleOuzvVBbSAIRCeNN4Otsq5wlmhe9gHKZQJgwC-bcDCGtOtj3ibYDmI2Y6t0OdKQP3sCQh88a1rMOn-TiBOEDP-XJS9qzgLG_gPixkJeOejZ1ArdEHgHOgW_zTadH3q1htse1UmVvsUUSmgLgwL2rPqfDuumcLqCjQ-_-MnhyOfNoIHkTiFCSLT_Pn5Eh1HdnyruQ2DArgakS16O6OFpRXrWO1u-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65216">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65216" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
✅
🎁
کد هدیه 100 دلاری:
Sport100
🌀
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🥇
صرافی معتبر
🌐
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/65216" target="_blank">📅 21:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65215">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🌐
اسپانسر رسمی لالیگای اسپانیا
😀
مورد تایید سازمان Gambling Judge
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/65215" target="_blank">📅 21:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HKguuF7--CRyLFvjw1K7oqpBt84N7hqM66sbRZCysg_D4s2Uo4KKIsF3x_69HMws5_JkiiMC9kwYY_VCyryFQ0THKupl6xO6sfH1F2rvHDmE5REt2geXvB9O7_QBmBEHwqp5gul6K3DqUCzCC-dZ-J2igknP4uN7fj8T_KiMi4E8amJ-EK2xJ8LEdRip3fY2NXvefczn1O0QYmVNlGddI-69oKwBz66q349Kafxxl2hvSPOXEP2rN9fsVQ1lnkTKqXnfNBoSsq85DyHUJz-4E005VueO329f2ZZZPlJZl62EUTHNzSHplacrcOC_YRaqlpxiLPBzOuozFxyfmb9elA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyKnq7Y2aJsZyj0nPJpNAbod-nKoLUTcazkLmPIcgtN20Mp56KmcOsNk6XCxcN3YYhIYJ24MvccZYyPp5K7cS9BfWi-njxYTsDEIAEKbTla3rP8oqk48qlEENwnuh8KnnI15QFb1ZDuPMmfltuoG24bBTDL2zD1FUvE63cUQlLc2PfYa1h5cEIxPmLhr3IhCy_ogObcAABzdFJiI_a8CAt2IbmRCBWyZtORWFHYck19ixMFMDTS9ba_XzB5oVeySiSkq77IO7i8fcX1wIhcQbl1HsWvbXN5nnB1spZHGgKYRWtMmDlkx7a4R9OAb0b9iityfmsHfBxcBMSi_-JDBqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3xSzT0lg8HzWxemYwG0oihUTwpo_PlUxwXafOij8XXaGkJqpsdyjoUtoStEKJwezEQ_GS2dvy_mCmncau0vpwQK6lnxyQ6tXWXNjmwwkg1UV7xFqwvrCgftujfO0k5y85M-GMr4fbt8IXHwHdblPWT2wPWcjiuyBX_cHiooxNLMDAFGp4E497X1s5GVPBAg_Afgiszp-K7HMJTPHB-4fzqCgl_P2hih-F5M4cy4D7Kh24M3TV-qcmW377OVS5-Clh1gi3pT17tTJzDCwPOV35b8ocpGI-jbvXsreKfuNbecQVMn2CLyoByPHL7WkLKEW3C1opt3DHOCAuO0WU6VDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhxllV6SEUFYM-NeBUqKJxZE4c8pwmEp92fFJllfEIyn8GV6xrfRvkcFPeBYP5pcdNQtYSjfWXuV3-Ha3_rwcBPNBOap3glSkh6Aei0tzn1ZTc8JlmlcAF1Qq4uOfqulb6KseZL_3Js6Pr0msudJtnttNsmAEpEXBqlnIMfFamg4ppXVt37KNqY-tDho0SOWhUdTkNEjGGLk-vSUMVAVnhtdyjbj0LuQ4z_zWD7mwMmL9L1F76noq-YqNPmbYBG3BZ1dZSRXOaq4ntFtnJs_HjPieuddtm-mmhPqWjKYtifTSlaH3sA1HH8K5jchKlYPzk_EA21_KU3mdWLmtgz47g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CITB5Dq0KRKYet24iiZcPuzjFXN4G8oGkn2Qd1CgZvc0-YrUB9Ee0dEyAZ87SnqTEQEz2Qq66P4MvieFh18C9HOe4Ngr_64fARxRlNHLXlOzp88y_FhuhPnA3YFKXecYcHZdMeJQCbEtf60XsT7_8qtXikqGwoMryXoJKooynDVTLUAnJjbvrpWoiWIqGV919edsbpLG6rCnpIC4hzYWu2xM0hPp51s8G5HT99ABuK9I9BlxYCEJN4G53-w9xvx7hfcZVxMYm8EnFPMlEJ1txeg4eeeg67mDbeO4pw95NmBsHPXyEXdvsb9ulLmG9E9QJDeJhuPtc0R1rLvBQibuVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIRaRqIzWL-dPGSTzojJCjm_vrRv0noaxW3OYjaJX2AIBF7UC6ePVfaWiSZEg2GF74ElAUAKyRuUGQN4hEtr27nDmON5GS2bzFQAoxQceqN4wS7U73Geuxa5fJbqsjlnb1VEQj8fjFtEk3J8K7Ux0_ur--EIYO6wfLERp2Ysi78GYisOkTa3fVAw-uIQqyDTBo6OLr5GjhL4fLnWZUe3CmPMKTeHNDs8wc0aw3zVLPbXF8yQ4pxQRoHzZcUfyZz_HrDf-Qty-AYwDI18niOvUhUUtZI-GUfqS6FPFwLnS8Ps4b9hsqC68YV7Harr_jCAjZa9Aj2NTWskeO0SNZ2JjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9ch0TXlmBlAxD550Hoy6JtCJiwaoUbaZnJCsZh9zxcmEzDxslRBCtmTB6GZzgMOEHw4qxgTuUimz13flzWbeyQZ2jREWkQ1y-9abyOAZ2sOSXcqhkcBoAfeGuXlmbvi2Od_MOWxBwTQXM6TvRhLw7ZNe4fce-278YFdVkKXl9P9KKeYCtVLz6mCh7FQOSfVfqyT2yDwltMd3NFETMtWr5dKYoX6EOvLGe5EyiM9habXdl-JnyAdBp1huCCTcDODlfRmx90KnAW234tu5DTkbPsM0xpZd96QO0HwCH-2oHPUxz7a529l7bZSjAfZNmJXqpju5njF3VVc4m29GvWxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPbvVvSS5-pd6XMphfRhOlkDFLaAK-PDehdvSitZJjiD8l6sSDyqxUry0y4j-78kQObuavcCjH9PJH85WvJNDWChWqXJNutisZAU_jeX29LbUbBBdRm3C5J4NuuMBdvPkxl3TSRlK_CaYD4zU5L2TssbEDl3BeEZhLx2eTi2cRfoaWXIPZmg5Fa09l3C2kab3eOvDpPEjYstjO_AczaMHVL1ntn5qm3yN4t2e4mgXQ9jeSyVb9uEGotNDtacB4caiV2jBnsQ-b1sFpis1K7dM3cjVxAzPT0IpxNoUzMyoFoouvVLMlFCKL-hiWKTiQlm-w5lvpT3RBHw497Kj3K7wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqJq885jv-f5hz2DEtKEi-XwWIN_SD4nGio4YFjWEMlo3cenqDCrrxp0jNwAiPgNPoaswOpl7jHlsChBbC57eiWMl1LnQIHa-6rrlYLNlxq38N7A_aMjUQYcvzTZ7zGdSPYx-aUfhvD-O03U6xbwQldh2-4vGNRV0HiRi1IsuxW-b7FExXIfN9EQCI-_wtBTyY6Fw1_3GiRx1wY-bX92cdNyIVfI_3G3QGvLJK_eEw_ncpUrON_QBO5_Ru9jAgZKNIqozuCkvptSNFGvoKQiv47q2P6XrrG1115cbU0lpprXDNhnS9K-U2yXOd2XC-3CR0jg2DxvrY3jRnoWcNTnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=nyR4d239nDMZ21zs4WG-VtPduAml-pOfoq26BY42ydPqXqL5MQJ4cEz3UaHKtDeehsZkeQMmLDxRwGFJi24hri2gkhw3P7VRK9PN3QO_1Kr6Ag6pjAc1jsfbQgZihni3BpzQLZVOiyMFunw7O4SVlXVgiuohcvGCor4-5TF_Fd35IcMBXt-Q0Klkno-3B5QV-SDZfFaPWCU25E2Spwbc0_5c7sTuV1XoTyd_WGMXtIrmaJXiyVuCWmwa93vNY1eh7Cyx8m6jwzJe1kTi_MF9O8EZGEAfgFJinJqZE9eGHM8a3WGBD9XFZ1w_VuIsR4aGyqX0WHulFNg4ZZPh7yMy5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=nyR4d239nDMZ21zs4WG-VtPduAml-pOfoq26BY42ydPqXqL5MQJ4cEz3UaHKtDeehsZkeQMmLDxRwGFJi24hri2gkhw3P7VRK9PN3QO_1Kr6Ag6pjAc1jsfbQgZihni3BpzQLZVOiyMFunw7O4SVlXVgiuohcvGCor4-5TF_Fd35IcMBXt-Q0Klkno-3B5QV-SDZfFaPWCU25E2Spwbc0_5c7sTuV1XoTyd_WGMXtIrmaJXiyVuCWmwa93vNY1eh7Cyx8m6jwzJe1kTi_MF9O8EZGEAfgFJinJqZE9eGHM8a3WGBD9XFZ1w_VuIsR4aGyqX0WHulFNg4ZZPh7yMy5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=n9RZyw2xmzsxGIsqPL4AXO8NGZBNhJIfzOAZ4O7dQIgR92di6U85F9M5LXkJHJweO6YhAUZjb4XDmXcM8I1lDL3KzLvKBPnLkorXnoxS9d5N0rO8vAnbiAxayEsjJ8W6R7_zB0p-s_LkQsofIV-Wmv69aDtRtgmh3xOu3JUYjchdn4CeFZU_sl6tuw02Y9wLybkW0ZnMufnbkYcr43M-3RsfwHJtsF2aAlX9qbF1ATE0LRfM4bcxjWnvLNvTtS7tEKfS5Dqhj_tVunL1_xlGDqGpO_S07hWkcrxyShfE6ywAg7VKCg4UabCBjQXk2o6uST2cg3sU0y4Gvw9jewX7bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=n9RZyw2xmzsxGIsqPL4AXO8NGZBNhJIfzOAZ4O7dQIgR92di6U85F9M5LXkJHJweO6YhAUZjb4XDmXcM8I1lDL3KzLvKBPnLkorXnoxS9d5N0rO8vAnbiAxayEsjJ8W6R7_zB0p-s_LkQsofIV-Wmv69aDtRtgmh3xOu3JUYjchdn4CeFZU_sl6tuw02Y9wLybkW0ZnMufnbkYcr43M-3RsfwHJtsF2aAlX9qbF1ATE0LRfM4bcxjWnvLNvTtS7tEKfS5Dqhj_tVunL1_xlGDqGpO_S07hWkcrxyShfE6ywAg7VKCg4UabCBjQXk2o6uST2cg3sU0y4Gvw9jewX7bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TgbQ0Tss6gylG6wXH5LEaIpghgT5N6NbcLaMSlvuGB_vlFNkcFwVW3I11tREzPNuwP199TKBQWj23owA4l_zQDNNy9Ha0SIupj5SOgxdz3jZAArCt1nwUexlMMF0apV3GVdUGbvV62M_rrIoUAtMJKeygCuooZNimijV1F_dRKqLBz07Qxuoj6-ZgmHKrWZOdQAJJGlxSdB7msJwt6b4CiNBoBjKzbEucJM4APXePW5Wc7dPDZDeOcZ3XLd6RORp0dGfa4yv6et6Bmy0WTOxuvu9fOpLHppLgKxd1mqx5mx1Y__Wn26naLF8cR1H4BsOQHz8wtsDBOBeKvZB8oRnqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LRPseH_P8vXnvQvDLIlUlxHlJvnB1BXmmLyjWVuZt7R-Ow-2ob7xeWo6raAg8f6jbyVf3Ylia8CROY1UWv7LmYzmPdl6dNmJrluHAqu_2gK8N-HG2MKbOZMrpLaFdfD48QIs628HJ3SftUqU5iRizLY8eBGR8EkbFWgD89S1Dc1ON4Xqqk1DGfdae3Vgv1vzIEJ-avB8ylSwzGL0Lo0EhubaJBm9zcuVJRZLjyuSgeOkYmtpO0e9jtT40h-lyIi7kBznhs3QM7OXTqZz4exd_qYd4GaKF_Xefbafrrt1NHtfr2WYOoryqBRO7mZj4EYGAFbt4HK6fEad-c2X00rDjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=OhEbqE33UPAF3SnKr5djIBgVoq9bkHArMnagFEYD2fEadAsC5pHHI_U_NOyN67oU7ixMBwLtzjsML3MTMJotfdBbPm1YgaCwvDXhTttI1psdiIhaujg6_a4sWyLqAVnqUN2WgagOUKk6JjMOTBr89JmDGbhJblz76r0C8-K5-wXSGg750AjHEa90Wn7Pp0tvf9D8cXOPafTHAWxCL-ag3E7vhQF5cBiA_EbEC1VteEFywz7k8XkrBrXb2K6wgpXo_Ho4Y2WIJqovi3wOM2S_oG-TTnffzEImHGvxC7NDeMqDCAeAP2U7-cjfEggAGeYHaTS1Pwg2wuQiLmfApbyIuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=OhEbqE33UPAF3SnKr5djIBgVoq9bkHArMnagFEYD2fEadAsC5pHHI_U_NOyN67oU7ixMBwLtzjsML3MTMJotfdBbPm1YgaCwvDXhTttI1psdiIhaujg6_a4sWyLqAVnqUN2WgagOUKk6JjMOTBr89JmDGbhJblz76r0C8-K5-wXSGg750AjHEa90Wn7Pp0tvf9D8cXOPafTHAWxCL-ag3E7vhQF5cBiA_EbEC1VteEFywz7k8XkrBrXb2K6wgpXo_Ho4Y2WIJqovi3wOM2S_oG-TTnffzEImHGvxC7NDeMqDCAeAP2U7-cjfEggAGeYHaTS1Pwg2wuQiLmfApbyIuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=SestwSDBs5y6cloDEohIkSvBC9DhVLo8dAy30Ib9Wig12roeZy18YRhqNoCqo9uLuXFeAFNiQiMg4DXFF4xlQoNg5Uc2nmk1zEekvb5t1RC-Gts9hvvB8Y0MRIGOYA8BHNcnz9y7ObDxTkqaxPIC698iqXgV06zwdlUNH3yHXn2ZLF1Bff4BZD3yhfuwM8I3O13_IBF6Z73SbS5M8kzsYVthHJxr53NHIJWwgKgLloOr-kXprmWmruB0kDqA69muiA2Giqjs_FiTax45FjIol9KYI_5kfZi9KxcRDt0dsqHcKCidQUcHgfPTOqT8ayCmbBkzJuugY3fUMOIEzxhdug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=SestwSDBs5y6cloDEohIkSvBC9DhVLo8dAy30Ib9Wig12roeZy18YRhqNoCqo9uLuXFeAFNiQiMg4DXFF4xlQoNg5Uc2nmk1zEekvb5t1RC-Gts9hvvB8Y0MRIGOYA8BHNcnz9y7ObDxTkqaxPIC698iqXgV06zwdlUNH3yHXn2ZLF1Bff4BZD3yhfuwM8I3O13_IBF6Z73SbS5M8kzsYVthHJxr53NHIJWwgKgLloOr-kXprmWmruB0kDqA69muiA2Giqjs_FiTax45FjIol9KYI_5kfZi9KxcRDt0dsqHcKCidQUcHgfPTOqT8ayCmbBkzJuugY3fUMOIEzxhdug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctRSXXAvwqNYuFi87X6fMeIqK_Y7UC_73haQv6mBBRc6M95NB8QpTyhwNBQ2vXEd_vvySyMemj8OiAeeSlFTSdHlLGGjoo-MH4d2s95NRfN9creBkGSjq_xaUYEfdTj0cybWCwQYO6sEHCgfWIo3nWoJVSxC8U83yV3gNoWQ-qJUFSg-31-cpAtiYso-DE8WSgWta3QFm4mc75b9-ZISBOBcz_M6BYxPujkI8hPp6GXHqH_IqKMnBiWXU2fSMF-9RTb9m8fm38okJ_Pd2zp8QSGmzjU5xuemc5Rrs0H5jLB7zjQwjxHmqTxFXD7iMM8ZGMak6bx1sF3egMhFJgKLGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekZ7FK2yZzTu91YntGT5ooHygkyjyvnv-tTxBtpsJct3XVMbVcLmY-VQltcaErC-vq_dC0yG0IABNrIS7dKXh6WFxwPelNJYzRM9eHZesi3ZeDcEgDua5XaAhV38OSDPJrSD8JFlZ5LIPO9b5pvhMWTR9UPBdZKHKL-ud8YRvFMJ3JRkd0FMu3D6ZHFqIL4pgnKI4e5bHcqC9JQrXuBxgX6FtmNxmtad-w18RrIMk5Do7MutXe7ArT3bj7eBtUkZ0wdPbRM1MLn6RJYttgufTStD_UhLvjV382S0mwKo0FEUGt6H_2fAiIeOZe1vFM2O9MGjeJto3OC5ezOlu6U3Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WsXFcz8CQ1SaM8OF9-xGYgZFNwO-SuqqKT1ObdZP3BGQETpLWIso1bRyIviuQPNokI0Acn_V2i6N0qSjA2M-HQSmFijR45o8qwlxLRqk5ph8eWXwZmhKXHDi9Z8U2LJ94ktSuaAJ58Rq5LNmhVVguXkL745k6Jo3TWgGvu9yfb7obwzP83Uw-zSKXVg7-4IQs19l5GVUke-taqcHQ6g7wUEHJgQjDJKUGJCzxnyw_ei6kXuoQqLYPx0br3lp5CmuA9a-AF6YFJpuD4G1_U0bjykiNE0TJoQtZel3ycmtnYg0_9EoOAEVxoH36YnbA_6MxFxJcaluNTl6qsuUy4LXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-Tuw6GgY9viI4LAu8Y06-lmM78LuOS9QwH4_yPyjKg0-hLM-Edm053a8t0QpTxJcEUC7-gSLpZ1NAxvJ0F-Ne5O468ZQn6zx-4vfRcMouc8d85Zg6YwtSfLTuMdxcrHe6Couiz94fvJOOnhQbmJw3Ar4GTUhzeOptpWaRb02x6eFbUl4GaC7GTBdnPEwDVzuU9bG4Xb80HyiRLrcEoga8BSxsgFNqMZr7kPUJZgN63eQKFUItTO4XC3ms_h9emrXnamXWCW4JaNbXWiWmL4hukzEwZ85qR-MZTpglYPIaWgtT5HE2fE2pmX-NEjN7wFsT9VphCW5bf2mSPjoVC9sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3cOSVx9zhK4rpw6ifRWFbZ2JCKHO09DPhUUxXZiNDRjC2C_GGLqQx1Sa49YwHBLJNajMrt9_NXREzpzooAFbC2QKSLq5dza9LNQ136pMsjlQ8y0aUvq97d3H_ySHd7oYDjkaGmOoYVArRprVmfzCxDaXTtB-UGBM0AghW44EyCyp1UwRNPD334viUAeEpq1TlhliBL-_MGKYxTNtvXrYe1yFwibjKQejR7eqm_WErhXdwhgsAYl2tINvlWm8CY-Q1aXsccfl-w2MCUSU-WdtYevgfDWTNwLoG67Cgx8S-q52BsnxGwHPgj1oXT2bs44Bu3PVlG7pbYEtEBNrMJLAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a4TJ9oykxCQHrlXe4xvFgBkeH43DacpWOgUVETUZwgLHxNTwdBjjJA0mTMhwRp1Al__wjvdo2e3ydpSbsskpcwCfUHaSwJNtxPiIwGor9Dx9cYPhmlzJHxicWzNUSaKVbGe5eqYXeoMBQ2rZGTd0hbJraK4MgvwxSXZQd958HWp67AGxlRBVuAwmN-BlBIPTbauQfzOV-bpUDdLElOKwLXlOPLGaPXeaBfR1qX3LGjBy6CcJR5KhsYY3koAqGhC_luQ2QUDG97cIQxKLjl4BbYVGKY2IDTOBQJIzhlVBxkZKFDmAQi_QxV9Wt8Ak3fjTmz963OEuRu1KPkhYfvCtFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65151">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65151" target="_blank">📅 00:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65150">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE2CWQle5gkpxNmaqDcsfpqFcqsZcw3yqoxSsB6p1OFtOQGnVHSMSrCR8TTRuOhsdaTgzoOWxCnrfqZu_ZgUO35rDDcaiD7EzI0UxVg3VpJtZpGRr2PuNdOBWURj7TNctTi90nPOoxbJ76nvENHLgakmRNuebCVDpM9pwJG_XUT83ffW9nMvmeiL08zPwHfZWbA5AKFf1kGw-Tk8urTWuQFwPQRWzbhX81BdmHIQkeSQcukYGXPjFBWSK7DnNjVEs0TOE1gv1N8acAxfG3vjoiCcZ5VpmELpkuUBSOY-WIrRh0BgWI6Op3SHuoYqbB5pRMiwG_0F89sdlVAX3SDCLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویل بگیر آقای املاکی!!
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ترامپ باید بدونه که ایران به عنوان پیروز میدون شرایطو تعیین می‌کنه
نقد مقابل نقد، نسیه مقابل نسیه، هیچ مقابل هیچ
البته برای موضوعاتی که مورد مذاکرست نه آرزوهاش.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65150" target="_blank">📅 23:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65149">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBncYjviY5bq3cqmT5RnLfhKCB8iUjncp5zDNero1kLhay9d6kyXtDRiMTiF0TuhvskKapDNL8T14tVn0XyQ_UWnF6GfmlWDtO70MiRHmMg6sImFtQ4MeGCWI0gvI5NMbf5ODN1TKAV4lGDG8HlXA4FIPrC5j0mt5C3rL-NOqrlWcOBqZhGNrux7z8pTwBvgR8oPjHDnZOu66FO8qpfzJQlYN4MmR3HnDc-P5Wtj5sIcfkkrV002NLwLewep5bqCRbxD3Wl5ip4pyjvnUxJLj9tGAOloAh7EDLtYqVb9oacE6Zx2EG65y0fHV5YJT-lRCdI4vzEt7rotTrfIDTP2ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمودی، رییس شورای هماهنگی تبلیغات اسلامی تهران: ستاد آماده‌ی تشییع جنازه‌ی علی خامنه‌ای هست و میخوایم با جمعیت میلیونی برگزارش کنیم ولی زمان‌ش هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65149" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65147">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
گزارش فعالیت پدافند قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65147" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65146">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
بقائی، سخنگوی وزارت خارجه: در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم؛ مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65146" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65145">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خبرگزاری فارس به تازگی اعلام کرده ترامپ مفاد توافق ایران را تحریف می‌کند.
او ادعا کرد که ایران موافقت کرده تنگه هرمز را به صورت رایگان باز کند و مواد هسته‌ای خود را از بین ببرد هیچ‌کدام در متن اصلی وجود ندارد.
ایالات متحده باید فوراً ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران را قبل از ادامه مذاکرات آزاد کند و آتش‌بس کامل در لبنان (طبق شرایط حزب‌الله) نیز الزامی است.
این توافق هنوز در انتظار تأیید نهایی در ایران است. منابع آگاه اظهارات ترامپ را ترکیبی از حقیقت و دروغ توصیف می‌کنند تلاشی برای ادعای پیروزی زودهنگام.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65145" target="_blank">📅 20:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65142">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-9jP7SfyJikOjd2S5vnYwLTg1dW3lhJmjVsOZ9TZ0-khOB_HF9jxbJVSQDx0Mx19MafR1ehkxFo94drKx_d5_yqOE16fl1NuGWLtSOFYz6ueuUBYG5NuVCpjM93n-KOjj2NIn5XYx-RyWmU3NjrPqPaPBxdQn1IwLuDwvBVlyDYpEsZHOEtu1morLWYzOy_s6xA0JAjYDbxtwcGPd2kgos9RivOZj6na53LSxNrexmR5UltxnAWFkDBlN7eDu-x1d9tu0KDigMgPij4ILyPgUezaEf7fBk_NUkBv5GhJWs7fMjtqB4FMry1d7Vrz6exZnNU-qC3FwxCHPBACtSpIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65142" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65141">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65141" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65140">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abbDXlLf2kP_AAFGqagwGRZ9iSldK2LoPEdjv09L1B0FvfoM2lqEE6sXhnolS2QfKH3H5_iGcEravXUobN-8IDckAE7Q8QD6MDWSqSWAFuL3NpmCLEY5Jl-3hmvOFp9hx6Y3T6q4aK9Lk4sLr94D1IyRpBJpCH9bG8El6Es-9SkVxRT1Kw8suqrOOP_-ErjKycItDaskCWs5CbolPTwPFRU_H94T_qlpsoS6vY0K6QwfPnxx5lBtU0Lp2fnUjkBNQ2bhi5oEK7aIcRSxGqJH1eF0XG2wkkMP9l88clbXnVVwrJ5fxXaPiQtO0dpgK-iTTJifT-n4XyF0xSdF3N7PnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی مشاورین املاکه
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65140" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65137">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dgRN1SQcqClZ5nzlXTYKYgH-r2JCH67AGVG976MhmyzBz-o9aCypBxFkO-ubrcc-SWrxqMjZFT3HLqgLkGbyhqhUBT7PNumqLKILn_Rs0MZxeEluaX3fxdOG64QNXxo_Y8BEdXOOmOSrSAvc6md9PSKUu73IENXZOi7nAV3OKGrzTopvQ1j1bLNE2QeFt-AhBUXX8UuemeYVjZaqmq4-nENlaoFiWDqmJDxnI_VQUdiPcP4-nNkoAczrZlr3zFz8U6WpzsQc5utU_F8QjuOjcXYOnzu7VTKNCdlfCyTXdvQb1enobQyWA_XQ7fq6N9-MxSFdWc8eyAxvR6m9vgEdpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نت نداشتین این دوتا شده بودن سمبل شرافت و نجابت حکومتی‌ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65137" target="_blank">📅 14:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65136">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMwM1jONvKG4v7usQ86ARLl5ScdvgBECI-TbZnpP-UtusA71vdFhFVEqAb6CdEbPcXHcA_zYnmxl4zliX-Rt3ZgL5ztzn53jcRVbFrIt_xz-RtuZutjlhNA0H12MX56JrULozznP3v2fm7VToUOIwmG9MGsWcBSuMr3GBdp7xc0uL5mkgtygS6L8Kgag_I9un54eAzgF9ovQ4lu3wpDsjIAeaRKHNConFgW5UAYbS9lx5MA8mt8QehXZoI6AKpDT2aSo2v1nCZ0ov0ZGt13z0NMwltsrFxjhIx3dXDuH1jwTklFW-qOZIB5PQIKJbmiohjArSOE5u4-RXLWx6Q5rjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های حمید رسایی تو کانالش درباره چه کسی شایسته جایگاه رهبری است با آیه‌یی از نوح و پسرش که حتی صدای خود طرفداران حکومت رو هم درآورده
خیلی‌ها میگن مجتبی رو به پسر نوح تشبیه کرده
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65136" target="_blank">📅 13:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65135">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=Mj_7kd4az1koK0iFWwf9lmS6xtclIEMlSz97spaye_FsgzXgMb7gHD6n9rSYGxgP8oEl7YortmqhebjJU396l_V39nZhxdpuKBt3V9u8HNqk0457DB7Ct6qN2S2ZYBHNtYQuSHotHNG1GxjUWkpHYTRik55QoVp-m-Hy0w8vBysUaVQdRHVex363BBQfQV5WEMKw0UKkGWIX08Beu2OfLKX6Vr1DGhEN8rHi2I0Zo_IlQPzI4tTCOO8DDhqXhkNQ02dQnBCl_z8IdPIKxkAP97mAAQfMydpC7seEuTbI9cTSeDXmktmw7Vl52c1aZgx8VV3jSjanbT8ZP_EQhBuYdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=Mj_7kd4az1koK0iFWwf9lmS6xtclIEMlSz97spaye_FsgzXgMb7gHD6n9rSYGxgP8oEl7YortmqhebjJU396l_V39nZhxdpuKBt3V9u8HNqk0457DB7Ct6qN2S2ZYBHNtYQuSHotHNG1GxjUWkpHYTRik55QoVp-m-Hy0w8vBysUaVQdRHVex363BBQfQV5WEMKw0UKkGWIX08Beu2OfLKX6Vr1DGhEN8rHi2I0Zo_IlQPzI4tTCOO8DDhqXhkNQ02dQnBCl_z8IdPIKxkAP97mAAQfMydpC7seEuTbI9cTSeDXmktmw7Vl52c1aZgx8VV3jSjanbT8ZP_EQhBuYdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماهواره فضایی شرکت آمازون دیشب حین پرتاب به این شکل پشم‌ریزون منفجر شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65135" target="_blank">📅 12:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65132">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiD4g9mj5biuPouRVhKazUc8Yu0xkA6QoDmcNw88_W0xuXcKzVFi7G8i-BZMtzBIFDn3w4HUzhAQFcknAWbC_CkImscpgRSvTXFNrTITd0JRob6Ov4D8lHU1XaWSAIDhMuwwmrLKcjsIEBbro9CQWeth6OaWFHDH72pXZjoc5wIu_HI2VS_s0q66ivVO3upi3QSvKjUT3Bp_1ENn7LB_5hxzSNrLP1JZOPDIABjG_3FggGk_A3T36wzk4_awp02IupeHQDM6AugNpLc8kJSDQm4LqYp743ymiz8YLVW0xhJgdJE2e5Qi4KOXTezKtCsAnjQzKdrdbXVrWDwTjszsgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
واشنگتن پست: دولت ترامپ داره به اداره چاپ اسکناس فشار میاره تا ۲۵۰ دلاری با عکس ترامپ چاپ کنه
قبلا ترامپ ۱۰۰ دلاری های با امضا خودش تونست به چاپ برسونه و اولین فرد درحال درحال خدمتی بود که این اتفاق براش افتاد
همچنین طبق قوانین امریکا عکس افراد مرده میتونه فقط رو اسکناس چاپ بشه و از سال ۱۸۶۶ که این اتفاق بی سابقه‌ست
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65132" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65131">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=TBJg9gkKYv9RiLz4Hbh2tDzLrApoQQpxGkVUxLqz9u-W666IGTFjlKhs0SB9XcpBY1jRh1jQJeLnnKX13Oh7qn2-5wY3XfUOLfTECowlH2m0ruoh8ONm2lt4LGOe1nrssc_SqviXSfgpjjdTB65kVWaCK0niK5v8zZGGUE1istaJb9Xsy8UQVneUZWAZeFaMIU4p2T_Mi8_mpb7m8tnWYdcwasBocBsOoKaHcIUQu4cTfZHQfyWssW6yxFk2ER2nXjcWVYbK--8l8XVFuvVy4MUB61pVE8bFdqJ4StduDbOdq5cgpAa0REelpd81U03Y-qFEIuw9qJnstfi-5v_8IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=TBJg9gkKYv9RiLz4Hbh2tDzLrApoQQpxGkVUxLqz9u-W666IGTFjlKhs0SB9XcpBY1jRh1jQJeLnnKX13Oh7qn2-5wY3XfUOLfTECowlH2m0ruoh8ONm2lt4LGOe1nrssc_SqviXSfgpjjdTB65kVWaCK0niK5v8zZGGUE1istaJb9Xsy8UQVneUZWAZeFaMIU4p2T_Mi8_mpb7m8tnWYdcwasBocBsOoKaHcIUQu4cTfZHQfyWssW6yxFk2ER2nXjcWVYbK--8l8XVFuvVy4MUB61pVE8bFdqJ4StduDbOdq5cgpAa0REelpd81U03Y-qFEIuw9qJnstfi-5v_8IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: کشور‌های عربی مثل امارات و بحرین و مراکش برای تاسیس دولت فلسطین به پیمان ابراهیم نپیوستن بلکه چون اسرائیل رو یک متحد قدرتمند علیه ایران می‌دیدن به این توافق روی آوردن
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65131" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65130">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEYE3S0apMdKPn4lC50ctl6HIogDh_Ot7a9zHE9Kw0pAmQ352Ip-A6nQDMp3Mu6MNB8SDazrqWbW74ip76jwdDi9fXPZLdiGp13PcKxpkNwutfYE61ZP45aFxpQ_zXe3i5LDbTzfcvmSMHWoYd8M33vgwn8ri9EjhckQu-qaKtoNQBdmB21MmDsFfvuJJNA2L5RDn4zEtUOYd4uKRi9rNgb9eSO8I6xy3C18vDTPGkmj0OJkEYWs_siqklBejSWbvtUhWYWl_7l5g31H3e9hlprt96sw4pGS8QCPJo2LtsUe6zeJMEUFgkIcGsPTGltYrSLex6G27iymNPc3skplEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش دفاعی اسرائیل: از زمان عملیات غرش شیران تقریبا ۲۵۰۰ عضو و فرمانده حزب الله و ۸۰۰ نفر از اعضا رو از زمان شروع آتش‌بس حذف کردیم‌.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65130" target="_blank">📅 08:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65127">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
گزارش صدای انفجار و همچنین پرتاب موشک از شهر جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65127" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65126">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65126" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65124">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇺🇸
#رسمی
؛ توافق موقت ۶۰ روزه‌ی ایران و آمریکا نهایی شد و متن توافق، فقط منتظر تایید ترامپ است، هرلحظه ممکن است خبر اعلام شود
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65124" target="_blank">📅 22:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65121">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=mC61MJiicfguXEaurtJayPk8KDkY17h5kb0F94PgcU-mjflc0aIgKXyxgFyckcHzRqqRQzRgkb4-ppj7RuDsYLBCDy0-cSUvfLjxpPX8KY14wiASdTwWlYR7yhPdXlXe5c_CmyHx4WuvVIM4S-IIBtQBq7cO4zFvR_WFBLxsGEFByUDTmjZWUynjSMnnsrWgP-TjsGiVFMSLCLt8Res6fMEKqMB9icdrZHufEx-vKLst7FtaIDY9JxPtE0KuKW27_oCwBe97wkPL6gPrjkTeL_fzDhCmuQfSWBY0f9NjBbCh5jvxl5qPumnIT_iv4I7Z_WOjKJ7xKj6Qk7ohdVgupw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=mC61MJiicfguXEaurtJayPk8KDkY17h5kb0F94PgcU-mjflc0aIgKXyxgFyckcHzRqqRQzRgkb4-ppj7RuDsYLBCDy0-cSUvfLjxpPX8KY14wiASdTwWlYR7yhPdXlXe5c_CmyHx4WuvVIM4S-IIBtQBq7cO4zFvR_WFBLxsGEFByUDTmjZWUynjSMnnsrWgP-TjsGiVFMSLCLt8Res6fMEKqMB9icdrZHufEx-vKLst7FtaIDY9JxPtE0KuKW27_oCwBe97wkPL6gPrjkTeL_fzDhCmuQfSWBY0f9NjBbCh5jvxl5qPumnIT_iv4I7Z_WOjKJ7xKj6Qk7ohdVgupw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالی که جمهوری اسلامی اصرار داره یکی از بندهای توافق آتش‌بس تو لبنان باشه  نتانیاهو و اسرائیل در روزهای اخیر بشدت حملات رو علیه حزب‌الله افزایش دادن
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65121" target="_blank">📅 22:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65120">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌ها به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65120" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65119">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⭕️
توییت جدید اسکات بسنت وزیر خزانه داری ایالات متحده.
دولت ایالات متحده هیچ تلاشی برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
به ویژه عمان باید بداند که وزارت خزانه‌داری ایالات متحده به شدت هر بازیگری را که مستقیم یا غیرمستقیم در تسهیل عوارض تنگه دخیل باشد، هدف قرار خواهد داد و هر شریک مایل به این کار مجازات خواهد شد.
همه ملت‌ها باید هرگونه تلاش ایران برای ایجاد اختلال در جریان آزاد تجارت را به طور کامل رد کنند. روزهای ارعاب تهران در منطقه و جهان به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65119" target="_blank">📅 19:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65116">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSrXJpwrU-xm5QOtQ8vRdskF8UoAHSmKlWxAdOIyz6knuBCzU7Vn_c5F1neBHpblh_9aq-YtHr_qmRtAqT0XrFdNMcIgU-gEodg4CfnYMe_bNpXcKRs1lpk3N422f8PMT489PwKBcLPlJG04GkBBXJQhNLZGSCC2AHH7jx3j3SGHhKsCA7NGECVttUH2NdMbds8tLhryxjPUqslvmeF2pQXWAKyTw8omig_OmtjiAZCSZjPvo7xWLd3DYX5cEugF3clvjHUdy41kyeYdGieXKQmSpLFbVhMLvb7wDOKsTRzuety-h2gGaRplriBW8m0h2R8LuvLdRuUgD70Mnnhpcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
آکسیوس: اکثر شرایط تا سه‌شنبه نهایی شده بود و مذاکره‌کنندگان ایرانی بعداً اعلام کردند که تأییدیه‌های لازم برای امضا را دریافت کرده‌اند. ترامپ در جریان توافق قرار گرفت اما به میانجی‌ها گفت که «چند روز» برای بررسی آن می‌خواهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65116" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65115">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uutcrVw4w2Vbc7HH6lhOw5IOffBWdNIewJrZANUY8AyW3EDqTgRGzJ-lzP26Iy0Ykr9LRYmoq10urm8xRa-91vNE92G_TMXoxXu3ROefsnh_OBXm6314VAn8qUJEM2Zaco7GPZFDUUvhOXxcrC-Ss5AjrZb2k7v613gKwB-irL3WjgpTv4TOmOxC7qETvYC0FOLUUaZ4OtyTH_0QRl5qH9PsCOQHmuF4uioAExPTG9heE3gdttKPh9fKqi_j1kZ3IPkf-aQJ1SzyzgzXXfms658WCznpCge2FmQwohlctKmaB5aZXc9ay5afPJEE53Qh4CS6w-gXMDm53PUjH7dGxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوارنگاره جدید میدام فلسطین از حرف جدید مجتبی خامنه‌ای درباره اسرائیل؛
" رژیم صهیونیستی 15 سال آینده را نخواهد دید"
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65115" target="_blank">📅 16:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65113">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0T4F1ptlxajCVWwMQozbwmQzM3pqMcHr42kKXfeXZoOhBZW5Rfadn1QAeySG-i6lv0AHwgj-z8XEyLiIcF0JIWO13TrrQFPTPM0lAHwfNjff2a3XqTiCL6q4qd_tGeukLXnCJix1mDm_8lRER2kIDSDZaKCdBoSLZAFpy7KgvFRP-XDfjYerWutYZcdLSoiklYcIMQyzmoQDm6vB7TYGU8PdRwc4NByPvkVtCjUQ4P6JATGlUaqXO32O5XhmIS4sVSrk8jgKqPwqDrpI4d0VmQGSiGYWBSqHQBFy4ALyJ9a98oMF7kStdFSlcZzJvy1DvXU17Tyoka_9b0cB9WWeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
نت بلاکس
: سه ماه پیش در چنین روزی Iran دسترسی به
اینترنت جهانی
را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با
فیلترینگ
شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65113" target="_blank">📅 16:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65112">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حملات تازه اسرائیل به جنوب لبنان؛ تل‌آویو از هدف قرار دادن زیرساخت‌های حزب‌الله خبر داد
ارتش اسرائیل اعلام کرد حملاتی را در جنوب لبنان انجام داده و زیرساخت‌های متعلق به حزب‌الله را در منطقه صور هدف قرار داده است.
ارتش اسرائیل در بیانیه‌ای کوتاه گفت این عملیات علیه «زیرساخت‌های حزب‌الله» صورت گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65112" target="_blank">📅 13:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65109">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس: ایران ۴ پهپاد یک‌طرفه به یک کشتی تجاری آمریکایی شلیک کرد. ارتش آمریکا این پهپادها را سرنگون کرد و پیش از پرتاب، یک واحد پرتاب پهپاد ایرانی دیگر را در زمین هدف قرار داد.  @News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/65109" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65108">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/news_hut/65108" target="_blank">📅 03:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65107">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/news_hut/65107" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65106">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">چرا نت من قبل از وصلی ها بهتر بود، چه وضعشششه آخه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/news_hut/65106" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65105">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عمو Pishgiri بهم sms زده و گفته خشخاش نکارم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/news_hut/65105" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65104">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/news_hut/65104" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65103">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65103" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65102">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:  @News_Hut</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/news_hut/65102" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65101">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEY_kjBAWOedMo3Qc93atxKQ3vwkztZXCIrIkgmg3O2AacukCQElmhXbsuIGHXxGhxzBU0DzncBBZxZ2v6yzSldH3C_9v4PyDn2cuBE_3lw8DC9jSxtbc8Zt5MKmvgiIbkk-SwZzsRkQUWlHFyIvVlEH9WUpMpCm1pAFOz6R-9yMMho_QVFoh9w950FWx1FzQT1lxTzVE7wMPnaGnGyfePqbzCcf23RRNG822Nnx6dF-YEpkphmSHt5lGuByRQpNLVJWVgy3122wDKKonNPS2DFLhaWe15-dy5u3HGMr3fvvLUSK8s7WBuLeaaTK8aJ28SC3mHQ5iIAFGZ_lr-6koQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@News_Hut</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/news_hut/65101" target="_blank">📅 08:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65100">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">امروز ۶ خرداد عید قربونه
@News_Hut</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/news_hut/65100" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65099">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcF3kBCikxhDKAnW42lyKlHtRNE21Yb1JuytEq_N7uiMrvwLSVB-S4my5JUWMowd9d9nNy1pDutF6jj0ZsvWqtYzuW7_LuX_udkOupnsCtvcmRT6cQa-QtttzTspprsyUXSU2P7Ed2O002zKwaszbIA3bgHBi2DNEduNkPrTlx3glG3nfEXctTHxEyE8Oc5xqGfeatTfegBq4YEjSDO7GUcE7i7eP5B0xq3za4uB0odrreLSmDahhiDiomZL4yWSV75F4fWdXwAtxR9QDccFYwb0rFBpdGdFBLDGLyaQCceAYzcLuQO1-NnMSQ_avxtTBLUKfE0xwUDq3s5sss04Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها پارمیدا دیگه بعدش آنلاین نشده
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/news_hut/65099" target="_blank">📅 08:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65098">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اولین صبحِ اتصال اینترنت بخیر جوون ایرانی
🫂
#hjAly</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/65098" target="_blank">📅 08:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65097">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جالبه یه یارو مثلا نورالدین الدغیر خبرنگار الجزیره تو تهران میاد توئیت میزنه همچی تموم شده و فقط امضا بین دوطرف مونده
خبرگزاری داخلی و وابسته به حکومت همینو بعنوان خبر میزنه ینی شما بیصاب شده‌ها به منبع ندارین خودتون؟
@News_Hut</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/news_hut/65097" target="_blank">📅 03:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65096">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UGk-OOfbO-j1NQlpym387pLr8NJhVf2yXoozr3_jn6wMNJo2LO0Pu_tmUQqCy9TyRMYOzyD8K3bAiMBCEKcyn3Dz81jMR8O4JxwOAGJRQJy6yHCtpvumYC92sX7mNUtVjTwrq2JEDb37OeiSIMu_3sTpwqj_WChebFmLmSsdpGHZUCHr7bImNBYObkOnGSNSj6JF9aQRj2ewZNYIEIg2Jc7VugJECUVkSfR6IbdhSIABHLvSqsXbo1wZpG6-MbOV0XvTJcJbrzoJJcjlFmLYAiH1ZMYrnwUzi3_h0vbhF8jnY_aoxyQ22_r4lwvw7n0NfTHQbhkpuXWf_0rGaumNOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  «اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/news_hut/65096" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65095">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اتاق اصناف: از این به بعد فروش سیگار نخی ممنوعه
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65095" target="_blank">📅 22:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65094">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swUEvDk_sCjni8GYW48BAgM_jCilDWCKisrZg5E7AM1bYgnIZIWArFTeQwNsoy251Cl64ndJioZlPPooXGlrCZbeX_ZSkFYH-ED_q8fwmxzPu0LOO-Zw27MjylS0KtFjtk3hHs_fQt4Cqrmcrtra8PNgs-H0-rCikH0p2MpMzJwGynO5SZbX9eIKuOLpgF7CJbLWicr4JrLuWn7U37cwH9UBfNemqohewntW9Y_rpfcFFHBB-wgWE4AwE_r9QdMRgNl_f02CvA0iiC1tyjewh_RPKb7UBRuxIHBMIF45RuqWE1MeZm1Z1h2JjqU36eooldLjShzUNo8CrCp448O9hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: همین الان معاینه 6 ماهه‌ام تموم شد، همه‌چیز کاملا عالی بود از دکترها و کادر فوق‌العاده مرکز پزشکی نظامی والتر رید تشکر می‌کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65094" target="_blank">📅 22:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65089">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65089" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65088">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIgzCZU-sd7KQpceW5aR3OcusUIeAeXXO4IYa-7OKo0CsJFzPBsAWdDKi5yW0wMtleiwnC2hBWJhkR7h9fkREgus6c1nwSlvEhlGgQaUEvqUea9VHRXfjbdQCx5du_yFQhPfGc7X40oBDeXeq3LE7kkuet3roPrMKfmc_PTh_lRE1wY9ovr8kNz5mEF9UGWzJdYXxJvnj9nZXfGiRM8bSC0TqJYmkTwNKv-2l9LR1JfOn356aBNgF8vvCObs7Mnnb39bHUD158xvB-8aibJP8nTI642ZszcA5J74ITCJNFZDMlZKgkgumw7sFW7MTGKk3lK8Nm1bbNOuiGS0V4GVSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد عوده، فرمانده ارشد حماس، توسط اسرائیل ترور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65088" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65085">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نت بلاکس: دسترسی به نت تو ایران به ۸۶ درصد رسید، اینترنت همچنان فیلتره ولی امکان دور زدنش فراهم شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65085" target="_blank">📅 21:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65084">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=MSeHfz7Jo-a5JYh8N4YyCqpzeW5s8Raz1ODrWWoG2iy_7FztRpCL1r-yntKqOuS6FSWW4XpvFB3_7CyGRxzZb36Hi1czWrGP2vABpIy-A6cCPXdYfy80NZVD3QvxWmsSzB3nCspTK-XHY8nTdkhGDtcIdoPrqj9DRMe79gf4F1VSEBeesvHxN86_3BgCSnShP1qUEzsh4F9vjSmO5S8XUmvbrF_5Chs_E8v09Hse9qosy4Oc39vP9S1njEFQSDA5MrS-jonM6HnqZ4WAZRXW9VTDolY4OC0tUWwuxcfDXRdb3K-rUNqBQky4CmGLNcsrnFl4MBS8nKQz_xzqL6jGWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=MSeHfz7Jo-a5JYh8N4YyCqpzeW5s8Raz1ODrWWoG2iy_7FztRpCL1r-yntKqOuS6FSWW4XpvFB3_7CyGRxzZb36Hi1czWrGP2vABpIy-A6cCPXdYfy80NZVD3QvxWmsSzB3nCspTK-XHY8nTdkhGDtcIdoPrqj9DRMe79gf4F1VSEBeesvHxN86_3BgCSnShP1qUEzsh4F9vjSmO5S8XUmvbrF_5Chs_E8v09Hse9qosy4Oc39vP9S1njEFQSDA5MrS-jonM6HnqZ4WAZRXW9VTDolY4OC0tUWwuxcfDXRdb3K-rUNqBQky4CmGLNcsrnFl4MBS8nKQz_xzqL6jGWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن  @News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65084" target="_blank">📅 17:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65083">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFudo.</strong></div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/65083" target="_blank">📅 17:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65082">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65082" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65081">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMKPX</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag1XnoaV6E1hFibqoFBdKpc_k6qreIDFTIP90DtVSHRNCvMHcLImctkrRBJsEnvG3Rd7WCu5KY1t6T4g0dJ9zpcz0t0RwXdQ8U_nRW7dMZ554iaexXDWCQk2MMnOODSkCT5UIfc9JqvBpCcLZNbZNKSqQyPxqBoL3QJ9rnwL4-u3uH57sgsZhOi-Aff18wPsTw4bfdLb4Tl2N4M3js1qnlie2stlv0Rj4ri0YKmV3cV959nMDZ8t8OUtw57ffpUyA3CUHtkAwRtdjo7nKu30bXDT0e8s2qwkVWPkeIZ_F5LKbb3XnGZlmwx3ZFTaCr4dy5gUrcEyCPohNojsoSmVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65081" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65080">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65079" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65078">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwiQUEf93f0wqpjmkQhKqYTTrKqnt-eVZa4uDjk3Myf0by_Puph5swOKL0i8TztbEi1CIZprMxHkEKCBFJ5RXZwRW4q4W7DeHNy-vC1jzy3tnvCcmSLaI-_uk6ZCbhdbMsdaIS0Fukz_juTF7_y8s-fQUmeHsiY4lnl1jlRKx4QzfYQ6_opWn68IFGeYjtUDBrnuxDAa9ZFQIkFrzyZXt2nmLEjeyIf-y4mxW2iQs1A6lC233aZntV6TXUH628i2v188dyjE_eVJTHkYUTB1CBvDYPCznDMvnChUv9DT6zAdpUKMok7q2y5JkGgriTpwEcuHj0JtcwuQgcx_E5fA_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65078" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65077">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.   این چهار حروم‌لقمه عبارتند از: رضا تقی پور، نماینده مجلس کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی رسول جلیلی،…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65077" target="_blank">📅 14:57 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
