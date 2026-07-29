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
<img src="https://cdn4.telesco.pe/file/Oru4rpP2zpgsS6IyWlDbuDb6nNRY-4uIMFOUc-g8AuGvM2lhNze520Ea7TDPJYinjHAZJV42FS-LhtGePGPI3UzOqTsEhwExQuTb7t2pEN3vrFkZjx6aG51eyc8fu2x7VX-nK1qJ9hok2JhJYgIUsBx7PzHdq3xUl8t5wzSN5cYxgDS7eFgnc0b__ukGgPrUmY_8VWLUMYeGpwtgzXCmGbhUHnhx0rwu-83jsdLs3ySC42CiSFkEbY-uOqciFKmS3VCEvG3PFLljjGG76t0S2zcj8lLYVkMINYES6K59-zjaoRDa3uGLkQoKNtBEKUhcEfT3-Oho2M-YIsSCv6dMsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 18:55:34</div>
<hr>

<div class="tg-post" id="msg-19434">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مقاومت اسلامی عراق با محکوم‌کردن حمله آمریکا به حشدالشعبی در کربلا، به دولت عراق تا ۲۳ صفر مهلت داد تا توانایی خود را در دفاع از کشور نشان دهد.</div>
<div class="tg-footer">👁️ 620 · <a href="https://t.me/SBoxxx/19434" target="_blank">📅 18:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19433">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مقاومت اسلامی عراق اعلام کرد که انتقام خود را از حملات اخیر ایالات متحده تا پس از مراسم اربعین به تأخیر می‌اندازد تا امنیت میلیون‌ها زائر مختل نشود.   این گروه هشدار داد که حملات علیه نیروهای ایالات متحده اجتناب‌ناپذیر است و گفت که در صورت لزوم عربستان سعودی…</div>
<div class="tg-footer">👁️ 772 · <a href="https://t.me/SBoxxx/19433" target="_blank">📅 18:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19432">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مقاومت اسلامی عراق اعلام کرد که انتقام خود را از حملات اخیر ایالات متحده تا پس از مراسم اربعین به تأخیر می‌اندازد تا امنیت میلیون‌ها زائر مختل نشود.
این گروه هشدار داد که حملات علیه نیروهای ایالات متحده اجتناب‌ناپذیر است و گفت که در صورت لزوم عربستان سعودی نیز می‌تواند هدف قرار گیرد.</div>
<div class="tg-footer">👁️ 864 · <a href="https://t.me/SBoxxx/19432" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19431">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رسانه‌های ایرانی گزارش دادند که 4 عضو سپاه پاسداران از کاشان در حملات مشترک آمریکا و عربستان سعودی که در طول شب به سایت‌های حشد الشعبی در عراق اصابت کرد، کشته شدند.</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/SBoxxx/19431" target="_blank">📅 17:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19430">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نتنياهو امروز با پیت هگست، وزیر دفاع ایالات متحده، دیدار خواهد کرد.</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SBoxxx/19430" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19429">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حمله موشکی ایران به اردن</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/19429" target="_blank">📅 17:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19428">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJO3bDoAEdNhuTtstEfdT6vhOYGeU8huKp5NP0TTG8ToqjccK_NcajfK5qIO2O4EHpFlXwy0XucOJeSSAdHBCDtsPrvgfzHtLIpCEX1Q87_Lobaleao_bohDS68HcV2drMcV1kK_LbwqlvUGVuQOu_ZV_Grn6LSXHZpaeoC7T-3v7b71JhW-LFpgCHDTsQnIRJ06dmmsE1QGcEJHbMUgSpSnFJ98AOGRRGLy7MMM5mxRazYLIRBL3RJs_pSARQW9xqZdiZDKq8UUAzZ2-NcphewynocizdwSgMOYjca73jBg5VmWDuC3Stb-QkIDJGPQweu5rtvLnJeDfP5AUY-W7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای وزارت خارجه در هدف قرار گرفتن مواکب زائران حسینی در حملات دیشب سعودی و آمریکا!</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/19428" target="_blank">📅 16:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19427">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/19427" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19426">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/19426" target="_blank">📅 16:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19425">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انتظار می‌رود که اسرائیل امروز به حزب‌الله پاسخ دهد، اما این پاسخ احتمالاً مناطق جنوبی بیروت را هدف قرار نخواهد داد.
— کانال 14 اسرائیل</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/19425" target="_blank">📅 16:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19424">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده:  «حمله دیروز ایران یک غافلگیری بود و نیروهای ما تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.»</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/19424" target="_blank">📅 16:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19423">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده:
«حمله دیروز ایران یک غافلگیری بود و نیروهای ما تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.»</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/19423" target="_blank">📅 16:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19422">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وزیر دفاع اسرائیل:  در دور آخر درگیری‌ ها جنگنده‌ها و سوخت‌رسان‌های آمریکایی از اسرائیل پرواز می کردند اما ایران همه را زد جز ما</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/19422" target="_blank">📅 14:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19421">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پرتابه دشمن به استان آذربایجان غربی برخورد کرد - فارس</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/19421" target="_blank">📅 14:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19420">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مطمئنم امین سهامداره  @Piknikanalyst</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/19420" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19419">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vDsiC6KyJj0yjwWh4xmzAl6LwM8POw7t4DnxlBi1Kr9b7B5IzWWNdZPFoz0qeRhOkPHiqMR4w9XF0t1JGPYuphFJ4os_7-6DXR0Sf2Jt437wK_joyETf19HRBDqwwjW7sYcMp69BA0IzwcWY3vQVtHXC5F0ZXsU377CD4XWqtC5OCFvqs3lylwcDpQP4L2bF5ID3jB60yZfIzuRL68muyO34BfKa_D3QjTWyuK0LQ-lN017dis4NcernTN2_58avcZ7-BNqwsPKrBa8JVmFeJrS1Jnju8cWH-YdD7aUD_ewjWcpxs9R39ZCKJCXeoIxYGf7htvddFs3C-aFtZapiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطمئنم امین سهامداره
@Piknikanalyst</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/19419" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19418">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نیروی هوایی ایران اعلام کرد که جسد سرتیپ مجید کاظمی، خلبان جنگنده بمب‌افکن سوخو-24MK که در تاریخ 2 مارس توسط جنگنده‌های F-15QA نیروی هوایی قطر سرنگون شد، پیدا شده است و طی چند ساعت به کشور بازگردانده خواهد شد.  نیروی هوایی ایران همچنین افزود که مقامات همچنان…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19418" target="_blank">📅 11:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19417">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfJA6198tt6rI6j95uazG-aNRDvq1m5O5YCJl09EXbl34NBR3WbmfNBtbXhYBVsK2o-B1K8yimjCjZt_pq-aRjhUsdGFHBj-qNm6NNhS3QSx-wOr9063VQ58FxlBu2tqjDOg6ZH12Fph3pKq8wU28QHQDNnr8wqHso_PPs9t6z06QLdUX7ZEseUO_e-n6XxYDjyD_-7MlYMmEjvMtg0MNKf_RaSDVDgkP9LUXmTdWgsJrPJgvnYONXJOXibZuPgLIIxt1QJ8gY8cYprOTVEJhknPljKAr6ZTNrfBnIzZDP38TgGz4ipScmcIs_nm8KCO1lb6mdnbOwkEskph5gK-SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران تأیید کرد که تعدادی از ناوگان بمب افکن‌های سوخو-۲۴MK اش سرنگون شده‌اند.  این هواپیماها در حملاتی در عراق و سپس قطر شرکت کرده بودند اما سرنگون شدند.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/19417" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19416">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a40b3b45d.mp4?token=OKjjHpGs__lOO8A-gyPpWDqyYIqsSj7XEnv0o3AW6wjOT_aBBT8lINXEL5AdundYxubCaHC9xfVT-U6Roeft9Zb_MQnOSdigbTrhiAUR32O45g3d0_6X-6tZmiIIg9mQpFzY2aAYTeQTWZNkyVrFHUdkajv_jiwQoh1xwlQdACns9Zbp0UxCYFEIvxW4ys__qxOZv5IR5jcD_G1_pp7DZXH_ProI67HROvOxjA0EWSXYe-UKsW8ocf4EFdj7rgr80F9mBMqeAK_M0DS8Iu5CneXnqtS0FAuvtiydH6Ue0vP8pu403-e5R804WCFC-3D_XKVsITctlJRZ-6gl5JxVLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a40b3b45d.mp4?token=OKjjHpGs__lOO8A-gyPpWDqyYIqsSj7XEnv0o3AW6wjOT_aBBT8lINXEL5AdundYxubCaHC9xfVT-U6Roeft9Zb_MQnOSdigbTrhiAUR32O45g3d0_6X-6tZmiIIg9mQpFzY2aAYTeQTWZNkyVrFHUdkajv_jiwQoh1xwlQdACns9Zbp0UxCYFEIvxW4ys__qxOZv5IR5jcD_G1_pp7DZXH_ProI67HROvOxjA0EWSXYe-UKsW8ocf4EFdj7rgr80F9mBMqeAK_M0DS8Iu5CneXnqtS0FAuvtiydH6Ue0vP8pu403-e5R804WCFC-3D_XKVsITctlJRZ-6gl5JxVLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمار تلفات حمله عربستان به حشدالشعبی  ۱۰ کشته از تیپ ۳۰ شَبک ۲ کشته از تیپ ۲۴ حشد الشعبی</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/19416" target="_blank">📅 11:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19415">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtJ96RT4HLDPpM_cuVVJu3pk83ROdzvTT8ZjIZp_gBdjB9vmPFb4oFNuxWUMu5HMB7v82rcIxpqEVusJyJDz9_uZ_hAG2XQ9txMQP4quZcdPz-LU7iOQ5ZBRwxhXKj--9ATiY_XPCmWLqnx_AwOv_ScV8k8NZnGfyZEXlxuaJpStOncI_E-lnNphG9w1PAVvHtrQWK-_rMXYi-9gHsQxbNeMqIpDbZGQPcq1aNe53aNpgHOv54zCNXMD2DLrQvj3JoZarlWVgLnr_e_OUkoUOeBQ4PJNYUkBRLYZ5p-f6NfP_SAEv7dbenNoxTFPRaWaiaEmSz_t91X2gGMeZ5wkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز هم در وضعیت مناسبی قرار دارد و انتظار رشد طلا می رود.
دقت کنید که امشب نشست سرنوشت ساز FOMC را هم داریم که سناریوهای موجود
در این یادداشت
بررسی شده است.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/19415" target="_blank">📅 11:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19414">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خب مثل اینکه «درنظر داشته» حمله کند  ایران، پس از حمله اوکراین به یک کشتی ایرانی در دریای خزر، یک حمله نمادین با موشک‌های بالستیک به یک بندر اوکراینی در دریای سیاه را مد نظر قرار داد.  اما گفتگوی تلفنی بین وزرای امور خارجه ایران که در آن این حمله به عنوان…</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/19414" target="_blank">📅 10:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19413">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خب مثل اینکه «درنظر داشته» حمله کند  ایران، پس از حمله اوکراین به یک کشتی ایرانی در دریای خزر، یک حمله نمادین با موشک‌های بالستیک به یک بندر اوکراینی در دریای سیاه را مد نظر قرار داد.  اما گفتگوی تلفنی بین وزرای امور خارجه ایران که در آن این حمله به عنوان…</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/19413" target="_blank">📅 10:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19412">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCvciYbipk3SlFl_b96F3FA5SoAfMCNWpbSTZRiO4Qbl2wlD5c-LvbszKCe-FiCZTK6wlw1b6zgWO61M52m9ifHN1skkQTics1WdONpVdvZGfknK0UgJpwzIP4J1KFnfNyRH8X609GVauMWwq-ZZJtuUPZNYHnPFznGazUtutHwaaY-ZPxcvDhBJejXw1VxXxyn67Fsf6VtNnIlbKaJpySBu5VCTH3clsFKMylKpwosIGOHwdZ0VdlUlCOYgvV6BR2r67qhJoUDu-5UBdJKMtkkrYHSQyGNRDx-quH3t-0UmS_ytqKkReUDjbVTqQbM3pXByiXLkRIlz0Dz-LwHMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/19412" target="_blank">📅 10:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19411">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAXXM_MdhQeu-5EpKkJ5atniBHqlt0vYlGTBF0A4_nuEyOfuY_7n-GtdOkzyJeqGsZNt3u6J_EvgQoBxwwiy8Rr74sqJmCrt6YJJaJhbGHSduz2DzBr0kpkIK3cHPqIYj6Y6snKTrjkVThlRI1UCddRuLtwBMYpCoj532Dpn5y7gcCMw-C3_A2pMRqhhS8nRD3c-csKdFWhC9wYKRAN-thv_2XtADwhwvHKj-CJI3ZN698yd2iD_366A-plSmrrb-D1nbokr6qIiNdCRYFpqJ1jL2cw-aJz5slZVXjl3YiITZpIog-NrSXuOk3AF6cxp1SA_1khGDZgCDs_sQ7WNMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌ها، ایران قرار است در یک قرارداد به ارزش 60 تا 70 میلیون دلار، 300 تا 400 دستگاه موشک دوش‌پرتاب چینی (مدل‌های QW-12 و FN-16) دریافت کند. اولین محموله‌ها طی چند هفته آینده از طریق شهر اورومچی و از طریق پاکستان به ایران ارسال خواهند شد.
این قرارداد از طریق یک واسطه مستقر در هنگ‌کنگ به نام "Zhongqing Baoshang" انجام می‌شود.
چین و پاکستان این گزارش را رد کرده‌اند.
منبع: رویترز</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/19411" target="_blank">📅 10:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19410">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJXrE5RRJbkVvBFDt1mso8vHyoMh_TrP6x6oDvwCtBDI059uKtHcwHld8vqrgEeRhrU3LKNNpfkiIKDzbmWDjJXT6_o6uFrKR-K660WUlihWHxCeN5iFCnljGvWJKbKo2a7MDN_bnoyHRoHMVzDhrEabXUJQp59GXMgMOuDZkpSwT64JU_n5h5DIDnMGw255pIvkPmGK1-NiYV0-WmjC-tarQGeN7brUi8jONv9_SNZNY1VWpJDu9limpJoaYLYNMbKwmsgnQ31L-fTg3EzBsXyf-62UBUyHn-Tskko-Y3f7iOq1_Ip2a4xsSBbxhic6D8a5MjshRb1pCi-XmThuCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/19410" target="_blank">📅 10:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19409">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/19409" target="_blank">📅 10:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19408">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حملات عربستان به عراق !  گویا نیروهای حشدالشعبی هدف قرار گرفته اند.</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/19408" target="_blank">📅 09:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19407">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnXygfyl36qKez-Ncu_iriHaM5WM4qLDl9VyzTbFfel9yqydZr0quh03FDI5D3pdBhh9Nr-Nr5_iazlQaNEcna1xDbDKNS-X1s5-iHM9mGvp5flKhTV3j-mnwij-1QAY6y_D5sIn1gAcFnPgNAttocXdsGCuQfpQ3gHKqsjMLy7bCxUcWp1ogIe2ZVoQo3_3WIcAjCdNZPZzfCli-Fs_cO9WgvFrxHsfZdwnGX5ZAppP9xKFRpN3EVtpuzD_MXnPxc8JfmhsFYM4gKkq6bcT-CJpWrxpyA-SefHsm67fURkrcs6kWf-cy8POoxy2xuXCYjU20oReNA14KCjW17-IXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
فدرال رزرو در دوراهی حساس؛ تثبیت نرخ بهره یا افزایشی که پیام انقباضی ندارد؟
محتمل‌ترین سناریو برای نشست فدرال رزرو، تثبیت نرخ بهره است؛ هرچند افزایش ۲۵ واحد پایه‌ای با لحنی داویش نیز همچنان یکی از گزینه‌های جدی بازار محسوب می‌شود.
واکنش بازارها به تصمیم فدرال رزرو بیش از خود نرخ بهره، به پیام کوین وارش بستگی دارد و مسیر دلار، طلا، اوراق و سهام را تعیین خواهد کرد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/19407" target="_blank">📅 09:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19406">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حملات عربستان به عراق !
گویا نیروهای حشدالشعبی هدف قرار گرفته اند.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19406" target="_blank">📅 03:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19405">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nC6Exr5Sp5YHqHy2D1-3JOhXGIHLdfJfqlixeqOA-kk3v1RpnHKJVrbHSn5tsl2-ykE8B3Yi9BSJmXHxP9Pgb_PqE5HZpkCZKr8zCSRukXi6TW1MPQjpHlB-3W2sPyroMyow_f7hF9Efx6MRzJ0rnEHHnhx3riy81juGRPvjI4opakXglL_kl8vJbgKjPdgt-Zzj5kYiS2l2aINlYbu7o04plW-GSAfRNj5VAKjtmHGGfk29wuPC5lLVnwt5C2V4OYSTmHCRv1DHAgF_PEZTUEp-oMWvS-7pGaJz-icqwkDcZPVAF7vTXSTY7dwRg5z0aBZz2xrvyjdbuAyk5wEQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19405" target="_blank">📅 02:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19404">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Psvo-YWXFiX-GM00Kftp9kvyP8Q0iQfhKFm0wL8k1p8ps5HcEVCpWJmv8w8ddTUIwChp8nk64FCWyR7PsLDm7WmV_sWTBDKnYpVIHsvPtQhISC74Q73Ja-cpyssvmPbuIMYw7ephrWTgeKefcj0y_m_Tta27pf4zycrtR-eAp5ga134EKs5XHqfvEAA39ruROS4TepvP3CQlbfCO0FEGyEmtVt2OL0FiAnE-BtMA8ixMRnrv-B8rS_8PK7G5GHV50q4ISiBN8KR1mR5S3HkoUvg6Eb8EsAq29Nk6zm2EA0HHMut0p6u4Mn00xkUDSqqyN5f68d48zpvW5QqBCOHNVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه جنگنده های ما پرواز نمی کنند و این یعنی احتمال حمله هوایی بالاست.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19404" target="_blank">📅 02:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19403">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilZSePzJJKK2-jxcHkIBnSNwf6WJYtQw5q6WQz1iWs06B913tkN6ALszLBG0qyCJvI-Tt43TIP0yxX7u3dpvlAppW0YeSHWzQ2_7j07Q_ppKJt9OayP-yMWkPS39fxeZVJSvi-hWn5CDUkhKci8Qisi7mSDtBkg-xnztdeD81YAPtUH2xekKlMNqlwgYLM1Vgo_MgTvvvb4Y4oo-vlN2Kg4l_pNPiEuEO-xVG3wMdwwKLzOpDTlQw2Hgg-zHoMdbmicJS_PZVsnZdNCmsKN-HjrDXCS-pjdeC5UGKZuWQVQwRbywainE-trysTngQsK4LDbB1RQ8bqYF0a--HSjU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلاً قیمت نفت بیش از 5% پرواز کرده</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19403" target="_blank">📅 02:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19402">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دیدید؟ همه گویا رهگیری شدند!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19402" target="_blank">📅 01:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19401">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oO32T-kFxhJgjrZIutZt4lvuOt1jznTRLSrdPT77kSM4XRbD5GhZbYzZKUIoDWNivfC9QvME564Tzc01c4216DZCsSW6BS5yyBibILy3_64hIBL0Xbjk9wVp_FRLeoXGk1Zik8a4QKqvAcGDuWCBxR5etWvhAK92Z1qbBHfTWb1Og_Dvbfpsw9jfyN8IxaOnmResCb5enAlN5B5wOnIMa1WVpITxpVQPzKA4w_vE_PmjcBeKQgFNTyPK0meawiU2EDwDUf5d4NSPSkD5SPiCePtQLyp8jB4uRZXRtDOVV0RMzTtxSYlgLI7eBcumbtvLXVrPhClbt5H_0rc3FEkNLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدید؟ همه گویا رهگیری شدند!</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19401" target="_blank">📅 01:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19400">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اگر هدف پایگاه الازرق باشد هیچ اتفاقی نمی افتد.  مگر اینکه یک پایگاه الاحمر نامی را بزنند تا در هم کوبیده شود.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19400" target="_blank">📅 01:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19399">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صبح ها اعدام داریم، ظهرها قطع برق، شب ها جنگ!
بعد برخی آمده اند تولدم را به من تبریک گفته اند!
وا بدهید لطفاً.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19399" target="_blank">📅 01:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19398">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POeJ_fI6GameT09Gye4ZpysrE5-iYVS_q3jdOKvwjvPuF9tH_HmgO91C74vNTFVQCQhCOknhqERNtmLywJTEMZXsp03xgc1_Y-HGX4C0_vRXDIhaENf5xyE-PuNDgdmSB4V46IYB_4hXydPQhZ76HwNcjgBNXyoyouXt6z__WaQ6DdrACVEohjH6v1hO5XP_Cdvd37rgCwzG84Od9jmFRw9zWb75AnCjSPT1b76kBauoVwZmjqPKN2Yxn-Oze7CEq4xl9xDyIiXyNfaHWbR4r-xAH9QgoBZ5so3t_qMWmr4cVGFI6F9VAPBpeulZ5NBjSjumDAsvFyE54UuIcDM6dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جا دارد دوباره گوش جان بسپاریم به آوای روح بخش بانو لورا برانیگن که زینت بخش این شبهای پرکت خواهرمیانه است.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19398" target="_blank">📅 01:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19397">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جا دارد دوباره گوش جان بسپاریم به آوای روح بخش بانو لورا برانیگن که زینت بخش این شبهای پرکت خواهرمیانه است.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/19397" target="_blank">📅 01:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19396">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مقصد گویا اردن است.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19396" target="_blank">📅 01:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19395">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">به نظر داریم وارد موج 2 از 5 می شویم و موج 1 از 5 تمام شده است.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19395" target="_blank">📅 01:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19394">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گیِرْت وِلدِرْس، چهره راست‌گرای هلندی:
من آرزو می‌کنم که در اروپا افراد بیشتری مانند بنیامین نتانیاهو وجود می داشتند!</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19394" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19393">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">موج جدید پرتاب موشک ها از ایران</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19393" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19392">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شلیک موشک از ایران به سمت اهداف نامشخص!  (اوکراین؟!)</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19392" target="_blank">📅 01:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19391">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شلیک موشک از ایران به سمت اهداف نامشخص!
(اوکراین؟!)</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19391" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19390">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرگزاری نایا : موشکای ایرانی همسر دوم یه مرد اردنی را لو دادند!
یک خانم اردنی در جریان حمله موشکی به پایگاه موفق السلطی اردن، بعد از دیدن آلارم هشدار روی تلفن دومی که شوهرش در کمد پنهان کرده بود متوجه شد که  شوهرش از این گوشی برای ارتباط با همسر دومش استفاده می‌کرده است!
به این ترتیب، ماجرای زن دوم شوهر این خانم  کشف شده و اکنون وی درخواست طلاق داده است!</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19390" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19389">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuBPB4zclVU4yKXH_FU-JDr37sHBPQAUkZW6hjWfwht5e179n-8ridyxCdm6QXkqVkuN3Z6HwxZ9RqBnxK4ODwCVqRKjhQePIMrkHRa8zAc19GPXwGlEluSrc4FcfuIwJNDFKFrYsuD84xDk6PmRTbTGKzrasgwONHL-IRbJutf-eqXB5qM3GPt0ws1DjlEdiByC_1HMYLzCR-IAo7v_FS46m1krLXWyJu5BvR2cP0n3cDozFnJgwNh_yb6vZsqFFqdzagLoU5nz0KaMncoPC0vNffGkdW34mWKE697VG1E38yNovt4ncevVdGmapwgiNWoKU04aS3FEwaWSKlupbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:  برخی از حاکمان خلیج فارس به صورت پنهانی به ایران پول می‌دهند تا در آرامش زندگی کنند. برخی دیگر در حال عمیق‌تر کردن پیوندهای دفاعی با کشورهایی مانند ترکیه و پیوندهای اقتصادی با چین هستند.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19389" target="_blank">📅 22:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19388">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHACdkXm16oBwNABwQnOL1jzCwcvZ2HA0Muw3aYujvSyAyJO37LgeOnfHL-khRALqnvyg6-LsHexA4RUHEG2-j8XcGvwips9EnAppTv3QIzcAax671FuZL2u2v_AffNfIyESYqXjQrtjSd7ZG1lKS-3izS5HkMdL9Rvb6zJM8QNsYvaRprzmEXh3NjuXT513tZoTZ5uF_apA-s0hjJRk8Q920WS0ogXtHjpVI_q-xBDNDWn_O9Za_zI-V65cEOzf-DwfY-F6m5gDMc2RwnwJmOXNbVGQCw8e26SpAaXZ9Hu5JLPrnrF9rI59Mng2m4VzM4B8CdBTdU6zNmQbnF-OUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقت کنید که وزیرخارجه اوکراین هیچ عذرخواهی نکرده و یا وعده ای برای جبران خسارت نداده است.  تاکید کرده که هدف ما زدن روسهاست و هر کسی با روسها باشد خب هدف قرار می گیرد و جنگ روسها ضد ما غیرقانونی است و ...</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19388" target="_blank">📅 22:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19387">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وزیر امور خارجه اوکراین:  من با وزیر امور خارجه ایران برای یک گفتگوی صریح تماس گرفتم. دیپلماسی به معنای گفتگوی مستقیم است، حتی زمانی که این گفتگو دشوار باشد. من تاکید کردم که هدف ما اجتناب از تشدید غیرضروری است.  من بار دیگر تاکید کردم که تمام اقدامات اوکراین…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19387" target="_blank">📅 22:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19386">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزیر امور خارجه اوکراین:  تهدیدهای ایران بی‌دلیل و بی‌اساس است. رژیم تهران یک همدست مستقیم در تهاجم روسیه به اوکراین است که با سلاح‌هایی که از سال ۲۰۲۲ جان اوکراینی‌ها را گرفته‌اند، جنگ جنایتکارانه مسکو را دامن می‌زند.  ایران هیچ جایگاهی برای ادعای قربانی…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19386" target="_blank">📅 22:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19385">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/19385" target="_blank">📅 22:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19384">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">غریب‌آبادی، معاون حقوقی وزارت خارجه:   هر کس فکر می‌کند که می‌تواند، بالای ۵۰ میلیارد دلار از تنگه هرمز درآمد داشته باشد، کنترات می‌دهیم برود کسب درآمد کند و نصفش برای خودش و نصفش برای جمهوری اسلامی ایران</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/19384" target="_blank">📅 22:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19383">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">غریب‌آبادی:   پیشنهاد شده با عمان در مورد یک مسیر موقت در تنگۀ هرمز مذاکره شود و اگر تفاهم شد، جایگزین مسیر شمال و جنوب در تنگه شود    عمانی‌ها گفتند مسیری را طراحی کنیم که ۵۰ درصد آن در اختیار ایران باشد و ۵۰ درصد آن در اختیار عمان. ما گفتیم این موضوع رفع‌کنندۀ…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/19383" target="_blank">📅 22:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19382">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXM_Hg0ozq8mTY5FXXi7ThaW_gamwLfmt40NtmuDJYDtTQFD0wLxP4s-2dTczapnEXce6u4CVZsIY6R5m6duQxT03UCDe2cOCCJ16dU6T82YLLOBNtXHeBPBO2uhuYAxxpPE3Xeok-lANpRv7tHzLybPDhPqlNZefi-MwXDMs6we6LZNWukIpfTC0m3RfIVfXqevZS5IxmEu9x1pzPVJ3BobUfi_BO29L-iRteJRiCD-zWkZbsxtf_kbrC24SYiqU2EZKJ7nzh8JnC_wmSSydkmty8J0dYpbrC7d83wdYbbuB3HoCn2gwKrGR1m17p6uXUwjTtNG5F5ZPQ7-YV0cmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/19382" target="_blank">📅 22:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19381">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c8b5e1cc.mp4?token=MlQ0xAqlFT5htrM7XVyJ_v8D01_M4_7A66LUWB88sAIpnsSmcewv2qZ6xg1tvEepF3m2hMknJESLx_qH7ctwEP492VLc4WlpeeGtm-GN3jfxd5dY1VtZcRviYl8s2D63BdKNTtVluKLNlzpR_edUj-R_0A6me1GvXqMsga-Jsr_PBj2k3AqrxUfwwjTyS9khszIqiuAWSZg-8SzejTCQq8okd2jSV5zIlPEUvuAAYgSLYrtx-6OAnuNXhBVchEt4eB3jv9jESMm7Hl7GFomsKgoxbxZZ666RcME_aLLldjXsjcoy7JG9D5dztDsnnGzZut6g-rWMp1C1QNEqBoGvLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c8b5e1cc.mp4?token=MlQ0xAqlFT5htrM7XVyJ_v8D01_M4_7A66LUWB88sAIpnsSmcewv2qZ6xg1tvEepF3m2hMknJESLx_qH7ctwEP492VLc4WlpeeGtm-GN3jfxd5dY1VtZcRviYl8s2D63BdKNTtVluKLNlzpR_edUj-R_0A6me1GvXqMsga-Jsr_PBj2k3AqrxUfwwjTyS9khszIqiuAWSZg-8SzejTCQq8okd2jSV5zIlPEUvuAAYgSLYrtx-6OAnuNXhBVchEt4eB3jv9jESMm7Hl7GFomsKgoxbxZZ666RcME_aLLldjXsjcoy7JG9D5dztDsnnGzZut6g-rWMp1C1QNEqBoGvLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره لیندسی گراهام:
به نظر من، من می‌دانم او کجا قرار دارد، و فکر می‌کنم او آن بالاست و به نظر من، او ما را زیر نظر دارد. من تقریباً از این موضوع مطمئنم.</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/19381" target="_blank">📅 22:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19380">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8c4c6d69b.mp4?token=cl0uOxtCUwhKMzGMGG3Mqu2ZNaFm2Gv_JfBN7alW_faUXdD3pbni6mD90FfbORv-oYhRWjIOTDCtBc_japwDETZ-ShRbrrMXrAEC-MY5XHJ7SIwpYtU0F2nmSBm3GYMYqmXnZHoJDASwv228ROxf3K0ULNZKTf_YA8rZ5t4iF5fdufYQa2zgm1cyJH6TevhkyW-zWB4BrEBJ2tqs1BRnlyuzmkm46A5RIRZnDbA3sBN14GariIMRBorNHpKnu7I-VPzzOy3_IUbohvpgicwNbqatxsrmkGtXiTdSdKj-JZrhxe8NvNn5uxunvaHmlfbE6BfvYPMcFAIQPac5ZI8U1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8c4c6d69b.mp4?token=cl0uOxtCUwhKMzGMGG3Mqu2ZNaFm2Gv_JfBN7alW_faUXdD3pbni6mD90FfbORv-oYhRWjIOTDCtBc_japwDETZ-ShRbrrMXrAEC-MY5XHJ7SIwpYtU0F2nmSBm3GYMYqmXnZHoJDASwv228ROxf3K0ULNZKTf_YA8rZ5t4iF5fdufYQa2zgm1cyJH6TevhkyW-zWB4BrEBJ2tqs1BRnlyuzmkm46A5RIRZnDbA3sBN14GariIMRBorNHpKnu7I-VPzzOy3_IUbohvpgicwNbqatxsrmkGtXiTdSdKj-JZrhxe8NvNn5uxunvaHmlfbE6BfvYPMcFAIQPac5ZI8U1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم مصاحبه این 3 چه نکات تازه ای در بردارد.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/19380" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19379">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_25FjZX4Sq_keGxLQNOrzGXLusObcHhkkU8SgDALsoV9HPG57_oILaXb8WaLka437I6afH8wPfuZoVxRrz7dxpPZEgAzzL8rKX0tG_UwdHmj3EhPCcUWEAuruoV3BmstwfUnuhcpRYHe_MmrHkW2QRS-Nn9L41qhOF6lZ1gPEg0YY0I9iDvwQnY3hYYOdZEo4WpM_SoqFf--bVOoRPY83AHDyOCO6Fq5WFM_gVkc4_8g6pwSJ9tuBjsRmm8BVMDuu6nKTxnvkWu2OTzghWMmgEZJX0pB4CKknbbnf4wZX5axZ3pX7WN62C9SHOuLpfyRLeTC1A5VMpDr00JWKEmnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز سطح شاخص ریسک ژئوپولیتیک افت محسوسی داشته و پیش بینی می شود که رشد خوبی در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/19379" target="_blank">📅 22:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19378">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">روسیه:  «حمله اوکراین به یک کشتی ایرانی، به عنوان حمله به ایران تلقی می‌شود.»</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/19378" target="_blank">📅 21:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19377">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">غریب‌آبادی:   پیشنهاد شده با عمان در مورد یک مسیر موقت در تنگۀ هرمز مذاکره شود و اگر تفاهم شد، جایگزین مسیر شمال و جنوب در تنگه شود    عمانی‌ها گفتند مسیری را طراحی کنیم که ۵۰ درصد آن در اختیار ایران باشد و ۵۰ درصد آن در اختیار عمان. ما گفتیم این موضوع رفع‌کنندۀ…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/19377" target="_blank">📅 21:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19376">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">غریب‌آبادی:   آمریکا هردفعه وارد جنگ می‌شود ضربات سنگین‌تری می‌خورد و عقب می‌رود؛ دوباره برمی‌گردد و باز دوبرابر می‌خورد  مجری صداوسیما:   ما در این وضعیت هستیم؟ چرا دنبالش نمی‌رویم؛ ۴ ضربه بزنیم که دیگر نیاید  غریب آبادی:   کسی مانع نیروهای مسلح ما نیست،…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19376" target="_blank">📅 21:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19375">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">غریب‌آبادی:   آمریکا هردفعه وارد جنگ می‌شود ضربات سنگین‌تری می‌خورد و عقب می‌رود؛ دوباره برمی‌گردد و باز دوبرابر می‌خورد  مجری صداوسیما:   ما در این وضعیت هستیم؟ چرا دنبالش نمی‌رویم؛ ۴ ضربه بزنیم که دیگر نیاید  غریب آبادی:   کسی مانع نیروهای مسلح ما نیست،…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/19375" target="_blank">📅 20:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19374">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">غریب‌آبادی:
آمریکا هردفعه وارد جنگ می‌شود ضربات سنگین‌تری می‌خورد و عقب می‌رود؛ دوباره برمی‌گردد و باز دوبرابر می‌خورد
مجری صداوسیما:
ما در این وضعیت هستیم؟ چرا دنبالش نمی‌رویم؛ ۴ ضربه بزنیم که دیگر نیاید
غریب آبادی:
کسی مانع نیروهای مسلح ما نیست، برویم بزنیم
نباید پاسخ‌های خودمان را ضعیف تلقی کنیم.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/19374" target="_blank">📅 20:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19373">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حمله یمنی ها به یک کشتی دیگر سعودی</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/19373" target="_blank">📅 20:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19372">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کاخ سفید:  رئیس‌جمهور ترامپ جلسات خود را در دفتر بیضی شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو به پایان رساند.  هر دو جلسه مثبت و سازنده بودند!</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/19372" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19371">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">برنامه امروز دیدارهای ترامپ در کاخ سفید</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19371" target="_blank">📅 20:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19370">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">باز این پفیوزها می خواهند تندروهای داخلی را تحریک کنند تا تنگه را ببندند و قیمت نفت بالا برود و غرب از کمک بیشتر به اوکراین که خشتک روسها را بر کله شان کشیده منصرف بشود.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/19370" target="_blank">📅 20:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19369">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">باز این پفیوزها می خواهند تندروهای داخلی را تحریک کنند تا تنگه را ببندند و قیمت نفت بالا برود و غرب از کمک بیشتر به اوکراین که خشتک روسها را بر کله شان کشیده منصرف بشود.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19369" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19368">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📌
چرا سهام شرکت‌های نیمه‌رسانا سقوط کرد؟ بررسی عوامل پشت پرده اصلاح بزرگ در سهام تراشه‌ها  افت سهام نیمه‌رساناها نتیجه ترکیبی از نگرانی درباره رقابت چین، ارزش‌گذاری بالای سهام و شناسایی سود پس از رشد چشمگیر صنعت هوش مصنوعی بود.  این ریزش فعلاً بیشتر به بازتنظیم…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/19368" target="_blank">📅 18:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19367">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lk737xZkoSBvRnyG5_Jn7OzD3SqG0tG6ZLjNX50zjV0bCQIkUWCN5_5yYHJEYCo04teZY3VzzAmaUiA-0z0Hgjdfw6nmyzRe9gW91HhP-WC7gjVMjDD-AhTFv3L4SdbOFX_FgNWW_IGFHZF2qhUyoWB8u5XKETwxCsBAeyA4WTzS_gJ9zP8DY9N3RoC86Qf0L86Ln0du7KxUBT_bwzc4SSAZat3OpuSXZkb-6lA_0bXaaGsBmA_kppUtV1gHJEZxF2tUZKzoxbRmi88IcnjEQNuzLQPBbPdhZ6XqTbZHucVVtz98DZZ-KS33KFSYlgsBp77LClnbdXkPGw20hjR7ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا سهام شرکت‌های نیمه‌رسانا سقوط کرد؟ بررسی عوامل پشت پرده اصلاح بزرگ در سهام تراشه‌ها
افت سهام نیمه‌رساناها نتیجه ترکیبی از نگرانی درباره رقابت چین، ارزش‌گذاری بالای سهام و شناسایی سود پس از رشد چشمگیر صنعت هوش مصنوعی بود.
این ریزش فعلاً بیشتر به بازتنظیم انتظارات بازار شباهت دارد و تداوم آن به توان شرکت‌ها در اثبات سودآوری واقعی سرمایه‌گذاری‌های هوش مصنوعی بستگی دارد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/19367" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19366">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ادعای رسانه های روسی:
یک مقام ایرانی به ما گفت تهران قطعاً به صورت نظامی به حمله اوکراین به یک کشتی ایرانی در دریای کاسپین پاسخ خواهد داد.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/19366" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19365">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حمله دیروز یمنی ها به مبداء خط لوله شرقی-غربی عربستان یعنی تاسیسات نفتی ابقیق انجام شده.  سعودی ها کوشیده بودند با این خط لوله وابستگی خود به صادرات از تنگه هرمز را کاهش دهند که با این تشدید تنش یمنی ها روبرو شده اند.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19365" target="_blank">📅 14:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19364">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شما ببینید چقدر سرعت تحولات ژئوپولیتیکی بالا و تاثیرگذاری آن روی پارامترهای اقتصادی از جمله احساسات مصرف کننده و تولیدکننده بالاست که امروز موسسه ING در
تحلیل گزارش مثبت دیروز IFO آلمان
چنین نوشته:
Normally, three consecutive increases in the Ifo index points would be a reason to party, celebrating increasing optimism in German businesses and higher hopes for an economic rebound in the second half of the year. However, in this highly volatile geopolitical environment, even leading indicators have become rather outdated.
Today’s Ifo index reading probably reflects more the initial relief after the US-Iran Memorandum of Understanding than the recent surge in energy prices.
ترجمه:
به‌ طور معمول، سه افزایش متوالی در شاخص ایفو دلیلی برای جشن گرفتن است؛ چراکه نشانه‌ای از افزایش خوش‌بینی در کسب‌وکارهای آلمانی و امید به بهبود اقتصادی در نیمه دوم سال است. با این حال، در محیط ژئوپلیتیکی بسیار ناپایدار کنونی، حتی شاخص‌های پیشرو نیز تا حدودی از اعتبار افتاده‌اند.
ارقام امروز شاخص ایفو احتمالاً بیش‌تر بازتاب‌دهنده آرامش اولیه پس از تفاهم‌نامه آمریکا و ایران است تا افزایش اخیر قیمت‌های انرژی.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19364" target="_blank">📅 14:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19363">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">311.2 KB</div>
</div>
<a href="https://t.me/SBoxxx/19363" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 14</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/19363" target="_blank">📅 14:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19362">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وزیر دفاع اسرائیل:  در دور آخر درگیری‌ ها جنگنده‌ها و سوخت‌رسان‌های آمریکایی از اسرائیل پرواز می کردند اما ایران همه را زد جز ما</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19362" target="_blank">📅 14:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19361">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وزیر دفاع اسرائیل:
در دور آخر درگیری‌ ها جنگنده‌ها و سوخت‌رسان‌های آمریکایی از اسرائیل پرواز می کردند اما ایران همه را زد جز ما</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19361" target="_blank">📅 14:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19360">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:  ما اجازه نمی‌دهیم اردوغان سوریه را علیه ما تقویت کند. ما می‌دانیم چگونه منافع اسرائیل را دفاع کنیم.  در حال حاضر هیچ درگیری نظامی مستقیم بین اسرائیل و ترکیه وجود ندارد و ما تمایلی به ورود به چنین درگیری‌ای نداریم.  اما اردوغان…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19360" target="_blank">📅 13:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19359">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وزیر انرژی اسرائیل، الی کوهن: ما دخالت‌های ترکیه در سوریه را نخواهیم پذیرفت.
🔹
اگر ترکیه پایگاه‌هایی در سوریه ایجاد کند، ما نیز اقدام خواهیم کرد تا پایگاه‌هایی را در داخل خود سوریه ایجاد کنیم</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19359" target="_blank">📅 13:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19358">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وزیر امور دیاسپورای اسرائیل، آمیخای چیکلی:  «ترکیه اردوغان و سوریه الشرع اکنون بسیار نگران‌کننده‌تر از ایران هستند.  دوران امپراتوری شیعه ایران به پایان رسیده است. محور جدید، محور اخوان المسلمین ترکیه، سوریه و قطر است».</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19358" target="_blank">📅 13:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19357">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وزیر انرژی اسرائیل، الی کوهن: ما دخالت‌های ترکیه در سوریه را نخواهیم پذیرفت.
🔹
اگر ترکیه پایگاه‌هایی در سوریه ایجاد کند، ما نیز اقدام خواهیم کرد تا پایگاه‌هایی را در داخل خود سوریه ایجاد کنیم</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/19357" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19356">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 14</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19356" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 14
سه شنبه 28 جولای 2026</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SBoxxx/19356" target="_blank">📅 12:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19355">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">برنامه امروز دیدارهای ترامپ در کاخ سفید</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/19355" target="_blank">📅 12:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19354">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رویترز: در پیشنهاد عمان، تهران کنترل انحصاری تنگه هرمز را در اختیار نخواهد داشت
خبرگزاری رویترز به نقل از یک منبع آگاه گزارش داد عمان پیشنهادی را به جمهوری اسلامی ارائه کرده است که بر اساس آن، سازوکاری مشترک میان کشورهای منطقه برای مدیریت تنگه هرمز، با دریافت کارمزدهای داوطلبانه، ایجاد شود. بر پایه این پیشنهاد، جمهوری اسلامی کنترل انحصاری این آبراه راهبردی را در اختیار نخواهد داشت.
پیشنهاد عمان از حمایت کشورهای منطقه برخوردار است و بر اساس الگوی تنگه مالاکا تدوین شده است؛ الگویی که در آن استفاده‌کنندگان از آبراه به صورت داوطلبانه در تامین هزینه‌های ناوبری، حفاظت از محیط زیست و عملیات جست‌وجو و نجات مشارکت مالی می‌کنند.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/19354" target="_blank">📅 12:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19353">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwWNf1CyvHHBCVVlWta7EhnPCtGh1NSZqFPius_pmC4mmV4Xm1vx-mt4TukPIzNAE_sFI9gLQMWiXNeKa842aOimPCg2NEUfOymtNbLQHvVvOm0_PKV4OO_lYEhvV2lo5WxVpwNlpeXl1CLLeFvRmIduPmr-Cilk6kcRG07Dw04QaM4-YriLygNZ7yjTfgdOP63dHvc_jeOwKzC2H_vTPZE72PUurGnJfI_Xxa6H2w5pYdgzcgSExyn46huJmd7cPPP1Gl6obq6Ky7pVymCYsny8YrHw5dNVMdAOgX7fKC2NrA0l7mxYDjFaylHG3B5nuYIuxX34LbysL5yuU4Fy_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخریب تأسیسات گاز پارس جنوبی عمق بحران ناترازی انرژی در ایران را چند برابر کرده است!
خروج ناگهانی ۲۳۰ میلیون متر مکعب از ظرفیت تولید روزانه گاز، شوک شدیدی به رگ‌های حیاتی اقتصاد و رفاه عمومی وارد آورده است. این رخداد، ناترازی مزمن گاز را از یک چالش مدیریتی و ساختاری به یک بحران ملی و اضطراری تبدیل کرده و پیامدهای این ویرانی به سرعت در دو جبهه حیاتی خود را نشان خواهدداد: سفره و آسایش مردم در بخش گاز شهری، و شریان‌های اقتصادی در بخش صنایع سنگین مانند فولاد.
سقوط مصرف در بخش گاز شهری
گاز شهری خط قرمز دولت‌ها برای حفظ رضایت عمومی است. با این حال، کسر بخش بزرگی از تولید، پایداری شبکه توزیع را در شهرهای بزرگ و مناطق سردسیر به لرزه درآورده است. افت فشار شدید در شبکه‌های خانگی، قطع پراکنده گاز در نقاط انتهایی شبکه و لزوم جیره‌بندی پنهان انرژی، نخستین پیامدهای ملموس این بحران هستند.
دولت برای جلوگیری از خاموشی مطلق خانه‌ها، مجبور به کاهش ارسال گاز به نیروگاه‌ها خواهدشد. این تغییر مسیر، نیروگاه‌ها را به سمت سوزاندن مازوت و گازوئیل سوق می‌دهد. نتیجه این زنجیره، تشدید آلودگی هوا در کلان‌شهرها و به خطر افتادن سلامت عمومی است. به عبارتی، شهروندان هزینه این تخریب را یا با سرمای خانه‌ها یا با استنشاق هوای آلوده و یا هر دو پرداخت می‌کنند.
فلج شدن صنعت فولاد و زنجیره‌های تولید
بخش عمده‌ای از بار سنگین این کسری به دوش بخش مولد اقتصاد، به‌ویژه صنعت فولاد، افتاده است. تولید فولاد در ایران به شدت وابسته به فرآیند احیای مستقیم و مصرف گاز طبیعی به عنوان ماده اولیه و سوخت است. قطع یا محدودیت شدید گاز صنایع به معنای توقف کوره‌ها و کاهش چشمگیر حجم تولید است.
کاهش درآمد و صادرات
افت تولید فولاد، ارزآوری کشور را کاهش داده و ارز غیرنفتی را محدود می‌کند.
کاهش سود کارخانه‌ه:
توقف خطوط تولید، هزینه‌های ثابت را بالا برده و سودآوری شرکت‌های بورسی را کاهش می‌دهد.
بحران در صنایع وابسته
کمبود فولاد خام، صنایع خودروسازی، ساختمان‌سازی و لوازم خانگی را نیز با جهش قیمت مواجه می‌کند.
سرایت بحران به سیمان و پتروشیمی
علاوه بر فولاد، صنایع سیمان و پتروشیمی نیز در صف نخست آسیب قرار دارند. پتروشیمی‌ها که گاز را به عنوان خوراک مصرف می‌کنند، با توقف تولید و فسخ قراردادهای صادراتی روبرو شده‌اند. کارخانه‌های سیمان نیز با قطع گاز به سمت مازوت‌سوزی رفته‌ و خواهندرفت که هزینه‌های حمل‌ونقل و تولید آن‌ها را به شدت افزایش داده و قیمت نهایی ساخت‌وساز را بالا می‌برد.
نتیجه‌گیری
تخریب‌های ناشی از جنگ، ساختار آسیب‌پذیر انرژی ایران را با چالشی بی‌سابقه روبرو کرده است. جبران ۱۰۰ میلیون متر مکعب از این ظرفیت در ماه‌های آینده، تنها یک مُسکن موقت است. تا زمانی که زیرساخت‌ها به طور کامل بازسازی نشوند و سرمایه‌گذاری کلان در بهینه‌سازی مصرف رخ ندهد، ناترازی گاز مانند سایه‌ای سنگین بر سر رفاه خانگی و رشد صنعتی کشور باقی خواهد ماند.</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/SBoxxx/19353" target="_blank">📅 12:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19352">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wj4j7PBzUf6NTfaLWeAm1L7hmXalqnTHqyz2fzyGQFJ5xf1Wyr5rnEcWxd1mD-5wMiGuZXOmDkHI8VCh9HMB8Nr49Zy3NHySq0R8l-WbBzWFaBDovQHMCQ-jX2XEmDlpxbU_I7NZWxaN6OAcxI-XdIZ00ze22ipyPpIxllQofKRU4m_mXVgAdnWSdRLFCwihbtiyvlFCN6tJIcPLS3EkODGSPUd09aTLNfXNwEOIXUCbvxX79vys02VUWTsKgDBqHR-9Y2RqsIiTQwtKeebxuHELuKY7qb1KwqwYEXH6On1Z8YTb3NDIw4VU9SfYvG7C_1tlhFYXXxWSHJbwUNKFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز سطح شاخص ریسک ژئوپولیتیک افت محسوسی داشته و پیش بینی می شود که رشد خوبی در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/19352" target="_blank">📅 11:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19351">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYvdpj0JEpmZ70ckyV6gjAwsTBPc2HzWTKOw6lxouOHbR3H02DJ9njFknphfvaXPhSE898RlXcC6OMzJO2pT3mGv9LEjFZSp6gATo_qKZjTkOlFQne4kQlJyol05B8GIhKUVptHlc5-bbN-vimGqgNfkWP8yaTIvlBumsdQCqLzJFBBVwZviC-MhKnINu7TQA9eK_GRiURZay2nz6Vny2kRxDV0sYbB9WsYUcjUFW7EvlBBMsJcDmLNcDy1XmsookFdkwcM-i7laRvOc1u7Witw9P4qOUS_QF9ZYfvpFIw293yxTI6f0wxh2zHR2cvSc0G63podTkMsO0_5vPfQf9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا زلنسکی هم به آمریکا همزمان با نتانیاهو سفر خواهدکرد تا دیدار مشترکی با ترامپ داشته باشند!</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/19351" target="_blank">📅 11:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19350">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c9893728.mp4?token=TDHbWG3F1BJehqzOOfAGPvgAQTKGnzWx3YaEDsga8iB2Mso8qQ_DbC4HirD3On7BBac28CNgudX3np6fUW11LGkVRD78GGt7Q0BV20DWC91BXKG_6F9ymy7vJkulABDaQUTpq7FCwfnZH4ZdGM-80G9u7p-9iXAqbw_SN-QQTcqltfWt7CsBWnqI2xMPJ5k0fQoatauJlUJ4_40b1j3K30yJNU5EbEyRBkek_-tl2qEusXomSDwdRctPHR9NWxlM9IE2AjCOv9so_w7mvKM7NzWeeIq_WOWQrrUezXEt_jAScoLnas3_OfnWltvDxjJLEFhUCk_sDH7Ty-4YAWjDpYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c9893728.mp4?token=TDHbWG3F1BJehqzOOfAGPvgAQTKGnzWx3YaEDsga8iB2Mso8qQ_DbC4HirD3On7BBac28CNgudX3np6fUW11LGkVRD78GGt7Q0BV20DWC91BXKG_6F9ymy7vJkulABDaQUTpq7FCwfnZH4ZdGM-80G9u7p-9iXAqbw_SN-QQTcqltfWt7CsBWnqI2xMPJ5k0fQoatauJlUJ4_40b1j3K30yJNU5EbEyRBkek_-tl2qEusXomSDwdRctPHR9NWxlM9IE2AjCOv9so_w7mvKM7NzWeeIq_WOWQrrUezXEt_jAScoLnas3_OfnWltvDxjJLEFhUCk_sDH7Ty-4YAWjDpYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسائه ادب فرج الله دباغ — اوباش فراری معروف به سروش — به ساحت استاد موسی غنی نژاد</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/19350" target="_blank">📅 11:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19349">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6wpbmlqUl8kjA-HGqtjLbGAJkjpLdlLM0Vsn2ZMEEdj0X4HphilJQpbJF36Sk-rwlSY3jQRgwPEvNW8Ew4lRzeIqdhyLlt9iRRYJV1k2mLX0uHl1bhI80zia1XQ7qW4jDUuJbBS2rfXvW4xgb_NmQIAJ0aOjfohA0s7TbKqGvl-8lNBIxtp6GQyi9iPKk1bjzqk6KzVfsKvX8y6ZPMiZYCwnxaIg2D7WZN890yvcnWAfVLXhCIyjJQAZ_VvFGP_tMGABV5HwUuuyEl2UTjFLtk5AdJRm3StlL7AKS_bv0pHyOO_58IxEgFQPbv-8f6EVQefs46hCGNLGXg9mGj1fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسائه ادب فرج الله دباغ — اوباش فراری معروف به سروش — به ساحت استاد موسی غنی نژاد</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19349" target="_blank">📅 11:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19348">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKaibZ3dW5cNSj5efbJC1Bc2xzhxCeE0GcdCAnqj5eIESNNYD8pJTWkLFSqu4tuJmxgK71JI5waMYjZPG6PK6q30exnUNWAM0dUVFI4VCtIkd20rDUrNBXJiFcIegUQpF38-3eUMN3_p4U_NJXreUdKrgdzFI_Q6AWAGMwXHftW2zMgjEC_hHh8jP--B13D6AB8RN5Jx0hVdB7f5JGnJwgHsGMTI5jlcsvMh5abcqx6FLQOo4UjJx-yJxUJzovUkY5te7UsAOWeyxSrjIdfjRql7Z6Bc8rAiJ3YRnOfp3VWXfo_1h4_Gff4vI8nfjC7HXQPkztb6QP4IadkeGz_u_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله دیروز یمنی ها به مبداء خط لوله شرقی-غربی عربستان یعنی تاسیسات نفتی ابقیق انجام شده.
سعودی ها کوشیده بودند با این خط لوله وابستگی خود به صادرات از تنگه هرمز را کاهش دهند که با این تشدید تنش یمنی ها روبرو شده اند.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19348" target="_blank">📅 11:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19347">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ:
ایران می‌گوید: "لطفاً، لطفاً،  محاصره دریایی را بردارید."</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19347" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19346">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBph2B3DHYPXKicU2s1k6u4wHXEs4J13ktdefu_hgbZrtbwk9_BWfSDmNu0B6oM3gpbtKuqasY370mLor3hEMvy22k_3Pz4hLbbhSBirE4DzZNLML3liXr08GR0qgatL2VcVib39y-S_Im22p4nGuFDD_CxmiN9jBhCrRuROHxLWJ7c2hjpQ_AMdq1kSUyafyeC37-kfTzv_T_BfdksVDIE7PsCNvcDfqh53tuwRFWLlgE_UzJcMbzW_bkks4EIpXkSFpGPrxGUe1TLPAjTnuloeQE604JnXCB4uOhSGYBWc0jdshgbhKE6XONgJT-nh8qhN6QeAd1gOE6E6cyIuZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه محموله جدیدی از موشک‌های کورنت و پرتابگرهای کنترل از راه دور به یگان‌های خط مقدم تحویل داد.
این سامانه پیش‌تر علیه تانک‌های لئوپارد و چلنجر، خودروهای زرهی بردلی، استحکامات و مراکز فرماندهی استفاده شده است. تجهیزات پرتاب جدید به خدمه اجازه می‌دهد در فاصله از پرتابگر و در پناهگاه شلیک کنند.
شرکت روستک اعلام کرد کورنت هزاران هدف را در نبرد منهدم کرده است.
موشک کورنت-ای‌ام با کلاهک سنگین با قابلیت نفوذ ۱۱۰۰ تا ۱۳۰۰ میلی‌متر زره همگن نوردیده پس از زره واکنشی، تهدیدی برای تانک‌های مدرن است. هدایت لیزری آن در برابر اختلالات الکترونیکی و نوری مقاوم است. پرتابگرهای خودکار می‌توانند اهداف را پس از قفل ردیابی کنند. برد این سامانه علیه اهداف زرهی تا ۸ کیلومتر و با موشک‌های انفجاری تا ۱۰ کیلومتر است.
تجهیزات کنترل از راه دور خطر قرارگیری خدمه در معرض آتش متقابل، توپخانه و پهپادهای اف‌پی‌وی را کاهش می‌دهد. این سامانه روی خودروها، خودروهای سبک، چهارچرخ‌ها و سکوهای رباتیک نصب می‌شود</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19346" target="_blank">📅 04:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19345">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بر اساس بیانیه فرماندهی مرکزی ایالات متحده، از زمان اعمال مجدد محاصره کشتی‌ها به بنادر ایران، دو فروند کشتی برای اطمینان از رعایت قوانین از کار افتاده، دو فروند کشتی بازرسی شده و ۱۷ فروند کشتی تغییر مسیر داده‌اند</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19345" target="_blank">📅 03:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19344">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رسانه‌های محلی گزارش می‌دهند که شماری از پهپادها، احتمالاً ساخت ایران یا تحت حمایت ایران، در اربیل عراق و مناطق اطراف آن رهگیری شده‌اند. هم‌زمان، سامانه‌های ضد راکت، توپخانه و خمپاره در اربیل فعال شده‌اند</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19344" target="_blank">📅 01:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19343">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbrE82F-RJfoVaz_3WvkaKBtUdCNUM2DZKV6PHPRn-fC6Z_AjdgWbCxlcv_NMq8tBdw7NONIjBaTqkF-UUQOl1UwutoB9G9qmf7ORj9I5NgHJSvhdN8O-PkMzJePJXRDiCPP9q1ZQy1ogiY4f-MtXrGzKVzouMpIThGykzV5TopjwCG_9RGjEBZKGI8d7JWVLki-Ru_pkYyJD_ZINAJgwMgktWViRKQ8MBtOuRA552ORolZq5DyDGVYY5wkfIHknDa8r16GJsFfXkheOOdsLE4Z7FvxZuK4ScSJX9u5e2AuNMMHLpuW9yV-skQpB6THvfcJMRkllkKW__Nbnx5Lb9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک بالستیک Lora در خدمت ارتش یونان!  به زودی، نیروهای مسلح یونان به موشک‌های بالستیک هدایت‌شونده دقیق لورا از اسرائیل مجهز خواهند شد. این موشک‌های بالستیک نه تنها توسط نیروی هوایی یونان بلکه توسط نیروهای زمینی این کشور در سراسر جزایر اژه و مدیترانه یونان…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19343" target="_blank">📅 00:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19342">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عمده خاک اوکراین در برد موشکهای ایرانی قرار داد</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19342" target="_blank">📅 00:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19341">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یادداشتی خواندنی از یورونیوز درباره ایزنکوت و حزب ش.  لینک</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19341" target="_blank">📅 00:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19340">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76775f04b.mp4?token=UfNJdVf1nNrvqvOLw--9UrsrRUuO7SqvqrVySL5gX5jmf9Ne84LcdU_D3sqbTq6cJYPIENn6c67sVBHf0AZCEJf5Yo_opbw58kJRdXS9NC02k4AiNI8qjMslAGToZmAOjqxIg6XXr3dlqoyhM0uV9AXnRyzoufIuNYLyvZ7aSDvf_AAsdOKq5l-B6iRHglLf7tFZCDtQxZy2EppQ9i-q1UmFSioLhxhrMD4mO3Ltmb4sCLVeX4NZllsj76-9Zc9LCJfwT0uCymLWbj76h8Q0hbeamxN5BKA3IKFGubxOC9Otyn5-loIiWpz8tXLl-ZaSg7nsP5qGoYVk8mT2e6nH1kd_tiI3tE0puueEjMCr36tkyQc1eesePvQlawGZjNd5MBOf0z_sGacPQhCO3EULfDhHthwjEZX2jtv-XA7bRfb5NtddzxVuUgKHVf72cNQg_QUjYxzEgMUKNQN47cxIYBno2SVJHntwn77tEc-4F88A44I5FAvznYRSj8vG-haJrBQsl-Hs_4ImN-xS0sPtULLDDa0X_Ue_CxgnJNhDdhk5ZJhy-XsMa0WZTDx1_P0q94_hz6D6gPT0LzSXnD3pdoLSrCJsZAyECKaeQYEM1pqOYbKznYc-FVGgjW_35ZEMVk15916pEW2DXr_M5gubBa06c3kpIgs_XvWWv5CAwh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76775f04b.mp4?token=UfNJdVf1nNrvqvOLw--9UrsrRUuO7SqvqrVySL5gX5jmf9Ne84LcdU_D3sqbTq6cJYPIENn6c67sVBHf0AZCEJf5Yo_opbw58kJRdXS9NC02k4AiNI8qjMslAGToZmAOjqxIg6XXr3dlqoyhM0uV9AXnRyzoufIuNYLyvZ7aSDvf_AAsdOKq5l-B6iRHglLf7tFZCDtQxZy2EppQ9i-q1UmFSioLhxhrMD4mO3Ltmb4sCLVeX4NZllsj76-9Zc9LCJfwT0uCymLWbj76h8Q0hbeamxN5BKA3IKFGubxOC9Otyn5-loIiWpz8tXLl-ZaSg7nsP5qGoYVk8mT2e6nH1kd_tiI3tE0puueEjMCr36tkyQc1eesePvQlawGZjNd5MBOf0z_sGacPQhCO3EULfDhHthwjEZX2jtv-XA7bRfb5NtddzxVuUgKHVf72cNQg_QUjYxzEgMUKNQN47cxIYBno2SVJHntwn77tEc-4F88A44I5FAvznYRSj8vG-haJrBQsl-Hs_4ImN-xS0sPtULLDDa0X_Ue_CxgnJNhDdhk5ZJhy-XsMa0WZTDx1_P0q94_hz6D6gPT0LzSXnD3pdoLSrCJsZAyECKaeQYEM1pqOYbKznYc-FVGgjW_35ZEMVk15916pEW2DXr_M5gubBa06c3kpIgs_XvWWv5CAwh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راه حل قطعی پایان جنگ پیدا شد!
استراتژیست نابغه ایرانی — مستر قرهی — موفق شدند با استعانت از خدای تبارک و تعالی و نیز هوش خدادادی و سرشار خود راهکاری فوری برای تسلیم آمریکا و کله زرد ریقو پیدا کنند:
سرش (سر فضاپیما) را کج کنیم تا بخورد به آمریکا و مردم آمریکا ضد ترامپ شورش کنند!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19340" target="_blank">📅 23:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19339">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_ovGZQ_Qhjh57UM8QDcfLS3phtmQ8tFIQq-aJ2wd6ietp5c9o4ZshUg7Jt7KsktSd_5Y6unUVnp2i4g5GIReOJny7Mben5u3P92gqVdw9-7cS-DVR-FBNVjvpKPtUqg1LNSyKzkhSiBuu-qGZcFR7u6psgGQ_YoRtfqT1K8J5fgpxhyiWtgnozoB0DqAOSaY9Z1Mf24eVzAf2v_lgIg5J-Gxect3mp0FmpS-9Ja6_I55n4Bmspy7uDwkGJF4eBHv0Di3ykv24yoM8YNaVCGesnpjn7SwuhgHNrDNpDqsNu5I4GN8FcpCsxAitwJPl0BUpt0T2v2I3z44TNUJ76oZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19339" target="_blank">📅 20:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19338">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اظهارات ترامپ درباره ترکیه:  ترکیه علاقه‌ای چندانی به اسرائیل و بنیامین نتانیاهو ندارد اما ترکیه برای من بسیار ارزشمند بوده است.  به هر حال، ترکیه یک کشور بسیار قدرتمند است. فوق‌العاده و با یک ارتش بسیار بزرگ.  ارتش آن‌ها تجهیزات بسیار خوبی دارد.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19338" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19337">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دقیقاً طبق تحلیلی که ارائه شد آمریکایی ها نخستین پس گردنی را به اردوغان زدند و علیرغم همه وعده های ترامپ، گویا تحویل جنگنده های اف-35 به ترکیه متوقف شده است.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19337" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19336">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-ZyJeMbwU1ArV5-tmZJGLUIPWU9nNt8qD2RnzVoib06tylRkK8lPkxtIomQQbGXp1Ycb--_Il5HCA7umBXNHIdExLUHjxYkHN560QU6b65zB-30NPsugKDvIzlG8lmDGVqbNZ7ADf6J1P6gL-VDl7HiY6dDe2q6g1bzzZhDTijI5qL72am3hP4baO87FVfna7RWC_L-IYneq8kWLGlGl1STLFWrcFfK8PlL3kz0FN6Q6cFAsJa_EDetrpStb7lFNQqAj8Aa0Lj7FYG69vnvp_K14kU8mIAPt-ooQwzcV3wq-hWk5lt_0kyXVAJT4oHVoxSdtJtgObKGBzMCvPajmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19336" target="_blank">📅 20:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19335">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پدرسگ ما خودمان دزدهایی داریم 100 درجه بهتر از تو.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19335" target="_blank">📅 20:16 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
