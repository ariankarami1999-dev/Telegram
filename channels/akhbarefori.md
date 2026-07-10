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
<img src="https://cdn4.telesco.pe/file/Uey9xI1TvSn_7vJSN913eJJ37MSYbhL6W4N8-K6MJAGj0dyzsCs_Z6YgSEJvslBSaJFnw-QJg9x-ayAWWR-hwsPnz_wR2-r_dc-5OgJdR6-DjygIUUu1hTXCj4NsiXmXU6Eporc059gLDmOSKVYAOWDNgx2EUJqgS_dH9nF9e2p02eUXxWTDMpOl3qSd52OI9HsUoSzB6Fev9NZRba8ugLw0wsx9ZPzqkMQyNMdXvAz8B7GnunTTZ7LGwj3SFftjfRQh9Ime4SDTvIz_rNp8ZQ0CrmaM8NPB4LFYkwTc1kjb7klZ5TzOjy8XkkRuCPKcX6FAfMNgj-iXRERpMZHTEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.47M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 10:29:07</div>
<hr>

<div class="tg-post" id="msg-669396">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQjbdCG4fXNNoCfwzjoeyLX091gcpW9P_MTsLQ40OagNtdIysALVK9lZ4FYP81y0r27tHOZghh7CIuhLV8bsX6GUZHhKAxz9oGng3XGRyFekMU9bSOsGFn9aVpx2Qu3mFidTSuS-NwAhh_ohXyhc4l1Xn2i6vh8IavuEJhKFmd6vov94oUn5aETjcjKgpm9kN8IUc-locwZcktRW2eQl_wjRiHbIcPYrE0fGOTBqlh6xoOPbEOwEXVtfzw2jTBNo0uLYyBKPCUTzrntBHF6oclZ-DdrT0GN0NeZNLgnxcKfFnENbp2dQEsdxiYLnLSnrd3_v5jPj622KnvbcOiw_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آماده روزهای داغ باشید!
🔹
بر اساس اعلام سازمان هواشناسی، از
۱۹ تا ۲۵ تیر
با استقرار الگوی تابستانه، دمای هوا در بخش‌های گسترده‌ای از کشور افزایش می‌یابد و هوای گرم تداوم خواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/akhbarefori/669396" target="_blank">📅 10:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669395">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnTTXNcA97ke-2WUs1yzrhhYI1dtciqX2Am0eDN-K3z-w7hZMBJYdFr-X2oUln_2Fj6WirAWhxAvKDti1RfzWP0RhT7XKe81QC-W5iUrWT47ZAd1y4f3kQKYzaryTnEWC3bKcAOLk4iwyEbIsmeY2vMqUo50Ifi6IsfgG1gr43mNth-ohDexFP4DWCNt4Hmf3AOHvk1EtZEnviXvdKMJEWKClTba-_z3pwDyuc2hnR-flEbEL0f--L35ugfQC-r0pxqin-35bvzUoIL2nSuMl9c16K327hEEUNFdPhykSm8DTvta3v24D8fmnUXCh_mDA5XLM0A_eNExnBT6yjhzmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سریع‌ترین عنکبوت جهان با سرعت ۱۳ کیلومتربرساعت شناسایی شد
🔹
دانشمندان با مطالعه ۲۵۸ گونه، سریع‌ترین عنکبوت جهان را در کوئینزلند استرالیا شناسایی کردند.
🔹
این عنکبوت شکارچی با سرعت ۳٫۶ متربرثانیه (۱۳ کیلومتربرساعت) می‌دود که از سرعت پیاده‌روی سریع انسان هم بیشتر است. پژوهش نشان داد که سرعت بالا نه به باریکی پاها، بلکه به بلندی پاها، جثه بزرگ‌تر و نیاز به شکار مربوط است./ دیجیاتو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/669395" target="_blank">📅 10:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669394">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qM0gXURTTbRl6-BPqeW7fOrFK9BPeXbl0KH7bUHIIf0-qFYvLqqx2Y8mvdjYqUZmdeZFj50UISbUnbMkTE1et0nPROmbL0XaW2lb502mC33MezZoVJagf3HdozyldIZk1rZ16V6nY4n0gVwSME2ukA9BIYp10IztbUwLxt0rGVNbhYyQGCHBjkvy2k_WsVBFG2ZEBqOe40tSkSCddUhSQ9XpUC0rpHQK6UUasexewkLyyWWu2M7Rw0WRf455sZmvJcLoC1gxMQbn3CkhUDTpLt4UT-x1txzNC5zDfgsO6wIEXmr55x3xwUxAV1hybpI0brwMMRrPnwgaxyezmZRMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از دماوند زیبا، امروز صبح
🔹
عکاس: مجید قهرودی
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/669394" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669393">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iy4grax6IgLCDSz_GujHEYjqnFRWbbyvzkY3HercSK7c9LoQnJydrv2ITOBSLJHumZXtjVtAQdAMBwzpNjSMgxu2TFqGqd-7F_YCMngE-ayZ_S5HEGMzySdR245dD90uNrnPNwg-_CZ9oWSTktX4TMShDgmz5i0P7aMLlhbbRuQ_c2CH7gFEKrkEeMkps2DBtbDaXn8-r1Q6mv8rcJBqeynfzY7Z3M9PRCVLvPZ_VWBzAmhzPt0y0ESOKhV1RQgZRSGioE5WpiWmVpUl57diam_ijk45rpr-IYvnT4EhJ1NHNsd3a2Ia_v6IIsbPMDtjLy0dz40hkfNwWOARkTV3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت ۷۶ دلار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/669393" target="_blank">📅 10:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669392">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
فرمانده کل ارتش: راه رهبر شهید انقلاب با عزم و اراده این ملت همچنان جاری خواهد ماند
سرلشکر حاتمی:
🔹
راه رهبر شهید انقلاب با عزم ملت، بر پایه حق، عدالت و مقاومت، پایدار و شکست‌ناپذیر است. ایران مانند گذشته، از سختی‌ها قوی‌تر بیرون می‌آید و با تلاش بیشتر، آرمان‌های عزت، استقلال و ایستادگی را تحقق می‌بخشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/669392" target="_blank">📅 10:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669391">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/669391" target="_blank">📅 09:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669387">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qhPTkZ2KP7_sYGLphO8YewJ4FPwEgTvgYXe-UIGY5FybTRkWqbPI8ygrpVdBah1Zdr04GIeFeisdBZ_H7NjgJfZRlvsEnNMPScllKfAzERXpv9RbTlSBxmWbcJ742uNkXXK0K0Dm7Ro6Qzg_LUEK6b5l1Z2iIRQUsjqByTD0Rq_D8JUcxUKrSWl0DufGvzDMUEEbSMxWlBFIqynqiMDWA3qHmNRgin4yyFzZbffSq0OcQxld4XvKb_6wbQo-7rt4U0rnZy0oTpBqWQ8wMnvQjHSNS6b96w5r-zSTEuTEDWufWpuQum2ZEeJsDE1UHWESiVhYqPz9pck6TY6fhPgdcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKmneAMAsbfTR4DOCvkpVj52GlyfnBEZ9VMe-lt2RBx4gmAGjtqkDBqYdPQMyBDIv9yG76V-zlY_QDQSvCRRW6bcGbNYlb4EFmwU9bbmsfoqzgdEAoY42XH-NjzGkWMmr2avUZEUkJaMgaG6xD5MnJfmKZxbwKQSdpDjf0M4S2hGNCGhJl3I3k5gXX1YEfZr0kFZHkpj0s9KTBcTnqVRCNGdKQ7Rc20y8I_s4jFBdibxieJbtaas_Lz6ruteXJkwuF6vdPi_LSRijHpEJB1S2tW_6LA59MdSckrwEUik94Lnz7UJ9u70n3t_-0tG3yUXy9TDdVNbMifCRhbFphpRMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5988ad7731.mp4?token=FdIwKi21DnIOzB-A3mJKzcaNEgr63_oQWR3QGLVlavdBBQzRvMWs760_yazasTBIjopJGNmwToRUS30rEp0HzqzAqWHqAnFYNQ4EE7zjX-2scdeQPfsMyY4zfYO77ZqF8fUa0v7FKZdlddWXo8nzXYtf8QLkwIzPqUpDihXxq7XT0JRT_nN68i8u43-B8BotEx_FdipowHP5_EZs05FP2Nj1lW-8y2PfQi9V8QVLx6w0m7_kqwtyQmBzvoJXltVwf7hsDdsglwypoo6uIx26xs-CXjU-v0nzXSm8vPLkrFmD_KfYvfI4e9rEjxNYzpBQ41QF16f0ot1nCIrAfG665w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5988ad7731.mp4?token=FdIwKi21DnIOzB-A3mJKzcaNEgr63_oQWR3QGLVlavdBBQzRvMWs760_yazasTBIjopJGNmwToRUS30rEp0HzqzAqWHqAnFYNQ4EE7zjX-2scdeQPfsMyY4zfYO77ZqF8fUa0v7FKZdlddWXo8nzXYtf8QLkwIzPqUpDihXxq7XT0JRT_nN68i8u43-B8BotEx_FdipowHP5_EZs05FP2Nj1lW-8y2PfQi9V8QVLx6w0m7_kqwtyQmBzvoJXltVwf7hsDdsglwypoo6uIx26xs-CXjU-v0nzXSm8vPLkrFmD_KfYvfI4e9rEjxNYzpBQ41QF16f0ot1nCIrAfG665w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برگزاری مراسم روضه و سینه‌زنی برای رهبر مسلمانان جهان در برلین آلمان
اخبار مربوط به آلمان را از اینجا دنبال کنید
👇
@AkhbareFori_DE</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/669387" target="_blank">📅 09:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669386">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فردا شنبه ۲۰ تیر، کالابرگ سرپرست خانوارهای با کد ملی ۳، ۴، ۵ و ۶ شارژ می‌شود.
🔹
فردا، آخرین مهلت ثبت نمرات دانش‌آموزان پایه نهم است.
🔹
هشدار افزایش خطرناک UV: گرم‌ترین روزهای سال در راه هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/669386" target="_blank">📅 09:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669385">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzxKO9UM4b7jKDr9g2KDIC2Mlh5bWXi7aIrEi-6JNvj-VAf9JuDyMC4AypDCDATW0vxFr2jbfh9KGwQJLfvs0ise555qFpwed3ODA7w3m8pnvJoOhxV6AUol0BUHArhaoNkmDVEdkqnRcGz2Mdy7vEXrGR77y_PXeCsuFQeYIkEctp8WwIZHfHo0dBnGJqyXlQ9BC7h_3BFJm0x5U_fluzMoVXUnucumD_h6AMIRK2tqzOF4aj2OUxneYc-oUcnjW_C0dd5WcZEQcjwW90uKNi7oLIC15OwzZcNtcHlvIMKv6qoKv3kq2oRAYWVlIFLlqJ24QSKr4Mu8L9NxtmTYdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرور سریع مهم‌ترین اتفاقات فناوری در ایران وجهان #نبض_تکنولوژی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/669385" target="_blank">📅 09:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669384">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
شبکه‌های اجتماعی؛ آزمایشگاه هویتی نسل Z
چرا کامنت و آنفالو برایشان مهم است؟
سعیدی،روانشناس:
🔹
نسل Z (متولد ۱۳۸۰–۱۳۹۵) و آلفا (۱۳۹۶ به‌بعد) از نظر سن مواجهه با دیجیتال تفاوت اساسی دارند؛ آلفا از پیش‌دبستانی وارد فضای مجازی می‌شود.
🔹
برای نسل Z اما، کنش‌های کوچکی مثل سین‌نشدن پیام، حذف از گروه، تأخیر در پاسخ یا آنفالو، بار عاطفی واقعی دارد و شبکه‌های اجتماعی به آزمایشگاه هویت آن‌ها تبدیل شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/669384" target="_blank">📅 09:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669383">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/968ccb3c3e.mp4?token=c0Q7rc_6D7aJz1yYKmYVMc0lRKSSOQsqi53T4_sb7z0OOoy94_13FvfRaUebJ8MmEB3dajjI6vUNK_mQU7Eon0zRx51LPvvcnpsIg_lpa_K3E9bvMyo7PoYvQs1yed2qKBOBwBVWXzEqP6aJ8yf8bCqMifxCEiorvlqvR-dpnULtJLomMjghB5dUR3jmTazbM09aaODx1Qphq9j5oF0C0p4R0ecrXfwkkwW5KL3SK1ZIm__wL5yQrA2PCcUiErJATahGMQQg-NQIGPmnaGenFJ8u9MQX3VGRoak-EMkiJFqPZoDWdPLNl7_Jo0J_M9NVtFbUacsoiBUaqn4g0PwtoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/968ccb3c3e.mp4?token=c0Q7rc_6D7aJz1yYKmYVMc0lRKSSOQsqi53T4_sb7z0OOoy94_13FvfRaUebJ8MmEB3dajjI6vUNK_mQU7Eon0zRx51LPvvcnpsIg_lpa_K3E9bvMyo7PoYvQs1yed2qKBOBwBVWXzEqP6aJ8yf8bCqMifxCEiorvlqvR-dpnULtJLomMjghB5dUR3jmTazbM09aaODx1Qphq9j5oF0C0p4R0ecrXfwkkwW5KL3SK1ZIm__wL5yQrA2PCcUiErJATahGMQQg-NQIGPmnaGenFJ8u9MQX3VGRoak-EMkiJFqPZoDWdPLNl7_Jo0J_M9NVtFbUacsoiBUaqn4g0PwtoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات مجری مطرح فاکس‌نیوز علیه ویتکاف و کوشنر؛ آنها آدم توافق با ایران نیستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/669383" target="_blank">📅 08:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669379">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8dff0e95.mp4?token=Wz8dHAjj9m_m9JgnHLZq5wXeWk67t1CgKpFPvXjMiKpYPzOYI1DnLd-NfehGhECWPMHfkz39_dQKS9DLpyzq30t30lID-YpppNwFWEOPvwppDsf3PHAR6LZVIEmV641dmjKkgH4HWoJgY2c4MOuVgBmACpqHGuvHNuroXXf2w2lyQlMdOCXzqpelqvVdkdyTerEH5fyoGiXdPm8emgf2hkvztK33IjtSPndFTOY9GtbtOlekE4V7d4miPuidledtqOdeKhH6u3KEDaHFq3hV6gspwCVJBsfxUpjt1Fc_y2HBhYRhIyh2dAAonlVZVWYopnpl_qNi7gI0VG2FX4JfiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8dff0e95.mp4?token=Wz8dHAjj9m_m9JgnHLZq5wXeWk67t1CgKpFPvXjMiKpYPzOYI1DnLd-NfehGhECWPMHfkz39_dQKS9DLpyzq30t30lID-YpppNwFWEOPvwppDsf3PHAR6LZVIEmV641dmjKkgH4HWoJgY2c4MOuVgBmACpqHGuvHNuroXXf2w2lyQlMdOCXzqpelqvVdkdyTerEH5fyoGiXdPm8emgf2hkvztK33IjtSPndFTOY9GtbtOlekE4V7d4miPuidledtqOdeKhH6u3KEDaHFq3hV6gspwCVJBsfxUpjt1Fc_y2HBhYRhIyh2dAAonlVZVWYopnpl_qNi7gI0VG2FX4JfiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی جنگلی در جنوب اسپانیا ۱۲ قربانی گرفت
🔹
مقامات منطقه اندلس اسپانیا اعلام کردند آتش‌سوزی گسترده جنگلی در نزدیکی شهر لوس گالاردوس در استان آلمریا تاکنون دست‌کم ۱۲ کشته و ۶ مجروح بر جای گذاشته و به مرگبارترین آتش‌سوزی سال‌های اخیر این منطقه تبدیل شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/669379" target="_blank">📅 08:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669378">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
تداوم نسل کشی اسرائیل؛ این بار در لبنان
🔹
سازمان عفو بین‌الملل امروز خبر داد رژیم صهیونسیتی طی یک هفته، سه خانواده از جمله ۱۲ کودک را در لبنان به شهادت رسانده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/669378" target="_blank">📅 08:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669377">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1LDfhjsD9D-wLKUwVNTxzp3sV13MESSyr9ogfLYOz2djGCDzyQC9-l7QE4d-RMdxDocfV32I8POw8KuhYpiyypxzl6yh9rf0oQ0yM25Gk9pfCymL6NEhtYR7jfRjQpboS9raMz008aeVhaSVno2jxjJ9jZgpEZT2SJsNwkBiVTBgEBpjVgGJ4GXAhVaHcjPh_ZuzLYjBhDmOJSplpsHPU0YhoXLaFYnhZXdFD0FfOaRc7VBkOP3ge9rNhSnmJO0n8_vVT9agffdAjLE7CDyxaj_fnDEScsznN56yNWQsIvBz4Pk7t64LlmE0MhG6tjxe8JVImIoB1Hf5JR7ZX4qBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان روز اول مرحله ۱/۴ نهایی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/669377" target="_blank">📅 08:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669376">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehhDEFDMSSfoBs0LHjo6UtkwCfxDqeRgGW6yg5nW0gO4z3QG75BQz8nUPx32JV9pp0SwX0FEUmNd1fhe_Oy5p0xXOvpxzaaU6yBo2Jr22RVEbcT3geBJKTN-amCeCVei6glQ56bjt63LZVIE033nPsJ5MRoRuWpsU05lnTXFOor3q9GM-ufD8AvCSaevwzsfIJR8IUCmUI8tuc5XqrkusP1t59UixmD0z8nprv4Tg2rEWPCChm73GksFZGLLqPfUci6UMhj4WmAoduGQ70FLJT6vlPXDZVNHeIrLML5knheCD4o-eJe4a41BRoJ1Y_H5oZPTJ7NZouIbqcSGUoPdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳ هدف راهبردی ایران؛ چرا این تأسیسات آمریکایی در منطقه اهمیت داشتند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/669376" target="_blank">📅 08:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669375">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhwAEishfjjQXpLU_fam8KnQNcSeaR009Mj7TCsdFMMsFynEv1TGXX3cfoGHrsjU1fNltj5tcM2mvm3rOP-tPHOU8LnEhs6NzVxmvTmL4TMc0c8CeVXLcfzW2kd9hoGwMpasnTYPecRy5H9JBKCzqIsaeJxRx_S7irjTiGycIoLAZLclo4pAZZD8Y41D6TrjELmUUU_yHs19jKwuTp1A16Dn7yyrPsEqPerOJCSERFi82jN1zOriQo-VT7R0xdVL9SF0IEJlIEsOgYwYL4BzZrMsxpZna66Hp0TSTZLbta5ch9iYwwqH3PZf6B0WLheDUoFz2BdMGpekfH3wlnJleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شرکت چیپسِ کشور مصر، تولید تمامیِ بسته‌بندی‌های و غذاهایی که برچسبِ لیونل مسی بر روی آنها خورده است رو متوقف کرد و از این به بعد عکس بازیکنانی مثل کریستیانو رونالدو، ارلینگ هالند و کیلیان امباپه رو میزنند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/669375" target="_blank">📅 08:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669374">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کره شمالی تصمیم به گسترش کمی و کیفی نیروهای هسته‌ای خود گرفت.
🔹
سی‌ان‌ان: بیروت ادامه مذاکرات را به عقب‌نشینی صهیونیست‌ها از جنوب لبنان گره زده است.
🔹
عضو کمیسیون امنیت ملی مجلس: امارات تاوان همکاری با آمریکا را خواهد داد
🔹
عطوان، تحلیلگر عرب: حمله به ایران در میانه مراسم تشییع رهبر انقلاب، اوج سقوط اخلاقی ترامپ بود
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/669374" target="_blank">📅 07:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669373">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7DD8KzslCguPSLeT5nOCtfLF3VKD5HW1i1Zw99zzUdoC63lgziepX9-NtJtrCmt4rRs8eYhonQlG4Bqy9lnttf9829eYdfBA511YAMPhcqMM6Aag0JgJgUyHz-AbJelGmGx1WfFkaK7mpM96t3CATJwuPwMHEx38QP8dHK9Cq3bc0ZjfBtWkNc2VaxX9plKcMzH_guohX-XBBpdnBiwxaFiA4_D_87AtmvKWtkcOjKEng_6MywV0LIGf507-6_An7U9j9XIaYZR_J1WSISOXitHEbd_DkoL1p-Jxc6frxcQ2yOMkhf6aUnVLIG75_xRw04O07bRnpP9VObkDK5Xnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیکر مطهر رهبر شهید انقلاب اسلامی در دارالذکر حرم امام رضا(ع) به خاک سپرده شد #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/669373" target="_blank">📅 07:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669372">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
«محمد» در صدر نام‌های کودکان انگلیسی برای سومین سال پیاپی
🔹
بر اساس جدیدترین آمار منتشر شده از سوی ادارهٔ آمار ملی بریتانیا (ONS)، نام «محمد» برای سومین سال متوالی، محبوبترین نام برای پسران متولدشده در انگلستان و ولز باقی مانده است.
🔹
در سال ۲۰۲۵، نزدیک به ۶۰۰۰ پسر با این نام ثبت شده‌اند که تقریباً ۲۰۰۰ نفر بیشتر از نام رتبهٔ دوم، یعنی «نوح» است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/669372" target="_blank">📅 07:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669370">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huQ_HEMlaHeJRtcfd2genYRuTDNiGRRH7Kw10tAjRm3U3reov5OStWUnVAjeEMH5g6o5AgJoMZUiQOlrkT4m72O8zEV8KIfJTKx3dC1pXt1esKKxeJaM5sRZvK0fbPf8jsC2WXtMNLDGiEx7qNJINJuM_aoML7dLl7oGCU2QjshdXGx_q3P3d-2xfbyvevFHKIlJT8NuFf_MAHxYFmO1yDxd0Pv1fOEDvF3SX8SXp87LynJd7tEoBRQtcJFreN7PaUvyMUcV2Kfx9l54QDwG72gMixA3EB0cOPeX8Sb_uhe3sr0sp8sqDbdBR-eFAUmibVU6TjtzYYSAqLbDwbkr9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پسر نتانیاهو نام خانوادگی‌اش را تغییر داد
🔹
یائیر نتانیاهو، پسر نخست‌وزیر اسرائیل، نام خود را به «یوناتان هان» تغییر داده و در نهادهای رسمی ثبت کرده است.
🔹
این اقدام هم‌زمان با محکومیت‌های بین‌المللی علیه خانواده‌اش انجام شده و روزنامه هاآرتص این تغییر را از طریق اسناد مالیاتی کشف کرده است.
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/669370" target="_blank">📅 07:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669369">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
منبع دیپلماتیک اروپایی: مناقشه ایران باعث ایجاد تفرقه و اختلاف نظر در ناتو شده است
یک منبع اروپایی در گفت‌وگو با خبرگزاری روسی ریانووستی:
🔹
مناقشه ایران اختلافات درون ناتو را عمیق‌تر کرده است، زیرا بسیاری از متحدان اروپایی تمایلی به حمایت از دخالت نظامی احتمالی این ائتلاف در کمک به آمریکا ندارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/669369" target="_blank">📅 07:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669368">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
سی‌ان‌ان به نقل از مقامات آمریکایی ادعا کرد: در صورت نیاز، مقدمات حمله به ایران در حال انجام است، اما تمرکز در حال حاضر بر دیپلماسی است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/669368" target="_blank">📅 07:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669367">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOA_3T8-LUiPoooU0TpH3WFRkZLOhKCaFJkZHyyT5SHzJpwTJtgAjzM6nbLig1FGAoH9CcF3dUJfKUvApqUpYDwQ94nOUQJNbbZM3t-cc7S1CiAtyaRtz8jmKRgCXwQl_JzMVJYirZUFj0RKadYHfuaMKr7eeVFtfDH6QD0olM-9bi9EYHNwp_W9DUk4ANnMCx3lQ1q1_Dp-dqAkF_cpc6qS0kf4hNLR_Hw8NbuaSmSaY9py_Seh5QTZRJgsBl9ifPAD838AvkzfrHh1kVgDedWe-0FeG_XFY9C9MTG-2rRlcuwZAszCRRmbBsB-ljzqrQ0MTEOlL6-ZcQPcVpM7vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پخش صدای خواندن تلقین بر پیکر امام شهید ما در حرم مطهر امام رضا علیه‌السلام
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/669367" target="_blank">📅 07:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669366">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmhiU1c4oltNDCS8wz1awuk7F6p-KHCosvcU0LuogcJDf79Ss5t95N5Nf3wSOyIjSi_QyMwTe4jJt0N6Ff3_RYt8hEzaa182JM-B9PuiWFsUT0zCr7BtF8VjUmm6fHe9siSWA5O23cDJNrAmmhzow5fEs0oebhoHmuPf752JqZi8EadubaqsqIuKNITYT0QFj9xen9KtBmgp0cdNLiYzTwTI1EtdWmePuoU0kY-j9q7My-ZAjIK-ObBvV2M50fspBB5YDxegY2oed_0gC-nzi4bErJ_py14JG2TiwCnJeUDU1vz89Um5mOY0diXhkiNBWHJT7eRGiExHYmLHSIONNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۱۹ تیر ماه
۲۵ محرم ۱۴۴۸
۱۰ جولای ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/669366" target="_blank">📅 07:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669365">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873ea1718c.mp4?token=ZKlVeZ_UKIAhooG6M9xtzn2ZAkza23ihp0JiFe4v1MJ1FJRrhNtKj-eKyOkJkb2mN4gJhoM-_cEJT_D1TcRo2hR9dnDEyhMbx32zhCTEW79ly7ILtDWUJ-8wj0dCrJo8QDJBz10qex9esnj28QhuQ-AnJFOOo_lXpXK3KS4DmUWOLVHLuCJiLW7cKenWD5SREfAbRb89ZFhlXAw8i600xEyw7bBocWA1oJFNxdS9P4_XJej3tILTfjiOo0CxWcXJpWPDofCa8god16z2j1KeNjUvR6f0ErkxdwSXC8Cejv7ZFZwMrM8s66nNojVXQrLpLXoV4twZeknvWaFQrQj8GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873ea1718c.mp4?token=ZKlVeZ_UKIAhooG6M9xtzn2ZAkza23ihp0JiFe4v1MJ1FJRrhNtKj-eKyOkJkb2mN4gJhoM-_cEJT_D1TcRo2hR9dnDEyhMbx32zhCTEW79ly7ILtDWUJ-8wj0dCrJo8QDJBz10qex9esnj28QhuQ-AnJFOOo_lXpXK3KS4DmUWOLVHLuCJiLW7cKenWD5SREfAbRb89ZFhlXAw8i600xEyw7bBocWA1oJFNxdS9P4_XJej3tILTfjiOo0CxWcXJpWPDofCa8god16z2j1KeNjUvR6f0ErkxdwSXC8Cejv7ZFZwMrM8s66nNojVXQrLpLXoV4twZeknvWaFQrQj8GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نگاهم به خالی‌ترین صندلی است
دلم تنگ لبخند سیدعلی است...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/669365" target="_blank">📅 06:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669364">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
حمله پهپادی جدید رژیم صهیونیستی به جنوب لبنان
🔹
رسانه‌های لبنان از حمله پهپادی جدید رژیم صهیونیستی به شهرک«كفردجال» در جنوب لبنان و زخمی شدن دو شهروند لبنانی در این حمله خبر می دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/669364" target="_blank">📅 06:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669363">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIcj4NiHeiiU8dzHOTPIzfSLS2hDlDlkH9BwMGQZ8T4qSugC_a2ef7-Ik8eLKv1QIdEuYpoaYmuN7BdBttSPcSumiUDkkHOGF7iUAMEFKc0cQYFc4NC3wO-gZTq1mP4c_BmIabOC-zSPYfFQQUMJ20CxrJphlqNYgEcAqKBAF2ehgsdqU1RD-UHwWOuF91YFsA0P9oiJkb3ZlmuqnGot8eSlkd5BUZ8g9-PmW5NYf2IhP9K9wBC1wDcyLVAFvU_4Absn6NEgDkCM_a5EeNRa8WkP31KSuSH31RabdPsBifFN-I9o3O33IlCJodVECEbrEqhnUdH7ODtO5PLD4H2qyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلگراف: میلیون‌ها نفر پیش از مراسم خاکسپاری رهبر مسلمانان جهان، خیابان‌ها را مملو از جمعیت کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/669363" target="_blank">📅 03:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669362">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
عبور از کریدور پیشنهادی آمریکا در تنگۀ هرمز به صفر رسید
🔹
بخش انگلیسی‌زبان شبکۀ خبری بی‌بی‌سی گزارش داده پس از تنش‌های اخیر میان ایران و آمریکا عبور کشتی‌ها از مسیر پیشنهادی آمریکا در جنوب تنگۀ هرمز موسوم به کریدور عمانی به صفر رسیده است.
🔹
داده‌های شرکت رصد اطلاعات دریایی «کپلر» نشان می‌دهد که در روز ۲۵ ژوئن حدود ۲۸ فروند از کریدور عمانی برای تردد استفاده کرده بودند اما این رقم از روز چهارشنبه هفتۀ جاری به صفر رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/669362" target="_blank">📅 03:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669361">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6MUUI7wbIETn9JM-PSHuABDhceOHBu-nat9JLePWBf7TRdE1AR5h9FH9yyzckWBWA9L7R7x7mUtIgtAdbZDCpGDNMhbfrGcg3e1QanahT99UOWeH3fHgAKQ7t7sOJRxdeoifm8HBJbVcZv3Zao0WBFMTuq5wAtgrOKSrh9t9xJTuHKF9oU2im7LX4KfoYzDZDGFOCFLbEMNguF6iK2oy9hw5k4F4Qac5yPnXBUHmfOiINZ8Wo8ciNbMndoPXyZZjHPziHuY3a-RPdyeXdm3fzEdYziqJpQ2v0IVhn3Y5cDD5v7OI4rDB-Wj7grYG8ZRhkjyDg1OAPg8kdhPZ3hCkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیری است ز آشیانه جدا مانده‌ای امین
غربت بس است رو سوی آن کوی و بام کن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/669361" target="_blank">📅 03:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669360">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سی‌ان‌ان به نقل از یک مقام آمریکایی گزارش داد که در پشت‌پرده، تلاش‌های دیپلماتیک برای کاهش تنش‌ها در درگیری میان آمریکا و ایران ادامه دارد./انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/669360" target="_blank">📅 03:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669359">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLzLKazMeD3O_-szYRIS8ErV0S4i8b3zfP9VVhsxnY2ZXvjpiFYEAbdcBlPuWx1pdYfpA4KnBSrCE9Cn890I5kVJ8GNomL4Vrmf2hEq7pLv_3MplKw52rfhw5FIcOK4rmA0CEH62j18jILRhSZtmtXrSGbHWbN5aARR0yIc4-JNNilVDdHJ94MXJtwydSWBLJPUcRvKXtcRzlUeaLiwT1dRalLCu2ymwubiPQ0QC9HJb22YefE5IoKAFd2x9OQrJEM8YqTX1KPa9NSs5RROKXruJ0qHPnW5ASXll5IYkUAq0xzgXMaDZse30H4KP7oFbQJJPFmGJr_Rqes6ZZfP8gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
نماز لیلةالدفن آقای شهیدمان
...
⚫️
روش خواندن نماز لیلة‌الدفن به این صورت است که در رکعت اول سوره حمد و آية‌الکرسی و در رکعت دوم سوره حمد و ده مرتبه سوره قدر می‌خواند و بعد از نماز می‌گويد:
💬
«اَللّهُمَّ صَلِّ عَلی مُحَمَّدٍ وَ آلِ مُحَمَّدٍ وَ ابْعَثْ ثَوابَها إلی قَبرِ فُلانِ بنِ فُلانْ»
👈
(به جای «فلان بن فلان» اسم هر شهید و پدر ایشان گفته شود)
📝
اسامی شهدا به همراه نام پدر:
👇
🖤
حضرت آیت‌الله العظمی شهید سید علی حسینی خامنه‌ای، نام پدر: سید جواد
▪️
شهید مصباح الهدی باقری کنی، نام پدر: محمدباقر
▪️
شهید زهرا حداد عادل، نام پدر: غلامعلی
▪️
شهید سیده بشری حسینی خامنه‌ای، نام پدر: سید علی
▪️
شهید زهرا محمدی گلپایگانی، نام پدر: محمد جواد
🏴
#باید_برخاست
|
نسخه قابل چاپ
🖥
Farsi.Khamenei.ir</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/669359" target="_blank">📅 02:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669358">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
خواندن تلقین بر پیکر نوه خردسال آقای شهید، زهرا محمدی گلپایگانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/669358" target="_blank">📅 02:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669357">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/269183605e.mp4?token=qjbsr9tjTpQA-o2KwOo7iVGJEURAow_mijuJ1uisloQchDTW0AsHOnY9KxHhHwBsFNCXWoB36zRIB4itO0KvPeMX-y2Uliva-n-AKlaCX05qpZcNQHeYOfcRhj-Ut_d99u4L5BOusOaK5jL31c4rJy1eJXMUV-1mS3KviigNdFoVAlEWS3VNzsWw-s8y5Y6SRT-MSPfSyLoMBqkvtXxOzRRxuVDNhoywNWp0W03-N5PLKOvG1ms6r6odYA-33-JZ1STTFxn5fBcA2yuHE7ME9JAPvMwsYzwAwAHNIBT-1lCtj4wEOj7lYy87vwUkrtfSujP416lraNdSbmTbtNAi4XFpC9spyngmYpA4DnZO2zijQP7YEU3Ao3E4zfr0faaNGRvvrpz3Ddc6VEeFZaScIClJ1CJOdJQspEv1LD2VbtNOLgkIIkcg6OJUvMIEU-JExnMRO2HzGnalZfvc2fBR59pBMO47MI3UYRlBrHo59Ii1_ziiAL7BMbnKXkRqWL6XbqcgmYa8xuRR85q0Ls8irU8ywGoHU4PQ12LVU9lOiEV5n3LC1qp8c68iYIPo8e9c0Ar73NRrbwdO5WNFLERYBJZYc0xmJPihk3IDpsDOLym3DNviBEzCZfsz2_7ia5KGQ7c8uJT3YYg1fnoy_OKqYBAPe4HyxFlzAcOx9p-1ILc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/269183605e.mp4?token=qjbsr9tjTpQA-o2KwOo7iVGJEURAow_mijuJ1uisloQchDTW0AsHOnY9KxHhHwBsFNCXWoB36zRIB4itO0KvPeMX-y2Uliva-n-AKlaCX05qpZcNQHeYOfcRhj-Ut_d99u4L5BOusOaK5jL31c4rJy1eJXMUV-1mS3KviigNdFoVAlEWS3VNzsWw-s8y5Y6SRT-MSPfSyLoMBqkvtXxOzRRxuVDNhoywNWp0W03-N5PLKOvG1ms6r6odYA-33-JZ1STTFxn5fBcA2yuHE7ME9JAPvMwsYzwAwAHNIBT-1lCtj4wEOj7lYy87vwUkrtfSujP416lraNdSbmTbtNAi4XFpC9spyngmYpA4DnZO2zijQP7YEU3Ao3E4zfr0faaNGRvvrpz3Ddc6VEeFZaScIClJ1CJOdJQspEv1LD2VbtNOLgkIIkcg6OJUvMIEU-JExnMRO2HzGnalZfvc2fBR59pBMO47MI3UYRlBrHo59Ii1_ziiAL7BMbnKXkRqWL6XbqcgmYa8xuRR85q0Ls8irU8ywGoHU4PQ12LVU9lOiEV5n3LC1qp8c68iYIPo8e9c0Ar73NRrbwdO5WNFLERYBJZYc0xmJPihk3IDpsDOLym3DNviBEzCZfsz2_7ia5KGQ7c8uJT3YYg1fnoy_OKqYBAPe4HyxFlzAcOx9p-1ILc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خواندن تلقین بر پیکر نوه خردسال آقای شهید، زهرا محمدی گلپایگانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/669357" target="_blank">📅 02:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669356">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
پایان بدرقه تاریخی؛ آرامش ابدی رهبر شهید در جوار حرم رضوی
🔹
پیکر مطهر رهبر شهید، حضرت آیت‌الله العظمی سیدعلی حسینی خامنه‌ای پس از عمری مجاهدت و جانفشانی در راه اعتلای دین و سربلندی ایران در جوار نورانی امام رئوف حضرت علی بن موسی الرضا (ع) در مشهد مقدس آرام…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/669356" target="_blank">📅 02:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669355">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzjccclE0UWXxAnA9J7F3_rKrAe02Yc70IfP0yTkHq20fGCl2QopcHjyAxzYw048wH6o-fejibig2Ewd13Ck_j90TkeVu1XBOXYGXRA3SYvjs5sYwCKzx9OqjU02p7CIdYHofbusimrkG8uafQ2DTc_b3gVbE8kADDlvBaRjnKcSKnx2YC-MMq9yCpJf6c9jlCyFqdsX97oFzn5u_4X_zTvu5fhFQFUlOdb9cCTNobyq5mMFbufY-4u3fLUG-SOV5Qf83ss5C9B39fBJqkFBze-dDA5FlFeIVbfZ7kaM08ouzfXGIFjYXgpRnE8xuYN_ZCcOm1NYuC_y2w10_1nAEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و آنجا که آمد و شد خیل ملائک است
کنجی گزین و تا به قیامت مُقام کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/669355" target="_blank">📅 02:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669354">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438841b458.mp4?token=gusqvHVuTTWbUSsERBJ7U8poEousq6at7s1Ov3JgAe4Z8MJtdbIBT77exUimMeuOb3uFCr02CE3AFfAE7ScpVqLpqL15YLiBngW9eAySkjnO3_DEeSt7Tqz4UPQQmuxFwUdPRHCko7A_HWeFmRtejE6ooa5qE3_NBy-YnuK0E68V-YSHwox1eLT4TVdEhNCy5TsloVc6q6QVGaudho0HoVBnCC9GIk0JQwIYe64dFf2yQ7KlYTckvtrcLSVXaCZV_3s5DIFhIuFMyfOAOlUqCAT6o8kkG2gYIeG4V6umyG9KOcCHMvT9nAb9n32yRjm-sImRWix4F36WIhIMaPqvGgv1O9h8GjQJjABs_4jk5pfCK25NfqklC1geEiZNFDJxIZZ-n7RyKaAiIm8QRVYEFmM1BRUtRW4Vng--eIS9MOxhOb0s0S3Yxh9ULPWUP43MsCImAs8SXMziHzcuvqBbDzRpzv09o3vYoz0cEuZPnmeclc3XD4sy4cTYc5fFV4AMHJrlDYgfaB1NapL0Uii4TnLjLOIA_OCBQxtuihnhy74v5ggCX2hbx5m9mQLf763KMUCsDXdyZTcKdnuQlvb90by4hNfKKmNfFqYzK7fL4iH8OVvthQHK7Uq8Yeze3vPRP-rJsfmtZal1ZToNnDz1r_qf156ynMHAf-Hi4ApvC3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438841b458.mp4?token=gusqvHVuTTWbUSsERBJ7U8poEousq6at7s1Ov3JgAe4Z8MJtdbIBT77exUimMeuOb3uFCr02CE3AFfAE7ScpVqLpqL15YLiBngW9eAySkjnO3_DEeSt7Tqz4UPQQmuxFwUdPRHCko7A_HWeFmRtejE6ooa5qE3_NBy-YnuK0E68V-YSHwox1eLT4TVdEhNCy5TsloVc6q6QVGaudho0HoVBnCC9GIk0JQwIYe64dFf2yQ7KlYTckvtrcLSVXaCZV_3s5DIFhIuFMyfOAOlUqCAT6o8kkG2gYIeG4V6umyG9KOcCHMvT9nAb9n32yRjm-sImRWix4F36WIhIMaPqvGgv1O9h8GjQJjABs_4jk5pfCK25NfqklC1geEiZNFDJxIZZ-n7RyKaAiIm8QRVYEFmM1BRUtRW4Vng--eIS9MOxhOb0s0S3Yxh9ULPWUP43MsCImAs8SXMziHzcuvqBbDzRpzv09o3vYoz0cEuZPnmeclc3XD4sy4cTYc5fFV4AMHJrlDYgfaB1NapL0Uii4TnLjLOIA_OCBQxtuihnhy74v5ggCX2hbx5m9mQLf763KMUCsDXdyZTcKdnuQlvb90by4hNfKKmNfFqYzK7fL4iH8OVvthQHK7Uq8Yeze3vPRP-rJsfmtZal1ZToNnDz1r_qf156ynMHAf-Hi4ApvC3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پخش صدای خواندن تلقین بر پیکر امام شهید ما در حرم مطهر امام رضا علیه‌السلام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/669354" target="_blank">📅 02:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669353">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZC1UzypNHRMyyuNFyhfRk3GMKdxEKrXtzTXIGRpndU7BzVwghtD_-OvWiJ3oiRecqUVLgfc0CRPQXj7LULb3B-UKCqUex7tYKq2eo2bK80Xp_J0NgveUEQFqitB6hLiqnu9a5UjZOQCxwYMzH6GJXKOzcmvUGnIpG9xSFPD26LO_6SfbtbaOnJqTOSW2xvRUspbhO63rkUJJjEiuL8rlplTSzHQdZjKSIcd84dh1AZkWcLPydWt3gi67bF9qyl1K2s_g-MT4yBHbLkYBLmP6KgYYxUOJu2FRKB8AFNtNcpnDearidgrJzweJmZRiXzbYoZILApm2mDmbWna1mNXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار پاکستانی: ایالات متحده و اسرائیل تمام تلاش خود را چه در بهترین حالت و چه در بدترین شکل به کار گرفتند تا جهان اسلام را دچار شکاف کنند، میان اهل سنت و شیعیان اختلاف و گسست ایجاد کنند و از بسیاری دیگر از نقاط اختلاف بهره‌برداری کنند؛ اما در نهایت نتیجه معکوس گرفتند و باعث اتحاد همگان شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/669353" target="_blank">📅 02:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669352">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6367522cf0.mp4?token=APzWv_uedVh00gwDZ__nSqHt9w6FIaTcjFoel-dNCig2rsgCLJbdHv4dumj6_VAvVmxYDaOGarctub71vD2tnSMz2IM2_-JAZfachCY9KB96qw7KhY3qr4mIuVX1vQWZa7QwtcnzDOeMdenlnYiwY9Yxnhh7njIuQ71PjYNASPWVLByRHfXf69zIDC5xbaId9AR60tJo1U2Pbn-Lc3akw4dHD0DYb8dTesTYW0geai-W0TH12zvmj0N0-reV7YrpTMSVXgQKECHvJ7Nl-s6MtEuu1hmPXxGudiU8GFP4x4lg7eS-OuimgghKJcA_iISRpKG6BLwPW5DtPe-k1SdHdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6367522cf0.mp4?token=APzWv_uedVh00gwDZ__nSqHt9w6FIaTcjFoel-dNCig2rsgCLJbdHv4dumj6_VAvVmxYDaOGarctub71vD2tnSMz2IM2_-JAZfachCY9KB96qw7KhY3qr4mIuVX1vQWZa7QwtcnzDOeMdenlnYiwY9Yxnhh7njIuQ71PjYNASPWVLByRHfXf69zIDC5xbaId9AR60tJo1U2Pbn-Lc3akw4dHD0DYb8dTesTYW0geai-W0TH12zvmj0N0-reV7YrpTMSVXgQKECHvJ7Nl-s6MtEuu1hmPXxGudiU8GFP4x4lg7eS-OuimgghKJcA_iISRpKG6BLwPW5DtPe-k1SdHdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین ز خیل ملائک حرم پر از صف شد
علی‌ست زائر مولا، «امین» مُنَجَّف شد
🔹
قاب‌هایی از تشییع پیکر رهبر شهید ما در حرم امام علی علیه‌السلام
﻿
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/669352" target="_blank">📅 02:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669351">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
روضه خدام حرم امام رضا علیه السلام بعد از تشییع پیکر امام شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/669351" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669350">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2757dbcfa9.mp4?token=VbGWI7lY9gRvrXwqm82u5D-pkfwYIgEiKjcMaAN_khW9BANpLmB6-ZLFZksjq2e9an4ImEqFc95WZ-AglE_-9YXJh4RFTHoR__3NCQzFP3MDFBW4d8nXBMp7kujn8rRMwkoO549o3uNlVS8vVEAuxWB6uCcMuEEJy5uvKw4LvktjQruTSG4NwtRmUN65526YQSGDZ-jVcBL6pLPTYqE-SCHw1-38QXzo6eojOpLtC12RCyRPE7Hvcu-kxDhqjCIvF-5LFkK1RV63yVaxfJcmAE1TnX4pZgy61CMugHm7OQqLeqCgpk0nA1Ay7AOGHmsYaTXNa3IYNg4smWTHyBLhHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2757dbcfa9.mp4?token=VbGWI7lY9gRvrXwqm82u5D-pkfwYIgEiKjcMaAN_khW9BANpLmB6-ZLFZksjq2e9an4ImEqFc95WZ-AglE_-9YXJh4RFTHoR__3NCQzFP3MDFBW4d8nXBMp7kujn8rRMwkoO549o3uNlVS8vVEAuxWB6uCcMuEEJy5uvKw4LvktjQruTSG4NwtRmUN65526YQSGDZ-jVcBL6pLPTYqE-SCHw1-38QXzo6eojOpLtC12RCyRPE7Hvcu-kxDhqjCIvF-5LFkK1RV63yVaxfJcmAE1TnX4pZgy61CMugHm7OQqLeqCgpk0nA1Ay7AOGHmsYaTXNa3IYNg4smWTHyBLhHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به امید دیداری دیگر...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/669350" target="_blank">📅 02:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669349">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84b553e0cb.mp4?token=ToAnon5rhp_8UTHERJjG7Lvu-HtEj1Id2vKyJSglvPL8n9nhlYXBOkRvtvwrdic_AMbXS14us-6zhfQB1vusrY1AJnExXq_X9-WaCosWWreMEZt83LNyzJFP7ASEa6v_6Yai_IbQYvQkKojOxJQThScAMKqtHbN1S5RswN9QMEINZrcUJCTPvN3DExbYzdTpK5nwrOyAT29rCv8-C_atsCAOT5bKu_RxPzn2-60KfRVsvpJ2rPPogw_mPtR0gpLQH4f_uv5C7A-B8RuC7jeieAKEfKEukybK2wapKnb4g96_05zXLjYe3yfQzkrZYAC0D_1I306mwVwWR0UnQhc62Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84b553e0cb.mp4?token=ToAnon5rhp_8UTHERJjG7Lvu-HtEj1Id2vKyJSglvPL8n9nhlYXBOkRvtvwrdic_AMbXS14us-6zhfQB1vusrY1AJnExXq_X9-WaCosWWreMEZt83LNyzJFP7ASEa6v_6Yai_IbQYvQkKojOxJQThScAMKqtHbN1S5RswN9QMEINZrcUJCTPvN3DExbYzdTpK5nwrOyAT29rCv8-C_atsCAOT5bKu_RxPzn2-60KfRVsvpJ2rPPogw_mPtR0gpLQH4f_uv5C7A-B8RuC7jeieAKEfKEukybK2wapKnb4g96_05zXLjYe3yfQzkrZYAC0D_1I306mwVwWR0UnQhc62Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار ما به قیامت آقای آسمانی...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/669349" target="_blank">📅 01:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669348">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2RA-lIcp0e3_WiziDkqsMC0JT_EWDBcdUjn8IwdlSWhOnmahY0qTqphvCJsO_H9gIfp6cGy_6xMY16iHJ-6XmeskdK5pygzenzRFpVuoJ2vb3K9SiF-2r3VeNmcMpvJub54L0kjvRPo0ttvZ2GR1s4FCrERMPpJTLGzcNF-fHwZkTn0ez3II9OViPbyVz-6CZoc-6D9ZdyML12-tdiTs2OE9TFk5tOfJvyf3EsmMbXLG87Wrp1SBDGDGMLvFSYsoLbwTG1EoG4Iq6jbgqpIEYwmveY5JlUGJ2lj0kCO_9mR93Uf4oUNkk127ZFpJc7Sle72mdJzU8K6bu9UwcgQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۱:۲۰</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/669348" target="_blank">📅 01:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669347">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb2e3a97f.mp4?token=ka0-Ir55R2YmY1uOiM02Vi_wk3Jo8-llZhVeB7HwBGI4dWfLiCpFjXnRwUz3NKk0H2e93-M4YW-WyWNxsRGMQgq7Hx2b_Y1Ka8S9M_lz0K2YozMcRdFql4tfF6IOCZKi8tLssubFs3QvFJDWMhwgKhN1uHc8LmTaoUOKftmFaa08ByADkihZnj8t3AYe3sAooG6Wz5IiQ6fopux3pF4D_FMzWv0H37KB-I0TScRkFvvJBBS8_H6qZq6UYvYOAcF5xW5CgpuGJq-BE4Sbcapnva3S7NbZOOj12RyPddg3cxhpw0eD7CrTiI60UCjiPndUKnMxxUHsmGRQuqjvGWh6OFkI-6Wc734zqW42jY1t2QsNaNzdsZviafqK_FknadJtKYZhZGWL8DvGSGx06rkGXgMZxlhtBgFl2-463wUVByO_MD13O7m2OosjNuat1qTaGd1rkcN_4Gw03fcNsCyNaLRrhyKriqqaXMcKAiyu__zC0GpTMTunGjFxOKL8Gm9m906JeC8UOkn5A979j93NZhZK_wI3vi4THii5AQFrbocOcKjztePHkxz8ARgPkJg-heSJpOORj4BXdzVPFVDrgLJQBpgnaoho7qattbEobS7bUD8oVCtskNPHJju8ZHnXhgMSbv6D54JPsHjMwdtsVIUd2FY6YQ5EPnNMmEx6kKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb2e3a97f.mp4?token=ka0-Ir55R2YmY1uOiM02Vi_wk3Jo8-llZhVeB7HwBGI4dWfLiCpFjXnRwUz3NKk0H2e93-M4YW-WyWNxsRGMQgq7Hx2b_Y1Ka8S9M_lz0K2YozMcRdFql4tfF6IOCZKi8tLssubFs3QvFJDWMhwgKhN1uHc8LmTaoUOKftmFaa08ByADkihZnj8t3AYe3sAooG6Wz5IiQ6fopux3pF4D_FMzWv0H37KB-I0TScRkFvvJBBS8_H6qZq6UYvYOAcF5xW5CgpuGJq-BE4Sbcapnva3S7NbZOOj12RyPddg3cxhpw0eD7CrTiI60UCjiPndUKnMxxUHsmGRQuqjvGWh6OFkI-6Wc734zqW42jY1t2QsNaNzdsZviafqK_FknadJtKYZhZGWL8DvGSGx06rkGXgMZxlhtBgFl2-463wUVByO_MD13O7m2OosjNuat1qTaGd1rkcN_4Gw03fcNsCyNaLRrhyKriqqaXMcKAiyu__zC0GpTMTunGjFxOKL8Gm9m906JeC8UOkn5A979j93NZhZK_wI3vi4THii5AQFrbocOcKjztePHkxz8ARgPkJg-heSJpOORj4BXdzVPFVDrgLJQBpgnaoho7qattbEobS7bUD8oVCtskNPHJju8ZHnXhgMSbv6D54JPsHjMwdtsVIUd2FY6YQ5EPnNMmEx6kKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بله، وقت تمام شد...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/akhbarefori/669347" target="_blank">📅 01:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669346">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYigegoSYjOUo2SoHi0tS7eYHtkj3_F5uynqtVaSr3ikIhE0FRH0HxLuLoH6P5QMR1SL2Xu8-KxTKE9W54OGy79cVuoDqiEZ75iBeCuireRuHoGJV4QrVD7X-GSNgjcCU5bi7V729KUX5p9gNbtWa_PLJDh9S97KzKMBxGS7BxG514WdfIFdk_IVsKJ7gIUKskwpR1L003WugbTzaEeauk4ZV4P-H8FocWWAHCUB7plNPxs4R2A16W4kR-FTdaqNF8S-dzRfBDBu11BHWzy5kGgMvbjkUicAVh4XzpfeewkcdGjA4KF-g0MUF3bs6tPOLUTfZIT_gc398TTUUuABnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینک شما و وحشت دنیای بی علی...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/669346" target="_blank">📅 01:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669345">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91faf2a0b.mp4?token=EdODjygXCrcfLlhHmpdLkGsgMPUeUIUviuPMaa5tBvNUd2YToNdicx3OvnpR1D1-p253nM54yu1brpNrP3t5VOQBqirsEDj_b8hZyKIIKwJYAzyfMYt1nw55P0yXIcU6Q1amvjPPSM7glZle5WA-lsKhB-zf1j6NJtY8l4QY7L7seqhPczeaFWKGwmTWwmltUmSoc3gHZ9lLV3SEPEMFBaZenWNKTh6JqyeylZ4WgCl5wP57HEdncftzwyh7mqeJABLKo77TIyBIcbSNtd7rWtTa9IwexR2dspmM75kyftHKvEQz__S3aJVrGC7AVNYPyhM29zrRPA_-LSv5Hw6_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91faf2a0b.mp4?token=EdODjygXCrcfLlhHmpdLkGsgMPUeUIUviuPMaa5tBvNUd2YToNdicx3OvnpR1D1-p253nM54yu1brpNrP3t5VOQBqirsEDj_b8hZyKIIKwJYAzyfMYt1nw55P0yXIcU6Q1amvjPPSM7glZle5WA-lsKhB-zf1j6NJtY8l4QY7L7seqhPczeaFWKGwmTWwmltUmSoc3gHZ9lLV3SEPEMFBaZenWNKTh6JqyeylZ4WgCl5wP57HEdncftzwyh7mqeJABLKo77TIyBIcbSNtd7rWtTa9IwexR2dspmM75kyftHKvEQz__S3aJVrGC7AVNYPyhM29zrRPA_-LSv5Hw6_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در جمع خادمانت، شوری به‌پا بود امشب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/akhbarefori/669345" target="_blank">📅 01:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669344">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1iBaFDorWX67BgDbCChPAmqz8VAwU4Sn021_kyrPrsf13FD_Kaw8X2PFST3KkQwI1skkpcRv4AqGfaeuNvQ64jAG4syV7l46f34W94Td1vAymrtyWi53_sDwlxIZd88NTL-4Wp0HU-iiakfjWD-WQlACxgnseqW5RuG0-mhE_xrtNiLbU8MfAOWa3ejEJCV5VfABAnZRBNDT3QvYVsyE1lJlFHbTGropgX9V3kj_ewdndtEEgV1XrVnY73LXZcmf1q3CFm7V7EG0z3Sv3GCEaAbmYoKCMzDYC95Lg-QpFu8_WVmcGwsAxxL8KQEudWd_ySqG1LWcJQ8DwqXZz5-lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خروس‌ها نخستین تیم صعودکننده به نیمه‌نهایی جام جهانی
🔹
تیم ملی فوتبال فرانسه با ۲ گل کیلین امباپه و عثمان دمبله با برد مقابل مراکش، برای سومین دوره پیاپی راهی نیمه‌نهایی شد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/akhbarefori/669344" target="_blank">📅 01:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669343">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">نقطه‌ای که ادمینِ کانال اخبار رهبر شهید انقلاب بعد از طواف و خاکسپاری پیکر آقا گذاشت کار صدتا روضه رو انجام داد.</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/akhbarefori/669343" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669342">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H88ZtVQtw-lHh5lNn4LeKb4huDttl1X4Xtr-lqDlCRhPy1vNMEJrpm-JjCOaoLag5XcBW6_mADEEApFTJgrkUGa7OWpaBF5rWALYUwc7yb-4yJLp27qTwc_HC2kCcWIW5r8cmdoMyOobN7Qju1mnqAeCvwgl-JPE9wwalMnVcinEWS3hJqcrNWQsMUQY19z4g7WeZtrUgmK5Ts1J1BjJT1T1tICqlY5h7n8HFlYcmx58PkbnwAHbiGRWSSuIjE4117urjqe9sVdW6oZwmd9rlhn81ESFeN8nZ2WZ4T3fwGITK6VyuoeOzeCEEP7L4nrQ_skDtsWjORtFBOWAOJjnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقطه‌ای که ادمینِ کانال اخبار رهبر شهید انقلاب بعد از طواف و خاکسپاری پیکر آقا گذاشت کار صدتا روضه رو انجام داد.</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/akhbarefori/669342" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669338">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa8a1ef2d7.mp4?token=TVR8P1Y5X3MGGsE_u-HEFvAJrmc_5NcBpMO03XqNdCV4lQIn6A3Cc6ni_-7C40cQQwBC5-DHZTHP_l3WShzFNqawtlMMg9B0rjs3SadcN9BaT67JkJmZ-hmYjEGbjUv_DFVdx9QYr4o6fDgLYlIaiyVmIV1Jeg7_wbEyO7cdzdyXrn69DhdTErD1OfblRB4qrFv01UkEVMHoO6wg6zuFJ0JcAbcRt8c-R6ESFG35bX_qY2KeNpNsTWxxTZpEp_fmqHCLw9X090quxR1NnyvmAxFOI3wLF065M3gjzwmBuUAh3UCzs1is04NHWYCZIKh1PIPl2A2P4b5_Zd316iNEYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa8a1ef2d7.mp4?token=TVR8P1Y5X3MGGsE_u-HEFvAJrmc_5NcBpMO03XqNdCV4lQIn6A3Cc6ni_-7C40cQQwBC5-DHZTHP_l3WShzFNqawtlMMg9B0rjs3SadcN9BaT67JkJmZ-hmYjEGbjUv_DFVdx9QYr4o6fDgLYlIaiyVmIV1Jeg7_wbEyO7cdzdyXrn69DhdTErD1OfblRB4qrFv01UkEVMHoO6wg6zuFJ0JcAbcRt8c-R6ESFG35bX_qY2KeNpNsTWxxTZpEp_fmqHCLw9X090quxR1NnyvmAxFOI3wLF065M3gjzwmBuUAh3UCzs1is04NHWYCZIKh1PIPl2A2P4b5_Zd316iNEYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طواف پیکرهای خانواده رهبر شهید برگرد ضریح مطهر حضرت رضا (ع)
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/akhbarefori/669338" target="_blank">📅 01:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669336">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال: اسرائیل به آمریکا اطلاعاتی داده که نشان از طرح ایران برای ترور ترامپ دارد
🔹
اسرائیل اخیراً اطلاعات جدیدی را با آمریکا به اشتراک گذاشته که به گفته آن، نشان می‌دهد ایران طرح جدیدی برای ترور ترامپ، دارد.
🔹
خوک نجس روز چهارشنبه در جریان نشست سران ناتو در آنکارا، ترکیه، به تهدیدهای ایران علیه جان خود اشاره کرد و گفت: «آن‌ها می‌خواهند رهبر آمریکا — یعنی من — را از بین ببرند... من در همه فهرست‌ها هستم. امروز صبح دیدم که در تک‌تک فهرست‌های آن‌ها قرار دارم.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/akhbarefori/669336" target="_blank">📅 01:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669335">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPbAnmg8fyOCb30ywolAn3_WmJzAE6psa6OE0giYdlNUJXQ-vMGBsmNwlE2x_wUQ5FoOwDa83CYMRjZNCWQA62z7c1jgBDf_GM7Cgm6RYbTixUytb9s157up54pE7Va-TTEwdFqr93wnTKv4G_My3NbIZFwYGPiXWf8vzgElrDvPjlZ88PwmXTJzrIlQTydyFdTrTCg9P7d7oBHw8EEQZao7hi1NVL7HpdxhjgmyDPLkK5h7EYFJKyfz78FQqpIWJupYrbFUM_xm7IpPcSuDV6-eYOS4bvew9HDHv44XPm0sliPMY4RG1plwnJaE3t3fcvB39-1Hn4zoWHE8u5utQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا دشمن، از درک معمای حضور میلیونی مردم ایران در صحنه عاجز است؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/akhbarefori/669335" target="_blank">📅 01:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669334">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55abc22245.mp4?token=hutxpcvyNDTewHIHrAqhHD92r7Vziq6JavdiEzHmvoB7qXq8pmRtIGYBxHPS7jmPN1bVzysT5NcDJ33klYKaBGb0NRsQ5eR8IW8JcbYosSdaEwcXMOsUsdPVo-P9C8J00YHeC2M62BixtVpKFCxxgnc3vQNVYfZ7C7e71mrtbY2A3GLrJPqO5xhrsu84b2OnJbK4o86a9h_iFnZeYM4JV45FrPxppARQr1MZ3RddG2zA3y1OC9CO6eF-aXLsb4bfym2CZbDvIkMS4jeb1Vqdo6fkQ4x_1GGuE42ZTrZgs-rhZU7SoRwuMgor_onebGYtNzHDKWFQL3NfuHIRUzaqIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55abc22245.mp4?token=hutxpcvyNDTewHIHrAqhHD92r7Vziq6JavdiEzHmvoB7qXq8pmRtIGYBxHPS7jmPN1bVzysT5NcDJ33klYKaBGb0NRsQ5eR8IW8JcbYosSdaEwcXMOsUsdPVo-P9C8J00YHeC2M62BixtVpKFCxxgnc3vQNVYfZ7C7e71mrtbY2A3GLrJPqO5xhrsu84b2OnJbK4o86a9h_iFnZeYM4JV45FrPxppARQr1MZ3RddG2zA3y1OC9CO6eF-aXLsb4bfym2CZbDvIkMS4jeb1Vqdo6fkQ4x_1GGuE42ZTrZgs-rhZU7SoRwuMgor_onebGYtNzHDKWFQL3NfuHIRUzaqIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حلالیت‌طلبی یوسف سلامی، خبرنگار صدا‌وسیما از رهبر شهید انقلاب به‌نیابت از همه کسانی‌که طلب حلالیت داشتند
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/akhbarefori/669334" target="_blank">📅 01:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669333">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هم‌اکنون سوزاندن نمادین طرح لگویی ترامپ در مشهد
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/akhbarefori/669333" target="_blank">📅 01:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669332">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
معاون امنیتی استانداری خوزستان: هیچ حادثه امنیتی در استان رخ نداده است
🔹
معاون امنیتی و انتظامی‌ استانداری خوزستان اعلام کرد که برخلاف شایعات و ادعای دروغین رسانه‌های صهیونیستی، هیچ‌گونه حادثه امنیتی یا حمله‌ای از سوی دشمنان در سطح استان صورت نگرفته است.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/akhbarefori/669332" target="_blank">📅 01:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669331">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967d589bff.mp4?token=G6xYPIITmsk7mkSVBDFc8Zg7nW_0X8iyh0OWlPM14h6uZeec1LNFXVOuAf47zK14BR1lFS0yTU41gjAYPZFVtP3NvnK_5ONSX63wtieCrlhVNAXUjHZAmlO5j2rnyhxBaH_qfEv99LVLDLh_YvGmzaYYq7hAtb-UG6CUlTfDh3JykMMBF3eYToYxbO8gF5ZVBpqR0UW85dCO0GHHmv1ZhVyZLEPPbQovjlCWpeJGRmSCFF3tnrx_Yvmdn47ZnO-PHN7Ib97ACLwP-VsJkdTCa6964FBrXwXAeUfPhU85-A5b6or8akqXlHvz84OEHpDQ6ZA-n_2AX8GrXtr5QdHqg4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967d589bff.mp4?token=G6xYPIITmsk7mkSVBDFc8Zg7nW_0X8iyh0OWlPM14h6uZeec1LNFXVOuAf47zK14BR1lFS0yTU41gjAYPZFVtP3NvnK_5ONSX63wtieCrlhVNAXUjHZAmlO5j2rnyhxBaH_qfEv99LVLDLh_YvGmzaYYq7hAtb-UG6CUlTfDh3JykMMBF3eYToYxbO8gF5ZVBpqR0UW85dCO0GHHmv1ZhVyZLEPPbQovjlCWpeJGRmSCFF3tnrx_Yvmdn47ZnO-PHN7Ib97ACLwP-VsJkdTCa6964FBrXwXAeUfPhU85-A5b6or8akqXlHvz84OEHpDQ6ZA-n_2AX8GrXtr5QdHqg4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم فرانسه به مراکش توسط دمبله
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/akhbarefori/669331" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669329">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
وقوع تیراندازی در مشهد تائید شد/ دو نفر کشته شدند
🔹
معاون امنیتی استاندار خراسان رضوی وقوع تیراندازی در منطقه بلوار سرافرازان مشهد و کشته شدن ۲ نفر را تایید کرد و از ارائه جزییات بیشتر در این باره خودداری و تاکید کرد: «هنوز علت حادثه و هویت کشته شدگان مشخص نیست.»/ ایرنا
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/akhbarefori/669329" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669328">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344822aa12.mp4?token=OXga43IVlOzSZ5mfj2SXKRqA-3mDlm_zcMr3egv1Tuogh62-zF-1h9NtQfkeCdI4tl1RtlaoMeEfo4PoS46ub5RPW-CSfgugB5xetm4Xc07yTexJl62LU4Fu26ANqHgnX2k-XsZy_SKJhKD-zddadscp07ogv4Qz5Ubk8CpDdZfZ68qrjjxtcxO2tWTJ2b2tAv8GBmEvZDz5FeXqnQVGeM1y99IPUzUlwaUiJ9kAoRpygLwJZaWBfl5KgYMmTF6f3UHLTWoKCZsauRebe0e_vudJuZC8-o2Y_VLMWJaZofv1OzslFTl0jwNMxAlUFhHE55R6cwh8uPzYC09KUEM7og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344822aa12.mp4?token=OXga43IVlOzSZ5mfj2SXKRqA-3mDlm_zcMr3egv1Tuogh62-zF-1h9NtQfkeCdI4tl1RtlaoMeEfo4PoS46ub5RPW-CSfgugB5xetm4Xc07yTexJl62LU4Fu26ANqHgnX2k-XsZy_SKJhKD-zddadscp07ogv4Qz5Ubk8CpDdZfZ68qrjjxtcxO2tWTJ2b2tAv8GBmEvZDz5FeXqnQVGeM1y99IPUzUlwaUiJ9kAoRpygLwJZaWBfl5KgYMmTF6f3UHLTWoKCZsauRebe0e_vudJuZC8-o2Y_VLMWJaZofv1OzslFTl0jwNMxAlUFhHE55R6cwh8uPzYC09KUEM7og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول فرانسه به مراکش توسط امباپه در دقیقه ۶
۰
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/akhbarefori/669328" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669326">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ادعای جدید سنتکام درباره تنگه هرمز
سازمان تروریستی سنتکام:
🔹
ادعاهای رسانه‌های ایرانی مبنی بر اینکه عبور از تنگه هرمز فقط از طریق مسیرهای تعیین‌ شده توسط تهران مجاز است، نادرست است. آمریکا در هفته‌های گذشته مسیر جدیدی برای عبور کشتی‌ها از تنگه هرمز پیشنهاد داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/akhbarefori/669326" target="_blank">📅 00:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669325">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
علت عدم حضور آیت‌الله نوری همدانی برای اقامه نماز امام شهید
اطلاعیه دفتر معظم له:
🔹
با وجود آنکه مقدمات حضور معظم‌له در این مراسم مورد بررسی قرار گرفته بود، اما با توجه به ملاحظات جسمانی معظم‌له، بُعد مسافت و فراهم نشدن شرایط لازم برای انجام سفر، حضور ایشان میسر نگردید.
🔹
همچنین چند روز پیش از برگزاری مراسم، عدم امکان حضور معظم‌له اطلاع داده شده بود. با این حال، متأسفانه علی‌رغم اطلاع‌رسانی قبلی، خبر حضور معظم‌له تا ساعات پایانی مراسم در برخی رسانه‌ها منتشر شد و موجب بروز برخی ابهامات گردید.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/669325" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669324">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46229c7a7a.mp4?token=MtMXPSDP4tatyVWgIDTH7yuFQM_L9DjE6cNqKG7Or88ivMTHvkNaLFRq-qRiTkuGPwgbR8d-ny790kaTu4n7UrgzJ9f3FWlZUcjsxSuLWbzoOP72fhSwNe-9A7pgJmjrbE7MQ5cxuHOg3wmdIRh8Uxyd0E0sBgjD_3qHjCLNJjtuKZgbqTzHclcEtIW80WTnO9S1xCRgzHTmF0YQtFdMDGpmT8SmMLCwMEvzwgzJ-VPxVrfFRqt_dlaEI4jtsUz1jKy9VzWUUvXV-h_xkLjKsMzfoHEPZV9hsFkS4QLv6OIloNYMRsFuh7fayhPs_plAHUhfog69ioJNdDplqzK5oE94asqa9b1cX0AXU96FaU_-cvhlrYSnR0WDNSn4tGrsq-N_lcZFr10jrqEaqYeeYWeL_p0eZGl-xEQopIKBOUPkgiNCLpTWMl_eKpWH1MkK5fzSpGa8GbdF94obuywWXRLCu9oIn-4Vod9yhn_81-iUtKx03DhLNILggME-451U8a10uRr4V9wThuzGxOBHnynY7_TGgDTHESNoNerXNECRQXub7oCyNRNpHX4NbpKnTLf46X5MWt7OFuDkY8hrsqDJskFtiKPuj9MeBztw6UPiWvg2qwcIXi-OHo0yF_jHDxYlzE3jY0bch9vIFvx-cQKad9XPT4n5iLfdOCmf5eM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46229c7a7a.mp4?token=MtMXPSDP4tatyVWgIDTH7yuFQM_L9DjE6cNqKG7Or88ivMTHvkNaLFRq-qRiTkuGPwgbR8d-ny790kaTu4n7UrgzJ9f3FWlZUcjsxSuLWbzoOP72fhSwNe-9A7pgJmjrbE7MQ5cxuHOg3wmdIRh8Uxyd0E0sBgjD_3qHjCLNJjtuKZgbqTzHclcEtIW80WTnO9S1xCRgzHTmF0YQtFdMDGpmT8SmMLCwMEvzwgzJ-VPxVrfFRqt_dlaEI4jtsUz1jKy9VzWUUvXV-h_xkLjKsMzfoHEPZV9hsFkS4QLv6OIloNYMRsFuh7fayhPs_plAHUhfog69ioJNdDplqzK5oE94asqa9b1cX0AXU96FaU_-cvhlrYSnR0WDNSn4tGrsq-N_lcZFr10jrqEaqYeeYWeL_p0eZGl-xEQopIKBOUPkgiNCLpTWMl_eKpWH1MkK5fzSpGa8GbdF94obuywWXRLCu9oIn-4Vod9yhn_81-iUtKx03DhLNILggME-451U8a10uRr4V9wThuzGxOBHnynY7_TGgDTHESNoNerXNECRQXub7oCyNRNpHX4NbpKnTLf46X5MWt7OFuDkY8hrsqDJskFtiKPuj9MeBztw6UPiWvg2qwcIXi-OHo0yF_jHDxYlzE3jY0bch9vIFvx-cQKad9XPT4n5iLfdOCmf5eM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طواف پیکرهای اعضای شهید خانوادۀ ابرمرد شهید تاریخ به دور ضریح امام رضا(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/669324" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669323">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddbc94faed.mp4?token=RVMV_1SauXiDsVz_Vcmu1YwfAibHWUvfMMiSIx9DGCVKnGKmER9ByvFgg4iyMM2w65bzUB-SoOpMoDD_pvqq_NA8_1jQ2rm-jznNu3m-rE7lLyUSew80TyFFuNE6EvbBKY3hUTtiseYvUNVmjURE85Fp7ascNtj5hsHzOC0zKAyV9gp1T60KFcYAScdrlH9_KqoESFfNosz4Ae0iCTV-2NVDAmw5cjpwIAPYe2vZThSEQYVyPHyht1RRDeipbfwNdJt3Exal1SAgdHA1uK2cVeeJRMgECdpIdnt4MuSVcSonrNPaNGcQ5yl1iyhohclTwmYbW3cILIwZYHOLAQa3ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddbc94faed.mp4?token=RVMV_1SauXiDsVz_Vcmu1YwfAibHWUvfMMiSIx9DGCVKnGKmER9ByvFgg4iyMM2w65bzUB-SoOpMoDD_pvqq_NA8_1jQ2rm-jznNu3m-rE7lLyUSew80TyFFuNE6EvbBKY3hUTtiseYvUNVmjURE85Fp7ascNtj5hsHzOC0zKAyV9gp1T60KFcYAScdrlH9_KqoESFfNosz4Ae0iCTV-2NVDAmw5cjpwIAPYe2vZThSEQYVyPHyht1RRDeipbfwNdJt3Exal1SAgdHA1uK2cVeeJRMgECdpIdnt4MuSVcSonrNPaNGcQ5yl1iyhohclTwmYbW3cILIwZYHOLAQa3ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوهٔ ۱۴ ماههٔ رهبر شهید به آغوش امام رضا رسید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/669323" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669322">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab92d02555.mp4?token=neP6w4lkr7vF3DRu8PNax76QdgErfhMudyGdFmuw3ImrDJ1KfkDoOihkeleFB88Ld011r0Ll9EizdQlHQOijqI8eQuPg_gzZfpXldWeMgQkx0gDTlbFCuQIqEOO8JM6EGlPVQ-hrhfnulCL0KfhU7vu-_58dqy4h4IO1u5SKTVBaflCfK-Tq0YYegVJ3NTue908W8uzPOiL6TfXX_qLNhAc4fxQwQWo1yadUypMPR_EN1TuJyDDT9rmJ9C06-QuNtHXT6d4NW_dBEd0waFOjzTS6PJ3eYff8JxJ3W47UgkZahr_XG6FJ9dXtPbUBoZIXabj9fwipp-_QIB069K_b8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab92d02555.mp4?token=neP6w4lkr7vF3DRu8PNax76QdgErfhMudyGdFmuw3ImrDJ1KfkDoOihkeleFB88Ld011r0Ll9EizdQlHQOijqI8eQuPg_gzZfpXldWeMgQkx0gDTlbFCuQIqEOO8JM6EGlPVQ-hrhfnulCL0KfhU7vu-_58dqy4h4IO1u5SKTVBaflCfK-Tq0YYegVJ3NTue908W8uzPOiL6TfXX_qLNhAc4fxQwQWo1yadUypMPR_EN1TuJyDDT9rmJ9C06-QuNtHXT6d4NW_dBEd0waFOjzTS6PJ3eYff8JxJ3W47UgkZahr_XG6FJ9dXtPbUBoZIXabj9fwipp-_QIB069K_b8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روضه محمود کریمی در فراق رهبر شهید و گریه بی‌امان خدام
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/669322" target="_blank">📅 00:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669321">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyCKgxIjJGT4h0fvvONkSx2RD5iyUzqBz4VQmVJILRshsHg4lRY-XOvOUpdrSoBwXaV4b-MHVoiwgkTIYFNVt3fY1TO4iG_yDe_1p8vt0m-v0TWj_foGxXtTlzGzoZPsaLNKqd2l_zsDtkjJq9Q_Jb4VGuhOSabpoo2ylXrxVYXbbPW1dNlAJ2xP1sN-0OQprn64KVAgLozbIAyyUNevbeOsJu3op3e86Xk0E4298M874ZLDCtTy7QE9AMg6uLOBOAB5gsilHQ4Zzxhgmb2j-KonXt4IxLjC206ryrUBYJg1BFWDkSNPhYPl_vZtXbxHIEqdhpV2qEoQLqoDQFxcyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام رزمندگان پای لانچر به مردم: خدا را شکر که جای خالی ما را در تشییع امام شهید پر کردید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/669321" target="_blank">📅 00:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669320">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqIUe8_POMDzUQJo6SitEMP2wvylI4VTHKOw5LLXAcytBFDElELapbMrcDrmQOe_NLqgTxqpyrcuTwrxBfiXI0chjN1lhs1DqCkkHAnyUZci8XK57X2iGOy4Nv7aLZpthbwnrFd124gv7wULV6fOBv7-P_7UOs1hdZ7Ula1f_V95WTfiNhzeW-u1hJEZ7eITGkfi2guEGFy0D5ySeCDPLkxDwcxVhhEj6wnfw9df4x-CH7IdWSSlG82Bgq5CyULpCgbc2fCR7LMCTtE9FkwfRhb9EfWbRM4l9k5CO444HQ4EptJZVSkA7-vlSEW0phctVGLRBpBDvWXXj8mrUp0KeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر شهید در آغوش امام رضا(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/669320" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669319">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/361a464c64.mp4?token=EBhMHrZAQIKztoAh0VS5OmxSscDJoW7qAfMAXw6Da1KN5Vnl2WMwzq8OM7oonbJCMhKLsNko9on99Yk5BwHkaUhOmfySRXDCfwz5E8SUdkuOiuR4OkEvjox9yxI2AMW96_APhW0aSQoMawBQfQVYI4Q7cTEmf7rP8jgk46-lFVg3qwId9ZrHxKKdBEcpzNjyjDp-EGaY2PKLOh7WpDXU35afed1Wob7d-KVv7IfixJpY_L-NbRb1iLFK45Mu0_wKJC08Qb2vJvBf85IDWoC893brG5lvgmtv6LoKswsYcsGS_jr9PbGupupmaQ-RJNqC1Oi0Z34tc8PkEtNLR9Dicrh-fcTGoUukM4HTrqogaMWj3RRiJOJ84oeBVtqt6pGj6o51cfx47oNm457rzjTw1TT0kIfh5h_BXW6KJW_KDn6tiE5C0Ku7W7C-Tk06Ss8S-5lb_uEMuCJKkhPFbiDxv06YpPc9g0XW6ipishwffmu66Bx8AF4AQkGmUFY1adXnInPQjvmZUPooaw6jxLyOI7rCPr2kvvHgHWAgy_-8SitTxpczg6RIyKXx-Yk6BQKnalcsaweEBJAatqR7635YhV62Zq_G6gw9evmFfyKpOd6yW3ij3r0UCi5AI7pFq-_RgS_HVebRKBpVr0a7JrhfXVr74VMUW44AT8A4ip4IOx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/361a464c64.mp4?token=EBhMHrZAQIKztoAh0VS5OmxSscDJoW7qAfMAXw6Da1KN5Vnl2WMwzq8OM7oonbJCMhKLsNko9on99Yk5BwHkaUhOmfySRXDCfwz5E8SUdkuOiuR4OkEvjox9yxI2AMW96_APhW0aSQoMawBQfQVYI4Q7cTEmf7rP8jgk46-lFVg3qwId9ZrHxKKdBEcpzNjyjDp-EGaY2PKLOh7WpDXU35afed1Wob7d-KVv7IfixJpY_L-NbRb1iLFK45Mu0_wKJC08Qb2vJvBf85IDWoC893brG5lvgmtv6LoKswsYcsGS_jr9PbGupupmaQ-RJNqC1Oi0Z34tc8PkEtNLR9Dicrh-fcTGoUukM4HTrqogaMWj3RRiJOJ84oeBVtqt6pGj6o51cfx47oNm457rzjTw1TT0kIfh5h_BXW6KJW_KDn6tiE5C0Ku7W7C-Tk06Ss8S-5lb_uEMuCJKkhPFbiDxv06YpPc9g0XW6ipishwffmu66Bx8AF4AQkGmUFY1adXnInPQjvmZUPooaw6jxLyOI7rCPr2kvvHgHWAgy_-8SitTxpczg6RIyKXx-Yk6BQKnalcsaweEBJAatqR7635YhV62Zq_G6gw9evmFfyKpOd6yW3ij3r0UCi5AI7pFq-_RgS_HVebRKBpVr0a7JrhfXVr74VMUW44AT8A4ip4IOx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر رهبر شهید روی دستان خادمان حرم امام رضا(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/669319" target="_blank">📅 00:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669318">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23fc6307b0.mp4?token=szEj-iINWz6R4XAu6GnzdYR6nmoNE9PscxIiZatYzlBrR334BVS7rvA8p4kiy8Bz4ZEyv4qbk-CY0mlslcJ60JGANUIzzkOZXm6FWtJOoRmy7dA5SC8LKzdZOQlvqAqGwnEuGlpVvOTNIuNyA6wsfwBO93gaxhekbGnOsjjhWQ_qpoePsR9ZREIJ3HQaNMJUkBe92cunmaNqnBIkmfXKKBD6k8z9AKqtopvLG193NujJ70C77ObTddTxfyekvLYdI_HAZ1M-dar2eA42AnefjoFk8JuTCqdZdfknnvxk5G3JswCwEs-ePzNlvzd4B03TUxRJ79G_mcsLmQUtoniTYgbXncuntwrADWUHxjlwtGmag1Ukha6nfJPTLXk8qHWSC7QpQQA_jGN86Cb47VuPhK4Z0TO91vf82kv7AXN8UTbP_EiH9wj38Y-jVf1l7R8ygOYXWQNcy7yeKuLfCjbOkeJSgFk_93ixuQhqlkWuI7wHSaGmfqu3JEkyvBjjpn72bT4wXaufBDzhSTKY6y5T50rNMHjjkDz63o1Z9KnqzHXsKWHssJCH0h2fIjrybsD3nDVtJMhClw25QOaBSwWZXP-HrOJ3_S2ugFxHSOgt7dm2kgSeoaojPe-97LDpuoz3qEbfKWB4sP9vkFHZLl6_YfFZnhTWUWQmksFBfON_Z3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23fc6307b0.mp4?token=szEj-iINWz6R4XAu6GnzdYR6nmoNE9PscxIiZatYzlBrR334BVS7rvA8p4kiy8Bz4ZEyv4qbk-CY0mlslcJ60JGANUIzzkOZXm6FWtJOoRmy7dA5SC8LKzdZOQlvqAqGwnEuGlpVvOTNIuNyA6wsfwBO93gaxhekbGnOsjjhWQ_qpoePsR9ZREIJ3HQaNMJUkBe92cunmaNqnBIkmfXKKBD6k8z9AKqtopvLG193NujJ70C77ObTddTxfyekvLYdI_HAZ1M-dar2eA42AnefjoFk8JuTCqdZdfknnvxk5G3JswCwEs-ePzNlvzd4B03TUxRJ79G_mcsLmQUtoniTYgbXncuntwrADWUHxjlwtGmag1Ukha6nfJPTLXk8qHWSC7QpQQA_jGN86Cb47VuPhK4Z0TO91vf82kv7AXN8UTbP_EiH9wj38Y-jVf1l7R8ygOYXWQNcy7yeKuLfCjbOkeJSgFk_93ixuQhqlkWuI7wHSaGmfqu3JEkyvBjjpn72bT4wXaufBDzhSTKY6y5T50rNMHjjkDz63o1Z9KnqzHXsKWHssJCH0h2fIjrybsD3nDVtJMhClw25QOaBSwWZXP-HrOJ3_S2ugFxHSOgt7dm2kgSeoaojPe-97LDpuoz3qEbfKWB4sP9vkFHZLl6_YfFZnhTWUWQmksFBfON_Z3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از روضه حاج میثم مطیعی قبل از تدفین پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/669318" target="_blank">📅 00:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669317">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaLr7ayjD-ztWWXYWNJeCuv5y5ctiBMGptnoEgOw4KN5mCmB1t3fd44aUiiQe-CJGGuqOASv2yxv_DNx4eOFITE8IkpgyuDPaMdpv7G8f8qK25szDkl0tI8GaCgBP_XcenBbX7nFwe5QZozM9Yh8eY1MIUrM7W75FzUEr2WcYuLUwUCT8B5G5yPOGIwEkdn53vdfO8Yr35O0XAPayzn4t91c6pd3RSwEJeD6H3OZri-VGyDrAss2mFxQIDdmnjegP-QlawSzALZZjzZnoznRwlzlk5jodfTHbU3qpc18GJNT5mqaRGU23MJNovWCwmudBraOcSpFLTl839NL2P5Zig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
رئیس خدام آستان قدس رضوی، امشب مهمان خاص امام رضاست
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/669317" target="_blank">📅 00:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669316">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYgqYE1_oGYwDSHoYDvVlBzbdPAggJS-t6E7NYRDCcs6aRoC0OnI_MfUpX39NYXy6w3jb_AJzFhq009_hwavOBKxNqkjKdQNoEOuWqZhec7aXSv7a_vJOvNYZtHX-6ilX8DD0a7gCBXELa6gL1J2Pb5EYuaQR0r1Cxfip0PPkzwDNN35ZmCx3lf8_c9WzAPI688VM5CDbsloRG9gb3hVf3WifNBTsUWgqtqw5U00szsUqGJR90HN0tObdKsHYtthUtq3rbaz52pVClqMLDgLUdjCjhmHqTbPhHj5POsINwCI_kGWxbfSXJ-E4Dvp41pd9uvmQiGCvzIvE5EHwAKSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور علی اصغر حجازی، قائم مقام دفتر رهبر شهید در مراسم تشییع و تدفین رهبر مسلمانان جهان در مشهد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/669316" target="_blank">📅 00:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669315">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f920723e4a.mp4?token=Pnr8BpE3N-i6dnjSbeVljOaozw_MUQclkKuUyUxHVdoj0_VyBcTZcI8cVKzs4oLPDA2uygqDJQNjr7_XzYhxfLBlThdbxHKqkTQa4de4xrIJ_QhJ9csyIoaGXCRwSGX_IoB_xzbxmF0ePj85XwI9w4mmPaIFG730OAFprrKxNWVtrEnI_EfEFyK8niKmL5of_3mmwKclE4S2g6fDXKEsh4Irz5ILOqX45mP70m3jeCIkW7D-FqGEp_Gi0bVeXF-WNIcu9e-BmPIzJ0LOSog9NH3VJO7wPMGxglWFsquO7tNkc1GWog0olVf2Abotv47Qqpaxm0TDIWEXgIdYMJ1GBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f920723e4a.mp4?token=Pnr8BpE3N-i6dnjSbeVljOaozw_MUQclkKuUyUxHVdoj0_VyBcTZcI8cVKzs4oLPDA2uygqDJQNjr7_XzYhxfLBlThdbxHKqkTQa4de4xrIJ_QhJ9csyIoaGXCRwSGX_IoB_xzbxmF0ePj85XwI9w4mmPaIFG730OAFprrKxNWVtrEnI_EfEFyK8niKmL5of_3mmwKclE4S2g6fDXKEsh4Irz5ILOqX45mP70m3jeCIkW7D-FqGEp_Gi0bVeXF-WNIcu9e-BmPIzJ0LOSog9NH3VJO7wPMGxglWFsquO7tNkc1GWog0olVf2Abotv47Qqpaxm0TDIWEXgIdYMJ1GBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مهار پنالتی امباپه توسط یاسین بونو
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/669315" target="_blank">📅 00:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669314">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3FXIYE2aLtwZvP8ndygRl1OEpDqq4WrCh5HwEJiigg2Nk-7bX0BprBv1XpCmmADQkd26ZA0tOMHyKmQ6xy57LQgtVTuzeLmXQVB2EZpb-6eedhDFm1QGcY6rqfNKn8hMuOJWWjXjd84qc-JGpijOdhE4Y7d3AdSGiCtEsy1rXSr1sb4eNYeS2NzOr0QcU1zQ-EM-438jN7AsmWwIFobm-SYW9oY9NVY3cGjI4J1UmApi7ovsvEIdHYJz48HoEhSsg6ts804Lf8Zb58rBiW-GcE_d2gXI_Yb0cMkcJl0NmQkCp-Oynt5KKvYiKvO8UzQBJo0KjTjLblb4jk6VFvoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار | شروع مجدد جنگ و نوسان شدید طلا
⚠️
در جنگ دوازده روزه و هم در جنگ چهل روزه طلا ریزش بسیار شدیدی را تجربه کرد
❗️
این دفعه مجدد جنگ شروع بشود آیا قیمت طلا به گرمی
1
4
میلیون می‌رسد و دوباره قمیت
ملک
شدیداً رشد می‌کند؟
تحلیل تخصصی منتشر شد!! روی لینک زیر کلیک کن و تحلیل رو ببین تا دوباره ضرر نکنی.
⬇️
⬇️
⬇️
دریافت رایگان تحلیل طلا و ملک</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/669314" target="_blank">📅 00:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669313">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3SvtjCnCo5R8iZPTiNusxgpOZj-pz6tRtH5voJTYJgA_IdmF7elDIGJujcDv9hP3Nbzhs24Kyoe25weTsrl76cXCwRC_DW_O6uB1ViAfhwyh-LVfk9fMPj0eUkFUMLU4sB-g5jaTzUbESGzixcp3hSgPGq3M87yMl66stgBDzs_7sKXU5qLBv0lyIwiRQD53NLbKASEII_XEoJ6NxYeqXl9sqX5j1gUUXa-yiSmiQoN07x58-kBWzufqLCZTsFlIen0aP9Z_HA7BH4NAj9B_bPKjxzCbVhsNUAtyU9krGLcZzwu2dJCAiM6tqqa-VUDm1Ff_InY56x3dv2iMXjaGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/669313" target="_blank">📅 00:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669312">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-text">📢
به اطلاع ملت بزرگ ایران و امّت اسلامی میرساند:
▪️
پس از مراسم تشییع پیکر مطهر رهبر شهید انقلاب اسلامی اعلی‌الله‌مقامه‌الشریف در مشهد مقدس و اقامه‌ی نماز بر پیکر ایشان در صحن پیامبر اعظم صلوات‌الله‌علیه‌وآله،
هم‌اکنون برنامه‌ی وداع خانواده مکرم رهبر شهید انقلاب با پیکر مطهر ایشان در حال برگزاری است و هنوز تدفین پیکر مطهر هنوز انجام نشده است.
👈
پس از انجام تدفین پیکر مطهر، اطلاع‌رسانی لازم برای انجام اعمال و نماز لیلةالدفن از رسانه‌ی
KHAMENEI.IR
انجام خواهد شد.
🏴
#باید_برخاست
🖥
Farsi.Khamenei.ir</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/669312" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669311">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
فرماندار کنارک: منطقه نظامی نیروی دریایی در دو مرحله هدف حمله دشمن قرار
گرفته است
فرماندار
کنارک
:
🔹
منطقه نظامی نیروی دریایی شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.
🔹
دستگاه‌های مسئول، نیروهای امدادی و نیروهای امنیتی بلافاصله در محل حادثه حاضر شدند و بررسی ابعاد و جزئیات این حمله در دستور کار قرار دارد./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/669311" target="_blank">📅 23:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669310">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
عربستان به‌دنبال حذف اسرائیل از کریدور آیمک
شبکه عبری‌زبان «آی۲۴»:
🔹
عربستان سعودی در تلاش است تا اسرائیل را از پروژه کریدور اقتصادی هند-خاورمیانه-اروپا (IMEC) کنار گذاشته و مسیر آن را به سمت سوریه و ترکیه تغییر دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/669310" target="_blank">📅 23:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669309">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
فارس: اولین برآوردها از میزان شرکت‌کنندگان در تشییع رهبر شهید انقلاب ۴۱ تا ۴۳ میلیون نفر است
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/669309" target="_blank">📅 23:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669308">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09749751ad.mp4?token=YDIoXYkMUoSQZqBFXMqp288OegGWS2njIsiWXuSTy2l-hUCMe_Pu4PmiIg711-axm0VLH7wd9POrkEoh7jw3yi3X1FALZnz9DEujuHG9sAcxmo2sCzoilPxSwfWiaAs2t7rRFGekHNtZeVPxEqE6Ge0rI6ST9vt0a3gR_ZIDWniNA1DG48GBvNWRGI5BXtdhi04CUGpJvJl4mKYCLqMmpV8fbxQEluOPkzwT6mjItpDMfOkWgp-LEukmEd8iWpuo2ypQpOYHguG377VfIgQ0R_QEkQez1DkcV5et49dB1LZgutvt4Of_Quv-YeljE1KhG__rhUrZHqXytveiKWGbIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09749751ad.mp4?token=YDIoXYkMUoSQZqBFXMqp288OegGWS2njIsiWXuSTy2l-hUCMe_Pu4PmiIg711-axm0VLH7wd9POrkEoh7jw3yi3X1FALZnz9DEujuHG9sAcxmo2sCzoilPxSwfWiaAs2t7rRFGekHNtZeVPxEqE6Ge0rI6ST9vt0a3gR_ZIDWniNA1DG48GBvNWRGI5BXtdhi04CUGpJvJl4mKYCLqMmpV8fbxQEluOPkzwT6mjItpDMfOkWgp-LEukmEd8iWpuo2ypQpOYHguG377VfIgQ0R_QEkQez1DkcV5et49dB1LZgutvt4Of_Quv-YeljE1KhG__rhUrZHqXytveiKWGbIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا دقایقی دیگر خانواده با رهبر شهید وداع می‌کنند
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/669308" target="_blank">📅 23:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669307">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa04b01c83.mp4?token=n1LE8ox3occzNcfS-Nk5T6NeA1JETjo2ljv9bLi_M8dDpzbDUs-GNS4IUWfAlCF9VzG6ni11KGArd1hO288w-_gb_nGQF3PAiV6IkVUSJ0cAZ5CDtj_ZkaFAUblSa-v6s92Truk7DCvzlcbPIRqABhDXNcnNXODpD6xSi2mm6DHYn1AmZJm9kIHnaAklRC4AuizvyyefX0_UscZi2yf58vd_LGeywf14-9Ck6F_WDofMi7UoIxZR3LaykH2LYIdY45mdM-pWMkOFhCnyNerPuiQrOMcDPzpyG3Bfz3ts04Y8NkKxUAssWM3IiMO4Gl4-450pvbln7Ha0kgVQrPcIJzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa04b01c83.mp4?token=n1LE8ox3occzNcfS-Nk5T6NeA1JETjo2ljv9bLi_M8dDpzbDUs-GNS4IUWfAlCF9VzG6ni11KGArd1hO288w-_gb_nGQF3PAiV6IkVUSJ0cAZ5CDtj_ZkaFAUblSa-v6s92Truk7DCvzlcbPIRqABhDXNcnNXODpD6xSi2mm6DHYn1AmZJm9kIHnaAklRC4AuizvyyefX0_UscZi2yf58vd_LGeywf14-9Ck6F_WDofMi7UoIxZR3LaykH2LYIdY45mdM-pWMkOFhCnyNerPuiQrOMcDPzpyG3Bfz3ts04Y8NkKxUAssWM3IiMO4Gl4-450pvbln7Ha0kgVQrPcIJzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#باید_برخاست
♦️
در مسیر وداع با رهبر شهید ایران، آتش‌نشانان مشهد با دل‌هایی داغدار و دستانی خدمتگزار، گرمای راه را از زائران گرفتند تا سهمشان از این بدرقه باشکوه، خدمت بی‌منت باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/669307" target="_blank">📅 23:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669306">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4ee86ff9.mp4?token=FSk7y8LIB95sMOERsaCeGpkxzGsMbv8vPDJXtdwQkcIhNjeO_vONi5QJfsdrAjiEv1D08UpZjkP-U8of-ovAKPnQcCx_8qkKHeRAst2eueNoLODZ5CRrkRBBIJI47M49bWGK7Hs6FiPZRtgLXtq_8v7sEWHQvTTn9n3VFMK-vPyzKmZBhulUjgzJDuxGcgf-8M23bBTjPGEs2sUrt65nCJaoLmo-KDfFjw8z26CsMGugBlxS-NI0bDR4_sp4eZFzsH52JUs9HGfAIyvCoXVL1X3JpFN6mcszmyzfwmUW6XnUk5cU1urG28sWN_y-BDaaa-r3eZKh91o4Mkzwq3YZZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4ee86ff9.mp4?token=FSk7y8LIB95sMOERsaCeGpkxzGsMbv8vPDJXtdwQkcIhNjeO_vONi5QJfsdrAjiEv1D08UpZjkP-U8of-ovAKPnQcCx_8qkKHeRAst2eueNoLODZ5CRrkRBBIJI47M49bWGK7Hs6FiPZRtgLXtq_8v7sEWHQvTTn9n3VFMK-vPyzKmZBhulUjgzJDuxGcgf-8M23bBTjPGEs2sUrt65nCJaoLmo-KDfFjw8z26CsMGugBlxS-NI0bDR4_sp4eZFzsH52JUs9HGfAIyvCoXVL1X3JpFN6mcszmyzfwmUW6XnUk5cU1urG28sWN_y-BDaaa-r3eZKh91o4Mkzwq3YZZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار کشتن ترامپ هم‌اکنون در اجتماع شام غریبان رهبر شهید انقلاب در میدان احمدآباد مشهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/669306" target="_blank">📅 23:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669305">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔹
از خبرهای پُربازدید امروز وبسایت خبرفوری غافل نمانید
🔹
🔹
نماز بر پیکر آقای شهید ایران به امامت فرزند ایشان
👇
khabarfoori.com/fa/tiny/news-3228909
🔹
صدای انفجار در چند شهر جنوبی ایران؛ آمریکا: ما نبودیم
👇
khabarfoori.com/fa/tiny/news-3229100
🔹
تصاویر از داخل خانه رهبر شهید
👇
khabarfoori.com/fa/tiny/news-3229045
🔹
وفاداری هالند به نامزدش، زبان‌زد دنیا شد/ عکس
👇
khabarfoori.com/fa/tiny/news-3229043
🔹
توهین‌های ترامپ دوباره احمدی‌نژاد را وایرال کرد
👇
khabarfoori.com/fa/tiny/news-3229101
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/669305" target="_blank">📅 23:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669304">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
نتانیاهو: جنگ هنوز به‌طور کامل تمام نشده و اسرائیل برای هر سناریویی آمادگی کامل دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/669304" target="_blank">📅 23:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669303">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
نتانیاهو با خوک زرد تماس گرفت
دفتر نتانیاهو:
🔹
نخست‌وزیر و رئیس‌جمهور آمریکا در یک تماس تلفنی، در چارچوب ارتباطات مستمر، با یکدیگر گفتگو کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/669303" target="_blank">📅 23:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669302">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
سناتور دموکرات: تصرف خارگ خطر از دست رفتن صدها سرباز آمریکایی را همراه دارد
کریس کونز:
🔹
تصرف جزیرهٔ خارک برای ایالات متحده بسیار دشوار خواهد بود، زیرا خطر از دست دادن صدها سرباز وجود دارد، چرا که این جزیره در گوشهٔ شمال‌غربی خلیج‌فارس، نزدیک به ایران قرار دارد، و ما باید درگیری سنگینی را انجام دهیم و جان بسیاری را به خطر بیندازیم تا بتوانیم جزیرهٔ خارگ را تصرف کنیم. /سی‌ان‌ان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/669302" target="_blank">📅 23:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669301">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2b858c81.mp4?token=ioplanmGPR-1rQMuJnp6N_hlSYrlNQgbh2Yc_6CK0ybjsAw9D861bmyHb1kUh3ZTkbeYj6rvf6-2tGzmn_8uUe2uJf05GE1gjleO4_iAeM7Nox9N3Wc8gVFBDl5ReE6PH0XhTn6iamt3_zFXbL90DlE-2QAYLE3eppC3Dx279aSNc1zdoEizdKASqovnHTylFYaowk6IvEeTT9nEij2uSawdBEAW7id_XySu7Hys3U97oWVMCnkhAivfdrSo2wgVkeM6J9nczH26zePnAGA5pGKDBBVa5UTuUo5xORFw1GEoN4QTUvrGxVu9J47ZM7w8K9VB2SuGYwAg7rqQ-UxNCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2b858c81.mp4?token=ioplanmGPR-1rQMuJnp6N_hlSYrlNQgbh2Yc_6CK0ybjsAw9D861bmyHb1kUh3ZTkbeYj6rvf6-2tGzmn_8uUe2uJf05GE1gjleO4_iAeM7Nox9N3Wc8gVFBDl5ReE6PH0XhTn6iamt3_zFXbL90DlE-2QAYLE3eppC3Dx279aSNc1zdoEizdKASqovnHTylFYaowk6IvEeTT9nEij2uSawdBEAW7id_XySu7Hys3U97oWVMCnkhAivfdrSo2wgVkeM6J9nczH26zePnAGA5pGKDBBVa5UTuUo5xORFw1GEoN4QTUvrGxVu9J47ZM7w8K9VB2SuGYwAg7rqQ-UxNCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون رونمایی از لگوی غول‌آسای ترامپ در مراسم شام غریبان قائد امت در میدان احمدآباد مشهد @AkhbareFori</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/669301" target="_blank">📅 23:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669300">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
صداوسیما: اقامۀ نماز لیلةالدفن پس از خاکسپاری پیکر شهدا انجام خواهد شد
🔹
به محض خاکسپاری پیکر مطهر رهبر شهید ایران و شهدای خانواده ایشان، اطلاع رسانی می‌شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/669300" target="_blank">📅 23:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669299">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvFwVBc71ynneEj3lWl8Rjw0zKF3fuqo06G3SMVCQ2j0AT5WskmEs12HyR1cAUDT7nfUaOyiIM-ZY2Nm7tcce9uMtMYYg7EbxEm_j0moZDG9RsVRzZfQ9I0fIpC3OaYpa4ahr0cWFwtet7EFLhqgEXzz08qnTlAvtlWK_bFPauokbQhkwW77-Iq_3uezOv48x51Ej05SEo_GoE1TmEccfmsABuzPuSaKK4YIG08lMU4C2vCMazDB3pR0eWfLhtGlOjSJr8VVP75awIot4nkly048IEkdt-c0EYfKFTRoEZ39b9Zhntd_k77FVMQhoq6qHxueKQqG9V3Q1hXOXiXgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/669299" target="_blank">📅 23:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669298">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/votheEcISiXDMpSMOGw74WQ1IBmB5G9cXdN194b7noIEQK0GzdDPSL30Cr01wIpMyunYNFYpsumEzXJiLEgnjWFQ5_qub6FxADyvixqdjvCtX8wmU8tEZ_wXMuXZiyY6fXUJTTXhWGdsaH88hEdLrt5jmHYrXKgnymkJzG4YKw3pdBho5YtdTXav9Ma-5MEw7vWQKJ0w5oRuEsbbq2A-g9PWMQV3EhOrT2zwuKyoGuNpVE3QLvGBCTlkEo487Y-bCSn_tcvk_Ob9mvJJoYJQW4Mn2u5GbflUFaXVULfvoTj5Y2iB7UGOX1xeBpKgNMuFhLHbBPN4dJUHUra7rieaPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازتاب جهانی تشییع ابرمرد شهید تاریخ
خبرگزاری پرس تراست هند:
🔹
ایرانیان با چشمانی اشکبار در مشهد برای آخرین بار با آیت‌الله علی خامنه‌ای، رهبر شهید، وداع کردند
.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/669298" target="_blank">📅 23:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669294">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d4f26adf.mp4?token=WeEFHeVwuEPhebrmX-ejU4aFGFLCq3q-4ZAc_xXH_u2wE_xcZnc1mCscwUrb7_DYrIMXoVD49_vzjYtWaKi1qYftfCMgHO6MCtKps8ssrIo0dq5Lw0d8boywPdEC-HE8JGnbVmKAB9ygK3daR5smbgV3A0PUadbttzs67EWArFYsDCLu6rhnDXXgzUumVGauG1SMWJbXyQCnDk1JV_o85ZIUxOhjfffgGUqSxqPWMmVV7SZZjqxWwRSJSVzh-hsxP40XFUK6m6bkI03bwwuFqZXa0d7GXaQIbOXUttDqIffdUMdefOUaRmr1lP1K7NwLmeQu7dwr9-adMDodMtoEYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d4f26adf.mp4?token=WeEFHeVwuEPhebrmX-ejU4aFGFLCq3q-4ZAc_xXH_u2wE_xcZnc1mCscwUrb7_DYrIMXoVD49_vzjYtWaKi1qYftfCMgHO6MCtKps8ssrIo0dq5Lw0d8boywPdEC-HE8JGnbVmKAB9ygK3daR5smbgV3A0PUadbttzs67EWArFYsDCLu6rhnDXXgzUumVGauG1SMWJbXyQCnDk1JV_o85ZIUxOhjfffgGUqSxqPWMmVV7SZZjqxWwRSJSVzh-hsxP40XFUK6m6bkI03bwwuFqZXa0d7GXaQIbOXUttDqIffdUMdefOUaRmr1lP1K7NwLmeQu7dwr9-adMDodMtoEYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از مراسم شام غریبان امام شهید با حضور پرشور مردم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/669294" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669293">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7XgBfjo2DhUYLCy6vH6EmuiXyIKVopXr2CJa5M-Cg1AQiP3dlGWw2px-v1iAWzlZAueY042npEwUn62RatFP_i4yQiteDf0tfDnKcsTpfsDaBMFFtGSDE_vEIFUKrCLOPt_fnTV4UDUbzq83rG_U5lwqRrpAPLlOjA0oDpGwIjEvT7RhEMiV64q-euYY9TbBscFmd4lkQFL_ba3te5XNXAGM5R53RGN-LAQYFRzmOQM1fACyjscqYxwc7pgc-ZZ6fsLOP4ph-E_nkGWAUziUpaxxdV8k4QEIdmxBPwBhWT4eQZJx654_hW6SQzB4AYRas55mGLmCDpTjLHf11JS6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در آستانه برگزاری آیین باشکوه تشییع پیکر مطهر رهبر شهید انقلاب صورت گرفت
🔹
فعالیت فروشگاه‌های «شهرما» برای تأمین اقلام اساسی و معیشتی زائران و مجاوران در مشهد مقدس
🔹
هم‌زمان با آماده‌سازی پایتخت معنوی ایران برای وداع تاریخی با پیکر مطهر رهبر شهید انقلاب و تشرف خیل عظیم دلدادگان به مشهدالرضا (ع)، سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد ظرفیت زنجیره فروشگاهی «شهرما» را برای عرضه گسترده و تسهیل در تأمین مایحتاج ضروری زائران و مجاوران فعال کرد.
🔹
به گزارش روابط عمومی سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد: «با توجه به حضور پرشور و گسترده عزاداران در پهنه کلان‌شهر مشهد، ۱۴ فروشگاه “شهرما” در سطح شهر با هدف عرضه کالاهای اساسی و تأمین ارزاق عمومی زائران و مجاوران، تمهیدات ویژه‌ای را در دستور کار قرار داده‌اند. در همین راستا، به‌منظور رفاه حال بیشتر زائران و مجاوران گرامی، ساعت کاری این فروشگاه‌ها برای خدمت‌رسانی بهتر، از ساعت ۸ صبح الی ۲۲ (۱۰ شب) تنظیم شده است.»
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/669293" target="_blank">📅 22:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669292">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
منشا صدای انفجار در بوشهر در دست بررسی است
🔹
فرماندار بوشهر ضمن تایید شنیده شدن صدا در بوشهر و چغادک گفت: اینکه صدای شنیده شده از منشا پدافند نیروهای مسلح، اصابت پرتابه دشمن به مناطق یا هدف قرارگرفتن پهپاد دشمن بوده همچنان در دست بررسی است و علت قطعی آن…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/669292" target="_blank">📅 22:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669285">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fE6D4HjkClPtJApYgthjtKOb--WyEQiOc2r0kg5YtxsDgvWE3yWiIbilB6lCrfjgr0avsM235qYsyIWMCMkpcTlyLFdZ9NndhXt8YauYFF4ewMJ3qyOqAPTxDUOGCllvE0qPNpLWxJyccg0f1GHmG5FCsQQ4zRi2xWnm0iMyDRNNA7ShPwvyu-yQkzIPZlnbQGo1JsdenGMUyD9Ez-z0A7ss7dq2T0Ties1Q99LawN0OXARiq-Rrs_gG6ecbmA-XPWBNdEOa0qmgUxOyAAJQBdQy7fZtJoITWZeIuM7tLFAtp-b__dQGHevZHEJJf55JaX8Rxmmupchg4AwrLXB5TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ ایران به بیانیه ناتو: اتهامات درباره برنامه هسته‌ای و تنگه هرمز مردود است
🔹
در این بیانیه تأکید شده است که برنامه هسته‌ای ایران کاملاً صلح‌آمیز بوده و ایران به‌عنوان عضو معاهده منع گسترش سلاح‌های هسته‌ای (NPT)، بارها اعلام کرده سلاح هسته‌ای هیچ جایگاهی در دکترین دفاعی کشور ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/669285" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669284">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d897623a.mp4?token=DytYjxDcxQzWq6HLzw0vUbOotWfNcpnBi-zn5DHKd-WOUrjJ9_LZ-lvrOnoPJ5evM5wmeiIQKj3a3qUO-Pn3NM4fT0WkLb2xHoQzF62rHwjKYCpMXPlaW-CGMFa0ObCVo9RnKb4fVIk3cynu2AC7rpmD7FHwWdXeBryKa5ilwn3vpVcYP604PK2rBascKQvjvohniiP4lGQDpW-8kDbvLoMytb6kZ9YXR0IFZPJgNUJKgl6SH_E2rQ44u5A8ygrZKKC9Z5nXQRWc8B2czdGzt3nWSBxrMVplvo2OSqeW5z7eTIk4AIliEof8AEgzLRA6Y2tUIDGYySsNBHLHdj3Yag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d897623a.mp4?token=DytYjxDcxQzWq6HLzw0vUbOotWfNcpnBi-zn5DHKd-WOUrjJ9_LZ-lvrOnoPJ5evM5wmeiIQKj3a3qUO-Pn3NM4fT0WkLb2xHoQzF62rHwjKYCpMXPlaW-CGMFa0ObCVo9RnKb4fVIk3cynu2AC7rpmD7FHwWdXeBryKa5ilwn3vpVcYP604PK2rBascKQvjvohniiP4lGQDpW-8kDbvLoMytb6kZ9YXR0IFZPJgNUJKgl6SH_E2rQ44u5A8ygrZKKC9Z5nXQRWc8B2czdGzt3nWSBxrMVplvo2OSqeW5z7eTIk4AIliEof8AEgzLRA6Y2tUIDGYySsNBHLHdj3Yag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شام غریبان رهبر شهید در خیابان‌های مشهد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/669284" target="_blank">📅 22:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669283">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH3fRyXUdKlFoJdXeKGQdZZqOmFJkDhNwR-LJz3mxdYzUPMXHFMEgCyUzMkkCF2C-M2BH4Y0aNcfURX7owmQU8XBl3Bo8soPXRc5q2ge1M-a7CBJ3CKbBQ58EbFflNGvuGjSSOyFKJaziT9tErwz9nGuli9h9B9MA5fQLYzuAvbMaHW_RcdQQh6lCBugfSj6LYhBctttlr4n67UUfaPhGSSFuhTTcOBfwB1kS-PblUFrZtvMcnOMljJpEkCuW5kSwrlXfCCqei6mx6f_LE9Oq6fa0SmEbX_3VfisJ8UItu2nq7K7ZIBcFz0yUu0q-MkYVXSTAv-hDy_AN2rbMPA0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جاودانه شد
🔹
تشییع باشکوه پیکر رهبر شهید انقلاب در میان خیل عظیم زائران و مجاوران حرم مطهر امام رضا(ع) در مشهد، صحنه‌ای ماندگار و تاریخی را رقم زد؛ آیینی که در حافظه ملت ایران جاودانه خواهد ماند. این مراسم در شرایطی برگزار شد که هم‌زمان، آمریکا بار دیگر حملات جنایتکارانه خود را از سر گرفته بود، اما این اقدامات نتوانست از شکوه بدرقه مردمی بکاهد. اکنون با آرام گرفتن پیکر رهبر شهید در جوار حضرت علی‌بن موسی‌الرضا(ع)، نام و راه ایشان نیز در کنار این بارگاه نورانی، به نمادی از ایثار، مقاومت و ماندگاری در تاریخ انقلاب اسلامی تبدیل شده و جاودانه شد.
🔹
ویژه‌نامه جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/669283" target="_blank">📅 22:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669282">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
صداوسیما: برخلاف برخی خبرهای منتشر شده در  فضای مجازی
،
تا این لحظه هیچ انفجاری در بندرعباس، قشم، سیریک و جاسک گزارش نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/669282" target="_blank">📅 22:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669281">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏
♦️
گزارش‌های تایید نشده از وقوع انفجار در اهواز و بوشهر/صابرین نیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/669281" target="_blank">📅 22:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669280">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
رسانه عربی نایا: احتمالا حملات امشب کار کویت و بحرین است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/669280" target="_blank">📅 22:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669279">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619ccc9a61.mp4?token=J9aUR2gw0HULGPqPIoy1Rc0dsdqTtD8iXgMdPpR1qtJlTGVy42ioCbslcCYNqHMQajBx3OdTzUH4lcd1wgIygaFuQMjOzKREVGloqyI-AElck-I-h1o1tyP6qwMUJPyc6I6BruwRAy06QkQRpIgMoAzCXJeCAOzcb_PZladjG8K8QSbrq9MQLfQrGwCkXkenuxyWenR1osTamCnxg64QD6V-tK8udAeQeJi4aBLhh6a_8fFOsZzxTM2uQY75CrOXiWepouyKm5phrnpqgexvGVvVYtLFvOTW-N6bRYR_QwQxgpnOSXHrNRBBYeJ-BbwtfIKJZV5wJ5agGWcVP9al1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619ccc9a61.mp4?token=J9aUR2gw0HULGPqPIoy1Rc0dsdqTtD8iXgMdPpR1qtJlTGVy42ioCbslcCYNqHMQajBx3OdTzUH4lcd1wgIygaFuQMjOzKREVGloqyI-AElck-I-h1o1tyP6qwMUJPyc6I6BruwRAy06QkQRpIgMoAzCXJeCAOzcb_PZladjG8K8QSbrq9MQLfQrGwCkXkenuxyWenR1osTamCnxg64QD6V-tK8udAeQeJi4aBLhh6a_8fFOsZzxTM2uQY75CrOXiWepouyKm5phrnpqgexvGVvVYtLFvOTW-N6bRYR_QwQxgpnOSXHrNRBBYeJ-BbwtfIKJZV5wJ5agGWcVP9al1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرم رضوی در ماتم
🔹
حضور مردم عزادار در حرم رضوی پس از اقامه نماز بر پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/669279" target="_blank">📅 22:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669278">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f0fb62bec.mp4?token=khWpIoQXRJBbpxqYHY7ku6tq_EoA-YpqN4u0ChGh7OdPoRS7qKBkMk6a-pyRhn19fI3LnYUUin3wJvaRvFjPM79Pt8tEmdZ7oDcPeJwH9l5cv76hiB21hw3mIr6bmv4DXNZyh3gDaQZW2IfbOUrOdCcBac9Fa9_4-Sq_nj2E06LqVsAt2wW08YbqattrDtc8kx8r-sTms9FlhVz0nMUu6ZwiwM_2pp-Nwq9JSJcAExcc2PDhXVHjyc_5BnYZvMjUsqUFFm2RJtn5H_RFL2Czgtqj0ipO0zr5wFVQ4OnRd7ncMNQq6lUHAq_Cc8CYuetw_1MyZpI_N8H2_ot-9daQBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f0fb62bec.mp4?token=khWpIoQXRJBbpxqYHY7ku6tq_EoA-YpqN4u0ChGh7OdPoRS7qKBkMk6a-pyRhn19fI3LnYUUin3wJvaRvFjPM79Pt8tEmdZ7oDcPeJwH9l5cv76hiB21hw3mIr6bmv4DXNZyh3gDaQZW2IfbOUrOdCcBac9Fa9_4-Sq_nj2E06LqVsAt2wW08YbqattrDtc8kx8r-sTms9FlhVz0nMUu6ZwiwM_2pp-Nwq9JSJcAExcc2PDhXVHjyc_5BnYZvMjUsqUFFm2RJtn5H_RFL2Czgtqj0ipO0zr5wFVQ4OnRd7ncMNQq6lUHAq_Cc8CYuetw_1MyZpI_N8H2_ot-9daQBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون رونمایی از لگوی غول‌آسای ترامپ در مراسم شام غریبان قائد امت در میدان احمدآباد مشهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/669278" target="_blank">📅 22:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669277">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
یک مقام آمریکایی به CNN گفته است که ارتش ایالات متحده در حال حاضر مشغول انجام حملات نظامی نیست./انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/669277" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669276">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ادعای آکسیوس به نقل از یک مقام آمریکایی: ما در حال حاضر هیچ ارتباطی با هیچ حمله‌ای به ایران نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/669276" target="_blank">📅 22:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669275">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
تاکنون دو انفجار در بوشهر و سه انفجار در چابهار شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/669275" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
