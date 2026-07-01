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
<img src="https://cdn4.telesco.pe/file/TKzzx13pQ25N9g9POIjlcvconfMgALIcTWtwV4OBNuhGcZZYkulVB1snPIMpNaqpDdVSl_cjziMJARugr5g2AQFUGhLIU1LR6pumS5yxuqqns5K91-3mW_B8VS1chc0HKpL2Rop9gLcqnJ8zsZxtcNeJF4LMnr2o0hJpYJsnt3gzLcHBpYzncTmLSQL5wb7VVPit-HvBRzEphRNonWtF8PcOy1GIQ6z31SVn2NzFnh2QKzv_gkQZJp7Ry2tzO-g08Ck0l_cUEHv55yoAh0ehS9KW0lGPUGPLpzkdtva02R1XZTCbj0-2wNQ0aa1v9C-0cFQFfu5CLY9Y8h2OfMHCsg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 944K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 17:41:53</div>
<hr>

<div class="tg-post" id="msg-131280">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
کاخ سفید به فاکس نیوز گفت:
رئیس جمهور ترامپ به روشنی گفته است که اگر ایران به سمت ما شلیک کند، تلافی خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/alonews/131280" target="_blank">📅 17:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131279">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ترامپ اعلام کرد که قصد دارد بخش عمده‌ای از اسناد و اطلاعات محرمانه دولت را از طبقه‌بندی خارج کرده و در دسترس عموم قرار دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/131279" target="_blank">📅 17:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131278">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c924191a.mp4?token=Vb1NPF_DBh7QUX0EUeeEf6SqsM4NHwDqBhLoQ5js9W2FXGFp09hT7wvq0X8bS_Dmp_WgdhuF5vCw9KheCGtstP97pao6X9YNSTMNRKlAOM1dNN6Tvvrt2tTKZW7TTnLLoQy4zQuI51kqL8fglhPi4b7OUmOtam9DV2f73U8VxXgiLvVMKTPhpOCH7w4y5x3JI--EHPZlKrjlGr1xlnGA1Us3DHSLgDTa37kdoBp2-TFX9Gyxv93dolGz4_MZDhIQsipyYj0z133qetcVA9Ey1k2o0ZnJswqy39k7P-hVD3OI-GTFVORGDnXw0UheIcGcXCLR5PrQYSmo5seQiolWrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c924191a.mp4?token=Vb1NPF_DBh7QUX0EUeeEf6SqsM4NHwDqBhLoQ5js9W2FXGFp09hT7wvq0X8bS_Dmp_WgdhuF5vCw9KheCGtstP97pao6X9YNSTMNRKlAOM1dNN6Tvvrt2tTKZW7TTnLLoQy4zQuI51kqL8fglhPi4b7OUmOtam9DV2f73U8VxXgiLvVMKTPhpOCH7w4y5x3JI--EHPZlKrjlGr1xlnGA1Us3DHSLgDTa37kdoBp2-TFX9Gyxv93dolGz4_MZDhIQsipyYj0z133qetcVA9Ey1k2o0ZnJswqy39k7P-hVD3OI-GTFVORGDnXw0UheIcGcXCLR5PrQYSmo5seQiolWrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو پربازدید از اظهارات سردار سعید قاسمی در مورد قالیباف سال ۹۸
🔴
قاسمی گفت قالیباف مانند حسن روحانی است و چه موقع جنگ ۸ساله چه الان به او بدبین هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/131278" target="_blank">📅 17:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131277">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY8iZmtiMeZWHZTBhzK4GIacgBiydji1bTiKrddzBUu6QyEpo0EaHXds5nfG3fmbAIv7MqpRIcc_v6XNNWIB9IDQDrq4GzvfMeM1Rgh35JxE8UqkpRiNok8fmvjOPtph_WGjzdAJEUfJJlMvN4AzihlZER5j2fDhJgp1FxpODNBUy8X18LpsYTxSGsR6uagYH99xEMfMXrRTOaP2KlEAjg7BmeH-WITv389UxNAZ5nIqVv99EYGfske0L8keSHmjgiO87qlsXKoEbeFh22TTdiDp_cFPJ6kVaVowKCUooX8bqORP0A19B6mrRXYHITtHrUTQ0qzt1Fe2uehPy0QRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قاسمیان، موسس شِلتر: باید هرجور شده اسرائیل رو نابود کنیم و مردم باید سختی رو تحمل کنن چون ثواب داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/131277" target="_blank">📅 17:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131276">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">دهم تیر، یادآور حماسه آرش کمانگیر و یکی از روزهای گرامی جشن کهن تیرگان است؛ روزی که نماد فداکاری، میهن‌دوستی، امید و پیروزی را در فرهنگ ایران‌زمین زنده نگه می‌دارد.
تیرگان، جشن آب، باران و آرزوهای نیک است و یادآور این حقیقت که با ایثار، همدلی و امید، می‌توان مرزهای ناامیدی را پشت سر گذاشت.
تیرگان خجسته باد؛
به امید روزهایی سرشار از شادی، برکت، سلامتی و سربلندی برای ایران و ایرانیان.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/131276" target="_blank">📅 16:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131275">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
رویترز: قیمت نفت خام آمریکا به ۶۸.۲۲ دلار در هر بشکه رسید که پایین‌ترین سطح از ۲۷ فوریه تاکنون است
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/131275" target="_blank">📅 16:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131274">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
آژانس ایمنی هوانوردی اتحادیه اروپا (EASA) به شرکت‌های هواپیمایی توصیه کرده است که از حریم هوایی عراق و لبنان استفاده نکنند.
🔴
این هشدار به دلیل ابهام درباره آتش‌بس میان آمریکا و ایران و خطر تشدید ناگهانی تنش‌ها صادر شده است.
🔴
همچنین EASA هشدار مربوط به منطقه درگیری را تا ۸ ژوئیه تمدید کرده است.
این نهاد همچنین از شرکت‌های هواپیمایی خواسته در سراسر منطقه خاورمیانه با احتیاط بیشتری عمل کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/131274" target="_blank">📅 16:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131273">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
وزیر جهاد کشاورزی: در صورت رعایت شروط ایران، از خرید کالاهای اساسی از آمریکا استقبال می‌کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/131273" target="_blank">📅 16:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131272">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWN0fdIYcDOGCiX91mbLjRHLd2mL3IObK6usEQ09sYZvGFWBN2fVCffD4qi04O2q6jJmZR4sg-VyX1ul4mIf12s5whorv8APPwn0QuRzs80qVW1QRWJPM82HzEAJNDtUUwcjT1p2A4ne2neyRFsnCronZqCenyG4EwtQEToE5DpyralqrgngK8Ttp3WGL_UwbZGgZgpesgzChRvgIF6JvkI4AVs5eMXC-413Ats0pZS8P78GbIyvpFF7NTZK-7pS-ei0JZ8x6G83HWrPBwYdYkWb0nLLhM-LbCOSsWt_OZnCvrOqdoWqxFkrvFHBf333_nPpfdTtgFFPxpiuR4ThWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاهده شدن دود در جنوب تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/131272" target="_blank">📅 16:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131271">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ: تا زمانی که دوره ریاست‌جمهوری من به پایان برسد، می‌توانیم ۵۰ درصد بازار تراشه‌های جهان را در اختیار داشته باشیم.
می‌دانید الان چقدر سهم داریم؟ هیچ.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/131271" target="_blank">📅 16:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131270">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ
: اینتل به کمک نیاز داشت. به آن‌ها گفتم: "کمکتان می‌کنم، اما در عوض ۱۰ درصد از شرکت را به ایالات متحده آمریکا بدهید."
🔴
او گفت: "قبول است."
🔴
آن‌قدر سریع قبول کرد که با خودم گفتم، شاید باید سهم بیشتری درخواست می‌کردم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/131270" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131269">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ اعلام کرد که قصد دارد بخش عمده‌ای از اسناد و اطلاعات محرمانه دولت را از طبقه‌بندی خارج کرده و در دسترس عموم قرار دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/131269" target="_blank">📅 16:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131268">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ترامپ : باید ببینیم چی میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/131268" target="_blank">📅 16:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131267">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a717d0815.mp4?token=o0Rv7a9kpnyG4-OPe8fV37BAQy5M-lsRNK59AqdFFswzVZQDJ7alpU7fhj1AVVRDRJn3KJmBQCZyKj0aWQ8urIDH2GdBUvAwb3bh2v2BxwDH-wreWL4U2qS1dz2_7BGF1UyFyVg_B0yv-vORrweYFeQrlnXXQvDVgo81EzT0RlDXSIJDintt0nWwAjdrwgyS9RcAIe2RGLGpRM2hzkDkU_YDEUDRe7IgL6bSPey3eN3aGVSwq6pcaCFCk53CKVI9eNOcpsL7CLJ4DmActyHZ0jDrDvAxXfhAJscu56tgKHjC7rPqLAaDV3LUgtSczuWa4f45zhy_Jxugf_sg850lyosZfqZbja9nNvRyKD657xl4-9osdi9vMotkldEwiKdWKIyK8-eaiDCzRTOoNNDPFaAlYZMdPkV4CSQ9CXOd8cIA7q__etyBeLcYnwjZWBWvDCy2llwtghdyAD4p_DFpntoUCWoOdIlJ2hgDjk8OiUTgndsHr98ytt_tzreB6YjegqVdiyFaL-25lhFoIN64gKUpzRCt9iJEhzO4YE3obqZmd9oRAdzUTH2e1r9TAtyn44kA5KIB6n3RKoSfHzfxhAFniWpm0e_rEfs15vOs92T7Sl_ANfUv2jIv7sO8CUb0hLTGlpi4qmG_SO3CKnkPewg_7jHuhWlbJc9QgaKyCQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a717d0815.mp4?token=o0Rv7a9kpnyG4-OPe8fV37BAQy5M-lsRNK59AqdFFswzVZQDJ7alpU7fhj1AVVRDRJn3KJmBQCZyKj0aWQ8urIDH2GdBUvAwb3bh2v2BxwDH-wreWL4U2qS1dz2_7BGF1UyFyVg_B0yv-vORrweYFeQrlnXXQvDVgo81EzT0RlDXSIJDintt0nWwAjdrwgyS9RcAIe2RGLGpRM2hzkDkU_YDEUDRe7IgL6bSPey3eN3aGVSwq6pcaCFCk53CKVI9eNOcpsL7CLJ4DmActyHZ0jDrDvAxXfhAJscu56tgKHjC7rPqLAaDV3LUgtSczuWa4f45zhy_Jxugf_sg850lyosZfqZbja9nNvRyKD657xl4-9osdi9vMotkldEwiKdWKIyK8-eaiDCzRTOoNNDPFaAlYZMdPkV4CSQ9CXOd8cIA7q__etyBeLcYnwjZWBWvDCy2llwtghdyAD4p_DFpntoUCWoOdIlJ2hgDjk8OiUTgndsHr98ytt_tzreB6YjegqVdiyFaL-25lhFoIN64gKUpzRCt9iJEhzO4YE3obqZmd9oRAdzUTH2e1r9TAtyn44kA5KIB6n3RKoSfHzfxhAFniWpm0e_rEfs15vOs92T7Sl_ANfUv2jIv7sO8CUb0hLTGlpi4qmG_SO3CKnkPewg_7jHuhWlbJc9QgaKyCQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: منتقدان شما می‌گویند از ریاست‌جمهوری برای کسب سود شخصی استفاده می‌کنید.
🔴
ترامپ: من سود می‌کنم، چون بازار سهام در حال رشد است. همه ما داریم سود می‌کنیم.
🔴
حساب بازنشستگی شما چطور است؟ ۸۵ درصد رشد کرده. باید بگویید: "متشکرم، رئیس‌جمهور ترامپ!"
🔴
من سود می‌کنم، چون پول زیادی دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/alonews/131267" target="_blank">📅 16:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131266">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ: هفته گذشته حملات قدرتمندی علیه ایران انجام دادیم
🔴
ایران پیشرفت قابل توجهی در توافق داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131266" target="_blank">📅 16:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131265">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ: ما جلسه بسیار خوبی با طرف ایرانی داشتیم.
🔴
ما در مسیر خلع سلاح هسته‌ای ایران پیش می‌رویم
🔴
همه ما از افزایش بازارهای سهام و کاهش قیمت نفت و همچنین قیمت‌های بخش خرده‌فروشی سود می‌بریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131265" target="_blank">📅 16:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131264">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
جان رتکلیف» مدیر سازمان اطلاعات مرکزی آمریکا (سیا) ادعا کرد که جنگ آمریکا و اسرائیل علیه ایران اکنون جنگ فناوری است و گفت: «کشوری که بهتر بتواند از قدرت فناوری استفاده کند، آینده جهان را تعیین خواهد کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/131264" target="_blank">📅 16:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131263">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
روزنامه آمریکایی نیویورک تایمز به نقل از یک مقام ایرانی و چهار دیپلمات منطقه‌ای آگاه گزارش داد که ایران و عمان با وجود مخالفت علنی واشنگتن، در حال پیشبرد طرحی برای دریافت عوارض از کشتی‌های عبوری از تنگه هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/131263" target="_blank">📅 15:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131262">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7SMekGziLLeDQimfCA0AXgc9CW5lsW5bekSkw3QDn3dPodYHfNpBYGW-EuZkj5FhDuAarhNt5G0pp6TYZXzWAijJq5uTUN1lxtwSPw9pMmYRn9g7G1AtDRpuhKJTNNuF6_0ORdt-Ii_PQWBJ4WmWRRlcP1vDVIn1EmZ3-pzfzJcfVexO7k489NYeTSXPXdEf5K3gl75wUGLYNktG75Obaf_R1s6hxbG1acFlZqnWoUXay9f5rk6UW2pAEhgNi0CCnR_IasEUvh_uN5FPJ7noeuKXdybmOwXVXfbLu2POi95FRVa7SK1dgMCoylxS3DvDB4EAyHyPGiWi98oYId2Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: مردم میگن نون خشک هم بخوریم باید مقاومت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/131262" target="_blank">📅 15:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131261">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
شبکه الحدث: مذاکرات ایران و آمریکا در دوحه در مورد تنگه هرمز طبق طرح جدیدی که توسط عمان پیشنهاد شده در حال انجام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131261" target="_blank">📅 15:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131255">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ng_ALF5yMM8M5h2veAFDolaQ8L82zG90rjW02brBXd8KnPcqL3IoEXONS92BraHBxJ2kW0lqeL2Kfa4BeDMLxConnFqTRdraQoOuKiOqrYoS5OOpI6X_5U5OtF7JpbbLJxNzBAvAHpGi2iYp5k8SbWT_UZPifICssFCes2czuiipAZk9FaOo3I_0lsQw2JfPWO_mQgrM4XpDlb3BIgX38KCf_92Mr2l89vnye65bkt31ITuqS2YH1aVBbxYpIGP5tvtlo8eaK-7mzb5uAa9S4VKQuzv-Kezw4uNOboemQ_SE-CBPUuWGySw5xfs6RucRHLd5h29m84WDD4uXYIDZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k8nEJ7LoCvcI68nDX4DmcsqQf6rBcK1BDnJK_10mnwRGmoZAP7G5aKVxTDUbiaJS7DXSsgrOnGfE2-86AyjwmvDfhxFThGWgYM8NgvbbMFGbA-T1CSSNFIEHwdp_rVwG9ldDJWRMeRhwZ1AXgmR6Dr06vPCAjqb0T7XYfe9NNhv4-uxqtKepOG6_Y7FYCmn78y0yqNAvA0NiDdMHCvm-ym542IZ3JOSrhHH8YdQlv2n5CYbcFYfWMWcW2Iqc_1mWcBpl2mjU28YOv5xvWKjOa3uMoPsidAJ-DVvsk_f9fmIFNw7YOtkK0X6OQ2qPtGWggpOmcaZm3j30EuFgVwJdsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auDTnWl0sjkRq_D3I-KRM9QkhWpIPpNaKLvcQVjb38OK6E1V_SCw7-niHBM0u7daA0w_754PzlrJ176gCif5UZgaRh61mvEuOctg7N6DrtdnokN5YLnWM5XDoSXkW2Uo6-F3o3QhHsIf3FVeq_IlQmGxjngG1UhrzTIl0eCiqYzo8opAXOEZOgjgyXpXCGpWYwSH00rWMvxBjo0Ajtr19bEDXJbCEKNjs46gvofxkbLXPEkmzWptJCXy7PzNroNwnDUgaiqEhig8DeX5PvdSVjiIhW1wDXHEVUWlUbuQnH6bBjdQTgmnunkFbCvqHCgkhWxLwQy7s8JbytTd0Kl2JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c1770a4f.mp4?token=N-TsxyV3fed5Xy0FRrrPZfaJF9U3yJLTOymrCLtov_u3d4DajLp_blSPXRSzmsfCcj94c2rBksnDitbQb-M765j8oR218v2Ed8fstc_UVZxRQnStXPQOvQuwArMszqHt7osCTleRbVt3DJE5Mo2LkNyF8r4BYxrpnJaDyQmRUjXyZm28O-Xj0KIZeYZACqGA1gpzoN3D-FMDGp_9PLmqPfokfC78engN1pIXVgqDoqenbED9kVpgZ8g0_PcKF8nRzXBqdgni1HvdGTRsp6Q-5b39YsWA_TyNXj92L_Mp6z-RoVpXBuABqVrw01lTUGFuNc49QHRv5jfCzwRv0FReQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c1770a4f.mp4?token=N-TsxyV3fed5Xy0FRrrPZfaJF9U3yJLTOymrCLtov_u3d4DajLp_blSPXRSzmsfCcj94c2rBksnDitbQb-M765j8oR218v2Ed8fstc_UVZxRQnStXPQOvQuwArMszqHt7osCTleRbVt3DJE5Mo2LkNyF8r4BYxrpnJaDyQmRUjXyZm28O-Xj0KIZeYZACqGA1gpzoN3D-FMDGp_9PLmqPfokfC78engN1pIXVgqDoqenbED9kVpgZ8g0_PcKF8nRzXBqdgni1HvdGTRsp6Q-5b39YsWA_TyNXj92L_Mp6z-RoVpXBuABqVrw01lTUGFuNc49QHRv5jfCzwRv0FReQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایستگاه‌ برق تو شهر لوبرتسی، منطقه مسکو "روسیه" درحال سوختنه
🔴
بعد حمله اوکراین، اون منطقه بدون برق مونده
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/131255" target="_blank">📅 15:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131254">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وال استریت ژورنال: اختلاف بین بن سلمان و ترامپ در پی جنگ علیه ایران
🔴
رئیس‌جمهور آمریکا به دنبال کاهش حضور نظامی در سعودی است
🔴
مقامات عربستان می‌گویند عدم سفر روبیو به ریاض در هفته اخیر، برای تحقیر آن‌ها بوده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/131254" target="_blank">📅 15:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131253">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gd2TXBg6--v5fLgXxmeNVMrbubHYhCe4he73Ml7PD3FZZin9GHPAaPv7_K6By-IPtZ7VZP9V5G4a7sqk_vWoxNn5IMKvECjSJqi_9Q5tozgGNpg3uHDIJ9VR3R5mbRf0Glc7f1NgdjJrmMuOU5xBlskNHYJXq14p_iqKWIkKk_sHmX2jeyKNa7E_ficPHTRkp6XWYI2dQIbdavOJ5--h1SBlqxbo4PJ8mP5fyAMQ9UXdl37jHleX3b-HvwJsZ7d597x470vhZhl9-01UggLIqKGHv0BNyDf7IpFfEfvHsDsFbgede1VJCwPw42c-4OaVXc8GH96idf0sZP461py2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشف لباس زیر طلا زنانه در بازرسی از خانه نماینده پارلمان عراق!
🔴
کشف لباس زیر از طلای خالص در میان اموال کشف‌شده از منزل یک نماینده زن پارلمان عراق، جنجالی شده است.
🔴
به تازگی و همزمان با بازداشت عالیه نصیف نماینده زن پارلمان عراق به اتهام فساد مالی، تصاویری از کشف و توقیف حجم زیادی پول ( دینار و دلار)، جواهرات، طلا و ساعت‌های گران قیمت منتشر شد. در میان این عکس‌ها، تصویری از کشف لباس زیر زنانه شامل سوتین و شورت ساخته شده از طلا با واکنش‌های زیادی در شبکه‌های اجتماعی روبه رو شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131253" target="_blank">📅 15:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131252">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
مرکز تحقیقات صداوسیما: تماشای رادیو و تلویزیون در میان جوانان و نسل زد تقریباً در همه کشورهای جهان کاهش یافته و ایران نیز از این روند مستثنی نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131252" target="_blank">📅 15:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131251">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESe5oJ9mOG2lo8rvKI5VJhXR9Ag9SSOd4zxXuxsFdRo7n0EJYtPFelRh7hWVY1Vb7nhUaOVDwMU_ID4VkBgboWLcF_2NHKcFBxIGUAIr9kotxrr-_Nrl1cbP8OJLHdGZMZNN0qT8vcjFBMSyPStuUHkhSnbFhXCfQDW5-TTCVWHhnut-r6MuIVLQrNilKU6d9qEae_Xp1zb-PbCwW-ucuO89pUac-tNU23TZIKUMkhzjMY-6qXNAET8tvtwWiGo-H03ZdeDAv_GtXGCAFbxjuM2WTzeLUrmXWtKm-TV8btNdNCvlOVfmcJMeSptPkhZf9wdU9Djgb_h5a7l8LZWMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / منابع العربیه: توافق اولیه برای آزادسازی ۳ میلیارد دلار به ایران حاصل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131251" target="_blank">📅 15:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131250">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
جی‌ دی‌ ونس : فکر می‌کنم کاری که رئیس جمهور به ما گفته این است که از این تفاهم‌نامه برای پر کردن مجدد ذخایر نفت جهان استفاده کنیم و بعد ببینیم اوضاع دست کیه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131250" target="_blank">📅 15:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131249">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCn1f2qrXJgN1dS0F64rUveGJL3egVS9mV2cjyMGYy0-lOREib45asYKGMDr4sqAQgWrzl4WjURBLHLf_DWeKzUme1y8BYYX5CUv6oJ4k3roD4-vcXdnoRbbFi_M3comR9NVTNbrVmvyd02MaLnDVhS99NiQCy14HZaOzSGaT0X9kWo7w55C3sLC9niiShryxNbV7z_UYWMrDm3_WJatAYMgKy2-BgrKx6YLr-hsgHkVlnEYTLaTr2Zb3Mb2nV5_LWd8KQLmYWz_HZTjx0FoQdNdSertkPF6tN91puUBTBq1ynmaChFAkULDXXlMx8pDDdB4yVa1cFTq7Mhepy3kQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه هواپیمای دولتی روسیه بعد از توقف یه ساعته تو تهران به سمت مسکو برگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131249" target="_blank">📅 15:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131248">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
پزشکیان:ممکن است در برخی مسائل دیدگاه‌ها و سلیقه‌های متفاوتی وجود داشته باشد، اما آنچه باید در این مقطع تاریخی به نمایش گذاشته شود، وحدت، همدلی، هماهنگی و انسجام ملی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/131248" target="_blank">📅 15:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131247">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
قدردانی پزشکیان  از تلاش‌های قالیباف، عراقچی و سایر مسئولان ذی‌ربط در پیشبرد مذاکرات:
مجموعه این تلاش‌ها در جهت تأمین منافع ملی، کاهش تنش‌ها و تقویت جایگاه جمهوری اسلامی ایران در عرصه منطقه‌ای و بین‌المللی صورت گرفته و شایسته تقدیر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131247" target="_blank">📅 15:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131246">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
پزشکیان با اشاره به ارزیابی مثبت مراجع عظام تقلید از توافق و تفاهمات اخیر کشور: تمامی بزرگوارانی که در این سفر توفیق دیدار با آنان را داشتیم،
از روند شکل‌گرفته ابراز رضایت کردند
و آن را اقدامی مثبت و در مسیر تأمین منافع ملی دانستند
🔴
خوشبختانه دستاوردهای مهم و ارزشمندی در حوزه‌های اقتصادی و تجاری حاصل شده است
🔴
استمرار صادرات نفت، تسهیل بخشی از محدودیت‌های مالی و ارزی و فراهم شدن زمینه‌های جدید برای توسعه همکاری‌های اقتصادی از جمله نتایج این روند بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131246" target="_blank">📅 15:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131245">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSx4D5Ro3tvaBpn9u28xQOQ3W9CDyiwl6CxcPEPyIJE-pzHyXrhauF_dAwxoJT04CEsh3c2dyQg4ZjFSsmMDmrKXhTy1WGulY90v41oJAanbg2dYvgrbUaGcw1vNKL8mGfLN81ff6c7Xj_5FOGx8FGeSgGlzQkBMQ5yX_G0_vwaK7vviWndHDhuwQbzhs3ubLbmgztCQJqAEB_53x-eLn2A20Og4VqjASA6ulX9CNAvLWcCqVcuJzfjcXc3Hpi5eJJRLceQZyHwRKNDE-oN2r1YtNmcjKDnoGX7wKGlayT_ZyKB9SdCU8gYXiiK5AkdynSKpCrBS5fdDGzUetXLPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیافه میثاقی قشنگ اینجوریه آخ‌جون بالاخره یه نفر غیر محسن بیاتی‌نیا و سیروس دین‌محمدی داره باهام حرف‌میزنه
@AloSport</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131245" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131244">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_uaehGpIvVZ6GOZB8JCT5NMmbehuD6sI782WbbwMPsnRypY5LCftTKV3dDXi-t8DvueFwyPG-I4Ys2-t8rWI4QldDJ2IWoW0w2qdlB-v2ETqWi1S80SBL4N1G81YVRPmKbaGRw2aBSp2j6-5g6hkDV-AnJsoVlLGNXXm0-nzXtU3qNHjEETVFGXo2cQFxnYfIRk6aZMCl2-K0aMpvsdeySPZnK9zkt2wg0w6M3MM6nYOd080ARMNL9uEAHtlY9-R8JGLNN9cM3gl7dFoTCY_eigvUh-CQL3QEr7kBtHMp4QJheMu1fUm-HsMKfwDA2I150VfIMAe4Uja2ZUaVJE0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی خطاب به آمریکا: اگر حیوان خانگیتان ساکت نشود، ایران به آنها درس می دهد
🔴
توییت جدید وزیر امورخارجه: ترامپ آمریکا را به «ساکت کردن حیوانات خانگی‌اش در تل‌آویو» متعهد کرده است. اگر آنها ارباب خود را نادیده بگیرند، ایران به آنها درس خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131244" target="_blank">📅 14:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131243">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
غریب آبادی، معاون وزارت خارجه: گفت‌وگوهای امروز در قطر متمرکز بر پیگیری اجرای مفاد یادداشت تفاهم است
🔴
کارگروه‌های پیگیری اجرای تفاهم و مذاکره برای توافق نهایی شکل گرفته است، اما هنوز مذاکره‌ای در این قالب‌ها شروع نشده است.
🔴
رایزنی برای تعیین زمان و مکان مذاکرات در قالب این کارگروه‌ها از طریق میانجیگران ادامه دارد و در صورت فراهم شدن شرایط لازم، مذاکرات در قالب این کارگروه‌ها آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131243" target="_blank">📅 14:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131242">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
زمین لرزه‌ ۳.۳ ریشتر تو عمق ۱۴ کیلومتری زمین، پاکدشت تهران رو لرزوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131242" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131241">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6DpotSYwUigSvWY5qTKRNAmVRi4NLy3eyg9yPWlHR9HhlAAEsOYj8IAFCCNrBqIBZLJ_PI1AKAEtl4nEkRCLCTsARNoGnMhWNqP4RIYUuHTSJpHhLuWOIFKLIuKaITUWTdoYIa574goBtqv9APnR6ldxb-A_Yyi0JrE_zBiA4Oc4ME-KV30jX-xnQ_mDcJIpj8acBj5K6tCPX0yNiFIyMYbQq53EyZejH_GlcU4yYjttdxt0mpoMAx26MlQwsa9axv51k7NQtQNO0rHz66ufozX4PkK_7-GXLdEVR2GxOrWWfsmsUG3B7W8RnfUpUuydcbiY95r8S-FYPi50VGrMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم کارشناس ارشد صداوسیما:
چین باید میانجیگری کنه چون ما به قطر اعتماد نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131241" target="_blank">📅 13:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131240">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
مجلس نمایندگان آمریکا که تحت کنترل جمهوری‌خواهان است، با ۱۸۹ رای موافق در برابر ۲۳۵ رای مخالف این قطعنامه را رد کرد. دو جمهوری‌خواه از این قطعنامه حمایت کردند و ۲۲ دموکرات به آن رای منفی دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131240" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131239">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
بخشنامه تعطیلات هفته آینده ابلاغ شد
🔴
بر اساس بخشنامه رئیس سازمان اداری و استخدامی کشور به دستگاه‌های اجرایی: روزهای شنبه، یکشنبه و سه‌شنبه ۱۳، ۱۴ و ۱۶ تیر ماه استان تهران تعطیل است.
🔴
دوشنبه ‍۱۵ تیر سراسر کشور تعطیل است.
🔴
سه‌شنبه ۱۶ تیر استان قم تعطیل است.
🔴
پنج‌شنبه ۱۸ تیر خراسان رضوی تعطیل است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131239" target="_blank">📅 13:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131238">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
برنامه‌های برگزاری اجلاس ناتو در سال ۲۰۲۷ در آلبانی به دلیل مقاومت دولت ترامپ و انتقاد برخی از متحدان به خاطر هزینه پایین دفاعی تیرانا، در هاله‌ای از ابهام قرار دارد، رویترز گزارش می‌دهد
🔴
پیش‌نویس بیانیه اجلاس ناتو هفته آینده در آنکارا، ترکیه، آلبانی را به عنوان میزبان بعدی ذکر نکرده است، با وجود تعهد قبلی.
🔴
یک منبع گفت برگزاری اجلاس در آنجا ممکن است رئیس‌جمهور ترامپ را عصبانی کند و تیترهای منفی ایجاد کند، در حالی که دولت آلبانی پاسخ داد «پیش‌نویس‌ها پیش‌نویس هستند، نه تصمیمات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131238" target="_blank">📅 13:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131237">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f0ade05a.mp4?token=Mh0oo5l_DN9S4lqZvKWLt0mdmjW0ltV9wsYswdlPb8RD54-M_kLcagoUlJ38zdOaDg3kFMx6QHs8s3Q0Xs9McbswMzWu--lFkhMpX_6ywdrJ4eathPsOYXK4IZozpmf7vTdjX0MWi01CgJcJQY3qGLd3gXwiIJYsHiSd75u2p4XnW1n-O1u8IIxk4i4aWdq5lQ6wuyt31FEqhLKNfozxFYJcDIGiy-KYy-pkkB9p2B-_MCtLsDigL5NTJr3Q09ZFXiT3iIafI2XaC3guubHQNtAnL29j4RkWmWwrHTkyigAEetqlU8fsmafm6T7RAl74ZoC_m-GRHTH6DQkadmqIpR5LYbjZtrlvxnKuGf-iF_RzEUgbtbHtZeN_J2XRFXKm_7bi21C2RUt4QzVmaFVyLKM7KvW00bcCchtBtS4mxM8fiQ0xexjC6-34q1QpWHHKZaG5mvsou1echxLyVfP47_brzfKBTjnB9iWoD2lGlUDc-N8K5GBGjnw2nBx9PWwcBFtNrI9w88gEH5qNl2EpzsZMia4EzdtTCo_VgV2FLt2Z_y_2ywnI35-8MAY5buK56opmIg_udoXaTcb_62YFwtastWhaklJ5yQ3j0jF12toa27iJmloC6cDqnLUwq1Fm416X6vSk4925Cu8JfEbLezsAS5DmJwEPT8rXRAo6VnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f0ade05a.mp4?token=Mh0oo5l_DN9S4lqZvKWLt0mdmjW0ltV9wsYswdlPb8RD54-M_kLcagoUlJ38zdOaDg3kFMx6QHs8s3Q0Xs9McbswMzWu--lFkhMpX_6ywdrJ4eathPsOYXK4IZozpmf7vTdjX0MWi01CgJcJQY3qGLd3gXwiIJYsHiSd75u2p4XnW1n-O1u8IIxk4i4aWdq5lQ6wuyt31FEqhLKNfozxFYJcDIGiy-KYy-pkkB9p2B-_MCtLsDigL5NTJr3Q09ZFXiT3iIafI2XaC3guubHQNtAnL29j4RkWmWwrHTkyigAEetqlU8fsmafm6T7RAl74ZoC_m-GRHTH6DQkadmqIpR5LYbjZtrlvxnKuGf-iF_RzEUgbtbHtZeN_J2XRFXKm_7bi21C2RUt4QzVmaFVyLKM7KvW00bcCchtBtS4mxM8fiQ0xexjC6-34q1QpWHHKZaG5mvsou1echxLyVfP47_brzfKBTjnB9iWoD2lGlUDc-N8K5GBGjnw2nBx9PWwcBFtNrI9w88gEH5qNl2EpzsZMia4EzdtTCo_VgV2FLt2Z_y_2ywnI35-8MAY5buK56opmIg_udoXaTcb_62YFwtastWhaklJ5yQ3j0jF12toa27iJmloC6cDqnLUwq1Fm416X6vSk4925Cu8JfEbLezsAS5DmJwEPT8rXRAo6VnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هشدار گوگل به میلیون ها شهروند ونزوئلایی قبل از وقوع زلزله
🔴
در حین وقوع دو زلزله سهمگین ۷.۲ و ۷.۵ ریشتری در ونزوئلا، سیستم هوشمند هشدار زلزله گوگل توانسته بود چند ثانیه پیش از آغاز لرزش‌های مخرب، به بیش از ۱۱.۴ میلیون شهروند هشدار بدهد.
🔴
از آنجایی که ونزوئلا فاقد سیستم ملی هشدار زلزله است، این فناوری که از شتاب‌سنج گوشی‌های اندرویدی به عنوان حسگر لرزه‌نگاری استفاده می‌کند، توانست زمانی حیاتی را برای پناه گرفتن در اختیار مردم قرار دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131237" target="_blank">📅 13:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131236">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نتانیاهو: ایران سعی کرد ما را مجبور به عقب‌نشینی از جنوب لبنان کند، اما این اتفاق نخواهد افتاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131236" target="_blank">📅 13:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131235">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ اسرائیل: ترامپ درحال بررسی بازگشت به جنگ تمام عیار با ایرانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/131235" target="_blank">📅 13:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131234">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c28e55c3.mp4?token=szkrMUXtmLfxUQI3UV02TRUPMWxxqOm0mlDEJJsJRgWvMCqZ2Ghc2se2vwq5XyYWlpINEnY_JAxnkGC1gCYMvFjEuF-jSWnLeXgeOZKtx3ZCsVSITJlQEYDAhrQ08u4zy6b8z1W0aSTC2lZ4UJpDKNPZarjQ5l--PVaNePdFeyCAGaMNoRuIqCDOaWSc9LUrwsPdRwFIPoL9BrW40xWfFiG2Mkpz63eB1hAsaSIKkt1KXFyITlPbS8Go5T3Sf213AqTYGMgKiw8a-r32TNk6V1n5FgTNLjS5sqAD-ie-VxA3V2ac-tnEha5ERd1xYlOS73KjXE9ZDQ0L2sh4EvTHqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c28e55c3.mp4?token=szkrMUXtmLfxUQI3UV02TRUPMWxxqOm0mlDEJJsJRgWvMCqZ2Ghc2se2vwq5XyYWlpINEnY_JAxnkGC1gCYMvFjEuF-jSWnLeXgeOZKtx3ZCsVSITJlQEYDAhrQ08u4zy6b8z1W0aSTC2lZ4UJpDKNPZarjQ5l--PVaNePdFeyCAGaMNoRuIqCDOaWSc9LUrwsPdRwFIPoL9BrW40xWfFiG2Mkpz63eB1hAsaSIKkt1KXFyITlPbS8Go5T3Sf213AqTYGMgKiw8a-r32TNk6V1n5FgTNLjS5sqAD-ie-VxA3V2ac-tnEha5ERd1xYlOS73KjXE9ZDQ0L2sh4EvTHqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمرین شبیه سازی حمله به جزایر ایران توسط ناو باکسر که به تازگی به نزدیکی ایران رسیده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131234" target="_blank">📅 13:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131233">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام ایرانی:
مذاکرات دوحه بر تنگه هرمز و پول‌های بلوکه‌شده متمرکز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131233" target="_blank">📅 13:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131232">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وقوع حادثه دریایی در آب‌های یمن
🔴
شرکت خدمات دریایی انگلیس اعلام کرد که یک حادثه دریایی در ۷۶ مایل دریایی جنوب بلحاف در یمن رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131232" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131231">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr_XE3UeNxeghn_npE5XYZKwcAdk90JqTNl9V2NypPenwEH1osTfzJ9dgNqzn6HGss6M9NuXjnE-yNwK0Ex4tohJrzSwUYRskSSlB6gSF8YR6IbcZ3BEQU8FJHwlnWlAkxg9R9fr8HZkycLF_clBp1W1yGZeXmrEUDvwR3iuc8S2Df6fKgUwyABp8Zbhec2t6dQEHOV3SIui6YOYw9Pr0e0zcxp9X3UueSELapF87nAO8mooDWjyfmKVW0ePhubRkdLHZB1X4JBJXSgnfZN9TcjpPDDU33CjssSl7KiK1ff8c55uxnK2hZpEiuonk0NGKOv4mfZBX2ZMioI1zzkliw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۶۰ هزار واحدی به ۵ میلیون و ۱۸۷ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131231" target="_blank">📅 12:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131230">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
صداوسیما: یک فروند کشتی که از مسیری غیر از مسیر تعیین شده در قالب نظم ایرانی در تنگه هرمز، تردد می‌کرد، به گل نشسته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131230" target="_blank">📅 12:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131229">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل: در طول ماه‌های اخیر، ۲۸ پهپاد با موفقیت وارد نوار غزه شده‌اند که بیشتر آن‌ها به دست حماس رسیده‌اند
🔴
مشخص نیست چه محموله‌ای با استفاده از آن‌ها جا‌به‌جا شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131229" target="_blank">📅 12:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131228">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
الجزیره : گفت‌وگوهای فنی ایران و آمریکا در قطر در جریان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131228" target="_blank">📅 12:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131227">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
کوشنر و ویتکاف روز سه‌شنبه با نخست‌وزیر قطر دیدار کردند تا زمینه‌سازی برای جلسات فنی چهارشنبه انجام شود، اما خودشان در جلسات شرکت نمی‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131227" target="_blank">📅 12:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131226">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9119f36555.mp4?token=j2kaddvR8Gy2aSL2nxwFHCjoBekXcwHvIco6fpXiS55-EMypb5PAIP-fPVzaV2pMIMcNzAHKe-dU6onat1mo5ZoVsRZLeQBxW8QswBI6W7mArbhhPC6CGL9N4zazzu_wenTzRHoYL3EqoAMl5hLak7X3IoxNh-0JRyrb_O1dvWaNFkN8r13af5N9JD6k2PR7BKT8IIzqnTpRxS1dFlcp7A_VuZL-Nh3FTNTqW4xGzOnrbeetvBgihZIC7EWByM_zlotVGS5iuP7ej_ggvvc4ahYnslZh1JWJ29qivn3ZO5pRnNDKu98VgxAf0Y3jPcbvcXzZXedD4G7hjCrycKWyTAemTYClxxcGbDproXx_AXyXsl45KZkYVeglg44OUbm7NsT1VMO9nyBVSXxhZwASrM7qxQ1asI-9gRZvtAIFi2EP1w0rH5fzsZu9kE_CS22fbg1anwlSlSzS61edZ-Fgr2mWV7u2MuJvvWv-NStSE_IV-V89O4gocF3autazV_wIqfhB8N5qrbdQmlaOp1dgEio49jONptvh6rNjYEgZHMkYxjLjWJwK4_tAIed-pOyEyNfYb5NnrBQaspDexHx1MPqywaeajiAZLTeMrJdAxyWEfex9F8Rwe8L6bz3Wh6BJ9NwefwiCzlbtbspnLiJpDrIVJ4Ie1Vbg42ekHsRoz8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9119f36555.mp4?token=j2kaddvR8Gy2aSL2nxwFHCjoBekXcwHvIco6fpXiS55-EMypb5PAIP-fPVzaV2pMIMcNzAHKe-dU6onat1mo5ZoVsRZLeQBxW8QswBI6W7mArbhhPC6CGL9N4zazzu_wenTzRHoYL3EqoAMl5hLak7X3IoxNh-0JRyrb_O1dvWaNFkN8r13af5N9JD6k2PR7BKT8IIzqnTpRxS1dFlcp7A_VuZL-Nh3FTNTqW4xGzOnrbeetvBgihZIC7EWByM_zlotVGS5iuP7ej_ggvvc4ahYnslZh1JWJ29qivn3ZO5pRnNDKu98VgxAf0Y3jPcbvcXzZXedD4G7hjCrycKWyTAemTYClxxcGbDproXx_AXyXsl45KZkYVeglg44OUbm7NsT1VMO9nyBVSXxhZwASrM7qxQ1asI-9gRZvtAIFi2EP1w0rH5fzsZu9kE_CS22fbg1anwlSlSzS61edZ-Fgr2mWV7u2MuJvvWv-NStSE_IV-V89O4gocF3autazV_wIqfhB8N5qrbdQmlaOp1dgEio49jONptvh6rNjYEgZHMkYxjLjWJwK4_tAIed-pOyEyNfYb5NnrBQaspDexHx1MPqywaeajiAZLTeMrJdAxyWEfex9F8Rwe8L6bz3Wh6BJ9NwefwiCzlbtbspnLiJpDrIVJ4Ie1Vbg42ekHsRoz8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک هاکبی، سفیر آمریکا در اسرائیل:
یکی از چیزهایی که وقتی سفیر شدم یاد گرفتم این است که باید هر روز خوراک شبکه‌های اجتماعی ترامپ را چک کنی.
🔴
نمی‌دانم این را می‌دانید یا نه، اما او معروف است که نیمه‌شب از طریق شبکه‌های اجتماعی افراد را اخراج می‌کند.
🔴
پس اولین کاری که هر روز صبح انجام می‌دهم این است که بیدار می‌شوم، حساب توییترش را چک می‌کنم و می‌بینم که آیا اخراج شده‌ام یا نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131226" target="_blank">📅 12:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131225">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رویترز: مذاکرات فنی غیرمستقیم میان آمریکا و ایران در دوحه، با میانجیگری قطر و پاکستان در حال برگزاری است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131225" target="_blank">📅 12:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131224">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
دلار هم اکنون 175,500 تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131224" target="_blank">📅 12:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131223">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
فارس: ارزیابی‌های اولیه حاکی از آلودگی نفتی بیش از ۲۵۰ کیلومتر از سواحل هرمزگان در پی حمله آمریکا به ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131223" target="_blank">📅 11:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131222">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مصاحبه حق و جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:  خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟ پسر بچه: آره، جونم مهم تره خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد. پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131222" target="_blank">📅 11:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131221">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=NNYpfd-Yg30mE7H0vCYBYc6ku10gyoB4b3MMfXTHTTa8lzZ4w--9m70RvYb_SgbnhLZDc33RpEz4zZ6slrFVeVYWvOmSZDOATkKx2T-tWJEvv26P2-PG9xVMjERPG-EfBlWzh6nyU4qcIj8WOlL0SsHDbL3Gxo28skDsb2MZPc9RKNMdh1OwXJosMWApDVagV_tY5pkXITM_OzIEvxqHB0DkGohWj-VFizkKdNYTmnPABDPI0BL8-oogP9KH2i6gzWu0u1WnqjBNeCjnR7W7l0ckpoLB2MvSNR4nx71-1AEpd6c23pVclNZWro0CpR-CjKXz4TmHT87umaUx-uv4cg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=NNYpfd-Yg30mE7H0vCYBYc6ku10gyoB4b3MMfXTHTTa8lzZ4w--9m70RvYb_SgbnhLZDc33RpEz4zZ6slrFVeVYWvOmSZDOATkKx2T-tWJEvv26P2-PG9xVMjERPG-EfBlWzh6nyU4qcIj8WOlL0SsHDbL3Gxo28skDsb2MZPc9RKNMdh1OwXJosMWApDVagV_tY5pkXITM_OzIEvxqHB0DkGohWj-VFizkKdNYTmnPABDPI0BL8-oogP9KH2i6gzWu0u1WnqjBNeCjnR7W7l0ckpoLB2MvSNR4nx71-1AEpd6c23pVclNZWro0CpR-CjKXz4TmHT87umaUx-uv4cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه حق و جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
پسر بچه: آره، جونم مهم تره
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131221" target="_blank">📅 11:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131220">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZkzIxhsxZ5FYyRFm30sMzEQARFqOdAJIrinONBHo7OgP2G2mr6K5hLR5ae4YYM6Qi6va7GAMewDF1hQ18LTTscwvvDu6UsRpNY52PCb5t56XMSDfUOcPvi3ybSL0Ias-CGpox8WE77B21-X0F5ZH-RuMU_VZhA1C5Djw66vvmrAeVODRhgZWSB0O5czn5UxcTAJTMUMP2j5y0SohYWvH0ywY_jMFz_L22c5xHz7snPLAi4WVQe6kXTtzHmVecCjrSYKMiVjf-_B9JC5ju3R9Zdo5CltjSHsXAcBLF7IQRHktOylqxo89R9ImGAWzXmjbrjSTTqEq5ReQ591PmY_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شریعتمداری: اگر مشاوران به پزشکیان اطلاع می‌دادند که ترامپ ادعای دروغ صفر شدن صادرات نفت ایران را مطرح کرده، رئیس‌جمهور نمی‌گفت «۴۰، ۵۰ روز است نتوانستیم یک بشکه نفت صادر کنیم» و ترامپ این سخن را به نشانه پیروزی خود توئیت نمی‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131220" target="_blank">📅 11:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131219">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
رسانه اسرائیلی ای ۲۴ نیوز: سیا و موساد اسرائیل نقشه‌ای محرمانه، مشترک و پیچیده برای سرنگونی دولت ایران در طول جنگ آمریکا و ایران اوایل امسال داشتند.
🔴
بخشی از این نقشه نیازمند نفوذ مسلحانه جدایی‌طلبان کرد به مرز غربی ایران بود.
🔴
معاون ترامپ، جی‌دی ونس، از این نقشه‌های محرمانه مطلع شد و بلافاصله به اردوغان ترکیه اطلاع داد، زیرا می‌دانست اردوغان سیاست‌های توسعه‌طلبانه کردها را رد خواهد کرد.
🔴
این نقشه در نهایت پس از افشای جزئیات آن توسط ونس شکست خورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131219" target="_blank">📅 11:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131218">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
کوبا: مذاکرات با آمریکا متوقف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131218" target="_blank">📅 11:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131217">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
نتانیاهو:من می‌خواهم کمک‌های آمریکا را متوقف کنم. این مثل کمک‌های رفاهی است؛ من آن را نمی‌خواهم
🔴
اقتصاد ما دیگر یک اقتصاد کوچک نیست... ما می‌توانیم همین بخش کوچک از درصد تولید ناخالص داخلی‌مان که از ایالات متحده دریافت می‌کنیم را خودمان تأمین مالی کنیم.
🔴
می‌خواهم این روند امسال شروع شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131217" target="_blank">📅 11:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131216">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
خبرنگار الجزیره : تهران خواستار آزادی ۱۲ میلیارد دلار است؛ البته نه برای خرید کالای آمریکایی
🔴
عمر حواش، خبرنگار الجزیره در تهران، گزارش داد که اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، تأیید کرد که دستور کار هیئت ایرانی به ریاست کاظم غریب‌آبادی، معاون وزیر امور خارجه، محدود به مذاکرات «ایرانی-قطری» برای تسویه دارایی‌های مسدود شده است و وجود هرگونه کانال مذاکره مستقیم با هیئت آمریکایی را تکذیب کرد.
🔴
تهران خواستار آزادسازی فوری ۱۲ میلیارد دلار در دو مرحله ظرف مهلت ۶۰ روزه است که با ۶ میلیارد دلار سپرده‌گذاری شده در بانک‌های قطر آغاز می‌شود.
🔴
در پشت صحنه، یک اختلاف نظر شدید آشکار شد، زیرا تهران شرایط واشنگتن برای ایجاد یک خط اعتباری انحصاری برای خرید کالاهای کشاورزی آمریکایی (مانند گندم، سویا و ذرت) را رد می‌کند، در حالی که به حق مطلق بانک مرکزی ایران برای تعیین نیازهای خود به کالاها و داروها بدون دخالت خارجی پایبند است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131216" target="_blank">📅 11:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131215">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtx8ttmiKF7QqpNcl-qibJKEPdlcg-KNWw4LT2HS_Xixiu0jJvvPADZSEGOogNaHP2fwCwX0n-XsXiNU6-neor_nJU1_KwQw0NI7G63doa4UBBL6UM_nzOatRiYyZIxzWP7PF9MrgqyHCzg-hbZnhnHvDu0uAS0_af6300tqg27DMxN4vPtHFgaT6UzvNj60tqzQ7xVJ2hl7NuaQD5vjJSQiF6_hSkgFG_utJi_xjSe5C1MrnR_vaAZnb2wH2xlQ4M3iAJsmZpeUOpnt9fZNCaNwuK1nJc1TR482YShXSjsqip9_r39z8e7NhB5mUZwxq03A9InB9Vfb79yCTlK95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش جدید وارزون از نقاط استقرار ناو های هواپیمابر آمریکا
🔴
از مجموع 10 ناو هواپیمابر آمریکا ۳ ناو در حال حال تعمیر ، ۲ ناو در حال تمرین ، ۳ ناو مستقر در آمریکا ، ۱ ناو مستقر در دریای چین جنوبی و ۳ ناو نیز در منطقه خاورمیانه قرار دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131215" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131214">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLy1WZzNePsEBK_TGgQvL7bgpRe9wzIYk8Q6LCs_hcI0SKLTt4WCMfHaljcKJ0MLE5kjvr282sq-nmv2LMe-PWXM4iO7RF7kzpqtRlg_QIz3cQuokZpx57s-gBSDOGImPySQt0SnzH4JHMCrxJr4SZypsRYFg6f4Z8xjb3C7xeazBgVnQjJg1Pt1tXdggGHiC2pNhcdXwoKHnM41M0s8BoNdxdvfSChNYz9YXv9ozDLwf-HMMHhlaD-1mNC7V0pZfJgNrBqPBX5fVzzp0KitPYohJFSQj57FFwc403x1uuCzXYofcFx7ViaMaB79O0ftpXYQZSNjvbiPIdmEBFimIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی عضو تیم مذاکره کننده: ایران به سرعت درحال بازسازی زیر ساخت‌های غیر نظامی خود است.
🔴
ذخیره سازی اقلام حیاتی را انجام می‌دهد.
🔴
سیستم های تسلیحاتی جدید را پیش می‌برد.
🔴
هزاران فریب دهنده «ماکت» نابود شده را جایگزین می‌کند.
🔴
فناوری های نوظهور را مستقر می‌سازد‌.
🔴
شبکه پایگاه های زیرزمینی و مراکز فرماندهی و کنترل خود را گسترش می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131214" target="_blank">📅 11:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131213">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سی‌ان‌ان: با تعلیق موقت عملیات سازمان ملل در تنگه هرمز، تا کنون حدود ۲۵۰۰ دریانورد از تنگه تخلیه شدند و بیش از ۸۵۰۰ نفر همچنان در تنگه سرگردان هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131213" target="_blank">📅 11:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131212">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
آمریکا قصد اعزام نیروی زمینی به لبنان دارد
🔴
بر اساس گزارش واشنگتن‌‌پست وزارت جنگ آمریکا (پنتاگون) در حال آماده شدن برای اعزام نیروهای زمینی ایالات متحده به لبنان است.
🔴
این اقدام با هدف اجرای توافق‌نامه اخیر و جنجالی با میانجیگری آمریکا میان لبنان و اسرائیل صورت می‌گیرد که خواهان خلع سلاح حزب‌الله است.
🔴
روزنامه واشنگتن‌پست به نقل از مقامات آمریکایی گزارش داد که نیروهای آمریکایی برای نظارت بر پایبندی لبنان و اسرائیل به این توافق‌نامه، در خاک لبنان مستقر خواهند شد
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131212" target="_blank">📅 11:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131211">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/816b9c6962.mp4?token=q9k8Yi_Z3ZjYtVgJeBlXsovHClE-R8BMx1_Jj-XEMl_oIr-YLBDFITlflUUIzvPpSKn6vSWFWNeSKy8pGPodWgSCzL6Q-9j8cDc7ulEKRN9VYZlNxsi-lZVCdUIceoBLguy3Tf-BHVNKt7Y8N0QLwQ79XGdU5eLcI93tnwqMXXCnYPP6f3Pk-G4BVCNqLcY6Fu-oWIJhsCErsEDZFDBf0cn0V-bzjywmAjGiFHp-HDkwwmOvEmBPHb5eZx4sQSUrA_To_1LK3B1M7sOVGn4pM8igFFN1Fj-17aRggEFjrnjsMcdl_PFdV_SJ21N2-v0p43MzrY_ZD772HUclPohgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/816b9c6962.mp4?token=q9k8Yi_Z3ZjYtVgJeBlXsovHClE-R8BMx1_Jj-XEMl_oIr-YLBDFITlflUUIzvPpSKn6vSWFWNeSKy8pGPodWgSCzL6Q-9j8cDc7ulEKRN9VYZlNxsi-lZVCdUIceoBLguy3Tf-BHVNKt7Y8N0QLwQ79XGdU5eLcI93tnwqMXXCnYPP6f3Pk-G4BVCNqLcY6Fu-oWIJhsCErsEDZFDBf0cn0V-bzjywmAjGiFHp-HDkwwmOvEmBPHb5eZx4sQSUrA_To_1LK3B1M7sOVGn4pM8igFFN1Fj-17aRggEFjrnjsMcdl_PFdV_SJ21N2-v0p43MzrY_ZD772HUclPohgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلی هانری :)
@AloSport</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131211" target="_blank">📅 11:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131210">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
🚨
قرعه کشی پرمیوم رایگان  دیگه همتون از پرمیوم تلگرام خبر دارید که باهاش میتونید تیک ابی و استوری و ایموجی پرمیوم رو باز کنید.  فقط کافیه توی چنل های زیر جوین باشید
🔗
@CRYPTOSMART_ORG
🔗
@Proxy1y
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/131210" target="_blank">📅 11:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131209">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUGucUj3nwZ1EUG0XqSJ6md1oUAdTOA3ELV3xlqpMtX7b5vl9eswdFZR9XrjiD7hHxdOQaLb8aCHLjCUEQ9Q_u1lfcqSPMY9MBBSBOTpSZFllkwLKF2Ai_JtPArU8aSKid1_krikHxNPscVgHqvHLn0vXV9Jj80DNmz71OJQVTxvCV2LWJuivgZCiROkRhILvmVbCrlKpMe5Pot0kT7nQhjsYU87MXFCxGRA-JKWKIM33H-Li8SQ7dckOVH8WN-PN8XMHF_rarLrENS_HCW0Y9nS7KEC8DVK7tarVb2q3BlmaGz5RkOH53J6bJwKxvHRHLDcN8SA_IJ309RuSwQHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش فرانسه: ناو هواپیمابر شارل دوگل در خلیج عدن در نزدیکی تنگه هرمز مستقر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131209" target="_blank">📅 10:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131208">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سازمان جهانی دریانوردی: دریافت عوارض اجباری از کشتی‌های عبوری از تنگه هرمز مغایر قوانین بین‌المللی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/131208" target="_blank">📅 10:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131207">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
فرودگاه مهرآباد از ۵ صبح روز جمعه تعطیل می‌شود/ توقف کامل پروازهای تهران در روز دوشنبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131207" target="_blank">📅 10:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131206">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وزیر خارجه چین: شتاب مذاکرات آمریکا و ایران حفظ شود
🔴
باید توافقی جامع حاصل شود که مورد پذیرش کشور‌های منطقه نیز باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131206" target="_blank">📅 10:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131205">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
پاکستان: دیشب طالبان بهمون حمله پهپادی کرد ولی همه رو رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131205" target="_blank">📅 10:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131200">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjSzNp08Qx3KLw7TdaqqNao_CIX0YVPL8-k2HU7miuhI_AC_ZVpzk6zzrq6zONeTkl-m_DiKGkH6Y8Qaakp2QKtn_tVuQQpfB_yI1yHBxVhFwcIBLCtr6IUNOfl-G23UDsaakbDgx6M9p8xJzXhmq8sMqCMXAgqFI_vs8V9vDHl6IAGfHtZ5aXQpk05dymMahwtqZeh11MFJXuFCySpyHZeR3-BjD1SHY37JqtNJgIcK46N0imbeILMiRWnYDgRdN0uev_1TW7iZqaLaNu5qBsdzwmmceo6FgmdVWyXrQ4jx_PacfRkJqny1jnkL4caIi_lPnLOQvmwuVPPnHMOBUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oeJF44XfVEruMxcieQUlVRgOGQuzP-Jx_4cvUCa20PX-ozwRJcSzRw9JcnjHyKhgXUfJOcdCFe5hUvfYcb4sWk5YJmwA2DlGh2ASBCLxVNEKMRMXav1qLM7EkpZIOQ36mMzurp6TezDzX-v9U1Ur1phtA7xNKBnv3jQ_y4ccfkvd2pJm-LtuV0EvSMMKZttYDLfsBo_KDigOELuZ2UzAS-WjpQ9QI8u0Hp-UeAAeRSOdLq4RGQzeYUFiblOrFkcuuL21bzeTMId_-GRbHUtCVUg_iwlnqniDAwQnq0C-XJrdD9kZRAw1UA7PH9yaw80rP9qgOUv4za9UcbWA-fz6ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CcbalJkMHalLphPOgOsr95k-BK6N0Py4Un8G1periiNQWsdQS9IkKc1_nAzjuGrvOobtxvJVQSsFPNbHM4LPV3JvwaFKO7NQZTk4Q0bDnsLtOlc9K3_1hB3TUiC-5AuQw-nO8pipxG6MBImGkcrGrP4KahkZHNhaEP1BEYMlkLxJukiIWo9yVWhy8e0mqBDZBGKRTKnEaFXUx5MrAJQed6lTJoFD2g-JdFPifxWpqWr7g57rnw_on0zHwx_OWTXSKPGpEN5IzgitMDB0QqifpkxcKK4CueX7cqEsmZKojTCzEXXTRoXw6HKVYrLITYiYcfOOz5yv7058ZzjH7DpaGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MW6zz7NTLmAJXG7dml_X5ZS-HDU0PmHPpWSfeo7-I0PHGlo6A0gAqD4PnjMynOervJSnxIUHHSKWp6yIX7mnan1W1_d4q9D5Mukh7nSW_XC0pKbBDqSziztcx85kWbf-vlqqjm-7cn6H7toQcxRfqYnFryuMdqeCL3je9a5InsBVYOM7-e4M8tDvjMghSON2inCYOQqse0c4XUTqv00xWQmhNhum5nIEfHgU7OrLHQ2DpsZlDCQh5MhAelDvFDurJwD5nlxcZi0jHCskuUwPtseGxePU0KzVTi6pSM0CBx04pba0_JjWLOYmkmkvWE_Y-sZXDOh4toAzDPPZha3EIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2FDerybTrSqGdZR_ttTB833imwxQFm_nU4hUZJDd5DmrdqSp7gD4FvHzgClFHZ6yhVh5WNtCtZwKfUieo-Ai0aknnBBMZuR9_kqq2eeqyZzDbsdCzUc47W-kw73boQIHZbqOfPxH7Fp2yvpfv5phzoqFja8C0bgs4mVKnCgjr91eW0T_-fcScmCiWMmf9XMmQOb8hxALVb7nN3xTTfm27RDqqg6J-_-gI5qpM8ZEx47g8MzcQyrQrtt_6dNNMqFBvV13yocMEe0PTZIjxLDtwXZycTDtIcSk4wyCHUBMAdwYgbiLWZaRgKPIhUtnGtblRZAy6rDxsO0HCRrVBx2SA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات ارتش اسرائیل به جنوب لبنان همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131200" target="_blank">📅 10:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131199">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bd7mk-G2KV-316EhLCokWWdXAIsCx2b-k0ZFx1W8plXJ8BQtaakKdjT4zdpEe2vYV-GQlOdV0Qg0nC2IRcBz6ehNEYMsYB-Ws0njQTIM2TRKWNA2AgcTuAZuePLotNbADWjc8D6an7AT5iZ_SvalbfaPz4sLFx6qUD_NUu8yq2i32jfdaiD4mgFbFYvCXwriswrEhzee69nsbSTaw2bmBAlREEG12hJ7wF5gzdqvkNggx7iE5iJAfoao3wqtzmh0QHqnIY_pgOrDlceNHTPiBlUst-pY4IpSvpxX0yOyVINmKA4iEIf07OclA2ZyMHLAsZtFzjZNTEdyzGvLrcGEtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ناوهای یو‌اس باکسر و یو‌اس پورتلند به خاورمیانه رسیدند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/131199" target="_blank">📅 10:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131198">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار کنترل شده در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131198" target="_blank">📅 10:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131197">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سخنگوی دولت: سه‌شنبه ۱۶ تیر تهران تعطیل شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131197" target="_blank">📅 10:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131196">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
بی‌بی‌سی: ترامپ در سال گذشته بیش از یک میلیارد دلار از فعالیت‌های تجاری، به‌ویژه در حوزه رمزارزها، درآمد کسب کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131196" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131195">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
خبرگزاری بلومبرگ در تازه‌ترین ادعای خود به نقل از یک مقام آمریکایی گزارش داد که استیو ویتکاف فرستاده ویژه رئیس‌جمهور آمریکا، و جرد کوشنر داماد دونالد ترامپ رئیس جمهور آمریکا و فرستادگان این کشور در روند مذاکرات با ایران، گفت‌وگوهای مثبتی با سران منطقه‌ای در دوحه داشته‌اند.
🔴
این منبع افزود که تماس‌های فنی بین آمریکا و ایران در چارچوب تلاش‌ها برای دستیابی به تفاهماتی درباره توقف درگیری‌ها همچنان ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131195" target="_blank">📅 09:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131194">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2068fce62f.mp4?token=a9Bljp48g4wg7k80OF-sMCBSm0u8WFdbmAV6d-Z24Dp2yRSV_5YDiFo6wszEPvHSnXHvRvJJI4zExPaV7WmHbIFXofhyfj4SJk__meuMBLJRrPqjuMsF2HrHcUb_Njt16ZhOWR5TK_4KMG69KWy59GEwkgJC1_nHIYznrhmrayFJCgqLSeXaE4bhABgi8lZ-QRr3U4KD-h3hQAzX9OEGtAzu76YisoQBJG1PKPKVvKRuOQnX8HZkx6agTfq0WIZMW6lbwMW5jPr1nx9s5mVfzKn3dNJnBuqOINEp6e7DtUNMI9lryC-KPjFaI1j3OoHrjWmlC2RMMRh0NLSQk-Mwbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2068fce62f.mp4?token=a9Bljp48g4wg7k80OF-sMCBSm0u8WFdbmAV6d-Z24Dp2yRSV_5YDiFo6wszEPvHSnXHvRvJJI4zExPaV7WmHbIFXofhyfj4SJk__meuMBLJRrPqjuMsF2HrHcUb_Njt16ZhOWR5TK_4KMG69KWy59GEwkgJC1_nHIYznrhmrayFJCgqLSeXaE4bhABgi8lZ-QRr3U4KD-h3hQAzX9OEGtAzu76YisoQBJG1PKPKVvKRuOQnX8HZkx6agTfq0WIZMW6lbwMW5jPr1nx9s5mVfzKn3dNJnBuqOINEp6e7DtUNMI9lryC-KPjFaI1j3OoHrjWmlC2RMMRh0NLSQk-Mwbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گرمای بی‌سابقه در آلمان؛ خیابان‌های برلین را با آب خنک می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131194" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131193">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92e2ffb510.mp4?token=JdQQZuOPiSxbvio19BMHjc96mDEfqggKFvZnHZqYhsy0s7M7Xl_I_fW5E1JuJMjspSUyOgHPlFneCWpmax_DZ8C7px2lxupfY_Yg6NVFOLhSz6upqr6PhBTQIHL7JuaxOLLlolnftLVShvYFf4axwh1jItYens7ulXmqBTjeUKzfF4lGdFSXibVS6GKT2nQKdWKg4gGqHRYEl7v_BuplOutEO2kI1f-6-ZqWnWvukJnafT2u_Ls7_8UvJF4y9A44MWIqYHGo0EQ5_iWh2uIzFSNjtv2nBYjZUHwX5qGPz8FZmRZ9k6Wm31ic1CqivFMU2Ra_esMhx-mVbVhmycjgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92e2ffb510.mp4?token=JdQQZuOPiSxbvio19BMHjc96mDEfqggKFvZnHZqYhsy0s7M7Xl_I_fW5E1JuJMjspSUyOgHPlFneCWpmax_DZ8C7px2lxupfY_Yg6NVFOLhSz6upqr6PhBTQIHL7JuaxOLLlolnftLVShvYFf4axwh1jItYens7ulXmqBTjeUKzfF4lGdFSXibVS6GKT2nQKdWKg4gGqHRYEl7v_BuplOutEO2kI1f-6-ZqWnWvukJnafT2u_Ls7_8UvJF4y9A44MWIqYHGo0EQ5_iWh2uIzFSNjtv2nBYjZUHwX5qGPz8FZmRZ9k6Wm31ic1CqivFMU2Ra_esMhx-mVbVhmycjgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر منتشرشده از پایتخت ونزوئلا، آسمانی با رنگ سرخ و نارنجی پررنگ را در زمان غروب خورشید نشان می‌دهد.
🔴
بر اساس گزارش‌های منتشرشده، گردوغبار برخاسته از زمین در پی زمین‌لرزه‌های اخیر با پراکنده کردن نور خورشید این منظره غیرمعمول را بر فراز آسمان کاراکاس ایجاد کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131193" target="_blank">📅 09:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131192">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
الحدث: به گفته مقامات آگاه آمریکایی، دونالد ترامپ در حال بررسی بازگشت به رویارویی نظامی با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131192" target="_blank">📅 09:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131191">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
میزان خسارات وارده به زیرساخت های آموزشی در جنگ اخیر حدود ۳.۷ همت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131191" target="_blank">📅 09:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131189">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pII8155ElozOgdERPw8d2jXuSP_--RpDTb5PqwC_JdkZ1Ptn6SQIjl09apxsbMoDaRqCgvy7fFtuL7cc8N6rDFfBKRwSnIHKX7LdlnJyouw64FwLpAuryd1cATaoB7W5Z1Mjwafw4zB7IlhnZYuKwFtpM8m7NN8xtCRqHFUbl0IekK9_zAEmFDFu9Z7LrhKOxMqiwZMGSwLPwRiM_bdpz02CzIFJL4B-uB4JfOK-ozsL2vrfJXXEikjjGkzzgO7c70WX67kmpsuDbd5DhytG-h_H_4LIW6X0Ir3WJQ2T4EToHoYZYUBC2R97Tdos6unWGIn7p-cK4uG5REQvNP5-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r67XXEzb0IzkrjDbCCOKS7xfbGUMCZjBhniwtLRZTq0NQWYWVpF4qT9ARU0VGcekSSOi3pnOMbzBsn_SRoRb_zk9pjjgROZhTuz89_o9r1gdeMrtWSmV1mRg_kAl0ddNGlirFLe6ajR5Pt7bJwKXbPBrSts9kCaHeD3N-Y7aujN_kijYzqb7-A3y2ij8wOplCN2HdHq7K5P9rEguJOrmz4wGlToB7s1x2GJJdC2GPUBLbiyoxScBQD6hA7nQSyPNaxUomKFNr0NUqa0gRp_bpu10z9ISYSCwWquZ7bqS8xBew60dCcRJEj09SW0fitI-NioB0c2aQDMiLiDrC0NdRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اوایل دیروز، پدافند هوایی S-300/400 روسیه تلاش کرد تا پرتابه‌های ناشناس اوکراینی را بر فراز مسکو در ارتفاع بالا رهگیری کند.
🔴
با توجه به هشدار موشکی صادر شده برای منطقه و ارتفاع بالایی که رهگیری‌ها در آن انجام شده است، این احتمال وجود دارد که اوکراین برای اولین بار از موشک بالستیک آزمایشی FP-9 خود استفاده کرده باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131189" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131188">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz1gvltLY18s3VuR_OMNd4zV3lbcsIjMhj0lu1T6zrx2tfyF_-qbKQCiwqoJ-PNLvX9J12scYM3bqDMxI2TfV0gNmPr06iMKvpssDJaOWvUY1AucBC_LbmjWETb8_bYvARdE90h2Jl9XIVFZXjqV32lXrgdqhsVQWpAmpdHif6CmqnZ-AqvvazequjtJu296U44uyLRPx22evVaC-wEENXYlgh2QOTx4we7reh5iF3_Zte7l0WcoI2qZwD7F85JD8b_Y3U95wHf6SVBePzti3tkbbmB2Pt9nRm1Md0aOCcL0TcfVDCxGw4mk3bJlzI4VxAc3IuOp4-k3ZRhEmorU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گفته WSJ، رئیس جمهور ترامپ اخیراً در مورد احتمال از سرگیری حملات نظامی در مقیاس بزرگ به ایران با پیت هگزت وزیر دفاع و ژنرال دن کین رئیس ستاد مشترک گفتگو کرده است، اما به گفته WSJ فعلاً ادامه مذاکرات دیپلماتیک را انتخاب کرده است.
🔴
ترامپ معتقد است که بازگشت به حملات تمام عیار می تواند مذاکرات را تضعیف کند و شانس دستیابی به توافق برای برچیدن برنامه هسته ای ایران را کاهش دهد.
🔴
او همچنین مایل است اجازه دهد مذاکرات فراتر از ضرب الاجل 18 اوت ادامه یابد و در حال حاضر از حملات تلافی جویانه محدود در صورتی که ایران یادداشت تفاهم فعلی را نقض کند، حمایت می کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131188" target="_blank">📅 08:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131187">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eky42jKYDcb_Cjv5paQHlY-7r9mydVk00eEQtCurwwOCteDGkyyabJVVYPAZGKkpsGWYGn-xtqC38mB5RSG9DtqCzi4DnmU0KniyRsl4EeUYy54Nqvi3ZTIxv8gtOjRvmRICPABfmKrYfNH8FtTmq6AM-gOBqdpiUvmbW3fEsRa3wDObE9vMH4Eu8euL2JYSk7kZjnqaLynmHL6trFSygJLqRLqjoN_t-n-BV9Nw29xP-Id8U8vvpCWnbuQ2rsVuq0OnoCe9-r4IGtesGGNJ3ZiGXjuhcM8GgArRwrdVuL7WltVT-QUyQ9o3tSaIgorVxKNiIFOJ3t8HmPfaV9EqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش وال‌استریت ژورنال، عربستان ابتدا دسترسی نظامی آمریکا به پایگاه‌ها و حریم هوایی خود را برای عملیات امنیت تنگه هرمز محدود کرد که با تهدید واشنگتن به تعلیق تحویل سامانه‌های دفاع هوایی همراه شد.
🔴
هرچند ریاض بعداً موضع خود را تعدیل کرد، اما این اختلافات و تنش‌های دیپلماتیک اخیر باعث شده آمریکا به کاهش حضور نظامی خود در عربستان فکر کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131187" target="_blank">📅 08:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131186">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ورود ناوهای آبی‌خاکی آمریکا به منطقه مسئولیت سنتکام؛ استقرار گروه آماده تفنگداران دریایی در خاورمیانه!
🔴
در ادامه تقویت آرایش نظامی آمریکا در منطقه، فرماندهی مرکزی ایالات متحده اعلام کرده است ناوهای یواس‌اس باکسر و یواس‌اس پورتلند اکنون در منطقه مسئولیت این فرماندهی فعالیت می‌کنند
🔴
همزمان، یازدهمین واحد اعزامی تفنگداران دریایی آمریکا که بر عرشه ناو باکسر مستقر است، به‌عنوان بخشی از گروه آماده آبی‌خاکی، همراه با ناو یواس‌اس کامستاک در این منطقه عملیاتی حضور دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131186" target="_blank">📅 08:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131185">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
آخرین وضعیت کیفیت هوای تهران
🔴
شاخص فعلی:۱۲۷
🔴
وضعیت: ناسالم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/131185" target="_blank">📅 08:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131184">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
افغانستان مدعی حمله پهپادی به پایگاه‌های داعش در خاک پاکستان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/131184" target="_blank">📅 08:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131183">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfzbHueXu6V4cRwPq5CDJ3yIkZqvjQkwqMunwCeK9hlowFRpzZHvKuW9mWqO474BjSY_ndJxKOihpVaFrccH2tYnFx9C5ZfpnYXYQMerVYq9HXfC0WEQ-ZkjEL9QHl-MEZQwfvTEJlzCN20UdBIlrf2P5jCtIPknMfS5VYtbucA0NntynHdtM1UAlVkgMg9tmSrH5jGeQRLXD0197FYllL9t-iOWjOZ2Qa5LBaxep3decvRkgzMf46agGWp_VMYdpU-ouk8cUF3dJz-uuNP7btjKaUGK1yh0zvOA1qtXWRihaDfIV3dD4oPzwpqLemmozuPfZiJVTa7zqFXo8SWQBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این شخص غلامرضا قاسمیان است کسی که یه مکانی درست کرده به نام پناهگاه زنان خیابانی که اونجا زنان رو جمع میکنه تا خدمات جنسی بدن! و اسمشم گذاشته شلتر
🔴
قاسمیان در این ویدیو میگه خودمم اینجا میرم و میام
🔴
صدا و سیما هم یه هفته هست اینو هی میاره تو آنتن زنده…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/131183" target="_blank">📅 07:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131182">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjUm60J2_fxMu28g-gG8qu-qwp3GefvcrrZS0AzcC0oFsSOZ6iTJ7tlkDwRXd9YRxa8Mh2Xsm_ETeu08hcDTDDphRethwO2JezDcXmABMztD_FftVmH81Fu7Rd1leIt_A_WuWCxPIUcYtnNLPHa8f_bv1tl2QmIvddTmJK6D5zT0b6ZdHFAOwfDL2UqAFGvoi1E_y8wO1y18nOvmQVHjb4U34EFDhJF_PCZVmPEerwm4-GiNa6nBIdPzXle06B16DOJSvxBdXYl635yeM0-RBGKT002Kiv1KOMZezLwWO48VwTXVUy79AahktAITDea6bb_te5nFvAZscmRVNfboLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده رهبر در سپاه:
آقا مجتبی رو خدا انتخاب کرده و ایشون یه پاداش الهی به مردم بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/131182" target="_blank">📅 07:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131181">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/131181" target="_blank">📅 01:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131180">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکریپتو اسمارت | Crypto Smart</strong></div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/131180" target="_blank">📅 01:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131179">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsIDt1UwQLr6jgUWXl_TOc6DetnTSmAgr6QTOfcg4AYeuiI7odAe6avZMPwiiy42sxC6dZR16VPRrcAIvMlTD-rUX3-u2PZ4ICbgEd-8t5EbKqREvO3tIBwiLkD5fBwnwOby4U9rviC5kiTDoA2QAPFUktPugiwWH0JzlWfhJ-JVIJdbTkdEBPhvOwCP2G0Ih1AzYgftChKrlkze47ZCBSsIggcDwTacRPKptuHLO--d84cnhTsqRs5P-405s-nyoUE7nwTBxyUhYkcLYKOcggr83oY8f-fI_49lCUfA9Y4DISPsn6zEHCikhnV2GubfTuEb8HA_FRJ9XaJQEOf99Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حماسه سرایی پیج تیم ملی از ریدمان قلعه نویی
تنها سرمربی بدون شکست ایران در ادوار جام جهانی، مرد خودتی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/131179" target="_blank">📅 01:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131178">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UU8b9571LgJ4YWwEGzgRMEAQg-ra2PPyoBmZ6HcEEwDMtLizHtZCexfQF6GKzkVfRItHjGC-rfShV6z0MAZQtKFSKjioq2RKsEWixEiC4_UUzUEMYMrmAwjDjQts9TQvr9hM9-ijNUlyWN9neotudBJeveNqWxUBLdLYnxRLAKeScf8nmyfCKX6r3gzjAPHr36a0H8vnQ06wLD1Gl1P1rHtgO2jo0Odinv-ZNF39mDW80-ydR2er0MwdVCLfKLR-yOzuzVNBmHPS2rEHATj2XO02BrBS6HYCcETj7Ey_2xTWzEaNzalKmAG5U_hgIMRortofmoVG8H7ytz2v7TogsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون ترامپ:
ترامپ از وقوع جنگ جهانی سوم جلوگیری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/131178" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131177">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaUinnckxJ3yt0QKF8P7IfjFIm2EW1Me39oM_0LCeUpfa-cjqkZEIJUuMZsw3p3KAdZ34I4VP--GhK0UWHQ3cthW9GwtOxCtXQklmhcqePBiIvS0nRHtJvMAcQLVtMjbiCbI8x3NDUVsooOsJFKluNrd0_Rww9TD5lV9gjn53Dp7yEFhdUjYHyahVUnBe-IZaxJAfTOKbM-BGP12b7wI9qtN6A4XUww-v0pSQZEw4TKZwwfyaQLNLU81gQdDYFsJyHN-6sAvr6lHVxDRFCWrc6Z042Kn3IqcqYQc_C6rY_bKRrXg7AmQIfiodR9qvhPOKiurrFepNkOmVsRlrS4F6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طوفان توئیتری طرفداران قالیباف علیه جریان خوارج، از دقایقی قبل هشتگ
#اخراج_جبلی
در توئیتر ترند شده تا این شخص منفور از ریاست صدا و سیما برکنار شود
🔴
سالهاست صدا و سیما در انحصار یک جریان طالبانی است و تقریبا مخاطب قشر خاکستری را از دست داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/131177" target="_blank">📅 00:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131176">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jktT9hdc0bl2x2xeA7hzpSoaBaMeDbkrWMO5zo2xC89mLEtveH4o1E0zg_yRV6OfxkMJNVSattbTNH0dtHYDbAbSD6EKOfc_AkrXd_XLeSuBtBQK7xH35STKNLJuSfgKpegRcLYlx-qESKN92rLE9b1MUn3zCgA0zY0fn10gS4uETm4H5LhWosOaNmXijaL5IZx95_Y-hdH0leMR3FklzDqMFNbNKh0HxfGVwZwlk3kD5_hJDst_Ae1XGTE7Pq8JMBRWAH9146fsNGC2C6r6XaCOJtnUEzvkVC7k_xEGc4Fy1uktH80RBLFtph6xIh8rtZBjtCh1zfL-9S4VLlNzqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جبهه پایداری:قالیباف مجلس رو باز کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131176" target="_blank">📅 00:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131175">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95ddaa0dc.mp4?token=VlH-c9nMbrwuZEDZ2cTR0QAuXVhqJriPccQbUEq4pzKQtOKKyKNb_czdcFt_AQ01vlcF2Ng0Ri8s65lDNvbFS1ONHXAwbyFk8ptGXu1Wd5KfFUiK612RwDHnxYk678-fuqXz8hWfONbn5jBYOivi3uUFLC8wy3ovsEfOEw-cKGw-Yul37EXAMiIW2BtPBqzfifuSdrMmKBN2WdqeEh5Dna5mQDh1p7X5tEAfvfkTzLx4h7q87o55r_-9lmsuAleCHgt5WO5WydJEQqDVkjmd9xzs9Nv0BNBvHzjexzIwkflT0sqxe6TGJ4OVPnOIxeeFj2ve2lzKtQ6MOFWm7exYog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95ddaa0dc.mp4?token=VlH-c9nMbrwuZEDZ2cTR0QAuXVhqJriPccQbUEq4pzKQtOKKyKNb_czdcFt_AQ01vlcF2Ng0Ri8s65lDNvbFS1ONHXAwbyFk8ptGXu1Wd5KfFUiK612RwDHnxYk678-fuqXz8hWfONbn5jBYOivi3uUFLC8wy3ovsEfOEw-cKGw-Yul37EXAMiIW2BtPBqzfifuSdrMmKBN2WdqeEh5Dna5mQDh1p7X5tEAfvfkTzLx4h7q87o55r_-9lmsuAleCHgt5WO5WydJEQqDVkjmd9xzs9Nv0BNBvHzjexzIwkflT0sqxe6TGJ4OVPnOIxeeFj2ve2lzKtQ6MOFWm7exYog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حال بچه‌های کنکوری خوب نیست...
🔴
یعنی مسئولین این صحنه‌ها رو می‌بینن و سکوت می‌کنن؟
🔴
سهمیه برای ۸ نفر المپیادی ردیف شد...
🔴
ولی برای کنکوری‌های ۴۰۵، با این همه فشار و آسیب روحی
🔴
کسی به تعویق امتحانات  توجهی نکرد.
🔴
کاش یه سهمیه اعصاب و روان هم برای کنکوری‌های ۴۰۵ وجود داشت...
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/131175" target="_blank">📅 00:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131174">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QTifggK8J9d9j4cW_gHvyTIYKFuMI-aUdGHOzz0f5m4RbO2voG7Qvv40ffv58yu-jJlB6oEgY40cd67jYkfoWQ5DhY_cw6OhmM7LZ-KUgsuuKeyHTzB2w016a17kGc_kR16VvlalCo1dX3Hi170Tr8KrZobhHqc9QfbqOdzhJW6CwJ7nU8Ip0JhJpY9KJ0AcOCy67fwJiGqSJPB67ZP-vGaFRDBgpxzbQsWurLkHwqh8RuaIH4ctURE_hOyaG7ncD3YGgnCEYzcBn4h17lDnW9z5513Mx5ELgxPGEGPnSf9OTk1P3aZasY7avfgr5J8lDr1byBfsFtaiBJ2tGe5U5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما: قالیباف امشب خیلی حرف زد، بقیه حرفاش فردا شب پخش میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/131174" target="_blank">📅 00:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131173">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c196a09733.mp4?token=Qbnu4jWU8KGgZLDapQP-7lWDCRPmcKYaerl9H0UqlCAnO__d2bFCSeKnUtcVfMkTL4Rlf9OTs6UE6bDQS0o3xR6SXxinPw63LSDqBt9cbb9h63v-ZvaimvNoQEjs0cAYIgN6HOy7LaAGrq69IaBNMknfa0kLR4NMpFw9WESNmzX2UV4f5nocxfAOgzTfTntsj8CvhzPaoCEdnwIgwLGwnIva-mjzws1s41rOuAZtvhXU5FGn4RHOO6vdeHCeAPOMh9eDmZsymOi3wsZ4afgm3d6CGra57sImcNNshf3ihm1p1HqjCYYcEPCIAsY7RfPWg7J0Pj1Eogitzl1gkVHVdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c196a09733.mp4?token=Qbnu4jWU8KGgZLDapQP-7lWDCRPmcKYaerl9H0UqlCAnO__d2bFCSeKnUtcVfMkTL4Rlf9OTs6UE6bDQS0o3xR6SXxinPw63LSDqBt9cbb9h63v-ZvaimvNoQEjs0cAYIgN6HOy7LaAGrq69IaBNMknfa0kLR4NMpFw9WESNmzX2UV4f5nocxfAOgzTfTntsj8CvhzPaoCEdnwIgwLGwnIva-mjzws1s41rOuAZtvhXU5FGn4RHOO6vdeHCeAPOMh9eDmZsymOi3wsZ4afgm3d6CGra57sImcNNshf3ihm1p1HqjCYYcEPCIAsY7RfPWg7J0Pj1Eogitzl1gkVHVdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بخش سانسور شده صحبت‌های قالیباف در صداوسیما: قالیباف: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوپک صادرات نفت انجام می‌شود.
🔴
۲۰دقیقه از این مصاحبه توسط صداوسیما سانسور شده است !
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/131173" target="_blank">📅 00:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131172">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
دولت ونزوئلا : یه کودک ۳ ساله رو از زیر آوار، بعد شیش روز نجات دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/131172" target="_blank">📅 00:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131171">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
روزنامه «العربی الجدید»: تلویزیون ایران به‌طور ناگهانی گفت‌وگوی زنده با محمدباقر قالیباف، رئیس مجلس شورای اسلامی، را بدون ارائه هیچ توضیحی قطع و پایان داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/131171" target="_blank">📅 23:58 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
