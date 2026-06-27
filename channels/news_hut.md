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
<img src="https://cdn4.telesco.pe/file/GtgpS4OSr6-C3lKDcBTpU0TTIzrlOuB0-an4VuSbr0DROZgN1gtvmWYdfD_V9ATD7KXqbp_IEQRXEBe0BmfzoDtujY1DI14xTM37MwOM4nkeg7BZp6guvijfJb_YWpMy8ZtN7jDLejTy9cHEffsNzOL0U-q2pACYNvSMoweHj8l7IdJ1BAjKQ8l48fMnOPQTcv3iWcprBh0r75E2oIIC7VIRGNQX1nkH2iIG8bG0YljPFRw_H--WsKRujNw-GiXM9nENIxq74GuBRARD-8tmrA-mpikxcYiMHJw-IqQpnYiAFcLa2W-pstEvb9couoX1bHzYQikI6UACRdLUpUVi1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 02:27:07</div>
<hr>

<div class="tg-post" id="msg-66956">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
❌
صداوسیما:
جزئیات عملیات امشب نیروی دریایی سپاه علیه دشمن آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/news_hut/66956" target="_blank">📅 02:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66955">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
❌
مقام آمریکایی:
ارتش آمریکا سامانه‌های پدافند هوایی، انبارهای نگهداری پهپاد، موشک‌های کروز، رادارهای هدایت آتش، توانمندی‌های مین‌گذاری و سامانه‌های موشکی زمین به هوا را هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/news_hut/66955" target="_blank">📅 01:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66954">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات هوایی امشب به اهدافی در ایران به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/news_hut/66954" target="_blank">📅 01:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66953">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
شنیده شدن صدای چند انفجار در بندر لنگه و بندر‌کنگ
@News_Hut</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/news_hut/66953" target="_blank">📅 01:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66952">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
نیروهای آمریکایی و بحرینی ۹پهباد ایرانی را که به سمت نیرو‌های آمریکایی در بحرین شلیک شده بود سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/news_hut/66952" target="_blank">📅 01:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66951">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
حمله کنونی آمریکا بزرگتر از حمله ای است که دیشب رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/news_hut/66951" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66950">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A88N4T4pvo_jiBIyW1KhyPdRx0C6lUpWXM1a2eao1yW1Kr-5AfORmQGPxZ5OBV65EQO5H2vPXcEMTvB8u2havJIG6mZ7zSHb-v0sSealZ9v6O3PXhDb4rdR7Ed72CDVXYoh9SRuL_1VykfHW5VKxpXvu5y01oGT2LURVsN6UfK5OubqBFcgPBfsUmA_KeO9urDUcIoubeOj3oVrNrD3z9FFT2FLqWblQ4N9dfcqgGM727QIcv-2MJJC9UGHOh_Kf-e5i07Tmp8ELp9obSYxw0iPoTn1r9BZJXawBYflyV8veLKMBGXrRj32gnFdwsdo6P2vCPyqrEDA1DF_ovTFMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام:
پس از حملات دیروز ایالات متحده در پاسخ به حمله ایران به کشتی ام/وی اور لاولی، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند باشد، اما وقتی نیروهایش ساعت ۴:۳۰ صبح به وقت شرق آمریکا یک پهپاد تهاجمی یک‌طرفه را به سمت کشتی ام/تی کیکو شلیک کردند، این فرصت را از دست دادند. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز با بیش از دو میلیون بشکه نفت خام در حال عبور بود.
نیروهای فرماندهی مرکزی ایالات متحده امروز در پاسخ مستقیم به ادامه تجاوز ایران به کشتی‌های تجاری، حملاتی را انجام دادند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و قابلیت‌های مین‌ریزی ایران را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/news_hut/66950" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66949">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
صدای انفجار در سواحل سیریک
دقایقی پیش مردم در سواحل و محدودۀ ساحلی منطقۀ طاهروییه سیریک صدای چند انفجار شنیدند.
همچنین اهالی مسن در قشم نیز از شنیده‌شدن صدای چند انفجار در این منطقه خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/news_hut/66949" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66948">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmYq-4c7nuu38RydXJNJcxrt_2iDNIvonEroP_Iz-uYgDcA3nkvN1SN3B7ZwaeBU_KJA7JURSN9vsWMMGQtnXvykJaqNJiAxc3D3ZGdU-7Li06koLvVlizFZ-LJ5-G7hM3CFsR4TZd_0p_M0K30EM3L5cQoDFipT5m_owQ5bACz8tg-BPoOeej5eLdcaU-FC0uCf1d-rZxtFcjjQxK7b5xr8CpKzfBIPngHiWwY2us-4WgzGW1T5bLolk5IvTIL-8ZlEC0NQpGg2QN6wdkimK1CXCyKLN3AjaqfIOcaZy4cdgmTAz--3h6EYzJvJTbmvuB0AGjD9pfnNKKfbArcmXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید اکسیوس:
یک مقام آمریکایی اعلام کرد که ارتش آمریکا در تلافی حمله صبح امروز ایران به یک نفتکش تجاری، در حال انجام حملاتی به اهداف ایرانی در منطقه تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/news_hut/66948" target="_blank">📅 01:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66946">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما:
شنیده شدن صدای چند انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/66946" target="_blank">📅 00:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66945">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDLG4IX43CIeWq0Ioo1OWWTSJNDDFFlYXX3GcSgcivJJmMDvQOhOEMknB9CcF-RyZDX5HpRM2uMuqoNehKTvrelk4qpbt77pNUcM9J946N4epU_kccO03kt3gohmkNDZ391jkXHnlmPH-vqYdLzJp08m6BbgUP1eRp-ze7IlzDSKkBo_ppvzVrdbYOkV_fhzIVQXJO6hbcmAY3RbbaxM7IyyIttRT5NykD2B2KOqS1vsAyb7AuwRTXobvS9b8AIFJs4hp7ZXKGxjAv1Y3ZF6KBKrdJBp95wlBmdhqa3iBDwbZEo_GwxOXMXNblCIx-f0NnTZGUsq0o_TpdvmFd1lgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
به گزارش وال‌استریت ژورنال، یک مقام آمریکایی اعلام کرده است:
🔴
در جریان حمله روز شنبه به بحرین، دو پهپاد ایرانی شناسایی شدند.
🔴
یکی از آن‌ها توسط سامانه‌های پدافند هوایی زمینی سرنگون شد.پهپاد دوم بدون اینکه هدفی را مورد اصابت قرار دهد، در منطقه‌ای دورافتاده از یک فرودگاه به زمین نشست.
🔴
این مقام همچنین مدعی شد که:
یک پهپاد ایرانی به یک نفتکش حامل ۲ میلیون بشکه نفت خام در نزدیکی تنگه هرمز برخورد کرده است.
🔴
نیروهای آمریکایی نیز دو پهپاد دیگر را که به سمت کشتی‌های تجاری در حرکت بودند، رهگیری و متوقف کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/66945" target="_blank">📅 00:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66944">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=vxPILOBHOxgLpYh17lYRHXz70b7RD7jlN5r5yvCRK9hdfvlWmmdNnaYCOwR7KcscWImlAh35Tp88cVHBMCEpPQkm_E5TeP6gug0C3_-w89UyJCvEP75sSMcpxwIsUFtGiQHCIhw27FXSxGuLJjwWknsZ8zz2Hjd4-q_GRPcG1jR6ZTYWxktd60mtMS5iG728Tj1hbk72N7ClWVuMN58T31oe3CUOUXnTHYQH8JMb9pJptBkci-HuOBiFPoIs_WqFH9qC57bRHEPadSnnSl3vpd6Y095lyW1UCCG3QyeROObspfJg-j82VysGTV2acn1plvZTVOEg6y2ARLiFWv_BBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=vxPILOBHOxgLpYh17lYRHXz70b7RD7jlN5r5yvCRK9hdfvlWmmdNnaYCOwR7KcscWImlAh35Tp88cVHBMCEpPQkm_E5TeP6gug0C3_-w89UyJCvEP75sSMcpxwIsUFtGiQHCIhw27FXSxGuLJjwWknsZ8zz2Hjd4-q_GRPcG1jR6ZTYWxktd60mtMS5iG728Tj1hbk72N7ClWVuMN58T31oe3CUOUXnTHYQH8JMb9pJptBkci-HuOBiFPoIs_WqFH9qC57bRHEPadSnnSl3vpd6Y095lyW1UCCG3QyeROObspfJg-j82VysGTV2acn1plvZTVOEg6y2ARLiFWv_BBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئوی مسخره کردن خوشحالی بعد گل آفساید شجاع خلیل‌زاده توسط مصری‌ها به سرعت در فضای مجازی در حال وایرال شدنه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/66944" target="_blank">📅 00:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66943">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=VAhixyIDxronvba-TluvJEfVNpmE-h2gMd8t51E7ySBxuOi3IazoFTE4Ra0jsi6N4NtcCfE-ukMqpGjn5UV6Xcu69TshR71voPFiAZDH5iBmpmjFkMr5nfYZep8-f5mmWPbqEmbj7vguvQoaxRalJzaq3uuz70hXTkagy1vcSOiiWuQdHA5luTkbERuXffMukM7YEy3VplpI6ChXsbwPD2u3dHVodU26yh88yFX86w0IwSWKQUBeTbNniaO-s07I5tgng_Uhgm_M82gyIGDvgziy9vv6skiRGDkW8FbAuHfXPzViJZV46SRCu244YDfewjyi7hjS7ivbUKw5jsbD-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=VAhixyIDxronvba-TluvJEfVNpmE-h2gMd8t51E7ySBxuOi3IazoFTE4Ra0jsi6N4NtcCfE-ukMqpGjn5UV6Xcu69TshR71voPFiAZDH5iBmpmjFkMr5nfYZep8-f5mmWPbqEmbj7vguvQoaxRalJzaq3uuz70hXTkagy1vcSOiiWuQdHA5luTkbERuXffMukM7YEy3VplpI6ChXsbwPD2u3dHVodU26yh88yFX86w0IwSWKQUBeTbNniaO-s07I5tgng_Uhgm_M82gyIGDvgziy9vv6skiRGDkW8FbAuHfXPzViJZV46SRCu244YDfewjyi7hjS7ivbUKw5jsbD-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
صادق خرازی: یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور قرار گرفته!| کمال خرازی را به صورت استنشاقی در بخش عمومی ترور کردند
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/66943" target="_blank">📅 00:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66942">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02e1890541.mp4?token=WLM3mIqL8A6IcreADiw_gP8Jn-f4ikkU3nVCD0VbWZGhUcIUmQ39polKVIaEDzKg48qhWNbMrvAzeeoqPAQY5xvmlLuW85FHZ0js1hzKd5vuqJ1R3tFkGYNixJTFVWB-rcmPpa-WDCHQQBi3WDLO4Kgd4crCF97eLc_I6zWdaagzz0Lqhxv0twHt572xzBKVxg89tD9kPQxILxf8IWXyTyqCZ1NIwFR-yd_wNKdnEluLeitYTXaVG7aQXTEg5ERNXRcwyuqyCHU-Ox4Wc5YDKoc0NLiIFGsq8P6ztomdMV_c_8BLw9L0dFRe2nWlXqbyib7Ij0Z9AGqCEvunb_wI7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02e1890541.mp4?token=WLM3mIqL8A6IcreADiw_gP8Jn-f4ikkU3nVCD0VbWZGhUcIUmQ39polKVIaEDzKg48qhWNbMrvAzeeoqPAQY5xvmlLuW85FHZ0js1hzKd5vuqJ1R3tFkGYNixJTFVWB-rcmPpa-WDCHQQBi3WDLO4Kgd4crCF97eLc_I6zWdaagzz0Lqhxv0twHt572xzBKVxg89tD9kPQxILxf8IWXyTyqCZ1NIwFR-yd_wNKdnEluLeitYTXaVG7aQXTEg5ERNXRcwyuqyCHU-Ox4Wc5YDKoc0NLiIFGsq8P6ztomdMV_c_8BLw9L0dFRe2nWlXqbyib7Ij0Z9AGqCEvunb_wI7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف گرفت رو تندروها؛
اینایی که سوپرانقلابی و تندرون؛ هیچ غلطی برای این انقلاب نکردن. پس حق ندارن حرف بزنن و طلبکار باشن. دهنشونو باز نکنن و سرشون تو کار خودشون باشه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66942" target="_blank">📅 23:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66941">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⚠️
🔴
مارک لوین خبرنگار نزدیک ترامپ:
اگر این رژیم در ایران می توانست، تک تک شما را که در این اتاق نشسته اید بکشد، تک تک شما را می کشت.
هر زن که در این اتاق بود به آنها تجاوز می کرد. تک تک.
اگر اینجا نوه داشتی آنها را می کشتند.
آنها را سلاخی می کردند، تک تک شما در اینجا میکشتند چون یهودی هستید یا مسیحی یا فقط یکی از آنها نیستید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66941" target="_blank">📅 22:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66940">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=YU8vhMNkHsTbbL2QOr8LqpcUjM9dbYakBZw9oW9nXDZlnXfpOm1pGazoR1e_n9bwu9PKSquHIV-SsKk2bxXqjMRa0bYbbe_g5u-JLQAStm_l1fytOdON6ZRmp5p2Vb8fpuUA-bBqReDHoqpfyoqLoR3eTqCL_sFC5dlHs4FkCgaXPs1d2qmDAPMLsh3EeW16xDfcO84qiMHkRzbZKhcOmEhjnWPgjUNOjp0pnGasmwIrBZTp01m94UbR8FJuoI2YGmAmnGQsi4jcvFe6fQTgKf-xN5Br2hX4-m_2bZMnl8XdQreYveY7Xk4AFwMzjq2Ei6Jb1yExobKVSayiQwXpvIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=YU8vhMNkHsTbbL2QOr8LqpcUjM9dbYakBZw9oW9nXDZlnXfpOm1pGazoR1e_n9bwu9PKSquHIV-SsKk2bxXqjMRa0bYbbe_g5u-JLQAStm_l1fytOdON6ZRmp5p2Vb8fpuUA-bBqReDHoqpfyoqLoR3eTqCL_sFC5dlHs4FkCgaXPs1d2qmDAPMLsh3EeW16xDfcO84qiMHkRzbZKhcOmEhjnWPgjUNOjp0pnGasmwIrBZTp01m94UbR8FJuoI2YGmAmnGQsi4jcvFe6fQTgKf-xN5Br2hX4-m_2bZMnl8XdQreYveY7Xk4AFwMzjq2Ei6Jb1yExobKVSayiQwXpvIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
بنیامین نتانیاهو:
دیروز تهدیدی بسیار دورتر از سربازان ما وجود داشت - نه در برد فوری.
آن‌ها هفت تروریست را دیدند که وارد خانه‌ای می‌شوند. آن‌ها هنوز شلیک نکرده بودند و هنوز خود را سازماندهی نکرده بودند.
اما آن خانه نابود شد و آن هفت تروریست حذف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66940" target="_blank">📅 22:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66939">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=esl9njUAoYewhC5__UsK6mG-SmpmUvpLO05M5OQlC7GcN0uGfQcN9P-aM2cippM0mtX916X9MZPZVxG7ILxrWhGRDhiaTWIO-5aFoPIxuJAA6XgdbOPlecBWBIzqBG65JFI1GqY6fvMluIkBkUUfwZwESaOM-PU6uNfkwhEVF5xxWvaI2jTQTv8W6Gc-tbL8DZ4ciG2kGf9Rr3klzip8kO5DnTULhzLg9QfkV64zNiuVwQjkHEX5j7U2Hh8rxpzwC8aYIi1jXEYgVIhKYYEU8iMy7kF8mBQafViFCz0nI-V-n7tw-bl1vd0TNy7icbscKW6Sr3G-0HRmLkWXIzYf-S4ntiA2_PXkr0EXgCUuWAxQhphgR_UrBrXyS5ixAsuPFx2Vk1nUeEtH91UhxPi_UuX1lZ1ZaUgVup2JWqsjpT95PRQeVkKq4miEKXv3Ts7U9LjnutdBCmmQMeIqwRi9PGiBQkFi3oJB9q6rfkIdA86REhGkX7qybYQqDv2H43epWrQYRihf4Y97qDD3gRX1JeYDoDDD3dYdkpYUlPAUCcAy_A-F4vfaD8ODxCSzoW7m3iqizhyc-n_gK85Ehyvo6UhQz4Jps_TAGZ-sgR0Q280XyqmSlvpOqt0rw0oO2ozIKtux9c5bhbIyhcqW2SRv2L3eA9fsYCWbDx8X-hIm7zo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=esl9njUAoYewhC5__UsK6mG-SmpmUvpLO05M5OQlC7GcN0uGfQcN9P-aM2cippM0mtX916X9MZPZVxG7ILxrWhGRDhiaTWIO-5aFoPIxuJAA6XgdbOPlecBWBIzqBG65JFI1GqY6fvMluIkBkUUfwZwESaOM-PU6uNfkwhEVF5xxWvaI2jTQTv8W6Gc-tbL8DZ4ciG2kGf9Rr3klzip8kO5DnTULhzLg9QfkV64zNiuVwQjkHEX5j7U2Hh8rxpzwC8aYIi1jXEYgVIhKYYEU8iMy7kF8mBQafViFCz0nI-V-n7tw-bl1vd0TNy7icbscKW6Sr3G-0HRmLkWXIzYf-S4ntiA2_PXkr0EXgCUuWAxQhphgR_UrBrXyS5ixAsuPFx2Vk1nUeEtH91UhxPi_UuX1lZ1ZaUgVup2JWqsjpT95PRQeVkKq4miEKXv3Ts7U9LjnutdBCmmQMeIqwRi9PGiBQkFi3oJB9q6rfkIdA86REhGkX7qybYQqDv2H43epWrQYRihf4Y97qDD3gRX1JeYDoDDD3dYdkpYUlPAUCcAy_A-F4vfaD8ODxCSzoW7m3iqizhyc-n_gK85Ehyvo6UhQz4Jps_TAGZ-sgR0Q280XyqmSlvpOqt0rw0oO2ozIKtux9c5bhbIyhcqW2SRv2L3eA9fsYCWbDx8X-hIm7zo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتانیاهو درباره لبنان:
اسرائیل در منطقه امنیتی زرد باقی می‌ماند که ما را ایمن نگه می‌دارد. و این یک دستاورد بزرگ است. بزرگ!
چون آنها چه کردند؟ آنها تلاش کردند ما را از آنجا با انواع روش‌ها و فشارها بیرون بکشند. البته این اتفاق نیفتاد.
از رئیس‌جمهور ترامپ و وزیر امور خارجه روبیو برای مشارکت و کمک‌هایشان تشکر می‌کنم
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66939" target="_blank">📅 22:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66938">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=pagtbWNGi06q7SvHMA92r0tlSAyzPgUIuzyfqLaysrrwTmlGDDwtrJLlJrwC0nH8Hy0HhSHaIEkOrbkGgwreOgeNHtgq15CRGyEBFRgVCGprCrKHEyZTPubFxIdh9mG6Pq3fscYIoL3Y8s_Vqv7dU0rG6SUk9DO7cviZGXnoHm7-3aApWuHvQOtBhoMkfmsJCLkh52BigiUIkujnf1UMb0KTeBfeseMR4VpX2VHl0ktjA-REf-pjw8oh-XbiClXFfhiTF72lXwHMoBYze6ZQscRM_9UHBxZDkXYTfVAuR1NKXK8LlwMpWJzYQAH-LfJE-mheDdn0yv3v4YvJmua1Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=pagtbWNGi06q7SvHMA92r0tlSAyzPgUIuzyfqLaysrrwTmlGDDwtrJLlJrwC0nH8Hy0HhSHaIEkOrbkGgwreOgeNHtgq15CRGyEBFRgVCGprCrKHEyZTPubFxIdh9mG6Pq3fscYIoL3Y8s_Vqv7dU0rG6SUk9DO7cviZGXnoHm7-3aApWuHvQOtBhoMkfmsJCLkh52BigiUIkujnf1UMb0KTeBfeseMR4VpX2VHl0ktjA-REf-pjw8oh-XbiClXFfhiTF72lXwHMoBYze6ZQscRM_9UHBxZDkXYTfVAuR1NKXK8LlwMpWJzYQAH-LfJE-mheDdn0yv3v4YvJmua1Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏کاتز وزیر جنگ اسرائیل:
اگر ایران برای جلوگیری از اجرای این توافق تلاش کند به اسرائیل حمله کند، ما با قدرتی قاطع و کوبنده پاسخ خواهیم داد و شکاف موجود در توان نظامی میان دو طرف را به نمایش خواهیم گذاشت.
این توافق «ضربه‌ای راهبردی» به محور تحت رهبری ایران وارد می‌کند. اسرائیل در منطقه امنیتی خود در جنوب لبنان باقی خواهد ماند و تا زمانی که حزب الله به طور کامل در سراسر لبنان خلع سلاح نشود، نیروهای اسرائیلی از آن منطقه عقب‌نشینی نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66938" target="_blank">📅 21:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66937">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8KMrJMrSqeADz7xqtE1sehGPQyw16MYXOFOEDeoDFpfuFfBwCp0Jh_S3ztInHcyI0pu97wkNj-et4mza45BQLOgeB1MVoF3IcLcpu1il-Dxy_4yI7gqjcc1_S9-v0oFd2lchmM8dlijFIYV9K_lzegZ6qWGHDlOZT55SWrNH3pTlquM42F1vBQUX5ftlzH9m-iJJCNwA0lWA8dkn421XqtTsHUGnqrRDh8qjmmG7EphqualUHs4BFe3OYvtHdY2rsyGpffotgZwAqKpiXR9BpGMG5mTQL0iRyHoJoHGWBe5-ngGBWAnvm41R-N1VuV4vL_AFsV2-P1rmF5ugKWn6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مرندی:
همانطور که انتظار می‌رفت، رژیم ترامپ چندین ماده از تفاهم‌نامه را نقض می‌کند. در نتیجه، ایران نیز مجبور به انجام همین کار است. جمهوری اسلامی تا زمانی که تمام تعهدات ایالات متحده به طور کامل اجرا نشود، به اعمال فشار اقتصادی و نظامی ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66937" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66935">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KV8yrRWd6bcOPlPLHkmTl-itH8illelxyH99UavFuI7Efgr99T1Bq7DGyeKYahg2tVBexklkpuvRBkzbZoSbbgsKUc62F2eTqOQHAr7zZJNswCCSmb3y0XnUEPNjtdsQdiD3khIws_TrQwYI8EzA3SUiBg-bUsYOQyTNv76lgcbOeJelrlg1Q18-Bv0X0lAn9-v4y3KWmrEg-WDUSv0udfe55wnZa6n8iHpmUVrL-xjsuqoZAsDID12-TSgnXyxELiHZj5rRFQRAX8PUZN7ChHYIFzZtRf-u1lfY70NA_ubwmRU-BA3ugEMBpc8HLGcVaEJlMwlCd1xZEEWh4o-MKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IAM3pt0tJaht_Ro9SDqWpeYfByIHM2e3Dp-IvWnuviXnS6WfnJ_72Uftif7uCvs7oOLBeicX851YIoCcH7nWM-F6xijCgibwaUPAIDFTOQ3xjwa97MjG_4Yx6dPv9eenM75veWkAVPKcMHbxiyxijaw_r7j_4nvvmyBcnY2421-LkV82T4-xYJuJ4eBqulS2TYbvc8FTPxJkBpmsPPryLRbf_hf37zbxYzl3b9tUqZnzh6yuJL8Vde3Kh_0NwZpktVJosYYhb3Rl0jEtIjE-sbq28mSpyyzHhhO4R5gIFyjEWsFa7JUwg3BrCQb-43bco2ysORNIVCSQV4xfB2qw1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترامپ در تروث سوشال
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66935" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66934">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWXqgtVdeEtlH480L06Tcgx6i_FMRLuiiFJgJp5dA9t_1dd9HCrR-akhDqi2PLSC2fRod075ShkQpFZq8ZSaTTiK6WGfzzCvkLIRU8xVBg9p_LoZbc-Y5pvsgZOqRsYdrNiRC-8HaWNRjdBtZcGO6Cuej8f7ZFWXMW3BtXgaRk-wH5AxLZlB16yUdenBhrFPvA62JsMT4VPF88o0TTbja4zsSZrnIJw5YnjZfczrJCz6lU5nEJ8aroU6j_352vFYS9UBs2VHlnQM0duaL_c6KuWWU2CmRSOpLMMoUY1BEexjoWm5k76PSNSFe-mHgExnoZI0j4Xp8DYbLGQYuy9fXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامران غضنفری، نماینده مجلس:
گویا قرار شده هر موقع آمریکا یا اسرائیل تفاهم را نقض کردند، قالیباف ۴۸ ساعت اخم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66934" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66932">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quxvzbJAjYCCk7ecuy_ywPjqHeKQDxqHJ8BVnqc7FkU0kNqinZLdE82eZOMb3FO2eSP7GvPgrB7KXueTDm2OH0s5a24-2YJYyDkpRDS8gN4BDXrW_hDrpgy7warZOTxGUpedHV6ZpJM0LBbnb5zEDI20DfVx0V6vwrudPqfyGBRcEOtm6WQDrFwohpyGsAyq5PpNP7gU-Jwimf5bfVgDRsF8L_5m8pfguFlUN92dK3dbrcrmFkkRhTvgU5p3JpMB3WYUZ3lat2BUEHW3mupHBWG6xCVa25_XRvQj1XFVQDsOT7AVzJrlYo4IHfF--2-kY6hzovOFb3na_x3EJXk5_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=BPdQu5xi-GjZPCuQ-jqOzv2g0mk9YVrl8ZUm2uscfewlr8zXFaFclcii6uVCvPeqWhGI5du0eGlDz-MiamlwFg_jh_q01Jv9N98zZgyEGwLiBfjVrdo-FUE_Lt9yvJoMK5Z11pjZKH3EQwMXyBEDv78DigQVKp_Dw0-rGxQUW7TIdNvUy6sosqmGhwjzU8mKWpQpjGNv-jGZ8pANqMZ_SOrGomOcIdzeMorANfLbqH3tvKsN1s9ymy-Gjh4Lw2CGNZhcQhvfr7yyITmMCMT5JRZxpJcQE8qJHsFIb9F-4NVlVZMTXauqdNXQHdRjvGy6H8LxaQTH2NKrJ15gqV3Whw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=BPdQu5xi-GjZPCuQ-jqOzv2g0mk9YVrl8ZUm2uscfewlr8zXFaFclcii6uVCvPeqWhGI5du0eGlDz-MiamlwFg_jh_q01Jv9N98zZgyEGwLiBfjVrdo-FUE_Lt9yvJoMK5Z11pjZKH3EQwMXyBEDv78DigQVKp_Dw0-rGxQUW7TIdNvUy6sosqmGhwjzU8mKWpQpjGNv-jGZ8pANqMZ_SOrGomOcIdzeMorANfLbqH3tvKsN1s9ymy-Gjh4Lw2CGNZhcQhvfr7yyITmMCMT5JRZxpJcQE8qJHsFIb9F-4NVlVZMTXauqdNXQHdRjvGy6H8LxaQTH2NKrJ15gqV3Whw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66932" target="_blank">📅 19:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66931">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=bbalWJXusDVvu7Svt3osCUTP_EmeC2MCsJ48HAW8A08hDESQENvLi7HhqPNzT5eMmenMAO-29cRUdX5x9VsBdNMmQLwhRulLeaj62KMICXdS3MHJtD2hz9jgPHcm48YwuEcPcb28-0n4uLHEkmPJZDqB0XPQyQKzpbx6r4nyuTudCktOoh2-PkCV-mepIG7harJ0tjF8T3sAgcgfbBdWyNBVJ8zw2oEX9o4PvrpLujtyuVyNcGlpRRvMVzUR1YYWF6fCgs0Ix2JlVz480mFrmZZtraGP-ef5ntijsQBNZEUN5aumUF3s__DILN7vDJvDZLpcJ7aTFS3pY4KTbeaH_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=bbalWJXusDVvu7Svt3osCUTP_EmeC2MCsJ48HAW8A08hDESQENvLi7HhqPNzT5eMmenMAO-29cRUdX5x9VsBdNMmQLwhRulLeaj62KMICXdS3MHJtD2hz9jgPHcm48YwuEcPcb28-0n4uLHEkmPJZDqB0XPQyQKzpbx6r4nyuTudCktOoh2-PkCV-mepIG7harJ0tjF8T3sAgcgfbBdWyNBVJ8zw2oEX9o4PvrpLujtyuVyNcGlpRRvMVzUR1YYWF6fCgs0Ix2JlVz480mFrmZZtraGP-ef5ntijsQBNZEUN5aumUF3s__DILN7vDJvDZLpcJ7aTFS3pY4KTbeaH_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نفهمیدند رفتنش فقط پایانِ یک پادشاه نبود؛
شروع رقص طنابِ دار و بوسه مرگ بود.
عکسش رو از اسکناس‌ها پاره کردن،
و از همون لحظه سقوط شروع شد
و نسلی که خیال می‌کرد وارثِ آزادی می‌شه،
وارثِ تحقیر و فقر و چوبه‌های دار شد...
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66931" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66930">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=lwU8DNLGsBfraOIHBq3_lQFiWKJb_zkBSSRqqz6DLzDo-NxTvGpHS_xrjWBOELJ7OG3O-LxC9cxruW5o0h6RmBliOGruki-4w2XowzZZb_O7vGAvNyY1cSwYNhnfyWfDtATCPAZpoIFiKw0BeEny4fsiU7eapekS_uqbXfZJZziaZYI7GqJ37TXPy7jMU0vGGqwugiM-OqGYdMStoi1mzHiPow4yc0fmeKi6x3PVeZ-6ucBGUexOuPqG5uqe9kRt8_mnJkroPyC3rQIm2oL_R-WDJ4x27AyfZ259b-B216fscCk9yDFd65-MlRU79EFm0AYcn-qofa3XBgXa_6VjHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=lwU8DNLGsBfraOIHBq3_lQFiWKJb_zkBSSRqqz6DLzDo-NxTvGpHS_xrjWBOELJ7OG3O-LxC9cxruW5o0h6RmBliOGruki-4w2XowzZZb_O7vGAvNyY1cSwYNhnfyWfDtATCPAZpoIFiKw0BeEny4fsiU7eapekS_uqbXfZJZziaZYI7GqJ37TXPy7jMU0vGGqwugiM-OqGYdMStoi1mzHiPow4yc0fmeKi6x3PVeZ-6ucBGUexOuPqG5uqe9kRt8_mnJkroPyC3rQIm2oL_R-WDJ4x27AyfZ259b-B216fscCk9yDFd65-MlRU79EFm0AYcn-qofa3XBgXa_6VjHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش تلویزیون الجزیره از خوشحالی مردم مظلوم غزه بعد از گل مصر به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66930" target="_blank">📅 19:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66929">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krxVMbbD-b9Fwuz5FsKZYNm3kNf1p5lhEfLs70-VF1Kcg2WBkBzfKOssYd6S-PqKQpZtZAGXN1rBW6az7gcvP2VfMV-ADOhTaPteip8aY1MMIz_oaE-bK4qLWJnsbBh1oWAuvUeAlYNKnDowL0AJVZjHiQLVMJeL-QnU3fTpC2onudC2Yu-rl57_R3Ka7wJooaA7zrkae1DiLZ1s8N_eBKt_I7D8afpybqyk2VQFr04OqFZK_flbrl31s0FLIuqS5OKCBeqT0MYg1OOH-WMl_oQLWPf2QIj1w-mrS2CskYHYqNukBhFxyOyfDBdlCO6O8sTZzow5CPtENpsoAzuDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه به نقل از سنتکام:
حملات ایران به کشتی های تجاری را نادیده نخواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66929" target="_blank">📅 18:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66928">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=m3lcvhFppsqx7nOibf1MH2AX6CoKq17Vlz0JbFbGJN0PdUc7Bpbmds0sLVib5qYHL1qqW_3zfrmGo-apX1ZBimtPDq-KI5mTyOh0VVQu4B4twLEpAD8FELD5tby84xISQ_PVXK7dd6yp7rB9BUcRYqNBLXiEb134hm7pDIE9PGaykQ8KakiE1JH7gQ7S-kqcAiDF9ZpLbOGqMxGcdwnMmdKATvAxglyAvveqrXae33msAfM6a3JAuDDSzzd65uJ6Fff-6dpK2hDVZHsNueJ24W0z_gLSI45Z0zhJq17R5JbUw1pLUpoP7oM2Bnm77IV5ywahH9VXG5PSTst2WLs4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=m3lcvhFppsqx7nOibf1MH2AX6CoKq17Vlz0JbFbGJN0PdUc7Bpbmds0sLVib5qYHL1qqW_3zfrmGo-apX1ZBimtPDq-KI5mTyOh0VVQu4B4twLEpAD8FELD5tby84xISQ_PVXK7dd6yp7rB9BUcRYqNBLXiEb134hm7pDIE9PGaykQ8KakiE1JH7gQ7S-kqcAiDF9ZpLbOGqMxGcdwnMmdKATvAxglyAvveqrXae33msAfM6a3JAuDDSzzd65uJ6Fff-6dpK2hDVZHsNueJ24W0z_gLSI45Z0zhJq17R5JbUw1pLUpoP7oM2Bnm77IV5ywahH9VXG5PSTst2WLs4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
صادق خرازی برادرزاده کمال خرازی اعلام کرد عموش بعد بمبارون خونش زنده میمونه و تو بیمارستان بستری میشه که موساد میره بالا سرش و با گاز خفش میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66928" target="_blank">📅 18:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66927">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2861d69191.mp4?token=GgEkcE6otmZrT3AjNBYYqaIQTfPy7APys7lJol-IgEeCQu0YxrsszG-mPJ9mgJDT73QCEXkGM-sAebkaYj-IGaUgbqX7evJ5iKk09UmOgh2X0pSDZpPbFmVluUoucVj1x9HoaYbtU91czJvxp9AbONMS-Q_8z0ub_5hnxl-we4GpRn8oo64bX00taDFeXXz1AAucC9LdvKaNwra-WRwH3wf2_Tx4Juo4ytYKpiwX9OUuqDlr_7u08ZtyL9DxoVsyy8dAA4EmoLOAg3lx8Em18uF6xJu8BlITLQoxGZg4g5EspbkU2sJpt_M2Hvjew2LCmo4cSCWRU0M4P-ligj7XrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2861d69191.mp4?token=GgEkcE6otmZrT3AjNBYYqaIQTfPy7APys7lJol-IgEeCQu0YxrsszG-mPJ9mgJDT73QCEXkGM-sAebkaYj-IGaUgbqX7evJ5iKk09UmOgh2X0pSDZpPbFmVluUoucVj1x9HoaYbtU91czJvxp9AbONMS-Q_8z0ub_5hnxl-we4GpRn8oo64bX00taDFeXXz1AAucC9LdvKaNwra-WRwH3wf2_Tx4Juo4ytYKpiwX9OUuqDlr_7u08ZtyL9DxoVsyy8dAA4EmoLOAg3lx8Em18uF6xJu8BlITLQoxGZg4g5EspbkU2sJpt_M2Hvjew2LCmo4cSCWRU0M4P-ligj7XrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سلیمی، نماینده مجلس:
اگر حزب الله در بیروت نجنگد، ما باید در تهران و کرمانشاه با اسرائیل بجنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66927" target="_blank">📅 17:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66926">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
این توافق باطل و بی‌اثر است و مفاد تفاهم‌نامه ایران و آمریکا باید اجرا شود.
این تشکیلات، ادامه اشغال را برای سال‌های متمادی مشروعیت می‌بخشد، امری که می‌تواند به الحاق این سرزمین‌ها به رژیم صهیونیستی منجر شود.
ربط دادن عقب‌نشینی اسرائیل به خلع سلاح مقاومت، پیشنهادی بسیار خطرناک است که از تمام خطوط قرمز عبور می‌کند.
ما به مقامات لبنان می‌گوییم: وقت آن رسیده که از اقداماتی که لبنان را ویران می‌کند، دست بردارید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66926" target="_blank">📅 16:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66925">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23291f5586.mp4?token=thksge3Hv2N1-k4oh4a7n04qtYbdCBsjdXEo1ZZBsORx6KT58zcBu_u3DkopQv8L40b28yEDWUtxXfoLVo498-6tSguQeCeXlgtUiGl4Xll5xc8QEURtwK7nEKK-BC5M8XXbymPjrHUz83xycjtbZ9J7U8-EJugZphRuDfa-g4X4w8gY7Nn8qA6o4LhDLLCuTTi8J4RPO7eCwiB61bQtNBh8tgqxVbxAHALR-NfMoGPN_Lh35fBCbFIqotGoFevgK8vo10dPqXITY9tIWhevnFI4r2Ef3FgF8MAl3G8ydPIf7b2zO8MEvrPYk_J3K6UGSTgEx3PqtSwqxaz781oAig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23291f5586.mp4?token=thksge3Hv2N1-k4oh4a7n04qtYbdCBsjdXEo1ZZBsORx6KT58zcBu_u3DkopQv8L40b28yEDWUtxXfoLVo498-6tSguQeCeXlgtUiGl4Xll5xc8QEURtwK7nEKK-BC5M8XXbymPjrHUz83xycjtbZ9J7U8-EJugZphRuDfa-g4X4w8gY7Nn8qA6o4LhDLLCuTTi8J4RPO7eCwiB61bQtNBh8tgqxVbxAHALR-NfMoGPN_Lh35fBCbFIqotGoFevgK8vo10dPqXITY9tIWhevnFI4r2Ef3FgF8MAl3G8ydPIf7b2zO8MEvrPYk_J3K6UGSTgEx3PqtSwqxaz781oAig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو پخش زنده ورزش سه چخبره؟!
به جوادخیابانی میگن چرا انقدر الکی از قلعه‌نویی انتقاد کردی؟ جواد هم قهر کرد و کلا از برنامه زد بیرون
🤦‍♂
🤦‍♂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66925" target="_blank">📅 16:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66924">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=XLfulJ4yLvKWk7dBQ8AgbM3h5Iplv3r-LIX0dhEaP7jLNUh7eZ8QfKa0-KINZSu53ODlhl62WYvPFB9k9ezu2dwDXNrdKxkPtWOs6NutL70mCP5fuTeA4La5OVB-7wPVZAS6bRrXQyMLB7mjPQfnSPSTXBas7xW1mrzT1RDT8WJYhFko70xGR-ozcGb1-bk-86cAYvmjjHrm4XgCP8Ib278aYNNsHLZ0g1DOZhlOzUYYTVCx7X2Ho_gi_tYpHWzQkXK-j-d8qZ659bN233KhR7v_q5SLyTVud_FvlQ119fWqdleabShvIqKK7aFoPEhvSDLkYFhZVj1T5wWSrvlcsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=XLfulJ4yLvKWk7dBQ8AgbM3h5Iplv3r-LIX0dhEaP7jLNUh7eZ8QfKa0-KINZSu53ODlhl62WYvPFB9k9ezu2dwDXNrdKxkPtWOs6NutL70mCP5fuTeA4La5OVB-7wPVZAS6bRrXQyMLB7mjPQfnSPSTXBas7xW1mrzT1RDT8WJYhFko70xGR-ozcGb1-bk-86cAYvmjjHrm4XgCP8Ib278aYNNsHLZ0g1DOZhlOzUYYTVCx7X2Ho_gi_tYpHWzQkXK-j-d8qZ659bN233KhR7v_q5SLyTVud_FvlQ119fWqdleabShvIqKK7aFoPEhvSDLkYFhZVj1T5wWSrvlcsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ونس درمورد سه قطب قدرت در سیستم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66924" target="_blank">📅 15:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66923">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=B__oPwVIHAMh4iJW5hYctSkBUOZh7ajiNt3BgeBNo6WcQucmqpvbYA1wwoeaPmUhLytLTsH5E3jjGObZlM1ub9jG9eV2_bYbsMTYarr5qeiOQuauaTA0OPszAEKXs70qxbIrbbKM9a-UPJQDNW1Z1nLL_Px3w931nCQEsJ84ZT73Zha1b6pfpP_gupjrxcoQKkk9s7N5wFmYM29E9r88dDOBpbiB0XQtxDU8ls9lwHKxVvn14Do5t63we2MMItmy_SFfBIKQEoCgmEnPyKAVDWH3gyilDXoKU7SL8HDcg9_iUfryuov4-HlW-cQ7qSV3YD3Z-9Mb_Sf4gRr9gzGjRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=B__oPwVIHAMh4iJW5hYctSkBUOZh7ajiNt3BgeBNo6WcQucmqpvbYA1wwoeaPmUhLytLTsH5E3jjGObZlM1ub9jG9eV2_bYbsMTYarr5qeiOQuauaTA0OPszAEKXs70qxbIrbbKM9a-UPJQDNW1Z1nLL_Px3w931nCQEsJ84ZT73Zha1b6pfpP_gupjrxcoQKkk9s7N5wFmYM29E9r88dDOBpbiB0XQtxDU8ls9lwHKxVvn14Do5t63we2MMItmy_SFfBIKQEoCgmEnPyKAVDWH3gyilDXoKU7SL8HDcg9_iUfryuov4-HlW-cQ7qSV3YD3Z-9Mb_Sf4gRr9gzGjRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
تصاویر ماهواره‌ای از قبل و بعداز زلزله‌ مهیب ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66923" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66922">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgC2Gh9lAPm-Sytlwe2MJTZn0rqvEs3J-UCCWAPQrj0nk6V4ZkS58U6al_JP2ND2Q4Y87FE0ldZt8J3Xiyec8Sxd90KdvKgTYbDcym4oF3igqADc03jFYzWqZNELx3H9ctOfbM09GKwN46UusthHhmknOZO1NuOZ7qrarPkPJdi43TpuDlFXA6WHTGhclawMrmnm9sDLQJ_73i1LTO03BacuYhZtnj4Rp2ZlM0MrmXAcU5WNs46JXijcKFYel5x3_ystu__2KakJ_jdEXMIi5ErfkKpMwou1vSqsJVfTKqF6ulhoD2JopNVfjzPh-TYPwHZVuRyDILZwTjHYX6EsIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
پاسخ به ناقضان تفاهم‌نامه سریع و کوبنده خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66922" target="_blank">📅 14:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66921">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
⚠️
صابرین نیوز:
این نفتکش، برخلاف مسیرهای اعلام‌ شده از سوی نیروی دریایی سپاه پاسداران، قصد تغییر مسیر و عبور از آب‌ های عمان را داشت که در پی بی‌توجهی به هشدارهای مکرر، مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66921" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66920">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTs5JR1aXXhEBrHTmfNOT_qQlCt92QoPp_z6VsTp70s_DVlTXqIZIHCLjcz7zSkFbLKIpOJDfTFWqPyxG3u8o38jUJR_byDTRMgnKXz83XNSL91HZUm-Yb2FVgmZD3bkqp2TAwFEzJnLVC839GiQUaJrHCtbExrYmC3D5h20gzjTv6tmmdsObB53DT1u1NVWHa8ppnDm25JprLk4NCnk1oi4rEnCFl_KroWoi019jWFMRvtiGLGG5cwWFMUA7_TcSPsSHQKqCKEGlI-xdUdP5-xHLiHykGqY8NMjEtzathI_MaDF6L4oBmsaZNe-DzZHtOUIOPcMVxPvUV4relc94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛لحظاتی پیش اکانت عملیات تجارت دریایی بریتانیا اعلام کرد یک تانکر در شمال کشور عمان و در ورودی خلیج فارس مورد اصابت یک پرتابه‌ی ناشناس قرار گرفته و عرشه فرماندهی کشتی دچار آسیب و خسارت شده.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66920" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66919">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
بحرین:
صبح امروز جمهوری اسلامی با تعدادی پهباد به ما حمله کرد.
ما این حملات را با شدیدترین عبارت محکوم میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66919" target="_blank">📅 13:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66918">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvWRSqtPgJWEfT1gkr_wSEesoZpL8nGvhH4NcMUpsB31gE_Lyv85edsGJuXtiOXPZdAXipPfWsjloB1n5i1L472bCmQfxHOjcH6H67k_CGjgIwzkJpiGBiSqxH7BG9skAlyvVcQgL6QgbfoYbSc_6JEob2SPj3O7H8_4ioDTHhZNr_2vDJK-CXYnsF5TDavFFhYD1Ds7CI-VXq8Ic-QOXiaJKOembwg4uPE9hNeLrho8c0qi5-f7Lw5ck2yY_b6fGsaqUdqv5MslcUpiSZMhWlEmEfafS-QfdUPf4SdTy2c1rcjk9aDfdVTfZtYdJvMl-nkbi4w66FKaeqoG-H_r8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نبویان:
ضمن تشکر از سپاه قهرمان ما به خاطر پاسخ به تجاوز دیشب رژیم امریکا و در نتیجه نقض بند یک تفاهم‌نامه، مطابق بند ۱۳ قبل از عمل به بندهای۱،۴،۵،۱۰،۱۱هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود.
منتظر تحقق شروط و واکنش شفاف و پشیمان کننده‌ی مسئولان مذاکرات نسبت به نقض تفاهم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66918" target="_blank">📅 12:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66917">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=bynGzpRYPjR8mCLsLwumKO0O17RBUGUCAP4Bc0HyzoE4NRQIZSe3T606qyWS46_T1KSbWB5DCT4zTazMZGnT4jfvv_ijhsmSzrnhrEIvsC_bkl9AnTb2QWq7l3_VH4YHzQAIy8MjhVuCsDdnRTQv_4F220VA6tnu9nh9v8I5i56q_ELelmP3gFNTnf0JkXGN1RmncW-U-tJZzl4DPTNnYG7fWO7-D1YNrDAx8jW-h1RXLGweQscT-xitxRI_vDl36-fWfjIFLhuvQm1iOqftngGFMM8rdqbxcKqpxIIq7u3gjmrUpTF_PBCU83oQTGq1_jxf427W0U-b5dgOegeWiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=bynGzpRYPjR8mCLsLwumKO0O17RBUGUCAP4Bc0HyzoE4NRQIZSe3T606qyWS46_T1KSbWB5DCT4zTazMZGnT4jfvv_ijhsmSzrnhrEIvsC_bkl9AnTb2QWq7l3_VH4YHzQAIy8MjhVuCsDdnRTQv_4F220VA6tnu9nh9v8I5i56q_ELelmP3gFNTnf0JkXGN1RmncW-U-tJZzl4DPTNnYG7fWO7-D1YNrDAx8jW-h1RXLGweQscT-xitxRI_vDl36-fWfjIFLhuvQm1iOqftngGFMM8rdqbxcKqpxIIq7u3gjmrUpTF_PBCU83oQTGq1_jxf427W0U-b5dgOegeWiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شیر تعذیه به جمعیت
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66917" target="_blank">📅 11:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66916">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=Ncm46_2bEu6Z8BGvTmHFjjrB_iJegPM_SmC3EeLx3TNkkG2DHLCM5kEF-I97ImcO0v1NtqcLLOMr_46BlqvmM6fUQ56eFX5n_Ag5v7azb5FuX3tO8zfUhdQQF-fqbagULrgoX4znbRwAf3cp7K94BIl0EewHm88VMXLg2NZ0L3OVYfoHCLdA21jJM5U3b3hwn_agrcKKnndfbmim2GJusDmacExwOm_vfINWY5BvmbnUWSGPaHFUw_2OqJxUf3WKeKp1oLWDphJdrZTnedy1_Odc4EYBv5Wpf3hTQWZV04waTPnPuQPrV_mTqe7bpxEMF4h6Bkrl69sDL4T2dTnE_qm8cERdV9VQb2xhM-fz0lAqD8n-lc_yLJb2Qp121AI5GjV80yR_dX52YPDn7NedYzgaSKsrd5Z6FBRhlBniGABk4kRKGk7h1C_QPkhrUzbiN07Bg-95Map9b5W2UR2L24rc4Zb29NkCwCQg3L4WsXwCiOsidFNljgRJwzcrFtxsFiHY7A7W9MmzJQGNso8zRPMXivOucb1hqB8HdCtVr85dYzY4v11fijnQ049oW1mKXN5mJg45kY_RGD-7FATCrn8AmcQYcSUx4YZPKOFtGpCa0LAkT4dtotfkV1zYZdA8uAzocNj0iDyVZf5wGO8EH8V9G1JfH__5wWSFuMpkki4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=Ncm46_2bEu6Z8BGvTmHFjjrB_iJegPM_SmC3EeLx3TNkkG2DHLCM5kEF-I97ImcO0v1NtqcLLOMr_46BlqvmM6fUQ56eFX5n_Ag5v7azb5FuX3tO8zfUhdQQF-fqbagULrgoX4znbRwAf3cp7K94BIl0EewHm88VMXLg2NZ0L3OVYfoHCLdA21jJM5U3b3hwn_agrcKKnndfbmim2GJusDmacExwOm_vfINWY5BvmbnUWSGPaHFUw_2OqJxUf3WKeKp1oLWDphJdrZTnedy1_Odc4EYBv5Wpf3hTQWZV04waTPnPuQPrV_mTqe7bpxEMF4h6Bkrl69sDL4T2dTnE_qm8cERdV9VQb2xhM-fz0lAqD8n-lc_yLJb2Qp121AI5GjV80yR_dX52YPDn7NedYzgaSKsrd5Z6FBRhlBniGABk4kRKGk7h1C_QPkhrUzbiN07Bg-95Map9b5W2UR2L24rc4Zb29NkCwCQg3L4WsXwCiOsidFNljgRJwzcrFtxsFiHY7A7W9MmzJQGNso8zRPMXivOucb1hqB8HdCtVr85dYzY4v11fijnQ049oW1mKXN5mJg45kY_RGD-7FATCrn8AmcQYcSUx4YZPKOFtGpCa0LAkT4dtotfkV1zYZdA8uAzocNj0iDyVZf5wGO8EH8V9G1JfH__5wWSFuMpkki4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک آخوند:
غلات آمریکایی آلوده هستن و میخوان ژن مردم ایران رو تغییر بدن. آمریکا قبلا شکر شوروی و برنج ویتنام رو آلوده کرده. خون هایی که قبلا برای ایران فرستادن هم آلوده به ایدز بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66916" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66915">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlf3k9TXdq8D44ve_uadCLO5tJwOJMbkafc9XA6e6ITVCvjqOgP4Ln681-ffb2P8hxEq9KPQdtfoictJbf77s8tFiz91JzG3to4o7cf58YM1J2cQMhc-0sFBHWoZXles4PGF3y172UR7QIN9zlGpSScw5vp-x7JGmebZyvScbzB_Ij2XIcWbCaB5SWDCER6GzkZsdJg14f_KImnxIA2u3jJKyi-9nr1qt7gFzxjiH4DDuDd2bmD7fpa1ZmQMavSPJnCVK5qDqzx2EBaWFlRV8Yp7saR38PHmjeJysQ_Wjsag2t6Kr69l5We61lfi12YNkQFDD0NCL0BnBNc4En3A_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
نمایش هوایی چهارم ژوئیه، در آسمان واشنگتن دی‌سی، پایتخت بزرگ ما، بزرگ‌ترین نمایش هوایی در تاریخ ایالات متحده آمریکا خواهد بود.
صدها هواپیما از انواع، اندازه‌ها و سرعت‌های مختلف به نمایش درخواهند آمد. من حدود ساعت ۹ شب سخنرانی خواهم کرد که پیش از آتش‌بازی است که باز هم، مانند نمایش هوایی، تقریباً ده برابر بزرگ‌ترین آتش‌بازی در تاریخ کشورمان خواهد بود.
پس اگر هواپیماها، آتش‌بازی و دونالد ترامپ را دوست دارید، آنجا باشید!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66915" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66912">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhYx6bnAVroOoIUDEcnLljcxhNe8hxDSN1CsHaSeIenouILd2uBxEN35iOLtpwLBgQVSzJMde5AH3J7FMHeJ17Be6dXf9BsSXm-C3mRE7cjvwDuYjnyS18WMB-dGdCOBZ1PxcT8VLXofX4q1b7vUE0MtpBC30B5-stb7jF2QVPu_4iiiL5GIK5XGS1WUmDCcTYZNQKs3_ofBbD4CUCQ5tDtvhXbnD5XY9lENJNB-W9OlMw9Pki8wrXx4_RpAMTxyu6GOlcFLj4JOm9JuviODvCFzBZCqHyP9JFXuLOF4FTVOhuoJf9hV8bSgMtydZu9z5ZLmagKHKtwxvugnth73oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJJn9gM8OEL-Wy9GzVzbXm_kop0eBm6ncb_RsketF2hyZE82D59rBZuX2DTCRAwl5lAx6bgykV23BhUPxBXz1Yg_NXFC3o53-wSYdp-T7iqzOP5TfM9BWIpPydXFF2aEchRdowAAJzRW0eT1KPlYWnmUDrYuq9HH3is-WWsCfqWyeGwL1noKgenMWLyt_UCaD1zm3K34Hr7wn5QQQXgo75MiL0_ATLhWGQUp_HKZvak2Sax24i0xX0xfJM77mHL15_5eqLSsPc-3Gm2hR5Fc_gvl-8v2Z5KWWDpgVKRGbThCIZgnyCZF-j6QWD99rZz4SFPKBwWfolhmZx3m2Z0rcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=oZQYx_UDDBEWf21Y5gapWIyvSR9fMfumnAe6Vl1TEE8hHtMrpHSrQG2AgJh9LI6l9LTIT0Kwn2S5AXnZwyUN9iY9Hu6hJwLaEoltZX3iWzCRrzEXfg-cfbZ_SBZ9Gv96feeBaUan75VKEXktMchx-dI3XzFs_NERW_yXIRZIMgH9Celmfb81_zKSKprNIOmtHIjVt6SIbeTMzWqchL1ZJVX0eXcQwBQYSx7tdw28vxOtN80VaENQX8S7thvhl6-JZjGIUNyrLBCL358bPLfJdKX9FQfDfqoYujsKJpnBqIxllfkhDI4CbIALS2RcMeTrjmKtBUJccVm62aSut0d7jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=oZQYx_UDDBEWf21Y5gapWIyvSR9fMfumnAe6Vl1TEE8hHtMrpHSrQG2AgJh9LI6l9LTIT0Kwn2S5AXnZwyUN9iY9Hu6hJwLaEoltZX3iWzCRrzEXfg-cfbZ_SBZ9Gv96feeBaUan75VKEXktMchx-dI3XzFs_NERW_yXIRZIMgH9Celmfb81_zKSKprNIOmtHIjVt6SIbeTMzWqchL1ZJVX0eXcQwBQYSx7tdw28vxOtN80VaENQX8S7thvhl6-JZjGIUNyrLBCL358bPLfJdKX9FQfDfqoYujsKJpnBqIxllfkhDI4CbIALS2RcMeTrjmKtBUJccVm62aSut0d7jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت (حدود ۵۱۸ متر) در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
در اثر این برخورد، دو پنجره ساختمان شکسته شد و هواپیما کاملاً متلاشی گردید.
دود غلیظی از طبقه همکف ساختمان، جایی که لاشه هواپیما پراکنده شده بود، به هوا برخاست.
شمار تلفات هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66912" target="_blank">📅 10:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66911">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFe_kQ5s1Svw0XvkIBCKHF-GsdX0x6JkqrlakBOr56BFtx7Xoj_zFn-CidjsVwlgwUBCR84UIkueSntFaLwaCBQ1IPiGz9RfizZMblQUZ2Kdgm4SLbFUBFZcGJUNlOrOpJu0C_Xlgk429Z-oN2z6mQQ8Fbh3YlGJNG_UnFJJmu8I1Y366OiomUBJKhLzjKmIKiFBB0YNPSGCZG5BwcoTfwRMF1-J5EqgnDlzHwA9wrTgRfOjXCAkPSoocmpyg8sM9u7vrONQXfUgZqAJ2BnhlQNf9xUDug43BJ6IGhu1I4qwtkr3wDR-4NCj6P1x1Iq2wrlH_I067rEFQHFbcei_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
🇺🇸
آیت‌الله جی‌دی‌ونس:
ایران توافقنامه آتش بس امضا کرد. ما آن را گرامی داشته ایم. اگر آنها در مورد نحوه اعمال تفاهم نامه اختلاف نظر دارند، می توانند تلفن را بردارند.
اما خشونت با خشونت روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66911" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66910">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=gyti1GN5WrUVAuhza-Ktwqv8Ev4VgBN0rCMzDCrhQF3PAIWni3shtCJGf4QPF9qmqyThHDxUKIZWFzsHdECIE3NFWUojmjttu65Eo7h358GABaJb5pXvD7jVfCJ7NGc4OllFaFl5gnT8jVxZCaLhHQnCb6hi411iuFm7pQGimaYfq88liOpY38wxR8kDKPS9_AZrneB8d3Xy54-Cc0CaRsLQ2LUfVeo_drlkN7yi8oY_KMuaU_u0_b1MaevAHb0sl9dfPXsSkCkC0rGxZpQuCgqK-cV1ibJlSzrrU-Dm9BIG_r2NQx_Rr3oWmzRvD8XyaQvle4U_Raf1FtY27hOE5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=gyti1GN5WrUVAuhza-Ktwqv8Ev4VgBN0rCMzDCrhQF3PAIWni3shtCJGf4QPF9qmqyThHDxUKIZWFzsHdECIE3NFWUojmjttu65Eo7h358GABaJb5pXvD7jVfCJ7NGc4OllFaFl5gnT8jVxZCaLhHQnCb6hi411iuFm7pQGimaYfq88liOpY38wxR8kDKPS9_AZrneB8d3Xy54-Cc0CaRsLQ2LUfVeo_drlkN7yi8oY_KMuaU_u0_b1MaevAHb0sl9dfPXsSkCkC0rGxZpQuCgqK-cV1ibJlSzrrU-Dm9BIG_r2NQx_Rr3oWmzRvD8XyaQvle4U_Raf1FtY27hOE5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی:
اینم یه ازمایشه؛خدا داره منو میکنه
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66910" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66909">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=PDiiO3IXLhEri4L9UeiIlNtbtzmd6muDXpQmq7K9c2mF7C6cnAMlxCmRTV6qDVKp8S8QHaKBg2pDyBI3GNMOL8Hd-g-BmFrNzBEosURYEr2n0QcxjmM4-ZTU5Ju5w33pJCMzQy3_61uUg1E8LJqrwodaMEpwflSE3XbXMqBTUu9Sl4zdchsRtsnQySKTlbs6ed-SuAQl3stvvvHI3pb-lqHxVPZmmKZlXq82TLCkbtHxibESkgWds854kbjnvH6qHqJucPRYkep7GlpzqCsoa9VTZfKErnuculFfTklThe3GwnszXCsp6R1_Tw9EzjdQ0_wKx7Zutj0e0yJb2X2wCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=PDiiO3IXLhEri4L9UeiIlNtbtzmd6muDXpQmq7K9c2mF7C6cnAMlxCmRTV6qDVKp8S8QHaKBg2pDyBI3GNMOL8Hd-g-BmFrNzBEosURYEr2n0QcxjmM4-ZTU5Ju5w33pJCMzQy3_61uUg1E8LJqrwodaMEpwflSE3XbXMqBTUu9Sl4zdchsRtsnQySKTlbs6ed-SuAQl3stvvvHI3pb-lqHxVPZmmKZlXq82TLCkbtHxibESkgWds854kbjnvH6qHqJucPRYkep7GlpzqCsoa9VTZfKErnuculFfTklThe3GwnszXCsp6R1_Tw9EzjdQ0_wKx7Zutj0e0yJb2X2wCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه رامین رضاییان بعد بازی
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66909" target="_blank">📅 09:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66908">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=BdS26E3SO6jNfAf12G68NAGI_bwpHpzt0hSTv-HNWcyus70WMT7hA_M0CM0cZWi2bP1wpp5Ttmh8xb0MJZj2zpRFZvhTwWc_0hIKNhjzjvA1k1gsmqwmUVNinXhWC8v7FUKqX6IiUmlAYEf8IUvnfTGjH9PSESNwQcp3geIpssdYQsMpX3jr7-ouG48Mt5Dw7pMHhaXJJoC37tB7CViYf5gjaSNKVsBeR9RBWK4ogMTH_AaT6YuO6JSdeHahEqyzzwCelg94n70A1_SgOtMw21sIjmMigFbHlW6X0f4TbFqtsU_z_kdBmx168N3-QTnEiL74KwY8pCOD9ADuql6J_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=BdS26E3SO6jNfAf12G68NAGI_bwpHpzt0hSTv-HNWcyus70WMT7hA_M0CM0cZWi2bP1wpp5Ttmh8xb0MJZj2zpRFZvhTwWc_0hIKNhjzjvA1k1gsmqwmUVNinXhWC8v7FUKqX6IiUmlAYEf8IUvnfTGjH9PSESNwQcp3geIpssdYQsMpX3jr7-ouG48Mt5Dw7pMHhaXJJoC37tB7CViYf5gjaSNKVsBeR9RBWK4ogMTH_AaT6YuO6JSdeHahEqyzzwCelg94n70A1_SgOtMw21sIjmMigFbHlW6X0f4TbFqtsU_z_kdBmx168N3-QTnEiL74KwY8pCOD9ADuql6J_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فرماندهی مرکزی ایالات متحده (سنتکام) ویدیویی از حمله نیروهای آمریکایی به یکی از اهداف مورد‌نظر در ایران را منتشر کرد.
حملات سنتکام در واکنش به حمله پهپادی پنج‌شنبه سپاه پاسداران به یک کشتی انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66908" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66907">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
بازی تیم جمهوری اسلامی و مصر با تساوی ۱/۱ به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66907" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66906">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66906" target="_blank">📅 02:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66904">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O_cE9SgDQd1pwdariR66FhFir45z0Gr-iyDRT_3v97G726nKHNm2TDxl2O_w1hRh6J49eYyt2WWlCPHoBE5sB19fAwMxU8ezJUoOJtmUzyZZaWts16TXOQFrhR0tkTyDZ1CjG6nSddg5V4TQX1GeUPt93TwmAJRbiO9eLep67jk-U2xNM4i33xnO4Tv3vNFrbVN_YCYKrgPS0yBAgYpAc9Ha3ZIm1gj9erV95cIXLKluhaLG2_pFWM2QOdmMF3wBHyryCD5steNk4fafPnDRkSRKlQq0HH96mVpqJf0JLKWfnXvAhw933Asc4TL6RriohdZuyT1Onn_dwVUQDJvgNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66904" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66903">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان به نقل از یک مقام آمریکایی:
حملات آمریکا در ایران اکنون به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66903" target="_blank">📅 01:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66902">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه پاسداران در واکنش به حمله آمریکا به سیریک:
نیروهای ما موفق شدند این حمله را خنثی کنند و نیروهای مهاجم را وادار به عقب‌نشینی کنند
ما تأکید می‌کنیم که این تهاجم بدون پاسخ نخواهد ماند و پاسخ ما در زمان و مکانی که انتخاب می‌کنیم، سریع و قاطع خواهد بود. هرگونه حماقت جدید با پاسخی سخت مواجه خواهد شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66902" target="_blank">📅 01:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66900">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=SmODPcvYWmcx9mT3qKbV8YtcoAb4Pv2T8BCZaMz5i94vngUReGgy0ZEahvsA0NauBS08h2hjGnllN6_PHpyL3E9wqo5d_YDjFSJ-AC1GpQtq68Aln4uW7DFRv2ljWJpvCDKQhX4mm_QvsYU56q240yVpnCJM0hDsjtHyIxxktkAkcO7o3gBqjZBQ_Odk6lrYVa0weMeAGsz08ct60k4e1KzGEgRy3wh189GlU1WieNnusoUCwPGCKdU5uOxFlAkXOh2UB0uqLHs-o1avXfgPlu9zqSK8e-ZYxwaJoFTD0PyXHWGxdRvJtw_9iCAE2IqEhqTA7oKhd00szx3hajRAww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=SmODPcvYWmcx9mT3qKbV8YtcoAb4Pv2T8BCZaMz5i94vngUReGgy0ZEahvsA0NauBS08h2hjGnllN6_PHpyL3E9wqo5d_YDjFSJ-AC1GpQtq68Aln4uW7DFRv2ljWJpvCDKQhX4mm_QvsYU56q240yVpnCJM0hDsjtHyIxxktkAkcO7o3gBqjZBQ_Odk6lrYVa0weMeAGsz08ct60k4e1KzGEgRy3wh189GlU1WieNnusoUCwPGCKdU5uOxFlAkXOh2UB0uqLHs-o1avXfgPlu9zqSK8e-ZYxwaJoFTD0PyXHWGxdRvJtw_9iCAE2IqEhqTA7oKhd00szx3hajRAww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
اغتشاشگران در حال حرکت به سمت مقر های دولتی در بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66900" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66899">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66899" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66897">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2dJUbzTQauCO_ciIKS3yxYF1vuNa320SMxZanGwEG7MQgJzfkej5AKvTjcdnvBrV8T4RiKR3RHUl4ON5OGtKg_xgFiAmOFDc87VWwQFm6LyAtG3hcPg5TJAC0Pi2kIDAih5FLgWHt5dsajT1LLVb7pdieGGg25jKETqrStR79ftFIZaosNa-hRsQJP_hScKG23QTMe9PoIgmFoD3-kzninrf3ugm0NZfqjUAvm9SJK-hwiYVQO_G9T-_kptkP_JwFUTIvneZGTjs7Pthb1llfEMppwPRdIxMNlzHdSkiWxUeNbMvPzNFRMkeSB5Rp24vh4zNoNknBGeivlmfC7k4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c146777e05.mp4?token=EbgxtbDcb2BmiUDVsLPYzXgUhpLws2CD0LsRERn3s-kFDyGHaT1DdDmLgKD7iemebeEXn0D70sOY-OfxlEN1C_jFNVU3ikwonWWa_SqFXIWOjmnQKCV7o5nxd9rxAhXwzpFh1KYVkGfr4SQMch9t-PY6CxwIDLf3uECAduhNIbUWXr2_EdBxNFeykmFuKIuthshKac3OntZ26J9iizhf6oaGxjzB9_8yvXFqP4OkjqLIqbHXVowkr404DW6KY_a3UPosGqO6YdwRbc1s9rPj6xrtVUbVR0wXbCSfeHWPcYYPRYdyiHlHH4fC8KDiIMaGO6rgWi0XnT1gnqg9eR1PcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c146777e05.mp4?token=EbgxtbDcb2BmiUDVsLPYzXgUhpLws2CD0LsRERn3s-kFDyGHaT1DdDmLgKD7iemebeEXn0D70sOY-OfxlEN1C_jFNVU3ikwonWWa_SqFXIWOjmnQKCV7o5nxd9rxAhXwzpFh1KYVkGfr4SQMch9t-PY6CxwIDLf3uECAduhNIbUWXr2_EdBxNFeykmFuKIuthshKac3OntZ26J9iizhf6oaGxjzB9_8yvXFqP4OkjqLIqbHXVowkr404DW6KY_a3UPosGqO6YdwRbc1s9rPj6xrtVUbVR0wXbCSfeHWPcYYPRYdyiHlHH4fC8KDiIMaGO6rgWi0XnT1gnqg9eR1PcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اغتشاش هواداران حزب الله در بیروت در پی امضای توافق اولیه میان دولت لبنان و اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66897" target="_blank">📅 00:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66896">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات آمریکا به اهداف ایرانی همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66896" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66895">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7MJP6j1WDyYlP9MaGsXGuJwyD7n_mMJhleQ7DM0qV7dDNh2qpByyQ129engcEBdp1R2XeQ_TxwDa8iPBU_iZ59erFsswEQARydJrEIaXY39X0DHSvXhJ0S3DcY8csHFNe0dMZXft1m_hbJfx6cDY4HLibqJzf8NludgW82kcWk-gwW3YQcCjSC2JxHxqDhf0e2Sda21flc7dpB8crpU97uz7X08GX6Ep549DqiXk1j8Kx-vDxCbVH24nSxmCiufYJTF_wRy9W39ta_V6P634Wx-5hJq9Y7G9ifdVYf9Q13NWkIE4TK2-vvqbvhPtqyhg9488eTOR2lPd0ApDc9aGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۲۶ ژوئن، به عنوان پاسخی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی را علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک طرفه، کشتی M/V Ever Lovely را هدف قرار داد، به محل‌های نگهداری موشک و پهپاد و سایت‌های رادار ساحلی ایران حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/66895" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66894">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛باراک راوید به نقل از منابع آمریکایی:
ارتش آمریکا به اهداف ایرانی در منطقه تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/66894" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66893">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
❌
صدای انفجار ها به «طاهرویه» در سیریک هرمزگان مربوط بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/66893" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66892">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=sX4PhEi1b5_UBKoaODG_Ec35-dwL3WL54Y1YDyzdraPt-DVpSQxXpR__BmWmYcMUTB4KN8l4qjPYKzVuBtYsn6fykJ1IYG9eeGhSk1CgpfgdNX59h7knwNrVFcC57-Wn9DfkQEa9sFVRZGVzR6_8P1ZPuPTPYAQPn5QF2d3G8h2VQTo9v0616yOAlnXgpoitJi5QaIox7QZJW6elOC90F-5JHNz41zWlmUghUW5Jvy8_1FM2ec6DySzvUM6HwF0xvmydG7EIqy0Hq5kU7JvF5geosK-XPVM9WI-x_uE0HrMnBtKtK789n5zuvvmxJ137biL94VVSFY2bunNWgohibg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=sX4PhEi1b5_UBKoaODG_Ec35-dwL3WL54Y1YDyzdraPt-DVpSQxXpR__BmWmYcMUTB4KN8l4qjPYKzVuBtYsn6fykJ1IYG9eeGhSk1CgpfgdNX59h7knwNrVFcC57-Wn9DfkQEa9sFVRZGVzR6_8P1ZPuPTPYAQPn5QF2d3G8h2VQTo9v0616yOAlnXgpoitJi5QaIox7QZJW6elOC90F-5JHNz41zWlmUghUW5Jvy8_1FM2ec6DySzvUM6HwF0xvmydG7EIqy0Hq5kU7JvF5geosK-XPVM9WI-x_uE0HrMnBtKtK789n5zuvvmxJ137biL94VVSFY2bunNWgohibg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ: از اینکه ایران پهپاد شلیک کرده اصلا راضی نیستم!
خبرنگار: شما گفتید که ایران آتش‌بس را نقض کرده. آیا این کار عواقبی برای آن‌ها خواهد داشت؟
ترامپ: خب، به‌زودی متوجه خواهید شد.
خبرنگار: آیا آتش‌بس همچنان برقرار خواهد ماند؟
ترامپ: از اینکه دیروز شلیک کردند، اصلاً راضی نیستم. در واقع ۴ شلیک انجام شد که ما ۳ تای آن‌ را ساقط کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/66892" target="_blank">📅 23:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66891">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: صدای چند انفجار در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66891" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66890">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
🚨
🚨
🚨
گزارش ها از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66890" target="_blank">📅 23:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66888">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d178038cac.mp4?token=YQYYEZgdlOwfeKj1F0uk9wkADWx7bomlebZlVy-9jE4cnV1xRxrFAYEX2vTFLVnM-q2xGhBQMz0R-gtwSARrNcySVfX747J5QkM7EeOqbcBCPjkwxZs_CDOfOYymJ7GlLggnXmZoiGTCP_SlPxsvaKhhIK9VLQdWNvQu11rhdRWDV8VHVibCSjDb_MnDxtBHeoZyd-f4QEmeGvecAv8FKqzQOenqmqCzK3rnVn6qT63LiIhK-IR09tJy2SxZqytxPBz8aJxqOwIBcUEkwubf5vyotU0Ck5hm_B2QDBjgDAmKEZmpoIKI2YuYSJV6vw5cjM1ITCoVQhxCFACap1MQjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d178038cac.mp4?token=YQYYEZgdlOwfeKj1F0uk9wkADWx7bomlebZlVy-9jE4cnV1xRxrFAYEX2vTFLVnM-q2xGhBQMz0R-gtwSARrNcySVfX747J5QkM7EeOqbcBCPjkwxZs_CDOfOYymJ7GlLggnXmZoiGTCP_SlPxsvaKhhIK9VLQdWNvQu11rhdRWDV8VHVibCSjDb_MnDxtBHeoZyd-f4QEmeGvecAv8FKqzQOenqmqCzK3rnVn6qT63LiIhK-IR09tJy2SxZqytxPBz8aJxqOwIBcUEkwubf5vyotU0Ck5hm_B2QDBjgDAmKEZmpoIKI2YuYSJV6vw5cjM1ITCoVQhxCFACap1MQjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر مسکن و توسعه شهری ایالات متحده، اسکات ترنر:
خداوند تنها دو جنس آفرید، مرد و زن.
و زمان آن رسیده است که این حقیقت را یک‌بار برای همیشه در کشورمان تثبیت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66888" target="_blank">📅 23:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66887">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCTb3dCi4TbqU6Ij7qxo7I7hdVt8ZK-vTt8ww0QQWZ4Z2dcQuQpiQWup1VzB712rBU_OtPDuBGdzCpYZ9pYjSaFFvENCY09S6mBzq4aLUw-HWAppWB50GZ5_Mgw8e0SSGbQa7yR7yGXv68fs6u4ZIj27HhUlhHmYEA0nCpgqv9lj7cBsxOXCPEksnyaFP8hErsGJdmEQMBh_9KOD0PKbbWe7vkwJmAOy5kUVMevz1vHmWjAcnjt-WsJaY2gymqeMyakSi1j-ljoStBWaka08op5OqpXflNj33rb8LojCP-WqlRjk1i7GXEjTg4sXtBmzhU_VsYlHhKYT7dqBhLU15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66887" target="_blank">📅 23:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66886">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=Phe5uWKlnaH62hhmKU6_S7a7vyC0uwzuWCs0SwWxsu1niZUU5RvcGuW1KGNJ7RDRwm0P4FbPYsSlDiqNGRMTlY_ZDyakvBO3f6WXQa-vrSjtlfTECmFyq9kRLuIB_Qm1unqLkE2PRvO6vhhUbZRP0aaioEXWU0o05p3WHrpRqNXKFlY4Le9ho2GF08BXy4AuUvcdjPH6qWqOX8XKBPfhEBp7lXXaox0f7KLypqvqWG0zXbNg5YmW9J5swTP30BwKs3oR9RBg1tIPZrpaz5PdFNl72zOeDx-qi9jmlRrjA7J9UpElgmslTqlTDjhZQOh2opgfI6PoPJ_YTABmdue77w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=Phe5uWKlnaH62hhmKU6_S7a7vyC0uwzuWCs0SwWxsu1niZUU5RvcGuW1KGNJ7RDRwm0P4FbPYsSlDiqNGRMTlY_ZDyakvBO3f6WXQa-vrSjtlfTECmFyq9kRLuIB_Qm1unqLkE2PRvO6vhhUbZRP0aaioEXWU0o05p3WHrpRqNXKFlY4Le9ho2GF08BXy4AuUvcdjPH6qWqOX8XKBPfhEBp7lXXaox0f7KLypqvqWG0zXbNg5YmW9J5swTP30BwKs3oR9RBg1tIPZrpaz5PdFNl72zOeDx-qi9jmlRrjA7J9UpElgmslTqlTDjhZQOh2opgfI6PoPJ_YTABmdue77w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
کشته شدن سلیمانی یکی از بزرگترین اتفاقاتی بود که تاکنون در خاورمیانه رخ داده است.فکر می‌کنم خامنه ای و دیگران در ایران از کشتن سلیمانی توسط من خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66886" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66885">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66885" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66884">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjVIHaQ9gxy0V20rPrBTxUiCQb8cpx-Ik0arGZoW2uZm9CEABfSVSkyv1yZ41c3DUKy7GtTB0CsKzB4qfBujU117_AmVExjvDvl7ZYO6Oeb3phfIFNhwqFS8if_8y7DkhZDMJxb5SMtPe-eHc2vhOXoe3bLPwoiJN8z3Xu4gnOW2Vlmn52snypxaSbEoy2DpZldgDUXyqyWzEE0X78SiMcLseZqJxfpHlDsXLSd1z1BbM35R12oMHGdaoxIjCYqfElNE1sU29eDTwBB9FaQ43EFnP8sWyJ02kpDZA8XRrUgbthNrJQReh_wTGuWpCJTMxUQj3QZdrfBjrVatyjTsYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
رئیس کمیسیون امنیت ملی:
به سران شورای همکاری خلیج فارس هشدار می‌دهیم، قمار بر سناریوی آمریکا، ثبات و امنیت شما را بر باد خواهد داد.
دیدید که پایگاه‌های نظامی آمریکا در کشورهای‌تان چگونه به جای تامین امنیت، به منبع تهدید بدل شد.
قدرت موشکی، پهپادی و همچنین مدیریت تنگه هرمز، خط قرمز جدی ایران است.
تنها راه تامین امنیت منطقه، فاصله گرفتن از امریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66884" target="_blank">📅 22:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66883">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=MswFlMpbpOWwBPvWWVFWI11ir7w5J2ajbDXplLs1Hkl-4J2GH05P8-xNEoxDM5Sriu9EyPyWSYTLxn-e8Pz5ifj4tH4Vrg3xTP7FM2iZJRbr2mKIaNgk3Uv4XRwctggyllccwqQQTjdauP0xsH00fO8jD7Id1AH0Z56e8ImjHEXq_yIvT1BUe1BWsQCrwgnSobMocPk4AB50-D7rB0IwD6Ru2mPzOL4Cx39mRaxKiz6ecV8lgtdRracuZXrauz7GtzVSujNivKiL9oH--9uSn8Im2fG6os22mSocKU03NO02SEhy48NxzeZ4VpBoiXDBgwJ6-aEEskECZwI4z3FRnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=MswFlMpbpOWwBPvWWVFWI11ir7w5J2ajbDXplLs1Hkl-4J2GH05P8-xNEoxDM5Sriu9EyPyWSYTLxn-e8Pz5ifj4tH4Vrg3xTP7FM2iZJRbr2mKIaNgk3Uv4XRwctggyllccwqQQTjdauP0xsH00fO8jD7Id1AH0Z56e8ImjHEXq_yIvT1BUe1BWsQCrwgnSobMocPk4AB50-D7rB0IwD6Ru2mPzOL4Cx39mRaxKiz6ecV8lgtdRracuZXrauz7GtzVSujNivKiL9oH--9uSn8Im2fG6os22mSocKU03NO02SEhy48NxzeZ4VpBoiXDBgwJ6-aEEskECZwI4z3FRnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏نخست وزیر نتانیاهو: اسرائیل تا زمانی که حزب‌الله خلع سلاح نشود از لبنان عقب نشینی نخواهد کرد.
🔴
«شهروندان اسرائیل، پیش از آغاز شَبّات می‌خواهم خبر یک دستاورد بزرگ برای کشور اسرائیل را به شما بدهم. همان‌طور که می‌دانید، ما در واشنگتن مذاکراتی میان نمایندگان اسرائیل، لبنان و ایالات متحده در جریان داشتیم. این مذاکرات طولانی بود و امروز به نتیجه رسید.
🔴
مهم‌ترین نکته این است که اسرائیل در درجه اول در منطقهٔ امنیتی جنوب لبنان باقی می‌ماند. این یک دستاورد بزرگ است و تا زمانی که حزب‌الله خلع سلاح نشده باشد و تا وقتی که خطری متوجه کشور اسرائیل باشد، این وضعیت را حفظ خواهیم کرد.
🔴
این همچنین ضربه‌ای بزرگ به ایران است. ایران تلاش می‌کند با زور ما را وادار به عقب‌نشینی از جنوب لبنان کند. اما در واقع اسرائیل، لبنان و ایالات متحده به آن‌ها می‌گویند: این موضوع به شما ربطی ندارد. شما هیچ نقشی در لبنان ندارید؛ نه شما، نه حزب‌الله و نه هیچ سازمان تروریستی دیگری.
🔴
نکتهٔ دیگر این است که ما به ارتش لبنان اجازه می‌دهیم تا سازماندهی خود را برای در اختیار گرفتن برخی مناطق آغاز کند. ما دو منطقهٔ آزمایشی (پایلوت) ایجاد می‌کنیم که هر دو به توصیهٔ ارتش اسرائیل هستند. یکی از آن‌ها اصلاً خارج از منطقهٔ امنیتی و در جنوب رود لیتانی قرار دارد و دیگری در شمال رود لیتانی است؛ بخش کوچکی از آن در منطقهٔ امنیتی گسترش‌یافته‌ای قرار دارد که طی دو هفتهٔ گذشته به دست آورده‌ایم و ارتش اسرائیل به آن نیازی ندارد؛ ارتش این موضوع را کاملاً صریح اعلام کرده است.
🔴
ما همچنان منطقهٔ امنیتی اصلی را که خارج از برد موشک‌های ضدتانک قرار دارد حفظ می‌کنیم. اجازه نمی‌دهیم نه حزب‌الله و نه غیرنظامیان وارد آن شوند. این وضعیت حفظ خواهد شد. و مهم‌تر از همه، اسرائیل می‌گوید: امنیت ما بالاتر از هر چیز دیگری است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66883" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66882">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4N1uMPJIcbVwa-SRWsAhaDIxtJTdd6bwYBKjM7hJm6YaJqeSCEoeuu1mAStj5jRQJOKUOMQ2BLCDI3gIp5VH8dYtwU-ROQ8au4CrDZn98r7NWqegSx087PeqyrlplqwBnWIOyFlUW5kKlH2R3MMg9t9E-mr9fWPwp7SZX3qrDV7XnnI80_Qj2nVbHq6QLncwLrL2lcHE6jTleW0dB90C0vcHqcU0v9mCDyq2_gtzReWePI4akg0WTcuf4yapQC4sVpOnxprKTPmK2ZoIedivLEFH9FgIk8aVV8pJPcMUgwa7Qju6ryd6zlZ3tcBmYrb7nHOlTYqZ7dAM_j4dQOSuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و لبنان به تازگی در واشنگتن دی سی توافقنامه‌ای را امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66882" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66881">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‼️
🇱🇧
حزب‌الله تصرف تپه «علی‌الطاهر» توسط نیروهای ارتش اسرائیل در جنوب لبنان را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66881" target="_blank">📅 21:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66880">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJEoYo_OL2L31N9AsHQ5F9Mk0jlSGGrChcB8c-Wa5Uu9CNsy74ie0BrQcYt3-B5_9UlTY-zGLcFatr7ZNihs9q-rnttpx2C-QtpEtXFH0dTYF4JvS1hW31tMOnX0772eF0ardwWYEDI4vTTegnaPbmirmyiinczyQ131TndM6SkkWsnchdTZPCy8j7cNuoig36p6A4VH23HyeOv0caV289FyRTulvfLOdnOXVlxd_y8fA-bdieKHwcHkvzBmG4ukGcFi9ICeJ-jVonMhBK3uDHSYE4spmZ_MPyk2wz1566ljsSnLengoxtNSgXwl0p4p9x9YdCwZ9zM-SKs740FwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید اکسیوس:
مقامات اسرائیلی و لبنانی به من می‌گویند که انتظار دارند پس از چهار روز مذاکره در واشنگتن، امروز توافقی کلی بین دو دولت اعلام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66880" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66878">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iw7ZzfA7VH838PEGD4sU4GAhksYriRyV7SvuZNTl-uPVqIW5IfFF6CfHYyntqvKhTv6unzozObojT3fjjEy84urnUo_2lN1VqUBZ35ywyF-mDpvLvIp8zIfb2ifM50MFIChKZSTrOvKtmfQDWw1P_VDzX5BgdrJzn-m8qzeKaJk_RFnx5AOYi0fOeCcaA1QvIN8tkn3Bf5AFqZI3KsFJ8lLm3m97C8lCLCINICronCv77uzD5GD9mVK6bewwlnt9RVzzgWkEF5RluApDhcwv5vBzmI4z5OBxsrXDwcuz0je1oIOT_phbNJ0vc1kdkIOjRltxdxId2ZDP6PshTIgPHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PK9ln93-Y3_SZzdEWz9RkNELmRf3LCIRVdDfgkvUXRUfFhZWZ7O5z-ah8mAPKrvsKEWkGNZ3s4Itcgc1jQ_HY5YkOc4bK6RZ0VdsbyCQ2r5b909d5bXfDcRtZl1M2d9fLY75xLTsgf6qRl9dnyTSyWorMmv4U7lEBOKlpQitcQXdec5ylQf3uwMEswEYck38rPa6vmJDFlDbmMa0Z4hROlV2SbKpdxkmgVseypCXI4NzTNf7dwMW0fqVRMuLzc0HzaFN0vLo0TQrqby0zlHGOfeDFKLLOGOt359Dei6xP5AKKm6jaJQpBXg6fFJVa2q_YiKt7mUDK8b4-wZrAI0N8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در فاصله چند ساعت مانده تا آغاز بازی حساس جمهوری اسلامی و مصر رژه‌‌ی همجنسگرایان در شهر سیاتل آمریکا آغاز شد!!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66878" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66877">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZV8mrQVZX7IxlYzOjpre1D6H30uEA0bPvGcNuZbU5w1F80PaLDfioi2J_eO5Q5qihQsd5NYedKOp5kJvhl-kRgdfeGEmDIa_hKEgg_f-u-mviHjDaff5Phy_Xr4KROoXd4N4__Z40_U3-PfmI0TsbxefaIlHoxqwwdkNS6ikKN7MId_KeOvS037Hh05Jw1gAtBZU4z9VDt0eWKWVXo4u6Zslac_G_DfhGcenTEjIUs0hfTgcpdvBTrLUFyXlqvf4-N2PuGbhaFBN4ha7lwUkRH_iOGHmnv3R3whCg0-laHY67vZokme7d23upU_xFGDzAsJC2FlOFxgcYLomZQROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد.
خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد. ما سه پهپاد دیگر را سرنگون کردیم.
بدیهی است که این نقض احمقانه توافق آتش‌بس ما است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66877" target="_blank">📅 19:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66876">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEVnJ19K3TxShe1BIppvcrReuxnwwSlUSaDIdKz3a-0EVCK7625aHj8JxMIfvvKpBdqY2RmjJJ523pZzJlnAi5uJy0iRSCS6WFMK_LtNOH3pnOyvQhLBrbAwj0uVdA4e_dakT5c19pP-3IUpZDUtES_aaevMfWx3GMf0BdqUuC9ZNMiwaqf9LK11GDJMvYiVZe99J71yKTVXYvLJYDwldpfDK0wM8kpwJXHCfKZEnaLQTbfIL6pMxgxYefRNLybTqMNrxH7-zDGd5nR4msc44YAauYnY3IpBnHbs8eVKno4-5jftXQ2Bgg1oNP576xWWC97_un-5_UDSpKarYzvWfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ:عمان هشدار داد تنگه هرمز به شرایط پیش از جنگ باز نخواهد گشت، کشتی‌ها ممکن است مجبور به پرداخت عوارض عبور شوند
عمان به متحدان اروپایی خود هشدار داده است که تنگه هرمز به وضعیت پیشین خود قبل از جنگ باز نخواهد گشت، که این امر نشان‌دهنده احتمال اعمال عوارض عبور جدید برای کشتی‌ها است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66876" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66875">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8HvwaHbYPtd1tjV95RYT3Jfxvp32HGsnzj5If8Y7Mqjy_Ds2O3DA4iamTZFrjax5eOcmXS7EX5SoC47FCp7d1RCCmogBo3pllw7gRwp_b_1cKxMyEQrz27woMx2hXtP8ZYsFYrsqpXNm-96znxZOX9HWUjHdRee4tTWkWuZOJrINLPuiC1eFAGPPaqZJfBB4yaQA0NZbbkOPSalHF0IbEWrabMZBm1_gM3m7oURFykK2zwVQv4jPCxbSGejhtyjvxVBcnbkUSH4ANp-g8yFDcU2_YG5MsAfkWrhV7EbHOrl0E-7ydEvbAPSP1lHrH6_X4oTeeSPcY66_-w84hVgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
رونالدو تو جام جهانی گریه می‌کنه؟
پلی مارکت می‌گه ۶۵٪ بله. احتمالاً آخرین تورنمنت ملیشه و دوربین‌ها منتظرن. البته رونالدو رو که می‌شناسی، شاید حتی با قهرمانی هم گریه کنه!
قبل از اولین اشک رونالدو، پیش‌بینی‌ات رو توی 30 ثانیه روی پلی مارکت از تلگرام ثبتش کن
👇
https://t.me/PolyBaaz_Bot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66875" target="_blank">📅 19:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66874">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=meKPPKSGUElzREI1qjmugFWLZdIEH7_uJZRViiorY7fyGYmaRZWueaZSdyszpZVjXtj2MSE7jbf8iQp48Ju-XyghnHROHBQMG7e6y9Sf3uBF6L-e0TIGZLyXSKGiBDm2PrtR7uRfTUQz8-AnGYXTQtBQmIWUco36qGbo9SW292v9Ggep2DDm36fALM2ufLgSU5J5Z4jojeMgFFLMpkyXXMlgtDYikb_ZIpH3gi5ALJdWWMtmn_ixoCuZVAZvn42I6vgPwdC2W0aSRk8NaUn82mEIVoWakFW5buII7frtFqLXNLz5WH1ZpgNLeU46S414bsfYLqSlusUZRgQupJZGJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=meKPPKSGUElzREI1qjmugFWLZdIEH7_uJZRViiorY7fyGYmaRZWueaZSdyszpZVjXtj2MSE7jbf8iQp48Ju-XyghnHROHBQMG7e6y9Sf3uBF6L-e0TIGZLyXSKGiBDm2PrtR7uRfTUQz8-AnGYXTQtBQmIWUco36qGbo9SW292v9Ggep2DDm36fALM2ufLgSU5J5Z4jojeMgFFLMpkyXXMlgtDYikb_ZIpH3gi5ALJdWWMtmn_ixoCuZVAZvn42I6vgPwdC2W0aSRk8NaUn82mEIVoWakFW5buII7frtFqLXNLz5WH1ZpgNLeU46S414bsfYLqSlusUZRgQupJZGJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قاسمیان:
به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66874" target="_blank">📅 18:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66873">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLwGjs6fOcYIJImrHer61RMGdsblJTB0LWItygWDyQsMok1FJFhMcvx4fr7OOrXbnIxbhDe1YbGCxt4ULWF9wb559jy9iYsnNix7CghMHtodIcfWYHJMeviPBDhAPv3BfEfAmmFBdxxxrFnN4EqCvTkRONLESI9LynveR_S0vTHjXBBUWT_qmfQaJ6ui8BAJZ3ovX-WThUy4YMwKXw92JemTEh9Y4AZ-4e7MZlP9RLD-_7HK9rTCyPGhNC8ozSFYHJVNEYPXG3zgVsK5tuBtMU3s96rBAPaXC5IO0zDm7RG0TNMQPwUGlAgzdrHVSIDnFKDxFjGguH3AgiyH8uocKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
توییت کاتز وزیر جنگ اسرائیل که قالیباف و عراقچی و پزشکیان رو تگ کرده:
فرمانده نیروی قدس، قاآنی، این روزها مدام اسرائیل را تهدید می‌کند.
به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحکِ تهدید به او می‌آید.
در هر صورت اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.
نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان، هیچ‌‌چیز ما را متوقف نخواهند کرد.
نیروهای ما آماده‌اند تا کار را به پایان برسانند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66873" target="_blank">📅 18:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66872">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=roymmNGZDTAMhEPH4NvXnAqIM8FBpH1hbUbgGrvNEId9G3VvDjfiL0nKbZH397nBmZIY-2cGz-6M6KQYQLSwY94BuVZtRDyAz_NssM8OsPqR_hQoWgJ-YQj2e5nOGZsL3_kwQMRpcJXXYZ70uLWqr6bNy0CzrnffIkqsQ_-oXfaWVPrUAnogL24SX3RCtgfJkPsAtrpRjEzEkPRTYbtkGuQOR_Q9f2Ta0GAyEV3ctUjZlvSULzBgRabLLrgct6_LCUZic6O5SZtgFu6u4eHB2ohOawPqqoGvOHWLzjDx181OATr3TurbKMgpJkYUnSiKDTabfqSwwIuM0gxrTqAPag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=roymmNGZDTAMhEPH4NvXnAqIM8FBpH1hbUbgGrvNEId9G3VvDjfiL0nKbZH397nBmZIY-2cGz-6M6KQYQLSwY94BuVZtRDyAz_NssM8OsPqR_hQoWgJ-YQj2e5nOGZsL3_kwQMRpcJXXYZ70uLWqr6bNy0CzrnffIkqsQ_-oXfaWVPrUAnogL24SX3RCtgfJkPsAtrpRjEzEkPRTYbtkGuQOR_Q9f2Ta0GAyEV3ctUjZlvSULzBgRabLLrgct6_LCUZic6O5SZtgFu6u4eHB2ohOawPqqoGvOHWLzjDx181OATr3TurbKMgpJkYUnSiKDTabfqSwwIuM0gxrTqAPag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای وایرال شده‌ی یه آخوند تو یکی از هیئتای مملکت :
حضرت آدم دید هر عضوی از بدنش به درد یه کاری میخوره که یهو یه نگاه به وسط پاش کرد دید یه تکه گوشت اون وسط اضافه اس٬ گفت این دیگه چیه؟ هرچی دست بهش مالید دید اضافس بدرد نمیخوره؛
حضرت آدم خنجر یمنی رو کشید که کیر خودشو قطع کنه که یه دفعه حضرت حوا ظاهر شد گفت آی آدم چرا میخوای بیچاره‌مون کنی که یه دفعه آدم دید کیرش راست شد؛ بعد با خودش گفت این مال کس دیگه ایه٬ این تو اختیار ما نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66872" target="_blank">📅 17:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66870">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRYHz6lMZYBQ4Z5d4cRZ9FolKxn-CO7g22ac5w9BCqwjCcm2vi095KIsz-IAuwqDtODhIMuOTRPr6g5oUaQ81vthSSl0FHOmz6UdloUmxw_dJ0lIZoe6H1zczgjDFWxrUBymo_9rQzRHCtdfGcqfHY_f9wwTP3mKWpny_OmgijD3Cf44bWFMq6Bg5xzerHNqCec5i7Vn-Iy7A2nbbaoFLwfRSHvD_CrsQL4OlfPy2cAH8CIRnQ8at5IEPXNJVzrPqZxv5_V14ecptbWn7wsMY0dHPH2s1XfSfM-6IAeKOV9zrlmxCXUU3YUt1vPY1NpCd-mZ7l5ghL7JpX-xEpZICw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLIUmI9GJMEYoGzsXmolRs1W3QB2Eybxmp8xhQEnm8jo8uvem-X_kPlExnu9R7veQWAPObCFy2c-sDDojPfs23V_4YEoxTxmuX_ydmYHn9n4dHdboxA0XFjV3MjVwihXk7C8--R-WA06okRntqLDGqhI_50bO5B25TIV57VaGwTWIn2RPs7apZwJIKvh2ZgVnv1x67Pv06APpBZdDXy64ftuSbkqa5xzzuM2--nPNGPwtad5rwcdOC0n6DBOw6TgmkqFHpq3iPySU5zsbEnKRCphsswJpIzmfh9KJJRY071mgtJRT6KE2wKpPGPW_cmzi3lhwInPoP7W-E0XG5b0CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
‏
بر اساس تصاویر ماهواره‌ای که روزنامه وال‌استریت ژورنال تحلیل کرده، حملات موشکی و پهپادی ایران خسارات گسترده‌ای به پایگاه نیروی دریایی آمریکا در بحرین، از جمله مقر ناوگان پنجم، تأسیسات ارتباطی، انبارها و ساختمان‌های پشتیبانی وارد کرده است .
با وجود اینکه پنتاگون اعلام کرده عملیات ادامه داشته و تلفات انسانی ناچیز بوده، این حملات آسیب‌پذیری قابل‌توجه پایگاه‌های آمریکا در خلیج فارس را آشکار کرده و موجب بازنگری گسترده در آرایش نظامی ایالات متحده در منطقه شده.
مقام‌های آمریکایی در حال بررسی انتقال یا بازطراحی تأسیسات کلیدی به نقاطی دورتر از برد موشک‌های ایران هستند. گزینه‌های مورد بررسی شامل پراکنده‌سازی نیروها، تقویت استحکامات پایگاه‌ها و گسترش استقرار در مکان‌هایی مانند اسرائیل است.
برآورد می‌شود هزینه بازسازی خسارات واردشده به پایگاه بحرین حدود ۴۰۰ میلیون دلار باشد و مجموع خسارات واردشده به پایگاه‌های آمریکا در منطقه از ۲ میلیارد دلار فراتر رود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66870" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66869">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=QjLj6ZeVV-gbOCOSyZUXDhMQiSAP1sORPAGOBMR-0KoQsfa_M3Qc1vN8ykjYjdqvC8g38TqeF7JKIpB___jHX346_Kch4aq5KRRs99oPt_hp1biITaDr1rA_Gm-PbFU48sfjQGttNzC8305xln6tJWXzehhC6_Z4LecHKdK2Zxd5fIQFVa97_WSbTKdi8GbjZYbkBjY1GOExYRpFdpfempw2Xa1fdWAVTQiLZKTqFO_pzAIRKyt4rgdtyVB87XaLvNKI65G3lsKzGnKas6GfpCKGbfj1BC6gn1lRCzK3c8iGWtPCeZ98x3T007MnOI-KDdc1aDKiDwrUQ3KBI5uIfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=QjLj6ZeVV-gbOCOSyZUXDhMQiSAP1sORPAGOBMR-0KoQsfa_M3Qc1vN8ykjYjdqvC8g38TqeF7JKIpB___jHX346_Kch4aq5KRRs99oPt_hp1biITaDr1rA_Gm-PbFU48sfjQGttNzC8305xln6tJWXzehhC6_Z4LecHKdK2Zxd5fIQFVa97_WSbTKdi8GbjZYbkBjY1GOExYRpFdpfempw2Xa1fdWAVTQiLZKTqFO_pzAIRKyt4rgdtyVB87XaLvNKI65G3lsKzGnKas6GfpCKGbfj1BC6gn1lRCzK3c8iGWtPCeZ98x3T007MnOI-KDdc1aDKiDwrUQ3KBI5uIfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟥
فاکس نیوز:
دبیر کل ناتو  فاش کرده در جنگ اخیر فقط ۵۰۰ جنگنده آمریکایی از مبدا ایتالیا به سمت ایران پرواز کرده اند؛
«اگر ایتالیا را به‌عنوان مثال در نظر بگیرید، ۵۰۰ جنگنده آمریکایی از پایگاه‌های آمریکا در ایتالیا برای پشتیبانی از عملیات “Epic Fury” به پرواز درآمدند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66869" target="_blank">📅 16:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66868">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=cUTrlCtvURugCYCB73b8ISVQ868lnEWgtQ6kXu15hmBtHFEcAxCevLK62jS8TiuhziUhnIS99HQqDRpxdRiiBRvpQVahBi61aJvRKgDfCo3Tai2xnbtnaIyR1FFJ7QNtjVeRvvyYCdv-6IvvTTXozCC5SsuW1ce8b72LK7NH9Jv-MvvDvs--NCoKCw5WRA4VsZWaCOi-lyToHZETkPOegF0hq7QydyQ7yZ2bRTOGcahCy2vdDx7R16ZqN3p7bcldi3JJOm7wws03cDt-1EKaik_NMK0pg9K4ceM-jd9UiZCFKsquLLv1H8_jd4-IUrMuvSMZ2QfFWfkH_7Co1UMv8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=cUTrlCtvURugCYCB73b8ISVQ868lnEWgtQ6kXu15hmBtHFEcAxCevLK62jS8TiuhziUhnIS99HQqDRpxdRiiBRvpQVahBi61aJvRKgDfCo3Tai2xnbtnaIyR1FFJ7QNtjVeRvvyYCdv-6IvvTTXozCC5SsuW1ce8b72LK7NH9Jv-MvvDvs--NCoKCw5WRA4VsZWaCOi-lyToHZETkPOegF0hq7QydyQ7yZ2bRTOGcahCy2vdDx7R16ZqN3p7bcldi3JJOm7wws03cDt-1EKaik_NMK0pg9K4ceM-jd9UiZCFKsquLLv1H8_jd4-IUrMuvSMZ2QfFWfkH_7Co1UMv8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاسخ سخنگوی وزارت خارجه به دست ندادن تیم مذاکره کننده با ونس با شعر مولانا:
چون بسی ابلیس آدم روی هست
پس به هر دستی نشاید داد دست
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66868" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66867">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66867" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66866">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=mqATysasm6HeU0klLoWDKiCyDZrc2ZDKXFqkpM-beJQ-CJA8b7iPZstD8Y2lUACCn-xVM5TGcwOAwfqTALA0hpRH6D8mcooAAaX2ilRkYQgwDp4YrZkqoXCogg3b1AubB5IAiPbjd4uojDyiyvo0yPUZ1g7P0GJdLCipaE0QexH8-V3H_vJNiwXBUxwFCp4qtiWlj_v4ATmKaFcY47iCZ1iA0vRBytXO3A7VvqmGnVL1v5ux0-LeVI6RKtmvNUqaBobjzC1kQ-XDROWuGT8PPJYUqt8Zu4_fiBf-2MtqrgOrrH8GFTx3TkNQdO_0lh5uGjBgNvBcDALvfKv45rubdRYlmh7KTb2JExap6Ary2h6OgDi9cOLhfFbX6akGhqUX-nGjkR2wsrSyTI5NNnvXSoB6OiJvPBJQVdfK8fhin1GCknuRQcmtXBnkd9xtehz0iVnfVvFrTjRlatyIPfDAzrk4sknmVHtcg1i1esYNv_um5bvmWli5SKrnEPvkj1Xyc58xDAC0lFhxuqtf5x_2oiDIYRMaNBet_TgQ-6m4WHvRKPNZLyDcwquVN0jWLl4Sf_rGwJHmudoETsg6sC5pFX-VwPLk8i9MkAYbU-VRImgb4q55xwuQJN1l1Gull0VKm-wp2wnZDwjre_qLGYgbZppJ9D7lmOVGz60KM4JbDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=mqATysasm6HeU0klLoWDKiCyDZrc2ZDKXFqkpM-beJQ-CJA8b7iPZstD8Y2lUACCn-xVM5TGcwOAwfqTALA0hpRH6D8mcooAAaX2ilRkYQgwDp4YrZkqoXCogg3b1AubB5IAiPbjd4uojDyiyvo0yPUZ1g7P0GJdLCipaE0QexH8-V3H_vJNiwXBUxwFCp4qtiWlj_v4ATmKaFcY47iCZ1iA0vRBytXO3A7VvqmGnVL1v5ux0-LeVI6RKtmvNUqaBobjzC1kQ-XDROWuGT8PPJYUqt8Zu4_fiBf-2MtqrgOrrH8GFTx3TkNQdO_0lh5uGjBgNvBcDALvfKv45rubdRYlmh7KTb2JExap6Ary2h6OgDi9cOLhfFbX6akGhqUX-nGjkR2wsrSyTI5NNnvXSoB6OiJvPBJQVdfK8fhin1GCknuRQcmtXBnkd9xtehz0iVnfVvFrTjRlatyIPfDAzrk4sknmVHtcg1i1esYNv_um5bvmWli5SKrnEPvkj1Xyc58xDAC0lFhxuqtf5x_2oiDIYRMaNBet_TgQ-6m4WHvRKPNZLyDcwquVN0jWLl4Sf_rGwJHmudoETsg6sC5pFX-VwPLk8i9MkAYbU-VRImgb4q55xwuQJN1l1Gull0VKm-wp2wnZDwjre_qLGYgbZppJ9D7lmOVGz60KM4JbDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66866" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66864">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHL5uSrqaHoYegRPDpv0BWBHZv-Kmy8EwrpPfWdJxAMACrnoX73aBIilOyWBYljRiY5K53UJqw6wQ7S3YS8BLSKrsS_mj1F1qWAZcEDWhVcmSHjQtYrIBc8xExJoDJyiPF_Y5OwguXZBEmbCyBHywvHT0msttCA18qrcLQEethywX-lcfzwR8n19iHLrDqeSGW4ugswlZMsEPs65gTv9O_1inOaAM0HLP3ZljhIJ8Efrwdl75I6t5Q0a0gjWg2YiNe_7osdMG7HNN337jsfGxQzcWdaX8igUDB9fuX7h1_CZBPt-puY24FG26t2pAIRqbXAlM0WhaGTqUWiKxnu4MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=HVhPKtl3gFaSctCWx9RTVNcA7ITwQMfE63nGZhKEiUE_rLscLLm2LB1mD7GCE5qW7FXDaZwxIUt4CXQFwCvps7DEpTVJu8EVJXdjq8nowP0iWT2EieErwg_i1eS86OphauSKoP78aSGRWnS6tBOY40DjrahopdGWElwH49sk1kTeU8GFMmbIQgDUlZz2Vm_0cGOpu5QVZXUM_kALdmkebderEHekI2fKJaMsA7miKuYGbnC0Pp_ZuLhWRA5WRgfMiv9QkpymxxLl7ASVXfmEAIWwiQC9TcFxNI3b42eSDtd6HpJ2zFVAxLUrol6pOXHyrF0LM2Zy0X57c8rENBb4vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=HVhPKtl3gFaSctCWx9RTVNcA7ITwQMfE63nGZhKEiUE_rLscLLm2LB1mD7GCE5qW7FXDaZwxIUt4CXQFwCvps7DEpTVJu8EVJXdjq8nowP0iWT2EieErwg_i1eS86OphauSKoP78aSGRWnS6tBOY40DjrahopdGWElwH49sk1kTeU8GFMmbIQgDUlZz2Vm_0cGOpu5QVZXUM_kALdmkebderEHekI2fKJaMsA7miKuYGbnC0Pp_ZuLhWRA5WRgfMiv9QkpymxxLl7ASVXfmEAIWwiQC9TcFxNI3b42eSDtd6HpJ2zFVAxLUrol6pOXHyrF0LM2Zy0X57c8rENBb4vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های لبنانی گزارش می‌دهند که یک پهپاد ارتش اسرائیل، اعلامیه‌هایی را بر فراز شهر منصوری در جنوب لبنان، نزدیک صور، رها کرده است.
روی این اعلامیه‌ها نوشته شده است: «منطقه خطر! دور بمانید! هرگونه نزدیک شدن به نیروهای ارتش اسرائیل شما را در معرض خطر قرار می‌دهد.»
هنوز تأیید فوری از سوی ارتش اسرائیل وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66864" target="_blank">📅 15:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66863">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=W00d_FdZknKfQ0CeqKKQ0zxbEWQIPFHGbfFNBCpT-2X_NepwPaSgdhQ4lusYpua9trSEwZDl4N-W6KkbqHMITevDAwxMmp9ml9BqJjufuiiMZ0tZnmFsF4_kJ98kZX3FD_qNLVbN630bhuVxDct_vKBZxRpXX8YQIywbNTprYLLZpA1vqBh-s5Mbe7naoVQWdb5mXHfSwtgoNixwp1g9c_z8nMkQIq7G4HJvr4-TfjN0gCdVKhtkRT5khCHUgy_oNnOTcGD4-7QdJkQkO8ZTv8fpyoyvc4pJUqirmjIehQ3dpslraxoeVI3NnNnJTgm1gv9lfAOmbKe3EP82Th-Kgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=W00d_FdZknKfQ0CeqKKQ0zxbEWQIPFHGbfFNBCpT-2X_NepwPaSgdhQ4lusYpua9trSEwZDl4N-W6KkbqHMITevDAwxMmp9ml9BqJjufuiiMZ0tZnmFsF4_kJ98kZX3FD_qNLVbN630bhuVxDct_vKBZxRpXX8YQIywbNTprYLLZpA1vqBh-s5Mbe7naoVQWdb5mXHfSwtgoNixwp1g9c_z8nMkQIq7G4HJvr4-TfjN0gCdVKhtkRT5khCHUgy_oNnOTcGD4-7QdJkQkO8ZTv8fpyoyvc4pJUqirmjIehQ3dpslraxoeVI3NnNnJTgm1gv9lfAOmbKe3EP82Th-Kgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
اکثر مردم نمی‌دانند که حرف B در کلمه dumb وجود دارد
😢
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66863" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66862">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⚠️
خبرگزاری فوق معتبر فارس:
درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66862" target="_blank">📅 14:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66861">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=mur3gWRQGEt-hiwOdK8jilGJA5fJme87ralpqSMmCSBdyHOcz94_mBqJjrCFlnvDibf0MBJ5yBHWPihokPwbUUPXEyV2vQLFBpRDB9GCsICuzXOXSwoDOW3O-17Z_G006L6jFhI8d_fdwAO6l3_yKw3a1M5sEx9Not-VIymhr4iv-26YlYSnwaOChyUyj6eqFOQh9gX1YnXh683IkxNaHGvMG8IGK5SUvbj2v0ipcHK10pAS7xvOdkFzSLOaLzKslKZlVTBTuK-TWRf36pTYv3JGH5em4za_kbVnPEmlWAIpzCE7lzPVcIwfb6ZzK_UMgGzUoaE7jhWXApVXuPDSBA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=mur3gWRQGEt-hiwOdK8jilGJA5fJme87ralpqSMmCSBdyHOcz94_mBqJjrCFlnvDibf0MBJ5yBHWPihokPwbUUPXEyV2vQLFBpRDB9GCsICuzXOXSwoDOW3O-17Z_G006L6jFhI8d_fdwAO6l3_yKw3a1M5sEx9Not-VIymhr4iv-26YlYSnwaOChyUyj6eqFOQh9gX1YnXh683IkxNaHGvMG8IGK5SUvbj2v0ipcHK10pAS7xvOdkFzSLOaLzKslKZlVTBTuK-TWRf36pTYv3JGH5em4za_kbVnPEmlWAIpzCE7lzPVcIwfb6ZzK_UMgGzUoaE7jhWXApVXuPDSBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسمای محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66861" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66860">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
قرارگاه مرکزی خاتم الانبیا:
🔴
پرواز هواپیماهای نظامی اسرائیل در نزدیکی حریم هوایی ایران یک تهدید مستقیم محسوب می‌شود و اگر ایالات متحده اسرائیل را مهار نکند، ایران این تهدیدها را تحمل نخواهد کرد و حق پاسخ را برای خود محفوظ می‌داند
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66860" target="_blank">📅 13:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66857">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUWkt1YUFXQMFhXKD58Mc6WbDfpdElDCiaKGMVOAeJWNuPDGWrq8Oc4jSF2Y37uvm1bNG0RBLQmKs0cI3zL-Qk0c4Axm38O5Fp_91xt5ngWfMloM17JnitIqyYVbPhDwQczjyB7ATVplJeWpJcig5qbCusknF8XNTURMG64pZ58ykaKByOk6319e3WDN3QQv9r7gsTk4ylu3eHsdmksdjQRE6swhAE3MIsVEb56DxjqCkujlygQyv_RwKFHU8Z7HhmX4mzfCNZH3SHC6Ui1bhMmJT_UXi16797diOymP0fxzSAhMLl0ZFFsjw4IJTZZyTtEt4n_eP1V0S6NxirJ2-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qReprF7SEXFoyn3pJDLeZh6HigwwrfYqfJ5AkaiU1Qk8S7bmHIWLrVcJMUCkN75ImLNqdk1Cy_KuhiILlDgqKiq0u9vU7zUnDDkHgXxyQ-R9O9Ac5V2sHICkQEsRXMk3xOeAIyvw2FktiR3n8WMFwL4Vw3aY3-UVCFZEtwZ9oxlmdG6UDeUNCuAPhGgQHm3T4R9tzDmWR_RBj7giseLJ1prpdwF4jq4sVbLNaNI8kFSOkaIr-s45Gkz18FAya4YCEv6UP80YqDwXLW41LfaJvtOKFT6NT9OTjijHH7mvfh3Vib35iDOIfeVR5caFZ-nDSeKTFtSzIBFMWHqWxxskXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UR3Bq5lkj5OCooI8ytVN82P8HGZwr4P5qEQDQf0RuP5CygQ6GMdGuFuFvi0WxP6qxUFfnIb-jGR9Tf-53JmobBlw7Ltv-VtoWbgzoynGV2gjxkMpiPSazy_1VFBP0IluApToS2knkD6dhDCYXL617lAblTQ-zd7lP44DhHzh3mcmq0UDLDCxZrIr8tCLmuPLnqXAMTihtYlxI4vL3YNOo3OW_N6S2dHAoh-6Hg6WuquXnpGRS4JneAAYZ8Upbkpy7N_ERIo08kAUVzJiBMSPKw_3LhImVllGNLEzZcq_mvNNDUej-FGQ4NZarlKOASR32pRKB81YW7aijATzyaVlZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حملات هوایی صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66857" target="_blank">📅 12:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66856">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=eJ0yZqCh9Evjgd3J5PpHsInT-4ppyeWLZrlXh5TJwMjo7StfqwE4GJEDnKJ3BZfxIcW6jKlB4_3-rEJFinPVqhtH8LNSM9UIGjz5deBAWASkIQ-czXJsgO4cupOFqU_e-n_gBQUjCq7YyIh3BPGN2QQCbU7ZqJv3F9gzX7hgaK-Y3MvEhJG-vGTopeZb0DH2bHq4LCTv6CsGJLRWo_8NvHlCPRJXJayjRqIlaGDR-R4VzQrUzUT1WnFCLCsS6eagIvswLi9fJdraqapfqnbyWfD13bUclz5Hb2XsnbR_pyYgmQFNYmdqvv7qx-lKuy7u6RBsuMszN0c9rJLjngTGeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=eJ0yZqCh9Evjgd3J5PpHsInT-4ppyeWLZrlXh5TJwMjo7StfqwE4GJEDnKJ3BZfxIcW6jKlB4_3-rEJFinPVqhtH8LNSM9UIGjz5deBAWASkIQ-czXJsgO4cupOFqU_e-n_gBQUjCq7YyIh3BPGN2QQCbU7ZqJv3F9gzX7hgaK-Y3MvEhJG-vGTopeZb0DH2bHq4LCTv6CsGJLRWo_8NvHlCPRJXJayjRqIlaGDR-R4VzQrUzUT1WnFCLCsS6eagIvswLi9fJdraqapfqnbyWfD13bUclz5Hb2XsnbR_pyYgmQFNYmdqvv7qx-lKuy7u6RBsuMszN0c9rJLjngTGeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
«یک بازار جدید دیگر هم در راه داریم و آن، کشور دوست‌داشتنی ایران است.
ایران کشور زیبایی است. کسی دوست دارد به آنجا برود؟ جمهوری اسلامی ایران با مشکل تأمین مواد غذایی روبه‌رو است و ما قرار است بخشی از پول آن‌ها را بگیریم و آن را خرج کنیم. همچنین قرار است مقدار زیادی گندم، سویا و ذرت خریداری کنیم و این روند به‌زودی آغاز خواهد شد.
این برنامه هم بسیار بزرگ خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66856" target="_blank">📅 12:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66855">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sw0cX-oXSzeADz8PXWHPFtKsEbhwOG8_fmYkWt9qKIYieI_l0BQzTabLOx1Ur_sX_CetupHuAXn1elvI4cpv4UY0WkfRmEK9XemYj2r8zxhOptxvllNm69Uuckn_8ZMDS2KWI48bcS5pzVmJSfJJaBnNCcpU1PwF-wvoM5blbPqgfL2AkaEVmlUl2LkDYyEXtGfYqoWk1Qz82L9vHG1NbNqZ-XOIbBCofaPc8uJLXmckl9nJrhNRF_G8fiohYcB3XtsbggCm33SHi9H4HTnG7sI-91jGa_MtwuMEYvS8tVG-Y4lB__JK6ByWH9rc_o4sOZigEddlM1Nt2nc_6EGmmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ:
روند خرید محصولات کشاورزی ایران از ما خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66855" target="_blank">📅 11:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66854">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‼️
جی‌دی ونس درمورد ایران:
🔴
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
🔴
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
🔴
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
🔴
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
🔴
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
🔴
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66854" target="_blank">📅 10:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66853">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=CCWI45Me9maeNb2z0kPnO9omOPBv4KOzGhWCvM1kBpU_hfqj_Oqzg1YtZutBIKjqxTPHGZ822Jyn4x5uVnfWqGe-GmFEWOGBP1XJVD-LfK-f0cqcIsFDp-szSyDEFL4m7AwWcNmISZnx2D_JZvg9r1xvMYZhsklZtrnVRFLuJ6Ow49xhpaZgVIdYVwC1bndcjCfPC7vWi7qs0aZ9TD3HTsYsyEraA2TYXvVnUm9mM4krcWFKvr_cXrf6mfmKUzBfnU01rmrC6rCMUr3G9PNlMgaSrlxkN2aKPm0IJnaF3qji-m1bxMHNgHZF-DjfS9KHsnQfnza-YzZ7LWFtc_BBJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=CCWI45Me9maeNb2z0kPnO9omOPBv4KOzGhWCvM1kBpU_hfqj_Oqzg1YtZutBIKjqxTPHGZ822Jyn4x5uVnfWqGe-GmFEWOGBP1XJVD-LfK-f0cqcIsFDp-szSyDEFL4m7AwWcNmISZnx2D_JZvg9r1xvMYZhsklZtrnVRFLuJ6Ow49xhpaZgVIdYVwC1bndcjCfPC7vWi7qs0aZ9TD3HTsYsyEraA2TYXvVnUm9mM4krcWFKvr_cXrf6mfmKUzBfnU01rmrC6rCMUr3G9PNlMgaSrlxkN2aKPm0IJnaF3qji-m1bxMHNgHZF-DjfS9KHsnQfnza-YzZ7LWFtc_BBJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66853" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66851">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=vifJ_B6UCdbrCpdoIBsE0SjAWT8z4HoFVirn1GnjRUAjhfxCaRbyXlZS14K8Qb6EQVyE4wj4H9ijfQa0hcARwRndsoPzpGqC1iNWyS10C4di9jFuP1ZPK9Vk97bGJJ_VSwJLg0gT3ZiARf8Jy4DhY5yUh6UHkLURdC0I9R1Ssoya4r_ynCKW9yoiyJG8PRaQr-WtPM_YMRWtPSvSJroZYkIIeL2yxWqZNgYPXHfdbWJKH7tGrhVHUGsCaQ8YhjHlWOsST2v-WBw7aMAjgfB5YUrtlqYQfrTVTTmPkI6LxAqb0-faeKZfgRhu8KlKRfF0csemu22eTycCBQi5gOpgAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=vifJ_B6UCdbrCpdoIBsE0SjAWT8z4HoFVirn1GnjRUAjhfxCaRbyXlZS14K8Qb6EQVyE4wj4H9ijfQa0hcARwRndsoPzpGqC1iNWyS10C4di9jFuP1ZPK9Vk97bGJJ_VSwJLg0gT3ZiARf8Jy4DhY5yUh6UHkLURdC0I9R1Ssoya4r_ynCKW9yoiyJG8PRaQr-WtPM_YMRWtPSvSJroZYkIIeL2yxWqZNgYPXHfdbWJKH7tGrhVHUGsCaQ8YhjHlWOsST2v-WBw7aMAjgfB5YUrtlqYQfrTVTTmPkI6LxAqb0-faeKZfgRhu8KlKRfF0csemu22eTycCBQi5gOpgAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسری و ماسک اومده بوده هیئت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66851" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66850">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=eqr1arHv5UlFj5jQRg94ivmIK-eFCDDnJidNGDrvR5Q6ity8697LT7ACciW8o2KWm1lM9iCYuVoor8Np_NHVib2PvaBo2Oj1NMpLI2vSxmgPKT4TPTj_jL9vx1j-aLNVzyIlCoURo0Hg-WDXRFS4z5Id6P4rHumLkKXpUatIwtzk0L80D_dy6iBc4qm69X2ZAr-Vqb1t667zhZeqq7Z1JS0-THFmqxamw1wlDgO6ri42RSRv8KmK_AN3mpFOOuES81GktVcXSUBtZ8xWg0znKSpEl1X6c79KIncimztLiEXx7hAGfY4jB9FXtf2Y-VSetL-3uv5u0Ovm_8JiHSt2Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=eqr1arHv5UlFj5jQRg94ivmIK-eFCDDnJidNGDrvR5Q6ity8697LT7ACciW8o2KWm1lM9iCYuVoor8Np_NHVib2PvaBo2Oj1NMpLI2vSxmgPKT4TPTj_jL9vx1j-aLNVzyIlCoURo0Hg-WDXRFS4z5Id6P4rHumLkKXpUatIwtzk0L80D_dy6iBc4qm69X2ZAr-Vqb1t667zhZeqq7Z1JS0-THFmqxamw1wlDgO6ri42RSRv8KmK_AN3mpFOOuES81GktVcXSUBtZ8xWg0znKSpEl1X6c79KIncimztLiEXx7hAGfY4jB9FXtf2Y-VSetL-3uv5u0Ovm_8JiHSt2Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرماندهی مرکزی ایالات متحده:
جت‌های جنگنده اف-۳۵ بر روی ناو هواپیمابر یو‌اس‌اس تریپولی  (LHA 7)، ناو پرچمدار گروه آماده آبی-خاکی تریپولی/یگان سی و یکم اعزامی تفنگداران دریایی، در حال برخاستن و فرود هستند. ملوانان و تفنگداران دریایی ایالات متحده در دریای عرب در حال عملیات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66850" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66849">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66849" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66848">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sODSAtRvtRh8H3wEPLTg35T3vUB74gHvnnVfoLcTjlY7DukEOr5vmelN5t3-nXBlv8ZQzsj8wH38sLzq2HKIWKpy1U5tuYyy-Sfpge1umzE23wsMfvsh9puA20vh2WmKVLAd5E5DyJF2ILPQebA1Wn8iCdcIPj3gVhpG2H-jpIMp06moPG_rut0EGS3TUwQJCO_9ZhA7Pqk7odyCzmFKyKlcpeP1ybDIdJIJ6A2lea2Rp4lWTIq0uO5Y4-qrvMIdZXNuy-AGUKI66mV3IkFsqB-s_iQd_rVb2crCcQCktDzEdeBf01hDSX51tlN8VnVplZk8qiF_YJnxq1-A74dgSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
@Palang_Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
@Palang_Bet
@Palang_Bet</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66848" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66847">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-Z4kqz-1_PopVUbnuCHsYudLBUKUKeuvpeyxRpf5JNwbfY9iCZio3BxB07vq4fjFNqH8ugzzPS37Dp3aIdc1qOmgGfXEZAtYY99lcYIkHXg6FMq_5dJs6puZgyk2bFtfkEn9ZmqnkH42hfyGam70lDK6SwqUAJM0ONJQrh4VJYiC2bZsM6uusHmxNB9pIAsFP2_4iY97WWdWr_ILUJG7p5JlYu0A572dNLuKjAMw5nXi1_Am9j58lqOgq5kQzpiPSkYrCA1wmmRPJFxBm6qADBzVrdFwErMNna1-RGpU-tyXk1j3LG8tmZaoGFOEnlGsmNNlT2iVA3r15pUfXIX4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏بر اساس گزارش وال‌استریت ژورنال (WSJ):
🔴
ایران روز پنج‌شنبه به یک کشتی باری با پرچم سنگاپور در تنگه هرمز حمله کرد؛ اقدامی که به‌عنوان آزمونی برای توافق هفته گذشته میان آمریکا و ایران جهت بازگشایی این مسیر حیاتی کشتیرانی تلقی می‌شود.
این حمله به پل فرماندهی کشتی آسیب زد، اما هیچ تلفات جانی در پی نداشت.
این حادثه چند ساعت پس از آن رخ داد که ایران به کشتی‌ها هشدار داده بود از مسیرهایی که مورد تأییدش نیست استفاده نکنند
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66847" target="_blank">📅 01:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66846">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رسانه های اسرائیلی اعلام کردند طی درگیری ارتش اسرائیل و نیروهای حزب الله در منطقه بیت یاحون در جنوب لبنان چند نفر از سربازان ارتش اسرائیل از تیپ ۷۶۹ مجروح شده و با بالگرد از منطقه تخلیه شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66846" target="_blank">📅 00:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66845">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">با بحرانی تر شدن وضعیت ونزوئلا و مفقود شدن بیش از پنجاه هزار نفر گویا به نظر می‌رسد مثل زلزله سال ۲۰۱۰ هائیتی که ایالات متحده آمریکا به این کشور نیروی امدادی/نظامی ارسال کرد دولت ترامپ هم به سمت همچین سناریویی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66845" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66844">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
وقتی نت ملی بود ، تنها سرویسی که برامون قطع نشد همین بود
🔥
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66844" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66843">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRPD4Lh7BIlGJ6n5a2sQK4Cw8hGWJfDxye4NXI99HMp0KiwwyB6JM_4u6cWKQ3kd73qjQqPhm9guDgkkm7umofFWHMKlFw9FhtQGiBObAYszFc3Idr-hEOYBiqc2T5_cnromddOULAqcf8n_p2jeQA8vMp1WS0C9rWZH4rLhN-JbDWaLctr8eOcXDL1iALaQnhTqDbRmwJU5baKE3E-XfXsLoDZY5VsJiMqBhbaxKCE4KrqNPkLz3K3QAbBCqNhsh-MC4L5WsUBhhfJcfepdDzMEEA0zvlSUkeSzBFFwiSw_uoY00hGCjqV34s5FTNmlzVoOKpu3KcZBRbySKL1_3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کانفینگ نامحدود برای همه اپراتورها
🔥
⚡
سرعت بالا | بدون قطعی | تحویل آنی
💵
یک‌ماهه: 380
❗️
پشتیبانی 24 ساعته واقعی
❗️
✅
سازگار با تمام خطوط
🚀
اگه سرعت مهمه، همین الان پیام بده
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66843" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66842">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWFOSzTXbOyprhOiUXsaFJPlwr7Lyh0pI2uKHIWSG7tY9wuLLWpAJEyjJuygpNUq4BH94hsqO5Tdjb9BNVn615UZOazHTWt209CNfgBcxMU6ziy-bcvttcxCfCEkoNtf_R5ia3lVOMapvP8iO0JQi5DVqtUlT66B4zLmBwxY2PicREh35A_L-p3XrDZuDMh8r9DpnBvaLEssQPvOgNu1bU32etjyDcUnie2R8dEIJHlA5BOm7-2MEmhqdlY2eEO9Rxnx1fbyqPLR2w-wp_nBc8Y5gDFMAuxTH_jCORCU7uWftHVK1hFMP5rLDLJUsUndT4E8EZThxyLZ0ADcPwCTwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش از لبنان: جت‌های اسرائیلی به بیت یانون در جنوب لبنان حمله کردند.
این پس از تهدید امروز سپاه پاسداران علیه اسرائیل صورت می‌گیرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66842" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
