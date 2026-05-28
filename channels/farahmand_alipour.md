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
<img src="https://cdn4.telesco.pe/file/T65xj10RbAQWdGrKZtScce2_0HoEKzNJfFbY22UMBvYAKNUb1IQaoH5zbAeUcof8Vbm1qG39ybgZxjM3dgxsMNhLwCayynaz88KrL8TUTFox-QhPyLGG1Z_FhpCa1LjZPeSoSvyIApm2k2vtOjprXeWlvdlv8xSdXl7EM_Es1OLGlU_IwKIBAyaKnriPJsvbx4T3P0uMBAvUX4_nlAS-o5BVx4h6z7PlS5z13kP97g2xRGnrUqIYF0X_EAKqEWxO3zmjgb9HXpi6y5vqB8lGtSIrFZiooMRgh0_m9l38yliZgVZYIsRAkRoVcYdHVNuNM09CcibSXEmlCrmAwxgQFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 18:01:13</div>
<hr>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=Y0nxJqA_NlJ1R3Ob-O2hqy9G6GITVzImM2R76mRjkrJMl9BFohc-Nps8H6tRE4Nn83lGxG5nRO4hyOiefZ0ZGgZaN2VGdJkQKCubx8ChLttI5AQeeokS8SMtHfNJhIj6yqqhvRW2p_NBKbaFMn54mSRbxUbBnEdY2WsvzJ3_9u27vHLHxIoC0vtfFG-ryID5IdkQD0fdcwH-kJza8DhXH-nk5KHB1YWe6wtbSnkQs-Uxh6wLPX5KHPtst03w9ypxSQl71QE5e4lfR28gztcGF7iRzxqavrUrk096N888S6wPLQE4e1qSULjK3JvSWNeducYu_hJdFCdvaINGPiXbHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=Y0nxJqA_NlJ1R3Ob-O2hqy9G6GITVzImM2R76mRjkrJMl9BFohc-Nps8H6tRE4Nn83lGxG5nRO4hyOiefZ0ZGgZaN2VGdJkQKCubx8ChLttI5AQeeokS8SMtHfNJhIj6yqqhvRW2p_NBKbaFMn54mSRbxUbBnEdY2WsvzJ3_9u27vHLHxIoC0vtfFG-ryID5IdkQD0fdcwH-kJza8DhXH-nk5KHB1YWe6wtbSnkQs-Uxh6wLPX5KHPtst03w9ypxSQl71QE5e4lfR28gztcGF7iRzxqavrUrk096N888S6wPLQE4e1qSULjK3JvSWNeducYu_hJdFCdvaINGPiXbHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=aOrt1PPpCDGvER47f29w4hAOf4Ltz933NnDIBRm8YPMXWv4pAlOWBWPcVDKct3hbNAlV-qx7tiydAZ7s2Sm9iQHkrerIZrLg-T7JQybiZtMaDz2dVqh_T6iHhS1c3mO4zdHXv1Wo-3EU6ugU5ilI7njySdiGLcOcY8eOUvziAuAqtGNrTgwVwfQ_AQbdFKV-1iPUi7jGs1hh53oiZDMTZcx8Fm69ZUC1Fr81osOX5HoBGIclCc_0WLeeadgKgLBuACJib_6YO1A4zeOhN58ttHvByYvcCg6IEGe7kqz3h1h_eQCPtj32w2opyn3_8__qcECDpcRdWRc5h1_yA2Pcnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=aOrt1PPpCDGvER47f29w4hAOf4Ltz933NnDIBRm8YPMXWv4pAlOWBWPcVDKct3hbNAlV-qx7tiydAZ7s2Sm9iQHkrerIZrLg-T7JQybiZtMaDz2dVqh_T6iHhS1c3mO4zdHXv1Wo-3EU6ugU5ilI7njySdiGLcOcY8eOUvziAuAqtGNrTgwVwfQ_AQbdFKV-1iPUi7jGs1hh53oiZDMTZcx8Fm69ZUC1Fr81osOX5HoBGIclCc_0WLeeadgKgLBuACJib_6YO1A4zeOhN58ttHvByYvcCg6IEGe7kqz3h1h_eQCPtj32w2opyn3_8__qcECDpcRdWRc5h1_yA2Pcnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Edbt87X-xpZjrPqv2Rcm23gD39bSlkA0hUDky6JxRlwfDQvcInzBhm5lzKTmzR9loh9ExVethoIwZzcdeltJIef6MlG78i3xo7oAw-YCKhJEzvvk1K7i0Y9xDvI-Tiyd6vbZBfhqBtStOT_2L3faYks1D6qrL3TK-hOKbChwFqlmrbqyYVn6cR0w2JSZ59nGBXl24DS9QHsGbddtH17UGXVdaJaGNhmMmCTz6zoHrqT_LE7tgtpAa0cx_DNs54q2KKE37vKOsrdRPud2GRvzGiyUaHDzo3lp3OyF22ptyHCaJ3k3kA78sKDQXci7o26d_6_XeKnoLEwaAs6R7xhnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=Kamsb2-u7jEVPLxiN2ZXRjgHqbC_p6Vr4D9PYsgrmq84Z-BQ4mxZRbdnDxVfAlw_jm8-MDXwwKB9zSgxLAkGEkDZOsN7UMTuPpgt0y3rKnPVV_otiwF7SNmN-ZRgaBc3Y8ZPZ6dCguBWoyM7nhJZnv7JYT5vvpLoI360TFS-kzOugG8DuruPT3SmjBBTjqDGQEEpZZsIDe4xVpxRKXXLSUyVfDQf1KUtFHFChe9eskswFW51_HXhrxEFiOA4Qy9UtxG_47xoFJ7q4SfGomUZQXdYbsDyVdx-ixnBCpcHhcMnyZahFmhcN84-HSe2TbwMMN5QCAta9V6x312JKmYQ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=Kamsb2-u7jEVPLxiN2ZXRjgHqbC_p6Vr4D9PYsgrmq84Z-BQ4mxZRbdnDxVfAlw_jm8-MDXwwKB9zSgxLAkGEkDZOsN7UMTuPpgt0y3rKnPVV_otiwF7SNmN-ZRgaBc3Y8ZPZ6dCguBWoyM7nhJZnv7JYT5vvpLoI360TFS-kzOugG8DuruPT3SmjBBTjqDGQEEpZZsIDe4xVpxRKXXLSUyVfDQf1KUtFHFChe9eskswFW51_HXhrxEFiOA4Qy9UtxG_47xoFJ7q4SfGomUZQXdYbsDyVdx-ixnBCpcHhcMnyZahFmhcN84-HSe2TbwMMN5QCAta9V6x312JKmYQ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMeB-HsSjq2YMMHj5WyeZ6XnGy7ZmrVuSAOhAM4FBXmvPJ31JMCmlFSo_g-xT84MunDxCSgvEi0Xap3R8kzA1GscHwstWvFVfvFgdrp0tgI04lYEakY9Hyx78YJPAYOMAtRKl6740QQPJIbCHi_3D6-INOrirnBbbikTBWOW7Ygu2jqD8uVCp_tvljvTIAXdzYjpDjhgQp4GPvpKkx6d9PA5tdSRMb34ORI9dSHZWiu6e2aFEOElHp9tyON6o3YdabSABBgZNIbOFa2r0GRWTmD-NoUpWekg3GRcHIOGcZ9LYo_kBLuaNJadHtOVjSHSr5Ozh6ytlBufI3SM-gNK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=j4zXSEvR05j0TPU7puX0Vh9G_hHEgehH_HrluI4sCIgo6YynJhmQzYDbH57mUN4FaymZu4OrXNIjFh1rCDLMxYCefmZRSRg2LNQY-HcGarcgRYLJNp-RiEkeb9q4AN5NT05vNlT4bAlk5I2mghbPqZqpD_6vCyfOY-hVZWBmK5736xALM1zwiKj8mtRtzVgUr9yaA6w_r7V3csVbSHt0yiobVGRK5o5KJr8e8tjCkyLq6Sv_O2hWUM9hedHzYs-H7wj0ZNUHmLzAT3M8-BoOxU2SbZWnzz1zY96BYcfJ42BHSiCQwo3yv1Vwi8miyyhQddfdQLTGpPfFg3mPuK8XFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=j4zXSEvR05j0TPU7puX0Vh9G_hHEgehH_HrluI4sCIgo6YynJhmQzYDbH57mUN4FaymZu4OrXNIjFh1rCDLMxYCefmZRSRg2LNQY-HcGarcgRYLJNp-RiEkeb9q4AN5NT05vNlT4bAlk5I2mghbPqZqpD_6vCyfOY-hVZWBmK5736xALM1zwiKj8mtRtzVgUr9yaA6w_r7V3csVbSHt0yiobVGRK5o5KJr8e8tjCkyLq6Sv_O2hWUM9hedHzYs-H7wj0ZNUHmLzAT3M8-BoOxU2SbZWnzz1zY96BYcfJ42BHSiCQwo3yv1Vwi8miyyhQddfdQLTGpPfFg3mPuK8XFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkJ8CHRFBAWvEd2TAQAYZNpShabxRdJcaVbVVKakRuLNuHK2DedtIWLLwmYCixnkjt4-jSUWhFY2j9vPWKqWrK5Pvy46abVT16XsIYLcftttkK9SVPywPUeWvYSxvqatp8PmsXt6BDnj3mZIOe7iDjS0onR30hQ_0HAgDS2DHkoFI2JwWhUcvbPI6Q11MP2A9aUbWERdSbwd6P_m-h_nofwmtf8OA_rBFy-zIB_5YaRTOQO1NRkzogoCQ_Atc9CFk9RU5hbvZaPFYcwOVYJ2XdCypTFmLHRzXaaQuZYbnHDUSLvVSt0Ge5GwK1epHs-08HWUw690B0tBmBBkK7K5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTX7abO_HBWQHB5OHCn8fQ0fVF5Qt47vGKBs4RZ-ymc9Xv0K0QuIbbghgvxfHtzGWNJuRXDgQ3AFpJ_uZVZMndKziOMAWkDrw6vEBI83EWi9vH0nPHW5V2lhwLkbB82jiV0SZKtiw-R7ycJCQRGKa2Y1qFfJHmh7oFsqvks_oAwQE-U8LcZRohEvA32P6e_79MdC48q0pVHlklseHPmR6qN-anF14e5SCY9kmxxE2hUsjNcaLUbta1w4JWIcjw2LrPWombTlfStTNIndvcpF5_Ce2ZDzAA1eozhEg51-9exRYnkrkmWC-SbC4eLXDQY28whBgv0FcbmdkOhb-0ukWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8omnbdlXorNlxVYpRAuo6P7rfCZcbQPZEHGoSaLRJyF2ozz9KVqz81ERap1vzQBCNbgalcoj-SExDRR5549WKas3P4RArERIjYTC_u_DFcyu8jZDGyZOPtiuKDuDzzO0JyJrqPHIAGO7nrog8ak614KlurVqZV7fNgfPR__MlYjCdxMe-LoP4U1Gv-3q4HanIe0LbLsBnHtcw82KMIDop7Y2qgGiFBIicGrjWyJjSEZCVsqGiheHY5WQRvd4BTFlBE7g_RzkKIlCBawDF4FlXGbxToD6oXfW5n3t-I9IamhRrhRQw8RtM8EufMYhg8s1aMOkRPn2dqYFypSidPIvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijEOeEETvZ-GNeuJElr77oI-Lwvk3-SY9nS83vxHkdCfr2BRgTQudXsrfPxneQhZwvKyROyidOnBgdyZ1n4FmC8k7rUK-jceWdiASxp5rq_MQa6BvwZIrezlZnPVJmjDuUgffd8QJOBrEL13k0d2OmPibQEOIK5kYWcpe0Qmj6TTFpZt5Rh_gFr18ZCByLffJ_O1KuMPvycWm0OmO0ayLdKjI3s8xf0yJCwE6uvESsy_43fHu0Zad72LQlgsZGFggPMOa-4A_2L8Q1-DOPi8yQSpX24_7yWf8bc501UKCh9UZy9DgkyT7COxgiYvj99Hcep8WvZ-IUMXa_UUeUyU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vknurSUj5MKClQsp4e9AqoBwUsqXu8sqRxI85EzmfpvHX0nkezi34cfC99d7CUYTRCL2nhK9xgmnSedZI6qPPqqbBUDfOBthbiHKjLlW2Kf-HjLXVTughig2xolNUhOiB2riv1H2jcmGRWg7sy_sFDC4exoPFmlpEz3IlCgpcYMk9ZAhEUBHb3DlJoV2W5YPC19FyvURheZy3rp3q8c2RJDBHzd7jPw6KBrVkx_bEL430DHCXg3pnd03thWphZo6qyDG3yZ6SBCPi-42sS6J8cfOFGTAgv_hn2AmlGh7EB6Rz_srLI2JMVwwhjbe8UqwpcM7djQvbde5Oh1nAjM1BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIDPvvCBsjwjzytJq0K8TavZNpU8bC1pt0knmRzaJGx7dng290phOpqudGh8jeYaNsrY8qqjdBQGTNjott-pzjtcOJt2a4zJN1M8zZCTnrja3992PgC04oqkVZJ8XDqihSzAurqnfetKG_asgPPIn1v8b9ZxYr-DefXv7LZGtr4z9Kr_E5hLB7TtvYkqURaKSOn1Ye4Alf4ToYCO9EIlBhpB2iypOGOPNcSbDDv3xMAEvWfre64Md1ONOiftIr9ynFJvQrWy-5JNxPhF9JtZxbbxWOlHSE5wl44KC7bwd8iIF6YuN-AA-GNeOEj0UCseGU9s7kkHo0KGe3vGFfY9TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quASYbv6tYX18IfIEwbFxG_cGUqpAF7cDfcAE9rpWj7yUNXQa1UlkeaaZM8FoqoiZmIGbx__swPb_zNHIQ_MxcZBPE_SbS5IZDH1kHTAHo60uNi6o9WxB1j71E_UkT1r2eDFpBP9jqY5eGoS5VVbHVzihmzJMe_2fsSMh5UDgwYqNusC4fdJqWSZWtvDg6VMLGhifUSphxGT3hAjNUHstBTSIdF0l_X1TJa9fOaJ688XnwjDvljrK7AL8aNAnx0D_eN35JK4hNRrAnzf93ON4w-toi4X7q3Qtb3BJnnz-KOO_y88JpYMQ3avxJT-McRggZoJR9w5eDAiehYZGhrquQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7HI9uK1YjtkrwjXjriEZ9Mf78i3aug9DRxVxLzsw-GFEL8uVNypFJB_g2SAbbxkXEqA3ltCh5ztafiTIdX4ErvFUOGshSYDwwxgQ6jDk-iVK9qjq0xg0f-eeP9lC6WR_Sh_VgtP-9COjyi0vBh6bp7rur4eZSmvMJY1g7fiW0D51UDHAtWBC2E8yv-zdkOY55DPlv0vsV1VFHTfxnwMmJpTt1eF1mzEzt0A7Fs5S2ijC2eY5ZL1YHwkTEiXpEJqwU6mFwiOFVtLjOzjT9iwi-CFKi2mVRTAP5hr--TGIrXkaCsfPvJEk61Scut339kWtnmWcQ6qB9XQA6wmOTksSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=aaGoHH6Rq2v3CWph9pim5DplYvOSyEjVwU9rLxpwMl2oIMU6omO1cE5iGTyvEXyUP34hxSFjRQAHNdChW-Lunhcb-URw6d2-BeohWvJS9dQNtd8KCB7CqTaDhmtFa3_4z1TPKCZubdp-LOVQfgb_7ySMif0VQiWPWt3oY6FNZNgl2XmPAppVKY6stRVGHZ6C9B4ORgqA6u8pDw1V8Dr45chsSluIv8Fpezw-qTxNoF2hme36PpPjKyKnRu2YKH6vkG6LyFHiiJpaWHY1Hb0q64aqO_G75rFfcBNGfZyzo9El5KD17BbPFxaip9m3puP6zNRIDEM8MmqCSGDPQM4RwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=aaGoHH6Rq2v3CWph9pim5DplYvOSyEjVwU9rLxpwMl2oIMU6omO1cE5iGTyvEXyUP34hxSFjRQAHNdChW-Lunhcb-URw6d2-BeohWvJS9dQNtd8KCB7CqTaDhmtFa3_4z1TPKCZubdp-LOVQfgb_7ySMif0VQiWPWt3oY6FNZNgl2XmPAppVKY6stRVGHZ6C9B4ORgqA6u8pDw1V8Dr45chsSluIv8Fpezw-qTxNoF2hme36PpPjKyKnRu2YKH6vkG6LyFHiiJpaWHY1Hb0q64aqO_G75rFfcBNGfZyzo9El5KD17BbPFxaip9m3puP6zNRIDEM8MmqCSGDPQM4RwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfOhJJ3L64WqMYmjhcQ9Lg0jQaK5euGx3R2zeEOQPM2d5HCip8AAvEoHntjMy8C5EhNUWrjdCM-H4RZIsdRYjNdGAH4AKNuxxEm5qvOQcrFx00hexwYDjREajjfZByuvGMZD7lmWwx3n3hmjR3OdVqwv3blKDTZ_H5VD0mCmy_hLv4hdR2ZeGx_gE1l-iyXZxcFrsXTjzIvoHY8xXfM8xyqaGFOKGnZGjpBcMuAqXrU8M_PtEJnTHKC04tUrHsOxYoozvmh2NFuyVnQDcz8TMBk1TAyNmy47BMhHuVplKJ-bQ-keLWP57J1Mj99Y1DVh1EeF28Oz8w8xe2lZAHLpoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTOE3ggsXaLLLPwyNTxkmcS4bCG7wRxzTza-4dfAUmO1Q5raCUl99bFGspE62a5CI9ckODH59EP3jAVVi0eiC12If_FEQE5PJ47e38cFrWjWzD6S7BRSGJcEFwwYdRrs1bnDsJcm7mHJROOND7S-oZDvjQue8nEcCUgSk5ZKy4a2y3x1WgZ7qoChhuEksQOu1rTMR1N2ESbG7KN4RBe8UT6hIbT2fjocB6c49G9PwF6mqkRw-fASbtfAALrSPN3QPwNlfMOhuQ9VH2f3FgWbFlMLQCJ6HbtWBiLWdXxx0-CzkeA3I7dix9lFRwFLAxwhXLnz1BCjaajTkRl7vdCD-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9tqR0m2M_sY7o9z21CKfHbEcToELygKFmbpq9x7eH5RKQD4WWATVQc17o5hFclOSFLHOar9H_yMWkpo6kl5fewsCb3EVYzVxoq0LAduPZBO8TPFga6NHItfujGf3zRO4gMSXownb3k-GnvTFD4w5jVF4NAAzGkDTcrDSUZX1h0pGZXmv7rmWyUdNa41kpoIX6u-aaOEGAKz0OY6Ce0yItcmH7XjnxV9-__3nuZQHv7IPwv1t2fQoyPjoNdykLdzyCWYp3X7F_RPkeLsqcrzIO0Q9WJd3xIBur_KUAEy72O-IMP74bYrcpSlMB24eRuFfnCvvROxzwuZmOn57RWsmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGPocdYoSl2hduZB8hx0JF41PXnXfblN2jFpqzPW7xTEA7zP1Wv2eUkIOD3qL2uQBupcCPwFSdzgfulJ9bYAEFbj2r996bXm_Xr1PO1QSO_-b9oq-N7Dxr_L-Ium9Lh1qlfQdCIlu2ej9KUl0DYKAZRmFmm-uGdcyTFybyIjnml8k0tSaXoKsz37WsKz0IhzuGNtXlk5yFdORLNbD0KtOhljZrGeROqmQiZ131i7XnheV19C0OZiUgT9Ye51l_Sp10LwGmldoVi0e-tbuYlG86Tq5j8nSFKMbiOLCkRKatI3wfkUtUxdGe3_ZJrm5FAcl9EWSmyT0l-cCX-yvyM8lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5cyOhD7URVvo3xlaP1uk2ME-26dp960eE6ybZCUi7S2boan54VCnz-Tc1YYPLq3at8VbERdFieAQX0Hd6c00386MtyZCpSLFeVL2qy2R9JBFadHXWsNqkCpVKTye69dVPsNYnRC73UmFleaqj7cnHXyt0PlUS2iNWW8MTuU7XaRF-6wn2bWPLr816gbzql3zmfApeRSQFqOX4fTtQ7i2S2_gFbvojxeZ25drzPlCOSjSC3ET0DznpDXoirGxkrqWj4ZDaNh7u_BDnUQwZM3yIE5LLLcLuSQzGbRVBBU_fyHBeOYsZ27-jaye7rz-TGrboRemwKCXjsRsj7wYCUC_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=M4WVOlsuHc36Gbqd_XP38cssDGyHNzpw39iiTK1VReEgv6xjKVaYFC7CWrBUpUNp7sUjbNANFM25_vm0VoYRuNI41ZMU9BqVhaijKAqdWT9FbU9pa8FAHZkm1z6l82YLPl5Kw7BgyjnT3tKyAxqp7gpAY-Nc4hQlic4v2ZVJl5qWWUgKMCrF7C0lhWfoio2MzweCm5JHst7UDEntU6-mHj6d_qcmBo3MJm1IM7_Ce-H2P8KUh8YXwGefwwOTHTzfzdakKWhisfQeUK-6J8g6WkVN_gLJkNc_omuIQ7kbKhbbgVeF92ulMfrmg3GWAYVyPVAQeJABxRGLmvNp8Gn38g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=M4WVOlsuHc36Gbqd_XP38cssDGyHNzpw39iiTK1VReEgv6xjKVaYFC7CWrBUpUNp7sUjbNANFM25_vm0VoYRuNI41ZMU9BqVhaijKAqdWT9FbU9pa8FAHZkm1z6l82YLPl5Kw7BgyjnT3tKyAxqp7gpAY-Nc4hQlic4v2ZVJl5qWWUgKMCrF7C0lhWfoio2MzweCm5JHst7UDEntU6-mHj6d_qcmBo3MJm1IM7_Ce-H2P8KUh8YXwGefwwOTHTzfzdakKWhisfQeUK-6J8g6WkVN_gLJkNc_omuIQ7kbKhbbgVeF92ulMfrmg3GWAYVyPVAQeJABxRGLmvNp8Gn38g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3V8I1HGtFq78G6RoJM0AYx5nrzYJjZpjKj2va7OVaS4SkEIywaqxgSgBClMYfJfY3mI-bqqgbopM4-DOCzKXGymmbv_iUtpxA-Z884zys-Qp1N8AX2Ri6mlqwHnQ9H41MPAsxoh_brHb6kPGUiPuDZp3un8Z34xsQWqX4aLHZmmEmPq_-7IoG9X5S3WiVR4SF-SZaXWfoLrZ6zdXr4QdPA-4nKLOqecx4BmLS8jgZmmsJiDmbfGBmTc1WatCBNvHnUkzLoXJiTneXjk2V2qvf8LHTbm8LftQ1SBdGTKLEIuvQHHL8lkig9doLPT59Om1E1dh582hwdgdASl8V9ViQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=OqY1gEZqcmuLOra4OjF1dPkq_lxIZdC0Hy01ZEuNBtSLNEmqFzAF2rwUtPucG7k3OZDZSmd4fOChK2_9mlLlu8lsgYR5i0xAVX-deuM3f5ejA85adWF16HuDPMTxswP_u9UZCLoHvMtL8R9K09QYxyPKiQaUYTG5e3tRS9SFhCGa5_s9pDryreDrenyHiqE6Jxz0qDzRBmaGpuwzkJA2xgJVvjATtyzeer2d8xMl1FoQHV5W6RGANIM4__Hb3OrB9IF1nLyVnS_vTZ1Rx0z4wcEyrbyTiagl6Ooto866_cWKCMIevhhuHXZLR3eW0jzl9hdcR640ayJG_DF3z6Dx8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=OqY1gEZqcmuLOra4OjF1dPkq_lxIZdC0Hy01ZEuNBtSLNEmqFzAF2rwUtPucG7k3OZDZSmd4fOChK2_9mlLlu8lsgYR5i0xAVX-deuM3f5ejA85adWF16HuDPMTxswP_u9UZCLoHvMtL8R9K09QYxyPKiQaUYTG5e3tRS9SFhCGa5_s9pDryreDrenyHiqE6Jxz0qDzRBmaGpuwzkJA2xgJVvjATtyzeer2d8xMl1FoQHV5W6RGANIM4__Hb3OrB9IF1nLyVnS_vTZ1Rx0z4wcEyrbyTiagl6Ooto866_cWKCMIevhhuHXZLR3eW0jzl9hdcR640ayJG_DF3z6Dx8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخلاف
گزارش صدا و سیما
۱- بسیار بعیده آمریکا و اسرائیل
به جمهوری اسلامی حق غنی سازی رو بدن،
۲- غیر قابل تصوره که آمریکا
کنترل تنگه هرمز رو در دست سپاه بگذاره و چندین کشور ثروتمند عربی
رو بگذارن گروگان اینها باشن.
مسئله بزرگ‌تر از جمهوری اسلامی است
مسئله سرنوشت منطقه است.
۳- غیر قابل تصوره آمریکا تحریم‌های اولیه
و ثانویه و….. رو برداره و دارایی‌های
مسدود شده رو بهشون بده!
🔺
اما اگه این حرف‌ها ۱٪ درست باشه :
۴- فاصله میان جنگ ۱۲ روزه
تا جنگ ۴۰ روزه حدود ۲۵۰ روز بود.
ترامپ بعد از جنگ ۱۲ روزه گفت بود :
« جنگ تمام شد، ما پیروز شدیم و تهدید
را خنثی کردیم! »
۵- ۱۶۲ روز دیگه در آمریکا انتخابات میان‌دوره‌ای است.
ولی شاید حتی پیش از ۱۶۲ روز دیگر،
جنگ سومی در راه باشد! و شاید پس از انتخابات.(با فرض اینکه حرفهای صدا و سیما درست باشه!)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=bBEp1xaINpI9JN5GDny1tT1QNTeHhdSd9gcSQX_WqdElGa-PlgEg-xZS_TW4ABojwmUckkU6qFUVSYvrMSdxsDGHMQ8XK97IeIUdEvMAKyYRR9K5X_gYfJ8Nn9_Mh6Q0IUhGMMI_74Ec2F6vuqP3cVtDTHNpI7doNmVcE5IMUYgrgmTX3PHh069d3OPFnLUWpGt5f1jkxzCe7_nlOairCT4tUdDB8byGugrn-jq1nrLl_wueaZYDkLb5jeLmqB3WfJtnUEYXNY5K5M-axXo7Qm6sN8V6-LUs-jP5Qnz9tR8pqzJAt3dzHOAcrRNcyWCnRayBsi5XqI_ispHQ_VKgvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=bBEp1xaINpI9JN5GDny1tT1QNTeHhdSd9gcSQX_WqdElGa-PlgEg-xZS_TW4ABojwmUckkU6qFUVSYvrMSdxsDGHMQ8XK97IeIUdEvMAKyYRR9K5X_gYfJ8Nn9_Mh6Q0IUhGMMI_74Ec2F6vuqP3cVtDTHNpI7doNmVcE5IMUYgrgmTX3PHh069d3OPFnLUWpGt5f1jkxzCe7_nlOairCT4tUdDB8byGugrn-jq1nrLl_wueaZYDkLb5jeLmqB3WfJtnUEYXNY5K5M-axXo7Qm6sN8V6-LUs-jP5Qnz9tR8pqzJAt3dzHOAcrRNcyWCnRayBsi5XqI_ispHQ_VKgvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما:
آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده
‏۱. آمریکا متعهد به عدم تجاوز به ایران شده
‏۲. استمرار کنترل ایران بر تنگه هرمز
‏۳.پذیرش غنی سازی
‏۴.رفع همه تحریم های اولیه
‏۵.رفع همه تحریم های ثانویه
‏۶.خاتمه تمامی قطعنامه های شورای امنیت
‏۷.خاتمه تمامی قطعنامه های شورای حکام
‏۸.پرداخت خسارت به ایران
‏۹.خروج تمام نیروی آمریکایی از منطقه
‏ ۱۰. توقف جنگ در همه جبهه ها از جمله لبنان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8Ez4TtllRFTSbf86TO-Ac_16s1FkjjnBYInjQ9Ru43BucvQBGKF9GTLdYehlrmzCJKkfy8rZUPguSylRLsM5B9D0BeLXBq-tbQzdy59DLYWW55IpkRQLZo3S1eBnn01H0cNyISCPCvtBjQwO7bhbtDZvl81seIz6v99xGBT71EOLcb8jQyfv3fhRx39SaGY24Sg21u3ZLyV-JnpivGXJgmv-sci-mMJe3jQGX2uuDomI6qIKr2_m6ZiPO7rEO_Il8OPDo3wVg3h1woWA7XAp-JjbZQ_kvafih8Ho47UldekAx8kMLcLo3mj0yuTSHyvONA2vsQXWFUPgEaGpZ8KiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏
🚨
🚨
ترامپ :«من اکنون در کاخ سفید هستم؛ جایی که همین لحظات تماس بسیار خوبی با محمد بن سلمان آل سعود، ولیعهد عربستان سعودی؛
محمد بن زاید آل نهیان، رئیس امارات متحده عربی؛
امیر تمیم بن حمد بن خلیفه آل ثانی، امیر قطر؛
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر؛
فیلدمارشال سید عاصم منیر احمد شاه از پاکستان؛
رجب طیب اردوغان، رئیس‌جمهور ترکیه؛ عبدالفتاح السیسی، رئیس‌جمهور مصر؛ ملک عبدالله دوم، پادشاه اردن؛
و همچنین ملک حمد بن عیسی آل خلیفه، پادشاه بحرین داشتیم.
موضوع این گفت‌وگوها جمهوری اسلامی ایران و تمامی مسائل مرتبط با یک “یادداشت تفاهم” در ارتباط با صلح بود.
یک توافق تا حد زیادی مورد مذاکره قرار گرفته و تنها نهایی‌سازی آن میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلفی که نام برده شد باقی مانده است.
به‌طور جداگانه، من همچنین با نخست‌وزیر اسرائیل،بی‌بی نتانیاهو، تماس داشتم که آن هم به همان اندازه بسیار خوب پیش رفت.
در حال حاضر، جنبه‌ها و جزئیات نهایی این توافق در حال بررسی و گفت‌وگو است و به‌زودی اعلام خواهد شد.
علاوه بر بسیاری از بندهای دیگر توافق، تنگه هرمز نیز باز خواهد شد.»</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMDzSNERUsTqrt0TziYL8b2nHS2vWTSt8cVf_aZGOLCvpgF2OhZ7P_dAO-EAZzQNJlWKLB9NdDKRhNK1POVtITvaUoE52bgiL-22rjR8lIUuF5QC_VAcO6m0rwiPY2nH2_8CDTSf74Dr9rqJd5q-H-3aghoBDvaZ9Kd_XsEMW67oC1Cdu9KDp2s1anjVMR5lvu4MnVRns48xMsbq5F37b3L-xNLqdPxMHsZRCjzInmm4DAzPCIs-b7E9LfHgtAGkyUIjCTGSnelipRBZ6H1uSlw2B6Eb1NKrTptG-Z2iADF1xmZ5rRbFSMN7jxE9tMnFjPwkc_wi3_lOOezh-hZSow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=hICfQ-PovEAmEhsTqRINOOOBJiYTgSN7PbUhd4-CJp3y-HiTdSNh6uIcSoL73tvzMEOvnW24T70FNJKb7ILwSzkrQ_G9xyO_6L-6AnH2eOlovk5nbQQcoo1SIv8BKQhvFqPA3HH8pmvW2zkWZ_89so0yLhyXoflacX3lniS_ji3PqZLT3nvXYol62MWg0o102qZJk3Inhi3RDXuIGXAC6Or-W0ovPzF15gfMC9J4ZeIbRrjdTUvp1NbxlH34QriqpfrFLlzLxFzxHuZwDO3C-PxlGx85PnnLGTbCwjUQN-DKz4iemlAnE1TB1F1j5HEEStuO7htcxN-CSAa2V29bjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=hICfQ-PovEAmEhsTqRINOOOBJiYTgSN7PbUhd4-CJp3y-HiTdSNh6uIcSoL73tvzMEOvnW24T70FNJKb7ILwSzkrQ_G9xyO_6L-6AnH2eOlovk5nbQQcoo1SIv8BKQhvFqPA3HH8pmvW2zkWZ_89so0yLhyXoflacX3lniS_ji3PqZLT3nvXYol62MWg0o102qZJk3Inhi3RDXuIGXAC6Or-W0ovPzF15gfMC9J4ZeIbRrjdTUvp1NbxlH34QriqpfrFLlzLxFzxHuZwDO3C-PxlGx85PnnLGTbCwjUQN-DKz4iemlAnE1TB1F1j5HEEStuO7htcxN-CSAa2V29bjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1f4-QdvBVvLeC0gCKdEOC-Uo-tT-TxopJzZVKBx8Kb50uByhEUYEFFvDgdUermsvWCf1im9v1OWBNi53laINIqNzDrqg3FP8pHH-s49HUwGdFtxZyZUg3Ji1DvYGD_ljy64z0e1BuKTV-qWLn5k9bp3d6zs8sIoYzHZ7RqN266ksaswYQpVn_x1TZJyI94PWQcE89TzVB8LChvSJ6e4fgneBjIiyxlNFTfSz-WjqBausEiQqyNZmqP0FVuMsaHJ16AUkIDpTd7B3ps78ysHHKTOpYgCUAqr9D9HdCE65sKmg1RDHKyTsqHlvNd_u8ZKSlBJWEC-WUZxjtR8acofWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال دریای مدیترانه، اروپا، نماد پیشرفت
آرامش، ثروت، هنر و معماری و….. است.
جنوب مدیترانه، نماد فقر و بی‌ثباتی
و جنگ و سیل مهاجرانی که
از این سرزمین‌ها می‌گریزند و …..
مصر، در جنوب مدیترانه، برای ۹۷۰ سال بخشی از جهان یونانی - رومی بود.
لبنان و فلسطین هزار سال، لیبی ۱۲۰۰ سال،
تونس و الجزایر و مراکش حدود ۹۰۰ سال.
تا اینکه اسلام از راه رسید
و تفاوت میان شمال مدیترانه
و جنوب مدیترانه شکل گرفت.
و دو سرنوشت متفاوت، دو چهره متفاوت گرفت.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVdc1fhEbx0oNGUVX1lRxD1ilJhQwyLAEhg8FsPPZjUYP2pCz0LtLCAGydRmUcYCkhHI_k-48UX57jyOWssbTphgfl-V71g7xwWpEeZJmM8M88R6ZmD0KuZtFP9FzgPDEMfgs7TC6nhwp62YzIH79wx3dmtsPm3xmHg7PoAb6GqUpLYYPcf3c94C7rBPp0gcmpKJTOfRjZSPZtmWNCLKm6vPSgWVDQET-OPscoiODSF5ykVEd8H0jD0i15dFJnroeZeh6_Y8CFALtI3aCDUe0JbcCbR1cm0ziGeC_L0Z0i7SRnAQ72OK_FfO_6DVkadPsdEa9AhnBW-hvftcp_ckTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NevxspBvv7lPInUiBGXxshKyc-VToaRxz80wz2Kfwgk-rDEdDyN3klv0Yy5U1pz9ndMfz38nWwRloSdGLQIYvPFdzQAMiVz_9rJ3tN0lbBR1K7epqxGjImcFFIkeUFjPT4mRrVST6UO9MqrBGB4h3LdxfEEslvbJERk7XR9IDHk3D54jD4LsrQhPcFLPFFt7NGQrpd2I57rNNGzLm4OGBxmgbWF5ZMef9J9M9zH86fgQs5yx-xZcRlRJCeXE_33H51DKDHmTUNjX6Um5G-cvDcmA7squXjD1qVWfZuIxEHRXbbuFp4EN_VkJzKwKQLI8NB2rHcUWm1Wejkz0hF2BzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdCG5vJPNagX1aQIMcx_g5r5sE8jMJSjjH9cx9SRB0MX1GSkzL6oFOjpB3xvNbIIlnTdaPerZAJ66vn4GV85E9jDC_pT4Ja5dvaIFr6lTVyUmV2d5_5AAlGImym4xn8S89XOEfghA4UQcHdd4K7s6tl94tP7fpWajoV9DpHP2bgpwVsSHlEWD_S4RgwrxzrkL0I7sdVE1CXWXAAPyoXXFKuO44I6j_pZ0SmK5EO7EbKgzIN0KxG062iW0zA7qVqFCfgsCFH1sgIPPj33MD-9TQTebhALAlDlFydZUBEX5haLwRWa2d27xYhKBUrkVWqpYe_TCT1ISwUr2cR_vWS9uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
نیویورک پست در گزارش اختصاصی خبر داده که طرح ترور ایوانکا ترامپ خنثی شده
.
فردی که برای ترور دختر ترامپ تلاش کرده «محمد
باقر
سعد
داوود
الساعدی ۳۲ ساله و شهروند عراق است که گفته شده توسط سپاه پاسداران آموزش دیده.
انگیزه او انتقام از ترور سلیمانی عنوان شده.
نیویورک پست نوشته که الساعدی از اعضای ارشد گروه شبه‌نظامی کتائب
حزب‌الله
عراق (از گروه‌های نیابتی مورد حمایت جمهوری اسلامی در عراق) است و گفته می‌شود
آموزش‌های نظامی و اطلاعاتی خود را مستقیماً زیر نظر سپاه پاسداران در تهران گذرانده است
. او با قاسم سلیمانی و جانشین وی، اسماعیل قاآنی، ارتباطات نزدیکی داشته است</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYqgUrqyQoHuaQEViZMBMs5_0_tekVJXZmpu-XX9GeVLArP6TP9Gcl81U86ZKSGi71dbiINHk7CvBIzPwqefImPhQnibb3HVjcK3TwLgrW6SOm_3AEy7rFXg6pX0OUM2kP_ePI6kmsC-JxlVA5u5bAmbWG-Xm58W3SMw0Quicgy-Ef0rhaZ7Rmlw7EbF8IukcEAjZ7kaEjcuytq4gaWZBE8VItLoMf0AvTjamgxSr-ZMdNtnMVlOBJchDIE6fOYjfK_z5YScdK4wRNYlbyGtvxwO0ElXz7NgR62vPQXL81e7gJFzDG09aAwbKvdtOfxMvR85DVlT3m9tn5cs4ICyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0aqKQqPsSF7VsMyT-OqgoHfBbv3XO8M19JJRvwaHt_ytOQt6MIWldvaQXbbxsbeTiJDs-TyEGnka3x55OzJMKlyHo0wi4u146b2rq-ucih__kX1PqIlNhWvsRdEg_FVsKmYc3gB2-MgZr08VD49H0oOSKfRYsnbt0F8PWn1VR8z7WnTeXPEcOdZhO4-9vpQbNm7zyI_WCdgRC8DEw5E15SV8aWGP_ecrGPaFmrZ_bomXt4IA9axyed3VQppk48_PpKWAleMdpN6rHTvxV23U1v8wJtOppuWJo-P9dERx1LL49D7rMVJIoyXRsQKUttPLgFXxTuTRPCtYhBnqXhrVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">مصاحبه اختصاصی با قرقاش: ایران در موقعیت ضعیفی است، دور دوم جنگ فاجعه‌بار خواهد بود
🔸
انور قرقاش، مشاور رئیس امارات متحده عربی در امور خارجی، می‌گوید دور دیگر درگیری میان ایران، آمریکا و اسرائیل «فاجعه‌بار» خواهد بود.
🔸
آقای قرقاش که در نشست امنیتی گلوبسک در پراگ حضور دارد، در گفتگویی اختصاصی با گلناز اسفندیاری از رادیو فردا، گفت که کشورش از یک راه‌حل سیاسی حمایت می‌کند، اما در صورت بروز یک دور دیگر از درگیری‌ها از خود دفاع خواهد کرد. او همچنین گفت جنگ کنونی نفوذ آمریکا در خلیج فارس را پررنگ‌تر خواهد کرد.
🔸
رادیو فردا
: آیا امارات از مذاکرات با ایران برای پایان دادن به جنگ حمایت می‌کند یا ترجیح می‌دهد آمریکا و اسرائیل فشار نظامی بیشتری بر ایران وارد کنند و همان‌طور که برخی می‌گویند «کار را تمام کنند»؟
🔸
انور قرقاش
: نه، ما به‌وضوح تلاش زیادی کردیم تا از وقوع جنگ جلوگیری کنیم، زیرا روابط ما با ایران در حدود ۴۰ سال گذشته همواره رابطه‌ای پیچیده بوده است. ما همسایه هستیم؛ تجارت، سرمایه‌گذاری و پیوندهای زیادی با یکدیگر داریم. موضع ما این است که حل این مسئله باید از طریق سیاسی باشد.
راه‌حل‌های نظامی، همان‌طور که امروز دیده‌ایم، پیچیدگی‌های بسیاری به همراه دارند. ما همچنان از یک راه‌حل سیاسی حمایت می‌کنیم، اما این نباید بهانه‌ای برای درگیری‌های آینده باشد. مسئله تنگه هرمز روابط را پیچیده‌تر می‌کند، به‌ویژه در مورد دسترسی آزاد برای تجارت و انرژی جهانی.
🔸
رادیو فردا
: پس در واقع، همه‌چیز به جزئیات بستگی دارد.
🔸
انور قرقاش
: بله، جزئیات بسیار مهم هستند، اما ما همچنان نمی‌خواهیم شاهد تشدید نظامی باشیم، چراکه می‌دانیم تشدید درگیری‌ها در منطقه همیشه به بن‌بست منجر می‌شود و آن بن‌بست مشکلات بیشتری ایجاد می‌کند. همچنین باید در نظر داشته باشیم که منطقه نیازمند ترمیم فراوان است. به‌طور مشخص، امارات هدف ۳۳۰۰ موشک قرار گرفته است.
🔸
رادیو فردا
: که حتی بیشتر از حملات ایران به اسرائیل بود.
🔸
انور قرقاش
: بله بیشتر از اسرائیل و ما همچنان در حال پیدا کردن پهپادهای زیادی هستیم، بنابراین شمار نهایی از ۳۰۰۰ فراتر خواهد رفت. کار زیادی برای ترمیم روابط باقی مانده و پل‌هایی که سوزانده شده‌اند باید دوباره بازسازی شوند.
🔸
کامل این گفت‌وگو را در وب‌سایت
رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifyvR8If5H0C4XsCx5ChSjRq-iJWEdjgBD_XCGsiONWTDou7Bq_1t9Yr1pitRk618OOfLBS36Pxgo5A8ocZANr71Eb2zWpi6XvaKpWMFnV5XWAB0F4uY-NUbVFhuAXkrVmN-bZXMYqjbF7GOiWw9pYUmGiGA4qYCTmsRSgj-DbzTWybCo8Gt0r15GEu8TTuLPadcKv5j6p68JtdaMZQNXxd3p33uEJwn2b4WlywXBYizZdQjxwa7yrAk0h2-3pWAtF4gHGqPx4pDiWvDoBiqJ1DqwQ19n02iveHOCsE1NGM45yB0uLEFDOgXc9UwjEvCN0YBe2lMn7F4oraf2ZkG5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f64UuTI-5ICfrlHqvd13tjXCOWUXxcD20pLzfjTwn-SJzRmmUHn6pgILIf-bUC3TaGEjNN4L9RBNYDdlQDyxTxQm4u-nFnZpprFGEmZtaW8tbznko_4QR6O6Lf8K00t8hH_Fk8CbhK13UlXQrm8IQtLGSa66pCEuz-EDX0VN-FN7xx6uWlTH0k2dHJ5dXmciBOwswzw8iBWTxpZi0PjNc3Aivy6qxNYPU9ap-VXRI51DQIfB3fgJlPU8TzjHGjYK6iWfb-1Qo0QOivk0v4AvafMUP1cNb23Y2tcrLXXXYeBApwM2rlalL6YYRGipnZ7NtqXblS9ZkFzEVYs9F0i9XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXpSnNAZmDancdnD2c5j9yE0yPZ92HqTr0Zpqr935EKfbZpnUEghpPZHcQqCefYGrml8HWDHxCKoFwRDHO-wn6NDiSdDNs_9xq3X_9MgPRVJTp3jzKR2NE58osoUJscTkflggSOmOPGUxl-lb8hUOmf5kpaql6144_HOwpD4LVQoO6FptO_zIdmv_4kUut_-DaIXAW8-IPxLiapOo_cuFCaxd7BHhFg13c2Ubhm0wquINJEWW9v4ZsUv9YrwtdLMdFmRfg2A9zj5Ccf8bIGWCDTo0mQJ_P4S3n07-NEM6n9uW6RviH7ffS5F7vGYhgqW_kGzC8oqAsZkEDcJg5WupA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdc5mNUAzYTUmztzg75hDBbXaaF4dJplF5YNlfARoUMDUW-U03SfN-jAOkiqTaMlwew7ipr8CPhNG2kPyyaquGAaTaUEfqz6Lpul1rcI4E56hx8f6pmwwWCpVr_T4efZoIjDnKl8oFxgYR7uD8ZtSHOHQ_3FHgIhSxrsKpLiyoERtGJ1nig7kf2Ob7jSkRcsfcF7PQaTfZlIkAWJ6oE0Bv2r3q8x6dCJLGnwF_GCXxcEhF-hUuHfT6woeKV4mOPEWJIFeRTJ6TMwGJS6WDl-GoHS3hqwNyvTenddkK6ss5riTOnRXTexOY1jwWyg2QFkVch0upragOVjXS6Hx847Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipOuw12dqgf3eGv8S6YpFjpst1ByBTVGuKGOvxdeG_kgS8pdQpMWYnNpuUkJILliKiQIfl_Q-OTOPrWceT7sJKvFmGheQBKIJfHyAucOzETr22aOgJXaqeBBT1Eb_x-WikN5q-OjEEL8JPFiZ2HMX7ocKzaapdDRiKqojGVWtzhzE-R59hThkSCsVG9g2qHq5n3Xeu4hFK9Idr3U-JOGML7eeW5rGVsWziI62FWd2clRUnKjGbKyns4JfIgnQsxQgYfpup6pQQFHhBn1Z3CquyiQu_pO7Xdf7W20AyUhQua7E-zHcUJ0IZZgUcjFEgDv_2IP4KcJxYc6DfQ3k754fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=IQv1A_79eT0aSUKHkvlZt-qHutWj1KhZ7rp2QUBKFJtPSM8AmMcmh8b189NBctGwY5cj-eIBTtp9xnskGfSC6lawTQitIroyd_QssfgMWarb0-Ezil3q27GVsg-2nQuFR086Gd7vI5KswQ1xLC2H18RapVuu-iNdT0oBI3Rj7rZOlHHO2wdO5YV4zitb6EPWwKvbJ-7enTvm9BUpXxGncCMmyp3eR2_0wl52Sccg5OYdDWoKW7qx5Rv97AivdKeAKPb91Oodp5nghfLNyV2KdnTeN8G36YVlAHdbxyMXnlMD1syrUFv7SLnDPe6ArYfNm8m3GbIKmztrbkfPgdJM2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=IQv1A_79eT0aSUKHkvlZt-qHutWj1KhZ7rp2QUBKFJtPSM8AmMcmh8b189NBctGwY5cj-eIBTtp9xnskGfSC6lawTQitIroyd_QssfgMWarb0-Ezil3q27GVsg-2nQuFR086Gd7vI5KswQ1xLC2H18RapVuu-iNdT0oBI3Rj7rZOlHHO2wdO5YV4zitb6EPWwKvbJ-7enTvm9BUpXxGncCMmyp3eR2_0wl52Sccg5OYdDWoKW7qx5Rv97AivdKeAKPb91Oodp5nghfLNyV2KdnTeN8G36YVlAHdbxyMXnlMD1syrUFv7SLnDPe6ArYfNm8m3GbIKmztrbkfPgdJM2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=m04awUxieL2PagMFj6cXvgGGMiI8FwhNz8oRxIjV2N4Tw0avxf8KoWlUJpWIzkwn8LYjil4VraTbOUK5Rz5pxlJVtqX2DrHmFuPKIsF33OTXbMVfea_Fvfza6Isldf77308z7zAuOBWeSHcTi5SoE44dzPQ8qM9RGwVHyzch_Z5x7GAXYupBg2fcz5SL5oM1ULIpXqAmppqEQsmOanbQgXxL0PkFxzCahDKVft04IxscbDHMCUSrkK9B5VSYlUs_JlWx6kn8FbGxFKHBa2mO29ACOza0vqhOjBI1S333XIaA7uQM4PkGUyov8KILLvk2ukCO4uaqLCP7RcHgxodTpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=m04awUxieL2PagMFj6cXvgGGMiI8FwhNz8oRxIjV2N4Tw0avxf8KoWlUJpWIzkwn8LYjil4VraTbOUK5Rz5pxlJVtqX2DrHmFuPKIsF33OTXbMVfea_Fvfza6Isldf77308z7zAuOBWeSHcTi5SoE44dzPQ8qM9RGwVHyzch_Z5x7GAXYupBg2fcz5SL5oM1ULIpXqAmppqEQsmOanbQgXxL0PkFxzCahDKVft04IxscbDHMCUSrkK9B5VSYlUs_JlWx6kn8FbGxFKHBa2mO29ACOza0vqhOjBI1S333XIaA7uQM4PkGUyov8KILLvk2ukCO4uaqLCP7RcHgxodTpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEIoS3uuvts8xvynUFlPZ6AKGcyTPOhEmMYSPsKAFi20h4c2jF95GDJ6Ptb60IyVfL8DyHIa-2uu_Ulg4PA5jiC9CdI8HyQOng00CXzcwOrtTSB1IFcrxdTfgw8K3GUYJXOkpaqIvH6sy_wFu8Bt73Xek0ITvgBDI-4U7zcVqsUOe1ZUw0lAsmpZkMbwgx-c8guF5rJiu7RYkV6FbxgZzVVuQWSQB7IQLnXARCK4Fh4T8XTJu6GgDLBjT_az-tMgK1Xb4zlAPJEqIbtSsLJ51ptvW8EWZw6u5Bp7N73mnscLLjeAV0OFcrzFcMaIFB7CaKykOKrpTm0NCJf2bSbAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Goi5KL36Bi_uH32Q0jAkwrukYSEL-Apqy9MEbe3DF0blWGzpWocpQM2s7y9h2hYDeH9Gv5bACqG2CT0vW4pTrMVPUpQe_gICICk1ik7pDMDiqhRfNxqQswou-xyv07z5kiX27QAEaZAh4M87bvtrJYiX0Lvrd6Oih3Ew4rtbXMxEQPzVRIdwaFa_kAI9H7rXmqFToH45Y1Yjc3WEHmS2niqQICAQGn0vNi6Zg3--ngLCNa2-RwU9bc8kcqhfwJo0leV1_DsZQnFRJRrCM4N5jhRrPSbCJvgCGoKfMc3kMiXGWkEbZWTAyMDI9r7FCTv30wgOv-vRyt1CE8Tlw1G09w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPMbjUGpo7KhNDYUgGWy3i9QLKo7ZDhmDBFUU2bUJMiqUi6nBb5_wW_PZXW1C5uK8vXw2Q51HFRIfvNVBMjj-xjqfhtNVg5IoIx1W3mh_BWeG5QFA0Q6rAjsrPv3hMYBtDfYN2Dz36RpfGeZ_BXx3JP9-lqTV9UDvX2P-iKKkdrF95z7o0IL7aAU5ITplDB-8CVGC6Z2ykK-rQGgykqQPaK_AYjBBWmoL3DblAI7llPhUXHUN2Vc7I14B-H7er5oUUP17FxWSA7xoCMlYoIsfHHN3baRA4NGVFUKomzC20sDpo6JioHjfDpqmVHT9jFowZpDvlDS4hqKJW1lmohA7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=NfoWM3EbQjKBYGx2GcnYDTX6mPHrvGPb75vtzkW6HIuyMN0x3EYfg7ppjpIy4x6rPjUWKrOoFXjdMAI4UJtY53dNj_r02_ldDpMos49282pj1O_9kfnJQ9uie8cuULzfNy4gPWHuu5WvlAjjdH6qW_YxiH_KogFsD_gcFRisTlxFuMQT0c8f2VXpshuv0w0s-5bw9erMOLNZcLIxN_JehYua7odNrcflFTmS4Ljcdu7n_-v7StBJMo-QpC0EsI_8frGu7bx8zL90Ai8xzLcrzmPiVFHCqGCEEAeaXEzR4poEcmuklAgbdJ9vzLBC50KK7uryNSOpTykvvQU8Ol-w2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=NfoWM3EbQjKBYGx2GcnYDTX6mPHrvGPb75vtzkW6HIuyMN0x3EYfg7ppjpIy4x6rPjUWKrOoFXjdMAI4UJtY53dNj_r02_ldDpMos49282pj1O_9kfnJQ9uie8cuULzfNy4gPWHuu5WvlAjjdH6qW_YxiH_KogFsD_gcFRisTlxFuMQT0c8f2VXpshuv0w0s-5bw9erMOLNZcLIxN_JehYua7odNrcflFTmS4Ljcdu7n_-v7StBJMo-QpC0EsI_8frGu7bx8zL90Ai8xzLcrzmPiVFHCqGCEEAeaXEzR4poEcmuklAgbdJ9vzLBC50KK7uryNSOpTykvvQU8Ol-w2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انترهای جمهوری اسلامی
یادتونه برای حمله گروه تروریستی حماس،
شیرینی میدادن؟ یک‌ شب شیرینی دادن و ۲ سال
به سازمان ملل و به دنیا فحش میدادن که چرا مداخله نمی‌کنید و متوقف نمیکنید؟
(شما چرا نرفتید متوقف کنید؟ و البته میگن
پیروز شدن و نمیگن اگه پیروز شدن
چرا خواستار توقف مسیر پیروزی‌ها بودن)
حالا هر شب میگن «بزن و ‌دوباره بزن»!
فردا که «زدن‌ها» شروع شد، بخش «خوردن» که رسید، مقصر میشه دنیا و این «لاشخورها» میشن «کبوتران صلح»</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfmWQRLQEd7_kJFONur0PqBrRMS6HFTU2ssG7mYpEKlEm0Rgne6UzVyTzVtuMvksRo4pMG4zTM0lzq74bkfekQERLBw7oKZVgBzJDFzmFcPyKSuIOOgwoCTp_zywGMD2uTg3cPRBY964wvMmEnZo0vP6i8WWgXDQK1uy2mL29z6WOXJBhZZ3xz32d_DouzdUe5CluXaHA8NLLonGFrBGmzfOzOCS5W6eIF45E7UMZj0_4AZN3JfiszRscg0fYJswaBc-Dt-yJaLkLz7qjkOqLT8nT1QPotJ9oSJqsVy40YKSgLEmvPFxE3EMa3_LK1FgyOrvNjTzu87DXdtZtWW6rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xq2ez6D2x2hYl1urzOwBMTNMlqr_BbMhZJ61JKEQWaQnnm4btn7zSVYV_4d_cuqkrQTDRWW0K-fOKYjLfFC_9zKp8oz_1a46MmMsH8fil-h7Pl35-uKr6X5R8WCulBcY7dPxNtSX2bMVekbMe5u3-xD2n_Xdm4fmlM7vSCmqwl23HJiSFa6766U7ofGX2v6uH4tSnQTm7uRzRmTrVOEC2LDkI-J65hY-g2nELxoV1nXLhFgzs_4RZg8N6_W2PeT7MMrZQ4n14yFHYupikspdNRODd1cvc84NhNd4WWNVj-MIIybGbLWnLmPu6SM9SGDecl0983rz3iGSIB91rGxD-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjZIpl2GGRIoRSCWqu78OcF9IZYLTKPtPmAGwxCXdGFjx9W4jKNwG34pn0kN0Ix01c8kPPjCScmKZSSPlCqTvNXwG47VenwSYeykYsVXeVQDX338LRKWS6YzB1FbCM29u361vBfuJxuuBFM3YGgXrB2nZkVWa_d5MscghB7QPQgVsn4YND6doEVB9Pbqpb9syHlVt15R2mA0pLLEo6HCcNGPd96E0b-73OluNi-2c85lccrl3DgfBbsdynGqBoXFW4ijtPss1YSdmiI-zJrY5w6tIL-adYMbJdV-fKC2tsucyoOhYmqu5nsjL72GGb2uIi0J9ifNSimjxY2vvgIEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gew6weC-KgrDohw9bMqWqLi08RPA7wTFm7yVyIFyd9vBZ7M39UAeYQoTXYwOlshPYUCCM5DivwMnU4v6dJtCro60RRfWJe95Uu2kcRla885Cm7FGzK12srsRM5TQB_gHEO6W8jle2qSKuwqfBvvC_PYz4Vvb88o0c3X70pvDStRcIzXLJusbbSeFpCzTL9LMvRHS4rtiW3s1DCBKZZvkJ6aKkbRJY5zvSolOoLCiVFNEVOXlW0MZAeS8XxACOCBZlbZ2nlsRdPA7FUoLiYNm0-I1CwArdILwBgwdWfDzOOMw2hbRoS02STXPyBKPZ-aY7Yxni4BCtVaMDk3SofVwXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtWruQZtkYfH6V8AH_58_u5R-TxF2kmSi_d5dk1c0cv-bv9vITd-_pXCN5qoWwInx7MyAin1aShzOTscooaoiI1zjRn1JDKZXR_TlDhbe9kxtkeYurCujj8IJEI-6RRdOACO9d0ZnyfD3hoQ3UkeGItmh5WCPgItzMVi3JYKOp_DhbKpB6SVFyMbQZ0yB4bk_fKBnVnL-issV-48OZ-wN88FWNIaOaPK-Qe4HpCWPK73TUQ1puVWAisFihJGfFe5TVSPO1iaXRL0XMLmDjy6xkywDUjudeZjGLhnT3ZqKB78RKmyp37_9HVCJfqQN7DxWXs7BYZfxwX30HFj6NJYIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lz4uPlPXFkEPn_Yu-_cmr3FGgeNRGigaOGDSpKRmxLTgkNGYxp-dt0ow2sKia9kpNdYNYsql99ioRa5rAfrMUot68h9iwaKX_OAk3QCu2Ns9a0fyx6zvpsq5AwCka2H2WI-tO5rrfL0ajwoCTtvmiYZ5hhKX4nbImZZ2Mb8yXjZFL90dOGjjvoi_9xG7cvq4MoF9C1GksOZx9uYQR_YyPdetdPVSWO1Xd8RYBjMjjzCTfMTVSXe61sWrV_s57dvTL638uliAkb--3xTq6X9AaA0EoFBX0NLMTxUnHB1048olt26mtkx0f4loL6IEwulCo7n9UI7Kc3UX5nM1YRbKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i67YaLLhFs5yuruRZBcMEG9nBvNd_HYmLYvnT8BArMhcsaoWV3NdnJKZTswZILjv0mzw2BmkUeh8umMCI1IQ3q1EQKoaggb417mSYf3oxyuCXYa65I4kiNWLhPOg90JiiCpK-GKRNq3XO9k63pNmno7LP5kuTWWZxu5nR4T3kTnbCVHpw-Wztu_n6UGh7BOFdOxEuYPgEsSdjx69rwx7FKcWQlmBk2EIiCJ4EXzvIcIKruZCw8eIf8ORceYW5a_lXz4Ira4CuDfvHTPVeWDHCjxcCGDrwea2u729NhiPzCxo3da-GoIVcJaXAJkZ7CEhmexqKZ5wYcBlYcaFfbiGzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OZZYKWN0DJ6TmmXt9H77y6YkaSaDdO_QZYcSJxyGGpVXQOnViMrzdoQdO_Wenfv9oEahaKtAcBFvZ2qtWqOJXs9aSYrHd3Z_zWfE2NZB70tl4CRA8bSZjeTP2lY4xiYS88bMgzeFNPwl8JEf__Q4qbh_0xJjSzgmucUyL78Ke7hMv0S5Mrx6BiIDuuRqvcNNA685mZ6Fuljl4FzdHuLBTrpH3gIV87msWeBfOHo6kPKJAIScm0a4Se_JWsFFiFrIS_SUBYyVEb334FEQK7WXIaZyvr8OuEKV5KQ3kUm1BR-CtOUk6QYg9GXbc5avDKJxPIPaR4WjJaF6IyL3yIhpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqJnPPBFt7j2mCo61GCDG1rIOE-E8lvzrC1BL-benQvzKffwNumiLtpzD6KGJHnEhx1mD7WB683vr1PFx-uZhcy5T828XQgml5a_MDRrV_9ukLqa4rolGfdgsrdzJO1Zdyv3aNCSmQFAT4-32a-gt_idCpOOn_59OvDyUFECbnHej_Q2er0u-5fLcRwgPHPykVlRvzH0VRkjaG6o5nKM8vWyD4vZZu5xKGK20h71PsFkHg2xoT10NuK8P8DNCNfJgw97kkkn5Onv83ueVdlNFwdlyYI46GFW6NmI9KzAcy9ARpgzi3AT_T54BWosQgpr2YVOG4Thx_3_4xbaUzM-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ToQ7hNkYgpgW8RFNeAfwb4gRgkzkabZBxMzUYPXsO4WSYPcaf92Rp12z5IGHgi2X68sGWSjwvzZxfBGqC2WS8XYlRxPkFpHZ7ZBk9qTOJLwm8UoUVD-EP3-qaoHyWz6Xje1PNEOI0-QIMm_OgLaTayp47HlC_ZUUdKc0b0GFpMPz-I-fncZmEzWBWcGzvv9PqbVJIJypnz34k45-BdceWkbNoW-af-pa1teRVBvbkBu6IAu-AL7ArSNFGt3Ll6l1SNAOVWTxI3-DqBg6jKl3DGtDHY2vIO1dp1CRE748V-Ukrjr-Dwdp0zJuaGC0s4Sq2jrK7Ik0EGCC68ZqeM2WHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ps0Jhb53MJEHjU4LQh_l-_YoCAtd-aJqBWLavVJ4D_zDWGxHK0E9DqnHdmpNykMk9Ld943Jf6FSxgpepHc0h8-Nv8y7rPu8MHRT-EuKvErC-_l1hnNLHorFiYqeAsyl5CCtm3AT3qDvQXs7kCAYcT13PhL6p05BntWzQEFhKV1lmWhaRRxeOPBoBhZedyjopl7dUC5alQuIgUd3if4eMSMtrmNJDmunx-Q53eBfw9jMeYzrEc0-to7vkOyPMmy7E-39HmE2wx4z9FcWYNY_kR6rsWteKmlS78tg0-R2isZEnlrYYLR6r2GDQ4lan9gnGGU13t3lpYOQVeAq7kT12Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=enlZJ1MgGdIPWcsAZ_uPARZ5Ws6YYNxMgwUScGUnS4-r7r125eeTcky-hiTAQvetBmmo6FeiEj5moFstrKpVHbVws3jLYIStubIahzr37WhdXeyGI7ipkO8tZSwvI7_WnnOUM7iZ1SqZn0LV6HrTaWVURPan6YvnjTrm_e9JSPpKq9nnISPMcZatTL5lI3GNdzJiyYq4O2AyCCWtBn47z7LBTHN5fZLZhpyUvEU0REw8SQKK-ezk33s8DWqLqdLwhZJ-Hs18IU43nTB2DhsgulHuPoApQgLWoS3TD19uDpWhxD03qqVa7FtxYRelwg1saHku3vKHdZ3TgfVwiFViig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=enlZJ1MgGdIPWcsAZ_uPARZ5Ws6YYNxMgwUScGUnS4-r7r125eeTcky-hiTAQvetBmmo6FeiEj5moFstrKpVHbVws3jLYIStubIahzr37WhdXeyGI7ipkO8tZSwvI7_WnnOUM7iZ1SqZn0LV6HrTaWVURPan6YvnjTrm_e9JSPpKq9nnISPMcZatTL5lI3GNdzJiyYq4O2AyCCWtBn47z7LBTHN5fZLZhpyUvEU0REw8SQKK-ezk33s8DWqLqdLwhZJ-Hs18IU43nTB2DhsgulHuPoApQgLWoS3TD19uDpWhxD03qqVa7FtxYRelwg1saHku3vKHdZ3TgfVwiFViig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاصل ۱۴۰۰ سال علوم اسلامی!
علی خامنه‌ای هم به صراحت در یک سخنرانی «اجنه» را متهم کرد که با سرویس‌های اطلاعاتی غربی علیه جمهوری اسلامی همکاری می‌کنند.
در زمان محاصره اصفهان
توسط ارتش محمود افغان،
روحانیون بلند پایه شیعه، به شاه صفوی وعده دادند که به زودی ارتشی از اجنه
به یاری ارتش امام زمان (ارتش صفویه)
خواهد آمد و شورش افغان‌ها را دفع خواهند کرد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=qxqCEsYGk7RIXjXQS5j9Fko6xsW9FxHUn1E4dQC4WYSO2bVNffMrt0CyD4v9gkyD7yXAI1wnr-aJ220xLJ4zt0GajkIii2AUkEyz7A3AauGnIDVedx8uPd4nCQFgtfe904zWB-5u3uqkMO64mf7oLDYKJkaE1d-oR3xL393NmP3EQrnAfEFjTu0oJYina860kRAKbJpgJIHLYcXQNX9tiq6IvALxNK1hbqABp0MYbtCZAkZU0v2Vqv2l0jFVVLxXesqhYPEyj3G1fhK1oKHOfRA6T2Nwrh6OgyAgIkWRMx_zPklAlhX37fS4G9V2eKjOK_ZhuTauAoFXYkDgm_8oWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=qxqCEsYGk7RIXjXQS5j9Fko6xsW9FxHUn1E4dQC4WYSO2bVNffMrt0CyD4v9gkyD7yXAI1wnr-aJ220xLJ4zt0GajkIii2AUkEyz7A3AauGnIDVedx8uPd4nCQFgtfe904zWB-5u3uqkMO64mf7oLDYKJkaE1d-oR3xL393NmP3EQrnAfEFjTu0oJYina860kRAKbJpgJIHLYcXQNX9tiq6IvALxNK1hbqABp0MYbtCZAkZU0v2Vqv2l0jFVVLxXesqhYPEyj3G1fhK1oKHOfRA6T2Nwrh6OgyAgIkWRMx_zPklAlhX37fS4G9V2eKjOK_ZhuTauAoFXYkDgm_8oWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادآوری :
در پی انتشار رسمی خبر کشته شدن خامنه‌ای، در شهرهای ایران جشن گرفته شد
و ویدئوهای بسیار زیادی از این جشن
و تجمع‌ها منتشر شد.
و به قول این مداح
«صداش عالم رو پر کرد»!
حکومت از همون موقع اینترنت رو بست.
تا الان جمهوری اسلامی بیش از ۴ میلیارد دلار به خاطر قطع اینترنت زیان کرده!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=mcdkV6ybqKwJpU1PRvSuXyP6le9fpHyliAwPwT6rlT9hE8MD9RuzBi8n0HnimxiWDexKq-05ZFH2lMvENAJ2DfVXP9jZHxCAlU9t8MHhzhTXMjQnU4WYf-VFL2ezMHLaSyEqW30-z-14n1J6vFgPNVE_AUJs2WKA1jeytmVGJRXXIcANLjJrPqw5wCGIXFgUg-Rg9VGRVseZGSjjjxwhPVY_lHuSrCkrmBFfP4N0RoHFOGoP_wxgkYcX0kmUr4SYnSK5y5BNoGsSwcPEEA1aPIAgxOqn1DfAU8pS0iELnGFOcoMvYM14fKWkHb8M08mSmSYux1b662SV5zhcNavUpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=mcdkV6ybqKwJpU1PRvSuXyP6le9fpHyliAwPwT6rlT9hE8MD9RuzBi8n0HnimxiWDexKq-05ZFH2lMvENAJ2DfVXP9jZHxCAlU9t8MHhzhTXMjQnU4WYf-VFL2ezMHLaSyEqW30-z-14n1J6vFgPNVE_AUJs2WKA1jeytmVGJRXXIcANLjJrPqw5wCGIXFgUg-Rg9VGRVseZGSjjjxwhPVY_lHuSrCkrmBFfP4N0RoHFOGoP_wxgkYcX0kmUr4SYnSK5y5BNoGsSwcPEEA1aPIAgxOqn1DfAU8pS0iELnGFOcoMvYM14fKWkHb8M08mSmSYux1b662SV5zhcNavUpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_NxeHBZIdHCKvMJJhHwM8rmdsySTR8HlzG6dWaDXfEnfHJHID1IP_fVn0Cl-jTT4mw_rq01Op3Qw7fauSE6GhajW3A0K04CSu6RT8N-CrXdlQnB5uGv0mXSztHlKjzmECm9ijelGutsGxzywAku_R4nmR2pLJmuYWordaOEVlQzgqXAnyQsC0lZr95KFiYjM-Cvh55x2Pa1F8GBfHxKXJVMdUu7slN_h19aWE-0wKsDu54cutIKr-pi8YJfc3__M69P6CPGGwU1bfs7DFg3gcH63EckZe962R110l4iwRHDZaaH78Gkey6NQS2PKfjYdslRC6YoxemT8AGsDQdTJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=e-Pt82yPvK3wP-qVuQ4lAKDbOvM38xiT3pq6gDE2FSzzS3hsOzLSNyJbQwiO4xBTI8mzZfTYdA15qeRqsiVh4NpLjwkMkDfVTNVjrSnYlDggUZxcs09Hn6fl0KyMZO94UY9JY4RXCOqSgqVls6Cr_HMTs8RLJY8-e2Y0p1vmYHWnYIKYYcNIO0MxRlLACtTyPIitpHM7Utz2zMJwyh7I4_HtdiPiI_c7HHe4to5gUM1ZgSnZEJ6QHZj2JG7zx679APxH393FMyMi6ULSrhMcdPOON8PFU3bgizwpZKPtORQugOvxfBeoocNilhQm5mt4JkJ9RIAY2wKB7lTpjC5u3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=e-Pt82yPvK3wP-qVuQ4lAKDbOvM38xiT3pq6gDE2FSzzS3hsOzLSNyJbQwiO4xBTI8mzZfTYdA15qeRqsiVh4NpLjwkMkDfVTNVjrSnYlDggUZxcs09Hn6fl0KyMZO94UY9JY4RXCOqSgqVls6Cr_HMTs8RLJY8-e2Y0p1vmYHWnYIKYYcNIO0MxRlLACtTyPIitpHM7Utz2zMJwyh7I4_HtdiPiI_c7HHe4to5gUM1ZgSnZEJ6QHZj2JG7zx679APxH393FMyMi6ULSrhMcdPOON8PFU3bgizwpZKPtORQugOvxfBeoocNilhQm5mt4JkJ9RIAY2wKB7lTpjC5u3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=TMMM7pHtDUsJ7OFUu-LOvq2QLqcTq0AwLDQ92ijsTrHhPYprCmfjg6qjZOuVfTYPdoIyMKDT-y_Ao9yTkDjlxhAHjyDaSY5ncm3C07ZieCMpBCMXcaKTAaGjy6QItheDejBNsQg0c634i30yiqcT2eo1vjxBGdXwbVd1AurPe-BBoV0XyHTXmaqYugFF3A1rXbb6QmXgppKtam5FijTvg54mHw7SlgWTrJE3okqEaD4fI-Ssxzv5r2ur-mQmLjaVzo-bozw5mfPeNvFHCFKNV0DLmRBanscu8hSrOshJJKeFV4rTow9CfiAi6JhZY43vFOYS8x2gd9c9WQmqF1HBdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=TMMM7pHtDUsJ7OFUu-LOvq2QLqcTq0AwLDQ92ijsTrHhPYprCmfjg6qjZOuVfTYPdoIyMKDT-y_Ao9yTkDjlxhAHjyDaSY5ncm3C07ZieCMpBCMXcaKTAaGjy6QItheDejBNsQg0c634i30yiqcT2eo1vjxBGdXwbVd1AurPe-BBoV0XyHTXmaqYugFF3A1rXbb6QmXgppKtam5FijTvg54mHw7SlgWTrJE3okqEaD4fI-Ssxzv5r2ur-mQmLjaVzo-bozw5mfPeNvFHCFKNV0DLmRBanscu8hSrOshJJKeFV4rTow9CfiAi6JhZY43vFOYS8x2gd9c9WQmqF1HBdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tw8F7ZFGT9k2fPGqi_ixPeBeNdm9HMUYyyDT4ncCISiNtJBhY-OGpqARwn7D6zbd1JYB-M8fy8GYJY9ivC0LrEbgp_P1jogruMbz9eUX9edGKoVcQmZ7DVog-mfRYVzgrzkvTvCO99lIbepepbnyNvRptx00cMcTKFs33NO7TG3YRdrONf6jF7lddOe-li3kjzQRler_hSpcCQRVFDc7dxXJng30wWPmv9_KxpAPzvdgWfRE-EFaiXxFYYjLmv2Ou_ouxO4-lx7A4_LSrEvF34Qg6M4XTu4DtJgmMosAuwtATky3YVBiyt7kGRlnocHy1g4QeNyGKJivUdYsGR22JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قراره جنگ بشه و هزینه‌اش رو هم ملت مستضعف و فقرای آمریکا پرداخت کنن!
قالیباف توی پیام‌‌هاش همش به فکر
یا مردم مظلوم غزه است! یا مردم مظلوم آمریکا!
مردم ایران هم که مشخصه
تنها نیازشون توسعه موشکی است
و تداوم غنی‌سازی!
الیاس هم توی استرالیا توی کار ملک و املاکه
زنش در شمال تهران
خانواده اش در طرقبه!
گاهی هم به دنبال سیسمونی و خرید و فروش آپارتمان در استانبول!
زندگی زیباست!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soafuhPyOTBH4WYwiFNuASKX6L4CBX1D_8QuCfN5FWuOPSHOChRhlyRRsQF_1tFUiAVzSlOAXrT-M2d5duMiO-YCwivLz-CL0iy3UH1B7XGAz-hGaoSLj3U5dWOZ8tPI_dF_sHeOs_wMRqQQ6rQt3sFK18zqJmOm7UeoM2n3b4VR9dTZiJMhY1ZxMExthHTxBrF7suQSOEhEOAZbundtwSnLmIR9oIEENAL9ulJl1mS_GwAAoQ4AYWvyyDGp1_KtFNqHeTkXt2Ge7UkOnusb5PctVrVaSQ0DHTJKQhtiT_kae3yweIFE0Y0c1-dWuWRiqG1dHqUco84mG4HZ5UhVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRM-ZL6bWKz7UYYXqscSm9B-VOdFIUJ3wboS3JKjA6HkBjXfeqxh3nNL13SuaM--kckSnKgYMwsprrBNrVlIswdLPV8Hxco8Wg8O-g26MVOG5ctcAK3_zfXlf6A7EsGXSEkOQL5Av6wOuhS9w-EhFULP7yhC5chzuWboJrdP7aIxhBO2EPe8bKHuEpZCzXQKQliHZpB96kFplAX2B_6e-t8rYeDJOPChatUVViSKmimPXmcr39QaNkvhPcfnL6rYAljjZgRKx7gKO2RV3LuGPZvbUN5o-7MBecvS4D-zFhVtDvdHlln_j-1s6dFjpuPZ0QCInJ1HclYGHFc5gSFyDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAWZEgvXxFJW476twuArtBOOavSV7oyu1q0ootP6cSbUlXOigCZ2IFzopzpuqLcEwdvJsm7StQKFbtOVW5w_giNZhDo3cqGxh3JKhC8iF0EJg25V6HDmPSGROnz0TnfeWHDm1mZGGT1n7SLZz8afpRaP0283xZ6CtmdTlw71AObzOrjv21Z2hwhPacJ3KsVcGvCseeHsmNatGVsubKxRbcLjWuYW4jX5AovbRWLXM-eJCqPq8h7G-3gjbAoM11H5fFLfVg7sZLrr0lHodWwX2BeKkEEF73jNKf4s9dRJ2-ECpzohWU8g2NySncl4GhWQzg4dQWvd7nABJE8a5jFUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qfCiHjdMT3fMYLFqhT6M42KRSdy_D8tJu4qSYHYYehpy45JtrMKHVJ7pOqjCXDSQggOvzHnEzDh0LiB9oztyby-ihTcT9AQAodaNAX9qWzRt-RmzS6BU4E1H3ohR1yQbFtVsw-BvwoIhKwr4fnUqoO-yY7caV2VUMNDxP9Q2eDc6GW47tMy3rknMnmNyk-TDln-HNMDEm1RhRykSse9j4GEqdoprb8gq0qzF1UVnj_JrEH3lat9KxcRbCvkGLx61sh46n74VeaGUGoFBxDNfRjMqPL_k7DhuzPrP500G8XHqzQM1CmKSXLiokzvKMPr5gKClZ_v9aol2QRmtQF5LXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YIDyl1tqTIuxHNN5dqfwxjUBbY2waFxZWCWJXom2SmGcheiYt3sV8AsG_zSxGJIOLdUJXB-8U04v9jj18NLsy2OjUGGYWWA7-jJS-4gV79dWRhG_b4r9epfmJj6CzAcPPRV3FOfnEKDiHmWRc3_y3fo8gIiOUn6PNE5IH0KFKDUwVAxnN6RLz8F-u5Zo82HTfKe04Vf4uS_AdWFAe2gP2wzHLdwBN4n9ffCzDIyQzS6JNMzaT8NhZ4yhgniYF325ZDl_LrlVv3g0HaQ6OHtrD9dNZJBFS4XxI_xtiPFrLC9HlW0H7NTDigJONpSM86zCq56H0MaNjbbUdUO1yIVr6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K6T8GGIpOrAxuXh4CMV5OueyyxzftQ8GQ0qdRxXU0bJI9Uj51g0immdGhMc4c0PiglqcX7OzFixxsgJQAoHtn4uYcPwE5kMqKp05t4VA9yVUdHcHyIOS_c_R7l7Hx8LMP4xItZSZbHu8d6GfUGaY8hCIjWkJxYptkmlyOEVI5DjuA4HEqgrAb04pcrqKvmxH2nu7VSWJrMfebZzRnRWTex6xB98Tb0x5H4AYU7HZ9ta5LcmrilBKAVgpOz8twPBP5nWIpDEUqDq9PgfB6Fu6FVULDmiSPVg0ip8E_9CeA3GiABHNIJG-H25CB0JhEmm-XuYXzG4mZ4c5ixLbqVwPNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=iCX4pmo7aQwoRu_MKeIKhrmAMduMTF0pLcgDquAQAg1PfZYwkzujXDjgt0DYYgcd2hfp1sgZJdZrmTJWp5tR3THx3e0-mhIuYuNSb6VYlRKXxL6FKG4btyVTuuMCTqvWF65rR9GQJcDKt69KEdCFxwk3_-qRq5jPiU90emxVvoFDmpWXa3TZlG61ZF1zGyN27j76n-3UleCpKLFkO3mM3xlPDoksTxm0sRBPdPlDvbM099LoxmyczORonxYgFHRvydW15Scn7SvTAiGgDB-ltU7xsE9rW4sJqYIb0TAGnB10TQM4Y8HH6GclQEwtBJOt6ECnTlgS7JxiVjyIxWifLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=iCX4pmo7aQwoRu_MKeIKhrmAMduMTF0pLcgDquAQAg1PfZYwkzujXDjgt0DYYgcd2hfp1sgZJdZrmTJWp5tR3THx3e0-mhIuYuNSb6VYlRKXxL6FKG4btyVTuuMCTqvWF65rR9GQJcDKt69KEdCFxwk3_-qRq5jPiU90emxVvoFDmpWXa3TZlG61ZF1zGyN27j76n-3UleCpKLFkO3mM3xlPDoksTxm0sRBPdPlDvbM099LoxmyczORonxYgFHRvydW15Scn7SvTAiGgDB-ltU7xsE9rW4sJqYIb0TAGnB10TQM4Y8HH6GclQEwtBJOt6ECnTlgS7JxiVjyIxWifLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEamnk03m00GoXCnbvTjnyoujO3rPv4QPYoONC8O34UhlYEOFrh1NrVpneuAbUJpiaZXepcvz0JqZvfhgXy2iuH_KfWrLaGEnBroPbZ8z0uNFwyh7yiNZ-521Iu1iOFRb8HayPbKdFOJM9YGieZgD2C7J85ARFz3Qc3bEvteH858F0grKfVAQ_2wmB5s3mjdzRw1Id3aAtICjOE-EWdpMY9Kvc4RSO3m7EnTjAd4tyLoTHqVgPQYFIDMwv3OlK9DoaR3y7hO4I5IMjOoXsXAiAI7ZlzffYwF-_dJIYrBIcCpd1I-LT0Q2q-o0FbZBHH6CFeDgqYHGa0sVfGzZTLSyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
